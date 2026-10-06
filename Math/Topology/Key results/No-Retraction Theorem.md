---
subject: math
type: theorem
source: "[[Topology]]"
aliases: ["Topology 26.6"]
tags: [topology, hub]
---
![[§25a Retractions and Fixed Points#^thm-26-6]]

## Treated in
- [[§25a Retractions and Fixed Points#^thm-26-6|Theorem §26.6: No-Retraction Theorem (Munkres 55.2)]], in [[§26 Deformation Retracts and Homotopy Type]]

## Its proof uses
- [[§23 The Fundamental Group#^def-23-4|Definition §23.4: Induced Homomorphism]]
- [[§23 The Fundamental Group#^thm-23-5|Theorem §23.5: Functoriality of π₁]]
- [[§24a Lifting and the Fundamental Group of the Circle#^thm-24-10|Theorem §24.10: π₁(S¹) ≅ ℤ]]
- [[§25a Retractions and Fixed Points#^prop-26-5|Proposition §26.5: Bⁿ is Convex and Simply Connected]]

## Used in (Topology)
- [[§25a Retractions and Fixed Points#^thm-26-7|Theorem §26.7: Brouwer Fixed Point Theorem for B² (Munkres 55.6)]]

## Connections
- **Proof pattern.** A retraction would satisfy r ∘ j = id, so by [[Functoriality of π₁]] the map j∗ : ℤ → π₁(B²) = 0 would be injective, which is impossible. This uses [[Fundamental Group of the Circle]] and [[§25a Retractions and Fixed Points#^prop-26-5|Bⁿ is Convex and Simply Connected]]. It is the template for π₁ obstruction arguments ([[§25a Retractions and Fixed Points#^rem-26-2|Why This Matters]]).
- **Immediate consequence.** [[Brouwer Fixed Point Theorem]].
- **Higher dimensions.** The π₁ argument cannot prove the [[§25a Retractions and Fixed Points#^thm-26-9|Generalized No-Retraction Theorem]], because [[Sⁿ is Simply Connected for n ≥ 2]] makes j∗ : 0 → 0 unobstructed. That case needs homology ([[§25a Retractions and Fixed Points#^rem-26-4|Why Our Proof Does Not Generalize]]).
