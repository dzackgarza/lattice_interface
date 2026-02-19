from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class ClassifiedError:
    code: str
    message: str


CLAUDE_LIMIT = re.compile(r"hit your limit|usage limit", re.IGNORECASE)
CODEX_LIMIT = re.compile(
    r"rate limit|quota|too many requests|429|hit your usage limit", re.IGNORECASE
)
GEMINI_LIMIT = re.compile(r"rate limit|quota|resource_exhausted|429", re.IGNORECASE)
OLLAMA_LIMIT = re.compile(r"rate limit|quota|resource_exhausted|429", re.IGNORECASE)


def classify_usage_limit(agent: str, stdout: str) -> ClassifiedError | None:
    combined = stdout
    if agent == "claude" and CLAUDE_LIMIT.search(combined):
        return ClassifiedError(code="usage_limit", message="Claude usage limit")
    if agent == "codex" and CODEX_LIMIT.search(combined):
        return ClassifiedError(code="usage_limit", message="Codex usage limit")
    if agent == "gemini" and GEMINI_LIMIT.search(combined):
        return ClassifiedError(code="usage_limit", message="Gemini usage limit")
    if agent == "ollama" and OLLAMA_LIMIT.search(combined):
        return ClassifiedError(code="usage_limit", message="Ollama usage limit")
    return None
