---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 1
section: 1
lay: "1.1"
aliases: ["Lay 1.1"]
tags: [applied-linear-algebra, math235]
---
↑ [[· 1 Linear Equations in Linear Algebra]] · [[§2 Row Reduction and Echelon Forms]] →

*Lay, Section 1.1 · MATH 235 lectures L02, L1.*

A linear system is solved by replacing it with a simpler system that has the same solutions. This section records a system as its augmented matrix, introduces the three elementary row operations, and shows that they never change the solution set, because each one can be undone. Along the way it raises the two questions that run through the whole subject: does a solution exist, and is it unique? Geometrically, each equation in two or three unknowns is a line or a plane, and solving the system means intersecting them.

## Linear Systems

> [!definition] Definition §1.1: Linear Equation
> A **linear equation** in the variables $x_1, \ldots, x_n$ is an equation that can be written in the form
>
> $$
> a_1x_1 + a_2x_2 + \cdots + a_nx_n = b ,
> $$
>
> where $b$ and the **coefficients** $a_1, \ldots, a_n$ are real or complex numbers, usually known in advance.
>
> For example, $4x_1 - 5x_2 + 2 = x_1$ and $x_2 = 2(\sqrt6 - x_1) + x_3$ are linear, since they rearrange to $3x_1 - 5x_2 = -2$ and $2x_1 + x_2 - x_3 = 2\sqrt6$. The equations $4x_1 - 5x_2 = x_1x_2$ and $x_2 = 2\sqrt{x_1} - 6$ are not linear, because of the product $x_1x_2$ and the root $\sqrt{x_1}$.
>
> *Lay: 1.1 (text)*

^def-1-1

> [!definition] Definition §1.4: Linear System
> A **system of linear equations** (or **linear system**) is a collection of one or more linear equations involving the same variables $x_1, \ldots, x_n$.
>
> *Lay: 1.1 (text)*

^def-1-2

> [!definition] Definition §1.5: Solution; Solution Set
> A **solution** of the system is a list $(s_1, \ldots, s_n)$ of numbers that makes each equation a true statement when $s_1, \ldots, s_n$ are substituted for $x_1, \ldots, x_n$. The set of all solutions is the **solution set** of the system.
>
> For example, $(5, 6.5, 3)$ is a solution of
>
> $$
> \begin{aligned}
> 2x_1 - x_2 + 1.5x_3 &= 8 \\
> x_1 \phantom{{}- x_2} - 4x_3 &= -7 ,
> \end{aligned}
> $$
>
> since substituting gives $10 - 6.5 + 4.5 = 8$ and $5 - 12 = -7$.
>
> *Lay: 1.1 (text)*

^def-1-3

> [!definition] Definition §1.8: Equivalent Systems
> Two linear systems are **equivalent** if they have the same solution set.
>
> *Lay: 1.1 (text)*

^def-1-4

A system of two equations in two unknowns asks for the intersection of two lines: they meet in one point, are parallel, or coincide ([[§1 Systems of Linear Equations#^ex-1-2|Example §1.2]]). The same three possibilities are the only ones in general: *a system of linear equations has no solution, exactly one solution, or infinitely many solutions.* Lay verifies this in Section 1.2: [[§3 Solutions of Linear Systems#^cor-3-2|Corollary §3.2]], from Lay's Theorem 2, the Existence and Uniqueness Theorem ([[§3 Solutions of Linear Systems#^thm-3-1|Theorem §3.1]]).

> [!definition] Definition §1.9: Consistent and Inconsistent Systems
> A system of linear equations is **consistent** if it has either one solution or infinitely many solutions (that is, at least one solution); it is **inconsistent** if it has no solution.
>
> *Lay: 1.1 (text)*

^def-1-5

> [!remark] Remark: Why Not Exactly Two Solutions
> A linear system cannot have exactly two solutions. If $\mathbf{u} = (u_1, \ldots, u_n)$ and $\mathbf{v} = (v_1, \ldots, v_n)$ are both solutions, then so is every point
>
> $$
> (1 - t)\mathbf{u} + t\mathbf{v}, \qquad t \in \mathbb{R},
> $$
>
> of the line through them: for each equation $a_1x_1 + \cdots + a_nx_n = b$,
>
> $$
> \sum_i a_i\big((1 - t)u_i + tv_i\big) = (1 - t)\sum_i a_iu_i + t\sum_i a_iv_i = (1 - t)b + tb = b .
> $$
>
> If $\mathbf{u} \ne \mathbf{v}$, different values of $t$ give different points, so two solutions force infinitely many. In the picture, the solution set of each equation in three unknowns is a plane, and two planes that share two points share the whole line through them. The lecture states the finer count "$\infty^a$": a line of solutions is "$\infty^1$", a plane "$\infty^2$", and for $m$ equations in $\ell$ unknowns one expects $\infty^{\ell - m}$ solutions. What is true is that a system has either no solution or $\infty^{k}$ solutions with $k \ge \ell - m$ (and $k \ge 0$, where $\infty^0 = 1$ means a unique solution): the exponent is the number of free variables ([[§3 Solutions of Linear Systems#^thm-3-1|Theorem §3.1]]), and since at most $m$ of the $\ell$ variables have a pivot, at least $\ell - m$ of them are free.
>
> *Source: 235 lecture L02*

^rem-1-1

## Matrix Notation

> [!definition] Definition §1.10: Matrix
> A **matrix** is a rectangular array of numbers.
>
> *Lay: 1.1 (text)*

^def-1-6

> [!remark]- Connections
> - Rigorous treatment: [[§9 Matrices#^ladr-3-29|LADR 3.29]] (an $m$-by-$n$ matrix with entries $A_{j,k}$). Axler meets linear systems only as one application of linear maps, writing the system as $T(x) = c$ for a linear $T: \mathbb{F}^n \to \mathbb{F}^m$ ([[§8 Null Spaces and Ranges#^ladr-3-26|LADR 3.26]], [[§8 Null Spaces and Ranges#^ladr-3-28|LADR 3.28]]); Lay starts from the systems and reaches linear maps in [[§9 Introduction to Linear Transformations|§9]].

> [!definition] Definition §1.7: Coefficient Matrix and Augmented Matrix
> Given a linear system with the coefficients of each variable aligned in columns, the matrix of the coefficients is the **coefficient matrix** (or matrix of coefficients) of the system, and the coefficient matrix with an added column containing the constants from the right sides of the equations is the **augmented matrix** of the system. For the system
>
> $$
> \begin{aligned}
> x_1 - 2x_2 + \phantom{8}x_3 &= 0 \\
> 2x_2 - 8x_3 &= 8 \\
> 5x_1 \phantom{{}- 2x_2} - 5x_3 &= 10
> \end{aligned}
> \qquad (3)
> $$
>
> they are
>
> $$
> \begin{bmatrix} 1 & -2 & 1 \\ 0 & 2 & -8 \\ 5 & 0 & -5 \end{bmatrix}
> \qquad\text{and}\qquad
> \begin{bmatrix} 1 & -2 & 1 & 0 \\ 0 & 2 & -8 & 8 \\ 5 & 0 & -5 & 10 \end{bmatrix} . \qquad (4)
> $$
>
> (The second row contains a zero because the second equation can be written $0 \cdot x_1 + 2x_2 - 8x_3 = 8$.) (The lecture calls the coefficient matrix the **main part** of the augmented matrix.)
>
> *Lay: 1.1 (text)*

^def-1-7

> [!definition] Definition §1.8: Size of a Matrix
> The **size** of a matrix tells how many rows and columns it has: an **$m \times n$ matrix** ("$m$ by $n$") has $m$ rows and $n$ columns, rows always first. The augmented matrix (4) is $3 \times 4$.
>
> *Lay: 1.1 (text)*

^def-1-8

## Solving a Linear System

The strategy is to replace a system by an equivalent system that is easier to solve. Use the $x_1$ term in the first equation to eliminate $x_1$ from the other equations, then the $x_2$ term in the second equation to eliminate $x_2$ from the others, and so on. Three operations on equations are used, and on the augmented matrix they act on rows.

> [!definition] Definition §1.9: Elementary Row Operations
> The **elementary row operations** on a matrix are:
> 1. **(Replacement)** Replace one row by the sum of itself and a multiple of another row ("add to one row a multiple of another row").
> 2. **(Interchange)** Interchange two rows.
> 3. **(Scaling)** Multiply all entries in a row by a nonzero constant.
>
> They can be applied to any matrix, not only to the augmented matrix of a linear system. On the augmented matrix they correspond to the three operations on equations: add a multiple of one equation to another, interchange two equations, multiply an equation by a nonzero constant.
>
> *Lay: 1.1, Elementary Row Operations*

^def-1-9

> [!definition] Definition §1.10: Row Equivalent
> Two matrices are **row equivalent** if there is a sequence of elementary row operations that transforms one matrix into the other. We write $A \sim B$.
>
> *Lay: 1.1 (text)*

^def-1-10

> [!theorem] Proposition §1.1: Row Operations Are Reversible
> Each elementary row operation can be undone by an elementary row operation of the same type. Consequently, if a sequence of row operations transforms $A$ into $B$, then a sequence of row operations transforms $B$ back into $A$: row equivalence is symmetric.
>
> *Lay: 1.1 (text)*

^prop-1-1

> [!proof]+ Proof
> - If rows $i$ and $j$ are interchanged, interchanging them again restores the original matrix.
> - If row $i$ is scaled by $c \ne 0$, scaling the new row $i$ by $1/c$ (allowed since $1/c \ne 0$) restores it.
> - Suppose $c$ times row $i$ is added to row $j$ ($i \ne j$), so that the new row $j$ is $R_j + cR_i$ and row $i$ is unchanged. Adding $-c$ times row $i$ to the new row $j$ gives $(R_j + cR_i) - cR_i = R_j$, the original row $j$.
>
> If $A = A_0 \to A_1 \to \cdots \to A_k = B$ by row operations, undo them in reverse order: $B = A_k \to A_{k-1} \to \cdots \to A_0 = A$. (Lay leaves the details to Exercises 29–32.)

^pf-1-1

*Uses:* [[§1 Systems of Linear Equations#^def-1-9|Def. §1.9]], [[§1 Systems of Linear Equations#^def-1-10|Def. §1.10]]

> [!theorem] Theorem §1.2: Row-Equivalent Systems Have the Same Solution Set
> If the augmented matrices of two linear systems are row equivalent, then the two systems have the same solution set.
>
> *Lay: 1.1 (text)*

^thm-1-2

> [!proof]+ Proof
> Each row of an augmented matrix stands for one equation. It suffices to treat a single row operation, since a sequence of them can be followed one step at a time. Let $(s_1, \ldots, s_n)$ be a solution of the original system, and look at each type of operation.
> - **Interchange.** The new system has the same equations in a different order, so $(s_1, \ldots, s_n)$ still satisfies all of them.
> - **Scaling.** If equation $i$, $a_1x_1 + \cdots + a_nx_n = b$, is replaced by $ca_1x_1 + \cdots + ca_nx_n = cb$, then substituting gives $c(a_1s_1 + \cdots + a_ns_n) = cb$, which holds because $a_1s_1 + \cdots + a_ns_n = b$.
> - **Replacement.** If equation $j$, $\sum_k a_{jk}x_k = b_j$, is replaced by $\sum_k (a_{jk} + ca_{ik})x_k = b_j + cb_i$, then $\sum_k (a_{jk} + ca_{ik})s_k = \sum_k a_{jk}s_k + c\sum_k a_{ik}s_k = b_j + cb_i$.
>
> In each case the other equations are untouched, so every solution of the original system is a solution of the new one. Conversely, by [[§1 Systems of Linear Equations#^prop-1-1|Proposition §1.1]] the original system is obtained from the new one by row operations, so the same argument shows that every solution of the new system is a solution of the original. The two solution sets are equal.

^pf-1-2

*Uses:* [[§1 Systems of Linear Equations#^prop-1-1|§1.1]], [[§1 Systems of Linear Equations#^def-1-3|Def. §1.3]], [[§1 Systems of Linear Equations#^def-1-9|Def. §1.9]]

> [!example] Example §1.1: Solving a System by Elimination
> **(a)** Solve system (3).
>
> Work on the augmented matrix; each step is the matching operation on the equations.
>
> $$
> \begin{bmatrix} 1 & -2 & 1 & 0 \\ 0 & 2 & -8 & 8 \\ 5 & 0 & -5 & 10 \end{bmatrix}
> \xrightarrow{R_3 - 5R_1}
> \begin{bmatrix} 1 & -2 & 1 & 0 \\ 0 & 2 & -8 & 8 \\ 0 & 10 & -10 & 10 \end{bmatrix}
> \xrightarrow{\frac12 R_2}
> \begin{bmatrix} 1 & -2 & 1 & 0 \\ 0 & 1 & -4 & 4 \\ 0 & 10 & -10 & 10 \end{bmatrix}
> $$
>
> $$
> \xrightarrow{R_3 - 10R_2}
> \begin{bmatrix} 1 & -2 & 1 & 0 \\ 0 & 1 & -4 & 4 \\ 0 & 0 & 30 & -30 \end{bmatrix}
> \xrightarrow{\frac1{30} R_3}
> \begin{bmatrix} 1 & -2 & 1 & 0 \\ 0 & 1 & -4 & 4 \\ 0 & 0 & 1 & -1 \end{bmatrix} .
> $$
>
> The system now has a "triangular" form: $x_3 = -1$, and equations 2 and 1 then determine $x_2$ and $x_1$. So the system is consistent, and the solution is unique. (This is all that Lay's Example 2 asks.) To finish, use $x_3$ in row 3 to clear the $x_3$ terms above it, then $x_2$ in row 2 to clear the $x_2$ term above it:
>
> $$
> \xrightarrow[R_1 - R_3]{R_2 + 4R_3}
> \begin{bmatrix} 1 & -2 & 0 & 1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & -1 \end{bmatrix}
> \xrightarrow{R_1 + 2R_2}
> \begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & -1 \end{bmatrix} .
> $$
>
> The only solution is $(1, 0, -1)$. **Check:** $1 - 2(0) + (-1) = 0$, $2(0) - 8(-1) = 8$, $5(1) - 5(-1) = 10$. Each equation of (3) defines a plane in $\mathbb{R}^3$, and $(1, 0, -1)$ is the one point on all three planes.
>
> **(b)** Solve $x + 2y + 3z = 29$, $x + 3y + 2z = 34$, $3x + 2y + z = 26$.
>
> Subtract equation 1 from equation 2 and $3$ times equation 1 from equation 3:
>
> $$
> x + 2y + 3z = 29, \qquad y - z = 5, \qquad -4y - 8z = 26 - 87 = -61 .
> $$
>
> Now use the second equation to eliminate $y$ from the others ($E_1 - 2E_2$ and $E_3 + 4E_2$):
>
> $$
> x + 5z = 19, \qquad y - z = 5, \qquad -12z = -61 + 20 = -41 .
> $$
>
> So $z = \tfrac{41}{12}$, $y = 5 + \tfrac{41}{12} = \tfrac{101}{12}$, $x = 19 - 5 \cdot \tfrac{41}{12} = \tfrac{228 - 205}{12} = \tfrac{23}{12}$. The three planes meet in the single point $\big(\tfrac{23}{12}, \tfrac{101}{12}, \tfrac{41}{12}\big)$. **Check:** $\tfrac{23 + 202 + 123}{12} = 29$, $\tfrac{23 + 303 + 82}{12} = 34$, $\tfrac{69 + 202 + 41}{12} = 26$.
>
> *The lecture first writes the second reduced equation as $y - z = -5$ (it is $+5$, as the lecture has on the next page), overwrites the signs in front of $z$ and $12z$ in the next system, and later restates the first plane as $x + 2y + 3z = 39$ (it is $29$); with $y - z = 5$ and $-12z = -41$ the solution above checks.*
>
> *Lay: Examples 1.1.1 and 1.1.2*
> *Source: 235 lecture L02*

^ex-1-1

> [!example] Example §1.2: One, None, or Infinitely Many
> Three systems of two equations in two unknowns, one for each possibility.
>
> **(a)** $x + y = 2$, $x - y = 1$. Subtracting the first equation from the second gives $-2y = -1$, so $y = \tfrac12$ and $x = 2 - y = \tfrac32$. The two lines meet in exactly one point, $\big(\tfrac32, \tfrac12\big)$.
>
> **(b)** $x + y = 2$, $x + y = 3$. Subtracting the first equation from the second gives $0 = 1$, which no $(x, y)$ satisfies. The system is inconsistent: the lines are parallel and never meet.
>
> **(c)** $x + y = 2$, $2x + 2y = 4$. Subtracting $2$ times the first equation from the second gives $0 = 0$, so the system is equivalent to the single equation $x + y = 2$. Every point of that line is a solution: infinitely many.
>
> Lay's Figures 1 and 2 show the same three cases with $x_1 - 2x_2 = -1$ and $-x_1 + 3x_2 = 3$ (one solution, $(3, 2)$), $-x_1 + 2x_2 = 3$ (no solution) and $-x_1 + 2x_2 = 1$ (infinitely many).
>
> *Lay: 1.1, Figures 1 and 2*
> *Source: 235 lecture L02*

^ex-1-2

![[m235-1-1.svg]]
*The three systems of [[§1 Systems of Linear Equations#^ex-1-2|Example §1.2]]. Two lines in the plane meet in one point (a), are parallel (b), or coincide (c). Row reduction detects (b) as the equation $0 = 1$ and (c) as the equation $0 = 0$.*

## Existence and Uniqueness Questions

> [!remark] Remark: Two Fundamental Questions About a Linear System
> 1. Is the system consistent; that is, does at least one solution exist?
> 2. If a solution exists, is it the only one; that is, is the solution unique?
>
> These two questions appear throughout the subject in many guises. Row operations on the augmented matrix answer both: bring the matrix to a triangular form, and read off whether a contradiction $0 = b$ ($b \ne 0$) appears and whether every variable is determined. [[§3 Solutions of Linear Systems#^thm-3-1|Theorem §3.1]] makes this precise.

^rem-1-2

> [!example] Example §1.3: An Inconsistent System
> Determine if the following system is consistent:
>
> $$
> \begin{aligned}
> x_2 - 4x_3 &= 8 \\
> 2x_1 - 3x_2 + 2x_3 &= 1 \\
> 4x_1 - 8x_2 + 12x_3 &= 1 .
> \end{aligned}
> $$
>
> To get an $x_1$ in the first equation, interchange rows 1 and 2; then add $-2$ times row 1 to row 3:
>
> $$
> \begin{bmatrix} 0 & 1 & -4 & 8 \\ 2 & -3 & 2 & 1 \\ 4 & -8 & 12 & 1 \end{bmatrix}
> \xrightarrow{R_1 \leftrightarrow R_2}
> \begin{bmatrix} 2 & -3 & 2 & 1 \\ 0 & 1 & -4 & 8 \\ 4 & -8 & 12 & 1 \end{bmatrix}
> \xrightarrow{R_3 - 2R_1}
> \begin{bmatrix} 2 & -3 & 2 & 1 \\ 0 & 1 & -4 & 8 \\ 0 & -2 & 8 & -1 \end{bmatrix} .
> $$
>
> Use the $x_2$ term of row 2 to eliminate the $-2x_2$ in row 3 (add $2$ times row 2 to row 3):
>
> $$
> \begin{bmatrix} 2 & -3 & 2 & 1 \\ 0 & 1 & -4 & 8 \\ 0 & 0 & 0 & 15 \end{bmatrix} ,
> \qquad\text{that is,}\qquad
> \begin{aligned}
> 2x_1 - 3x_2 + 2x_3 &= 1 \\
> x_2 - 4x_3 &= 8 \\
> 0 &= 15 .
> \end{aligned}
> $$
>
> The last equation, $0x_1 + 0x_2 + 0x_3 = 15$, is never true. By [[§1 Systems of Linear Equations#^thm-1-2|Theorem §1.2]] the original system has the same (empty) solution set: it is inconsistent. Geometrically, no point lies on all three planes. A last row of the form $[\,0\ 0\ 0\ \ b\,]$ with $b \ne 0$ is typical of an inconsistent system in triangular form.
>
> *Lay: Example 1.1.3*

^ex-1-3

> [!example] Example §1.4: When Is a System Consistent?
> For what values of $h$ and $k$ is the system
>
> $$
> 2x_1 - x_2 = h, \qquad -6x_1 + 3x_2 = k
> $$
>
> consistent?
>
> Replace the second equation by its sum with $3$ times the first:
>
> $$
> \begin{bmatrix} 2 & -1 & h \\ -6 & 3 & k \end{bmatrix}
> \xrightarrow{R_2 + 3R_1}
> \begin{bmatrix} 2 & -1 & h \\ 0 & 0 & k + 3h \end{bmatrix} .
> $$
>
> The second equation is now $0 = k + 3h$. If $k + 3h \ne 0$ there is no solution. If $k + 3h = 0$ the second equation is $0 = 0$, and every point of the line $2x_1 - x_2 = h$ is a solution. So the system is consistent exactly when $k = -3h$. Geometrically, the two lines are parallel (the second coefficient row is $-3$ times the first), and they coincide exactly when $k = -3h$.
>
> *Lay: 1.1, Practice Problem 4*

^ex-1-4

> [!example] Example §1.5: Back-Substitution in a Triangular System
> Solve the system whose augmented matrix is already in triangular form:
>
> $$
> \begin{bmatrix} 2 & 3 & 1 & 5 \\ 0 & 2 & 1 & 1 \\ 0 & 0 & 1 & -2 \end{bmatrix} ,
> \qquad\text{that is,}\qquad
> \begin{aligned}
> 2x + 3y + z &= 5 \\
> 2y + z &= 1 \\
> z &= -2 .
> \end{aligned}
> $$
>
> Instead of clearing the entries above the diagonal by row operations as in [[§1 Systems of Linear Equations#^ex-1-1|Example §1.1]], substitute from the bottom up (**back-substitution**). The last equation gives $z = -2$. Substituting into the second, $2y = 1 - z = 1 + 2 = 3$, so $y = \tfrac32$. Substituting both into the first, $2x = 5 - 3y - z = 5 - \tfrac92 + 2 = \tfrac52$, so $x = \tfrac54$. The solution is $\big(\tfrac54, \tfrac32, -2\big)$. **Check:** $2 \cdot \tfrac54 + 3 \cdot \tfrac32 - 2 = \tfrac52 + \tfrac92 - 2 = 5$ and $2 \cdot \tfrac32 - 2 = 1$.
>
> This also answers both fundamental questions at once, as in Lay's Example 2: each diagonal coefficient ($2$, $2$, $1$) is nonzero, so each equation determines its variable from the ones below it, a solution exists, and it is unique.
>
> *Source: 235 lecture L1*

^ex-1-5

> [!remark]- Remark: Numerical Note — Floating Point Arithmetic
> In real-world problems linear systems are solved by computer. For a square coefficient matrix, programs nearly always use the elimination algorithm of this section and [[§2 Row Reduction and Echelon Forms|§2]], slightly modified for accuracy. They work in floating point arithmetic: numbers are stored as $\pm .d_1 \cdots d_p \times 10^r$ with $p$ usually between 8 and 16 digits, so results are rounded, and even entering $1/3$ introduces a **roundoff error**. Such inaccuracies seldom cause problems.

^rem-1-3
