---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 32.1", "Lebesgue FTC"]
tags: [measure-theory, hub]
---
![[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-32-1]]

## Treated in
- [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-32-1|Theorem §32.1: The Fundamental Theorem of Calculus for Lebesgue Integrals]], in [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals]]

## Its proof uses
- [[§29 Lebesgue's Differentiation Theorem#^cor-29-2|Corollary §29.2: BV Functions are Differentiable A.E.]]
- [[§30 Differentiating the Integral#^thm-30-7|Theorem §30.7: Differentiation of the Integral]]
- [[§31 Absolute Continuity#^prop-31-1|Proposition §31.1: Basic Properties of AC Functions]]
- [[§31 Absolute Continuity#^thm-31-2|Theorem §31.2: The Integral Function is Absolutely Continuous]]
- [[§31 Absolute Continuity#^thm-31-3|Theorem §31.3: AC ⇒ BV]]
- [[§31 Absolute Continuity#^thm-31-4|Theorem §31.4]]

## Used in (Measure Theory)
- [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^cor-32-2|Corollary §32.2: Term-by-Term Differentiation of AC Series]]
- [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-32-6|Theorem §32.6: AC Functions Map Null Sets to Null Sets]]

## Connections
- **Proof idea.** AC ⇒ BV ([[§31 Absolute Continuity#^thm-31-3|§31.3]]), so f′ exists a.e. and is integrable ([[§29 Lebesgue's Differentiation Theorem#^cor-29-2|§29.2]]). Then F = f − f(a) − ∫ₐˣ f′ is AC ([[§31 Absolute Continuity#^thm-31-2|§31.2]]), F′ = 0 a.e. by [[§30 Differentiating the Integral#^thm-30-7|Differentiation of the Integral]] (§18.26), and F is constant by [[§31 Absolute Continuity#^thm-31-4|Theorem §31.4]]. This completes the chain Vitali covering → Lebesgue differentiation → FTC.
- **Riemann vs Lebesgue.** In the MATH 451 [[Fundamental Theorem of Calculus]], FTC I needs f differentiable everywhere with Riemann-integrable f′, and FTC II gives F′ = f at points of continuity. Here absolute continuity replaces “differentiable everywhere”. The 451 step “f′ = 0 ⇒ constant” ([[§29 The Mean Value Theorem#^cor-29-4|451 §29.4]], from the [[Mean Value Theorem]]) needs AC once f′ = 0 only a.e.
- **Where hypotheses matter.** BV and continuity are not enough. The [[§31 Absolute Continuity#^ex-31-1|Cantor function]] is continuous and increasing with φ′ = 0 a.e., yet φ(1) − φ(0) = 1. [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-32-3|Lebesgue Decomposition]] (§18.15) splits such a singular part off an increasing function.
- **Used for.** [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^cor-32-2|Term-by-term differentiation of AC series]] (§18.14) and [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-32-6|AC Functions Map Null Sets to Null Sets]] (§18.19). It is also the tool of [[Measure Theory Problem-Solving Techniques#^rem-19-25|Technique 21: FTC + MCT for Series of Monotone AC Functions]].
