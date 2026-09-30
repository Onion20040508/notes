---
subject: math
type: theorem
source: "[[Axler LADR]] 3.15"
ladr: "3.15"
page: 60
aliases: ["LADR 3.15"]
tags: [linear-algebra, ladr/3B]
---
> [!theorem] 3.15 Injectivity ⟺ null space equals {0}
> Let $T\in\Lin(V,W)$. Then $T$ is injective if and only if $\nullsp T=\{0\}$.

> [!proof]-
> ($\Rightarrow$) $\{0\}\subseteq\nullsp T$ by [[Linear maps take 0 to 0]]. If $v\in\nullsp T$ then $Tv=0=T(0)$, so $v=0$ by injectivity.
>
> ($\Leftarrow$) If $Tu=Tv$ then $T(u-v)=Tu-Tv=0$, so $u-v\in\nullsp T=\{0\}$, i.e. $u=v$.

## Uses (in the proof)
- [[Linear maps take 0 to 0]] (3.10)

## Connections
- Same 'uniqueness at $0$' principle as [[Condition for a direct sum]] and [[Linearly independent]].
- Used in [[Linear map to a lower-dimensional space is not injective]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]], [[ST = I ⟺ TS = I (on vector spaces of the same dimension)]].
