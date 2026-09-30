---
subject: math
type: theorem
source: "[[Linear Algebra]] 2.25"
ladr: "2.25"
page: 36
aliases: ["LADR 2.25"]
tags: [linear-algebra, ladr/2A]
---
> [!theorem] 2.25 Finite-dimensional subspaces
> Every subspace of a finite-dimensional vector space is finite-dimensional.

> [!proof]-
> Let $U$ be a subspace of finite-dimensional $V$.
>
> **Step 1.** If $U=\{0\}$, done. Otherwise choose $u_1\in U$, $u_1\neq0$.
>
> **Step $k$.** If $U=\Span(u_1,\dots,u_{k-1})$, done. Otherwise choose $u_k\in U\setminus\Span(u_1,\dots,u_{k-1})$.
>
> At every stage no vector of the list lies in the span of the previous ones, so the list is linearly independent by [[Linear dependence lemma]]. By [[Length of linearly independent list ≤ length of spanning list]] its length cannot exceed the length of a spanning list of $V$, so the process stops, and when it stops $U$ is spanned by a finite list.

## Uses (in the proof)
- [[Linear dependence lemma]] (2.19)
- [[Length of linearly independent list ≤ length of spanning list]] (2.22)

## Connections
- Used implicitly in [[Fundamental theorem of linear maps]] (null space is finite-dimensional) and in [[Every subspace of V is part of a direct sum equal to V]].
