---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 25.6", "Fubini–Tonelli"]
tags: [measure-theory, hub]
---
![[§25 Invariance Properties and Fubini's Theorem#^thm-25-6]]

## Treated in
- [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|Theorem §25.6: Fubini's Theorem]], in [[§25 Invariance Properties and Fubini's Theorem]]

## Its proof uses
- [[§16 Limits and Positive Parts of Measurable Functions#^prop-16-5|Proposition §16.5: Properties of f⁺ and f⁻]]
- [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|Proposition §20.3: Basic Properties]]
- [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-3|Proposition §21.3: Integrability Implies A.E. Finiteness]]
- [[§22 The General Lebesgue Integral#^def-22-1|Definition §22.1: Lebesgue Integral of a General Measurable Function]]
- [[§22 The General Lebesgue Integral#^thm-22-2|Theorem §22.2: Linearity]]
- [[§25 Invariance Properties and Fubini's Theorem#^thm-25-3|Theorem §25.3: Tonelli's Theorem]]

## Used in (Measure Theory)
- [[§30 Differentiating the Integral#^thm-30-3|Theorem §30.3: Linear Maps Preserve Null Sets]]

## Connections
- **Proof idea.** Apply [[Tonelli's Theorem]] to |f| to get a.e. integrable slices. Then apply it to f⁺ and f⁻ separately and subtract, which is legitimate because both iterated integrals are finite ([[§16 Limits and Positive Parts of Measurable Functions#^prop-16-5|§16.5]], [[§22 The General Lebesgue Integral#^thm-22-2|linearity]]).
- **Riemann vs Lebesgue.** The MATH 452 [[Fubini's Theorem]] (452 §15.8) is for continuous f on a rectangle, extended to [[§23 Fubini's Theorem#^thm-23-2|Type I regions]], and is proved with Riemann sums and uniform continuity. Here f is only integrable on ℝᵖ × ℝ^q, the slices are integrable only for a.e. x, and Jordan content is replaced by Lebesgue measure.
- **Where hypotheses matter.** Integrability cannot be dropped. For (x² − y²)/(x² + y²)² on the unit square the two iterated integrals are −π/4 and π/4 ([[§25 Invariance Properties and Fubini's Theorem#^rem-25-3|Rem. §17.3]], [[§23 Fubini's Theorem#^ex-23-2|452 Ex. §23.2]]). In practice, check ∬|f| < ∞ with Tonelli first ([[Measure Theory Problem-Solving Techniques#^rem-19-21|Technique 17: Tonelli Swap]]).
- **Used for.** The volume of sheared rectangles in [[§30 Differentiating the Integral#^thm-30-3|Linear Maps Preserve Null Sets]] (§30.3), the measure-side counterpart of the volume scaling in [[§37 Determinants#^ladr-9-61|LADR 9.61]] and of the linear case of the 452 [[Change of Variables Formula (multiple integrals)]].
