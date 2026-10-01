---
type: section
subject: "[[Calculus]]"
chapter: 10
section: 65
stewart: "10.3"
aliases: ["Stewart 10.3"]
tags: [calculus]
---
← [[§64 Calculus with Parametric Curves]] · ↑ [[· 10 Parametric Equations and Polar Coordinates]] · [[§66 Calculus in Polar Coordinates]] →

*Stewart, Section 10.3 · reviewed in MATH 233 (UMass, Spring 2023), before double integrals in polar coordinates.*

Polar coordinates locate a point by its distance $r$ from a fixed point and the angle $\theta$ of the ray to it. Unlike Cartesian coordinates, every point has infinitely many polar representations, and negative $r$ is allowed. The conversion formulas $x = r\cos\theta$, $y = r\sin\theta$ connect the two systems. Many curves that are awkward in $x$ and $y$ (circles through the origin, cardioids, roses, spirals) have simple polar equations $r = f(\theta)$, and the section shows how to sketch them: first graph $r$ against $\theta$ in Cartesian coordinates, then read off the polar curve, using symmetry. Polar coordinates return for double integrals in [[§100 Double Integrals in Polar Coordinates|§100]].

## The Polar Coordinate System

> [!definition] Definition §65.1: Polar Coordinates
> Choose a point $O$ in the plane, the **pole** (or origin), and a ray starting at $O$, the **polar axis**, usually drawn horizontally to the right (the positive $x$-axis). For any other point $P$, let $r$ be the distance from $O$ to $P$ and $\theta$ the angle (usually in radians) between the polar axis and the line $OP$. Then $P$ is represented by the ordered pair $(r, \theta)$, and $r$, $\theta$ are the **polar coordinates** of $P$.
> - An angle is positive if measured counterclockwise from the polar axis and negative if measured clockwise.
> - If $P = O$, then $r = 0$, and $(0, \theta)$ represents the pole for every $\theta$.
> - **Negative $r$.** The points $(-r, \theta)$ and $(r, \theta)$ lie on the same line through $O$, at the same distance $|r|$ from $O$, on opposite sides of $O$. So if $r > 0$, the point $(r, \theta)$ lies in the same quadrant as $\theta$; if $r < 0$, it lies in the quadrant on the opposite side of the pole. In particular $(-r, \theta)$ is the same point as $(r, \theta + \pi)$.
>
> *Stewart: 10.3 (text)*

^def-65-1

> [!theorem] Proposition §65.1: Many Representations of a Point
> The point with polar coordinates $(r, \theta)$ is also represented by
>
> $$
> (r, \theta + 2n\pi) \qquad\text{and}\qquad (-r, \theta + (2n + 1)\pi), \qquad n \text{ any integer}.
> $$
>
> *Stewart: 10.3 (text)*

^prop-65-1

> [!proof]+ Proof
> A complete counterclockwise rotation is an angle of $2\pi$, so the rays at angles $\theta$ and $\theta + 2n\pi$ coincide, and $(r, \theta + 2n\pi)$ is the same point as $(r, \theta)$. By Definition §65.1, $(-r, \varphi)$ is the same point as $(r, \varphi + \pi)$; with $\varphi = \theta + (2n + 1)\pi$ this is $(r, \theta + (2n + 2)\pi)$, which is $(r, \theta)$ by the first part.

^pf-65-1

*Uses:* [[§65 Polar Coordinates#^def-65-1|Def. §65.1]]

## Relationship Between Polar and Cartesian Coordinates

Let the pole be the origin and the polar axis the positive $x$-axis.

> [!theorem] Theorem §65.2: Converting Between Polar and Cartesian Coordinates
> If $P$ has Cartesian coordinates $(x, y)$ and polar coordinates $(r, \theta)$, then
>
> $$
> x = r\cos\theta, \qquad y = r\sin\theta \qquad (1)
> $$
>
> and
>
> $$
> r^2 = x^2 + y^2, \qquad \tan\theta = \frac{y}{x} \quad (x \ne 0). \qquad (2)
> $$
>
> These hold for all values of $r$ and $\theta$.
>
> *Stewart: 10.3, Equations 1 and 2*

^thm-65-2

> [!proof]+ Proof
> Stewart reads the equations from a figure with $r > 0$ and $0 < \theta < \pi/2$: in the right triangle with hypotenuse $OP = r$, $\cos\theta = x/r$ and $\sin\theta = y/r$. For general values:
>
> **$r > 0$.** $P$ lies on the circle of radius $r$ about $O$, on the ray at angle $\theta$. By the general definition of sine and cosine ([[§119 Trigonometry#^def-119-4|Definition §119.4]]: $\cos\theta = x/r$, $\sin\theta = y/r$ for the point $(x, y)$ at angle $\theta$ on the circle of radius $r$), $x = r\cos\theta$ and $y = r\sin\theta$.
>
> **$r < 0$.** $(r, \theta)$ is the point $(|r|, \theta + \pi)$, so by the first case $x = |r|\cos(\theta + \pi) = -|r|\cos\theta = r\cos\theta$, and likewise $y = -|r|\sin\theta = r\sin\theta$. (Here $\cos(\theta + \pi) = -\cos\theta$ and $\sin(\theta + \pi) = -\sin\theta$ by Definition §119.4: if $(x', y')$ is on the terminal side of $\theta$, then $(-x', -y')$, at the same distance from $O$, is on the terminal side of $\theta + \pi$.)
>
> **$r = 0$.** Both sides are $0$.
>
> Equations 2 follow from Equations 1: $x^2 + y^2 = r^2(\cos^2\theta + \sin^2\theta) = r^2$, and if $x \ne 0$ then $\dfrac yx = \dfrac{r\sin\theta}{r\cos\theta} = \tan\theta$ (here $r \ne 0$ because $x \ne 0$).

^pf-65-2

*Uses:* [[§65 Polar Coordinates#^def-65-1|Def. §65.1]], [[§119 Trigonometry#^def-119-4|Def. §119.4]] (sine and cosine of a general angle, $\cos(\theta + \pi) = -\cos\theta$, $\sin(\theta + \pi) = -\sin\theta$), [[§119 Trigonometry#^thm-119-4|§119.4]] ($\cos^2\theta + \sin^2\theta = 1$)

> [!remark]- Connections
> - The map $(r, \theta) \mapsto (r\cos\theta, r\sin\theta)$ in 452: it is locally invertible wherever its Jacobian $r$ is nonzero, [[§13 The Inverse Function Theorem#^ex-13-4|452 Ex. §13.4]] (with its inverse, [[§13 The Inverse Function Theorem#^ex-13-3|452 Ex. §13.3]]), and $r$ is the factor in $dx\,dy = r\,dr\,d\theta$, [[§15 Multivariable Integration#^thm-15-7|452 Thm. §15.7]]. Workhorse example: [[Polar and spherical coordinates]].

> [!remark] Remark: Choosing the Angle
> Equations 2 do not determine $\theta$: as $\theta$ runs through $[0, 2\pi)$, each value of $\tan\theta$ occurs twice. When converting from Cartesian to polar coordinates, it is not enough to find $r$ and $\theta$ satisfying Equations 2; choose $\theta$ so that the point $(r, \theta)$ lies in the correct quadrant (Example §65.1(c)).

^rem-65-1

> [!example] Example §65.1: Plotting and Converting Points
> **(a) Negative $r$.** The point $(-3, 3\pi/4)$ lies three units from the pole in the **fourth** quadrant: the angle $3\pi/4$ points into the second quadrant and $r = -3$ is negative. By Equations 1 it is
>
> $$
> \Big(-3\cos\frac{3\pi}{4},\ -3\sin\frac{3\pi}{4}\Big) = \Big(\frac{3}{\sqrt2},\ -\frac{3}{\sqrt2}\Big) .
> $$
>
> **(b) Polar to Cartesian.** For $(2, \pi/3)$, Equations 1 give $x = 2\cos\frac{\pi}{3} = 2 \cdot \frac12 = 1$ and $y = 2\sin\frac{\pi}{3} = 2 \cdot \frac{\sqrt3}{2} = \sqrt3$: the point $(1, \sqrt3)$.
>
> **(c) Cartesian to polar.** For $(1, -1)$, choosing $r > 0$, Equations 2 give $r = \sqrt{1^2 + (-1)^2} = \sqrt2$ and $\tan\theta = -1/1 = -1$. The point is in the fourth quadrant, so $\theta = -\pi/4$ or $\theta = 7\pi/4$: $(\sqrt2, -\pi/4)$ or $(\sqrt2, 7\pi/4)$. (The other solution $\theta = 3\pi/4$ of $\tan\theta = -1$ would give the point $(-1, 1)$, unless $r = -\sqrt2$ is used.)
>
> **(d) Many representations.** By Proposition §65.1, the point $(1, 5\pi/4)$ is also $(1, -3\pi/4)$, $(1, 13\pi/4)$ and $(-1, \pi/4)$.
>
> *Stewart: Examples 10.3.1, 10.3.2 and 10.3.3*

^ex-65-1

## Polar Curves

> [!definition] Definition §65.2: Graph of a Polar Equation
> The **graph of a polar equation** $r = f(\theta)$, or more generally $F(r, \theta) = 0$, consists of all points $P$ that have **at least one** polar representation $(r, \theta)$ whose coordinates satisfy the equation.
>
> *Stewart: 10.3 (text)*

^def-65-2

> [!example] Example §65.2: Circles About the Pole and Lines Through It
> **$r = 2$.** Since $r$ is the distance from the pole, this is the circle with center $O$ and radius $2$. In general $r = a$ is the circle with center $O$ and radius $|a|$ (for $a < 0$ the points $(a, \theta)$ are at distance $|a|$ on the opposite ray).
>
> **$\theta = 1$.** All points $(r, 1)$: the straight line through $O$ making an angle of $1$ radian with the polar axis. The points with $r > 0$ are in the first quadrant, those with $r < 0$ in the third.
>
> *Stewart: Examples 10.3.4 and 10.3.5*

^ex-65-2

> [!example] Example §65.3: A Circle Through the Pole
> Sketch $r = 2\cos\theta$ and find a Cartesian equation for it.
>
> **Plotting.**
>
> | $\theta$ | $0$ | $\pi/6$ | $\pi/4$ | $\pi/3$ | $\pi/2$ | $2\pi/3$ | $3\pi/4$ | $5\pi/6$ | $\pi$ |
> |---|---|---|---|---|---|---|---|---|---|
> | $r = 2\cos\theta$ | $2$ | $\sqrt3$ | $\sqrt2$ | $1$ | $0$ | $-1$ | $-\sqrt2$ | $-\sqrt3$ | $-2$ |
>
> For $0 \le \theta \le \pi/2$ the points run from $(2, 0)$ through the first quadrant to the pole; for $\pi/2 \le \theta \le \pi$, $r < 0$ and the points run through the fourth quadrant back to $(2, 0)$ (e.g. $(-1, 2\pi/3)$ is in the fourth quadrant). The curve looks like a circle, and $\theta$ beyond $\pi$ gives the same points again, since $2\cos(\theta + \pi) = -2\cos\theta$ and $(-r, \theta + \pi)$ is the point $(r, \theta)$.
>
> **Cartesian equation.** From $x = r\cos\theta$, $\cos\theta = x/r$, so $r = 2\cos\theta$ becomes $r = 2x/r$, that is,
>
> $$
> 2x = r^2 = x^2 + y^2, \qquad x^2 + y^2 - 2x = 0 .
> $$
>
> (Multiplying by $r$ adds no new point: $r = 0$ is the pole, which is already on the curve at $\theta = \pi/2$.) Completing the square, $(x - 1)^2 + y^2 = 1$: the circle with center $(1, 0)$ and radius $1$.
>
> **Geometrically.** Let $Q = (2, 0)$ and $P$ a point of this circle. Since $OQ$ is a diameter, the angle $OPQ$ is a right angle (an angle inscribed in a semicircle), so in the right triangle $OPQ$, $r = |OP| = |OQ|\cos\theta = 2\cos\theta$.
>
> *Stewart: Example 10.3.6*

^ex-65-3

> [!example] Example §65.4: The Cardioid
> Sketch $r = 1 + \sin\theta$.
>
> Instead of plotting points, first graph $r = 1 + \sin\theta$, $0 \le \theta \le 2\pi$, in *Cartesian* coordinates (the sine curve shifted up one unit). It shows at a glance how the distance $r$ from $O$ changes as $\theta$ increases:
> - $0 \to \pi/2$: $r$ increases from $1$ to $2$. The curve runs through the first quadrant from $(1, 0)$ out to the point at distance $2$ on the ray $\theta = \pi/2$, that is, $(0, 2)$.
> - $\pi/2 \to \pi$: $r$ decreases from $2$ to $1$, through the second quadrant to $(-1, 0)$.
> - $\pi \to 3\pi/2$: $r$ decreases from $1$ to $0$, through the third quadrant into the pole, which it reaches pointing straight down.
> - $3\pi/2 \to 2\pi$: $r$ increases from $0$ to $1$, through the fourth quadrant back to $(1, 0)$.
>
> Beyond $2\pi$ or below $0$ the path is retraced. The curve is heart-shaped, with a cusp at the pole: a **cardioid**. It is symmetric about the line $\theta = \pi/2$ ([[§65 Polar Coordinates#^thm-65-3|Theorem §65.3]](c)), since $\sin(\pi - \theta) = \sin\theta$.
>
> *Stewart: Example 10.3.7*

^ex-65-4

> [!example] Example §65.5: The Four-Leaved Rose
> Sketch $r = \cos 2\theta$.
>
> Graph $r = \cos 2\theta$, $0 \le \theta \le 2\pi$, in Cartesian coordinates and follow the sign of $r$. As $\theta$ increases from $0$ to $\pi/4$, $r$ decreases from $1$ to $0$: half of a loop in the first quadrant (part ①). As $\theta$ increases from $\pi/4$ to $\pi/2$, $r$ decreases from $0$ to $-1$: the distance from $O$ grows from $0$ to $1$, but since $r < 0$ these points lie on the opposite side of the pole, in the **third** quadrant (part ②). Continuing in steps of $\pi/4$:
>
> | part | $\theta$ | $r$ | quadrant of the points |
> |---|---|---|---|
> | ① | $0 \to \pi/4$ | $1 \to 0$ | I (right leaf) |
> | ② | $\pi/4 \to \pi/2$ | $0 \to -1$ | III (bottom leaf) |
> | ③ | $\pi/2 \to 3\pi/4$ | $-1 \to 0$ | IV (bottom leaf) |
> | ④ | $3\pi/4 \to \pi$ | $0 \to 1$ | II (left leaf) |
> | ⑤ | $\pi \to 5\pi/4$ | $1 \to 0$ | III (left leaf) |
> | ⑥ | $5\pi/4 \to 3\pi/2$ | $0 \to -1$ | I (top leaf) |
> | ⑦ | $3\pi/2 \to 7\pi/4$ | $-1 \to 0$ | II (top leaf) |
> | ⑧ | $7\pi/4 \to 2\pi$ | $0 \to 1$ | IV (right leaf) |
>
> The result has four loops, centred on the axes: a **four-leaved rose**. Note that the leaves along the $y$-axis come from the intervals where $r < 0$.
>
> *Stewart: Example 10.3.8*

^ex-65-5

![[m233-65-1.svg]]
*The four-leaved rose $r = \cos 2\theta$ of Example §65.5. Left: $r$ against $\theta$ in Cartesian coordinates, cut into the eight quarter-periods. Right: the polar curve, with the same numbers. Where $r < 0$ (parts ②, ③, ⑥, ⑦, blue) the point lies on the opposite side of the pole from the ray at angle $\theta$, which is how the leaves along the $y$-axis arise.*

## Symmetry

> [!theorem] Theorem §65.3: Symmetry of Polar Curves
> (a) If a polar equation is unchanged when $\theta$ is replaced by $-\theta$, the curve is symmetric about the polar axis.
>
> (b) If the equation is unchanged when $r$ is replaced by $-r$, or when $\theta$ is replaced by $\theta + \pi$, the curve is symmetric about the pole: it is unchanged by a rotation through $180°$ about the origin.
>
> (c) If the equation is unchanged when $\theta$ is replaced by $\pi - \theta$, the curve is symmetric about the vertical line $\theta = \pi/2$.
>
> *Stewart: 10.3 (text)*

^thm-65-3

> [!proof]+ Proof
> Stewart explains the rules by a figure; in coordinates, by Equations 1: let $P$ be a point of the curve. By Definition §65.2 it has a representation $(r, \theta)$ satisfying the equation, and $P = (x, y) = (r\cos\theta, r\sin\theta)$.
>
> (a) By hypothesis $(r, -\theta)$ also satisfies the equation, so the point $(r\cos(-\theta), r\sin(-\theta)) = (x, -y)$ is on the curve. This is the reflection of $P$ in the polar axis.
>
> (b) If $(-r, \theta)$ satisfies the equation, the point $(-r\cos\theta, -r\sin\theta) = (-x, -y)$ is on the curve. If instead $(r, \theta + \pi)$ satisfies it, the point $(r\cos(\theta + \pi), r\sin(\theta + \pi)) = (-x, -y)$ is on the curve. Either way the reflection of $P$ through the origin is on the curve.
>
> (c) $(r, \pi - \theta)$ satisfies the equation, so the point $(r\cos(\pi - \theta), r\sin(\pi - \theta)) = (-x, y)$ is on the curve: the reflection of $P$ in the $y$-axis, which is the line $\theta = \pi/2$.

^pf-65-3

*Uses:* [[§65 Polar Coordinates#^def-65-2|Def. §65.2]], [[§65 Polar Coordinates#^thm-65-2|§65.2]], [[§119 Trigonometry#^thm-119-5|§119.5]] (cosine is even, sine is odd), [[§119 Trigonometry#^def-119-4|Def. §119.4]] ($\cos(\theta + \pi) = -\cos\theta$, $\sin(\theta + \pi) = -\sin\theta$; $\cos(\pi - \theta) = -\cos\theta$, $\sin(\pi - \theta) = \sin\theta$, since $(-x, y)$ is on the terminal side of $\pi - \theta$ when $(x, y)$ is on that of $\theta$)

> [!remark] Remark: Using Symmetry
> The circle $r = 2\cos\theta$ and the rose $r = \cos 2\theta$ are symmetric about the polar axis, since $\cos(-\theta) = \cos\theta$. The cardioid $r = 1 + \sin\theta$ and the rose are symmetric about $\theta = \pi/2$, since $\sin(\pi - \theta) = \sin\theta$ and $\cos[2(\pi - \theta)] = \cos(2\pi - 2\theta) = \cos 2\theta$. The rose is also symmetric about the pole. So in Example §65.3 it would have been enough to plot points for $0 \le \theta \le \pi/2$ and reflect in the polar axis. The tests are sufficient, not necessary, because a point has many polar representations. For example, replacing $\theta$ by $-\theta$ turns $r = \sin 2\theta$ into $r = -\sin 2\theta$, yet this rose is symmetric about the polar axis: if $(r, \theta)$ satisfies $r = \sin 2\theta$, then the reflected point $(r, -\theta)$ has the representation $(-r, \pi - \theta)$, and $\sin 2(\pi - \theta) = -\sin 2\theta = -r$.

^rem-65-2

## Graphing Polar Curves with Technology

> [!remark]- Remark: Graphing Polar Curves with Technology
> To graph a polar curve with software one must first choose the $\theta$-interval that gives the whole curve. For $r = \sin(8\theta/5)$ (Stewart's Example 9): after $n$ full turns, $\sin\frac{8(\theta + 2n\pi)}{5} = \sin\big(\frac{8\theta}{5} + \frac{16n\pi}{5}\big)$, which equals $\sin\frac{8\theta}{5}$ for all $\theta$ once $16n\pi/5$ is an even multiple of $\pi$, first at $n = 5$. So $0 \le \theta \le 10\pi$ gives the entire curve, which has $16$ loops.
>
> Stewart's Example 10 graphs the **limaçons** $r = 1 + c\sin\theta$ ($0 \le \theta \le 2\pi$ gives the whole curve). For $c > 1$ there is an inner loop, which shrinks as $c$ decreases; at $c = 1$ it disappears and the curve is the cardioid of Example §65.4; for $\frac12 < c < 1$ the cusp is smoothed into a "dimple"; for $0 < c \le \frac12$ the curve is an oval, more and more circular as $c \to 0$; at $c = 0$ it is the circle $r = 1$. For negative $c$ the shapes repeat in reverse order, reflected in the horizontal axis (replacing $c$ by $-c$ and $\theta$ by $-\theta$ leaves $r$ unchanged). The path of Mars as seen from Earth has been modelled by a limaçon with a loop.

^rem-65-3

> [!remark] Remark: Common Polar Curves
> Stewart's Table 1 (for $a > 0$, $b > 0$):
>
> | family | equations | shapes |
> |---|---|---|
> | circles | $r = a$, $r = a\sin\theta$, $r = a\cos\theta$ | about $O$; through $O$ with center on the $y$-axis; through $O$ with center on the $x$-axis |
> | spiral | $r = a\theta$ | spiral of Archimedes |
> | limaçons | $r = a \pm b\sin\theta$, $r = a \pm b\cos\theta$ | $a < b$: inner loop; $a = b$: cardioid; $b < a < 2b$: dimpled; $a \ge 2b$: convex |
> | roses | $r = a\sin n\theta$, $r = a\cos n\theta$ | $n$ leaves if $n$ is odd, $2n$ leaves if $n$ is even |
> | lemniscates | $r^2 = a^2\sin 2\theta$, $r^2 = a^2\cos 2\theta$ | figure eights |
>
> The orientation of a limaçon depends on the trigonometric function (sine or cosine) and the sign of $b$.

^rem-65-4
