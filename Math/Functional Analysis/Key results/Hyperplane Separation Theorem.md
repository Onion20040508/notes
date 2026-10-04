---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 7.1", "geometric Hahn–Banach", "Lax §3.2, Thm 5"]
tags: [functional-analysis, hub]
---
![[§7 The Hyperplane Separation Theorem#^thm-7-1]]

## Treated in
- [[§7 The Hyperplane Separation Theorem#^thm-7-1|Theorem §7.1: Hyperplane Separation; Geometric Hahn–Banach]], in [[§7 The Hyperplane Separation Theorem]]

## Its proof uses
- [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Definition §2.3: Convex Set]]
- [[§4 Statement and Motivation#^thm-4-2|Theorem §4.2: Hahn–Banach]]
- [[§6 Convex Sets and the Gauge#^def-6-1|Definition §6.1: Interior Point]]
- [[§6 Convex Sets and the Gauge#^def-6-2|Definition §6.2: Gauge]]
- [[§6 Convex Sets and the Gauge#^prop-6-5|Proposition §6.5: Values of the Gauge]]
- [[§6 Convex Sets and the Gauge#^prop-6-6|Proposition §6.6: The Gauge is Positive Homogeneous and Subadditive]]
- [[§6 Convex Sets and the Gauge#^cor-6-8|Corollary §6.8: Convex Sets of Interior Points are Sublevel Sets]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** This is where the functionals and convexity threads meet. Translate so that 0 ∈ K, and set ℓ(a y₀) = a on span{y₀}. Since y₀ ∉ K = {p_K < 1}, we have p_K(y₀) ≥ 1, so ℓ ≤ p_K on the line. The [[Hahn–Banach Theorem]] extends ℓ to L ≤ p_K on X, so L(y₀) = 1 while L < 1 on K. The gauge turns the geometry into an inequality and back ([[§7 The Hyperplane Separation Theorem#^rem-7-2|Remark §7]]).
- **Why the hypotheses.** That every point of K is interior is what makes K exactly {p_K < 1} ([[§6 Convex Sets and the Gauge#^cor-6-8|§6.8]], [[Interior Points via the Gauge]]). Nonemptiness is needed to translate a point of K to 0 ([[§7 The Hyperplane Separation Theorem#^rem-7-1|Remark §7]]). “Interior” is the algebraic notion, tested line by line, so X needs no topology. A metric interior point is interior in this sense ([[§10 Normed Linear Spaces#^prop-10-7|§10.7]]), but not conversely ([[§10 Normed Linear Spaces#^ex-10-2|Ex. §10.2]]). Lax's versions with one interior point, or with two disjoint convex sets, were not covered.
- **Same idea elsewhere.** In ℝⁿ, {a·x = c} is a plane and {a·x < c}, {a·x > c} are its two sides ([[§4 Statement and Motivation#^ex-4-3|Ex. §4.3]]). On a Hilbert space the hyperplane {ℓ = 0} of a nonzero bounded functional has a normal vector, its Riesz representer ([[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-23-4|§23.4]], [[Riesz Representation Theorem (Hilbert spaces)]]).
