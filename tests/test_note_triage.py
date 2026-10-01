import unittest

from note_triage.evaluate import evaluate
from note_triage.types import Label, Prediction, Sentence
from note_triage.validation import validate_prediction


class NoteTriageTests(unittest.TestCase):
    def test_fact_without_verbatim_quote_abstains(self) -> None:
        sentence = Sentence("N01", 1, "Client confirmed SSO is enabled.", Label.FACT)
        prediction = Prediction("N01", 1, Label.FACT, quote="SSO will be enabled")
        self.assertEqual(validate_prediction(sentence, prediction).label, Label.ABSTAIN)

    def test_assumption_as_fact_uses_assumption_denominator(self) -> None:
        sentences = [
            Sentence("N01", 1, "Assume VPN works.", Label.ASSUMPTION),
            Sentence("N01", 2, "Client confirmed SSO.", Label.FACT),
        ]
        predictions = [
            Prediction("N01", 1, Label.FACT, quote="Assume VPN works."),
            Prediction("N01", 2, Label.FACT, quote="Client confirmed SSO."),
        ]
        metrics = evaluate(sentences, predictions)
        self.assertEqual(metrics.assumptions, 1)
        self.assertEqual(metrics.assumption_as_fact_errors, 1)
        self.assertEqual(metrics.assumption_as_fact_rate, 1.0)
