# Julia Doc Method Gap Checklist

Tracks every documented method in `docs/julia_lattice_methods_reference.md` (sections 1-4) that lacks a `method:` tagged test. Check off as tests are written.

---

## Batch 1: Indefinite.jl (5 methods) — HIGH PRIORITY
**File:** `tests/julia_pytest/migrated_julia_doc/test_migrated_indefinite_jl.py`

- [ ] `INDEF_FORM_TestEquivalence`
- [ ] `INDEF_FORM_AutomorphismGroup`
- [ ] `INDEF_FORM_GetOrbitRepresentative`
- [ ] `INDEF_FORM_GetOrbit_IsotropicKplane`
- [ ] `INDEF_FORM_GetOrbit_IsotropicKflag`

## Batch 2: Quadratic/Hermitian Spaces §2.2 (13 methods)
**File:** `tests/julia_pytest/migrated_julia_doc/test_migrated_quadratic_spaces.py`

- [ ] `hermitian_space`
- [ ] `diagonal_with_transform`
- [ ] `orthogonal_basis`
- [ ] `is_regular`
- [ ] `is_quadratic`
- [ ] `invariants`
- [ ] `is_locally_represented_by`
- [ ] `is_represented_by`
- [ ] `inner_product(V, v, w)`
- [ ] `orthogonal_complement(V, M)`
- [ ] `orthogonal_projection`
- [ ] `is_isotropic(V, p)`
- [ ] `is_locally_hyperbolic`
- [ ] `restrict_scalars`

## Batch 3: Construction §2.3 (2 methods)
**File:** `tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_construction.py`

- [ ] `mukai_lattice`
- [ ] `hyperkaehler_lattice`

## Batch 4: Vector Enumeration §2.6 (3 methods)
**File:** `tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_enumeration.py`

- [ ] `short_vectors_iterator`
- [ ] `vectors_of_square_and_divisibility`
- [ ] `enumerate_quadratic_triples`

## Batch 5: ZZLocalGenus §2.7 (5 methods)
**File:** `tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py`

- [ ] `symbol(S, scale)`
- [ ] `dim(S)`
- [ ] `scale(S)`
- [ ] `norm(S)`
- [ ] `level(S)`
- [ ] `represents(S1, S2)`

## Batch 6: Automorphism §2.8 (1 method)
**File:** `tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_automorphism.py`

- [ ] `is_locally_isometric`

## Batch 7: Module Operations §2.9 (6 methods)
**File:** `tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_module_ops.py`

- [ ] `+(L1, L2)`
- [ ] `*(n, L)`
- [ ] `is_sublattice_with_relations`
- [ ] `divisibility`
- [ ] `in(v, L)`
- [ ] `irreducible_components`

## Batch 8: Overlattices & Embeddings §2.9 (7 methods)
**File:** `tests/julia_pytest/migrated_julia_doc/test_migrated_overlattices.py`

- [ ] `glue_map`
- [ ] `overlattice`
- [ ] `local_modification`
- [ ] `is_maximal`
- [ ] `embed`
- [ ] `embed_in_unimodular`
- [ ] `root_lattice_recognition_fundamental`

## Batch 9: TorQuadModule §2.11 (8 methods)
**File:** `tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py`

- [ ] `value_module`
- [ ] `value_module_quadratic_form`
- [ ] `quadratic_product`
- [ ] `inner_product(TorQuadModule)`
- [ ] `lift`
- [ ] `orthogonal_submodule(TorQuadModule)`
- [ ] `stable_submodules`
- [ ] `direct_product(TorQuadModule)`

## Batch 10: Hermitian Lattices §2.12 (14 methods)
**File:** `tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_lattices.py`

- [ ] `base_ring`
- [ ] `fixed_ring`
- [ ] `involution`
- [ ] `pseudo_basis`
- [ ] `coefficient_ideals`
- [ ] `absolute_basis`
- [ ] `generators(HermLat)`
- [ ] `gram_matrix_of_generators`
- [ ] `local_basis_matrix`
- [ ] `is_isotropic(HermLat)`
- [ ] `is_modular`
- [ ] `can_scale_totally_positive`
- [ ] `volume`
- [ ] `is_maximal_integral(HermLat)`

## Batch 11: Primitive Embeddings §2.15 (1 method)
**File:** `tests/julia_pytest/migrated_julia_doc/test_migrated_primitive_embeddings.py`

- [ ] `primitive_embeddings(q::TorQuadModule, sig, M)`

## Batch 12: Hermitian Genera §2.16 (8 methods)
**File:** `tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_genera.py`

- [ ] `hermitian_genera`
- [ ] `hermitian_local_genera`
- [ ] `scale(G_herm)`
- [ ] `norm(G_herm)`
- [ ] `local_symbols(G_herm)`
- [ ] `direct_sum(G1_herm, G2_herm)`
- [ ] `rescale(G_herm, a)`
- [ ] `is_ramified`

---

**Total: ~73 methods**

Last updated: 2026-02-16
