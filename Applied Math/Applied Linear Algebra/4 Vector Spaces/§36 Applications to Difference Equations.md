---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 4
section: 36
lay: "4.8"
aliases: ["Lay 4.8"]
tags: [applied-linear-algebra, math235]
---
← [[§35 Change of Basis]] · ↑ [[· 4 Vector Spaces]] · [[§37 Solution Sets of Linear Difference Equations]] →

*Lay, Section 4.8 · MATH 235 lecture L18.*

Discrete data (sampled music, yearly populations, monthly loan balances) are sequences, and the equations that govern them are difference equations, the discrete counterpart of differential equations. This section applies the vector space ideas of Chapter 4 to the space $\mathbb{S}$ of signals. The solutions of a homogeneous linear difference equation of order $n$ form an $n$-dimensional subspace of $\mathbb{S}$, so by the Basis Theorem any $n$ linearly independent solutions (found from the roots of the auxiliary equation and checked with the Casorati matrix) give all solutions. A nonhomogeneous equation has the general solution "particular solution plus homogeneous solutions", exactly as for $A\mathbf{x} = \mathbf{b}$. The Fibonacci numbers of lecture L18 are the standard example. Finally, every such equation can be rewritten as a first-order system $\mathbf{x}_{k+1} = A\mathbf{x}_k$, the form studied with eigenvectors in Chapter 5.

## Discrete-Time Signals

> [!definition] Definition §36.1: Signals; the Space 𝕊
> A **signal** is a function defined only on the integers, visualized as a doubly infinite sequence of numbers $\{y_k\} = (\ldots, y_{-2}, y_{-1}, y_0, y_1, y_2, \ldots)$; examples are $\{(.7)^k\}$, $\{1^k\}$ and $\{(-1)^k\}$. The signals form the vector space $\mathbb{S}$ of Section 4.1 ([[§29 Vector Spaces and Subspaces#^ex-29-1|Example §29.1]](c)), with termwise addition and scalar multiplication. When a process begins at a specific time, a signal may be written $(y_0, y_1, y_2, \ldots)$, the terms with $k < 0$ being zero or omitted.
>
> *Lay: 4.8 (text); 4.1, Example 3*

^def-36-1

Signals arise wherever a process is measured, or *sampled*, at discrete time intervals. A compact disc stores music sampled $44{,}100$ times per second: the amplitude $y_k$ at each measurement, and the sequence $\{y_k\}$ contains enough information to reproduce all frequencies up to about $20{,}000$ cycles per second, beyond human hearing (Lay, Example 4.8.1).

## Linear Independence in the Space 𝕊 of Signals

Three signals $\{u_k\}$, $\{v_k\}$, $\{w_k\}$ are linearly independent precisely when

$$
c_1 u_k + c_2 v_k + c_3 w_k = 0 \quad \text{for all } k \qquad (1)
$$

implies $c_1 = c_2 = c_3 = 0$. "For all $k$" means all integers $k$ (or all $k \ge 0$ for signals that start at $k = 0$).

> [!definition] Definition §36.2: Casorati Matrix; Casoratian
> The **Casorati matrix** of the signals $\{u_k\}$, $\{v_k\}$, $\{w_k\}$ is
>
> $$
> C(k) = \begin{bmatrix} u_k & v_k & w_k \\ u_{k+1} & v_{k+1} & w_{k+1} \\ u_{k+2} & v_{k+2} & w_{k+2} \end{bmatrix},
> $$
>
> and its determinant is the **Casoratian** of the signals. For $n$ signals, $C(k)$ is the $n \times n$ matrix whose rows list the values at $k, k+1, \ldots, k+n-1$.
>
> *Lay: 4.8 (text)*

^def-36-2

> [!theorem] Proposition §36.1: The Casorati Test
> If the Casorati matrix $C(k)$ of $n$ signals is invertible for at least one value of $k$, then the signals are linearly independent.
>
> *Lay: 4.8 (text)*

^prop-36-1

> [!proof]+ Proof
> Take $n = 3$ (the general case is the same). Suppose $c_1, c_2, c_3$ satisfy (1). Then (1) holds for any three consecutive values of $k$, say $k$, $k + 1$ and $k + 2$:
>
> $$
> c_1 u_{k+1} + c_2 v_{k+1} + c_3 w_{k+1} = 0, \qquad c_1 u_{k+2} + c_2 v_{k+2} + c_3 w_{k+2} = 0 \qquad \text{for all } k .
> $$
>
> Together with (1) this says $C(k)\,\mathbf{c} = \mathbf{0}$ for all $k$, where $\mathbf{c} = (c_1, c_2, c_3)$. If $C(k_0)$ is invertible for one $k_0$, then $\mathbf{c} = C(k_0)^{-1}\mathbf{0} = \mathbf{0}$. So $c_1 = c_2 = c_3 = 0$ and the signals are independent.

^pf-36-1

*Uses:* [[§14 The Inverse of a Matrix#^thm-14-3|§14.3]] (solving with an inverse)

If no Casorati matrix is invertible, the signals may or may not be linearly independent (Lay, Exercise 33: $k^2$ and $2k|k|$). For solutions of one homogeneous difference equation, however, the test is decisive: [[§37 Solution Sets of Linear Difference Equations#^prop-37-4|Proposition §37.4]].

> [!example] Example §36.1: A Casorati Matrix
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
> Three pivots, so $C(0)$ is invertible, and $1^k$, $(-2)^k$, $3^k$ are linearly independent by [[§36 Applications to Difference Equations#^prop-36-1|Proposition §36.1]].
>
> *Lay: Example 4.8.2*

^ex-36-1

## Linear Difference Equations

> [!definition] Definition §36.3: Linear Difference Equation
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

^def-36-3

> [!example] Example §36.2: A Low-Pass Filter
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

^ex-36-2

![[m235-30-1.svg]]
*[[§36 Applications to Difference Equations#^ex-36-2|Example §36.2]]. Top: the input $y_k = \cos(\pi k/4)$ (blue stems, sampled from the blue curve) and the filter's output $z_k = y_{k+1}$ (red circles), the same wave shifted one step to the left. Bottom: the input $w_k = \cos(3\pi k/4)$, sampled from a faster wave; the output is $0$ for every $k$ (red circles on the axis).*

Solutions of a homogeneous equation are often of the form $y_k = r^k$.

> [!definition] Definition §36.4: Auxiliary Equation
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

^def-36-4

> [!theorem] Proposition §36.2: Exponential Solutions
> A nonzero signal $\{r^k\}$ ($r \ne 0$) satisfies the homogeneous difference equation of [[§36 Applications to Difference Equations#^def-36-4|Definition §36.4]] if and only if $r$ is a root of its auxiliary equation.
>
> *Lay: 4.8 (text and Example 4.8.4)*

^prop-36-2

> [!proof]+ Proof
> Substitute $y_k = r^k$ and factor out $r^k$:
>
> $$
> r^{k+n} + a_1 r^{k+n-1} + \cdots + a_n r^k = r^k\,(r^n + a_1 r^{n-1} + \cdots + a_n) .
> $$
>
> Since $r^k \ne 0$, this is $0$ for all $k$ exactly when $r^n + a_1 r^{n-1} + \cdots + a_n = 0$.

^pf-36-2

*Uses:* [[§36 Applications to Difference Equations#^def-36-4|Def. §36.4]]

> [!remark] Remark: Repeated and Complex Roots
> Lay does not treat repeated roots of the auxiliary equation (then $\{r^k\}$ gives fewer than $n$ solutions; a root $r$ of multiplicity two also gives $\{k r^k\}$, as in Exercise 5). Lecture L18 poses the recurrence $A_{n+1} = 2A_n - A_{n-1}$ as an exercise (the left side is written $A_n$ there), asking for a formula of the Fibonacci shape $(\mu_1^n - \mu_2^n)/c$; its auxiliary equation $r^2 - 2r + 1 = (r - 1)^2$ has the double root $1$, so that shape does not apply, and the solutions are $\{1\}$ and $\{k\}$: $A_k = c_1 + c_2 k$, the arithmetic progressions (Casorati matrix at $k = 0$: $\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$, invertible). When the auxiliary equation has a complex root, the difference equation has real solutions of the form $s^k\cos k\omega$ and $s^k\sin k\omega$ for constants $s$ and $\omega$: the signal $w_k = \cos(3\pi k/4)$ of [[§36 Applications to Difference Equations#^ex-36-2|Example §36.2]] is one ($s = 1$, $\omega = 3\pi/4$; the auxiliary equation $.35r^2 + .5r + .35 = 0$ has the roots $e^{\pm 3\pi i/4}$). Complex numbers and $e^{i\theta}$: [[§64 Complex Numbers#^rem-64-1|Remark: Euler's Formula]]. For differential equations the same substitution, $y = e^{rt}$ in place of $y_k = r^k$, leads to the characteristic equation: [[§17 Homogeneous Differential Equations with Constant Coefficients#^thm-17-1|331 Thm. §17.1]].

^rem-36-1

*Continued in [[§37 Solution Sets of Linear Difference Equations]]: the solution space and fundamental sets of solutions, nonhomogeneous equations, and reduction to first-order systems.*
