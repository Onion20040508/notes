---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 14.4", "Hessian test"]
tags: [multivariable-analysis, hub]
---
![[Multivariable Analysis §14 Optimization and Lagrange Multipliers#^thm-14-4]]

## Treated in
- [[Multivariable Analysis §14 Optimization and Lagrange Multipliers#^thm-14-4|Theorem §14.4: Second-Order Sufficient Conditions — Unconstrained]], in [[Multivariable Analysis §14 Optimization and Lagrange Multipliers]]

## Its proof uses
- [[Multivariable Analysis §5 Equality of Mixed Partials#^thm-5-1|Theorem §5.1: Schwarz–Clairaut]]
- [[Multivariable Analysis §9 Taylor's Theorem for Multivariable Functions#^thm-9-1|Theorem §9.1: Derivatives of F(t)]]
- [[Multivariable Analysis §9 Taylor's Theorem for Multivariable Functions#^thm-9-2|Theorem §9.2: Multivariable Taylor's Theorem]]
- [[Multivariable Analysis §14 Optimization and Lagrange Multipliers#^def-14-1|Definition §14.1: Local Maximum/Minimum]]
- [[Multivariable Analysis §14 Optimization and Lagrange Multipliers#^def-14-3|Definition §14.3: Positive/Negative Definite]]

## Its proof uses (other subjects)
- [[Real spectral theorem]] (Linear Algebra)
- [[Single Variable Analysis §31 Taylor's Theorem#^thm-31-2|451 §31.2: Taylor's Theorem with Lagrange Remainder]]

## Used in (Multivariable Analysis)
- (not cited later in the course)

## Connections
- **Proof idea.** At a critical point, second-order [[Multivariable Taylor's Theorem]] (from the 451 [[Single Variable Analysis §31 Taylor's Theorem#^thm-31-2|Taylor's theorem]]) gives f(x₀ + h) − f(x₀) = ½ hᵀHh, with H evaluated at an intermediate point. Continuity of the second partials keeps H definite nearby. In one variable, H is just f″(x₀).
- **Linear algebra.** H is symmetric by [[Schwarz–Clairaut Theorem]], so the [[Real spectral theorem]] (LADR 7.29) diagonalizes it. H is positive definite iff all eigenvalues are positive, negative definite iff all are negative, and indefinite iff there are signs of both kinds. For other tests, see [[Linear Algebra 7C Positive Operators#^ladr-7-38|LADR 7.38]] and [[Multivariable Analysis §14 Optimization and Lagrange Multipliers#^rem-14-9|Sylvester's criterion]].
- **Where hypotheses matter.** A semidefinite H is inconclusive. For example, x⁴ + y⁴ (a minimum) and x⁴ − y⁴ (a saddle) both have H = 0 at the origin. Candidates come from [[Multivariable Analysis §14 Optimization and Lagrange Multipliers#^thm-14-1|Fermat's theorem]] (∇f = 0).
- **Local vs. global.** The test is local. Global extrema on a compact set exist ([[Heine–Borel Theorem]], [[Continuous Image of a Compact Space is Compact]]) and are found by comparing values at the candidates and on the boundary ([[Multivariable Analysis §14 Optimization and Lagrange Multipliers#^rem-14-10|The Logical Flow]]).
