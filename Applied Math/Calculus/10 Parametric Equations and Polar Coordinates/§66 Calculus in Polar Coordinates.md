---
type: section
subject: "[[Calculus]]"
chapter: 10
section: 66
stewart: "10.4"
aliases: ["Stewart 10.4"]
tags: [calculus]
---
← [[§65 Polar Coordinates]] · ↑ [[· 10 Parametric Equations and Polar Coordinates]] · [[§67 Conic Sections]] →

*Stewart, Section 10.4.*

Areas, arc lengths and tangents of polar curves $r = f(\theta)$. For areas the natural pieces are not rectangles but thin sectors swept out by a rotating ray, and the area of a sector, $\frac12 r^2\theta$, leads to $A = \int \frac12 r^2\,d\theta$. For arc length and tangents, $\theta$ is treated as the parameter of the parametric curve $x = f(\theta)\cos\theta$, $y = f(\theta)\sin\theta$, and the results of [[§64 Calculus with Parametric Curves|§64]] apply. A recurring difficulty is that a point has many polar representations, so two polar curves can meet at a point where their equations have no common solution.

## Area

> [!theorem] Theorem §66.1: Area of a Sector
> The area of a sector of a circle with radius $r$ and central angle $\theta$ (in radians) is
>
> $$
> A = \tfrac12 r^2\theta .
> $$
>
> *Stewart: 10.4, Formula 1*

^thm-66-1

> [!proof]+ Proof
> The area of a sector is proportional to its central angle. The whole disk, with central angle $2\pi$, has area $\pi r^2$, so $A = \dfrac{\theta}{2\pi} \cdot \pi r^2 = \dfrac12 r^2\theta$. (Stewart's Exercise 7.3.41 computes it by integration.)

^pf-66-1

*Uses:* area $\pi r^2$ of a disk (computed by integration in [[§46 Trigonometric Substitution|§46]])

> [!theorem] Theorem §66.2: Area of a Polar Region
> Let $\mathscr{R}$ be the region bounded by the polar curve $r = f(\theta)$ and the rays $\theta = a$ and $\theta = b$, where $f$ is a positive continuous function and $0 < b - a \le 2\pi$. The area of $\mathscr{R}$ is
>
> $$
> A = \int_a^b \tfrac12 [f(\theta)]^2\,d\theta , \qquad\text{often written}\qquad A = \int_a^b \tfrac12 r^2\,d\theta ,
> $$
>
> with the understanding that $r = f(\theta)$. Think of the area as swept out by a ray through $O$ rotating from angle $a$ to angle $b$.
>
> *Stewart: 10.4, Formulas 3 and 4*

^thm-66-2

> [!remark] Remark: Why It Works
> Divide $[a, b]$ into $n$ subintervals with endpoints $\theta_0, \ldots, \theta_n$ and equal width $\Delta\theta$. The rays $\theta = \theta_i$ cut $\mathscr{R}$ into $n$ thin regions of central angle $\Delta\theta$. Choosing $\theta_i^*$ in $[\theta_{i-1}, \theta_i]$, the $i$th region is approximately a sector of radius $f(\theta_i^*)$, of area $\Delta A_i \approx \frac12 [f(\theta_i^*)]^2\,\Delta\theta$ by Theorem §66.1. So
>
> $$
> A \approx \sum_{i=1}^n \tfrac12 [f(\theta_i^*)]^2\,\Delta\theta , \qquad (2)
> $$
>
> a Riemann sum for $\frac12 f^2$, and the approximation improves as $n \to \infty$. This is Stewart's argument ("it appears plausible, and can in fact be proved"). Note the similarity between Formula 1, $A = \frac12 r^2\theta$, and Formula 4, $A = \int \frac12 r^2\,d\theta$.

^rem-66-1

> [!proof]+ Proof
> We make the approximation (2) precise by squeezing each thin region between two sectors. (Stewart only says the formula "can in fact be proved"; this argument assumes, as Stewart does, that area is additive and that a region contained in another has smaller area.)
>
> On $[\theta_{i-1}, \theta_i]$ the continuous function $f$ has a minimum $m_i = f(u_i)$ and a maximum $M_i = f(v_i)$ (Extreme Value Theorem, [[§25 Maximum and Minimum Values|§25]]). The $i$th thin region consists of the points $(r, \theta)$ with $\theta_{i-1} \le \theta \le \theta_i$ and $0 \le r \le f(\theta)$. It contains the sector of radius $m_i$ and is contained in the sector of radius $M_i$, both with central angle $\Delta\theta$, so by Theorem §66.1
>
> $$
> \tfrac12 [f(u_i)]^2\,\Delta\theta \;\le\; \Delta A_i \;\le\; \tfrac12 [f(v_i)]^2\,\Delta\theta .
> $$
>
> Adding over $i$ (the thin regions overlap only along rays, which have no area; here $b - a \le 2\pi$ ensures that they do not overlap otherwise):
>
> $$
> \sum_{i=1}^n \tfrac12 [f(u_i)]^2\,\Delta\theta \;\le\; A \;\le\; \sum_{i=1}^n \tfrac12 [f(v_i)]^2\,\Delta\theta .
> $$
>
> Both outer sums are Riemann sums for the continuous function $\frac12 f^2$ on $[a, b]$, so both tend to $\int_a^b \frac12 [f(\theta)]^2\,d\theta$ as $n \to \infty$ ([[§35 The Definite Integral|§35]]). Since $A$ does not depend on $n$, the Squeeze Theorem gives $A = \int_a^b \frac12 [f(\theta)]^2\,d\theta$.

^pf-66-2

*Uses:* [[§66 Calculus in Polar Coordinates#^thm-66-1|§66.1]], [[§25 Maximum and Minimum Values|§25]] (Extreme Value Theorem), [[§35 The Definite Integral|§35]] (Riemann sums of a continuous function converge to the integral), [[§8 Calculating Limits Using the Limit Laws|§8]] (Squeeze Theorem)

![[m233-66-1.svg]]
*The proof of Theorem §66.2. The rays $\theta = \theta_{i-1}$ and $\theta = \theta_i$ cut a thin piece (blue) out of the region under $r = f(\theta)$. It contains the sector of radius $m_i = \min f$ (green) and lies inside the sector of radius $M_i = \max f$ (red dashed), both of area $\frac12(\text{radius})^2\Delta\theta$.*

> [!remark]- Connections
> - In double-integral form the same area is $\iint_{\mathscr{R}} dA = \int_a^b \int_0^{f(\theta)} r\,dr\,d\theta = \int_a^b \frac12 [f(\theta)]^2\,d\theta$, by the change of variables to polar coordinates: [[§15 Multivariable Integration#^thm-15-7|452 Thm. §15.7]] (and [[§100 Double Integrals in Polar Coordinates|§100]]).

> [!example] Example §66.1: One Loop of the Four-Leaved Rose
> Find the area enclosed by one loop of $r = \cos 2\theta$.
>
> The right loop ([[§65 Polar Coordinates#^ex-65-5|Example §65.5]]) is swept out by a ray rotating from $\theta = -\pi/4$ to $\theta = \pi/4$, on which $\cos 2\theta \ge 0$. By Theorem §66.2,
>
> $$
> A = \int_{-\pi/4}^{\pi/4} \tfrac12 r^2\,d\theta = \tfrac12 \int_{-\pi/4}^{\pi/4} \cos^2 2\theta\,d\theta .
> $$
>
> The integrand is even (the loop is symmetric about the polar axis), so using $\cos^2 u = \frac12(1 + \cos 2u)$,
>
> $$
> A = 2 \cdot \tfrac12 \int_0^{\pi/4} \cos^2 2\theta\,d\theta = \int_0^{\pi/4} \tfrac12 (1 + \cos 4\theta)\,d\theta = \tfrac12 \Big[\theta + \tfrac14 \sin 4\theta\Big]_0^{\pi/4} = \tfrac12 \cdot \frac{\pi}{4} = \frac{\pi}{8} .
> $$
>
> *Stewart: Example 10.4.1*

^ex-66-1

> [!theorem] Corollary §66.3: Area Between Two Polar Curves
> Let $\mathscr{R}$ be bounded by $r = f(\theta)$, $r = g(\theta)$, $\theta = a$ and $\theta = b$, where $f(\theta) \ge g(\theta) \ge 0$ are continuous and $0 < b - a \le 2\pi$. Then
>
> $$
> A = \int_a^b \tfrac12 [f(\theta)]^2\,d\theta - \int_a^b \tfrac12 [g(\theta)]^2\,d\theta = \tfrac12 \int_a^b \big([f(\theta)]^2 - [g(\theta)]^2\big)\,d\theta .
> $$
>
> *Stewart: 10.4 (text)*

^cor-66-3

> [!proof]+ Proof
> $\mathscr{R}$ is the region inside $r = f(\theta)$ between the rays, minus the region inside $r = g(\theta)$ between the rays, which it contains because $g \le f$. Subtract the two areas given by Theorem §66.2 and combine the integrals by linearity. (Where $g = 0$ the inner region degenerates, and Theorem §66.2 still holds for $f \ge 0$ by the same proof.)

^pf-66-3

*Uses:* [[§66 Calculus in Polar Coordinates#^thm-66-2|§66.2]]

> [!example] Example §66.2: Inside a Circle, Outside a Cardioid
> Find the area of the region inside the circle $r = 3\sin\theta$ and outside the cardioid $r = 1 + \sin\theta$.
>
> **Limits.** The curves meet where $3\sin\theta = 1 + \sin\theta$, that is $\sin\theta = \frac12$: $\theta = \pi/6$ and $5\pi/6$. For $\pi/6 \le \theta \le 5\pi/6$, $3\sin\theta \ge 1 + \sin\theta$, so the circle is the outer curve.
>
> **Area.** By Corollary §66.3,
>
> $$
> A = \tfrac12 \int_{\pi/6}^{5\pi/6} (3\sin\theta)^2\,d\theta - \tfrac12 \int_{\pi/6}^{5\pi/6} (1 + \sin\theta)^2\,d\theta .
> $$
>
> The region is symmetric about $\theta = \pi/2$ (both integrands are unchanged by $\theta \mapsto \pi - \theta$), so
>
> $$
> \begin{aligned}
> A &= 2\Big[\tfrac12 \int_{\pi/6}^{\pi/2} 9\sin^2\theta\,d\theta - \tfrac12 \int_{\pi/6}^{\pi/2} (1 + 2\sin\theta + \sin^2\theta)\,d\theta\Big]
> = \int_{\pi/6}^{\pi/2} (8\sin^2\theta - 1 - 2\sin\theta)\,d\theta \\
> &= \int_{\pi/6}^{\pi/2} (3 - 4\cos 2\theta - 2\sin\theta)\,d\theta \qquad [\sin^2\theta = \tfrac12(1 - \cos 2\theta)] \\
> &= \Big[3\theta - 2\sin 2\theta + 2\cos\theta\Big]_{\pi/6}^{\pi/2} = \Big(\frac{3\pi}{2} - 0 + 0\Big) - \Big(\frac{\pi}{2} - \sqrt3 + \sqrt3\Big) = \pi .
> \end{aligned}
> $$
>
> *Stewart: Example 10.4.2*

^ex-66-2

> [!remark] Remark: Finding All Points of Intersection
> Because a point has many polar representations, solving the two equations simultaneously may miss intersection points. In Example §66.2 the circle and the cardioid meet in **three** points, but the equations give only $(\frac32, \pi/6)$ and $(\frac32, 5\pi/6)$. The third is the pole. As $(0, 0)$ or $(0, \pi)$ it satisfies $r = 3\sin\theta$, and as $(0, 3\pi/2)$ it satisfies $r = 1 + \sin\theta$, but no single representation satisfies both. Think of two points moving along the curves as $\theta$ runs from $0$ to $2\pi$: one reaches the pole at $\theta = 0$ and $\theta = \pi$, the other at $\theta = 3\pi/2$. They do not collide, but the curves still intersect. To find all intersection points, draw both curves (Stewart recommends a graphing device) and check the pole separately.

^rem-66-2

> [!example] Example §66.3: Intersections of a Rose and a Circle
> Find all points of intersection of $r = \cos 2\theta$ and $r = \frac12$.
>
> Solving simultaneously, $\cos 2\theta = \frac12$, so $2\theta = \pi/3, 5\pi/3, 7\pi/3, 11\pi/3$ (for $0 \le \theta < 2\pi$), giving the four points
>
> $$
> (\tfrac12, \pi/6), \quad (\tfrac12, 5\pi/6), \quad (\tfrac12, 7\pi/6), \quad (\tfrac12, 11\pi/6) .
> $$
>
> But a sketch shows that the circle meets each of the four leaves twice, so there are eight intersection points. The other four lie on the leaves traced with $r < 0$. The same circle is also $r = -\frac12$ (the points $(-\frac12, \theta)$ are at distance $\frac12$ from $O$), and solving $\cos 2\theta = -\frac12$ gives $2\theta = 2\pi/3, 4\pi/3, 8\pi/3, 10\pi/3$, i.e. $\theta = \pi/3, 2\pi/3, 4\pi/3, 5\pi/3$. The points $(-\frac12, \theta)$ for these $\theta$ are the same as $(\frac12, \theta + \pi)$, so the remaining four points are
>
> $$
> (\tfrac12, \pi/3), \quad (\tfrac12, 2\pi/3), \quad (\tfrac12, 4\pi/3), \quad (\tfrac12, 5\pi/3)
> $$
>
> (for instance $(-\frac12, 2\pi/3) = (\frac12, 5\pi/3)$). They can also be found by symmetry.
>
> *Stewart: Example 10.4.3*

^ex-66-3

## Arc Length

> [!theorem] Theorem §66.4: Arc Length of a Polar Curve
> Regarding $\theta$ as a parameter, the polar curve $r = f(\theta)$ has the parametric equations
>
> $$
> x = r\cos\theta = f(\theta)\cos\theta, \qquad y = r\sin\theta = f(\theta)\sin\theta . \qquad (5)
> $$
>
> If $f'$ is continuous and the curve is traversed exactly once for $a \le \theta \le b$, its length is
>
> $$
> L = \int_a^b \sqrt{r^2 + \Big(\frac{dr}{d\theta}\Big)^2}\,d\theta . \qquad (6)
> $$
>
> *Stewart: 10.4, Equations 5 and Formula 6*

^thm-66-4

> [!proof]+ Proof
> Equations 5 are Equations 1 of [[§65 Polar Coordinates#^thm-65-2|Theorem §65.2]] with $r = f(\theta)$. Differentiating with respect to $\theta$ by the Product Rule,
>
> $$
> \frac{dx}{d\theta} = \frac{dr}{d\theta}\cos\theta - r\sin\theta, \qquad \frac{dy}{d\theta} = \frac{dr}{d\theta}\sin\theta + r\cos\theta .
> $$
>
> Squaring and adding, the cross terms $\mp 2r\frac{dr}{d\theta}\cos\theta\sin\theta$ cancel, and $\cos^2\theta + \sin^2\theta = 1$ gives
>
> $$
> \Big(\frac{dx}{d\theta}\Big)^2 + \Big(\frac{dy}{d\theta}\Big)^2 = \Big(\frac{dr}{d\theta}\Big)^2(\cos^2\theta + \sin^2\theta) + r^2(\sin^2\theta + \cos^2\theta) = \Big(\frac{dr}{d\theta}\Big)^2 + r^2 .
> $$
>
> Since $f'$ is continuous, so are $dx/d\theta$ and $dy/d\theta$, and Theorem §64.4 gives $L = \int_a^b \sqrt{(dx/d\theta)^2 + (dy/d\theta)^2}\,d\theta$, which is Formula 6.

^pf-66-4

*Uses:* [[§65 Polar Coordinates#^thm-65-2|§65.2]], [[§15 The Product and Quotient Rules|§15]] (Product Rule), [[§64 Calculus with Parametric Curves#^thm-64-4|§64.4]]

> [!example] Example §66.4: The Length of the Cardioid
> Find the length of the cardioid $r = 1 + \sin\theta$ ([[§65 Polar Coordinates#^ex-65-4|Example §65.4]]).
>
> The whole cardioid is traced once for $0 \le \theta \le 2\pi$, and $dr/d\theta = \cos\theta$. By Formula 6,
>
> $$
> L = \int_0^{2\pi} \sqrt{(1 + \sin\theta)^2 + \cos^2\theta}\,d\theta = \int_0^{2\pi} \sqrt{1 + 2\sin\theta + \sin^2\theta + \cos^2\theta}\,d\theta = \int_0^{2\pi} \sqrt{2 + 2\sin\theta}\,d\theta .
> $$
>
> Stewart evaluates this by multiplying and dividing by $\sqrt{2 - 2\sin\theta}$, or by software. A half-angle identity is quicker: $\sin\theta = \cos(\theta - \frac{\pi}{2})$ and $1 + \cos\varphi = 2\cos^2(\varphi/2)$ give $2 + 2\sin\theta = 4\cos^2\big(\frac{\theta}{2} - \frac{\pi}{4}\big)$. With $u = \frac{\theta}{2} - \frac{\pi}{4}$, $d\theta = 2\,du$, $u$ from $-\frac{\pi}{4}$ to $\frac{3\pi}{4}$:
>
> $$
> L = \int_{-\pi/4}^{3\pi/4} 2|\cos u| \cdot 2\,du = 4\Big[\int_{-\pi/4}^{\pi/2} \cos u\,du - \int_{\pi/2}^{3\pi/4} \cos u\,du\Big] = 4\Big[\Big(1 + \frac{\sqrt2}{2}\Big) + \Big(1 - \frac{\sqrt2}{2}\Big)\Big] = 8 .
> $$
>
> The absolute value matters: $\cos u < 0$ for $\frac{\pi}{2} < u \le \frac{3\pi}{4}$, which is the part of the cardioid near the cusp.
>
> *Stewart: Example 10.4.4*

^ex-66-4

## Tangents

> [!theorem] Theorem §66.5: Slope of a Polar Curve
> For the polar curve $r = f(\theta)$ with $f$ differentiable,
>
> $$
> \frac{dy}{dx} = \frac{\dfrac{dy}{d\theta}}{\dfrac{dx}{d\theta}} = \frac{\dfrac{dr}{d\theta}\sin\theta + r\cos\theta}{\dfrac{dr}{d\theta}\cos\theta - r\sin\theta} \qquad (7)
> $$
>
> wherever the denominator is not $0$. Horizontal tangents occur where $dy/d\theta = 0$ (provided $dx/d\theta \ne 0$), vertical tangents where $dx/d\theta = 0$ (provided $dy/d\theta \ne 0$). At the pole ($r = 0$),
>
> $$
> \frac{dy}{dx} = \tan\theta \qquad \text{if } \frac{dr}{d\theta} \ne 0 ,
> $$
>
> so the tangent line at the pole is the line through $O$ at the angle $\theta$ at which the curve reaches the pole.
>
> *Stewart: 10.4, Equation 7 (and text)*

^thm-66-5

> [!proof]+ Proof
> Apply [[§64 Calculus with Parametric Curves#^thm-64-1|Theorem §64.1]] to the parametric equations (5), with the derivatives $dx/d\theta$ and $dy/d\theta$ computed in the proof of Theorem §66.4 by the Product Rule. At the pole, put $r = 0$ in (7): $\dfrac{dy}{dx} = \dfrac{(dr/d\theta)\sin\theta}{(dr/d\theta)\cos\theta} = \tan\theta$ when $dr/d\theta \ne 0$ (and $\cos\theta \ne 0$; if $\cos\theta = 0$ then $dx/d\theta = 0 \ne dy/d\theta$ and the tangent is vertical, the line $\theta = \pi/2$). Either way the tangent at the pole is the line through $O$ at angle $\theta$.

^pf-66-5

*Uses:* [[§64 Calculus with Parametric Curves#^thm-64-1|§64.1]], [[§66 Calculus in Polar Coordinates#^thm-66-4|§66.4]], [[§15 The Product and Quotient Rules|§15]] (Product Rule)

For instance, $r = \cos 2\theta = 0$ at $\theta = \pi/4$ and $3\pi/4$, where $dr/d\theta = -2\sin 2\theta \ne 0$, so the lines $y = x$ and $y = -x$ are the tangent lines to the four-leaved rose at the origin.

> [!example] Example §66.5: Tangents to the Cardioid
> For $r = 1 + \sin\theta$: (a) find the slope of the tangent at $\theta = \pi/3$; (b) find the points where the tangent is horizontal or vertical.
>
> With $dr/d\theta = \cos\theta$, Equation 7 gives
>
> $$
> \frac{dy}{dx} = \frac{\cos\theta\sin\theta + (1 + \sin\theta)\cos\theta}{\cos\theta\cos\theta - (1 + \sin\theta)\sin\theta} = \frac{\cos\theta\,(1 + 2\sin\theta)}{1 - 2\sin^2\theta - \sin\theta} = \frac{\cos\theta\,(1 + 2\sin\theta)}{(1 + \sin\theta)(1 - 2\sin\theta)} ,
> $$
>
> using $\cos^2\theta = 1 - \sin^2\theta$ in the denominator.
>
> **(a)** At $\theta = \pi/3$, $\cos\theta = \frac12$ and $\sin\theta = \frac{\sqrt3}{2}$:
>
> $$
> \frac{dy}{dx}\Big|_{\theta = \pi/3} = \frac{\frac12(1 + \sqrt3)}{(1 + \frac{\sqrt3}{2})(1 - \sqrt3)} = \frac{1 + \sqrt3}{(2 + \sqrt3)(1 - \sqrt3)} = \frac{1 + \sqrt3}{-1 - \sqrt3} = -1 ,
> $$
>
> since $(2 + \sqrt3)(1 - \sqrt3) = 2 - 2\sqrt3 + \sqrt3 - 3 = -1 - \sqrt3$.
>
> **(b)** In $0 \le \theta < 2\pi$:
>
> $$
> \frac{dy}{d\theta} = \cos\theta\,(1 + 2\sin\theta) = 0 \ \text{ when } \theta = \frac{\pi}{2}, \frac{3\pi}{2}, \frac{7\pi}{6}, \frac{11\pi}{6};
> \qquad
> \frac{dx}{d\theta} = (1 + \sin\theta)(1 - 2\sin\theta) = 0 \ \text{ when } \theta = \frac{3\pi}{2}, \frac{\pi}{6}, \frac{5\pi}{6} .
> $$
>
> So there are horizontal tangents at $(2, \pi/2)$, $(\frac12, 7\pi/6)$, $(\frac12, 11\pi/6)$ and vertical tangents at $(\frac32, \pi/6)$, $(\frac32, 5\pi/6)$. At $\theta = 3\pi/2$ both derivatives vanish. By l'Hospital's Rule ([[§28 Indeterminate Forms and L'Hospital's Rule|§28]]),
>
> $$
> \lim_{\theta \to (3\pi/2)^-} \frac{dy}{dx} = \Big(\lim_{\theta \to (3\pi/2)^-} \frac{1 + 2\sin\theta}{1 - 2\sin\theta}\Big)\Big(\lim_{\theta \to (3\pi/2)^-} \frac{\cos\theta}{1 + \sin\theta}\Big) = -\frac13 \lim_{\theta \to (3\pi/2)^-} \frac{-\sin\theta}{\cos\theta} = \infty ,
> $$
>
> because $-\sin\theta \to 1$ and $\cos\theta \to 0$ through negative values. By symmetry, $dy/dx \to -\infty$ as $\theta \to (3\pi/2)^+$. So there is a vertical tangent at the pole, the cusp of the cardioid.
>
> Instead of Equation 7 one can redo its derivation: $x = (1 + \sin\theta)\cos\theta = \cos\theta + \frac12\sin 2\theta$ and $y = (1 + \sin\theta)\sin\theta = \sin\theta + \sin^2\theta$ give $\dfrac{dy}{dx} = \dfrac{\cos\theta + \sin 2\theta}{-\sin\theta + \cos 2\theta}$, an equivalent expression.
>
> *Stewart: Example 10.4.5*

^ex-66-5
