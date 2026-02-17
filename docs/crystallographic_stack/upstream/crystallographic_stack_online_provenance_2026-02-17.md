# Online Provenance: GAP crystallographic stack (2026-02-17 UTC)

## Scope

Source survey for first-class checklist/reference surfaces covering:

- `Cryst`
- `CARATInterface`
- `CrystCat`

## Canonical and supporting URLs used

- Cryst package page:
  `https://gap-packages.github.io/cryst/`
- GAP package install/index page with package listings and short descriptions:
  `https://www.math.rwth-aachen.de/~Greg.Gamble/gap4r3/pkg/inst.htm`
- CrystCat/CARAT-related function chapter:
  `https://www.math.rwth-aachen.de/~Greg.Gamble/gap4r3/pkg/crystcat/doc/chap39.htm`
- Cryst method chapter (historical mirror used for method-surface continuity):
  `https://webusers.imj-prg.fr/~jean.michel/gap3/htm/chap035.htm`

## Evidence extraction summary

- Package-level existence and role evidence:
  - `inst.htm` listing includes entries for `CARATInterface`, `Cryst`, and `CrystCat`.
- Method-surface evidence:
  - Cryst methods (`AffineCrystGroupOnRight`, `PointGroup`, `TranslationsCrystGroup`,
    `SpaceGroupsByPointGroupOnRight`, Wyckoff family) from crystallographic manual
    chapter mirror.
  - CrystCat/CARAT-linked class and normalizer methods
    (`CrystCatZClass`, `CaratQClassNumber`, `NormalizerInGLnZ`, etc.) from chapter 39.

## Open triage items

- Exact modern signature typing for several methods is still unresolved in currently
  retrievable modern GAP package docs; current surfaces keep `...` placeholders where
  source does not expose stable typed signatures directly.
- Method-to-package attribution between `CrystCat` and `CARATInterface` is partly coupled
  in available chapter material; current docs state this explicitly rather than guessing.

## Local docs linked

- `docs/crystallographic_stack_methods_checklist.md`
- `docs/crystallographic_stack/lattice/crystallographic_stack_lattice_reference.md`
