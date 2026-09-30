---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.56"
ladr: "3.56"
page: 78
aliases: ["LADR 3.56"]
tags: [linear-algebra, ladr/3C]
---
> [!theorem] 3.56 Column–row factorization
> Suppose $A\in\F^{m,n}$ has column rank $c\ge1$. Then $A=CR$ for some $C\in\F^{m,c}$ and $R\in\F^{c,n}$.

> [!proof]-
> Reduce the list of columns $A_{\cdot,1},\dots,A_{\cdot,n}$ to a basis of their span ([[Every spanning list contains a basis]]); it has length $c$. Let $C$ be the $m$-by-$c$ matrix with these basis vectors as columns. Each column $A_{\cdot,k}$ is a linear combination of the columns of $C$; put its coefficients into column $k$ of a $c$-by-$n$ matrix $R$. Then $A=CR$ by [[Matrix multiplication as linear combinations of columns]](a).

## Uses (in the proof)
- [[Every spanning list contains a basis]] (2.30)
- [[Matrix multiplication as linear combinations of columns]] (3.51)

## Connections
- Immediately gives [[Column rank equals row rank (LADR 3.57)]]. Refinements with orthonormal columns: [[QR factorization]], and the SVD [[Matrix version of SVD]].
