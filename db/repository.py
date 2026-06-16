"""
Ma'lumotlar bazasi bilan ishlash (repository).

Barcha funksiyalar xavfsiz: DB o'chiq yoki xato bo'lsa, jim ravishda
o'tkazib yuboriladi va bot ishlashda davom etadi.
"""

from __future__ import annotations

import json
import logging
from typing import Any, Dict, List, Optional

from db.database import get_pool

logger = logging.getLogger(__name__)


async def upsert_user(telegram_id: int, lang: str) -> None:
    """Foydalanuvchini yaratadi yoki tilini/last_seen'ini yangilaydi."""
    pool = get_pool()
    if pool is None:
        return
    try:
        async with pool.acquire() as conn:
            await conn.execute(
                """
                INSERT INTO bot_users (telegram_id, lang)
                VALUES ($1, $2)
                ON CONFLICT (telegram_id)
                DO UPDATE SET lang = EXCLUDED.lang, last_seen = now()
                """,
                telegram_id,
                lang,
            )
    except Exception as exc:  # noqa: BLE001
        logger.error("upsert_user xatoligi: %s", exc)


async def save_diagnosis(
    telegram_id: int,
    lang: str,
    category: str,
    result: Dict[str, Any],
    symptoms: Dict[str, bool],
) -> None:
    """Tashxis natijasini saqlaydi."""
    pool = get_pool()
    if pool is None:
        return
    try:
        async with pool.acquire() as conn:
            await conn.execute(
                """
                INSERT INTO diagnoses
                    (telegram_id, lang, category, disease_id, diagnosis,
                     confidence, uncertain, symptoms, alternatives)
                VALUES ($1, $2, $3, $4, $5, $6, $7, $8::jsonb, $9::jsonb)
                """,
                telegram_id,
                lang,
                category,
                result.get("disease_id"),
                result.get("diagnosis"),
                float(result.get("confidence", 0.0)),
                bool(result.get("uncertain", False)),
                json.dumps(symptoms, ensure_ascii=False),
                json.dumps(result.get("alternatives", []), ensure_ascii=False),
            )
    except Exception as exc:  # noqa: BLE001
        logger.error("save_diagnosis xatoligi: %s", exc)



# ════════════════════════════════════════════════════════════════
#  V2.0 — Clinical Data Collection Platform
# ════════════════════════════════════════════════════════════════

async def save_session(
    telegram_id: int,
    lang: str,
    category: str,
    result: Dict[str, Any],
    symptoms: Dict[str, bool],
    asked: List[str],
    demo: Optional[Any] = None,
    location: Optional[Dict[str, str]] = None,
) -> Optional[int]:
    """
    To'liq diagnostik sessiyani saqlaydi: diagnosis_sessions + session_answers,
    legacy diagnoses sammari va disease_statistics. session_id qaytaradi (yoki None).
    Barchasi xavfsiz — DB o'chiq bo'lsa None qaytadi.
    """
    pool = get_pool()
    if pool is None:
        return None

    age_group = getattr(demo, "age_group", None) if demo else None
    sex = getattr(demo, "sex", None) if demo else None
    location = location or {}
    alts = result.get("alternatives", []) or []
    top2 = alts[0] if len(alts) > 0 else None
    top3 = alts[1] if len(alts) > 1 else None

    try:
        async with pool.acquire() as conn:
            async with conn.transaction():
                session_id = await conn.fetchval(
                    """
                    INSERT INTO diagnosis_sessions
                        (telegram_id, lang, age_group, sex, category, location,
                         question_count, top1_disease, top1_conf, top2_disease,
                         top3_disease, uncertain, completed_at)
                    VALUES ($1,$2,$3,$4,$5,$6::jsonb,$7,$8,$9,$10,$11,$12, now())
                    RETURNING session_id
                    """,
                    telegram_id, lang, age_group, sex, category,
                    json.dumps(location, ensure_ascii=False),
                    len(asked or []),
                    result.get("disease_id"),
                    float(result.get("confidence", 0.0)),
                    top2, top3,
                    bool(result.get("uncertain", False)),
                )

                for step, qid in enumerate(asked or []):
                    await conn.execute(
                        """
                        INSERT INTO session_answers (session_id, question_id, answer, step)
                        VALUES ($1, $2, $3, $4)
                        """,
                        session_id, qid, bool(symptoms.get(qid, False)), step,
                    )

                await conn.execute(
                    """
                    INSERT INTO diagnoses
                        (telegram_id, lang, category, disease_id, diagnosis,
                         confidence, uncertain, symptoms, alternatives, age_group, sex, location)
                    VALUES ($1,$2,$3,$4,$5,$6,$7,$8::jsonb,$9::jsonb,$10,$11,$12::jsonb)
                    """,
                    telegram_id, lang, category,
                    result.get("disease_id"), result.get("diagnosis"),
                    float(result.get("confidence", 0.0)),
                    bool(result.get("uncertain", False)),
                    json.dumps(symptoms, ensure_ascii=False),
                    json.dumps(alts, ensure_ascii=False),
                    age_group, sex, json.dumps(location, ensure_ascii=False),
                )

                if result.get("disease_id"):
                    await conn.execute(
                        """
                        INSERT INTO disease_statistics (disease_id, predicted_count)
                        VALUES ($1, 1)
                        ON CONFLICT (disease_id)
                        DO UPDATE SET predicted_count = disease_statistics.predicted_count + 1,
                                      updated_at = now()
                        """,
                        result["disease_id"],
                    )
            return session_id
    except Exception as exc:  # noqa: BLE001
        logger.error("save_session xatoligi: %s", exc)
        return None


async def save_doctor_feedback(
    session_id: int,
    final_diagnosis: Optional[str],
    confirmed: Optional[bool],
    notes: Optional[str] = None,
) -> None:
    """Shifokor tasdig'ini saqlaydi (kalibrlash va prior yangilash uchun)."""
    pool = get_pool()
    if pool is None:
        return
    try:
        async with pool.acquire() as conn:
            async with conn.transaction():
                await conn.execute(
                    """
                    INSERT INTO doctor_feedback (session_id, final_diagnosis, confirmed, notes)
                    VALUES ($1, $2, $3, $4)
                    """,
                    session_id, final_diagnosis, confirmed, notes,
                )
                if final_diagnosis:
                    await conn.execute(
                        """
                        INSERT INTO disease_statistics (disease_id, confirmed_count)
                        VALUES ($1, 1)
                        ON CONFLICT (disease_id)
                        DO UPDATE SET confirmed_count = disease_statistics.confirmed_count + 1,
                                      updated_at = now()
                        """,
                        final_diagnosis,
                    )
    except Exception as exc:  # noqa: BLE001
        logger.error("save_doctor_feedback xatoligi: %s", exc)


async def load_learned_priors() -> Dict[str, float]:
    """priors jadvalidan o'rganilgan multiplikatorlarni yuklaydi (Self-Learning)."""
    pool = get_pool()
    if pool is None:
        return {}
    try:
        async with pool.acquire() as conn:
            rows = await conn.fetch("SELECT disease_id, multiplier FROM priors")
            return {r["disease_id"]: float(r["multiplier"]) for r in rows}
    except Exception as exc:  # noqa: BLE001
        logger.error("load_learned_priors xatoligi: %s", exc)
        return {}
