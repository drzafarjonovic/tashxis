"""
Supabase Postgres ulanishi (asyncpg).

Dizayn tamoyili: DB ixtiyoriy. DATABASE_URL bo'sh bo'lsa yoki ulanish
muvaffaqiyatsiz bo'lsa, bot baribir to'liq ishlaydi (graceful degradation).
asyncpg faqat funksiyalar ichida import qilinadi — shu sabab modulni
asyncpg o'rnatilmagan muhitda ham import qilish mumkin.
"""

from __future__ import annotations

import asyncio
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


def _ssl_context():
    """Supabase uchun SSL konteksti (sertifikat tekshiruvisiz)."""
    import ssl as _ssl
    ctx = _ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = _ssl.CERT_NONE
    return ctx


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

    # 1-bosqich: ulanish
    try:
        _pool = await asyncpg.create_pool(
            dsn=settings.database_url,
            min_size=1,
            max_size=5,
            command_timeout=15,
            timeout=20,
            ssl=_ssl_context(),
            statement_cache_size=0,   # Supabase pooler (transaction mode) mosligi
        )
    except Exception as exc:  # noqa: BLE001
        logger.error(
            "DB ULANISHI muvaffaqiyatsiz (%s: %s) — bot DB'siz davom etadi. "
            "Eslatma: Railway IPv6'ni qo'llamaydi — Supabase 'Connection Pooler' "
            "(IPv4, aws-0-...pooler.supabase.com:6543) URL'ini ishlating.",
            type(exc).__name__, exc,
        )
        _pool = None
        return

    # 2-bosqich: sxema (alohida — ulanish saqlanib qoladi, sxema xatosi DB'ni o'chirmaydi)
    try:
        await _ensure_schema()
        logger.info("Supabase Postgres ulanishi tayyor (sxema qo'llandi).")
    except Exception as exc:  # noqa: BLE001
        logger.error(
            "DB ulandi, ammo SXEMA qo'llashda xato (%s: %s). Jadvallar mavjud bo'lsa "
            "hisobotlar baribir ishlaydi.",
            type(exc).__name__, exc,
        )


async def _ensure_schema() -> None:
    """Sxemani bayonotlarga bo'lib, har birini alohida qo'llaydi (pooler-xavfsiz)."""
    if _pool is None:
        return
    schema_sql = _SCHEMA_PATH.read_text(encoding="utf-8")
    statements = [s.strip() for s in schema_sql.split(";") if s.strip()]
    async with _pool.acquire() as conn:
        for stmt in statements:
            try:
                await conn.execute(stmt)
            except Exception as exc:  # noqa: BLE001
                logger.warning("Sxema bayonoti o'tkazib yuborildi (%s): %.60s",
                               type(exc).__name__, stmt.replace("\n", " "))


async def diagnose() -> str:
    """Jonli ulanishni sinaydi va aniq natija/xatoni ODDIY MATN sifatida qaytaradi."""
    if not settings.db_enabled:
        return "DATABASE_URL berilmagan."
    try:
        import asyncpg
    except ImportError:
        return "asyncpg o'rnatilmagan."

    if _pool is not None:
        try:
            val = await asyncio.wait_for(_pool.fetchval("SELECT 1"), timeout=12)
            return f"✅ DB ulangan va ishlayapti (SELECT 1 = {val})."
        except Exception as exc:  # noqa: BLE001
            return f"⚠️ Pool mavjud, lekin so'rov xato berdi:\n{type(exc).__name__}: {exc}"

    # Pool yo'q — yangi ulanish sinab, aniq xatoni qaytaramiz (qat'iy timeout bilan)
    async def _try_connect():
        conn = await asyncpg.connect(
            dsn=settings.database_url,
            timeout=12,
            ssl=_ssl_context(),
            statement_cache_size=0,
        )
        try:
            return await conn.fetchval("SELECT 1")
        finally:
            await conn.close()

    try:
        val = await asyncio.wait_for(_try_connect(), timeout=15)
        return f"✅ Yangi ulanish muvaffaqiyatli (SELECT 1 = {val}). Botni qayta deploy qiling."
    except asyncio.TimeoutError:
        return (
            "❌ Ulanish vaqti tugadi (timeout, 15s). Ehtimol host/port noto'g'ri yoki "
            "tarmoq yopiq. Pooler URL ni tekshiring: "
            "aws-0-...pooler.supabase.com:6543"
        )
    except Exception as exc:  # noqa: BLE001
        return (
            f"❌ Ulanib bo'lmadi:\n{type(exc).__name__}: {exc}\n\n"
            "Tekshiring: pooler URL, user 'postgres.<ref>', parol to'g'riligi."
        )


async def close_db() -> None:
    global _pool
    if _pool is not None:
        await _pool.close()
        _pool = None
        logger.info("DB ulanishi yopildi.")
