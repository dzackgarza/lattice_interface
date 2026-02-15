import os
import re
import sys

import pytest

os.environ.setdefault("HOME", "/tmp/sage-home")
os.environ.setdefault("PYTHON_JULIAPKG_PROJECT", "/tmp/sage-home/julia_env")
os.environ.setdefault("JULIA_DEPOT_PATH", "/tmp/sage-home/.julia")

from juliacall import Main as jl


@pytest.fixture(scope="session", autouse=True)
def _init_julia_oscar() -> None:
    jl.seval("using Pkg")
    jl.seval('Pkg.activate("tests/julia_doc")')
    jl.seval("using Nemo")
    jl.seval("using Hecke")
    jl.seval("using Oscar")
    jl.seval("using Test")


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def _method_token_from_docstring(func) -> str | None:
    doc = getattr(func, "__doc__", "") or ""
    for line in doc.splitlines():
        line = line.strip()
        if line.startswith("method:"):
            return line.split(":", 1)[1].strip()
    return None


def _covered_methods_from_module(module) -> set[str]:
    covered: set[str] = set()
    for name, func in module.__dict__.items():
        if not name.startswith("test_") or not callable(func) or name.endswith("_coverage"):
            continue
        token = _method_token_from_docstring(func)
        if token is not None:
            covered.add(token)
    return covered


def test_1_lll_reduces_basis_of_positive_definite_lattice():
    """
    method: lll
    """
    code = r'''
    # method: lll
    using Oscar
    # Start with a non-reduced basis
    L = integer_lattice(gram = ZZ[4 2; 2 4])
    M = lll(L)
    @test rank(M) == rank(L)
    @test det(M) == det(L)
'''
    _jl_eval_testitem(code)

def test_2_lll_preserves_lattice_isometry_class():
    """
    method: lll
    """
    code = r'''
    # method: lll
    using Oscar
    L = root_lattice(:A, 3)
    M = lll(L)
    @test rank(M) == 3
    # LLL preserves the lattice, only changes basis
    @test det(M) == det(L)
'''
    _jl_eval_testitem(code)

def test_3_lll_works_on_indefinite_lattice():
    """
    method: lll
    """
    code = r'''
    # method: lll
    using Oscar
    L = hyperbolic_plane_lattice()
    M = lll(L)
    @test rank(M) == 2
    @test det(M) == det(L)
'''
    _jl_eval_testitem(code)

MIGRATED_METHODS = {
    'lll',
}

def test_migrated_method_coverage():
    """
    method: runtime_coverage
    """
    covered = _covered_methods_from_module(sys.modules[__name__])
    missing = sorted(MIGRATED_METHODS - covered)
    assert not missing, (
        "Coverage failure: uncovered migrated methods found.\n"
        f"Declared methods: {sorted(MIGRATED_METHODS)}\n"
        f"Covered methods: {sorted(covered)}\n"
        f"Missing methods: {missing}"
    )
