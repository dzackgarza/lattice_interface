# Isometry Surface Online Provenance Note (2026-02-17)

This note localizes the online source evidence used in passes `20260217-12` and `20260217-13` for `QuadSpaceWithIsom`, `ZZLatWithIsom`, `TorQuadModuleWithIsom`, and related group-action isometry surfaces.

## Online sources surveyed

- OSCAR stable NumberTheory `QuadFormAndIsom` pages:
  - https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/spacewithisom/
  - https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/latwithisom/
  - https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/torquadmodwithisom/
  - https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/manualindex/
- OSCAR dev NumberTheory `QuadFormAndIsom` pages (drift cross-check):
  - https://docs.oscar-system.org/dev/NumberTheory/QuadFormAndIsom/spacewithisom/
  - https://docs.oscar-system.org/dev/NumberTheory/QuadFormAndIsom/latwithisom/
  - https://docs.oscar-system.org/dev/NumberTheory/QuadFormAndIsom/torquadmodwithisom/
  - https://docs.oscar-system.org/dev/NumberTheory/QuadFormAndIsom/manualindex/
- OSCAR `v1` Experimental `QuadFormAndIsom` pages (signature-block cross-check for current generated method surfaces):
  - https://docs.oscar-system.org/v1/Experimental/QuadFormAndIsom/spacewithisom/
  - https://docs.oscar-system.org/v1/Experimental/QuadFormAndIsom/latwithisom/
  - https://docs.oscar-system.org/v1/Experimental/QuadFormAndIsom/torquadmodwithisom/
  - https://docs.oscar-system.org/v1/Experimental/QuadFormAndIsom/manualindex/
- OSCAR stable Hecke manual (lattices with isometry):
  - https://docs.oscar-system.org/stable/Hecke/manual/lattices/lattices_with_isometry/
- OSCAR dev Hecke manual (lattices with isometry, drift cross-check):
  - https://docs.oscar-system.org/dev/Hecke/manual/lattices/lattices_with_isometry/
- OSCAR release notes stream (surface-change corroboration for isometry/group-action methods):
  - https://github.com/oscar-system/Oscar.jl/releases

Access date (UTC): 2026-02-17

## Contracts verified from online docs

- `order_of_isometry(::QuadSpaceWithIsom)` contract includes explicit infinite-order and rank-zero behavior:
  - infinite order stored as `PosInf`,
  - rank-zero edge case uses `-1`.
- `quadratic_space_with_isometry(::Hecke.QuadSpace, ::QQMatrix; check=...)` has conflicting default wording across visible generated docs (`check::Bool=false` in signature block vs prose saying default checks are performed). Local docs now advise passing `check` explicitly instead of asserting a single default.
- Current generated signatures for `direct_sum` on `QuadSpaceWithIsom` and `ZZLatWithIsom` include both vararg and vector-input forms (not vector-only shorthand):
  - `direct_sum(Vf::Union{QuadSpaceWithIsom, Vector{QuadSpaceWithIsom}}...)`,
  - `direct_sum(Lf::Union{ZZLatWithIsom, Vector{ZZLatWithIsom}}...)`,
  and binary forms are documented with tuple outputs carrying embedding maps.
- `ZZLatWithIsom` construction from an ambient pair includes both ambient-lattice extraction and basis-matrix construction surfaces:
  - `lattice(::QuadSpaceWithIsom)`,
  - `lattice(::QuadSpaceWithIsom, ::MatElem{<:RationalUnion})`.
- `integer_lattice_with_isometry(::ZZLat, ::QQMatrix; ambient_representation=...)` explicitly distinguishes matrix representation in ambient-space basis versus fixed lattice basis.
- `trace_lattice_with_isometry` is documented with two call surfaces in current pages:
  - `trace_lattice_with_isometry(H)`,
  - `trace_lattice_with_isometry(H, res)` (explicit residue-embedding choice).
- `discriminant_group` for `ZZLatWithIsom` is documented beyond plain `TorQuadModule` output, including typed forms with induced action:
  - `discriminant_group(Lf::ZZLatWithIsom)`,
  - `discriminant_group(::Type{TorQuadModuleWithIsom}, Lf::ZZLatWithIsom; ambient_representation=true)`.
- `image_in_Oq` is documented as the general image-of-`π` computation (Miranda-Morrison context), distinct from `image_centralizer_in_Oq`.
- `torsion_quadratic_module_with_isometry` constructors are documented with broader action-data types than the minimal local signature form (current generated signatures include map/hom/matrix/group-element style action inputs).
- Generated method lists for finite-module and group-action layers show signature granularity that local docs now mirror more closely, notably:
  - `admissible_triples(::ZZGenus, ::Int)` / `is_admissible_triple(::ZZGenus, ::ZZGenus, ::ZZGenus, ::Int)`,
  - `splitting(::ZZLatWithIsom, ::Int, ::Int)` and prime-power splitting variants,
  - `is_stable_isometry(::ZZLatWithIsom)` / `is_special_isometry(::ZZLatWithIsom)`.
- For group-action layers, current manual indexes list both `invariant_coinvariant_pair(::ZZLatWithIsom)` and a distinct `fingrpact` entry for `invariant_coinvariant_pair` on plain lattices under matrix/group actions; local docs now explicitly represent the `ZZLat` action signature from the local `fingrpact` snapshot:
  - `invariant_coinvariant_pair(::ZZLat, ::Union{QQMatrix, Vector{QQMatrix}, MatGroup})`.
- `fingrpact` section wording identifies `is_isometry*` and `is_isometry_group*` helpers as non-exported input-check utilities and frames `extend_to_ambient_space` / `restrict_to_lattice` as coordinate-representation conversion between ambient-space and fixed lattice bases for collections of isometries.

## Pass-14 addendum (2026-02-17): stabilizer signature-surface fidelity

- Re-surveyed online index surfaces for `Collections of isometries` method names:
  - stable manual index: https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/manualindex/
  - dev manual index: https://docs.oscar-system.org/dev/NumberTheory/QuadFormAndIsom/manualindex/
  - v1 manual index: https://docs.oscar-system.org/v1/Experimental/QuadFormAndIsom/manualindex/
- Local snapshot source for the same section:
  - `docs/julia/oscar_jl/number_theory/quad_form_and_isom/fingrpact.md`
- Verified from these sources:
  - typed dispatch entries are explicitly shown for `is_isometry*`, `is_isometry_group*`, `special_*`, `stable_*`, `maximal_extension(::ZZLat, ::ZZLat, ::MatGroup)`, and `saturation` overloads,
  - stabilizer-family entries are currently listed by runtime method name (`stabilizer_*`) without explicit typed dispatch blocks in the available docs surfaces.
- Inference recorded for local docs/checklist alignment:
  - keep stabilizer-family methods runtime-name exact (`...` placeholders) rather than asserting speculative argument types,
  - keep `extend_to_ambient_space(::ZZLat, ...)` / `restrict_to_lattice(::ZZLat, ...)` framed as basis-representation conversion for collections of isometries, matching upstream section text.

## Pass-19 addendum (2026-02-18): map-return contract fidelity for isometry APIs

- Re-surveyed upstream pages for tuple return shapes and preconditions:
  - https://docs.oscar-system.org/v1.4/Hecke/manual/lattices/integrelattices/
  - https://docs.oscar-system.org/v1/Hecke/manual/quad_forms/torquadmod/
  - https://docs.oscar-system.org/dev/Hecke/manual/quad_forms/torquadmodwithisom/
- Verified from these pages:
  - `is_isometric_with_isometry(L, M; depth=3, bacher_depth=5, ambient_representation=true)` has explicit tuple-return contract:
    - returns `(true, f)` when an isometry exists,
    - returns `(false, zero_matrix(QQ, 0, 0))` otherwise.
  - `is_isometric_with_isometry(T, U)` / `is_anti_isometric_with_anti_isometry(T, U)` on finite quadratic modules are documented with tuple-return shape and explicit preconditions:
    - modulus compatibility (`modulus_quadratic_form` equality) or prior rescaling,
    - semiregular decomposition conditions on the relevant direct sums.
  - `is_isomorphic_with_map(Tf, Sf)` / `is_anti_isomorphic_with_map(Tf, Sf)` on `TorQuadModuleWithIsom` are documented with explicit failure sentinel:
    - success returns `(true, map)` (or anti-map),
    - failure returns `(false, 0)`.

## Documentation caveat captured

In current generated docs for torsion quadratic modules with isometry, one automorphism signature location typesets `TorQuadModuleWithMap` while the page/type context is `TorQuadModuleWithIsom`. Local references treat this as a documentation typing inconsistency and keep semantic interpretation aligned with the page context.

## Local snapshot linkage

For reproducible offline context, see:

- `docs/julia/oscar_jl/number_theory/quad_form_and_isom/spacewithisom.md`
- `docs/julia/oscar_jl/number_theory/quad_form_and_isom/latwithisom.md`
- `docs/julia/oscar_jl/number_theory/quad_form_and_isom/torquadmodwithisom.md`
- `docs/julia/oscar_jl/number_theory/quad_form_and_isom/fingrpact.md`
- `docs/julia/oscar_jl/number_theory/quad_form_and_isom/enumeration.md`
- `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md`
- `docs/julia_methods_checklist.md`
