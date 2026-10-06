---
type: section
subject: "[[Linear Algebra]]"
chapter: 8
section: 28
aliases: ["LADR 8A", "8A Generalized Eigenvectors and Nilpotent Operators"]
tags: [linear-algebra]
---
← [[§27 Consequences of Singular Value Decomposition]] · ↑ [[· 8 Operators on Complex Vector Spaces]] · [[§29 Generalized Eigenspace Decomposition]] →

> [!remark] Remark: Standing assumptions for Chapter 8
> Throughout Chapter 8, $V$ is a finite-dimensional nonzero vector space over $\F$ ($\F$ is $\R$ or $\C$). These are Axler's standing assumptions for the chapter; the chapter's statements use them without repeating them.

> [!theorem] Theorem 8.1: Sequence of increasing null spaces
> For $T\in\Lin(V)$,
> $$
> \{0\}=\nullsp T^0\subseteq\nullsp T^1\subseteq\cdots\subseteq\nullsp T^k\subseteq\nullsp T^{k+1}\subseteq\cdots .
> $$

^ladr-8-1

> [!proof]+ Proof
> If $T^kv=0$ then $T^{k+1}v=T(T^kv)=0$.

> [!remark]- Connections
> - Stabilization: [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-2|8.2]], [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-3|8.3]]; figure after [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-3|8.3]].

> [!theorem] Theorem 8.2: Equality in the sequence of null spaces
> If $\nullsp T^m=\nullsp T^{m+1}$ for some $m\ge0$, then $\nullsp T^m=\nullsp T^{m+1}=\nullsp T^{m+2}=\cdots$.

^ladr-8-2

> [!remark] Remark: Slogan
> Once the chain pauses, it stops for good.

> [!proof]+ Proof
> Let $k\ge1$; we show $\nullsp T^{m+k+1}\subseteq\nullsp T^{m+k}$ (the other inclusion is [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-1|8.1]]). If $T^{m+k+1}v=0$ then $T^{m+1}(T^kv)=0$, so $T^kv\in\nullsp T^{m+1}=\nullsp T^m$, i.e. $T^{m+k}v=0$.

*Uses:* [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-1|8.1]]

> [!theorem] Theorem 8.3: Null spaces stop growing
> For $T\in\Lin(V)$,
> $$
> \nullsp T^{\dim V}=\nullsp T^{\dim V+1}=\nullsp T^{\dim V+2}=\cdots .
> $$

^ladr-8-3

> [!proof]+ Proof
> By [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-2|8.2]] it suffices that $\nullsp T^n=\nullsp T^{n+1}$ ($n=\dim V$). Otherwise, by [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-1|8.1]] and [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-2|8.2]], every inclusion $\nullsp T^0\subsetneq\dots\subsetneq\nullsp T^{n+1}$ is strict, each raising the dimension by at least $1$, so $\dim\nullsp T^{n+1}\ge n+1>\dim V$.

*Uses:* [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-2|8.2]], [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-1|8.1]]

%% ex:8.3-fig %%
> [!example] Example: The chain of null spaces, pictured
> For an operator on an $8$-dimensional space whose nilpotent part at $0$ has Jordan blocks of sizes $3,2,1$ (and which is invertible on a complementary $2$-dimensional piece), $\dim\nullsp T^k$ grows $0,3,5,6$ and then stops. The jumps $3,2,1$ (red) count the blocks of size $\ge1,\ge2,\ge3$.
>
> ![[ladr-8.3-null-chain.svg|420]]

%% ex:8.3-thm84 %%
> [!theorem] Theorem 8.4: $V=\nullsp T^{\dim V}\oplus\range T^{\dim V}$
> For $T\in\Lin(V)$ and $n=\dim V$: $\ V=\nullsp T^n\oplus\range T^n$.
>
> Substitute for $V=\nullsp T\oplus\range T$, which fails in general (see [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-6|8.6]]).

^ladr-8-4

> [!proof]+ Proof
> If $v\in\nullsp T^n\cap\range T^n$, then $v=T^nu$ and $0=T^nv=T^{2n}u$, so $T^nu=0$ by [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-3|8.3]], i.e. $v=0$. So the sum is direct ([[§3 Subspaces#^ladr-1-46|1.46]]), and its dimension is $\dim\nullsp T^n+\dim\range T^n=\dim V$ ([[Fundamental theorem of linear maps|3.21]]), so it is $V$.

*Uses:* [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-3|8.3]], [[§3 Subspaces#^ladr-1-46|1.46]], [[Fundamental theorem of linear maps|3.21]]

> [!example] Example 8.6: $\F^3=\nullsp T^3\oplus\range T^3$ (p. 299)
> $T(z_1,z_2,z_3)=(4z_2,0,5z_3)$ on $\F^3$: $\nullsp T=\{(z_1,0,0)\}$ and $\range T=\{(z_1,0,z_3)\}$ intersect, so $\nullsp T+\range T$ is not direct (and not $\F^3$). But $T^3(z_1,z_2,z_3)=(0,0,125z_3)$, so $\nullsp T^3=\{(z_1,z_2,0)\}$, $\range T^3=\{(0,0,z_3)\}$, and $\F^3=\nullsp T^3\oplus\range T^3$, as [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-4|8.4]] promises.

^ladr-8-6

%% ex:8.6-fig %%
> [!example] Example: Null spaces and ranges of $T$ and $T^3$, pictured
> Drawn over $\R$. Left: $\nullsp T$ (the $z_1$-axis) lies inside $\range T$ (the $z_1z_3$-plane), so the sum is not direct. Right: $\nullsp T^3$ (the $z_1z_2$-plane) and $\range T^3$ (the $z_3$-axis) are complementary, as [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-4|8.4]] promises. They are $G(0,T)$ and $G(5,T)$ of [[§29 Generalized Eigenspace Decomposition#^ladr-8-21|8.21]].
>
> ![[ladr-8.6-null-range.svg|460]]

> [!definition] Definition 8.8: Generalized eigenvector
> For an eigenvalue $\lambda$ of $T\in\Lin(V)$, a *generalized eigenvector* for $\lambda$ is a $v\ne0$ with $(T-\lambda I)^kv=0$ for some $k\ge1$. Equivalently $(T-\lambda I)^{\dim V}v=0$ ([[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-1|8.1]], [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-3|8.3]]).

^ladr-8-8

> [!remark] Remark: No generalized eigenvalues
> If $(T-\lambda I)^k$ is not injective, neither is $T-\lambda I$, so $\lambda$ is already an eigenvalue.

> [!remark]- Connections
> - Enough of them over $\C$: [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-9|8.9]]. Physics: in degenerate perturbation theory and in non-Hermitian (e.g. damped) systems, missing eigenvectors are replaced by generalized ones.
> - Computational version: [[§35 Eigenvectors and Linear Transformations#^ex-35-3|235 Ex. §35.3]] (a $2\times2$ matrix with a generalized eigenvector: $(A+2I)\mathbf b_2=\mathbf b_1$).
> - Computational version: [[§34★ Repeated Eigenvalues#^def-34-2|331 Def. §34.2]] (the case $k = 2$, used to solve $\mathbf{x}' = \mathbf{A}\mathbf{x}$ when an eigenvector is missing, [[§34★ Repeated Eigenvalues#^thm-34-2|331 Thm. §34.2]]).

> [!theorem] Theorem 8.9: A basis of generalized eigenvectors
> If $\F=\C$ and $T\in\Lin(V)$, then $V$ has a basis of generalized eigenvectors of $T$.

^ladr-8-9

> [!remark] Remark: Over $\R$
> False in general: rotation of $\R^2$ has no eigenvalues, hence no generalized eigenvectors.

> [!proof]+ Proof
> Induction on $n=\dim V$; $n=1$ uses that $T$ has an eigenvalue ($\F=\C$, [[Existence of eigenvalues|5.19]]). For $n>1$ let $\lambda$ be an eigenvalue. By [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-4|8.4]] applied to $T-\lambda I$,
> $$
> V=\nullsp(T-\lambda I)^n\oplus\range(T-\lambda I)^n .
> $$
> If the null space is $V$, every nonzero vector is a generalized eigenvector. Otherwise $0<\dim\range(T-\lambda I)^n<n$ (the null space contains an eigenvector). The range is invariant ([[§14 Invariant Subspaces#^ladr-5-18|5.18]]), so by induction it has a basis of generalized eigenvectors of $T$ restricted to it, hence of $T$. Adjoin a basis of $\nullsp(T-\lambda I)^n$.

*Uses:* [[Existence of eigenvalues|5.19]], [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-4|8.4]], [[§14 Invariant Subspaces#^ladr-5-18|5.18]]

> [!example] Example 8.10: Generalized eigenvectors of an operator on C³ (p. 302)
> Same $T$ on $\C^3$. Eigenvalues $0$ and $5$, with eigenvectors only $(z_1,0,0)$ and $(0,0,z_3)$: not enough to span. With $T^3(z)=(0,0,125z_3)$ and $(T-5I)^3(z)=(-125z_1+300z_2,\ -125z_2,\ 0)$ (verified):
> - generalized eigenvectors for $0$: $(z_1,z_2,0)\ne0$;
> - for $5$: $(0,0,z_3)\ne0$.
>
> The standard basis consists of generalized eigenvectors ([[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-9|8.9]]).

^ladr-8-10

> [!theorem] Theorem 8.11: Generalized eigenvector corresponds to a unique eigenvalue
> Each generalized eigenvector of $T$ corresponds to only one eigenvalue.

^ladr-8-11

> [!proof]+ Proof
> Let $v$ be generalized for $\alpha$ and $\lambda$, $m$ minimal with $(T-\alpha I)^mv=0$, $n=\dim V$. Expanding binomially,
> $$
> 0=(T-\lambda I)^nv=\big((T-\alpha I)+(\alpha-\lambda)I\big)^nv=\sum_{k=0}^n\binom nk(\alpha-\lambda)^{n-k}(T-\alpha I)^kv .
> $$
> Apply $(T-\alpha I)^{m-1}$: every term with $k\ge1$ dies, leaving $0=(\alpha-\lambda)^n(T-\alpha I)^{m-1}v$. As $(T-\alpha I)^{m-1}v\ne0$, $\alpha=\lambda$.

> [!theorem] Theorem 8.12: Linearly independent generalized eigenvectors
> Generalized eigenvectors of $T$ for distinct eigenvalues are linearly independent.

^ladr-8-12

> [!proof]+ Proof
> If not, take a dependent list $v_1,\dots,v_m$ (eigenvalues $\lambda_1,\dots,\lambda_m$ distinct) with $m$ minimal; then $\sum a_kv_k=0$ with all $a_k\ne0$. Apply $(T-\lambda_mI)^n$: $\sum_{k<m}a_k(T-\lambda_mI)^nv_k=0$. For $k<m$, $w_k=(T-\lambda_mI)^nv_k\ne0$ (else $v_k$ would be generalized for $\lambda_m$ too, contradicting [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-11|8.11]]), and $(T-\lambda_kI)^nw_k=(T-\lambda_mI)^n(T-\lambda_kI)^nv_k=0$. So $w_1,\dots,w_{m-1}$ is a shorter dependent list of generalized eigenvectors for distinct eigenvalues: contradiction.

*Uses:* [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-11|8.11]]

> [!remark]- Connections
> - Generalizes [[Linearly independent eigenvectors|5.11]]; gives directness in [[Generalized eigenspace decomposition|8.22]].

> [!definition] Definition 8.14: Nilpotent
> An operator is *nilpotent* if some power of it is $0$. Equivalently, every nonzero vector is a generalized eigenvector for $0$.

^ladr-8-14

> [!remark]- Connections
> - Physics: ladder operators on a finite spin multiplet ($S_+^{2s+1}=0$) are nilpotent; so are fermionic creation operators ($c^{\dagger2}=0$).

> [!example] Example 8.15: Nilpotent operators (p. 304)
> - (a) $T(z_1,z_2,z_3,z_4)=(0,0,z_1,z_2)$ on $\F^4$: $T^2=0$.
> - (b) $\begin{pmatrix}-3&9&0\\-7&9&6\\4&0&-6\end{pmatrix}$: its square is $\begin{pmatrix}-54&54&54\\-18&18&18\\-36&36&36\end{pmatrix}\ne0$ and its cube is $0$ (verified).
> - (c) Differentiation on $\Poly_m(\R)$: $D^{m+1}=0$, and $D^m\ne0$, so the bound $\dim V=m+1$ in [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-16|8.16]] is attained.

^ladr-8-15

> [!theorem] Theorem 8.16: Nilpotent operator raised to dimension of domain is 0
> If $T\in\Lin(V)$ is nilpotent, then $T^{\dim V}=0$.

^ladr-8-16

> [!proof]+ Proof
> $\nullsp T^k=V$ for some $k$, so $\nullsp T^{\dim V}=V$ by [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-1|8.1]] and [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-3|8.3]].

*Uses:* [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-1|8.1]], [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-3|8.3]]

> [!theorem] Theorem 8.17: Eigenvalues of nilpotent operator
> (a) If $T$ is nilpotent, $0$ is an eigenvalue and the only one. (b) If $\F=\C$ and $0$ is the only eigenvalue of $T$, then $T$ is nilpotent.

^ladr-8-17

> [!remark] Remark: (b) needs $\C$
> Over $\R$, an operator on $\R^3$ acting as $0$ on a line and as a rotation on the complementary plane has only the eigenvalue $0$ but is not nilpotent.

> [!proof]+ Proof
> (a) $T^m=0$ makes $T$ non-injective. If $Tv=\lambda v$, $v\ne0$, then $\lambda^mv=T^mv=0$, so $\lambda=0$. (b) The minimal polynomial has only the zero $0$ ([[§15 The Minimal Polynomial#^ladr-5-27|5.27]]) and splits over $\C$, so it is $z^m$ and $T^m=0$.

*Uses:* [[§15 The Minimal Polynomial#^ladr-5-27|5.27]]

> [!theorem] Theorem 8.18: Minimal polynomial and upper-triangular matrix of nilpotent operator
> For $T\in\Lin(V)$, equivalent:
> - (a) $T$ is nilpotent;
> - (b) the minimal polynomial of $T$ is $z^m$ for some $m\ge1$;
> - (c) in some basis, $\mathcal{M}(T)$ is upper triangular with zero diagonal.

^ladr-8-18

> [!proof]+ Proof
> (a)$\Rightarrow$(b): $T^n=0$, so the minimal polynomial divides $z^n$ ([[§15 The Minimal Polynomial#^ladr-5-29|5.29]]). (b)$\Rightarrow$(c): $0$ is the only eigenvalue ([[§15 The Minimal Polynomial#^ladr-5-27|5.27]]), the minimal polynomial splits, so $T$ is upper triangular ([[§16 Upper-Triangular Matrices#^ladr-5-44|5.44]]) with diagonal entries the eigenvalues ([[§16 Upper-Triangular Matrices#^ladr-5-41|5.41]]), all $0$. (c)$\Rightarrow$(a): $T^{\dim V}=0$ by [[§16 Upper-Triangular Matrices#^ladr-5-40|5.40]].

*Uses:* [[§15 The Minimal Polynomial#^ladr-5-29|5.29]], [[§15 The Minimal Polynomial#^ladr-5-27|5.27]], [[§16 Upper-Triangular Matrices#^ladr-5-44|5.44]], [[§16 Upper-Triangular Matrices#^ladr-5-41|5.41]], [[§16 Upper-Triangular Matrices#^ladr-5-40|5.40]]

