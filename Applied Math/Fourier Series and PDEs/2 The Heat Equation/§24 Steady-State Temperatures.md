---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 2
section: 24
powers: "2.2"
aliases: ["Powers 2.2"]
tags: [fourier-series-and-pdes, math341]
---
← [[§23 Initial and Boundary Conditions; Diffusion]] · ↑ [[· 2 The Heat Equation]] · [[§25 Example꞉ Fixed End Temperatures]] →

*Powers, Section 2.2 · MAT 341 lecture 9.19 · HW 4, HW 5 · Practice Midterm 1.*

Before solving a complete heat conduction problem, this section solves a simpler one: the steady state, or equilibrium, temperature $v(x)$ that the rod settles into after a long time. Setting $\partial u/\partial t = 0$ turns the partial differential equation into an ordinary one, and the steady-state problem is a two-point boundary value problem for $v$. Usually it has exactly one solution (a straight line, for fixed or convective ends), but with both ends insulated it has infinitely many. The steady state is also the first step toward the complete solution: the remainder $w = u - v$, the transient, satisfies a problem with homogeneous equation and boundary conditions, which is what separation of variables in [[§25 Example꞉ Fixed End Temperatures|§25]] needs.

## The Steady-State Problem

Begin with the problem

$$
\begin{aligned}
\frac{\partial^2u}{\partial x^2} &= \frac1k\frac{\partial u}{\partial t}, && 0 < x < a, \quad 0 < t, && (1) \\
u(0, t) &= T_0, && 0 < t, && (2) \\
u(a, t) &= T_1, && 0 < t, && (3) \\
u(x, 0) &= f(x), && 0 < x < a, && (4)
\end{aligned}
$$

the temperature in a cylindrical rod with insulated lateral surface whose ends are held at the constant temperatures $T_0$ and $T_1$. Experience indicates that after a long time under the same conditions the variation of temperature with time dies away.

> [!definition] Definition §24.1: Steady-State Temperature Distribution
> For a heat conduction problem whose boundary conditions and generation terms do not depend on $t$, the **steady-state temperature distribution** (or **equilibrium** distribution) is the function
>
> $$
> v(x) = \lim_{t \to \infty} u(x, t) ,
> $$
>
> where it is expected that the limit exists, depends only on $x$, and that also
>
> $$
> \lim_{t \to \infty}\frac{\partial u}{\partial t} = 0 .
> $$
>
> $v(x)$ must still satisfy the partial differential equation and the boundary conditions, which are valid for all $t > 0$.
>
> *Powers: 2.2 (text)*

^def-24-1

> [!example] Example §24.1: Fixed End Temperatures
> For the problem (1)–(4), $v(x)$ should be the solution of
>
> $$
> \frac{d^2v}{dx^2} = 0, \quad 0 < x < a , \qquad (5)
> $$
>
> $$
> v(0) = T_0, \qquad v(a) = T_1 . \qquad (6)
> $$
>
> Integrating the differential equation twice gives $dv/dx = A$ and $v(x) = Ax + B$. The constants must satisfy the boundary conditions:
>
> $$
> v(0) = B = T_0, \qquad v(a) = Aa + B = T_1 .
> $$
>
> So $B = T_0$, $A = (T_1 - T_0)/a$, and the steady-state distribution is
>
> $$
> v(x) = T_0 + (T_1 - T_0)\frac xa . \qquad (7)
> $$
>
> Equations (5)–(6) could have been set up from scratch as a boundary value problem, as in [[§5★ Boundary Value Problems#^prop-5-2|Proposition §5.2]]; here they appear as part of a more comprehensive problem. The same steady state appears with $u_t = 2u_{xx}$ on $0 < x < 1$, $u(0, t) = 0$, $u(1, t) = 3$: $0 = 2v''$, $v(0) = 0$, $v(1) = 3$, so $v(x) = 3x$ (the diffusivity drops out).
>
> *Powers: 2.2, Example; Source: 341 Practice Midterm 1, Q7(a)*

^ex-24-1

> [!remark] Remark: Method — Setting Up the Steady-State Problem
> To set up the steady-state problem corresponding to a given heat conduction problem:
> 1. Take the equations that are valid for large $t$: the partial differential equation and the boundary conditions. Drop the initial condition.
> 2. Replace $u$ and its $x$-derivatives by $v$ and its derivatives, and replace $\partial u/\partial t$ by $0$.
> 3. Solve the resulting ordinary differential equation for $v(x)$ and impose the boundary conditions: a two-point boundary value problem.
>
> This requires boundary conditions and generation terms independent of $t$ (constants $T$, $C$, $T_0$ in the Dirichlet, Neumann, Robin conditions); otherwise there is no steady state.

^rem-24-1

> [!example] Example §24.2: Convection at One End
> Find the steady-state problem and its solution for (13)–(16) of [[§23 Initial and Boundary Conditions; Diffusion#^def-23-6|Definition §23.6]]:
>
> $$
> \begin{aligned}
> \frac{\partial^2u}{\partial x^2} &= \frac1k\frac{\partial u}{\partial t}, && 0 < x < a, \quad 0 < t, && (8) \\
> u(0, t) &= T_0, && 0 < t, && (9) \\
> -\kappa\frac{\partial u}{\partial x}(a, t) &= h\big(u(a, t) - T_1\big), && 0 < t, && (10) \\
> u(x, 0) &= f(x), && 0 < x < a . && (11)
> \end{aligned}
> $$
>
> The rule of [[§24 Steady-State Temperatures#^rem-24-1|the method remark]] gives
>
> $$
> \frac{d^2v}{dx^2} = 0, \quad 0 < x < a; \qquad v(0) = T_0, \qquad -\kappa v'(a) = h\big(v(a) - T_1\big) .
> $$
>
> The solution of the differential equation is $v(x) = A + Bx$. The boundary conditions require
>
> $$
> v(0) = T_0\colon\ A = T_0, \qquad -\kappa v'(a) = h\big(v(a) - T_1\big)\colon\ -\kappa B = h(A + Ba - T_1) .
> $$
>
> Substituting $A = T_0$ in the second, $-\kappa B - haB = h(T_0 - T_1)$, so $B = h(T_1 - T_0)/(\kappa + ha)$. Thus the steady-state solution of (8)–(11) is
>
> $$
> v(x) = T_0 + \frac{xh(T_1 - T_0)}{\kappa + ha} . \qquad (12)
> $$
>
> At $x = a$, $v(a) = T_0 + (T_1 - T_0)\frac{ha}{\kappa + ha}$ lies between $T_0$ and $T_1$: the end does not reach the fluid temperature. As $h \to \infty$ (perfect contact) $v(a) \to T_1$ and (12) becomes (7); as $h \to 0$ (insulated end) $v \to T_0$.
>
> *Lecture 9.19 (Example 2) writes the slope as $hT_1/(\kappa + ha)$; substituting in $-\kappa v'(a) = h(v(a) - T_1)$ shows that $h(T_1 - T_0)/(\kappa + ha)$ is correct, and the two agree only when $T_0 = 0$.*
>
> *Powers: 2.2, Example; Source: 341 lecture 9.19*

^ex-24-2

![[m341-18-1.svg]]
*(a) The steady states (12) of Example §24.2 with $T_0 = 20$, $T_1 = 100$, for $\kappa/ha = 0$ (perfect contact, the line (7)), $0.1$, $1$ and $10$: the larger the ratio of conduction to convection, the less the right end feels the fluid. (b) Steady states of Example §24.5, $v'' = \gamma^2 v$ with ends at $20$ and $100$ and the surrounding fluid at $U = 0$, for $\gamma a = 0$, $2$, $5$, $15$: lateral cooling bends the line down, and for large $\gamma a$ the interior is near the fluid temperature.*

In both examples the steady-state distribution has been uniquely determined by the differential equation and boundary conditions. This is usually the case, but not always.

> [!example] Example §24.3: Insulated Ends — No Unique Steady State
> For the problem
>
> $$
> \begin{aligned}
> \frac{\partial^2u}{\partial x^2} &= \frac1k\frac{\partial u}{\partial t}, && 0 < x < a, \quad 0 < t, && (13) \\
> \frac{\partial u}{\partial x}(0, t) &= 0, && 0 < t, && (14) \\
> \frac{\partial u}{\partial x}(a, t) &= 0, && 0 < t, && (15) \\
> u(x, 0) &= f(x), && 0 < x < a, && (16)
> \end{aligned}
> $$
>
> which describes the temperature in an insulated rod that also has insulated ends, the steady-state problem for $v(x) = \lim_{t\to\infty} u(x, t)$ is
>
> $$
> \frac{d^2v}{dx^2} = 0, \quad 0 < x < a; \qquad \frac{dv}{dx}(0) = 0, \qquad \frac{dv}{dx}(a) = 0 .
> $$
>
> With $v = Ax + B$, both conditions say $A = 0$, and $B$ is free: $v(x) = T$ is a solution for any constant $T$. There is no information in the steady-state problem to tell what value $T$ should take, so this boundary value problem has infinitely many solutions. ([[§26 Example꞉ Insulated Bar#^thm-26-2|Theorem §26.2]] finds $T$ from the initial condition: it is the average of $f$.)
>
> *Powers: 2.2, Example*

^ex-24-3

It should not be supposed that every steady-state distribution has a straight-line graph; see [[§24 Steady-State Temperatures#^ex-24-4|Example §24.4]] and [[§24 Steady-State Temperatures#^ex-24-5|Example §24.5]].

## The Transient Problem

The steady state gives valuable information about the solution, and it is also the first step in finding the complete solution. The "rest" of the unknown temperature is isolated as follows.

> [!definition] Definition §24.2: Transient Temperature Distribution
> The **transient temperature distribution** is
>
> $$
> w(x, t) = u(x, t) - v(x) .
> $$
>
> The name is appropriate because, by the assumptions on the behavior of $u$ for large $t$, $w(x, t)$ is expected to tend to zero as $t \to \infty$.
>
> *Powers: 2.2 (text)*

^def-24-2

> [!theorem] Proposition §24.1: The Transient Problem Is Homogeneous
> Let $u$ solve (1)–(4) and let $v$ be the steady state (7). Then $w = u - v$ satisfies
>
> $$
> \begin{aligned}
> \frac{\partial^2w}{\partial x^2} &= \frac1k\frac{\partial w}{\partial t}, && 0 < x < a, \quad 0 < t, && (17) \\
> w(0, t) &= 0, && 0 < t, && (18) \\
> w(a, t) &= 0, && 0 < t, && (19) \\
> w(x, 0) &= f(x) - \Big[T_0 + (T_1 - T_0)\frac xa\Big] \equiv g(x), && 0 < x < a . && (20)\text{–}(21)
> \end{aligned}
> $$
>
> The partial differential equation (17) and the boundary conditions (18), (19) are **homogeneous**: the function $w \equiv 0$ satisfies them (but not, in general, the initial condition).
>
> *Powers: 2.2, Equations (17)–(21)*

^prop-24-1

> [!proof]+ Proof
> Write $u(x, t) = w(x, t) + v(x)$ and use what is known about $v$, namely (5) and (6).
> - By the rules of calculus, $\dfrac{\partial^2u}{\partial x^2} = \dfrac{\partial^2w}{\partial x^2} + \dfrac{d^2v}{dx^2} = \dfrac{\partial^2w}{\partial x^2}$, because of (5).
> - $\dfrac{\partial u}{\partial t} = \dfrac{\partial w}{\partial t} + \dfrac{\partial v}{\partial t} = \dfrac{\partial w}{\partial t}$, since $v(x)$ does not depend on $t$.
> - Substituting both into (1) gives (17).
> - $u(0, t) = w(0, t) + v(0)$, by definition of the transient; with (2) and (6), $T_0 = w(0, t) + T_0$, so $w(0, t) = 0$.
> - $u(a, t) = w(a, t) + v(a)$; with (3) and (6), $T_1 = w(a, t) + T_1$, so $w(a, t) = 0$.
> - $u(x, 0) = w(x, 0) + v(x)$; with (4) and (7), $f(x) = w(x, 0) + T_0 + (T_1 - T_0)x/a$, which is (20). In (21) the combination of $f(x)$ and $v(x)$ is just renamed $g(x)$.

^pf-24-1

*Uses:* [[§24 Steady-State Temperatures#^def-24-2|Def. §24.2]], [[§24 Steady-State Temperatures#^ex-24-1|Ex. §24.1]]

> [!remark] Remark: Why the Transient Problem Matters
> The mathematical purpose of setting up the steady-state problem and then the transient problem is that the transient problem is homogeneous. Test: try $w \equiv 0$; it satisfies (17), (18) and (19). It is crucially important for the method of [[§25 Example꞉ Fixed End Temperatures|§25]] (separation of variables) to have a homogeneous partial differential equation and homogeneous boundary conditions: then sums and multiples of solutions are again solutions. The nonhomogeneous data ($T_0$, $T_1$, a source term) are absorbed by $v$; only the initial condition remains nonhomogeneous, with the new initial function $g = f - v$.

^rem-24-2

> [!remark] Remark: Boundary Conditions of the Transient
> The same computation works for each kind of boundary condition with constant data, because $v$ satisfies the same condition as $u$ and the conditions are linear. At an end where
> 1. **Dirichlet:** $u(0, t) = T$ and $v(0) = T$, the transient has $w(0, t) = 0$;
> 2. **Neumann:** $u_x(0, t) = C$ and $v'(0) = C$, the transient has $w_x(0, t) = 0$;
> 3. **Robin:** $-\kappa u_x(a, t) = h(u(a, t) - T_1)$ and $-\kappa v'(a) = h(v(a) - T_1)$; subtracting, $-\kappa w_x(a, t) = hw(a, t)$, that is $hw(a, t) + \kappa w_x(a, t) = 0$.
>
> In each case the constant on the right is replaced by $0$. The equation also loses its source: if $u_{xx} + K = u_t$ and $v'' + K = 0$, then $w_{xx} = w_t$.
>
> *Source: 341 lecture 9.19*

^rem-24-3

> [!example] Example §24.4: A Uniform Heat Source
> Consider
>
> $$
> \frac{\partial^2u}{\partial x^2} + K = \frac{\partial u}{\partial t}, \quad 0 < x < a,\ t > 0; \qquad u(x, 0) = f(x); \qquad u(0, t) = T; \qquad \frac{\partial u}{\partial x}(a, t) = 0,
> $$
>
> with constants $K$ and $T$ (the rod of [[§23 Initial and Boundary Conditions; Diffusion#^ex-23-1|Example §23.1]]). **(b)** Find the steady state. **(c)** State the problem for $w = u - v$.
>
> **(b)** The steady-state problem is
>
> $$
> \frac{d^2v}{dx^2} + K = 0, \quad 0 < x < a; \qquad v(0) = T, \qquad \frac{dv}{dx}(a) = 0 .
> $$
>
> Integrating, $v'(x) = -Kx + C_1$ and $v(x) = -\frac12Kx^2 + C_1x + C_2$. Then $v(0) = C_2 = T$ and $v'(a) = -Ka + C_1 = 0$, so $C_1 = Ka$:
>
> $$
> v(x) = -\tfrac12Kx^2 + Kax + T .
> $$
>
> This is a parabola, not a line: the heat generated inside must flow out through the end $x = 0$, the only end where it can leave, so (for $K > 0$) the rod is hottest at the insulated end, $v(a) = T + \frac12Ka^2$.
>
> **(c)** With $u = w + v$: $u_t = w_t$ and $u_{xx} = w_{xx} + v'' = w_{xx} - K$, so the equation becomes $w_{xx} - K + K = w_t$. Also $u(0, t) = w(0, t) + T$ and $u_x(a, t) = w_x(a, t) + v'(a) = w_x(a, t)$. Hence
>
> $$
> \frac{\partial^2w}{\partial x^2} = \frac{\partial w}{\partial t}, \quad 0 < x < a,\ t > 0; \qquad w(x, 0) = f(x) + \tfrac12Kx^2 - Kax - T; \qquad w(0, t) = 0; \qquad \frac{\partial w}{\partial x}(a, t) = 0 .
> $$
>
> The source $K$ has disappeared from the transient problem. [[§27 Example꞉ Different Boundary Conditions#^ex-27-3|Example §27.3]] solves it for $f(x) = -\frac12Kx^2$.
>
> *Source: 341 HW 4, Problem 1(b)–(c)*

^ex-24-4

> [!example] Example §24.5: Lateral Convection — A Steady State That Is Not a Line
> Consider the rod of [[§23 Initial and Boundary Conditions; Diffusion#^ex-23-3|Example §23.3]], which loses heat through its lateral surface to a fluid at temperature $T$:
>
> $$
> \frac{\partial u}{\partial t} = \frac{\partial^2u}{\partial x^2} - \gamma^2(u - T), \quad 0 < x < a,\ t > 0; \qquad u(0, t) = T, \quad u(a, t) = T; \qquad u(x, 0) = f(x) .
> $$
>
> **(a) Steady state.** $0 = v'' - \gamma^2(v - T)$, $v(0) = v(a) = T$. Put $\tilde v = v - T$; then $\tilde v'' - \gamma^2\tilde v = 0$, $\tilde v(0) = \tilde v(a) = 0$. The characteristic roots are $\pm\gamma$ ([[§17 Homogeneous Differential Equations with Constant Coefficients#^thm-17-2|331 Thm. §17.2]]), so $\tilde v = C_1e^{\gamma x} + C_2e^{-\gamma x}$. Then $\tilde v(0) = C_1 + C_2 = 0$ and $\tilde v(a) = C_1(e^{\gamma a} - e^{-\gamma a}) = 0$; since $\gamma a \ne 0$, $C_1 = C_2 = 0$. So $v(x) = T$: rod, ends and fluid at one temperature.
>
> **(b) Transient.** $w = u - T$ satisfies $w_t = w_{xx} - \gamma^2w$, $w(0, t) = w(a, t) = 0$, $w(x, 0) = f(x) - T$; it is solved in [[§25 Example꞉ Fixed End Temperatures#^ex-25-4|Example §25.4]].
>
> **Different end temperatures.** If instead $u(0, t) = T_0$, $u(a, t) = T_1$ and the fluid is at $U$, the same substitution $\tilde v = v - U$ with $\tilde v(0) = T_0 - U$, $\tilde v(a) = T_1 - U$ gives, in the hyperbolic basis $\sinh\gamma x$, $\sinh\gamma(a - x)$,
>
> $$
> v(x) = U + \frac{(T_0 - U)\sinh\gamma(a - x) + (T_1 - U)\sinh\gamma x}{\sinh\gamma a} .
> $$
>
> (Check: at $x = 0$ the second term vanishes and the first gives $T_0 - U$; at $x = a$ the first vanishes; and each of $\sinh\gamma x$, $\sinh\gamma(a - x)$ satisfies $\tilde v'' = \gamma^2\tilde v$.) This $v$ is not a straight line: it sags toward $U$ in the middle (figure above, panel (b)). As $\gamma \to 0$ it tends to the line (7).
>
> *Source: 341 HW 5, Problem 1(a)–(b); Powers: Exercise 2.2.1*

^ex-24-5
