---
type: section
subject: "[[Linear Algebra]]"
chapter: 3
section: "3F"
tags: [linear-algebra]
---
← [[Linear Algebra 3E Products and Quotients of Vector Spaces]] · ↑ [[Linear Algebra — 3 Linear Maps]] · [[Linear Algebra 4 Polynomials]] →

> [!definition] 3.108 Linear functional
> A *linear functional* on $V$ is a linear map $V\to\F$, i.e. an element of $\Lin(V,\F)$.

^ladr-3-108

> [!remark] Examples
> $\varphi(x_1,x_2,x_3)=4x_1-5x_2+2x_3$ on $\R^3$; $p\mapsto\int_0^1p$ on $\Poly(\R)$; evaluation $p\mapsto p(3)$.

> [!remark]- Connections
> - They form [[Linear Algebra 3F Duality#^ladr-3-110|Dual space, V′]]. On inner product spaces every functional is $v\mapsto\ip{v}{w}$: [[Riesz representation theorem]].
> - Physics: bras $\langle\psi|$ are linear functionals on kets.

> [!example] 3.109 Linear functionals (p. 105)
> Linear functionals:
> - $\varphi(x,y,z)=4x-5y+2z$ on $\R^3$;
> - $\varphi(x_1,\dots,x_n)=c_1x_1+\dots+c_nx_n$ on $\F^n$, for fixed $c_k$ (and every functional on $\F^n$ has this form);
> - $\varphi(p)=3p''(5)+7p(4)$ on $\Poly(\R)$;
> - $\varphi(p)=\int_0^1p$ on $\Poly(\R)$.

^ladr-3-109

> [!definition] 3.110 Dual space, V′
> The *dual space* of $V$ is $V'=\Lin(V,\F)$, the vector space of linear functionals on $V$.

^ladr-3-110

> [!remark]- Connections
> - Dimension: [[Linear Algebra 3F Duality#^ladr-3-111|Dim V′ = dim V]]. Basis: [[Linear Algebra 3F Duality#^ladr-3-112|Dual basis]], [[Linear Algebra 3F Duality#^ladr-3-116|Dual basis is a basis of the dual space]]. Maps induce dual maps: [[Linear Algebra 3F Duality#^ladr-3-118|Dual map, T′]].

> [!theorem] 3.111 Dim V′ = dim V
> If $V$ is finite-dimensional, then $V'$ is finite-dimensional and $\dim V'=\dim V$.

^ladr-3-111

> [!remark] Isomorphic but not canonically
> $V\cong V'$ by [[Dimension shows whether vector spaces are isomorphic]], but the isomorphism depends on a basis (via [[Linear Algebra 3F Duality#^ladr-3-112|Dual basis]]). An inner product gives a canonical one ([[Riesz representation theorem]]); in general only $V\cong V''$ is canonical.

> [!proof]+
> By [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-72|Dim L(V, W) = (dim V)(dim W)]], $\dim V'=\dim\Lin(V,\F)=(\dim V)(\dim\F)=\dim V$.

*Uses:* [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-72|3.72]]

> [!remark]- Connections
> - Used in [[Linear Algebra 3F Duality#^ladr-3-116|Dual basis is a basis of the dual space]], [[Linear Algebra 3F Duality#^ladr-3-125|Dimension of the annihilator]], [[Linear Algebra 3F Duality#^ladr-3-130|The range of T]].

> [!definition] 3.112 Dual basis
> If $v_1,\dots,v_n$ is a basis of $V$, its *dual basis* is the list $\varphi_1,\dots,\varphi_n$ in $V'$ where
> $$
> \varphi_j(v_k)=\begin{cases}1 & k=j,\\ 0 & k\neq j.\end{cases}
> $$

^ladr-3-112

> [!remark] Well defined
> Each $\varphi_j$ exists and is unique by [[Linear map lemma]].

> [!remark]- Connections
> - $\varphi_j$ reads off the $j$-th coordinate: [[Linear Algebra 3F Duality#^ladr-3-114|Dual basis gives coefficients for linear combination]]. It is a basis: [[Linear Algebra 3F Duality#^ladr-3-116|Dual basis is a basis of the dual space]].
> - Physics: $\langle e_j|$ against an orthonormal $|e_k\rangle$; index notation $e^j(e_k)=\delta^j_k$ for upper/lower indices.

> [!example] 3.113 The dual basis of the standard basis of Fⁿ (p. 106)
> On $\F^n$ let $\varphi_j(x_1,\dots,x_n)=x_j$ (select the $j$-th coordinate). Then $\varphi_j(e_k)=1$ if $k=j$ and $0$ otherwise, so $\varphi_1,\dots,\varphi_n$ is the dual basis of the standard basis ([[Linear Algebra 3F Duality#^ladr-3-112|3.112]]). In index notation: $e^j(e_k)=\delta^j_k$.

^ladr-3-113

> [!theorem] 3.114 Dual basis gives coefficients for linear combination
> If $v_1,\dots,v_n$ is a basis of $V$ with dual basis $\varphi_1,\dots,\varphi_n$, then for every $v\in V$
> $$
> v=\varphi_1(v)v_1+\dots+\varphi_n(v)v_n .
> $$

^ladr-3-114

> [!proof]+
> Write $v=c_1v_1+\dots+c_nv_n$. Applying $\varphi_j$ gives $\varphi_j(v)=c_j$.

> [!remark]- Connections
> - Orthonormal analogue: [[Linear Algebra 6B Orthonormal Bases#^ladr-6-30|Writing a vector as a linear combination of an orthonormal basis]] with $\varphi_j=\ip{\cdot}{e_j}$.

%% ex:3.114-fig %%
> [!example] The dual basis, pictured
> In $\R^2$ with basis $v_1,v_2$, the level lines of $\varphi_1$ (blue, dashed) are parallel to $v_2$, since $\varphi_1(v_2)=0$; those of $\varphi_2$ (red, dashed) are parallel to $v_1$. Reading off which level lines pass through $v$ gives its coordinates: here $\varphi_1(v)=2$, $\varphi_2(v)=1$, so $v=2v_1+v_2$.
>
> ![[ladr-3.114-dual-basis.svg|400]]

> [!theorem] 3.116 Dual basis is a basis of the dual space
> If $V$ is finite-dimensional, the dual basis of a basis of $V$ is a basis of $V'$.

^ladr-3-116

> [!proof]+
> If $a_1\varphi_1+\dots+a_n\varphi_n=0$, evaluating at $v_k$ gives $a_k=0$; so the list is linearly independent. Its length is $n=\dim V'$ ([[Linear Algebra 3F Duality#^ladr-3-111|Dim V′ = dim V]]), so it is a basis by [[Linear Algebra 2C Dimension#^ladr-2-38|Linearly independent list of the right length is a basis]].

*Uses:* [[Linear Algebra 3F Duality#^ladr-3-111|3.111]], [[Linear Algebra 2C Dimension#^ladr-2-38|2.38]]

> [!remark]- Connections
> - Matrix of a dual map in dual bases: [[Linear Algebra 3F Duality#^ladr-3-132|Matrix of T (LADR 3.132)]].

> [!definition] 3.118 Dual map, $T'$
> For $T\in\Lin(V,W)$, the *dual map* $T'\in\Lin(W',V')$ is
> $$
> T'(\varphi)=\varphi\circ T\qquad(\varphi\in W').
> $$

^ladr-3-118

> [!remark] Why it is linear, and the direction
> $\varphi\circ T$ is a linear functional on $V$, and $T'(\varphi+\psi)=(\varphi+\psi)\circ T=\varphi\circ T+\psi\circ T$, $T'(\lambda\varphi)=\lambda T'(\varphi)$. Note $T'$ goes *backwards*, from $W'$ to $V'$ (pullback).

> [!remark]- Connections
> - Algebra: [[Linear Algebra 3F Duality#^ladr-3-120|Algebraic properties of dual maps]]. Null space and range: [[Linear Algebra 3F Duality#^ladr-3-128|The null space of T]], [[Linear Algebra 3F Duality#^ladr-3-130|The range of T]]. Matrix is the transpose: [[Linear Algebra 3F Duality#^ladr-3-132|Matrix of T (LADR 3.132)]].
> - Not the adjoint $T^*$ of Chapter 7 ([[Linear Algebra 7A Self-Adjoint and Normal Operators#^ladr-7-1|Adjoint, T∗]]), although both are represented by (conjugate) transposes.

> [!example] 3.119 Dual map of the differentiation linear map (p. 108)
> $D:\Poly(\R)\to\Poly(\R)$, $Dp=p'$. The dual map $D'$ pulls a functional back by precomposing with $D$:
> - if $\varphi(p)=p(3)$, then $\big(D'(\varphi)\big)(p)=\varphi(p')=p'(3)$;
> - if $\varphi(p)=\int_0^1p$, then $\big(D'(\varphi)\big)(p)=\int_0^1p'=p(1)-p(0)$.
>
> The second item is the fundamental theorem of calculus in the language of duality. Directions: $T$ goes $V\to W$ but $T'$ goes $W'\to V'$:
>
> ![[ladr-3.119-dual-map.svg|420]]

^ladr-3-119

> [!theorem] 3.120 Algebraic properties of dual maps
> For $T\in\Lin(V,W)$:
> - (a) $(S+T)'=S'+T'$ for all $S\in\Lin(V,W)$;
> - (b) $(\lambda T)'=\lambda T'$ for all $\lambda\in\F$;
> - (c) $(ST)'=T'S'$ for all $S\in\Lin(W,U)$.

^ladr-3-120

> [!remark] Order reverses
> Like $(AB)^t=B^tA^t$, consistent with [[Linear Algebra 3F Duality#^ladr-3-132|Matrix of T (LADR 3.132)]]. Axler writes $V'$, $T'$ for duality and saves $T^*$ for the adjoint.

> [!proof]+
> *(Filled in: (a), (b).)* $(S+T)'(\varphi)=\varphi\circ(S+T)=\varphi\circ S+\varphi\circ T$ since $\varphi$ is additive; similarly $(\lambda T)'(\varphi)=\varphi\circ(\lambda T)=\lambda(\varphi\circ T)$ by homogeneity of $\varphi$.
>
> (c) For $\varphi\in U'$: $(ST)'(\varphi)=\varphi\circ(ST)=(\varphi\circ S)\circ T=T'(S'(\varphi))$.

> [!remark]- Connections
> - So $T\mapsto T'$ is a linear map $\Lin(V,W)\to\Lin(W',V')$ reversing composition.

> [!definition] 3.121 Annihilator, U0
> For a subset $U\subseteq V$, the *annihilator* of $U$ is
> $$
> U^0=\{\varphi\in V' : \varphi(u)=0\text{ for all }u\in U\}.
> $$

^ladr-3-121

> [!remark] Lives in the dual
> $U^0\subseteq V'$, not in $V$. It is the dual-space stand-in for an orthogonal complement ([[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-46|Orthogonal complement, U⟂]]).

> [!remark]- Connections
> - A subspace: [[Linear Algebra 3F Duality#^ladr-3-124|The annihilator is a subspace]]. Dimension: [[Linear Algebra 3F Duality#^ladr-3-125|Dimension of the annihilator]].

> [!example] 3.122 Element of an annihilator (p. 109)
> Let $U\subseteq\Poly(\R)$ be the polynomial multiples of $x^2$ and $\varphi(p)=p'(0)$. For $p=x^2q$, $p'(0)=\big(2xq+x^2q'\big)(0)=0$, so $\varphi\in U^0$.
>
> $U^0$ depends on the ambient space ($U^0\subseteq V'$), even though the notation hides it.

^ladr-3-122

> [!example] 3.123 The annihilator of a two-dimensional subspace of R⁵ (p. 109)
> In $\R^5$ with standard basis $e_1,\dots,e_5$ and dual basis $\varphi_1,\dots,\varphi_5$, let $U=\Span(e_1,e_2)$. Then
> $$
> U^0=\Span(\varphi_3,\varphi_4,\varphi_5).
> $$
> **$\supseteq$:** $\varphi_3,\varphi_4,\varphi_5$ kill $e_1,e_2$. **$\subseteq$:** write $\varphi=\sum_kc_k\varphi_k$ ([[Linear Algebra 3F Duality#^ladr-3-116|3.116]]); then $0=\varphi(e_1)=c_1$ and $0=\varphi(e_2)=c_2$.
>
> So $\dim U^0=3=5-2$, the pattern of [[Linear Algebra 3F Duality#^ladr-3-125|3.125]]; this example is the hands-on proof of that result.

^ladr-3-123

> [!theorem] 3.124 The annihilator is a subspace
> For any $U\subseteq V$, $U^0$ is a subspace of $V'$.

^ladr-3-124

> [!proof]+
> The zero functional kills everything, so $0\in U^0$. If $\varphi,\psi\in U^0$ and $u\in U$, then $(\varphi+\psi)(u)=0+0=0$ and $(\lambda\varphi)(u)=\lambda\cdot0=0$. Conclude by [[Linear Algebra 1C Subspaces#^ladr-1-34|Conditions for a subspace]].

*Uses:* [[Linear Algebra 1C Subspaces#^ladr-1-34|1.34]]

> [!remark]- Connections
> - Dimension: [[Linear Algebra 3F Duality#^ladr-3-125|Dimension of the annihilator]].

> [!theorem] 3.125 Dimension of the annihilator
> If $V$ is finite-dimensional and $U$ is a subspace, then $\dim U^0=\dim V-\dim U$.

^ladr-3-125

> [!remark] The hands-on proof
> Alternatively: with the extended basis and its dual basis $\varphi_1,\dots,\varphi_n$, the functionals dual to the $w$'s form a basis of $U^0$.

> [!proof]+
> Let $i\in\Lin(U,V)$ be the inclusion; then $i'\in\Lin(V',U')$ and $i'(\varphi)=\varphi|_U$. So $\nullsp i'=U^0$. By [[Fundamental theorem of linear maps]] and [[Linear Algebra 3F Duality#^ladr-3-111|Dim V′ = dim V]],
> $$
> \dim\range i'+\dim U^0=\dim V'=\dim V .
> $$
> *(Filled in: Axler cites an exercise.)* $i'$ is surjective: given $\varphi\in U'$, extend a basis $u_1,\dots,u_m$ of $U$ to a basis $u_1,\dots,u_m,w_1,\dots,w_k$ of $V$ ([[Every linearly independent list extends to a basis]]) and let $\psi\in V'$ agree with $\varphi$ on the $u$'s and vanish on the $w$'s ([[Linear map lemma]]); then $i'(\psi)=\varphi$. Hence $\dim\range i'=\dim U'=\dim U$, giving $\dim U+\dim U^0=\dim V$.

*Uses:* [[Fundamental theorem of linear maps|3.21]], [[Linear Algebra 3F Duality#^ladr-3-111|3.111]], [[Every linearly independent list extends to a basis|2.32]], [[Linear map lemma|3.4]]

> [!remark]- Connections
> - Same count as [[Linear Algebra 3E Products and Quotients of Vector Spaces#^ladr-3-105|Dimension of quotient space]]; indeed $U^0\cong(V/U)'$.
> - Inner-product analogue: [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-51|Dimension of orthogonal complement]].

> [!theorem] 3.127 Condition for the annihilator to equal {0} or the whole space
> If $V$ is finite-dimensional and $U$ is a subspace, then
> - (a) $U^0=\{0\}\iff U=V$;
> - (b) $U^0=V'\iff U=\{0\}$.

^ladr-3-127

> [!remark] How to use it
> (a) shows a subspace is everything by showing no nonzero functional kills it; (b) shows it is trivial by showing every functional kills it.

> [!proof]+
> (a) $U^0=\{0\}\iff\dim U^0=0\iff\dim U=\dim V\iff U=V$, by [[Linear Algebra 3F Duality#^ladr-3-125|Dimension of the annihilator]] and [[Linear Algebra 2C Dimension#^ladr-2-39|Subspace of full dimension equals the whole space]].
>
> (b) $U^0=V'\iff\dim U^0=\dim V'$ (one direction by [[Linear Algebra 2C Dimension#^ladr-2-39|Subspace of full dimension equals the whole space]]) $\iff\dim U^0=\dim V$ ([[Linear Algebra 3F Duality#^ladr-3-111|Dim V′ = dim V]]) $\iff\dim U=0$ ([[Linear Algebra 3F Duality#^ladr-3-125|Dimension of the annihilator]]) $\iff U=\{0\}$.

*Uses:* [[Linear Algebra 3F Duality#^ladr-3-125|3.125]], [[Linear Algebra 2C Dimension#^ladr-2-39|2.39]], [[Linear Algebra 3F Duality#^ladr-3-111|3.111]]

> [!remark]- Connections
> - Gives the surjective/injective dualities in [[Linear Algebra 3F Duality#^ladr-3-128|The null space of T]] and [[Linear Algebra 3F Duality#^ladr-3-130|The range of T]].

> [!theorem] 3.128 The null space of $T'$
> Let $V,W$ be finite-dimensional and $T\in\Lin(V,W)$. Then
> - (a) $\nullsp T'=(\range T)^0$;
> - (b) $\dim\nullsp T'=\dim\nullsp T+\dim W-\dim V$.
>
> **Corollary (Axler 3.129).** $T$ is surjective $\iff T'$ is injective.

^ladr-3-128

> [!proof]+
> (a) $\varphi\in\nullsp T'\iff\varphi\circ T=0\iff\varphi(Tv)=0$ for all $v\iff\varphi\in(\range T)^0$. (This part needs no finite-dimensionality.)
>
> (b) By (a), [[Linear Algebra 3F Duality#^ladr-3-125|Dimension of the annihilator]] and [[Fundamental theorem of linear maps]]:
> $$
> \dim\nullsp T'=\dim W-\dim\range T=\dim W-(\dim V-\dim\nullsp T).
> $$
>
> *Corollary.* $T$ surjective $\iff\range T=W\iff(\range T)^0=\{0\}$ ([[Linear Algebra 3F Duality#^ladr-3-127|Condition for the annihilator to equal {0} or the whole space]](a)) $\iff\nullsp T'=\{0\}$ (by (a)) $\iff T'$ injective.

*Uses:* [[Linear Algebra 3F Duality#^ladr-3-125|3.125]], [[Fundamental theorem of linear maps|3.21]], [[Linear Algebra 3F Duality#^ladr-3-127|3.127]]

> [!remark]- Connections
> - Companion: [[Linear Algebra 3F Duality#^ladr-3-130|The range of T]]. Useful when injectivity of $T'$ is easier to check than surjectivity of $T$.

> [!theorem] 3.130 The range of $T'$
> Let $V,W$ be finite-dimensional and $T\in\Lin(V,W)$. Then
> - (a) $\dim\range T'=\dim\range T$;
> - (b) $\range T'=(\nullsp T)^0$.
>
> **Corollary (Axler 3.131).** $T$ is injective $\iff T'$ is surjective.

^ladr-3-130

> [!proof]+
> (a) By [[Fundamental theorem of linear maps]], [[Linear Algebra 3F Duality#^ladr-3-111|Dim V′ = dim V]], [[Linear Algebra 3F Duality#^ladr-3-128|The null space of T]](a) and [[Linear Algebra 3F Duality#^ladr-3-125|Dimension of the annihilator]]:
> $$
> \dim\range T'=\dim W'-\dim\nullsp T'=\dim W-\dim(\range T)^0=\dim\range T .
> $$
> (b) If $\varphi=T'(\psi)$ and $v\in\nullsp T$, then $\varphi(v)=\psi(Tv)=\psi(0)=0$; so $\range T'\subseteq(\nullsp T)^0$. Both have the same dimension: $\dim\range T'=\dim\range T=\dim V-\dim\nullsp T=\dim(\nullsp T)^0$ (by (a), [[Fundamental theorem of linear maps]], [[Linear Algebra 3F Duality#^ladr-3-125|Dimension of the annihilator]]). Hence equality ([[Linear Algebra 2C Dimension#^ladr-2-39|Subspace of full dimension equals the whole space]]).
>
> *Corollary.* $T$ injective $\iff\nullsp T=\{0\}\iff(\nullsp T)^0=V'$ ([[Linear Algebra 3F Duality#^ladr-3-127|Condition for the annihilator to equal {0} or the whole space]](b)) $\iff\range T'=V'$ (by (b)).

*Uses:* [[Fundamental theorem of linear maps|3.21]], [[Linear Algebra 3F Duality#^ladr-3-111|3.111]], [[Linear Algebra 3F Duality#^ladr-3-128|3.128]], [[Linear Algebra 3F Duality#^ladr-3-125|3.125]], [[Linear Algebra 2C Dimension#^ladr-2-39|2.39]], [[Linear Algebra 3F Duality#^ladr-3-127|3.127]]

> [!remark]- Connections
> - (a) is the abstract form of row rank $=$ column rank: [[Linear Algebra 3F Duality#^ladr-3-133|Column rank equals row rank (LADR 3.133)]].

%% ex:3.130-fig %%
> [!example] Null spaces and ranges under duality
> Passing to the dual map swaps the roles of null space and range: the annihilator of $\nullsp T$ is $\range T'$ ([[Linear Algebra 3F Duality#^ladr-3-130|3.130]](b)), and the annihilator of $\range T$ is $\nullsp T'$ ([[Linear Algebra 3F Duality#^ladr-3-128|3.128]](a)). That is why injectivity of $T$ matches surjectivity of $T'$, and surjectivity of $T$ matches injectivity of $T'$.
>
> ![[ladr-3.130-four-subspaces.svg|440]]

> [!theorem] 3.132 Matrix of $T'$ is the transpose of the matrix of $T$
> Let $V,W$ be finite-dimensional, $T\in\Lin(V,W)$, with bases $v_1,\dots,v_n$ of $V$, $w_1,\dots,w_m$ of $W$ and the dual bases $\varphi_1,\dots,\varphi_n$, $\psi_1,\dots,\psi_m$. Then
> $$
> \mathcal{M}(T')=\big(\mathcal{M}(T)\big)^t .
> $$

^ladr-3-132

> [!proof]+
> Let $A=\mathcal{M}(T)$, $C=\mathcal{M}(T')$. By definition $T'(\psi_j)=\sum_rC_{r,j}\varphi_r$; evaluating at $v_k$ gives $(\psi_j\circ T)(v_k)=C_{k,j}$. On the other hand
> $$
> (\psi_j\circ T)(v_k)=\psi_j\Big(\sum_rA_{r,k}w_r\Big)=A_{j,k}.
> $$
> So $C_{k,j}=A_{j,k}$, i.e. $C=A^t$.

> [!remark]- Connections
> - Explains [[Linear Algebra 3F Duality#^ladr-3-120|Algebraic properties of dual maps]](c) as $(AB)^t=B^tA^t$. Used in [[Linear Algebra 3F Duality#^ladr-3-133|Column rank equals row rank (LADR 3.133)]].
> - With respect to orthonormal bases the adjoint has the conjugate transpose: [[Linear Algebra 7A Self-Adjoint and Normal Operators#^ladr-7-9|Matrix of T (LADR 7.9)]].

> [!theorem] 3.133 Column rank equals row rank
> For every $A\in\F^{m,n}$, the column rank of $A$ equals the row rank of $A$.

^ladr-3-133

> [!proof]+
> Let $T:\F^{n,1}\to\F^{m,1}$, $Tx=Ax$, so $\mathcal{M}(T)=A$ in the standard bases. Then
> $$
> \text{col rank }A=\dim\range T=\dim\range T'=\text{col rank }\mathcal{M}(T')=\text{col rank }A^t=\text{row rank }A,
> $$
> using [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-78|Dimension of range T equals column rank of M(T)]], [[Linear Algebra 3F Duality#^ladr-3-130|The range of T]](a), [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-78|Dimension of range T equals column rank of M(T)]], [[Linear Algebra 3F Duality#^ladr-3-132|Matrix of T (LADR 3.132)]].

*Uses:* [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-78|3.78]], [[Linear Algebra 3F Duality#^ladr-3-130|3.130]], [[Linear Algebra 3F Duality#^ladr-3-132|3.132]]

> [!remark]- Connections
> - First proof by column–row factorization: [[Linear Algebra 3C Matrices#^ladr-3-57|Column rank equals row rank (LADR 3.57)]]. A third proof via adjoints appears in Chapter 7.
