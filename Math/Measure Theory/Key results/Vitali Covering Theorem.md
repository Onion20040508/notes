---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 18.2", "Vitali covering lemma"]
tags: [measure-theory, hub]
---
![[§18 Differentiation Theory#^thm-18-2]]

## Treated in
- [[§18 Differentiation Theory#^thm-18-2|Theorem §18.2: Vitali Covering Theorem]], in [[§18 Differentiation Theory]]

## Its proof uses
- [[§9 Lebesgue Outer Measure#^prop-9-1|Proposition §9.1: Basic Properties of Outer Measure]]
- [[§9 Lebesgue Outer Measure#^prop-9-2|Proposition §9.2: Outer Measure of Closed Rectangles]]
- [[§9 Lebesgue Outer Measure#^def-9-4|Definition §9.4: Outer Measure]]
- [[§10 Lebesgue Measurable Sets#^thm-10-3|Theorem §10.3: ℳ is a σ-Algebra with Countable Additivity]]
- [[§18 Differentiation Theory#^def-18-1|Definition §18.1: Vitali Covering]]

## Used in (Measure Theory)
- [[§18 Differentiation Theory#^thm-18-9|Theorem §18.9: Lebesgue's Differentiation Theorem for Monotone Functions]]
- [[§18 Differentiation Theory#^thm-18-27|Theorem §18.27]]

## Connections
- **Proof idea.** Work inside an open G ⊇ E of finite measure. Choose disjoint intervals greedily, each longer than half the longest interval still available. Their lengths are summable, and every point left uncovered after n₀ steps lies in the 5× enlargement ([[§18 Differentiation Theory#^rem-18-2|Rem. §18.2]]) of a later interval. So what is left has outer measure at most 5 times the tail of the series.
- **Compare compactness.** [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|Heine–Borel]] (§6.4; [[Heine–Borel Theorem]]) extracts a finite subcover of a compact set, and the intervals may overlap. Vitali needs no compactness and extracts finitely many disjoint intervals, at the cost of leaving out a set of outer measure < ε.
- **Chain.** Vitali covering → [[Lebesgue's Differentiation Theorem for Monotone Functions]] (used twice) → [[Fundamental Theorem of Calculus for Lebesgue Integrals]]. It also proves [[§18 Differentiation Theory#^thm-18-27|Theorem §18.27]] (a non-constant f with f′ = 0 a.e. is not AC). That result replaces the 451 fact that f′ = 0 everywhere implies f is constant ([[§29 The Mean Value Theorem#^cor-29-4|451 §29.4]]).
