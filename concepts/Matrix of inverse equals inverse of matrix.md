---
subject: math
type: theorem
source: "[[Axler LADR]] 3.86"
ladr: "3.86"
page: 93
aliases: ["LADR 3.86"]
tags: [linear-algebra, ladr/3D]
---
> [!theorem] 3.86 Matrix of inverse equals inverse of matrix
> If $v_1,\dots,v_n$ is a basis of $V$ and $T\in\Lin(V)$ is invertible, then $\mathcal{M}(T^{-1})=\mathcal{M}(T)^{-1}$ (all with respect to $v_1,\dots,v_n$).

> [!proof]-
> *(Filled in; left as an exercise in Axler.)* By [[Matrix of product of linear maps (LADR 3.43)]], $\mathcal{M}(T^{-1})\mathcal{M}(T)=\mathcal{M}(T^{-1}T)=\mathcal{M}(I)=I$, and likewise $\mathcal{M}(T)\mathcal{M}(T^{-1})=I$. So $\mathcal{M}(T^{-1})$ is the inverse of $\mathcal{M}(T)$ ([[Invertible, inverse, A⁻¹]]).

## Uses (in the proof)
- [[Matrix of product of linear maps (LADR 3.43)]] (3.43)
- [[Invertible, inverse, A⁻¹]] (3.80)

## Connections
- So $T$ is invertible iff $\mathcal{M}(T)$ is (the converse via [[Dim L(V, W) = (dim V)(dim W)]]: an inverse matrix is the matrix of some map).
