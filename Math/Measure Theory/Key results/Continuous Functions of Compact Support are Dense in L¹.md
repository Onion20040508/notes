---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 16.7", "density of C_c in L¹"]
tags: [measure-theory, hub]
---
![[Measure Theory §16 The L¹ Space and Density Theorems#^thm-16-7]]

## Treated in
- [[Measure Theory §16 The L¹ Space and Density Theorems#^thm-16-7|Theorem §16.7: Compactly Supported Continuous Functions are Dense in L¹]], in [[Measure Theory §16 The L¹ Space and Density Theorems]]

## Its proof uses
- [[Measure Theory §9 Lebesgue Outer Measure#^def-9-1|Definition §9.1: Rectangles in ℝⁿ]]
- [[Measure Theory §12 Measurable Functions#^def-12-7|Definition §12.7: Support of a Function]]
- [[Measure Theory §15 The General Lebesgue Integral#^prop-15-1|Proposition §15.1: Basic Properties]]
- [[Measure Theory §16 The L¹ Space and Density Theorems#^thm-16-4|Theorem §16.4: L¹ is a Normed Vector Space]]
- [[Measure Theory §16 The L¹ Space and Density Theorems#^thm-16-6|Theorem §16.6: Step Functions are Dense in L¹]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-3|Theorem §17.3: Tonelli's Theorem]]

## Its proof uses (other subjects)
- [[Single Variable Analysis §3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3: Properties of the Absolute Value]]

## Used in (Measure Theory)
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-2|Theorem §17.2: Average Continuity]]
- [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|Theorem §19.19: Density in Lᵖ]]

## Connections
- **Proof idea.** [[Measure Theory §16 The L¹ Space and Density Theorems#^thm-16-6|Step functions are dense]] (§16.6), so by linearity it is enough to approximate one χ_R. In one variable, replace χ_(a,b) by a trapezoid that is 1 inside and linear on two short transition intervals. For a rectangle in ℝⁿ, take the product of these one-variable functions.
- **Uniform vs L¹.** A uniform limit of continuous functions is continuous ([[Single Variable Analysis §24 Uniform Convergence#^thm-24-2|451 §24.2]], [[Measure Theory §12 Measurable Functions#^thm-12-16|§12.16]]), so χ_[0,1] is not such a limit. The density holds only for the L¹ distance (and Lᵖ, p < ∞), and it fails in L∞ ([[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^rem-19-4|Rem. §19.4]]). The pointwise counterpart is [[Lusin's Theorem]].
- **Used for.** It gives [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-2|Average Continuity]] (§17.2), where g ∈ C_c is uniformly continuous because its support is compact ([[Heine–Borel Theorem]]). That feeds the [[Measure Theory §18 Differentiation Theory#^lem-18-25|Averaging Lemma]] and [[Measure Theory §18 Differentiation Theory#^thm-18-26|Differentiation of the Integral]]. The Lᵖ version is [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|Theorem §19.19]](iii).
- **Technique.** It is the last link of the approximation chain ([[Measure Theory §16 The L¹ Space and Density Theorems#^rem-16-1|Rem. §16.1]]) used in [[Measure Theory — Problem-Solving Techniques#^rem-19-19|Technique 15: Density Bootstrap]].
