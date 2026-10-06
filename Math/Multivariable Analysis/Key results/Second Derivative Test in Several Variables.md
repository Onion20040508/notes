---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 14.4", "Hessian test"]
tags: [multivariable-analysis, hub]
---
![[§14 Optimization and Lagrange Multipliers#^thm-14-4]]

## Treated in
- [[§14 Optimization and Lagrange Multipliers#^thm-14-4|Theorem §14.4: Second-Order Sufficient Conditions — Unconstrained]], in [[§14 Optimization and Lagrange Multipliers]]

## Its proof uses
- [[§5 Equality of Mixed Partials#^thm-5-1|Theorem §5.1: Schwarz–Clairaut]]
- [[§9 Taylor's Theorem for Multivariable Functions#^thm-9-1|Theorem §9.1: Derivatives of F(t)]]
- [[§9 Taylor's Theorem for Multivariable Functions#^thm-9-2|Theorem §9.2: Multivariable Taylor's Theorem]]
- [[§14 Optimization and Lagrange Multipliers#^def-14-1|Definition §14.1: Local Maximum]]
- [[§14 Optimization and Lagrange Multipliers#^def-14-new1|Definition §14.1: Local Minimum]]
- [[§14a Second-Order Sufficient Conditions#^def-14-3|Definition §14.3: Positive Definite]]
- [[§14a Second-Order Sufficient Conditions#^def-14-new2|Definition §14.3: Negative Definite]]
- [[§14a Second-Order Sufficient Conditions#^def-14-new3|Definition §14.3: Indefinite]]

## Its proof uses (other subjects)
- [[Real spectral theorem]] (Linear Algebra)
- [[§31 Taylor's Theorem#^thm-31-2|451 §31.2: Taylor's Theorem with Lagrange Remainder]]

## Used in (Multivariable Analysis)
- (not cited later in the course)

## Connections
- **Proof idea.** At a critical point, second-order [[Multivariable Taylor's Theorem]] (from the 451 [[§31 Taylor's Theorem#^thm-31-2|Taylor's theorem]]) gives f(x₀ + h) − f(x₀) = ½ hᵀHh, with H evaluated at an intermediate point. Continuity of the second partials keeps H definite nearby. In one variable, H is just f″(x₀).
- **Linear algebra.** H is symmetric by [[Schwarz–Clairaut Theorem]], so the [[Real spectral theorem]] (LADR 7.29) diagonalizes it. H is positive definite iff all eigenvalues are positive, negative definite iff all are negative, and indefinite iff there are signs of both kinds. For other tests, see [[§24 Positive Operators#^ladr-7-38|LADR 7.38]] and [[§14 Optimization and Lagrange Multipliers#^rem-14-9|Sylvester's criterion]].
- **Where hypotheses matter.** A semidefinite H is inconclusive. For example, x⁴ + y⁴ (a minimum) and x⁴ − y⁴ (a saddle) both have H = 0 at the origin. Candidates come from [[§14 Optimization and Lagrange Multipliers#^thm-14-1|Fermat's theorem]] (∇f = 0).
- **Local vs. global.** The test is local. Global extrema on a compact set exist ([[Heine–Borel Theorem]], [[Continuous Image of a Compact Space is Compact]]) and are found by comparing values at the candidates and on the boundary ([[§14 Optimization and Lagrange Multipliers#^rem-14-10|The Logical Flow]]).
- **Also in [[Calculus]]:** [[§96 Maximum and Minimum Values#^thm-96-2|Calc Thm. §96.2]] (computational treatment with worked examples).
- **Also in [[Applied Linear Algebra]]:** [[§49★ Quadratic Forms#^thm-49-4|235 Thm. §49.4]] (definiteness of a symmetric matrix from the signs of its eigenvalues, with worked classifications).
