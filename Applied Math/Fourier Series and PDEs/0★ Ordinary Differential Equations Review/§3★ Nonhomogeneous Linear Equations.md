---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 0
section: "3★"
powers: "0.2"
aliases: ["Powers 0.2"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§2★ Variable Coefficients and Higher-Order Equations]] · ↑ [[· 0★ Ordinary Differential Equations Review]] · [[§4★ Variation of Parameters]] →

*Powers, Section 0.2.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

A nonhomogeneous linear equation $u'' + k(t)u' + p(t)u = f(t)$ is solved in two parts: the general solution of the homogeneous equation ([[§1★ Homogeneous Linear Equations|§1★]]) plus one particular solution. This section reviews the two ways of finding a particular solution: undetermined coefficients, a guess that works for constant coefficients and simple inhomogeneities, and variation of parameters, which always works once the homogeneous equation is solved. The second leads to a formula $u_p(t) = \int_{t_0}^t G(t, z)f(z)\,dz$ that expresses the response to a forcing $f$ as a superposition of responses to its values, the first appearance of a Green's function; [[§7★ Green's Functions|§7★]] builds the same kind of formula for boundary value problems. Physically, the forced mass–spring–damper shows resonance. All of this is proved in [[Ordinary Differential Equations]], and each item links to its home there.

## Particular and Complementary Solutions

> [!definition] Definition §3.1: Inhomogeneity
> In the nonhomogeneous linear equations
>
> $$
> \frac{du}{dt} = k(t)u + f(t), \qquad \frac{d^2u}{dt^2} + k(t)\frac{du}{dt} + p(t)u = f(t) ,
> $$
>
> the function $f(t)$, not identically $0$, is the **inhomogeneity**.
>
> *Powers: 0.2 (text)*

^def-3-1

> [!definition] Definition §3.2: Particular Solution
> A **particular solution** $u_p(t)$ is any one solution of the nonhomogeneous equation ([[§3★ Nonhomogeneous Linear Equations#^def-3-1|Definition §3.1]]).
>
> *Powers: 0.2 (text)*

^def-3-2

> [!definition] Definition §3.3: Complementary Solution
> For the same nonhomogeneous equation, the **complementary solution** $u_c(t)$ is the general solution of the corresponding homogeneous equation (the same equation with $f = 0$).
>
> *Powers: 0.2 (text)*

^def-3-3

This is [[§21 Nonhomogeneous Equations; Method of Undetermined Coefficients#^def-21-1|331 Def. §21.1]].

> [!theorem] Theorem §3.1: The Simplest Nonhomogeneous Equations
> The equation
>
> $$
> \frac{du}{dt} = f(t) \qquad (1)
> $$
>
> with $f$ continuous has the general solution
>
> $$
> u(t) = \int f(t)\,dt + c , \qquad\text{more precisely}\qquad u(t) = \int_{t_0}^{t} f(z)\,dz + c , \qquad (2), (3)
> $$
>
> where the lower limit $t_0$ is usually an initial time and the integration variable is renamed ($z$) so as not to confuse it with the limit $t$. The equation
>
> $$
> \frac{d^2u}{dt^2} = f(t) \qquad (4)
> $$
>
> is solved by two successive integrations: $u(t) = \int_{t_0}^{t}\int_{t_0}^{s} f(z)\,dz\,ds + c_1t + c_2$.
>
> *Powers: 0.2, Equations (1)–(4)*

^thm-3-1

> [!proof]+ Proof
> By the Fundamental Theorem of Calculus, $F(t) = \int_{t_0}^t f(z)\,dz$ satisfies $F' = f$. If $u' = f$, then $(u - F)' = 0$, so $u - F$ is a constant $c$; conversely every $F + c$ solves (1). For (4), $u'' = f$ means that $u'$ solves (1), so $u'(s) = \int_{t_0}^s f(z)\,dz + c_1$, and integrating once more gives the stated formula (with a new constant $c_2$).

^pf-3-1

*Uses:* [[§41 The Fundamental Theorem of Calculus#^thm-41-1|Calc Thm. §41.1]] (FTC), [[§29 Rolle's Theorem and the Mean Value Theorem#^cor-29-4|Calc Cor. §29.4]] (zero derivative means constant)

> [!theorem] Theorem §3.2: Structure of the General Solution
> The general solution of a nonhomogeneous linear equation has the form
>
> $$
> u(t) = u_p(t) + u_c(t) ,
> $$
>
> where $u_p(t)$ is any particular solution of the nonhomogeneous equation and $u_c(t)$ is the general solution of the corresponding homogeneous equation.
>
> *Powers: 0.2, Theorem 1*

^thm-3-2

*Proved in ODE: [[§21 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-21-2|331 Thm. §21.2]] (via [[§21 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-21-1|331 Thm. §21.1]]: the difference of two solutions solves the homogeneous equation).*

> [!theorem] Theorem §3.3: Superposition of Inhomogeneities
> If $u_{p1}(t)$ and $u_{p2}(t)$ are particular solutions of a linear differential equation with inhomogeneities $f_1(t)$ and $f_2(t)$, respectively, then $k_1u_{p1}(t) + k_2u_{p2}(t)$ is a particular solution of the same differential equation with inhomogeneity $k_1f_1(t) + k_2f_2(t)$ ($k_1$, $k_2$ constants).
>
> *Powers: 0.2, Theorem 2*

^thm-3-3

> [!proof]+ Proof
> Write the equation as $L[u] = f$, with $L[u] = u'' + k(t)u' + p(t)u$ (or $L[u] = u' - k(t)u$). The computation in the proof of superposition, [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-2|331 Thm. §18.2]], shows $L[k_1u_1 + k_2u_2] = k_1L[u_1] + k_2L[u_2]$ for any twice differentiable $u_1$, $u_2$. Hence $L[k_1u_{p1} + k_2u_{p2}] = k_1f_1 + k_2f_2$.

^pf-3-3

*Uses:* [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-2|331 Thm. §18.2]]

The sum case for constant coefficients is [[§21 Nonhomogeneous Equations; Method of Undetermined Coefficients#^prop-21-3|331 Prop. §21.3]].

> [!example] Example §3.1: Assembling a General Solution
> Find the general solution of
>
> $$
> \frac{d^2u}{dt^2} + u = 1 - e^{-t} .
> $$
>
> **Complementary solution.** The homogeneous equation $u'' + u = 0$ has $u_c(t) = c_1\cos(t) + c_2\sin(t)$ ([[§1★ Homogeneous Linear Equations#^ex-1-1|Example §1.1]] with $\lambda = 1$).
>
> **Particular solutions for the pieces.** For the inhomogeneity $f_1 = 1$, $u_{p1}(t) = 1$ solves $u'' + u = 1$. For $f_2 = e^{-t}$, $u_{p2}(t) = \frac12e^{-t}$ solves $u'' + u = e^{-t}$, since $\frac12e^{-t} + \frac12e^{-t} = e^{-t}$.
>
> **Combine.** By Theorem §3.3 with $k_1 = 1$, $k_2 = -1$, a particular solution of the given equation is $u_p(t) = 1 - \frac12e^{-t}$, and by Theorem §3.2 the general solution is
>
> $$
> u(t) = 1 - \tfrac12e^{-t} + c_1\cos(t) + c_2\sin(t) .
> $$
>
> If two initial conditions are given, $c_1$ and $c_2$ are available to satisfy them. An initial condition applies to the entire solution, not just to $u_c(t)$.
>
> *Powers: 0.2, Example (Theorems 1 and 2)*

^ex-3-1

## Undetermined Coefficients

This method guesses the form of a trial solution and then finds its coefficients. It is limited to equations with constant coefficients and inhomogeneities of simple form.

> [!theorem] Theorem §3.4: Undetermined Coefficients
> For a linear equation with constant coefficients and an inhomogeneity $f(t)$ of the form in the left column, a particular solution can be found of the form in the right column:
>
> | Inhomogeneity $f(t)$ | Trial solution $u_p(t)$ |
> |---|---|
> | $(a_0t^n + a_1t^{n-1} + \cdots + a_n)e^{\alpha t}$ | $(A_0t^n + A_1t^{n-1} + \cdots + A_n)e^{\alpha t}$ |
> | $(a_0t^n + \cdots + a_n)e^{\alpha t}\cos(\beta t) + (b_0t^n + \cdots + b_n)e^{\alpha t}\sin(\beta t)$ | $(A_0t^n + \cdots + A_n)e^{\alpha t}\cos(\beta t) + (B_0t^n + \cdots + B_n)e^{\alpha t}\sin(\beta t)$ |
>
> The parameters $n$, $\alpha$, $\beta$ are read off from $f$. Line 1 includes polynomials ($\alpha = 0$) and exponentials ($n = 0$, $\alpha \ne 0$). In line 2 both sine and cosine must be included in the trial solution even if one is absent from $f(t)$; $\alpha = 0$ and $n = 0$ are allowed.
>
> **Revision Rule.** If a term of the trial solution solves the corresponding homogeneous equation, multiply the trial solution by the lowest positive integral power of $t$ such that no term in it satisfies the homogeneous equation.
>
> *Powers: 0.2, Table 4 and Revision Rule*

^thm-3-4

*Powers omits the proof. The same table, with the power $t^s$ of the Revision Rule built in, is [[§21 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-21-4|331 Thm. §21.4]], where it is explained.*

> [!example] Example §3.2: Trial Solutions and the Revision Rule
> **(a)** Find a particular solution of $u'' + 5u = te^{-t}$.
>
> Line 1 of Table 4 with $n = 1$, $\alpha = -1$ suggests $u_p(t) = (A_0t + A_1)e^{-t}$; no term solves $u'' + 5u = 0$ (whose solutions are $\cos\sqrt5t$, $\sin\sqrt5t$). Then $u_p' = (A_0 - A_0t - A_1)e^{-t}$, $u_p'' = (A_0t + A_1 - 2A_0)e^{-t}$, and substituting,
>
> $$
> (A_0t + A_1 - 2A_0)e^{-t} + 5(A_0t + A_1)e^{-t} = te^{-t} .
> $$
>
> Equating coefficients: $6A_0 = 1$ (of $te^{-t}$) and $6A_1 - 2A_0 = 0$ (of $e^{-t}$), so $A_0 = 1/6$, $A_1 = 1/18$, and
>
> $$
> u_p(t) = \Big(\frac16t + \frac1{18}\Big)e^{-t} .
> $$
>
> **(b)** For $u'' - u = te^{-t}$ the table suggests $(A_0t + A_1)e^{-t}$ again, but $u_c = c_1e^t + c_2e^{-t}$, so the term $A_1e^{-t}$ solves the homogeneous equation. Multiplying by $t$ removes the conflict: the revised trial solution is
>
> $$
> u_p(t) = t(A_0t + A_1)e^{-t} = (A_0t^2 + A_1t)e^{-t} .
> $$
>
> (Carrying it through: $u_p'' - u_p = (-4A_0t + 2A_0 - 2A_1)e^{-t} = te^{-t}$ gives $A_0 = A_1 = -\frac14$, so $u_p = -\frac14(t^2 + t)e^{-t}$.)
>
> **(c)** For $u'' + 2u' + u = te^{-t}$, the homogeneous solutions are $c_1e^{-t} + c_2te^{-t}$ (double root $-1$). Multiplying the trial solution by $t$ still leaves the term $A_1te^{-t}$; the lowest power that works is $t^2$:
>
> $$
> u_p(t) = t^2(A_0t + A_1)e^{-t} .
> $$
>
> (Carrying it through gives $A_0 = \frac16$, $A_1 = 0$: $u_p = \frac16t^3e^{-t}$.)
>
> *Powers: 0.2, Examples (undetermined coefficients)*

^ex-3-2

> [!example] Example §3.3: Forced Vibrations and Resonance
> A mass–spring–damper system ([[§1★ Homogeneous Linear Equations#^ex-1-2|Example §1.2]]) starting from rest with an external sinusoidal force is described by
>
> $$
> \frac{d^2u}{dt^2} + b\frac{du}{dt} + \omega^2u = f_0\cos(\mu t), \qquad u(0) = 0, \quad \frac{du}{dt}(0) = 0 ,
> $$
>
> with $f_0$ proportional to the magnitude of the force.
>
> **$b = 0$, $\mu \ne \omega$: undamped, no resonance.** The trial solution $u_p = A\cos(\mu t) + B\sin(\mu t)$ gives $(\omega^2 - \mu^2)(A\cos\mu t + B\sin\mu t) = f_0\cos\mu t$, so $B = 0$ and
>
> $$
> u_p(t) = \frac{f_0}{\omega^2 - \mu^2}\cos(\mu t), \qquad u(t) = \frac{f_0}{\omega^2 - \mu^2}\cos(\mu t) + c_1\cos(\omega t) + c_2\sin(\omega t) .
> $$
>
> The initial conditions give $c_1 = -f_0/(\omega^2 - \mu^2)$, $c_2 = 0$:
>
> $$
> u(t) = \frac{f_0}{\omega^2 - \mu^2}\big(\cos(\mu t) - \cos(\omega t)\big) .
> $$
>
> **$b = 0$, $\mu = \omega$: resonance.** Now $\cos\mu t$ and $\sin\mu t$ solve the homogeneous equation, and the Revision Rule gives $u_p = At\cos(\mu t) + Bt\sin(\mu t)$. Substituting, $u_p'' + \mu^2u_p = -2A\mu\sin(\mu t) + 2B\mu\cos(\mu t) = f_0\cos(\mu t)$, so $A = 0$, $B = f_0/2\mu$. The general solution is $u = \frac{f_0}{2\mu}t\sin(\mu t) + c_1\cos(\mu t) + c_2\sin(\mu t)$, and the initial conditions give $c_1 = c_2 = 0$:
>
> $$
> u(t) = \frac{f_0}{2\mu}\,t\sin(\mu t) .
> $$
>
> The factor $t$ makes the amplitude of the oscillation grow without bound. This is the phenomenon of **resonance**.
>
> **$b > 0$: damped motion.** The trial solution is again a combination of $\cos(\mu t)$ and $\sin(\mu t)$, and solving for its coefficients gives
>
> $$
> u_p(t) = \frac{f_0}{\Delta}\Big((\omega^2 - \mu^2)\cos(\mu t) + \mu b\sin(\mu t)\Big), \qquad \Delta = (\omega^2 - \mu^2)^2 + \mu^2b^2 .
> $$
>
> In the underdamped case, with $\gamma = \sqrt{\omega^2 - (b/2)^2}$ real,
>
> $$
> u(t) = \frac{f_0}{\Delta}\Big((\omega^2 - \mu^2)\cos(\mu t) + \mu b\sin(\mu t)\Big) + e^{-bt/2}\big(c_1\cos(\gamma t) + c_2\sin(\gamma t)\big) .
> $$
>
> The initial conditions: $u(0) = 0$ gives $c_1 = -\frac{f_0}{\Delta}(\omega^2 - \mu^2)$; $u'(0) = \frac{f_0}{\Delta}\mu^2b - \frac b2c_1 + \gamma c_2 = 0$ then gives
>
> $$
> c_2 = -\frac{f_0}{\Delta}\,\frac b\gamma\,\frac{\omega^2 + \mu^2}{2} .
> $$
>
> As $t$ increases the terms from the complementary solution die out (the factor $e^{-bt/2}$), while the particular solution persists: it is the steady-state response.
>
> *Powers: 0.2, Example (Forced Vibrations)*

^ex-3-3

The three cases are [[§24 Forced Periodic Vibrations#^prop-24-3|331 Prop. §24.3]] (beats), [[§24 Forced Periodic Vibrations#^prop-24-4|331 Prop. §24.4]] (undamped resonance) and [[§24 Forced Periodic Vibrations#^thm-24-1|331 Thm. §24.1]] (the damped steady-state response), with graphs.

*Continued in [[§4★ Variation of Parameters]]: variation of parameters and the particular solution as a Green's function integral.*
