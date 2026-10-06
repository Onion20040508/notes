---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 7.1", "structure of open sets"]
tags: [measure-theory, hub]
---
![[§7 Structure of Open Sets#^prop-7-1]]

## Treated in
- [[§7 Structure of Open Sets#^prop-7-1|Proposition §7.1: Open Sets in ℝ are Countable Unions of Disjoint Intervals]], in [[§7 Structure of Open Sets]]

## Its proof uses
- [[§5 Topology of ℝⁿ#^def-5-2|Definition §5.2: Open Set]]
- [[§7 Structure of Open Sets#^lem-7-2|Lemma §7.2]]

## Its proof uses (other subjects)
- [[Characterization of the Supremum]] (Single Variable Analysis)
- [[Completeness Axiom]] (Single Variable Analysis)

## Used in (Measure Theory)
- [[§11 Borel Sets and Measure Spaces#^thm-11-6|Theorem §11.6: Open Sets are Measurable]]
- [[§13 Egorov's and Lusin's Theorems#^thm-13-3|Theorem §13.3: Lusin's Theorem]]
- [[§15 The General Lebesgue Integral#^ex-15-2|Example §15.2: Application: Vanishing Integrals over Intervals]]
- [[§18 Differentiation Theory#^thm-18-19|Theorem §18.19: AC Functions Map Null Sets to Null Sets]]

## Connections
- **Proof idea.** For x ∈ O, take the largest open interval in O containing x, with endpoints given by inf and sup ([[Completeness Axiom]], [[Characterization of the Supremum]]). Two such intervals are equal or disjoint, and each contains a rational ([[§4 The Completeness Axiom#^thm-4-7|density of ℚ]]), so there are countably many ([[§7 Structure of Open Sets#^lem-7-2|Lemma §7.2]]).
- **Topology.** The intervals are the [[§1 Point-Set Topology Review#^def-1-8|connected components]] (591 Def. §1.8) of O, since [[§14 Connected Subspaces of ℝ#^cor-14-2|intervals in ℝ are connected]]. Countability comes from a rational in each interval, the same device that makes ℝⁿ second countable and hence Lindelöf ([[§6 Open Covers and the Heine–Borel Theorem#^thm-6-1|§6.1]], [[§18 Countability Axioms#^thm-18-6|590 §18.6]]). MATH 451 states the result without proof ([[§13 Some Topological Concepts in Metric Spaces#^rem-13-5|451 Rem. §13.5]]).
- **ℝⁿ.** For n ≥ 2 there is no version with disjoint open boxes: an open disc is connected, so it is not a disjoint union of two or more nonempty open sets. The substitute is [[§7 Structure of Open Sets#^prop-7-3|Proposition §7.3]], with countably many disjoint half-open dyadic cubes, the same grid as the inner Jordan approximations of MATH 452 ([[§15 Multivariable Integration#^def-15-3|452 Def. §15.3]]).
- **Used for.** Each interval is measurable, so O is too; this is the case n = 1 of [[§11 Borel Sets and Measure Spaces#^thm-11-6|Open Sets are Measurable]] (§11.6), and m(O) is the sum of the lengths. It is also used in [[§15 The General Lebesgue Integral#^ex-15-2|Ex. §15.2]] (∫ₐᶜ f = 0 for all c ⇒ f = 0 a.e.) and in [[§18 Differentiation Theory#^thm-18-19|AC Functions Map Null Sets to Null Sets]] (§18.19).
