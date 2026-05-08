from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from locales.strings import t


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
            [KeyboardButton(text=t("help_btn", lang))],
        ],
        resize_keyboard=True,
    )


def category_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("loc_tooth",  lang), callback_data="cat_tooth")],
        [InlineKeyboardButton(text=t("loc_gum",    lang), callback_data="cat_periodontal")],
        [InlineKeyboardButton(text=t("loc_mucosa", lang), callback_data="cat_mucosa")],
        [InlineKeyboardButton(text=t("loc_jaw",    lang), callback_data="cat_jaw")],
    ])


def yes_no_keyboard(lang: str, question_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=t("yes_btn", lang), callback_data=f"ans_yes_{question_id}"),
            InlineKeyboardButton(text=t("no_btn",  lang), callback_data=f"ans_no_{question_id}"),
        ]
    ])
