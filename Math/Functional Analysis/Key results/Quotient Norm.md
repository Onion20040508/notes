---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 10.8", "Lax §5.1, Thm 1"]
tags: [functional-analysis, hub]
---
![[§10 New Normed Spaces from Old#^thm-10-8]]

## Treated in
- [[§10 New Normed Spaces from Old#^thm-10-8|Theorem §10.8: Quotient Norm]], in [[§10 New Normed Spaces from Old]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-2|Definition §1.2: Linear Subspace]]
- [[§1 Linear Spaces#^prop-1-6|Proposition §1.6: X/Y is a Linear Space]]
- [[§1 Linear Spaces#^def-1-7|Definition §1.7: Equivalence Class and Quotient Space]]
- [[§8 Normed Linear Spaces#^def-8-1|Definition §8.1: Norm; Normed Linear Space]]
- [[§8 Normed Linear Spaces#^def-8-6|Definition §8.6: Closed Subset]]

## Its proof uses (other subjects)
- [[Characterization of the Supremum]] (Single Variable Analysis)

## Used in (Functional Analysis)
- [[§10 New Normed Spaces from Old#^prop-10-9|Proposition §10.9: The Quotient Seminorm; Closedness is Necessary]]

## Connections
- **How.** ‖[x]‖ is the infimum of the norms in the coset, i.e. the distance from 0 to the translate x + Y. Homogeneity follows by substituting y = ay′. Subadditivity uses ε-near minimizers in [x] and [y] ([[Characterization of the Supremum]]). Positivity is where closedness enters: if ‖[x]‖ = 0, then elements of Y converge to −x.
- **Why closed.** For any subspace the formula is a seminorm, and it is a norm iff Y is closed ([[§10 New Normed Spaces from Old#^prop-10-9|§10.9]]). For example, c₀₀ is not closed in ℓᵖ (1 ≤ p < ∞), because truncations converge ([[§10 New Normed Spaces from Old#^rem-10-3|Remark §10]]). This is the same closedness that makes dist(x₀, Y) > 0 in [[Riesz's Lemma]]; that distance is exactly ‖[x₀]‖.
- **Same idea elsewhere.** The underlying linear space is the algebraic quotient ([[§1 Linear Spaces#^prop-1-6|§1.6]]; [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-103|LADR 3.103]]). In 551, total variation is only a seminorm on BV and becomes a norm on BV modulo constants ([[§19 Normed Linear Spaces and Lᵖ Spaces#^ex-19-3|551 Ex. §19.3]]).
- **With an inner product.** The infimum is attained at the foot of the perpendicular ([[Closest Point in a Closed Convex Set]]), and X/Y ≅ Y⊥ ([[Orthogonal Decomposition Theorem]], [[§1 Linear Spaces#^cor-1-13|§1.13]]). In a general normed space there is no perpendicular, and the infimum need not be attained.
