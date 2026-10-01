---
type: section
subject: "[[Linear Algebra]]"
chapter: 8
section: 31
aliases: ["LADR 8D", "8D Trace꞉ A Connection Between Matrices and Operators"]
tags: [linear-algebra]
---
← [[§30 Consequences of Generalized Eigenspace Decomposition]] · ↑ [[· 8 Operators on Complex Vector Spaces]] · [[§32 Bilinear Forms and Quadratic Forms]] →

> [!definition] Definition 8.47: Trace of a matrix
> The *trace* $\operatorname{tr}A$ of a square matrix is the sum of its diagonal entries.

^ladr-8-47

> [!example] Example 8.48: Trace of a 3-by-3 matrix (p. 326)
> $\operatorname{tr}\begin{pmatrix}3&-1&-2\\3&2&-3\\1&2&0\end{pmatrix}=3+2+0=5$.

^ladr-8-48

> [!theorem] Theorem 8.49: Trace of AB equals trace of BA
> For $A$ ($m$-by-$n$) and $B$ ($n$-by-$m$), $\operatorname{tr}(AB)=\operatorname{tr}(BA)$.

^ladr-8-49

> [!remark] Remark: Cyclic, not symmetric
> $\operatorname{tr}(ABC)=\operatorname{tr}(CAB)$, but in general $\operatorname{tr}(ABC)\ne\operatorname{tr}(BAC)$.

> [!proof]+ Proof
> $\operatorname{tr}(AB)=\sum_j\sum_kA_{j,k}B_{k,j}=\sum_k\sum_jB_{k,j}A_{j,k}=\operatorname{tr}(BA)$.

> [!theorem] Theorem 8.50: Trace of matrix of operator does not depend on basis
> For $T\in\Lin(V)$ and bases $u$, $v$ of $V$: $\operatorname{tr}\mathcal{M}(T,(u))=\operatorname{tr}\mathcal{M}(T,(v))$.

^ladr-8-50

> [!proof]+ Proof
> $A=C^{-1}BC$ by [[§10 Invertibility and Isomorphisms#^ladr-3-84|3.84]], so $\operatorname{tr}A=\operatorname{tr}\big((C^{-1}B)C\big)=\operatorname{tr}\big(C(C^{-1}B)\big)=\operatorname{tr}B$ ([[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|8.49]]).

*Uses:* [[§10 Invertibility and Isomorphisms#^ladr-3-84|3.84]], [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|8.49]]

> [!definition] Definition 8.51: Trace of an operator
> The *trace* of $T\in\Lin(V)$ is $\operatorname{tr}T=\operatorname{tr}\mathcal{M}(T,(v_1,\dots,v_n))$ for any basis (well defined by [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-50|8.50]]).

^ladr-8-51

> [!theorem] Theorem 8.52: On complex vector spaces, trace equals sum of eigenvalues
> If $\F=\C$, $\operatorname{tr}T$ is the sum of the eigenvalues of $T$, each counted with multiplicity.

^ladr-8-52

> [!proof]+ Proof
> In the basis of [[§29 Generalized Eigenspace Decomposition#^ladr-8-37|8.37]] the diagonal lists each eigenvalue as often as its multiplicity; the trace is basis-independent ([[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-50|8.50]]).

*Uses:* [[§29 Generalized Eigenspace Decomposition#^ladr-8-37|8.37]], [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-50|8.50]]

> [!remark]- Connections
> - Real operators: via complexification, or [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-54|Trace and characteristic polynomial]].

> [!example] Example 8.53: Trace of an operator on C³ (p. 328)
> $T(z_1,z_2,z_3)=(3z_1-z_2-2z_3,\ 3z_1+2z_2-3z_3,\ z_1+2z_2)$ on $\C^3$ has the matrix of [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-48|8.48]], so $\operatorname{tr}T=5$. Its eigenvalues are $1$, $2+3i$, $2-3i$ (verified), and $1+(2+3i)+(2-3i)=5$, as [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-52|8.52]] predicts.

^ladr-8-53

> [!theorem] Theorem 8.54: Trace and characteristic polynomial
> ($\F=\C$, $n=\dim V$) $\operatorname{tr}T$ is minus the coefficient of $z^{n-1}$ in the characteristic polynomial.

^ladr-8-54

> [!remark] Remark: Constant term
> The constant term is $(-1)^n$ times the product of the eigenvalues, i.e. $(-1)^n\det T$.

> [!proof]+ Proof
> $(z-\lambda_1)\cdots(z-\lambda_n)=z^n-(\lambda_1+\dots+\lambda_n)z^{n-1}+\dots+(-1)^n\lambda_1\cdots\lambda_n$; use [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-52|8.52]].

*Uses:* [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-52|8.52]]

> [!theorem] Theorem 8.55: Trace on an inner product space
> On an inner product space with orthonormal basis $e_1,\dots,e_n$,
> $$
> \operatorname{tr}T=\langle Te_1,e_1\rangle+\dots+\langle Te_n,e_n\rangle .
> $$

^ladr-8-55

> [!proof]+ Proof
> The $(k,k)$ entry of $\mathcal{M}(T)$ is $\langle Te_k,e_k\rangle$ ([[§20 Orthonormal Bases#^ladr-6-30|6.30]](a) for $v=Te_k$).

*Uses:* [[§20 Orthonormal Bases#^ladr-6-30|6.30]]

> [!remark]- Connections
> - Physics: $\operatorname{Tr}(\rho A)=\sum_k\langle e_k|\rho A|e_k\rangle$ is the expectation value of $A$ in the state $\rho$, independent of the basis.

> [!theorem] Theorem 8.56: Trace is linear
> $\operatorname{tr}:\Lin(V)\to\F$ is a linear functional with $\operatorname{tr}(ST)=\operatorname{tr}(TS)$ for all $S,T$.

^ladr-8-56

> [!remark] Remark: Characterization
> $\operatorname{tr}$ is the unique linear functional on $\Lin(V)$ with $\operatorname{tr}(ST)=\operatorname{tr}(TS)$ and $\operatorname{tr}I=\dim V$.

> [!proof]+ Proof
> In a fixed basis, $\mathcal{M}(\lambda T)=\lambda\mathcal{M}(T)$ and $\mathcal{M}(S+T)=\mathcal{M}(S)+\mathcal{M}(T)$ ([[§9 Matrices#^ladr-3-38|3.38]], [[§9 Matrices#^ladr-3-35|3.35]]), and matrix trace is linear. And $\operatorname{tr}(ST)=\operatorname{tr}(\mathcal{M}(S)\mathcal{M}(T))=\operatorname{tr}(\mathcal{M}(T)\mathcal{M}(S))=\operatorname{tr}(TS)$ ([[§9 Matrices#^ladr-3-43|3.43]], [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|8.49]]).

*Uses:* [[§9 Matrices#^ladr-3-38|3.38]], [[§9 Matrices#^ladr-3-35|3.35]], [[§9 Matrices#^ladr-3-43|3.43]], [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|8.49]]

> [!theorem] Theorem 8.57: Identity operator is not the difference of ST and TS
> There are no $S,T\in\Lin(V)$ with $ST-TS=I$.

^ladr-8-57

> [!remark] Remark: Physics
> So the canonical commutation relation $[\hat x,\hat p]=i\hbar I$ has no finite-dimensional solution: position and momentum must act on an infinite-dimensional space. On $\Poly(\R)$, $D\circ M_x-M_x\circ D=I$ does hold ([[§7 Vector Space of Linear Maps#^ladr-3-9|3.9]]).

> [!proof]+ Proof
> $\operatorname{tr}(ST-TS)=0$ ([[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-56|8.56]]) but $\operatorname{tr}I=\dim V\ne0$.

*Uses:* [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-56|8.56]]

