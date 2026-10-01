"""Minimal OpenRouter client with a fixed structured-output contract."""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from urllib.request import Request, urlopen

from .types import Label, Prediction, Sentence


@dataclass(frozen=True)
class ModelRun:
    predictions: list[Prediction]
    model: str
    latency_seconds: float
    prompt_tokens: int | None
    completion_tokens: int | None
    total_cost_usd: float | None


SYSTEM_PROMPT = """You classify IT discovery-note sentences for a delivery team.
Use fact only for client-confirmed or directly observed statements. Use assumption
for an unverified inference, estimate, internal plan, or tentative agreement. Use
open_question for an unresolved gap, contradiction, or required follow-up. If
evidence is insufficient, use abstain. A fact must include a verbatim quote from
the input sentence. Return only valid JSON matching the requested schema."""


def classify(sentences: list[Sentence], model: str | None = None, api_key: str | None = None) -> ModelRun:
    """Classify a note batch through OpenRouter without exposing gold labels."""
    api_key = api_key or os.environ.get("OPENROUTER_API_KEY")
    model = model or os.environ.get("OPENROUTER_MODEL")
    if not api_key or not model:
        raise ValueError("Set OPENROUTER_API_KEY and OPENROUTER_MODEL before calling the LLM.")
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": json.dumps(
                    {"sentences": [{"note_id": s.note_id, "n": s.number, "text": s.text} for s in sentences]},
                    ensure_ascii=False,
                ),
            },
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "note_triage_predictions",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "predictions": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "note_id": {"type": "string"},
                                    "n": {"type": "integer"},
                                    "label": {"type": "string", "enum": [label.value for label in Label]},
                                    "quote": {"type": ["string", "null"]},
                                },
                                "required": ["note_id", "n", "label", "quote"],
                                "additionalProperties": False,
                            },
                        }
                    },
                    "required": ["predictions"],
                    "additionalProperties": False,
                },
            },
        },
        "temperature": 0,
    }
    request = Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    started = time.perf_counter()
    with urlopen(request, timeout=90) as response:  # nosec B310 - fixed HTTPS endpoint
        body = json.load(response)
    latency = time.perf_counter() - started
    content = body["choices"][0]["message"]["content"]
    parsed = json.loads(content)
    predictions = [
        Prediction(item["note_id"], item["n"], Label(item["label"]), item["quote"])
        for item in parsed["predictions"]
    ]
    expected = {(sentence.note_id, sentence.number) for sentence in sentences}
    observed = {(prediction.note_id, prediction.number) for prediction in predictions}
    if observed != expected:
        raise ValueError("Model response does not contain exactly one prediction per input sentence.")
    usage = body.get("usage", {})
    return ModelRun(
        predictions=predictions,
        model=model,
        latency_seconds=latency,
        prompt_tokens=usage.get("prompt_tokens"),
        completion_tokens=usage.get("completion_tokens"),
        total_cost_usd=float(usage["total_cost"]) if usage.get("total_cost") is not None else None,
    )
