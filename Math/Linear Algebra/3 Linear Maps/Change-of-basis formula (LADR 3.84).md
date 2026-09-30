---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.84"
ladr: "3.84"
page: 93
aliases: ["LADR 3.84"]
tags: [linear-algebra, ladr/3D]
---
> [!theorem] 3.84 Change-of-basis formula
> Let $T\in\Lin(V)$ and let $u_1,\dots,u_n$, $v_1,\dots,v_n$ be bases of $V$. With
> $$
> A=\mathcal{M}(T,(u)),\quad B=\mathcal{M}(T,(v)),\quad C=\mathcal{M}(I,(u),(v)),
> $$
> we have $A=C^{-1}BC$.

> [!remark] Reading it right to left
> $C$ converts $u$-coordinates to $v$-coordinates, $B$ applies $T$ in $v$-coordinates, $C^{-1}$ converts back.

> [!proof]-
> By [[Matrix of product of linear maps (LADR 3.81)]] (with $S=I$, target basis $u$) and [[Matrix of identity operator with respect to two bases]]: $A=C^{-1}\,\mathcal{M}(T,(u),(v))$. By [[Matrix of product of linear maps (LADR 3.81)]] again (with $T$ replaced by $I$ and $S$ by $T$): $\mathcal{M}(T,(u),(v))=BC$. Substitute.

## Uses (in the proof)
- [[Matrix of product of linear maps (LADR 3.81)]] (3.81)
- [[Matrix of identity operator with respect to two bases]] (3.82)

## Connections
- Similar matrices describe the same operator; similarity invariants: [[Trace of matrix of operator does not depend on basis]], [[Determinant is a similarity invariant]].
- Physics: with orthonormal bases $C$ is unitary and this is the familiar $A=U^\dagger BU$ change of representation.
- Bilinear-form version (different rule, $C^tBC$): [[Change-of-basis formula (LADR 9.7)]].
