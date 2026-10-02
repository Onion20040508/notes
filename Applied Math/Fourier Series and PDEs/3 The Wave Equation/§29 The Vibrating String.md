---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 3
section: 29
powers: "3.1"
aliases: ["Powers 3.1"]
tags: [fourier-series-and-pdes, math341]
---
← [[§28★ The Error Function]] · ↑ [[· 3 The Wave Equation]] · [[§30 Solution of the Vibrating String Problem]] →

*Powers, Section 3.1 · MAT 341 lecture 10.29 · HW 10.*

This section derives the equation of motion of a taut string, like a guitar or violin string, from Newton's second law applied to a short piece of it. The result is the one-dimensional **wave equation** $u_{xx} = u_{tt}/c^2$, where $u(x, t)$ is the transverse displacement and $c^2 = T/\rho$ is tension over linear density; $c$ turns out to be the speed at which waves travel along the string ([[§31 d'Alembert's Solution#^def-31-1|Definition §31.1]]). Because Newton's law is second order in time, the problem needs two initial conditions, the initial shape and the initial velocity, where the heat equation needed one. The same derivation with extra forces gives the forced and the damped string, which reappear in the course problems [[§32 One-Dimensional Wave Equation꞉ Generalities#^ex-32-2|Example §32.2]] and [[§32 One-Dimensional Wave Equation꞉ Generalities#^ex-32-3|Example §32.3]].

## Derivation of the Equation of Motion

> [!definition] Definition §29.1: The Model of a Vibrating String
> A string is stretched along the $x$-axis between $x = 0$ and $x = a$. Its **transverse displacement** $u(x, t)$ is measured up from the $x$-axis. The modelling assumptions are:
> 1. The string is **perfectly flexible**: it offers no resistance to bending, so the only force one part of the string exerts on the next is a pull, the **tension**, acting tangentially to the centerline of the string. Its magnitude is $T(x, t)$, and $\phi(x, t)$ denotes the angle between the tangent and the horizontal.
> 2. Each point of the string moves only in the vertical direction, so the horizontal acceleration is zero.
> 3. The only external force is gravity, acting perpendicular to the $x$-direction.
> 4. The mass of a short piece of length $\Delta x$ is $m = \rho\,\Delta x$, where $\rho$ is the **linear density** (mass per unit length).
>
> Since $\tan\phi(x, t)$ is the slope of the string at $(x, t)$,
>
> $$
> \tan\big(\phi(x, t)\big) = \frac{\partial u}{\partial x}(x, t) .
> $$
>
> *Powers: 3.1 (text)*

^def-29-1

![[m341-29-1.svg]]
*Forces on the piece of string between $x$ and $x + \Delta x$: tensions $T(x, t)$ and $T(x + \Delta x, t)$ along the tangents, at angles $\alpha = \phi(x, t)$ and $\beta = \phi(x + \Delta x, t)$ to the horizontal, and the weight $mg$. When the string bends upward ($\beta > \alpha$), the vertical components of the tensions do not cancel, and the net force accelerates the piece.*

> [!theorem] Theorem §29.1: Equation of Motion of the String
> Under the assumptions of Definition §29.1, the horizontal component of the tension is a constant $T$,
>
> $$
> T(x, t)\cos\big(\phi(x, t)\big) = T(x + \Delta x, t)\cos\big(\phi(x + \Delta x, t)\big) = T , \qquad (1)
> $$
>
> and the displacement satisfies
>
> $$
> T\frac{\partial^2 u}{\partial x^2} = \rho\frac{\partial^2 u}{\partial t^2} + \rho g , \qquad (4)
> $$
>
> or, with $c^2 = T/\rho$,
>
> $$
> \frac{\partial^2 u}{\partial x^2} = \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2} + \frac{1}{c^2}g . \qquad (5)
> $$
>
> *Powers: 3.1, Equations (1)–(5)*

^thm-29-1

> [!proof]+ Proof
> Apply Newton's second law to the piece of string between $x$ and $x + \Delta x$ (figure above). The rest of the string pulls on its left end with force $T(x, t)$ directed down and to the left along the tangent, at angle $\phi(x, t)$ below the horizontal, and on its right end with force $T(x + \Delta x, t)$ directed up and to the right, at angle $\phi(x + \Delta x, t)$ above it.
>
> **Horizontal direction.** The horizontal acceleration is zero (assumption 2) and gravity is vertical, so
>
> $$
> -T(x, t)\cos\big(\phi(x, t)\big) + T(x + \Delta x, t)\cos\big(\phi(x + \Delta x, t)\big) = 0 .
> $$
>
> This is (1): the horizontal component of tension is the same at every point, independent of $x$. It could still depend on $t$, but for a taut string it can vary only slightly with $t$, and it is assumed constant, $T$.
>
> **Vertical direction.** Since $u$ measures vertical displacement, $\partial^2u/\partial t^2$ is the vertical acceleration, and
>
> $$
> -T(x, t)\sin\big(\phi(x, t)\big) + T(x + \Delta x, t)\sin\big(\phi(x + \Delta x, t)\big) - mg = m\frac{\partial^2 u}{\partial t^2}(x, t) . \qquad (2)
> $$
>
> By (1), $T(x, t) = T/\cos(\phi(x, t))$ and $T(x + \Delta x, t) = T/\cos(\phi(x + \Delta x, t))$. Substituting these and $m = \rho\,\Delta x$ into (2),
>
> $$
> -T\tan\big(\phi(x, t)\big) + T\tan\big(\phi(x + \Delta x, t)\big) - \rho\,\Delta x\,g = \rho\,\Delta x\frac{\partial^2 u}{\partial t^2} . \qquad (3)
> $$
>
> Replace each tangent by the slope $\partial u/\partial x$ (Definition §29.1) and divide by $\Delta x$:
>
> $$
> \frac{T}{\Delta x}\Big(\frac{\partial u}{\partial x}(x + \Delta x, t) - \frac{\partial u}{\partial x}(x, t)\Big) = \rho\Big(\frac{\partial^2 u}{\partial t^2} + g\Big) .
> $$
>
> The left side is $T$ times a difference quotient of $\partial u/\partial x$; as $\Delta x \to 0$ it tends to $T\,\partial^2 u/\partial x^2(x, t)$, which is (4). Dividing (4) by $T$ and writing $\rho/T = 1/c^2$ gives (5).
>
> Two approximations are hidden in the model. The mass $\rho\,\Delta x$ is the mass of a piece whose *length* is about $\Delta x$, which is accurate when the slope $u_x$ is small. And the acceleration $u_{tt}$ varies along the piece; (Powers takes it at the left end; here is why that is harmless:) the correct right side of (2) is $\int_x^{x + \Delta x}\rho\,u_{tt}(s, t)\,ds = \rho\,\Delta x\,u_{tt}(\xi, t)$ for some $\xi$ between $x$ and $x + \Delta x$ by the mean value theorem for integrals, and $u_{tt}(\xi, t) \to u_{tt}(x, t)$ as $\Delta x \to 0$ if $u_{tt}$ is continuous.

^pf-29-1

*Uses:* [[§29 The Vibrating String#^def-29-1|Def. §29.1]]

If $c^2$ is very large (usually on the order of $10^5\ \mathrm{m^2/s^2}$), the last term $g/c^2$ in (5) is negligible ([[§29 The Vibrating String#^ex-29-2|Example §29.2]] shows how small its effect is), and the equation becomes the wave equation.

> [!definition] Definition §29.2: The One-Dimensional Wave Equation
> The equation of the vibrating string with gravity neglected,
>
> $$
> \frac{\partial^2 u}{\partial x^2} = \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2} , \qquad 0 < x < a, \quad 0 < t , \qquad (6)
> $$
>
> or equivalently $u_{tt} = c^2u_{xx}$, is the **wave equation in one dimension**. The positive constant $c$, with $c^2 = T/\rho$, is the **wave speed**. Two- and three-dimensional versions appear in Chapter 5 ([[§41★ Two-Dimensional Wave Equation꞉ Derivation#^thm-41-1|Theorem §41.1]]).
>
> *Powers: 3.1, Equation (6)*

^def-29-2

> [!remark]- Connections
> - Stewart's version, with $a$ in place of $c$, and the check that $\sin(x - at)$ solves it: [[§92 Partial Derivatives#^def-92-5|Calc Def. §92.5]].
> - The derivation is Newton's law for a continuum of masses coupled by tension; for a single mass on a spring it gives the oscillator equation $mu'' + ku = 0$, [[§19 Mechanical and Electrical Vibrations#^prop-19-1|331 Prop. §19.1]]. Each mode of the string, [[§30 Solution of the Vibrating String Problem#^def-30-1|Definition §30.1]], is exactly such an oscillator.

## The Vibrating String Problem

To describe the motion of an object, one must specify both its equation of motion and its initial position and velocity. For the string, the initial conditions state the initial displacement $u(x, 0)$ and the initial velocity $\partial u/\partial t(x, 0)$ of every particle; the ends are held fixed.

> [!definition] Definition §29.3: The Vibrating String Problem
> The boundary value–initial value problem for the string with fixed ends, gravity neglected, is
>
> $$
> \begin{aligned}
> &\frac{\partial^2 u}{\partial x^2} = \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2}, && 0 < x < a, \quad 0 < t, && (7) \\
> &u(0, t) = 0, \quad u(a, t) = 0, && 0 < t, && (8) \\
> &u(x, 0) = f(x), && 0 < x < a, && (9) \\
> &\frac{\partial u}{\partial t}(x, 0) = g(x), && 0 < x < a . && (10)
> \end{aligned}
> $$
>
> Here (8) are the **boundary conditions** (zero displacement at the ends) and (9), (10) the **initial conditions**: $f$ is the initial displacement and $g$ the initial velocity.
>
> *Powers: 3.1, Equations (7)–(10)*

^def-29-3

> [!remark] Remark: Wave Equation versus Heat Equation
> The heat equation $u_{xx} = u_t/k$ ([[§17 Derivation and Boundary Conditions#^thm-17-2|Theorem §17.2]]) is first order in $t$ and needs one initial condition, the initial temperature. The wave equation is second order in $t$, like Newton's law, and needs two. The boundary conditions are of the same kinds in both problems, and the method of solution in [[§30 Solution of the Vibrating String Problem|§30]] is the one used for heat in [[§19 Example꞉ Fixed End Temperatures|§19]]; the difference shows in the time factors, which decay for heat and oscillate for waves. In the lecture the equation is written $u_{tt} = c^2u_{xx}$, and the derivation is done with the horizontal tension $H$ in place of $T$; it is the same computation.

^rem-29-1

> [!example] Example §29.1: Dimensions and the Wave Speed
> Find the dimensions of $u$, $\partial^2u/\partial x^2$, $\partial^2u/\partial t^2$, $c$ and $g/c^2$, using that force has dimension $mL/t^2$ (mass $m$, length $L$, time $t$) and tension is a force, and check that each term of (5) has the same dimension.
>
> - $u$ is a displacement: $L$. So $\partial^2u/\partial x^2$ has dimension $L/L^2 = 1/L$, and $\partial^2u/\partial t^2$ has dimension $L/t^2$, an acceleration.
> - $\rho$ is mass per length, $m/L$, so $c^2 = T/\rho$ has dimension $\dfrac{mL/t^2}{m/L} = \dfrac{L^2}{t^2}$. Thus $c$ is a **velocity**, $L/t$, which is why it is called the wave speed.
> - $g$ is an acceleration, $L/t^2$, so $g/c^2$ has dimension $\dfrac{L/t^2}{L^2/t^2} = 1/L$.
> - In (5): $u_{xx}$ has dimension $1/L$; $\frac{1}{c^2}u_{tt}$ has dimension $\dfrac{t^2}{L^2}\cdot\dfrac{L}{t^2} = 1/L$; and $g/c^2$ has dimension $1/L$. All terms agree.
>
> With $c^2 \approx 10^5\ \mathrm{m^2/s^2}$, $c \approx 316\ \mathrm{m/s}$, of the order of the speed of sound in air.
>
> *Powers: Exercise 3.1.1*

^ex-29-1

> [!example] Example §29.2: The Equilibrium Shape under Gravity
> Find the solution $v(x)$ of (5) with the boundary conditions (8) that is independent of time.
>
> If $v$ does not depend on $t$, then $v_{tt} = 0$ and (5) becomes
>
> $$
> v'' = \frac{g}{c^2}, \qquad 0 < x < a, \qquad v(0) = 0, \quad v(a) = 0 .
> $$
>
> Integrating twice, $v = \dfrac{g}{2c^2}x^2 + Bx + C$. Then $v(0) = 0$ gives $C = 0$, and $v(a) = \dfrac{g a^2}{2c^2} + Ba = 0$ gives $B = -\dfrac{ga}{2c^2}$. So
>
> $$
> v(x) = \frac{g}{2c^2}\big(x^2 - ax\big) = -\frac{g}{2c^2}\,x(a - x) ,
> $$
>
> a parabola sagging below the axis, deepest at the middle with $v(a/2) = -ga^2/(8c^2)$. For $a = 1\ \mathrm{m}$ and $c^2 = 10^5\ \mathrm{m^2/s^2}$ the sag is $9.8/(8 \cdot 10^5) \approx 1.2 \times 10^{-5}\ \mathrm{m}$, about a hundredth of a millimetre: this is why gravity is neglected in (6). Powers calls $v$ an **equilibrium solution**; "steady state" is not appropriate, because, as [[§32 One-Dimensional Wave Equation꞉ Generalities#^rem-32-1|§32]] shows, $u$ does not tend to $v$.
>
> HW 10 asks the same for $u_{tt} = u_{xx} - F$ (that is, $c = 1$ and a constant downward force, as with $F = g$): the equilibrium problem $0 = v'' - F$, $v(0) = v(a) = 0$ has the solution $v(x) = \frac{F}{2}(x^2 - ax)$. The full problem is solved in [[§32 One-Dimensional Wave Equation꞉ Generalities#^ex-32-2|Example §32.2]].
>
> *Powers: Exercise 3.1.3 · Source: 341 HW 10, Problem 3(a)*

^ex-29-2

> [!example] Example §29.3: Setting Up the Initial Conditions
> Write the initial conditions for **(a)** a string of length $a$ lifted at its midpoint to height $h$ and released from rest, and **(b)** a piano string at rest in its equilibrium position, struck by a hammer so that its initial velocity grows linearly from $0$ at the ends to $1$ at the midpoint.
>
> **(a)** The lifted string is two straight segments, from $(0, 0)$ to $(a/2, h)$ and from $(a/2, h)$ to $(a, 0)$. The first has slope $2h/a$, the second $-2h/a$, so
>
> $$
> u(x, 0) = f(x) = \begin{cases} h\cdot\dfrac{2x}{a}, & 0 < x < \dfrac a2, \\[2mm] h\Big(2 - \dfrac{2x}{a}\Big), & \dfrac a2 < x < a, \end{cases} \qquad \frac{\partial u}{\partial t}(x, 0) = g(x) \equiv 0 .
> $$
>
> "Released" means the initial velocity is zero. Note that $f$ is continuous, with $f(0) = f(a) = 0$, as the boundary conditions demand.
>
> **(b)** Now the displacement starts at zero and the velocity carries the information:
>
> $$
> u(x, 0) = 0, \qquad \frac{\partial u}{\partial t}(x, 0) = g(x) = \begin{cases} \dfrac{2x}{a}, & 0 < x < \dfrac a2, \\[2mm] 2 - \dfrac{2x}{a}, & \dfrac a2 < x < a . \end{cases}
> $$
>
> Both problems are solved in [[§30 Solution of the Vibrating String Problem#^ex-30-1|Example §30.1]] and [[§30 Solution of the Vibrating String Problem#^ex-30-3|Example §30.3]].
>
> *Powers: 3.2, Example (the initial condition) · Source: 341 lecture 10.29; 341 HW 10, Problem 1*

^ex-29-3

## Other Forces

The derivation of Theorem §29.1 adapts at once when other vertical forces act on the string. Both of the following equations are used later.

> [!theorem] Proposition §29.2: The Forced String
> If a distributed vertical force $F(x, t)$ (force per unit length, positive upward) acts on the string, the equation of motion is
>
> $$
> \frac{\partial^2 u}{\partial x^2} = \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2} - \frac{1}{T}F(x, t) .
> $$
>
> The weight of the string is the case $F(x, t) = -\rho g$, which gives (5) back.
>
> *Powers: Exercise 3.1.2*

^prop-29-2

> [!proof]+ Proof
> In the vertical balance (2), the force on the piece between $x$ and $x + \Delta x$ is $\int_x^{x + \Delta x}F(s, t)\,ds = F(\eta, t)\,\Delta x$ for some $\eta$ in the interval (mean value theorem for integrals, $F$ continuous), in place of $-mg$. Following the proof of Theorem §29.1,
>
> $$
> T\Big(\frac{\partial u}{\partial x}(x + \Delta x, t) - \frac{\partial u}{\partial x}(x, t)\Big) + F(\eta, t)\,\Delta x = \rho\,\Delta x\,\frac{\partial^2 u}{\partial t^2} .
> $$
>
> Dividing by $\Delta x$ and letting $\Delta x \to 0$ gives $Tu_{xx} + F = \rho u_{tt}$; dividing by $T$ and using $\rho/T = 1/c^2$ gives the stated equation. With $F = -\rho g$, $-F/T = \rho g/T = g/c^2$, which is (5). (Dimensions: $F$ is force per length, so $F/T$ has dimension $1/L$, like $u_{xx}$.)

^pf-29-2

*Uses:* [[§29 The Vibrating String#^thm-29-1|§29.1]]

> [!theorem] Proposition §29.3: The String in a Resisting Medium
> If the string moves in a medium (such as air) that resists the motion with a force opposite to the velocity and proportional to it, $-r\,u_t$ per unit length ($r > 0$), and gravity is neglected, the equation of motion is
>
> $$
> \frac{\partial^2 u}{\partial t^2} + k\frac{\partial u}{\partial t} = c^2\frac{\partial^2 u}{\partial x^2}, \qquad k = \frac{r}{\rho} > 0 ,
> $$
>
> equivalently $u_{xx} = \frac{1}{c^2}u_{tt} + \frac{r}{T}u_t$, the form of Powers' Exercise 3.2.9.
>
> *Powers: Exercise 3.1.4*

^prop-29-3

> [!proof]+ Proof
> The resistance affects only the vertical balance (2). It is the case $F(x, t) = -r\,u_t(x, t)$ of Proposition §29.2: $u_{xx} = \frac{1}{c^2}u_{tt} + \frac{r}{T}u_t$. Multiplying by $c^2 = T/\rho$ gives $c^2u_{xx} = u_{tt} + \frac{r}{\rho}u_t$.

^pf-29-3

*Uses:* [[§29 The Vibrating String#^prop-29-2|§29.2]]

The damped string is solved by separation of variables in [[§32 One-Dimensional Wave Equation꞉ Generalities#^ex-32-3|Example §32.3]]: its modes decay like damped oscillators instead of vibrating forever.
