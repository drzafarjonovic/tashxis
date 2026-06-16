"""
Bayes asosidagi ballash (scoring).

Har bir kasallik — gipoteza. Bemorning javoblari (kuzatishlar) asosida
har bir kasallikning *aposterior* ehtimoli hisoblanadi:

    P(kasallik | javoblar) ∝ P(kasallik) · ∏ P(javob_f | kasallik)

So'ralmagan simptomlar mahsulotga kirmaydi → neytral.
Bu yondashuv noaniqlikni to'g'ri boshqaradi va haqiqiy ishonchlilik beradi.
"""

from __future__ import annotations

import math
from typing import Dict, List, Optional, Tuple

from engine.location import location_likelihood
from engine.priors import effective_prior
from medical.disease_model import Disease

# Simptom kasallikda KUZATILISH (present=True) ehtimoli, belgilar turiga qarab.
#   core      → kasallik uchun deyarli doim bor
#   optional  → ko'pincha bor
#   negative  → bu belgi BORLIGI kasallikka qarshi dalil (ya'ni odatda yo'q)
#   bog'liq emas → past bazaviy ehtimol
P_PRESENT_CORE = 0.90
P_PRESENT_OPTIONAL = 0.62
P_PRESENT_NEGATIVE = 0.10
P_PRESENT_BASE = 0.22

# Ehtimolliklarni 0/1 ga yopishib qolishdan saqlash (raqamli barqarorlik)
_EPS = 1e-6


def p_symptom_present(disease: Disease, feature: str) -> float:
    """Berilgan kasallikda simptom mavjud bo'lish ehtimoli P(present=True | disease)."""
    if feature in disease.core_features:
        return P_PRESENT_CORE
    if feature in disease.optional_features:
        return P_PRESENT_OPTIONAL
    if feature in disease.negative_features:
        return P_PRESENT_NEGATIVE
    return P_PRESENT_BASE


def _log_likelihood(disease: Disease, observations: Dict[str, bool]) -> float:
    """log P(kuzatishlar | kasallik). So'ralmagan simptomlar hisobga olinmaydi."""
    total = 0.0
    for feature, present in observations.items():
        p_present = p_symptom_present(disease, feature)
        p = p_present if present else (1.0 - p_present)
        total += math.log(max(p, _EPS))
    return total


def posterior(
    diseases: List[Disease],
    observations: Dict[str, bool],
    demo: Optional[object] = None,
    location: Optional[Dict[str, str]] = None,
) -> List[Tuple[Disease, float]]:
    """
    Kasalliklar bo'yicha normallashtirilgan aposterior ehtimollar:

        P(D | S, L) ∝ P(D | demografiya) · P(S | D) · P(L | D)

    - P(D | demografiya): epidemiologik prior (tarqalganlik × yosh × jins)
    - P(S | D): simptomlar likelihood'i (so'ralmaganlar neytral)
    - P(L | D): anatomik joylashuv likelihood'i (profil bo'lmasa neytral)

    Kamayish tartibida saralangan (disease, probability) ro'yxati.
    """
    if not diseases:
        return []

    log_scores = []
    for d in diseases:
        score = _log_likelihood(d, observations)
        score += math.log(max(effective_prior(d, demo), _EPS))
        score += math.log(max(location_likelihood(d, location), _EPS))
        log_scores.append(score)

    # Softmax (log-sum-exp orqali barqaror)
    max_ll = max(log_scores)
    exps = [math.exp(ll - max_ll) for ll in log_scores]
    total = sum(exps) or 1.0
    probs = [e / total for e in exps]

    ranked = list(zip(diseases, probs))
    ranked.sort(key=lambda x: x[1], reverse=True)
    return ranked


def entropy(probs: List[float]) -> float:
    """Taqsimotning Shannon entropiyasi (bit)."""
    h = 0.0
    for p in probs:
        if p > _EPS:
            h -= p * math.log2(p)
    return h
