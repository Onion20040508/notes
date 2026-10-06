---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 7
section: 50
lay: "7.3"
aliases: ["Lay 7.3"]
tags: [applied-linear-algebra, math235, extension]
---
← [[§49★ Quadratic Forms]] · ↑ [[· 7★ Symmetric Matrices and Quadratic Forms]] · [[§51★ The Singular Value Decomposition]] →

*Lay, Section 7.3.*
★ *Beyond MATH 235: the course ended with inner products (Ch. 6); Chapter 7 is included from Lay as the continuation.*

How large and how small can a quadratic form $\mathbf{x}^T A \mathbf{x}$ be on the unit sphere $\|\mathbf{x}\| = 1$? The answer is exactly the largest and the smallest eigenvalue of $A$, attained at the corresponding unit eigenvectors. Adding the constraints that $\mathbf{x}$ be orthogonal to the first few eigenvectors picks out the next eigenvalues one by one, so all eigenvalues of a symmetric matrix are solutions of optimization problems. The proofs are one line each after the Principal Axes Theorem of §49: in the coordinates of the principal axes the form is $\lambda_1 y_1^2 + \cdots + \lambda_n y_n^2$, and an orthogonal change of variable keeps the sphere a sphere. These results drive the singular value decomposition (§51) and principal component analysis (§52).

## Maximum and Minimum on the Unit Sphere

The requirement that a vector $\mathbf{x}$ in $\mathbb{R}^n$ be a unit vector can be stated in several equivalent ways:

$$
\|\mathbf{x}\| = 1, \qquad \|\mathbf{x}\|^2 = 1, \qquad \mathbf{x}^T\mathbf{x} = 1, \qquad x_1^2 + x_2^2 + \cdots + x_n^2 = 1 . \qquad (1)
$$

The expanded version is the one commonly used in applications. When the form has no cross-product terms, its extreme values on the unit sphere can be read off by comparing coefficients.

> [!example] Example §50.1: A Form Without Cross-Product Terms
> Find the maximum and minimum values of $Q(\mathbf{x}) = 9x_1^2 + 4x_2^2 + 3x_3^2$ subject to the constraint $\mathbf{x}^T\mathbf{x} = 1$.
>
> **Maximum.** Since $x_2^2$ and $x_3^2$ are nonnegative, $4x_2^2 \le 9x_2^2$ and $3x_3^2 \le 9x_3^2$. Hence, whenever $x_1^2 + x_2^2 + x_3^2 = 1$,
>
> $$
> Q(\mathbf{x}) = 9x_1^2 + 4x_2^2 + 3x_3^2 \le 9x_1^2 + 9x_2^2 + 9x_3^2 = 9(x_1^2 + x_2^2 + x_3^2) = 9 .
> $$
>
> So $Q(\mathbf{x})$ cannot exceed $9$ on unit vectors, and $Q(1, 0, 0) = 9$. The maximum is $9$.
>
> **Minimum.** Similarly $9x_1^2 \ge 3x_1^2$ and $4x_2^2 \ge 3x_2^2$, so on unit vectors
>
> $$
> Q(\mathbf{x}) \ge 3x_1^2 + 3x_2^2 + 3x_3^2 = 3(x_1^2 + x_2^2 + x_3^2) = 3 ,
> $$
>
> and $Q(0, 0, 1) = 3$. The minimum is $3$.
>
> The matrix of $Q$ is $\operatorname{diag}(9, 4, 3)$, with eigenvalues $9, 4, 3$: the greatest and least eigenvalues are the constrained maximum and minimum.
>
> **Geometrically** (Lay's Example 2), for $Q(\mathbf{x}) = 3x_1^2 + 7x_2^2$ on $\mathbb{R}^2$ the constrained values are the heights $z$ of the curve in which the surface $z = Q(x_1, x_2)$ meets the cylinder $x_1^2 + x_2^2 = 1$. Its two highest points, at height $7$, lie over $(0, \pm 1)$, the unit eigenvectors for the eigenvalue $7$ of $\operatorname{diag}(3, 7)$; its two lowest points, at height $3$, lie over $(\pm 1, 0)$, the unit eigenvectors for $3$. Every height $t$ with $3 \le t \le 7$ occurs on the curve.
>
> *Lay: Examples 7.3.1 and 7.3.2*

^ex-50-1

> [!definition] Definition §50.1: Constrained Maximum and Minimum of a Quadratic Form
> For a symmetric matrix $A$, let
>
> $$
> m = \min\{\mathbf{x}^T A \mathbf{x} : \|\mathbf{x}\| = 1\}, \qquad M = \max\{\mathbf{x}^T A \mathbf{x} : \|\mathbf{x}\| = 1\} . \qquad (2)
> $$
>
> Here *minimum* and *maximum* (and *least* and *greatest* below) refer to the natural order of the real numbers, not to magnitudes. That the minimum and maximum exist is part of Theorem §50.1.
>
> *Lay: 7.3, Equation (2)*

^def-50-1

> [!theorem] Theorem §50.1: Extreme Values Are Extreme Eigenvalues
> Let $A$ be a symmetric matrix, and define $m$ and $M$ as in (2). Then $M$ is the greatest eigenvalue $\lambda_1$ of $A$ and $m$ is the least eigenvalue of $A$. The value of $\mathbf{x}^T A \mathbf{x}$ is $M$ when $\mathbf{x}$ is a unit eigenvector $\mathbf{u}_1$ corresponding to $M$. The value of $\mathbf{x}^T A \mathbf{x}$ is $m$ when $\mathbf{x}$ is a unit eigenvector corresponding to $m$.
>
> *Lay: Theorem 6 (7.3)*

^thm-50-1

> [!proof]+ Proof
> Orthogonally diagonalize $A$ as $PDP^{-1} = PDP^T$, with the eigenvalues arranged as $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_n$ on the diagonal of $D$ and the corresponding unit eigenvectors as the columns $\mathbf{u}_1, \dots, \mathbf{u}_n$ of $P$. By the Principal Axes Theorem,
>
> $$
> \mathbf{x}^T A \mathbf{x} = \mathbf{y}^T D \mathbf{y} \qquad \text{when } \mathbf{x} = P\mathbf{y} . \qquad (3)
> $$
>
> Also $\|\mathbf{x}\| = \|P\mathbf{y}\| = \|\mathbf{y}\|$ for all $\mathbf{y}$, because $P^TP = I$ and $\|P\mathbf{y}\|^2 = (P\mathbf{y})^T(P\mathbf{y}) = \mathbf{y}^T P^T P \mathbf{y} = \mathbf{y}^T\mathbf{y} = \|\mathbf{y}\|^2$. In particular $\|\mathbf{y}\| = 1$ if and only if $\|\mathbf{x}\| = 1$, so $\mathbf{x}^T A \mathbf{x}$ and $\mathbf{y}^T D \mathbf{y}$ take the same set of values as $\mathbf{x}$ and $\mathbf{y}$ range over the unit vectors.
>
> (Lay writes the argument for a $3 \times 3$ matrix with eigenvalues $a \ge b \ge c$; here it is for $n \times n$.) Given any unit vector $\mathbf{y}$, since $\lambda_i y_i^2 \le \lambda_1 y_i^2$ for every $i$,
>
> $$
> \mathbf{y}^T D \mathbf{y} = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \cdots + \lambda_n y_n^2 \le \lambda_1 y_1^2 + \lambda_1 y_2^2 + \cdots + \lambda_1 y_n^2 = \lambda_1 \|\mathbf{y}\|^2 = \lambda_1 .
> $$
>
> Thus every constrained value is $\le \lambda_1$. But $\mathbf{y}^T D \mathbf{y} = \lambda_1$ when $\mathbf{y} = \mathbf{e}_1 = (1, 0, \dots, 0)$, so the maximum exists and $M = \lambda_1$. By (3), the $\mathbf{x}$ that corresponds to $\mathbf{y} = \mathbf{e}_1$ is the eigenvector $\mathbf{u}_1$:
>
> $$
> \mathbf{x} = P\mathbf{e}_1 = [\,\mathbf{u}_1\ \ \mathbf{u}_2\ \cdots\ \mathbf{u}_n\,] \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix} = \mathbf{u}_1 ,
> $$
>
> and $M = \lambda_1 = \mathbf{e}_1^T D \mathbf{e}_1 = \mathbf{u}_1^T A \mathbf{u}_1$. In the same way $\lambda_i y_i^2 \ge \lambda_n y_i^2$ gives $\mathbf{y}^T D \mathbf{y} \ge \lambda_n$ on unit vectors, with equality at $\mathbf{y} = \mathbf{e}_n$, that is, at $\mathbf{x} = P\mathbf{e}_n = \mathbf{u}_n$. So $m = \lambda_n$, the least eigenvalue, attained at $\mathbf{u}_n$.

^pf-50-1

*Uses:* [[§49★ Quadratic Forms#^thm-49-2|§49.2]] (Principal Axes Theorem), [[§48★ Diagonalization of Symmetric Matrices#^thm-48-3|§48.3]], [[§50★ Constrained Optimization#^def-50-1|Def. §50.1]], [[§41 Orthogonal Sets#^thm-41-5|§41.5]] ($\|P\mathbf{y}\| = \|\mathbf{y}\|$)

> [!remark]- Connections
> - The same answer by Lagrange multipliers: maximize $f(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$ subject to $g(\mathbf{x}) = \mathbf{x}^T\mathbf{x} - 1 = 0$. Since $\nabla f = 2A\mathbf{x}$ (using $A^T = A$) and $\nabla g = 2\mathbf{x} \ne \mathbf{0}$ on the sphere, the Lagrange condition $\nabla f = \lambda \nabla g$ is exactly $A\mathbf{x} = \lambda\mathbf{x}$: the constrained critical points are the unit eigenvectors, and there $f(\mathbf{x}) = \lambda\,\mathbf{x}^T\mathbf{x} = \lambda$. The sphere is compact ([[Heine–Borel Theorem|590 Thm. §15.12]]), so the maximum and minimum exist ([[Continuous Image of a Compact Space is Compact|590 Thm. §15.3]]) and are the largest and smallest eigenvalues. See [[§97 Lagrange Multipliers#^thm-97-1|Calc Thm. §97.1]] and, rigorously in $\mathbb{R}^n$, [[§14 Optimization and Lagrange Multipliers#^thm-14-3|452 Thm. §14.3]]. The proof above avoids calculus altogether.
> - For a symmetric $A$, Theorem §50.1 also gives $\max_{\|\mathbf{x}\| = 1} \|A\mathbf{x}\| = \max_i |\lambda_i|$, the operator norm: [[§27 Consequences of Singular Value Decomposition#^ladr-7-90|LADR 7.90]], [[§27 Consequences of Singular Value Decomposition#^ladr-7-88|LADR 7.88]].
> - PDE version: [[§33★ Estimation of Eigenvalues#^thm-33-2|341 Thm. §33.2]] (Rayleigh's bound: the lowest eigenvalue of a Sturm–Liouville problem is at most the Rayleigh quotient $N(y)/D(y)$ of any trial function, with equality for the first eigenfunction, [[§33★ Estimation of Eigenvalues#^prop-33-1|341 Prop. §33.1]]).

> [!theorem] Corollary §50.2: The Range of a Quadratic Form on the Unit Sphere
> Let $A$ be symmetric with $m$ and $M$ as in (2).
> - (a) Every eigenvalue $\lambda$ of $A$ satisfies $m \le \lambda \le M$.
> - (b) The set of all values of $\mathbf{x}^T A \mathbf{x}$ for $\|\mathbf{x}\| = 1$ is the closed interval $[m, M]$.
>
> *Lay: 7.3 (text; Exercises 12 and 13)*

^cor-50-2

> [!proof]+ Proof
> **(a)** (Exercise 12.) Let $A\mathbf{x} = \lambda\mathbf{x}$ with $\mathbf{x}$ a unit vector (normalize any eigenvector). Then $\mathbf{x}^T A \mathbf{x} = \mathbf{x}^T(\lambda\mathbf{x}) = \lambda\,\mathbf{x}^T\mathbf{x} = \lambda$, so $\lambda$ is one of the values in (2), and $m \le \lambda \le M$.
>
> **(b)** (Exercise 13.) By definition every value lies in $[m, M]$. Conversely, let $m \le t \le M$. As in the proof of Theorem §50.1, let $\mathbf{u}_1$ and $\mathbf{u}_n$ be the first and last columns of an orthogonal $P$ that diagonalizes $A$, unit eigenvectors for $M$ and $m$ ($\mathbf{u}_1 \cdot \mathbf{u}_n = 0$ if $n \ge 2$; for $n = 1$ there is nothing to prove). Write $t = (1 - \alpha)m + \alpha M$ with $0 \le \alpha \le 1$ (possible since $t$ lies between $m$ and $M$), and let
>
> $$
> \mathbf{x} = \sqrt{1 - \alpha}\,\mathbf{u}_n + \sqrt{\alpha}\,\mathbf{u}_1 .
> $$
>
> Since $\mathbf{u}_n$ and $\mathbf{u}_1$ are orthonormal, $\mathbf{x}^T\mathbf{x} = (1 - \alpha) + \alpha = 1$. And since $A\mathbf{x} = \sqrt{1 - \alpha}\, m\,\mathbf{u}_n + \sqrt\alpha\, M \mathbf{u}_1$, the cross terms vanish again and
>
> $$
> \mathbf{x}^T A \mathbf{x} = (1 - \alpha) m + \alpha M = t .
> $$

^pf-50-2

*Uses:* [[§50★ Constrained Optimization#^thm-50-1|§50.1]], [[§50★ Constrained Optimization#^def-50-1|Def. §50.1]]

> [!example] Example §50.2: The Maximum of a Form With Cross-Product Terms
> Let $A = \begin{bmatrix} 3 & 2 & 1 \\ 2 & 3 & 1 \\ 1 & 1 & 4 \end{bmatrix}$. Find the maximum value of the quadratic form $\mathbf{x}^T A \mathbf{x}$ subject to the constraint $\mathbf{x}^T\mathbf{x} = 1$, and find a unit vector at which this maximum is attained.
>
> By Theorem §50.1, the maximum is the greatest eigenvalue of $A$. The characteristic equation is
>
> $$
> 0 = -\lambda^3 + 10\lambda^2 - 27\lambda + 18 = -(\lambda - 6)(\lambda - 3)(\lambda - 1) ,
> $$
>
> so the greatest eigenvalue is $6$. The maximum is attained at a unit eigenvector for $\lambda = 6$. Solve $(A - 6I)\mathbf{x} = \mathbf{0}$:
>
> $$
> A - 6I = \begin{bmatrix} -3 & 2 & 1 \\ 2 & -3 & 1 \\ 1 & 1 & -2 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{bmatrix}
> \ \Rightarrow\ \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}, \qquad \mathbf{u}_1 = \begin{bmatrix} 1/\sqrt3 \\ 1/\sqrt3 \\ 1/\sqrt3 \end{bmatrix}.
> $$
>
> Check: $A\mathbf{u}_1 = \frac{1}{\sqrt3}(6, 6, 6) = 6\mathbf{u}_1$, so $\mathbf{u}_1^T A \mathbf{u}_1 = 6$. The minimum on the unit sphere is the least eigenvalue, $1$.
>
> *Lay: Example 7.3.3*

^ex-50-2

> [!example] Example §50.3: A Change of Variable, and a Common Error
> Let $Q(\mathbf{x}) = 3x_1^2 + 3x_2^2 + 2x_1x_2$. Find a change of variable that removes the cross-product term, and the maximum of $Q$ on unit vectors with a unit vector at which it is attained.
>
> The matrix is $A = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}$, with characteristic polynomial $(3 - \lambda)^2 - 1 = (\lambda - 4)(\lambda - 2)$. Unit eigenvectors: $(1/\sqrt2, 1/\sqrt2)$ for $4$ (from $A - 4I = \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}$) and $(-1/\sqrt2, 1/\sqrt2)$ for $2$. So
>
> $$
> \mathbf{x} = P\mathbf{y}, \quad P = \begin{bmatrix} 1/\sqrt2 & -1/\sqrt2 \\ 1/\sqrt2 & 1/\sqrt2 \end{bmatrix}, \qquad Q = \mathbf{y}^T D \mathbf{y} = 4y_1^2 + 2y_2^2 .
> $$
>
> (A common error is to forget to normalize the eigenvectors: then $P$ is not orthogonal and $P^TAP \ne D$.)
>
> The maximum of $Q(\mathbf{x})$ for a unit vector $\mathbf{x}$ is $4$, attained at the unit eigenvector $\mathbf{x} = (1/\sqrt2, 1/\sqrt2)$; indeed $Q = \frac32 + \frac32 + 1 = 4$ there. A common incorrect answer is $(1, 0)$: that vector maximizes $\mathbf{y}^T D \mathbf{y}$ in the *$\mathbf{y}$-coordinates*, and the corresponding $\mathbf{x}$ is $P\mathbf{e}_1 = (1/\sqrt2, 1/\sqrt2)$. (At $\mathbf{x} = (1, 0)$, $Q = 3$.)
>
> *Lay: 7.3, Practice Problems 1–2*

^ex-50-3

## Further Constraints: The Other Eigenvalues

> [!theorem] Theorem §50.3: The Second Eigenvalue
> Let $A$, $\lambda_1$ and $\mathbf{u}_1$ be as in Theorem §50.1. Then the maximum value of $\mathbf{x}^T A \mathbf{x}$ subject to the constraints
>
> $$
> \mathbf{x}^T\mathbf{x} = 1, \qquad \mathbf{x}^T\mathbf{u}_1 = 0
> $$
>
> is the second greatest eigenvalue, $\lambda_2$, and this maximum is attained when $\mathbf{x}$ is an eigenvector $\mathbf{u}_2$ corresponding to $\lambda_2$.
>
> *Lay: Theorem 7 (7.3)*

^thm-50-3

> [!proof]+ Proof
> *Lay gives this as a sketch* ("an argument similar to the one above in which the theorem is reduced to the case where the matrix of the quadratic form is diagonal", with Example §50.4 below as the diagonal case). It is the case $k = 2$ of Theorem §50.4, whose proof follows.

^pf-50-3

*Uses:* [[§50★ Constrained Optimization#^thm-50-4|§50.4]]

> [!example] Example §50.4: Maximizing Orthogonally to the First Eigenvector
> **(a) A diagonal form.** Find the maximum value of $9x_1^2 + 4x_2^2 + 3x_3^2$ subject to $\mathbf{x}^T\mathbf{x} = 1$ and $\mathbf{x}^T\mathbf{u}_1 = 0$, where $\mathbf{u}_1 = (1, 0, 0)$, a unit eigenvector for the greatest eigenvalue $9$ of the matrix of the form.
>
> The constraint $\mathbf{x}^T\mathbf{u}_1 = 0$ means simply $x_1 = 0$. For such a unit vector, $x_2^2 + x_3^2 = 1$, and
>
> $$
> 9x_1^2 + 4x_2^2 + 3x_3^2 = 4x_2^2 + 3x_3^2 \le 4x_2^2 + 4x_3^2 = 4(x_2^2 + x_3^2) = 4 .
> $$
>
> The value $4$ is attained at $\mathbf{x} = (0, 1, 0)$, an eigenvector for the second greatest eigenvalue. So the constrained maximum is $4$.
>
> **(b) The matrix of Example §50.2.** Let $\mathbf{u}_1 = (1, 1, 1)/\sqrt3$ be the unit eigenvector for the greatest eigenvalue $6$ of $A = \begin{bmatrix} 3 & 2 & 1 \\ 2 & 3 & 1 \\ 1 & 1 & 4 \end{bmatrix}$. Find the maximum of $\mathbf{x}^T A \mathbf{x}$ subject to
>
> $$
> \mathbf{x}^T\mathbf{x} = 1, \qquad \mathbf{x}^T\mathbf{u}_1 = 0 . \qquad (4)
> $$
>
> By Theorem §50.3 it is the second greatest eigenvalue, $\lambda = 3$. Solve $(A - 3I)\mathbf{x} = \mathbf{0}$:
>
> $$
> A - 3I = \begin{bmatrix} 0 & 2 & 1 \\ 2 & 0 & 1 \\ 1 & 1 & 1 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & 1/2 \\ 0 & 1 & 1/2 \\ 0 & 0 & 0 \end{bmatrix}
> \ \Rightarrow\ \begin{bmatrix} -1 \\ -1 \\ 2 \end{bmatrix}, \qquad
> \mathbf{u}_2 = \begin{bmatrix} 1/\sqrt6 \\ 1/\sqrt6 \\ -2/\sqrt6 \end{bmatrix}
> $$
>
> (normalized, with the sign flipped). $\mathbf{u}_2$ is automatically orthogonal to $\mathbf{u}_1$, since they belong to different eigenvalues ([[§48★ Diagonalization of Symmetric Matrices#^thm-48-1|Theorem §48.1]]). So the maximum subject to (4) is $3$, attained at $\mathbf{x} = \mathbf{u}_2$.
>
> *Lay: Examples 7.3.4 and 7.3.5*

^ex-50-4

> [!theorem] Theorem §50.4: All Eigenvalues as Constrained Maxima
> Let $A$ be a symmetric $n \times n$ matrix with an orthogonal diagonalization $A = PDP^{-1}$, where the entries on the diagonal of $D$ are arranged so that $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_n$ and where the columns of $P$ are corresponding unit eigenvectors $\mathbf{u}_1, \dots, \mathbf{u}_n$. Then for $k = 2, \dots, n$, the maximum value of $\mathbf{x}^T A \mathbf{x}$ subject to the constraints
>
> $$
> \mathbf{x}^T\mathbf{x} = 1, \qquad \mathbf{x}^T\mathbf{u}_1 = 0, \qquad \dots, \qquad \mathbf{x}^T\mathbf{u}_{k-1} = 0
> $$
>
> is the eigenvalue $\lambda_k$, and this maximum is attained at $\mathbf{x} = \mathbf{u}_k$.
>
> *Lay: Theorem 8 (7.3)*

^thm-50-4

*Lay omits the proof; the argument of Theorem §50.1 carries over directly, as follows.*

> [!proof]+ Proof
> Change variable by $\mathbf{x} = P\mathbf{y}$, so $\mathbf{y} = P^T\mathbf{x}$, whose $i$th entry is $y_i = \mathbf{u}_i^T\mathbf{x}$. As in the proof of Theorem §50.1, $\|\mathbf{y}\| = \|\mathbf{x}\|$ and $\mathbf{x}^TA\mathbf{x} = \lambda_1 y_1^2 + \cdots + \lambda_n y_n^2$. The constraints $\mathbf{x}^T\mathbf{u}_i = 0$ for $i < k$ say exactly that $y_1 = \cdots = y_{k-1} = 0$. For such a unit vector, using $\lambda_i \le \lambda_k$ for $i \ge k$,
>
> $$
> \mathbf{x}^T A \mathbf{x} = \lambda_k y_k^2 + \lambda_{k+1} y_{k+1}^2 + \cdots + \lambda_n y_n^2 \le \lambda_k (y_k^2 + \cdots + y_n^2) = \lambda_k \|\mathbf{y}\|^2 = \lambda_k .
> $$
>
> The vector $\mathbf{x} = \mathbf{u}_k = P\mathbf{e}_k$ is a unit vector orthogonal to $\mathbf{u}_1, \dots, \mathbf{u}_{k-1}$ (the columns of $P$ are orthonormal), so it satisfies the constraints, and $\mathbf{u}_k^T A \mathbf{u}_k = \lambda_k \mathbf{u}_k^T\mathbf{u}_k = \lambda_k$. So the constrained maximum is $\lambda_k$, attained at $\mathbf{u}_k$.

^pf-50-4

*Uses:* [[§50★ Constrained Optimization#^thm-50-1|§50.1]], [[§49★ Quadratic Forms#^thm-49-2|§49.2]]

> [!remark]- Connections
> - Theorem §50.4 depends on the eigenvectors $\mathbf{u}_1, \dots, \mathbf{u}_{k-1}$. The Courant–Fischer min-max theorem (not in Lay, nor yet in the vault) removes that dependence: $\lambda_k = \max_{\dim W = k}\ \min\{\mathbf{x}^TA\mathbf{x} : \mathbf{x} \in W,\ \|\mathbf{x}\| = 1\}$. The same "next singular value" mechanism gives the best rank-$k$ approximation of a matrix, [[§27 Consequences of Singular Value Decomposition#^ladr-7-92|LADR 7.92]].

> [!remark] Remark: Method — Constrained Extremes of a Quadratic Form
> To find the maximum and minimum of $Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$ subject to $\|\mathbf{x}\| = 1$:
> 1. Write the symmetric matrix $A$ of $Q$.
> 2. Find its eigenvalues $\lambda_1 \ge \cdots \ge \lambda_n$. The maximum is $\lambda_1$ and the minimum is $\lambda_n$ (Theorem §50.1).
> 3. To locate them, find unit eigenvectors $\mathbf{u}_1$ and $\mathbf{u}_n$. With the extra constraint $\mathbf{x} \perp \mathbf{u}_1, \dots, \mathbf{u}_{k-1}$, the maximum is $\lambda_k$ at $\mathbf{u}_k$ (Theorem §50.4).
> 4. If the constraint is not a unit sphere but an ellipse or ellipsoid $\sum (x_i/a_i)^2 = 1$, first rescale each variable, $x_i = a_i \tilde x_i$, to turn it into $\tilde{\mathbf{x}}^T\tilde{\mathbf{x}} = 1$ (Example §50.5), then return to the original variables at the end.

^rem-50-1

## An Application: Allocating Resources

> [!example] Example §50.5: Maximizing Utility on a Budget Ellipse
> During the next year, a county government plans to repair $x$ hundred miles of public roads and bridges and to improve $y$ hundred acres of parks and recreation areas. If it is more cost effective to work on both projects at once than on only one, then $x$ and $y$ might satisfy a constraint such as
>
> $$
> 4x^2 + 9y^2 \le 36 .
> $$
>
> Each point $(x, y)$ of this **feasible set** (in the first quadrant) is a possible public works schedule; the points on the constraint curve $4x^2 + 9y^2 = 36$ use the maximum resources available. To measure the value, or **utility**, the residents would assign to a schedule $(x, y)$, economists sometimes use a function such as $q(x, y) = xy$. The curves $q(x, y) = c$ are **indifference curves**: points on one of them are alternatives the residents would find equally valuable. Find the schedule that maximizes $q$.
>
> **Reduce to unit vectors.** Since $q(tx, ty) = t^2 q(x, y)$, scaling a schedule outward increases its utility, so the maximum over the feasible set lies on the curve $4x^2 + 9y^2 = 36$. That curve is not a set of unit vectors, but a change of variable fixes this. Write the constraint as
>
> $$
> \left(\frac{x}{3}\right)^2 + \left(\frac{y}{2}\right)^2 = 1
> $$
>
> and define $x_1 = x/3$, $x_2 = y/2$, that is, $x = 3x_1$, $y = 2x_2$. The constraint becomes $x_1^2 + x_2^2 = 1$, and the utility becomes $q(3x_1, 2x_2) = (3x_1)(2x_2) = 6x_1x_2$.
>
> **Apply Theorem §50.1.** With $\mathbf{x} = (x_1, x_2)$, the problem is to maximize $Q(\mathbf{x}) = 6x_1x_2 = \mathbf{x}^T A \mathbf{x}$ subject to $\mathbf{x}^T\mathbf{x} = 1$, where
>
> $$
> A = \begin{bmatrix} 0 & 3 \\ 3 & 0 \end{bmatrix}.
> $$
>
> The characteristic polynomial is $\lambda^2 - 9$, so the eigenvalues are $\pm 3$, with unit eigenvectors $(1/\sqrt2, 1/\sqrt2)$ for $\lambda = 3$ and $(-1/\sqrt2, 1/\sqrt2)$ for $\lambda = -3$. So the maximum of $Q(\mathbf{x}) = q(x_1, x_2)$ is $3$, attained at $x_1 = 1/\sqrt2$, $x_2 = 1/\sqrt2$.
>
> **Back to the original variables.** The optimal schedule is
>
> $$
> x = 3x_1 = \frac{3}{\sqrt2} \approx 2.1 \text{ hundred miles of roads and bridges}, \qquad y = 2x_2 = \sqrt2 \approx 1.4 \text{ hundred acres of parks},
> $$
>
> with utility $q = \frac{3}{\sqrt2} \cdot \sqrt2 = 3$. It is the point where the constraint curve and the indifference curve $q(x, y) = 3$ just meet. Points with a higher utility lie on indifference curves that do not touch the feasible set.
>
> *Lay: Example 7.3.6*

^ex-50-5

![[m235-50-1.svg]]
*Example §50.5. The feasible set (blue) is a quarter of the region inside the ellipse $4x^2 + 9y^2 = 36$. Utility increases across the indifference curves $xy = 2, 3, 4$; the best schedule is where the highest attainable one, $xy = 3$ (red), touches the constraint curve, at $(3/\sqrt2, \sqrt2) \approx (2.1, 1.4)$. That the two curves are tangent there is the Lagrange condition $\nabla(xy) \parallel \nabla(4x^2 + 9y^2)$.*
