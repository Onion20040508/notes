---
subject: math
type: example
source: "[[Functional Analysis]]"
tags: ["math556", "workhorse"]
---
The finitely supported sequences $c_{00} = \{ a \in \ell : a_i = 0 \text{ for all but finitely many } i \}$. For $1 \le p < \infty$ it is a subspace of $\ell^p$ ([[Sequence spaces ℓᵖ]]) that is not closed: the truncations $(a_1, \ldots, a_n, 0, \ldots)$ of any $a \in \ell^p$ lie in $c_{00}$ and converge to $a$, while $a = (2^{-i})$ is not finitely supported. So it is the standing example of an infinite-dimensional subspace that is not closed, showing why closedness hypotheses are needed, and in $\ell^2$ that they are sharp: $c_{00}^\perp = \{0\}$. On it all the $p$-norms are finite sums, which is why Minkowski's inequality is proved there first and then passed to all sequences by truncation. Its orthogonal complement in $\ell^2$ is computed with the [[Standard unit vectors eₙ]]. Its uses in MATH 556:

*Revisit sections:* [[§3 ℝⁿ and ℓ²|Chapter 1]] · [[§13 ℝⁿ, C［a,b］ and ℓᵖ|Chapter 3]] · [[§25 Sequence and Function Spaces|Chapter 5]]

- In $\ell^2$ the finitely supported sequences $Y$ have $Y^\perp = \{0\}$, so $Y^\perp$ is not a complement ([[§1 Linear Spaces#^rem-1-10|§1]])
- $c_{00}$ is not closed in $\ell^p$: finite-dimensional subspaces are closed, infinite-dimensional ones need not be ([[§12 New Normed Spaces from Old#^rem-12-3|§12]])
- Minkowski's inequality for finitely supported sequences ([[§16 Minkowski's Inequality and the Spaces ℓᵖ#^lem-16-2|§16]])
- $c_{00} \subset \ell^2$: both parts of the orthogonal decomposition fail without closedness ([[§22 Projection and Orthogonal Decomposition#^rem-22-5|§22]])
- Finitely supported sequences with rational entries are dense: $\ell^p$ is separable ([[§25 Sequence and Function Spaces#^prop-25-1|§25]])

## In $\ell^2$ the finitely supported sequences $Y$ have $Y^\perp = \{0\}$, so $Y^\perp$ is not a complement
![[§1 Linear Spaces#^rem-1-10]]

## $c_{00}$ is not closed in $\ell^p$: finite-dimensional subspaces are closed, infinite-dimensional ones need not be
![[§12 New Normed Spaces from Old#^rem-12-3]]

## Minkowski's inequality for finitely supported sequences
![[§16 Minkowski's Inequality and the Spaces ℓᵖ#^lem-16-2]]

## $c_{00} \subset \ell^2$: both parts of the orthogonal decomposition fail without closedness
![[§22 Projection and Orthogonal Decomposition#^rem-22-5]]

## Finitely supported sequences with rational entries are dense: $\ell^p$ is separable
![[§25 Sequence and Function Spaces#^prop-25-1]]
