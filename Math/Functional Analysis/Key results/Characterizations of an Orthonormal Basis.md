---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 24.8", "Parseval", "Lax §6.4, Lemma 8"]
tags: [functional-analysis, hub]
---
![[§24 Orthonormal Sets and Bases#^thm-24-8]]

## Treated in
- [[§24 Orthonormal Sets and Bases#^thm-24-8|Theorem §24.8: Characterizations of an Orthonormal Basis]], in [[§24 Orthonormal Sets and Bases]]

## Its proof uses
- [[§24 Orthonormal Sets and Bases#^def-24-2|Definition §24.2: Complete Orthogonal Set]]
- [[§24 Orthonormal Sets and Bases#^def-24-4|Definition §24.4: Orthonormal Basis]]
- [[§24 Orthonormal Sets and Bases#^prop-24-6|Proposition §24.6: The Orthonormal Expansion Converges]]
- [[§24 Orthonormal Sets and Bases#^lem-24-7|Lemma §24.7: Coefficients and Norm of the Expansion]]

## Used in (Functional Analysis)
- [[§24 Orthonormal Sets and Bases#^ex-24-1|Example §24.1: The Standard Basis of ell²]]
- [[§24 Orthonormal Sets and Bases#^prop-24-9|Proposition §24.9: Lax's Definition of Orthonormal Base Agrees]]
- [[§24 Orthonormal Sets and Bases#^prop-24-10|Proposition §24.10: Small Perturbations of a Complete Orthonormal Set]]
- [[§24 Orthonormal Sets and Bases#^thm-24-11|Theorem §24.11: The Fourier Basis of L²[0,2π]]]
- [[§24 Orthonormal Sets and Bases#^thm-24-12|Theorem §24.12: Existence of Orthonormal Bases]]
- [[§24 Orthonormal Sets and Bases#^thm-24-13|Theorem §24.13: Separable Hilbert Spaces and Countable Bases]]
- [[§24 Orthonormal Sets and Bases#^thm-24-15|Theorem §24.15: Classification of Separable Hilbert Spaces]]
- [[§31 The Completeness Relation#^thm-31-2|Theorem §31.2: The Completeness Relation]]
- [[§31 The Completeness Relation#^cor-31-4|Corollary §31.4: Inserting a Complete Set of States]]
- [[§32 Position Eigenstates and Continuous Resolutions#^thm-32-2|Theorem §32.2: L²(ℝⁿ) is Separable]]
- [[§33 Bound States Need Not Be Complete꞉ Hydrogen#^cor-33-2|Corollary §33.2: Bound States are Not Complete]]

## Connections
- **How.** Everything rests on the expansion s(x) = Σ(x, e_α)e_α. It converges by [[Bessel's Inequality]], and it has the same coefficients as x, because the inner product is continuous and passes through the limit ([[§24 Orthonormal Sets and Bases#^lem-24-7|§24.7]]). Then (1)⇒(2): x − s(x) is orthogonal to every e_α, so completeness kills it. (2)⇒(3) is the norm of the expansion, and (3)⇒(1) is immediate. Bessel becomes an equality exactly for complete sets.
- **Finite dimensions.** In LADR, v = Σ⟨v, e_k⟩e_k and ‖v‖² = Σ|⟨v, e_k⟩|² for an orthonormal basis ([[§20 Orthonormal Bases#^ladr-6-30|LADR 6.30]]). In infinite dimensions the three conditions agree only once the sums are read as countable-support limits. They are also equivalent to Lax's definition, closed span = H, via the orthogonal decomposition ([[§24 Orthonormal Sets and Bases#^prop-24-9|§24.9]]).
- **Used for.** It identifies the standard basis of ℓ² ([[§24 Orthonormal Sets and Bases#^ex-24-1|Ex. §24.1]]) and the Fourier basis of L²[0,2π] ([[§24 Orthonormal Sets and Bases#^thm-24-11|§24.11]]), where Parseval reads ∫|f|² = Σ|c_n|². It turns maximal orthonormal sets into bases ([[Existence of Orthonormal Bases]]) and yields countable bases in separable spaces ([[Separable Hilbert Spaces Have Countable Orthonormal Bases]]). Parseval for a complete set drives the perturbation result [[§24 Orthonormal Sets and Bases#^prop-24-10|§24.10]] ([[Functional Analysis Problem-Solving Techniques#^rem-t13|Technique 13]]).
- **In the companion chapter.** (1)⇔(2) is the completeness relation Σ|e_n⟩⟨e_n| = 𝟏. It holds strongly ([[§31 The Completeness Relation#^thm-31-2|§31.2]]) but never in operator norm for an infinite set ([[§31 The Completeness Relation#^prop-31-3|§31.3]]). Polarized Parseval is “inserting a complete set of states” ([[§31 The Completeness Relation#^cor-31-4|§31.4]]). Hydrogen's bound states fail (1), so Parseval fails for them ([[§33 Bound States Need Not Be Complete꞉ Hydrogen#^cor-33-2|§33.2]]).
- **Also in [[Applied Linear Algebra]]:** [[§41 Orthogonal Sets#^thm-41-2|235 Thm. §41.2]] (the finite expansion in an orthogonal basis of a subspace of ℝⁿ, with worked examples; Parseval is not stated there).
- **Also in [[Fourier Series and PDEs]]:** [[§11★ Mean Error and Convergence in Mean#^thm-11-4|341 Thm. §11.4]] (Parseval's equality for Fourier series, used to sum series such as Σ1/n⁴).
