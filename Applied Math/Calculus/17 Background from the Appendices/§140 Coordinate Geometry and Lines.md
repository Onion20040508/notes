---
type: section
subject: "[[Calculus]]"
chapter: 17
section: 140
stewart: "Appendix B"
aliases: ["Stewart Appendix B"]
tags: [calculus]
---
← [[§139 Numbers, Inequalities, and Absolute Values]] · ↑ [[· 17 Background from the Appendices]] · [[§141 Graphs of Second-Degree Equations]] →

*Stewart, Appendix B.*

Points of the plane are identified with ordered pairs of real numbers, as points of a line were identified with real numbers in [[§139 Numbers, Inequalities, and Absolute Values#^def-139-2|Definition §139.2]]. The Pythagorean Theorem then gives the distance between two points, and the slope, the constant rate of change of $y$ with respect to $x$, gives the equations of lines: point-slope, slope-intercept, and the general linear equation $Ax + By + C = 0$. Slopes also decide when lines are parallel or perpendicular. All of this is used constantly, starting with tangent lines in [[§14 Derivatives and Rates of Change#^def-14-1|Definition §14.1]].

## The Coordinate Plane

> [!definition] Definition §140.1: Cartesian Coordinates
> Draw two perpendicular coordinate lines meeting at the origin $O$ of each: the horizontal **$x$-axis**, positive to the right, and the vertical **$y$-axis**, positive upward. For a point $P$, draw the lines through $P$ perpendicular to the axes; they meet the axes at coordinates $a$ and $b$. Then $P$ is assigned the ordered pair $(a, b)$: $a$ is the **$x$-coordinate** and $b$ the **$y$-coordinate** of $P$, and we write $P(a, b)$ or simply "the point $(a, b)$". (The context distinguishes it from the open interval $(a, b)$.)
>
> This is the **rectangular** or **Cartesian coordinate system** (after Descartes; Fermat found the principles of analytic geometry at the same time). The plane with this system is the **coordinate plane** or **Cartesian plane**, $\mathbb{R}^2$. The **coordinate axes** divide it into four **quadrants**, I to IV counterclockwise; the first quadrant consists of the points with both coordinates positive.
>
> *Stewart: Appendix B (text)*

^def-140-1

> [!example] Example §140.1: Regions Described by Sets
> Describe and sketch (a) $\{(x, y) \mid x \ge 0\}$, (b) $\{(x, y) \mid y = 1\}$, (c) $\{(x, y) \mid |y| < 1\}$.
>
> **(a)** The points whose $x$-coordinate is $0$ or positive: the $y$-axis together with everything to its right (a closed half-plane).
>
> **(b)** The points with $y$-coordinate $1$: the horizontal line one unit above the $x$-axis.
>
> **(c)** By [[§139 Numbers, Inequalities, and Absolute Values#^thm-139-5|Theorem §139.5]], $|y| < 1$ if and only if $-1 < y < 1$. So the region consists of the points between, but not on, the horizontal lines $y = 1$ and $y = -1$ (drawn dashed to show that they are excluded): an open horizontal strip.
>
> *Stewart: Appendix B, Example 1*

^ex-140-1

> [!theorem] Theorem §140.1: Distance Formula
> The distance between the points $P_1(x_1, y_1)$ and $P_2(x_2, y_2)$ is
>
> $$
> |P_1P_2| = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} .
> $$
>
> *Stewart: Appendix B, (1) Distance Formula*

^thm-140-1

> [!proof]+ Proof
> Let $P_3 = (x_2, y_1)$. The distance between points on a horizontal line is the distance between their $x$-coordinates on the number line, so $|P_1P_3| = |x_2 - x_1|$ ([[§139 Numbers, Inequalities, and Absolute Values#^def-139-6|Definition §139.6]]); likewise $|P_2P_3| = |y_2 - y_1|$ on the vertical line $x = x_2$. The triangle $P_1P_2P_3$ has a right angle at $P_3$, so by the Pythagorean Theorem
>
> $$
> |P_1P_2| = \sqrt{|P_1P_3|^2 + |P_2P_3|^2} = \sqrt{|x_2 - x_1|^2 + |y_2 - y_1|^2} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} ,
> $$
>
> since $|a|^2 = a^2$. (If $x_1 = x_2$ or $y_1 = y_2$ the triangle degenerates, and the formula reduces to the distance on a line, by [[§139 Numbers, Inequalities, and Absolute Values#^prop-139-3|Proposition §139.3]].)

^pf-140-1

*Uses:* [[§139 Numbers, Inequalities, and Absolute Values#^def-139-6|Def. §139.6]], [[§139 Numbers, Inequalities, and Absolute Values#^prop-139-3|§139.3]], Pythagorean Theorem

> [!remark]- Connections
> - This is the Euclidean distance $\|P_2 - P_1\|$ of $\mathbb{R}^2$, the norm from the dot product ([[§20 Inner Products and Norms#^ladr-6-7|LADR 6.7]]), and the standard example of a metric ([[§13 Some Topological Concepts in Metric Spaces#^def-13-1|451 Def. §13.1]]).

## Lines

An equation of a line $L$ is one satisfied by the coordinates of the points on $L$ and by no other point. It is found from the steepness of the line.

> [!definition] Definition §140.2: Slope
> The **slope** of a nonvertical line through the points $P_1(x_1, y_1)$ and $P_2(x_2, y_2)$ is
>
> $$
> m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1} .
> $$
>
> The slope of a vertical line is not defined.
>
> *Stewart: Appendix B, (2) Definition*

^def-140-2

> [!remark] Remark: What the Slope Measures
> The slope is the ratio of the change in $y$ ("rise") to the change in $x$ ("run"), the rate of change of $y$ with respect to $x$; that a line is straight means that this rate is constant (the value of $m$ does not depend on which two points are used, by similar triangles). Lines with positive slope slant upward to the right, lines with negative slope downward; the larger $|m|$, the steeper the line; a horizontal line has slope $0$.

^rem-140-1

> [!theorem] Theorem §140.2: Point-Slope Form of the Equation of a Line
> An equation of the line passing through the point $P_1(x_1, y_1)$ and having slope $m$ is
>
> $$
> y - y_1 = m(x - x_1) .
> $$
>
> *Stewart: Appendix B, (3)*

^thm-140-2

> [!proof]+ Proof
> A point $P(x, y)$ with $x \ne x_1$ lies on the line if and only if the slope of the line through $P_1$ and $P$ equals $m$, that is, $\dfrac{y - y_1}{x - x_1} = m$, which is equivalent to $y - y_1 = m(x - x_1)$. For $x = x_1$, the only point of the (nonvertical) line is $P_1$ itself, and the equation holds for $x = x_1$ exactly when $y = y_1$. So the points satisfying the equation are exactly the points of the line.

^pf-140-2

*Uses:* [[§140 Coordinate Geometry and Lines#^def-140-2|Def. §140.2]]

> [!theorem] Corollary §140.3: Slope-Intercept Form; Horizontal and Vertical Lines
> An equation of the line with slope $m$ and $y$-intercept $b$ is
>
> $$
> y = mx + b .
> $$
>
> In particular, a horizontal line has equation $y = b$ ($m = 0$). A vertical line has no slope; its equation is $x = a$, where $a$ is its $x$-intercept.
>
> *Stewart: Appendix B, (4)*

^cor-140-3

> [!proof]+ Proof
> The line meets the $y$-axis at $(0, b)$, so the point-slope form with $x_1 = 0$, $y_1 = b$ gives $y - b = m(x - 0)$, that is, $y = mx + b$. With $m = 0$ this is $y = b$. Every point of a vertical line has the same $x$-coordinate $a$, and every point with $x$-coordinate $a$ is on it, so its equation is $x = a$.

^pf-140-3

*Uses:* [[§140 Coordinate Geometry and Lines#^thm-140-2|§140.2]]

> [!theorem] Theorem §140.4: The General Equation of a Line
> The equation of every line can be written in the form
>
> $$
> Ax + By + C = 0 , \qquad (5)
> $$
>
> with constants $A$, $B$ not both $0$. Conversely, the graph of every such first-degree equation is a line. Therefore (5) is called a **linear equation**, or the **general equation of a line**, and one speaks of "the line $Ax + By + C = 0$".
>
> *Stewart: Appendix B, (5)*

^thm-140-4

> [!proof]+ Proof
> A vertical line $x = a$ is $x - a = 0$ ($A = 1$, $B = 0$, $C = -a$). A nonvertical line $y = mx + b$ is $-mx + y - b = 0$ ($A = -m$, $B = 1$, $C = -b$). Conversely, take $A$, $B$ not both $0$. If $B = 0$, then $A \ne 0$ and the equation is $x = -C/A$, a vertical line with $x$-intercept $-C/A$. If $B \ne 0$, solving for $y$ gives
>
> $$
> y = -\frac AB x - \frac CB ,
> $$
>
> the slope-intercept form with $m = -A/B$ and $b = -C/B$.

^pf-140-4

*Uses:* [[§140 Coordinate Geometry and Lines#^cor-140-3|§140.3]]

> [!example] Example §140.2: Distances and Equations of Lines
> **(a) Distance.** The distance between $(1, -2)$ and $(5, 3)$ is $\sqrt{(5 - 1)^2 + [3 - (-2)]^2} = \sqrt{4^2 + 5^2} = \sqrt{41}$.
>
> **(b) Point and slope.** The line through $(1, -7)$ with slope $-\frac12$ is, by [[§140 Coordinate Geometry and Lines#^thm-140-2|Theorem §140.2]], $y + 7 = -\frac12(x - 1)$. Multiplying by $2$: $2y + 14 = -x + 1$, or $x + 2y + 13 = 0$.
>
> **(c) Two points.** For the line through $(-1, 2)$ and $(3, -4)$, [[§140 Coordinate Geometry and Lines#^def-140-2|Definition §140.2]] gives $m = \dfrac{-4 - 2}{3 - (-1)} = -\dfrac32$. The point-slope form with $x_1 = -1$, $y_1 = 2$ is $y - 2 = -\frac32(x + 1)$, that is, $2y - 4 = -3x - 3$, or $3x + 2y = 1$.
>
> *Stewart: Appendix B, Examples 2, 3 and 4*

^ex-140-2

> [!example] Example §140.3: Graphing a Line and a Linear Inequality
> **(a)** Sketch $3x - 5y = 15$. The equation is linear, so its graph is a line ([[§140 Coordinate Geometry and Lines#^thm-140-4|Theorem §140.4]]), and two points determine it. The intercepts are easiest: $y = 0$ gives $3x = 15$, $x = 5$; $x = 0$ gives $-5y = 15$, $y = -3$. The line passes through $(5, 0)$ and $(0, -3)$.
>
> **(b)** Graph the inequality $x + 2y > 5$, that is, the set $\{(x, y) \mid x + 2y > 5\}$. Solve for $y$: $2y > -x + 5$, so $y > -\frac12 x + \frac52$. The line $y = -\frac12 x + \frac52$ has slope $-\frac12$ and $y$-intercept $\frac52$, and the graph consists of the points whose $y$-coordinates are *larger* than those on the line: the half-plane **above** the line, not including the line itself (drawn dashed).
>
> *Stewart: Appendix B, Examples 5 and 6*

^ex-140-3

## Parallel and Perpendicular Lines

> [!theorem] Theorem §140.5: Parallel and Perpendicular Lines
> 1. Two nonvertical lines are parallel if and only if they have the same slope.
> 2. Two lines with slopes $m_1$ and $m_2$ are perpendicular if and only if $m_1m_2 = -1$, that is, their slopes are negative reciprocals: $m_2 = -\dfrac{1}{m_1}$.
>
> *Stewart: Appendix B, (6)*

^thm-140-5

*Stewart omits the proof, referring to Stewart, Redlin and Watson, Precalculus: Mathematics for Calculus; the argument is sketched in the next remark.*

> [!remark] Remark: Why It Works
> **Parallel.** The lines $y = m_1x + b_1$ and $y = m_2x + b_2$ meet where $(m_1 - m_2)x = b_2 - b_1$. If $m_1 \ne m_2$ this has the solution $x = (b_2 - b_1)/(m_1 - m_2)$, so the lines intersect. If $m_1 = m_2$, they are either the same line ($b_1 = b_2$) or never meet. So distinct lines are parallel exactly when their slopes are equal.
>
> **Perpendicular.** Shifting does not change slopes or angles, so take both lines through the origin: $y = m_1x$ through $P_1(1, m_1)$ and $y = m_2x$ through $P_2(1, m_2)$. The lines are perpendicular if and only if the angle $P_1OP_2$ is a right angle, which by the Pythagorean Theorem and its converse happens exactly when $|P_1P_2|^2 = |OP_1|^2 + |OP_2|^2$. By the Distance Formula this reads
>
> $$
> (m_1 - m_2)^2 = (1 + m_1^2) + (1 + m_2^2) \iff -2m_1m_2 = 2 \iff m_1m_2 = -1 .
> $$

^rem-140-2

> [!remark]- Connections
> - In vector form: the direction vectors $\langle 1, m_1 \rangle$ and $\langle 1, m_2 \rangle$ have dot product $1 + m_1m_2$, so perpendicularity is orthogonality, $\langle 1, m_1 \rangle \cdot \langle 1, m_2 \rangle = 0$ ([[§20 Inner Products and Norms#^ladr-6-10|LADR 6.10]]; in Calculus, [[§95 The Dot Product#^thm-95-4|Theorem §95.4]]).

> [!example] Example §140.4: Parallel and Perpendicular Lines
> **(a)** Find an equation of the line through $(5, 2)$ parallel to $4x + 6y + 5 = 0$. In slope-intercept form the given line is $y = -\frac23 x - \frac56$, with slope $-\frac23$. A parallel line has the same slope, so the required line is $y - 2 = -\frac23(x - 5)$, that is, $3y - 6 = -2x + 10$, or $2x + 3y = 16$.
>
> **(b)** Show that $2x + 3y = 1$ and $6x - 4y - 1 = 0$ are perpendicular. In slope-intercept form they are $y = -\frac23 x + \frac13$ and $y = \frac32 x - \frac14$, with slopes $m_1 = -\frac23$ and $m_2 = \frac32$. Since $m_1m_2 = -1$, the lines are perpendicular.
>
> *Stewart: Appendix B, Examples 7 and 8*

^ex-140-4
