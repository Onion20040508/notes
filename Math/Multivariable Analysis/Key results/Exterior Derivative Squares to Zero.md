---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 38.4", "d² = 0"]
tags: [multivariable-analysis, hub]
---
![[§38 The Exterior Derivative#^thm-38-4]]

## Treated in
- [[§38 The Exterior Derivative#^thm-38-4|Theorem §38.4: d² = 0]], in [[§38 The Exterior Derivative]]

## Its proof uses
- [[§6 Equality of Mixed Partials#^thm-6-1|Theorem §6.1: Schwarz–Clairaut]]
- [[§37 The Algebra of Differential Forms#^def-37-1|Definition §37.1: Wedge Product]]
- [[§38 The Exterior Derivative#^def-38-1|Definition §38.1: Exterior Derivative]]

## Used in (Multivariable Analysis)
- [[§39 Closed and Exact Forms#^prop-39-5|Proposition §39.5: Exact ⇒ Closed]]

## Connections
- **Proof.** It suffices to check d(df). The coefficient of dxᵢ∧dxⱼ is a difference of the two mixed partials, which is 0 by [[Schwarz–Clairaut Theorem]]. Conversely, d² = 0 is equivalent to Clairaut and to the symmetry of the second derivative ([[§39 Closed and Exact Forms#^prop-39-4|Proposition §39.4]]).
- **Linear algebra.** The second derivative is a symmetric bilinear form. The wedge product keeps only the alternating part, and bilinear forms split into symmetric plus alternating parts ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-17|LADR 9.17]]), so the result is zero.
- **Classical consequences.** curl(∇f) = 0 and div(curl F) = 0 are the same identity at two rungs of the ladder ([[§38 The Exterior Derivative#^rem-38-5|Classical Consequences]]). Together with [[Stokes' Theorem in ℝ³]], the flux of a curl through a closed surface is zero ([[§34 Stokes' Theorem in ℝ³#^rem-34-4|Special Cases]]).
- **Exact and closed.** It gives [[§39 Closed and Exact Forms#^prop-39-5|Exact ⇒ Closed]]. The converse holds on star-shaped domains ([[Poincaré Lemma]]) and fails on ℝ² ∖ {0} ([[§39 Closed and Exact Forms#^prop-39-6|A Closed Form That Is Not Exact]]).
