from __future__ import annotations

import os
from pathlib import Path

import pytest


# Julia runtime for juliacall must come from the managed project runtime,
# not from any system-wide Julia installation.
_HOME = Path("/tmp/sage-home")
_PROJECT = _HOME / "julia_env"
_DEPOT = _HOME / ".julia"
_MANAGED_JULIA = _PROJECT / "pyjuliapkg" / "install" / "bin" / "julia"

_HOME.mkdir(parents=True, exist_ok=True)
_PROJECT.mkdir(parents=True, exist_ok=True)
_DEPOT.mkdir(parents=True, exist_ok=True)

os.environ["HOME"] = str(_HOME)
os.environ["PYTHON_JULIAPKG_PROJECT"] = str(_PROJECT)
os.environ["JULIA_DEPOT_PATH"] = str(_DEPOT)
os.environ["PYTHON_JULIAPKG_EXE"] = str(_MANAGED_JULIA)
os.environ["PYTHON_JULIAPKG_OFFLINE"] = "yes"

if not _MANAGED_JULIA.exists():
    raise RuntimeError(
        "Managed Julia runtime not found at "
        f"{_MANAGED_JULIA}. Install/initialize juliacall runtime first; "
        "system Julia is intentionally not allowed for these tests."
    )

from juliacall import Main as jl


@pytest.fixture(scope="session", autouse=True)
def _init_julia_oscar_runtime() -> None:
    jl.seval("using Pkg")
    jl.seval('Pkg.activate("tests/julia_doc")')
    jl.seval("using Nemo")
    jl.seval("using Hecke")
    jl.seval("using Oscar")
    jl.seval("using Test")
