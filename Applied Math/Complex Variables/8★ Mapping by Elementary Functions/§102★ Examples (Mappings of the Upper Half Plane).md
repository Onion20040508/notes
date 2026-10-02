---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: 102
bc: "102"
aliases: ["B&C 102"]
tags: [complex-variables, math342, extension]
---
← [[§101★ Mappings of the Upper Half Plane]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§103★ Mappings by the Exponential Function]] →

*Brown–Churchill, Section 102.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

The examples here put [[§101★ Mappings of the Upper Half Plane#^thm-101-1|Theorem §101.1]] to work and show the standard way of finding the image of a half plane or disk under a linear fractional transformation: the boundary goes to a circle or line, fixed by three points, and the side is decided by one formula or one test point. The last example composes a linear fractional map with the principal logarithm and turns the upper half plane into a horizontal strip; its level curves are the equipotentials and field lines of a classical electrostatics problem.

> [!remark] Remark: Method — The Image of a Half Plane or Disk under a Linear Fractional Transformation
> 1. **Boundary.** The boundary line or circle goes onto a line or circle ([[§99★ Linear Fractional Transformations#^cor-99-3|Corollary §99.3]]). Find it from the images of three boundary points; if one image is $\infty$, it is a line. If real points have real images, the real axis goes onto the real axis.
> 2. **Side.** Compute $\operatorname{Im} w$ (or $|w|$, or $\operatorname{Re} w$) in terms of $x$ and $y$, or map one interior point. Since the map is one to one on the extended plane ([[§99★ Linear Fractional Transformations#^thm-99-4|Theorem §99.4]]), the region goes onto one of the two sides of the image boundary.
> 3. **Compose.** Write a complicated map as a chain of known ones: linear maps, $1/z$, the half-plane-to-disk maps of §101, and $\operatorname{Log}$ or powers to open a half plane into a strip or a wedge.

^rem-102-1

## Examples

> [!example] Example §102.1: The Map (i − z)/(i + z)
> The transformation $w = \dfrac{i - z}{i + z}$ can be written
>
> $$
> w = e^{i\pi}\Big(\frac{z - i}{z - \bar i}\Big)
> $$
>
> (since $\bar i = -i$ and $e^{i\pi} = -1$), the case $\alpha = \pi$, $z_0 = i$ of [[§101★ Mappings of the Upper Half Plane#^thm-101-1|Theorem §101.1]]. So it maps the half plane $\operatorname{Im} z > 0$ onto the disk $|w| < 1$ and the real axis onto the circle $|w| = 1$. (It was found in [[§100★ An Implicit Form#^ex-100-3|Example §100.3]] as the map sending $-1, 0, 1$ to $-i, 1, i$.)
>
> **The boundary in detail.** For real $z = x$, multiply numerator and denominator by $\overline{i + x} = x - i$:
>
> $$
> w = \frac{(i - x)(x - i)}{x^2 + 1} = \frac{1 - x^2}{1 + x^2} + i\,\frac{2x}{1 + x^2} .
> $$
>
> Then $u^2 + v^2 = \frac{(1 - x^2)^2 + 4x^2}{(1 + x^2)^2} = 1$, $v$ has the sign of $x$, and $u > 0$ exactly when $|x| < 1$. The points $x = -1, 0, 1$ go to $-i, 1, i$, and $x \to \pm\infty$ gives $w \to -1$. So the segment $-1 \le x \le 0$ goes onto the quarter circle from $-i$ to $1$, $0 \le x \le 1$ onto the quarter circle from $1$ to $i$, $x \ge 1$ onto the arc from $i$ through the second quadrant toward $-1$, and $x \le -1$ onto the arc from $-1$ through the third quadrant to $-i$: as $x$ increases, the circle is traversed once counterclockwise, starting and ending at $-1 = T(\infty)$.
>
> *B&C: Sec. 102, Example 1 and Exercise 1*

^ex-102-1

> [!example] Example §102.2: A Half Plane onto Itself
> Show that
>
> $$
> w = \frac{z - 1}{z + 1} \qquad (2)
> $$
>
> maps the half plane $y > 0$ onto the half plane $v > 0$ and the $x$ axis onto the $u$ axis.
>
> When $z$ is real so is $w$; since the image of the real axis is a circle or a line containing these real points, it is the real axis $v = 0$. For $z \ne -1$,
>
> $$
> v = \operatorname{Im} w = \operatorname{Im}\frac{(z - 1)(\bar z + 1)}{(z + 1)(\bar z + 1)} = \frac{\operatorname{Im}\big(z\bar z + z - \bar z - 1\big)}{|z + 1|^2} = \frac{2y}{|z + 1|^2} .
> $$
>
> So $y$ and $v$ have the same sign: points above the $x$ axis go to points above the $u$ axis, and points below to points below. Since the map is one to one from the extended plane onto itself (Theorem §99.4) and the real axis (with $\infty$) goes onto the real axis (with $\infty$), the upper half plane goes **onto** the upper half plane.
>
> *B&C: Sec. 102, Example 2*

^ex-102-2

> [!example] Example §102.3: The Upper Half Plane onto a Strip
> Show that
>
> $$
> w = \operatorname{Log}\frac{z - 1}{z + 1} , \qquad (3)
> $$
>
> with the principal branch of the logarithm ([[§31 The Logarithmic Function#^def-31-2|Definition §31.2]]), maps the half plane $y > 0$ onto the strip $0 < v < \pi$.
>
> Write (3) as the composition
>
> $$
> Z = \frac{z - 1}{z + 1} \qquad\text{and}\qquad w = \operatorname{Log} Z . \qquad (4)
> $$
>
> By Example §102.2 the first map takes $y > 0$ onto $Y > 0$, where $Z = X + iY$. For the second, write $Z = R\exp(i\Theta)$ with $R > 0$, $0 < \Theta < \pi$; then
>
> $$
> \operatorname{Log} Z = \ln R + i\Theta .
> $$
>
> As $Z = R\exp(i\Theta_0)$ moves outward along the ray $\Theta = \Theta_0$ ($0 < \Theta_0 < \pi$), its image $(\ln R, \Theta_0)$ moves to the right along the entire horizontal line $v = \Theta_0$. These lines fill the strip $0 < v < \pi$ as $\Theta_0$ runs from $0$ to $\pi$, each point being hit once. So $w = \operatorname{Log} Z$ maps $Y > 0$ one to one onto the strip, and (3) maps $y > 0$ onto $0 < v < \pi$.
>
> On the boundary, $Z$ is positive for $x > 1$ and for $x < -1$, so both rays go onto the line $v = 0$ (the ray $x > 1$ onto $u < 0$, the ray $x < -1$ onto $u > 0$); and $Z$ is negative for $-1 < x < 1$, so the segment goes onto the line $v = \pi$.
>
> *B&C: Sec. 102, Example 3*

^ex-102-3

![[m342-102-1.svg]]
*The map (3) and its level curves. The horizontal lines $v = k\pi/6$ of the strip (blue) come from the arcs through $\pm1$ on which the segment $[-1, 1]$ subtends the angle $\arg(z - 1) - \arg(z + 1) = k\pi/6$ (the semicircle $|z| = 1$ for $v = \frac\pi2$); the vertical lines $u = \pm0.75, \pm1.5$ (red) come from the circles $|z - 1|/|z + 1| = e^u$ around $\pm1$. The segment $[-1, 1]$ (orange) goes onto the top edge $v = \pi$, the two rays (black) onto the bottom edge.*

> [!remark] Remark: A Potential from Example §102.3
> The function $v = \operatorname{Arg}\frac{z - 1}{z + 1}$ is the imaginary part of an analytic function, hence harmonic in $y > 0$ ([[§27★ Harmonic Functions|§27]]), and by the boundary behavior above $v/\pi$ tends to $1$ on the segment $-1 < x < 1$ and to $0$ on $|x| > 1$. So $v/\pi$ is the steady temperature in a half plane whose boundary is kept at temperature $1$ on a segment and $0$ elsewhere, or the electrostatic potential above a conducting strip at potential $1$ in a grounded plane. The blue arcs in the figure are the isotherms (equipotentials), and the red circles, on which $u$ is constant, are the heat-flow lines (lines of force). Chapter 10 develops this method ([[§116★ Transformations of Harmonic Functions|§116]]).

^rem-102-2

> [!example] Example §102.4: A Disk onto a Half Plane, and Back
> **(a)** Solving $w = (i - z)/(i + z)$ for $z$ gives $z = i(1 - w)/(1 + w)$. So the transformation
>
> $$
> w = i\,\frac{1 - z}{1 + z}
> $$
>
> is the inverse of the map of Example §102.1 (with the letters renamed), and it maps the disk $|z| \le 1$ onto the half plane $\operatorname{Im} w \ge 0$, the point $z = -1$ going to $\infty$. Directly: with $z = x + iy$,
>
> $$
> \operatorname{Im}\Big(i\,\frac{1 - z}{1 + z}\Big) = \operatorname{Re}\frac{(1 - z)(1 + \bar z)}{|1 + z|^2} = \frac{1 - x^2 - y^2}{|1 + z|^2} ,
> $$
>
> which is $\ge 0$ exactly when $|z| \le 1$.
>
> **(b)** The transformation $w = (z - 2)/z$ is the composition
>
> $$
> Z = z - 1, \qquad W = i\,\frac{1 - Z}{1 + Z}, \qquad w = iW ,
> $$
>
> since $iW = -\frac{1 - Z}{1 + Z} = \frac{Z - 1}{Z + 1} = \frac{z - 2}{z}$. The disk $|z - 1| \le 1$ is $|Z| \le 1$; part (a) takes it onto $\operatorname{Im} W \ge 0$; and the rotation through $\pi/2$ takes the upper half plane onto the left half plane. So $w = (z - 2)/z$ maps $|z - 1| \le 1$ onto $\operatorname{Re} w \le 0$, with $z = 0$ going to $\infty$. Check: $\operatorname{Re}\frac{z - 2}{z} = \frac{x^2 - 2x + y^2}{x^2 + y^2}$, which is $\le 0$ exactly when $(x - 1)^2 + y^2 \le 1$.
>
> *B&C: Sec. 102, Exercise 3*

^ex-102-4

> [!example] Example §102.5: Choosing a Branch for log(z − 1)
> Find a branch of $\log Z$ such that $w = \log(z - 1)$ maps the plane cut along the ray $x \ge 1$ onto the strip $0 < v < 2\pi$.
>
> Write $w = \log(z - 1)$ as $Z = z - 1$, $w = \log Z$. The translation takes the cut $z$ plane onto the $Z$ plane cut along the ray $X \ge 0$. Take the branch
>
> $$
> \log Z = \ln R + i\Theta \qquad (R > 0,\ 0 < \Theta < 2\pi) ,
> $$
>
> whose branch cut is exactly that ray ([[§33 Branches and Derivatives of Logarithms#^ex-33-2|Example §33.2]]). As in Example §102.3, the ray $\Theta = \Theta_0$ goes onto the full line $v = \Theta_0$, and these lines fill $0 < v < 2\pi$ once as $\Theta_0$ runs over $(0, 2\pi)$. So $w = \ln|z - 1| + i\arg(z - 1)$, $0 < \arg(z - 1) < 2\pi$, is the required branch; its inverse is $z = 1 + e^w$.
>
> *B&C: Sec. 102, Exercise 7*

^ex-102-5
