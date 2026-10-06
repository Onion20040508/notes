---
type: section
subject: "[[Calculus]]"
chapter: 10
section: 73
stewart: "10.1"
aliases: ["Stewart 10.1"]
tags: [calculus]
---
← [[§72 The RL Circuit]] · ↑ [[· 10 Parametric Equations and Polar Coordinates]] · [[§74 Calculus with Parametric Curves]] →

*Stewart, Section 10.1 · reviewed in MATH 233 (UMass, Spring 2023), with Chapter 13.*

Many curves are not graphs $y = f(x)$: a circle, or the path of a particle that loops back on itself, fails the Vertical Line Test ([[§1 Four Ways to Represent a Function#^thm-1-1|Theorem §1.1]]). Instead, both coordinates are given as functions of a third variable $t$, the parameter. A parametrization says more than the curve does: it also says where the point is at each time and in which direction it moves, so the same curve can be traced in many ways. This section sets up the language, shows how to identify a parametric curve by eliminating the parameter, and derives the parametric equations of the cycloid. Calculus with parametric curves follows in [[§74 Calculus with Parametric Curves|§74]]; in three dimensions the same idea becomes the vector function of [[§100 Vector Functions and Space Curves#^def-100-1|Definition §100.1]].

## Parametric Equations

> [!definition] Definition §73.1: Parametric Equations and Parametric Curve
> Suppose that $x$ and $y$ are both given as functions of a third variable $t$, called a **parameter**, by the equations
>
> $$
> x = f(t), \qquad y = g(t),
> $$
>
> called **parametric equations**. Each value of $t$ determines a point $(x, y) = (f(t), g(t))$ in the plane. As $t$ varies, this point traces out a **parametric curve**.
>
> The parameter need not represent time, and any letter may be used for it. When $t$ is time, $(f(t), g(t))$ is the position of a moving object at time $t$.
>
> *Stewart: 10.1 (text)*

^def-73-1

> [!definition] Definition §73.2: Initial and Terminal Point
> If $t$ is restricted to an interval, the curve
>
> $$
> x = f(t), \qquad y = g(t), \qquad a \le t \le b
> $$
>
> has **initial point** $(f(a), g(a))$ and **terminal point** $(f(b), g(b))$. The direction in which the curve is traced as $t$ increases is marked by arrowheads.
>
> *Stewart: 10.1 (text)*

^def-73-2

> [!remark] Remark: Method — Eliminating the Parameter
> To identify a parametric curve $x = f(t)$, $y = g(t)$:
> 1. Find an equation in $x$ and $y$ alone that every point $(f(t), g(t))$ satisfies: solve one equation for $t$ and substitute into the other, or use an identity such as $\cos^2 t + \sin^2 t = 1$.
> 2. This shows only that the parametric curve lies *on* the graph of that equation. Determine which part of the graph is actually traced, from the ranges of $f$ and $g$ on the allowed values of $t$.
> 3. Determine the direction of motion (and whether parts are traced more than once) from how $x$ and $y$ change as $t$ increases; plotting a few points helps.
>
> The Cartesian equation describes the road; the parametric equations also track the car on it. Information is lost in step 1, which is why steps 2 and 3 are needed. Not every parametric curve can be described by an equation in $x$ and $y$ at all.

^rem-73-1

> [!example] Example §73.1: A Parabola Traced from Bottom to Top
> Sketch and identify the curve $x = t^2 - 2t$, $y = t + 1$.
>
> **Plotting points.**
>
> | $t$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ |
> |---|---|---|---|---|---|---|---|
> | $x$ | $8$ | $3$ | $0$ | $-1$ | $0$ | $3$ | $8$ |
> | $y$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
>
> As $t$ increases the point moves upward ($y = t + 1$ increases), first to the left and then, after $t = 1$, to the right. Equal steps in $t$ do not give equal distances on the curve: the particle slows down near $(-1, 2)$ and then speeds up.
>
> **Eliminating the parameter.** From the second equation $t = y - 1$, so
>
> $$
> x = t^2 - 2t = (y - 1)^2 - 2(y - 1) = y^2 - 4y + 3 .
> $$
>
> Every point of the parametric curve lies on the parabola $x = y^2 - 4y + 3$ (axis horizontal, vertex $(-1, 2)$). Since $t$ can be chosen to make $y = t + 1$ any real number, the parametric curve is the whole parabola.
>
> Restricting to $0 \le t \le 4$ gives only the arc from the initial point $(0, 1)$ to the terminal point $(8, 5)$ ([[§73 Curves Defined by Parametric Equations#^def-73-2|Definition §73.2]]).
>
> *Stewart: Example 10.1.1*

^ex-73-1

> [!example] Example §73.2: The Unit Circle, Traced Two Ways
> **(a)** $x = \cos t$, $y = \sin t$, $0 \le t \le 2\pi$. For every $t$,
>
> $$
> x^2 + y^2 = \cos^2 t + \sin^2 t = 1 ,
> $$
>
> so the point moves on the unit circle. Here $t$ is the angle from the positive $x$-axis to the point, so as $t$ increases from $0$ to $2\pi$ the point goes once around the circle **counterclockwise**, starting and ending at $(1, 0)$.
>
> **(b)** $x = \sin 2t$, $y = \cos 2t$, $0 \le t \le 2\pi$. Again $x^2 + y^2 = \sin^2 2t + \cos^2 2t = 1$, the unit circle. But now the point starts at $(\sin 0, \cos 0) = (0, 1)$. At $t = \pi/4$ it is at $(1, 0)$, so it moves **clockwise**, and since $2t$ runs from $0$ to $4\pi$ it goes around **twice**.
>
> *Stewart: Examples 10.1.2 and 10.1.3*

^ex-73-2

> [!definition] Definition §73.3: Curve versus Parametric Curve
> A **curve** is a set of points. A **parametric curve** is a curve together with a particular way of tracing out its points: different parametric equations can represent the same curve, as in [[§73 Curves Defined by Parametric Equations#^ex-73-2|Example §73.2]].
>
> *Stewart: 10.1, Note*

^def-73-3

> [!remark]- Connections
> - With $f$ and $g$ continuous on $[a, b]$, a parametric curve is a path in the sense of topology, a continuous map $[a, b] \to \mathbb{R}^2$ ([[§16 Connected Subspaces of ℝ#^def-16-3|590 Def. §16.3]]); the curve is its image. Smooth curves on manifolds: [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|591 Def. §31.2]].

> [!theorem] Proposition §73.1: Parametric Equations of a Circle
> The circle with center $(h, k)$ and radius $r$ is traced once counterclockwise, starting from $(h + r, k)$, by
>
> $$
> x = h + r\cos t, \qquad y = k + r\sin t, \qquad 0 \le t \le 2\pi .
> $$
>
> *Stewart: Example 10.1.4*

^prop-73-1

> [!proof]+ Proof
> Multiplying the equations of [[§73 Curves Defined by Parametric Equations#^ex-73-2|Example §73.2]](a) by $r$ gives $x = r\cos t$, $y = r\sin t$, with $x^2 + y^2 = r^2(\cos^2 t + \sin^2 t) = r^2$: the circle of radius $r$ about the origin, traced counterclockwise from $(r, 0)$. Shifting by $h$ in the $x$-direction and $k$ in the $y$-direction moves the center to $(h, k)$:
>
> $$
> (x - h)^2 + (y - k)^2 = r^2\cos^2 t + r^2\sin^2 t = r^2 .
> $$
>
> Conversely, every point of this circle is reached: if $(x - h)^2 + (y - k)^2 = r^2$, then $\big(\tfrac{x-h}{r}, \tfrac{y-k}{r}\big)$ is on the unit circle and so equals $(\cos t, \sin t)$ for some $t \in [0, 2\pi)$, the angle of that point ([[§142 Trigonometry#^def-142-4|Definition §142.4]] with $r = 1$). The direction and starting point are those of [[§73 Curves Defined by Parametric Equations#^ex-73-2|Example §73.2]](a), shifted.

^pf-73-1

*Uses:* [[§73 Curves Defined by Parametric Equations#^ex-73-2|Ex. §73.2]], [[§141 Graphs of Second-Degree Equations#^thm-141-1|§141.1]] (equation of a circle), [[§142 Trigonometry#^def-142-4|Def. §142.4]] (the point at angle $t$ on the unit circle)

> [!example] Example §73.3: One Curve, Four Motions
> Each pair gives the position of a particle at time $t$:
>
> $$
> \text{(a)}\ x = t^3,\ y = t \qquad \text{(b)}\ x = -t^3,\ y = -t \qquad \text{(c)}\ x = t^{3/2},\ y = \sqrt{t} \qquad \text{(d)}\ x = e^{-3t},\ y = e^{-t}
> $$
>
> In each case $x = y^3$: for (c), $y^3 = (t^{1/2})^3 = t^{3/2}$, and for (d), $y^3 = (e^{-t})^3 = e^{-3t}$. So every particle moves along the cubic curve $x = y^3$, but in different ways.
> - **(a)** $y = t$ takes every real value and increases, so the particle traverses the whole curve from left to right.
> - **(b)** $y = -t$ decreases, so the particle traverses the whole curve from right to left.
> - **(c)** The equations make sense only for $t \ge 0$. The particle starts at the origin at $t = 0$ and moves to the right along the upper half ($y \ge 0$).
> - **(d)** Here $x > 0$ and $y > 0$ for all $t$, so only the part in the first quadrant is traced. As $t$ increases through negative values toward $0$, $y = e^{-t}$ decreases toward $1$: the particle comes in from the far right toward $(1, 1)$, which it reaches at $t = 0$. As $t \to \infty$, $(x, y) \to (0, 0)$: it approaches the origin but never reaches it.
>
> *Stewart: Example 10.1.5*

^ex-73-3

> [!example] Example §73.4: Back and Forth on a Parabola
> Sketch the curve $x = \sin t$, $y = \sin^2 t$.
>
> Since $y = (\sin t)^2 = x^2$, the point moves on the parabola $y = x^2$. But $-1 \le \sin t \le 1$, so only the part with $-1 \le x \le 1$ is traced. As $t$ increases, $x = \sin t$ oscillates between $-1$ and $1$, so the point moves back and forth infinitely often along the arc of the parabola from $(-1, 1)$ to $(1, 1)$: from $(0, 0)$ to $(1, 1)$ for $0 \le t \le \pi/2$, back through $(0, 0)$ to $(-1, 1)$ for $\pi/2 \le t \le 3\pi/2$, and back to $(0, 0)$ for $3\pi/2 \le t \le 2\pi$.
>
> *Stewart: Example 10.1.6*

^ex-73-4

> [!example] Example §73.5: A Lissajous Figure
> Sketch the curve $x = \cos t$, $y = \sin 2t$.
>
> Eliminating the parameter is possible but not very helpful: $y^2 = \sin^2 2t = 4\sin^2 t \cos^2 t = 4(1 - x^2)x^2$, that is, $y^2 = 4x^2 - 4x^4$. Instead, read the curve off the graphs of $x = \cos t$ and $y = \sin 2t$ as functions of $t$, one quarter-period at a time.
>
> | $t$ | $x = \cos t$ | $y = \sin 2t$ | part of the curve |
> |---|---|---|---|
> | $0 \to \pi/2$ | $1 \to 0$ | $0 \to 1 \to 0$ | arc in quadrant I, from $(1, 0)$ to $(0, 0)$ |
> | $\pi/2 \to \pi$ | $0 \to -1$ | $0 \to -1 \to 0$ | arc in quadrant III, to $(-1, 0)$ |
> | $\pi \to 3\pi/2$ | $-1 \to 0$ | $0 \to 1 \to 0$ | arc in quadrant II, back to $(0, 0)$ |
> | $3\pi/2 \to 2\pi$ | $0 \to 1$ | $0 \to -1 \to 0$ | arc in quadrant IV, back to $(1, 0)$ |
>
> The arcs in quadrants I and IV make up the right loop, those in quadrants III and II the left loop. The curve is a figure eight lying on its side, passing through the origin twice (at $t = \pi/2$ and $t = 3\pi/2$), with $|x| \le 1$ and $|y| \le 1$; $y = \pm 1$ is reached at $x = \pm 1/\sqrt2$. Since $x$ and $y$ have period $2\pi$, it is traced once for $0 \le t \le 2\pi$.
>
> *Stewart: Example 10.1.7*

^ex-73-5

## Graphing Parametric Curves with Technology

> [!remark] Remark: Graphs as Parametric Curves
> A graph $y = f(x)$ is the parametric curve $x = t$, $y = f(t)$, and a curve $x = g(y)$ is the parametric curve $x = g(t)$, $y = t$. Graphing software uses the second form to draw, say, $x = y^4 - 3y^2$ (Stewart's Example 8), which would otherwise have to be solved for $y$ as four separate functions of $x$. Software also draws curves such as $x = t + \sin 5t$, $y = t + \sin 6t$ that are hopeless by hand; parametric curves called Bézier curves are the basis of computer-aided design and of the letter shapes in PDF files.

^rem-73-2

## The Cycloid

> [!definition] Definition §73.4: Cycloid
> The **cycloid** is the curve traced out by a point $P$ on the circumference of a circle as the circle rolls along a straight line (like a pebble stuck in a car tire).
>
> *Stewart: Example 10.1.9*

^def-73-4

> [!theorem] Proposition §73.2: Parametric Equations of the Cycloid
> If the circle has radius $r$, rolls along the $x$-axis, and $P$ is at the origin in one of its positions, then the cycloid has parametric equations
>
> $$
> x = r(\theta - \sin\theta), \qquad y = r(1 - \cos\theta), \qquad \theta \in \mathbb{R},
> $$
>
> where the parameter $\theta$ is the angle through which the circle has rotated ($\theta = 0$ when $P$ is at the origin). One arch comes from one rotation, $0 \le \theta \le 2\pi$.
>
> *Stewart: 10.1, Equation 1 (Example 10.1.9)*

^prop-73-2

> [!proof]+ Proof
> Suppose the circle has rotated through $\theta$ radians, $0 < \theta < \pi/2$, and let $T$ be its point of contact with the $x$-axis. Since the circle has rolled without slipping, the distance it has rolled equals the arc of the circle that has touched the line:
>
> $$
> |OT| = \text{arc } PT = r\theta .
> $$
>
> So the center is $C(r\theta, r)$. Let $P = (x, y)$, and let $Q$ be the foot of the perpendicular from $P$ to the vertical segment $CT$. In the right triangle $PQC$ the angle at $C$ is $\theta$ and the hypotenuse is $|CP| = r$, so $|PQ| = r\sin\theta$ and $|QC| = r\cos\theta$. Therefore
>
> $$
> x = |OT| - |PQ| = r\theta - r\sin\theta = r(\theta - \sin\theta), \qquad
> y = |TC| - |QC| = r - r\cos\theta = r(1 - \cos\theta) .
> $$
>
> **All values of $\theta$.** (Stewart asserts that the equations remain valid and leaves this as Exercise 48; here is why.) The radius $CP$ points straight down, in the direction $(0, -1)$, when $\theta = 0$. Rolling to the right turns the circle clockwise, so after rotating through $\theta$ the radius points in the direction obtained by turning $(0, -1)$ clockwise through $\theta$, namely $(-\sin\theta, -\cos\theta)$. The center is still at $(r\theta, r)$ for every $\theta$ (for $\theta < 0$ the circle has rolled to the left by $r|\theta|$). Hence for every real $\theta$
>
> $$
> (x, y) = (r\theta, r) + r(-\sin\theta, -\cos\theta) = \big(r(\theta - \sin\theta),\ r(1 - \cos\theta)\big) .
> $$

^pf-73-2

*Uses:* [[§73 Curves Defined by Parametric Equations#^def-73-4|Def. §73.4]], [[§142 Trigonometry#^thm-142-1|§142.1]] (arc length $r\theta$), [[§142 Trigonometry#^def-142-3|Def. §142.3]] (right-triangle trigonometry), [[§142 Trigonometry#^def-142-4|Def. §142.4]] (the direction at a general angle)

![[m233-63-1.svg]]
*Deriving the cycloid. After the circle (blue) has rotated through $\theta$, it has rolled the distance $|OT| = r\theta$, equal to the arc $PT$ (green) that has been in contact with the line. The coordinates of $P = (x, y)$ are $x = |OT| - |PQ| = r\theta - r\sin\theta$ and $y = |TC| - |QC| = r - r\cos\theta$. The red curve is the arch traced by $P$ for $0 \le \theta \le 2\pi$.*

> [!remark] Remark: The Cartesian Equation
> Eliminating $\theta$ is possible but awkward. For $0 \le \theta \le \pi$: $\cos\theta = 1 - y/r$ gives $\theta = \cos^{-1}(1 - y/r)$, and then $r\sin\theta = r\sqrt{1 - (1 - y/r)^2} = \sqrt{2ry - y^2}$, so
>
> $$
> x = r\cos^{-1}\!\Big(1 - \frac{y}{r}\Big) - \sqrt{2ry - y^2} ,
> $$
>
> which describes only half of one arch. The parametric equations are far easier to work with.

^rem-73-3

> [!remark]- Remark: Brachistochrone and Tautochrone
> Galileo proposed that bridges be built in the shape of cycloids and tried to find the area under an arch (done in [[§74 Calculus with Parametric Curves#^ex-74-3|Example §74.3]]). The cycloid answers the **brachistochrone problem**, posed by Johann Bernoulli in 1696: find the curve along which a particle slides in the shortest time, under gravity, from a point $A$ to a lower point $B$ not directly beneath $A$. The answer is part of an inverted arch of a cycloid. Huygens showed by 1673 that the inverted cycloid also solves the **tautochrone problem**: wherever a particle is placed on it, it takes the same time to slide to the bottom. He proposed pendulum clocks swinging in cycloidal arcs, so that the period would not depend on the amplitude.

^rem-73-4

## Families of Parametric Curves

> [!remark]- Remark: The Conchoids of Nicomedes
> Stewart's Example 10 graphs the family $x = a + \cos t$, $y = a\tan t + \sin t$ for several values of $a$. For $a \ne 0$ every member has two branches, both approaching the vertical asymptote $x = a$ (as $t \to \pm\pi/2$, $\tan t \to \pm\infty$ while $x \to a$). For $a < -1$ both branches are smooth; at $a = -1$ the right branch acquires a cusp; for $-1 < a < 0$ the cusp opens into a loop that grows as $a \to 0$; at $a = 0$ the curve is the unit circle $x = \cos t$, $y = \sin t$. Replacing $a$ by $-a$ and $t$ by $\pi - t$ changes $(x, y)$ to $(-x, y)$, so the curves with $a > 0$ are the mirror images in the $y$-axis of those with $a < 0$. These are the **conchoids of Nicomedes**, named for the shell-like outer branches.

^rem-73-5
