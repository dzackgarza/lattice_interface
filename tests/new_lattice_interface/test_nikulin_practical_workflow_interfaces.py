from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from .conftest import assert_equal
from .types import (
    Lattice,
    LatticeDiscriminantGroup,
    LatticeGlueData,
    LatticePrimitiveEmbedding,
)


def test_lattice_is_isometric_small_known_examples():
    """
    method: is_isometric

    Practical classification contract:
    isometry query distinguishes equal-model hyperbolic aliases from non-isometric signatures.
    """
    u: Lattice = Lattice.U()
    h: Lattice = Lattice.H()
    e8: Lattice = Lattice.E(8)

    assert_equal(u.is_isometric(h), True, f"Expected U and H to be isometric in contract model: U={u}, H={h}")
    assert_equal(
        u.is_isometric(e8),
        False,
        f"Expected non-isometry for different signatures: U.sig={u.signature()}, E8.sig={e8.signature()}",
    )


def test_lattice_primitive_embedding_queries_for_identity_case():
    """
    method: primitive_embedding_exists

    Practical classification contract:
    any lattice admits the identity primitive embedding into itself.
    """
    u: Lattice = Lattice.U()
    assert_equal(
        u.primitive_embedding_exists(u),
        True,
        f"Expected identity primitive embedding to exist for lattice: U={u}",
    )


def test_lattice_primitive_embeddings_returns_typed_embedding_objects():
    """
    method: primitive_embeddings

    Practical classification contract:
    primitive embedding enumeration returns typed embedding records for small identity case.
    """
    u: Lattice = Lattice.U()
    embeddings: tuple[LatticePrimitiveEmbedding, ...] = u.primitive_embeddings(u)
    assert_equal(len(embeddings), 1, f"Expected unique identity primitive embedding in contract model: {embeddings}")
    emb = embeddings[0]
    assert_equal(emb.source().is_isometric(u), True, f"Embedding source mismatch for U->U identity case: emb={emb}")
    assert_equal(emb.target().is_isometric(u), True, f"Embedding target mismatch for U->U identity case: emb={emb}")


def test_lattice_orthogonal_complement_in_for_identity_embedding():
    """
    method: orthogonal_complement_in

    Practical classification contract:
    orthogonal complement of identity embedding U -> U is rank-0 in this contract model.
    """
    u: Lattice = Lattice.U()
    comp: Lattice = u.orthogonal_complement_in(u)
    assert_equal(comp.rank(), 0, f"Expected rank-0 orthogonal complement for identity embedding: comp={comp}")


def test_discriminant_form_isotropic_subgroups_returns_glue_data():
    """
    method: isotropic_subgroups

    Practical classification contract:
    isotropic-subgroup enumeration on discriminant form returns typed glue data.
    """
    disc_u: LatticeDiscriminantGroup = Lattice.U().discriminant()
    glue_candidates: tuple[LatticeGlueData, ...] = disc_u.isotropic_subgroups()
    assert_equal(len(glue_candidates), 1, f"Expected unique trivial isotropic subgroup for A_U=0: {glue_candidates}")
    glue0 = glue_candidates[0]
    assert_equal(glue0.is_isotropic(), True, f"Trivial glue datum should be isotropic: glue={glue0}")
    assert_equal(
        glue0.subgroup_generators(),
        tuple(),
        f"Trivial isotropic subgroup should have empty generator set in contract model: glue={glue0}",
    )


def test_lattice_overlattice_from_glue_roundtrip_on_trivial_glue():
    """
    method: overlattice_from_glue

    Practical classification contract:
    applying trivial isotropic glue for U returns an overlattice isometric to U.
    """
    u: Lattice = Lattice.U()
    disc_u: LatticeDiscriminantGroup = u.discriminant()
    trivial_glue: LatticeGlueData = disc_u.isotropic_subgroups()[0]
    over_u: Lattice = u.overlattice_from_glue(trivial_glue)

    assert_equal(over_u.is_isometric(u), True, f"Expected trivial-glue overlattice to stay isometric to U: over={over_u}")


def test_lattice_glue_data_inverse_direction_contract():
    """
    method: glue_data

    Practical classification contract:
    glue-data extraction from an overlattice produces isotropic glue compatible with base discriminant form.
    """
    u: Lattice = Lattice.U()
    disc_u: LatticeDiscriminantGroup = u.discriminant()
    trivial_glue: LatticeGlueData = disc_u.isotropic_subgroups()[0]
    over_u: Lattice = u.overlattice_from_glue(trivial_glue)
    recovered: LatticeGlueData = u.glue_data(over_u)

    assert_equal(recovered.is_isotropic(), True, f"Recovered glue should be isotropic: recovered={recovered}")
    assert_equal(
        recovered.base_discriminant_form().is_isomorphic(disc_u),
        True,
        "Recovered glue must reference base discriminant form isomorphic to the starting one",
    )


def test_lattice_overlattices_lists_concrete_small_candidates():
    """
    method: overlattices

    Practical classification contract:
    overlattice enumeration contains at least the base lattice itself for U.
    """
    u: Lattice = Lattice.U()
    candidates: tuple[Lattice, ...] = u.overlattices()
    assert_equal(len(candidates), 1, f"Expected only base lattice as overlattice in trivial contract model: {candidates}")
    assert_equal(candidates[0].is_isometric(u), True, f"Expected sole overlattice candidate to be isometric to U: {candidates}")
