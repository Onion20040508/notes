---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.93"
ladr: "3.93"
page: 98
aliases: ["LADR 3.93"]
tags: [linear-algebra, ladr/3E]
---
> [!theorem] 3.93 Products and direct sums
> Let $V_1,\dots,V_m$ be subspaces of $V$ and define $\Gamma:V_1\times\dots\times V_m\to V_1+\dots+V_m$ by
> $$
> \Gamma(v_1,\dots,v_m)=v_1+\dots+v_m .
> $$
> Then $V_1+\dots+V_m$ is a direct sum if and only if $\Gamma$ is injective.

> [!remark] Always surjective
> $\Gamma$ is onto by the definition of the sum, so "injective" can be replaced by "invertible": a direct sum is canonically isomorphic to the product.

> [!proof]-
> By [[Injectivity ⟺ null space equals {0}]], $\Gamma$ is injective iff the only way to write $0=v_1+\dots+v_m$ with $v_k\in V_k$ is with all $v_k=0$. By [[Condition for a direct sum]] this is exactly the condition for a direct sum.

## Uses (in the proof)
- [[Injectivity ⟺ null space equals {0}]] (3.15)
- [[Condition for a direct sum]] (1.45)

## Connections
- Dimension version: [[A sum is a direct sum if and only if dimensions add up]].
