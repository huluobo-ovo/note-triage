"""Guardrails for claim grounding."""

from __future__ import annotations

from .types import Label, Prediction, Sentence


def validate_prediction(sentence: Sentence, prediction: Prediction) -> Prediction:
    """Downgrade an invalid fact claim to abstention.

    Facts require a non-empty verbatim quote contained in the source sentence.
    """
    if prediction.label is not Label.FACT:
        return prediction
    if not prediction.quote or prediction.quote not in sentence.text:
        return Prediction(
            note_id=prediction.note_id,
            number=prediction.number,
            label=Label.ABSTAIN,
            rationale="Fact rejected: missing or non-verbatim source quote.",
        )
    return prediction
