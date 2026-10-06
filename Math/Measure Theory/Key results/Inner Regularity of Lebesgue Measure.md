---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 13.3", "approximation by closed sets", "F_σ approximation"]
tags: [measure-theory, hub]
---
![[§13 Approximation and Continuity of Measure#^thm-13-3]]

## Treated in
- [[§13 Approximation and Continuity of Measure#^thm-13-3|Theorem §13.3: Approximation by Closed and F_σ Sets]], in [[§13 Approximation and Continuity of Measure]]

## Its proof uses
- [[§5 Topology of ℝⁿ#^def-5-3|Definition §5.3: Closed Set]]
- [[§10 Lebesgue Outer Measure#^prop-10-1|Proposition §10.1: Basic Properties of Outer Measure]]
- [[§11 Lebesgue Measurable Sets#^thm-11-1|Theorem §11.1: Closure Properties of ℳ]]
- [[§13 Approximation and Continuity of Measure#^thm-13-1|Theorem §13.1: Approximation by Open and G_δ Sets]]
- [[§13 Approximation and Continuity of Measure#^def-13-2|Definition §13.2: F_σ Sets]]

## Used in (Measure Theory)
- [[§13 Approximation and Continuity of Measure#^thm-13-6|Theorem §13.6: Approximation by Bounded Closed Sets and Finite Unions of Rectangles]]
- [[§18 Egorov's and Lusin's Theorems#^thm-18-3|Theorem §18.3: Lusin's Theorem]]
- [[§22 The General Lebesgue Integral#^ex-22-2|Example §22.2: Application: Vanishing Integrals over Intervals]]
- [[§26 Applications of Tonelli's Theorem#^thm-26-3|Theorem §26.3: Measurability of Product Sets]]
- [[§30 Differentiating the Integral#^thm-30-2|Theorem §30.2: Continuous Maps Preserving Null Sets Preserve Measurability]]

## Connections
- **Proof idea.** Apply [[Outer Regularity of Lebesgue Measure]] to Eᶜ. An open G ⊇ Eᶜ with m(G ∖ Eᶜ) < ε gives the closed set F = Gᶜ ⊆ E with m(E ∖ F) < ε. Taking ε = 1/n and a union gives the F_σ set of (2) ([[Measure Theory Problem-Solving Techniques#^rem-19-16|Technique 12]]).
- **Compactness.** When m(E) < ∞, cutting off by large cubes makes F bounded ([[§13 Approximation and Continuity of Measure#^thm-13-6|Theorem §13.6]]), hence compact by [[Heine–Borel Theorem|Heine–Borel]]. Finite subcovers then apply ([[Measure Theory Problem-Solving Techniques#^rem-19-9|Technique 5]]).
- **Used for.** [[Lusin's Theorem]], which needs closed pieces of each level set, and [[§26 Applications of Tonelli's Theorem#^thm-26-3|Measurability of Product Sets]] (§26.3). It is also used in [[§30 Differentiating the Integral#^thm-30-2|Continuous Maps Preserving Null Sets Preserve Measurability]] (§30.2), which needs compact pieces because their continuous images are compact ([[Continuous Image of a Compact Space is Compact]]) and so closed ([[Compact Subspace of a Hausdorff Space is Closed]]).
- **Borel vs Lebesgue.** Every measurable set is an F_σ set plus a null set, so ℳ differs from the Borel sets only by null sets ([[§12 Borel Sets and Measure Spaces#^rem-12-2|Rem. §11.2]]).
