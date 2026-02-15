from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Domain = Literal["definite_only", "indefinite_only", "both"]


@dataclass(frozen=True)
class CapabilitySpec:
    id: str
    domain: Domain
    input_contract: str
    output_contract: str
    assertion_profile: str
    description: str


CAPABILITY_REGISTRY: dict[str, CapabilitySpec] = {
    "constructor.from_gram": CapabilitySpec(
        id="constructor.from_gram",
        domain="both",
        input_contract="integral/rational symmetric Gram matrix",
        output_contract="typed Lattice",
        assertion_profile="rank/gram/signature coherence",
        description="Construct lattice from Gram data.",
    ),
    "constructor.root": CapabilitySpec(
        id="constructor.root",
        domain="definite_only",
        input_contract="root type + rank",
        output_contract="RootLattice",
        assertion_profile="known invariants on canonical ADE/BCFG examples",
        description="Finite root-lattice constructors.",
    ),
    "constructor.hyperbolic": CapabilitySpec(
        id="constructor.hyperbolic",
        domain="indefinite_only",
        input_contract="rank >= 2",
        output_contract="HyperbolicLattice",
        assertion_profile="signature/witt/isotropic consistency",
        description="Hyperbolic-lattice constructors.",
    ),
    "invariant.rank": CapabilitySpec(
        id="invariant.rank",
        domain="both",
        input_contract="Lattice",
        output_contract="int",
        assertion_profile="matches dimension of Gram/basis data",
        description="Lattice rank invariant.",
    ),
    "invariant.signature": CapabilitySpec(
        id="invariant.signature",
        domain="both",
        input_contract="Lattice",
        output_contract="(p, q) pair",
        assertion_profile="p+q equals rank and matches definiteness predicates",
        description="Lattice signature invariant.",
    ),
    "invariant.determinant": CapabilitySpec(
        id="invariant.determinant",
        domain="both",
        input_contract="Lattice",
        output_contract="int|Fraction",
        assertion_profile="determinant/discriminant compatibility",
        description="Determinant invariant.",
    ),
    "invariant.discriminant": CapabilitySpec(
        id="invariant.discriminant",
        domain="both",
        input_contract="Lattice",
        output_contract="int|Fraction",
        assertion_profile="discriminant identities",
        description="Discriminant invariant family.",
    ),
    "pairing.bilinear": CapabilitySpec(
        id="pairing.bilinear",
        domain="both",
        input_contract="LatticeElement x LatticeElement",
        output_contract="scalar",
        assertion_profile="symmetry/bilinearity and consistency with norms",
        description="Element and lattice bilinear pairing.",
    ),
    "element.norm": CapabilitySpec(
        id="element.norm",
        domain="both",
        input_contract="LatticeElement",
        output_contract="scalar",
        assertion_profile="agreement with lattice-level norm/pairing",
        description="Element norm evaluation.",
    ),
    "reduction.lll": CapabilitySpec(
        id="reduction.lll",
        domain="definite_only",
        input_contract="integral positive-definite lattice/basis",
        output_contract="reduced basis/lattice",
        assertion_profile="determinant preserved + reduction predicate",
        description="LLL reduction family.",
    ),
    "reduction.bkz_hkz": CapabilitySpec(
        id="reduction.bkz_hkz",
        domain="definite_only",
        input_contract="integral positive-definite lattice/basis",
        output_contract="reduced basis/lattice",
        assertion_profile="determinant preserved + quality monotonicity",
        description="BKZ/HKZ reduction family.",
    ),
    "enumeration.short_vectors": CapabilitySpec(
        id="enumeration.short_vectors",
        domain="definite_only",
        input_contract="definite lattice + bound",
        output_contract="collection of vectors",
        assertion_profile="exact norms + expected representative membership",
        description="Short-vector enumeration.",
    ),
    "enumeration.closest_vectors": CapabilitySpec(
        id="enumeration.closest_vectors",
        domain="definite_only",
        input_contract="definite lattice + target",
        output_contract="closest vector(s)",
        assertion_profile="distance optimality contract",
        description="Closest vector algorithms.",
    ),
    "enumeration.minimum_kissing": CapabilitySpec(
        id="enumeration.minimum_kissing",
        domain="definite_only",
        input_contract="definite lattice",
        output_contract="minimum/kissing numbers",
        assertion_profile="canonical exact values on small examples",
        description="Minimum and kissing number functionality.",
    ),
    "isometry.orthogonal_group": CapabilitySpec(
        id="isometry.orthogonal_group",
        domain="both",
        input_contract="Lattice",
        output_contract="group object",
        assertion_profile="generator action preserves form",
        description="Orthogonal/isometry group operations.",
    ),
    "isometry.orbits_stabilizers": CapabilitySpec(
        id="isometry.orbits_stabilizers",
        domain="indefinite_only",
        input_contract="indefinite lattice + vectors",
        output_contract="orbit/stabilizer data",
        assertion_profile="same_orbit equivalence + isotropic invariance",
        description="Orbit and stabilizer algorithms in indefinite regimes.",
    ),
    "indefinite.isotropic_vectors": CapabilitySpec(
        id="indefinite.isotropic_vectors",
        domain="indefinite_only",
        input_contract="indefinite lattice",
        output_contract="isotropic witness/representatives",
        assertion_profile="norm 0 + primitivity/orbit non-conjugacy",
        description="Isotropic-vector existence and enumeration.",
    ),
    "indefinite.witt": CapabilitySpec(
        id="indefinite.witt",
        domain="indefinite_only",
        input_contract="indefinite lattice",
        output_contract="Witt index and predicates",
        assertion_profile="Witt/signature compatibility",
        description="Witt-index and indefinite predicates.",
    ),
    "substructure.sublattice": CapabilitySpec(
        id="substructure.sublattice",
        domain="both",
        input_contract="ambient lattice + generators",
        output_contract="SubLattice",
        assertion_profile="rank/determinant/containment contracts",
        description="Sublattice and orthogonal-complement style operations.",
    ),
    "substructure.quotient": CapabilitySpec(
        id="substructure.quotient",
        domain="both",
        input_contract="Lattice and sublattice",
        output_contract="LatticeQuotient",
        assertion_profile="order and identity laws",
        description="Quotients by sublattices.",
    ),
    "substructure.dual": CapabilitySpec(
        id="substructure.dual",
        domain="both",
        input_contract="Lattice",
        output_contract="RationalLattice|Lattice",
        assertion_profile="det(L)*det(L^vee) identities",
        description="Dual-lattice functionality.",
    ),
    "discriminant.group": CapabilitySpec(
        id="discriminant.group",
        domain="both",
        input_contract="Lattice",
        output_contract="LatticeDiscriminantGroup",
        assertion_profile="group order = |det| for integral samples",
        description="Discriminant-group construction and order.",
    ),
    "discriminant.forms": CapabilitySpec(
        id="discriminant.forms",
        domain="both",
        input_contract="Discriminant group elements",
        output_contract="bilinear/quadratic values",
        assertion_profile="torsion + quadratic/bilinear relations",
        description="Discriminant bilinear and quadratic forms.",
    ),
    "root.reflection": CapabilitySpec(
        id="root.reflection",
        domain="indefinite_only",
        input_contract="reflective root",
        output_contract="orthogonal group element",
        assertion_profile="s(r)=-r, involution, form preservation",
        description="Root reflections.",
    ),
    "root.orthogonal_hyperplane": CapabilitySpec(
        id="root.orthogonal_hyperplane",
        domain="indefinite_only",
        input_contract="root vector",
        output_contract="LatticeHyperplane",
        assertion_profile="hyperplane orthogonality contract",
        description="Root orthogonal hyperplanes.",
    ),
    "coxeter.vinberg": CapabilitySpec(
        id="coxeter.vinberg",
        domain="indefinite_only",
        input_contract="hyperbolic/indefinite lattice",
        output_contract="CoxeterData",
        assertion_profile="simple root norms + root-system consistency",
        description="Vinberg/Coxeter-domain algorithms.",
    ),
    "root_system.isomorphism": CapabilitySpec(
        id="root_system.isomorphism",
        domain="both",
        input_contract="LatticeRootSystem pair",
        output_contract="bool",
        assertion_profile="positive/negative isomorphism witnesses",
        description="Root-system isomorphism checks.",
    ),
    "genus.local_global": CapabilitySpec(
        id="genus.local_global",
        domain="both",
        input_contract="lattice/genus object",
        output_contract="genus invariants, local symbols, mass",
        assertion_profile="local-global compatibility identities",
        description="Genus/local-density style functionality.",
    ),
    "nemo.normal_forms": CapabilitySpec(
        id="nemo.normal_forms",
        domain="both",
        input_contract="integer matrix/lattice basis",
        output_contract="HNF/SNF data (+ transforms)",
        assertion_profile="reconstruction identities with transforms",
        description="HNF/SNF and related normal-form algorithms.",
    ),
    "matrix.linear_algebra": CapabilitySpec(
        id="matrix.linear_algebra",
        domain="both",
        input_contract="matrix / linear map data",
        output_contract="matrix / decomposition / solution data",
        assertion_profile="rank/kernel/image/solve consistency identities",
        description="General matrix and linear-algebra algorithms used by lattice workflows.",
    ),
    "number_field.algorithms": CapabilitySpec(
        id="number_field.algorithms",
        domain="both",
        input_contract="number field / order / ideals",
        output_contract="arithmetic invariants and structures",
        assertion_profile="field/order/arithmetic identity checks",
        description="Number-field and ideal arithmetic algorithms supporting lattice workflows.",
    ),
    "quadratic_form.local_algorithms": CapabilitySpec(
        id="quadratic_form.local_algorithms",
        domain="both",
        input_contract="quadratic form and local data",
        output_contract="local invariants/densities/symbols",
        assertion_profile="local-global density and symbol compatibility",
        description="Quadratic-form local and density algorithms.",
    ),
    "quadratic_form.transformations": CapabilitySpec(
        id="quadratic_form.transformations",
        domain="both",
        input_contract="quadratic form + substitutions/operations",
        output_contract="transformed equivalent forms and coefficients",
        assertion_profile="equivalence and invariant preservation",
        description="Quadratic-form transformation and reduction families.",
    ),
    "module.structure": CapabilitySpec(
        id="module.structure",
        domain="both",
        input_contract="module/lattice/submodule objects",
        output_contract="module relations, closures, intersections",
        assertion_profile="containment/index/closure laws",
        description="Module and submodule structure operations.",
    ),
    "interface.conversions": CapabilitySpec(
        id="interface.conversions",
        domain="both",
        input_contract="lattice/form/field object",
        output_contract="bridge object in another representation",
        assertion_profile="roundtrip and invariant preservation checks",
        description="Cross-representation conversion and bridge operations.",
    ),
    "toric.lattice_geometry": CapabilitySpec(
        id="toric.lattice_geometry",
        domain="both",
        input_contract="toric lattice / cones / polytopes",
        output_contract="lattice-geometry derived structures",
        assertion_profile="duality and incidence invariants",
        description="Toric/lattice geometry functionality.",
    ),
    "combinatorics.enumeration": CapabilitySpec(
        id="combinatorics.enumeration",
        domain="both",
        input_contract="algebraic structure + constraints",
        output_contract="enumerated representatives/classes",
        assertion_profile="count and representative correctness checks",
        description="Enumeration/classification algorithms beyond short vectors.",
    ),
}


def capabilities_by_domain(domain: Domain) -> set[str]:
    return {cid for cid, spec in CAPABILITY_REGISTRY.items() if spec.domain == domain}


def all_capabilities() -> set[str]:
    return set(CAPABILITY_REGISTRY)
