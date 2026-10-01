# Hand Authored Holdout Data Card

## Purpose

This directory contains the 15-note holdout for the final NoteTriage evaluation. The model receives only the contents of `notes.jsonl`; presentation tables and categorising headings from the original source are deliberately excluded.

## Provenance

The project author manually wrote the holdout wording. It uses fictional IT-delivery situations and contains no real client transcripts, personal data, employer files, credentials, or system identifiers. Some scenario themes were inspired by early development examples; this limits topical independence and must be discussed as an evaluation limitation.

## Freeze protocol

1. The author completes `labels.template.csv` manually with exactly one of `fact`, `assumption`, or `open_question` for every sentence. The CSV is intended for Excel or Numbers.
2. The author preserves the completed CSV, then the project converts it into `labels.jsonl` without changing note text, sentence numbers, or character offsets.
3. Commit the notes and labels together before running the final baseline or LLM evaluation.
4. Do not revise the holdout or its labels after reviewing predictions.

## Label definitions

- `fact`: a client-confirmed statement or directly observed evidence recorded without uncertainty.
- `assumption`: an internal estimate, inference, tentative plan, unverified statement, or soft agreement.
- `open_question`: an unresolved gap, contradiction, or follow-up required from the client.
