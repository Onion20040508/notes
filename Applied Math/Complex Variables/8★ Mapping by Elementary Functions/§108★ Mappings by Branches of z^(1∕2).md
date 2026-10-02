---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: 108
bc: "108"
aliases: ["B&C 108"]
tags: [complex-variables, math342, extension]
---
← [[§107★ Mappings by z²]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§109★ Square Roots of Polynomials]] →

*Brown–Churchill, Section 108.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

The square root is the inverse of $z^2$, but it is double-valued, so a mapping needs a branch. Every branch halves arguments and takes square roots of moduli: the principal branch $F_0$ maps the plane cut along the negative real axis onto the right half plane, and the other values are $-F_0$. A branch can be cut along any ray from the origin, but no choice of values makes it continuous on the whole plane. The same description works for the $n$ branches of $z^{1/n}$, which map the cut plane onto $n$ sectors of angle $2\pi/n$. Square roots of polynomials ([[§109★ Square Roots of Polynomials|§109]]) and Riemann surfaces ([[§110★ Riemann Surfaces|§110]]) build on this.

## Branches of the Square Root

Recall ([[§10 Roots of Complex Numbers|§10]]) that for $z = r\exp(i\Theta)$, $r > 0$, $-\pi < \Theta \le \pi$, the two square roots of $z$ are

$$
z^{1/2} = \sqrt r\exp\frac{i(\Theta + 2k\pi)}{2} \qquad (k = 0, 1) , \qquad (1)
$$

the principal root occurring when $k = 0$; and ([[§35 The Power Function|§35]]) that $z^{1/2} = \exp\big(\tfrac12\log z\big)$ for $z \ne 0$. (2)

> [!definition] Definition §108.1: The Principal Branch F₀ of z^(1/2)
> The **principal branch** of the double-valued function $z^{1/2}$ is obtained by taking the principal branch of $\log z$ in (2):
>
> $$
> F_0(z) = \exp\Big(\frac12\operatorname{Log} z\Big) = \sqrt r\exp\frac{i\Theta}{2} \qquad (r > 0,\ -\pi < \Theta < \pi) , \qquad (3)
> $$
>
> since $\frac12\operatorname{Log} z = \frac12(\ln r + i\Theta) = \ln\sqrt r + \frac{i\Theta}{2}$. The origin and the ray $\Theta = \pi$ form its branch cut, and the origin is the branch point. For images under $w = F_0(z)$ one writes $w = \rho\exp(i\phi)$ with $\rho = \sqrt r$ and $\phi = \Theta/2$: arguments are halved. It is understood that $w = 0$ when $z = 0$.
>
> *B&C: Sec. 108, Equation (3)*

^def-108-1

This is the case $c = 1/2$ of the principal branch of $z^c$, [[§35 The Power Function#^def-35-2|Definition §35.2]]; it is analytic in its domain ([[§35 The Power Function#^thm-35-2|Theorem §35.2]]).

> [!theorem] Proposition §108.1: The Two Branches ±F₀
> When $-\pi < \Theta < \pi$ and the branch $\log z = \ln r + i(\Theta + 2\pi)$ is used, (2) gives the branch
>
> $$
> F_1(z) = \sqrt r\exp\frac{i(\Theta + 2\pi)}{2} \qquad (r > 0,\ -\pi < \Theta < \pi) \qquad (4)
> $$
>
> of $z^{1/2}$, corresponding to $k = 1$ in (1), and $F_1(z) = -F_0(z)$. The values $\pm F_0(z)$ are all the values of $z^{1/2}$ in the domain $r > 0$, $-\pi < \Theta < \pi$. If $F_0$ is extended by (3) to the ray $\Theta = \pi$ and by $F_0(0) = 0$, the values $\pm F_0(z)$ are all the values of $z^{1/2}$ in the entire plane.
>
> *B&C: Sec. 108 (text)*

^prop-108-1

> [!proof]+ Proof
> Since $\exp(i\pi) = -1$, $F_1(z) = \sqrt r\exp\frac{i\Theta}{2}\exp(i\pi) = -F_0(z)$. By (1), for $z \ne 0$ the square roots of $z$ are the $k = 0$ and $k = 1$ values, which are $F_0(z)$ and $-F_0(z)$ when $-\pi < \Theta < \pi$, and also when $\Theta = \pi$ with $F_0$ extended by (3). At $z = 0$ the only square root is $0 = \pm F_0(0)$.

^pf-108-1

*Uses:* [[§108★ Mappings by Branches of z^(1∕2)#^def-108-1|Def. §108.1]], [[§10 Roots of Complex Numbers|§10]]

> [!definition] Definition §108.2: The Branch f_α Cut Along θ = α
> Other branches of $z^{1/2}$ come from other branches of $\log z$ in (2). The branch whose branch cut is the ray $\theta = \alpha$ is
>
> $$
> f_\alpha(z) = \sqrt r\exp\frac{i\theta}{2} \qquad (r > 0,\ \alpha < \theta < \alpha + 2\pi) . \qquad (5)
> $$
>
> When $\alpha = -\pi$ this is $F_0$, and when $\alpha = \pi$ it is $F_1$.
>
> *B&C: Sec. 108, Equation (5)*

^def-108-2

> [!theorem] Proposition §108.2: No Branch Is Continuous on the Whole Plane
> Extend $f_\alpha$ to the whole plane by using (5) at the nonzero points of the branch cut (with $\theta = \alpha$) and setting $f_\alpha(0) = 0$. The extension is not continuous at any nonzero point of the cut.
>
> *B&C: Sec. 108 (text)*

^prop-108-2

> [!proof]+ Proof
> B&C asserts this; here is why. Let $z_0 = r_0e^{i\alpha}$, $r_0 > 0$, be on the cut. Approaching $z_0$ through points $re^{i\theta}$ with $\theta \to \alpha^+$, the values $\sqrt r\,e^{i\theta/2}$ tend to $\sqrt{r_0}\,e^{i\alpha/2}$. Approaching through points with $\theta \to (\alpha + 2\pi)^-$ (the other side of the cut), they tend to
>
> $$
> \sqrt{r_0}\,e^{i(\alpha + 2\pi)/2} = -\sqrt{r_0}\,e^{i\alpha/2} .
> $$
>
> The two limits differ (their difference has modulus $2\sqrt{r_0} > 0$), so $f_\alpha$ has no limit at $z_0$, whatever value it is given there.

^pf-108-2

*Uses:* [[§108★ Mappings by Branches of z^(1∕2)#^def-108-2|Def. §108.2]]

> [!remark] Remark: Method — Choosing a Branch of z^(1/n) for a Region
> 1. Choose a ray $\theta = \alpha$ from the branch point that avoids the region (and its boundary, if the boundary is to be mapped continuously).
> 2. Take the branch with $\alpha < \theta < \alpha + 2\pi$, and fix the sheet by one prescribed value (for example, a positive value on the positive real axis).
> 3. Read off images in polar coordinates: $\rho = r^{1/n}$, $\phi = \theta/n$. Rays go onto rays and circles $|z| = r$ onto circles $|w| = r^{1/n}$.

^rem-108-1

## nth Roots

> [!theorem] Proposition §108.3: Branches of z^(1/n)
> Let $n \ge 2$. For $z \ne 0$ the values of $z^{1/n}$ are
>
> $$
> z^{1/n} = \exp\Big(\frac1n\log z\Big) = \sqrt[n]{r}\exp\frac{i(\Theta + 2k\pi)}{n} \qquad (k = 0, 1, 2, \ldots, n - 1) , \qquad (6)
> $$
>
> where $r = |z|$ and $\Theta = \operatorname{Arg} z$. Each of the $n$ functions
>
> $$
> F_k(z) = \sqrt[n]{r}\exp\frac{i(\Theta + 2k\pi)}{n} \qquad (k = 0, 1, 2, \ldots, n - 1) \qquad (7)
> $$
>
> is a branch of $z^{1/n}$ on the domain $r > 0$, $-\pi < \Theta < \pi$, and, with $w = \rho e^{i\phi}$, the transformation $w = F_k(z)$ maps that domain one to one onto the sector
>
> $$
> \rho > 0, \qquad \frac{(2k - 1)\pi}{n} < \phi < \frac{(2k + 1)\pi}{n} .
> $$
>
> These $n$ branches give the $n$ distinct $n$th roots of $z$ at each point of the domain; the principal branch is $k = 0$.
>
> *B&C: Sec. 108, Equations (6) and (7)*

^prop-108-3

> [!proof]+ Proof
> Using the branch $\log z = \ln r + i(\Theta + 2k\pi)$, $-\pi < \Theta < \pi$, which is analytic there ([[§33 Branches and Derivatives of Logarithms|§33]]), $\exp\big(\frac1n\log z\big) = \exp\big(\frac1n\ln r\big)\exp\frac{i(\Theta + 2k\pi)}{n} = F_k(z)$, an analytic function whose $n$th power is $z$: a branch. In polar coordinates $F_k$ is $(r, \Theta) \mapsto (\rho, \phi) = \big(r^{1/n}, (\Theta + 2k\pi)/n\big)$, a bijection of $(0, \infty) \times (-\pi, \pi)$ onto $(0, \infty) \times \big((2k - 1)\pi/n, (2k + 1)\pi/n\big)$. Since the angular interval has length $2\pi/n < 2\pi$, distinct pairs $(\rho, \phi)$ in it are distinct points: the map is one to one onto the sector. For fixed $z$ the arguments $(\Theta + 2k\pi)/n$, $k = 0, \ldots, n - 1$, differ by multiples of $2\pi/n$ less than $2\pi$, so the $n$ values are distinct, and they are all the $n$th roots of $z$ ([[§10 Roots of Complex Numbers|§10]]).

^pf-108-3

*Uses:* [[§10 Roots of Complex Numbers|§10]], [[§33 Branches and Derivatives of Logarithms#^thm-33-1|§33.1]], [[§34 Some Identities Involving Logarithms#^prop-34-4|§34.4]]

## Examples

> [!example] Example §108.1: A Quarter Disk onto a Sector
> Show that $w = F_0(z)$ maps the quarter disk $0 \le r \le 2$, $0 \le \theta \le \pi/2$ one to one onto the sector $0 \le \rho \le \sqrt2$, $0 \le \phi \le \pi/4$.
>
> As a point $z = r\exp(i\theta_1)$ moves outward from the origin along a radius $R_1$ of length $2$ with angle of inclination $\theta_1$ ($0 \le \theta_1 \le \pi/2$), its image $w = \sqrt r\exp(i\theta_1/2)$ moves outward from the origin along a radius $R_1'$ of length $\sqrt2$ and inclination $\theta_1/2$. If the quarter disk is swept out by a radius turning from $DA$ (on the positive $x$ axis) to $DC$ (on the positive $y$ axis), the sector is swept out by the image radius turning from $D'A'$ to $D'C'$, and distinct radii go to distinct radii. This gives a one to one correspondence between the two regions.
>
> *B&C: Sec. 108, Example*

^ex-108-1

![[m342-108-1.svg]]
*The principal square root $F_0$ on the quarter disk $|z| \le 2$, $0 \le \theta \le \frac\pi2$: radii (red, every $\frac\pi8$) go onto radii at half the angle, and quarter circles $r = 0.5, 1, 1.5, 2$ (blue) onto arcs of radius $\sqrt r$. The right angle at $D$ is halved, the one place where the map is not conformal.*

> [!example] Example §108.2: The Four Branches of z^(1/4) and the Fourth Roots of i
> By Proposition §108.3 with $n = 4$, the branches $F_k(z) = \sqrt[4]{r}\exp\frac{i(\Theta + 2k\pi)}{4}$ map the domain $r > 0$, $-\pi < \Theta < \pi$ onto the quadrant-shaped sectors
>
> $$
> F_0: -\tfrac\pi4 < \phi < \tfrac\pi4, \qquad F_1: \tfrac\pi4 < \phi < \tfrac{3\pi}4, \qquad F_2: \tfrac{3\pi}4 < \phi < \tfrac{5\pi}4, \qquad F_3: \tfrac{5\pi}4 < \phi < \tfrac{7\pi}4 .
> $$
>
> For $z = i$: $r = 1$, $\Theta = \pi/2$, so
>
> $$
> F_k(i) = \exp\frac{i(\pi/2 + 2k\pi)}{4} = e^{i\pi/8},\ e^{5i\pi/8},\ e^{9i\pi/8},\ e^{13i\pi/8} \qquad (k = 0, 1, 2, 3) ,
> $$
>
> that is, $\pm(\cos\frac\pi8 + i\sin\frac\pi8) \approx \pm(0.9239 + 0.3827i)$ and $\pm(-\sin\frac\pi8 + i\cos\frac\pi8) \approx \pm(-0.3827 + 0.9239i)$. Each lies in the sector of its branch, and each has fourth power $e^{i\pi/2 + 2k\pi i} = i$.
>
> *B&C: Sec. 108, Exercise 8*

^ex-108-2

> [!example] Example §108.3: The Square Root of (z − 1)/(z + 1)
> By [[§102★ Examples (Mappings of the Upper Half Plane)#^ex-102-2|Example §102.2]], $Z = \dfrac{z - 1}{z + 1}$ maps the $x$ axis onto the $X$ axis and the half planes $y > 0$, $y < 0$ onto $Y > 0$, $Y < 0$. On the segment $-1 \le x \le 1$, $Z = (x - 1)/(x + 1)$ runs from $\infty$ (at $x = -1$) down to $0$ (at $x = 1$) through negative values: the segment goes onto $X \le 0$ (with $\infty$). So the $z$ plane minus that segment goes one to one onto the $Z$ plane minus the ray $X \le 0$, except that $Z = 1$ is the image of $z = \infty$ only.
>
> The principal branch $F_0$ maps the $Z$ plane cut along $X \le 0$ one to one onto the right half plane $u > 0$ (arguments in $(-\pi, \pi)$ are halved into $(-\pi/2, \pi/2)$). Hence the composite function
>
> $$
> w = Z^{1/2} = \Big(\frac{z - 1}{z + 1}\Big)^{1/2}
> $$
>
> maps the $z$ plane, except for the segment $-1 \le x \le 1$, onto the right half plane $u > 0$, with $w = 1$ corresponding to $z = \infty$. This branch reappears in [[§109★ Square Roots of Polynomials#^ex-109-3|Example §109.3]].
>
> *B&C: Sec. 108, Exercise 7*

^ex-108-3

> [!example] Example §108.4: The Square Root of sin z
> Show that $w = F_0(\sin z)$, with $F_0(0) = 0$, maps the vertical semi-infinite strip $0 \le x \le \pi/2$, $y \ge 0$ onto the octant $0 \le \phi \le \pi/4$ of the $w$ plane.
>
> Write $Z = \sin z$, $w = F_0(Z)$. By [[§104★ Mapping Vertical Line Segments by w = sin z#^ex-104-2|Example §104.2]], the first map takes the strip one to one onto the closed first quadrant $0 \le \operatorname{Arg} Z \le \pi/2$. On that quadrant $F_0$ is defined (the cut $\Theta = \pi$ is avoided) and halves arguments, so it maps the quadrant one to one onto $0 \le \phi \le \pi/4$. Boundary: the base goes through $Z \in [0, 1]$ onto $0 \le w \le 1$; the wall $x = \pi/2$ through $Z = \cosh y$ onto $w = \sqrt{\cosh y} \ge 1$; and the $y$ axis through $Z = i\sinh y$ onto the ray $w = \sqrt{\sinh y}\,e^{i\pi/4}$. Compare [[§107★ Mappings by z²#^ex-107-2|Example §107.2]], where squaring instead of taking roots gives a half plane.
>
> *B&C: Sec. 108, Exercise 5*

^ex-108-4
