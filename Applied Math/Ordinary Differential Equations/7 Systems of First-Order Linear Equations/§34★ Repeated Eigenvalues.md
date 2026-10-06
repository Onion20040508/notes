---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 7
section: 34
bdp: "7.8"
aliases: ["BDP 7.8"]
tags: [ordinary-differential-equations, math331, extension]
---
← [[§33★ Fundamental Matrices]] · ↑ [[· 7 Systems of First-Order Linear Equations]] · [[§35★ Nonhomogeneous Linear Systems]] →

*Boyce–DiPrima, Section 7.8.*
★ *Beyond MATH 331: the course skipped this section; it is included from Boyce–DiPrima as part of the chapter.*

This section finishes the constant-coefficient system $\mathbf{x}' = \mathbf{A}\mathbf{x}$ with the case of a repeated eigenvalue. If an eigenvalue $\rho$ of algebraic multiplicity $m$ has $m$ independent eigenvectors, nothing changes. If it has fewer, the eigenvector solutions $\boldsymbol{\xi}e^{\rho t}$ run out. As for the double root of $ay'' + by' + cy = 0$ ([[§16 Repeated Roots; Reduction of Order|§16]]), a factor $t$ appears, but for systems the second solution is $\boldsymbol{\xi}te^{\rho t} + \boldsymbol{\eta}e^{\rho t}$, where the generalized eigenvector $\boldsymbol{\eta}$ solves $(\mathbf{A} - \rho\mathbf{I})\boldsymbol{\eta} = \boldsymbol{\xi}$. In the plane the origin is then an improper node. In matrix language, $\mathbf{A}$ is not diagonalizable but has a Jordan form $\mathbf{J}$, and $e^{\mathbf{A}t} = \mathbf{T}e^{\mathbf{J}t}\mathbf{T}^{-1}$ replaces the formula $\mathbf{T}e^{\mathbf{D}t}\mathbf{T}^{-1}$ of [[§33★ Fundamental Matrices|§33★]].

## Repeated Eigenvalues

Let $r = \rho$ be an $m$-fold root of the characteristic equation $\det(\mathbf{A} - r\mathbf{I}) = 0$ (7), so that $\rho$ is an eigenvalue of algebraic multiplicity $m$. Its geometric multiplicity, the number of linearly independent eigenvectors, may be less than $m$ ([[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-3|Theorem §29.3]]). There are two possibilities.

> [!theorem] Proposition §34.1: A Repeated Eigenvalue with a Full Set of Eigenvectors
> Let $\rho$ be an eigenvalue of $\mathbf{A}$ of algebraic multiplicity $m$ that has $m$ linearly independent eigenvectors $\boldsymbol{\xi}^{(1)}, \ldots, \boldsymbol{\xi}^{(m)}$. Then
>
> $$
> \mathbf{x}^{(1)}(t) = \boldsymbol{\xi}^{(1)}e^{\rho t}, \quad \ldots, \quad \mathbf{x}^{(m)}(t) = \boldsymbol{\xi}^{(m)}e^{\rho t}
> $$
>
> are $m$ linearly independent solutions of $\mathbf{x}' = \mathbf{A}\mathbf{x}$, so the repetition of $\rho$ makes no difference. This case always occurs if $\mathbf{A}$ is Hermitian (or real and symmetric).
>
> *BDP: 7.8 (text)*

^prop-34-1

> [!proof]+ Proof
> Each is a solution: $(\boldsymbol{\xi}^{(i)}e^{\rho t})' = \rho\boldsymbol{\xi}^{(i)}e^{\rho t} = \mathbf{A}\boldsymbol{\xi}^{(i)}e^{\rho t}$. If $\sum_i c_i\boldsymbol{\xi}^{(i)}e^{\rho t} = \mathbf{0}$ at some $t$, then dividing by $e^{\rho t} \ne 0$ gives $\sum_i c_i\boldsymbol{\xi}^{(i)} = \mathbf{0}$, so all $c_i = 0$: the solutions are linearly independent at every $t$.
>
> **The Hermitian case.** A Hermitian matrix has a full set of $n$ linearly independent eigenvectors, regardless of the multiplicities of its eigenvalues ([[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-5|Theorem §29.5]]). With them as the columns of $\mathbf{T}$, [[§33★ Fundamental Matrices#^thm-33-7|Theorem §33.7]] gives $\mathbf{T}^{-1}\mathbf{A}\mathbf{T} = \mathbf{D} = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$, and
>
> $$
> \det(\mathbf{A} - r\mathbf{I}) = \det\big(\mathbf{T}^{-1}(\mathbf{A} - r\mathbf{I})\mathbf{T}\big) = \det(\mathbf{D} - r\mathbf{I}) = (\lambda_1 - r)\cdots(\lambda_n - r) .
> $$
>
> Since $\rho$ is an $m$-fold root, exactly $m$ of the $\lambda_k$ equal $\rho$, so $m$ of these independent eigenvectors belong to $\rho$.

^pf-34-1

*Uses:* [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-5|§29.5]] (Hermitian matrices), [[§33★ Fundamental Matrices#^thm-33-7|§33.7]]

> [!remark]- Connections
> - In Lay's terms the geometric multiplicity of an eigenvalue is at most its algebraic multiplicity, [[§34 Diagonalization#^thm-34-3|235 Thm. §34.3]](a), and the hypothesis here is the case of equality; when this holds for every eigenvalue, $\mathbf{A}$ is diagonalizable ([[§34 Diagonalization#^thm-34-3|235 Thm. §34.3]](b)) and the eigenvector solutions form a fundamental set.

If $\mathbf{A}$ is not Hermitian, $\rho$ may have fewer than $m$ independent eigenvectors, and then fewer than $m$ solutions of the form $\boldsymbol{\xi}e^{\rho t}$; other solutions must be found.

> [!example] Example §34.1: A Double Eigenvalue with Only One Eigenvector
> Find a fundamental set of solutions of
>
> $$
> \mathbf{x}' = \mathbf{A}\mathbf{x} = \begin{pmatrix} 1 & -1 \\ 1 & 3 \end{pmatrix}\mathbf{x} \qquad (8)
> $$
>
> and describe its phase portrait.
>
> **Eigenvalues and eigenvectors.** The eigenvalues are the roots of
>
> $$
> \det(\mathbf{A} - r\mathbf{I}) = \begin{vmatrix} 1 - r & -1 \\ 1 & 3 - r \end{vmatrix} = (1 - r)(3 - r) + 1 = r^2 - 4r + 4 = (r - 2)^2 = 0, \qquad (4)
> $$
>
> so $r_1 = r_2 = 2$: the eigenvalue $2$ has algebraic multiplicity $2$. For $r = 2$, $(\mathbf{A} - 2\mathbf{I})\boldsymbol{\xi} = \mathbf{0}$ reads
>
> $$
> \begin{pmatrix} -1 & -1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} \xi_1 \\ \xi_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}, \qquad (5)
> $$
>
> the single condition $\xi_1 + \xi_2 = 0$. So every eigenvector is a multiple of $\boldsymbol{\xi} = (1, -1)^T$ (6): only one linearly independent eigenvector. One solution is
>
> $$
> \mathbf{x}^{(1)}(t) = \begin{pmatrix} 1 \\ -1 \end{pmatrix}e^{2t}, \qquad (9)
> $$
>
> and there is no second solution of the form $\boldsymbol{\xi}e^{rt}$.
>
> **The form $\boldsymbol{\xi}te^{2t}$ fails.** Imitating [[§16 Repeated Roots; Reduction of Order#^thm-16-1|Theorem §16.1]], try $\mathbf{x} = \boldsymbol{\xi}te^{2t}$ (10). Substituting into (8),
>
> $$
> 2\boldsymbol{\xi}te^{2t} + \boldsymbol{\xi}e^{2t} = \mathbf{A}\boldsymbol{\xi}te^{2t} . \qquad (11)
> $$
>
> For this to hold for all $t$, the coefficients of $te^{2t}$ and of $e^{2t}$ must agree on both sides; the $e^{2t}$ terms give $\boldsymbol{\xi} = \mathbf{0}$ (12).
>
> **The form $\boldsymbol{\xi}te^{2t} + \boldsymbol{\eta}e^{2t}$.** Since (11) has both $te^{2t}$ and $e^{2t}$ terms, assume
>
> $$
> \mathbf{x} = \boldsymbol{\xi}te^{2t} + \boldsymbol{\eta}e^{2t} \qquad (13)
> $$
>
> with constant vectors $\boldsymbol{\xi}$, $\boldsymbol{\eta}$. Substituting,
>
> $$
> 2\boldsymbol{\xi}te^{2t} + (\boldsymbol{\xi} + 2\boldsymbol{\eta})e^{2t} = \mathbf{A}(\boldsymbol{\xi}te^{2t} + \boldsymbol{\eta}e^{2t}) , \qquad (14)
> $$
>
> and equating coefficients of $te^{2t}$ and $e^{2t}$ gives $2\boldsymbol{\xi} = \mathbf{A}\boldsymbol{\xi}$ and $\boldsymbol{\xi} + 2\boldsymbol{\eta} = \mathbf{A}\boldsymbol{\eta}$, that is,
>
> $$
> (\mathbf{A} - 2\mathbf{I})\boldsymbol{\xi} = \mathbf{0}, \qquad (15) \qquad\qquad (\mathbf{A} - 2\mathbf{I})\boldsymbol{\eta} = \boldsymbol{\xi} . \qquad (16)
> $$
>
> Take $\boldsymbol{\xi} = (1, -1)^T$. Although $\det(\mathbf{A} - 2\mathbf{I}) = 0$, (16) is solvable: its augmented matrix
>
> $$
> \left(\begin{array}{cc|c} -1 & -1 & 1 \\ 1 & 1 & -1 \end{array}\right)
> $$
>
> has its second row proportional to the first, leaving $-\eta_1 - \eta_2 = 1$. With $\eta_1 = k$ arbitrary, $\eta_2 = -1 - k$, and
>
> $$
> \boldsymbol{\eta} = \begin{pmatrix} k \\ -1 - k \end{pmatrix} = \begin{pmatrix} 0 \\ -1 \end{pmatrix} + k\begin{pmatrix} 1 \\ -1 \end{pmatrix} . \qquad (17)
> $$
>
> Substituting into (13),
>
> $$
> \mathbf{x} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}te^{2t} + \begin{pmatrix} 0 \\ -1 \end{pmatrix}e^{2t} + k\begin{pmatrix} 1 \\ -1 \end{pmatrix}e^{2t} . \qquad (18)
> $$
>
> The last term is a multiple of $\mathbf{x}^{(1)}$ and may be dropped; the first two form a new solution
>
> $$
> \mathbf{x}^{(2)}(t) = \begin{pmatrix} 1 \\ -1 \end{pmatrix}te^{2t} + \begin{pmatrix} 0 \\ -1 \end{pmatrix}e^{2t} . \qquad (19)
> $$
>
> **Fundamental set.**
>
> $$
> W[\mathbf{x}^{(1)}, \mathbf{x}^{(2)}](t) = \begin{vmatrix} e^{2t} & te^{2t} \\ -e^{2t} & -te^{2t} - e^{2t} \end{vmatrix} = -te^{4t} - e^{4t} + te^{4t} = -e^{4t} \ne 0,
> $$
>
> so $\mathbf{x}^{(1)}$, $\mathbf{x}^{(2)}$ form a fundamental set, and the general solution is
>
> $$
> \mathbf{x} = c_1\begin{pmatrix} 1 \\ -1 \end{pmatrix}e^{2t} + c_2\left[\begin{pmatrix} 1 \\ -1 \end{pmatrix}te^{2t} + \begin{pmatrix} 0 \\ -1 \end{pmatrix}e^{2t}\right] . \qquad (20)
> $$
>
> **Phase portrait.** Every term has the factor $e^{2t}$, so $\mathbf{x} \to \mathbf{0}$ as $t \to -\infty$, and unless $c_1 = c_2 = 0$, $\mathbf{x}$ is unbounded as $t \to \infty$. Along a trajectory with $c_2 \ne 0$,
>
> $$
> \frac{x_2(t)}{x_1(t)} = \frac{-c_1e^{2t} + c_2(-te^{2t} - e^{2t})}{c_1e^{2t} + c_2te^{2t}} = \frac{-c_1 - c_2 - c_2t}{c_1 + c_2t} \longrightarrow -1 \qquad (t \to \pm\infty),
> $$
>
> and for $c_2 = 0$ the ratio is $-1$ exactly. So every trajectory approaches the origin, as $t \to -\infty$, tangent to the eigenvector line $x_2 = -x_1$, and its slope also tends to $-1$ as $t \to \infty$. Yet the trajectories with $c_2 \ne 0$ have no asymptote as $t \to \infty$: $x_1 + x_2 = -c_2e^{2t} \to \pm\infty$, so they move ever farther from every line $x_1 + x_2 = \text{const}$. Thus the trajectories leave the origin tangent to the eigenvector line, turn, and run off nearly parallel to it, on the side fixed by the sign of $c_2$.
>
> *BDP: Examples 7.8.1 and 7.8.2*

^ex-34-1

![[m331-34-1.svg]]
*Phase portrait of [[§34★ Repeated Eigenvalues#^ex-34-1|Example §34.1]], computed from $\mathbf{x}(t) = e^{2t}[\mathbf{I} + t(\mathbf{A} - 2\mathbf{I})]\mathbf{x}(0)$ ([[§34★ Repeated Eigenvalues#^ex-34-2|Example §34.2]]). Green: the eigenvector line $x_2 = -x_1$, carrying $\pm\mathbf{x}^{(1)}$. Red: $\pm\mathbf{x}^{(2)}$, through $(0, \mp1)$ at $t = 0$. Every trajectory leaves the origin tangent to the eigenvector line and turns to run off nearly parallel to it: an unstable improper node. The grey arrows are the direction field $\mathbf{A}\mathbf{x}$.*

> [!definition] Definition §34.1: Improper Node
> For a $2 \times 2$ system $\mathbf{x}' = \mathbf{A}\mathbf{x}$ whose coefficient matrix has a repeated eigenvalue with only one independent eigenvector, the origin is called an **improper node**. If the eigenvalue is negative, the trajectories are like those of [[§34★ Repeated Eigenvalues#^ex-34-1|Example §34.1]] but traversed inward, and the improper node is asymptotically stable; if it is positive, the node is unstable.
>
> *BDP: 7.8 (text)*

^def-34-1

One difference from a single second-order equation shows here. For a repeated root $r_1$ of $ay'' + by' + cy = 0$, a term $ce^{r_1t}$ in the second solution is not needed, since it is a multiple of the first solution. For a system, the term $\boldsymbol{\eta}e^{r_1t}$ in (13) is in general *not* a multiple of $\boldsymbol{\xi}e^{r_1t}$, and it must be kept.

[[§34★ Repeated Eigenvalues#^ex-34-1|Example §34.1]] is entirely typical of a double eigenvalue with a single eigenvector.

> [!theorem] Theorem §34.2: Double Eigenvalue with One Eigenvector
> Suppose $r = \rho$ is a double eigenvalue of $\mathbf{A}$ with only one linearly independent eigenvector $\boldsymbol{\xi}$:
>
> $$
> (\mathbf{A} - \rho\mathbf{I})\boldsymbol{\xi} = \mathbf{0} . \qquad (22)
> $$
>
> Then the equation
>
> $$
> (\mathbf{A} - \rho\mathbf{I})\boldsymbol{\eta} = \boldsymbol{\xi} \qquad (24)
> $$
>
> always has a solution $\boldsymbol{\eta}$, unique up to adding a multiple of $\boldsymbol{\xi}$, even though $\det(\mathbf{A} - \rho\mathbf{I}) = 0$; and
>
> $$
> \mathbf{x}^{(1)}(t) = \boldsymbol{\xi}e^{\rho t}, \qquad \mathbf{x}^{(2)}(t) = \boldsymbol{\xi}te^{\rho t} + \boldsymbol{\eta}e^{\rho t} \qquad (21),\ (23)
> $$
>
> are linearly independent solutions of $\mathbf{x}' = \mathbf{A}\mathbf{x}$.
>
> *BDP: 7.8 (text), Equations (21)–(24)*

^thm-34-2

> [!proof]+ Proof
> Write $\mathbf{N} = \mathbf{A} - \rho\mathbf{I}$, so (22) and (24) read $\mathbf{N}\boldsymbol{\xi} = \mathbf{0}$ and $\mathbf{N}\boldsymbol{\eta} = \boldsymbol{\xi}$.
>
> **Solutions.** $\mathbf{x}^{(1)}$ is a solution as in [[§34★ Repeated Eigenvalues#^prop-34-1|Proposition §34.1]]. For $\mathbf{x}^{(2)}$,
>
> $$
> \mathbf{x}^{(2)\prime} = \rho\boldsymbol{\xi}te^{\rho t} + (\boldsymbol{\xi} + \rho\boldsymbol{\eta})e^{\rho t}, \qquad \mathbf{A}\mathbf{x}^{(2)} = (\mathbf{A}\boldsymbol{\xi})te^{\rho t} + (\mathbf{A}\boldsymbol{\eta})e^{\rho t} = \rho\boldsymbol{\xi}te^{\rho t} + (\rho\boldsymbol{\eta} + \boldsymbol{\xi})e^{\rho t},
> $$
>
> using $\mathbf{A}\boldsymbol{\xi} = \rho\boldsymbol{\xi}$ and $\mathbf{A}\boldsymbol{\eta} = \rho\boldsymbol{\eta} + \boldsymbol{\xi}$. The two agree.
>
> **Independence.** $\boldsymbol{\eta}$ is not a multiple of $\boldsymbol{\xi}$: if $\boldsymbol{\eta} = c\boldsymbol{\xi}$, then $\boldsymbol{\xi} = \mathbf{N}\boldsymbol{\eta} = c\mathbf{N}\boldsymbol{\xi} = \mathbf{0}$, which is impossible for an eigenvector. If $a\mathbf{x}^{(1)}(t) + b\mathbf{x}^{(2)}(t) = \mathbf{0}$ at some $t$, then $e^{\rho t}[(a + bt)\boldsymbol{\xi} + b\boldsymbol{\eta}] = \mathbf{0}$, and independence of $\boldsymbol{\xi}, \boldsymbol{\eta}$ gives $b = 0$, then $a = 0$.
>
> **Solvability of (24).** (BDP: "it can be shown that it is always possible to solve equation (24) … we will not present all of the details". Here they are.)
> - *The $2 \times 2$ case.* $\mathbf{N}$ has the one-dimensional null space $\operatorname{span}\{\boldsymbol{\xi}\}$, so its column space is a line, spanned by some $\mathbf{w} \ne \mathbf{0}$. Since $\mathbf{N}\mathbf{w}$ lies in the column space, $\mathbf{N}\mathbf{w} = \mu\mathbf{w}$ for some $\mu$, so $\mu$ is an eigenvalue of $\mathbf{N}$. The eigenvalues of $\mathbf{N}$ are those of $\mathbf{A}$ minus $\rho$ (as $\mathbf{N} - \mu\mathbf{I} = \mathbf{A} - (\rho + \mu)\mathbf{I}$), and $\rho$ is the only eigenvalue of $\mathbf{A}$; so $\mu = 0$ and $\mathbf{w}$ lies in the null space $\operatorname{span}\{\boldsymbol{\xi}\}$. Hence the column space of $\mathbf{N}$ is $\operatorname{span}\{\boldsymbol{\xi}\}$, and $\boldsymbol{\xi} = \mathbf{N}\boldsymbol{\eta}$ for some $\boldsymbol{\eta}$. (This is the argument of [[§35 Eigenvectors and Linear Transformations#^thm-35-3|235 Thm. §35.3]].)
> - *The $n \times n$ case* (over $\mathbb{C}$). Let $G = G(\rho, \mathbf{A})$ be the generalized eigenspace. Its dimension is the algebraic multiplicity $2$ ([[§34 Determinants#^ladr-9-62|LADR 9.62]]), $\mathbf{N}$ maps $G$ into itself, and $\mathbf{N}|_G$ is nilpotent ([[§29 Generalized Eigenspace Decomposition#^ladr-8-22|LADR 8.22]]), so $(\mathbf{N}|_G)^2 = 0$ ([[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-16|LADR 8.16]]). Thus $\mathbf{N}(G)$ lies in the null space of $\mathbf{N}$, which is $\operatorname{span}\{\boldsymbol{\xi}\}$. And $\mathbf{N}(G) \ne \{\mathbf{0}\}$, since otherwise the two-dimensional $G$ would lie in the one-dimensional null space. So $\mathbf{N}(G) = \operatorname{span}\{\boldsymbol{\xi}\}$, and $\boldsymbol{\xi} = \mathbf{N}\boldsymbol{\eta}$ for some $\boldsymbol{\eta} \in G$. (If $\mathbf{A}$, $\rho$ and $\boldsymbol{\xi}$ are real, taking real parts in $\mathbf{N}\boldsymbol{\eta} = \boldsymbol{\xi}$ gives a real solution $\operatorname{Re}\boldsymbol{\eta}$.)
>
> **Uniqueness up to $\boldsymbol{\xi}$.** If $\mathbf{N}\boldsymbol{\eta} = \mathbf{N}\boldsymbol{\eta}' = \boldsymbol{\xi}$, then $\mathbf{N}(\boldsymbol{\eta} - \boldsymbol{\eta}') = \mathbf{0}$, so $\boldsymbol{\eta} - \boldsymbol{\eta}'$ is a multiple of $\boldsymbol{\xi}$. Adding $k\boldsymbol{\xi}$ to $\boldsymbol{\eta}$ adds $k\mathbf{x}^{(1)}$ to $\mathbf{x}^{(2)}$, as in (18).

^pf-34-2

*Uses:* [[§34★ Repeated Eigenvalues#^prop-34-1|§34.1]], [[§35 Eigenvectors and Linear Transformations#^thm-35-3|235 Thm. §35.3]], [[§34 Determinants#^ladr-9-62|LADR 9.62]], [[§29 Generalized Eigenspace Decomposition#^ladr-8-22|LADR 8.22]], [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-16|LADR 8.16]]

Multiplying (24) by $\mathbf{A} - \rho\mathbf{I}$ and using (22) gives
$$
(\mathbf{A} - \rho\mathbf{I})^2\boldsymbol{\eta} = \mathbf{0} .
$$

> [!definition] Definition §34.2: Generalized Eigenvector
> A vector $\boldsymbol{\eta}$ satisfying $(\mathbf{A} - \rho\mathbf{I})\boldsymbol{\eta} = \boldsymbol{\xi}$, where $\boldsymbol{\xi}$ is an eigenvector of $\mathbf{A}$ for the eigenvalue $\rho$, is called a **generalized eigenvector** of $\mathbf{A}$ corresponding to $\rho$. It satisfies $(\mathbf{A} - \rho\mathbf{I})^2\boldsymbol{\eta} = \mathbf{0}$ but $(\mathbf{A} - \rho\mathbf{I})\boldsymbol{\eta} \ne \mathbf{0}$.
>
> *BDP: 7.8 (text)*

^def-34-2

> [!remark]- Connections
> - Rigorous treatment: [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-8|LADR 8.8]]. Axler calls any $v \ne 0$ with $(T - \lambda I)^kv = 0$ for some $k$ a generalized eigenvector, so eigenvectors are included; BDP's $\boldsymbol{\eta}$ is the case $k = 2$ that is not an eigenvector. Over $\mathbb{C}$ every operator has a basis of generalized eigenvectors, [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-9|LADR 8.9]], which is why this method never runs out of solutions.
> - Lay meets the same vector in [[§35 Eigenvectors and Linear Transformations#^ex-35-3|235 Ex. §35.3]], where $(A + 2I)\mathbf{b}_2 = \mathbf{b}_1$.

> [!remark] Remark: Method — Double Eigenvalue with One Eigenvector
> To solve $\mathbf{x}' = \mathbf{A}\mathbf{x}$ when $\rho$ is a double root of $\det(\mathbf{A} - r\mathbf{I}) = 0$:
> 1. **Find the eigenvectors** for $\rho$ by row reducing $\mathbf{A} - \rho\mathbf{I}$. If there are two independent ones, use $\boldsymbol{\xi}^{(1)}e^{\rho t}$, $\boldsymbol{\xi}^{(2)}e^{\rho t}$ ([[§34★ Repeated Eigenvalues#^prop-34-1|Proposition §34.1]]) and stop.
> 2. **If there is only one, $\boldsymbol{\xi}$,** solve $(\mathbf{A} - \rho\mathbf{I})\boldsymbol{\eta} = \boldsymbol{\xi}$ by row reduction. Any particular solution will do; the free multiple of $\boldsymbol{\xi}$ only adds a multiple of the first solution.
> 3. **Write** $\mathbf{x}^{(1)} = \boldsymbol{\xi}e^{\rho t}$ and $\mathbf{x}^{(2)} = \boldsymbol{\xi}te^{\rho t} + \boldsymbol{\eta}e^{\rho t}$; the general solution is $c_1\mathbf{x}^{(1)} + c_2\mathbf{x}^{(2)}$ plus the solutions from the other eigenvalues.
> 4. **Initial conditions:** at $t = 0$, $\mathbf{x}^{(1)}(0) = \boldsymbol{\xi}$ and $\mathbf{x}^{(2)}(0) = \boldsymbol{\eta}$, so solve $c_1\boldsymbol{\xi} + c_2\boldsymbol{\eta} + \cdots = \mathbf{x}^0$.
>
> The steps can also be run in reverse order (BDP, Problem 15): for a $2 \times 2$ matrix, $(\mathbf{A} - \rho\mathbf{I})^2 = \mathbf{0}$, so any $\boldsymbol{\eta}$ that is not an eigenvector works, and then $\boldsymbol{\xi} = (\mathbf{A} - \rho\mathbf{I})\boldsymbol{\eta}$ is automatically an eigenvector. In [[§34★ Repeated Eigenvalues#^ex-34-1|Example §34.1]], $(\mathbf{A} - 2\mathbf{I})^2 = \begin{pmatrix} -1 & -1 \\ 1 & 1 \end{pmatrix}^2 = \mathbf{0}$, and $\boldsymbol{\eta} = (0, -1)^T$ gives back $\boldsymbol{\xi} = (1, -1)^T$.

^rem-34-1

## Fundamental Matrices

Fundamental matrices are formed, as in [[§33★ Fundamental Matrices#^def-33-1|Definition §33.1]], by arranging linearly independent solutions in columns.

> [!example] Example §34.2: Ψ and Φ = exp(At) for Example §34.1
> From the solutions (9) and (19), a fundamental matrix for the system (8) is
>
> $$
> \mathbf{\Psi}(t) = \begin{pmatrix} e^{2t} & te^{2t} \\ -e^{2t} & -te^{2t} - e^{2t} \end{pmatrix} = e^{2t}\begin{pmatrix} 1 & t \\ -1 & -1 - t \end{pmatrix} . \qquad (25)
> $$
>
> The fundamental matrix with $\mathbf{\Phi}(0) = \mathbf{I}$ is $\mathbf{\Phi}(t) = \mathbf{\Psi}(t)\mathbf{\Psi}^{-1}(0)$ ([[§33★ Fundamental Matrices#^thm-33-2|Theorem §33.2]]). Here
>
> $$
> \mathbf{\Psi}(0) = \begin{pmatrix} 1 & 0 \\ -1 & -1 \end{pmatrix}, \qquad \mathbf{\Psi}^{-1}(0) = \begin{pmatrix} 1 & 0 \\ -1 & -1 \end{pmatrix} \qquad (26)
> $$
>
> (the matrix is its own inverse: its square is $\begin{pmatrix} 1 & 0 \\ -1 + 1 & 0 + 1 \end{pmatrix} = \mathbf{I}$), so
>
> $$
> \mathbf{\Phi}(t) = e^{2t}\begin{pmatrix} 1 & t \\ -1 & -1 - t \end{pmatrix}\begin{pmatrix} 1 & 0 \\ -1 & -1 \end{pmatrix} = e^{2t}\begin{pmatrix} 1 - t & -t \\ t & 1 + t \end{pmatrix} . \qquad (27)
> $$
>
> By [[§33★ Fundamental Matrices#^thm-33-4|Theorem §33.4]] this is $e^{\mathbf{A}t}$, and the solution of $\mathbf{x}' = \mathbf{A}\mathbf{x}$, $\mathbf{x}(0) = \mathbf{x}^0$ is $\mathbf{x}(t) = e^{\mathbf{A}t}\mathbf{x}^0 = \mathbf{\Phi}(t)\mathbf{x}^0$. Note the form of the answer: $\mathbf{\Phi}(t) = e^{2t}[\mathbf{I} + t(\mathbf{A} - 2\mathbf{I})]$, since $\mathbf{A} - 2\mathbf{I} = \begin{pmatrix} -1 & -1 \\ 1 & 1 \end{pmatrix}$.
>
> *BDP: 7.8 (text)*

^ex-34-2

## Jordan Forms

A matrix can be diagonalized as in [[§33★ Fundamental Matrices#^thm-33-7|Theorem §33.7]] only if it has a full complement of $n$ linearly independent eigenvectors. When repeated eigenvalues leave a shortage of eigenvectors, the best possible is a nearly diagonal matrix.

> [!definition] Definition §34.3: Jordan Form
> An $n \times n$ matrix $\mathbf{A}$ can always be transformed, $\mathbf{T}^{-1}\mathbf{A}\mathbf{T} = \mathbf{J}$, into a nearly diagonal matrix $\mathbf{J}$, its **Jordan form**: $\mathbf{J}$ has the eigenvalues of $\mathbf{A}$ on the main diagonal, ones in certain positions on the diagonal above the main diagonal, and zeros elsewhere. The columns of $\mathbf{T}$ are eigenvectors and generalized eigenvectors; $\mathbf{J}$ has a $1$ above the main diagonal in each column corresponding to an eigenvector that is lacking (and is replaced in $\mathbf{T}$ by a generalized eigenvector).
>
> *BDP: 7.8 (text)*

^def-34-3

*BDP omits the proof that every matrix has a Jordan form ("requires a greater background in linear algebra"); see [[§30 Consequences of Generalized Eigenspace Decomposition#^ladr-8-46|LADR 8.46]] (over $\mathbb{C}$), and for $2 \times 2$ matrices with real eigenvalues [[§35 Eigenvectors and Linear Transformations#^thm-35-3|235 Thm. §35.3]].*

> [!remark]- Connections
> - Hub: [[Jordan form]]. Axler builds a Jordan basis from the generalized eigenspace decomposition, [[§29 Generalized Eigenspace Decomposition#^ladr-8-22|LADR 8.22]], and a Jordan basis for each nilpotent part, [[§30 Consequences of Generalized Eigenspace Decomposition#^ladr-8-45|LADR 8.45]].
> - In the plane: a real $2 \times 2$ matrix is similar to $\operatorname{diag}(\lambda_1, \lambda_2)$, to $\lambda\mathbf{I}$ or to $\begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix}$ when its eigenvalues are real ([[§35 Eigenvectors and Linear Transformations#^thm-35-3|235 Thm. §35.3]]), and to a rotation–scaling matrix when they are complex ([[§36 Complex Eigenvalues#^thm-36-4|235 Thm. §36.4]]). These normal forms are the phase-portrait cases of BDP 7.5, 7.6 and 7.8.

> [!example] Example §34.3: The Jordan Form of A and exp(Jt)
> Transform $\mathbf{A} = \begin{pmatrix} 1 & -1 \\ 1 & 3 \end{pmatrix}$ of [[§34★ Repeated Eigenvalues#^ex-34-1|Example §34.1]] into its Jordan form, and use it to find a fundamental matrix of $\mathbf{x}' = \mathbf{A}\mathbf{x}$.
>
> **The Jordan form.** Put the eigenvector $\boldsymbol{\xi} = (1, -1)^T$ in the first column of $\mathbf{T}$ and the generalized eigenvector $\boldsymbol{\eta} = (0, -1)^T$ ($k = 0$ in (17)) in the second:
>
> $$
> \mathbf{T} = \begin{pmatrix} 1 & 0 \\ -1 & -1 \end{pmatrix}, \qquad \mathbf{T}^{-1} = \begin{pmatrix} 1 & 0 \\ -1 & -1 \end{pmatrix} . \qquad (28)
> $$
>
> Then $\mathbf{A}\mathbf{T} = \begin{pmatrix} 2 & 1 \\ -2 & -3 \end{pmatrix}$ and
>
> $$
> \mathbf{T}^{-1}\mathbf{A}\mathbf{T} = \begin{pmatrix} 1 & 0 \\ -1 & -1 \end{pmatrix}\begin{pmatrix} 2 & 1 \\ -2 & -3 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = \mathbf{J} . \qquad (29)
> $$
>
> Column by column, $\mathbf{A}\mathbf{T} = \mathbf{T}\mathbf{J}$ says $\mathbf{A}\boldsymbol{\xi} = 2\boldsymbol{\xi}$ and $\mathbf{A}\boldsymbol{\eta} = \boldsymbol{\xi} + 2\boldsymbol{\eta}$, which are (15) and (16); the $1$ sits in the column of the missing eigenvector.
>
> **The system $\mathbf{y}' = \mathbf{J}\mathbf{y}$.** The substitution $\mathbf{x} = \mathbf{T}\mathbf{y}$ gives $\mathbf{y}' = \mathbf{J}\mathbf{y}$ (30), as in [[§33★ Fundamental Matrices#^thm-33-8|Theorem §33.8]](a). In scalar form,
>
> $$
> y_1' = 2y_1 + y_2, \qquad y_2' = 2y_2 . \qquad (31)
> $$
>
> This is not uncoupled, but it can be solved in reverse order. First $y_2 = c_1e^{2t}$. Then $y_1' - 2y_1 = c_1e^{2t}$; with the integrating factor $e^{-2t}$ ([[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-2|Theorem §4.2]]), $(e^{-2t}y_1)' = c_1$, so $y_1 = c_1te^{2t} + c_2e^{2t}$ (32). Two independent solutions are
>
> $$
> \mathbf{y}^{(1)}(t) = \begin{pmatrix} 1 \\ 0 \end{pmatrix}e^{2t}, \qquad \mathbf{y}^{(2)}(t) = \begin{pmatrix} t \\ 1 \end{pmatrix}e^{2t}, \qquad (33)
> $$
>
> with fundamental matrix
>
> $$
> \hat{\mathbf{\Psi}}(t) = \begin{pmatrix} e^{2t} & te^{2t} \\ 0 & e^{2t} \end{pmatrix} . \qquad (34)
> $$
>
> Since $\hat{\mathbf{\Psi}}(0) = \mathbf{I}$, this is $e^{\mathbf{J}t}$ ([[§33★ Fundamental Matrices#^thm-33-4|Theorem §33.4]]), in agreement with [[§34★ Repeated Eigenvalues#^prop-34-3|Proposition §34.3]] below.
>
> **Back to $\mathbf{x}$.**
>
> $$
> \mathbf{\Psi}(t) = \mathbf{T}e^{\mathbf{J}t} = \begin{pmatrix} 1 & 0 \\ -1 & -1 \end{pmatrix}\begin{pmatrix} e^{2t} & te^{2t} \\ 0 & e^{2t} \end{pmatrix} = \begin{pmatrix} e^{2t} & te^{2t} \\ -e^{2t} & -e^{2t} - te^{2t} \end{pmatrix}, \qquad (35)
> $$
>
> the fundamental matrix (25) of [[§34★ Repeated Eigenvalues#^ex-34-2|Example §34.2]].
>
> *BDP: 7.8 (text)*

^ex-34-3

> [!theorem] Proposition §34.3: Exponentials of Jordan Blocks
> Let $\lambda$ be a real number.
>
> (a) If $\mathbf{J} = \begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix}$, then
>
> $$
> \mathbf{J}^k = \begin{pmatrix} \lambda^k & k\lambda^{k-1} \\ 0 & \lambda^k \end{pmatrix} \quad (k \ge 1), \qquad e^{\mathbf{J}t} = e^{\lambda t}\begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix} .
> $$
>
> (b) If $\mathbf{J} = \begin{pmatrix} \lambda & 1 & 0 \\ 0 & \lambda & 1 \\ 0 & 0 & \lambda \end{pmatrix}$, then
>
> $$
> \mathbf{J}^k = \begin{pmatrix} \lambda^k & k\lambda^{k-1} & \frac12 k(k-1)\lambda^{k-2} \\ 0 & \lambda^k & k\lambda^{k-1} \\ 0 & 0 & \lambda^k \end{pmatrix} \quad (k \ge 1), \qquad e^{\mathbf{J}t} = e^{\lambda t}\begin{pmatrix} 1 & t & \frac12 t^2 \\ 0 & 1 & t \\ 0 & 0 & 1 \end{pmatrix} .
> $$
>
> *BDP: Problems 7.8.19 and 7.8.21*

^prop-34-3

> [!proof]+ Proof
> **Powers**, by induction on $k$; at $k = 1$ the formulas give $\mathbf{J}$ (read $\frac12k(k-1)\lambda^{k-2} = 0$ for $k = 1$). In (a), $\mathbf{J}^{k+1} = \mathbf{J}^k\mathbf{J}$ has $(1, 2)$ entry $\lambda^k \cdot 1 + k\lambda^{k-1} \cdot \lambda = (k+1)\lambda^k$, and its other entries are clearly $\lambda^{k+1}$, $0$, $\lambda^{k+1}$. In (b) the diagonal and the first superdiagonal work the same way, and the $(1, 3)$ entry of $\mathbf{J}^k\mathbf{J}$ is
>
> $$
> \lambda^k \cdot 0 + k\lambda^{k-1} \cdot 1 + \tfrac12k(k-1)\lambda^{k-2} \cdot \lambda = \big(k + \tfrac12k(k-1)\big)\lambda^{k-1} = \tfrac12(k+1)k\,\lambda^{k-1} .
> $$
>
> **Exponentials**, entry by entry from the series (23) ([[§33★ Fundamental Matrices#^def-33-3|Definition §33.3]]). The diagonal entries are $\sum_{k\ge0} \lambda^kt^k/k! = e^{\lambda t}$. A first-superdiagonal entry is
>
> $$
> \sum_{k\ge1} \frac{k\lambda^{k-1}t^k}{k!} = t\sum_{k\ge1} \frac{(\lambda t)^{k-1}}{(k-1)!} = te^{\lambda t},
> $$
>
> and in (b) the $(1, 3)$ entry is
>
> $$
> \sum_{k\ge2} \frac{\frac12k(k-1)\lambda^{k-2}t^k}{k!} = \frac{t^2}{2}\sum_{k\ge2} \frac{(\lambda t)^{k-2}}{(k-2)!} = \frac{t^2}{2}e^{\lambda t}
> $$
>
> ([[§78 Taylor and Maclaurin Series#^thm-78-6|Calc Thm. §78.6]]). The entries below the diagonal are $0$ in every power.

^pf-34-3

*Uses:* [[§33★ Fundamental Matrices#^def-33-3|Def. §33.3]], [[§78 Taylor and Maclaurin Series#^thm-78-6|Calc Thm. §78.6]]

> [!remark] Remark: Jordan Form and the Matrix Exponential
> If $\mathbf{T}^{-1}\mathbf{A}\mathbf{T} = \mathbf{J}$, the proof of [[§33★ Fundamental Matrices#^thm-33-8|Theorem §33.8]] goes through with $\mathbf{J}$ in place of $\mathbf{D}$: $\mathbf{x} = \mathbf{T}\mathbf{y}$ turns $\mathbf{x}' = \mathbf{A}\mathbf{x}$ into $\mathbf{y}' = \mathbf{J}\mathbf{y}$, $\mathbf{\Psi}(t) = \mathbf{T}e^{\mathbf{J}t}$ is a fundamental matrix, and
>
> $$
> e^{\mathbf{A}t} = \mathbf{T}e^{\mathbf{J}t}\mathbf{T}^{-1} .
> $$
>
> For [[§34★ Repeated Eigenvalues#^ex-34-3|Example §34.3]] this gives $\begin{pmatrix} 1 & 0 \\ -1 & -1 \end{pmatrix} e^{2t}\begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ -1 & -1 \end{pmatrix} = e^{2t}\begin{pmatrix} 1 - t & -t \\ t & 1 + t \end{pmatrix}$, the $\mathbf{\Phi}(t)$ of [[§34★ Repeated Eigenvalues#^ex-34-2|Example §34.2]]. The entries $te^{\lambda t}$ and $\frac12t^2e^{\lambda t}$ of $e^{\mathbf{J}t}$ are where the factors $t$, $t^2$ in the solutions come from.

^rem-34-2

> [!remark]- Remark: Eigenvalues of Multiplicity 3, and Larger Systems
> If $\rho$ has algebraic multiplicity $3$, it may have one, two or three independent eigenvectors (BDP, preamble to Problems 17–18).
> - **Three eigenvectors:** three solutions $\boldsymbol{\xi}^{(i)}e^{\rho t}$ ([[§34★ Repeated Eigenvalues#^prop-34-1|Proposition §34.1]]).
> - **One eigenvector $\boldsymbol{\xi}$:** the solutions are
>
>   $$
>   \boldsymbol{\xi}e^{\rho t}, \qquad \boldsymbol{\xi}te^{\rho t} + \boldsymbol{\eta}e^{\rho t}, \qquad \boldsymbol{\xi}\frac{t^2}{2}e^{\rho t} + \boldsymbol{\eta}te^{\rho t} + \boldsymbol{\zeta}e^{\rho t},
>   $$
>
>   where $(\mathbf{A} - \rho\mathbf{I})\boldsymbol{\xi} = \mathbf{0}$, $(\mathbf{A} - \rho\mathbf{I})\boldsymbol{\eta} = \boldsymbol{\xi}$, $(\mathbf{A} - \rho\mathbf{I})\boldsymbol{\zeta} = \boldsymbol{\eta}$: a chain of generalized eigenvectors. (Substituting the third: its derivative is $\rho$ times itself plus $\boldsymbol{\xi}te^{\rho t} + \boldsymbol{\eta}e^{\rho t}$, and so is $\mathbf{A}$ times it, by the three equations.) The Jordan form is the $3 \times 3$ block of [[§34★ Repeated Eigenvalues#^prop-34-3|Proposition §34.3]](b).
> - **Two eigenvectors $\boldsymbol{\xi}^{(1)}, \boldsymbol{\xi}^{(2)}$:** two solutions $\boldsymbol{\xi}^{(i)}e^{\rho t}$, and a third $\boldsymbol{\xi}te^{\rho t} + \boldsymbol{\eta}e^{\rho t}$, where now $\boldsymbol{\xi}$ must be a suitable linear combination of $\boldsymbol{\xi}^{(1)}$ and $\boldsymbol{\xi}^{(2)}$ for $(\mathbf{A} - \rho\mathbf{I})\boldsymbol{\eta} = \boldsymbol{\xi}$ to be solvable. Alternatively choose $\boldsymbol{\eta}$ with $(\mathbf{A} - \rho\mathbf{I})^2\boldsymbol{\eta} = \mathbf{0}$, independent of the eigenvectors, and set $\boldsymbol{\xi} = (\mathbf{A} - \rho\mathbf{I})\boldsymbol{\eta}$. The Jordan form has one $2 \times 2$ block and one $1 \times 1$ block for $\rho$.
>
> For large $n$ there may be eigenvalues of high algebraic multiplicity $m$ and much lower geometric multiplicity $q$, giving $m - q$ generalized eigenvectors, and repeated complex eigenvalues when $n \ge 4$. The arithmetic is prohibitive by hand even for $n = 3$ or $4$, so software is used routinely. And when the entries of $\mathbf{A}$ come from measurements, it may not even be clear whether two eigenvalues are equal or merely close together.

^rem-34-3
