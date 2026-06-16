"""
Demographic Engine (V2.0).

Sessiya boshida bemorning yoshi va jinsi yig'iladi va `DemographicContext`
yaratiladi. Bu kontekst Bayes modeliga prior sifatida uzatiladi
(engine/priors.py).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from medical.epidemiology import AGE_GROUPS, SEXES


@dataclass(frozen=True)
class DemographicContext:
    age_group: Optional[str] = None   # "5-12" | "13-18" | "19-40" | "41-65" | "65+"
    sex: Optional[str] = None         # "male" | "female"

    def as_dict(self) -> dict:
        return {"age_group": self.age_group, "sex": self.sex}

    @classmethod
    def from_dict(cls, data: Optional[dict]) -> "DemographicContext":
        if not data:
            return cls()
        return cls(age_group=data.get("age_group"), sex=data.get("sex"))


def is_valid_age_group(value: str) -> bool:
    return value in AGE_GROUPS


def is_valid_sex(value: str) -> bool:
    return value in SEXES
