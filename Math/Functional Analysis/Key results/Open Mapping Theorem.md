---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 41.2", "open mapping principle", "Lax §15.5, Thm 10"]
tags: [functional-analysis, hub]
---
![[§41 The Open Mapping Theorem and Its Consequences#^thm-41-2]]

## Treated in
- [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-2|Theorem §41.2: Open Mapping Theorem]], in [[§41 The Open Mapping Theorem and Its Consequences]]

## Its proof uses
- [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|Theorem §41.1: The Image of the Unit Ball Contains a Ball About 0]]

## Used in (Functional Analysis)
- [[§42 Uniform Boundedness and Approximation#^thm-42-2|Theorem §42.2: Open Mapping Theorem, General Form]]

## Connections
- **How.** By [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]], $M(B(0,1))$ contains a ball $B(0,\delta)$. Translating and scaling, $M(B(x, r)) \supset B(Mx, r\delta)$, so the image of an open set contains a ball about each of its points. The work is in §41.1: the [[Baire Category Theorem]] gives a ball in the closure of the image, and successive approximation removes the closure ([[Functional Analysis Problem-Solving Techniques#^rem-t26|Technique 26]]).
- **Why the hypotheses.** Completeness of $Y$ enters only through Baire, so it can be weakened to: the range is of the second category ([[§42 Uniform Boundedness and Approximation#^thm-42-2|§42.2]]; then $M$ is onto, [[§42 Uniform Boundedness and Approximation#^cor-42-3|§42.3]], HW9). Completeness of $X$ is used to sum the corrections ([[§41 The Open Mapping Theorem and Its Consequences#^rem-41-1|Remark: Where Completeness is Used]]).
- **Used for.** [[Banach's Inverse Mapping Theorem]], then the equivalent norm theorem ([[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]) and the [[Closed Graph Theorem]]; the ball in the image gives the estimate in the closed range criterion ([[§41 The Open Mapping Theorem and Its Consequences#^prop-41-5|§41.5]]). The chain is in [[§41 The Open Mapping Theorem and Its Consequences#^rem-41-3|Remark: How the Theorems Fit Together]].
- **Finite dimensions.** A linear map onto a finite-dimensional space is open without any of this: all norms are equivalent there ([[All Norms on a Finite-Dimensional Space Are Equivalent]]) and a right inverse can be written on a basis.
