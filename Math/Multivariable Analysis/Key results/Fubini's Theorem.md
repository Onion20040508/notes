---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 23.1", "Fubini"]
tags: [multivariable-analysis, hub]
---
![[§23 Fubini's Theorem#^thm-23-1]]

## Treated in
- [[§23 Fubini's Theorem#^thm-23-1|Theorem §23.1: Fubini's Theorem — Rectangle Case]], in [[§23 Fubini's Theorem]]

## Its proof uses
- [[§21 The Definition of the Integral#^rem-21-6|Remark: Evaluating the Integral]]
- [[§21 The Definition of the Integral#^def-21-7|Definition §21.7: The Integral]]

## Its proof uses (other subjects)
- [[§32 The Definition of the Riemann Integral#^def-32-8|451 §32.8: Riemann Integrability]]
- [[§32 The Definition of the Riemann Integral#^thm-32-7|451 §32.7: Continuous Functions Are Integrable]]
- [[Heine–Borel Theorem]] (Topology)
- [[§18 Compact Spaces#^rem-18-1|590 Remark: Why Compactness Matters]]

## Used in (Multivariable Analysis)
- [[§23 Fubini's Theorem#^thm-23-2|Theorem §23.2: Fubini for Type I Regions]]

## Connections
- **Proof idea.** The double Riemann sum over a grid is the iterated Riemann sum. The inner integrals exist because continuous functions are integrable ([[§32 The Definition of the Riemann Integral#^thm-32-7|451 §32.7]]). Passing to the limit uses uniform continuity of f on the compact rectangle ([[Heine–Borel Theorem]], [[§18 Compact Spaces#^rem-18-1|Why Compactness Matters]]).
- **Where hypotheses matter.** Without absolute integrability the two iterated integrals can differ. For (x² − y²)/(x² + y²)² on (0, 1]² they are π/4 and −π/4 ([[§23 Fubini's Theorem#^ex-23-2|Example §23.2]]). For f ≥ 0, see [[§23 Fubini's Theorem#^thm-23-5|Fubini–Tonelli]].
- **Extensions.** [[§23 Fubini's Theorem#^thm-23-2|Type I]] and [[§23 Fubini's Theorem#^thm-23-3|Type II]] regions, and [[§23 Fubini's Theorem#^cor-23-4|changing the order of integration]]. It is also used to compute the [[§22 Properties of the Integral#^thm-22-6|polar change of variables]] (§15.7).
- **Used for.** The Type I/II form, with the [[Fundamental Theorem of Calculus]] in the inner variable, proves [[Green's Theorem]] and, one dimension up, the [[Divergence Theorem in ℝⁿ]] and [[Divergence Theorem in ℝ³]].
- **Lebesgue version.** [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 Thm. §25.6]] for every integrable f, with [[§25 Invariance Properties and Fubini's Theorem#^thm-25-3|551 Thm. §25.3]] (Tonelli) for f ≥ 0; integrability is the hypothesis that rules out [[§23 Fubini's Theorem#^ex-23-2|Example §23.2]].
- **Also in [[Calculus]]:** [[§115 Double Integrals Over Rectangles#^thm-115-3|Calc Thm. §115.3]], with Type I and II regions in [[§116 Double Integrals Over General Regions#^thm-116-1|Calc Thm. §116.1]] and [[§116 Double Integrals Over General Regions#^thm-116-2|Calc Thm. §116.2]] (computational treatment with worked examples).
