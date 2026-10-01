"""A transparent, deliberately conservative keyword/regex baseline."""

from __future__ import annotations

import re

from .types import Label, Prediction, Sentence


QUESTION_PATTERNS = tuple(
    re.compile(pattern, re.IGNORECASE)
    for pattern in (
        r"\?",
        r"\b(need to ask|still need|not provided|not discussed|unknown|unclear|not settled|not named|not captured|blank in the notes)\b",
        r"^(who|what|when|where|which|whether|how)\b",
    )
)
ASSUMPTION_PATTERNS = tuple(
    re.compile(pattern, re.IGNORECASE)
    for pattern in (
        r"\b(assume|assumption|think|reckon|probably|might|maybe|guess|placeholder|sounds fine)\b",
        r"\b(our side|i.m taking|we used last time|not locked|not a counted export)\b",
    )
)
FACT_PATTERN = re.compile(
    r"\b(client|sponsor)\s+(confirmed|said|showed|opened|put)\b", re.IGNORECASE
)


def classify(sentence: Sentence) -> Prediction:
    """Classify without an LLM. Only explicit client evidence becomes a fact."""
    text = sentence.text.strip()
    if any(pattern.search(text) for pattern in QUESTION_PATTERNS):
        label = Label.OPEN_QUESTION
    elif any(pattern.search(text) for pattern in ASSUMPTION_PATTERNS):
        label = Label.ASSUMPTION
    elif FACT_PATTERN.search(text):
        label = Label.FACT
    else:
        # Conservatism is intentional: an ungrounded statement must not become a fact.
        label = Label.ABSTAIN
    quote = text if label is Label.FACT else None
    return Prediction(note_id=sentence.note_id, number=sentence.number, label=label, quote=quote)


def classify_all(sentences: list[Sentence]) -> list[Prediction]:
    return [classify(sentence) for sentence in sentences]
