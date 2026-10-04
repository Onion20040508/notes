---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 1.11", "quotient and complement"]
tags: [functional-analysis, hub]
---
![[§1 Linear Spaces#^thm-1-11]]

## Treated in
- [[§1 Linear Spaces#^thm-1-11|Theorem §1.11: X ≅ X/Y ⊕ Y]], in [[§1 Linear Spaces]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-4|Definition §1.4: Direct Sum]]
- [[§1 Linear Spaces#^prop-1-6|Proposition §1.6: X/Y is a Linear Space]]
- [[§1 Linear Spaces#^def-1-7|Definition §1.7: Equivalence Class and Quotient Space]]
- [[§1 Linear Spaces#^lem-1-10|Lemma §1.10: Unique Decomposition]]
- [[§2 Linear Maps, Convexity, and Linear Functionals#^lem-2-1|Lemma §2.1: Inverse of an Isomorphism]]
- [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-2|Definition §2.2: Isomorphism]]

## Used in (Functional Analysis)
- [[§1 Linear Spaces#^cor-1-12|Corollary §1.12: A Complement is a Model of the Quotient]]
- [[§1 Linear Spaces#^cor-1-13|Corollary §1.13: Orthogonal Complement (inner products; later)]]

## Connections
- **How.** Fix a complement W ([[Every Subspace Has a Complement]]). Decompose x = w + y uniquely ([[§1 Linear Spaces#^lem-1-10|§1.10]], [[Functional Analysis Problem-Solving Techniques#^rem-t2|Technique 2]]) and send x ↦ ([w], y). Linearity follows from uniqueness of the decomposition ([[Functional Analysis Problem-Solving Techniques#^rem-t4|Technique 4]]). Surjectivity replaces a representative by its W-component ([[Functional Analysis Problem-Solving Techniques#^rem-t1|Technique 1]]).
- **Not canonical.** M depends on the choice of W. X/Y is canonical and isomorphic to every complement ([[§1 Linear Spaces#^cor-1-12|§1.12]]), but equal to none ([[§1 Linear Spaces#^rem-1-9|Remark §1]]).
- **Finite dimensions.** It gives dim V/U = dim V − dim U ([[§11 Products and Quotients of Vector Spaces#^ladr-3-105|LADR 3.105]]), with a complement obtained by extending a basis ([[§5 Bases#^ladr-2-33|LADR 2.33]]).
- **With more structure.** If X = Y + Y⊥ for an inner product, then Y⊥ is a complement and X/Y ≅ Y⊥ ([[§1 Linear Spaces#^cor-1-13|§1.13]]). The [[Orthogonal Decomposition Theorem]] supplies this for closed Y in a Hilbert space, and c₀₀ ⊂ ℓ² shows that it can fail otherwise ([[§1 Linear Spaces#^rem-1-10|Remark §1]]). With a norm, X/Y is normed when Y is closed ([[Quotient Norm]]).
