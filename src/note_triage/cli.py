"""Command-line entry point for local baseline evaluation."""

from __future__ import annotations

import argparse

from .baseline import classify_all
from .data import load_labeled_sentences
from .evaluate import evaluate


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate the NoteTriage keyword baseline.")
    parser.add_argument("labels", help="JSONL file containing frozen sentence labels")
    args = parser.parse_args()
    sentences = load_labeled_sentences(args.labels)
    metrics = evaluate(sentences, classify_all(sentences))
    print(f"sentences: {len(sentences)}")
    print(f"assumption-as-fact: {metrics.assumption_as_fact_errors}/{metrics.assumptions} ({metrics.assumption_as_fact_rate:.1%})")
    print(f"macro-F1: {metrics.macro_f1:.3f}")
    print(f"fact quote validity: {metrics.fact_quote_validity_rate:.1%}")
    print(f"abstentions: {metrics.abstentions}/{len(sentences)} ({metrics.abstention_rate:.1%})")


if __name__ == "__main__":
    main()
