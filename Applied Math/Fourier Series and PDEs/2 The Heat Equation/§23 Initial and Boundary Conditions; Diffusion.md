---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 2
section: 23
powers: "2.1"
aliases: ["Powers 2.1 (cont.)"]
tags: [fourier-series-and-pdes, math341]
---
← [[§22 Derivation and Boundary Conditions]] · ↑ [[· 2 The Heat Equation]] · [[§24 Steady-State Temperatures]] →

*Powers, Section 2.1 · MAT 341 lectures 9.17, 9.19 · HW 4.*

The heat equation alone ([[§22 Derivation and Boundary Conditions|§22]]) has infinitely many solutions; the temperature is pinned down by an initial condition and one boundary condition at each end, of Dirichlet (fixed temperature), Neumann (fixed heat flow, in particular insulation) or Robin (convection) type. The same equation, with Fick's law in place of Fourier's, governs diffusion of a substance through a medium.

## Initial and Boundary Conditions

> [!definition] Definition §29.2: Initial Condition
> The **initial condition** specifies the temperature at every point of the rod at the start:
>
> $$
> u(x, 0) = f(x), \qquad 0 < x < a ,
> $$
>
> where $f(x)$ is a given function of $x$ alone.
>
> *Powers: 2.1 (text)*

^def-23-1

The **boundary conditions** describe what happens at the ends. Let $x_0$ denote an endpoint, $0$ or $a$.

> [!definition] Definition §23.2: Dirichlet Condition
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

^def-23-2

> [!definition] Definition §23.3: Neumann Condition; Insulated End
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

^def-23-3

> [!definition] Definition §23.4: Robin Condition
> A **Robin condition**, or **condition of the third kind**, is
>
> $$
> c_1u(x_0, t) + c_2\frac{\partial u}{\partial x}(x_0, t) = \gamma(t) , \qquad (8)
> $$
>
> a linear combination of the temperature and its gradient at the boundary.
>
> *Powers: 2.1, Equation (8)*

^def-23-4

> [!theorem] Proposition §29.1: Convection Gives a Robin Condition
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

^prop-23-1

> [!proof]+ Proof
> The heat conducted up to the surface from inside the rod is carried away by convection, so the conducted flux $q(a, t)$ equals the convective flux (9). By Fourier's law ([[§22 Derivation and Boundary Conditions#^def-22-4|Definition §22.4]]), $q(a, t) = -\kappa u_x(a, t)$; substituting in (9) gives (10). Moving $hu(a, t)$ to the left, $hu(a, t) + \kappa u_x(a, t) = hT(t)$, which is (8).

^pf-23-1

*Uses:* [[§22 Derivation and Boundary Conditions#^def-22-4|Def. §22.4]], [[§23 Initial and Boundary Conditions; Diffusion#^def-23-4|Def. §23.4]]

> [!remark]- Connections
> - Newton's law of cooling for a body of uniform temperature, $dT/dt = k(T - T_s)$, and its exponential solution: [[§24 Exponential Growth and Decay#^def-24-4|Calc Def. §24.4]], [[§24 Exponential Growth and Decay#^cor-24-2|Calc Cor. §24.2]], [[§7 Modeling with First-Order Differential Equations#^ex-7-5|331 Ex. §7.5]]. Here the same law acts only at the surface, and the interior is governed by conduction.

> [!definition] Definition §23.5: Mixed Boundary Conditions
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

^def-23-5

Many other kinds of boundary conditions exist and are even realizable, but these four are the most common. All four involve a **linear** operation on the function $u$; this is what the method of [[§25 Example꞉ Fixed End Temperatures|§25]] relies on, through the principle of superposition ([[§25 Example꞉ Fixed End Temperatures#^thm-25-4|Theorem §25.4]]).

> [!definition] Definition §23.6: Initial Value–Boundary Value Problem
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

^def-23-6

> [!theorem] Theorem §29.2: Existence and Uniqueness
> A complete initial value–boundary value problem for the heat equation, such as (13)–(16), has one, and only one, solution.
>
> *Powers: 2.1 (text)*

^thm-23-2

*Powers omits the proof.*

> [!remark] Remark: Rods and Slabs
> The heat equation was derived for a "rod", an object much longer than it is wide. It applies equally to a "slab", an object much wider than it is thick. What matters is that the temperature varies in only one space direction (along the rod, or through the thickness of the slab). The multidimensional heat equation is derived in [[§52 Three-Dimensional Heat Equation#^thm-52-3|Theorem §52.3]].

^rem-23-3

> [!example] Example §29.1: Reading Off the Boundary Conditions
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

^ex-23-1

> [!example] Example §29.2: Convection at the Left End
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

^ex-23-2

> [!example] Example §29.3: Convection Through the Lateral Surface
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
> Here $g$ depends on $u$, but linearly, so the equation is still linear. This is the equation of [[§24 Steady-State Temperatures#^ex-24-5|Example §24.5]] and [[§25 Example꞉ Fixed End Temperatures#^ex-25-4|Example §25.4]] (with $k = 1$, $U = T$).
>
> *Powers: Exercise 2.1.3*

^ex-23-3

## Diffusion

The same equations have a second, completely different but equally important physical interpretation. Suppose a static medium occupies the slab $0 < x < a$, and another substance, whose molecules or atoms can move (diffuse) through it, has **concentration** $u(x, t)$, measured in mass per unit volume. Let $q(x, t)$ be the **mass flux**, $[q] = m/tL^2$, and $g$ a generation rate, $[g] = m/tL^3$, accounting for any gain or loss of the substance in the layer other than by movement in the $x$-direction. For example, if the substance takes part in a first-order chemical reaction with the medium, at a rate proportional to its concentration, then $g = -k_ru(x, t)$ with a rate constant $k_r$ (Powers writes $k$, equation (19); here $k_r$, to avoid a clash with the diffusivity $k$).

> [!definition] Definition §23.7: Fick's First Law; Diffusivity
> **Fick's first law** relates the concentration and the mass flux; in one dimension,
>
> $$
> q = -D\frac{\partial u}{\partial x} . \qquad (20)
> $$
>
> The diffusing substance moves toward regions of lower concentration at a rate proportional to the concentration gradient. The coefficient $D$, usually constant, is the **diffusivity**.
>
> *Powers: 2.1, Equation (20)*

^def-23-7

> [!theorem] Theorem §29.3: The Diffusion Equation
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

^thm-23-3

> [!proof]+ Proof
> The argument of [[§22 Derivation and Boundary Conditions#^prop-22-1|Proposition §22.1]] applies with mass in place of heat (per unit area of the layer, so $A$ cancels, and with $\rho c$ replaced by $1$): rearrange (17) as $\frac{q(x, t) - q(x + \Delta x, t)}{\Delta x} + g = u_t$ and let $\Delta x \to 0$ to get (18). Substituting $q = -Du_x$ with $D$ constant gives $Du_{xx} + g = u_t$; divide by $D$ for (21). Finally (23) is (22) with Fick's law $q(a, t) = -Du_x(a, t)$, exactly as in [[§23 Initial and Boundary Conditions; Diffusion#^prop-23-1|Proposition §23.1]].

^pf-23-3

*Uses:* [[§22 Derivation and Boundary Conditions#^prop-22-1|§22.1]], [[§23 Initial and Boundary Conditions; Diffusion#^def-23-7|Def. §23.7]], [[§23 Initial and Boundary Conditions; Diffusion#^prop-23-1|§23.1]]

So everything said about the heat equation, with $k$ replaced by $D$, applies to diffusion, and conversely.
