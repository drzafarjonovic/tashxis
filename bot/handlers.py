"""
Bot handlerlari — to'liq Akinator oqimi.

Oqim:
  /start  →  til tanlash  →  lokatsiya (triage)  →  ketma-ket savollar  →  natija
"""

import logging
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.states import DiagnosticFSM
from bot.keyboards import (
    lang_keyboard, main_keyboard,
    category_keyboard, yes_no_keyboard,
)
from locales.strings import t
from engine.akinator import (
    get_next_question, should_stop_early, get_diagnosis,
    MIN_QUESTIONS, MAX_QUESTIONS,
)
from ai.groq_ai import explain_diagnosis

logger = logging.getLogger(__name__)
router = Router()


# ─────────────────────────────────────────────────────────────────
#  /start
# ─────────────────────────────────────────────────────────────────

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        t("welcome", "uz"),   # boshlang'ich ko'rsatma — har doim uz
        reply_markup=lang_keyboard(),
        parse_mode="Markdown",
    )
    await state.set_state(DiagnosticFSM.lang)


# ─────────────────────────────────────────────────────────────────
#  TIL TANLASH
# ─────────────────────────────────────────────────────────────────

@router.callback_query(DiagnosticFSM.lang, F.data.startswith("lang_"))
async def cb_lang(call: CallbackQuery, state: FSMContext):
    await call.answer()
    lang = call.data.split("_")[1]   # uz | ru | en
    await state.update_data(lang=lang, symptoms={}, asked=[], category=None)
    await call.message.edit_text(t("lang_set", lang))
    await call.message.answer(
        t("welcome", lang),
        reply_markup=main_keyboard(lang),
        parse_mode="Markdown",
    )
    await state.set_state(None)   # asosiy menyu


# ─────────────────────────────────────────────────────────────────
#  ASOSIY TUGMALAR
# ─────────────────────────────────────────────────────────────────

@router.message(F.text)
async def text_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uz")

    start_labels = [t("start_btn", l) for l in ("uz", "ru", "en")]
    help_labels  = [t("help_btn",  l) for l in ("uz", "ru", "en")]

    if message.text in start_labels:
        await _start_triage(message, state, lang)
    elif message.text in help_labels:
        await message.answer(t("help_text", lang), parse_mode="Markdown")
    else:
        current = await state.get_state()
        if current is None:
            await message.answer(t("unknown_command", lang))


async def _start_triage(message: Message, state: FSMContext, lang: str):
    await state.update_data(symptoms={}, asked=[])
    await message.answer(
        t("choose_location", lang),
        reply_markup=category_keyboard(lang),
    )
    await state.set_state(DiagnosticFSM.category)


# ─────────────────────────────────────────────────────────────────
#  TRIAGE — KATEGORIA TANLASH
# ─────────────────────────────────────────────────────────────────

CATEGORY_MAP = {
    "cat_tooth":       "tooth",
    "cat_periodontal": "periodontal",
    "cat_mucosa":      "mucosa",
    "cat_jaw":         "jaw",
}

# Tish tanlansa qaysi sub-kategoriyadan boshlash kerakligi — aqlli yo'naltirish
TOOTH_START_CATEGORIES = ["tooth", "pulp", "periapical"]


@router.callback_query(DiagnosticFSM.category, F.data.startswith("cat_"))
async def cb_category(call: CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    lang = data.get("lang", "uz")

    raw_cat = CATEGORY_MAP.get(call.data, "tooth")

    # "tooth" tanlansa avval tish simptomlaridan boshlaymiz,
    # savol oqimi dinamik ravishda pulp/periapical ga o'tadi
    await state.update_data(
        category=raw_cat,
        symptoms={},
        asked=[],
        q_count=0,
    )
    await call.message.edit_text(f"✅ {call.message.reply_markup.inline_keyboard[0][0].text if False else ''}")
    await _ask_next(call.message, state, lang, edit=False)
    await state.set_state(DiagnosticFSM.questioning)


# ─────────────────────────────────────────────────────────────────
#  SAVOL-JAVOB OQIMI
# ─────────────────────────────────────────────────────────────────

@router.callback_query(DiagnosticFSM.questioning, F.data.startswith("ans_"))
async def cb_answer(call: CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    lang      = data.get("lang", "uz")
    symptoms  = data.get("symptoms", {})
    asked     = data.get("asked", [])
    category  = data.get("category", "tooth")
    q_count   = data.get("q_count", 0)

    # Javobni parse qilish: "ans_yes_spontaneous_pain" → yes / spontaneous_pain
    parts = call.data.split("_", 2)   # ["ans", "yes", "spontaneous_pain"]
    answer  = parts[1]                 # "yes" | "no"
    qid     = parts[2] if len(parts) > 2 else ""

    # Simptomni yozish
    symptoms[qid] = (answer == "yes")
    asked.append(qid)
    q_count += 1

    # Dinamik kategoria o'zgartirish (tooth → pulp/periapical)
    category = _update_category(category, symptoms)

    await state.update_data(
        symptoms=symptoms,
        asked=asked,
        q_count=q_count,
        category=category,
    )

    # Xavf sinovlari — darhol to'xtatish
    if _is_emergency(symptoms):
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer(t("red_flag_alert", lang), parse_mode="Markdown")
        await state.clear()
        return

    # Erta to'xtatish yoki maksimum savolga yetish
    if q_count >= MAX_QUESTIONS or should_stop_early(category, symptoms, q_count):
        await call.message.edit_reply_markup(reply_markup=None)
        await _show_result(call.message, state, lang, symptoms, category)
        return

    # Keyingi savol
    await call.message.edit_reply_markup(reply_markup=None)
    await _ask_next(call.message, state, lang, edit=False)


def _update_category(category: str, symptoms: dict) -> str:
    """
    Tish bo'limida spontan og'riq yoki tunda og'riq paydo bo'lsa — pulpga,
    perkussiya og'rig'i yoki tish devital bo'lsa — periapicalga o'tamiz.
    """
    if category != "tooth":
        return category
    if symptoms.get("spontaneous_pain") or symptoms.get("night_pain"):
        return "pulp"
    if symptoms.get("percussion_pain") or symptoms.get("no_sensitivity") or symptoms.get("tooth_discoloration"):
        return "periapical"
    return "tooth"


def _is_emergency(symptoms: dict) -> bool:
    return bool(symptoms.get("high_fever") and symptoms.get("jaw_swelling")) or \
           bool(symptoms.get("fever") and symptoms.get("trismus") and symptoms.get("jaw_swelling"))


async def _ask_next(message: Message, state: FSMContext, lang: str, edit: bool = False):
    data     = await state.get_data()
    category = data.get("category", "tooth")
    asked    = data.get("asked", [])
    q_count  = data.get("q_count", 0)

    q = get_next_question(category, data.get("symptoms", {}), asked, lang)
    if q is None:
        # Barcha savollar tugadi
        await _show_result(
            message, state, lang,
            data.get("symptoms", {}),
            category,
        )
        return

    text = (
        f"*{t('question_prefix', lang)} {q_count + 1}:*\n\n"
        f"{q['text']}"
    )
    await message.answer(
        text,
        reply_markup=yes_no_keyboard(lang, q["id"]),
        parse_mode="Markdown",
    )


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

    result = get_diagnosis(category, symptoms, lang)
    diagnosis = result["diagnosis"]
    confidence = int(result["confidence"] * 100)
    alternatives = result.get("alternatives", [])
    red_flags = result.get("red_flags", [])

    # AI tushuntirishi
    ai_text = explain_diagnosis(diagnosis, symptoms, lang)

    # Natija matni
    lines = [
        t("result_header", lang),
        "",
        f"🏷 *{t('top_diagnosis', lang)}:* {diagnosis}",
        f"📊 {'Ehtimollik' if lang == 'uz' else 'Вероятность' if lang == 'ru' else 'Confidence'}: {confidence}%",
    ]

    if alternatives:
        alt_text = ", ".join(alternatives)
        lines += ["", f"🔄 *{t('alternatives_label', lang)}:* {alt_text}"]

    if ai_text:
        lines += ["", f"{t('ai_explanation_label', lang)}", ai_text]

    if red_flags:
        lines += ["", t("red_flags_label", lang)]
        for rf in red_flags:
            lines.append(f"  • {rf}")

    lines += ["", t("disclaimer", lang), "", t("restart_hint", lang)]

    await message.answer("\n".join(lines), parse_mode="Markdown")
    await state.clear()
