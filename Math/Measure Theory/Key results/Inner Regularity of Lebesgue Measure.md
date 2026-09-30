---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 11.10", "approximation by closed sets", "F_σ approximation"]
tags: [measure-theory, hub]
---
![[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-10]]

## Treated in
- [[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-10|Theorem §11.10: Approximation by Closed and F_σ Sets]], in [[Measure Theory §11 Borel Sets and Measure Spaces]]

## Its proof uses
- [[Measure Theory §5 Topology of ℝⁿ#^def-5-3|Definition §5.3: Closed Set]]
- [[Measure Theory §9 Lebesgue Outer Measure#^prop-9-1|Proposition §9.1: Basic Properties of Outer Measure]]
- [[Measure Theory §10 Lebesgue Measurable Sets#^thm-10-1|Theorem §10.1: Closure Properties of ℳ]]
- [[Measure Theory §11 Borel Sets and Measure Spaces#^def-11-8|Definition §11.8: G_δ and F_σ Sets]]
- [[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-8|Theorem §11.8: Approximation by Open and G_δ Sets]]

## Used in (Measure Theory)
- [[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-11|Theorem §11.11: Approximation by Bounded Closed Sets and Finite Unions of Rectangles]]
- [[Measure Theory §13 Egorov's and Lusin's Theorems#^thm-13-3|Theorem §13.3: Lusin's Theorem]]
- [[Measure Theory §15 The General Lebesgue Integral#^ex-15-2|Example §15.2: Application: Vanishing Integrals over Intervals]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-8|Theorem §17.8: Measurability of Product Sets]]
- [[Measure Theory §18 Differentiation Theory#^thm-18-21|Theorem §18.21: Continuous Maps Preserving Null Sets Preserve Measurability]]

## Connections
- **Proof idea.** Apply [[Outer Regularity of Lebesgue Measure]] to Eᶜ. An open G ⊇ Eᶜ with m(G ∖ Eᶜ) < ε gives the closed set F = Gᶜ ⊆ E with m(E ∖ F) < ε. Taking ε = 1/n and a union gives the F_σ set of (2) ([[Measure Theory — Problem-Solving Techniques#^rem-19-16|Technique 12]]).
- **Compactness.** When m(E) < ∞, cutting off by large cubes makes F bounded ([[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-11|Theorem §11.11]]), hence compact by [[Heine–Borel Theorem|Heine–Borel]]. Finite subcovers then apply ([[Measure Theory — Problem-Solving Techniques#^rem-19-9|Technique 5]]).
- **Used for.** [[Lusin's Theorem]], which needs closed pieces of each level set, and [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-8|Measurability of Product Sets]] (§17.8). It is also used in [[Measure Theory §18 Differentiation Theory#^thm-18-21|Continuous Maps Preserving Null Sets Preserve Measurability]] (§18.21), which needs compact pieces because their continuous images are compact ([[Continuous Image of a Compact Space is Compact]]) and so closed ([[Compact Subspace of a Hausdorff Space is Closed]]).
- **Borel vs Lebesgue.** Every measurable set is an F_σ set plus a null set, so ℳ differs from the Borel sets only by null sets ([[Measure Theory §11 Borel Sets and Measure Spaces#^rem-11-2|Rem. §11.2]]).
