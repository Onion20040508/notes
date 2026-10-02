---
type: section
subject: "[[Linear Algebra]]"
chapter: 7
section: 25
aliases: ["LADR 7D", "7D Isometries, Unitary Operators, and Matrix Factorization"]
tags: [linear-algebra]
---
← [[§24 Positive Operators]] · ↑ [[· 7 Operators on Inner Product Spaces]] · [[§26 Singular Value Decomposition]] →

> [!definition] Definition 7.44: Isometry
> $S\in\Lin(V,W)$ is an *isometry* if $\|Sv\|=\|v\|$ for every $v\in V$. Every isometry is injective ($Sv=0\Rightarrow\|v\|=0$).

^ladr-7-44

> [!remark]- Connections
> - Characterizations [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|7.49]]; singular values all $1$ ([[§26 Singular Value Decomposition#^ladr-7-69|7.69]]).
> - Infinite-dimensional counterpart: isomorphic Hilbert spaces are related by an inner-product-preserving bijection ([[§20 Orthonormal Sets and Bases#^def-20-6|556 Def. §20.6]]), and there an isometry of a space into itself need not be onto ([[§20 Orthonormal Sets and Bases#^ex-20-2|556 Ex. §20.2]]).
> - Computational version: [[§41 Orthogonal Sets#^thm-41-5|235 Thm. §41.5]] (a matrix with orthonormal columns preserves lengths and inner products).

> [!example] Example 7.45: Orthonormal basis maps to orthonormal list ⟹ isometry (p. 258)
> If $e_1,\dots,e_n$ is an orthonormal basis of $V$ and $g_1,\dots,g_n$ an orthonormal list in $W$, the linear $S$ with $Se_k=g_k$ is an isometry: for $v=\sum\langle v,e_k\rangle e_k$,
> $$
> \|Sv\|^2=\Big\|\sum\langle v,e_k\rangle g_k\Big\|^2=\sum|\langle v,e_k\rangle|^2=\|v\|^2
> $$
> ([[§20 Orthonormal Bases#^ladr-6-24|6.24]], [[§20 Orthonormal Bases#^ladr-6-30|6.30]](b)). By [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|7.49]](d) every isometry arises this way.

^ladr-7-45

> [!theorem] Theorem 7.49: Characterization of isometries
> Let $S\in\Lin(V,W)$, with orthonormal bases $e_1,\dots,e_n$ of $V$ and $f_1,\dots,f_m$ of $W$. Equivalent:
> - (a) $S$ is an isometry;
> - (b) $S^*S=I$;
> - (c) $\langle Su,Sv\rangle=\langle u,v\rangle$ for all $u,v$;
> - (d) $Se_1,\dots,Se_n$ is orthonormal;
> - (e) the columns of $\mathcal{M}(S,(e),(f))$ are orthonormal in $\F^m$.

^ladr-7-49

> [!remark] Remark: Consequences
> An isometry maps *some* orthonormal basis to an orthonormal list iff it maps *every* one; and 'preserves norms' is the same as 'preserves inner products' (c).

> [!proof]+ Proof
> (a)$\Rightarrow$(b): $\langle(I-S^*S)v,v\rangle=\|v\|^2-\|Sv\|^2=0$ for all $v$, and $I-S^*S$ is self-adjoint, so it is $0$ ([[§22 Self-Adjoint and Normal Operators#^ladr-7-16|7.16]]).
>
> (b)$\Rightarrow$(c): $\langle Su,Sv\rangle=\langle S^*Su,v\rangle=\langle u,v\rangle$.
>
> (c)$\Rightarrow$(d): $\langle Se_j,Se_k\rangle=\langle e_j,e_k\rangle$.
>
> (d)$\Rightarrow$(e): with $A=\mathcal{M}(S)$, $Se_k=\sum_jA_{j,k}f_j$, so the Euclidean inner product of columns $k,r$ is $\sum_jA_{j,k}\overline{A_{j,r}}=\langle Se_k,Se_r\rangle$ ([[§20 Orthonormal Bases#^ladr-6-30|6.30]](c)), which is $\delta_{kr}$.
>
> (e)$\Rightarrow$(a): reading the same computation backwards, $Se_1,\dots,Se_n$ is orthonormal. Then for $v=\sum\langle v,e_k\rangle e_k$, $\|Sv\|^2=\sum|\langle v,e_k\rangle|^2=\|v\|^2$ by [[§20 Orthonormal Bases#^ladr-6-24|6.24]] and [[§20 Orthonormal Bases#^ladr-6-30|6.30]](b).

*Uses:* [[§22 Self-Adjoint and Normal Operators#^ladr-7-16|7.16]], [[§20 Orthonormal Bases#^ladr-6-30|6.30]], [[§20 Orthonormal Bases#^ladr-6-24|6.24]]

> [!remark]- Connections
> - Computational version: [[§41 Orthogonal Sets#^thm-41-4|235 Thm. §41.4]] ($U^TU=I$ iff $U$ has orthonormal columns) and [[§41 Orthogonal Sets#^thm-41-5|235 Thm. §41.5]].

> [!definition] Definition 7.51: Unitary operator
> An operator $S\in\Lin(V)$ is *unitary* if it is an invertible isometry. (In finite dimensions 'invertible' is automatic, by injectivity and [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]].)

^ladr-7-51

> [!remark]- Connections
> - Real case: orthogonal operators. Physics: time evolution $e^{-iHt/\hbar}$ and symmetry transformations are unitary.
> - Used in Quantum Mechanics: rotations act on kets by unitary operators $e^{-i\mathbf J\cdot\hat n\phi/\hbar}$ — [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-3|QM Theorem §C5.1.3]].

> [!example] Example 7.52: Rotation of R² (p. 260)
> $\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$ has orthonormal columns, so it is unitary ([[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|7.49]](e)). Over $\R$ it is rotation by $\theta$, which obviously preserves length. Its eigenvalues over $\C$ are $e^{\pm i\theta}$, of absolute value $1$ ([[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-54|7.54]]).

^ladr-7-52

> [!theorem] Theorem 7.53: Characterization of unitary operators
> Let $S\in\Lin(V)$ and $e_1,\dots,e_n$ an orthonormal basis. Equivalent:
> - (a) $S$ is unitary;
> - (b) $S^*S=SS^*=I$;
> - (c) $S$ is invertible and $S^{-1}=S^*$;
> - (d) $Se_1,\dots,Se_n$ is an orthonormal basis of $V$;
> - (e) the rows of $\mathcal{M}(S,(e))$ form an orthonormal basis of $\F^n$;
> - (f) $S^*$ is unitary.

^ladr-7-53

> [!proof]+ Proof
> (a)$\Rightarrow$(b): $S^*S=I$ ([[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|7.49]]); multiplying on the right by $S^{-1}$ gives $S^*=S^{-1}$, so $SS^*=I$. (b)$\Rightarrow$(c): definition of inverse. (c)$\Rightarrow$(d): $S^*S=I$ makes $Se_1,\dots,Se_n$ orthonormal ([[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|7.49]]), of length $\dim V$ ([[§20 Orthonormal Bases#^ladr-6-28|6.28]]). (d)$\Rightarrow$(e): by [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|7.49]] $S$ is unitary, so $(S^*)^*S^*=SS^*=I$ and $S^*$ is an isometry; the columns of $\mathcal{M}(S^*)=\mathcal{M}(S)^*$ are orthonormal ([[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|7.49]](e)), and these are the conjugated rows of $\mathcal{M}(S)$. (e)$\Rightarrow$(f): the same reading backwards makes $S^*$ an isometry, hence unitary. (f)$\Rightarrow$(a): apply (a)$\Rightarrow$(f) to $S^*$ and use $(S^*)^*=S$.

*Uses:* [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|7.49]], [[§20 Orthonormal Bases#^ladr-6-28|6.28]]

> [!remark]- Connections
> - Unitary operators are normal, so over $\C$ the spectral theorem applies: [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-55|7.55]].
> - Computational version: [[§41 Orthogonal Sets#^prop-41-6|235 Prop. §41.6]] (orthogonal matrices: $U^{-1}=U^T$ iff orthonormal columns iff orthonormal rows).

> [!theorem] Theorem 7.54: Eigenvalues of unitary operators have absolute value 1
> Every eigenvalue $\lambda$ of a unitary operator has $|\lambda|=1$.

^ladr-7-54

> [!proof]+ Proof
> $Sv=\lambda v$, $v\ne0$: $|\lambda|\|v\|=\|Sv\|=\|v\|$.

> [!theorem] Theorem 7.55: Description of unitary operators on complex inner product spaces
> Let $\F=\C$ and $S\in\Lin(V)$. Then $S$ is unitary iff $V$ has an orthonormal basis of eigenvectors of $S$ whose eigenvalues all have absolute value $1$.

^ladr-7-55

> [!remark] Remark: Unitary = $e^{i\cdot\text{Hermitian}}$
> Writing $\lambda_k=e^{i\theta_k}$, $S=e^{iA}$ where $A$ is self-adjoint with eigenvalues $\theta_k$ on the same eigenbasis. This is the finite-dimensional Stone theorem.

> [!proof]+ Proof
> ($\Rightarrow$) $S$ is normal ([[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-53|7.53]](b)), so [[Complex spectral theorem|7.31]] gives an orthonormal eigenbasis, and [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-54|7.54]] gives $|\lambda_k|=1$.
>
> ($\Leftarrow$) $\langle Se_j,Se_k\rangle=\lambda_j\bar\lambda_k\langle e_j,e_k\rangle=\delta_{jk}$ (since $|\lambda_k|^2=1$), so $Se_1,\dots,Se_n$ is orthonormal and $S$ is unitary ([[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-53|7.53]](d)).

*Uses:* [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-53|7.53]], [[Complex spectral theorem|7.31]], [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-54|7.54]]

> [!remark]- Connections
> - Used in Quantum Mechanics: the time-evolution operator of a time-independent Hamiltonian, $\mathscr U = e^{-iHt/\hbar}$, is this description read backwards — [[§C3.1 The Time-Evolution Operator and the Schrödinger Equation#^thm-c3-1-4|QM Theorem §C3.1.4]].

> [!definition] Definition 7.56: Unitary matrix
> An $n$-by-$n$ matrix is *unitary* if its columns form an orthonormal list (equivalently basis) in $\F^n$. For orthonormal bases, $S$ is unitary iff its matrix is ([[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|7.49]](e)).

^ladr-7-56

> [!remark]- Connections
> - Computational version: [[§41 Orthogonal Sets#^def-41-5|235 Def. §41.5]] (orthogonal matrices, the real case).

> [!theorem] Theorem 7.57: Characterizations of unitary matrices
> For an $n$-by-$n$ matrix $Q$, equivalent:
> - (a) $Q$ is unitary;
> - (b) the rows of $Q$ form an orthonormal list;
> - (c) $\|Qv\|=\|v\|$ for all $v\in\F^n$;
> - (d) $Q^*Q=QQ^*=I$.

^ladr-7-57

> [!proof]+ Proof
> (Left as an exercise in Axler.) Let $S\in\Lin(\F^n)$ have standard matrix $Q$; the standard basis is orthonormal. Then (a) says the columns are orthonormal, i.e. $S$ is an isometry ([[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|7.49]](e)), i.e. $S$ is unitary ([[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-51|7.51]]); (b) is [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-53|7.53]](e); (c) is the definition of isometry for $S$; (d) is [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-53|7.53]](b) translated by [[§22 Self-Adjoint and Normal Operators#^ladr-7-9|7.9]]. All are equivalent to $S$ being unitary.

*Uses:* [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|7.49]], [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-51|7.51]], [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-53|7.53]], [[§22 Self-Adjoint and Normal Operators#^ladr-7-9|7.9]]

> [!remark]- Connections
> - The real orthogonal matrices form the orthogonal group O(n), [[§3 Basic Examples of Groups#^def-3-7|493 Def. §3.7]].
> - The matrices described here form the groups O(n) and U(n) of 591: [[§8 Topological Groups and Classical Matrix Groups#^def-8-6|591 Def. §8.6]], [[§8 Topological Groups and Classical Matrix Groups#^prop-8-7|591 Prop. §8.7]], [[§8 Topological Groups and Classical Matrix Groups#^def-8-8|591 Def. §8.8]]; orthonormal columns make U(n) compact, [[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-19-5|591 Cor. §19.5]].
> - Computational version: [[§41 Orthogonal Sets#^prop-41-6|235 Prop. §41.6]] and [[§41 Orthogonal Sets#^thm-41-5|235 Thm. §41.5]] (length preservation, as in (c)).
> - Used in Quantum Mechanics: the $2\times2$ unitary matrices of determinant 1 (with Theorem 9.58) form $SU(2)$, the unit sphere of $\mathbb C^2$, and are exactly the spin-½ rotation matrices — [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-5|QM Theorem §C5.2.5]].

> [!theorem] Theorem 7.58: QR factorization
> If $A$ is a square matrix with linearly independent columns, there are unique $Q,R$ with $Q$ unitary, $R$ upper triangular with positive diagonal, and $A=QR$.

^ladr-7-58

> [!remark] Remark: Use
> $Ax=b\iff Rx=Q^*b$, solved by back substitution; numerically more stable than Gaussian elimination.

> [!proof]+ Proof
> **Existence.** Let $v_1,\dots,v_n$ be the columns of $A$; Gram–Schmidt ([[Gram–Schmidt procedure|6.32]]) gives an orthonormal basis $e_1,\dots,e_n$ with $\Span(v_1,\dots,v_k)=\Span(e_1,\dots,e_k)$. Put $R_{j,k}=\langle v_k,e_j\rangle$ and let $Q$ have columns $e_1,\dots,e_n$. For $j>k$, $e_j\perp\Span(e_1,\dots,e_k)\ni v_k$, so $R$ is upper triangular. Column $k$ of $QR$ is $\sum_j\langle v_k,e_j\rangle e_j=v_k$ ([[§20 Orthonormal Bases#^ladr-6-30|6.30]](a)), so $QR=A$. From the Gram–Schmidt formulas $v_k=\|f_k\|e_k+(\text{combination of }e_1,\dots,e_{k-1})$, so $R_{k,k}=\|f_k\|>0$.
>
> **Uniqueness.** If $A=QR=\hat Q\hat R$, then $U=\hat Q^*Q=\hat RR^{-1}$ is unitary and upper triangular with positive diagonal. Its inverse $U^*$ is lower triangular, but the inverse of an invertible upper-triangular matrix is upper triangular; so $U^*$, hence $U$, is diagonal. A diagonal unitary matrix has $|u_{k,k}|=1$, and $u_{k,k}>0$, so $U=I$: $\hat Q=Q$ and $\hat R=R$.

*Uses:* [[Gram–Schmidt procedure|6.32]], [[§20 Orthonormal Bases#^ladr-6-30|6.30]]

> [!remark]- Connections
> - Gives Cholesky [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-63|7.63]]; used for Hadamard's inequality ([[§34 Determinants#^ladr-9-66|Hadamard’s inequality]]).
> - Computational version: [[§43 The Gram–Schmidt Process#^thm-43-3|235 Thm. §43.3]] (QR from Gram–Schmidt, for $m\times n$ matrices with independent columns; worked in [[§43 The Gram–Schmidt Process#^ex-43-3|235 Ex. §43.3]]).

> [!example] Example 7.60: QR factorization of a 3-by-3 matrix (p. 265)
> $A=\begin{pmatrix}1&2&1\\0&1&-4\\0&3&2\end{pmatrix}$, columns $v_1=(1,0,0)$, $v_2=(2,1,3)$, $v_3=(1,-4,2)$. Gram–Schmidt gives
> $$
> e_1=(1,0,0),\quad e_2=\tfrac1{\sqrt{10}}(0,1,3),\quad e_3=\tfrac1{\sqrt{10}}(0,-3,1),
> $$
> and $R_{j,k}=\langle v_k,e_j\rangle$:
> $$
> Q=\begin{pmatrix}1&0&0\\0&\frac1{\sqrt{10}}&-\frac3{\sqrt{10}}\\0&\frac3{\sqrt{10}}&\frac1{\sqrt{10}}\end{pmatrix},\qquad
> R=\begin{pmatrix}1&2&1\\0&\sqrt{10}&\frac{\sqrt{10}}5\\0&0&\frac{7\sqrt{10}}5\end{pmatrix}.
> $$
> Checked symbolically: $QR=A$ and $Q^*Q=I$.

^ladr-7-60

> [!theorem] Theorem 7.61: Positive invertible operator
> A self-adjoint $T\in\Lin(V)$ is positive and invertible iff $\langle Tv,v\rangle>0$ for every $v\ne0$.

^ladr-7-61

> [!proof]+ Proof
> ($\Rightarrow$) $v\ne0\Rightarrow Tv\ne0\Rightarrow\langle Tv,v\rangle\ne0$ ([[§24 Positive Operators#^ladr-7-43|7.43]]), and it is $\ge0$. ($\Leftarrow$) positivity is clear, and $\langle Tv,v\rangle>0$ forces $Tv\ne0$, so $T$ is injective, hence invertible ([[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]]).

*Uses:* [[§24 Positive Operators#^ladr-7-43|7.43]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]]

> [!definition] Definition 7.62: Positive definite
> $B\in\F^{n,n}$ is *positive definite* if $B^*=B$ and $\langle Bx,x\rangle>0$ for every nonzero $x\in\F^n$.

^ladr-7-62

> [!remark]- Connections
> - Equivalently all eigenvalues $>0$; Gram matrices $\big(\langle v_k,v_j\rangle\big)$ of independent lists are positive definite. Metric tensors $g_{ij}$ in Riemannian geometry are positive definite at each point.
> - Computational version: [[§49★ Quadratic Forms#^def-49-5|235 Def. §49.5]] (positive definite matrices, real case).
> - Used in Electromagnetism: the capacitance matrix of a system of conductors is a Gram matrix, and it and the coefficients of potential are positive definite — [[§C4.3 The Capacitance Matrix#^thm-c4-3-2|EM Theorem §C4.3.2]], [[§C4.3 The Capacitance Matrix#^thm-c4-3-5|EM Theorem §C4.3.5]].

> [!theorem] Theorem 7.63: Cholesky factorization
> If $B$ is positive definite, there is a unique upper-triangular $R$ with positive diagonal such that $B=R^*R$.

^ladr-7-63

> [!remark] Remark: Use
> Solving $Bx=b$ via two triangular systems; sampling correlated Gaussians ($x=R^*z$ has covariance $B$).

> [!proof]+ Proof
> By [[§24 Positive Operators#^ladr-7-38|7.38]](f), $B=A^*A$ for some $A$, invertible since $B$ is. With $A=QR$ ([[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-58|7.58]]), $B=R^*Q^*QR=R^*R$.
>
> Uniqueness: if also $B=S^*S$ with $S$ upper triangular, positive diagonal, then $S$ is invertible and $(AS^{-1})^*(AS^{-1})=(S^*)^{-1}BS^{-1}=I$, so $AS^{-1}$ is unitary and $A=(AS^{-1})S$ is a QR factorization. Uniqueness in [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-58|7.58]] gives $S=R$.

*Uses:* [[§24 Positive Operators#^ladr-7-38|7.38]], [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-58|7.58]]

> [!remark]- Connections
> - Computational version: [[§49★ Quadratic Forms#^rem-49-3|235 Remark §49.3]] (as a fast test for positive definiteness).
> - Used in Quantum Mechanics: the Ritz equations $\mathsf H\mathbf c = \varepsilon\mathsf S\mathbf c$ with a positive definite overlap matrix $\mathsf S$ (Definition 7.62), a generalized eigenvalue problem that the Cholesky factorization turns into an ordinary one — [[§C9.3 The Ritz Variational Method#^thm-c9-3-3|QM Theorem §C9.3.3]].

