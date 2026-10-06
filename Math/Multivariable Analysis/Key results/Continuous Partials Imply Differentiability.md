---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 7.2"]
tags: [multivariable-analysis, hub]
---
![[§7 Differentiability#^thm-7-2]]

## Treated in
- [[§7 Differentiability#^thm-7-2|Theorem §7.2: Continuous Partials Imply Differentiability]], in [[§7 Differentiability]]

## Its proof uses
- [[§2 Open and Closed Sets#^def-2-6|Definition §2.6: Open Set]]
- [[§3 Continuity and Limits of Functions#^def-3-1|Definition §3.1: Continuity]]
- [[§3 Continuity and Limits of Functions#^def-3-4|Definition §3.4: Little-o Notation]]
- [[§5 Partial Derivatives#^def-5-1|Definition §5.1: Partial Derivatives]]
- [[§7 Differentiability#^def-7-1|Definition §7.1: Differentiability]]

## Its proof uses (other subjects)
- [[Mean Value Theorem]] (Single Variable Analysis)
- [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3: Properties of the Absolute Value]]

## Used in (Multivariable Analysis)
- [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-1|Theorem §11.1: Derivatives of F(t)]]
- [[§12 Composition of Functions and the Chain Rule#^thm-12-2|Theorem §12.2: Multivariable Chain Rule]]
- [[§15 The Implicit Function Theorem#^thm-15-1|Theorem §15.1: Implicit Function Theorem]]

## Connections
- **Proof idea.** Go from (x₀, y₀) to (x₀ + h, y₀ + k) in an x-step and a y-step, and apply the one-variable [[Mean Value Theorem]] to each slice. Continuity of f_x and f_y at the point makes the error o(ρ).
- **Where hypotheses matter.** Partials that merely exist are not enough: the [[2xy∕(x²+y²) family|function 2xy/(x² + y²)]] has both partials at the origin but is not differentiable there ([[§7 Differentiability#^ex-7-1|Example §7.1]]).
- **What it produces.** A total derivative, i.e. the linear map (h, k) ↦ f_x h + f_y k ([[§7 Differentiability#^def-7-2|Def. §7.2]]), a linear functional on ℝ² ([[§12 Duality#^ladr-3-108|LADR 3.108]]). Differentiability then gives every directional derivative ([[Directional Derivative Formula]]).
- **Used for.** It is how the course's C¹ hypotheses turn into differentiability: in the [[Implicit Function Theorem]] and in the derivatives of F(t) behind [[Multivariable Taylor's Theorem]] ([[§11 Taylor's Theorem for Multivariable Functions#^thm-11-1|§11.1]]). The [[Multivariable Chain Rule]] (§10.2) assumes the same continuous-partials hypothesis.
- **Also in [[Calculus]]:** [[§109 Tangent Planes and Linear Approximations#^thm-109-2|Calc Thm. §109.2]] (computational treatment with worked examples).
- **Also in [[Complex Variables]]:** [[§23 Sufficient Conditions for Differentiability#^thm-23-1|342 Thm. §23.1]] (continuous partials plus the Cauchy–Riemann equations give complex differentiability; complex-variables version with worked examples).
