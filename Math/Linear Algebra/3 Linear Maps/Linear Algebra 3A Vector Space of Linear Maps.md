---
type: section
subject: "[[Linear Algebra]]"
chapter: 3
section: "3A"
tags: [linear-algebra]
---
← [[Linear Algebra 2C Dimension]] · ↑ [[Linear Algebra — 3 Linear Maps]] · [[Linear Algebra 3B Null Spaces and Ranges]] →

> [!definition] 3.1 Linear map
> A *linear map* from $V$ to $W$ is a function $T:V\to W$ with
> - **additivity** $T(u+v)=Tu+Tv$ for all $u,v\in V$;
> - **homogeneity** $T(\lambda v)=\lambda(Tv)$ for all $\lambda\in\F$, $v\in V$.
>
> $\Lin(V,W)$ denotes the set of linear maps $V\to W$, and $\Lin(V)=\Lin(V,V)$.

^ladr-3-1

> [!remark] Not every 'linear' function
> $f(x)=mx+b$ on $\R$ is a linear map only when $b=0$ (see [[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-10|Linear maps take 0 to 0]]). And $\cos$ is not linear, whatever one might wish about $\cos(x+y)$.

> [!remark]- Connections
> - Determined by values on a basis: [[Linear map lemma]]. Vector space of linear maps: [[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-5|Addition and scalar multiplication on L(V, W)]]. Composition: [[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-7|Product of linear maps]].
> - Two subspaces attached to every linear map: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-11|Null space, null T]], [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-16|Range]], tied together by [[Fundamental theorem of linear maps]].
> - Physics: observables and time evolution in quantum mechanics are linear maps on the state space.

> [!remark] 3.2 Notation: L(V, W), L(V) (p. 52)

^ladr-3-2

> [!example] 3.3 Linear maps (p. 52)
> The standard list, used throughout the book:
> - **zero** $0\in\Lin(V,W)$, $0v=0$ (the $0$ on the left is a map, on the right a vector of $W$);
> - **identity** $I\in\Lin(V)$, $Iv=v$;
> - **differentiation** $D\in\Lin(\Poly(\R))$, $Dp=p'$: linearity *is* the rules $(f+g)'=f'+g'$, $(\lambda f)'=\lambda f'$;
> - **integration** $T\in\Lin(\Poly(\R),\R)$, $Tp=\int_0^1p$;
> - **multiplication by $x^2$** $T\in\Lin(\Poly(\R))$, $(Tp)(x)=x^2p(x)$;
> - **backward shift** $T\in\Lin(\F^\infty)$, $T(x_1,x_2,x_3,\dots)=(x_2,x_3,\dots)$;
> - **from $\R^3$ to $\R^2$** $T(x,y,z)=(2x-y+3z,\ 7x+5y-6z)$;
> - **from $\F^n$ to $\F^m$** $T(x_1,\dots,x_n)=\big(\sum_kA_{1,k}x_k,\dots,\sum_kA_{m,k}x_k\big)$ for fixed scalars $A_{j,k}$; every linear map $\F^n\to\F^m$ has this form (this is where matrices come from, [[Linear Algebra 3C Matrices#^ladr-3-31|3.31]]);
> - **composition** for fixed $q\in\Poly(\R)$, $(Tp)(x)=p(q(x))$.

^ladr-3-3

> [!theorem] 3.4 Linear map lemma
> Suppose $v_1,\dots,v_n$ is a basis of $V$ and $w_1,\dots,w_n\in W$. Then there is a unique linear map $T:V\to W$ with $Tv_k=w_k$ for each $k$.

^ladr-3-4

> [!proof]+
> **Existence.** Define $T(c_1v_1+\dots+c_nv_n)=c_1w_1+\dots+c_nw_n$. This is a well-defined function because every $v\in V$ has exactly one such representation ([[Linear Algebra 2B Bases#^ladr-2-28|Criterion for basis]]). Taking $c_k=1$ and the other $c$'s $0$ gives $Tv_k=w_k$. If $u=\sum a_kv_k$ and $v=\sum c_kv_k$, then
> $$
> T(u+v)=\textstyle\sum(a_k+c_k)w_k=\sum a_kw_k+\sum c_kw_k=Tu+Tv,
> $$
> and similarly $T(\lambda v)=\sum\lambda c_kw_k=\lambda Tv$. So $T$ is linear.
>
> **Uniqueness.** If $T$ is linear with $Tv_k=w_k$, then homogeneity and additivity force $T(\sum c_kv_k)=\sum c_kw_k$, so $T$ is determined on $\Span(v_1,\dots,v_n)=V$.

*Uses:* [[Linear Algebra 2B Bases#^ladr-2-28|2.28]]

%% ex:3.4-fig %%
> [!example] The linear map lemma, pictured
> The basis $v_1,v_2$ of $V$ gives the grid of points $c_1v_1+c_2v_2$. Choosing $w_1,w_2$ determines $T$ on all of it: the grid is carried to the grid of $w_1,w_2$, and each point goes to the point with the same coefficients, e.g. $T(2v_1+v_2)=2w_1+w_2$.
>
> ![[ladr-3.4-linear-map-lemma.svg|520]]

> [!definition] 3.5 Addition and scalar multiplication on L(V, W)
> For $S,T\in\Lin(V,W)$ and $\lambda\in\F$, define $S+T$ and $\lambda T$ in $\Lin(V,W)$ by
> $$
> (S+T)(v)=Sv+Tv,\qquad (\lambda T)(v)=\lambda(Tv).
> $$

^ladr-3-5

> [!remark] $\Lin(V,W)$ is a vector space
> One checks that $S+T$ and $\lambda T$ are again linear; with these operations $\Lin(V,W)$ is a vector space (Axler 3.6) whose zero is the zero map.

> [!remark]- Connections
> - Its dimension: [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-72|Dim L(V, W) = (dim V)(dim W)]]. Matrices respect the operations: [[Linear Algebra 3C Matrices#^ladr-3-35|Matrix of the sum of linear maps]], [[Linear Algebra 3C Matrices#^ladr-3-38|The matrix of a scalar times a linear map]].

> [!definition] 3.7 Product of linear maps
> If $T\in\Lin(U,V)$ and $S\in\Lin(V,W)$, the *product* $ST\in\Lin(U,W)$ is $(ST)(u)=S(Tu)$.

^ladr-3-7

> [!remark] Composition
> $ST$ is $S\circ T$; it is defined only when $T$ lands in the domain of $S$. It is linear: $ST(u+u')=S(Tu+Tu')=STu+STu'$, and similarly for scalars.

> [!remark]- Connections
> - Algebra of products: [[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-8|Algebraic properties of products of linear maps]]. Matrix side: [[Linear Algebra 3C Matrices#^ladr-3-41|Matrix multiplication]], [[Linear Algebra 3C Matrices#^ladr-3-43|Matrix of product of linear maps (LADR 3.43)]].

> [!theorem] 3.8 Algebraic properties of products of linear maps
> Whenever the products make sense:
> - **associativity** $(T_1T_2)T_3=T_1(T_2T_3)$;
> - **identity** $TI=IT=T$ for $T\in\Lin(V,W)$ (first $I$ on $V$, second on $W$);
> - **distributive properties** $(S_1+S_2)T=S_1T+S_2T$ and $S(T_1+T_2)=ST_1+ST_2$.

^ladr-3-8

> [!remark] Not commutative
> $ST\neq TS$ in general, even when both make sense. For example on $\Poly(\R)$, with $D$ = differentiation and $T$ = multiplication by $x$: $(DT-TD)p=p$.

> [!proof]+
> *(Filled in.)* Each identity is checked pointwise. Associativity: both sides send $u$ to $T_1(T_2(T_3u))$. Distributivity: $(S_1+S_2)(Tu)=S_1Tu+S_2Tu$ by definition of $S_1+S_2$; and $S(T_1u+T_2u)=ST_1u+ST_2u$ by additivity of $S$ (this is where linearity of $S$ is needed).

> [!remark]- Connections
> - Commutation relations such as $DT-TD=I$ are the prototype of $[\hat{p},\hat{x}]$ in quantum mechanics; in finite dimensions $ST-TS=I$ is impossible ([[Linear Algebra 8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-57|Identity operator is not the difference of ST and TS]]).
> - Commuting operators: [[Linear Algebra 5E Commuting Operators#^ladr-5-71|Commute]].

> [!example] 3.9 Two noncommuting linear maps from P(R) to P(R) (p. 56)
> With $D$ = differentiation and $T$ = multiplication by $x^2$ on $\Poly(\R)$:
> $$
> \big((TD)p\big)(x)=x^2p'(x),\qquad \big((DT)p\big)(x)=x^2p'(x)+2xp(x).
> $$
> So $TD\ne DT$: the order of operations matters ([[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-8|3.8]]). The same computation with multiplication by $x$ gives $DT-TD=I$, the finite-dimensionally impossible commutation relation ([[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-8|3.8]]).

^ladr-3-9

> [!theorem] 3.10 Linear maps take 0 to 0
> If $T$ is a linear map from $V$ to $W$, then $T(0)=0$.

^ladr-3-10

> [!proof]+
> $T(0)=T(0+0)=T(0)+T(0)$; add the additive inverse of $T(0)$ to both sides.

> [!remark]- Connections
> - Gives $0\in\nullsp T$ and $0\in\range T$: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-13|The null space is a subspace]], [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-18|The range is a subspace]]. Also $\{0\}\subseteq\nullsp T$ in [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]].
