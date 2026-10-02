---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 0
section: 4
powers: "0.4"
aliases: ["Powers 0.4"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§3★ Boundary Value Problems]] · ↑ [[· 0★ Ordinary Differential Equations Review]] · [[§5★ Green's Functions]] →

*Powers, Section 0.4.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

A boundary value problem is singular when an endpoint of the interval is a singular point of the differential equation, or when the interval is infinitely long. In both cases there is nowhere to impose an ordinary boundary condition at that end, and its place is taken by the requirement that the solution stay bounded. The first case arises whenever a boundary point is a mathematical boundary but not a physical one, like the center $r = 0$ of a disk described in polar coordinates; the second whenever a body is so long (a cooling fin, a semi-infinite rod) that its far end is idealized away. The section shows that a boundedness condition works exactly like a boundary condition: it removes one of the two constants. These conditions will be imposed on every problem in a disk, cylinder or sphere (Chapter 5) and on every unbounded region.

> [!definition] Definition §4.1: Singular Boundary Value Problem
> A boundary value problem is **singular** if
> 1. an endpoint of the interval of interest is a singular point of the differential equation ([[§1★ Homogeneous Linear Equations#^def-1-6|Definition §1.6]]), or
> 2. the interval is infinitely long.
>
> *Powers: 0.4 (text)*

^def-4-1

## Regular Singular Points

Recall ([[§1★ Homogeneous Linear Equations#^def-1-6|Definition §1.6]]) that $x_0$ is a regular singular point of $u'' + k(x)u' + p(x)u = f(x)$ if $k(x)$ or $p(x)$ or both become infinite as $x \to x_0$, but $(x - x_0)k(x)$ and $(x - x_0)^2p(x)$ both have Taylor series expansions centered at $x_0$.

> [!example] Example §4.1: Locating Singular Points
> To find singular points, first divide by the coefficient of $u''$ to reach the form $u'' + ku' + pu = f$.
>
> **(a)** $(1 - x)u'' + u' + xu = 0$. In standard form,
>
> $$
> u'' + \frac{1}{1 - x}u' + \frac{x}{1 - x}u = 0 .
> $$
>
> Both $k(x) = \frac1{1 - x}$ and $p(x) = \frac x{1 - x}$ become infinite at $x = 1$, but $(x - 1)k(x) = -1$ and $(x - 1)^2p(x) = -x(x - 1)$ are polynomials, so they have Taylor series about $x = 1$: $x_0 = 1$ is a regular singular point.
>
> **(b)** $\dfrac1r\dfrac{d}{dr}\Big(r\dfrac{du}{dr}\Big) = u$, the radial part of a polar-coordinate problem. Carrying out the differentiation, $u'' + \frac1ru' - u = 0$. Here $rk(r) = 1$ and $r^2p(r) = -r^2$, so $r = 0$ is a regular singular point.
>
> **(c)** $\dfrac{d}{dx}\Big((1 - x^2)\dfrac{du}{dx}\Big) = 0$, a Legendre-type equation. Then $(1 - x^2)u'' - 2xu' = 0$, that is $u'' - \frac{2x}{1 - x^2}u' = 0$, singular at $x = \pm1$. At $x = 1$, $(x - 1)k(x) = \frac{2x}{1 + x}$ has a Taylor series about $1$; similarly at $x = -1$. Both are regular singular points.
>
> **(d)** $\dfrac1{\rho^2}\dfrac{d}{d\rho}\Big(\rho^2\dfrac{du}{d\rho}\Big) = -\lambda^2u$, the radial part of a spherical problem. Then $u'' + \frac2\rho u' + \lambda^2u = 0$, and $\rho k = 2$, $\rho^2p = \lambda^2\rho^2$: $\rho = 0$ is a regular singular point.
>
> The Cauchy–Euler equation of [[§1★ Homogeneous Linear Equations#^def-1-5|Definition §1.5]] is another example, with a regular singular point at the origin.
>
> *Powers: 0.4, Example (regular singular point); Exercise 0.4.1*

^ex-4-1

This situation typically arises when a boundary point is a mathematical boundary without being a physical boundary. A disk of radius $c$ is described in polar coordinates by $0 \le r \le c$; the origin $r = 0$ is a boundary of this interval, yet physically it is a point in the interior of the disk.

> [!definition] Definition §4.2: Boundedness Condition at a Singular Point
> At a singular point $x_0$ one cannot specify a value for the solution $u(x_0)$ or its derivative. Instead one requires that
>
> $$
> u(x_0), \quad u'(x_0) \quad \text{be finite (bounded)} .
> $$
>
> This is tacitly required at every point of the interval where a differential equation is solved; when a singular point is a boundary point of that interval, the condition is enforced explicitly, in place of a boundary condition.
>
> *Powers: 0.4 (text)*

^def-4-2

> [!example] Example §4.2: Radial Heat Flow in a Rod
> A long cylindrical bar of radius $c$, surrounded by a medium at temperature $T$, carries an electric current. If heat flows radially much faster than axially, the temperature $u(r)$ satisfies
>
> $$
> \frac1r\frac{d}{dr}\Big(r\frac{du}{dr}\Big) = -H, \quad 0 \le r < c, \qquad u(c) = T , \qquad (1), (2)
> $$
>
> with $H$ a constant proportional to the electric power converted into heat. Only the physical boundary condition (2) is given. In the form $u'' + \frac1ru' = -H$ the equation shows that $r = 0$ is a singular point, so we add
>
> $$
> u(0), \quad u'(0) \quad \text{finite} . \qquad (3)
> $$
>
> **Solve.** Multiply (1) by $r$ and integrate: $r\dfrac{du}{dr} = -H\dfrac{r^2}{2} + c_1$. Divide by $r$ and integrate again:
>
> $$
> u(r) = -H\frac{r^2}{4} + c_1\ln(r) + c_2 .
> $$
>
> **Boundedness.** Both $\ln r$ and its derivative $1/r$ become infinite as $r \to 0$, while the other terms stay finite, so (3) forces $c_1 = 0$.
>
> **Boundary condition.** $u(c) = -Hc^2/4 + c_2 = T$ gives $c_2 = Hc^2/4 + T$, and
>
> $$
> u(r) = \frac{H(c^2 - r^2)}{4} + T . \qquad (4)
> $$
>
> The temperature is highest on the axis, $u(0) = T + Hc^2/4$, and falls parabolically to the surface.
>
> *Powers: 0.4, Example (Radial Heat Flow)*

^ex-4-2

> [!remark] Remark: Boundedness Works Like a Boundary Condition
> In Example §4.2 the "artificial" condition, boundedness of $u$ at the singular point $r = 0$, worked exactly as an ordinary boundary condition at a regular point does: it gave one condition on the unknown constants $c_1$, $c_2$, which were then completely determined by the second, physical boundary condition. The mechanism is that here one solution of the homogeneous equation is bounded near $r = 0$ ($1$) and the other is not ($\ln r$), so boundedness selects a one-dimensional family, just as a boundary condition does. This is the typical situation at the singular points met in this subject (Bessel's and Legendre's equations), but not a general law: both solutions $t$, $t^2$ of the Cauchy–Euler equation $t^2u'' - 2tu' + 2u = 0$ are bounded at $t = 0$.

^rem-4-1

## Semi-Infinite and Infinite Intervals

The other type of singular boundary value problem has an infinite interval of interest, always a mathematical abstraction that cannot be realized physically.

> [!definition] Definition §4.3: Semi-Infinite Interval; Boundedness at Infinity
> The interval $0 < x < \infty$ is called **semi-infinite**: it has one finite endpoint, where a boundary condition is normally imposed. At the other "end" no boundary condition is imposed, because no boundary exists. Instead one normally requires that $u(x)$ and $u'(x)$ remain bounded as $x$ increases: there are constants $M$ and $M'$ with
>
> $$
> |u(x)| \le M \qquad\text{and}\qquad |u'(x)| \le M'
> $$
>
> for all $x$, no matter how large. $M$ and $M'$ are never identified, and the condition is written
>
> $$
> u(x) \quad\text{and}\quad u'(x) \quad \text{bounded as } x \to \infty .
> $$
>
> On $-\infty < x < \infty$ the same condition is imposed as $x \to \pm\infty$.
>
> *Powers: 0.4 (text)*

^def-4-3

> [!theorem] Proposition §4.1: Bounded Solutions of u″ − μ²u = 0
> Let $\mu > 0$. A solution $u(x) = c_1'e^{\mu x} + c_2'e^{-\mu x}$ of $u'' - \mu^2u = 0$ is bounded on $0 < x < \infty$ (together with $u'$) if and only if $c_1' = 0$, that is, $u$ is a constant multiple of $e^{-\mu x} = \cosh(\mu x) - \sinh(\mu x)$. On $-\infty < x < \infty$, only $u \equiv 0$ is bounded.
>
> *Powers: 0.4 (text)*

^prop-4-1

> [!proof]+ Proof
> If $c_1' = 0$, then $|u| = |c_2'|e^{-\mu x} \le |c_2'|$ and $|u'| = \mu|c_2'|e^{-\mu x} \le \mu|c_2'|$ for $x > 0$. If $c_1' \ne 0$, then for $x > 0$
>
> $$
> |u(x)| \ge |c_1'|e^{\mu x} - |c_2'|e^{-\mu x} \ge |c_1'|e^{\mu x} - |c_2'| \longrightarrow \infty \qquad (x \to \infty) ,
> $$
>
> so $u$ is unbounded. In terms of $\cosh$ and $\sinh$: by [[§1★ Homogeneous Linear Equations#^def-1-4|Definition §1.4]], $c_1\cosh(\mu x) + c_2\sinh(\mu x) = \frac{c_1 + c_2}2e^{\mu x} + \frac{c_1 - c_2}2e^{-\mu x}$, which is bounded exactly when $c_2 = -c_1$, and then equals $c_1e^{-\mu x}$. On the whole line, the same argument as $x \to -\infty$ forces $c_2' = 0$ as well.

^pf-4-1

*Uses:* [[§1★ Homogeneous Linear Equations#^def-1-4|Def. §1.4]]

> [!example] Example §4.3: A Long Cooling Fin
> A long cooling fin has one end held at a constant temperature $T_0$ and exchanges heat by convection with a medium at temperature $T$. Its temperature satisfies
>
> $$
> \frac{d^2u}{dx^2} = \frac{hC}{\kappa A}(u - T), \quad 0 < x, \qquad u(0) = T_0 \qquad (5), (6)
> $$
>
> (the equation of [[§3★ Boundary Value Problems#^prop-3-2|Proposition §3.2]] with the convective source of [[§3★ Boundary Value Problems#^def-3-2|Definition §3.2]]). The problem is posed on a semi-infinite interval because the fin is very long, and perhaps to mask our ignorance of what happens at its other physical end; so we impose
>
> $$
> u(x), \quad u'(x) \quad \text{bounded as } x \to \infty . \qquad (7)
> $$
>
> **General solution.** With $\mu = \sqrt{hC/\kappa A}$, $w = u - T$ satisfies $w'' - \mu^2w = 0$, so
>
> $$
> u(x) = T + c_1\cosh(\mu x) + c_2\sinh(\mu x) .
> $$
>
> **Conditions.** $u(0) = T + c_1 = T_0$ gives $c_1 = T_0 - T$. Boundedness (7) requires $c_2 = -c_1$: of all linear combinations of $\cosh$ and $\sinh$, the only ones bounded as $x \to \infty$ are the multiples of $\cosh(\mu x) - \sinh(\mu x) = e^{-\mu x}$ ([[§4★ Singular Boundary Value Problems#^prop-4-1|Proposition §4.1]]). So
>
> $$
> u(x) = T + (T_0 - T)\big(\cosh(\mu x) - \sinh(\mu x)\big) = T + (T_0 - T)e^{-\mu x} .
> $$
>
> The fin's temperature decays exponentially from $T_0$ to the surrounding temperature, over a length of order $1/\mu$.
>
> *Powers: 0.4, Example (Cooling Fin)*

^ex-4-3

![[m341-4-1.svg]]
*Why boundedness fixes the second constant in Example §4.3: every solution $u = T + c_1\cosh\mu x + c_2\sinh\mu x$ with $u(0) = T_0$ starts at the same point, but unless $c_2 = -c_1$ exactly, the growing part $\frac{c_1 + c_2}2e^{\mu x}$ eventually takes over (blue: $c_2 = -0.8c_1, -0.9c_1, -0.97c_1$; orange: $c_2 = -1.03c_1, -1.1c_1, -1.2c_1$). Only the red curve $e^{-\mu x}$ stays bounded.*

> [!remark] Remark: Method — Choosing the Form of the Solution of u″ − μ²u = 0
> Satisfying the boundedness condition in Example §4.3 would have been simpler with the general solution written as $u = T + c_1'e^{\mu x} + c_2'e^{-\mu x}$: one sees at once that $c_1' = 0$ is the only way. As a rule of thumb, the solution of
>
> $$
> \frac{d^2u}{dx^2} - \mu^2u = 0
> $$
>
> on an interval $I$ is best expressed as
>
> $$
> u(x) = \begin{cases} c_1\cosh(\mu x) + c_2\sinh(\mu x), & \text{if } I \text{ is finite}, \\ c_1e^{\mu x} + c_2e^{-\mu x}, & \text{if } I \text{ is infinite}. \end{cases}
> $$
>
> On a finite interval $0 < x < a$, $\cosh$ and $\sinh$ (or their shifts $\sinh\mu(a - x)$, $\cosh\mu(x - a/2)$) make boundary conditions at the ends easy to apply ([[§3★ Boundary Value Problems#^ex-3-3|Example §3.3]]); on an infinite interval the exponentials separate the bounded solution from the unbounded one.

^rem-4-2

## The Radial Operator in Spherical Coordinates

Problems in a sphere lead to the operator $\frac1{\rho^2}\frac{d}{d\rho}\big(\rho^2\frac{du}{d\rho}\big)$ of Example §4.1(d). A substitution reduces it to a second derivative (Powers' Exercises 0.1.19 and 0.4.4). The radial solutions $\sin(\lambda\rho)/\rho$ it produces reappear for spherical waves, [[§48★ Some Applications of Bessel Functions#^prop-48-4|Proposition §48.4]] (Powers 5.8), where Powers obtains them from Bessel functions of order $\frac12$.

> [!theorem] Lemma §4.2: The Substitution u = v/ρ
> For a twice differentiable function $v$ on $\rho > 0$ and $u = v/\rho$,
>
> $$
> \frac1{\rho^2}\frac{d}{d\rho}\Big(\rho^2\frac{du}{d\rho}\Big) = \frac1\rho\frac{d^2v}{d\rho^2} .
> $$
>
> In particular $\frac1{\rho^2}(\rho^2u')' = -\mu^2u$ if and only if $v'' + \mu^2v = 0$, and $\frac1{\rho^2}(\rho^2u')' = 0$ if and only if $v'' = 0$.
>
> *Powers: Exercises 0.1.19 and 0.4.4*

^lem-4-2

> [!proof]+ Proof
> With $u = v/\rho$, $u' = \dfrac{v'}{\rho} - \dfrac{v}{\rho^2}$, so $\rho^2u' = \rho v' - v$ and
>
> $$
> \frac{d}{d\rho}\big(\rho^2u'\big) = v' + \rho v'' - v' = \rho v'' .
> $$
>
> Dividing by $\rho^2$ gives $v''/\rho$. Since $-\mu^2u = -\mu^2v/\rho$, the two equations are equivalent after multiplying by $\rho > 0$.

^pf-4-2

> [!remark]- Connections
> - The operator of Lemma §4.2 is the Laplacian of a radial function in space, [[§19 The Laplacian in Spherical Coordinates#^rem-19-2|452 Remark: Verification: Radial Functions]]; with $\mu = 0$ the lemma gives $v = c_1 + c_2\rho$, so the radial harmonic functions are $c_2 + c_1/\rho$, the constants and the fundamental solution $C/r$. The planar counterpart $\frac1r\frac{d}{dr}\big(r\frac{du}{dr}\big)$ of Example §4.2 has the homogeneous solutions $1$ and $\ln r$; the second is, up to a constant factor, the fundamental solution of [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-5|452 Thm. §17.5]].

> [!example] Example §4.4: The Critical Radius of a Uranium Sphere
> The neutron flux $u$ in a sphere of uranium of radius $a$ obeys
>
> $$
> \frac\lambda3\,\frac1{\rho^2}\frac{d}{d\rho}\Big(\rho^2\frac{du}{d\rho}\Big) + (k - 1)Au = 0, \qquad 0 < \rho < a ,
> $$
>
> where $\lambda$ is the effective distance a neutron travels between collisions, $A$ the absorption cross section and $k > 1$ the number of neutrons produced by a collision during fission. The flux is $0$ at the boundary, $u(a) = 0$, and $u$ must be bounded at the singular point $\rho = 0$. For which radius $a$ is there a solution other than $u \equiv 0$?
>
> **Reduce.** With $\mu^2 = 3(k - 1)A/\lambda > 0$ the equation reads $\frac1{\rho^2}(\rho^2u')' = -\mu^2u$, and by Lemma §4.2 the substitution $u = v/\rho$ turns it into $v'' + \mu^2v = 0$. So
>
> $$
> v(\rho) = c_1\cos(\mu\rho) + c_2\sin(\mu\rho), \qquad u(\rho) = c_1\frac{\cos(\mu\rho)}{\rho} + c_2\frac{\sin(\mu\rho)}{\rho} .
> $$
>
> **Boundedness.** $\cos(\mu\rho)/\rho \to \infty$ as $\rho \to 0$, while $\sin(\mu\rho)/\rho \to \mu$ and its derivative $(\mu\rho\cos\mu\rho - \sin\mu\rho)/\rho^2 \to 0$. So boundedness forces $c_1 = 0$, and $u = c_2\sin(\mu\rho)/\rho$.
>
> **Boundary condition.** $u(a) = c_2\sin(\mu a)/a = 0$ has a solution with $c_2 \ne 0$ exactly when $\mu a = n\pi$. The smallest such radius,
>
> $$
> a = \frac\pi\mu = \pi\sqrt{\frac{\lambda}{3(k - 1)A}} ,
> $$
>
> is the **critical radius**: there a nonzero, self-sustaining neutron flux $u = c_2\sin(\pi\rho/a)/\rho$ exists. This is an eigenvalue problem ([[§3★ Boundary Value Problems#^def-3-3|Definition §3.3]]) with a boundedness condition at one end, the same structure as the buckling column ([[§3★ Boundary Value Problems#^ex-3-4|Example §3.4]]).
>
> *Powers: Exercises 0.4.4 and 0.4.5*

^ex-4-4
