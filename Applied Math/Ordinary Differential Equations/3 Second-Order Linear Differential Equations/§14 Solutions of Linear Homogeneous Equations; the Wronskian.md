---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 3
section: 14
bdp: "3.2"
aliases: ["BDP 3.2"]
tags: [ordinary-differential-equations, math331]
---
← [[§13 Homogeneous Differential Equations with Constant Coefficients]] · ↑ [[· 3 Second-Order Linear Differential Equations]] · [[§15 Complex Roots of the Characteristic Equation]] →

*Boyce–DiPrima, Section 3.2 · MATH 331 Midterm (Fall 2021), Midterm (Summer 2023).*

This section explains why two solutions are enough. The existence and uniqueness theorem guarantees exactly one solution of $y'' + p(t)y' + q(t)y = g(t)$ for each pair of initial conditions, on the whole interval where the coefficients are continuous. The principle of superposition says that linear combinations of solutions of the homogeneous equation are solutions. Whether $c_1y_1 + c_2y_2$ can meet every pair of initial conditions, and hence contains every solution, is decided by a single determinant, the Wronskian $W[y_1, y_2] = y_1y_2' - y_1'y_2$; two solutions with nonzero Wronskian form a fundamental set. In the language of linear algebra, the solutions form a two-dimensional vector space and a fundamental set is a basis. Real and imaginary parts of complex solutions are solutions, which is the tool for complex roots in [[§15 Complex Roots of the Characteristic Equation|§15]]. Abel's theorem gives the Wronskian of any two solutions without solving the equation.

## The Differential Operator L

> [!definition] Definition §14.1: The Differential Operator L
> Let $p$ and $q$ be continuous on an open interval $I$: $\alpha < t < \beta$ (where $\alpha = -\infty$, $\beta = \infty$, or both, are allowed). For a function $\phi$ that is twice differentiable on $I$, the **differential operator** $L$ is defined by
>
> $$
> L[\phi] = \phi'' + p\phi' + q\phi . \qquad (1)
> $$
>
> $L[\phi]$ is again a function, with value $L[\phi](t) = \phi''(t) + p(t)\phi'(t) + q(t)\phi(t)$. One writes $L = D^2 + pD + q$, where $D[\phi] = \phi'$ is the derivative operator. For example, if $p(t) = t^2$, $q(t) = 1 + t$ and $\phi(t) = \sin 3t$, then
>
> $$
> L[\phi](t) = (\sin 3t)'' + t^2(\sin 3t)' + (1 + t)\sin 3t = -9\sin 3t + 3t^2\cos 3t + (1 + t)\sin 3t .
> $$
>
> The homogeneous equation $L[\phi](t) = 0$ is written, with $y$ for $\phi(t)$,
>
> $$
> L[y] = y'' + p(t)y' + q(t)y = 0 , \qquad (2)
> $$
>
> with initial conditions
>
> $$
> y(t_0) = y_0, \qquad y'(t_0) = y_0' , \qquad (3)
> $$
>
> where $t_0 \in I$ and $y_0$, $y_0'$ are given real numbers.
>
> *BDP: 3.2 (text)*

^def-14-1

## Existence and Uniqueness

> [!theorem] Theorem §14.1: Existence and Uniqueness Theorem
> Consider the initial value problem
>
> $$
> y'' + p(t)y' + q(t)y = g(t), \qquad y(t_0) = y_0, \quad y'(t_0) = y_0' , \qquad (4)
> $$
>
> where $p$, $q$ and $g$ are continuous on an open interval $I$ that contains the point $t_0$. This problem has exactly one solution $y = \phi(t)$, and the solution exists throughout the interval $I$.
>
> *BDP: Theorem 3.2.1*

^thm-14-1

*BDP omits the proof ("fairly difficult"; it refers to Coddington, Chapter 6, Section 8). §11 proves the first-order case by Picard iteration, [[§11 The Existence and Uniqueness Theorem#^thm-11-7|Theorem §11.7]] (Theorem 2.8.1); the second-order linear equation is the case $n = 2$ of the systems version, [[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|Theorem §27.3]] (Theorem 7.1.2), which BDP does not prove either.*

> [!remark] Remark: What the Theorem Says
> Three things: the problem *has* a solution (existence); it has *only one* (uniqueness); and the solution is defined, and twice differentiable, *throughout* the interval $I$ where the coefficients are continuous. This is the second-order analog of [[§7 Differences Between Linear and Nonlinear Differential Equations#^thm-7-1|Theorem §7.1]] (Theorem 2.4.1) for first-order linear equations. Existence is sometimes visible directly: $y = \frac12e^t + \frac32e^{-t}$ solves $y'' - y = 0$, $y(0) = 2$, $y'(0) = -1$ on $(-\infty, \infty)$ ([[§13 Homogeneous Differential Equations with Constant Coefficients#^ex-13-1|Example §13.1]]). That it is the *only* solution is not obvious; the theorem guarantees it. Unlike first-order linear equations, second-order equations generally have no useful solution formula, so the proof has to work without one.

^rem-14-1

> [!example] Example §14.1: Applying the Theorem
> **(a)** Find the longest interval in which the solution of
>
> $$
> (t^2 - 3t)y'' + ty' - (t + 3)y = 0, \qquad y(1) = 2, \quad y'(1) = 1
> $$
>
> is certain to exist. Dividing by $t^2 - 3t = t(t - 3)$ puts the equation in the form (4) with
>
> $$
> p(t) = \frac{t}{t(t - 3)} = \frac{1}{t - 3}, \qquad q(t) = -\frac{t + 3}{t(t - 3)}, \qquad g(t) = 0 .
> $$
>
> The coefficients are discontinuous only at $t = 0$ (where $q$ blows up) and $t = 3$. The longest open interval containing the initial point $t = 1$ on which all of them are continuous is $0 < t < 3$, and Theorem §14.1 guarantees a solution there.
>
> **(b)** Find the unique solution of $y'' + p(t)y' + q(t)y = 0$, $y(t_0) = 0$, $y'(t_0) = 0$, where $p$ and $q$ are continuous on an open interval $I$ containing $t_0$. The function $\phi(t) = 0$ for all $t$ in $I$ satisfies the equation and the initial conditions. By the uniqueness part of Theorem §14.1 it is the only solution.
>
> *BDP: Examples 3.2.1 and 3.2.2*

^ex-14-1

## Superposition

> [!theorem] Theorem §14.2: Principle of Superposition
> If $y_1$ and $y_2$ are two solutions of the differential equation (2),
>
> $$
> L[y] = y'' + p(t)y' + q(t)y = 0 ,
> $$
>
> then the linear combination $c_1y_1 + c_2y_2$ is also a solution for any values of the constants $c_1$ and $c_2$. In particular ($c_2 = 0$), any constant multiple of a solution is a solution.
>
> *BDP: Theorem 3.2.2*

^thm-14-2

> [!proof]+ Proof
> Substitute $y = c_1y_1(t) + c_2y_2(t)$ in (2). By the sum and constant multiple rules for derivatives,
>
> $$
> \begin{aligned}
> L[c_1y_1 + c_2y_2] &= [c_1y_1 + c_2y_2]'' + p[c_1y_1 + c_2y_2]' + q[c_1y_1 + c_2y_2] \\
> &= c_1y_1'' + c_2y_2'' + c_1py_1' + c_2py_2' + c_1qy_1 + c_2qy_2 \\
> &= c_1[y_1'' + py_1' + qy_1] + c_2[y_2'' + py_2' + qy_2] \\
> &= c_1L[y_1] + c_2L[y_2] .
> \end{aligned}
> $$
>
> Since $L[y_1] = 0$ and $L[y_2] = 0$, also $L[c_1y_1 + c_2y_2] = 0$. The computation uses only the rules of algebra, so it holds equally for complex constants $c_1$, $c_2$ and complex-valued $y_1$, $y_2$ (used in [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^cor-14-7|Corollary §14.7]]).

^pf-14-2

*Uses:* [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^def-14-1|Def. §14.1]]

> [!remark]- Connections
> - The computation says that $L$ is a linear map, $L[c_1y_1 + c_2y_2] = c_1L[y_1] + c_2L[y_2]$, so the solution set of $L[y] = 0$ is its null space and hence a subspace: [[§8 Null Spaces and Ranges#^ladr-3-13|LADR 3.13]], [[§24 Null Spaces, Column Spaces, and Linear Transformations#^thm-24-5|235 Thm. §24.5]]. Lay's instance is $y'' + \omega^2y = 0$, [[§24 Null Spaces, Column Spaces, and Linear Transformations#^ex-24-5|235 Ex. §24.5]].
> - The same principle for systems $\mathbf{x}' = A\mathbf{x}$: [[§38 Applications to Differential Equations#^prop-38-1|235 Prop. §38.1]].
> - PDE version: [[§19 Example꞉ Fixed End Temperatures#^thm-19-4|341 Thm. §19.4]] (superposition for linear homogeneous partial differential equations and boundary conditions, which lets separation of variables build series solutions); in Powers' review of ODEs, [[§1★ Homogeneous Linear Equations#^thm-1-2|341 Thm. §1.2]].

## The Wronskian

Superposition produces an infinite family $c_1y_1 + c_2y_2$ from two solutions. Does it contain every solution? First ask whether $c_1$ and $c_2$ can be chosen to satisfy the initial conditions (3). They must solve

$$
\begin{aligned}
c_1y_1(t_0) + c_2y_2(t_0) &= y_0, \\
c_1y_1'(t_0) + c_2y_2'(t_0) &= y_0' .
\end{aligned} \qquad (8)
$$

> [!definition] Definition §14.2: Wronskian
> The determinant of the coefficients of the system (8),
>
> $$
> W = \begin{vmatrix} y_1(t_0) & y_2(t_0) \\ y_1'(t_0) & y_2'(t_0) \end{vmatrix} = y_1(t_0)y_2'(t_0) - y_1'(t_0)y_2(t_0) , \qquad (9)
> $$
>
> is the **Wronskian determinant**, or simply the **Wronskian**, of $y_1$ and $y_2$ (after Józef Maria Hoëné-Wroński). Writing $W[y_1, y_2](t_0)$ emphasizes that it depends on the functions $y_1$, $y_2$ and on the point $t_0$; as a function of $t$, $W[y_1, y_2] = y_1y_2' - y_1'y_2$.
>
> *BDP: 3.2, Equation (9)*

^def-14-2

> [!theorem] Theorem §14.3: Solvability of the Initial Conditions
> Suppose that $y_1$ and $y_2$ are two solutions of (2), $L[y] = y'' + p(t)y' + q(t)y = 0$, and that the initial conditions (3), $y(t_0) = y_0$, $y'(t_0) = y_0'$, are assigned. Then it is always possible to choose the constants $c_1$, $c_2$ so that
>
> $$
> y = c_1y_1(t) + c_2y_2(t)
> $$
>
> satisfies the differential equation (2) and the initial conditions (3) if and only if the Wronskian $W[y_1, y_2] = y_1y_2' - y_1'y_2$ is not zero at $t_0$.
>
> *BDP: Theorem 3.2.3*

^thm-14-3

> [!proof]+ Proof
> By [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-2|Theorem §14.2]], $c_1y_1 + c_2y_2$ satisfies (2) for every choice of constants, so the question is only whether the linear system (8) for $c_1$, $c_2$ can be solved for every right side $(y_0, y_0')$.
>
> **If $W \ne 0$.** Multiply the first equation of (8) by $y_2'(t_0)$, the second by $y_2(t_0)$, and subtract; then multiply the first by $y_1'(t_0)$, the second by $y_1(t_0)$, and subtract the first from the second. This gives $c_1W = y_0y_2'(t_0) - y_0'y_2(t_0)$ and $c_2W = -y_0y_1'(t_0) + y_0'y_1(t_0)$, so (8) has the unique solution
>
> $$
> c_1 = \frac{y_0y_2'(t_0) - y_0'y_2(t_0)}{y_1(t_0)y_2'(t_0) - y_1'(t_0)y_2(t_0)}, \qquad
> c_2 = \frac{-y_0y_1'(t_0) + y_0'y_1(t_0)}{y_1(t_0)y_2'(t_0) - y_1'(t_0)y_2(t_0)} , \qquad (10)
> $$
>
> or, in terms of determinants,
>
> $$
> c_1 = \frac{\begin{vmatrix} y_0 & y_2(t_0) \\ y_0' & y_2'(t_0) \end{vmatrix}}{\begin{vmatrix} y_1(t_0) & y_2(t_0) \\ y_1'(t_0) & y_2'(t_0) \end{vmatrix}}, \qquad
> c_2 = \frac{\begin{vmatrix} y_1(t_0) & y_0 \\ y_1'(t_0) & y_0' \end{vmatrix}}{\begin{vmatrix} y_1(t_0) & y_2(t_0) \\ y_1'(t_0) & y_2'(t_0) \end{vmatrix}} . \qquad (11)
> $$
>
> (Substituting (10) back into (8) confirms it.) With these constants, $y = c_1y_1 + c_2y_2$ satisfies (2) and (3), whatever $y_0$ and $y_0'$ are.
>
> **If $W = 0$.** The denominators in (10) and (11) vanish, and (8) has no solution unless $y_0$ and $y_0'$ also make the numerators zero. (BDP asserts this; here is why. $W = 0$ says that the columns $(y_1(t_0), y_1'(t_0))$ and $(y_2(t_0), y_2'(t_0))$ of the coefficient matrix are proportional. Then every left side $c_1(y_1(t_0), y_1'(t_0)) + c_2(y_2(t_0), y_2'(t_0))$ lies on one line through the origin of the plane, or is $(0, 0)$, and any $(y_0, y_0')$ off that line cannot be reached.) So there are many initial conditions that no choice of $c_1$, $c_2$ satisfies.

^pf-14-3

*Uses:* [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-2|§14.2]], [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^def-14-2|Def. §14.2]]

> [!remark]- Connections
> - $W$ is the $2 \times 2$ determinant ([[§20 Introduction to Determinants#^def-20-2|235 Def. §20.2]]) of the coefficient matrix of (8), and the system is solvable for every right side exactly when that matrix is invertible, [[§21 Properties of Determinants#^thm-21-3|235 Thm. §21.3]] (for $2 \times 2$: [[§12 The Inverse of a Matrix#^thm-12-2|235 Thm. §12.2]]). Formula (11) is Cramer's rule, [[§22 Cramer’s Rule, Volume, and Linear Transformations#^thm-22-1|235 Thm. §22.1]].

> [!example] Example §14.2: Distinct Exponentials Form a Fundamental Set
> **(a)** By [[§13 Homogeneous Differential Equations with Constant Coefficients#^ex-13-2|Example §13.2]], $y_1(t) = e^{-2t}$ and $y_2(t) = e^{-3t}$ solve $y'' + 5y' + 6y = 0$. Their Wronskian is
>
> $$
> W[e^{-2t}, e^{-3t}] = \begin{vmatrix} e^{-2t} & e^{-3t} \\ -2e^{-2t} & -3e^{-3t} \end{vmatrix} = -3e^{-5t} + 2e^{-5t} = -e^{-5t} .
> $$
>
> It is nonzero for every $t$, so by Theorem §14.3 combinations of $y_1$, $y_2$ meet initial conditions prescribed at any point.
>
> **(b)** In general, suppose $y_1 = e^{r_1t}$ and $y_2 = e^{r_2t}$ solve an equation (2), with $r_1 \ne r_2$. Then
>
> $$
> W = \begin{vmatrix} e^{r_1t} & e^{r_2t} \\ r_1e^{r_1t} & r_2e^{r_2t} \end{vmatrix} = (r_2 - r_1)\exp[(r_1 + r_2)t] ,
> $$
>
> which is never zero because the exponential never vanishes and $r_2 - r_1 \ne 0$. So $y_1$, $y_2$ form a fundamental set ([[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^def-14-3|Definition §14.3]]), and $c_1e^{r_1t} + c_2e^{r_2t}$ is the general solution, as claimed in [[§13 Homogeneous Differential Equations with Constant Coefficients#^thm-13-2|Theorem §13.2]].
>
> *BDP: Examples 3.2.3 and 3.2.4*

^ex-14-2

## Fundamental Sets of Solutions

> [!theorem] Theorem §14.4: The General Solution
> Suppose that $y_1$ and $y_2$ are two solutions of the second-order linear differential equation (2), $L[y] = y'' + p(t)y' + q(t)y = 0$. Then the two-parameter family of solutions
>
> $$
> y = c_1y_1(t) + c_2y_2(t)
> $$
>
> with arbitrary coefficients $c_1$ and $c_2$ includes every solution of (2) if and only if there is a point $t_0$ where the Wronskian of $y_1$ and $y_2$ is not zero.
>
> *BDP: Theorem 3.2.4*

^thm-14-4

> [!proof]+ Proof
> **If $W[y_1, y_2](t_0) \ne 0$ for some $t_0$.** Let $\phi$ be any solution of (2), and put $y_0 = \phi(t_0)$, $y_0' = \phi'(t_0)$. Then $\phi$ solves the initial value problem
>
> $$
> y'' + p(t)y' + q(t)y = 0, \qquad y(t_0) = y_0, \quad y'(t_0) = y_0' . \qquad (12)
> $$
>
> Since $W[y_1, y_2](t_0) \ne 0$, Theorem §14.3 gives $c_1$, $c_2$ (by (10) or (11)) such that $y = c_1y_1(t) + c_2y_2(t)$ also solves the initial value problem (12). By the uniqueness part of [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|Theorem §14.1]] the two solutions of (12) are the same function:
>
> $$
> \phi(t) = c_1y_1(t) + c_2y_2(t) . \qquad (13)
> $$
>
> So $\phi$ belongs to the family, and since $\phi$ was an arbitrary solution, every solution does.
>
> **If $W[y_1, y_2](t_0) = 0$ for every $t_0$.** Pick any $t_0 \in I$. By Theorem §14.3 there are values $y_0$, $y_0'$ for which no $c_1$, $c_2$ satisfy the system (8). Let $\phi$ be the solution of (2) with $\phi(t_0) = y_0$, $\phi'(t_0) = y_0'$, which exists by Theorem §14.1. If $\phi$ were $c_1y_1 + c_2y_2$, then evaluating it and its derivative at $t_0$ would give constants solving (8). So $\phi$ is not in the family, and the linear combinations of $y_1$ and $y_2$ do not include all solutions.

^pf-14-4

*Uses:* [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|§14.1]], [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-3|§14.3]]

> [!definition] Definition §14.3: General Solution; Fundamental Set of Solutions
> If $y_1$ and $y_2$ are solutions of (2) whose Wronskian is not everywhere zero, the expression
>
> $$
> y = c_1y_1(t) + c_2y_2(t)
> $$
>
> with arbitrary constant coefficients is called the **general solution** of (2), and $y_1$ and $y_2$ are said to form a **fundamental set of solutions** of (2). By Theorem §14.4 the general solution contains all solutions. So to find all solutions of (2) one needs only two solutions with nonzero Wronskian.
>
> *BDP: 3.2 (text)*

^def-14-3

> [!remark]- Connections
> - The map $y \mapsto (y(t_0), y'(t_0))$ from the solution space to $\mathbb{R}^2$ is an isomorphism ([[§10 Invertibility and Isomorphisms#^ladr-3-69|LADR 3.69]]; see the remark below), so the solution space has dimension $2$ ([[§10 Invertibility and Isomorphisms#^ladr-3-70|LADR 3.70]]), and two linearly independent solutions are automatically a basis ([[§6 Dimension#^ladr-2-38|LADR 2.38]], [[§27 The Dimension of a Vector Space#^thm-27-5|235 Thm. §27.5]]).
> - Linear independence of functions, such as $\sin t$ and $\cos t$ in $C[0, 1]$: [[§25 Linearly Independent Sets; Bases#^ex-25-1|235 Ex. §25.1]].

> [!remark] Remark: The Solution Space Is a Two-Dimensional Vector Space
> The theorems so far fit together into one statement of linear algebra. Let $S$ be the set of all solutions of $L[y] = 0$ on $I$.
> 1. **$S$ is a vector space.** It contains $0$, and by [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-2|Theorem §14.2]] it is closed under linear combinations: it is the null space of the linear map $L$.
> 2. **$\dim S = 2$.** Fix $t_0 \in I$ and let $\Phi(y) = (y(t_0), y'(t_0))$, a linear map $S \to \mathbb{R}^2$. The existence part of [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|Theorem §14.1]] says that $\Phi$ is onto. The uniqueness part says that $\Phi$ is one-to-one: if $\Phi(y) = (0, 0)$ then $y = 0$ by [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^ex-14-1|Example §14.1(b)]]. So $\Phi$ is an isomorphism and $S$ has dimension $2$.
> 3. **Fundamental set = basis.** $\Phi(y_1)$ and $\Phi(y_2)$ are the columns of the matrix in (9), so $W[y_1, y_2](t_0) \ne 0$ exactly when they form a basis of $\mathbb{R}^2$, that is, exactly when $y_1$, $y_2$ form a basis of $S$. The general solution $c_1y_1 + c_2y_2$ is the statement that every vector is a combination of basis vectors, and $c_1$, $c_2$ in (11) are its coordinates.
> 4. **Independence.** Two solutions of (2) are linearly independent if and only if their Wronskian is nonzero at one point, and then ([[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-8|Theorem §14.8]]) at every point of $I$. Theorem §14.5 below picks the basis $\Phi^{-1}(1, 0)$, $\Phi^{-1}(0, 1)$, and [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^ex-14-4|Example §14.4]] shows two different bases of the same $S$.

^rem-14-2

> [!example] Example §14.3: A Fundamental Set on the Midterm
> Consider $y'' - 3y' - 10y = 0$. **(a)** Find two solutions that can be used to build the general solution (a fundamental set). **(b)** Use the Wronskian to prove that they form a fundamental set. **(c)** Find the general solution.
>
> **(a)** The characteristic equation $r^2 - 3r - 10 = (r - 5)(r + 2) = 0$ has roots $5$ and $-2$, so by [[§13 Homogeneous Differential Equations with Constant Coefficients#^thm-13-1|Theorem §13.1]] $y_1 = e^{5t}$ and $y_2 = e^{-2t}$ are solutions.
>
> **(b)**
>
> $$
> W[e^{5t}, e^{-2t}] = \begin{vmatrix} e^{5t} & e^{-2t} \\ 5e^{5t} & -2e^{-2t} \end{vmatrix} = -2e^{3t} - 5e^{3t} = -7e^{3t} \ne 0
> $$
>
> for every $t$, so $y_1$, $y_2$ form a fundamental set (Definition §14.3).
>
> **(c)** By Theorem §14.4 the general solution is $y = c_1e^{5t} + c_2e^{-2t}$.
>
> The Summer 2023 midterm asked the same for $y'' - 6y' + 8y = 0$: the roots are $4$ and $2$, and $W[e^{4t}, e^{2t}] = e^{4t} \cdot 2e^{2t} - 4e^{4t} \cdot e^{2t} = -2e^{6t} \ne 0$, so the general solution is $y = c_1e^{4t} + c_2e^{2t}$. The order matters only for the sign: $W[y_2, y_1] = -W[y_1, y_2]$.
>
> *Source: 331 Midterm (Fall 2021), Q3; 331 Midterm (Summer 2023), Q1*

^ex-14-3

> [!theorem] Theorem §14.5: A Fundamental Set Always Exists
> Consider the differential equation (2), $L[y] = y'' + p(t)y' + q(t)y = 0$, whose coefficients $p$ and $q$ are continuous on some open interval $I$. Choose some point $t_0$ in $I$. Let $y_1$ be the solution of (2) that also satisfies
>
> $$
> y(t_0) = 1, \qquad y'(t_0) = 0 ,
> $$
>
> and let $y_2$ be the solution of (2) that satisfies
>
> $$
> y(t_0) = 0, \qquad y'(t_0) = 1 .
> $$
>
> Then $y_1$ and $y_2$ form a fundamental set of solutions of (2).
>
> *BDP: Theorem 3.2.5*

^thm-14-5

> [!proof]+ Proof
> The solutions $y_1$ and $y_2$ exist by the existence part of [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|Theorem §14.1]]. Their Wronskian at $t_0$ is
>
> $$
> W[y_1, y_2](t_0) = \begin{vmatrix} y_1(t_0) & y_2(t_0) \\ y_1'(t_0) & y_2'(t_0) \end{vmatrix} = \begin{vmatrix} 1 & 0 \\ 0 & 1 \end{vmatrix} = 1 \ne 0 ,
> $$
>
> so they form a fundamental set by Definition §14.3 (and Theorem §14.4).
>
> The difficult part, the existence of the two solutions, is carried by Theorem §14.1. The theorem does not say how to find $y_1$ and $y_2$; it only guarantees that a fundamental set always exists.

^pf-14-5

*Uses:* [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|§14.1]], [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^def-14-3|Def. §14.3]], [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-4|§14.4]]

> [!example] Example §14.4: The Fundamental Set of Theorem §14.5
> Find the fundamental set $y_1$, $y_2$ specified by Theorem §14.5 for $y'' - y = 0$ with initial point $t_0 = 0$.
>
> The solutions $e^t$ and $e^{-t}$ from [[§13 Homogeneous Differential Equations with Constant Coefficients#^ex-13-1|Example §13.1]] form a fundamental set, since $W[e^t, e^{-t}](t) = e^t(-e^{-t}) - e^te^{-t} = -2 \ne 0$. But they are not the ones of the theorem, because they do not satisfy its initial conditions at $t = 0$.
>
> The general solution is $y = c_1e^t + c_2e^{-t}$. The solution $y_3$ with $y(0) = 1$, $y'(0) = 0$ needs $c_1 + c_2 = 1$ and $c_1 - c_2 = 0$, so $c_1 = c_2 = \frac12$:
>
> $$
> y_3(t) = \tfrac12e^t + \tfrac12e^{-t} = \cosh t .
> $$
>
> The solution $y_4$ with $y(0) = 0$, $y'(0) = 1$ needs $c_1 + c_2 = 0$ and $c_1 - c_2 = 1$, so $c_1 = \frac12$, $c_2 = -\frac12$:
>
> $$
> y_4(t) = \tfrac12e^t - \tfrac12e^{-t} = \sinh t .
> $$
>
> Their Wronskian is $W[y_3, y_4](t) = \cosh^2 t - \sinh^2 t = 1$, so they too form a fundamental set, and the general solution can also be written
>
> $$
> y = k_1\cosh t + k_2\sinh t . \qquad (20)
> $$
>
> The constants $k_1$, $k_2$ are not the same as $c_1$, $c_2$. A differential equation has infinitely many fundamental sets; choose the most convenient one.
>
> *BDP: Example 3.2.6*

^ex-14-4

## Complex-Valued Solutions

> [!theorem] Theorem §14.6: Real and Imaginary Parts of a Complex Solution
> Consider again the equation (2), $L[y] = y'' + p(t)y' + q(t)y = 0$, where $p$ and $q$ are continuous real-valued functions. If $y = u(t) + iv(t)$ is a complex-valued solution of (2), then its real part $u$ and its imaginary part $v$ are also solutions of this equation.
>
> *BDP: Theorem 3.2.6*

^thm-14-6

> [!proof]+ Proof
> Substitute $u(t) + iv(t)$ for $y$ in $L[y]$ (derivatives of a complex-valued function are taken separately on its real and imaginary parts):
>
> $$
> L[y](t) = u''(t) + iv''(t) + p(t)\big(u'(t) + iv'(t)\big) + q(t)\big(u(t) + iv(t)\big) . \qquad (21)
> $$
>
> Because $p(t)$ and $q(t)$ are real, (21) separates into real and imaginary parts:
>
> $$
> L[y](t) = \big(u''(t) + p(t)u'(t) + q(t)u(t)\big) + i\big(v''(t) + p(t)v'(t) + q(t)v(t)\big) = L[u](t) + iL[v](t) ,
> $$
>
> with $L[u](t)$ and $L[v](t)$ real. A complex number is zero if and only if its real and imaginary parts are both zero. Since $L[y] = 0$, both $L[u] = 0$ and $L[v] = 0$: the real-valued functions $u$ and $v$ are solutions of (2).

^pf-14-6

*Uses:* [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^def-14-1|Def. §14.1]]

> [!theorem] Corollary §14.7: The Conjugate of a Solution
> If $y = u(t) + iv(t)$ is a complex-valued solution of (2), with $p$ and $q$ real, then its complex conjugate $\bar y = u(t) - iv(t)$ is also a solution.
>
> *BDP: 3.2 (text)*

^cor-14-7

> [!proof]+ Proof
> By Theorem §14.6, $u$ and $v$ are solutions. Then $\bar y = u + (-i)v$ is a linear combination of two solutions, hence a solution by [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-2|Theorem §14.2]] (whose proof allows complex constants). BDP notes that an argument like the proof of Theorem §14.6 works as well: conjugating $L[y] = 0$ gives $L[\bar y] = 0$, again because $p$ and $q$ are real.

^pf-14-7

*Uses:* [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-6|§14.6]], [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-2|§14.2]]

## Abel's Theorem

> [!theorem] Theorem §14.8: Abel's Theorem
> If $y_1$ and $y_2$ are solutions of the second-order linear differential equation
>
> $$
> L[y] = y'' + p(t)y' + q(t)y = 0 , \qquad (22)
> $$
>
> where $p$ and $q$ are continuous on an open interval $I$, then the Wronskian $W[y_1, y_2](t)$ is given by
>
> $$
> W[y_1, y_2](t) = c\exp\Big(-\int p(t)\,dt\Big) , \qquad (23)
> $$
>
> where $c$ is a certain constant that depends on $y_1$ and $y_2$, but not on $t$. Further, $W[y_1, y_2](t)$ either is zero for all $t$ in $I$ (if $c = 0$) or else is never zero in $I$ (if $c \ne 0$).
>
> *BDP: Theorem 3.2.7*

^thm-14-8

> [!proof]+ Proof
> The solutions satisfy
>
> $$
> \begin{aligned}
> y_1'' + p(t)y_1' + q(t)y_1 &= 0, \\
> y_2'' + p(t)y_2' + q(t)y_2 &= 0 .
> \end{aligned} \qquad (24)
> $$
>
> Multiply the first equation by $-y_2$, the second by $y_1$, and add. The terms with $q$ cancel, and
>
> $$
> (y_1y_2'' - y_1''y_2) + p(t)(y_1y_2' - y_1'y_2) = 0 . \qquad (25)
> $$
>
> Let $W(t) = W[y_1, y_2](t) = y_1y_2' - y_1'y_2$. By the product rule $W' = y_1'y_2' + y_1y_2'' - y_1''y_2 - y_1'y_2'$, that is,
>
> $$
> W' = y_1y_2'' - y_1''y_2 . \qquad (26)
> $$
>
> So (25) reads
>
> $$
> W' + p(t)W = 0 . \qquad (27)
> $$
>
> This is a first-order equation that is both linear ([[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-2|Theorem §4.2]]) and separable ([[§5 Separable Differential Equations#^thm-5-1|Theorem §5.1]]). With the integrating factor $\mu(t) = \exp\big(\int p(t)\,dt\big)$ (an antiderivative of $p$ exists on $I$ because $p$ is continuous), (27) becomes $(\mu W)' = 0$, so $\mu W = c$ for a constant $c$ on the interval $I$, and
>
> $$
> W(t) = c\exp\Big(-\int p(t)\,dt\Big) . \qquad (28)
> $$
>
> The value of $c$ depends on which pair of solutions is used. Since the exponential function is never zero, $W(t)$ is not zero unless $c = 0$, in which case $W(t)$ is zero for all $t$.

^pf-14-8

*Uses:* [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^def-14-2|Def. §14.2]], [[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-2|§4.2]]

> [!remark] Remark: Consequences of Abel's Theorem
> - The Wronskians of any two fundamental sets of the same equation differ only by a multiplicative constant, and the Wronskian of any fundamental set can be found, up to that constant, without solving the equation.
> - Since $W$ is either always zero or never zero on $I$, it can be tested at any single convenient value of $t$. This is why "nonzero at one point" in [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-4|Theorem §14.4]] and "not everywhere zero" in Definition §14.3 are the same condition.

^rem-14-3

> [!example] Example §14.5: A Fundamental Set for a Variable-Coefficient Equation
> Show that $y_1(t) = t^{1/2}$ and $y_2(t) = t^{-1}$ form a fundamental set of solutions of
>
> $$
> 2t^2y'' + 3ty' - y = 0, \qquad t > 0 , \qquad (14)
> $$
>
> and check that their Wronskian is given by Abel's formula (23).
>
> **Solutions.** $y_1' = \frac12t^{-1/2}$ and $y_1'' = -\frac14t^{-3/2}$, so
>
> $$
> 2t^2\Big(-\tfrac14t^{-3/2}\Big) + 3t\Big(\tfrac12t^{-1/2}\Big) - t^{1/2} = \Big(-\tfrac12 + \tfrac32 - 1\Big)t^{1/2} = 0 .
> $$
>
> $y_2' = -t^{-2}$ and $y_2'' = 2t^{-3}$, so $2t^2(2t^{-3}) + 3t(-t^{-2}) - t^{-1} = (4 - 3 - 1)t^{-1} = 0$.
>
> **Wronskian.**
>
> $$
> W = \begin{vmatrix} t^{1/2} & t^{-1} \\ \frac12t^{-1/2} & -t^{-2} \end{vmatrix} = -t^{-3/2} - \tfrac12t^{-3/2} = -\tfrac32t^{-3/2} . \qquad (15)
> $$
>
> Since $W \ne 0$ for $t > 0$, $y_1$ and $y_2$ form a fundamental set there, and the general solution is $y = c_1t^{1/2} + c_2t^{-1}$ for $t > 0$. (How to find these solutions: the Euler equations of BDP Problem 3.3.25, which MATH 331 did not cover.)
>
> **Abel's formula.** In the standard form with leading coefficient $1$ the equation is $y'' + \frac{3}{2t}y' - \frac{1}{2t^2}y = 0$, so $p(t) = \frac{3}{2t}$ and
>
> $$
> W[y_1, y_2](t) = c\exp\Big(-\int\frac{3}{2t}\,dt\Big) = c\exp\Big(-\tfrac32\ln t\Big) = ct^{-3/2} . \qquad (30)
> $$
>
> This is the Wronskian of any pair of solutions of (14); for the pair above, $c = -\frac32$, in agreement with (15).
>
> *BDP: Examples 3.2.5 and 3.2.7*

^ex-14-5

> [!remark]- Connections
> - See also: [[§1★ Homogeneous Linear Equations#^thm-1-5|341 Thm. §1.5]] (Cauchy–Euler equations $t^2u'' + ktu' + pu = 0$, which MATH 331 did not cover: the trial solution $t^m$ gives the characteristic equation $m(m - 1) + km + p = 0$; for the equation here, divided by $2$, its roots are $\frac12$ and $-1$), with examples in [[§1★ Homogeneous Linear Equations#^ex-1-3|341 Ex. §1.3]].

> [!remark] Remark: Method — Finding the General Solution of y″ + p(t)y′ + q(t)y = 0
> To find the general solution of $y'' + p(t)y' + q(t)y = 0$ on $\alpha < t < \beta$:
> 1. Find two functions $y_1$ and $y_2$ that satisfy the differential equation in $\alpha < t < \beta$.
> 2. Make sure that there is a point in the interval where their Wronskian $W = y_1y_2' - y_1'y_2$ is nonzero (by [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-8|Theorem §14.8]], any one convenient point will do).
> 3. Then $y_1$ and $y_2$ form a fundamental set, and the general solution is $y = c_1y_1(t) + c_2y_2(t)$ with arbitrary constants $c_1$, $c_2$.
> 4. If initial conditions are prescribed at a point of $\alpha < t < \beta$, choose $c_1$ and $c_2$ to satisfy them, by solving (8) or with (10).

^rem-14-4
