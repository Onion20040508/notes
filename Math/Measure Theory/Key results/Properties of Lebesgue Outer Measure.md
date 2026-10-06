---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 9.1", "outer measure properties"]
tags: [measure-theory, hub]
---
![[§9 Lebesgue Outer Measure#^prop-9-1]]

## Treated in
- [[§9 Lebesgue Outer Measure#^prop-9-1|Proposition §9.1: Basic Properties of Outer Measure]], in [[§9 Lebesgue Outer Measure]]

## Its proof uses
- [[§3 Countability of Rationals and Unions#^prop-3-1|Proposition §3.1: Countable Union of Countable Sets]]
- [[§9 Lebesgue Outer Measure#^rem-9-1|Remark]]
- [[§9 Lebesgue Outer Measure#^def-9-3|Definition §9.3: L-covering]]
- [[§9 Lebesgue Outer Measure#^def-9-4|Definition §9.4: Outer Measure]]

## Used in (Measure Theory)
- [[§9 Lebesgue Outer Measure#^prop-9-2|Proposition §9.2: Outer Measure of Closed Rectangles]]
- [[§10 Lebesgue Measurable Sets#^ex-10-1|Example §10.1: Sets of Measure Zero are Measurable]]
- [[§10 Lebesgue Measurable Sets#^thm-10-3|Theorem §10.3: ℳ is a σ-Algebra with Countable Additivity]]
- [[§11 Borel Sets and Measure Spaces#^prop-11-4|Proposition §11.4: Rectangle Test for Measurability]]
- [[§11 Borel Sets and Measure Spaces#^prop-11-5|Proposition §11.5: Rectangles are Measurable]]
- [[§11 Borel Sets and Measure Spaces#^thm-11-8|Theorem §11.8: Approximation by Open and G_δ Sets]]
- [[§11 Borel Sets and Measure Spaces#^prop-11-9|Proposition §11.9: Outer Approximation of Arbitrary Sets]]
- [[§11 Borel Sets and Measure Spaces#^thm-11-10|Theorem §11.10: Approximation by Closed and F_σ Sets]]
- [[§11 Borel Sets and Measure Spaces#^thm-11-11|Theorem §11.11: Approximation by Bounded Closed Sets and Finite Unions of Rectangles]]
- [[§11 Borel Sets and Measure Spaces#^thm-11-14|Theorem §11.14: Continuity of Outer Measure from Below via Measurable Exhaustion]]
- [[§11 Borel Sets and Measure Spaces#^thm-11-20|Theorem §11.20: The Vitali Set is Not Measurable]]
- [[§11 Borel Sets and Measure Spaces#^prop-11-21|Proposition §11.21: Properties of the Cantor Set]]
- [[§12 Measurable Functions#^prop-12-12|Proposition §12.12: Functions Equal a.e. to Measurable Functions]]
- [[§13 Egorov's and Lusin's Theorems#^thm-13-1|Theorem §13.1: Egorov's Theorem]]
- [[§13 Egorov's and Lusin's Theorems#^thm-13-3|Theorem §13.3: Lusin's Theorem]]
- [[§14 The Lebesgue Integral for Simple Functions#^prop-14-2|Proposition §14.2: Restriction and Null Sets]]
- [[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|Proposition §14.11: Vanishing Integral for Non-Negative Functions]]
- [[§17 Invariance Properties and Fubini's Theorem#^lem-17-5|Lemma §17.5: Closure Properties of 𝓕]]
- [[§17 Invariance Properties and Fubini's Theorem#^thm-17-8|Theorem §17.8: Measurability of Product Sets]]
- [[§17 Invariance Properties and Fubini's Theorem#^cor-17-10|Corollary §17.10: The Graph Has Measure Zero]]
- [[§18 Differentiation Theory#^thm-18-2|Theorem §18.2: Vitali Covering Theorem]]
- [[§18 Differentiation Theory#^thm-18-9|Theorem §18.9: Lebesgue's Differentiation Theorem for Monotone Functions]]
- [[§18 Differentiation Theory#^thm-18-19|Theorem §18.19: AC Functions Map Null Sets to Null Sets]]
- [[§18 Differentiation Theory#^thm-18-22|Theorem §18.22: Linear Maps Preserve Null Sets]]
- [[§18 Differentiation Theory#^thm-18-27|Theorem §18.27]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|Proposition §19.2: The Essential Supremum is Achieved A.E.]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-18|Theorem §19.18: Riesz–Fischer Theorem]]

## Connections
- **Proof idea.** For (3), cover each A_i by rectangles of total volume ≤ m*(A_i) + ε/2ⁱ. All of these rectangles together are a countable L-covering of ⋃A_i ([[Countable Union of Countable Sets is Countable]]), costing at most ε extra ([[§14 Series#^ex-14-4|geometric series]]).
- **Only subadditive.** m* is not additive on all sets. Restricting to the sets that satisfy the [[§10 Lebesgue Measurable Sets#^def-10-1|Carathéodory criterion]] gives [[Lebesgue Measurable Sets Form a σ-Algebra|countable additivity]], and the [[The Vitali Set is Not Measurable|Vitali set]] shows the restriction is necessary. These three properties become the axioms of a general [[§11 Borel Sets and Measure Spaces#^def-11-3|outer measure]] in [[Carathéodory's Theorem]].
- **Jordan vs Lebesgue.** Outer Jordan content ([[§15 Multivariable Integration#^def-15-new2|452 Def. §15.4]]) uses finitely many squares. Countable coverings make every countable set null ([[§9 Lebesgue Outer Measure#^ex-9-2|Ex. §9.2]]), including ℚ ∩ [0, 1], whose outer Jordan content is 1.
- **Technique.** [[Measure Theory Problem-Solving Techniques#^rem-19-7|Technique 3: Subadditivity and Monotonicity Estimates]].
