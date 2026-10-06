---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 18.3", "Luzin"]
tags: [measure-theory, hub]
---
![[§18 Egorov's and Lusin's Theorems#^thm-18-3]]

## Treated in
- [[§18 Egorov's and Lusin's Theorems#^thm-18-3|Theorem §18.3: Lusin's Theorem]], in [[§18 Egorov's and Lusin's Theorems]]

## Its proof uses
- [[§5 Topology of ℝⁿ#^def-5-1|Definition §5.1: Open Ball]]
- [[§7 Structure of Open Sets#^prop-7-2|Proposition §7.2: Open Sets in ℝ are Countable Unions of Disjoint Intervals]]
- [[§10 Lebesgue Outer Measure#^prop-10-1|Proposition §10.1: Basic Properties of Outer Measure]]
- [[§13 Approximation and Continuity of Measure#^thm-13-3|Theorem §13.3: Approximation by Closed and F_σ Sets]]
- [[§15 Measurable Functions#^def-15-2|Definition §15.2: Measurable Function]]
- [[§15 Measurable Functions#^prop-15-2|Proposition §15.2: Equivalent Conditions for Measurability]]
- [[§15 Measurable Functions#^thm-15-3|Theorem §15.3: Arithmetic Operations Preserve Measurability]]
- [[§17 Simple Functions and Modes of Convergence#^prop-17-1|Proposition §17.1: Canonical Representation of Simple Functions]]
- [[§17 Simple Functions and Modes of Convergence#^thm-17-4|Theorem §17.4: Uniform Limit of Continuous Functions]]
- [[§17 Simple Functions and Modes of Convergence#^thm-17-5|Theorem §17.5: Uniform Approximation for Bounded Functions]]
- [[§18 Egorov's and Lusin's Theorems#^lem-18-2|Lemma §18.2: Distance Between Disjoint Compact Sets]]

## Its proof uses (other subjects)
- [[§14 Series#^ex-14-4|451 §14.4: The Geometric Series]]
- [[§17 Continuous Functions#^thm-17-2|451 §17.2: Absolute Value of a Continuous Function]]
- [[§17 Continuous Functions#^thm-17-3|451 §17.3: Arithmetic of Continuous Functions]]
- [[§24 Uniform Convergence#^thm-24-2|451 §24.2: Uniform Limits Preserve Continuity]]
- [[§7 Closed Sets and Limit Points#^thm-7-1|590 §7.1: Properties of Closed Sets]]
- [[§10 Continuous Functions#^thm-10-4|590 §10.4: Rules for Continuous Functions]]

## Used in (Measure Theory)
- (not cited later in the course)

## Connections
- **Proof idea.** For a simple f, [[Inner Regularity of Lebesgue Measure]] gives finitely many disjoint closed F_i ⊆ {f = a_i} missing measure < δ. By [[§18 Egorov's and Lusin's Theorems#^lem-18-2|Lemma §18.2]] on bounded regions the pieces stay apart, so f is locally constant on ⋃F_i. For bounded f, combine the [[§17 Simple Functions and Modes of Convergence#^thm-17-5|uniform simple approximation]] (tolerance δ/2ᵏ) with [[§17 Simple Functions and Modes of Convergence#^thm-17-4|uniform limits of continuous functions]] ([[§24 Uniform Convergence#^thm-24-2|451 §24.2]]). General f reduces to f/(1 + |f|).
- **Topology.** “f continuous on F” means f restricted to F is continuous in the [[§5 Subspace Topology#^def-5-1|subspace topology]], not that f is continuous at points of F. For example, the Dirichlet function χ_ℚ is nowhere continuous ([[Dirichlet and Thomae functions]]), but it is 0 on closed subsets of the irrationals of measure close to 1. By Tietze ([[§24 Normal Spaces#^rem-24-3|not covered]]), f restricted to F extends continuously to ℝⁿ.
- **Compare.** It is the partner of [[Egorov's Theorem]]: measurable becomes continuous off a small set, just as a.e. convergence becomes uniform ([[§18 Egorov's and Lusin's Theorems#^rem-18-3|Rem. §13.3]]). The converse (HW5 P3) is [[Measure Theory Problem-Solving Techniques#^rem-19-16|Technique 12]]. The approximation-in-norm version is [[Continuous Functions of Compact Support are Dense in L¹]].
