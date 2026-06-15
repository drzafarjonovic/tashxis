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
