"""Metrics required by the NoteTriage project."""

from __future__ import annotations

from dataclasses import dataclass

from .types import GOLD_LABELS, Label, Prediction, Sentence
from .validation import validate_prediction


@dataclass(frozen=True)
class Metrics:
    assumptions: int
    assumption_as_fact_errors: int
    assumption_as_fact_rate: float
    abstentions: int
    abstention_rate: float
    fact_quote_validity_rate: float
    macro_f1: float


def _f1(gold: list[Label], predicted: list[Label], label: Label) -> float:
    tp = sum(g == label and p == label for g, p in zip(gold, predicted, strict=True))
    fp = sum(g != label and p == label for g, p in zip(gold, predicted, strict=True))
    fn = sum(g == label and p != label for g, p in zip(gold, predicted, strict=True))
    denominator = 2 * tp + fp + fn
    return 0.0 if denominator == 0 else 2 * tp / denominator


def evaluate(sentences: list[Sentence], predictions: list[Prediction]) -> Metrics:
    if len(sentences) != len(predictions):
        raise ValueError("Sentences and predictions must have the same length")
    checked = [validate_prediction(sentence, prediction) for sentence, prediction in zip(sentences, predictions, strict=True)]
    gold = [sentence.gold_label for sentence in sentences]
    if any(label not in GOLD_LABELS for label in gold):
        raise ValueError("All evaluated sentences need a gold label")
    predicted = [prediction.label for prediction in checked]
    assumptions = sum(label is Label.ASSUMPTION for label in gold)
    errors = sum(g is Label.ASSUMPTION and p is Label.FACT for g, p in zip(gold, predicted, strict=True))
    abstentions = sum(label is Label.ABSTAIN for label in predicted)
    facts = [i for i, label in enumerate(predicted) if label is Label.FACT]
    valid_facts = sum(checked[i].quote in sentences[i].text for i in facts)
    # Abstentions count as a wrong prediction in the three-class macro-F1.
    macro_f1 = sum(_f1(gold, predicted, label) for label in GOLD_LABELS) / len(GOLD_LABELS)
    return Metrics(
        assumptions=assumptions,
        assumption_as_fact_errors=errors,
        assumption_as_fact_rate=0.0 if assumptions == 0 else errors / assumptions,
        abstentions=abstentions,
        abstention_rate=abstentions / len(sentences) if sentences else 0.0,
        fact_quote_validity_rate=valid_facts / len(facts) if facts else 1.0,
        macro_f1=macro_f1,
    )
