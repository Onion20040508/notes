---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.50"
ladr: "3.50"
page: 76
aliases: ["LADR 3.50"]
tags: [linear-algebra, ladr/3C]
---
> [!theorem] 3.50 Linear combination of columns
> If $A$ is $m$-by-$n$ and $b=(b_1,\dots,b_n)^t$ is $n$-by-$1$, then
> $$
> Ab=b_1A_{\cdot,1}+\dots+b_nA_{\cdot,n},
> $$
> a linear combination of the columns of $A$ with coefficients from $b$.

> [!proof]-
> Row $k$ of $Ab$ is $A_{k,1}b_1+\dots+A_{k,n}b_n$, which is also row $k$ of $b_1A_{\cdot,1}+\dots+b_nA_{\cdot,n}$.

## Uses (in the proof)
- (definitions only)

## Connections
- Why $\range$ of a matrix map is the column space; used in [[Linear maps act like matrix multiplication]] and [[Dimension of range T equals column rank of M(T)]].
