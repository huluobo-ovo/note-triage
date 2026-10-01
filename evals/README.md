# Evaluation

Run the frozen holdout once after setting `OPENROUTER_API_KEY` and `OPENROUTER_MODEL`:

```bash
PYTHONPATH=src python scripts/run_openrouter_eval.py
```

The runner sends only `data/raw/holdout/notes.jsonl` to the model. It never sends `labels.jsonl`. It validates fact quotes against the source sentence, then writes predictions, metrics, token usage, cost, latency, and the gold-label distribution of abstentions to `evals/results/gpt4o_holdout_run.json`.
