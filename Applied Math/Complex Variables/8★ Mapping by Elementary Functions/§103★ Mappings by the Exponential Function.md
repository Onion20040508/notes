---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: "103★"
bc: "103"
aliases: ["B&C 103"]
tags: [complex-variables, math342, extension]
---
← [[§102★ Examples (Mappings of the Upper Half Plane)]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§104★ Mapping Vertical Line Segments by w = sin z]] →

*Brown–Churchill, Section 103.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

The exponential function turns Cartesian coordinates in the $z$ plane into polar coordinates in the $w$ plane: $|e^z| = e^x$ and $\arg e^z = y$. So vertical lines go onto circles, horizontal lines onto rays, rectangles onto pieces of annuli, and a horizontal strip of height $\pi$ onto a half plane. This is how strips, which are easy to handle with linear functions, are converted into half planes and wedges, and it is the inverse of the logarithm used in [[§102★ Examples (Mappings of the Upper Half Plane)#^ex-102-3|Example §102.3]].

## Lines and Rectangles

> [!theorem] Proposition §103.1: The Exponential in Polar Form
> The transformation
>
> $$
> w = e^z \qquad (1)
> $$
>
> can be written $w = e^xe^{iy}$, where $z = x + iy$. Thus if $w = \rho e^{i\phi}$, then
>
> $$
> \rho = e^x, \qquad \phi = y . \qquad (2)
> $$
>
> *B&C: Sec. 103, Equations (1) and (2)*

^prop-103-1

> [!proof]+ Proof
> By definition $e^z = e^xe^{iy}$, with $e^x > 0$ and $|e^{iy}| = 1$. So $e^z$ is written in exponential form with modulus $e^x$ and an argument $y$ ([[§30 The Exponential Function#^prop-30-1|Proposition §30.1]]).

^pf-103-1

*Uses:* [[§30 The Exponential Function#^def-30-1|Def. §30.1]], [[§30 The Exponential Function#^prop-30-1|§30.1]]

> [!remark] Remark: Method — Images under the Exponential
> Sweep the region by vertical segments (each goes onto an arc of the circle $\rho = e^x$) or by horizontal segments (each goes onto a piece of the ray $\phi = y$). The mapping is one to one on any region whose height is less than $2\pi$: by [[§30 The Exponential Function#^prop-30-1|Proposition §30.1]], $e^{z_1} = e^{z_2}$ exactly when $x_1 = x_2$ and $y_1 - y_2$ is a multiple of $2\pi$ (the period of [[§30 The Exponential Function#^prop-30-4|Proposition §30.4]]).

^rem-103-1

> [!example] Example §103.1: Vertical and Horizontal Lines
> The image of a typical point $z = (c_1, y)$ on a vertical line $x = c_1$ has polar coordinates $\rho = \exp c_1$ and $\phi = y$. As $z$ moves up the line, its image moves counterclockwise around the circle $\rho = \exp c_1$. The image of the line is the entire circle, and each point of the circle is the image of infinitely many points of the line, spaced $2\pi$ apart.
>
> A horizontal line $y = c_2$ is mapped one to one onto the ray $\phi = c_2$: the image of $z = (x, c_2)$ has $\rho = e^x$, $\phi = c_2$, and as $x$ increases over all reals, $\rho = e^x$ increases over all positive reals. So as $z$ moves along the line from left to right, its image moves outward along the entire ray, starting arbitrarily close to the origin.
>
> *B&C: Sec. 103, Example 1*

^ex-103-1

> [!example] Example §103.2: A Rectangle onto a Piece of an Annulus
> Show that $w = e^z$ maps the rectangle $a \le x \le b$, $c \le y \le d$ onto the region $e^a \le \rho \le e^b$, $c \le \phi \le d$.
>
> Let $A = (a, c)$, $B = (b, c)$, $C = (b, d)$, $D = (a, d)$. The vertical segment $AD$ goes onto the arc $\rho = e^a$, $c \le \phi \le d$, labeled $A'D'$. The vertical segments to the right of $AD$ go onto larger arcs with the same angular range, and finally $BC$ goes onto the arc $\rho = e^b$, $c \le \phi \le d$, labeled $B'C'$. The vertical segments fill the rectangle and their image arcs fill the region $e^a \le \rho \le e^b$, $c \le \phi \le d$.
>
> The same result comes from horizontal segments: $y = c_2$, $a \le x \le b$, goes onto the part $e^a \le \rho \le e^b$ of the ray $\phi = c_2$, and these radial segments sweep out the region as $c_2$ runs from $c$ to $d$.
>
> The mapping is one to one if $d - c < 2\pi$: two points of the rectangle with the same image have $e^{x_1} = e^{x_2}$, so $x_1 = x_2$, and $y_1 - y_2$ a multiple of $2\pi$, so $y_1 = y_2$. In particular, for $c = 0$ and $d = \pi$ the rectangle goes onto half of a circular ring.
>
> *B&C: Sec. 103, Example 2; Sec. 106, Exercise 2*

^ex-103-2

![[m342-103-1.svg]]
*The rectangle $-0.4 \le x \le 0.7$, $\frac\pi6 \le y \le \frac{2\pi}{3}$ under $w = e^z$. Vertical segments (blue) go onto arcs of the circles $\rho = e^x$, horizontal segments (red) onto pieces of the rays $\phi = y$; right angles between grid lines are preserved. The left side $AD$ goes onto the inner arc $A'D'$, of radius $e^{-0.4} \approx 0.67$.*

## A Strip onto a Half Plane

> [!example] Example §103.3: The Strip 0 ≤ y ≤ π
> When $w = e^z$, the image of the infinite strip $0 \le y \le \pi$ is the upper half $v \ge 0$ of the $w$ plane, with the origin omitted.
>
> By Example §103.1, the horizontal line $y = c$ goes onto the ray $\phi = c$ from the origin. As $c$ increases from $0$ to $\pi$, the lines sweep the strip upward and their image rays turn from $\phi = 0$ to $\phi = \pi$, sweeping the closed upper half plane (without $w = 0$, which is not a value of $e^z$). Since the strip has height $\pi < 2\pi$, each point is covered once. The two edges go onto the positive and the negative real axis: $y = 0$ onto $u > 0$ and $y = \pi$ onto $u < 0$.
>
> *B&C: Sec. 103, Example 3*

^ex-103-3

> [!example] Example §103.4: Slanted Lines onto Spirals
> Show that the lines $ay = x$ ($a \ne 0$) are mapped onto the spirals $\rho = \exp(a\phi)$ by $w = e^z$, where $w = \rho\exp(i\phi)$.
>
> On the line, $z = ay + iy$ with $y$ real, so by (2) the image has $\rho = e^{ay}$ and $\phi = y$ (taking for $\phi$ the value $y$, not reduced to an interval). Eliminating $y$: $\rho = \exp(a\phi)$, $-\infty < \phi < \infty$. This is a logarithmic spiral, winding outward counterclockwise when $a > 0$ and inward when $a < 0$; the map is one to one on the line, since $y$ is recovered as the accumulated angle $\phi$.
>
> *B&C: Sec. 106, Exercise 1*

^ex-103-4

> [!example] Example §103.5: A Half Strip
> Find the image of the semi-infinite strip $x \ge 0$, $0 \le y \le \pi$ under $w = e^z$.
>
> By (2), $\rho = e^x \ge 1$ and $0 \le \phi = y \le \pi$. So the image is the part of the closed upper half plane outside the open unit disk,
>
> $$
> |w| \ge 1, \qquad v \ge 0 ,
> $$
>
> covered once. On the boundary: the segment $x = 0$, $0 \le y \le \pi$ goes onto the upper half of the unit circle, from $w = 1$ to $w = -1$; the ray $y = 0$, $x \ge 0$ goes onto the ray $u \ge 1$ of the real axis; and the ray $y = \pi$, $x \ge 0$ goes onto the ray $u \le -1$.
>
> *B&C: Sec. 106, Exercise 4*

^ex-103-5
