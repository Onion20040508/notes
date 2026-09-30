---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.107"
ladr: "3.107"
page: 102
aliases: ["LADR 3.107", "first isomorphism theorem"]
tags: [linear-algebra, ladr/3E]
---
> [!theorem] 3.107 Null space and range of $\tilde T$
> Let $T\in\Lin(V,W)$ and define $\tilde T:V/(\nullsp T)\to W$ by $\tilde T(v+\nullsp T)=Tv$. Then
> - (a) $\tilde T\circ\pi=T$, where $\pi:V\to V/(\nullsp T)$ is the quotient map;
> - (b) $\tilde T$ is injective;
> - (c) $\range\tilde T=\range T$;
> - (d) $V/(\nullsp T)$ and $\range T$ are isomorphic.

> [!remark] First isomorphism theorem
> (d) is the vector-space case of $G/\ker\varphi\cong\operatorname{im}\varphi$. Taking dimensions with [[Dimension of quotient space]] recovers [[Fundamental theorem of linear maps]].

> [!proof]-
> *(Filled in: Axler 3.106.)* $\tilde T$ is well defined: if $v+\nullsp T=w+\nullsp T$ then $v-w\in\nullsp T$ ([[Two translates of a subspace are equal or disjoint]]), so $Tv=Tw$. It is linear because $T$ is and the operations on the quotient are computed on representatives.
>
> (a) $\tilde T(\pi(v))=\tilde T(v+\nullsp T)=Tv$.
>
> (b) If $\tilde T(v+\nullsp T)=0$ then $Tv=0$, so $v\in\nullsp T$ and $v+\nullsp T=0+\nullsp T$ ([[Two translates of a subspace are equal or disjoint]]). Thus $\nullsp\tilde T$ is trivial.
>
> (c) Immediate from the definition.
>
> (d) By (b) and (c), $\tilde T$ viewed as a map onto $\range T$ is an isomorphism.

## Uses (in the proof)
- [[Two translates of a subspace are equal or disjoint]] (3.101)

## Connections
- Same statement for groups and rings in MATH 591.
- Universal property: any linear map that kills $\nullsp T$ factors uniquely through $\pi$.
