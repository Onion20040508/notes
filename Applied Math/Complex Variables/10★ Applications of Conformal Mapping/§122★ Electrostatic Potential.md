---
type: section
subject: "[[Complex Variables]]"
chapter: 10
section: 122
bc: "122"
aliases: ["B&C 122"]
tags: [complex-variables, math342, extension]
---
← [[§121★ Temperatures in a Quadrant]] · ↑ [[· 10★ Applications of Conformal Mapping]] · [[§123★ Examples (Electrostatic Potential)]] →

*Brown–Churchill, Section 122 (with Exercises 4, 5 and 7 of Section 123).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

The second physical interpretation of harmonic functions: electrostatics. In a region free of charges the electrostatic potential satisfies Laplace's equation, and when nothing varies along one axis it is a harmonic function of two variables, so every steady-temperature solution of [[§118★ Steady Temperatures|§118]]–[[§121★ Temperatures in a Quadrant|§121]] is also a potential problem. Conductors play the role of isotherms (they are equipotentials), the field intensity is minus the gradient of the potential, and the level curves of a harmonic conjugate are the flux lines, along which the field points.

## Potential and Field Intensity

> [!definition] Definition §122.1: Field Intensity; Electrostatic Potential
> In an electrostatic force field, the **field intensity** at a point is the vector representing the force exerted on a unit positive charge placed at that point. The **electrostatic potential** is a scalar function of the space coordinates such that, at each point, its directional derivative in any direction is the negative of the component of the field intensity in that direction.
>
> *B&C: Sec. 122 (text)*

^def-122-1

For two stationary charged particles, the force of attraction or repulsion is proportional to the product of the charges and inversely proportional to the square of the distance between them (the inverse-square law).

> [!theorem] Proposition §122.1: The Potential Is Harmonic Where There Are No Charges
> The potential at a point due to a single charged particle in space is inversely proportional to the distance between the point and the particle. In any region free of charges, the potential due to a distribution of charges outside the region satisfies Laplace's equation in three dimensions. If the potential $V$ is the same in all planes parallel to the $xy$ plane, then in regions free of charges $V$ is a harmonic function of $x$ and $y$:
>
> $$
> V_{xx}(x, y) + V_{yy}(x, y) = 0 ,
> $$
>
> and the field intensity at each point is parallel to the $xy$ plane, with components $-V_x(x, y)$ and $-V_y(x, y)$: it is $-\operatorname{grad} V$.
>
> *B&C: Sec. 122 (text)*

^prop-122-1

*B&C omits the proof (it is physics: the inverse-square law and superposition). The mathematical core, that $1/r$ is harmonic in space away from the origin, is [[§19 The Laplacian in Spherical Coordinates#^rem-19-2|452 Rem. §19.2]]; in the plane the corresponding potential of a line charge is $\ln r$, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-5|452 Thm. §17.5]] (Example §122.1).*

> [!definition] Definition §122.2: Equipotentials; Flux Lines
> A surface along which $V(x, y)$ is constant is an **equipotential surface** (in the $xy$ plane, an equipotential curve $V(x, y) = c_1$). If $U$ is a harmonic conjugate of $V$, the curves $U(x, y) = c_2$ in the $xy$ plane are the **flux lines**.
>
> *B&C: Sec. 122 (text)*

^def-122-2

> [!theorem] Proposition §122.2: Conductors Are Equipotentials; Flux Lines Follow the Field
> **(a)** In the static case the surface of a conductor is an equipotential.
>
> **(b)** Where a flux line $U(x, y) = c_2$ meets an equipotential $V(x, y) = c_1$ at a point where the derivative of the analytic function $V(x, y) + iU(x, y)$ is not zero, the two curves are orthogonal, and the field intensity is tangent to the flux line there.
>
> *B&C: Sec. 122 (text)*

^prop-122-2

> [!proof]+ Proof
> **(a)** (Physical argument, as in B&C.) Charges are free to move on a conducting surface, so in the static case the tangential component of the field intensity there is zero. By Definition §122.1 the directional derivative of $V$ along the surface is then zero in every tangent direction, so $V$ is constant along the (connected) surface.
>
> **(b)** By the Cauchy–Riemann equations $U_x = -V_y$, $U_y = V_x$, so $\operatorname{grad} U$ is $\operatorname{grad} V$ turned through $+\pi/2$, and both are nonzero where $(V + iU)' = V_x - iV_y \ne 0$. The level curves are smooth there, with normals $\operatorname{grad} V$ and $\operatorname{grad} U$, which are perpendicular, so the curves are orthogonal ([[§112★ Preservation of Angles and Scale Factors#^ex-112-2|Example §112.2]]). The tangent of $U = c_2$ is perpendicular to $\operatorname{grad} U$, hence parallel to $\operatorname{grad} V$ and to the field intensity $-\operatorname{grad} V$. (This is [[§118★ Steady Temperatures#^prop-118-2|Proposition §118.2]](b) with $V$, $U$ in place of $T$, $S$.)

^pf-122-2

*Uses:* [[§122★ Electrostatic Potential#^def-122-1|Def. §122.1]], [[§122★ Electrostatic Potential#^def-122-2|Def. §122.2]], [[§122★ Electrostatic Potential#^prop-122-1|§122.1]], [[§21 Cauchy–Riemann Equations#^thm-21-1|§21.1]], [[§112★ Preservation of Angles and Scale Factors#^ex-112-2|Ex. §112.2]], [[§118★ Steady Temperatures#^prop-118-2|§118.2]]

> [!remark] Remark: One Mathematical Problem, Several Physical Ones
> Boundary value problems for the potential $V$ are the same mathematical problems as those for steady temperatures $T$, and, as there, complex variables handle only two-dimensional problems. For instance, the problem of [[§120★ A Related Problem (Steady Temperatures in a Half Plane)#^ex-120-1|Example §120.1]] is also that of the electrostatic potential in the empty space $-\pi/2 < x < \pi/2$, $y > 0$ bounded by the conducting planes $x = \pm\pi/2$ and $y = 0$, insulated from each other at their intersections, when the first two are kept at potential $0$ and the third at potential $1$. The potential in the steady flow of electricity in a plane conducting sheet is also harmonic at points free of sources and sinks, and so is the gravitational potential in empty space.

^rem-122-1

> [!remark]- Connections
> - Laplace's equation for potentials, steady temperatures and ideal flows, and the Dirichlet and Neumann problems: [[§35 Potential Equation#^def-35-1|341 Def. §35.1]], [[§35 Potential Equation#^def-35-2|341 Def. §35.2]]. Gradient fields and potentials of inverse-square force fields in Stewart: [[§107 Vector Fields#^ex-107-2|Calc Ex. §107.2]], [[§107 Vector Fields#^ex-107-4|Calc Ex. §107.4]] (with the opposite sign convention $\mathbf F = \nabla f$).

## Examples

> [!example] Example §122.1: Coaxial Cylinders
> All branches of $\log z$ have the same real part $\ln|z| = \frac12\ln(x^2 + y^2)$, which is harmonic everywhere except at the origin. Find the electrostatic potential $V(x, y)$ in the space between two coaxial conducting cylindrical surfaces $x^2 + y^2 = 1$ and $x^2 + y^2 = r_0^2$ $(r_0 \ne 1)$, with $V = 0$ on the first and $V = 1$ on the second.
>
> **Solution.** $V = A\ln r + B$ is harmonic for $r > 0$. The conditions $V(1) = B = 0$ and $V(r_0) = A\ln r_0 = 1$ give
>
> $$
> V = \frac{\ln r}{\ln r_0} = \frac{\ln(x^2 + y^2)}{2\ln r_0} .
> $$
>
> **Field and flux lines.** The field intensity is $-\operatorname{grad} V = -\dfrac{1}{\ln r_0}\,\dfrac{(x, y)}{x^2 + y^2}$, radial, of size $\dfrac{1}{r|\ln r_0|}$; for $r_0 > 1$ it points inward, from the outer conductor at the higher potential toward the inner one. A harmonic conjugate is $U = \theta/\ln r_0$ (on any slit domain), so the flux lines are the rays $\theta = $ const, orthogonal to the equipotential circles. The potential has the form of a line charge on the axis ([[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-5|452 Thm. §17.5]], the fundamental solution $\ln r$).
>
> *B&C: Sec. 123, Exercise 4*

^ex-122-1

> [!example] Example §122.2: A Charged Strip in a Grounded Plane
> Find the bounded electrostatic potential $V(x, y)$ in the space $y > 0$ bounded by an infinite conducting plane $y = 0$, one strip $-a < x < a$ of which is insulated from the rest of the plane and kept at potential $V = 1$, while $V = 0$ on the rest (B&C's Fig. 168).
>
> **Solution.** This is the temperature problem of [[§119★ Steady Temperatures in a Half Plane#^ex-119-1|Example §119.1]] with lengths scaled by $a$: the map $z \mapsto z/a$ is conformal and takes the strip to $-1 < x < 1$. Replacing $(x, y)$ by $(x/a, y/a)$ in (6) of §119,
>
> $$
> V = \frac1\pi\arctan\Big(\frac{2(y/a)}{(x/a)^2 + (y/a)^2 - 1}\Big) = \frac1\pi\arctan\Big(\frac{2ay}{x^2 + y^2 - a^2}\Big) \qquad (0 \le \arctan t \le \pi).
> $$
>
> **Check.** For $|x| < a$, $y \to 0^+$: the quotient tends to $0^-$ and $V \to 1$. For $|x| > a$: $0^+$ and $V \to 0$. $V$ is harmonic (Theorem [[§116★ Transformations of Harmonic Functions#^thm-116-1|§116.1]], a composition with $z/a$) and $0 \le V \le 1$. The equipotentials are circular arcs through $(\pm a, 0)$.
>
> *B&C: Sec. 123, Exercise 5*

^ex-122-2

> [!example] Example §122.3: Two Parallel Planes, Each Split in Half
> Find the potential $V$ in the space between the planes $y = 0$ and $y = \pi$ when $V = 0$ on the parts of both planes where $x > 0$ and $V = 1$ on the parts where $x < 0$ (B&C's Fig. 170).
>
> **Map.** $w = e^z$ maps the strip $0 < y < \pi$ onto the upper half plane ([[§103★ Mappings by the Exponential Function#^ex-103-3|Example §103.3]]): on $y = 0$, $x > 0$ goes to $u > 1$ and $x < 0$ to $0 < u < 1$; on $y = \pi$, $x > 0$ goes to $u < -1$ and $x < 0$ to $-1 < u < 0$. So $V = 1$ on $-1 < u < 1$ and $V = 0$ on $|u| > 1$: the problem of Example §119.1 in the $w$ plane.
>
> **Compose.** By (6) of §119, $V = \frac1\pi\arctan\big(\frac{2v}{u^2 + v^2 - 1}\big)$ with $u^2 + v^2 = e^{2x}$ and $v = e^x\sin y$:
>
> $$
> \frac{2e^x\sin y}{e^{2x} - 1} = \frac{\sin y}{\sinh x}, \qquad V = \frac1\pi\arctan\Big(\frac{\sin y}{\sinh x}\Big) \qquad (0 \le \arctan t \le \pi).
> $$
>
> **Check.** For $x > 0$ and $y \to 0^+$ or $y \to \pi^-$, $\sin y/\sinh x \to 0^+$ and $V \to 0$. For $x < 0$, $\sinh x < 0$ and the quotient tends to $0^-$, so $V \to 1$. On the midline $x = 0$ ($0 < y < \pi$), the quotient is infinite and $V = \frac12$, as symmetry demands.
>
> *B&C: Sec. 123, Exercise 7*

^ex-122-3
