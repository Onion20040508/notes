---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 39.2", "bounded inverse theorem", "inverse mapping theorem", "Lax §15.5, Thm 11"]
tags: [functional-analysis, hub]
---
![[§39 Solving Mx = y#^thm-39-2]]

## Treated in
- [[§39 Solving Mx = y#^thm-39-2|Theorem §39.2: Banach's Inverse Mapping Theorem]], in [[§39 Solving Mx = y]]

## Its proof uses
- [[§30 Boundedness and Continuity#^prop-30-2|Proposition §30.2: Continuous if and only if Bounded]]
- [[§39 Solving Mx = y#^lem-39-3|Lemma §39.3: Continuity by Open Sets]]
- [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-2|Theorem §41.2: Open Mapping Theorem]]

## Used in (Functional Analysis)
- [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|Theorem §41.3: Equivalent Norm Theorem]]
- [[§42 Uniform Boundedness and Approximation#^thm-42-9|Theorem §42.9: Lax Equivalence Theorem]]

## Connections
- **How.** It is the [[Open Mapping Theorem]] read for a bijection: $M$ open means $M^{-1}$ pulls open sets back to open sets, which is continuity ([[§39 Solving Mx = y#^lem-39-3|§39.3]]), and continuous means bounded ([[Bounded Linear Maps Are Continuous]]). The theorem is stated in Lecture 15 and proved in Lecture 16 ([[§41 The Open Mapping Theorem and Its Consequences#^pf-39-2|proof in §41]]).
- **What it says.** Of the three questions about $Mx = y$ (existence, uniqueness, stability), the third is free: if the solution exists and is unique for every $y$, it depends continuously on $y$, $\|x\| \le C\|y\|$.
- **Why both spaces complete.** The identity from $C^1[a,b]$ with the $C^1$ norm to $C^1[a,b]$ with the maximum norm is bounded, one-to-one and onto, but its inverse is not bounded; so the maximum norm on $C^1$ cannot be complete ([[§41 The Open Mapping Theorem and Its Consequences#^ex-41-1|Ex. §41.1]]). The same argument run on $C[0,1]$ with the $L^1$ norm is [[§41 The Open Mapping Theorem and Its Consequences#^ex-41-2|Ex. §41.2]].
- **Used for.** The equivalent norm theorem ([[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]: apply it to the identity map), and the [[Lax Equivalence Theorem]], where it makes each $T_n^{-1}$ bounded.
- **Finite dimensions.** Every linear map there is bounded ([[§30 Boundedness and Continuity#^prop-30-7|§30.7]]), so the inverse of a bijective linear map is automatically bounded, and one-to-one already gives onto when the dimensions agree ([[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]).
- **Same idea elsewhere.** In topology, a continuous bijection from a compact space to a Hausdorff space has a continuous inverse ([[Bijection from Compact to Hausdorff is a Homeomorphism|590 §18.7]]). There compactness does the work that completeness and linearity do here.
