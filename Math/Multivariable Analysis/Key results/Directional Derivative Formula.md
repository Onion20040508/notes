---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 7.1", "directional derivative = gradient · u"]
tags: [multivariable-analysis, hub]
---
![[§7 Directional Derivatives#^thm-7-1]]

## Treated in
- [[§7 Directional Derivatives#^thm-7-1|Theorem §7.1: Directional Derivative Formula]], in [[§7 Directional Derivatives]]

## Its proof uses
- [[§6 Differentiability#^def-6-1|Definition §6.1: Differentiability]]
- [[§7 Directional Derivatives#^def-7-1|Definition §7.1: Directional Derivative]]

## Used in (Multivariable Analysis)
- [[§22 The Algebra of Differential Forms#^prop-22-2|Proposition §22.2: d on 0-Forms Gives the Gradient]]
- [[§22 The Algebra of Differential Forms#^prop-22-6|Proposition §22.6: Gradient = Differential = 1-Form]]

## Used in (Differentiable Manifolds)
- [[§30 Submanifolds#^prop-30-8|Proposition §30.8: The Old and New Versions Agree]]

## Connections
- **Proof.** Substitute h = ρ cos α and k = ρ sin α into the definition of [[§6 Differentiability#^def-6-1|differentiability]] and let ρ → 0. The unit-vector form, with the total derivative L = Df, is [[§6 Differentiability#^thm-6-1|Theorem §6.1]].
- **Linear algebra.** D_u f = ∇f · u is the linear functional Df evaluated at u, and ∇f is the vector that represents it ([[Riesz representation theorem]]). By the equality case of the [[Cauchy–Schwarz inequality]], D_u f is largest when u points along ∇f, with maximum |∇f| ([[§7 Directional Derivatives#^rem-7-3|Gradient and Maximum Rate of Change]]).
- **In forms language.** The differential eats a direction and returns this derivative, df(v) = ∇f · v: [[§22 The Algebra of Differential Forms#^prop-22-2|d on 0-Forms Gives the Gradient]] and [[§22 The Algebra of Differential Forms#^prop-22-6|Gradient = Differential = 1-Form]].
- **Later uses.** The normal derivative ∂v/∂n = ∇v · n̂ in [[Green's First Identity]] is this formula with u = n̂. The fact that the gradient is perpendicular to level curves is the geometry behind the [[Method of Lagrange Multipliers]].
- **On manifolds.** D_u f = df(u) survives as df_p(D) = D[f] for every tangent vector D, [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|591 Prop. §27.1]].
- **Also in [[Calculus]]:** [[§95 Directional Derivatives and the Gradient Vector#^thm-95-1|Calc Thm. §95.1]] (computational treatment with worked examples).
