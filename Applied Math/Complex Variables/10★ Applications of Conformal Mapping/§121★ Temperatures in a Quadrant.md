---
type: section
subject: "[[Complex Variables]]"
chapter: 10
section: "121★"
bc: "121"
aliases: ["B&C 121"]
tags: [complex-variables, math342, extension]
---
← [[§120★ A Related Problem (Steady Temperatures in a Half Plane)]] · ↑ [[· 10★ Applications of Conformal Mapping]] · [[§122★ Electrostatic Potential]] →

*Brown–Churchill, Section 121 (with Exercises 5–8).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Here the boundary conditions change type along a single edge: part of the edge is insulated ($dT/dN = 0$) and the rest is held at a fixed temperature. Separation of variables cannot handle such mixed conditions, but a conformal map can, because both types survive the map ([[§117★ Transformations of Boundary Conditions#^thm-117-2|Theorem §117.2]]). The inverse of $z = \sin w$ straightens the quadrant into a half strip in which the insulated piece becomes the base and the two fixed-temperature pieces become the sides; there the temperature is linear in $u$. In the quadrant the isotherms are confocal hyperbolas and the lines of flow confocal ellipses, with foci at the point where the condition changes type.

## The Quadrant with an Insulated Segment

> [!example] Example §121.1: A Quadrant with Mixed Conditions on One Edge
> Find the steady temperatures in a thin plate in the form of the quadrant $x > 0$, $y > 0$ (faces insulated), when a segment at the end of one edge is insulated, the rest of that edge is kept at one fixed temperature, and the second edge at another. With suitable units the problem is
>
> $$
> T_{xx}(x, y) + T_{yy}(x, y) = 0 \qquad (x > 0,\ y > 0), \qquad (1)
> $$
>
> $$
> \begin{cases} T_y(x, 0) = 0 & \text{when } 0 < x < 1, \\ T(x, 0) = 1 & \text{when } x > 1, \end{cases} \qquad (2) \qquad\qquad T(0, y) = 0 \quad (y > 0), \qquad (3)
> $$
>
> with $T$ bounded in the quadrant (B&C's Fig. 157, left). Conditions (2) prescribe the normal derivative on part of a boundary line and the values of $T$ on another part of the same line; the separation of variables method of §120 is not adapted to that.
>
> **The map.** The transformation
>
> $$
> z = \sin w \qquad (4)
> $$
>
> is a one to one mapping of the half strip $0 \le u \le \pi/2$, $v \ge 0$ onto the quadrant $x \ge 0$, $y \ge 0$ ([[§104★ Mapping Vertical Line Segments by w = sin z#^ex-104-2|Example §104.2]]): the base $0 < u < \pi/2$, $v = 0$ goes onto $0 < x < 1$ ($\sin u$); the side $u = \pi/2$ onto $x > 1$ ($\sin(\frac\pi2 + iv) = \cosh v$); the side $u = 0$ onto the positive $y$ axis ($\sin(iv) = i\sinh v$). Being one to one and onto, it has an inverse. Since (4) is conformal throughout the strip except at $w = \pi/2$ (where $\cos w = 0$), the inverse is conformal throughout the quadrant except at $z = 1$ (Theorem [[§114★ Local Inverses#^thm-114-1|§114.1]]).
>
> **The new problem.** So it suffices to find a function harmonic in the strip with: $T_v = 0$ on the base, $T = 1$ on $u = \pi/2$, $T = 0$ on $u = 0$ (B&C's Fig. 157, right). These are conditions of the types $h = h_0$ and $dh/dn = 0$ of [[§117★ Transformations of Boundary Conditions#^thm-117-2|Theorem §117.2]]. The required function is clearly
>
> $$
> T = \frac2\pi u , \qquad (5)
> $$
>
> the real part of the entire function $\frac2\pi w$; its normal derivative on the base is $T_v = 0$.
>
> **$u$ in terms of $x$ and $y$.** By (4) and [[§37 The Trigonometric Functions sin z and cos z#^prop-37-5|Proposition §37.5]],
>
> $$
> x = \sin u\cosh v, \qquad y = \cos u\sinh v . \qquad (6)
> $$
>
> When $0 < u < \pi/2$, both $\sin u$ and $\cos u$ are nonzero, and $\cosh^2v - \sinh^2v = 1$ gives
>
> $$
> \frac{x^2}{\sin^2u} - \frac{y^2}{\cos^2u} = 1 . \qquad (7)
> $$
>
> For fixed $u$ this hyperbola has foci at $z = \pm\sqrt{\sin^2u + \cos^2u} = \pm1$, and its transverse axis, the segment joining the vertices $(\pm\sin u, 0)$, has length $2\sin u$. So for a point $(x, y)$ on the branch in the first quadrant, the difference of the distances to the two foci is
>
> $$
> \sqrt{(x + 1)^2 + y^2} - \sqrt{(x - 1)^2 + y^2} = 2\sin u .
> $$
>
> By (6) this also holds when $u = 0$ ($x = 0$: the difference is $0$) and when $u = \pi/2$ ($y = 0$, $x = \cosh v \ge 1$: the difference is $(x + 1) - (x - 1) = 2$). By (5), the temperature is
>
> $$
> T = \frac2\pi\arcsin\left[\frac{\sqrt{(x + 1)^2 + y^2} - \sqrt{(x - 1)^2 + y^2}}{2}\right] , \qquad (8)
> $$
>
> where the arcsine has range $0$ to $\pi/2$, since $0 \le u \le \pi/2$.
>
> **Checking (2) and (3).** Remember that $\sqrt{(x - 1)^2}$ denotes $x - 1$ when $x > 1$ and $1 - x$ when $0 < x < 1$ (positive square roots). For $x > 1$, $y = 0$: the bracket is $\frac{(x + 1) - (x - 1)}{2} = 1$, so $T = 1$. For $x = 0$: the two distances are equal and $T = 0$. For $0 < x < 1$, $y = 0$: the bracket is $\frac{(x + 1) - (1 - x)}{2} = x$, so the temperature along the insulated part of the lower edge is
>
> $$
> T(x, 0) = \frac2\pi\arcsin x \qquad (0 < x < 1);
> $$
>
> and $T_y(x, 0) = 0$ there because (8) depends on $y$ only through $y^2$ and is differentiable at these points.
>
> **Isotherms and lines of flow.** By (5) the isotherms $T = c_1$ $(0 < c_1 < 1)$ are the parts in the first quadrant of the confocal hyperbolas (7) with $u = \pi c_1/2$. Since $\frac2\pi v$ is a harmonic conjugate of (5), the lines of flow are quarters of the confocal ellipses obtained by holding $v$ constant in (6),
>
> $$
> \frac{x^2}{\cosh^2v} + \frac{y^2}{\sinh^2v} = 1 .
> $$
>
> Heat enters through the hot part $x > 1$ of the lower edge and travels along these ellipses to the cold edge $x = 0$; the insulated segment $0 < x < 1$ is itself a line of flow (the degenerate ellipse $v = 0$), as Proposition [[§118★ Steady Temperatures#^prop-118-2|§118.2]](c) requires.
>
> *B&C: Sec. 121 (text)*

^ex-121-1

![[m342-121-1.svg]]
*Example §121.1. Isotherms $T = 0.1, \ldots, 0.9$ (blue): arcs of the confocal hyperbolas (7) with foci $\pm1$. Lines of flow (orange): quarters of the confocal ellipses $x^2/\cosh^2v + y^2/\sinh^2v = 1$. The insulated segment $0 < x < 1$ (gray) is a line of flow and the isotherms meet it at right angles; the hot edge $x > 1$ (red) and the cold edge $x = 0$ are isotherms.*

## Related Problems

> [!example] Example §121.2: A Half Plane with an Insulated Strip
> Find the bounded steady temperatures $T(x, y)$ in the semi-infinite solid $y \ge 0$ if $T = 0$ on the part $x < -1$ of the boundary $y = 0$, $T = 1$ on the part $x > 1$, and the strip $-1 < x < 1$ is insulated (B&C's Fig. 161).
>
> **Map.** $z = \sin w$ maps the half strip $-\pi/2 \le u \le \pi/2$, $v \ge 0$ one to one onto the half plane $y \ge 0$ ([[§104★ Mapping Vertical Line Segments by w = sin z#^ex-104-1|Example §104.1]]): the base onto $-1 \le x \le 1$, the side $u = \pi/2$ onto $x \ge 1$, the side $u = -\pi/2$ onto $x \le -1$. The new problem: $T = 0$ on $u = -\pi/2$, $T = 1$ on $u = \pi/2$, $T_v = 0$ on the base. Its bounded solution is $T = \frac12 + \frac u\pi$.
>
> **Back to $z$.** As in Example §121.1, $x = \sin u\cosh v$, $y = \cos u\sinh v$, and the point lies on the hyperbola with foci $\pm1$ and vertices $\pm\sin u$; now $u$ may be negative, and the signed difference of the focal distances is $\sqrt{(x + 1)^2 + y^2} - \sqrt{(x - 1)^2 + y^2} = 2\sin u$ (negative when $x < 0$). Hence
>
> $$
> T = \frac12 + \frac1\pi\arcsin\left[\frac{\sqrt{(x + 1)^2 + y^2} - \sqrt{(x - 1)^2 + y^2}}{2}\right] \qquad \Big(-\frac\pi2 \le \arcsin t \le \frac\pi2\Big).
> $$
>
> **Check.** For $x > 1$, $y = 0$: bracket $1$, $T = \frac12 + \frac12 = 1$. For $x < -1$: bracket $\frac{(-x - 1) - (1 - x)}{2} = -1$, $T = 0$. For $|x| < 1$: bracket $x$, $T = \frac12 + \frac1\pi\arcsin x$, and $T_y = 0$ by evenness in $y$. (A finite-difference check of $T_{xx} + T_{yy}$ at $(0.7, 0.4)$ and $(1.3, 2.1)$ gives $0$ to rounding.)
>
> *B&C: Sec. 121, Exercise 5*

^ex-121-2

> [!example] Example §121.3: Two Problems That Reduce to Example §121.2
> **(a) A strip with insulated half edges.** The portions $x < 0$ of both edges of the infinite plate $0 \le y \le \pi$ are insulated, as are the faces; $T(x, 0) = 1$ and $T(x, \pi) = 0$ for $x > 0$ (B&C's Fig. 162). Find $T$.
>
> The map $W = e^z$ takes the strip onto the upper half plane ([[§103★ Mappings by the Exponential Function#^ex-103-3|Example §103.3]]): the lower edge $y = 0$ onto the positive real axis, with $x > 0$ going to $U > 1$ and $x < 0$ to $0 < U < 1$; the upper edge $y = \pi$ onto the negative real axis, with $x > 0$ going to $U < -1$ and $x < 0$ to $-1 < U < 0$. So $T = 1$ on $U > 1$, $T = 0$ on $U < -1$, and $-1 < U < 1$ is insulated: the problem of Example §121.2. Since $e^z$ is conformal everywhere,
>
> $$
> T = \frac12 + \frac1\pi\arcsin\Big[\frac{|e^z + 1| - |e^z - 1|}{2}\Big], \qquad |e^z \pm 1| = \sqrt{e^{2x} \pm 2e^x\cos y + 1} .
> $$
>
> Check: for $x > 0$, $y = 0$, the bracket is $\frac{(e^x + 1) - (e^x - 1)}{2} = 1$ and $T = 1$; for $x > 0$, $y = \pi$, it is $\frac{(e^x - 1) - (e^x + 1)}{2} = -1$ and $T = 0$.
>
> **(b) A quadrant with insulated strips at the corner.** In the solid $x \ge 0$, $y \ge 0$ the face $y = 0$ is kept at $T = 1$ for $x > 1$, the face $x = 0$ at $T = 0$ for $y > 1$, and the strips $0 < x < 1$ and $0 < y < 1$ at the corner are insulated (B&C's Fig. 163). The map $W = z^2$ takes the quadrant onto the upper half plane, the positive $x$ axis onto $U > 0$ ($x > 1$ to $U > 1$) and the positive $y$ axis onto $U < 0$ ($y > 1$ to $U < -1$); it is conformal except at the corner $z = 0$. Again this is Example §121.2, and with $W = z^2 = (x^2 - y^2) + i2xy$,
>
> $$
> T = \frac12 + \frac1\pi\arcsin\left[\frac{\sqrt{(x^2 - y^2 + 1)^2 + (2xy)^2} - \sqrt{(x^2 - y^2 - 1)^2 + (2xy)^2}}{2}\right] \qquad \Big(-\frac\pi2 \le \arcsin t \le \frac\pi2\Big).
> $$
>
> *B&C: Sec. 121, Exercises 6 and 7*

^ex-121-3

> [!example] Example §121.4: Back to the Quadrant by w = i/z
> Solve the problem for the plate $x \ge 0$, $y \ge 0$ (faces insulated) with $T = 0$ on the positive $x$ axis, $T = 1$ on the segment $0 < y < 1$ of the $y$ axis, and the rest $y > 1$ of the $y$ axis insulated (B&C's Fig. 164).
>
> **Map.** $w = \dfrac iz = \dfrac{i\bar z}{|z|^2}$ sends $z = re^{i\theta}$ to $\frac1re^{i(\pi/2 - \theta)}$, so it maps the quadrant onto itself, exchanging the axes and inverting distances from $0$: the positive $x$ axis goes onto the positive $v$ axis; the segment $0 < y < 1$ onto $u > 1$; the half line $y > 1$ onto $0 < u < 1$. It is conformal for $z \ne 0$. The new problem, $T = 0$ on the $v$ axis, $T = 1$ for $u > 1$, $T_v = 0$ for $0 < u < 1$, is that of Example §121.1.
>
> **Compose.** By (8) with $|w \pm 1| = |i \pm z|/|z|$,
>
> $$
> T = \frac2\pi\arcsin\left[\frac{|z + i| - |z - i|}{2|z|}\right] = \frac2\pi\arcsin\left[\frac{\sqrt{x^2 + (y + 1)^2} - \sqrt{x^2 + (y - 1)^2}}{2\sqrt{x^2 + y^2}}\right] .
> $$
>
> **Check.** On $y = 0$ the two distances are equal: $T = 0$. On $x = 0$, $0 < y < 1$: the bracket is $\frac{(y + 1) - (1 - y)}{2y} = 1$, $T = 1$. On $x = 0$, $y > 1$: the bracket is $\frac{(y + 1) - (y - 1)}{2y} = \frac1y$, so $T = \frac2\pi\arcsin\frac1y$, and $T_x = 0$ there because $T$ depends on $x$ only through $x^2$.
>
> *B&C: Sec. 121, Exercise 8*

^ex-121-4
