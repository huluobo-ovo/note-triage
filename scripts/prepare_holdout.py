"""Create the immutable NoteTriage holdout input and label template.

The source Markdown contains presentation tables and prose labels. They are
excluded from model input so the classifier cannot infer gold labels from the
document structure. This script never assigns labels; the project author must
fill them in manually before the holdout is frozen.
"""

from __future__ import annotations

import json
import re
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/raw/holdout/notes_source.md"
NOTES = ROOT / "data/raw/holdout/notes.jsonl"
LABEL_TEMPLATE = ROOT / "data/raw/holdout/labels.template.jsonl"
LABEL_CSV = ROOT / "data/raw/holdout/labels.template.csv"


def parse_notes(markdown: str) -> list[dict[str, object]]:
    sections = re.split(r"(?m)^# (?=\d{2} )", markdown)[1:]
    records: list[dict[str, object]] = []
    for section in sections:
        heading, _, remainder = section.partition("\n")
        match = re.match(r"(?P<number>\d{2})\s+(?P<title>.+)", heading)
        if not match:
            raise ValueError(f"Cannot parse note heading: {heading!r}")
        bullets = re.findall(r"(?m)^•\s*(.+)$", remainder)
        if not bullets:
            raise ValueError(f"{heading}: no bullet sentences found")
        note_id = f"H{match.group('number')}"
        title = match.group("title")
        text = f"{title}\n\n" + "\n".join(bullets) + "\n"
        cursor = len(title) + 2
        sentences = []
        for number, sentence in enumerate(bullets, start=1):
            start = cursor
            end = start + len(sentence)
            sentences.append({"n": number, "text": sentence, "start": start, "end": end})
            cursor = end + 1
        records.append({"id": note_id, "title": title, "text": text, "sentences": sentences})
    if len(records) != 15:
        raise ValueError(f"Expected 15 notes; found {len(records)}")
    return records


def main() -> None:
    records = parse_notes(SOURCE.read_text(encoding="utf-8"))
    with (
        NOTES.open("w", encoding="utf-8") as notes_file,
        LABEL_TEMPLATE.open("w", encoding="utf-8") as labels_file,
        LABEL_CSV.open("w", encoding="utf-8", newline="") as csv_file,
    ):
        csv_writer = csv.DictWriter(csv_file, fieldnames=["note_id", "sentence_number", "sentence", "gold_label"])
        csv_writer.writeheader()
        for record in records:
            notes_file.write(json.dumps({key: record[key] for key in ("id", "title", "text")}, ensure_ascii=False) + "\n")
            labels_file.write(
                json.dumps(
                    {"id": record["id"], "sentences": [{**sentence, "gold_label": None} for sentence in record["sentences"]]},
                    ensure_ascii=False,
                )
                + "\n"
            )
            for sentence in record["sentences"]:
                csv_writer.writerow(
                    {
                        "note_id": record["id"],
                        "sentence_number": sentence["n"],
                        "sentence": sentence["text"],
                        "gold_label": "",
                    }
                )
    print(f"Prepared {len(records)} unlabeled holdout notes.")


if __name__ == "__main__":
    main()
