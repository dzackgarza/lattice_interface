from __future__ import annotations

import sys
import pytest

pytest.importorskip("sage.all")
from sage.all import CartanType, RootSystem
from .conftest import assert_runtime_methods_covered


def test_rootsystem_simple_root_scalar_recovers_cartan_entry():
    """
    method: scalar

    scalar(alpha, alphacheck) gives Cartan pairing <alpha, alpha^vee>.
    Assertion: For A2, an off-diagonal Cartan entry is -1.
    """
    L = RootSystem(["A", 2]).root_lattice()
    a = L.simple_roots()
    ac = L.simple_coroots()
    actual = a[1].scalar(ac[2])
    expected = -1
    assert actual == expected, (
        f"RootSystem.scalar Cartan entry mismatch: actual={actual}, expected={expected}"
    )


def test_rootsystem_positive_roots_count_matches_type_a2():
    """
    method: positive_roots

    positive_roots() returns all positive roots in the chosen realization.
    Assertion: Type A2 has exactly three positive roots.
    """
    L = RootSystem(["A", 2]).root_lattice()
    actual = len(list(L.positive_roots()))
    expected = 3
    assert actual == expected, (
        f"RootSystem.positive_roots count mismatch: actual={actual}, expected={expected}"
    )


def test_rootsystem_highest_root_is_positive():
    """
    method: highest_root

    highest_root() returns the maximal positive root in the root poset.
    Assertion: Returned root is contained in positive_roots().
    """
    L = RootSystem(["A", 2]).root_lattice()
    highest = L.highest_root()
    actual = highest in L.positive_roots()
    expected = True
    assert actual == expected, (
        f"RootSystem.highest_root membership mismatch: actual={actual}, expected={expected}, highest={highest}"
    )


def test_rootsystem_cartan_type_rank_matches_lattice_dimension():
    """
    method: root_lattice

    root_lattice() builds the free Z-module realization attached to the Cartan type.
    Assertion: Lattice dimension equals Cartan rank.
    """
    ct = CartanType(["A", 3])
    L = RootSystem(["A", 3]).root_lattice()
    actual = L.dimension()
    expected = ct.rank()
    assert actual == expected, (
        f"RootSystem.root_lattice dimension mismatch: actual={actual}, expected={expected}"
    )


def test_rootsystem_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant root-lattice runtime method should
    correspond to at least one explicit test method tag in this module.
    """
    sample = RootSystem(["A", 3]).root_lattice()
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.combinat.root_system",),
    )
