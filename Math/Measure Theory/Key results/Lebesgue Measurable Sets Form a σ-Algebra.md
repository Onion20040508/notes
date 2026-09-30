---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 10.3", "countable additivity of Lebesgue measure"]
tags: [measure-theory, hub]
---
![[Measure Theory §10 Lebesgue Measurable Sets#^thm-10-3]]

## Treated in
- [[Measure Theory §10 Lebesgue Measurable Sets#^thm-10-3|Theorem §10.3: ℳ is a σ-Algebra with Countable Additivity]], in [[Measure Theory §10 Lebesgue Measurable Sets]]

## Its proof uses
- [[Measure Theory §9 Lebesgue Outer Measure#^prop-9-1|Proposition §9.1: Basic Properties of Outer Measure]]
- [[Measure Theory §10 Lebesgue Measurable Sets#^rem-10-1|Remark]]
- [[Measure Theory §10 Lebesgue Measurable Sets#^def-10-1|Definition §10.1: Lebesgue Measurable Set]]
- [[Measure Theory §10 Lebesgue Measurable Sets#^thm-10-1|Theorem §10.1: Closure Properties of ℳ]]
- [[Measure Theory §10 Lebesgue Measurable Sets#^lem-10-2|Lemma §10.2: Finite Additivity for Disjoint Measurable Sets]]
- [[Measure Theory §10 Lebesgue Measurable Sets#^def-10-4|Definition §10.4: σ-Algebra]]

## Used in (Measure Theory)
- [[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-6|Theorem §11.6: Open Sets are Measurable]]
- [[Measure Theory §11 Borel Sets and Measure Spaces#^cor-11-7|Corollary §11.7]]
- [[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-8|Theorem §11.8: Approximation by Open and G_δ Sets]]
- [[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-11|Theorem §11.11: Approximation by Bounded Closed Sets and Finite Unions of Rectangles]]
- [[Measure Theory §11 Borel Sets and Measure Spaces#^prop-11-12|Proposition §11.12: Continuity of Measure from Below]]
- [[Measure Theory §11 Borel Sets and Measure Spaces#^prop-11-13|Proposition §11.13: Continuity of Measure from Above]]
- [[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-20|Theorem §11.20: The Vitali Set is Not Measurable]]
- [[Measure Theory §11 Borel Sets and Measure Spaces#^prop-11-21|Proposition §11.21: Properties of the Cantor Set]]
- [[Measure Theory §12 Measurable Functions#^prop-12-1|Proposition §12.1: Characteristic Functions of Measurable Sets]]
- [[Measure Theory §12 Measurable Functions#^ex-12-2|Example §12.2: Continuous Functions are Measurable]]
- [[Measure Theory §12 Measurable Functions#^prop-12-2|Proposition §12.2: Equivalent Conditions for Measurability]]
- [[Measure Theory §12 Measurable Functions#^thm-12-3|Theorem §12.3: Arithmetic Operations Preserve Measurability]]
- [[Measure Theory §12 Measurable Functions#^prop-12-4|Proposition §12.4: Union of Domains]]
- [[Measure Theory §12 Measurable Functions#^prop-12-5|Proposition §12.5: Restriction to Measurable Subsets]]
- [[Measure Theory §12 Measurable Functions#^thm-12-6|Theorem §12.6: Measurability of Suprema and Infima]]
- [[Measure Theory §12 Measurable Functions#^prop-12-9|Proposition §12.9: Measurability of 1/f]]
- [[Measure Theory §12 Measurable Functions#^prop-12-12|Proposition §12.12: Functions Equal a.e. to Measurable Functions]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-8|Theorem §17.8: Measurability of Product Sets]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^cor-17-10|Corollary §17.10: The Graph Has Measure Zero]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-11|Theorem §17.11: The Subgraph Theorem]]
- [[Measure Theory §18 Differentiation Theory#^thm-18-2|Theorem §18.2: Vitali Covering Theorem]]
- [[Measure Theory §18 Differentiation Theory#^thm-18-9|Theorem §18.9: Lebesgue's Differentiation Theorem for Monotone Functions]]
- [[Measure Theory §18 Differentiation Theory#^thm-18-21|Theorem §18.21: Continuous Maps Preserving Null Sets Preserve Measurability]]

## Connections
- **Proof idea.** For disjoint E_j, split a test set T along E₁ ∪ … ∪ E_k with [[Measure Theory §10 Lebesgue Measurable Sets#^lem-10-2|Lemma §10.2]]. Let k → ∞ and use subadditivity ([[Properties of Lebesgue Outer Measure]]) to get the Carathéodory inequality for ⋃E_j. Taking T = ⋃E_j gives countable additivity. General unions are first made disjoint using [[Measure Theory §10 Lebesgue Measurable Sets#^thm-10-1|§10.1]].
- **Chain.** Outer measure (§9.1) → [[Measure Theory §10 Lebesgue Measurable Sets#^def-10-1|Carathéodory criterion]] → σ-algebra with countable additivity. The same argument for any outer measure is [[Carathéodory's Theorem]]. The result makes (ℝⁿ, ℳ, m) a [[Measure Theory §11 Borel Sets and Measure Spaces#^def-11-7|measure space]] and gives [[Continuity of Measure]].
- **Jordan vs Lebesgue.** The Jordan content of MATH 452 ([[Multivariable Analysis §15 Multivariable Integration#^def-15-4|452 Def. §15.4]]) uses finite grids and is only finitely additive ([[Multivariable Analysis §15 Multivariable Integration#^thm-15-1|452 §15.1]]). ℚ ∩ [0, 1] is Lebesgue-null ([[Measure Theory §9 Lebesgue Outer Measure#^ex-9-2|Ex. §9.2]]) but not Jordan measurable, since its inner content is 0 and its outer content is 1.
- **Scope.** With [[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-6|open sets measurable]] it gives Borel ⊆ ℳ ([[Measure Theory §11 Borel Sets and Measure Spaces#^cor-11-7|§11.7]]), but ℳ ≠ 𝒫(ℝ): [[The Vitali Set is Not Measurable]]. A σ-algebra is closed under complements and countable unions, while a topology is closed under arbitrary unions and finite intersections ([[Topology §1 Topological Spaces#^def-1-1|590 Def. §1.1]]).
