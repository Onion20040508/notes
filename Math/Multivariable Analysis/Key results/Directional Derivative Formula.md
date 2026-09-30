---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 7.1", "directional derivative = gradient · u"]
tags: [multivariable-analysis, hub]
---
![[Multivariable Analysis §7 Directional Derivatives#^thm-7-1]]

## Treated in
- [[Multivariable Analysis §7 Directional Derivatives#^thm-7-1|Theorem §7.1: Directional Derivative Formula]], in [[Multivariable Analysis §7 Directional Derivatives]]

## Its proof uses
- [[Multivariable Analysis §6 Differentiability#^def-6-1|Definition §6.1: Differentiability]]
- [[Multivariable Analysis §7 Directional Derivatives#^def-7-1|Definition §7.1: Directional Derivative]]

## Used in (Multivariable Analysis)
- [[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-2|Proposition §22.2: d on 0-Forms Gives the Gradient]]
- [[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-6|Proposition §22.6: Gradient = Differential = 1-Form]]

## Connections
- **Proof.** Substitute h = ρ cos α and k = ρ sin α into the definition of [[Multivariable Analysis §6 Differentiability#^def-6-1|differentiability]] and let ρ → 0. The unit-vector form, with the total derivative L = Df, is [[Multivariable Analysis §6 Differentiability#^thm-6-1|Theorem §6.1]].
- **Linear algebra.** D_u f = ∇f · u is the linear functional Df evaluated at u, and ∇f is the vector that represents it ([[Riesz representation theorem]]). By the equality case of the [[Cauchy–Schwarz inequality]], D_u f is largest when u points along ∇f, with maximum |∇f| ([[Multivariable Analysis §7 Directional Derivatives#^rem-7-3|Gradient and Maximum Rate of Change]]).
- **In forms language.** The differential eats a direction and returns this derivative, df(v) = ∇f · v: [[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-2|d on 0-Forms Gives the Gradient]] and [[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-6|Gradient = Differential = 1-Form]].
- **Later uses.** The normal derivative ∂v/∂n = ∇v · n̂ in [[Green's First Identity]] is this formula with u = n̂. The fact that the gradient is perpendicular to level curves is the geometry behind the [[Method of Lagrange Multipliers]].
