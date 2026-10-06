---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 4
section: 35
powers: "4.1"
aliases: ["Powers 4.1"]
tags: [fourier-series-and-pdes, math341]
---
← [[§34★ Wave Equation in Unbounded Regions]] · ↑ [[· 4 The Potential Equation]] · [[§36 Potential in a Rectangle]] →

*Powers, Section 4.1 · MAT 341 lectures 11.7, 11.19–11.21.*

Chapter 4 studies the potential equation, or Laplace's equation, $\nabla^2u = 0$. It is the time-independent part of both the heat and the wave equation in two or three dimensions: it governs steady-state temperatures in a plate, the equilibrium shape of a stretched membrane, electrostatic and gravitational potentials away from charges and masses, and the velocity potential of an ideal fluid. Its solutions, the harmonic functions, are very rigid: they satisfy a maximum principle and a mean value property, which make the Dirichlet problem uniquely solvable. This section sets up the equation and its boundary value problems, finds the simplest harmonic functions, and rewrites the Laplacian in polar and cylindrical coordinates for the disk problems of [[§39 Potential in a Disk|§39]].

## Laplace's Equation

> [!definition] Definition §35.1: Potential Equation; Harmonic Function
> The **potential equation**, or **Laplace's equation**, in two dimensions is
>
> $$
> \frac{\partial^2u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} = 0 ,
> $$
>
> and in three dimensions
>
> $$
> \frac{\partial^2u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} + \frac{\partial^2u}{\partial z^2} = 0 .
> $$
>
> Either is written $\nabla^2u = 0$ (also $\Delta u = 0$), where $\nabla^2u = u_{xx} + u_{yy}\ (+\,u_{zz})$ is the **Laplacian** of $u$. A solution of the potential equation in a region is called a **harmonic function** there.
>
> *Powers: 4.1 (text)*

^def-35-1

> [!remark]- Connections
> - The same definition, with the example $e^x\sin y$: [[§92 Partial Derivatives#^def-92-5|Calc Def. §92.5]]; $\nabla^2 = \nabla\cdot\nabla$ as the divergence of the gradient, [[§111 Curl and Divergence#^def-111-5|Calc Def. §111.5]].
> - The Laplacian in $\mathbb{R}^n$ and the normal derivative, the setting of Green's identities: [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-2|452 Def. §17.2]].
> - Complex-variables version: [[§27★ Harmonic Functions#^def-27-1|342 Def. §27.1]] (the same definition) and [[§27★ Harmonic Functions#^thm-27-1|342 Thm. §27.1]] (the real and imaginary parts of an analytic function are harmonic, the source of closed-form solutions).

Where the equation comes from:
- **Heat.** The two-dimensional heat equation is $u_t = k\nabla^2u$ ([[§42 Three-Dimensional Heat Equation#^thm-42-3|Theorem §42.3]]). A steady-state (time-independent) temperature has $u_t = 0$, hence $\nabla^2u = 0$. This is the two-dimensional version of the steady-state problems of [[§18 Steady-State Temperatures#^def-18-1|§18]], where $\nabla^2u = 0$ reduced to $u'' = 0$.
- **Membranes.** The two-dimensional wave equation is $u_{tt} = c^2\nabla^2u$ ([[§41★ Two-Dimensional Wave Equation꞉ Derivation#^thm-41-1|Theorem §41.1]]). An equilibrium displacement of a membrane has $u_{tt} = 0$, hence $\nabla^2u = 0$.
- **Potentials.** The gravitational potential in empty space and the electrostatic potential in a charge-free region satisfy $\nabla^2u = 0$; hence the name.
- **Ideal flow.** The velocity potential of an incompressible, irrotational flow is harmonic (Example §35.1).

> [!example] Example §35.1: Velocity Potential of an Ideal Fluid
> Let $u$ and $v$ be the $x$- and $y$-components of the velocity of a two-dimensional fluid flow. Under suitable assumptions (incompressible and irrotational flow) they satisfy
>
> $$
> \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} = 0 , \qquad \text{(A)}
> $$
>
> $$
> \frac{\partial u}{\partial y} - \frac{\partial v}{\partial x} = 0 . \qquad \text{(B)}
> $$
>
> Define a **velocity potential** $\phi$ by $u = -\partial\phi/\partial x$, $v = -\partial\phi/\partial y$. Then (B) holds identically and (A) becomes the potential equation.
>
> Indeed, if $\phi$ has continuous second partial derivatives, then $\partial u/\partial y - \partial v/\partial x = -\phi_{xy} + \phi_{yx} = 0$ by the [[Schwarz–Clairaut Theorem|equality of mixed partials]], so (B) is automatic. Substituting into (A),
>
> $$
> \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} = -\phi_{xx} - \phi_{yy} = 0 \qquad\Longleftrightarrow\qquad \nabla^2\phi = 0 .
> $$
>
> So the flow is found by solving the potential equation for $\phi$. On a wall the flow cannot cross, the normal velocity $-\partial\phi/\partial n$ is zero: such walls give the Neumann conditions of Definition §35.2 below. The same derivation, starting from conservation of mass, is [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^rem-17-4|452 §17]] (irrotational flow).
>
> *Powers (p. 257) prints (B) as $\partial u/\partial x - \partial v/\partial x = 0$; the irrotationality condition is $\partial u/\partial y - \partial v/\partial x = 0$, as above.*
>
> *Powers: Exercise 4.1.8*

^ex-35-1

> [!remark]- Connections
> - Complex-variables version: [[§124★ Two-Dimensional Fluid Flow#^prop-124-5|342 Prop. §124.5]] (the velocity potential is harmonic, with the opposite sign convention $\mathbf V = +\nabla\phi$), and the stream function and complex potential in [[§125★ The Stream Function#^def-125-1|342 Def. §125.1]].

Harmonic functions have many special properties. The most important one, the **maximum principle**, says: *if $\nabla^2u = 0$ in a region, then $u$ cannot have a relative maximum or minimum inside the region unless $u$ is constant.* In particular, a point inside the region where $\partial u/\partial x$ and $\partial u/\partial y$ both vanish is a saddle point. It is proved, from the mean value property, in [[§39 Potential in a Disk#^thm-39-5|Theorem §39.5]].

> [!remark] Remark: Why the Maximum Principle Is Plausible
> Think of $u$ as the steady-state temperature in a metal plate. If the temperature at some point were higher than at all nearby points, heat would flow away from the hot point to the cooler points nearby, and the temperature at the hot point would drop. But then the temperature would not be unchanging in time, contradicting the steady state. The same argument rules out a cold spot. Lecture 11.7 lists the other properties to come: the **mean value property**, $u$ at a point equals its average over any circle (or disk) centered there ([[§39 Potential in a Disk#^thm-39-4|Theorem §39.4]]); and harmonic functions are smooth, indeed locally given by power series.

^rem-35-1

## Boundary Value Problems

> [!definition] Definition §35.2: Dirichlet Problem; Neumann Problem
> A complete boundary value problem for the potential equation consists of the equation in a region together with boundary conditions. Along any section of the boundary these may be of any of the three types
>
> $$
> u \ \text{given}, \qquad \frac{\partial u}{\partial n} \ \text{given}, \qquad \text{or} \qquad \alpha u + \beta\frac{\partial u}{\partial n} \ \text{given} ,
> $$
>
> where $\partial u/\partial n$ is the **normal derivative**, the directional derivative in the direction normal (perpendicular) to the boundary. When $u$ is specified along the whole boundary, the problem is called **Dirichlet's problem**; when $\partial u/\partial n$ is specified along the whole boundary, it is **Neumann's problem**.
>
> *Powers: 4.1 (text)*

^def-35-2

> [!remark]- Connections
> - Complex-variables version: [[§116★ Transformations of Harmonic Functions#^def-116-1|342 Def. §116.1]] (the same Dirichlet and Neumann problems), with [[§117★ Transformations of Boundary Conditions#^thm-117-2|342 Thm. §117.2]] (conformal maps preserve the conditions $h = h_0$ and $dh/dn = 0$) and the Neumann problem for a disk solved in [[§140★ Neumann Problems#^thm-140-2|342 Thm. §140.2]].

On the sides of a rectangle $0 < x < a$, $0 < y < b$ the normal derivative is simply $\pm u_x$ (at $x = 0$, $x = a$) or $\pm u_y$ (at $y = 0$, $y = b$); a zero normal derivative means "insulated" for temperatures and "no flow across" for fluids.

> [!theorem] Proposition §35.1: Solutions of Neumann's Problem Are Not Unique
> If $u$ is a solution of Neumann's problem in a region, then so is $u + C$ for every constant $C$.
>
> *Powers: 4.1 (text)*

^prop-35-1

> [!proof]+ Proof
> Derivatives of a constant vanish, so $\nabla^2(u + C) = \nabla^2u = 0$ and $\partial(u + C)/\partial n = \partial u/\partial n$ on the whole boundary.

^pf-35-1

*Uses:* [[§35 Potential Equation#^def-35-2|Def. §35.2]]

For Dirichlet's problem, by contrast, the solution is unique: [[§39 Potential in a Disk#^cor-39-6|Corollary §39.6]].

> [!remark]- Connections
> - Green's first identity proves both facts: a Dirichlet solution is unique, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-17-1|452 Ex. §17.1]], and a Neumann solution is unique up to a constant, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-17-2|452 Ex. §17.2]].
> - The same identity with the first function equal to $1$ ([[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-2|452 Thm. §17.2]]) shows that $\oint \partial u/\partial n \, ds = \iint \nabla^2u \, dA = 0$ for a harmonic $u$: Neumann data can be prescribed only if their integral over the boundary is zero (no net heat flow into a steady-state plate).
> - See also: [[§140★ Neumann Problems#^thm-140-2|342 Thm. §140.2]] (the Neumann problem for a disk, solved up to an arbitrary additive constant $U_0$) and [[§140★ Neumann Problems#^rem-140-1|342 Remark §140.1]] (why the data must have mean zero).

## Harmonic Polynomials

The simplest harmonic functions are polynomials. They are useful for satisfying simple boundary conditions, which reduces the work in rectangle problems ([[§36 Potential in a Rectangle#^rem-36-2|§36]], [[§37 Further Examples for a Rectangle#^ex-37-4|§37]]).

> [!theorem] Proposition §35.2: Harmonic Polynomials of Degree Two
> The polynomial
>
> $$
> p(x, y) = a + bx + cy + dx^2 + exy + fy^2
> $$
>
> satisfies the potential equation if and only if $d + f = 0$. If $p$ is harmonic and is not a polynomial of degree at most one, then at a point where $\partial p/\partial x$ and $\partial p/\partial y$ are both zero the surface $z = p(x, y)$ is saddle shaped.
>
> *Powers: Exercise 4.1.1*

^prop-35-2

> [!proof]+ Proof
> $p_{xx} = 2d$ and $p_{yy} = 2f$, so $\nabla^2p = 2(d + f)$, which is zero exactly when $d + f = 0$.
>
> Now let $f = -d$, and suppose $p_x = p_y = 0$ at $(x_0, y_0)$. Since $p$ is quadratic, its Taylor expansion about $(x_0, y_0)$ is exact:
>
> $$
> p(x_0 + h, y_0 + k) = p(x_0, y_0) + d\,h^2 + e\,hk - d\,k^2 .
> $$
>
> The quadratic form $Q(h, k) = dh^2 + ehk - dk^2$ has discriminant $e^2 - 4d(-d) = e^2 + 4d^2$, which is positive unless $d = e = 0$, that is, unless $p$ has degree at most one. When it is positive, $Q$ takes both signs: along the $h$-axis $Q = dh^2$ and along the $k$-axis $Q = -dk^2$ have opposite signs if $d \ne 0$, and if $d = 0$, $e \ne 0$, then $Q = ehk$ is positive in two opposite quadrants and negative in the other two. So $p$ rises in some directions from $(x_0, y_0)$ and falls in others: a saddle. (In the language of the second derivative test, the Hessian determinant is $p_{xx}p_{yy} - p_{xy}^2 = -4d^2 - e^2 < 0$.)

^pf-35-2

*Uses:* [[§35 Potential Equation#^def-35-1|Def. §35.1]], [[§96 Maximum and Minimum Values#^thm-96-2|Calc Thm. §96.2]] (second derivatives test)

> [!example] Example §35.2: The Harmonic Polynomials x² − y² and xy
> Both $u = x^2 - y^2$ and $u = xy$ satisfy Laplace's equation: for the first, $u_{xx} + u_{yy} = 2 - 2 = 0$; for the second, $u_{xx} = u_{yy} = 0$. They are the cases $d = 1$, $f = -1$ and $e = 1$ of Proposition §35.2, and their graphs are saddles centered at the origin.
>
> On the sides of the rectangle $0 < x < a$, $0 < y < b$ they take the values
>
> | side | $u = x^2 - y^2$ | $u = xy$ |
> |---|---|---|
> | $x = 0$ | $-y^2$ | $0$ |
> | $x = a$ | $a^2 - y^2$ | $ay$ |
> | $y = 0$ | $x^2$ | $0$ |
> | $y = b$ | $x^2 - b^2$ | $bx$ |
>
> So $u = xy$ is the solution of the Dirichlet problem in the rectangle with $u(x, b) = bx$, $u(a, y) = ay$ and $u = 0$ on the other two sides (Powers' Exercise 4.2.7c), found without any series. By the uniqueness of Dirichlet solutions ([[§39 Potential in a Disk#^cor-39-6|Corollary §39.6]]), the series method of [[§36 Potential in a Rectangle#^thm-36-2|Theorem §36.2]] must produce the same function.
>
> *Powers: Exercise 4.1.2*

^ex-35-2

## Polar and Cylindrical Coordinates

For disks and other round regions the potential equation is rewritten in polar coordinates
$$
r = \sqrt{x^2 + y^2}, \qquad \theta = \tan^{-1}\Big(\frac yx\Big), \qquad x = r\cos\theta, \qquad y = r\sin\theta ,
$$
with the convention $r \ge 0$. Define
$$
u(x, y) = u\big(r\cos\theta, r\sin\theta\big) = v(r, \theta) .
$$

> [!theorem] Theorem §35.3: The Laplacian in Polar and Cylindrical Coordinates
> Let $u$ have continuous second partial derivatives, and $v(r, \theta) = u(r\cos\theta, r\sin\theta)$ for $r > 0$. Then
>
> $$
> \begin{aligned}
> \frac{\partial^2u}{\partial x^2} &= \cos^2\theta\,\frac{\partial^2v}{\partial r^2} - \frac{2\sin\theta\cos\theta}{r}\,\frac{\partial^2v}{\partial\theta\,\partial r} + \frac{\sin^2\theta}{r^2}\,\frac{\partial^2v}{\partial\theta^2} + \frac{\sin^2\theta}{r}\,\frac{\partial v}{\partial r} + \frac{2\sin\theta\cos\theta}{r^2}\,\frac{\partial v}{\partial\theta} , \\
> \frac{\partial^2u}{\partial y^2} &= \sin^2\theta\,\frac{\partial^2v}{\partial r^2} + \frac{2\sin\theta\cos\theta}{r}\,\frac{\partial^2v}{\partial\theta\,\partial r} + \frac{\cos^2\theta}{r^2}\,\frac{\partial^2v}{\partial\theta^2} + \frac{\cos^2\theta}{r}\,\frac{\partial v}{\partial r} - \frac{2\sin\theta\cos\theta}{r^2}\,\frac{\partial v}{\partial\theta} ,
> \end{aligned}
> $$
>
> and therefore the **Laplacian in polar coordinates** is
>
> $$
> \nabla^2v = \frac{\partial^2v}{\partial r^2} + \frac1r\frac{\partial v}{\partial r} + \frac{1}{r^2}\frac{\partial^2v}{\partial\theta^2} = \frac1r\frac{\partial}{\partial r}\Big(r\frac{\partial v}{\partial r}\Big) + \frac{1}{r^2}\frac{\partial^2v}{\partial\theta^2} .
> $$
>
> In **cylindrical coordinates** $(r, \theta, z)$, with $x = r\cos\theta$, $y = r\sin\theta$ and $z$ unchanged, the Laplacian is
>
> $$
> \nabla^2v = \frac1r\frac{\partial}{\partial r}\Big(r\frac{\partial v}{\partial r}\Big) + \frac{1}{r^2}\frac{\partial^2v}{\partial\theta^2} + \frac{\partial^2v}{\partial z^2} .
> $$
>
> *Powers (p. 256) prints $2\sin\theta\sin\theta/r^2$ as the coefficient of $\partial v/\partial\theta$ in both second derivatives; the correct coefficient is $\pm 2\sin\theta\cos\theta/r^2$, as above.*
>
> *Powers: 4.1 (text)*

^thm-35-3

> [!proof]+ Proof
> Powers calls the calculation "elementary but tedious" and leaves it as Exercise 7; lecture 11.21 carries it out. Here it is.
>
> **First derivatives of $r$ and $\theta$.** From $r = \sqrt{x^2 + y^2}$ and $\tan\theta = y/x$ (the derivatives of $\theta$ are the same on every branch),
>
> $$
> r_x = \frac xr = \cos\theta, \qquad r_y = \frac yr = \sin\theta, \qquad \theta_x = \frac{-y}{x^2 + y^2} = -\frac{\sin\theta}{r}, \qquad \theta_y = \frac{x}{x^2 + y^2} = \frac{\cos\theta}{r} .
> $$
>
> **First derivatives of $u$.** By the chain rule, $u_x = v_r\,r_x + v_\theta\,\theta_x$ and $u_y = v_r\,r_y + v_\theta\,\theta_y$. So for any function $w(r, \theta)$ of the point,
>
> $$
> \frac{\partial w}{\partial x} = \cos\theta\,\frac{\partial w}{\partial r} - \frac{\sin\theta}{r}\,\frac{\partial w}{\partial\theta}, \qquad \frac{\partial w}{\partial y} = \sin\theta\,\frac{\partial w}{\partial r} + \frac{\cos\theta}{r}\,\frac{\partial w}{\partial\theta} , \qquad (\ast)
> $$
>
> and in particular $u_x = \cos\theta\,v_r - \dfrac{\sin\theta}{r}\,v_\theta$, $u_y = \sin\theta\,v_r + \dfrac{\cos\theta}{r}\,v_\theta$.
>
> **$u_{xx}$.** Apply $(\ast)$ to $w = u_x$. By the product rule, and with $v_{r\theta} = v_{\theta r}$ (equality of mixed partials),
>
> $$
> \frac{\partial u_x}{\partial r} = \cos\theta\,v_{rr} + \frac{\sin\theta}{r^2}\,v_\theta - \frac{\sin\theta}{r}\,v_{r\theta}, \qquad
> \frac{\partial u_x}{\partial\theta} = -\sin\theta\,v_r + \cos\theta\,v_{r\theta} - \frac{\cos\theta}{r}\,v_\theta - \frac{\sin\theta}{r}\,v_{\theta\theta} .
> $$
>
> Hence
>
> $$
> \begin{aligned}
> u_{xx} &= \cos\theta\,\frac{\partial u_x}{\partial r} - \frac{\sin\theta}{r}\,\frac{\partial u_x}{\partial\theta} \\
> &= \cos^2\theta\,v_{rr} + \frac{\sin\theta\cos\theta}{r^2}v_\theta - \frac{\sin\theta\cos\theta}{r}v_{r\theta} + \frac{\sin^2\theta}{r}v_r - \frac{\sin\theta\cos\theta}{r}v_{r\theta} + \frac{\sin\theta\cos\theta}{r^2}v_\theta + \frac{\sin^2\theta}{r^2}v_{\theta\theta} ,
> \end{aligned}
> $$
>
> which collects to the stated formula.
>
> **$u_{yy}$.** In the same way, with $w = u_y$,
>
> $$
> \frac{\partial u_y}{\partial r} = \sin\theta\,v_{rr} - \frac{\cos\theta}{r^2}\,v_\theta + \frac{\cos\theta}{r}\,v_{r\theta}, \qquad
> \frac{\partial u_y}{\partial\theta} = \cos\theta\,v_r + \sin\theta\,v_{r\theta} - \frac{\sin\theta}{r}\,v_\theta + \frac{\cos\theta}{r}\,v_{\theta\theta} ,
> $$
>
> $$
> u_{yy} = \sin\theta\,\frac{\partial u_y}{\partial r} + \frac{\cos\theta}{r}\,\frac{\partial u_y}{\partial\theta}
> = \sin^2\theta\,v_{rr} + \frac{2\sin\theta\cos\theta}{r}v_{r\theta} + \frac{\cos^2\theta}{r^2}v_{\theta\theta} + \frac{\cos^2\theta}{r}v_r - \frac{2\sin\theta\cos\theta}{r^2}v_\theta .
> $$
>
> **The sum.** Adding, the terms in $v_{r\theta}$ and in $v_\theta$ cancel, and $\cos^2\theta + \sin^2\theta = 1$ gives
>
> $$
> u_{xx} + u_{yy} = v_{rr} + \frac1r\,v_r + \frac{1}{r^2}\,v_{\theta\theta} .
> $$
>
> Since $\dfrac1r\dfrac{\partial}{\partial r}(rv_r) = \dfrac1r(v_r + rv_{rr}) = v_{rr} + \dfrac1r v_r$, this is also the second form.
>
> **Cylindrical coordinates.** The change of variables does not involve $z$, so $u_{zz} = v_{zz}$, while $u_{xx} + u_{yy}$ is computed exactly as above with $z$ held fixed. Adding $v_{zz}$ gives the cylindrical formula.

^pf-35-3

*Uses:* [[§10 Composition of Functions and the Chain Rule#^thm-10-2|452 Thm. §10.2]] (chain rule), [[§5 Equality of Mixed Partials#^thm-5-1|452 Thm. §5.1]] (equality of mixed partials)

> [!remark]- Connections
> - The coordinates: [[§65 Polar Coordinates#^def-65-1|Calc Def. §65.1]] (polar), [[§104 Triple Integrals in Cylindrical Coordinates#^def-104-1|Calc Def. §104.1]] (cylindrical). The three-dimensional analogue, the Laplacian in spherical coordinates, is [[§19 The Laplacian in Spherical Coordinates#^thm-19-1|452 Thm. §19.1]], derived there from the divergence theorem instead of the chain rule.
> - The general formula for orthogonal coordinates with scale factors, [[§19 The Laplacian in Spherical Coordinates#^rem-19-3|452 §19]] (Remark: General Orthogonal Coordinates), gives the cylindrical formula at once from $h_r = 1$, $h_\theta = r$, $h_z = 1$.
> - Complex-variables version: [[§116★ Transformations of Harmonic Functions#^prop-116-2|342 Prop. §116.2]] (the Laplacian under an analytic change of variables; with $w = \operatorname{Log} z$ it gives the polar form).

> [!example] Example §35.3: Simple Harmonic Functions in Cartesian and Polar Form
> **(a) Functions of $x$ only.** If $u = u(x)$, the potential equation reduces to $u'' = 0$, so $u(x) = A + Bx$.
>
> **(b) Functions of $r$ only.** If $v = v(r)$, the polar form of Theorem §35.3 reduces to
>
> $$
> \frac1r\frac{d}{dr}\Big(r\frac{dv}{dr}\Big) = 0 \qquad\Longrightarrow\qquad r\frac{dv}{dr} = B \qquad\Longrightarrow\qquad v(r) = A + B\ln r \qquad (r > 0) .
> $$
>
> This is the Cauchy–Euler equation of [[§1★ Homogeneous Linear Equations#^ex-1-3|Example §1.3]](c). The function $\ln r$ is harmonic everywhere except at the origin, where it is unbounded; it is the fundamental solution of the two-dimensional Laplacian, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-5|452 Thm. §17.5]].
>
> **(c) $r^n\cos(n\theta)$ and $r^n\sin(n\theta)$.** For $v = r^n\cos(n\theta)$, $n = 0, 1, 2, \ldots$,
>
> $$
> \frac1r\frac{\partial}{\partial r}\big(r \cdot nr^{n-1}\big)\cos(n\theta) + \frac{1}{r^2}\,r^n\big(-n^2\cos(n\theta)\big) = n^2r^{n-2}\cos(n\theta) - n^2r^{n-2}\cos(n\theta) = 0 ,
> $$
>
> and the same computation works for $r^n\sin(n\theta)$, and for $r^{-n}\cos(n\theta)$, $r^{-n}\sin(n\theta)$ (replace $n$ by $-n$ in the radial factor; the result is again $n^2r^{-n-2} - n^2r^{-n-2} = 0$). The first few are polynomials: $r\cos\theta = x$, $r\sin\theta = y$, $r^2\cos 2\theta = x^2 - y^2$, $r^2\sin 2\theta = 2xy$, recovering Example §35.2. These functions are the building blocks of the disk solution, [[§39 Potential in a Disk#^thm-39-2|Theorem §39.2]].
>
> *Powers: Exercises 4.1.4, 4.1.5 and 4.1.6*

^ex-35-3
