---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 12.8", "Lax §5.1, Thm 1"]
tags: [functional-analysis, hub]
---
![[§14 New Normed Spaces from Old#^thm-14-8]]

## Treated in
- [[§14 New Normed Spaces from Old#^thm-14-8|Theorem §14.8: Quotient Norm]], in [[§14 New Normed Spaces from Old]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-2|Definition §1.2: Linear Subspace]]
- [[§2 Quotient Spaces and Complements#^prop-2-1|Proposition §2.1: X/Y is a Linear Space]]
- [[§2 Quotient Spaces and Complements#^def-2-2|Definition §2.2: Equivalence Class and Quotient Space]]
- [[§11 Normed Linear Spaces#^def-11-1|Definition §11.1: Norm; Normed Linear Space]]
- [[§11 Normed Linear Spaces#^def-11-6|Definition §11.6: Closed Subset]]

## Its proof uses (other subjects)
- [[Characterization of the Supremum]] (Single Variable Analysis)

## Used in (Functional Analysis)
- [[§14 New Normed Spaces from Old#^prop-14-9|Proposition §14.9: The Quotient Seminorm; Closedness is Necessary]]

## Connections
- **How.** ‖[x]‖ is the infimum of the norms in the coset, i.e. the distance from 0 to the translate x + Y. Homogeneity follows by substituting y = ay′. Subadditivity uses ε-near minimizers in [x] and [y] ([[Characterization of the Supremum]]). Positivity is where closedness enters: if ‖[x]‖ = 0, then elements of Y converge to −x.
- **Why closed.** For any subspace the formula is a seminorm, and it is a norm iff Y is closed ([[§14 New Normed Spaces from Old#^prop-14-9|§14.9]]). For example, c₀₀ is not closed in ℓᵖ (1 ≤ p < ∞), because truncations converge ([[§14 New Normed Spaces from Old#^rem-14-3|Remark §14]]). This is the same closedness that makes dist(x₀, Y) > 0 in [[Riesz's Lemma]]; that distance is exactly ‖[x₀]‖.
- **Same idea elsewhere.** The underlying linear space is the algebraic quotient ([[§2 Quotient Spaces and Complements#^prop-2-1|§2.1]]; [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-103|LADR 3.103]]). In 551, total variation ([[§28 Differentiation Theory#^def-28-2|551 Def. §28.2]]) is only a seminorm on BV ([[§28 Differentiation Theory#^def-28-3|551 Def. §28.3]]) and becomes a norm on BV modulo constants ([[§34 Normed Linear Spaces and Lᵖ Spaces#^ex-34-3|551 Ex. §34.3]]).
- **With an inner product.** The infimum is attained at the foot of the perpendicular ([[Closest Point in a Closed Convex Set]]), and X/Y ≅ Y⊥ ([[Orthogonal Decomposition Theorem]], [[§2 Quotient Spaces and Complements#^cor-2-8|§2.8]]). In a general normed space there is no perpendicular, and the infimum need not be attained.
