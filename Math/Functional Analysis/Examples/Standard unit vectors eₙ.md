---
subject: math
type: example
source: "[[Functional Analysis]]"
tags: ["math556", "workhorse"]
---
The sequences $e_j = (0, \ldots, 0, 1, 0, \ldots)$, with the $1$ in the $j$-th place, in the [[Sequence spaces ℓᵖ]]. They are linearly independent, which is what makes $\ell^p$ infinite-dimensional, and they are the sequence that shows what fails there: $\|e_i - e_j\|_p = 2^{1/p}$ for $i \neq j$, so $\{e_j\}$ has no convergent subsequence and the closed unit ball is not compact. [[The Unit Ball of an Infinite-Dimensional Space Is Not Compact|Theorem §15.5]] says that every infinite-dimensional normed space contains a sequence behaving like this one, even when no basis is available to write it down. The same vectors give the inequivalence of the $p$-norms on $\ell^p$ and the failure of the parallelogram law for $p \neq 2$, and in $\ell^2$ they are the standard orthonormal basis, with $(a, e_j) = a_j$. Its uses in MATH 556:

*Revisit sections:* [[§15 ℝⁿ, C［a,b］ and ℓᵖ|Chapter 3]] · [[§21 ℝⁿ, C［a,b］, ℓᵖ and Lᵖ|Chapter 4]] · [[§29 Sequence and Function Spaces|Chapter 5]]

- In $\ell^2$, $(z, e_i) = z_i$, so the finitely supported sequences have orthogonal complement $\{0\}$ ([[§2 Quotient Spaces and Complements#^rem-2-5|§2]])
- On the unit sphere of $\ell^1$, $\|e_i - e_j\|_1 = 2$: equivalence of norms fails in infinite dimensions ([[§14 New Normed Spaces from Old#^rem-14-2|§14]])
- $e_1, e_2, \ldots$ are linearly independent, so $\ell^p$ is infinite-dimensional ([[§18 Minkowski's Inequality and the Spaces ℓᵖ#^rem-18-2|§18]])
- $s_n = e_1 + \cdots + e_n$: the norms $\|\cdot\|_p$ and $\|\cdot\|_q$ are not equivalent on $\ell^p$ ([[§18 Minkowski's Inequality and the Spaces ℓᵖ#^pf-18-4|§18]])
- The alternating sequence $e_1, e_2, e_1, e_2, \ldots$ is not Cauchy in $\ell^p$ ([[§18 Minkowski's Inequality and the Spaces ℓᵖ#^rem-18-5|§18]])
- The separated sequence: the closed unit ball of $\ell^p$ is not compact ([[§20 Compactness and the Unit Ball#^ex-20-2|§20]])
- $x = e_1$, $y = e_2$ violate the parallelogram law for $p \neq 2$ ([[§24 The Parallelogram Law and Jordan–von Neumann#^pf-24-3|§24]])
- The shifted sequence $f_n = e_{n+1}$ is orthonormal but not complete ([[§27 Orthonormal Sets and Bases#^rem-27-8|§27]])
- The standard basis of $\ell^2$ is an orthonormal basis ([[§27 Orthonormal Sets and Bases#^ex-27-1|§27]])
- $e_1$ is not in the range of the shift $S(a_1, a_2, \ldots) = (0, a_1, a_2, \ldots)$ on $\ell^2$ ([[§28 Existence of Orthonormal Bases and Separability#^ex-28-1|§28]])

## In $\ell^2$, $(z, e_i) = z_i$, so the finitely supported sequences have orthogonal complement $\{0\}$
![[§2 Quotient Spaces and Complements#^rem-2-5]]

## On the unit sphere of $\ell^1$, $\|e_i - e_j\|_1 = 2$: equivalence of norms fails in infinite dimensions
![[§14 New Normed Spaces from Old#^rem-14-2]]

## $e_1, e_2, \ldots$ are linearly independent, so $\ell^p$ is infinite-dimensional
![[§18 Minkowski's Inequality and the Spaces ℓᵖ#^rem-18-2]]

## $s_n = e_1 + \cdots + e_n$: the norms $\|\cdot\|_p$ and $\|\cdot\|_q$ are not equivalent on $\ell^p$
![[§18 Minkowski's Inequality and the Spaces ℓᵖ#^pf-18-4]]

## The alternating sequence $e_1, e_2, e_1, e_2, \ldots$ is not Cauchy in $\ell^p$
![[§18 Minkowski's Inequality and the Spaces ℓᵖ#^rem-18-5]]

## The separated sequence: the closed unit ball of $\ell^p$ is not compact
![[§20 Compactness and the Unit Ball#^ex-20-2]]

## $x = e_1$, $y = e_2$ violate the parallelogram law for $p \neq 2$
![[§24 The Parallelogram Law and Jordan–von Neumann#^pf-24-3]]

## The shifted sequence $f_n = e_{n+1}$ is orthonormal but not complete
![[§27 Orthonormal Sets and Bases#^rem-27-8]]

## The standard basis of $\ell^2$ is an orthonormal basis
![[§27 Orthonormal Sets and Bases#^ex-27-1]]

## $e_1$ is not in the range of the shift $S(a_1, a_2, \ldots) = (0, a_1, a_2, \ldots)$ on $\ell^2$
![[§28 Existence of Orthonormal Bases and Separability#^ex-28-1]]
