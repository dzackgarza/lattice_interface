from __future__ import annotations

from dataclasses import dataclass

from git import Repo

from . import config


def _to_str(value: object) -> str:
    if isinstance(value, bytes):
        return value.decode("utf-8", "replace")
    if value is None:
        return ""
    return str(value)


@dataclass(frozen=True)
class CommitInfo:
    commit: str
    subject: str
    author: str
    date: str


@dataclass(frozen=True)
class CommitSummary:
    commits: list[CommitInfo]
    files_changed: list[str]
    insertions: int
    deletions: int


def _repo() -> Repo:
    return Repo(str(config.settings.repo_root))


def get_head() -> str:
    repo = _repo()
    return repo.head.commit.hexsha


def get_commits_between(head_before: str, head_after: str) -> list[CommitInfo]:
    if head_before == head_after:
        return []
    repo = _repo()
    commits: list[CommitInfo] = []
    for commit in repo.iter_commits(f"{head_before}..{head_after}", reverse=True):
        commits.append(
            CommitInfo(
                commit=_to_str(commit.hexsha),
                subject=_to_str(commit.summary),
                author=_to_str(commit.author.name),
                date=_to_str(commit.committed_datetime.isoformat()),
            )
        )
    return commits


def parse_numstat(output: str) -> tuple[list[str], int, int]:
    files: list[str] = []
    insertions = 0
    deletions = 0
    for line in output.splitlines():
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        add_str, del_str, path = parts
        if add_str.isdigit():
            insertions += int(add_str)
        if del_str.isdigit():
            deletions += int(del_str)
        files.append(path)
    return (sorted(set(files)), insertions, deletions)


def get_numstat_between(head_before: str, head_after: str) -> tuple[list[str], int, int]:
    if head_before == head_after:
        return ([], 0, 0)
    repo = _repo()
    output = repo.git.diff("--numstat", f"{head_before}..{head_after}")
    return parse_numstat(output)


def summarize_commits(head_before: str, head_after: str) -> CommitSummary:
    commits = get_commits_between(head_before, head_after)
    files, insertions, deletions = get_numstat_between(head_before, head_after)
    return CommitSummary(
        commits=commits,
        files_changed=files,
        insertions=insertions,
        deletions=deletions,
    )
