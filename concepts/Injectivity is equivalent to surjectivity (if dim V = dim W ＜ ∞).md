---
subject: math
type: theorem
source: "[[Axler LADR]] 3.65"
ladr: "3.65"
page: 84
aliases: ["LADR 3.65"]
tags: [linear-algebra, ladr/3D]
---
> [!theorem] 3.65 Injectivity is equivalent to surjectivity (if dim V = dim W < ∞)
> Suppose $V,W$ are finite-dimensional, $\dim V=\dim W$, and $T\in\Lin(V,W)$. Then
> $$
> T\text{ invertible}\iff T\text{ injective}\iff T\text{ surjective}.
> $$

> [!remark] Finite dimension is essential
> On $\F^\infty$, the backward shift is surjective but not injective and the forward shift is injective but not surjective.

> [!proof]-
> By [[Fundamental theorem of linear maps]], $\dim V=\dim\nullsp T+\dim\range T$. If $T$ is injective, then $\dim\nullsp T=0$ ([[Injectivity ⟺ null space equals {0}]]), so $\dim\range T=\dim V=\dim W$ and $\range T=W$ by [[Subspace of full dimension equals the whole space]]. If $T$ is surjective, then $\dim\nullsp T=\dim V-\dim W=0$, so $T$ is injective. Either condition therefore gives both, hence invertibility by [[Invertibility ⟺ injectivity and surjectivity]].

## Uses (in the proof)
- [[Fundamental theorem of linear maps]] (3.21)
- [[Injectivity ⟺ null space equals {0}]] (3.15)
- [[Subspace of full dimension equals the whole space]] (2.39)
- [[Invertibility ⟺ injectivity and surjectivity]] (3.63)

## Connections
- Matrix and operator consequences: [[ST = I ⟺ TS = I (on vector spaces of the same dimension)]]. Eigenvalue criterion: [[Equivalent conditions to be an eigenvalue]].
