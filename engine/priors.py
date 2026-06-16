"""
Clinical Prior System (V2.0).

effective_prior = base_prior(prevalence) × age_factor × sex_factor

Bu modul kasallikning epidemiologik oldindan ehtimolini (prior) hisoblaydi.
Demografik kontekst (yosh/jins) berilmasa, faqat bazaviy tarqalganlik priori
qo'llanadi (age/sex omillari = 1.0).

Self-Learning kengaytmasi: agar `priors` ma'lumotlar bazasida (yoki kelajakdagi
overrides faylida) tasdiqlangan statistikaga asoslangan yangilangan qiymatlar
bo'lsa, ular shu yerda standart tier'lar ustidan qo'llanishi mumkin.
"""

from __future__ import annotations

from typing import Optional

from medical.disease_model import Disease
from medical.epidemiology import (
    AGE_PRIORS,
    SEX_PRIORS,
    TIER_WEIGHTS,
)

# Tasdiqlangan ma'lumot asosida yangilanadigan override (Self-Learning).
# {disease_id: multiplier}. Bo'sh — hozircha standart qiymatlar ishlatiladi.
LEARNED_PRIOR_OVERRIDES: dict = {}

_DEFAULT_TIER = "uncommon"


def base_prior(disease: Disease) -> float:
    """1-qatlam: tarqalganlik tier'iga ko'ra bazaviy prior."""
    return TIER_WEIGHTS.get(disease.prevalence, TIER_WEIGHTS[_DEFAULT_TIER])


def age_factor(disease: Disease, age_group: Optional[str]) -> float:
    """2-qatlam: yosh guruhiga ko'ra omil (default 1.0)."""
    if not age_group:
        return 1.0
    return AGE_PRIORS.get(disease.id, {}).get(age_group, 1.0)


def sex_factor(disease: Disease, sex: Optional[str]) -> float:
    """3-qatlam: jinsga ko'ra omil (default 1.0)."""
    if not sex:
        return 1.0
    return SEX_PRIORS.get(disease.id, {}).get(sex, 1.0)


def effective_prior(disease: Disease, demo: Optional[object] = None) -> float:
    """
    Yakuniy prior = base × age × sex × (learned override).

    `demo` — DemographicContext (age_group, sex atributlari) yoki None.
    """
    age_group = getattr(demo, "age_group", None) if demo else None
    sex = getattr(demo, "sex", None) if demo else None

    prior = base_prior(disease)
    prior *= age_factor(disease, age_group)
    prior *= sex_factor(disease, sex)
    prior *= LEARNED_PRIOR_OVERRIDES.get(disease.id, 1.0)
    return max(prior, 1e-6)
