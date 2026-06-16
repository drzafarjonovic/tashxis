"""
Markaziy konfiguratsiya — barcha sozlamalar bitta joyda.

Sozlamalar muhit o'zgaruvchilaridan (environment variables) o'qiladi.
Railway / Supabase'da bu qiymatlar dashboard orqali beriladi,
lokal ishlashda esa `.env` faylidan yuklanadi.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


def _get_bool(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in ("1", "true", "yes", "on")


@dataclass(frozen=True)
class Settings:
    # Telegram
    bot_token: str

    # Ma'lumotlar bazasi (Supabase Postgres). Bo'sh bo'lsa — bot DB'siz ishlaydi.
    database_url: str

    # AI integratsiyasi. v1.1 da o'chirilgan (False). v2.0 da yoqiladi.
    ai_enabled: bool

    # AI kaliti (ai_enabled=True bo'lganda kerak)
    groq_api_key: str

    # Admin bilan aloqa (ixtiyoriy). ADMIN_ID — admin Telegram ID si (relay uchun).
    admin_id: int
    admin_username: str

    # Health-check web server porti (Railway PORT ni avtomatik beradi)
    port: int

    # Log darajasi
    log_level: str

    @property
    def db_enabled(self) -> bool:
        return bool(self.database_url)

    @property
    def admin_enabled(self) -> bool:
        return self.admin_id > 0


def _get_int(name: str, default: int = 0) -> int:
    raw = (os.getenv(name) or "").strip()
    try:
        return int(raw)
    except (TypeError, ValueError):
        return default


def _load_settings() -> Settings:
    bot_token = os.getenv("BOT_TOKEN", "").strip()
    if not bot_token:
        raise ValueError(
            "BOT_TOKEN topilmadi! Railway env yoki .env faylida BOT_TOKEN ni o'rnating."
        )

    return Settings(
        bot_token=bot_token,
        database_url=os.getenv("DATABASE_URL", "").strip(),
        ai_enabled=_get_bool("AI_ENABLED", default=False),
        groq_api_key=(os.getenv("GROQ_API_KEY") or os.getenv("AI_API_KEY") or "").strip(),
        admin_id=_get_int("ADMIN_ID", 0),
        admin_username=os.getenv("ADMIN_USERNAME", "").strip().lstrip("@"),
        port=int(os.getenv("PORT", "8080")),
        log_level=os.getenv("LOG_LEVEL", "INFO").strip().upper(),
    )


settings = _load_settings()

# Orqaga moslik uchun (eski kod BOT_TOKEN ni to'g'ridan import qilgan bo'lishi mumkin)
BOT_TOKEN = settings.bot_token
