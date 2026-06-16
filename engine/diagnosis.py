"""
Tashxis orkestratori — savol oqimini boshqaradi va yakuniy natijani tuzadi.

V2.0: demografik kontekst (yosh/jins) va anatomik joylashuv Bayes yadrosiga
uzatiladi; yakuniy ishonch Confidence Calibration Engine orqali o'tkaziladi.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from engine.advice import build_explanation
from engine.calibration import calibrate_confidence
from engine.scoring import posterior
from engine.selector import next_question as _next_question
from medical import DIAGNOSTIC_GROUPS

# Savollar soni chegaralari
MIN_QUESTIONS = 4
MAX_QUESTIONS = 14

# Erta to'xtatish: yetakchi kasallik aniq ustun bo'lsa
EARLY_STOP_CONFIDENCE = 0.82      # yetakchi ehtimol shu darajadan yuqori
EARLY_STOP_MARGIN = 0.45          # yetakchi va ikkinchi o'rtasidagi farq

# Natija "aniq emas" deb belgilanadigan ishonchlilik chegarasi
UNCERTAIN_CONFIDENCE = 0.35

# Muqobil variant ko'rsatish uchun minimal ehtimol
ALTERNATIVE_MIN_PROB = 0.12


def get_next_question(
    category: str,
    observations: Dict[str, bool],
    asked: List[str],
    demo: Optional[object] = None,
    location: Optional[Dict[str, str]] = None,
) -> Optional[str]:
    """Keyingi eng informativ savol id'si (yoki None)."""
    diseases = DIAGNOSTIC_GROUPS.get(category, [])
    return _next_question(category, observations, asked, diseases, demo, location)


def should_stop(
    category: str,
    observations: Dict[str, bool],
    asked_count: int,
    demo: Optional[object] = None,
    location: Optional[Dict[str, str]] = None,
) -> bool:
    """Erta to'xtatish kerakmi — yetakchi kasallik yetarlicha aniqmi."""
    if asked_count < MIN_QUESTIONS:
        return False
    if asked_count >= MAX_QUESTIONS:
        return True

    diseases = DIAGNOSTIC_GROUPS.get(category, [])
    if len(diseases) < 2:
        return True

    ranked = posterior(diseases, observations, demo, location)
    if len(ranked) < 2:
        return True

    top_prob = ranked[0][1]
    margin = ranked[0][1] - ranked[1][1]
    return top_prob >= EARLY_STOP_CONFIDENCE or margin >= EARLY_STOP_MARGIN


def diagnose(
    category: str,
    observations: Dict[str, bool],
    lang: str = "uz",
    demo: Optional[object] = None,
    location: Optional[Dict[str, str]] = None,
) -> Dict:
    """
    Yakuniy tashxis natijasini qaytaradi.

    Qaytariladigan dict:
      diagnosis, disease_id, confidence (0..1, kalibrlangan), uncertain (bool),
      alternatives, red_flags, discriminators, explanation, category,
      description, symptoms_text, differential, treatment
    """
    diseases = DIAGNOSTIC_GROUPS.get(category, [])
    if not diseases:
        return {
            "diagnosis": None,
            "disease_id": None,
            "confidence": 0.0,
            "uncertain": True,
            "alternatives": [],
            "red_flags": [],
            "discriminators": [],
            "explanation": "",
            "category": category,
            "description": "",
            "symptoms_text": "",
            "differential": "",
            "treatment": "",
        }

    ranked = posterior(diseases, observations, demo, location)
    top_disease, top_prob = ranked[0]

    # Confidence Calibration Engine (hozircha identity — ma'lumot kelganda fit qilinadi)
    confidence = calibrate_confidence(top_prob)
    uncertain = confidence < UNCERTAIN_CONFIDENCE

    alternatives = [
        d.get_name(lang)
        for d, p in ranked[1:3]
        if p >= ALTERNATIVE_MIN_PROB
    ]

    return {
        "diagnosis": top_disease.get_name(lang),
        "disease_id": top_disease.id,
        "confidence": round(confidence, 2),
        "uncertain": uncertain,
        "alternatives": alternatives,
        "red_flags": top_disease.red_flags,
        "discriminators": top_disease.discriminators,
        "explanation": build_explanation(top_disease, category, lang),
        "category": category,
        # Tashxis aniqlangandan keyingi boy ma'lumot (bo'sh bo'lishi mumkin)
        "description": top_disease.get_description(lang),
        "symptoms_text": top_disease.get_symptoms_text(lang),
        "differential": top_disease.get_differential(lang),
        "treatment": top_disease.get_treatment(lang),
    }
