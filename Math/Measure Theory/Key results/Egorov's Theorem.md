---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 13.1", "Egoroff"]
tags: [measure-theory, hub]
---
![[§13 Egorov's and Lusin's Theorems#^thm-13-1]]

## Treated in
- [[§13 Egorov's and Lusin's Theorems#^thm-13-1|Theorem §13.1: Egorov's Theorem]], in [[§13 Egorov's and Lusin's Theorems]]

## Its proof uses
- [[§9 Lebesgue Outer Measure#^prop-9-1|Proposition §9.1: Basic Properties of Outer Measure]]
- [[§11 Borel Sets and Measure Spaces#^prop-11-13|Proposition §11.13: Continuity of Measure from Above]]
- [[§12 Measurable Functions#^def-12-2|Definition §12.2: Measurable Function]]
- [[§12 Measurable Functions#^ex-12-3|Example §12.3: Common Uses of “Almost Everywhere”]]
- [[§12 Measurable Functions#^def-12-8|Definition §12.8: Pointwise and Almost Everywhere Convergence]]
- [[§12 Measurable Functions#^def-12-9|Definition §12.9: Uniform Convergence]]
- [[§12 Measurable Functions#^def-12-10|Definition §12.10: Set of Convergence and Divergence]]

## Its proof uses (other subjects)
- [[Archimedean Property]] (Single Variable Analysis)
- [[§14 Series#^ex-14-4|451 §14.4: The Geometric Series]]

## Used in (Measure Theory)
- (not cited later in the course)

## Connections
- **Proof idea.** For each j, the sets ⋃_{k≥ℓ} {|f_k − f| ≥ 1/j} decrease in ℓ to a subset of the [[§12 Measurable Functions#^def-12-10|set of divergence]], which is null. [[§11 Borel Sets and Measure Spaces#^prop-11-13|Continuity from above]] then gives an ℓ_j for which this set has measure < δ/2ʲ. E_δ is the union of these sets over j, and the [[Geometric series|geometric series]] bounds its measure by δ.
- **Where hypotheses matter.** m(E) < ∞ is exactly what continuity from above needs. On ℝ, χ_[k,k+1] → 0 pointwise but not uniformly off any set of finite measure ([[§13 Egorov's and Lusin's Theorems#^rem-13-1|Rem. §13.1]]). The exceptional set cannot be dropped: x^k on [0, 1] converges uniformly on [0, 1 − δ] but not on [0, 1) ([[§13 Egorov's and Lusin's Theorems#^ex-13-1|Ex. §13.1]], [[§24 Uniform Convergence#^ex-24-2|451 Ex. §24.2]]).
- **Uniform vs a.e.** Uniform convergence is the MATH 451 mode ([[§24 Uniform Convergence#^def-24-2|451 Def. §24.2]]) under which Riemann integrals pass to the limit ([[§33 Properties of the Riemann Integral#^thm-33-12|451 §33.12]]). On a set of finite measure, a.e. convergence is uniform off an arbitrarily small set. [[Lusin's Theorem]] follows the same pattern of excising a small bad set ([[§13 Egorov's and Lusin's Theorems#^rem-13-3|Rem. §13.3]]).
- **Techniques.** Applied with δ = 1/n in [[Measure Theory Problem-Solving Techniques#^rem-19-16|Technique 12: Iterated ε-Extraction]] (HW5 P2).
