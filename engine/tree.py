"""
Triage — foydalanuvchi tugmasini ichki kategoriyaga bog'lash va
xavfli holatlarni (red flags) erta aniqlash.

Eslatma: "tooth" tanlanganda barcha tish kasalliklari bitta diagnostik
guruhda ko'rib chiqiladi (medical.DIAGNOSTIC_GROUPS), shuning uchun
alohida pulp/periapical yo'naltirish kerak emas — Akinator info-gain
orqali ajratuvchi savollarni o'zi tanlaydi.
"""

from __future__ import annotations

from typing import Dict

# Foydalanuvchi tugmasi → ichki kategoriya
CATEGORY_MAP: Dict[str, str] = {
    "cat_tooth": "tooth",
    "cat_periodontal": "periodontal",
    "cat_mucosa": "mucosa",
    "cat_jaw": "jaw",
}


def is_emergency(observations: Dict[str, bool]) -> bool:
    """
    Xavfli (shoshilinch) holat: yiringli/tarqalgan jarayonga shubha.

      - yuqori isitma + jag'/yuz shishi, yoki
      - isitma + trizm + jag' shishi
    """
    high_fever_swelling = observations.get("high_fever") and observations.get("jaw_swelling")
    spreading = (
        observations.get("fever")
        and observations.get("trismus")
        and observations.get("jaw_swelling")
    )
    return bool(high_fever_swelling or spreading)
