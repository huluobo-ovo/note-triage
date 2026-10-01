"""Core types shared by classification and evaluation."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class Label(StrEnum):
    FACT = "fact"
    ASSUMPTION = "assumption"
    OPEN_QUESTION = "open_question"
    ABSTAIN = "abstain"


GOLD_LABELS = frozenset({Label.FACT, Label.ASSUMPTION, Label.OPEN_QUESTION})


@dataclass(frozen=True)
class Sentence:
    note_id: str
    number: int
    text: str
    gold_label: Label | None = None
    start: int | None = None
    end: int | None = None


@dataclass(frozen=True)
class Prediction:
    note_id: str
    number: int
    label: Label
    quote: str | None = None
    rationale: str | None = None
