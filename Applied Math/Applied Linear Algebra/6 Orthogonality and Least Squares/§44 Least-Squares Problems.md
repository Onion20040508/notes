---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 6
section: 44
lay: "6.5"
aliases: ["Lay 6.5"]
tags: [applied-linear-algebra, math235]
---
← [[§43 The Gram–Schmidt Process]] · ↑ [[· 6 Orthogonality and Least Squares]] · [[§45 Applications to Linear Models]] →

*Lay, Section 6.5.*

When $A\mathbf{x} = \mathbf{b}$ has no solution, the best one can do is to make $A\mathbf{x}$ as close to $\mathbf{b}$ as possible. Since $A\mathbf{x}$ ranges over $\operatorname{Col} A$, the closest it can get is $\hat{\mathbf{b}} = \operatorname{proj}_{\operatorname{Col} A} \mathbf{b}$ (Best Approximation Theorem), and a least-squares solution is any $\hat{\mathbf{x}}$ with $A\hat{\mathbf{x}} = \hat{\mathbf{b}}$. Orthogonality turns this into a linear system, the normal equations $A^TA\mathbf{x} = A^T\mathbf{b}$. The solution is unique exactly when the columns of $A$ are independent. For numerical work a QR factorization gives the same solution more reliably.

> [!definition] Definition §44.1: Least-Squares Solution
> If $A$ is $m \times n$ and $\mathbf{b}$ is in $\mathbb{R}^m$, a **least-squares solution** of $A\mathbf{x} = \mathbf{b}$ is an $\hat{\mathbf{x}}$ in $\mathbb{R}^n$ such that
>
> $$
> \|\mathbf{b} - A\hat{\mathbf{x}}\| \le \|\mathbf{b} - A\mathbf{x}\| \qquad\text{for all } \mathbf{x} \text{ in } \mathbb{R}^n .
> $$
>
> The **general least-squares problem** is to find such an $\hat{\mathbf{x}}$. The name comes from $\|\mathbf{b} - A\mathbf{x}\|$ being the square root of a sum of squares. If $\mathbf{b} \in \operatorname{Col} A$, the least-squares solutions are the ordinary solutions.
>
> *Lay: 6.5, Definition*

^def-44-1

## Solution of the General Least-Squares Problem

> [!definition] Definition §44.2: Normal Equations
> The system of equations
>
> $$
> A^TA\mathbf{x} = A^T\mathbf{b}
> $$
>
> is called the system of **normal equations** for $A\mathbf{x} = \mathbf{b}$. A solution of the normal equations is often denoted $\hat{\mathbf{x}}$.
>
> *Lay: 6.5 (text)*

^def-44-2

> [!theorem] Theorem §44.1: Least Squares via the Normal Equations
> The set of least-squares solutions of $A\mathbf{x} = \mathbf{b}$ coincides with the nonempty set of solutions of the normal equations $A^TA\mathbf{x} = A^T\mathbf{b}$.
>
> *Lay: Theorem 13 (6.5)*

^thm-44-1

> [!proof]+ Proof
> **Least-squares solutions are the solutions of $A\mathbf{x} = \hat{\mathbf{b}}$.** Let $\hat{\mathbf{b}} = \operatorname{proj}_{\operatorname{Col} A} \mathbf{b}$. Since $\hat{\mathbf{b}} \in \operatorname{Col} A$, the equation
>
> $$
> A\mathbf{x} = \hat{\mathbf{b}} \tag{1}
> $$
>
> is consistent. For every $\mathbf{x}$, $A\mathbf{x} \in \operatorname{Col} A$, and by the Best Approximation Theorem $\|\mathbf{b} - A\mathbf{x}\| \ge \|\mathbf{b} - \hat{\mathbf{b}}\|$, with equality only if $A\mathbf{x} = \hat{\mathbf{b}}$. So $\hat{\mathbf{x}}$ is a least-squares solution if and only if it satisfies (1). In particular, least-squares solutions exist.
>
> **Every least-squares solution satisfies the normal equations.** Let $A\hat{\mathbf{x}} = \hat{\mathbf{b}}$. By the Orthogonal Decomposition Theorem, $\mathbf{b} - \hat{\mathbf{b}}$ is orthogonal to $\operatorname{Col} A$, so $\mathbf{b} - A\hat{\mathbf{x}}$ is orthogonal to each column $\mathbf{a}_j$ of $A$: $\mathbf{a}_j^T(\mathbf{b} - A\hat{\mathbf{x}}) = 0$. The $\mathbf{a}_j^T$ are the rows of $A^T$, so
>
> $$
> A^T(\mathbf{b} - A\hat{\mathbf{x}}) = \mathbf{0}, \tag{2}
> $$
>
> that is, $A^T\mathbf{b} - A^TA\hat{\mathbf{x}} = \mathbf{0}$: $\hat{\mathbf{x}}$ satisfies the normal equations. (Equivalently, (2) says $\mathbf{b} - A\hat{\mathbf{x}} \in (\operatorname{Col} A)^\perp = \operatorname{Nul} A^T$, [[§40 Inner Product, Length, and Orthogonality#^thm-40-6|Theorem §40.6]].)
>
> **Every solution of the normal equations is a least-squares solution.** Suppose $A^TA\hat{\mathbf{x}} = A^T\mathbf{b}$. Then (2) holds, so $\mathbf{b} - A\hat{\mathbf{x}}$ is orthogonal to the rows of $A^T$, that is, to the columns of $A$. These span $\operatorname{Col} A$, so $\mathbf{b} - A\hat{\mathbf{x}}$ is orthogonal to all of $\operatorname{Col} A$. Hence
>
> $$
> \mathbf{b} = A\hat{\mathbf{x}} + (\mathbf{b} - A\hat{\mathbf{x}})
> $$
>
> decomposes $\mathbf{b}$ into a vector in $\operatorname{Col} A$ plus a vector in $(\operatorname{Col} A)^\perp$. By the uniqueness of the orthogonal decomposition, $A\hat{\mathbf{x}} = \hat{\mathbf{b}}$, and $\hat{\mathbf{x}}$ is a least-squares solution.

^pf-44-1

*Uses:* [[§42 Orthogonal Projections#^thm-42-1|§42.1]], [[§42 Orthogonal Projections#^thm-42-3|§42.3]], [[§40 Inner Product, Length, and Orthogonality#^thm-40-5|§40.5]], [[§40 Inner Product, Length, and Orthogonality#^thm-40-6|§40.6]]

![[m235-44-1.svg]]
*The least-squares solution $\hat{\mathbf{x}}$ lives in $\mathbb{R}^n$; $A$ maps it to $\hat{\mathbf{b}} = A\hat{\mathbf{x}}$, the point of $\operatorname{Col} A \subseteq \mathbb{R}^m$ closest to $\mathbf{b}$. The residual $\mathbf{b} - A\hat{\mathbf{x}}$ (red) is orthogonal to $\operatorname{Col} A$, which is what the normal equations $A^T(\mathbf{b} - A\hat{\mathbf{x}}) = \mathbf{0}$ express. Every other $A\mathbf{x}$ is farther from $\mathbf{b}$ (dashed).*

> [!remark]- Connections
> - Rigorous treatment: the minimization theorem [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-61|LADR 6.61]] applied to $U = \operatorname{range} T$, and the pseudoinverse [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-70|LADR 6.70]]: $T^\dagger b$ is a least-squares solution, and among all least-squares solutions the one of smallest norm (the one in $(\operatorname{null} T)^\perp$). The normal equations $T^*Tx = T^*b$ appear with the singular value decomposition, [[§26 Singular Value Decomposition|LADR 7E]].
> - Fitting a regression line by least squares, as used in Calculus: [[§2 Mathematical Models꞉ A Catalog of Essential Functions#^def-2-3|Calc Def. §2.3]] (empirical models); the computation behind it is [[§45 Applications to Linear Models|§45]].

> [!remark] Remark: Method — Least Squares via the Normal Equations
> To find the least-squares solutions of $A\mathbf{x} = \mathbf{b}$:
> 1. Compute $A^TA$ ($n \times n$, symmetric) and $A^T\mathbf{b}$ ($n \times 1$).
> 2. Solve $A^TA\mathbf{x} = A^T\mathbf{b}$ by row reducing $[\,A^TA \ \ A^T\mathbf{b}\,]$. This system is always consistent (Theorem §44.1). Free variables give infinitely many least-squares solutions.
> 3. If $A^TA$ is invertible and $2 \times 2$, it is quicker to use $\hat{\mathbf{x}} = (A^TA)^{-1}A^T\mathbf{b}$ (Theorem §44.2).
> 4. If needed, the least-squares error is $\|\mathbf{b} - A\hat{\mathbf{x}}\|$ (Definition §44.3).
>
> Shortcuts: if the columns of $A$ are orthogonal, compute $\hat{\mathbf{b}}$ by the projection formula and read off $\hat{\mathbf{x}}$ (Example §44.4); if $A = QR$ is known, solve $R\mathbf{x} = Q^T\mathbf{b}$ (Theorem §44.3). If $\mathbf{b}$ is orthogonal to the columns of $A$, then $\hat{\mathbf{b}} = \mathbf{0}$ and the least-squares solutions are the solutions of $A\mathbf{x} = \mathbf{0}$.

^rem-44-1

> [!example] Example §44.1: An Inconsistent System with a Unique Least-Squares Solution
> Find a least-squares solution of $A\mathbf{x} = \mathbf{b}$ for
>
> $$
> A = \begin{bmatrix} 4 & 0 \\ 0 & 2 \\ 1 & 1 \end{bmatrix}, \qquad \mathbf{b} = \begin{bmatrix} 2 \\ 0 \\ 11 \end{bmatrix} .
> $$
>
> (The system is inconsistent: the first two equations force $x_1 = \frac12$, $x_2 = 0$, and then $x_1 + x_2 = \frac12 \ne 11$.) Compute
>
> $$
> A^TA = \begin{bmatrix} 4 & 0 & 1 \\ 0 & 2 & 1 \end{bmatrix} \begin{bmatrix} 4 & 0 \\ 0 & 2 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 17 & 1 \\ 1 & 5 \end{bmatrix}, \qquad
> A^T\mathbf{b} = \begin{bmatrix} 4 & 0 & 1 \\ 0 & 2 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 0 \\ 11 \end{bmatrix} = \begin{bmatrix} 19 \\ 11 \end{bmatrix} .
> $$
>
> The normal equations are $\begin{bmatrix} 17 & 1 \\ 1 & 5 \end{bmatrix}\mathbf{x} = \begin{bmatrix} 19 \\ 11 \end{bmatrix}$. Since $\det A^TA = 85 - 1 = 84 \ne 0$,
>
> $$
> (A^TA)^{-1} = \frac{1}{84}\begin{bmatrix} 5 & -1 \\ -1 & 17 \end{bmatrix}, \qquad
> \hat{\mathbf{x}} = (A^TA)^{-1}A^T\mathbf{b} = \frac{1}{84}\begin{bmatrix} 95 - 11 \\ -19 + 187 \end{bmatrix} = \frac{1}{84}\begin{bmatrix} 84 \\ 168 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \end{bmatrix} .
> $$
>
> *Lay: Example 6.5.1*

^ex-44-1

> [!example] Example §44.2: Infinitely Many Least-Squares Solutions
> Find the least-squares solutions of $A\mathbf{x} = \mathbf{b}$ for
>
> $$
> A = \begin{bmatrix} 1 & 1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 0 & 0 & 1 \\ 1 & 0 & 0 & 1 \end{bmatrix}, \qquad \mathbf{b} = \begin{bmatrix} -3 \\ -1 \\ 0 \\ 2 \\ 5 \\ 1 \end{bmatrix} .
> $$
>
> (A matrix of this sort appears in analysis of variance problems in statistics.) Column 1 is the sum of the other three, so $A^TA$ will not be invertible. Each entry of $A^TA$ is the inner product of two columns of $A$, and each entry of $A^T\mathbf{b}$ is a column of $A$ dotted with $\mathbf{b}$:
>
> $$
> A^TA = \begin{bmatrix} 6 & 2 & 2 & 2 \\ 2 & 2 & 0 & 0 \\ 2 & 0 & 2 & 0 \\ 2 & 0 & 0 & 2 \end{bmatrix}, \qquad
> A^T\mathbf{b} = \begin{bmatrix} -3 - 1 + 0 + 2 + 5 + 1 \\ -3 - 1 \\ 0 + 2 \\ 5 + 1 \end{bmatrix} = \begin{bmatrix} 4 \\ -4 \\ 2 \\ 6 \end{bmatrix} .
> $$
>
> Row reduce the augmented matrix of the normal equations:
>
> $$
> \begin{bmatrix} 6 & 2 & 2 & 2 & 4 \\ 2 & 2 & 0 & 0 & -4 \\ 2 & 0 & 2 & 0 & 2 \\ 2 & 0 & 0 & 2 & 6 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & 0 & 1 & 3 \\ 0 & 1 & 0 & -1 & -5 \\ 0 & 0 & 1 & -1 & -2 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> So $x_1 = 3 - x_4$, $x_2 = -5 + x_4$, $x_3 = -2 + x_4$, with $x_4$ free, and the general least-squares solution is
>
> $$
> \hat{\mathbf{x}} = \begin{bmatrix} 3 \\ -5 \\ -2 \\ 0 \end{bmatrix} + x_4\begin{bmatrix} -1 \\ 1 \\ 1 \\ 1 \end{bmatrix} .
> $$
>
> (Check with the first normal equation: $6(3 - x_4) + 2(-5 + x_4) + 2(-2 + x_4) + 2x_4 = 18 - 10 - 4 = 4$.) The direction vector $(-1, 1, 1, 1)$ spans $\operatorname{Nul} A$, and all these $\hat{\mathbf{x}}$ give the same $A\hat{\mathbf{x}} = \hat{\mathbf{b}}$.
>
> *Lay: Example 6.5.2*

^ex-44-2

> [!theorem] Theorem §44.2: When the Least-Squares Solution Is Unique
> Let $A$ be an $m \times n$ matrix. The following statements are logically equivalent:
>
> a. The equation $A\mathbf{x} = \mathbf{b}$ has a unique least-squares solution for each $\mathbf{b}$ in $\mathbb{R}^m$.
>
> b. The columns of $A$ are linearly independent.
>
> c. The matrix $A^TA$ is invertible.
>
> When these statements are true, the least-squares solution $\hat{\mathbf{x}}$ is given by
>
> $$
> \hat{\mathbf{x}} = (A^TA)^{-1}A^T\mathbf{b} . \tag{4}
> $$
>
> *Lay: Theorem 14 (6.5)*

^thm-44-2

> [!proof]+ Proof
> Lay outlines the proof in Exercises 19–21; here it is in full.
>
> **Key fact: $\operatorname{Nul}(A^TA) = \operatorname{Nul} A$.** If $A\mathbf{x} = \mathbf{0}$, then $A^TA\mathbf{x} = A^T\mathbf{0} = \mathbf{0}$. Conversely, if $A^TA\mathbf{x} = \mathbf{0}$, then
>
> $$
> 0 = \mathbf{x}^TA^TA\mathbf{x} = (A\mathbf{x})^T(A\mathbf{x}) = \|A\mathbf{x}\|^2,
> $$
>
> so $A\mathbf{x} = \mathbf{0}$.
>
> **(a) ⇔ (b).** By the proof of Theorem §44.1, the least-squares solutions of $A\mathbf{x} = \mathbf{b}$ are the solutions of the consistent equation $A\mathbf{x} = \hat{\mathbf{b}}$. Its solution set is $\mathbf{p} + \operatorname{Nul} A$ for any particular solution $\mathbf{p}$, so it is a single vector if and only if $\operatorname{Nul} A = \{\mathbf{0}\}$, that is, if and only if the columns of $A$ are linearly independent. (For (a) ⇒ (b), apply this to any one $\mathbf{b}$, say $\mathbf{b} = \mathbf{0}$.)
>
> **(b) ⇔ (c).** $A^TA$ is a square $n \times n$ matrix, so by the Invertible Matrix Theorem it is invertible if and only if $\operatorname{Nul}(A^TA) = \{\mathbf{0}\}$. By the key fact this means $\operatorname{Nul} A = \{\mathbf{0}\}$, which is (b).
>
> **Formula (4).** If $A^TA$ is invertible, the normal equations $A^TA\mathbf{x} = A^T\mathbf{b}$ have the unique solution $(A^TA)^{-1}A^T\mathbf{b}$, which by Theorem §44.1 is the least-squares solution.

^pf-44-2

*Uses:* [[§44 Least-Squares Problems#^thm-44-1|§44.1]], [[§5 Solution Sets of Linear Systems#^thm-5-3|§5.3]] (solution set of $A\mathbf{x} = \mathbf{b}$ as $\mathbf{p} + \operatorname{Nul} A$), [[§7 Linear Independence#^prop-7-1|§7.1]] (independent columns iff $A\mathbf{x} = \mathbf{0}$ has only the trivial solution), [[§13 Characterizations of Invertible Matrices#^thm-13-1|§13.1]] (the Invertible Matrix Theorem)

Formula (4) is mainly of theoretical use, and for hand calculations when $A^TA$ is an invertible $2 \times 2$ matrix. In every case the projection $\hat{\mathbf{b}}$ is unique; only $\hat{\mathbf{x}}$ can fail to be.

> [!definition] Definition §44.3: Least-Squares Error
> When a least-squares solution $\hat{\mathbf{x}}$ is used to produce $A\hat{\mathbf{x}}$ as an approximation to $\mathbf{b}$, the distance $\|\mathbf{b} - A\hat{\mathbf{x}}\|$ from $\mathbf{b}$ to $A\hat{\mathbf{x}}$ is the **least-squares error** of the approximation. It is the same for all least-squares solutions, since all have $A\hat{\mathbf{x}} = \hat{\mathbf{b}}$.
>
> *Lay: 6.5 (text)*

^def-44-3

> [!example] Example §44.3: The Least-Squares Error
> For $A$ and $\mathbf{b}$ as in Example §44.1, find the least-squares error.
>
> With $\hat{\mathbf{x}} = (1, 2)$,
>
> $$
> A\hat{\mathbf{x}} = \begin{bmatrix} 4 & 0 \\ 0 & 2 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 4 \\ 4 \\ 3 \end{bmatrix}, \qquad
> \mathbf{b} - A\hat{\mathbf{x}} = \begin{bmatrix} 2 \\ 0 \\ 11 \end{bmatrix} - \begin{bmatrix} 4 \\ 4 \\ 3 \end{bmatrix} = \begin{bmatrix} -2 \\ -4 \\ 8 \end{bmatrix},
> $$
>
> $$
> \|\mathbf{b} - A\hat{\mathbf{x}}\| = \sqrt{(-2)^2 + (-4)^2 + 8^2} = \sqrt{84} .
> $$
>
> So for every $\mathbf{x} \in \mathbb{R}^2$ the distance from $\mathbf{b}$ to $A\mathbf{x}$ is at least $\sqrt{84}$. Check that the residual is orthogonal to the columns $(4, 0, 1)$ and $(0, 2, 1)$ of $A$: $-8 + 0 + 8 = 0$ and $0 - 8 + 8 = 0$.
>
> *Lay: Example 6.5.3*

^ex-44-3

## Alternative Calculations of Least-Squares Solutions

> [!example] Example §44.4: A Matrix with Orthogonal Columns
> Find a least-squares solution of $A\mathbf{x} = \mathbf{b}$ for
>
> $$
> A = \begin{bmatrix} 1 & -6 \\ 1 & -2 \\ 1 & 1 \\ 1 & 7 \end{bmatrix}, \qquad \mathbf{b} = \begin{bmatrix} -1 \\ 2 \\ 1 \\ 6 \end{bmatrix} .
> $$
>
> The columns $\mathbf{a}_1$, $\mathbf{a}_2$ are orthogonal: $\mathbf{a}_1 \cdot \mathbf{a}_2 = -6 - 2 + 1 + 7 = 0$. So the projection of $\mathbf{b}$ onto $\operatorname{Col} A$ is given by [[§42 Orthogonal Projections#^thm-42-1|formula (2) of Theorem §42.1]]. With $\mathbf{b} \cdot \mathbf{a}_1 = -1 + 2 + 1 + 6 = 8$, $\mathbf{a}_1 \cdot \mathbf{a}_1 = 4$, $\mathbf{b} \cdot \mathbf{a}_2 = 6 - 4 + 1 + 42 = 45$, $\mathbf{a}_2 \cdot \mathbf{a}_2 = 36 + 4 + 1 + 49 = 90$:
>
> $$
> \hat{\mathbf{b}} = \frac{8}{4}\mathbf{a}_1 + \frac{45}{90}\mathbf{a}_2 = \begin{bmatrix} 2 \\ 2 \\ 2 \\ 2 \end{bmatrix} + \begin{bmatrix} -3 \\ -1 \\ 1/2 \\ 7/2 \end{bmatrix} = \begin{bmatrix} -1 \\ 1 \\ 5/2 \\ 11/2 \end{bmatrix} .
> $$
>
> Now solving $A\hat{\mathbf{x}} = \hat{\mathbf{b}}$ is trivial: the weights on the columns are already known, so
>
> $$
> \hat{\mathbf{x}} = \begin{bmatrix} 8/4 \\ 45/90 \end{bmatrix} = \begin{bmatrix} 2 \\ 1/2 \end{bmatrix} .
> $$
>
> (The normal equations agree: $A^TA = \operatorname{diag}(4, 90)$ and $A^T\mathbf{b} = (8, 45)$.)
>
> *Lay: Example 6.5.4*

^ex-44-4

> [!remark] Remark: Ill-Conditioned Normal Equations
> The normal equations can be *ill-conditioned*: small errors in computing the entries of $A^TA$ may cause relatively large errors in $\hat{\mathbf{x}}$. If the columns of $A$ are linearly independent, the least-squares solution can often be computed more reliably from a QR factorization of $A$ ([[§43 The Gram–Schmidt Process#^thm-43-3|Theorem §43.3]]), which avoids forming $A^TA$.

^rem-44-2

> [!theorem] Theorem §44.3: Least Squares via QR
> Given an $m \times n$ matrix $A$ with linearly independent columns, let $A = QR$ be a QR factorization of $A$ as in [[§43 The Gram–Schmidt Process#^thm-43-3|Theorem §43.3]]. Then, for each $\mathbf{b}$ in $\mathbb{R}^m$, the equation $A\mathbf{x} = \mathbf{b}$ has a unique least-squares solution, given by
>
> $$
> \hat{\mathbf{x}} = R^{-1}Q^T\mathbf{b} . \tag{6}
> $$
>
> *Lay: Theorem 15 (6.5)*

^thm-44-3

> [!proof]+ Proof
> $R$ is invertible by [[§43 The Gram–Schmidt Process#^thm-43-3|Theorem §43.3]]. Let $\hat{\mathbf{x}} = R^{-1}Q^T\mathbf{b}$. Then
>
> $$
> A\hat{\mathbf{x}} = QR\hat{\mathbf{x}} = QRR^{-1}Q^T\mathbf{b} = QQ^T\mathbf{b} .
> $$
>
> The columns of $Q$ form an orthonormal basis of $\operatorname{Col} A$, so by [[§42 Orthogonal Projections#^thm-42-4|Theorem §42.4]], $QQ^T\mathbf{b}$ is the orthogonal projection $\hat{\mathbf{b}}$ of $\mathbf{b}$ onto $\operatorname{Col} A$. Thus $A\hat{\mathbf{x}} = \hat{\mathbf{b}}$, and $\hat{\mathbf{x}}$ is a least-squares solution (proof of Theorem §44.1). It is the only one by Theorem §44.2, since the columns of $A$ are independent.

^pf-44-3

*Uses:* [[§43 The Gram–Schmidt Process#^thm-43-3|§43.3]], [[§42 Orthogonal Projections#^thm-42-4|§42.4]], [[§44 Least-Squares Problems#^thm-44-1|§44.1]], [[§44 Least-Squares Problems#^thm-44-2|§44.2]]

> [!remark] Remark: Numerical Note — Back-Substitution
> Since $R$ is upper triangular, compute $\hat{\mathbf{x}}$ as the exact solution of
>
> $$
> R\mathbf{x} = Q^T\mathbf{b} \tag{7}
> $$
>
> by back-substitution or row operations. This is much faster than computing $R^{-1}$ and using (6).

^rem-44-3

> [!example] Example §44.5: Least Squares with a QR Factorization
> Find the least-squares solution of $A\mathbf{x} = \mathbf{b}$ for
>
> $$
> A = \begin{bmatrix} 1 & 3 & 5 \\ 1 & 1 & 0 \\ 1 & 1 & 2 \\ 1 & 3 & 3 \end{bmatrix}, \qquad \mathbf{b} = \begin{bmatrix} 3 \\ 5 \\ 7 \\ -3 \end{bmatrix} .
> $$
>
> A QR factorization (obtained as in [[§43 The Gram–Schmidt Process#^rem-43-2|the QR method of §43]]) is
>
> $$
> A = QR = \begin{bmatrix} 1/2 & 1/2 & 1/2 \\ 1/2 & -1/2 & -1/2 \\ 1/2 & -1/2 & 1/2 \\ 1/2 & 1/2 & -1/2 \end{bmatrix} \begin{bmatrix} 2 & 4 & 5 \\ 0 & 2 & 3 \\ 0 & 0 & 2 \end{bmatrix} .
> $$
>
> (Check row 2: $(\frac12, -\frac12, -\frac12)R = (1, 2 - 1, \frac52 - \frac32 - 1) = (1, 1, 0)$.) Then
>
> $$
> Q^T\mathbf{b} = \begin{bmatrix} 1/2 & 1/2 & 1/2 & 1/2 \\ 1/2 & -1/2 & -1/2 & 1/2 \\ 1/2 & -1/2 & 1/2 & -1/2 \end{bmatrix} \begin{bmatrix} 3 \\ 5 \\ 7 \\ -3 \end{bmatrix} = \begin{bmatrix} (3 + 5 + 7 - 3)/2 \\ (3 - 5 - 7 - 3)/2 \\ (3 - 5 + 7 + 3)/2 \end{bmatrix} = \begin{bmatrix} 6 \\ -6 \\ 4 \end{bmatrix} .
> $$
>
> Solve $R\mathbf{x} = Q^T\mathbf{b}$ by back-substitution:
>
> $$
> \begin{bmatrix} 2 & 4 & 5 \\ 0 & 2 & 3 \\ 0 & 0 & 2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 6 \\ -6 \\ 4 \end{bmatrix}: \qquad
> x_3 = 2, \quad 2x_2 + 6 = -6 \Rightarrow x_2 = -6, \quad 2x_1 - 24 + 10 = 6 \Rightarrow x_1 = 10 .
> $$
>
> So $\hat{\mathbf{x}} = (10, -6, 2)$.
>
> *Lay: Example 6.5.5*

^ex-44-5
