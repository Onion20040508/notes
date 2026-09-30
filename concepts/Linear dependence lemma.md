---
subject: math
type: theorem
source: "[[Axler LADR]] 2.19"
ladr: "2.19"
page: 33
aliases: ["LADR 2.19"]
tags: [linear-algebra, ladr/2A]
---
> [!theorem] 2.19 Linear dependence lemma
> Suppose $v_1,\dots,v_m$ is linearly dependent in $V$. Then there is $k\in\{1,\dots,m\}$ with
> $$
> v_k\in\Span(v_1,\dots,v_{k-1}).
> $$
> Moreover, for any such $k$, removing $v_k$ from the list does not change its span.

> [!remark] The case $k=1$
> $v_1\in\Span(\,)=\{0\}$ means $v_1=0$; the proof still works with empty sums.

> [!proof]-
> Pick $a_1,\dots,a_m$, not all $0$, with $a_1v_1+\dots+a_mv_m=0$, and let $k$ be the **largest** index with $a_k\neq0$. Then
> $$
> v_k=-\frac{a_1}{a_k}v_1-\dots-\frac{a_{k-1}}{a_k}v_{k-1}\in\Span(v_1,\dots,v_{k-1}).
> $$
> For the second part, let $k$ be any index with $v_k=b_1v_1+\dots+b_{k-1}v_{k-1}$. In any $u=c_1v_1+\dots+c_mv_m$, substitute this expression for $v_k$; the result is a linear combination of the list without $v_k$. So removing $v_k$ keeps the span.

## Uses (in the proof)
- (definitions only)

## Connections
- The engine of Chapter 2: [[Length of linearly independent list ≤ length of spanning list]], [[Finite-dimensional subspaces]], [[Every spanning list contains a basis]]. Through those it underlies almost everything that follows.
