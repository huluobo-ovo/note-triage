"""Run one reproducible OpenRouter evaluation against the frozen holdout."""

from __future__ import annotations

import json
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

from note_triage.data import load_holdout
from note_triage.evaluate import evaluate
from note_triage.openrouter import classify
from note_triage.validation import validate_prediction


ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / "data/raw/holdout/notes.jsonl"
LABELS = ROOT / "data/raw/holdout/labels.jsonl"
RESULTS = ROOT / "evals/results"


def main() -> None:
    sentences = load_holdout(NOTES, LABELS)
    run = classify(sentences)
    checked = [validate_prediction(sentence, prediction) for sentence, prediction in zip(sentences, run.predictions, strict=True)]
    metrics = evaluate(sentences, checked)
    abstained_by_gold = Counter(
        sentence.gold_label.value
        for sentence, prediction in zip(sentences, checked, strict=True)
        if prediction.label.value == "abstain"
    )
    result = {
        "run_at_utc": datetime.now(UTC).isoformat(),
        "model": run.model,
        "dataset": {"notes": str(NOTES.relative_to(ROOT)), "labels": str(LABELS.relative_to(ROOT)), "sentences": len(sentences)},
        "usage": {
            "latency_seconds": run.latency_seconds,
            "prompt_tokens": run.prompt_tokens,
            "completion_tokens": run.completion_tokens,
            "total_cost_usd": run.total_cost_usd,
        },
        "metrics": metrics.__dict__,
        "abstentions_by_gold_label": dict(sorted(abstained_by_gold.items())),
        "predictions": [prediction.__dict__ for prediction in checked],
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    result_path = RESULTS / "gpt4o_holdout_run.json"
    result_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {result_path}")
    print(f"assumption-as-fact: {metrics.assumption_as_fact_errors}/{metrics.assumptions} ({metrics.assumption_as_fact_rate:.1%})")
    print(f"macro-F1: {metrics.macro_f1:.3f}")
    print(f"abstentions: {metrics.abstentions}/{len(sentences)} ({metrics.abstention_rate:.1%})")
    print(f"cost: {run.total_cost_usd if run.total_cost_usd is not None else 'not returned'} USD")


if __name__ == "__main__":
    main()
