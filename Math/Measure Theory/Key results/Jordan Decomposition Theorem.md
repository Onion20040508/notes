---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 28.7", "BV = difference of increasing"]
tags: [measure-theory, hub]
---
![[§28 Differentiation Theory#^thm-28-7]]

## Treated in
- [[§28 Differentiation Theory#^thm-28-7|Theorem §28.7: Jordan Decomposition Theorem]], in [[§28 Differentiation Theory]]

## Its proof uses
- [[§28 Differentiation Theory#^ex-28-2|Example §28.2: Monotone Functions are BV]]
- [[§28 Differentiation Theory#^prop-28-4|Proposition §28.4: Properties of BV Functions]]
- [[§28 Differentiation Theory#^prop-28-5|Proposition §28.5: Additivity of Total Variation]]
- [[§28 Differentiation Theory#^cor-28-6|Corollary §28.6: The Variation Function is Increasing]]

## Used in (Measure Theory)
- [[§29 Lebesgue's Differentiation Theorem#^cor-29-2|Corollary §29.2: BV Functions are Differentiable A.E.]]

## Connections
- **Proof idea.** g(x) = total variation of f on [a, x] is increasing ([[§28 Differentiation Theory#^cor-28-6|§28.6]]). h = g − f is increasing because f(x₂) − f(x₁) is at most the variation on [x₁, x₂] ([[§28 Differentiation Theory#^prop-28-5|§28.5]]). Conversely, increasing functions are BV ([[§28 Differentiation Theory#^ex-28-2|Ex. §28.2]]) and BV is a linear space ([[§28 Differentiation Theory#^prop-28-4|§28.4]]).
- **Used for.** It reduces BV to monotone functions. With [[Lebesgue's Differentiation Theorem for Monotone Functions]] it gives [[§29 Lebesgue's Differentiation Theorem#^cor-29-2|BV Functions are Differentiable A.E.]] (§18.10). This is the first step of the [[Fundamental Theorem of Calculus for Lebesgue Integrals]] (AC ⇒ BV ⇒ f′ exists a.e.).
- **Analogues.** It parallels f = f⁺ − f⁻ ([[§16 Limits and Positive Parts of Measurable Functions#^prop-16-5|§16.5]]) and the splitting F = ∫f⁺ − ∫f⁻ of [[§28 Differentiation Theory#^rem-28-1|Rem. §18.1]]. Monotone functions are Riemann integrable ([[§33 Properties of the Riemann Integral#^thm-33-1|451 §33.1]]), so BV functions are too.
- **Where hypotheses matter.** Continuity does not give BV: √x·sin(π/x) is continuous on [0, 1] but has infinite variation ([[§28 Differentiation Theory#^ex-28-3|Ex. §28.3]]).
