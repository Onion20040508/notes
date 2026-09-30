---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 13.3", "Luzin"]
tags: [measure-theory, hub]
---
![[Measure Theory §13 Egorov's and Lusin's Theorems#^thm-13-3]]

## Treated in
- [[Measure Theory §13 Egorov's and Lusin's Theorems#^thm-13-3|Theorem §13.3: Lusin's Theorem]], in [[Measure Theory §13 Egorov's and Lusin's Theorems]]

## Its proof uses
- [[Measure Theory §5 Topology of ℝⁿ#^def-5-1|Definition §5.1: Open Ball]]
- [[Measure Theory §7 Structure of Open Sets#^prop-7-1|Proposition §7.1: Open Sets in ℝ are Countable Unions of Disjoint Intervals]]
- [[Measure Theory §9 Lebesgue Outer Measure#^prop-9-1|Proposition §9.1: Basic Properties of Outer Measure]]
- [[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-10|Theorem §11.10: Approximation by Closed and F_σ Sets]]
- [[Measure Theory §12 Measurable Functions#^prop-12-2|Proposition §12.2: Equivalent Conditions for Measurability]]
- [[Measure Theory §12 Measurable Functions#^def-12-2|Definition §12.2: Measurable Function]]
- [[Measure Theory §12 Measurable Functions#^thm-12-3|Theorem §12.3: Arithmetic Operations Preserve Measurability]]
- [[Measure Theory §12 Measurable Functions#^prop-12-13|Proposition §12.13: Canonical Representation of Simple Functions]]
- [[Measure Theory §12 Measurable Functions#^thm-12-16|Theorem §12.16: Uniform Limit of Continuous Functions]]
- [[Measure Theory §12 Measurable Functions#^thm-12-17|Theorem §12.17: Uniform Approximation for Bounded Functions]]
- [[Measure Theory §13 Egorov's and Lusin's Theorems#^lem-13-2|Lemma §13.2: Distance Between Disjoint Compact Sets]]

## Its proof uses (other subjects)
- [[Single Variable Analysis §14 Series#^ex-14-4|451 §14.4: The geometric series]]
- [[Single Variable Analysis §17 Continuous Functions#^thm-17-2|451 §17.2: Absolute Value of a Continuous Function]]
- [[Single Variable Analysis §17 Continuous Functions#^thm-17-3|451 §17.3: Arithmetic of Continuous Functions]]
- [[Single Variable Analysis §24 Uniform Convergence#^thm-24-2|451 §24.2: Uniform Limits Preserve Continuity]]
- [[Topology §6 Closed Sets and Limit Points#^thm-6-1|590 §6.1: Properties of Closed Sets]]
- [[Topology §9 Continuous Functions#^thm-9-4|590 §9.4: Rules for Continuous Functions]]

## Used in (Measure Theory)
- (not cited later in the course)

## Connections
- **Proof idea.** For a simple f, [[Inner Regularity of Lebesgue Measure]] gives finitely many disjoint closed F_i ⊆ {f = a_i} missing measure < δ. By [[Measure Theory §13 Egorov's and Lusin's Theorems#^lem-13-2|Lemma §13.2]] on bounded regions the pieces stay apart, so f is locally constant on ⋃F_i. For bounded f, combine the [[Measure Theory §12 Measurable Functions#^thm-12-17|uniform simple approximation]] (tolerance δ/2ᵏ) with [[Measure Theory §12 Measurable Functions#^thm-12-16|uniform limits of continuous functions]] ([[Single Variable Analysis §24 Uniform Convergence#^thm-24-2|451 §24.2]]). General f reduces to f/(1 + |f|).
- **Topology.** “f continuous on F” means f restricted to F is continuous in the [[Topology §5 Subspace Topology#^def-5-1|subspace topology]], not that f is continuous at points of F. For example, the Dirichlet function χ_ℚ is nowhere continuous ([[Dirichlet and Thomae functions]]), but it is 0 on closed subsets of the irrationals of measure close to 1. By Tietze ([[Topology §20 Normal Spaces#^rem-20-3|not covered]]), f restricted to F extends continuously to ℝⁿ.
- **Compare.** It is the partner of [[Egorov's Theorem]]: measurable becomes continuous off a small set, just as a.e. convergence becomes uniform ([[Measure Theory §13 Egorov's and Lusin's Theorems#^rem-13-3|Rem. §13.3]]). The converse (HW5 P3) is [[Measure Theory — Problem-Solving Techniques#^rem-19-16|Technique 12]]. The approximation-in-norm version is [[Continuous Functions of Compact Support are Dense in L¹]].
