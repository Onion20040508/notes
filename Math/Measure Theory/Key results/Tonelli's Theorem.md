---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 25.3", "Tonelli"]
tags: [measure-theory, hub]
---
![[§25 Invariance Properties and Fubini's Theorem#^thm-25-3]]

## Treated in
- [[§25 Invariance Properties and Fubini's Theorem#^thm-25-3|Theorem §25.3: Tonelli's Theorem]], in [[§25 Invariance Properties and Fubini's Theorem]]

## Its proof uses
- [[§7 Structure of Open Sets#^prop-7-3|Proposition §7.3: Open Sets in ℝⁿ as Unions of Rectangles]]
- [[§13 Approximation and Continuity of Measure#^def-13-1|Definition §13.1: G_δ and F_σ Sets]]
- [[§13 Approximation and Continuity of Measure#^thm-13-1|Theorem §13.1: Approximation by Open and G_δ Sets]]
- [[§17 Simple Functions and Modes of Convergence#^thm-17-2|Theorem §17.2: Approximation by Simple Functions: Non-negative Case]]
- [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|Theorem §21.1: Linearity of the Integral]]
- [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|Proposition §21.4: Vanishing Integral for Non-Negative Functions]]
- [[§25 Invariance Properties and Fubini's Theorem#^def-25-2|Definition §25.2: The Tonelli Class 𝓕]]
- [[§25 Invariance Properties and Fubini's Theorem#^lem-25-5|Lemma §25.5: Closure Properties of 𝓕]]

## Used in (Measure Theory)
- [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|Theorem §25.6: Fubini's Theorem]]
- [[§26 Applications of Tonelli's Theorem#^thm-26-1|Theorem §26.1: Cross-Section Theorem (Restated)]]
- [[§26 Applications of Tonelli's Theorem#^thm-26-3|Theorem §26.3: Measurability of Product Sets]]
- [[§26 Applications of Tonelli's Theorem#^thm-26-5|Theorem §26.5: The Subgraph Theorem]]
- [[§26 Applications of Tonelli's Theorem#^thm-26-7|Theorem §26.7: Layer Cake Formula (Cavalieri's Principle)]]
- [[§30 Differentiating the Integral#^lem-30-6|Lemma §30.6: Averaging Lemma]]

## Connections
- **Proof idea.** Show that the [[§25 Invariance Properties and Fubini's Theorem#^def-25-2|Tonelli class]] contains every nonnegative measurable f by climbing, using the closure properties of [[§25 Invariance Properties and Fubini's Theorem#^lem-25-5|Lemma §25.5]]. The steps are: rectangles; open sets as disjoint unions of dyadic cubes ([[§7 Structure of Open Sets#^prop-7-3|§7.3]]); G_δ sets as decreasing limits; null sets; measurable sets as E = H ∖ Z ([[Outer Regularity of Lebesgue Measure]]); simple functions; and finally increasing limits ([[Simple Function Approximation Theorem]], MCT).
- **Riemann vs Lebesgue.** The MATH 452 counterparts are [[§23 Fubini's Theorem#^thm-23-5|Fubini–Tonelli for non-negative functions]] (452 §15.12) and the Riemann [[Fubini's Theorem]] (452 §15.8) for continuous f on rectangles. Here f needs no continuity or boundedness, the value +∞ is allowed, and the slice statements hold for a.e. x.
- **Used for.** [[Fubini's Theorem (Lebesgue)]] applies it to |f|, f⁺ and f⁻. It also gives the [[§26 Applications of Tonelli's Theorem#^thm-26-1|Cross-Section Theorem]] (Cavalieri: m(E) = ∫m(E_x) dx), [[§26 Applications of Tonelli's Theorem#^thm-26-3|Measurability of Product Sets]], the [[§26 Applications of Tonelli's Theorem#^thm-26-5|Subgraph Theorem]], the [[§26 Applications of Tonelli's Theorem#^thm-26-7|Layer Cake Formula]] and the [[§30 Differentiating the Integral#^lem-30-6|Averaging Lemma]].
- **Technique.** [[Measure Theory Problem-Solving Techniques#^rem-19-21|Technique 17: Tonelli Swap for Integral Identities]]. Only measurability and nonnegativity need checking before swapping.
