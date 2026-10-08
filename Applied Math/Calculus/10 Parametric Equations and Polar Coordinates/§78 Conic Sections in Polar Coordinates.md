---
type: section
subject: "[[Calculus]]"
chapter: 10
section: 78
stewart: "10.6"
aliases: ["Stewart 10.6"]
tags: [calculus]
---
← [[§77 Conic Sections]] · ↑ [[· 10 Parametric Equations and Polar Coordinates]] · [[§79 The Cycloid, the Cardioid and the Four-Leaved Rose]] →

*Stewart, Section 10.6.*

[[§77 Conic Sections|§77]] defined the parabola by a focus and a directrix, but the ellipse and the hyperbola by two foci. Here all three are described the same way: the points whose distance to a focus is a fixed multiple $e$, the eccentricity, of their distance to a directrix. With the focus at the origin, every conic then has a polar equation $r = ed/(1 \pm e\cos\theta)$ or $r = ed/(1 \pm e\sin\theta)$. This is the natural form for orbits, since a planet moves on an ellipse with the sun at a focus (Kepler's First Law), and it gives the closest and farthest distances of a planet from the sun.

## A Unified Description of Conics

> [!definition] Definition §78.1: Focus, Directrix and Eccentricity
> Let $F$ be a fixed point (the **focus**), $l$ a fixed line not through $F$ (the **directrix**), and $e$ a fixed positive number (the **eccentricity**). For a point $P$, $|PF|$ is its distance to $F$ and $|Pl|$ its distance to $l$.
>
> *Stewart: 10.6, Theorem 1*

^def-78-1

> [!theorem] Theorem §78.1: Unified Description of Conics
> The set of all points $P$ in the plane such that
>
> $$
> \frac{|PF|}{|Pl|} = e
> $$
>
> (the ratio of the distance from $F$ to the distance from $l$ is the constant $e$) is a conic section. The conic is
>
> - (a) an ellipse if $e < 1$;
> - (b) a parabola if $e = 1$;
> - (c) a hyperbola if $e > 1$.
>
> For the ellipse and the hyperbola, $F$ is one of the two foci of [[§77 Conic Sections#^def-77-2|Definition §77.2]] or [[§77 Conic Sections#^def-77-3|Definition §77.3]], and $e = c/a$, where $c$ is the distance from the center to a focus and $a$ the distance from the center to a vertex.
>
> *Stewart: 10.6, Theorem 1*

^thm-78-1

> [!proof]+ Proof
> If $e = 1$, the condition is $|PF| = |Pl|$, which is the definition of a parabola ([[§77 Conic Sections#^def-77-1|Definition §77.1]]).
>
> Place $F$ at the origin and the directrix parallel to the $y$-axis, $d$ units to the right: $l$ is the line $x = d$, $d > 0$. If $P$ has polar coordinates $(r, \theta)$, with $r \ge 0$, and Cartesian coordinates $(x, y)$, then
>
> $$
> |PF| = r = \sqrt{x^2 + y^2}, \qquad |Pl| = |d - x| = |d - r\cos\theta| .
> $$
>
> So the condition $|PF| = e|Pl|$ is $r = e|d - r\cos\theta|$, which for $P$ to the left of $l$ reads
>
> $$
> r = e(d - r\cos\theta) . \qquad (2)
> $$
>
> (Stewart writes only this case, $|Pl| = d - r\cos\theta$, as in his figure. A hyperbola also has points to the right of $l$; squaring treats both sides at once.) Both sides of $\sqrt{x^2 + y^2} = e|d - x|$ are $\ge 0$, so it is equivalent to its square:
>
> $$
> x^2 + y^2 = e^2(d - x)^2 = e^2(d^2 - 2dx + x^2), \qquad\text{or}\qquad (1 - e^2)x^2 + 2de^2x + y^2 = e^2d^2 .
> $$
>
> For $e \ne 1$, divide by $1 - e^2$ and complete the square in $x$:
>
> $$
> \Big(x + \frac{e^2d}{1 - e^2}\Big)^2 + \frac{y^2}{1 - e^2} = \frac{e^2d^2}{1 - e^2} + \frac{e^4d^2}{(1 - e^2)^2} = \frac{e^2d^2}{(1 - e^2)^2} . \qquad (3)
> $$
>
> **$e < 1$.** Then $1 - e^2 > 0$, and (3) is the ellipse $\dfrac{(x - h)^2}{a^2} + \dfrac{y^2}{b^2} = 1$ with
>
> $$
> h = -\frac{e^2d}{1 - e^2}, \qquad a^2 = \frac{e^2d^2}{(1 - e^2)^2}, \qquad b^2 = \frac{e^2d^2}{1 - e^2} . \qquad (4)
> $$
>
> Since $b^2 = a^2(1 - e^2) < a^2$, the major axis is horizontal, and by [[§77 Conic Sections#^thm-77-3|Theorem §77.3]] (shifted by $h$) the foci are at distance $c$ from the center $(h, 0)$, where
>
> $$
> c^2 = a^2 - b^2 = \frac{e^2d^2 - e^2d^2(1 - e^2)}{(1 - e^2)^2} = \frac{e^4d^2}{(1 - e^2)^2}, \qquad c = \frac{e^2d}{1 - e^2} = -h . \qquad (5)
> $$
>
> So the right-hand focus $(h + c, 0) = (0, 0)$ is $F$: the focus of [[§78 Conic Sections in Polar Coordinates#^thm-78-1|Theorem §78.1]] is a focus in the sense of [[§77 Conic Sections|§77]]. Dividing, $c/a = \dfrac{e^2d/(1 - e^2)}{ed/(1 - e^2)} = e$.
>
> **$e > 1$.** Then $1 - e^2 < 0$, and multiplying (3) by $(1 - e^2)^2/(e^2d^2)$ gives the hyperbola $\dfrac{(x - h)^2}{a^2} - \dfrac{y^2}{b^2} = 1$ with $h = \dfrac{e^2d}{e^2 - 1}$, $a^2 = \dfrac{e^2d^2}{(e^2 - 1)^2}$, $b^2 = \dfrac{e^2d^2}{e^2 - 1}$. By [[§77 Conic Sections#^thm-77-5|Theorem §77.5]], $c^2 = a^2 + b^2 = \dfrac{e^2d^2 + e^2d^2(e^2 - 1)}{(e^2 - 1)^2} = \dfrac{e^4d^2}{(e^2 - 1)^2}$, so $c = \dfrac{e^2d}{e^2 - 1} = h$. The focus $(h - c, 0) = (0, 0)$ is $F$, and again $e = c/a$, now with $c^2 = a^2 + b^2$.
>
> Every step was an equivalence, so the set of points is the whole conic.

^pf-78-1

*Uses:* [[§78 Conic Sections in Polar Coordinates#^def-78-1|Def. §78.1]], [[§77 Conic Sections#^def-77-1|Def. §77.1]], [[§77 Conic Sections#^thm-77-3|§77.3]], [[§77 Conic Sections#^thm-77-5|§77.5]], [[§75 Polar Coordinates#^thm-75-2|§75.2]], [[§141 Graphs of Second-Degree Equations#^thm-141-5|§141.5]] (shifted conics)

![[m233-68-1.svg]]
*The focus–directrix description with the focus at the pole and the directrix $x = d$. For $P(r, \theta)$, $|PF| = r$ and $|Pl| = d - r\cos\theta$ (here $\theta > \pi/2$, so $r\cos\theta < 0$), and the conic is where $|PF| = e|Pl|$. Here $e = 0.6$: an ellipse, with $F$ as its right-hand focus.*

## Polar Equations of Conics

To rotate a polar curve, rotate its angle variable.

> [!theorem] Lemma §78.2: Rotating a Polar Curve
> The graph of $r = f(\theta - \alpha)$ is the graph of $r = f(\theta)$ rotated counterclockwise about the origin through the angle $\alpha$.
>
> *Stewart: 10.6 (text; Exercise 10.3.65)*

^lem-78-2

> [!proof]+ Proof
> Rotating counterclockwise through $\alpha$ takes the point with polar coordinates $(r, \varphi)$ to the point $(r, \varphi + \alpha)$. A point $(r, \varphi)$ satisfies $r = f(\varphi)$ exactly when $(r, \theta)$ with $\theta = \varphi + \alpha$ satisfies $r = f(\theta - \alpha)$. So the rotation maps the representations satisfying the first equation onto those satisfying the second, and hence ([[§75 Polar Coordinates#^def-75-2|Definition §75.2]]) the first graph onto the second.

^pf-78-2

*Uses:* [[§75 Polar Coordinates#^def-75-1|Def. §75.1]], [[§75 Polar Coordinates#^def-75-2|Def. §75.2]]

> [!theorem] Theorem §78.3: Polar Equations of Conics
> A polar equation of the form
>
> $$
> r = \frac{ed}{1 \pm e\cos\theta} \qquad\text{or}\qquad r = \frac{ed}{1 \pm e\sin\theta} \qquad (d > 0)
> $$
>
> represents a conic section with eccentricity $e$, focus at the origin and directrix $x = d$, $x = -d$, $y = d$, $y = -d$ respectively (for $+\cos$, $-\cos$, $+\sin$, $-\sin$). The conic is an ellipse if $e < 1$, a parabola if $e = 1$, or a hyperbola if $e > 1$.
>
> *Stewart: 10.6, Theorem 6*

^thm-78-3

> [!proof]+ Proof
> **Directrix $x = d$.** Solving Equation 2, $r = e(d - r\cos\theta)$, for $r$ gives $r(1 + e\cos\theta) = ed$, that is, $r = \dfrac{ed}{1 + e\cos\theta}$. (Stewart stops here. Negative values of $r$ occur when $1 + e\cos\theta < 0$, which is possible only for $e > 1$; they give the branch of the hyperbola to the right of the directrix. Here is why the equation describes exactly the conic.) If $(r, \theta)$ satisfies the equation, then $r = e(d - r\cos\theta) = e(d - x)$, so $x^2 + y^2 = r^2 = e^2(d - x)^2$, which is $|PF| = e|Pl|$. Conversely, let $P(x, y)$ satisfy $|PF| = e|Pl|$; $P$ is not on $l$, since then $|PF| = 0$ and $P = F$, which is not on $l$. If $x < d$, represent $P$ with $r = |PF| > 0$: then $r = e(d - x) = e(d - r\cos\theta)$. If $x > d$, represent $P$ with $r = -|PF| < 0$, which does not change $x = r\cos\theta$: then $r = -e(x - d) = e(d - r\cos\theta)$. Either way some representation satisfies the polar equation. By [[§78 Conic Sections in Polar Coordinates#^thm-78-1|Theorem §78.1]] the graph is the conic with eccentricity $e$.
>
> **The other directrices.** By [[§78 Conic Sections in Polar Coordinates#^lem-78-2|Lemma §78.2]], rotating the conic of the first case through $\pi$, $\pi/2$ and $-\pi/2$ (which takes the directrix $x = d$ to $x = -d$, $y = d$, $y = -d$) replaces $\cos\theta$ by
>
> $$
> \cos(\theta - \pi) = -\cos\theta, \qquad \cos(\theta - \tfrac{\pi}{2}) = \sin\theta, \qquad \cos(\theta + \tfrac{\pi}{2}) = -\sin\theta .
> $$

^pf-78-3

*Uses:* [[§78 Conic Sections in Polar Coordinates#^thm-78-1|§78.1]], [[§78 Conic Sections in Polar Coordinates#^lem-78-2|§78.2]], [[§75 Polar Coordinates#^def-75-1|Def. §75.1]] (negative $r$), [[§142 Trigonometry#^cor-142-8|§142.8]] (subtraction formulas)

> [!remark] Remark: Method — Reading a Polar Equation of a Conic
> 1. Divide numerator and denominator so that the constant term of the denominator is $1$: $r = \dfrac{ed}{1 \pm e\cos\theta}$ or $\dfrac{ed}{1 \pm e\sin\theta}$.
> 2. The coefficient of $\cos\theta$ or $\sin\theta$ is $e$; it decides the type. Then $d = (\text{numerator})/e$.
> 3. The sign and the function locate the directrix: $+\cos$: $x = d$; $-\cos$: $x = -d$; $+\sin$: $y = d$; $-\sin$: $y = -d$.
> 4. Plot $r$ at $\theta = 0, \pi/2, \pi, 3\pi/2$; these include the vertices. For a hyperbola, the asymptotes are parallel to the rays on which the denominator is $0$.

^rem-78-1

> [!example] Example §78.1: A Parabola with Focus at the Origin
> Find a polar equation for the parabola with focus at the origin and directrix $y = -6$.
>
> By [[§78 Conic Sections in Polar Coordinates#^thm-78-3|Theorem §78.3]] with $e = 1$, $d = 6$ and the directrix below the focus, $r = \dfrac{6}{1 - \sin\theta}$.
>
> *Stewart: Example 10.6.1*

^ex-78-1

> [!example] Example §78.2: An Ellipse, and the Same Ellipse Rotated
> Identify $r = \dfrac{10}{3 - 2\cos\theta}$, find its eccentricity and directrix, and sketch it. Then rotate it through $\pi/4$ about the origin.
>
> Dividing numerator and denominator by $3$, $r = \dfrac{10/3}{1 - \frac23\cos\theta}$. By [[§78 Conic Sections in Polar Coordinates#^thm-78-3|Theorem §78.3]] this is an ellipse with $e = \frac23$. Since $ed = \frac{10}{3}$, $d = \dfrac{10/3}{2/3} = 5$, and the directrix is $x = -5$. Values of $r$:
>
> | $\theta$ | $0$ | $\pi/2$ | $\pi$ | $3\pi/2$ |
> |---|---|---|---|---|
> | $r$ | $10$ | $10/3$ | $2$ | $10/3$ |
>
> The vertices are $(10, 0)$ and $(2, \pi)$, the point $(-2, 0)$ in Cartesian coordinates; the ellipse crosses the $y$-axis at $(0, \pm\frac{10}{3})$, and its left focus is the origin. (Check: $2a = 10 + 2 = 12$, so $a = 6$, the center is $(4, 0)$, $c = 4$, and $c/a = \frac23 = e$.)
>
> **Rotation.** By [[§78 Conic Sections in Polar Coordinates#^lem-78-2|Lemma §78.2]], replacing $\theta$ by $\theta - \pi/4$ gives the ellipse rotated counterclockwise through $\pi/4$ about the origin, which is its left focus:
>
> $$
> r = \frac{10}{3 - 2\cos(\theta - \pi/4)} .
> $$
>
> *Stewart: Examples 10.6.2 and 10.6.4*

^ex-78-2

> [!example] Example §78.3: A Hyperbola
> Sketch $r = \dfrac{12}{2 + 4\sin\theta}$.
>
> Dividing by $2$, $r = \dfrac{6}{1 + 2\sin\theta}$: a hyperbola with $e = 2$. Since $ed = 6$, $d = 3$, and the directrix is $y = 3$. Values of $r$:
>
> | $\theta$ | $0$ | $\pi/2$ | $\pi$ | $3\pi/2$ |
> |---|---|---|---|---|
> | $r$ | $6$ | $2$ | $6$ | $-6$ |
>
> The vertices occur at $\theta = \pi/2$ and $3\pi/2$: $(2, \pi/2)$ and $(-6, 3\pi/2) = (6, \pi/2)$, the Cartesian points $(0, 2)$ and $(0, 6)$. The $x$-intercepts are at $\theta = 0, \pi$, both with $r = 6$: $(\pm6, 0)$. The lower branch passes through $(0, 2)$ and $(\pm 6, 0)$, the upper branch through $(0, 6)$ (traced with $r < 0$). For the asymptotes: $r \to \pm\infty$ when $1 + 2\sin\theta \to 0^\pm$, and $1 + 2\sin\theta = 0$ when $\sin\theta = -\frac12$. So the asymptotes are parallel to the rays $\theta = 7\pi/6$ and $\theta = 11\pi/6$, with slopes $\pm 1/\sqrt3$. (Center $(0, 4)$, $a = 2$, $c = 4$, $c/a = 2 = e$.)
>
> *Stewart: Example 10.6.3*

^ex-78-3

> [!remark]- Remark: The Effect of the Eccentricity
> For $e$ close to $0$ the ellipse is nearly circular; it becomes more elongated as $e \to 1^-$; at $e = 1$ it is a parabola; for $e > 1$ the hyperbola's branches open wider as $e$ grows (the asymptotes have slopes $\pm b/a = \pm\sqrt{e^2 - 1}$). In terms of the semimajor axis, $b/a = \sqrt{1 - e^2}$ for the ellipse, by (4).

^rem-78-2

## Kepler's Laws

In 1609 Kepler, from large amounts of astronomical data, published three laws of planetary motion: (1) a planet revolves around the sun in an elliptical orbit with the sun at one focus; (2) the line joining the sun to a planet sweeps out equal areas in equal times; (3) the square of the period of revolution of a planet is proportional to the cube of the length of the major axis of its orbit. They apply equally to moons, comets and satellites orbiting under a single gravitational force. Stewart deduces them from Newton's laws in Section 13.4 ([[§104 Motion in Space꞉ Velocity and Acceleration#^thm-104-6|Theorem §104.6]], where the First Law is proved). Here the First Law and the polar equation of an ellipse give astronomical distances.

> [!theorem] Theorem §78.4: Polar Equation of an Ellipse by Semimajor Axis
> The polar equation of an ellipse with focus at the origin, semimajor axis $a$, eccentricity $e$, and directrix $x = d$ can be written as
>
> $$
> r = \frac{a(1 - e^2)}{1 + e\cos\theta} .
> $$
>
> *Stewart: 10.6, Equation 7*

^thm-78-4

> [!proof]+ Proof
> By (4) in the proof of [[§78 Conic Sections in Polar Coordinates#^thm-78-1|Theorem §78.1]], $a^2 = \dfrac{e^2d^2}{(1 - e^2)^2}$, so $d^2 = \dfrac{a^2(1 - e^2)^2}{e^2}$ and, since $d$, $a$, $1 - e^2$ and $e$ are positive, $d = \dfrac{a(1 - e^2)}{e}$. Hence $ed = a(1 - e^2)$, and [[§78 Conic Sections in Polar Coordinates#^thm-78-3|Theorem §78.3]] gives $r = \dfrac{ed}{1 + e\cos\theta} = \dfrac{a(1 - e^2)}{1 + e\cos\theta}$.

^pf-78-4

*Uses:* [[§78 Conic Sections in Polar Coordinates#^thm-78-1|§78.1]] (Equations 4), [[§78 Conic Sections in Polar Coordinates#^thm-78-3|§78.3]]

> [!definition] Definition §78.2: Perihelion and Aphelion
> The positions of a planet closest to and farthest from the sun are its **perihelion** and **aphelion**; they are the vertices of the elliptical orbit. The distances from the sun to them are the **perihelion distance** and the **aphelion distance**.
>
> *Stewart: 10.6 (text)*

^def-78-2

> [!theorem] Corollary §78.5: Perihelion and Aphelion Distances
> The perihelion distance from a planet to the sun is $a(1 - e)$ and the aphelion distance is $a(1 + e)$.
>
> *Stewart: 10.6, Equation 8*

^cor-78-5

> [!proof]+ Proof
> Put the sun at the focus $F$ = origin, as in [[§78 Conic Sections in Polar Coordinates#^thm-78-4|Theorem §78.4]]. The distance $r = \dfrac{a(1 - e^2)}{1 + e\cos\theta}$ is smallest when $\cos\theta = 1$ and largest when $\cos\theta = -1$ (since $0 < e < 1$, the denominator is positive and largest, resp. smallest, there). At perihelion, $\theta = 0$:
>
> $$
> r = \frac{a(1 - e^2)}{1 + e} = \frac{a(1 - e)(1 + e)}{1 + e} = a(1 - e) ,
> $$
>
> and at aphelion, $\theta = \pi$: $r = \dfrac{a(1 - e^2)}{1 - e} = a(1 + e)$.

^pf-78-5

*Uses:* [[§78 Conic Sections in Polar Coordinates#^thm-78-4|§78.4]]

> [!example] Example §78.4: The Earth's Orbit
> The eccentricity of the earth's orbit is about $0.017$ and the length of the major axis about $2.99 \times 10^8$ km. (a) Find an approximate polar equation for the orbit, with the sun at the origin. (b) Find the perihelion and aphelion distances.
>
> **(a)** $2a = 2.99 \times 10^8$, so $a = 1.495 \times 10^8$. By [[§78 Conic Sections in Polar Coordinates#^thm-78-4|Theorem §78.4]],
>
> $$
> r = \frac{(1.495 \times 10^8)[1 - (0.017)^2]}{1 + 0.017\cos\theta} \approx \frac{1.49 \times 10^8}{1 + 0.017\cos\theta}
> $$
>
> (the numerator is $1.495 \times 10^8 \times 0.999711 \approx 1.4946 \times 10^8$).
>
> **(b)** By [[§78 Conic Sections in Polar Coordinates#^cor-78-5|Corollary §78.5]], the perihelion distance is $a(1 - e) \approx (1.495 \times 10^8)(0.983) \approx 1.47 \times 10^8$ km and the aphelion distance is $a(1 + e) \approx (1.495 \times 10^8)(1.017) \approx 1.52 \times 10^8$ km.
>
> *Stewart: Example 10.6.5*

^ex-78-4
