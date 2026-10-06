---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 1
section: 5
lay: "1.5"
aliases: ["Lay 1.5"]
tags: [applied-linear-algebra, math235]
---
← [[§4 The Matrix Equation Ax = b]] · ↑ [[· 1 Linear Equations in Linear Algebra]] · [[§6 Applications of Linear Systems]] →

*Lay, Section 1.5 · MATH 235 lectures L2, L3.*

Vector notation turns the general solution of a linear system into a geometric object. The solutions of a homogeneous system $A\mathbf{x} = \mathbf{0}$ always form a span: a point, a line or a plane through the origin, or a higher-dimensional analogue. It is written in *parametric vector form*, with one vector for each free variable. The solutions of a consistent system $A\mathbf{x} = \mathbf{b}$ form a translate of that set: one particular solution $\mathbf{p}$ plus all solutions of $A\mathbf{x} = \mathbf{0}$, a line or plane parallel to the homogeneous one.

## Homogeneous Linear Systems

> [!definition] Definition §5.1: Homogeneous System, Trivial and Nontrivial Solutions
> A system of linear equations is **homogeneous** if it can be written in the form $A\mathbf{x} = \mathbf{0}$, where $A$ is an $m \times n$ matrix and $\mathbf{0}$ is the zero vector in $\mathbb{R}^m$. Such a system always has the solution $\mathbf{x} = \mathbf{0}$ (the zero vector in $\mathbb{R}^n$), the **trivial solution**. A **nontrivial solution** is a nonzero vector $\mathbf{x}$ that satisfies $A\mathbf{x} = \mathbf{0}$. (It may have some zero entries, as long as not all of its entries are zero.)
>
> *Lay: 1.5 (text)*

^def-5-1

> [!theorem] Corollary §5.1: Nontrivial Solutions and Free Variables
> The homogeneous equation $A\mathbf{x} = \mathbf{0}$ has a nontrivial solution if and only if the equation has at least one free variable.
>
> *Lay: 1.5, boxed statement*

^cor-5-1

> [!proof]+ Proof
> $A\mathbf{x} = \mathbf{0}$ is consistent, since $\mathbf{x} = \mathbf{0}$ is a solution. By the [[§2 Row Reduction and Echelon Forms#^thm-2-3|Existence and Uniqueness Theorem]], a consistent system has a unique solution (here: only the trivial one) when there are no free variables, and infinitely many solutions, in particular nonzero ones, when there is at least one free variable.

^pf-5-1

*Uses:* [[§2 Row Reduction and Echelon Forms#^thm-2-3|§2.3]], [[§5 Solution Sets of Linear Systems#^def-5-1|Def. §5.1]]

> [!example] Example §5.1: A Line of Solutions
> Determine if the homogeneous system
>
> $$
> 3x_1 + 5x_2 - 4x_3 = 0, \qquad -3x_1 - 2x_2 + 4x_3 = 0, \qquad 6x_1 + x_2 - 8x_3 = 0
> $$
>
> has a nontrivial solution, and describe the solution set.
>
> Row reduce $[\,A\ \ \mathbf{0}\,]$ ($R_2 + R_1$, $R_3 - 2R_1$, then $R_3 + 3R_2$):
>
> $$
> \begin{bmatrix} 3 & 5 & -4 & 0 \\ -3 & -2 & 4 & 0 \\ 6 & 1 & -8 & 0 \end{bmatrix}
> \sim
> \begin{bmatrix} 3 & 5 & -4 & 0 \\ 0 & 3 & 0 & 0 \\ 0 & -9 & 0 & 0 \end{bmatrix}
> \sim
> \begin{bmatrix} 3 & 5 & -4 & 0 \\ 0 & 3 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> $x_3$ is free, so there are nontrivial solutions, one for each choice of $x_3$ (Corollary §5.1). Continue to the reduced echelon form ($\tfrac13 R_2$, $R_1 - 5R_2$, $\tfrac13 R_1$):
>
> $$
> \begin{bmatrix} 1 & 0 & -\tfrac43 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix},
> \qquad x_1 - \tfrac43 x_3 = 0, \quad x_2 = 0 .
> $$
>
> So $x_1 = \tfrac43 x_3$, $x_2 = 0$, $x_3$ free, and
>
> $$
> \mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} \tfrac43 x_3 \\ 0 \\ x_3 \end{bmatrix} = x_3\begin{bmatrix} \tfrac43 \\ 0 \\ 1 \end{bmatrix} = x_3\mathbf{v} .
> $$
>
> Every solution is a multiple of $\mathbf{v}$; the trivial solution is $x_3 = 0$. The solution set is $\operatorname{Span}\{\mathbf{v}\}$, a line through $\mathbf{0}$ in $\mathbb{R}^3$. **Check:** $3 \cdot \tfrac43 - 4 = 0$, $-3 \cdot \tfrac43 + 4 = 0$, $6 \cdot \tfrac43 - 8 = 0$.
>
> The lecture's version: for $A = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{bmatrix}$, $R_1 - 2R_2$ gives $\begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{bmatrix}$, so $x_3 = t$ is free, $x_1 = t$, $x_2 = -2t$, and the solution set is the line $\operatorname{Span}\{(1, -2, 1)\}$.
>
> *Lay: Example 1.5.1*
> *Source: 235 lecture L3*

^ex-5-1

> [!example] Example §5.2: A Plane of Solutions
> Describe all solutions of the single homogeneous equation
>
> $$
> 10x_1 - 3x_2 - 2x_3 = 0 . \qquad (1)
> $$
>
> No matrix notation is needed: $x_1$ is basic and $x_2, x_3$ are free, with $x_1 = .3x_2 + .2x_3$. As a vector,
>
> $$
> \mathbf{x} = \begin{bmatrix} .3x_2 + .2x_3 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} .3x_2 \\ x_2 \\ 0 \end{bmatrix} + \begin{bmatrix} .2x_3 \\ 0 \\ x_3 \end{bmatrix}
> = x_2\underbrace{\begin{bmatrix} .3 \\ 1 \\ 0 \end{bmatrix}}_{\mathbf{u}} + x_3\underbrace{\begin{bmatrix} .2 \\ 0 \\ 1 \end{bmatrix}}_{\mathbf{v}} \qquad (x_2, x_3 \text{ free}). \qquad (2)
> $$
>
> Every solution is a linear combination of $\mathbf{u}$ and $\mathbf{v}$: the solution set is $\operatorname{Span}\{\mathbf{u}, \mathbf{v}\}$. Neither vector is a multiple of the other, so it is a plane through the origin. **Check:** $10(.3) - 3 = 0$ and $10(.2) - 2 = 0$.
>
> *Lay: Example 1.5.2*

^ex-5-2

> [!theorem] Proposition §5.2: The Solution Set of Ax = 0 Is a Span
> (a) If $\mathbf{x}$ and $\mathbf{y}$ are solutions of $A\mathbf{x} = \mathbf{0}$ and $c$ is a scalar, then $\mathbf{x} + \mathbf{y}$ and $c\mathbf{x}$ are solutions.
>
> (b) The solution set of $A\mathbf{x} = \mathbf{0}$ can always be written as $\operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ for suitable vectors $\mathbf{v}_1, \ldots, \mathbf{v}_p$, one for each free variable ($\operatorname{Span}\{\mathbf{0}\}$ if there are none).
>
> *Lay: 1.5 (text)*
> *Source: 235 lecture L3*

^prop-5-2

> [!proof]+ Proof
> (a) By [[§4 The Matrix Equation Ax = b#^thm-4-5|Theorem §4.5]], $A(\mathbf{x} + \mathbf{y}) = A\mathbf{x} + A\mathbf{y} = \mathbf{0} + \mathbf{0} = \mathbf{0}$ and $A(c\mathbf{x}) = c(A\mathbf{x}) = c\mathbf{0} = \mathbf{0}$.
>
> (b) (Lay illustrates this with Examples 1 and 2; in general:) Row reduce $[\,A\ \ \mathbf{0}\,]$ to reduced echelon form; the last column stays zero. Let the free variables be $x_{j_1}, \ldots, x_{j_p}$. Each nonzero row gives an equation expressing one basic variable as a combination of free variables, with no constant term. So every solution has the form $\mathbf{x} = x_{j_1}\mathbf{v}_1 + \cdots + x_{j_p}\mathbf{v}_p$, where $\mathbf{v}_k$ is the solution obtained by setting $x_{j_k} = 1$ and the other free variables to $0$. Conversely, each such combination is a solution, by (a) (or because any values of the free variables give a solution). If $p = 0$, the only solution is $\mathbf{0}$, and the solution set is $\{\mathbf{0}\} = \operatorname{Span}\{\mathbf{0}\}$.

^pf-5-2

*Uses:* [[§4 The Matrix Equation Ax = b#^thm-4-5|§4.5]], [[§2 Row Reduction and Echelon Forms#^def-2-4|Def. §2.4]], [[§3 Vector Equations#^def-3-4|Def. §3.4]]

One free variable gives a line through the origin (Example §5.1); two or more give a plane through the origin as a good mental image (Example §5.2). The same picture serves for $\operatorname{Span}\{\mathbf{u}, \mathbf{v}\}$ in general ([[§3 Vector Equations#^rem-3-2|§3, Remark]]). The solution set of $A\mathbf{x} = \mathbf{0}$ is the null space of $A$ ([[§18 Subspaces of ℝⁿ#^def-18-3|Definition §18.3]]).

## Parametric Vector Form

> [!definition] Definition §5.2: Parametric Vector Form
> Equation (1) is an **implicit description** of its plane; solving it gives an **explicit description** of the plane as the span of $\mathbf{u}$ and $\mathbf{v}$. Equation (2) is a **parametric vector equation** of the plane, also written
>
> $$
> \mathbf{x} = s\mathbf{u} + t\mathbf{v} \qquad (s, t \in \mathbb{R})
> $$
>
> to stress that the parameters range over all real numbers. In Example §5.1, $\mathbf{x} = x_3\mathbf{v}$ (or $\mathbf{x} = t\mathbf{v}$, $t \in \mathbb{R}$) is a parametric vector equation of a line. Whenever a solution set is described explicitly with vectors in this way, the solution is in **parametric vector form**.
>
> *Lay: 1.5 (text)*

^def-5-2

## Solutions of Nonhomogeneous Systems

> [!example] Example §5.3: A Translated Line
> Describe all solutions of $A\mathbf{x} = \mathbf{b}$, where
>
> $$
> A = \begin{bmatrix} 3 & 5 & -4 \\ -3 & -2 & 4 \\ 6 & 1 & -8 \end{bmatrix}, \qquad \mathbf{b} = \begin{bmatrix} 7 \\ -1 \\ -4 \end{bmatrix} .
> $$
>
> $A$ is the coefficient matrix of Example §5.1. The same row operations ($R_2 + R_1$ gives $[\,0\ 3\ 0\ 6\,]$; $R_3 - 2R_1$ gives $[\,0\ {-9}\ 0\ {-18}\,]$; $R_3 + 3R_2$ gives a zero row; then $\tfrac13 R_2 = [\,0\ 1\ 0\ 2\,]$, $R_1 - 5R_2 = [\,3\ 0\ {-4}\ {-3}\,]$, $\tfrac13 R_1$) give
>
> $$
> \begin{bmatrix} 3 & 5 & -4 & 7 \\ -3 & -2 & 4 & -1 \\ 6 & 1 & -8 & -4 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 0 & -\tfrac43 & -1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix},
> \qquad x_1 - \tfrac43 x_3 = -1, \quad x_2 = 2 .
> $$
>
> So $x_1 = -1 + \tfrac43 x_3$, $x_2 = 2$, $x_3$ free:
>
> $$
> \mathbf{x} = \begin{bmatrix} -1 + \tfrac43 x_3 \\ 2 \\ x_3 \end{bmatrix} = \begin{bmatrix} -1 \\ 2 \\ 0 \end{bmatrix} + \begin{bmatrix} \tfrac43 x_3 \\ 0 \\ x_3 \end{bmatrix} = \underbrace{\begin{bmatrix} -1 \\ 2 \\ 0 \end{bmatrix}}_{\mathbf{p}} + x_3\underbrace{\begin{bmatrix} \tfrac43 \\ 0 \\ 1 \end{bmatrix}}_{\mathbf{v}} .
> $$
>
> In parametric vector form, $\mathbf{x} = \mathbf{p} + t\mathbf{v}$ ($t \in \mathbb{R}$) (3), while the solutions of $A\mathbf{x} = \mathbf{0}$ are $\mathbf{x} = t\mathbf{v}$ (4), with the *same* $\mathbf{v}$. The solutions of $A\mathbf{x} = \mathbf{b}$ are obtained by adding $\mathbf{p}$ to the solutions of $A\mathbf{x} = \mathbf{0}$; $\mathbf{p}$ itself is one particular solution ($t = 0$). **Check:** $3(-1) + 5(2) = 7$, $-3(-1) - 2(2) = -1$, $6(-1) + 2 = -4$.
>
> *Lay: Example 1.5.3*

^ex-5-3

Geometrically, adding $\mathbf{p}$ to $\mathbf{v}$ *translates* $\mathbf{v}$ to $\mathbf{v} + \mathbf{p}$: it moves $\mathbf{v}$ in a direction parallel to the line through $\mathbf{p}$ and $\mathbf{0}$. Translating every point of a line $L$ by $\mathbf{p}$ gives a line parallel to $L$. Equation (3) is **the equation of the line through $\mathbf{p}$ parallel to $\mathbf{v}$**. So the solution set of $A\mathbf{x} = \mathbf{b}$ in Example §5.3 is a line through $\mathbf{p}$ parallel to the solution set of $A\mathbf{x} = \mathbf{0}$.

![[m235-5-1.svg]]
*Parallel solution sets. The solutions $t\mathbf{v}$ of $A\mathbf{x} = \mathbf{0}$ form a line through $\mathbf{0}$; adding one particular solution $\mathbf{p}$ of $A\mathbf{x} = \mathbf{b}$ to each of them (dashed) gives all solutions $\mathbf{p} + t\mathbf{v}$ of $A\mathbf{x} = \mathbf{b}$, the parallel line through $\mathbf{p}$.*

> [!theorem] Theorem §5.3: Solutions of Ax = b Are a Translate of the Solutions of Ax = 0
> Suppose the equation $A\mathbf{x} = \mathbf{b}$ is consistent for some given $\mathbf{b}$, and let $\mathbf{p}$ be a solution. Then the solution set of $A\mathbf{x} = \mathbf{b}$ is the set of all vectors of the form $\mathbf{w} = \mathbf{p} + \mathbf{v}_h$, where $\mathbf{v}_h$ is any solution of the homogeneous equation $A\mathbf{x} = \mathbf{0}$.
>
> *Lay: Theorem 6 (1.5)*

^thm-5-3

> [!proof]+ Proof
> Lay proves the first inclusion in the solution to Practice Problem 3 and leaves the second to Exercise 25 (written out here). Both follow from [[§4 The Matrix Equation Ax = b#^thm-4-5|Theorem §4.5]].
> - If $A\mathbf{v}_h = \mathbf{0}$ and $\mathbf{w} = \mathbf{p} + \mathbf{v}_h$, then $A\mathbf{w} = A\mathbf{p} + A\mathbf{v}_h = \mathbf{b} + \mathbf{0} = \mathbf{b}$. So every vector of the form $\mathbf{p} + \mathbf{v}_h$ is a solution.
> - Conversely, let $\mathbf{w}$ be any solution of $A\mathbf{x} = \mathbf{b}$ and put $\mathbf{v}_h = \mathbf{w} - \mathbf{p}$. Then $A\mathbf{v}_h = A\mathbf{w} - A\mathbf{p} = \mathbf{b} - \mathbf{b} = \mathbf{0}$, so $\mathbf{v}_h$ solves the homogeneous equation and $\mathbf{w} = \mathbf{p} + \mathbf{v}_h$ has the stated form.

^pf-5-3

*Uses:* [[§4 The Matrix Equation Ax = b#^thm-4-5|§4.5]]

> [!remark]- Connections
> - Rigorous treatment: the solution set is the translate $\mathbf{p} + \operatorname{Nul} A$ of a subspace, [[§11 Products and Quotients of Vector Spaces#^ladr-3-97|LADR 3.97]]; Axler shows that two translates of a subspace are equal or disjoint and makes them the points of the quotient space $V/U$. In group language $\mathbf{p} + \operatorname{Nul} A$ is a coset of $\operatorname{Nul} A$ in $(\mathbb{R}^n, +)$, [[§28 Left and Right Cosets#^def-28-2|493 Def. §28.2]].
> - The line $\mathbf{x} = \mathbf{p} + t\mathbf{v}$ is Stewart's vector equation of a line, [[§84 Equations of Lines and Planes#^thm-84-1|Calc Thm. §84.1]].
> - See also: the same structure for linear differential equations, general solution = solution of the homogeneous equation + one particular solution: [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-2|331 Thm. §17.2]] (for $ay'' + by' + cy = g$) and [[§35★ Nonhomogeneous Linear Systems#^thm-35-1|331 Thm. §35.1]] (for systems $\mathbf{x}' = P(t)\mathbf{x} + \mathbf{g}$).

So if $A\mathbf{x} = \mathbf{b}$ has a solution, its solution set is the solution set of $A\mathbf{x} = \mathbf{0}$ translated by *any* particular solution $\mathbf{p}$. With two free variables it is a plane parallel to the plane of homogeneous solutions. Even for $n > 3$, the mental image of the solution set of a consistent system $A\mathbf{x} = \mathbf{b}$ with $\mathbf{b} \ne \mathbf{0}$ is a single nonzero point, or a line or plane not passing through the origin. *Warning:* Theorem §5.3 applies only to an equation $A\mathbf{x} = \mathbf{b}$ that has at least one solution $\mathbf{p}$; when $A\mathbf{x} = \mathbf{b}$ has no solution, the solution set is empty.

> [!remark] Remark: Method — Writing a Solution Set (of a Consistent System) in Parametric Vector Form
> 1. Row reduce the augmented matrix to reduced echelon form.
> 2. Express each basic variable in terms of any free variables appearing in an equation.
> 3. Write a typical solution $\mathbf{x}$ as a vector whose entries depend on the free variables, if any.
> 4. Decompose $\mathbf{x}$ into a linear combination of vectors (with numeric entries) using the free variables as parameters.
>
> The constant vector in step 4 is a particular solution $\mathbf{p}$; the vectors multiplying the free variables span the solution set of $A\mathbf{x} = \mathbf{0}$ (Theorem §5.3). [[§2 Row Reduction and Echelon Forms#^ex-2-5|Example §2.5]] is a five-variable instance.

^rem-5-1

> [!example] Example §5.4: Two Planes, and a Plane Not Through the Origin
> **(a)** Each equation $x_1 + 4x_2 - 5x_3 = 0$, $2x_1 - x_2 + 8x_3 = 9$ determines a plane in $\mathbb{R}^3$. Do the planes intersect? If so, describe the intersection.
>
> Row reduce ($R_2 - 2R_1$, $-\tfrac19 R_2$, $R_1 - 4R_2$):
>
> $$
> \begin{bmatrix} 1 & 4 & -5 & 0 \\ 2 & -1 & 8 & 9 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 4 & -5 & 0 \\ 0 & -9 & 18 & 9 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 4 & -5 & 0 \\ 0 & 1 & -2 & -1 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 0 & 3 & 4 \\ 0 & 1 & -2 & -1 \end{bmatrix} .
> $$
>
> So $x_1 = 4 - 3x_3$, $x_2 = -1 + 2x_3$, $x_3$ free, and
>
> $$
> \mathbf{x} = \begin{bmatrix} 4 \\ -1 \\ 0 \end{bmatrix} + x_3\begin{bmatrix} -3 \\ 2 \\ 1 \end{bmatrix} .
> $$
>
> The planes intersect in the line through $\mathbf{p} = (4, -1, 0)$ in the direction $\mathbf{v} = (-3, 2, 1)$. **Check:** $\mathbf{p}$: $4 - 4 = 0$, $8 + 1 = 9$; $\mathbf{v}$: $-3 + 8 - 5 = 0$, $-6 - 2 + 8 = 0$.
>
> **(b)** Write the general solution of $10x_1 - 3x_2 - 2x_3 = 7$ in parametric vector form and compare with Example §5.2.
>
> $x_1 = .7 + .3x_2 + .2x_3$ with $x_2, x_3$ free, so
>
> $$
> \mathbf{x} = \begin{bmatrix} .7 \\ 0 \\ 0 \end{bmatrix} + x_2\begin{bmatrix} .3 \\ 1 \\ 0 \end{bmatrix} + x_3\begin{bmatrix} .2 \\ 0 \\ 1 \end{bmatrix} = \mathbf{p} + x_2\mathbf{u} + x_3\mathbf{v} .
> $$
>
> The solution set is the plane through $\mathbf{p} = (.7, 0, 0)$ parallel to the plane $\operatorname{Span}\{\mathbf{u}, \mathbf{v}\}$ of Example §5.2, as Theorem §5.3 predicts.
>
> *Lay: 1.5, Practice Problems 1 and 2*

^ex-5-4
