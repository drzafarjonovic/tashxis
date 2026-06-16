from aiogram.fsm.state import StatesGroup, State


class DiagnosticFSM(StatesGroup):
    lang         = State()   # Til tanlash
    demographics = State()   # Yosh / jins (Demographic Engine)
    category     = State()   # Muammo joyi (triage)
    localizing   = State()   # Joylashuvni aniqlash (jag'/tomon/tish turi)
    questioning  = State()   # Akinator savollari
    contact      = State()   # Admin bilan aloqa (xabar yozish)


class AdminFSM(StatesGroup):
    awaiting_user_id   = State()   # Individual hisobot uchun user_id kutilmoqda
    awaiting_interval  = State()   # Interval (sana oralig'i) kutilmoqda
