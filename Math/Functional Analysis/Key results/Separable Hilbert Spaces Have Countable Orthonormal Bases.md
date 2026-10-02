---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 20.18", "Lax §6.4, Thm 9'"]
tags: [functional-analysis, hub]
---
![[§20 Orthonormal Sets and Bases#^thm-20-18]]

## Treated in
- [[§20 Orthonormal Sets and Bases#^thm-20-18|Theorem §20.18: Separable Hilbert Spaces and Countable Bases]], in [[§20 Orthonormal Sets and Bases]]

## Its proof uses
- [[§18 Projection and Orthogonal Decomposition#^lem-18-1|Lemma §18.1: The Inner Product is Continuous]]
- [[§20 Orthonormal Sets and Bases#^lem-20-1|Lemma §20.1: Pythagoras]]
- [[§20 Orthonormal Sets and Bases#^def-20-2|Definition §20.2: Complete Orthogonal Set]]
- [[§20 Orthonormal Sets and Bases#^def-20-5|Definition §20.5: Separable Space]]
- [[§20 Orthonormal Sets and Bases#^prop-20-6|Proposition §20.6: The Orthonormal Expansion Converges]]
- [[§20 Orthonormal Sets and Bases#^thm-20-8|Theorem §20.8: Characterizations of an Orthonormal Basis]]
- [[§20 Orthonormal Sets and Bases#^prop-20-13|Proposition §20.13: ℓ^p is Separable for 1 ≤ p < ∞]]
- [[§20 Orthonormal Sets and Bases#^lem-20-19|Lemma §20.19: Gram–Schmidt]]

## Its proof uses (other subjects)
- [[Countable Union of Countable Sets is Countable]] (Measure Theory)

## Used in (Functional Analysis)
- [[§20 Orthonormal Sets and Bases#^thm-20-20|Theorem §20.20: Classification of Separable Hilbert Spaces]]

## Connections
- **How.** (⇒) Finite rational combinations of basis vectors form a countable set, and it is dense: truncate the expansion, then round the finitely many coefficients, as for ℓᵖ ([[§20 Orthonormal Sets and Bases#^prop-20-13|§20.13]]). (⇐) Thin the dense sequence to a linearly independent one with the same span, and apply Gram–Schmidt ([[§20 Orthonormal Sets and Bases#^lem-20-19|§20.19]]). The result is complete: if x ⊥ every e_j, then x is orthogonal to the dense set, so (x, x) = lim (x, y_(n_k)) = 0 by continuity of the inner product.
- **Same idea elsewhere.** Lemma §20.19 is LADR's [[Gram–Schmidt procedure]] (6.32) run along an infinite sequence; only finite combinations occur, and the limit is taken in the inner product. Separability is the metric notion of 551 ([[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-9|551 Def. §19.9]]) and the topological one of 590 ([[§18 Countability Axioms#^def-18-5|590 Def. §18.5]]). Since L²(ℝⁿ) is separable ([[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-20|551 §19.20]], [[§20 Orthonormal Sets and Bases#^prop-20-16|§20.16]]), it has a countable orthonormal basis.
- **Stronger.** In a separable space every orthonormal set is countable. Orthonormal vectors are √2 apart, so disjoint balls of radius √2/2 around them each catch their own point of the dense set ([[§26 Position Eigenstates and Continuous Resolutions#^prop-26-1|§26.1]]). Hence every orthonormal basis of L²(ℝⁿ) is countably infinite ([[§26 Position Eigenstates and Continuous Resolutions#^thm-26-2|§26.2]]), and the uncountable family |x⟩ cannot be one.
- **Classification.** The classification of separable Hilbert spaces is [[§20 Orthonormal Sets and Bases#^thm-20-20|§20.20]] (HW5, Problem 2): a countable orthonormal basis gives a unitary map onto $\mathbb{F}^n$ or $\ell^2$.
