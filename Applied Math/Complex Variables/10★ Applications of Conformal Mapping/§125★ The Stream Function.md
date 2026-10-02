---
type: section
subject: "[[Complex Variables]]"
chapter: 10
section: 125
bc: "125"
aliases: ["B&C 125"]
tags: [complex-variables, math342, extension]
---
← [[§124★ Two-Dimensional Fluid Flow]] · ↑ [[· 10★ Applications of Conformal Mapping]] · [[§126★ Flows Around a Corner and Around a Cylinder]] →

*Brown–Churchill, Section 125 (with Exercises 1 and 2 of Section 126).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

A harmonic conjugate $\psi$ of the velocity potential $\phi$ is the stream function: its level curves are the streamlines, along which the fluid moves, and its values measure how much fluid crosses a curve. The two combine into one analytic function, the complex potential $F = \phi + i\psi$, and the velocity is simply the conjugate of its derivative, $V = \overline{F'(z)}$. So a flow is specified by a single analytic function, and the flows of [[§126★ Flows Around a Corner and Around a Cylinder|§126]] are found by composing a simple complex potential with a conformal map.

## Streamlines and the Complex Potential

By [[§124★ Two-Dimensional Fluid Flow#^thm-124-4|Theorem §124.4]], in a simply connected domain where the flow is irrotational the velocity
$$
V = p(x, y) + iq(x, y) \qquad (1)
$$
can be written
$$
V = \phi_x(x, y) + i\phi_y(x, y) = \operatorname{grad}\phi(x, y), \qquad (2)
$$
where $\phi$ is the velocity potential; when $V \ne 0$ it is normal to the equipotential through $(x, y)$.

> [!definition] Definition §125.1: Stream Function; Streamlines; Complex Potential
> Let $\phi$ be the velocity potential of an irrotational flow of an incompressible fluid in a simply connected domain, and let $\psi(x, y)$ be a harmonic conjugate of $\phi$ ([[§115★ Harmonic Conjugates#^thm-115-4|Theorem §115.4]]). Then $\psi$ is the **stream function** of the flow, the curves $\psi(x, y) = c_2$ are the **streamlines**, and the analytic function
>
> $$
> F(z) = \phi(x, y) + i\psi(x, y)
> $$
>
> is the **complex potential** of the flow.
>
> *B&C: Sec. 125 (text)*

^def-125-1

> [!theorem] Proposition §125.1: Velocity from the Complex Potential
> The velocity is tangent to the streamline through each point where it is not zero, and
>
> $$
> V = \overline{F'(z)}, \qquad |V| = |F'(z)| . \qquad (3)
> $$
>
> In particular a boundary across which fluid cannot flow is a streamline.
>
> *B&C: Sec. 125, Equation (3) and text*

^prop-125-1

> [!proof]+ Proof
> Since $F$ is analytic, $F'(z) = \phi_x + i\psi_x$ ([[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]), and by the Cauchy–Riemann equation $\psi_x = -\phi_y$,
>
> $$
> F'(z) = \phi_x(x, y) - i\phi_y(x, y) .
> $$
>
> Comparing with (2), $V = \overline{F'(z)}$, and $|V| = |F'(z)|$. Where $V \ne 0$, $\operatorname{grad}\psi = (-\phi_y, \phi_x)$ is $\operatorname{grad}\phi$ turned through $+\pi/2$ and is nonzero, so the streamline $\psi = c_2$ is a smooth curve with normal $\operatorname{grad}\psi$ and tangent parallel to $\operatorname{grad}\phi = V$ (as in [[§118★ Steady Temperatures#^prop-118-2|Proposition §118.2]](b)). On a boundary arc that fluid cannot cross, the normal component of $V$ is $0$; by Proposition §125.2 below, $\psi$ changes along the arc at the rate $V_N = 0$, so $\psi$ is constant there and the arc is a streamline.

^pf-125-1

*Uses:* [[§125★ The Stream Function#^def-125-1|Def. §125.1]], [[§124★ Two-Dimensional Fluid Flow#^thm-124-4|§124.4]], [[§21 Cauchy–Riemann Equations#^thm-21-1|§21.1]], [[§118★ Steady Temperatures#^prop-118-2|§118.2]], [[§125★ The Stream Function#^prop-125-2|§125.2]]

By [[§115★ Harmonic Conjugates#^thm-115-4|Theorem §115.4]], equation (9) there, if $\phi$ is harmonic in a simply connected domain $D$, a harmonic conjugate is
$$
\psi(x, y) = \int_{(x_0, y_0)}^{(x, y)} -\phi_t(s, t)\,ds + \phi_s(s, t)\,dt ,
$$
the integral being independent of path.

> [!theorem] Proposition §125.2: The Stream Function Measures the Flow Across a Curve
> With $p = \phi_x$, $q = \phi_y$ as in (2),
>
> $$
> \psi(x, y) = \int_C -q(s, t)\,ds + p(s, t)\,dt \qquad (4)
> $$
>
> for any contour $C$ in $D$ from $(x_0, y_0)$ to $(x, y)$, and
>
> $$
> \psi(x, y) = \int_C V_N(s, t)\,d\sigma , \qquad (5)
> $$
>
> where $V_N$ is the component of the velocity along the unit normal $\mathbf N$ to $C$ obtained by turning the unit tangent through $-\pi/2$ (to the right of the direction of travel). Physically, $\psi(x, y)$ is the rate of flow of the fluid, by volume, across a surface of unit height standing perpendicular to the $xy$ plane on $C$, from its left side to its right side.
>
> *B&C: Sec. 125, Equations (4) and (5)*

^prop-125-2

> [!proof]+ Proof
> (4) is the formula above with $\phi_t(s, t) = q(s, t)$ and $\phi_s(s, t) = p(s, t)$, by (6) of §124. For (5) (B&C refers it to advanced calculus): parametrize each smooth piece of $C$ by arc length, $(s(\sigma), t(\sigma))$; the unit tangent is $\mathbf T = (s', t')$ and the normal turned through $-\pi/2$ is $\mathbf N = (t', -s')$. Then $V_N = (p, q)\cdot\mathbf N = pt' - qs'$, and
>
> $$
> \int_C -q\,ds + p\,dt = \int\big(-q\,s' + p\,t'\big)\,d\sigma = \int_C V_N\,d\sigma .
> $$

^pf-125-2

*Uses:* [[§115★ Harmonic Conjugates#^thm-115-4|§115.4]], [[§124★ Two-Dimensional Fluid Flow#^thm-124-4|§124.4]], [[§108 Line Integrals#^thm-108-2|Calc Thm. §108.2]]

> [!remark]- Connections
> - The flux of a plane field across a curve as the line integral of its normal component, $\int_C \mathbf F\cdot\mathbf n\,ds = \int_C -q\,dx + p\,dy$ for $\mathbf F = (p, q)$, and its form for closed curves: [[§111 Curl and Divergence#^thm-111-5|Calc Thm. §111.5]] (Green's theorem, normal form). In the language of forms, $\psi$ is a primitive of the flux form $-q\,dx + p\,dy$, which is closed exactly when the flow is incompressible.

## Examples

> [!example] Example §125.1: Uniform Flow
> When the complex potential is
>
> $$
> F(z) = Az , \qquad (6)
> $$
>
> $A$ a positive real constant,
>
> $$
> \phi(x, y) = Ax \qquad\text{and}\qquad \psi(x, y) = Ay . \qquad (7)
> $$
>
> The streamlines $\psi = c_2$ are the horizontal lines $y = c_2/A$, and the velocity at every point is $V = \overline{F'(z)} = A$. Here $\psi = 0$ at every point of the $x$ axis; taking the origin as $(x_0, y_0)$, $\psi(x, y) = Ay$ is the rate of flow across any contour from the origin to $(x, y)$ (B&C's Fig. 172): for instance across the vertical segment from $(x, 0)$ to $(x, y)$, $V_N = A$ along a length $y$. The flow is uniform and to the right. It can be read as the uniform flow in the upper half plane bounded by the $x$ axis, which is a streamline, or as the uniform flow between two parallel lines $y = y_1$ and $y = y_2$.
>
> *B&C: Sec. 125, Example*

^ex-125-1

> [!remark] Remark: Uniqueness Is Not Examined
> The stream function characterizes a definite flow in a region. Whether only one such function corresponds to a given region, up to a constant factor or an additive constant, is not examined in B&C. Sometimes, when the velocity is uniform far from an obstacle or when sources and sinks are prescribed (Chapter 11), the physical situation shows that the flow is determined by the conditions of the problem. But prescribing boundary values alone does not determine a harmonic function, even up to a constant factor (Example §125.2).

^rem-125-1

> [!example] Example §125.2: Two Stream Functions with the Same Zero Boundary Values
> The function $\psi = Ay$ of Example §125.1 is harmonic in the half plane $y > 0$ and vanishes on its boundary. So does $\psi_1(x, y) = Be^x\sin y$, the imaginary part of $F_1(z) = Be^z$ ($B$ real). But $\psi_1$ is not a multiple of $\psi$, and its streamline $\psi_1 = 0$ consists not only of the line $y = 0$ but also of the lines $y = n\pi$ $(n = 1, 2, \ldots)$. In fact $F_1 = Be^z$ is the complex potential of a flow in the strip $0 < y < \pi$, both of whose edges form the streamline $\psi_1 = 0$. Its velocity is $V = \overline{Be^z} = Be^xe^{-iy}$: on $y = 0$ it is $Be^x$, and on $y = \pi$ it is $-Be^x$. So if $B > 0$ the fluid flows to the right along the lower line and to the left along the upper one.
>
> *B&C: Sec. 125 (text)*

^ex-125-2

> [!example] Example §125.3: The Velocity from the Stream Function
> State why the components of velocity can be obtained from the stream function by
>
> $$
> p(x, y) = \psi_y(x, y), \qquad q(x, y) = -\psi_x(x, y) .
> $$
>
> Since $\psi$ is a harmonic conjugate of $\phi$, the Cauchy–Riemann equations $\phi_x = \psi_y$ and $\phi_y = -\psi_x$ hold, and by (2) $p = \phi_x$, $q = \phi_y$. (Equivalently, $\overline{F'} = \phi_x - i\psi_x = \psi_y - i\psi_x$.) For $\psi = Ay$: $p = A$, $q = 0$, the uniform flow of Example §125.1.
>
> *B&C: Sec. 126, Exercise 1*

^ex-125-3

> [!example] Example §125.4: The Pressure Has No Interior Minimum
> Show that at an interior point of a region of flow (under the assumptions of §124) the fluid pressure cannot be less than the pressure at all other points of a neighborhood of that point.
>
> Suppose $P(z_0) < P(z)$ for all $z \ne z_0$ in some neighborhood $|z - z_0| < \varepsilon$ in which the complex potential $F$ is analytic. By Bernoulli's equation ([[§124★ Two-Dimensional Fluid Flow#^prop-124-3|Proposition §124.3]]), $P = \rho\big(c - \frac12|V|^2\big)$, so $|V(z_0)| > |V(z)|$ there, and by (3), $|F'(z)| \le |F'(z_0)|$ throughout the neighborhood. Since $F'$ is analytic ([[§57 Some Consequences of the Extension#^thm-57-1|Theorem §57.1]]), [[§59 Maximum Modulus Principle#^lem-59-2|Lemma §59.2]] makes $F'$ constant in the neighborhood. Then $|V|$, and with it $P$, is constant there, contradicting $P(z_0) < P(z)$. (The pressure can have an interior maximum: at a stagnation point, where $V = 0$; see [[§126★ Flows Around a Corner and Around a Cylinder#^ex-126-1|Example §126.1]].)
>
> *B&C: Sec. 126, Exercise 2*

^ex-125-4
