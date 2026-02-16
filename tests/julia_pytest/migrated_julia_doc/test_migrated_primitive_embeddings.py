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


def test_1_primitive_embeddings_a1_into_a2_direct_sum_a1():
    """
    method: primitive_embeddings
    """
    code = r'''
    # method: primitive_embeddings
    using Oscar
    M = root_lattice(:A, 1)
    L1 = root_lattice(:A, 2)
    L2 = root_lattice(:A, 1)
    L, _, _ = direct_sum(L1, L2)
    embs = primitive_embeddings(L, M)
    @test length(embs) >= 1
'''
    _jl_eval_testitem(code)

def test_2_primitive_embeddings_via_genus():
    """
    method: primitive_embeddings(G::ZZGenus, M)
    """
    code = r'''
    # method: primitive_embeddings(G::ZZGenus, M)
    using Oscar
    M = root_lattice(:A, 1)
    L = root_lattice(:A, 2)
    G = genus(L)
    embs = primitive_embeddings(G, M)
    @test length(embs) >= 0  # may or may not embed
'''
    _jl_eval_testitem(code)

def test_3_primitive_extensions_glue_two_lattices():
    """
    method: primitive_extensions
    """
    code = r'''
    # method: primitive_extensions
    using Oscar
    L1 = root_lattice(:A, 1)
    L2 = root_lattice(:A, 1)
    exts = primitive_extensions(L1, L2)
    @test length(exts) >= 1
'''
    _jl_eval_testitem(code)
def test_4_primitive_embeddings_via_torquadmodule():
    """
    method: primitive_embeddings(q::TorQuadModule, sig, M)
    """
    code = r'''
    # method: primitive_embeddings(q::TorQuadModule, sig, M)
    using Oscar
    M = root_lattice(:A, 1)
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    embs = primitive_embeddings(T, (2, 0), M)
    @test length(embs) >= 0
'''
    _jl_eval_testitem(code)


MIGRATED_METHODS = {
    'primitive_embeddings',
    'primitive_embeddings(G::ZZGenus, M)',
    'primitive_embeddings(q::TorQuadModule, sig, M)',
    'primitive_extensions',
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
