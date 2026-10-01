---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 6.1", "geometric Hahn–Banach", "Lax §3.2, Thm 5"]
tags: [functional-analysis, hub]
---
![[§6 The Hyperplane Separation Theorem#^thm-6-1]]

## Treated in
- [[§6 The Hyperplane Separation Theorem#^thm-6-1|Theorem §6.1: Hyperplane Separation; Geometric Hahn–Banach]], in [[§6 The Hyperplane Separation Theorem]]

## Its proof uses
- [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Definition §2.3: Convex Set]]
- [[§3 Statement and Motivation#^def-3-2|Definition §3.2: Hyperplane; Half-Space]]
- [[§3 Statement and Motivation#^thm-3-2|Theorem §3.2: Hahn–Banach]]
- [[§4 Proof of the Hahn–Banach Theorem#^ex-4-1|Example §4.1: Extending from a Line]]
- [[§5 Convex Sets and the Gauge#^def-5-1|Definition §5.1: Interior Point]]
- [[§5 Convex Sets and the Gauge#^def-5-2|Definition §5.2: Gauge]]
- [[§5 Convex Sets and the Gauge#^prop-5-5|Proposition §5.5: Values of the Gauge]]
- [[§5 Convex Sets and the Gauge#^prop-5-6|Proposition §5.6: The Gauge is Positive Homogeneous and Subadditive]]
- [[§5 Convex Sets and the Gauge#^cor-5-8|Corollary §5.8: Convex Sets of Interior Points are Sublevel Sets]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** This is where the functionals and convexity threads meet. Translate so that 0 ∈ K, and set ℓ(a y₀) = a on span{y₀}. Since y₀ ∉ K = {p_K < 1}, we have p_K(y₀) ≥ 1, so ℓ ≤ p_K on the line. The [[Hahn–Banach Theorem]] extends ℓ to L ≤ p_K on X, so L(y₀) = 1 while L < 1 on K. The gauge turns the geometry into an inequality and back ([[§6 The Hyperplane Separation Theorem#^rem-6-2|Remark §6]]).
- **Why the hypotheses.** That every point of K is interior is what makes K exactly {p_K < 1} ([[§5 Convex Sets and the Gauge#^cor-5-8|§5.8]], [[Interior Points via the Gauge]]). Nonemptiness is needed to translate a point of K to 0 ([[§6 The Hyperplane Separation Theorem#^rem-6-1|Remark §6]]). “Interior” is the algebraic notion, tested line by line, so X needs no topology. A metric interior point is interior in this sense ([[§8 Normed Linear Spaces#^prop-8-7|§8.7]]), but not conversely ([[§8 Normed Linear Spaces#^ex-8-2|Ex. §8.2]]). Lax's versions with one interior point, or with two disjoint convex sets, were not covered.
- **Same idea elsewhere.** In ℝⁿ, {a·x = c} is a plane and {a·x < c}, {a·x > c} are its two sides ([[§3 Statement and Motivation#^ex-3-3|Ex. §3.3]]). On a Hilbert space the hyperplane {ℓ = 0} of a nonzero bounded functional has a normal vector, its Riesz representer ([[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-19-4|§19.4]], [[Riesz Representation Theorem (Hilbert spaces)]]).
