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


def test_1_is_isometry_identity_is_an_isometry():
    """
    method: is_isometry
    """
    code = r'''
    # method: is_isometry
    using Oscar
    L = root_lattice(:A, 2)
    f = identity_matrix(ZZ, 2)
    @test is_isometry(L, f) == true
'''
    _jl_eval_testitem(code)

def test_2_is_isometry_non_isometry_detected():
    """
    method: is_isometry
    """
    code = r'''
    # method: is_isometry
    using Oscar
    L = root_lattice(:A, 2)
    f = ZZ[2 0; 0 1]
    @test is_isometry(L, f) == false
'''
    _jl_eval_testitem(code)

def test_3_is_isometry_negation_is_an_isometry():
    """
    method: is_isometry
    """
    code = r'''
    # method: is_isometry
    using Oscar
    L = root_lattice(:A, 2)
    f = -identity_matrix(ZZ, 2)
    @test is_isometry(L, f) == true
'''
    _jl_eval_testitem(code)

def test_4_saturation_primitive_closure_in_lattice():
    """
    method: saturation
    """
    code = r'''
    # method: saturation
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L))
    S = saturation(L, M)
    @test is_primitive(L, S) == true
'''
    _jl_eval_testitem(code)

def test_5_is_saturated_with_saturation_test_and_compute():
    """
    method: is_saturated_with_saturation
    """
    code = r'''
    # method: is_saturated_with_saturation
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L))
    flag, S = is_saturated_with_saturation(L, M)
    @test flag == false
    @test is_primitive(L, S) == true
'''
    _jl_eval_testitem(code)

MIGRATED_METHODS = {
    'is_isometry',
    'is_saturated_with_saturation',
    'saturation',
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
