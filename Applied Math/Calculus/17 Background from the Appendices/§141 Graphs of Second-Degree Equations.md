---
type: section
subject: "[[Calculus]]"
chapter: 17
section: 141
stewart: "Appendix C"
aliases: ["Stewart Appendix C"]
tags: [calculus]
---
← [[§140 Coordinate Geometry and Lines]] · ↑ [[· 17 Background from the Appendices]] · [[§142 Trigonometry]] →

*Stewart, Appendix C.*

A first-degree equation $Ax + By + C = 0$ represents a line ([[§140 Coordinate Geometry and Lines#^thm-140-4|Theorem §140.4]]). Second-degree equations such as $x^2 + y^2 = 1$, $y = x^2 + 1$, $\frac{x^2}{9} + \frac{y^2}{4} = 1$ and $x^2 - y^2 = 1$ represent a circle, a parabola, an ellipse and a hyperbola. This appendix gives their standard forms, the symmetry tests and intercepts used to sketch them, and the rule for shifting a graph, which together with completing the square identifies a shifted conic. The geometric definitions (foci, directrices) are in [[§77 Conic Sections|§77]].

> [!definition] Definition §141.1: Graph of an Equation
> The **graph** of an equation in $x$ and $y$ is the set of all points $(x, y)$ that satisfy the equation. Conversely, an equation of a curve is an equation satisfied by the coordinates of the points on the curve and by no other point.
>
> *Stewart: Appendix C (text)*

^def-141-1

This is the basic principle of analytic geometry (Descartes and Fermat): a geometric curve represented by an algebraic equation can be analyzed by the rules of algebra.

## Circles

> [!theorem] Theorem §141.1: Equation of a Circle
> An equation of the circle with center $(h, k)$ and radius $r$ is
>
> $$
> (x - h)^2 + (y - k)^2 = r^2 .
> $$
>
> In particular, if the center is the origin, the equation is $x^2 + y^2 = r^2$.
>
> *Stewart: Appendix C, (1) Equation of a Circle*

^thm-141-1

> [!proof]+ Proof
> By definition the circle is the set of points $P(x, y)$ whose distance from the center $C(h, k)$ is $r$. By the Distance Formula ([[§140 Coordinate Geometry and Lines#^thm-140-1|Theorem §140.1]]), $|PC| = r$ is
>
> $$
> \sqrt{(x - h)^2 + (y - k)^2} = r ,
> $$
>
> and since both sides are $\ge 0$, this is equivalent to its square, $(x - h)^2 + (y - k)^2 = r^2$.

^pf-141-1

*Uses:* [[§140 Coordinate Geometry and Lines#^thm-140-1|§140.1]]

> [!example] Example §141.1: Writing and Recognizing a Circle
> **(a)** The circle with radius $3$ and center $(2, -5)$ is $(x - 2)^2 + (y + 5)^2 = 9$, by [[§141 Graphs of Second-Degree Equations#^thm-141-1|Theorem §141.1]] with $h = 2$, $k = -5$, $r = 3$.
>
> **(b)** Show that $x^2 + y^2 + 2x - 6y + 7 = 0$ is a circle, and find its center and radius. Group the $x$-terms and the $y$-terms: $(x^2 + 2x) + (y^2 - 6y) = -7$. Complete the square in each group, adding the squares of half the coefficients of $x$ and $y$ to both sides:
>
> $$
> (x^2 + 2x + 1) + (y^2 - 6y + 9) = -7 + 1 + 9, \qquad\text{or}\qquad (x + 1)^2 + (y - 3)^2 = 3 .
> $$
>
> This is a circle with center $(-1, 3)$ and radius $\sqrt3$.
>
> *Stewart: Appendix C, Examples 1 and 2*

^ex-141-1

## Parabolas

> [!definition] Definition §141.2: Parabola as a Graph
> Here a **parabola** is the graph of an equation $y = ax^2 + bx + c$ with $a \ne 0$ (or, with $x$ and $y$ interchanged, $x = ay^2 + by + c$). The point where the parabola changes direction is its **vertex**. (The geometric definition by focus and directrix is [[§77 Conic Sections#^def-77-1|Definition §77.1]].)
>
> *Stewart: Appendix C (text)*

^def-141-2

> [!theorem] Proposition §141.2: The Parabolas y = ax² and x = ay²
> The parabola $y = ax^2$ has its vertex at the origin and opens upward if $a > 0$, downward if $a < 0$; the larger $|a|$, the narrower it is. The parabola $x = ay^2$ has its vertex at the origin and opens to the right if $a > 0$, to the left if $a < 0$.
>
> *Stewart: Appendix C (text)*

^prop-141-2

> [!proof]+ Proof
> If $a > 0$ then $y = ax^2 \ge 0$, with equality only at $x = 0$; $y$ decreases for $x < 0$ and increases for $x > 0$ (since $x^2$ does). So the graph lies above the $x$-axis except at the vertex $(0, 0)$. For $a < 0$ all signs reverse. Since $|y| = |a|x^2$, a larger $|a|$ gives larger $|y|$ for the same $x$: a narrower parabola. Interchanging $x$ and $y$ reflects the plane in the line $y = x$, which takes "upward" to "to the right", so $x = ay^2$ opens to the right for $a > 0$ and to the left for $a < 0$.

^pf-141-2

*Uses:* [[§141 Graphs of Second-Degree Equations#^def-141-2|Def. §141.2]]

> [!theorem] Theorem §141.3: Symmetry Tests
> The graph of an equation is
> - **symmetric with respect to the $y$-axis** if the equation is unchanged when $x$ is replaced by $-x$;
> - **symmetric with respect to the $x$-axis** if the equation is unchanged when $y$ is replaced by $-y$.
>
> For example, $y = ax^2$ is symmetric about the $y$-axis and $x = ay^2$ about the $x$-axis.
>
> *Stewart: Appendix C (boxed statements)*

^thm-141-3

> [!proof]+ Proof
> If the equation is unchanged when $x$ is replaced by $-x$, then whenever $(x, y)$ satisfies it, so does $(-x, y)$. So the reflection $(-x, y)$ in the $y$-axis of every point $(x, y)$ of the graph is again on the graph: reflecting the right half about the $y$-axis gives the left half. The $x$-axis case is the same with $(x, -y)$.

^pf-141-3

*Uses:* [[§141 Graphs of Second-Degree Equations#^def-141-1|Def. §141.1]]

> [!example] Example §141.2: A Region Bounded by a Parabola and a Line
> Sketch the region bounded by $x = y^2$ and $y = x - 2$.
>
> **Intersections.** Substituting $x = y + 2$ into $x = y^2$ gives $y + 2 = y^2$, so $0 = y^2 - y - 2 = (y - 2)(y + 1)$ and $y = 2$ or $y = -1$. The points of intersection are $(4, 2)$ and $(1, -1)$.
>
> **Sketch.** Draw the line $y = x - 2$ through these points, and the parabola $x = y^2$ (opening to the right, [[§141 Graphs of Second-Degree Equations#^prop-141-2|Proposition §141.2]]) through them. The region bounded by the two curves is the finite region between them: to the right of the parabola and to the left of the line, for $-1 \le y \le 2$. (This is the setting of area computations with respect to $y$ in [[§45 Areas Between Curves#^thm-45-3|Theorem §45.3]].)
>
> *Stewart: Appendix C, Example 4*

^ex-141-2

## Ellipses and Hyperbolas

> [!definition] Definition §141.3: Intercepts
> The **$x$-intercepts** of a graph are the $x$-coordinates of the points where it meets the $x$-axis; they are found by setting $y = 0$ in its equation. The **$y$-intercepts** are the $y$-coordinates of the points where it meets the $y$-axis, found by setting $x = 0$.
>
> *Stewart: Appendix C (boxed statement)*

^def-141-3

> [!definition] Definition §141.4: Ellipse and Hyperbola in Standard Position
> For positive numbers $a$ and $b$, the curve
>
> $$
> \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \qquad (2)
> $$
>
> is an **ellipse** in standard position, and the curves
>
> $$
> \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1 \qquad (3) \qquad\qquad \frac{y^2}{a^2} - \frac{x^2}{b^2} = 1
> $$
>
> are **hyperbolas** in standard position. (Their geometric properties: [[§77 Conic Sections#^thm-77-3|Theorem §77.3]] and [[§77 Conic Sections#^thm-77-5|Theorem §77.5]].)
>
> *Stewart: Appendix C, Equations 2 and 3*

^def-141-4

> [!remark]- Connections
> - See also: [[§59★ Quadratic Forms#^prop-59-3|235 Prop. §59.3]] (a level curve $\mathbf{x}^TA\mathbf{x} = c$ of a quadratic form in two variables is an ellipse or hyperbola, in standard position exactly when $A$ is diagonal; otherwise the eigenvectors of $A$ rotate it into standard position), worked in [[§59★ Quadratic Forms#^ex-59-3|235 Ex. §59.3]].

> [!theorem] Proposition §141.4: Sketching Ellipses and Hyperbolas
> (a) The ellipse (2) is symmetric about both axes, with $x$-intercepts $\pm a$ and $y$-intercepts $\pm b$. If $a = b$ it is the circle of radius $a$.
>
> (b) The hyperbola (3) is symmetric about both axes, has $x$-intercepts $\pm a$ and no $y$-intercept, and consists of two **branches**, $x \ge a$ and $x \le -a$. Both branches approach the **asymptotes** $y = \pm(b/a)x$. Interchanging $x$ and $y$, the hyperbola $\frac{y^2}{a^2} - \frac{x^2}{b^2} = 1$ has $y$-intercepts $\pm a$ and asymptotes $y = \pm(a/b)x$.
>
> *Stewart: Appendix C (text)*

^prop-141-4

> [!proof]+ Proof
> Both equations are unchanged when $x$ is replaced by $-x$ or $y$ by $-y$, so both curves are symmetric about both axes ([[§141 Graphs of Second-Degree Equations#^thm-141-3|Theorem §141.3]]). In (2), $y = 0$ gives $x^2 = a^2$, so $x = \pm a$, and $x = 0$ gives $y = \pm b$; with $a = b$, (2) is $x^2 + y^2 = a^2$. In (3), $y = 0$ gives $x = \pm a$, while $x = 0$ gives $y^2 = -b^2$, which is impossible. From (3), $\frac{x^2}{a^2} = 1 + \frac{y^2}{b^2} \ge 1$, so $x^2 \ge a^2$ and $|x| = \sqrt{x^2} \ge a$: $x \ge a$ or $x \le -a$. The asymptotes are proved in [[§77 Conic Sections#^thm-77-5|Theorem §77.5]] (Stewart: "this involves the idea of a limit").

^pf-141-4

*Uses:* [[§141 Graphs of Second-Degree Equations#^thm-141-3|§141.3]], [[§141 Graphs of Second-Degree Equations#^def-141-3|Def. §141.3]], [[§77 Conic Sections#^thm-77-5|§77.5]]

> [!example] Example §141.3: Sketching an Ellipse and a Hyperbola
> **(a)** $9x^2 + 16y^2 = 144$. Dividing by $144$: $\frac{x^2}{16} + \frac{y^2}{9} = 1$, the ellipse (2) with $a = 4$, $b = 3$. Its $x$-intercepts are $\pm4$ and its $y$-intercepts $\pm3$.
>
> **(b)** $9x^2 - 4y^2 = 36$. Dividing by $36$: $\frac{x^2}{4} - \frac{y^2}{9} = 1$, the hyperbola (3) with $a^2 = 4$, $b^2 = 9$. Its $x$-intercepts are $\pm2$ and its asymptotes $y = \pm\frac32 x$; draw the asymptotes first, then the branches through $(\pm2, 0)$.
>
> *Stewart: Appendix C, Examples 5 and 6*

^ex-141-3

> [!remark] Remark: Equilateral Hyperbolas
> If $b = a$, the hyperbola $x^2 - y^2 = a^2$ (or $y^2 - x^2 = a^2$) is called **equilateral**. Its asymptotes $y = \pm x$ are perpendicular. Rotated by $45°$, its asymptotes become the coordinate axes, and its equation becomes $xy = k$ for a constant $k$. (Stewart: "it can be shown". In coordinates $X = (x + y)/\sqrt2$, $Y = (y - x)/\sqrt2$, rotated by $45°$, $x^2 - y^2 = (x - y)(x + y) = -2XY$, so $x^2 - y^2 = a^2$ becomes $XY = -a^2/2$; rotating the other way gives $k = a^2/2$.)

^rem-141-1

## Shifted Conics

> [!theorem] Theorem §141.5: Shifting a Graph
> Replacing $x$ by $x - h$ and $y$ by $y - k$ in an equation shifts its graph $h$ units horizontally and $k$ units vertically. For instance, the ellipse
>
> $$
> \frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1 \qquad (5)
> $$
>
> is the ellipse (2) with its center moved to $(h, k)$, and $y - k = a(x - h)^2$, or $y = a(x - h)^2 + k$, is the parabola $y = ax^2$ with its vertex moved to $(h, k)$.
>
> *Stewart: Appendix C, (4) and (5)*

^thm-141-5

> [!proof]+ Proof
> A point $(x, y)$ satisfies the new equation exactly when the point $(x - h, y - k)$ satisfies the original one. So $(x, y)$ is on the new graph if and only if it is obtained from a point $(x - h, y - k)$ of the original graph by adding $h$ to the first coordinate and $k$ to the second.

^pf-141-5

*Uses:* [[§141 Graphs of Second-Degree Equations#^def-141-1|Def. §141.1]]

> [!example] Example §141.4: Shifted Parabolas
> **(a)** Sketch $y = 2x^2 - 4x + 1$. Complete the square: $y = 2(x^2 - 2x) + 1 = 2(x^2 - 2x + 1) - 2 + 1 = 2(x - 1)^2 - 1$. By [[§141 Graphs of Second-Degree Equations#^thm-141-5|Theorem §141.5]] this is the parabola $y = 2x^2$ shifted so that its vertex is at $(1, -1)$; it opens upward and crosses the $y$-axis at $1$.
>
> **(b)** Sketch $x = 1 - y^2$. Start with $x = -y^2$, which opens to the left ([[§141 Graphs of Second-Degree Equations#^prop-141-2|Proposition §141.2]] with $a = -1$), and shift it one unit to the right: the vertex is $(1, 0)$, and the $y$-intercepts are $\pm1$.
>
> *Stewart: Appendix C, Examples 7 and 8*

^ex-141-4
