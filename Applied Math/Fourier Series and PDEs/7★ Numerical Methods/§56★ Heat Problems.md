---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 7
section: 56
powers: "7.2"
aliases: ["Powers 7.2"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§55★ Boundary Value Problems]] · ↑ [[· 7★ Numerical Methods]] · [[§57★ Wave Equation]] →

*Powers, Section 7.2.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

For the heat equation $u_{xx} = u_t$ the space derivative is replaced as in [[§55★ Boundary Value Problems|§55]], and the time derivative by a forward difference. The result is an explicit scheme: each new temperature is a weighted average of three temperatures at the previous time level, so the table of values is filled in row by row from the initial condition, the way Euler's method marches an ODE forward. The price of this simplicity is a restriction on the time step. If $r = \Delta t/(\Delta x)^2$ exceeds $\frac12$, the computed values oscillate and grow without bound, although the true temperatures decay. Powers gives a rule of thumb that detects this before computing: no weight may be negative.

## The Explicit Scheme

In heat problems there are two independent variables, $0 < x < 1$ and $t > 0$. A table of $u(x, t)$ uses equally spaced points and times,

$$
x_i = i\,\Delta x, \qquad t_m = m\,\Delta t, \qquad i = 0, 1, \ldots, n, \quad m = 0, 1, 2, \ldots, \qquad \Delta x = \frac1n .
$$

> [!definition] Definition §56.1: Explicit Scheme for the Heat Equation
> Write $u_i(m) \cong u(x_i, t_m)$: the subscript gives the position, the number in parentheses the time level. The space derivatives are replaced as in [[§55★ Boundary Value Problems#^def-55-new1|Definition §55.1]], and the time derivative by the **forward difference**:
>
> $$
> \frac{\partial^2u}{\partial x^2}(x_i, t_m) \to \frac{u_{i+1}(m) - 2u_i(m) + u_{i-1}(m)}{(\Delta x)^2}, \qquad
> \frac{\partial u}{\partial x}(x_i, t_m) \to \frac{u_{i+1}(m) - u_{i-1}(m)}{2\,\Delta x}, \qquad (1),\ (2)
> $$
>
> $$
> \frac{\partial u}{\partial t}(x_i, t_m) \to \frac{u_i(m + 1) - u_i(m)}{\Delta t} . \qquad (3)
> $$
>
> For the heat problem
>
> $$
> \frac{\partial^2u}{\partial x^2} = \frac{\partial u}{\partial t}, \quad 0 < x < 1, \quad 0 < t; \qquad u(0, t) = 0, \quad u(1, t) = 0; \qquad u(x, 0) = f(x) \qquad (4)\text{–}(6)
> $$
>
> the replacement equations are
>
> $$
> \frac{u_{i-1}(m) - 2u_i(m) + u_{i+1}(m)}{(\Delta x)^2} = \frac{u_i(m + 1) - u_i(m)}{\Delta t}, \qquad i = 1, \ldots, n - 1, \quad m = 0, 1, 2, \ldots, \qquad (7)
> $$
>
> and solved for the new value they give the **explicit scheme**
>
> $$
> u_i(m + 1) = r\,u_{i-1}(m) + (1 - 2r)\,u_i(m) + r\,u_{i+1}(m), \qquad r = \frac{\Delta t}{(\Delta x)^2} . \qquad (8)
> $$
>
> Each $u_i(m + 1)$ is computed from values at the preceding time level only.
>
> *Powers: 7.2, Equations (1)–(8)*

^def-56-1

> [!remark]- Connections
> - If only $x$ is discretized, (7) becomes a system of ODEs $u_i'(t) = \big(u_{i-1} - 2u_i + u_{i+1}\big)/(\Delta x)^2$ (the "method of lines"), and (8) is exactly Euler's method with step $\Delta t$ applied to that system: [[§10 Numerical Approximations꞉ Euler's Method#^def-10-1|331 Def. §10.1]].
> - In vector form (8) reads $\mathbf u(m + 1) = M\mathbf u(m)$ with a tridiagonal matrix $M$, a discrete dynamical system; expanding $\mathbf u(0)$ in eigenvectors of $M$ gives $\mathbf u(m) = \sum c_k\mu_k^m\mathbf v_k$, [[§37 Discrete Dynamical Systems#^thm-37-1|235 Thm. §37.1]]. The eigenvectors are the sampled sines $\sin(k\pi x_i)$, with $\mu_k = 1 - 4r\sin^2\frac{k\pi\Delta x}{2}$; compare the factors $e^{-k^2\pi^2t}$ of the series solution.

> [!remark] Remark: Method — The Explicit Scheme for a Heat Problem
> 1. Choose $\Delta x = 1/n$ and $\Delta t$; compute $r = \Delta t/(\Delta x)^2$ and check stability ([[§56★ Heat Problems#^thm-56-1|Theorem §56.1]]).
> 2. Write the replacement equations at each mesh point where $u$ is unknown and solve them for $u_i(m + 1)$, as in (8). A derivative boundary condition makes the end value unknown; eliminate the fictitious point with the replaced boundary condition, as in [[§55★ Boundary Value Problems#^rem-55-1|§55, Remark: Method]].
> 3. Make a table with a column for each mesh point $x_0, \ldots, x_n$ and a row for each time level $t_0, t_1, \ldots$.
> 4. Fill the top row from the initial condition, $u_i(0) = f(x_i)$, and the boundary columns from the boundary conditions.
> 5. Fill each further row from the one above with the formulas of step 2.

^rem-56-1

![[m341-56-1.svg]]
*The stencil of the explicit scheme (8): the new value $u_i(m + 1)$ (red) is a weighted combination of three neighbouring values at the previous time level (blue), with weights $r$, $1 - 2r$, $r$ that add up to $1$.*

> [!example] Example §56.1: A Bar with Initial Temperature x
> Solve (4)–(6) with $f(x) = x$, $\Delta x = \frac14$ and $r = \frac12$, so $\Delta t = r(\Delta x)^2 = \frac1{32}$.
>
> With $r = \frac12$ the middle weight $1 - 2r$ vanishes and (8) becomes
>
> $$
> u_1(m + 1) = \tfrac12\big(u_0(m) + u_2(m)\big), \qquad u_2(m + 1) = \tfrac12\big(u_1(m) + u_3(m)\big), \qquad u_3(m + 1) = \tfrac12\big(u_2(m) + u_4(m)\big) . \qquad (9)
> $$
>
> The boundary conditions give $u_0(m) = u_4(m) = 0$ for $m \ge 1$, and the initial condition gives the top row $u_i(0) = x_i$. The initial condition suggests $u(1, 0) = 1$, the boundary condition $0$; neither actually specifies it. Following Powers, take $u_4(0) = 1$ (see the remark below). Filling in row by row:
>
> | $m$ | $u_0$ | $u_1$ | $u_2$ | $u_3$ | $u_4$ |
> |---|---|---|---|---|---|
> | $0$ | $0$ | $0.25$ | $0.5$ | $0.75$ | $1$ |
> | $1$ | $0$ | $0.25$ | $0.5$ | $0.75$ | $0$ |
> | $2$ | $0$ | $0.25$ | $0.5$ | $0.25$ | $0$ |
> | $3$ | $0$ | $0.25$ | $0.25$ | $0.25$ | $0$ |
> | $4$ | $0$ | $0.125$ | $0.25$ | $0.125$ | $0$ |
> | $5$ | $0$ | $0.125$ | $0.125$ | $0.125$ | $0$ |
>
> **Comparison with the exact solution.** By [[§19 Example꞉ Fixed End Temperatures#^thm-19-5|Theorem §19.5]], the solution is $u(x, t) = \sum_{n \ge 1} \frac{2(-1)^{n+1}}{n\pi}\sin(n\pi x)\,e^{-n^2\pi^2t}$ (here $b_n = 2\int_0^1x\sin(n\pi x)\,dx = \frac{2(-1)^{n+1}}{n\pi}$). At $x = \frac14, \frac12, \frac34$:
>
> | $t$ | numerical | exact |
> |---|---|---|
> | $\frac2{32}$ ($m = 2$) | $0.25,\ 0.5,\ 0.25$ | $0.217,\ 0.343,\ 0.271$ |
> | $\frac4{32}$ ($m = 4$) | $0.125,\ 0.25,\ 0.125$ | $0.129,\ 0.185,\ 0.133$ |
> | $\frac5{32}$ ($m = 5$) | $0.125,\ 0.125,\ 0.125$ | $0.096,\ 0.136,\ 0.097$ |
>
> Four intervals are a very coarse mesh, and the jump of the initial data at $x = 1$ hurts at early times; but the computed temperatures decay at the right rate on average. With $\Delta x = \frac1{40}$, $r = \frac12$ (and the same corner value $1$) the values at $t = \frac5{32}$ are $0.096$, $0.137$, $0.097$, within $0.001$ of the series.
>
> *Powers: 7.2, Example 1 and Table 4*

^ex-56-1

> [!remark]- Remark: The Corner Value
> Taking $u_4(0) = 0$ instead of $1$ (Powers' Exercise 1) gives the rows $(0.25, 0.5, 0.25)$, $(0.25, 0.25, 0.25)$, $(0.125, 0.25, 0.125)$, …: exactly the rows of Example §56.1 one level later. The choice at the corner shifts the computation by one time step $\Delta t$, an effect that disappears as $\Delta t \to 0$. So it does not matter much which value is used.

^rem-56-2

## Stability

The choice $r = \frac12$ simplified the arithmetic. A larger $r$, that is, a longer time step, would reach later times faster. It fails dramatically.

> [!example] Example §56.2: An Unstable Time Step
> Repeat Example §56.1 with $r = 1$ ($\Delta t = \frac1{16}$). Now (8) is
>
> $$
> u_i(m + 1) = u_{i-1}(m) - u_i(m) + u_{i+1}(m) ,
> $$
>
> and the table becomes
>
> | $m$ | $u_0$ | $u_1$ | $u_2$ | $u_3$ | $u_4$ |
> |---|---|---|---|---|---|
> | $0$ | $0$ | $0.25$ | $0.50$ | $0.75$ | $1$ |
> | $1$ | $0$ | $0.25$ | $0.50$ | $0.75$ | $0$ |
> | $2$ | $0$ | $0.25$ | $0.50$ | $-0.25$ | $0$ |
> | $3$ | $0$ | $0.25$ | $-0.50$ | $0.75$ | $0$ |
> | $4$ | $0$ | $-0.75$ | $1.50$ | $-1.25$ | $0$ |
> | $5$ | $0$ | $2.25$ | $-3.50$ | $2.75$ | $0$ |
>
> No one can believe that these wildly fluctuating values approximate a temperature that decays from values between $0$ and $1$ (figure below, panel (b)). This is **numerical instability**: the time step is too long relative to the mesh size.
>
> *Powers: 7.2, Table 5*

^ex-56-2

> [!definition] Definition §56.2: Numerical Stability
> A scheme that computes each time level from the preceding ones is **numerically stable** if a change in the values at one time level (a roundoff error, or the small error committed by each replacement) produces changes at later time levels that are no larger; it is **numerically unstable** if such changes can grow from level to level without bound, as in Example §56.2.
>
> *Powers: 7.2 (text)*

^def-56-2

> [!theorem] Theorem §56.1: Rule of Thumb for Stability
> Write the replacement equations solved for the new values in the form
>
> $$
> u_i(m + 1) = a_i\,u_{i-1}(m) + b_i\,u_i(m) + c_i\,u_{i+1}(m)
> $$
>
> (plus terms that do not depend on the $u$'s). The computation is stable if the coefficients satisfy two conditions:
> 1. no coefficient is negative: $a_i, b_i, c_i \ge 0$;
> 2. the sum of the coefficients is not greater than $1$: $a_i + b_i + c_i \le 1$.
>
> *Powers: 7.2 (text)*

^thm-56-1

*Powers omits the proof ("the analysis of instability requires familiarity with matrix theory").*

> [!remark] Remark: Why It Works
> Let two computations with the same boundary data differ by $e_i(m)$ at level $m$. Subtracting, the terms that do not involve the $u$'s cancel and $e_i(m + 1) = a_ie_{i-1}(m) + b_ie_i(m) + c_ie_{i+1}(m)$, with $e = 0$ at points where $u$ is prescribed. If the coefficients are nonnegative with sum at most $1$, then
>
> $$
> |e_i(m + 1)| \le a_i|e_{i-1}(m)| + b_i|e_i(m)| + c_i|e_{i+1}(m)| \le (a_i + b_i + c_i)\max_j|e_j(m)| \le \max_j|e_j(m)| ,
> $$
>
> so the largest difference never grows: the scheme is stable in the sense of Definition §56.2. The same estimate shows that each new value lies between the smallest and largest neighbouring old values (when the sum is $1$), a discrete maximum principle, just as the true temperature never exceeds its initial and boundary values.
>
> A negative coefficient breaks this, and the sampled sines show how. For (8), $u_i(m) = \mu^m\sin(k\pi x_i)$ is a solution if $\mu = 1 - 4r\sin^2\frac{k\pi\Delta x}{2}$. The exact solution multiplies the same mode by $e^{-k^2\pi^2\Delta t}$ per step, a number between $0$ and $1$. If $r > \frac12$, then for the highest mode ($k = n - 1$, with $\sin^2\frac{k\pi\Delta x}{2} = \cos^2\frac{\pi\Delta x}{2}$ close to $1$ once $\Delta x$ is small) $\mu < -1$, and the mode is amplified and changes sign at every step. In Example §56.2 ($r = 1$, $\Delta x = \frac14$, $k = 3$) the factor is $\mu = 1 - 4\sin^2\frac{3\pi}{8} \approx -2.41$, which is the growth and alternation seen in the table.

^rem-56-3

> [!theorem] Corollary §56.2: The Stability Condition r ≤ 1/2
> For the problem (4)–(6), the explicit scheme (8) satisfies the rule of thumb if and only if
>
> $$
> r = \frac{\Delta t}{(\Delta x)^2} \le \frac12 , \qquad\text{that is,}\qquad \Delta t \le \tfrac12(\Delta x)^2 .
> $$
>
> So $r = \frac12$ in Example §56.1 was the longest stable time step.
>
> *Powers: 7.2 (text)*

^cor-56-2

> [!proof]+ Proof
> In (8) the coefficients are $a_i = c_i = r$ and $b_i = 1 - 2r$. Their sum is $r + (1 - 2r) + r = 1$, so the second condition of [[§56★ Heat Problems#^thm-56-1|Theorem §56.1]] holds automatically. The first holds if and only if $1 - 2r \ge 0$, that is, $r \le \frac12$.

^pf-56-2

*Uses:* [[§56★ Heat Problems#^thm-56-1|§56.1]], [[§56★ Heat Problems#^def-56-1|Def. §56.1]]

> [!remark]- Connections
> - The same condition from the ODE point of view: Euler's method for $y' = \lambda y$ gives $y_{m+1} = (1 + \lambda\Delta t)y_m$, which decays only if $|1 + \lambda\Delta t| \le 1$. The semi-discrete system of Definition §56.1 has eigenvalues $\lambda_k = -\frac{4}{(\Delta x)^2}\sin^2\frac{k\pi\Delta x}{2}$, down to almost $-4/(\Delta x)^2$, and $|1 + \lambda_k\Delta t| \le 1$ for all $k$ means $\Delta t \le \frac{(\Delta x)^2}{2\cos^2(\pi\Delta x/2)}$, which tends to $\Delta t \le \frac12(\Delta x)^2$ as the mesh is refined. The fastest-decaying modes, which matter least physically, decide the step size; compare the analysis of a fixed-point iteration $u_{n+1} = g(u_n)$, stable when $|g'| < 1$, [[§12★ First-Order Difference Equations#^lem-12-5|331 Lem. §12.5]].

The time step is tied to the square of the space step: halving $\Delta x$ forces $\Delta t$ to be divided by $4$.

> [!example] Example §56.3: A Shorter Time Step
> Solve the problem of Example §56.1 ($f(x) = x$, $\Delta x = \frac14$, $u_4(0) = 1$) with $r = \frac14$, so $\Delta t = \frac1{64}$, and compare with Example §56.1 at corresponding times.
>
> Now (8) is $u_i(m + 1) = \frac14\big(u_{i-1}(m) + 2u_i(m) + u_{i+1}(m)\big)$, with all coefficients positive (stable). The first rows for $u_1, u_2, u_3$ are
>
> $$
> \big(\tfrac14, \tfrac12, \tfrac34\big), \quad \big(\tfrac14, \tfrac12, \tfrac12\big), \quad \big(\tfrac14, \tfrac7{16}, \tfrac38\big), \quad \big(\tfrac{15}{64}, \tfrac38, \tfrac{19}{64}\big), \quad \ldots \qquad (m = 1, 2, 3, 4) .
> $$
>
> Level $2m$ with $r = \frac14$ is the same time as level $m$ with $r = \frac12$. At $x = \frac14, \frac12, \frac34$:
>
> | $t$ | $r = \frac12$ | $r = \frac14$ | exact |
> |---|---|---|---|
> | $\frac2{32}$ | $0.250,\ 0.500,\ 0.250$ | $0.234,\ 0.375,\ 0.297$ | $0.217,\ 0.343,\ 0.271$ |
> | $\frac5{32}$ | $0.125,\ 0.125,\ 0.125$ | $0.102,\ 0.145,\ 0.103$ | $0.096,\ 0.136,\ 0.097$ |
>
> The shorter step is noticeably more accurate and smoother, at twice the work. What remains is mostly the error of the coarse space mesh, which a smaller $\Delta t$ alone cannot remove.
>
> *Powers: Exercise 7.2.2*

^ex-56-3

![[m341-56-2.svg]]
*(a) The series solution of Example §56.1 (blue) at $t = \frac2{32}$ and $t = \frac5{32}$, with the explicit scheme on $\Delta x = \frac14$: $r = \frac12$ (red dots) and $r = \frac14$ (green triangles). (b) With $r = 1$ (Example §56.2) the computed values alternate in sign and grow by a factor of about $2.4$ per step.*

> [!example] Example §56.4: A Convection Boundary Condition Lowers the Limit on r
> Different problems give different maximum values of $r$. Consider
>
> $$
> \frac{\partial^2u}{\partial x^2} = \frac{\partial u}{\partial t}, \quad 0 < x < 1, \ 0 < t; \qquad u(0, t) = 1, \quad \frac{\partial u}{\partial x}(1, t) + \gamma u(1, t) = 0; \qquad u(x, 0) = 0 , \qquad (10)\text{–}(12)
> $$
>
> with $\Delta x = \frac14$ ($n = 4$).
>
> **Replacement equations.** For $i = 1, 2, 3$ they are (8). Now $u_4 = u(1, t)$ is unknown. Its equation (8) at $i = 4$ contains the fictitious $u_5$; the replaced boundary condition $\frac{u_5(m) - u_3(m)}{2\Delta x} + \gamma u_4(m) = 0$ gives $u_5(m) = u_3(m) - \frac12\gamma u_4(m)$. Substituting,
>
> $$
> \begin{aligned}
> u_i(m + 1) &= ru_{i-1}(m) + (1 - 2r)u_i(m) + ru_{i+1}(m), \qquad i = 1, 2, 3, \\
> u_4(m + 1) &= 2ru_3(m) + \big(1 - 2r - \tfrac12r\gamma\big)u_4(m) .
> \end{aligned} \qquad (13)
> $$
>
> **Stability.** The sums of coefficients are $1$ and $1 - \frac12r\gamma \le 1$, so the second rule holds. The first requires
>
> $$
> 1 - 2r - \tfrac12r\gamma \ge 0 \qquad\text{or}\qquad r \le \frac{1}{2 + \frac12\gamma} . \qquad (14)
> $$
>
> **The case $\gamma = 1$.** The longest stable step is $r = \frac25$, $\Delta t = \frac25 \cdot \frac1{16} = \frac1{40}$. Then the last equation is $u_4(m + 1) = \frac45u_3(m)$, and the others are $u_i(m + 1) = \frac25u_{i-1}(m) + \frac15u_i(m) + \frac25u_{i+1}(m)$. Letting the boundary condition fix $u_0(m) = 1$ for all $m$:
>
> | $m$ | $u_0$ | $u_1$ | $u_2$ | $u_3$ | $u_4$ |
> |---|---|---|---|---|---|
> | $0$ | $1$ | $0$ | $0$ | $0$ | $0$ |
> | $1$ | $1$ | $0.4$ | $0$ | $0$ | $0$ |
> | $2$ | $1$ | $0.48$ | $0.16$ | $0$ | $0$ |
> | $3$ | $1$ | $0.56$ | $0.224$ | $0.064$ | $0$ |
> | $4$ | $1$ | $0.6016$ | $0.2944$ | $0.1024$ | $0.0512$ |
> | $5$ | $1$ | $0.6381$ | $0.3405$ | $0.1587$ | $0.0819$ |
> | $6$ | $1$ | $0.6638$ | $0.3868$ | $0.2007$ | $0.1270$ |
>
> The heat enters from the left end and spreads one mesh interval per step. As $m \to \infty$ the values approach the steady state $1, 0.875, 0.75, 0.625, 0.5$, which is the exact steady-state temperature $u = 1 - \frac12x$ ($u'' = 0$, $u(0) = 1$, $u'(1) + u(1) = 0$) at the mesh points: a linear function satisfies the replacement equations exactly.
>
> *Powers: 7.2, Example 2 and Exercise 3*

^ex-56-4
