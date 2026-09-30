---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 15.8", "Fubini"]
tags: [multivariable-analysis, hub]
---
![[Multivariable Analysis §15 Multivariable Integration#^thm-15-8]]

## Treated in
- [[Multivariable Analysis §15 Multivariable Integration#^thm-15-8|Theorem §15.8: Fubini's Theorem — Rectangle Case]], in [[Multivariable Analysis §15 Multivariable Integration]]

## Its proof uses
- [[Multivariable Analysis §15 Multivariable Integration#^rem-15-6|Remark: Evaluating the Integral]]
- [[Multivariable Analysis §15 Multivariable Integration#^def-15-11|Definition §15.11: The Integral]]

## Its proof uses (other subjects)
- [[Single Variable Analysis §32 The Definition of the Riemann Integral#^def-32-3|451 §32.3: Mesh; Riemann Sums; Riemann Integrability]]
- [[Single Variable Analysis §32 The Definition of the Riemann Integral#^thm-32-7|451 §32.7: Continuous Functions Are Integrable]]
- [[Heine–Borel Theorem]] (Topology)
- [[Topology §15 Compact Spaces#^rem-15-1|590 Remark: Why Compactness Matters]]

## Used in (Multivariable Analysis)
- [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|Theorem §15.9: Fubini for Type I Regions]]

## Connections
- **Proof idea.** The double Riemann sum over a grid is the iterated Riemann sum. The inner integrals exist because continuous functions are integrable ([[Single Variable Analysis §32 The Definition of the Riemann Integral#^thm-32-7|451 §32.7]]). Passing to the limit uses uniform continuity of f on the compact rectangle ([[Heine–Borel Theorem]], [[Topology §15 Compact Spaces#^rem-15-1|Why Compactness Matters]]).
- **Where hypotheses matter.** Without absolute integrability the two iterated integrals can differ. For (x² − y²)/(x² + y²)² on (0, 1]² they are π/4 and −π/4 ([[Multivariable Analysis §15 Multivariable Integration#^ex-15-2|Example §15.2]]). For f ≥ 0, see [[Multivariable Analysis §15 Multivariable Integration#^thm-15-12|Fubini–Tonelli]].
- **Extensions.** [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|Type I]] and [[Multivariable Analysis §15 Multivariable Integration#^thm-15-10|Type II]] regions, and [[Multivariable Analysis §15 Multivariable Integration#^cor-15-11|changing the order of integration]]. It is also used to compute the [[Multivariable Analysis §15 Multivariable Integration#^thm-15-7|polar change of variables]] (§15.7).
- **Used for.** The Type I/II form, with the [[Fundamental Theorem of Calculus]] in the inner variable, proves [[Green's Theorem]] and, one dimension up, the [[Divergence Theorem in ℝⁿ]] and [[Divergence Theorem in ℝ³]].
