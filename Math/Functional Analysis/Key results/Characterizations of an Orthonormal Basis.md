---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 20.8", "Parseval", "Lax §6.4, Lemma 8"]
tags: [functional-analysis, hub]
---
![[§20 Orthonormal Sets and Bases#^thm-20-8]]

## Treated in
- [[§20 Orthonormal Sets and Bases#^thm-20-8|Theorem §20.8: Characterizations of an Orthonormal Basis]], in [[§20 Orthonormal Sets and Bases]]

## Its proof uses
- [[§20 Orthonormal Sets and Bases#^def-20-2|Definition §20.2: Complete Orthogonal Set]]
- [[§20 Orthonormal Sets and Bases#^def-20-4|Definition §20.4: Orthonormal Basis]]
- [[§20 Orthonormal Sets and Bases#^prop-20-6|Proposition §20.6: The Orthonormal Expansion Converges]]
- [[§20 Orthonormal Sets and Bases#^lem-20-7|Lemma §20.7: Coefficients and Norm of the Expansion]]

## Used in (Functional Analysis)
- [[§20 Orthonormal Sets and Bases#^ex-20-1|Example §20.1: The Standard Basis of ell²]]
- [[§20 Orthonormal Sets and Bases#^prop-20-9|Proposition §20.9: Lax's Definition of Orthonormal Base Agrees]]
- [[§20 Orthonormal Sets and Bases#^prop-20-10|Proposition §20.10: Small Perturbations of a Complete Orthonormal Set]]
- [[§20 Orthonormal Sets and Bases#^thm-20-11|Theorem §20.11: The Fourier Basis of L²[0,2π]]]
- [[§20 Orthonormal Sets and Bases#^thm-20-12|Theorem §20.12: Existence of Orthonormal Bases]]
- [[§20 Orthonormal Sets and Bases#^thm-20-17|Theorem §20.17: Separable Hilbert Spaces and Countable Bases]]
- [[§25 The Completeness Relation#^thm-25-2|Theorem §25.2: The Completeness Relation]]
- [[§25 The Completeness Relation#^cor-25-4|Corollary §25.4: Inserting a Complete Set of States]]
- [[§26 Position Eigenstates and Continuous Resolutions#^thm-26-2|Theorem §26.2: L²(ℝⁿ) is Separable]]
- [[§27 Bound States Need Not Be Complete꞉ Hydrogen#^cor-27-2|Corollary §27.2: Bound States are Not Complete]]

## Connections
- **How.** Everything rests on the expansion s(x) = Σ(x, e_α)e_α. It converges by [[Bessel's Inequality]], and it has the same coefficients as x, because the inner product is continuous and passes through the limit ([[§20 Orthonormal Sets and Bases#^lem-20-7|§20.7]]). Then (1)⇒(2): x − s(x) is orthogonal to every e_α, so completeness kills it. (2)⇒(3) is the norm of the expansion, and (3)⇒(1) is immediate. Bessel becomes an equality exactly for complete sets.
- **Finite dimensions.** In LADR, v = Σ⟨v, e_k⟩e_k and ‖v‖² = Σ|⟨v, e_k⟩|² for an orthonormal basis ([[§20 Orthonormal Bases#^ladr-6-30|LADR 6.30]]). In infinite dimensions the three conditions agree only once the sums are read as countable-support limits. They are also equivalent to Lax's definition, closed span = H, via the orthogonal decomposition ([[§20 Orthonormal Sets and Bases#^prop-20-9|§20.9]]).
- **Used for.** It identifies the standard basis of ℓ² ([[§20 Orthonormal Sets and Bases#^ex-20-1|Ex. §20.1]]) and the Fourier basis of L²[0,2π] ([[§20 Orthonormal Sets and Bases#^thm-20-11|§20.11]]), where Parseval reads ∫|f|² = Σ|c_n|². It turns maximal orthonormal sets into bases ([[Existence of Orthonormal Bases]]) and yields countable bases in separable spaces ([[Separable Hilbert Spaces Have Countable Orthonormal Bases]]). Parseval for a complete set drives the perturbation result [[§20 Orthonormal Sets and Bases#^prop-20-10|§20.10]] ([[Functional Analysis Problem-Solving Techniques#^rem-t13|Technique 13]]).
- **In the companion chapter.** (1)⇔(2) is the completeness relation Σ|e_n⟩⟨e_n| = 𝟏. It holds strongly ([[§25 The Completeness Relation#^thm-25-2|§25.2]]) but never in operator norm for an infinite set ([[§25 The Completeness Relation#^prop-25-3|§25.3]]). Polarized Parseval is “inserting a complete set of states” ([[§25 The Completeness Relation#^cor-25-4|§25.4]]). Hydrogen's bound states fail (1), so Parseval fails for them ([[§27 Bound States Need Not Be Complete꞉ Hydrogen#^cor-27-2|§27.2]]).
