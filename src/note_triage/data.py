"""Read and validate the frozen JSONL note format."""

from __future__ import annotations

import json
from pathlib import Path

from .types import GOLD_LABELS, Label, Sentence


def load_labeled_sentences(path: str | Path) -> list[Sentence]:
    """Load sentence labels and reject malformed source spans early."""
    source = Path(path)
    sentences: list[Sentence] = []
    for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        record = json.loads(line)
        text = record["text"]
        for item in record["sentences"]:
            label = Label(item["label"])
            if label not in GOLD_LABELS:
                raise ValueError(f"{source}:{line_number}: gold label cannot be {label}")
            start, end = item["start"], item["end"]
            if text[start:end] != item["text"]:
                raise ValueError(
                    f"{source}:{line_number}, sentence {item['n']}: source span does not match text"
                )
            sentences.append(
                Sentence(
                    note_id=record["id"],
                    number=item["n"],
                    text=item["text"],
                    gold_label=label,
                    start=start,
                    end=end,
                )
            )
    return sentences


def load_holdout(notes_path: str | Path, labels_path: str | Path) -> list[Sentence]:
    """Join frozen unlabeled notes to their separately stored gold labels."""
    notes = {
        record["id"]: record
        for record in (
            json.loads(line)
            for line in Path(notes_path).read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    }
    sentences: list[Sentence] = []
    for line in Path(labels_path).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        note = notes.get(record["id"])
        if note is None:
            raise ValueError(f"Labels reference unknown note {record['id']}")
        for item in record["sentences"]:
            label = Label(item["gold_label"])
            if label not in GOLD_LABELS:
                raise ValueError(f"Invalid holdout label {label}")
            if note["text"][item["start"] : item["end"]] != item["text"]:
                raise ValueError(f"Source span mismatch for {record['id']} sentence {item['n']}")
            sentences.append(
                Sentence(
                    note_id=record["id"],
                    number=item["n"],
                    text=item["text"],
                    gold_label=label,
                    start=item["start"],
                    end=item["end"],
                )
            )
    return sentences
