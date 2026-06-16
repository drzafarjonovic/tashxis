import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand, BotCommandScopeChat
from aiohttp import web

from app.config import settings
from app.version import APP_NAME, VERSION
from bot.admin import admin_router
from bot.handlers import router
from db.database import close_db, init_db

logging.basicConfig(
    level=getattr(logging, settings.log_level, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


async def health_check(request: web.Request) -> web.Response:
    return web.Response(text=f"OK — {APP_NAME} v{VERSION} ishlayapti!")


async def start_web() -> web.AppRunner:
    app = web.Application()
    app.router.add_get("/", health_check)
    app.router.add_get("/health", health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", settings.port)
    await site.start()
    logger.info("Web server port %s da ishga tushdi.", settings.port)
    return runner


async def set_commands(bot: Bot) -> None:
    await bot.set_my_commands([
        BotCommand(command="start", description="Boshlash / Начать / Start"),
        BotCommand(command="about", description="Bot haqida / О боте / About"),
        BotCommand(command="help", description="Yordam / Помощь / Help"),
        BotCommand(command="myid", description="Mening ID im / Мой ID / My ID"),
    ])
    # Admin uchun qo'shimcha buyruqlar (faqat admin chatida ko'rinadi)
    if settings.admin_enabled:
        try:
            await bot.set_my_commands(
                [
                    BotCommand(command="admin", description="Admin paneli — hisobotlar"),
                    BotCommand(command="dbtest", description="DB ulanishini tekshirish"),
                    BotCommand(command="reply", description="Foydalanuvchiga javob: /reply <id> matn"),
                    BotCommand(command="myid", description="Mening ID im"),
                    BotCommand(command="start", description="Boshlash"),
                ],
                scope=BotCommandScopeChat(chat_id=settings.admin_id),
            )
        except Exception as exc:  # noqa: BLE001
            logger.warning("Admin buyruqlarini o'rnatib bo'lmadi: %s", exc)


async def main() -> None:
    logger.info(
        "%s v%s ishga tushmoqda... (AI_ENABLED=%s, ADMIN_ID=%s)",
        APP_NAME, VERSION, settings.ai_enabled,
        settings.admin_id if settings.admin_enabled else "(sozlanmagan)",
    )

    runner = await start_web()
    await init_db()

    # Self-Learning: DB'dagi o'rganilgan prior overrides'ni yuklash (bo'lsa)
    try:
        from db.repository import load_learned_priors
        from engine import priors as _priors
        learned = await load_learned_priors()
        if learned:
            _priors.LEARNED_PRIOR_OVERRIDES.update(learned)
            logger.info("O'rganilgan prior overrides yuklandi: %d ta kasallik.", len(learned))
    except Exception as exc:  # noqa: BLE001
        logger.warning("Prior overrides yuklash o'tkazib yuborildi: %s", exc)

    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(admin_router)  # admin paneli — asosiy routerdan oldin
    dp.include_router(router)

    await set_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    logger.info("Polling boshlandi.")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await close_db()
        await runner.cleanup()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot to'xtatildi.")
