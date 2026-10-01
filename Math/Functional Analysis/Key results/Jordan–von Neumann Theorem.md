---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 17.4", "parallelogram law characterizes inner product norms", "Lax §6.1, Exercise 1"]
tags: [functional-analysis, hub]
---
![[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-4]]

## Treated in
- [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-4|Theorem §17.4: Jordan–von Neumann]], in [[§17 Cauchy–Schwarz and the Induced Norm]]

## Its proof uses
- [[§8 Normed Linear Spaces#^def-8-1|Definition §8.1: Norm; Normed Linear Space]]
- [[§8 Normed Linear Spaces#^lem-8-3|Lemma §8.3: Reverse Triangle Inequality]]
- [[§8 Normed Linear Spaces#^prop-8-4|Proposition §8.4: A Norm is Continuous]]
- [[§16 Definition and Examples#^def-16-1|Definition §16.1: Inner Product; Scalar Product]]
- [[§17 Cauchy–Schwarz and the Induced Norm#^prop-17-3|Proposition §17.3: Parallelogram Law and Polarization]]

## Its proof uses (other subjects)
- [[§4 The Completeness Axiom#^thm-4-7|451 §4.7: Density of ℚ in ℝ]]

## Used in (Functional Analysis)
- [[§17 Cauchy–Schwarz and the Induced Norm#^cor-17-5|Corollary §17.5: Only p = 2 Gives an Inner Product]]

## Connections
- **How.** Define (x, y) by polarization. The parallelogram law gives a midpoint identity, hence additivity, and additivity gives ℚ-homogeneity by algebra. Continuity of the norm and density of ℚ ([[§4 The Completeness Axiom#^thm-4-7|451 §4.7]]) extend this to ℝ ([[Functional Analysis Problem-Solving Techniques#^rem-t10|Technique 10]]). In the complex case the real form R is an inner product on the underlying real space, and (x, y) = R(x, y) + iR(x, iy). This is the same reduction as in the [[Complex Hahn–Banach Theorem]].
- **Why continuity.** Additivity alone does not give linearity, since additive non-linear functions ℝ → ℝ exist (built from a Hamel basis). Real homogeneity is the only analytic step ([[§17 Cauchy–Schwarz and the Induced Norm#^rem-17-3|Remark §17]]).
- **Used for.** Only p = 2 gives an inner-product norm on 𝔽ⁿ (n ≥ 2), ℓᵖ and Lᵖ ([[§17 Cauchy–Schwarz and the Induced Norm#^cor-17-5|§17.5]]). Unit vectors with disjoint supports violate the parallelogram law unless p = 2. So [[Closest Point in a Closed Convex Set]], which runs on the parallelogram law, is a Hilbert-space theorem.
- **Finite dimensions.** LADR's parallelogram equality ([[§19 Inner Products and Norms#^ladr-6-21|LADR 6.21]]) has a remark naming Jordan–von Neumann. The operator norm on ℒ(V, W) fails the law and so comes from no inner product (remark after [[§27 Consequences of Singular Value Decomposition#^ladr-7-86|LADR 7.86]]).
