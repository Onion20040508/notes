---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 28.3", "Lax §6.4, Thm 9'"]
tags: [functional-analysis, hub]
---
![[§28 Existence of Orthonormal Bases and Separability#^thm-28-3]]

## Treated in
- [[§28 Existence of Orthonormal Bases and Separability#^thm-28-3|Theorem §28.3: Separable Hilbert Spaces and Countable Bases]], in [[§28 Existence of Orthonormal Bases and Separability]]

## Its proof uses
- [[§25 Projection and Orthogonal Decomposition#^lem-25-1|Lemma §25.1: The Inner Product is Continuous]]
- [[§27 Orthonormal Sets and Bases#^lem-27-1|Lemma §27.1: Pythagoras]]
- [[§27 Orthonormal Sets and Bases#^def-27-2|Definition §27.2: Complete Orthogonal Set]]
- [[§27 Orthonormal Sets and Bases#^prop-27-6|Proposition §27.6: The Orthonormal Expansion Converges]]
- [[§27 Orthonormal Sets and Bases#^thm-27-8|Theorem §27.8: Characterizations of an Orthonormal Basis]]
- [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|Definition §28.1: Separable Space]]
- [[§28 Existence of Orthonormal Bases and Separability#^lem-28-2|Lemma §28.2: Gram–Schmidt]]

## Its proof uses (other subjects)
- [[Countable Union of Countable Sets is Countable]] (Measure Theory)

## Used in (Functional Analysis)
- [[§28 Existence of Orthonormal Bases and Separability#^thm-28-4|Theorem §28.4: Classification of Separable Hilbert Spaces]]

## Connections
- **How.** (⇒) Finite rational combinations of basis vectors form a countable set, and it is dense: truncate the expansion, then round the finitely many coefficients, as for ℓᵖ ([[§29 Sequence and Function Spaces#^prop-29-1|§29.1]]). (⇐) Thin the dense sequence to a linearly independent one with the same span, and apply Gram–Schmidt ([[§28 Existence of Orthonormal Bases and Separability#^lem-28-2|§28.2]]). The result is complete: if x ⊥ every e_j, then x is orthogonal to the dense set, so (x, x) = lim (x, y_(n_k)) = 0 by continuity of the inner product.
- **Same idea elsewhere.** Lemma [[§28 Existence of Orthonormal Bases and Separability#^lem-28-2|§28.2]] is LADR's [[Gram–Schmidt procedure]] (6.32) run along an infinite sequence; only finite combinations occur, and the limit is taken in the inner product. Separability is the metric notion of 551 ([[§35 Lᵖ as a Banach Space#^def-35-5|551 Def. §35.5]]) and the topological one of 590 ([[§22 Countability Axioms#^def-22-5|590 Def. §22.5]]). Since L²(ℝⁿ) is separable ([[§35 Lᵖ as a Banach Space#^cor-35-13|551 §35.13]], [[§29 Sequence and Function Spaces#^prop-29-4|§29.4]]), it has a countable orthonormal basis.
- **Stronger.** In a separable space every orthonormal set is countable. Orthonormal vectors are √2 apart, so disjoint balls of radius √2/2 around them each catch their own point of the dense set ([[§37 Position Eigenstates and Continuous Resolutions#^prop-37-1|§37.1]]). Hence every orthonormal basis of L²(ℝⁿ) is countably infinite ([[§37 Position Eigenstates and Continuous Resolutions#^thm-37-2|§37.2]]), and the uncountable family |x⟩ cannot be one.
- **Classification.** The classification of separable Hilbert spaces is [[§28 Existence of Orthonormal Bases and Separability#^thm-28-4|§28.4]] (HW5, Problem 2): a countable orthonormal basis gives a unitary map onto 𝔽ⁿ or ℓ².
