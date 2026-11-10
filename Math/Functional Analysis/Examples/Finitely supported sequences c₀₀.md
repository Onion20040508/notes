---
subject: math
type: example
source: "[[Functional Analysis]]"
tags: ["math556", "workhorse"]
---
The finitely supported sequences $c_{00} = \{ a \in \ell : a_i = 0 \text{ for all but finitely many } i \}$. For $1 \le p < \infty$ it is a subspace of $\ell^p$ ([[Sequence spaces ℓᵖ]]) that is not closed: the truncations $(a_1, \ldots, a_n, 0, \ldots)$ of any $a \in \ell^p$ lie in $c_{00}$ and converge to $a$, while $a = (2^{-i})$ is not finitely supported. So it is the standing example of an infinite-dimensional subspace that is not closed, showing why closedness hypotheses are needed, and in $\ell^2$ that they are sharp: $c_{00}^\perp = \{0\}$. On it all the $p$-norms are finite sums, which is why Minkowski's inequality is proved there first and then passed to all sequences by truncation. Its orthogonal complement in $\ell^2$ is computed with the [[Standard unit vectors eₙ]]. Its uses in MATH 556:

*Revisit sections:* [[§4 ℝⁿ and ℓ²|Chapter 1]] · [[§15 ℝⁿ, C［a,b］ and ℓᵖ|Chapter 3]] · [[§29 Sequence and Function Spaces|Chapter 5]]

- In $\ell^2$ the finitely supported sequences $Y$ have $Y^\perp = \{0\}$, so $Y^\perp$ is not a complement ([[§2 Quotient Spaces and Complements#^ex-2-3|Ex. §2.3]])
- $c_{00}$ is not closed in $\ell^p$: finite-dimensional subspaces are closed, infinite-dimensional ones need not be ([[§14 New Normed Spaces from Old#^ex-14-3|Ex. §14.3]])
- Minkowski's inequality for finitely supported sequences ([[§18 Minkowski's Inequality and the Spaces ℓᵖ#^lem-18-2|§18]])
- $c_{00} \subset \ell^2$: both parts of the orthogonal decomposition fail without closedness ([[§25 Projection and Orthogonal Decomposition#^ex-25-5|Ex. §25.5]])
- Finitely supported sequences with rational entries are dense: $\ell^p$ is [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|separable]] ([[§29 Sequence and Function Spaces#^prop-29-1|§29]])
- On $c_{00}$ the functionals $A_n x = n\,x_n$ are pointwise but not uniformly bounded: the uniform boundedness principle needs completeness ([[§42 Uniform Boundedness and Approximation#^ex-42-2|§42]])
- An unbounded weak-$\ast$ null sequence on $c_{00}$ ([[§43 Weak and Weak-Star Convergence#^ex-43-7|§43]])

## In $\ell^2$ the finitely supported sequences $Y$ have $Y^\perp = \{0\}$, so $Y^\perp$ is not a complement
![[§2 Quotient Spaces and Complements#^ex-2-3]]

## $c_{00}$ is not closed in $\ell^p$: finite-dimensional subspaces are closed, infinite-dimensional ones need not be
![[§14 New Normed Spaces from Old#^ex-14-3]]

## Minkowski's inequality for finitely supported sequences
![[§18 Minkowski's Inequality and the Spaces ℓᵖ#^lem-18-2]]

## $c_{00} \subset \ell^2$: both parts of the orthogonal decomposition fail without closedness
![[§25 Projection and Orthogonal Decomposition#^ex-25-5]]

## Finitely supported sequences with rational entries are dense: $\ell^p$ is separable
![[§29 Sequence and Function Spaces#^prop-29-1]]

## On $c_{00}$ the functionals $A_n x = n\,x_n$ are pointwise but not uniformly bounded: the uniform boundedness principle needs completeness
![[§42 Uniform Boundedness and Approximation#^ex-42-2]]

## An unbounded weak-$\ast$ null sequence on $c_{00}$
![[§43 Weak and Weak-Star Convergence#^ex-43-7]]
