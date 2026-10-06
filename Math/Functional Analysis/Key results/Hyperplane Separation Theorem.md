---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 8.1", "geometric Hahn–Banach", "Lax §3.2, Thm 5"]
tags: [functional-analysis, hub]
---
![[§8 The Hyperplane Separation Theorem#^thm-8-1]]

## Treated in
- [[§8 The Hyperplane Separation Theorem#^thm-8-1|Theorem §8.1: Hyperplane Separation; Geometric Hahn–Banach]], in [[§8 The Hyperplane Separation Theorem]]

## Its proof uses
- [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-3|Definition §3.3: Convex Set]]
- [[§5 Statement and Motivation#^thm-5-2|Theorem §5.2: Hahn–Banach]]
- [[§7 Convex Sets and the Gauge#^def-7-1|Definition §7.1: Interior Point]]
- [[§7 Convex Sets and the Gauge#^def-7-2|Definition §7.2: Gauge]]
- [[§7 Convex Sets and the Gauge#^prop-7-5|Proposition §7.5: Values of the Gauge]]
- [[§7 Convex Sets and the Gauge#^prop-7-6|Proposition §7.6: The Gauge is Positive Homogeneous and Subadditive]]
- [[§7 Convex Sets and the Gauge#^cor-7-8|Corollary §7.8: Convex Sets of Interior Points are Sublevel Sets]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** This is where the functionals and convexity threads meet. Translate so that 0 ∈ K, and set ℓ(a y₀) = a on span{y₀}. Since y₀ ∉ K = {p_K < 1}, we have p_K(y₀) ≥ 1, so ℓ ≤ p_K on the line. The [[Hahn–Banach Theorem]] extends ℓ to L ≤ p_K on X, so L(y₀) = 1 while L < 1 on K. The gauge turns the geometry into an inequality and back ([[§8 The Hyperplane Separation Theorem#^rem-8-1|Remark §8]]).
- **Why the hypotheses.** That every point of K is interior is what makes K exactly {p_K < 1} ([[§7 Convex Sets and the Gauge#^cor-7-8|§7.8]], [[Interior Points via the Gauge]]). Nonemptiness is needed to translate a point of K to 0 ([[§8 The Hyperplane Separation Theorem#^rem-8-2|Remark §8]]). “Interior” is the algebraic notion, tested line by line, so X needs no topology. A metric interior point is interior in this sense ([[§11 Normed Linear Spaces#^prop-11-7|§11.7]]), but not conversely ([[§11 Normed Linear Spaces#^ex-11-2|Ex. §11.2]]). Lax's versions with one interior point, or with two disjoint convex sets, were not covered.
- **Same idea elsewhere.** In ℝⁿ, {a·x = c} is a plane and {a·x < c}, {a·x > c} are its two sides ([[§5 Statement and Motivation#^ex-5-3|Ex. §5.3]]). On a Hilbert space the hyperplane {ℓ = 0} of a nonzero bounded functional has a normal vector, its Riesz representer ([[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-3|§26.3]], [[Riesz Representation Theorem (Hilbert spaces)]]).
