from typing import Any

class LocalPath:
    def __getitem__(self, item: str) -> LocalCommand: ...

class LocalCommand:
    def run(
        self, _env: dict[str, str] | None = ..., retcode: int | None = ..., **kwargs: Any
    ) -> tuple[int, str, str]: ...

local: LocalPath
