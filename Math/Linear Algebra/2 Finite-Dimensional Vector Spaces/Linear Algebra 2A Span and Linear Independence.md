---
type: section
subject: "[[Linear Algebra]]"
chapter: 2
section: "2A"
tags: [linear-algebra]
---
← [[Linear Algebra 1C Subspaces]] · ↑ [[Linear Algebra — 2 Finite-Dimensional Vector Spaces]] · [[Linear Algebra 2B Bases]] →

> [!remark] 2.1 Notation: List of vectors (p. 28)

^ladr-2-1

> [!definition] 2.2 Linear combination
> A *linear combination* of a list $v_1,\dots,v_m$ in $V$ is a vector $a_1v_1+\dots+a_mv_m$ with $a_1,\dots,a_m\in\F$.

^ladr-2-2

> [!remark]- Connections
> - The set of all of them: [[Linear Algebra 2A Span and Linear Independence#^ladr-2-4|Span]].

> [!example] 2.3 Linear combinations in R³ (p. 28)
> - $(17,-4,2)=6(2,1,-3)+5(1,-2,4)$, so it is a linear combination of $(2,1,-3),(1,-2,4)$.
> - $(17,-4,5)$ is not. Solving $2a_1+a_2=17$, $a_1-2a_2=-4$ forces $a_1=6$, $a_2=5$, but then the third coordinate is $-3\cdot6+4\cdot5=2\ne5$.

^ladr-2-3

> [!definition] 2.4 Span
> The *span* of $v_1,\dots,v_m$ is the set of all their linear combinations:
> $$
> \Span(v_1,\dots,v_m)=\{a_1v_1+\dots+a_mv_m : a_1,\dots,a_m\in\F\}.
> $$
> The span of the empty list is $\{0\}$.

^ladr-2-4

> [!remark]- Connections
> - It is the smallest subspace containing the list: [[Linear Algebra 2A Span and Linear Independence#^ladr-2-6|Span is the smallest containing subspace]]. Spanning: [[Linear Algebra 2A Span and Linear Independence#^ladr-2-7|Spans]].

> [!example] 2.5 Span (p. 29)
> By [[Linear Algebra 2A Span and Linear Independence#^ladr-2-3|2.3]]: $(17,-4,2)\in\Span\big((2,1,-3),(1,-2,4)\big)$ but $(17,-4,5)\notin\Span\big((2,1,-3),(1,-2,4)\big)$. The span is a plane through $0$ in $\F^3$, and the second vector lies off it.
>
> Picture for $\F=\R$ (not to scale): the plane is gridded by multiples of $v_1=(2,1,-3)$ and $v_2=(1,-2,4)$. Going $6v_1$ and then $5v_2$ reaches $(17,-4,2)$; the point $(17,-4,5)$ sits $(0,0,3)$ above it, and $(0,0,3)$ is not in the span:
>
> ![[ladr-2.5-span-plane.svg|480]]

^ladr-2-5

> [!theorem] 2.6 Span is the smallest containing subspace
> The span of a list of vectors in $V$ is the smallest subspace of $V$ containing all vectors in the list.

^ladr-2-6

> [!proof]+
> $0=0v_1+\dots+0v_m$ is in the span; sums and scalar multiples of linear combinations are linear combinations:
> $$
> \textstyle\sum a_kv_k+\sum c_kv_k=\sum (a_k+c_k)v_k,\qquad \lambda\sum a_kv_k=\sum(\lambda a_k)v_k .
> $$
> So the span is a subspace by [[Linear Algebra 1C Subspaces#^ladr-1-34|Conditions for a subspace]]. It contains each $v_k$ (coefficient $1$ on $v_k$, $0$ elsewhere). Any subspace containing all $v_k$ contains all their linear combinations.

*Uses:* [[Linear Algebra 1C Subspaces#^ladr-1-34|1.34]]

> [!remark]- Connections
> - Parallel to [[Linear Algebra 1C Subspaces#^ladr-1-40|Sum of subspaces is the smallest containing subspace]]: $\Span(v_1,\dots,v_m)=\Span(v_1)+\dots+\Span(v_m)$.

> [!definition] 2.7 Spans
> If $\Span(v_1,\dots,v_m)=V$, we say $v_1,\dots,v_m$ *spans* $V$.

^ladr-2-7

> [!remark]- Connections
> - Defines [[Linear Algebra 2A Span and Linear Independence#^ladr-2-9|Finite-dimensional vector space]]; half of [[Linear Algebra 2B Bases#^ladr-2-26|Basis]].

> [!example] 2.8 A list that spans Fⁿ (p. 30)
> The list $e_1=(1,0,\dots,0),\ \dots,\ e_n=(0,\dots,0,1)$ spans $\F^n$, since
> $$
> (x_1,\dots,x_n)=x_1e_1+\dots+x_ne_n .
> $$
> So $\F^n$ is finite-dimensional ([[Linear Algebra 2A Span and Linear Independence#^ladr-2-9|2.9]]).

^ladr-2-8

> [!definition] 2.9 Finite-dimensional vector space
> A vector space is *finite-dimensional* if some list of vectors in it spans the space.

^ladr-2-9

> [!remark] Built-in finiteness
> Lists have finite length ([[Linear Algebra 1A Rⁿ and Cⁿ#^ladr-1-8|List, length]]), so this says finitely many vectors suffice. $\F^n$ is finite-dimensional.

> [!remark]- Connections
> - Opposite: [[Linear Algebra 2A Span and Linear Independence#^ladr-2-13|Infinite-dimensional vector space]]. Every such space has a basis: [[Linear Algebra 2B Bases#^ladr-2-31|Basis of finite-dimensional vector space]].

> [!definition] 2.10 Polynomial, P(F)
> A function $p:\F\to\F$ is a *polynomial with coefficients in $\F$* if there are $a_0,\dots,a_m\in\F$ with
> $$
> p(z)=a_0+a_1z+\dots+a_mz^m \quad\text{for all } z\in\F .
> $$
> $\mathcal{P}(\F)$ denotes the set of all such polynomials.

^ladr-2-10

> [!remark] Structure
> $\Poly(\F)$ is a subspace of $\F^\F$ (functions $\F\to\F$). The coefficients are determined by the function; this is proved later ([[Linear Algebra 4 Polynomials#^ladr-4-8|Degree m implies at most m zeros]]), and it is what makes [[Linear Algebra 2A Span and Linear Independence#^ladr-2-11|Degree of a polynomial, deg p]] well defined.

> [!remark]- Connections
> - Degree: [[Linear Algebra 2A Span and Linear Independence#^ladr-2-11|Degree of a polynomial, deg p]]. Infinite-dimensional: [[Linear Algebra 2A Span and Linear Independence#^ladr-2-13|Infinite-dimensional vector space]]. Chapter 4 theory: [[Linear Algebra 4 Polynomials#^ladr-4-6|Each zero of a polynomial corresponds to a degree-one factor]], [[Linear Algebra 4 Polynomials#^ladr-4-9|Division algorithm for polynomials]].

> [!definition] 2.11 Degree of a polynomial, deg p
> A polynomial $p$ has *degree $m$* if $p(z)=a_0+a_1z+\dots+a_mz^m$ for all $z$ with $a_m\neq 0$. The zero polynomial has degree $-\infty$. Notation: $\deg p$. With the convention $-\infty<m$, $\Poly_m(\F)$ denotes the polynomials of degree at most $m$ (so $0\in\Poly_m(\F)$).

^ladr-2-11

> [!remark]- Connections
> - $\Poly_m(\F)$ is spanned by $1,z,\dots,z^m$, a list that is linearly independent by [[Linear Algebra 4 Polynomials#^ladr-4-8|Degree m implies at most m zeros]]; so $\dim\Poly_m(\F)=m+1$ ([[Linear Algebra 2C Dimension#^ladr-2-35|Dimension, dim V]]).

> [!remark] 2.12 Notation: Pm(F) (p. 31)

^ladr-2-12

> [!definition] 2.13 Infinite-dimensional vector space
> A vector space is *infinite-dimensional* if it is not finite-dimensional.

^ladr-2-13

> [!remark] Standard example
> $\Poly(\F)$ is infinite-dimensional: every finite list of polynomials has some maximal degree $m$, and $z^{m+1}$ is not in its span.

> [!remark]- Connections
> - Physics: wave-function spaces are infinite-dimensional, so finite-dimensional results such as [[Existence of eigenvalues]] or [[Fundamental theorem of linear maps]] cannot be assumed there without extra structure.

> [!example] 2.14 P(F) is infinite-dimensional. (p. 31)
> $\Poly(\F)$ is infinite-dimensional ([[Linear Algebra 2A Span and Linear Independence#^ladr-2-13|2.13]]): given any finite list of polynomials, let $m$ be the largest degree occurring. Every polynomial in the span has degree $\le m$, so $z^{m+1}$ is not in the span. No finite list spans.

^ladr-2-14

> [!definition] 2.15 Linearly independent
> A list $v_1,\dots,v_m$ in $V$ is *linearly independent* if the only choice of $a_1,\dots,a_m\in\F$ with $a_1v_1+\dots+a_mv_m=0$ is $a_1=\dots=a_m=0$. The empty list is declared linearly independent.

^ladr-2-15

> [!remark] Equivalent form
> $v_1,\dots,v_m$ is linearly independent iff every vector of $\Span(v_1,\dots,v_m)$ has exactly one representation as a linear combination of the list (subtract two representations).

> [!remark]- Connections
> - Negation: [[Linear Algebra 2A Span and Linear Independence#^ladr-2-17|Linearly dependent]]. Same 'uniqueness at $0$' pattern as [[Condition for a direct sum]]. Half of [[Linear Algebra 2B Bases#^ladr-2-26|Basis]].

> [!example] 2.16 Linearly independent lists (p. 32)
> - (a) $(1,0,0,0),(0,1,0,0),(0,0,1,0)$ is linearly independent in $\F^4$: $a_1(1,0,0,0)+a_2(0,1,0,0)+a_3(0,0,1,0)=(a_1,a_2,a_3,0)$, which is $0$ only if all $a_k=0$.
> - (b) $1,z,\dots,z^m$ is linearly independent in $\Poly(\F)$: a polynomial that vanishes for every $z\in\F$ has all coefficients $0$ ([[Linear Algebra 4 Polynomials#^ladr-4-8|4.8]]).
> - (c) A list $v$ of length one is independent iff $v\ne0$.
> - (d) A list $v,w$ of length two is independent iff neither vector is a scalar multiple of the other.

^ladr-2-16

> [!definition] 2.17 Linearly dependent
> A list is *linearly dependent* if it is not linearly independent; i.e. there are $a_1,\dots,a_m\in\F$, not all $0$, with $a_1v_1+\dots+a_mv_m=0$.

^ladr-2-17

> [!remark]- Connections
> - What you can do with a dependent list: [[Linear dependence lemma]].

> [!example] 2.18 Linearly dependent lists (p. 33)
> - $(2,3,1),(1,-1,2),(7,3,8)$ is dependent: $2(2,3,1)+3(1,-1,2)-(7,3,8)=0$.
> - $(2,3,1),(1,-1,2),(7,3,c)$ is dependent iff $c=8$. The first two vectors are independent, and the only combination $a(2,3,1)+b(1,-1,2)$ with first two coordinates $(7,3)$ has $a=2$, $b=3$, giving third coordinate $8$.
> - If some vector of a list is a combination of the others, the list is dependent (move it to the other side with coefficient $-1$).
> - In particular, any list containing $0$ is dependent.

^ladr-2-18

> [!theorem] 2.19 Linear dependence lemma
> Suppose $v_1,\dots,v_m$ is linearly dependent in $V$. Then there is $k\in\{1,\dots,m\}$ with
> $$
> v_k\in\Span(v_1,\dots,v_{k-1}).
> $$
> Moreover, for any such $k$, removing $v_k$ from the list does not change its span.

^ladr-2-19

> [!remark] The case $k=1$
> $v_1\in\Span(\,)=\{0\}$ means $v_1=0$; the proof still works with empty sums.

> [!proof]+
> Pick $a_1,\dots,a_m$, not all $0$, with $a_1v_1+\dots+a_mv_m=0$, and let $k$ be the **largest** index with $a_k\neq0$. Then
> $$
> v_k=-\frac{a_1}{a_k}v_1-\dots-\frac{a_{k-1}}{a_k}v_{k-1}\in\Span(v_1,\dots,v_{k-1}).
> $$
> For the second part, let $k$ be any index with $v_k=b_1v_1+\dots+b_{k-1}v_{k-1}$. In any $u=c_1v_1+\dots+c_mv_m$, substitute this expression for $v_k$; the result is a linear combination of the list without $v_k$. So removing $v_k$ keeps the span.

> [!example] 2.21 Smallest k in linear dependence lemma (p. 34)
> Take $(1,2,3),(6,5,4),(15,16,17),(8,9,7)$ in $\R^3$. A list of length $4$ in $\R^3$ is dependent ([[Length of linearly independent list ≤ length of spanning list|2.22]]), so [[Linear dependence lemma|2.19]] applies. Which is the smallest $k$?
> - $k=1$ would need $(1,2,3)=0$: no.
> - $k=2$ would need $(6,5,4)=c(1,2,3)$: no.
> - $k=3$: solve $(15,16,17)=a(1,2,3)+b(6,5,4)$. The first two coordinates give $a=3$, $b=2$, and the third checks: $9+8=17$. So $k=3$.
>
> Removing the third vector keeps the span. The remaining list $(1,2,3),(6,5,4),(8,9,7)$ is independent (its determinant is $21\ne0$), so it is a basis of $\R^3$.

^ladr-2-21

> [!theorem] 2.22 Length of linearly independent list ≤ length of spanning list
> In a finite-dimensional vector space, the length of every linearly independent list is at most the length of every spanning list.

^ladr-2-22

> [!proof]+
> Let $u_1,\dots,u_m$ be linearly independent and $w_1,\dots,w_n$ span $V$. We show $m\le n$ by an exchange process of $m$ steps, each adding one $u$ and removing one $w$ while keeping a spanning list of length $n$.
>
> **Step 1.** Let $B=w_1,\dots,w_n$. Since $B$ spans, $u_1,w_1,\dots,w_n$ is linearly dependent. By [[Linear dependence lemma]] some vector of it lies in the span of the previous ones. It is not $u_1$, since $u_1\neq0$ (independence). So some $w$ can be removed, leaving a spanning list $B$ of length $n$ consisting of $u_1$ and $n-1$ of the $w$'s.
>
> **Step $k$** ($2\le k\le m$). $B$ spans, so adjoining $u_k$ right after $u_1,\dots,u_{k-1}$ gives a dependent list of length $n+1$. By [[Linear dependence lemma]] some vector lies in the span of its predecessors. It cannot be one of $u_1,\dots,u_k$, because they are linearly independent. So it is a $w$; remove it. The new $B$ has length $n$, consists of $u_1,\dots,u_k$ and some $w$'s, and still spans.
>
> After step $m$, $B$ contains all of $u_1,\dots,u_m$ and has length $n$, so $m\le n$. (At each step there was a $w$ left to remove, since otherwise the $u$'s would be dependent.)

*Uses:* [[Linear dependence lemma|2.19]]

%% ex:2.22-fig %%
> [!example] The exchange process, pictured
> With $m=3$ independent $u$'s and a spanning list of $n=4$ $w$'s. At each step the new $u_k$ (thick border) is inserted after the earlier $u$'s; the list is now dependent, and [[Linear dependence lemma|2.19]] removes a vector lying in the span of its predecessors (red, crossed). It is always a $w$, never a $u$, so the list keeps length $n$ and keeps spanning. When the $u$'s are used up, $m\le n$.
>
> ![[ladr-2.22-exchange.svg|460]]

> [!example] 2.23 No list of length 4 is linearly independent in R³ (p. 36)
> $(1,0,0),(0,1,0),(0,0,1)$ spans $\R^3$ and has length $3$, so by [[Length of linearly independent list ≤ length of spanning list|2.22]] no list of length $4$ in $\R^3$ is independent. For instance $(1,2,3),(4,5,8),(9,6,7),(-3,2,8)$ is dependent, with no computation needed.

^ladr-2-23

> [!example] 2.24 No list of length 3 spans R⁴ (p. 36)
> $(1,0,0,0),\dots,(0,0,0,1)$ is independent in $\R^4$ and has length $4$, so by [[Length of linearly independent list ≤ length of spanning list|2.22]] no list of length $3$ spans $\R^4$. For instance $(1,2,3,-5),(4,5,8,3),(9,6,7,-1)$ does not span $\R^4$.

^ladr-2-24

> [!theorem] 2.25 Finite-dimensional subspaces
> Every subspace of a finite-dimensional vector space is finite-dimensional.

^ladr-2-25

> [!proof]+
> Let $U$ be a subspace of finite-dimensional $V$.
>
> **Step 1.** If $U=\{0\}$, done. Otherwise choose $u_1\in U$, $u_1\neq0$.
>
> **Step $k$.** If $U=\Span(u_1,\dots,u_{k-1})$, done. Otherwise choose $u_k\in U\setminus\Span(u_1,\dots,u_{k-1})$.
>
> At every stage no vector of the list lies in the span of the previous ones, so the list is linearly independent by [[Linear dependence lemma]]. By [[Length of linearly independent list ≤ length of spanning list]] its length cannot exceed the length of a spanning list of $V$, so the process stops, and when it stops $U$ is spanned by a finite list.

*Uses:* [[Linear dependence lemma|2.19]], [[Length of linearly independent list ≤ length of spanning list|2.22]]

> [!remark]- Connections
> - Used implicitly in [[Fundamental theorem of linear maps]] (null space is finite-dimensional) and in [[Linear Algebra 2B Bases#^ladr-2-33|Every subspace of V is part of a direct sum equal to V]].
