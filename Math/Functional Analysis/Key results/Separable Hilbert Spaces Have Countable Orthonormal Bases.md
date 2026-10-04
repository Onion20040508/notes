---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 24.13", "Lax §6.4, Thm 9'"]
tags: [functional-analysis, hub]
---
![[§24 Orthonormal Sets and Bases#^thm-24-13]]

## Treated in
- [[§24 Orthonormal Sets and Bases#^thm-24-13|Theorem §24.13: Separable Hilbert Spaces and Countable Bases]], in [[§24 Orthonormal Sets and Bases]]

## Its proof uses
- [[§22 Projection and Orthogonal Decomposition#^lem-22-1|Lemma §22.1: The Inner Product is Continuous]]
- [[§24 Orthonormal Sets and Bases#^lem-24-1|Lemma §24.1: Pythagoras]]
- [[§24 Orthonormal Sets and Bases#^def-24-2|Definition §24.2: Complete Orthogonal Set]]
- [[§24 Orthonormal Sets and Bases#^def-24-5|Definition §24.5: Separable Space]]
- [[§24 Orthonormal Sets and Bases#^prop-24-6|Proposition §24.6: The Orthonormal Expansion Converges]]
- [[§24 Orthonormal Sets and Bases#^thm-24-8|Theorem §24.8: Characterizations of an Orthonormal Basis]]
- [[§24 Orthonormal Sets and Bases#^lem-24-14|Lemma §24.14: Gram–Schmidt]]
- [[§25 Sequence and Function Spaces#^prop-25-1|Proposition §25.1: ℓ^p is Separable for 1 ≤ p < ∞]]

## Its proof uses (other subjects)
- [[Countable Union of Countable Sets is Countable]] (Measure Theory)

## Used in (Functional Analysis)
- [[§24 Orthonormal Sets and Bases#^thm-24-15|Theorem §24.15: Classification of Separable Hilbert Spaces]]

## Connections
- **How.** (⇒) Finite rational combinations of basis vectors form a countable set, and it is dense: truncate the expansion, then round the finitely many coefficients, as for ℓᵖ ([[§25 Sequence and Function Spaces#^prop-25-1|§25.1]]). (⇐) Thin the dense sequence to a linearly independent one with the same span, and apply Gram–Schmidt ([[§24 Orthonormal Sets and Bases#^lem-24-14|§24.14]]). The result is complete: if x ⊥ every e_j, then x is orthogonal to the dense set, so (x, x) = lim (x, y_(n_k)) = 0 by continuity of the inner product.
- **Same idea elsewhere.** Lemma §24.14 is LADR's [[Gram–Schmidt procedure]] (6.32) run along an infinite sequence; only finite combinations occur, and the limit is taken in the inner product. Separability is the metric notion of 551 ([[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-9|551 Def. §19.9]]) and the topological one of 590 ([[§18 Countability Axioms#^def-18-5|590 Def. §18.5]]). Since L²(ℝⁿ) is separable ([[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-20|551 §19.20]], [[§25 Sequence and Function Spaces#^prop-25-4|§25.4]]), it has a countable orthonormal basis.
- **Stronger.** In a separable space every orthonormal set is countable. Orthonormal vectors are √2 apart, so disjoint balls of radius √2/2 around them each catch their own point of the dense set ([[§32 Position Eigenstates and Continuous Resolutions#^prop-32-1|§32.1]]). Hence every orthonormal basis of L²(ℝⁿ) is countably infinite ([[§32 Position Eigenstates and Continuous Resolutions#^thm-32-2|§32.2]]), and the uncountable family |x⟩ cannot be one.
- **Classification.** The classification of separable Hilbert spaces is [[§24 Orthonormal Sets and Bases#^thm-24-15|§24.15]] (HW5, Problem 2): a countable orthonormal basis gives a unitary map onto $\mathbb{F}^n$ or $\ell^2$.
