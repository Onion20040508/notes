---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 15.8", "Fubini"]
tags: [multivariable-analysis, hub]
---
![[§15 Multivariable Integration#^thm-15-8]]

## Treated in
- [[§15c Fubini's Theorem#^thm-15-8|Theorem §15.8: Fubini's Theorem — Rectangle Case]], in [[§15c Fubini's Theorem]]

## Its proof uses
- [[§15 Multivariable Integration#^rem-15-6|Remark: Evaluating the Integral]]
- [[§15 Multivariable Integration#^def-15-11|Definition §15.11: The Integral]]

## Its proof uses (other subjects)
- [[§32 The Definition of the Riemann Integral#^def-32-new5|451 §32.3: Riemann Integrability]]
- [[§32 The Definition of the Riemann Integral#^thm-32-7|451 §32.7: Continuous Functions Are Integrable]]
- [[Heine–Borel Theorem]] (Topology)
- [[§15 Compact Spaces#^rem-15-1|590 Remark: Why Compactness Matters]]

## Used in (Multivariable Analysis)
- [[§15 Multivariable Integration#^thm-15-9|Theorem §15.9: Fubini for Type I Regions]]

## Connections
- **Proof idea.** The double Riemann sum over a grid is the iterated Riemann sum. The inner integrals exist because continuous functions are integrable ([[§32 The Definition of the Riemann Integral#^thm-32-7|451 §32.7]]). Passing to the limit uses uniform continuity of f on the compact rectangle ([[Heine–Borel Theorem]], [[§15 Compact Spaces#^rem-15-1|Why Compactness Matters]]).
- **Where hypotheses matter.** Without absolute integrability the two iterated integrals can differ. For (x² − y²)/(x² + y²)² on (0, 1]² they are π/4 and −π/4 ([[§15 Multivariable Integration#^ex-15-2|Example §15.2]]). For f ≥ 0, see [[§15 Multivariable Integration#^thm-15-12|Fubini–Tonelli]].
- **Extensions.** [[§15 Multivariable Integration#^thm-15-9|Type I]] and [[§15 Multivariable Integration#^thm-15-10|Type II]] regions, and [[§15 Multivariable Integration#^cor-15-11|changing the order of integration]]. It is also used to compute the [[§15 Multivariable Integration#^thm-15-7|polar change of variables]] (§15.7).
- **Used for.** The Type I/II form, with the [[Fundamental Theorem of Calculus]] in the inner variable, proves [[Green's Theorem]] and, one dimension up, the [[Divergence Theorem in ℝⁿ]] and [[Divergence Theorem in ℝ³]].
- **Lebesgue version.** [[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|551 Thm. §17.6]] for every integrable f, with [[§17 Invariance Properties and Fubini's Theorem#^thm-17-3|551 Thm. §17.3]] (Tonelli) for f ≥ 0; integrability is the hypothesis that rules out [[§15 Multivariable Integration#^ex-15-2|Example §15.2]].
- **Also in [[Calculus]]:** [[§98 Double Integrals Over Rectangles#^thm-98-3|Calc Thm. §98.3]], with Type I and II regions in [[§99 Double Integrals Over General Regions#^thm-99-1|Calc Thm. §99.1]] and [[§99 Double Integrals Over General Regions#^thm-99-2|Calc Thm. §99.2]] (computational treatment with worked examples).
