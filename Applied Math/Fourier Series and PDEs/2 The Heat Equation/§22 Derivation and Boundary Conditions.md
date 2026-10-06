---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 2
section: 22
powers: "2.1"
aliases: ["Powers 2.1"]
tags: [fourier-series-and-pdes, math341]
---
← [[§21 Sawtooth, Triangle Wave, Parabola, Rectified Sine, Sinc Function and Rectangular Pulse]] · ↑ [[· 2 The Heat Equation]] · [[§23 Initial and Boundary Conditions; Diffusion]] →

*Powers, Section 2.1 · MAT 341 lectures 9.17, 9.19 · HW 4.*

This section derives the first partial differential equation of the course, the heat equation $u_{xx} = \frac1k u_t$ for the temperature $u(x, t)$ in a thin rod. Two physical laws go in: conservation of energy, applied to a thin slice of the rod, and Fourier's law, which says that heat flows from hot to cold at a rate proportional to the temperature gradient. The equation alone has infinitely many solutions; the temperature is pinned down by an initial condition and one boundary condition at each end, of Dirichlet (fixed temperature), Neumann (fixed heat flow, in particular insulation) or Robin (convection) type. The same equation, with Fick's law in place of Fourier's, governs diffusion of a substance through a medium.

## The Heat Balance

Consider a rod or bar of heat-conducting material with uniform cross section of area $A$, along the $x$-axis from $x = 0$ to $x = a$. Assume that the temperature does not vary over a cross section, so that it depends only on position $x$ and time $t$. The idea is to apply conservation of energy to the slice of the rod between $x$ and $x + \Delta x$.

> [!definition] Definition §22.1: Heat Flux
> Let $u(x, t)$ be the temperature at position $x$ and time $t$. The **heat flux** $q(x, t)$ is the rate at which heat crosses the section at $x$, per unit area; it is positive when heat flows to the right. Its dimensions are $[q] = H/tL^2$ ($H$ = heat energy, $t$ = time, $L$ = length; square brackets mean "dimension of").
>
> *Powers: 2.1 (text)*

^def-22-1

> [!definition] Definition §22.2: Heat Capacity
> Let $u(x, t)$ be the temperature at position $x$ and time $t$. The material has **density** $\rho$ and **heat capacity** $c$ per unit mass, $[c] = H/mT$ ($m$ = mass, $T$ = temperature). The rate at which heat is stored in a slice of length $\Delta x$ is proportional to the rate of change of temperature: approximately $\rho cA\,\Delta x\,\dfrac{\partial u}{\partial t}(x, t)$.
>
> *Powers: 2.1 (text)*

^def-22-2

> [!definition] Definition §22.3: Generation Rate
> The **generation rate** $g$, $[g] = H/tL^3$, is the rate per unit volume at which heat enters the rod other than by conduction along it: by radiation or convection from a surrounding medium, or by conversion from another form of energy (resistance to an electric current, a chemical or nuclear reaction). A negative $g$ means heat is lost. $g$ may depend on $x$, $t$ and even $u$. The rate of generation in the slice is $A\,\Delta x\,g$.
>
> *Powers: 2.1 (text)*

^def-22-3

The **law of conservation of energy** says that the heat entering a region plus the heat generated inside equals the heat leaving plus the heat stored; it holds equally for rates per unit time. Heat enters the slice through the face at $x$ at the rate $Aq(x, t)$ and leaves through the face at $x + \Delta x$ at the rate $Aq(x + \Delta x, t)$.

> [!theorem] Proposition §28.1: Heat Balance Equation
> If $q$ has a continuous $x$-derivative and $u$ a continuous $t$-derivative, and $g$ is continuous, then at every point of the rod
>
> $$
> -\frac{\partial q}{\partial x} + g = \rho c\frac{\partial u}{\partial t} . \qquad (2)
> $$
>
> *Powers: 2.1, Equation (2)*

^prop-22-1

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

^pf-22-1

*Uses:* [[§22 Derivation and Boundary Conditions#^def-22-1|Def. §22.1]], [[§22 Derivation and Boundary Conditions#^def-22-2|Def. §22.2]], [[§22 Derivation and Boundary Conditions#^def-22-3|Def. §22.3]], [[§49 Average Value of a Function#^thm-49-1|Calc Thm. §49.1]]

![[m341-17-1.svg]]
*The heat balance (1) for the slice between $x$ and $x + \Delta x$ (blue). Heat flows in through the left face at the rate $Aq(x,t)$ and out through the right face at the rate $Aq(x + \Delta x, t)$ (red); inside, heat is generated at the rate $A\,\Delta x\,g$ and stored at the rate $\rho cA\,\Delta x\,u_t$ (green). Nothing crosses the insulated lateral surface; heat lost through it would be counted in $g$.*

> [!remark] Remark: The Same Balance in Integral Form
> The derivation can be run on a whole segment $x_1 < x < x_2$ instead of a thin slice. The heat in the segment is $\int_{x_1}^{x_2} \rho cA\,u\,dx$, and conservation of energy says
>
> $$
> \frac{d}{dt}\int_{x_1}^{x_2} \rho cA\,u\,dx = Aq(x_1, t) - Aq(x_2, t) + \int_{x_1}^{x_2} A\,g\,dx .
> $$
>
> By the [[Fundamental Theorem of Calculus|fundamental theorem of calculus]] the flux difference is a volume integral, $q(x_1, t) - q(x_2, t) = -\int_{x_1}^{x_2} q_x\,dx$, so $\int_{x_1}^{x_2} (\rho c\,u_t + q_x - g)\,dx = 0$ for every segment. A continuous function whose integral over every interval is zero vanishes identically (the one-dimensional case of [[§52 Three-Dimensional Heat Equation#^lem-52-1|Lemma §52.1]]), which is (2) again. In a three-dimensional body $V$ the heat leaving through the boundary is the flux integral $\iint_{\partial V} \mathbf{q}\cdot\mathbf{n}\,dS$, and the divergence theorem turns it into $\iiint_V \nabla\cdot\mathbf{q}\,dV$. The same argument then gives $\rho c\,u_t = -\nabla\cdot\mathbf{q} + g$, and with $\mathbf{q} = -\kappa\nabla u$ the three-dimensional heat equation, [[§52 Three-Dimensional Heat Equation#^thm-52-3|Theorem §52.3]]. In one dimension the divergence theorem is just the fundamental theorem of calculus.

^rem-22-1

> [!remark]- Connections
> - The divergence theorem $\int_{\partial D} \mathbf{u}\cdot\hat n\,dS = \int_D \nabla\cdot\mathbf{u}\,dV$ for bounded domains with piecewise smooth boundary, proved in $\mathbb{R}^n$: [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]]; Stewart's version in $\mathbb{R}^3$: [[§137 The Divergence Theorem#^thm-137-1|Calc Thm. §137.1]].
> - The one-dimensional case, $\int_{x_1}^{x_2} q_x\,dx = q(x_2) - q(x_1)$: [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]].

There are two unknowns, $q$ and $u$, in (2). A second relation between them is needed.

> [!definition] Definition §22.4: Fourier's Law of Heat Conduction
> **Fourier's law** of heat conduction in one dimension is
>
> $$
> q = -\kappa\frac{\partial u}{\partial x} .
> $$
>
> Heat flows downhill: $q$ is positive when $\partial u/\partial x$ is negative, at a rate proportional to the gradient of the temperature. The proportionality factor $\kappa$ is the **thermal conductivity**. It may depend on $x$ if the rod is not uniform, and also on the temperature; usually it is assumed constant.
>
> *Powers: 2.1 (text)*

^def-22-4

> [!definition] Definition §22.5: Thermal Diffusivity
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

^def-22-5

> [!theorem] Theorem §28.2: The Heat Equation
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

^thm-22-2

> [!proof]+ Proof
> Substituting $q = -\kappa\,\partial u/\partial x$ ([[§22 Derivation and Boundary Conditions#^def-22-4|Definition §22.4]]) into (2) gives $-\frac{\partial}{\partial x}\big(-\kappa\frac{\partial u}{\partial x}\big) + g = \rho c\frac{\partial u}{\partial t}$, which is (3). If $\kappa$ is constant it comes out of the derivative, $\kappa u_{xx} + g = \rho c\,u_t$; dividing by $\kappa$ and writing $\rho c/\kappa = 1/k$ gives (4). With $g = 0$, (4) is (5).

^pf-22-2

*Uses:* [[§22 Derivation and Boundary Conditions#^prop-22-1|§22.1]], [[§22 Derivation and Boundary Conditions#^def-22-4|Def. §22.4]], [[§22 Derivation and Boundary Conditions#^def-22-5|Def. §22.5]]

> [!remark] Remark: Solutions Straighten Out
> Some qualitative features can be read off the equation itself. Fix a time $t^*$ and look at the graph of $u(x, t^*)$. Where the graph is concave up (shaped like U, J or a backwards J), $\partial^2u/\partial x^2 > 0$, so by the heat equation $\partial u/\partial t > 0$: the temperature rises there. Where the graph is concave down, $\partial^2u/\partial x^2 < 0$ and the temperature falls. Bumps are filled in and peaks worn down, so a solution of the heat equation tends to straighten out.

^rem-22-2

> [!example] Example §28.1: The Equation Alone Does Not Determine the Temperature
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
> are solutions: in each case $u_{xx} = -\lambda^2u$ and $\frac1k u_t = \frac1k(-\lambda^2k)u = -\lambda^2u$. (These are the building blocks of every solution in [[§25 Example꞉ Fixed End Temperatures|§25]]–[[§28 Example꞉ Convection|§28]].)
>
> So the partial differential equation has infinitely many solutions. This is unsatisfactory both mathematically and physically: the temperature should be uniquely determined. More conditions must be placed on $u$, describing the initial temperature in the rod and what happens at its ends.
>
> *Powers: 2.1 (text) and Exercise 2.1.2*

^ex-22-1

*Continued in [[§23 Initial and Boundary Conditions; Diffusion]]: initial and boundary conditions of Dirichlet, Neumann and Robin type, and diffusion.*
