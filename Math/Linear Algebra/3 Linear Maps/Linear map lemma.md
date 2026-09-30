---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.4"
ladr: "3.4"
page: 54
aliases: ["LADR 3.4"]
tags: [linear-algebra, ladr/3A]
---
> [!theorem] 3.4 Linear map lemma
> Suppose $v_1,\dots,v_n$ is a basis of $V$ and $w_1,\dots,w_n\in W$. Then there is a unique linear map $T:V\to W$ with $Tv_k=w_k$ for each $k$.

> [!proof]-
> **Existence.** Define $T(c_1v_1+\dots+c_nv_n)=c_1w_1+\dots+c_nw_n$. This is a well-defined function because every $v\in V$ has exactly one such representation ([[Criterion for basis]]). Taking $c_k=1$ and the other $c$'s $0$ gives $Tv_k=w_k$. If $u=\sum a_kv_k$ and $v=\sum c_kv_k$, then
> $$
> T(u+v)=\textstyle\sum(a_k+c_k)w_k=\sum a_kw_k+\sum c_kw_k=Tu+Tv,
> $$
> and similarly $T(\lambda v)=\sum\lambda c_kw_k=\lambda Tv$. So $T$ is linear.
>
> **Uniqueness.** If $T$ is linear with $Tv_k=w_k$, then homogeneity and additivity force $T(\sum c_kv_k)=\sum c_kw_k$, so $T$ is determined on $\Span(v_1,\dots,v_n)=V$.

## Uses (in the proof)
- [[Criterion for basis]] (2.28)

## Connections
- The reason a linear map is the same data as its matrix: [[Matrix of a linear map, M(T)]], and why $\mathcal{M}$ is bijective in [[Dim L(V, W) = (dim V)(dim W)]].
- Builds the isomorphism in [[Dimension shows whether vector spaces are isomorphic]].
