from __future__ import annotations

from python_ntfy import MessagePriority, NtfyClient

from . import config


def _sanitize_header(value: str) -> str:
    return value.encode("latin-1", "ignore").decode("latin-1")


def _priority_from_string(value: str) -> MessagePriority:
    normalized = value.strip().lower()
    if normalized in {"min", "lowest"}:
        return MessagePriority.MIN
    if normalized in {"low"}:
        return MessagePriority.LOW
    if normalized in {"high"}:
        return MessagePriority.HIGH
    if normalized in {"max", "urgent"}:
        return MessagePriority.MAX
    return MessagePriority.DEFAULT


def _parse_tags(tags: str) -> list[str]:
    return [_sanitize_header(tag.strip()) for tag in tags.split(",") if tag.strip()]


def send_notification(title: str, body: str, priority: str, tags: str) -> tuple[bool, str | None]:
    try:
        client = NtfyClient(topic=config.settings.ntfy_topic, server=config.settings.ntfy_server)
        client.send(
            message=body,
            title=_sanitize_header(title),
            priority=_priority_from_string(priority),
            tags=_parse_tags(tags),
        )
        return True, None
    except Exception as exc:
        return False, str(exc)
