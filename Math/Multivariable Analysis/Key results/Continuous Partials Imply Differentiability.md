---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 6.2"]
tags: [multivariable-analysis, hub]
---
![[§6 Differentiability#^thm-6-2]]

## Treated in
- [[§6 Differentiability#^thm-6-2|Theorem §6.2: Continuous Partials Imply Differentiability]], in [[§6 Differentiability]]

## Its proof uses
- [[§2 Open and Closed Sets#^def-2-4|Definition §2.4: Open and Closed Sets]]
- [[§3 Continuity and Limits of Functions#^def-3-1|Definition §3.1: Continuity]]
- [[§3 Continuity and Limits of Functions#^def-3-3|Definition §3.3: Big-O and Little-o Notation]]
- [[§4 Partial Derivatives#^def-4-1|Definition §4.1: Partial Derivatives]]
- [[§6 Differentiability#^def-6-1|Definition §6.1: Differentiability]]

## Its proof uses (other subjects)
- [[Mean Value Theorem]] (Single Variable Analysis)
- [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3: Properties of the Absolute Value]]

## Used in (Multivariable Analysis)
- [[§9 Taylor's Theorem for Multivariable Functions#^thm-9-1|Theorem §9.1: Derivatives of F(t)]]
- [[§10 Composition of Functions and the Chain Rule#^thm-10-2|Theorem §10.2: Multivariable Chain Rule]]
- [[§12 The Implicit Function Theorem#^thm-12-1|Theorem §12.1: Implicit Function Theorem]]

## Connections
- **Proof idea.** Go from (x₀, y₀) to (x₀ + h, y₀ + k) in an x-step and a y-step, and apply the one-variable [[Mean Value Theorem]] to each slice. Continuity of f_x and f_y at the point makes the error o(ρ).
- **Where hypotheses matter.** Partials that merely exist are not enough: the [[2xy∕(x²+y²) family|function 2xy/(x² + y²)]] has both partials at the origin but is not differentiable there ([[§6 Differentiability#^ex-6-1|Example §6.1]]).
- **What it produces.** A total derivative, i.e. the linear map (h, k) ↦ f_x h + f_y k ([[§6 Differentiability#^def-6-2|Def. §6.2]]), a linear functional on ℝ² ([[3F Duality#^ladr-3-108|LADR 3.108]]). Differentiability then gives every directional derivative ([[Directional Derivative Formula]]).
- **Used for.** It is how the course's C¹ hypotheses turn into differentiability: in the [[Implicit Function Theorem]] and in the derivatives of F(t) behind [[Multivariable Taylor's Theorem]] ([[§9 Taylor's Theorem for Multivariable Functions#^thm-9-1|§9.1]]). The [[Multivariable Chain Rule]] (§10.2) assumes the same continuous-partials hypothesis.
