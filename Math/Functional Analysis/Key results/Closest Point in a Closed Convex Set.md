---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 22.2", "projection theorem", "Lax §6.2, Thm 2"]
tags: [functional-analysis, hub]
---
![[§25 Projection and Orthogonal Decomposition#^thm-25-2]]

## Treated in
- [[§25 Projection and Orthogonal Decomposition#^thm-25-2|Theorem §25.2: Closest Point in a Closed Convex Set]], in [[§25 Projection and Orthogonal Decomposition]]

## Its proof uses
- [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-3|Definition §3.3: Convex Set]]
- [[§11 Normed Linear Spaces#^prop-11-4|Proposition §11.4: A Norm is Continuous]]
- [[§11 Normed Linear Spaces#^def-11-5|Definition §11.5: Cauchy Sequence]]
- [[§11 Normed Linear Spaces#^def-11-6|Definition §11.6: Closed Subset]]
- [[§23 Cauchy–Schwarz and the Induced Norm#^def-23-1|Definition §23.1: Hilbert Space]]
- [[§24 The Parallelogram Law and Jordan–von Neumann#^prop-24-1|Proposition §24.1: Parallelogram Law and Polarization]]

## Used in (Functional Analysis)
- [[§25 Projection and Orthogonal Decomposition#^thm-25-4|Theorem §25.4: Orthogonal Decomposition]]
- [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-5|Proposition §26.5: Minimizing a Quadratic Functional over a Closed Convex Set]]

## Connections
- **How.** Take a minimizing sequence and apply the parallelogram law to x₀ − y_m and x₀ − y_n. Convexity puts the midpoint in K, which forces ‖y_n − y_m‖² < 2/m + 2/n. Completeness gives a limit, and closedness keeps it in K. The same midpoint argument proves uniqueness. Wu supplied the continuity of the inner product ([[§25 Projection and Orthogonal Decomposition#^lem-25-1|Lemma §25.1]]) at this point in lecture, but continuity of the norm suffices for the proof. This is step (i) of [[Functional Analysis Problem-Solving Techniques#^rem-t11|Technique 11]].
- **Why the hypotheses.** Each one is needed ([[§25 Projection and Orthogonal Decomposition#^rem-25-2|Remark §22]]). In ℓ¹, a norm with no inner product, closest points need not be unique. In an incomplete inner product space a minimizing sequence need not converge, and for an open K the infimum need not be attained. In a bare normed space only an almost-closest point is available, as in Step 2 of the [[§20 Compactness and the Unit Ball#^pf-20-2|proof]] of [[Riesz's Lemma]]. Since the parallelogram law characterizes inner-product norms ([[Jordan–von Neumann Theorem]]), the argument is specific to Hilbert spaces. Lax also proves the result in uniformly convex Banach spaces ([[§25 Projection and Orthogonal Decomposition#^rem-25-3|Remark §22]]; not covered).
- **Used for.** With K a closed subspace it gives the [[Orthogonal Decomposition Theorem]], and through it the [[Riesz Representation Theorem (Hilbert spaces)]]. In the sharp integral inequality [[§25 Projection and Orthogonal Decomposition#^prop-25-8|§25.8]], the minimizer is the point closest to 0 of a closed affine subspace ([[§25 Projection and Orthogonal Decomposition#^rem-25-8|Remark §22]]).
- **Finite dimensions.** LADR's minimization theorem ([[§22 Orthogonal Complements and Minimization Problems#^ladr-6-61|LADR 6.61]]) is the case where K is a subspace and the closest point is P_U v. There no limit has to be produced.
- **Also in [[Applied Linear Algebra]]:** [[§52 Orthogonal Projections#^thm-52-3|235 Thm. §52.3]] (K a subspace of ℝⁿ: the closest point is the orthogonal projection, with worked distances and least squares).
