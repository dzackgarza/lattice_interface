# Julia Methods Checklist — Organized by Doc Page

---

## 1. `julia_lattice_methods_reference.md`

### §1 — Indefinite.jl

- [ ] `INDEF_FORM_TestEquivalence(Q1, Q2)`
- [ ] `INDEF_FORM_AutomorphismGroup(Q)`
- [ ] `INDEF_FORM_GetOrbitRepresentative(Q, C)`
- [ ] `INDEF_FORM_GetOrbit_IsotropicKplane(Q, k)`
- [ ] `INDEF_FORM_GetOrbit_IsotropicKflag(Q, k)`

### §2.1 — Hecke Types

- [ ] `ZZLat`
- [ ] `QuadLat`
- [ ] `HermLat`
- [ ] `ZZGenus`
- [ ] `ZZLocalGenus`
- [ ] `TorQuadModule`
- [ ] `QuadSpace`
- [ ] `HermSpace`
- [ ] `ZZLatWithIsom`
- [ ] `QuadSpaceWithIsom`

### §2.2 — Quadratic and Hermitian Spaces

- [ ] `quadratic_space(K, n)` / `quadratic_space(K, G)`
- [ ] `hermitian_space(E, n)` / `hermitian_space(E, G)`
- [ ] `rank(V)` / `dim(V)`
- [ ] `gram_matrix(V)` / `gram_matrix(V, M)`
- [ ] `det(V)` / `discriminant(V)`
- [ ] `diagonal(V)`
- [ ] `diagonal_with_transform(V)`
- [ ] `orthogonal_basis(V)`
- [ ] `signature_tuple(V)`
- [ ] `is_regular(V)`
- [ ] `is_quadratic(V)` / `is_hermitian(V)`
- [ ] `is_positive_definite(V)` / `is_negative_definite(V)` / `is_definite(V)`
- [ ] `hasse_invariant(V, p)` / `witt_invariant(V, p)`
- [ ] `invariants(V)`
- [ ] `is_isometric(V, W)` / `is_isometric(V, W, p)`
- [ ] `is_locally_represented_by(U, V, p)`
- [ ] `is_represented_by(U, V)`
- [ ] `inner_product(V, v, w)`
- [ ] `orthogonal_complement(V, M)`
- [ ] `orthogonal_projection(V, M)`
- [ ] `is_isotropic(V, p)`
- [ ] `is_locally_hyperbolic(V, p)`
- [ ] `restrict_scalars(V, K, α)`
- [ ] `direct_sum(V, W)` / `direct_product` / `biproduct`

### §2.3 — Construction

- [ ] `integer_lattice(; gram=G)`
- [ ] `integer_lattice(B; gram=G)`
- [ ] `lattice(V, B)`
- [ ] `quadratic_lattice(K, gens; gram=M)`
- [ ] `hermitian_lattice(E, gens; gram=M)`
- [ ] `root_lattice(:A, n)` / `(:D, n)` / `(:E, n)` / `(:I, n)`
- [ ] `hyperbolic_plane_lattice(n)`
- [ ] `leech_lattice()`
- [ ] `k3_lattice()`
- [ ] `mukai_lattice()`
- [ ] `hyperkaehler_lattice(:K3, n=3)`
- [ ] `rescale(L, r)`

### §2.4 — Intrinsic Data

- [ ] `gram_matrix(L)`
- [ ] `basis_matrix(L)`
- [ ] `ambient_space(L)`
- [ ] `rational_span(L)`
- [ ] `rank(L)`
- [ ] `degree(L)`
- [ ] `signature_tuple(L)`
- [ ] `det(L)`
- [ ] `discriminant(L)`
- [ ] `scale(L)`
- [ ] `norm(L)`
- [ ] `is_positive_definite(L)`
- [ ] `is_negative_definite(L)`
- [ ] `is_definite(L)`
- [ ] `is_even(L)`
- [ ] `is_integral(L)`
- [ ] `is_unimodular(L)`
- [ ] `is_primary(L, p)`
- [ ] `is_primary_with_prime(L)`
- [ ] `is_elementary(L, p)`
- [ ] `is_elementary_with_prime(L)`

### §2.5 — Reduction

- [ ] `lll(L::ZZLat; same_ambient=true)`

### §2.6 — Vector Enumeration

- [ ] `short_vectors(L, lb, ub)`
- [ ] `short_vectors_iterator(L, lb, ub)`
- [ ] `shortest_vectors(L)`
- [ ] `close_vectors(L, v, ub; lb=0, check=true)`
- [ ] `short_vectors_affine(S, v, α, d)`
- [ ] `vectors_of_square_and_divisibility(L, n, d)`
- [ ] `enumerate_quadratic_triples(L, n)`
- [ ] `minimum(L)`
- [ ] `kissing_number(L)`

### §2.7 — Genus and Classification

#### ZZGenus methods

- [ ] `genus(L::ZZLat)`
- [ ] `genus(A::MatElem)`
- [ ] `genus(L, p)`
- [ ] `integer_genera(sig, det)`
- [ ] `direct_sum(G1::ZZGenus, G2::ZZGenus)`
- [ ] `representative(gen)`
- [ ] `representatives(gen)`
- [ ] `mass(gen)`
- [ ] `dim(gen)` / `rank(gen)`
- [ ] `signature(gen)`
- [ ] `det(gen)`
- [ ] `iseven(gen)`
- [ ] `is_definite(gen)`
- [ ] `level(gen)`
- [ ] `scale(gen)` / `norm(gen)`
- [ ] `primes(gen)`
- [ ] `is_integral(gen)`
- [ ] `local_symbol(gen, p)`
- [ ] `quadratic_space(gen)`
- [ ] `rational_representative(gen)`
- [ ] `rescale(gen, a)`
- [ ] `represents(G1, G2)`

#### ZZLocalGenus methods

- [ ] `prime(S)`
- [ ] `iseven(S)`
- [ ] `symbol(S, scale)`
- [ ] `hasse_invariant(S)`
- [ ] `det(S)` / `dim(S)` / `rank(S)`
- [ ] `excess(S)`
- [ ] `signature(S)`
- [ ] `oddity(S)`
- [ ] `scale(S)` / `norm(S)` / `level(S)`
- [ ] `representative(S)` / `gram_matrix(S)`
- [ ] `rescale(S, a)`
- [ ] `direct_sum(S1, S2)`
- [ ] `represents(S1, S2)`

#### Discriminant group and classification

- [ ] `discriminant_group(L)`
- [ ] `genus_representatives(L)`
- [ ] `Hecke.quadratic_lattice_database()`

### §2.8 — Automorphism and Isometry

- [ ] `automorphism_group_generators(L)`
- [ ] `automorphism_group_order(L)`
- [ ] `is_isometric(L1, L2)`
- [ ] `is_isometric_with_isometry(L1, L2)`
- [ ] `is_locally_isometric(L1, L2, p)`
- [ ] `is_rationally_isometric(L1, L2)`
- [ ] `hasse_invariant(L, p)`
- [ ] `witt_invariant(L, p)`

### §2.9 — Module Operations and Embeddings

- [ ] `direct_sum(L1, L2)`
- [ ] `direct_product(L1, L2)`
- [ ] `biproduct(L1, L2)`
- [ ] `intersect(L1, L2)`
- [ ] `+(L1, L2)`
- [ ] `*(n, L)`
- [ ] `lattice_in_same_ambient_space(L, B)`
- [ ] `orthogonal_submodule(L, S)`
- [ ] `dual(L)`
- [ ] `is_sublattice(L, S)`
- [ ] `is_sublattice_with_relations(L, S)`
- [ ] `is_primitive(L, S)`
- [ ] `primitive_closure(L, S)`
- [ ] `divisibility(L, v)`
- [ ] `in(v, L)`
- [ ] `irreducible_components(L)`

#### Overlattices and embeddings

- [ ] `glue_map(L, S, gen_imgs)`
- [ ] `overlattice(glue_map)`
- [ ] `primitive_extension(L1, L2, glue_map)`
- [ ] `local_modification(L, M, p)`
- [ ] `maximal_integral_lattice(L)`
- [ ] `is_maximal_integral(L)`
- [ ] `is_maximal(L)`
- [ ] `embed(L, gen)`
- [ ] `embed_in_unimodular(L)`

#### Endomorphism-based sublattices

- [ ] `kernel_lattice(L, f)`
- [ ] `invariant_lattice(L, G)`
- [ ] `coinvariant_lattice(L, G)`

#### Root lattice recognition

- [ ] `root_lattice_recognition(L)`
- [ ] `root_lattice_recognition_fundamental(L)`
- [ ] `ADE_type(L)`
- [ ] `coxeter_number(L)`
- [ ] `highest_root(L)`

### §2.10 — Vinberg's Algorithm

- [ ] `vinberg_algorithm(Q::ZZMatrix, ub; v0, root_lengths, direction_vector)`
- [ ] `vinberg_algorithm(S::ZZLat, ub; v0, root_lengths, direction_vector)`
- [ ] `short_vectors_affine(S, v, α, d)` *(also in §2.6)*

### §2.11 — Discriminant Groups (`TorQuadModule`)

- [ ] `torsion_quadratic_module(M, N)`
- [ ] `torsion_quadratic_module(q::QQMatrix)`
- [ ] `discriminant_group(L)` *(also in §2.7)*
- [ ] `abelian_group(T)`
- [ ] `cover(T)` / `relations(T)`
- [ ] `gram_matrix_bilinear(T)`
- [ ] `gram_matrix_quadratic(T)`
- [ ] `value_module(T)`
- [ ] `value_module_quadratic_form(T)`
- [ ] `modulus_bilinear_form(T)`
- [ ] `modulus_quadratic_form(T)`
- [ ] `quadratic_product(a)`
- [ ] `inner_product(a, b)`
- [ ] `lift(a)` / `representative(a)`
- [ ] `orthogonal_submodule(T, S)`
- [ ] `is_isometric_with_isometry(T, U)`
- [ ] `is_anti_isometric_with_anti_isometry(T, U)`
- [ ] `is_degenerate(T)`
- [ ] `is_semi_regular(T)`
- [ ] `radical_bilinear(T)`
- [ ] `radical_quadratic(T)`
- [ ] `normal_form(T; partial=false)`
- [ ] `brown_invariant(T)`
- [ ] `snf(T)` / `is_snf(T)`
- [ ] `rescale(T, k)`
- [ ] `genus(T, sig_pair)`
- [ ] `is_genus(T, sig_pair)`
- [ ] `direct_sum(T1, T2)` / `direct_product` / `biproduct`
- [ ] `submodules(T)`
- [ ] `stable_submodules(T, act)`

### §2.12 — Hermitian Lattices (`HermLat` / `QuadLat`)

- [ ] `base_field(L)` / `base_ring(L)`
- [ ] `fixed_field(L)` / `fixed_ring(L)`
- [ ] `involution(L)`
- [ ] `pseudo_matrix(L)` / `pseudo_basis(L)`
- [ ] `coefficient_ideals(L)`
- [ ] `absolute_basis(L)` / `absolute_basis_matrix(L)`
- [ ] `generators(L)` / `gram_matrix_of_generators(L)`
- [ ] `local_basis_matrix(L, p)`
- [ ] `jordan_decomposition(L, p)`
- [ ] `is_isotropic(L, p)`
- [ ] `is_modular(L)` / `is_modular(L, p)`
- [ ] `can_scale_totally_positive(L)`
- [ ] `volume(L)`
- [ ] `is_maximal_integral(L)` / `is_maximal(L)`
- [ ] `maximal_integral_lattice(L)`

### §2.13 — Quadratic Spaces with Isometry (`QuadSpaceWithIsom`)

- [ ] `quadratic_space_with_isometry(V, f; check)`
- [ ] `quadratic_space_with_isometry(V; neg=false)`
- [ ] `space(Vf)` / `isometry(Vf)` / `order_of_isometry(Vf)`
- [ ] `rank(Vf)` / `dim(Vf)` / `gram_matrix(Vf)` / `det(Vf)` / `discriminant(Vf)`
- [ ] `diagonal(Vf)` / `signature_tuple(Vf)`
- [ ] `is_definite(Vf)` / `is_positive_definite(Vf)` / `is_negative_definite(Vf)`
- [ ] `characteristic_polynomial(Vf)` / `minimal_polynomial(Vf)`
- [ ] `Base.:^(Vf, n)`
- [ ] `direct_sum(Vf, Wg)`
- [ ] `rescale(Vf, a)`
- [ ] `rational_spinor_norm(Vf; b)`

### §2.14 — Lattices with Isometry (`ZZLatWithIsom`)

#### Construction

- [ ] `integer_lattice_with_isometry(L, f; check, ambient_representation)`
- [ ] `integer_lattice_with_isometry(L; neg=false)`
- [ ] `lattice(Vf::QuadSpaceWithIsom)`
- [ ] `lattice_in_same_ambient_space(Lf, B)`

#### Accessors

- [ ] `isometry(Lf)`
- [ ] `ambient_isometry(Lf)`
- [ ] `ambient_space(Lf)`
- [ ] `lattice(Lf)`
- [ ] `basis_matrix(Lf)`
- [ ] `order_of_isometry(Lf)`
- [ ] `characteristic_polynomial(Lf)` / `minimal_polynomial(Lf)`

#### Type classification

- [ ] `type(Lf)`
- [ ] `is_of_type(Lf, t::Dict)`
- [ ] `is_of_same_type(Lf, Mg)`
- [ ] `is_of_hermitian_type(Lf)`
- [ ] `hermitian_structure(Lf)`
- [ ] `trace_lattice_with_isometry(H)`
- [ ] `is_hermitian(t::Dict)`

#### Operations

- [ ] `Base.:^(Lf, n)`
- [ ] `direct_sum(Lf, Mg)`
- [ ] `dual(Lf)`
- [ ] `lll(Lf)`
- [ ] `rescale(Lf, a)`
- [ ] `orthogonal_submodule(Lf, B)`

#### Kernel sublattices

- [ ] `kernel_lattice(Lf, p)`
- [ ] `kernel_lattice(Lf, l)`
- [ ] `invariant_lattice(Lf)`
- [ ] `coinvariant_lattice(Lf)`
- [ ] `invariant_coinvariant_pair(Lf)`

#### Discriminant groups

- [ ] `discriminant_group(Lf)`
- [ ] `image_centralizer_in_Oq(Lf)`
- [ ] `discriminant_representation(L, G)`

#### Spinor norm

- [ ] `signatures(Lf)`
- [ ] `rational_spinor_norm(Lf; b)`

#### Enumeration

- [ ] `enumerate_classes_of_lattices_with_isometry(gen, poly)`
- [ ] `enumerate_classes_of_lattices_with_isometry(::Union{ZZGenus, ZZLat}, ::Int)`
- [ ] `representatives_of_hermitian_type(gen, poly)`
- [ ] `representatives_of_hermitian_type(::Union{ZZGenus, ZZLat}, ::Int, ::Int)`
- [ ] `admissible_triples(gen, p)`
- [ ] `is_admissible_triple(::ZZGenus, ::ZZGenus, ::ZZGenus, ::Int)`
- [ ] `splitting(Lf)`
- [ ] `splitting_of_hermitian_type(Lf)`
- [ ] `splitting_of_prime_power(Lf, p)`
- [ ] `splitting_of_pure_mixed_prime_power(Lf, p)`
- [ ] `splitting_of_mixed_prime_power(Lf, p)`

### §2.15 — Primitive Embeddings

- [ ] `primitive_embeddings(L, M)`
- [ ] `primitive_embeddings(G::ZZGenus, M)`
- [ ] `primitive_embeddings(q::TorQuadModule, sig, M)`
- [ ] `primitive_extensions(M, N)`
- [ ] `equivariant_primitive_extensions(Mf, Nf; glue_only=false)`
- [ ] `admissible_equivariant_primitive_extensions(Mf, Nf, gen, poly, p)`

### §2.16 — Hermitian Genera

- [ ] `genus(L::HermLat)`
- [ ] `genus(L::HermLat, p)`
- [ ] `hermitian_genera(E, rank, sigs, det)`
- [ ] `hermitian_local_genera(E, p, rank, det_val, min_scale, max_scale)`
- [ ] `representative(G)` / `representatives(G)`
- [ ] `genus_representatives(L)`
- [ ] `mass(L)`
- [ ] `rank(G)` / `primes(G)` / `signatures(G)` / `is_integral(G)`
- [ ] `scale(G)` / `norm(G)` / `local_symbols(G)`
- [ ] `direct_sum(G1, G2)` / `rescale(G, a)`
- [ ] `is_ramified(g)` / `is_split(g)` / `is_inert(g)` / `is_dyadic(g)`

### §2.17 — Isometry Group Actions on Lattices

- [ ] `is_isometry(L, f)`
- [ ] `is_isometry_list(L, fs)`
- [ ] `is_isometry_group(L, G)`
- [ ] `is_stable_isometry(L, S, f)`
- [ ] `is_special_isometry(L, f)`
- [ ] `special_orthogonal_group(L)` / `special_subgroup(G)`
- [ ] `stable_orthogonal_group(L, S)` / `stable_subgroup(G, S)`
- [ ] `stabilizer_discriminant_subgroup(G, T)`
- [ ] `stabilizer_in_orthogonal_group(L, S)`
- [ ] `pointwise_stabilizer_in_orthogonal_group(L, S)`
- [ ] `setwise_stabilizer_in_orthogonal_group(L, S)`
- [ ] `pointwise_stabilizer_orthogonal_complement_in_orthogonal_group(L, S)`
- [ ] `stabilizer_in_diagonal_action(L1, L2)`
- [ ] `maximal_extension(::ZZLat, ::ZZLat, ::MatGroup)`
- [ ] `saturation(L, S)`
- [ ] `is_saturated_with_saturation(L, S)`
- [ ] `extend_to_ambient_space(L, f)`
- [ ] `restrict_to_lattice(L, f)`

### §3 — Oscar.jl (Integration Points)

- [ ] `Oscar.ZZLat`
- [ ] `Oscar.to_oscar(obj)`

### §4.1 — Nemo.jl: LLL Reduction

- [ ] `lll(B::ZZMatrix, ctx::LLLContext)`
- [ ] `lll_with_transform(B)`
- [ ] `lll_gram(G)`
- [ ] `lll_gram_with_transform(G)`

### §4.2 — Nemo.jl: Hermite Normal Form

- [ ] `hnf(X)`
- [ ] `hnf_with_transform(X)`

### §4.3 — Nemo.jl: Smith Normal Form

- [ ] `snf(X)`
- [ ] `snf_with_transform(X)`

### §5 — LLLplus.jl

- [ ] `lll(B)`
- [ ] `seysen(B)`
- [ ] `hkz(B)`
- [ ] `brun(B)`
- [ ] `cvp(Q, R, y)`
- [ ] `subsetsum`
- [ ] `integerfeasibility`
- [ ] `rationalapprox`

### §6 — LatticeAlgorithms.jl

- [ ] LLL reduction capability
- [ ] KZ (HKZ) reduction capability
- [ ] SVP solver capability (Fincke-Pohst enumeration)
- [ ] CVP solver capability (sphere decoding / A* search)
- [ ] Predefined lattices capability (`D_n`, repetition-GKP)
- [ ] MLD for surface-square GKP capability

---

## 2. `nemo_hecke_lattice_reference.md`

*(Most methods overlap with `julia_lattice_methods_reference.md`; only unique additions or distinct groupings listed.)*

### §2.9 — Vinberg Algorithm

- [ ] `vinberg_algorithm(Q::ZZMatrix, ub; v0, root_lengths, direction_vector)`
- [ ] `vinberg_algorithm(S::ZZLat, ub; v0, root_lengths, direction_vector)`
- [ ] `short_vectors_affine(S, v, a, d)`

### §2.12 — Hermitian-Specific Surfaces

- [ ] `jordan_decomposition(L, p)`
- [ ] `is_isotropic(L, p)` / `is_modular(L)` / `is_modular(L, p)`
- [ ] `volume(L)`
- [ ] `genus(L::HermLat)` / `genus(L::HermLat, p)`
- [ ] `hermitian_genera(E, rank, sigs, det)` / `hermitian_local_genera(E, p, rank, det_val, min_scale, max_scale)`
- [ ] `mass(L)`

---

## 3. `LieTheory/cartan_matrix.md`

### Constructors

- [ ] `cartan_matrix(::Symbol, ::Int)`
- [ ] `cartan_matrix(::Vector{Tuple{Symbol,Int}})`

### Properties

- [ ] `is_cartan_matrix(::ZZMatrix)`
- [ ] `cartan_symmetrizer(::ZZMatrix)`
- [ ] `cartan_bilinear_form(::ZZMatrix)`

### Cartan Types

- [ ] `is_cartan_type(::Symbol, ::Int)`
- [ ] `cartan_type(::ZZMatrix)`
- [ ] `cartan_type_with_ordering(::ZZMatrix)`

---

## 4. `LieTheory/root_systems.md`

### Constructors

- [ ] `root_system(::ZZMatrix)`
- [ ] `root_system(::Symbol, ::Int64)`
- [ ] `root_system(::Vector{Tuple{Symbol, Int64}})`

### Properties

- [ ] `is_simple(::RootSystem)`
- [ ] `rank(::RootSystem)`

### Cartan Matrix and Weyl Group

- [ ] `cartan_matrix(::RootSystem)`
- [ ] `weight_lattice(::RootSystem)`
- [ ] `weyl_group(::RootSystem)`

### Root System Type

- [ ] `has_root_system_type(::RootSystem)`
- [ ] `root_system_type(::RootSystem)`
- [ ] `root_system_type_with_ordering(::RootSystem)`

### Root Getters

- [ ] `number_of_roots(::RootSystem)`
- [ ] `number_of_positive_roots(::RootSystem)`
- [ ] `number_of_simple_roots(::RootSystem)`
- [ ] `root(::RootSystem, ::Int64)`
- [ ] `roots(::RootSystem)`
- [ ] `simple_root(::RootSystem, ::Int64)`
- [ ] `simple_roots(::RootSystem)`
- [ ] `positive_root(::RootSystem, ::Int64)`
- [ ] `positive_roots(::RootSystem)`
- [ ] `negative_root(::RootSystem, ::Int64)`
- [ ] `negative_roots(::RootSystem)`
- [ ] `highest_root(::RootSystem)`

### Coroot Getters

- [ ] `coroot(::RootSystem, ::Int64)`
- [ ] `coroots(::RootSystem)`
- [ ] `simple_coroot(::RootSystem, ::Int64)`
- [ ] `simple_coroots(::RootSystem)`
- [ ] `positive_coroot(::RootSystem, ::Int64)`
- [ ] `positive_coroots(::RootSystem)`
- [ ] `negative_coroot(::RootSystem, ::Int64)`
- [ ] `negative_coroots(::RootSystem)`

### Weight Getters

- [ ] `fundamental_weight(::RootSystem, ::Int64)`
- [ ] `fundamental_weights(::RootSystem)`
- [ ] `weyl_vector(::RootSystem)`

### Root Space Elements

- [ ] `RootSpaceElem(::RootSystem, ::Vector{<:RationalUnion})`
- [ ] `RootSpaceElem(::RootSystem, ::QQMatrix)`
- [ ] `RootSpaceElem(::WeightLatticeElem)`
- [ ] `zero(::Type{RootSpaceElem}, ::RootSystem)`
- [ ] `root_system(::RootSpaceElem)`
- [ ] `coeff(::RootSpaceElem, ::Int)`
- [ ] `coefficients(::RootSpaceElem)`
- [ ] `height(::RootSpaceElem)`
- [ ] `iszero(::RootSpaceElem)`

### Root Testing

- [ ] `is_root(::RootSpaceElem)`
- [ ] `is_root_with_index(::RootSpaceElem)`
- [ ] `is_simple_root(::RootSpaceElem)`
- [ ] `is_simple_root_with_index(::RootSpaceElem)`
- [ ] `is_positive_root(::RootSpaceElem)`
- [ ] `is_positive_root_with_index(::RootSpaceElem)`
- [ ] `is_negative_root(::RootSpaceElem)`
- [ ] `is_negative_root_with_index(::RootSpaceElem)`

### Reflections (RootSpaceElem)

- [ ] `reflect(::RootSpaceElem, ::Int)`
- [ ] `reflect!(::RootSpaceElem, ::Int)`
- [ ] `reflect(::RootSpaceElem, ::RootSpaceElem)`
- [ ] `reflect!(::RootSpaceElem, ::RootSpaceElem)`

### Dual Root Space Elements

- [ ] `DualRootSpaceElem(::RootSystem, ::Vector{<:RationalUnion})`
- [ ] `DualRootSpaceElem(::RootSystem, ::QQMatrix)`
- [ ] `zero(::Type{DualRootSpaceElem}, ::RootSystem)`
- [ ] `root_system(::DualRootSpaceElem)`
- [ ] `coeff(::DualRootSpaceElem, ::Int)`
- [ ] `coefficients(::DualRootSpaceElem)`
- [ ] `height(::DualRootSpaceElem)`
- [ ] `iszero(::DualRootSpaceElem)`

### Coroot Testing

- [ ] `is_coroot(::DualRootSpaceElem)`
- [ ] `is_coroot_with_index(::DualRootSpaceElem)`
- [ ] `is_simple_coroot(::DualRootSpaceElem)`
- [ ] `is_simple_coroot_with_index(::DualRootSpaceElem)`
- [ ] `is_positive_coroot(::DualRootSpaceElem)`
- [ ] `is_positive_coroot_with_index(::DualRootSpaceElem)`
- [ ] `is_negative_coroot(::DualRootSpaceElem)`
- [ ] `is_negative_coroot_with_index(::DualRootSpaceElem)`

---

## 5. `LieTheory/weight_lattices.md`

### Constructors

- [ ] `weight_lattice(::RootSystem)`

### Properties

- [ ] `rank(::WeightLattice)`
- [ ] `is_finite(::WeightLattice)`
- [ ] `zero(::WeightLattice)`
- [ ] `gen(::WeightLattice, ::Int)`
- [ ] `gens(::WeightLattice)`
- [ ] `root_system(::WeightLattice)`

### Weight Lattice Elements

- [ ] `WeightLatticeElem(::WeightLattice, ::Vector{<:IntegerUnion})`
- [ ] `WeightLatticeElem(::RootSystem, ::Vector{<:IntegerUnion})`
- [ ] `WeightLatticeElem(::WeightLattice, ::ZZMatrix)`
- [ ] `WeightLatticeElem(::RootSystem, ::ZZMatrix)`
- [ ] `WeightLatticeElem(::RootSpaceElem)`
- [ ] `coeff(::WeightLatticeElem, ::Int)`
- [ ] `coefficients(::WeightLatticeElem)`
- [ ] `iszero(::WeightLatticeElem)`
- [ ] `is_dominant(::WeightLatticeElem)`
- [ ] `is_fundamental_weight(::WeightLatticeElem)`
- [ ] `is_fundamental_weight_with_index(::WeightLatticeElem)`

### Reflections (WeightLatticeElem)

- [ ] `reflect(::WeightLatticeElem, ::Int)`
- [ ] `reflect!(::WeightLatticeElem, ::Int)`
- [ ] `reflect(::WeightLatticeElem, ::RootSpaceElem)`
- [ ] `reflect!(::WeightLatticeElem, ::RootSpaceElem)`

### Conjugate Dominant Weight

- [ ] `conjugate_dominant_weight(::WeightLatticeElem)`
- [ ] `conjugate_dominant_weight_with_elem(::WeightLatticeElem)`

---

## 6. `LieTheory/weyl_groups.md`

### Constructors

- [ ] `weyl_group(::RootSystem)`
- [ ] `weyl_group(::ZZMatrix)`
- [ ] `weyl_group(::Symbol, ::Int)`
- [ ] `weyl_group(::Vector{Tuple{Symbol,Int}})`

### Basic Properties

- [ ] `is_finite(::WeylGroup)`
- [ ] `one(::WeylGroup)`
- [ ] `isone(::WeylGroupElem)`
- [ ] `gen(::WeylGroup, ::Int)`
- [ ] `gens(::WeylGroup)`
- [ ] `number_of_generators(::WeylGroup)`
- [ ] `order(::Type{T}, ::WeylGroup) where {T}`
- [ ] `is_finite_order(::WeylGroupElem)`
- [ ] `order(::Type{T}, ::WeylGroupElem) where {T}`
- [ ] `root_system(::WeylGroup)`

### Element Constructors

- [ ] `reflection(::RootSpaceElem)`

### Words and Length

- [ ] `word(::WeylGroupElem)`
- [ ] `length(::WeylGroupElem)`
- [ ] `longest_element(::WeylGroup)`

### Bruhat Order

- [ ] `<(::WeylGroupElem, ::WeylGroupElem)`

### Reduced Expressions

- [ ] `reduced_expressions(::WeylGroupElem)`

### Action on Roots and Weights

- [ ] `*(::Union{RootSpaceElem,WeightLatticeElem}, ::WeylGroupElem)`
- [ ] `geometric_representation(::WeylGroup)`
- [ ] `dual_geometric_representation(::WeylGroup)`

### Orbits

- [ ] `weyl_orbit(::WeightLatticeElem)`

---

## 7. `AlgebraicGeometry/Surfaces/K3Surfaces.md`

- [ ] `K3_surface_automorphism_group(S::ZZLat)`
- [ ] `borcherds_method`
- [ ] `K3Chamber` (type)
- [ ] `chamber(data::BorcherdsCtx, weyl_vector::ZZMatrix, parent_wall::ZZMatrix=zero_matrix(ZZ, 0, 0))`
- [ ] `weyl_vector(D::K3Chamber)`
- [ ] `walls(::K3Chamber)`
- [ ] `inner_point(::K3Chamber)`
- [ ] `rays(::K3Chamber)`
- [ ] `aut(::K3Chamber)`
- [ ] `hom(::K3Chamber,::K3Chamber)`
- [ ] `adjacent_chamber(D::K3Chamber, v::ZZMatrix)`
- [ ] `separating_hyperplanes(S::ZZLat, v::QQMatrix, h::QQMatrix, d)`
- [ ] `has_zero_entropy`

---

## 8. `AlgebraicGeometry/Surfaces/EnriquesSurfaces.md`

### Automorphisms

- [ ] `generic_enriques_surface(n::Int)`
- [ ] `enriques_surface_automorphism_group(SY2::ZZLat, SX::ZZLat)`

### The Surface

- [ ] `EnriquesBorcherdsCtx` (type)
- [ ] `borcherds_method(Y::EnriquesBorcherdsCtx; max_nchambers=-1)`
- [ ] `splitting_roots_mod2(Y::EnriquesBorcherdsCtx)`
- [ ] `root_invariant(Y::EnriquesBorcherdsCtx)`
- [ ] `mass(ECtx::EnriquesBorcherdsCtx)`
- [ ] `numerical_lattice(Y::EnriquesBorcherdsCtx)`
- [ ] `numerical_lattice_of_K3_cover(Y::EnriquesBorcherdsCtx)`
- [ ] `invariant_lattice_of_K3_cover(Y::EnriquesBorcherdsCtx)`

### Chambers

- [ ] `rays(D::EnriquesChamber)`
- [ ] `isotropic_rays(D::EnriquesChamber)`
- [ ] `walls(D::EnriquesChamber)`
- [ ] `hom(D1::EnriquesChamber, D2::EnriquesChamber)`
- [ ] `adjacent_chamber(D::EnriquesChamber, v::ZZMatrix)`
- [ ] `chamber_invariants(Y::EnriquesBorcherdsCtx)`

### Orbits of Nef Divisors

- [ ] `isomorphism_classes_polarizations(Y::EnriquesBorcherdsCtx, h::ZZMatrix)`
- [ ] `isomorphism_classes_elliptic_fibrations(Y::EnriquesBorcherdsCtx)`
- [ ] `reducible_fibers(Y::EnriquesBorcherdsCtx, fbar::TorQuadModuleElem)`

---

## 9. `NumberTheory/QuadFormAndIsom/spacewithisom.md`

### Types

- [ ] `QuadSpaceWithIsom` (type)

### Accessors

- [ ] `isometry(::QuadSpaceWithIsom)`
- [ ] `order_of_isometry(::QuadSpaceWithIsom)`
- [ ] `space(::QuadSpaceWithIsom)`

### Constructors

- [ ] `quadratic_space_with_isometry(::Hecke.QuadSpace, ::QQMatrix)`
- [ ] `quadratic_space_with_isometry(::Hecke.QuadSpace)`

### Attributes

- [ ] `characteristic_polynomial(::QuadSpaceWithIsom)`
- [ ] `det(::QuadSpaceWithIsom)`
- [ ] `diagonal(::QuadSpaceWithIsom)`
- [ ] `dim(::QuadSpaceWithIsom)`
- [ ] `discriminant(::QuadSpaceWithIsom)`
- [ ] `gram_matrix(::QuadSpaceWithIsom)`
- [ ] `is_definite(::QuadSpaceWithIsom)`
- [ ] `is_positive_definite(::QuadSpaceWithIsom)`
- [ ] `is_negative_definite(::QuadSpaceWithIsom)`
- [ ] `minimal_polynomial(::QuadSpaceWithIsom)`
- [ ] `rank(::QuadSpaceWithIsom)`
- [ ] `signature_tuple(::QuadSpaceWithIsom)`

### Operations

- [ ] `^(::QuadSpaceWithIsom, ::Int)`
- [ ] `direct_sum(::Vector{QuadSpaceWithIsom})`
- [ ] `rescale(::QuadSpaceWithIsom, ::RationalUnion)`

### Spinor Norm

- [ ] `rational_spinor_norm(::QuadSpaceWithIsom)`

---

## 10. `NumberTheory/QuadFormAndIsom/latwithisom.md`

### Types

- [ ] `ZZLatWithIsom` (type)

### Accessors

- [ ] `ambient_isometry(::ZZLatWithIsom)`
- [ ] `ambient_space(::ZZLatWithIsom)`
- [ ] `isometry(::ZZLatWithIsom)`
- [ ] `lattice(::ZZLatWithIsom)`
- [ ] `order_of_isometry(::ZZLatWithIsom)`

### Constructors

- [ ] `integer_lattice_with_isometry(::ZZLat, ::QQMatrix)`
- [ ] `integer_lattice_with_isometry(::ZZLat)`
- [ ] `lattice(::QuadSpaceWithIsom)`
- [ ] `lattice(::QuadSpaceWithIsom, ::MatElem{<:RationalUnion})`
- [ ] `lattice_in_same_ambient_space(::ZZLatWithIsom, ::MatElem)`

### Attributes

- [ ] `basis_matrix(::ZZLatWithIsom)`
- [ ] `characteristic_polynomial(::ZZLatWithIsom)`
- [ ] `degree(::ZZLatWithIsom)`
- [ ] `det(::ZZLatWithIsom)`
- [ ] `discriminant(::ZZLatWithIsom)`
- [ ] `genus(::ZZLatWithIsom)`
- [ ] `gram_matrix(::ZZLatWithIsom)`
- [ ] `is_definite(::ZZLatWithIsom)`
- [ ] `is_even(::ZZLatWithIsom)`
- [ ] `is_elementary(::ZZLatWithIsom, ::IntegerUnion)`
- [ ] `is_elementary_with_prime(::ZZLatWithIsom)`
- [ ] `is_integral(::ZZLatWithIsom)`
- [ ] `is_positive_definite(::ZZLatWithIsom)`
- [ ] `is_primary(::ZZLatWithIsom, ::IntegerUnion)`
- [ ] `is_primary_with_prime(::ZZLatWithIsom)`
- [ ] `is_negative_definite(::ZZLatWithIsom)`
- [ ] `is_unimodular(::ZZLatWithIsom)`
- [ ] `minimum(::ZZLatWithIsom)`
- [ ] `minimal_polynomial(::ZZLatWithIsom)`
- [ ] `norm(::ZZLatWithIsom)`
- [ ] `rank(::ZZLatWithIsom)`
- [ ] `rational_span(::ZZLatWithIsom)`
- [ ] `scale(::ZZLatWithIsom)`
- [ ] `signature_tuple(::ZZLatWithIsom)`

### Operations

- [ ] `^(::ZZLatWithIsom, ::Int)`
- [ ] `direct_sum(::Vector{ZZLatWithIsom})`
- [ ] `dual(::ZZLatWithIsom)`
- [ ] `lll(::ZZLatWithIsom)`
- [ ] `orthogonal_submodule(::ZZLatWithIsom, ::QQMatrix)`
- [ ] `rescale(::ZZLatWithIsom, ::RationalUnion)`

### Type Classification

- [ ] `type(::ZZLatWithIsom)`
- [ ] `is_of_type(::ZZLatWithIsom, ::Dict)`
- [ ] `is_of_same_type(::ZZLatWithIsom, ::ZZLatWithIsom)`
- [ ] `is_of_hermitian_type(::ZZLatWithIsom)`
- [ ] `is_hermitian(::Dict)`

### Hermitian Structure

- [ ] `hermitian_structure(::ZZLatWithIsom)`

### Discriminant Groups

- [ ] `discriminant_group(::ZZLatWithIsom)`
- [ ] `image_centralizer_in_Oq(::ZZLatWithIsom)`
- [ ] `discriminant_representation(::ZZLat, ::MatGroup)`

### Kernel Sublattices

- [ ] `kernel_lattice(::ZZLatWithIsom, ::Union{ZZPolyRingElem, QQPolyRingElem})`
- [ ] `kernel_lattice(::ZZLatWithIsom, ::Integer)`
- [ ] `coinvariant_lattice(::ZZLatWithIsom)`
- [ ] `invariant_lattice(::ZZLatWithIsom)`
- [ ] `invariant_coinvariant_pair(::ZZLatWithIsom)`

### Signatures and Spinor Norm

- [ ] `signatures(::ZZLatWithIsom)`
- [ ] `rational_spinor_norm(::ZZLatWithIsom)`

---

## 11. `NumberTheory/QuadFormAndIsom/fingrpact.md`

### Change of Basis Representation

- [ ] `extend_to_ambient_space`
- [ ] `restrict_to_lattice`

### Invariant and Coinvariant Lattices

- [ ] `coinvariant_lattice(::ZZLat, ::MatGroup)`
- [ ] `invariant_lattice(::ZZLat, ::MatGroup)`
- [ ] `invariant_coinvariant_pair(::ZZLat, ::Union{QQMatrix, Vector{QQMatrix}, MatGroup})`

### Special Isometries

- [ ] `special_orthogonal_group(::ZZLat)`
- [ ] `special_subgroup(::ZZLat, ::MatGroup)`

### Stable Isometries

- [ ] `stable_orthogonal_group(::ZZLat)`
- [ ] `stable_subgroup(::ZZLat, ::MatGroup)`

### Stabilizers

- [ ] `stabilizer_discriminant_subgroup`
- [ ] `stabilizer_in_diagonal_action`
- [ ] `maximal_extension(::ZZLat, ::ZZLat, ::MatGroup)`
- [ ] `stabilizer_in_orthogonal_group`
- [ ] `pointwise_stabilizer_in_orthogonal_group`
- [ ] `setwise_stabilizer_in_orthogonal_group`
- [ ] `pointwise_stabilizer_orthogonal_complement_in_orthogonal_group`

### Saturation

- [ ] `saturation(::ZZLat, ::MatGroup, ::MatGroup)`
- [ ] `saturation(::ZZLat, ::MatGroup)`
- [ ] `is_saturated_with_saturation`

### Isometry Checks

- [ ] `is_isometry(::Hecke.QuadSpace, ::QQMatrix)`
- [ ] `is_isometry(::ZZLat, ::QQMatrix)`
- [ ] `is_isometry_list(::Hecke.QuadSpace, ::Vector{QQMatrix})`
- [ ] `is_isometry_list(::ZZLat, ::Vector{QQMatrix})`
- [ ] `is_isometry_group(::Hecke.QuadSpace, ::MatGroup)`
- [ ] `is_isometry_group(::ZZLat, ::MatGroup)`
- [ ] `is_stable_isometry(::ZZLatWithIsom)`
- [ ] `is_special_isometry(::ZZLatWithIsom)`

---

## 12. `NumberTheory/QuadFormAndIsom/enumeration.md`

### Admissible Triples

- [ ] `admissible_triples(::ZZGenus, ::Int)`
- [ ] `is_admissible_triple(::ZZGenus, ::ZZGenus, ::ZZGenus, ::Int)`

### Hermitian Case

- [ ] `representatives_of_hermitian_type(::Union{ZZLat, ZZGenus}, ::Union{ZZPolyRingElem, QQPolyRingElem}, ::Int)`
- [ ] `representatives_of_hermitian_type(::Union{ZZGenus, ZZLat}, ::Int, ::Int)`

### Generic Case

- [ ] `enumerate_classes_of_lattices_with_isometry(::Union{ZZGenus, ZZLat}, ::Int)`

### Underlying Machinery

- [ ] `representatives_of_hermitian_type(::ZZLatWithIsom, ::Int, ::Int)`
- [ ] `splitting_of_hermitian_type(::ZZLatWithIsom, ::Int, ::Int)`
- [ ] `splitting_of_prime_power(::ZZLatWithIsom, ::Int, ::Int)`
- [ ] `splitting_of_pure_mixed_prime_power(::ZZLatWithIsom, ::Int)`
- [ ] `splitting_of_mixed_prime_power(::ZZLatWithIsom, ::Int, ::Int)`
- [ ] `splitting(::ZZLatWithIsom, ::Int, ::Int)`

---

## 13. `NumberTheory/QuadFormAndIsom/primembed.md`

### Primitive Embeddings

- [ ] `primitive_embeddings(::ZZLat, ::ZZLat)`
- [ ] `primitive_embeddings(::ZZGenus, ::ZZLat)`
- [ ] `primitive_embeddings(::TorQuadModule, ::Tuple{Int, Int}, ::ZZLat)`

### Primitive Extensions

- [ ] `primitive_extensions(::ZZLat, ::ZZLat)`

### Equivariant Primitive Extensions

- [ ] `equivariant_primitive_extensions(::Union{ZZLatWithIsom, ZZLat}, ::Union{ZZLatWithIsom, ZZLat})`

### Admissible Equivariant Primitive Extensions

- [ ] `admissible_equivariant_primitive_extensions(::ZZLatWithIsom, ::ZZLatWithIsom, ::ZZLatWithIsom, ::Int, ::Int)`

---

## 14. `NumberTheory/QuadFormAndIsom/torquadmodwithisom.md`

### Types

- [ ] `TorQuadModuleWithIsom` (type)

### Accessors

- [ ] `underlying_module(::TorQuadModuleWithIsom)`
- [ ] `torsion_quadratic_module(::TorQuadModuleWithIsom)`
- [ ] `isometry(::TorQuadModuleWithIsom)`
- [ ] `order_of_isometry(::TorQuadModuleWithIsom)`

### Constructors

- [ ] `torsion_quadratic_module_with_isometry(::TorQuadModule, ::TorQuadModuleMap)`
- [ ] `torsion_quadratic_module_with_isometry(::QQMatrix, ::ZZMatrix)`

### Submodules

- [ ] `sub(::TorQuadModuleWithIsom, ::Vector{TorQuadModuleElem})`
- [ ] `primary_part(::TorQuadModuleWithIsom, ::IntegerUnion)`
- [ ] `orthogonal_submodule(::TorQuadModuleWithIsom, ::TorQuadModule)`
- [ ] `submodules(::TorQuadModuleWithIsom)`

### (Anti-)Isomorphism

- [ ] `automorphism_group_with_inclusion(::TorQuadModuleWithIsom)`
- [ ] `automorphism_group(::TorQuadModuleWithIsom)`
- [ ] `is_isomorphic_with_map(::TorQuadModuleWithIsom, ::TorQuadModuleWithIsom)`
- [ ] `is_anti_isomorphic_with_map(::TorQuadModuleWithIsom, ::TorQuadModuleWithIsom)`
