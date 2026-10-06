---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 24.7", "density of C_c in L¹"]
tags: [measure-theory, hub]
---
![[§24 The L¹ Space and Density Theorems#^thm-24-7]]

## Treated in
- [[§24 The L¹ Space and Density Theorems#^thm-24-7|Theorem §24.7: Compactly Supported Continuous Functions are Dense in L¹]], in [[§24 The L¹ Space and Density Theorems]]

## Its proof uses
- [[§10 Lebesgue Outer Measure#^def-10-1|Definition §10.1: Rectangles in ℝⁿ]]
- [[§17 Simple Functions and Modes of Convergence#^def-17-2|Definition §17.2: Support of a Function]]
- [[§22 The General Lebesgue Integral#^prop-22-1|Proposition §22.1: Basic Properties]]
- [[§24 The L¹ Space and Density Theorems#^thm-24-4|Theorem §24.4: L¹ is a Normed Vector Space]]
- [[§24 The L¹ Space and Density Theorems#^thm-24-6|Theorem §24.6: Step Functions are Dense in L¹]]
- [[§25 Invariance Properties and Fubini's Theorem#^thm-25-3|Theorem §25.3: Tonelli's Theorem]]

## Its proof uses (other subjects)
- [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3: Properties of the Absolute Value]]

## Used in (Measure Theory)
- [[§25 Invariance Properties and Fubini's Theorem#^thm-25-2|Theorem §25.2: Average Continuity]]
- [[§35 Lᵖ as a Banach Space#^thm-35-12|Theorem §35.12: Density in Lᵖ]]

## Connections
- **Proof idea.** [[§24 The L¹ Space and Density Theorems#^thm-24-6|Step functions are dense]] (§24.6), so by linearity it is enough to approximate one χ_R. In one variable, replace χ_(a,b) by a trapezoid that is 1 inside and linear on two short transition intervals. For a rectangle in ℝⁿ, take the product of these one-variable functions.
- **Uniform vs L¹.** A uniform limit of continuous functions is continuous ([[§24 Uniform Convergence#^thm-24-2|451 §24.2]], [[§17 Simple Functions and Modes of Convergence#^thm-17-4|§17.4]]), so χ_[0,1] is not such a limit. The density holds only for the L¹ distance (and Lᵖ, p < ∞), and it fails in L∞ ([[§35 Lᵖ as a Banach Space#^rem-35-4|Rem. §19.4]]). The pointwise counterpart is [[Lusin's Theorem]].
- **Used for.** It gives [[§25 Invariance Properties and Fubini's Theorem#^thm-25-2|Average Continuity]] (§25.2), where g ∈ C_c is uniformly continuous because its support is compact ([[Heine–Borel Theorem]]). That feeds the [[§30 Differentiating the Integral#^lem-30-6|Averaging Lemma]] and [[§30 Differentiating the Integral#^thm-30-7|Differentiation of the Integral]]. The Lᵖ version is [[§35 Lᵖ as a Banach Space#^thm-35-12|Theorem §35.12]](iii).
- **Technique.** It is the last link of the approximation chain ([[§24 The L¹ Space and Density Theorems#^rem-24-1|Rem. §16.1]]) used in [[Measure Theory Problem-Solving Techniques#^rem-19-19|Technique 15: Density Bootstrap]].
