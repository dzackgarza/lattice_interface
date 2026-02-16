from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from .conftest import assert_equal
from .types import (
    DiscriminantFormIsometry,
    DiscriminantOrthogonalGroup,
    Lattice,
    LatticeGlueData,
    LatticeOrthogonalSubgroup,
    LatticePrimitiveEmbedding,
    LatticeAutomorphism,
)


def test_lattice_direct_sum_and_glued_construction_interfaces():
    """
    method: direct_sum

    Gluing-workflow contract:
    interface exposes direct-sum construction and glued-model recognition.
    """
    u: Lattice = Lattice.U()
    two_u: Lattice = u.direct_sum(u)
    disc_u = u.discriminant()
    glue: LatticeGlueData = disc_u.isotropic_subgroups()[0]

    assert_equal(two_u.rank(), 4, f"Expected rank(U⊕U)=4 in contract example: rank={two_u.rank()}")
    assert_equal(
        two_u.is_glued_from(u, u, glue),
        True,
        f"Expected direct sum model to be recognized as glue realization in trivial case: lattice={two_u}",
    )


def test_lattice_primitive_complement_and_embedding_glue_isometry_interfaces():
    """
    method: primitive_complement_in

    Embedding-workflow contract:
    primitive embeddings expose complements and their discriminant-form glue isometries.
    """
    u: Lattice = Lattice.U()
    embeddings: tuple[LatticePrimitiveEmbedding, ...] = u.primitive_embeddings(u)
    emb: LatticePrimitiveEmbedding = embeddings[0]
    comp: Lattice = u.primitive_complement_in(u, embedding=emb)
    glue_iso: DiscriminantFormIsometry = emb.glue_isometry()

    assert_equal(comp.rank(), 0, f"Expected rank-0 primitive complement for identity embedding: comp={comp}")
    assert_equal(
        glue_iso.is_anti_isometry(),
        True,
        "Expected primitive-embedding glue map to be represented as anti-isometry in contract interface",
    )


def test_lattice_discriminant_automorphism_image_interface():
    """
    method: automorphism_group_on_discriminant

    Automorphism-workflow contract:
    image of lattice isometries in O(A_L) is explicitly queryable.
    """
    u: Lattice = Lattice.U()
    image_default: DiscriminantOrthogonalGroup = u.automorphism_group_on_discriminant()
    subgroup: LatticeOrthogonalSubgroup = u.orthogonal_set_stabilizer([u.element((1, 0))])
    image_subgroup: DiscriminantOrthogonalGroup = u.automorphism_group_on_discriminant(subgroup=subgroup)
    id_default = image_default.identity()
    id_subgroup = image_subgroup.identity()

    assert_equal(
        image_default.contains(id_default),
        True,
        "Image of O(L) in O(A_L) should contain identity discriminant automorphism",
    )
    assert_equal(
        image_subgroup.contains(id_subgroup),
        True,
        "Image of subgroup in O(A_L) should contain identity discriminant automorphism",
    )


def test_lattice_glue_compatibility_and_lift_decision_interfaces():
    """
    method: automorphism_lifts_to_overlattice

    Lifting-workflow contract:
    liftability decision is exposed independently for a fixed gluing context.
    """
    u: Lattice = Lattice.U()
    id_u: LatticeAutomorphism = u.orthogonal_group().identity()
    glue: LatticeGlueData = u.discriminant().isotropic_subgroups()[0]

    assert_equal(
        u.automorphism_lifts_to_overlattice(id_u, u, glue),
        True,
        "Identity automorphism should be liftable in trivial contract case",
    )


def test_lattice_lift_construction_and_liftable_subgroup_interfaces():
    """
    method: extend_automorphism_to_overlattice

    Lifting-workflow contract:
    interface provides both explicit lift construction and subgroup-level liftability filter.
    """
    u: Lattice = Lattice.U()
    id_u: LatticeAutomorphism = u.orthogonal_group().identity()
    glue: LatticeGlueData = u.discriminant().isotropic_subgroups()[0]

    lifted: LatticeAutomorphism = u.extend_automorphism_to_overlattice(id_u, u, glue)
    liftable: LatticeOrthogonalSubgroup = u.liftable_automorphisms(u, glue)

    assert_equal(lifted in liftable, True, "Lifted automorphism should belong to liftable subgroup")


def test_lattice_glue_compatibility_identity_pair():
    """
    method: glue_compatibility

    Lifting-workflow contract:
    identity automorphisms on summands are glue-compatible for trivial isotropic gluing.
    """
    u: Lattice = Lattice.U()
    id_u: LatticeAutomorphism = u.orthogonal_group().identity()
    glue: LatticeGlueData = u.discriminant().isotropic_subgroups()[0]
    assert_equal(
        u.glue_compatibility(id_u, id_u, glue),
        True,
        "Identity summand automorphisms should satisfy glue compatibility in trivial contract example",
    )


def test_lattice_structured_automorphism_lifting_result_interface():
    """
    method: automorphism_lifting_result

    Lifting-workflow contract:
    theorem decision can be returned as structured data with boolean, witness, and obstruction.
    """
    u: Lattice = Lattice.U()
    id_u: LatticeAutomorphism = u.orthogonal_group().identity()
    glue: LatticeGlueData = u.discriminant().isotropic_subgroups()[0]

    result: tuple[bool, LatticeAutomorphism | None, str | None] = u.automorphism_lifting_result(id_u, u, glue)
    lifts, witness, obstruction = result
    liftable: LatticeOrthogonalSubgroup = u.liftable_automorphisms(u, glue)
    assert_equal(lifts, True, f"Expected identity to be liftable in contract example: result={result}")
    assert_equal(obstruction, None, f"Expected no obstruction for liftable identity: result={result}")
    assert_equal(
        witness in liftable,
        True,
        f"Expected witness to be an element of the liftable subgroup: result={result}",
    )
