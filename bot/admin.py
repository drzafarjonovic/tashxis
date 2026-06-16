"""
Admin paneli — bot obunachilari bo'yicha audit va hisobotlar.

Faqat ADMIN_ID egasi uchun. Hisobotlar matn + grafik (PNG) + PDF + Excel
ko'rinishida beriladi: kunlik / haftalik / oylik / umumiy / ixtiyoriy interval,
shuningdek har bir obunachi bo'yicha individual hisobot.

Router asosiy routerdan OLDIN ulanadi (main.py) — shunda /admin va admin
callback/holatlari to'g'ri ushlanadi.
"""

from __future__ import annotations

import asyncio
import logging
from datetime import datetime, timedelta, timezone

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    BufferedInputFile,
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from app.config import settings
from bot.states import AdminFSM
from db import reports
from db.database import is_enabled as db_enabled
from reporting import exporters

logger = logging.getLogger(__name__)
admin_router = Router()


def _is_admin(user_id: int) -> bool:
    return settings.admin_enabled and user_id == settings.admin_id


def _admin_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📊 Bugun", callback_data="adr_daily"),
            InlineKeyboardButton(text="📅 Hafta", callback_data="adr_weekly"),
            InlineKeyboardButton(text="🗓 Oy", callback_data="adr_monthly"),
        ],
        [InlineKeyboardButton(text="📈 Umumiy (barcha vaqt)", callback_data="adr_all")],
        [InlineKeyboardButton(text="🗓 Interval (sana oralig'i)", callback_data="adr_custom")],
        [InlineKeyboardButton(text="👤 Obunachi bo'yicha hisobot", callback_data="adr_user")],
        [InlineKeyboardButton(text="👥 Obunachilar ro'yxati (Excel)", callback_data="adr_users")],
    ])


@admin_router.message(Command("admin"))
async def cmd_admin(message: Message, state: FSMContext):
    if not _is_admin(message.from_user.id):
        # Jim qolish o'rniga aniq sabab (debug uchun)
        if not settings.admin_enabled:
            await message.answer(
                "⚠️ ADMIN_ID sozlanmagan (yoki o'qilmadi).\n"
                "Railway'da ADMIN_ID o'zgaruvchisini qo'shing va qayta deploy qiling.\n"
                "ID ni bilish uchun: /myid"
            )
        else:
            await message.answer(
                "⛔ Bu buyruq faqat admin uchun.\n"
                f"Sizning ID: <code>{message.from_user.id}</code>\n"
                "Agar bu siz bo'lsangiz — ADMIN_ID ni shu ID ga to'g'rilang (/myid)."
            )
        return
    await state.set_state(None)
    if not db_enabled():
        await message.answer(
            "⚠️ Ma'lumotlar bazasi ulanmagan — hisobotlar uchun ma'lumot yo'q.\n"
            "Railway'da DATABASE_URL (Supabase <b>Connection Pooler</b>, IPv4) to'g'ri "
            "ekanini tekshiring va deploy loglarida 'ulanish tayyor' yozuvini qarang.\n"
            "Holatni tekshirish: /myid"
        )
        return
    await message.answer("🛠 <b>Admin paneli — hisobotlar</b>\n\nKerakli hisobotni tanlang:",
                         reply_markup=_admin_menu())


# ─────────────────────────────────────────────────────────────────
#  DAVR HISOBOTLARI
# ─────────────────────────────────────────────────────────────────

def _summary_text(title: str, ov: dict) -> str:
    if not ov:
        return f"{title}\n\nMa'lumot yo'q yoki DB sozlanmagan."
    lines = [
        f"🛠 <b>{title}</b>", "",
        f"👥 Jami obunachilar: <b>{ov.get('total_users', 0)}</b>",
        f"🆕 Yangi (davr): <b>{ov.get('new_users', 0)}</b>",
        f"🩺 Sessiyalar (davr): <b>{ov.get('total_sessions', 0)}</b>",
        f"🙋 Faol foydalanuvchilar: <b>{ov.get('active_users', 0)}</b>",
        f"❓ O'rtacha savol: <b>{round(ov.get('avg_questions', 0.0), 1)}</b>",
        f"📊 O'rtacha ishonch: <b>{round(ov.get('avg_confidence', 0.0), 2)}</b>",
        f"🤔 Aniqlanmagan: <b>{ov.get('uncertain', 0)}</b>",
    ]
    td = ov.get("top_diseases", [])
    if td:
        lines += ["", "🏆 <b>Eng ko'p tashxislar:</b>"]
        for did, cnt in td[:5]:
            lines.append(f"  • {exporters.disease_name(did)} — {cnt}")
    tc = ov.get("top_categories", [])
    if tc:
        lines += ["", "📂 <b>Bo'limlar:</b> " + ", ".join(f"{c}={n}" for c, n in tc[:6])]
    return "\n".join(lines)


async def _send_period_report(message: Message, title: str, start: datetime, end: datetime):
    note = await message.answer("⏳ Hisobot tayyorlanmoqda...")

    ov = await reports.overview(start, end)
    series = await reports.activity_series(start, end)
    sessions = await reports.sessions_detail(start, end)
    answers = await reports.answers_for_sessions([s["session_id"] for s in sessions])
    users = await reports.users_list()

    await message.answer(_summary_text(title, ov))

    # Grafik + PDF + Excel (sinxron generatsiya — alohida threadда)
    chart = await asyncio.to_thread(
        exporters.build_overview_chart, series, ov.get("top_diseases", []), title
    )
    pdf = await asyncio.to_thread(exporters.build_pdf_report, title, ov, chart)
    excel = await asyncio.to_thread(
        exporters.build_excel_report, title, ov, sessions, answers, users
    )

    if chart:
        await message.answer_photo(BufferedInputFile(chart, filename="grafik.png"),
                                   caption="📈 Faollik va tashxislar grafigi")
    if pdf:
        await message.answer_document(BufferedInputFile(pdf, filename="hisobot.pdf"))
    if excel:
        await message.answer_document(
            BufferedInputFile(excel, filename="audit.xlsx"),
            caption="📋 To'liq audit (sessiyalar, savol-javoblar, obunachilar)",
        )
    if not (chart or pdf or excel):
        await message.answer(
            "ℹ️ Fayl generatsiyasi kutubxonalari mavjud emas — faqat matnli hisobot berildi."
        )
    try:
        await note.delete()
    except Exception:  # noqa: BLE001
        pass


def _now() -> datetime:
    return datetime.now(timezone.utc)


@admin_router.callback_query(F.data == "adr_daily")
async def cb_daily(call: CallbackQuery, state: FSMContext):
    if not _is_admin(call.from_user.id):
        return
    await call.answer()
    now = _now()
    start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    await _send_period_report(call.message, "Kunlik hisobot (bugun)", start, now)


@admin_router.callback_query(F.data == "adr_weekly")
async def cb_weekly(call: CallbackQuery, state: FSMContext):
    if not _is_admin(call.from_user.id):
        return
    await call.answer()
    now = _now()
    await _send_period_report(call.message, "Haftalik hisobot (7 kun)", now - timedelta(days=7), now)


@admin_router.callback_query(F.data == "adr_monthly")
async def cb_monthly(call: CallbackQuery, state: FSMContext):
    if not _is_admin(call.from_user.id):
        return
    await call.answer()
    now = _now()
    await _send_period_report(call.message, "Oylik hisobot (30 kun)", now - timedelta(days=30), now)


@admin_router.callback_query(F.data == "adr_all")
async def cb_all(call: CallbackQuery, state: FSMContext):
    if not _is_admin(call.from_user.id):
        return
    await call.answer()
    start = datetime(2020, 1, 1, tzinfo=timezone.utc)
    await _send_period_report(call.message, "Umumiy hisobot (barcha vaqt)", start, _now())


@admin_router.callback_query(F.data == "adr_custom")
async def cb_custom(call: CallbackQuery, state: FSMContext):
    if not _is_admin(call.from_user.id):
        return
    await call.answer()
    await call.message.answer(
        "🗓 Sana oralig'ini yuboring (YYYY-MM-DD YYYY-MM-DD):\n"
        "Masalan: <code>2026-06-01 2026-06-16</code>\n\nBekor qilish: /admin"
    )
    await state.set_state(AdminFSM.awaiting_interval)


@admin_router.callback_query(F.data == "adr_user")
async def cb_user(call: CallbackQuery, state: FSMContext):
    if not _is_admin(call.from_user.id):
        return
    await call.answer()
    await call.message.answer(
        "👤 Obunachining Telegram ID sini yuboring (raqam):\n\nBekor qilish: /admin"
    )
    await state.set_state(AdminFSM.awaiting_user_id)


@admin_router.callback_query(F.data == "adr_users")
async def cb_users(call: CallbackQuery, state: FSMContext):
    if not _is_admin(call.from_user.id):
        return
    await call.answer()
    users = await reports.users_list()
    if not users:
        await call.message.answer("Obunachilar topilmadi (yoki DB sozlanmagan).")
        return
    excel = await asyncio.to_thread(
        exporters.build_excel_report, "Obunachilar ro'yxati", {}, [], {}, users
    )
    text = f"👥 Jami obunachilar: <b>{len(users)}</b>\n\nEng faollar:\n"
    for u in users[:15]:
        uname = f"@{u['username']}" if u.get("username") else "—"
        text += f"  • {u.get('name','—')} ({uname}, id {u['telegram_id']}) — {u.get('sessions',0)} sessiya\n"
    await call.message.answer(text)
    if excel:
        await call.message.answer_document(BufferedInputFile(excel, filename="obunachilar.xlsx"))


# ─────────────────────────────────────────────────────────────────
#  ADMIN MATNLI KIRITISHLAR (interval / user_id)
# ─────────────────────────────────────────────────────────────────

@admin_router.message(AdminFSM.awaiting_interval, F.text)
async def on_interval(message: Message, state: FSMContext):
    if not _is_admin(message.from_user.id):
        return
    parts = (message.text or "").split()
    try:
        start = datetime.strptime(parts[0], "%Y-%m-%d").replace(tzinfo=timezone.utc)
        end = datetime.strptime(parts[1], "%Y-%m-%d").replace(tzinfo=timezone.utc) + timedelta(days=1)
    except (IndexError, ValueError):
        await message.answer("❌ Format noto'g'ri. Masalan: <code>2026-06-01 2026-06-16</code>")
        return
    await state.set_state(None)
    title = f"Interval hisoboti ({parts[0]} … {parts[1]})"
    await _send_period_report(message, title, start, end)


@admin_router.message(AdminFSM.awaiting_user_id, F.text)
async def on_user_id(message: Message, state: FSMContext):
    if not _is_admin(message.from_user.id):
        return
    raw = (message.text or "").strip().lstrip("@")
    if not raw.isdigit():
        await message.answer("❌ Telegram ID raqam bo'lishi kerak. Qaytadan yuboring yoki /admin.")
        return
    await state.set_state(None)
    tid = int(raw)
    note = await message.answer("⏳ Obunachi hisoboti tayyorlanmoqda...")

    data = await reports.user_report(tid)
    if not data or not data.get("user"):
        await message.answer("Bu ID bo'yicha obunachi topilmadi.")
        return

    user = data["user"]
    sessions = data["sessions"]
    answers = data["answers"]

    uname = f"@{user['username']}" if user.get("username") else "—"
    text = (
        f"👤 <b>{user.get('name','—')}</b>\n"
        f"🆔 <code>{user.get('telegram_id')}</code> | {uname} | til: {user.get('lang','—')}\n"
        f"🩺 Sessiyalar: <b>{len(sessions)}</b>\n\n"
    )
    for s in sessions[:10]:
        text += (
            f"• #{s.get('session_id')} — {s.get('category','—')} → "
            f"{exporters.disease_name(s.get('top1_disease'))} "
            f"({round(float(s.get('top1_conf') or 0), 2)})\n"
        )
    await message.answer(text)

    pdf = await asyncio.to_thread(exporters.build_user_pdf, user, sessions, answers)
    excel = await asyncio.to_thread(exporters.build_user_excel, user, sessions, answers)
    if pdf:
        await message.answer_document(BufferedInputFile(pdf, filename=f"obunachi_{tid}.pdf"))
    if excel:
        await message.answer_document(BufferedInputFile(excel, filename=f"obunachi_{tid}.xlsx"))
    try:
        await note.delete()
    except Exception:  # noqa: BLE001
        pass
