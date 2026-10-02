---
type: section
subject: "[[Linear Algebra]]"
chapter: 5
section: 18
aliases: ["LADR 5E", "5E Commuting Operators"]
tags: [linear-algebra]
---
← [[§17 Diagonalizable Operators]] · ↑ [[· 5 Eigenvalues and Eigenvectors]] · [[§19 Inner Products and Norms]] →

> [!definition] Definition 5.71: Commute
> Operators $S,T$ on the same space *commute* if $ST=TS$; square matrices $A,B$ commute if $AB=BA$.

^ladr-5-71

> [!remark] Remark: Rare
> Polynomials in one operator commute ([[§14 Invariant Subspaces#^ladr-5-17|5.17]]), and $I$ commutes with everything, but random pairs almost never commute (Axler: about $0.3\%$ of integer $2\times2$ pairs with entries in $[-5,5]$).

> [!remark]- Connections
> - Physics: commuting observables can be measured simultaneously; they share an eigenbasis ([[§18 Commuting Operators#^ladr-5-76|5.76]]).

> [!example] Example 5.72: Partial differentiation operators commute (p. 175)
> On $\Poly_m(\R^2)$ (real polynomials $\sum_{j+k\le m}a_{j,k}x^jy^k$), the partial derivatives $D_x,D_y$ commute:
> $$
> D_xD_yp=\sum jk\,a_{j,k}x^{j-1}y^{k-1}=D_yD_xp .
> $$
> This is the polynomial case of the symmetry of mixed partials.

^ladr-5-72

> [!theorem] Theorem 5.74: Commuting operators correspond to commuting matrices
> Let $S,T\in\Lin(V)$ and $v_1,\dots,v_n$ a basis. Then $S,T$ commute iff $\mathcal{M}(S)$ and $\mathcal{M}(T)$ (same basis) commute.

^ladr-5-74

> [!proof]+ Proof
> $ST=TS\iff\mathcal{M}(ST)=\mathcal{M}(TS)\iff\mathcal{M}(S)\mathcal{M}(T)=\mathcal{M}(T)\mathcal{M}(S)$, by [[§9 Matrices#^ladr-3-43|3.43]] and the injectivity of $T\mapsto\mathcal{M}(T)$ (an isomorphism; see the proof of [[§10 Invertibility and Isomorphisms#^ladr-3-72|3.72]]).

*Uses:* [[§9 Matrices#^ladr-3-43|3.43]], [[§10 Invertibility and Isomorphisms#^ladr-3-72|3.72]]

> [!remark]- Connections
> - Used in [[§18 Commuting Operators#^ladr-5-76|5.76]].

> [!theorem] Theorem 5.75: Eigenspace is invariant under commuting operator
> If $S,T\in\Lin(V)$ commute and $\lambda\in\F$, then $E(\lambda,S)$ is invariant under $T$.

^ladr-5-75

> [!proof]+ Proof
> For $Sv=\lambda v$: $S(Tv)=T(Sv)=\lambda Tv$, so $Tv\in E(\lambda,S)$.

> [!remark]- Connections
> - The engine of 5E: [[§18 Commuting Operators#^ladr-5-76|5.76]], [[§18 Commuting Operators#^ladr-5-78|5.78]]. Physics: a symmetry commuting with $H$ maps each energy eigenspace to itself, which is why degeneracies organize into representations of the symmetry group.

> [!theorem] Theorem 5.76: Simultaneous diagonalizablity ⟺ commutativity
> Two diagonalizable operators on the same space are diagonal with respect to a common basis iff they commute.

^ladr-5-76

> [!proof]+ Proof
> ($\Rightarrow$) Diagonal matrices commute; use [[§18 Commuting Operators#^ladr-5-74|5.74]].
>
> ($\Leftarrow$) Let $\lambda_1,\dots,\lambda_m$ be the distinct eigenvalues of $S$, so $V=E(\lambda_1,S)\oplus\dots\oplus E(\lambda_m,S)$ ([[§17 Diagonalizable Operators#^ladr-5-55|5.55]]). Each $E(\lambda_k,S)$ is invariant under $T$ ([[§18 Commuting Operators#^ladr-5-75|5.75]]), and $T$ restricted to it is diagonalizable ([[§17 Diagonalizable Operators#^ladr-5-65|5.65]]). A basis of each $E(\lambda_k,S)$ of eigenvectors of $T$ consists of common eigenvectors; together they form a basis of $V$.

*Uses:* [[§18 Commuting Operators#^ladr-5-74|5.74]], [[§17 Diagonalizable Operators#^ladr-5-55|5.55]], [[§18 Commuting Operators#^ladr-5-75|5.75]], [[§17 Diagonalizable Operators#^ladr-5-65|5.65]]

> [!remark]- Connections
> - Physics: a complete set of commuting observables labels a basis by their joint eigenvalues. Orthonormal version for normal operators: the spectral theorems [[Real spectral theorem|7.29]], [[Complex spectral theorem|7.31]].
> - Used in Quantum Mechanics: a complete set of commuting observables labels a basis of simultaneous eigenkets — [[§C1.3 Measurements, Compatible Observables and Uncertainty#^thm-c1-3-2|QM Theorem §C1.3.2]].

%% ex:5.76-fig %%
> [!example] Example: The proof of 5.76, pictured
> Let $S$ have the diagonal matrix $\operatorname{diag}(8,5,5)$ of [[§17 Diagonalizable Operators#^ladr-5-49|5.49]] in a basis $v_1,v_2,v_3$, so $E(8,S)=\Span(v_1)$ and $E(5,S)=\Span(v_2,v_3)$ ([[§17 Diagonalizable Operators#^ladr-5-53|5.53]]). Let $T$ have matrix $\begin{pmatrix}4&0&0\\0&2&1\\0&1&2\end{pmatrix}$ in the same basis; then $ST=TS$. $T$ maps each eigenspace of $S$ into itself ([[§18 Commuting Operators#^ladr-5-75|5.75]]), and inside the plane $E(5,S)$ it has the eigenvectors $v_2+v_3$ (eigenvalue $3$) and $v_2-v_3$ (eigenvalue $1$). With $v_1$ they form a common eigenbasis (red).
>
> ![[ladr-5.76-common-eigenbasis.svg|380]]

> [!theorem] Theorem 5.78: Common eigenvector for commuting operators
> Two commuting operators on a finite-dimensional nonzero complex vector space have a common eigenvector.

^ladr-5-78

> [!remark] Remark: Common eigenvector, not eigenvalue
> The two operators need not share an eigenvalue; only the vector is common.

> [!proof]+ Proof
> Let $\lambda$ be an eigenvalue of $S$ ([[Existence of eigenvalues|5.19]]), so $E(\lambda,S)\ne\{0\}$. It is invariant under $T$ ([[§18 Commuting Operators#^ladr-5-75|5.75]]), so $T|_{E(\lambda,S)}$ has an eigenvector ([[Existence of eigenvalues|5.19]]); it is an eigenvector of both.

*Uses:* [[Existence of eigenvalues|5.19]], [[§18 Commuting Operators#^ladr-5-75|5.75]]

> [!remark]- Connections
> - Starts the induction in [[§18 Commuting Operators#^ladr-5-80|5.80]].
> - Group-theoretic use: a common eigenvector of a group of operators gives a character, [[§41 Characters#^thm-41-2|493 Thm. §41.2]].

> [!example] Example 5.79: Common eigenvector for partial differentiation operators (p. 177)
> $D_x,D_y$ of [[§18 Commuting Operators#^ladr-5-72|5.72]] have only the eigenvalue $0$, with
> $$
> E(0,D_x)=\Big\{\sum_ka_ky^k\Big\},\qquad E(0,D_y)=\Big\{\sum_jc_jx^j\Big\}.
> $$
> Their intersection, the common eigenvectors, is the constants, as [[§18 Commuting Operators#^ladr-5-78|5.78]] guarantees (here over $\R$, which works because the eigenvalue $0$ is real).

^ladr-5-79

> [!theorem] Theorem 5.80: Commuting operators are simultaneously upper triangularizable
> If $V$ is a finite-dimensional complex vector space and $S,T\in\Lin(V)$ commute, there is a basis of $V$ in which both $S$ and $T$ are upper triangular.

^ladr-5-80

> [!proof]+ Proof
> Induction on $n=\dim V$; $n=1$ is trivial. Let $v_1$ be a common eigenvector ([[§18 Commuting Operators#^ladr-5-78|5.78]]) and $V=\Span(v_1)\oplus W$ ([[§5 Bases#^ladr-2-33|2.33]]). Let $P:V\to W$, $P(av_1+w)=w$, and $\hat S=PS|_W$, $\hat T=PT|_W\in\Lin(W)$.
>
> **$\hat S,\hat T$ commute.** For $w\in W$, $Tw=av_1+\hat Tw$ for some $a$, so $\hat S\hat Tw=P S(Tw-av_1)=P(STw)$ since $Sv_1\in\Span(v_1)$ and $Pv_1=0$. Similarly $\hat T\hat Sw=P(TSw)$, and $ST=TS$.
>
> By induction $W$ has a basis $v_2,\dots,v_n$ making $\hat S,\hat T$ upper triangular. For $k\ge2$, $Sv_k=a_kv_1+\hat Sv_k$ with $\hat Sv_k\in\Span(v_2,\dots,v_k)$, so $Sv_k\in\Span(v_1,\dots,v_k)$; likewise for $T$, and $Sv_1,Tv_1\in\Span(v_1)$. By [[§16 Upper-Triangular Matrices#^ladr-5-39|5.39]] both are upper triangular in $v_1,\dots,v_n$.

*Uses:* [[§18 Commuting Operators#^ladr-5-78|5.78]], [[§5 Bases#^ladr-2-33|2.33]], [[§16 Upper-Triangular Matrices#^ladr-5-39|5.39]]

> [!remark]- Connections
> - Extends [[If F = C, then every operator on V has an upper-triangular matrix|5.47]] to commuting pairs. Consequence: [[§18 Commuting Operators#^ladr-5-81|5.81]].

> [!theorem] Theorem 5.81: Eigenvalues of sum and product of commuting operators
> Let $V$ be a finite-dimensional complex vector space and $S,T\in\Lin(V)$ commute. Then every eigenvalue of $S+T$ is an eigenvalue of $S$ plus an eigenvalue of $T$, and every eigenvalue of $ST$ is an eigenvalue of $S$ times an eigenvalue of $T$.

^ladr-5-81

> [!remark] Remark: Commutativity is needed
> $S=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $T=\begin{pmatrix}0&0\\1&0\end{pmatrix}$ have only the eigenvalue $0$, but $S+T$ has eigenvalues $\pm1$.

> [!proof]+ Proof
> In a basis making both upper triangular ([[§18 Commuting Operators#^ladr-5-80|5.80]]), $\mathcal{M}(S+T)=\mathcal{M}(S)+\mathcal{M}(T)$ and $\mathcal{M}(ST)=\mathcal{M}(S)\mathcal{M}(T)$ ([[§9 Matrices#^ladr-3-35|3.35]], [[§9 Matrices#^ladr-3-43|3.43]]) are upper triangular, with diagonals the entrywise sums and products. By [[§16 Upper-Triangular Matrices#^ladr-5-41|5.41]], eigenvalues are diagonal entries in each case.

*Uses:* [[§18 Commuting Operators#^ladr-5-80|5.80]], [[§9 Matrices#^ladr-3-35|3.35]], [[§9 Matrices#^ladr-3-43|3.43]], [[§16 Upper-Triangular Matrices#^ladr-5-41|5.41]]

> [!remark]- Connections
> - Physics: for commuting observables, eigenvalues of $A+B$ are sums of joint eigenvalues (e.g. total angular momentum $J_z=L_z+S_z$).

