---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 46.6", "N(M') = R(M)^perp", "Lax §15.1, Thm 5"]
tags: [functional-analysis, hub]
---
![[§46 The Transpose#^thm-46-6]]

## Treated in
- [[§46 The Transpose#^thm-46-6|Theorem §46.6: Null Spaces and Ranges of M and M']], in [[§46 The Transpose]]

## Its proof uses
- [[§36 Duality in Normed Spaces#^cor-36-3|Corollary §36.3: Bounded Functionals Separate Points]]

## Used in (Functional Analysis)
- [[§46 The Transpose#^cor-46-7|Corollary §46.7: The Closure of the Range]]

## Connections
- **What it says.** $N(M') = R(M)^\perp$: a functional is killed by $M'$ exactly when it vanishes on the range of $M$. And $N(M) = {}^\perp R(M')$: a vector is killed by $M$ exactly when every functional $M'\ell$ vanishes on it.
- **How.** Both follow from $\langle Mx, \ell \rangle = \langle x, M'\ell \rangle$; the second half also needs functionals that separate points, a consequence of Hahn–Banach ([[§36 Duality in Normed Spaces#^cor-36-3|Cor. §36.3]]).
- **Used for.** The closure of the range is ${}^\perp N(M')$ ([[§46 The Transpose#^cor-46-7|Cor. §46.7]]); when the range is closed, $Mx = y$ is solvable exactly when $y$ is annihilated by $N(M')$, the infinite-dimensional form of the solvability criterion for matrices. Whether the range is closed: [[§41 The Open Mapping Theorem and Its Consequences#^prop-41-5|§41.5]].
- **Finite dimensions.** [[§12 Duality#^ladr-3-128|LADR 3.128]] and [[§12 Duality#^ladr-3-130|LADR 3.130]].
- **In Lax.** §15.1, Thm 5(ii)–(iii).
