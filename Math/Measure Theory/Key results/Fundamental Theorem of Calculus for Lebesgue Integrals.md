---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 18.13", "Lebesgue FTC"]
tags: [measure-theory, hub]
---
![[§18 Differentiation Theory#^thm-18-13]]

## Treated in
- [[§18 Differentiation Theory#^thm-18-13|Theorem §18.13: The Fundamental Theorem of Calculus for Lebesgue Integrals]], in [[§18 Differentiation Theory]]

## Its proof uses
- [[§18 Differentiation Theory#^cor-18-10|Corollary §18.10: BV Functions are Differentiable A.E.]]
- [[§18 Differentiation Theory#^prop-18-11|Proposition §18.11: Basic Properties of AC Functions]]
- [[§18 Differentiation Theory#^thm-18-12|Theorem §18.12: The Integral Function is Absolutely Continuous]]
- [[§18 Differentiation Theory#^thm-18-16|Theorem §18.16: AC ⇒ BV]]
- [[§18 Differentiation Theory#^thm-18-26|Theorem §18.26: Differentiation of the Integral]]
- [[§18 Differentiation Theory#^thm-18-27|Theorem §18.27]]

## Used in (Measure Theory)
- [[§18 Differentiation Theory#^cor-18-14|Corollary §18.14: Term-by-Term Differentiation of AC Series]]
- [[§18 Differentiation Theory#^thm-18-19|Theorem §18.19: AC Functions Map Null Sets to Null Sets]]

## Connections
- **Proof idea.** AC ⇒ BV ([[§18 Differentiation Theory#^thm-18-16|§18.16]]), so f′ exists a.e. and is integrable ([[§18 Differentiation Theory#^cor-18-10|§18.10]]). Then F = f − f(a) − ∫ₐˣ f′ is AC ([[§18 Differentiation Theory#^thm-18-12|§18.12]]), F′ = 0 a.e. by [[§18 Differentiation Theory#^thm-18-26|Differentiation of the Integral]] (§18.26), and F is constant by [[§18 Differentiation Theory#^thm-18-27|Theorem §18.27]]. This completes the chain Vitali covering → Lebesgue differentiation → FTC.
- **Riemann vs Lebesgue.** In the MATH 451 [[Fundamental Theorem of Calculus]], FTC I needs f differentiable everywhere with Riemann-integrable f′, and FTC II gives F′ = f at points of continuity. Here absolute continuity replaces “differentiable everywhere”. The 451 step “f′ = 0 ⇒ constant” ([[§29 The Mean Value Theorem#^cor-29-4|451 §29.4]], from the [[Mean Value Theorem]]) needs AC once f′ = 0 only a.e.
- **Where hypotheses matter.** BV and continuity are not enough. The [[§18 Differentiation Theory#^ex-18-4|Cantor function]] is continuous and increasing with φ′ = 0 a.e., yet φ(1) − φ(0) = 1. [[§18 Differentiation Theory#^thm-18-15|Lebesgue Decomposition]] (§18.15) splits such a singular part off an increasing function.
- **Used for.** [[§18 Differentiation Theory#^cor-18-14|Term-by-term differentiation of AC series]] (§18.14) and [[§18 Differentiation Theory#^thm-18-19|AC Functions Map Null Sets to Null Sets]] (§18.19). It is also the tool of [[Measure Theory Problem-Solving Techniques#^rem-19-25|Technique 21: FTC + MCT for Series of Monotone AC Functions]].
