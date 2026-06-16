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

    # Supabase SSL talab qiladi. Sertifikat tekshiruvisiz shifrlangan ulanish
    # (pooler/host nomi mosligi muammolarini oldini oladi).
    import ssl as _ssl
    ssl_ctx = _ssl.create_default_context()
    ssl_ctx.check_hostname = False
    ssl_ctx.verify_mode = _ssl.CERT_NONE

    try:
        _pool = await asyncpg.create_pool(
            dsn=settings.database_url,
            min_size=1,
            max_size=5,
            command_timeout=15,
            timeout=20,                 # ulanish kutish vaqti
            ssl=ssl_ctx,                # Supabase uchun SSL
            statement_cache_size=0,     # Supabase pooler (transaction mode) mosligi
        )
        await _ensure_schema()
        logger.info("Supabase Postgres ulanishi tayyor.")
    except Exception as exc:  # noqa: BLE001
        logger.error(
            "DB ulanishi muvaffaqiyatsiz (%s: %s) — bot DB'siz davom etadi. "
            "Eslatma: Railway IPv6'ni qo'llamaydi — Supabase 'Connection Pooler' "
            "(IPv4) URL'ini ishlating.",
            type(exc).__name__, exc,
        )
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
