---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.128"
ladr: "3.128"
page: 111
aliases: ["LADR 3.128", "null T′"]
tags: [linear-algebra, ladr/3F]
---
> [!theorem] 3.128 The null space of $T'$
> Let $V,W$ be finite-dimensional and $T\in\Lin(V,W)$. Then
> - (a) $\nullsp T'=(\range T)^0$;
> - (b) $\dim\nullsp T'=\dim\nullsp T+\dim W-\dim V$.
>
> **Corollary (Axler 3.129).** $T$ is surjective $\iff T'$ is injective.

> [!proof]-
> (a) $\varphi\in\nullsp T'\iff\varphi\circ T=0\iff\varphi(Tv)=0$ for all $v\iff\varphi\in(\range T)^0$. (This part needs no finite-dimensionality.)
>
> (b) By (a), [[Dimension of the annihilator]] and [[Fundamental theorem of linear maps]]:
> $$
> \dim\nullsp T'=\dim W-\dim\range T=\dim W-(\dim V-\dim\nullsp T).
> $$
>
> *Corollary.* $T$ surjective $\iff\range T=W\iff(\range T)^0=\{0\}$ ([[Condition for the annihilator to equal {0} or the whole space]](a)) $\iff\nullsp T'=\{0\}$ (by (a)) $\iff T'$ injective.

## Uses (in the proof)
- [[Dimension of the annihilator]] (3.125)
- [[Fundamental theorem of linear maps]] (3.21)
- [[Condition for the annihilator to equal {0} or the whole space]] (3.127)

## Connections
- Companion: [[The range of T]]. Useful when injectivity of $T'$ is easier to check than surjectivity of $T$.
