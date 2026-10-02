---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 2
section: 17
powers: "2.1"
aliases: ["Powers 2.1"]
tags: [fourier-series-and-pdes, math341]
---
← [[§16★ Applications of Fourier Series and Integrals]] · ↑ [[· 2 The Heat Equation]] · [[§18 Steady-State Temperatures]] →

*Powers, Section 2.1 · MAT 341 lectures 9.17, 9.19 · HW 4.*

This section derives the first partial differential equation of the course, the heat equation $u_{xx} = \frac1k u_t$ for the temperature $u(x, t)$ in a thin rod. Two physical laws go in: conservation of energy, applied to a thin slice of the rod, and Fourier's law, which says that heat flows from hot to cold at a rate proportional to the temperature gradient. The equation alone has infinitely many solutions; the temperature is pinned down by an initial condition and one boundary condition at each end, of Dirichlet (fixed temperature), Neumann (fixed heat flow, in particular insulation) or Robin (convection) type. The same equation, with Fick's law in place of Fourier's, governs diffusion of a substance through a medium.

## The Heat Balance

Consider a rod or bar of heat-conducting material with uniform cross section of area $A$, along the $x$-axis from $x = 0$ to $x = a$. Assume that the temperature does not vary over a cross section, so that it depends only on position $x$ and time $t$. The idea is to apply conservation of energy to the slice of the rod between $x$ and $x + \Delta x$.

> [!definition] Definition §17.1: Heat Flux, Heat Capacity and Generation Rate
> Let $u(x, t)$ be the temperature at position $x$ and time $t$.
> - The **heat flux** $q(x, t)$ is the rate at which heat crosses the section at $x$, per unit area; it is positive when heat flows to the right. Its dimensions are $[q] = H/tL^2$ ($H$ = heat energy, $t$ = time, $L$ = length; square brackets mean "dimension of").
> - The material has **density** $\rho$ and **heat capacity** $c$ per unit mass, $[c] = H/mT$ ($m$ = mass, $T$ = temperature). The rate at which heat is stored in a slice of length $\Delta x$ is proportional to the rate of change of temperature: approximately $\rho cA\,\Delta x\,\dfrac{\partial u}{\partial t}(x, t)$.
> - The **generation rate** $g$, $[g] = H/tL^3$, is the rate per unit volume at which heat enters the rod other than by conduction along it: by radiation or convection from a surrounding medium, or by conversion from another form of energy (resistance to an electric current, a chemical or nuclear reaction). A negative $g$ means heat is lost. $g$ may depend on $x$, $t$ and even $u$. The rate of generation in the slice is $A\,\Delta x\,g$.
>
> *Powers: 2.1 (text)*

^def-17-1

The **law of conservation of energy** says that the heat entering a region plus the heat generated inside equals the heat leaving plus the heat stored; it holds equally for rates per unit time. Heat enters the slice through the face at $x$ at the rate $Aq(x, t)$ and leaves through the face at $x + \Delta x$ at the rate $Aq(x + \Delta x, t)$.

> [!theorem] Proposition §17.1: Heat Balance Equation
> If $q$ has a continuous $x$-derivative and $u$ a continuous $t$-derivative, and $g$ is continuous, then at every point of the rod
>
> $$
> -\frac{\partial q}{\partial x} + g = \rho c\frac{\partial u}{\partial t} . \qquad (2)
> $$
>
> *Powers: 2.1, Equation (2)*

^prop-17-1

> [!proof]+ Proof
> Conservation of energy for the slice between $x$ and $x + \Delta x$ reads
>
> $$
> Aq(x, t) + A\,\Delta x\,g = Aq(x + \Delta x, t) + A\,\Delta x\,\rho c\frac{\partial u}{\partial t} . \qquad (1)
> $$
>
> Divide by $A\,\Delta x$ and rearrange:
>
> $$
> \frac{q(x, t) - q(x + \Delta x, t)}{\Delta x} + g = \rho c\frac{\partial u}{\partial t} .
> $$
>
> The ratio $\big(q(x + \Delta x, t) - q(x, t)\big)/\Delta x$ is a difference quotient, and as $\Delta x \to 0$ it tends to $\partial q/\partial x$. So in the limit, (2) holds.
>
> (Powers writes the storage and generation terms in (1) as approximations; here is why the limit is nevertheless exact. The exact storage and generation rates in the slice are $\int_x^{x + \Delta x} \rho cA\,u_t(\xi, t)\,d\xi$ and $\int_x^{x + \Delta x} A\,g(\xi, t)\,d\xi$. By the mean value theorem for integrals they equal $\rho cA\,\Delta x\,u_t(\xi_1, t)$ and $A\,\Delta x\,g(\xi_2, t)$ for some $\xi_1, \xi_2$ between $x$ and $x + \Delta x$. After division by $A\,\Delta x$ and $\Delta x \to 0$, continuity gives $\rho c\,u_t(x, t)$ and $g(x, t)$.)

^pf-17-1

*Uses:* [[§17 Derivation and Boundary Conditions#^def-17-1|Def. §17.1]], [[§43 Average Value of a Function#^thm-43-1|Calc Thm. §43.1]]

![[m341-17-1.svg]]
*The heat balance (1) for the slice between $x$ and $x + \Delta x$ (blue). Heat flows in through the left face at the rate $Aq(x,t)$ and out through the right face at the rate $Aq(x + \Delta x, t)$ (red); inside, heat is generated at the rate $A\,\Delta x\,g$ and stored at the rate $\rho cA\,\Delta x\,u_t$ (green). Nothing crosses the insulated lateral surface; heat lost through it would be counted in $g$.*

> [!remark] Remark: The Same Balance in Integral Form
> The derivation can be run on a whole segment $x_1 < x < x_2$ instead of a thin slice. The heat in the segment is $\int_{x_1}^{x_2} \rho cA\,u\,dx$, and conservation of energy says
>
> $$
> \frac{d}{dt}\int_{x_1}^{x_2} \rho cA\,u\,dx = Aq(x_1, t) - Aq(x_2, t) + \int_{x_1}^{x_2} A\,g\,dx .
> $$
>
> By the fundamental theorem of calculus the flux difference is a volume integral, $q(x_1, t) - q(x_2, t) = -\int_{x_1}^{x_2} q_x\,dx$, so $\int_{x_1}^{x_2} (\rho c\,u_t + q_x - g)\,dx = 0$ for every segment. A continuous function whose integral over every interval is zero vanishes identically (the one-dimensional case of [[§42 Three-Dimensional Heat Equation#^lem-42-1|Lemma §42.1]]), which is (2) again. In a three-dimensional body $V$ the heat leaving through the boundary is the flux integral $\iint_{\partial V} \mathbf{q}\cdot\mathbf{n}\,dS$, and the divergence theorem turns it into $\iiint_V \nabla\cdot\mathbf{q}\,dV$. The same argument then gives $\rho c\,u_t = -\nabla\cdot\mathbf{q} + g$, and with $\mathbf{q} = -\kappa\nabla u$ the three-dimensional heat equation, [[§42 Three-Dimensional Heat Equation#^thm-42-3|Theorem §42.3]]. In one dimension the divergence theorem is just the fundamental theorem of calculus.

^rem-17-1

> [!remark]- Connections
> - The divergence theorem $\int_{\partial D} \mathbf{u}\cdot\hat n\,dS = \int_D \nabla\cdot\mathbf{u}\,dV$ for bounded domains with piecewise smooth boundary, proved in $\mathbb{R}^n$: [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1|452 Thm. §17.1]]; Stewart's version in $\mathbb{R}^3$: [[§115 The Divergence Theorem#^thm-115-1|Calc Thm. §115.1]].
> - The one-dimensional case, $\int_{x_1}^{x_2} q_x\,dx = q(x_2) - q(x_1)$: [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]].

There are two unknowns, $q$ and $u$, in (2). A second relation between them is needed.

> [!definition] Definition §17.2: Fourier's Law of Heat Conduction
> **Fourier's law** of heat conduction in one dimension is
>
> $$
> q = -\kappa\frac{\partial u}{\partial x} .
> $$
>
> Heat flows downhill: $q$ is positive when $\partial u/\partial x$ is negative, at a rate proportional to the gradient of the temperature. The proportionality factor $\kappa$ is the **thermal conductivity**. It may depend on $x$ if the rod is not uniform, and also on the temperature; usually it is assumed constant.
>
> *Powers: 2.1 (text)*

^def-17-2

> [!definition] Definition §17.3: Thermal Diffusivity
> When $\kappa$, $\rho$ and $c$ are constants, the quantity
>
> $$
> k = \frac{\kappa}{\rho c}
> $$
>
> is the **thermal diffusivity** of the material, $[k] = L^2/t$. Typical values:
>
> | Material | $c$ (cal/g °C) | $\rho$ (g/cm³) | $\kappa$ (cal/s cm °C) | $k$ (cm²/s) |
> |---|---|---|---|---|
> | Aluminum | 0.21 | 2.7 | 0.48 | 0.83 |
> | Copper | 0.094 | 8.9 | 0.92 | 1.1 |
> | Steel | 0.11 | 7.8 | 0.11 | 0.13 |
> | Glass | 0.15 | 2.6 | 0.0014 | 0.0036 |
> | Concrete | 0.16 | 2.3 | 0.0041 | 0.011 |
> | Ice | 0.48 | 0.92 | 0.004 | 0.009 |
>
> *Powers: 2.1, Table 1*

^def-17-3

> [!theorem] Theorem §17.2: The Heat Equation
> Under Fourier's law the heat balance (2) becomes
>
> $$
> \frac{\partial}{\partial x}\Big(\kappa\frac{\partial u}{\partial x}\Big) + g = \rho c\frac{\partial u}{\partial t} , \qquad (3)
> $$
>
> where $\kappa$, $\rho$ and $c$ may all be functions. If they are independent of $x$, $t$ and $u$,
>
> $$
> \frac{\partial^2u}{\partial x^2} + \frac{g}{\kappa} = \frac1k\frac{\partial u}{\partial t} , \qquad (4)
> $$
>
> valid where the rod is and after the experiment starts: $0 < x < a$, $t > 0$. For a rod of length $a$ with uniform properties and cross section, no heat generated inside, and insulated cylindrical surface, this is the **heat equation**
>
> $$
> \frac{\partial^2u}{\partial x^2} = \frac1k\frac{\partial u}{\partial t} , \qquad 0 < x < a, \quad 0 < t . \qquad (5)
> $$
>
> *Powers: 2.1, Equations (3)–(5)*

^thm-17-2

> [!proof]+ Proof
> Substituting $q = -\kappa\,\partial u/\partial x$ ([[§17 Derivation and Boundary Conditions#^def-17-2|Definition §17.2]]) into (2) gives $-\frac{\partial}{\partial x}\big(-\kappa\frac{\partial u}{\partial x}\big) + g = \rho c\frac{\partial u}{\partial t}$, which is (3). If $\kappa$ is constant it comes out of the derivative, $\kappa u_{xx} + g = \rho c\,u_t$; dividing by $\kappa$ and writing $\rho c/\kappa = 1/k$ gives (4). With $g = 0$, (4) is (5).

^pf-17-2

*Uses:* [[§17 Derivation and Boundary Conditions#^prop-17-1|§17.1]], [[§17 Derivation and Boundary Conditions#^def-17-2|Def. §17.2]], [[§17 Derivation and Boundary Conditions#^def-17-3|Def. §17.3]]

> [!remark] Remark: Solutions Straighten Out
> Some qualitative features can be read off the equation itself. Fix a time $t^*$ and look at the graph of $u(x, t^*)$. Where the graph is concave up (shaped like U, J or a backwards J), $\partial^2u/\partial x^2 > 0$, so by the heat equation $\partial u/\partial t > 0$: the temperature rises there. Where the graph is concave down, $\partial^2u/\partial x^2 < 0$ and the temperature falls. Bumps are filled in and peaks worn down, so a solution of the heat equation tends to straighten out.

^rem-17-2

> [!example] Example §17.1: The Equation Alone Does Not Determine the Temperature
> Each of the functions
>
> $$
> u(x, t) = x^2 + 2kt, \qquad u(x, t) = e^{-kt}\sin(x)
> $$
>
> satisfies the heat equation (5). For the first, $u_{xx} = 2$ and $\frac1k u_t = \frac1k \cdot 2k = 2$. For the second, $u_{xx} = -e^{-kt}\sin x$ and $\frac1k u_t = \frac1k(-k)e^{-kt}\sin x = -e^{-kt}\sin x$. Since the equation is linear, their sum and difference are solutions too.
>
> More generally, for any constant $\lambda$,
>
> $$
> u(x, t) = \exp(-\lambda^2kt)\cos(\lambda x), \qquad u(x, t) = \exp(-\lambda^2kt)\sin(\lambda x)
> $$
>
> are solutions: in each case $u_{xx} = -\lambda^2u$ and $\frac1k u_t = \frac1k(-\lambda^2k)u = -\lambda^2u$. (These are the building blocks of every solution in [[§19 Example꞉ Fixed End Temperatures|§19]]–[[§22 Example꞉ Convection|§22]].)
>
> So the partial differential equation has infinitely many solutions. This is unsatisfactory both mathematically and physically: the temperature should be uniquely determined. More conditions must be placed on $u$, describing the initial temperature in the rod and what happens at its ends.
>
> *Powers: 2.1 (text) and Exercise 2.1.2*

^ex-17-1

## Initial and Boundary Conditions

> [!definition] Definition §17.4: Initial Condition
> The **initial condition** specifies the temperature at every point of the rod at the start:
>
> $$
> u(x, 0) = f(x), \qquad 0 < x < a ,
> $$
>
> where $f(x)$ is a given function of $x$ alone.
>
> *Powers: 2.1 (text)*

^def-17-4

The **boundary conditions** describe what happens at the ends. Let $x_0$ denote an endpoint, $0$ or $a$.

> [!definition] Definition §17.5: Dirichlet Condition
> A **Dirichlet condition**, or **condition of the first kind**, controls the temperature at the boundary:
>
> $$
> u(x_0, t) = \alpha(t) , \qquad (6)
> $$
>
> where $\alpha$ is a function of time; the constant case is included. For instance, ends exposed to an ice-water bath or to condensing steam are held at constant temperatures:
>
> $$
> u(0, t) = T_0, \qquad u(a, t) = T_1, \qquad t > 0 ,
> $$
>
> where $T_0$ and $T_1$ may be the same or different.
>
> *Powers: 2.1, Equation (6)*

^def-17-5

> [!definition] Definition §17.6: Neumann Condition; Insulated End
> A **Neumann condition**, or **condition of the second kind**, controls the heat flow rate at the boundary. Since Fourier's law ties the heat flow to the temperature gradient, it is written
>
> $$
> \frac{\partial u}{\partial x}(x_0, t) = \beta(t) , \qquad (7)
> $$
>
> where $\beta$ is a function of time. Most often $\beta(t) \equiv 0$. The condition
>
> $$
> \frac{\partial u}{\partial x}(x_0, t) = 0
> $$
>
> says that the heat flow through the end is zero: it describes an **insulated** surface.
>
> *Powers: 2.1, Equation (7)*

^def-17-6

> [!definition] Definition §17.7: Robin Condition
> A **Robin condition**, or **condition of the third kind**, is
>
> $$
> c_1u(x_0, t) + c_2\frac{\partial u}{\partial x}(x_0, t) = \gamma(t) , \qquad (8)
> $$
>
> a linear combination of the temperature and its gradient at the boundary.
>
> *Powers: 2.1, Equation (8)*

^def-17-7

> [!theorem] Proposition §17.3: Convection Gives a Robin Condition
> Suppose the surface at $x = a$ is exposed to air or another fluid at temperature $T(t)$, and that, by **Newton's law of cooling**, the rate at which heat passes from the body to the fluid is proportional to the difference between their temperatures:
>
> $$
> q(a, t) = h\big(u(a, t) - T(t)\big) . \qquad (9)
> $$
>
> The constant $h$ is the **convection coefficient** or **heat transfer coefficient**, $[h] = H/L^2tT$. Then
>
> $$
> -\kappa\frac{\partial u}{\partial x}(a, t) = hu(a, t) - hT(t) , \qquad (10)
> $$
>
> a Robin condition (8) with $c_1 = h$, $c_2 = \kappa$, $\gamma = hT$.
>
> *Powers: 2.1, Equations (9)–(10)*

^prop-17-3

> [!proof]+ Proof
> The heat conducted up to the surface from inside the rod is carried away by convection, so the conducted flux $q(a, t)$ equals the convective flux (9). By Fourier's law ([[§17 Derivation and Boundary Conditions#^def-17-2|Definition §17.2]]), $q(a, t) = -\kappa u_x(a, t)$; substituting in (9) gives (10). Moving $hu(a, t)$ to the left, $hu(a, t) + \kappa u_x(a, t) = hT(t)$, which is (8).

^pf-17-3

*Uses:* [[§17 Derivation and Boundary Conditions#^def-17-2|Def. §17.2]], [[§17 Derivation and Boundary Conditions#^def-17-7|Def. §17.7]]

> [!remark]- Connections
> - Newton's law of cooling for a body of uniform temperature, $dT/dt = k(T - T_s)$, and its exponential solution: [[§21 Exponential Growth and Decay#^def-21-4|Calc Def. §21.4]], [[§21 Exponential Growth and Decay#^cor-21-2|Calc Cor. §21.2]], [[§6 Modeling with First-Order Differential Equations#^ex-6-5|331 Ex. §6.5]]. Here the same law acts only at the surface, and the interior is governed by conduction.

> [!definition] Definition §17.8: Mixed Boundary Conditions
> The conditions (6), (7) and (8) each involve $u$ or its derivative at one point. If more than one point is involved, the boundary condition is called **mixed**. For example, if a uniform rod is bent into a ring and the ends $x = 0$ and $x = a$ are joined, appropriate boundary conditions are
>
> $$
> u(0, t) = u(a, t), \qquad t > 0 , \qquad (11)
> $$
>
> $$
> \frac{\partial u}{\partial x}(0, t) = \frac{\partial u}{\partial x}(a, t), \qquad t > 0 , \qquad (12)
> $$
>
> both of mixed type.
>
> *Powers: 2.1, Equations (11)–(12)*

^def-17-8

Many other kinds of boundary conditions exist and are even realizable, but these four are the most common. All four involve a **linear** operation on the function $u$; this is what the method of [[§19 Example꞉ Fixed End Temperatures|§19]] relies on, through the principle of superposition ([[§19 Example꞉ Fixed End Temperatures#^thm-19-4|Theorem §19.4]]).

> [!definition] Definition §17.9: Initial Value–Boundary Value Problem
> The heat equation, an initial condition and a boundary condition for each end form an **initial value–boundary value problem**. For instance:
>
> $$
> \begin{aligned}
> \frac{\partial^2u}{\partial x^2} &= \frac1k\frac{\partial u}{\partial t}, && 0 < x < a, \quad 0 < t, && (13) \\
> u(0, t) &= T_0, && 0 < t, && (14) \\
> -\kappa\frac{\partial u}{\partial x}(a, t) &= h\big(u(a, t) - T_1\big), && 0 < t, && (15) \\
> u(x, 0) &= f(x), && 0 < x < a . && (16)
> \end{aligned}
> $$
>
> The boundary conditions may be of different kinds at the two ends: here a fixed temperature at $x = 0$ and convection to a fluid at temperature $T_1$ at $x = a$.
>
> *Powers: 2.1, Equations (13)–(16)*

^def-17-9

> [!theorem] Theorem §17.4: Existence and Uniqueness
> A complete initial value–boundary value problem for the heat equation, such as (13)–(16), has one, and only one, solution.
>
> *Powers: 2.1 (text)*

^thm-17-4

*Powers omits the proof.*

> [!remark] Remark: Rods and Slabs
> The heat equation was derived for a "rod", an object much longer than it is wide. It applies equally to a "slab", an object much wider than it is thick. What matters is that the temperature varies in only one space direction (along the rod, or through the thickness of the slab). The multidimensional heat equation is derived in [[§42 Three-Dimensional Heat Equation#^thm-42-3|Theorem §42.3]].

^rem-17-3

> [!example] Example §17.2: Reading Off the Boundary Conditions
> Consider
>
> $$
> \frac{\partial^2u}{\partial x^2} + K = \frac{\partial u}{\partial t}, \quad 0 < x < a,\ t > 0; \qquad u(x, 0) = f(x); \qquad u(0, t) = T; \qquad \frac{\partial u}{\partial x}(a, t) = 0 ,
> $$
>
> where $K$ and $T$ are constants and $u$ is the temperature. Name the type of each boundary condition and explain its physical meaning.
>
> - The equation is (4) with $k = 1$ and a constant generation rate $g/\kappa = K$: heat is produced uniformly throughout the rod (for instance by an electric current).
> - $u(x, 0) = f(x)$ is the initial condition: the temperature distribution at $t = 0$.
> - $u(0, t) = T$ is a **Dirichlet** condition: the temperature at the end $x = 0$ is held fixed at $T$.
> - $u_x(a, t) = 0$ is a **Neumann** condition with $\beta = 0$: by Fourier's law the heat flux $q(a, t) = -\kappa u_x(a, t)$ is zero, so no heat crosses the end $x = a$; that end is insulated. (It does not say that the temperature at $x = a$ is constant; $u(a, t)$ changes in time.)
>
> In the lecture's example $u_t = ku_{xx}$, $u(0, t) = T_0$, the condition at $x = a$ is either Neumann, $u_x(a, t) = 0$, or Robin, $-\kappa u_x(a, t) = h(u(a, t) - T)$.
>
> *Source: 341 HW 4, Problem 1(a); 341 lecture 9.17*

^ex-17-2

> [!example] Example §17.3: Convection at the Left End
> Put (10) in the form (8), and find the condition when the surface at $x = 0$ (the left end) is exposed to convection with a fluid at temperature $T(t)$.
>
> **At $x = a$.** (10) is $hu(a, t) + \kappa u_x(a, t) = hT(t)$. The signs say that heat flows toward lower temperature: if $u(a, t) > T(t)$, the rod is hotter than the fluid, so $q(a, t) = h(u(a, t) - T(t)) > 0$ (heat leaves to the right) and $u_x(a, t) = -q(a, t)/\kappa < 0$ (the rod cools toward its right end).
>
> **At $x = 0$.** Heat leaving the rod now moves to the left, in the negative direction, so the flux leaving the rod is $-q(0, t)$, and Newton's law of cooling reads $-q(0, t) = h(u(0, t) - T(t))$. With Fourier's law $-q(0, t) = \kappa u_x(0, t)$:
>
> $$
> \kappa\frac{\partial u}{\partial x}(0, t) = hu(0, t) - hT(t) .
> $$
>
> Check of the signs: if $u(0, t) > T(t)$ the right side is positive, so $u_x(0, t) > 0$; the temperature increases into the rod, and heat flows from the interior toward the colder left end and out. In the form (8): $hu(0, t) - \kappa u_x(0, t) = hT(t)$. The coefficient of $u_x$ has opposite signs at the two ends, because the outward direction is $+x$ at $x = a$ and $-x$ at $x = 0$.
>
> *The summary of boundary conditions in lecture 9.19 writes the convection condition at $x = 0$ as $-\kappa u_x(0, t) = h(u(0, t) - T_0)$, the sign of the right-end condition (10); at a left end the sign of the $u_x$ term is reversed, as above.*
>
> *Powers: Exercise 2.1.5*

^ex-17-3

> [!example] Example §17.4: Convection Through the Lateral Surface
> Suppose the rod exchanges heat through its cylindrical surface by convection with a surrounding fluid at constant temperature $U$, the rate of transfer being proportional to the exposed area and to the temperature difference (Newton's law of cooling). Find $g$ in (1) and the form of (4).
>
> Let $P$ be the perimeter of a cross section. The slice between $x$ and $x + \Delta x$ exposes the area $P\,\Delta x$, so it loses heat to the fluid at the rate $hP\,\Delta x\,(u - U)$. As a generation rate per unit volume (volume $A\,\Delta x$),
>
> $$
> g = -\frac{hP}{A}(u - U) .
> $$
>
> Then (4) becomes
>
> $$
> \frac{\partial^2u}{\partial x^2} - \gamma^2(u - U) = \frac1k\frac{\partial u}{\partial t}, \qquad \gamma^2 = \frac{hP}{\kappa A} .
> $$
>
> Here $g$ depends on $u$, but linearly, so the equation is still linear. This is the equation of [[§18 Steady-State Temperatures#^ex-18-5|Example §18.5]] and [[§19 Example꞉ Fixed End Temperatures#^ex-19-4|Example §19.4]] (with $k = 1$, $U = T$).
>
> *Powers: Exercise 2.1.3*

^ex-17-4

## Diffusion

The same equations have a second, completely different but equally important physical interpretation. Suppose a static medium occupies the slab $0 < x < a$, and another substance, whose molecules or atoms can move (diffuse) through it, has **concentration** $u(x, t)$, measured in mass per unit volume. Let $q(x, t)$ be the **mass flux**, $[q] = m/tL^2$, and $g$ a generation rate, $[g] = m/tL^3$, accounting for any gain or loss of the substance in the layer other than by movement in the $x$-direction. For example, if the substance takes part in a first-order chemical reaction with the medium, at a rate proportional to its concentration, then $g = -k_ru(x, t)$ with a rate constant $k_r$ (Powers writes $k$, equation (19); here $k_r$, to avoid a clash with the diffusivity $k$).

> [!definition] Definition §17.10: Fick's First Law; Diffusivity
> **Fick's first law** relates the concentration and the mass flux; in one dimension,
>
> $$
> q = -D\frac{\partial u}{\partial x} . \qquad (20)
> $$
>
> The diffusing substance moves toward regions of lower concentration at a rate proportional to the concentration gradient. The coefficient $D$, usually constant, is the **diffusivity**.
>
> *Powers: 2.1, Equation (20)*

^def-17-10

> [!theorem] Theorem §17.5: The Diffusion Equation
> Conservation of mass for the layer between $x$ and $x + \Delta x$,
>
> $$
> q(x, t) + \Delta x\,g = q(x + \Delta x, t) + \Delta x\,\frac{\partial u}{\partial t}(x, t) , \qquad (17)
> $$
>
> gives in the limit $\Delta x \to 0$
>
> $$
> -\frac{\partial q}{\partial x} + g = \frac{\partial u}{\partial t} , \qquad (18)
> $$
>
> and with Fick's law (20), the **diffusion equation**
>
> $$
> \frac{\partial^2u}{\partial x^2} + \frac gD = \frac1D\frac{\partial u}{\partial t} . \qquad (21)
> $$
>
> At a boundary the concentration may be controlled, giving a condition like (6), or the flux, giving via Fick's law a condition like (7); an impermeable surface has zero flux. If the boundary $x = a$ is covered with a permeable film, the flux through the film is taken proportional to the difference of the concentrations on its two sides,
>
> $$
> q(a, t) = h\big(u(a, t) - C(t)\big) , \qquad (22)
> $$
>
> where $h$ is the **film coefficient** and $C$ the concentration outside the medium. Then
>
> $$
> -D\frac{\partial u}{\partial x}(a, t) = hu(a, t) - hC(t) , \qquad (23)
> $$
>
> a Robin condition, analogous to (10).
>
> *Powers: 2.1, Equations (17)–(23)*

^thm-17-5

> [!proof]+ Proof
> The argument of [[§17 Derivation and Boundary Conditions#^prop-17-1|Proposition §17.1]] applies with mass in place of heat (per unit area of the layer, so $A$ cancels, and with $\rho c$ replaced by $1$): rearrange (17) as $\frac{q(x, t) - q(x + \Delta x, t)}{\Delta x} + g = u_t$ and let $\Delta x \to 0$ to get (18). Substituting $q = -Du_x$ with $D$ constant gives $Du_{xx} + g = u_t$; divide by $D$ for (21). Finally (23) is (22) with Fick's law $q(a, t) = -Du_x(a, t)$, exactly as in [[§17 Derivation and Boundary Conditions#^prop-17-3|Proposition §17.3]].

^pf-17-5

*Uses:* [[§17 Derivation and Boundary Conditions#^prop-17-1|§17.1]], [[§17 Derivation and Boundary Conditions#^def-17-10|Def. §17.10]], [[§17 Derivation and Boundary Conditions#^prop-17-3|§17.3]]

So everything said about the heat equation, with $k$ replaced by $D$, applies to diffusion, and conversely.
