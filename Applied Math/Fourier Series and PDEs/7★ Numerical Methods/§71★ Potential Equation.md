---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 7
section: "71★"
powers: "7.4"
aliases: ["Powers 7.4"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§70★ Wave Equation]] · ↑ [[· 7★ Numerical Methods]] · [[§72★ Two-Dimensional Problems]] →

*Powers, Section 7.4.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

For the potential equation $\nabla^2u = 0$ and its relatives in a plane region, the Laplacian is replaced by the five-point approximation on a square mesh. Each interior mesh point then gives one linear equation, and together they form a system with one unknown per point; there is no time variable and no stability condition. Separation of variables needs a rectangle, but the mesh method works on any region that fits on graph paper, such as L-shapes and T-shapes. The replacement equation says that each value is the average of its four neighbours, a discrete form of the mean-value property of harmonic functions. For fine meshes the systems become large, and they are solved by iteration (Gauss–Seidel). Physically these are steady-state temperatures, electrostatic potentials, and the deflection of a loaded membrane.

## The Five-Point Approximation

Consider a region $R$ of the $xy$-plane whose boundary can be made to coincide with the lines of a sheet of graph paper with square divisions: rectangles, L's and T's, but not circles or triangles. The graph paper provides a mesh of points in $R$ and on its boundary. The points are numbered in some fashion, usually left to right and bottom to top.

> [!definition] Definition §71.1: Five-Point Approximation to the Laplacian
> At a mesh point $i$ with neighbours $E$, $W$ (right and left) and $N$, $S$ (above and below), the Laplacian is replaced by
>
> $$
> \frac{\partial^2u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} \to \frac{u_W - 2u_i + u_E}{(\Delta x)^2} + \frac{u_N - 2u_i + u_S}{(\Delta y)^2} , \qquad (1)
> $$
>
> the **five-point approximation to the Laplacian**. On a square mesh, $\Delta x = \Delta y$, it simplifies to
>
> $$
> \frac{\partial^2u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} \to \frac{u_N + u_S + u_E + u_W - 4u_i}{(\Delta x)^2} . \qquad (2)
> $$
>
> *Powers: 7.4, Equations (1)–(2) and Figure 1*

^def-71-1

> [!remark]- Connections
> - The Laplacian $\nabla^2u = u_{xx} + u_{yy}$ of a $C^2$ function: [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-28-3|452 Def. §28.3]]. Each of the two second differences in (1) approximates its partial derivative with error $\frac{(\Delta x)^2}{12}u_{xxxx}$, resp. $\frac{(\Delta y)^2}{12}u_{yyyy}$, at some nearby point, by [[§68★ Boundary Value Problems#^prop-68-1|Proposition §68.1]] applied along the lines $y =$ const and $x =$ const.

> [!remark] Remark: Method — Replacement Equations for a Potential Problem
> 1. Lay a square mesh with spacing $\Delta x$ over the region; number the interior mesh points (left to right, bottom to top) and write the given boundary values at the boundary mesh points.
> 2. At each interior point write (2), with the right side of the equation evaluated at that point; boundary neighbours contribute known numbers.
> 3. Look for symmetries of the region and the data; points that correspond under a symmetry have equal values, which reduces the number of unknowns.
> 4. Solve the linear system: by elimination for a few unknowns, iteratively (Definition §71.2) for many.

^rem-71-1

> [!example] Example §71.1: The Square with Tent-Shaped Boundary Values
> Solve numerically
>
> $$
> \frac{\partial^2u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} = 0, \quad 0 < x < 1, \ 0 < y < 1; \qquad u(0, y) = u(1, y) = 0; \qquad u(x, 0) = u(x, 1) = f(x), \qquad (3)\text{–}(5)
> $$
>
> $$
> f(x) = \begin{cases} 2x, & 0 < x < \frac12, \\ 2(1 - x), & \frac12 \le x < 1, \end{cases} \qquad (6)
> $$
>
> with $\Delta x = \Delta y = \frac14$ and the numbering of the figure below: $u_1, u_2, u_3$ on $y = \frac14$, $u_4, u_5, u_6$ on $y = \frac12$, $u_7, u_8, u_9$ on $y = \frac34$. The boundary values are $f(\frac14) = \frac12$, $f(\frac12) = 1$, $f(\frac34) = \frac12$ on the top and bottom, and $0$ on the sides.
>
> **Equations.** At each of the nine points, $u_N + u_S + u_E + u_W - 4u_i = 0$ (7):
>
> $$
> \begin{aligned}
> u_2 + u_4 + \tfrac12 - 4u_1 &= 0, & u_1 + u_3 + u_5 + 1 - 4u_2 &= 0, & u_2 + u_6 + \tfrac12 - 4u_3 &= 0, \\
> u_1 + u_5 + u_7 - 4u_4 &= 0, & u_2 + u_4 + u_6 + u_8 - 4u_5 &= 0, & u_3 + u_5 + u_9 - 4u_6 &= 0, \\
> u_4 + u_8 + \tfrac12 - 4u_7 &= 0, & u_5 + u_7 + u_9 + 1 - 4u_8 &= 0, & u_6 + u_8 + \tfrac12 - 4u_9 &= 0 .
> \end{aligned} \qquad (8)
> $$
>
> **Symmetry.** The problem is symmetric about $x = \frac12$ and about $y = \frac12$, so $u_1 = u_3 = u_7 = u_9 = a$, $u_2 = u_8 = b$, $u_4 = u_6 = c$, $u_5 = d$, and (8) reduces to
>
> $$
> b + c + \tfrac12 - 4a = 0, \qquad 2a + d + 1 - 4b = 0, \qquad 2a + d - 4c = 0, \qquad 2b + 2c - 4d = 0 .
> $$
>
> The last gives $d = \frac12(b + c)$, and the first $b + c = 4a - \frac12$, so $d = 2a - \frac14$. Then the second gives $b = a + \frac3{16}$ and the third $c = a - \frac1{16}$. Substituting in $b + c = 4a - \frac12$: $2a + \frac18 = 4a - \frac12$, so
>
> $$
> a = \tfrac5{16}, \qquad b = \tfrac12, \qquad c = \tfrac14, \qquad d = \tfrac38 .
> $$
>
> **Comparison.** The exact solution is that of [[§45 Potential in a Rectangle#^thm-45-1|Theorem §45.1]] (two nonzero sides) with the same data $f$ on the bottom and top, written symmetrically:
>
> $$
> u(x, y) = \sum_{n = 1}^\infty b_n\sin(n\pi x)\,\frac{\sinh(n\pi(1 - y)) + \sinh(n\pi y)}{\sinh(n\pi)}, \qquad b_n = 2\int_0^1f(x)\sin(n\pi x)\,dx = \frac{8\sin(n\pi/2)}{n^2\pi^2} .
> $$
>
> | point | $(\frac14, \frac14)$ | $(\frac12, \frac14)$ | $(\frac14, \frac12)$ | $(\frac12, \frac12)$ |
> |---|---|---|---|---|
> | $\Delta x = \frac14$ | $0.3125$ | $0.5000$ | $0.2500$ | $0.3750$ |
> | $\Delta x = \frac18$ | $0.3006$ | $0.4540$ | $0.2335$ | $0.3364$ |
> | $\Delta x = \frac1{16}$ | $0.2972$ | $0.4412$ | $0.2288$ | $0.3275$ |
> | exact | $0.2961$ | $0.4372$ | $0.2273$ | $0.3247$ |
>
> At the center the error is $0.050$, $0.012$, $0.003$: halving the mesh divides it by about $4$, as for the boundary value problems of [[§68★ Boundary Value Problems#^ex-68-3|Example §68.3]].
>
> *Powers: 7.4, Example 1 and Figures 2–3*

^ex-71-1

![[m341-58-1.svg]]
*(a) The five-point stencil (2): the Laplacian at point $i$ (red) is approximated from its four neighbours (blue). (b) Example §71.1: the numbering of the nine interior points (grey), the boundary values (blue) and the solution of the replacement equations (red). Each red value is the average of its four neighbours.*

![[m341-58-2.svg]]
*Example §58.1 along the lines $y = \frac14$ and $y = \frac12$: the series solution (blue), the mesh solution with $\Delta x = \frac14$ (red) and with $\Delta x = \frac18$ (green). The largest error, at the peak of the boundary data, falls by a factor of about $4$ when the mesh is halved.*

> [!remark] Remark: A Discrete Mean-Value Property
> With zero right side, the replacement equation (7) says $u_i = \frac14(u_N + u_S + u_E + u_W)$: each value is the average of its four neighbours, a discrete analogue of the mean-value property of harmonic functions ([[§49 The Poisson Integral Formula and the Mean Value Property#^thm-49-2|Theorem §49.2]]). It has the same consequence: an interior value cannot be larger than all of its neighbours, so the largest and smallest values of the mesh solution occur on the boundary (a discrete maximum principle; compare [[§49 The Poisson Integral Formula and the Mean Value Property#^thm-49-3|Theorem §49.3]]). In Example §71.1 all values lie between $0$ and $1$, the extremes of the boundary data. This also shows that the system has only one solution: the difference of two solutions has zero boundary values, so its maximum and minimum are both $0$.

^rem-71-2

> [!example] Example §71.2: An Equation with a Term in u
> Set up and solve the replacement equations for
>
> $$
> \frac{\partial^2u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} = 16(u - 1), \quad 0 < x < 1, \ 0 < y < 1; \qquad u = 0 \text{ on all four sides}, \qquad (9)\text{–}(11)
> $$
>
> with $\Delta x = \frac14$ and the numbering of Example §71.1.
>
> **Equations.** At each mesh point
>
> $$
> \frac{u_N + u_S + u_E + u_W - 4u_i}{(\Delta x)^2} = 16(u_i - 1) . \qquad (12)
> $$
>
> Since $(1/\Delta x)^2 = 16$ this becomes $u_N + u_S + u_E + u_W - 4u_i = u_i - 1$, or
>
> $$
> u_N + u_S + u_E + u_W - 5u_i = -1 . \qquad (13)
> $$
>
> The first four equations are $u_2 + u_4 - 5u_1 = -1$, $u_1 + u_3 + u_5 - 5u_2 = -1$, $u_2 + u_6 - 5u_3 = -1$, $u_1 + u_5 + u_7 - 5u_4 = -1$ (14), and the other five are similar.
>
> **Solution.** Now the problem is symmetric under all the symmetries of the square, so the corners have one value $a = u_1 = u_3 = u_7 = u_9$, the edge midpoints one value $b = u_2 = u_4 = u_6 = u_8$, and the center $d = u_5$:
>
> $$
> 2b - 5a = -1, \qquad 2a + d - 5b = -1, \qquad 4b - 5d = -1 .
> $$
>
> From the first and third, $a = \frac{1 + 2b}{5}$ and $d = \frac{1 + 4b}{5}$; then the second gives $\frac{2 + 4b + 1 + 4b}{5} - 5b = -1$, so $3 + 8b - 25b = -5$ and $b = \frac8{17}$. Hence
>
> $$
> a = \tfrac{33}{85} \approx 0.388, \qquad b = \tfrac8{17} \approx 0.471, \qquad d = \tfrac{49}{85} \approx 0.576 .
> $$
>
> For comparison, the exact solution, from the double sine series $u = \sum_{m, n\ \mathrm{odd}}\frac{256}{mn\pi^2\left((m^2 + n^2)\pi^2 + 16\right)}\sin(m\pi x)\sin(n\pi y)$, has the values $0.419$, $0.502$, $0.612$ at these points. Physically $u$ is a steady temperature in a plate that exchanges heat with surroundings at temperature $1$ while its edges are held at $0$.
>
> *Powers: 7.4, Example 2 (Powers sets up the equations and leaves the solution as an exercise)*

^ex-71-2

On more complicated regions the replacement for the Laplacian has exactly the same form, since the mesh is still the graph-paper mesh; only the system of equations is less regular.

> [!example] Example §71.3: An L-Shaped Region
> Solve
>
> $$
> \frac{\partial^2u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} = -16 \ \text{ in } R, \qquad u = 0 \ \text{ on the boundary of } R, \qquad (15),\ (16)
> $$
>
> where $R$ is the $1 \times 1$ square with the $\frac14 \times \frac14$ square at its upper right corner removed. Take $\Delta x = \frac14$.
>
> **Mesh.** The interior points are those of Example §71.1 except $(\frac34, \frac34)$, which is now a corner of the boundary. Number them $u_1, u_2, u_3$ on $y = \frac14$, $u_4, u_5, u_6$ on $y = \frac12$, $u_7, u_8$ on $y = \frac34$. Since $(\Delta x)^2 \cdot (-16) = -1$, the general replacement equation is
>
> $$
> u_N + u_S + u_E + u_W - 4u_i = -1 , \qquad (17)
> $$
>
> and the eight equations are
>
> $$
> \begin{aligned}
> u_2 + u_4 - 4u_1 &= -1, & u_1 + u_3 + u_5 - 4u_2 &= -1, & u_2 + u_6 - 4u_3 &= -1, & u_1 + u_5 + u_7 - 4u_4 &= -1, \\
> u_2 + u_4 + u_6 + u_8 - 4u_5 &= -1, & u_3 + u_5 - 4u_6 &= -1, & u_4 + u_8 - 4u_7 &= -1, & u_5 + u_7 - 4u_8 &= -1 .
> \end{aligned} \qquad (18)
> $$
>
> **Symmetry.** The region is symmetric about the diagonal $y = x$, which exchanges $u_2 \leftrightarrow u_4$, $u_3 \leftrightarrow u_7$, $u_6 \leftrightarrow u_8$. With these equalities five equations remain:
>
> $$
> 2u_2 - 4u_1 = -1, \quad u_1 + u_3 + u_5 - 4u_2 = -1, \quad u_2 + u_6 - 4u_3 = -1, \quad 2u_2 + 2u_6 - 4u_5 = -1, \quad u_3 + u_5 - 4u_6 = -1 .
> $$
>
> Elimination gives
>
> $$
> u_1 = \tfrac{44}{67} \approx 0.657, \quad u_2 = u_4 = \tfrac{109}{134} \approx 0.813, \quad u_3 = u_7 = \tfrac{165}{268} \approx 0.616, \quad u_5 = \tfrac{263}{268} \approx 0.981, \quad u_6 = u_8 = \tfrac{87}{134} \approx 0.649 . \qquad (19)
> $$
>
> The largest value is at the center, $u_5$, and the points next to the missing corner ($u_6$, $u_8$) are lower than their mirror images across the other diagonal ($u_2$, $u_4$). Physically, $u$ is the deflection of an L-shaped membrane under a uniform load, or the stress function of an L-shaped bar in torsion.
>
> *Powers: 7.4, Example 3 and Figure 4*

^ex-71-3

## Iterative Methods

Systems of up to ten equations can be solved by elimination. A finer mesh, needed for better accuracy, increases the number of unknowns dramatically: with $\Delta x = \Delta y = \frac1{10}$, Example §71.1 has $81$ unknowns ($25$ with symmetry), and problems with many thousands of unknowns are common. Such systems are almost always solved by iterative methods, which generate a sequence of approximate solutions.

> [!definition] Definition §71.2: Gauss–Seidel Method
> On a mesh with $\Delta x = \Delta y = 1/N$, index the values by $u_{i,j} \cong u(x_i, y_j)$ (20). The replacement equations for the potential equation,
>
> $$
> \frac{u_{i+1,j} - 2u_{i,j} + u_{i-1,j}}{(\Delta x)^2} + \frac{u_{i,j+1} - 2u_{i,j} + u_{i,j-1}}{(\Delta y)^2} = 0 ,
> $$
>
> become, with $\Delta x = \Delta y$,
>
> $$
> u_{i,j} = \tfrac14\big(u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1}\big), \qquad 1 \le i, j \le N - 1 , \qquad (21)
> $$
>
> with the boundary values ($u_{0,j}$, $u_{N,j}$, $u_{i,0}$, $u_{i,N}$) given. The **Gauss–Seidel method** sweeps through the array of $u$'s, replacing each $u_{i,j}$ by the combination on the right of (21), always using the newest available values. After several sweeps the numbers no longer change much; when new and old values agree closely enough at every point, the iteration stops.
>
> *Powers: 7.4, Equations (20)–(23) and text*

^def-71-2

The result satisfies (21) only approximately. But the exact solution of the replacement equations is itself only an approximation to the solution of the differential equation, so it is not urgent to obtain it exactly.

> [!example] Example §71.4: Gauss–Seidel Sweeps
> Apply the Gauss–Seidel method to Example §71.1 ($N = 4$), starting from $u = 0$ at all interior points and sweeping left to right, bottom to top.
>
> **First sweep.** $u_1 = \frac14(u_2 + u_4 + \frac12 + 0) = \frac18$; then $u_2 = \frac14(u_1 + u_3 + u_5 + 1) = \frac14(\frac18 + 1) = \frac9{32}$, using the new $u_1$; $u_3 = \frac14(\frac9{32} + \frac12) = \frac{25}{128}$; $u_4 = \frac14 u_1 = \frac1{32}$; $u_5 = \frac14(u_2 + u_4) = \frac5{64}$; and so on.
>
> Continuing, the values at the four representative points are:
>
> | sweep | $u_1$ | $u_2$ | $u_4$ | $u_5$ |
> |---|---|---|---|---|
> | $1$ | $0.1250$ | $0.2813$ | $0.0313$ | $0.0781$ |
> | $2$ | $0.2031$ | $0.3691$ | $0.1035$ | $0.2109$ |
> | $3$ | $0.2432$ | $0.4221$ | $0.1702$ | $0.2930$ |
> | $5$ | $0.2922$ | $0.4796$ | $0.2295$ | $0.3545$ |
> | $10$ | $0.3119$ | $0.4994$ | $0.2494$ | $0.3744$ |
> | $15$ | $0.3125$ | $0.5000$ | $0.2500$ | $0.3750$ |
>
> By sweep $15$ the values agree with the solution $\frac5{16}, \frac12, \frac14, \frac38$ to four decimals; the largest change in a sweep falls below $0.0005$ after $11$ sweeps.
>
> **A finer mesh.** With $N = 10$ (81 unknowns) the same stopping rule ends after $48$ sweeps with $u(\frac12, \frac12) \approx 0.3277$, while the fully converged solution of the replacement equations has $0.3321$ and the exact value is $0.3247$. Two lessons: the iteration slows down as the mesh is refined, so small changes per sweep do not mean small distance from the solution; and the error of the replacement equations themselves ($0.007$ here) is of the same size, which is why Powers stops early.
>
> *Powers: 7.4, Iterative Methods (text)*

^ex-71-4
