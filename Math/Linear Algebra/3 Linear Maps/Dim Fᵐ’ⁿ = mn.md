---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.40"
ladr: "3.40"
page: 72
aliases: ["LADR 3.40"]
tags: [linear-algebra, ladr/3C]
---
> [!theorem] 3.40 Dim Fᵐ’ⁿ = mn
> For positive integers $m,n$, $\F^{m,n}$ with entrywise addition and scalar multiplication is a vector space of dimension $mn$.

> [!proof]-
> *(Filled in.)* The axioms hold entrywise because they hold in $\F$; the zero is the all-$0$ matrix. Let $E^{(j,k)}$ be the matrix with $1$ in entry $(j,k)$ and $0$ elsewhere. Every $A$ equals $\sum_{j,k}A_{j,k}E^{(j,k)}$, and this representation is unique (the coefficients are read off entrywise), so the $mn$ matrices $E^{(j,k)}$ form a basis ([[Criterion for basis]]).

## Uses (in the proof)
- [[Criterion for basis]] (2.28)

## Connections
- Combined with $\Lin(V,W)\cong\F^{m,n}$: [[Dim L(V, W) = (dim V)(dim W)]].
