# Online Provenance: GAP crystallographic stack (2026-02-17 UTC)

## Scope

Source survey for first-class checklist/reference surfaces covering:

- `Cryst`
- `CARATInterface`
- `CrystCat`

Current-phase cursory package-surface check:

- no additional clear in-scope bilinear-form lattice package surface was identified in this pass; focus remained on Goal 2 contract fidelity for existing crystallographic surfaces.

## Canonical and supporting URLs used

- Cryst package page:
  `https://gap-packages.github.io/cryst/`
- GAP package install/index page with package listings and short descriptions:
  `https://www.math.rwth-aachen.de/~Greg.Gamble/gap4r3/pkg/inst.htm`
- GAP Reference Manual, Cryst chapter (canonical signatures for `AffineCrystGroup*`, `PointGroup`, Wyckoff methods):
  `https://docs.gap-system.org/doc/ref/chap35.html`
- GAP Reference Manual, CARAT chapter section (canonical signatures for `Bravais*`, `Carat*`, normalizer/centralizer methods):
  `https://docs.gap-system.org/doc/ref/chap44.html`

## Evidence extraction summary

- Package-level existence and role evidence:
  - package listings include entries for `CARATInterface`, `Cryst`, and `CrystCat`.
- Canonical method-surface evidence:
  - Chapter 35 provides explicit argument surfaces for crystallographic constructors,
    point-group/translation extraction, space-group classification, and Wyckoff routines.
  - Chapter 44.6 provides explicit signatures for Bravais/CARAT class and normalizer APIs.

## Signature-fidelity closure in this pass

- Replaced placeholder method signatures (`...`) in the crystallographic stack reference/checklist with canonical forms from GAP Reference chapters 35 and 44.
- Added canonical methods missing from previous checklist/reference surface:
  - `WyckoffNormalClosure(G, p)`
  - `IsBravaisEquivalent(R, S)`
  - `CaratZClass(R)` / `CaratQClass(R)`
  - `IsCaratZClass(R)` / `IsCaratQClass(R)`
- Reclassified `CrystCatZClass(...)`, `CrystCatQClass(...)`, and `CrystCatQClasses(...)` as legacy-alias triage items pending explicit confirmation in canonical current docs.

## Remaining contract gaps

- Optional selector argument domains (`f`, `s`, `k`, and `normedQclass` / `orbitsQclass`) are documented syntactically, but accepted value domains should be lifted in a future focused pass.

## Local docs linked

- `docs/crystallographic_stack_methods_checklist.md`
- `docs/crystallographic_stack/lattice/crystallographic_stack_lattice_reference.md`
