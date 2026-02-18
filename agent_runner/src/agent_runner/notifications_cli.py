from __future__ import annotations

from datetime import datetime, timezone

import typer

from .notifications import send_notification

app = typer.Typer(add_completion=False)


@app.command("notify")
def notify(
    title: str | None = typer.Option(None, "--title"),
    body: str | None = typer.Option(None, "--body"),
    priority: str = typer.Option("default", "--priority"),
    tags: str = typer.Option("bell", "--tags"),
    test: bool = typer.Option(False, "--test"),
) -> int:
    if test:
        title = title or "[notify-test]"
        body = body or f"notify-test at {datetime.now(timezone.utc).isoformat()}"
    else:
        if not title or not body:
            typer.echo("--title and --body are required unless --test is set", err=True)
            raise typer.Exit(2)

    ok, err = send_notification(title=title, body=body, priority=priority, tags=tags)
    if not ok:
        typer.echo(f"notification failed: {err}", err=True)
        raise typer.Exit(1)
    return 0


def main() -> None:
    app()
