---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 22.5", "d² = 0"]
tags: [multivariable-analysis, hub]
---
![[§22 The Algebra of Differential Forms#^thm-22-5]]

## Treated in
- [[§22 The Algebra of Differential Forms#^thm-22-5|Theorem §22.5: d² = 0]], in [[§22 The Algebra of Differential Forms]]

## Its proof uses
- [[§5 Equality of Mixed Partials#^thm-5-1|Theorem §5.1: Schwarz–Clairaut]]
- [[§22 The Algebra of Differential Forms#^def-22-1|Definition §22.1: Wedge Product]]
- [[§22 The Algebra of Differential Forms#^def-22-4|Definition §22.4: Exterior Derivative]]

## Used in (Multivariable Analysis)
- [[§22 The Algebra of Differential Forms#^prop-22-10|Proposition §22.10: Exact ⇒ Closed]]

## Connections
- **Proof.** It suffices to check d(df). The coefficient of dxᵢ∧dxⱼ is a difference of the two mixed partials, which is 0 by [[Schwarz–Clairaut Theorem]]. Conversely, d² = 0 is equivalent to Clairaut and to the symmetry of the second derivative ([[§22 The Algebra of Differential Forms#^prop-22-9|Proposition §22.9]]).
- **Linear algebra.** The second derivative is a symmetric bilinear form. The wedge product keeps only the alternating part, and bilinear forms split into symmetric plus alternating parts ([[§32 Bilinear Forms and Quadratic Forms#^ladr-9-17|LADR 9.17]]), so the result is zero.
- **Classical consequences.** curl(∇f) = 0 and div(curl F) = 0 are the same identity at two rungs of the ladder ([[§22 The Algebra of Differential Forms#^rem-22-5|Classical Consequences]]). Together with [[Stokes' Theorem in ℝ³]], the flux of a curl through a closed surface is zero ([[§20 Stokes' Theorem in ℝ³#^rem-20-4|Special Cases]]).
- **Exact and closed.** It gives [[§22 The Algebra of Differential Forms#^prop-22-10|Exact ⇒ Closed]]. The converse holds on star-shaped domains ([[Poincaré Lemma]]) and fails on ℝ² ∖ {0} ([[§22 The Algebra of Differential Forms#^prop-22-11|A Closed Form That Is Not Exact]]).
