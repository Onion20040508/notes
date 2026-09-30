---
subject: math
type: theorem
source: "[[Axler LADR]] 3.8"
ladr: "3.8"
page: 56
aliases: ["LADR 3.8"]
tags: [linear-algebra, ladr/3A]
---
> [!theorem] 3.8 Algebraic properties of products of linear maps
> Whenever the products make sense:
> - **associativity** $(T_1T_2)T_3=T_1(T_2T_3)$;
> - **identity** $TI=IT=T$ for $T\in\Lin(V,W)$ (first $I$ on $V$, second on $W$);
> - **distributive properties** $(S_1+S_2)T=S_1T+S_2T$ and $S(T_1+T_2)=ST_1+ST_2$.

> [!remark] Not commutative
> $ST\neq TS$ in general, even when both make sense. For example on $\Poly(\R)$, with $D$ = differentiation and $T$ = multiplication by $x$: $(DT-TD)p=p$.

> [!proof]-
> *(Filled in.)* Each identity is checked pointwise. Associativity: both sides send $u$ to $T_1(T_2(T_3u))$. Distributivity: $(S_1+S_2)(Tu)=S_1Tu+S_2Tu$ by definition of $S_1+S_2$; and $S(T_1u+T_2u)=ST_1u+ST_2u$ by additivity of $S$ (this is where linearity of $S$ is needed).

## Uses (in the proof)
- (definitions only)

## Connections
- Commutation relations such as $DT-TD=I$ are the prototype of $[\hat{p},\hat{x}]$ in quantum mechanics; in finite dimensions $ST-TS=I$ is impossible ([[Identity operator is not the difference of ST and TS]]).
- Commuting operators: [[Commute]].
