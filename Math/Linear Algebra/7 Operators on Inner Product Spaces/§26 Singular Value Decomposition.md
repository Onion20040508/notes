---
type: section
subject: "[[Linear Algebra]]"
chapter: 7
section: 26
aliases: ["LADR 7E", "7E Singular Value Decomposition"]
tags: [linear-algebra]
---
← [[§25 Isometries, Unitary Operators, and Matrix Factorization]] · ↑ [[· 7 Operators on Inner Product Spaces]] · [[§27 Consequences of Singular Value Decomposition]] →

> [!theorem] Theorem 7.64: Properties of T∗T
> For $T\in\Lin(V,W)$:
> - (a) $T^*T$ is a positive operator on $V$;
> - (b) $\nullsp T^*T=\nullsp T$;
> - (c) $\range T^*T=\range T^*$;
> - (d) $\dim\range T=\dim\range T^*=\dim\range T^*T$.

^ladr-7-64

> [!proof]+ Proof
> (a) $(T^*T)^*=T^*T$ and $\langle T^*Tv,v\rangle=\|Tv\|^2\ge0$. (b) $T^*Tv=0\Rightarrow\|Tv\|^2=\langle T^*Tv,v\rangle=0$; the other inclusion is clear. (c) $\range T^*T=(\nullsp T^*T)^\perp=(\nullsp T)^\perp=\range T^*$ ([[§22 Self-Adjoint and Normal Operators#^ladr-7-6|7.6]], self-adjointness, (b)). (d) $\dim\range T=\dim(\nullsp T^*)^\perp=\dim W-\dim\nullsp T^*=\dim\range T^*$ ([[§22 Self-Adjoint and Normal Operators#^ladr-7-6|7.6]], [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-51|6.51]], [[Fundamental theorem of linear maps|3.21]]); the last equality is (c).

*Uses:* [[§22 Self-Adjoint and Normal Operators#^ladr-7-6|7.6]], [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-51|6.51]], [[Fundamental theorem of linear maps|3.21]]

> [!remark]- Connections
> - Row rank = column rank once more (d). Least squares: normal equations $T^*Tx=T^*b$.

> [!definition] Definition 7.65: Singular values
> The *singular values* of $T\in\Lin(V,W)$ are the nonnegative square roots of the eigenvalues of $T^*T$, in decreasing order, each repeated $\dim E(\lambda,T^*T)$ times. There are exactly $\dim V$ of them.

^ladr-7-65

> [!remark] Remark: Eigenvalues vs singular values
> Singular values: defined for any $T:V\to W$; always real $\ge0$; list length $\dim V$; contain $0$ iff $T$ is not injective. Eigenvalues: only for operators; possibly complex or absent; no canonical order.

> [!example] Example 7.66: Singular values of an operator on F⁴ (p. 271)
> $T(z_1,z_2,z_3,z_4)=(0,\ 3z_1,\ 2z_2,\ -3z_4)$ on $\F^4$. Then $T^*T(z_1,z_2,z_3,z_4)=(9z_1,4z_2,0,9z_4)$, with eigenvalues $9$ (twice), $4$, $0$, so the singular values are $3,3,2,0$. The eigenvalues of $T$ are only $-3$ and $0$: the '$2$' in the definition of $T$ is invisible to eigenvalues but visible to singular values. (Verified numerically.)

^ladr-7-66

> [!example] Example 7.67: Singular values of a linear map from F⁴ to F³ (p. 271)
> $T:\F^4\to\F^3$ with matrix $\begin{pmatrix}0&0&0&-5\\0&0&0&0\\1&1&0&0\end{pmatrix}$:
> $$
> \mathcal{M}(T^*T)=\begin{pmatrix}1&1&0&0\\1&1&0&0\\0&0&0&0\\0&0&0&25\end{pmatrix},
> $$
> eigenvalues $25,2,0,0$, so singular values $5,\sqrt2,0,0$ (verified numerically).

^ladr-7-67

> [!theorem] Theorem 7.68: Role of positive singular values
> For $T\in\Lin(V,W)$:
> - (a) $T$ is injective iff $0$ is not a singular value;
> - (b) the number of positive singular values equals $\dim\range T$;
> - (c) $T$ is surjective iff that number equals $\dim W$.

^ladr-7-68

> [!proof]+ Proof
> (a) $\nullsp T=\{0\}\iff\nullsp T^*T=\{0\}$ ([[§26 Singular Value Decomposition#^ladr-7-64|7.64]](b)) $\iff0$ is not an eigenvalue of $T^*T$. (b) By the spectral theorem $\dim\range T^*T$ is the number of positive eigenvalues of $T^*T$ with multiplicity, and $\dim\range T^*T=\dim\range T$ ([[§26 Singular Value Decomposition#^ladr-7-64|7.64]](d)). (c) from (b) and [[§6 Dimension#^ladr-2-39|2.39]].

*Uses:* [[§26 Singular Value Decomposition#^ladr-7-64|7.64]], [[§6 Dimension#^ladr-2-39|2.39]]

> [!theorem] Theorem 7.69: Isometries characterized by having all singular values equal 1
> $S\in\Lin(V,W)$ is an isometry iff all singular values of $S$ equal $1$.

^ladr-7-69

> [!proof]+ Proof
> $S$ isometry $\iff S^*S=I$ ([[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|7.49]]) $\iff$ all eigenvalues of the self-adjoint $S^*S$ are $1$ (spectral theorem) $\iff$ all singular values are $1$.

*Uses:* [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|7.49]]

> [!theorem] Theorem 7.70: Singular value decomposition
> Let $T\in\Lin(V,W)$ with positive singular values $s_1\ge\dots\ge s_m$. There are orthonormal lists $e_1,\dots,e_m$ in $V$ and $f_1,\dots,f_m$ in $W$ with
> $$
> Tv=s_1\langle v,e_1\rangle f_1+\dots+s_m\langle v,e_m\rangle f_m\qquad\text{for all }v\in V .
> $$

^ladr-7-70

> [!remark] Remark: Reading it
> Every linear map is: take coordinates along an orthonormal frame in $V$, scale the $k$-th by $s_k$, and place it along an orthonormal frame in $W$. Unlike the spectral theorem, the two frames differ, and the same proof works over $\R$ and $\C$.

> [!proof]+ Proof
> $T^*T$ is positive ([[§26 Singular Value Decomposition#^ladr-7-64|7.64]](a)), so there is an orthonormal basis $e_1,\dots,e_n$ of $V$ with $T^*Te_k=s_k^2e_k$ (spectral theorem; $s_k=0$ for $k>m$). For $k\le m$ put $f_k=Te_k/s_k$. Then
> $$
> \langle f_j,f_k\rangle=\frac{\langle Te_j,Te_k\rangle}{s_js_k}=\frac{\langle e_j,T^*Te_k\rangle}{s_js_k}=\frac{s_k}{s_j}\langle e_j,e_k\rangle=\delta_{jk},
> $$
> so $f_1,\dots,f_m$ is orthonormal. For $k>m$, $T^*Te_k=0$, hence $Te_k=0$ ([[§26 Singular Value Decomposition#^ladr-7-64|7.64]](b)). So $Tv=\sum_{k\le n}\langle v,e_k\rangle Te_k=\sum_{k\le m}s_k\langle v,e_k\rangle f_k$.

*Uses:* [[§26 Singular Value Decomposition#^ladr-7-64|7.64]]

%% ex:7.70-fig %%
> [!example] Example: SVD pictured: the unit ball goes to an ellipsoid
> The orthonormal frame $e_1,e_2$ in the domain goes to the axes $s_1f_1,s_2f_2$ of an ellipse in the target ([[§27 Consequences of Singular Value Decomposition#^ladr-7-99|7.99]]). Here $s_1=2$, $s_2=0.8$, and the two frames are rotated differently.
>
> ![[ladr-7.70-svd.svg|520]]

> [!definition] Definition 7.74: Diagonal matrix
> An $M$-by-$N$ matrix is *diagonal* if all entries are $0$ except possibly $A_{k,k}$, $k=1,\dots,\min\{M,N\}$.

^ladr-7-74

> [!remark] Remark: SVD as a matrix
> Extending $e$'s and $f$'s to orthonormal bases, $\mathcal{M}(T,(e),(f))$ is diagonal (in this rectangular sense) with $s_1,\dots,s_m$ first and zeros after.

> [!theorem] Theorem 7.75: Singular value decomposition of adjoint and pseudoinverse
> If $Tv=\sum_{k=1}^ms_k\langle v,e_k\rangle f_k$ is an SVD of $T$ (positive $s_k$, orthonormal $e$'s and $f$'s), then for every $w\in W$
> $$
> T^*w=\sum_{k=1}^ms_k\langle w,f_k\rangle e_k,\qquad T^\dagger w=\sum_{k=1}^m\frac{\langle w,f_k\rangle}{s_k}e_k .
> $$

^ladr-7-75

> [!remark] Remark: Recipe
> Adjoint: swap $e$ and $f$. Pseudoinverse: swap and invert the positive singular values (zeros stay zero).

> [!proof]+ Proof
> **Adjoint.** $\langle Tv,w\rangle=\sum_ks_k\langle v,e_k\rangle\langle f_k,w\rangle=\big\langle v,\sum_ks_k\langle w,f_k\rangle e_k\big\rangle$ ($s_k$ real).
>
> **Pseudoinverse.** Let $v=\sum_k\frac{\langle w,f_k\rangle}{s_k}e_k$. Since $Te_k=s_kf_k$, $Tv=\sum_k\langle w,f_k\rangle f_k=P_{\range T}w$ ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-57|6.57]](i); $f_1,\dots,f_m$ is an orthonormal basis of $\range T$). Also $v\in\Span(e_1,\dots,e_m)=\range T^*=(\nullsp T)^\perp$ (by the adjoint formula and [[§22 Self-Adjoint and Normal Operators#^ladr-7-6|7.6]]). By the definition [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-68|6.68]], $v=T^\dagger w$.

*Uses:* [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-57|6.57]], [[§22 Self-Adjoint and Normal Operators#^ladr-7-6|7.6]], [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-68|6.68]]

> [!example] Example 7.79: Finding a singular value decomposition (p. 276)
> SVD of $T(x_1,x_2,x_3,x_4)=(-5x_4,\ 0,\ x_1+x_2)$ (the map of [[§26 Singular Value Decomposition#^ladr-7-67|7.67]]). Positive singular values $5,\sqrt2$. Orthonormal eigenvectors of $T^*T$: $e_1=(0,0,0,1)$ for $25$, $e_2=\tfrac1{\sqrt2}(1,1,0,0)$ for $2$. Then
> $$
> f_1=\frac{Te_1}5=(-1,0,0),\qquad f_2=\frac{Te_2}{\sqrt2}=(0,0,1),
> $$
> and $Tv=5\langle v,e_1\rangle f_1+\sqrt2\langle v,e_2\rangle f_2$ for all $v\in\F^4$.

^ladr-7-79

> [!theorem] Theorem 7.80: Matrix version of SVD
> An $M$-by-$n$ matrix $A$ of rank $m\ge1$ factors as $A=BDC^*$ with $B$ ($M$-by-$m$) and $C$ ($n$-by-$m$) having orthonormal columns and $D$ ($m$-by-$m$) diagonal with positive diagonal.

^ladr-7-80

> [!proof]+ Proof
> Let $T:\F^n\to\F^M$ have matrix $A$; $\dim\range T=m$. Take an SVD $Tv=\sum_{k\le m}s_k\langle v,e_k\rangle f_k$ and let $B,D,C$ have columns $f_k$, diagonal $s_k$, columns $e_k$. With $u_k$ the standard basis of $\F^m$: $(AC-BD)u_k=Ae_k-s_kf_k=0$, so $AC=BD$ and $ACC^*=BDC^*$. Now $C^*e_k=u_k$, so $CC^*e_k=e_k$; and $C^*v=0$, $Av=0$ for $v\perp\Span(e_1,\dots,e_m)$. So $ACC^*=A$ on both summands of $\F^n=\Span(e)\oplus\Span(e)^\perp$, giving $A=BDC^*$.

> [!remark]- Connections
> - The usual 'full' SVD $A=U\Sigma V^*$ with square unitary $U,V$ is obtained by extending the orthonormal columns to bases.

