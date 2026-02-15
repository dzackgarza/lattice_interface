from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .types import DefiniteLattice, IndefiniteLattice, Lattice


class LatticeProvider(Protocol):
    """Backend-agnostic provider for contract tests."""

    name: str

    def from_gram(self, gram) -> Lattice: ...

    def canonical_definite(self) -> DefiniteLattice: ...

    def canonical_indefinite(self) -> IndefiniteLattice: ...

    def supports(self, capability_id: str) -> bool: ...


@dataclass(frozen=True)
class ProviderDescriptor:
    name: str
    notes: str
