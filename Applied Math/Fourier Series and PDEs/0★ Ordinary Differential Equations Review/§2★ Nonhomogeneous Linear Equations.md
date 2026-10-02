---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 0
section: 2
powers: "0.2"
aliases: ["Powers 0.2"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§1★ Homogeneous Linear Equations]] · ↑ [[· 0★ Ordinary Differential Equations Review]] · [[§3★ Boundary Value Problems]] →

*Powers, Section 0.2.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

A nonhomogeneous linear equation $u'' + k(t)u' + p(t)u = f(t)$ is solved in two parts: the general solution of the homogeneous equation ([[§1★ Homogeneous Linear Equations|§1★]]) plus one particular solution. This section reviews the two ways of finding a particular solution: undetermined coefficients, a guess that works for constant coefficients and simple inhomogeneities, and variation of parameters, which always works once the homogeneous equation is solved. The second leads to a formula $u_p(t) = \int_{t_0}^t G(t, z)f(z)\,dz$ that expresses the response to a forcing $f$ as a superposition of responses to its values, the first appearance of a Green's function; [[§5★ Green's Functions|§5★]] builds the same kind of formula for boundary value problems. Physically, the forced mass–spring–damper shows resonance. All of this is proved in [[Ordinary Differential Equations]], and each item links to its home there.

## Particular and Complementary Solutions

> [!definition] Definition §2.1: Inhomogeneity; Particular and Complementary Solutions
> In the nonhomogeneous linear equations
>
> $$
> \frac{du}{dt} = k(t)u + f(t), \qquad \frac{d^2u}{dt^2} + k(t)\frac{du}{dt} + p(t)u = f(t) ,
> $$
>
> the function $f(t)$, not identically $0$, is the **inhomogeneity**. A **particular solution** $u_p(t)$ is any one solution of the nonhomogeneous equation; the **complementary solution** $u_c(t)$ is the general solution of the corresponding homogeneous equation (the same equation with $f = 0$).
>
> *Powers: 0.2 (text)*

^def-2-1

This is [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^def-17-1|331 Def. §17.1]].

> [!theorem] Theorem §2.1: The Simplest Nonhomogeneous Equations
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

^thm-2-1

> [!proof]+ Proof
> By the Fundamental Theorem of Calculus, $F(t) = \int_{t_0}^t f(z)\,dz$ satisfies $F' = f$. If $u' = f$, then $(u - F)' = 0$, so $u - F$ is a constant $c$; conversely every $F + c$ solves (1). For (4), $u'' = f$ means that $u'$ solves (1), so $u'(s) = \int_{t_0}^s f(z)\,dz + c_1$, and integrating once more gives the stated formula (with a new constant $c_2$).

^pf-2-1

*Uses:* [[§36 The Fundamental Theorem of Calculus#^thm-36-1|Calc Thm. §36.1]] (FTC), [[§26 The Mean Value Theorem#^cor-26-4|Calc Cor. §26.4]] (zero derivative means constant)

> [!theorem] Theorem §2.2: Structure of the General Solution
> The general solution of a nonhomogeneous linear equation has the form
>
> $$
> u(t) = u_p(t) + u_c(t) ,
> $$
>
> where $u_p(t)$ is any particular solution of the nonhomogeneous equation and $u_c(t)$ is the general solution of the corresponding homogeneous equation.
>
> *Powers: 0.2, Theorem 1*

^thm-2-2

*Proved in ODE: [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-2|331 Thm. §17.2]] (via [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-1|331 Thm. §17.1]]: the difference of two solutions solves the homogeneous equation).*

> [!theorem] Theorem §2.3: Superposition of Inhomogeneities
> If $u_{p1}(t)$ and $u_{p2}(t)$ are particular solutions of a linear differential equation with inhomogeneities $f_1(t)$ and $f_2(t)$, respectively, then $k_1u_{p1}(t) + k_2u_{p2}(t)$ is a particular solution of the same differential equation with inhomogeneity $k_1f_1(t) + k_2f_2(t)$ ($k_1$, $k_2$ constants).
>
> *Powers: 0.2, Theorem 2*

^thm-2-3

> [!proof]+ Proof
> Write the equation as $L[u] = f$, with $L[u] = u'' + k(t)u' + p(t)u$ (or $L[u] = u' - k(t)u$). The computation in the proof of superposition, [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-2|331 Thm. §14.2]], shows $L[k_1u_1 + k_2u_2] = k_1L[u_1] + k_2L[u_2]$ for any twice differentiable $u_1$, $u_2$. Hence $L[k_1u_{p1} + k_2u_{p2}] = k_1f_1 + k_2f_2$.

^pf-2-3

*Uses:* [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-2|331 Thm. §14.2]]

The sum case for constant coefficients is [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^prop-17-3|331 Prop. §17.3]].

> [!example] Example §2.1: Assembling a General Solution
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
> **Combine.** By Theorem §2.3 with $k_1 = 1$, $k_2 = -1$, a particular solution of the given equation is $u_p(t) = 1 - \frac12e^{-t}$, and by Theorem §2.2 the general solution is
>
> $$
> u(t) = 1 - \tfrac12e^{-t} + c_1\cos(t) + c_2\sin(t) .
> $$
>
> If two initial conditions are given, $c_1$ and $c_2$ are available to satisfy them. An initial condition applies to the entire solution, not just to $u_c(t)$.
>
> *Powers: 0.2, Example (Theorems 1 and 2)*

^ex-2-1

## Undetermined Coefficients

This method guesses the form of a trial solution and then finds its coefficients. It is limited to equations with constant coefficients and inhomogeneities of simple form.

> [!theorem] Theorem §2.4: Undetermined Coefficients
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

^thm-2-4

*Powers omits the proof. The same table, with the power $t^s$ of the Revision Rule built in, is [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-4|331 Thm. §17.4]], where it is explained.*

> [!example] Example §2.2: Trial Solutions and the Revision Rule
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

^ex-2-2

> [!example] Example §2.3: Forced Vibrations and Resonance
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

^ex-2-3

The three cases are [[§20 Forced Periodic Vibrations#^prop-20-3|331 Prop. §20.3]] (beats), [[§20 Forced Periodic Vibrations#^prop-20-4|331 Prop. §20.4]] (undamped resonance) and [[§20 Forced Periodic Vibrations#^thm-20-1|331 Thm. §20.1]] (the damped steady-state response), with graphs.

## Variation of Parameters

If a linear homogeneous equation can be solved, the corresponding nonhomogeneous equation can also be solved, at least in terms of integrals.

> [!theorem] Theorem §2.5: Variation of Parameters for First-Order Equations
> Let $u_c(t)$ be a nonzero solution of the homogeneous equation
>
> $$
> \frac{du}{dt} = k(t)u . \qquad (5)
> $$
>
> Then $u_p(t) = v(t)u_c(t)$ is a particular solution of
>
> $$
> \frac{du}{dt} = k(t)u + f(t) \qquad (6)
> $$
>
> if and only if
>
> $$
> \frac{dv}{dt} = \frac{f(t)}{u_c(t)} , \qquad (8)
> $$
>
> a nonhomogeneous equation of the simplest type, solved for $v$ by one integration (Theorem §2.1).
>
> *Powers: 0.2, Equations (5)–(8)*

^thm-2-5

> [!proof]+ Proof
> Substituting $u_p = vu_c$ into (6) gives
>
> $$
> \frac{dv}{dt}u_c + v\frac{du_c}{dt} = k(t)vu_c + f(t) . \qquad (7)
> $$
>
> Since $u_c' = k(t)u_c$, the second term on the left cancels the first on the right, leaving $v'u_c = f$. By [[§1★ Homogeneous Linear Equations#^thm-1-1|Theorem §1.1]], $u_c = ce^{\int k\,dt}$ with $c \ne 0$, which never vanishes, so this is equivalent to (8).

^pf-2-5

*Uses:* [[§1★ Homogeneous Linear Equations#^thm-1-1|§1.1]], [[§2★ Nonhomogeneous Linear Equations#^thm-2-1|§2.1]]

The resulting formula $u_p = u_c\int f/u_c\,dt$ is the integrating-factor solution [[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-2|331 Thm. §4.2]], with $1/u_c$ as the integrating factor.

> [!example] Example §2.4: A First-Order Equation
> Find a solution of $\dfrac{du}{dt} = 5u + t$.
>
> Since $e^{5t}$ solves $u' = 5u$, try $u_p(t) = v(t)e^{5t}$. Substituting, $v'e^{5t} + 5ve^{5t} = 5ve^{5t} + t$, so $v' = te^{-5t}$. Integrating by parts,
>
> $$
> v(t) = \int te^{-5t}\,dt = -\frac t5e^{-5t} + \frac15\int e^{-5t}\,dt = \Big(-\frac t5 - \frac1{25}\Big)e^{-5t} ,
> $$
>
> and $u_p(t) = v(t)e^{5t} = -\big(\frac15t + \frac1{25}\big)$. Check: $u_p' = -\frac15$ and $5u_p + t = -t - \frac15 + t = -\frac15$.
>
> *Powers: 0.2, Example (first-order variation of parameters)*

^ex-2-4

> [!theorem] Theorem §2.6: Variation of Parameters for Second-Order Equations
> Let $u_1(t)$, $u_2(t)$ be independent solutions of the homogeneous equation
>
> $$
> \frac{d^2u}{dt^2} + k(t)\frac{du}{dt} + p(t)u = 0 . \qquad (10)
> $$
>
> Then a particular solution of
>
> $$
> \frac{d^2u}{dt^2} + k(t)\frac{du}{dt} + p(t)u = f(t) \qquad (9)
> $$
>
> has the form
>
> $$
> u_p(t) = v_1(t)u_1(t) + v_2(t)u_2(t) , \qquad (11)
> $$
>
> where $v_1'$, $v_2'$ solve the simultaneous equations
>
> $$
> v_1'u_1 + v_2'u_2 = 0, \qquad v_1'u_1' + v_2'u_2' = f(t) , \qquad (12'), (15)
> $$
>
> whose determinant is the Wronskian $W(t) = u_1u_2' - u_2u_1'$, nonzero because $u_1$, $u_2$ are independent (16). Explicitly,
>
> $$
> v_1' = -\frac{u_2f}{W}, \quad v_2' = \frac{u_1f}{W}; \qquad v_1(t) = -\int_{t_0}^{t}\frac{u_2(z)f(z)}{W(z)}\,dz, \quad v_2(t) = \int_{t_0}^{t}\frac{u_1(z)f(z)}{W(z)}\,dz , \qquad (20), (22)
> $$
>
> where the lower limit $t_0$ is usually the initial value of $t$ but may be any convenient value.
>
> *Powers: 0.2, Equations (9)–(22)*

^thm-2-6

*Proved in ODE: [[§18★ Variation of Parameters#^thm-18-1|331 Thm. §18.1]]. Powers' derivation is the same: the extra requirement (12) makes $u_p' = v_1u_1' + v_2u_2'$ free of $v_1'$, $v_2'$ (13), so that substituting $u_p$ and $u_p'' = v_1'u_1' + v_2'u_2' + v_1u_1'' + v_2u_2''$ (14) into (9) leaves only (15), the multipliers of $v_1$ and $v_2$ being zero because $u_1$, $u_2$ solve (10).*

> [!theorem] Theorem §2.7: The Particular Solution as a Green's Function Integral
> Let $u_1(t)$ and $u_2(t)$ be independent solutions of
>
> $$
> \frac{d^2u}{dt^2} + k(t)\frac{du}{dt} + p(t)u = 0 \qquad \text{(H)}
> $$
>
> with Wronskian $W(t) = u_1(t)u_2'(t) - u_2(t)u_1'(t)$. Then
>
> $$
> u_p(t) = \int_{t_0}^{t} G(t, z)f(z)\,dz
> $$
>
> is a particular solution of the nonhomogeneous equation
>
> $$
> \frac{d^2u}{dt^2} + k(t)\frac{du}{dt} + p(t)u = f(t) , \qquad \text{(NH)}
> $$
>
> where $G$ is the **Green's function** defined by
>
> $$
> G(t, z) = \frac{u_1(z)u_2(t) - u_2(z)u_1(t)}{W(z)} . \qquad (23)
> $$
>
> *Powers: 0.2, Theorem 3*

^thm-2-7

*Powers obtains it from (22): $u_p(t) = -u_1(t)\int_{t_0}^t \frac{u_2f}{W}\,dz + u_2(t)\int_{t_0}^t \frac{u_1f}{W}\,dz$, and the factors $u_1(t)$, $u_2(t)$ can be moved inside the integrals, which are not with respect to $t$. Proved in ODE: [[§18★ Variation of Parameters#^cor-18-2|331 Cor. §18.2]], which also shows that this $u_p$ is the solution with $u_p(t_0) = 0$, $u_p'(t_0) = 0$.*

> [!remark]- Connections
> - For constant coefficients $G(t, z)$ depends only on $t - z$ ([[§2★ Nonhomogeneous Linear Equations#^ex-2-5|Example §2.5]](a)), so $u_p$ is a convolution; the Laplace transform produces it as the impulse response, [[§26★ The Convolution Integral#^thm-26-3|331 Thm. §26.3]] (and in this subject [[§52★ Partial Fractions and Convolutions#^ex-52-5|Example §52.5]], by the convolution theorem [[§52★ Partial Fractions and Convolutions#^thm-52-3|Theorem §52.3]], Powers 6.2).

> [!remark] Remark: Reading the Green's Function
> For fixed $z$, $G(t, z)$ as a function of $t$ is the solution of the homogeneous equation (H) with $G(z, z) = 0$ and $\partial_tG(z, z) = \frac{u_1(z)u_2'(z) - u_2(z)u_1'(z)}{W(z)} = 1$. So $u_p(t) = \int_{t_0}^tG(t, z)f(z)\,dz$ adds up, for each earlier time $z$, the free motion started at time $z$ by a unit kick, weighted by $f(z)\,dz$: the effect of the forcing is a superposition of its effects at each instant. This is the initial-value version of the Green's function; [[§5★ Green's Functions#^def-5-2|Definition §5.2]] builds one that satisfies boundary conditions at both ends of an interval, starting from this formula.

^rem-2-1

> [!example] Example §2.5: Forcing a Harmonic Oscillator
> **(a)** Use Theorem §2.7 to show that a particular solution of $u'' + \gamma^2u = f(t)$ ($\gamma > 0$) is
>
> $$
> u_p(t) = \frac1\gamma\int_0^t \sin\gamma(t - z)\,f(z)\,dz .
> $$
>
> With $u_1 = \cos(\gamma t)$, $u_2 = \sin(\gamma t)$, the Wronskian is $W = \cos(\gamma t)\cdot\gamma\cos(\gamma t) - \sin(\gamma t)\cdot(-\gamma\sin(\gamma t)) = \gamma$, and by (23)
>
> $$
> G(t, z) = \frac{\cos(\gamma z)\sin(\gamma t) - \sin(\gamma z)\cos(\gamma t)}{\gamma} = \frac{\sin\gamma(t - z)}{\gamma} .
> $$
>
> Theorem §2.7 with $t_0 = 0$ gives the formula.
>
> **(b)** Solve $u'' + u = \cos(\omega t)$, $\omega \ne 1$, by variation of parameters. With $u_1 = \cos t$, $u_2 = \sin t$ (so $W = 1$), the equations (12′), (15) read
>
> $$
> v_1'\cos(t) + v_2'\sin(t) = 0, \qquad -v_1'\sin(t) + v_2'\cos(t) = \cos(\omega t) , \qquad (17), (18)
> $$
>
> with solution
>
> $$
> v_1' = -\sin(t)\cos(\omega t), \qquad v_2' = \cos(t)\cos(\omega t) . \qquad (19)
> $$
>
> Powers stops here. Integrating from $0$ is the same as using (a) with $\gamma = 1$:
>
> $$
> u_p(t) = \int_0^t \sin(t - z)\cos(\omega z)\,dz = \frac12\int_0^t\Big(\sin\big(t - (1 - \omega)z\big) + \sin\big(t - (1 + \omega)z\big)\Big)dz ,
> $$
>
> using $\sin A\cos B = \frac12(\sin(A + B) + \sin(A - B))$ with $A = t - z$, $B = \omega z$. Since $\int_0^t\sin(t - cz)\,dz = \frac{\cos\big((1 - c)t\big) - \cos t}{c}$ for $c \ne 0$, this is
>
> $$
> u_p(t) = \frac12\Big(\frac{\cos(\omega t) - \cos t}{1 - \omega} + \frac{\cos(\omega t) - \cos t}{1 + \omega}\Big) = \frac{\cos(\omega t) - \cos(t)}{1 - \omega^2} .
> $$
>
> It satisfies $u_p(0) = u_p'(0) = 0$; adding the complementary solution $c_1\cos t + c_2\sin t$ absorbs the $-\cos t$ term and recovers the undamped particular solution $\frac{\cos\omega t}{1 - \omega^2}$ of [[§2★ Nonhomogeneous Linear Equations#^ex-2-3|Example §2.3]] (there with $\omega$ and $\mu$ in place of $1$ and $\omega$).
>
> *Powers: 0.2, Example (variation of parameters); Exercise 0.2.20*

^ex-2-5

