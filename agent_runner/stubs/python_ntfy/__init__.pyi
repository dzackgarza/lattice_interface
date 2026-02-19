from enum import Enum
from typing import Any


class MessagePriority(Enum):
    MIN = "min"
    LOW = "low"
    DEFAULT = "default"
    HIGH = "high"
    MAX = "max"


class NtfyClient:
    def __init__(self, topic: str, server: str = ...) -> None: ...
    def send(
        self,
        message: str,
        title: str | None = ...,
        priority: MessagePriority = ...,
        tags: list[str] | None = ...,
        **kwargs: Any,
    ) -> None: ...
