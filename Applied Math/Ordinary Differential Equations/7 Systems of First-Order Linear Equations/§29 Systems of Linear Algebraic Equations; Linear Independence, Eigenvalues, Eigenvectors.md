---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 7
section: 29
bdp: "7.3"
aliases: ["BDP 7.3"]
tags: [ordinary-differential-equations, math331]
---
← [[§28 Matrices]] · ↑ [[· 7 Systems of First-Order Linear Equations]] · [[§30 Basic Theory of Systems of First-Order Linear Equations]] →

*Boyce–DiPrima, Section 7.3.*

This section collects the linear algebra that Chapter 7 runs on: when $\mathbf{A}\mathbf{x} = \mathbf{b}$ is solvable, when $n$ vectors are linearly independent (exactly when their determinant is nonzero), and how to find eigenvalues and eigenvectors. BDP states these facts as a summary and gives no proofs. Their home is [[Applied Linear Algebra]] (Lay), and each box below links there. What is new compared with Lay is the setting Chapter 7 needs: complex scalars and vectors, the inner product $(\mathbf{x}, \mathbf{y})$ with conjugation ([[§28 Matrices#^def-28-3|Definition §28.3]]), linear independence of vector *functions* on an interval, and the special behavior of Hermitian matrices.

## Systems of Linear Algebraic Equations

> [!definition] Definition §29.1: Homogeneous and Nonhomogeneous Systems
> A system of $n$ linear algebraic equations in $n$ variables,
>
> $$
> a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1, \quad \ldots, \quad a_{n1}x_1 + a_{n2}x_2 + \cdots + a_{nn}x_n = b_n, \qquad (1)
> $$
>
> is written in matrix form as
>
> $$
> \mathbf{A}\mathbf{x} = \mathbf{b}, \qquad (2)
> $$
>
> where the $n \times n$ matrix $\mathbf{A}$ and the vector $\mathbf{b}$ are given and $\mathbf{x}$ is to be determined. The system is **homogeneous** if $\mathbf{b} = \mathbf{0}$ and **nonhomogeneous** otherwise.
>
> *BDP: 7.3 (text)*

^def-29-1

> [!theorem] Theorem §29.1: Solvability of Ax = b
> **(a) $\mathbf{A}$ nonsingular** ($\det\mathbf{A} \ne 0$). For every $\mathbf{b}$, the system (2) has the unique solution
>
> $$
> \mathbf{x} = \mathbf{A}^{-1}\mathbf{b} . \qquad (3)
> $$
>
> In particular the homogeneous system $\mathbf{A}\mathbf{x} = \mathbf{0}$ has only the trivial solution $\mathbf{x} = \mathbf{0}$.
>
> **(b) $\mathbf{A}$ singular** ($\det\mathbf{A} = 0$). The homogeneous system
>
> $$
> \mathbf{A}\mathbf{x} = \mathbf{0} \qquad (4)
> $$
>
> has infinitely many nonzero solutions. The nonhomogeneous system (2) has no solution unless
>
> $$
> (\mathbf{b}, \mathbf{y}) = 0 \quad \text{for all vectors } \mathbf{y} \text{ with } \mathbf{A}^*\mathbf{y} = \mathbf{0}, \qquad (5)
> $$
>
> where $\mathbf{A}^*$ is the adjoint of $\mathbf{A}$ ([[§28 Matrices#^def-28-1|Definition §28.1]]). If (5) holds, (2) has infinitely many solutions, all of the form
>
> $$
> \mathbf{x} = \mathbf{x}^{(0)} + \boldsymbol{\xi}, \qquad (6)
> $$
>
> where $\mathbf{x}^{(0)}$ is one particular solution of (2) and $\boldsymbol{\xi}$ is the most general solution of (4).
>
> *BDP: 7.3 (text), Equations (3)–(6)*

^thm-29-1

*BDP omits the proofs (Problems 7.3.21–25 outline those of (5) and (6)). For real $\mathbf{A}$: part (a) and the first statement of (b) are the Invertible Matrix Theorem, [[§13 Characterizations of Invertible Matrices#^thm-13-1|235 Thm. §13.1]] with [[§21 Properties of Determinants#^thm-21-3|235 Thm. §21.3]]; the form (6) is [[§5 Solution Sets of Linear Systems#^thm-5-3|235 Thm. §5.3]]; and since $\mathbf{A}^* = \mathbf{A}^T$, condition (5) says $\mathbf{b} \in (\operatorname{Nul}\mathbf{A}^T)^\perp = \operatorname{Col}\mathbf{A}$, by [[§40 Inner Product, Length, and Orthogonality#^thm-40-6|235 Thm. §40.6]].*

The resemblance of (6) to the general solution of a nonhomogeneous linear differential equation (a particular solution plus the general solution of the homogeneous equation) is not an accident; it is the same linear-algebra fact.

> [!remark] Remark: Method — Solving by Row Reduction
> To solve a particular system, (3) and (5) are rarely the best tools. Instead:
> 1. Form the **augmented matrix** $(\mathbf{A} \mid \mathbf{b})$ by adjoining $\mathbf{b}$ to $\mathbf{A}$ as an extra column.
> 2. Use elementary row operations (they correspond to legitimate operations on the equations) to bring $\mathbf{A}$ to **upper triangular** form, with zeros below the main diagonal.
> 3. A row of the form $(0 \ \cdots \ 0 \mid c)$ with $c \ne 0$ means there is no solution. Otherwise, choose the variables without a pivot arbitrarily and solve for the others by back substitution, from the last equation up.
>
> This is the row reduction algorithm of [[§2 Row Reduction and Echelon Forms#^rem-2-1|235 §2]].

^rem-29-1

> [!example] Example §29.1: A Nonsingular and a Singular System
> **(a)** Solve $x_1 - 2x_2 + 3x_3 = 7$, $\ -x_1 + x_2 - 2x_3 = -5$, $\ 2x_1 - x_2 - x_3 = 4$.
>
> Add row 1 to row 2 and $-2$ times row 1 to row 3; multiply row 2 by $-1$; add $-3$ times row 2 to row 3; divide row 3 by $-4$:
>
> $$
> \left(\begin{array}{rrr|r} 1 & -2 & 3 & 7 \\ -1 & 1 & -2 & -5 \\ 2 & -1 & -1 & 4 \end{array}\right)
> \to \left(\begin{array}{rrr|r} 1 & -2 & 3 & 7 \\ 0 & -1 & 1 & 2 \\ 0 & 3 & -7 & -10 \end{array}\right)
> \to \left(\begin{array}{rrr|r} 1 & -2 & 3 & 7 \\ 0 & 1 & -1 & -2 \\ 0 & 0 & -4 & -4 \end{array}\right)
> \to \left(\begin{array}{rrr|r} 1 & -2 & 3 & 7 \\ 0 & 1 & -1 & -2 \\ 0 & 0 & 1 & 1 \end{array}\right) .
> $$
>
> Back substitution: $x_3 = 1$, $x_2 = -2 + x_3 = -1$, $x_1 = 7 + 2x_2 - 3x_3 = 2$, so $\mathbf{x} = (2, -1, 1)^T$. The solution is unique, so the coefficient matrix is nonsingular.
>
> **(b)** Discuss $x_1 - 2x_2 + 3x_3 = b_1$, $\ -x_1 + x_2 - 2x_3 = b_2$, $\ 2x_1 - x_2 + 3x_3 = b_3$ (only the coefficient of $x_3$ in the third equation has changed).
>
> The same three steps give
>
> $$
> \left(\begin{array}{rrr|c} 1 & -2 & 3 & b_1 \\ 0 & 1 & -1 & -b_1 - b_2 \\ 0 & 0 & 0 & b_1 + 3b_2 + b_3 \end{array}\right) .
> $$
>
> The third row reads $0 = b_1 + 3b_2 + b_3$, so there is no solution unless
>
> $$
> b_1 + 3b_2 + b_3 = 0 . \qquad (14)
> $$
>
> (This is condition (5) for this system: $\mathbf{A}^T\mathbf{y} = \mathbf{0}$ has the solutions $\mathbf{y} = c\,(1, 3, 1)^T$.) Take $b_1 = 2$, $b_2 = 1$, $b_3 = -5$, which satisfy (14). The first two rows give $x_1 - 2x_2 + 3x_3 = 2$, $x_2 - x_3 = -3$. Let $x_3 = \alpha$ be arbitrary; then $x_2 = \alpha - 3$ and $x_1 = 2(\alpha - 3) - 3\alpha + 2 = -\alpha - 4$:
>
> $$
> \mathbf{x} = \begin{pmatrix} -\alpha - 4 \\ \alpha - 3 \\ \alpha \end{pmatrix} = \alpha\begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix} + \begin{pmatrix} -4 \\ -3 \\ 0 \end{pmatrix} .
> $$
>
> This is the form (6): $(-4, -3, 0)^T$ is a particular solution of the nonhomogeneous system, and $\alpha(-1, 1, 1)^T$ is the general solution of the homogeneous one.
>
> *BDP: Examples 7.3.1 and 7.3.2*

^ex-29-1

## Linear Dependence and Independence

> [!definition] Definition §29.2: Linear Dependence and Independence
> Vectors $\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(k)}$ are **linearly dependent** if there are real or complex numbers $c_1, \ldots, c_k$, at least one of which is nonzero, such that
>
> $$
> c_1\mathbf{x}^{(1)} + \cdots + c_k\mathbf{x}^{(k)} = \mathbf{0} . \qquad (17)
> $$
>
> That is, there is a linear relation among them. If (17) holds only for $c_1 = c_2 = \cdots = c_k = 0$, the vectors are **linearly independent**.
>
> *BDP: 7.3 (text)*

^def-29-2

> [!remark]- Connections
> - Lay's definition for real scalars, and the matrix test (the columns of $A$ are independent iff $A\mathbf{x} = \mathbf{0}$ has only the trivial solution): [[§7 Linear Independence#^def-7-1|235 Def. §7.1]], [[§7 Linear Independence#^prop-7-1|235 Prop. §7.1]]. In an abstract vector space over $\mathbb{R}$ or $\mathbb{C}$: [[§4 Span and Linear Independence#^ladr-2-15|LADR 2.15]].

> [!theorem] Theorem §29.2: Independence and the Determinant
> **(a)** Let $\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}$ be $n$ vectors with $n$ components each, and let $\mathbf{X}$ be the $n \times n$ matrix whose $j$th column is $\mathbf{x}^{(j)}$, so $\mathbf{X} = (x_{ij})$ with $x_{ij} = x_i^{(j)}$. Then $\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}$ are linearly independent if and only if $\det\mathbf{X} \ne 0$. The same holds for the rows of a square matrix.
>
> **(b)** If $\mathbf{C} = \mathbf{A}\mathbf{B}$, then $\det\mathbf{C} = (\det\mathbf{A})(\det\mathbf{B})$. Hence if the columns (or rows) of both $\mathbf{A}$ and $\mathbf{B}$ are linearly independent, so are those of $\mathbf{C}$.
>
> *BDP: 7.3 (text), Equation (18)*

^thm-29-2

> [!proof]+ Proof
> **(a)** Write $\mathbf{c} = (c_1, \ldots, c_n)^T$. The $i$th component of $c_1\mathbf{x}^{(1)} + \cdots + c_n\mathbf{x}^{(n)}$ is $x_i^{(1)}c_1 + \cdots + x_i^{(n)}c_n = x_{i1}c_1 + \cdots + x_{in}c_n$, the $i$th component of $\mathbf{X}\mathbf{c}$. So (17) is the homogeneous system
>
> $$
> \mathbf{X}\mathbf{c} = \mathbf{0} . \qquad (18)
> $$
>
> If $\det\mathbf{X} \ne 0$, its only solution is $\mathbf{c} = \mathbf{0}$ (Theorem §29.1(a)), so the vectors are independent. If $\det\mathbf{X} = 0$, it has nonzero solutions (Theorem §29.1(b)), so they are dependent. For rows, apply this to $\mathbf{X}^T$, which has the same determinant ([[§21 Properties of Determinants#^thm-21-6|235 Thm. §21.6]]).
>
> **(b)** The product formula is cited, not proved, in BDP; see [[§21 Properties of Determinants#^thm-21-9|235 Thm. §21.9]]. Given it, independent columns of $\mathbf{A}$ and $\mathbf{B}$ mean $\det\mathbf{A} \ne 0 \ne \det\mathbf{B}$ by (a), so $\det\mathbf{C} \ne 0$ and the columns of $\mathbf{C}$ are independent by (a).

^pf-29-2

*Uses:* [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-1|§29.1]], [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^def-29-2|Def. §29.2]], [[§21 Properties of Determinants#^thm-21-9|235 Thm. §21.9]] (multiplicative property), [[§21 Properties of Determinants#^thm-21-6|235 Thm. §21.6]] (transpose)

> [!example] Example §29.2: Testing Three Vectors
> Are $\mathbf{x}^{(1)} = (1, 2, -1)^T$, $\mathbf{x}^{(2)} = (2, 1, 3)^T$, $\mathbf{x}^{(3)} = (-4, 1, -11)^T$ linearly independent? If not, find a linear relation.
>
> **By row reduction.** Solve $c_1\mathbf{x}^{(1)} + c_2\mathbf{x}^{(2)} + c_3\mathbf{x}^{(3)} = \mathbf{0}$. Add $-2$ times row 1 to row 2 and row 1 to row 3; then divide row 2 by $-3$ and add $-5$ times it to row 3:
>
> $$
> \left(\begin{array}{rrr|r} 1 & 2 & -4 & 0 \\ 2 & 1 & 1 & 0 \\ -1 & 3 & -11 & 0 \end{array}\right)
> \to \left(\begin{array}{rrr|r} 1 & 2 & -4 & 0 \\ 0 & -3 & 9 & 0 \\ 0 & 5 & -15 & 0 \end{array}\right)
> \to \left(\begin{array}{rrr|r} 1 & 2 & -4 & 0 \\ 0 & 1 & -3 & 0 \\ 0 & 0 & 0 & 0 \end{array}\right) .
> $$
>
> So $c_2 = 3c_3$ and $c_1 = 4c_3 - 2c_2 = -2c_3$ with $c_3$ free: there are nontrivial solutions, and the vectors are dependent. With $c_3 = -1$: $c_1 = 2$, $c_2 = -3$, and
>
> $$
> 2\mathbf{x}^{(1)} - 3\mathbf{x}^{(2)} - \mathbf{x}^{(3)} = \mathbf{0} .
> $$
>
> (Check, first components: $2 - 6 + 4 = 0$.)
>
> **By the determinant.** Expanding along the first row,
>
> $$
> \det\mathbf{X} = \begin{vmatrix} 1 & 2 & -4 \\ 2 & 1 & 1 \\ -1 & 3 & -11 \end{vmatrix}
> = 1\begin{vmatrix} 1 & 1 \\ 3 & -11 \end{vmatrix} - 2\begin{vmatrix} 2 & 1 \\ -1 & -11 \end{vmatrix} + (-4)\begin{vmatrix} 2 & 1 \\ -1 & 3 \end{vmatrix}
> = -14 - 2(-21) - 4(7) = 0 ,
> $$
>
> which confirms dependence (Theorem §29.2) but does not produce the relation. In the same way, the coefficient columns of Example §29.1(a) are independent and those of Example §29.1(b) are dependent.
>
> *BDP: Example 7.3.3*

^ex-29-2

> [!definition] Definition §29.3: Linear Independence of Vector Functions
> Vector functions $\mathbf{x}^{(1)}(t), \ldots, \mathbf{x}^{(k)}(t)$ defined on an interval $\alpha < t < \beta$ are **linearly dependent on** $\alpha < t < \beta$ if there are constants $c_1, \ldots, c_k$, not all zero, such that
>
> $$
> c_1\mathbf{x}^{(1)}(t) + \cdots + c_k\mathbf{x}^{(k)}(t) = \mathbf{0} \quad \text{for all } t \text{ in the interval.}
> $$
>
> Otherwise they are **linearly independent** on the interval.
>
> *BDP: 7.3 (text)*

^def-29-3

> [!remark] Remark: On an Interval versus at Each Point
> Functions that are dependent on an interval are dependent at each point of it (use the same constants). The converse fails, because the constants may change from point to point. BDP's Problem 13: $\mathbf{x}^{(1)}(t) = (e^t, te^t)^T$ and $\mathbf{x}^{(2)}(t) = (1, t)^T$ satisfy $\mathbf{x}^{(1)}(t) = e^t\,\mathbf{x}^{(2)}(t)$, so they are dependent at every $t$. But on $0 \le t \le 1$ they are independent: $c_1\mathbf{x}^{(1)} + c_2\mathbf{x}^{(2)} \equiv \mathbf{0}$ gives, in the first component, $c_1e^t + c_2 = 0$ for all $t$; differentiating, $c_1e^t = 0$, so $c_1 = 0$ and then $c_2 = 0$. For *solutions* of a linear system $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$ this cannot happen: there, dependence at one point forces dependence on the whole interval ([[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-3|Theorem §30.3]]).

^rem-29-2

## Eigenvalues and Eigenvectors

> [!definition] Definition §29.4: Eigenvalue, Eigenvector, Characteristic Equation
> Let $\mathbf{A}$ be an $n \times n$ matrix. A number $\lambda$ (real or complex) is an **eigenvalue** of $\mathbf{A}$ if the equation
>
> $$
> \mathbf{A}\mathbf{x} = \lambda\mathbf{x}, \qquad\text{equivalently}\qquad (\mathbf{A} - \lambda\mathbf{I})\mathbf{x} = \mathbf{0}, \qquad (25), (26)
> $$
>
> has a nonzero solution $\mathbf{x}$; such nonzero solutions are the **eigenvectors** corresponding to $\lambda$. By Theorem §29.1, (26) has nonzero solutions if and only if
>
> $$
> \det(\mathbf{A} - \lambda\mathbf{I}) = 0 . \qquad (27)
> $$
>
> Equation (27), a polynomial equation of degree $n$ in $\lambda$, is the **characteristic equation** of $\mathbf{A}$. So the eigenvalues are its roots.
>
> *BDP: 7.3 (text), Equations (25)–(27)*

^def-29-4

> [!remark]- Connections
> - Lay's treatment of real eigenvalues, with the characteristic equation and a proof that it has degree $n$: [[§32 Eigenvectors and Eigenvalues#^def-32-1|235 Def. §32.1]], [[§33 The Characteristic Equation#^thm-33-4|235 Thm. §33.4]], [[§33 The Characteristic Equation#^thm-33-5|235 Thm. §33.5]]; complex eigenvalues and eigenvectors: [[§36 Complex Eigenvalues#^def-36-1|235 Def. §36.1]].
> - Rigorous treatment for operators: [[§14 Invariant Subspaces#^ladr-5-5|LADR 5.5]]; that the eigenvalues are the zeros of $\det(z\mathbf{I} - \mathbf{A})$: [[§34 Determinants#^ladr-9-62|LADR 9.62]].

> [!example] Example §29.3: Eigenvalues and Eigenvectors of a 2 × 2 Matrix
> Find the eigenvalues and eigenvectors of $\mathbf{A} = \begin{pmatrix} 3 & -1 \\ 4 & -2 \end{pmatrix}$.
>
> **Eigenvalues.**
>
> $$
> \det(\mathbf{A} - \lambda\mathbf{I}) = \begin{vmatrix} 3 - \lambda & -1 \\ 4 & -2 - \lambda \end{vmatrix} = (3 - \lambda)(-2 - \lambda) + 4 = \lambda^2 - \lambda - 2 = (\lambda - 2)(\lambda + 1) ,
> $$
>
> so $\lambda_1 = 2$ and $\lambda_2 = -1$.
>
> **Eigenvectors.** For $\lambda = 2$, $(\mathbf{A} - 2\mathbf{I})\mathbf{x} = \mathbf{0}$ is $\begin{pmatrix} 1 & -1 \\ 4 & -4 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \mathbf{0}$; both rows say $x_1 - x_2 = 0$. So $\mathbf{x}^{(1)} = c\,(1, 1)^T$, $c \ne 0$, and we take $\mathbf{x}^{(1)} = (1, 1)^T$. For $\lambda = -1$, $\begin{pmatrix} 4 & -1 \\ 4 & -1 \end{pmatrix}\mathbf{x} = \mathbf{0}$ gives $4x_1 - x_2 = 0$, so $\mathbf{x}^{(2)} = (1, 4)^T$ (or any nonzero multiple).
>
> Check: $\mathbf{A}(1, 4)^T = (3 - 4, 4 - 8)^T = (-1, -4)^T = -1 \cdot (1, 4)^T$.
>
> *BDP: Example 7.3.4*

^ex-29-3

> [!definition] Definition §29.5: Normalized Eigenvector; Algebraic and Geometric Multiplicity
> - Eigenvectors are determined only up to a nonzero multiplicative constant. Fixing this constant in some way **normalizes** the eigenvector: for instance by making its components small integers, or by making its length $\|\mathbf{x}\| = (\mathbf{x}, \mathbf{x})^{1/2}$ equal to $1$.
> - Counting repeated roots, an $n \times n$ matrix has $n$ eigenvalues $\lambda_1, \ldots, \lambda_n$. An eigenvalue that appears $m$ times as a root of (27) has **algebraic multiplicity** $m$. If it has $q$ linearly independent eigenvectors (and no more), it has **geometric multiplicity** $q$. An eigenvalue of algebraic multiplicity $1$ is **simple**.
>
> *BDP: 7.3 (text)*

^def-29-5

> [!theorem] Theorem §29.3: Geometric Multiplicity Is at Most Algebraic Multiplicity
> For every eigenvalue,
>
> $$
> 1 \le q \le m . \qquad (36)
> $$
>
> Examples show that $q$ can be any integer in this range. In particular a simple eigenvalue has geometric multiplicity $1$.
>
> *BDP: 7.3 (text), Equation (36)*

^thm-29-3

*BDP omits the proof ("it is possible to show"); it is [[§34 Diagonalization#^thm-34-3|235 Thm. §34.3]](a), proved there by extending a basis of the eigenspace to a basis of $\mathbb{R}^n$. The case $q < m$ is the source of the complications in [[§34★ Repeated Eigenvalues|§34★]] (Section 7.8).*

> [!theorem] Theorem §29.4: Eigenvectors of Distinct Eigenvalues Are Independent
> If $\lambda_1, \ldots, \lambda_k$ are distinct eigenvalues of $\mathbf{A}$ with eigenvectors $\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(k)}$, then $\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(k)}$ are linearly independent. Consequently, if every eigenvalue of an $n \times n$ matrix is simple, the $n$ eigenvectors, one for each eigenvalue, are linearly independent.
>
> *BDP: 7.3 (text) and Problem 7.3.29*

^thm-29-4

> [!proof]+ Proof
> *BDP outlines the case $k = 2$ in Problem 29; the general case is the same argument by induction.*
>
> **$k = 2$.** Suppose $c_1\mathbf{x}^{(1)} + c_2\mathbf{x}^{(2)} = \mathbf{0}$. Multiplying by $\mathbf{A}$ gives $c_1\lambda_1\mathbf{x}^{(1)} + c_2\lambda_2\mathbf{x}^{(2)} = \mathbf{0}$. Subtract $\lambda_2$ times the first equation: $c_1(\lambda_1 - \lambda_2)\mathbf{x}^{(1)} = \mathbf{0}$. Since $\lambda_1 \ne \lambda_2$ and $\mathbf{x}^{(1)} \ne \mathbf{0}$, $c_1 = 0$. Then $c_2\mathbf{x}^{(2)} = \mathbf{0}$ gives $c_2 = 0$.
>
> **Induction.** Assume the statement for $k - 1$ eigenvectors and let $c_1\mathbf{x}^{(1)} + \cdots + c_k\mathbf{x}^{(k)} = \mathbf{0}$. Multiply by $\mathbf{A}$ and subtract $\lambda_k$ times the original relation:
>
> $$
> c_1(\lambda_1 - \lambda_k)\mathbf{x}^{(1)} + \cdots + c_{k-1}(\lambda_{k-1} - \lambda_k)\mathbf{x}^{(k-1)} = \mathbf{0} .
> $$
>
> By the induction hypothesis every coefficient $c_j(\lambda_j - \lambda_k)$ is $0$, and $\lambda_j \ne \lambda_k$, so $c_1 = \cdots = c_{k-1} = 0$. Then $c_k\mathbf{x}^{(k)} = \mathbf{0}$ gives $c_k = 0$.
>
> If all $n$ eigenvalues are simple, they are $n$ distinct numbers, and the first statement applies with $k = n$.

^pf-29-4

*Uses:* [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^def-29-2|Def. §29.2]], [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^def-29-4|Def. §29.4]], [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^def-29-5|Def. §29.5]]

With a repeated eigenvalue there may be fewer than $n$ independent eigenvectors, because $q < m$ is possible. The next example has a double eigenvalue with $q = m = 2$.

> [!example] Example §29.4: A Double Eigenvalue with Two Eigenvectors
> Find the eigenvalues and eigenvectors of $\mathbf{A} = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}$.
>
> **Eigenvalues.** Expanding along the first row,
>
> $$
> \det(\mathbf{A} - \lambda\mathbf{I}) = \begin{vmatrix} -\lambda & 1 & 1 \\ 1 & -\lambda & 1 \\ 1 & 1 & -\lambda \end{vmatrix} = -\lambda(\lambda^2 - 1) - (-\lambda - 1) + (1 + \lambda) = -\lambda^3 + 3\lambda + 2 = -(\lambda - 2)(\lambda + 1)^2 .
> $$
>
> So $\lambda_1 = 2$ is simple and $\lambda_2 = \lambda_3 = -1$ is a double eigenvalue ($m = 2$).
>
> **$\lambda = 2$.** Row reducing $\mathbf{A} - 2\mathbf{I}$ gives $\begin{pmatrix} 2 & -1 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix}$, so $x_2 = x_3$, $x_1 = x_3$, and $\mathbf{x}^{(1)} = (1, 1, 1)^T$.
>
> **$\lambda = -1$.** Every row of $\mathbf{A} + \mathbf{I}$ is $(1, 1, 1)$, so the system reduces to the single equation $x_1 + x_2 + x_3 = 0$. Two variables are free: with $x_1 = c_1$, $x_2 = c_2$,
>
> $$
> \mathbf{x} = \begin{pmatrix} c_1 \\ c_2 \\ -c_1 - c_2 \end{pmatrix} = c_1\begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} + c_2\begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} .
> $$
>
> The choices $(c_1, c_2) = (1, 0)$ and $(0, 1)$ give two independent eigenvectors $\mathbf{x}^{(2)} = (1, 0, -1)^T$ and $\mathbf{x}^{(3)} = (0, 1, -1)^T$. So here $q = m = 2$.
>
> **An orthogonal choice.** $\mathbf{A}$ is real and symmetric, and $\mathbf{x}^{(1)}$ is orthogonal to both $\mathbf{x}^{(2)}$ and $\mathbf{x}^{(3)}$, as Theorem §29.5 below predicts. But $(\mathbf{x}^{(2)}, \mathbf{x}^{(3)}) = 1 \ne 0$. Choosing $(c_1, c_2) = (1, -2)$ instead gives $\mathbf{x}^{(3)} = (1, -2, 1)^T$, and then $\mathbf{x}^{(1)}, \mathbf{x}^{(2)}, \mathbf{x}^{(3)}$ are mutually orthogonal.
>
> *BDP: Example 7.3.5*

^ex-29-4

> [!definition] Definition §29.6: Self-Adjoint (Hermitian) Matrix
> A matrix $\mathbf{A}$ is **self-adjoint**, or **Hermitian**, if $\mathbf{A}^* = \mathbf{A}$, that is, $\bar a_{ji} = a_{ij}$ for all $i, j$. The real Hermitian matrices are the real **symmetric** matrices, $\mathbf{A}^T = \mathbf{A}$.
>
> *BDP: 7.3 (text)*

^def-29-6

> [!theorem] Theorem §29.5: Eigenvalues and Eigenvectors of a Hermitian Matrix
> Let $\mathbf{A}$ be Hermitian. Then:
> 1. All eigenvalues of $\mathbf{A}$ are real.
> 2. There is always a full set of $n$ linearly independent eigenvectors, whatever the algebraic multiplicities.
> 3. If $\mathbf{x}^{(1)}$ and $\mathbf{x}^{(2)}$ are eigenvectors for different eigenvalues, then $(\mathbf{x}^{(1)}, \mathbf{x}^{(2)}) = 0$. So if all eigenvalues are simple, the eigenvectors form an orthogonal set.
> 4. For an eigenvalue of algebraic multiplicity $m$, one can choose $m$ mutually orthogonal eigenvectors. So the full set of $n$ eigenvectors can be chosen orthogonal as well as linearly independent.
>
> *BDP: 7.3 (text)*

^thm-29-5

> [!proof]- Proof
> *BDP outlines 1 and 3 in Problems 7.3.27–28 and omits 2 and 4; see the Connections below.* Recall $(\mathbf{x}, \mathbf{y}) = \sum_i x_i\bar y_i$ ([[§28 Matrices#^def-28-3|Definition §28.3]]), which is linear in $\mathbf{x}$, satisfies $(\mathbf{x}, c\mathbf{y}) = \bar c\,(\mathbf{x}, \mathbf{y})$, and has $(\mathbf{x}, \mathbf{x}) = \sum_i |x_i|^2 > 0$ for $\mathbf{x} \ne \mathbf{0}$.
>
> **The adjoint identity** (Problem 21). For any $\mathbf{A}$,
>
> $$
> (\mathbf{A}\mathbf{x}, \mathbf{y}) = \sum_i \Big(\sum_j a_{ij}x_j\Big)\bar y_i = \sum_j x_j\,\overline{\sum_i \bar a_{ij}\,y_i} = (\mathbf{x}, \mathbf{A}^*\mathbf{y}),
> $$
>
> since the $j$th entry of $\mathbf{A}^*\mathbf{y}$ is $\sum_i \bar a_{ij}y_i$. If $\mathbf{A}$ is Hermitian, $(\mathbf{A}\mathbf{x}, \mathbf{y}) = (\mathbf{x}, \mathbf{A}\mathbf{y})$.
>
> **1.** Let $\mathbf{A}\mathbf{x} = \lambda\mathbf{x}$ with $\mathbf{x} \ne \mathbf{0}$. Then
>
> $$
> \lambda(\mathbf{x}, \mathbf{x}) = (\mathbf{A}\mathbf{x}, \mathbf{x}) = (\mathbf{x}, \mathbf{A}\mathbf{x}) = (\mathbf{x}, \lambda\mathbf{x}) = \bar\lambda(\mathbf{x}, \mathbf{x}) .
> $$
>
> Since $(\mathbf{x}, \mathbf{x}) > 0$, $\lambda = \bar\lambda$: $\lambda$ is real.
>
> **3.** Let $\mathbf{A}\mathbf{x}^{(1)} = \lambda_1\mathbf{x}^{(1)}$, $\mathbf{A}\mathbf{x}^{(2)} = \lambda_2\mathbf{x}^{(2)}$, $\lambda_1 \ne \lambda_2$. By 1, $\bar\lambda_2 = \lambda_2$, so
>
> $$
> \lambda_1(\mathbf{x}^{(1)}, \mathbf{x}^{(2)}) = (\mathbf{A}\mathbf{x}^{(1)}, \mathbf{x}^{(2)}) = (\mathbf{x}^{(1)}, \mathbf{A}\mathbf{x}^{(2)}) = \bar\lambda_2(\mathbf{x}^{(1)}, \mathbf{x}^{(2)}) = \lambda_2(\mathbf{x}^{(1)}, \mathbf{x}^{(2)}) .
> $$
>
> Hence $(\lambda_1 - \lambda_2)(\mathbf{x}^{(1)}, \mathbf{x}^{(2)}) = 0$, and $(\mathbf{x}^{(1)}, \mathbf{x}^{(2)}) = 0$.
>
> **2 and 4** together say that $\mathbf{C}^n$ has an orthonormal basis of eigenvectors of $\mathbf{A}$. This is the spectral theorem, which BDP does not prove.

^pf-29-5

*Uses:* [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^def-29-4|Def. §29.4]], [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^def-29-6|Def. §29.6]], [[§28 Matrices#^def-28-1|Def. §28.1]] (adjoint), [[§28 Matrices#^def-28-3|Def. §28.3]] (inner product)

> [!remark]- Connections
> - Rigorous treatment: real eigenvalues [[§22 Self-Adjoint and Normal Operators#^ladr-7-12|LADR 7.12]], orthogonal eigenvectors [[§22 Self-Adjoint and Normal Operators#^ladr-7-22|LADR 7.22]], and statements 2 and 4, the spectral theorems [[§23 Spectral Theorem#^ladr-7-29|LADR 7.29]] (real symmetric) and [[§23 Spectral Theorem#^ladr-7-31|LADR 7.31]] (complex; Hermitian matrices are normal).
> - For real symmetric matrices, with Lay's proof via the Schur factorization: [[§48★ Diagonalization of Symmetric Matrices#^thm-48-3|235 Thm. §48.3]].

These properties are why real symmetric coefficient matrices cause no trouble in §31 ([[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-2|Theorem §31.2]](b)): even with repeated eigenvalues there are always $n$ independent eigenvectors ([[§31 Homogeneous Linear Systems with Constant Coefficients#^ex-31-3|Example §31.3]] uses the matrix of Example §29.4).
