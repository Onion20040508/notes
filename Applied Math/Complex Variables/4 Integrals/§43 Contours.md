---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 43
bc: "43"
aliases: ["B&C 43"]
tags: [complex-variables, math342]
---
← [[§42 Definite Integrals of Functions w(t)]] · ↑ [[· 4 Integrals]] · [[§44 Contour Integrals]] →

*Brown–Churchill, Section 43.*

Integrals of functions of a complex variable are taken along curves in the plane, and this section fixes the class of curves. An arc is a continuous image of a parameter interval, traced in the order of increasing parameter; it is smooth if it has a continuously turning tangent, and a **contour** is finitely many smooth arcs joined end to end, so polygons and circles are contours. Arc length turns out not to depend on the parametrization, and the same computation will show in [[§44 Contour Integrals#^prop-44-1|§44]] that contour integrals do not either. The section ends with the Jordan curve theorem, which gives every simple closed contour an inside and an outside; the Cauchy–Goursat theorem and the Cauchy integral formula are statements about that inside.

## Arcs

> [!definition] Definition §43.1: Arc, Simple Arc, Simple Closed Curve
> A set of points $z = (x, y)$ in the complex plane is an **arc** if
>
> $$
> x = x(t), \qquad y = y(t) \qquad (a \le t \le b), \qquad (1)
> $$
>
> where $x(t)$ and $y(t)$ are continuous functions of the real parameter $t$. This is a continuous mapping of the interval $a \le t \le b$ into the plane, and the image points are ordered according to increasing values of $t$. It is convenient to write the points of $C$ as
>
> $$
> z = z(t) \quad (a \le t \le b), \qquad (2) \qquad\qquad z(t) = x(t) + iy(t) . \qquad (3)
> $$
>
> The arc $C$ is a **simple arc**, or **Jordan arc**, if it does not cross itself, that is, if $z(t_1) \ne z(t_2)$ when $t_1 \ne t_2$. When $C$ is simple except that $z(b) = z(a)$, it is a **simple closed curve**, or **Jordan curve**. Such a curve is **positively oriented** when it is described in the counterclockwise direction.
>
> *B&C: Sec. 43 (text)*

^def-43-1

The geometric nature of an arc often suggests a notation for the parameter other than $t$.

> [!example] Example §43.1: A Polygonal Line
> The polygonal line ([[§12★ Regions in the Complex Plane#^def-12-4|Definition §12.4]]) defined by
>
> $$
> z = \begin{cases} x + ix & \text{when } 0 \le x \le 1, \\ x + i & \text{when } 1 \le x \le 2, \end{cases} \qquad (4)
> $$
>
> consisting of a line segment from $0$ to $1 + i$ followed by one from $1 + i$ to $2 + i$, is a simple arc. The two formulas agree at $x = 1$, so $z$ is continuous; and $\operatorname{Re} z = x$, so different parameter values give different points.
>
> *B&C: Sec. 43, Example 1*

^ex-43-1

> [!example] Example §43.2: Circles
> The unit circle
>
> $$
> z = e^{i\theta} \qquad (0 \le \theta \le 2\pi) \qquad (5)
> $$
>
> about the origin is a simple closed curve, oriented in the counterclockwise direction. So is the circle
>
> $$
> z = z_0 + Re^{i\theta} \qquad (0 \le \theta \le 2\pi), \qquad (6)
> $$
>
> centered at $z_0$ with radius $R$ ([[§7 Exponential Form#^prop-7-1|Proposition §7.1]]). Here $e^{i\theta_1} = e^{i\theta_2}$ with $0 \le \theta_1 < \theta_2 \le 2\pi$ only for $\theta_1 = 0$, $\theta_2 = 2\pi$, the endpoints.
>
> *B&C: Sec. 43, Example 2*

^ex-43-2

The same set of points can make up different arcs.

> [!example] Example §43.3: Same Points, Different Arcs
> The arc
>
> $$
> z = e^{-i\theta} \qquad (0 \le \theta \le 2\pi) \qquad (7)
> $$
>
> is not the same as the arc (5): the set of points is the same, but now the circle is traversed in the *clockwise* direction. The points on the arc
>
> $$
> z = e^{i2\theta} \qquad (0 \le \theta \le 2\pi) \qquad (8)
> $$
>
> are again those of (5) and (7), but this arc differs from both, since the circle is traversed *twice* in the counterclockwise direction. It is not a simple closed curve: $e^{i2\theta}$ takes the value $1$ at $\theta = 0$, $\pi$ and $2\pi$.
>
> *B&C: Sec. 43, Examples 3 and 4*

^ex-43-3

## Change of Parameter and Arc Length

The parametric representation of a given arc is not unique; the parameter interval can be changed to any other interval.

> [!definition] Definition §43.2: Change of Parameter
> Let $C$ be given by (2), and let
>
> $$
> t = \phi(\tau) \qquad (\alpha \le \tau \le \beta), \qquad (9)
> $$
>
> where $\phi$ is a real-valued function mapping the interval $\alpha \le \tau \le \beta$ onto $a \le t \le b$, $\phi$ is continuous with a continuous derivative, and $\phi'(\tau) > 0$ for each $\tau$ (so $t$ increases with $\tau$). Then (2) is transformed by (9) into
>
> $$
> z = Z(\tau) \quad (\alpha \le \tau \le \beta), \qquad (10) \qquad\qquad Z(\tau) = z[\phi(\tau)] . \qquad (11)
> $$
>
> *B&C: Sec. 43 (text)*

^def-43-2

The simplest change of parameter is linear: the line through $(\alpha, a)$ and $(\beta, b)$ in the $\tau t$ plane is
$$
\phi(\tau) = \frac{b - a}{\beta - \alpha}\,\tau + \frac{a\beta - b\alpha}{\beta - \alpha} ,
$$
which maps $[\alpha, \beta]$ onto $[a, b]$ with $\phi' = (b - a)/(\beta - \alpha) > 0$ (B&C, Exercise 3). It is used to join two contours end to end with a single parameter.

Two facts about such changes of parameter are used repeatedly: the substitution rule for integrals of $w(t)$, and the chain rule for $Z(\tau)$. The text relies on both, so they are boxed here.

> [!theorem] Lemma §43.1: Change of Variables in Integrals of w(t)
> Let $w(t) = u(t) + iv(t)$ be continuous on $a \le t \le b$. Then
>
> **(a)** $\displaystyle\int_{-b}^{-a} w(-t)\,dt = \int_a^b w(\tau)\,d\tau$;
>
> **(b)** $\displaystyle\int_a^b w(t)\,dt = \int_\alpha^\beta w[\phi(\tau)]\,\phi'(\tau)\,d\tau$, where $\phi$ is a change of parameter as in (9).
>
> Both identities remain true when $w$ is only piecewise continuous.
>
> *B&C: Sec. 43, Exercise 1*

^lem-43-1

> [!proof]+ Proof
> By definition ([[§42 Definite Integrals of Functions w(t)#^def-42-1|Definition §42.1]]) each side is (integral of the real part) $+ i\,$(integral of the imaginary part), and the real and imaginary parts of $w(-t)$ and of $w[\phi(\tau)]\phi'(\tau)$ are $u(-t)$, $v(-t)$ and $u[\phi(\tau)]\phi'(\tau)$, $v[\phi(\tau)]\phi'(\tau)$, since $\phi'$ is real. So it suffices to prove both identities for a continuous real function $u$.
>
> **(a)** Substitute $\tau = -t$, $d\tau = -dt$: $\int_{-b}^{-a} u(-t)\,dt = -\int_{b}^{a} u(\tau)\,d\tau = \int_a^b u(\tau)\,d\tau$.
>
> **(b)** This is the substitution rule $t = \phi(\tau)$ for definite integrals, valid since $\phi$ has a continuous derivative, $\phi(\alpha) = a$ and $\phi(\beta) = b$ (because $\phi$ is increasing and onto).
>
> **Piecewise continuous $w$.** Let $a = t_0 < \cdots < t_n = b$ include the points of discontinuity of $w$. On each $[t_{k-1}, t_k]$, $w$ agrees except at the endpoints with a continuous function (use the one-sided limits there), and the corresponding $\tau$-interval is $[\phi^{-1}(t_{k-1}), \phi^{-1}(t_k)]$, since $\phi$ is a strictly increasing bijection. Apply the continuous case on each piece and add, by [[§42 Definite Integrals of Functions w(t)#^prop-42-1|Proposition §42.1]](d); (a) is handled in the same way.

^pf-43-1

*Uses:* [[§42 Definite Integrals of Functions w(t)#^def-42-1|Def. §42.1]], [[§42 Definite Integrals of Functions w(t)#^prop-42-1|§42.1]], [[§43 Contours#^def-43-2|Def. §43.2]], [[§38 The Substitution Rule#^thm-38-3|Calc Thm. §38.3]] (substitution rule for definite integrals)

> [!theorem] Lemma §43.2: Chain Rule for a Change of Parameter
> If $z(t)$ is differentiable at $t = \phi(\tau)$ and $\phi$ is differentiable at $\tau$, then $Z(\tau) = z[\phi(\tau)]$ is differentiable at $\tau$ and
>
> $$
> Z'(\tau) = z'[\phi(\tau)]\,\phi'(\tau) . \qquad (14)
> $$
>
> *B&C: Sec. 43, Exercise 4*

^lem-43-2

> [!proof]+ Proof
> (B&C's suggestion.) Write $Z(\tau) = x[\phi(\tau)] + iy[\phi(\tau)]$. By the real chain rule, $\frac{d}{d\tau}x[\phi(\tau)] = x'[\phi(\tau)]\phi'(\tau)$ and likewise for $y$. So, by [[§41 Derivatives of Functions w(t)#^def-41-1|Definition §41.1]], $Z'(\tau) = \big(x'[\phi(\tau)] + iy'[\phi(\tau)]\big)\phi'(\tau) = z'[\phi(\tau)]\phi'(\tau)$.

^pf-43-2

*Uses:* [[§41 Derivatives of Functions w(t)#^def-41-1|Def. §41.1]], [[§28 Basic Properties of the Derivative#^thm-28-3|451 Thm. §28.3]] (chain rule)

> [!definition] Definition §43.3: Differentiable Arc; Length
> Suppose that the components $x'(t)$ and $y'(t)$ of the derivative
>
> $$
> z'(t) = x'(t) + iy'(t) \qquad (12)
> $$
>
> of the function (3) used to represent $C$ are continuous on the entire interval $a \le t \le b$. The arc is then called a **differentiable arc**, the real-valued function $|z'(t)| = \sqrt{[x'(t)]^2 + [y'(t)]^2}$ is integrable over $a \le t \le b$, and the **length** of $C$ is the number
>
> $$
> L = \int_a^b |z'(t)|\,dt . \qquad (13)
> $$
>
> *B&C: Sec. 43 (text)*

^def-43-3

> [!remark]- Connections
> - Formula (13) is the arc length formula of calculus for the plane curve $\langle x(t), y(t)\rangle$, [[§88 Arc Length and Curvature#^thm-88-1|Calc Thm. §88.1]], written with the modulus of a complex number.

> [!theorem] Proposition §43.3: Arc Length Does Not Depend on the Parametrization
> If $C$ is a differentiable arc (2) and $\phi$ is a change of parameter (9), then $Z(\tau) = z[\phi(\tau)]$ is a differentiable arc and
>
> $$
> L = \int_a^b |z'(t)|\,dt = \int_\alpha^\beta |Z'(\tau)|\,d\tau .
> $$
>
> *B&C: Sec. 43 (text)*

^prop-43-3

> [!proof]+ Proof
> By Lemma §43.2, $Z'(\tau) = z'[\phi(\tau)]\phi'(\tau)$, which is continuous, as a product of continuous functions; so $Z$ is a differentiable arc. Applying Lemma §43.1(b) to the continuous real function $|z'(t)|$,
>
> $$
> L = \int_\alpha^\beta |z'[\phi(\tau)]|\,\phi'(\tau)\,d\tau .
> $$
>
> Since $\phi'(\tau) > 0$, $|z'[\phi(\tau)]|\,\phi'(\tau) = |z'[\phi(\tau)]\,\phi'(\tau)| = |Z'(\tau)|$, by (14).

^pf-43-3

*Uses:* [[§43 Contours#^def-43-2|Def. §43.2]], [[§43 Contours#^def-43-3|Def. §43.3]], [[§43 Contours#^lem-43-1|§43.1]], [[§43 Contours#^lem-43-2|§43.2]]

> [!example] Example §43.4: Two Parametrizations of a Half Circle
> Let $C$ be the right-hand half of the circle $|z| = 2$, in the counterclockwise direction, from $-2i$ to $2i$. Two parametric representations of $C$ are
>
> $$
> z = z(\theta) = 2e^{i\theta} \quad \Big(-\frac\pi2 \le \theta \le \frac\pi2\Big) \qquad\text{and}\qquad z = Z(y) = \sqrt{4 - y^2} + iy \quad (-2 \le y \le 2) .
> $$
>
> Verify that $Z(y) = z[\phi(y)]$, where $\phi(y) = \arctan\dfrac{y}{\sqrt{4 - y^2}}$ $\big(-\frac\pi2 < \arctan t < \frac\pi2\big)$, and that $\phi$ has a positive derivative.
>
> **$Z = z \circ \phi$.** For $-2 < y < 2$ let $\theta = \phi(y)$, an angle in $(-\frac\pi2, \frac\pi2)$ with $\tan\theta = y/\sqrt{4 - y^2}$. Since $\cos\theta > 0$, the right triangle with legs $\sqrt{4 - y^2}$, $y$ and hypotenuse $2$ gives $\cos\theta = \frac12\sqrt{4 - y^2}$ and $\sin\theta = \frac y2$. Hence $z[\phi(y)] = 2\cos\theta + 2i\sin\theta = \sqrt{4 - y^2} + iy = Z(y)$. At $y = \pm2$ set $\phi(\pm2) = \pm\frac\pi2$, the limits of $\phi$ there; then $Z(\pm2) = \pm2i = z(\pm\frac\pi2)$ as well, and $\phi$ maps $[-2, 2]$ continuously onto $[-\frac\pi2, \frac\pi2]$.
>
> **$\phi' > 0$.** With $g(y) = y(4 - y^2)^{-1/2}$, $g'(y) = (4 - y^2)^{-1/2} + y^2(4 - y^2)^{-3/2} = 4(4 - y^2)^{-3/2}$, and
>
> $$
> \phi'(y) = \frac{g'(y)}{1 + g(y)^2} = \frac{4(4 - y^2)^{-3/2}}{4/(4 - y^2)} = \frac{1}{\sqrt{4 - y^2}} > 0 \qquad (-2 < y < 2) .
> $$
>
> (Numerically, $\phi'(0.3) = 0.50572 = 1/\sqrt{3.91}$.) Note that $\phi'(y) \to \infty$ as $y \to \pm2$, so $\phi$ satisfies the conditions of Definition §43.2 only on closed subintervals of $(-2, 2)$; correspondingly $Z'(y) = -y/\sqrt{4 - y^2} + i$ is unbounded near $y = \pm2$, and $Z$ is not a smooth parametrization of $C$ at its endpoints although $z(\theta)$ is. [[§44 Contour Integrals#^ex-44-1|Example §44.1]] integrates $\bar z$ along $C$ with both representations.
>
> *B&C: Sec. 43, Exercise 2*

^ex-43-4

## Smooth Arcs and Contours

> [!definition] Definition §43.4: Smooth Arc; Unit Tangent
> A **smooth arc** is an arc $z = z(t)$ $(a \le t \le b)$ whose derivative $z'(t)$ is continuous on the closed interval $a \le t \le b$ and nonzero throughout the open interval $a < t < b$. Then the **unit tangent vector**
>
> $$
> \mathbf{T} = \frac{z'(t)}{|z'(t)|}
> $$
>
> is well defined for all $t$ in $a < t < b$, with angle of inclination $\arg z'(t)$, and it turns continuously as $t$ varies. (This is the unit tangent of calculus when $z(t)$ is read as a radius vector.)
>
> *B&C: Sec. 43 (text)*

^def-43-4

> [!definition] Definition §43.5: Contour; Simple Closed Contour
> A **contour**, or piecewise smooth arc, is an arc consisting of a finite number of smooth arcs joined end to end. Hence if (2) represents a contour, $z(t)$ is continuous, whereas its derivative $z'(t)$ is piecewise continuous. When only the initial and final values of $z(t)$ are the same, the contour is a **simple closed contour**. The **length** of a contour or simple closed contour is the sum of the lengths of the smooth arcs that make it up.
>
> *B&C: Sec. 43 (text)*

^def-43-5

The polygonal line (4) is a contour; the circles (5) and (6) and the boundary of a triangle or a rectangle, taken in a specific direction, are simple closed contours.

> [!remark]- Connections
> - A contour is the piecewise-smooth curve of calculus, [[§108 Line Integrals#^def-108-2|Calc Def. §108.2]], which is also the class of curves along which line integrals and Green's theorem ([[§110 Green's Theorem#^thm-110-1|Calc Thm. §110.1]]) are developed there.

> [!example] Example §43.5: A Smooth Arc That Crosses the Real Axis Infinitely Often
> Let $y(x) = x^3\sin(\pi/x)$ when $0 < x \le 1$ and $y(0) = 0$, and let $C$ be $z = x + iy(x)$ $(0 \le x \le 1)$.
>
> **(a)** $C$ meets the real axis exactly where $y(x) = 0$, that is, at $x = 0$ and where $\sin(\pi/x) = 0$, i.e. $\pi/x = n\pi$: at the points $z = 1/n$ $(n = 1, 2, \ldots)$ and $z = 0$. It is a simple arc, since $\operatorname{Re} z = x$.
>
> **(b)** $C$ is smooth. For continuity at $0$: $0 \le |x^3\sin(\pi/x)| \le x^3 \to 0$. For $y'(0)$: $\big|\frac{y(x) - y(0)}{x}\big| = |x^2\sin(\pi/x)| \le x^2 \to 0$, so $y'(0) = 0$. For $x > 0$, $y'(x) = 3x^2\sin(\pi/x) - \pi x\cos(\pi/x)$, and $|y'(x)| \le 3x^2 + \pi x \to 0$ as $x \to 0^+$; so $y'$ is continuous on $[0, 1]$. Then $z'(x) = 1 + iy'(x)$ is continuous and never zero.
>
> So a smooth arc can wiggle across a line infinitely often near a point; [[§52 Simply Connected Domains#^ex-52-2|Example §52.2]] uses this arc to build a closed contour with infinitely many self-intersections.
>
> *B&C: Sec. 43, Exercise 6*

^ex-43-5

> [!theorem] Theorem §43.4: Jordan Curve Theorem
> The points on any simple closed curve or simple closed contour $C$ are boundary points of two distinct domains. One of them, the **interior** of $C$, is bounded; the other, the **exterior** of $C$, is unbounded.
>
> *B&C: Sec. 43 (text)*

^thm-43-4

*B&C omits the proof.*

B&C accepts the statement as geometrically evident and remarks that the proof is not easy; it cites Newman and Thron for the general case and Hille (Vol. 1, pp. 281–285) for a simple closed polygon. The vault has no proof either. The theorem is what gives meaning to "the points interior to and on $C$" in the Cauchy–Goursat theorem ([[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|Theorem §51.3]]) and the Cauchy integral formula ([[§54 Cauchy Integral Formula#^thm-54-1|Theorem §54.1]]). For a positively oriented simple closed contour the interior lies to the left as $C$ is traversed.

![[m342-43-1.svg]]
*Left: the polygonal line (4), a contour made of two smooth arcs with a corner at $1 + i$. Right: a positively oriented simple closed contour made of three smooth arcs (a segment, a quarter circle, and a curved arc), with corners where they meet. By the Jordan curve theorem its points are the common boundary of a bounded interior (shaded), which lies to the left of the direction of travel, and an unbounded exterior.*

## The Chain Rule Along an Arc

Later sections ([[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|§49]], and the angle-preservation of conformal maps in [[§112★ Preservation of Angles and Scale Factors#^thm-112-1|Theorem §112.1]]) differentiate an analytic function along an arc.

> [!theorem] Proposition §43.5: Chain Rule Along an Arc
> Suppose that a function $f(z)$ is analytic at a point $z_0 = z(t_0)$ lying on a smooth arc $z = z(t)$ $(a \le t \le b)$. If $w(t) = f[z(t)]$, then
>
> $$
> w'(t_0) = f'[z(t_0)]\,z'(t_0) .
> $$
>
> *B&C: Sec. 43, Exercise 5*

^prop-43-5

> [!proof]+ Proof
> B&C suggests writing $w(t) = u[x(t), y(t)] + iv[x(t), y(t)]$ and using the two-variable chain rule with the Cauchy–Riemann equations; that route needs $u$ and $v$ to be differentiable as functions of $(x, y)$ at $(x_0, y_0)$, which follows from the existence of $f'(z_0)$ (the remark after [[§23 Sufficient Conditions for Differentiability#^cor-23-2|Corollary §23.2]]). Here is a direct argument that uses only the existence of $f'(z_0)$ and of $z'(t_0)$.
>
> Define $\eta(z) = \dfrac{f(z) - f(z_0)}{z - z_0} - f'(z_0)$ for $z \ne z_0$ in a neighborhood of $z_0$ where $f$ is defined, and $\eta(z_0) = 0$. By the definition of $f'(z_0)$ ([[§19 Derivatives#^def-19-1|Definition §19.1]]), $\eta(z) \to 0 = \eta(z_0)$ as $z \to z_0$, so $\eta$ is continuous at $z_0$, and
>
> $$
> f(z) - f(z_0) = \big[f'(z_0) + \eta(z)\big](z - z_0)
> $$
>
> for all $z$ in that neighborhood (both sides vanish at $z_0$). Since $z(t)$ is continuous, $z(t)$ lies in the neighborhood for $t$ near $t_0$, and then, for $t \ne t_0$,
>
> $$
> \frac{w(t) - w(t_0)}{t - t_0} = \big[f'(z_0) + \eta(z(t))\big]\,\frac{z(t) - z(t_0)}{t - t_0} .
> $$
>
> As $t \to t_0$, $\eta(z(t)) \to \eta(z_0) = 0$ (a continuous function of a continuous function), and the last quotient tends to $z'(t_0)$. Hence the left side tends to $f'(z_0)z'(t_0)$. A complex-valued function of $t$ has a limit exactly when its real and imaginary parts do ([[§16 Theorems on Limits#^thm-16-1|Theorem §16.1]]), so the difference quotients of $\operatorname{Re} w$ and $\operatorname{Im} w$ converge, and by [[§41 Derivatives of Functions w(t)#^def-41-1|Definition §41.1]] $w'(t_0) = f'(z_0)z'(t_0)$. (At an endpoint $t_0 = a$ or $b$ the limits are one-sided.)
>
> In the notation of B&C's suggestion the result reads $w' = (u_xx' + u_yy') + i(v_xx' + v_yy')$, which by $u_x = v_y$, $u_y = -v_x$ ([[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]) equals $(u_x + iv_x)(x' + iy') = f'(z_0)z'(t_0)$.

^pf-43-5

*Uses:* [[§41 Derivatives of Functions w(t)#^def-41-1|Def. §41.1]], [[§19 Derivatives#^def-19-1|Def. §19.1]], [[§16 Theorems on Limits#^thm-16-1|§16.1]], [[§21 Cauchy–Riemann Equations#^thm-21-1|§21.1]]

> [!remark]- Connections
> - B&C's route is the multivariable chain rule, [[§10 Composition of Functions and the Chain Rule#^thm-10-2|452 Thm. §10.2]], applied to $(u, v)$ composed with $(x(t), y(t))$; complex differentiability at $z_0$ gives the real differentiability of $(u, v)$ that it needs, with Jacobian the rotation–scaling matrix of $f'(z_0)$.
