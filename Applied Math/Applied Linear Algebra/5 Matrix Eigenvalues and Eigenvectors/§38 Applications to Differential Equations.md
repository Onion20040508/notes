---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 5
section: 38
lay: "5.7"
aliases: ["Lay 5.7"]
tags: [applied-linear-algebra, math235]
---
← [[§37 Discrete Dynamical Systems]] · ↑ [[· 5 Matrix Eigenvalues and Eigenvectors]] · [[§39 Iterative Estimates for Eigenvalues]] →

*Lay, Section 5.7.*

This section is the continuous analogue of [[§37 Discrete Dynamical Systems|§37]]. A system of linear differential equations $\mathbf{x}'(t) = A\mathbf{x}(t)$ with constant coefficients is solved by the same idea: each eigenvalue–eigenvector pair $(\lambda, \mathbf{v})$ gives a solution $\mathbf{v}e^{\lambda t}$, and when $A$ is diagonalizable these eigenfunctions combine into the general solution. In eigenvector coordinates the system decouples into $n$ scalar equations $y' = \lambda y$. The signs of the eigenvalues decide whether the origin attracts or repels trajectories, or is a saddle point. A pair of complex eigenvalues $a \pm bi$ produces real solutions with $e^{at}\cos bt$ and $e^{at}\sin bt$, whose trajectories spiral. The examples are electrical circuits and a particle in a force field.

## Systems of Linear Differential Equations

> [!definition] Definition §38.1: Linear System of Differential Equations
> Let $x_1, \ldots, x_n$ be differentiable functions of $t$ and $a_{ij}$ constants. The system
>
> $$
> x_1' = a_{11}x_1 + \cdots + a_{1n}x_n, \quad \ldots, \quad x_n' = a_{n1}x_1 + \cdots + a_{nn}x_n
> $$
>
> is written as the **matrix differential equation**
>
> $$
> \mathbf{x}'(t) = A\mathbf{x}(t), \qquad \mathbf{x}(t) = \begin{bmatrix} x_1(t) \\ \vdots \\ x_n(t) \end{bmatrix}, \quad \mathbf{x}'(t) = \begin{bmatrix} x_1'(t) \\ \vdots \\ x_n'(t) \end{bmatrix}, \quad A = \begin{bmatrix} a_{11} & \cdots & a_{1n} \\ \vdots & & \vdots \\ a_{n1} & \cdots & a_{nn} \end{bmatrix} . \qquad (1)
> $$
>
> A **solution** of (1) is a vector-valued function that satisfies (1) for all $t$ in some interval of real numbers, such as $t \ge 0$. Given a vector $\mathbf{x}_0$, the **initial value problem** is to construct the (unique) function $\mathbf{x}$ with $\mathbf{x}' = A\mathbf{x}$ and $\mathbf{x}(0) = \mathbf{x}_0$.
>
> *Lay: 5.7 (text)*

^def-38-1

> [!theorem] Proposition §38.1: Superposition of Solutions
> If $\mathbf{u}$ and $\mathbf{v}$ are solutions of $\mathbf{x}' = A\mathbf{x}$, then so is $c\mathbf{u} + d\mathbf{v}$ for any scalars $c$, $d$. The identically zero function is a (trivial) solution. So the set of all solutions of (1) is a subspace of the vector space of continuous functions with values in $\mathbb{R}^n$.
>
> *Lay: 5.7 (text)*

^prop-38-1

> [!proof]+ Proof
> Differentiation of functions and multiplication of vectors by a matrix are both linear, so
>
> $$
> (c\mathbf{u} + d\mathbf{v})' = c\mathbf{u}' + d\mathbf{v}' = cA\mathbf{u} + dA\mathbf{v} = A(c\mathbf{u} + d\mathbf{v}) .
> $$
>
> The zero function has derivative $\mathbf{0} = A\mathbf{0}$. A set of functions containing $\mathbf{0}$ and closed under linear combinations is a subspace ([[§23 Vector Spaces and Subspaces#^def-23-2|Definition §23.2]]). (Engineers call this property **superposition of solutions**.)

^pf-38-1

*Uses:* [[§23 Vector Spaces and Subspaces#^def-23-2|Def. §23.2]] (subspace)

Standard texts on differential equations show that there is always a **fundamental set of solutions** of (1): $n$ linearly independent functions such that every solution is a unique linear combination of them. That is, the solution set is an $n$-dimensional vector space of functions, and a fundamental set is a basis for it; each initial value problem has exactly one solution. Lay does not prove this; for diagonalizable $A$ the fundamental set is constructed explicitly below (Theorem §38.3).

> [!remark]- Connections
> - ODE version: [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-1|331 Thm. §30.1]] (superposition for $\mathbf{x}' = P(t)\mathbf{x}$, where the coefficients may depend on $t$).
> - The fact Lay cites from "standard texts": 331 derives it from existence and uniqueness for linear systems, [[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|331 Thm. §27.3]] (which BDP also states without proof). The solutions with $\mathbf{x}(t_0) = \mathbf{e}_1, \ldots, \mathbf{e}_n$ form a fundamental set, [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-4|331 Thm. §30.4]], [[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-3|331 Def. §30.3]], and every solution is a unique combination of a fundamental set, [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-2|331 Thm. §30.2]]. For constant $A$ and $t_0 = 0$ these solutions are the columns of the matrix exponential $e^{At}$, [[§33★ Fundamental Matrices#^thm-33-4|331 Thm. §33.4]].

When $A$ is diagonal, the system can be solved by elementary calculus. For instance,

$$
\begin{bmatrix} x_1'(t) \\ x_2'(t) \end{bmatrix} = \begin{bmatrix} 3 & 0 \\ 0 & -5 \end{bmatrix}\begin{bmatrix} x_1(t) \\ x_2(t) \end{bmatrix}, \quad\text{that is,}\quad x_1'(t) = 3x_1(t), \quad x_2'(t) = -5x_2(t), \qquad (2), (3)
$$

is **decoupled**: each derivative depends only on the function itself, not on a combination ("coupling") of $x_1$ and $x_2$. By calculus ([[§21 Exponential Growth and Decay#^thm-21-1|Calc Thm. §21.1]]: the solutions of $y' = ky$ are $y = Ce^{kt}$), $x_1(t) = c_1e^{3t}$ and $x_2(t) = c_2e^{-5t}$, so every solution of (2) has the form

$$
\begin{bmatrix} x_1(t) \\ x_2(t) \end{bmatrix} = \begin{bmatrix} c_1e^{3t} \\ c_2e^{-5t} \end{bmatrix} = c_1\begin{bmatrix} 1 \\ 0 \end{bmatrix}e^{3t} + c_2\begin{bmatrix} 0 \\ 1 \end{bmatrix}e^{-5t} .
$$

This suggests looking for solutions of the general equation $\mathbf{x}' = A\mathbf{x}$ of the form $\mathbf{v}e^{\lambda t}$.

> [!theorem] Theorem §38.2: Eigenfunctions
> Let $\lambda$ be a scalar and $\mathbf{v} \ne \mathbf{0}$ a fixed vector. The function
>
> $$
> \mathbf{x}(t) = \mathbf{v}e^{\lambda t} \qquad (4)
> $$
>
> is a solution of $\mathbf{x}' = A\mathbf{x}$ if and only if $\lambda$ is an eigenvalue of $A$ and $\mathbf{v}$ is a corresponding eigenvector. Such solutions are called **eigenfunctions** of the differential equation.
>
> *Lay: 5.7 (text)*

^thm-38-2

> [!proof]+ Proof
> Since $\mathbf{v}$ is a constant vector, $\mathbf{x}'(t) = \lambda\mathbf{v}e^{\lambda t}$. Multiplying (4) by $A$ gives $A\mathbf{x}(t) = A\mathbf{v}e^{\lambda t}$. Since $e^{\lambda t}$ is never zero, $\mathbf{x}'(t) = A\mathbf{x}(t)$ (for one, or all, $t$) if and only if $\lambda\mathbf{v} = A\mathbf{v}$. (If $\mathbf{v} = \mathbf{0}$, the function is identically zero and trivially a solution.)

^pf-38-2

*Uses:* [[§32 Eigenvectors and Eigenvalues#^def-32-1|Def. §32.1]], [[§21 Exponential Growth and Decay#^thm-21-1|Calc Thm. §21.1]] (derivative of $e^{kt}$)

> [!example] Example §38.1: An RC Circuit (Attractor)
> The circuit of two capacitors $C_1$, $C_2$ and two resistors $R_1$, $R_2$ in Lay's Figure 1 is described by
>
> $$
> \begin{bmatrix} x_1'(t) \\ x_2'(t) \end{bmatrix} = \begin{bmatrix} -(1/R_1 + 1/R_2)/C_1 & 1/(R_2C_1) \\ 1/(R_2C_2) & -1/(R_2C_2) \end{bmatrix}\begin{bmatrix} x_1(t) \\ x_2(t) \end{bmatrix},
> $$
>
> where $x_1(t)$, $x_2(t)$ are the voltages across the two capacitors. Let $R_1 = 1$ ohm, $R_2 = 2$ ohms, $C_1 = 1$ farad and $C_2 = .5$ farad, with initial charges of $5$ volts on $C_1$ and $4$ volts on $C_2$. Find $x_1(t)$ and $x_2(t)$.
>
> **The data.** $-(1 + \frac12)/1 = -1.5$, $1/(2 \cdot 1) = .5$, $1/(2 \cdot .5) = 1$, so
>
> $$
> A = \begin{bmatrix} -1.5 & .5 \\ 1 & -1 \end{bmatrix}, \qquad \mathbf{x}(0) = \begin{bmatrix} 5 \\ 4 \end{bmatrix} .
> $$
>
> **Eigenvalues and eigenvectors.** $\det(A - \lambda I) = (-1.5 - \lambda)(-1 - \lambda) - .5 = \lambda^2 + 2.5\lambda + 1 = (\lambda + .5)(\lambda + 2)$, so $\lambda_1 = -.5$, $\lambda_2 = -2$. Then $A\begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} -.5 \\ -1 \end{bmatrix}$ and $A\begin{bmatrix} -1 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 \\ -2 \end{bmatrix}$, so $\mathbf{v}_1 = (1, 2)$ and $\mathbf{v}_2 = (-1, 1)$.
>
> **The solution.** The eigenfunctions $\mathbf{v}_1e^{\lambda_1t}$ and $\mathbf{v}_2e^{\lambda_2t}$ satisfy $\mathbf{x}' = A\mathbf{x}$ (Theorem §38.2), and so does any linear combination (Proposition §38.1):
>
> $$
> \mathbf{x}(t) = c_1\mathbf{v}_1e^{\lambda_1t} + c_2\mathbf{v}_2e^{\lambda_2t} = c_1\begin{bmatrix} 1 \\ 2 \end{bmatrix}e^{-.5t} + c_2\begin{bmatrix} -1 \\ 1 \end{bmatrix}e^{-2t} .
> $$
>
> Since $\mathbf{x}(0) = c_1\mathbf{v}_1 + c_2\mathbf{v}_2$ and $\mathbf{v}_1$, $\mathbf{v}_2$ are linearly independent (so they span $\mathbb{R}^2$), we can match $\mathbf{x}(0)$:
>
> $$
> c_1\begin{bmatrix} 1 \\ 2 \end{bmatrix} + c_2\begin{bmatrix} -1 \\ 1 \end{bmatrix} = \begin{bmatrix} 5 \\ 4 \end{bmatrix}: \quad c_1 - c_2 = 5, \ \ 2c_1 + c_2 = 4 \quad\Rightarrow\quad 3c_1 = 9, \ \ c_1 = 3, \ \ c_2 = -2 .
> $$
>
> So
>
> $$
> \mathbf{x}(t) = 3\begin{bmatrix} 1 \\ 2 \end{bmatrix}e^{-.5t} - 2\begin{bmatrix} -1 \\ 1 \end{bmatrix}e^{-2t}, \qquad\text{or}\qquad \begin{bmatrix} x_1(t) \\ x_2(t) \end{bmatrix} = \begin{bmatrix} 3e^{-.5t} + 2e^{-2t} \\ 6e^{-.5t} - 2e^{-2t} \end{bmatrix} .
> $$
>
> **Behavior.** Both eigenfunctions decay to zero as $t \to \infty$, but $\mathbf{v}_2e^{-2t}$ decays faster. The entries of $\mathbf{v}_2 = (-1, 1)$ show that the voltages decay to zero as rapidly as possible when the initial voltages are equal in magnitude but opposite in sign. The trajectories of the two eigenfunctions lie in the eigenspaces of $A$.
>
> *Lay: Example 5.7.1*

^ex-38-1

> [!definition] Definition §38.2: Attractor (Sink), Repeller (Source), Saddle Point
> For the dynamical system $\mathbf{x}' = A\mathbf{x}$, the origin is called
> - an **attractor**, or **sink**, if all trajectories are drawn into the origin (as in Example §38.1, where both eigenvalues are negative). The **direction of greatest attraction** is along the trajectory of the eigenfunction for the more negative eigenvalue; trajectories not on this line become asymptotic to the line of the other eigenvector, because their components in the faster direction decay so rapidly;
> - a **repeller**, or **source**, if the trajectories are traversed away from the origin (as when both eigenvalues are positive); the **direction of greatest repulsion** is the line of the eigenfunction for the more positive eigenvalue;
> - a **saddle point** if some trajectories approach the origin at first and then change direction and move away; this arises whenever $A$ has both positive and negative eigenvalues. The direction of greatest repulsion is the line through the eigenvector for the positive eigenvalue, the direction of greatest attraction the line through the eigenvector for the negative one.
>
> *Lay: 5.7 (text)*

^def-38-2

> [!remark]- Connections
> - ODE version: BDP's names for the real-eigenvalue cases, saddle point, [[§31 Homogeneous Linear Systems with Constant Coefficients#^def-31-3|331 Def. §31.3]], and node (an attractor or repeller with distinct real eigenvalues), [[§31 Homogeneous Linear Systems with Constant Coefficients#^def-31-4|331 Def. §31.4]]; the full $2 \times 2$ classification, with spiral points and centers, [[§32 Complex-Valued Eigenvalues#^thm-32-3|331 Thm. §32.3]].

> [!example] Example §38.2: A Particle in a Force Field (Saddle Point)
> A particle moves in a planar force field, and its position vector $\mathbf{x}$ satisfies $\mathbf{x}' = A\mathbf{x}$, $\mathbf{x}(0) = \mathbf{x}_0$, where
>
> $$
> A = \begin{bmatrix} 4 & -5 \\ -2 & 1 \end{bmatrix}, \qquad \mathbf{x}_0 = \begin{bmatrix} 2.9 \\ 2.6 \end{bmatrix} .
> $$
>
> Solve this initial value problem for $t \ge 0$.
>
> **Eigenvalues and eigenvectors.** $\det(A - \lambda I) = (4 - \lambda)(1 - \lambda) - 10 = \lambda^2 - 5\lambda - 6 = (\lambda - 6)(\lambda + 1)$, so $\lambda_1 = 6$ and $\lambda_2 = -1$. Check: $A\begin{bmatrix} -5 \\ 2 \end{bmatrix} = \begin{bmatrix} -20 - 10 \\ 10 + 2 \end{bmatrix} = 6\begin{bmatrix} -5 \\ 2 \end{bmatrix}$ and $A\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} -1 \\ -1 \end{bmatrix}$, so $\mathbf{v}_1 = (-5, 2)$, $\mathbf{v}_2 = (1, 1)$.
>
> **The solution.** For any constants $c_1, c_2$, $\mathbf{x}(t) = c_1\begin{bmatrix} -5 \\ 2 \end{bmatrix}e^{6t} + c_2\begin{bmatrix} 1 \\ 1 \end{bmatrix}e^{-t}$ is a solution. For $\mathbf{x}(0) = \mathbf{x}_0$:
>
> $$
> \begin{bmatrix} -5 & 1 \\ 2 & 1 \end{bmatrix}\begin{bmatrix} c_1 \\ c_2 \end{bmatrix} = \begin{bmatrix} 2.9 \\ 2.6 \end{bmatrix} .
> $$
>
> Subtracting the second equation from the first, $-7c_1 = .3$, so $c_1 = -3/70$, and then $c_2 = 2.6 - 2c_1 = 2.6 + 6/70 = 188/70$. So
>
> $$
> \mathbf{x}(t) = -\frac{3}{70}\begin{bmatrix} -5 \\ 2 \end{bmatrix}e^{6t} + \frac{188}{70}\begin{bmatrix} 1 \\ 1 \end{bmatrix}e^{-t} .
> $$
>
> The origin is a saddle point. Because $c_1$ is small, the particle first moves toward the origin along the attracting line through $\mathbf{v}_2$; eventually the term $-\frac{3}{70}e^{6t}\mathbf{v}_1$ takes over and the particle moves away in the direction of $-\mathbf{v}_1 = (5, -2)$, the direction of greatest repulsion.
>
> *Lay: Example 5.7.2*

^ex-38-2

## Decoupling a Dynamical System

> [!theorem] Theorem §38.3: General Solution for Diagonalizable A
> Let $A$ be $n \times n$ with $n$ linearly independent eigenvectors $\mathbf{v}_1, \ldots, \mathbf{v}_n$ and corresponding eigenvalues $\lambda_1, \ldots, \lambda_n$, so that $A = PDP^{-1}$ with $P = [\,\mathbf{v}_1 \; \cdots \; \mathbf{v}_n\,]$ and $D = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$. Then the change of variable
>
> $$
> \mathbf{y}(t) = P^{-1}\mathbf{x}(t), \qquad\text{or equivalently}\qquad \mathbf{x}(t) = P\mathbf{y}(t),
> $$
>
> turns $\mathbf{x}' = A\mathbf{x}$ into the decoupled system $\mathbf{y}' = D\mathbf{y}$, that is, $y_k' = \lambda_ky_k$ for each $k$. Every solution of $\mathbf{x}' = A\mathbf{x}$ is
>
> $$
> \mathbf{x}(t) = c_1\mathbf{v}_1e^{\lambda_1t} + \cdots + c_n\mathbf{v}_ne^{\lambda_nt}, \qquad \begin{bmatrix} c_1 \\ \vdots \\ c_n \end{bmatrix} = P^{-1}\mathbf{x}(0),
> $$
>
> so the eigenfunctions $\mathbf{v}_1e^{\lambda_1t}, \ldots, \mathbf{v}_ne^{\lambda_nt}$ form a fundamental set of solutions.
>
> *Lay: 5.7 (text, "Decoupling a Dynamical System")*

^thm-38-3

> [!proof]+ Proof
> $\mathbf{y}(t) = P^{-1}\mathbf{x}(t)$ is the coordinate vector of $\mathbf{x}(t)$ relative to the eigenvector basis. Substituting $\mathbf{x} = P\mathbf{y}$ into $\mathbf{x}' = A\mathbf{x}$ gives
>
> $$
> \frac{d}{dt}(P\mathbf{y}) = A(P\mathbf{y}) = (PDP^{-1})P\mathbf{y} = PD\mathbf{y} . \qquad (5)
> $$
>
> Since $P$ is a constant matrix, the left side of (5) is $P\mathbf{y}'$ (each entry of $P\mathbf{y}$ is a constant combination of the $y_k$, and differentiation is linear). Left-multiplying both sides by $P^{-1}$ gives $\mathbf{y}' = D\mathbf{y}$, that is,
>
> $$
> \begin{bmatrix} y_1'(t) \\ y_2'(t) \\ \vdots \\ y_n'(t) \end{bmatrix} = \begin{bmatrix} \lambda_1 & 0 & \cdots & 0 \\ 0 & \lambda_2 & & \vdots \\ \vdots & & \ddots & 0 \\ 0 & \cdots & 0 & \lambda_n \end{bmatrix}\begin{bmatrix} y_1(t) \\ y_2(t) \\ \vdots \\ y_n(t) \end{bmatrix} .
> $$
>
> The derivative of each $y_k$ depends only on $y_k$. Since $y_1' = \lambda_1y_1$, we have $y_1(t) = c_1e^{\lambda_1t}$ ([[§21 Exponential Growth and Decay#^thm-21-1|Calc Thm. §21.1]]), and similarly for $y_2, \ldots, y_n$, with $(c_1, \ldots, c_n) = \mathbf{y}(0) = P^{-1}\mathbf{x}(0)$. Then
>
> $$
> \mathbf{x}(t) = P\mathbf{y}(t) = [\,\mathbf{v}_1 \; \cdots \; \mathbf{v}_n\,]\begin{bmatrix} c_1e^{\lambda_1t} \\ \vdots \\ c_ne^{\lambda_nt} \end{bmatrix} = c_1\mathbf{v}_1e^{\lambda_1t} + \cdots + c_n\mathbf{v}_ne^{\lambda_nt} .
> $$
>
> This is the eigenfunction expansion of Examples §38.1 and §38.2. The eigenfunctions are linearly independent as functions: if a combination is the zero function, its value at $t = 0$ is $\sum c_k\mathbf{v}_k = \mathbf{0}$, so all $c_k = 0$.

^pf-38-3

*Uses:* [[§34 Diagonalization#^thm-34-1|§34.1]], [[§21 Exponential Growth and Decay#^thm-21-1|Calc Thm. §21.1]], [[§38 Applications to Differential Equations#^thm-38-2|§38.2]]

> [!remark]- Connections
> - ODE version: [[§33★ Fundamental Matrices#^thm-33-8|331 Thm. §33.8]] (the same decoupling $\mathbf{x} = \mathbf{T}\mathbf{y}$, $\mathbf{y}' = D\mathbf{y}$, which also gives $e^{At} = \mathbf{T}e^{Dt}\mathbf{T}^{-1}$) and [[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-2|331 Thm. §31.2]] (the eigenfunctions form a fundamental set). The same substitution uncouples the nonhomogeneous system $\mathbf{x}' = A\mathbf{x} + \mathbf{g}(t)$, [[§35★ Nonhomogeneous Linear Systems#^thm-35-2|331 Thm. §35.2]].

This is the same change of variable as [[§37 Discrete Dynamical Systems#^thm-37-4|Theorem §37.4]] for difference equations, with $\lambda^k$ replaced by $e^{\lambda t}$. In particular the origin is an attractor when all $\lambda_k < 0$ ($e^{\lambda_kt} \to 0$) and a repeller when all $\lambda_k > 0$, where for $\mathbf{x}_{k+1} = A\mathbf{x}_k$ the dividing line was $|\lambda_k| = 1$.

## Complex Eigenvalues

Let the real matrix $A$ have a pair of complex eigenvalues $\lambda$ and $\bar\lambda$ with eigenvectors $\mathbf{v}$ and $\overline{\mathbf{v}}$ ([[§36 Complex Eigenvalues#^thm-36-2|Theorem §36.2]]). Then $\mathbf{x}_1(t) = \mathbf{v}e^{\lambda t}$ and $\mathbf{x}_2(t) = \overline{\mathbf{v}}e^{\bar\lambda t}$ are complex solutions, with $\mathbf{x}_2 = \overline{\mathbf{x}_1}$. Real solutions are often more appropriate, and they are the real and imaginary parts of $\mathbf{x}_1$. This needs the exponential of a complex number.

> [!definition] Definition §38.3: The Complex Exponential
> For a complex number $\lambda = a + bi$ ($a$, $b$ real) and real $t$, $e^{\lambda t}$ is defined by the power series $e^{\lambda t} = 1 + (\lambda t) + \frac{1}{2!}(\lambda t)^2 + \cdots + \frac{1}{n!}(\lambda t)^n + \cdots$, the series of $e^x$ ([[§78 Taylor and Maclaurin Series#^thm-78-6|Calc Thm. §78.6]]) with $x = \lambda t$. Using the series for cosine and sine, one shows that
>
> $$
> e^{(a + bi)t} = e^{at} \cdot e^{ibt} = e^{at}(\cos bt + i\sin bt) . \qquad (7)
> $$
>
> *Lay: 5.7 (text), Equation (7)*

^def-38-3

*Lay omits the verification of (7). The factor $e^{ibt} = \cos bt + i\sin bt$ is Euler's formula, derived from the series in [[§53 Complex Numbers#^rem-53-1|§53, Remark: Euler's Formula]]; the step $e^{(a + bi)t} = e^{at}e^{ibt}$ uses the law of exponents for complex numbers, which follows from the series by multiplying them out (rigorous treatment of power series: Single Variable Analysis). Below, (7) is all that is used.*

> [!theorem] Theorem §38.4: Real Solutions from a Complex Eigenvalue
> Let $A$ be a real $n \times n$ matrix with a complex eigenvalue $\lambda = a + bi$ ($b \ne 0$) and eigenvector $\mathbf{v}$ in $\mathbb{C}^n$. Then $\mathbf{x}_1(t) = \mathbf{v}e^{\lambda t}$ is a (complex) solution of $\mathbf{x}' = A\mathbf{x}$, and its real and imaginary parts
>
> $$
> \begin{aligned}
> \mathbf{y}_1(t) &= \operatorname{Re}\mathbf{x}_1(t) = \big[(\operatorname{Re}\mathbf{v})\cos bt - (\operatorname{Im}\mathbf{v})\sin bt\big]e^{at}, \\
> \mathbf{y}_2(t) &= \operatorname{Im}\mathbf{x}_1(t) = \big[(\operatorname{Re}\mathbf{v})\sin bt + (\operatorname{Im}\mathbf{v})\cos bt\big]e^{at}
> \end{aligned}
> $$
>
> are two linearly independent real solutions.
>
> *Lay: 5.7 (text)*

^thm-38-4

> [!proof]+ Proof
> **$\mathbf{x}_1$ is a solution.** By (7), $e^{\lambda t} = e^{at}\cos bt + ie^{at}\sin bt$. Differentiating real and imaginary parts with the product rule,
>
> $$
> \frac{d}{dt}e^{\lambda t} = e^{at}(a\cos bt - b\sin bt) + ie^{at}(a\sin bt + b\cos bt) = (a + bi)e^{at}(\cos bt + i\sin bt) = \lambda e^{\lambda t},
> $$
>
> as one checks by multiplying out $(a + bi)(\cos bt + i\sin bt)$. So $\mathbf{x}_1'(t) = \lambda\mathbf{v}e^{\lambda t} = A\mathbf{v}e^{\lambda t} = A\mathbf{x}_1(t)$, as in Theorem §38.2.
>
> **The real and imaginary parts are solutions.** Lay: they are linear combinations of the solutions $\mathbf{x}_1$ and $\overline{\mathbf{x}_1}$, $\operatorname{Re}\mathbf{x}_1 = \frac12(\mathbf{x}_1 + \overline{\mathbf{x}_1})$ and $\operatorname{Im}\mathbf{x}_1 = \frac{1}{2i}(\mathbf{x}_1 - \overline{\mathbf{x}_1})$. Directly: differentiation commutes with taking real and imaginary parts, and $A$ is real, so by [[§36 Complex Eigenvalues#^prop-36-1|Proposition §36.1]]
>
> $$
> (\operatorname{Re}\mathbf{x}_1)' = \operatorname{Re}(\mathbf{x}_1') = \operatorname{Re}(A\mathbf{x}_1) = A\operatorname{Re}\mathbf{x}_1 ,
> $$
>
> and likewise for $\operatorname{Im}\mathbf{x}_1$.
>
> **The formulas.** Multiply out:
>
> $$
> \mathbf{v}e^{\lambda t} = (\operatorname{Re}\mathbf{v} + i\operatorname{Im}\mathbf{v})\,e^{at}(\cos bt + i\sin bt) = \big[(\operatorname{Re}\mathbf{v})\cos bt - (\operatorname{Im}\mathbf{v})\sin bt\big]e^{at} + i\big[(\operatorname{Re}\mathbf{v})\sin bt + (\operatorname{Im}\mathbf{v})\cos bt\big]e^{at} .
> $$
>
> **Independence** (Lay: "it can be shown"). At $t = 0$, $\mathbf{y}_1(0) = \operatorname{Re}\mathbf{v}$ and $\mathbf{y}_2(0) = \operatorname{Im}\mathbf{v}$, which are linearly independent by Step 1 of the proof of [[§36 Complex Eigenvalues#^thm-36-4|Theorem §36.4]] (valid for real $n \times n$ matrices; it uses only that the eigenvalue is not real, so it applies to $a + bi$ as well as to $a - bi$). If $c_1\mathbf{y}_1 + c_2\mathbf{y}_2$ is the zero function, its value at $0$ gives $c_1 = c_2 = 0$.

^pf-38-4

*Uses:* [[§38 Applications to Differential Equations#^def-38-3|Def. §38.3]], [[§38 Applications to Differential Equations#^thm-38-2|§38.2]], [[§36 Complex Eigenvalues#^prop-36-1|§36.1]], [[§36 Complex Eigenvalues#^thm-36-4|§36.4]] (Step 1)

> [!remark]- Connections
> - ODE version: [[§32 Complex-Valued Eigenvalues#^thm-32-2|331 Thm. §32.2]] (the same real solutions, with $\mathbf{a} + i\mathbf{b}$ for $\operatorname{Re}\mathbf{v} + i\operatorname{Im}\mathbf{v}$), worked in [[§32 Complex-Valued Eigenvalues#^ex-32-1|331 Ex. §32.1]]. The rule $\frac{d}{dt}e^{\lambda t} = \lambda e^{\lambda t}$ for complex $\lambda$, used in the first step: [[§15 Complex Roots of the Characteristic Equation#^prop-15-1|331 Prop. §15.1]].

Since $\mathbf{x}_2 = \overline{\mathbf{x}_1}$ has real and imaginary parts $\mathbf{y}_1$ and $-\mathbf{y}_2$, one can use either $\mathbf{x}_1$ or $\mathbf{x}_2$, but not both, to produce two real linearly independent solutions.

> [!example] Example §38.3: An RLC Circuit (Spiral Point)
> The circuit of Lay's Figure 4 (resistors $R_1$, $R_2$, capacitor $C$, inductor $L$) is described by
>
> $$
> \begin{bmatrix} i_L' \\ v_C' \end{bmatrix} = \begin{bmatrix} -R_2/L & -1/L \\ 1/C & -1/(R_1C) \end{bmatrix}\begin{bmatrix} i_L \\ v_C \end{bmatrix},
> $$
>
> where $i_L$ is the current through the inductor and $v_C$ the voltage drop across the capacitor. Let $R_1 = 5$ ohms, $R_2 = .8$ ohm, $C = .1$ farad, $L = .4$ henry, with initial current $3$ amperes and initial voltage $3$ volts. Find $i_L$ and $v_C$.
>
> **The data.** $-.8/.4 = -2$, $-1/.4 = -2.5$, $1/.1 = 10$, $-1/(5 \cdot .1) = -2$:
>
> $$
> A = \begin{bmatrix} -2 & -2.5 \\ 10 & -2 \end{bmatrix}, \qquad \mathbf{x}_0 = \begin{bmatrix} 3 \\ 3 \end{bmatrix} .
> $$
>
> **Eigenvalue and eigenvector.** $\det(A - \lambda I) = (-2 - \lambda)^2 + 25$, which vanishes when $-2 - \lambda = \pm 5i$: $\lambda = -2 \mp 5i$. For $\lambda = -2 + 5i$, the first row of $A - \lambda I$ is $(-5i, -2.5)$, and [[§36 Complex Eigenvalues#^rem-36-1|Remark: Method]] gives the eigenvector $(2.5, -5i)$; multiplying it by $i/2.5$ gives the simpler $\mathbf{v}_1 = \begin{bmatrix} i \\ 2 \end{bmatrix}$. Check: $(-5i)(i) - 2.5(2) = 5 - 5 = 0$, and second row: $10i + (-2 - (-2 + 5i))\cdot 2 = 10i - 10i = 0$. The complex solutions are combinations of
>
> $$
> \mathbf{x}_1(t) = \begin{bmatrix} i \\ 2 \end{bmatrix}e^{(-2 + 5i)t} \qquad\text{and}\qquad \mathbf{x}_2(t) = \begin{bmatrix} -i \\ 2 \end{bmatrix}e^{(-2 - 5i)t} .
> $$
>
> **Real solutions.** By (7), $\mathbf{x}_1(t) = \begin{bmatrix} i \\ 2 \end{bmatrix}e^{-2t}(\cos 5t + i\sin 5t) = \begin{bmatrix} -\sin 5t + i\cos 5t \\ 2\cos 5t + 2i\sin 5t \end{bmatrix}e^{-2t}$, so
>
> $$
> \mathbf{y}_1(t) = \begin{bmatrix} -\sin 5t \\ 2\cos 5t \end{bmatrix}e^{-2t}, \qquad \mathbf{y}_2(t) = \begin{bmatrix} \cos 5t \\ 2\sin 5t \end{bmatrix}e^{-2t} .
> $$
>
> They are linearly independent (Theorem §38.4), hence a basis for the two-dimensional real vector space of solutions, and the general solution is $\mathbf{x}(t) = c_1\mathbf{y}_1(t) + c_2\mathbf{y}_2(t)$.
>
> **Initial values.** $\mathbf{x}(0) = c_1\begin{bmatrix} 0 \\ 2 \end{bmatrix} + c_2\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 3 \\ 3 \end{bmatrix}$ gives $c_2 = 3$ and $c_1 = 1.5$. Thus
>
> $$
> \mathbf{x}(t) = 1.5\begin{bmatrix} -\sin 5t \\ 2\cos 5t \end{bmatrix}e^{-2t} + 3\begin{bmatrix} \cos 5t \\ 2\sin 5t \end{bmatrix}e^{-2t}, \qquad\text{or}\qquad \begin{bmatrix} i_L(t) \\ v_C(t) \end{bmatrix} = \begin{bmatrix} -1.5\sin 5t + 3\cos 5t \\ 3\cos 5t + 6\sin 5t \end{bmatrix}e^{-2t} .
> $$
>
> The origin is a **spiral point** of the system: the sine and cosine, coming from the imaginary part $5$ of the eigenvalue, make the trajectories rotate, and the factor $e^{-2t}$, from the real part $-2$, makes them spiral inward. When $A$ has a complex eigenvalue with positive real part, the trajectories spiral outward; if the real part is zero, they are ellipses around the origin.
>
> *Lay: Example 5.7.3*

^ex-38-3

![[m235-38-1.svg]]
*(a) Example §38.1: trajectories of $\mathbf{x}' = A\mathbf{x}$ with eigenvalues $-.5$ and $-2$. The origin is a sink; the solution from $(5, 4)$ (red) first moves quickly in the $\mathbf{v}_2$-direction (green, fast decay $e^{-2t}$) and then comes in tangent to the line through $\mathbf{v}_1$ (blue, slow decay $e^{-.5t}$). (b) Example §38.3: the trajectory from $(3, 3)$ in the $(i_L, v_C)$-plane spirals into the origin, turning with $\cos 5t$, $\sin 5t$ and shrinking like $e^{-2t}$.*
