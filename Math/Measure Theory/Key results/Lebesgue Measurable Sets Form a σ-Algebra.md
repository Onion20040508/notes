---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 11.3", "countable additivity of Lebesgue measure"]
tags: [measure-theory, hub]
---
![[§11 Lebesgue Measurable Sets#^thm-11-3]]

## Treated in
- [[§11 Lebesgue Measurable Sets#^thm-11-3|Theorem §11.3: ℳ is a σ-Algebra with Countable Additivity]], in [[§11 Lebesgue Measurable Sets]]

## Its proof uses
- [[§10 Lebesgue Outer Measure#^prop-10-1|Proposition §10.1: Basic Properties of Outer Measure]]
- [[§11 Lebesgue Measurable Sets#^def-11-1|Definition §11.1: Lebesgue Measurable Set]]
- [[§11 Lebesgue Measurable Sets#^rem-11-1|Remark]]
- [[§11 Lebesgue Measurable Sets#^thm-11-1|Theorem §11.1: Closure Properties of ℳ]]
- [[§11 Lebesgue Measurable Sets#^lem-11-2|Lemma §11.2: Finite Additivity for Disjoint Measurable Sets]]
- [[§11 Lebesgue Measurable Sets#^def-11-4|Definition §11.4: σ-Algebra]]

## Used in (Measure Theory)
- [[§12 Borel Sets and Measure Spaces#^thm-12-6|Theorem §12.6: Open Sets are Measurable]]
- [[§12 Borel Sets and Measure Spaces#^cor-12-7|Corollary §12.7]]
- [[§13 Approximation and Continuity of Measure#^thm-13-1|Theorem §13.1: Approximation by Open and G_δ Sets]]
- [[§13 Approximation and Continuity of Measure#^thm-13-6|Theorem §13.6: Approximation by Bounded Closed Sets and Finite Unions of Rectangles]]
- [[§13 Approximation and Continuity of Measure#^prop-13-4|Proposition §13.4: Continuity of Measure from Below]]
- [[§13 Approximation and Continuity of Measure#^prop-13-5|Proposition §13.5: Continuity of Measure from Above]]
- [[§14 The Vitali Set and the Cantor Set#^thm-14-6|Theorem §14.6: The Vitali Set is Not Measurable]]
- [[§14 The Vitali Set and the Cantor Set#^prop-14-7|Proposition §14.7: Properties of the Cantor Set]]
- [[§15 Measurable Functions#^prop-15-1|Proposition §15.1: Characteristic Functions of Measurable Sets]]
- [[§15 Measurable Functions#^prop-15-2|Proposition §15.2: Equivalent Conditions for Measurability]]
- [[§15 Measurable Functions#^thm-15-3|Theorem §15.3: Arithmetic Operations Preserve Measurability]]
- [[§15 Measurable Functions#^prop-15-4|Proposition §15.4: Union of Domains]]
- [[§15 Measurable Functions#^prop-15-5|Proposition §15.5: Restriction to Measurable Subsets]]
- [[§16 Limits and Positive Parts of Measurable Functions#^thm-16-1|Theorem §16.1: Measurability of Suprema and Infima]]
- [[§16 Limits and Positive Parts of Measurable Functions#^prop-16-4|Proposition §16.4: Measurability of 1/f]]
- [[§16 Limits and Positive Parts of Measurable Functions#^prop-16-7|Proposition §16.7: Functions Equal a.e. to Measurable Functions]]
- [[§26 Applications of Tonelli's Theorem#^thm-26-3|Theorem §26.3: Measurability of Product Sets]]
- [[§26 Applications of Tonelli's Theorem#^cor-26-4|Corollary §26.4: The Graph Has Measure Zero]]
- [[§26 Applications of Tonelli's Theorem#^thm-26-5|Theorem §26.5: The Subgraph Theorem]]
- [[§28 Differentiation Theory#^thm-28-2|Theorem §28.2: Vitali Covering Theorem]]
- [[§29 Lebesgue's Differentiation Theorem#^thm-29-1|Theorem §29.1: Lebesgue's Differentiation Theorem for Monotone Functions]]
- [[§30 Differentiating the Integral#^thm-30-2|Theorem §30.2: Continuous Maps Preserving Null Sets Preserve Measurability]]

## Connections
- **Proof idea.** For disjoint E_j, split a test set T along E₁ ∪ … ∪ E_k with [[§11 Lebesgue Measurable Sets#^lem-11-2|Lemma §11.2]]. Let k → ∞ and use subadditivity ([[Properties of Lebesgue Outer Measure]]) to get the Carathéodory inequality for ⋃E_j. Taking T = ⋃E_j gives countable additivity. General unions are first made disjoint using [[§11 Lebesgue Measurable Sets#^thm-11-1|§11.1]].
- **Chain.** Outer measure (§9.1) → [[§11 Lebesgue Measurable Sets#^def-11-1|Carathéodory criterion]] → σ-algebra with countable additivity. The same argument for any outer measure is [[Carathéodory's Theorem]]. The result makes (ℝⁿ, ℳ, m) a [[§12 Borel Sets and Measure Spaces#^def-12-7|measure space]] and gives [[Continuity of Measure]].
- **Jordan vs Lebesgue.** The Jordan content of MATH 452 ([[§20 Multivariable Integration#^def-20-5|452 Def. §20.5]], [[§20 Multivariable Integration#^def-20-6|452 Def. §20.6]]) uses finite grids and is only finitely additive ([[§20 Multivariable Integration#^thm-20-1|452 §20.1]]). ℚ ∩ [0, 1] is Lebesgue-null ([[§10 Lebesgue Outer Measure#^ex-10-2|Ex. §10.2]]) but not Jordan measurable, since its inner content is 0 and its outer content is 1.
- **Scope.** With [[§12 Borel Sets and Measure Spaces#^thm-12-6|open sets measurable]] it gives Borel ⊆ ℳ ([[§12 Borel Sets and Measure Spaces#^cor-12-7|§12.7]]), but ℳ ≠ 𝒫(ℝ): [[The Vitali Set is Not Measurable]]. A σ-algebra is closed under complements and countable unions, while a topology is closed under arbitrary unions and finite intersections ([[§1 Topological Spaces#^def-1-1|590 Def. §1.1]]).
