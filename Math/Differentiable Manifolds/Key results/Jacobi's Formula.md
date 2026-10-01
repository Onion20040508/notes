---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 5.9", "derivative of the determinant", "Lee Problem 7-4"]
tags: [differentiable-manifolds, hub]
---
![[§5 Topological Groups and Classical Matrix Groups#^prop-5-9]]

## Treated in
- [[§5 Topological Groups and Classical Matrix Groups#^prop-5-9|Proposition §5.9: Derivative of the Determinant]], in [[§5 Topological Groups and Classical Matrix Groups]]

## Its proof uses
- [[§5 Topological Groups and Classical Matrix Groups#^prop-5-2|Proposition §5.2: Properties of the Sign]]
- [[§5 Topological Groups and Classical Matrix Groups#^def-5-3|Definition §5.3: Permutations and the Sign]]

## Its proof uses (other subjects)
- [[8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-47|LADR 8.47 Trace of a matrix]]
- [[9C Determinants#^ladr-9-46|LADR 9.46 Formula for determinant of a matrix]]
- [[9C Determinants#^ladr-9-49|LADR 9.49 Determinant is multiplicative]]
- [[Multivariable Chain Rule]] (Multivariable Analysis)
- [[§28 Basic Properties of the Derivative#^thm-28-2|451 §28.2: Arithmetic of Derivatives]]

## Used in (Differentiable Manifolds)
- [[§5 Topological Groups and Classical Matrix Groups#^cor-5-10|Corollary §5.10: Jacobi's Formula — Gradient Form]]
- [[§5 Topological Groups and Classical Matrix Groups#^cor-5-11|Corollary §5.11: 1 Is a Regular Value of det]]
- [[§5 Topological Groups and Classical Matrix Groups#^cor-5-12|Corollary §5.12: Every Nonzero Value Is a Regular Value of det]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5|Theorem §11.5: The Classical Groups]]

## Connections
- **Used for.** The gradient of det does not vanish on SL(n,ℝ), and every c ≠ 0 is a regular value of det ([[§5 Topological Groups and Classical Matrix Groups#^cor-5-11|§5.11]], [[§5 Topological Groups and Classical Matrix Groups#^cor-5-12|§5.12]]), so SL(n,ℝ) is a manifold of dimension n² − 1 ([[§5 Topological Groups and Classical Matrix Groups#^cor-5-13|§5.13]]). At g = I the derivative is A ↦ tr A, whose kernel, the trace-zero matrices, is the tangent space of SL(n,ℝ) in [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5|§11.5]].
- **Only nonzero values.** For n ≥ 2, det(tA) = tⁿ det A, so the gradient of det vanishes at the zero matrix and 0 is a critical value; [[§5 Topological Groups and Classical Matrix Groups#^cor-5-12|§5.12]] covers exactly the c ≠ 0.
- **The method.** Differentiate along the line g + tA instead of expanding the Leibniz formula ([[§5 Topological Groups and Classical Matrix Groups#^rem-5-3|The Method]]). Made coordinate-free, dF_p(v) is the derivative of F(p + tv) at t = 0 ([[§10 Vector Spaces and Matrix Groups#^thm-10-10|§10.10]]), and on manifolds the computation of differentials by curves ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-31|§12.31]]). The linear algebra is the multiplicativity of det and the trace of a matrix ([[9C Determinants#^ladr-9-49|LADR 9.49]], [[8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-47|LADR 8.47]]).
- **Coming later in the course.** For Lie groups, the formula at g = I says that the differential at the identity of the homomorphism det : GL(n,ℝ) → ℝ^× is the trace; exponentiated, det(e^X) = e^(tr X).
