---
subject: math
type: theorem
source: "[[Axler LADR]] 1.40"
ladr: "1.40"
page: 21
aliases: ["LADR 1.40"]
tags: [linear-algebra, ladr/1C]
---
> [!theorem] 1.40 Sum of subspaces is the smallest containing subspace
> If $V_1,\dots,V_m$ are subspaces of $V$, then $V_1+\dots+V_m$ is the smallest subspace of $V$ containing $V_1,\dots,V_m$.

> [!remark] Analogy
> Sums of subspaces play the role of unions of sets: the union of two subspaces is usually not a subspace, and the sum is the smallest subspace containing both.

> [!proof]-
> *(Filled in.)* $0=0+\dots+0$ lies in the sum;
> $(v_1+\dots+v_m)+(w_1+\dots+w_m)=(v_1+w_1)+\dots+(v_m+w_m)$ and $\lambda(v_1+\dots+v_m)=\lambda v_1+\dots+\lambda v_m$ stay in the sum because each $V_k$ is a subspace. So the sum is a subspace by [[Conditions for a subspace]].
>
> It contains each $V_k$ (take all other summands $0$). Any subspace containing every $V_k$ is closed under finite sums, so it contains $V_1+\dots+V_m$.

## Uses (in the proof)
- [[Conditions for a subspace]] (1.34)

## Connections
- Same shape of result: [[Span is the smallest containing subspace]] for spans.
