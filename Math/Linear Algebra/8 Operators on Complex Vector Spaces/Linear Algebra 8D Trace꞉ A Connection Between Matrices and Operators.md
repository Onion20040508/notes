---
type: section
subject: "[[Linear Algebra]]"
chapter: 8
section: "8D"
tags: [linear-algebra]
---
← [[Linear Algebra 8C Consequences of Generalized Eigenspace Decomposition]] · ↑ [[Linear Algebra — 8 Operators on Complex Vector Spaces]] · [[Linear Algebra 9A Bilinear Forms and Quadratic Forms]] →

> [!definition] 8.47 Trace of a matrix
> The *trace* $\operatorname{tr}A$ of a square matrix is the sum of its diagonal entries.

^ladr-8-47

> [!example] 8.48 Trace of a 3-by-3 matrix (p. 326)
> $\operatorname{tr}\begin{pmatrix}3&-1&-2\\3&2&-3\\1&2&0\end{pmatrix}=3+2+0=5$.

^ladr-8-48

> [!theorem] 8.49 Trace of AB equals trace of BA
> For $A$ ($m$-by-$n$) and $B$ ($n$-by-$m$), $\operatorname{tr}(AB)=\operatorname{tr}(BA)$.

^ladr-8-49

> [!remark] Cyclic, not symmetric
> $\operatorname{tr}(ABC)=\operatorname{tr}(CAB)$, but in general $\operatorname{tr}(ABC)\ne\operatorname{tr}(BAC)$.

> [!proof]+
> $\operatorname{tr}(AB)=\sum_j\sum_kA_{j,k}B_{k,j}=\sum_k\sum_jB_{k,j}A_{j,k}=\operatorname{tr}(BA)$.

> [!theorem] 8.50 Trace of matrix of operator does not depend on basis
> For $T\in\Lin(V)$ and bases $u$, $v$ of $V$: $\operatorname{tr}\mathcal{M}(T,(u))=\operatorname{tr}\mathcal{M}(T,(v))$.

^ladr-8-50

> [!proof]+
> $A=C^{-1}BC$ by [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-84|3.84]], so $\operatorname{tr}A=\operatorname{tr}\big((C^{-1}B)C\big)=\operatorname{tr}\big(C(C^{-1}B)\big)=\operatorname{tr}B$ ([[Linear Algebra 8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|8.49]]).

*Uses:* [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-84|3.84]], [[Linear Algebra 8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|8.49]]

> [!definition] 8.51 Trace of an operator
> The *trace* of $T\in\Lin(V)$ is $\operatorname{tr}T=\operatorname{tr}\mathcal{M}(T,(v_1,\dots,v_n))$ for any basis (well defined by [[Linear Algebra 8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-50|8.50]]).

^ladr-8-51

> [!theorem] 8.52 On complex vector spaces, trace equals sum of eigenvalues
> If $\F=\C$, $\operatorname{tr}T$ is the sum of the eigenvalues of $T$, each counted with multiplicity.

^ladr-8-52

> [!proof]+
> In the basis of [[Linear Algebra 8B Generalized Eigenspace Decomposition#^ladr-8-37|8.37]] the diagonal lists each eigenvalue as often as its multiplicity; the trace is basis-independent ([[Linear Algebra 8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-50|8.50]]).

*Uses:* [[Linear Algebra 8B Generalized Eigenspace Decomposition#^ladr-8-37|8.37]], [[Linear Algebra 8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-50|8.50]]

> [!remark]- Connections
> - Real operators: via complexification, or [[Linear Algebra 8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-54|Trace and characteristic polynomial]].

> [!example] 8.53 Trace of an operator on C³ (p. 328)
> $T(z_1,z_2,z_3)=(3z_1-z_2-2z_3,\ 3z_1+2z_2-3z_3,\ z_1+2z_2)$ on $\C^3$ has the matrix of [[Linear Algebra 8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-48|8.48]], so $\operatorname{tr}T=5$. Its eigenvalues are $1$, $2+3i$, $2-3i$ (verified), and $1+(2+3i)+(2-3i)=5$, as [[Linear Algebra 8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-52|8.52]] predicts.

^ladr-8-53

> [!theorem] 8.54 Trace and characteristic polynomial
> ($\F=\C$, $n=\dim V$) $\operatorname{tr}T$ is minus the coefficient of $z^{n-1}$ in the characteristic polynomial.

^ladr-8-54

> [!remark] Constant term
> The constant term is $(-1)^n$ times the product of the eigenvalues, i.e. $(-1)^n\det T$.

> [!proof]+
> $(z-\lambda_1)\cdots(z-\lambda_n)=z^n-(\lambda_1+\dots+\lambda_n)z^{n-1}+\dots+(-1)^n\lambda_1\cdots\lambda_n$; use [[Linear Algebra 8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-52|8.52]].

*Uses:* [[Linear Algebra 8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-52|8.52]]

> [!theorem] 8.55 Trace on an inner product space
> On an inner product space with orthonormal basis $e_1,\dots,e_n$,
> $$
> \operatorname{tr}T=\langle Te_1,e_1\rangle+\dots+\langle Te_n,e_n\rangle .
> $$

^ladr-8-55

> [!proof]+
> The $(k,k)$ entry of $\mathcal{M}(T)$ is $\langle Te_k,e_k\rangle$ ([[Linear Algebra 6B Orthonormal Bases#^ladr-6-30|6.30]](a) for $v=Te_k$).

*Uses:* [[Linear Algebra 6B Orthonormal Bases#^ladr-6-30|6.30]]

> [!remark]- Connections
> - Physics: $\operatorname{Tr}(\rho A)=\sum_k\langle e_k|\rho A|e_k\rangle$ is the expectation value of $A$ in the state $\rho$, independent of the basis.

> [!theorem] 8.56 Trace is linear
> $\operatorname{tr}:\Lin(V)\to\F$ is a linear functional with $\operatorname{tr}(ST)=\operatorname{tr}(TS)$ for all $S,T$.

^ladr-8-56

> [!remark] Characterization
> $\operatorname{tr}$ is the unique linear functional on $\Lin(V)$ with $\operatorname{tr}(ST)=\operatorname{tr}(TS)$ and $\operatorname{tr}I=\dim V$.

> [!proof]+
> In a fixed basis, $\mathcal{M}(\lambda T)=\lambda\mathcal{M}(T)$ and $\mathcal{M}(S+T)=\mathcal{M}(S)+\mathcal{M}(T)$ ([[Linear Algebra 3C Matrices#^ladr-3-38|3.38]], [[Linear Algebra 3C Matrices#^ladr-3-35|3.35]]), and matrix trace is linear. And $\operatorname{tr}(ST)=\operatorname{tr}(\mathcal{M}(S)\mathcal{M}(T))=\operatorname{tr}(\mathcal{M}(T)\mathcal{M}(S))=\operatorname{tr}(TS)$ ([[Linear Algebra 3C Matrices#^ladr-3-43|3.43]], [[Linear Algebra 8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|8.49]]).

*Uses:* [[Linear Algebra 3C Matrices#^ladr-3-38|3.38]], [[Linear Algebra 3C Matrices#^ladr-3-35|3.35]], [[Linear Algebra 3C Matrices#^ladr-3-43|3.43]], [[Linear Algebra 8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|8.49]]

> [!theorem] 8.57 Identity operator is not the difference of ST and TS
> There are no $S,T\in\Lin(V)$ with $ST-TS=I$.

^ladr-8-57

> [!remark] Physics
> So the canonical commutation relation $[\hat x,\hat p]=i\hbar I$ has no finite-dimensional solution: position and momentum must act on an infinite-dimensional space. On $\Poly(\R)$, $D\circ M_x-M_x\circ D=I$ does hold ([[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-9|3.9]]).

> [!proof]+
> $\operatorname{tr}(ST-TS)=0$ ([[Linear Algebra 8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-56|8.56]]) but $\operatorname{tr}I=\dim V\ne0$.

*Uses:* [[Linear Algebra 8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-56|8.56]]

