---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 10.3", "equivalence of norms"]
tags: [functional-analysis, hub]
---
![[§10 New Normed Spaces from Old#^thm-10-3]]

## Treated in
- [[§10 New Normed Spaces from Old#^thm-10-3|Theorem §10.3: All Norms on a Finite-Dimensional Space are Equivalent]], in [[§10 New Normed Spaces from Old]]

## Its proof uses
- [[§8 Normed Linear Spaces#^def-8-1|Definition §8.1: Norm; Normed Linear Space]]
- [[§8 Normed Linear Spaces#^lem-8-3|Lemma §8.3: Reverse Triangle Inequality]]
- [[§10 New Normed Spaces from Old#^def-10-1|Definition §10.1: Equivalent Norms]]

## Its proof uses (other subjects)
- [[Bolzano–Weierstrass Theorem]] (Single Variable Analysis)

## Used in (Functional Analysis)
- [[§10 New Normed Spaces from Old#^cor-10-4|Corollary §10.4: Finite-Dimensional Normed Spaces are Complete]]
- [[§15 Compactness and the Unit Ball#^ex-15-1|Example §15.1: The Closed Unit Ball in 𝔽ⁿ]]

## Connections
- **How.** Compare an arbitrary norm with the coordinate norm ‖x‖₁ = Σ|aᵢ|. The bound ‖x‖′ ≤ C‖x‖₁ is pure algebra (the triangle inequality on a basis). The reverse bound comes from minimizing ‖·‖′ on the ‖·‖₁-unit sphere: the sphere is sequentially compact by the [[Bolzano–Weierstrass Theorem]] applied coordinate by coordinate, ‖·‖′ is continuous there by the reverse triangle inequality, and the minimum is positive. This is [[Functional Analysis Problem-Solving Techniques#^rem-t7|Technique 7]].
- **Used for.** Every finite-dimensional normed space is complete ([[§10 New Normed Spaces from Old#^cor-10-4|§10.4]]), so finite-dimensional subspaces are closed ([[§10 New Normed Spaces from Old#^cor-10-5|§10.5]]). That closedness is what lets [[Riesz's Lemma]] run at every step of [[The Unit Ball of an Infinite-Dimensional Space Is Not Compact]]. Completeness of 𝔽ᵏ is the coordinate step of [[ℓᵖ Is a Banach Space]]. The closed unit ball of 𝔽ⁿ is compact in every norm ([[§15 Compactness and the Unit Ball#^ex-15-1|Ex. §15.1]]). It also makes every linear functional on a finite-dimensional space bounded ([[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^rem-19-1|Remark §19]]).
- **Fails without finite dimension.** Compactness of the sphere is the step that fails. On the ℓ¹ sphere, e₁, e₂, … are pairwise at distance 2, and on ℓᵖ the norms ‖·‖ₚ and ‖·‖_q (p < q) are not equivalent: for s_n = e₁ + ⋯ + e_n the ratio of the two norms is n^(1/p − 1/q) → ∞ ([[§13 Minkowski's Inequality and the Spaces ℓᵖ#^prop-13-4|§13.4]](c)). The same set can also be complete under one norm and not under another, as C[a,b] is with ‖·‖∞ and with the L¹ norm, so those two norms are not equivalent ([[§10 New Normed Spaces from Old#^rem-10-1|Remark §10]]).
- **Same idea elsewhere.** The prototype is the comparison of the Euclidean and max distances on ℝⁿ ([[§13 Some Topological Concepts in Metric Spaces#^prop-13-1|451 §13.1]]). In topological language, the two metrics induce the same topology ([[§11 Metric Topology#^thm-11-2|590 §11.2]]).
