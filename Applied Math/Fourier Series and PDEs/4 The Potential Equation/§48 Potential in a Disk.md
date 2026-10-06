---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 4
section: 48
powers: "4.5"
aliases: ["Powers 4.5"]
tags: [fourier-series-and-pdes, math341]
---
← [[§47 Potential in Unbounded Regions]] · ↑ [[· 4 The Potential Equation]] · [[§49 The Poisson Integral Formula and the Mean Value Property]] →

*Powers, Section 4.5 · MAT 341 lectures 11.21, 11.26, 12.3 · HW 13 · Practice Final.*

In a disk the natural coordinates are polar, and separation of variables in $r$ and $\theta$ needs two conditions that are not boundary conditions at all: periodicity in $\theta$, because $\theta$ and $\theta + 2\pi$ are the same direction, and boundedness at the center, where the polar Laplacian has singular coefficients. The angular factor then runs through $1, \cos n\theta, \sin n\theta$ and the radial factor through $r^n$, so the solution of Dirichlet's problem is the Fourier series of the boundary values with its $n$th terms damped by $(r/c)^n$. Summing that series gives the Poisson integral formula. Setting $r = 0$ gives the mean value property, from which follow the maximum principle and the uniqueness of the solution of Dirichlet's problem in any region. Physically: the electrostatic potential inside a long cylinder with prescribed voltage on its surface, or the steady temperature in a circular plate.

## Dirichlet's Problem in a Disk

To solve the potential equation in the disk $x^2 + y^2 < c^2$, use polar coordinates, in which the disk is $0 \le r < c$ and the potential equation reads ([[§44 Potential Equation#^thm-44-3|Theorem §44.3]])

$$
\frac1r\frac{\partial}{\partial r}\Big(r\frac{\partial v}{\partial r}\Big) + \frac{1}{r^2}\frac{\partial^2v}{\partial\theta^2} = 0 .
$$

Two features of this coordinate system matter. Some coefficients of the Laplacian are negative powers of $r$, so a boundedness condition must be enforced at $r = 0$ ([[§6★ Singular Boundary Value Problems#^def-6-2|Definition §6.2]]). And $\theta$ and $\theta + 2\pi$ refer to the same angle, so $v(r, \theta)$ must be periodic with period $2\pi$ in $\theta$. **Dirichlet's problem on a disk** is therefore

$$
\begin{aligned}
&\frac1r\frac{\partial}{\partial r}\Big(r\frac{\partial v}{\partial r}\Big) + \frac{1}{r^2}\frac{\partial^2v}{\partial\theta^2} = 0, && 0 \le r < c, && (1) \\
&v(c, \theta) = f(\theta), && && (2) \\
&v(r, \theta + 2\pi) = v(r, \theta), && 0 < r < c, && (3) \\
&v(r, \theta) \ \text{bounded as } r \to 0^+ . && && (4)
\end{aligned}
$$

Separating variables, $v = R(r)Q(\theta)$, the equation becomes $\frac1r(rR')'Q + \frac{1}{r^2}RQ'' = 0$, and dividing by $RQ/r^2$,

$$
\frac{r\big(rR'(r)\big)'}{R(r)} + \frac{Q''(\theta)}{Q(\theta)} = 0 .
$$

Both terms must be constant. If $Q''/Q$ were a positive constant $\mu^2$, then $Q = Ae^{\mu\theta} + Be^{-\mu\theta}$ would be exponential, not periodic: $Q(\theta + 2\pi) = Q(\theta)$ for all $\theta$ means $A(e^{2\pi\mu} - 1)e^{\mu\theta} + B(e^{-2\pi\mu} - 1)e^{-\mu\theta} = 0$, which forces $A = B = 0$. So $Q''/Q = -\lambda^2$, and we obtain a **singular eigenvalue problem** (the periodicity condition replaces boundary conditions; compare [[§6★ Singular Boundary Value Problems#^def-6-1|Definition §6.1]], and for the boundedness condition (8) [[§6★ Singular Boundary Value Problems#^def-6-2|Definition §6.2]]):

$$
Q'' + \lambda^2Q = 0, \quad (5) \qquad Q(\theta + 2\pi) = Q(\theta), \quad (6)
$$

with the accompanying equation for $R(r)$

$$
r\big(rR'\big)' - \lambda^2R = 0, \quad (7) \qquad R(r) \ \text{bounded as } r \to 0^+ . \quad (8)
$$

> [!theorem] Proposition §48.1: The Periodic Eigenvalue Problem
> The solutions of the singular eigenvalue problem (5)–(6) are
>
> $$
> \lambda_0 = 0, \quad Q_0(\theta) = 1; \qquad \lambda_n = n, \quad Q_n(\theta) = A\cos(n\theta) + B\sin(n\theta), \quad n = 1, 2, 3, \ldots
> $$
>
> The novelty is that each eigenvalue $n \ge 1$ has **two** independent eigenfunctions, $\cos(n\theta)$ and $\sin(n\theta)$.
>
> *Powers: 4.5 (text)*

^prop-48-1

> [!proof]+ Proof
> **$\lambda > 0$.** The general solution of (5) is $Q(\theta) = A\cos(\lambda\theta) + B\sin(\lambda\theta)$. This function is periodic for every $\lambda$, but its period is $2\pi$ only if $\lambda$ is an integer. (Powers asserts this; here is why.) Since $Q$ solves a second-order equation, $Q(\theta + 2\pi) = Q(\theta)$ for all $\theta$ holds if and only if $Q(2\pi) = Q(0)$ and $Q'(2\pi) = Q'(0)$ (both sides of (6) solve (5), and two solutions with the same value and derivative at one point coincide). These two conditions read
>
> $$
> \big(\cos 2\pi\lambda - 1\big)A + \sin(2\pi\lambda)\,B = 0, \qquad -\sin(2\pi\lambda)\,A + \big(\cos 2\pi\lambda - 1\big)B = 0 ,
> $$
>
> a homogeneous system with determinant $(\cos 2\pi\lambda - 1)^2 + \sin^2 2\pi\lambda = 2 - 2\cos 2\pi\lambda$. A nonzero solution $(A, B)$ exists exactly when this is $0$, that is, when $\lambda$ is an integer $n$; and then every $(A, B)$ works.
>
> **$\lambda = 0$.** Then $Q = A + B\theta$, which is periodic if and only if $B = 0$: any constant is a periodic solution.

^pf-48-1

*Uses:* [[§1★ Homogeneous Linear Equations#^ex-1-1|Ex. §1.1]] (solutions of $Q'' + \lambda^2Q = 0$), [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-1|331 Thm. §18.1]] (uniqueness for initial value problems)

> [!theorem] Theorem §48.2: Solution of Dirichlet's Problem in a Disk
> The solution of (1)–(4) is
>
> $$
> v(r, \theta) = a_0 + \sum_{n=1}^{\infty}a_nr^n\cos(n\theta) + \sum_{n=1}^{\infty}b_nr^n\sin(n\theta) , \qquad (10)
> $$
>
> with
>
> $$
> a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi}f(\theta)\,d\theta, \qquad a_n = \frac{1}{\pi c^n}\int_{-\pi}^{\pi}f(\theta)\cos(n\theta)\,d\theta, \qquad b_n = \frac{1}{\pi c^n}\int_{-\pi}^{\pi}f(\theta)\sin(n\theta)\,d\theta . \qquad (11)
> $$
>
> In other words, $v(r, \theta)$ is the Fourier series of $f$ with its $n$th harmonic multiplied by $(r/c)^n$.
>
> *Powers: 4.5, Equations (10)–(11)*

^thm-48-2

> [!proof]+ Proof
> **The radial factor.** By Proposition §48.1, $\lambda_n^2 = n^2$, and the equation (7) for $R$ becomes, when the indicated differentiations are carried out,
>
> $$
> r^2R'' + rR' - n^2R = 0, \qquad 0 < r < c .
> $$
>
> This is a Cauchy–Euler equation ([[§2★ Variable Coefficients and Higher-Order Equations#^thm-2-1|Theorem §2.1]]), whose solutions have the form $R(r) = r^\alpha$ with $\alpha$ constant. Substituting $R = r^\alpha$, $R' = \alpha r^{\alpha-1}$, $R'' = \alpha(\alpha - 1)r^{\alpha-2}$ leaves
>
> $$
> \big(\alpha(\alpha - 1) + \alpha - n^2\big)r^\alpha = 0, \qquad 0 < r < c .
> $$
>
> Because $r^\alpha \ne 0$, $\alpha^2 = n^2$, that is, $\alpha = \pm n$. For $n \ge 1$ the general solution is any combination of $r^n$ and $r^{-n}$; the latter is unbounded as $r \to 0^+$, so (8) discards it and $R_n(r) = r^n$. In the special case $n = 0$ the two solutions are the constant function $1$ and $\ln r$ ([[§44 Potential Equation#^ex-44-3|Example §44.3]](b)); the logarithm is discarded because of its behavior at $r = 0$.
>
> **Superposition.** The functions
>
> $$
> r^0\cdot 1 = 1, \qquad r^n\cos(n\theta), \qquad r^n\sin(n\theta) \qquad (9)
> $$
>
> are all solutions of the potential equation satisfying (3) and (4), so a general linear combination (10) of them is a solution too.
>
> **The boundary condition.** At the true boundary $r = c$, (2) reads
>
> $$
> v(c, \theta) = a_0 + \sum_{n=1}^{\infty}c^n\big(a_n\cos(n\theta) + b_n\sin(n\theta)\big) = f(\theta), \qquad -\pi < \theta \le \pi .
> $$
>
> This is a Fourier series problem for the $2\pi$-periodic function $f$ ([[§9 Periodic Functions and Fourier Series#^def-9-3|Definition §9.3]]): $a_0$ is the constant term of the Fourier series of $f$, and $c^na_n$, $c^nb_n$ are its $n$th cosine and sine coefficients. Dividing by $c^n$ gives (11).

^pf-48-2

*Uses:* [[§48 Potential in a Disk#^prop-48-1|§48.1]], [[§2★ Variable Coefficients and Higher-Order Equations#^thm-2-1|§2.1]] (Cauchy–Euler), [[§44 Potential Equation#^ex-44-3|Ex. §44.3]], [[§9 Periodic Functions and Fourier Series#^def-9-2|Def. §9.2]] (Fourier coefficients)

> [!remark]- Connections
> - Complex-variables version: [[§135★ Dirichlet Problem for a Disk#^thm-135-1|342 Thm. §135.1]] (the same Dirichlet problem solved by the Poisson integral, for piecewise continuous boundary values) and [[§135★ Dirichlet Problem for a Disk#^prop-135-4|342 Prop. §135.4]] (which expands that integral back into this series).

If $f$ is continuous, sectionally smooth and $f(-\pi^+) = f(\pi^-)$, the sum of the absolute values of its Fourier coefficients is finite ([[§13 Uniform Convergence#^rem-13-2|§13]], the remark after [[§13 Uniform Convergence#^thm-13-3|Theorem §13.3]]); since $|a_nr^n| \le |a_nc^n|$ and $|b_nr^n| \le |b_nc^n|$, the M-test then shows that (10) converges uniformly on the closed disk $r \le c$, so $v$ is continuous up to the boundary and takes the values $f$ there. Inside the disk no smoothness of $f$ is needed: since $|c^na_n|, |c^nb_n| \le \frac1\pi\int_{-\pi}^{\pi}|f|$, the terms of (10) are bounded by a constant times $(r/c)^n$, and the series converges uniformly on every smaller disk $r \le r_0 < c$, together with all its term-by-term derivatives.

> [!remark] Remark: Method — The Potential Equation in a Disk
> Lecture 11.26 organizes the work as follows.
> 1. **Polar form.** Write the problem in $(r, \theta)$, adding the two implicit conditions: periodicity $v(r, \theta + 2\pi) = v(r, \theta)$ and boundedness as $r \to 0^+$.
> 2. **Separate.** $v = R(r)Q(\theta)$ gives $\dfrac{r^2R'' + rR'}{R} = -\dfrac{Q''}{Q} = p$, with $Q$ periodic and $R$ bounded at $0$.
> 3. **Solve for $Q$.** $p < 0$: not periodic; $p = 0$: $Q =$ constant; $p = n^2$: $Q = A\cos(n\theta) + B\sin(n\theta)$.
> 4. **Solve for $R$** (test function $r^\alpha$): $R = r^n$ for $n \ge 1$, $R =$ constant for $n = 0$; discard $r^{-n}$ and $\ln r$.
> 5. **Fit the boundary values:** $v(c, \theta) = f(\theta)$ is a Fourier series; compute $a_0, a_n, b_n$ by (11).
> After solving, $v(0, \theta)$ is a constant, as it must be: the center has no direction.
>
> *Source: 341 lecture 11.26*

^rem-48-1

> [!example] Example §48.1: Half the Boundary at Potential 1
> Solve (1)–(4) with
>
> $$
> v(c, \theta) = f(\theta) = \begin{cases} 0, & -\pi < \theta < -\pi/2, \\ 1, & -\pi/2 < \theta < \pi/2, \\ 0, & \pi/2 < \theta < \pi. \end{cases}
> $$
>
> **Coefficients.** Since $f$ is even, $b_n = 0$, and
>
> $$
> a_0 = \frac1\pi\int_0^\pi f(\theta)\,d\theta = \frac1\pi\cdot\frac\pi2 = \frac12, \qquad a_n = \frac{2}{\pi c^n}\int_0^\pi f(\theta)\cos(n\theta)\,d\theta = \frac{2}{\pi c^n}\int_0^{\pi/2}\cos(n\theta)\,d\theta = \frac{2\sin(n\pi/2)}{n\pi c^n} .
> $$
>
> **Solution.**
>
> $$
> v(r, \theta) = \frac12 + \sum_{n=1}^{\infty}\frac{2\sin(n\pi/2)}{n\pi}\,\frac{r^n}{c^n}\cos(n\theta) . \qquad (12)
> $$
>
> **On the $x$-axis** ($\theta = 0$, $x = r$) only odd $n$ contribute, with $\sin(n\pi/2) = (-1)^{(n-1)/2}$, and $\sum_{n \text{ odd}}(-1)^{(n-1)/2}t^n/n = t - t^3/3 + t^5/5 - \cdots = \tan^{-1}t$; the same holds for $\theta = \pi$, $x = -r$. So along the $x$-axis the function has the simple closed form
>
> $$
> v = \frac12 + \frac2\pi\tan^{-1}\Big(\frac xc\Big) .
> $$
>
> **Level curves.** The level curves of $v$ are all arcs of circles that pass through the boundary points $r = c$, $\theta = \pm\pi/2$, where $f$ jumps between $0$ and $1$. (Powers asserts this; here is why.) With $z = x + iy$, the same computation in complex form (as in [[§19★ Complex Methods#^ex-19-1|Example §19.1]]) gives $v = \frac12 + \frac2\pi\operatorname{Re}\tan^{-1}(z/c)$, and $\tan^{-1}w = \frac{1}{2i}\ln\frac{1 + iw}{1 - iw}$, so
>
> $$
> v = \frac12 + \frac1\pi\arg\frac{c + iz}{c - iz} .
> $$
>
> The argument of the quotient is the angle between the vectors from $z$ to the points $ic$ and $-ic$ (up to sign and an additive constant), and by the inscribed angle theorem the points from which the segment between $(0, c)$ and $(0, -c)$ is seen at a fixed angle form a circular arc through those two points.
>
> *Powers: 4.5, Example; Source: 341 lecture 11.26*

^ex-48-1

![[m341-39-1.svg]]
*Level curves $v = 0.1, \ldots, 0.9$ of the solution (12) in the disk $c = 1$. The boundary value is $1$ on the right half (red) and $0$ on the left half (blue). Every level curve is a circular arc through the two points $(0, \pm1)$ where the boundary value jumps; the curve $v = \frac12$ is the diameter, and on the $x$-axis $v = \frac12 + \frac2\pi\tan^{-1}x$.*

> [!remark]- Connections
> - Complex-variables version: [[§136★ Examples (Dirichlet Problem for a Disk)#^ex-136-1|342 Ex. §136.1]] (the same split cylinder, rotated a quarter turn, solved by integrating the Poisson kernel in closed form).

> [!example] Example §48.2: Boundary Values θ and 2θ + cos 3θ on a Disk of Radius 2
> **(a) HW 13.** Solve $u_{xx} + u_{yy} = 0$ in $x^2 + y^2 \le 4$ with $u = f(\theta) = \theta$ ($-\pi < \theta < \pi$) on $x^2 + y^2 = 4$.
>
> *Polar form.* $u_{rr} + \frac1ru_r + \frac{1}{r^2}u_{\theta\theta} = 0$ for $0 < r < 2$; $u(r, \theta) = u(r, \theta + 2\pi)$; $u(2, \theta) = \theta$; $u$ bounded as $r \to 0^+$.
>
> *Separation and basic solutions.* $u_n = R(r)Q(\theta)$ with $\dfrac{r^2R'' + rR'}{R} = -\dfrac{Q''}{Q} = p$, $R$ bounded as $r \to 0^+$, $Q(\theta) = Q(\theta + 2\pi)$. As in the Method: $-p > 0$ gives no periodic solution; $p = 0$ gives $Q =$ constant and $R = C_0 + D_0\ln r$ with $D_0 = 0$; $p = n^2$ gives $Q_n = A\cos(n\theta) + B\sin(n\theta)$ and $R_n = C_nr^n + D_nr^{-n}$ with $D_n = 0$. So the basic solutions are $1$, $r^n\cos(n\theta)$, $r^n\sin(n\theta)$.
>
> *Coefficients.* $f(\theta) = \theta$ is odd, so $a_0 = a_n = 0$, and by (11) with $c = 2$, integrating by parts,
>
> $$
> 2^nb_n = \frac1\pi\int_{-\pi}^{\pi}\theta\sin(n\theta)\,d\theta = -\frac{1}{n\pi}\Big[\theta\cos(n\theta)\Big]_{-\pi}^{\pi} + \frac{1}{n\pi}\int_{-\pi}^{\pi}\cos(n\theta)\,d\theta = \frac{2(-1)^{n+1}}{n} .
> $$
>
> *Solution.*
>
> $$
> u(r, \theta) = \sum_{n=1}^{\infty}\frac{2(-1)^{n+1}}{n\,2^n}\,r^n\sin(n\theta) = 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\Big(\frac r2\Big)^n\sin(n\theta) .
> $$
>
> The series can be summed: $\sum(-1)^{n+1}w^n/n = \ln(1 + w)$ for $|w| < 1$, and with $w = (r/2)e^{i\theta}$ the imaginary part gives $u = 2\tan^{-1}\dfrac{r\sin\theta}{2 + r\cos\theta} = 2\tan^{-1}\dfrac{y}{x + 2}$: twice the angle that the line from the boundary point $(-2, 0)$, where $f$ jumps from $\pi$ to $-\pi$, to the point $(x, y)$ makes with the $x$-axis. For a point of the circle this angle is the inscribed angle $\theta/2$, so $u(2, \theta) = \theta$ indeed. The value at the center is $0$, the average of $\theta$ over $(-\pi, \pi)$, as the mean value property requires.
>
> *The key's final line has $(-1)^n$ in place of $(-1)^{n+1}$; its coefficient computation is correct.*
>
> **(b) Practice Final.** Same disk, with $u(2, \theta) = 2\theta + \cos 3\theta$. *Which form?* Of $A_0 + \sum e^{-2r}\big(A_n\cos(n\theta) + B_n\sin(n\theta)\big)$ and $A_0 + \sum r^n\big(A_n\cos(n\theta) + B_n\sin(n\theta)\big)$, only the second is right: $e^{-2r}\cos(n\theta)$ does not satisfy the potential equation, since the radial factor must solve $r^2R'' + rR' - n^2R = 0$.
>
> *Coefficients.* $A_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi}(2\theta + \cos 3\theta)\,d\theta = 0$. By orthogonality, $2^nA_n = \frac1\pi\int_{-\pi}^{\pi}(2\theta + \cos 3\theta)\cos(n\theta)\,d\theta$ is $1$ for $n = 3$ and $0$ otherwise, and $2^nB_n = \frac1\pi\int_{-\pi}^{\pi}2\theta\sin(n\theta)\,d\theta = \frac{4(-1)^{n+1}}{n}$ by part (a). So
>
> $$
> u(r, \theta) = \frac18r^3\cos(3\theta) + \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{2^{n-2}\,n}\,r^n\sin(n\theta) = \frac18\big(x^3 - 3xy^2\big) + 4\tan^{-1}\frac{y}{x + 2} .
> $$
>
> *The key misprints the intermediate value of $2^nB_n$ (as $-\frac{4}{n\pi}(-1)^{n-1}$); its final formula is correct.*
>
> *Source: 341 HW 13, Problem 1; 341 Practice Final, Q6*

^ex-48-2

*Continued in [[§49 The Poisson Integral Formula and the Mean Value Property]]: the Poisson integral formula, the mean value property, the maximum principle and uniqueness for Dirichlet's problem.*

## The Poisson Equation in a Disk

The bonus lecture of 12.3 solved the Poisson equation ([[§46 Further Examples for a Rectangle#^def-46-1|Definition §46.1]]) in a disk. In place of a polynomial particular solution, both $u$ and the source are expanded in Fourier series in $\theta$, which turns the PDE into one ODE for each harmonic. (The lecture writes $\nabla^2u = f$; in Powers' notation $f = -H$.)

> [!example] Example §48.3: The Poisson Equation in the Unit Disk
> Solve
>
> $$
> u_{xx} + u_{yy} = f(x, y), \quad x^2 + y^2 < 1; \qquad u = 0, \quad x^2 + y^2 = 1 .
> $$
>
> **Polar form.** $u_{rr} + \frac1ru_r + \frac{1}{r^2}u_{\theta\theta} = f(r, \theta)$ for $0 < r < 1$; $u(r, \theta) = u(r, \theta + 2\pi)$; $u(1, \theta) = 0$; $u$ bounded as $r \to 0^+$.
>
> **Step 1: Fourier series in $\theta$.** For each $r$, $u$ and $f$ are $2\pi$-periodic in $\theta$:
>
> $$
> u = u_0(r) + \sum_{n=1}^{\infty}\big(u_n(r)\cos(n\theta) + w_n(r)\sin(n\theta)\big), \qquad f = f_0(r) + \sum_{n=1}^{\infty}\big(f_n(r)\cos(n\theta) + g_n(r)\sin(n\theta)\big),
> $$
>
> with $u_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi}u\,d\theta$, $u_n = \frac1\pi\int_{-\pi}^{\pi}u\cos(n\theta)\,d\theta$, $w_n = \frac1\pi\int_{-\pi}^{\pi}u\sin(n\theta)\,d\theta$, and $f_0, f_n, g_n$ likewise.
>
> **Step 2: ODEs for the coefficients.** Since $\partial_\theta^2$ multiplies the $n$th harmonic by $-n^2$, matching coefficients gives
>
> $$
> u_0'' + \frac1ru_0' = f_0, \qquad u_n'' + \frac1ru_n' - \frac{n^2}{r^2}u_n = f_n, \qquad w_n'' + \frac1rw_n' - \frac{n^2}{r^2}w_n = g_n ,
> $$
>
> each with the conditions "$=0$ at $r = 1$" and "bounded as $r \to 0^+$".
>
> **Step 3: Solve.** The homogeneous equations have the solutions $r^n$, $r^{-n}$ ($n \ge 1$) and $1$, $\ln r$ ($n = 0$) (Theorem §48.2). Their Wronskians are $W(r^n, r^{-n}) = -2n/r$ and $W(1, \ln r) = 1/r$, and variation of parameters ([[§22★ Variation of Parameters#^thm-22-1|331 Thm. §22.1]]; the lecture's "Wronskian method", $u_n = A(r)r^n + B(r)r^{-n}$ with $A'r^n + B'r^{-n} = 0$, $nA'r^{n-1} - nB'r^{-n-1} = f_n$) gives
>
> $$
> A'(r) = \frac{1}{2n}r^{1-n}f_n(r), \qquad B'(r) = -\frac{1}{2n}r^{1+n}f_n(r) .
> $$
>
> Now choose the constants. Boundedness at $0$ requires the $r^{-n}$ part to be $-\frac{r^{-n}}{2n}\int_0^rt^{1+n}f_n(t)\,dt$ (lower limit $0$, which is $O(r^2)$ for bounded $f_n$) with no extra multiple of $r^{-n}$; the condition at $r = 1$ then fixes the multiple of $r^n$. The result is
>
> $$
> u_n(r) = -\frac{r^{-n}}{2n}\int_0^rt^{1+n}f_n(t)\,dt + \frac{r^n}{2n}\int_1^rt^{1-n}f_n(t)\,dt + \frac{r^n}{2n}\int_0^1t^{1+n}f_n(t)\,dt ,
> $$
>
> and $w_n$ is the same with $g_n$ in place of $f_n$. For $n = 0$, $A' = -r\ln r\,f_0$ and $B' = rf_0$ for $u_0 = A(r) + B(r)\ln r$, and the bounded solution vanishing at $r = 1$ is
>
> $$
> u_0(r) = \ln r\int_0^rtf_0(t)\,dt - \int_1^rt\ln t\,f_0(t)\,dt .
> $$
>
> (At $r = 1$ both terms vanish; as $r \to 0^+$ the first behaves like $r^2\ln r \to 0$ and the second has a finite limit, since $t\ln t$ is bounded.)
>
> **(i) $f = r\sin\theta$** ($= y$; lecture 12.3). Only $g_1 = r$ is nonzero, so $u_0 = u_n = 0$ and $w_n = 0$ for $n \ge 2$, while
>
> $$
> w_1(r) = -\frac{1}{2r}\int_0^rt^3\,dt + \frac r2\int_1^rt\,dt + \frac r2\int_0^1t^3\,dt = -\frac{r^3}{8} + \frac{r^3 - r}{4} + \frac r8 = \frac{r^3 - r}{8} .
> $$
>
> So $u = \frac18(r^3 - r)\sin\theta = \frac18(x^2 + y^2 - 1)y$. Check: $\nabla^2\big[(x^2y + y^3 - y)/8\big] = (2y + 6y)/8 = y$, and $u = 0$ on the unit circle.
>
> **(ii) $f = r$** (Practice Final). Only $f_0 = r$ is nonzero:
>
> $$
> u_0(r) = \ln r\int_0^rt^2\,dt - \int_1^rt^2\ln t\,dt = \frac{r^3\ln r}{3} - \Big[\frac{t^3\ln t}{3} - \frac{t^3}{9}\Big]_1^r = \frac{r^3 - 1}{9} .
> $$
>
> So $u = \frac19(r^3 - 1)$. Check: $u_{rr} + \frac1ru_r = \frac{6r}{9} + \frac{3r}{9} = r$.
>
> *The lecture's final formula for $u_n$ drops the factor $\frac{1}{2n}$ that appears in its $A'$, $B'$, so its answer for (i), $\frac14(r^3 - r)\sin\theta$, is twice the correct one. The Practice Final key's general formula for $u_0$ in part (b) has the lower limits $0$ and $1$ of the two integrals interchanged (as written it is unbounded at $r = 0$ and nonzero at $r = 1$); its part (c) uses the correct limits and gets $\frac19(r^3 - 1)$.*
>
> *Source: 341 lecture 12.3; 341 Practice Final, Q11*

^ex-48-3
