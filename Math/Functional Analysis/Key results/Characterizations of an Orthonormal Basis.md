---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 27.8", "Parseval", "Lax §6.4, Lemma 8"]
tags: [functional-analysis, hub]
---
![[§27 Orthonormal Sets and Bases#^thm-27-8]]

## Treated in
- [[§27 Orthonormal Sets and Bases#^thm-27-8|Theorem §27.8: Characterizations of an Orthonormal Basis]], in [[§27 Orthonormal Sets and Bases]]

## Its proof uses
- [[§27 Orthonormal Sets and Bases#^def-27-2|Definition §27.2: Complete Orthogonal Set]]
- [[§27 Orthonormal Sets and Bases#^def-27-4|Definition §27.4: Orthonormal Basis]]
- [[§27 Orthonormal Sets and Bases#^prop-27-6|Proposition §27.6: The Orthonormal Expansion Converges]]
- [[§27 Orthonormal Sets and Bases#^lem-27-7|Lemma §27.7: Coefficients and Norm of the Expansion]]

## Used in (Functional Analysis)
- [[§27 Orthonormal Sets and Bases#^prop-27-9|Proposition §27.9: Lax's Definition of Orthonormal Base Agrees]]
- [[§27 Orthonormal Sets and Bases#^prop-27-10|Proposition §27.10: Small Perturbations of a Complete Orthonormal Set]]
- [[§27 Orthonormal Sets and Bases#^thm-27-11|Theorem §27.11: The Fourier Basis of L²[0,2π]]]
- [[§28 Existence of Orthonormal Bases and Separability#^thm-28-1|Theorem §28.1: Existence of Orthonormal Bases]]
- [[§28 Existence of Orthonormal Bases and Separability#^thm-28-3|Theorem §28.3: Separable Hilbert Spaces and Countable Bases]]
- [[§28 Existence of Orthonormal Bases and Separability#^thm-28-4|Theorem §28.4: Classification of Separable Hilbert Spaces]]
- [[§36 The Completeness Relation#^thm-36-2|Theorem §36.2: The Completeness Relation]]
- [[§37 Position Eigenstates and Continuous Resolutions#^thm-37-2|Theorem §37.2: L²(ℝⁿ) is Separable]]
- [[§38 Bound States Need Not Be Complete꞉ Hydrogen#^cor-38-2|Corollary §38.2: Bound States are Not Complete]]

## Connections
- **How.** Everything rests on the expansion s(x) = Σ(x, e_α)e_α. It converges by [[Bessel's Inequality]], and it has the same coefficients as x, because the inner product is continuous and passes through the limit ([[§27 Orthonormal Sets and Bases#^lem-27-7|§27.7]]). Then (1)⇒(2): x − s(x) is orthogonal to every e_α, so completeness kills it. (2)⇒(3) is the norm of the expansion, and (3)⇒(1) is immediate. Bessel becomes an equality exactly for complete sets.
- **Finite dimensions.** In LADR, v = Σ⟨v, e_k⟩e_k and ‖v‖² = Σ|⟨v, e_k⟩|² for an orthonormal basis ([[§21 Orthonormal Bases#^ladr-6-30|LADR 6.30]]). In infinite dimensions the three conditions agree only once the sums are read as countable-support limits. They are also equivalent to Lax's definition, closed span = H, via the orthogonal decomposition ([[§27 Orthonormal Sets and Bases#^prop-27-9|§27.9]]).
- **Used for.** It identifies the standard basis of ℓ² ([[§27 Orthonormal Sets and Bases#^ex-27-1|Ex. §27.1]]) and the Fourier basis of L²[0,2π] ([[§27 Orthonormal Sets and Bases#^thm-27-11|§27.11]]), where Parseval reads ∫|f|² = Σ|c_n|². It turns maximal orthonormal sets into bases ([[Existence of Orthonormal Bases]]) and yields countable bases in separable spaces ([[Separable Hilbert Spaces Have Countable Orthonormal Bases]]). Parseval for a complete set drives the perturbation result [[§27 Orthonormal Sets and Bases#^prop-27-10|§27.10]] ([[Functional Analysis Problem-Solving Techniques#^rem-t13|Technique 13]]).
- **In the companion chapter.** (1)⇔(2) is the completeness relation Σ|e_n⟩⟨e_n| = 𝟏. It holds strongly ([[§36 The Completeness Relation#^thm-36-2|§36.2]]) but never in operator norm for an infinite set ([[§36 The Completeness Relation#^prop-36-3|§36.3]]). Polarized Parseval is “inserting a complete set of states” ([[§36 The Completeness Relation#^cor-36-4|§36.4]]). Hydrogen's bound states fail (1), so Parseval fails for them ([[§38 Bound States Need Not Be Complete꞉ Hydrogen#^cor-38-2|§38.2]]).
- **Also in [[Applied Linear Algebra]]:** [[§51 Orthogonal Sets#^thm-51-2|235 Thm. §51.2]] (the finite expansion in an orthogonal basis of a subspace of ℝⁿ, with worked examples; Parseval is not stated there).
- **Also in [[Fourier Series and PDEs]]:** [[§15★ Mean Error and Convergence in Mean#^thm-15-4|341 Thm. §15.4]] (Parseval's equality for Fourier series, used to sum series such as Σ1/n⁴).
