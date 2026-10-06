---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 12.1", "derivative of the determinant", "Lee Problem 7-4"]
tags: [differentiable-manifolds, hub]
---
![[§12 The Classical Groups Are Topological Manifolds#^prop-12-1]]

## Treated in
- [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|Proposition §12.1: Derivative of the Determinant]], in [[§12 The Classical Groups Are Topological Manifolds]]

## Its proof uses
- [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|Proposition §11.2: Properties of the Sign]]
- [[§11 Topological Groups and Classical Matrix Groups#^def-11-3|Definition §11.3: The Symmetric Group]]
- [[§11 Topological Groups and Classical Matrix Groups#^def-11-4|Definition §11.4: The Sign of a Permutation]]

## Its proof uses (other subjects)
- [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-47|LADR 8.47 Trace of a matrix]]
- [[§37 Determinants#^ladr-9-46|LADR 9.46 Formula for determinant of a matrix]]
- [[§37 Determinants#^ladr-9-49|LADR 9.49 Determinant is multiplicative]]
- [[Multivariable Chain Rule]] (Multivariable Analysis)
- [[§28 Basic Properties of the Derivative#^thm-28-2|451 §28.2: Arithmetic of Derivatives]]

## Used in (Differentiable Manifolds)
- [[§12 The Classical Groups Are Topological Manifolds#^cor-12-2|Corollary §12.2: Jacobi's Formula — Gradient Form]]
- [[§12 The Classical Groups Are Topological Manifolds#^cor-12-3|Corollary §12.3: 1 Is a Regular Value of det]]
- [[§12 The Classical Groups Are Topological Manifolds#^cor-12-4|Corollary §12.4: Every Nonzero Value Is a Regular Value of det]]
- [[§25 The Geometric Tangent Space#^thm-25-5|Theorem §25.5: The Classical Groups]]

## Connections
- **Used for.** The gradient of det does not vanish on SL(n,ℝ), and every c ≠ 0 is a regular value of det ([[§12 The Classical Groups Are Topological Manifolds#^cor-12-3|§12.3]], [[§12 The Classical Groups Are Topological Manifolds#^cor-12-4|§12.4]]), so SL(n,ℝ) is a manifold of dimension n² − 1 ([[§12 The Classical Groups Are Topological Manifolds#^cor-12-5|§12.5]]). At g = I the derivative is A ↦ tr A, whose kernel, the trace-zero matrices, is the tangent space of SL(n,ℝ) in [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]].
- **Only nonzero values.** For n ≥ 2, det(tA) = tⁿ det A, so the gradient of det vanishes at the zero matrix and 0 is a critical value; [[§12 The Classical Groups Are Topological Manifolds#^cor-12-4|§12.4]] covers exactly the c ≠ 0.
- **The method.** Differentiate along the line g + tA instead of expanding the Leibniz formula ([[§12 The Classical Groups Are Topological Manifolds#^rem-12-1|The Method]]). Made coordinate-free, dF_p(v) is the derivative of F(p + tv) at t = 0 ([[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]]), and on manifolds the computation of differentials by curves ([[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]]). The linear algebra is the multiplicativity of det and the trace of a matrix ([[§37 Determinants#^ladr-9-49|LADR 9.49]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-47|LADR 8.47]]).
- **Coming later in the course.** For Lie groups, the formula at g = I says that the differential at the identity of the homomorphism det : GL(n,ℝ) → ℝ^× is the trace; exponentiated, det(e^X) = e^(tr X).
- **Also in [[Ordinary Differential Equations]]:** [[§36 Basic Theory of Systems of First-Order Linear Equations#^thm-36-3|331 Thm. §36.3]] (Abel's theorem: the derivative of the Wronskian det X(t) of a solution matrix, W′ = (tr P)W, with worked examples).
