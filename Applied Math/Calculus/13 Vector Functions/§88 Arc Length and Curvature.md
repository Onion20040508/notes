---
type: section
subject: "[[Calculus]]"
chapter: 13
section: 88
stewart: "13.3"
aliases: ["Stewart 13.3"]
tags: [calculus, math233]
---
← [[§87 Derivatives and Integrals of Vector Functions]] · ↑ [[· 13 Vector Functions]] · [[§89 Motion in Space꞉ Velocity and Acceleration]] →

*Stewart, Section 13.3 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q15, Q16), Practice Exam 1 (Q3(b)), Exam 1 Review (Q12, Q14), SI Midterm 1 Problem Set (Q4(b)).*

This section measures the geometry of a space curve: how long it is, how sharply it bends, and how it twists out of a plane. The length is $\int_a^b |\mathbf{r}'(t)|\,dt$, and the arc length function $s(t)$ allows a curve to be reparametrized by arc length, a parametrization that depends only on the curve. Curvature is the rate at which the unit tangent vector turns per unit of arc length; three formulas compute it in practice. The unit normal $\mathbf{N}$ and binormal $\mathbf{B}$ complete $\mathbf{T}$ to a moving orthonormal frame, which gives the normal and osculating planes and the osculating circle, and torsion measures how fast the osculating plane turns. Curvature and $\mathbf{N}$ reappear in [[§89 Motion in Space꞉ Velocity and Acceleration|§89]], where they split acceleration into tangential and normal parts.

## Arc Length

> [!definition] Definition §88.1: Length of a Space Curve
> The **length** of a space curve is the limit of the lengths of inscribed polygonal paths, as the number of vertices increases and the distances between consecutive vertices go to $0$, exactly as for plane curves ([[§52 Arc Length#^def-52-1|Definition §52.1]], [[§64 Calculus with Parametric Curves#^thm-64-4|Theorem §64.4]]).
>
> *Stewart: 13.3 (text)*

^def-88-1

> [!theorem] Theorem §88.1: Arc Length Formula
> Suppose a curve has vector equation $\mathbf{r}(t) = \langle f(t), g(t), h(t) \rangle$, $a \le t \le b$, where $f'$, $g'$, $h'$ are continuous, and the curve is traversed exactly once as $t$ increases from $a$ to $b$. Then its length is
>
> $$
> L = \int_a^b \sqrt{[f'(t)]^2 + [g'(t)]^2 + [h'(t)]^2}\,dt = \int_a^b \sqrt{\Big(\frac{dx}{dt}\Big)^2 + \Big(\frac{dy}{dt}\Big)^2 + \Big(\frac{dz}{dt}\Big)^2}\,dt ,
> $$
>
> or more compactly, for plane and space curves alike,
>
> $$
> L = \int_a^b |\mathbf{r}'(t)|\,dt .
> $$
>
> *Stewart: 13.3, Equations 2 and 3*

^thm-88-1

*Stewart omits the proof ("it can be shown"). The proof of the plane case, [[§64 Calculus with Parametric Curves#^thm-64-4|Theorem §64.4]], carries over word for word with a third component (the Mean Value Theorem applied to $h$ as well); the same derivation appears in 452 with [[§16 Line Integrals and Green's Theorem#^def-16-1|452 Def. §16.1]].*

> [!remark]- Connections
> - In 452 the arc length element $|\mathbf{r}'(t)|\,dt$ is the weight in the scalar line integral, [[§16 Line Integrals and Green's Theorem#^def-16-1|452 Def. §16.1]], and its two-dimensional analog is the area element $|\mathbf{X}_u \times \mathbf{X}_v|\,du\,dv$ of [[§18 Surface Integrals#^thm-18-1|452 Thm. §18.1]].
> - Complex-variables version: [[§43 Contours#^def-43-new3|342 Def. §43.6]] (the length of a contour, $\int_a^b |z'(t)|\,dt$).

> [!remark] Remark: Why It Works
> Divide $[a, b]$ by $a = t_0 < t_1 < \cdots < t_n = b$ and join the points $\mathbf{r}(t_0), \ldots, \mathbf{r}(t_n)$ by segments. The $i$-th segment has length
>
> $$
> |\mathbf{r}(t_i) - \mathbf{r}(t_{i-1})| = \sqrt{[f(t_i) - f(t_{i-1})]^2 + [g(t_i) - g(t_{i-1})]^2 + [h(t_i) - h(t_{i-1})]^2} .
> $$
>
> By the Mean Value Theorem ([[§26 The Mean Value Theorem#^thm-26-2|Theorem §26.2]]), $f(t_i) - f(t_{i-1}) = f'(t_i^*)\,\Delta t_i$ for some $t_i^*$ in the subinterval, and similarly for $g$ and $h$ (at possibly different points). So the polygon has length
>
> $$
> \sum_{i=1}^n \sqrt{f'(t_i^*)^2 + g'(t_i^{**})^2 + h'(t_i^{***})^2}\,\Delta t_i ,
> $$
>
> which is almost a Riemann sum for $\int_a^b |\mathbf{r}'(t)|\,dt$. Because $f'$, $g'$, $h'$ are continuous, the three different sample points make no difference in the limit (the estimate is in the proof of [[§64 Calculus with Parametric Curves#^thm-64-4|Theorem §64.4]]), and the polygon lengths tend to the integral. In the plane case, the formula is $L = \int_a^b \sqrt{[f'(t)]^2 + [g'(t)]^2}\,dt$, since $|\mathbf{r}'(t)| = |f'(t)\,\mathbf{i} + g'(t)\,\mathbf{j}|$. In [[§89 Motion in Space꞉ Velocity and Acceleration#^prop-89-1|Proposition §89.1]] $|\mathbf{r}'(t)|$ is the speed, so the formula says: to compute distance traveled, integrate speed.

^rem-88-1

> [!example] Example §88.1: Lengths of Helices and Other Curves
> **(a)** Find the length of the arc of the circular helix $\mathbf{r}(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} + t\,\mathbf{k}$ from $(1, 0, 0)$ to $(1, 0, 2\pi)$.
>
> Since $\mathbf{r}'(t) = -\sin t\,\mathbf{i} + \cos t\,\mathbf{j} + \mathbf{k}$, we have $|\mathbf{r}'(t)| = \sqrt{\sin^2 t + \cos^2 t + 1} = \sqrt2$. The arc is described by $0 \le t \le 2\pi$, so by [[§88 Arc Length and Curvature#^thm-88-1|Theorem §88.1]]
>
> $$
> L = \int_0^{2\pi} |\mathbf{r}'(t)|\,dt = \int_0^{2\pi} \sqrt2\,dt = 2\sqrt2\,\pi .
> $$
>
> **(b)** For $\mathbf{r}(t) = \cos(2t)\,\mathbf{i} + \sin(2t)\,\mathbf{j} + t\,\mathbf{k}$, $0 \le t \le 5$: $\mathbf{r}'(t) = \langle -2\sin 2t, 2\cos 2t, 1 \rangle$ and $|\mathbf{r}'(t)| = \sqrt{4 + 1} = \sqrt5$, so $L = \int_0^5 \sqrt5\,dt = 5\sqrt5$.
>
> **(c)** For $\mathbf{r}(t) = \langle 2t^{3/2}, \cos 2t, \sin 2t \rangle$, $0 \le t \le 1$: $\mathbf{r}'(t) = \langle 3t^{1/2}, -2\sin 2t, 2\cos 2t \rangle$ and $|\mathbf{r}'(t)| = \sqrt{9t + 4}$, so
>
> $$
> L = \int_0^1 \sqrt{9t + 4}\,dt = \Big[\frac{2}{27}(9t + 4)^{3/2}\Big]_0^1 = \frac{2}{27}\big(13^{3/2} - 8\big) .
> $$
>
> *Stewart: Example 13.3.1*
> *Source: 233 Midterm 1 Practice Questions, Q15; 233 Exam 1 Review, Q12*

^ex-88-1

> [!example] Example §88.2: A Perfect Square Under the Root
> A particle moves with position $\mathbf{r}(t) = \langle t^2, t\sqrt2, \tfrac12\ln t \rangle$, $t > 0$. Find the distance it travels from $t = 1$ to $t = e$.
>
> Here $\mathbf{r}'(t) = \big\langle 2t, \sqrt2, \frac{1}{2t} \big\rangle$, and the expression under the root is a perfect square:
>
> $$
> |\mathbf{r}'(t)|^2 = 4t^2 + 2 + \frac{1}{4t^2} = \Big(2t + \frac{1}{2t}\Big)^2 .
> $$
>
> Since $2t + \frac{1}{2t} > 0$ for $t > 0$, $|\mathbf{r}'(t)| = 2t + \frac{1}{2t}$, and
>
> $$
> L = \int_1^e \Big(2t + \frac{1}{2t}\Big)\,dt = \Big[t^2 + \frac12\ln t\Big]_1^e = \Big(e^2 + \frac12\Big) - (1 + 0) = e^2 - \frac12 .
> $$
>
> The same thing happens for $\mathbf{r}(t) = \langle t^2, -t^2, \frac12 t^2 \rangle$, $1 \le t \le 4$: $|\mathbf{r}'(t)| = \sqrt{4t^2 + 4t^2 + t^2} = 3t$, and $L = \int_1^4 3t\,dt = \frac32(16 - 1) = \frac{45}{2}$. Exam problems on arc length are almost always built so that the square root simplifies.
>
> *Source: 233 Practice Exam 1, Q3(b); 233 SI Midterm 1 Problem Set, Q4(b)*

^ex-88-2

> [!remark] Remark: Arc Length Does Not Depend on the Parametrization
> A single curve $C$ can be represented by more than one vector function, each called a **parametrization** of $C$. For instance, the twisted cubic $\mathbf{r}_1(t) = \langle t, t^2, t^3 \rangle$, $1 \le t \le 2$, is also given by $\mathbf{r}_2(u) = \langle e^u, e^{2u}, e^{3u} \rangle$, $0 \le u \le \ln 2$, where $t = e^u$. Arc length is a geometric property of the curve, so [[§88 Arc Length and Curvature#^thm-88-1|Theorem §88.1]] gives the same answer for either parametrization. Indeed, if $t = \phi(u)$ with $\phi$ increasing, then $\mathbf{r}_2(u) = \mathbf{r}_1(\phi(u))$ and $|\mathbf{r}_2'(u)| = |\mathbf{r}_1'(\phi(u))|\,\phi'(u)$ by the Chain Rule ([[§87 Derivatives and Integrals of Vector Functions#^thm-87-2|Theorem §87.2]], Formula 6), so the substitution $t = \phi(u)$ ([[§38 The Substitution Rule#^thm-38-3|Theorem §38.3]]) turns $\int |\mathbf{r}_2'(u)|\,du$ into $\int |\mathbf{r}_1'(t)|\,dt$ over the corresponding interval.

^rem-88-2

## The Arc Length Function

> [!definition] Definition §88.2: Arc Length Function
> Let $C$ be given by $\mathbf{r}(t) = f(t)\,\mathbf{i} + g(t)\,\mathbf{j} + h(t)\,\mathbf{k}$, $a \le t \le b$, where $\mathbf{r}'$ is continuous and $C$ is traversed exactly once as $t$ increases from $a$ to $b$. Its **arc length function** is
>
> $$
> s(t) = \int_a^t |\mathbf{r}'(u)|\,du = \int_a^t \sqrt{\Big(\frac{dx}{du}\Big)^2 + \Big(\frac{dy}{du}\Big)^2 + \Big(\frac{dz}{du}\Big)^2}\,du ,
> $$
>
> the length of the part of $C$ between $\mathbf{r}(a)$ and $\mathbf{r}(t)$. If we can solve $s = s(t)$ for $t$ as a function of $s$, then $\mathbf{r}(t(s))$ is the **parametrization of $C$ with respect to arc length** (measured from $\mathbf{r}(a)$ in the direction of increasing $t$): $\mathbf{r}(t(3))$, for instance, is the point $3$ units of length along the curve from its starting point.
>
> *Stewart: 13.3, Equation 6*

^def-88-2

> [!theorem] Proposition §88.2: Derivative of Arc Length
> $$
> \frac{ds}{dt} = |\mathbf{r}'(t)| .
> $$
>
> *Stewart: 13.3, Equation 7*

^prop-88-2

> [!proof]+ Proof
> The integrand $|\mathbf{r}'(u)|$ of [[§88 Arc Length and Curvature#^def-88-2|Definition §88.2]] is continuous, because $\mathbf{r}'$ is. So Part 1 of the Fundamental Theorem of Calculus ([[§36 The Fundamental Theorem of Calculus#^thm-36-1|Theorem §36.1]]) gives $s'(t) = |\mathbf{r}'(t)|$.

^pf-88-2

*Uses:* [[§88 Arc Length and Curvature#^def-88-2|Def. §88.2]], [[§36 The Fundamental Theorem of Calculus#^thm-36-1|§36.1]]

> [!remark] Remark: Method — Reparametrizing by Arc Length
> 1. Compute $|\mathbf{r}'(t)|$ and the arc length function $s(t) = \int_a^t |\mathbf{r}'(u)|\,du$, where $t = a$ is the given starting point.
> 2. Solve $s = s(t)$ for $t = t(s)$.
> 3. Substitute: $\mathbf{r}(t(s))$. Check that $|d\mathbf{r}/ds| = 1$: a curve parametrized by arc length moves at unit speed.

^rem-88-3

> [!example] Example §88.3: Reparametrizing by Arc Length
> **(a)** Reparametrize the helix $\mathbf{r}(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} + t\,\mathbf{k}$ with respect to arc length measured from $(1, 0, 0)$ in the direction of increasing $t$.
>
> The starting point corresponds to $t = 0$. From [[§88 Arc Length and Curvature#^ex-88-1|Example §88.1]], $ds/dt = |\mathbf{r}'(t)| = \sqrt2$, so $s = s(t) = \int_0^t \sqrt2\,du = \sqrt2\,t$. Therefore $t = s/\sqrt2$ and
>
> $$
> \mathbf{r}(t(s)) = \cos\big(s/\sqrt2\big)\,\mathbf{i} + \sin\big(s/\sqrt2\big)\,\mathbf{j} + \big(s/\sqrt2\big)\,\mathbf{k} .
> $$
>
> **(b)** Reparametrize $\mathbf{r}(t) = e^t\,\mathbf{i} + e^t\sin t\,\mathbf{j} + e^t\cos t\,\mathbf{k}$ with respect to arc length from $(1, 0, 1)$ in the direction of increasing $t$.
>
> The point $(1, 0, 1)$ is $\mathbf{r}(0)$. By the Product Rule,
>
> $$
> \mathbf{r}'(t) = \big\langle e^t,\ e^t(\sin t + \cos t),\ e^t(\cos t - \sin t) \big\rangle ,
> $$
>
> and since $(\sin t + \cos t)^2 + (\cos t - \sin t)^2 = 2$, $|\mathbf{r}'(t)| = e^t\sqrt{1 + 2} = \sqrt3\,e^t$. So $s(t) = \int_0^t \sqrt3\,e^u\,du = \sqrt3\,(e^t - 1)$, which gives $e^t = 1 + s/\sqrt3$ and $t = \ln(1 + s/\sqrt3)$. Substituting,
>
> $$
> \mathbf{r}(t(s)) = \Big(1 + \frac{s}{\sqrt3}\Big)\Big\langle 1,\ \sin\ln\Big(1 + \frac{s}{\sqrt3}\Big),\ \cos\ln\Big(1 + \frac{s}{\sqrt3}\Big) \Big\rangle, \qquad s > -\sqrt3 .
> $$
>
> **(c)** Find the arc length function (from $t = 0$) for $\mathbf{r}(t) = e^{2t}\cos 2t\,\mathbf{i} + 2\,\mathbf{j} + e^{2t}\sin 2t\,\mathbf{k}$. Here
>
> $$
> \mathbf{r}'(t) = \big\langle 2e^{2t}(\cos 2t - \sin 2t),\ 0,\ 2e^{2t}(\sin 2t + \cos 2t) \big\rangle, \qquad |\mathbf{r}'(t)| = 2e^{2t}\sqrt2 = 2\sqrt2\,e^{2t} ,
> $$
>
> so $s(t) = \int_0^t 2\sqrt2\,e^{2u}\,du = \sqrt2\,(e^{2t} - 1)$.
>
> *The posted answer, $2\sqrt2\,e^{2t}$, is the speed $ds/dt$; the arc length function measured from $t = 0$ is its integral, $\sqrt2\,(e^{2t} - 1)$.*
>
> *Stewart: Example 13.3.2*
> *Source: 233 Exam 1 Review, Q14; 233 Midterm 1 Practice Questions, Q16*

^ex-88-3

## Curvature

> [!definition] Definition §88.3: Smooth Parametrization and Smooth Curve
> A parametrization $\mathbf{r}(t)$ is **smooth** on an interval $I$ if $\mathbf{r}'$ is continuous and $\mathbf{r}'(t) \ne \mathbf{0}$ on $I$. A curve is **smooth** if it has a smooth parametrization. A smooth curve has no sharp corner or cusp: when its tangent vector turns, it does so continuously.
>
> *Stewart: 13.3 (text)*

^def-88-3

> [!definition] Definition §88.4: Curvature
> Let $C$ be a smooth curve with unit tangent vector $\mathbf{T} = \mathbf{r}'/|\mathbf{r}'|$ ([[§87 Derivatives and Integrals of Vector Functions#^def-87-new2|Definition §87.4]]). The **curvature** of $C$ is
>
> $$
> \kappa = \left| \frac{d\mathbf{T}}{ds} \right| ,
> $$
>
> the magnitude of the rate of change of the unit tangent vector with respect to arc length.
>
> *Stewart: 13.3, Definition 8*

^def-88-4

> [!remark] Remark: What Curvature Measures
> $\mathbf{T}(t)$ changes direction slowly where $C$ is fairly straight and quickly where $C$ bends or twists sharply. Since $\mathbf{T}$ has constant length, only changes in its direction contribute to $d\mathbf{T}/ds$. Arc length, rather than $t$, is used so that the curvature does not depend on the parametrization. A straight line has curvature $0$, since its tangent vector is constant.

^rem-88-4

> [!theorem] Proposition §88.3: Curvature in Terms of t
> $$
> \kappa(t) = \frac{|\mathbf{T}'(t)|}{|\mathbf{r}'(t)|} .
> $$
>
> *Stewart: 13.3, Equation 9*

^prop-88-3

> [!proof]+ Proof
> By the Chain Rule ([[§87 Derivatives and Integrals of Vector Functions#^thm-87-2|Theorem §87.2]], Formula 6), $\dfrac{d\mathbf{T}}{dt} = \dfrac{d\mathbf{T}}{ds}\dfrac{ds}{dt}$. Since $ds/dt = |\mathbf{r}'(t)| > 0$ for a smooth parametrization ([[§88 Arc Length and Curvature#^prop-88-2|Proposition §88.2]]),
>
> $$
> \kappa = \left| \frac{d\mathbf{T}}{ds} \right| = \left| \frac{d\mathbf{T}/dt}{ds/dt} \right| = \frac{|\mathbf{T}'(t)|}{|\mathbf{r}'(t)|} .
> $$

^pf-88-3

*Uses:* [[§88 Arc Length and Curvature#^def-88-4|Def. §88.4]], [[§88 Arc Length and Curvature#^prop-88-2|§88.2]], [[§87 Derivatives and Integrals of Vector Functions#^thm-87-2|§87.2]]

> [!theorem] Theorem §88.4: Curvature from r′ and r″
> The curvature of the curve given by the vector function $\mathbf{r}$ is
>
> $$
> \kappa(t) = \frac{|\mathbf{r}'(t) \times \mathbf{r}''(t)|}{|\mathbf{r}'(t)|^3} .
> $$
>
> *Stewart: 13.3, Theorem 10*

^thm-88-4

> [!proof]+ Proof
> Since $\mathbf{T} = \mathbf{r}'/|\mathbf{r}'|$ and $|\mathbf{r}'| = ds/dt$,
>
> $$
> \mathbf{r}' = |\mathbf{r}'|\,\mathbf{T} = \frac{ds}{dt}\,\mathbf{T} ,
> $$
>
> so the Product Rule ([[§87 Derivatives and Integrals of Vector Functions#^thm-87-2|Theorem §87.2]], Formula 3) gives
>
> $$
> \mathbf{r}'' = \frac{d^2s}{dt^2}\,\mathbf{T} + \frac{ds}{dt}\,\mathbf{T}' .
> $$
>
> Since $\mathbf{T} \times \mathbf{T} = \mathbf{0}$ ([[§83 The Cross Product#^ex-83-1|Example §83.1]](b)), the properties of the cross product ([[§83 The Cross Product#^thm-83-8|Theorem §83.8]]) give
>
> $$
> \mathbf{r}' \times \mathbf{r}'' = \frac{ds}{dt}\frac{d^2s}{dt^2}(\mathbf{T} \times \mathbf{T}) + \Big(\frac{ds}{dt}\Big)^2(\mathbf{T} \times \mathbf{T}') = \Big(\frac{ds}{dt}\Big)^2(\mathbf{T} \times \mathbf{T}') .
> $$
>
> Now $|\mathbf{T}(t)| = 1$ for all $t$, so $\mathbf{T}$ and $\mathbf{T}'$ are orthogonal ([[§87 Derivatives and Integrals of Vector Functions#^thm-87-3|Theorem §87.3]]), and by [[§83 The Cross Product#^thm-83-4|Theorem §83.4]] with $\theta = \pi/2$,
>
> $$
> |\mathbf{r}' \times \mathbf{r}''| = \Big(\frac{ds}{dt}\Big)^2 |\mathbf{T}|\,|\mathbf{T}'| = \Big(\frac{ds}{dt}\Big)^2 |\mathbf{T}'| .
> $$
>
> (If $\mathbf{T}' = \mathbf{0}$ both sides are $0$.) Thus $|\mathbf{T}'| = |\mathbf{r}' \times \mathbf{r}''|/(ds/dt)^2 = |\mathbf{r}' \times \mathbf{r}''|/|\mathbf{r}'|^2$, and by [[§88 Arc Length and Curvature#^prop-88-3|Proposition §88.3]]
>
> $$
> \kappa = \frac{|\mathbf{T}'|}{|\mathbf{r}'|} = \frac{|\mathbf{r}' \times \mathbf{r}''|}{|\mathbf{r}'|^3} .
> $$

^pf-88-4

*Uses:* [[§88 Arc Length and Curvature#^prop-88-3|§88.3]], [[§88 Arc Length and Curvature#^prop-88-2|§88.2]], [[§87 Derivatives and Integrals of Vector Functions#^thm-87-2|§87.2]], [[§87 Derivatives and Integrals of Vector Functions#^thm-87-3|§87.3]], [[§83 The Cross Product#^thm-83-4|§83.4]], [[§83 The Cross Product#^thm-83-8|§83.8]], [[§83 The Cross Product#^ex-83-1|Ex. §83.1]] ($\mathbf{T} \times \mathbf{T} = \mathbf{0}$)

> [!theorem] Corollary §88.5: Curvature of a Plane Curve y = f(x)
> The curvature of the plane curve $y = f(x)$ is
>
> $$
> \kappa(x) = \frac{|f''(x)|}{\big[1 + (f'(x))^2\big]^{3/2}} .
> $$
>
> *Stewart: 13.3, Equation 11*

^cor-88-5

> [!proof]+ Proof
> Take $x$ as the parameter: $\mathbf{r}(x) = x\,\mathbf{i} + f(x)\,\mathbf{j}$, regarded as a space curve with zero $\mathbf{k}$-component. Then $\mathbf{r}'(x) = \mathbf{i} + f'(x)\,\mathbf{j}$ and $\mathbf{r}''(x) = f''(x)\,\mathbf{j}$. Since $\mathbf{i} \times \mathbf{j} = \mathbf{k}$ and $\mathbf{j} \times \mathbf{j} = \mathbf{0}$ ([[§83 The Cross Product#^prop-83-7|Proposition §83.7]]), $\mathbf{r}'(x) \times \mathbf{r}''(x) = f''(x)\,\mathbf{k}$. Also $|\mathbf{r}'(x)| = \sqrt{1 + [f'(x)]^2}$. [[§88 Arc Length and Curvature#^thm-88-4|Theorem §88.4]] gives the formula.

^pf-88-5

*Uses:* [[§88 Arc Length and Curvature#^thm-88-4|§88.4]], [[§83 The Cross Product#^prop-83-7|§83.7]]

> [!example] Example §88.4: Curvature by the Three Formulas
> **(a)** *Circle, by [[§88 Arc Length and Curvature#^prop-88-3|Proposition §88.3]].* The circle of radius $a$ about the origin is $\mathbf{r}(t) = a\cos t\,\mathbf{i} + a\sin t\,\mathbf{j}$. Then $\mathbf{r}'(t) = -a\sin t\,\mathbf{i} + a\cos t\,\mathbf{j}$, $|\mathbf{r}'(t)| = a$, $\mathbf{T}(t) = -\sin t\,\mathbf{i} + \cos t\,\mathbf{j}$ and $\mathbf{T}'(t) = -\cos t\,\mathbf{i} - \sin t\,\mathbf{j}$, so $|\mathbf{T}'(t)| = 1$ and $\kappa(t) = 1/a$. Small circles have large curvature and large circles small curvature, as they should.
>
> **(b)** *Twisted cubic, by [[§88 Arc Length and Curvature#^thm-88-4|Theorem §88.4]].* For $\mathbf{r}(t) = \langle t, t^2, t^3 \rangle$: $\mathbf{r}'(t) = \langle 1, 2t, 3t^2 \rangle$, $\mathbf{r}''(t) = \langle 0, 2, 6t \rangle$, $|\mathbf{r}'(t)| = \sqrt{1 + 4t^2 + 9t^4}$, and
>
> $$
> \mathbf{r}'(t) \times \mathbf{r}''(t) = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2t & 3t^2 \\ 0 & 2 & 6t \end{vmatrix} = 6t^2\,\mathbf{i} - 6t\,\mathbf{j} + 2\,\mathbf{k}, \qquad |\mathbf{r}' \times \mathbf{r}''| = \sqrt{36t^4 + 36t^2 + 4} = 2\sqrt{9t^4 + 9t^2 + 1} .
> $$
>
> So $\kappa(t) = \dfrac{2\sqrt{1 + 9t^2 + 9t^4}}{(1 + 4t^2 + 9t^4)^{3/2}}$; at the origin ($t = 0$), $\kappa(0) = 2$.
>
> **(c)** *Parabola, by [[§88 Arc Length and Curvature#^cor-88-5|Corollary §88.5]].* For $y = x^2$, $y' = 2x$ and $y'' = 2$, so
>
> $$
> \kappa(x) = \frac{2}{(1 + 4x^2)^{3/2}} .
> $$
>
> At $(0, 0)$, $\kappa = 2$; at $(1, 1)$, $\kappa = 2/5^{3/2} \approx 0.18$; at $(2, 4)$, $\kappa = 2/17^{3/2} \approx 0.03$. As $x \to \pm\infty$, $\kappa(x) \to 0$: the parabola becomes nearly straight.
>
> **(d)** *The osculating circle of $y = x^2$ at the origin* ([[§88a The TNB Frame and Torsion#^def-88-new3|Definition §88.8]] below). By (c) its radius is $1/\kappa(0) = \frac12$. The tangent at the origin is horizontal, so $\mathbf{N} = \langle 0, 1 \rangle$ points up into the parabola, and the center of curvature is $\big(0, \frac12\big)$. The osculating circle is $x^2 + \big(y - \frac12\big)^2 = \frac14$.
>
> *Stewart: Examples 13.3.3, 13.3.4, 13.3.5 and 13.3.9*

^ex-88-4

![[m233-88-1.svg]]
*The parabola $y = x^2$ (blue), its curvature function $\kappa(x) = 2/(1 + 4x^2)^{3/2}$ (green) and its osculating circle at the origin (red), of radius $1/\kappa(0) = \frac12$ and center $(0, \frac12)$. The curvature is largest at the vertex, where the parabola bends most, and tends to $0$ as the parabola straightens out. Near the origin, circle and parabola bend alike: they share the point, the tangent, the normal and the curvature.*

*The section continues in [[§88a The TNB Frame and Torsion]].*
