---
type: section
subject: "[[Linear Algebra]]"
chapter: 9
section: 34
aliases: ["LADR 9C", "9C Determinants"]
tags: [linear-algebra]
---
← [[§33 Alternating Multilinear Forms]] · ↑ [[· 9 Multilinear Algebra and Determinants]] · [[§35 Tensor Products]] →

> [!definition] Definition 9.40: ΑT
> For $T\in\Lin(V)$ and $\alpha\in V^{(m)}_{\mathrm{alt}}$, define $\alpha_T\in V^{(m)}_{\mathrm{alt}}$ by $\alpha_T(v_1,\dots,v_m)=\alpha(Tv_1,\dots,Tv_m)$. The map $\alpha\mapsto\alpha_T$ is linear on $V^{(m)}_{\mathrm{alt}}$.

^ladr-9-40

> [!remark] Remark: Why alternating is preserved
> If $v_j=v_k$ then $Tv_j=Tv_k$, so $\alpha_T$ vanishes. In [[Differentiable Manifolds]] language, $\alpha_T=T^*\alpha$ is the pullback.

> [!definition] Definition 9.41: Determinant of an operator, det T
> The *determinant* $\det T$ of $T\in\Lin(V)$ is the unique number with
> $$
> \alpha_T=(\det T)\,\alpha\qquad\text{for all }\alpha\in V^{(\dim V)}_{\mathrm{alt}} .
> $$
> It exists because $V^{(\dim V)}_{\mathrm{alt}}$ is $1$-dimensional ([[§33 Alternating Multilinear Forms#^ladr-9-37|9.37]]), and every linear map of a $1$-dimensional space to itself is multiplication by a scalar.

^ladr-9-41

> [!remark] Remark: Meaning
> The factor by which $T$ scales every 'volume form'. No basis, no formula: those come afterwards ([[§34 Determinants#^ladr-9-46|9.46]], [[§34 Determinants#^ladr-9-53|9.53]]).

> [!example] Example 9.42: Determinants of operators (p. 354)
> With $n=\dim V$ and $\alpha\in V^{(n)}_{\mathrm{alt}}$:
> - $\alpha_I=\alpha$, so $\det I=1$.
> - $\alpha_{\lambda I}=\lambda^n\alpha$, so $\det(\lambda I)=\lambda^n$; more generally $\det(\lambda T)=\lambda^n\det T$.
> - If $T$ has an eigenbasis $e_k$ with eigenvalues $\lambda_k$: $\alpha_T(e_1,\dots,e_n)=\lambda_1\cdots\lambda_n\,\alpha(e_1,\dots,e_n)$, and $\alpha(e)\ne0$ for $\alpha\ne0$ ([[§33 Alternating Multilinear Forms#^ladr-9-39|9.39]]), so $\det T=\lambda_1\cdots\lambda_n$.

^ladr-9-42

> [!definition] Definition 9.43: Determinant of a matrix, det A
> For an $n$-by-$n$ matrix $A$, $\det A=\det T$ where $T\in\Lin(\F^n)$ has matrix $A$ in the standard basis.

^ladr-9-43

> [!example] Example 9.44: Determinants of matrices (p. 355)
> - $\det I=1$ for the identity matrix.
> - A diagonal matrix with entries $\lambda_1,\dots,\lambda_n$ has $\det=\lambda_1\cdots\lambda_n$ (last bullet of [[§34 Determinants#^ladr-9-42|9.42]]).

^ladr-9-44

> [!theorem] Theorem 9.45: Determinant is an alternating multilinear form
> $(v_1,\dots,v_n)\mapsto\det\begin{pmatrix}v_1&\cdots&v_n\end{pmatrix}$ (columns $v_k\in\F^n$) is an alternating $n$-linear form on $\F^n$.

^ladr-9-45

> [!proof]+ Proof
> Let $T\in\Lin(\F^n)$ with $Te_k=v_k$, so $\det\begin{pmatrix}v_1&\cdots&v_n\end{pmatrix}=\det T$. Take $\alpha\in(\F^n)^{(n)}_{\mathrm{alt}}$ with $\alpha(e_1,\dots,e_n)=1$ ([[§33 Alternating Multilinear Forms#^ladr-9-37|9.37]]). Then
> $$
> \det T=(\det T)\,\alpha(e_1,\dots,e_n)=\alpha(Te_1,\dots,Te_n)=\alpha(v_1,\dots,v_n) .
> $$
> So the map in question *is* $\alpha$.

*Uses:* [[§33 Alternating Multilinear Forms#^ladr-9-37|9.37]]

> [!remark]- Connections
> - Consequences for row/column operations: [[§34 Determinants#^ladr-9-57|9.57]].

> [!theorem] Theorem 9.46: Formula for determinant of a matrix
> For an $n$-by-$n$ matrix $A$,
> $$
> \det A=\sum_{(j_1,\dots,j_n)\in\operatorname{perm}n}\operatorname{sign}(j_1,\dots,j_n)\,A_{j_1,1}\cdots A_{j_n,n}.
> $$

^ladr-9-46

> [!remark] Remark: Not for computing
> $n!$ terms: $10!>3\times10^6$, $100!\approx10^{158}$. Compute with row reduction ([[§34 Determinants#^ladr-9-57|9.57]]) or a factorization ($LU$/$QR$) and [[§34 Determinants#^ladr-9-48|9.48]].

> [!proof]+ Proof
> Apply [[§33 Alternating Multilinear Forms#^ladr-9-36|9.36]] on $\F^n$ with the standard basis and the alternating form of [[§34 Determinants#^ladr-9-45|9.45]]: here $b_{j,k}=A_{j,k}$ and $\alpha(e_1,\dots,e_n)=\det I=1$.

*Uses:* [[§33 Alternating Multilinear Forms#^ladr-9-36|9.36]], [[§34 Determinants#^ladr-9-45|9.45]]

> [!remark]- Connections
> - Index form: $\det A=\varepsilon_{i_1\cdots i_n}A_{i_11}\cdots A_{i_nn}$ with the Levi-Civita symbol.

> [!example] Example 9.47: Explicit formula for determinant (p. 356)
> - $2\times2$: $\det A=A_{1,1}A_{2,2}-A_{2,1}A_{1,2}$.
> - $3\times3$: $\det A=A_{1,1}A_{2,2}A_{3,3}-A_{2,1}A_{1,2}A_{3,3}-A_{3,1}A_{2,2}A_{1,3}-A_{1,1}A_{3,2}A_{2,3}+A_{3,1}A_{1,2}A_{2,3}+A_{2,1}A_{3,2}A_{1,3}$ (six permutations, three of each sign).
>
> In $\R^3$ this is the scalar triple product $v_1\cdot(v_2\times v_3)$ of the columns.

^ladr-9-47

> [!theorem] Theorem 9.48: Determinant of upper-triangular matrix
> If $A$ is upper triangular with diagonal $\lambda_1,\dots,\lambda_n$, then $\det A=\lambda_1\cdots\lambda_n$.

^ladr-9-48

> [!proof]+ Proof
> For $(j_1,\dots,j_n)\ne(1,\dots,n)$ some $j_k>k$ (otherwise, going from $k=1$ up, $j_k=k$ is forced), so $A_{j_k,k}=0$. Only the identity permutation contributes to [[§34 Determinants#^ladr-9-46|9.46]].

*Uses:* [[§34 Determinants#^ladr-9-46|9.46]]

> [!theorem] Theorem 9.49: Determinant is multiplicative
> (a) $\det(ST)=(\det S)(\det T)$ for $S,T\in\Lin(V)$. (b) $\det(AB)=(\det A)(\det B)$ for square matrices of the same size.

^ladr-9-49

> [!remark] Remark: Why this is 'magic'
> With the Leibniz formula this is a messy computation; with the abstract definition it is one line: scaling factors compose.

> [!proof]+ Proof
> (a) For $\alpha\in V^{(n)}_{\mathrm{alt}}$:
> $$
> \alpha_{ST}(v_1,\dots,v_n)=\alpha(S(Tv_1),\dots,S(Tv_n))=(\det S)\,\alpha(Tv_1,\dots,Tv_n)=(\det S)(\det T)\,\alpha(v_1,\dots,v_n).
> $$
> (b) Take $S,T$ with standard matrices $A,B$; $\mathcal{M}(ST)=AB$ ([[§9 Matrices#^ladr-3-43|3.43]]).

*Uses:* [[§9 Matrices#^ladr-3-43|3.43]]

> [!theorem] Theorem 9.50: Invertible ⟺ nonzero determinant
> $T\in\Lin(V)$ is invertible iff $\det T\ne0$; then $\det(T^{-1})=\dfrac1{\det T}$.

^ladr-9-50

> [!proof]+ Proof
> If $T$ is invertible, $1=\det I=\det(TT^{-1})=(\det T)\det(T^{-1})$ ([[§34 Determinants#^ladr-9-49|9.49]]).
>
> If $\det T\ne0$ and $v\ne0$, extend to a basis $v,e_2,\dots,e_n$ and take $\alpha\ne0$ alternating. Then $\alpha(v,e_2,\dots,e_n)\ne0$ ([[§33 Alternating Multilinear Forms#^ladr-9-39|9.39]]), so $\alpha(Tv,Te_2,\dots,Te_n)=(\det T)\alpha(v,e_2,\dots,e_n)\ne0$, forcing $Tv\ne0$. So $T$ is injective, hence invertible ([[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]]).

*Uses:* [[§34 Determinants#^ladr-9-49|9.49]], [[§33 Alternating Multilinear Forms#^ladr-9-39|9.39]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]]

> [!theorem] Theorem 9.51: Eigenvalues and determinants
> $\lambda$ is an eigenvalue of $T$ iff $\det(\lambda I-T)=0$.

^ladr-9-51

> [!proof]+ Proof
> $\lambda$ is an eigenvalue iff $T-\lambda I$ is not invertible ([[§14 Invariant Subspaces#^ladr-5-7|5.7]]) iff $\lambda I-T$ is not invertible iff $\det(\lambda I-T)=0$ ([[Invertible ⟺ nonzero determinant|9.50]]).

*Uses:* [[§14 Invariant Subspaces#^ladr-5-7|5.7]], [[Invertible ⟺ nonzero determinant|9.50]]

> [!theorem] Theorem 9.52: Determinant is a similarity invariant
> If $T\in\Lin(V)$ and $S:W\to V$ is invertible, then $\det(S^{-1}TS)=\det T$.

^ladr-9-52

> [!proof]+ Proof
> (Works even for $W\ne V$, where $\det S$ is meaningless.) For $\tau\in W^{(n)}_{\mathrm{alt}}$ define $\alpha(v_1,\dots,v_n)=\tau(S^{-1}v_1,\dots,S^{-1}v_n)\in V^{(n)}_{\mathrm{alt}}$. Then
> $$
> \tau_{S^{-1}TS}(w_1,\dots,w_n)=\alpha(TSw_1,\dots,TSw_n)=(\det T)\,\alpha(Sw_1,\dots,Sw_n)=(\det T)\,\tau(w_1,\dots,w_n).
> $$

> [!theorem] Theorem 9.53: Determinant of operator equals determinant of its matrix
> For any basis $e_1,\dots,e_n$ of $V$, $\det T=\det\mathcal{M}(T,(e_1,\dots,e_n))$.

^ladr-9-53

> [!proof]+ Proof
> Let $S:\F^n\to V$, $Sf_k=e_k$ ($f$ the standard basis). Then $\mathcal{M}(S^{-1}TS,(f))=\mathcal{M}(T,(e))$ ([[§9 Matrices#^ladr-3-43|3.43]]), so $\det T=\det(S^{-1}TS)=\det\mathcal{M}(T,(e))$ by [[§34 Determinants#^ladr-9-52|9.52]] and [[§34 Determinants#^ladr-9-43|9.43]].

*Uses:* [[§9 Matrices#^ladr-3-43|3.43]], [[§34 Determinants#^ladr-9-52|9.52]], [[§34 Determinants#^ladr-9-43|9.43]]

> [!theorem] Theorem 9.55: If F = C, then determinant equals product of eigenvalues
> If $\F=\C$, $\det T$ is the product of the eigenvalues of $T$, each counted with multiplicity.

^ladr-9-55

> [!proof]+ Proof
> Use the upper-triangular basis of [[§29 Generalized Eigenspace Decomposition#^ladr-8-37|8.37]] with [[§34 Determinants#^ladr-9-53|9.53]] and [[§34 Determinants#^ladr-9-48|9.48]].

*Uses:* [[§29 Generalized Eigenspace Decomposition#^ladr-8-37|8.37]], [[§34 Determinants#^ladr-9-53|9.53]], [[§34 Determinants#^ladr-9-48|9.48]]

> [!remark]- Connections
> - Compare $\operatorname{tr}T$ = sum of eigenvalues ([[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-52|8.52]]); both are coefficients of the characteristic polynomial ([[§34 Determinants#^ladr-9-65|9.65]]).

> [!theorem] Theorem 9.56: Determinant of transpose, dual, or adjoint
> (a) $\det A^t=\det A$. (b) $\det T'=\det T$. (c) On an inner product space, $\det T^*=\overline{\det T}$.

^ladr-9-56

> [!remark] Remark: Rows vs columns
> (a) means everything true for columns is true for rows.

> [!proof]+ Proof
> (a) $\alpha(v_1,\dots,v_n)=\det\big(\begin{pmatrix}v_1&\cdots&v_n\end{pmatrix}^t\big)$ is $n$-linear by [[§34 Determinants#^ladr-9-46|9.46]]. It is alternating: if $v_j=v_k$ the matrix $\begin{pmatrix}v_1&\cdots&v_n\end{pmatrix}^t$ has two equal rows, so $\big(\cdots\big)^tB$ never equals $I$; the matrix is not invertible and its determinant is $0$ ([[Invertible ⟺ nonzero determinant|9.50]]). It takes the value $1$ on the standard basis, so by [[§33 Alternating Multilinear Forms#^ladr-9-37|9.37]] it equals $\det\begin{pmatrix}v_1&\cdots&v_n\end{pmatrix}$.
>
> (b) $\mathcal{M}(T')=\mathcal{M}(T)^t$ in dual bases ([[§12 Duality#^ladr-3-132|Matrix of T (LADR 3.132)]]); use (a) and [[§34 Determinants#^ladr-9-53|9.53]]. (c) In an orthonormal basis $\mathcal{M}(T^*)=\overline{\mathcal{M}(T)}^t$ ([[§22 Self-Adjoint and Normal Operators#^ladr-7-9|7.9]]); conjugating every entry conjugates the Leibniz sum; use (a).

*Uses:* [[§34 Determinants#^ladr-9-46|9.46]], [[Invertible ⟺ nonzero determinant|9.50]], [[§33 Alternating Multilinear Forms#^ladr-9-37|9.37]], [[§34 Determinants#^ladr-9-53|9.53]], [[§22 Self-Adjoint and Normal Operators#^ladr-7-9|7.9]]

> [!theorem] Theorem 9.57: Helpful results in evaluating determinants
> For square matrices:
> - (a) two equal columns or two equal rows $\Rightarrow\det=0$;
> - (b) swapping two columns or two rows changes the sign;
> - (c) multiplying a column or row by $c$ multiplies $\det$ by $c$;
> - (d) adding a multiple of one column to another leaves $\det$ unchanged;
> - (e) likewise for rows.

^ladr-9-57

> [!remark] Remark: Computation
> Row-reduce to upper-triangular form using (b) and (e), tracking sign changes, then multiply the diagonal ([[§34 Determinants#^ladr-9-48|9.48]]): $O(n^3)$ operations instead of $n!$.

> [!proof]+ Proof
> $\det$ is an alternating multilinear function of the columns ([[§34 Determinants#^ladr-9-45|9.45]]) and of the rows ([[§34 Determinants#^ladr-9-56|9.56]](a)). (a) is 'alternating', (b) is [[§33 Alternating Multilinear Forms#^ladr-9-30|9.30]], (c) is linearity in one slot, and (d):
> $$
> \det\begin{pmatrix}v_1+cv_2&v_2&\cdots\end{pmatrix}=\det\begin{pmatrix}v_1&v_2&\cdots\end{pmatrix}+c\det\begin{pmatrix}v_2&v_2&\cdots\end{pmatrix}=\det\begin{pmatrix}v_1&v_2&\cdots\end{pmatrix}.
> $$
> (e) is (d) for $A^t$.

*Uses:* [[§34 Determinants#^ladr-9-45|9.45]], [[§34 Determinants#^ladr-9-56|9.56]], [[§33 Alternating Multilinear Forms#^ladr-9-30|9.30]]

%% ex:9.57-fig %%
> [!example] Example: Adding a multiple of a column, pictured
> In $\R^2$, replacing $v_1$ by $v_1+cv_2$ slides the top edge of the parallelogram along $v_2$. The base $v_2$ and the height stay the same, so the area $|\det\begin{pmatrix}v_1&v_2\end{pmatrix}|$ does not change: this is (d).
>
> ![[ladr-9.57-shear.svg|400]]

> [!theorem] Theorem 9.58: Every unitary operator has determinant with absolute value 1
> If $S$ is unitary, then $|\det S|=1$.

^ladr-9-58

> [!remark] Remark: Real case
> Orthogonal operators have $\det=\pm1$: rotations ($+1$) versus reflections ($-1$).

> [!proof]+ Proof
> $1=\det(S^*S)=\overline{\det S}\,\det S=|\det S|^2$ ([[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-53|7.53]], [[§34 Determinants#^ladr-9-49|9.49]], [[§34 Determinants#^ladr-9-56|9.56]](c)).

*Uses:* [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-53|7.53]], [[§34 Determinants#^ladr-9-49|9.49]], [[§34 Determinants#^ladr-9-56|9.56]]

> [!theorem] Theorem 9.59: Every positive operator has nonnegative determinant
> If $T$ is positive, then $\det T\ge0$.

^ladr-9-59

> [!proof]+ Proof
> In an orthonormal eigenbasis ([[Real spectral theorem|7.29]], [[Complex spectral theorem|7.31]]) $\det T$ is the product of the eigenvalues (last bullet of [[§34 Determinants#^ladr-9-42|9.42]]), all $\ge0$ ([[§24 Positive Operators#^ladr-7-38|7.38]]).

*Uses:* [[Real spectral theorem|7.29]], [[Complex spectral theorem|7.31]], [[§34 Determinants#^ladr-9-42|9.42]], [[§24 Positive Operators#^ladr-7-38|7.38]]

> [!theorem] Theorem 9.60: |det T| = product of singular values of T
> On an inner product space, $|\det T|=\sqrt{\det(T^*T)}=$ the product of the singular values of $T$.

^ladr-9-60

> [!proof]+ Proof
> $|\det T|^2=\overline{\det T}\det T=\det(T^*)\det T=\det(T^*T)$ ([[§34 Determinants#^ladr-9-56|9.56]](c), [[§34 Determinants#^ladr-9-49|9.49]]). In an orthonormal eigenbasis of $T^*T$ its eigenvalues are $s_1^2,\dots,s_n^2$, so $\det(T^*T)=s_1^2\cdots s_n^2$.

*Uses:* [[§34 Determinants#^ladr-9-56|9.56]], [[§34 Determinants#^ladr-9-49|9.49]]

> [!remark]- Connections
> - Combined with [[§27 Consequences of Singular Value Decomposition#^ladr-7-111|7.111]]: [[§34 Determinants#^ladr-9-61|9.61]]. Also the polar decomposition $T=S\sqrt{T^*T}$ ([[§27 Consequences of Singular Value Decomposition#^ladr-7-93|7.93]]) with $|\det S|=1$.

> [!theorem] Theorem 9.61: T changes volume by factor of |det T|
> For $T\in\Lin(\R^n)$ and $\Omega\subseteq\R^n$: $\operatorname{volume}T(\Omega)=|\det T|\operatorname{volume}\Omega$.

^ladr-9-61

> [!remark] Remark: Orientation
> The sign of $\det T$ records whether $T$ preserves ($+$) or reverses ($-$) orientation; figure below.

> [!proof]+ Proof
> [[§27 Consequences of Singular Value Decomposition#^ladr-7-111|7.111]] and [[§34 Determinants#^ladr-9-60|9.60]] (if $T$ is not invertible, $T(\Omega)$ lies in a proper subspace and has volume $0=|\det T|$).

*Uses:* [[§27 Consequences of Singular Value Decomposition#^ladr-7-111|7.111]], [[§34 Determinants#^ladr-9-60|9.60]]

> [!remark]- Connections
> - The Jacobian in the change-of-variables formula $\int_{T(\Omega)}f=\int_\Omega(f\circ T)|\det DT|$; integration of forms on oriented manifolds keeps the sign (Lee, Ch. 16).

%% ex:9.61-fig %%
> [!example] Example: Determinant as signed volume
> The unit square (dashed) spanned by $e_1,e_2$ goes to the parallelogram spanned by $Te_1,Te_2$, whose area is $|\det T|$. Left: $\det T=2>0$, orientation kept ($Te_1$ to $Te_2$ still counterclockwise). Right: $\det T=-2<0$, same area, orientation reversed.
>
> ![[ladr-9.61-signed-area.svg|520]]

> [!theorem] Theorem 9.62: If F = C, then characteristic polynomial of T equals det(zI − T)
> If $\F=\C$, then $\det(zI-T)=(z-\lambda_1)^{d_1}\cdots(z-\lambda_m)^{d_m}$: the characteristic polynomial of [[§29 Generalized Eigenspace Decomposition#^ladr-8-26|8.26]].

^ladr-9-62

> [!proof]+ Proof
> In the basis of [[§29 Generalized Eigenspace Decomposition#^ladr-8-37|8.37]], $zI-T$ is upper triangular with $z-\lambda_k$ appearing $d_k$ times on the diagonal; apply [[§34 Determinants#^ladr-9-48|9.48]] and [[§34 Determinants#^ladr-9-53|9.53]].

*Uses:* [[§29 Generalized Eigenspace Decomposition#^ladr-8-37|8.37]], [[§34 Determinants#^ladr-9-48|9.48]], [[§34 Determinants#^ladr-9-53|9.53]]

> [!definition] Definition 9.63: Characteristic polynomial
> The *characteristic polynomial* of $T\in\Lin(V)$ is $z\mapsto\det(zI-T)$ (any $\F$). It is monic of degree $\dim V$ ([[§34 Determinants#^ladr-9-46|9.46]]), and its zeros in $\F$ are the eigenvalues ([[§34 Determinants#^ladr-9-51|9.51]]).

^ladr-9-63

> [!remark]- Connections
> - Agrees with [[§29 Generalized Eigenspace Decomposition#^ladr-8-26|8.26]] over $\C$ ([[§34 Determinants#^ladr-9-62|9.62]]); makes sense over $\R$, where operators may lack eigenvalues.

> [!theorem] Theorem 9.64: Cayley–Hamilton theorem
> If $q$ is the characteristic polynomial of $T\in\Lin(V)$ (any $\F$), then $q(T)=0$.

^ladr-9-64

> [!remark] Remark: Complexification
> The real case is proved by viewing the same matrix over $\C$: a standard technique.

> [!proof]+ Proof
> Over $\C$: [[§34 Determinants#^ladr-9-62|9.62]] and [[Cayley–Hamilton theorem|8.29]]. Over $\R$: fix a basis, let $A=\mathcal{M}(T)$ and $S\in\Lin(\C^n)$ with matrix $A$. For real $z$, $q(z)=\det(zI-A)$, which is also the characteristic polynomial of $S$; so $q(S)=0$ by the complex case, i.e. $q(A)=0$, i.e. $q(T)=0$.

*Uses:* [[§34 Determinants#^ladr-9-62|9.62]], [[Cayley–Hamilton theorem|8.29]]

> [!theorem] Theorem 9.65: Characteristic polynomial, trace, and determinant
> With $n=\dim V$, the characteristic polynomial of $T$ is
> $$
> z^n-(\operatorname{tr}T)\,z^{n-1}+\dots+(-1)^n\det T .
> $$

^ladr-9-65

> [!proof]+ Proof
> The constant term is the value at $z=0$: $\det(-T)=(-1)^n\det T$ ([[§34 Determinants#^ladr-9-42|9.42]]). In [[§34 Determinants#^ladr-9-46|9.46]] for $\det(zI-A)$, the identity permutation contributes $(z-A_{1,1})\cdots(z-A_{n,n})$, whose $z^{n-1}$ coefficient is $-\operatorname{tr}A$; every other permutation moves at least two indices, so its term has at most $n-2$ diagonal factors and no $z^{n-1}$.

*Uses:* [[§34 Determinants#^ladr-9-42|9.42]], [[§34 Determinants#^ladr-9-46|9.46]]

> [!remark]- Connections
> - For $2\times2$: $z^2-(\operatorname{tr}T)z+\det T$; eigenvalues $\frac12\big(\operatorname{tr}\pm\sqrt{\operatorname{tr}^2-4\det}\big)$.

> [!theorem] Theorem 9.66: Hadamard’s inequality
> If $A$ is $n$-by-$n$ with columns $v_1,\dots,v_n$, then
> $$
> |\det A|\le\prod_{k=1}^n\|v_k\| .
> $$

^ladr-9-66

> [!remark] Remark: Geometry
> Among parallelepipeds with given edge lengths, the box (orthogonal edges) has the largest volume.

> [!proof]+ Proof
> If $A$ is not invertible, $\det A=0$. Otherwise $A=QR$ ([[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-58|7.58]]), and
> $$
> |\det A|=|\det Q|\,|\det R|=\prod_kR_{k,k}\le\prod_k\|R_{\cdot,k}\|=\prod_k\|QR_{\cdot,k}\|=\prod_k\|v_k\| ,
> $$
> using [[§34 Determinants#^ladr-9-49|9.49]], [[§34 Determinants#^ladr-9-58|9.58]], [[§34 Determinants#^ladr-9-48|9.48]], $R_{k,k}\le$ the norm of column $k$ of $R$, and that $Q$ is an isometry.

*Uses:* [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-58|7.58]], [[§34 Determinants#^ladr-9-49|9.49]], [[§34 Determinants#^ladr-9-58|9.58]], [[§34 Determinants#^ladr-9-48|9.48]]

%% ex:9.66-fig %%
> [!example] Example: Hadamard's inequality, pictured
> For two columns: $R_{1,1}=\|v_1\|$ is the base and $R_{2,2}$, the distance from $v_2$ to $\Span(v_1)$, is the height, so $|\det A|=R_{1,1}R_{2,2}$. Since $R_{2,2}\le\|v_2\|$, the parallelogram has area at most that of the dashed box with sides $\|v_1\|,\|v_2\|$.
>
> ![[ladr-9.66-hadamard.svg|320]]

> [!theorem] Theorem 9.67: Determinant of Vandermonde matrix
> For $n>1$ and $\beta_1,\dots,\beta_n\in\F$,
> $$
> \det\begin{pmatrix}1&\beta_1&\beta_1^2&\cdots&\beta_1^{n-1}\\\vdots&&&&\vdots\\1&\beta_n&\beta_n^2&\cdots&\beta_n^{n-1}\end{pmatrix}=\prod_{1\le j<k\le n}(\beta_k-\beta_j).
> $$

^ladr-9-67

> [!proof]+ Proof
> The Vandermonde matrix $A$ is $\mathcal{M}(S)$ for $S:\Poly_{n-1}(\F)\to\F^n$, $Sp=(p(\beta_1),\dots,p(\beta_n))$, with bases $1,z,\dots,z^{n-1}$ and standard. Let $T$ on $\Poly_{n-1}(\F)$ send $1\mapsto1$ and $z^k\mapsto(z-\beta_1)\cdots(z-\beta_k)$; its matrix $B$ is upper triangular with $1$'s on the diagonal, so $\det B=1$. Then $C=\mathcal{M}(ST)=AB$ has entries $C_{j,k+1}=(\beta_j-\beta_1)\cdots(\beta_j-\beta_k)$, which is $0$ for $j\le k$: $C$ is lower triangular with diagonal entries $\prod_{i<j}(\beta_j-\beta_i)$. Hence $\det A=\det C=\prod_{j<k}(\beta_k-\beta_j)$ ([[§34 Determinants#^ladr-9-56|9.56]](a), [[§34 Determinants#^ladr-9-48|9.48]]).

*Uses:* [[§34 Determinants#^ladr-9-56|9.56]], [[§34 Determinants#^ladr-9-48|9.48]]

> [!remark]- Connections
> - Polynomial interpolation through $n$ points with distinct $\beta_k$ exists and is unique (the matrix is invertible, [[Invertible ⟺ nonzero determinant|9.50]]).

