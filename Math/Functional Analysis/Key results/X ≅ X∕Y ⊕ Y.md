---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 1.11", "quotient and complement"]
tags: [functional-analysis, hub]
---
![[§2 Quotient Spaces and Complements#^thm-2-6]]

## Treated in
- [[§2 Quotient Spaces and Complements#^thm-2-6|Theorem §2.6: X ≅ X/Y oplus Y]], in [[§1 Linear Spaces]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-4|Definition §1.4: Direct Sum]]
- [[§2 Quotient Spaces and Complements#^prop-2-1|Proposition §2.1: X/Y is a Linear Space]]
- [[§2 Quotient Spaces and Complements#^def-2-2|Definition §2.2: Equivalence Class and Quotient Space]]
- [[§2 Quotient Spaces and Complements#^lem-2-5|Lemma §2.5: Unique Decomposition]]
- [[§3 Linear Maps, Convexity, and Linear Functionals#^lem-3-1|Lemma §3.1: Inverse of an Isomorphism]]
- [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-2|Definition §3.2: Isomorphism]]

## Used in (Functional Analysis)
- [[§2 Quotient Spaces and Complements#^cor-2-7|Corollary §2.7: A Complement is a Model of the Quotient]]
- [[§2 Quotient Spaces and Complements#^cor-2-8|Corollary §2.8: Orthogonal Complement (inner products; later)]]

## Connections
- **How.** Fix a complement W ([[Every Subspace Has a Complement]]). Decompose x = w + y uniquely ([[§2 Quotient Spaces and Complements#^lem-2-5|§2.5]], [[Functional Analysis Problem-Solving Techniques#^rem-t2|Technique 2]]) and send x ↦ ([w], y). Linearity follows from uniqueness of the decomposition ([[Functional Analysis Problem-Solving Techniques#^rem-t4|Technique 4]]). Surjectivity replaces a representative by its W-component ([[Functional Analysis Problem-Solving Techniques#^rem-t1|Technique 1]]).
- **Not canonical.** M depends on the choice of W. X/Y is canonical and isomorphic to every complement ([[§2 Quotient Spaces and Complements#^cor-2-7|§2.7]]), but equal to none ([[§2 Quotient Spaces and Complements#^rem-2-4|Remark §2]]).
- **Finite dimensions.** It gives dim V/U = dim V − dim U ([[§11 Products and Quotients of Vector Spaces#^ladr-3-105|LADR 3.105]]), with a complement obtained by extending a basis ([[§5 Bases#^ladr-2-33|LADR 2.33]]).
- **With more structure.** If X = Y + Y⊥ for an inner product, then Y⊥ is a complement and X/Y ≅ Y⊥ ([[§2 Quotient Spaces and Complements#^cor-2-8|§2.8]]). The [[Orthogonal Decomposition Theorem]] supplies this for closed Y in a Hilbert space, and c₀₀ ⊂ ℓ² shows that it can fail otherwise ([[§2 Quotient Spaces and Complements#^rem-2-5|Remark §2]]). With a norm, X/Y is normed when Y is closed ([[Quotient Norm]]).
