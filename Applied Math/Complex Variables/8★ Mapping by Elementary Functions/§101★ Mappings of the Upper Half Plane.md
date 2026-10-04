---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: 101
bc: "101"
aliases: ["B&C 101"]
tags: [complex-variables, math342, extension]
---
← [[§100★ An Implicit Form]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§102★ Examples (Mappings of the Upper Half Plane)]] →

*Brown–Churchill, Section 101.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Which linear fractional transformations carry the upper half plane onto the unit disk? This section finds all of them: they are exactly $w = e^{i\alpha}(z - z_0)/(z - \bar z_0)$ with $\operatorname{Im} z_0 > 0$, where $z_0$ is the point sent to the center and $\alpha$ a free rotation. The proof that every such map works is a one-line piece of geometry: the real axis is the perpendicular bisector of $z_0$ and $\bar z_0$. The half plane and the disk are the two standard regions of potential theory, so this family lets a Dirichlet problem be moved freely between them (compare the Poisson integrals of [[§134★ Poisson Integral Formula|§134]] and [[§139★ Dirichlet Problem for a Half Plane|§139]]).

## The Theorem

> [!theorem] Theorem §101.1: Linear Fractional Maps of the Upper Half Plane onto the Unit Disk
> For a linear fractional transformation $w = T(z)$ the following are equivalent:
> - **(a)** it maps the upper half plane $\operatorname{Im} z > 0$ onto the open disk $|w| < 1$, and the boundary $\operatorname{Im} z = 0$ of the half plane, together with the point at infinity, onto the boundary $|w| = 1$ of the disk;
> - **(b)** it has the form
>
>   $$
>   w = e^{i\alpha}\Big(\frac{z - z_0}{z - \bar z_0}\Big) \qquad (\operatorname{Im} z_0 > 0) ,
>   $$
>
>   where $\alpha$ is a real number.
>
> *B&C: Sec. 101 (text)*

^thm-101-1

> [!proof]+ Proof
> **(a) implies (b).** Write $T$ as
>
> $$
> w = \frac{az + b}{cz + d} \qquad (ad - bc \ne 0) \qquad (1)
> $$
>
> and use that the three points $z = 0$, $z = 1$, $z = \infty$ of the extended real axis must have images of modulus $1$. (The point at infinity has to be included: $T$ is one to one on the extended plane, so if the finite real axis alone covered the circle, $T(\infty)$ could not lie on it; yet $T(\infty)$ is the limit of $T(x)$ as $x \to \infty$ along the real axis (continuity, [[§99★ Linear Fractional Transformations#^thm-99-4|Theorem §99.4]]), so it lies on the circle, which is closed. B&C's "boundary" means the extended real axis.)
>
> At $z = 0$: $T(0)$ must be finite, so $d \ne 0$ (if $d = 0$ then $T(0) = \infty$), and $|T(0)| = |b/d| = 1$ gives
>
> $$
> |b| = |d| \ne 0 . \qquad (2)
> $$
>
> At $z = \infty$: by [[§99★ Linear Fractional Transformations#^def-99-2|Definition §99.2]], $T(\infty)$ is finite only if $c \ne 0$, and then $T(\infty) = a/c$. So $|a/c| = 1$:
>
> $$
> |a| = |c| \ne 0 . \qquad (3)
> $$
>
> Since $a$ and $c$ are nonzero, (1) can be rewritten
>
> $$
> w = \frac ac\cdot\frac{z + (b/a)}{z + (d/c)} . \qquad (4)
> $$
>
> By (2) and (3), $|a/c| = 1$ and $|b/a| = |d/c| \ne 0$. So with $a/c = e^{i\alpha}$ ($\alpha$ real), $z_0 = -b/a$ and $z_1 = -d/c$, (4) becomes
>
> $$
> w = e^{i\alpha}\Big(\frac{z - z_0}{z - z_1}\Big) \qquad (|z_1| = |z_0| \ne 0) . \qquad (5)
> $$
>
> At $z = 1$: $|w| = 1$ means $|1 - z_1| = |1 - z_0|$, or
>
> $$
> (1 - z_1)(1 - \bar z_1) = (1 - z_0)(1 - \bar z_0) .
> $$
>
> Expanding, and using $z_1\bar z_1 = z_0\bar z_0$ (since $|z_1| = |z_0|$), this reduces to $z_1 + \bar z_1 = z_0 + \bar z_0$, that is $\operatorname{Re} z_1 = \operatorname{Re} z_0$. Two numbers with the same modulus and the same real part have imaginary parts equal up to sign, so either $z_1 = z_0$ or $z_1 = \bar z_0$. If $z_1 = z_0$, (5) is the constant function $w = e^{i\alpha}$, which is not a linear fractional transformation. Hence $z_1 = \bar z_0$, and $z_0$ is not real.
>
> Finally, (5) with $z_1 = \bar z_0$ maps $z_0$ to $w = 0$, which lies in the disk $|w| < 1$. By (a) the disk is the image of the upper half plane, and $T$ is one to one on the extended plane ([[§99★ Linear Fractional Transformations#^thm-99-4|Theorem §99.4]]), so the only preimage $z_0$ of $0$ lies in the upper half plane: $\operatorname{Im} z_0 > 0$. This is (b).
>
> **(b) implies (a).** First, (b) is a genuine linear fractional transformation: with $a = e^{i\alpha}$, $b = -e^{i\alpha}z_0$, $c = 1$, $d = -\bar z_0$, $ad - bc = e^{i\alpha}(z_0 - \bar z_0) = 2ie^{i\alpha}\operatorname{Im} z_0 \ne 0$. Taking moduli in (b),
>
> $$
> |w| = \frac{|z - z_0|}{|z - \bar z_0|} .
> $$
>
> The real axis is the perpendicular bisector of the segment joining $z_0$ and $\bar z_0$. If $z$ lies above the real axis, it is on the same side as $z_0$, so it is closer to $z_0$ than to $\bar z_0$: $|z - z_0| < |z - \bar z_0|$, that is $|w| < 1$. If $z$ lies below the real axis, $|z - z_0| > |z - \bar z_0|$ and $|w| > 1$. If $z$ is real, $|z - z_0| = |z - \bar z_0|$ and $|w| = 1$; also $T(\infty) = e^{i\alpha}$ has modulus $1$.
>
> So $T$ maps the upper half plane into the open disk, the lower half plane into the exterior $|w| > 1$, and the extended real axis into the circle. Since $T$ is a one-to-one map of the extended plane onto itself (Theorem §99.4), every point of the disk has a preimage, which cannot lie in the lower half plane or on the extended real axis; hence it lies in the upper half plane. Likewise every point of the circle comes from the extended real axis. This is (a).

^pf-101-1

*Uses:* [[§99★ Linear Fractional Transformations#^def-99-2|Def. §99.2]], [[§99★ Linear Fractional Transformations#^thm-99-4|§99.4]]

![[m342-101-1.svg]]
*The case $z_0 = i$, $\alpha = 0$ of Theorem §101.1, $w = (z - i)/(z + i)$. Left: a point $z$ above the real axis is nearer to $z_0 = i$ than to its mirror image $\bar z_0 = -i$, so $|w| < 1$. Right: the horizontal lines $y = \frac12, 1, 2$ (red) go onto circles inside the disk, all tangent to the unit circle at $w = 1$, the image of $\infty$; the vertical half lines $x = -1, 0, 1$ (blue) go onto arcs from the boundary to $w = 1$, and $x = 0$ onto the radius from $-1$ to $1$. The point $z_0 = i$ goes to the center.*

> [!remark] Remark: What the Two Parameters Do
> In (b), $z_0$ is the point of the half plane that goes to the center $w = 0$, and the factor $e^{i\alpha}$ is a final rotation of the disk; the point at infinity goes to $w = e^{i\alpha}$. So a map of the half plane onto the disk can send any chosen point to the center, and then any chosen boundary point to any chosen point of the circle; after that it is fixed. This is the count of three real conditions behind Theorem §100.3: a boundary-to-boundary map is determined by three boundary points.

^rem-101-1

## Examples

The exercises on Sections 101 and 102 are printed after Section 102.

> [!example] Example §101.1: The Lower Half Plane
> Show that if $\operatorname{Im} z_0 < 0$, the transformation $w = e^{i\alpha}(z - z_0)/(z - \bar z_0)$ maps the lower half plane $\operatorname{Im} z \le 0$ onto the closed disk $|w| \le 1$.
>
> The argument of (b) implies (a) applies with the sides exchanged. Again $|w| = |z - z_0|/|z - \bar z_0|$ and the real axis bisects the segment from $z_0$ to $\bar z_0$, but now $z_0$ is below it. A point $z$ with $\operatorname{Im} z < 0$ is on the side of $z_0$, so $|w| < 1$; a point with $\operatorname{Im} z > 0$ has $|w| > 1$; a real $z$ has $|w| = 1$. By the bijectivity of Theorem §99.4, the open lower half plane goes onto $|w| < 1$ and the real axis together with $\infty$ onto $|w| = 1$; so the closed lower half plane goes onto the closed disk $|w| \le 1$ with the single boundary point $e^{i\alpha} = T(\infty)$ omitted.
>
> *B&C: Sec. 102, Exercise 6*

^ex-101-1

> [!example] Example §101.2: Prescribing Two Boundary Points
> The transformation $w = e^{i\alpha}(z - z_0)/(z - \bar z_0)$ sends $z = \infty$ to $w = e^{i\alpha}$. Show that if $0 < \alpha < 2\pi$, and $z = 0$ and $z = 1$ are to go to $w = 1$ and $w = \exp(i\alpha/2)$, then
>
> $$
> w = e^{i\alpha}\Big[\frac{z + \exp(-i\alpha/2)}{z + \exp(i\alpha/2)}\Big] .
> $$
>
> The condition at $z = 0$ is $e^{i\alpha}z_0/\bar z_0 = 1$, so $z_0/\bar z_0 = e^{-i\alpha}$. Writing $z_0 = |z_0|e^{i\beta}$, this says $e^{2i\beta} = e^{-i\alpha}$, so $z_0 = t\,e^{-i\alpha/2}$ with $t$ real and nonzero. The condition at $z = 1$ is
>
> $$
> e^{i\alpha}\frac{1 - te^{-i\alpha/2}}{1 - te^{i\alpha/2}} = e^{i\alpha/2} \iff 1 - te^{-i\alpha/2} = e^{-i\alpha/2}\big(1 - te^{i\alpha/2}\big) = e^{-i\alpha/2} - t ,
> $$
>
> that is $(1 + t)(1 - e^{-i\alpha/2}) = 0$. Since $0 < \alpha/2 < \pi$, $e^{-i\alpha/2} \ne 1$, so $t = -1$ and
>
> $$
> z_0 = -\exp(-i\alpha/2), \qquad \bar z_0 = -\exp(i\alpha/2) .
> $$
>
> This is admissible: $\operatorname{Im} z_0 = \sin(\alpha/2) > 0$. Substituting gives the stated formula.
>
> *B&C: Sec. 102, Exercise 4*

^ex-101-2

> [!example] Example §101.3: Following the Real Axis Around the Circle
> For $\alpha = \pi/2$, Example §101.2 gives (since $i\exp(-i\pi/4) = \exp(i\pi/4)$)
>
> $$
> w = \frac{iz + \exp(i\pi/4)}{z + \exp(i\pi/4)} .
> $$
>
> Track the real axis, with $A = -\infty$, $B = -1$, $C = 0$, $D = 1$, $E = +\infty$:
>
> | $z$ | $w$ | $\arg w$ |
> |---|---|---|
> | $\pm\infty$ ($A$, $E$) | $i$ | $\pi/2$ |
> | $-1$ ($B$) | $\dfrac{-i + e^{i\pi/4}}{-1 + e^{i\pi/4}} = e^{-3\pi i/4}$ | $-3\pi/4$ |
> | $0$ ($C$) | $1$ | $0$ |
> | $1$ ($D$) | $\dfrac{i + e^{i\pi/4}}{1 + e^{i\pi/4}} = e^{i\pi/4}$ | $\pi/4$ |
>
> (each value computed and checked numerically). As $x$ increases from $-\infty$ to $\infty$, $\arg w$ increases steadily: from $\pi/2$ through $\pi$ to $5\pi/4$ on $AB$, from $5\pi/4$ to $2\pi$ on $BC$, from $0$ to $\pi/4$ on $CD$, and from $\pi/4$ to $\pi/2$ on $DE$ (for instance $x = -2, -\frac12, \frac12, 2$ give $\arg w \approx 0.82\pi, 1.68\pi, 0.16\pi, 0.34\pi$). So the real axis, traversed left to right, goes once counterclockwise around the circle, starting and ending at $A' = E' = i$, and the upper half plane (on its left) goes onto the inside of the circle (on the left of the image), as Theorem §101.1 says.
>
> *B&C: Sec. 102, Exercise 5*

^ex-101-3
