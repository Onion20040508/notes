---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 17.4"]
tags: [group-theory, hub]
---
![[§17 Cyclic Groups#^thm-17-4]]

## Treated in
- [[§17 Cyclic Groups#^thm-17-4|Theorem §17.4: Subgroups of Cyclic Groups Are Cyclic]], in [[§17 Cyclic Groups]]

## Its proof uses
- [[§4 Subgroups#^lem-4-4|Lemma §4.4: Exponent Laws]]
- [[§4 Subgroups#^prop-4-6|Proposition §4.6: ⟨g⟩ Is the Smallest Subgroup Containing g]]
- [[§6 Divisibility and Congruence#^lem-6-1|Lemma §6.1: Division Algorithm]]

## Its proof uses (other subjects)
- [[§1 The Set ℕ of Natural Numbers#^thm-1-2|451 §1.2: Well-Ordering Principle]]

## Used in (Group Theory)
- [[§17 Cyclic Groups#^cor-17-6|Corollary §17.6: Generators and Subgroups of a Finite Cyclic Group]]

## Connections
- **Used for.** [[§17 Cyclic Groups#^cor-17-6|Generators and Subgroups of a Finite Cyclic Group]] (§17.6): exactly one subgroup of each order d dividing n, e.g. in ℤ/12ℤ ([[§17 Cyclic Groups#^ex-17-1|Ex. §17.1]]).
- **Proof shape.** Take the least m > 0 with gᵐ ∈ H and divide any exponent t with gᵗ ∈ H by m: the remainder must be 0, so H = ⟨gᵐ⟩. Equivalently, those exponents form a subgroup of ℤ, which is mℤ by [[Subgroups of ℤ]]. It is [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^rem-9-2|The Division-Algorithm Pattern]] again.
- **Cyclic is needed.** Subgroups of ℤ² can need two generators ([[§5 A Zoo of Subgroups#^ex-5-1|Ex. §5.1]], [[§5 A Zoo of Subgroups#^rem-5-2|Forward Pointer: Rank]]). The converse also fails: every proper subgroup of U₈ ≅ ℤ/2ℤ × ℤ/2ℤ is cyclic, but U₈ is not ([[§16 Isomorphisms#^prop-16-8|§16.8]]).
- **Same idea elsewhere.** The 590 notes sketch the same argument ([[§21 Algebra Prerequisites꞉ Groups#^prop-21-1|590 Prop. §21.1]], part 2).
- **Foundation in [[Logic and Proofs]]:** the well-ordering principle used for the least exponent m is [[§5 The Induction Principle#^cor-5-7|250 Cor. §5.7]] (proved there from induction).
