---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 43.9", "simplicity of the alternating groups"]
tags: [group-theory, hub]
---
![[§43 Simple Groups#^thm-43-9]]

## Treated in
- [[§43 Simple Groups#^thm-43-9|Theorem §43.9: Aₙ Is Simple for n ≥ 5]], in [[§43 Simple Groups]]

## Its proof uses
- [[§11 Disjoint Cycle Decomposition#^lem-11-2|Lemma §11.2: Disjoint Cycles Commute]]
- [[§12 Multiplying and Conjugating Cycles#^prop-12-1|Proposition §12.1: Conjugation Relabels a Cycle]]
- [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|Corollary §21.4: Parity of a Permutation]]
- [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-9|Theorem §21.9: Generators of Aₙ]]
- [[§38 Normal Subgroups#^def-38-1|Definition §38.1: Normal Subgroup]]
- [[§43 Simple Groups#^def-43-1|Definition §43.1: Simple Group]]
- [[§43 Simple Groups#^lem-43-8|Lemma §43.8: 3-Cycles Are Conjugate in Aₙ for n ≥ 5]]

## Used in (Group Theory)
- [[§43 Simple Groups#^cor-43-11|Corollary §43.11: Which Aₙ Are Simple]]

## Connections
- **Why n ≥ 5.** For n = 4 it fails: V = {e, (1 2)(3 4), (1 3)(2 4), (1 4)(2 3)} is normal in A₄, as the kernel of the pair-partition map ([[§43 Simple Groups#^prop-43-10|§43.10]]), and (1 2 3), (1 3 2) are not conjugate in A₄ ([[§43 Simple Groups#^ex-43-1|Ex. §43.1]], [[§43 Simple Groups#^rem-43-6|Why n ≥ 5]]).
- **Used for.** [[§43 Simple Groups#^cor-43-11|Which Aₙ Are Simple]] (§43.11). It gives the first infinite family of non-abelian simple groups, starting with A₅, the smallest one ([[§43 Simple Groups#^thm-43-7|§43.7]]). The other family is PSL_n(F) ([[§43 Simple Groups#^thm-43-13|§43.13]]). For n = 5 the class sizes 1, 20, 15, 12, 12 give a second proof ([[§43 Simple Groups#^prop-43-6|A₅ Is Simple]]).
- **Proof idea.** A nontrivial normal subgroup N contains the commutator g(i j k)g⁻¹(i j k)⁻¹ for suitable g ∈ N; it is a nontrivial product of two 3-cycles, and a case check on its cycle type then yields a 3-cycle in N. [[Conjugation Relabels a Cycle]] and [[§43 Simple Groups#^lem-43-8|3-Cycles Are Conjugate in Aₙ]] then bring in every 3-cycle, and the 3-cycles generate Aₙ ([[§21 The Sign Homomorphism and the Alternating Group#^thm-21-9|§21.9]]).
- **Coming later in the course.** Composition series and the Jordan–Hölder theorem: for n ≥ 5, Sₙ ⊳ Aₙ ⊳ {e} is a composition series with factors ℤ/2ℤ and Aₙ, so Sₙ is not solvable.
