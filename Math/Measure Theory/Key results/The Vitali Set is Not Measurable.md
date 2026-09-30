---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 11.20", "Vitali set"]
tags: [measure-theory, hub]
---
![[§11 Borel Sets and Measure Spaces#^thm-11-20]]

## Treated in
- [[§11 Borel Sets and Measure Spaces#^thm-11-20|Theorem §11.20: The Vitali Set is Not Measurable]], in [[§11 Borel Sets and Measure Spaces]]

## Its proof uses
- [[§9 Lebesgue Outer Measure#^prop-9-1|Proposition §9.1: Basic Properties of Outer Measure]]
- [[§9 Lebesgue Outer Measure#^prop-9-2|Proposition §9.2: Outer Measure of Closed Rectangles]]
- [[§10 Lebesgue Measurable Sets#^thm-10-3|Theorem §10.3: ℳ is a σ-Algebra with Countable Additivity]]
- [[§11 Borel Sets and Measure Spaces#^lem-11-15|Lemma §11.15: Translation Invariance of Measure]]
- [[§11 Borel Sets and Measure Spaces#^prop-11-19|Proposition §11.19: Disjoint Translates Cover the Unit Interval]]

## Used in (Measure Theory)
- (not cited later in the course)

## Connections
- **Proof idea.** The rational translates r_j + V, r_j ∈ ℚ ∩ [−1, 1], are pairwise disjoint and cover [0, 1] inside [−1, 2] ([[§11 Borel Sets and Measure Spaces#^prop-11-19|§11.19]]). If V were measurable, [[§11 Borel Sets and Measure Spaces#^lem-11-15|translation invariance]] and countable additivity would give 1 ≤ Σ_j m(V) ≤ 3. That is impossible whether m(V) = 0 or m(V) > 0.
- **What it shows.** Outer measure is not additive on all subsets, and ℳ ≠ 𝒫(ℝ), even though Borel ⊆ ℳ ([[§11 Borel Sets and Measure Spaces#^cor-11-7|§11.7]]). The construction uses the Axiom of Choice ([[§11 Borel Sets and Measure Spaces#^rem-11-6|Rem. §11.6]]). Its failure of the Carathéodory criterion is the “partition wall” picture of [[§10 Lebesgue Measurable Sets#^rem-10-2|Rem. §10.2]].
- **Linear algebra.** The equivalence classes are the cosets x + ℚ of ℚ in ℝ, viewed as a ℚ-vector space. Such translates are equal or disjoint ([[3E Products and Quotients of Vector Spaces#^ladr-3-101|LADR 3.101]]), and V picks one point from each.
- **Counterexamples.** [[Measure Theory Problem-Solving Techniques#^rem-19-13|Technique 9: Vitali Set as Universal Counterexample]] gives three: χ_V is not measurable, a supremum of uncountably many measurable functions need not be measurable, and (−∞, 0) ∪ V fails the Carathéodory criterion.
