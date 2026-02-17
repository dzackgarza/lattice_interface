# GAP Forms Package Lattice-Oriented Reference
## Finite-field sesquilinear/quadratic forms and orthogonal decomposition workflows

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PKG]` | Provided by GAP package `Forms` |
| `[FFORM]` | Finite-field form setting (no real-signature PD/INDEF notion) |
| `[EQUIV]` | Isometry/similarity/equivalence workflow |
| `[GRP]` | Matrix-group interaction |
| `[DECOMP]` | Orthogonal decomposition / Witt-index workflow |

---

## 1. Scope

The GAP `Forms` package provides sesquilinear and quadratic-form APIs over finite fields and supporting matrix-group workflows.

This surface is lattice-relevant in the finite-field and group-action sense:

- form constructors from matrices and coercion APIs,
- form predicates/invariants (rank, radical, symmetry/alternation),
- isometry/similarity and form-preserving matrix-group computations,
- orthogonal decomposition and Witt-index methods.

---

## 2. Constructors and Coercions

| Function | Description | Tags |
|----------|-------------|------|
| `AsSesquilinearForm(obj[, field][, antiautomorphism])` | Construct/coerce sesquilinear form from matrix/form object with optional field and involution control. | `[PKG, FFORM]` |
| `AsQuadraticForm(obj[, field])` | Construct/coerce quadratic form from matrix/form object with optional field override. | `[PKG, FFORM]` |
| `SesquilinearFormByMatrix(matrix[, field][, antiautomorphism])` | Build a sesquilinear form from matrix data. | `[PKG, FFORM]` |
| `QuadraticFormByMatrix(matrix[, field])` | Build a quadratic form from matrix data. | `[PKG, FFORM]` |

---

## 3. Categories, Attributes, and Predicates

| Function | Description | Tags |
|----------|-------------|------|
| `IsSesquilinearForm(obj)` | Category predicate for sesquilinear forms. | `[PKG, FFORM]` |
| `IsQuadraticForm(obj)` | Category predicate for quadratic forms. | `[PKG, FFORM]` |
| `UnderlyingVectorSpace(form)` | Return underlying vector space of form domain. | `[PKG, FFORM]` |
| `MatrixOfSesquilinearForm(form)` | Matrix representation associated to a sesquilinear form. | `[PKG, FFORM]` |
| `MatrixOfQuadraticForm(form)` | Matrix representation for quadratic form (documented for odd characteristic). | `[PKG, FFORM]` |
| `RankOfForm(form)` | Rank invariant of the form. | `[PKG, FFORM]` |
| `BaseField(form)` | Base field of the form. | `[PKG, FFORM]` |
| `IsReflexiveForm(form)` | Reflexivity predicate. | `[PKG, FFORM]` |
| `IsSymmetricForm(form)` | Symmetry predicate. | `[PKG, FFORM]` |
| `IsAlternatingForm(form)` | Alternation predicate. | `[PKG, FFORM]` |
| `IsDegenerateForm(form)` | Degeneracy predicate. | `[PKG, FFORM]` |
| `RadicalOfForm(form)` | Radical subspace of the form. | `[PKG, FFORM, DECOMP]` |

Characteristic caveat:
- Manual chapter 4 documents `MatrixOfQuadraticForm` for odd characteristic and notes matrix reconstruction differences in characteristic `2`.

---

## 4. Equivalence and Symmetry Groups

| Function | Description | Tags |
|----------|-------------|------|
| `IsometricForms(form1, form2)` | Isometry test between forms. | `[PKG, FFORM, EQUIV]` |
| `SimilarityForms(form1, form2)` | Similarity test between forms. | `[PKG, FFORM, EQUIV]` |
| `IsometryGroup(form)` | Group preserving the form exactly. | `[PKG, FFORM, EQUIV, GRP]` |
| `SimilarityGroup(form)` | Group preserving the form up to scalar factor. | `[PKG, FFORM, EQUIV, GRP]` |

---

## 5. Invariant and Preserved Forms of Matrix Groups

| Function | Description | Tags |
|----------|-------------|------|
| `InvariantBilinearForm(G[, involution][, isom])` | Construct bilinear form invariant under matrix-group action. | `[PKG, FFORM, GRP]` |
| `InvariantQuadraticForm(G[, involution][, isom])` | Construct quadratic form invariant under matrix-group action. | `[PKG, FFORM, GRP]` |
| `PreservedSesquilinearForms(G)` | Return preserved sesquilinear forms for `G`; documented for absolutely irreducible groups. | `[PKG, FFORM, GRP]` |
| `PreservedQuadraticForms(G)` | Return preserved quadratic forms for absolutely irreducible groups over finite fields of odd characteristic. | `[PKG, FFORM, GRP]` |

Workflow caveat:
- Chapter 5 states `PreservedSesquilinearForms`/`PreservedQuadraticForms` in an absolutely irreducible matrix-group regime; quadratic case is odd-characteristic only.

---

## 6. Orthogonal Decomposition and Witt Index

| Function | Description | Tags |
|----------|-------------|------|
| `OrthogonalSubgroups(G, n[, s])` | Orthogonal decomposition helper returning subgroup data for form model `n`. | `[PKG, FFORM, DECOMP]` |
| `OrthogonalSubgroupsAsList(G, n[, s])` | List-form output variant of orthogonal subgroup decomposition. | `[PKG, FFORM, DECOMP]` |
| `OrthogonalComponents(G, n)` | Orthogonal components of module/group with respect to form `n`. | `[PKG, FFORM, DECOMP]` |
| `OrthogonalComponentsOfSubgroup(U, n)` | Orthogonal components restricted to subgroup `U` of ambient row-space carrying form `n`. | `[PKG, FFORM, DECOMP]` |
| `WittIndex(form)` | Witt-index computation for finite-field forms; characteristic `2` requires non-singular form. | `[PKG, FFORM, DECOMP]` |

---

## 7. Definiteness and Domain Notes

- `Forms` is finite-field linear/form algebra and does not provide real-signature (`PD`/`INDEF`) contracts.
- Orthogonal and Witt-index methods here should not be conflated with integer-lattice genus/signature classification over `ZZ`/`QQ`.
- For integer-matrix normal forms and Euclidean reduction in GAP, use core integer-matrix and `LLLReduced*` APIs (documented in `docs/gap/lattice/gap_lattice_methods_reference.md`).

---

## 8. Sources

- Forms package page: `https://gap-packages.github.io/forms/`
- Forms manual TOC: `https://gap-packages.github.io/forms/doc/chap0_mj.html`
- Forms manual chapter 4: `https://gap-packages.github.io/forms/doc/chap4_mj.html`
- Forms manual chapter 5: `https://gap-packages.github.io/forms/doc/chap5_mj.html`
