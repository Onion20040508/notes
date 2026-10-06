---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 6
section: 43
lay: "6.4"
aliases: ["Lay 6.4"]
tags: [applied-linear-algebra, math235]
---
← [[§42 Orthogonal Projections]] · ↑ [[· 6 Orthogonality and Least Squares]] · [[§44 Least-Squares Problems]] →

*Lay, Section 6.4.*

The Gram–Schmidt process turns any basis $\mathbf{x}_1, \ldots, \mathbf{x}_p$ of a subspace into an orthogonal basis. Each new vector is $\mathbf{x}_k$ minus its projection onto the span of the vectors already built. So every nonzero subspace of $\mathbb{R}^n$ has an orthogonal (and an orthonormal) basis, the fact that makes the projection formula of [[§42 Orthogonal Projections#^thm-42-1|Theorem §42.1]] always usable. Run on the columns of a matrix $A$ with linearly independent columns, the process factors $A = QR$, with $Q$ having orthonormal columns and $R$ upper triangular. The QR factorization is used in [[§44 Least-Squares Problems|§44]] to solve least-squares problems stably.

> [!example] Example §43.1: Two Vectors in ℝ³
> Let $W = \operatorname{Span}\{\mathbf{x}_1, \mathbf{x}_2\}$ with $\mathbf{x}_1 = \begin{bmatrix} 3 \\ 6 \\ 0 \end{bmatrix}$ and $\mathbf{x}_2 = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}$. Construct an orthogonal basis $\{\mathbf{v}_1, \mathbf{v}_2\}$ of $W$, then an orthonormal one.
>
> **Orthogonal basis.** Keep $\mathbf{v}_1 = \mathbf{x}_1$. Let $\mathbf{p}$ be the projection of $\mathbf{x}_2$ onto $\mathbf{x}_1$; the component of $\mathbf{x}_2$ orthogonal to $\mathbf{x}_1$ is $\mathbf{x}_2 - \mathbf{p}$. With $\mathbf{x}_2 \cdot \mathbf{x}_1 = 3 + 12 + 0 = 15$ and $\mathbf{x}_1 \cdot \mathbf{x}_1 = 9 + 36 = 45$,
>
> $$
> \mathbf{v}_2 = \mathbf{x}_2 - \mathbf{p} = \mathbf{x}_2 - \frac{\mathbf{x}_2 \cdot \mathbf{x}_1}{\mathbf{x}_1 \cdot \mathbf{x}_1}\mathbf{x}_1 = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix} - \frac{15}{45}\begin{bmatrix} 3 \\ 6 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 2 \end{bmatrix} .
> $$
>
> $\mathbf{v}_2$ lies in $W$, being a combination of $\mathbf{x}_2$ and $\mathbf{x}_1$. So $\{\mathbf{v}_1, \mathbf{v}_2\}$ is an orthogonal set of nonzero vectors in $W$, linearly independent by [[§41 Orthogonal Sets#^thm-41-1|Theorem §41.1]]; since $\dim W = 2$, it is a basis of $W$.
>
> **Orthonormal basis.** Normalize at the end (this postpones the square roots):
>
> $$
> \mathbf{u}_1 = \frac{1}{\|\mathbf{v}_1\|}\mathbf{v}_1 = \frac{1}{\sqrt{45}}\begin{bmatrix} 3 \\ 6 \\ 0 \end{bmatrix} = \begin{bmatrix} 1/\sqrt5 \\ 2/\sqrt5 \\ 0 \end{bmatrix}, \qquad
> \mathbf{u}_2 = \frac{1}{\|\mathbf{v}_2\|}\mathbf{v}_2 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} .
> $$
>
> *Lay: Examples 6.4.1 and 6.4.3*

^ex-43-1

![[m235-43-1.svg]]
*Example §43.1, drawn in the plane $W$. The first Gram–Schmidt step keeps $\mathbf{v}_1 = \mathbf{x}_1$ and replaces $\mathbf{x}_2$ by its component $\mathbf{v}_2 = \mathbf{x}_2 - \mathbf{p}$ orthogonal to $\mathbf{x}_1$ (red), where $\mathbf{p} = \frac13\mathbf{x}_1$ is the projection of $\mathbf{x}_2$ onto $\mathbf{x}_1$. Both $\{\mathbf{x}_1, \mathbf{x}_2\}$ and $\{\mathbf{v}_1, \mathbf{v}_2\}$ span $W$.*

> [!example] Example §43.2: The Full Process in ℝ⁴
> Let
>
> $$
> \mathbf{x}_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix}, \qquad \mathbf{x}_2 = \begin{bmatrix} 0 \\ 1 \\ 1 \\ 1 \end{bmatrix}, \qquad \mathbf{x}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \\ 1 \end{bmatrix} .
> $$
>
> These are clearly linearly independent (look at the first entries, then the second), so they form a basis of a subspace $W$ of $\mathbb{R}^4$. Construct an orthogonal basis of $W$.
>
> **Step 1.** $\mathbf{v}_1 = \mathbf{x}_1$ and $W_1 = \operatorname{Span}\{\mathbf{x}_1\} = \operatorname{Span}\{\mathbf{v}_1\}$.
>
> **Step 2.** Subtract from $\mathbf{x}_2$ its projection onto $W_1$. Here $\mathbf{x}_2 \cdot \mathbf{v}_1 = 3$ and $\mathbf{v}_1 \cdot \mathbf{v}_1 = 4$:
>
> $$
> \mathbf{v}_2 = \mathbf{x}_2 - \operatorname{proj}_{W_1} \mathbf{x}_2 = \mathbf{x}_2 - \frac{\mathbf{x}_2 \cdot \mathbf{v}_1}{\mathbf{v}_1 \cdot \mathbf{v}_1}\mathbf{v}_1 = \begin{bmatrix} 0 \\ 1 \\ 1 \\ 1 \end{bmatrix} - \frac34\begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} -3/4 \\ 1/4 \\ 1/4 \\ 1/4 \end{bmatrix} .
> $$
>
> $\{\mathbf{v}_1, \mathbf{v}_2\}$ is an orthogonal basis of $W_2 = \operatorname{Span}\{\mathbf{x}_1, \mathbf{x}_2\}$.
>
> **Step 2′ (optional).** Scale to clear fractions: replace $\mathbf{v}_2$ by $\mathbf{v}_2' = 4\mathbf{v}_2 = (-3, 1, 1, 1)$. Scaling does not affect orthogonality or the span.
>
> **Step 3.** Subtract from $\mathbf{x}_3$ its projection onto $W_2$, computed with the orthogonal basis $\{\mathbf{v}_1, \mathbf{v}_2'\}$. With $\mathbf{x}_3 \cdot \mathbf{v}_1 = 2$, $\mathbf{v}_1 \cdot \mathbf{v}_1 = 4$, $\mathbf{x}_3 \cdot \mathbf{v}_2' = 0 + 0 + 1 + 1 = 2$, $\mathbf{v}_2' \cdot \mathbf{v}_2' = 9 + 1 + 1 + 1 = 12$:
>
> $$
> \operatorname{proj}_{W_2} \mathbf{x}_3 = \frac{2}{4}\begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix} + \frac{2}{12}\begin{bmatrix} -3 \\ 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 1/2 - 1/2 \\ 1/2 + 1/6 \\ 1/2 + 1/6 \\ 1/2 + 1/6 \end{bmatrix} = \begin{bmatrix} 0 \\ 2/3 \\ 2/3 \\ 2/3 \end{bmatrix}, \qquad
> \mathbf{v}_3 = \mathbf{x}_3 - \operatorname{proj}_{W_2} \mathbf{x}_3 = \begin{bmatrix} 0 \\ -2/3 \\ 1/3 \\ 1/3 \end{bmatrix} .
> $$
>
> $\mathbf{v}_3$ is in $W$, because $\mathbf{x}_3$ and $\operatorname{proj}_{W_2} \mathbf{x}_3$ are. So $\{\mathbf{v}_1, \mathbf{v}_2', \mathbf{v}_3\}$ is an orthogonal set of nonzero vectors in the $3$-dimensional space $W$, hence an orthogonal basis of $W$ by the Basis Theorem. (Check: $\mathbf{v}_3 \cdot \mathbf{v}_1 = 0 - \frac23 + \frac13 + \frac13 = 0$ and $\mathbf{v}_3 \cdot \mathbf{v}_2' = 0 - \frac23 + \frac13 + \frac13 = 0$.)
>
> *Lay: Example 6.4.2*

^ex-43-2

## The Gram–Schmidt Process

> [!theorem] Theorem §43.1: The Gram–Schmidt Process
> Given a basis $\{\mathbf{x}_1, \ldots, \mathbf{x}_p\}$ for a nonzero subspace $W$ of $\mathbb{R}^n$, define
>
> $$
> \begin{aligned}
> \mathbf{v}_1 &= \mathbf{x}_1 \\
> \mathbf{v}_2 &= \mathbf{x}_2 - \frac{\mathbf{x}_2 \cdot \mathbf{v}_1}{\mathbf{v}_1 \cdot \mathbf{v}_1}\mathbf{v}_1 \\
> \mathbf{v}_3 &= \mathbf{x}_3 - \frac{\mathbf{x}_3 \cdot \mathbf{v}_1}{\mathbf{v}_1 \cdot \mathbf{v}_1}\mathbf{v}_1 - \frac{\mathbf{x}_3 \cdot \mathbf{v}_2}{\mathbf{v}_2 \cdot \mathbf{v}_2}\mathbf{v}_2 \\
> &\ \ \vdots \\
> \mathbf{v}_p &= \mathbf{x}_p - \frac{\mathbf{x}_p \cdot \mathbf{v}_1}{\mathbf{v}_1 \cdot \mathbf{v}_1}\mathbf{v}_1 - \frac{\mathbf{x}_p \cdot \mathbf{v}_2}{\mathbf{v}_2 \cdot \mathbf{v}_2}\mathbf{v}_2 - \cdots - \frac{\mathbf{x}_p \cdot \mathbf{v}_{p-1}}{\mathbf{v}_{p-1} \cdot \mathbf{v}_{p-1}}\mathbf{v}_{p-1} .
> \end{aligned}
> $$
>
> Then $\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ is an orthogonal basis for $W$. In addition,
>
> $$
> \operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\} = \operatorname{Span}\{\mathbf{x}_1, \ldots, \mathbf{x}_k\} \qquad\text{for } 1 \le k \le p . \tag{1}
> $$
>
> *Lay: Theorem 11 (6.4)*

^thm-43-1

> [!proof]+ Proof
> For $1 \le k \le p$ let $W_k = \operatorname{Span}\{\mathbf{x}_1, \ldots, \mathbf{x}_k\}$. We show by induction on $k$ that $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ is an orthogonal basis of $W_k$; for $k = p$ this is the theorem, and for each $k$ it gives (1).
>
> For $k = 1$: $\mathbf{v}_1 = \mathbf{x}_1 \ne \mathbf{0}$ (it belongs to a basis), so $\{\mathbf{v}_1\}$ is an orthogonal basis of $W_1 = \operatorname{Span}\{\mathbf{x}_1\}$.
>
> Suppose that for some $k < p$, $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ is an orthogonal basis of $W_k$. By the formula of the theorem and formula (2) of [[§42 Orthogonal Projections#^thm-42-1|Theorem §42.1]] (applied with this orthogonal basis of $W_k$),
>
> $$
> \mathbf{v}_{k+1} = \mathbf{x}_{k+1} - \operatorname{proj}_{W_k} \mathbf{x}_{k+1} . \tag{2}
> $$
>
> - By the Orthogonal Decomposition Theorem ([[§42 Orthogonal Projections#^thm-42-1|Theorem §42.1]]), $\mathbf{v}_{k+1}$ is orthogonal to $W_k$, in particular to $\mathbf{v}_1, \ldots, \mathbf{v}_k$.
> - $\operatorname{proj}_{W_k} \mathbf{x}_{k+1}$ lies in $W_k \subseteq W_{k+1}$, and $\mathbf{x}_{k+1} \in W_{k+1}$; a subspace is closed under subtraction, so $\mathbf{v}_{k+1} \in W_{k+1}$.
> - $\mathbf{v}_{k+1} \ne \mathbf{0}$: otherwise $\mathbf{x}_{k+1} = \operatorname{proj}_{W_k} \mathbf{x}_{k+1} \in W_k = \operatorname{Span}\{\mathbf{x}_1, \ldots, \mathbf{x}_k\}$, contradicting the linear independence of the $\mathbf{x}$'s.
>
> Hence $\{\mathbf{v}_1, \ldots, \mathbf{v}_{k+1}\}$ is an orthogonal set of $k + 1$ nonzero vectors in $W_{k+1}$, which has dimension $k + 1$ (it has the basis $\mathbf{x}_1, \ldots, \mathbf{x}_{k+1}$). It is linearly independent by [[§41 Orthogonal Sets#^thm-41-1|Theorem §41.1]], so by the Basis Theorem it is a basis of $W_{k+1}$. This completes the induction; the process stops at $k + 1 = p$.

^pf-43-1

*Uses:* [[§42 Orthogonal Projections#^thm-42-1|§42.1]], [[§41 Orthogonal Sets#^thm-41-1|§41.1]], [[§27 The Dimension of a Vector Space#^thm-27-5|§27.5]] (the Basis Theorem)

> [!remark]- Connections
> - Rigorous treatment: [[§20 Orthonormal Bases#^ladr-6-32|LADR 6.32]] (Gram–Schmidt for a linearly independent list in any inner product space; Axler normalizes at every step, $e_k = f_k / \|f_k\|$, and proves the same span property (1)).
> - For a countable linearly independent sequence in a Hilbert space the process runs forever and produces an orthonormal sequence with the same spans: [[§24 Orthonormal Sets and Bases#^lem-24-14|556 Lem. §24.14]].

> [!theorem] Corollary §43.2: Existence of Orthogonal and Orthonormal Bases
> Every nonzero subspace $W$ of $\mathbb{R}^n$ has an orthogonal basis, and an orthonormal basis.
>
> *Lay: 6.4 (text)*

^cor-43-2

> [!proof]+ Proof
> $W$ has an ordinary basis $\{\mathbf{x}_1, \ldots, \mathbf{x}_p\}$, since a subspace of the finite-dimensional space $\mathbb{R}^n$ is finite-dimensional. Applying Theorem §43.1 to it gives an orthogonal basis $\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$. The process uses only orthogonal projections onto the subspaces $W_k$, which already have orthogonal bases at that stage, so it does not presuppose the corollary. Normalizing each $\mathbf{v}_k$ gives an orthonormal set ([[§41 Orthogonal Sets#^def-41-4|Definition §41.4]]) of $p$ vectors spanning $W$, an orthonormal basis.

^pf-43-2

*Uses:* [[§43 The Gram–Schmidt Process#^thm-43-1|§43.1]], [[§27 The Dimension of a Vector Space#^thm-27-3|§27.3]] (a subspace of a finite-dimensional space has a basis), [[§41 Orthogonal Sets#^def-41-4|Def. §41.4]]

> [!remark]- Connections
> - Rigorous treatment: [[§20 Orthonormal Bases#^ladr-6-35|LADR 6.35]] (every finite-dimensional inner product space has an orthonormal basis, by the same argument) and [[§20 Orthonormal Bases#^ladr-6-36|LADR 6.36]] (every orthonormal list extends to an orthonormal basis, the step used to complete $U$ in the proof of the SVD, [[§51★ The Singular Value Decomposition#^thm-51-4|Theorem §51.4]]).

> [!remark] Remark: Method — Gram–Schmidt by Hand
> Given a basis $\mathbf{x}_1, \ldots, \mathbf{x}_p$ of $W$:
> 1. Put $\mathbf{v}_1 = \mathbf{x}_1$.
> 2. For $k = 2, \ldots, p$: compute $\mathbf{v}_k = \mathbf{x}_k - \sum_{j < k} \frac{\mathbf{x}_k \cdot \mathbf{v}_j}{\mathbf{v}_j \cdot \mathbf{v}_j}\mathbf{v}_j$, that is, subtract from $\mathbf{x}_k$ its projection onto $\operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_{k-1}\}$, always using the *new* vectors $\mathbf{v}_j$ (not the $\mathbf{x}_j$) in the denominators.
> 3. Optionally scale each $\mathbf{v}_k$ to clear fractions before using it in later steps (Step 2′ of Example §43.2).
> 4. Check $\mathbf{v}_k \cdot \mathbf{v}_j = 0$ for $j < k$ as you go. A zero $\mathbf{v}_k$ means that $\mathbf{x}_k$ depended on the earlier vectors: the $\mathbf{x}$'s were not a basis.
> 5. For an orthonormal basis, normalize at the end: $\mathbf{u}_k = \mathbf{v}_k / \|\mathbf{v}_k\|$. Doing it last keeps square roots out of the intermediate steps.
>
> If some $\mathbf{x}_k$ is already orthogonal to the earlier $\mathbf{v}_j$, then $\mathbf{v}_k = \mathbf{x}_k$. For example, for $\mathbf{x}_1 = (1, 1, 1)$, $\mathbf{x}_2 = (\frac13, \frac13, -\frac23)$, $\mathbf{x}_2 \cdot \mathbf{x}_1 = 0$, so only normalization is needed: $\mathbf{u}_1 = (1, 1, 1)/\sqrt3$ and, scaling $\mathbf{x}_2$ to $(1, 1, -2)$ first, $\mathbf{u}_2 = (1, 1, -2)/\sqrt6$ (Lay's Practice Problem 1).

^rem-43-1

## QR Factorization of Matrices

> [!theorem] Theorem §43.3: The QR Factorization
> If $A$ is an $m \times n$ matrix with linearly independent columns, then $A$ can be factored as $A = QR$, where $Q$ is an $m \times n$ matrix whose columns form an orthonormal basis for $\operatorname{Col} A$ and $R$ is an $n \times n$ upper triangular invertible matrix with positive entries on its diagonal.
>
> *Lay: Theorem 12 (6.4)*

^thm-43-3

> [!proof]+ Proof
> The columns $\mathbf{x}_1, \ldots, \mathbf{x}_n$ of $A$ form a basis of $\operatorname{Col} A$. Construct an orthonormal basis $\{\mathbf{u}_1, \ldots, \mathbf{u}_n\}$ of $W = \operatorname{Col} A$ with property (1) of Theorem §43.1, for instance by Gram–Schmidt followed by normalization, and let
>
> $$
> Q = [\,\mathbf{u}_1\ \mathbf{u}_2\ \cdots\ \mathbf{u}_n\,] .
> $$
>
> For $k = 1, \ldots, n$, $\mathbf{x}_k \in \operatorname{Span}\{\mathbf{x}_1, \ldots, \mathbf{x}_k\} = \operatorname{Span}\{\mathbf{u}_1, \ldots, \mathbf{u}_k\}$, so there are constants $r_{1k}, \ldots, r_{kk}$ with
>
> $$
> \mathbf{x}_k = r_{1k}\mathbf{u}_1 + \cdots + r_{kk}\mathbf{u}_k + 0 \cdot \mathbf{u}_{k+1} + \cdots + 0 \cdot \mathbf{u}_n .
> $$
>
> We may assume $r_{kk} \ge 0$: if $r_{kk} < 0$, replace $\mathbf{u}_k$ by $-\mathbf{u}_k$ (the basis stays orthonormal with property (1)), which changes the signs of $r_{kk}$ and of the coefficients of $\mathbf{u}_k$ in the later $\mathbf{x}_j$. (With Gram–Schmidt, $r_{kk} = \|\mathbf{v}_k\| > 0$ automatically.) So $\mathbf{x}_k = Q\mathbf{r}_k$, where $\mathbf{r}_k = (r_{1k}, \ldots, r_{kk}, 0, \ldots, 0) \in \mathbb{R}^n$. Let $R = [\,\mathbf{r}_1\ \cdots\ \mathbf{r}_n\,]$. Then
>
> $$
> A = [\,\mathbf{x}_1\ \cdots\ \mathbf{x}_n\,] = [\,Q\mathbf{r}_1\ \cdots\ Q\mathbf{r}_n\,] = QR .
> $$
>
> $R$ is upper triangular, because the entries of $\mathbf{r}_k$ below position $k$ are $0$.
>
> **$R$ is invertible** (Lay's Exercise 19). If $R\mathbf{x} = \mathbf{0}$, then $A\mathbf{x} = QR\mathbf{x} = \mathbf{0}$; the columns of $A$ are linearly independent, so $\mathbf{x} = \mathbf{0}$. Thus $R\mathbf{x} = \mathbf{0}$ has only the trivial solution and the square matrix $R$ is invertible by the Invertible Matrix Theorem.
>
> **Positive diagonal.** The determinant of the triangular matrix $R$ is the product $r_{11}\cdots r_{nn}$ of its diagonal entries, and it is nonzero since $R$ is invertible. So no $r_{kk}$ is $0$, and the nonnegative $r_{kk}$ are positive.

^pf-43-3

*Uses:* [[§43 The Gram–Schmidt Process#^thm-43-1|§43.1]], [[§13 Characterizations of Invertible Matrices#^thm-13-1|§13.1]] (the Invertible Matrix Theorem), [[§20 Introduction to Determinants#^thm-20-2|§20.2]] (determinant of a triangular matrix), [[§21 Properties of Determinants#^thm-21-3|§21.3]] (invertible iff $\det \ne 0$)

> [!remark]- Connections
> - Rigorous treatment: [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-58|LADR 7.58]], for square $A$ (where $Q$ is unitary), with the same Gram–Schmidt construction and a proof that $Q$ and $R$ are *unique*.

> [!remark] Remark: Method — Computing a QR Factorization
> Let $A$ have linearly independent columns $\mathbf{x}_1, \ldots, \mathbf{x}_n$.
> 1. Apply Gram–Schmidt to $\mathbf{x}_1, \ldots, \mathbf{x}_n$ (scaling intermediate vectors if convenient) to get an orthogonal basis $\mathbf{v}_1, \ldots, \mathbf{v}_n$ of $\operatorname{Col} A$, in order.
> 2. Normalize: $\mathbf{u}_k = \mathbf{v}_k / \|\mathbf{v}_k\|$, and let $Q = [\,\mathbf{u}_1\ \cdots\ \mathbf{u}_n\,]$. Scaling $\mathbf{v}_k$ by a positive factor does not change $\mathbf{u}_k$; a negative factor would flip its sign and produce a negative diagonal entry in $R$.
> 3. Compute $R = Q^TA$. This works because $Q^TQ = I$ ([[§41 Orthogonal Sets#^thm-41-4|Theorem §41.4]]), so $Q^TA = Q^T(QR) = R$.
> 4. Check that $R$ is upper triangular with positive diagonal; a nonzero entry below the diagonal signals an arithmetic error.

^rem-43-2

> [!example] Example §43.3: A QR Factorization
> Find a QR factorization of
>
> $$
> A = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix} .
> $$
>
> **Orthogonal basis.** The columns of $A$ are $\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3$ of Example §43.2, which produced the orthogonal basis $\mathbf{v}_1 = (1, 1, 1, 1)$, $\mathbf{v}_2' = (-3, 1, 1, 1)$, $\mathbf{v}_3 = (0, -\frac23, \frac13, \frac13)$ of $\operatorname{Col} A$. Scale $\mathbf{v}_3$ to $\mathbf{v}_3' = 3\mathbf{v}_3 = (0, -2, 1, 1)$.
>
> **Q.** The lengths are $\|\mathbf{v}_1\| = 2$, $\|\mathbf{v}_2'\| = \sqrt{12}$, $\|\mathbf{v}_3'\| = \sqrt6$, so
>
> $$
> Q = \begin{bmatrix} 1/2 & -3/\sqrt{12} & 0 \\ 1/2 & 1/\sqrt{12} & -2/\sqrt6 \\ 1/2 & 1/\sqrt{12} & 1/\sqrt6 \\ 1/2 & 1/\sqrt{12} & 1/\sqrt6 \end{bmatrix} .
> $$
>
> By construction, the first $k$ columns of $Q$ are an orthonormal basis of $\operatorname{Span}\{\mathbf{x}_1, \ldots, \mathbf{x}_k\}$.
>
> **R.** Since $Q^TQ = I$, $R = Q^TA$:
>
> $$
> R = \begin{bmatrix} 1/2 & 1/2 & 1/2 & 1/2 \\ -3/\sqrt{12} & 1/\sqrt{12} & 1/\sqrt{12} & 1/\sqrt{12} \\ 0 & -2/\sqrt6 & 1/\sqrt6 & 1/\sqrt6 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 3/2 & 1 \\ 0 & 3/\sqrt{12} & 2/\sqrt{12} \\ 0 & 0 & 2/\sqrt6 \end{bmatrix} .
> $$
>
> For instance, entry $(1, 2)$ is $\frac12(0 + 1 + 1 + 1) = \frac32$, entry $(2, 1)$ is $(-3 + 1 + 1 + 1)/\sqrt{12} = 0$, and entry $(3, 2)$ is $(0 - 2 + 1 + 1)/\sqrt6 = 0$. As predicted, $R$ is upper triangular with positive diagonal.
>
> *Lay: Example 6.4.4*

^ex-43-3

> [!remark]- Remark: Numerical Notes
> 1. On a computer, roundoff error builds up as the $\mathbf{u}_k$ are computed one by one: for $j$ and $k$ large but unequal, $\mathbf{u}_j^T\mathbf{u}_k$ may not be close enough to $0$. Rearranging the order of the calculations ("modified Gram–Schmidt") reduces this loss of orthogonality substantially, but a different computer QR factorization is usually preferred because it yields a more accurate orthonormal basis, even though it needs about twice as much arithmetic.
> 2. That method left-multiplies $A$ by a sequence of orthogonal matrices until $A$ becomes upper triangular, in analogy with the left multiplication by elementary matrices that produces an LU factorization ([[§15 Matrix Factorizations#^def-15-1|Definition §15.1]]).

^rem-43-3
