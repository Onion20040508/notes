---
subject: math
type: theorem
source: "[[Axler LADR]] 3.133"
ladr: "3.133"
page: 114
aliases: ["LADR 3.133"]
tags: [linear-algebra, ladr/3F]
---
> [!theorem] 3.133 Column rank equals row rank
> For every $A\in\F^{m,n}$, the column rank of $A$ equals the row rank of $A$.

> [!proof]-
> Let $T:\F^{n,1}\to\F^{m,1}$, $Tx=Ax$, so $\mathcal{M}(T)=A$ in the standard bases. Then
> $$
> \text{col rank }A=\dim\range T=\dim\range T'=\text{col rank }\mathcal{M}(T')=\text{col rank }A^t=\text{row rank }A,
> $$
> using [[Dimension of range T equals column rank of M(T)]], [[The range of T]](a), [[Dimension of range T equals column rank of M(T)]], [[Matrix of T (LADR 3.132)]].

## Uses (in the proof)
- [[Dimension of range T equals column rank of M(T)]] (3.78)
- [[The range of T]] (3.130)
- [[Matrix of T (LADR 3.132)]] (3.132)

## Connections
- First proof by column–row factorization: [[Column rank equals row rank (LADR 3.57)]]. A third proof via adjoints appears in Chapter 7.
