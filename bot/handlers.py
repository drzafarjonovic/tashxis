"""
Bot handlerlari — Akinator oqimi.

Oqim:
  /start → til tanlash → muammo joyi (triage) → ketma-ket savollar → natija
"""

from __future__ import annotations

import html
import logging

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.keyboards import (
    category_keyboard,
    lang_keyboard,
    main_keyboard,
    yes_no_keyboard,
)
from bot.states import DiagnosticFSM
from db import repository
from domain.symptoms import question_text
from engine import (
    CATEGORY_MAP,
    MAX_QUESTIONS,
    diagnose,
    get_next_question,
    is_emergency,
    should_stop,
)
from locales.strings import t

logger = logging.getLogger(__name__)
router = Router()


def _esc(text: str) -> str:
    """HTML xavfsiz qilish (dinamik matnlar uchun)."""
    return html.escape(str(text))


# ─────────────────────────────────────────────────────────────────
#  /start  va  /help
# ─────────────────────────────────────────────────────────────────

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        t("welcome", "uz"),
        reply_markup=lang_keyboard(),
    )
    await state.set_state(DiagnosticFSM.lang)


@router.message(Command("help"))
async def cmd_help(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uz")
    await message.answer(t("help_text", lang))


# ─────────────────────────────────────────────────────────────────
#  TIL TANLASH
# ─────────────────────────────────────────────────────────────────

@router.callback_query(DiagnosticFSM.lang, F.data.startswith("lang_"))
async def cb_lang(call: CallbackQuery, state: FSMContext):
    await call.answer()
    lang = call.data.split("_")[1]  # uz | ru | en
    await state.update_data(lang=lang)

    await repository.upsert_user(call.from_user.id, lang)

    await call.message.edit_text(t("lang_set", lang))
    await call.message.answer(
        t("menu_hint", lang),
        reply_markup=main_keyboard(lang),
    )
    await state.set_state(None)  # asosiy menyu


# ─────────────────────────────────────────────────────────────────
#  ASOSIY MATN TUGMALARI
# ─────────────────────────────────────────────────────────────────

@router.message(F.text)
async def text_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uz")

    start_labels = {t("start_btn", l) for l in ("uz", "ru", "en")}
    help_labels = {t("help_btn", l) for l in ("uz", "ru", "en")}

    if message.text in start_labels:
        await _start_triage(message, state, lang)
    elif message.text in help_labels:
        await message.answer(t("help_text", lang))
    else:
        current = await state.get_state()
        if current is None:
            await message.answer(t("unknown_command", lang))


async def _start_triage(message: Message, state: FSMContext, lang: str):
    await state.update_data(symptoms={}, asked=[], q_count=0, category=None)
    await message.answer(
        t("choose_location", lang),
        reply_markup=category_keyboard(lang),
    )
    await state.set_state(DiagnosticFSM.category)


# ─────────────────────────────────────────────────────────────────
#  TRIAGE — KATEGORIYA TANLASH
# ─────────────────────────────────────────────────────────────────

@router.callback_query(DiagnosticFSM.category, F.data.startswith("cat_"))
async def cb_category(call: CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    lang = data.get("lang", "uz")

    category = CATEGORY_MAP.get(call.data, "tooth")
    await state.update_data(category=category, symptoms={}, asked=[], q_count=0)

    await call.message.edit_reply_markup(reply_markup=None)
    await _ask_next(call.message, state, lang)
    await state.set_state(DiagnosticFSM.questioning)


# ─────────────────────────────────────────────────────────────────
#  SAVOL-JAVOB OQIMI
# ─────────────────────────────────────────────────────────────────

@router.callback_query(DiagnosticFSM.questioning, F.data.startswith("ans_"))
async def cb_answer(call: CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    lang = data.get("lang", "uz")
    symptoms = data.get("symptoms", {})
    asked = data.get("asked", [])
    category = data.get("category", "tooth")
    q_count = data.get("q_count", 0)

    # "ans_yes_spontaneous_pain" → yes / spontaneous_pain
    parts = call.data.split("_", 2)
    answer = parts[1]
    qid = parts[2] if len(parts) > 2 else ""
    if not qid:
        return

    symptoms[qid] = answer == "yes"
    if qid not in asked:
        asked.append(qid)
    q_count += 1

    await state.update_data(
        symptoms=symptoms, asked=asked, q_count=q_count, category=category
    )

    await call.message.edit_reply_markup(reply_markup=None)

    # Xavfli holat — darhol to'xtatish
    if is_emergency(symptoms):
        await call.message.answer(t("red_flag_alert", lang))
        await state.clear()
        return

    # Erta to'xtatish yoki maksimumga yetish
    if q_count >= MAX_QUESTIONS or should_stop(category, symptoms, q_count):
        await _show_result(call.message, state, lang, symptoms, category)
        return

    await _ask_next(call.message, state, lang)


async def _ask_next(message: Message, state: FSMContext, lang: str):
    data = await state.get_data()
    category = data.get("category", "tooth")
    asked = data.get("asked", [])
    symptoms = data.get("symptoms", {})
    q_count = data.get("q_count", 0)

    qid = get_next_question(category, symptoms, asked)
    if qid is None:
        await _show_result(message, state, lang, symptoms, category)
        return

    text = (
        f"<b>{_esc(t('question_prefix', lang))} {q_count + 1}:</b>\n\n"
        f"{_esc(question_text(qid, lang))}"
    )
    await message.answer(text, reply_markup=yes_no_keyboard(lang, qid))


# ─────────────────────────────────────────────────────────────────
#  NATIJANI KO'RSATISH
# ─────────────────────────────────────────────────────────────────

async def _show_result(
    message: Message,
    state: FSMContext,
    lang: str,
    symptoms: dict,
    category: str,
):
    await message.answer(t("analyzing", lang))

    result = diagnose(category, symptoms, lang)

    # DB ga yozish (xavfsiz — DB o'chiq bo'lsa o'tkazib yuboriladi)
    await repository.save_diagnosis(
        telegram_id=message.chat.id,
        lang=lang,
        category=category,
        result=result,
        symptoms=symptoms,
    )

    lines = [t("result_header", lang), ""]

    if result.get("uncertain"):
        lines += [t("uncertain_result", lang), ""]

    confidence = int(result.get("confidence", 0.0) * 100)
    lines += [
        f"🏷 <b>{_esc(t('top_diagnosis', lang))}:</b> {_esc(result['diagnosis'])}",
        f"📊 {_esc(t('confidence_label', lang))}: {confidence}%",
    ]

    alternatives = result.get("alternatives", [])
    if alternatives:
        alt_text = ", ".join(_esc(a) for a in alternatives)
        lines += ["", f"🔄 <b>{_esc(t('alternatives_label', lang))}:</b> {alt_text}"]

    explanation = result.get("explanation", "")
    if explanation:
        lines += ["", t("ai_explanation_label", lang), _esc(explanation)]

    red_flags = result.get("red_flags", [])
    if red_flags:
        lines += ["", t("red_flags_label", lang)]
        lines += [f"  • {_esc(rf)}" for rf in red_flags]

    lines += ["", t("disclaimer", lang), "", t("restart_hint", lang)]

    await message.answer("\n".join(lines))
    await state.clear()


# ─────────────────────────────────────────────────────────────────
#  ESKIRGAN / MOS KELMAYDIGAN TUGMALAR (fallback)
# ─────────────────────────────────────────────────────────────────

@router.callback_query()
async def cb_stale(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uz")
    await call.answer()
    await call.message.answer(t("session_expired", lang))
