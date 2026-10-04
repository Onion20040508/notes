---
subject: math
type: example
source: "[[Functional Analysis]]"
tags: ["math556", "workhorse"]
---
For $1 \le p \le \infty$, $\ell^p$ is the space of sequences $a = (a_1, a_2, \ldots)$ with $\|a\|_p = \bigl(\sum_i |a_i|^p\bigr)^{1/p} < \infty$, respectively $\|a\|_\infty = \sup_i |a_i| < \infty$. It is the first genuinely infinite-dimensional normed space in the course, and, as Wu stressed, without $L^p$ the course has few examples beyond sequence spaces. Unlike the norms $\|\cdot\|_p$ on $\mathbb{R}^n$ ([[Norms on ℝⁿ and their unit balls]]), the spaces $\ell^p$ for different $p$ are different sets, and their norms are not equivalent where both are defined. Each $\ell^p$ is a Banach space, its closed unit ball is not compact, $\ell^2$ is the one with an inner product, and in $\ell^1$ closest points need not be unique. The standard vectors have their own note, [[Standard unit vectors eₙ]], and so does the subspace of finitely supported sequences, [[Finitely supported sequences c₀₀]]; the function-space analogue is in [[L² function spaces]]. Its uses in MATH 556:

*Revisit sections:* [[§3 ℝⁿ and ℓ²|Chapter 1]] · [[§13 ℝⁿ, C［a,b］ and ℓᵖ|Chapter 3]] · [[§19 ℝⁿ, C［a,b］, ℓᵖ and Lᵖ|Chapter 4]] · [[§25 Sequence and Function Spaces|Chapter 5]] · [[§29 ℝⁿ, Cᵐ and Lᵖ|Chapter 6]]

- The completion is complete by the plan of the $\ell^p$ proof, with a diagonal candidate ([[§11 Completeness#^rem-11-5|§11]])
- The sequence space $\ell$ and the $p$-norms, with values in $[0, \infty]$ ([[§15 Hölder's Inequality for Sequences#^def-15-1|§15]])
- On all of $\ell$ the $p$-norms may be infinite; they are norms where they are finite ([[§15 Hölder's Inequality for Sequences#^rem-15-1|§15]])
- Definition of $\ell^p$ ([[§16 Minkowski's Inequality and the Spaces ℓᵖ#^def-16-1|§16]])
- $\ell^p$ is a normed linear space ([[§16 Minkowski's Inequality and the Spaces ℓᵖ#^prop-16-3|§16]])
- The first genuinely infinite-dimensional normed space ([[§16 Minkowski's Inequality and the Spaces ℓᵖ#^rem-16-2|§16]])
- Nesting: $\ell^p \subsetneq \ell^q$ for $p < q$, with norms that are not equivalent ([[§16 Minkowski's Inequality and the Spaces ℓᵖ#^prop-16-4|§16]])
- $\ell^p$ is a Banach space ([[§16 Minkowski's Inequality and the Spaces ℓᵖ#^thm-16-5|§16]])
- The closed unit ball of $\ell^p$ is not compact ([[§18 Compactness and the Unit Ball#^ex-18-2|§18]])
- $\ell^2$ with $(a, b) = \sum_i a_i \overline{b_i}$, the one $\ell^p$ where this converges ([[§20 Definition and Examples#^ex-20-2|§20]])
- $\ell^2$ is a Hilbert space ([[§21 Cauchy–Schwarz and the Induced Norm#^ex-21-1|§21]])
- For $p \neq 2$ the norm of $\ell^p$ does not come from an inner product ([[§21 Cauchy–Schwarz and the Induced Norm#^cor-21-5|§21]])
- In $\ell^1$ closest points need not be unique ([[§22 Projection and Orthogonal Decomposition#^rem-22-2|§22]])
- The standard basis of $\ell^2$ is an orthonormal basis ([[§24 Orthonormal Sets and Bases#^ex-24-1|§24]])
- $\ell^p$ is separable for $1 \le p < \infty$ ([[§25 Sequence and Function Spaces#^prop-25-1|§25]])
- $c_0$ is a separable Banach space ([[§25 Sequence and Function Spaces#^prop-25-2|§25]])
- $\ell^\infty$ is not separable ([[§25 Sequence and Function Spaces#^prop-25-3|§25]])
- The shift $S(a_1, a_2, \ldots) = (0, a_1, a_2, \ldots)$ on $\ell^2$: an isometry that is not an isomorphism ([[§24 Orthonormal Sets and Bases#^ex-24-2|§24]])
- Classification of separable Hilbert spaces ([[§24 Orthonormal Sets and Bases#^thm-24-15|§24]])
- $(\ell^2)' = \ell^2$ by the Riesz representation theorem ([[§27 Dual Spaces#^ex-27-1|§27]])

## The completion is complete by the plan of the $\ell^p$ proof, with a diagonal candidate
![[§11 Completeness#^rem-11-5]]

## The sequence space $\ell$ and the $p$-norms, with values in $[0, \infty]$
![[§15 Hölder's Inequality for Sequences#^def-15-1]]

## On all of $\ell$ the $p$-norms may be infinite; they are norms where they are finite
![[§15 Hölder's Inequality for Sequences#^rem-15-1]]

## Definition of $\ell^p$
![[§16 Minkowski's Inequality and the Spaces ℓᵖ#^def-16-1]]

## $\ell^p$ is a normed linear space
![[§16 Minkowski's Inequality and the Spaces ℓᵖ#^prop-16-3]]

## The first genuinely infinite-dimensional normed space
![[§16 Minkowski's Inequality and the Spaces ℓᵖ#^rem-16-2]]

## Nesting: $\ell^p \subsetneq \ell^q$ for $p < q$, with norms that are not equivalent
![[§16 Minkowski's Inequality and the Spaces ℓᵖ#^prop-16-4]]

## $\ell^p$ is a Banach space
![[§16 Minkowski's Inequality and the Spaces ℓᵖ#^thm-16-5]]

## The closed unit ball of $\ell^p$ is not compact
![[§18 Compactness and the Unit Ball#^ex-18-2]]

## $\ell^2$ with $(a, b) = \sum_i a_i \overline{b_i}$, the one $\ell^p$ where this converges
![[§20 Definition and Examples#^ex-20-2]]

## $\ell^2$ is a Hilbert space
![[§21 Cauchy–Schwarz and the Induced Norm#^ex-21-1]]

## For $p \neq 2$ the norm of $\ell^p$ does not come from an inner product
![[§21 Cauchy–Schwarz and the Induced Norm#^cor-21-5]]

## In $\ell^1$ closest points need not be unique
![[§22 Projection and Orthogonal Decomposition#^rem-22-2]]

## The standard basis of $\ell^2$ is an orthonormal basis
![[§24 Orthonormal Sets and Bases#^ex-24-1]]

## $\ell^p$ is separable for $1 \le p < \infty$
![[§25 Sequence and Function Spaces#^prop-25-1]]

## $c_0$ is a separable Banach space
![[§25 Sequence and Function Spaces#^prop-25-2]]

## $\ell^\infty$ is not separable
![[§25 Sequence and Function Spaces#^prop-25-3]]

## The shift $S(a_1, a_2, \ldots) = (0, a_1, a_2, \ldots)$ on $\ell^2$: an isometry that is not an isomorphism
![[§24 Orthonormal Sets and Bases#^ex-24-2]]

## Classification of separable Hilbert spaces
![[§24 Orthonormal Sets and Bases#^thm-24-15]]

## $(\ell^2)' = \ell^2$ by the Riesz representation theorem
![[§27 Dual Spaces#^ex-27-1]]
