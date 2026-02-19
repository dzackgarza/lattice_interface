# Documentation Gaps - Bilinear-Form Lattice Methods

This file tracks the prerequisite state for building complete documentation.
Reference docs (`docs/*/lattice/*.md`) track method surfaces with source-backed signatures.
Checklist files (`docs/*_methods_checklist.md`) track TEST COVERAGE - separate task.

**STATUS (2026-02-19)**: Goal 1 COMPLETE. Goal 2 COMPLETE - all reference doc sections now have explicit type specifications.

**Corrections applied (2026-02-19, follow-up pass)**:
- GAP core reference: LLL and short-vector sections (1.2, 1.3) converted to 5-column format with source-backed argument types and return types from chap25.html; `LLLReducedBasis(...)` placeholder replaced with full optional-argument signature.
- SageMath QuadraticForm reference: `local_representation_conditions` argument types corrected (was `—`, now `recompute_flag=False, silent_flag=False`) and critical ≥3-variable constraint added; return type corrected from `RepresentationConditions` to `LocalRepresentationConditions`.

## Goal 1: Local Doc Integration (MANDATORY PREREQUISITE)

Local upstream docs under `docs/**/upstream/` are required before contract-fidelity work can proceed.

### Packages with integrated local docs (all complete)

- [x] hypercells (full chapter snapshots)
- [x] flatter (README and example profiles)
- [x] SageMath (integral lattice docs)
- [x] Oscar/Hecke (Julia lattice docs)
- [x] flint (fmpz_lll.rst + fmpz_mat.rst integrated; signatures verified and corrected 2026-02-19)
- [x] NTL (LLL.txt + mat_ZZ.txt integrated; signatures verified and corrected 2026-02-19)
- [x] GAP core (matint.xml, chap24/25/26.html and related sources present under upstream/)
- [x] fpylll (.pyx source files + online provenance snapshot present; reference doc verified)
- [x] forms (chap1-5 HTML files present; reference doc covers all major API surfaces)
- [x] g6k (siever.pyx + README + algorithms/*.py present; reference doc verified)
- [x] crystallographic_stack (cryst/caratinterface/crystcat .gd and .tex files present; reference verified)
- [x] pari_gp (HTML upstream sections present; reference doc covers qf* API surface)


## Goal 2: Contract-Fidelity Work (Post-Integration)

This section tracks gaps in method documentation completeness (argument surfaces, types, assumptions, constraints) for packages with integrated local docs.

### GAP Forms Package (`docs/forms/lattice/forms_lattice_reference.md`)

- [x] **Explicit Type Specifications:** Add explicit GAP type annotations or descriptions for all function arguments and return values. The current documentation lacks this detail, making it harder to use without consulting the original GAP manual.

### SageMath (`docs/sage_methods_checklist.md`)

- [x] **Explicit Type Specifications:** Added to IntegralLattice and IntegerLattice method tables in sagemath_lattice_reference.md (sections 3-4) and to BinaryQF (section 6), TernaryQF (section 7), TorsionQuadraticModule (section 8), and Genus (section 9); QuadraticForm (section 5) now completed 2026-02-19

### Julia/Hecke.jl (`docs/julia_methods_checklist.md`)

- [x] **Explicit Type Specifications:** Added to all sections in julia_lattice_methods_reference.md: Quadratic/hermitian spaces (2.2), Construction (2.3), Intrinsic data (2.4), Reduction (2.5), Vector enumeration (2.6), Genus/ZZGenus/ZZLocalGenus (2.7), Automorphism/isometry (2.8), Module operations/embeddings (2.9), Vinberg's algorithm (2.10), TorQuadModule (2.11), Hermitian lattices HermLat/QuadLat (2.12), QuadSpaceWithIsom (2.13), all ZZLatWithIsom subsections (2.14), Primitive embeddings (2.15), Hermitian genera (2.16), Isometry group actions (2.17), TorQuadModuleWithIsom (2.18); all sections completed 2026-02-19
