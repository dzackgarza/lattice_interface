from __future__ import annotations

import os
import warnings
import time
from datetime import datetime, timedelta, timezone
from typing import Literal, assert_never

import typer
from pydantic import BaseModel

from . import config, git, transcript
from .agents import (
    ClaudeAgent,
    CodexAgent,
    GeminiAgent,
    KiloAgent,
    OllamaAgent,
    OpencodeAgent,
    QwenAgent,
    RunContext,
)
from .agent_errors import classify_usage_limit
from .errors import (
    AgentCommitMissingError,
    AgentProcessError,
    AgentRunnerError,
    AgentTimeoutError,
    RateLimitUsageError,
)
from .logging import (
    build_run_context,
    get_logger,
    get_summary_logger,
    write_metadata,
    write_text,
)
from .notifications import send_notification
from .tasks import (
    AgentTask,
    AgentManagementTask,
    DebugSmokeCommitTask,
    DocumentCoverageTask,
    DocumentTestAlignmentTask,
)

app = typer.Typer(add_completion=False)

AgentName = Literal["codex", "claude", "gemini", "kilo", "ollama", "opencode", "qwen"]
TaskName = Literal[
    "agent_management",
    "document_coverage",
    "document_test_alignment",
    "debug_smoke_commit",
    "debug_hello_world",
    "debug_hello_simple",
]


class OrchestratorArgs(BaseModel):
    agent: AgentName
    task: TaskName
    debug: bool = False
    debug_prompt: str | None = None
    dry_run: bool = False


class Orchestrator(BaseModel):
    args: OrchestratorArgs

    def run(self) -> int:
        """Run an agent task with centralized logging."""
        task_obj = _build_task(self.args.task)
        agent_obj = _build_agent(self.args.agent)

        now = datetime.now(timezone.utc)
        run_id = now.strftime("%Y%m%d_%H%M%S")
        run_ctx = build_run_context(
            agent_name=agent_obj.name, task_name=task_obj.name, run_id=run_id
        )
        logger = get_logger(run_ctx)

        debug_prompt_path = None
        if self.args.debug_prompt:
            debug_prompt_path = config.settings.debug_prompts()[self.args.debug_prompt]
        elif self.args.debug:
            debug_prompt_path = config.settings.debug_prompts()["smoke"]

        start_time = datetime.now(timezone.utc)
        end_time = start_time
        exit_code = 0
        error_type: str | None = None
        error_detail: str | None = None

        try:
            head_before = git.get_head()

            if debug_prompt_path is not None:
                task_obj = task_obj.model_copy(
                    update={"prompt_path": debug_prompt_path}
                )

            if self.args.dry_run:
                proc_result = None
                stdout = "(dry-run)"
                exit_code = 0
            else:
                proc_result = agent_obj.run_task(task_obj, run_ctx)
                stdout = proc_result.stdout
                exit_code = proc_result.exit_code

            write_text(run_ctx.stdout_path, stdout)

            classified = classify_usage_limit(agent_obj.name, stdout)
            if classified:
                raise RateLimitUsageError(agent_obj.name, classified.message)

            if exit_code != 0:
                raise AgentProcessError(agent_obj.name, task_obj.name, exit_code)

            head_after = git.get_head()
            commit_summary = git.summarize_commits(head_before, head_after)
            if (
                not self.args.dry_run
                and task_obj.requires_commit
                and len(commit_summary.commits) == 0
            ):
                raise AgentCommitMissingError(agent_obj.name, task_obj.name)

            end_time = datetime.now(timezone.utc)
            elapsed = end_time - start_time
            # Invariant: every task runs forward in time; start_time was set before agent launch.
            assert elapsed.total_seconds() >= 0

            last_message = transcript.parse_last_message(
                agent=agent_obj.name,
                stdout=stdout,
                last_message_path=proc_result.last_message_path
                if proc_result
                else None,
            )
            token_count = transcript.parse_token_usage_from_outputs(
                stdout=stdout,
                last_message_path=proc_result.last_message_path
                if proc_result
                else None,
            )
            if agent_obj.name == "gemini":
                gemini_message, gemini_tokens = transcript.parse_gemini_json(stdout)
                if gemini_message:
                    last_message = gemini_message
                if gemini_tokens is not None:
                    token_count = gemini_tokens

            metadata = {
                "run_id": run_ctx.run_id,
                "agent": agent_obj.name,
                "task": task_obj.name,
                "start_time": start_time.isoformat(),
                "end_time": end_time.isoformat(),
                "elapsed_seconds": elapsed.total_seconds(),
                "exit_code": exit_code,
                "token_count": token_count,
                "last_message": last_message,
                "commits": [commit.__dict__ for commit in commit_summary.commits],
                "files_changed": commit_summary.files_changed,
                "insertions": commit_summary.insertions,
                "deletions": commit_summary.deletions,
                "debug_prompt": str(debug_prompt_path) if debug_prompt_path else None,
                "dry_run": self.args.dry_run,
                "requires_commit": task_obj.requires_commit,
                "classified_error": None,
            }
            write_metadata(run_ctx.metadata_path, metadata)

            summary_text = (
                f"{start_time.strftime('%Y-%m-%d %H:%M:%S UTC')} "
                f"[{agent_obj.name}/{task_obj.name}] "
                f"elapsed={_format_elapsed(elapsed)} "
                f"tokens={token_count if token_count is not None else 'n/a'} "
                f"files={len(commit_summary.files_changed)} "
                f"loc=+{commit_summary.insertions}/-{commit_summary.deletions}\n"
                f"last_message: {last_message}\n"
            )
            write_text(run_ctx.summary_path, summary_text)

            header = (
                f"\n=== {start_time.strftime('%Y-%m-%d %H:%M:%S UTC')} "
                f"[{agent_obj.name}/{task_obj.name}] ===\n"
            )
            summary_logger = get_summary_logger(run_ctx)
            summary_logger.info(header + summary_text)

            if task_obj.notify:
                notified, notify_err = _notify_success(
                    run_ctx=run_ctx,
                    start_time=start_time,
                    end_time=end_time,
                    elapsed=elapsed,
                    last_message=last_message,
                    token_count=token_count,
                    commit_summary=commit_summary,
                )
                if not notified:
                    logger.error("Notification failed", error=notify_err)
            logger.info("Run complete")
            return 0
        except RateLimitUsageError as exc:
            end_time = datetime.now(timezone.utc)
            exit_code = 10
            error_type = "usage limit"
            error_detail = str(exc)
            logger.exception("Agent runner error")
            warnings.warn(str(exc), RuntimeWarning)
            typer.echo(f"RateLimitUsageError: {exc}", err=True)
            error_meta = {
                "run_id": run_ctx.run_id,
                "agent": agent_obj.name,
                "task": task_obj.name,
                "exit_code": None,
                "error": str(exc),
                "classified_error": "usage_limit",
                "requires_commit": task_obj.requires_commit,
            }
            write_metadata(run_ctx.metadata_path, error_meta)
        except AgentTimeoutError as exc:
            end_time = datetime.now(timezone.utc)
            exit_code = 11
            error_type = "timeout"
            error_detail = str(exc)
            logger.exception("Agent timed out")
            typer.echo(f"AgentTimeoutError: {exc}", err=True)
            error_meta = {
                "run_id": run_ctx.run_id,
                "agent": agent_obj.name,
                "task": task_obj.name,
                "exit_code": None,
                "error": str(exc),
                "classified_error": "timeout",
                "requires_commit": task_obj.requires_commit,
            }
            write_metadata(run_ctx.metadata_path, error_meta)
        except AgentRunnerError as exc:
            end_time = datetime.now(timezone.utc)
            exit_code = 1
            error_type = "unknown"
            error_detail = str(exc)
            logger.exception("Agent runner error")
            error_meta = {
                "run_id": run_ctx.run_id,
                "agent": agent_obj.name,
                "task": task_obj.name,
                "exit_code": None,
                "error": str(exc),
                "classified_error": None,
                "requires_commit": task_obj.requires_commit,
            }
            write_metadata(run_ctx.metadata_path, error_meta)
        except typer.Exit:
            raise
        except Exception as exc:  # pragma: no cover
            end_time = datetime.now(timezone.utc)
            exit_code = 2
            error_type = "unhandled"
            error_detail = str(exc)
            logger.exception("Unhandled error", error=str(exc))
            error_meta = {
                "run_id": run_ctx.run_id,
                "agent": agent_obj.name,
                "task": task_obj.name,
                "exit_code": None,
                "error": str(exc),
                "classified_error": None,
                "requires_commit": task_obj.requires_commit,
            }
            write_metadata(run_ctx.metadata_path, error_meta)
        finally:
            if error_type is not None and task_obj.notify:
                notified, notify_err = _notify_error(
                    run_ctx=run_ctx,
                    error_type=error_type,
                    error_detail=error_detail,
                    start_time=start_time,
                    end_time=end_time,
                )
                if not notified:
                    logger.error("Notification failed", error=notify_err)

        return exit_code


def _build_task(task_name: TaskName) -> AgentTask:
    match task_name:
        case "agent_management":
            return AgentManagementTask(
                name="agent_management",
                task_key="agent_management",
                prompt_path=config.settings.task_prompts()["agent_management"],
            )
        case "document_coverage":
            return DocumentCoverageTask(
                name="document_coverage",
                task_key="doc_coverage",
                prompt_path=config.settings.task_prompts()["document_coverage"],
            )
        case "document_test_alignment":
            return DocumentTestAlignmentTask(
                name="document_test_alignment",
                task_key="test_coverage",
                prompt_path=config.settings.task_prompts()["document_test_alignment"],
            )
        case "debug_smoke_commit":
            return DebugSmokeCommitTask(
                name="debug_smoke_commit",
                task_key="debug_smoke_commit",
                prompt_path=config.settings.task_prompts()["debug_smoke_commit"],
            )
        case "debug_hello_world":
            return DebugSmokeCommitTask(
                name="debug_hello_world",
                task_key="debug_hello_world",
                prompt_path=config.settings.task_prompts()["debug_hello_world"],
            )
        case "debug_hello_simple":
            return DebugSmokeCommitTask(
                name="debug_hello_simple",
                task_key="debug_hello_simple",
                prompt_path=config.settings.task_prompts()["debug_hello_simple"],
                requires_commit=False,
            )
        case _:
            assert_never(task_name)


def _build_agent(agent_name: AgentName):
    env = {"PATH": f"{config.settings.path_prefix}:{os.environ.get('PATH', '')}"}
    match agent_name:
        case "codex":
            return CodexAgent(
                name="codex",
                binary=config.settings.codex_bin,
                subcommand="exec",
                base_args=[],
                env=env,
            )
        case "claude":
            return ClaudeAgent(
                name="claude",
                binary=config.settings.claude_bin,
                subcommand=None,
                base_args=[],
                env=env,
            )
        case "gemini":
            return GeminiAgent(
                name="gemini",
                binary=config.settings.gemini_bin,
                subcommand=None,
                base_args=[],
                env=env,
            )
        case "ollama":
            return OllamaAgent(
                name="ollama",
                binary=config.settings.ollama_bin,
                subcommand=None,
                base_args=[],
                env=env,
            )
        case "kilo":
            return KiloAgent(
                name="kilo",
                binary=config.settings.kilo_bin,
                subcommand=None,
                base_args=[],
                env=env,
            )
        case "opencode":
            return OpencodeAgent(
                name="opencode",
                binary=config.settings.opencode_bin,
                subcommand=None,
                base_args=[],
                env=env,
            )
        case "qwen":
            return QwenAgent(
                name="qwen",
                binary=config.settings.qwen_bin,
                subcommand=None,
                base_args=[],
                env=env,
            )
        case _:
            assert_never(agent_name)


def _format_elapsed(elapsed: float | timedelta) -> str:
    if isinstance(elapsed, timedelta):
        total_seconds = elapsed.total_seconds()
    else:
        total_seconds = elapsed
    minutes, secs = divmod(int(total_seconds), 60)
    return f"{minutes}m{secs:02d}s"


def _notify_success(
    run_ctx: RunContext,
    start_time: datetime,
    end_time: datetime,
    elapsed: float | timedelta,
    last_message: str,
    token_count: int | None,
    commit_summary: git.CommitSummary,
) -> tuple[bool, str | None]:
    start_str = start_time.strftime("%Y-%m-%d %H:%M:%S UTC")
    end_str = end_time.strftime("%Y-%m-%d %H:%M:%S UTC")
    elapsed_str = _format_elapsed(elapsed)
    token_line = f"tokens: {token_count}" if token_count is not None else "tokens: n/a"
    files_line = ", ".join(commit_summary.files_changed) or "(no files)"
    loc_line = f"+{commit_summary.insertions}/-{commit_summary.deletions}"
    commit_subjects = (
        "\n".join(
            f"- {commit.subject} ({commit.commit[:8]})"
            for commit in commit_summary.commits
        )
        or "(no commits)"
    )
    body = (
        f"agent: {run_ctx.agent_name}\n"
        f"task: {run_ctx.task_name}\n"
        f"start: {start_str}\n"
        f"end: {end_str}\n"
        f"elapsed: {elapsed_str}\n"
        f"{token_line}\n\n"
        f"commits:\n{commit_subjects}\n\n"
        f"files: {files_line}\n"
        f"loc: {loc_line}\n\n"
        f"last_message:\n{last_message}\n"
    )
    title = f"[{run_ctx.task_name}] {run_ctx.agent_name} — SUCCESS — {end_str}"
    return send_notification(
        title=title, body=body, priority="default", tags="white_check_mark"
    )


def _notify_error(
    run_ctx: RunContext,
    error_type: str,
    error_detail: str | None,
    start_time: datetime,
    end_time: datetime,
) -> tuple[bool, str | None]:
    start_str = start_time.strftime("%Y-%m-%d %H:%M:%S UTC")
    end_str = end_time.strftime("%Y-%m-%d %H:%M:%S UTC")
    elapsed = end_time - start_time
    elapsed_str = _format_elapsed(elapsed)

    detail_line = f"{error_detail}\n" if error_detail else ""
    body = (
        f"Agent: {run_ctx.agent_name}\n"
        f"Task: {run_ctx.task_name}\n"
        f"Start: {start_str}\n"
        f"End: {end_str}\n"
        f"Elapsed: {elapsed_str}\n\n"
        f"Error: {error_type}\n"
        f"{detail_line}"
    )
    title = f"[{run_ctx.task_name}] {run_ctx.agent_name} — FAILED"
    return send_notification(title=title, body=body, priority="high", tags="x")


@app.command("run")
def run(
    agent: AgentName = typer.Option(..., "--agent"),
    task: TaskName = typer.Option(..., "--task"),
    debug: bool = typer.Option(False, "--debug"),
    debug_prompt: str | None = typer.Option(None, "--debug-prompt"),
    dry_run: bool = typer.Option(False, "--dry-run"),
) -> int:
    args = OrchestratorArgs(
        agent=agent,
        task=task,
        debug=debug,
        debug_prompt=debug_prompt,
        dry_run=dry_run,
    )
    return Orchestrator(args=args).run()


@app.command("heartbeat")
def heartbeat() -> None:
    """Append a UTC timestamp to heartbeat.log and the heartbeat task log."""
    now = datetime.now(timezone.utc)
    line = now.strftime("%Y-%m-%d %H:%M:%S UTC") + "\n"

    repo_log = config.settings.repo_root / "heartbeat.log"
    with repo_log.open("a", encoding="utf-8") as f:
        f.write(line)

    task_log = config.settings.log_root / "heartbeat" / "task.log"
    task_log.parent.mkdir(parents=True, exist_ok=True)
    with task_log.open("a", encoding="utf-8") as f:
        f.write(line)


def main() -> None:
    app()
