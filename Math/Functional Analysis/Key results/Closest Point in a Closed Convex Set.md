---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 18.2", "projection theorem", "Lax §6.2, Thm 2"]
tags: [functional-analysis, hub]
---
![[§18 Projection and Orthogonal Decomposition#^thm-18-2]]

## Treated in
- [[§18 Projection and Orthogonal Decomposition#^thm-18-2|Theorem §18.2: Closest Point in a Closed Convex Set]], in [[§18 Projection and Orthogonal Decomposition]]

## Its proof uses
- [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Definition §2.3: Convex Set]]
- [[§8 Normed Linear Spaces#^prop-8-4|Proposition §8.4: A Norm is Continuous]]
- [[§8 Normed Linear Spaces#^def-8-5|Definition §8.5: Cauchy Sequence]]
- [[§8 Normed Linear Spaces#^def-8-6|Definition §8.6: Closed Subset]]
- [[§17 Cauchy–Schwarz and the Induced Norm#^def-17-1|Definition §17.1: Hilbert Space]]
- [[§17 Cauchy–Schwarz and the Induced Norm#^prop-17-3|Proposition §17.3: Parallelogram Law and Polarization]]
- [[§18 Projection and Orthogonal Decomposition#^lem-18-1|Lemma §18.1: The Inner Product is Continuous]]

## Used in (Functional Analysis)
- [[§18 Projection and Orthogonal Decomposition#^thm-18-4|Theorem §18.4: Orthogonal Decomposition]]
- [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-19-5|Proposition §19.5: Minimizing a Quadratic Functional over a Closed Convex Set]]

## Connections
- **How.** Take a minimizing sequence and apply the parallelogram law to x₀ − y_m and x₀ − y_n. Convexity puts the midpoint in K, which forces ‖y_n − y_m‖² < 2/m + 2/n. Completeness gives a limit, and closedness keeps it in K. The same midpoint argument proves uniqueness. This is step (i) of [[Functional Analysis Problem-Solving Techniques#^rem-t11|Technique 11]].
- **Why the hypotheses.** Each one is needed ([[§18 Projection and Orthogonal Decomposition#^rem-18-2|Remark §18]]). In ℓ¹, a norm with no inner product, closest points need not be unique. In an incomplete inner product space a minimizing sequence need not converge, and for an open K the infimum need not be attained. In a bare normed space only an almost-closest point is available, as in Step 2 of [[Riesz's Lemma]]. Since the parallelogram law characterizes inner-product norms ([[Jordan–von Neumann Theorem]]), the argument is specific to Hilbert spaces. Lax also proves the result in uniformly convex Banach spaces ([[§18 Projection and Orthogonal Decomposition#^rem-18-3|Remark §18]]; not covered).
- **Used for.** With K a closed subspace it gives the [[Orthogonal Decomposition Theorem]], and through it the [[Riesz Representation Theorem (Hilbert spaces)]]. In the sharp integral inequality [[§18 Projection and Orthogonal Decomposition#^prop-18-8|§18.8]], the minimizer is the point closest to 0 of a closed affine subspace ([[§18 Projection and Orthogonal Decomposition#^rem-18-8|Remark §18]]).
- **Finite dimensions.** LADR's minimization theorem ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-61|LADR 6.61]]) is the case where K is a subspace and the closest point is P_U v. There no limit has to be produced.
- **Also in [[Applied Linear Algebra]]:** [[§42 Orthogonal Projections#^thm-42-3|235 Thm. §42.3]] (K a subspace of ℝⁿ: the closest point is the orthogonal projection, with worked distances and least squares).
