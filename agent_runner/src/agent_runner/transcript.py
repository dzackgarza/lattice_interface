from __future__ import annotations

import json
import re
from pathlib import Path

TOKEN_REGEX = re.compile(
    r"tokens\s+used\s*\n\s*([\d,]+)",
    re.IGNORECASE,
)


def parse_last_message(
    agent: str, stdout: str, last_message_path: Path | None
) -> str:
    if agent == "codex" and last_message_path and last_message_path.exists():
        content = last_message_path.read_text(encoding="utf-8").strip()
        if content:
            return content
    for line in reversed(stdout.splitlines()):
        if line.strip():
            return line.strip()
    return "(no message captured)"


def parse_token_usage(text: str) -> int | None:
    match = TOKEN_REGEX.search(text)
    if not match:
        return None
    value = match.group(1).replace(",", "")
    if not value.isdigit():
        return None
    return int(value)


def parse_token_usage_from_outputs(
    stdout: str, last_message_path: Path | None
) -> int | None:
    candidates = []
    if last_message_path and last_message_path.exists():
        candidates.append(last_message_path.read_text(encoding="utf-8"))
    candidates.append(stdout)
    for candidate in candidates:
        value = parse_token_usage(candidate)
        if value is not None:
            return value
    return None


def parse_gemini_json(stdout: str) -> tuple[str | None, int | None]:
    try:
        data = json.loads(stdout)
    except json.JSONDecodeError:
        return None, None
    if not isinstance(data, dict):
        return None, None
    response = data.get("response")
    token_count = None
    stats = data.get("stats")
    if isinstance(stats, dict):
        models = stats.get("models")
        if isinstance(models, dict):
            for model_info in models.values():
                if not isinstance(model_info, dict):
                    continue
                tokens = model_info.get("tokens")
                if isinstance(tokens, dict):
                    total = tokens.get("total")
                    if isinstance(total, int):
                        token_count = total
                        break
    return response if isinstance(response, str) else None, token_count
