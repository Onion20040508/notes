---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 11.8", "approximation by open sets", "G_δ approximation"]
tags: [measure-theory, hub]
---
![[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-8]]

## Treated in
- [[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-8|Theorem §11.8: Approximation by Open and G_δ Sets]], in [[Measure Theory §11 Borel Sets and Measure Spaces]]

## Its proof uses
- [[Measure Theory §5 Topology of ℝⁿ#^def-5-1|Definition §5.1: Open Ball]]
- [[Measure Theory §9 Lebesgue Outer Measure#^rem-9-1|Remark]]
- [[Measure Theory §9 Lebesgue Outer Measure#^prop-9-1|Proposition §9.1: Basic Properties of Outer Measure]]
- [[Measure Theory §9 Lebesgue Outer Measure#^prop-9-2|Proposition §9.2: Outer Measure of Closed Rectangles]]
- [[Measure Theory §10 Lebesgue Measurable Sets#^thm-10-3|Theorem §10.3: ℳ is a σ-Algebra with Countable Additivity]]
- [[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-6|Theorem §11.6: Open Sets are Measurable]]
- [[Measure Theory §11 Borel Sets and Measure Spaces#^def-11-8|Definition §11.8: G_δ and F_σ Sets]]

## Used in (Measure Theory)
- [[Measure Theory §11 Borel Sets and Measure Spaces#^prop-11-9|Proposition §11.9: Outer Approximation of Arbitrary Sets]]
- [[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-10|Theorem §11.10: Approximation by Closed and F_σ Sets]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-3|Theorem §17.3: Tonelli's Theorem]]

## Connections
- **Proof idea.** If m(E) < ∞, an L-covering with total volume < m(E) + ε has an open union G ⊇ E with m(G ∖ E) ≤ ε. If m(E) = ∞, apply this to E ∩ B(0, k) with ε/2ᵏ and take the union. Intersecting open sets with m(Gₙ ∖ E) < 1/n gives the G_δ hull of (2) ([[Measure Theory — Problem-Solving Techniques#^rem-19-16|Technique 12]]).
- **Mirror images.** Complements turn it into [[Inner Regularity of Lebesgue Measure]]. For arbitrary sets it gives a G_δ hull H ⊇ A with m*(A) = m(H) ([[Measure Theory §11 Borel Sets and Measure Spaces#^prop-11-9|§11.9]]). Every measurable set is a G_δ set minus a null set ([[Measure Theory §11 Borel Sets and Measure Spaces#^rem-11-2|Rem. §11.2]]).
- **Used for.** [[Tonelli's Theorem]] climbs from open sets to G_δ sets to null sets and then to all measurable sets through E = H ∖ Z. The ε-enlargement behind it is [[Measure Theory — Problem-Solving Techniques#^rem-19-9|Technique 5: ε-Covering and Approximation]].
