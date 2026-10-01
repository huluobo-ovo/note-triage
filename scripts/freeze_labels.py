"""Validate author-completed holdout labels and create the final JSONL file."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOLDOUT = ROOT / "data/raw/holdout"
COMPLETED_CSV = HOLDOUT / "labels.csv"
TEMPLATE_JSONL = HOLDOUT / "labels.template.jsonl"
OUTPUT_JSONL = HOLDOUT / "labels.jsonl"
VALID_LABELS = {"fact", "assumption", "open_question"}


def read_template() -> dict[tuple[str, int], dict[str, object]]:
    rows: dict[tuple[str, int], dict[str, object]] = {}
    for line in TEMPLATE_JSONL.read_text(encoding="utf-8").splitlines():
        record = json.loads(line)
        for sentence in record["sentences"]:
            key = (record["id"], sentence["n"])
            rows[key] = sentence
    return rows


def main() -> None:
    template = read_template()
    completed: dict[tuple[str, int], str] = {}
    with COMPLETED_CSV.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        required = {"note_id", "sentence_number", "sentence", "gold_label"}
        if set(reader.fieldnames or ()) != required:
            raise ValueError(f"CSV headers must be exactly {sorted(required)}")
        for line_number, row in enumerate(reader, start=2):
            key = (row["note_id"], int(row["sentence_number"]))
            if key in completed:
                raise ValueError(f"CSV line {line_number}: duplicate label for {key}")
            expected = template.get(key)
            if expected is None:
                raise ValueError(f"CSV line {line_number}: unknown sentence {key}")
            if row["sentence"] != expected["text"]:
                raise ValueError(f"CSV line {line_number}: sentence text differs from frozen template for {key}")
            label = row["gold_label"].strip()
            if label not in VALID_LABELS:
                raise ValueError(f"CSV line {line_number}: invalid or blank label {label!r}")
            completed[key] = label
    if set(completed) != set(template):
        missing = sorted(set(template) - set(completed))
        extra = sorted(set(completed) - set(template))
        raise ValueError(f"Label coverage mismatch; missing={missing}, extra={extra}")

    records: dict[str, list[dict[str, object]]] = {}
    for (note_id, number), sentence in template.items():
        records.setdefault(note_id, []).append({**sentence, "gold_label": completed[(note_id, number)]})
    with OUTPUT_JSONL.open("w", encoding="utf-8") as file:
        for note_id in sorted(records):
            sentences = sorted(records[note_id], key=lambda item: item["n"])
            file.write(json.dumps({"id": note_id, "sentences": sentences}, ensure_ascii=False) + "\n")
    print(f"Frozen {len(completed)} labels across {len(records)} notes: {OUTPUT_JSONL}")


if __name__ == "__main__":
    main()
