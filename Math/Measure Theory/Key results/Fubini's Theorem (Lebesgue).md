---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 17.6", "Fubini–Tonelli"]
tags: [measure-theory, hub]
---
![[§17 Invariance Properties and Fubini's Theorem#^thm-17-6]]

## Treated in
- [[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|Theorem §17.6: Fubini's Theorem]], in [[§17 Invariance Properties and Fubini's Theorem]]

## Its proof uses
- [[§12 Measurable Functions#^prop-12-10|Proposition §12.10: Properties of f⁺ and f⁻]]
- [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|Proposition §14.3: Basic Properties]]
- [[§14 The Lebesgue Integral for Simple Functions#^prop-14-10|Proposition §14.10: Integrability Implies A.E. Finiteness]]
- [[§15 The General Lebesgue Integral#^def-15-1|Definition §15.1: Lebesgue Integral of a General Measurable Function]]
- [[§15 The General Lebesgue Integral#^thm-15-2|Theorem §15.2: Linearity]]
- [[§17 Invariance Properties and Fubini's Theorem#^thm-17-3|Theorem §17.3: Tonelli's Theorem]]

## Used in (Measure Theory)
- [[§18 Differentiation Theory#^thm-18-22|Theorem §18.22: Linear Maps Preserve Null Sets]]

## Connections
- **Proof idea.** Apply [[Tonelli's Theorem]] to |f| to get a.e. integrable slices. Then apply it to f⁺ and f⁻ separately and subtract, which is legitimate because both iterated integrals are finite ([[§12 Measurable Functions#^prop-12-10|§12.10]], [[§15 The General Lebesgue Integral#^thm-15-2|linearity]]).
- **Riemann vs Lebesgue.** The MATH 452 [[Fubini's Theorem]] (452 §15.8) is for continuous f on a rectangle, extended to [[§15 Multivariable Integration#^thm-15-9|Type I regions]], and is proved with Riemann sums and uniform continuity. Here f is only integrable on ℝᵖ × ℝ^q, the slices are integrable only for a.e. x, and Jordan content is replaced by Lebesgue measure.
- **Where hypotheses matter.** Integrability cannot be dropped. For (x² − y²)/(x² + y²)² on the unit square the two iterated integrals are −π/4 and π/4 ([[§17 Invariance Properties and Fubini's Theorem#^rem-17-3|Rem. §17.3]], [[§15 Multivariable Integration#^ex-15-2|452 Ex. §15.2]]). In practice, check ∬|f| < ∞ with Tonelli first ([[Measure Theory Problem-Solving Techniques#^rem-19-21|Technique 17: Tonelli Swap]]).
- **Used for.** The volume of sheared rectangles in [[§18 Differentiation Theory#^thm-18-22|Linear Maps Preserve Null Sets]] (§18.22), the measure-side counterpart of the volume scaling in [[9C Determinants#^ladr-9-61|LADR 9.61]] and of the linear case of the 452 [[Change of Variables Formula (multiple integrals)]].
