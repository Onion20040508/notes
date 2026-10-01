---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 9.1"]
tags: [group-theory, hub]
---
![[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1]]

## Treated in
- [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|Lemma §9.1: Euclid's Lemma]], in [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem]]

## Its proof uses
- [[§5 A Zoo of Subgroups#^cor-5-2|Corollary §5.2: Generated Subgroups of ℤ, and Bézout]]
- [[§6 Divisibility and Congruence#^def-6-1|Definition §6.1: Divisibility]]
- [[§8 Invertibility and Unit Groups#^def-8-1|Definition §8.1: Greatest Common Divisor; Coprime]]

## Used in (Group Theory)
- [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-2|Theorem §9.2: Unique Prime Factorization]]
- [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-3|Theorem §9.3: Chinese Remainder Theorem]]
- [[§17 Cyclic Groups#^prop-17-5|Proposition §17.5: The Order of a Power]]
- [[§21 The Structure of Uₙ#^thm-21-2|Theorem §21.2: Uₙ as a Product of Prime-Power Unit Groups]]

## Connections
- **Used for.** The uniqueness half of [[Unique Prime Factorization]], the [[Chinese Remainder Theorem]], [[§17 Cyclic Groups#^prop-17-5|The Order of a Power]] (§17.5), and [[§21 The Structure of Uₙ#^thm-21-2|the structure of Uₙ]] (§21.2).
- **Primality is needed.** 6 divides 2 · 3 but neither factor. In ℤ/nℤ, Euclid's lemma says [a][b] = [0] mod p forces [a] = [0] or [b] = [0]. This fails mod 6, where [2][3] = [0], which is why ℤ/nℤ is a field exactly for n prime ([[§8 Invertibility and Unit Groups#^prop-8-4|§8.4]], [[§3 Basic Examples of Groups#^prop-3-1|No Zero Divisors in a Field]]).
- **Proof idea.** If p ∤ a then gcd(a, p) = 1, and [[Bézout's Identity]] 1 = ax + py gives b = abx + pby, which p divides.
- **Also proved in [[Logic and Proofs]]:** [[§23 The Sequence of Prime Numbers#^thm-23-2|250 Thm. §23.2]] (prime case) and [[§17 Consequences of the Euclidean Algorithm#^thm-17-4|250 Thm. §17.4]] (coprime case), elementary proofs from Bézout, which is obtained there by the Euclidean algorithm.
