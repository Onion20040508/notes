---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 5.1", "Clairaut", "equality of mixed partials"]
tags: [multivariable-analysis, hub]
---
![[Multivariable Analysis §5 Equality of Mixed Partials#^thm-5-1]]

## Treated in
- [[Multivariable Analysis §5 Equality of Mixed Partials#^thm-5-1|Theorem §5.1: Schwarz–Clairaut]], in [[Multivariable Analysis §5 Equality of Mixed Partials]]

## Its proof uses
- [[Multivariable Analysis §2 Open and Closed Sets#^def-2-4|Definition §2.4: Open and Closed Sets]]
- [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-1|Definition §3.1: Continuity]]
- [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-2|Definition §3.2: Limit of a Function]]
- [[Multivariable Analysis §4 Partial Derivatives#^def-4-1|Definition §4.1: Partial Derivatives]]

## Its proof uses (other subjects)
- [[Mean Value Theorem]] (Single Variable Analysis)

## Used in (Multivariable Analysis)
- [[Multivariable Analysis §8 The Differential#^def-8-2|Definition §8.2: Second Differential]]
- [[Multivariable Analysis §9 Taylor's Theorem for Multivariable Functions#^thm-9-1|Theorem §9.1: Derivatives of F(t)]]
- [[Multivariable Analysis §14 Optimization and Lagrange Multipliers#^def-14-2|Definition §14.2: Hessian Matrix]]
- [[Multivariable Analysis §14 Optimization and Lagrange Multipliers#^thm-14-4|Theorem §14.4: Second-Order Sufficient Conditions — Unconstrained]]
- [[Multivariable Analysis §20 Stokes' Theorem in ℝ³#^thm-20-1|Theorem §20.1: Stokes' Theorem]]
- [[Multivariable Analysis §22 The Algebra of Differential Forms#^thm-22-5|Theorem §22.5: d² = 0]]
- [[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-9|Proposition §22.9: d² = 0 Is Clairaut's Theorem in Forms Language]]

## Connections
- **Proof idea.** The mixed second difference I(h, k) is symmetric in the two directions. Applying the one-variable [[Mean Value Theorem]] twice, in either order, writes it as f_xy at one nearby point and as f_yx at another. Continuity at the point finishes the proof.
- **Where hypotheses matter.** Continuity of the mixed partials is needed. For f = xy(x² − y²)/(x² + y²) with f(0, 0) = 0, both mixed partials exist at the origin, but they are 1 and −1.
- **Linear algebra.** It makes the [[Multivariable Analysis §14 Optimization and Lagrange Multipliers#^def-14-2|Hessian]] a symmetric matrix, i.e. the second derivative is a symmetric bilinear form ([[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-7|§22.7]]). So the [[Real spectral theorem]] (LADR 7.29) applies, which is the basis of the [[Second Derivative Test in Several Variables]].
- **In forms language.** It is equivalent to d² = 0 ([[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-9|§22.9]], [[Exterior Derivative Squares to Zero]]). It is also why the second-derivative terms cancel in the proof of [[Stokes' Theorem in ℝ³]], which therefore needs a C² parametrization.
