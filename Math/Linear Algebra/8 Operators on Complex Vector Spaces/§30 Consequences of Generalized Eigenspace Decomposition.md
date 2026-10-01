---
type: section
subject: "[[Linear Algebra]]"
chapter: 8
section: 30
aliases: ["LADR 8C", "8C Consequences of Generalized Eigenspace Decomposition"]
tags: [linear-algebra]
---
← [[§29 Generalized Eigenspace Decomposition]] · ↑ [[· 8 Operators on Complex Vector Spaces]] · [[§31 Trace꞉ A Connection Between Matrices and Operators]] →

> [!theorem] 8.39 Identity plus nilpotent has a square root
> If $T$ is nilpotent, then $I+T$ has a square root.

^ladr-8-39

> [!remark] Why it works
> Nilpotency truncates the power series, so there are no convergence questions.

> [!proof]+
> Motivated by $\sqrt{1+x}=1+\frac12x-\frac18x^2+\frac1{16}x^3-\cdots$, look for $R=I+a_1T+\dots+a_{m-1}T^{m-1}$ where $T^m=0$. Then
> $$
> R^2=I+2a_1T+(2a_2+a_1^2)T^2+\dots+\big(2a_k+(\text{terms in }a_1,\dots,a_{k-1})\big)T^k+\dots ,
> $$
> all terms with $T^{\ge m}$ vanishing. Choose $a_1=\frac12$ and then, recursively, $a_k$ so that the coefficient of $T^k$ is $0$ for $k=2,\dots,m-1$ (possible since $a_k$ enters with coefficient $2$). Then $R^2=I+T$. (The $a_k$ are exactly the Taylor coefficients: $a_2=-\frac18$, $a_3=\frac1{16}$, $a_4=-\frac5{128}$.)

> [!theorem] 8.41 Over C, invertible operators have square roots
> If $V$ is a complex vector space and $T\in\Lin(V)$ is invertible, then $T$ has a square root.

^ladr-8-41

> [!remark] Hypotheses matter
> Invertibility: $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ has no square root. $\C$: $-1$ on $\R$ has none. The same method gives $k$-th roots.

> [!proof]+
> On $G(\lambda_k,T)$, $T=\lambda_kI+N_k$ with $N_k$ nilpotent ([[Generalized eigenspace decomposition|8.22]]), and $\lambda_k\ne0$, so $T|_{G(\lambda_k,T)}=\lambda_k(I+N_k/\lambda_k)$. With $\mu_k^2=\lambda_k$ and $S_k^2=I+N_k/\lambda_k$ ([[§30 Consequences of Generalized Eigenspace Decomposition#^ladr-8-39|8.39]]), $R_k=\mu_kS_k$ is a square root of $T|_{G(\lambda_k,T)}$ mapping $G(\lambda_k,T)$ into itself. For $v=u_1+\dots+u_m$, $u_k\in G(\lambda_k,T)$, set $Rv=R_1u_1+\dots+R_mu_m$. Then $R^2v=\sum R_k^2u_k=\sum Tu_k=Tv$.

*Uses:* [[Generalized eigenspace decomposition|8.22]], [[§30 Consequences of Generalized Eigenspace Decomposition#^ladr-8-39|8.39]]

> [!remark]- Connections
> - Compare [[§24 Positive Operators#^ladr-7-39|7.39]]: positive operators have a unique *positive* square root, for any $\F$.

> [!example] 8.42 Nilpotent operator with nice matrix (p. 321)
> $T(z_1,z_2,z_3,z_4)=(0,z_1,z_2,z_3)$ on $\C^4$: $T^4=0$. With $v=(1,0,0,0)$, the basis $T^3v,T^2v,Tv,v$ gives
> $$
> \mathcal{M}(T)=\begin{pmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\0&0&0&0\end{pmatrix}:
> $$
> a single Jordan block, from a single chain.

^ladr-8-42

> [!example] 8.43 Nilpotent operator with slightly more complicated matrix (p. 321)
> $T(z_1,\dots,z_6)=(0,z_1,z_2,0,z_4,0)$ on $\C^6$: $T^3=0$, but no single chain spans $\C^6$. With $v_1=e_1$, $v_2=e_4$, $v_3=e_6$, the basis $T^2v_1,Tv_1,v_1,\ Tv_2,v_2,\ v_3$ gives
> $$
> \mathcal{M}(T)=\begin{pmatrix}0&1&0&&&\\0&0&1&&&\\0&0&0&&&\\&&&0&1&\\&&&0&0&\\&&&&&0\end{pmatrix}
> $$
> (blank entries $0$): blocks of sizes $3,2,1$, one per chain:
>
> ![[ladr-8.43-chains.svg|480]]

^ladr-8-43

> [!definition] 8.44 Jordan basis
> A basis of $V$ is a *Jordan basis* for $T$ if $\mathcal{M}(T)$ is block diagonal with blocks
> $$
> \begin{pmatrix}\lambda&1&&0\\&\ddots&\ddots&\\&&\ddots&1\\0&&&\lambda\end{pmatrix}
> $$
> ($\lambda$ on the diagonal, $1$ directly above it, $0$ elsewhere).

^ladr-8-44

> [!remark]- Connections
> - Existence: [[§30 Consequences of Generalized Eigenspace Decomposition#^ladr-8-45|8.45]] (nilpotent), [[Jordan form|8.46]] (over $\C$). Picture of the chains: [[§30 Consequences of Generalized Eigenspace Decomposition#^ladr-8-43|8.43]].

> [!theorem] 8.45 Every nilpotent operator has a Jordan basis
> Every nilpotent $T\in\Lin(V)$ has a Jordan basis (over $\R$ or $\C$).

^ladr-8-45

> [!remark] Structure
> The basis consists of chains $T^{j}v_k$; each chain is one Jordan block, and $\dim\nullsp T$ is the number of blocks (figure in [[§30 Consequences of Generalized Eigenspace Decomposition#^ladr-8-43|8.43]]).

> [!proof]+
> Induction on $\dim V$; $\dim V=1$ is trivial. Let $m$ be minimal with $T^m=0$, pick $u$ with $T^{m-1}u\ne0$, and let $U=\Span(u,Tu,\dots,T^{m-1}u)$. This list is independent (if $\sum c_jT^ju=0$ with $k$ the least index with $c_k\ne0$, applying $T^{m-1-k}$ leaves $c_kT^{m-1}u=0$). $U$ is invariant, and $T^{m-1}u,\dots,Tu,u$ is a Jordan basis for $T|_U$ (one block). If $U=V$ we are done.
>
> Choose $\varphi\in V'$ with $\varphi(T^{m-1}u)\ne0$ and let
> $$
> W=\{v\in V:\varphi(T^kv)=0\text{ for }k=0,\dots,m-1\}.
> $$
> $W$ is an invariant subspace (for $v\in W$, $\varphi(T^k(Tv))=\varphi(T^{k+1}v)=0$, the case $k=m-1$ because $T^m=0$).
>
> **$U\cap W=\{0\}$.** If $v=\sum_{j<m}c_jT^ju\in W$ with $v\ne0$, let $k$ be least with $c_k\ne0$. Then $T^{m-1-k}v=c_kT^{m-1}u$, so $0=\varphi(T^{m-1-k}v)=c_k\varphi(T^{m-1}u)\ne0$: contradiction.
>
> **$\dim W\ge\dim V-m$.** $W$ is the null space of $v\mapsto(\varphi(v),\varphi(Tv),\dots,\varphi(T^{m-1}v))\in\F^m$ ([[Fundamental theorem of linear maps|3.21]]).
>
> So $V=U\oplus W$. As $\dim W<\dim V$, $T|_W$ has a Jordan basis by induction; together with the chain basis of $U$ this is a Jordan basis for $T$.

*Uses:* [[Fundamental theorem of linear maps|3.21]]

> [!theorem] 8.46 Jordan form
> If $\F=\C$ and $T\in\Lin(V)$, then $V$ has a Jordan basis for $T$.

^ladr-8-46

> [!remark] What is determined
> The block sizes for each eigenvalue are determined by $T$: the number of blocks of size $\ge j$ for $\lambda$ is $\dim\nullsp(T-\lambda I)^j-\dim\nullsp(T-\lambda I)^{j-1}$. Diagonalizable iff all blocks have size $1$.

> [!proof]+
> $V=\bigoplus_kG(\lambda_k,T)$ with each $(T-\lambda_kI)|_{G(\lambda_k,T)}$ nilpotent ([[Generalized eigenspace decomposition|8.22]]). Take a Jordan basis for each ([[§30 Consequences of Generalized Eigenspace Decomposition#^ladr-8-45|8.45]]); on $G(\lambda_k,T)$ it is a Jordan basis for $T=\lambda_kI+(T-\lambda_kI)$. Concatenate.

*Uses:* [[Generalized eigenspace decomposition|8.22]], [[§30 Consequences of Generalized Eigenspace Decomposition#^ladr-8-45|8.45]]

%% ex:8.46-fig %%
> [!example] What a Jordan form looks like
> Eigenvalue $\lambda_1$ with multiplicity $4$ (blocks of size $3$ and $1$) and $\lambda_2$ with multiplicity $2$ (one block): $1$'s only directly above the diagonal, inside blocks.
>
> ![[ladr-8.46-jordan.svg|420]]

