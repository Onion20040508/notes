---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 1
section: 3
lay: "1.2"
aliases: ["Lay 1.2 (cont.)"]
tags: [applied-linear-algebra, math235]
---
← [[§2 Row Reduction and Echelon Forms]] · ↑ [[· 1 Linear Equations in Linear Algebra]] · [[§4 Vector Equations]] →

*Lay, Section 1.2 and Appendix A · MATH 235 lectures L1, L2.*

Pivots answer the two fundamental questions at once. A system is consistent exactly when the last column of its augmented matrix is not a pivot column, and a consistent system has a unique solution exactly when there are no free variables. Otherwise the free variables parametrize the infinitely many solutions.

## Solutions of Linear Systems

Applied to the augmented matrix of a linear system, row reduction describes the solution set explicitly. For example, if the augmented matrix has been reduced to
$$
\begin{bmatrix} 1 & 0 & -5 & 1 \\ 0 & 1 & 1 & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix},
\qquad\text{the system is}\qquad
\begin{aligned} x_1 - 5x_3 &= 1 \\ x_2 + x_3 &= 4 \\ 0 &= 0 . \end{aligned}
$$

> [!definition] Definition §3.1: Basic Variables and Free Variables
> In a linear system, the variables corresponding to pivot columns of the coefficient matrix are **basic variables** (some texts say *leading variables*). The other variables are **free variables**.
>
> In the system above, $x_1$ and $x_2$ are basic and $x_3$ is free. Solving the reduced equations for the basic variables gives
>
> $$
> x_1 = 1 + 5x_3, \qquad x_2 = 4 - x_3, \qquad x_3 \text{ is free.}
> $$
>
> "$x_3$ is free" means that any value may be chosen for $x_3$; the formulas then determine $x_1$ and $x_2$. For $x_3 = 0$ the solution is $(1, 4, 0)$, for $x_3 = 1$ it is $(6, 3, 1)$. Each choice of $x_3$ gives a different solution, and every solution arises from a choice of $x_3$. This works because the reduced echelon form places each basic variable in one and only one equation.
>
> *Lay: 1.2 (text)*

^def-3-1

> [!definition] Definition §3.2: Parametric Description of a Solution Set
> A description of the solution set in which the free variables act as parameters, such as the formulas above, is a **parametric description** of the solution set, also called the **general solution** of the system. *Solving a system* means finding a parametric description of the solution set or determining that the solution set is empty.
>
> A consistent system with free variables has many parametric descriptions. (Adding $5$ times the second equation above to the first gives $x_1 + 5x_2 = 21$, $x_2 + x_3 = 4$, and $x_2$ could serve as the parameter.) The convention is always to use the free variables as the parameters. An inconsistent system has an empty solution set, even if it has free variables, and so has no parametric description.
>
> *Lay: 1.2 (text)*

^def-3-2

> [!example] Example §3.1: A General Solution
> Find the general solution of the linear system whose augmented matrix has been reduced to
>
> $$
> \begin{bmatrix} 1 & 6 & 2 & -5 & -2 & -4 \\ 0 & 0 & 2 & -8 & -1 & 3 \\ 0 & 0 & 0 & 0 & 1 & 7 \end{bmatrix} .
> $$
>
> The matrix is in echelon form; complete the reduction before solving. Add $2$ times row 3 to row 1 and row 3 to row 2; scale row 2 by $\tfrac12$; add $-2$ times row 2 to row 1:
>
> $$
> \sim
> \begin{bmatrix} 1 & 6 & 2 & -5 & 0 & 10 \\ 0 & 0 & 2 & -8 & 0 & 10 \\ 0 & 0 & 0 & 0 & 1 & 7 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 6 & 2 & -5 & 0 & 10 \\ 0 & 0 & 1 & -4 & 0 & 5 \\ 0 & 0 & 0 & 0 & 1 & 7 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 6 & 0 & 3 & 0 & 0 \\ 0 & 0 & 1 & -4 & 0 & 5 \\ 0 & 0 & 0 & 0 & 1 & 7 \end{bmatrix} .
> $$
>
> There are five variables (six columns). The system is now
>
> $$
> x_1 + 6x_2 + 3x_4 = 0, \qquad x_3 - 4x_4 = 5, \qquad x_5 = 7 .
> $$
>
> The pivot columns are 1, 3 and 5, so $x_1, x_3, x_5$ are basic and $x_2, x_4$ are free. The general solution is
>
> $$
> x_1 = -6x_2 - 3x_4, \qquad x_2 \text{ free}, \qquad x_3 = 5 + 4x_4, \qquad x_4 \text{ free}, \qquad x_5 = 7 .
> $$
>
> The value of $x_5$ is fixed by the third equation.
>
> *Lay: Example 1.2.4*

^ex-3-1

> [!remark]- Remark: Back-Substitution
> A computer solves a system in echelon form, such as
>
> $$
> x_1 - 7x_2 + 2x_3 - 5x_4 + 8x_5 = 10, \qquad x_2 - 3x_3 + 3x_4 + x_5 = -5, \qquad x_4 - x_5 = 4,
> $$
>
> by **back-substitution**: solve the last equation for $x_4$ in terms of $x_5$, substitute into the second and solve for $x_2$, then substitute both into the first and solve for $x_1$ (a small case by hand: [[§1 Systems of Linear Equations#^ex-1-5|Example §1.5]]). The matrix form of the backward phase uses the same number of arithmetic operations, and its discipline makes errors less likely in hand computation. Best strategy by hand: solve from the *reduced* echelon form only.

^rem-3-1
## Existence and Uniqueness Questions

A nonreduced echelon form is a poor tool for solving a system, but it is just right for the two fundamental questions of [[§1 Systems of Linear Equations#^rem-1-2|§1]].

> [!theorem] Theorem §3.1: Existence and Uniqueness Theorem
> A linear system is consistent if and only if the rightmost column of the augmented matrix is *not* a pivot column, that is, if and only if an echelon form of the augmented matrix has *no* row of the form
>
> $$
> [\,0\ \ \cdots\ \ 0\ \ b\,] \qquad \text{with } b \text{ nonzero.}
> $$
>
> If a linear system is consistent, then the solution set contains either:
> - (i) a unique solution, when there are no free variables;
> - (ii) infinitely many solutions, when there is at least one free variable.
>
> *Lay: Theorem 2 (1.2)*

^thm-3-1

> [!proof]+ Proof
> **The two forms of the condition agree.** In an echelon form of the augmented matrix, the pivot positions are the positions of the leading entries ([[§2 Row Reduction and Echelon Forms#^cor-2-2|Corollary §2.2]]). The rightmost column contains a pivot position exactly when some row has its leading entry in the last column, that is, when some row is $[\,0\ \cdots\ 0\ \ b\,]$ with $b \ne 0$.
>
> **Such a row makes the system inconsistent.** It stands for the equation $0x_1 + \cdots + 0x_n = b$, which no list of numbers satisfies. By [[§1 Systems of Linear Equations#^thm-1-2|Theorem §1.2]], the original system has the same (empty) solution set.
>
> **Otherwise the system is consistent.** Suppose there is no such row, and pass to the reduced echelon form (still without such a row). Every nonzero row then has its leading $1$ in a coefficient column, so every nonzero equation contains exactly one basic variable with coefficient $1$, and that basic variable appears in no other equation. Zero rows say $0 = 0$. Choose any values for the free variables (say all $0$) and solve each nonzero equation for its basic variable. This gives a solution of the reduced system, hence of the original one ([[§1 Systems of Linear Equations#^thm-1-2|Theorem §1.2]]).
>
> **Counting the solutions.** Let the system be consistent, with reduced system as above. Each solution is determined by the values of the free variables, since the equations express every basic variable in terms of them (a basic variable equals a constant when its equation contains no free variable). If there are no free variables, the reduced system reads $x_i = d_i$ for every $i$, and the solution is unique. If $x_j$ is free, then every real value of $x_j$ (with the other free variables, say, $0$) gives a solution, and different values give solutions that differ in the $j$th entry. So there are infinitely many solutions.

^pf-3-1

*Uses:* [[§1 Systems of Linear Equations#^thm-1-2|§1.2]], [[§2 Row Reduction and Echelon Forms#^cor-2-2|§2.2]], [[§3 Solutions of Linear Systems#^def-3-1|Def. §3.1]]

> [!remark]- Connections
> - Axler gets the two counting consequences by dimension, without row reduction: a homogeneous system with more variables than equations has a nonzero solution ([[§8 Null Spaces and Ranges#^ladr-3-26|LADR 3.26]]), and a system with more equations than variables is inconsistent for some right-hand side ([[§8 Null Spaces and Ranges#^ladr-3-28|LADR 3.28]]). In Lay's language both are pivot counts: more columns than rows forces a free variable ([[§8 Linear Independence#^thm-8-6|Theorem §8.6]]), more rows than columns leaves a row without a pivot ([[§5 The Matrix Equation Ax = b#^thm-5-3|Theorem §5.3]]).

> [!theorem] Corollary §3.2: No Solution, One Solution, or Infinitely Many
> A system of linear equations has
> 1. no solution, or
> 2. exactly one solution, or
> 3. infinitely many solutions.
>
> *Lay: 1.1 (text; verified in 1.2)*

^cor-3-2

> [!proof]+ Proof
> If the system is inconsistent, it has no solution. If it is consistent, [[§3 Solutions of Linear Systems#^thm-3-1|Theorem §3.1]] says that it has exactly one solution (no free variables) or infinitely many (at least one free variable).

^pf-3-2

*Uses:* [[§3 Solutions of Linear Systems#^thm-3-1|§3.1]]

The lecture's shorthand for the count: a consistent system has "$\infty^{k}$" solutions, $k$ the number of free variables, i.e. of nonpivot columns of the coefficient matrix, with $\infty^0 = 1$ ([[§1 Systems of Linear Equations#^rem-1-1|§1, Remark]]). A unique solution shows in the reduced echelon form as an identity block followed by zero rows, with the solution in the last column.

> [!remark] Remark: Method — Using Row Reduction to Solve a Linear System
> 1. Write the augmented matrix of the system.
> 2. Use the row reduction algorithm to obtain an equivalent augmented matrix in echelon form. Decide whether the system is consistent (look for a "bad row" $[\,0\ \cdots\ 0\ \ b\,]$, $b \ne 0$). If there is no solution, stop; otherwise, go on.
> 3. Continue row reduction to obtain the reduced echelon form.
> 4. Write the system of equations corresponding to the matrix obtained in step 3.
> 5. Rewrite each nonzero equation from step 4 so that its one basic variable is expressed in terms of any free variables appearing in the equation.

^rem-3-2
> [!example] Example §3.2: Five Unknowns, Two Free Variables
> Solve
>
> $$
> \begin{aligned}
> 2x_1 + 4x_2 - 2x_3 + 2x_4 + 4x_5 &= 2 \\
> x_1 + 2x_2 - x_3 + 2x_4 \phantom{{}+ 4x_5} &= 4 \\
> 3x_1 + 6x_2 - 2x_3 + x_4 + 9x_5 &= 1 \\
> 5x_1 + 10x_2 - 4x_3 + 5x_4 + 9x_5 &= 9 .
> \end{aligned}
> $$
>
> **Forward phase.** Divide row 1 by $2$, then clear column 1 ($R_2 - R_1$, $R_3 - 3R_1$, $R_4 - 5R_1$):
>
> $$
> \begin{bmatrix} 1 & 2 & -1 & 1 & 2 & 1 \\ 1 & 2 & -1 & 2 & 0 & 4 \\ 3 & 6 & -2 & 1 & 9 & 1 \\ 5 & 10 & -4 & 5 & 9 & 9 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 2 & -1 & 1 & 2 & 1 \\ 0 & 0 & 0 & 1 & -2 & 3 \\ 0 & 0 & 1 & -2 & 3 & -2 \\ 0 & 0 & 1 & 0 & -1 & 4 \end{bmatrix} .
> $$
>
> Column 2 has no pivot (all entries below row 1 are $0$). Swap rows 2 and 3 to get a pivot in column 3, then $R_4 - R_2$ gives $[\,0\ 0\ 0\ 2\ {-4}\ 6\,]$, and $R_4 - 2R_3$ gives a zero row:
>
> $$
> \sim
> \begin{bmatrix} 1 & 2 & -1 & 1 & 2 & 1 \\ 0 & 0 & 1 & -2 & 3 & -2 \\ 0 & 0 & 0 & 1 & -2 & 3 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> This echelon form already answers the questions: no bad row, so the system is consistent; columns 2 and 5 have no pivot, so $x_2$ and $x_5$ are free and there are infinitely many ("$\infty^2$") solutions.
>
> **Backward phase.** $R_2 + 2R_3$ gives $[\,0\ 0\ 1\ 0\ {-1}\ 4\,]$; $R_1 - R_3$ gives $[\,1\ 2\ {-1}\ 0\ 4\ {-2}\,]$; then $R_1 + R_2$:
>
> $$
> \begin{bmatrix} 1 & 2 & 0 & 0 & 3 & 2 \\ 0 & 0 & 1 & 0 & -1 & 4 \\ 0 & 0 & 0 & 1 & -2 & 3 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> **Parametric form.** The pivot variables are $x_1, x_3, x_4$. Set the free variables to parameters, $x_2 = t$, $x_5 = r$ ($t, r$ any numbers), and express the pivot variables through them:
>
> $$
> \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{bmatrix}
> = \begin{bmatrix} 2 - 2t - 3r \\ t \\ 4 + r \\ 3 + 2r \\ r \end{bmatrix}
> = \begin{bmatrix} 2 \\ 0 \\ 4 \\ 3 \\ 0 \end{bmatrix}
> + t \begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}
> + r \begin{bmatrix} -3 \\ 0 \\ 1 \\ 2 \\ 1 \end{bmatrix} .
> $$
>
> (Vector notation is introduced in [[§4 Vector Equations|§4]]; this is the "parametric vector form" of [[§6 Solution Sets of Linear Systems#^def-6-2|Definition §6.2]].) **Check:** $(2, 0, 4, 3, 0)$ gives $4 - 8 + 6 = 2$, $2 - 4 + 6 = 4$, $6 - 8 + 3 = 1$, $10 - 16 + 15 = 9$; and both direction vectors make every left side $0$ (for instance $(-3, 0, 1, 2, 1)$ in equation 3: $-9 - 2 + 2 + 9 = 0$).
>
> *In the L2 version the first row keeps the right-hand side $2$ after division by $2$ (it should be $1$), so some intermediate matrices there are off; the reduced echelon form and the parametric solution in both lectures are the ones above.*
>
> *Source: 235 lectures L1 and L2*

^ex-3-2
