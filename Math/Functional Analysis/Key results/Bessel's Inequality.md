---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 27.5"]
tags: [functional-analysis, hub]
---
![[§27 Orthonormal Sets and Bases#^thm-27-5]]

## Treated in
- [[§27 Orthonormal Sets and Bases#^thm-27-5|Theorem §27.5: Bessel's Inequality]], in [[§27 Orthonormal Sets and Bases]]

## Its proof uses
- [[§27 Orthonormal Sets and Bases#^lem-27-2|Lemma §27.2: Finite Bessel Inequality]]
- [[§27 Orthonormal Sets and Bases#^def-27-3|Definition §27.3: Sums of Non-Negative Families]]
- [[§27 Orthonormal Sets and Bases#^lem-27-3|Lemma §27.3: The Sum Does Not Depend on the Enumeration]]
- [[§27 Orthonormal Sets and Bases#^prop-27-4|Proposition §27.4: Only Countably Many Coefficients are Nonzero]]

## Used in (Functional Analysis)
- [[§27 Orthonormal Sets and Bases#^prop-27-6|Proposition §27.6: The Orthonormal Expansion Converges]]
- [[§35 The Completeness Relation#^cor-35-4|Corollary §35.4: Inserting a Complete Set of States]]
- [[§37 Bound States Need Not Be Complete꞉ Hydrogen#^cor-37-2|Corollary §37.2: Bound States are Not Complete]]

## Connections
- **How.** The finite version comes first. Subtracting from x its components along e₁, …, e_k leaves a remainder orthogonal to each e_j, so Pythagoras gives ‖x‖² = ‖y‖² + Σ|(x, e_j)|² ([[§27 Orthonormal Sets and Bases#^lem-27-2|§27.2]]). To make sense of the sum over an arbitrary index set, the level sets |(x, e_α)| ≥ 1/k each have at most k²‖x‖² elements, so only countably many coefficients are nonzero ([[§27 Orthonormal Sets and Bases#^prop-27-4|§27.4]], [[Functional Analysis Problem-Solving Techniques#^rem-t12|Technique 12]]). A sum of non-negative terms is the supremum of its finite sums ([[§27 Orthonormal Sets and Bases#^lem-27-3|§27.3]]). No completeness is used, so Bessel holds in every inner product space.
- **Used for.** In a Hilbert space it makes the orthonormal expansion converge. ‖s_n − s_m‖² is a tail of the convergent series Σ|(x, e_j)|², so the partial sums are Cauchy ([[§27 Orthonormal Sets and Bases#^prop-27-6|§27.6]]). Equality for every x is Parseval, which holds exactly for complete sets ([[Characterizations of an Orthonormal Basis]]).
- **Finite dimensions.** LADR's Bessel inequality for an orthonormal list ([[§21 Orthonormal Bases#^ladr-6-26|LADR 6.26]]) is exactly the finite lemma [[§27 Orthonormal Sets and Bases#^lem-27-2|§27.2]]. What is new here is countable support and the passage to the limit.
- **In the companion chapter.** For a normalized state ψ, Σ|(ψ, ψ_nlm)|² is the probability of finding the hydrogen electron in some bound state, and Bessel says it is at most 1. It is strictly less than 1 for some ψ, because the bound states are not complete ([[§37 Bound States Need Not Be Complete꞉ Hydrogen#^cor-37-2|§37.2]]); the deficit is the ionization probability. Bessel also gives the absolute convergence in “inserting a complete set of states” ([[§35 The Completeness Relation#^cor-35-4|§35.4]]).
- **Also in [[Applied Linear Algebra]]:** [[§56 Inner Product Spaces#^prop-56-3|235 Prop. §56.3]] (the finite form: the projection onto a finite-dimensional subspace is shorter than the vector, used there to prove Cauchy–Schwarz).
- **Also in [[Fourier Series and PDEs]]:** [[§15★ Mean Error and Convergence in Mean#^thm-15-3|341 Thm. §15.3]] (Bessel's inequality for Fourier series, from the mean square error; its consequence that the coefficients tend to 0 is [[§15★ Mean Error and Convergence in Mean#^cor-15-5|341 Cor. §15.5]]).
