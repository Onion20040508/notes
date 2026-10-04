---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 18.2", "Lax §5.2, Lemma 7"]
tags: [functional-analysis, hub]
---
![[§18 Compactness and the Unit Ball#^lem-18-2]]

## Treated in
- [[§18 Compactness and the Unit Ball#^lem-18-2|Lemma §18.2: Riesz's Lemma]], in [[§18 Compactness and the Unit Ball]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-2|Definition §1.2: Linear Subspace]]
- [[§10 Normed Linear Spaces#^def-10-1|Definition §10.1: Norm; Normed Linear Space]]
- [[§10 Normed Linear Spaces#^def-10-6|Definition §10.6: Closed Subset]]

## Used in (Functional Analysis)
- [[§18 Compactness and the Unit Ball#^cor-18-3|Corollary §18.3: Riesz's Lemma with Any Constant Below One]]
- [[§18 Compactness and the Unit Ball#^thm-18-5|Theorem §18.5: The Unit Ball of an Infinite-Dimensional Space is Not Compact]]

## Connections
- **How.** Pick x₀ ∉ Y. Then d = dist(x₀, Y) > 0 because Y is closed. Since the infimum may not be attained, take y₀ ∈ Y with ‖x₀ − y₀‖ = a < 2d and normalize z = (x₀ − y₀)/a. Since y₀ + ay ∈ Y, ‖z − y‖ ≥ d/a > ½ for every y ∈ Y. Any constant θ < 1 works in place of ½ ([[§18 Compactness and the Unit Ball#^cor-18-3|§18.3]]).
- **Why the hypothesis.** Closedness is used only to get d > 0, and there it is essential. The constant 1 can fail: in {f ∈ C[0,1] : f(0) = 0} with the sup norm, the subspace {∫f = 0} is closed, yet every unit vector lies at distance < 1 from it ([[§18 Compactness and the Unit Ball#^prop-18-4|§18.4]]). The distance d is the [[Quotient Norm]] of [x₀] in X/Y, positive for the same reason.
- **Used for.** By induction it builds a ½-separated sequence on the unit sphere of any infinite-dimensional normed space: [[The Unit Ball of an Infinite-Dimensional Space Is Not Compact]].
- **Same idea elsewhere.** It is the normed-space substitute for a unit normal vector. In a Hilbert space the [[Orthogonal Decomposition Theorem]] gives a unit z ⊥ Y with ‖z − y‖² = 1 + ‖y‖² ≥ 1, so the constant 1 is attained ([[§18 Compactness and the Unit Ball#^rem-18-2|Remark §18]], [[§22 Projection and Orthogonal Decomposition#^rem-22-6|Remark §22]]).
