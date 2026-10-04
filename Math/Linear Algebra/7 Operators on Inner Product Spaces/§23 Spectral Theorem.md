---
type: section
subject: "[[Linear Algebra]]"
chapter: 7
section: 23
aliases: ["LADR 7B", "7B Spectral Theorem"]
tags: [linear-algebra]
---
← [[§22 Self-Adjoint and Normal Operators]] · ↑ [[· 7 Operators on Inner Product Spaces]] · [[§24 Positive Operators]] →

> [!theorem] Theorem 7.26: Invertible quadratic expressions
> If $T$ is self-adjoint and $b,c\in\R$ with $b^2<4c$, then $T^2+bT+cI$ is invertible.

^ladr-7-26

> [!remark] Remark: Meaning
> $z^2+bz+c$ has no real roots, and a self-adjoint $T$ 'is real', so $T^2+bT+cI$ cannot kill anything. It is in fact positive ([[§24 Positive Operators#^ladr-7-35|7.35]](c)).

> [!proof]+ Proof
> For $v\ne0$, using $\langle T^2v,v\rangle=\|Tv\|^2$ (self-adjoint) and [[Cauchy–Schwarz inequality|6.14]],
> $$
> \langle(T^2+bT+cI)v,v\rangle\ge\|Tv\|^2-|b|\|Tv\|\|v\|+c\|v\|^2=\Big(\|Tv\|-\frac{|b|\|v\|}2\Big)^2+\Big(c-\frac{b^2}4\Big)\|v\|^2>0 .
> $$
> So the operator is injective, hence invertible ([[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]]).

*Uses:* [[Cauchy–Schwarz inequality|6.14]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]]

> [!theorem] Theorem 7.27: Minimal polynomial of self-adjoint operator
> If $T$ is self-adjoint, its minimal polynomial is $(z-\lambda_1)\cdots(z-\lambda_m)$ with all $\lambda_k\in\R$.

^ladr-7-27

> [!proof]+ Proof
> **$\F=\C$:** the zeros of the minimal polynomial are eigenvalues ([[§15 The Minimal Polynomial#^ladr-5-27|5.27]]), which are real ([[§22 Self-Adjoint and Normal Operators#^ladr-7-12|7.12]]); the polynomial splits over $\C$ ([[§13 Polynomials#^ladr-4-13|4.13]]).
>
> **$\F=\R$:** by [[§13 Polynomials#^ladr-4-16|4.16]] the minimal polynomial is $(z-\lambda_1)\cdots(z-\lambda_m)(z^2+b_1z+c_1)\cdots(z^2+b_Nz+c_N)$ with $b_k^2<4c_k$. If $N>0$, multiply the equation $p(T)=0$ on the right by $(T^2+b_NT+c_NI)^{-1}$ ([[§23 Spectral Theorem#^ladr-7-26|7.26]]): a polynomial of degree two less kills $T$, contradicting minimality. So $N=0$.

*Uses:* [[§15 The Minimal Polynomial#^ladr-5-27|5.27]], [[§22 Self-Adjoint and Normal Operators#^ladr-7-12|7.12]], [[§13 Polynomials#^ladr-4-13|4.13]], [[§13 Polynomials#^ladr-4-16|4.16]], [[§23 Spectral Theorem#^ladr-7-26|7.26]]

> [!remark]- Connections
> - In particular every self-adjoint operator (on $V\ne\{0\}$) has an eigenvalue, even over $\R$.
> - No analogue in infinite dimensions, where a self-adjoint operator need not have any eigenvalue: multiplication by x on L²(ℝ) has no eigenvectors at all, [[§32 Position Eigenstates and Continuous Resolutions#^prop-32-3|556 Prop. §32.3]].

> [!theorem] Theorem 7.29: Real spectral theorem
> Let $\F=\R$ and $T\in\Lin(V)$. Equivalent:
> - (a) $T$ is self-adjoint;
> - (b) $T$ has a diagonal matrix with respect to some orthonormal basis;
> - (c) $V$ has an orthonormal basis of eigenvectors of $T$.

^ladr-7-29

> [!remark] Remark: Geometry
> A symmetric matrix acts by stretching along perpendicular axes. The unit sphere goes to an ellipsoid whose axes are the eigenvectors (see [[§14 Invariant Subspaces#^ladr-5-8|5.8]] and the figure below).

> [!proof]+ Proof
> (a)$\Rightarrow$(b): by [[§23 Spectral Theorem#^ladr-7-27|7.27]] and [[§20 Orthonormal Bases#^ladr-6-37|6.37]], $T$ is upper triangular in some orthonormal basis. There $\mathcal{M}(T^*)=\mathcal{M}(T)^t$ ([[§22 Self-Adjoint and Normal Operators#^ladr-7-9|7.9]]), and $T=T^*$, so the upper-triangular matrix equals its transpose: it is diagonal.
>
> (b)$\Rightarrow$(a): a diagonal real matrix equals its transpose, so $\mathcal{M}(T^*)=\mathcal{M}(T)$ and $T^*=T$.
>
> (b)$\iff$(c): as in [[§17 Diagonalizable Operators#^ladr-5-55|5.55]].

*Uses:* [[§23 Spectral Theorem#^ladr-7-27|7.27]], [[§20 Orthonormal Bases#^ladr-6-37|6.37]], [[§22 Self-Adjoint and Normal Operators#^ladr-7-9|7.9]], [[§17 Diagonalizable Operators#^ladr-5-55|5.55]]

> [!remark]- Connections
> - Computational version: [[§48★ Diagonalization of Symmetric Matrices#^thm-48-3|235 Thm. §48.3]] (the spectral theorem for symmetric matrices) and [[§48★ Diagonalization of Symmetric Matrices#^thm-48-2|235 Thm. §48.2]] (orthogonally diagonalizable iff symmetric), with worked orthogonal diagonalizations.
> - Matrix version: a Hermitian (in particular real symmetric) matrix has $n$ mutually orthogonal eigenvectors, [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-5|331 Thm. §29.5]] (2), (4), used to solve $\mathbf{x}' = \mathbf{A}\mathbf{x}$ with symmetric $\mathbf{A}$.
> - Infinite-dimensional analogue: a regular Sturm–Liouville problem has infinitely many real eigenvalues, [[§23 Sturm–Liouville Problems#^thm-23-5|341 Thm. §23.5]], and every sectionally smooth function expands in its orthogonal eigenfunctions, [[§24 Expansion in Series of Eigenfunctions#^thm-24-2|341 Thm. §24.2]] (stated there without proof).
> - Second derivative test: the Hessian is symmetric, so by this theorem its definiteness is read off from the signs of its eigenvalues, [[Second Derivative Test in Several Variables|452 Thm. §14.4]].

%% ex:7.29-fig %%
> [!example] Example: Self-adjoint versus merely diagonalizable
> Left: $\begin{pmatrix}2&1\\1&2\end{pmatrix}$ is symmetric; its eigenvector lines are perpendicular and the unit circle goes to an ellipse with axes along them. Right: $\begin{pmatrix}2&1\\0&3\end{pmatrix}$ is diagonalizable (distinct eigenvalues) but not self-adjoint; its eigenvector lines $\Span(1,0)$ and $\Span(1,1)$ meet at $45^\circ$, so no orthonormal eigenbasis exists.
>
> ![[ladr-7.29-orthogonal-vs-skew.svg|520]]

> [!example] Example 7.30: An orthonormal basis of eigenvectors for an operator (p. 245)
> $\mathcal{M}(T)=\begin{pmatrix}14&-13&8\\-13&14&8\\8&8&-7\end{pmatrix}$ is real symmetric, so $T$ is self-adjoint. The orthonormal basis
> $$
> \tfrac1{\sqrt2}(1,-1,0),\qquad\tfrac1{\sqrt3}(1,1,1),\qquad\tfrac1{\sqrt6}(1,1,-2)
> $$
> consists of eigenvectors with eigenvalues $27$, $9$, $-15$ (checked: e.g. $T(1,1,-2)=(-15,-15,30)$), so in it $\mathcal{M}(T)=\operatorname{diag}(27,9,-15)$.

^ladr-7-30

> [!theorem] Theorem 7.31: Complex spectral theorem
> Let $\F=\C$ and $T\in\Lin(V)$. Equivalent:
> - (a) $T$ is normal;
> - (b) $T$ has a diagonal matrix with respect to some orthonormal basis;
> - (c) $V$ has an orthonormal basis of eigenvectors of $T$.

^ladr-7-31

> [!remark] Remark: Why the real theorem needs more
> Over $\R$ normal is not enough: rotation by $90^\circ$ is normal ($TT^*=I$) but has no real eigenvalues ([[§14 Invariant Subspaces#^ladr-5-9|5.9]]).

> [!proof]+ Proof
> (a)$\Rightarrow$(b): by Schur ([[§20 Orthonormal Bases#^ladr-6-38|6.38]]), $T$ is upper triangular, $(a_{j,k})$, in an orthonormal basis $e_1,\dots,e_n$. From the matrix,
> $$
> \|Te_1\|^2=|a_{1,1}|^2,\qquad\|T^*e_1\|^2=|a_{1,1}|^2+|a_{1,2}|^2+\dots+|a_{1,n}|^2
> $$
> (using [[§22 Self-Adjoint and Normal Operators#^ladr-7-9|7.9]]: row 1 of $\mathcal{M}(T)$ conjugated is column 1 of $\mathcal{M}(T^*)$). Normality gives $\|Te_1\|=\|T^*e_1\|$ ([[§22 Self-Adjoint and Normal Operators#^ladr-7-20|7.20]]), so $a_{1,2}=\dots=a_{1,n}=0$. Then $\|Te_2\|^2=|a_{2,2}|^2$ and $\|T^*e_2\|^2=|a_{2,2}|^2+\dots+|a_{2,n}|^2$ force row 2 to vanish off the diagonal; inductively every row does.
>
> (b)$\Rightarrow$(a): $\mathcal{M}(T^*)$ is the conjugate diagonal matrix, and diagonal matrices commute.
>
> (b)$\iff$(c): as in [[§17 Diagonalizable Operators#^ladr-5-55|5.55]].

*Uses:* [[§20 Orthonormal Bases#^ladr-6-38|6.38]], [[§22 Self-Adjoint and Normal Operators#^ladr-7-9|7.9]], [[§22 Self-Adjoint and Normal Operators#^ladr-7-20|7.20]], [[§17 Diagonalizable Operators#^ladr-5-55|5.55]]

> [!remark]- Connections
> - Used in Quantum Mechanics: a change of basis to the eigenbasis of an observable by diagonalizing its matrix, and unitarily equivalent observables with identical spectra — [[§C1.4 Change of Basis and Unitary Equivalence#^thm-c1-4-3|QM Theorem §C1.4.3]], [[§C1.4 Change of Basis and Unitary Equivalence#^thm-c1-4-4|QM Theorem §C1.4.4]].
> - Matrix version for Hermitian matrices: [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-5|331 Thm. §29.5]] (2), (4), and $\mathbf{T}^{-1} = \mathbf{T}^*$ in [[§33★ Fundamental Matrices#^thm-33-7|331 Thm. §33.7]] (b).

> [!example] Example 7.33: An orthonormal basis of eigenvectors for an operator (p. 247)
> $T(w,z)=(2w-3z,\ 3w+2z)$ on $\C^2$ is normal ([[§22 Self-Adjoint and Normal Operators#^ladr-7-19|7.19]]). The orthonormal basis $\tfrac1{\sqrt2}(i,1)$, $\tfrac1{\sqrt2}(-i,1)$ consists of eigenvectors (e.g. $T(i,1)=(2i-3,\ 3i+2)=(2+3i)(i,1)$), and
> $$
> \mathcal{M}(T)=\begin{pmatrix}2+3i&0\\0&2-3i\end{pmatrix}.
> $$
> Over $\R$ this $T$ has no eigenvalues: normal does not suffice for the real spectral theorem.

^ladr-7-33
