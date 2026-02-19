from typing import Any, Callable, TypeVar, overload

_F = TypeVar("_F", bound=Callable[..., Any])

class Typer:
    def __init__(self, *, add_completion: bool = ...) -> None: ...
    def command(self, name: str = ...) -> Callable[[_F], _F]: ...

TyperOption: Any
Option: Any

@overload
def Option(default: Any = ..., *param_decls: str, **kwargs: Any) -> Any: ...
@overload
def Option(*param_decls: str, **kwargs: Any) -> Any: ...

def Exit(code: int = ...) -> None: ...
