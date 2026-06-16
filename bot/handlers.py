"""
Bot handlerlari.

Oqimlar:
  1. Tashxis: /start → til → muammo joyi → (joylashuv) → savollar → natija
  2. Ma'lumotnoma: bo'lim → kasallik → to'liq ma'lumot
"""

from __future__ import annotations

import html
import logging

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.keyboards import (
    catalog_categories_keyboard,
    catalog_diseases_keyboard,
    category_keyboard,
    disease_card_keyboard,
    lang_keyboard,
    localization_keyboard,
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
from medical import ALL_DISEASES, DISEASES_BY_CATEGORY

logger = logging.getLogger(__name__)
router = Router()

# Tashxisni aniqlashtirish uchun joylashuv bosqichlari (kategoriyaga qarab)
LOCATION_FLOW = {
    "tooth": ["jaw", "side", "type"],
    "trauma": ["jaw", "side", "type"],
    "periodontal": ["jaw", "side"],
    "jaw": ["jaw", "side"],
}

# Joylashuv qiymatlari uchun matnli yorliqlar (natijada ko'rsatish uchun)
_LOC_LABELS = {
    "jaw": {
        "upper": {"uz": "yuqori jag'", "ru": "верхняя челюсть", "en": "upper jaw"},
        "lower": {"uz": "pastki jag'", "ru": "нижняя челюсть", "en": "lower jaw"},
    },
    "side": {
        "right": {"uz": "o'ng tomon", "ru": "правая сторона", "en": "right side"},
        "left": {"uz": "chap tomon", "ru": "левая сторона", "en": "left side"},
    },
    "type": {
        "incisor": {"uz": "kurak tish", "ru": "резец", "en": "incisor"},
        "canine": {"uz": "qoziq tish", "ru": "клык", "en": "canine"},
        "premolar": {"uz": "kichik oziq tish", "ru": "малый коренной", "en": "premolar"},
        "molar": {"uz": "katta oziq tish", "ru": "большой коренной", "en": "molar"},
    },
}

# id → Disease (ma'lumotnoma uchun tez qidiruv)
_DISEASE_BY_ID = {d.id: d for d in ALL_DISEASES}


def _esc(text: str) -> str:
    """HTML xavfsiz qilish (dinamik matnlar uchun)."""
    return html.escape(str(text))


def _location_text(location: dict, lang: str) -> str:
    """Joylashuv qiymatlaridan o'qiladigan matn tuzadi ('unknown' o'tkazib yuboriladi)."""
    if not location:
        return ""
    parts = []
    for step in ("jaw", "side", "type"):
        value = location.get(step)
        if value and value != "unknown":
            label = _LOC_LABELS.get(step, {}).get(value, {})
            txt = label.get(lang) or label.get("uz")
            if txt:
                parts.append(txt)
    return ", ".join(parts)


def _append_info_blocks(lines: list, lang: str, description: str,
                        symptoms_text: str, differential: str, treatment: str) -> None:
    """Kasallik haqidagi 4 ta ma'lumot blokini matn satrlariga qo'shadi."""
    if description:
        lines += ["", f"📖 <b>{_esc(t('about_disease_label', lang))}</b>", _esc(description)]
    if symptoms_text:
        lines += ["", f"🔬 <b>{_esc(t('symptoms_label', lang))}</b>", _esc(symptoms_text)]
    if differential:
        lines += ["", f"🔀 <b>{_esc(t('differential_label', lang))}</b>", _esc(differential)]
    if treatment:
        lines += ["", f"💊 <b>{_esc(t('treatment_label', lang))}</b>", _esc(treatment)]


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
    ref_labels = {t("reference_btn", l) for l in ("uz", "ru", "en")}

    if message.text in start_labels:
        await _start_triage(message, state, lang)
    elif message.text in ref_labels:
        await message.answer(
            t("ref_choose_category", lang),
            reply_markup=catalog_categories_keyboard(lang),
        )
    elif message.text in help_labels:
        await message.answer(t("help_text", lang))
    else:
        current = await state.get_state()
        if current is None:
            await message.answer(t("unknown_command", lang))


async def _start_triage(message: Message, state: FSMContext, lang: str):
    await state.update_data(symptoms={}, asked=[], q_count=0, category=None, location={})
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
    await state.update_data(
        category=category, symptoms={}, asked=[], q_count=0, location={}
    )

    await call.message.edit_reply_markup(reply_markup=None)

    steps = LOCATION_FLOW.get(category, [])
    if steps:
        await state.update_data(loc_steps=steps, loc_index=0)
        await _ask_localization(call.message, lang, steps[0])
        await state.set_state(DiagnosticFSM.localizing)
    else:
        await _ask_next(call.message, state, lang)
        await state.set_state(DiagnosticFSM.questioning)


# ─────────────────────────────────────────────────────────────────
#  JOYLASHUVNI ANIQLASH
# ─────────────────────────────────────────────────────────────────

async def _ask_localization(message: Message, lang: str, step: str):
    text = (
        f"<b>{_esc(t('loc_step_prefix', lang))}</b>\n\n"
        f"{_esc(t(f'loc_q_{step}', lang))}"
    )
    await message.answer(text, reply_markup=localization_keyboard(step, lang))


@router.callback_query(DiagnosticFSM.localizing, F.data.startswith("loc_"))
async def cb_localize(call: CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    lang = data.get("lang", "uz")

    # "loc_<step>_<value>"
    parts = call.data.split("_", 2)
    if len(parts) < 3:
        return
    step, value = parts[1], parts[2]

    location = data.get("location", {})
    location[step] = value
    loc_steps = data.get("loc_steps", [])
    loc_index = data.get("loc_index", 0) + 1
    await state.update_data(location=location, loc_index=loc_index)

    await call.message.edit_reply_markup(reply_markup=None)

    if loc_index < len(loc_steps):
        await _ask_localization(call.message, lang, loc_steps[loc_index])
    else:
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

    data = await state.get_data()
    location = data.get("location", {})

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

    area = _location_text(location, lang)
    if area:
        lines += [f"🦷 <b>{_esc(t('loc_area_label', lang))}:</b> {_esc(area)}"]

    alternatives = result.get("alternatives", [])
    if alternatives:
        alt_text = ", ".join(_esc(a) for a in alternatives)
        lines += ["", f"🔄 <b>{_esc(t('alternatives_label', lang))}:</b> {alt_text}"]

    _append_info_blocks(
        lines, lang,
        result.get("description", ""),
        result.get("symptoms_text", ""),
        result.get("differential", ""),
        result.get("treatment", ""),
    )

    explanation = result.get("explanation", "")
    if explanation and not (result.get("description") or result.get("treatment")):
        # Boy ma'lumot bo'lmasa, qisqa avtomatik izohga qaytamiz
        lines += ["", t("ai_explanation_label", lang), _esc(explanation)]

    red_flags = result.get("red_flags", [])
    if red_flags:
        lines += ["", t("red_flags_label", lang)]
        lines += [f"  • {_esc(rf)}" for rf in red_flags]

    lines += ["", t("disclaimer", lang), "", t("restart_hint", lang)]

    await message.answer("\n".join(lines))
    await state.clear()


# ─────────────────────────────────────────────────────────────────
#  KASALLIKLAR MA'LUMOTNOMASI (katalog)
# ─────────────────────────────────────────────────────────────────

@router.callback_query(F.data == "rhome")
async def cb_ref_home(call: CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    lang = data.get("lang", "uz")
    await call.message.edit_text(
        t("ref_choose_category", lang),
        reply_markup=catalog_categories_keyboard(lang),
    )


@router.callback_query(F.data.startswith("rc_"))
async def cb_ref_category(call: CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    lang = data.get("lang", "uz")

    # "rc_<category>_<page>"
    parts = call.data.split("_")
    category = parts[1] if len(parts) > 1 else "tooth"
    page = int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 0

    title = f"{t(f'ref_cat_{category}', lang)}\n\n{t('ref_choose_disease', lang)}"
    await call.message.edit_text(
        title,
        reply_markup=catalog_diseases_keyboard(category, page, lang),
    )


@router.callback_query(F.data.startswith("rd_"))
async def cb_ref_disease(call: CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    lang = data.get("lang", "uz")

    disease_id = call.data[len("rd_"):]
    disease = _DISEASE_BY_ID.get(disease_id)
    if disease is None:
        await call.message.answer(t("session_expired", lang))
        return

    # Ma'lumotnoma kategoriyasini aniqlash (orqaga qaytish uchun)
    catalog_cat = disease.category
    if catalog_cat not in DISEASES_BY_CATEGORY:
        catalog_cat = "tooth"

    lines = [f"🩺 <b>{_esc(disease.get_name(lang))}</b>"]
    _append_info_blocks(
        lines, lang,
        disease.get_description(lang),
        disease.get_symptoms_text(lang),
        disease.get_differential(lang),
        disease.get_treatment(lang),
    )
    if disease.red_flags:
        lines += ["", t("red_flags_label", lang)]
        lines += [f"  • {_esc(rf)}" for rf in disease.red_flags]
    lines += ["", t("disclaimer", lang)]

    await call.message.edit_text(
        "\n".join(lines),
        reply_markup=disease_card_keyboard(catalog_cat, lang),
    )


# ─────────────────────────────────────────────────────────────────
#  ESKIRGAN / MOS KELMAYDIGAN TUGMALAR (fallback)
# ─────────────────────────────────────────────────────────────────

@router.callback_query()
async def cb_stale(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uz")
    await call.answer()
    await call.message.answer(t("session_expired", lang))
