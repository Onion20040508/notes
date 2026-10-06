---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 12.8", "Lax §5.1, Thm 1"]
tags: [functional-analysis, hub]
---
![[§12 New Normed Spaces from Old#^thm-12-8]]

## Treated in
- [[§12 New Normed Spaces from Old#^thm-12-8|Theorem §12.8: Quotient Norm]], in [[§12 New Normed Spaces from Old]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-2|Definition §1.2: Linear Subspace]]
- [[§1 Linear Spaces#^prop-1-6|Proposition §1.6: X/Y is a Linear Space]]
- [[§1 Linear Spaces#^def-1-7|Definition §1.7: Equivalence Class and Quotient Space]]
- [[§10 Normed Linear Spaces#^def-10-1|Definition §10.1: Norm; Normed Linear Space]]
- [[§10 Normed Linear Spaces#^def-10-6|Definition §10.6: Closed Subset]]

## Its proof uses (other subjects)
- [[Characterization of the Supremum]] (Single Variable Analysis)

## Used in (Functional Analysis)
- [[§12 New Normed Spaces from Old#^prop-12-9|Proposition §12.9: The Quotient Seminorm; Closedness is Necessary]]

## Connections
- **How.** ‖[x]‖ is the infimum of the norms in the coset, i.e. the distance from 0 to the translate x + Y. Homogeneity follows by substituting y = ay′. Subadditivity uses ε-near minimizers in [x] and [y] ([[Characterization of the Supremum]]). Positivity is where closedness enters: if ‖[x]‖ = 0, then elements of Y converge to −x.
- **Why closed.** For any subspace the formula is a seminorm, and it is a norm iff Y is closed ([[§12 New Normed Spaces from Old#^prop-12-9|§12.9]]). For example, c₀₀ is not closed in ℓᵖ (1 ≤ p < ∞), because truncations converge ([[§12 New Normed Spaces from Old#^rem-12-3|Remark §12]]). This is the same closedness that makes dist(x₀, Y) > 0 in [[Riesz's Lemma]]; that distance is exactly ‖[x₀]‖.
- **Same idea elsewhere.** The underlying linear space is the algebraic quotient ([[§1 Linear Spaces#^prop-1-6|§1.6]]; [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-103|LADR 3.103]]). In 551, total variation ([[§18 Differentiation Theory#^def-18-2|551 Def. §18.2]]) is only a seminorm on BV and becomes a norm on BV modulo constants ([[§19 Normed Linear Spaces and Lᵖ Spaces#^ex-19-3|551 Ex. §19.3]]).
- **With an inner product.** The infimum is attained at the foot of the perpendicular ([[Closest Point in a Closed Convex Set]]), and X/Y ≅ Y⊥ ([[Orthogonal Decomposition Theorem]], [[§1 Linear Spaces#^cor-1-13|§1.13]]). In a general normed space there is no perpendicular, and the infimum need not be attained.
