---
subject: math
type: theorem
source: "[[Linear Algebra]] 2.22"
ladr: "2.22"
page: 35
aliases: ["LADR 2.22"]
tags: [linear-algebra, ladr/2A]
---
> [!theorem] 2.22 Length of linearly independent list ≤ length of spanning list
> In a finite-dimensional vector space, the length of every linearly independent list is at most the length of every spanning list.

> [!proof]-
> Let $u_1,\dots,u_m$ be linearly independent and $w_1,\dots,w_n$ span $V$. We show $m\le n$ by an exchange process of $m$ steps, each adding one $u$ and removing one $w$ while keeping a spanning list of length $n$.
>
> **Step 1.** Let $B=w_1,\dots,w_n$. Since $B$ spans, $u_1,w_1,\dots,w_n$ is linearly dependent. By [[Linear dependence lemma]] some vector of it lies in the span of the previous ones. It is not $u_1$, since $u_1\neq0$ (independence). So some $w$ can be removed, leaving a spanning list $B$ of length $n$ consisting of $u_1$ and $n-1$ of the $w$'s.
>
> **Step $k$** ($2\le k\le m$). $B$ spans, so adjoining $u_k$ right after $u_1,\dots,u_{k-1}$ gives a dependent list of length $n+1$. By [[Linear dependence lemma]] some vector lies in the span of its predecessors. It cannot be one of $u_1,\dots,u_k$, because they are linearly independent. So it is a $w$; remove it. The new $B$ has length $n$, consists of $u_1,\dots,u_k$ and some $w$'s, and still spans.
>
> After step $m$, $B$ contains all of $u_1,\dots,u_m$ and has length $n$, so $m\le n$. (At each step there was a $w$ left to remove, since otherwise the $u$'s would be dependent.)

## Uses (in the proof)
- [[Linear dependence lemma]] (2.19)

## Connections
- Gives well-defined dimension: [[Basis length does not depend on basis]]. Also [[Finite-dimensional subspaces]] and [[Dimension of a subspace]].
- Consequence in Chapter 3: [[Linear map to a lower-dimensional space is not injective]] and [[Linear map to a higher-dimensional space is not surjective]] (via [[Fundamental theorem of linear maps]]).
