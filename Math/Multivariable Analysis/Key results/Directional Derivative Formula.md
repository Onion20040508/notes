---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 9.1", "directional derivative = gradient · u"]
tags: [multivariable-analysis, hub]
---
![[§9 Directional Derivatives#^thm-9-1]]

## Treated in
- [[§9 Directional Derivatives#^thm-9-1|Theorem §9.1: Directional Derivative Formula]], in [[§9 Directional Derivatives]]

## Its proof uses
- [[§7 Differentiability#^def-7-1|Definition §7.1: Differentiability]]
- [[§9 Directional Derivatives#^def-9-1|Definition §9.1: Directional Derivative]]

## Used in (Multivariable Analysis)
- [[§38 The Exterior Derivative#^prop-38-1|Proposition §38.1: d on 0-Forms Gives the Gradient]]
- [[§39 Closed and Exact Forms#^prop-39-1|Proposition §39.1: Gradient = Differential = 1-Form]]

## Used in (Differentiable Manifolds)
- [[§35 Submanifolds#^prop-35-8|Proposition §35.8: The Old and New Versions Agree]]

## Connections
- **Proof.** Substitute h = ρ cos α and k = ρ sin α into the definition of [[§7 Differentiability#^def-7-1|differentiability]] and let ρ → 0. The unit-vector form, with the total derivative L = Df, is [[§7 Differentiability#^thm-7-1|Theorem §7.1]].
- **Linear algebra.** D_u f = ∇f · u is the [[§12 Duality#^ladr-3-108|linear functional]] Df evaluated at u, and ∇f is the vector that represents it ([[Riesz representation theorem]]). By the equality case of the [[Cauchy–Schwarz inequality]], D_u f is largest when u points along ∇f, with maximum |∇f| ([[§9 Directional Derivatives#^rem-9-3|Gradient and Maximum Rate of Change]]).
- **In forms language.** The differential eats a direction and returns this derivative, df(v) = ∇f · v: [[§38 The Exterior Derivative#^prop-38-1|d on 0-Forms Gives the Gradient]] and [[§39 Closed and Exact Forms#^prop-39-1|Gradient = Differential = 1-Form]].
- **Later uses.** The normal derivative ∂v/∂n = ∇v · n̂ in [[Green's First Identity]] is this formula with u = n̂. The fact that the gradient is perpendicular to level curves is the geometry behind the [[Method of Lagrange Multipliers]].
- **On manifolds.** D_u f = df(u) survives as df_p(D) = D[f] for every tangent vector D, [[§32 The Cotangent Space#^prop-32-1|591 Prop. §32.1]].
- **Also in [[Calculus]]:** [[§111 Directional Derivatives and the Gradient Vector#^thm-111-1|Calc Thm. §111.1]] (computational treatment with worked examples).
