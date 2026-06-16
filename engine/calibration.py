"""
Confidence Calibration Engine (V2.0) — interfeys + xavfsiz fallback.

Maqsad: model bergan "ishonch" qiymati haqiqiy to'g'rilik ehtimolini aks
ettirsin (0.80 ishonch ≈ 80% holatda to'g'ri).

Hozir: real labeled ma'lumot (doctor_feedback) yo'q, shuning uchun kalibrator
IDENTITY (o'zgartirmaydi). Ma'lumot to'planganda `fit_isotonic` (PAV algoritmi,
tashqi kutubxonasiz) yoki Platt scaling bilan o'qitiladi va shu yerda qo'llanadi.
"""

from __future__ import annotations

from typing import List, Optional, Tuple


class Calibrator:
    """Ehtimolni kalibrlaydi. Fit qilinmagan bo'lsa — identity (o'zgartirmaydi)."""

    def __init__(self) -> None:
        # Isotonic bosqichlari: (threshold, calibrated_value) kamayatmaydigan ro'yxat
        self._steps: Optional[List[Tuple[float, float]]] = None

    @property
    def is_fitted(self) -> bool:
        return self._steps is not None

    def calibrate(self, prob: float) -> float:
        if not self._steps:
            return prob
        result = self._steps[0][1]
        for threshold, value in self._steps:
            if prob >= threshold:
                result = value
            else:
                break
        return min(max(result, 0.0), 1.0)

    def fit_isotonic(self, samples: List[Tuple[float, int]]) -> None:
        """
        PAV (Pool Adjacent Violators) — monoton isotonic regressiya.
        samples: (predicted_prob, correct{0|1}) juftliklari.
        Yetarli ma'lumot bo'lmasa — fit qilinmaydi (identity qoladi).
        """
        if len(samples) < 50:
            return
        data = sorted(samples, key=lambda s: s[0])
        xs = [p for p, _ in data]
        ys = [float(c) for _, c in data]
        weights = [1.0] * len(ys)

        # PAV
        i = 0
        while i < len(ys) - 1:
            if ys[i] > ys[i + 1]:
                # pool
                new_w = weights[i] + weights[i + 1]
                new_y = (ys[i] * weights[i] + ys[i + 1] * weights[i + 1]) / new_w
                ys[i] = new_y
                weights[i] = new_w
                del ys[i + 1]
                del weights[i + 1]
                del xs[i + 1]
                if i > 0:
                    i -= 1
            else:
                i += 1
        self._steps = list(zip(xs, ys))


# Global kalibrator (hozircha identity). Ma'lumot kelganda fit qilinadi.
calibrator = Calibrator()


def calibrate_confidence(prob: float) -> float:
    return calibrator.calibrate(prob)
