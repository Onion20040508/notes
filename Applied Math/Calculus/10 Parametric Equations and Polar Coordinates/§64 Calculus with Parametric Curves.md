---
type: section
subject: "[[Calculus]]"
chapter: 10
section: 64
stewart: "10.2"
aliases: ["Stewart 10.2"]
tags: [calculus]
---
← [[§63 Curves Defined by Parametric Equations]] · ↑ [[· 10 Parametric Equations and Polar Coordinates]] · [[§65 Polar Coordinates]] →

*Stewart, Section 10.2.*

The methods of calculus apply to parametric curves directly, without eliminating the parameter. The Chain Rule gives the slope $dy/dx$ as a ratio of two $t$-derivatives, and the Substitution Rule turns the area, arc length and surface area formulas of Chapters 5 and 8 into integrals in $t$. The arc length formula is also proved for curves that are not graphs, by approximating with polygons, and its integrand is the speed of a moving particle. The cycloid of [[§63 Curves Defined by Parametric Equations#^prop-63-2|Proposition §63.2]] serves as the running example.

## Tangents

> [!theorem] Theorem §64.1: Slope of a Parametric Curve
> Let $f$ and $g$ be differentiable and consider the curve $x = f(t)$, $y = g(t)$, where near the point $y$ is also a differentiable function of $x$ (this is automatic when $f'$ is continuous and $dx/dt \ne 0$; see the proof). At a point where $dx/dt \ne 0$,
>
> $$
> \frac{dy}{dx} = \frac{dy/dt}{dx/dt} .
> $$
>
> So the curve has a **horizontal tangent** where $dy/dt = 0$ (provided $dx/dt \ne 0$) and a **vertical tangent** where $dx/dt = 0$ (provided $dy/dt \ne 0$). If both derivatives vanish, other methods are needed (Example §64.2).
>
> *Stewart: 10.2, Formula 1*

^thm-64-1

> [!remark] Remark: Why It Works
> Think of the curve as traced by a moving particle. Then $dx/dt$ and $dy/dt$ are its horizontal and vertical velocities, and the slope of the tangent is the ratio of these velocities. The formula is easy to remember by "cancelling the $dt$'s".

^rem-64-1

> [!proof]+ Proof
> Stewart assumes that $y$ is also a differentiable function of $x$ near the point. (Stewart asserts this; here is why it holds when $f'$ is continuous: since $f'(t_0) \ne 0$, $f'$ has constant sign on an interval around $t_0$, so $f$ is one-to-one there with a differentiable inverse, $t = f^{-1}(x)$ ([[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-1|Theorem §19.1]]), and $y = g(f^{-1}(x))$ is differentiable by the Chain Rule.) Then $y = g(t)$ is the composite of $y$ as a function of $x$ with $x = f(t)$, and the Chain Rule ([[§17 The Chain Rule#^thm-17-2|Theorem §17.2]]) gives
>
> $$
> \frac{dy}{dt} = \frac{dy}{dx} \cdot \frac{dx}{dt} .
> $$
>
> Since $dx/dt \ne 0$, we can divide by it. The tangent is horizontal exactly when $dy/dx = 0$, that is, when $dy/dt = 0$. Where $dx/dt = 0$ but $dy/dt \ne 0$, $|dy/dx| \to \infty$ as $t \to t_0$ (if $f'$ and $g'$ are continuous), which is a vertical tangent.

^pf-64-1

*Uses:* [[§17 The Chain Rule#^thm-17-2|§17.2]] (Chain Rule), [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-1|§19.1]] (derivative of an inverse function)

> [!remark]- Connections
> - The inverse function step, rigorously: [[§29 The Mean Value Theorem#^thm-29-10|451 Thm. §29.10]]. The tangent line is the image of the derivative of the map $t \mapsto (f(t), g(t))$; on manifolds this is the velocity of a curve, [[§29 Tangent Vectors as Velocities of Curves#^def-29-1|591 Def. §29.1]].

> [!theorem] Theorem §64.2: Second Derivative of a Parametric Curve
> Where $dx/dt \ne 0$ and $dy/dx$ is a differentiable function of $t$,
>
> $$
> \frac{d^2y}{dx^2} = \frac{d}{dx}\Big(\frac{dy}{dx}\Big) = \frac{\dfrac{d}{dt}\Big(\dfrac{dy}{dx}\Big)}{\dfrac{dx}{dt}} .
> $$
>
> Note that $\dfrac{d^2y}{dx^2} \ne \dfrac{d^2y/dt^2}{d^2x/dt^2}$ in general.
>
> *Stewart: 10.2 (boxed formula after Formula 1)*

^thm-64-2

> [!proof]+ Proof
> Apply Theorem §64.1 to the curve $x = f(t)$, $Y = \dfrac{dy}{dx}$ (as a function of $t$) in place of $y$: then $\dfrac{dY}{dx} = \dfrac{dY/dt}{dx/dt}$, and $\dfrac{dY}{dx} = \dfrac{d^2y}{dx^2}$.

^pf-64-2

*Uses:* [[§64 Calculus with Parametric Curves#^thm-64-1|§64.1]]

> [!example] Example §64.1: A Curve That Crosses Itself
> The curve $C$ is given by $x = t^2$, $y = t^3 - 3t$.
>
> **(a) Two tangents at $(3, 0)$.** $x = 3$ for $t = \pm\sqrt3$, and in both cases $y = t(t^2 - 3) = 0$. So $C$ passes through $(3, 0)$ twice: it crosses itself there. By Theorem §64.1,
>
> $$
> \frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{3t^2 - 3}{2t} .
> $$
>
> At $t = \sqrt3$ the slope is $\dfrac{9 - 3}{2\sqrt3} = \dfrac{6}{2\sqrt3} = \sqrt3$, and at $t = -\sqrt3$ it is $\dfrac{6}{-2\sqrt3} = -\sqrt3$. So there are two tangent lines at $(3, 0)$:
>
> $$
> y = \sqrt3\,(x - 3) \qquad\text{and}\qquad y = -\sqrt3\,(x - 3) .
> $$
>
> **(b) Horizontal and vertical tangents.** $dy/dt = 3t^2 - 3 = 0$ when $t = \pm1$, where $dx/dt = \pm 2 \ne 0$: horizontal tangents at $t = 1$, the point $(1, -2)$, and at $t = -1$, the point $(1, 2)$. $dx/dt = 2t = 0$ when $t = 0$, where $dy/dt = -3 \ne 0$: a vertical tangent at $(0, 0)$.
>
> **(c) Concavity.** By Theorem §64.2,
>
> $$
> \frac{d^2y}{dx^2} = \frac{\dfrac{d}{dt}\Big(\dfrac{3t^2 - 3}{2t}\Big)}{2t} = \frac{\dfrac{d}{dt}\Big(\dfrac{3t}{2} - \dfrac{3}{2t}\Big)}{2t} = \frac{\dfrac32 + \dfrac{3}{2t^2}}{2t} = \frac{3t^2 + 3}{4t^3} .
> $$
>
> The numerator is positive, so the curve is concave upward for $t > 0$ and concave downward for $t < 0$.
>
> **(d) Sketch.** Replacing $t$ by $-t$ keeps $x$ and changes the sign of $y$, so $C$ is symmetric about the $x$-axis. For $-\sqrt3 \le t \le \sqrt3$ the curve makes a loop: from $(3, 0)$ up to $(1, 2)$, around through the vertical tangent at $(0, 0)$, down to $(1, -2)$ and back to $(3, 0)$, counterclockwise. For $|t| > \sqrt3$ the two branches run off to the right, to $y \to \pm\infty$.
>
> *Stewart: Example 10.2.1*

^ex-64-1

![[m233-64-1.svg]]
*The curve $x = t^2$, $y = t^3 - 3t$ of Example §64.1. The loop is traced counterclockwise for $-\sqrt3 \le t \le \sqrt3$, and the curve passes through $(3, 0)$ twice, at $t = -\sqrt3$ and $t = \sqrt3$, with the two tangents $y = \pm\sqrt3(x - 3)$ (red). Horizontal tangents at $t = \pm1$ and the vertical tangent at $t = 0$ are where $dy/dt = 0$ and $dx/dt = 0$.*

> [!example] Example §64.2: Tangents to the Cycloid
> Consider the cycloid $x = r(\theta - \sin\theta)$, $y = r(1 - \cos\theta)$ ([[§63 Curves Defined by Parametric Equations#^prop-63-2|Proposition §63.2]]).
>
> **(a) The tangent at $\theta = \pi/3$.** By Theorem §64.1,
>
> $$
> \frac{dy}{dx} = \frac{dy/d\theta}{dx/d\theta} = \frac{r\sin\theta}{r(1 - \cos\theta)} = \frac{\sin\theta}{1 - \cos\theta} .
> $$
>
> At $\theta = \pi/3$:
>
> $$
> x = r\Big(\frac{\pi}{3} - \frac{\sqrt3}{2}\Big), \qquad y = r\Big(1 - \frac12\Big) = \frac r2, \qquad \frac{dy}{dx} = \frac{\sqrt3/2}{1 - \frac12} = \sqrt3 .
> $$
>
> The tangent line is
>
> $$
> y - \frac r2 = \sqrt3\Big(x - \frac{r\pi}{3} + \frac{r\sqrt3}{2}\Big), \qquad\text{that is,}\qquad \sqrt3\,x - y = r\Big(\frac{\pi}{\sqrt3} - 2\Big),
> $$
>
> since $\sqrt3 \cdot r\big(\frac{\pi}{3} - \frac{\sqrt3}{2}\big) - \frac r2 = r\big(\frac{\pi}{\sqrt3} - \frac32 - \frac12\big)$.
>
> **(b) Horizontal tangents.** $dy/dx = 0$ when $\sin\theta = 0$ and $1 - \cos\theta \ne 0$, that is, $\theta = (2n - 1)\pi$ with $n$ an integer. These are the tops of the arches, $\big((2n - 1)\pi r,\ 2r\big)$.
>
> **(c) Vertical tangents.** At $\theta = 2n\pi$ both $dx/d\theta = r(1 - \cos\theta)$ and $dy/d\theta = r\sin\theta$ are $0$, so Theorem §64.1 says nothing. Compute the limit of the slope instead, by l'Hospital's Rule ([[§28 Indeterminate Forms and L'Hospital's Rule#^thm-28-2|Theorem §28.2]]; the quotient has the form $0/0$):
>
> $$
> \lim_{\theta \to 2n\pi^+} \frac{dy}{dx} = \lim_{\theta \to 2n\pi^+} \frac{\sin\theta}{1 - \cos\theta} = \lim_{\theta \to 2n\pi^+} \frac{\cos\theta}{\sin\theta} = \infty ,
> $$
>
> because $\cos\theta \to 1$ and $\sin\theta \to 0$ through positive values. In the same way $dy/dx \to -\infty$ as $\theta \to 2n\pi^-$. So the cycloid has vertical tangents at $x = 2n\pi r$, where it touches the $x$-axis: the cusps between arches.
>
> *Stewart: Example 10.2.2*

^ex-64-2

## Areas

> [!theorem] Theorem §64.3: Area Under a Parametric Curve
> Suppose the curve $y = F(x)$, $a \le x \le b$, with $F(x) \ge 0$, is traced out once by $x = f(t)$, $y = g(t)$, $\alpha \le t \le \beta$, with $f'$ continuous. Then the area under it is
>
> $$
> A = \int_a^b y\,dx = \int_\alpha^\beta g(t) f'(t)\,dt \qquad \Big[\text{or } \int_\beta^\alpha g(t) f'(t)\,dt\Big] .
> $$
>
> The limits in $t$ are found as in any substitution: when $x = a$, $t$ is $\alpha$ or $\beta$, and when $x = b$, $t$ is the other one.
>
> *Stewart: 10.2 (text)*

^thm-64-3

> [!proof]+ Proof
> The area is $A = \int_a^b F(x)\,dx$ ([[§35 The Definite Integral#^rem-35-1|§35, Remark: The Integral as a Net Area]]). Since the curve is traced once, $x = f(t)$ runs through $[a, b]$ once, and the points of the curve are $(f(t), g(t)) = (f(t), F(f(t)))$, so $g(t) = F(f(t))$.
>
> If $f(\alpha) = a$ and $f(\beta) = b$, the Substitution Rule for Definite Integrals ([[§38 The Substitution Rule#^thm-38-3|Theorem §38.3]]) with $x = f(t)$, $dx = f'(t)\,dt$ gives
>
> $$
> \int_a^b F(x)\,dx = \int_\alpha^\beta F(f(t))\,f'(t)\,dt = \int_\alpha^\beta g(t) f'(t)\,dt .
> $$
>
> If instead $f(\beta) = a$ and $f(\alpha) = b$ (the curve is traced from right to left), the same substitution gives $\int_\beta^\alpha g(t) f'(t)\,dt$.

^pf-64-3

*Uses:* [[§35 The Definite Integral#^rem-35-1|§35, Remark: The Integral as a Net Area]] (area as an integral), [[§38 The Substitution Rule#^thm-38-3|§38.3]] (Substitution Rule for definite integrals)

## Arc Length

> [!theorem] Theorem §64.4: Arc Length of a Parametric Curve
> If a curve $C$ is described by the parametric equations $x = f(t)$, $y = g(t)$, $\alpha \le t \le \beta$, where $f'$ and $g'$ are continuous on $[\alpha, \beta]$ and $C$ is traversed exactly once as $t$ increases from $\alpha$ to $\beta$, then the length of $C$ is
>
> $$
> L = \int_\alpha^\beta \sqrt{\Big(\frac{dx}{dt}\Big)^2 + \Big(\frac{dy}{dt}\Big)^2}\,dt .
> $$
>
> *Stewart: 10.2, Theorem 5 (and Formula 3)*

^thm-64-4

> [!proof]+ Proof
> **A special case (Formula 3).** Suppose $C$ is also a graph $y = F(x)$, $a \le x \le b$, with $F'$ continuous, and that $dx/dt = f'(t) > 0$, so $C$ is traversed once from left to right with $f(\alpha) = a$, $f(\beta) = b$. By Formula 8.1.3 ([[§52 Arc Length#^thm-52-1|Theorem §52.1]]), $L = \int_a^b \sqrt{1 + (dy/dx)^2}\,dx$. Substitute $x = f(t)$ and use Theorem §64.1:
>
> $$
> L = \int_\alpha^\beta \sqrt{1 + \Big(\frac{dy/dt}{dx/dt}\Big)^2}\,\frac{dx}{dt}\,dt = \int_\alpha^\beta \sqrt{\Big(\frac{dx}{dt}\Big)^2 + \Big(\frac{dy}{dt}\Big)^2}\,dt ,
> $$
>
> where $dx/dt > 0$ was moved inside the square root as $\sqrt{(dx/dt)^2}$.
>
> **The general case.** Even if $C$ is not a graph, the formula holds; we prove it from the definition of length by polygonal approximation ([[§52 Arc Length#^def-52-1|Definition §52.1]]). Divide $[\alpha, \beta]$ into $n$ subintervals of equal width $\Delta t$ with endpoints $t_0, t_1, \ldots, t_n$. The points $P_i = (f(t_i), g(t_i))$ lie on $C$, and the polygonal path $P_0 P_1 \cdots P_n$ approximates $C$. The length of $C$ is
>
> $$
> L = \lim_{n \to \infty} \sum_{i=1}^n |P_{i-1} P_i| .
> $$
>
> The Mean Value Theorem ([[§26 The Mean Value Theorem#^thm-26-2|Theorem §26.2]]) applied to $f$ and to $g$ on $[t_{i-1}, t_i]$ gives numbers $t_i^*$ and $t_i^{**}$ in $(t_{i-1}, t_i)$ with
>
> $$
> \Delta x_i = f(t_i) - f(t_{i-1}) = f'(t_i^*)\,\Delta t, \qquad \Delta y_i = g(t_i) - g(t_{i-1}) = g'(t_i^{**})\,\Delta t .
> $$
>
> Therefore
>
> $$
> |P_{i-1} P_i| = \sqrt{(\Delta x_i)^2 + (\Delta y_i)^2} = \sqrt{[f'(t_i^*)]^2 + [g'(t_i^{**})]^2}\;\Delta t ,
> \qquad
> L = \lim_{n \to \infty} \sum_{i=1}^n \sqrt{[f'(t_i^*)]^2 + [g'(t_i^{**})]^2}\;\Delta t . \qquad (4)
> $$
>
> The sum in (4) resembles a Riemann sum for $h(t) = \sqrt{[f'(t)]^2 + [g'(t)]^2}$, but it is not one, because $t_i^* \ne t_i^{**}$ in general. Stewart states that "it can be shown" that the limit is the same as if $t_i^*$ and $t_i^{**}$ were equal; here is why. For real numbers $a, b, c$,
>
> $$
> \Big|\sqrt{a^2 + b^2} - \sqrt{a^2 + c^2}\Big| \le |b - c| ,
> $$
>
> because the left side is the difference of the distances from the origin to $(a, b)$ and to $(a, c)$, and by the triangle inequality this is at most the distance $|b - c|$ between the two points. Hence the sum in (4) differs from the Riemann sum $R_n = \sum_{i=1}^n h(t_i^*)\,\Delta t$ by at most
>
> $$
> \sum_{i=1}^n |g'(t_i^{**}) - g'(t_i^*)|\,\Delta t .
> $$
>
> Since $g'$ is continuous on the closed interval $[\alpha, \beta]$, it is uniformly continuous: for every $\varepsilon > 0$ there is $\delta > 0$ with $|g'(s) - g'(u)| < \varepsilon$ whenever $|s - u| < \delta$. Once $\Delta t < \delta$, the points $t_i^*$ and $t_i^{**}$ lie in the same subinterval, so the difference is less than $\sum \varepsilon\,\Delta t = \varepsilon(\beta - \alpha)$. Thus the sum in (4) and $R_n$ have the same limit. Since $h$ is continuous, it is integrable ([[§35 The Definite Integral#^thm-35-1|Theorem §35.1]]), so $R_n \to \int_\alpha^\beta h(t)\,dt$ ([[§35 The Definite Integral#^def-35-1|Definition §35.1]]), which is the formula.
>
> Where was "traversed exactly once" used? The polygonal paths approximate $C$ only if the points $P_i$ run along $C$ once, in order; if part of $C$ is traced twice, the polygons and the integral both count it twice (Remark below).

^pf-64-4

*Uses:* [[§52 Arc Length#^thm-52-1|§52.1]] (Formula 8.1.3), [[§52 Arc Length#^def-52-1|Def. §52.1]] (length as a limit of polygonal paths), [[§64 Calculus with Parametric Curves#^thm-64-1|§64.1]], [[§38 The Substitution Rule#^thm-38-3|§38.3]], [[§26 The Mean Value Theorem#^thm-26-2|§26.2]], [[§35 The Definite Integral#^thm-35-1|§35.1]], [[§35 The Definite Integral#^def-35-1|Def. §35.1]] (Riemann sums of a continuous function); uniform continuity [[§19 Uniform Continuity#^thm-19-1|451 Thm. §19.1]]

> [!remark]- Connections
> - The same polygonal derivation, with the same Mean Value Theorem step and uniform-continuity estimate, gives the scalar line integral in 452: [[§16 Line Integrals and Green's Theorem#^def-16-1|452 Def. §16.1]] (the arc length is the case $f = 1$).

> [!remark] Remark: The Curve Must Be Traversed Once
> The unit circle $x = \cos t$, $y = \sin t$, $0 \le t \le 2\pi$ ([[§63 Curves Defined by Parametric Equations#^ex-63-2|Example §63.2]](a)) has $dx/dt = -\sin t$, $dy/dt = \cos t$, and
>
> $$
> L = \int_0^{2\pi} \sqrt{\sin^2 t + \cos^2 t}\,dt = \int_0^{2\pi} dt = 2\pi ,
> $$
>
> as expected. With $x = \sin 2t$, $y = \cos 2t$, $0 \le t \le 2\pi$ (Example §63.2(b)), $dx/dt = 2\cos 2t$, $dy/dt = -2\sin 2t$, and the integral is
>
> $$
> \int_0^{2\pi} \sqrt{4\cos^2 2t + 4\sin^2 2t}\,dt = \int_0^{2\pi} 2\,dt = 4\pi ,
> $$
>
> twice the circumference, because this parametrization goes around the circle twice. Before using Theorem §64.4, check that $C$ is traversed only once as $t$ runs from $\alpha$ to $\beta$.

^rem-64-2

> [!example] Example §64.3: Area and Length of One Arch of the Cycloid
> One arch of the cycloid $x = r(\theta - \sin\theta)$, $y = r(1 - \cos\theta)$ is traced once for $0 \le \theta \le 2\pi$, from $x = 0$ to $x = 2\pi r$, with $dx/d\theta = r(1 - \cos\theta) \ge 0$ and $dy/d\theta = r\sin\theta$.
>
> **Area under the arch.** By Theorem §64.3, with $y = r(1 - \cos\theta)$ and $dx = r(1 - \cos\theta)\,d\theta$,
>
> $$
> \begin{aligned}
> A &= \int_0^{2\pi r} y\,dx = \int_0^{2\pi} r(1 - \cos\theta)\,r(1 - \cos\theta)\,d\theta = r^2 \int_0^{2\pi} (1 - 2\cos\theta + \cos^2\theta)\,d\theta \\
> &= r^2 \int_0^{2\pi} \Big[1 - 2\cos\theta + \tfrac12(1 + \cos 2\theta)\Big]\,d\theta
> = r^2 \Big[\tfrac32\theta - 2\sin\theta + \tfrac14\sin 2\theta\Big]_0^{2\pi} = r^2 \cdot \tfrac32 \cdot 2\pi = 3\pi r^2 .
> \end{aligned}
> $$
>
> This is three times the area of the rolling circle. (Galileo guessed it; Roberval and Torricelli first proved it.)
>
> **Length of the arch.** By Theorem §64.4,
>
> $$
> L = \int_0^{2\pi} \sqrt{r^2(1 - \cos\theta)^2 + r^2\sin^2\theta}\,d\theta = \int_0^{2\pi} \sqrt{r^2(1 - 2\cos\theta + \cos^2\theta + \sin^2\theta)}\,d\theta = r\int_0^{2\pi} \sqrt{2(1 - \cos\theta)}\,d\theta .
> $$
>
> The half-angle identity $\sin^2 u = \frac12(1 - \cos 2u)$ with $\theta = 2u$ gives $1 - \cos\theta = 2\sin^2(\theta/2)$. For $0 \le \theta \le 2\pi$ we have $0 \le \theta/2 \le \pi$, so $\sin(\theta/2) \ge 0$ and
>
> $$
> \sqrt{2(1 - \cos\theta)} = \sqrt{4\sin^2(\theta/2)} = 2|\sin(\theta/2)| = 2\sin(\theta/2) .
> $$
>
> Therefore
>
> $$
> L = 2r\int_0^{2\pi} \sin(\theta/2)\,d\theta = 2r\Big[-2\cos(\theta/2)\Big]_0^{2\pi} = 2r\,[2 + 2] = 8r ,
> $$
>
> eight times the radius of the generating circle (first proved by Christopher Wren in 1658).
>
> *Stewart: Examples 10.2.3 and 10.2.5*

^ex-64-3

### The Arc Length Function and Speed

> [!definition] Definition §64.1: Arc Length Function and Arc Length Element
> Let $C$ be given by $x = f(t)$, $y = g(t)$ with $f'$ and $g'$ continuous. The **arc length function** $s(t)$ is the length of $C$ from the initial point $(f(\alpha), g(\alpha))$ to the point $(f(t), g(t))$. By Theorem §64.4,
>
> $$
> s(t) = \int_\alpha^t \sqrt{\Big(\frac{dx}{du}\Big)^2 + \Big(\frac{dy}{du}\Big)^2}\,du
> $$
>
> (the variable of integration is renamed $u$ so that $t$ does not have two meanings). The **arc length element** is
>
> $$
> ds = \sqrt{\Big(\frac{dx}{dt}\Big)^2 + \Big(\frac{dy}{dt}\Big)^2}\,dt ,
> $$
>
> so that Theorem §64.4 reads $L = \int ds$, as in [[§52 Arc Length#^def-52-4|Definition §52.4]]; $s(t)$ is the parametric form of the arc length function [[§52 Arc Length#^def-52-3|Definition §52.3]] (Formula 8.1.5).
>
> *Stewart: 10.2, Equations 6 and 7*

^def-64-1

> [!definition] Definition §64.2: Speed
> If $x = f(t)$, $y = g(t)$ is the position of a moving particle at time $t$, its **speed** $v(t)$ at time $t$ is the rate of change of distance traveled (arc length) with respect to time: $v(t) = s'(t)$.
>
> *Stewart: 10.2 (text)*

^def-64-2

> [!theorem] Theorem §64.5: Speed Along a Parametric Curve
> If $f'$ and $g'$ are continuous, the speed of the particle at $(f(t), g(t))$ is
>
> $$
> v(t) = s'(t) = \sqrt{\Big(\frac{dx}{dt}\Big)^2 + \Big(\frac{dy}{dt}\Big)^2} .
> $$
>
> *Stewart: 10.2, Equation 8*

^thm-64-5

> [!proof]+ Proof
> The integrand $u \mapsto \sqrt{f'(u)^2 + g'(u)^2}$ in Definition §64.1 is continuous, so by Part 1 of the Fundamental Theorem of Calculus ([[§36 The Fundamental Theorem of Calculus#^thm-36-1|Theorem §36.1]]) $s$ is differentiable with $s'(t) = \sqrt{f'(t)^2 + g'(t)^2}$.

^pf-64-5

*Uses:* [[§64 Calculus with Parametric Curves#^def-64-1|Def. §64.1]], [[§64 Calculus with Parametric Curves#^def-64-2|Def. §64.2]], [[§36 The Fundamental Theorem of Calculus#^thm-36-1|§36.1]] (FTC Part 1)

> [!example] Example §64.4: The Speed of a Particle
> A particle has position $x = 2t + 3$, $y = 4t^2$, $t \ge 0$. Find its speed when it is at $(5, 4)$.
>
> By Theorem §64.5, $v(t) = \sqrt{2^2 + (8t)^2} = \sqrt{4(1 + 16t^2)} = 2\sqrt{1 + 16t^2}$. The particle is at $(5, 4)$ when $2t + 3 = 5$, that is $t = 1$ (and indeed $4 \cdot 1^2 = 4$). So its speed there is $v(1) = 2\sqrt{17} \approx 8.25$ (in m/s, if distance is in meters and time in seconds).
>
> *Stewart: Example 10.2.6*

^ex-64-4

## Surface Area

> [!theorem] Theorem §64.6: Surface Area for a Parametric Curve
> Suppose $C$ is given by $x = f(t)$, $y = g(t)$, $\alpha \le t \le \beta$, where $f'$ and $g'$ are continuous, $g(t) \ge 0$, and $C$ is traversed exactly once as $t$ increases from $\alpha$ to $\beta$. The area of the surface obtained by rotating $C$ about the $x$-axis is
>
> $$
> S = \int_\alpha^\beta 2\pi y \sqrt{\Big(\frac{dx}{dt}\Big)^2 + \Big(\frac{dy}{dt}\Big)^2}\,dt .
> $$
>
> The symbolic formulas $S = \int 2\pi y\,ds$ (rotation about the $x$-axis) and $S = \int 2\pi x\,ds$ (rotation about the $y$-axis, for $x \ge 0$) of [[§53 Area of a Surface of Revolution#^thm-53-3|Theorem §53.3]] (Formulas 8.2.7 and 8.2.8) remain valid, with $ds$ as in Definition §64.1.
>
> *Stewart: 10.2, Formula 9*

^thm-64-6

> [!proof]+ Proof
> *Stewart gives this as a sketch* ("in the same way as for arc length"). In the case where $dx/dt > 0$, so that $C$ is a graph $y = F(x)$, $a \le x \le b$, traversed from left to right, start from Formula 8.2.5 ([[§53 Area of a Surface of Revolution#^def-53-2|Definition §53.2]]),
>
> $$
> S = \int_a^b 2\pi y \sqrt{1 + \Big(\frac{dy}{dx}\Big)^2}\,dx ,
> $$
>
> and substitute $x = f(t)$ exactly as in the special case of the proof of Theorem §64.4: $\sqrt{1 + (dy/dx)^2}\,\dfrac{dx}{dt} = \sqrt{(dx/dt)^2 + (dy/dt)^2}$ because $dx/dt > 0$. This gives Formula 9. For a general curve the formula comes from approximating $C$ by polygonal paths and the surface by the bands (frustums of cones) that the segments sweep out, as in [[§53 Area of a Surface of Revolution#^thm-53-1|Theorem §53.1]] and Definition §53.2, with the Mean Value Theorem step of the proof of Theorem §64.4; Stewart does not carry this out.

^pf-64-6

*Uses:* [[§53 Area of a Surface of Revolution#^def-53-2|Def. §53.2]] (Formula 8.2.5), [[§64 Calculus with Parametric Curves#^thm-64-1|§64.1]], [[§64 Calculus with Parametric Curves#^thm-64-4|§64.4]], [[§38 The Substitution Rule#^thm-38-3|§38.3]]

> [!example] Example §64.5: The Surface Area of a Sphere
> Show that the surface area of a sphere of radius $r$ is $4\pi r^2$.
>
> The sphere is obtained by rotating the upper semicircle $x = r\cos t$, $y = r\sin t$, $0 \le t \le \pi$, about the $x$-axis. It is traversed once, and $y = r\sin t \ge 0$. By Theorem §64.6,
>
> $$
> \begin{aligned}
> S &= \int_0^\pi 2\pi r\sin t\,\sqrt{(-r\sin t)^2 + (r\cos t)^2}\,dt = 2\pi\int_0^\pi r\sin t\,\sqrt{r^2(\sin^2 t + \cos^2 t)}\,dt \\
> &= 2\pi\int_0^\pi r\sin t \cdot r\,dt = 2\pi r^2 \int_0^\pi \sin t\,dt = 2\pi r^2 \Big[-\cos t\Big]_0^\pi = 2\pi r^2 \cdot 2 = 4\pi r^2 .
> \end{aligned}
> $$
>
> *Stewart: Example 10.2.7*

^ex-64-5
