---
subject: math
type: theorem
source: "[[Linear Algebra]] 5.18"
ladr: "5.18"
page: 139
aliases: ["LADR 5.18"]
tags: [linear-algebra, ladr/5A]
---
> [!theorem] 5.18 Null space and range of p(T) are invariant under T
> For $T\in\Lin(V)$ and $p\in\Poly(\F)$, the subspaces $\nullsp p(T)$ and $\range p(T)$ are invariant under $T$.

> [!proof]-
> If $p(T)u=0$ then $p(T)(Tu)=T(p(T)u)=T0=0$ (since $T$ commutes with $p(T)$, [[Multiplicative properties]]). If $u=p(T)v$ then $Tu=p(T)(Tv)\in\range p(T)$.

## Uses (in the proof)
- [[Multiplicative properties]] (5.17)

## Connections
- Produces the invariant subspaces used in [[Existence, uniqueness, and degree of minimal polynomial]], [[Even-dimensional null space]], [[Operators on odd-dimensional vector spaces have eigenvalues]]; eigenspaces and generalized eigenspaces are special cases.
