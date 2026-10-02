---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 9.1", "derivative of the determinant", "Lee Problem 7-4"]
tags: [differentiable-manifolds, hub]
---
![[§9 The Classical Groups Are Topological Manifolds#^prop-9-1]]

## Treated in
- [[§9 The Classical Groups Are Topological Manifolds#^prop-9-1|Proposition §9.1: Derivative of the Determinant]], in [[§9 The Classical Groups Are Topological Manifolds]]

## Its proof uses
- [[§8 Topological Groups and Classical Matrix Groups#^prop-8-2|Proposition §8.2: Properties of the Sign]]
- [[§8 Topological Groups and Classical Matrix Groups#^def-8-3|Definition §8.3: Permutations and the Sign]]

## Its proof uses (other subjects)
- [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-47|LADR 8.47 Trace of a matrix]]
- [[§34 Determinants#^ladr-9-46|LADR 9.46 Formula for determinant of a matrix]]
- [[§34 Determinants#^ladr-9-49|LADR 9.49 Determinant is multiplicative]]
- [[Multivariable Chain Rule]] (Multivariable Analysis)
- [[§28 Basic Properties of the Derivative#^thm-28-2|451 §28.2: Arithmetic of Derivatives]]

## Used in (Differentiable Manifolds)
- [[§9 The Classical Groups Are Topological Manifolds#^cor-9-2|Corollary §9.2: Jacobi's Formula — Gradient Form]]
- [[§9 The Classical Groups Are Topological Manifolds#^cor-9-3|Corollary §9.3: 1 Is a Regular Value of det]]
- [[§9 The Classical Groups Are Topological Manifolds#^cor-9-4|Corollary §9.4: Every Nonzero Value Is a Regular Value of det]]
- [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5|Theorem §20.5: The Classical Groups]]

## Connections
- **Used for.** The gradient of det does not vanish on SL(n,ℝ), and every c ≠ 0 is a regular value of det ([[§9 The Classical Groups Are Topological Manifolds#^cor-9-3|§9.3]], [[§9 The Classical Groups Are Topological Manifolds#^cor-9-4|§9.4]]), so SL(n,ℝ) is a manifold of dimension n² − 1 ([[§9 The Classical Groups Are Topological Manifolds#^cor-9-5|§9.5]]). At g = I the derivative is A ↦ tr A, whose kernel, the trace-zero matrices, is the tangent space of SL(n,ℝ) in [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5|§20.5]].
- **Only nonzero values.** For n ≥ 2, det(tA) = tⁿ det A, so the gradient of det vanishes at the zero matrix and 0 is a critical value; [[§9 The Classical Groups Are Topological Manifolds#^cor-9-4|§9.4]] covers exactly the c ≠ 0.
- **The method.** Differentiate along the line g + tA instead of expanding the Leibniz formula ([[§9 The Classical Groups Are Topological Manifolds#^rem-9-1|The Method]]). Made coordinate-free, dF_p(v) is the derivative of F(p + tv) at t = 0 ([[§18 The Differential of a Map Between Vector Spaces#^thm-18-3|§18.3]]), and on manifolds the computation of differentials by curves ([[§26 Tangent Vectors as Velocities of Curves#^cor-26-3|§26.3]]). The linear algebra is the multiplicativity of det and the trace of a matrix ([[§34 Determinants#^ladr-9-49|LADR 9.49]], [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-47|LADR 8.47]]).
- **Coming later in the course.** For Lie groups, the formula at g = I says that the differential at the identity of the homomorphism det : GL(n,ℝ) → ℝ^× is the trace; exponentiated, det(e^X) = e^(tr X).
- **Also in [[Ordinary Differential Equations]]:** [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-3|331 Thm. §30.3]] (Abel's theorem: the derivative of the Wronskian det X(t) of a solution matrix, W′ = (tr P)W, with worked examples).
