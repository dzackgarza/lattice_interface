# Isometry Surface Online Provenance Note (2026-02-17)

This note localizes the online source evidence used in pass `20260217-12` for `QuadSpaceWithIsom`, `ZZLatWithIsom`, and `TorQuadModuleWithIsom` contract updates.

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
- OSCAR `v1` Experimental `QuadFormAndIsom` pages (signature-block cross-check for current generated method surfaces):
  - https://docs.oscar-system.org/v1/Experimental/QuadFormAndIsom/spacewithisom/
  - https://docs.oscar-system.org/v1/Experimental/QuadFormAndIsom/latwithisom/
  - https://docs.oscar-system.org/v1/Experimental/QuadFormAndIsom/torquadmodwithisom/
- OSCAR stable Hecke manual (lattices with isometry):
  - https://docs.oscar-system.org/stable/Hecke/manual/lattices/lattices_with_isometry/
- OSCAR dev Hecke manual (lattices with isometry, drift cross-check):
  - https://docs.oscar-system.org/dev/Hecke/manual/lattices/lattices_with_isometry/

Access date (UTC): 2026-02-17

## Contracts verified from online docs

- `order_of_isometry(::QuadSpaceWithIsom)` contract includes explicit infinite-order and rank-zero behavior:
  - infinite order stored as `PosInf`,
  - rank-zero edge case uses `-1`.
- `quadratic_space_with_isometry(::Hecke.QuadSpace, ::QQMatrix; check=...)` has conflicting default wording across visible generated docs (`check::Bool=false` in signature block vs prose saying default checks are performed). Local docs now advise passing `check` explicitly instead of asserting a single default.
- The constructor/operation surfaces for `QuadSpaceWithIsom` and `ZZLatWithIsom` are exposed in current generated docs as vector-style direct-sum methods:
  - `direct_sum(::Vector{QuadSpaceWithIsom})`,
  - `direct_sum(::Vector{ZZLatWithIsom})`.
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
