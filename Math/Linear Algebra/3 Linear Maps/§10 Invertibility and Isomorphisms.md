---
type: section
subject: "[[Linear Algebra]]"
chapter: 3
section: 10
aliases: ["LADR 3D", "3D Invertibility and Isomorphisms"]
tags: [linear-algebra]
---
← [[§9 Matrices]] · ↑ [[· 3 Linear Maps]] · [[§11 Products and Quotients of Vector Spaces]] →

> [!definition] 3.59 Invertible, inverse
> $T\in\Lin(V,W)$ is *invertible* if there is $S\in\Lin(W,V)$ with $ST=I_V$ and $TS=I_W$. Such an $S$ is called an *inverse* of $T$.

^ladr-3-59

> [!remark]- Connections
> - The inverse is unique: [[§10 Invertibility and Isomorphisms#^ladr-3-60|Inverse is unique]] (so we write $T^{-1}$). Criterion: [[§10 Invertibility and Isomorphisms#^ladr-3-63|Invertibility ⟺ injectivity and surjectivity]]. Synonym: isomorphism [[§10 Invertibility and Isomorphisms#^ladr-3-69|Isomorphism, isomorphic]].

> [!theorem] 3.60 Inverse is unique
> An invertible linear map has a unique inverse.

^ladr-3-60

> [!proof]+
> If $S_1,S_2$ are inverses of $T$, then $S_1=S_1I=S_1(TS_2)=(S_1T)S_2=IS_2=S_2$.

> [!remark]- Connections
> - Same argument as [[§2 Definition of Vector Space#^ladr-1-27|Unique additive inverse]]; same argument for matrices in [[§10 Invertibility and Isomorphisms#^ladr-3-80|Invertible, inverse, A⁻¹]].

> [!remark] 3.61 Notation: T⁻¹ (p. 82)

^ladr-3-61

> [!example] 3.62 Inverse of a linear map from R³ to R³ (p. 82)
> $T(x,y,z)=(-y,x,4z)$ on $\R^3$ rotates the $xy$-plane by $90^\circ$ counterclockwise and stretches the $z$-axis by $4$. Its inverse undoes both:
> $$
> T^{-1}(x,y,z)=\big(y,\,-x,\,\tfrac14z\big),
> $$
> as $T\big(y,-x,\tfrac z4\big)=(x,y,z)$ confirms.

^ladr-3-62

> [!theorem] 3.63 Invertibility ⟺ injectivity and surjectivity
> A linear map is invertible if and only if it is injective and surjective.

^ladr-3-63

> [!proof]+
> ($\Rightarrow$) If $Tu=Tv$ then $u=T^{-1}Tu=T^{-1}Tv=v$. Any $w\in W$ equals $T(T^{-1}w)$.
>
> ($\Leftarrow$) For $w\in W$ let $S(w)$ be the unique $v$ with $Tv=w$ (exists by surjectivity, unique by injectivity). Then $TS=I_W$. For $v\in V$, $T(STv)=(TS)(Tv)=Tv$, so $STv=v$ by injectivity; thus $ST=I_V$. Linearity of $S$: $T(Sw_1+Sw_2)=w_1+w_2$, so $Sw_1+Sw_2$ is the unique preimage of $w_1+w_2$, i.e. $S(w_1+w_2)=Sw_1+Sw_2$. *(Filled in.)* Likewise $T(\lambda Sw)=\lambda w$ gives $S(\lambda w)=\lambda Sw$.

> [!remark]- Connections
> - Linear bijections automatically have linear inverses. In finite equal dimensions, one condition suffices: [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]].

> [!example] 3.64 Neither injectivity nor surjectivity implies invertibility (p. 84)
> In infinite dimensions neither half of [[§10 Invertibility and Isomorphisms#^ladr-3-63|3.63]] suffices:
> - multiplication by $x^2$ on $\Poly(\R)$ is injective but not surjective ($1$ is not in the range);
> - the backward shift on $\F^\infty$ is surjective but not injective ($(1,0,0,\dots)$ is in the null space).
>
> Contrast [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]]: in equal finite dimensions either condition alone gives invertibility.

^ladr-3-64

> [!theorem] 3.65 Injectivity is equivalent to surjectivity (if dim V = dim W < ∞)
> Suppose $V,W$ are finite-dimensional, $\dim V=\dim W$, and $T\in\Lin(V,W)$. Then
> $$
> T\text{ invertible}\iff T\text{ injective}\iff T\text{ surjective}.
> $$

^ladr-3-65

> [!remark] Finite dimension is essential
> On $\F^\infty$, the backward shift is surjective but not injective and the forward shift is injective but not surjective.

> [!proof]+
> By [[Fundamental theorem of linear maps]], $\dim V=\dim\nullsp T+\dim\range T$. If $T$ is injective, then $\dim\nullsp T=0$ ([[§8 Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]]), so $\dim\range T=\dim V=\dim W$ and $\range T=W$ by [[§6 Dimension#^ladr-2-39|Subspace of full dimension equals the whole space]]. If $T$ is surjective, then $\dim\nullsp T=\dim V-\dim W=0$, so $T$ is injective. Either condition therefore gives both, hence invertibility by [[§10 Invertibility and Isomorphisms#^ladr-3-63|Invertibility ⟺ injectivity and surjectivity]].

*Uses:* [[Fundamental theorem of linear maps|3.21]], [[§8 Null Spaces and Ranges#^ladr-3-15|3.15]], [[§6 Dimension#^ladr-2-39|2.39]], [[§10 Invertibility and Isomorphisms#^ladr-3-63|3.63]]

%% ex:3.65-fig %%
> [!example] The shifts on $\F^\infty$, pictured
> The backward shift $(x_1,x_2,x_3,\dots)\mapsto(x_2,x_3,\dots)$ discards $x_1$ (red): it is surjective, but $(1,0,0,\dots)$ is sent to $0$. The forward shift $(x_1,x_2,\dots)\mapsto(0,x_1,x_2,\dots)$ loses nothing but always puts $0$ in the first slot (red): it is injective, but $(1,0,0,\dots)$ is not in its range.
>
> ![[ladr-3.65-shifts.svg|480]]

> [!example] 3.67 There exists a polynomial $p$ such that $\big((x^2+5x+7)p\big)''=q$ (p. 85)
> **Claim.** For every $q\in\Poly(\R)$ there is $p\in\Poly(\R)$ with $\big((x^2+5x+7)p\big)''=q$.
>
> The map $p\mapsto\big((x^2+5x+7)p\big)''$ is injective on $\Poly(\R)$, but [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]] cannot be used there (see [[§10 Invertibility and Isomorphisms#^ladr-3-64|3.64]]). So restrict: choose $m$ with $q\in\Poly_m(\R)$ and let $T:\Poly_m(\R)\to\Poly_m(\R)$, $Tp=\big((x^2+5x+7)p\big)''$. Multiplying by the quadratic raises degree by $2$ and differentiating twice lowers it by $2$, so $T$ maps into $\Poly_m(\R)$.
>
> $T$ is injective: if $Tp=0$ then $(x^2+5x+7)p=ax+b$, which forces $p=0$ by degree count. By [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]], $T$ is surjective, so $q=Tp$ for some $p$.
>
> The trick (reduce an infinite-dimensional problem to a finite-dimensional invariant piece) recurs throughout the book.

^ladr-3-67

> [!theorem] 3.68 ST = I ⟺ TS = I (on vector spaces of the same dimension)
> Let $V,W$ be finite-dimensional of the same dimension, $S\in\Lin(V,W)$, $T\in\Lin(W,V)$. Then $ST=I\iff TS=I$.

^ladr-3-68

> [!proof]+
> Suppose $ST=I$. If $Tv=0$ then $v=STv=S0=0$, so $T$ is injective ([[§8 Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]]) and hence invertible ([[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]]). Multiplying $ST=I$ on the right by $T^{-1}$ gives $S=T^{-1}$, so $TS=I$. The converse follows by swapping roles.

*Uses:* [[§8 Null Spaces and Ranges#^ladr-3-15|3.15]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]]

> [!remark]- Connections
> - For square matrices: a one-sided inverse is automatically two-sided. Fails in infinite dimensions (shift operators).

> [!definition] 3.69 Isomorphism, isomorphic
> An *isomorphism* is an invertible linear map. $V$ and $W$ are *isomorphic* if there is an isomorphism from $V$ onto $W$.

^ladr-3-69

> [!remark] Relabeling
> An isomorphism $T:V\to W$ relabels $v$ as $Tv$; isomorphic spaces share every vector-space property.

> [!remark]- Connections
> - Classified by dimension: [[Dimension shows whether vector spaces are isomorphic]]. First isomorphism theorem: [[First isomorphism theorem]].

> [!theorem] 3.70 Dimension shows whether vector spaces are isomorphic
> Two finite-dimensional vector spaces over $\F$ are isomorphic if and only if they have the same dimension.

^ladr-3-70

> [!remark] Why not just study $\F^n$
> Every $n$-dimensional space is isomorphic to $\F^n$, but only via a choice of basis. Natural constructions (null spaces, ranges, quotients, duals) do not come with preferred bases.

> [!proof]+
> ($\Rightarrow$) If $T:V\to W$ is an isomorphism, then $\nullsp T=\{0\}$ and $\range T=W$, so [[Fundamental theorem of linear maps]] gives $\dim V=0+\dim W$.
>
> ($\Leftarrow$) Let $v_1,\dots,v_n$ and $w_1,\dots,w_n$ be bases. Define $T(\sum c_kv_k)=\sum c_kw_k$ (a linear map by [[Linear map lemma]]). It is surjective since the $w$'s span, and injective since the $w$'s are independent ($\sum c_kw_k=0\Rightarrow$ all $c_k=0$). So $T$ is an isomorphism by [[§10 Invertibility and Isomorphisms#^ladr-3-63|Invertibility ⟺ injectivity and surjectivity]].

*Uses:* [[Fundamental theorem of linear maps|3.21]], [[Linear map lemma|3.4]], [[§10 Invertibility and Isomorphisms#^ladr-3-63|3.63]]

> [!theorem] 3.72 Dim L(V, W) = (dim V)(dim W)
> If $V,W$ are finite-dimensional, then $\Lin(V,W)$ is finite-dimensional and $\dim\Lin(V,W)=(\dim V)(\dim W)$.

^ladr-3-72

> [!proof]+
> *(Filled in: Axler 3.71.)* Fix bases, $\dim V=n$, $\dim W=m$. The map $\mathcal{M}:\Lin(V,W)\to\F^{m,n}$ is linear by [[§9 Matrices#^ladr-3-35|Matrix of the sum of linear maps]] and [[§9 Matrices#^ladr-3-38|The matrix of a scalar times a linear map]]. It is injective: $\mathcal{M}(T)=0$ means $Tv_k=0$ for all $k$, so $T=0$. It is surjective: given $A$, [[Linear map lemma]] gives $T$ with $Tv_k=\sum_jA_{j,k}w_j$. So $\Lin(V,W)\cong\F^{m,n}$, and $\dim\Lin(V,W)=mn$ by [[Dimension shows whether vector spaces are isomorphic]] and [[§9 Matrices#^ladr-3-40|Dim Fᵐ’ⁿ = mn]].

*Uses:* [[§9 Matrices#^ladr-3-35|3.35]], [[§9 Matrices#^ladr-3-38|3.38]], [[Linear map lemma|3.4]], [[Dimension shows whether vector spaces are isomorphic|3.70]], [[§9 Matrices#^ladr-3-40|3.40]]

> [!remark]- Connections
> - Special case $W=\F$: $\dim V'=\dim V$ ([[§12 Duality#^ladr-3-111|Dim V′ = dim V]]).

> [!definition] 3.73 Matrix of a vector, M(v)
> Let $v_1,\dots,v_n$ be a basis of $V$. The *matrix of $v\in V$* is the $n$-by-$1$ matrix $\mathcal{M}(v)=(b_1,\dots,b_n)^t$ where $v=b_1v_1+\dots+b_nv_n$.

^ladr-3-73

> [!remark] Coordinates
> $v\mapsto\mathcal{M}(v)$ is an isomorphism $V\to\F^{n,1}$ (well defined by [[§5 Bases#^ladr-2-28|Criterion for basis]]). Column $k$ of $\mathcal{M}(T)$ is $\mathcal{M}(Tv_k)$ (Axler 3.75).

> [!remark]- Connections
> - How $T$ acts in coordinates: [[§10 Invertibility and Isomorphisms#^ladr-3-76|Linear maps act like matrix multiplication]].

> [!example] 3.74 Matrix of a vector (p. 88)
> - The matrix of $2-7x+5x^3+x^4$ in the standard basis of $\Poly_4(\R)$ is $(2,-7,0,5,1)^t$.
> - For $x=(x_1,\dots,x_n)\in\F^n$ and the standard basis, $\mathcal{M}(x)=(x_1,\dots,x_n)^t$.
>
> Once a basis is fixed, $v\mapsto\mathcal{M}(v)$ is an isomorphism $V\to\F^{n,1}$: coordinates are a relabeling ([[§10 Invertibility and Isomorphisms#^ladr-3-73|3.73]]).

^ladr-3-74

> [!theorem] 3.76 Linear maps act like matrix multiplication
> Let $T\in\Lin(V,W)$, $v\in V$, with bases $v_1,\dots,v_n$ of $V$ and $w_1,\dots,w_m$ of $W$. Then
> $$
> \mathcal{M}(Tv)=\mathcal{M}(T)\,\mathcal{M}(v).
> $$

^ladr-3-76

> [!remark] Every map is a matrix, after relabeling
> Identifying $v$ with $\mathcal{M}(v)$, $T$ becomes multiplication by $\mathcal{M}(T)$ on $\F^{n,1}$. The matrix depends on the bases, and choosing bases to simplify it is a central theme later.

> [!proof]+
> Write $v=b_1v_1+\dots+b_nv_n$, so $Tv=\sum b_kTv_k$. Since $\mathcal{M}$ is linear on $W$ and $\mathcal{M}(Tv_k)$ is column $k$ of $\mathcal{M}(T)$,
> $$
> \mathcal{M}(Tv)=\sum_kb_k\,\mathcal{M}(T)_{\cdot,k}=\mathcal{M}(T)\mathcal{M}(v)
> $$
> by [[§9 Matrices#^ladr-3-50|Linear combination of columns]].

*Uses:* [[§9 Matrices#^ladr-3-50|3.50]]

> [!remark]- Connections
> - Used in [[§10 Invertibility and Isomorphisms#^ladr-3-78|Dimension of range T equals column rank of M(T)]] and in the change-of-basis story [[§10 Invertibility and Isomorphisms#^ladr-3-84|Change-of-basis formula (LADR 3.84)]].

> [!theorem] 3.78 Dimension of range T equals column rank of M(T)
> If $V,W$ are finite-dimensional and $T\in\Lin(V,W)$, then $\dim\range T$ equals the column rank of $\mathcal{M}(T)$.

^ladr-3-78

> [!proof]+
> $w\mapsto\mathcal{M}(w)$ is an isomorphism $W\to\F^{m,1}$. *(Filled in.)* $\range T=\Span(Tv_1,\dots,Tv_n)$, since $T(\sum c_kv_k)=\sum c_kTv_k$. The isomorphism restricts to an isomorphism from $\range T$ onto $\Span(\mathcal{M}(Tv_1),\dots,\mathcal{M}(Tv_n))$, and $\mathcal{M}(Tv_k)$ is column $k$ of $\mathcal{M}(T)$. Isomorphic spaces have equal dimension ([[Dimension shows whether vector spaces are isomorphic]]).

*Uses:* [[Dimension shows whether vector spaces are isomorphic|3.70]]

> [!remark]- Connections
> - With [[Fundamental theorem of linear maps]]: $\dim V=\dim\nullsp T+\operatorname{rank}\mathcal{M}(T)$, the matrix rank–nullity theorem.

> [!definition] 3.79 Identity matrix, I
> The $n$-by-$n$ *identity matrix* $I$ has $1$'s on the diagonal and $0$'s elsewhere.

^ladr-3-79

> [!remark] Two meanings of $I$
> With respect to any single basis, $\mathcal{M}(I)=I$ (operator on the left, matrix on the right). $AI=IA=A$ for square $A$ of the same size.

> [!remark]- Connections
> - With two different bases $\mathcal{M}(I)$ is not the identity matrix: [[§10 Invertibility and Isomorphisms#^ladr-3-82|Matrix of identity operator with respect to two bases]].

> [!definition] 3.80 Invertible, inverse, A⁻¹
> A square matrix $A$ is *invertible* if there is a square matrix $B$ of the same size with $AB=BA=I$; then $B$ is unique and written $A^{-1}$.

^ladr-3-80

> [!remark] Rules
> Uniqueness: same proof as [[§10 Invertibility and Isomorphisms#^ladr-3-60|Inverse is unique]]. $(A^{-1})^{-1}=A$, and $(AC)^{-1}=C^{-1}A^{-1}$ since $(AC)(C^{-1}A^{-1})=AIA^{-1}=I$ and similarly on the other side. By [[§10 Invertibility and Isomorphisms#^ladr-3-68|ST = I ⟺ TS = I (on vector spaces of the same dimension)]], one of $AB=I$, $BA=I$ already implies the other.

> [!remark]- Connections
> - Matrix of an inverse map: [[§10 Invertibility and Isomorphisms#^ladr-3-86|Matrix of inverse equals inverse of matrix]]. Determinant test: [[Invertible ⟺ nonzero determinant]].

> [!theorem] 3.81 Matrix of product of linear maps
> Let $T\in\Lin(U,V)$, $S\in\Lin(V,W)$ with bases $u_1,\dots,u_m$ of $U$, $v_1,\dots,v_n$ of $V$, $w_1,\dots,w_p$ of $W$. Then
> $$
> \mathcal{M}\big(ST,(u),(w)\big)=\mathcal{M}\big(S,(v),(w)\big)\,\mathcal{M}\big(T,(u),(v)\big).
> $$

^ladr-3-81

> [!remark] Reading $\mathcal{M}(I,(u),(v))$
> Its column $k$ holds the coordinates of $u_k$ in the basis $v_1,\dots,v_n$: it converts $u$-coordinates into $v$-coordinates.

> [!proof]+
> This is [[§9 Matrices#^ladr-3-43|Matrix of product of linear maps (LADR 3.43)]] with the bases written out.

*Uses:* [[§9 Matrices#^ladr-3-43|3.43]]

> [!remark]- Connections
> - Used in [[§10 Invertibility and Isomorphisms#^ladr-3-82|Matrix of identity operator with respect to two bases]] and [[§10 Invertibility and Isomorphisms#^ladr-3-84|Change-of-basis formula (LADR 3.84)]].

> [!theorem] 3.82 Matrix of identity operator with respect to two bases
> If $u_1,\dots,u_n$ and $v_1,\dots,v_n$ are bases of $V$, then $\mathcal{M}(I,(u),(v))$ and $\mathcal{M}(I,(v),(u))$ are invertible and inverse to each other.

^ladr-3-82

> [!proof]+
> Apply [[§10 Invertibility and Isomorphisms#^ladr-3-81|Matrix of product of linear maps (LADR 3.81)]] with $S=T=I$ and $w=u$:
> $$
> I=\mathcal{M}(I,(v),(u))\,\mathcal{M}(I,(u),(v)).
> $$
> Swapping the roles of $u$ and $v$ gives the product in the other order.

*Uses:* [[§10 Invertibility and Isomorphisms#^ladr-3-81|3.81]]

> [!remark]- Connections
> - The change-of-basis matrix $C$ in [[§10 Invertibility and Isomorphisms#^ladr-3-84|Change-of-basis formula (LADR 3.84)]].

> [!example] 3.83 Matrix of identity on F (p. 92)
> Bases $u=((4,2),(5,3))$ and $e=((1,0),(0,1))$ of $\F^2$. Since $(4,2)=4e_1+2e_2$ and $(5,3)=5e_1+3e_2$,
> $$
> \mathcal{M}\big(I,(u),(e)\big)=\begin{pmatrix}4&5\\2&3\end{pmatrix},\qquad
> \mathcal{M}\big(I,(e),(u)\big)=\begin{pmatrix}4&5\\2&3\end{pmatrix}^{-1}=\begin{pmatrix}\tfrac32&-\tfrac52\\-1&2\end{pmatrix}
> $$
> by [[§10 Invertibility and Isomorphisms#^ladr-3-82|3.82]] (check: the product is $I$). The second matrix converts standard coordinates into $u$-coordinates.

^ladr-3-83

> [!theorem] 3.84 Change-of-basis formula
> Let $T\in\Lin(V)$ and let $u_1,\dots,u_n$, $v_1,\dots,v_n$ be bases of $V$. With
> $$
> A=\mathcal{M}(T,(u)),\quad B=\mathcal{M}(T,(v)),\quad C=\mathcal{M}(I,(u),(v)),
> $$
> we have $A=C^{-1}BC$.

^ladr-3-84

> [!remark] Reading it right to left
> $C$ converts $u$-coordinates to $v$-coordinates, $B$ applies $T$ in $v$-coordinates, $C^{-1}$ converts back.

> [!proof]+
> By [[§10 Invertibility and Isomorphisms#^ladr-3-81|Matrix of product of linear maps (LADR 3.81)]] (with $S=I$, target basis $u$) and [[§10 Invertibility and Isomorphisms#^ladr-3-82|Matrix of identity operator with respect to two bases]]: $A=C^{-1}\,\mathcal{M}(T,(u),(v))$. By [[§10 Invertibility and Isomorphisms#^ladr-3-81|Matrix of product of linear maps (LADR 3.81)]] again (with $T$ replaced by $I$ and $S$ by $T$): $\mathcal{M}(T,(u),(v))=BC$. Substitute.

*Uses:* [[§10 Invertibility and Isomorphisms#^ladr-3-81|3.81]], [[§10 Invertibility and Isomorphisms#^ladr-3-82|3.82]]

> [!remark]- Connections
> - Similar matrices describe the same operator; similarity invariants: [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-50|Trace of matrix of operator does not depend on basis]], [[§34 Determinants#^ladr-9-52|Determinant is a similarity invariant]].
> - Physics: with orthonormal bases $C$ is unitary and this is the familiar $A=U^\dagger BU$ change of representation.
> - Bilinear-form version (different rule, $C^tBC$): [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-7|Change-of-basis formula (LADR 9.7)]].

%% ex:3.84-diagram %%
> [!example] Reading the change-of-basis formula as a diagram
> Both paths from the top-left corner to the top-right give $A$: apply $T$ in $u$-coordinates directly, or convert to $v$-coordinates ($C$), apply $T$ there ($B$), and convert back ($C^{-1}$). That is $A=C^{-1}BC$.
>
> ![[ladr-3.84-change-of-basis.svg|520]]
>
> With the bases of [[§10 Invertibility and Isomorphisms#^ladr-3-83|3.83]]: $C=\mathcal{M}(I,(u),(e))$ turns $u$-coordinates into standard ones, so for $T$ with standard matrix $B$, the matrix in the basis $(4,2),(5,3)$ is $C^{-1}BC$.

> [!theorem] 3.86 Matrix of inverse equals inverse of matrix
> If $v_1,\dots,v_n$ is a basis of $V$ and $T\in\Lin(V)$ is invertible, then $\mathcal{M}(T^{-1})=\mathcal{M}(T)^{-1}$ (all with respect to $v_1,\dots,v_n$).

^ladr-3-86

> [!proof]+
> *(Filled in; left as an exercise in Axler.)* By [[§9 Matrices#^ladr-3-43|Matrix of product of linear maps (LADR 3.43)]], $\mathcal{M}(T^{-1})\mathcal{M}(T)=\mathcal{M}(T^{-1}T)=\mathcal{M}(I)=I$, and likewise $\mathcal{M}(T)\mathcal{M}(T^{-1})=I$. So $\mathcal{M}(T^{-1})$ is the inverse of $\mathcal{M}(T)$ ([[§10 Invertibility and Isomorphisms#^ladr-3-80|Invertible, inverse, A⁻¹]]).

*Uses:* [[§9 Matrices#^ladr-3-43|3.43]], [[§10 Invertibility and Isomorphisms#^ladr-3-80|3.80]]

> [!remark]- Connections
> - So $T$ is invertible iff $\mathcal{M}(T)$ is (the converse via [[§10 Invertibility and Isomorphisms#^ladr-3-72|Dim L(V, W) = (dim V)(dim W)]]: an inverse matrix is the matrix of some map).
