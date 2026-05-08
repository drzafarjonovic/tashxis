from aiogram.fsm.state import StatesGroup, State


class DiagnosticFSM(StatesGroup):
    lang        = State()   # Til tanlash
    category    = State()   # Muammo joyi (triage)
    questioning = State()   # Akinator savollari
