---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 35.11", "Lᵖ is complete"]
tags: [measure-theory, hub]
---
![[§35 Lᵖ as a Banach Space#^thm-35-11]]

## Treated in
- [[§35 Lᵖ as a Banach Space#^thm-35-11|Theorem §35.11: Riesz–Fischer Theorem]], in [[§35 Lᵖ as a Banach Space]]

## Its proof uses
- [[§10 Lebesgue Outer Measure#^prop-10-1|Proposition §10.1: Basic Properties of Outer Measure]]
- [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-2|Proposition §21.2: Integral over Null Sets and A.E. Equal Functions]]
- [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-8|Theorem §21.8: Fatou's Lemma]]
- [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|Proposition §34.2: The Essential Supremum is Achieved A.E.]]
- [[§35 Lᵖ as a Banach Space#^def-35-1|Definition §35.1: Lᵖ Convergence]]
- [[§35 Lᵖ as a Banach Space#^def-35-2|Definition §35.2: Cauchy Sequences in Lᵖ]]
- [[§35 Lᵖ as a Banach Space#^def-35-3|Definition §35.3: Completeness of Lᵖ]]
- [[§35 Lᵖ as a Banach Space#^lem-35-9|Lemma §35.9: Cauchy Subsequence Lemma]]

## Its proof uses (other subjects)
- [[§10a Cauchy Sequences#^thm-10a-3|451 §10a.3: Cauchy Implies Convergent]]
- [[§24 Uniform Convergence#^def-24-2|451 §24.2: Uniform Convergence]]

## Used in (Measure Theory)
- (not cited later in the course)

## Connections
- **Proof idea.** A Cauchy sequence has a subsequence whose consecutive differences have summable Lᵖ norms. By the absolute series test ([[§35 Lᵖ as a Banach Space#^cor-35-7|§35.7]], [[§35 Lᵖ as a Banach Space#^lem-35-9|Lemma §35.9]]), the subsequence converges a.e. to some f. [[Fatou's Lemma]] then bounds the Lᵖ distance from f_k to f by the liminf over j of the distance from f_k to the j-th subsequence term, which is small. For p = ∞, the convergence is uniform off a null set ([[§24 Uniform Convergence#^def-24-2|451 Def. §24.2]], [[§10a Cauchy Sequences#^thm-10a-3|Cauchy implies convergent]]).
- **Chain.** Hölder → [[Minkowski's Inequality]] → Riesz–Fischer. The engine is “absolutely convergent series converge”, built on the [[Monotone Convergence Theorem (Lebesgue)|MCT]] ([[§23 The Dominated Convergence Theorem#^cor-23-4|§23.4]] for p = 1). This is the Lᵖ analogue of [[§14 Series#^prop-14-6|451 §14.6]], and in a normed space it is equivalent to completeness.
- **Riemann vs Lebesgue.** Lᵖ is complete like ℝⁿ ([[§13 Some Topological Concepts in Metric Spaces#^thm-13-2|451 §13.2]]). The Riemann integrable functions with the L¹ distance are not: min(n, x^(−1/2)) is L¹-Cauchy on (0, 1] with an unbounded limit. For p = 2, L² is a complete inner product space, extending the inner products of [[§20 Inner Products and Norms#^ladr-6-2|LADR 6.2]].
- **Byproduct.** Lᵖ convergence implies a.e. convergence of a subsequence ([[§35 Lᵖ as a Banach Space#^cor-35-10|§35.10]]). This is used, ahead of its proof, in [[§30 Differentiating the Integral#^thm-30-7|Differentiation of the Integral]] (§18.26).
