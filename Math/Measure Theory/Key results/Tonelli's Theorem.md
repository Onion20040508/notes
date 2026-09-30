---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 17.3", "Tonelli"]
tags: [measure-theory, hub]
---
![[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-3]]

## Treated in
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-3|Theorem §17.3: Tonelli's Theorem]], in [[Measure Theory §17 Invariance Properties and Fubini's Theorem]]

## Its proof uses
- [[Measure Theory §7 Structure of Open Sets#^prop-7-3|Proposition §7.3: Open Sets in ℝⁿ as Unions of Rectangles]]
- [[Measure Theory §11 Borel Sets and Measure Spaces#^def-11-8|Definition §11.8: G_δ and F_σ Sets]]
- [[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-8|Theorem §11.8: Approximation by Open and G_δ Sets]]
- [[Measure Theory §12 Measurable Functions#^thm-12-14|Theorem §12.14: Approximation by Simple Functions: Non-negative Case]]
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-8|Theorem §14.8: Linearity of the Integral]]
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-11|Proposition §14.11: Vanishing Integral for Non-Negative Functions]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^def-17-2|Definition §17.2: The Tonelli Class mathcal{F}]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^lem-17-5|Lemma §17.5: Closure Properties of mathcal{F}]]

## Used in (Measure Theory)
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-6|Theorem §17.6: Fubini's Theorem]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-7|Theorem §17.7: Cross-Section Theorem (Restated)]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-8|Theorem §17.8: Measurability of Product Sets]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-11|Theorem §17.11: The Subgraph Theorem]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-13|Theorem §17.13: Layer Cake Formula (Cavalieri's Principle)]]
- [[Measure Theory §18 Differentiation Theory#^lem-18-25|Lemma §18.25: Averaging Lemma]]

## Connections
- **Proof idea.** Show that the [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^def-17-2|Tonelli class]] contains every nonnegative measurable f by climbing, using the closure properties of [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^lem-17-5|Lemma §17.5]]. The steps are: rectangles; open sets as disjoint unions of dyadic cubes ([[Measure Theory §7 Structure of Open Sets#^prop-7-3|§7.3]]); G_δ sets as decreasing limits; null sets; measurable sets as E = H ∖ Z ([[Outer Regularity of Lebesgue Measure]]); simple functions; and finally increasing limits ([[Simple Function Approximation Theorem]], MCT).
- **Riemann vs Lebesgue.** The MATH 452 counterparts are [[Multivariable Analysis §15 Multivariable Integration#^thm-15-12|Fubini–Tonelli for non-negative functions]] (452 §15.12) and the Riemann [[Fubini's Theorem]] (452 §15.8) for continuous f on rectangles. Here f needs no continuity or boundedness, the value +∞ is allowed, and the slice statements hold for a.e. x.
- **Used for.** [[Fubini's Theorem (Lebesgue)]] applies it to |f|, f⁺ and f⁻. It also gives the [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-7|Cross-Section Theorem]] (Cavalieri: m(E) = ∫m(E_x) dx), [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-8|Measurability of Product Sets]], the [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-11|Subgraph Theorem]], the [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-13|Layer Cake Formula]] and the [[Measure Theory §18 Differentiation Theory#^lem-18-25|Averaging Lemma]].
- **Technique.** [[Measure Theory — Problem-Solving Techniques#^rem-19-21|Technique 17: Tonelli Swap for Integral Identities]]. Only measurability and nonnegativity need checking before swapping.
