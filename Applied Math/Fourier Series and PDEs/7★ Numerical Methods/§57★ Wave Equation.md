---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 7
section: 57
powers: "7.3"
aliases: ["Powers 7.3"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§56★ Heat Problems]] · ↑ [[· 7★ Numerical Methods]] · [[§58★ Potential Equation]] →

*Powers, Section 7.3.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

The plain vibrating string seldom needs numerical methods, since d'Alembert's solution gives $u(x, t)$ directly. But a term in $u$, a forcing term or a more complicated boundary condition can make series and d'Alembert-type solutions impractical, and then a simple finite-difference scheme is very effective. Both second derivatives are replaced by central differences. The resulting scheme needs two time levels to compute the next one, so the second initial condition supplies a special starting equation. The stability condition is now $\Delta t \le \Delta x$: in one time step the computation must reach at least as far as the wave travels. At the limit $\Delta t = \Delta x$ the scheme reproduces d'Alembert's solution exactly.

## The Scheme

The vibrating string problem of [[§29 The Vibrating String|§29]], with $c = 1$, is

$$
\frac{\partial^2u}{\partial x^2} = \frac{\partial^2u}{\partial t^2}, \quad 0 < x < 1, \ 0 < t; \qquad u(0, t) = 0, \quad u(1, t) = 0; \qquad u(x, 0) = f(x), \quad \frac{\partial u}{\partial t}(x, 0) = g(x) . \qquad (1)\text{–}(3)
$$

> [!definition] Definition §57.1: Central-Difference Scheme for the Wave Equation
> With mesh points $x_i = i\,\Delta x$ ($\Delta x = 1/n$), times $t_m = m\,\Delta t$ and $u_i(m) \cong u(x_i, t_m)$, both second derivatives are replaced by **central differences**:
>
> $$
> \frac{\partial^2u}{\partial x^2} \to \frac{u_{i+1}(m) - 2u_i(m) + u_{i-1}(m)}{(\Delta x)^2}, \qquad
> \frac{\partial^2u}{\partial t^2} \to \frac{u_i(m + 1) - 2u_i(m) + u_i(m - 1)}{(\Delta t)^2} .
> $$
>
> With $\rho = \Delta t/\Delta x$ the wave equation becomes the partial difference equation
>
> $$
> u_i(m + 1) - 2u_i(m) + u_i(m - 1) = \rho^2\big(u_{i+1}(m) - 2u_i(m) + u_{i-1}(m)\big),
> $$
>
> and solved for the new value, the **running equation**
>
> $$
> u_i(m + 1) = \rho^2u_{i-1}(m) + 2(1 - \rho^2)u_i(m) + \rho^2u_{i+1}(m) - u_i(m - 1), \qquad i = 1, \ldots, n - 1 . \qquad (4)
> $$
>
> The boundary conditions (2) carry over as $u_0(m) = 0$, $u_n(m) = 0$.
>
> *Powers: 7.3, Equation (4)*

^def-57-1

The running equation needs levels $m$ and $m - 1$ to produce level $m + 1$. For $u_i(1)$ it needs $u_{i-1}(0)$, $u_i(0)$, $u_{i+1}(0)$, which the initial condition supplies, and also $u_i(-1)$. The second initial condition has not been used yet.

> [!theorem] Proposition §57.1: The Starting Equation
> Replace the initial velocity condition $u_t(x, 0) = g(x)$ by the central difference
>
> $$
> \frac{u_i(1) - u_i(-1)}{2\,\Delta t} = g(x_i), \qquad i = 1, \ldots, n - 1 . \qquad (5)
> $$
>
> Then (4) with $m = 0$ and (5) determine the first time level:
>
> $$
> u_i(1) = \tfrac12\rho^2f(x_{i-1}) + (1 - \rho^2)f(x_i) + \tfrac12\rho^2f(x_{i+1}) + \Delta t\,g(x_i) . \qquad (7)
> $$
>
> *Powers: 7.3, Equations (5)–(7)*

^prop-57-1

> [!proof]+ Proof
> With $m = 0$ and $u_i(0) = f(x_i)$, the running equation (4) reads, after moving $u_i(-1)$ to the left, and (5) multiplied by $2\Delta t$ reads,
>
> $$
> \begin{aligned}
> u_i(1) + u_i(-1) &= \rho^2f(x_{i-1}) + 2(1 - \rho^2)f(x_i) + \rho^2f(x_{i+1}), \\
> u_i(1) - u_i(-1) &= 2\,\Delta t\,g(x_i) .
> \end{aligned} \qquad (6)
> $$
>
> Adding the two equations eliminates the fictitious value $u_i(-1)$; dividing by $2$ gives (7).

^pf-57-1

*Uses:* [[§57★ Wave Equation#^def-57-1|Def. §57.1]]

> [!remark] Remark: Method — Starting and Running Equations
> To solve a wave problem like (1)–(3) numerically:
> 1. Choose $\Delta x = 1/n$ and $\Delta t$ with $\rho = \Delta t/\Delta x \le 1$ ([[§57★ Wave Equation#^cor-57-4|Corollary §57.4]]); $\rho = 1$ is usually the most accurate.
> 2. Fill the first row of the table with the initial displacement, $u_i(0) = f(x_i)$, and the boundary columns with the boundary values.
> 3. Fill the second row with the **starting equation** (7) (or its analogue for the problem at hand: combine the running equation at $m = 0$ with the central-difference form of the velocity condition, and eliminate $u_i(-1)$).
> 4. Fill each further row with the **running equation** (4) from the two rows above.

^rem-57-1

> [!example] Example §57.1: The Plucked String
> Solve (1)–(3) with $g(x) \equiv 0$ and
>
> $$
> f(x) = \begin{cases} 2x, & 0 < x < \frac12, \\ 2(1 - x), & \frac12 < x < 1, \end{cases} \qquad (8)
> $$
>
> taking $n = 4$ and $\rho = 1$, that is, $\Delta t = \Delta x = \frac14$.
>
> With $\rho = 1$ the middle coefficient vanishes, and the running and starting equations are
>
> $$
> u_i(m + 1) = u_{i-1}(m) + u_{i+1}(m) - u_i(m - 1), \qquad u_i(1) = \tfrac12\big(f(x_{i-1}) + f(x_{i+1})\big) . \qquad (9)
> $$
>
> The first row is $f(x_i) = 0, \frac12, 1, \frac12, 0$. The starting equation gives $u_1(1) = \frac12(0 + 1) = \frac12$, $u_2(1) = \frac12(\frac12 + \frac12) = \frac12$, $u_3(1) = \frac12$. Then, for instance, $u_2(2) = u_1(1) + u_3(1) - u_2(0) = \frac12 + \frac12 - 1 = 0$. The table:
>
> | $m$ | $u_0$ | $u_1$ | $u_2$ | $u_3$ | $u_4$ |
> |---|---|---|---|---|---|
> | $0$ | $0$ | $0.5$ | $1$ | $0.5$ | $0$ |
> | $1$ | $0$ | $0.5$ | $0.5$ | $0.5$ | $0$ |
> | $2$ | $0$ | $0$ | $0$ | $0$ | $0$ |
> | $3$ | $0$ | $-0.5$ | $-0.5$ | $-0.5$ | $0$ |
> | $4$ | $0$ | $-0.5$ | $-1$ | $-0.5$ | $0$ |
> | $5$ | $0$ | $-0.5$ | $-0.5$ | $-0.5$ | $0$ |
> | $6$ | $0$ | $0$ | $0$ | $0$ | $0$ |
>
> After $8$ steps ($t = 2$, the period) the string is back in its initial position. These numbers coincide with d'Alembert's solution $u(x, t) = \frac12\big[\bar f(x - t) + \bar f(x + t)\big]$ at every mesh point; for example $u(\frac12, \frac14) = \frac12\big[f(\frac14) + f(\frac34)\big] = \frac12$. Proposition §57.2 below explains why.
>
> *Powers prints $0.5$ for $u_3(5)$ in Table 6; the running equation gives $u_3(5) = u_2(4) + u_4(4) - u_3(3) = -1 + 0 + 0.5 = -0.5$, as symmetry requires.*
>
> *Powers: 7.3, Example 1 and Table 6*

^ex-57-1

> [!theorem] Proposition §57.2: With ρ = 1 the Scheme Is Exact
> Let $f$ be continuous with $f(0) = f(1) = 0$ and $g \equiv 0$. If $\rho = 1$ ($\Delta t = \Delta x$), the numbers $u_i(m)$ computed from the starting equation (7) and the running equation (4) are exactly the values $u(x_i, t_m)$ of d'Alembert's solution of (1)–(3), for all $i$ and $m$.
>
> *Powers: 7.3 (text) and Exercise 6*

^prop-57-2

> [!proof]+ Proof
> Powers asserts this for Example §57.1 ("easy to check"); here is why it holds in general. Let $\bar f$ be the odd, $2$-periodic extension of $f$, and let $h = \Delta x = \Delta t$. By d'Alembert's formula ([[§31 d'Alembert's Solution|§31]]) the solution is $u(x, t) = \frac12\big[\bar f(x - t) + \bar f(x + t)\big]$.
>
> **Running equation.** Every function of the form $\phi(x + t) + \psi(x - t)$ satisfies the running equation with $\rho = 1$ exactly. Indeed, at $x = x_i$, $t = t_m$,
>
> $$
> u(x_i, t_m + h) + u(x_i, t_m - h) = \phi(x_i + t_m + h) + \psi(x_i - t_m - h) + \phi(x_i + t_m - h) + \psi(x_i - t_m + h),
> $$
>
> $$
> u(x_i + h, t_m) + u(x_i - h, t_m) = \phi(x_i + h + t_m) + \psi(x_i + h - t_m) + \phi(x_i - h + t_m) + \psi(x_i - h - t_m),
> $$
>
> and the right sides are the same four terms. With $\rho = 1$, (4) says precisely $u_i(m + 1) + u_i(m - 1) = u_{i+1}(m) + u_{i-1}(m)$.
>
> **Starting equation.** With $\rho = 1$, $g = 0$, (7) gives $u_i(1) = \frac12\big[f(x_{i-1}) + f(x_{i+1})\big]$, while $u(x_i, h) = \frac12\big[\bar f(x_i - h) + \bar f(x_i + h)\big]$. These agree because $\bar f = f$ on $[0, 1]$.
>
> **Boundary values.** $\bar f$ is odd and $2$-periodic, so $u(0, t) = \frac12[\bar f(-t) + \bar f(t)] = 0$ and $u(1, t) = \frac12[\bar f(1 - t) + \bar f(1 + t)] = \frac12[\bar f(1 - t) - \bar f(t - 1)] = 0$, matching $u_0(m) = u_n(m) = 0$.
>
> So the exact values and the computed values have the same rows $m = 0$ and $m = 1$, the same boundary columns, and satisfy the same recursion; by induction on $m$ they agree for all $m$.

^pf-57-2

*Uses:* [[§57★ Wave Equation#^def-57-1|Def. §57.1]], [[§57★ Wave Equation#^prop-57-1|§57.1]], [[§31 d'Alembert's Solution|§31]] (d'Alembert's formula)

> [!remark] Remark: When the Scheme Is Only Approximate
> The proof uses two special features: $\rho = 1$, and an initial velocity that is zero. With $g \ne 0$ the running equation is still exact, but the starting value $\Delta t\,g(x_i)$ only approximates the exact contribution $\frac12\int_{x_i - \Delta t}^{x_i + \Delta t}\bar g(s)\,ds$, and that error is carried along ([[§57★ Wave Equation#^ex-57-4|Example §57.4]]). With $\rho < 1$ the running equation is no longer exact either.

^rem-57-2

## Stability

> [!example] Example §57.2: A Time Step Longer Than the Space Step
> Solve the problem of Example §57.1 with $\rho^2 = (\Delta t/\Delta x)^2 = 2$. Then (4) becomes
>
> $$
> u_i(m + 1) = 2\big(u_{i-1}(m) - u_i(m) + u_{i+1}(m)\big) - u_i(m - 1),
> $$
>
> and (7), with $\frac12\rho^2 = 1$ and $1 - \rho^2 = -1$, is $u_i(1) = f(x_{i-1}) - f(x_i) + f(x_{i+1})$. The table:
>
> | $m$ | $u_0$ | $u_1$ | $u_2$ | $u_3$ | $u_4$ |
> |---|---|---|---|---|---|
> | $0$ | $0$ | $0.5$ | $1$ | $0.5$ | $0$ |
> | $1$ | $0$ | $0.5$ | $0$ | $0.5$ | $0$ |
> | $2$ | $0$ | $-1.5$ | $1$ | $-1.5$ | $0$ |
> | $3$ | $0$ | $4.5$ | $-8$ | $4.5$ | $0$ |
> | $4$ | $0$ | $-23.5$ | $33$ | $-23.5$ | $0$ |
>
> The values bear no resemblance to a vibrating string, whose displacement never exceeds $1$: the same instability as in [[§56★ Heat Problems#^ex-56-2|Example §56.2]].
>
> *Powers: 7.3, Table 7*

^ex-57-2

> [!theorem] Theorem §57.3: Rule of Thumb for Stability of the Wave Scheme
> Write the equations for the new values in terms of the $u$'s at levels $m$ and $m - 1$:
>
> $$
> u_i(m + 1) = a_iu_{i-1}(m) + b_iu_i(m) + c_iu_{i+1}(m) - u_i(m - 1)
> $$
>
> (plus terms that do not depend on the $u$'s). The computation is stable if
> 1. none of the coefficients $a_i$, $b_i$, $c_i$ is negative;
> 2. their sum is not greater than $2$: $a_i + b_i + c_i \le 2$.
>
> The coefficient $-1$ of $u_i(m - 1)$ is always there and does not enter the rules.
>
> *Powers: 7.3 (text)*

^thm-57-3

*Powers omits the proof.*

> [!remark] Remark: Why It Works
> Try $u_i(m) = \mu^m\sin(k\pi x_i)$ in (4). Since $\sin(k\pi x_{i+1}) + \sin(k\pi x_{i-1}) = 2\cos(k\pi\Delta x)\sin(k\pi x_i)$, it is a solution when
>
> $$
> \mu^2 - 2\big(1 - 2\rho^2s^2\big)\mu + 1 = 0, \qquad s = \sin\frac{k\pi\Delta x}{2} .
> $$
>
> The two roots have product $1$. If $|1 - 2\rho^2s^2| \le 1$ they are complex conjugates of absolute value $1$ (or a double root $\pm1$), and the mode oscillates without growing, like the true mode $\cos(k\pi t)$. If $1 - 2\rho^2s^2 < -1$, that is $\rho s > 1$, the roots are real and one of them is less than $-1$: the mode grows and alternates in sign. Since $s^2$ comes close to $1$ for the highest mode, no growth for any mode means $\rho \le 1$, which is what the rule gives. In Example §57.2 ($\rho^2 = 2$, $k = 3$, $s^2 \approx 0.854$) the roots are about $-4.6$ and $-0.22$, matching the growth in the table.

^rem-57-3

> [!theorem] Corollary §57.4: The Time Step Must Not Exceed the Space Step
> For the running equation (4), the rule of thumb holds if and only if
>
> $$
> \rho = \frac{\Delta t}{\Delta x} \le 1 .
> $$
>
> With wave speed $c$ (equation $c^2u_{xx} = u_{tt}$) the condition becomes $c\,\Delta t \le \Delta x$.
>
> *Powers: 7.3 (text)*

^cor-57-4

> [!proof]+ Proof
> In (4) the coefficients are $a_i = c_i = \rho^2 \ge 0$ and $b_i = 2(1 - \rho^2)$, with sum $\rho^2 + 2 - 2\rho^2 + \rho^2 = 2$. So the second condition of [[§57★ Wave Equation#^thm-57-3|Theorem §57.3]] always holds, and the first holds if and only if $1 - \rho^2 \ge 0$, that is $\rho \le 1$. For $c^2u_{xx} = u_{tt}$ the same computation goes through with $\rho = c\,\Delta t/\Delta x$ (substitute $t' = ct$).

^pf-57-4

*Uses:* [[§57★ Wave Equation#^thm-57-3|§57.3]], [[§57★ Wave Equation#^def-57-1|Def. §57.1]]

![[m341-57-1.svg]]
*The stencil of the running equation (green weights) and the meaning of $\rho \le 1$. The value at $(x_i, t_{m+1})$ (red) depends physically on the data between the characteristics through it (blue), and numerically on the data between the orange lines through $x_{i \pm 1}$. If $\Delta t \le \Delta x$ the numerical cone contains the physical one; if $\Delta t > \Delta x$, part of the information that determines the solution never reaches the computation.*

## A Forced String

> [!example] Example §57.3: Resonance
> Solve
>
> $$
> \frac{\partial^2u}{\partial x^2} = \frac{\partial^2u}{\partial t^2} - 16\cos(\pi t), \quad 0 < x < 1, \ 0 < t; \qquad u(0, t) = u(1, t) = 0; \qquad u(x, 0) = 0, \quad \frac{\partial u}{\partial t}(x, 0) = 0 . \qquad (10)\text{–}(12)
> $$
>
> **Running equation.** Replacing the derivatives as before,
>
> $$
> \frac{u_{i+1}(m) - 2u_i(m) + u_{i-1}(m)}{(\Delta x)^2} = \frac{u_i(m + 1) - 2u_i(m) + u_i(m - 1)}{(\Delta t)^2} - 16\cos(\pi t_m),
> $$
>
> $$
> u_i(m + 1) = (2 - 2\rho^2)u_i(m) + \rho^2u_{i+1}(m) + \rho^2u_{i-1}(m) - u_i(m - 1) + 16(\Delta t)^2\cos(\pi m\,\Delta t) . \qquad (13)
> $$
>
> With $\Delta x = \Delta t = \frac14$, $\rho = 1$ and $16(\Delta t)^2 = 1$:
>
> $$
> u_i(m + 1) = u_{i+1}(m) + u_{i-1}(m) - u_i(m - 1) + \cos\frac{m\pi}{4} . \qquad (14)
> $$
>
> **Starting equation.** At $m = 0$, with $u_i(0) = 0$, (14) gives $u_i(1) = -u_i(-1) + 1$; the velocity condition gives $\frac{u_i(1) - u_i(-1)}{2\Delta t} = 0$, so $u_i(1) = u_i(-1) = \frac12$ for $i = 1, 2, 3$.
>
> **Table.** With $\cos\frac\pi4 \approx 0.7071$, and so on (by symmetry $u_3 = u_1$):
>
> | $m$ | $u_1$ | $u_2$ | $u_3$ |
> |---|---|---|---|
> | $0$ | $0$ | $0$ | $0$ |
> | $1$ | $0.5$ | $0.5$ | $0.5$ |
> | $2$ | $1.2071$ | $1.7071$ | $1.2071$ |
> | $3$ | $1.2071$ | $1.9142$ | $1.2071$ |
> | $4$ | $0$ | $0$ | $0$ |
> | $5$ | $-2.2071$ | $-2.9142$ | $-2.2071$ |
> | $6$ | $-3.6213$ | $-5.1213$ | $-3.6213$ |
> | $7$ | $-2.9142$ | $-4.3284$ | $-2.9142$ |
>
> **Exact solution.** Expand the forcing in the eigenfunctions of [[§30 Solution of the Vibrating String Problem|§30]]: $16 = \sum_{n\ \mathrm{odd}}\frac{64}{n\pi}\sin(n\pi x)$. The coefficient $a_n(t)$ of $\sin(n\pi x)$ then satisfies $a_n'' + n^2\pi^2a_n = \frac{64}{n\pi}\cos(\pi t)$, $a_n(0) = a_n'(0) = 0$. For $n = 1$ the forcing frequency equals the natural frequency $\pi$ (resonance), and $a_1 = \frac{32}{\pi^2}t\sin(\pi t)$; for odd $n \ge 3$, $a_n = \frac{64}{\pi^3n(n^2 - 1)}\big(\cos\pi t - \cos n\pi t\big)$. So
>
> $$
> u(x, t) = \frac{32}{\pi^2}t\sin(\pi t)\sin(\pi x) + \frac{32}{\pi^3}\sum_{n = 3}^\infty\frac{1 - \cos(n\pi)}{n(n^2 - 1)}\big(\cos(\pi t) - \cos(n\pi t)\big)\sin(n\pi x) .
> $$
>
> At $x = \frac12$ this gives $u(\frac12, t_m) = 0.4748$, $1.6211$, $1.8178$, $0$, $-2.7675$, $-4.8634$, $-4.1105$ for $m = 1, \ldots, 7$. The middle column of the table is consistently about $5\%$ too large ($1.9142$ against $1.8178$, $-5.1213$ against $-4.8634$). The growth of $u$ is resonance in the physical system, not numerical instability: $\rho = 1$ is stable (figure below).
>
> *Powers states that at $x = \frac12$ the sum of the series is $0$, so that $u(\frac12, t) = \frac{32}{\pi^2}t\sin(\pi t)$; this holds only when $t$ is a multiple of $\frac12$ (at $t = \frac14$ the series contributes $-0.098$). The comparison above uses the full series.*
>
> *Powers: 7.3, Example 2 and Table 8*

^ex-57-3

![[m341-57-2.svg]]
*Example §57.3: the displacement of the midpoint of a string driven at its natural frequency. The computed values (red) follow the series solution (blue), about $5\%$ high; the amplitude grows linearly in $t$ because of resonance. The resonant term alone (dashed grey) is almost indistinguishable from the full solution at this scale.*

> [!example] Example §57.4: A Nonzero Initial Velocity
> Solve (1)–(3) with $f(x) \equiv 0$, $g(x) = \sin(\pi x)$, $\Delta x = \frac14$, $\rho = 1$, and compare with the exact solution $u(x, t) = \frac1\pi\sin(\pi x)\sin(\pi t)$.
>
> **Starting equation.** With $f = 0$, (7) is $u_i(1) = \Delta t\,g(x_i) = \frac14\sin(\pi x_i)$: $u_1(1) = u_3(1) = \frac{\sqrt2}{8} \approx 0.1768$, $u_2(1) = 0.25$.
>
> **Running equation** (9). For instance $u_2(2) = u_1(1) + u_3(1) - u_2(0) = \frac{\sqrt2}{4} \approx 0.3536$. At $x = \frac14, \frac12, \frac34$:
>
> | $m$ | numerical | exact |
> |---|---|---|
> | $1$ | $0.1768,\ 0.2500,\ 0.1768$ | $0.1592,\ 0.2251,\ 0.1592$ |
> | $2$ | $0.2500,\ 0.3536,\ 0.2500$ | $0.2251,\ 0.3183,\ 0.2251$ |
> | $3$ | $0.1768,\ 0.2500,\ 0.1768$ | $0.1592,\ 0.2251,\ 0.1592$ |
> | $4$ | $0,\ 0,\ 0$ | $0,\ 0,\ 0$ |
>
> and then the same values with opposite sign for $m = 5, 6, 7$, returning to $0$ at $m = 8$ ($t = 2$, the exact period). The shape and the timing are exact, but every value is too large by the same factor $\frac{\pi/4}{\sin(\pi/4)} \approx 1.111$. The reason is the starting equation: the exact value at the first step is $u(x_i, \frac14) = \frac{\sin(\pi/4)}{\pi}\sin(\pi x_i) \approx 0.2251\sin(\pi x_i)$, while (7) uses $\Delta t\,g(x_i) = 0.25\sin(\pi x_i)$. The running equation is exact for this d'Alembert-type solution (proof of Proposition §57.2), so this one error is carried along unchanged.
>
> *Powers: Exercises 7.3.3 and 7.3.4*

^ex-57-4
