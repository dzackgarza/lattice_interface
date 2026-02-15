from __future__ import annotations

from tests.new_lattice_interface.capability_registry import (
    CAPABILITY_REGISTRY,
    CapabilitySpec,
    capabilities_by_domain,
)


def test_capability_registry_schema_is_complete():
    """method: capability_registry_schema"""
    assert CAPABILITY_REGISTRY, "Capability registry must be non-empty."
    for capability_id, spec in CAPABILITY_REGISTRY.items():
        assert isinstance(spec, CapabilitySpec), (
            f"Capability schema type mismatch: capability={capability_id}, spec={spec}"
        )
        assert spec.id == capability_id, (
            f"Capability id mismatch: key={capability_id}, spec.id={spec.id}"
        )
        assert spec.domain in {"definite_only", "indefinite_only", "both"}, (
            f"Capability domain mismatch: capability={capability_id}, domain={spec.domain}"
        )
        assert spec.input_contract, f"Missing input_contract for capability={capability_id}"
        assert spec.output_contract, f"Missing output_contract for capability={capability_id}"
        assert spec.assertion_profile, f"Missing assertion_profile for capability={capability_id}"
        assert spec.description, f"Missing description for capability={capability_id}"


def test_definite_and_indefinite_domains_are_disjoint():
    """method: capability_domain_partition"""
    definite = capabilities_by_domain("definite_only")
    indefinite = capabilities_by_domain("indefinite_only")
    overlap = sorted(definite & indefinite)
    assert not overlap, f"Capability domain overlap found: overlap={overlap}"


def test_core_domains_have_nonzero_capability_counts():
    """method: capability_domain_nonempty"""
    assert capabilities_by_domain("definite_only"), "No definite_only capabilities registered."
    assert capabilities_by_domain("indefinite_only"), "No indefinite_only capabilities registered."
    assert capabilities_by_domain("both"), "No shared capabilities registered."
