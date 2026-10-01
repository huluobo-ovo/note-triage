# Evaluation

Run the frozen holdout once after setting `OPENROUTER_API_KEY` and `OPENROUTER_MODEL`:

```bash
PYTHONPATH=src python scripts/run_openrouter_eval.py
```

The runner sends only `data/raw/holdout/notes.jsonl` to the model. It never sends `labels.jsonl`. It validates fact quotes against the source sentence, then writes predictions, metrics, token usage, cost, latency, and the gold-label distribution of abstentions to `evals/results/gpt4o_holdout_run.json`.

## Frozen GPT-4o run

The saved run used `openai/gpt-4o-2024-08-06` on 113 sentences from 15 holdout notes. OpenRouter returned 4,120 input tokens and 3,786 output tokens but did not return a total cost. `gpt4o_cost_calculation.json` therefore records a transparent estimate from the listed USD 2.50/M input and USD 10.00/M output prices: USD 0.04816 for the 15-note batch, or about USD 0.00321 per note.
