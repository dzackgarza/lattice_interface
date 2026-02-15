# Tests for §2.13-2.14: QuadSpaceWithIsom and ZZLatWithIsom

# -- QuadSpaceWithIsom --

@testitem "quadratic_space_with_isometry: pair space with identity" begin
    # method: quadratic_space_with_isometry(V; neg)
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    @test rank(Vf) == 2
    @test order_of_isometry(Vf) == 1
end

@testitem "quadratic_space_with_isometry: pair with negation" begin
    # method: quadratic_space_with_isometry(V; neg=true)
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V; neg = true)
    @test rank(Vf) == 2
    @test order_of_isometry(Vf) == 2
end

@testitem "space: extract space from QuadSpaceWithIsom" begin
    # method: space
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    @test rank(space(Vf)) == 2
end

@testitem "isometry: extract isometry matrix" begin
    # method: isometry(Vf)
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    f = isometry(Vf)
    @test f == identity_matrix(QQ, 2)
end

@testitem "characteristic_polynomial: QuadSpaceWithIsom" begin
    # method: characteristic_polynomial(Vf)
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V; neg = true)
    p = characteristic_polynomial(Vf)
    @test degree(p) == 2
end

# -- ZZLatWithIsom --

@testitem "integer_lattice_with_isometry: pair with identity" begin
    # method: integer_lattice_with_isometry(L; neg)
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test rank(lattice(Lf)) == 2
    @test order_of_isometry(Lf) == 1
end

@testitem "integer_lattice_with_isometry: pair with negation" begin
    # method: integer_lattice_with_isometry(L; neg=true)
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    @test order_of_isometry(Lf) == 2
end

@testitem "integer_lattice_with_isometry: explicit isometry matrix" begin
    # method: integer_lattice_with_isometry(L, f)
    using Oscar
    L = root_lattice(:A, 2)
    f = -identity_matrix(ZZ, 2)
    Lf = integer_lattice_with_isometry(L, f)
    @test isometry(Lf) == f
end

@testitem "lattice: extract ZZLat from ZZLatWithIsom" begin
    # method: lattice(Lf)
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test rank(lattice(Lf)) == 2
end

@testitem "isometry: ZZLatWithIsom isometry matrix" begin
    # method: isometry(Lf)
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test isometry(Lf) == identity_matrix(ZZ, 2)
end

@testitem "order_of_isometry: identity has order 1" begin
    # method: order_of_isometry
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test order_of_isometry(Lf) == 1
end

@testitem "characteristic_polynomial: ZZLatWithIsom" begin
    # method: characteristic_polynomial(Lf)
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    p = characteristic_polynomial(Lf)
    @test degree(p) == 2
end

@testitem "minimal_polynomial: ZZLatWithIsom" begin
    # method: minimal_polynomial(Lf)
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    p = minimal_polynomial(Lf)
    @test degree(p) >= 1
end

@testitem "^: raise isometry to power" begin
    # method: ^(Lf, n)
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    Lf2 = Lf^2
    @test order_of_isometry(Lf2) == 1
end

@testitem "direct_sum: equivariant direct sum" begin
    # method: direct_sum(Lf, Mg)
    using Oscar
    L = root_lattice(:A, 1)
    Lf = integer_lattice_with_isometry(L)
    Mg = integer_lattice_with_isometry(L; neg = true)
    S, _, _ = direct_sum(Lf, Mg)
    @test rank(lattice(S)) == 2
end

@testitem "dual: dual with induced isometry" begin
    # method: dual(Lf)
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    Df = dual(Lf)
    @test rank(lattice(Df)) == 2
end

@testitem "lll: LLL with isometry carried along" begin
    # method: lll(Lf)
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    Mf = lll(Lf)
    @test rank(lattice(Mf)) == 2
end

@testitem "rescale: ZZLatWithIsom rescale" begin
    # method: rescale(Lf, a)
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    Mf = rescale(Lf, 2)
    @test rank(lattice(Mf)) == 2
end

@testitem "invariant_lattice: fixed sublattice" begin
    # method: invariant_lattice(Lf)
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    I = invariant_lattice(Lf)
    @test rank(lattice(I)) == 2  # identity fixes everything
end

@testitem "coinvariant_lattice: orthogonal complement of fixed" begin
    # method: coinvariant_lattice(Lf)
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    C = coinvariant_lattice(Lf)
    @test rank(lattice(C)) == 0  # identity: coinvariant is trivial
end

@testitem "type: type of lattice-with-isometry" begin
    # method: type(Lf)
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    t = type(Lf)
    @test t isa Dict
end

@testitem "discriminant_group: ZZLatWithIsom discriminant group" begin
    # method: discriminant_group(Lf)
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    T = discriminant_group(Lf)
    @test order(T) == 3
end

@testitem "coverage guard: ZZLatWithIsom methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    L = root_lattice(:A, 2)
    sample = integer_lattice_with_isometry(L)
    assert_runtime_methods_covered(@__FILE__, sample)
end

@testitem "coverage guard: QuadSpaceWithIsom methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    sample = quadratic_space_with_isometry(V)
    assert_runtime_methods_covered(@__FILE__, sample)
end
