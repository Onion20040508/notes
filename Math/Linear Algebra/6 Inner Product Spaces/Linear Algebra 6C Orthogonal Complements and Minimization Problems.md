---
type: section
subject: "[[Linear Algebra]]"
chapter: 6
section: "6C"
tags: [linear-algebra]
---
← [[Linear Algebra 6B Orthonormal Bases]] · ↑ [[Linear Algebra — 6 Inner Product Spaces]] · [[Linear Algebra 7A Self-Adjoint and Normal Operators]] →

> [!definition] 6.46 Orthogonal complement, U⟂
> For a subset $U\subseteq V$, the *orthogonal complement* is
> $$
> U^\perp=\{v\in V:\langle u,v\rangle=0\text{ for every }u\in U\}.
> $$
> It depends on the ambient $V$ as well as on $U$.

^ladr-6-46

> [!remark]- Connections
> - Basic properties [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-48|6.48]]; direct sum [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-49|6.49]]. Compare the annihilator $U^0\subseteq V'$ ([[Linear Algebra 3F Duality#^ladr-3-121|3.121]]): Riesz ([[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-58|6.58]]) identifies $U^\perp$ with $U^0$.

> [!example] 6.47 Orthogonal complements (p. 211)
> - In $\R^3$: $\{(2,3,5)\}^\perp$ is the plane $2x+3y+5z=0$, and the complement of that plane is the line $\{t(2,3,5)\}$.
> - In general in $\R^3$: a plane through $0$ and the perpendicular line through $0$ are each other's complements.
> - In $\F^5$: $\{(a,b,0,0,0)\}^\perp=\{(0,0,x,y,z)\}$.
> - If $e_1,\dots,e_m,f_1,\dots,f_n$ is an orthonormal basis of $V$, then $\Span(e_1,\dots,e_m)^\perp=\Span(f_1,\dots,f_n)$.

^ladr-6-47

> [!theorem] 6.48 Properties of orthogonal complement
> - (a) For any subset $U$, $U^\perp$ is a subspace of $V$.
> - (b) $\{0\}^\perp=V$.
> - (c) $V^\perp=\{0\}$.
> - (d) $U\cap U^\perp\subseteq\{0\}$.
> - (e) If $G\subseteq H$ then $H^\perp\subseteq G^\perp$.

^ladr-6-48

> [!proof]+
> (a) $0\in U^\perp$, and if $v,w\in U^\perp$, $\lambda\in\F$, $u\in U$: $\langle u,v+w\rangle=0+0$ and $\langle u,\lambda v\rangle=\bar\lambda\cdot0=0$ ([[Linear Algebra 6A Inner Products and Norms#^ladr-6-6|6.6]]). (b) $\langle0,v\rangle=0$. (c) $v\in V^\perp$ gives $\langle v,v\rangle=0$. (d) $u\in U\cap U^\perp$ gives $\langle u,u\rangle=0$. (e) orthogonal to all of $H$ implies orthogonal to all of $G$.

*Uses:* [[Linear Algebra 6A Inner Products and Norms#^ladr-6-6|6.6]]

> [!theorem] 6.49 Direct sum of a subspace and its orthogonal complement
> If $U$ is a finite-dimensional subspace of $V$, then
> $$
> V=U\oplus U^\perp .
> $$

^ladr-6-49

> [!remark] $V$ need not be finite-dimensional
> Only $U$ must be. Without that, it can fail: in the space of continuous functions (or $\ell^2$-type sequence spaces) a dense subspace $U\ne V$ can have $U^\perp=\{0\}$.

> [!proof]+
> Let $e_1,\dots,e_m$ be an orthonormal basis of $U$ ([[Linear Algebra 6B Orthonormal Bases#^ladr-6-35|6.35]]). For $v\in V$ write
> $$
> v=\underbrace{\langle v,e_1\rangle e_1+\dots+\langle v,e_m\rangle e_m}_{u}+\underbrace{v-u}_{w}.
> $$
> $u\in U$, and $\langle w,e_k\rangle=\langle v,e_k\rangle-\langle v,e_k\rangle=0$ for each $k$, so $w\perp\Span(e_1,\dots,e_m)=U$. Thus $V=U+U^\perp$, and $U\cap U^\perp=\{0\}$ ([[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-48|6.48]](d)), so the sum is direct ([[Linear Algebra 1C Subspaces#^ladr-1-46|1.46]]).

*Uses:* [[Linear Algebra 6B Orthonormal Bases#^ladr-6-35|6.35]], [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-48|6.48]], [[Linear Algebra 1C Subspaces#^ladr-1-46|1.46]]

> [!remark]- Connections
> - Defines $P_U$ ([[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-55|6.55]]); dimensions [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-51|6.51]]; double complement [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-52|6.52]].

> [!theorem] 6.51 Dimension of orthogonal complement
> If $V$ is finite-dimensional and $U$ a subspace, then $\dim U^\perp=\dim V-\dim U$.

^ladr-6-51

> [!proof]+
> [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-49|6.49]] and [[Linear Algebra 3E Products and Quotients of Vector Spaces#^ladr-3-94|3.94]].

*Uses:* [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-49|6.49]], [[Linear Algebra 3E Products and Quotients of Vector Spaces#^ladr-3-94|3.94]]

> [!remark]- Connections
> - Parallel to $\dim U^0=\dim V-\dim U$ ([[Linear Algebra 3F Duality#^ladr-3-125|3.125]]).

> [!theorem] 6.52 Orthogonal complement of the orthogonal complement
> If $U$ is a finite-dimensional subspace of $V$, then $U=(U^\perp)^\perp$.

^ladr-6-52

> [!proof]+
> $U\subseteq(U^\perp)^\perp$: each $u\in U$ is orthogonal to every vector of $U^\perp$.
>
> Conversely let $v\in(U^\perp)^\perp$ and write $v=u+w$, $u\in U$, $w\in U^\perp$ ([[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-49|6.49]]). Then $v-u=w\in U^\perp$, and also $v-u\in(U^\perp)^\perp$ (both $v$ and $u$ are). So $v-u\in U^\perp\cap(U^\perp)^\perp=\{0\}$ ([[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-48|6.48]](d)), i.e. $v=u\in U$.

*Uses:* [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-49|6.49]], [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-48|6.48]]

> [!theorem] 6.54 U⟂ = {0} ⟺ U = V (for U a finite-dimensional subspace of V)
> For a finite-dimensional subspace $U$ of $V$: $U^\perp=\{0\}\iff U=V$.

^ladr-6-54

> [!remark] Use
> To show a subspace is everything, show that only $0$ is orthogonal to it. This is how completeness of a system of functions is proved.

> [!proof]+
> If $U^\perp=\{0\}$ then $U=(U^\perp)^\perp=\{0\}^\perp=V$ ([[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-52|6.52]], [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-48|6.48]](b)). If $U=V$ then $U^\perp=V^\perp=\{0\}$ ([[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-48|6.48]](c)).

*Uses:* [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-52|6.52]], [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-48|6.48]]

> [!definition] 6.55 Orthogonal projection, PU
> For a finite-dimensional subspace $U$ of $V$, the *orthogonal projection* $P_U\in\Lin(V)$ is defined by: write $v=u+w$ with $u\in U$, $w\in U^\perp$ ([[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-49|6.49]]), and set $P_Uv=u$.

^ladr-6-55

> [!remark]- Connections
> - Properties [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-57|6.57]]; closest point [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-61|6.61]]. Physics: $P_U=\sum_k|e_k\rangle\langle e_k|$ over an orthonormal basis of $U$, the projector of a measurement outcome.

> [!example] 6.56 Orthogonal projection onto one-dimensional subspace (p. 214)
> For $U=\Span(u)$, $u\ne0$:
> $$
> P_Uv=\frac{\langle v,u\rangle}{\|u\|^2}\,u ,
> $$
> which is [[Linear Algebra 6A Inner Products and Norms#^ladr-6-13|6.13]]. Checks: $P_Uu=u$ and $P_Uv=0$ for $v\perp u$. For a unit vector $u$ this is $P_U=|u\rangle\langle u|$ in Dirac notation.

^ladr-6-56

> [!theorem] 6.57 Properties of orthogonal projection PU
> For a finite-dimensional subspace $U$ of $V$:
> - (a) $P_U\in\Lin(V)$;
> - (b) $P_Uu=u$ for $u\in U$;
> - (c) $P_Uw=0$ for $w\in U^\perp$;
> - (d) $\range P_U=U$;
> - (e) $\nullsp P_U=U^\perp$;
> - (f) $v-P_Uv\in U^\perp$;
> - (g) $P_U^2=P_U$;
> - (h) $\|P_Uv\|\le\|v\|$;
> - (i) for an orthonormal basis $e_1,\dots,e_m$ of $U$, $P_Uv=\langle v,e_1\rangle e_1+\dots+\langle v,e_m\rangle e_m$.

^ladr-6-57

> [!proof]+
> Throughout write $v=u+w$, $u\in U$, $w\in U^\perp$ (unique by [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-49|6.49]]).
>
> (a) If $v_j=u_j+w_j$, then $v_1+v_2=(u_1+u_2)+(w_1+w_2)$ and $\lambda v=\lambda u+\lambda w$ are the decompositions, so $P_U$ is additive and homogeneous. (b) $u=u+0$. (c) $w=0+w$. (d) $\range P_U\subseteq U$ by definition and $\supseteq$ by (b). (e) $\supseteq$ by (c); if $P_Uv=0$ the decomposition is $v=0+v$, so $v\in U^\perp$. (f) $v-P_Uv=w$. (g) $P_U(P_Uv)=P_Uu=u$. (h) $\|P_Uv\|^2=\|u\|^2\le\|u\|^2+\|w\|^2=\|v\|^2$ ([[Linear Algebra 6A Inner Products and Norms#^ladr-6-12|6.12]]). (i) is the decomposition in the proof of [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-49|6.49]].

*Uses:* [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-49|6.49]], [[Linear Algebra 6A Inner Products and Norms#^ladr-6-12|6.12]]

> [!remark]- Connections
> - (g)+(e): $P_U$ is an idempotent whose null space is orthogonal to its range; these are exactly the self-adjoint idempotents (Chapter 7).

> [!theorem] 6.58 Riesz representation theorem, revisited
> Let $V$ be finite-dimensional. For $v\in V$ define $\varphi_v\in V'$ by $\varphi_v(u)=\langle u,v\rangle$. Then $v\mapsto\varphi_v$ is a bijection $V\to V'$.

^ladr-6-58

> [!remark] Not linear over $\C$
> $\varphi_{\lambda v}=\bar\lambda\varphi_v$: the map is conjugate-linear. Over $\R$ it is an isomorphism $V\cong V'$ that, unlike [[Linear Algebra 3F Duality#^ladr-3-111|3.111]], needs no basis, only the inner product.

> [!proof]+
> **Injective:** $\varphi_{v_1}=\varphi_{v_2}$ gives $\langle u,v_1-v_2\rangle=0$ for all $u$; take $u=v_1-v_2$.
>
> **Surjective** (a proof without bases). Let $\varphi\in V'$, $\varphi\ne0$ (else $\varphi=\varphi_0$). Then $\nullsp\varphi\ne V$, so $(\nullsp\varphi)^\perp\ne\{0\}$ ([[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-54|6.54]]); pick $w\ne0$ in it and set $v=\dfrac{\overline{\varphi(w)}}{\|w\|^2}w$. Then $v\in(\nullsp\varphi)^\perp$, $v\ne0$, and $\varphi(v)=\dfrac{|\varphi(w)|^2}{\|w\|^2}=\|v\|^2$. For any $u$,
> $$
> u=\Big(u-\frac{\varphi(u)}{\varphi(v)}v\Big)+\frac{\varphi(u)}{\|v\|^2}v ,
> $$
> where the first term is in $\nullsp\varphi$, hence orthogonal to $v$. Taking the inner product with $v$ gives $\langle u,v\rangle=\varphi(u)$.

*Uses:* [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-54|6.54]]

> [!remark]- Connections
> - This proof uses only $V=U\oplus U^\perp$ for $U=\nullsp\varphi$, which is why it generalizes to Hilbert spaces (closed subspaces).

> [!theorem] 6.61 Minimizing distance to a subspace
> Let $U$ be a finite-dimensional subspace of $V$, $v\in V$, $u\in U$. Then
> $$
> \|v-P_Uv\|\le\|v-u\|,
> $$
> with equality iff $u=P_Uv$.

^ladr-6-61

> [!remark] Recipe
> Best approximation from $U$ = orthogonal projection, computed by [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-57|6.57]](i) after Gram–Schmidt. This is least squares, Fourier truncation, and [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-63|6.63]].

> [!proof]+
> $v-P_Uv\in U^\perp$ ([[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-57|6.57]](f)) and $P_Uv-u\in U$, so by [[Linear Algebra 6A Inner Products and Norms#^ladr-6-12|6.12]]
> $$
> \|v-P_Uv\|^2\le\|v-P_Uv\|^2+\|P_Uv-u\|^2=\|(v-P_Uv)+(P_Uv-u)\|^2=\|v-u\|^2 .
> $$
> Equality iff $\|P_Uv-u\|=0$.

*Uses:* [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-57|6.57]], [[Linear Algebra 6A Inner Products and Norms#^ladr-6-12|6.12]]

> [!remark]- Connections
> - Pseudoinverse version for equations $Tx=b$: [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-70|6.70]].

%% ex:6.61-fig %%
> [!example] The closest point, pictured
> $v-P_Uv$ is perpendicular to $U$, and for any other $u\in U$ the distance $\|v-u\|$ is the hypotenuse of a right triangle with leg $\|v-P_Uv\|$.
>
> ![[ladr-6.61-closest-point.svg|380]]

> [!example] 6.63 Using linear algebra to approximate the sine function (p. 218)
> Best approximation of $\sin x$ on $[-\pi,\pi]$ by a polynomial of degree $\le5$, in the sense of minimizing $\int_{-\pi}^\pi|\sin x-u(x)|^2dx$.
>
> In $C[-\pi,\pi]$ with $\langle f,g\rangle=\int_{-\pi}^\pi fg$, let $U=\Poly_5(\R)$. By [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-61|6.61]] the answer is $P_U\sin$: Gram–Schmidt on $1,x,\dots,x^5$, then [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-57|6.57]](i). The result (recomputed here by solving the normal equations) is
> $$
> u(x)=0.987862\,x-0.155271\,x^3+0.00564312\,x^5 .
> $$
> Compare the Taylor polynomial $x-\frac{x^3}{6}+\frac{x^5}{120}=x-0.166667\,x^3+0.008333\,x^5$: Taylor is perfect near $0$ and poor near $\pm\pi$, while $u$ spreads the error over the whole interval. On this scale $u$ is indistinguishable from $\sin$; Taylor visibly misses at the ends:
>
> ![[ladr-6.63-sine.svg|460]]

^ladr-6-63

> [!theorem] 6.67 Restriction of a linear map to obtain a one-to-one and onto map
> Let $V$ be finite-dimensional and $T\in\Lin(V,W)$. Then $T|_{(\nullsp T)^\perp}$ is a bijection of $(\nullsp T)^\perp$ onto $\range T$.

^ladr-6-67

> [!proof]+
> **Injective:** if $v\in(\nullsp T)^\perp$ and $Tv=0$, then $v\in\nullsp T\cap(\nullsp T)^\perp=\{0\}$.
>
> **Onto $\range T$:** for $w=Tv$, write $v=u+x$ with $u\in\nullsp T$, $x\in(\nullsp T)^\perp$ ([[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-49|6.49]]); then $Tx=Tv-Tu=w$.

*Uses:* [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-49|6.49]]

> [!remark]- Connections
> - Inner-product version of [[First isomorphism theorem|3.107]]: the quotient $V/\nullsp T$ is replaced by the concrete subspace $(\nullsp T)^\perp$. Used to define [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-68|6.68]].

> [!definition] 6.68 Pseudoinverse, T†
> For $V$ finite-dimensional and $T\in\Lin(V,W)$, the *pseudoinverse* $T^\dagger\in\Lin(W,V)$ is
> $$
> T^\dagger w=\big(T|_{(\nullsp T)^\perp}\big)^{-1}P_{\range T}\,w .
> $$
> So $T^\dagger w=0$ for $w\in(\range T)^\perp$, and for $w\in\range T$, $T^\dagger w$ is the unique $v\in(\nullsp T)^\perp$ with $Tv=w$.

^ladr-6-68

> [!remark] Also called
> the Moore–Penrose inverse. Formula via SVD: [[Linear Algebra 7E Singular Value Decomposition#^ladr-7-75|Singular value decomposition of adjoint and pseudoinverse]].

> [!theorem] 6.69 Algebraic properties of the pseudoinverse
> Let $V$ be finite-dimensional and $T\in\Lin(V,W)$.
> - (a) If $T$ is invertible, $T^\dagger=T^{-1}$.
> - (b) $TT^\dagger=P_{\range T}$.
> - (c) $T^\dagger T=P_{(\nullsp T)^\perp}$.

^ladr-6-69

> [!remark] One-sided inverses
> If $T$ is surjective, $TT^\dagger=I_W$; if injective, $T^\dagger T=I_V$.

> [!proof]+
> (a) $(\nullsp T)^\perp=V$ and $P_{\range T}=I$.
>
> (b) For $w\in\range T$, $TT^\dagger w=w$; for $w\in(\range T)^\perp$, $T^\dagger w=0$. So $TT^\dagger$ and $P_{\range T}$ agree on both summands of $W=\range T\oplus(\range T)^\perp$ ([[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-49|6.49]]).
>
> (c) For $v\in(\nullsp T)^\perp$, $T^\dagger Tv=v$; for $v\in\nullsp T$, $T^\dagger Tv=0$. Again they agree on both summands.

*Uses:* [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-49|6.49]]

> [!theorem] 6.70 Pseudoinverse provides best approximate solution or best solution
> Let $V$ be finite-dimensional, $T\in\Lin(V,W)$, $b\in W$.
> - (a) For every $x\in V$, $\|T(T^\dagger b)-b\|\le\|Tx-b\|$, with equality iff $x\in T^\dagger b+\nullsp T$.
> - (b) If $x\in T^\dagger b+\nullsp T$, then $\|T^\dagger b\|\le\|x\|$, with equality iff $x=T^\dagger b$.

^ladr-6-70

> [!remark] In words
> $T^\dagger b$ is the least-squares solution of $Tx=b$, and among all least-squares solutions it has the smallest norm.

> [!proof]+
> (a) $Tx-b=(Tx-TT^\dagger b)+(TT^\dagger b-b)$. The first term is in $\range T$; the second is in $(\range T)^\perp$ because $TT^\dagger=P_{\range T}$ ([[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-69|6.69]](b), [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-57|6.57]](f)). By [[Linear Algebra 6A Inner Products and Norms#^ladr-6-12|6.12]], $\|Tx-b\|\ge\|TT^\dagger b-b\|$, with equality iff $T(x-T^\dagger b)=0$.
>
> (b) $x=(x-T^\dagger b)+T^\dagger b$ with $x-T^\dagger b\in\nullsp T$ and $T^\dagger b\in(\nullsp T)^\perp$; apply [[Linear Algebra 6A Inner Products and Norms#^ladr-6-12|6.12]].

*Uses:* [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-69|6.69]], [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-57|6.57]], [[Linear Algebra 6A Inner Products and Norms#^ladr-6-12|6.12]]

> [!example] 6.71 Pseudoinverse of a linear map from F⁴ to F³ (p. 223)
> $T(a,b,c,d)=(a+b+c,\ 2c+d,\ 0)$ from $\F^4$ to $\F^3$ is neither injective nor surjective.
> - $\range T=\{(x,y,0)\}$, so $P_{\range T}(x,y,z)=(x,y,0)$.
> - $\nullsp T$ has basis $(-1,1,0,0)$, $(-1,0,1,-2)$.
>
> $T^\dagger(x,y,z)$ is the $(a,b,c,d)\in(\nullsp T)^\perp$ with $T(a,b,c,d)=(x,y,0)$:
> $$
> a+b+c=x,\quad 2c+d=y,\quad -a+b=0,\quad -a+c-2d=0,
> $$
> giving
> $$
> T^\dagger(x,y,z)=\tfrac1{11}\big(5x-2y,\ 5x-2y,\ x+4y,\ -2x+3y\big)
> $$
> (agrees with the Moore–Penrose inverse computed numerically). Note that $z$ is ignored: it is the part of the target that $T$ cannot reach.

^ladr-6-71
