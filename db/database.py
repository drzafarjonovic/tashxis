"""
Supabase Postgres ulanishi (asyncpg).

Dizayn tamoyili: DB ixtiyoriy. DATABASE_URL bo'sh bo'lsa yoki ulanish
muvaffaqiyatsiz bo'lsa, bot baribir to'liq ishlaydi (graceful degradation).
asyncpg faqat init_db() ichida import qilinadi — shu sabab modulni
asyncpg o'rnatilmagan muhitda ham import qilish mumkin.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

from app.config import settings

logger = logging.getLogger(__name__)

_pool = None  # asyncpg.Pool | None

_SCHEMA_PATH = Path(__file__).with_name("schema.sql")


def get_pool():
    """Joriy ulanish pulini qaytaradi (yoki None)."""
    return _pool


def is_enabled() -> bool:
    return _pool is not None


async def init_db() -> None:
    """Ulanish pulini yaratadi va sxemani qo'llaydi. Xatoda bot DB'siz davom etadi."""
    global _pool

    if not settings.db_enabled:
        logger.info("DATABASE_URL berilmagan — bot DB'siz ishlaydi.")
        return

    try:
        import asyncpg  # lokal import — ixtiyoriy bog'liqlik
    except ImportError:
        logger.warning("asyncpg o'rnatilmagan — DB o'chirildi.")
        return

    try:
        _pool = await asyncpg.create_pool(
            dsn=settings.database_url,
            min_size=1,
            max_size=5,
            command_timeout=10,
        )
        await _ensure_schema()
        logger.info("Supabase Postgres ulanishi tayyor.")
    except Exception as exc:  # noqa: BLE001
        logger.error("DB ulanishi muvaffaqiyatsiz (%s) — bot DB'siz davom etadi.", exc)
        _pool = None


async def _ensure_schema() -> None:
    if _pool is None:
        return
    schema_sql = _SCHEMA_PATH.read_text(encoding="utf-8")
    async with _pool.acquire() as conn:
        await conn.execute(schema_sql)


async def close_db() -> None:
    global _pool
    if _pool is not None:
        await _pool.close()
        _pool = None
        logger.info("DB ulanishi yopildi.")
