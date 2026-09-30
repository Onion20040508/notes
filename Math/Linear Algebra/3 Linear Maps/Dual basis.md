---
subject: math
type: definition
source: "[[Linear Algebra]] 3.112"
ladr: "3.112"
page: 106
aliases: ["LADR 3.112"]
tags: [linear-algebra, ladr/3F]
---
> [!definition] 3.112 Dual basis
> If $v_1,\dots,v_n$ is a basis of $V$, its *dual basis* is the list $\varphi_1,\dots,\varphi_n$ in $V'$ where
> $$
> \varphi_j(v_k)=\begin{cases}1 & k=j,\\ 0 & k\neq j.\end{cases}
> $$

> [!remark] Well defined
> Each $\varphi_j$ exists and is unique by [[Linear map lemma]].

## Connections
- $\varphi_j$ reads off the $j$-th coordinate: [[Dual basis gives coefficients for linear combination]]. It is a basis: [[Dual basis is a basis of the dual space]].
- Physics: $\langle e_j|$ against an orthonormal $|e_k\rangle$; index notation $e^j(e_k)=\delta^j_k$ for upper/lower indices.
