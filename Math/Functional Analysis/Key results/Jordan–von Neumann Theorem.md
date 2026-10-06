---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 21.4", "parallelogram law characterizes inner product norms", "Lax §6.1, Exercise 1"]
tags: [functional-analysis, hub]
---
![[§24 The Parallelogram Law and Jordan–von Neumann#^thm-24-2]]

## Treated in
- [[§24 The Parallelogram Law and Jordan–von Neumann#^thm-24-2|Theorem §24.2: Jordan–von Neumann]], in [[§23 Cauchy–Schwarz and the Induced Norm]]

## Its proof uses
- [[§11 Normed Linear Spaces#^def-11-1|Definition §11.1: Norm; Normed Linear Space]]
- [[§11 Normed Linear Spaces#^lem-11-3|Lemma §11.3: Reverse Triangle Inequality]]
- [[§11 Normed Linear Spaces#^prop-11-4|Proposition §11.4: A Norm is Continuous]]
- [[§22 Definition and Examples#^def-22-1|Definition §22.1: Inner Product; Scalar Product]]
- [[§24 The Parallelogram Law and Jordan–von Neumann#^prop-24-1|Proposition §24.1: Parallelogram Law and Polarization]]

## Its proof uses (other subjects)
- [[§4 The Completeness Axiom#^thm-4-7|451 §4.7: Density of ℚ in ℝ]]

## Used in (Functional Analysis)
- [[§24 The Parallelogram Law and Jordan–von Neumann#^cor-24-3|Corollary §24.3: Only p = 2 Gives an Inner Product]]

## Connections
- **How.** Define (x, y) by polarization. The parallelogram law gives a midpoint identity, hence additivity, and additivity gives ℚ-homogeneity by algebra. Continuity of the norm and density of ℚ ([[§4 The Completeness Axiom#^thm-4-7|451 §4.7]]) extend this to ℝ ([[Functional Analysis Problem-Solving Techniques#^rem-t10|Technique 10]]). In the complex case the real form R is an inner product on the underlying real space, and (x, y) = R(x, y) + iR(x, iy). This is the same reduction as in the [[Complex Hahn–Banach Theorem]].
- **Why continuity.** Additivity alone does not give linearity, since additive non-linear functions ℝ → ℝ exist (built from a Hamel basis). Real homogeneity is the only analytic step ([[§24 The Parallelogram Law and Jordan–von Neumann#^rem-24-1|Remark §21]]).
- **Used for.** Only p = 2 gives an inner-product norm on 𝔽ⁿ (n ≥ 2), ℓᵖ and Lᵖ ([[§24 The Parallelogram Law and Jordan–von Neumann#^cor-24-3|§24.3]]). Unit vectors with disjoint supports violate the parallelogram law unless p = 2. So [[Closest Point in a Closed Convex Set]], which runs on the parallelogram law, is a Hilbert-space theorem.
- **Finite dimensions.** LADR's parallelogram equality ([[§20 Inner Products and Norms#^ladr-6-21|LADR 6.21]]) has a remark naming Jordan–von Neumann. The operator norm on ℒ(V, W) fails the law and so comes from no inner product (remark after [[§28 Consequences of Singular Value Decomposition#^ladr-7-86|LADR 7.86]]).
