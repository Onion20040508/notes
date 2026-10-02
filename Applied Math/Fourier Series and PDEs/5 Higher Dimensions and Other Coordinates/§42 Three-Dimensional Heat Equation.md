---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 5
section: 42
powers: "5.2"
aliases: ["Powers 5.2"]
tags: [fourier-series-and-pdes, math341]
---
← [[§41★ Two-Dimensional Wave Equation꞉ Derivation]] · ↑ [[· 5 Higher Dimensions and Other Coordinates]] · [[§43 Two-Dimensional Heat Equation꞉ Solution]] →

*Powers, Section 5.2.*

This section derives the heat equation in a three-dimensional body by vector methods. Conservation of energy is written for an arbitrary piece $\mathcal{V}$ of the body; the divergence theorem turns the heat flowing through its surface into a volume integral; since $\mathcal{V}$ is arbitrary, the integrand must vanish at every point; and Fourier's law $\mathbf{q} = -\kappa\nabla u$ turns the result into $\kappa\nabla^2u + g = \rho c\,u_t$. The argument needs no coordinates, and the same steps give the continuity equation for a fluid, diffusion of a chemical, and conservation of charge. The boundary conditions are the three kinds already met for the rod in [[§17 Derivation and Boundary Conditions|§17]]: prescribed temperature, prescribed heat flux, and convection. The section ends by reducing a three-dimensional problem to a two-dimensional one by averaging over a thin direction.

## Heat Balance for a Subregion

Suppose we are investigating the temperature $u(P, t)$ in a body that occupies a region $\mathcal{R}$ in space, and let $\mathcal{V}$ be a subregion of $\mathcal{R}$ bounded by the surface $\mathcal{S}$, with outward unit normal $\hat{\mathbf{n}}$.

> [!definition] Definition §42.1: Heat Flow, Generation and Storage; the Heat Balance
> - The **heat flow rate** at a point of $\mathcal{R}$ is a vector function $\mathbf{q}(P, t)$, measured in $\mathrm{J/(m^2\,s)}$ or similar units. The rate of heat flow through a small piece of surface of area $\Delta A$ is approximately $\hat{\mathbf{n}}\cdot\mathbf{q}\,\Delta A$, positive for outward flow; the inflow is its negative.
> - The **rate of generation** of heat (conversion from chemical, electrical or nuclear energy) is specified as an intensity $g(P, t)$, in $\mathrm{J/(m^3\,s)}$: heat is generated in a small volume $\Delta V$ about $P$ at the rate $g(P, t)\,\Delta V$.
> - The **storage rate** in a small volume $\Delta V$ about $P$ is proportional to the rate at which the temperature changes there: $\rho c\,\Delta V\,u_t(P, t)$, where $\rho$ is the density and $c$ the specific heat.
>
> Summing over $\mathcal{V}$ and passing to integrals, the law of conservation of energy for $\mathcal{V}$, *net rate of heat in + rate of generation inside = rate of accumulation*, reads
>
> $$
> \iint_{\mathcal{S}} -\mathbf{q}\cdot\hat{\mathbf{n}}\,dA + \iiint_{\mathcal{V}} g\,dV = \iiint_{\mathcal{V}} \rho c\,\frac{\partial u}{\partial t}\,dV . \qquad (1)
> $$
>
> *Powers: 5.2 (text), Equation (1)*

^def-42-1

In this section $c$ is the specific heat, not a wave speed; $\rho c$ is the heat capacity per unit volume.

> [!theorem] Lemma §42.1: A Continuous Function with Zero Integral over Every Subregion Is Zero
> Let $F$ be continuous on $\mathcal{R}$. If $\iiint_{\mathcal{V}} F\,dV = 0$ for every subregion $\mathcal{V}$ of $\mathcal{R}$, then $F = 0$ at every point of $\mathcal{R}$.
>
> *Powers: 5.2 (text)*

^lem-42-1

> [!proof]+ Proof
> If $F$ were not identically $0$, there would be a subregion of $\mathcal{R}$ throughout which it is positive (or negative), and its integral over that subregion would be positive (or negative), a contradiction. (Powers asserts the existence of such a subregion; here is why.) Suppose $F(P_0) > 0$ at a point $P_0$ of $\mathcal{R}$. By continuity there is a small ball $B$ about $P_0$, inside $\mathcal{R}$, on which $F > F(P_0)/2$. Then by the comparison theorem for integrals
>
> $$
> \iiint_B F\,dV \ge \frac{F(P_0)}{2}\,\mathrm{vol}(B) > 0 ,
> $$
>
> contradicting the hypothesis with $\mathcal{V} = B$. The case $F(P_0) < 0$ is the same with $-F$.

^pf-42-1

*Uses:* [[§15 Multivariable Integration#^thm-15-5|452 Thm. §15.5]] (comparison theorem; stated there for double integrals, the same for triple integrals)

> [!theorem] Theorem §42.2: The Local Heat Balance
> If $\mathbf{q}$ is continuously differentiable and $u_t$ and $g$ are continuous, the heat balance (1) for every subregion $\mathcal{V}$ implies
>
> $$
> -\nabla\cdot\mathbf{q} + g - \rho c\,\frac{\partial u}{\partial t} = 0 \qquad \text{in } \mathcal{R}, \quad 0 < t . \qquad (4)
> $$
>
> *Powers: 5.2, Equation (4)*

^thm-42-2

> [!proof]+ Proof
> By the divergence theorem, the integral over a closed surface $\mathcal{S}$ of the outward normal component of a vector function equals the integral over the volume bounded by $\mathcal{S}$ of its divergence:
>
> $$
> \iint_{\mathcal{S}} \mathbf{q}\cdot\hat{\mathbf{n}}\,dA = \iiint_{\mathcal{V}} \nabla\cdot\mathbf{q}\,dV . \qquad (2)
> $$
>
> Make this replacement in (1) and collect all terms on one side:
>
> $$
> \iiint_{\mathcal{V}} \Big[-\nabla\cdot\mathbf{q} + g - \rho c\,\frac{\partial u}{\partial t}\Big]\,dV = 0 . \qquad (3)
> $$
>
> The integrand is continuous by the hypotheses, and (3) holds for every subregion $\mathcal{V}$. By Lemma §42.1 the integrand is $0$ at every point, which is (4).

^pf-42-2

*Uses:* [[§42 Three-Dimensional Heat Equation#^def-42-1|Def. §42.1]], [[§42 Three-Dimensional Heat Equation#^lem-42-1|§42.1]], [[§18 Surface Integrals#^thm-18-2|452 Thm. §18.2]] (divergence theorem)

> [!remark]- Connections
> - The divergence theorem in $\mathbb{R}^3$: [[§18 Surface Integrals#^thm-18-2|452 Thm. §18.2]] (proved there for simple solid regions), in $\mathbb{R}^n$ [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1|452 Thm. §17.1]]; Stewart's version with worked flux computations, [[§115 The Divergence Theorem#^thm-115-1|Calc Thm. §115.1]].
> - 452 derives the continuity equation $\rho_t + \nabla\cdot(\rho\mathbf{u}) = 0$ by exactly this argument, with mass in place of heat and no source term: [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-4|452 Thm. §17.4]].

> [!definition] Definition §42.2: Fourier's Law of Heat Conduction
> In an **isotropic** solid (same properties in all directions), the heat flow rate is negatively proportional to the temperature gradient:
>
> $$
> \mathbf{q} = -\kappa\nabla u . \qquad (5)
> $$
>
> The constant $\kappa > 0$ is the **thermal conductivity**. The minus sign makes heat flow "downhill", from hotter to colder regions: $\nabla u$ points in the direction in which $u$ increases fastest.
>
> *Powers: 5.2, Equation (5)*

^def-42-2

> [!theorem] Theorem §42.3: The Three-Dimensional Heat Equation
> If Fourier's law (5) holds with constant conductivity $\kappa$, the temperature satisfies
>
> $$
> \kappa\nabla^2u + g = \rho c\,\frac{\partial u}{\partial t} \qquad \text{in } \mathcal{R}, \quad 0 < t . \qquad (6)
> $$
>
> With no generation ($g = 0$) and the diffusivity $k = \kappa/(\rho c)$, this is $\nabla^2u = \frac{1}{k}\frac{\partial u}{\partial t}$.
>
> *Powers: 5.2, Equation (6)*

^thm-42-3

> [!proof]+ Proof
> Substitute (5) into (4). Since $\kappa$ is constant, $\nabla\cdot\mathbf{q} = \nabla\cdot(-\kappa\nabla u) = -\kappa\,\nabla\cdot\nabla u = -\kappa\nabla^2u$, so (4) becomes $\kappa\nabla^2u + g - \rho c\,u_t = 0$, which is (6). Dividing by $\kappa$ with $g = 0$ gives $\nabla^2u = (\rho c/\kappa)\,u_t = u_t/k$.

^pf-42-3

*Uses:* [[§42 Three-Dimensional Heat Equation#^thm-42-2|§42.2]], [[§42 Three-Dimensional Heat Equation#^def-42-2|Def. §42.2]], [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-2|452 Def. §17.2]] ($\nabla^2 = \nabla\cdot\nabla$)

> [!remark]- Connections
> - The one-dimensional case, derived for a rod with $q$ a scalar and Fourier's law $q = -\kappa u_x$ ([[§17 Derivation and Boundary Conditions#^def-17-2|Definition §17.2]]): [[§17 Derivation and Boundary Conditions#^thm-17-2|Theorem §17.2]]. In a rod $\nabla^2u = u_{xx}$ and (6) reduces to the heat equation there.
> - The Laplacian $\nabla^2 = \nabla\cdot\nabla$: [[§111 Curl and Divergence#^def-111-5|Calc Def. §111.5]]; that the gradient points in the direction of fastest increase, which the minus sign in (5) reverses: [[§95 Directional Derivatives and the Gradient Vector#^thm-95-4|Calc Thm. §95.4]].

> [!remark] Remark: Units
> In SI units $\kappa$ is in $\mathrm{J/(m\,s\,K)}$, $\rho$ in $\mathrm{kg/m^3}$ and $c$ in $\mathrm{J/(kg\,K)}$, so $\rho c$ is in $\mathrm{J/(m^3\,K)}$ and the diffusivity $k = \kappa/(\rho c)$ is in $\mathrm{m^2/s}$. Each term of (6) is then in $\mathrm{J/(m^3\,s)}$, a rate of heat per unit volume: $\kappa\nabla^2u$ because $\nabla^2u$ is in $\mathrm{K/m^2}$, and $g$ and $\rho c\,u_t$ directly (Powers' Exercise 5.2.4).

^rem-42-1

## Initial and Boundary Conditions

> [!definition] Definition §42.3: Initial and Boundary Conditions for the Heat Equation
> The heat equation (6) is accompanied by an **initial condition**
>
> $$
> u(P, 0) = f(P) \qquad \text{for } P \text{ in } \mathcal{R} , \qquad (7)
> $$
>
> and, at every point of the surface $\mathcal{B}$ bounding $\mathcal{R}$, some **boundary condition**. Commonly one of the following is given on $\mathcal{B}$ or on a portion $\mathcal{B}'$ of it.
> 1. **Temperature specified:** $u(P, t) = h_1(P, t)$ for $P$ in $\mathcal{B}'$, $h_1$ a given function.
> 2. **Heat flow rate specified.** The outward heat flow rate through a small piece of surface about $P$ on $\mathcal{B}'$ is $\mathbf{q}(P, t)\cdot\hat{\mathbf{n}}$ times its area. By Fourier's law, controlling it controls $\nabla u\cdot\hat{\mathbf{n}}$, the directional derivative of $u$ in the outward normal direction, so
>
>    $$
>    \frac{\partial u}{\partial n}(P, t) = h_2(P, t) \qquad \text{for } P \text{ on } \mathcal{B}' , \qquad (8)
>    $$
>
>    with $h_2$ given. An **insulated** surface has $h_2 = 0$.
> 3. **Convection.** If part of the surface is exposed to a fluid at temperature $T(P, t)$, an accounting of the energy passing through a small piece of surface about $P$ gives $\mathbf{q}(P, t)\cdot\hat{\mathbf{n}} = h\big(u(P, t) - T(P, t)\big)$, with $h$ the heat transfer coefficient. By Fourier's law,
>
>    $$
>    \kappa\frac{\partial u}{\partial n}(P, t) + h\,u(P, t) = h\,T(P, t) \qquad \text{for } P \text{ on } \mathcal{B}' . \qquad (9)
>    $$
>
> *Powers: 5.2 (text), Equations (7)–(9)*

^def-42-3

These are the three-dimensional forms of the conditions of the first, second and third kinds for the rod ([[§17 Derivation and Boundary Conditions#^def-17-5|Definition §17.5]], [[§17 Derivation and Boundary Conditions#^def-17-6|Definition §17.6]], [[§17 Derivation and Boundary Conditions#^def-17-7|Definition §17.7]]). The normal derivative is $\partial u/\partial n = \nabla u\cdot\hat{\mathbf{n}}$, the directional derivative as a dot product ([[§95 Directional Derivatives and the Gradient Vector#^cor-95-2|Calc Cor. §95.2]]). On a face where the outward normal is $-\mathbf{k}$, for instance, $\partial u/\partial n = -\partial u/\partial z$.

## Examples: A Rectangular Block and Its Reductions

> [!example] Example §42.1: Heat Conduction in a Rectangular Block
> Set up the three-dimensional problem for a solid in the form of a rectangular parallelepiped $0 < x < a$, $0 < y < b$, $0 < z < c$, with no generation inside, if the faces $x = 0$ and $x = a$ are held at temperatures $T_0$ and $T_1$, the top and bottom are insulated, and the faces $y = 0$ and $y = b$ are exposed to a fluid at temperature $T_2$.
>
> Cartesian coordinates are appropriate. With $g = 0$, (6) is
>
> $$
> \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} = \frac{1}{k}\frac{\partial u}{\partial t}, \qquad 0 < x < a, \quad 0 < y < b, \quad 0 < z < c, \quad 0 < t . \qquad (10)
> $$
>
> **Controlled faces** (condition 1):
>
> $$
> u(0, y, z, t) = T_0, \quad u(a, y, z, t) = T_1, \qquad 0 < y < b, \quad 0 < z < c, \quad 0 < t . \qquad (11)
> $$
>
> **Insulated top and bottom** (condition 2 with $h_2 = 0$). The outward normals on the bottom $z = 0$ and the top $z = c$ are the negative and positive $z$-directions, so $\partial u/\partial n = \mp\partial u/\partial z$, and either way
>
> $$
> \frac{\partial u}{\partial z}(x, y, 0, t) = 0, \quad \frac{\partial u}{\partial z}(x, y, c, t) = 0, \qquad 0 < x < a, \quad 0 < y < b, \quad 0 < t . \qquad (12)
> $$
>
> **Convecting faces** (condition 3). At $y = 0$ the outward normal is $-\mathbf{j}$, so $\partial u/\partial n = -\partial u/\partial y$; at $y = b$ it is $+\mathbf{j}$. By (9),
>
> $$
> \begin{aligned}
> -\kappa\frac{\partial u}{\partial y}(x, 0, z, t) + h\,u(x, 0, z, t) &= hT_2, \\
> \kappa\frac{\partial u}{\partial y}(x, b, z, t) + h\,u(x, b, z, t) &= hT_2,
> \end{aligned} \qquad 0 < x < a, \quad 0 < z < c, \quad 0 < t . \qquad (13)
> $$
>
> **Initial condition:**
>
> $$
> u(x, y, z, 0) = f(x, y, z), \qquad 0 < x < a, \quad 0 < y < b, \quad 0 < z < c . \qquad (14)
> $$
>
> The sign difference in (13) is the point to watch: in both cases heat flows out when the face is hotter than the fluid.
>
> *Powers: 5.2 (text), Equations (10)–(14)*

^ex-42-1

A full three-dimensional problem is complicated to solve, so one looks for ways to reduce it to two or even one dimension. Here $c$ is the height of the block.

> [!example] Example §42.2: Averaging over the Height
> For the solution $u$ of (10)–(14), let $v$ be the temperature averaged over $0 < z < c$:
>
> $$
> v(x, y, t) = \frac{1}{c}\int_0^c u(x, y, z, t)\,dz .
> $$
>
> Show that $v$ satisfies the two-dimensional heat equation, and find its boundary and initial conditions.
>
> **The $z$-term drops out.** By the fundamental theorem of calculus and the insulation conditions (12),
>
> $$
> \int_0^c \frac{\partial^2 u}{\partial z^2}\,dz = \frac{\partial u}{\partial z}(x, y, c, t) - \frac{\partial u}{\partial z}(x, y, 0, t) = 0 .
> $$
>
> **The equation.** Differentiation with respect to $x$, $y$ or $t$ gives the same result inside or outside the integral with respect to $z$ (for smooth $u$). So averaging (10) over $z$ gives
>
> $$
> \frac{1}{c}\int_0^c \Big(\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2}\Big)dz = \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} \quad\text{and}\quad \frac{1}{c}\int_0^c \frac{1}{k}\frac{\partial u}{\partial t}\,dz = \frac{1}{k}\frac{\partial v}{\partial t} ,
> $$
>
> and $v$ satisfies the two-dimensional heat equation
>
> $$
> \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} = \frac{1}{k}\frac{\partial v}{\partial t}, \qquad 0 < x < a, \quad 0 < y < b, \quad 0 < t .
> $$
>
> **Boundary and initial conditions.** Averaging (11), (13) and (14) over $z$, term by term:
>
> $$
> \begin{aligned}
> &v(0, y, t) = T_0, \quad v(a, y, t) = T_1, && 0 < y < b, \quad 0 < t, \\
> &-\kappa\frac{\partial v}{\partial y}(x, 0, t) + h\,v(x, 0, t) = hT_2, \quad \kappa\frac{\partial v}{\partial y}(x, b, t) + h\,v(x, b, t) = hT_2, && 0 < x < a, \quad 0 < t, \\
> &v(x, y, 0) = \frac{1}{c}\int_0^c f(x, y, z)\,dz, && 0 < x < a, \quad 0 < y < b .
> \end{aligned}
> $$
>
> The conditions are linear with coefficients independent of $z$, so averaging passes through them exactly: no approximation is made. The averaged problem is a two-dimensional heat problem in a rectangle; with fixed edge temperatures such a problem is solved in [[§43 Two-Dimensional Heat Equation꞉ Solution#^thm-43-4|Theorem §43.4]] and [[§43 Two-Dimensional Heat Equation꞉ Solution#^rem-43-1|the method remark of §43]].
>
> *Powers: 5.2 (text); Exercises 5.2.1 and 5.2.2*

^ex-42-2

> [!example] Example §42.3: A Thin Plate Cooled on Its Faces
> If the $z$-variation cannot be ignored but the block is thin in the $y$-direction (a plate parallel to the $xz$-plane, with its broad faces $y = 0$, $y = b$ convecting), average in that direction instead:
>
> $$
> w(x, z, t) = \frac{1}{b}\int_0^b u(x, y, z, t)\,dy .
> $$
>
> **The $y$-term.** This time the boundary conditions (13) at the ends of the interval of integration do not make the integral vanish. Solving (13) for the derivatives, $\frac{\partial u}{\partial y}(x, b, z, t) = \frac{h}{\kappa}\big(T_2 - u(x, b, z, t)\big)$ and $\frac{\partial u}{\partial y}(x, 0, z, t) = -\frac{h}{\kappa}\big(T_2 - u(x, 0, z, t)\big)$, so
>
> $$
> \int_0^b \frac{\partial^2 u}{\partial y^2}\,dy = \frac{\partial u}{\partial y}(x, b, z, t) - \frac{\partial u}{\partial y}(x, 0, z, t) = \frac{h}{\kappa}\Big[\big(T_2 - u(x, b, z, t)\big) + \big(T_2 - u(x, 0, z, t)\big)\Big] .
> $$
>
> **The thin-plate approximation.** If $b$ is small, the temperature hardly varies across the plate, and we may accept the approximation $u(x, b, z, t) + u(x, 0, z, t) \cong 2w(x, z, t)$. Then
>
> $$
> \frac{1}{b}\int_0^b \frac{\partial^2 u}{\partial y^2}\,dy \cong \frac{2h}{b\kappa}\big(T_2 - w(x, z, t)\big) .
> $$
>
> Averaging (10), (11), (12) and (14) over $y$ gives the two-dimensional problem
>
> $$
> \begin{aligned}
> &\frac{\partial^2 w}{\partial x^2} + \frac{\partial^2 w}{\partial z^2} + \frac{2h}{b\kappa}(T_2 - w) = \frac{1}{k}\frac{\partial w}{\partial t}, && 0 < x < a, \quad 0 < z < c, \quad 0 < t, && (15) \\
> &w(0, z, t) = T_0, \quad w(a, z, t) = T_1, && 0 < z < c, \quad 0 < t, && (16) \\
> &\frac{\partial w}{\partial z}(x, 0, t) = 0, \quad \frac{\partial w}{\partial z}(x, c, t) = 0, && 0 < x < a, \quad 0 < t, && (17) \\
> &w(x, z, 0) = \frac{1}{b}\int_0^b f(x, y, z)\,dy, && 0 < x < a, \quad 0 < z < c . && (18)
> \end{aligned}
> $$
>
> The convection through the faces has become a heat loss term $\frac{2h}{b\kappa}(T_2 - w)$ in the equation, the same kind of term as for a rod losing heat through its lateral surface, $u_{xx} - \gamma^2(u - U) = u_t/k$ ([[§17 Derivation and Boundary Conditions#^ex-17-4|Example §17.4]]).
>
> **Steady state.** Suppose $w(x, z, t) \to W(x, z)$ as $t \to \infty$. Then $W$ satisfies (15)–(17) with $\partial w/\partial t = 0$. Nothing in that problem depends on $z$, so look for $W = W(x)$; (17) then holds automatically, and with $\gamma^2 = 2h/(b\kappa)$
>
> $$
> W'' - \gamma^2(W - T_2) = 0, \quad 0 < x < a, \qquad W(0) = T_0, \quad W(a) = T_1 .
> $$
>
> The function $W - T_2$ solves $y'' = \gamma^2 y$, whose solutions are combinations of $\sinh\gamma x$ and $\sinh\gamma(a - x)$. Matching the end values,
>
> $$
> W(x) = T_2 + \frac{(T_0 - T_2)\sinh\gamma(a - x) + (T_1 - T_2)\sinh\gamma x}{\sinh\gamma a} .
> $$
>
> Check: at $x = 0$ the fraction is $T_0 - T_2$, so $W(0) = T_0$; at $x = a$ it is $T_1 - T_2$, so $W(a) = T_1$. This is the steady state of the rod with lateral convection ([[§18 Steady-State Temperatures#^ex-18-5|Example §18.5]]), with $U = T_2$. It is a cooling fin: between the held ends the plate's temperature sags toward the fluid temperature $T_2$, the more so the larger $\gamma a$ (thin plate, good convection, poor conduction).
>
> *Powers: 5.2 (text), Equations (15)–(18); Exercise 5.2.3*

^ex-42-3
