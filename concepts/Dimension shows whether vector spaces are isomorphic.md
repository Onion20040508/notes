---
subject: math
type: theorem
source: "[[Axler LADR]] 3.70"
ladr: "3.70"
page: 86
aliases: ["LADR 3.70"]
tags: [linear-algebra, ladr/3D]
---
> [!theorem] 3.70 Dimension shows whether vector spaces are isomorphic
> Two finite-dimensional vector spaces over $\F$ are isomorphic if and only if they have the same dimension.

> [!remark] Why not just study $\F^n$
> Every $n$-dimensional space is isomorphic to $\F^n$, but only via a choice of basis. Natural constructions (null spaces, ranges, quotients, duals) do not come with preferred bases.

> [!proof]-
> ($\Rightarrow$) If $T:V\to W$ is an isomorphism, then $\nullsp T=\{0\}$ and $\range T=W$, so [[Fundamental theorem of linear maps]] gives $\dim V=0+\dim W$.
>
> ($\Leftarrow$) Let $v_1,\dots,v_n$ and $w_1,\dots,w_n$ be bases. Define $T(\sum c_kv_k)=\sum c_kw_k$ (a linear map by [[Linear map lemma]]). It is surjective since the $w$'s span, and injective since the $w$'s are independent ($\sum c_kw_k=0\Rightarrow$ all $c_k=0$). So $T$ is an isomorphism by [[Invertibility ⟺ injectivity and surjectivity]].

## Uses (in the proof)
- [[Fundamental theorem of linear maps]] (3.21)
- [[Linear map lemma]] (3.4)
- [[Invertibility ⟺ injectivity and surjectivity]] (3.63)

## Connections
- Coordinates as the isomorphism $v\mapsto\mathcal{M}(v)$: [[Matrix of a vector, M(v)]]. Dimension of $\Lin(V,W)$: [[Dim L(V, W) = (dim V)(dim W)]].
