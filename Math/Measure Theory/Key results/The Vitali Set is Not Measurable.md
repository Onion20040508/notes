---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 14.6", "Vitali set"]
tags: [measure-theory, hub]
---
![[§14 The Vitali Set and the Cantor Set#^thm-14-6]]

## Treated in
- [[§14 The Vitali Set and the Cantor Set#^thm-14-6|Theorem §14.6: The Vitali Set is Not Measurable]], in [[§14 The Vitali Set and the Cantor Set]]

## Its proof uses
- [[§10 Lebesgue Outer Measure#^prop-10-1|Proposition §10.1: Basic Properties of Outer Measure]]
- [[§10 Lebesgue Outer Measure#^prop-10-2|Proposition §10.2: Outer Measure of Closed Rectangles]]
- [[§11 Lebesgue Measurable Sets#^thm-11-3|Theorem §11.3: ℳ is a σ-Algebra with Countable Additivity]]
- [[§14 The Vitali Set and the Cantor Set#^lem-14-1|Lemma §14.1: Translation Invariance of Measure]]
- [[§14 The Vitali Set and the Cantor Set#^prop-14-5|Proposition §14.5: Disjoint Translates Cover the Unit Interval]]

## Used in (Measure Theory)
- (not cited later in the course)

## Connections
- **Proof idea.** The rational translates r_j + V, r_j ∈ ℚ ∩ [−1, 1], are pairwise disjoint and cover [0, 1] inside [−1, 2] ([[§14 The Vitali Set and the Cantor Set#^prop-14-5|§14.5]]). If V were measurable, [[§14 The Vitali Set and the Cantor Set#^lem-14-1|translation invariance]] and countable additivity would give 1 ≤ Σ_j m(V) ≤ 3. That is impossible whether m(V) = 0 or m(V) > 0.
- **What it shows.** Outer measure is not additive on all subsets, and ℳ ≠ 𝒫(ℝ), even though Borel ⊆ ℳ ([[§12 Borel Sets and Measure Spaces#^cor-12-7|§12.7]]). The construction uses the Axiom of Choice ([[§14 The Vitali Set and the Cantor Set#^rem-14-6|Rem. §11.6]]). Its failure of the Carathéodory criterion is the “partition wall” picture of [[§11 Lebesgue Measurable Sets#^rem-11-2|Rem. §10.2]].
- **Linear algebra.** The equivalence classes are the cosets x + ℚ of ℚ in ℝ, viewed as a ℚ-vector space. Such translates are equal or disjoint ([[§11 Products and Quotients of Vector Spaces#^ladr-3-101|LADR 3.101]]), and V picks one point from each.
- **Counterexamples.** [[Measure Theory Problem-Solving Techniques#^rem-19-13|Technique 9: Vitali Set as Universal Counterexample]] gives three: χ_V is not measurable, a supremum of uncountably many measurable functions need not be measurable, and (−∞, 0) ∪ V fails the Carathéodory criterion.
