---
subject: math
type: theorem
source: "[[Axler LADR]] 3.120"
ladr: "3.120"
page: 108
aliases: ["LADR 3.120"]
tags: [linear-algebra, ladr/3F]
---
> [!theorem] 3.120 Algebraic properties of dual maps
> For $T\in\Lin(V,W)$:
> - (a) $(S+T)'=S'+T'$ for all $S\in\Lin(V,W)$;
> - (b) $(\lambda T)'=\lambda T'$ for all $\lambda\in\F$;
> - (c) $(ST)'=T'S'$ for all $S\in\Lin(W,U)$.

> [!remark] Order reverses
> Like $(AB)^t=B^tA^t$, consistent with [[Matrix of T (LADR 3.132)]]. Axler writes $V'$, $T'$ for duality and saves $T^*$ for the adjoint.

> [!proof]-
> *(Filled in: (a), (b).)* $(S+T)'(\varphi)=\varphi\circ(S+T)=\varphi\circ S+\varphi\circ T$ since $\varphi$ is additive; similarly $(\lambda T)'(\varphi)=\varphi\circ(\lambda T)=\lambda(\varphi\circ T)$ by homogeneity of $\varphi$.
>
> (c) For $\varphi\in U'$: $(ST)'(\varphi)=\varphi\circ(ST)=(\varphi\circ S)\circ T=T'(S'(\varphi))$.

## Uses (in the proof)
- (definitions only)

## Connections
- So $T\mapsto T'$ is a linear map $\Lin(V,W)\to\Lin(W',V')$ reversing composition.
