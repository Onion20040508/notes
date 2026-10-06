---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 3
section: 27
lay: "3.3"
aliases: ["Lay 3.3"]
tags: [applied-linear-algebra, math235]
---
← [[§26 Transposes, Products, and Linearity of Determinants]] · ↑ [[· 3 Determinants]] · [[§28 Determinants as Area or Volume]] →

*Lay, Section 3.3 · MATH 235 lectures L11, L12, L13.*

This section turns the theory of [[§24 Introduction to Determinants|§24]]–[[§25 Properties of Determinants|§25]] into formulas and geometry. Cramer's rule writes the solution of an invertible system $A\mathbf{x} = \mathbf{b}$ as quotients of determinants, and applied to the columns of the identity it gives an explicit inverse, $A^{-1} = \frac{1}{\det A}\operatorname{adj} A$. Both are mainly theoretical tools: they show how solutions depend on the data. Geometrically, $|\det A|$ is the area (in $\mathbb{R}^2$) or volume (in $\mathbb{R}^3$) of the parallelogram or parallelepiped spanned by the columns of $A$, and the linear map $\mathbf{x} \mapsto A\mathbf{x}$ multiplies every area or volume by $|\det A|$. In multivariable calculus this factor becomes the Jacobian.

## Cramer's Rule

> [!definition] Definition §27.1: The Matrix A_i(b)
> For an $n \times n$ matrix $A = [\mathbf{a}_1 \ \cdots \ \mathbf{a}_n]$ and $\mathbf{b} \in \mathbb{R}^n$, $A_i(\mathbf{b})$ is the matrix obtained from $A$ by replacing column $i$ by $\mathbf{b}$:
>
> $$
> A_i(\mathbf{b}) = [\mathbf{a}_1 \ \cdots \ \mathbf{a}_{i-1} \ \ \mathbf{b} \ \ \mathbf{a}_{i+1} \ \cdots \ \mathbf{a}_n] .
> $$
>
> *Lay: 3.3 (text)*

^def-27-1

> [!theorem] Theorem §27.1: Cramer's Rule
> Let $A$ be an invertible $n \times n$ matrix. For any $\mathbf{b}$ in $\mathbb{R}^n$, the unique solution $\mathbf{x}$ of $A\mathbf{x} = \mathbf{b}$ has entries given by
>
> $$
> x_i = \frac{\det A_i(\mathbf{b})}{\det A}, \qquad i = 1, 2, \ldots, n . \qquad (1)
> $$
>
> *Lay: Theorem 7 (3.3)*

^thm-27-1

> [!proof]+ Proof
> Since $A$ is invertible, $\det A \ne 0$ ([[§25 Properties of Determinants#^thm-25-3|Theorem §25.3]]) and the solution $\mathbf{x} = A^{-1}\mathbf{b}$ is unique. Let $\mathbf{e}_1, \ldots, \mathbf{e}_n$ be the columns of $I$. If $A\mathbf{x} = \mathbf{b}$, the definition of matrix multiplication (column by column) gives
>
> $$
> A \cdot I_i(\mathbf{x}) = A\,[\mathbf{e}_1 \ \cdots \ \mathbf{x} \ \cdots \ \mathbf{e}_n] = [A\mathbf{e}_1 \ \cdots \ A\mathbf{x} \ \cdots \ A\mathbf{e}_n] = [\mathbf{a}_1 \ \cdots \ \mathbf{b} \ \cdots \ \mathbf{a}_n] = A_i(\mathbf{b}) .
> $$
>
> By the multiplicative property ([[§26 Transposes, Products, and Linearity of Determinants#^thm-26-4|Theorem §26.4]]),
>
> $$
> (\det A)(\det I_i(\mathbf{x})) = \det A_i(\mathbf{b}) .
> $$
>
> Row $i$ of $I_i(\mathbf{x})$ is $(0, \ldots, 0, x_i, 0, \ldots, 0)$ with $x_i$ in position $i$, and deleting row $i$ and column $i$ leaves $I_{n-1}$. So the cofactor expansion across row $i$ gives $\det I_i(\mathbf{x}) = x_i \det I_{n-1} = x_i$. Hence $(\det A)\,x_i = \det A_i(\mathbf{b})$, which is (1) because $\det A \ne 0$.

^pf-27-1

*Uses:* [[§27 Cramer’s Rule, Volume, and Linear Transformations#^def-27-1|Def. §27.1]], [[§25 Properties of Determinants#^thm-25-3|§25.3]], [[§26 Transposes, Products, and Linearity of Determinants#^thm-26-4|§26.4]], [[§24 Introduction to Determinants#^thm-24-1|§24.1]], [[§12 Matrix Operations#^prop-12-3|§12.3]] (columns of a product)

> [!remark]- Connections
> - See also: Cramer's rule for $n = 2$ fits a combination $c_1y_1 + c_2y_2$ of two solutions of $y'' + py' + qy = 0$ to initial conditions, with the Wronskian as the common denominator, [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-3|331 Thm. §18.3]] (formula (11) of its proof).

> [!example] Example §27.1: Cramer's Rule, With and Without a Parameter
> **(a)** Solve $\begin{cases} x_1 + 2x_2 = 5 \\ 3x_1 + 4x_2 = 7 \end{cases}$. Here
>
> $$
> A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad A_1(\mathbf{b}) = \begin{bmatrix} 5 & 2 \\ 7 & 4 \end{bmatrix}, \quad A_2(\mathbf{b}) = \begin{bmatrix} 1 & 5 \\ 3 & 7 \end{bmatrix}, \quad \det A = 4 - 6 = -2 \ne 0 ,
> $$
>
> so Cramer's rule applies:
>
> $$
> x_1 = \frac{20 - 14}{-2} = \frac{6}{-2} = -3, \qquad x_2 = \frac{7 - 15}{-2} = \frac{-8}{-2} = 4 .
> $$
>
> Check: $-3 + 2 \cdot 4 = 5$ and $3(-3) + 4 \cdot 4 = 7$.
>
> **(b)** Systems whose coefficients involve a parameter $s$ arise when [[§26 Definition of the Laplace Transform#^def-26-4|Laplace transforms]] turn linear differential equations (electrical engineering, control theory) into algebraic equations. For which $s$ does
>
> $$
> \begin{cases} 3s\,x_1 - 2x_2 = 4 \\ -6x_1 + s\,x_2 = 1 \end{cases}
> $$
>
> have a unique solution, and what is it? Here
>
> $$
> A = \begin{bmatrix} 3s & -2 \\ -6 & s \end{bmatrix}, \quad A_1(\mathbf{b}) = \begin{bmatrix} 4 & -2 \\ 1 & s \end{bmatrix}, \quad A_2(\mathbf{b}) = \begin{bmatrix} 3s & 4 \\ -6 & 1 \end{bmatrix}, \quad \det A = 3s^2 - 12 = 3(s + 2)(s - 2) .
> $$
>
> So the solution is unique exactly when $s \ne \pm 2$, and then
>
> $$
> x_1 = \frac{\det A_1(\mathbf{b})}{\det A} = \frac{4s + 2}{3(s + 2)(s - 2)}, \qquad x_2 = \frac{\det A_2(\mathbf{b})}{\det A} = \frac{3s + 24}{3(s + 2)(s - 2)} = \frac{s + 8}{(s + 2)(s - 2)} .
> $$
>
> For $s = \pm 2$ Cramer's rule says nothing, and row reduction decides: for $s = 2$ the equations are $6x_1 - 2x_2 = 4$ and $-6x_1 + 2x_2 = 1$, whose sum is $0 = 5$; for $s = -2$ they are $-6x_1 - 2x_2 = 4$ and $-6x_1 - 2x_2 = 1$. Both systems are inconsistent.
>
> *Lay: Example 3.3.2*
> *Source: 235 lecture L13*

^ex-27-1

> [!example] Example §27.2: Lagrange Interpolation
> **Problem.** A quadratic $f(x) = Ax^2 + Bx + C$ has $f(1) = 3$, $f(2) = -1$, $f(3) = 2$. Find $f(4)$.
>
> **Lagrange polynomials.** For distinct numbers $a, b, c$, look for the quadratic $L_{a,b,c}(x) = Ax^2 + Bx + C$ with $L_{a,b,c}(a) = 1$, $L_{a,b,c}(b) = 0$, $L_{a,b,c}(c) = 0$. With the unknowns ordered $C, B, A$ the conditions are
>
> $$
> V \begin{bmatrix} C \\ B \\ A \end{bmatrix} = \mathbf{e}_1, \qquad V = \begin{bmatrix} 1 & a & a^2 \\ 1 & b & b^2 \\ 1 & c & c^2 \end{bmatrix} = \Delta(a, b, c)^T ,
> $$
>
> the transpose of the Vandermonde matrix of [[§26 Transposes, Products, and Linearity of Determinants#^prop-26-3|Proposition §26.3]]. So $\det V = (b - a)(c - a)(c - b) \ne 0$, and Cramer's rule gives $C = \det V_1(\mathbf{e}_1)/\det V$, $B = \det V_2(\mathbf{e}_1)/\det V$, $A = \det V_3(\mathbf{e}_1)/\det V$. Expanding $V_k(\mathbf{e}_1)$ down its column $k$, which is $\mathbf{e}_1$, shows $\det V_k(\mathbf{e}_1) = C_{1k}$, the $(1,k)$-cofactor of $V$. Hence
>
> $$
> L_{a,b,c}(x) = \frac{C_{11} + C_{12}\,x + C_{13}\,x^2}{\det V} = \frac{1}{\det V}\begin{vmatrix} 1 & x & x^2 \\ 1 & b & b^2 \\ 1 & c & c^2 \end{vmatrix} = \frac{\det\Delta(x, b, c)}{\det\Delta(a, b, c)} ,
> $$
>
> by the cofactor expansion across the first row of the matrix in the middle (its cofactors $C_{1k}$ are those of $V$). By the Vandermonde formula,
>
> $$
> L_{a,b,c}(x) = \frac{(b - x)(c - x)(c - b)}{(b - a)(c - a)(c - b)} = \frac{(x - b)(x - c)}{(a - b)(a - c)} .
> $$
>
> The determinant form shows the required values at once: $L_{a,b,c}(a) = 1$, and $L_{a,b,c}(b) = \det\Delta(b, b, c)/\det\Delta(a,b,c) = 0$ because $\Delta(b, b, c)$ has two equal columns; likewise at $c$.
>
> **Interpolation.** The quadratic with $f(a) = v_a$, $f(b) = v_b$, $f(c) = v_c$ is
>
> $$
> f(x) = v_a L_{a,b,c}(x) + v_b L_{b,c,a}(x) + v_c L_{c,a,b}(x),
> $$
>
> since at $x = a$ only the first term survives and gives $v_a$, and similarly at $b$ and $c$. (It is the only one: the coefficient system has the invertible matrix $V$.) For $a, b, c = 1, 2, 3$:
>
> $$
> f(x) = 3\,\frac{(x - 2)(x - 3)}{(1 - 2)(1 - 3)} + (-1)\,\frac{(x - 1)(x - 3)}{(2 - 1)(2 - 3)} + 2\,\frac{(x - 1)(x - 2)}{(3 - 1)(3 - 2)},
> $$
>
> $$
> f(4) = 3 \cdot \frac{2 \cdot 1}{2} + (-1)\cdot\frac{3 \cdot 1}{-1} + 2 \cdot \frac{3 \cdot 2}{2} = 3 + 3 + 6 = 12 .
> $$
>
> Multiplying out, $f(x) = \tfrac72 x^2 - \tfrac{29}{2} x + 14$; indeed $f(1) = 3$, $f(2) = -1$, $f(3) = 2$, $f(4) = 56 - 58 + 14 = 12$. In general, the Lagrange polynomial of degree $n - 1$ for distinct points $a_1, \ldots, a_n$ is
>
> $$
> L_{a_1, \ldots, a_n}(x) = \frac{(x - a_2)(x - a_3)\cdots(x - a_n)}{(a_1 - a_2)(a_1 - a_3)\cdots(a_1 - a_n)} = \frac{\det\Delta(x, a_2, \ldots, a_n)}{\det\Delta(a_1, a_2, \ldots, a_n)} .
> $$
>
> *The lecture orders the unknowns $A, B, C$, so its coefficient matrix has rows $(a^2, a, 1)$ and its determinant is $-\det\Delta(a,b,c)$, not $\det\Delta(a,b,c)$ as written; the numerator changes sign in the same way, so the quotient $L_{a,b,c}$ is unaffected.*
>
> *Source: 235 lecture L13*

^ex-27-2

## A Formula for the Inverse

> [!definition] Definition §27.2: Adjugate
> The **adjugate** (or **classical adjoint**) of an $n \times n$ matrix $A$ is the transpose of the matrix of cofactors ([[§24 Introduction to Determinants#^def-24-3|Definition §24.3]]):
>
> $$
> \operatorname{adj} A = \begin{bmatrix} C_{11} & C_{21} & \cdots & C_{n1} \\ C_{12} & C_{22} & \cdots & C_{n2} \\ \vdots & \vdots & & \vdots \\ C_{1n} & C_{2n} & \cdots & C_{nn} \end{bmatrix}, \qquad (\operatorname{adj} A)_{ij} = C_{ji} .
> $$
>
> Note the reversed subscripts. (The term *adjoint* has another meaning in advanced texts on linear transformations: the adjoint operator of an inner product space, [[§23 Self-Adjoint and Normal Operators#^ladr-7-1|LADR 7.1]].)
>
> *Lay: 3.3 (text)*

^def-27-2

> [!theorem] Theorem §27.2: An Inverse Formula
> Let $A$ be an invertible $n \times n$ matrix. Then
>
> $$
> A^{-1} = \frac{1}{\det A}\operatorname{adj} A .
> $$
>
> *Lay: Theorem 8 (3.3)*

^thm-27-2

> [!proof]+ Proof
> The $j$th column of $A^{-1}$ is the vector $\mathbf{x}$ with $A\mathbf{x} = \mathbf{e}_j$, and the $i$th entry of $\mathbf{x}$ is the $(i,j)$-entry of $A^{-1}$. By Cramer's rule,
>
> $$
> \{(i,j)\text{-entry of } A^{-1}\} = x_i = \frac{\det A_i(\mathbf{e}_j)}{\det A} . \qquad (2)
> $$
>
> Column $i$ of $A_i(\mathbf{e}_j)$ is $\mathbf{e}_j$, whose only nonzero entry is a $1$ in row $j$. Deleting row $j$ and column $i$ of $A_i(\mathbf{e}_j)$ gives $A_{ji}$ (column $i$, the only changed column, is gone). So the cofactor expansion down column $i$ gives
>
> $$
> \det A_i(\mathbf{e}_j) = (-1)^{j+i}\det A_{ji} = C_{ji} . \qquad (3)
> $$
>
> By (2) and (3), the $(i,j)$-entry of $A^{-1}$ is $C_{ji}/\det A$, the $(i,j)$-entry of $\frac{1}{\det A}\operatorname{adj} A$.

^pf-27-2

*Uses:* [[§27 Cramer’s Rule, Volume, and Linear Transformations#^thm-27-1|§27.1]], [[§27 Cramer’s Rule, Volume, and Linear Transformations#^def-27-2|Def. §27.2]], [[§24 Introduction to Determinants#^thm-24-1|§24.1]]

> [!remark] Remark: The 2 × 2 Case
> For $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ the submatrices are $1 \times 1$: $C_{11} = d$, $C_{12} = -c$, $C_{21} = -b$, $C_{22} = a$. So
>
> $$
> \operatorname{adj} A = \begin{bmatrix} C_{11} & C_{21} \\ C_{12} & C_{22} \end{bmatrix} = \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}, \qquad A^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix},
> $$
>
> the formula of [[§14 The Inverse of a Matrix#^thm-14-2|Theorem §14.2]] (Theorem 4 of 2.2).
>
> *Source: 235 lecture L13*

^rem-27-1

> [!example] Example §27.3: An Inverse by Cofactors
> Find the inverse of $A = \begin{bmatrix} 2 & 1 & 3 \\ 1 & -1 & 1 \\ 1 & 4 & -2 \end{bmatrix}$.
>
> The nine cofactors are
>
> $$
> \begin{aligned}
> C_{11} &= +\begin{vmatrix} -1 & 1 \\ 4 & -2 \end{vmatrix} = -2, & C_{12} &= -\begin{vmatrix} 1 & 1 \\ 1 & -2 \end{vmatrix} = 3, & C_{13} &= +\begin{vmatrix} 1 & -1 \\ 1 & 4 \end{vmatrix} = 5, \\
> C_{21} &= -\begin{vmatrix} 1 & 3 \\ 4 & -2 \end{vmatrix} = 14, & C_{22} &= +\begin{vmatrix} 2 & 3 \\ 1 & -2 \end{vmatrix} = -7, & C_{23} &= -\begin{vmatrix} 2 & 1 \\ 1 & 4 \end{vmatrix} = -7, \\
> C_{31} &= +\begin{vmatrix} 1 & 3 \\ -1 & 1 \end{vmatrix} = 4, & C_{32} &= -\begin{vmatrix} 2 & 3 \\ 1 & 1 \end{vmatrix} = 1, & C_{33} &= +\begin{vmatrix} 2 & 1 \\ 1 & -1 \end{vmatrix} = -3 .
> \end{aligned}
> $$
>
> The adjugate is the *transpose* of the matrix of cofactors ($C_{12}$ goes in position $(2,1)$, and so on):
>
> $$
> \operatorname{adj} A = \begin{bmatrix} -2 & 14 & 4 \\ 3 & -7 & 1 \\ 5 & -7 & -3 \end{bmatrix} .
> $$
>
> Instead of computing $\det A$ separately, multiply: this checks the cofactors and produces $\det A$ at the same time.
>
> $$
> (\operatorname{adj} A)\,A = \begin{bmatrix} -2 & 14 & 4 \\ 3 & -7 & 1 \\ 5 & -7 & -3 \end{bmatrix}\begin{bmatrix} 2 & 1 & 3 \\ 1 & -1 & 1 \\ 1 & 4 & -2 \end{bmatrix} = \begin{bmatrix} 14 & 0 & 0 \\ 0 & 14 & 0 \\ 0 & 0 & 14 \end{bmatrix} = 14I .
> $$
>
> Since $(\operatorname{adj} A)A = 14I$, the matrix $\frac{1}{14}\operatorname{adj} A$ is a left inverse of $A$, so $A$ is invertible ([[§16 Characterizations of Invertible Matrices#^cor-16-2|Corollary §16.2]]). [[§27 Cramer’s Rule, Volume, and Linear Transformations#^thm-27-2|Theorem §27.2]] then says $(\operatorname{adj} A)A = (\det A)I$, so $\det A = 14$ and
>
> $$
> A^{-1} = \frac{1}{14}\begin{bmatrix} -2 & 14 & 4 \\ 3 & -7 & 1 \\ 5 & -7 & -3 \end{bmatrix} = \begin{bmatrix} -1/7 & 1 & 2/7 \\ 3/14 & -1/2 & 1/14 \\ 5/14 & -1/2 & -3/14 \end{bmatrix} .
> $$
>
> *Lay: Example 3.3.3*

^ex-27-3

> [!remark] Remark: When to Use Cramer's Rule and the Adjugate
> - **Conditions.** Cramer's rule applies only to a *square* system with an *invertible* coefficient matrix ($\det A \ne 0$). When $\det A = 0$ it says nothing: the system may be inconsistent or have infinitely many solutions, and row reduction must decide ([[§27 Cramer’s Rule, Volume, and Linear Transformations#^ex-27-1|Example §27.1]](b)).
> - **Advantages.** Both formulas are explicit. They show how the solution or the inverse depends on the entries of $A$ and $\mathbf{b}$, which makes them the tool for theoretical questions: sensitivity of $\mathbf{x}$ to errors in $\mathbf{b}$ or $A$; solutions depending on a parameter ([[§27 Cramer’s Rule, Volume, and Linear Transformations#^ex-27-1|Example §27.1]](b)); integrality (if $A$ has integer entries and $\det A = \pm 1$, then $A^{-1} = \pm\operatorname{adj} A$ has integer entries, Lay's Exercise 18). For a $3 \times 3$ matrix with *complex* entries, Cramer's rule is sometimes preferred because row reduction of $[A \ \mathbf{b}]$ with complex arithmetic is messy.
> - **Cost.** For a larger $n \times n$ matrix, real or complex, Cramer's rule is hopelessly inefficient: it needs $n + 1$ determinants, and computing just *one* determinant takes about as much work as solving $A\mathbf{x} = \mathbf{b}$ by row reduction. Likewise, except in special cases, row reducing $[A \ I]$ ([[§15 Elementary Matrices and the Inversion Algorithm#^rem-15-2|§15, Remark: Method — Finding the Inverse of a Matrix]]) is a much better way to compute $A^{-1}$ than the $n^2$ cofactors of $\operatorname{adj} A$.

^rem-27-2

*Continued in [[§28 Determinants as Area or Volume]]: areas and volumes as determinants, and how a linear transformation changes them.*
