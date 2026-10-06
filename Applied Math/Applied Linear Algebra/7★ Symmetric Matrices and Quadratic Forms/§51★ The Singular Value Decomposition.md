---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 7
section: 51
lay: "7.4"
aliases: ["Lay 7.4"]
tags: [applied-linear-algebra, math235, extension]
---
← [[§50★ Constrained Optimization]] · ↑ [[· 7★ Symmetric Matrices and Quadratic Forms]] · [[§51★ The Singular Value Decomposition in Applications]] →

*Lay, Section 7.4.*
★ *Beyond MATH 235: the course ended with inner products (Ch. 6); Chapter 7 is included from Lay as the continuation.*

Not every matrix can be diagonalized as $A = PDP^{-1}$, and a rectangular matrix has no eigenvalues at all. But *every* $m \times n$ matrix factors as $A = U\Sigma V^T$ with $U$ and $V$ orthogonal and $\Sigma$ "diagonal". This is the singular value decomposition, one of the most useful factorizations in applied linear algebra. It comes from applying the spectral theorem to the symmetric matrix $A^TA$: its orthonormal eigenvectors $\mathbf{v}_i$ are sent by $A$ to orthogonal vectors $A\mathbf{v}_i$ whose lengths, the singular values $\sigma_i$, measure how much $A$ stretches in each direction. Geometrically, $A$ maps the unit sphere onto an ellipsoid with semi-axes $\sigma_i \mathbf{u}_i$. The SVD reveals the rank of a matrix reliably, gives orthonormal bases for its four fundamental subspaces, measures the sensitivity of $A\mathbf{x} = \mathbf{b}$ (the condition number), and produces the pseudoinverse and minimum-length least-squares solutions.

## The Singular Values of an m × n Matrix

The SVD imitates the following property of diagonalization. If $A$ is symmetric, $A\mathbf{x} = \lambda\mathbf{x}$ and $\|\mathbf{x}\| = 1$, then $\|A\mathbf{x}\| = \|\lambda\mathbf{x}\| = |\lambda|\,\|\mathbf{x}\| = |\lambda|$: the absolute values of the eigenvalues measure how much $A$ stretches or shrinks its eigenvectors, and a unit eigenvector for the eigenvalue of greatest magnitude points in the direction of greatest stretching. For a rectangular $A$, the direction of greatest stretching is found from the quadratic form $\mathbf{x}^T(A^TA)\mathbf{x} = \|A\mathbf{x}\|^2$.

> [!example] Example §51.1: The Direction of Greatest Stretching
> Let $A = \begin{bmatrix} 4 & 11 & 14 \\ 8 & 7 & -2 \end{bmatrix}$. The linear transformation $\mathbf{x} \mapsto A\mathbf{x}$ maps the unit sphere $\{\mathbf{x} : \|\mathbf{x}\| = 1\}$ in $\mathbb{R}^3$ onto an ellipse in $\mathbb{R}^2$ (with its inside). Find a unit vector $\mathbf{x}$ at which $\|A\mathbf{x}\|$ is maximized, and the maximum length.
>
> **Reduce to a quadratic form.** $\|A\mathbf{x}\|^2$ is maximized at the same $\mathbf{x}$ as $\|A\mathbf{x}\|$, and it is easier to study:
>
> $$
> \|A\mathbf{x}\|^2 = (A\mathbf{x})^T(A\mathbf{x}) = \mathbf{x}^T A^T A \mathbf{x} = \mathbf{x}^T (A^TA) \mathbf{x} .
> $$
>
> $A^TA$ is symmetric, since $(A^TA)^T = A^T A^{TT} = A^TA$. So we must maximize the quadratic form $\mathbf{x}^T(A^TA)\mathbf{x}$ subject to $\|\mathbf{x}\| = 1$. By [[§50★ Constrained Optimization#^thm-50-1|Theorem §50.1]], the maximum is the greatest eigenvalue $\lambda_1$ of $A^TA$, attained at a corresponding unit eigenvector.
>
> **Eigenvalues of $A^TA$.**
>
> $$
> A^TA = \begin{bmatrix} 4 & 8 \\ 11 & 7 \\ 14 & -2 \end{bmatrix} \begin{bmatrix} 4 & 11 & 14 \\ 8 & 7 & -2 \end{bmatrix} = \begin{bmatrix} 80 & 100 & 40 \\ 100 & 170 & 140 \\ 40 & 140 & 200 \end{bmatrix},
> $$
>
> whose characteristic polynomial is $-\lambda(\lambda - 360)(\lambda - 90)$. The eigenvalues are $\lambda_1 = 360$, $\lambda_2 = 90$, $\lambda_3 = 0$. Row reducing $A^TA - \lambda I$ ($A^TA - 360I \sim \begin{bmatrix} 1 & 0 & -1/2 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{bmatrix}$, $A^TA - 90I \sim \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1/2 \\ 0 & 0 & 0 \end{bmatrix}$, $A^TA \sim \begin{bmatrix} 1 & 0 & -2 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{bmatrix}$) and normalizing gives the unit eigenvectors
>
> $$
> \mathbf{v}_1 = \begin{bmatrix} 1/3 \\ 2/3 \\ 2/3 \end{bmatrix}, \qquad \mathbf{v}_2 = \begin{bmatrix} -2/3 \\ -1/3 \\ 2/3 \end{bmatrix}, \qquad \mathbf{v}_3 = \begin{bmatrix} 2/3 \\ -2/3 \\ 1/3 \end{bmatrix}.
> $$
>
> **Answer.** The maximum of $\|A\mathbf{x}\|^2$ is $360$, attained at the unit vector $\mathbf{v}_1$. The point $A\mathbf{v}_1$ of the ellipse farthest from the origin is
>
> $$
> A\mathbf{v}_1 = \begin{bmatrix} 4 & 11 & 14 \\ 8 & 7 & -2 \end{bmatrix} \begin{bmatrix} 1/3 \\ 2/3 \\ 2/3 \end{bmatrix} = \begin{bmatrix} (4 + 22 + 28)/3 \\ (8 + 14 - 4)/3 \end{bmatrix} = \begin{bmatrix} 18 \\ 6 \end{bmatrix},
> $$
>
> and the maximum length is $\|A\mathbf{v}_1\| = \sqrt{324 + 36} = \sqrt{360} = 6\sqrt{10}$.
>
> **The minor axis.** By [[§51★ The Singular Value Decomposition#^prop-51-2|Proposition §51.2]] below, the maximum of $\|A\mathbf{x}\|$ over unit vectors orthogonal to $\mathbf{v}_1$ is attained at $\mathbf{v}_2$:
>
> $$
> A\mathbf{v}_2 = \begin{bmatrix} (-8 - 11 + 28)/3 \\ (-16 - 7 - 4)/3 \end{bmatrix} = \begin{bmatrix} 3 \\ -9 \end{bmatrix}, \qquad \|A\mathbf{v}_2\| = \sqrt{90} = 3\sqrt{10} .
> $$
>
> This point is on the minor axis of the ellipse, just as $A\mathbf{v}_1$ is on the major axis; and $A\mathbf{v}_3 = \mathbf{0}$. The singular values of $A$ ([[§51★ The Singular Value Decomposition#^def-51-1|Definition §51.1]]) are $\sigma_1 = \sqrt{360} = 6\sqrt{10}$, $\sigma_2 = \sqrt{90} = 3\sqrt{10}$, $\sigma_3 = 0$: the first two are the lengths of the semi-axes of the ellipse.
>
> *Lay: Examples 7.4.1 and 7.4.2*

^ex-51-1

![[m235-51-1.svg]]
*[[§51★ The Singular Value Decomposition#^ex-51-1|Example §51.1]]: the image of the unit sphere of $\mathbb{R}^3$ under $A$ is the region bounded by an ellipse in $\mathbb{R}^2$. Its semi-axes are $A\mathbf{v}_1 = (18, 6)$ and $A\mathbf{v}_2 = (3, -9)$, perpendicular ([[§51★ The Singular Value Decomposition#^thm-51-3|Theorem §51.3]]), of lengths $\sigma_1 = 6\sqrt{10}$ and $\sigma_2 = 3\sqrt{10}$. The direction $\mathbf{v}_3$ is collapsed to $\mathbf{0}$, so the sphere is flattened onto the plane, filling the inside of the ellipse.*

> [!theorem] Proposition §51.1: The Eigenvalues of AᵀA
> Let $A$ be an $m \times n$ matrix. Then $A^TA$ is symmetric and can be orthogonally diagonalized. If $\{\mathbf{v}_1, \dots, \mathbf{v}_n\}$ is an orthonormal basis for $\mathbb{R}^n$ consisting of eigenvectors of $A^TA$, with eigenvalues $\lambda_1, \dots, \lambda_n$, then
>
> $$
> \|A\mathbf{v}_i\|^2 = \lambda_i \qquad (1 \le i \le n) . \qquad (2)
> $$
>
> In particular, the eigenvalues of $A^TA$ are all nonnegative.
>
> *Lay: 7.4, Equation (2)*

^prop-51-1

> [!proof]+ Proof
> $(A^TA)^T = A^TA^{TT} = A^TA$, so $A^TA$ is symmetric and the Spectral Theorem ([[§48★ Diagonalization of Symmetric Matrices#^thm-48-3|Theorem §48.3]]) gives the orthonormal eigenvector basis. For each $i$,
>
> $$
> \begin{aligned}
> \|A\mathbf{v}_i\|^2 &= (A\mathbf{v}_i)^T A\mathbf{v}_i = \mathbf{v}_i^T A^TA \mathbf{v}_i \\
> &= \mathbf{v}_i^T (\lambda_i \mathbf{v}_i) && \text{since } \mathbf{v}_i \text{ is an eigenvector of } A^TA \\
> &= \lambda_i && \text{since } \mathbf{v}_i \text{ is a unit vector.}
> \end{aligned}
> $$
>
> A squared length is $\ge 0$, so $\lambda_i \ge 0$.

^pf-51-1

*Uses:* [[§48★ Diagonalization of Symmetric Matrices#^thm-48-3|§48.3]], [[§11 Matrix Operations#^thm-11-7|§11.7]] (transpose of a product)

By renumbering if necessary, we may assume the eigenvalues are arranged so that $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_n \ge 0$.

> [!definition] Definition §51.1: Singular Values
> The **singular values** of an $m \times n$ matrix $A$ are the square roots of the eigenvalues of $A^TA$, denoted by $\sigma_1, \dots, \sigma_n$ and arranged in decreasing order:
>
> $$
> \sigma_i = \sqrt{\lambda_i} \quad (1 \le i \le n), \qquad \sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_n \ge 0 .
> $$
>
> By (2), *the singular values of $A$ are the lengths of the vectors $A\mathbf{v}_1, \dots, A\mathbf{v}_n$*.
>
> *Lay: 7.4, Definition*

^def-51-1

> [!theorem] Proposition §51.2: Singular Values as Maximal Stretching
> Let $A$, $\mathbf{v}_1, \dots, \mathbf{v}_n$ and $\sigma_1 \ge \cdots \ge \sigma_n$ be as above. Then $\sigma_1$ is the maximum of $\|A\mathbf{x}\|$ over all unit vectors $\mathbf{x}$, attained at $\mathbf{x} = \mathbf{v}_1$; and for $k = 2, \dots, n$, $\sigma_k$ is the maximum of $\|A\mathbf{x}\|$ over all unit vectors $\mathbf{x}$ orthogonal to $\mathbf{v}_1, \dots, \mathbf{v}_{k-1}$, attained at $\mathbf{x} = \mathbf{v}_k$.
>
> *Lay: 7.4 (text, Examples 7.4.1–2; Exercise 21)*

^prop-51-2

> [!proof]+ Proof
> $\|A\mathbf{x}\|^2 = \mathbf{x}^T(A^TA)\mathbf{x}$ is a quadratic form with the symmetric matrix $A^TA$, whose eigenvalues are $\lambda_1 \ge \cdots \ge \lambda_n$ with orthonormal eigenvectors $\mathbf{v}_1, \dots, \mathbf{v}_n$. By [[§50★ Constrained Optimization#^thm-50-1|Theorem §50.1]], its maximum over unit vectors is $\lambda_1$, at $\mathbf{v}_1$; by [[§50★ Constrained Optimization#^thm-50-4|Theorem §50.4]], its maximum over unit vectors orthogonal to $\mathbf{v}_1, \dots, \mathbf{v}_{k-1}$ is $\lambda_k$, at $\mathbf{v}_k$. Since $t \mapsto \sqrt t$ is increasing on $[0, \infty)$, $\|A\mathbf{x}\|$ is maximized at the same vectors, with maximum values $\sqrt{\lambda_1} = \sigma_1$ and $\sqrt{\lambda_k} = \sigma_k$.

^pf-51-2

*Uses:* [[§50★ Constrained Optimization#^thm-50-1|§50.1]], [[§50★ Constrained Optimization#^thm-50-4|§50.4]], [[§51★ The Singular Value Decomposition#^prop-51-1|§51.1]]

> [!remark]- Connections
> - Rigorous treatment: [[§26 Singular Value Decomposition#^ladr-7-65|LADR 7.65]] defines the singular values of any linear map $T : V \to W$ between inner product spaces exactly this way, from the positive operator $T^*T$ ([[§26 Singular Value Decomposition#^ladr-7-64|LADR 7.64]]: $T^*T$ is positive, $\operatorname{null} T^*T = \operatorname{null} T$). The first part of [[§51★ The Singular Value Decomposition#^prop-51-2|Proposition §51.2]] is "the norm of $T$ is its largest singular value", [[§27 Consequences of Singular Value Decomposition#^ladr-7-88|LADR 7.88]].

The vectors $A\mathbf{v}_1$ and $A\mathbf{v}_2$ in [[§51★ The Singular Value Decomposition#^ex-51-1|Example §51.1]] are orthogonal. This is no accident.

> [!theorem] Theorem §51.3: An Orthogonal Basis for Col A
> Suppose $\{\mathbf{v}_1, \dots, \mathbf{v}_n\}$ is an orthonormal basis of $\mathbb{R}^n$ consisting of eigenvectors of $A^TA$, arranged so that the corresponding eigenvalues of $A^TA$ satisfy $\lambda_1 \ge \cdots \ge \lambda_n$, and suppose $A$ has $r$ nonzero singular values. Then $\{A\mathbf{v}_1, \dots, A\mathbf{v}_r\}$ is an orthogonal basis for $\operatorname{Col} A$, and $\operatorname{rank} A = r$.
>
> *Lay: Theorem 9 (7.4)*

^thm-51-3

> [!proof]+ Proof
> Because $\mathbf{v}_i$ and $\lambda_j\mathbf{v}_j$ are orthogonal for $i \ne j$,
>
> $$
> (A\mathbf{v}_i)^T(A\mathbf{v}_j) = \mathbf{v}_i^T A^TA \mathbf{v}_j = \mathbf{v}_i^T(\lambda_j\mathbf{v}_j) = 0 .
> $$
>
> Thus $\{A\mathbf{v}_1, \dots, A\mathbf{v}_n\}$ is an orthogonal set. Furthermore, the lengths of $A\mathbf{v}_1, \dots, A\mathbf{v}_n$ are the singular values of $A$, and since there are $r$ nonzero singular values (the first $r$, by the ordering), $A\mathbf{v}_i \ne \mathbf{0}$ if and only if $1 \le i \le r$. So $A\mathbf{v}_1, \dots, A\mathbf{v}_r$ are nonzero orthogonal vectors, hence linearly independent ([[§41 Orthogonal Sets#^thm-41-1|Theorem §41.1]]), and they lie in $\operatorname{Col} A$. Finally, for any $\mathbf{y}$ in $\operatorname{Col} A$, say $\mathbf{y} = A\mathbf{x}$, write $\mathbf{x} = c_1\mathbf{v}_1 + \cdots + c_n\mathbf{v}_n$; then
>
> $$
> \mathbf{y} = A\mathbf{x} = c_1A\mathbf{v}_1 + \cdots + c_rA\mathbf{v}_r + c_{r+1}A\mathbf{v}_{r+1} + \cdots + c_nA\mathbf{v}_n = c_1A\mathbf{v}_1 + \cdots + c_rA\mathbf{v}_r + \mathbf{0} + \cdots + \mathbf{0} .
> $$
>
> Thus $\mathbf{y}$ is in $\operatorname{Span}\{A\mathbf{v}_1, \dots, A\mathbf{v}_r\}$, which shows that $\{A\mathbf{v}_1, \dots, A\mathbf{v}_r\}$ is an (orthogonal) basis for $\operatorname{Col} A$. Hence $\operatorname{rank} A = \dim \operatorname{Col} A = r$.

^pf-51-3

*Uses:* [[§51★ The Singular Value Decomposition#^prop-51-1|§51.1]], [[§51★ The Singular Value Decomposition#^def-51-1|Def. §51.1]], [[§41 Orthogonal Sets#^thm-41-1|§41.1]], [[§28 Rank#^def-28-1|Def. §28.1]] (rank)

> [!remark]- Remark: Numerical Note — Effective Rank
> The rank of $A$ may be very sensitive to small changes in its entries. Counting pivot columns does not work well when a computer row reduces $A$: roundoff error often creates an echelon form with full rank. In practice, the most reliable way to estimate the rank of a large matrix is to count its nonzero singular values ([[§51★ The Singular Value Decomposition#^thm-51-3|Theorem §51.3]]), treating extremely small nonzero singular values as zero. The number that remains is the **effective rank** of the matrix.

^rem-51-1

## The Singular Value Decomposition

> [!theorem] Theorem §51.4: The Singular Value Decomposition
> Let $A$ be an $m \times n$ matrix with rank $r$. Then there exists an $m \times n$ matrix $\Sigma$ of the form
>
> $$
> \Sigma = \begin{bmatrix} D & 0 \\ 0 & 0 \end{bmatrix} \qquad (3)
> $$
>
> ($m - r$ rows and $n - r$ columns of zeros; if $r = m$ or $r = n$ or both, some or all of the zero blocks do not appear), for which the diagonal entries of the $r \times r$ diagonal matrix $D$ are the first $r$ singular values of $A$, $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r > 0$, and there exist an $m \times m$ orthogonal matrix $U$ and an $n \times n$ orthogonal matrix $V$ such that
>
> $$
> A = U\Sigma V^T .
> $$
>
> *Lay: Theorem 10 (7.4)*

^thm-51-4

> [!proof]+ Proof
> Let $\lambda_i$ and $\mathbf{v}_i$ be as in [[§51★ The Singular Value Decomposition#^thm-51-3|Theorem §51.3]], so that $\{A\mathbf{v}_1, \dots, A\mathbf{v}_r\}$ is an orthogonal basis for $\operatorname{Col} A$. Normalize each $A\mathbf{v}_i$ to obtain an orthonormal basis $\{\mathbf{u}_1, \dots, \mathbf{u}_r\}$, where
>
> $$
> \mathbf{u}_i = \frac{1}{\|A\mathbf{v}_i\|} A\mathbf{v}_i = \frac{1}{\sigma_i} A\mathbf{v}_i
> \qquad\text{and}\qquad
> A\mathbf{v}_i = \sigma_i \mathbf{u}_i \quad (1 \le i \le r) . \qquad (4)
> $$
>
> Now extend $\{\mathbf{u}_1, \dots, \mathbf{u}_r\}$ to an orthonormal basis $\{\mathbf{u}_1, \dots, \mathbf{u}_m\}$ of $\mathbb{R}^m$ (for instance with an orthonormal basis of $(\operatorname{Col} A)^\perp$, which exists by [[§43 The Gram–Schmidt Process#^cor-43-2|Corollary §43.2]] and has $m - r$ vectors by [[§40 Inner Product, Length, and Orthogonality#^prop-40-7|Proposition §40.7]]; the $m$ orthonormal vectors together are linearly independent, hence a basis of $\mathbb{R}^m$), and let
>
> $$
> U = [\,\mathbf{u}_1\ \ \mathbf{u}_2\ \cdots\ \mathbf{u}_m\,] \qquad\text{and}\qquad V = [\,\mathbf{v}_1\ \ \mathbf{v}_2\ \cdots\ \mathbf{v}_n\,] .
> $$
>
> By construction, $U$ and $V$ are orthogonal matrices. Also, from (4) and $A\mathbf{v}_i = \mathbf{0}$ for $i > r$,
>
> $$
> AV = [\,A\mathbf{v}_1\ \cdots\ A\mathbf{v}_r\ \ \mathbf{0}\ \cdots\ \mathbf{0}\,] = [\,\sigma_1\mathbf{u}_1\ \cdots\ \sigma_r\mathbf{u}_r\ \ \mathbf{0}\ \cdots\ \mathbf{0}\,] .
> $$
>
> Let $D$ be the diagonal matrix with diagonal entries $\sigma_1, \dots, \sigma_r$, and let $\Sigma$ be as in (3). Column $j$ of $U\Sigma$ is $U$ times column $j$ of $\Sigma$, which is $\sigma_j\mathbf{e}_j$ for $j \le r$ and $\mathbf{0}$ for $j > r$. So
>
> $$
> U\Sigma = [\,\sigma_1\mathbf{u}_1\ \cdots\ \sigma_r\mathbf{u}_r\ \ \mathbf{0}\ \cdots\ \mathbf{0}\,] = AV .
> $$
>
> Since $V$ is an orthogonal matrix, $VV^T = I$, and $U\Sigma V^T = AVV^T = A$.

^pf-51-4

*Uses:* [[§51★ The Singular Value Decomposition#^thm-51-3|§51.3]], [[§41 Orthogonal Sets#^thm-41-4|§41.4]], [[§41 Orthogonal Sets#^def-41-5|Def. §41.5]] (orthogonal matrices), [[§43 The Gram–Schmidt Process#^cor-43-2|§43.2]], [[§40 Inner Product, Length, and Orthogonality#^prop-40-7|§40.7]], [[§41 Orthogonal Sets#^thm-41-1|§41.1]] (the extended orthonormal set is independent)

> [!definition] Definition §51.2: Singular Value Decomposition; Singular Vectors
> Any factorization $A = U\Sigma V^T$, with $U$ and $V$ orthogonal, $\Sigma$ as in (3), and positive diagonal entries in $D$, is called a **singular value decomposition** (or **SVD**) of $A$. The columns of $U$ are called **left singular vectors** of $A$, and the columns of $V$ are called **right singular vectors** of $A$.
>
> The matrices $U$ and $V$ are not uniquely determined by $A$, but the diagonal entries of $\Sigma$ are necessarily the singular values of $A$: from $A = U\Sigma V^T$ one gets $A^TA = V(\Sigma^T\Sigma)V^T$, an orthogonal diagonalization of $A^TA$ whose diagonal entries are the $\sigma_i^2$ (Exercise 19).
>
> *Lay: 7.4, Definition and text*

^def-51-2

> [!remark]- Connections
> - Rigorous treatment: [[§26 Singular Value Decomposition#^ladr-7-70|LADR 7.70]] (hub [[Singular value decomposition]]) proves the same construction for a linear map $T : V \to W$, written as $Tv = \sum_k s_k \langle v, e_k \rangle f_k$ (that is, $A = \sum_{i \le r} \sigma_i \mathbf{u}_i \mathbf{v}_i^T$, Lay's Exercise 23); the matrix form, in the reduced shape of [[§51★ The Singular Value Decomposition#^def-51-4|Definition §51.4]], is [[§26 Singular Value Decomposition#^ladr-7-80|LADR 7.80]]. Axler's proof is Lay's: diagonalize $T^*T$, set $f_k = Te_k/s_k$.
> - Polar decomposition (Lay's Supplementary Exercise 11): $A = (U\Sigma U^T)(UV^T)$ writes a square $A$ as a positive semidefinite matrix times an orthogonal matrix, a stretch along perpendicular axes followed by a rotation or reflection: [[§27 Consequences of Singular Value Decomposition#^ladr-7-93|LADR 7.93]].

> [!remark] Remark: Method — Computing an SVD
> To construct an SVD $A = U\Sigma V^T$ of an $m \times n$ matrix $A$ by hand:
> 1. **Find an orthogonal diagonalization of $A^TA$:** its eigenvalues and a corresponding orthonormal set of eigenvectors. (If $A$ has fewer rows than columns, it may be easier to start from $AA^T$ and work with $A^T$, using that $A^T = V\Sigma^TU^T$ is an SVD of $A^T$.)
> 2. **Set up $V$ and $\Sigma$.** Arrange the eigenvalues of $A^TA$ in decreasing order; the corresponding unit eigenvectors $\mathbf{v}_1, \dots, \mathbf{v}_n$, in this order, are the columns of $V$. The singular values are $\sigma_i = \sqrt{\lambda_i}$; the nonzero ones, $\sigma_1, \dots, \sigma_r$, go on the diagonal of $D$, and $\Sigma$ is $D$ padded with zeros to the size $m \times n$ of $A$.
> 3. **Construct $U$.** Its first $r$ columns are $\mathbf{u}_i = \frac{1}{\sigma_i} A\mathbf{v}_i$, $i = 1, \dots, r$ (check: $\|A\mathbf{v}_i\| = \sigma_i$). If $r < m$, extend $\{\mathbf{u}_1, \dots, \mathbf{u}_r\}$ to an orthonormal basis of $\mathbb{R}^m$: find a basis of the solutions of $\mathbf{u}_1^T\mathbf{x} = \cdots = \mathbf{u}_r^T\mathbf{x} = 0$ (that is, of $\operatorname{Nul} A^T$) and apply Gram–Schmidt with normalization.
>
> Writing $A = U\Sigma V^T$ needs $V^T$, not $V$.

^rem-51-2

> [!example] Example §51.2: An SVD of a 2 × 3 Matrix
> Use [[§51★ The Singular Value Decomposition#^ex-51-1|Example §51.1]] to construct a singular value decomposition of $A = \begin{bmatrix} 4 & 11 & 14 \\ 8 & 7 & -2 \end{bmatrix}$.
>
> **Step 1.** [[§51★ The Singular Value Decomposition#^ex-51-1|Example §51.1]] orthogonally diagonalized $A^TA$: eigenvalues $360, 90, 0$ with unit eigenvectors $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$.
>
> **Step 2.** The eigenvalues are already in decreasing order, so
>
> $$
> V = [\,\mathbf{v}_1\ \ \mathbf{v}_2\ \ \mathbf{v}_3\,] = \begin{bmatrix} 1/3 & -2/3 & 2/3 \\ 2/3 & -1/3 & -2/3 \\ 2/3 & 2/3 & 1/3 \end{bmatrix}.
> $$
>
> The singular values are $\sigma_1 = 6\sqrt{10}$, $\sigma_2 = 3\sqrt{10}$, $\sigma_3 = 0$. The nonzero ones form $D$, and $\Sigma$ has the size $2 \times 3$ of $A$:
>
> $$
> D = \begin{bmatrix} 6\sqrt{10} & 0 \\ 0 & 3\sqrt{10} \end{bmatrix}, \qquad \Sigma = [\,D\ \ \mathbf{0}\,] = \begin{bmatrix} 6\sqrt{10} & 0 & 0 \\ 0 & 3\sqrt{10} & 0 \end{bmatrix}.
> $$
>
> **Step 3.** $A$ has two nonzero singular values, so $\operatorname{rank} A = 2$, and
>
> $$
> \mathbf{u}_1 = \frac{1}{\sigma_1} A\mathbf{v}_1 = \frac{1}{6\sqrt{10}} \begin{bmatrix} 18 \\ 6 \end{bmatrix} = \begin{bmatrix} 3/\sqrt{10} \\ 1/\sqrt{10} \end{bmatrix}, \qquad
> \mathbf{u}_2 = \frac{1}{\sigma_2} A\mathbf{v}_2 = \frac{1}{3\sqrt{10}} \begin{bmatrix} 3 \\ -9 \end{bmatrix} = \begin{bmatrix} 1/\sqrt{10} \\ -3/\sqrt{10} \end{bmatrix}.
> $$
>
> $\{\mathbf{u}_1, \mathbf{u}_2\}$ is already a basis of $\mathbb{R}^2$, so no more columns are needed and $U = [\,\mathbf{u}_1\ \ \mathbf{u}_2\,]$. The SVD is
>
> $$
> A = \underbrace{\begin{bmatrix} 3/\sqrt{10} & 1/\sqrt{10} \\ 1/\sqrt{10} & -3/\sqrt{10} \end{bmatrix}}_{U}
> \underbrace{\begin{bmatrix} 6\sqrt{10} & 0 & 0 \\ 0 & 3\sqrt{10} & 0 \end{bmatrix}}_{\Sigma}
> \underbrace{\begin{bmatrix} 1/3 & 2/3 & 2/3 \\ -2/3 & -1/3 & 2/3 \\ 2/3 & -2/3 & 1/3 \end{bmatrix}}_{V^T}.
> $$
>
> (Check of the first entry: $\frac{3}{\sqrt{10}} \cdot 6\sqrt{10} \cdot \frac13 + \frac{1}{\sqrt{10}} \cdot 3\sqrt{10} \cdot (-\frac23) = 6 - 2 = 4$.)
>
> *Lay: Example 7.4.3*

^ex-51-2

> [!example] Example §51.3: An SVD of a Rank-One 3 × 2 Matrix
> Find a singular value decomposition of $A = \begin{bmatrix} 1 & -1 \\ -2 & 2 \\ 2 & -2 \end{bmatrix}$.
>
> **Step 1.** $A^TA = \begin{bmatrix} 9 & -9 \\ -9 & 9 \end{bmatrix}$, with characteristic polynomial $(9 - \lambda)^2 - 81 = \lambda(\lambda - 18)$. The eigenvalues are $18$ and $0$, with unit eigenvectors
>
> $$
> \mathbf{v}_1 = \begin{bmatrix} 1/\sqrt2 \\ -1/\sqrt2 \end{bmatrix}, \qquad \mathbf{v}_2 = \begin{bmatrix} 1/\sqrt2 \\ 1/\sqrt2 \end{bmatrix}.
> $$
>
> **Step 2.** $V = [\,\mathbf{v}_1\ \ \mathbf{v}_2\,] = \begin{bmatrix} 1/\sqrt2 & 1/\sqrt2 \\ -1/\sqrt2 & 1/\sqrt2 \end{bmatrix}$. The singular values are $\sigma_1 = \sqrt{18} = 3\sqrt2$ and $\sigma_2 = 0$. With only one nonzero singular value, $D$ is the single number $3\sqrt2$, and $\Sigma$ has the size $3 \times 2$ of $A$:
>
> $$
> \Sigma = \begin{bmatrix} D & 0 \\ 0 & 0 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 3\sqrt2 & 0 \\ 0 & 0 \\ 0 & 0 \end{bmatrix}.
> $$
>
> **Step 3.** Compute
>
> $$
> A\mathbf{v}_1 = \begin{bmatrix} 2/\sqrt2 \\ -4/\sqrt2 \\ 4/\sqrt2 \end{bmatrix}, \qquad A\mathbf{v}_2 = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}.
> $$
>
> As a check, $\|A\mathbf{v}_1\| = \sqrt{(4 + 16 + 16)/2} = \sqrt{18} = \sigma_1$, and $A\mathbf{v}_2 = \mathbf{0}$ because $\|A\mathbf{v}_2\| = \sigma_2 = 0$. The only column of $U$ found so far is
>
> $$
> \mathbf{u}_1 = \frac{1}{3\sqrt2} A\mathbf{v}_1 = \begin{bmatrix} 1/3 \\ -2/3 \\ 2/3 \end{bmatrix}.
> $$
>
> The other columns of $U$ come from extending $\{\mathbf{u}_1\}$ to an orthonormal basis of $\mathbb{R}^3$: we need two orthogonal unit vectors $\mathbf{u}_2, \mathbf{u}_3$ orthogonal to $\mathbf{u}_1$. Each must satisfy $\mathbf{u}_1^T\mathbf{x} = 0$, which is equivalent to $x_1 - 2x_2 + 2x_3 = 0$. A basis for its solution set ($x_1 = 2x_2 - 2x_3$, $x_2, x_3$ free) is
>
> $$
> \mathbf{w}_1 = \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}, \qquad \mathbf{w}_2 = \begin{bmatrix} -2 \\ 0 \\ 1 \end{bmatrix}.
> $$
>
> Gram–Schmidt: $\mathbf{w}_2 - \frac{\mathbf{w}_2 \cdot \mathbf{w}_1}{\mathbf{w}_1 \cdot \mathbf{w}_1}\mathbf{w}_1 = \mathbf{w}_2 + \frac45\mathbf{w}_1 = (-\frac25, \frac45, 1) = \frac15(-2, 4, 5)$, and $\|(-2, 4, 5)\| = \sqrt{45}$. Normalizing,
>
> $$
> \mathbf{u}_2 = \begin{bmatrix} 2/\sqrt5 \\ 1/\sqrt5 \\ 0 \end{bmatrix}, \qquad \mathbf{u}_3 = \begin{bmatrix} -2/\sqrt{45} \\ 4/\sqrt{45} \\ 5/\sqrt{45} \end{bmatrix}.
> $$
>
> Finally, with $U = [\,\mathbf{u}_1\ \ \mathbf{u}_2\ \ \mathbf{u}_3\,]$,
>
> $$
> A = \begin{bmatrix} 1 & -1 \\ -2 & 2 \\ 2 & -2 \end{bmatrix} = \begin{bmatrix} 1/3 & 2/\sqrt5 & -2/\sqrt{45} \\ -2/3 & 1/\sqrt5 & 4/\sqrt{45} \\ 2/3 & 0 & 5/\sqrt{45} \end{bmatrix} \begin{bmatrix} 3\sqrt2 & 0 \\ 0 & 0 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} 1/\sqrt2 & -1/\sqrt2 \\ 1/\sqrt2 & 1/\sqrt2 \end{bmatrix}.
> $$
>
> Geometrically: $A$ collapses the line through $\mathbf{v}_2$ (which is $\operatorname{Nul} A$) and sends the unit circle onto the segment from $-3\sqrt2\,\mathbf{u}_1$ to $3\sqrt2\,\mathbf{u}_1$ on the line $\operatorname{Col} A$; $\mathbf{u}_2, \mathbf{u}_3$ span the plane $\operatorname{Nul} A^T = (\operatorname{Col} A)^\perp$.
>
> *Lay: Example 7.4.4*

^ex-51-3

*Continued in [[§51★ The Singular Value Decomposition in Applications]]: the condition number, bases for the four fundamental subspaces, the reduced SVD and the pseudoinverse.*
