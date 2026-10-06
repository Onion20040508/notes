---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 2.1", "cancellation", "mixed hypothesis"]
tags: [group-theory, hub]
---
![[§2 First Consequences of the Axioms#^prop-2-1]]

## Treated in
- [[§2 First Consequences of the Axioms#^prop-2-1|Proposition §2.1: Cancellation, and What the Mixed Hypothesis Really Gives]], in [[§2 First Consequences of the Axioms]]

## Its proof uses
- [[§1 The Definition of a Group#^def-1-1|Definition §1.1: Group]]

## Used in (Group Theory)
- [[§2 First Consequences of the Axioms#^prop-2-3|Proposition §2.3: Uniqueness of Inverses]]
- [[§2 First Consequences of the Axioms#^prop-2-6|Proposition §2.6: One-Sided Inverses Suffice]]
- [[§2 First Consequences of the Axioms#^prop-2-7|Proposition §2.7: Unique Solvability of Linear Equations]]
- [[§3 Basic Examples of Groups#^prop-3-1|Proposition §3.1: No Zero Divisors in a Field]]
- [[§4 Subgroups#^prop-4-1|Proposition §4.1: A Subset That Is a Group Is a Subgroup]]
- [[§13 The Symmetric Group S₃#^prop-13-1|Proposition §13.1: Subgroups of S_3]]
- [[§15 Homomorphisms#^prop-15-1|Proposition §15.1: Homomorphisms Preserve Identity and Inverses]]
- [[§18 Conjugation, Products, and Pointwise Products#^prop-18-2|Proposition §18.2: Pointwise Products of Homomorphisms]]
- [[§18 Conjugation, Products, and Pointwise Products#^prop-18-4|Proposition §18.4: Characterizations of Abelian Groups]]
- [[§18 Conjugation, Products, and Pointwise Products#^prop-18-5|Proposition §18.5: Characterizations of Abelian Groups, Worksheet Form]]
- [[§29 The Index and Lagrange's Theorem#^prop-29-1|Proposition §29.1: All Cosets Have the Same Size]]
- [[§29 The Index and Lagrange's Theorem#^prop-29-5|Proposition §29.5: The Index Is Multiplicative]]

## Connections
- **Used for.** [[§2 First Consequences of the Axioms#^prop-2-3|Uniqueness of Inverses]], [[§2 First Consequences of the Axioms#^prop-2-6|One-Sided Inverses Suffice]] and [[§2 First Consequences of the Axioms#^prop-2-7|Unique Solvability of Linear Equations]]. The last gives the [[§2 First Consequences of the Axioms#^cor-2-8|Latin Square Property]] of group tables. Later it shows that all cosets have the same size ([[§29 The Index and Lagrange's Theorem#^prop-29-1|§29.1]]), which is the counting step in [[Lagrange's Theorem]].
- **Only same-side cancellation.** gh₁ = h₂g does not give h₁ = h₂: in S₃, (1 2)(2 3) = (1 3)(1 2) ([[§2 First Consequences of the Axioms#^ex-2-1|Ex. §2.1]]). The mixed hypothesis only gives h₂ = gh₁g⁻¹, a conjugate ([[§13 The Symmetric Group S₃#^ex-13-1|Ex. §13.1]], [[Conjugation Relabels a Cycle]]).
- **Without inverses.** In a field, cancelling a nonzero factor is the absence of zero divisors ([[§3 Basic Examples of Groups#^prop-3-1|§3.1]]). Modulo a prime, Euclid's Lemma plays this role: it makes multiplication by a nonzero class injective, hence a permutation of the nonzero classes ([[§8 Invertibility and Unit Groups#^prop-8-2|§8.2]]).
- **Same idea elsewhere.** The 590 notes use the same step for uniqueness of inverses ([[§21 Algebra Prerequisites꞉ Groups#^rem-21-2|Uniqueness of Identity and Inverses]]). It also shows that a group of order 2 is ℤ/2ℤ in the computation of π₁(P²) ([[§28 Fundamental Group of Some Surfaces#^pf-28-2|590 Thm. §28.2, proof]]).
