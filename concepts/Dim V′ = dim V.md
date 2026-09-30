---
subject: math
type: theorem
source: "[[Axler LADR]] 3.111"
ladr: "3.111"
page: 105
aliases: ["LADR 3.111"]
tags: [linear-algebra, ladr/3F]
---
> [!theorem] 3.111 Dim V′ = dim V
> If $V$ is finite-dimensional, then $V'$ is finite-dimensional and $\dim V'=\dim V$.

> [!remark] Isomorphic but not canonically
> $V\cong V'$ by [[Dimension shows whether vector spaces are isomorphic]], but the isomorphism depends on a basis (via [[Dual basis]]). An inner product gives a canonical one ([[Riesz representation theorem]]); in general only $V\cong V''$ is canonical.

> [!proof]-
> By [[Dim L(V, W) = (dim V)(dim W)]], $\dim V'=\dim\Lin(V,\F)=(\dim V)(\dim\F)=\dim V$.

## Uses (in the proof)
- [[Dim L(V, W) = (dim V)(dim W)]] (3.72)

## Connections
- Used in [[Dual basis is a basis of the dual space]], [[Dimension of the annihilator]], [[The range of T]].
