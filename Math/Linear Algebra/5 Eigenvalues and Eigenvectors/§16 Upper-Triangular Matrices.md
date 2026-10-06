---
type: section
subject: "[[Linear Algebra]]"
chapter: 5
section: 16
aliases: ["LADR 5C", "5C Upper-Triangular Matrices"]
tags: [linear-algebra]
---
← [[§15 The Minimal Polynomial]] · ↑ [[· 5 Eigenvalues and Eigenvectors]] · [[§17 Diagonalizable Operators]] →

> [!definition] Definition 5.35: Matrix of an operator, M(T)
> For $T\in\Lin(V)$ and a basis $v_1,\dots,v_n$ of $V$, the *matrix of $T$* is the $n$-by-$n$ matrix $\mathcal{M}(T)$ with
> $$
> Tv_k=A_{1,k}v_1+\dots+A_{n,k}v_n .
> $$
> Written $\mathcal{M}(T,(v_1,\dots,v_n))$ when the basis matters. Operators have **square** matrices; column $k$ holds the coordinates of $Tv_k$.

^ladr-5-35

> [!remark] Remark: The program of Chapters 5–8
> Choose a basis making $\mathcal{M}(T)$ as simple as possible: first a zero first column below $\lambda$ (any eigenvector as $v_1$), then upper triangular ([[§16 Upper-Triangular Matrices#^ladr-5-44|5.44]]), then diagonal when possible ([[§17 Diagonalizable Operators#^ladr-5-62|5.62]]), and in general Jordan form ([[Jordan form|8.46]]).

> [!remark]- Connections
> - Special case of [[§9 Matrices#^ladr-3-31|3.31]] with the same basis on both sides; change of basis is [[§10 Invertibility and Isomorphisms#^ladr-3-84|3.84]].
> - Computational version: [[§35 Eigenvectors and Linear Transformations#^def-35-1|235 Def. §35.1]] and [[§35 Eigenvectors and Linear Transformations#^thm-35-1|235 Thm. §35.1]] (the matrix of a transformation relative to bases, computed column by column, with worked examples).

> [!example] Example 5.36: Matrix of an operator with respect to standard basis (p. 154)
> $T(x,y,z)=(2x+y,\ 5y+3z,\ 8z)$ on $\F^3$. The columns of the matrix are $T(e_1)=(2,0,0)$, $T(e_2)=(1,5,0)$, $T(e_3)=(0,3,8)$:
> $$
> \mathcal{M}(T)=\begin{pmatrix}2&1&0\\0&5&3\\0&0&8\end{pmatrix}.
> $$
> Over $\C$ one can always get at least a zero first column below $\lambda$: take an eigenvector as $v_1$ ([[Existence of eigenvalues|5.19]]) and extend to a basis.

^ladr-5-36

> [!definition] Definition 5.37: Diagonal of a matrix
> The *diagonal* of a square matrix is the list of entries $A_{1,1},\dots,A_{n,n}$, from the upper left to the lower right corner.

^ladr-5-37

> [!remark]- Connections
> - For upper-triangular matrices the diagonal is exactly the list of eigenvalues: [[§16 Upper-Triangular Matrices#^ladr-5-41|5.41]]. Its sum is the trace ([[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-47|Trace of a matrix]]).

> [!definition] Definition 5.38: Upper-triangular matrix
> A square matrix is *upper triangular* if all entries below the diagonal are $0$:
> $$
> \begin{pmatrix}\lambda_1&&*\\&\ddots&\\0&&\lambda_n\end{pmatrix}.
> $$

^ladr-5-38

> [!remark]- Connections
> - Characterized by invariant subspaces: [[§16 Upper-Triangular Matrices#^ladr-5-39|5.39]]. Existence: [[§16 Upper-Triangular Matrices#^ladr-5-44|5.44]], always over $\C$ ([[If F = C, then every operator on V has an upper-triangular matrix|5.47]]).

> [!theorem] Theorem 5.39: Conditions for upper-triangular matrix
> Let $T\in\Lin(V)$ and $v_1,\dots,v_n$ a basis of $V$. The following are equivalent:
> - (a) $\mathcal{M}(T,(v_1,\dots,v_n))$ is upper triangular;
> - (b) $\Span(v_1,\dots,v_k)$ is invariant under $T$ for each $k=1,\dots,n$;
> - (c) $Tv_k\in\Span(v_1,\dots,v_k)$ for each $k=1,\dots,n$.

^ladr-5-39

> [!remark] Remark: Flags
> A chain $\{0\}\subsetneq U_1\subsetneq\dots\subsetneq U_n=V$ with $\dim U_k=k$ is a *flag*. So: $T$ is upper triangular in some basis iff $T$ preserves some flag.

> [!proof]+ Proof
> (a)$\Rightarrow$(b): upper triangular means $Tv_j\in\Span(v_1,\dots,v_j)\subseteq\Span(v_1,\dots,v_k)$ for $j\le k$, so $\Span(v_1,\dots,v_k)$ is invariant.
>
> (b)$\Rightarrow$(c): take $v_k\in\Span(v_1,\dots,v_k)$.
>
> (c)$\Rightarrow$(a): writing $Tv_k$ in the basis uses only $v_1,\dots,v_k$, so column $k$ has zeros below the diagonal.

> [!remark]- Connections
> - Used in [[§16 Upper-Triangular Matrices#^ladr-5-44|5.44]] and [[§18 Commuting Operators#^ladr-5-80|5.80]].

%% ex:5.39-flag %%
> [!example] Example: Upper triangular = preserving a flag
> In $\R^3$ with $v_1,v_2,v_3$: $T$ is upper triangular iff it maps the line $\Span(v_1)$ into itself and the plane $\Span(v_1,v_2)$ into itself ([[§16 Upper-Triangular Matrices#^ladr-5-39|5.39]]). In red, condition (c): $Tv_1\in\Span(v_1)$, $Tv_2\in\Span(v_1,v_2)$, and $Tv_3$ anywhere in $V$.
>
> ![[ladr-5.39-flag.svg|340]]

> [!theorem] Theorem 5.40: Equation satisfied by operator with upper-triangular matrix
> If $T\in\Lin(V)$ has an upper-triangular matrix with diagonal entries $\lambda_1,\dots,\lambda_n$ with respect to some basis, then
> $$
> (T-\lambda_1I)\cdots(T-\lambda_nI)=0 .
> $$

^ladr-5-40

> [!remark] Remark: Cayley–Hamilton preview
> The polynomial $(z-\lambda_1)\cdots(z-\lambda_n)$ is the [[§34 Determinants#^ladr-9-63|characteristic polynomial]]; over $\C$ this is already Cayley–Hamilton ([[Cayley–Hamilton theorem|8.29]]).

> [!proof]+ Proof
> Let $v_1,\dots,v_n$ be the basis. We show by induction on $k$ that $(T-\lambda_1I)\cdots(T-\lambda_kI)$ kills $v_1,\dots,v_k$. For $k=1$: $Tv_1=\lambda_1v_1$. For the step, $(T-\lambda_kI)v_k\in\Span(v_1,\dots,v_{k-1})$ (the diagonal entry cancels), which the first $k-1$ factors kill; and they kill $v_1,\dots,v_{k-1}$ already. Since the factors commute ([[§14 Invariant Subspaces#^ladr-5-17|5.17]]), adding more factors on the left keeps these vectors killed. For $k=n$ the product vanishes on a basis, hence is $0$.

*Uses:* [[§14 Invariant Subspaces#^ladr-5-17|5.17]]

> [!remark]- Connections
> - Gives the bound on the minimal polynomial used in [[§16 Upper-Triangular Matrices#^ladr-5-41|5.41]], [[§16 Upper-Triangular Matrices#^ladr-5-44|5.44]], and in [[§17 Diagonalizable Operators#^ladr-5-61|5.61]].

> [!theorem] Theorem 5.41: Determination of eigenvalues from upper-triangular matrix
> If $T\in\Lin(V)$ has an upper-triangular matrix with respect to some basis, then the eigenvalues of $T$ are exactly the entries on the diagonal of that matrix.

^ladr-5-41

> [!remark] Remark: Not row echelon form
> Gaussian elimination produces an upper-triangular matrix too, but it is not the matrix of $T$ in any basis and its diagonal is not the eigenvalue list. Also: only $v_1$ is guaranteed to be an eigenvector; $v_k$ is one iff column $k$ is zero off the diagonal.

> [!proof]+ Proof
> **Diagonal entries are eigenvalues.** $Tv_1=\lambda_1v_1$. For $k\ge2$, $(T-\lambda_kI)v_k\in\Span(v_1,\dots,v_{k-1})$, so $T-\lambda_kI$ maps the $k$-dimensional $\Span(v_1,\dots,v_k)$ into the $(k-1)$-dimensional $\Span(v_1,\dots,v_{k-1})$. By [[§8 Null Spaces and Ranges#^ladr-3-22|3.22]] it is not injective there, giving an eigenvector for $\lambda_k$.
>
> **No others.** $q(z)=(z-\lambda_1)\cdots(z-\lambda_n)$ satisfies $q(T)=0$ ([[§16 Upper-Triangular Matrices#^ladr-5-40|5.40]]), so the minimal polynomial divides $q$ ([[§15 The Minimal Polynomial#^ladr-5-29|5.29]]); its zeros, which are the eigenvalues ([[§15 The Minimal Polynomial#^ladr-5-27|5.27]]), are among $\lambda_1,\dots,\lambda_n$.

*Uses:* [[§8 Null Spaces and Ranges#^ladr-3-22|3.22]], [[§16 Upper-Triangular Matrices#^ladr-5-40|5.40]], [[§15 The Minimal Polynomial#^ladr-5-29|5.29]], [[§15 The Minimal Polynomial#^ladr-5-27|5.27]]

> [!remark]- Connections
> - Eigenvalues are hard to compute in general ([[§15 The Minimal Polynomial#^ladr-5-28|5.28]]); upper-triangular form makes them visible.
> - Computational version: [[§32 Eigenvectors and Eigenvalues#^thm-32-1|235 Thm. §32.1]] (the eigenvalues of a triangular matrix are its diagonal entries).

> [!example] Example 5.42: Eigenvalues via an upper-triangular matrix (p. 158)
> For $T$ of [[§16 Upper-Triangular Matrices#^ladr-5-36|5.36]], the standard matrix is upper triangular with diagonal $2,5,8$, so by [[§16 Upper-Triangular Matrices#^ladr-5-41|5.41]] the eigenvalues are exactly $2$, $5$, $8$, with no computation.

^ladr-5-42

%% ex:5.41-fig %%
> [!example] Example: Why a diagonal entry is an eigenvalue, pictured
> For $T$ of [[§16 Upper-Triangular Matrices#^ladr-5-36|5.36]] on $\Span(e_1,e_2)$: $Te_1=2e_1$ and $Te_2=e_1+5e_2$, so $T-5I$ sends $e_1\mapsto-3e_1$ and $e_2\mapsto e_1$. It squeezes the plane $\Span(e_1,e_2)$ into the line $\Span(e_1)$, as in the proof of [[§16 Upper-Triangular Matrices#^ladr-5-41|5.41]], so some nonzero vector goes to $0$: $(T-5I)(e_1+3e_2)=-3e_1+3e_1=0$. Thus $(1,3,0)$ is an eigenvector for $5$ (red; compare [[§17 Diagonalizable Operators#^ladr-5-59|5.59]]).
>
> ![[ladr-5.41-collapse.svg|440]]

> [!example] Example 5.43: Whether T has an upper-triangular matrix can depend on F (p. 158)
> $T(z_1,z_2,z_3,z_4)=(-z_2,\ z_1,\ 2z_1+3z_3,\ z_3+3z_4)$, i.e.
> $$
> \mathcal{M}(T)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\2&0&3&0\\0&0&1&3\end{pmatrix},
> $$
> with minimal polynomial $p(z)=(z^2+1)(z-3)^2=z^4-6z^3+10z^2-6z+9$ (verified: $(T^2+I)(T-3I)\ne0$, so the square is needed).
> - $\F=\R$: $z^2+1$ does not split, so by [[§16 Upper-Triangular Matrices#^ladr-5-44|5.44]] no basis of $\R^4$ makes $T$ upper triangular.
> - $\F=\C$: $p=(z-i)(z+i)(z-3)^2$ splits. Indeed, in the basis $(4-3i,-3-4i,-3+i,1)$, $(4+3i,-3+4i,-3-i,1)$, $(0,0,0,1)$, $(0,0,1,0)$,
> $$
> \mathcal{M}(T)=\begin{pmatrix}i&0&0&0\\0&-i&0&0\\0&0&3&1\\0&0&0&3\end{pmatrix}
> $$
> (verified by computing $B^{-1}AB$). Note the $3$-block is not diagonal: this $T$ is not diagonalizable ([[§17 Diagonalizable Operators#^ladr-5-62|5.62]], repeated root).

^ladr-5-43

> [!theorem] Theorem 5.44: Necessary and sufficient condition to have an upper-triangular matrix
> Let $V$ be finite-dimensional and $T\in\Lin(V)$. Then $T$ has an upper-triangular matrix with respect to some basis iff the minimal polynomial of $T$ equals $(z-\lambda_1)\cdots(z-\lambda_m)$ for some $\lambda_1,\dots,\lambda_m\in\F$.

^ladr-5-44

> [!proof]+ Proof
> ($\Rightarrow$) With diagonal entries $\alpha_1,\dots,\alpha_n$, $q(z)=(z-\alpha_1)\cdots(z-\alpha_n)$ has $q(T)=0$ ([[§16 Upper-Triangular Matrices#^ladr-5-40|5.40]]), so the minimal polynomial divides $q$ ([[§15 The Minimal Polynomial#^ladr-5-29|5.29]]) and is a product of linear factors.
>
> ($\Leftarrow$) Induction on $m$. If $m=1$, $T=\lambda_1I$. For $m>1$ let $U=\range(T-\lambda_mI)$, invariant by [[§14 Invariant Subspaces#^ladr-5-18|5.18]]. For $u=(T-\lambda_mI)v\in U$, $(T-\lambda_1I)\cdots(T-\lambda_{m-1}I)u=0$, so the minimal polynomial of $T|_U$ divides $(z-\lambda_1)\cdots(z-\lambda_{m-1})$ ([[§15 The Minimal Polynomial#^ladr-5-29|5.29]]); by induction $U$ has a basis $u_1,\dots,u_M$ with $T|_U$ upper triangular. Extend to a basis $u_1,\dots,u_M,v_1,\dots,v_N$ of $V$ ([[Every linearly independent list extends to a basis|2.32]]). Then $Tu_j\in\Span(u_1,\dots,u_j)$ and
> $$
> Tv_k=(T-\lambda_mI)v_k+\lambda_mv_k\in U+\Span(v_k)\subseteq\Span(u_1,\dots,u_M,v_1,\dots,v_k),
> $$
> so the matrix is upper triangular by [[§16 Upper-Triangular Matrices#^ladr-5-39|5.39]].

*Uses:* [[§16 Upper-Triangular Matrices#^ladr-5-40|5.40]], [[§15 The Minimal Polynomial#^ladr-5-29|5.29]], [[§14 Invariant Subspaces#^ladr-5-18|5.18]], [[Every linearly independent list extends to a basis|2.32]], [[§16 Upper-Triangular Matrices#^ladr-5-39|5.39]]

> [!remark]- Connections
> - Over $\C$ the condition is automatic: [[If F = C, then every operator on V has an upper-triangular matrix|5.47]]. Diagonal version: [[§17 Diagonalizable Operators#^ladr-5-62|5.62]] (distinct $\lambda$'s).

> [!theorem] Theorem 5.47: If F = C, then every operator on V has an upper-triangular matrix
> If $V$ is a finite-dimensional complex vector space and $T\in\Lin(V)$, then $T$ has an upper-triangular matrix with respect to some basis of $V$.

^ladr-5-47

> [!proof]+ Proof
> The minimal polynomial factors into linear factors over $\C$ ([[§13 Polynomials#^ladr-4-13|4.13]]); apply [[§16 Upper-Triangular Matrices#^ladr-5-44|5.44]].

*Uses:* [[§13 Polynomials#^ladr-4-13|4.13]], [[§16 Upper-Triangular Matrices#^ladr-5-44|5.44]]

