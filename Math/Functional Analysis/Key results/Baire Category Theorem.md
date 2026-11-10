---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 40.4", "Baire", "complete metric spaces are of the second category", "Lax §15.5, proof of Thm 9"]
tags: [functional-analysis, hub]
---
![[§40 The Baire Category Theorem#^thm-40-4]]

## Treated in
- [[§40 The Baire Category Theorem#^thm-40-4|Theorem §40.4: Baire Category Theorem]], in [[§40 The Baire Category Theorem]]

## Its proof uses
- [[§11 Normed Linear Spaces#^def-11-6|Definition §11.6: Closed Subset]]
- [[§11 Normed Linear Spaces#^prop-11-7|Proposition §11.7: Properties of the Closure]]
- [[§40 The Baire Category Theorem#^lem-40-1|Lemma §40.1: Nowhere Dense via Balls]]
- [[§40 The Baire Category Theorem#^lem-40-2|Lemma §40.2: Smaller Balls Also Work]]

## Used in (Functional Analysis)
- [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|Theorem §41.1: The Image of the Unit Ball Contains a Ball About 0]]

## Connections
- **How.** Suppose a complete metric space were a countable union of nowhere dense sets $E_n$. Build nested closed balls, the $n$-th one missing $\overline{E}_n$ ([[§40 The Baire Category Theorem#^lem-40-1|§40.1]], [[§40 The Baire Category Theorem#^lem-40-2|§40.2]]) and of radius $< 1/n$. The centres are Cauchy, completeness gives a limit, and the limit lies in every ball, hence in no $E_n$ ([[Functional Analysis Problem-Solving Techniques#^rem-t25|Technique 25]]). The proof was begun in Lecture 15 and redone in full in Lecture 16.
- **Why complete.** $\mathbb{Q}^n$ is a countable union of points, so it is of the first category ([[§40 The Baire Category Theorem#^ex-40-1|Ex. §40.1]]); with the metric of $\mathbb{R}^n$ it is not complete. Completeness is the only hypothesis: no linear structure is used.
- **Used for.** Once, in Step 1 of [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]]: $Y = \bigcup_n \overline{M(B(0,n))}$, so one of these closed sets has an interior point. Everything in [[Open Mapping Theorem]], [[Banach's Inverse Mapping Theorem]], [[Closed Graph Theorem]] and, in this course, [[Uniform Boundedness Principle]] descends from that one use ([[§41 The Open Mapping Theorem and Its Consequences#^rem-41-3|Remark: How the Theorems Fit Together]]). What is really needed there is that the range is of the second category ([[§42 Uniform Boundedness and Approximation#^thm-42-2|§42.2]]).
- **Same idea elsewhere.** Lax proves the uniform boundedness principle by applying Baire directly to the closed sets $\{x : \sup_\alpha \|A_\alpha x\| \le k\}$ ([[§42 Uniform Boundedness and Approximation#^rem-42-2|Remark: Other Proofs of the Principle]]). The other existence tools of the course are compactness in finite dimensions ([[Bolzano–Weierstrass Theorem]]) and [[Zorn's Lemma]]; Baire is the one that runs on completeness alone.
