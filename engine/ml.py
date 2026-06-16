"""
Machine Learning Layer (V2.0) — interfeys + xavfsiz fallback.

Arxitektura: Bayes + ML (gibrid).
    FinalScore = W_BAYES * P_bayes + W_ML * P_ml

Hozir: o'qitilgan model YO'Q (real dataset to'planmagan va sandbox internetsiz —
CatBoost/LightGBM o'rnatib bo'lmaydi). Shu sababli `MLRanker.available` = False
va gibrid ballash sof Bayes'ga qaytadi (fallback).

Ma'lumot (10k+ tasdiqlangan case) to'planganda:
  - feature extraction: {age, sex, jaw, side, type, symptom_1..n}
  - CatBoost (categorical featurelar, kichik dataset, explainable) o'qitiladi
  - bu yerdagi `MLRanker` real modelni yuklaydi va predict_proba qaytaradi.
"""

from __future__ import annotations

from typing import Dict, Optional

W_BAYES = 0.6
W_ML = 0.4


class MLRanker:
    """ML model uchun interfeys. Model bo'lmasa available=False."""

    def __init__(self) -> None:
        self._model = None  # kelajakda yuklangan CatBoost/LightGBM modeli

    @property
    def available(self) -> bool:
        return self._model is not None

    def predict_proba(self, features: dict) -> Optional[Dict[str, float]]:
        """{disease_id: probability} yoki model yo'q bo'lsa None."""
        if self._model is None:
            return None
        # Kelajakda: return self._model.predict_proba(features)
        return None


ml_ranker = MLRanker()


def hybrid_scores(
    bayes_scores: Dict[str, float],
    features: Optional[dict] = None,
) -> Dict[str, float]:
    """
    Bayes va ML ballarini birlashtiradi. ML mavjud bo'lmasa — sof Bayes.
    """
    if not ml_ranker.available or features is None:
        return bayes_scores
    ml_scores = ml_ranker.predict_proba(features)
    if not ml_scores:
        return bayes_scores
    combined = {}
    for did, p_bayes in bayes_scores.items():
        p_ml = ml_scores.get(did, 0.0)
        combined[did] = W_BAYES * p_bayes + W_ML * p_ml
    return combined
