---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 5
section: "54★"
powers: "5.4"
aliases: ["Powers 5.4"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§53 Two-Dimensional Heat Equation꞉ Solution]] · ↑ [[· 5 Higher Dimensions and Other Coordinates]] · [[§55★ Bessel's Equation]] →

*Powers, Section 5.4.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

This section sets up the vibrations of a circular membrane and heat conduction in a circular plate, side by side, in polar coordinates. As in one dimension and on the rectangle, the two problems share their steady state, a potential problem in a disk, and their eigenvalue problem. Separating variables in the eigenvalue problem $\nabla^2\phi = -\lambda^2\phi$ gives the periodic problem in $\theta$ already solved for the potential in a disk, with $\cos m\theta$ and $\sin m\theta$, and a new radial equation, Bessel's equation, which is solved in [[§55★ Bessel's Equation|§45]]. Physically this is the mathematics of drums, circular plates and cylinders, and the same separation in polar coordinates reappears for the quantum particle in a circular box.

## Heat and Wave Problems in a Disk

> [!definition] Definition §54.1: Heat and Wave Problems in a Disk
> In the disk $0 < r < a$, the **wave problem** (circular membrane) and the **heat problem** (circular plate) for $v(r, \theta, t)$ are
>
> | | Wave | Heat |
> |---|---|---|
> | equation | $\nabla^2v = \dfrac{1}{c^2}\dfrac{\partial^2v}{\partial t^2}$ | $\nabla^2v = \dfrac{1}{k}\dfrac{\partial v}{\partial t}$ |
> | boundary condition | $v(a, \theta, t) = f(\theta)$ | $v(a, \theta, t) = f(\theta)$ |
> | initial conditions | $v(r, \theta, 0) = g(r, \theta)$, $\ \dfrac{\partial v}{\partial t}(r, \theta, 0) = h(r, \theta)$ | $v(r, \theta, 0) = g(r, \theta)$ |
>
> for $0 < r < a$, $0 < t$, where $\nabla^2$ is the Laplacian in polar coordinates,
>
> $$
> \nabla^2v = \frac{\partial^2v}{\partial r^2} + \frac{1}{r}\frac{\partial v}{\partial r} + \frac{1}{r^2}\frac{\partial^2v}{\partial\theta^2} = \frac{1}{r}\frac{\partial}{\partial r}\Big(r\frac{\partial v}{\partial r}\Big) + \frac{1}{r^2}\frac{\partial^2v}{\partial\theta^2} .
> $$
>
> In both problems $v$ must be periodic in $\theta$ with period $2\pi$, $v(r, \theta, t) = v(r, \theta + 2\pi, t)$, and bounded as $r \to 0$, as for the potential in a disk.
>
> *Powers: 5.4 (text)*

^def-54-1

> [!remark]- Connections
> - The polar form of the Laplacian is derived by the chain rule in [[§44 Potential Equation#^thm-44-3|Theorem §44.3]]; the chain rule for $v(r, \theta) = u(r\cos\theta, r\sin\theta)$ is [[§110 The Chain Rule#^thm-110-2|Calc Thm. §110.2]], and polar coordinates are [[§75 Polar Coordinates#^thm-75-2|Calc Thm. §75.2]].
> - 452 obtains it differently, from the divergence theorem in any orthogonal coordinates: with scale factors $h_r = 1$, $h_\theta = r$, the formula $\nabla^2v = \frac{1}{h_rh_\theta}\big[\partial_r\big(\frac{h_\theta}{h_r}v_r\big) + \partial_\theta\big(\frac{h_r}{h_\theta}v_\theta\big)\big]$ of [[§33 The Laplacian in Spherical Coordinates#^rem-33-3|452, General Orthogonal Coordinates]] is the second form above. The polar coordinate change itself, with its Jacobian $r$: [[Polar and spherical coordinates]].

Although the interpretation of $v$ differs in the two cases, the solution of

$$
\nabla^2v = 0, \qquad v(a, \theta) = f(\theta)
$$

(periodic, bounded) is the rest state of the membrane, or the steady-state temperature of the plate. It is the potential in a disk, found in [[§48 Potential in a Disk#^thm-48-2|Theorem §48.2]], and it is needed in both problems to make the boundary condition at $r = a$ homogeneous. Suppose it has been found and subtracted, so that $f(\theta)$ is replaced by zero:

$$
\nabla^2v = \frac{1}{c^2}\frac{\partial^2v}{\partial t^2} \quad\text{or}\quad \nabla^2v = \frac{1}{k}\frac{\partial v}{\partial t}, \qquad v(a, \theta, t) = 0 ,
$$

plus the appropriate initial conditions.

## Separation of Variables

> [!theorem] Theorem §54.1: The Eigenvalue Problem for the Disk
> A product $v(r, \theta, t) = \phi(r, \theta)T(t)$, not identically zero, satisfies the wave or heat equation of Definition §54.1, the boundary condition $v(a, \theta, t) = 0$, periodicity and boundedness, if and only if, for some constant $\lambda^2$,
>
> $$
> \begin{aligned}
> &\frac{1}{r}\frac{\partial}{\partial r}\Big(r\frac{\partial\phi}{\partial r}\Big) + \frac{1}{r^2}\frac{\partial^2\phi}{\partial\theta^2} = -\lambda^2\phi, && 0 < r < a, && (1) \\
> &\phi(a, \theta) = 0, && && (2) \\
> &\phi(r, \theta + 2\pi) = \phi(r, \theta), && && (3) \\
> &\phi \text{ bounded as } r \to 0, && && (4)
> \end{aligned}
> $$
>
> and $T$ satisfies
>
> $$
> T'' + \lambda^2c^2T = 0 \quad\text{(wave)}, \qquad\text{or}\qquad T' + \lambda^2kT = 0 \quad\text{(heat)} .
> $$
>
> *Powers: 5.4, Equations (1)–(4); Exercises 5.4.2 and 5.4.3*

^thm-54-1

> [!proof]+ Proof
> (Powers prints condition (3) as $\phi(r, \theta + 2\pi) = \phi(r, \pi)$; it is $\phi(r, \theta)$.)
>
> For the wave equation, substituting $v = \phi T$ and dividing by $\phi T$ gives
>
> $$
> \frac{\nabla^2\phi}{\phi} = \frac{T''}{c^2T} ;
> $$
>
> for the heat equation the right side is $T'/(kT)$. The left side depends only on $(r, \theta)$ and the right side only on $t$, so both equal a constant, written $-\lambda^2$: this gives (1) and the equation for $T$. The boundary condition $\phi(a, \theta)T(t) = 0$ for all $t$ forces $\phi(a, \theta) = 0$ unless $T \equiv 0$; in the same way periodicity and boundedness of $\phi T$ in $(r, \theta)$ are those of $\phi$. The converse is the same computation read backwards.

^pf-54-1

*Uses:* [[§54★ Problems in Polar Coordinates#^def-54-1|Def. §54.1]]

The constant $-\lambda^2$ is indeed negative: see [[§54★ Problems in Polar Coordinates#^rem-54-2|Remark: The Eigenvalues Are Positive]] below. The two-dimensional eigenvalue problem (1)–(4) can be separated again.

> [!theorem] Theorem §54.2: Separation of the Disk Eigenvalue Problem
> A product $\phi(r, \theta) = R(r)Q(\theta)$, not identically zero, solves (1)–(4) if and only if $Q$ is a solution of the periodic eigenvalue problem
>
> $$
> Q'' + \mu^2Q = 0, \qquad Q(\theta + 2\pi) = Q(\theta) , \qquad (9),\ (10)
> $$
>
> whose solutions are
>
> $$
> \mu_0^2 = 0,\quad Q_0(\theta) = 1; \qquad \mu_m^2 = m^2,\quad Q_m(\theta) = \cos(m\theta) \text{ and } \sin(m\theta), \quad m = 1, 2, 3, \ldots , \qquad (11)
> $$
>
> and, with $\mu = m$, $R$ is a solution of the singular problem
>
> $$
> (rR')' - \frac{\mu^2}{r}R + \lambda^2rR = 0, \quad 0 < r < a, \qquad R(a) = 0, \qquad R(r) \text{ bounded as } r \to 0 . \qquad (12)\text{–}(14)
> $$
>
> *Powers: 5.4, Equations (5)–(14)*

^thm-54-2

> [!proof]+ Proof
> **Separation.** (Powers: "after some algebra".) With $\phi = RQ$, (1) reads $\frac{1}{r}(rR')'Q + \frac{1}{r^2}RQ'' = -\lambda^2RQ$, and dividing by $RQ$,
>
> $$
> \frac{(rR')'}{rR} + \frac{Q''}{r^2Q} = -\lambda^2 . \qquad (5)
> $$
>
> The conditions (2)–(4) become $R(a)Q(\theta) = 0$, $R(r)Q(\theta + 2\pi) = R(r)Q(\theta)$ and $RQ$ bounded as $r \to 0$; since neither factor is identically zero, they say $R(a) = 0$ (6), $Q(\theta) = Q(\theta + 2\pi)$ (7) and $R$ bounded as $r \to 0$ (8). Multiplying (5) by $r^2$,
>
> $$
> \frac{r(rR')'}{R} + \lambda^2r^2 = -\frac{Q''}{Q} .
> $$
>
> The left side depends only on $r$ and the right side only on $\theta$, so $Q''/Q$ must be a constant, $-\mu^2$; otherwise $\lambda^2$ could not be constant. This gives (9)–(10), and multiplying $\frac{r(rR')'}{R} + \lambda^2r^2 = \mu^2$ by $R/r$ gives (12).
>
> **The periodic problem** (Powers' Exercise 5.4.4). As Powers notes, (9)–(10) was solved in Chapter 4: it is the $\theta$-problem of the potential in a disk, with $\mu$ in place of $\lambda$. A positive ratio $Q''/Q = s^2$ gives $Q = Ae^{s\theta} + Be^{-s\theta}$, which is periodic only for $A = B = 0$ (shown just before [[§48 Potential in a Disk#^prop-48-1|Proposition §48.1]]); for $-\mu^2 \le 0$ the periodic solutions are exactly (11), by [[§48 Potential in a Disk#^prop-48-1|Proposition §48.1]] (periodicity forces $\cos 2\pi\mu = 1$, so $\mu = m$ is an integer).

^pf-54-2

*Uses:* [[§54★ Problems in Polar Coordinates#^thm-54-1|§54.1]], [[§48 Potential in a Disk#^prop-48-1|§48.1]] (the periodic problem)

Equation (12) is **Bessel's equation** ([[§55★ Bessel's Equation#^def-55-1|Definition §55.1]]). Its bounded solutions are the Bessel functions $J_m(\lambda r)$ ([[§55★ Bessel's Equation#^thm-55-5|Theorem §55.5]]), and $R(a) = 0$ becomes $J_m(\lambda a) = 0$, which determines the eigenvalues $\lambda$ through the zeros of $J_m$. The problem is singular: the coefficient $\mu^2/r$ blows up at $r = 0$, where the boundedness condition replaces a boundary condition ([[§6★ Singular Boundary Value Problems#^def-6-2|Definition §6.2]]).

> [!remark] Remark: Method — Heat and Wave Problems in a Disk
> 1. **Steady state.** Solve the potential problem $\nabla^2v_\infty = 0$, $v_\infty(a, \theta) = f(\theta)$, periodic and bounded ([[§48 Potential in a Disk#^thm-48-2|Theorem §48.2]]), and subtract it, which makes the boundary condition homogeneous.
> 2. **Separate time**, $v = \phi(r, \theta)T(t)$: the eigenvalue problem (1)–(4) and $T'' + \lambda^2c^2T = 0$ or $T' + \lambda^2kT = 0$ (Theorem §54.1).
> 3. **Separate space**, $\phi = R(r)Q(\theta)$: $Q = 1$, $\cos m\theta$, $\sin m\theta$ with $\mu = m$ (Theorem §54.2).
> 4. **Radial problem.** For each $m$, the bounded solutions of Bessel's equation (12) are $R = J_m(\lambda r)$; the boundary condition picks out the eigenvalues, $\lambda a =$ a zero of $J_m$ (or of $J_m'$ for an insulated edge).
> 5. **Superpose** over $m$ and over the zeros, and find the coefficients from the initial conditions by orthogonality (Theorem §54.3); this is carried out for radially symmetric problems in [[§57★ Temperature in a Cylinder|§46]] and for the drum in [[§58★ Vibrations of a Circular Membrane|§47]].

^rem-54-1

## Examples

> [!example] Example §54.1: Subtracting the Steady State
> State the problems that result from the problems of Definition §54.1 when the steady-state solution is subtracted from $v$, and find them explicitly for the boundary temperature $f(\theta) = \cos\theta$.
>
> Let $v_\infty(r, \theta)$ solve $\nabla^2v_\infty = 0$ in $0 < r < a$, $v_\infty(a, \theta) = f(\theta)$, periodic in $\theta$ and bounded as $r \to 0$, and put $w = v - v_\infty$. Since $v_\infty$ does not depend on $t$ and $\nabla^2v_\infty = 0$, we have $\nabla^2w = \nabla^2v$, $w_t = v_t$ and $w_{tt} = v_{tt}$, and $w(a, \theta, t) = f(\theta) - f(\theta) = 0$. So
>
> | | Wave | Heat |
> |---|---|---|
> | equation | $\nabla^2w = \dfrac{1}{c^2}\dfrac{\partial^2w}{\partial t^2}$ | $\nabla^2w = \dfrac{1}{k}\dfrac{\partial w}{\partial t}$ |
> | boundary condition | $w(a, \theta, t) = 0$ | $w(a, \theta, t) = 0$ |
> | initial conditions | $w(r, \theta, 0) = g(r, \theta) - v_\infty(r, \theta)$, $\ \dfrac{\partial w}{\partial t}(r, \theta, 0) = h(r, \theta)$ | $w(r, \theta, 0) = g(r, \theta) - v_\infty(r, \theta)$ |
>
> with $w$ periodic in $\theta$ and bounded as $r \to 0$. The initial velocity is unchanged, because $v_\infty$ does not move. For a membrane, $v_\infty$ is the shape the membrane takes at rest when its frame is warped to the height $f(\theta)$, and $w$ is the vibration about that shape.
>
> For $f(\theta) = \cos\theta$, the potential in a disk ([[§48 Potential in a Disk#^thm-48-2|Theorem §48.2]], whose series has the single term $n = 1$) is $v_\infty = (r/a)\cos\theta$: it is harmonic, since $\frac{1}{r}\big(r\cdot\frac{\cos\theta}{a}\big)_r - \frac{1}{r^2}\cdot\frac{r\cos\theta}{a} = \frac{\cos\theta}{ra} - \frac{\cos\theta}{ra} = 0$, bounded, periodic, and equal to $\cos\theta$ at $r = a$. The transient problem has initial condition $w(r, \theta, 0) = g(r, \theta) - (r/a)\cos\theta$.
>
> *Powers: 5.4 (text); Exercise 5.4.1*

^ex-54-1

> [!example] Example §54.2: A Half-Disk
> Suppose the problems are to be solved in the half-disk $0 < r < a$, $0 < \theta < \pi$, with the additional conditions
>
> $$
> v(r, 0, t) = 0, \quad v(r, \pi, t) = 0, \qquad 0 < r < a, \quad 0 < t .
> $$
>
> What eigenvalue problem arises in place of (9)–(11)?
>
> The straight edges $\theta = 0$ and $\theta = \pi$ are now real boundaries, and $\theta$ no longer runs around a full circle, so periodicity is replaced by the boundary conditions. With $v = R(r)Q(\theta)T(t)$ they become $Q(0) = 0$, $Q(\pi) = 0$, and the separation of Theorem §54.2 gives
>
> $$
> Q'' + \mu^2Q = 0, \quad 0 < \theta < \pi, \qquad Q(0) = 0, \quad Q(\pi) = 0 .
> $$
>
> This is the fixed-end problem of [[§25 Example꞉ Fixed End Temperatures#^thm-25-2|Theorem §25.2]] on an interval of length $\pi$: $\mu_m = m$, $Q_m(\theta) = \sin(m\theta)$, $m = 1, 2, 3, \ldots$. Compared with (11), the cosines and the constant $Q_0 = 1$ are gone. The radial problem is still Bessel's equation (12) with $\mu = m$, now only for $m \ge 1$.
>
> *Powers: Exercise 5.4.5*

^ex-54-2

> [!example] Example §54.3: An Insulated Edge
> Suppose the boundary condition $v(a, \theta, t) = f(\theta)$ is replaced by
>
> $$
> \frac{\partial v}{\partial r}(a, \theta, t) = 0, \qquad -\pi < \theta \le \pi, \quad 0 < t .
> $$
>
> Carry out the separation of variables and find what changes.
>
> The equation, periodicity and boundedness are unchanged, so Theorem §54.1 and Theorem §54.2 go through word for word except for the boundary condition. With $v = R(r)Q(\theta)T(t)$, the new condition reads $R'(a)Q(\theta)T(t) = 0$ for all $\theta$ and $t$, which forces
>
> $$
> R'(a) = 0
> $$
>
> in place of (6) and (13). Everything else, the $\theta$-problem (9)–(11) and Bessel's equation (12), is the same. One new feature appears: $\lambda = 0$, $\mu = 0$ is now allowed, since $R = 1$ satisfies $(rR')' = 0$ and $R'(a) = 0$. For heat this constant mode does not decay: an insulated plate tends to its mean initial temperature. The radial eigenvalues are worked out for $\mu = 0$ in [[§56★ Properties of Bessel Functions#^ex-56-2|Example §56.2]].
>
> *Powers: Exercise 5.4.6*

^ex-54-3

## Orthogonality of the Eigenfunctions

> [!theorem] Theorem §54.3: Eigenfunctions of the Laplacian Are Orthogonal
> Let $\mathcal{R}$ be a region in the plane bounded by the closed curve $\mathcal{C}$. If $\phi_k$ and $\phi_m$ are eigenfunctions of the problem
>
> $$
> \nabla^2\phi = -\lambda^2\phi \quad\text{in } \mathcal{R}, \qquad \phi = 0 \quad\text{on } \mathcal{C} ,
> $$
>
> corresponding to different eigenvalues $\lambda_k^2 \ne \lambda_m^2$, then
>
> $$
> \iint_{\mathcal{R}} \phi_k\,\phi_m\,dA = 0 .
> $$
>
> The same holds with the boundary condition $\phi + \beta\,\dfrac{\partial\phi}{\partial n} = 0$ on $\mathcal{C}$, $\beta$ a constant.
>
> *Powers: Exercises 5.4.7 and 5.4.8*

^thm-54-3

> [!proof]+ Proof
> (Powers writes the constant in the second boundary condition as $\lambda$; it is renamed $\beta$ here, since it has nothing to do with the eigenvalue.)
>
> One of the consequences of Green's theorem is the integral relation
>
> $$
> \iint_{\mathcal{R}} \big(f\nabla^2g - g\nabla^2f\big)\,dA = \oint_{\mathcal{C}} \Big(f\frac{\partial g}{\partial n} - g\frac{\partial f}{\partial n}\Big)ds ,
> $$
>
> where $\partial f/\partial n$ is the directional derivative in the direction normal to $\mathcal{C}$, valid for $f$, $g$ twice continuously differentiable up to $\mathcal{C}$ (as the eigenfunctions are assumed to be). Take $f = \phi_k$ and $g = \phi_m$. On the left, $\nabla^2\phi_m = -\lambda_m^2\phi_m$ and $\nabla^2\phi_k = -\lambda_k^2\phi_k$, so the integrand is $(\lambda_k^2 - \lambda_m^2)\phi_k\phi_m$.
>
> **Dirichlet condition.** On $\mathcal{C}$, $\phi_k = \phi_m = 0$, so the boundary integrand is $0$.
>
> **The condition $\phi + \beta\,\partial\phi/\partial n = 0$.** If $\beta = 0$ this is the Dirichlet condition. If $\beta \ne 0$, then $\partial\phi/\partial n = -\phi/\beta$ on $\mathcal{C}$ for both eigenfunctions, and
>
> $$
> \phi_k\frac{\partial\phi_m}{\partial n} - \phi_m\frac{\partial\phi_k}{\partial n} = -\frac{\phi_k\phi_m}{\beta} + \frac{\phi_m\phi_k}{\beta} = 0 .
> $$
>
> In both cases $(\lambda_k^2 - \lambda_m^2)\iint_{\mathcal{R}} \phi_k\phi_m\,dA = 0$, and since $\lambda_k^2 \ne \lambda_m^2$ the integral is $0$.

^pf-54-3

*Uses:* [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-3|452 Thm. §28.3]] (Green's second identity), [[§132 Curl and Divergence#^thm-132-5|Calc Thm. §132.5]] (Green's theorem, normal form)

> [!remark]- Connections
> - Green's second identity $\int_D (u\Delta v - v\Delta u) = \int_{\partial D}(u\,\partial_nv - v\,\partial_nu)$ is [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-3|452 Thm. §28.3]], proved there from the divergence theorem; it says that $\nabla^2$ is a symmetric operator on functions satisfying these boundary conditions, and the proof above is then the argument of [[§23 Self-Adjoint and Normal Operators#^ladr-7-22|LADR 7.22]] (eigenvectors of a self-adjoint operator for distinct eigenvalues are orthogonal).
> - The one-dimensional version is the orthogonality of Sturm–Liouville eigenfunctions, [[§29 Sturm–Liouville Problems#^thm-29-2|Theorem §29.2]] (Powers 2.7). For the rectangle the theorem gives (16) of [[§53 Two-Dimensional Heat Equation꞉ Solution#^thm-53-3|Theorem §53.3]] without computing integrals whenever the two eigenvalues differ; for the circular membrane it gives the orthogonality of modes with different frequencies in [[§58★ Vibrations of a Circular Membrane#^prop-58-3|Proposition §58.3]]. Eigenfunctions with the same eigenvalue (a square's $\phi_{12}$ and $\phi_{21}$, or $J_m(\lambda r)\cos m\theta$ and $J_m(\lambda r)\sin m\theta$) are not covered and need the direct computation.

> [!remark] Remark: The Eigenvalues Are Positive
> For the Dirichlet problem every eigenvalue $\lambda^2$ is positive, which justifies writing the separation constant as $-\lambda^2$. Green's first identity, $\iint_{\mathcal{R}} \big(\phi\nabla^2\phi + |\nabla\phi|^2\big)\,dA = \oint_{\mathcal{C}} \phi\,\frac{\partial\phi}{\partial n}\,ds$ ([[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-2|452 Thm. §28.2]] with $u = v = \phi$), with $\phi = 0$ on $\mathcal{C}$ and $\nabla^2\phi = -\lambda^2\phi$, gives
>
> $$
> \lambda^2 = \frac{\iint_{\mathcal{R}} |\nabla\phi|^2\,dA}{\iint_{\mathcal{R}} \phi^2\,dA} > 0 ,
> $$
>
> because $\nabla\phi \equiv 0$ would make $\phi$ constant, hence $0$ by the boundary condition. For the rectangle this is Powers' Exercise 5.3.9, proved one variable at a time in [[§53 Two-Dimensional Heat Equation꞉ Solution#^thm-53-2|Theorem §53.2]]. With an insulated boundary ($\partial\phi/\partial n = 0$) the same identity gives $\lambda^2 \ge 0$, with $\lambda = 0$ exactly for the constants, as in Example §54.3.
>
> *Source: a standard consequence of Green's first identity; not in Powers.*

^rem-54-2
