---
type: section
subject: "[[Complex Variables]]"
chapter: 10
section: 123
bc: "123"
aliases: ["B&C 123"]
tags: [complex-variables, math342, extension]
---
← [[§122★ Electrostatic Potential]] · ↑ [[· 10★ Applications of Conformal Mapping]] · [[§124★ Two-Dimensional Fluid Flow]] →

*Brown–Churchill, Section 123 (with Exercises 1, 2, 3 and 8).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Two potential problems solved by mapping. In the first, a cylinder split lengthwise into two electrodes is mapped by a linear fractional transformation onto a half plane, where the potential is a multiple of $\operatorname{Arg} w$; the equipotentials are circular arcs through the two gaps. In the second, a logarithm maps a half annulus onto a rectangle, where separation of variables gives a series, and composing with the logarithm turns that series into the solution in the original region. Mapping and series methods thus combine: the map supplies a region where the series method works.

## A Split Cylinder

> [!example] Example §123.1: Two Halves of a Cylinder at Potentials 0 and 1
> A long hollow circular cylinder made of a thin conducting sheet is split lengthwise into two equal parts, separated by slender insulating strips and used as electrodes: one is grounded at potential $0$, the other kept at potential $1$. Over any cross section far from the ends, the potential $V(x, y)$ is harmonic inside the circle $x^2 + y^2 = 1$, with $V = 0$ on the upper half of the circle and $V = 1$ on the lower half (B&C's Fig. 165). Find $V$, its equipotentials and its flux lines.
>
> **The map.** The linear fractional transformation $z = \dfrac{i - w}{i + w}$ (1) maps the upper half plane onto the disk, the positive real axis onto the upper semicircle and the negative real axis onto the lower semicircle ([[§102★ Examples (Mappings of the Upper Half Plane)#^ex-102-1|Example §102.1]]). Its inverse is
>
> $$
> w = i\,\frac{1 - z}{1 + z} . \qquad (4)
> $$
>
> Check on the circle: for $z = e^{i\theta}$, $\frac{1 - e^{i\theta}}{1 + e^{i\theta}} = -i\tan\frac\theta2$, so $w = \tan\frac\theta2$, which is positive for $0 < \theta < \pi$ and negative for $-\pi < \theta < 0$. So the new problem is: $V$ harmonic and bounded in $v > 0$, $V = 0$ on the positive $u$ axis, $V = 1$ on the negative $u$ axis.
>
> **Solution in the half plane.** The imaginary part of
>
> $$
> \frac1\pi\operatorname{Log} w = \frac1\pi\ln\rho + i\frac1\pi\phi \qquad (\rho > 0,\ 0 \le \phi \le \pi) \qquad (2)
> $$
>
> is bounded and takes the required values on $\phi = 0$ and $\phi = \pi$. Hence
>
> $$
> V = \frac1\pi\arctan\Big(\frac vu\Big) , \qquad (3)
> $$
>
> with the arctangent taking values from $0$ to $\pi$.
>
> **Back to the disk.** From (4), $w = \dfrac{i(1 - z)(1 + \bar z)}{|1 + z|^2} = \dfrac{2y + i(1 - x^2 - y^2)}{|1 + z|^2}$, so $\dfrac vu = \dfrac{1 - x^2 - y^2}{2y}$ and
>
> $$
> V = \frac1\pi\arctan\Big(\frac{1 - x^2 - y^2}{2y}\Big) \qquad (0 \le \arctan t \le \pi). \qquad (5)
> $$
>
> It is harmonic inside the circle (Theorem [[§116★ Transformations of Harmonic Functions#^thm-116-1|§116.1]]) and takes the required values: as $z$ approaches a point of the upper semicircle from inside, $1 - x^2 - y^2 \to 0^+$ with $y > 0$, and $\lim_{t\to0^+}\arctan t = 0$; on the lower semicircle $y < 0$ and $\lim_{t\to0^-}\arctan t = \pi$, so $V \to 1$.
>
> **Equipotentials and flux lines.** $V = c_1$ $(0 < c_1 < 1)$ means $1 - x^2 - y^2 = 2y\tan\pi c_1$, that is,
>
> $$
> x^2 + (y + \tan\pi c_1)^2 = \sec^2\pi c_1 ,
> $$
>
> arcs of circles through the gaps $(\pm1, 0)$. The segment of the $x$ axis between them is the equipotential $V = \frac12$ (there $t = \pm\infty$). A harmonic conjugate of $V$ is $U = -\frac1\pi\ln\rho$, the imaginary part of $-\frac i\pi\operatorname{Log} w = \frac\phi\pi - \frac i\pi\ln\rho$; by (4),
>
> $$
> U = -\frac1\pi\ln\left|\frac{1 - z}{1 + z}\right| .
> $$
>
> So the flux lines $|1 - z| = k|1 + z|$ are arcs of circles with centers on the $x$ axis (as in [[§119★ Steady Temperatures in a Half Plane#^ex-119-2|Example §119.2]]), and the segment of the $y$ axis between the electrodes ($k = 1$) is a flux line.
>
> **Boundedness matters.** If the imaginary part $Ae^u\sin v$ of $Ae^w$ ($A$ real) is added to (3), the result is still harmonic in $v > 0$ and still $0$ on $u > 0$ and $1$ on $u < 0$ (since $\sin v = 0$ on $v = 0$), but it is unbounded for $A \ne 0$, since $e^u \to \infty$; in the disk this happens near $z = -1$, where $u = 2y/|1 + z|^2$ is unbounded.
>
> *B&C: Sec. 123, Example 1 and Exercise 1*

^ex-123-1

![[m342-123-1.svg]]
*Example §123.1. Equipotentials $V = 0.1, \ldots, 0.9$ (blue), arcs of circles through the gaps $\pm1$; the diameter is $V = \frac12$. Flux lines (orange), arcs of circles centered on the $x$ axis, run from the lower electrode ($V = 1$, red) to the upper one ($V = 0$) and cross the equipotentials at right angles.*

*Chain: the map $(i - z)/(i + z)$ earlier in [[§111a Three Linear Fractional Maps, the Sine Half Strip and ((z − 1)∕(z + 1))^(1∕2)#The Map (i − z)∕(i + z)|Chapter 8]]; the split cylinder later in [[§140a The Split Cylinder and the Boundary Values cos θ#The Split Cylinder|Chapter 12]]*

> [!remark]- Connections
> - Used in Electromagnetism: Example §123.1 is the split cylinder solved by a Möbius map — [[§C6.4★ The Complex Potential and the Variational Principle#^ex-c6-4-3|EM Example §C6.4.3]].

## A Half Annulus via a Rectangle

> [!example] Example §123.2: A Half Annulus Solved by a Series in a Rectangle
> Let $r_0 > 1$. Find the potential in the half annulus $1 < r < r_0$, $0 < \theta < \pi$ which is $1$ on the segment $-r_0 < x < -1$ of the $x$ axis and $0$ on the rest of the boundary (both semicircles and the segment $1 < x < r_0$) (B&C's Fig. 166, left).
>
> **The rectangle.** The problem on the right in B&C's Fig. 166, harmonic in $0 < u < \ln r_0$, $0 < v < \pi$, equal to $1$ on the top $v = \pi$ and $0$ on the other three sides, has the series solution
>
> $$
> V = \frac4\pi\sum_{n=1}^{\infty}\frac{\sinh(\alpha_nv)}{\sinh(\alpha_n\pi)}\cdot\frac{\sin(\alpha_nu)}{2n - 1}, \qquad \alpha_n = \frac{(2n - 1)\pi}{\ln r_0} \quad (n = 1, 2, \ldots). \qquad (6), (7)
> $$
>
> (B&C quotes this from separation of variables; here is why.) Each term $\sinh(\alpha v)\sin(\alpha u)$ is harmonic, vanishes on $u = 0$, on $u = \ln r_0$ (since $\alpha_n\ln r_0$ is a multiple of $\pi$) and on $v = 0$. At $v = \pi$ the series is $\frac4\pi\sum\frac{\sin(\alpha_nu)}{2n - 1}$, the Fourier sine series of the constant $1$ on $0 < u < \ln r_0$, which converges to $1$ there.
>
> **The map.** The branch
>
> $$
> \log z = \ln r + i\theta \qquad \Big(r > 0,\ -\frac\pi2 < \theta < \frac{3\pi}2\Big) \qquad (8)
> $$
>
> maps the half annulus one to one onto the rectangle: the arcs $r = 1$ and $r = r_0$ go to the sides $u = 0$ and $u = \ln r_0$; the segment $1 < x < r_0$ ($\theta = 0$) to the bottom $v = 0$; the segment $-r_0 < x < -1$ ($\theta = \pi$) to the top $v = \pi$. Corresponding boundary points carry the same values, so by Theorems [[§116★ Transformations of Harmonic Functions#^thm-116-1|§116.1]] and [[§117★ Transformations of Boundary Conditions#^thm-117-2|§117.2]], with $u = \ln r$ and $v = \theta$,
>
> $$
> V(r, \theta) = \frac4\pi\sum_{n=1}^{\infty}\frac{\sinh(\alpha_n\theta)}{\sinh(\alpha_n\pi)}\cdot\frac{\sin(\alpha_n\ln r)}{2n - 1} . \qquad (9)
> $$
>
> (Numerically, with $r_0 = 3$: $V(2, \pi - 0.01) \approx 0.980$, near the electrode at potential $1$, and $V(2, 1) \approx 0.0025$.)
>
> *B&C: Sec. 123, Example 2*

^ex-123-2

> [!remark]- Connections
> - The series (6) is the rectangle solution of separation of variables, [[§36 Potential in a Rectangle#^thm-36-1|341 Thm. §36.1]], the coefficients $\frac{4}{\pi(2n - 1)}$ being those of the sine series of the constant $1$. The polar Laplacian that (9) satisfies directly is [[§35 Potential Equation#^thm-35-3|341 Thm. §35.3]].

## More Mapped Problems

> [!example] Example §123.3: A Half Cylinder over a Plane, and a Wedge
> **(a)** Show that (4) maps the upper half of the disk onto the first quadrant of the $w$ plane and the diameter $CE$ (the segment $-1 < x < 1$) onto the positive $v$ axis. Then find the potential in the space enclosed by the half cylinder $x^2 + y^2 = 1$, $y \ge 0$, and the plane $y = 0$, when $V = 0$ on the cylindrical surface and $V = 1$ on the plane (B&C's Fig. 167).
>
> By Example §123.1, (4) maps the upper semicircle onto the positive $u$ axis. For real $z = x$, $-1 < x < 1$, $w = i\frac{1 - x}{1 + x}$ is on the positive $v$ axis. The upper half disk is bounded by these two pieces, and $u = \frac{2y}{|1 + z|^2} > 0$, $v = \frac{1 - x^2 - y^2}{|1 + z|^2} > 0$ there: it goes onto the first quadrant. The new problem, $V = 0$ on the positive $u$ axis and $V = 1$ on the positive $v$ axis, has the solution $V = \frac2\pi\arctan\frac vu$ ([[§118★ Steady Temperatures#^ex-118-1|Example §118.1]]), so
>
> $$
> V = \frac2\pi\arctan\Big(\frac{1 - x^2 - y^2}{2y}\Big) \qquad \Big(0 \le \arctan t \le \frac\pi2\Big).
> $$
>
> **(b)** Find the potential $V(r, \theta)$ in the space $0 < r < 1$, $0 < \theta < \pi/4$ bounded by the half planes $\theta = 0$, $\theta = \pi/4$ and the cylindrical surface $r = 1$, when $V = 1$ on the plane faces and $V = 0$ on the cylindrical one.
>
> $Z = z^4$ maps the sector onto the upper half disk: $\theta = 0$ goes to $0 < X < 1$ and $\theta = \pi/4$ to $-1 < X < 0$ (the diameter), and the arc to the upper semicircle; it is conformal for $z \ne 0$. With $|Z|^2 = r^8$ and $\operatorname{Im} Z = r^4\sin 4\theta$, part (a) gives
>
> $$
> V = \frac2\pi\arctan\Big(\frac{1 - r^8}{2r^4\sin 4\theta}\Big) \qquad \Big(0 \le \arctan t \le \frac\pi2\Big).
> $$
>
> Check: as $\theta \to 0^+$ or $\theta \to \frac\pi4^-$ (with $r < 1$), $\sin 4\theta \to 0^+$ and $V \to 1$; as $r \to 1^-$, the numerator tends to $0$ and $V \to 0$.
>
> *B&C: Sec. 123, Exercises 2 and 3*

^ex-123-3

> [!example] Example §123.4: A Cylinder with One Quarter Grounded
> Find the potential inside a long cylinder $r = 1$ when $V = 0$ on the first quadrant ($0 < \theta < \pi/2$) of the cylindrical surface and $V = 1$ on the rest ($\pi/2 < \theta < 2\pi$). Show that $V = \frac34$ on the axis.
>
> **Map.** The transformation $w = i\,\dfrac{z + e^{-i\pi/4}}{z + e^{i\pi/4}}$ maps the upper half plane onto the unit disk, $z = 0$ to $1$, $z = 1$ to $e^{i\pi/4}$ and $z = \infty$ to $i$ ([[§101★ Mappings of the Upper Half Plane#^ex-101-2|Example §101.2]] with $\alpha = \pi/2$, which is [[§101★ Mappings of the Upper Half Plane#^ex-101-3|Example §101.3]]; B&C's Sec. 102, Exercises 4 and 5): the positive real axis goes onto the quarter circle from $1$ to $i$, and the negative real axis onto the rest of the circle. Write the problem in the disk with variable $z$ and use the inverse, solved from $w(Z + e^{i\pi/4}) = i(Z + e^{-i\pi/4})$ and $ie^{-i\pi/4} = e^{i\pi/4}$:
>
> $$
> Z = e^{i\pi/4}\,\frac{1 - z}{z - i} .
> $$
>
> It maps the disk onto the upper half plane, the arc $0 < \theta < \pi/2$ onto $X > 0$ (where $V = 0$) and the rest of the circle onto $X < 0$ (where $V = 1$). (Numerically, $\theta = 0.3$ goes to $Z \approx 0.252$ and $\theta = 4$ to $Z \approx -0.970$.)
>
> **Solution.** As in Example §123.1, $V = \frac1\pi\operatorname{Arg} Z$ $(0 \le \operatorname{Arg} Z \le \pi)$:
>
> $$
> V = \frac1\pi\operatorname{Arg}\Big(e^{i\pi/4}\,\frac{1 - z}{z - i}\Big) .
> $$
>
> **On the axis**, $z = 0$: $Z = e^{i\pi/4}\cdot\frac{1}{-i} = e^{i\pi/4}e^{i\pi/2} = e^{i3\pi/4}$, so $V = \frac1\pi\cdot\frac{3\pi}{4} = \frac34$. This agrees with the mean value property: the potential at the center of a circle is the average of its boundary values, $\frac{1}{2\pi}\big(0\cdot\frac\pi2 + 1\cdot\frac{3\pi}{2}\big) = \frac34$ ([[§39 Potential in a Disk#^thm-39-4|341 Thm. §39.4]]; B&C's version is the Poisson integral, [[§134★ Poisson Integral Formula#^thm-134-1|Theorem §134.1]]).
>
> *B&C: Sec. 123, Exercise 8*

^ex-123-4
