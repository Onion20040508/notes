---
subject: math
type: definition
source: "[[Linear Algebra]] 3.7"
ladr: "3.7"
page: 55
aliases: ["LADR 3.7"]
tags: [linear-algebra, ladr/3A]
---
> [!definition] 3.7 Product of linear maps
> If $T\in\Lin(U,V)$ and $S\in\Lin(V,W)$, the *product* $ST\in\Lin(U,W)$ is $(ST)(u)=S(Tu)$.

> [!remark] Composition
> $ST$ is $S\circ T$; it is defined only when $T$ lands in the domain of $S$. It is linear: $ST(u+u')=S(Tu+Tu')=STu+STu'$, and similarly for scalars.

## Connections
- Algebra of products: [[Algebraic properties of products of linear maps]]. Matrix side: [[Matrix multiplication]], [[Matrix of product of linear maps (LADR 3.43)]].
