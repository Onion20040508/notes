---
type: section
subject: "[[Linear Algebra]]"
chapter: 9
section: 35
aliases: ["LADR 9A", "9A Bilinear Forms and Quadratic Forms"]
tags: [linear-algebra]
---
← [[§34 The Operators (4z₂, 0, 5z₃) and (6z₁ + 3z₂ + 4z₃, 6z₂ + 2z₃, 7z₃)]] · ↑ [[· 9 Multilinear Algebra and Determinants]] · [[§36 Alternating Multilinear Forms]] →

> [!remark] Remark: Standing assumptions for Chapter 9
> Throughout Chapter 9, $V$ and $W$ are finite-dimensional nonzero vector spaces over $\F$ ($\F$ is $\R$ or $\C$). These are Axler's standing assumptions for the chapter; the chapter's statements use them without repeating them.

> [!definition] Definition 9.1: Bilinear form
> A *bilinear form* on $V$ is a function $\beta:V\times V\to\F$ such that $v\mapsto\beta(v,u)$ and $v\mapsto\beta(u,v)$ are linear functionals for every $u\in V$.

^ladr-9-1

> [!remark] Remark: Versus inner products
> A real inner product is a bilinear form that is also symmetric and positive definite. A complex inner product is *not* bilinear (conjugate-linear in the second slot).

> [!remark]- Connections
> - Physics: the Minkowski metric $\eta(u,v)=u^0v^0-u^1v^1-u^2v^2-u^3v^3$ (your $(+,-,-,-)$ convention) is a symmetric bilinear form that is not positive definite.
> - Used in Relativity: the Minkowski metric, its scalar product and the interval, a symmetric bilinear form and its quadratic form — [[§B1.1 The Metric and Index Notation#^def-b1-1-3|REL Def. §B1.1.3]].

> [!example] Example 9.2: Bilinear forms (p. 333)
> - $\beta(x,y)=x_1y_2-5x_2y_3+2x_3y_1$ on $\F^3$.
> - For $A\in\F^{n,n}$: $\beta_A(x,y)=\sum_{j,k}A_{j,k}x_jy_k=x^tAy$ (the first bullet is $A=\begin{pmatrix}0&1&0\\0&0&-5\\2&0&0\end{pmatrix}$).
> - On a real inner product space, $\beta(u,v)=\langle u,Tv\rangle$ for $T\in\Lin(V)$.
> - On $\Poly_n(\R)$: $\beta(p,q)=p(2)\,q'(3)$.
> - For $\varphi,\tau\in V'$: $\beta(u,v)=\varphi(u)\tau(v)$, and sums of such (every bilinear form is a sum of at most $\dim V$ such products).
>
> None of these is linear on $V\times V$ (unless $0$): bilinear is not linear.

^ladr-9-2

> [!definition] Definition 9.3: V⁽²⁾
> $V^{(2)}$ denotes the vector space of bilinear forms on $V$ (pointwise operations).

^ladr-9-3

> [!definition] Definition 9.4: Matrix of a bilinear form, M(β)
> For $\beta\in V^{(2)}$ and a basis $e_1,\dots,e_n$, the *matrix of $\beta$* is the $n$-by-$n$ matrix with
> $$
> \mathcal{M}(\beta)_{j,k}=\beta(e_j,e_k).
> $$

^ladr-9-4

> [!remark] Remark: Coordinates
> If $u,v$ have coordinate columns $x,y$, then $\beta(u,v)=x^t\,\mathcal{M}(\beta)\,y$.

> [!theorem] Theorem 9.5: Dim V⁽²⁾ = (dim V)²
> For a basis $e_1,\dots,e_n$, the map $\beta\mapsto\mathcal{M}(\beta)$ is an isomorphism $V^{(2)}\to\F^{n,n}$; hence $\dim V^{(2)}=(\dim V)^2$.

^ladr-9-5

> [!proof]+ Proof
> The map is linear. For $A\in\F^{n,n}$ define $\beta_A\big(\sum x_je_j,\sum y_ke_k\big)=\sum_{j,k}A_{j,k}x_jy_k$, a bilinear form with $\mathcal{M}(\beta_A)=A$. Conversely, expanding $\beta(\sum x_je_j,\sum y_ke_k)$ bilinearly gives $\sum_{j,k}\beta(e_j,e_k)x_jy_k$, so $\beta_{\mathcal{M}(\beta)}=\beta$. The two maps are inverse; $\dim\F^{n,n}=n^2$ ([[§9 Matrices#^ladr-3-40|3.40]]).

*Uses:* [[§9 Matrices#^ladr-3-40|3.40]]

> [!theorem] Theorem 9.6: Composition of a bilinear form and an operator
> For $\beta\in V^{(2)}$, $T\in\Lin(V)$, define $\alpha(u,v)=\beta(u,Tv)$ and $\rho(u,v)=\beta(Tu,v)$. In any basis,
> $$
> \mathcal{M}(\alpha)=\mathcal{M}(\beta)\mathcal{M}(T),\qquad\mathcal{M}(\rho)=\mathcal{M}(T)^t\mathcal{M}(\beta).
> $$

^ladr-9-6

> [!proof]+ Proof
> $\mathcal{M}(\alpha)_{j,k}=\beta\big(e_j,\sum_m\mathcal{M}(T)_{m,k}e_m\big)=\sum_m\mathcal{M}(\beta)_{j,m}\mathcal{M}(T)_{m,k}$. Similarly $\mathcal{M}(\rho)_{j,k}=\sum_m\mathcal{M}(T)_{m,j}\mathcal{M}(\beta)_{m,k}=\big(\mathcal{M}(T)^t\mathcal{M}(\beta)\big)_{j,k}$.

> [!theorem] Theorem 9.7: Change-of-basis formula
> Let $\beta\in V^{(2)}$, bases $e$ and $f$, $A=\mathcal{M}(\beta,(e))$, $B=\mathcal{M}(\beta,(f))$, $C=\mathcal{M}(I,(e),(f))$. Then
> $$
> A=C^tBC .
> $$

^ladr-9-7

> [!proof]+ Proof
> Let $T\in\Lin(V)$ with $Tf_k=e_k$ ([[Linear map lemma|3.4]]); then $\mathcal{M}(T,(f))=C$. Put $\alpha(u,v)=\beta(u,Tv)$ and $\rho(u,v)=\alpha(Tu,v)=\beta(Tu,Tv)$. Then $\beta(e_j,e_k)=\rho(f_j,f_k)$, so by [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-6|9.6]] (twice) $A=\mathcal{M}(\rho,(f))=C^t\mathcal{M}(\alpha,(f))=C^tBC$.

*Uses:* [[Linear map lemma|3.4]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-6|9.6]]

> [!remark] Remark: Contrast with operators
> Operators transform by $C^{-1}BC$ ([[§10 Invertibility and Isomorphisms#^ladr-3-84|3.84]]); bilinear forms by $C^tBC$. In index language: operators are $(1,1)$-tensors, bilinear forms are $(0,2)$-tensors. They agree exactly when $C^t=C^{-1}$ (orthogonal changes of basis), which is why the difference is invisible in orthonormal frames.

> [!remark]- Connections
> - Physics/GR: $g'_{\mu\nu}=\frac{\partial x^\alpha}{\partial x'^\mu}\frac{\partial x^\beta}{\partial x'^\nu}g_{\alpha\beta}$ is this formula.
> - Used in Relativity: a Lorentz transformation is a change of basis that leaves the matrix of the metric unchanged, $\Lambda^{\mathsf T}\eta\Lambda = \eta$ — [[§B1.2 Lorentz Transformations and the Lorentz Group#^def-b1-2-1|REL Def. §B1.2.1]]; the field tensor, an alternating bilinear form, transforms by the same formula — [[§B4.2 The Electromagnetic Field Tensor#^def-b4-2-2|REL Def. §B4.2.2]], [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-2|REL Theorem §B4.2.2]].
> - Computational version: [[§59★ Quadratic Forms#^prop-59-1|235 Prop. §59.1]] (the change of variable $\mathbf x=P\mathbf y$ turns the matrix $A$ of a quadratic form into $P^TAP$).

> [!example] Example 9.8: The matrix of a bilinear form on P2(R) (p. 336)
> $\beta(p,q)=p(2)\,q'(3)$ on $\Poly_2(\R)$. With the bases $(1,\ x-2,\ (x-3)^2)$ and $(1,x,x^2)$:
> $$
> A=\begin{pmatrix}0&1&0\\0&0&0\\0&1&0\end{pmatrix},\quad
> B=\begin{pmatrix}0&1&6\\0&2&12\\0&4&24\end{pmatrix},\quad
> C=\begin{pmatrix}1&-2&9\\0&1&-6\\0&0&1\end{pmatrix},
> $$
> ($A_{j,k}=e_j(2)e_k'(3)$; column $k$ of $C$ is $e_k$ in the basis $1,x,x^2$, e.g. $(x-3)^2=9-6x+x^2$), and $C^tBC=A$ (verified).

^ladr-9-8

> [!definition] Definition 9.9: Symmetric bilinear form, V⁽²⁾ sym
> $\rho\in V^{(2)}$ is *symmetric* if $\rho(u,w)=\rho(w,u)$ for all $u,w$. $V^{(2)}_{\mathrm{sym}}$ is the set of symmetric bilinear forms.

^ladr-9-9

> [!example] Example 9.10: Symmetric bilinear forms (p. 337)
> - A real inner product is a symmetric bilinear form.
> - On a real inner product space, $\rho(u,w)=\langle u,Tw\rangle$ is symmetric iff $T$ is self-adjoint.
> - $\rho(S,T)=\operatorname{tr}(ST)$ on $\Lin(V)$ is symmetric, since $\operatorname{tr}(ST)=\operatorname{tr}(TS)$ ([[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-56|8.56]]). (Up to a constant factor this is the Killing form of $\mathfrak{su}(n)$, used to define inner products on Lie algebras.)

^ladr-9-10

> [!definition] Definition 9.11: Symmetric matrix
> A square matrix $A$ is *symmetric* if $A^t=A$.

^ladr-9-11

> [!remark] Remark: Forms vs operators
> An operator can be symmetric in some bases and not others; a bilinear form is symmetric in all bases or in none ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-12|9.12]]).

> [!remark]- Connections
> - The symmetric matrices form a Euclidean space of dimension n(n + 1)∕2, [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^def-23-1|591 Def. §23.1]], the target of A ↦ AAᵗ when O(n) is shown to be a manifold ([[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|591 Ex. §23.1]]).
> - Computational version: [[§58★ Diagonalization of Symmetric Matrices#^def-58-1|235 Def. §58.1]] (symmetric matrices, with examples).

> [!theorem] Theorem 9.12: Symmetric bilinear forms are diagonalizable
> For $\rho\in V^{(2)}$, equivalent:
> - (a) $\rho$ is symmetric;
> - (b) $\mathcal{M}(\rho,(e))$ is symmetric for every basis;
> - (c) $\mathcal{M}(\rho,(e))$ is symmetric for some basis;
> - (d) $\mathcal{M}(\rho,(e))$ is diagonal for some basis.

^ladr-9-12

> [!proof]+ Proof
> (a)$\Rightarrow$(b)$\Rightarrow$(c) are immediate. (c)$\Rightarrow$(a): expanding $\rho(\sum a_je_j,\sum b_ke_k)=\sum a_jb_k\rho(e_j,e_k)$ and using $\rho(e_j,e_k)=\rho(e_k,e_j)$ gives $\rho(u,w)=\rho(w,u)$. (d)$\Rightarrow$(c): diagonal matrices are symmetric.
>
> (a)$\Rightarrow$(d), by induction on $n$; $n=1$ is trivial. If $\rho=0$ any basis works. Otherwise some $v$ has $\rho(v,v)\neq0$: if $\rho(v,v)=0$ for all $v$, then $\rho$ would be alternating as well as symmetric, hence $0$ ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-17|9.17]], later in this section; its proof does not use 9.12). Let $U=\{u:\rho(u,v)=0\}$, the null space of a nonzero functional, so $\dim U=n-1$ and $v\notin U$, giving $V=\Span(v)\oplus U$. By induction $\rho|_{U\times U}$ is diagonal in a basis $e_1,\dots,e_{n-1}$ of $U$; then in $e_1,\dots,e_{n-1},v$ the matrix of $\rho$ is diagonal (each $\rho(e_j,v)=\rho(v,e_j)=0$).

*Uses:* [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-17|9.17]]

> [!remark] Remark: Why this is easy
> Unlike operators, every symmetric form can be diagonalized, over any $\F$ (of characteristic $\ne2$): the transformation rule $C^tBC$ is much more flexible than $C^{-1}BC$.

> [!remark]- Connections
> - Orthonormal version: [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-13|9.13]]. Sylvester's law of inertia (not in Axler): the numbers of positive, negative and zero diagonal entries do not depend on the diagonalizing basis (for $\F=\R$); e.g. Minkowski space has signature $(1,3)$.
> - Used in Relativity: Minkowski space has signature (1, 3) in every inertial frame — [[§B1.1 The Metric and Index Notation#^def-b1-1-3|REL Def. §B1.1.3]].

> [!theorem] Theorem 9.13: Diagonalization of a symmetric bilinear form by an orthonormal basis
> On a real inner product space, every symmetric bilinear form has a diagonal matrix with respect to some **orthonormal** basis.

^ladr-9-13

> [!proof]+ Proof
> Let $f$ be an orthonormal basis, $B=\mathcal{M}(\rho,(f))$ (symmetric, [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-12|9.12]]), and $T$ the operator with $\mathcal{M}(T,(f))=B$, self-adjoint ([[§23 Self-Adjoint and Normal Operators#^ladr-7-9|7.9]]). By [[Real spectral theorem|7.29]] there is an orthonormal basis $e$ with $C^{-1}BC$ diagonal, $C=\mathcal{M}(I,(e),(f))$. $C$ is a real unitary matrix, so $C^t=C^{-1}$ ([[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|7.57]]), and $\mathcal{M}(\rho,(e))=C^tBC=C^{-1}BC$ ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-7|9.7]]).

*Uses:* [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-12|9.12]], [[§23 Self-Adjoint and Normal Operators#^ladr-7-9|7.9]], [[Real spectral theorem|7.29]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|7.57]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-7|9.7]]

> [!remark] Remark: Principal axes
> This is the principal-axis theorem: the level sets of a quadratic form are ellipsoids/hyperboloids whose axes are orthogonal (figure after [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-23|9.23]]).

> [!remark]- Connections
> - Used in Stewart to bring a quadric surface to standard form: [[§99 Cylinders and Quadric Surfaces#^def-99-3|Calc Def. §99.3]].
> - Computational version: [[§59★ Quadratic Forms#^thm-59-2|235 Thm. §59.2]] (the Principal Axes Theorem for $\mathbf x^TA\mathbf x$ on $\mathbb R^n$).

> [!definition] Definition 9.14: Alternating bilinear form, V⁽²⁾ alt
> $\alpha\in V^{(2)}$ is *alternating* if $\alpha(v,v)=0$ for all $v$. $V^{(2)}_{\mathrm{alt}}$ is the set of alternating bilinear forms.

^ladr-9-14

> [!remark]- Connections
> - Physics: the symplectic form $\omega\big((q,p),(q',p')\big)=q\cdot p'-p\cdot q'$ of Hamiltonian mechanics is alternating; in the language of [[Differentiable Manifolds]] it is a $2$-form.
> - Used in Relativity: the electromagnetic field tensor $F_{\mu\nu}$ is an alternating bilinear form on spacetime — [[§B4.2 The Electromagnetic Field Tensor#^def-b4-2-2|REL Def. §B4.2.2]], [[§B4.2 The Electromagnetic Field Tensor|REL §B4.2]] (Connections).

> [!example] Example 9.15: Alternating bilinear forms (p. 339)
> - On $\F^n$ ($n\ge3$): $\alpha(x,y)=x_1y_2-x_2y_1+x_1y_3-x_3y_1$.
> - For $\varphi,\tau\in V'$: $\alpha(u,w)=\varphi(u)\tau(w)-\varphi(w)\tau(u)$, i.e. $\varphi\wedge\tau$. (The first bullet is $e^1\wedge e^2+e^1\wedge e^3$.)

^ladr-9-15

> [!theorem] Theorem 9.16: Characterization of alternating bilinear forms
> A bilinear form $\alpha$ is alternating iff $\alpha(u,w)=-\alpha(w,u)$ for all $u,w$.

^ladr-9-16

> [!proof]+ Proof
> ($\Rightarrow$) $0=\alpha(u+w,u+w)=\alpha(u,w)+\alpha(w,u)$. ($\Leftarrow$) $\alpha(v,v)=-\alpha(v,v)$, so $\alpha(v,v)=0$ ($2\ne0$ in $\F$).

%% ex:9.16-sym-alt %%
> [!theorem] Theorem 9.17: $V^{(2)}=V^{(2)}_{\mathrm{sym}}\oplus V^{(2)}_{\mathrm{alt}}$
> Both are subspaces of $V^{(2)}$, and every bilinear form is uniquely a symmetric plus an alternating one.
>
> In matrices: every square matrix is uniquely symmetric plus antisymmetric, $B=\frac{B+B^t}2+\frac{B-B^t}2$.

^ladr-9-17

> [!proof]+ Proof
> For $\beta\in V^{(2)}$ put $\rho(u,w)=\frac{\beta(u,w)+\beta(w,u)}2$ and $\alpha(u,w)=\frac{\beta(u,w)-\beta(w,u)}2$: $\rho$ is symmetric, $\alpha$ is alternating ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-16|9.16]]), and $\beta=\rho+\alpha$. If a form is both symmetric and alternating, $\rho(u,w)=\rho(w,u)=-\rho(u,w)$, so it is $0$. Hence the sum is direct.

*Uses:* [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-16|9.16]]

> [!remark]- Connections
> - Used in Relativity: every rank-2 Lorentz tensor splits uniquely, and in every frame alike, into symmetric and antisymmetric parts — [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]].
> - For bilinear forms on $\R^n$ in the language of differential forms: [[§39 Closed and Exact Forms#^prop-39-3|452 Prop. §39.3]].
> - The same split for tensors of higher order: in a potential term $\lambda_{ijk}\varphi_i\varphi_j\varphi_k$ only the totally symmetric part of the coefficients contributes, so the coefficients may be taken totally symmetric ([[§R1.1 N Real Scalar Fields and Their Potential#^rem-r1-1-1|Thesis §R1.1, Remark]]).

> [!definition] Definition 9.18: Quadratic form associated with a bilinear form, qβ
> For $\beta\in V^{(2)}$, $q_\beta(v)=\beta(v,v)$. A *quadratic form* is a function $q=q_\beta$ for some bilinear $\beta$. $q_\beta=0$ iff $\beta$ is alternating.

^ladr-9-18

> [!remark]- Connections
> - Computational version: [[§59★ Quadratic Forms#^def-59-1|235 Def. §59.1]] (quadratic forms $\mathbf x^TA\mathbf x$ on $\mathbb R^n$).
> - In several variables: the second-order term of Taylor's formula is the quadratic form of the Hessian, [[Multivariable Taylor's Theorem|452 Thm. §11.2]], whose sign decides the [[Second Derivative Test in Several Variables|452 Thm. §18.1]].

> [!example] Example 9.19: Quadratic form (p. 341)
> $\beta(x,y)=x_1y_1-4x_1y_2+8x_1y_3-3x_3y_3$ on $\R^3$ gives $q_\beta(x)=x_1^2-4x_1x_2+8x_1x_3-3x_3^2$.

^ladr-9-19

> [!theorem] Theorem 9.20: Quadratic forms on Fⁿ
> $q:\F^n\to\F$ is a quadratic form iff there are $A_{j,k}\in\F$ with $q(x_1,\dots,x_n)=\sum_{j,k}A_{j,k}x_jx_k$.

^ladr-9-20

> [!proof]+ Proof
> ($\Rightarrow$) take $A=\mathcal{M}(\beta)$ in the standard basis. ($\Leftarrow$) $\beta(x,y)=\sum_{j,k}A_{j,k}x_jy_k$ is bilinear with $q_\beta=q$.

> [!remark]- Connections
> - Computational version: [[§59★ Quadratic Forms#^def-59-1|235 Def. §59.1]] (the real case, with $A$ symmetric).

> [!theorem] Theorem 9.21: Characterization of quadratic forms
> For $q:V\to\F$, equivalent:
> - (a) $q$ is a quadratic form;
> - (b) $q=q_\rho$ for a **unique** symmetric bilinear form $\rho$;
> - (c) $q(\lambda v)=\lambda^2q(v)$, and $(u,w)\mapsto q(u+w)-q(u)-q(w)$ is a symmetric bilinear form;
> - (d) $q(2v)=4q(v)$, and $(u,w)\mapsto q(u+w)-q(u)-q(w)$ is a symmetric bilinear form.

^ladr-9-21

> [!proof]+ Proof
> (a)$\Rightarrow$(b): $q=q_\beta$ and $\beta=\rho+\alpha$ ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-17|9.17]]); $q_\alpha=0$, so $q=q_\rho$. If also $q=q_{\rho'}$, then $\rho'-\rho$ is symmetric with $q_{\rho'-\rho}=0$, i.e. also alternating, so $\rho'=\rho$.
>
> (b)$\Rightarrow$(c): $q(\lambda v)=\lambda^2\rho(v,v)$, and $q(u+w)-q(u)-q(w)=2\rho(u,w)$.
>
> (c)$\Rightarrow$(d): take $\lambda=2$.
>
> (d)$\Rightarrow$(a): let $\rho(u,w)=\frac12\big(q(u+w)-q(u)-q(w)\big)$, symmetric bilinear by hypothesis. Then $q_\rho(v)=\frac12\big(q(2v)-2q(v)\big)=\frac12\big(4q(v)-2q(v)\big)=q(v)$.

*Uses:* [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-17|9.17]]

> [!remark] Remark: Polarization
> $\rho(u,w)=\frac12\big(q(u+w)-q(u)-q(w)\big)$ recovers the symmetric form from the quadratic form (compare [[§20 Inner Products and Norms#^ladr-6-21|6.21]]).

> [!remark]- Connections
> - Used in Relativity: invariance of the interval, a quadratic form, gives invariance of the Minkowski scalar product — [[§B1.1 The Metric and Index Notation#^thm-b1-1-1|REL Theorem §B1.1.1]]; and a quadratic form fixes its symmetric matrix in the proof that the postulates force the invariance of the interval — [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-1|REL Theorem §B1.2.1]].
> - Computational version: [[§59★ Quadratic Forms#^def-59-1|235 Def. §59.1]] (the symmetric matrix of a form on $\mathbb R^n$ is unique: split each cross-product coefficient evenly, as in (b)).

> [!example] Example 9.22: Symmetric bilinear form associated with a quadratic form (p. 343)
> The $\beta$ of [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-19|9.19]] is not symmetric. The unique symmetric $\rho$ with $q_\rho=q_\beta$ splits each cross term evenly:
> $$
> \rho(x,y)=x_1y_1-2x_1y_2-2x_2y_1+4x_1y_3+4x_3y_1-3x_3y_3,
> \qquad \mathcal{M}(\rho)=\begin{pmatrix}1&-2&4\\-2&0&0\\4&0&-3\end{pmatrix}=\tfrac12\big(\mathcal{M}(\beta)+\mathcal{M}(\beta)^t\big).
> $$

^ladr-9-22

> [!remark]- Connections
> - Computational version: [[§59★ Quadratic Forms#^ex-59-1|235 Ex. §59.1]] (from a matrix to a form and back, splitting the cross terms evenly).

> [!theorem] Theorem 9.23: Diagonalization of quadratic form
> Let $q$ be a quadratic form on $V$.
> - (a) There are a basis $e_1,\dots,e_n$ and $\lambda_1,\dots,\lambda_n\in\F$ with $q\big(\sum x_ke_k\big)=\lambda_1x_1^2+\dots+\lambda_nx_n^2$.
> - (b) If $\F=\R$ and $V$ is an inner product space, the basis can be chosen orthonormal.

^ladr-9-23

> [!proof]+ Proof
> (a) $q=q_\rho$ with $\rho$ symmetric ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-21|9.21]]); diagonalize $\rho$ ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-12|9.12]]): $\rho(e_j,e_k)=\lambda_j\delta_{jk}$. Then $q(\sum x_ke_k)=\sum_{j,k}x_jx_k\rho(e_j,e_k)=\sum\lambda_kx_k^2$. (b) Use [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-13|9.13]].

*Uses:* [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-21|9.21]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-12|9.12]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-13|9.13]]

> [!remark]- Connections
> - Physics: normal modes (simultaneously diagonalize kinetic and potential energy forms), the inertia tensor, and the second-derivative test (Hessian) are all this result.
> - Computational version: [[§59★ Quadratic Forms#^thm-59-2|235 Thm. §59.2]] (part (b) on $\mathbb R^n$, worked in [[§59★ Quadratic Forms#^ex-59-2|235 Ex. §59.2]]).

%% ex:9.23-fig %%
> [!example] Example: Diagonalizing a quadratic form, pictured
> Left: $q(x,y)=3x^2+2xy+3y^2$, i.e. matrix $\begin{pmatrix}3&1\\1&3\end{pmatrix}$ with eigenvalues $4,2$ on $\tfrac1{\sqrt2}(1,1)$, $\tfrac1{\sqrt2}(-1,1)$. In those orthonormal coordinates $q=4u^2+2w^2$, and the level set $q=1$ is an ellipse with its axes on the eigenlines. Right: $q(x,y)=2xy=u^2-w^2$ (indefinite), whose level sets are hyperbolas with asymptotes $u=\pm w$, i.e. the coordinate axes.
>
> ![[ladr-9.23-quadratic.svg|520]]

