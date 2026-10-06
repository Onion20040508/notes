---
type: section
subject: "[[Linear Algebra]]"
chapter: 5
section: 17
aliases: ["LADR 5D", "5D Diagonalizable Operators"]
tags: [linear-algebra]
---
← [[§16 Upper-Triangular Matrices]] · ↑ [[· 5 Eigenvalues and Eigenvectors]] · [[§18 Commuting Operators]] →

> [!definition] Definition 5.48: Diagonal matrix
> A *diagonal matrix* is a square matrix that is $0$ everywhere except possibly on the diagonal.

^ladr-5-48

> [!remark]- Connections
> - Diagonal matrices commute with each other; powers are computed entrywise ([[§17 Diagonalizable Operators#^ladr-5-59|5.59]]).

> [!example] Example 5.49: Diagonal matrix (p. 163)
> $\begin{pmatrix}8&0&0\\0&5&0\\0&0&5\end{pmatrix}$ is diagonal. Every diagonal matrix is upper triangular, and its diagonal entries are the eigenvalues (here $8$ and $5$).

^ladr-5-49

> [!definition] Definition 5.50: Diagonalizable
> $T\in\Lin(V)$ is *diagonalizable* if $T$ has a diagonal matrix with respect to some basis of $V$.

^ladr-5-50

> [!remark]- Connections
> - Equivalent conditions: [[§17 Diagonalizable Operators#^ladr-5-55|5.55]], [[§17 Diagonalizable Operators#^ladr-5-62|5.62]]. Sufficient condition: [[§17 Diagonalizable Operators#^ladr-5-58|5.58]]. Physics: diagonalizing a Hamiltonian = finding a basis of stationary states.
> - Computational version: [[§34 Diagonalization#^def-34-1|235 Def. §34.1]] ($A=PDP^{-1}$) and [[§35 Eigenvectors and Linear Transformations#^thm-35-2|235 Thm. §35.2]] ($D$ is then the matrix of $\mathbf x\mapsto A\mathbf x$ in the basis of columns of $P$).

> [!example] Example 5.51: Diagonalization may require a different basis (p. 163)
> $T(x,y)=(41x+7y,\ -20x+74y)$ on $\R^2$ has standard matrix $\begin{pmatrix}41&7\\-20&74\end{pmatrix}$, not diagonal. But
> $$
> T(1,4)=(69,276)=69\,(1,4),\qquad T(7,5)=(322,230)=46\,(7,5),
> $$
> so in the basis $(1,4),(7,5)$, $\mathcal{M}(T)=\begin{pmatrix}69&0\\0&46\end{pmatrix}$. Diagonalizing means finding the right basis, not changing the operator.

^ladr-5-51

> [!definition] Definition 5.52: Eigenspace, E(λ, T)
> For $T\in\Lin(V)$ and $\lambda\in\F$, the *eigenspace*
> $$
> E(\lambda,T)=\nullsp(T-\lambda I)=\{v\in V:Tv=\lambda v\}.
> $$
> It is a subspace; $\lambda$ is an eigenvalue iff $E(\lambda,T)\ne\{0\}$, and $T$ acts on $E(\lambda,T)$ as multiplication by $\lambda$.

^ladr-5-52

> [!remark]- Connections
> - Eigenspaces form a direct sum: [[§17 Diagonalizable Operators#^ladr-5-54|5.54]]. Invariant under commuting operators: [[§18 Commuting Operators#^ladr-5-75|5.75]]. Physics: the degenerate subspace of an energy level.
> - Computational version: [[§32 Eigenvectors and Eigenvalues#^def-32-2|235 Def. §32.2]] (the eigenspace $\operatorname{Nul}(A-\lambda I)$, with bases found by row reduction).

> [!example] Example 5.53: Eigenspaces of an operator (p. 164)
> If $T$ has the matrix of [[§17 Diagonalizable Operators#^ladr-5-49|5.49]] in a basis $v_1,v_2,v_3$, then
> $$
> E(8,T)=\Span(v_1),\qquad E(5,T)=\Span(v_2,v_3).
> $$
> The eigenvalue $5$ has a $2$-dimensional eigenspace ('degenerate', in physics language).

^ladr-5-53

> [!theorem] Theorem 5.54: Sum of eigenspaces is a direct sum
> Let $T\in\Lin(V)$ with distinct eigenvalues $\lambda_1,\dots,\lambda_m$. Then $E(\lambda_1,T)+\dots+E(\lambda_m,T)$ is a direct sum, and if $V$ is finite-dimensional,
> $$
> \dim E(\lambda_1,T)+\dots+\dim E(\lambda_m,T)\le\dim V .
> $$

^ladr-5-54

> [!proof]+ Proof
> If $v_1+\dots+v_m=0$ with $v_k\in E(\lambda_k,T)$, the nonzero $v_k$ would be eigenvectors for distinct eigenvalues, hence independent ([[Linearly independent eigenvectors|5.11]]); so all $v_k=0$ and the sum is direct ([[Condition for a direct sum|1.45]]). Then $\sum\dim E(\lambda_k,T)=\dim\bigoplus E(\lambda_k,T)\le\dim V$ by [[§11 Products and Quotients of Vector Spaces#^ladr-3-94|3.94]] and [[§6 Dimension#^ladr-2-37|2.37]].

*Uses:* [[Linearly independent eigenvectors|5.11]], [[Condition for a direct sum|1.45]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-94|3.94]], [[§6 Dimension#^ladr-2-37|2.37]]

> [!remark]- Connections
> - Equality is diagonalizability: [[§17 Diagonalizable Operators#^ladr-5-55|5.55]]. Generalized version: [[Generalized eigenspace decomposition|8.22]].

> [!theorem] Theorem 5.55: Conditions equivalent to diagonalizability
> Let $V$ be finite-dimensional, $T\in\Lin(V)$, with distinct eigenvalues $\lambda_1,\dots,\lambda_m$. Equivalent:
> - (a) $T$ is diagonalizable;
> - (b) $V$ has a basis of eigenvectors of $T$;
> - (c) $V=E(\lambda_1,T)\oplus\dots\oplus E(\lambda_m,T)$;
> - (d) $\dim V=\dim E(\lambda_1,T)+\dots+\dim E(\lambda_m,T)$.

^ladr-5-55

> [!proof]+ Proof
> (a)$\iff$(b): the matrix in the basis $v_1,\dots,v_n$ is diagonal iff each $Tv_k=\lambda_kv_k$.
>
> (b)$\Rightarrow$(c): every vector is a sum of eigenvectors, so $V=\sum E(\lambda_k,T)$, which is direct by [[§17 Diagonalizable Operators#^ladr-5-54|5.54]].
>
> (c)$\Rightarrow$(d): [[§11 Products and Quotients of Vector Spaces#^ladr-3-94|3.94]].
>
> (d)$\Rightarrow$(b): concatenate bases of the $E(\lambda_k,T)$ into a list of $\dim V$ eigenvectors. If $\sum a_jv_j=0$, group the terms by eigenspace: $u_1+\dots+u_m=0$ with $u_k\in E(\lambda_k,T)$, so each $u_k=0$ ([[Linearly independent eigenvectors|5.11]]), and then each group's coefficients vanish (basis of $E(\lambda_k,T)$). So the list is independent of length $\dim V$, a basis ([[§6 Dimension#^ladr-2-38|2.38]]).

*Uses:* [[§17 Diagonalizable Operators#^ladr-5-54|5.54]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-94|3.94]], [[Linearly independent eigenvectors|5.11]], [[§6 Dimension#^ladr-2-38|2.38]]

> [!remark]- Connections
> - Minimal-polynomial criterion: [[§17 Diagonalizable Operators#^ladr-5-62|5.62]]. Failure: [[§17 Diagonalizable Operators#^ladr-5-57|5.57]].
> - Computational version: [[§34 Diagonalization#^thm-34-1|235 Thm. §34.1]] (diagonalizable iff there are $n$ independent eigenvectors) and [[§34 Diagonalization#^thm-34-3|235 Thm. §34.3]] (iff the eigenspace dimensions add up to $n$), with worked diagonalizations.
> - Computational version: diagonalization $\mathbf{T}^{-1}\mathbf{A}\mathbf{T} = \mathbf{D}$ by a matrix of eigenvectors, used to uncouple $\mathbf{x}' = \mathbf{A}\mathbf{x}$, [[§33★ Fundamental Matrices#^thm-33-7|331 Thm. §33.7]].

> [!example] Example 5.57: An operator that is not diagonalizable (p. 166)
> $T(a,b,c)=(b,c,0)$ on $\F^3$, with $\mathcal{M}(T)=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}$ (upper triangular, not diagonal). Its only eigenvalue is $0$ ([[§16 Upper-Triangular Matrices#^ladr-5-41|5.41]]), and $E(0,T)=\{(a,0,0)\}$ is $1$-dimensional $<3$. So (d) of [[§17 Diagonalizable Operators#^ladr-5-55|5.55]] fails and $T$ is not diagonalizable, over $\R$ and over $\C$.
>
> The same failure in the plane: the shear $(x,y)\mapsto(x+y,y)$ has only the eigenvalue $1$ and only one invariant line, the $x$-axis.
>
> ![[ladr-5.57-shear.svg|400]]

^ladr-5-57

> [!theorem] Theorem 5.58: Enough eigenvalues implies diagonalizability
> If $V$ is finite-dimensional and $T\in\Lin(V)$ has $\dim V$ distinct eigenvalues, then $T$ is diagonalizable.

^ladr-5-58

> [!remark] Remark: Sufficient, not necessary
> $T(x,y,z)=(6x,6y,7z)$ has only two eigenvalues but is diagonal in the standard basis. Generic matrices have distinct eigenvalues, so 'most' operators over $\C$ are diagonalizable.

> [!proof]+ Proof
> One eigenvector per eigenvalue gives $\dim V$ vectors, independent by [[Linearly independent eigenvectors|5.11]], hence a basis ([[§6 Dimension#^ladr-2-38|2.38]]); $T$ is diagonal in it.

*Uses:* [[Linearly independent eigenvectors|5.11]], [[§6 Dimension#^ladr-2-38|2.38]]

> [!remark]- Connections
> - Used in [[§17 Diagonalizable Operators#^ladr-5-59|5.59]]. Other sufficient conditions: the spectral theorems [[Real spectral theorem|7.29]], [[Complex spectral theorem|7.31]].
> - Computational version: [[§34 Diagonalization#^thm-34-2|235 Thm. §34.2]] (an $n\times n$ matrix with $n$ distinct eigenvalues is diagonalizable).

> [!example] Example 5.59: Using diagonalization to compute T¹⁰⁰ (p. 167)
> $T(x,y,z)=(2x+y,\ 5y+3z,\ 8z)$ has eigenvalues $2,5,8$ ([[§16 Upper-Triangular Matrices#^ladr-5-42|5.42]]): three distinct, so diagonalizable ([[§17 Diagonalizable Operators#^ladr-5-58|5.58]]). Eigenvectors: $(1,0,0)$, $(1,3,0)$, $(1,6,6)$.
>
> To compute $T^{100}(0,0,1)$, expand in the eigenbasis:
> $$
> (0,0,1)=\tfrac16(1,0,0)-\tfrac13(1,3,0)+\tfrac16(1,6,6),
> $$
> then apply $T^{100}$ termwise:
> $$
> T^{100}(0,0,1)=\tfrac16\big(2^{100}-2\cdot5^{100}+8^{100},\ 6\cdot8^{100}-6\cdot5^{100},\ 6\cdot8^{100}\big).
> $$
> (Checked with exponent $3$ in place of $100$.) The same idea gives a closed formula for the Fibonacci numbers ([[§5 The Induction Principle#^def-5-5|250 Def. §5.5]]), the Binet formula, proved by induction in [[§5 The Induction Principle#^prop-5-8|250 Prop. §5.8]].

^ladr-5-59

> [!remark]- Connections
> - Computational version: [[§34 Diagonalization#^ex-34-1|235 Ex. §34.1]] ($A^k=PD^kP^{-1}$ for a $2\times2$ matrix); the Fibonacci formula by the same idea, [[§30 Applications to Difference Equations#^ex-30-4|235 Ex. §30.4]].

> [!example] Example 5.60: Diagonalizable, but with no known exact eigenvalues (p. 168)
> The operator of [[§15 The Minimal Polynomial#^ladr-5-28|5.28]] on $\C^5$ has minimal polynomial $z^5-6z+3$, whose five zeros are numerically distinct ($\approx-1.67,\ 0.51,\ 1.40,\ -0.12\pm1.59i$). Distinct roots, so it is diagonalizable ([[§17 Diagonalizable Operators#^ladr-5-62|5.62]]), although no eigenvalue has an exact formula.

^ladr-5-60

> [!example] Example 5.61: Showing that an operator is not diagonalizable (p. 168)
> $T(z_1,z_2,z_3)=(6z_1+3z_2+4z_3,\ 6z_2+2z_3,\ 7z_3)$, $\mathcal{M}(T)=\begin{pmatrix}6&3&4\\0&6&2\\0&0&7\end{pmatrix}$.
>
> Eigenvalues $6,7$ ([[§16 Upper-Triangular Matrices#^ladr-5-41|5.41]]), and $(T-6I)^2(T-7I)=0$ ([[§16 Upper-Triangular Matrices#^ladr-5-40|5.40]]). So the minimal polynomial is $(z-6)(z-7)$ or $(z-6)^2(z-7)$. Computing,
> $$
> (T-6I)(T-7I)=\begin{pmatrix}0&-3&6\\0&0&0\\0&0&0\end{pmatrix}\ne0,
> $$
> so it is $(z-6)^2(z-7)$, with a repeated root: not diagonalizable ([[§17 Diagonalizable Operators#^ladr-5-62|5.62]]).

^ladr-5-61

> [!theorem] Theorem 5.62: Necessary and sufficient condition for diagonalizability
> Let $V$ be finite-dimensional and $T\in\Lin(V)$. Then $T$ is diagonalizable iff the minimal polynomial of $T$ equals $(z-\lambda_1)\cdots(z-\lambda_m)$ for some list of **distinct** $\lambda_1,\dots,\lambda_m\in\F$.

^ladr-5-62

> [!remark] Remark: How to use it
> To test diagonalizability, compute the minimal polynomial and check for repeated roots ([[§17 Diagonalizable Operators#^ladr-5-61|5.61]]). Over $\C$: $T$ is diagonalizable iff $p(T)=0$ for some polynomial $p$ with distinct roots, e.g. $T^k=I$ implies diagonalizable.

> [!proof]+ Proof
> ($\Rightarrow$) With a basis of eigenvectors and distinct eigenvalues $\lambda_1,\dots,\lambda_m$, every basis vector is killed by some $T-\lambda_kI$, hence by $(T-\lambda_1I)\cdots(T-\lambda_mI)$ (factors commute). So this product is $0$; it is the minimal polynomial since every eigenvalue must be a zero of the minimal polynomial ([[§15 The Minimal Polynomial#^ladr-5-27|5.27]]).
>
> ($\Leftarrow$) Induction on $m$; $m=1$ means $T=\lambda_1I$. For $m>1$, $U=\range(T-\lambda_mI)$ is invariant ([[§14 Invariant Subspaces#^ladr-5-18|5.18]]) and $(T-\lambda_1I)\cdots(T-\lambda_{m-1}I)$ kills $U$, so by [[§15 The Minimal Polynomial#^ladr-5-29|5.29]] and induction $U$ has a basis of eigenvectors of $T$. If $u\in U\cap\nullsp(T-\lambda_mI)$, then $Tu=\lambda_mu$ and
> $$
> 0=(T-\lambda_1I)\cdots(T-\lambda_{m-1}I)u=(\lambda_m-\lambda_1)\cdots(\lambda_m-\lambda_{m-1})u ,
> $$
> so $u=0$ (distinctness). Thus $U+\nullsp(T-\lambda_mI)$ is direct, and by [[Fundamental theorem of linear maps|3.21]] its dimension is $\dim V$, so $V=U\oplus E(\lambda_m,T)$. Combining the eigenvector basis of $U$ with a basis of $E(\lambda_m,T)$ gives a basis of eigenvectors of $V$.

*Uses:* [[§15 The Minimal Polynomial#^ladr-5-27|5.27]], [[§14 Invariant Subspaces#^ladr-5-18|5.18]], [[§15 The Minimal Polynomial#^ladr-5-29|5.29]], [[Fundamental theorem of linear maps|3.21]]

> [!remark]- Connections
> - Restrictions stay diagonalizable: [[§17 Diagonalizable Operators#^ladr-5-65|5.65]]. Non-diagonalizable operators are handled by Jordan form ([[Jordan form|8.46]]).

> [!theorem] Theorem 5.65: Restriction of diagonalizable operator to invariant subspace
> If $T\in\Lin(V)$ is diagonalizable and $U$ is invariant under $T$, then $T|_U$ is diagonalizable.

^ladr-5-65

> [!proof]+ Proof
> The minimal polynomial of $T$ is $(z-\lambda_1)\cdots(z-\lambda_m)$ with distinct $\lambda_k$ ([[§17 Diagonalizable Operators#^ladr-5-62|5.62]]); the minimal polynomial of $T|_U$ divides it ([[§15 The Minimal Polynomial#^ladr-5-31|5.31]]), so it has the same form, and [[§17 Diagonalizable Operators#^ladr-5-62|5.62]] applies to $T|_U$.

*Uses:* [[§17 Diagonalizable Operators#^ladr-5-62|5.62]], [[§15 The Minimal Polynomial#^ladr-5-31|5.31]]

> [!remark]- Connections
> - Key step in simultaneous diagonalization [[§18 Commuting Operators#^ladr-5-76|5.76]].

> [!definition] Definition 5.66: Gershgorin disks
> Let $T\in\Lin(V)$ with matrix $A$ in a basis $v_1,\dots,v_n$. The *Gershgorin disks* of $T$ (for this basis) are
> $$
> \Big\{z\in\F:\ |z-A_{j,j}|\le\sum_{k\ne j}|A_{j,k}|\Big\},\qquad j=1,\dots,n :
> $$
> centered at a diagonal entry, with radius the sum of the other absolute values in that row.

^ladr-5-66

> [!remark] Remark: Over $\R$
> The disks are closed intervals. For a diagonal matrix they are single points.

> [!remark]- Connections
> - Contain all eigenvalues: [[§17 Diagonalizable Operators#^ladr-5-67|5.67]].

> [!theorem] Theorem 5.67: Gershgorin disk theorem
> For $T\in\Lin(V)$ and any basis $v_1,\dots,v_n$, every eigenvalue of $T$ lies in some Gershgorin disk of $T$ with respect to that basis.

^ladr-5-67

> [!remark] Remark: Use and a sharper version
> Small off-diagonal entries force eigenvalues near the diagonal entries. Columns may replace rows (apply the theorem to the transpose). A sharper statement, not proved in Axler, says a union of $k$ disks disjoint from the others contains exactly $k$ eigenvalues.

> [!proof]+ Proof
> Let $Tw=\lambda w$, $w=\sum c_kv_k\ne0$, and $A=\mathcal{M}(T)$. Comparing coefficients of $v_j$ in $\lambda w=\sum_kc_kTv_k=\sum_j\big(\sum_kA_{j,k}c_k\big)v_j$ gives $\lambda c_j=\sum_kA_{j,k}c_k$. Choose $j$ with $|c_j|$ maximal (so $c_j\ne0$). Then
> $$
> |\lambda-A_{j,j}|=\Big|\sum_{k\ne j}A_{j,k}\frac{c_k}{c_j}\Big|\le\sum_{k\ne j}|A_{j,k}| .
> $$

> [!remark]- Connections
> - Diagonally dominant matrices ($|A_{j,j}|>\sum_{k\ne j}|A_{j,k}|$ for all $j$) have no eigenvalue $0$, hence are invertible ([[§14 Invariant Subspaces#^ladr-5-7|5.7]]).

%% ex:5.67-disks %%
> [!example] Example: Gershgorin disks of a $3\times3$ matrix
> For $A=\begin{pmatrix}1&2&0\\-2&1&0.5\\0.5&0.5&-4\end{pmatrix}$ the disks are centered at $1$ (radius $2$), $1$ (radius $2.5$), and $-4$ (radius $1$). The eigenvalues are approximately $1.01\pm1.97i$ and $-4.03$, each inside a disk:
>
> ![[ladr-5.67-gershgorin.svg|420]]

