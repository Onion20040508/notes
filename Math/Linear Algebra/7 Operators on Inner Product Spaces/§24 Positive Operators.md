---
type: section
subject: "[[Linear Algebra]]"
chapter: 7
section: 24
aliases: ["LADR 7C", "7C Positive Operators"]
tags: [linear-algebra]
---
← [[§23 Spectral Theorem]] · ↑ [[· 7 Operators on Inner Product Spaces]] · [[§25 Isometries, Unitary Operators, and Matrix Factorization]] →

> [!definition] Definition 7.34: Positive operator
> $T\in\Lin(V)$ is *positive* if $T$ is self-adjoint and $\langle Tv,v\rangle\ge0$ for all $v$. (Over $\C$ self-adjointness is automatic, by [[§22 Self-Adjoint and Normal Operators#^ladr-7-14|7.14]].)

^ladr-7-34

> [!remark] Remark: Terminology
> 'Positive' means $\ge0$ (positive semidefinite). Invertible positive operators are the positive definite ones ([[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-61|Positive invertible operator]]).

> [!remark]- Connections
> - Physics: density operators are positive with trace $1$; $T^*T$ is always positive ([[§24 Positive Operators#^ladr-7-38|7.38]](f)).
> - Computational version: [[§49★ Quadratic Forms#^def-49-5|235 Def. §49.5]] (positive semidefinite matrices).

> [!example] Example 7.35: Positive operators (p. 251)
> - (a) $\mathcal{M}(T)=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}$ is self-adjoint and $\langle T(w,z),(w,z)\rangle=2|w|^2-2\operatorname{Re}(w\bar z)+|z|^2=|w-z|^2+|w|^2\ge0$: positive.
> - (b) Every orthogonal projection $P_U$ is positive: $\langle P_Uv,v\rangle=\langle P_Uv,P_Uv+(v-P_Uv)\rangle=\|P_Uv\|^2\ge0$, and $P_U$ is self-adjoint.
> - (c) For self-adjoint $T$ and $b^2<4c$, $T^2+bT+cI$ is positive (the proof of [[§23 Spectral Theorem#^ladr-7-26|7.26]]).

^ladr-7-35

> [!definition] Definition 7.36: Square root
> $R$ is a *square root* of $T$ if $R^2=T$.

^ladr-7-36

> [!remark]- Connections
> - Positive operators have a unique positive square root: [[§24 Positive Operators#^ladr-7-39|7.39]].

> [!example] Example 7.37: Square root of an operator (p. 251)
> $T(z_1,z_2,z_3)=(z_3,0,0)$ has the square root $R(z_1,z_2,z_3)=(z_2,z_3,0)$: $R^2(z_1,z_2,z_3)=R(z_2,z_3,0)=(z_3,0,0)$. Here $T$ is not positive (not self-adjoint), and $R$ is nilpotent.

^ladr-7-37

> [!theorem] Theorem 7.38: Characterization of positive operators
> For $T\in\Lin(V)$ the following are equivalent:
> - (a) $T$ is positive;
> - (b) $T$ is self-adjoint with all eigenvalues $\ge0$;
> - (c) in some orthonormal basis $\mathcal{M}(T)$ is diagonal with entries $\ge0$;
> - (d) $T$ has a positive square root;
> - (e) $T$ has a self-adjoint square root;
> - (f) $T=R^*R$ for some $R\in\Lin(V)$.

^ladr-7-38

> [!remark] Remark: The number analogy
> $z\in\C$ is $\ge0$ iff it has a $\ge0$ square root (d), iff it has a real square root (e), iff $z=\bar ww$ (f).

> [!proof]+ Proof
> (a)$\Rightarrow$(b): if $Tv=\lambda v$, $v\ne0$, then $0\le\langle Tv,v\rangle=\lambda\|v\|^2$.
>
> (b)$\Rightarrow$(c): spectral theorem ([[Real spectral theorem|7.29]], [[Complex spectral theorem|7.31]]).
>
> (c)$\Rightarrow$(d): if $Te_k=\lambda_ke_k$ with $\lambda_k\ge0$, define $Re_k=\sqrt{\lambda_k}e_k$. Then $R^2=T$, and $R$ is positive: diagonal real matrix in an orthonormal basis, and $\langle Rv,v\rangle=\sum\sqrt{\lambda_k}|\langle v,e_k\rangle|^2\ge0$.
>
> (d)$\Rightarrow$(e): positive operators are self-adjoint.
>
> (e)$\Rightarrow$(f): $T=R^2=R^*R$.
>
> (f)$\Rightarrow$(a): $(R^*R)^*=R^*R$ and $\langle R^*Rv,v\rangle=\|Rv\|^2\ge0$.

*Uses:* [[Real spectral theorem|7.29]], [[Complex spectral theorem|7.31]]

> [!remark]- Connections
> - (f) gives the positivity of $T^*T$ that SVD rests on ([[§26 Singular Value Decomposition#^ladr-7-64|Properties of T∗T]]).
> - Computational version: [[§49★ Quadratic Forms#^prop-49-5|235 Prop. §49.5]] ((a)⟺(b) for symmetric matrices; the definite case is [[§49★ Quadratic Forms#^thm-49-4|235 Thm. §49.4]]) and [[§52★ Applications to Image Processing and Statistics#^prop-52-1|235 Prop. §52.1]] ($BB^T$ is positive semidefinite, as in (f)).

> [!theorem] Theorem 7.39: Each positive operator has only one positive square root
> Every positive operator has a unique positive square root, denoted $\sqrt T$.

^ladr-7-39

> [!remark] Remark: Only one positive one
> Square roots in general are plentiful: $I$ on $\R^2$ has infinitely many (all reflections), but only $I$ itself is positive.

> [!proof]+ Proof
> Existence is [[§24 Positive Operators#^ladr-7-38|7.38]](d). For uniqueness let $R$ be any positive square root of $T$ and $Tv=\lambda v$; we show $Rv=\sqrt\lambda\,v$, which determines $R$ on an eigenbasis of $T$.
>
> Take an orthonormal eigenbasis of $R$ ([[Real spectral theorem|7.29]], [[Complex spectral theorem|7.31]]): $Re_k=\sqrt{\lambda_k}e_k$, $\lambda_k\ge0$. Write $v=\sum a_ke_k$. Then $\lambda v=Tv=R^2v=\sum a_k\lambda_ke_k$, so $a_k(\lambda-\lambda_k)=0$ for all $k$. Hence $v=\sum_{\lambda_k=\lambda}a_ke_k$ and $Rv=\sum_{\lambda_k=\lambda}a_k\sqrt\lambda\,e_k=\sqrt\lambda\,v$.

*Uses:* [[§24 Positive Operators#^ladr-7-38|7.38]], [[Real spectral theorem|7.29]], [[Complex spectral theorem|7.31]]

> [!remark]- Connections
> - Used in Quantum Field Theory: the positive square roots $\sqrt{p\cdot\sigma}$, $\sqrt{p\cdot\bar\sigma}$ that boost a Dirac spinor from rest to momentum $p$, and the positive factor in the polar decomposition of $SL(2, \mathbb C)$ — [[§C5a.5 Plane-Wave Solutions#^def-c5a-5-4|QFT Def. §C5a.5.4]], [[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-7|QFT Theorem §C5a.5.7]], [[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-4|QFT Theorem §C5a.1.4]].

> [!remark] Notation 7.40: √T (p. 253)

^ladr-7-40

> [!example] Example 7.41: Square root of positive operators (p. 254)
> $S(x,y)=(x,2y)$ and $T(x,y)=(x+y,x+y)$ on $\R^2$:
> $$
> \mathcal{M}(S)=\begin{pmatrix}1&0\\0&2\end{pmatrix},\qquad\mathcal{M}(T)=\begin{pmatrix}1&1\\1&1\end{pmatrix},
> $$
> both symmetric with $\langle S(x,y),(x,y)\rangle=x^2+2y^2\ge0$ and $\langle T(x,y),(x,y)\rangle=(x+y)^2\ge0$: positive. $T$ has orthonormal eigenvectors $\tfrac1{\sqrt2}(1,1)$ (eigenvalue $2$) and $\tfrac1{\sqrt2}(1,-1)$ (eigenvalue $0$), so $\sqrt T$ has the same eigenvectors with eigenvalues $\sqrt2,0$:
> $$
> \mathcal{M}(\sqrt S)=\begin{pmatrix}1&0\\0&\sqrt2\end{pmatrix},\qquad\mathcal{M}(\sqrt T)=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&1\end{pmatrix}
> $$
> (checked: squaring gives back $\mathcal{M}(T)$).

^ladr-7-41

> [!theorem] Theorem 7.43: T positive and ⟨Tv, v⟩ = 0 ⟹ Tv = 0
> If $T$ is positive and $\langle Tv,v\rangle=0$, then $Tv=0$.

^ladr-7-43

> [!proof]+ Proof
> $0=\langle Tv,v\rangle=\langle\sqrt T\sqrt Tv,v\rangle=\|\sqrt Tv\|^2$, so $\sqrt Tv=0$ and $Tv=\sqrt T(\sqrt Tv)=0$.

