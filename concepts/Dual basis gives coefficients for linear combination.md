---
subject: math
type: theorem
source: "[[Axler LADR]] 3.114"
ladr: "3.114"
page: 106
aliases: ["LADR 3.114"]
tags: [linear-algebra, ladr/3F]
---
> [!theorem] 3.114 Dual basis gives coefficients for linear combination
> If $v_1,\dots,v_n$ is a basis of $V$ with dual basis $\varphi_1,\dots,\varphi_n$, then for every $v\in V$
> $$
> v=\varphi_1(v)v_1+\dots+\varphi_n(v)v_n .
> $$

> [!proof]-
> Write $v=c_1v_1+\dots+c_nv_n$. Applying $\varphi_j$ gives $\varphi_j(v)=c_j$.

## Uses (in the proof)
- (definitions only)

## Connections
- Orthonormal analogue: [[Writing a vector as a linear combination of an orthonormal basis]] with $\varphi_j=\ip{\cdot}{e_j}$.
