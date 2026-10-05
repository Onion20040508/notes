---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 11.1", "derivative of the determinant", "Lee Problem 7-4"]
tags: [differentiable-manifolds, hub]
---
![[§11 The Classical Groups Are Topological Manifolds#^prop-11-1]]

## Treated in
- [[§11 The Classical Groups Are Topological Manifolds#^prop-11-1|Proposition §11.1: Derivative of the Determinant]], in [[§11 The Classical Groups Are Topological Manifolds]]

## Its proof uses
- [[§10 Topological Groups and Classical Matrix Groups#^prop-10-2|Proposition §10.2: Properties of the Sign]]
- [[§10 Topological Groups and Classical Matrix Groups#^def-10-3|Definition §10.3: Permutations and the Sign]]

## Its proof uses (other subjects)
- [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-47|LADR 8.47 Trace of a matrix]]
- [[§34 Determinants#^ladr-9-46|LADR 9.46 Formula for determinant of a matrix]]
- [[§34 Determinants#^ladr-9-49|LADR 9.49 Determinant is multiplicative]]
- [[Multivariable Chain Rule]] (Multivariable Analysis)
- [[§28 Basic Properties of the Derivative#^thm-28-2|451 §28.2: Arithmetic of Derivatives]]

## Used in (Differentiable Manifolds)
- [[§11 The Classical Groups Are Topological Manifolds#^cor-11-2|Corollary §11.2: Jacobi's Formula — Gradient Form]]
- [[§11 The Classical Groups Are Topological Manifolds#^cor-11-3|Corollary §11.3: 1 Is a Regular Value of det]]
- [[§11 The Classical Groups Are Topological Manifolds#^cor-11-4|Corollary §11.4: Every Nonzero Value Is a Regular Value of det]]
- [[§23 The Geometric Tangent Space#^thm-23-5|Theorem §23.5: The Classical Groups]]

## Connections
- **Used for.** The gradient of det does not vanish on SL(n,ℝ), and every c ≠ 0 is a regular value of det ([[§11 The Classical Groups Are Topological Manifolds#^cor-11-3|§11.3]], [[§11 The Classical Groups Are Topological Manifolds#^cor-11-4|§11.4]]), so SL(n,ℝ) is a manifold of dimension n² − 1 ([[§11 The Classical Groups Are Topological Manifolds#^cor-11-5|§11.5]]). At g = I the derivative is A ↦ tr A, whose kernel, the trace-zero matrices, is the tangent space of SL(n,ℝ) in [[§23 The Geometric Tangent Space#^thm-23-5|§23.5]].
- **Only nonzero values.** For n ≥ 2, det(tA) = tⁿ det A, so the gradient of det vanishes at the zero matrix and 0 is a critical value; [[§11 The Classical Groups Are Topological Manifolds#^cor-11-4|§11.4]] covers exactly the c ≠ 0.
- **The method.** Differentiate along the line g + tA instead of expanding the Leibniz formula ([[§11 The Classical Groups Are Topological Manifolds#^rem-11-1|The Method]]). Made coordinate-free, dF_p(v) is the derivative of F(p + tv) at t = 0 ([[§21 The Differential of a Map Between Vector Spaces#^thm-21-3|§21.3]]), and on manifolds the computation of differentials by curves ([[§29 Tangent Vectors as Velocities of Curves#^cor-29-3|§29.3]]). The linear algebra is the multiplicativity of det and the trace of a matrix ([[§34 Determinants#^ladr-9-49|LADR 9.49]], [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-47|LADR 8.47]]).
- **Coming later in the course.** For Lie groups, the formula at g = I says that the differential at the identity of the homomorphism det : GL(n,ℝ) → ℝ^× is the trace; exponentiated, det(e^X) = e^(tr X).
- **Also in [[Ordinary Differential Equations]]:** [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-3|331 Thm. §30.3]] (Abel's theorem: the derivative of the Wronskian det X(t) of a solution matrix, W′ = (tr P)W, with worked examples).
