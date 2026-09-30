---
subject: math
type: theorem
source: "[[Axler LADR]] 3.92"
ladr: "3.92"
page: 97
aliases: ["LADR 3.92"]
tags: [linear-algebra, ladr/3E]
---
> [!theorem] 3.92 Dimension of a product is the sum of dimensions
> If $V_1,\dots,V_m$ are finite-dimensional, then $V_1\times\dots\times V_m$ is finite-dimensional and
> $$
> \dim(V_1\times\dots\times V_m)=\dim V_1+\dots+\dim V_m .
> $$

> [!remark] Contrast with tensor products
> Dimensions add for products (and direct sums) but multiply for tensor products ([[Dimension of the tensor product of two vector spaces]]). In quantum mechanics, combining independent systems uses the tensor product, not the product.

> [!proof]-
> Choose a basis of each $V_k$. For each basis vector $e$ of $V_k$, take the element of the product with $e$ in slot $k$ and $0$ elsewhere. *(Filled in.)* These span: $(v_1,\dots,v_m)$ is the sum over $k$ of ($v_k$ expanded in its basis, placed in slot $k$). They are independent: a vanishing combination vanishes slot by slot, and in slot $k$ it is a combination of a basis of $V_k$. So they form a basis, of length $\sum_k\dim V_k$.

## Uses (in the proof)
- (definitions only)

## Connections
- Used in [[A sum is a direct sum if and only if dimensions add up]] and in the alternative proof of [[Dimension of a sum]].
