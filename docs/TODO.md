# Documentation Gaps - Bilinear-Form Lattice Methods

This file tracks outstanding items to do for building complete documentation.
Reference docs (`docs/*/lattice/*.md`) track method surfaces with source-backed signatures.
Checklist files (`docs/*_methods_checklist.md`) track TEST COVERAGE - separate task.

## Goal 1: Local Doc Integration (MANDATORY PREREQUISITE)

Local upstream docs under `docs/**/upstream/` are required before contract-fidelity work to proceed.
EVERY SINGLE PACKAGE must be a real upsteam source before ANY work can proceed.

### Missing upstream directories

- [ ] `docs/latticegen/upstream/` — reference doc and checklist exist but no upstream sources

## Goal 2: Contract-Fidelity Work (Post-Integration)

Completeness and provable correctness of all documented methods across all reference docs under `docs/`.

### Missing Sources sections

- [x] `docs/sage/lattice/sagemath_lattice_reference.md` — no Sources section
- [x] `docs/gap/lattice/gap_lattice_methods_reference.md` — no Sources section
