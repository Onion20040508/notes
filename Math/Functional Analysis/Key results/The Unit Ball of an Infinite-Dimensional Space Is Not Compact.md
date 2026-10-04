---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 18.5", "Lax §5.2, Thm 6"]
tags: [functional-analysis, hub]
---
![[§18 Compactness and the Unit Ball#^thm-18-5]]

## Treated in
- [[§18 Compactness and the Unit Ball#^thm-18-5|Theorem §18.5: The Unit Ball of an Infinite-Dimensional Space is Not Compact]], in [[§18 Compactness and the Unit Ball]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-5|Definition §1.5: Linear Span]]
- [[§10 Normed Linear Spaces#^prop-10-5|Proposition §10.5: Limits are Unique; Convergent Sequences are Cauchy]]
- [[§12 New Normed Spaces from Old#^cor-12-5|Corollary §12.5: Finite-Dimensional Subspaces are Closed]]
- [[§18 Compactness and the Unit Ball#^def-18-1|Definition §18.1: Sequentially Compact]]
- [[§18 Compactness and the Unit Ball#^lem-18-2|Lemma §18.2: Riesz's Lemma]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** The proof is an induction with [[Riesz's Lemma]]. Y_m = span{x₁, …, x_m} is closed, being finite-dimensional ([[§12 New Normed Spaces from Old#^cor-12-5|§12.5]]), and proper, because X is infinite-dimensional. So there is a unit vector x_(m+1) at distance ≥ ½ from Y_m. The resulting sequence has mutual distances ≥ ½ and no Cauchy subsequence. Infinite dimension is used exactly once, to know that Y_m is proper ([[§18 Compactness and the Unit Ball#^rem-18-3|Remark §18]]).
- **Finite dimensions.** The closed unit ball of 𝔽ⁿ is compact in any norm ([[§18 Compactness and the Unit Ball#^ex-18-1|Ex. §18.1]]), by the [[Bolzano–Weierstrass Theorem]] coordinatewise. That is the compactness behind [[All Norms on a Finite-Dimensional Space Are Equivalent]]; in ℝⁿ, the [[Heine–Borel Theorem]] makes closed bounded sets compact. So compactness of the closed unit ball characterizes finite dimension. In ℓᵖ (p < ∞) the separated sequence is explicit: the eₙ are 2^(1/p) apart ([[§18 Compactness and the Unit Ball#^ex-18-2|Ex. §18.2]]).
- **Why it matters.** In infinite dimensions a bounded sequence need not have a convergent subsequence, so a solution can no longer be produced as a limit of approximations by compactness. The course's response is weak convergence ([[§18 Compactness and the Unit Ball#^rem-18-4|Remark §18]]). In metric spaces sequential and open-cover compactness agree ([[§16 Limit Point Compactness#^thm-16-2|590 §16.2]]), so the ball fails both.
