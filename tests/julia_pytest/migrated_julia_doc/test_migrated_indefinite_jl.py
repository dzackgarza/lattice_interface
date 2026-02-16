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


@pytest.mark.tdd_red
def test_1_indef_form_test_equivalence_two_equivalent_forms():
    """
    method: INDEF_FORM_TestEquivalence
    """
    # Indefinite.jl is not installed in the Julia env yet.
    # Two copies of the hyperbolic plane U = [[0,1],[1,0]] should be equivalent.
    code = r'''
    # method: INDEF_FORM_TestEquivalence
    using Oscar
    # Requires: using Indefinite
    Q1 = ZZ[0 1; 1 0]
    Q2 = ZZ[0 1; 1 0]
    result = INDEF_FORM_TestEquivalence(Q1, Q2)
    # Returns a unimodular matrix T such that T' * Q1 * T == Q2
    @test result !== nothing
    T = result
    @test T * Q1 * transpose(T) == Q2
    @test abs(det(T)) == 1
'''
    _jl_eval_testitem(code)


@pytest.mark.tdd_red
def test_2_indef_form_automorphism_group_hyperbolic_plane():
    """
    method: INDEF_FORM_AutomorphismGroup
    """
    # Indefinite.jl is not installed in the Julia env yet.
    # Aut(U) for the hyperbolic plane is infinite but finitely generated.
    code = r'''
    # method: INDEF_FORM_AutomorphismGroup
    using Oscar
    # Requires: using Indefinite
    Q = ZZ[0 1; 1 0]
    gens = INDEF_FORM_AutomorphismGroup(Q)
    @test length(gens) >= 1
    G = Q
    for g in gens
        @test g * G * transpose(g) == G
    end
'''
    _jl_eval_testitem(code)


@pytest.mark.tdd_red
def test_3_indef_form_get_orbit_representative_isotropic_vectors():
    """
    method: INDEF_FORM_GetOrbitRepresentative
    """
    # Indefinite.jl is not installed in the Julia env yet.
    # For U, C=0 gives primitive isotropic vectors; there should be orbits.
    code = r'''
    # method: INDEF_FORM_GetOrbitRepresentative
    using Oscar
    # Requires: using Indefinite
    Q = ZZ[0 1; 1 0]
    C = 0
    reps = INDEF_FORM_GetOrbitRepresentative(Q, C)
    @test length(reps) >= 1
    for v in reps
        @test transpose(v) * Q * v == C
    end
'''
    _jl_eval_testitem(code)


@pytest.mark.tdd_red
def test_4_indef_form_get_orbit_isotropic_kplane():
    """
    method: INDEF_FORM_GetOrbit_IsotropicKplane
    """
    # Indefinite.jl is not installed in the Julia env yet.
    # For U (sig (1,1)), k=1 totally isotropic subspaces exist.
    code = r'''
    # method: INDEF_FORM_GetOrbit_IsotropicKplane
    using Oscar
    # Requires: using Indefinite
    Q = ZZ[0 1; 1 0]
    k = 1
    orbits = INDEF_FORM_GetOrbit_IsotropicKplane(Q, k)
    @test length(orbits) >= 1
'''
    _jl_eval_testitem(code)


@pytest.mark.tdd_red
def test_5_indef_form_get_orbit_isotropic_kflag():
    """
    method: INDEF_FORM_GetOrbit_IsotropicKflag
    """
    # Indefinite.jl is not installed in the Julia env yet.
    code = r'''
    # method: INDEF_FORM_GetOrbit_IsotropicKflag
    using Oscar
    # Requires: using Indefinite
    Q = ZZ[0 1; 1 0]
    k = 1
    flags = INDEF_FORM_GetOrbit_IsotropicKflag(Q, k)
    @test length(flags) >= 1
'''
    _jl_eval_testitem(code)


MIGRATED_METHODS = {
    'INDEF_FORM_TestEquivalence',
    'INDEF_FORM_AutomorphismGroup',
    'INDEF_FORM_GetOrbitRepresentative',
    'INDEF_FORM_GetOrbit_IsotropicKplane',
    'INDEF_FORM_GetOrbit_IsotropicKflag',
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
