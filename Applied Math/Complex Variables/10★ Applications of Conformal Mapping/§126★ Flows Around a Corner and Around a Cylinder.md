---
type: section
subject: "[[Complex Variables]]"
chapter: 10
section: 126
bc: "126"
aliases: ["B&C 126"]
tags: [complex-variables, math342, extension]
---
← [[§125★ The Stream Function]] · ↑ [[· 10★ Applications of Conformal Mapping]] · [[§127★ Mapping the Real Axis onto a Polygon]] →

*Brown–Churchill, Section 126 (with Exercises 3–6 and 10).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

To find a flow in a region of the $z$ plane, map the region conformally onto one where the flow is known (most often the upper half plane with uniform flow $F = Aw$) and compose: the complex potential in the $z$ plane is $F[f(z)]$. The squaring map turns uniform flow into flow around a right-angled corner, and the Joukowski map $w = z + 1/z$ turns it into the classical flow past a circular cylinder. From the complex potential one reads off the streamlines, the velocity $V = \overline{F'(z)}$, and, by Bernoulli's equation, where the pressure is greatest (at the stagnation points, where the fluid comes to rest) and least.

## Complex Potentials Under Conformal Maps

> [!theorem] Proposition §126.1: Composing a Complex Potential with an Analytic Map
> Let $w = f(z) = u(x, y) + iv(x, y)$ be analytic and map a domain $D_z$ onto a domain of flow $D_w$, and let $F(w) = \phi(u, v) + i\psi(u, v)$ be the complex potential of a flow in $D_w$. Then
>
> $$
> F[f(z)] = \phi[u(x, y), v(x, y)] + i\psi[u(x, y), v(x, y)]
> $$
>
> is analytic in $D_z$: its real and imaginary parts are harmonic there and may be interpreted as the velocity potential and stream function of a flow in $D_z$. A streamline or natural boundary $\psi(u, v) = c_2$ in the $uv$ plane corresponds to the streamline or natural boundary $\psi[u(x, y), v(x, y)] = c_2$ in the $xy$ plane.
>
> *B&C: Sec. 126 (text)*

^prop-126-1

> [!proof]+ Proof
> $F[f(z)]$ is analytic as a composition of analytic functions ([[§20 Rules for Differentiation|§20]]), so its real and imaginary parts are harmonic and the second is a harmonic conjugate of the first ([[§115★ Harmonic Conjugates#^thm-115-1|Theorem §115.1]]; equivalently Theorem [[§116★ Transformations of Harmonic Functions#^thm-116-1|§116.1]] applied to $\phi$ and $\psi$). A point $(x, y)$ lies on the curve $\psi[u(x, y), v(x, y)] = c_2$ exactly when its image lies on $\psi(u, v) = c_2$. A natural boundary, across which no fluid flows, has $\psi$ constant on it; its preimage has the composed $\psi$ constant on it, so it is a streamline of the new flow (Theorem [[§117★ Transformations of Boundary Conditions#^thm-117-2|§117.2]], the case $h = h_0$).

^pf-126-1

*Uses:* [[§20 Rules for Differentiation|§20]], [[§115★ Harmonic Conjugates#^thm-115-1|§115.1]], [[§116★ Transformations of Harmonic Functions#^thm-116-1|§116.1]], [[§117★ Transformations of Boundary Conditions#^thm-117-2|§117.2]], [[§125★ The Stream Function#^def-125-1|Def. §125.1]]

To avoid an excess of notation, the same symbols $F$, $\phi$ and $\psi$ are used for the complex potential, velocity potential and stream function in both planes.

> [!remark] Remark: Method — Finding a Flow by Conformal Mapping
> 1. **Map** the region of flow conformally onto a region where the flow is known, typically $f\colon D_z \to \{v > 0\}$ with the walls going onto the real axis.
> 2. **Write the complex potential there**: $F = Aw$ for uniform flow to the right in the upper half plane ([[§125★ The Stream Function#^ex-125-1|Example §125.1]]), $A > 0$.
> 3. **Compose**: $F[f(z)]$ is the complex potential in $D_z$ (Proposition §126.1); the walls are the streamline $\psi = 0$.
> 4. **Read off** the stream function $\psi = \operatorname{Im}F$ and its streamlines, the velocity $V = \overline{F'(z)}$ and speed $|F'(z)|$ ([[§125★ The Stream Function#^prop-125-1|Proposition §125.1]]), and the pressure from Bernoulli's equation ([[§124★ Two-Dimensional Fluid Flow#^prop-124-3|Proposition §124.3]]): it is greatest where the speed is least, at stagnation points where $F'(z) = 0$. Check the behavior far away (for example $V \to A$).

^rem-126-1

## The Corner and the Cylinder

> [!example] Example §126.1: Flow Around a Corner
> Find the flow in the first quadrant $x > 0$, $y > 0$ that comes in downward parallel to the $y$ axis but is forced to turn a corner near the origin (B&C's Fig. 173), and the point of the closed quadrant where the pressure is greatest.
>
> **Map and potential.** $w = z^2 = x^2 - y^2 + i2xy$ maps the first quadrant onto the upper half plane and its boundary onto the $u$ axis ([[§14 The Mapping w = z²|§14]], Example 2). The complex potential of uniform flow to the right in the upper half of the $w$ plane is $F = Aw$ ($A > 0$; [[§125★ The Stream Function#^ex-125-1|Example §125.1]]). So the potential in the quadrant is
>
> $$
> F = Az^2 = A(x^2 - y^2) + i2Axy , \qquad (1)
> $$
>
> and the stream function is
>
> $$
> \psi = 2Axy , \qquad (2)
> $$
>
> harmonic in the quadrant and zero on its boundary. The streamlines are the branches of the rectangular hyperbolas $2Axy = c_2$ in the quadrant.
>
> **Velocity.** By (3) of §125, $V = \overline{2Az} = 2A(x - iy)$. Far up the $y$ axis ($x$ small, $y$ large) this is nearly $-2Ayi$, a downward flow, as required; along the $x$ axis it is $2Ax$, to the right. The speed $|V| = 2A\sqrt{x^2 + y^2}$ is proportional to the distance from the origin. The value of $\psi$ at $(x, y)$ is the rate of flow across a segment from the origin to that point (Proposition [[§125★ The Stream Function#^prop-125-2|§125.2]]); the velocity potential $A(x^2 - y^2)$ is that of [[§124★ Two-Dimensional Fluid Flow#^ex-124-3|Example §124.3]].
>
> **Pressure.** By Bernoulli's equation the pressure is greatest where the speed is least. On the closed quadrant $|V| = 2A|z|$ is least, namely $0$, only at the corner $z = 0$: the pressure is greatest at the origin, a stagnation point where the fluid comes to rest ($F'(0) = 0$; the map $z^2$ is not conformal there).
>
> *B&C: Sec. 126, Example 1 and Exercise 3*

^ex-126-1

> [!example] Example §126.2: Flow Around a Cylinder
> A long circular cylinder of unit radius is placed in a large body of fluid flowing with uniform velocity, its axis perpendicular to the flow. Represent the cylinder by $x^2 + y^2 = 1$ and let the flow far away be parallel to the $x$ axis and to the right (B&C's Fig. 174). Find the flow, the speed on the cylinder, and where the pressure on the cylinder is greatest and least.
>
> **Region.** By symmetry the points of the $x$ axis outside the circle may be treated as boundary points, so it suffices to take as region of flow the part of the upper half plane outside the circle. Its boundary (the upper semicircle and the two parts of the $x$ axis with $|x| \ge 1$) is mapped onto the entire $u$ axis, and the region itself onto the upper half plane, by
>
> $$
> w = z + \frac1z
> $$
>
> (B&C's Appendix 2, Fig. 17). Indeed, for $z = re^{i\theta}$, $w = \big(r + \frac1r\big)\cos\theta + i\big(r - \frac1r\big)\sin\theta$, so $\operatorname{Im} w > 0$ exactly when $r > 1$ and $0 < \theta < \pi$. The map is one to one there: $z_1 + \frac1{z_1} = z_2 + \frac1{z_2}$ means $(z_1 - z_2)\big(1 - \frac{1}{z_1z_2}\big) = 0$, and $z_1z_2 = 1$ is impossible for $|z_1|, |z_2| > 1$. It is onto: for $\operatorname{Im} w > 0$ the roots of $z^2 - wz + 1 = 0$ have product $1$ and are not on the unit circle (that would make $w$ real), so one has $|z| > 1$, and then $\operatorname{Im} w > 0$ forces $\sin\theta > 0$.
>
> **Potential.** With $F = Aw$ in the half plane ($A > 0$), the complex potential in the region is
>
> $$
> F = A\Big(z + \frac1z\Big) , \qquad (3)
> $$
>
> and the velocity is
>
> $$
> V = \overline{F'(z)} = A\Big(1 - \frac{1}{\bar z^2}\Big) . \qquad (4)
> $$
>
> It approaches $A$ as $|z|$ increases: far from the cylinder the flow is nearly uniform and parallel to the $x$ axis. Since $V(\bar z) = \overline{V(z)}$, (4) also gives the mirror-image flow in the lower half, the lower semicircle being a streamline. In polar coordinates the stream function is
>
> $$
> \psi = \operatorname{Im}A\Big(re^{i\theta} + \frac1re^{-i\theta}\Big) = A\Big(r - \frac1r\Big)\sin\theta . \qquad (5)
> $$
>
> The streamlines $A\big(r - \frac1r\big)\sin\theta = c_2$ are symmetric about the $y$ axis ($\sin(\pi - \theta) = \sin\theta$) and have asymptotes parallel to the $x$ axis ($r\sin\theta = y \to c_2/A$ as $r \to \infty$). For $c_2 = 0$ the streamline consists of the circle $r = 1$ and the parts of the $x$ axis outside it.
>
> **Speed and pressure on the cylinder.** On $z = e^{i\theta}$, $F'(z) = A(1 - e^{-2i\theta}) = Ae^{-i\theta}\big(e^{i\theta} - e^{-i\theta}\big) = 2iAe^{-i\theta}\sin\theta$, so the speed is $|V| = 2A|\sin\theta|$. It is $0$ at $z = \pm1$ (the stagnation points, where the flow divides and rejoins) and largest, $2A$, at $z = \pm i$. By Bernoulli's equation the pressure on the cylinder is greatest at $z = \pm1$ and least at $z = \pm i$.
>
> **A cylinder of radius $r_0$.** Scaling, $\zeta = z/r_0$ maps $|z| > r_0$ onto $|\zeta| > 1$, and $F = Ar_0\big(\zeta + \frac1\zeta\big) = A\Big(z + \dfrac{r_0^2}{z}\Big)$ is the complex potential whose velocity $\overline{F'} = A\big(1 - r_0^2/\bar z^2\big)$ tends to the real constant $A$ as the point recedes from the cylinder $r = r_0$; on $|z| = r_0$, $\psi = \operatorname{Im}\big(A(r_0e^{i\theta} + r_0e^{-i\theta})\big) = 0$.
>
> *B&C: Sec. 126, Example 2 and Exercises 4 and 5*

^ex-126-2

![[m342-126-1.svg]]
*Left: Example §126.1, streamlines $xy = $ const of $F = Az^2$; the fluid comes down along the $y$ axis and turns the corner, with a stagnation point at $0$. Right: Example §126.2, streamlines $(r - 1/r)\sin\theta = c$ of $F = A(z + 1/z)$ around the unit cylinder; the flow divides at the stagnation point $-1$ and rejoins at $1$, and is fastest at $\pm i$.*

## Two Variations

> [!example] Example §126.3: Flow in a Wedge of Angle π/4
> Obtain the stream function $\psi = Ar^4\sin 4\theta$ for a flow in the angular region $r \ge 0$, $0 \le \theta \le \pi/4$ (B&C's Fig. 175), and describe the streamlines.
>
> $w = z^4 = r^4e^{4i\theta}$ maps the wedge $0 < \theta < \pi/4$ onto the upper half plane $0 < \arg w < \pi$, and its two edges onto the positive and negative $u$ axis; it is conformal except at $0$. With $F = Aw$ there, $F = Az^4$ in the wedge, so
>
> $$
> \psi = \operatorname{Im}\big(Ar^4e^{4i\theta}\big) = Ar^4\sin 4\theta ,
> $$
>
> zero on both edges. The streamlines $r^4\sin 4\theta = c_2$ come in parallel to the edge $\theta = \pi/4$ and go out parallel to the edge $\theta = 0$ (for small $\theta$, $r^4\sin 4\theta \approx 4r^4\theta \approx 4x^3y$, so $y \approx c_2/(4Ax^3)$). The velocity $V = \overline{4Az^3}$ has speed $4Ar^3$, vanishing at the corner faster than in the right-angled corner (where it is $2Ar$). In general $F = Az^n$ gives the flow in a wedge of angle $\pi/n$.
>
> *B&C: Sec. 126, Exercise 6*

^ex-126-3

> [!example] Example §126.4: A Cylinder in an Oblique Stream
> Suppose the flow far from the unit cylinder of Example §126.2 is uniform in a direction making an angle $\alpha$ with the $x$ axis: $\lim_{|z|\to\infty}V = Ae^{i\alpha}$ $(A > 0)$. Find the complex potential.
>
> **Rotate.** $\zeta = ze^{-i\alpha}$ is a rotation through $-\alpha$; it maps the exterior of the unit circle onto itself and turns the direction $\alpha$ into the direction of the positive real axis. In the $\zeta$ plane the flow is that of Example §126.2, $A(\zeta + 1/\zeta)$, so
>
> $$
> F = A\Big(ze^{-i\alpha} + \frac1ze^{i\alpha}\Big) .
> $$
>
> **Check.** $F'(z) = A\big(e^{-i\alpha} - e^{i\alpha}/z^2\big) \to Ae^{-i\alpha}$, so $V = \overline{F'(z)} \to Ae^{i\alpha}$. On $z = e^{i\theta}$, $ze^{-i\alpha} + e^{i\alpha}/z = e^{i(\theta - \alpha)} + e^{-i(\theta - \alpha)} = 2\cos(\theta - \alpha)$ is real, so $\psi = 0$ on the cylinder: it is a streamline. The stagnation points, where $F' = 0$, are $z^2 = e^{2i\alpha}$, that is, $z = \pm e^{i\alpha}$.
>
> *B&C: Sec. 126, Exercise 10*

^ex-126-4
