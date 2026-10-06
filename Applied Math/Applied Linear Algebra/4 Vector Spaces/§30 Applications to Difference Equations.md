---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 4
section: 30
lay: "4.8"
aliases: ["Lay 4.8"]
tags: [applied-linear-algebra, math235]
---
← [[§29 Change of Basis]] · ↑ [[· 4 Vector Spaces]] · [[§31 Applications to Markov Chains]] →

*Lay, Section 4.8 · MATH 235 lecture L18.*

Discrete data (sampled music, yearly populations, monthly loan balances) are sequences, and the equations that govern them are difference equations, the discrete counterpart of differential equations. This section applies the vector space ideas of Chapter 4 to the space $\mathbb{S}$ of signals. The solutions of a homogeneous linear difference equation of order $n$ form an $n$-dimensional subspace of $\mathbb{S}$, so by the Basis Theorem any $n$ linearly independent solutions (found from the roots of the auxiliary equation and checked with the Casorati matrix) give all solutions. A nonhomogeneous equation has the general solution "particular solution plus homogeneous solutions", exactly as for $A\mathbf{x} = \mathbf{b}$. The Fibonacci numbers of lecture L18 are the standard example. Finally, every such equation can be rewritten as a first-order system $\mathbf{x}_{k+1} = A\mathbf{x}_k$, the form studied with eigenvectors in Chapter 5.

## Discrete-Time Signals

> [!definition] Definition §30.1: Signals; the Space 𝕊
> A **signal** is a function defined only on the integers, visualized as a doubly infinite sequence of numbers $\{y_k\} = (\ldots, y_{-2}, y_{-1}, y_0, y_1, y_2, \ldots)$; examples are $\{(.7)^k\}$, $\{1^k\}$ and $\{(-1)^k\}$. The signals form the vector space $\mathbb{S}$ of Section 4.1 ([[§23 Vector Spaces and Subspaces#^ex-23-1|Example §23.1]](c)), with termwise addition and scalar multiplication. When a process begins at a specific time, a signal may be written $(y_0, y_1, y_2, \ldots)$, the terms with $k < 0$ being zero or omitted.
>
> *Lay: 4.8 (text); 4.1, Example 3*

^def-30-1

Signals arise wherever a process is measured, or *sampled*, at discrete time intervals. A compact disc stores music sampled $44{,}100$ times per second: the amplitude $y_k$ at each measurement, and the sequence $\{y_k\}$ contains enough information to reproduce all frequencies up to about $20{,}000$ cycles per second, beyond human hearing (Lay, Example 4.8.1).

## Linear Independence in the Space 𝕊 of Signals

Three signals $\{u_k\}$, $\{v_k\}$, $\{w_k\}$ are linearly independent precisely when

$$
c_1 u_k + c_2 v_k + c_3 w_k = 0 \quad \text{for all } k \qquad (1)
$$

implies $c_1 = c_2 = c_3 = 0$. "For all $k$" means all integers $k$ (or all $k \ge 0$ for signals that start at $k = 0$).

> [!definition] Definition §30.2: Casorati Matrix; Casoratian
> The **Casorati matrix** of the signals $\{u_k\}$, $\{v_k\}$, $\{w_k\}$ is
>
> $$
> C(k) = \begin{bmatrix} u_k & v_k & w_k \\ u_{k+1} & v_{k+1} & w_{k+1} \\ u_{k+2} & v_{k+2} & w_{k+2} \end{bmatrix},
> $$
>
> and its determinant is the **Casoratian** of the signals. For $n$ signals, $C(k)$ is the $n \times n$ matrix whose rows list the values at $k, k+1, \ldots, k+n-1$.
>
> *Lay: 4.8 (text)*

^def-30-2

> [!theorem] Proposition §30.1: The Casorati Test
> If the Casorati matrix $C(k)$ of $n$ signals is invertible for at least one value of $k$, then the signals are linearly independent.
>
> *Lay: 4.8 (text)*

^prop-30-1

> [!proof]+ Proof
> Take $n = 3$ (the general case is the same). Suppose $c_1, c_2, c_3$ satisfy (1). Then (1) holds for any three consecutive values of $k$, say $k$, $k + 1$ and $k + 2$:
>
> $$
> c_1 u_{k+1} + c_2 v_{k+1} + c_3 w_{k+1} = 0, \qquad c_1 u_{k+2} + c_2 v_{k+2} + c_3 w_{k+2} = 0 \qquad \text{for all } k .
> $$
>
> Together with (1) this says $C(k)\,\mathbf{c} = \mathbf{0}$ for all $k$, where $\mathbf{c} = (c_1, c_2, c_3)$. If $C(k_0)$ is invertible for one $k_0$, then $\mathbf{c} = C(k_0)^{-1}\mathbf{0} = \mathbf{0}$. So $c_1 = c_2 = c_3 = 0$ and the signals are independent.

^pf-30-1

*Uses:* [[§12 The Inverse of a Matrix#^thm-12-3|§12.3]] (solving with an inverse)

If no Casorati matrix is invertible, the signals may or may not be linearly independent (Lay, Exercise 33: $k^2$ and $2k|k|$). For solutions of one homogeneous difference equation, however, the test is decisive: [[§30 Applications to Difference Equations#^prop-30-6|Proposition §30.6]].

> [!example] Example §30.1: A Casorati Matrix
> Verify that $1^k$, $(-2)^k$ and $3^k$ are linearly independent signals.
>
> The Casorati matrix is
>
> $$
> C(k) = \begin{bmatrix} 1^k & (-2)^k & 3^k \\ 1^{k+1} & (-2)^{k+1} & 3^{k+1} \\ 1^{k+2} & (-2)^{k+2} & 3^{k+2} \end{bmatrix} .
> $$
>
> Row operations show fairly easily that $C(k)$ is always invertible, but it is faster to substitute one value, say $k = 0$, and row reduce the numerical matrix. Subtract row 1 from rows 2 and 3, then add row 2 to row 3:
>
> $$
> C(0) = \begin{bmatrix} 1 & 1 & 1 \\ 1 & -2 & 3 \\ 1 & 4 & 9 \end{bmatrix}
> \sim \begin{bmatrix} 1 & 1 & 1 \\ 0 & -3 & 2 \\ 0 & 3 & 8 \end{bmatrix}
> \sim \begin{bmatrix} 1 & 1 & 1 \\ 0 & -3 & 2 \\ 0 & 0 & 10 \end{bmatrix} .
> $$
>
> Three pivots, so $C(0)$ is invertible, and $1^k$, $(-2)^k$, $3^k$ are linearly independent by Proposition §30.1.
>
> *Lay: Example 4.8.2*

^ex-30-1

## Linear Difference Equations

> [!definition] Definition §30.3: Linear Difference Equation
> Given scalars $a_0, \ldots, a_n$ with $a_0$ and $a_n$ nonzero, and a signal $\{z_k\}$, the equation
>
> $$
> a_0 y_{k+n} + a_1 y_{k+n-1} + \cdots + a_{n-1} y_{k+1} + a_n y_k = z_k \quad \text{for all } k \qquad (3)
> $$
>
> is a **linear difference equation** (or **linear recurrence relation**) **of order $n$**. Often $a_0 = 1$. If $\{z_k\}$ is the zero sequence, the equation is **homogeneous**; otherwise it is **nonhomogeneous**. A signal $\{y_k\}$ that satisfies (3) is a **solution**.
>
> In digital signal processing, (3) describes a **linear filter** with **filter coefficients** $a_0, \ldots, a_n$: the input $\{y_k\}$ is turned into the output $\{z_k\}$, and the solutions of the homogeneous equation are the signals that are filtered *out*, turned into the zero signal.
>
> *Lay: 4.8 (text and Example 4.8.3)*

^def-30-3

> [!example] Example §30.2: A Low-Pass Filter
> Feed two signals into the filter
>
> $$
> .35\,y_{k+2} + .5\,y_{k+1} + .35\,y_k = z_k ,
> $$
>
> where $.35$ abbreviates $\sqrt2/4$ (so that $.35(.7)$ abbreviates $(\sqrt2/4)(\sqrt2/2) = .25$, and $.7$ abbreviates $\sqrt2/2$).
>
> **Low frequency passes.** Sample $y = \cos(\pi t/4)$ at the integers: $y_k = \cos(\pi k/4)$, that is, $\{y_k\} = (\ldots, 1, .7, 0, -.7, -1, -.7, 0, .7, 1, \ldots)$ with $y_0 = 1$. The first rows of the computation:
>
> | $k$ | $y_k$ | $y_{k+1}$ | $y_{k+2}$ | $.35y_k + .5y_{k+1} + .35y_{k+2}$ | $z_k$ |
> |---|---|---|---|---|---|
> | $0$ | $1$ | $.7$ | $0$ | $.35(1) + .5(.7) + .35(0)$ | $.7$ |
> | $1$ | $.7$ | $0$ | $-.7$ | $.35(.7) + .5(0) + .35(-.7)$ | $0$ |
> | $2$ | $0$ | $-.7$ | $-1$ | $.35(0) + .5(-.7) + .35(-1)$ | $-.7$ |
> | $3$ | $-.7$ | $-1$ | $-.7$ | $.35(-.7) + .5(-1) + .35(-.7)$ | $-1$ |
>
> The output is $\{y_k\}$ shifted by one term: $z_k = y_{k+1}$. Exactly: with $\theta = \pi(k + 1)/4$, the identity $\cos(\theta - \alpha) + \cos(\theta + \alpha) = 2\cos\theta\cos\alpha$ for $\alpha = \pi/4$ gives
>
> $$
> z_k = \tfrac{\sqrt2}{4}\big[\cos(\theta - \tfrac{\pi}{4}) + \cos(\theta + \tfrac{\pi}{4})\big] + \tfrac12\cos\theta = \tfrac{\sqrt2}{4} \cdot 2 \cdot \tfrac{\sqrt2}{2}\cos\theta + \tfrac12\cos\theta = \cos\theta = y_{k+1} .
> $$
>
> **High frequency is stopped.** Sample the higher-frequency $y = \cos(3\pi t/4)$: $w_k = \cos(3\pi k/4)$, that is, $\{w_k\} = (\ldots, 1, -.7, 0, .7, -1, .7, 0, -.7, 1, \ldots)$. The same identity with $\theta = 3\pi(k + 1)/4$ and $\alpha = 3\pi/4$, $\cos\alpha = -\sqrt2/2$, gives
>
> $$
> \tfrac{\sqrt2}{4} \cdot 2 \cdot \big(-\tfrac{\sqrt2}{2}\big)\cos\theta + \tfrac12\cos\theta = -\tfrac12\cos\theta + \tfrac12\cos\theta = 0 .
> $$
>
> The output is the zero sequence: $\{w_k\}$ solves the homogeneous equation. The filter lets the low frequency pass and stops the high one; it is a **low-pass filter**.
>
> *Lay: Example 4.8.3*

^ex-30-2

![[m235-30-1.svg]]
*Example §30.2. Top: the input $y_k = \cos(\pi k/4)$ (blue stems, sampled from the blue curve) and the filter's output $z_k = y_{k+1}$ (red circles), the same wave shifted one step to the left. Bottom: the input $w_k = \cos(3\pi k/4)$, sampled from a faster wave; the output is $0$ for every $k$ (red circles on the axis).*

Solutions of a homogeneous equation are often of the form $y_k = r^k$.

> [!definition] Definition §30.4: Auxiliary Equation
> The **auxiliary equation** of the homogeneous difference equation
>
> $$
> y_{k+n} + a_1 y_{k+n-1} + \cdots + a_{n-1} y_{k+1} + a_n y_k = 0 \quad \text{for all } k
> $$
>
> is the polynomial equation
>
> $$
> r^n + a_1 r^{n-1} + \cdots + a_{n-1} r + a_n = 0 .
> $$
>
> *Lay: 4.8 (text)*

^def-30-4

> [!theorem] Proposition §30.2: Exponential Solutions
> A nonzero signal $\{r^k\}$ ($r \ne 0$) satisfies the homogeneous difference equation of Definition §30.4 if and only if $r$ is a root of its auxiliary equation.
>
> *Lay: 4.8 (text and Example 4.8.4)*

^prop-30-2

> [!proof]+ Proof
> Substitute $y_k = r^k$ and factor out $r^k$:
>
> $$
> r^{k+n} + a_1 r^{k+n-1} + \cdots + a_n r^k = r^k\,(r^n + a_1 r^{n-1} + \cdots + a_n) .
> $$
>
> Since $r^k \ne 0$, this is $0$ for all $k$ exactly when $r^n + a_1 r^{n-1} + \cdots + a_n = 0$.

^pf-30-2

*Uses:* [[§30 Applications to Difference Equations#^def-30-4|Def. §30.4]]

> [!remark] Remark: Repeated and Complex Roots
> Lay does not treat repeated roots of the auxiliary equation (then $\{r^k\}$ gives fewer than $n$ solutions; a root $r$ of multiplicity two also gives $\{k r^k\}$, as in Exercise 5). Lecture L18 poses the recurrence $A_{n+1} = 2A_n - A_{n-1}$ as an exercise (the left side is written $A_n$ there), asking for a formula of the Fibonacci shape $(\mu_1^n - \mu_2^n)/c$; its auxiliary equation $r^2 - 2r + 1 = (r - 1)^2$ has the double root $1$, so that shape does not apply, and the solutions are $\{1\}$ and $\{k\}$: $A_k = c_1 + c_2 k$, the arithmetic progressions (Casorati matrix at $k = 0$: $\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$, invertible). When the auxiliary equation has a complex root, the difference equation has real solutions of the form $s^k\cos k\omega$ and $s^k\sin k\omega$ for constants $s$ and $\omega$: the signal $w_k = \cos(3\pi k/4)$ of Example §30.2 is one ($s = 1$, $\omega = 3\pi/4$; the auxiliary equation $.35r^2 + .5r + .35 = 0$ has the roots $e^{\pm 3\pi i/4}$). Complex numbers and $e^{i\theta}$: [[§53 Complex Numbers#^rem-53-1|Remark: Euler's Formula]]. For differential equations the same substitution, $y = e^{rt}$ in place of $y_k = r^k$, leads to the characteristic equation: [[§13 Homogeneous Differential Equations with Constant Coefficients#^thm-13-1|331 Thm. §13.1]].

^rem-30-1

## Solution Sets of Linear Difference Equations

> [!theorem] Proposition §30.3: The Solutions Form a Subspace
> Given $a_1, \ldots, a_n$, the map $T : \mathbb{S} \to \mathbb{S}$ that sends $\{y_k\}$ to $\{w_k\}$,
>
> $$
> w_k = y_{k+n} + a_1 y_{k+n-1} + \cdots + a_{n-1} y_{k+1} + a_n y_k ,
> $$
>
> is a linear transformation. Hence the solution set of the homogeneous equation $y_{k+n} + a_1 y_{k+n-1} + \cdots + a_n y_k = 0$ for all $k$ is the kernel of $T$, a subspace of $\mathbb{S}$: any linear combination of solutions is again a solution.
>
> *Lay: 4.8 (text)*

^prop-30-3

> [!proof]+ Proof
> ("It is readily checked", says Lay.) For signals $\{y_k\}$, $\{y'_k\}$ and a scalar $c$, the $k$th term of $T(\{y_k + y'_k\})$ is
>
> $$
> (y_{k+n} + y'_{k+n}) + a_1 (y_{k+n-1} + y'_{k+n-1}) + \cdots + a_n (y_k + y'_k) ,
> $$
>
> which regroups as the $k$th term of $T\{y_k\}$ plus the $k$th term of $T\{y'_k\}$; likewise the $k$th term of $T\{c y_k\}$ is $c$ times that of $T\{y_k\}$. So $T$ is linear, and the kernel of a linear transformation is a subspace ([[§24 Null Spaces, Column Spaces, and Linear Transformations#^thm-24-5|Theorem §24.5]]).

^pf-30-3

*Uses:* [[§24 Null Spaces, Column Spaces, and Linear Transformations#^thm-24-5|§24.5]] (the kernel is a subspace)

> [!theorem] Theorem §30.4: Existence and Uniqueness
> If $a_n \ne 0$ and $\{z_k\}$ is given, the equation
>
> $$
> y_{k+n} + a_1 y_{k+n-1} + \cdots + a_{n-1} y_{k+1} + a_n y_k = z_k \quad \text{for all } k \qquad (7)
> $$
>
> has a unique solution whenever $y_0, \ldots, y_{n-1}$ are specified.
>
> *Lay: Theorem 16 (4.8)*

^thm-30-4

> [!proof]+ Proof
> Suppose $y_0, \ldots, y_{n-1}$ are specified. Use (7) with $k = 0$ to *define*
>
> $$
> y_n = z_0 - [a_1 y_{n-1} + \cdots + a_{n-1} y_1 + a_n y_0] .
> $$
>
> Now that $y_1, \ldots, y_n$ are specified, use (7) with $k = 1$ to define $y_{n+1}$. In general, the recurrence relation
>
> $$
> y_{n+k} = z_k - [a_1 y_{k+n-1} + \cdots + a_n y_k] \qquad (8)
> $$
>
> defines $y_{n+k}$ for $k \ge 0$, one after the other. To define $y_k$ for $k < 0$, solve (7) for $y_k$, which is possible because $a_n \ne 0$:
>
> $$
> y_k = \frac{1}{a_n} z_k - \frac{1}{a_n}\big[ y_{k+n} + a_1 y_{k+n-1} + \cdots + a_{n-1} y_{k+1} \big] , \qquad (9)
> $$
>
> and use it for $k = -1, -2, \ldots$ in turn. This produces a signal that satisfies (7). Conversely, any signal that satisfies (7) for all $k$ satisfies (8) and (9), so its terms are forced, one at a time, by $y_0, \ldots, y_{n-1}$: the solution of (7) is unique.

^pf-30-4

*Uses:* [[§30 Applications to Difference Equations#^def-30-3|Def. §30.3]]

> [!theorem] Theorem §30.5: The Solution Space Has Dimension n
> The set $H$ of all solutions of the $n$th-order homogeneous linear difference equation
>
> $$
> y_{k+n} + a_1 y_{k+n-1} + \cdots + a_{n-1} y_{k+1} + a_n y_k = 0 \quad \text{for all } k \qquad (10)
> $$
>
> is an $n$-dimensional vector space.
>
> *Lay: Theorem 17 (4.8)*

^thm-30-5

> [!proof]+ Proof
> $H$ is a subspace of $\mathbb{S}$, the kernel of a linear transformation (Proposition §30.3). For $\{y_k\}$ in $H$, let $F\{y_k\}$ be the vector of its first $n$ values,
>
> $$
> F\{y_k\} = (y_0, y_1, \ldots, y_{n-1}) \in \mathbb{R}^n .
> $$
>
> $F : H \to \mathbb{R}^n$ is linear (the values at $0, \ldots, n-1$ of a sum or multiple of signals are the sums or multiples of the values). Given any vector $(y_0, y_1, \ldots, y_{n-1})$ in $\mathbb{R}^n$, Theorem §30.4 (with $z_k = 0$; here $a_n \ne 0$ is part of the definition of order $n$) says there is a unique signal $\{y_k\}$ in $H$ with $F\{y_k\} = (y_0, y_1, \ldots, y_{n-1})$. Existence says $F$ is onto $\mathbb{R}^n$, uniqueness that $F$ is one-to-one. So $F$ is an isomorphism, and $\dim H = \dim \mathbb{R}^n = n$ by [[§27 The Dimension of a Vector Space#^prop-27-7|Proposition §27.7]].

^pf-30-5

*Uses:* [[§30 Applications to Difference Equations#^prop-30-3|§30.3]], [[§30 Applications to Difference Equations#^thm-30-4|§30.4]], [[§27 The Dimension of a Vector Space#^prop-27-7|§27.7]]

> [!remark]- Connections
> - Rigorous treatment: finite-dimensional spaces are isomorphic exactly when they have the same dimension, [[§10 Invertibility and Isomorphisms#^ladr-3-70|LADR 3.70]]; here the isomorphism is "evaluate at $0, \ldots, n-1$". The same argument (an existence and uniqueness theorem for initial values) shows that the solutions of an $n$th-order linear homogeneous differential equation form an $n$-dimensional space.
> - ODE version: for $y'' + p(t)y' + q(t)y = 0$ the isomorphism is $y \mapsto (y(t_0), y'(t_0))$ and the dimension is $2$, [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^rem-14-2|331 §14, Remark: The Solution Space Is a Two-Dimensional Vector Space]]; for a system $\mathbf{x}' = P(t)\mathbf{x}$ of $n$ equations it is $\mathbf{x} \mapsto \mathbf{x}(t_0)$, and a fundamental set is a basis of the $n$-dimensional solution space, [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-2|331 Thm. §30.2]], [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-4|331 Thm. §30.4]].

> [!theorem] Proposition §30.6: The Casorati Test for Solutions
> Let $n$ signals be solutions of the same $n$th-order homogeneous equation (10), and let $C(k)$ be their Casorati matrix. Then either $C(k)$ is invertible for all $k$ and the signals are linearly independent, or $C(k)$ is invertible for no $k$ and the signals are linearly dependent.
>
> *Lay: 4.8 (text; proof in the Study Guide)*

^prop-30-6

> [!proof]+ Proof
> Lay states this and refers to the Study Guide; here is a short argument from Theorem §30.4. If $C(k)$ is invertible for some $k$, the signals are independent by Proposition §30.1. Suppose instead that $C(k_0)$ is singular for some $k_0$. Then there is $\mathbf{c} = (c_1, \ldots, c_n) \ne \mathbf{0}$ with $C(k_0)\mathbf{c} = \mathbf{0}$. The combination $\{x_k\} = c_1\{u^{(1)}_k\} + \cdots + c_n\{u^{(n)}_k\}$ of the given solutions is a solution of (10) (Proposition §30.3), and $C(k_0)\mathbf{c} = \mathbf{0}$ says $x_{k_0} = x_{k_0+1} = \cdots = x_{k_0+n-1} = 0$. The zero signal is also a solution with these $n$ consecutive values. Theorem §30.4, applied after shifting the index so that $k_0$ becomes $0$, says such a solution is unique, so $\{x_k\}$ is the zero signal. Thus a nontrivial combination of the signals vanishes: they are linearly dependent, and then (by the first case) no $C(k)$ can be invertible.

^pf-30-6

*Uses:* [[§30 Applications to Difference Equations#^prop-30-1|§30.1]], [[§30 Applications to Difference Equations#^prop-30-3|§30.3]], [[§30 Applications to Difference Equations#^thm-30-4|§30.4]]

> [!definition] Definition §30.5: Fundamental Set of Solutions
> A basis for the subspace of all solutions of the homogeneous equation (10) is a **fundamental set of solutions** of (10). Exhibiting one is the standard way to describe the "general solution". By Theorem §30.5 and the [[§27 The Dimension of a Vector Space#^thm-27-5|Basis Theorem]], any $n$ linearly independent solutions of (10) automatically span the $n$-dimensional solution space, so they form a fundamental set.
>
> *Lay: 4.8 (text)*

^def-30-5

> [!remark] Remark: Method — Solving a Homogeneous Linear Difference Equation
> 1. Normalize to $y_{k+n} + a_1 y_{k+n-1} + \cdots + a_n y_k = 0$ and write the auxiliary equation $r^n + a_1 r^{n-1} + \cdots + a_n = 0$.
> 2. Find its roots. Each root $r$ gives a solution $\{r^k\}$ (Proposition §30.2).
> 3. If there are $n$ distinct roots, the $n$ signals $r_i^k$ are linearly independent (check with a Casorati matrix at a convenient $k$, Proposition §30.1), hence a fundamental set (Definition §30.5). The general solution is $y_k = c_1 r_1^k + \cdots + c_n r_n^k$.
> 4. Given initial values $y_0, \ldots, y_{n-1}$, solve the linear system for $c_1, \ldots, c_n$; its coefficient matrix is the Casorati matrix $C(0)$, so the solution is unique (Theorem §30.4).
> 5. Nonhomogeneous equation: add one particular solution ([[§30 Applications to Difference Equations#^thm-30-7|Theorem §30.7]]).

^rem-30-2

> [!example] Example §30.3: A Fundamental Set from the Auxiliary Equation
> Find a basis for the set of all solutions of
>
> $$
> y_{k+3} - 2y_{k+2} - 5y_{k+1} + 6y_k = 0 \quad \text{for all } k . \qquad (4)
> $$
>
> **Solutions of the form $r^k$.** Substitute $r^k$ and factor:
>
> $$
> r^{k+3} - 2r^{k+2} - 5r^{k+1} + 6r^k = r^k(r^3 - 2r^2 - 5r + 6) = r^k(r - 1)(r + 2)(r - 3)
> $$
>
> (check: $(r - 1)(r + 2) = r^2 + r - 2$, and $(r^2 + r - 2)(r - 3) = r^3 - 2r^2 - 5r + 6$). By Proposition §30.2, $1^k$, $(-2)^k$ and $3^k$ are solutions. For instance
>
> $$
> 3^{k+3} - 2 \cdot 3^{k+2} - 5 \cdot 3^{k+1} + 6 \cdot 3^k = 3^k(27 - 18 - 15 + 6) = 0 \quad \text{for all } k .
> $$
>
> **A basis.** By Example §30.1 the three solutions are linearly independent. In general it can be hard to verify directly that a set of signals *spans* the solution space, but here there is no need: by Theorem §30.5 the solution space is exactly three-dimensional, and by the Basis Theorem three linearly independent vectors in a three-dimensional space form a basis. So $1^k$, $(-2)^k$, $3^k$ is a fundamental set, and every solution is $y_k = c_1 + c_2(-2)^k + c_3 3^k$.
>
> *Lay: Examples 4.8.4 and 4.8.5*

^ex-30-3

> [!example] Example §30.4: The Fibonacci Numbers
> The Fibonacci numbers satisfy $F_{k+2} = F_{k+1} + F_k$ with $F_0 = 0$, $F_1 = 1$: $0, 1, 1, 2, 3, 5, 8, 13, 21, \ldots$. Find a formula for $F_k$, and the limit of $F_{k+1}/F_k$.
>
> **The equation.** $F_{k+2} - F_{k+1} - F_k = 0$ is homogeneous of order $2$ ($a_1 = a_2 = -1$). Its auxiliary equation is
>
> $$
> r^2 - r - 1 = 0, \qquad r = \frac{1 \pm \sqrt5}{2}: \qquad \varphi = \frac{1 + \sqrt5}{2} \approx 1.618, \qquad \psi = \frac{1 - \sqrt5}{2} \approx -0.618 .
> $$
>
> **A fundamental set.** $\{\varphi^k\}$ and $\{\psi^k\}$ are solutions (Proposition §30.2). Their Casorati matrix at $k = 0$ is $\begin{bmatrix} 1 & 1 \\ \varphi & \psi \end{bmatrix}$, with determinant $\psi - \varphi = -\sqrt5 \ne 0$, so they are independent, and by Theorem §30.5 ($n = 2$) and the Basis Theorem they form a basis of the solution space. So $F_k = c_1\varphi^k + c_2\psi^k$ for some $c_1, c_2$.
>
> **Initial values.** $k = 0$: $c_1 + c_2 = 0$. $k = 1$: $c_1\varphi + c_2\psi = 1$. Substituting $c_2 = -c_1$ gives $c_1(\varphi - \psi) = c_1\sqrt5 = 1$. Hence
>
> $$
> F_k = \frac{\varphi^k - \psi^k}{\sqrt5} .
> $$
>
> Check: $F_0 = 0$, $F_1 = \frac{\sqrt5}{\sqrt5} = 1$, and $F_2 = \frac{\varphi^2 - \psi^2}{\sqrt5} = \frac{1}{\sqrt5}\Big(\frac{6 + 2\sqrt5}{4} - \frac{6 - 2\sqrt5}{4}\Big) = \frac{\sqrt5}{\sqrt5} = 1$.
>
> **Growth.** $\varphi > 1$ and $|\psi| < 1$, so $\psi^k \to 0$ and $F_k \approx \varphi^k/\sqrt5$ for large $k$ (for instance $\varphi^{10}/\sqrt5 \approx 55.004$, while $F_{10} = 55$). More precisely, with $q = \psi/\varphi$, $|q| < 1$,
>
> $$
> \frac{F_{k+1}}{F_k} = \frac{\varphi^{k+1} - \psi^{k+1}}{\varphi^k - \psi^k} = \varphi \cdot \frac{1 - q^{k+1}}{1 - q^k} \longrightarrow \varphi \qquad (k \to \infty) ,
> $$
>
> the golden ratio: the ratios $\frac21, \frac32, \frac53, \frac85, \frac{13}{8}, \frac{21}{13}, \ldots$ approach $\varphi$.
>
> **The lecture's route.** L18 writes the recurrence as a first-order system (Proposition §30.8): $\mathbf{v}_k = \begin{bmatrix} F_k \\ F_{k+1} \end{bmatrix}$ satisfies $\mathbf{v}_{k+1} = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}\mathbf{v}_k$, so $\mathbf{v}_k = A^k\mathbf{v}_0$. The eigenvalues of $A$ are the roots $\varphi$, $\psi$ of $\det(A - \lambda I) = \lambda^2 - \lambda - 1$, with eigenvectors $\mathbf{u} = (1, \varphi)$ and $\mathbf{v} = (1, \psi)$. Since $\mathbf{u} - \mathbf{v} = (0, \sqrt5) = \sqrt5\,\mathbf{v}_0$, one gets $\mathbf{v}_k = A^k\mathbf{v}_0 = \frac{1}{\sqrt5}(\varphi^k\mathbf{u} - \psi^k\mathbf{v})$, whose first entry is the same formula. (Eigenvectors: Chapter 5, [[§32 Eigenvectors and Eigenvalues#^ex-32-4|Example §32.4]] and [[§37 Discrete Dynamical Systems#^thm-37-1|Theorem §37.1]].)
>
> *The lecture first lists $F_0 = F_1 = 1$ and then uses $\mathbf{v}_0 = (F_0, F_1) = (0, 1)$; the closed formula $F_n = (\varphi^n - \psi^n)/\sqrt5$ it derives is the one for $F_0 = 0$, $F_1 = 1$, used here.*
>
> *Source: 235 lecture L18*

^ex-30-4

> [!remark]- Connections
> - The same formula by [[Strong Induction Principle|strong induction]]: [[§5 The Induction Principle#^prop-5-8|250 Prop. §5.8]] (Binet formula, with Fibonacci numbers [[§5 The Induction Principle#^def-5-5|250 Def. §5.5]] starting at $u_1 = u_2 = 1$). By diagonalizing an operator: [[§17 Diagonalizable Operators#^ladr-5-59|LADR 5.59]]. The Fibonacci sequence as a recursively defined sequence: [[§69 Sequences#^rem-69-1|Calc Remark: Ways to Describe a Sequence]]; the limit $q^k \to 0$ for $|q| < 1$: [[§69 Sequences#^thm-69-8|Calc Thm. §69.8]].

## Nonhomogeneous Equations

> [!theorem] Theorem §30.7: General Solution of a Nonhomogeneous Equation
> The general solution of the nonhomogeneous difference equation
>
> $$
> y_{k+n} + a_1 y_{k+n-1} + \cdots + a_{n-1} y_{k+1} + a_n y_k = z_k \quad \text{for all } k \qquad (11)
> $$
>
> is one particular solution of (11) plus an arbitrary linear combination of a fundamental set of solutions of the corresponding homogeneous equation (10).
>
> This is the analog of the result of Section 1.5 that the solution set of $A\mathbf{x} = \mathbf{b}$ is a translate of that of $A\mathbf{x} = \mathbf{0}$ ([[§5 Solution Sets of Linear Systems#^thm-5-3|Theorem §5.3]]), with the same explanation: both maps $\mathbf{x} \mapsto A\mathbf{x}$ and $\{y_k\} \mapsto \{z_k\}$ are linear.
>
> *Lay: 4.8 (text); Exercises 35 and 36*

^thm-30-7

> [!proof]+ Proof
> Let $T$ be the linear transformation of Proposition §30.3, so (11) reads $T\{y_k\} = \{z_k\}$, and let $\{p_k\}$ be one solution: $T\{p_k\} = \{z_k\}$. If $\{u_k\}$ solves the homogeneous equation, $T\{u_k\} = 0$, then $T\{p_k + u_k\} = \{z_k\} + 0 = \{z_k\}$, so $\{p_k + u_k\}$ solves (11). Conversely, if $\{y_k\}$ solves (11), then $T\{y_k - p_k\} = \{z_k\} - \{z_k\} = 0$, so $\{u_k\} = \{y_k - p_k\}$ is in the kernel of $T$ and $\{y_k\} = \{p_k\} + \{u_k\}$. Writing $\{u_k\}$ in a fundamental set gives the statement.

^pf-30-7

*Uses:* [[§30 Applications to Difference Equations#^prop-30-3|§30.3]], [[§30 Applications to Difference Equations#^def-30-5|Def. §30.5]]

> [!remark]- Connections
> - See also: the first-order case $y_{k+1} = \rho y_k + b_k$, solved explicitly for any $y_0$: [[§12★ First-Order Difference Equations#^prop-12-2|331 Prop. §12.2]]; for constant $b$ and $\rho \ne 1$ the solution is the equilibrium $b/(1 - \rho)$ plus a multiple of $\rho^k$, particular plus homogeneous. The same structure for linear differential equations: [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-2|331 Thm. §17.2]].

> [!example] Example §30.5: A Nonhomogeneous Equation
> Verify that $y_k = k^2$ satisfies
>
> $$
> y_{k+2} - 4y_{k+1} + 3y_k = -4k \quad \text{for all } k , \qquad (12)
> $$
>
> and describe all solutions.
>
> **A particular solution.** Substitute $k^2$ for $y_k$:
>
> $$
> (k + 2)^2 - 4(k + 1)^2 + 3k^2 = (k^2 + 4k + 4) - 4(k^2 + 2k + 1) + 3k^2 = -4k .
> $$
>
> **The homogeneous equation** $y_{k+2} - 4y_{k+1} + 3y_k = 0$ has auxiliary equation $r^2 - 4r + 3 = (r - 1)(r - 3) = 0$, with roots $1$ and $3$. So $1^k$ and $3^k$ are solutions; they are not multiples of each other, hence linearly independent, and by Theorem §30.5 the solution space is two-dimensional, so they form a basis.
>
> **General solution.** By Theorem §30.7,
>
> $$
> y_k = k^2 + c_1 1^k + c_2 3^k = k^2 + c_1 + c_2 3^k .
> $$
>
> Geometrically, in $\mathbb{S}$ the solutions of (12) form the plane $k^2 + \operatorname{Span}\{1^k, 3^k\}$, the translate by the signal $k^2$ of the plane of homogeneous solutions through the origin.
>
> *Lay: Example 4.8.6*

^ex-30-5

## Reduction to Systems of First-Order Equations

A modern way to study an $n$th-order homogeneous equation is to replace it by an equivalent first-order system $\mathbf{x}_{k+1} = A\mathbf{x}_k$, with $\mathbf{x}_k \in \mathbb{R}^n$ and $A$ an $n \times n$ matrix. Such vector difference equations appear in Section 1.10 ([[§10 Linear Models in Business, Science, and Engineering#^def-10-2|Definition §10.2]]), in Markov chains ([[§31 Applications to Markov Chains#^def-31-2|Definition §31.2]]) and in Section 5.6 ([[§37 Discrete Dynamical Systems|§37]]).

> [!theorem] Proposition §30.8: Reduction to a First-Order System
> The equation $y_{k+n} + a_1 y_{k+n-1} + \cdots + a_{n-1} y_{k+1} + a_n y_k = 0$ for all $k$ can be rewritten as $\mathbf{x}_{k+1} = A\mathbf{x}_k$ for all $k$, where
>
> $$
> \mathbf{x}_k = \begin{bmatrix} y_k \\ y_{k+1} \\ \vdots \\ y_{k+n-1} \end{bmatrix}, \qquad
> A = \begin{bmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ \vdots & & & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & 1 \\ -a_n & -a_{n-1} & -a_{n-2} & \cdots & -a_1 \end{bmatrix} .
> $$
>
> For example, $y_{k+3} - 2y_{k+2} - 5y_{k+1} + 6y_k = 0$ becomes $\mathbf{x}_{k+1} = A\mathbf{x}_k$ with
>
> $$
> \mathbf{x}_k = \begin{bmatrix} y_k \\ y_{k+1} \\ y_{k+2} \end{bmatrix}, \qquad A = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -6 & 5 & 2 \end{bmatrix} .
> $$
>
> *Lay: 4.8 (text); Example 4.8.7*

^prop-30-8

> [!proof]+ Proof
> The entries of $\mathbf{x}_{k+1}$ are $y_{k+1}, \ldots, y_{k+n-1}, y_{k+n}$. The first $n - 1$ of them are entries $2, \ldots, n$ of $\mathbf{x}_k$, which is what rows $1, \ldots, n - 1$ of $A$ (a single $1$ just right of the diagonal) pick out. The difference equation says
>
> $$
> y_{k+n} = -a_n y_k - a_{n-1} y_{k+1} - \cdots - a_1 y_{k+n-1} ,
> $$
>
> which is the last row of $A$ times $\mathbf{x}_k$. In the example, $y_{k+3} = -6y_k + 5y_{k+1} + 2y_{k+2}$, so
>
> $$
> \mathbf{x}_{k+1} = \begin{bmatrix} y_{k+1} \\ y_{k+2} \\ y_{k+3} \end{bmatrix} = \begin{bmatrix} 0 + y_{k+1} + 0 \\ 0 + 0 + y_{k+2} \\ -6y_k + 5y_{k+1} + 2y_{k+2} \end{bmatrix} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -6 & 5 & 2 \end{bmatrix} \begin{bmatrix} y_k \\ y_{k+1} \\ y_{k+2} \end{bmatrix} .
> $$
>
> Conversely, if $\mathbf{x}_{k+1} = A\mathbf{x}_k$ for vectors of this shape, the last row gives back the difference equation.

^pf-30-8

*Uses:* [[§30 Applications to Difference Equations#^def-30-3|Def. §30.3]]
