---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 7
section: "51a"
lay: "7.4"
aliases: ["Lay 7.4 (cont.)"]
tags: [applied-linear-algebra, math235, extension]
---
← [[§51★ The Singular Value Decomposition]] · ↑ [[· 7★ Symmetric Matrices and Quadratic Forms]] · [[§52★ Applications to Image Processing and Statistics]] →

*Lay, Section 7.4.*
★ *Beyond MATH 235: the course ended with inner products (Ch. 6); Chapter 7 is included from Lay as the continuation.*

The SVD reveals the rank of a matrix reliably, gives orthonormal bases for its four fundamental subspaces, measures the sensitivity of $A\mathbf{x} = \mathbf{b}$ (the condition number), and produces the pseudoinverse and minimum-length least-squares solutions.

## Applications of the Singular Value Decomposition

The two orthogonal matrices $U$ and $V$ do not affect lengths of vectors or angles between vectors ([[§41 Orthogonal Sets#^thm-41-5|Theorem §41.5]]). So any possible instability in a calculation with $A$ is identified in $\Sigma$: if the singular values of $A$ are extremely large or small, roundoff errors are almost inevitable, and an error analysis is aided by knowing $\Sigma$ and $V$.

> [!definition] Definition §51.3: Condition Number
> If $A$ is an invertible $n \times n$ matrix, the ratio $\sigma_1/\sigma_n$ of its largest and smallest singular values is the **condition number** of $A$. It measures how sensitive the solution of $A\mathbf{x} = \mathbf{b}$ is to changes (or errors) in the entries of $A$ (Lay's Exercises 41–43 of Section 2.3; see the remark on ill-conditioned matrices, [[§13 Characterizations of Invertible Matrices#^rem-13-3|§13]]). A "condition number" can be defined in several ways, but this one is widely used for studying $A\mathbf{x} = \mathbf{b}$.
>
> *Lay: Example 7.4.5*

^def-51-3

> [!theorem] Theorem §51.5: Orthonormal Bases for the Four Fundamental Subspaces
> Given an SVD $A = U\Sigma V^T$ of an $m \times n$ matrix $A$ of rank $r$, let $\mathbf{u}_1, \dots, \mathbf{u}_m$ be the left singular vectors, $\mathbf{v}_1, \dots, \mathbf{v}_n$ the right singular vectors and $\sigma_1, \dots, \sigma_n$ the singular values. Then
>
> $$
> \begin{aligned}
> &\{\mathbf{u}_1, \dots, \mathbf{u}_r\} \text{ is an orthonormal basis for } \operatorname{Col} A, && (5) \\
> &\{\mathbf{u}_{r+1}, \dots, \mathbf{u}_m\} \text{ is an orthonormal basis for } \operatorname{Nul} A^T, && (6) \\
> &\{\mathbf{v}_{r+1}, \dots, \mathbf{v}_n\} \text{ is an orthonormal basis for } \operatorname{Nul} A, && (7) \\
> &\{\mathbf{v}_1, \dots, \mathbf{v}_r\} \text{ is an orthonormal basis for } \operatorname{Row} A, && (8)
> \end{aligned}
> $$
>
> and $A\mathbf{v}_i = \sigma_i\mathbf{u}_i$ for $1 \le i \le r$, $A\mathbf{v}_i = \mathbf{0}$ for $i > r$. In words: $A$ maps the orthonormal basis $\mathbf{v}_1, \dots, \mathbf{v}_r$ of $\operatorname{Row} A$ onto the orthogonal basis $\sigma_1\mathbf{u}_1, \dots, \sigma_r\mathbf{u}_r$ of $\operatorname{Col} A$, and kills $\operatorname{Nul} A$.
>
> *Lay: Example 7.4.6*

^thm-51-5

> [!proof]+ Proof
> Comparing columns in $AV = U\Sigma$ gives $A\mathbf{v}_i = \sigma_i\mathbf{u}_i$ for $i \le r$ and $A\mathbf{v}_i = \mathbf{0}$ for $i > r$. (Lay takes the SVD from the construction in [[§51★ The Singular Value Decomposition#^thm-51-4|Theorem §51.4]]; this column comparison makes the argument work for any SVD.)
>
> **(5)** The vectors $A\mathbf{v}_1, \dots, A\mathbf{v}_r$ are nonzero and orthogonal, hence a basis of $\operatorname{Col} A$ by [[§51★ The Singular Value Decomposition#^thm-51-3|Theorem §51.3]] (its proof applies verbatim, since by [[§51★ The Singular Value Decomposition#^def-51-2|Definition §51.2]] the $\mathbf{v}_i$ are orthonormal eigenvectors of $A^TA$ for the eigenvalues $\sigma_i^2$); so their normalizations $\mathbf{u}_1, \dots, \mathbf{u}_r$ are an orthonormal basis.
>
> **(6)** Recall that $(\operatorname{Col} A)^\perp = \operatorname{Nul} A^T$ ([[§40 Inner Product, Length, and Orthogonality#^thm-40-6|Theorem §40.6]]). The vectors $\mathbf{u}_{r+1}, \dots, \mathbf{u}_m$ are orthonormal and orthogonal to $\mathbf{u}_1, \dots, \mathbf{u}_r$, hence to $\operatorname{Col} A$, so they lie in $\operatorname{Nul} A^T$. There are $m - r$ of them, and $\dim (\operatorname{Col} A)^\perp = m - r$ ([[§40 Inner Product, Length, and Orthogonality#^prop-40-7|Proposition §40.7]]), so by the Basis Theorem ([[§27 The Dimension of a Vector Space#^thm-27-5|Theorem §27.5]]) they form a basis.
>
> **(7)** Since $\|A\mathbf{v}_i\| = \sigma_i$ for $1 \le i \le n$, and $\sigma_i = 0$ if and only if $i > r$, the vectors $\mathbf{v}_{r+1}, \dots, \mathbf{v}_n$ lie in $\operatorname{Nul} A$, and they span a subspace of dimension $n - r$. By the Rank Theorem ([[§28 Rank#^thm-28-3|Theorem §28.3]]), $\dim \operatorname{Nul} A = n - \operatorname{rank} A = n - r$. So by the Basis Theorem, $\{\mathbf{v}_{r+1}, \dots, \mathbf{v}_n\}$ is an orthonormal basis for $\operatorname{Nul} A$.
>
> **(8)** From (5) and (6), the orthogonal complement of $\operatorname{Nul} A^T$ is $\operatorname{Col} A$. Interchanging $A$ and $A^T$: $(\operatorname{Nul} A)^\perp = \operatorname{Col} A^T = \operatorname{Row} A$. The vectors $\mathbf{v}_1, \dots, \mathbf{v}_r$ are orthogonal to $\mathbf{v}_{r+1}, \dots, \mathbf{v}_n$, hence by (7) to $\operatorname{Nul} A$, so they lie in $\operatorname{Row} A$; they are $r = \dim \operatorname{Row} A$ orthonormal vectors, so they are a basis.

^pf-51-5

*Uses:* [[§51★ The Singular Value Decomposition#^thm-51-3|§51.3]], [[§51★ The Singular Value Decomposition#^def-51-2|Def. §51.2]], [[§40 Inner Product, Length, and Orthogonality#^thm-40-6|§40.6]], [[§27 The Dimension of a Vector Space#^thm-27-5|§27.5]] (Basis Theorem), [[§28 Rank#^thm-28-3|§28.3]] (Rank Theorem), [[§40 Inner Product, Length, and Orthogonality#^prop-40-7|§40.7]] (dimension of $W^\perp$)

Explicit orthonormal bases for the four fundamental subspaces are useful in some calculations, particularly in constrained optimization problems. In [[§51★ The Singular Value Decomposition#^ex-51-3|Example §51.3]]: $\operatorname{Col} A$ is the line spanned by $\mathbf{u}_1$, $\operatorname{Nul} A^T$ the plane spanned by $\mathbf{u}_2, \mathbf{u}_3$, $\operatorname{Row} A$ the line spanned by $\mathbf{v}_1$, and $\operatorname{Nul} A$ the line spanned by $\mathbf{v}_2$.

The four fundamental subspaces and the singular values provide the final statements of the Invertible Matrix Theorem. (Statements about $A^T$ were omitted from earlier versions to avoid nearly doubling their length.)

> [!theorem] Theorem §51.6: The Invertible Matrix Theorem (Concluded)
> Let $A$ be an $n \times n$ matrix. Then the following statements are each equivalent to the statement that $A$ is an invertible matrix (and so to statements (a)–(t) of the earlier versions: (a)–(l) of [[§13 Characterizations of Invertible Matrices#^thm-13-1|Theorem §13.1]], (m)–(r) of [[§19 Dimension and Rank#^thm-19-3|Theorem §19.3]], and (s), (t) of the previous version, [[§33 The Characteristic Equation#^thm-33-2|Theorem §33.2]]):
> - (u) $(\operatorname{Col} A)^\perp = \{\mathbf{0}\}$.
> - (v) $(\operatorname{Nul} A)^\perp = \mathbb{R}^n$.
> - (w) $\operatorname{Row} A = \mathbb{R}^n$.
> - (x) $A$ has $n$ nonzero singular values.
>
> *Lay: 7.4, The Invertible Matrix Theorem (concluded)*

^thm-51-6

> [!proof]+ Proof
> (Lay states these without proof; each follows from earlier statements.)
>
> **(u)** By [[§40 Inner Product, Length, and Orthogonality#^thm-40-6|Theorem §40.6]], $(\operatorname{Col} A)^\perp = \operatorname{Nul} A^T$. So (u) says $A^T\mathbf{x} = \mathbf{0}$ has only the trivial solution, which by statement (d) of [[§13 Characterizations of Invertible Matrices#^thm-13-1|Theorem §13.1]] (applied to $A^T$) means $A^T$ is invertible, which is equivalent to $A$ invertible (statement (l)).
>
> **(v)** If $\operatorname{Nul} A = \{\mathbf{0}\}$, then $(\operatorname{Nul} A)^\perp = \{\mathbf{0}\}^\perp = \mathbb{R}^n$. Conversely, if $\operatorname{Nul} A$ contains some $\mathbf{x} \ne \mathbf{0}$, then $\mathbf{x} \cdot \mathbf{x} \ne 0$, so $\mathbf{x} \notin (\operatorname{Nul} A)^\perp$ and $(\operatorname{Nul} A)^\perp \ne \mathbb{R}^n$. So (v) is equivalent to $\operatorname{Nul} A = \{\mathbf{0}\}$, statement (q) of [[§19 Dimension and Rank#^thm-19-3|Theorem §19.3]].
>
> **(w)** $\operatorname{Row} A = \operatorname{Col} A^T$, so (w) says the columns of $A^T$ span $\mathbb{R}^n$, that is (statement (h) for $A^T$), $A^T$ is invertible, that is, $A$ is invertible. (Equivalently: $\dim \operatorname{Row} A = \operatorname{rank} A$, and $\operatorname{rank} A = n$ is statement (p) of [[§19 Dimension and Rank#^thm-19-3|Theorem §19.3]].)
>
> **(x)** By [[§51★ The Singular Value Decomposition#^thm-51-3|Theorem §51.3]], the number of nonzero singular values of $A$ is $\operatorname{rank} A$, and $\operatorname{rank} A = n$ is statement (p) of [[§19 Dimension and Rank#^thm-19-3|Theorem §19.3]].

^pf-51-6

*Uses:* [[§51★ The Singular Value Decomposition#^thm-51-3|§51.3]], [[§40 Inner Product, Length, and Orthogonality#^thm-40-6|§40.6]], [[§13 Characterizations of Invertible Matrices#^thm-13-1|§13.1]], [[§19 Dimension and Rank#^thm-19-3|§19.3]], [[§33 The Characteristic Equation#^thm-33-2|§33.2]]

> [!theorem] Proposition §51.7: The Reduced SVD
> Let $A = U\Sigma V^T$ be an SVD of an $m \times n$ matrix of rank $r$, with $D$ as in (3). Partition $U$ and $V$ into submatrices whose first blocks contain $r$ columns:
>
> $$
> U = [\,U_r\ \ U_{m-r}\,], \quad U_r = [\,\mathbf{u}_1\ \cdots\ \mathbf{u}_r\,]; \qquad V = [\,V_r\ \ V_{n-r}\,], \quad V_r = [\,\mathbf{v}_1\ \cdots\ \mathbf{v}_r\,] .
> $$
>
> Then $U_r$ is $m \times r$, $V_r$ is $n \times r$, and
>
> $$
> A = U_r D V_r^T . \qquad (9)
> $$
>
> *Lay: Example 7.4.7, Equation (9)*

^prop-51-7

> [!proof]+ Proof
> By partitioned matrix multiplication ([[§14 Partitioned Matrices#^prop-14-2|Proposition §14.2]]; to simplify notation, $U_{m-r}$ or $V_{n-r}$ is allowed to have no columns),
>
> $$
> A = [\,U_r\ \ U_{m-r}\,] \begin{bmatrix} D & 0 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} V_r^T \\ V_{n-r}^T \end{bmatrix} = [\,U_rD\ \ \ 0\,] \begin{bmatrix} V_r^T \\ V_{n-r}^T \end{bmatrix} = U_r D V_r^T .
> $$

^pf-51-7

*Uses:* [[§51★ The Singular Value Decomposition#^thm-51-4|§51.4]], [[§14 Partitioned Matrices#^prop-14-2|§14.2]] (block multiplication)

> [!definition] Definition §51.4: Reduced SVD
> The factorization (9), $A = U_rDV_r^T$, is called a **reduced singular value decomposition** of $A$.
>
> *Lay: Example 7.4.7, Equation (10)*

^def-51-4

> [!definition] Definition §51.4: Pseudoinverse
> Since the diagonal entries of $D$ are nonzero, $D$ is invertible, and the matrix
>
> $$
> A^+ = V_r D^{-1} U_r^T \qquad (10)
> $$
>
> is called the **pseudoinverse** (also the **Moore–Penrose inverse**) of $A$. It is $n \times m$, the shape of $A^T$.
>
> *Lay: Example 7.4.7, Equation (10)*

^def-51-new1

> [!theorem] Theorem §51.8: Least-Squares Solution by the Pseudoinverse
> Given the equation $A\mathbf{x} = \mathbf{b}$, let
>
> $$
> \hat{\mathbf{x}} = A^+\mathbf{b} = V_rD^{-1}U_r^T\mathbf{b} .
> $$
>
> Then $A\hat{\mathbf{x}} = U_rU_r^T\mathbf{b}$ is the orthogonal projection $\hat{\mathbf{b}}$ of $\mathbf{b}$ onto $\operatorname{Col} A$, so $\hat{\mathbf{x}}$ is a least-squares solution of $A\mathbf{x} = \mathbf{b}$. In fact, $\hat{\mathbf{x}}$ has the smallest length among all least-squares solutions.
>
> *Lay: Example 7.4.8*

^thm-51-8

> [!proof]+ Proof
> From the reduced SVD (9), and because $V_r^TV_r = I_r$ (the columns of $V_r$ are orthonormal),
>
> $$
> A\hat{\mathbf{x}} = (U_rDV_r^T)(V_rD^{-1}U_r^T\mathbf{b}) = U_rDD^{-1}U_r^T\mathbf{b} = U_rU_r^T\mathbf{b} .
> $$
>
> By (5), the columns of $U_r$ are an orthonormal basis of $\operatorname{Col} A$, so $U_rU_r^T\mathbf{b}$ is the orthogonal projection $\hat{\mathbf{b}}$ of $\mathbf{b}$ onto $\operatorname{Col} A$ ([[§42 Orthogonal Projections#^thm-42-4|Theorem §42.4]]). By the Best Approximation Theorem ([[§42 Orthogonal Projections#^thm-42-3|Theorem §42.3]]), $\hat{\mathbf{b}}$ is the unique point of $\operatorname{Col} A$ closest to $\mathbf{b}$, so a vector $\hat{\mathbf{x}}$ with $A\hat{\mathbf{x}} = \hat{\mathbf{b}}$ is a least-squares solution ([[§44 Least-Squares Problems#^def-44-1|Definition §44.1]]).
>
> *Minimal length.* (Lay leaves this to Supplementary Exercise 14; here is why.) Every least-squares solution satisfies $A\mathbf{x} = \hat{\mathbf{b}}$, so it differs from $\hat{\mathbf{x}}$ by a vector $\mathbf{z}$ of $\operatorname{Nul} A$. Now $\hat{\mathbf{x}} = V_r(D^{-1}U_r^T\mathbf{b})$ is a combination of $\mathbf{v}_1, \dots, \mathbf{v}_r$, so it is orthogonal to $\mathbf{v}_{r+1}, \dots, \mathbf{v}_n$, which span $\operatorname{Nul} A$ by (7); hence $\hat{\mathbf{x}} \cdot \mathbf{z} = 0$. By the Pythagorean Theorem ([[§40 Inner Product, Length, and Orthogonality#^thm-40-4|Theorem §40.4]]), $\|\hat{\mathbf{x}} + \mathbf{z}\|^2 = \|\hat{\mathbf{x}}\|^2 + \|\mathbf{z}\|^2 \ge \|\hat{\mathbf{x}}\|^2$, with equality only for $\mathbf{z} = \mathbf{0}$.

^pf-51-8

*Uses:* [[§51★ The Singular Value Decomposition#^prop-51-7|§51.7]], [[§51★ The Singular Value Decomposition#^thm-51-5|§51.5]], [[§42 Orthogonal Projections#^thm-42-4|§42.4]], [[§42 Orthogonal Projections#^thm-42-3|§42.3]], [[§44 Least-Squares Problems#^def-44-1|Def. §44.1]] (least-squares solutions), [[§40 Inner Product, Length, and Orthogonality#^thm-40-4|§40.4]] (Pythagorean Theorem)

> [!remark]- Connections
> - Rigorous treatment: the pseudoinverse $T^\dagger$ is defined in [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-68|LADR 6.68]] without the SVD (invert $T$ on $(\operatorname{null} T)^\perp \to \operatorname{range} T$, after projecting), and [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-70|LADR 6.70]] proves exactly [[§51★ The Singular Value Decomposition#^thm-51-8|Theorem §51.8]], best approximate solution of smallest norm. Its SVD formula, Lay's (10), is [[§26 Singular Value Decomposition#^ladr-7-75|LADR 7.75]]: "swap the singular vectors and invert the positive singular values".

> [!example] Example §51.4: A Pseudoinverse
> Find the reduced SVD and the pseudoinverse of the matrix $A = \begin{bmatrix} 1 & -1 \\ -2 & 2 \\ 2 & -2 \end{bmatrix}$ of [[§51★ The Singular Value Decomposition#^ex-51-3|Example §51.3]].
>
> There $r = 1$, $D = [\,3\sqrt2\,]$, $U_r = \mathbf{u}_1 = \frac13(1, -2, 2)$ and $V_r = \mathbf{v}_1 = \frac{1}{\sqrt2}(1, -1)$. The reduced SVD is
>
> $$
> A = U_rDV_r^T = \frac13 \begin{bmatrix} 1 \\ -2 \\ 2 \end{bmatrix} [\,3\sqrt2\,] \frac{1}{\sqrt2} [\,1\ \ -1\,] = \begin{bmatrix} 1 \\ -2 \\ 2 \end{bmatrix} [\,1\ \ -1\,],
> $$
>
> which is indeed $A$. The pseudoinverse is
>
> $$
> A^+ = V_rD^{-1}U_r^T = \frac{1}{\sqrt2} \begin{bmatrix} 1 \\ -1 \end{bmatrix} \cdot \frac{1}{3\sqrt2} \cdot \frac13 [\,1\ \ -2\ \ 2\,] = \frac{1}{18} \begin{bmatrix} 1 & -2 & 2 \\ -1 & 2 & -2 \end{bmatrix}.
> $$
>
> Check [[§51★ The Singular Value Decomposition#^thm-51-8|Theorem §51.8]]: $AA^+ = \frac{1}{18}\begin{bmatrix} 1 \\ -2 \\ 2 \end{bmatrix}[\,1\ \ -1\,]\begin{bmatrix} 1 & -2 & 2 \\ -1 & 2 & -2 \end{bmatrix} = \frac{1}{18} \cdot 2 \begin{bmatrix} 1 \\ -2 \\ 2 \end{bmatrix}[\,1\ \ -2\ \ 2\,] = \frac19 \begin{bmatrix} 1 & -2 & 2 \\ -2 & 4 & -4 \\ 2 & -4 & 4 \end{bmatrix} = \mathbf{u}_1\mathbf{u}_1^T$, the projection onto the line $\operatorname{Col} A$ ([[§48★ Diagonalization of Symmetric Matrices#^thm-48-4|Theorem §48.4]]). So for any $\mathbf{b}$, $\hat{\mathbf{x}} = A^+\mathbf{b} = \frac{b_1 - 2b_2 + 2b_3}{18}(1, -1)$ is the least-squares solution of smallest length; it lies on the line $\operatorname{Row} A$ spanned by $(1, -1)$.
>
> *Lay: Examples 7.4.4, 7.4.7 and 7.4.8 (combined)*

^ex-51-4

> [!remark]- Remark: Numerical Note
> Examples [[§51★ The Singular Value Decomposition#^ex-51-1|§51.1]]–[[§51★ The Singular Value Decomposition#^ex-51-4|§51.4]] show how singular values can be computed by hand. In practice, the computation of $A^TA$ should be avoided, since any errors in the entries of $A$ are squared in the entries of $A^TA$. Fast iterative methods produce the singular values and singular vectors of $A$ directly, accurately to many decimal places. Lay's Practice Problems note two consequences of the SVD: $A^T = V\Sigma^TU^T$ is an SVD of $A^T$, so $A$ and $A^T$ have the same nonzero singular values; and for square $A$, $AA^T = U\Sigma^2U^T$ and $A^TA = V\Sigma^2V^T$ are orthogonally similar, $AA^T = Q^T(A^TA)Q$ with $Q = VU^T$. (Lay's Practice Problem 2 prints $A^TA = Q^T(A^TA)Q$; the remark after it shows that $AA^T$ is meant on the left.)

^rem-51-3
