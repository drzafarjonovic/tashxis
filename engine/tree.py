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
    "cat_tmj": "tmj",
    "cat_trauma": "trauma",
    "cat_dentition": "dentition",
    "cat_salivary": "salivary",
}


def is_emergency(observations: Dict[str, bool]) -> bool:
    """
    Xavfli (shoshilinch) holat: yiringli/tarqalgan jarayonga shubha.

      - yuqori isitma + jag'/yuz shishi, yoki
      - isitma + trizm + jag' shishi, yoki
      - yuqori isitma + kuchli og'riq + trizm (o'tkir osteomiyelit), yoki
      - yuqori isitma + so'lak bezi shishi (yiringli sialadenit/abscess)
    """
    high_fever_swelling = observations.get("high_fever") and observations.get("jaw_swelling")
    spreading = (
        observations.get("fever")
        and observations.get("trismus")
        and observations.get("jaw_swelling")
    )
    osteomyelitis_like = (
        observations.get("high_fever")
        and observations.get("severe_pain")
        and observations.get("trismus")
    )
    gland_abscess = observations.get("high_fever") and observations.get("gland_swelling")
    return bool(high_fever_swelling or spreading or osteomyelitis_like or gland_abscess)
