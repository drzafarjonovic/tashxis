from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from locales.strings import t
from medical import DISEASES_BY_CATEGORY

# Ma'lumotnoma bo'limlari tartibi
CATALOG_CATEGORIES = [
    "tooth", "pulp", "periapical", "periodontal", "mucosa",
    "jaw", "tmj", "trauma", "dentition", "salivary",
]

# Joylashuvni aniqlash bosqichlari uchun variantlar
LOCATION_OPTIONS = {
    "jaw": ["upper", "lower", "unknown"],
    "side": ["right", "left", "unknown"],
    "type": ["incisor", "canine", "premolar", "molar", "unknown"],
}

DISEASES_PER_PAGE = 8


def lang_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek",  callback_data="lang_uz"),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en"),
        ]
    ])


def main_keyboard(lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=t("start_btn", lang))],
            [KeyboardButton(text=t("reference_btn", lang))],
            [KeyboardButton(text=t("help_btn", lang))],
        ],
        resize_keyboard=True,
    )


def category_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("loc_tooth",     lang), callback_data="cat_tooth")],
        [InlineKeyboardButton(text=t("loc_gum",       lang), callback_data="cat_periodontal")],
        [InlineKeyboardButton(text=t("loc_mucosa",    lang), callback_data="cat_mucosa")],
        [InlineKeyboardButton(text=t("loc_jaw",       lang), callback_data="cat_jaw")],
        [InlineKeyboardButton(text=t("loc_tmj",       lang), callback_data="cat_tmj")],
        [InlineKeyboardButton(text=t("loc_trauma",    lang), callback_data="cat_trauma")],
        [InlineKeyboardButton(text=t("loc_dentition", lang), callback_data="cat_dentition")],
        [InlineKeyboardButton(text=t("loc_salivary",  lang), callback_data="cat_salivary")],
    ])


def localization_keyboard(step: str, lang: str) -> InlineKeyboardMarkup:
    """Joylashuvni aniqlash bosqichi uchun variantlar klaviaturasi."""
    rows = []
    for opt in LOCATION_OPTIONS.get(step, []):
        rows.append([
            InlineKeyboardButton(
                text=t(f"loc_opt_{opt}", lang),
                callback_data=f"loc_{step}_{opt}",
            )
        ])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def demo_age_keyboard(lang: str) -> InlineKeyboardMarkup:
    rows = [
        [
            InlineKeyboardButton(text="5–12", callback_data="dg_age_5-12"),
            InlineKeyboardButton(text="13–18", callback_data="dg_age_13-18"),
        ],
        [
            InlineKeyboardButton(text="19–40", callback_data="dg_age_19-40"),
            InlineKeyboardButton(text="41–65", callback_data="dg_age_41-65"),
        ],
        [InlineKeyboardButton(text="65+", callback_data="dg_age_65+")],
        [InlineKeyboardButton(text=t("demo_skip", lang), callback_data="dg_age_skip")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def demo_sex_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=t("demo_sex_male", lang), callback_data="dg_sex_male"),
            InlineKeyboardButton(text=t("demo_sex_female", lang), callback_data="dg_sex_female"),
        ],
        [InlineKeyboardButton(text=t("demo_skip", lang), callback_data="dg_sex_skip")],
    ])


def yes_no_keyboard(lang: str, question_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=t("yes_btn", lang), callback_data=f"ans_yes_{question_id}"),
            InlineKeyboardButton(text=t("no_btn",  lang), callback_data=f"ans_no_{question_id}"),
        ]
    ])


# ─────────────────────────────────────────────────────────────────
#  KASALLIKLAR MA'LUMOTNOMASI (katalog)
# ─────────────────────────────────────────────────────────────────

def catalog_categories_keyboard(lang: str) -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(text=t(f"ref_cat_{cat}", lang), callback_data=f"rc_{cat}_0")]
        for cat in CATALOG_CATEGORIES
    ]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def catalog_diseases_keyboard(category: str, page: int, lang: str) -> InlineKeyboardMarkup:
    diseases = DISEASES_BY_CATEGORY.get(category, [])
    start = page * DISEASES_PER_PAGE
    chunk = diseases[start:start + DISEASES_PER_PAGE]

    rows = [
        [InlineKeyboardButton(text=d.get_name(lang), callback_data=f"rd_{d.id}")]
        for d in chunk
    ]

    nav = []
    if page > 0:
        nav.append(InlineKeyboardButton(text=t("ref_prev", lang), callback_data=f"rc_{category}_{page - 1}"))
    if start + DISEASES_PER_PAGE < len(diseases):
        nav.append(InlineKeyboardButton(text=t("ref_next", lang), callback_data=f"rc_{category}_{page + 1}"))
    if nav:
        rows.append(nav)

    rows.append([InlineKeyboardButton(text=t("ref_back_to_categories", lang), callback_data="rhome")])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def disease_card_keyboard(category: str, lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("ref_back_to_list", lang), callback_data=f"rc_{category}_0")],
        [InlineKeyboardButton(text=t("ref_back_to_categories", lang), callback_data="rhome")],
    ])
