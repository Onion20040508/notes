---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 6.1", "Clairaut", "equality of mixed partials"]
tags: [multivariable-analysis, hub]
---
![[§6 Equality of Mixed Partials#^thm-6-1]]

## Treated in
- [[§6 Equality of Mixed Partials#^thm-6-1|Theorem §6.1: Schwarz–Clairaut]], in [[§6 Equality of Mixed Partials]]

## Its proof uses
- [[§2 Open and Closed Sets#^def-2-6|Definition §2.6: Open Set]]
- [[§3 Continuity and Limits of Functions#^def-3-1|Definition §3.1: Continuity]]
- [[§3 Continuity and Limits of Functions#^def-3-2|Definition §3.2: Limit of a Function]]
- [[§5 Partial Derivatives#^def-5-1|Definition §5.1: Partial Derivatives]]

## Its proof uses (other subjects)
- [[Mean Value Theorem]] (Single Variable Analysis)

## Used in (Multivariable Analysis)
- [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-1|Theorem §11.1: Derivatives of F(t)]]
- [[§18 Second-Order Sufficient Conditions#^thm-18-1|Theorem §18.1: Second-Order Sufficient Conditions — Unconstrained]]
- [[§34 Stokes' Theorem in ℝ³#^thm-34-1|Theorem §34.1: Stokes' Theorem]]
- [[§38 The Exterior Derivative#^thm-38-4|Theorem §38.4: d² = 0]]
- [[§39 Closed and Exact Forms#^prop-39-4|Proposition §39.4: d² = 0 Is Clairaut's Theorem in Forms Language]]

## Used in (Differentiable Manifolds)
- [[§46 One-Forms#^prop-46-3|Proposition §46.3: A Necessary Condition for Being a Differential]]

## Connections
- **Proof idea.** The mixed second difference I(h, k) is symmetric in the two directions. Applying the one-variable [[Mean Value Theorem]] twice, in either order, writes it as f_xy at one nearby point and as f_yx at another. Continuity at the point finishes the proof.
- **Where hypotheses matter.** Continuity of the mixed partials is needed. For f = xy(x² − y²)/(x² + y²) with f(0, 0) = 0, both mixed partials exist at the origin, but they are 1 and −1.
- **Linear algebra.** It makes the [[§18 Second-Order Sufficient Conditions#^def-18-1|Hessian]] a symmetric matrix, i.e. the second derivative is a [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-9|symmetric bilinear form]] ([[§39 Closed and Exact Forms#^prop-39-2|§39.2]]). So the [[Real spectral theorem]] (LADR 7.29) applies, which is the basis of the [[Second Derivative Test in Several Variables]].
- **In forms language.** It is equivalent to d² = 0 ([[§39 Closed and Exact Forms#^prop-39-4|§39.4]], [[Exterior Derivative Squares to Zero]]). It is also why the second-derivative terms cancel in the proof of [[Stokes' Theorem in ℝ³]], which therefore needs a C² parametrization.
- **Also in [[Calculus]]:** [[§108 Partial Derivatives#^thm-108-2|Calc Thm. §108.2]] (computational treatment with worked examples).
