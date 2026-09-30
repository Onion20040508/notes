---
subject: math
type: theorem
source: "[[Axler LADR]] 3.130"
ladr: "3.130"
page: 112
aliases: ["LADR 3.130", "range T′"]
tags: [linear-algebra, ladr/3F]
---
> [!theorem] 3.130 The range of $T'$
> Let $V,W$ be finite-dimensional and $T\in\Lin(V,W)$. Then
> - (a) $\dim\range T'=\dim\range T$;
> - (b) $\range T'=(\nullsp T)^0$.
>
> **Corollary (Axler 3.131).** $T$ is injective $\iff T'$ is surjective.

> [!proof]-
> (a) By [[Fundamental theorem of linear maps]], [[Dim V′ = dim V]], [[The null space of T]](a) and [[Dimension of the annihilator]]:
> $$
> \dim\range T'=\dim W'-\dim\nullsp T'=\dim W-\dim(\range T)^0=\dim\range T .
> $$
> (b) If $\varphi=T'(\psi)$ and $v\in\nullsp T$, then $\varphi(v)=\psi(Tv)=\psi(0)=0$; so $\range T'\subseteq(\nullsp T)^0$. Both have the same dimension: $\dim\range T'=\dim\range T=\dim V-\dim\nullsp T=\dim(\nullsp T)^0$ (by (a), [[Fundamental theorem of linear maps]], [[Dimension of the annihilator]]). Hence equality ([[Subspace of full dimension equals the whole space]]).
>
> *Corollary.* $T$ injective $\iff\nullsp T=\{0\}\iff(\nullsp T)^0=V'$ ([[Condition for the annihilator to equal {0} or the whole space]](b)) $\iff\range T'=V'$ (by (b)).

## Uses (in the proof)
- [[Fundamental theorem of linear maps]] (3.21)
- [[Dim V′ = dim V]] (3.111)
- [[The null space of T]] (3.128)
- [[Dimension of the annihilator]] (3.125)
- [[Subspace of full dimension equals the whole space]] (2.39)
- [[Condition for the annihilator to equal {0} or the whole space]] (3.127)

## Connections
- (a) is the abstract form of row rank $=$ column rank: [[Column rank equals row rank (LADR 3.133)]].
