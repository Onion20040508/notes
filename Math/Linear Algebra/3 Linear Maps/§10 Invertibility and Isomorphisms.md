---
type: section
subject: "[[Linear Algebra]]"
chapter: 3
section: 10
aliases: ["LADR 3D", "3D Invertibility and Isomorphisms"]
tags: [linear-algebra]
---
← [[§9 Matrices]] · ↑ [[· 3 Linear Maps]] · [[§11 Products and Quotients of Vector Spaces]] →

> [!definition] Definition 3.59: Invertible, inverse
> $T\in\Lin(V,W)$ is *invertible* if there is $S\in\Lin(W,V)$ with $ST=I_V$ and $TS=I_W$. Such an $S$ is called an *inverse* of $T$.

^ladr-3-59

> [!remark]- Connections
> - The inverse is unique: [[§10 Invertibility and Isomorphisms#^ladr-3-60|Inverse is unique]] (so we write $T^{-1}$). Criterion: [[§10 Invertibility and Isomorphisms#^ladr-3-63|Invertibility ⟺ injectivity and surjectivity]]. Synonym: isomorphism [[§10 Invertibility and Isomorphisms#^ladr-3-69|Isomorphism, isomorphic]].
> - In ℝⁿ: [[§13 Characterizations of Invertible Matrices#^def-13-1|235 Def. §13.1]] (invertible linear transformation); for matrices, [[§12 The Inverse of a Matrix#^def-12-1|235 Def. §12.1]].

> [!theorem] Theorem 3.60: Inverse is unique
> An invertible linear map has a unique inverse.

^ladr-3-60

> [!proof]+ Proof
> If $S_1,S_2$ are inverses of $T$, then $S_1=S_1I=S_1(TS_2)=(S_1T)S_2=IS_2=S_2$.

> [!remark]- Connections
> - Same argument as [[§2 Definition of Vector Space#^ladr-1-27|Unique additive inverse]]; same argument for matrices in [[§10 Invertibility and Isomorphisms#^ladr-3-80|Invertible, inverse, A⁻¹]].
> - For arbitrary functions: [[§9 Injections, Surjections and Bijections#^thm-9-2|250 Thm. §9.2]] (an inverse, when it exists, is unique).
> - Same argument in any group: [[§2 First Consequences of the Axioms#^prop-2-3|493 Prop. §2.3]].
> - Matrix version: [[§12 The Inverse of a Matrix#^prop-12-1|235 Prop. §12.1]].

> [!remark] Notation 3.61: T⁻¹ (p. 82)
> If $T\in\Lin(V,W)$ is invertible, its inverse is written $T^{-1}$: the unique $T^{-1}\in\Lin(W,V)$ with $T^{-1}T=I_V$ and $TT^{-1}=I_W$.

^ladr-3-61

> [!example] Example 3.62: Inverse of a linear map from R³ to R³ (p. 82)
> $T(x,y,z)=(-y,x,4z)$ on $\R^3$ rotates the $xy$-plane by $90^\circ$ counterclockwise and stretches the $z$-axis by $4$. Its inverse undoes both:
> $$
> T^{-1}(x,y,z)=\big(y,\,-x,\,\tfrac14z\big),
> $$
> as $T\big(y,-x,\tfrac z4\big)=(x,y,z)$ confirms.

^ladr-3-62

> [!theorem] Theorem 3.63: Invertibility ⟺ injectivity and surjectivity
> A linear map is invertible if and only if it is injective and surjective.

^ladr-3-63

> [!proof]+ Proof
> ($\Rightarrow$) If $Tu=Tv$ then $u=T^{-1}Tu=T^{-1}Tv=v$. Any $w\in W$ equals $T(T^{-1}w)$.
>
> ($\Leftarrow$) For $w\in W$ let $S(w)$ be the unique $v$ with $Tv=w$ (exists by surjectivity, unique by injectivity). Then $TS=I_W$. For $v\in V$, $T(STv)=(TS)(Tv)=Tv$, so $STv=v$ by injectivity; thus $ST=I_V$. Linearity of $S$: $T(Sw_1+Sw_2)=w_1+w_2$, so $Sw_1+Sw_2$ is the unique preimage of $w_1+w_2$, i.e. $S(w_1+w_2)=Sw_1+Sw_2$. *(Filled in.)* Likewise $T(\lambda Sw)=\lambda w$ gives $S(\lambda w)=\lambda Sw$.

> [!remark]- Connections
> - Linear bijections automatically have linear inverses. In finite equal dimensions, one condition suffices: [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]].
> - Set-level version: [[§9 Injections, Surjections and Bijections#^thm-9-2|250 Thm. §9.2]] (a function is invertible if and only if it is bijective); the new point here is that the inverse is linear.
> - In ℝⁿ: [[§13 Characterizations of Invertible Matrices#^thm-13-3|235 Thm. §13.3]] (T is invertible iff its standard matrix is), with [[§13 Characterizations of Invertible Matrices#^rem-13-2|235 Remark §13.2]] (invertible means one-to-one and onto).

> [!example] Example 3.64: Neither injectivity nor surjectivity implies invertibility (p. 84)
> In infinite dimensions neither half of [[§10 Invertibility and Isomorphisms#^ladr-3-63|3.63]] suffices:
> - multiplication by $x^2$ on $\Poly(\R)$ is injective but not surjective ($1$ is not in the range);
> - the backward shift on $\F^\infty$ is surjective but not injective ($(1,0,0,\dots)$ is in the null space).
>
> Contrast [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]]: in equal finite dimensions either condition alone gives invertibility.

^ladr-3-64

> [!theorem] Theorem 3.65: Injectivity is equivalent to surjectivity (if dim V = dim W < ∞)
> Suppose $V,W$ are finite-dimensional, $\dim V=\dim W$, and $T\in\Lin(V,W)$. Then
> $$
> T\text{ invertible}\iff T\text{ injective}\iff T\text{ surjective}.
> $$

^ladr-3-65

> [!remark] Remark: Finite dimension is essential
> On $\F^\infty$, the backward shift is surjective but not injective and the forward shift is injective but not surjective.

> [!proof]+ Proof
> By [[Fundamental theorem of linear maps]], $\dim V=\dim\nullsp T+\dim\range T$. If $T$ is injective, then $\dim\nullsp T=0$ ([[§8 Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]]), so $\dim\range T=\dim V=\dim W$ and $\range T=W$ by [[§6 Dimension#^ladr-2-39|Subspace of full dimension equals the whole space]]. If $T$ is surjective, then $\dim\nullsp T=\dim V-\dim W=0$, so $T$ is injective. Either condition therefore gives both, hence invertibility by [[§10 Invertibility and Isomorphisms#^ladr-3-63|Invertibility ⟺ injectivity and surjectivity]].

*Uses:* [[Fundamental theorem of linear maps|3.21]], [[§8 Null Spaces and Ranges#^ladr-3-15|3.15]], [[§6 Dimension#^ladr-2-39|2.39]], [[§10 Invertibility and Isomorphisms#^ladr-3-63|3.63]]

> [!remark]- Connections
> - Finite-set analogue, with cardinality in place of dimension: [[§11 Properties of Finite Sets#^thm-11-7|250 Thm. §11.7]].
> - Matrix version: the Invertible Matrix Theorem, [[§13 Characterizations of Invertible Matrices#^thm-13-1|235 Thm. §13.1]] ((a), (f) and (i) are equivalent for square A).
> - Analogue for boundary value problems: [[§5★ Green's Functions#^thm-5-3|341 Thm. §5.3]] (a two-point boundary value problem has exactly one solution for every right side unless the homogeneous problem has a nonzero solution, and then it has none or infinitely many).

%% ex:3.65-fig %%
> [!example] Example: The shifts on $\F^\infty$, pictured
> The backward shift $(x_1,x_2,x_3,\dots)\mapsto(x_2,x_3,\dots)$ discards $x_1$ (red): it is surjective, but $(1,0,0,\dots)$ is sent to $0$. The forward shift $(x_1,x_2,\dots)\mapsto(0,x_1,x_2,\dots)$ loses nothing but always puts $0$ in the first slot (red): it is injective, but $(1,0,0,\dots)$ is not in its range.
>
> ![[ladr-3.65-shifts.svg|480]]

> [!example] Example 3.67: There exists a polynomial $p$ such that $\big((x^2+5x+7)p\big)''=q$ (p. 85)
> **Claim.** For every $q\in\Poly(\R)$ there is $p\in\Poly(\R)$ with $\big((x^2+5x+7)p\big)''=q$.
>
> The map $p\mapsto\big((x^2+5x+7)p\big)''$ is injective on $\Poly(\R)$, but [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]] cannot be used there (see [[§10 Invertibility and Isomorphisms#^ladr-3-64|3.64]]). So restrict: choose $m$ with $q\in\Poly_m(\R)$ and let $T:\Poly_m(\R)\to\Poly_m(\R)$, $Tp=\big((x^2+5x+7)p\big)''$. Multiplying by the quadratic raises degree by $2$ and differentiating twice lowers it by $2$, so $T$ maps into $\Poly_m(\R)$.
>
> $T$ is injective: if $Tp=0$ then $(x^2+5x+7)p=ax+b$, which forces $p=0$ by degree count. By [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]], $T$ is surjective, so $q=Tp$ for some $p$.
>
> The trick (reduce an infinite-dimensional problem to a finite-dimensional invariant piece) recurs throughout the book.

^ladr-3-67

> [!theorem] Theorem 3.68: ST = I ⟺ TS = I (on vector spaces of the same dimension)
> Let $V,W$ be finite-dimensional of the same dimension, $S\in\Lin(V,W)$, $T\in\Lin(W,V)$. Then $ST=I\iff TS=I$.

^ladr-3-68

> [!proof]+ Proof
> Suppose $ST=I$. If $Tv=0$ then $v=STv=S0=0$, so $T$ is injective ([[§8 Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]]) and hence invertible ([[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]]). Multiplying $ST=I$ on the right by $T^{-1}$ gives $S=T^{-1}$, so $TS=I$. The converse follows by swapping roles.

*Uses:* [[§8 Null Spaces and Ranges#^ladr-3-15|3.15]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]]

> [!remark]- Connections
> - For square matrices: a one-sided inverse is automatically two-sided. Fails in infinite dimensions (shift operators).
> - In a group a one-sided inverse is automatically two-sided, [[§2 First Consequences of the Axioms#^prop-2-6|493 Prop. §2.6]]; here the reason is dimension instead, since L(V) is not a group.
> - The failure in infinite dimensions: the right shift on ℓ² has a left inverse but is not onto, [[§24 Orthonormal Sets and Bases#^ex-24-2|556 Ex. §24.2]].
> - Used in 591 to define the unitary group by one equation: [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^lem-22-3|591 Lemma §22.3]], proved there with determinants.
> - Matrix version: [[§13 Characterizations of Invertible Matrices#^cor-13-2|235 Cor. §13.2]] (a one-sided inverse of a square matrix is an inverse).

> [!definition] Definition 3.69: Isomorphism, isomorphic
> An *isomorphism* is an invertible linear map. $V$ and $W$ are *isomorphic* if there is an isomorphism from $V$ onto $W$.

^ladr-3-69

> [!remark] Remark: Relabeling
> An isomorphism $T:V\to W$ relabels $v$ as $Tv$; isomorphic spaces share every vector-space property.

> [!remark]- Connections
> - Classified by dimension: [[Dimension shows whether vector spaces are isomorphic]]. First isomorphism theorem: [[First isomorphism theorem]].
> - Group version: [[§16 Isomorphisms#^def-16-1|493 Def. §16.1]].
> - Computational version: [[§26 Coordinate Systems#^def-26-3|235 Def. §26.3]].
> - ODE example: $y \mapsto (y(t_0), y'(t_0))$ is an isomorphism from the solution space of $y'' + py' + qy = 0$ onto $\mathbb{R}^2$, [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^rem-14-2|331 Remark §14.2]]; for systems, $\mathbf{x} \mapsto \mathbf{x}(t_0)$, [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-2|331 Thm. §30.2]].

> [!theorem] Theorem 3.70: Dimension shows whether vector spaces are isomorphic
> Two finite-dimensional vector spaces over $\F$ are isomorphic if and only if they have the same dimension.

^ladr-3-70

> [!remark] Remark: Why not just study $\F^n$
> Every $n$-dimensional space is isomorphic to $\F^n$, but only via a choice of basis. Natural constructions (null spaces, ranges, quotients, duals) do not come with preferred bases.

> [!proof]+ Proof
> ($\Rightarrow$) If $T:V\to W$ is an isomorphism, then $\nullsp T=\{0\}$ and $\range T=W$, so [[Fundamental theorem of linear maps]] gives $\dim V=0+\dim W$.
>
> ($\Leftarrow$) Let $v_1,\dots,v_n$ and $w_1,\dots,w_n$ be bases. Define $T(\sum c_kv_k)=\sum c_kw_k$ (a linear map by [[Linear map lemma]]). It is surjective since the $w$'s span, and injective since the $w$'s are independent ($\sum c_kw_k=0\Rightarrow$ all $c_k=0$). So $T$ is an isomorphism by [[§10 Invertibility and Isomorphisms#^ladr-3-63|Invertibility ⟺ injectivity and surjectivity]].

*Uses:* [[Fundamental theorem of linear maps|3.21]], [[Linear map lemma|3.4]], [[§10 Invertibility and Isomorphisms#^ladr-3-63|3.63]]

> [!remark]- Connections
> - Computational version: [[§26 Coordinate Systems#^thm-26-3|235 Thm. §26.3]] (a space with a basis of n vectors is isomorphic to ℝⁿ) and [[§27 The Dimension of a Vector Space#^prop-27-7|235 Prop. §27.7]] (isomorphic spaces have the same dimension).
> - ODE example: so the solution space of $y'' + py' + qy = 0$ has dimension 2, [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^rem-14-2|331 Remark §14.2]], and that of $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$ has dimension $n$, [[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-3|331 Def. §30.3]].

> [!theorem] Theorem 3.72: Dim L(V, W) = (dim V)(dim W)
> If $V,W$ are finite-dimensional, then $\Lin(V,W)$ is finite-dimensional and $\dim\Lin(V,W)=(\dim V)(\dim W)$.

^ladr-3-72

> [!proof]+ Proof
> *(Filled in: Axler 3.71.)* Fix bases, $\dim V=n$, $\dim W=m$. The map $\mathcal{M}:\Lin(V,W)\to\F^{m,n}$ is linear by [[§9 Matrices#^ladr-3-35|Matrix of the sum of linear maps]] and [[§9 Matrices#^ladr-3-38|The matrix of a scalar times a linear map]]. It is injective: $\mathcal{M}(T)=0$ means $Tv_k=0$ for all $k$, so $T=0$. It is surjective: given $A$, [[Linear map lemma]] gives $T$ with $Tv_k=\sum_jA_{j,k}w_j$. So $\Lin(V,W)\cong\F^{m,n}$, and $\dim\Lin(V,W)=mn$ by [[Dimension shows whether vector spaces are isomorphic]] and [[§9 Matrices#^ladr-3-40|Dim Fᵐ’ⁿ = mn]].

*Uses:* [[§9 Matrices#^ladr-3-35|3.35]], [[§9 Matrices#^ladr-3-38|3.38]], [[Linear map lemma|3.4]], [[Dimension shows whether vector spaces are isomorphic|3.70]], [[§9 Matrices#^ladr-3-40|3.40]]

> [!remark]- Connections
> - Special case $W=\F$: $\dim V'=\dim V$ ([[§12 Duality#^ladr-3-111|Dim V′ = dim V]]).

> [!definition] Definition 3.73: Matrix of a vector, M(v)
> Let $v_1,\dots,v_n$ be a basis of $V$. The *matrix of $v\in V$* is the $n$-by-$1$ matrix $\mathcal{M}(v)=(b_1,\dots,b_n)^t$ where $v=b_1v_1+\dots+b_nv_n$.

^ladr-3-73

> [!remark] Remark: Coordinates
> $v\mapsto\mathcal{M}(v)$ is an isomorphism $V\to\F^{n,1}$ (well defined by [[§5 Bases#^ladr-2-28|Criterion for basis]]). Column $k$ of $\mathcal{M}(T)$ is $\mathcal{M}(Tv_k)$ (Axler 3.75).

> [!remark]- Connections
> - How $T$ acts in coordinates: [[§10 Invertibility and Isomorphisms#^ladr-3-76|Linear maps act like matrix multiplication]].
> - A basis read as the isomorphism v ↦ M(v) is what 591 calls a linear coordinate system: [[§21 The Differential of a Map Between Vector Spaces#^def-21-1|591 Def. §21.1]].
> - Computational version: [[§26 Coordinate Systems#^def-26-1|235 Def. §26.1]] (the coordinate vector [x]_B), an isomorphism onto ℝⁿ by [[§26 Coordinate Systems#^thm-26-3|235 Thm. §26.3]].

> [!example] Example 3.74: Matrix of a vector (p. 88)
> - The matrix of $2-7x+5x^3+x^4$ in the standard basis of $\Poly_4(\R)$ is $(2,-7,0,5,1)^t$.
> - For $x=(x_1,\dots,x_n)\in\F^n$ and the standard basis, $\mathcal{M}(x)=(x_1,\dots,x_n)^t$.
>
> Once a basis is fixed, $v\mapsto\mathcal{M}(v)$ is an isomorphism $V\to\F^{n,1}$: coordinates are a relabeling ([[§10 Invertibility and Isomorphisms#^ladr-3-73|3.73]]).

^ladr-3-74

> [!theorem] Theorem 3.76: Linear maps act like matrix multiplication
> Let $T\in\Lin(V,W)$, $v\in V$, with bases $v_1,\dots,v_n$ of $V$ and $w_1,\dots,w_m$ of $W$. Then
> $$
> \mathcal{M}(Tv)=\mathcal{M}(T)\,\mathcal{M}(v).
> $$

^ladr-3-76

> [!remark] Remark: Every map is a matrix, after relabeling
> Identifying $v$ with $\mathcal{M}(v)$, $T$ becomes multiplication by $\mathcal{M}(T)$ on $\F^{n,1}$. The matrix depends on the bases, and choosing bases to simplify it is a central theme later.

> [!proof]+ Proof
> Write $v=b_1v_1+\dots+b_nv_n$, so $Tv=\sum b_kTv_k$. Since $\mathcal{M}$ is linear on $W$ and $\mathcal{M}(Tv_k)$ is column $k$ of $\mathcal{M}(T)$,
> $$
> \mathcal{M}(Tv)=\sum_kb_k\,\mathcal{M}(T)_{\cdot,k}=\mathcal{M}(T)\mathcal{M}(v)
> $$
> by [[§9 Matrices#^ladr-3-50|Linear combination of columns]].

*Uses:* [[§9 Matrices#^ladr-3-50|3.50]]

> [!remark]- Connections
> - Used in [[§10 Invertibility and Isomorphisms#^ladr-3-78|Dimension of range T equals column rank of M(T)]] and in the change-of-basis story [[§10 Invertibility and Isomorphisms#^ladr-3-84|Change-of-basis formula (LADR 3.84)]].
> - Computational version: [[§35 Eigenvectors and Linear Transformations#^thm-35-1|235 Thm. §35.1]] ([T(x)]_C = M[x]_B).

> [!theorem] Theorem 3.78: Dimension of range T equals column rank of M(T)
> If $V,W$ are finite-dimensional and $T\in\Lin(V,W)$, then $\dim\range T$ equals the column rank of $\mathcal{M}(T)$.

^ladr-3-78

> [!proof]+ Proof
> $w\mapsto\mathcal{M}(w)$ is an isomorphism $W\to\F^{m,1}$. *(Filled in.)* $\range T=\Span(Tv_1,\dots,Tv_n)$, since $T(\sum c_kv_k)=\sum c_kTv_k$. The isomorphism restricts to an isomorphism from $\range T$ onto $\Span(\mathcal{M}(Tv_1),\dots,\mathcal{M}(Tv_n))$, and $\mathcal{M}(Tv_k)$ is column $k$ of $\mathcal{M}(T)$. Isomorphic spaces have equal dimension ([[Dimension shows whether vector spaces are isomorphic]]).

*Uses:* [[Dimension shows whether vector spaces are isomorphic|3.70]]

> [!remark]- Connections
> - With [[Fundamental theorem of linear maps]]: $\dim V=\dim\nullsp T+\operatorname{rank}\mathcal{M}(T)$, the matrix rank–nullity theorem.
> - In ℝⁿ: the range of x ↦ Ax is Col A ([[§24 Null Spaces, Column Spaces, and Linear Transformations#^def-24-2|235 Def. §24.2]]), of dimension rank A, the number of pivot columns ([[§27 The Dimension of a Vector Space#^thm-27-8|235 Thm. §27.8]]).

> [!definition] Definition 3.79: Identity matrix, I
> The $n$-by-$n$ *identity matrix* $I$ has $1$'s on the diagonal and $0$'s elsewhere.

^ladr-3-79

> [!remark] Remark: Two meanings of $I$
> With respect to any single basis, $\mathcal{M}(I)=I$ (operator on the left, matrix on the right). $AI=IA=A$ for square $A$ of the same size.

> [!remark]- Connections
> - With two different bases $\mathcal{M}(I)$ is not the identity matrix: [[§10 Invertibility and Isomorphisms#^ladr-3-82|Matrix of identity operator with respect to two bases]].

> [!definition] Definition 3.80: Invertible, inverse, A⁻¹
> A square matrix $A$ is *invertible* if there is a square matrix $B$ of the same size with $AB=BA=I$; then $B$ is unique and written $A^{-1}$.

^ladr-3-80

> [!remark] Remark: Rules
> Uniqueness: same proof as [[§10 Invertibility and Isomorphisms#^ladr-3-60|Inverse is unique]]. $(A^{-1})^{-1}=A$, and $(AC)^{-1}=C^{-1}A^{-1}$ since $(AC)(C^{-1}A^{-1})=AIA^{-1}=I$ and similarly on the other side. By [[§10 Invertibility and Isomorphisms#^ladr-3-68|ST = I ⟺ TS = I (on vector spaces of the same dimension)]], one of $AB=I$, $BA=I$ already implies the other.

> [!remark]- Connections
> - Matrix of an inverse map: [[§10 Invertibility and Isomorphisms#^ladr-3-86|Matrix of inverse equals inverse of matrix]]. Determinant test: [[Invertible ⟺ nonzero determinant]].
> - The invertible n-by-n matrices form a group under multiplication, the general linear group: [[§3 Basic Examples of Groups#^def-3-6|493 Def. §3.6]].
> - Computational version: [[§12 The Inverse of a Matrix#^def-12-1|235 Def. §12.1]], with (A⁻¹)⁻¹ = A and (AB)⁻¹ = B⁻¹A⁻¹ in [[§12 The Inverse of a Matrix#^thm-12-4|235 Thm. §12.4]].

> [!theorem] Theorem 3.81: Matrix of product of linear maps
> Let $T\in\Lin(U,V)$, $S\in\Lin(V,W)$ with bases $u_1,\dots,u_m$ of $U$, $v_1,\dots,v_n$ of $V$, $w_1,\dots,w_p$ of $W$. Then
> $$
> \mathcal{M}\big(ST,(u),(w)\big)=\mathcal{M}\big(S,(v),(w)\big)\,\mathcal{M}\big(T,(u),(v)\big).
> $$

^ladr-3-81

> [!remark] Remark: Reading $\mathcal{M}(I,(u),(v))$
> Its column $k$ holds the coordinates of $u_k$ in the basis $v_1,\dots,v_n$: it converts $u$-coordinates into $v$-coordinates.

> [!proof]+ Proof
> This is [[§9 Matrices#^ladr-3-43|Matrix of product of linear maps (LADR 3.43)]] with the bases written out.

*Uses:* [[§9 Matrices#^ladr-3-43|3.43]]

> [!remark]- Connections
> - Used in [[§10 Invertibility and Isomorphisms#^ladr-3-82|Matrix of identity operator with respect to two bases]] and [[§10 Invertibility and Isomorphisms#^ladr-3-84|Change-of-basis formula (LADR 3.84)]].

> [!theorem] Theorem 3.82: Matrix of identity operator with respect to two bases
> If $u_1,\dots,u_n$ and $v_1,\dots,v_n$ are bases of $V$, then $\mathcal{M}(I,(u),(v))$ and $\mathcal{M}(I,(v),(u))$ are invertible and inverse to each other.

^ladr-3-82

> [!proof]+ Proof
> Apply [[§10 Invertibility and Isomorphisms#^ladr-3-81|Matrix of product of linear maps (LADR 3.81)]] with $S=T=I$ and $w=u$:
> $$
> I=\mathcal{M}(I,(v),(u))\,\mathcal{M}(I,(u),(v)).
> $$
> Swapping the roles of $u$ and $v$ gives the product in the other order.

*Uses:* [[§10 Invertibility and Isomorphisms#^ladr-3-81|3.81]]

> [!remark]- Connections
> - The change-of-basis matrix $C$ in [[§10 Invertibility and Isomorphisms#^ladr-3-84|Change-of-basis formula (LADR 3.84)]].
> - Computational version: [[§29 Change of Basis#^thm-29-2|235 Thm. §29.2]] ((P_{C←B})⁻¹ = P_{B←C}); M(I, (u), (v)) is the matrix P_{v←u} of [[§29 Change of Basis#^thm-29-1|235 Thm. §29.1]].

> [!example] Example 3.83: Matrix of identity on F² (p. 92)
> Bases $u=((4,2),(5,3))$ and $e=((1,0),(0,1))$ of $\F^2$. Since $(4,2)=4e_1+2e_2$ and $(5,3)=5e_1+3e_2$,
> $$
> \mathcal{M}\big(I,(u),(e)\big)=\begin{pmatrix}4&5\\2&3\end{pmatrix},\qquad
> \mathcal{M}\big(I,(e),(u)\big)=\begin{pmatrix}4&5\\2&3\end{pmatrix}^{-1}=\begin{pmatrix}\tfrac32&-\tfrac52\\-1&2\end{pmatrix}
> $$
> by [[§10 Invertibility and Isomorphisms#^ladr-3-82|3.82]] (check: the product is $I$). The second matrix converts standard coordinates into $u$-coordinates.

^ladr-3-83

> [!remark]- Connections
> - In 235: [[§26 Coordinate Systems#^def-26-2|235 Def. §26.2]] (P_B = [b₁ ⋯ bₙ] converts B-coordinates to standard ones) and [[§26 Coordinate Systems#^prop-26-2|235 Prop. §26.2]] (P_B⁻¹ converts back).

> [!theorem] Theorem 3.84: Change-of-basis formula
> Let $T\in\Lin(V)$ and let $u_1,\dots,u_n$, $v_1,\dots,v_n$ be bases of $V$. With
> $$
> A=\mathcal{M}(T,(u)),\quad B=\mathcal{M}(T,(v)),\quad C=\mathcal{M}(I,(u),(v)),
> $$
> we have $A=C^{-1}BC$.

^ladr-3-84

> [!remark] Remark: Reading it right to left
> $C$ converts $u$-coordinates to $v$-coordinates, $B$ applies $T$ in $v$-coordinates, $C^{-1}$ converts back.

> [!proof]+ Proof
> By [[§10 Invertibility and Isomorphisms#^ladr-3-81|Matrix of product of linear maps (LADR 3.81)]] (with $S=I$, target basis $u$) and [[§10 Invertibility and Isomorphisms#^ladr-3-82|Matrix of identity operator with respect to two bases]]: $A=C^{-1}\,\mathcal{M}(T,(u),(v))$. By [[§10 Invertibility and Isomorphisms#^ladr-3-81|Matrix of product of linear maps (LADR 3.81)]] again (with $T$ replaced by $I$ and $S$ by $T$): $\mathcal{M}(T,(u),(v))=BC$. Substitute.

*Uses:* [[§10 Invertibility and Isomorphisms#^ladr-3-81|3.81]], [[§10 Invertibility and Isomorphisms#^ladr-3-82|3.82]]

> [!remark]- Connections
> - Similar matrices describe the same operator; similarity invariants: [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-50|Trace of matrix of operator does not depend on basis]], [[§34 Determinants#^ladr-9-52|Determinant is a similarity invariant]].
> - Physics: with orthonormal bases $C$ is unitary and this is the familiar $A=U^\dagger BU$ change of representation.
> - Bilinear-form version (different rule, $C^tBC$): [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-7|Change-of-basis formula (LADR 9.7)]].
> - Similarity is conjugation by an invertible matrix; for invertible matrices, similar means conjugate in the general linear group: [[§33 Conjugacy Classes#^def-33-3|493 Def. §33.3]].
> - On a manifold the change-of-basis matrix between coordinate bases is the Jacobian of the transition map ([[§28 The Differential in Coordinates#^cor-28-4|591 Cor. §28.4]]); it gives the transition maps of the tangent bundle, [[§35 The Tangent Bundle#^prop-35-2|591 Prop. §35.2]].
> - Computational version: [[§35 Eigenvectors and Linear Transformations#^thm-35-2|235 Thm. §35.2]], [T]_B = P⁻¹AP, so the matrices of one operator are similar ([[§33 The Characteristic Equation#^def-33-3|235 Def. §33.3]]).

%% ex:3.84-diagram %%
> [!example] Example: Reading the change-of-basis formula as a diagram
> Both paths from the top-left corner to the top-right give $A$: apply $T$ in $u$-coordinates directly, or convert to $v$-coordinates ($C$), apply $T$ there ($B$), and convert back ($C^{-1}$). That is $A=C^{-1}BC$.
>
> ![[ladr-3.84-change-of-basis.svg|520]]
>
> With the bases of [[§10 Invertibility and Isomorphisms#^ladr-3-83|3.83]]: $C=\mathcal{M}(I,(u),(e))$ turns $u$-coordinates into standard ones, so for $T$ with standard matrix $B$, the matrix in the basis $(4,2),(5,3)$ is $C^{-1}BC$.

> [!theorem] Theorem 3.86: Matrix of inverse equals inverse of matrix
> If $v_1,\dots,v_n$ is a basis of $V$ and $T\in\Lin(V)$ is invertible, then $\mathcal{M}(T^{-1})=\mathcal{M}(T)^{-1}$ (all with respect to $v_1,\dots,v_n$).

^ladr-3-86

> [!proof]+ Proof
> *(Filled in; left as an exercise in Axler.)* By [[§9 Matrices#^ladr-3-43|Matrix of product of linear maps (LADR 3.43)]], $\mathcal{M}(T^{-1})\mathcal{M}(T)=\mathcal{M}(T^{-1}T)=\mathcal{M}(I)=I$, and likewise $\mathcal{M}(T)\mathcal{M}(T^{-1})=I$. So $\mathcal{M}(T^{-1})$ is the inverse of $\mathcal{M}(T)$ ([[§10 Invertibility and Isomorphisms#^ladr-3-80|Invertible, inverse, A⁻¹]]).

*Uses:* [[§9 Matrices#^ladr-3-43|3.43]], [[§10 Invertibility and Isomorphisms#^ladr-3-80|3.80]]

> [!remark]- Connections
> - So $T$ is invertible iff $\mathcal{M}(T)$ is (the converse via [[§10 Invertibility and Isomorphisms#^ladr-3-72|Dim L(V, W) = (dim V)(dim W)]]: an inverse matrix is the matrix of some map).
> - In ℝⁿ: [[§13 Characterizations of Invertible Matrices#^thm-13-3|235 Thm. §13.3]] (T⁻¹ is x ↦ A⁻¹x).
