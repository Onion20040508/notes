---
type: section
subject: "[[Complex Variables]]"
chapter: 10
section: "124★"
bc: "124"
aliases: ["B&C 124"]
tags: [complex-variables, math342, extension]
---
← [[§123★ Examples (Electrostatic Potential)]] · ↑ [[· 10★ Applications of Conformal Mapping]] · [[§125★ The Stream Function]] →

*Brown–Churchill, Section 124 (with Exercise 8 of Section 126).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

The third interpretation of harmonic functions: steady two-dimensional flow of an ideal fluid. The velocity is written as a complex number $V = p + iq$. Its circulation around a closed curve measures how much the fluid swirls, and by Green's theorem the swirl per unit area at a point is the rotation $\omega = \frac12(q_x - p_y)$. In an irrotational flow on a simply connected domain the velocity is the gradient of a single-valued velocity potential (the line-integral construction of [[§115★ Harmonic Conjugates#^lem-115-3|Lemma §115.3]] again), and if the fluid is incompressible this potential is harmonic. [[§125★ The Stream Function|§125]] adds a harmonic conjugate, the stream function, and with it the complex potential.

## Circulation and Rotation

We consider steady two-dimensional flow: the motion is the same in all planes parallel to the $xy$ plane, with velocity parallel to that plane and independent of time, so it suffices to consider a sheet of fluid in the $xy$ plane. The complex number
$$
V = p + iq
$$
represents the velocity of the fluid at $(x, y)$; its components are $p(x, y)$ and $q(x, y)$. At points interior to a region of flow without sources or sinks, $p$ and $q$ and their first-order partial derivatives are assumed continuous.

> [!definition] Definition §124.1: Circulation
> The **circulation** of the fluid along a contour $C$ is the line integral, with respect to arc length $\sigma$, of the tangential component $V_T(x, y)$ of the velocity along $C$:
>
> $$
> \int_C V_T(x, y)\,d\sigma . \qquad (1)
> $$
>
> The circulation divided by the length of $C$ is a mean speed of the fluid along $C$.
>
> *B&C: Sec. 124 (text)*

^def-124-1

> [!theorem] Proposition §124.1: Circulation as a Line Integral, and by Green's Theorem
> For any contour $C$,
>
> $$
> \int_C V_T(x, y)\,d\sigma = \int_C p(x, y)\,dx + q(x, y)\,dy . \qquad (2)
> $$
>
> If $C$ is a positively oriented simple closed contour lying in a simply connected domain of flow containing no sources or sinks, and $R$ is the closed region consisting of $C$ and its interior, then
>
> $$
> \int_C V_T(x, y)\,d\sigma = \iint_R \big[q_x(x, y) - p_y(x, y)\big]\,dA . \qquad (3)
> $$
>
> *B&C: Sec. 124, Equations (2) and (3)*

^prop-124-1

> [!proof]+ Proof
> B&C refers (2) to advanced calculus; here is why. On each smooth piece of $C$ use arc length $\sigma$ as parameter, $z = x(\sigma) + iy(\sigma)$; the unit tangent is $\mathbf T = (x'(\sigma), y'(\sigma))$, so $V_T = (p, q)\cdot\mathbf T = p\,x'(\sigma) + q\,y'(\sigma)$ and
>
> $$
> \int_C V_T\,d\sigma = \int\big[p\,x'(\sigma) + q\,y'(\sigma)\big]\,d\sigma = \int_C p\,dx + q\,dy ,
> $$
>
> the line integral of the field $(p, q)$ in component form ([[§127 Line Integrals of Vector Fields#^thm-127-2|Calc Thm. §127.2]]); summing over the pieces gives (2) for a contour. For (3), apply Green's theorem ([[§130 Green's Theorem#^thm-130-1|Calc Thm. §130.1]]; B&C's version is in [[§50 Cauchy–Goursat Theorem|§50]]) to $P = p$, $Q = q$, which have continuous first partials on an open set containing $R$ (no sources or sinks, and $R$ lies in the domain because it is simply connected).

^pf-124-1

*Uses:* [[§124★ Two-Dimensional Fluid Flow#^def-124-1|Def. §124.1]], [[§127 Line Integrals of Vector Fields#^def-127-2|Calc Def. §127.2]], [[§127 Line Integrals of Vector Fields#^thm-127-2|Calc Thm. §127.2]], [[§130 Green's Theorem#^thm-130-1|Calc Thm. §130.1]] (Green's theorem), [[§52 Simply Connected Domains#^def-52-1|Def. §52.1]]

> [!definition] Definition §124.2: Rotation; Irrotational Flow
> The function
>
> $$
> \omega(x, y) = \frac12\big[q_x(x, y) - p_y(x, y)\big] \qquad (4)
> $$
>
> is the **rotation** of the fluid. If $\omega(x, y) = 0$ at each point of a simply connected domain, the flow is **irrotational** in that domain.
>
> *B&C: Sec. 124 (text)*

^def-124-2

> [!definition] Definition §124.5: Incompressible Fluid
> A fluid is **incompressible** if its density does not change.
>
> *B&C: Sec. 124 (text)*

^def-124-3

> [!definition] Definition §124.4: Inviscid Fluid
> A fluid is **free from viscosity** (inviscid) if it has no internal friction.
>
> *B&C: Sec. 124 (text)*

^def-124-4

From here on all flows are irrotational, of incompressible, inviscid fluids of uniform density $\rho$.

> [!theorem] Proposition §124.2: The Rotation Is a Limiting Angular Speed
> Let $C_r$ be the circle of radius $r$ about $(x_0, y_0)$, taken counterclockwise, inside a simply connected domain of flow without sources or sinks. The mean angular speed of the fluid about $(x_0, y_0)$ along $C_r$, that is, the circulation divided by $2\pi r$ (a mean speed) and then by $r$, satisfies
>
> $$
> \frac{1}{2\pi r^2}\int_{C_r} V_T\,d\sigma = \frac{1}{\pi r^2}\iint_{R_r}\frac12\big[q_x - p_y\big]\,dA \longrightarrow \omega(x_0, y_0) \qquad (r \to 0),
> $$
>
> where $R_r$ is the disk bounded by $C_r$. So $\omega(x, y)$ is the limiting angular speed of a circular element of fluid as the circle shrinks to its center.
>
> *B&C: Sec. 124 (text)*

^prop-124-2

> [!proof]+ Proof
> The equality is (3) divided by $2\pi r^2$. The right side is the mean value of the continuous function $\omega$ over the disk $R_r$ of area $\pi r^2$. Given $\varepsilon > 0$, continuity gives $\delta > 0$ with $|\omega(x, y) - \omega(x_0, y_0)| < \varepsilon$ on $R_r$ for $r < \delta$, and then
>
> $$
> \Big|\frac{1}{\pi r^2}\iint_{R_r}\omega\,dA - \omega(x_0, y_0)\Big| = \Big|\frac{1}{\pi r^2}\iint_{R_r}\big(\omega - \omega(x_0, y_0)\big)\,dA\Big| \le \varepsilon .
> $$

^pf-124-2

*Uses:* [[§124★ Two-Dimensional Fluid Flow#^prop-124-1|§124.1]], [[§124★ Two-Dimensional Fluid Flow#^def-124-2|Def. §124.2]]

> [!remark]- Connections
> - In vector language, $2\omega$ is the $\mathbf k$ component of $\operatorname{curl}(p, q, 0)$, and Proposition §124.2 is the planar case of curl as circulation per unit area, [[§136 Stokes' Theorem#^thm-136-3|Calc Thm. §136.3]]; "irrotational" is [[§132 Curl and Divergence#^def-132-2|Calc Def. §132.2]] and [[§13 The Three Differential Operators꞉ Gradient, Curl, Divergence#^def-13-2|452 Def. §13.2]].

Under these assumptions it can be shown that the fluid pressure $P(x, y)$ satisfies a special case of **Bernoulli's equation**.

> [!theorem] Proposition §124.3: Bernoulli's Equation
> In a steady irrotational flow of an inviscid fluid of uniform density $\rho$, the pressure $P(x, y)$ satisfies
>
> $$
> \frac P\rho + \frac12|V|^2 = c ,
> $$
>
> where $c$ is a constant. In particular the pressure is greatest where the speed $|V|$ is least.
>
> *B&C: Sec. 124 (text)*

^prop-124-3

*B&C omits the proof (it is a law of fluid mechanics, derived from Newton's second law for the fluid).*

## The Velocity Potential

> [!theorem] Theorem §124.4: Existence of a Velocity Potential
> Let $D$ be a simply connected domain in which the flow is irrotational, and $(x_0, y_0)$ a fixed point of $D$. Then the line integral
>
> $$
> \phi(x, y) = \int_{(x_0, y_0)}^{(x, y)} p(s, t)\,ds + q(s, t)\,dt \qquad (5)
> $$
>
> is independent of the contour in $D$, defines a single-valued function on $D$, and
>
> $$
> \phi_x(x, y) = p(x, y), \qquad \phi_y(x, y) = q(x, y) . \qquad (6)
> $$
>
> A different reference point $(x_0, y_0)$ changes $\phi$ by an additive constant.
>
> *B&C: Sec. 124 (text)*

^thm-124-4

> [!proof]+ Proof
> By (4) with $\omega = 0$, $p_y = q_x$ throughout $D$, and $p$, $q$ have continuous first partials. This is the hypothesis of [[§115★ Harmonic Conjugates#^lem-115-3|Lemma §115.3]] with $P = p$, $Q = q$, which gives path independence, the single-valued function (5), the derivatives (6), and the change by a constant.

^pf-124-4

*Uses:* [[§124★ Two-Dimensional Fluid Flow#^def-124-2|Def. §124.2]], [[§115★ Harmonic Conjugates#^lem-115-3|§115.3]]

> [!definition] Definition §124.5: Velocity Potential
> The function $\phi(x, y)$ of (5) is the **velocity potential** of the flow. By (6) the velocity $V = p + iq$ is the gradient of $\phi$; the [[§111 Directional Derivatives and the Gradient Vector#^def-111-1|directional derivative]] of $\phi$ in any direction is the component of the velocity in that direction.
>
> *B&C: Sec. 124 (text)*

^def-124-5

> [!definition] Definition §124.6: Equipotentials
> The level curves $\phi(x, y) = c_1$ of the [[§124★ Two-Dimensional Fluid Flow#^def-124-5|velocity potential]] are the **equipotentials**, and $V$ is normal to the equipotential through any point where $V \ne 0$.
>
> *B&C: Sec. 124 (text)*

^def-124-6

> [!theorem] Proposition §124.5: The Velocity Potential Is Harmonic
> In a simply connected domain where the flow is irrotational and the incompressible fluid has no sources or sinks, the velocity potential satisfies Laplace's equation $\phi_{xx}(x, y) + \phi_{yy}(x, y) = 0$, and its first and second partial derivatives are continuous: $\phi$ is harmonic.
>
> *B&C: Sec. 124 (text)*

^prop-124-5

> [!proof]+ Proof
> *B&C gives this as a sketch* ("just as in the case of the flow of heat"); here is the balance written out. The fluid is incompressible and has no sources or sinks, so the net rate at which fluid leaves any rectangle $R = [x_1, x_2] \times [y_1, y_2]$ in $D$ through its four sides (per unit height) is zero. Through the side $x = x_2$ it leaves at the rate $\int_{y_1}^{y_2}p(x_2, t)\,dt$, through $x = x_1$ it enters at the rate $\int_{y_1}^{y_2}p(x_1, t)\,dt$, and likewise for the horizontal sides; so, as in [[§118★ Steady Temperatures#^prop-118-1|Proposition §118.1]],
>
> $$
> 0 = \int_{y_1}^{y_2}\big[p(x_2, t) - p(x_1, t)\big]dt + \int_{x_1}^{x_2}\big[q(s, y_2) - q(s, y_1)\big]ds = \iint_R\big(p_x + q_y\big)\,dA
> $$
>
> for every rectangle, which forces $p_x + q_y = 0$ at every point (a continuous function with zero integral over every small rectangle vanishes). By (6), $p_x + q_y = \phi_{xx} + \phi_{yy}$. Finally, (6) and the continuity of $p$, $q$ and their first partials show that the first and second partials of $\phi$ are continuous.

^pf-124-5

*Uses:* [[§124★ Two-Dimensional Fluid Flow#^thm-124-4|§124.4]], [[§124★ Two-Dimensional Fluid Flow#^def-124-3|Def. §124.3]] (incompressible), [[§118★ Steady Temperatures#^prop-118-1|§118.1]], [[§115 Double Integrals Over Rectangles#^thm-115-3|Calc Thm. §115.3]] (Fubini)

> [!remark]- Connections
> - The same conclusion in 341, with the opposite sign convention: [[§44 Potential Equation#^ex-44-1|341 Ex. §44.1]] defines the velocity potential by $u = -\phi_x$, $v = -\phi_y$, while B&C uses $V = +\operatorname{grad}\phi$. Conservation of mass in general form, $\rho_t + \nabla\cdot(\rho\mathbf u) = 0$, which for constant $\rho$ is the condition $p_x + q_y = 0$ used above: [[§29 Conservation of Mass and Laplace's Equation#^thm-29-1|452 Thm. §29.1]], and irrotational flow, [[§29 Conservation of Mass and Laplace's Equation#^rem-29-4|452 Rem. §17.4]]. A gradient field and its potential: [[§125 Vector Fields#^def-125-4|Calc Def. §125.4]], with the potential built as a line integral in [[§128 The Fundamental Theorem for Line Integrals#^thm-128-3|Calc Thm. §128.3]].

## Examples

> [!example] Example §124.1: A Rigid Rotation and a Point Vortex
> **(a) Rigid rotation.** For $V = \omega_0(-y + ix)$, i.e. $p = -\omega_0y$, $q = \omega_0x$ ($\omega_0$ a real constant), the fluid turns about the origin like a rigid body. Its rotation is $\omega = \frac12[\omega_0 - (-\omega_0)] = \omega_0$ everywhere. Check (3) on the circle $|z| = r$: $V_T = \omega_0r$, so the circulation is $2\pi r\cdot\omega_0r = 2\pi\omega_0r^2$, and $\iint(q_x - p_y)\,dA = 2\omega_0\cdot\pi r^2$, the same. Since $p_y = -\omega_0 \ne \omega_0 = q_x$, there is no velocity potential.
>
> **(b) Point vortex.** For $V = \dfrac{-y + ix}{x^2 + y^2}$ ($z \ne 0$), $p_y = \dfrac{-(x^2 + y^2) + 2y^2}{(x^2 + y^2)^2} = \dfrac{y^2 - x^2}{(x^2 + y^2)^2}$ and $q_x = \dfrac{(x^2 + y^2) - 2x^2}{(x^2 + y^2)^2} = \dfrac{y^2 - x^2}{(x^2 + y^2)^2}$, so $\omega = 0$ at every point $z \ne 0$. Yet on $|z| = r$, $V_T = 1/r$ and the circulation is $2\pi$ for every $r$. There is no contradiction with (3): the punctured plane is not simply connected, and the disk bounded by $C_r$ contains the singular point $0$. On a simply connected part, such as the plane cut along a ray, Theorem §124.4 gives the velocity potential $\phi = \theta$, a branch of $\arg z$, which increases by $2\pi$ around the origin.
>
> *B&C: Sec. 124, Equations (3) and (4); the examples are added*

^ex-124-1

> [!example] Example §124.2: A Source
> Show that if the velocity potential is $\phi = A\ln r$ $(A > 0)$ for flow in the region $r \ge r_0$, the streamlines (the curves to which the velocity is tangent) are the half lines $\theta = c$ $(r \ge r_0)$, and the rate of flow outward through each complete circle about the origin is $2\pi A$, corresponding to a source of that strength at the origin.
>
> **Velocity.** $\phi = \frac A2\ln(x^2 + y^2)$, so $p = \phi_x = \dfrac{Ax}{x^2 + y^2}$, $q = \phi_y = \dfrac{Ay}{x^2 + y^2}$: $V = \dfrac{A}{r}e^{i\theta}$, radial and outward, of speed $A/r$. The curves tangent to $V$ are the rays $\theta = c$. (In §125 they are the level curves of the stream function $\psi = A\theta$.) The flow is irrotational ($p_y = q_x = -2Axy/r^4$) and $\phi$ is harmonic for $r > 0$ ([[§115★ Harmonic Conjugates#^ex-115-4|Example §115.4]]).
>
> **Outflow.** Through the circle $|z| = r$ the outward normal component of the velocity is $A/r$, so the rate of flow outward (per unit height) is $\frac Ar\cdot 2\pi r = 2\pi A$, the same for every circle: the fluid is created at the origin at the rate $2\pi A$. (On the circle the outward normal is the unit vector $e^{i\theta}$, and $\int_0^{2\pi}\frac Ar\,r\,d\theta = 2\pi A$.)
>
> *B&C: Sec. 126, Exercise 8*

^ex-124-2

> [!example] Example §124.3: The Velocity Potential of a Flow Around a Corner
> The velocity $V = 2A(x - iy)$, i.e. $p = 2Ax$, $q = -2Ay$ ($A > 0$), will turn out to be the flow around a corner of [[§126★ Flows Around a Corner and Around a Cylinder|§126]]. Show that it is irrotational and incompressible, and find its velocity potential by (5).
>
> **Irrotational and incompressible.** $p_y = 0 = q_x$, so $\omega = 0$; and $p_x + q_y = 2A - 2A = 0$.
>
> **Potential.** Take $(x_0, y_0) = (0, 0)$ and integrate (5) first along the segment from $(0, 0)$ to $(x, 0)$ ($t = 0$, $dt = 0$) and then from $(x, 0)$ to $(x, y)$ ($s = x$, $ds = 0$):
>
> $$
> \phi(x, y) = \int_0^x 2As\,ds + \int_0^y(-2At)\,dt = A(x^2 - y^2) .
> $$
>
> Check: $\phi_x = 2Ax = p$, $\phi_y = -2Ay = q$, and $\phi_{xx} + \phi_{yy} = 2A - 2A = 0$, as Proposition §124.5 requires. The equipotentials $x^2 - y^2 = c_1$ are rectangular hyperbolas, and the velocity is normal to them.
>
> *B&C: Sec. 124, Equation (5); the velocity is that of Sec. 126, Example 1*

^ex-124-3
