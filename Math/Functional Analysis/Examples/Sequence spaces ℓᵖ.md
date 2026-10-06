---
subject: math
type: example
source: "[[Functional Analysis]]"
tags: ["math556", "workhorse"]
---
For $1 \le p \le \infty$, $\ell^p$ is the space of sequences $a = (a_1, a_2, \ldots)$ with $\|a\|_p = \bigl(\sum_i |a_i|^p\bigr)^{1/p} < \infty$, respectively $\|a\|_\infty = \sup_i |a_i| < \infty$. It is the first genuinely infinite-dimensional normed space in the course, and, as Wu stressed, without $L^p$ the course has few examples beyond sequence spaces. Unlike the norms $\|\cdot\|_p$ on $\mathbb{R}^n$ ([[Norms on ℝⁿ and their unit balls]]), the spaces $\ell^p$ for different $p$ are different sets, and their norms are not equivalent where both are defined. Each $\ell^p$ is a Banach space, its closed unit ball is not compact, $\ell^2$ is the one with an inner product, and in $\ell^1$ closest points need not be unique. The standard vectors have their own note, [[Standard unit vectors eₙ]], and so does the subspace of finitely supported sequences, [[Finitely supported sequences c₀₀]]; the function-space analogue is in [[L² function spaces]]. Its uses in MATH 556:

*Revisit sections:* [[§4 ℝⁿ and ℓ²|Chapter 1]] · [[§15 ℝⁿ, C［a,b］ and ℓᵖ|Chapter 3]] · [[§21 ℝⁿ, C［a,b］, ℓᵖ and Lᵖ|Chapter 4]] · [[§29 Sequence and Function Spaces|Chapter 5]] · [[§33 ℝⁿ, Cᵐ and Lᵖ|Chapter 6]]

- The completion is complete by the plan of the $\ell^p$ proof, with a diagonal candidate ([[§13 The Completion of a Normed Space#^rem-13-2|§11]])
- The sequence space $\ell$ and the $p$-norms, with values in $[0, \infty]$ ([[§17 Hölder's Inequality for Sequences#^def-17-1|§15]])
- On all of $\ell$ the $p$-norms may be infinite; they are norms where they are finite ([[§17 Hölder's Inequality for Sequences#^rem-17-1|§15]])
- Definition of $\ell^p$ ([[§18 Minkowski's Inequality and the Spaces ℓᵖ#^def-18-1|§16]])
- $\ell^p$ is a normed linear space ([[§18 Minkowski's Inequality and the Spaces ℓᵖ#^prop-18-3|§16]])
- The first genuinely infinite-dimensional normed space ([[§18 Minkowski's Inequality and the Spaces ℓᵖ#^rem-18-2|§16]])
- Nesting: $\ell^p \subsetneq \ell^q$ for $p < q$, with norms that are not equivalent ([[§18 Minkowski's Inequality and the Spaces ℓᵖ#^prop-18-4|§16]])
- $\ell^p$ is a Banach space ([[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-5|§16]])
- The closed unit ball of $\ell^p$ is not compact ([[§20 Compactness and the Unit Ball#^ex-20-2|§18]])
- $\ell^2$ with $(a, b) = \sum_i a_i \overline{b_i}$, the one $\ell^p$ where this converges ([[§22 Definition and Examples#^ex-22-2|§20]])
- $\ell^2$ is a Hilbert space ([[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-1|§21]])
- For $p \neq 2$ the norm of $\ell^p$ does not come from an inner product ([[§24 The Parallelogram Law and Jordan–von Neumann#^cor-24-3|§21]])
- In $\ell^1$ closest points need not be unique ([[§25 Projection and Orthogonal Decomposition#^rem-25-2|§22]])
- The standard basis of $\ell^2$ is an orthonormal basis ([[§27 Orthonormal Sets and Bases#^ex-27-1|§24]])
- $\ell^p$ is separable for $1 \le p < \infty$ ([[§29 Sequence and Function Spaces#^prop-29-1|§25]])
- $c_0$ is a separable Banach space ([[§29 Sequence and Function Spaces#^prop-29-2|§25]])
- $\ell^\infty$ is not separable ([[§29 Sequence and Function Spaces#^prop-29-3|§25]])
- The shift $S(a_1, a_2, \ldots) = (0, a_1, a_2, \ldots)$ on $\ell^2$: an isometry that is not an isomorphism ([[§28 Existence of Orthonormal Bases and Separability#^ex-28-1|§24]])
- Classification of separable Hilbert spaces ([[§28 Existence of Orthonormal Bases and Separability#^thm-28-4|§24]])
- $(\ell^2)' = \ell^2$ by the Riesz representation theorem ([[§31 Dual Spaces#^ex-31-1|§27]])

## The completion is complete by the plan of the $\ell^p$ proof, with a diagonal candidate
![[§13 The Completion of a Normed Space#^rem-13-2]]

## The sequence space $\ell$ and the $p$-norms, with values in $[0, \infty]$
![[§17 Hölder's Inequality for Sequences#^def-17-1]]

## On all of $\ell$ the $p$-norms may be infinite; they are norms where they are finite
![[§17 Hölder's Inequality for Sequences#^rem-17-1]]

## Definition of $\ell^p$
![[§18 Minkowski's Inequality and the Spaces ℓᵖ#^def-18-1]]

## $\ell^p$ is a normed linear space
![[§18 Minkowski's Inequality and the Spaces ℓᵖ#^prop-18-3]]

## The first genuinely infinite-dimensional normed space
![[§18 Minkowski's Inequality and the Spaces ℓᵖ#^rem-18-2]]

## Nesting: $\ell^p \subsetneq \ell^q$ for $p < q$, with norms that are not equivalent
![[§18 Minkowski's Inequality and the Spaces ℓᵖ#^prop-18-4]]

## $\ell^p$ is a Banach space
![[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-5]]

## The closed unit ball of $\ell^p$ is not compact
![[§20 Compactness and the Unit Ball#^ex-20-2]]

## $\ell^2$ with $(a, b) = \sum_i a_i \overline{b_i}$, the one $\ell^p$ where this converges
![[§22 Definition and Examples#^ex-22-2]]

## $\ell^2$ is a Hilbert space
![[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-1]]

## For $p \neq 2$ the norm of $\ell^p$ does not come from an inner product
![[§24 The Parallelogram Law and Jordan–von Neumann#^cor-24-3]]

## In $\ell^1$ closest points need not be unique
![[§25 Projection and Orthogonal Decomposition#^rem-25-2]]

## The standard basis of $\ell^2$ is an orthonormal basis
![[§27 Orthonormal Sets and Bases#^ex-27-1]]

## $\ell^p$ is separable for $1 \le p < \infty$
![[§29 Sequence and Function Spaces#^prop-29-1]]

## $c_0$ is a separable Banach space
![[§29 Sequence and Function Spaces#^prop-29-2]]

## $\ell^\infty$ is not separable
![[§29 Sequence and Function Spaces#^prop-29-3]]

## The shift $S(a_1, a_2, \ldots) = (0, a_1, a_2, \ldots)$ on $\ell^2$: an isometry that is not an isomorphism
![[§28 Existence of Orthonormal Bases and Separability#^ex-28-1]]

## Classification of separable Hilbert spaces
![[§28 Existence of Orthonormal Bases and Separability#^thm-28-4]]

## $(\ell^2)' = \ell^2$ by the Riesz representation theorem
![[§31 Dual Spaces#^ex-31-1]]
