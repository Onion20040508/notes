---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 7
section: 59
powers: "7.5"
aliases: ["Powers 7.5"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§58★ Potential Equation]] · ↑ [[· 7★ Numerical Methods]]

*Powers, Section 7.5.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

Separation of variables solves two-dimensional heat and wave problems only on the nicest regions, but the explicit schemes of [[§56★ Heat Problems|§56]] and [[§57★ Wave Equation|§57]] carry over directly to any region that fits on graph paper. Replace the Laplacian by the five-point approximation of [[§58★ Potential Equation|§58]] and the time derivative as in one dimension; boundary values, including time-dependent ones, enter as known numbers. The stability conditions become stricter, because each point now has four neighbours: $\Delta t \le \frac14(\Delta x)^2$ for heat, $\Delta t \le \Delta x/\sqrt2$ for waves. The examples are a cooling rectangular plate, an L-shaped plate whose edges are heated, and a vibrating square membrane.

On a square mesh, $\Delta x = \Delta y$, position is denoted by one or two subscripts and the time level by an index in parentheses. The Laplacian is replaced as in [[§58★ Potential Equation#^def-58-1|Definition §58.1]]:

$$
\frac{\partial^2u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} \to \frac{u_N(m) + u_S(m) + u_E(m) + u_W(m) - 4u_i(m)}{(\Delta x)^2} , \qquad (1)
$$

where $N$, $S$, $E$, $W$ are the indices of the four mesh points adjacent to point $i$.

## Heat Problems

> [!definition] Definition §59.1: Explicit Scheme for the Two-Dimensional Heat Equation
> For $\nabla^2u = u_t$, replacing the Laplacian by (1) and $u_t$ by a forward difference gives the replacement equation
>
> $$
> \frac{u_N(m) + u_S(m) + u_E(m) + u_W(m) - 4u_i(m)}{(\Delta x)^2} = \frac{u_i(m + 1) - u_i(m)}{\Delta t} , \qquad (7)
> $$
>
> and, solved for the new value,
>
> $$
> u_i(m + 1) = r\big[u_N(m) + u_S(m) + u_E(m) + u_W(m)\big] + (1 - 4r)\,u_i(m), \qquad r = \frac{\Delta t}{(\Delta x)^2} = \frac{\Delta t}{(\Delta y)^2} . \qquad (8)
> $$
>
> At a point next to the boundary, the boundary neighbours contribute their known values.
>
> *Powers: 7.5, Equations (1), (7), (8)*

^def-59-1

> [!theorem] Corollary §59.1: The Stability Condition r ≤ 1/4
> The rules of thumb of [[§56★ Heat Problems#^thm-56-1|Theorem §56.1]] (no negative coefficient, sum of coefficients at most $1$) hold for (8) if and only if
>
> $$
> r = \frac{\Delta t}{(\Delta x)^2} \le \frac14 .
> $$
>
> *Powers: 7.5 (text)*

^cor-59-1

> [!proof]+ Proof
> The coefficients in (8) are $r$ (four times) and $1 - 4r$, with sum $4r + 1 - 4r = 1$. So the second rule always holds, and the first holds if and only if $1 - 4r \ge 0$.

^pf-59-1

*Uses:* [[§56★ Heat Problems#^thm-56-1|§56.1]], [[§59★ Two-Dimensional Problems#^def-59-1|Def. §59.1]]

> [!remark]- Connections
> - As in one dimension, (8) is Euler's method ([[§10 Numerical Approximations꞉ Euler's Method#^def-10-1|331 Def. §10.1]]) for the system of ODEs obtained by discretizing only in space. Its eigenvalues are $-\frac{4}{(\Delta x)^2}\big(\sin^2\frac{j\pi\Delta x}{2a} + \sin^2\frac{k\pi\Delta y}{2b}\big)$ on an $a \times b$ rectangle, reaching almost $-8/(\Delta x)^2$, twice as far as in one dimension; Euler's condition $|1 + \lambda\Delta t| \le 1$ therefore halves the admissible step, from $\frac12(\Delta x)^2$ to $\frac14(\Delta x)^2$.

> [!remark] Remark: Method — Explicit Schemes on a Graph-Paper Region
> 1. Lay a square mesh over the region, number the interior points, and note which neighbours of each point are boundary points.
> 2. Choose the largest stable time step: $r = \frac14$ for heat (Corollary §59.1), $\rho^2 = \frac12$ for waves ([[§59★ Two-Dimensional Problems#^cor-59-2|Corollary §59.2]]). Both choices remove the $u_i(m)$ term and simplify the arithmetic.
> 3. Write the update (8), or for waves the starting and running equations ([[§59★ Two-Dimensional Problems#^prop-59-3|Proposition §59.3]], (20)), at each interior point, with boundary values inserted. If initial and boundary values disagree at boundary points at $t = 0$, let the boundary condition override.
> 4. Use the symmetries of the region and the data to reduce the number of values that must be computed.
> 5. Fill in the table level by level.

^rem-59-1

> [!example] Example §59.1: A Cooling Rectangular Plate
> Solve
>
> $$
> \nabla^2u = \frac{\partial u}{\partial t}, \quad 0 < x < 1.25, \ 0 < y < 1, \ 0 < t; \qquad u = 0 \ \text{on all four sides}; \qquad u(x, y, 0) = 1 \qquad (2)\text{–}(5)
> $$
>
> with $\Delta x = \Delta y = \frac14$.
>
> **Mesh.** The interior points are $x = \frac14, \frac12, \frac34, 1$ and $y = \frac14, \frac12, \frac34$, numbered $1$–$4$ on $y = \frac14$, $5$–$8$ on $y = \frac12$, $9$–$12$ on $y = \frac34$; so $u_1(m) \cong u(\frac14, \frac14, t_m)$, $u_2(m) \cong u(\frac12, \frac14, t_m)$, and so on (6).
>
> **Time step.** $r = \Delta t/(\Delta x)^2 = 16\,\Delta t$, and Corollary §59.1 requires $\Delta t \le \frac1{64}$. Take the longest stable step, $\Delta t = \frac1{64}$, $r = \frac14$: then $u_i(m + 1) = \frac14\big[u_N + u_S + u_E + u_W\big](m)$.
>
> **Symmetry.** The plate is symmetric about $x = 0.625$ and $y = \frac12$, so $u_1 = u_4 = u_9 = u_{12}$, $u_2 = u_3 = u_{10} = u_{11}$, $u_5 = u_8$, $u_6 = u_7$, and only $u_1, u_2, u_5, u_6$ need to be computed:
>
> $$
> u_1' = \tfrac14(u_2 + u_5), \qquad u_2' = \tfrac14(u_1 + u_2 + u_6), \qquad u_5' = \tfrac14(2u_1 + u_6), \qquad u_6' = \tfrac14(2u_2 + u_5 + u_6),
> $$
>
> where $'$ means the next level and boundary neighbours contribute $0$. For example, from $m = 1$ to $m = 2$: $u_6(2) = \frac14\big(2\cdot\frac34 + \frac34 + 1\big) = \frac{13}{16}$.
>
> | $m$ | $u_1$ | $u_2$ | $u_5$ | $u_6$ |
> |---|---|---|---|---|
> | $0$ | $1$ | $1$ | $1$ | $1$ |
> | $1$ | $\frac12$ | $\frac34$ | $\frac34$ | $1$ |
> | $2$ | $\frac38$ | $\frac9{16}$ | $\frac12$ | $\frac{13}{16}$ |
> | $3$ | $\frac{17}{64}$ | $\frac7{16}$ | $\frac{25}{64}$ | $\frac{39}{64}$ |
> | $4$ | $\frac{53}{256}$ | $\frac{21}{64}$ | $\frac{73}{256}$ | $\frac{15}{32}$ |
>
> **Comparison.** By [[§43 Two-Dimensional Heat Equation꞉ Solution#^thm-43-4|Theorem §43.4]], the exact solution is
>
> $$
> u(x, y, t) = \sum_{j, k\ \mathrm{odd}}\frac{16}{\pi^2jk}\sin\frac{j\pi x}{1.25}\sin(k\pi y)\exp\Big(-\pi^2\Big(\frac{j^2}{1.25^2} + k^2\Big)t\Big) .
> $$
>
> At the four points, at $t = \frac2{64}$ it gives $0.464$, $0.647$, $0.621$, $0.865$ (computed: $0.375$, $0.563$, $0.500$, $0.813$), and at $t = \frac3{64}$ it gives $0.334$, $0.505$, $0.465$, $0.702$ (computed: $0.266$, $0.438$, $0.391$, $0.609$). The coarse mesh cools too fast, mostly because the discontinuity between the initial value $1$ and the boundary value $0$ is smeared over a whole mesh interval; with $\Delta x = \frac18$ the computed values follow the series closely (figure below).
>
> *Powers' text takes the boundary values equal to $1$ at $m = 0$, which makes all $u_i(1) = 1$ and shifts everything one step later; his Table 9, reproduced here, lets the boundary value $0$ override from $m = 0$ on.*
>
> *Powers: 7.5, Example 1 and Table 9*

^ex-59-1

![[m341-59-2.svg]]
*Example §59.1 at the point $(\frac12, \frac12)$: the series solution (blue), the explicit scheme with $\Delta x = \frac14$, $\Delta t = \frac1{64}$ (red, the column $u_6$ of the table), and with $\Delta x = \frac18$, $\Delta t = \frac1{256}$ (green, every second step shown). Halving the mesh removes most of the error.*

> [!example] Example §59.2: An L-Shaped Plate with Rising Edge Temperature
> Solve a problem that separation of variables cannot handle:
>
> $$
> \nabla^2u = \frac{\partial u}{\partial t} \ \text{ in } R, \qquad u = f(t) = t \ \text{ on the boundary } C \text{ of } R, \qquad u = 0 \ \text{ in } R \text{ at } t = 0 , \qquad (9)\text{–}(11)
> $$
>
> where $R$ is the L-shaped region $[0, 1] \times [0, \frac35] \cup [\frac25, 1] \times [\frac35, 1]$.
>
> **Mesh.** Take $\Delta x = \Delta y = \frac15$. The interior points are $1$–$4$ on $y = \frac15$ ($x = \frac15, \ldots, \frac45$), $5$–$8$ on $y = \frac25$, $9, 10$ on $y = \frac35$ and $11, 12$ on $y = \frac45$ (both at $x = \frac35, \frac45$).
>
> **Time step.** $r = 25\,\Delta t$, so the longest stable step is $\Delta t = \frac1{100}$, $r = \frac14$, and
>
> $$
> u_i(m + 1) = \tfrac14\big(u_N(m) + u_S(m) + u_E(m) + u_W(m)\big) , \qquad (12)
> $$
>
> where every boundary neighbour contributes $f(t_m) = t_m = \frac{m}{100}$. Point $1$ has two boundary neighbours and point $2$ one: $u_1(m + 1) = \frac14\big(u_2(m) + u_5(m) + 2f(t_m)\big)$, $u_2(m + 1) = \frac14\big(u_1(m) + u_3(m) + u_6(m) + f(t_m)\big)$, and so on.
>
> **Symmetry.** The region is symmetric about the line $x + y = 1$ through points $4$ and $7$, which exchanges $1 \leftrightarrow 12$, $2 \leftrightarrow 10$, $3 \leftrightarrow 8$, $5 \leftrightarrow 11$, $6 \leftrightarrow 9$. So only $u_1, \ldots, u_7$ are computed; with $u_8 = u_3$ and $u_9 = u_6$ the remaining equations are
>
> $$
> \begin{aligned}
> u_3' &= \tfrac14(u_2 + u_4 + u_7 + f), & u_4' &= \tfrac14(2u_3 + 2f), & u_5' &= \tfrac14(u_1 + u_6 + 2f), \\
> u_6' &= \tfrac14(u_2 + u_5 + u_7 + f), & u_7' &= \tfrac14(2u_3 + 2u_6) .
> \end{aligned}
> $$
>
> **Table** (entries are $100 \times u_i(m)$):
>
> | $m$ | $u_1$ | $u_2$ | $u_3$ | $u_4$ | $u_5$ | $u_6$ | $u_7$ | $100f(t_m)$ |
> |---|---|---|---|---|---|---|---|---|
> | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ |
> | $1$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $1$ |
> | $2$ | $0.50$ | $0.25$ | $0.25$ | $0.50$ | $0.50$ | $0.25$ | $0$ | $2$ |
> | $3$ | $1.19$ | $0.75$ | $0.69$ | $1.13$ | $1.19$ | $0.69$ | $0.25$ | $3$ |
> | $4$ | $1.98$ | $1.39$ | $1.28$ | $1.84$ | $1.97$ | $1.30$ | $0.69$ | $4$ |
>
> For example $u_4(3) = \frac14\big(2 \cdot 0.25 + 2 \cdot 2\big) = 1.125$ and $u_3(4) = \frac14(0.75 + 1.125 + 0.25 + 3) = 1.281$. Points with more boundary neighbours warm first; point $7$, farthest inside, lags most. Continued further, the interior temperatures settle into rising with the boundary at a fixed lag: at $m = 60$ (boundary $0.60$) they are between $0.553$ and $0.575$.
>
> *Powers' Table 10 has $1.22$, $0.75$, $1.22$ for $u_1$, $u_4$, $u_5$ at $m = 3$; the scheme gives $1.19$, $1.13$, $1.19$, and these slips carry into his row $m = 4$ ($1.99$, $1.40$, $1.19$, $1.98$ for $u_1$, $u_2$, $u_3$, $u_5$).*
>
> *Powers: 7.5, Example 2 and Table 10*

^ex-59-2

## Wave Problems

> [!definition] Definition §59.2: Explicit Scheme for the Two-Dimensional Wave Equation
> For $\nabla^2u = u_{tt}$, replace the Laplacian by (1) and the time derivative by the central difference
>
> $$
> \frac{\partial^2u}{\partial t^2} \to \frac{u_i(m + 1) - 2u_i(m) + u_i(m - 1)}{(\Delta t)^2} . \qquad (13)
> $$
>
> The replacement equation
>
> $$
> \frac{u_i(m + 1) - 2u_i(m) + u_i(m - 1)}{(\Delta t)^2} = \frac{u_N(m) + u_S(m) + u_E(m) + u_W(m) - 4u_i(m)}{(\Delta x)^2} , \qquad (19)
> $$
>
> solved for the new value with $\rho = \Delta t/\Delta x$, is the **running equation**
>
> $$
> u_i(m + 1) = \rho^2\big[u_E(m) + u_W(m) + u_N(m) + u_S(m)\big] + (2 - 4\rho^2)\,u_i(m) - u_i(m - 1) . \qquad (20)
> $$
>
> *Powers: 7.5, Equations (13), (19), (20)*

^def-59-2

> [!theorem] Corollary §59.2: The Stability Condition ρ² ≤ 1/2
> The rules of thumb of [[§57★ Wave Equation#^thm-57-3|Theorem §57.3]] (no negative coefficient among those of the level-$m$ values, sum at most $2$) hold for (20) if and only if
>
> $$
> \rho^2 = \Big(\frac{\Delta t}{\Delta x}\Big)^2 \le \frac12 , \qquad\text{that is,}\qquad \Delta t \le \frac{\Delta x}{\sqrt2} .
> $$
>
> *Powers: 7.5 (text)*

^cor-59-2

> [!proof]+ Proof
> The coefficients of the level-$m$ values in (20) are $\rho^2$ (four times) and $2 - 4\rho^2$, with sum $2$. So the second rule always holds, and the first holds if and only if $2 - 4\rho^2 \ge 0$, that is, $\rho^2 \le \frac12$.

^pf-59-2

*Uses:* [[§57★ Wave Equation#^thm-57-3|§57.3]], [[§59★ Two-Dimensional Problems#^def-59-2|Def. §59.2]]

> [!theorem] Proposition §59.3: The Starting Equation in Two Dimensions
> For initial conditions $u(x, y, 0) = f(x, y)$, $u_t(x, y, 0) = g(x, y)$, replace the velocity condition by $\frac{u_i(1) - u_i(-1)}{2\Delta t} = g_i$. Together with (20) at $m = 0$ this gives
>
> $$
> u_i(1) = \tfrac12\rho^2\big[u_E(0) + u_W(0) + u_N(0) + u_S(0)\big] + (1 - 2\rho^2)\,u_i(0) + \Delta t\,g_i ;
> $$
>
> in particular, for $\rho^2 = \frac12$,
>
> $$
> u_i(1) = \tfrac14\big[u_E(0) + u_W(0) + u_N(0) + u_S(0)\big] + \Delta t\,g_i ,
> $$
>
> where $u_i(0) = f_i$ and the right side contains known values only.
>
> *Powers: 7.5, Equations (22)–(23)*

^prop-59-3

> [!proof]+ Proof
> At $m = 0$, (20) and the replaced velocity condition read
>
> $$
> u_i(1) + u_i(-1) = \rho^2\big[u_E(0) + u_W(0) + u_N(0) + u_S(0)\big] + (2 - 4\rho^2)u_i(0), \qquad u_i(1) - u_i(-1) = 2\,\Delta t\,g_i . \qquad (22),\ (23)
> $$
>
> Adding eliminates $u_i(-1)$; divide by $2$. For $\rho^2 = \frac12$ the coefficient $1 - 2\rho^2$ vanishes. This is the two-dimensional version of [[§57★ Wave Equation#^prop-57-1|Proposition §57.1]].

^pf-59-3

*Uses:* [[§59★ Two-Dimensional Problems#^def-59-2|Def. §59.2]]

> [!example] Example §59.3: A Square Membrane Plucked Near a Corner
> Solve
>
> $$
> \nabla^2u = \frac{\partial^2u}{\partial t^2}, \quad 0 < x < 1, \ 0 < y < 1, \ 0 < t; \qquad u = 0 \ \text{on the four sides}; \qquad u(x, y, 0) = f(x, y), \quad \frac{\partial u}{\partial t}(x, y, 0) = g(x, y) \qquad (14)\text{–}(18)
> $$
>
> with $\Delta x = \Delta y = \frac14$, $\rho^2 = \frac12$ (that is, $\Delta t = \frac1{4\sqrt2}$), $g \equiv 0$, and $f = 1$ at the mesh point $(\frac14, \frac14)$, $f = 0$ at the other mesh points.
>
> **Equations.** With the numbering of [[§58★ Potential Equation#^ex-58-1|Example §58.1]] ($u_1$ at $(\frac14, \frac14)$, …, $u_9$ at $(\frac34, \frac34)$), the running equation (20) with $\rho^2 = \frac12$ is
>
> $$
> u_i(m + 1) = \tfrac12\big[u_E(m) + u_W(m) + u_N(m) + u_S(m)\big] - u_i(m - 1) , \qquad (21)
> $$
>
> and since $g = 0$ the starting equation is $u_i(1) = \frac14\big[u_E(0) + u_W(0) + u_N(0) + u_S(0)\big]$.
>
> **Computation.** At $m = 1$ only the neighbours of point $1$ move: $u_2(1) = u_4(1) = \frac14$. At $m = 2$: $u_1(2) = \frac12(\frac14 + \frac14) - 1 = -\frac34$, $u_5(2) = \frac12(\frac14 + \frac14) = \frac14$, $u_3(2) = u_7(2) = \frac12\cdot\frac14 = \frac18$. The problem is symmetric about the diagonal $y = x$, so $u_2 = u_4$, $u_3 = u_7$, $u_6 = u_8$. In units of $\frac1{64}$:
>
> | $m$ | $u_1$ | $u_2 = u_4$ | $u_3 = u_7$ | $u_5$ | $u_6 = u_8$ | $u_9$ |
> |---|---|---|---|---|---|---|
> | $0$ | $64$ | $0$ | $0$ | $0$ | $0$ | $0$ |
> | $1$ | $0$ | $16$ | $0$ | $0$ | $0$ | $0$ |
> | $2$ | $-48$ | $0$ | $8$ | $16$ | $0$ | $0$ |
> | $3$ | $0$ | $-28$ | $0$ | $0$ | $12$ | $0$ |
> | $4$ | $20$ | $0$ | $-16$ | $-32$ | $0$ | $12$ |
> | $5$ | $0$ | $14$ | $0$ | $0$ | $-30$ | $0$ |
> | $6$ | $-6$ | $0$ | $8$ | $16$ | $0$ | $-42$ |
> | $7$ | $0$ | $-5$ | $0$ | $0$ | $21$ | $0$ |
> | $8$ | $1$ | $0$ | $0$ | $0$ | $0$ | $63$ |
>
> Two features stand out. The values form a checkerboard: at even levels only the points $1, 3, 5, 7, 9$ are nonzero, at odd levels only $2, 4, 6, 8$, because with $\rho^2 = \frac12$ the coefficient of $u_i(m)$ in (21) is zero, so the two families of points never mix. And after eight steps the displacement has moved almost entirely to the opposite corner ($\frac{63}{64}$ at $(\frac34, \frac34)$, $\frac1{64}$ left at the start).
>
> *Powers: 7.5, Example 3 and Figure 8*

^ex-59-3

![[m341-59-1.svg]]
*Example §59.3: the square membrane on a $\frac14$-mesh at time levels $m = 0, 2, 4, 8$, with values in units of $\frac1{64}$ (red discs upward, blue downward, area proportional to the size). The initial bump near $(\frac14, \frac14)$ spreads, reflects from the fixed edges, and after eight steps reappears almost intact at the opposite corner.*

> [!example] Example §59.4: A Membrane Struck in the Middle
> Solve (14)–(18) with $\Delta x = \Delta y = \frac14$, $\rho^2 = \frac12$, $f \equiv 0$, and $g = 4\sqrt2$ at the center $(\frac12, \frac12)$, $g = 0$ at the other mesh points.
>
> **Starting equation.** With $f = 0$, Proposition §59.3 gives $u_i(1) = \Delta t\,g_i$. Since $\Delta t = \frac1{4\sqrt2}$, this is $u_5(1) = 1$ at the center and $0$ elsewhere.
>
> **Running equation** (21). Writing (corners, edge midpoints, center) $= (u_1 = u_3 = u_7 = u_9,\ u_2 = u_4 = u_6 = u_8,\ u_5)$ by the symmetry of the square:
>
> | $m$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ |
> |---|---|---|---|---|---|---|---|---|---|---|
> | corners | $0$ | $0$ | $0$ | $\frac12$ | $0$ | $-\frac12$ | $0$ | $0$ | $0$ | $0$ |
> | edges | $0$ | $0$ | $\frac12$ | $0$ | $0$ | $0$ | $-\frac12$ | $0$ | $0$ | $0$ |
> | center | $0$ | $1$ | $0$ | $0$ | $0$ | $0$ | $0$ | $-1$ | $0$ | $1$ |
>
> For instance $u_1(3) = \frac12\big(u_2(2) + u_4(2)\big) - u_1(1) = \frac12$ and $u_5(3) = \frac12 \cdot 4 \cdot u_2(2) - u_5(1) = 1 - 1 = 0$. The pulse runs from the center to the edges and the corners, and returns inverted; the computed motion is exactly periodic with period $8\,\Delta t = \sqrt2$. That is the period $2\pi/(\sqrt2\,\pi)$ of the fundamental mode $\sin(\pi x)\sin(\pi y)\cos(\sqrt2\,\pi t)$ of the square membrane (substitute in $\nabla^2u = u_{tt}$; compare [[§43 Two-Dimensional Heat Equation꞉ Solution#^rem-43-3|§43]], Remark: The Rectangular Membrane).
>
> *Powers: Exercise 7.5.7*

^ex-59-4
