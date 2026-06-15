"""Tashxis dvigateli — ommaviy API."""

from engine.diagnosis import (
    MAX_QUESTIONS,
    MIN_QUESTIONS,
    diagnose,
    get_next_question,
    should_stop,
)
from engine.tree import CATEGORY_MAP, is_emergency

__all__ = [
    "MAX_QUESTIONS",
    "MIN_QUESTIONS",
    "diagnose",
    "get_next_question",
    "should_stop",
    "CATEGORY_MAP",
    "is_emergency",
]
