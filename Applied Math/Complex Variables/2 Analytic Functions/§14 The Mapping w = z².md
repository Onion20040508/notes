---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 14
bc: "14"
aliases: ["B&C 14"]
tags: [complex-variables, math342]
---
← [[§13 Functions and Mappings]] · ↑ [[· 2 Analytic Functions]] · [[§15 Limits]] →

*Brown–Churchill, Section 14 · MAT 342 HW 2.*

The squaring map is the first mapping studied in detail, and it shows the two ways of finding images. In Cartesian form, $u = x^2 - y^2$ and $v = 2xy$, so the two families of hyperbolas $x^2 - y^2 = c_1$ and $2xy = c_2$ are carried onto the vertical and horizontal lines of the $w$ plane; regions bounded by such hyperbolas go to rectangles and strips. In polar form, the modulus is squared and the argument doubled, so rays go to rays, circles to circles, and the first quadrant opens up onto the upper half plane. The same polar description handles $w = z^n$. Turned around, the hyperbolas $xy = c$ are the streamlines of an ideal fluid flowing around a right-angled corner ([[§126★ Flows Around a Corner and Around a Cylinder|§126★]]), and further mappings by $z^2$ come back in [[§107★ Mappings by z²|§107★]].

## Images of Hyperbolas

By [[§13 Functions and Mappings#^ex-13-2|Example §13.2]], the mapping $w = z^2$ is the transformation

$$
u = x^2 - y^2, \qquad v = 2xy \qquad (1)
$$

from the $xy$ plane into the $uv$ plane. This form is especially useful for finding the images of certain hyperbolas.

> [!theorem] Proposition §14.1: Hyperbolas x² − y² = c₁ Go to Vertical Lines
> Let $c_1 > 0$. Under $w = z^2$, each branch of the hyperbola
>
> $$
> x^2 - y^2 = c_1 \qquad (2)
> $$
>
> is mapped in a one to one manner onto the vertical line $u = c_1$. As a point moves **upward** along the entire right-hand branch, its image moves upward along the entire line; as a point moves **downward** along the entire left-hand branch, its image also moves upward along the entire line.
>
> *B&C: Sec. 14 (text)*

^prop-14-1

> [!proof]+ Proof
> By the first of equations (1), $u = c_1$ whenever $(x, y)$ lies on either branch, so both branches map into the line $u = c_1$.
>
> **The right-hand branch** is the set of points $\big(\sqrt{y^2 + c_1},\, y\big)$, $-\infty < y < \infty$. By the second of equations (1), its image has the parametric representation
>
> $$
> u = c_1, \qquad v = \varphi(y) = 2y\sqrt{y^2 + c_1} \qquad (-\infty < y < \infty) .
> $$
>
> (B&C says it is "evident" that the image moves up the entire line; here is why.) The function $\varphi$ is continuous, and
>
> $$
> \varphi'(y) = 2\sqrt{y^2 + c_1} + \frac{2y^2}{\sqrt{y^2 + c_1}} > 0 ,
> $$
>
> so $\varphi$ is strictly increasing, hence one to one. Also $\varphi(y) \to \pm\infty$ as $y \to \pm\infty$, so by the intermediate value theorem every real $v$ is a value of $\varphi$. Thus the right-hand branch is mapped one to one onto the whole line $u = c_1$, and the image moves upward as $y$ increases.
>
> **The left-hand branch** is the set of points $\big(-\sqrt{y^2 + c_1},\, y\big)$, and its image is
>
> $$
> u = c_1, \qquad v = -2y\sqrt{y^2 + c_1} = -\varphi(y) \qquad (-\infty < y < \infty) .
> $$
>
> Since $-\varphi$ is strictly decreasing with limits $\mp\infty$ as $y \to \pm\infty$, the same argument shows that this branch is also mapped one to one onto the line $u = c_1$, and that the image moves upward as $y$ decreases, that is, as the point moves downward along the branch.

^pf-14-1

*Uses:* [[§13 Functions and Mappings#^ex-13-2|Ex. §13.2]], [[§29 The Mean Value Theorem#^cor-29-7|451 Cor. §29.7]] (positive derivative gives strictly increasing), [[§18 Properties of Continuous Functions#^thm-18-3|451 Thm. §18.3]] (intermediate value theorem)

> [!theorem] Proposition §14.2: Hyperbolas 2xy = c₂ Go to Horizontal Lines
> Let $c_2 > 0$. Under $w = z^2$, each branch of the hyperbola
>
> $$
> 2xy = c_2 \qquad (3)
> $$
>
> is mapped in a one to one manner onto the horizontal line $v = c_2$. As a point travels **down** the entire upper branch (in the first quadrant), its image moves to the right along the entire line; as a point moves **upward** along the entire lower branch (in the third quadrant), its image also moves to the right along the entire line.
>
> *B&C: Sec. 14 (text)*

^prop-14-2

> [!proof]+ Proof
> By the second of equations (1), $v = c_2$ whenever $(x, y)$ is on either branch.
>
> **The upper branch.** On it $y = c_2/(2x)$, $0 < x < \infty$, and the first of equations (1) gives the parametric representation of its image
>
> $$
> u = \psi(x) = x^2 - \frac{c_2^2}{4x^2}, \qquad v = c_2 \qquad (0 < x < \infty) .
> $$
>
> Here
>
> $$
> \lim_{\substack{x\to0 \\ x>0}} u = -\infty \qquad\text{and}\qquad \lim_{x\to\infty} u = \infty ,
> $$
>
> and $\psi'(x) = 2x + c_2^2/(2x^3) > 0$, so $\psi$ is continuous and strictly increasing. As in Proposition §14.1, $\psi$ is a one to one map of $(0, \infty)$ onto $(-\infty, \infty)$. As $(x, y)$ travels down the branch, $x$ increases, and the image moves to the right along the entire line $v = c_2$.
>
> **The lower branch.** On it $x = c_2/(2y)$, $-\infty < y < 0$, and its image is
>
> $$
> u = \frac{c_2^2}{4y^2} - y^2, \qquad v = c_2 \qquad (-\infty < y < 0) ,
> $$
>
> with
>
> $$
> \lim_{y\to-\infty} u = -\infty \qquad\text{and}\qquad \lim_{\substack{y\to0 \\ y<0}} u = \infty .
> $$
>
> The derivative $du/dy = -c_2^2/(2y^3) - 2y$ is positive for $y < 0$ (both terms are), so again $u$ is a continuous, strictly increasing map of $(-\infty, 0)$ onto $(-\infty, \infty)$: as the point moves upward along the lower branch, its image travels to the right along the entire line.

^pf-14-2

*Uses:* [[§13 Functions and Mappings#^ex-13-2|Ex. §13.2]], [[§29 The Mean Value Theorem#^cor-29-7|451 Cor. §29.7]], [[§18 Properties of Continuous Functions#^thm-18-3|451 Thm. §18.3]]

![[m342-14-1.svg]]
*The hyperbolas $x^2 - y^2 = 1, 2$ (blue) and $2xy = 1, 2$ (red) in the $z$ plane, and their images under $w = z^2$: the vertical lines $u = 1, 2$ and the horizontal lines $v = 1, 2$. Each branch covers its line exactly once, in the direction of the arrows (Propositions §14.1 and §14.2). The shaded domain $x > 0$, $y > 0$, $xy < 1$, filled by the upper branches of $2xy = c$ with $0 < c < 2$, goes onto the shaded strip $0 < v < 2$ (Example §14.1).*

## Images of Regions

> [!example] Example §14.1: A Domain Bounded by a Hyperbola Goes onto a Strip
> Find the image under $w = z^2$ of the domain $x > 0$, $y > 0$, $xy < 1$, and of the closed region $x \ge 0$, $y \ge 0$, $xy \le 1$.
>
> **The domain.** A point $(x, y)$ with $x > 0$, $y > 0$ lies on exactly one hyperbola of the family $2xy = c$, namely $c = 2xy$, and on its upper branch; the condition $xy < 1$ says $0 < c < 2$. So the domain consists of all points lying on the upper branches of the hyperbolas $2xy = c$, $0 < c < 2$. By Proposition §14.2, as a point travels downward along the entirety of such a branch, its image moves to the right along the entire line $v = c$. Since, for all values of $c$ between $0$ and $2$, these upper branches fill out the domain, the domain is mapped onto the union of the lines $v = c$, $0 < c < 2$: the horizontal strip $0 < v < 2$.
>
> **The boundary.** By (1), the image of a point $(0, y)$ is $(-y^2, 0)$. So as $(0, y)$ travels downward to the origin along the $y$ axis, its image moves to the right along the negative $u$ axis and reaches the origin of the $w$ plane. The image of a point $(x, 0)$ is $(x^2, 0)$, which moves to the right from the origin along the $u$ axis as $(x, 0)$ moves to the right from the origin along the $x$ axis. The image of the upper branch of $xy = 1$ (that is, $2xy = 2$) is the horizontal line $v = 2$.
>
> Hence the closed region $x \ge 0$, $y \ge 0$, $xy \le 1$ is mapped onto the closed strip $0 \le v \le 2$. In the labels of B&C's Figure 20: the boundary path $A$ (far up the $y$ axis) $\to B$ (origin) $\to C$ (far along the $x$ axis) goes to the $u$ axis traversed from left to right, $A' \to B' \to C'$, and the branch $D \to E$ of $xy = 1$ goes to the line $v = 2$, $D' \to E'$. The mapping is one to one on this region, since it lies in the closed first quadrant, on which $z^2$ is one to one (Example §14.2).
>
> *B&C: Sec. 14, Example 1*

^ex-14-1

Polar coordinates are the other tool.

> [!example] Example §14.2: The First Quadrant Goes onto the Upper Half Plane
> When $z = re^{i\theta}$, the mapping $w = z^2$ becomes
>
> $$
> w = r^2e^{i2\theta} . \qquad (4)
> $$
>
> So the image $w = \rho e^{i\phi}$ of any nonzero point $z$ is found by squaring the modulus $r = |z|$ and doubling the value $\theta$ of $\arg z$ that is used:
>
> $$
> \rho = r^2 \qquad\text{and}\qquad \phi = 2\theta . \qquad (5)
> $$
>
> **Circles.** Points $z = r_0e^{i\theta}$ on a circle $r = r_0$ go to points $w = r_0^2e^{i2\theta}$ on the circle $\rho = r_0^2$. As a point of the first circle moves counterclockwise from the positive real axis to the positive imaginary axis ($0 \le \theta \le \pi/2$), its image moves counterclockwise from the positive real axis to the negative real axis ($0 \le \phi \le \pi$). As $r_0$ runs over all positive values, these quarter-circles fill out the first quadrant and their images fill out the upper half plane. So $w = z^2$ is a one to one mapping of the first quadrant $r \ge 0$, $0 \le \theta \le \pi/2$ onto the upper half plane $\rho \ge 0$, $0 \le \phi \le \pi$, with $z = 0$ going to $w = 0$.
>
> (B&C reads one to one and onto off the picture; here is the check.) *Onto:* a point $w = \rho e^{i\phi}$ with $\rho \ge 0$, $0 \le \phi \le \pi$ is the image of $z = \sqrt\rho\,e^{i\phi/2}$, whose argument $\phi/2$ lies in $[0, \pi/2]$. *One to one:* if $z_1^2 = z_2^2$, then $(z_1 - z_2)(z_1 + z_2) = 0$, so $z_1 = z_2$ or $z_1 = -z_2$; but if $z_2 \ne 0$ is in the closed first quadrant, $-z_2$ has an argument in $[\pi, 3\pi/2]$ and is not.
>
> **Rays** (B&C's Exercise 7). The ray $\theta = \alpha$ ($0 \le \alpha \le \pi/2$) goes to the ray $\phi = 2\alpha$, and since $r \mapsto r^2$ maps $[0, \infty)$ one to one onto itself, each ray is mapped one to one onto its image ray. The rays with $0 \le \alpha \le \pi/2$ fill the first quadrant, and their images, the rays with $0 \le \phi \le \pi$, fill the upper half plane: the same conclusion again.
>
> **The upper half plane.** The transformation also maps the upper half plane $r \ge 0$, $0 \le \theta \le \pi$ onto the entire $w$ plane, since $\phi = 2\theta$ then covers $[0, 2\pi]$. In this case the mapping is not one to one: both the positive and the negative real axes of the $z$ plane are mapped onto the positive real axis of the $w$ plane.
>
> *B&C: Sec. 14, Example 2 and Exercise 7*

^ex-14-2

When $n$ is a positive integer greater than $2$, the transformation $w = z^n$, or $w = r^ne^{in\theta}$, has mapping properties similar to those of $w = z^2$.

> [!theorem] Proposition §14.3: The Mapping w = zⁿ
> Let $n \ge 2$ be an integer. The transformation $w = z^n$
> 1. maps the entire $z$ plane onto the entire $w$ plane, and each nonzero point of the $w$ plane is the image of exactly $n$ distinct points of the $z$ plane;
> 2. maps the circle $r = r_0$ onto the circle $\rho = r_0^n$;
> 3. maps the sector $r \le r_0$, $0 \le \theta \le 2\pi/n$ onto the disk $\rho \le r_0^n$, but not in a one to one manner.
>
> *B&C: Sec. 14 (text)*

^prop-14-3

> [!proof]+ Proof
> Write $z = re^{i\theta}$, so that $w = z^n = r^ne^{in\theta}$ ([[§8 Products and Powers in Exponential Form|§8]]).
>
> 1. $w = 0$ has the single preimage $z = 0$. A nonzero $w$ is the image of exactly the $n$th roots of $w$, and by [[§10 Roots of Complex Numbers|§10]] a nonzero complex number has exactly $n$ distinct $n$th roots. In particular every $w$ is an image.
> 2. If $|z| = r_0$ then $|z^n| = r_0^n$, so the circle maps into the circle $\rho = r_0^n$. Conversely, a point $r_0^ne^{i\phi}$ of that circle is the image of $r_0e^{i\phi/n}$, which lies on the circle $r = r_0$. (As $\theta$ runs once around, $n\theta$ runs $n$ times around: the image circle is traced $n$ times.)
> 3. For $0 \le r \le r_0$ and $0 \le \theta \le 2\pi/n$, the image $w = r^ne^{in\theta}$ has modulus $r^n \le r_0^n$, so the sector maps into the disk. Conversely, every point $\rho e^{i\phi}$ of the disk with $0 \le \rho \le r_0^n$ and $0 \le \phi < 2\pi$ is the image of $\rho^{1/n}e^{i\phi/n}$, which lies in the sector since $0 \le \phi/n < 2\pi/n$. The mapping is not one to one on the sector, because the two bounding rays $\theta = 0$ and $\theta = 2\pi/n$ both go onto the positive real axis: $r$ and $re^{i2\pi/n}$ have the same image $r^n$.

^pf-14-3

*Uses:* [[§8 Products and Powers in Exponential Form|§8]], [[§10 Roots of Complex Numbers|§10]] (Theorem on $n$th roots)

> [!remark] Remark: Method — Images Under w = z² and w = zⁿ
> 1. **Choose the coordinates in which the given curves are level sets.** In Cartesian form ($u = x^2 - y^2$, $v = 2xy$), the hyperbolas $x^2 - y^2 = c$ and $xy = c$ go to the lines $u = c$ and $v = 2c$. In polar form ($\rho = r^n$, $\phi = n\theta$), circles $|z| = r_0$ go to circles $|w| = r_0^n$ and rays $\arg z = \alpha$ go to rays $\arg w = n\alpha$.
> 2. **Parametrize** the curve by the remaining variable and substitute into the other component, as in the proofs of Propositions §14.1 and §14.2.
> 3. **Track direction and extent:** check monotonicity and the limits at the ends of the parameter interval, to see whether the image is the whole line or ray and in which direction it is traced, and whether a closed curve is traced more than once.
> 4. **For a region,** write it as a union of such curves (Example §14.1), then map its boundary piece by piece to see which boundary points are included.

^rem-14-1

> [!example] Example §14.3: Rays, Circles and Points Under w = z³
> Find and plot the images under $f(z) = z^3$ of the rays $\ell_1 = \{\operatorname{Arg} z = \pi/4\}$ and $\ell_2 = \{\operatorname{Arg} z = \pi/3\}$, the circles $c_1$ of radius $1$ and $c_2$ of radius $\frac12$ centered at $0$, and the points $z_1 = i$ and $z_2 = -1 + i$.
>
> Work in exponential form: for $z = re^{i\theta}$, $f(z) = r^3e^{i3\theta}$, so moduli are cubed and arguments tripled.
>
> **The rays.** $\ell_1$ consists of the points $z = re^{i\pi/4}$, $r > 0$ (the origin has no argument and is not on the ray). Their images are $w = r^3e^{i3\pi/4}$, and as $r$ runs over $(0, \infty)$ so does $r^3$. So
>
> $$
> f(\ell_1) = \{\operatorname{Arg} w = 3\pi/4\} ,
> $$
>
> the open ray in the second quadrant on the line $v = -u$. Likewise $\ell_2 = \{re^{i\pi/3} : r > 0\}$ goes to $\{r^3e^{i\pi} : r > 0\}$:
>
> $$
> f(\ell_2) = \{\operatorname{Arg} w = \pi\} ,
> $$
>
> the negative real axis.
>
> **The circles.** $c_1 = \{e^{i\theta} : 0 \le \theta < 2\pi\}$ goes to $\{e^{i3\theta}\}$: the unit circle, traced counterclockwise three times as $z$ goes once around $c_1$. Similarly $c_2 = \{\frac12e^{i\theta}\}$ goes to $\{\frac18e^{i3\theta}\}$, the circle of radius $\frac18$, traced three times (Proposition §14.3(2) with $n = 3$).
>
> **The points.** $f(i) = i^3 = -i$. For $z_2$: $|{-1} + i| = \sqrt2$ and $\operatorname{Arg}(-1 + i) = 3\pi/4$, so $z_2 = \sqrt2\,e^{i3\pi/4}$ and
>
> $$
> f(z_2) = 2\sqrt2\,e^{i9\pi/4} = 2\sqrt2\,e^{i\pi/4} = 2\sqrt2\Big(\frac{\sqrt2}{2} + i\frac{\sqrt2}{2}\Big) = 2 + 2i .
> $$
>
> Check: $(-1 + i)^2 = -2i$ and $(-2i)(-1 + i) = 2 + 2i$.
>
> *Source: 342 HW 2, Problem 2*

^ex-14-3

![[m342-14-2.svg]]
*Example §14.3. Left: the rays $\operatorname{Arg} z = \pi/4$ (blue) and $\pi/3$ (green), the circles of radius $1$ (red) and $\frac12$ (orange), and the points $i$, $-1 + i$. Right: their images under $w = z^3$. The angles $\pi/4$ and $\pi/3$ triple to $3\pi/4$ and $\pi$; the radii cube to $1$ and $\frac18$; $i$ goes to $-i$ on the unit circle and $-1 + i$ to $2 + 2i$.*
