---
type: section
subject: "[[Linear Algebra]]"
chapter: 3
section: 12
aliases: ["LADR 3F", "3F Duality"]
tags: [linear-algebra]
---
← [[§11 Products and Quotients of Vector Spaces]] · ↑ [[· 3 Linear Maps]] · [[§13 Polynomials]] →

> [!definition] Definition 3.108: Linear functional
> A *linear functional* on $V$ is a linear map $V\to\F$, i.e. an element of $\Lin(V,\F)$.

^ladr-3-108

> [!remark] Remark: Examples
> $\varphi(x_1,x_2,x_3)=4x_1-5x_2+2x_3$ on $\R^3$; $p\mapsto\int_0^1p$ on $\Poly(\R)$; evaluation $p\mapsto p(3)$.

> [!remark]- Connections
> - They form [[§12 Duality#^ladr-3-110|Dual space, V′]]. On inner product spaces every functional is $v\mapsto\ip{v}{w}$: [[Riesz representation theorem]].
> - Physics: bras $\langle\psi|$ are linear functionals on kets.
> - 556 starts from the same definition ([[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-5|556 Def. §2.5]]); in infinite dimensions functionals need not be continuous, so it singles out the bounded ones ([[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^def-19-1|556 Def. §19.1]]) and produces them with Hahn–Banach ([[§3 Statement and Motivation#^thm-3-2|556 Thm. §3.2]]).
> - Used in Relativity: covariant components $a_\mu$ are the components of a linear functional, and the metric lowers indices — [[§B1.1 The Metric and Index Notation#^rem-b1-1-1|REL Remark: Why two index positions]]; covectors and tensors of type (m, n) — [[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]].

> [!example] Example 3.109: Linear functionals (p. 105)
> Linear functionals:
> - $\varphi(x,y,z)=4x-5y+2z$ on $\R^3$;
> - $\varphi(x_1,\dots,x_n)=c_1x_1+\dots+c_nx_n$ on $\F^n$, for fixed $c_k$ (and every functional on $\F^n$ has this form);
> - $\varphi(p)=3p''(5)+7p(4)$ on $\Poly(\R)$;
> - $\varphi(p)=\int_0^1p$ on $\Poly(\R)$.

^ladr-3-109

> [!definition] Definition 3.110: Dual space, V′
> The *dual space* of $V$ is $V'=\Lin(V,\F)$, the vector space of linear functionals on $V$.

^ladr-3-110

> [!remark]- Connections
> - Dimension: [[§12 Duality#^ladr-3-111|Dim V′ = dim V]]. Basis: [[§12 Duality#^ladr-3-112|Dual basis]], [[§12 Duality#^ladr-3-116|Dual basis is a basis of the dual space]]. Maps induce dual maps: [[§12 Duality#^ladr-3-118|Dual map, T′]].
> - For a normed space 556 keeps only the bounded functionals and adds the dual norm: [[§24 Bras, Kets, and the Riesz Map#^def-24-1|556 Def. §24.1]].
> - Same definition in 591 ([[§20 Linear Algebra Toolkit#^def-20-1|591 Def. §20.1]]); the dual of a tangent space is the cotangent space, [[§30 Tangent Spaces III꞉ The Cotangent Space#^def-30-1|591 Def. §30.1]].

> [!theorem] Theorem 3.111: Dim V′ = dim V
> If $V$ is finite-dimensional, then $V'$ is finite-dimensional and $\dim V'=\dim V$.

^ladr-3-111

> [!remark] Remark: Isomorphic but not canonically
> $V\cong V'$ by [[Dimension shows whether vector spaces are isomorphic]], but the isomorphism depends on a basis (via [[§12 Duality#^ladr-3-112|Dual basis]]). An inner product gives a canonical one ([[Riesz representation theorem]]); in general only $V\cong V''$ is canonical.

> [!proof]+ Proof
> By [[§10 Invertibility and Isomorphisms#^ladr-3-72|Dim L(V, W) = (dim V)(dim W)]], $\dim V'=\dim\Lin(V,\F)=(\dim V)(\dim\F)=\dim V$.

*Uses:* [[§10 Invertibility and Isomorphisms#^ladr-3-72|3.72]]

> [!remark]- Connections
> - Used in [[§12 Duality#^ladr-3-116|Dual basis is a basis of the dual space]], [[§12 Duality#^ladr-3-125|Dimension of the annihilator]], [[§12 Duality#^ladr-3-130|The range of T]].
> - The isomorphism V ≅ V′ needs a basis, but V → V″ is canonical: [[§20 Linear Algebra Toolkit#^prop-20-3|591 Prop. §20.3]]; more generally a non-degenerate pairing identifies one space with the dual of the other, [[§20 Linear Algebra Toolkit#^thm-20-5|591 Thm. §20.5]].

> [!definition] Definition 3.112: Dual basis
> If $v_1,\dots,v_n$ is a basis of $V$, its *dual basis* is the list $\varphi_1,\dots,\varphi_n$ in $V'$ where
> $$
> \varphi_j(v_k)=\begin{cases}1 & k=j,\\ 0 & k\neq j.\end{cases}
> $$

^ladr-3-112

> [!remark] Remark: Well defined
> Each $\varphi_j$ exists and is unique by [[Linear map lemma]].

> [!remark]- Connections
> - $\varphi_j$ reads off the $j$-th coordinate: [[§12 Duality#^ladr-3-114|Dual basis gives coefficients for linear combination]]. It is a basis: [[§12 Duality#^ladr-3-116|Dual basis is a basis of the dual space]].
> - Physics: $\langle e_j|$ against an orthonormal $|e_k\rangle$; index notation $e^j(e_k)=\delta^j_k$ for upper/lower indices.
> - Same in 591: [[§20 Linear Algebra Toolkit#^def-20-1|591 Def. §20.1]], a basis of the dual by [[§20 Linear Algebra Toolkit#^prop-20-2|591 Prop. §20.2]]; the differentials of the coordinate functions form the dual basis of the coordinate derivations, [[§30 Tangent Spaces III꞉ The Cotangent Space#^lem-30-2|591 Lemma §30.2]].

> [!example] Example 3.113: The dual basis of the standard basis of Fⁿ (p. 106)
> On $\F^n$ let $\varphi_j(x_1,\dots,x_n)=x_j$ (select the $j$-th coordinate). Then $\varphi_j(e_k)=1$ if $k=j$ and $0$ otherwise, so $\varphi_1,\dots,\varphi_n$ is the dual basis of the standard basis ([[§12 Duality#^ladr-3-112|3.112]]). In index notation: $e^j(e_k)=\delta^j_k$.

^ladr-3-113

> [!theorem] Theorem 3.114: Dual basis gives coefficients for linear combination
> If $v_1,\dots,v_n$ is a basis of $V$ with dual basis $\varphi_1,\dots,\varphi_n$, then for every $v\in V$
> $$
> v=\varphi_1(v)v_1+\dots+\varphi_n(v)v_n .
> $$

^ladr-3-114

> [!proof]+ Proof
> Write $v=c_1v_1+\dots+c_nv_n$. Applying $\varphi_j$ gives $\varphi_j(v)=c_j$.

> [!remark]- Connections
> - Orthonormal analogue: [[§20 Orthonormal Bases#^ladr-6-30|Writing a vector as a linear combination of an orthonormal basis]] with $\varphi_j=\ip{\cdot}{e_j}$.

%% ex:3.114-fig %%
> [!example] Example: The dual basis, pictured
> In $\R^2$ with basis $v_1,v_2$, the level lines of $\varphi_1$ (blue, dashed) are parallel to $v_2$, since $\varphi_1(v_2)=0$; those of $\varphi_2$ (red, dashed) are parallel to $v_1$. Reading off which level lines pass through $v$ gives its coordinates: here $\varphi_1(v)=2$, $\varphi_2(v)=1$, so $v=2v_1+v_2$.
>
> ![[ladr-3.114-dual-basis.svg|400]]

> [!theorem] Theorem 3.116: Dual basis is a basis of the dual space
> If $V$ is finite-dimensional, the dual basis of a basis of $V$ is a basis of $V'$.

^ladr-3-116

> [!proof]+ Proof
> If $a_1\varphi_1+\dots+a_n\varphi_n=0$, evaluating at $v_k$ gives $a_k=0$; so the list is linearly independent. Its length is $n=\dim V'$ ([[§12 Duality#^ladr-3-111|Dim V′ = dim V]]), so it is a basis by [[§6 Dimension#^ladr-2-38|Linearly independent list of the right length is a basis]].

*Uses:* [[§12 Duality#^ladr-3-111|3.111]], [[§6 Dimension#^ladr-2-38|2.38]]

> [!remark]- Connections
> - Matrix of a dual map in dual bases: [[§12 Duality#^ladr-3-132|Matrix of T (LADR 3.132)]].

> [!definition] Definition 3.118: Dual map, $T'$
> For $T\in\Lin(V,W)$, the *dual map* $T'\in\Lin(W',V')$ is
> $$
> T'(\varphi)=\varphi\circ T\qquad(\varphi\in W').
> $$

^ladr-3-118

> [!remark] Remark: Why it is linear, and the direction
> $\varphi\circ T$ is a linear functional on $V$, and $T'(\varphi+\psi)=(\varphi+\psi)\circ T=\varphi\circ T+\psi\circ T$, $T'(\lambda\varphi)=\lambda T'(\varphi)$. Note $T'$ goes *backwards*, from $W'$ to $V'$ (pullback).

> [!remark]- Connections
> - Algebra: [[§12 Duality#^ladr-3-120|Algebraic properties of dual maps]]. Null space and range: [[§12 Duality#^ladr-3-128|The null space of T]], [[§12 Duality#^ladr-3-130|The range of T]]. Matrix is the transpose: [[§12 Duality#^ladr-3-132|Matrix of T (LADR 3.132)]].
> - Not the adjoint $T^*$ of Chapter 7 ([[§22 Self-Adjoint and Normal Operators#^ladr-7-1|Adjoint, T∗]]), although both are represented by (conjugate) transposes.
> - Same definition in 591, written with a star and called the transpose: [[§20 Linear Algebra Toolkit#^def-20-2|591 Def. §20.2]], with its properties in [[§20 Linear Algebra Toolkit#^prop-20-4|591 Prop. §20.4]].

> [!example] Example 3.119: Dual map of the differentiation linear map (p. 108)
> $D:\Poly(\R)\to\Poly(\R)$, $Dp=p'$. The dual map $D'$ pulls a functional back by precomposing with $D$:
> - if $\varphi(p)=p(3)$, then $\big(D'(\varphi)\big)(p)=\varphi(p')=p'(3)$;
> - if $\varphi(p)=\int_0^1p$, then $\big(D'(\varphi)\big)(p)=\int_0^1p'=p(1)-p(0)$.
>
> The second item is the fundamental theorem of calculus in the language of duality. Directions: $T$ goes $V\to W$ but $T'$ goes $W'\to V'$:
>
> ![[ladr-3.119-dual-map.svg|420]]

^ladr-3-119

> [!theorem] Theorem 3.120: Algebraic properties of dual maps
> For $T\in\Lin(V,W)$:
> - (a) $(S+T)'=S'+T'$ for all $S\in\Lin(V,W)$;
> - (b) $(\lambda T)'=\lambda T'$ for all $\lambda\in\F$;
> - (c) $(ST)'=T'S'$ for all $S\in\Lin(W,U)$.

^ladr-3-120

> [!remark] Remark: Order reverses
> Like $(AB)^t=B^tA^t$, consistent with [[§12 Duality#^ladr-3-132|Matrix of T (LADR 3.132)]]. Axler writes $V'$, $T'$ for duality and saves $T^*$ for the adjoint.

> [!proof]+ Proof
> *(Filled in: (a), (b).)* $(S+T)'(\varphi)=\varphi\circ(S+T)=\varphi\circ S+\varphi\circ T$ since $\varphi$ is additive; similarly $(\lambda T)'(\varphi)=\varphi\circ(\lambda T)=\lambda(\varphi\circ T)$ by homogeneity of $\varphi$.
>
> (c) For $\varphi\in U'$: $(ST)'(\varphi)=\varphi\circ(ST)=(\varphi\circ S)\circ T=T'(S'(\varphi))$.

> [!remark]- Connections
> - So $T\mapsto T'$ is a linear map $\Lin(V,W)\to\Lin(W',V')$ reversing composition.

> [!definition] Definition 3.121: Annihilator, U0
> For a subset $U\subseteq V$, the *annihilator* of $U$ is
> $$
> U^0=\{\varphi\in V' : \varphi(u)=0\text{ for all }u\in U\}.
> $$

^ladr-3-121

> [!remark] Remark: Lives in the dual
> $U^0\subseteq V'$, not in $V$. It is the dual-space stand-in for an orthogonal complement ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-46|Orthogonal complement, U⟂]]).

> [!remark]- Connections
> - A subspace: [[§12 Duality#^ladr-3-124|The annihilator is a subspace]]. Dimension: [[§12 Duality#^ladr-3-125|Dimension of the annihilator]].
> - The conormal space of a submanifold is the annihilator of its tangent space: [[§33 Submanifolds#^def-33-2|591 Def. §33.2]], of dimension the codimension by [[§33 Submanifolds#^prop-33-5|591 Prop. §33.5]].

> [!example] Example 3.122: Element of an annihilator (p. 109)
> Let $U\subseteq\Poly(\R)$ be the polynomial multiples of $x^2$ and $\varphi(p)=p'(0)$. For $p=x^2q$, $p'(0)=\big(2xq+x^2q'\big)(0)=0$, so $\varphi\in U^0$.
>
> $U^0$ depends on the ambient space ($U^0\subseteq V'$), even though the notation hides it.

^ladr-3-122

> [!example] Example 3.123: The annihilator of a two-dimensional subspace of R⁵ (p. 109)
> In $\R^5$ with standard basis $e_1,\dots,e_5$ and dual basis $\varphi_1,\dots,\varphi_5$, let $U=\Span(e_1,e_2)$. Then
> $$
> U^0=\Span(\varphi_3,\varphi_4,\varphi_5).
> $$
> **$\supseteq$:** $\varphi_3,\varphi_4,\varphi_5$ kill $e_1,e_2$. **$\subseteq$:** write $\varphi=\sum_kc_k\varphi_k$ ([[§12 Duality#^ladr-3-116|3.116]]); then $0=\varphi(e_1)=c_1$ and $0=\varphi(e_2)=c_2$.
>
> So $\dim U^0=3=5-2$, the pattern of [[§12 Duality#^ladr-3-125|3.125]]; this example is the hands-on proof of that result.

^ladr-3-123

> [!theorem] Theorem 3.124: The annihilator is a subspace
> For any $U\subseteq V$, $U^0$ is a subspace of $V'$.

^ladr-3-124

> [!proof]+ Proof
> The zero functional kills everything, so $0\in U^0$. If $\varphi,\psi\in U^0$ and $u\in U$, then $(\varphi+\psi)(u)=0+0=0$ and $(\lambda\varphi)(u)=\lambda\cdot0=0$. Conclude by [[§3 Subspaces#^ladr-1-34|Conditions for a subspace]].

*Uses:* [[§3 Subspaces#^ladr-1-34|1.34]]

> [!remark]- Connections
> - Dimension: [[§12 Duality#^ladr-3-125|Dimension of the annihilator]].

> [!theorem] Theorem 3.125: Dimension of the annihilator
> If $V$ is finite-dimensional and $U$ is a subspace, then $\dim U^0=\dim V-\dim U$.

^ladr-3-125

> [!remark] Remark: The hands-on proof
> Alternatively: with the extended basis and its dual basis $\varphi_1,\dots,\varphi_n$, the functionals dual to the $w$'s form a basis of $U^0$.

> [!proof]+ Proof
> Let $i\in\Lin(U,V)$ be the inclusion; then $i'\in\Lin(V',U')$ and $i'(\varphi)=\varphi|_U$. So $\nullsp i'=U^0$. By [[Fundamental theorem of linear maps]] and [[§12 Duality#^ladr-3-111|Dim V′ = dim V]],
> $$
> \dim\range i'+\dim U^0=\dim V'=\dim V .
> $$
> *(Filled in: Axler cites an exercise.)* $i'$ is surjective: given $\varphi\in U'$, extend a basis $u_1,\dots,u_m$ of $U$ to a basis $u_1,\dots,u_m,w_1,\dots,w_k$ of $V$ ([[Every linearly independent list extends to a basis]]) and let $\psi\in V'$ agree with $\varphi$ on the $u$'s and vanish on the $w$'s ([[Linear map lemma]]); then $i'(\psi)=\varphi$. Hence $\dim\range i'=\dim U'=\dim U$, giving $\dim U+\dim U^0=\dim V$.

*Uses:* [[Fundamental theorem of linear maps|3.21]], [[§12 Duality#^ladr-3-111|3.111]], [[Every linearly independent list extends to a basis|2.32]], [[Linear map lemma|3.4]]

> [!remark]- Connections
> - Same count as [[§11 Products and Quotients of Vector Spaces#^ladr-3-105|Dimension of quotient space]]; indeed $U^0\cong(V/U)'$.
> - Inner-product analogue: [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-51|Dimension of orthogonal complement]].

> [!theorem] Theorem 3.127: Condition for the annihilator to equal {0} or the whole space
> If $V$ is finite-dimensional and $U$ is a subspace, then
> - (a) $U^0=\{0\}\iff U=V$;
> - (b) $U^0=V'\iff U=\{0\}$.

^ladr-3-127

> [!remark] Remark: How to use it
> (a) shows a subspace is everything by showing no nonzero functional kills it; (b) shows it is trivial by showing every functional kills it.

> [!proof]+ Proof
> (a) $U^0=\{0\}\iff\dim U^0=0\iff\dim U=\dim V\iff U=V$, by [[§12 Duality#^ladr-3-125|Dimension of the annihilator]] and [[§6 Dimension#^ladr-2-39|Subspace of full dimension equals the whole space]].
>
> (b) $U^0=V'\iff\dim U^0=\dim V'$ (one direction by [[§6 Dimension#^ladr-2-39|Subspace of full dimension equals the whole space]]) $\iff\dim U^0=\dim V$ ([[§12 Duality#^ladr-3-111|Dim V′ = dim V]]) $\iff\dim U=0$ ([[§12 Duality#^ladr-3-125|Dimension of the annihilator]]) $\iff U=\{0\}$.

*Uses:* [[§12 Duality#^ladr-3-125|3.125]], [[§6 Dimension#^ladr-2-39|2.39]], [[§12 Duality#^ladr-3-111|3.111]]

> [!remark]- Connections
> - Gives the surjective/injective dualities in [[§12 Duality#^ladr-3-128|The null space of T]] and [[§12 Duality#^ladr-3-130|The range of T]].

> [!theorem] Theorem 3.128: The null space of $T'$
> Let $V,W$ be finite-dimensional and $T\in\Lin(V,W)$. Then
> - (a) $\nullsp T'=(\range T)^0$;
> - (b) $\dim\nullsp T'=\dim\nullsp T+\dim W-\dim V$.
>
> **Corollary (Axler 3.129).** $T$ is surjective $\iff T'$ is injective.

^ladr-3-128

> [!proof]+ Proof
> (a) $\varphi\in\nullsp T'\iff\varphi\circ T=0\iff\varphi(Tv)=0$ for all $v\iff\varphi\in(\range T)^0$. (This part needs no finite-dimensionality.)
>
> (b) By (a), [[§12 Duality#^ladr-3-125|Dimension of the annihilator]] and [[Fundamental theorem of linear maps]]:
> $$
> \dim\nullsp T'=\dim W-\dim\range T=\dim W-(\dim V-\dim\nullsp T).
> $$
>
> *Corollary.* $T$ surjective $\iff\range T=W\iff(\range T)^0=\{0\}$ ([[§12 Duality#^ladr-3-127|Condition for the annihilator to equal {0} or the whole space]](a)) $\iff\nullsp T'=\{0\}$ (by (a)) $\iff T'$ injective.

*Uses:* [[§12 Duality#^ladr-3-125|3.125]], [[Fundamental theorem of linear maps|3.21]], [[§12 Duality#^ladr-3-127|3.127]]

> [!remark]- Connections
> - Companion: [[§12 Duality#^ladr-3-130|The range of T]]. Useful when injectivity of $T'$ is easier to check than surjectivity of $T$.

> [!theorem] Theorem 3.130: The range of $T'$
> Let $V,W$ be finite-dimensional and $T\in\Lin(V,W)$. Then
> - (a) $\dim\range T'=\dim\range T$;
> - (b) $\range T'=(\nullsp T)^0$.
>
> **Corollary (Axler 3.131).** $T$ is injective $\iff T'$ is surjective.

^ladr-3-130

> [!proof]+ Proof
> (a) By [[Fundamental theorem of linear maps]], [[§12 Duality#^ladr-3-111|Dim V′ = dim V]], [[§12 Duality#^ladr-3-128|The null space of T]](a) and [[§12 Duality#^ladr-3-125|Dimension of the annihilator]]:
> $$
> \dim\range T'=\dim W'-\dim\nullsp T'=\dim W-\dim(\range T)^0=\dim\range T .
> $$
> (b) If $\varphi=T'(\psi)$ and $v\in\nullsp T$, then $\varphi(v)=\psi(Tv)=\psi(0)=0$; so $\range T'\subseteq(\nullsp T)^0$. Both have the same dimension: $\dim\range T'=\dim\range T=\dim V-\dim\nullsp T=\dim(\nullsp T)^0$ (by (a), [[Fundamental theorem of linear maps]], [[§12 Duality#^ladr-3-125|Dimension of the annihilator]]). Hence equality ([[§6 Dimension#^ladr-2-39|Subspace of full dimension equals the whole space]]).
>
> *Corollary.* $T$ injective $\iff\nullsp T=\{0\}\iff(\nullsp T)^0=V'$ ([[§12 Duality#^ladr-3-127|Condition for the annihilator to equal {0} or the whole space]](b)) $\iff\range T'=V'$ (by (b)).

*Uses:* [[Fundamental theorem of linear maps|3.21]], [[§12 Duality#^ladr-3-111|3.111]], [[§12 Duality#^ladr-3-128|3.128]], [[§12 Duality#^ladr-3-125|3.125]], [[§6 Dimension#^ladr-2-39|2.39]], [[§12 Duality#^ladr-3-127|3.127]]

> [!remark]- Connections
> - (a) is the abstract form of row rank $=$ column rank: [[§12 Duality#^ladr-3-133|Column rank equals row rank (LADR 3.133)]].

%% ex:3.130-fig %%
> [!example] Example: Null spaces and ranges under duality
> Passing to the dual map swaps the roles of null space and range: the annihilator of $\nullsp T$ is $\range T'$ ([[§12 Duality#^ladr-3-130|3.130]](b)), and the annihilator of $\range T$ is $\nullsp T'$ ([[§12 Duality#^ladr-3-128|3.128]](a)). That is why injectivity of $T$ matches surjectivity of $T'$, and surjectivity of $T$ matches injectivity of $T'$.
>
> ![[ladr-3.130-four-subspaces.svg|440]]

> [!theorem] Theorem 3.132: Matrix of $T'$ is the transpose of the matrix of $T$
> Let $V,W$ be finite-dimensional, $T\in\Lin(V,W)$, with bases $v_1,\dots,v_n$ of $V$, $w_1,\dots,w_m$ of $W$ and the dual bases $\varphi_1,\dots,\varphi_n$, $\psi_1,\dots,\psi_m$. Then
> $$
> \mathcal{M}(T')=\big(\mathcal{M}(T)\big)^t .
> $$

^ladr-3-132

> [!proof]+ Proof
> Let $A=\mathcal{M}(T)$, $C=\mathcal{M}(T')$. By definition $T'(\psi_j)=\sum_rC_{r,j}\varphi_r$; evaluating at $v_k$ gives $(\psi_j\circ T)(v_k)=C_{k,j}$. On the other hand
> $$
> (\psi_j\circ T)(v_k)=\psi_j\Big(\sum_rA_{r,k}w_r\Big)=A_{j,k}.
> $$
> So $C_{k,j}=A_{j,k}$, i.e. $C=A^t$.

> [!remark]- Connections
> - Explains [[§12 Duality#^ladr-3-120|Algebraic properties of dual maps]](c) as $(AB)^t=B^tA^t$. Used in [[§12 Duality#^ladr-3-133|Column rank equals row rank (LADR 3.133)]].
> - With respect to orthonormal bases the adjoint has the conjugate transpose: [[§22 Self-Adjoint and Normal Operators#^ladr-7-9|Matrix of T (LADR 7.9)]].
> - This is why covector components change by the transpose of the inverse Jacobian: [[§35 The Tangent Bundle#^prop-35-5|591 Prop. §35.5]].
> - Used in Relativity: because the dual map has the transposed matrix, lower indices transform with the inverse transpose $\Lambda_\mu{}^\nu$ — [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-3|REL Theorem §B1.2.3]], [[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]].

> [!theorem] Theorem 3.133: Column rank equals row rank
> For every $A\in\F^{m,n}$, the column rank of $A$ equals the row rank of $A$.

^ladr-3-133

> [!proof]+ Proof
> Let $T:\F^{n,1}\to\F^{m,1}$, $Tx=Ax$, so $\mathcal{M}(T)=A$ in the standard bases. Then
> $$
> \text{col rank }A=\dim\range T=\dim\range T'=\text{col rank }\mathcal{M}(T')=\text{col rank }A^t=\text{row rank }A,
> $$
> using [[§10 Invertibility and Isomorphisms#^ladr-3-78|Dimension of range T equals column rank of M(T)]], [[§12 Duality#^ladr-3-130|The range of T]](a), [[§10 Invertibility and Isomorphisms#^ladr-3-78|Dimension of range T equals column rank of M(T)]], [[§12 Duality#^ladr-3-132|Matrix of T (LADR 3.132)]].

*Uses:* [[§10 Invertibility and Isomorphisms#^ladr-3-78|3.78]], [[§12 Duality#^ladr-3-130|3.130]], [[§12 Duality#^ladr-3-132|3.132]]

> [!remark]- Connections
> - First proof by column–row factorization: [[§9 Matrices#^ladr-3-57|Column rank equals row rank (LADR 3.57)]]. A third proof via adjoints appears in Chapter 7.
> - Computational version: [[§28 Rank#^thm-28-3|235 Thm. §28.3]] (dim Row A = dim Col A).
