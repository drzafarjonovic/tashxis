"""
Adaptive Question Engine (V2.0) — Expected Diagnostic Gain.

Oldingi versiya butun kasalliklar to'plami bo'yicha information-gain hisoblardi.
Endi har qadamda eng ehtimolli TOP-K kasallik (yetakchilar) ajratiladi va savol
aynan ularni eng yaxshi farqlaydiganiga qarab tanlanadi. Bu savollar sonini
kamaytiradi (10-12 → 5-7) chunki tizim allaqachon past ehtimolli kasalliklarga
savol sarflamaydi.

Demografik kontekst (yosh/jins) va anatomik joylashuv ham posterior orqali
hisobga olinadi.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from domain.symptoms import candidates_for
from engine.scoring import entropy, p_symptom_present, posterior
from medical.disease_model import Disease

# Yetakchi kasalliklar soni (savol shularni ajratishga yo'naltiriladi)
TOP_K = 6


def _posterior_after(
    diseases: List[Disease],
    observations: Dict[str, bool],
    feature: str,
    answer: bool,
    demo: Optional[object],
    location: Optional[Dict[str, str]],
) -> List[float]:
    """`feature`=answer qo'shilgandan keyingi aposterior ehtimollar ro'yxati."""
    hypothetical = dict(observations)
    hypothetical[feature] = answer
    return [p for _, p in posterior(diseases, hypothetical, demo, location)]


def expected_info_gain(
    diseases: List[Disease],
    observations: Dict[str, bool],
    feature: str,
    demo: Optional[object] = None,
    location: Optional[Dict[str, str]] = None,
) -> float:
    """
    `feature` savolini berishdan kutilayotgan diagnostik daromad.
    Gain = H(joriy) − E[H(javobdan keyin)] (berilgan kasalliklar to'plami bo'yicha).
    """
    ranked = posterior(diseases, observations, demo, location)
    current = [p for _, p in ranked]
    h_now = entropy(current)

    # Javob "ha" bo'lish ehtimoli (joriy ishonch bo'yicha o'rtacha)
    p_yes = sum(prob * p_symptom_present(d, feature) for d, prob in ranked)
    p_yes = min(max(p_yes, 0.0), 1.0)
    p_no = 1.0 - p_yes

    h_yes = entropy(_posterior_after(diseases, observations, feature, True, demo, location))
    h_no = entropy(_posterior_after(diseases, observations, feature, False, demo, location))

    expected_h = p_yes * h_yes + p_no * h_no
    return h_now - expected_h


def next_question(
    category: str,
    observations: Dict[str, bool],
    asked: List[str],
    diseases: List[Disease],
    demo: Optional[object] = None,
    location: Optional[Dict[str, str]] = None,
) -> Optional[str]:
    """
    Keyingi eng informativ simptom id'sini qaytaradi (top-K yetakchilarni
    ajratishga yo'naltirilgan). Mos savol qolmasa — None.
    """
    asked_set = set(asked)
    pool = [s for s in candidates_for(category) if s not in asked_set]
    if not pool or not diseases:
        return None

    # Yetakchi kasalliklarni hisobga olamiz, ammo gain'ni TO'LIQ to'plam bo'yicha
    # hisoblaymiz — shunda noyob "anchor" savollari (kam uchraydigan kasallikni
    # ko'taradigan) ham tanlanishi mumkin (reachability saqlanadi).
    ranked = posterior(diseases, observations, demo, location)
    _ = ranked[:TOP_K]  # diagnostik diqqat markazi (kelajakda tahlil uchun)

    best_feature: Optional[str] = None
    best_gain = float("-inf")
    for feature in pool:
        gain = expected_info_gain(diseases, observations, feature, demo, location)
        if gain > best_gain:
            best_gain = gain
            best_feature = feature

    # Hech qanday savol foydali ma'lumot bermasa (gain ~ 0), to'xtaymiz.
    if best_feature is None or best_gain <= 1e-4:
        return None
    return best_feature
