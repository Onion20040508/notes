---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 39.9", "simplicity of the alternating groups"]
tags: [group-theory, hub]
---
![[Group Theory §39 Simple Groups#^thm-39-9]]

## Treated in
- [[Group Theory §39 Simple Groups#^thm-39-9|Theorem §39.9: A_n Is Simple for n ≥ 5]], in [[Group Theory §39 Simple Groups]]

## Its proof uses
- [[Group Theory §11 Disjoint Cycle Decomposition#^lem-11-2|Lemma §11.2: Disjoint Cycles Commute]]
- [[Group Theory §12 Multiplying and Conjugating Cycles#^prop-12-1|Proposition §12.1: Conjugation Relabels a Cycle]]
- [[Group Theory §20 The Sign Homomorphism and the Alternating Group#^cor-20-4|Corollary §20.4: Parity of a Permutation]]
- [[Group Theory §20 The Sign Homomorphism and the Alternating Group#^thm-20-9|Theorem §20.9: Generators of A_n]]
- [[Group Theory §35 Normal Subgroups#^def-35-1|Definition §35.1: Normal Subgroup]]
- [[Group Theory §39 Simple Groups#^def-39-1|Definition §39.1: Simple Group]]
- [[Group Theory §39 Simple Groups#^lem-39-8|Lemma §39.8: 3-Cycles Are Conjugate in A_n for n ≥ 5]]

## Used in (Group Theory)
- [[Group Theory §39 Simple Groups#^cor-39-11|Corollary §39.11: Which A_n Are Simple]]

## Connections
- **Why n ≥ 5.** For n = 4 it fails: V = {e, (1 2)(3 4), (1 3)(2 4), (1 4)(2 3)} is normal in A₄, as the kernel of the pair-partition map ([[Group Theory §39 Simple Groups#^prop-39-10|§39.10]]), and (1 2 3), (1 3 2) are not conjugate in A₄ ([[Group Theory §39 Simple Groups#^ex-39-1|Ex. §39.1]], [[Group Theory §39 Simple Groups#^rem-39-6|Why n ≥ 5]]).
- **Used for.** [[Group Theory §39 Simple Groups#^cor-39-11|Which Aₙ Are Simple]] (§39.11). It gives the first infinite family of non-abelian simple groups, starting with A₅, the smallest one ([[Group Theory §39 Simple Groups#^thm-39-7|§39.7]]). The other family is PSL_n(F) ([[Group Theory §39 Simple Groups#^thm-39-13|§39.13]]). For n = 5 the class sizes 1, 20, 15, 12, 12 give a second proof ([[Group Theory §39 Simple Groups#^prop-39-6|A₅ Is Simple]]).
- **Proof idea.** A nontrivial normal subgroup N contains the commutator g(i j k)g⁻¹(i j k)⁻¹ for suitable g ∈ N; it is a nontrivial product of two 3-cycles, and a case check on its cycle type then yields a 3-cycle in N. [[Conjugation Relabels a Cycle]] and [[Group Theory §39 Simple Groups#^lem-39-8|3-Cycles Are Conjugate in Aₙ]] then bring in every 3-cycle, and the 3-cycles generate Aₙ ([[Group Theory §20 The Sign Homomorphism and the Alternating Group#^thm-20-9|§20.9]]).
- **Coming later in the course.** Composition series and the Jordan–Hölder theorem: for n ≥ 5, Sₙ ⊳ Aₙ ⊳ {e} is a composition series with factors ℤ/2ℤ and Aₙ, so Sₙ is not solvable.
