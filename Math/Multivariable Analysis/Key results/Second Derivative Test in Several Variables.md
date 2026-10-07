---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 18.1", "Hessian test"]
tags: [multivariable-analysis, hub]
---
![[§18 Second-Order Sufficient Conditions#^thm-18-1]]

## Treated in
- [[§18 Second-Order Sufficient Conditions#^thm-18-1|Theorem §18.1: Second-Order Sufficient Conditions — Unconstrained]], in [[§18 Second-Order Sufficient Conditions]]

## Its proof uses
- [[§6 Equality of Mixed Partials#^thm-6-1|Theorem §6.1: Schwarz–Clairaut]]
- [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-1|Theorem §11.1: Derivatives of F(t)]]
- [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-2|Theorem §11.2: Multivariable Taylor's Theorem]]
- [[§17 Optimization and Lagrange Multipliers#^def-17-1|Definition §17.1: Local Maximum]]
- [[§17 Optimization and Lagrange Multipliers#^def-17-2|Definition §17.2: Local Minimum]]
- [[§18 Second-Order Sufficient Conditions#^def-18-2|Definition §18.2: Positive Definite]]
- [[§18 Second-Order Sufficient Conditions#^def-18-3|Definition §18.3: Negative Definite]]
- [[§18 Second-Order Sufficient Conditions#^def-18-4|Definition §18.4: Indefinite]]

## Its proof uses (other subjects)
- [[Real spectral theorem]] (Linear Algebra)
- [[§31 Taylor's Theorem#^thm-31-2|451 §31.2: Taylor's Theorem with Lagrange Remainder]]

## Used in (Multivariable Analysis)
- (not cited later in the course)

## Connections
- **Proof idea.** At a critical point, second-order [[Multivariable Taylor's Theorem]] (from the 451 [[§31 Taylor's Theorem#^thm-31-2|Taylor's theorem]]) gives f(x₀ + h) − f(x₀) = ½ hᵀHh, with H evaluated at an intermediate point. Continuity of the second partials keeps H definite nearby. In one variable, H is just f″(x₀).
- **Linear algebra.** H is symmetric by [[Schwarz–Clairaut Theorem]], so the [[Real spectral theorem]] (LADR 7.29) diagonalizes it. H is positive definite iff all eigenvalues are positive, negative definite iff all are negative, and indefinite iff there are signs of both kinds. For other tests, see [[§25 Positive Operators#^ladr-7-38|LADR 7.38]] and [[§18 Second-Order Sufficient Conditions#^rem-18-9|Sylvester's criterion]].
- **Where hypotheses matter.** A semidefinite H is inconclusive. For example, x⁴ + y⁴ (a minimum) and x⁴ − y⁴ (a saddle) both have H = 0 at the origin. Candidates come from [[§17 Optimization and Lagrange Multipliers#^thm-17-1|Fermat's theorem]] (∇f = 0).
- **Local vs. global.** The test is local. Global extrema on a compact set exist ([[Heine–Borel Theorem]], [[Continuous Image of a Compact Space is Compact]]) and are found by comparing values at the candidates and on the boundary ([[§18 Second-Order Sufficient Conditions#^rem-18-10|The Logical Flow]]).
- **Also in [[Calculus]]:** [[§113 Maximum and Minimum Values#^thm-113-2|Calc Thm. §113.2]] (computational treatment with worked examples).
- **Also in [[Applied Linear Algebra]]:** [[§59★ Quadratic Forms#^thm-59-4|235 Thm. §59.4]] (definiteness of a symmetric matrix from the signs of its eigenvalues, with worked classifications).
- **Used in the honors thesis.** The N-variable form ([[§R2.1 The Hessian and the Second-Derivative Test in N Variables#^thm-r2-1-3|Thesis Thm. §R2.1.3]]) is the stability test for a vacuum of N scalar fields, whose Hessian is the mass matrix ([[§R1.4 The Mass Matrix Is the Hessian at the Vacuum#^thm-r1-4-3|Thesis Thm. §R1.4.3]]), and for stationary states of multipole lattices ([[§M3.2 Second Variation꞉ Plane-Wave Hessian and Bloch Stability#^thm-m3-2-2|Thesis Thm. §M3.2.2]]).
