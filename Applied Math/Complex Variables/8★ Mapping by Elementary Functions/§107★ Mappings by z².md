---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: 107
bc: "107"
aliases: ["B&C 107"]
tags: [complex-variables, math342, extension]
---
← [[§106★ Some Related Mappings]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§108★ Mappings by Branches of z^(1∕2)]] →

*Brown–Churchill, Section 107.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

The mapping $w = z^2$ was met in [[§14 The Mapping w = z²|§14]]: it squares moduli and doubles arguments, so it opens a quadrant into a half plane. Here it is used on less simple regions. Vertical and horizontal lines go onto parabolas, all with focus at the origin, and sweeping a vertical half strip by its vertical half lines gives a semiparabolic region. Composed with $\sin z$, it turns the half strip of [[§104★ Mapping Vertical Line Segments by w = sin z|§104]] into a half plane.

## Parabolas

With $z = x + iy$ and $w = u + iv$, the transformation $w = z^2$ reads ([[§14 The Mapping w = z²|§14]])

$$
u = x^2 - y^2, \qquad v = 2xy . \qquad (1)
$$

Eliminating one of the variables from (1) shows what the coordinate lines become: a vertical line $x = x_1$ goes onto the parabola $v^2 = -4x_1^2(u - x_1^2)$, opening to the left, and a horizontal line $y = y_1$ onto $v^2 = 4y_1^2(u + y_1^2)$, opening to the right. All of these parabolas have their focus at $w = 0$. The two examples below work out the first family; the second is Example §107.3.

> [!remark] Remark: Recovering the Line from the Point
> For the "fill" step of the sweeping method ([[§104★ Mapping Vertical Line Segments by w = sin z#^rem-104-1|§104, Method]]) it helps to solve for the parameter. If $w = (x_1 + iy)^2$ with $x_1 > 0$, then $t = x_1^2$ satisfies $v^2 = -4t(u - t)$, that is $4t^2 - 4ut - v^2 = 0$, whose only positive root is
>
> $$
> x_1^2 = \frac{|w| + u}{2} .
> $$
>
> Likewise a point on the image of $y = y_1 > 0$ has $y_1^2 = \frac{|w| - u}{2}$. These are the squares of the real and imaginary parts of the principal square root of $w$ ([[§108★ Mappings by Branches of z^(1∕2)|§108]]), as they should be.

^rem-107-1

## Examples

> [!example] Example §107.1: A Vertical Half Strip onto a Semiparabolic Region
> Show that the image of the vertical strip $0 \le x \le 1$, $y \ge 0$ under $w = z^2$ is the closed semiparabolic region bounded by the top half of the parabola $v^2 = -4(u - 1)$ and the negative $u$ axis (with $v \ge 0$), and that the correspondence is one to one.
>
> **Half lines.** When $0 < x_1 < 1$, the point $(x_1, y)$ moves up the vertical half line $L_1$ as $y$ increases from $0$. By (1) its image has the parametric representation
>
> $$
> u = x_1^2 - y^2, \qquad v = 2x_1y \qquad (0 \le y < \infty) . \qquad (2)
> $$
>
> Substituting $y = v/(2x_1)$ from the second equation into the first,
>
> $$
> v^2 = -4x_1^2(u - x_1^2) , \qquad (3)
> $$
>
> a parabola with vertex $(x_1^2, 0)$ and focus at the origin. Since $v = 2x_1y$ increases with $y$ from $v = 0$, as $(x_1, y)$ moves up $L_1$ its image moves up the top half $L_1'$ of the parabola, one to one. For $x_1 < x_2 < 1$, the image $L_2'$ of $L_2$ is a half parabola to the right of $L_1'$; the image of the half line $BA$ ($x = 1$) is the top half of $v^2 = -4(u - 1)$, labeled $B'A'$.
>
> **The edge $CD$.** A point $(0, y)$, $y \ge 0$, goes to $(-y^2, 0)$: as it moves up from the origin, its image moves left from the origin along the $u$ axis. So as the half lines move to the left, their image half parabolas shrink down to the half line $C'D'$.
>
> **Fill (B&C says "it is now clear").** Let $w$ be in the closed region. If $v > 0$, [[§107★ Mappings by z²#^rem-107-1|the remark above]] gives exactly one $x_1 = \sqrt{(|w| + u)/2} > 0$ whose parabola (3) passes through $w$, and $x_1 \le 1$ exactly because $w$ is on or inside $B'A'$; then $y = v/(2x_1) > 0$ is determined. If $v = 0$ and $u < 0$, the only preimage in the strip is on $CD$; if $v = 0$ and $0 \le u \le 1$, it is $(\sqrt u, 0)$ on $CB$. So each point of the semiparabolic region is the image of exactly one point of the strip.
>
> *B&C: Sec. 107, Example 1*

^ex-107-1

![[m342-107-1.svg]]
*The half strip $0 \le x \le 1$, $y \ge 0$ under $w = z^2$. Vertical half lines $x = 0.25, 0.5, 0.75, 1$ (blue) go onto upper halves of parabolas $v^2 = -4x_1^2(u - x_1^2)$ with focus at the origin; the segments $y = 0.5, 1, 1.5$ (red) onto arcs of the confocal parabolas opening the other way. The edge $CD$ (green) is folded onto the negative $u$ axis and the base $CB$ (black) onto $[0, 1]$.*

> [!example] Example §107.2: sin² z Maps a Half Strip onto a Half Plane
> Show that $w = \sin^2 z$ maps the semi-infinite vertical strip $0 \le x \le \pi/2$, $y \ge 0$ onto the upper half plane $v \ge 0$.
>
> Write
>
> $$
> Z = \sin z, \qquad w = Z^2 . \qquad (4)
> $$
>
> By [[§104★ Mapping Vertical Line Segments by w = sin z#^ex-104-2|Example §104.2]], the first map takes the strip one to one onto the first quadrant $X \ge 0$, $Y \ge 0$ of the $Z$ plane. The second squares moduli and doubles arguments ([[§14 The Mapping w = z²|§14]]): $Z = Re^{i\Theta}$ with $0 \le \Theta \le \pi/2$ goes to $R^2e^{2i\Theta}$ with $0 \le 2\Theta \le \pi$, one to one onto $v \ge 0$. So the composition maps the strip onto the upper half plane. On the boundary: the base $0 \le x \le \pi/2$ goes onto $0 \le u \le 1$, the wall $x = \pi/2$ onto $u \ge 1$, and the $y$ axis (through $Z = i\sinh y$, $w = -\sinh^2 y$) onto $u \le 0$.
>
> *B&C: Sec. 107, Example 2*

^ex-107-2

> [!example] Example §107.3: Horizontal Lines and Horizontal Strips
> **(a)** Under $w = z^2$, a horizontal line $y = y_1$ ($y_1 > 0$) has, by (1), the image $u = x^2 - y_1^2$, $v = 2xy_1$ ($-\infty < x < \infty$). Eliminating $x = v/(2y_1)$,
>
> $$
> v^2 = 4y_1^2(u + y_1^2) ,
> $$
>
> a parabola opening to the right with vertex $(-y_1^2, 0)$ and focus at $w = 0$. Since $v = 2xy_1$ increases with $x$, the line traversed left to right goes onto the parabola traversed upward, one to one.
>
> **(b)** Hence $w = z^2$ maps the horizontal strip $a \le y \le b$ ($0 < a < b$) one to one onto the closed region between the parabolas
>
> $$
> v^2 = 4a^2(u + a^2) \qquad\text{and}\qquad v^2 = 4b^2(u + b^2) .
> $$
>
> Indeed, as $y_1$ increases from $a$ to $b$ the parabolas move outward (vertex $-y_1^2$ moving left), and by [[§107★ Mappings by z²#^rem-107-1|the remark above]] a point $w$ lies on the parabola for $y_1 = \sqrt{(|w| - u)/2}$ only; so it lies in the region exactly when $a \le y_1 \le b$, and on that parabola it comes from the single point $x = v/(2y_1)$.
>
> *B&C: Sec. 108, Exercises 1 and 2*

^ex-107-3

> [!example] Example §107.4: A Triangle onto a Parabolic Region
> Show that $w = z^2$ maps the closed triangle bounded by the lines $y = \pm x$ and $x = 1$ onto the closed region bounded on the left by the segment $-2 \le v \le 2$ of the $v$ axis and on the right by a portion of the parabola $v^2 = -4(u - 1)$.
>
> **Boundary.** The side $x = 1$, $-1 \le y \le 1$ goes onto $u = 1 - y^2$, $v = 2y$, the arc of $v^2 = -4(u - 1)$ from $-2i$ through $1$ to $2i$. The side $y = x$, $0 \le x \le 1$ goes onto $u = 0$, $v = 2x^2$, the segment from $0$ to $2i$; the side $y = -x$ onto $u = 0$, $v = -2x^2$, the segment from $0$ to $-2i$.
>
> **Interior.** The triangle is swept by the vertical segments $x = x_1$, $|y| \le x_1$, $0 < x_1 \le 1$. As in Example §107.1, each goes one to one onto the arc of the parabola (3) with $|v| \le 2x_1^2$, which lies in $u = x_1^2 - y^2 \ge 0$; by [[§107★ Mappings by z²#^rem-107-1|the remark above]] these arcs are disjoint and fill the region, $x_1$ being recovered from $w$ as $\sqrt{(|w| + u)/2}$.
>
> *B&C: Sec. 108, Exercise 4*

^ex-107-4
