---
subject: math
type: theorem
source: "[[Axler LADR]] 3.13"
ladr: "3.13"
page: 59
aliases: ["LADR 3.13"]
tags: [linear-algebra, ladr/3B]
---
> [!theorem] 3.13 The null space is a subspace
> If $T\in\Lin(V,W)$, then $\nullsp T$ is a subspace of $V$.

> [!proof]-
> $T(0)=0$ by [[Linear maps take 0 to 0]], so $0\in\nullsp T$. If $u,v\in\nullsp T$ then $T(u+v)=Tu+Tv=0$. If $u\in\nullsp T$, $\lambda\in\F$, then $T(\lambda u)=\lambda Tu=0$. By [[Conditions for a subspace]], $\nullsp T$ is a subspace.

## Uses (in the proof)
- [[Linear maps take 0 to 0]] (3.10)
- [[Conditions for a subspace]] (1.34)

## Connections
- Companion: [[The range is a subspace]].
