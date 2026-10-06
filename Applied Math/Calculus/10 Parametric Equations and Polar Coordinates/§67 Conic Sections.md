---
type: section
subject: "[[Calculus]]"
chapter: 10
section: 67
stewart: "10.5"
aliases: ["Stewart 10.5"]
tags: [calculus]
---
← [[§66 Calculus in Polar Coordinates]] · ↑ [[· 10 Parametric Equations and Polar Coordinates]] · [[§68 Conic Sections in Polar Coordinates]] →

*Stewart, Section 10.5.*

Parabolas, ellipses and hyperbolas are called **conic sections**, or **conics**, because they are the curves in which a plane cuts a double cone: a plane tilted less steeply than the cone gives an ellipse, one parallel to a line of the cone a parabola, and one steeper than the cone a hyperbola (both halves of the cone). This section defines each conic geometrically, by distances to foci or to a focus and a directrix, and derives its standard equation when its axis is a coordinate axis. Completing the square then handles conics whose center or vertex has been shifted. [[§68 Conic Sections in Polar Coordinates#^thm-68-1|Theorem §68.1]] unifies the three definitions with the eccentricity.

## Parabolas

> [!definition] Definition §67.1: Parabola
> A **parabola** is the set of points in a plane that are equidistant from a fixed point $F$, the **focus**, and a fixed line, the **directrix**. The point halfway between the focus and the directrix lies on the parabola; it is the **vertex**. The line through the focus perpendicular to the directrix is the **axis** of the parabola.
>
> *Stewart: 10.5 (text)*

^def-67-1

> [!theorem] Theorem §67.1: Standard Equation of a Parabola
> An equation of the parabola with focus $(0, p)$ and directrix $y = -p$ is
>
> $$
> x^2 = 4py .
> $$
>
> With $a = 1/(4p)$ this is $y = ax^2$. The parabola opens upward if $p > 0$ and downward if $p < 0$, and it is symmetric about the $y$-axis, its axis.
>
> *Stewart: 10.5, Equation 1*

^thm-67-1

> [!proof]+ Proof
> The point $P(x, y)$ has distance $|PF| = \sqrt{x^2 + (y - p)^2}$ to the focus and $|y + p|$ to the directrix. So $P$ is on the parabola if and only if
>
> $$
> \sqrt{x^2 + (y - p)^2} = |y + p| .
> $$
>
> Both sides are $\ge 0$, so this is equivalent to the equation of squares (squaring adds no solutions here):
>
> $$
> x^2 + (y - p)^2 = (y + p)^2 \iff x^2 + y^2 - 2py + p^2 = y^2 + 2py + p^2 \iff x^2 = 4py .
> $$
>
> If $p > 0$ then $y = x^2/(4p) \ge 0$, and if $p < 0$ then $y \le 0$. The equation is unchanged when $x$ is replaced by $-x$, so the graph is symmetric about the $y$-axis.

^pf-67-1

*Uses:* [[§67 Conic Sections#^def-67-1|Def. §67.1]], distance formula ([[§117 Coordinate Geometry and Lines#^thm-117-1|§117.1]])

> [!theorem] Corollary §67.2: Parabola with Horizontal Axis
> An equation of the parabola with focus $(p, 0)$ and directrix $x = -p$ is
>
> $$
> y^2 = 4px .
> $$
>
> It opens to the right if $p > 0$ and to the left if $p < 0$, and it is symmetric about the $x$-axis, its axis.
>
> *Stewart: 10.5, Equation 2*

^cor-67-2

> [!proof]+ Proof
> Interchanging $x$ and $y$ reflects the plane in the line $y = x$, which preserves distances. It takes the focus $(0, p)$ to $(p, 0)$ and the directrix $y = -p$ to $x = -p$, so it takes the parabola of [[§67 Conic Sections#^thm-67-1|Theorem §67.1]] to this one, and its equation $x^2 = 4py$ to $y^2 = 4px$.

^pf-67-2

*Uses:* [[§67 Conic Sections#^thm-67-1|§67.1]]

> [!example] Example §67.1: Focus and Directrix of a Parabola
> Find the focus and directrix of $y^2 + 10x = 0$ and sketch it.
>
> Write it as $y^2 = -10x$ and compare with [[§67 Conic Sections#^cor-67-2|Corollary §67.2]]: $4p = -10$, so $p = -\frac52$. The focus is $(p, 0) = (-\frac52, 0)$ and the directrix is $x = \frac52$. The parabola has its vertex at the origin, opens to the left and is symmetric about the $x$-axis.
>
> *Stewart: Example 10.5.1*

^ex-67-1

## Ellipses

> [!definition] Definition §67.2: Ellipse
> An **ellipse** is the set of points in a plane the sum of whose distances from two fixed points $F_1$ and $F_2$ is a constant. The two fixed points are the **foci** (plural of focus).
>
> *Stewart: 10.5 (text)*

^def-67-2

> [!theorem] Theorem §67.3: Standard Equation of an Ellipse
> Let the foci be $(\pm c, 0)$ and the sum of distances $2a$, where $a > c \ge 0$, and put $b^2 = a^2 - c^2$. Then the ellipse has the equation
>
> $$
> \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 . \qquad (3)
> $$
>
> Conversely, the ellipse $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ with $a \ge b > 0$ has foci $(\pm c, 0)$, where $c^2 = a^2 - b^2$, and **vertices** $(\pm a, 0)$.
>
> *Stewart: 10.5, Equations 3 and 4*

^thm-67-3

> [!proof]+ Proof
> **The equation.** $P(x, y)$ is on the ellipse when $|PF_1| + |PF_2| = 2a$, that is,
>
> $$
> \sqrt{(x + c)^2 + y^2} + \sqrt{(x - c)^2 + y^2} = 2a, \quad\text{or}\quad \sqrt{(x - c)^2 + y^2} = 2a - \sqrt{(x + c)^2 + y^2} .
> $$
>
> Squaring both sides,
>
> $$
> x^2 - 2cx + c^2 + y^2 = 4a^2 - 4a\sqrt{(x + c)^2 + y^2} + x^2 + 2cx + c^2 + y^2 ,
> $$
>
> which simplifies to $a\sqrt{(x + c)^2 + y^2} = a^2 + cx$. Squaring again,
>
> $$
> a^2(x^2 + 2cx + c^2 + y^2) = a^4 + 2a^2cx + c^2x^2, \quad\text{which becomes}\quad (a^2 - c^2)x^2 + a^2y^2 = a^2(a^2 - c^2) .
> $$
>
> Here $a^2 - c^2 > 0$ by the hypothesis $a > c$, which is forced: in the triangle $F_1F_2P$ the side $F_1F_2$ is shorter than the sum of the other two, so $2c < 2a$. With $b^2 = a^2 - c^2$ the equation is $b^2x^2 + a^2y^2 = a^2b^2$; dividing by $a^2b^2$ gives (3).
>
> **Conversely** (Stewart does not check that squaring added no points; here is why it did not), let $(x, y)$ satisfy (3), so $y^2 = b^2 - b^2x^2/a^2$ and $|x| \le a$. Then
>
> $$
> (x \pm c)^2 + y^2 = x^2\Big(1 - \frac{b^2}{a^2}\Big) \pm 2cx + c^2 + b^2 = \frac{c^2x^2}{a^2} \pm 2cx + a^2 = \Big(a \pm \frac{cx}{a}\Big)^2 ,
> $$
>
> and $a \pm cx/a \ge a - c > 0$ because $|cx/a| \le c$. Hence $|PF_1| + |PF_2| = (a + cx/a) + (a - cx/a) = 2a$, and $(x, y)$ is on the ellipse.
>
> **Vertices.** Setting $y = 0$ gives $x^2 = a^2$, so $x = \pm a$: the vertices $(\pm a, 0)$. The segment joining them is the **major axis**. Setting $x = 0$ gives $y = \pm b$; the segment from $(0, -b)$ to $(0, b)$ is the **minor axis**. Since $b^2 = a^2 - c^2 \le a^2$, $b \le a$. Equation 3 is unchanged when $x$ is replaced by $-x$ or $y$ by $-y$, so the ellipse is symmetric about both axes. If the foci coincide, $c = 0$, then $a = b$ and the ellipse is the circle of radius $a$.

^pf-67-3

*Uses:* [[§67 Conic Sections#^def-67-2|Def. §67.2]], distance formula ([[§117 Coordinate Geometry and Lines#^thm-117-1|§117.1]]), triangle inequality in the plane ([[Triangle inequality|LADR 6.17]])

![[m233-67-1.svg]]
*The ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$. For every point $P$ on it, $|PF_1| + |PF_2| = 2a$ (blue). At the end $(0, b)$ of the minor axis the two distances are equal, so each is $a$, and the right triangle with legs $b$ and $c$ and hypotenuse $a$ (red) shows $c^2 = a^2 - b^2$.*

> [!theorem] Corollary §67.4: Ellipse with Foci on the y-Axis
> The ellipse
>
> $$
> \frac{x^2}{b^2} + \frac{y^2}{a^2} = 1, \qquad a \ge b > 0,
> $$
>
> has foci $(0, \pm c)$, where $c^2 = a^2 - b^2$, and vertices $(0, \pm a)$.
>
> *Stewart: 10.5, Equation 5*

^cor-67-4

> [!proof]+ Proof
> Interchange $x$ and $y$ in [[§67 Conic Sections#^thm-67-3|Theorem §67.3]] (a reflection in $y = x$, which preserves distances, foci and vertices).

^pf-67-4

*Uses:* [[§67 Conic Sections#^thm-67-3|§67.3]]

> [!example] Example §67.2: From Equation to Foci and Back
> **(a)** Sketch $9x^2 + 16y^2 = 144$ and locate the foci. Dividing by $144$,
>
> $$
> \frac{x^2}{16} + \frac{y^2}{9} = 1 ,
> $$
>
> so $a^2 = 16$, $b^2 = 9$, $a = 4$, $b = 3$. The $x$-intercepts are $\pm4$, the $y$-intercepts $\pm3$, and $c^2 = a^2 - b^2 = 7$: the foci are $(\pm\sqrt7, 0)$.
>
> **(b)** Find an equation of the ellipse with foci $(0, \pm2)$ and vertices $(0, \pm3)$. The foci are on the $y$-axis, so use [[§67 Conic Sections#^cor-67-4|Corollary §67.4]] with $c = 2$, $a = 3$: $b^2 = a^2 - c^2 = 9 - 4 = 5$, and the ellipse is
>
> $$
> \frac{x^2}{5} + \frac{y^2}{9} = 1, \qquad\text{or}\qquad 9x^2 + 5y^2 = 45 .
> $$
>
> *Stewart: Examples 10.5.2 and 10.5.3*

^ex-67-2

> [!remark]- Remark: Reflection Properties
> Light from a source at the focus of a parabolic mirror is reflected parallel to the axis (headlights, reflecting telescopes; Stewart's Problems Plus after Chapter 3). Light or sound from one focus of an elliptical reflector is reflected to the other focus (Stewart's Exercise 67). Lithotripsy uses this to treat kidney stones: with the stone at one focus, high-intensity sound waves generated at the other focus are reflected onto the stone and destroy it without surgery. Kepler's first law says that planets move in ellipses with the sun at one focus (proved in [[§89 Motion in Space꞉ Velocity and Acceleration#^thm-89-6|Theorem §89.6]]; [[§68 Conic Sections in Polar Coordinates|§68]] computes with it).

^rem-67-1

## Hyperbolas

> [!definition] Definition §67.3: Hyperbola
> A **hyperbola** is the set of all points in a plane the difference of whose distances from two fixed points $F_1$ and $F_2$, the **foci**, is a constant: $|PF_1| - |PF_2| = \pm 2a$.
>
> *Stewart: 10.5 (text)*

^def-67-3

> [!theorem] Theorem §67.5: Standard Equation of a Hyperbola
> Let the foci be $(\pm c, 0)$ and $|PF_1| - |PF_2| = \pm 2a$, where $0 < a < c$, and put $b^2 = c^2 - a^2$. Then the hyperbola has the equation
>
> $$
> \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1 . \qquad (6)
> $$
>
> Conversely, the hyperbola $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ has foci $(\pm c, 0)$, where $c^2 = a^2 + b^2$, **vertices** $(\pm a, 0)$, and **asymptotes** $y = \pm (b/a)x$. It consists of two **branches**, $x \ge a$ and $x \le -a$.
>
> *Stewart: 10.5, Equations 6 and 7*

^thm-67-5

> [!proof]+ Proof
> Stewart leaves the derivation as Exercise 54 and the asymptotes as Exercise 4.5.77; the argument is the one for the ellipse.
>
> **The equation.** $P(x, y)$ is on the hyperbola when $\sqrt{(x + c)^2 + y^2} = \pm 2a + \sqrt{(x - c)^2 + y^2}$. Squaring,
>
> $$
> x^2 + 2cx + c^2 + y^2 = 4a^2 \pm 4a\sqrt{(x - c)^2 + y^2} + x^2 - 2cx + c^2 + y^2 ,
> $$
>
> so $cx - a^2 = \pm a\sqrt{(x - c)^2 + y^2}$. Squaring again, $c^2x^2 - 2a^2cx + a^4 = a^2(x^2 - 2cx + c^2 + y^2)$, which becomes
>
> $$
> (c^2 - a^2)x^2 - a^2y^2 = a^2(c^2 - a^2) .
> $$
>
> Here $b^2 = c^2 - a^2 > 0$ by the hypothesis $a < c$, which is forced: in the triangle $F_1F_2P$ the difference of two sides is less than the third, so $2a < 2c$. Then $b^2x^2 - a^2y^2 = a^2b^2$, and dividing by $a^2b^2$ gives (6).
>
> **Conversely**, let $(x, y)$ satisfy (6), so $y^2 = b^2x^2/a^2 - b^2$. Then, as for the ellipse,
>
> $$
> (x \pm c)^2 + y^2 = x^2\Big(1 + \frac{b^2}{a^2}\Big) \pm 2cx + c^2 - b^2 = \frac{c^2x^2}{a^2} \pm 2cx + a^2 = \Big(\frac{cx}{a} \pm a\Big)^2 .
> $$
>
> From (6), $x^2/a^2 = 1 + y^2/b^2 \ge 1$, so $|x| \ge a$ and $|cx/a| \ge c > a$. If $x \ge a$, then $|PF_1| = cx/a + a$, $|PF_2| = cx/a - a$, and the difference is $2a$; if $x \le -a$, then $|PF_1| = -cx/a - a$, $|PF_2| = -cx/a + a$, and the difference is $-2a$. So $(x, y)$ is on the hyperbola, and the two cases are the two branches.
>
> **Vertices.** $y = 0$ gives $x = \pm a$. Putting $x = 0$ gives $y^2 = -b^2$, impossible, so there is no $y$-intercept. The curve is symmetric about both axes.
>
> **Asymptotes.** On the part of the right branch in the first quadrant, $y = \frac ba\sqrt{x^2 - a^2}$, and
>
> $$
> \frac ba x - \frac ba\sqrt{x^2 - a^2} = \frac ba \cdot \frac{x^2 - (x^2 - a^2)}{x + \sqrt{x^2 - a^2}} = \frac{ab}{x + \sqrt{x^2 - a^2}} \to 0 \quad (x \to \infty) .
> $$
>
> So the branch comes arbitrarily close to the line $y = (b/a)x$: a slant asymptote ([[§29 Summary of Curve Sketching#^def-29-2|Definition §29.2]]). By symmetry both branches approach both lines $y = \pm(b/a)x$.

^pf-67-5

*Uses:* [[§67 Conic Sections#^def-67-3|Def. §67.3]], distance formula ([[§117 Coordinate Geometry and Lines#^thm-117-1|§117.1]]), triangle inequality in the plane ([[Triangle inequality|LADR 6.17]]), [[§29 Summary of Curve Sketching#^def-29-2|Def. §29.2]] (slant asymptotes)

> [!theorem] Corollary §67.6: Hyperbola with Foci on the y-Axis
> The hyperbola
>
> $$
> \frac{y^2}{a^2} - \frac{x^2}{b^2} = 1
> $$
>
> has foci $(0, \pm c)$, where $c^2 = a^2 + b^2$, vertices $(0, \pm a)$, and asymptotes $y = \pm(a/b)x$.
>
> *Stewart: 10.5, Equation 8*

^cor-67-6

> [!proof]+ Proof
> Interchange $x$ and $y$ in [[§67 Conic Sections#^thm-67-5|Theorem §67.5]]. The asymptotes $x = \pm(b/a)y$ become $y = \pm(a/b)x$.

^pf-67-6

*Uses:* [[§67 Conic Sections#^thm-67-5|§67.5]]

> [!example] Example §67.3: Foci, Asymptotes and Equations of Hyperbolas
> **(a)** Find the foci and asymptotes of $9x^2 - 16y^2 = 144$. Dividing by $144$,
>
> $$
> \frac{x^2}{16} - \frac{y^2}{9} = 1 ,
> $$
>
> the form of [[§67 Conic Sections#^thm-67-5|Theorem §67.5]] with $a = 4$, $b = 3$. Then $c^2 = 16 + 9 = 25$: the foci are $(\pm5, 0)$, the vertices $(\pm4, 0)$, and the asymptotes $y = \frac34 x$ and $y = -\frac34 x$. To sketch, draw the asymptotes first, then the two branches through the vertices approaching them.
>
> **(b)** Find the foci and equation of the hyperbola with vertices $(0, \pm1)$ and asymptote $y = 2x$. The vertices are on the $y$-axis, so by [[§67 Conic Sections#^cor-67-6|Corollary §67.6]], $a = 1$ and $a/b = 2$. Thus $b = \frac12$ and $c^2 = a^2 + b^2 = \frac54$. The foci are $(0, \pm\sqrt5/2)$, and the equation is $y^2 - \dfrac{x^2}{1/4} = 1$, that is,
>
> $$
> y^2 - 4x^2 = 1 .
> $$
>
> *Stewart: Examples 10.5.4 and 10.5.5*

^ex-67-3

## Shifted Conics

> [!remark] Remark: Method — Shifted Conics
> Replacing $x$ and $y$ by $x - h$ and $y - k$ in a standard equation ([[§67 Conic Sections#^thm-67-1|Theorem §67.1]], [[§67 Conic Sections#^cor-67-2|Corollary §67.2]], [[§67 Conic Sections#^thm-67-3|Theorem §67.3]], [[§67 Conic Sections#^cor-67-4|Corollary §67.4]], [[§67 Conic Sections#^thm-67-5|Theorem §67.5]], [[§67 Conic Sections#^cor-67-6|Corollary §67.6]]) shifts the conic $h$ units horizontally and $k$ units vertically, together with its foci, vertices, directrix and asymptotes ([[§118 Graphs of Second-Degree Equations#^thm-118-5|Theorem §118.5]]).
> 1. **From the geometry to the equation:** find the center (midpoint of the vertices or foci) $(h, k)$, read off $a$, $b$, $c$ from distances, and write the standard equation in $x - h$, $y - k$.
> 2. **From the equation to the geometry:** collect the $x$-terms and the $y$-terms, complete the square in each, and divide to make the right side $1$. The signs of the squared terms decide the type (same sign: ellipse; opposite signs: hyperbola; only one squared variable: parabola).

^rem-67-2

> [!example] Example §67.4: A Shifted Ellipse
> Find an equation of the ellipse with foci $(2, -2)$, $(4, -2)$ and vertices $(1, -2)$, $(5, -2)$.
>
> The major axis joins the vertices and has length $4$, so $a = 2$. The distance between the foci is $2$, so $c = 1$, and $b^2 = a^2 - c^2 = 3$. The center is the midpoint $(3, -2)$, and the major axis is horizontal. Replacing $x$ and $y$ in [[§67 Conic Sections#^thm-67-3|Theorem §67.3]] by $x - 3$ and $y + 2$:
>
> $$
> \frac{(x - 3)^2}{4} + \frac{(y + 2)^2}{3} = 1 .
> $$
>
> *Stewart: Example 10.5.6*

^ex-67-4

> [!example] Example §67.5: Completing the Square
> Sketch the conic $9x^2 - 4y^2 - 72x + 8y + 176 = 0$ and find its foci.
>
> Complete the squares:
>
> $$
> \begin{aligned}
> 4(y^2 - 2y) - 9(x^2 - 8x) &= 176 \\
> 4(y^2 - 2y + 1) - 9(x^2 - 8x + 16) &= 176 + 4 - 144 \\
> 4(y - 1)^2 - 9(x - 4)^2 &= 36 \\
> \frac{(y - 1)^2}{9} - \frac{(x - 4)^2}{4} &= 1 .
> \end{aligned}
> $$
>
> This is [[§67 Conic Sections#^cor-67-6|Corollary §67.6]] with $x$, $y$ replaced by $x - 4$, $y - 1$: $a^2 = 9$, $b^2 = 4$, $c^2 = 13$, and the hyperbola is shifted $4$ units right and $1$ unit up, with center $(4, 1)$. The foci are $(4, 1 + \sqrt{13})$ and $(4, 1 - \sqrt{13})$, the vertices $(4, 4)$ and $(4, -2)$, and the asymptotes $y - 1 = \pm\frac32(x - 4)$.
>
> *Stewart: Example 10.5.7*

^ex-67-5
