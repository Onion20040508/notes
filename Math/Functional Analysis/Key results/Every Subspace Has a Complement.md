---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 1.8"]
tags: [functional-analysis, hub]
---
![[§1 Linear Spaces#^prop-1-8]]

## Treated in
- [[§1 Linear Spaces#^prop-1-8|Proposition §1.8: Every Subspace Has a Complement]], in [[§1 Linear Spaces]]

## Its proof uses
- [[§1 Linear Spaces#^lem-1-7|Lemma §1.7: One-Step Enlargement]]
- [[§1 Linear Spaces#^def-1-8|Definition §1.8: Complement]]
- [[§4 Statement and Motivation#^thm-4-2|Theorem §4.2: Hahn–Banach]] (the chain argument of its proof)
- [[§5 Proof of the Hahn–Banach Theorem#^thm-5-2|Theorem §5.2: Zorn's Lemma]]

## Used in (Functional Analysis)
- [[§1 Linear Spaces#^prop-1-9|Proposition §1.9: When the Complement is Unique]]

## Connections
- **How.** The proof is a one-step enlargement plus Zorn ([[Functional Analysis Problem-Solving Techniques#^rem-t3|Technique 3]]). Among subspaces W with W ∩ Y = {0}, the union of a chain is an upper bound. A maximal W has W + Y = X, since otherwise [[§1 Linear Spaces#^lem-1-7|§1.7]] adds a vector x₀ ∉ W + Y. This is the same pattern as the [[Hahn–Banach Theorem]] and [[Existence of Orthonormal Bases]].
- **Finite dimensions.** Zorn is unnecessary: apply the one-step lemma at most dim X − dim Y times ([[§1 Linear Spaces#^rem-1-8|Remark §1]]). LADR extends a basis of U to a basis of V ([[§5 Bases#^ladr-2-33|LADR 2.33]]).
- **Not unique.** The complement is unique only when Y = {0} or Y = X ([[§1 Linear Spaces#^prop-1-9|§1.9]]); every line through 0 other than the x-axis complements the x-axis in ℝ² ([[§1 Linear Spaces#^ex-1-5|Ex. §1.5]]). So [[X ≅ X∕Y ⊕ Y]] is not canonical, although all complements are isomorphic to X/Y ([[§1 Linear Spaces#^cor-1-12|§1.12]]).
- **With topology.** This complement is purely algebraic. A closed subspace of a Hilbert space has a canonical complement, Y⊥ ([[Orthogonal Decomposition Theorem]]). For the non-closed c₀₀ ⊂ ℓ², c₀₀⊥ = {0} is not a complement, although an algebraic complement still exists ([[§1 Linear Spaces#^rem-1-10|Remark §1]]).
