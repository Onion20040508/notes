---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 3
section: 22
lay: "3.3"
aliases: ["Lay 3.3"]
tags: [applied-linear-algebra, math235]
---
← [[§21 Properties of Determinants]] · ↑ [[· 3 Determinants]] · [[§23 Vector Spaces and Subspaces]] →

*Lay, Section 3.3 · MATH 235 lectures L11, L12, L13.*

This section turns the theory of [[§20 Introduction to Determinants|§20]]–[[§21 Properties of Determinants|§21]] into formulas and geometry. Cramer's rule writes the solution of an invertible system $A\mathbf{x} = \mathbf{b}$ as quotients of determinants, and applied to the columns of the identity it gives an explicit inverse, $A^{-1} = \frac{1}{\det A}\operatorname{adj} A$. Both are mainly theoretical tools: they show how solutions depend on the data. Geometrically, $|\det A|$ is the area (in $\mathbb{R}^2$) or volume (in $\mathbb{R}^3$) of the parallelogram or parallelepiped spanned by the columns of $A$, and the linear map $\mathbf{x} \mapsto A\mathbf{x}$ multiplies every area or volume by $|\det A|$. In multivariable calculus this factor becomes the Jacobian.

## Cramer's Rule

> [!definition] Definition §22.1: The Matrix A_i(b)
> For an $n \times n$ matrix $A = [\mathbf{a}_1 \ \cdots \ \mathbf{a}_n]$ and $\mathbf{b} \in \mathbb{R}^n$, $A_i(\mathbf{b})$ is the matrix obtained from $A$ by replacing column $i$ by $\mathbf{b}$:
>
> $$
> A_i(\mathbf{b}) = [\mathbf{a}_1 \ \cdots \ \mathbf{a}_{i-1} \ \ \mathbf{b} \ \ \mathbf{a}_{i+1} \ \cdots \ \mathbf{a}_n] .
> $$
>
> *Lay: 3.3 (text)*

^def-22-1

> [!theorem] Theorem §22.1: Cramer's Rule
> Let $A$ be an invertible $n \times n$ matrix. For any $\mathbf{b}$ in $\mathbb{R}^n$, the unique solution $\mathbf{x}$ of $A\mathbf{x} = \mathbf{b}$ has entries given by
>
> $$
> x_i = \frac{\det A_i(\mathbf{b})}{\det A}, \qquad i = 1, 2, \ldots, n . \qquad (1)
> $$
>
> *Lay: Theorem 7 (3.3)*

^thm-22-1

> [!proof]+ Proof
> Since $A$ is invertible, $\det A \ne 0$ ([[§21 Properties of Determinants#^thm-21-3|Theorem §21.3]]) and the solution $\mathbf{x} = A^{-1}\mathbf{b}$ is unique. Let $\mathbf{e}_1, \ldots, \mathbf{e}_n$ be the columns of $I$. If $A\mathbf{x} = \mathbf{b}$, the definition of matrix multiplication (column by column) gives
>
> $$
> A \cdot I_i(\mathbf{x}) = A\,[\mathbf{e}_1 \ \cdots \ \mathbf{x} \ \cdots \ \mathbf{e}_n] = [A\mathbf{e}_1 \ \cdots \ A\mathbf{x} \ \cdots \ A\mathbf{e}_n] = [\mathbf{a}_1 \ \cdots \ \mathbf{b} \ \cdots \ \mathbf{a}_n] = A_i(\mathbf{b}) .
> $$
>
> By the multiplicative property ([[§21 Properties of Determinants#^thm-21-9|Theorem §21.9]]),
>
> $$
> (\det A)(\det I_i(\mathbf{x})) = \det A_i(\mathbf{b}) .
> $$
>
> Row $i$ of $I_i(\mathbf{x})$ is $(0, \ldots, 0, x_i, 0, \ldots, 0)$ with $x_i$ in position $i$, and deleting row $i$ and column $i$ leaves $I_{n-1}$. So the cofactor expansion across row $i$ gives $\det I_i(\mathbf{x}) = x_i \det I_{n-1} = x_i$. Hence $(\det A)\,x_i = \det A_i(\mathbf{b})$, which is (1) because $\det A \ne 0$.

^pf-22-1

*Uses:* [[§22 Cramer’s Rule, Volume, and Linear Transformations#^def-22-1|Def. §22.1]], [[§21 Properties of Determinants#^thm-21-3|§21.3]], [[§21 Properties of Determinants#^thm-21-9|§21.9]], [[§20 Introduction to Determinants#^thm-20-1|§20.1]], [[§11 Matrix Operations#^prop-11-3|§11.3]] (columns of a product)

> [!remark]- Connections
> - See also: Cramer's rule for $n = 2$ fits a combination $c_1y_1 + c_2y_2$ of two solutions of $y'' + py' + qy = 0$ to initial conditions, with the Wronskian as the common denominator, [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-3|331 Thm. §14.3]] (formula (11) of its proof).

> [!example] Example §22.1: Cramer's Rule, With and Without a Parameter
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
> **(b)** Systems whose coefficients involve a parameter $s$ arise when Laplace transforms turn linear differential equations (electrical engineering, control theory) into algebraic equations. For which $s$ does
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

^ex-22-1

> [!example] Example §22.2: Lagrange Interpolation
> **Problem.** A quadratic $f(x) = Ax^2 + Bx + C$ has $f(1) = 3$, $f(2) = -1$, $f(3) = 2$. Find $f(4)$.
>
> **Lagrange polynomials.** For distinct numbers $a, b, c$, look for the quadratic $L_{a,b,c}(x) = Ax^2 + Bx + C$ with $L_{a,b,c}(a) = 1$, $L_{a,b,c}(b) = 0$, $L_{a,b,c}(c) = 0$. With the unknowns ordered $C, B, A$ the conditions are
>
> $$
> V \begin{bmatrix} C \\ B \\ A \end{bmatrix} = \mathbf{e}_1, \qquad V = \begin{bmatrix} 1 & a & a^2 \\ 1 & b & b^2 \\ 1 & c & c^2 \end{bmatrix} = \Delta(a, b, c)^T ,
> $$
>
> the transpose of the Vandermonde matrix of [[§21 Properties of Determinants#^prop-21-8|Proposition §21.8]]. So $\det V = (b - a)(c - a)(c - b) \ne 0$, and Cramer's rule gives $C = \det V_1(\mathbf{e}_1)/\det V$, $B = \det V_2(\mathbf{e}_1)/\det V$, $A = \det V_3(\mathbf{e}_1)/\det V$. Expanding $V_k(\mathbf{e}_1)$ down its column $k$, which is $\mathbf{e}_1$, shows $\det V_k(\mathbf{e}_1) = C_{1k}$, the $(1,k)$-cofactor of $V$. Hence
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

^ex-22-2

## A Formula for the Inverse

> [!definition] Definition §22.2: Adjugate
> The **adjugate** (or **classical adjoint**) of an $n \times n$ matrix $A$ is the transpose of the matrix of cofactors ([[§20 Introduction to Determinants#^def-20-3|Definition §20.3]]):
>
> $$
> \operatorname{adj} A = \begin{bmatrix} C_{11} & C_{21} & \cdots & C_{n1} \\ C_{12} & C_{22} & \cdots & C_{n2} \\ \vdots & \vdots & & \vdots \\ C_{1n} & C_{2n} & \cdots & C_{nn} \end{bmatrix}, \qquad (\operatorname{adj} A)_{ij} = C_{ji} .
> $$
>
> Note the reversed subscripts. (The term *adjoint* has another meaning in advanced texts on linear transformations: the adjoint operator of an inner product space.)
>
> *Lay: 3.3 (text)*

^def-22-2

> [!theorem] Theorem §22.2: An Inverse Formula
> Let $A$ be an invertible $n \times n$ matrix. Then
>
> $$
> A^{-1} = \frac{1}{\det A}\operatorname{adj} A .
> $$
>
> *Lay: Theorem 8 (3.3)*

^thm-22-2

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

^pf-22-2

*Uses:* [[§22 Cramer’s Rule, Volume, and Linear Transformations#^thm-22-1|§22.1]], [[§22 Cramer’s Rule, Volume, and Linear Transformations#^def-22-2|Def. §22.2]], [[§20 Introduction to Determinants#^thm-20-1|§20.1]]

> [!remark] Remark: The 2 × 2 Case
> For $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ the submatrices are $1 \times 1$: $C_{11} = d$, $C_{12} = -c$, $C_{21} = -b$, $C_{22} = a$. So
>
> $$
> \operatorname{adj} A = \begin{bmatrix} C_{11} & C_{21} \\ C_{12} & C_{22} \end{bmatrix} = \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}, \qquad A^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix},
> $$
>
> the formula of [[§12 The Inverse of a Matrix#^thm-12-2|Theorem §12.2]] (Theorem 4 of 2.2).
>
> *Source: 235 lecture L13*

^rem-22-1

> [!example] Example §22.3: An Inverse by Cofactors
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
> Since $(\operatorname{adj} A)A = 14I$, the matrix $\frac{1}{14}\operatorname{adj} A$ is a left inverse of $A$, so $A$ is invertible ([[§13 Characterizations of Invertible Matrices#^cor-13-2|Corollary §13.2]]). Theorem §22.2 then says $(\operatorname{adj} A)A = (\det A)I$, so $\det A = 14$ and
>
> $$
> A^{-1} = \frac{1}{14}\begin{bmatrix} -2 & 14 & 4 \\ 3 & -7 & 1 \\ 5 & -7 & -3 \end{bmatrix} = \begin{bmatrix} -1/7 & 1 & 2/7 \\ 3/14 & -1/2 & 1/14 \\ 5/14 & -1/2 & -3/14 \end{bmatrix} .
> $$
>
> *Lay: Example 3.3.3*

^ex-22-3

> [!remark] Remark: When to Use Cramer's Rule and the Adjugate
> - **Conditions.** Cramer's rule applies only to a *square* system with an *invertible* coefficient matrix ($\det A \ne 0$). When $\det A = 0$ it says nothing: the system may be inconsistent or have infinitely many solutions, and row reduction must decide (Example §22.1(b)).
> - **Advantages.** Both formulas are explicit. They show how the solution or the inverse depends on the entries of $A$ and $\mathbf{b}$, which makes them the tool for theoretical questions: sensitivity of $\mathbf{x}$ to errors in $\mathbf{b}$ or $A$; solutions depending on a parameter (Example §22.1(b)); integrality (if $A$ has integer entries and $\det A = \pm 1$, then $A^{-1} = \pm\operatorname{adj} A$ has integer entries, Lay's Exercise 18). For a $3 \times 3$ matrix with *complex* entries, Cramer's rule is sometimes preferred because row reduction of $[A \ \mathbf{b}]$ with complex arithmetic is messy.
> - **Cost.** For a larger $n \times n$ matrix, real or complex, Cramer's rule is hopelessly inefficient: it needs $n + 1$ determinants, and computing just *one* determinant takes about as much work as solving $A\mathbf{x} = \mathbf{b}$ by row reduction. Likewise, except in special cases, row reducing $[A \ I]$ ([[§12 The Inverse of a Matrix#^rem-12-3|Remark §12.3]]) is a much better way to compute $A^{-1}$ than the $n^2$ cofactors of $\operatorname{adj} A$.

^rem-22-2

## Determinants as Area or Volume

Lengths, areas and volumes in $\mathbb{R}^2$ and $\mathbb{R}^3$ are taken in their usual Euclidean sense (length and distance in $\mathbb{R}^n$ are defined in [[§40 Inner Product, Length, and Orthogonality#^def-40-2|Definition §40.2]]).

> [!theorem] Lemma §22.3: Shears Preserve Area and Volume
> Let $\mathbf{a}_1$ and $\mathbf{a}_2$ be nonzero vectors in $\mathbb{R}^2$. Then for any scalar $c$, the area of the parallelogram determined by $\mathbf{a}_1$ and $\mathbf{a}_2$ equals the area of the parallelogram determined by $\mathbf{a}_1$ and $\mathbf{a}_2 + c\mathbf{a}_1$.
>
> Likewise in $\mathbb{R}^3$: the parallelepiped determined by $\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3$ has the same volume as the one determined by $\mathbf{a}_1, \mathbf{a}_2 + c\mathbf{a}_1, \mathbf{a}_3$.
>
> *Lay: 3.3 (boxed statement in the proof of Theorem 9)*

^lem-22-3

> [!proof]+ Proof
> **In $\mathbb{R}^2$.** If $\mathbf{a}_2$ is a multiple of $\mathbf{a}_1$, so is $\mathbf{a}_2 + c\mathbf{a}_1$, and both parallelograms are degenerate, with area $0$. Otherwise, let $L$ be the line through $\mathbf{0}$ and $\mathbf{a}_1$. Then $\mathbf{a}_2 + L$ is the line through $\mathbf{a}_2$ parallel to $L$, and $\mathbf{a}_2 + c\mathbf{a}_1$ lies on it. The points $\mathbf{a}_2$ and $\mathbf{a}_2 + c\mathbf{a}_1$ therefore have the same perpendicular distance to $L$. The two parallelograms share the base from $\mathbf{0}$ to $\mathbf{a}_1$ and have the same height, so they have the same area.
>
> **In $\mathbb{R}^3$.** The volume of the parallelepiped is the area of its base, the parallelogram in the plane $\operatorname{Span}\{\mathbf{a}_1, \mathbf{a}_3\}$, times the altitude of $\mathbf{a}_2$ above that plane. The vector $\mathbf{a}_2 + c\mathbf{a}_1$ lies in the plane $\mathbf{a}_2 + \operatorname{Span}\{\mathbf{a}_1, \mathbf{a}_3\}$, which is parallel to $\operatorname{Span}\{\mathbf{a}_1, \mathbf{a}_3\}$, so it has the same altitude. Same base, same altitude: same volume. (If $\mathbf{a}_1, \mathbf{a}_3$ are dependent, both parallelepipeds lie in a plane and have volume $0$.)

^pf-22-3

*Uses:* only Euclidean geometry (area = base × height, volume = base area × altitude)

![[m235-22-1.svg]]
*Lemma §22.3 in $\mathbb{R}^2$. Adding $c\,\mathbf{a}_1$ to $\mathbf{a}_2$ slides the top side of the parallelogram along the line $\mathbf{a}_2 + L$, parallel to the base $L$. The blue and the green parallelogram share the base $\mathbf{0}\mathbf{a}_1$ and the height (red), so they have equal area. Algebraically this is a column replacement, which does not change the determinant either.*

> [!theorem] Theorem §22.4: Determinants as Area or Volume
> If $A$ is a $2 \times 2$ matrix, the area of the parallelogram determined by the columns of $A$ is $|\det A|$. If $A$ is a $3 \times 3$ matrix, the volume of the parallelepiped determined by the columns of $A$ is $|\det A|$.
>
> *Lay: Theorem 9 (3.3)*

^thm-22-4

> [!proof]+ Proof
> **$2 \times 2$.** The theorem is obviously true for a diagonal matrix:
>
> $$
> \left|\det\begin{bmatrix} a & 0 \\ 0 & d \end{bmatrix}\right| = |ad| = \text{area of the rectangle with sides } \begin{bmatrix} a \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ d \end{bmatrix} .
> $$
>
> If the columns of $A = [\mathbf{a}_1 \ \mathbf{a}_2]$ are linearly dependent, the parallelogram is degenerate (a segment or a point) with area $0$, and $\det A = 0$ ([[§21 Properties of Determinants#^cor-21-5|Corollary §21.5]]). So let $A$ be invertible. It suffices to transform $A$ into a diagonal matrix by operations that change neither $|\det A|$ nor the area of the parallelogram. Column interchanges and column replacements do not change $|\det A|$ ([[§21 Properties of Determinants#^cor-21-7|Corollary §21.7]]). Column interchanges do not change the parallelogram at all, and column replacements do not change its area (Lemma §22.3; all columns stay nonzero because the matrix stays invertible). Such operations do suffice to reach a diagonal matrix (Lay says this is "easy to see"; here is why): think of them as row operations on $A^T$. Row reduction with interchanges and replacements brings the invertible matrix $A^T$ to an echelon form with nonzero diagonal entries, and further replacements, using each diagonal entry from the bottom up to clear the entries above it, make it diagonal.
>
> **$3 \times 3$.** The same argument works. The theorem is obvious for a diagonal matrix, where the parallelepiped is a box with volume $|abc|$. If the columns are dependent, the parallelepiped is flat (volume $0$) and $\det A = 0$. Otherwise column interchanges and replacements turn $A$ into a diagonal matrix without changing $|\det A|$ or, by the $\mathbb{R}^3$ part of Lemma §22.3, the volume.

^pf-22-4

*Uses:* [[§22 Cramer’s Rule, Volume, and Linear Transformations#^lem-22-3|§22.3]], [[§21 Properties of Determinants#^cor-21-5|§21.5]], [[§21 Properties of Determinants#^cor-21-7|§21.7]], [[§20 Introduction to Determinants#^thm-20-2|§20.2]]

> [!remark]- Connections
> - In Calculus the same facts come from the cross product: area $= |\mathbf{a} \times \mathbf{b}|$ ([[§83 The Cross Product#^cor-83-6|Calc Cor. §83.6]]) and volume $= |\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})| = |\det|$ ([[§83 The Cross Product#^thm-83-10|Calc Thm. §83.10]]); the lecture writes $\det[\mathbf{v}_1 \ \mathbf{v}_2 \ \mathbf{v}_3] = (\mathbf{v}_1 \times \mathbf{v}_2) \cdot \mathbf{v}_3$.
> - Rigorous treatment in $\mathbb{R}^n$ for every measurable set: [[§34 Determinants#^ladr-9-61|LADR 9.61]] (proved via the singular value decomposition, [[§34 Determinants#^ladr-9-60|LADR 9.60]]); the sign of $\det$ records orientation, which $|\det|$ forgets.

> [!example] Example §22.4: Areas of Parallelograms, Triangles and Quadrilaterals
> **(a) A parallelogram given by its vertices.** Find the area of the parallelogram with vertices $(-2, -2)$, $(0, 3)$, $(4, -1)$, $(6, 4)$. First translate it so that one vertex is the origin: subtracting $(-2, -2)$ from each vertex gives $(0, 0)$, $(2, 5)$, $(6, 1)$, $(8, 6)$, a parallelogram with the same area. It is determined by the columns of
>
> $$
> A = \begin{bmatrix} 2 & 6 \\ 5 & 1 \end{bmatrix}, \qquad |\det A| = |2 - 30| = 28,
> $$
>
> so the area is $28$. (The fourth vertex $(8, 6) = (2, 5) + (6, 1)$ confirms which vertices are adjacent to the origin.)
>
> **(b) A triangle.** The triangle with vertices $(0, 0)$, $(1, 2)$, $(-3, 1)$ is half of the parallelogram with sides $\mathbf{v}_1 = (1, 2)$ and $\mathbf{v}_2 = (-3, 1)$, so its area is
>
> $$
> \frac12\left|\det\begin{bmatrix} 1 & -3 \\ 2 & 1 \end{bmatrix}\right| = \frac12(1 + 6) = \frac72 .
> $$
>
> For a triangle not at the origin, first translate one vertex to $\mathbf{0}$, as in (a).
>
> **(c) A quadrilateral.** Cut it along a diagonal into two triangles and add their areas. For the convex quadrilateral with vertices $(0,0)$, $(4,0)$, $(5,3)$, $(1,4)$ in order, the diagonal from $(0,0)$ to $(5,3)$ gives
>
> $$
> \frac12\left|\det\begin{bmatrix} 4 & 5 \\ 0 & 3 \end{bmatrix}\right| + \frac12\left|\det\begin{bmatrix} 5 & 1 \\ 3 & 4 \end{bmatrix}\right| = \frac12 \cdot 12 + \frac12 \cdot 17 = \frac{29}{2} .
> $$
>
> *Lay: Example 3.3.4*
> *Source: 235 lecture L11 (b); 235 checklist (c)*

^ex-22-4

## Linear Transformations

For a linear transformation $T$ and a set $S$ in its domain, $T(S)$ denotes the set of images of points of $S$. When $S$ is a region bounded by a parallelogram, $S$ is also called a parallelogram.

> [!theorem] Theorem §22.5: How a Linear Transformation Changes Area and Volume
> Let $T: \mathbb{R}^2 \to \mathbb{R}^2$ be the linear transformation determined by a $2 \times 2$ matrix $A$. If $S$ is a parallelogram in $\mathbb{R}^2$, then
>
> $$
> \{\text{area of } T(S)\} = |\det A| \cdot \{\text{area of } S\} . \qquad (5)
> $$
>
> If $T$ is determined by a $3 \times 3$ matrix $A$, and if $S$ is a parallelepiped in $\mathbb{R}^3$, then
>
> $$
> \{\text{volume of } T(S)\} = |\det A| \cdot \{\text{volume of } S\} . \qquad (6)
> $$
>
> *Lay: Theorem 10 (3.3)*

^thm-22-5

> [!proof]+ Proof
> **A parallelogram at the origin.** Let $A = [\mathbf{a}_1 \ \mathbf{a}_2]$. A parallelogram at the origin determined by vectors $\mathbf{b}_1$ and $\mathbf{b}_2$ has the form
>
> $$
> S = \{s_1\mathbf{b}_1 + s_2\mathbf{b}_2 : 0 \le s_1 \le 1,\ 0 \le s_2 \le 1\} .
> $$
>
> The image of $S$ under $T$ consists of the points
>
> $$
> T(s_1\mathbf{b}_1 + s_2\mathbf{b}_2) = s_1T(\mathbf{b}_1) + s_2T(\mathbf{b}_2) = s_1A\mathbf{b}_1 + s_2A\mathbf{b}_2, \qquad 0 \le s_1, s_2 \le 1 .
> $$
>
> So $T(S)$ is the parallelogram determined by the columns of $[A\mathbf{b}_1 \ A\mathbf{b}_2] = AB$, where $B = [\mathbf{b}_1 \ \mathbf{b}_2]$. By Theorem §22.4 and the multiplicative property,
>
> $$
> \{\text{area of } T(S)\} = |\det AB| = |\det A| \cdot |\det B| = |\det A| \cdot \{\text{area of } S\} . \qquad (7)
> $$
>
> **Any parallelogram.** An arbitrary parallelogram has the form $\mathbf{p} + S$ with $\mathbf{p}$ a vector and $S$ a parallelogram at the origin. By linearity $T(\mathbf{p} + \mathbf{s}) = T(\mathbf{p}) + T(\mathbf{s})$, so $T$ maps $\mathbf{p} + S$ onto the translate $T(\mathbf{p}) + T(S)$ (Lay's Exercise 26). Since translation does not affect area,
>
> $$
> \{\text{area of } T(\mathbf{p} + S)\} = \{\text{area of } T(\mathbf{p}) + T(S)\} = \{\text{area of } T(S)\} = |\det A| \cdot \{\text{area of } S\} = |\det A| \cdot \{\text{area of } \mathbf{p} + S\} .
> $$
>
> **The $3 \times 3$ case** (Lay: "analogous"). A parallelepiped at the origin is $S = \{s_1\mathbf{b}_1 + s_2\mathbf{b}_2 + s_3\mathbf{b}_3 : 0 \le s_i \le 1\}$, its image is the parallelepiped determined by the columns of $AB$ with $B = [\mathbf{b}_1 \ \mathbf{b}_2 \ \mathbf{b}_3]$, and $|\det AB| = |\det A|\,|\det B|$ gives (6) by Theorem §22.4; translations are handled as before.

^pf-22-5

*Uses:* [[§22 Cramer’s Rule, Volume, and Linear Transformations#^thm-22-4|§22.4]], [[§21 Properties of Determinants#^thm-21-9|§21.9]], [[§8 Introduction to Linear Transformations#^def-8-3|Def. §8.3]] (linearity)

> [!theorem] Theorem §22.6: Regions of Finite Area or Volume
> The conclusions of Theorem §22.5 hold whenever $S$ is a region in $\mathbb{R}^2$ with finite area or a region in $\mathbb{R}^3$ with finite volume.
>
> *Lay: 3.3 (boxed generalization of Theorem 10)*

^thm-22-6

*Lay outlines the argument (below); a proof needs the theory of area and volume. See [[§15 Multivariable Integration#^prop-15-19|452 Prop. §15.19]] and [[§34 Determinants#^ladr-9-61|LADR 9.61]].*

> [!remark] Remark: Why It Works
> A planar region $R$ with finite area can be approximated by a grid of small squares lying inside $R$; making the squares small enough, the total area of the squares is as close as desired to the area of $R$. Under $T$, each small square goes to a small parallelogram whose area is $|\det A|$ times the area of the square (Theorem §22.5). So if $R'$ is the union of the squares inside $R$, the area of $T(R')$ is $|\det A|$ times the area of $R'$, and the area of $T(R')$ is close to the area of $T(R)$. A limiting process gives $\{\text{area of } T(R)\} = |\det A| \cdot \{\text{area of } R\}$. The lecture draws the same picture for an arbitrary blob $D$, and composes: applying $S$ and then $T$ multiplies volume by $|\det S|$ and then by $|\det T|$ ([[§21 Properties of Determinants#^rem-21-4|Remark §21.4]]).

^rem-22-3

> [!remark]- Connections
> - For a nonlinear map the factor $|\det A|$ becomes the absolute value of the Jacobian determinant in the change of variables formula: [[§106 Change of Variables in Multiple Integrals#^thm-106-1|Calc Thm. §106.1]] (double integrals), [[§15 Multivariable Integration#^thm-15-20|452 Thm. §15.20]] (in $\mathbb{R}^n$). This is the "expansion rate near the poles" of Lay's chapter introduction.

> [!example] Example §22.5: Areas and Volumes of Images
> **(a) The image of a parallelogram.** Let $S$ be the parallelogram determined by $\mathbf{b}_1 = (1, 3)$ and $\mathbf{b}_2 = (5, 1)$, and let $A = \begin{bmatrix} 1 & -0.1 \\ 0 & 2 \end{bmatrix}$. The area of $S$ is $\left|\det\begin{bmatrix} 1 & 5 \\ 3 & 1 \end{bmatrix}\right| = |1 - 15| = 14$, and $\det A = 2$. By Theorem §22.5 the area of the image of $S$ under $\mathbf{x} \mapsto A\mathbf{x}$ is $2 \cdot 14 = 28$. Directly: $A\mathbf{b}_1 = (0.7, 6)$, $A\mathbf{b}_2 = (4.9, 2)$ and $|0.7 \cdot 2 - 4.9 \cdot 6| = |1.4 - 29.4| = 28$.
>
> **(b) The area of an ellipse.** Let $a, b > 0$ and let $E$ be the region bounded by the ellipse $\dfrac{x_1^2}{a^2} + \dfrac{x_2^2}{b^2} = 1$. Then $E$ is the image of the unit disk $D$ under $T(\mathbf{u}) = A\mathbf{u}$ with $A = \begin{bmatrix} a & 0 \\ 0 & b \end{bmatrix}$: if $\mathbf{x} = A\mathbf{u}$, then $u_1 = x_1/a$ and $u_2 = x_2/b$, so $\mathbf{u}$ is in the unit disk ($u_1^2 + u_2^2 \le 1$) if and only if $\mathbf{x}$ is in $E$ ($(x_1/a)^2 + (x_2/b)^2 \le 1$). By Theorem §22.6,
>
> $$
> \{\text{area of ellipse}\} = \{\text{area of } T(D)\} = |\det A| \cdot \{\text{area of } D\} = ab \cdot \pi(1)^2 = \pi ab .
> $$
>
> **(c) The volume of an ellipsoid.** In the same way $A = \operatorname{diag}(a, b, c)$ maps the unit ball onto the solid ellipsoid $\frac{x_1^2}{a^2} + \frac{x_2^2}{b^2} + \frac{x_3^2}{c^2} \le 1$, so its volume is $abc \cdot \frac43\pi = \frac43\pi abc$.
>
> *Lay: Example 3.3.5; Practice Problem 3.3; Exercise 31 (3.3)*

^ex-22-5

![[m235-22-2.svg]]
*Example §22.5(a). The parallelogram $S$ spanned by $\mathbf{b}_1, \mathbf{b}_2$ goes to the parallelogram $T(S)$ spanned by $A\mathbf{b}_1, A\mathbf{b}_2$, the columns of $AB$. Its area is $|\det AB| = |\det A|\,|\det B| = 2 \cdot 14$.*
