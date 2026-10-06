---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 5
section: 29
tags: [multivariable-analysis, math452]
---
← [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities]] · ↑ [[· 5 Line Integrals and the Divergence Theorem]] · [[§30 Radial Functions]] →

## Physical Application: Conservation of Mass and Laplace's Equation

### Flux and the Continuity Equation

Consider a fluid with density $\rho(x, y, t)$ and velocity field $\mathbf{u}(x, y, t)$. Let $D$ be a fixed region in the plane with boundary $\gamma$.

> [!theorem] Theorem §29.1: Continuity Equation / Conservation of Mass
> $$
> \boxed{\rho_t + \nabla \cdot (\rho \mathbf{u}) = 0}
> $$

^thm-29-1

> [!proof]+ Proof
> **Rate of outflow of volume** across $\gamma$: if the flow speed is $u$ in a pipe of cross-section $S$, the volume displaced in time $T$ is $uTS$, so the volume flux per unit time is $uS$. For a general boundary:
>
> $$
> \text{rate of outflow of volume} = \oint_\gamma \mathbf{u} \cdot \hat{n} \, ds.
> $$
>
> **Rate of outflow of mass** across $\gamma$: weight by density:
>
> $$
> \text{rate of outflow of mass} = \oint_\gamma \rho \, \mathbf{u} \cdot \hat{n} \, ds.
> $$
>
> **Mass in $D$:**
>
> $$
> \text{mass in } D = \iint_D \rho \, dx \, dy.
> $$
>
> **Rate of change of mass in $D$:**
>
> $$
> \frac{d}{dt} \iint_D \rho \, dx \, dy = \iint_D \rho_t \, dx \, dy.
> $$
>
> This differentiates under the integral sign, which is justified when $\rho_t$ is continuous: on the compact set $\overline{D} \times [t_0 - 1, t_0 + 1]$ it is [[§18 Compact Spaces#^rem-18-1|uniformly continuous]], so the difference quotients $(\rho(\cdot, t) - \rho(\cdot, t_0))/(t - t_0)$ converge to $\rho_t(\cdot, t_0)$ uniformly on $\overline{D}$ (by the [[Mean Value Theorem]]).
>
> If there are no sources or sinks (mass is neither created nor destroyed), then conservation of mass says:
>
> $$
> \underbrace{\frac{d}{dt} \iint_D \rho \, dx \, dy}_{\text{rate of change of mass in } D} + \underbrace{\oint_\gamma \rho \, \mathbf{u} \cdot \hat{n} \, ds}_{\text{rate of outflow of mass}} = 0. \tag{①+②=0}
> $$
>
> Now apply the [[§27 Line Integrals and Green's Theorem#^thm-27-2|Divergence Theorem]] to ②:
>
> $$
> \oint_\gamma \rho \, \mathbf{u} \cdot \hat{n} \, ds = \oint_\gamma (\rho \mathbf{u}) \cdot \hat{n} \, ds = \iint_D \nabla \cdot (\rho \mathbf{u}) \, dx \, dy.
> $$
>
> Substituting both terms:
>
> $$
> \iint_D \big( \rho_t + \nabla \cdot (\rho \mathbf{u}) \big) \, dx \, dy = 0 \qquad \text{for }\textbf{any}\text{ domain } D.
> $$
>
> **Key argument:** If $\iint_D f \, dx \, dy = 0$ for every domain $D$ and $f$ is continuous, then $f \equiv 0$. (If $f(\mathbf{p}) > 0$ at a point $\mathbf{p}$, then by [[§3 Continuity and Limits of Functions#^def-3-1|continuity]] $f \geq f(\mathbf{p})/2 > 0$ on some [[§2 Open and Closed Sets#^def-2-1|ball]] $B_\delta(\mathbf{p})$; taking $D = B_\delta(\mathbf{p})$ gives a [[§22 Properties of the Integral#^thm-22-4|positive integral]] — contradiction. Similarly if $f(\mathbf{p}) < 0$.)
>
> Therefore, the integrand vanishes pointwise, which is the equation of the theorem.

^pf-29-1

*Uses:* [[§27 Line Integrals and Green's Theorem#^thm-27-2|§27.2]], [[§3 Continuity and Limits of Functions#^def-3-1|Def. §3.1]], [[§2 Open and Closed Sets#^def-2-1|Def. §2.1]], [[§22 Properties of the Integral#^thm-22-4|§22.4]]

> [!remark]- Connections
> - Computational version: the same argument for heat in a solid, [[§52 Three-Dimensional Heat Equation#^lem-52-1|341 Lemma §52.1]] (a continuous function with zero integral over every subregion is zero) and [[§52 Three-Dimensional Heat Equation#^thm-52-2|341 Thm. §52.2]] (the local heat balance).

This is the **continuity equation**: the local form of conservation of mass.

### Incompressible Flow

Assume the fluid has constant density $\rho \equiv 1$ (incompressible). Then $\rho_t = 0$ and $\nabla \cdot (\rho \mathbf{u}) = \nabla \cdot \mathbf{u}$, so the continuity equation reduces to:

$$
\nabla \cdot \mathbf{u} = 0 \qquad \text{(divergence-free / incompressible)}.
$$

### Irrotational Flow

An additional physical condition: the flow is **[[§13 The Three Differential Operators꞉ Gradient, Curl, Divergence#^def-13-2|irrotational]]** (no rotation), meaning:

$$
\nabla \times \mathbf{u} = 0 \qquad \text{(curl-free / irrotational)}.
$$

Writing $\mathbf{u} = (u, v)$, the two conditions become the system:

$$
\begin{cases} u_x + v_y = 0 & (\text{divergence-free}) \\ v_x - u_y = 0 & (\text{curl-free}) \end{cases}
$$

### From Potential Functions to Laplace's Equation

**Physical motivation:** If the flow is driven by a potential (e.g., gravity), there exists a **potential function** $\phi(x,y)$ such that contour lines $\phi(x,y) = c$ are level curves of energy. The gradient $\nabla \phi = (\phi_x, \phi_y)$ points in the direction of increasing energy, and the fluid flows in the *opposite* direction:

$$
\mathbf{u} = (u, v) = -\nabla \phi = (-\phi_x, -\phi_y).
$$

**Check curl-free:** With $u = -\phi_x$ and $v = -\phi_y$:

$$
v_x - u_y = -\phi_{yx} - (-\phi_{xy}) = -\phi_{yx} + \phi_{xy} = 0
$$

by [[Schwarz–Clairaut Theorem|equality of mixed partials]]. So the curl-free condition is *automatically satisfied* for any potential function. This is a [[§13 The Three Differential Operators꞉ Gradient, Curl, Divergence|general fact]]: $\nabla \times (\nabla \phi) = 0$ always.

**Apply the divergence-free condition:**

$$
u_x + v_y = -\phi_{xx} - \phi_{yy} = 0 \qquad \Longleftrightarrow \qquad \boxed{\Delta \phi = \phi_{xx} + \phi_{yy} = 0.}
$$

This is **Laplace's equation**. A function satisfying $\Delta \phi = 0$ is called **harmonic**.

> [!remark] Remark: Summary of the Logical Chain
> $$
> \text{Conservation of mass} + \text{incompressible} + \text{irrotational} \quad \Longrightarrow \quad \text{Laplace's equation } \Delta \phi = 0.
> $$
>
> The problem of finding incompressible irrotational flow reduces to: find a potential function $\phi(x,y)$ satisfying $\Delta \phi = 0$ with appropriate boundary conditions. This is the **Dirichlet problem**, whose [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-28-1|uniqueness]] we proved using [[Green's First Identity|Green's first identity]].

^rem-29-4

> [!remark]- Connections
> - Computational version: [[§44 Potential Equation#^ex-44-1|341 Ex. §44.1]] (the velocity potential of an ideal fluid satisfies the potential equation).
> - Computational version in the plane: [[§124★ Two-Dimensional Fluid Flow#^prop-124-5|342 Prop. §124.5]] (for incompressible irrotational flow the velocity potential is harmonic, and the flow is described by an analytic complex potential).

> [!remark] Remark: Symmetry and Radial Solutions
> Laplace's equation $\phi_{xx} + \phi_{yy} = 0$ has a symmetric structure: the operator $\Delta$ treats $x$ and $y$ on equal footing. This symmetry motivates looking for **radial solutions**, i.e., solutions depending only on $r = \sqrt{x^2 + y^2}$: $\phi(x,y) = f(r)$.

^rem-29-5

> [!theorem] Theorem §29.2: Fundamental Solution of the 2D Laplacian
> The function
>
> $$
> \phi(x,y) = C \ln r = C \ln \sqrt{x^2 + y^2}
> $$
>
> satisfies Laplace's equation $\Delta \phi = 0$ for all $(x,y) \neq (0,0)$.

^thm-29-2

> [!proof]+ Proof
> **Computing $\Delta \phi$ for a Radial Function.**
>
> Let $\phi(x,y) = f(r)$ where $r = \sqrt{x^2 + y^2}$. We compute $\phi_{xx}$ and $\phi_{yy}$ via the [[Multivariable Chain Rule|chain rule]].
>
> **First derivatives of $r$:**
>
> $$
> r_x = \frac{x}{r}, \qquad r_y = \frac{y}{r}.
> $$
>
> **Second derivatives of $r$:**
>
> $$
> r_{xx} = \frac{\partial}{\partial x}\left(\frac{x}{r}\right) = \frac{r - x \cdot (x/r)}{r^2} = \frac{r^2 - x^2}{r^3}, \qquad r_{yy} = \frac{r^2 - y^2}{r^3}.
> $$
>
> **First derivative of $\phi$:**
>
> $$
> \phi_x = f'(r) \cdot r_x = f'(r) \cdot \frac{x}{r}.
> $$
>
> **Second derivative of $\phi$:** Using the [[§8 Algebra of Differentiable Functions#^thm-8-2|product rule]] on $\phi_x = f'(r) \cdot r_x$:
>
> $$
> \begin{aligned}
> \phi_{xx} &= \frac{\partial}{\partial x}\big(f'(r) \cdot r_x\big) = \big(f'(r)\big)_x \cdot r_x + f'(r) \cdot r_{xx} \\
> &= f''(r) \cdot r_x \cdot r_x + f'(r) \cdot r_{xx} \\
> &= f''(r) \cdot \frac{x^2}{r^2} + f'(r) \cdot \frac{r^2 - x^2}{r^3}.
> \end{aligned}
> $$
>
> By the same argument (replacing $x$ with $y$):
>
> $$
> \phi_{yy} = f''(r) \cdot \frac{y^2}{r^2} + f'(r) \cdot \frac{r^2 - y^2}{r^3}.
> $$
>
> **The Laplacian:**
>
> $$
> \begin{aligned}
> \Delta \phi = \phi_{xx} + \phi_{yy} &= f''(r) \cdot \frac{x^2 + y^2}{r^2} + f'(r) \cdot \frac{2r^2 - x^2 - y^2}{r^3} \\
> &= f''(r) \cdot \frac{r^2}{r^2} + f'(r) \cdot \frac{2r^2 - r^2}{r^3} \\
> &= f''(r) + \frac{f'(r)}{r}.
> \end{aligned}
> $$
>
> **Solving the Radial ODE.**
>
> Setting $\Delta \phi = 0$:
>
> $$
> f''(r) + \frac{1}{r} f'(r) = 0.
> $$
>
> **Step 1: Reduce order.** Let $g(r) = f'(r)$. Then:
>
> $$
> g'(r) + \frac{g(r)}{r} = 0.
> $$
>
> **Step 2: Separate variables.**
>
> $$
> \frac{dg}{g} = -\frac{dr}{r}.
> $$
>
> **Step 3: Integrate both sides.**
>
> $$
> \ln|g| = -\ln|r| + C_1 \qquad \Longrightarrow \qquad |g| = e^{C_1} \cdot \frac{1}{r} = \frac{C_2}{r}.
> $$
>
> So $g(r) = C/r$ for some constant $C$. (Step 2 divides by $g$, assuming $g \neq 0$; the solution $g \equiv 0$ is included as $C = 0$. More directly, $g' + g/r = 0$ says $(rg)' = 0$, so $rg$ is constant for $r > 0$.)
>
> **Verification:** $g'(r) = -C/r^2$, so $g'(r) + g(r)/r = -C/r^2 + C/r^2 = 0$. ✓
>
> **Step 4: Recover $f$.**
>
> $$
> f'(r) = g(r) = \frac{C}{r} \qquad \Longrightarrow \qquad f(r) = C \ln r + C'.
> $$
>
> Choosing $C' = 0$ gives the function of the theorem.

^pf-29-2

*Uses:* [[Multivariable Chain Rule|§12.2]], [[§8 Algebra of Differentiable Functions#^thm-8-2|§8.2]], [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-28-3|Def. §28.3]]

> [!remark]- Connections
> - The 3D radial computation (giving $f'' + \frac{2}{r} f'$ and the solution $1/r$): [[§33 The Laplacian in Spherical Coordinates#^rem-33-2|Verification: Radial Functions]], from the [[§33 The Laplacian in Spherical Coordinates#^thm-33-1|Laplacian in Spherical Coordinates (§33.1)]].
> - Computational version: [[§44 Potential Equation#^ex-44-3|341 Ex. §44.3]](b) (the radial harmonic functions $A+B\ln r$, from the polar form of the Laplacian).
> - Computational version: [[§122★ Electrostatic Potential#^ex-122-1|342 Ex. §122.1]] (the potential A ln r + B between coaxial cylinders) and [[§140★ Neumann Problems#^def-140-1|342 Def. §140.1]] (the Neumann kernel of the disk, a multiple of the fundamental solution).
> - Used in Electromagnetism: the potential of a line charge, the image of a line charge in a cylinder, and line sources as singularities of the complex potential — [[§C2.2 Gauss's Law and the Solid Angle#^thm-c2-2-4|EM Theorem §C2.2.4]], [[§C7.1 The Method of Images#^thm-c7-1-6|EM Theorem §C7.1.6]], [[§C7.5★ Logarithmic Potentials and the Poisson–Boltzmann Equation#^thm-c7-5-1|EM Theorem §C7.5.1]].

> [!remark] Remark: Connection to Other PDEs
> This fundamental solution is the starting point for solving boundary value problems via Green's functions. The same approach — exploit symmetry to reduce a PDE to an ODE — applies to other equations:
> - **Laplace's equation** $\Delta \phi = 0$: steady-state (time-independent) problems.
> - **Heat equation** $\phi_t = \Delta \phi$: diffusion and heat conduction (time-dependent).
> - **Wave equation** $\phi_{tt} = c^2 \Delta \phi$: vibrations and wave propagation.

^rem-29-6

> [!remark]- Connections
> - Worked out in Fourier Series and PDEs: Green's functions for one-dimensional boundary value problems, [[§7★ Green's Functions#^def-7-2|341 Def. §7.2]] and [[§7★ Green's Functions#^thm-7-1|341 Thm. §7.1]]; the heat and wave equations on an interval, solved by separation of variables, [[§25 Example꞉ Fixed End Temperatures#^thm-25-5|341 Thm. §25.5]] and [[§38 Solution of the Vibrating String Problem#^thm-38-2|341 Thm. §38.2]].
