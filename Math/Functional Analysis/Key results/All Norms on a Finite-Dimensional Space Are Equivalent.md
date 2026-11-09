---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 14.4", "equivalence of norms"]
tags: [functional-analysis, hub]
---
![[§14 New Normed Spaces from Old#^thm-14-4]]

## Treated in
- [[§14 New Normed Spaces from Old#^thm-14-4|Theorem §14.4: All Norms on a Finite-Dimensional Space are Equivalent]], in [[§14 New Normed Spaces from Old]]

## Its proof uses
- (only definitions)

## Its proof uses (other subjects)
- [[Bolzano–Weierstrass Theorem]] (Single Variable Analysis)

## Used in (Functional Analysis)
- [[§14 New Normed Spaces from Old#^cor-14-5|Corollary §14.5: Finite-Dimensional Normed Spaces are Complete]]
- [[§20 Compactness and the Unit Ball#^ex-20-1|Example §20.1: The Closed Unit Ball in 𝔽ⁿ]]
- [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-1|Proposition §26.1: Linear Functionals on Finite-Dimensional Spaces are Bounded]]
- [[§30 Boundedness and Continuity#^prop-30-7|Proposition §30.7: Linear Maps on Finite-Dimensional Spaces are Bounded]]

## Connections
- **How.** Compare an arbitrary norm with the coordinate norm ‖x‖₁ = Σ|aᵢ|. The bound ‖x‖′ ≤ C‖x‖₁ is pure algebra (the triangle inequality on a basis). The reverse bound comes from minimizing ‖·‖′ on the ‖·‖₁-unit sphere: the sphere is sequentially compact by the [[Bolzano–Weierstrass Theorem]] applied coordinate by coordinate, ‖·‖′ is continuous there by the reverse triangle inequality, and the minimum is positive. This is [[Functional Analysis Problem-Solving Techniques#^rem-t7|Technique 7]].
- **Used for.** Every finite-dimensional normed space is complete ([[§14 New Normed Spaces from Old#^cor-14-5|§14.5]]), so finite-dimensional subspaces are closed ([[§14 New Normed Spaces from Old#^cor-14-6|§14.6]]). That closedness is what lets [[Riesz's Lemma]] run at every step of [[The Unit Ball of an Infinite-Dimensional Space Is Not Compact]]. Completeness of 𝔽ᵏ is the coordinate step of [[ℓᵖ Is a Banach Space]]. The closed unit ball of 𝔽ⁿ is compact in every norm ([[§20 Compactness and the Unit Ball#^ex-20-1|Ex. §20.1]]). It also makes every linear functional on a finite-dimensional space bounded ([[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^rem-26-1|Remark §26]]).
- **Fails without finite dimension.** Compactness of the sphere is the step that fails. On the ℓ¹ sphere, e₁, e₂, … are pairwise at distance 2, and on ℓᵖ the norms ‖·‖ₚ and ‖·‖_q (p < q) are not equivalent: for s_n = e₁ + ⋯ + e_n the ratio of the two norms is n^(1/p − 1/q) → ∞ ([[§18 Minkowski's Inequality and the Spaces ℓᵖ#^prop-18-4|§18.4]](c)). The same set can also be complete under one norm and not under another, as C[a,b] is with ‖·‖∞ and with the L¹ norm, so those two norms are not equivalent ([[§14 New Normed Spaces from Old#^ex-14-1|Ex. §14.1]]).
- **Same idea elsewhere.** The prototype is the comparison of the Euclidean and max distances on ℝⁿ ([[§13 Some Topological Concepts in Metric Spaces#^prop-13-1|451 §13.1]]). In topological language, the two metrics induce the same topology ([[§12 Metric Topology#^thm-12-2|590 §12.2]]).
