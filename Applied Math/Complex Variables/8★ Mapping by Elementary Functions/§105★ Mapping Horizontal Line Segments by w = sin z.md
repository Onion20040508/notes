---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: 105
bc: "105"
aliases: ["B&C 105"]
tags: [complex-variables, math342, extension]
---
← [[§104★ Mapping Vertical Line Segments by w = sin z]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§106★ Some Related Mappings]] →

*Brown–Churchill, Section 105.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

The second family of curves for $w = \sin z$: horizontal segments of length $2\pi$ go onto ellipses, all with the same foci $\pm1$ as the hyperbolas of [[§104★ Mapping Vertical Line Segments by w = sin z|§104]]. As the segment drops to the real axis, the ellipse flattens onto the focal segment $[-1, 1]$. Sweeping a rectangle by horizontal segments gives a half ellipse, and a rectangle above the axis gives an elliptical ring cut along a radius. Together the two families form the elliptic coordinate system: the image of the Cartesian grid under $\sin z$ is a net of confocal ellipses and hyperbolas crossing at right angles.

## Horizontal Segments

> [!theorem] Proposition §105.1: Horizontal Segments Go onto Ellipses
> Let $c_2 > 0$. Under $w = \sin z$, the segment $y = c_2$, $-\pi \le x \le \pi$ goes onto the ellipse
>
> $$
> \frac{u^2}{\cosh^2 c_2} + \frac{v^2}{\sinh^2 c_2} = 1 , \qquad (2)
> $$
>
> whose foci are $w = \pm\sqrt{\cosh^2 c_2 - \sinh^2 c_2} = \pm1$. As the point $(x, c_2)$ moves to the right from $x = -\pi$ to $x = \pi$, its image makes one circuit around the ellipse in the clockwise direction. As $c_2$ decreases the ellipses shrink, keeping the foci $\pm1$. In the limiting case $c_2 = 0$, the interval $-\pi \le x \le \pi$ goes onto the segment $-1 \le u \le 1$, but not one to one.
>
> *B&C: Sec. 105 (text)*

^prop-105-1

> [!proof]+ Proof
> By (1) of [[§104★ Mapping Vertical Line Segments by w = sin z|§104]] (that is, [[§37 The Trigonometric Functions sin z and cos z#^prop-37-5|Proposition §37.5]]), the image of the segment has the parametric representation
>
> $$
> u = \sin x\cosh c_2, \qquad v = \cos x\sinh c_2 \qquad (-\pi \le x \le \pi) . \qquad (1)
> $$
>
> Since $\cosh c_2 > 0$ and $\sinh c_2 > 0$, the point $\big(u/\cosh c_2,\ v/\sinh c_2\big) = (\sin x, \cos x)$ lies on the unit circle, which is (2). As $x$ runs from $-\pi$ to $\pi$, the point $(\sin x, \cos x)$ starts at the bottom $(0, -1)$, passes through $(-1, 0)$ at $x = -\pi/2$, the top $(0, 1)$ at $x = 0$, and $(1, 0)$ at $x = \pi/2$, and returns to the bottom: one clockwise circuit, one to one except that $x = \pm\pi$ give the same point. Stretching the axes by $\cosh c_2$ and $\sinh c_2$ carries this onto (2). The semi-axes $\cosh c_2 > \sinh c_2$ give foci at $\pm\sqrt{\cosh^2 c_2 - \sinh^2 c_2} = \pm1$, and both semi-axes decrease as $c_2$ decreases. For $c_2 = 0$, (1) becomes $u = \sin x$, $v = 0$, which covers $[-1, 1]$ twice as $x$ runs over $[-\pi, \pi]$.

^pf-105-1

*Uses:* [[§37 The Trigonometric Functions sin z and cos z#^prop-37-5|§37.5]]

> [!remark] Remark: Ellipses by Their Foci
> The ellipse (2) is the set of $w$ with $|w - 1| + |w + 1| = 2\cosh c_2$ (sum of focal distances equal to the major axis). Since $|w - 1| + |w + 1| \ge 2$, with equality exactly on the segment $[-1, 1]$, every $w$ off that segment lies on exactly one ellipse (2), namely the one with $\cosh c_2 = \frac12\big(|w - 1| + |w + 1|\big)$. This is the "fill" step of the sweeping method ([[§104★ Mapping Vertical Line Segments by w = sin z#^rem-104-1|§104, Method]]) for horizontal segments.

^rem-105-1

## Examples

> [!example] Example §105.1: A Rectangle onto a Half Ellipse
> The rectangle $-\pi/2 \le x \le \pi/2$, $0 \le y \le b$ is mapped by $w = \sin z$ one to one onto the semi-elliptical region
>
> $$
> \frac{u^2}{\cosh^2 b} + \frac{v^2}{\sinh^2 b} \le 1, \qquad v \ge 0 .
> $$
>
> Let $L$ be the segment $y = c_2$, $-\pi/2 \le x \le \pi/2$, with $0 < c_2 \le b$. By the proof of Proposition §105.1, its image $L'$ is the part of the ellipse (2) traced from $(-\cosh c_2, 0)$ through $(0, \sinh c_2)$ to $(\cosh c_2, 0)$, that is, the top half (where $v = \cos x\sinh c_2 \ge 0$), one to one. As $c_2$ decreases, $L$ moves down toward the $x$ axis and $L'$ moves down and tends to the segment $E'F'A'$ from $w = -1$ to $w = 1$. For $c_2 = 0$, $u = \sin x$, $v = 0$ ($-\pi/2 \le x \le \pi/2$), clearly a one to one map of $EFA$ onto $E'F'A'$.
>
> By the [[§105★ Mapping Horizontal Line Segments by w = sin z#^rem-105-1|focal property]] above, each point of the closed semi-elliptical region lies on exactly one of the semi-ellipses ($0 < c_2 \le b$) or on the limiting segment $E'F'A'$, so it is the image of exactly one point of the rectangle. Corresponding boundary points: the top $DCB$ ($y = b$) goes onto the semi-ellipse $D'C'B'$; the side $x = \pi/2$ from $A$ to $B$ onto $1 \le u \le \cosh b$; the side $x = -\pi/2$ from $E$ to $D$ onto $-\cosh b \le u \le -1$.
>
> *B&C: Sec. 105, Example*

^ex-105-1

![[m342-105-1.svg]]
*The rectangle $|x| \le \frac\pi2$, $0 \le y \le 1$ under $w = \sin z$. Horizontal segments $y = 0.25, 0.5, 0.75, 1$ (red) go onto upper halves of ellipses with foci $\pm1$; vertical segments $x = \pm0.5, \pm1$ (blue) onto arcs of the confocal hyperbolas of §104, crossing the ellipses at right angles. The base (green) goes onto $[-1, 1]$ and the sides (black) onto $1 \le |u| \le \cosh 1 \approx 1.54$.*

> [!example] Example §105.2: The Half Strip Again, by Horizontal Segments
> Verify by horizontal segments that $w = \sin z$ maps the open region $-\pi/2 < x < \pi/2$, $y > 0$ one to one onto the half plane $v > 0$.
>
> For $c_2 > 0$, the open segment $y = c_2$, $-\pi/2 < x < \pi/2$ goes one to one onto the top half of the ellipse (2) without its two endpoints on the $u$ axis, that is, onto the points of (2) with $v > 0$ (here $v = \cos x\sinh c_2 > 0$). These open semi-ellipses lie in $v > 0$, and by the [[§105★ Mapping Horizontal Line Segments by w = sin z#^rem-105-1|focal property]] above every point with $v > 0$ (which is off the segment $[-1, 1]$) lies on exactly one of them. So each point of the half plane is the image of exactly one point of the open half strip. This agrees with [[§104★ Mapping Vertical Line Segments by w = sin z#^ex-104-1|Example §104.1]].
>
> *B&C: Sec. 106, Exercise 7*

^ex-105-2

> [!example] Example §105.3: A Quarter of the Rectangle
> Find the image of the rectangle $0 \le x \le \pi/2$, $0 \le y \le 1$ under $w = \sin z$.
>
> **Boundary.** By (1):
> - the bottom $y = 0$, $0 \le x \le \pi/2$ goes onto $u = \sin x$, $v = 0$: the segment $0 \le u \le 1$;
> - the right side $x = \pi/2$, $0 \le y \le 1$ goes onto $u = \cosh y$, $v = 0$: the segment $1 \le u \le \cosh 1$;
> - the top $y = 1$, $0 \le x \le \pi/2$ goes onto $u = \sin x\cosh 1$, $v = \cos x\sinh 1$: the quarter of the ellipse $\dfrac{u^2}{\cosh^2 1} + \dfrac{v^2}{\sinh^2 1} = 1$ in the first quadrant, from $i\sinh 1$ to $\cosh 1$;
> - the left side $x = 0$, $0 \le y \le 1$ goes onto $u = 0$, $v = \sinh y$: the segment of the $v$ axis from $0$ to $i\sinh 1$.
>
> Here $\cosh 1 \approx 1.5431$ and $\sinh 1 \approx 1.1752$.
>
> **Interior.** Each segment $y = c_2$, $0 < x < \pi/2$, with $0 < c_2 < 1$, goes one to one onto the open quarter of the ellipse (2) in the open first quadrant ($u = \sin x\cosh c_2 > 0$, $v = \cos x\sinh c_2 > 0$). By the [[§105★ Mapping Horizontal Line Segments by w = sin z#^rem-105-1|focal property]] above these quarter ellipses are disjoint and fill the open region bounded by the quarter ellipse of the top side and the two axes. So $w = \sin z$ maps the interior of the rectangle one to one onto the interior of that quarter-elliptical region.
>
> *B&C: Sec. 106, Exercise 8*

^ex-105-3

> [!example] Example §105.4: A Rectangle onto a Cut Elliptical Ring
> Let $0 < a < b$. Verify that the interior of the rectangle $-\pi \le x \le \pi$, $a \le y \le b$ is mapped by $w = \sin z$ onto the interior of an elliptical ring cut along the segment $-\sinh b \le v \le -\sinh a$ of the negative imaginary axis.
>
> The horizontal segments $y = c_2$, $a < c_2 < b$, $-\pi < x < \pi$, go one to one onto the ellipses (2) minus their lowest point $(0, -\sinh c_2)$ (Proposition §105.1: only $x = \pm\pi$ give that point). By the [[§105★ Mapping Horizontal Line Segments by w = sin z#^rem-105-1|focal property]] above, these punctured ellipses are disjoint and fill the region between the ellipses for $c_2 = a$ and $c_2 = b$, except for the points $(0, -\sinh c_2)$, which make up the open segment $-\sinh b < v < -\sinh a$ of the negative $v$ axis. So the interior of the rectangle goes one to one onto the ring with that cut.
>
> The boundary is not mapped one to one: the two vertical sides $x = \pm\pi$ both go onto the cut, since $\sin(\pm\pi + iy) = \sin(\pm\pi)\cosh y + i\cos(\pm\pi)\sinh y = -i\sinh y$; and the top and bottom go onto the outer and inner ellipses, each with its lowest point covered twice.
>
> *B&C: Sec. 106, Exercise 9*

^ex-105-4
