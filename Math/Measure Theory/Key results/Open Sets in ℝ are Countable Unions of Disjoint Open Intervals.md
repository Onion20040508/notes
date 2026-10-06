---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 7.2", "structure of open sets"]
tags: [measure-theory, hub]
---
![[§7 Structure of Open Sets#^prop-7-2]]

## Treated in
- [[§7 Structure of Open Sets#^prop-7-2|Proposition §7.2: Open Sets in ℝ are Countable Unions of Disjoint Intervals]], in [[§7 Structure of Open Sets]]

## Its proof uses
- [[§5 Topology of ℝⁿ#^def-5-2|Definition §5.2: Open Set]]
- [[§7 Structure of Open Sets#^lem-7-1|Lemma §7.1]]

## Its proof uses (other subjects)
- [[Characterization of the Supremum]] (Single Variable Analysis)
- [[Completeness Axiom]] (Single Variable Analysis)

## Used in (Measure Theory)
- [[§12 Borel Sets and Measure Spaces#^thm-12-6|Theorem §12.6: Open Sets are Measurable]]
- [[§18 Egorov's and Lusin's Theorems#^thm-18-3|Theorem §18.3: Lusin's Theorem]]
- [[§22 The General Lebesgue Integral#^ex-22-2|Example §22.2: Application: Vanishing Integrals over Intervals]]
- [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-32-6|Theorem §32.6: AC Functions Map Null Sets to Null Sets]]

## Connections
- **Proof idea.** For x ∈ O, take the largest open interval in O containing x, with endpoints given by inf and sup ([[Completeness Axiom]], [[Characterization of the Supremum]]). Two such intervals are equal or disjoint, and each contains a rational ([[§4 The Completeness Axiom#^thm-4-7|density of ℚ]]), so there are countably many ([[§7 Structure of Open Sets#^lem-7-1|Lemma §7.1]]).
- **Topology.** The intervals are the [[§1 Point-Set Topology Review#^def-1-9|connected components]] (591 Def. §1.9) of O, since [[§16 Connected Subspaces of ℝ#^cor-16-2|intervals in ℝ are connected]]. Countability comes from a rational in each interval, the same device that makes ℝⁿ second countable and hence Lindelöf ([[§6 Open Covers and the Heine–Borel Theorem#^thm-6-3|§6.3]], [[§22 Countability Axioms#^thm-22-6|590 §22.6]]). MATH 451 states the result without proof ([[§13 Some Topological Concepts in Metric Spaces#^rem-13-5|451 Rem. §13.5]]).
- **ℝⁿ.** For n ≥ 2 there is no version with disjoint open boxes: an open disc is connected, so it is not a disjoint union of two or more nonempty open sets. The substitute is [[§7 Structure of Open Sets#^prop-7-3|Proposition §7.3]], with countably many disjoint half-open dyadic cubes, the same grid as the inner Jordan approximations of MATH 452 ([[§20 Multivariable Integration#^def-20-4|452 Def. §20.4]]).
- **Used for.** Each interval is measurable, so O is too; this is the case n = 1 of [[§12 Borel Sets and Measure Spaces#^thm-12-6|Open Sets are Measurable]] (§12.6), and m(O) is the sum of the lengths. It is also used in [[§22 The General Lebesgue Integral#^ex-22-2|Ex. §22.2]] (∫ₐᶜ f = 0 for all c ⇒ f = 0 a.e.) and in [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-32-6|AC Functions Map Null Sets to Null Sets]] (§32.6).
