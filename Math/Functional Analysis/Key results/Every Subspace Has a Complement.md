---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 1.8"]
tags: [functional-analysis, hub]
---
![[§2 Quotient Spaces and Complements#^prop-2-3]]

## Treated in
- [[§2 Quotient Spaces and Complements#^prop-2-3|Proposition §2.3: Every Subspace Has a Complement]], in [[§1 Linear Spaces]]

## Its proof uses
- [[§2 Quotient Spaces and Complements#^lem-2-2|Lemma §2.2: One-Step Enlargement]]
- [[§2 Quotient Spaces and Complements#^def-2-4|Definition §2.4: Complement]]
- [[§5 Statement and Motivation#^thm-5-2|Theorem §5.2: Hahn–Banach]]
- [[§6 Proof of the Hahn–Banach Theorem#^thm-6-2|Theorem §6.2: Zorn's Lemma]]

## Used in (Functional Analysis)
- [[§2 Quotient Spaces and Complements#^prop-2-4|Proposition §2.4: When the Complement is Unique]]

## Connections
- **How.** The proof is a one-step enlargement plus Zorn ([[Functional Analysis Problem-Solving Techniques#^rem-t3|Technique 3]]). Among subspaces W with W ∩ Y = {0}, the union of a chain is an upper bound. A maximal W has W + Y = X, since otherwise [[§2 Quotient Spaces and Complements#^lem-2-2|§2.2]] adds a vector x₀ ∉ W + Y. This is the same pattern as the [[Hahn–Banach Theorem]] and [[Existence of Orthonormal Bases]].
- **Finite dimensions.** Zorn is unnecessary: apply the one-step lemma at most dim X − dim Y times ([[§2 Quotient Spaces and Complements#^rem-2-3|Remark §1]]). LADR extends a basis of U to a basis of V ([[§5 Bases#^ladr-2-33|LADR 2.33]]).
- **Not unique.** The complement is unique only when Y = {0} or Y = X ([[§2 Quotient Spaces and Complements#^prop-2-4|§2.4]]); every line through 0 other than the x-axis complements the x-axis in ℝ² ([[§2 Quotient Spaces and Complements#^ex-2-2|Ex. §2.2]]). So [[X ≅ X∕Y ⊕ Y]] is not canonical, although all complements are isomorphic to X/Y ([[§2 Quotient Spaces and Complements#^cor-2-7|§2.7]]).
- **With topology.** This complement is purely algebraic. A closed subspace of a Hilbert space has a canonical complement, Y⊥ ([[Orthogonal Decomposition Theorem]]). For the non-closed c₀₀ ⊂ ℓ², c₀₀⊥ = {0} is not a complement, although an algebraic complement still exists ([[§2 Quotient Spaces and Complements#^rem-2-5|Remark §1]]).
