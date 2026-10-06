---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 35.2", "Minkowski"]
tags: [measure-theory, hub]
---
![[§35 Lᵖ as a Banach Space#^thm-35-2]]

## Treated in
- [[§35 Lᵖ as a Banach Space#^thm-35-2|Theorem §35.2: Minkowski's Inequality]], in [[§35 Lᵖ as a Banach Space]]

## Its proof uses
- [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|Proposition §20.3: Basic Properties]]
- [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|Theorem §21.1: Linearity of the Integral]]
- [[§22 The General Lebesgue Integral#^prop-22-3|Proposition §22.3: Triangle Inequality]]
- [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|Proposition §34.2: The Essential Supremum is Achieved A.E.]]
- [[§34 Normed Linear Spaces and Lᵖ Spaces#^thm-34-5|Theorem §34.5: Hölder's Inequality]]
- [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-10|Definition §34.10: Conjugate Exponents]]
- [[§35 Lᵖ as a Banach Space#^prop-35-1|Proposition §35.1: Lᵖ is a Linear Space]]

## Used in (Measure Theory)
- [[§35 Lᵖ as a Banach Space#^thm-35-3|Theorem §35.3: Lᵖ is a Normed Linear Space]]
- [[§35 Lᵖ as a Banach Space#^cor-35-4|Corollary §35.4: Minkowski for Finite Sums]]
- [[§35 Lᵖ as a Banach Space#^prop-35-8|Proposition §35.8: Basic Properties of Lᵖ Convergence]]
- [[§35 Lᵖ as a Banach Space#^cor-35-10|Corollary §35.10: Lᵖ Convergence Implies A.E. Convergent Subsequence]]

## Connections
- **Proof idea.** For 1 < p < ∞, write |f + g|ᵖ ≤ |f|·|f + g|^(p−1) + |g|·|f + g|^(p−1). Apply [[Hölder's Inequality]] with exponents p and p′ = p/(p − 1) to each term, then divide by the Lᵖ norm of f + g raised to the power p − 1. p = 1 is [[§22 The General Lebesgue Integral#^prop-22-3|Proposition §22.3]], and p = ∞ is pointwise.
- **Linear algebra.** It is the triangle inequality that makes the Lᵖ norm a norm ([[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-2|Def. §34.2]], [[§35 Lᵖ as a Banach Space#^thm-35-3|§35.3]]). For p = 2 the norm comes from ⟨f, g⟩ = ∫fg, and Minkowski is the inner-product [[Triangle inequality]] (LADR 6.17), just as Hölder is [[Cauchy–Schwarz inequality|Cauchy–Schwarz]]. Among the Lᵖ norms only p = 2 satisfies the [[§20 Inner Products and Norms#^ladr-6-21|parallelogram equality]].
- **Chain.** Hölder → Minkowski → series bounds ([[§35 Lᵖ as a Banach Space#^cor-35-5|§35.5]], via the [[Monotone Convergence Theorem (Lebesgue)]], and [[§35 Lᵖ as a Banach Space#^cor-35-7|§35.7]]) → [[Riesz–Fischer Theorem]]. It also gives [[§35 Lᵖ as a Banach Space#^prop-35-8|uniqueness of Lᵖ limits and continuity of the norm]] (§19.15).
