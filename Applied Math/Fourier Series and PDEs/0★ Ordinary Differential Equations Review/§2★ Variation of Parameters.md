---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 0
section: 2
powers: "0.2"
aliases: ["Powers 0.2 (cont.)"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§2★ Nonhomogeneous Linear Equations]] · ↑ [[· 0★ Ordinary Differential Equations Review]] →

*Powers, Section 0.2.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

This section continues [[§2★ Nonhomogeneous Linear Equations|§2★]] with variation of parameters, which always works once the homogeneous equation is solved. It leads to a formula $u_p(t) = \int_{t_0}^t G(t, z)f(z)\,dz$ that expresses the response to a forcing $f$ as a superposition of responses to its values, the first appearance of a Green's function; [[§5★ Green's Functions|§5★]] builds the same kind of formula for boundary value problems.

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
