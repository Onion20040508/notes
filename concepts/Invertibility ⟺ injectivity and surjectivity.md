---
subject: math
type: theorem
source: "[[Axler LADR]] 3.63"
ladr: "3.63"
page: 83
aliases: ["LADR 3.63"]
tags: [linear-algebra, ladr/3D]
---
> [!theorem] 3.63 Invertibility ⟺ injectivity and surjectivity
> A linear map is invertible if and only if it is injective and surjective.

> [!proof]-
> ($\Rightarrow$) If $Tu=Tv$ then $u=T^{-1}Tu=T^{-1}Tv=v$. Any $w\in W$ equals $T(T^{-1}w)$.
>
> ($\Leftarrow$) For $w\in W$ let $S(w)$ be the unique $v$ with $Tv=w$ (exists by surjectivity, unique by injectivity). Then $TS=I_W$. For $v\in V$, $T(STv)=(TS)(Tv)=Tv$, so $STv=v$ by injectivity; thus $ST=I_V$. Linearity of $S$: $T(Sw_1+Sw_2)=w_1+w_2$, so $Sw_1+Sw_2$ is the unique preimage of $w_1+w_2$, i.e. $S(w_1+w_2)=Sw_1+Sw_2$. *(Filled in.)* Likewise $T(\lambda Sw)=\lambda w$ gives $S(\lambda w)=\lambda Sw$.

## Uses (in the proof)
- (definitions only)

## Connections
- Linear bijections automatically have linear inverses. In finite equal dimensions, one condition suffices: [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]].
