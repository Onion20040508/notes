---
type: chapter
subject: "[[Linear Algebra]]"
chapter: 5
tags: [chapter, linear-algebra]
---
# 5 Eigenvalues and Eigenvectors
↑ [[Linear Algebra]]

**Builds on:** [[Linear Algebra — 1 Vector Spaces|1 Vector Spaces]] (2 citations), [[Linear Algebra — 2 Finite-Dimensional Vector Spaces|2 Finite-Dimensional Vector Spaces]] (6 citations), [[Linear Algebra — 3 Linear Maps|3 Linear Maps]] (11 citations), [[Linear Algebra — 4 Polynomials|4 Polynomials]] (8 citations)
**Used by:** [[Linear Algebra — 6 Inner Product Spaces|6 Inner Product Spaces]] (3), [[Linear Algebra — 7 Operators on Inner Product Spaces|7 Operators on Inner Product Spaces]] (5), [[Linear Algebra — 8 Operators on Complex Vector Spaces|8 Operators on Complex Vector Spaces]] (12), [[Linear Algebra — 9 Multilinear Algebra and Determinants|9 Multilinear Algebra and Determinants]] (3)

## Load-bearing results
The results in this chapter with the most later results depending on them.
- [[Linearly independent eigenvectors]] (5.11): 46 later results depend on it
- [[Null space and range of p(T) are invariant under T]] (5.18): 39 later results depend on it
- [[Operator cannot have more eigenvalues than dimension of vector space]] (5.12): 31 later results depend on it
- [[Q(T) = 0 ⟺ q is a polynomial multiple of the minimal polynomial]] (5.29): 31 later results depend on it

## 5A Invariant Subspaces
- 5.1 [[Operator]] (p. 133)
- 5.2 [[Invariant subspace]] (p. 133)
- 5.3 example: subspace invariant under differentiation operator (p. 133)
- 5.4 example: four invariant subspaces, not necessarily all different (p. 133)
- 5.5 [[Eigenvalue]] (p. 134)
- 5.6 example: eigenvalue (p. 134)
- 5.7 [[Equivalent conditions to be an eigenvalue]] (p. 135)
- 5.8 [[Eigenvector]] (p. 135)
- 5.9 example: eigenvalues and eigenvectors (p. 135)
- 5.11 [[Linearly independent eigenvectors]] (p. 136)
- 5.12 [[Operator cannot have more eigenvalues than dimension of vector space]] (p. 136)
- 5.13 notation: Tm (p. 137)
- 5.14 notation: p(T) (p. 137)
- 5.15 example: a polynomial applied to the differentiation operator (p. 138)
- 5.16 [[Product of polynomials]] (p. 138)
- 5.17 [[Multiplicative properties]] (p. 138)
- 5.18 [[Null space and range of p(T) are invariant under T]] (p. 139)

## 5B The Minimal Polynomial
- 5.19 [[Existence of eigenvalues]] (p. 143)
- 5.20 example: an operator on a complex vector space with no eigenvalues (p. 143)
- 5.21 [[Monic polynomial]] (p. 144)
- 5.22 [[Existence, uniqueness, and degree of minimal polynomial]] (p. 144)
- 5.24 [[Minimal polynomial]] (p. 145)
- 5.26 example: minimal polynomial of an operator on F5 (p. 146)
- 5.27 [[Eigenvalues are the zeros of the minimal polynomial]] (p. 146)
- 5.28 example: An operator whose eigenvalues cannot be found exactly (p. 147)
- 5.29 [[Q(T) = 0 ⟺ q is a polynomial multiple of the minimal polynomial]] (p. 148)
- 5.31 [[Minimal polynomial of a restriction operator]] (p. 148)
- 5.32 [[T not invertible ⟺ constant term of minimal polynomial of T is 0]] (p. 149)
- 5.33 [[Even-dimensional null space]] (p. 149)
- 5.34 [[Operators on odd-dimensional vector spaces have eigenvalues]] (p. 150)

## 5C Upper-Triangular Matrices
- 5.35 [[Matrix of an operator, M(T)]] (p. 154)
- 5.36 example: matrix of an operator with respect to standard basis (p. 154)
- 5.37 [[Diagonal of a matrix]] (p. 155)
- 5.38 [[Upper-triangular matrix]] (p. 155)
- 5.39 [[Conditions for upper-triangular matrix]] (p. 156)
- 5.40 [[Equation satisfied by operator with upper-triangular matrix]] (p. 156)
- 5.41 [[Determination of eigenvalues from upper-triangular matrix]] (p. 157)
- 5.42 example: eigenvalues via an upper-triangular matrix (p. 158)
- 5.43 example: whether T has an upper-triangular matrix can depend on F (p. 158)
- 5.44 [[Necessary and sufficient condition to have an upper-triangular matrix]] (p. 159)
- 5.47 [[If F = C, then every operator on V has an upper-triangular matrix]] (p. 160)

## 5D Diagonalizable Operators
- 5.48 [[Diagonal matrix (LADR 5.48)]] (p. 163)
- 5.49 example: diagonal matrix (p. 163)
- 5.50 [[Diagonalizable]] (p. 163)
- 5.51 example: diagonalization may require a different basis (p. 163)
- 5.52 [[Eigenspace, E(λ, T)]] (p. 164)
- 5.53 example: eigenspaces of an operator (p. 164)
- 5.54 [[Sum of eigenspaces is a direct sum]] (p. 164)
- 5.55 [[Conditions equivalent to diagonalizability]] (p. 165)
- 5.57 example: an operator that is not diagonalizable (p. 166)
- 5.58 [[Enough eigenvalues implies diagonalizability]] (p. 166)
- 5.59 example: using diagonalization to compute T100 (p. 167)
- 5.60 example: diagonalizable, but with no known exact eigenvalues (p. 168)
- 5.61 example: showing that an operator is not diagonalizable (p. 168)
- 5.62 [[Necessary and sufficient condition for diagonalizability]] (p. 169)
- 5.65 [[Restriction of diagonalizable operator to invariant subspace]] (p. 170)
- 5.66 [[Gershgorin disks]] (p. 170)
- 5.67 [[Gershgorin disk theorem]] (p. 171)

## 5E Commuting Operators
- 5.71 [[Commute]] (p. 175)
- 5.72 example: partial differentiation operators commute (p. 175)
- 5.74 [[Commuting operators correspond to commuting matrices]] (p. 176)
- 5.75 [[Eigenspace is invariant under commuting operator]] (p. 176)
- 5.76 [[Simultaneous diagonalizablity ⟺ commutativity]] (p. 176)
- 5.78 [[Common eigenvector for commuting operators]] (p. 177)
- 5.79 example: common eigenvector for partial differentiation operators (p. 177)
- 5.80 [[Commuting operators are simultaneously upper triangularizable]] (p. 178)
- 5.81 [[Eigenvalues of sum and product of commuting operators]] (p. 179)
