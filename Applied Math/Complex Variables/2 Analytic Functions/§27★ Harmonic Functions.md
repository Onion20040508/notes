---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 27
bc: "27"
aliases: ["B&C 27"]
tags: [complex-variables, math342, extension]
---
← [[§26 Further Examples (Analytic Functions)]] · ↑ [[· 2 Analytic Functions]] · [[§28★ Uniquely Determined Analytic Functions]] →

*Brown–Churchill, Section 27 · MAT 342 Practice Finals (Fall 1999, Fall 2002, Spring 2005).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Harmonic functions, the solutions of Laplace's equation $H_{xx} + H_{yy} = 0$, describe steady temperatures in plates, electrostatic potentials in charge-free regions and velocity potentials of ideal fluid flow. This section proves the link that makes complex variables a tool for these problems: the real and imaginary parts of an analytic function are harmonic. So every analytic function supplies two harmonic functions, and, conversely, a function that is not harmonic cannot be the real part of an analytic function. The physical applications (Ch. 10–12) run this in the other direction, building analytic functions whose real parts take prescribed boundary values.

## Harmonic Functions

> [!definition] Definition §27.1: Harmonic Function
> A real-valued function $H$ of two real variables $x$ and $y$ is **harmonic** in a given domain of the $xy$ plane if, throughout that domain, it has continuous partial derivatives of the first and second order and satisfies the partial differential equation
>
> $$
> H_{xx}(x, y) + H_{yy}(x, y) = 0 , \qquad (1)
> $$
>
> known as **Laplace's equation**.
>
> *B&C: Sec. 27 (text)*

^def-27-1

> [!remark]- Connections
> - The same equation in the PDE course, solved by separation of variables in rectangles, slots and disks: [[§35 Potential Equation#^def-35-1|341 Def. §35.1]]. The Laplacian in $\mathbb{R}^n$ and Green's identities: [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-2|452 Def. §17.2]].

Harmonic functions play an important role in applied mathematics. For example, the temperatures $T(x, y)$ in thin plates lying in the $xy$ plane are often harmonic. A function $V(x, y)$ is harmonic when it denotes an electrostatic potential that varies only with $x$ and $y$ in the interior of a region of three-dimensional space that is free of charges.

## Components of Analytic Functions Are Harmonic

> [!theorem] Theorem §27.1: Real and Imaginary Parts Are Harmonic
> If a function $f(z) = u(x, y) + iv(x, y)$ is analytic in a domain $D$, then its component functions $u$ and $v$ are harmonic in $D$.
>
> *B&C: Sec. 27, Theorem*

^thm-27-1

> [!proof]+ Proof
> We need a result that is proved in Ch. 4, [[§57 Some Consequences of the Extension#^cor-57-2|Corollary §57.2]]: if a function of a complex variable is analytic at a point, then its real and imaginary components have continuous partial derivatives of all orders at that point. In particular $u$ and $v$ have continuous first- and second-order partial derivatives throughout $D$. (§57 does not depend on this section, so there is no circularity.)
>
> Since $f$ is analytic in $D$, the first-order partial derivatives of its component functions satisfy the Cauchy–Riemann equations throughout $D$:
>
> $$
> u_x = v_y, \qquad u_y = -v_x . \qquad (2)
> $$
>
> Differentiating both sides of these equations with respect to $x$, we have
>
> $$
> u_{xx} = v_{yx}, \qquad u_{yx} = -v_{xx} . \qquad (3)
> $$
>
> Likewise, differentiation with respect to $y$ yields
>
> $$
> u_{xy} = v_{yy}, \qquad u_{yy} = -v_{xy} . \qquad (4)
> $$
>
> By the theorem on mixed partial derivatives, the continuity of the second-order partial derivatives of $u$ and $v$ ensures that $u_{yx} = u_{xy}$ and $v_{yx} = v_{xy}$. It then follows from (3) and (4) that
>
> $$
> u_{xx} + u_{yy} = v_{yx} - v_{xy} = 0 \qquad\text{and}\qquad v_{xx} + v_{yy} = -u_{yx} + u_{xy} = 0 .
> $$
>
> That is, $u$ and $v$ are harmonic in $D$.

^pf-27-1

*Uses:* [[§21 Cauchy–Riemann Equations#^thm-21-1|§21.1]], [[§57 Some Consequences of the Extension#^cor-57-2|§57.2]], [[§27★ Harmonic Functions#^def-27-1|Def. §27.1]], [[§5 Equality of Mixed Partials#^thm-5-1|452 Thm. §5.1]] (Schwarz–Clairaut)

> [!remark]- Connections
> - Theorem §27.1 is the source of the closed-form solutions of potential problems; the converse direction (every harmonic function on a simply connected domain is the real part of an analytic function, its **harmonic conjugate** being the imaginary part) is [[§115★ Harmonic Conjugates#^thm-115-4|Theorem §115.4]]. The separation-of-variables solutions of [[§38 Potential in Unbounded Regions#^thm-38-1|341 Thm. §38.1]] are sums of real parts of analytic functions such as $-ie^{in\pi z/a}$; Example §27.1 is the term $n = 1$, $a = \pi$.

> [!example] Example §27.1: Steady Temperatures in a Semi-Infinite Strip
> The function $T(x, y) = e^{-y}\sin x$ is harmonic in any domain of the $xy$ plane and, in particular, in the semi-infinite vertical strip $0 < x < \pi$, $y > 0$. It also assumes the values indicated on the edges of the strip. More precisely, it satisfies all of the conditions
>
> $$
> T_{xx}(x, y) + T_{yy}(x, y) = 0 ,
> $$
>
> $$
> T(0, y) = 0, \qquad T(\pi, y) = 0 ,
> $$
>
> $$
> T(x, 0) = \sin x, \qquad \lim_{y\to\infty}T(x, y) = 0 ,
> $$
>
> which describe steady temperatures $T(x, y)$ in a thin homogeneous plate in the $xy$ plane that has no heat sources or sinks and is insulated except for the stated conditions along the edges.
>
> **Directly.** $T_{xx} = -e^{-y}\sin x$ and $T_{yy} = e^{-y}\sin x$, both continuous, so $T_{xx} + T_{yy} = 0$ everywhere. On the edges, $\sin 0 = \sin\pi = 0$, $e^{0} = 1$, and $|T(x, y)| \le e^{-y} \to 0$ as $y \to \infty$.
>
> **From Theorem §27.1.** The function $f(z) = e^{-y}\sin x - ie^{-y}\cos x$ is entire: its components $u = e^{-y}\sin x$, $v = -e^{-y}\cos x$ satisfy $u_x = e^{-y}\cos x = v_y$ and $u_y = -e^{-y}\sin x = -v_x$ everywhere, with continuous partials (B&C's Exercise 1(c) of Sec. 26). Hence its real component, the temperature function $T(x, y) = e^{-y}\sin x$, must be harmonic in every domain of the $xy$ plane. (With [[§30 The Exponential Function#^def-30-1|Definition §30.1]], $f(z) = -ie^{-y}e^{ix} = -ie^{iz}$.)
>
> *B&C: Sec. 27, Examples 1 and 2*

^ex-27-1

![[m342-27-1.svg]]
*Isotherms $T = e^{-y}\sin x = c$ (red, $c = 0.1, 0.2, 0.4, 0.6, 0.8$), that is $y = \ln(\sin x/c)$, in the strip $0 < x < \pi$, $y > 0$ with $T = \sin x$ on the bottom and $T = 0$ on the sides. The dashed blue curves are the level curves $e^{-y}\cos x = k$ of the conjugate component $v = -e^{-y}\cos x$ of $f(z) = -ie^{iz}$; they cross the isotherms at right angles and are the lines along which heat flows (Remark: Level Curves Are Orthogonal).*

> [!example] Example §27.2: The Components of 1/z²
> Since the function $f(z) = 1/z^2$ is analytic at every nonzero point $z$ ([[§24★ Polar Coordinates#^ex-24-1|Example §24.1]]) and since
>
> $$
> \frac{1}{z^2} = \frac{1}{z^2}\cdot\frac{\bar z^{\,2}}{\bar z^{\,2}} = \frac{\bar z^{\,2}}{(z\bar z)^2} = \frac{\bar z^{\,2}}{|z|^4} = \frac{(x^2 - y^2) - i2xy}{(x^2 + y^2)^2} ,
> $$
>
> the two functions
>
> $$
> u(x, y) = \frac{x^2 - y^2}{(x^2 + y^2)^2} \qquad\text{and}\qquad v(x, y) = -\frac{2xy}{(x^2 + y^2)^2}
> $$
>
> are harmonic throughout any domain in the $xy$ plane that does not contain the origin. Checking this directly takes a page of differentiation; Theorem §27.1 makes it immediate.
>
> *B&C: Sec. 27, Example 3*

^ex-27-2

> [!remark]- Remark: Level Curves Are Orthogonal
> Let $f = u + iv$ be analytic in $D$, and let $z_0 = (x_0, y_0)$ lie on the level curves $u(x, y) = c_1$ and $v(x, y) = c_2$. If $f'(z_0) \ne 0$, the curves cross at right angles at $z_0$ (B&C's Exercise 2). Indeed, their normal vectors are $\nabla u = (u_x, u_y)$ and $\nabla v = (v_x, v_y) = (-u_y, u_x)$ by the Cauchy–Riemann equations, so
>
> $$
> \nabla u\cdot\nabla v = -u_xu_y + u_yu_x = 0 ,
> $$
>
> and both gradients are nonzero because $|\nabla u|^2 = |\nabla v|^2 = u_x^2 + v_x^2 = |f'(z_0)|^2 \ne 0$. Two curves with perpendicular normals have perpendicular tangents. For $f(z) = z^2$ the families $x^2 - y^2 = c_1$ and $2xy = c_2$ are orthogonal hyperbolas, except at the origin, where $f'(0) = 0$ and the curves $u = 0$ (the lines $y = \pm x$) and $v = 0$ (the axes) meet at $45°$.
>
> Physically: if $u$ is a temperature, the curves $v = c_2$ are the heat flow lines; if $u$ is an electrostatic potential, they are the lines of force; if $u$ is a velocity potential, they are the streamlines.

^rem-27-1

## Which Functions Can Be Real Parts?

> [!example] Example §27.3: An Entire Function with Given Real Part
> Find an entire function $f(z)$ such that $\operatorname{Re} f = 4x^3y - 4xy^3 - y$.
>
> **The candidate is harmonic.** $u = 4x^3y - 4xy^3 - y$ has $u_{xx} = 24xy$ and $u_{yy} = -24xy$, so $u_{xx} + u_{yy} = 0$; by Theorem §27.1 this is necessary.
>
> **Find $v$ from the Cauchy–Riemann equations.** We need $v_y = u_x = 12x^2y - 4y^3$. Integrating in $y$,
>
> $$
> v = 6x^2y^2 - y^4 + \varphi(x) .
> $$
>
> Then $v_x = 12xy^2 + \varphi'(x)$ must equal $-u_y = -(4x^3 - 12xy^2 - 1) = -4x^3 + 12xy^2 + 1$, so $\varphi'(x) = -4x^3 + 1$ and $\varphi(x) = -x^4 + x + C$. Hence
>
> $$
> v(x, y) = -x^4 + 6x^2y^2 - y^4 + x + C \qquad (C \text{ real}) .
> $$
>
> The partials of $u$ and $v$ are continuous and satisfy the Cauchy–Riemann equations everywhere, so $f = u + iv$ is entire ([[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]]).
>
> **Recognize $f$.** Since $z^4 = (x^4 - 6x^2y^2 + y^4) + i(4x^3y - 4xy^3)$ and $iz = -y + ix$,
>
> $$
> f(z) = -iz^4 + iz + iC .
> $$
>
> Check: $\operatorname{Re}(-iz^4) = \operatorname{Im}(z^4) = 4x^3y - 4xy^3$ and $\operatorname{Re}(iz) = -y$. The answer is unique up to the imaginary constant $iC$: if $f_1, f_2$ are entire with the same real part, then $i(f_1 - f_2)$ is entire and real-valued, hence constant ([[§26 Further Examples (Analytic Functions)#^ex-26-5|Example §26.5]]).
>
> *Source: 342 practice final (Fall 1999), Q10*

^ex-27-3

> [!example] Example §27.4: Functions That Are Not Real Parts
> True or false: **(a)** there exists an entire function whose real part is $e^{x + y}$; **(b)** there exists an entire function whose real part is $xe^y$.
>
> Both are **false**. By Theorem §27.1 the real part of an entire function is harmonic in the whole plane.
>
> **(a)** $u = e^{x + y}$ has $u_{xx} = u_{yy} = e^{x + y}$, so $u_{xx} + u_{yy} = 2e^{x + y} \ne 0$ at every point: $u$ is not harmonic.
>
> **(b)** $u = xe^y$ has $u_{xx} = 0$ and $u_{yy} = xe^y$, so $u_{xx} + u_{yy} = xe^y$, which is nonzero whenever $x \ne 0$: $u$ is not harmonic in the plane (nor in any domain).
>
> By contrast $e^x\cos y$ and $e^x\sin y$ *are* real parts of entire functions, $e^z$ and $-ie^z$.
>
> The same conclusions follow from the Cauchy–Riemann equations alone, without the smoothness behind Theorem §27.1: [[§21 Cauchy–Riemann Equations#^rem-21-2|Remark: The Cauchy–Riemann Equations Alone Rule Out a Real Part]].
>
> *Source: 342 practice final (Spring 2005), Q8d; 342 practice final (Fall 2002), Q8d*

^ex-27-4

> [!example] Example §27.5: No Analytic f with |f|² = 4 − |z|²
> True or false: there is a function $f(z)$, analytic in the disk $D = \{|z| < 1\}$, such that $|f(z)|^2 = 4 - |z|^2$ for all $z$ in $D$.
>
> **False.** Suppose $f = u + iv$ were such a function. By Theorem §27.1 (and [[§57 Some Consequences of the Extension#^cor-57-2|Corollary §57.2]]) $u$ and $v$ have continuous second partials and are harmonic. For any such function, $(u^2)_{xx} = 2u_x^2 + 2uu_{xx}$, so
>
> $$
> \Delta(u^2) = 2(u_x^2 + u_y^2) + 2u\,\Delta u = 2(u_x^2 + u_y^2), \qquad \Delta(v^2) = 2(v_x^2 + v_y^2) ,
> $$
>
> where $\Delta = \partial^2/\partial x^2 + \partial^2/\partial y^2$. By the Cauchy–Riemann equations $u_y^2 = v_x^2$ and $v_y^2 = u_x^2$, so
>
> $$
> \Delta|f|^2 = \Delta(u^2 + v^2) = 4(u_x^2 + v_x^2) = 4|f'(z)|^2 \ge 0 .
> $$
>
> But $\Delta(4 - x^2 - y^2) = -2 - 2 = -4 < 0$. So no such $f$ exists.
>
> (Alternatively: $|f(0)| = 2$ while $|f(z)| < 2$ for $z \ne 0$, so $|f|$ has a maximum at an interior point; by the maximum modulus principle, [[§59 Maximum Modulus Principle#^thm-59-3|Theorem §59.3]], $f$ would be constant, and then $|f|^2$ could not equal the nonconstant $4 - |z|^2$.)
>
> *Source: 342 practice final (Fall 1999), Q7b*

^ex-27-5
