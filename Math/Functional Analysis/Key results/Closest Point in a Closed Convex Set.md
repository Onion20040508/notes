---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 22.2", "projection theorem", "Lax §6.2, Thm 2"]
tags: [functional-analysis, hub]
---
![[§22 Projection and Orthogonal Decomposition#^thm-22-2]]

## Treated in
- [[§22 Projection and Orthogonal Decomposition#^thm-22-2|Theorem §22.2: Closest Point in a Closed Convex Set]], in [[§22 Projection and Orthogonal Decomposition]]

## Its proof uses
- [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Definition §2.3: Convex Set]]
- [[§10 Normed Linear Spaces#^prop-10-4|Proposition §10.4: A Norm is Continuous]]
- [[§10 Normed Linear Spaces#^def-10-5|Definition §10.5: Cauchy Sequence]]
- [[§10 Normed Linear Spaces#^def-10-6|Definition §10.6: Closed Subset]]
- [[§21 Cauchy–Schwarz and the Induced Norm#^def-21-1|Definition §21.1: Hilbert Space]]
- [[§21 Cauchy–Schwarz and the Induced Norm#^prop-21-3|Proposition §21.3: Parallelogram Law and Polarization]]

## Used in (Functional Analysis)
- [[§22 Projection and Orthogonal Decomposition#^thm-22-4|Theorem §22.4: Orthogonal Decomposition]]
- [[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-23-5|Proposition §23.5: Minimizing a Quadratic Functional over a Closed Convex Set]]

## Connections
- **How.** Take a minimizing sequence and apply the parallelogram law to x₀ − y_m and x₀ − y_n. Convexity puts the midpoint in K, which forces ‖y_n − y_m‖² < 2/m + 2/n. Completeness gives a limit, and closedness keeps it in K. The same midpoint argument proves uniqueness. Wu supplied the continuity of the inner product ([[§22 Projection and Orthogonal Decomposition#^lem-22-1|Lemma §22.1]]) at this point in lecture, but continuity of the norm suffices for the proof. This is step (i) of [[Functional Analysis Problem-Solving Techniques#^rem-t11|Technique 11]].
- **Why the hypotheses.** Each one is needed ([[§22 Projection and Orthogonal Decomposition#^rem-22-2|Remark §22]]). In ℓ¹, a norm with no inner product, closest points need not be unique. In an incomplete inner product space a minimizing sequence need not converge, and for an open K the infimum need not be attained. In a bare normed space only an almost-closest point is available, as in Step 2 of the [[§18 Compactness and the Unit Ball#^pf-18-2|proof]] of [[Riesz's Lemma]]. Since the parallelogram law characterizes inner-product norms ([[Jordan–von Neumann Theorem]]), the argument is specific to Hilbert spaces. Lax also proves the result in uniformly convex Banach spaces ([[§22 Projection and Orthogonal Decomposition#^rem-22-3|Remark §22]]; not covered).
- **Used for.** With K a closed subspace it gives the [[Orthogonal Decomposition Theorem]], and through it the [[Riesz Representation Theorem (Hilbert spaces)]]. In the sharp integral inequality [[§22 Projection and Orthogonal Decomposition#^prop-22-8|§22.8]], the minimizer is the point closest to 0 of a closed affine subspace ([[§22 Projection and Orthogonal Decomposition#^rem-22-8|Remark §22]]).
- **Finite dimensions.** LADR's minimization theorem ([[§22 Orthogonal Complements and Minimization Problems#^ladr-6-61|LADR 6.61]]) is the case where K is a subspace and the closest point is P_U v. There no limit has to be produced.
- **Also in [[Applied Linear Algebra]]:** [[§52 Orthogonal Projections#^thm-52-3|235 Thm. §52.3]] (K a subspace of ℝⁿ: the closest point is the orthogonal projection, with worked distances and least squares).
