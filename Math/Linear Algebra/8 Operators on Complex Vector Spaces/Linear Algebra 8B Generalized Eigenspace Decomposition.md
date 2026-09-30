---
type: section
subject: "[[Linear Algebra]]"
chapter: 8
section: "8B"
tags: [linear-algebra]
---
← [[Linear Algebra 8A Generalized Eigenvectors and Nilpotent Operators]] · ↑ [[Linear Algebra — 8 Operators on Complex Vector Spaces]] · [[Linear Algebra 8C Consequences of Generalized Eigenspace Decomposition]] →

> [!definition] 8.19 Generalized eigenspace, G(λ, T)
> For $T\in\Lin(V)$ and $\lambda\in\F$, the *generalized eigenspace*
> $$
> G(\lambda,T)=\{v\in V:(T-\lambda I)^kv=0\text{ for some }k\ge1\}.
> $$
> $E(\lambda,T)\subseteq G(\lambda,T)$.

^ladr-8-19

> [!theorem] 8.20 Description of generalized eigenspaces
> $G(\lambda,T)=\nullsp(T-\lambda I)^{\dim V}$; in particular it is a subspace.

^ladr-8-20

> [!proof]+
> $\supseteq$ is the definition; $\subseteq$ follows from [[Linear Algebra 8A Generalized Eigenvectors and Nilpotent Operators#^ladr-8-1|8.1]], [[Linear Algebra 8A Generalized Eigenvectors and Nilpotent Operators#^ladr-8-3|8.3]] applied to $T-\lambda I$.

*Uses:* [[Linear Algebra 8A Generalized Eigenvectors and Nilpotent Operators#^ladr-8-1|8.1]], [[Linear Algebra 8A Generalized Eigenvectors and Nilpotent Operators#^ladr-8-3|8.3]]

> [!example] 8.21 Generalized eigenspaces of an operator on C³ (p. 308)
> For $T(z_1,z_2,z_3)=(4z_2,0,5z_3)$: $G(0,T)=\{(z_1,z_2,0)\}$, $G(5,T)=\{(0,0,z_3)\}$, and $\C^3=G(0,T)\oplus G(5,T)$, whereas $E(0,T)\oplus E(5,T)$ is only $2$-dimensional.

^ladr-8-21

> [!theorem] 8.22 Generalized eigenspace decomposition
> Let $\F=\C$, $T\in\Lin(V)$, with distinct eigenvalues $\lambda_1,\dots,\lambda_m$. Then
> - (a) each $G(\lambda_k,T)$ is invariant under $T$;
> - (b) $(T-\lambda_kI)|_{G(\lambda_k,T)}$ is nilpotent;
> - (c) $V=G(\lambda_1,T)\oplus\dots\oplus G(\lambda_m,T)$.

^ladr-8-22

> [!remark] Meaning
> On each piece, $T=\lambda_kI+N_k$ with $N_k$ nilpotent. Everything about $T$ reduces to nilpotent operators; Jordan form finishes the job ([[Jordan form|8.46]]).

> [!proof]+
> (a) $G(\lambda_k,T)=\nullsp(T-\lambda_kI)^{\dim V}$ ([[Linear Algebra 8B Generalized Eigenspace Decomposition#^ladr-8-20|8.20]]) is invariant by [[Linear Algebra 5A Invariant Subspaces#^ladr-5-18|5.18]]. (b) $(T-\lambda_kI)^{\dim V}$ kills $G(\lambda_k,T)$. (c) Directness: if $\sum v_k=0$ with $v_k\in G(\lambda_k,T)$, the nonzero $v_k$ would be independent ([[Linear Algebra 8A Generalized Eigenvectors and Nilpotent Operators#^ladr-8-12|8.12]]), so all vanish ([[Condition for a direct sum|1.45]]). Spanning: $V$ has a basis of generalized eigenvectors ([[Linear Algebra 8A Generalized Eigenvectors and Nilpotent Operators#^ladr-8-9|8.9]]).

*Uses:* [[Linear Algebra 8B Generalized Eigenspace Decomposition#^ladr-8-20|8.20]], [[Linear Algebra 5A Invariant Subspaces#^ladr-5-18|5.18]], [[Linear Algebra 8A Generalized Eigenvectors and Nilpotent Operators#^ladr-8-12|8.12]], [[Condition for a direct sum|1.45]], [[Linear Algebra 8A Generalized Eigenvectors and Nilpotent Operators#^ladr-8-9|8.9]]

> [!definition] 8.23 Multiplicity
> The *multiplicity* of an eigenvalue $\lambda$ of $T$ is $\dim G(\lambda,T)=\dim\nullsp(T-\lambda I)^{\dim V}$.

^ladr-8-23

> [!remark] Algebraic vs geometric
> This is the *algebraic* multiplicity; the *geometric* multiplicity is $\dim E(\lambda,T)$. Over $\C$ they agree for all $\lambda$ iff $T$ is diagonalizable, in particular for normal $T$.

> [!example] 8.24 Multiplicity of each eigenvalue of an operator (p. 310)
> $T(z_1,z_2,z_3)=(6z_1+3z_2+4z_3,\ 6z_2+2z_3,\ 7z_3)$ on $\C^3$, $\mathcal{M}(T)=\begin{pmatrix}6&3&4\\0&6&2\\0&0&7\end{pmatrix}$. Eigenvalues $6,7$, with
> $$
> G(6,T)=\Span\big((1,0,0),(0,1,0)\big),\qquad G(7,T)=\Span\big((10,2,1)\big)
> $$
> (verified: $(T-7I)(10,2,1)=0$). Multiplicities $2$ and $1$, matching the diagonal ([[Linear Algebra 8B Generalized Eigenspace Decomposition#^ladr-8-31|8.31]]). $E(6,T)$ is only $\Span(1,0,0)$, so there is no eigenbasis (compare [[Linear Algebra 5D Diagonalizable Operators#^ladr-5-61|5.61]]), but $(1,0,0),(0,1,0),(10,2,1)$ is a basis of generalized eigenvectors.

^ladr-8-24

> [!theorem] 8.25 Sum of the multiplicities equals dim V
> If $\F=\C$, the multiplicities of the eigenvalues of $T$ add up to $\dim V$.

^ladr-8-25

> [!proof]+
> [[Generalized eigenspace decomposition|8.22]](c) and [[Linear Algebra 3E Products and Quotients of Vector Spaces#^ladr-3-94|3.94]].

*Uses:* [[Generalized eigenspace decomposition|8.22]], [[Linear Algebra 3E Products and Quotients of Vector Spaces#^ladr-3-94|3.94]]

> [!definition] 8.26 Characteristic polynomial
> ($\F=\C$) If $T$ has distinct eigenvalues $\lambda_1,\dots,\lambda_m$ with multiplicities $d_1,\dots,d_m$, its *characteristic polynomial* is
> $$
> (z-\lambda_1)^{d_1}\cdots(z-\lambda_m)^{d_m}.
> $$

^ladr-8-26

> [!remark] No determinants
> Equivalent to $\det(zI-T)$ ([[Linear Algebra 9C Determinants#^ladr-9-62|If F = C, then characteristic polynomial of T equals det(zI − T)]]), but defined without them.

> [!example] 8.27 The characteristic polynomial of an operator (p. 311)
> The operator of [[Linear Algebra 8B Generalized Eigenspace Decomposition#^ladr-8-24|8.24]] has characteristic polynomial $(z-6)^2(z-7)$, which here equals the minimal polynomial ([[Linear Algebra 5D Diagonalizable Operators#^ladr-5-61|5.61]]).

^ladr-8-27

> [!theorem] 8.28 Degree and zeros of characteristic polynomial
> ($\F=\C$) The characteristic polynomial of $T$ has degree $\dim V$, and its zeros are the eigenvalues of $T$.

^ladr-8-28

> [!proof]+
> Degree by [[Linear Algebra 8B Generalized Eigenspace Decomposition#^ladr-8-25|8.25]]; zeros by definition.

*Uses:* [[Linear Algebra 8B Generalized Eigenspace Decomposition#^ladr-8-25|8.25]]

> [!theorem] 8.29 Cayley–Hamilton theorem
> If $\F=\C$ and $q$ is the characteristic polynomial of $T\in\Lin(V)$, then $q(T)=0$.

^ladr-8-29

> [!proof]+
> With $d_k=\dim G(\lambda_k,T)$, the nilpotent operator $(T-\lambda_kI)|_{G(\lambda_k,T)}$ satisfies $(T-\lambda_kI)^{d_k}|_{G(\lambda_k,T)}=0$ ([[Linear Algebra 8A Generalized Eigenvectors and Nilpotent Operators#^ladr-8-16|8.16]]). Since $V=\bigoplus G(\lambda_k,T)$ ([[Generalized eigenspace decomposition|8.22]]), it suffices that $q(T)$ vanishes on each $G(\lambda_k,T)$. The factors of $q(T)=\prod_j(T-\lambda_jI)^{d_j}$ commute, so put $(T-\lambda_kI)^{d_k}$ last (rightmost); it kills $G(\lambda_k,T)$.

*Uses:* [[Linear Algebra 8A Generalized Eigenvectors and Nilpotent Operators#^ladr-8-16|8.16]], [[Generalized eigenspace decomposition|8.22]]

> [!theorem] 8.30 Characteristic polynomial is a multiple of minimal polynomial
> ($\F=\C$) The characteristic polynomial is a polynomial multiple of the minimal polynomial.

^ladr-8-30

> [!remark] When equal
> If the minimal polynomial has degree $\dim V$ (the generic case), the two coincide.

> [!proof]+
> [[Cayley–Hamilton theorem|8.29]] and [[Linear Algebra 5B The Minimal Polynomial#^ladr-5-29|5.29]].

*Uses:* [[Cayley–Hamilton theorem|8.29]], [[Linear Algebra 5B The Minimal Polynomial#^ladr-5-29|5.29]]

> [!theorem] 8.31 Multiplicity of an eigenvalue equals number of times on diagonal
> ($\F=\C$) If $\mathcal{M}(T,(v_1,\dots,v_n))$ is upper triangular, each eigenvalue $\lambda$ appears on its diagonal exactly as many times as its multiplicity.

^ladr-8-31

> [!proof]+
> Let the diagonal be $\lambda_1,\dots,\lambda_n$, so $Tv_k=u_k+\lambda_kv_k$ with $u_k\in\Span(v_1,\dots,v_{k-1})$. If $\lambda_k\ne0$, $Tv_k\notin\Span(Tv_1,\dots,Tv_{k-1})$, so the $Tv_k$ with $\lambda_k\ne0$ are independent ([[Linear dependence lemma|2.19]]). With $d$ the number of zero diagonal entries, $\dim\range T\ge n-d$, hence $\dim\nullsp T\le d$ ([[Fundamental theorem of linear maps|3.21]]). The matrix of $T^n$ is upper triangular with diagonal $\lambda_k^n$, which has the same $d$ zeros, so $\dim\nullsp T^n\le d$.
>
> Apply this to $T-\lambda I$ (diagonal $\lambda_k-\lambda$): the multiplicity $m_\lambda=\dim\nullsp(T-\lambda I)^n\le d_\lambda$, the number of times $\lambda$ occurs on the diagonal. Summing over eigenvalues, $\sum m_\lambda=n$ ([[Linear Algebra 8B Generalized Eigenspace Decomposition#^ladr-8-25|8.25]]) and $\sum d_\lambda=n$ (every diagonal entry is an eigenvalue, [[Linear Algebra 5C Upper-Triangular Matrices#^ladr-5-41|5.41]]), so $m_\lambda=d_\lambda$ for each $\lambda$.

*Uses:* [[Linear dependence lemma|2.19]], [[Fundamental theorem of linear maps|3.21]], [[Linear Algebra 8B Generalized Eigenspace Decomposition#^ladr-8-25|8.25]], [[Linear Algebra 5C Upper-Triangular Matrices#^ladr-5-41|5.41]]

> [!definition] 8.35 Block diagonal matrix
> A *block diagonal matrix* is a square matrix $\begin{pmatrix}A_1&&0\\&\ddots&\\0&&A_m\end{pmatrix}$ with square blocks $A_k$ on the diagonal and zeros elsewhere.

^ladr-8-35

> [!remark] Meaning
> A block diagonal matrix of $T$ corresponds to a decomposition of $V$ into invariant subspaces, one per block.

> [!example] 8.36 A block diagonal matrix (p. 313)
> $$
> \begin{pmatrix}4&0&0&0&0\\0&2&-3&0&0\\0&0&2&0&0\\0&0&0&1&7\\0&0&0&0&1\end{pmatrix}
> $$
> is block diagonal with $A_1=(4)$, $A_2=\begin{pmatrix}2&-3\\0&2\end{pmatrix}$, $A_3=\begin{pmatrix}1&7\\0&1\end{pmatrix}$, each upper triangular with constant diagonal: the shape [[Linear Algebra 8B Generalized Eigenspace Decomposition#^ladr-8-37|8.37]] guarantees.

^ladr-8-36

> [!theorem] 8.37 Block diagonal matrix with upper-triangular blocks
> Let $\F=\C$, $T\in\Lin(V)$ with distinct eigenvalues $\lambda_1,\dots,\lambda_m$ of multiplicities $d_1,\dots,d_m$. In some basis $\mathcal{M}(T)$ is block diagonal with blocks
> $$
> A_k=\begin{pmatrix}\lambda_k&&*\\&\ddots&\\0&&\lambda_k\end{pmatrix}\qquad(d_k\text{-by-}d_k).
> $$

^ladr-8-37

> [!proof]+
> $(T-\lambda_kI)|_{G(\lambda_k,T)}$ is nilpotent ([[Generalized eigenspace decomposition|8.22]]); choose a basis of $G(\lambda_k,T)$ making it strictly upper triangular ([[Linear Algebra 8A Generalized Eigenvectors and Nilpotent Operators#^ladr-8-18|8.18]](c)). Then $T|_{G(\lambda_k,T)}=\lambda_kI+(T-\lambda_kI)|_{G(\lambda_k,T)}$ has the form $A_k$. Concatenate these bases ([[Generalized eigenspace decomposition|8.22]](c)).

*Uses:* [[Generalized eigenspace decomposition|8.22]], [[Linear Algebra 8A Generalized Eigenvectors and Nilpotent Operators#^ladr-8-18|8.18]]

> [!example] 8.38 Block diagonal matrix via generalized eigenvectors (p. 315)
> For $T$ of [[Linear Algebra 8B Generalized Eigenspace Decomposition#^ladr-8-24|8.24]], the basis $(1,0,0),(0,1,0),(10,2,1)$ of generalized eigenvectors gives
> $$
> \mathcal{M}(T)=\begin{pmatrix}6&3&0\\0&6&0\\0&0&7\end{pmatrix},
> $$
> block diagonal with blocks $\begin{pmatrix}6&3\\0&6\end{pmatrix}$ and $(7)$ (e.g. $T(0,1,0)=(3,6,0)$). Rescaling the second basis vector by $\frac13$ turns the $3$ into a $1$: a Jordan basis.

^ladr-8-38
