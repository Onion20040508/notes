---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 0
section: 3
powers: "0.3"
aliases: ["Powers 0.3"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§2★ Nonhomogeneous Linear Equations]] · ↑ [[· 0★ Ordinary Differential Equations Review]] · [[§4★ Singular Boundary Value Problems]] →

*Powers, Section 0.3.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

A boundary value problem prescribes conditions at the two ends of an interval instead of initial data at one point. The change is not cosmetic: an initial value problem for a linear equation always has exactly one solution, but even an innocent-looking boundary value problem may have one, none, or infinitely many. The section derives three physical boundary value problems: the shape of a hanging cable (a parabola under a uniform load, a catenary under its own weight), steady heat conduction in a rod, and the buckling of a column. The last is the first eigenvalue problem of the subject: the column buckles exactly at the loads for which a homogeneous problem has a nonzero solution. Separation of variables produces such eigenvalue problems for every heat, wave and potential problem from [[§19 Example꞉ Fixed End Temperatures#^thm-19-2|Theorem §19.2]] on.

## Boundary Value Problems

> [!definition] Definition §3.1: Boundary Value Problem
> A **boundary value problem** in one dimension is an ordinary differential equation together with conditions (**boundary conditions**) involving values of the solution and/or its derivatives at two or more points. The number of conditions imposed equals the order of the differential equation. Boundary value problems of physical relevance usually have these characteristics:
> 1. the conditions are imposed at two different points;
> 2. the solution is of interest only between those two points;
> 3. the independent variable is a space variable, written $x$.
>
> The main concern here is with linear second-order equations; problems in elasticity often involve fourth-order equations.
>
> *Powers: 0.3 (text)*

^def-3-1

When the differential equation has a known general solution, the two boundary conditions give two equations for the two constants in it. If the differential equation is linear these are two linear equations, easily solved if there is a solution. Unlike the initial value problem ([[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|331 Thm. §14.1]]), there need not be one.

> [!example] Example §3.1: One Solution, None, or Infinitely Many
> Of these three boundary value problems, one has exactly one solution, one has none, and one has infinitely many:
>
> $$
> \text{(a)}\ u'' + u = 0,\ u(0) = 0,\ u(\pi) = 0; \qquad \text{(b)}\ u'' + u = 1,\ u(0) = 0,\ u(1) = 0; \qquad \text{(c)}\ u'' + u = 0,\ u(0) = 0,\ u(\pi) = 1 .
> $$
>
> **(a)** The general solution is $u = c_1\cos x + c_2\sin x$. Then $u(0) = c_1 = 0$, and $u(\pi) = c_2\sin\pi = 0$ holds for every $c_2$. **Infinitely many** solutions: $u = c_2\sin x$.
>
> **(b)** A particular solution is $u_p = 1$, so $u = 1 + c_1\cos x + c_2\sin x$. Then $u(0) = 1 + c_1 = 0$ gives $c_1 = -1$, and $u(1) = 1 - \cos 1 + c_2\sin 1 = 0$ gives $c_2 = (\cos1 - 1)/\sin 1 = -\tan\frac12$ (half-angle formulas), since $\sin 1 \ne 0$. **Exactly one** solution:
>
> $$
> u(x) = 1 - \cos x - \tan\tfrac12\,\sin x .
> $$
>
> **(c)** As in (a), $u(0) = 0$ forces $u = c_2\sin x$, and then $u(\pi) = 0 \ne 1$ whatever $c_2$ is. **No** solution.
>
> In each case the boundary conditions give a linear system for $(c_1, c_2)$ with coefficient matrix $\begin{bmatrix}1 & 0 \\ \cos L & \sin L\end{bmatrix}$, $L = \pi$ or $1$. Its determinant $\sin L$ vanishes for $L = \pi$, and then the system has either no solution or infinitely many, depending on the right side. [[§5★ Green's Functions#^thm-5-3|Theorem §5.3]] turns this observation into a theorem.
>
> *Powers: Exercise 0.3.1*

^ex-3-1

> [!remark] Remark: Method — Solving a Linear Boundary Value Problem
> Solving a boundary value problem is not substantially different from solving an initial value problem:
> 1. Find the general solution of the differential equation, $u = u_p + c_1u_1 + c_2u_2$ ([[§2★ Nonhomogeneous Linear Equations#^thm-2-2|Theorem §2.2]]); it contains two arbitrary constants for a second-order equation.
> 2. Apply the two boundary conditions. For a linear equation with linear boundary conditions this gives two linear equations for $c_1$, $c_2$.
> 3. If the determinant of this system is not zero, there is exactly one solution. If it is zero, there is either no solution or infinitely many (Example §3.1).

^rem-3-1

## The Hanging Cable

Consider a cable fastened at each end and carrying a distributed load, such as the cable of a suspension bridge. Let $u(x)$ be the height of its centerline above a horizontal $x$-axis, $0 < x < a$. The key assumption is that the cable is **perfectly flexible**: the force inside it is always a tension, directed along the tangent to the centerline.

> [!theorem] Proposition §3.1: Equation of the Hanging Cable
> A perfectly flexible cable at rest, fastened at heights $h_0$ and $h_1$ above the ends of $0 \le x \le a$ and carrying a load of intensity $f(x)$ (force per unit of horizontal length, continuous), has a tension whose horizontal component $T$ is the same at every point, and its centerline satisfies
>
> $$
> T\frac{d^2u}{dx^2} = f(x), \quad 0 < x < a, \qquad (3)
> $$
>
> $$
> u(0) = h_0, \qquad u(a) = h_1 . \qquad (4)
> $$
>
> *Powers: 0.3, Equations (1)–(4)*

^prop-3-1

> [!proof]+ Proof
> Consider the small segment of cable between $x$ and $x + \Delta x$. Let $T(x)$ be the magnitude of the tension at $x$ and $\phi(x)$ the angle between the tangent to the centerline and the horizontal. The cable is not moving, so by Newton's second law the horizontal and the vertical components of the forces on the segment sum to $0$:
>
> $$
> T(x + \Delta x)\cos\big(\phi(x + \Delta x)\big) - T(x)\cos\big(\phi(x)\big) = 0 \qquad \text{(horizontal)}, \qquad (1)
> $$
>
> $$
> T(x + \Delta x)\sin\big(\phi(x + \Delta x)\big) - T(x)\sin\big(\phi(x)\big) - f(x)\Delta x = 0 \qquad \text{(vertical)} , \qquad (2)
> $$
>
> where $f(x)\Delta x$ is the load borne by the segment. (Exactly, the load is $\int_x^{x + \Delta x} f$, which is $f(x)\Delta x$ up to an error that is small compared with $\Delta x$ because $f$ is continuous; this does not affect the limit below.)
>
> By (1), the horizontal component $T(x)\cos\phi(x)$ is the same at both ends of every segment, hence has one value $T$ at every point, including the supports. So $T(x) = T/\cos\phi(x)$ and $T(x + \Delta x) = T/\cos\phi(x + \Delta x)$, and (2) becomes
>
> $$
> T\Big(\tan\big(\phi(x + \Delta x)\big) - \tan\big(\phi(x)\big)\Big) - f(x)\Delta x = 0 .
> $$
>
> Since $\phi(x)$ is the angle of the tangent, $\tan\phi(x) = u'(x)$ is the slope of the cable. Dividing by $\Delta x$,
>
> $$
> T\,\frac{u'(x + \Delta x) - u'(x)}{\Delta x} = f(x) ,
> $$
>
> and letting $\Delta x \to 0$ the difference quotient becomes $u''(x)$, which is (3). The conditions (4) say that the cable is fastened at the given heights.

^pf-3-1

The load model decides the equation. Two cases:
- **A load uniformly distributed in the horizontal direction**, $f(x)\Delta x = w\Delta x$, approximately true for a suspension bridge: $u'' = w/T$ (7).
- **The cable hanging under its own weight** of $w$ per unit length of cable: $f(x)\Delta x = w\,\Delta s$, with $s$ the arc length, and $\Delta s/\Delta x \to \sqrt{1 + (u')^2}$. The problem becomes

$$
\frac{d^2u}{dx^2} = \frac wT\sqrt{1 + \Big(\frac{du}{dx}\Big)^2}, \quad 0 < x < a, \qquad u(0) = h_0, \quad u(a) = h_1 , \qquad (5), (6)
$$

a **nonlinear** equation, which nevertheless can be solved in closed form.

> [!example] Example §3.2: Parabola and Catenary
> **(a) Uniform horizontal load.** Solve $u'' = w/T$, $u(0) = h_0$, $u(a) = h_1$ (7). Two integrations give the general solution $u(x) = \frac w{2T}x^2 + c_1x + c_2$. The boundary conditions require
>
> $$
> u(0) = h_0:\ c_2 = h_0, \qquad u(a) = h_1:\ \frac w{2T}a^2 + c_1a + c_2 = h_1 ,
> $$
>
> so $c_1 = \frac{h_1 - h_0}a - \frac{wa}{2T}$, and
>
> $$
> u(x) = \frac w{2T}(x^2 - ax) + \frac{h_1 - h_0}{a}x + h_0 . \qquad (8)
> $$
>
> The cable is part of a parabola opening upward.
>
> **(b) The cable's own weight.** With $\mu = w/T$, (5) reads $u'' = \mu\sqrt{1 + (u')^2}$. The unknown $u$ does not appear, so put $q = u'$: then $q' = \mu\sqrt{1 + q^2}$ is [[Solution of Separable Equations|separable]], $\int dq/\sqrt{1 + q^2} = \sinh^{-1}q = \mu x + \mu c$ ([[§24 Hyperbolic Functions#^thm-24-4|Calc Thm. §24.4]]), so $q = \sinh\big(\mu(x + c)\big)$ and
>
> $$
> u(x) = c' + \frac1\mu\cosh\big(\mu(x + c)\big)
> $$
>
> with arbitrary constants $c$, $c'$. (Check: $u' = \sinh\mu(x + c)$, $u'' = \mu\cosh\mu(x + c) = \mu\sqrt{1 + \sinh^2\mu(x + c)}$.) The graph is a **catenary**. For supports at equal heights, $u(0) = u(a) = h$, the condition $\cosh(\mu c) = \cosh\big(\mu(a + c)\big)$ forces $c = -(a + c)$, so $c = -a/2$ (the lowest point is in the middle), and then $c' = h - \frac1\mu\cosh\frac{\mu a}2$:
>
> $$
> u(x) = h - \frac1\mu\Big(\cosh\frac{\mu a}{2} - \cosh\mu\Big(x - \frac a2\Big)\Big) .
> $$
>
> *Powers: 0.3, Example (Hanging Cable); Exercises 0.3.4 and 0.3.5*

^ex-3-2

## Heat Conduction in a Rod

A long rod of uniform material and cross section conducts heat along its axis, and its temperature $u(x)$ does not change in time. Let $A$ be the cross-sectional area, $C$ the circumference and $q$ the heat flow rate (heat per unit time per unit area, in the direction of increasing $x$).

> [!definition] Definition §3.2: Fourier's Law
> **Fourier's law** (experimental): the heat flow rate through a unit area of material is proportional to the temperature difference and inversely proportional to the thickness. In the limit,
>
> $$
> q = -\kappa\frac{du}{dx} , \qquad (13)
> $$
>
> with $\kappa > 0$ the **conductivity**; the minus sign says that heat moves from hotter toward cooler regions.
>
> *Powers: 0.3 (text), Equations (10), (11), (13)*

^def-3-2

> [!definition] Definition §3.2: Newton's Law of Cooling
> **Newton's law of cooling**: heat lost through the cylindrical surface by convection to a surrounding medium at temperature $T$ is proportional to the temperature difference; per slice of length $\Delta x$ the rate of heat entering is
>
> $$
> g(x)A\,\Delta x = -h\big(u(x) - T\big)C\,\Delta x , \qquad (11)
> $$
>
> with $h$ the **heat transfer coefficient** (negative when $u > T$: heat leaves the rod). Heat generated by an electric current $I$ in a rod of resistance $R$ per unit length enters at the rate $g(x)A\,\Delta x = I^2R\,\Delta x$ (10).
>
> *Powers: 0.3 (text), Equations (10), (11), (13)*

^def-3-new1

> [!theorem] Proposition §3.2: Steady-State Heat Equation in a Rod
> If heat enters the rod at the rate $g(x)$ per unit volume by means other than conduction through the cross sections, and the conductivity $\kappa$ is constant, the steady temperature satisfies
>
> $$
> -\kappa\frac{d^2u}{dx^2} = g(x), \qquad 0 < x < a , \qquad (14)
> $$
>
> where $a$ is the length of the rod. If the ends are held at constant temperatures, the boundary conditions are
>
> $$
> u(0) = T_0, \qquad u(a) = T_1 ; \qquad (15)
> $$
>
> if instead heat is supplied at $x = 0$ at the rate $H$ (heat per unit time, by a heating coil, say), the condition there is
>
> $$
> -\kappa A\frac{du}{dx}(0) = H . \qquad (16)
> $$
>
> *Powers: 0.3, Equations (9)–(16)*

^prop-3-2

> [!proof]+ Proof
> Apply a heat balance, "what goes in must come out", to the slice between $x$ and $x + \Delta x$. Heat enters through the face at $x$ at the rate $q(x)A$ and by other means at the rate $g(x)A\Delta x$; it leaves through the face at $x + \Delta x$ at the rate $q(x + \Delta x)A$. Since the temperature does not change,
>
> $$
> q(x)A + g(x)A\Delta x = q(x + \Delta x)A . \qquad (9)
> $$
>
> Dividing by $A\Delta x$, $\frac{q(x + \Delta x) - q(x)}{\Delta x} = g(x)$, and in the limit
>
> $$
> \frac{dq}{dx} = g(x) . \qquad (12)
> $$
>
> The unknown $u$ does not appear in (12); Fourier's law (13) brings it in: $\frac{d}{dx}\big(-\kappa u'\big) = -\kappa u'' = g(x)$, which is (14). Condition (16) says that the heat flowing into the rod through the face $x = 0$, $q(0)A = -\kappa Au'(0)$, equals the rate $H$ supplied there.

^pf-3-2

*Uses:* [[§3★ Boundary Value Problems#^def-3-2|Def. §3.2]], [[§3★ Boundary Value Problems#^def-3-new1|Def. §3.2]]

> [!remark]- Connections
> - The three-dimensional version of the heat balance replaces the two faces by the boundary of a region and uses the divergence theorem, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1|452 Thm. §17.1]]; the same balance law in fluid form is the continuity equation, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-4|452 Thm. §17.4]]. The time-dependent derivation is [[§17 Derivation and Boundary Conditions#^thm-17-2|Theorem §17.2]] (Powers 2.1), and (14) is its steady state, [[§18 Steady-State Temperatures#^def-18-1|Definition §18.1]] (Powers 2.2).

> [!example] Example §3.3: A Rod Losing Heat to Its Surroundings
> Solve
>
> $$
> -\kappa\frac{d^2u}{dx^2} = -hu(x)\frac CA, \quad 0 < x < a, \qquad u(0) = T_0, \quad u(a) = T_0 . \qquad (17), (18)
> $$
>
> Physically the rod loses heat by convection to a medium at temperature $0$ (Definition §3.2 with $T = 0$), while both ends are held at $T_0$.
>
> **Equation.** With $\mu^2 = hC/\kappa A$, the equation becomes $u'' - \mu^2u = 0$, with general solution $u(x) = c_1\cosh(\mu x) + c_2\sinh(\mu x)$ ([[§1★ Homogeneous Linear Equations#^ex-1-1|Example §1.1]]).
>
> **Boundary conditions.** $u(0) = c_1 = T_0$. Then $u(a) = T_0\cosh(\mu a) + c_2\sinh(\mu a) = T_0$, and since $\sinh(\mu a) \ne 0$, $c_2 = T_0\big(1 - \cosh(\mu a)\big)/\sinh(\mu a)$:
>
> $$
> u(x) = T_0\Big(\cosh(\mu x) + \frac{1 - \cosh(\mu a)}{\sinh(\mu a)}\sinh(\mu x)\Big) .
> $$
>
> **A symmetric form.** The function $v(x) = T_0\dfrac{\cosh\mu(x - a/2)}{\cosh(\mu a/2)}$ also satisfies $v'' = \mu^2v$ and $v(0) = v(a) = T_0$ ($\cosh$ is even). The determinant of the system for $c_1$, $c_2$ is $\sinh(\mu a) \ne 0$, so the problem has only one solution, and
>
> $$
> u(x) = T_0\,\frac{\cosh\big(\mu(x - a/2)\big)}{\cosh(\mu a/2)} .
> $$
>
> This form shows at once that the profile is symmetric about the midpoint, where the temperature is lowest, $u(a/2) = T_0/\cosh(\mu a/2)$. The larger $\mu a$ (more convection, or a longer or thinner rod), the colder the middle (figure below).
>
> *Powers: 0.3, Example (Heat Conduction in a Rod); Exercise 0.3.10*

^ex-3-3

![[m341-3-1.svg]]
*Steady temperature $u(x) = T_0\cosh(\mu(x - a/2))/\cosh(\mu a/2)$ in a rod with both ends at $T_0$, losing heat to surroundings at temperature $0$ (Example §3.3), for $\mu a = 1, 3, 6, 12$. For small $\mu a$ conduction along the rod dominates and the profile is nearly flat; for large $\mu a$ convection dominates and only a boundary layer of width about $1/\mu$ near each end stays warm.*

## Buckling of a Column; Eigenvalue Problems

The next problem is different in spirit: instead of solving a boundary value problem, one looks for the parameter values that permit solutions of a special form.

> [!definition] Definition §3.3: Eigenvalue Problem
> An **eigenvalue problem** consists of a homogeneous differential equation containing a parameter $\lambda$, accompanied by homogeneous boundary conditions. Since both the equation and the boundary conditions are homogeneous, $u \equiv 0$ is always a solution. The question is: for which values of the parameter $\lambda$ are there nonzero solutions? Those values are the **eigenvalues**. Eigenvalue problems are often used to find the dividing line between stable and unstable behavior.
>
> *Powers: 0.3 (text)*

^def-3-3

The nonzero solutions belonging to an eigenvalue are its eigenfunctions; Powers introduces the name in 2.4, [[§20 Example꞉ Insulated Bar#^def-20-new1|Definition §20.1]], and the general theory in 2.7, [[§23 Sturm–Liouville Problems#^def-23-1|Definition §23.1]].

> [!remark]- Connections
> - The finite-dimensional model: $\lambda$ is an eigenvalue of an operator $T$ if $Tv = \lambda v$ for some $v \ne 0$, [[§14 Invariant Subspaces#^ladr-5-5|LADR 5.5]], [[§32 Eigenvectors and Eigenvalues#^def-32-1|235 Def. §32.1]]. Here the operator is $u \mapsto -u''$ on functions satisfying the homogeneous boundary conditions, and "nonzero solution of the homogeneous problem" is "nonzero vector in the null space of $T - \lambda I$".

> [!theorem] Proposition §3.3: The Eigenvalues of u″ + λ²u = 0, u(0) = u(a) = 0
> Let $\lambda > 0$. The problem
>
> $$
> \frac{d^2u}{dx^2} + \lambda^2u = 0, \quad 0 < x < a, \qquad u(0) = 0, \quad u(a) = 0 \qquad (21), (20)
> $$
>
> has a solution other than $u \equiv 0$ if and only if $\lambda a$ is an integer multiple of $\pi$, that is,
>
> $$
> \lambda = \frac{n\pi}{a}, \qquad n = 1, 2, 3, \ldots ;
> $$
>
> the solutions are then $u(x) = c\sin(n\pi x/a)$, $c$ arbitrary. For all other $\lambda > 0$, $u \equiv 0$ is the only solution.
>
> *Powers: 0.3, Example (Buckling of a Column)*

^prop-3-3

> [!proof]+ Proof
> The general solution of the equation is $u(x) = c_1\cos(\lambda x) + c_2\sin(\lambda x)$ ([[§1★ Homogeneous Linear Equations#^ex-1-1|Example §1.1]]). The condition $u(0) = 0$ forces $c_1 = 0$, leaving $u(x) = c_2\sin(\lambda x)$. The second condition requires
>
> $$
> u(a) = c_2\sin(\lambda a) = 0 .
> $$
>
> If $\sin(\lambda a) \ne 0$, the only possibility is $c_2 = 0$, and $u \equiv 0$. If $\sin(\lambda a) = 0$, any $c_2$ gives a solution. The integer multiples of $\pi$ are the only arguments at which the sine is $0$, and $\lambda a > 0$, so $\sin(\lambda a) = 0$ exactly when $\lambda a = n\pi$ with $n$ a positive integer.

^pf-3-3

*Uses:* [[§1★ Homogeneous Linear Equations#^ex-1-1|Ex. §1.1]]

> [!example] Example §3.4: Buckling of a Column; the Euler Load
> A long, slender column of length $a$ with hinged bottom end carries an axial load $P$; its upper end can move up or down but not sideways. Let $u(x)$ be the displacement of the centerline from a vertical reference line. If the column were cut at height $x$, an upward force $P$ and a clockwise moment $Pu(x)$ would have to be applied to the upper part to keep it in equilibrium, and they must be supplied by the lower part. The internal bending moment (positive counterclockwise) is $EI\,u''$, with $E$ Young's modulus and $I$ the moment of inertia of the cross section ($I = b^4/12$ for a square of side $b$). Equating external and internal moments,
>
> $$
> EI\frac{d^2u}{dx^2} = -Pu, \quad 0 < x < a, \qquad u(0) = 0, \quad u(a) = 0 . \qquad (19), (20)
> $$
>
> **Solve.** Set $P/EI = \lambda^2$; the equation becomes $u'' + \lambda^2u = 0$ (21). By Proposition §3.3:
> - If $\lambda a$ is not a multiple of $\pi$, the only solution is $u \equiv 0$: the column stands straight and transmits the load to its support, as intended.
> - If $\lambda a = n\pi$, every $u = c_2\sin(n\pi x/a)$ is a solution: the column can assume a sinusoidal shape, and may then collapse, or **buckle**, under the axial load.
>
> **The critical load.** In terms of the original parameters, $\lambda a = \pi$ is $\sqrt{P/EI}\,a = \pi$. Thinking of $E$, $I$ and $a$ as given, buckling is caused by the force
>
> $$
> P = EI\Big(\frac\pi a\Big)^2 ,
> $$
>
> the **critical** or **Euler load**. The higher critical loads, for $\lambda a = 2\pi, 3\pi, \ldots$, are so unstable as to be of no physical interest in this problem: the column has already buckled at the first.
>
> *Powers: 0.3, Example (Buckling of a Column)*

^ex-3-4

![[m341-3-2.svg]]
*The first three buckling shapes $\sin(n\pi x/a)$ of Example §3.4, the nonzero solutions of $u'' + \lambda^2u = 0$, $u(0) = u(a) = 0$ at the eigenvalues $\lambda = n\pi/a$ (Proposition §3.3). Only the first, at the Euler load $P = EI\pi^2/a^2$, is observed; the same functions are the modes of the vibrating string and the terms of the Fourier sine series.*

> [!example] Example §3.5: Eigenvalues with Other Boundary Conditions
> Find all $\lambda \ge 0$ for which these problems have a solution other than $u \equiv 0$:
>
> $$
> \text{(a)}\ u(0) = 0,\ u'(a) = 0; \qquad \text{(b)}\ u'(0) = 0,\ u(a) = 0; \qquad \text{(c)}\ u'(0) = 0,\ u'(a) = 0 ,
> $$
>
> each with the equation $u'' + \lambda^2u = 0$, $0 < x < a$.
>
> **$\lambda > 0$.** The general solution is $u = c_1\cos(\lambda x) + c_2\sin(\lambda x)$, with $u' = -\lambda c_1\sin(\lambda x) + \lambda c_2\cos(\lambda x)$.
> - (a) $u(0) = c_1 = 0$; then $u'(a) = \lambda c_2\cos(\lambda a) = 0$ needs $\cos(\lambda a) = 0$: $\lambda a = \frac\pi2, \frac{3\pi}2, \ldots$, so $\lambda = \dfrac{(2n - 1)\pi}{2a}$, $u = \sin(\lambda x)$.
> - (b) $u'(0) = \lambda c_2 = 0$, so $c_2 = 0$; then $u(a) = c_1\cos(\lambda a) = 0$: again $\lambda = \dfrac{(2n - 1)\pi}{2a}$, now with $u = \cos(\lambda x)$.
> - (c) $c_2 = 0$ as in (b); then $u'(a) = -\lambda c_1\sin(\lambda a) = 0$: $\lambda = \dfrac{n\pi}a$, $n = 1, 2, \ldots$, with $u = \cos(\lambda x)$.
>
> **$\lambda = 0$** must be checked separately, since then the general solution is $u = c_1 + c_2x$ ([[§1★ Homogeneous Linear Equations#^ex-1-1|Example §1.1]]). In (a), $c_1 = 0$ and $u'(a) = c_2 = 0$; in (b), $c_2 = 0$ and $u(a) = c_1 = 0$: only the zero solution. In (c), $c_2 = 0$ and $c_1$ is free: **$\lambda = 0$ is an eigenvalue of (c)**, with the constant solution $u = 1$.
>
> So (a) and (b) have the eigenvalues $\lambda = (2n - 1)\pi/2a$, $n = 1, 2, \ldots$, and (c) has $\lambda = n\pi/a$, $n = 0, 1, 2, \ldots$. (A negative $\lambda^2 = -\nu^2$ gives no eigenvalues: with $u = c_1\cosh\nu x + c_2\sinh\nu x$ the same steps force $c_1 = c_2 = 0$, because $\cosh$ never vanishes and $\sinh\nu a \ne 0$.) These are the eigenvalue problems of the heat equation with one end or both ends insulated, [[§20 Example꞉ Insulated Bar#^thm-20-1|Theorem §20.1]] (both ends insulated, (c)) and [[§21 Example꞉ Different Boundary Conditions#^thm-21-1|Theorem §21.1]] (one end fixed, one insulated, (a)) (Powers 2.4, 2.5).
>
> *Powers: Exercise 0.3.3*

^ex-3-5
