"""
Akinator yadrosi — information-gain asosida keyingi savolni tanlash.

Har qadamda nomzod savollardan biri tanlanadi: javobi joriy ishonchni
(aposterior taqsimotni) eng ko'p aniqlashtiradigani, ya'ni kutilayotgan
entropiyani eng ko'p kamaytiradigani.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from domain.symptoms import candidates_for
from engine.scoring import entropy, p_symptom_present, posterior
from medical.disease_model import Disease


def _posterior_after(
    diseases: List[Disease],
    observations: Dict[str, bool],
    feature: str,
    answer: bool,
) -> List[float]:
    """`feature`=answer qo'shilgandan keyingi aposterior ehtimollar ro'yxati."""
    hypothetical = dict(observations)
    hypothetical[feature] = answer
    return [p for _, p in posterior(diseases, hypothetical)]


def expected_info_gain(
    diseases: List[Disease],
    observations: Dict[str, bool],
    feature: str,
) -> float:
    """
    `feature` savolini berishdan kutilayotgan axborot daromadi (information gain).
    Gain = H(joriy) − E[H(javobdan keyin)].
    """
    current = [p for _, p in posterior(diseases, observations)]
    h_now = entropy(current)

    # Javob "ha" bo'lish ehtimoli (joriy ishonch bo'yicha o'rtacha)
    p_yes = sum(
        prob * p_symptom_present(d, feature)
        for d, prob in posterior(diseases, observations)
    )
    p_yes = min(max(p_yes, 0.0), 1.0)
    p_no = 1.0 - p_yes

    h_yes = entropy(_posterior_after(diseases, observations, feature, True))
    h_no = entropy(_posterior_after(diseases, observations, feature, False))

    expected_h = p_yes * h_yes + p_no * h_no
    return h_now - expected_h


def next_question(
    category: str,
    observations: Dict[str, bool],
    asked: List[str],
    diseases: List[Disease],
) -> Optional[str]:
    """
    Keyingi berilishi kerak bo'lgan eng informativ simptom id'sini qaytaradi.
    Mos savol qolmasa — None.
    """
    asked_set = set(asked)
    pool = [s for s in candidates_for(category) if s not in asked_set]
    if not pool or not diseases:
        return None

    best_feature: Optional[str] = None
    best_gain = float("-inf")
    for feature in pool:
        gain = expected_info_gain(diseases, observations, feature)
        if gain > best_gain:
            best_gain = gain
            best_feature = feature

    # Agar hech qanday savol foydali ma'lumot bermasa (gain ~ 0), to'xtaymiz.
    if best_feature is None or best_gain <= 1e-4:
        return None
    return best_feature
