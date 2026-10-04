---
subject: math
type: example
source: "[[Functional Analysis]]"
tags: ["math556", "workhorse"]
---
The sequences $e_j = (0, \ldots, 0, 1, 0, \ldots)$, with the $1$ in the $j$-th place, in the [[Sequence spaces ℓᵖ]]. They are linearly independent, which is what makes $\ell^p$ infinite-dimensional, and they are the sequence that shows what fails there: $\|e_i - e_j\|_p = 2^{1/p}$ for $i \neq j$, so $\{e_j\}$ has no convergent subsequence and the closed unit ball is not compact. [[The Unit Ball of an Infinite-Dimensional Space Is Not Compact|Theorem §18.5]] says that every infinite-dimensional normed space contains a sequence behaving like this one, even when no basis is available to write it down. The same vectors give the inequivalence of the $p$-norms on $\ell^p$ and the failure of the parallelogram law for $p \neq 2$, and in $\ell^2$ they are the standard orthonormal basis, with $(a, e_j) = a_j$. Its uses in MATH 556:

*Revisit sections:* [[§13 ℝⁿ, C［a,b］ and ℓᵖ|Chapter 3]] · [[§19 ℝⁿ, C［a,b］, ℓᵖ and Lᵖ|Chapter 4]] · [[§25 Sequence and Function Spaces|Chapter 5]]

- In $\ell^2$, $(z, e_i) = z_i$, so the finitely supported sequences have orthogonal complement $\{0\}$ ([[§1 Linear Spaces#^rem-1-10|§1]])
- On the unit sphere of $\ell^1$, $\|e_i - e_j\|_1 = 2$: equivalence of norms fails in infinite dimensions ([[§12 New Normed Spaces from Old#^rem-12-2|§12]])
- $e_1, e_2, \ldots$ are linearly independent, so $\ell^p$ is infinite-dimensional ([[§16 Minkowski's Inequality and the Spaces ℓᵖ#^rem-16-2|§16]])
- $s_n = e_1 + \cdots + e_n$: the norms $\|\cdot\|_p$ and $\|\cdot\|_q$ are not equivalent on $\ell^p$ ([[§16 Minkowski's Inequality and the Spaces ℓᵖ#^pf-16-4|§16]])
- The alternating sequence $e_1, e_2, e_1, e_2, \ldots$ is not Cauchy in $\ell^p$ ([[§16 Minkowski's Inequality and the Spaces ℓᵖ#^rem-16-5|§16]])
- The separated sequence: the closed unit ball of $\ell^p$ is not compact ([[§18 Compactness and the Unit Ball#^ex-18-2|§18]])
- $x = e_1$, $y = e_2$ violate the parallelogram law for $p \neq 2$ ([[§21 Cauchy–Schwarz and the Induced Norm#^pf-21-5|§21]])
- The shifted sequence $f_n = e_{n+1}$ is orthonormal but not complete ([[§24 Orthonormal Sets and Bases#^rem-24-8|§24]])
- The standard basis of $\ell^2$ is an orthonormal basis ([[§24 Orthonormal Sets and Bases#^ex-24-1|§24]])
- $e_1$ is not in the range of the shift $S(a_1, a_2, \ldots) = (0, a_1, a_2, \ldots)$ on $\ell^2$ ([[§24 Orthonormal Sets and Bases#^ex-24-2|§24]])

## In $\ell^2$, $(z, e_i) = z_i$, so the finitely supported sequences have orthogonal complement $\{0\}$
![[§1 Linear Spaces#^rem-1-10]]

## On the unit sphere of $\ell^1$, $\|e_i - e_j\|_1 = 2$: equivalence of norms fails in infinite dimensions
![[§12 New Normed Spaces from Old#^rem-12-2]]

## $e_1, e_2, \ldots$ are linearly independent, so $\ell^p$ is infinite-dimensional
![[§16 Minkowski's Inequality and the Spaces ℓᵖ#^rem-16-2]]

## $s_n = e_1 + \cdots + e_n$: the norms $\|\cdot\|_p$ and $\|\cdot\|_q$ are not equivalent on $\ell^p$
![[§16 Minkowski's Inequality and the Spaces ℓᵖ#^pf-16-4]]

## The alternating sequence $e_1, e_2, e_1, e_2, \ldots$ is not Cauchy in $\ell^p$
![[§16 Minkowski's Inequality and the Spaces ℓᵖ#^rem-16-5]]

## The separated sequence: the closed unit ball of $\ell^p$ is not compact
![[§18 Compactness and the Unit Ball#^ex-18-2]]

## $x = e_1$, $y = e_2$ violate the parallelogram law for $p \neq 2$
![[§21 Cauchy–Schwarz and the Induced Norm#^pf-21-5]]

## The shifted sequence $f_n = e_{n+1}$ is orthonormal but not complete
![[§24 Orthonormal Sets and Bases#^rem-24-8]]

## The standard basis of $\ell^2$ is an orthonormal basis
![[§24 Orthonormal Sets and Bases#^ex-24-1]]

## $e_1$ is not in the range of the shift $S(a_1, a_2, \ldots) = (0, a_1, a_2, \ldots)$ on $\ell^2$
![[§24 Orthonormal Sets and Bases#^ex-24-2]]
