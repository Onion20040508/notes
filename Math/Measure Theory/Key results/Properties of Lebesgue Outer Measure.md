---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 10.1", "outer measure properties"]
tags: [measure-theory, hub]
---
![[§10 Lebesgue Outer Measure#^prop-10-1]]

## Treated in
- [[§10 Lebesgue Outer Measure#^prop-10-1|Proposition §10.1: Basic Properties of Outer Measure]], in [[§10 Lebesgue Outer Measure]]

## Its proof uses
- [[§3 Countability of Rationals and Unions#^prop-3-1|Proposition §3.1: Countable Union of Countable Sets]]
- [[§10 Lebesgue Outer Measure#^rem-10-1|Remark]]
- [[§10 Lebesgue Outer Measure#^def-10-3|Definition §10.3: L-covering]]
- [[§10 Lebesgue Outer Measure#^def-10-4|Definition §10.4: Outer Measure]]

## Used in (Measure Theory)
- [[§10 Lebesgue Outer Measure#^prop-10-2|Proposition §10.2: Outer Measure of Closed Rectangles]]
- [[§11 Lebesgue Measurable Sets#^ex-11-1|Example §11.1: Sets of Measure Zero are Measurable]]
- [[§11 Lebesgue Measurable Sets#^thm-11-3|Theorem §11.3: ℳ is a σ-Algebra with Countable Additivity]]
- [[§12 Borel Sets and Measure Spaces#^prop-12-4|Proposition §12.4: Rectangle Test for Measurability]]
- [[§12 Borel Sets and Measure Spaces#^prop-12-5|Proposition §12.5: Rectangles are Measurable]]
- [[§13 Approximation and Continuity of Measure#^thm-13-1|Theorem §13.1: Approximation by Open and G_δ Sets]]
- [[§13 Approximation and Continuity of Measure#^prop-13-2|Proposition §13.2: Outer Approximation of Arbitrary Sets]]
- [[§13 Approximation and Continuity of Measure#^thm-13-3|Theorem §13.3: Approximation by Closed and F_σ Sets]]
- [[§13 Approximation and Continuity of Measure#^thm-13-6|Theorem §13.6: Approximation by Bounded Closed Sets and Finite Unions of Rectangles]]
- [[§13 Approximation and Continuity of Measure#^thm-13-7|Theorem §13.7: Continuity of Outer Measure from Below via Measurable Exhaustion]]
- [[§14 The Vitali Set and the Cantor Set#^thm-14-6|Theorem §14.6: The Vitali Set is Not Measurable]]
- [[§14 The Vitali Set and the Cantor Set#^prop-14-7|Proposition §14.7: Properties of the Cantor Set]]
- [[§16 Limits and Positive Parts of Measurable Functions#^prop-16-7|Proposition §16.7: Functions Equal a.e. to Measurable Functions]]
- [[§18 Egorov's and Lusin's Theorems#^thm-18-1|Theorem §18.1: Egorov's Theorem]]
- [[§18 Egorov's and Lusin's Theorems#^thm-18-3|Theorem §18.3: Lusin's Theorem]]
- [[§20 The Lebesgue Integral for Simple Functions#^prop-20-2|Proposition §20.2: Restriction and Null Sets]]
- [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|Proposition §21.4: Vanishing Integral for Non-Negative Functions]]
- [[§25 Invariance Properties and Fubini's Theorem#^lem-25-5|Lemma §25.5: Closure Properties of 𝓕]]
- [[§26 Applications of Tonelli's Theorem#^thm-26-3|Theorem §26.3: Measurability of Product Sets]]
- [[§26 Applications of Tonelli's Theorem#^cor-26-4|Corollary §26.4: The Graph Has Measure Zero]]
- [[§28 Differentiation Theory#^thm-28-2|Theorem §28.2: Vitali Covering Theorem]]
- [[§29 Lebesgue's Differentiation Theorem#^thm-29-1|Theorem §29.1: Lebesgue's Differentiation Theorem for Monotone Functions]]
- [[§30 Differentiating the Integral#^thm-30-3|Theorem §30.3: Linear Maps Preserve Null Sets]]
- [[§31 Absolute Continuity#^thm-31-4|Theorem §31.4]]
- [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-32-6|Theorem §32.6: AC Functions Map Null Sets to Null Sets]]
- [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|Proposition §34.2: The Essential Supremum is Achieved A.E.]]
- [[§35 Lᵖ as a Banach Space#^thm-35-11|Theorem §35.11: Riesz–Fischer Theorem]]

## Connections
- **Proof idea.** For (3), cover each A_i by rectangles of total volume ≤ m*(A_i) + ε/2ⁱ. All of these rectangles together are a countable L-covering of ⋃A_i ([[Countable Union of Countable Sets is Countable]]), costing at most ε extra ([[§14 Series#^ex-14-4|geometric series]]).
- **Only subadditive.** m* is not additive on all sets. Restricting to the sets that satisfy the [[§11 Lebesgue Measurable Sets#^def-11-1|Carathéodory criterion]] gives [[Lebesgue Measurable Sets Form a σ-Algebra|countable additivity]], and the [[The Vitali Set is Not Measurable|Vitali set]] shows the restriction is necessary. These three properties become the axioms of a general [[§12 Borel Sets and Measure Spaces#^def-12-3|outer measure]] in [[Carathéodory's Theorem]].
- **Jordan vs Lebesgue.** Outer Jordan content ([[§20 Multivariable Integration#^def-20-6|452 Def. §20.6]]) uses finitely many squares. Countable coverings make every countable set null ([[§10 Lebesgue Outer Measure#^ex-10-2|Ex. §10.2]]), including ℚ ∩ [0, 1], whose outer Jordan content is 1.
- **Technique.** [[Measure Theory Problem-Solving Techniques#^rem-19-7|Technique 3: Subadditivity and Monotonicity Estimates]].
