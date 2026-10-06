---
type: section
subject: "[[Linear Algebra]]"
chapter: 7
section: 22
aliases: ["LADR 7A", "7A Self-Adjoint and Normal Operators"]
tags: [linear-algebra]
---
← [[§21 Orthogonal Complements and Minimization Problems]] · ↑ [[· 7 Operators on Inner Product Spaces]] · [[§23 Spectral Theorem]] →

> [!remark] Remark: Standing assumptions for Chapter 7
> Throughout Chapter 7, $V$ and $W$ are nonzero finite-dimensional inner product spaces over $\F$ ($\F$ is $\R$ or $\C$). These are Axler's standing assumptions for the chapter; the chapter's statements use them without repeating them.

> [!definition] Definition 7.1: Adjoint, T∗
> For $T\in\Lin(V,W)$ (finite-dimensional inner product spaces), the *adjoint* $T^{\ast}:W\to V$ is defined by
> $$
> \langle Tv,w\rangle=\langle v,T^*w\rangle\qquad\text{for all }v\in V,\ w\in W .
> $$
> Well defined: for fixed $w$, $v\mapsto\langle Tv,w\rangle$ is a linear functional on $V$, so by [[Riesz representation theorem|6.42]] it is $\langle\cdot,u\rangle$ for a unique $u$; call it $T^*w$.

^ladr-7-1

> [!remark] Remark: How to compute
> Start from $\langle Tv,w\rangle$ and rewrite it until $v$ stands alone in the first slot; what sits in the second slot is $T^*w$ ([[§22 Self-Adjoint and Normal Operators#^ladr-7-2|7.2]], [[§22 Self-Adjoint and Normal Operators#^ladr-7-3|7.3]]). Not related to the 'classical adjoint' (adjugate, [[§22 Cramer’s Rule, Volume, and Linear Transformations#^def-22-2|235 Def. §22.2]]) of a matrix.

> [!remark]- Connections
> - Physics: the Hermitian conjugate $A^\dagger$, $\langle\phi|A\psi\rangle=\langle A^\dagger\phi|\psi\rangle$. Dual-space analogue: [[§12 Duality#^ladr-3-118|3.118]] ($T'$ acts on $W'$; Riesz turns $T'$ into $T^*$).
> - Matrix version on $\mathbb{C}^n$: BDP's adjoint $\mathbf{A}^* = \overline{\mathbf{A}}^T$, [[§28 Matrices#^def-28-1|331 Def. §28.1]], which satisfies $(\mathbf{A}\mathbf{x}, \mathbf{y}) = (\mathbf{x}, \mathbf{A}^*\mathbf{y})$ (proof of [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-5|331 Thm. §29.5]]).

> [!example] Example 7.2: Adjoint of a linear map from R³ to R² (p. 228)
> $T(x_1,x_2,x_3)=(x_2+3x_3,\ 2x_1)$ from $\R^3$ to $\R^2$:
> $$
> \langle T(x_1,x_2,x_3),(y_1,y_2)\rangle=x_2y_1+3x_3y_1+2x_1y_2=\langle(x_1,x_2,x_3),(2y_2,y_1,3y_1)\rangle,
> $$
> so $T^*(y_1,y_2)=(2y_2,y_1,3y_1)$. In matrices: $\begin{pmatrix}0&1&3\\2&0&0\end{pmatrix}^t$, as [[§22 Self-Adjoint and Normal Operators#^ladr-7-9|7.9]] predicts.

^ladr-7-2

> [!example] Example 7.3: Adjoint of a linear map with range of dimension at most 1 (p. 229)
> For fixed $u\in V$, $x\in W$, let $Tv=\langle v,u\rangle x$ (rank $\le1$). Then
> $$
> \langle Tv,w\rangle=\langle v,u\rangle\langle x,w\rangle=\big\langle v,\overline{\langle x,w\rangle}u\big\rangle=\langle v,\langle w,x\rangle u\rangle ,
> $$
> so $T^*w=\langle w,x\rangle u$. In Dirac notation $T=|x\rangle\langle u|$ and $T^\dagger=|u\rangle\langle x|$.

^ladr-7-3

> [!theorem] Theorem 7.4: Adjoint of a linear map is a linear map
> If $T\in\Lin(V,W)$, then $T^*\in\Lin(W,V)$.

^ladr-7-4

> [!proof]+ Proof
> For $v\in V$, $w_1,w_2\in W$: $\langle Tv,w_1+w_2\rangle=\langle v,T^*w_1\rangle+\langle v,T^*w_2\rangle=\langle v,T^*w_1+T^*w_2\rangle$, so $T^*(w_1+w_2)=T^*w_1+T^*w_2$ by uniqueness in [[Riesz representation theorem|6.42]]. For $\lambda\in\F$: $\langle Tv,\lambda w\rangle=\bar\lambda\langle Tv,w\rangle=\bar\lambda\langle v,T^*w\rangle=\langle v,\lambda T^*w\rangle$ ([[§19 Inner Products and Norms#^ladr-6-6|6.6]]), so $T^*(\lambda w)=\lambda T^*w$.

*Uses:* [[Riesz representation theorem|6.42]], [[§19 Inner Products and Norms#^ladr-6-6|6.6]]

> [!theorem] Theorem 7.5: Properties of the adjoint
> For $T\in\Lin(V,W)$:
> - (a) $(S+T)^*=S^*+T^*$ for $S\in\Lin(V,W)$;
> - (b) $(\lambda T)^*=\bar\lambda T^*$;
> - (c) $(T^*)^*=T$;
> - (d) $(ST)^*=T^*S^*$ for $S\in\Lin(W,U)$;
> - (e) $I^*=I$;
> - (f) if $T$ is invertible, so is $T^*$, and $(T^*)^{-1}=(T^{-1})^*$.

^ladr-7-5

> [!remark] Remark: Conjugate-linear
> Over $\C$, $T\mapsto T^*$ is not linear because of (b); over $\R$ it is.

> [!proof]+ Proof
> Each follows by moving operators across the inner product. (a) $\langle(S+T)v,w\rangle=\langle v,S^*w+T^*w\rangle$. (b) $\langle\lambda Tv,w\rangle=\lambda\langle v,T^*w\rangle=\langle v,\bar\lambda T^*w\rangle$. (c) $\langle T^*w,v\rangle=\overline{\langle v,T^*w\rangle}=\overline{\langle Tv,w\rangle}=\langle w,Tv\rangle$. (d) $\langle STv,u\rangle=\langle Tv,S^*u\rangle=\langle v,T^*S^*u\rangle$. (e) clear. (f) take adjoints of $T^{-1}T=I$ and $TT^{-1}=I$ using (d), (e).

> [!remark]- Connections
> - (d) is the reversal familiar from $(AB)^t=B^tA^t$ ([[§9 Matrices#^ladr-3-55|3.55]]) and $(ST)'=T'S'$ ([[§12 Duality#^ladr-3-120|3.120]]).

> [!theorem] Theorem 7.6: Null space and range of T∗
> For $T\in\Lin(V,W)$:
> - (a) $\nullsp T^*=(\range T)^\perp$;
> - (b) $\range T^*=(\nullsp T)^\perp$;
> - (c) $\nullsp T=(\range T^*)^\perp$;
> - (d) $\range T=(\nullsp T^*)^\perp$.

^ladr-7-6

> [!remark] Remark: Linear equations
> (d) says $Tx=b$ is solvable iff $b\perp\nullsp T^*$: the 'Fredholm alternative' in finite dimensions.

> [!proof]+ Proof
> (a) $w\in\nullsp T^*\iff\langle v,T^*w\rangle=0\ \forall v\iff\langle Tv,w\rangle=0\ \forall v\iff w\in(\range T)^\perp$. Taking complements of (a) gives (d) ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-52|6.52]]); replacing $T$ by $T^*$ in (a) and (d) gives (c) and (b) ([[§22 Self-Adjoint and Normal Operators#^ladr-7-5|7.5]](c)).

*Uses:* [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-52|6.52]], [[§22 Self-Adjoint and Normal Operators#^ladr-7-5|7.5]]

> [!remark]- Connections
> - Annihilator versions: [[§12 Duality#^ladr-3-128|3.128]], [[§12 Duality#^ladr-3-130|3.130]]. Dimension consequence: column rank = row rank again, via [[§26 Singular Value Decomposition#^ladr-7-64|7.64]](d).
> - Computational version: [[§40 Inner Product, Length, and Orthogonality#^thm-40-6|235 Thm. §40.6]] (the matrix case: $(\operatorname{Row}A)^\perp=\operatorname{Nul}A$ and $(\operatorname{Col}A)^\perp=\operatorname{Nul}A^T$).

%% ex:7.6-fig %%
> [!example] Example: The four subspaces, pictured
> Take the rank-one map $Tv=\langle v,u\rangle x$ of [[§22 Self-Adjoint and Normal Operators#^ladr-7-3|7.3]] on $\R^2$, with $T^*w=\langle w,x\rangle u$. In $V$, $\range T^*=\Span(u)$ and $\nullsp T=u^\perp$ are orthogonal complements (b); in $W$, $\range T=\Span(x)$ and $\nullsp T^*=x^\perp$ are (a). $T$ kills the red component of $v$ and sends the blue one onto $Tv\in\range T$.
>
> ![[ladr-7.6-four-subspaces.svg|460]]

> [!definition] Definition 7.7: Conjugate transpose, A∗
> The *conjugate transpose* $A^{\ast}$ of an $m$-by-$n$ matrix $A$ is the $n$-by-$m$ matrix with $(A^{\ast})_{j,k}=\overline{A_{k,j}}$. For real $A$, $A^{\ast}=A^t$.

^ladr-7-7

> [!remark]- Connections
> - Computational version: BDP calls $\mathbf{A}^*$ the adjoint of $\mathbf{A}$, [[§28 Matrices#^def-28-1|331 Def. §28.1]] (with a worked example).

> [!example] Example 7.8: Conjugate transpose of a 2-by-3 matrix (p. 231)
> $$
> \begin{pmatrix}2&3+4i&7\\6&5&8i\end{pmatrix}^*=\begin{pmatrix}2&6\\3-4i&5\\7&-8i\end{pmatrix}.
> $$
> For real matrices $A^*=A^t$.

^ladr-7-8

> [!theorem] Theorem 7.9: Matrix of T∗
> If $e_1,\dots,e_n$ and $f_1,\dots,f_m$ are **orthonormal** bases of $V$ and $W$, then
> $$
> \mathcal{M}\big(T^*,(f),(e)\big)=\mathcal{M}\big(T,(e),(f)\big)^* .
> $$

^ladr-7-9

> [!remark] Remark: Orthonormality is essential
> In a non-orthonormal basis the matrix of $T^*$ is generally not the conjugate transpose.

> [!proof]+ Proof
> By [[§20 Orthonormal Bases#^ladr-6-30|6.30]](a), $Te_k=\sum_j\langle Te_k,f_j\rangle f_j$, so $\mathcal{M}(T)_{j,k}=\langle Te_k,f_j\rangle$. Likewise $\mathcal{M}(T^*)_{j,k}=\langle T^*f_k,e_j\rangle=\overline{\langle e_j,T^*f_k\rangle}=\overline{\langle Te_j,f_k\rangle}=\overline{\mathcal{M}(T)_{k,j}}$.

*Uses:* [[§20 Orthonormal Bases#^ladr-6-30|6.30]]

> [!definition] Definition 7.10: Self-adjoint
> $T\in\Lin(V)$ is *self-adjoint* if $T=T^{\ast}$, i.e. $\langle Tv,w\rangle=\langle v,Tw\rangle$ for all $v,w$. In an orthonormal basis: $\mathcal{M}(T)=\mathcal{M}(T)^{\ast}$ ([[§22 Self-Adjoint and Normal Operators#^ladr-7-9|7.9]]).

^ladr-7-10

> [!remark] Remark: Analogy
> $T^*$ is to operators what $\bar z$ is to numbers; self-adjoint operators are the 'real numbers' ([[§22 Self-Adjoint and Normal Operators#^ladr-7-12|7.12]], [[§22 Self-Adjoint and Normal Operators#^ladr-7-14|7.14]]).

> [!remark]- Connections
> - Physics: Hermitian operators = observables. Structure: [[Real spectral theorem|7.29]], [[Complex spectral theorem|7.31]].
> - The self-adjoint matrices form the real vector space of Hermitian matrices, [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^def-22-2|591 Def. §22.2]], used to show that U(n) is a manifold.
> - Computational version: [[§48★ Diagonalization of Symmetric Matrices#^def-48-1|235 Def. §48.1]] (symmetric matrices: the real self-adjoint case in the standard basis).
> - Infinite-dimensional analogue: the Sturm–Liouville operator is self-adjoint for the weighted inner product, [[§23 Sturm–Liouville Problems#^rem-23-3|341 Remark §23.3]].

> [!example] Example 7.11: Determining whether T is self-adjoint from its matrix (p. 233)
> $\mathcal{M}(T)=\begin{pmatrix}2&c\\3&7\end{pmatrix}$ (standard basis of $\F^2$, orthonormal) has $\mathcal{M}(T^*)=\begin{pmatrix}2&3\\\bar c&7\end{pmatrix}$, so $T$ is self-adjoint iff $c=3$.

^ladr-7-11

> [!theorem] Theorem 7.12: Eigenvalues of self-adjoint operators
> Every eigenvalue of a self-adjoint operator is real.

^ladr-7-12

> [!proof]+ Proof
> If $Tv=\lambda v$, $v\ne0$: $\lambda\|v\|^2=\langle Tv,v\rangle=\langle v,Tv\rangle=\bar\lambda\|v\|^2$, so $\lambda=\bar\lambda$.

> [!remark]- Connections
> - Physics: measured values of an observable are real.
> - Computational version: [[§48★ Diagonalization of Symmetric Matrices#^thm-48-3|235 Thm. §48.3]](a) (a symmetric matrix has $n$ real eigenvalues, counting multiplicities).
> - Matrix version: [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-5|331 Thm. §29.5]] (1), for Hermitian matrices.
> - Infinite-dimensional analogue: the eigenvalues of a regular Sturm–Liouville problem are real, [[§23 Sturm–Liouville Problems#^prop-23-3|341 Prop. §23.3]], by the same computation.

> [!theorem] Theorem 7.13: Tv is orthogonal to v for all v ⟺ T = 0 (assuming F = C)
> On a **complex** inner product space, $\langle Tv,v\rangle=0$ for every $v$ iff $T=0$.

^ladr-7-13

> [!remark] Remark: False over $\R$
> Rotation by $90^\circ$ on $\R^2$ has $Tv\perp v$ for every $v$ but $T\ne0$ (picture in [[§14 Invariant Subspaces#^ladr-5-9|5.9]]). The real version needs self-adjointness: [[§22 Self-Adjoint and Normal Operators#^ladr-7-16|7.16]].

> [!proof]+ Proof
> The polarization identity
> $$
> \langle Tu,w\rangle=\frac{\langle T(u+w),u+w\rangle-\langle T(u-w),u-w\rangle}{4}+\frac{\langle T(u+iw),u+iw\rangle-\langle T(u-iw),u-iw\rangle}{4}\,i
> $$
> (check by expanding) expresses $\langle Tu,w\rangle$ through values $\langle Tv,v\rangle$. If all of these vanish, $\langle Tu,w\rangle=0$ for all $u,w$; take $w=Tu$.

> [!theorem] Theorem 7.14: ⟨Tv, v⟩ is real for all v ⟺ T is self-adjoint (assuming F = C)
> On a complex inner product space, $T$ is self-adjoint iff $\langle Tv,v\rangle\in\R$ for every $v$.

^ladr-7-14

> [!proof]+ Proof
> $\langle T^*v,v\rangle=\langle v,Tv\rangle=\overline{\langle Tv,v\rangle}$. So $T=T^*\iff\langle(T-T^*)v,v\rangle=0\ \forall v$ ([[§22 Self-Adjoint and Normal Operators#^ladr-7-13|7.13]]) $\iff\langle Tv,v\rangle-\overline{\langle Tv,v\rangle}=0\ \forall v\iff\langle Tv,v\rangle\in\R\ \forall v$.

*Uses:* [[§22 Self-Adjoint and Normal Operators#^ladr-7-13|7.13]]

> [!remark]- Connections
> - Physics: an operator is Hermitian iff all its expectation values are real.

> [!theorem] Theorem 7.16: T self-adjoint and ⟨Tv, v⟩ = 0 for all v ⟺ T = 0
> If $T$ is self-adjoint, then $\langle Tv,v\rangle=0$ for every $v$ iff $T=0$.

^ladr-7-16

> [!proof]+ Proof
> Over $\C$ this is [[§22 Self-Adjoint and Normal Operators#^ladr-7-13|7.13]]. Over $\R$, self-adjointness gives $\langle Tw,u\rangle=\langle Tu,w\rangle$, so
> $$
> \langle Tu,w\rangle=\frac{\langle T(u+w),u+w\rangle-\langle T(u-w),u-w\rangle}{4}.
> $$
> If all $\langle Tv,v\rangle=0$, then $\langle Tu,w\rangle=0$ for all $u,w$; take $w=Tu$.

*Uses:* [[§22 Self-Adjoint and Normal Operators#^ladr-7-13|7.13]]

> [!definition] Definition 7.18: Normal
> $T\in\Lin(V)$ is *normal* if $TT^{\ast}=T^{\ast}T$. Self-adjoint operators are normal.

^ladr-7-18

> [!remark]- Connections
> - Characterized by $\|Tv\|=\|T^*v\|$ ([[§22 Self-Adjoint and Normal Operators#^ladr-7-20|7.20]]). Over $\C$: exactly the orthonormally diagonalizable operators ([[Complex spectral theorem|7.31]]). Unitary operators are normal.

> [!example] Example 7.19: An operator that is normal but not self-adjoint (p. 235)
> $\mathcal{M}(T)=\begin{pmatrix}2&-3\\3&2\end{pmatrix}$, i.e. $T(w,z)=(2w-3z,\ 3w+2z)$. Not self-adjoint ($3\ne\overline{-3}$), but
> $$
> TT^*=\begin{pmatrix}2&-3\\3&2\end{pmatrix}\begin{pmatrix}2&3\\-3&2\end{pmatrix}=\begin{pmatrix}13&0\\0&13\end{pmatrix}=T^*T ,
> $$
> so $T$ is normal. (It is $\sqrt{13}$ times a rotation.)

^ladr-7-19

%% ex:7.19-normal %%
> [!theorem] Theorem 7.20: T is normal if and only if Tv and T∗v have the same norm
> $T\in\Lin(V)$ is normal $\iff\|Tv\|=\|T^*v\|$ for every $v\in V$.

^ladr-7-20

> [!proof]+ Proof
> $T^*T-TT^*$ is self-adjoint, so by [[§22 Self-Adjoint and Normal Operators#^ladr-7-16|7.16]] it is $0$ iff $\langle(T^*T-TT^*)v,v\rangle=0$ for all $v$, i.e. iff $\langle Tv,Tv\rangle=\langle T^*v,T^*v\rangle$ for all $v$.

*Uses:* [[§22 Self-Adjoint and Normal Operators#^ladr-7-16|7.16]]

> [!theorem] Theorem 7.21: Range, null space, and eigenvectors of a normal operator
> If $T\in\Lin(V)$ is normal, then
> - (a) $\nullsp T=\nullsp T^*$;
> - (b) $\range T=\range T^*$;
> - (c) $V=\nullsp T\oplus\range T$;
> - (d) $T-\lambda I$ is normal for every $\lambda\in\F$;
> - (e) $Tv=\lambda v\iff T^*v=\bar\lambda v$.

^ladr-7-21

> [!remark] Remark: (c) fails without normality
> For $T=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $\nullsp T=\range T=\Span(e_1)$.

> [!proof]+ Proof
> Recall [[§22 Self-Adjoint and Normal Operators#^ladr-7-20|7.20]]: $T$ is normal $\iff\|Tv\|=\|T^*v\|$ for all $v$.
>
> (a) $Tv=0\iff\|Tv\|=0\iff\|T^*v\|=0$. (b) $\range T=(\nullsp T^*)^\perp=(\nullsp T)^\perp=\range T^*$ by [[§22 Self-Adjoint and Normal Operators#^ladr-7-6|7.6]]. (c) $V=\nullsp T\oplus(\nullsp T)^\perp=\nullsp T\oplus\range T^*=\nullsp T\oplus\range T$ ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-49|6.49]], [[§22 Self-Adjoint and Normal Operators#^ladr-7-6|7.6]]). (d) Expanding, $(T-\lambda I)(T-\lambda I)^*=TT^*-\bar\lambda T-\lambda T^*+|\lambda|^2I$, symmetric under $TT^*\leftrightarrow T^*T$. (e) By (d) and 7.20, $\|(T-\lambda I)v\|=\|(T^*-\bar\lambda I)v\|$.

*Uses:* [[§22 Self-Adjoint and Normal Operators#^ladr-7-20|7.20]], [[§22 Self-Adjoint and Normal Operators#^ladr-7-6|7.6]], [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-49|6.49]]

> [!theorem] Theorem 7.22: Orthogonal eigenvectors for normal operators
> For normal $T$, eigenvectors for distinct eigenvalues are orthogonal.

^ladr-7-22

> [!proof]+ Proof
> Let $Tu=\alpha u$, $Tv=\beta v$, $\alpha\ne\beta$. Then $T^*v=\bar\beta v$ ([[§22 Self-Adjoint and Normal Operators#^ladr-7-21|7.21]](e)), so
> $$
> (\alpha-\beta)\langle u,v\rangle=\langle Tu,v\rangle-\langle u,T^*v\rangle=0 .
> $$

*Uses:* [[§22 Self-Adjoint and Normal Operators#^ladr-7-21|7.21]]

> [!remark]- Connections
> - Physics: eigenstates of an observable with different eigenvalues are orthogonal. Compare [[Linearly independent eigenvectors|5.11]] (only independent, for general operators).
> - Computational version: [[§48★ Diagonalization of Symmetric Matrices#^thm-48-1|235 Thm. §48.1]] (for symmetric matrices).
> - Matrix version: [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-5|331 Thm. §29.5]] (3), for Hermitian matrices.
> - Infinite-dimensional analogue: eigenfunctions of a Sturm–Liouville problem for different eigenvalues are orthogonal, [[§23 Sturm–Liouville Problems#^thm-23-2|341 Thm. §23.2]], and so are those of the Laplacian on a plane region, [[§44★ Problems in Polar Coordinates#^thm-44-3|341 Thm. §44.3]]; concrete cases include the Legendre polynomials, [[§49★ Spherical Coordinates; Legendre Polynomials#^prop-49-5|341 Prop. §49.5]].

> [!theorem] Theorem 7.23: T is normal ⟺ the real and imaginary parts of T commute
> Let $\F=\C$. Then $T\in\Lin(V)$ is normal iff $T=A+iB$ for commuting self-adjoint $A,B$.

^ladr-7-23

> [!remark] Remark: Informal title
> Normal iff the 'real and imaginary parts' of $T$ commute, just as $z=a+ib$ always does for numbers.

> [!proof]+ Proof
> Set $A=\frac{T+T^*}2$, $B=\frac{T-T^*}{2i}$: both self-adjoint, $T=A+iB$, and a direct computation gives
> $$
> AB-BA=\frac{T^*T-TT^*}{2i}.
> $$
> So $T$ normal $\Rightarrow AB=BA$. Conversely, if $T=A+iB$ with such $A,B$, then $T^*=A-iB$, so $A,B$ are the formulas above, and $AB=BA$ gives $T^*T=TT^*$.

