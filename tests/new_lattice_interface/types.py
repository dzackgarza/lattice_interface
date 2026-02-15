from __future__ import annotations

from abc import ABC
from fractions import Fraction

try:
    from pydantic import BaseModel, ConfigDict
except ModuleNotFoundError:
    class BaseModel:  # pragma: no cover - fallback for minimal test environments
        pass

    class ConfigDict(dict):  # pragma: no cover - fallback for minimal test environments
        def __init__(self, **kwargs):
            super().__init__(**kwargs)


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: actual={actual}, expected={expected}")


class LatticeElement(BaseModel, ABC):
    """Base lattice-element contract."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def coords(self) -> tuple[int, ...]:
        assert False, "stub: LatticeElement.coords"

    def norm(self) -> int:
        assert False, "stub: LatticeElement.norm"

    def __mul__(self, other: LatticeElement) -> int:
        assert False, "stub: LatticeElement.__mul__"

    def __iter__(self):
        assert False, "stub: LatticeElement.__iter__"

    def perp(self) -> SubLattice:
        assert False, "stub: LatticeElement.perp"


class LatticeHyperplane(BaseModel, ABC):
    """Hyperplane contract in a lattice ambient space."""

    model_config = ConfigDict(arbitrary_types_allowed=True)


class SageMatrix(BaseModel, ABC):
    """Sage matrix contract type."""

    model_config = ConfigDict(arbitrary_types_allowed=True)


class OrthogonalGroupElement(BaseModel, ABC):
    """Element contract for O(L)."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __call__(self, x: LatticeElement) -> LatticeElement:
        assert False, "stub: OrthogonalGroupElement.__call__"


class RootLatticeElement(LatticeElement, ABC):
    """Root-lattice element contract."""

    def reflection(self) -> OrthogonalGroupElement:
        assert False, "stub: RootLatticeElement.reflection"

    def orthogonal_hyperplane(self) -> LatticeHyperplane:
        assert False, "stub: RootLatticeElement.orthogonal_hyperplane"


class Lattice(BaseModel, ABC):
    """Base lattice constructor contract and factory."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    def from_gram(cls, gram: SageMatrix) -> Lattice:
        assert False, "stub: Lattice.from_gram"

    @classmethod
    def hyperbolic(cls, *, rank: int) -> HyperbolicLattice:
        assert False, "stub: Lattice.hyperbolic"

    @classmethod
    def U(cls) -> HyperbolicLattice:
        assert False, "stub: Lattice.U"

    @classmethod
    def H(cls) -> HyperbolicLattice:
        assert False, "stub: Lattice.H"

    @classmethod
    def I(cls, *, p: int, q: int) -> IndefiniteLattice:
        assert False, "stub: Lattice.I"

    @classmethod
    def II(cls, *, p: int, q: int) -> IndefiniteLattice:
        assert False, "stub: Lattice.II"

    @classmethod
    def A(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.A"

    @classmethod
    def B(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.B"

    @classmethod
    def C(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.C"

    @classmethod
    def D(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.D"

    @classmethod
    def E(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.E"

    @classmethod
    def F(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.F"

    @classmethod
    def G(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.G"

    @classmethod
    def A_affine(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.A_affine"

    @classmethod
    def B_affine(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.B_affine"

    @classmethod
    def C_affine(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.C_affine"

    @classmethod
    def D_affine(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.D_affine"

    @classmethod
    def E_affine(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.E_affine"

    @classmethod
    def F_affine(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.F_affine"

    @classmethod
    def G_affine(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.G_affine"

    def rank(self) -> int:
        assert False, "stub: Lattice.rank"

    def gram(self) -> SageMatrix:
        assert False, "stub: Lattice.gram"

    def element(self, coords: tuple[int, ...] | list[int]) -> LatticeElement:
        assert False, "stub: Lattice.element"

    def norm(self, x: LatticeElement) -> int:
        assert False, "stub: Lattice.norm"

    def pairing(self, x: LatticeElement, y: LatticeElement) -> int:
        assert False, "stub: Lattice.pairing"

    def signature(self) -> tuple[int, int]:
        assert False, "stub: Lattice.signature"

    def determinant(self) -> int | Fraction:
        assert False, "stub: Lattice.determinant"

    def dual(self) -> RationalLattice | Lattice:
        assert False, "stub: Lattice.dual"

    def sublattice(self, generators: tuple[LatticeElement, ...] | list[LatticeElement]) -> SubLattice:
        assert False, "stub: Lattice.sublattice"

    def quotient(self, *, by: SubLattice) -> LatticeQuotient:
        assert False, "stub: Lattice.quotient"

    def discriminant(self) -> LatticeDiscriminantGroup:
        assert False, "stub: Lattice.discriminant"

    def orthogonal_group(self) -> OrthogonalGroup:
        assert False, "stub: Lattice.orthogonal_group"


class DefiniteLattice(Lattice, ABC):
    """Definite-lattice contract."""

    def minimum(self) -> int | Fraction:
        assert False, "stub: DefiniteLattice.minimum"

    def shortest_vector(self) -> LatticeElement:
        assert False, "stub: DefiniteLattice.shortest_vector"


class IndefiniteLattice(Lattice, ABC):
    """Indefinite-lattice contract."""

    def is_indefinite(self) -> bool:
        assert False, "stub: IndefiniteLattice.is_indefinite"

    def witt_index(self) -> int:
        assert False, "stub: IndefiniteLattice.witt_index"

    def has_isotropic_vector(self) -> bool:
        assert False, "stub: IndefiniteLattice.has_isotropic_vector"

    def isotropic_vector(self) -> LatticeElement:
        assert False, "stub: IndefiniteLattice.isotropic_vector"

    def primitive_isotropic_vectors(self, *, bound: int) -> tuple[LatticeElement, ...]:
        assert False, "stub: IndefiniteLattice.primitive_isotropic_vectors"

    def isotropic_orbit_representatives(
        self, *, bound: int, primitive: bool = True
    ) -> tuple[LatticeElement, ...]:
        assert False, "stub: IndefiniteLattice.isotropic_orbit_representatives"

    def vinberg(self) -> CoxeterData:
        assert False, "stub: IndefiniteLattice.vinberg"

    def reflection(self, root: RootLatticeElement) -> OrthogonalGroupElement:
        assert False, "stub: IndefiniteLattice.reflection"

    def orthogonal_hyperplane(self, root: RootLatticeElement) -> LatticeHyperplane:
        assert False, "stub: IndefiniteLattice.orthogonal_hyperplane"


class DegenerateLattice(Lattice, ABC):
    """Degenerate-lattice contract."""


class RationalLattice(Lattice, ABC):
    """Rational-lattice contract."""


class SubLattice(Lattice, ABC):
    """Sub-lattice contract."""

    def ambient(self) -> Lattice:
        assert False, "stub: SubLattice.ambient"

    def contains(self, x: LatticeElement) -> bool:
        assert False, "stub: SubLattice.contains"


class RootLattice(DefiniteLattice, ABC):
    """Root-lattice contract."""

    def root_system(self) -> LatticeRootSystem:
        assert False, "stub: RootLattice.root_system"


class HyperbolicLattice(IndefiniteLattice, ABC):
    """Hyperbolic-lattice contract."""


class LatticePolytope(BaseModel, ABC):
    """Polytope contract for fundamental chambers/domains."""

    model_config = ConfigDict(arbitrary_types_allowed=True)


class LatticeCoxeterGroup(BaseModel, ABC):
    """Coxeter/orthogonal-group contract attached to lattice reflection data."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def contains(self, element: OrthogonalGroupElement) -> bool:
        assert False, "stub: LatticeCoxeterGroup.contains"


class OrthogonalGroup(LatticeCoxeterGroup, ABC):
    """Orthogonal-group contract O(L)."""

    def identity(self) -> OrthogonalGroupElement:
        assert False, "stub: OrthogonalGroup.identity"

    def orbit(self, x: LatticeElement, *, bound: int) -> tuple[LatticeElement, ...]:
        assert False, "stub: OrthogonalGroup.orbit"

    def same_orbit(self, x: LatticeElement, y: LatticeElement) -> bool:
        assert False, "stub: OrthogonalGroup.same_orbit"

    def stabilizer(self, x: LatticeElement) -> LatticeCoxeterGroup:
        assert False, "stub: OrthogonalGroup.stabilizer"


class LatticeRootSystem(BaseModel, ABC):
    """Root-system contract for Coxeter/Vinberg outputs."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    def A(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.A"

    @classmethod
    def B(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.B"

    @classmethod
    def C(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.C"

    @classmethod
    def D(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.D"

    @classmethod
    def E(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.E"

    @classmethod
    def F(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.F"

    @classmethod
    def G(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.G"

    @classmethod
    def A_affine(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.A_affine"

    @classmethod
    def B_affine(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.B_affine"

    @classmethod
    def C_affine(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.C_affine"

    @classmethod
    def D_affine(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.D_affine"

    @classmethod
    def E_affine(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.E_affine"

    @classmethod
    def F_affine(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.F_affine"

    @classmethod
    def G_affine(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.G_affine"

    def is_isomorphic(self, other: LatticeRootSystem) -> bool:
        assert False, "stub: LatticeRootSystem.is_isomorphic"


class CoxeterData(BaseModel, ABC):
    """Vinberg-style aggregated data contract."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def root_lattice(self) -> RootLattice:
        assert False, "stub: CoxeterData.root_lattice"

    def fundamental_domain(self) -> LatticePolytope:
        assert False, "stub: CoxeterData.fundamental_domain"

    def coxeter_group(self) -> LatticeCoxeterGroup:
        assert False, "stub: CoxeterData.coxeter_group"

    def root_system(self) -> LatticeRootSystem:
        assert False, "stub: CoxeterData.root_system"

    def simple_roots(self) -> tuple[RootLatticeElement, ...]:
        assert False, "stub: CoxeterData.simple_roots"


class LatticeQuotient(BaseModel, ABC):
    """Quotient contract for L/M with M a sublattice."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def order(self) -> int:
        assert False, "stub: LatticeQuotient.order"

    def zero(self) -> LatticeQuotientElement:
        assert False, "stub: LatticeQuotient.zero"


class LatticeQuotientElement(BaseModel, ABC):
    """Element contract for quotient lattices/groups."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __add__(self, other: LatticeQuotientElement) -> LatticeQuotientElement:
        assert False, "stub: LatticeQuotientElement.__add__"

    def __neg__(self) -> LatticeQuotientElement:
        assert False, "stub: LatticeQuotientElement.__neg__"


class DiscriminantGroupElement(LatticeQuotientElement, ABC):
    """Element contract for lattice discriminant groups."""

    def order(self) -> int:
        assert False, "stub: DiscriminantGroupElement.order"


class LatticeDiscriminantGroup(LatticeQuotient, ABC):
    """Discriminant group contract with bilinear/quadratic forms."""

    def generator(self, i: int) -> DiscriminantGroupElement:
        assert False, "stub: LatticeDiscriminantGroup.generator"

    def zero(self) -> DiscriminantGroupElement:
        assert False, "stub: LatticeDiscriminantGroup.zero"

    def bilinear(self, x: DiscriminantGroupElement, y: DiscriminantGroupElement) -> Fraction:
        assert False, "stub: LatticeDiscriminantGroup.bilinear"

    def quadratic(self, x: DiscriminantGroupElement) -> Fraction:
        assert False, "stub: LatticeDiscriminantGroup.quadratic"
