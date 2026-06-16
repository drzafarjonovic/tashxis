"""
Admin audit/hisobot uchun ma'lumotlar bazasi so'rovlari (faqat o'qish).

Barcha funksiyalar xavfsiz: DB o'chiq bo'lsa bo'sh natija qaytaradi.
Vaqt oralig'i [start, end) (UTC) bo'yicha ishlaydi.
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Any, Dict, List, Optional

from db.database import get_pool

logger = logging.getLogger(__name__)


def _display_name(row: Dict[str, Any]) -> str:
    parts = [row.get("first_name") or "", row.get("last_name") or ""]
    name = " ".join(p for p in parts if p).strip()
    return name or "—"


async def overview(start: datetime, end: datetime) -> Dict[str, Any]:
    """Davr bo'yicha umumiy ko'rsatkichlar."""
    pool = get_pool()
    if pool is None:
        return {}
    try:
        async with pool.acquire() as conn:
            total_users = await conn.fetchval("SELECT count(*) FROM bot_users") or 0
            new_users = await conn.fetchval(
                "SELECT count(*) FROM bot_users WHERE created_at >= $1 AND created_at < $2",
                start, end,
            ) or 0
            total_sessions = await conn.fetchval(
                "SELECT count(*) FROM diagnosis_sessions WHERE started_at >= $1 AND started_at < $2",
                start, end,
            ) or 0
            active_users = await conn.fetchval(
                "SELECT count(DISTINCT telegram_id) FROM diagnosis_sessions "
                "WHERE started_at >= $1 AND started_at < $2",
                start, end,
            ) or 0
            avg_q = await conn.fetchval(
                "SELECT avg(question_count) FROM diagnosis_sessions "
                "WHERE started_at >= $1 AND started_at < $2",
                start, end,
            )
            avg_conf = await conn.fetchval(
                "SELECT avg(top1_conf) FROM diagnosis_sessions "
                "WHERE started_at >= $1 AND started_at < $2",
                start, end,
            )
            uncertain = await conn.fetchval(
                "SELECT count(*) FROM diagnosis_sessions "
                "WHERE started_at >= $1 AND started_at < $2 AND uncertain = TRUE",
                start, end,
            ) or 0

            top_diseases = await conn.fetch(
                """
                SELECT top1_disease AS disease, count(*) AS cnt
                FROM diagnosis_sessions
                WHERE started_at >= $1 AND started_at < $2 AND top1_disease IS NOT NULL
                GROUP BY top1_disease ORDER BY cnt DESC LIMIT 10
                """,
                start, end,
            )
            top_categories = await conn.fetch(
                """
                SELECT category, count(*) AS cnt
                FROM diagnosis_sessions
                WHERE started_at >= $1 AND started_at < $2 AND category IS NOT NULL
                GROUP BY category ORDER BY cnt DESC
                """,
                start, end,
            )
            by_age = await conn.fetch(
                """
                SELECT COALESCE(age_group, '—') AS age_group, count(*) AS cnt
                FROM diagnosis_sessions
                WHERE started_at >= $1 AND started_at < $2
                GROUP BY age_group ORDER BY cnt DESC
                """,
                start, end,
            )
            by_sex = await conn.fetch(
                """
                SELECT COALESCE(sex, '—') AS sex, count(*) AS cnt
                FROM diagnosis_sessions
                WHERE started_at >= $1 AND started_at < $2
                GROUP BY sex ORDER BY cnt DESC
                """,
                start, end,
            )
        return {
            "total_users": total_users,
            "new_users": new_users,
            "total_sessions": total_sessions,
            "active_users": active_users,
            "avg_questions": float(avg_q) if avg_q is not None else 0.0,
            "avg_confidence": float(avg_conf) if avg_conf is not None else 0.0,
            "uncertain": uncertain,
            "top_diseases": [(r["disease"], r["cnt"]) for r in top_diseases],
            "top_categories": [(r["category"], r["cnt"]) for r in top_categories],
            "by_age": [(r["age_group"], r["cnt"]) for r in by_age],
            "by_sex": [(r["sex"], r["cnt"]) for r in by_sex],
        }
    except Exception as exc:  # noqa: BLE001
        logger.error("overview xatoligi: %s", exc)
        return {}


async def activity_series(start: datetime, end: datetime) -> List[tuple]:
    """Kunlik sessiyalar soni (grafik uchun): [(date_str, count), ...]."""
    pool = get_pool()
    if pool is None:
        return []
    try:
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                """
                SELECT to_char(date_trunc('day', started_at), 'YYYY-MM-DD') AS d,
                       count(*) AS cnt
                FROM diagnosis_sessions
                WHERE started_at >= $1 AND started_at < $2
                GROUP BY 1 ORDER BY 1
                """,
                start, end,
            )
        return [(r["d"], r["cnt"]) for r in rows]
    except Exception as exc:  # noqa: BLE001
        logger.error("activity_series xatoligi: %s", exc)
        return []


async def sessions_detail(start: datetime, end: datetime, limit: int = 5000) -> List[Dict[str, Any]]:
    """Davrdagi har bir sessiya (foydalanuvchi ma'lumoti bilan) — audit uchun."""
    pool = get_pool()
    if pool is None:
        return []
    try:
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                """
                SELECT s.session_id, s.started_at, s.telegram_id,
                       u.first_name, u.last_name, u.username,
                       s.lang, s.category, s.age_group, s.sex, s.location,
                       s.question_count, s.top1_disease, s.top1_conf,
                       s.top2_disease, s.top3_disease, s.uncertain
                FROM diagnosis_sessions s
                LEFT JOIN bot_users u ON u.telegram_id = s.telegram_id
                WHERE s.started_at >= $1 AND s.started_at < $2
                ORDER BY s.started_at DESC
                LIMIT $3
                """,
                start, end, limit,
            )
        result = []
        for r in rows:
            d = dict(r)
            d["name"] = _display_name(d)
            result.append(d)
        return result
    except Exception as exc:  # noqa: BLE001
        logger.error("sessions_detail xatoligi: %s", exc)
        return []


async def answers_for_sessions(session_ids: List[int]) -> Dict[int, List[Dict[str, Any]]]:
    """Sessiyalar bo'yicha barcha savol-javoblar (audit): {session_id: [{step,question_id,answer}]}."""
    pool = get_pool()
    if pool is None or not session_ids:
        return {}
    try:
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                """
                SELECT session_id, step, question_id, answer
                FROM session_answers
                WHERE session_id = ANY($1::bigint[])
                ORDER BY session_id, step
                """,
                session_ids,
            )
        out: Dict[int, List[Dict[str, Any]]] = {}
        for r in rows:
            out.setdefault(r["session_id"], []).append(
                {"step": r["step"], "question_id": r["question_id"], "answer": r["answer"]}
            )
        return out
    except Exception as exc:  # noqa: BLE001
        logger.error("answers_for_sessions xatoligi: %s", exc)
        return {}


async def users_list(limit: int = 5000) -> List[Dict[str, Any]]:
    """Barcha obunachilar ro'yxati (sessiyalar soni bilan)."""
    pool = get_pool()
    if pool is None:
        return []
    try:
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                """
                SELECT u.telegram_id, u.first_name, u.last_name, u.username, u.lang,
                       u.created_at, u.last_seen,
                       count(s.session_id) AS sessions
                FROM bot_users u
                LEFT JOIN diagnosis_sessions s ON s.telegram_id = u.telegram_id
                GROUP BY u.telegram_id, u.first_name, u.last_name, u.username, u.lang,
                         u.created_at, u.last_seen
                ORDER BY sessions DESC, u.last_seen DESC
                LIMIT $1
                """,
                limit,
            )
        result = []
        for r in rows:
            d = dict(r)
            d["name"] = _display_name(d)
            result.append(d)
        return result
    except Exception as exc:  # noqa: BLE001
        logger.error("users_list xatoligi: %s", exc)
        return []


async def user_report(telegram_id: int) -> Dict[str, Any]:
    """Bitta obunachi bo'yicha to'liq individual hisobot."""
    pool = get_pool()
    if pool is None:
        return {}
    try:
        async with pool.acquire() as conn:
            urow = await conn.fetchrow(
                "SELECT telegram_id, first_name, last_name, username, lang, created_at, last_seen "
                "FROM bot_users WHERE telegram_id = $1",
                telegram_id,
            )
            srows = await conn.fetch(
                """
                SELECT session_id, started_at, lang, category, age_group, sex, location,
                       question_count, top1_disease, top1_conf, top2_disease, top3_disease, uncertain
                FROM diagnosis_sessions
                WHERE telegram_id = $1
                ORDER BY started_at DESC
                """,
                telegram_id,
            )
        sessions = [dict(r) for r in srows]
        answers = await answers_for_sessions([s["session_id"] for s in sessions])
        user = dict(urow) if urow else {"telegram_id": telegram_id}
        user["name"] = _display_name(user)
        return {"user": user, "sessions": sessions, "answers": answers}
    except Exception as exc:  # noqa: BLE001
        logger.error("user_report xatoligi: %s", exc)
        return {}
