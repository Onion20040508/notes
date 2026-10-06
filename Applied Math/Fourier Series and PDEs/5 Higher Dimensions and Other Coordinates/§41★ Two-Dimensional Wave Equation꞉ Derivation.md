---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 5
section: 41
powers: "5.1"
aliases: ["Powers 5.1"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§40★ Classification and Limitations]] · ↑ [[· 5 Higher Dimensions and Other Coordinates]] · [[§42 Three-Dimensional Heat Equation]] →

*Powers, Section 5.1.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

This section derives the equation of a vibrating membrane, such as a drumhead or a soap film stretched over a frame. Newton's second law for a small rectangle of membrane, pulled along its four edges by the surface tension, gives $u_{xx} + u_{yy} = u_{tt}/c^2$ with $c^2 = \sigma/\rho$. It is the two-dimensional version of the vibrating string of [[§29 The Vibrating String|§29]], and the derivation makes the same assumption of small slopes, so the equation describes small vibrations. The membrane problem is solved on a rectangle at the end of [[§43 Two-Dimensional Heat Equation꞉ Solution#^rem-43-3|§43]], and on a disk, where Bessel functions appear, in [[§47★ Vibrations of a Circular Membrane#^prop-47-4|Proposition §47.4]].

## The Membrane

> [!definition] Definition §41.1: Stretched Membrane
> A **membrane** is stretched taut over a flat frame in the $xy$-plane; its displacement above the point $(x, y)$ at time $t$ is $u(x, y, t)$. The model assumes:
> 1. The **surface tension** $\sigma$ (dimensions $F/L$, force per unit length) is constant and independent of position. Across any short segment of length $\ell$ in the membrane, the rest of the membrane pulls with a force of magnitude $\sigma\ell$, tangent to the membrane and perpendicular to the segment.
> 2. The membrane is **perfectly flexible**: it does not resist bending, so the tension is the only internal force.
> 3. The membrane has **surface density** $\rho$ (dimensions $m/L^2$, mass per unit area).
>
> A soap film satisfies these assumptions quite accurately.
>
> *Powers: 5.1 (text)*

^def-41-1

## Newton's Law for a Small Rectangle

Cut out a small rectangle of membrane of dimensions $\Delta x$ by $\Delta y$, aligned with the coordinate axes, with corner above $(x, y)$. On each edge the rest of the membrane exerts a distributed force of magnitude $\sigma$ per unit length, which adds up to a concentrated force $\sigma\,\Delta y$ on each of the two edges parallel to the $y$-axis and $\sigma\,\Delta x$ on each of the two edges parallel to the $x$-axis. Projected on the $xu$-plane (figure below), the forces $\sigma\,\Delta y$ at $x$ and $x + \Delta x$ make angles $\alpha$ and $\beta$ with the horizontal; projected on the $yu$-plane, the forces $\sigma\,\Delta x$ at $y$ and $y + \Delta y$ make angles $\gamma$ and $\delta$.

> [!theorem] Theorem §41.1: The Two-Dimensional Wave Equation
> Under the assumptions of Definition §41.1, and if the slopes $\partial u/\partial x$ and $\partial u/\partial y$ of the membrane are small, the displacement satisfies
>
> $$
> \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2}, \qquad c^2 = \frac{\sigma}{\rho} ,
> $$
>
> that is, $\nabla^2 u = u_{tt}/c^2$. This is the **two-dimensional wave equation**; $c$ is the wave speed.
>
> *Powers: 5.1 (text)*

^thm-41-1

> [!proof]+ Proof
> *Powers gives this as a derivation from Newton's law; the small-angle approximations are part of the model, and the equation is exact only in the limit of small slopes.*
>
> **Horizontal forces.** The sum of the forces in the $x$-direction is $\sigma\,\Delta y\,(\cos\beta - \cos\alpha)$, and in the $y$-direction it is $\sigma\,\Delta x\,(\cos\delta - \cos\gamma)$. The membrane is to move only vertically, so these sums should be zero or at least negligible. This holds if $\alpha, \beta, \gamma, \delta$ are all small, since then $\cos\theta = 1 - \theta^2/2 + \cdots$ and the differences of cosines are of second order. Since
>
> $$
> \tan\alpha = \frac{\partial u}{\partial x}, \qquad \tan\gamma = \frac{\partial u}{\partial y}
> $$
>
> (and so on), with the derivatives evaluated at an appropriate point near $(x, y)$, this is the assumption that the slopes of the membrane are very small.
>
> **Vertical forces.** The vertical components of the four forces add up to the mass $\rho\,\Delta x\,\Delta y$ times the vertical acceleration:
>
> $$
> \sigma\,\Delta y\,\big(\sin\beta - \sin\alpha\big) + \sigma\,\Delta x\,\big(\sin\delta - \sin\gamma\big) = \rho\,\Delta x\,\Delta y\,\frac{\partial^2 u}{\partial t^2} .
> $$
>
> **Small angles.** For a small angle the sine is approximately equal to the tangent: $\sin\theta = \tan\theta/\sqrt{1 + \tan^2\theta} = \tan\theta\,\big(1 + O(\tan^2\theta)\big)$. So
>
> $$
> \sin\alpha \cong \frac{\partial u}{\partial x}(x, y, t), \quad \sin\beta \cong \frac{\partial u}{\partial x}(x + \Delta x, y, t), \quad \sin\gamma \cong \frac{\partial u}{\partial y}(x, y, t), \quad \sin\delta \cong \frac{\partial u}{\partial y}(x, y + \Delta y, t),
> $$
>
> and with these approximations the balance of vertical forces becomes
>
> $$
> \sigma\,\Delta y\Big(\frac{\partial u}{\partial x}(x + \Delta x, y, t) - \frac{\partial u}{\partial x}(x, y, t)\Big) + \sigma\,\Delta x\Big(\frac{\partial u}{\partial y}(x, y + \Delta y, t) - \frac{\partial u}{\partial y}(x, y, t)\Big) = \rho\,\Delta x\,\Delta y\,\frac{\partial^2 u}{\partial t^2} .
> $$
>
> (Powers prints $\partial y/\partial x$ for the first derivative here; it is $\partial u/\partial x$.)
>
> **Limit.** Dividing by $\Delta x\,\Delta y$ leaves two difference quotients on the left, of $\partial u/\partial x$ in $x$ and of $\partial u/\partial y$ in $y$. As $\Delta x, \Delta y \to 0$ they tend to partial derivatives, and
>
> $$
> \sigma\Big(\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}\Big) = \rho\,\frac{\partial^2 u}{\partial t^2} .
> $$
>
> Dividing by $\sigma$ and writing $\rho/\sigma = 1/c^2$ gives the wave equation. (As for the string, the acceleration varies over the rectangle; if $u_{tt}$ is continuous, its value at any point of the rectangle tends to $u_{tt}(x, y, t)$ in the limit.)

^pf-41-1

*Uses:* [[§41★ Two-Dimensional Wave Equation꞉ Derivation#^def-41-1|Def. §41.1]]

![[m341-41-1.svg]]
*The piece of membrane seen in the $xu$-plane. The forces $\sigma\,\Delta y$ on the edges at $x$ and $x + \Delta x$ pull along the membrane at angles $\alpha$ and $\beta$ to the horizontal. Where the membrane curves upward, $\beta > \alpha$, and the net vertical force $\sigma\,\Delta y\,(\sin\beta - \sin\alpha) \approx \sigma\,\Delta y\,\big(u_x(x + \Delta x) - u_x(x)\big)$ is upward: this gives the $u_{xx}$ term. The same picture in the $yu$-plane, with $\sigma\,\Delta x$, $\gamma$ and $\delta$, gives $u_{yy}$.*

> [!remark]- Connections
> - The one-dimensional derivation, with the tension $T$ of a string in place of $\sigma\,\Delta y$: [[§29 The Vibrating String#^thm-29-1|Theorem §29.1]], which gives $u_{xx} = u_{tt}/c^2$ with $c^2 = T/\rho$ ([[§29 The Vibrating String#^def-29-2|Def. §29.2]]).
> - The left side is the Laplacian, [[§111 Curl and Divergence#^def-111-5|Calc Def. §111.5]], [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-new1|452 Def. §17.2]]. The equation says that the membrane accelerates toward the average height of its neighbors: $\nabla^2u(x, y)$ is, up to a positive factor, the limit of (average of $u$ on a small circle about $(x, y)$) minus $u(x, y)$, divided by the squared radius.

> [!remark] Remark: The Wave Equation in Three Dimensions
> The same pattern continues in space: the three-dimensional wave equation is
>
> $$
> \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} = \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2} ,
> $$
>
> or $\nabla^2u = u_{tt}/c^2$ with the three-dimensional Laplacian. There is no membrane to derive it from; it governs, for example, small pressure disturbances in a gas (sound, with $c$ the speed of sound) and each component of the electric and magnetic fields in vacuum ($c$ the speed of light). In every case the acceleration of the disturbance is proportional to its Laplacian (Powers' Exercise 5.1.3).

^rem-41-1

## Boundary and Initial Conditions

> [!definition] Definition §41.2: The Membrane Problem
> If the membrane is fixed to the flat frame, its displacement $u(x, y, t)$ on the region $R$ inside the frame satisfies the wave equation of Theorem §41.1 in $R$, the **boundary condition**
>
> $$
> u(x, y, t) = 0 \qquad \text{for } (x, y) \text{ on the boundary of } R,\ t > 0 ,
> $$
>
> and the **initial conditions** describing the displacement and velocity of each point of the membrane at $t = 0$:
>
> $$
> u(x, y, 0) = f(x, y), \qquad \frac{\partial u}{\partial t}(x, y, 0) = g(x, y), \qquad (x, y) \text{ in } R .
> $$
>
> As for the string, two initial conditions are needed because the equation is of second order in $t$.
>
> *Powers: 5.1 (text)*

^def-41-2

> [!example] Example §41.1: A Rectangular Frame
> Suppose the frame is rectangular, bounded by segments of the lines $x = 0$, $x = a$, $y = 0$, $y = b$. Write the initial value–boundary value problem, complete with inequalities, for a membrane stretched over this frame.
>
> The region is $R\colon 0 < x < a$, $0 < y < b$, and its boundary consists of the four sides. By Definition §41.2,
>
> $$
> \begin{aligned}
> &\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2}, && 0 < x < a, \quad 0 < y < b, \quad 0 < t, \\
> &u(0, y, t) = 0, \quad u(a, y, t) = 0, && 0 < y < b, \quad 0 < t, \\
> &u(x, 0, t) = 0, \quad u(x, b, t) = 0, && 0 < x < a, \quad 0 < t, \\
> &u(x, y, 0) = f(x, y), \quad \frac{\partial u}{\partial t}(x, y, 0) = g(x, y), && 0 < x < a, \quad 0 < y < b .
> \end{aligned}
> $$
>
> The boundary conditions are imposed on the open sides; the equation holds only inside. The boundary conditions are homogeneous, so separation of variables applies; the product solutions and the frequencies of this membrane are found in [[§43 Two-Dimensional Heat Equation꞉ Solution#^rem-43-3|Remark: The Rectangular Membrane]] of §43.
>
> *Powers: Exercise 5.1.1*

^ex-41-1

> [!example] Example §41.2: A Circular Frame
> Suppose the frame is the circle $x^2 + y^2 = a^2$. Write the initial value–boundary value problem in polar coordinates.
>
> Put $v(r, \theta, t) = u(r\cos\theta, r\sin\theta, t)$. By [[§35 Potential Equation#^thm-35-3|Theorem §35.3]], the Laplacian in polar coordinates is $\nabla^2 v = \frac{1}{r}\frac{\partial}{\partial r}\big(r\frac{\partial v}{\partial r}\big) + \frac{1}{r^2}\frac{\partial^2 v}{\partial\theta^2}$, so
>
> $$
> \begin{aligned}
> &\frac{1}{r}\frac{\partial}{\partial r}\Big(r\frac{\partial v}{\partial r}\Big) + \frac{1}{r^2}\frac{\partial^2 v}{\partial\theta^2} = \frac{1}{c^2}\frac{\partial^2 v}{\partial t^2}, && 0 < r < a, \quad -\pi < \theta \le \pi, \quad 0 < t, \\
> &v(a, \theta, t) = 0, && -\pi < \theta \le \pi, \quad 0 < t, \\
> &v(r, \theta + 2\pi, t) = v(r, \theta, t), && 0 < r < a, \quad 0 < t, \\
> &v(r, \theta, t) \text{ bounded as } r \to 0^+, && 0 < t, \\
> &v(r, \theta, 0) = f(r, \theta), \quad \frac{\partial v}{\partial t}(r, \theta, 0) = g(r, \theta), && 0 < r < a .
> \end{aligned}
> $$
>
> Only $r = a$ is a real boundary. The two extra conditions come from the coordinates, as for the potential in a disk ([[§39 Potential in a Disk|§39]]): $\theta$ and $\theta + 2\pi$ name the same point, so $v$ must be $2\pi$-periodic in $\theta$; and the coefficients $1/r$, $1/r^2$ blow up at the center, where the membrane is nevertheless an ordinary interior point, so $v$ is required to stay bounded there. This problem is taken up in [[§44★ Problems in Polar Coordinates#^def-44-1|Definition §44.1]] and solved in [[§47★ Vibrations of a Circular Membrane#^prop-47-4|Proposition §47.4]].
>
> *Powers: Exercise 5.1.2*

^ex-41-2

> [!example] Example §41.3: The Wave Speed of a Membrane
> Check that $c$ has the dimensions of a velocity, and compute it for a membrane with $\sigma = 500\ \mathrm{N/m}$ and $\rho = 0.2\ \mathrm{kg/m^2}$.
>
> Force has dimensions $mL/t^2$, so $\sigma$ has dimensions $(mL/t^2)/L = m/t^2$, and $\rho$ has dimensions $m/L^2$. Hence
>
> $$
> c^2 = \frac{\sigma}{\rho} \quad\text{has dimensions}\quad \frac{m/t^2}{m/L^2} = \frac{L^2}{t^2} ,
> $$
>
> and $c$ is a velocity, $L/t$. Each term of the wave equation then has dimensions $L/L^2 = 1/L$: $u_{xx}$ and $u_{yy}$ directly, and $u_{tt}/c^2$ as $(L/t^2)(t^2/L^2)$. For the given membrane, $c^2 = 500/0.2 = 2500\ \mathrm{m^2/s^2}$, so $c = 50\ \mathrm{m/s}$. Since $c \propto \sqrt{\sigma}$, tightening the membrane to four times the tension doubles the wave speed, and with it every frequency of vibration ([[§43 Two-Dimensional Heat Equation꞉ Solution#^rem-43-3|§43]]): this is how a drum is tuned.
>
> *Powers: 5.1 (text)*

^ex-41-3
