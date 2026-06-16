"""
Anatomical Location Intelligence (V2.0).

Joylashuv endi faqat ko'rsatilmaydi — u Bayes modeliga kiradi:

    P(D | S, L) ∝ P(D) · P(S | D) · P(L | D)

`location_likelihood` kasallikning anatomik profili (Disease.location_profile)
asosida P(L | D) ni hisoblaydi. Profil bo'lmasa yoki joylashuv ko'rsatilmasa —
neytral (1.0).

Joylashuv tokenlari:
    jaw  = upper | lower
    side = right | left
    type = incisor | canine | premolar | molar
('unknown' va bo'sh qiymatlar e'tiborsiz qoldiriladi.)
"""

from __future__ import annotations

from typing import Dict, Optional

from medical.disease_model import Disease


def location_likelihood(disease: Disease, location: Optional[Dict[str, str]]) -> float:
    """P(L | D) — kasallikning joylashuv profiliga asoslangan nisbiy ehtimol."""
    profile = disease.location_profile
    if not profile or not location:
        return 1.0

    weight = 1.0
    for step in ("jaw", "side", "type"):
        value = location.get(step)
        if not value or value == "unknown":
            continue
        if value in profile:
            weight *= profile[value]
    return max(weight, 1e-6)
