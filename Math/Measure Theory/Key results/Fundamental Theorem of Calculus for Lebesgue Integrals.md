---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 18.13", "Lebesgue FTC"]
tags: [measure-theory, hub]
---
![[Measure Theory §18 Differentiation Theory#^thm-18-13]]

## Treated in
- [[Measure Theory §18 Differentiation Theory#^thm-18-13|Theorem §18.13: The Fundamental Theorem of Calculus for Lebesgue Integrals]], in [[Measure Theory §18 Differentiation Theory]]

## Its proof uses
- [[Measure Theory §18 Differentiation Theory#^cor-18-10|Corollary §18.10: BV Functions are Differentiable A.E.]]
- [[Measure Theory §18 Differentiation Theory#^prop-18-11|Proposition §18.11: Basic Properties of AC Functions]]
- [[Measure Theory §18 Differentiation Theory#^thm-18-12|Theorem §18.12: The Integral Function is Absolutely Continuous]]
- [[Measure Theory §18 Differentiation Theory#^thm-18-16|Theorem §18.16: AC ⇒ BV]]
- [[Measure Theory §18 Differentiation Theory#^thm-18-26|Theorem §18.26: Differentiation of the Integral]]
- [[Measure Theory §18 Differentiation Theory#^thm-18-27|Theorem §18.27]]

## Used in (Measure Theory)
- [[Measure Theory §18 Differentiation Theory#^cor-18-14|Corollary §18.14: Term-by-Term Differentiation of AC Series]]
- [[Measure Theory §18 Differentiation Theory#^thm-18-15|Theorem §18.15: Lebesgue Decomposition of Increasing Functions]]
- [[Measure Theory §18 Differentiation Theory#^thm-18-19|Theorem §18.19: AC Functions Map Null Sets to Null Sets]]

## Connections
- **Proof idea.** AC ⇒ BV ([[Measure Theory §18 Differentiation Theory#^thm-18-16|§18.16]]), so f′ exists a.e. and is integrable ([[Measure Theory §18 Differentiation Theory#^cor-18-10|§18.10]]). Then F = f − f(a) − ∫ₐˣ f′ is AC ([[Measure Theory §18 Differentiation Theory#^thm-18-12|§18.12]]), F′ = 0 a.e. by [[Measure Theory §18 Differentiation Theory#^thm-18-26|Differentiation of the Integral]] (§18.26), and F is constant by [[Measure Theory §18 Differentiation Theory#^thm-18-27|Theorem §18.27]]. This completes the chain Vitali covering → Lebesgue differentiation → FTC.
- **Riemann vs Lebesgue.** In the MATH 451 [[Fundamental Theorem of Calculus]], FTC I needs f differentiable everywhere with Riemann-integrable f′, and FTC II gives F′ = f at points of continuity. Here absolute continuity replaces “differentiable everywhere”. The 451 step “f′ = 0 ⇒ constant” ([[Single Variable Analysis §29 The Mean Value Theorem#^cor-29-4|451 §29.4]], from the [[Mean Value Theorem]]) needs AC once f′ = 0 only a.e.
- **Where hypotheses matter.** BV and continuity are not enough. The [[Measure Theory §18 Differentiation Theory#^ex-18-4|Cantor function]] is continuous and increasing with φ′ = 0 a.e., yet φ(1) − φ(0) = 1. [[Measure Theory §18 Differentiation Theory#^thm-18-15|Lebesgue Decomposition]] (§18.15) splits such a singular part off an increasing function.
- **Used for.** [[Measure Theory §18 Differentiation Theory#^cor-18-14|Term-by-term differentiation of AC series]] (§18.14) and [[Measure Theory §18 Differentiation Theory#^thm-18-19|AC Functions Map Null Sets to Null Sets]] (§18.19). It is also the tool of [[Measure Theory — Problem-Solving Techniques#^rem-19-25|Technique 21: FTC + MCT for Series of Monotone AC Functions]].
