---
subject: math
type: theorem
source: "[[Topology]]"
aliases: ["Topology 34.6"]
tags: [topology, hub]
---
![[§34 Retractions and Fixed Points#^thm-34-6]]

## Treated in
- [[§34 Retractions and Fixed Points#^thm-34-6|Theorem §34.6: No-Retraction Theorem (Munkres 55.2)]], in [[§35 Deformation Retracts and Homotopy Type]]

## Its proof uses
- [[§29 The Fundamental Group#^def-29-4|Definition §29.4: Induced Homomorphism]]
- [[§29 The Fundamental Group#^thm-29-5|Theorem §29.5: Functoriality of π₁]]
- [[§32 Lifting and the Fundamental Group of the Circle#^thm-32-5|Theorem §32.5: π₁(S¹) ≅ ℤ]]
- [[§34 Retractions and Fixed Points#^prop-34-5|Proposition §34.5: Bⁿ is Convex and Simply Connected]]

## Used in (Topology)
- [[§34 Retractions and Fixed Points#^thm-34-7|Theorem §34.7: Brouwer Fixed Point Theorem for B² (Munkres 55.6)]]

## Connections
- **Proof pattern.** A retraction would satisfy r ∘ j = id, so by [[Functoriality of π₁]] the map j∗ : ℤ → π₁(B²) = 0 would be injective, which is impossible. This uses [[Fundamental Group of the Circle]] and [[§34 Retractions and Fixed Points#^prop-34-5|Bⁿ is Convex and Simply Connected]]. It is the template for π₁ obstruction arguments ([[§34 Retractions and Fixed Points#^rem-34-2|Why This Matters]]).
- **Immediate consequence.** [[Brouwer Fixed Point Theorem]].
- **Higher dimensions.** The π₁ argument cannot prove the [[§34 Retractions and Fixed Points#^thm-34-9|Generalized No-Retraction Theorem]], because [[Sⁿ is Simply Connected for n ≥ 2]] makes j∗ : 0 → 0 unobstructed. That case needs homology ([[§34 Retractions and Fixed Points#^rem-34-4|Why Our Proof Does Not Generalize]]).
