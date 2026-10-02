---
type: section
subject: "[[Complex Variables]]"
chapter: 11
section: 133
bc: "133"
aliases: ["B&C 133"]
tags: [complex-variables, math342, extension]
---
← [[§132★ Flow in a Channel with an Offset]] · ↑ [[· 11★ The Schwarz–Christoffel Transformation]] · [[§134★ Poisson Integral Formula]] →

*Brown–Churchill, Section 133.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Two parallel grounded conducting planes with a semi-infinite plate at potential $1$ midway between them form a degenerate quadrilateral: a strip divided along half its length. The Schwarz–Christoffel transformation maps the upper half plane onto this divided strip; the three conductors become three intervals of the real axis, where the potential is the elementary harmonic function $\frac1\pi(\theta_1 - \theta_2)$ of [[§119★ Steady Temperatures in a Half Plane#^ex-119-1|Example §119.1]]. Mapping back gives the potential around the edge of the plate in closed form. The same technique gives the potential for a plate at any height ($h\pi$ instead of $\pi/2$) and the temperatures near a step, both from B&C's exercises.

> [!example] Example §133.1: Mapping the Upper Half Plane onto the Divided Strip
> Two parallel conducting plates of infinite extent are kept at potential $V = 0$, and a parallel semi-infinite plate placed midway between them is kept at $V = 1$. The coordinate system and unit of length are chosen so that the plates lie in the planes $v = 0$, $v = \pi$ and $v = \pi/2$ ($u \ge 0$). Find a conformal map of the upper half plane onto the region between the plates.
>
> **Angles.** The cross section has the limiting form of a quadrilateral with vertices $w_1$ and $w_3$ moving out to the right (between the plates, below and above the middle plate) and $w_4$ moving to the left; $w_2 = \pi i/2$ is the edge of the middle plate. Let $x_4 = \infty$ correspond to $w_4$, choose $x_1 = -1$, $x_3 = 1$, and leave $x_2$ to be determined. The limiting exterior angles are
>
> $$
> k_1\pi = \pi, \qquad k_2\pi = -\pi, \qquad k_3\pi = k_4\pi = \pi .
> $$
>
> **Derivative and integral.** Thus
>
> $$
> \frac{dw}{dz} = A(z + 1)^{-1}(z - x_2)(z - 1)^{-1} = A\,\frac{z - x_2}{z^2 - 1} = \frac A2\Big(\frac{1 + x_2}{z + 1} + \frac{1 - x_2}{z - 1}\Big) ,
> $$
>
> and
>
> $$
> w = \frac A2\big[(1 + x_2)\operatorname{Log}(z + 1) + (1 - x_2)\operatorname{Log}(z - 1)\big] + B . \qquad (1)
> $$
>
> **Constants.** Let $A = A_1 + iA_2$, $B = B_1 + iB_2$. When $z = x$, $w$ lies on the boundary, and by (1)
>
> $$
> u + iv = \frac{A_1 + iA_2}{2}\Big\{(1 + x_2)\big[\ln|x + 1| + i\arg(x + 1)\big] + (1 - x_2)\big[\ln|x - 1| + i\arg(x - 1)\big]\Big\} + B_1 + iB_2 . \qquad (2)
> $$
>
> - *The bottom plate.* The segment $w_4w_1$ tends to the $u$ axis; it is the image of the part of the $x$ axis to the left of $x_1 = -1$ (the segment $w_3w_4$ is the image of $x > 1$, and the other two sides are the images of the remaining two intervals). So as $v = 0$ and $u \to +\infty$, $x \to -1$ from the left; then $\arg(x + 1) = \arg(x - 1) = \pi$ and $\ln|x + 1| \to -\infty$. Since $-1 < x_2 < 1$, the real part of the braces tends to $-\infty$; as $v = 0$, the imaginary part of the right side must stay bounded, which forces $A_2 = 0$. Equating imaginary parts, $0 = \frac{A_1}{2}\big[(1 + x_2)\pi + (1 - x_2)\pi\big] + B_2$, so
>
> $$
> -\pi A_1 = B_2, \qquad A_2 = 0 . \qquad (3)
> $$
>
> - *The lower side of the middle plate.* The segment $w_1w_2$ tends to the half line $v = \pi/2$, $u \ge 0$, the image of $-1 < x \le x_2$, where $\arg(x + 1) = 0$ and $\arg(x - 1) = \pi$. Identifying imaginary parts,
>
> $$
> \frac\pi2 = \frac{A_1}{2}(1 - x_2)\pi + B_2 . \qquad (4)
> $$
>
> - *The top plate.* The points of $w_3w_4$ tend to $u + \pi i$, the images of $x > 1$, where both arguments are $0$: so $\pi = B_2$.
>
> Then (3) and (4) give $A_1 = -1$ and $x_2 = 0$. So $x = 0$ is the point whose image is the edge $w = \pi i/2$; substituting $x = 0$ into (2) and identifying real parts, $0 = -\frac12(\ln1 + \ln1) + B_1$, so $B_1 = 0$. Transformation (1) becomes
>
> $$
> w = -\frac12\big[\operatorname{Log}(z + 1) + \operatorname{Log}(z - 1)\big] + \pi i , \qquad (5)
> $$
>
> or, exponentiating $-2(w - \pi i) = \operatorname{Log}(z + 1) + \operatorname{Log}(z - 1)$,
>
> $$
> z^2 = 1 + e^{-2w} . \qquad (6)
> $$
>
> (Indeed $e^{-2w} = e^{2\pi i}(z + 1)(z - 1) = z^2 - 1$.)
>
> *B&C: Sec. 133 (text), equations (1)–(6)*

^ex-133-1

> [!example] Example §133.2: The Potential about the Edge
> Find the potential $V(u, v)$ between the plates of Example §133.1.
>
> **In the $z$ plane.** Under (5) the required harmonic function $V(u, v)$ becomes a harmonic function of $x$ and $y$ in the half plane $y > 0$ ([[§116★ Transformations of Harmonic Functions#^thm-116-1|Theorem §116.1]], [[§117★ Transformations of Boundary Conditions#^thm-117-2|Theorem §117.2]]), with boundary values $V = 0$ for $x < -1$ (bottom plate), $V = 1$ for $-1 < x < 1$ (both sides of the middle plate, since $x_2 = 0$ now) and $V = 0$ for $x > 1$ (top plate). The harmonic function in the half plane with these boundary values is the imaginary component of
>
> $$
> \frac1\pi\operatorname{Log}\frac{z - 1}{z + 1} = \frac1\pi\ln\frac{r_1}{r_2} + \frac i\pi(\theta_1 - \theta_2) ,
> $$
>
> where $r_1 = |z - 1|$, $r_2 = |z + 1|$, $\theta_1 = \arg(z - 1)$, $\theta_2 = \arg(z + 1)$, both angles ranging from $0$ to $\pi$. On $x > 1$, $\theta_1 = \theta_2 = 0$; on $x < -1$, $\theta_1 = \theta_2 = \pi$; on $-1 < x < 1$, $\theta_1 = \pi$, $\theta_2 = 0$. So $V = \frac1\pi(\theta_1 - \theta_2)$.
>
> **The tangent.** With $\tan\theta_1 = \dfrac{y}{x - 1}$ and $\tan\theta_2 = \dfrac{y}{x + 1}$,
>
> $$
> \tan\pi V = \tan(\theta_1 - \theta_2) = \frac{\frac{y}{x - 1} - \frac{y}{x + 1}}{1 + \frac{y^2}{x^2 - 1}} = \frac{2y}{x^2 + y^2 - 1} . \qquad (7)
> $$
>
> **In the $w$ plane.** Equation (6) furnishes $x^2 + y^2$ and $x^2 - y^2$ in terms of $u$ and $v$: $x^2 - y^2 + 2ixy = 1 + e^{-2u}(\cos2v - i\sin2v)$, and $x^2 + y^2 = |z^2| = \sqrt{1 + 2e^{-2u}\cos2v + e^{-4u}}$. Put
>
> $$
> s = -1 + \sqrt{1 + 2e^{-2u}\cos2v + e^{-4u}} = x^2 + y^2 - 1 .
> $$
>
> (B&C states the result; here is the computation.) Squaring $s + 1$ gives $s^2 + 2s = 2e^{-2u}\cos2v + e^{-4u}$. Also $2y^2 = (x^2 + y^2) - (x^2 - y^2) = (s + 1) - (1 + e^{-2u}\cos2v) = s - e^{-2u}\cos2v$. Hence $4y^2 = 2s - 2e^{-2u}\cos2v = e^{-4u} - s^2$, and since $y > 0$, (7) becomes
>
> $$
> \tan\pi V = \frac1s\sqrt{e^{-4u} - s^2} , \qquad (8)
> $$
>
> with $0 < V < 1$ fixing the branch ($\pi V$ is in $(0, \pi/2)$ where $s > 0$ and in $(\pi/2, \pi)$ where $s < 0$).
>
> **Check.** At $w = \pi i/4$, directly below the edge, $u = 0$ and $\cos2v = 0$, so $s = \sqrt2 - 1 = 0.41421$, $\sqrt{1 - s^2} = 0.91018$, $\tan\pi V = 2.19737$ and $V = 0.36406$. Computing instead $z$ from (6), $z^2 = 1 + e^{-\pi i/2} = 1 - i$, with the root in the upper half plane, $z = 2^{1/4}e^{7\pi i/8} = -1.0987 + 0.4551i$ (and (5) indeed returns $w = \pi i/4$), gives $\theta_1 = 2.92805$, $\theta_2 = 1.78434$ and $V = (\theta_1 - \theta_2)/\pi = 0.36406$.
>
> *B&C: Sec. 133 (text), equations (7)–(8)*

^ex-133-2

![[m342-133-1.svg]]
*Equipotentials $V = 0.1, 0.2, \ldots, 0.9$ between the grounded planes $v = 0$, $v = \pi$ and the plate $v = \pi/2$, $u \ge 0$, at potential $1$ (red). They are the images under (5) of the circular arcs $\theta_1 - \theta_2 = \pi V$ through $z = \pm1$. Far to the right they become parallel to the plates (the field of two parallel-plate capacitors); around the edge they crowd together, which is the strong fringe field at the edge of a plate.*

> [!example] Example §133.3: A Plate at Height hπ
> Generalize Example §133.1: the semi-infinite plate lies along $v = h\pi$, $u \ge 0$ ($0 < h < 1$), between the planes $v = 0$ and $v = \pi$. Obtain formally the mapping function given with B&C's Fig. 22 (Appendix 2),
>
> $$
> w = h\ln\frac{h}{1 - h} + \ln2(1 - h) + i\pi - h\operatorname{Log}(z + 1) - (1 - h)\operatorname{Log}(z - 1), \qquad x_1 = 2h - 1 ,
> $$
>
> where $x_1$ is the prevertex of the edge $h\pi i$.
>
> **Setup.** As in Example §133.1, with the edge's prevertex now called $x_1$ (B&C's figure labels it so) and $\pm1$ for the two vertices at infinity on the right:
>
> $$
> w = \frac A2\big[(1 + x_1)\operatorname{Log}(z + 1) + (1 - x_1)\operatorname{Log}(z - 1)\big] + B .
> $$
>
> **Imaginary parts.** With $A$ real (as before): on $x < -1$ (bottom plate, $v = 0$), $A\pi + B_2 = 0$; on $-1 < x < x_1$ (under side of the plate, $v = h\pi$), $\frac A2(1 - x_1)\pi + B_2 = h\pi$; on $x > 1$ (top plate), $B_2 = \pi$. So $A = -1$, and $-\frac12(1 - x_1)\pi + \pi = h\pi$ gives $x_1 = 2h - 1$. Then
>
> $$
> w = -h\operatorname{Log}(z + 1) - (1 - h)\operatorname{Log}(z - 1) + \pi i + B_1 .
> $$
>
> **Real part.** The edge $w(x_1) = h\pi i$ lies on the $v$ axis. At $x = 2h - 1$, $|x + 1| = 2h$ and $|x - 1| = 2(1 - h)$, and the imaginary part is $-(1 - h)\pi + \pi = h\pi$ as required. The real part vanishes when
>
> $$
> B_1 = h\ln2h + (1 - h)\ln2(1 - h) = h\ln\frac{h}{1 - h} + \ln2(1 - h) ,
> $$
>
> which is the constant in Fig. 22. For $h = \frac12$, $x_1 = 0$ and $B_1 = \frac12\ln1 + \ln1 = 0$, recovering (5).
>
> *B&C: Sec. 133, Exercise 1*

^ex-133-3

> [!example] Example §133.4: Temperatures at a Step
> Let $T(u, v)$ be the bounded steady temperatures in the region above the step of [[§132★ Flow in a Channel with an Offset#^ex-132-4|Example §132.4]] (B&C's Fig. 29), with $T(u, h) = 1$ for $u < 0$ and $T = 0$ on the rest of the boundary (the riser and the positive $u$ axis). Using a parameter $\alpha$, $0 < \alpha < \pi/2$, show that the image of the point $z = i\tan\alpha$ on the positive $y$ axis is
>
> $$
> w = \frac h\pi\Big[\ln(\tan\alpha + \sec\alpha) + i\Big(\frac\pi2 + \sec\alpha\Big)\Big] ,
> $$
>
> and that the temperature there is $T = \alpha/\pi$.
>
> **The temperature in the $z$ plane.** The boundary condition is $T = 1$ on $x < -1$ (the image of the upper bed) and $T = 0$ on $x > -1$. The bounded harmonic function with these values is $T = \frac1\pi\operatorname{Arg}(z + 1)$ ([[§119★ Steady Temperatures in a Half Plane|§119★]]). At $z = i\tan\alpha$, $z + 1 = 1 + i\tan\alpha = \sec\alpha\,e^{i\alpha}$, so $T = \alpha/\pi$.
>
> **The image point.** With $0 \le \arg(z \pm 1) \le \pi$: $z + 1 = \sec\alpha\,e^{i\alpha}$ and $z - 1 = -1 + i\tan\alpha = \sec\alpha\,e^{i(\pi - \alpha)}$, so
>
> $$
> (z + 1)^{1/2}(z - 1)^{1/2} = \sec\alpha\,e^{i(\alpha + \pi - \alpha)/2} = i\sec\alpha ,
> $$
>
> $z + (z + 1)^{1/2}(z - 1)^{1/2} = i(\tan\alpha + \sec\alpha)$, and $\operatorname{Log}$ of this is $\ln(\tan\alpha + \sec\alpha) + \frac{\pi i}{2}$. Substituting into the map of Example §132.4,
>
> $$
> w = \frac h\pi\Big[i\sec\alpha + \ln(\tan\alpha + \sec\alpha) + \frac{\pi i}{2}\Big] ,
> $$
>
> which is the stated point. As $\alpha$ runs from $0$ to $\pi/2$, this image of the $y$ axis runs from $w = \big(\frac12 + \frac1\pi\big)hi$ on the riser (where $T = 0$) up and to the right to infinity, and along it $T = \alpha/\pi$ rises from $0$ toward $\frac12$.
>
> *B&C: Sec. 133, Exercise 4*

^ex-133-4
