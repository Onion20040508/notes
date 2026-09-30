---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 18.7", "BV = difference of increasing"]
tags: [measure-theory, hub]
---
![[Measure Theory §18 Differentiation Theory#^thm-18-7]]

## Treated in
- [[Measure Theory §18 Differentiation Theory#^thm-18-7|Theorem §18.7: Jordan Decomposition Theorem]], in [[Measure Theory §18 Differentiation Theory]]

## Its proof uses
- [[Measure Theory §18 Differentiation Theory#^ex-18-2|Example §18.2: Monotone Functions are BV]]
- [[Measure Theory §18 Differentiation Theory#^prop-18-4|Proposition §18.4: Properties of BV Functions]]
- [[Measure Theory §18 Differentiation Theory#^prop-18-5|Proposition §18.5: Additivity of Total Variation]]
- [[Measure Theory §18 Differentiation Theory#^cor-18-6|Corollary §18.6: The Variation Function is Increasing]]

## Used in (Measure Theory)
- [[Measure Theory §18 Differentiation Theory#^cor-18-10|Corollary §18.10: BV Functions are Differentiable A.E.]]

## Connections
- **Proof idea.** g(x) = total variation of f on [a, x] is increasing ([[Measure Theory §18 Differentiation Theory#^cor-18-6|§18.6]]). h = g − f is increasing because f(x₂) − f(x₁) is at most the variation on [x₁, x₂] ([[Measure Theory §18 Differentiation Theory#^prop-18-5|§18.5]]). Conversely, increasing functions are BV ([[Measure Theory §18 Differentiation Theory#^ex-18-2|Ex. §18.2]]) and BV is a linear space ([[Measure Theory §18 Differentiation Theory#^prop-18-4|§18.4]]).
- **Used for.** It reduces BV to monotone functions. With [[Lebesgue's Differentiation Theorem for Monotone Functions]] it gives [[Measure Theory §18 Differentiation Theory#^cor-18-10|BV Functions are Differentiable A.E.]] (§18.10). This is the first step of the [[Fundamental Theorem of Calculus for Lebesgue Integrals]] (AC ⇒ BV ⇒ f′ exists a.e.).
- **Analogues.** It parallels f = f⁺ − f⁻ ([[Measure Theory §12 Measurable Functions#^prop-12-10|§12.10]]) and the splitting F = ∫f⁺ − ∫f⁻ of [[Measure Theory §18 Differentiation Theory#^rem-18-1|Rem. §18.1]]. Monotone functions are Riemann integrable ([[Single Variable Analysis §33 Properties of the Riemann Integral#^thm-33-1|451 §33.1]]), so BV functions are too.
- **Where hypotheses matter.** Continuity does not give BV: √x·sin(π/x) is continuous on [0, 1] but has infinite variation ([[Measure Theory §18 Differentiation Theory#^ex-18-3|Ex. §18.3]]).
