# Documentation Gaps - Bilinear-Form Lattice Methods

This file tracks outstanding items to do for building complete documentation.
Reference docs (`docs/*/lattice/*.md`) track method surfaces with source-backed signatures.
Checklist files (`docs/*_methods_checklist.md`) track TEST COVERAGE - separate task.

## Goal 1: Local Doc Integration (MANDATORY PREREQUISITE)

Local upstream docs under `docs/**/upstream/` are required before contract-fidelity work to proceed.
EVERY SINGLE PACKAGE must be a real upstream source before ANY work can proceed.

### Missing upstream directories

(None currently — all in-scope packages have upstream snapshots)

## Goal 2: Contract-Fidelity Work (Post-Integration)

Completeness and provable correctness of all documented methods across all reference docs under `docs/`.

### Verification status (2026-02-19)

All active in-scope reference docs have been verified to have:
- Sources sections with canonical upstream URLs
- Local upstream provenance snapshots under `docs/*/upstream/`
- Typed method signatures with argument/return types
- Definiteness tags (`[PD]`, `[INDEF]`, `[ND]`, etc.) documenting domain constraints
- Cross-references to related objects and alternative ecosystems

**Sage special forms note:** BinaryQF and TernaryQF method surfaces are documented in `sage/lattice/sagemath_lattice_reference.md` (sections 6–7). The separate upstream snapshots under `sage/special_forms/*/upstream/` provide additional detail but do not represent coverage gaps.

**Out-of-scope archives:** Polyhedral/toric packages (Normaliz, 4ti2, cddlib, etc.) are archived under `docs/archive/scope_violations/` and correctly excluded from active bilinear-form lattice coverage.

Goal 2 complete — all in-scope bilinear-form lattice method surfaces have source-backed documentation with typed signatures and domain constraints.
