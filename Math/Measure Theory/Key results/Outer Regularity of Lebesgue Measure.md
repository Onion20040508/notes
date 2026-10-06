---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 13.1", "approximation by open sets", "G_δ approximation"]
tags: [measure-theory, hub]
---
![[§13 Approximation and Continuity of Measure#^thm-13-1]]

## Treated in
- [[§13 Approximation and Continuity of Measure#^thm-13-1|Theorem §13.1: Approximation by Open and G_δ Sets]], in [[§13 Approximation and Continuity of Measure]]

## Its proof uses
- [[§5 Topology of ℝⁿ#^def-5-1|Definition §5.1: Open Ball]]
- [[§10 Lebesgue Outer Measure#^prop-10-1|Proposition §10.1: Basic Properties of Outer Measure]]
- [[§10 Lebesgue Outer Measure#^rem-10-1|Remark]]
- [[§10 Lebesgue Outer Measure#^prop-10-2|Proposition §10.2: Outer Measure of Closed Rectangles]]
- [[§11 Lebesgue Measurable Sets#^thm-11-3|Theorem §11.3: ℳ is a σ-Algebra with Countable Additivity]]
- [[§12 Borel Sets and Measure Spaces#^thm-12-6|Theorem §12.6: Open Sets are Measurable]]
- [[§13 Approximation and Continuity of Measure#^def-13-1|Definition §13.1: G_δ Sets]]

## Used in (Measure Theory)
- [[§13 Approximation and Continuity of Measure#^prop-13-2|Proposition §13.2: Outer Approximation of Arbitrary Sets]]
- [[§13 Approximation and Continuity of Measure#^thm-13-3|Theorem §13.3: Approximation by Closed and F_σ Sets]]
- [[§25 Invariance Properties and Fubini's Theorem#^thm-25-3|Theorem §25.3: Tonelli's Theorem]]

## Connections
- **Proof idea.** If m(E) < ∞, an L-covering with total volume < m(E) + ε has an open union G ⊇ E with m(G ∖ E) ≤ ε. If m(E) = ∞, apply this to E ∩ B(0, k) with ε/2ᵏ and take the union. Intersecting open sets with m(Gₙ ∖ E) < 1/n gives the G_δ hull of (2) ([[Measure Theory Problem-Solving Techniques#^rem-19-16|Technique 12]]).
- **Mirror images.** Complements turn it into [[Inner Regularity of Lebesgue Measure]]. For arbitrary sets it gives a G_δ hull H ⊇ A with m*(A) = m(H) ([[§13 Approximation and Continuity of Measure#^prop-13-2|§13.2]]). Every measurable set is a G_δ set minus a null set ([[§12 Borel Sets and Measure Spaces#^rem-12-2|Rem. §11.2]]).
- **Used for.** [[Tonelli's Theorem]] climbs from open sets to G_δ sets to null sets and then to all measurable sets through E = H ∖ Z. The ε-enlargement behind it is [[Measure Theory Problem-Solving Techniques#^rem-19-9|Technique 5: ε-Covering and Approximation]].
