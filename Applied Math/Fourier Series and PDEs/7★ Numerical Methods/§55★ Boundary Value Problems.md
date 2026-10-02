---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 7
section: 55
powers: "7.1"
aliases: ["Powers 7.1"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§54★ More Difficult Examples]] · ↑ [[· 7★ Numerical Methods]] · [[§56★ Heat Problems]] →

*Powers, Section 7.1.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

Most boundary value problems that arise in practice cannot be solved in closed form: the coefficients vary, the region is irregular, or the formula (here, Airy functions) is less informative than a table of numbers. This section replaces a two-point boundary value problem for an ODE by a finite system of linear equations for approximate values $u_i \approx u(x_i)$ at equally spaced mesh points, using difference quotients in place of derivatives. The same replacement of $u''$ by a second difference is the building block of every scheme in this chapter, for the heat, wave and potential equations. Taylor's theorem explains why it works: the central difference quotients differ from the derivatives by terms proportional to $(\Delta x)^2$.

## Replacement Equations

> [!definition] Definition §55.1: Mesh Points; Replacement Equations
> Let a boundary value problem be posed on $0 \le x \le 1$. Choose a positive integer $n$ and put
>
> $$
> x_i = i\,\Delta x, \qquad \Delta x = \frac1n, \qquad i = 0, 1, \ldots, n .
> $$
>
> The $x_i$ are the **mesh points**, and the numbers $u_i \cong u(x_i)$, $i = 0, 1, \ldots, n$, approximate the solution there. The **replacement equations** are the algebraic equations obtained from the differential equation at each mesh point $x_i$, and from the boundary conditions, by the replacements
>
> | differential equation | boundary condition |
> |---|---|
> | $u(x) \to u_i$ | $u(0) \to u_0$, $\quad u(1) \to u_n$ |
> | $\dfrac{d^2u}{dx^2}(x) \to \dfrac{u_{i+1} - 2u_i + u_{i-1}}{(\Delta x)^2}$ | $\dfrac{du}{dx}(0) \to \dfrac{u_1 - u_{-1}}{2\,\Delta x}$ |
> | $\dfrac{du}{dx}(x) \to \dfrac{u_{i+1} - u_{i-1}}{2\,\Delta x}$ | $\dfrac{du}{dx}(1) \to \dfrac{u_{n+1} - u_{n-1}}{2\,\Delta x}$ |
> | $f(x) \to f(x_i)$ | |
>
> Here $f(x)$ stands for any coefficient or inhomogeneity in the differential equation. The values $u_{-1}$ and $u_{n+1}$ belong to **fictitious points** $x_{-1} = -\Delta x$, $x_{n+1} = 1 + \Delta x$ outside the interval; they are used only to express a derivative boundary condition.
>
> *Powers: 7.1, Table 2*

^def-55-1

> [!remark]- Connections
> - The same idea for an initial value problem: Euler's method replaces $y'$ by the forward quotient $(y_{n+1} - y_n)/h$, [[§10 Numerical Approximations꞉ Euler's Method#^def-10-1|331 Def. §10.1]]. There the unknowns can be computed one after another; for a boundary value problem the conditions at both ends couple all the $u_i$, and they must be found together from one linear system.
> - That system is tridiagonal, hence sparse; elimination (an LU factorization without fill-in) solves it in a number of operations proportional to $n$, [[§15 Matrix Factorizations#^rem-15-4|235 Remark: Numerical Notes]].

> [!remark] Remark: Method — Replacement Equations for a Two-Point Problem
> To solve $u'' + k(x)u' + p(x)u = f(x)$, $0 < x < 1$, with boundary conditions at $x = 0$ and $x = 1$:
> 1. Choose $n$, set $\Delta x = 1/n$ and $x_i = i\,\Delta x$.
> 2. At each mesh point where $u$ is unknown, write the differential equation with the replacements of Definition §55.1. With $u_i$ unknown for $i = 1, \ldots, n - 1$ this gives $n - 1$ equations.
> 3. A condition $u(0) = a$ or $u(1) = b$ simply fixes $u_0 = a$ or $u_n = b$; move these known values to the right-hand side.
> 4. A condition involving $u'(1)$ makes $u_n$ unknown too. Use the equation of step 2 also at $i = n$; it contains the fictitious value $u_{n+1}$. Solve the replaced boundary condition for $u_{n+1}$ and substitute. The same at $x = 0$ with $u_{-1}$.
> 5. Collect coefficients: the result is a tridiagonal linear system, one equation per unknown. Solve it by elimination or iteratively.
> 6. Repeat with a larger $n$ and compare; agreement of the two tables indicates the accuracy.

^rem-55-1

![[m341-55-2.svg]]
*Mesh for a problem with $u(0)$ given and $u'(1)$ given. The equation at $x_n = 1$ reaches the fictitious point $x_{n+1}$ (orange); the central-difference form of the boundary condition expresses $u_{n+1}$ through $u_{n-1}$, which removes it.*

> [!example] Example §55.1: A Problem with an Airy-Function Solution
> Solve approximately
>
> $$
> \frac{d^2u}{dx^2} - 12xu = -1, \quad 0 < x < 1, \qquad u(0) = 1, \quad u(1) = -1 . \qquad (1),\ (2)
> $$
>
> The replacement equations are
>
> $$
> \frac{u_{i+1} - 2u_i + u_{i-1}}{(\Delta x)^2} - 12x_iu_i = -1, \quad i = 1, \ldots, n - 1, \qquad u_0 = 1, \quad u_n = -1 . \qquad (3),\ (4)
> $$
>
> Take $n = 5$, so $\Delta x = \frac15$, $(\Delta x)^{-2} = 25$ and $12x_i = \frac{12i}{5}$:
>
> $$
> \begin{aligned}
> 25(u_2 - 2u_1 + u_0) - \tfrac{12}{5}u_1 &= -1, \\
> 25(u_3 - 2u_2 + u_1) - \tfrac{24}{5}u_2 &= -1, \\
> 25(u_4 - 2u_3 + u_2) - \tfrac{36}{5}u_3 &= -1, \\
> 25(u_5 - 2u_4 + u_3) - \tfrac{48}{5}u_4 &= -1 .
> \end{aligned} \qquad (5)
> $$
>
> With $u_0 = 1$ and $u_5 = -1$ moved to the right ($-1 - 25 = -26$ in the first equation, $-1 + 25 = 24$ in the last), and the diagonal coefficients $-50 - \frac{12i}{5}$,
>
> $$
> \begin{aligned}
> -52.4u_1 + 25u_2 \phantom{{} + 25u_3} &= -26, \\
> 25u_1 - 54.8u_2 + 25u_3 &= -1, \\
> 25u_2 - 57.2u_3 + 25u_4 &= -1, \\
> 25u_3 - 59.6u_4 &= 24 .
> \end{aligned} \qquad (7)
> $$
>
> Elimination gives the first row of the table below. Powers' Table 1 was computed in the same way with $n = 100$; the row $n = 100$ agrees with a high-accuracy computation of the exact solution to the digits shown.
>
> | $x$ | $0$ | $0.2$ | $0.4$ | $0.6$ | $0.8$ | $1$ |
> |---|---|---|---|---|---|---|
> | $u_i$, $n = 5$ | $1$ | $0.635$ | $0.290$ | $-0.039$ | $-0.419$ | $-1$ |
> | $u_i$, $n = 100$ | $1$ | $0.643$ | $0.302$ | $-0.026$ | $-0.408$ | $-1$ |
>
> Already the coarse mesh is within about $0.013$ of the fine one.
>
> *Powers: 7.1, Example 1 and Table 1*

^ex-55-1

> [!example] Example §55.2: A Derivative Boundary Condition
> Solve approximately
>
> $$
> \frac{d^2u}{dx^2} - 10u = f(x), \quad 0 < x < 1, \qquad u(0) = 1, \quad \frac{du}{dx}(1) = -1, \qquad
> f(x) = \begin{cases} 0, & 0 < x < \frac12, \\ -50, & x = \frac12, \\ -100, & \frac12 < x < 1 . \end{cases} \qquad (8),\ (9)
> $$
>
> (At the jump, $f$ is given its average value.) The replacement equations are
>
> $$
> \frac{u_{i+1} - 2u_i + u_{i-1}}{(\Delta x)^2} - 10u_i = f(x_i), \qquad u_0 = 1, \qquad \frac{u_{n+1} - u_{n-1}}{2\,\Delta x} = -1 . \qquad (10),\ (11)
> $$
>
> Now $u_n$ is unknown, so (10) is needed for $i = 1, \ldots, n$, and at $i = n$ it involves $u_{n+1}$. Solving the boundary replacement for it,
>
> $$
> u_{n+1} = u_{n-1} - 2\,\Delta x , \qquad (12)
> $$
>
> and substituting in (10) at $i = n$ gives
>
> $$
> \frac{2u_{n-1} - 2\,\Delta x - 2u_n}{(\Delta x)^2} - 10u_n = f(x_n) . \qquad (13)
> $$
>
> With $n = 4$, $\Delta x = \frac14$, the equations for $i = 1, 2, 3$ are $16(u_2 - 2u_1 + u_0) - 10u_1 = 0$, $16(u_3 - 2u_2 + u_1) - 10u_2 = -50$, $16(u_4 - 2u_3 + u_2) - 10u_3 = -100$, and (13) is $16(2u_3 - \frac12 - 2u_4) - 10u_4 = -100$. With $u_0 = 1$:
>
> $$
> \begin{aligned}
> -42u_1 + 16u_2 \phantom{{} + 16u_3} &= -16, \\
> 16u_1 - 42u_2 + 16u_3 &= -50, \\
> 16u_2 - 42u_3 + 16u_4 &= -100, \\
> 32u_3 - 42u_4 &= -92 .
> \end{aligned} \qquad (14)
> $$
>
> The solution, together with $n = 100$ and the exact solution (solve $u'' - 10u = 0$ on $(0, \frac12)$ and $u'' - 10u = -100$ on $(\frac12, 1)$ with $\cosh$ and $\sinh$ of $\sqrt{10}\,x$, and match $u$ and $u'$ at $x = \frac12$):
>
> | $x$ | $0$ | $0.25$ | $0.5$ | $0.75$ | $1$ |
> |---|---|---|---|---|---|
> | $u_i$, $n = 4$ | $1$ | $2.174$ | $4.707$ | $7.057$ | $7.567$ |
> | $u_i$, $n = 100$ | $1$ | $2.155$ | $4.729$ | $7.125$ | $7.629$ |
> | exact | $1$ | $2.155$ | $4.729$ | $7.125$ | $7.629$ |
>
> Even with four unknowns the error is under $0.07$ (figure below, panel (a)).
>
> *Powers: 7.1, Example 2 and Table 3*

^ex-55-2

> [!remark] Remark: Iterative Solution
> Elimination is not the only way to solve systems like (7) or (14). Solve the $i$th equation for the $i$th unknown; the resulting formulas refer to one another (the formula for $u_2$ uses $u_1$ and $u_3$, whose formulas use $u_2$). Start from guessed values, feed them through the formulas to get improved values, and repeat until the values settle down. This needs a lot of arithmetic but no strategy, while elimination is the reverse; and it may also work for nonlinear equations, where elimination does not. The Gauss–Seidel version of this idea is the standard method for the large systems of [[§58★ Potential Equation#^def-58-2|Definition §58.2]].

^rem-55-2

## Why the Replacement Equations Work

> [!theorem] Proposition §55.1: Errors of the Central Difference Quotients
> If $u$ has three continuous derivatives near $x_i$, then
>
> $$
> \frac{u(x_{i+1}) - u(x_{i-1})}{2\,\Delta x} = u'(x_i) + \frac{(\Delta x)^2}{6}\,u^{(3)}(\bar x_i) ; \qquad (15)
> $$
>
> if $u$ has four continuous derivatives near $x_i$, then
>
> $$
> \frac{u(x_{i+1}) - 2u(x_i) + u(x_{i-1})}{(\Delta x)^2} = u''(x_i) + \frac{(\Delta x)^2}{12}\,u^{(4)}(\bar{\bar x}_i) , \qquad (16)
> $$
>
> where $\bar x_i$ and $\bar{\bar x}_i$ are points of $[x_{i-1}, x_{i+1}]$.
>
> *Powers: 7.1, Equations (15) and (16)*

^prop-55-1

> [!proof]+ Proof
> *Powers leaves this to Exercise 12 (Taylor expansion with $h = \pm\Delta x$); here are the details.* Write $x = x_i$, $h = \Delta x$.
>
> **(15).** Taylor's theorem with Lagrange remainder, to third order, gives points $\xi_+ \in (x, x + h)$ and $\xi_- \in (x - h, x)$ with
>
> $$
> u(x \pm h) = u(x) \pm hu'(x) + \frac{h^2}{2}u''(x) \pm \frac{h^3}{6}u^{(3)}(\xi_\pm) .
> $$
>
> Subtracting, the even terms cancel: $u(x + h) - u(x - h) = 2hu'(x) + \frac{h^3}{6}\big(u^{(3)}(\xi_+) + u^{(3)}(\xi_-)\big)$. Divide by $2h$:
>
> $$
> \frac{u(x + h) - u(x - h)}{2h} = u'(x) + \frac{h^2}{6}\cdot\frac{u^{(3)}(\xi_+) + u^{(3)}(\xi_-)}{2} .
> $$
>
> The average of two values of the continuous function $u^{(3)}$ lies between them, so by the intermediate value theorem it equals $u^{(3)}(\bar x_i)$ for some $\bar x_i$ between $\xi_-$ and $\xi_+$. This is (15).
>
> **(16).** To fourth order, with $\eta_+ \in (x, x + h)$ and $\eta_- \in (x - h, x)$,
>
> $$
> u(x \pm h) = u(x) \pm hu'(x) + \frac{h^2}{2}u''(x) \pm \frac{h^3}{6}u^{(3)}(x) + \frac{h^4}{24}u^{(4)}(\eta_\pm) .
> $$
>
> Adding, the odd terms cancel: $u(x + h) - 2u(x) + u(x - h) = h^2u''(x) + \frac{h^4}{24}\big(u^{(4)}(\eta_+) + u^{(4)}(\eta_-)\big)$. Divide by $h^2$ and replace the average $\frac12\big(u^{(4)}(\eta_+) + u^{(4)}(\eta_-)\big)$ by $u^{(4)}(\bar{\bar x}_i)$ as before; the factor is $\frac{h^2}{24}\cdot 2 = \frac{h^2}{12}$. This is (16).

^pf-55-1

*Uses:* [[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]] (Taylor with Lagrange remainder), [[§18 Properties of Continuous Functions#^thm-18-3|451 Thm. §18.3]] (intermediate value theorem)

> [!remark]- Connections
> - The forward quotient of Euler's method is less accurate: the same expansion gives $\frac{u(x + h) - u(x)}{h} = u'(x) + \frac h2u''(\xi)$, an error proportional to $h$ rather than $h^2$. This is the first-order error observed for Euler's method in [[§10 Numerical Approximations꞉ Euler's Method#^prop-10-1|331 Prop. §10.1]]. Centering the quotient at $x_i$ cancels the $h$ term.

> [!remark] Remark: Exact for Low-Degree Polynomials
> If $u$ is a polynomial of degree at most $3$, then $u^{(4)} = 0$ and (16) is exact; for degree at most $2$, (15) is exact too. So when the exact solution is such a polynomial (and the coefficients are constant), the exact values $u(x_i)$ satisfy the replacement equations, and since those equations have a unique solution, the numerical solution *is* the exact solution at the mesh points. For instance, $u'' = -1$, $u(0) = 0$, $u(1) = 1$ has the solution $u = \frac12x(3 - x)$; with $n = 4$ the replacement equations $16(u_{i+1} - 2u_i + u_{i-1}) = -1$ give $u_1 = \frac{11}{32}$, $u_2 = \frac58$, $u_3 = \frac{27}{32}$, which are $u(\frac14)$, $u(\frac12)$, $u(\frac34)$ exactly (Powers' Exercises 1–2).

^rem-55-3

Now let $u$ be the solution of the general linear problem

$$
\frac{d^2u}{dx^2} + k(x)\frac{du}{dx} + p(x)u(x) = f(x), \quad 0 < x < 1, \qquad \alpha u(0) - \alpha'u'(0) = a, \quad \beta u(1) + \beta'u'(1) = b . \qquad (17),\ (18)
$$

If $u$ has enough derivatives, then at every mesh point it satisfies (17), and so by Proposition §55.1 it satisfies

$$
\frac{u(x_{i+1}) - 2u(x_i) + u(x_{i-1})}{(\Delta x)^2} + k(x_i)\frac{u(x_{i+1}) - u(x_{i-1})}{2\,\Delta x} + p(x_i)u(x_i) = f(x_i) + \delta_i, \qquad (19)
$$

$$
\delta_i = \frac{(\Delta x)^2}{12}u^{(4)}(\bar{\bar x}_i) + k(x_i)\frac{(\Delta x)^2}{6}u^{(3)}(\bar x_i) .
$$

The replacement equation for (17) is

$$
\frac{u_{i+1} - 2u_i + u_{i-1}}{(\Delta x)^2} + k(x_i)\frac{u_{i+1} - u_{i-1}}{2\,\Delta x} + p(x_i)u_i = f(x_i) . \qquad (20)
$$

Since $\delta_i$ is proportional to $(\Delta x)^2$, the exact values $u(x_i)$ nearly satisfy (20), and conversely the solution $u_0, \ldots, u_n$ of (20) nearly satisfies (19).

> [!theorem] Theorem §55.2: Convergence of the Replacement Equations
> Under continuity and further conditions on $k(x)$, $p(x)$ and $f(x)$, the numbers $u_0, u_1, \ldots, u_n$ computed from the replacement equations (20) for the problem (17)–(18) approach the values $u(x_i)$ of the solution as $\Delta x \to 0$.
>
> *Powers: 7.1 (text)*

^thm-55-2

*Powers omits the proof.*

> [!remark] Remark: Why It Works
> "Nearly satisfying" is not yet "nearly equal". Subtract (20) from (19): the errors $e_i = u(x_i) - u_i$ satisfy the replacement equations with right-hand sides $\delta_i$ and zero boundary data, so $e = A^{-1}\delta$, where $A$ is the matrix of the system. Small $\delta_i$ (consistency) give small $e_i$ only if $A^{-1}$ stays bounded as $n$ grows (stability); the "further conditions" of the theorem are what guarantee this. For example, when $k = 0$ and $p \le 0$ with Dirichlet conditions one can show $|e_i| \le \frac18\max_j|\delta_j|$, so the error is proportional to $(\Delta x)^2$. When $p$ is positive and close to an eigenvalue, $A$ is nearly singular and coarse meshes fail badly; [[§55★ Boundary Value Problems#^ex-55-4|Example §55.4]] shows this. Consistency plus stability is the pattern of the whole chapter; for time-dependent problems stability becomes a condition on the time step ([[§56★ Heat Problems#^cor-56-2|Corollary §56.2]]).

^rem-55-4

## Accuracy in Practice

> [!example] Example §55.3: The Error Is Proportional to the Square of the Mesh Size
> Solve $u'' - u = -2x$, $0 < x < 1$, $u(0) = 0$, $u(1) = 1$, with $n = 4$, and compare with the exact solution.
>
> **Exact solution.** A particular solution is $2x$, and $\sinh x$ solves $u'' - u = 0$ with $u(0) = 0$. So $u = 2x + c\sinh x$, and $u(1) = 1$ gives $c = -1/\sinh 1$:
>
> $$
> u(x) = 2x - \frac{\sinh x}{\sinh 1} .
> $$
>
> **Replacement equations.** With $(\Delta x)^{-2} = 16$, $16(u_{i+1} - 2u_i + u_{i-1}) - u_i = -2x_i$, that is $16u_{i-1} - 33u_i + 16u_{i+1} = -2x_i$. With $u_0 = 0$, $u_4 = 1$:
>
> $$
> -33u_1 + 16u_2 = -\tfrac12, \qquad 16u_1 - 33u_2 + 16u_3 = -1, \qquad 16u_2 - 33u_3 = -\tfrac32 - 16 = -\tfrac{35}{2} .
> $$
>
> The solution is $u_1 = \frac{10849}{38082} \approx 0.28489$, $u_2 = \frac{321}{577} \approx 0.55633$, $u_3 = \frac{30467}{38082} \approx 0.80004$.
>
> | $x$ | $0.25$ | $0.5$ | $0.75$ |
> |---|---|---|---|
> | $u_i$, $n = 4$ | $0.28489$ | $0.55633$ | $0.80004$ |
> | exact | $0.28505$ | $0.55659$ | $0.80028$ |
>
> **Refining.** The largest error over the mesh points is $2.65 \times 10^{-4}$ for $n = 4$, $6.86 \times 10^{-5}$ for $n = 8$ and $1.72 \times 10^{-5}$ for $n = 16$: each halving of $\Delta x$ divides the error by about $4$, as the $(\Delta x)^2$ in $\delta_i$ predicts. (Here $p = -1 \le 0$, the stable case of Remark: Why It Works.)
>
> *Powers: Exercises 7.1.3 and 7.1.4*

^ex-55-3

> [!example] Example §55.4: A Problem Near Resonance
> Solve $u'' + 10u = 0$, $0 < x < 1$, $u(0) = 0$, $u(1) = -1$, with $n = 3$ and $n = 4$, and explain why the results differ so much.
>
> **$n = 3$.** With $(\Delta x)^{-2} = 9$: $9(u_{i+1} - 2u_i + u_{i-1}) + 10u_i = 0$, or $9u_{i-1} - 8u_i + 9u_{i+1} = 0$. With $u_0 = 0$, $u_3 = -1$: $-8u_1 + 9u_2 = 0$ and $9u_1 - 8u_2 = 9$, so $u_1 = \frac{81}{17} \approx 4.765$, $u_2 = \frac{72}{17} \approx 4.235$.
>
> **$n = 4$.** With $(\Delta x)^{-2} = 16$: $16u_{i-1} - 22u_i + 16u_{i+1} = 0$. With $u_0 = 0$, $u_4 = -1$: $-22u_1 + 16u_2 = 0$, $16u_1 - 22u_2 + 16u_3 = 0$, $16u_2 - 22u_3 = 16$, so $u_1 = \frac{512}{77} \approx 6.649$, $u_2 = \frac{64}{7} \approx 9.143$, $u_3 = \frac{456}{77} \approx 5.922$.
>
> **Exact solution.** $u = -\dfrac{\sin(\sqrt{10}\,x)}{\sin\sqrt{10}}$. Since $\sqrt{10} \approx 3.162$ is close to $\pi$, $\sin\sqrt{10} \approx -0.0207$, and the solution is large: $u(\frac12) \approx 48.3$. Neither mesh comes close, and even $n = 8$ gives only $u_4 \approx 24.0$ (figure below, panel (b)).
>
> **Why.** The number $10$ lies just above $\lambda_1 = \pi^2 \approx 9.870$, the first eigenvalue of $u'' + \lambda u = 0$, $u(0) = u(1) = 0$; the size of the solution is governed by the small gap $10 - \pi^2 \approx 0.130$. The replacement equations have their own first eigenvalue: $\sin(\pi x_i)$ satisfies $u_{i+1} - 2u_i + u_{i-1} = -4\sin^2(\frac{\pi\Delta x}{2})\,u_i$, so it is $\frac{4}{(\Delta x)^2}\sin^2\frac{\pi\Delta x}{2}$, which equals $9$ for $n = 3$, $9.373$ for $n = 4$, $9.743$ for $n = 8$ and $9.869$ for $n = 100$. The coarse meshes see a gap of $1$ or $0.63$ instead of $0.13$, and so underestimate the response by a large factor. Near an eigenvalue the problem is ill-conditioned, and only a fine mesh gives reliable numbers.
>
> *Powers: Exercise 7.1.7*

^ex-55-4

![[m341-55-1.svg]]
*(a) Example §55.2: four unknowns (red) already follow the exact solution (blue) closely, including the change of curvature where the source switches on at $x = \frac12$. (b) Example §55.4: for $u'' + 10u = 0$, close to the eigenvalue $\pi^2$, the exact solution has amplitude about $48$, and the meshes $n = 3, 4, 8$ fall far short.*
