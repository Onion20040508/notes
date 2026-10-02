---
type: section
subject: "[[Calculus]]"
chapter: 15
section: 105
stewart: "15.8"
aliases: ["Stewart 15.8"]
tags: [calculus, math233]
---
← [[§104 Triple Integrals in Cylindrical Coordinates]] · ↑ [[· 15 Multiple Integrals]] · [[§106 Change of Variables in Multiple Integrals]] →

*Stewart, Section 15.8 · MATH 233 (UMass, Spring 2023): Exam 2 Practice Questions (Q19, Q20), Chapter 15 Review (Q11), Practice Final Exam (Q4).*

Spherical coordinates describe a point by its distance $\rho$ from the origin and two angles: the polar angle $\theta$ of cylindrical coordinates and the angle $\phi$ down from the positive $z$-axis. Spheres centered at the origin become $\rho = c$ and cones around the $z$-axis become $\phi = c$, so solids bounded by spheres and cones become boxes in $(\rho, \theta, \phi)$. The volume of a small spherical wedge is about $\rho^2\sin\phi\,\Delta\rho\,\Delta\theta\,\Delta\phi$, which turns into the rule: replace $dV$ by $\rho^2\sin\phi\,d\rho\,d\theta\,d\phi$.

## Spherical Coordinates

> [!definition] Definition §105.1: Spherical Coordinates
> The **spherical coordinates** $(\rho, \theta, \phi)$ of a point $P$ in space are: $\rho = |OP|$, the distance from the origin to $P$; $\theta$, the same angle as in cylindrical coordinates ([[§104 Triple Integrals in Cylindrical Coordinates#^def-104-1|Definition §104.1]]); and $\phi$, the angle between the positive $z$-axis and the line segment $OP$. Note that
>
> $$
> \rho \ge 0 , \qquad 0 \le \phi \le \pi .
> $$
>
> From the right triangles $OPQ$ and $OPP'$ ($Q$ on the $z$-axis, $P'$ the projection of $P$ onto the $xy$-plane), $z = \rho\cos\phi$ and $r = \rho\sin\phi$, and since $x = r\cos\theta$, $y = r\sin\theta$, the conversion to rectangular coordinates is
>
> $$
> x = \rho\sin\phi\cos\theta , \qquad y = \rho\sin\phi\sin\theta , \qquad z = \rho\cos\phi . \qquad (1)
> $$
>
> The distance formula gives, for the conversion from rectangular coordinates,
>
> $$
> \rho^2 = x^2 + y^2 + z^2 . \qquad (2)
> $$
>
> *Stewart: 15.8, Equations 1 and 2*

^def-105-1

![[m233-105-1.svg]]
*The spherical coordinates of $P$: its distance $\rho$ from the origin, the angle $\phi$ from the positive $z$-axis, and the polar angle $\theta$ of its projection $P'$. The right triangle $OP'P$ shows $r = \rho\sin\phi$ (the distance from the $z$-axis) and $z = \rho\cos\phi$; then $x = r\cos\theta$, $y = r\sin\theta$ give Equations 1.*

> [!remark]- Connections
> - PDE version: [[§49★ Spherical Coordinates; Legendre Polynomials#^prop-49-1|341 Prop. §49.1]] (the Laplacian in the same coordinates $\rho, \theta, \phi$), whose separation leads to Legendre's equation, [[§49★ Spherical Coordinates; Legendre Polynomials#^prop-49-2|341 Prop. §49.2]].

The system is especially useful where there is symmetry about a point, placed at the origin. The sphere with center the origin and radius $c$ is $\rho = c$ (hence the name). The graph of $\theta = c$ is a vertical half-plane, and $\phi = c$ is a half-cone with the $z$-axis as its axis: opening upward if $0 < c < \pi/2$, downward if $\pi/2 < c < \pi$ (and $\phi = \pi/2$ is the $xy$-plane).

> [!remark] Remark: Warning on Notation
> There is no universal agreement on the notation for spherical coordinates. Most books on physics reverse the meanings of $\theta$ and $\phi$ and use $r$ in place of $\rho$.

^rem-105-1

> [!example] Example §105.1: Converting Points
> **(a)** The point $(2, \pi/4, \pi/3)$ is given in spherical coordinates. Find its rectangular coordinates.
>
> Here $\rho = 2$, $\theta = \pi/4$, $\phi = \pi/3$. By Equations 1,
>
> $$
> x = 2\sin\frac{\pi}{3}\cos\frac{\pi}{4} = 2\Big(\frac{\sqrt3}{2}\Big)\Big(\frac{1}{\sqrt2}\Big) = \sqrt{\frac32} , \qquad
> y = 2\sin\frac{\pi}{3}\sin\frac{\pi}{4} = \sqrt{\frac32} , \qquad
> z = 2\cos\frac{\pi}{3} = 2\Big(\frac12\Big) = 1 ,
> $$
>
> so the point is $\big(\sqrt{3/2}, \sqrt{3/2}, 1\big)$.
>
> **(b)** The point $(0, 2\sqrt3, -2)$ is given in rectangular coordinates. Find spherical coordinates for it.
>
> By Equation 2, $\rho = \sqrt{0 + 12 + 4} = 4$. Then Equations 1 give
>
> $$
> \cos\phi = \frac{z}{\rho} = \frac{-2}{4} = -\frac12 , \quad \phi = \frac{2\pi}{3} ; \qquad \cos\theta = \frac{x}{\rho\sin\phi} = 0 , \quad \theta = \frac{\pi}{2}
> $$
>
> ($\theta \ne 3\pi/2$ because $y = 2\sqrt3 > 0$). So the spherical coordinates are $(4, \pi/2, 2\pi/3)$. Unlike $\theta$, the angle $\phi$ is found from $\cos\phi = z/\rho$ without ambiguity, since $0 \le \phi \le \pi$.
>
> *Stewart: Examples 15.8.1 and 15.8.2*

^ex-105-1

## Triple Integrals in Spherical Coordinates

> [!definition] Definition §105.2: Spherical Wedge
> The counterpart of a rectangular box in spherical coordinates is a **spherical wedge**
>
> $$
> E = \{(\rho, \theta, \phi) \mid a \le \rho \le b,\ \alpha \le \theta \le \beta,\ c \le \phi \le d\} ,
> $$
>
> where $a \ge 0$, $\beta - \alpha \le 2\pi$ and $d - c \le \pi$. It is divided into smaller spherical wedges $E_{ijk}$ by equally spaced spheres $\rho = \rho_i$, half-planes $\theta = \theta_j$ and half-cones $\phi = \phi_k$.
>
> *Stewart: 15.8 (text)*

^def-105-2

$E_{ijk}$ is approximately a rectangular box with dimensions $\Delta\rho$, $\rho_i\,\Delta\phi$ (an arc of a circle of radius $\rho_i$ with angle $\Delta\phi$) and $\rho_i\sin\phi_k\,\Delta\theta$ (an arc of a circle of radius $\rho_i\sin\phi_k$, the distance from the $z$-axis, with angle $\Delta\theta$). So

$$
\Delta V_{ijk} \approx (\Delta\rho)(\rho_i\,\Delta\phi)(\rho_i\sin\phi_k\,\Delta\theta) = \rho_i^2\sin\phi_k\,\Delta\rho\,\Delta\theta\,\Delta\phi .
$$

The next lemma makes this exact.

> [!theorem] Lemma §105.1: The Volume of a Spherical Wedge
> The volume of the spherical wedge $\rho_1 \le \rho \le \rho_2$, $\theta_1 \le \theta \le \theta_2$, $\phi_1 \le \phi \le \phi_2$ is
>
> $$
> \Delta V = \frac{\rho_2^3 - \rho_1^3}{3}\,(\cos\phi_1 - \cos\phi_2)(\theta_2 - \theta_1) ,
> $$
>
> and there are $\tilde\rho$ between $\rho_1$ and $\rho_2$ and $\tilde\phi$ between $\phi_1$ and $\phi_2$ with
>
> $$
> \Delta V = \tilde\rho^{\,2}\sin\tilde\phi\,\Delta\rho\,\Delta\theta\,\Delta\phi , \qquad \Delta\rho = \rho_2 - \rho_1,\ \Delta\theta = \theta_2 - \theta_1,\ \Delta\phi = \phi_2 - \phi_1 .
> $$
>
> *Stewart: 15.8, Exercise 51 (used in the text)*

^lem-105-1

> [!proof]+ Proof
> *Stewart states this "with the aid of the Mean Value Theorem (Exercise 51)"; here is that exercise worked out.*
>
> **Step 1: an ice-cream-cone solid.** Let $0 < \phi_0 < \pi/2$ and let $W(a, \phi_0)$ be the solid $\rho \le a$, $0 \le \phi \le \phi_0$, $\theta_1 \le \theta \le \theta_2$: above the cone $z = r\cot\phi_0$ and below the sphere $r^2 + z^2 = a^2$. They meet where $r = a\sin\phi_0$. In cylindrical coordinates ([[§104 Triple Integrals in Cylindrical Coordinates#^thm-104-1|Theorem §104.1]]),
>
> $$
> \begin{aligned}
> V\big(W(a, \phi_0)\big) &= \int_{\theta_1}^{\theta_2} \int_0^{a\sin\phi_0} \big( \sqrt{a^2 - r^2} - r\cot\phi_0 \big)\,r\,dr\,d\theta = (\theta_2 - \theta_1)\Big[ -\tfrac13 (a^2 - r^2)^{3/2} - \tfrac13 r^3\cot\phi_0 \Big]_0^{a\sin\phi_0} \\
> &= (\theta_2 - \theta_1)\,\frac{a^3}{3}\big[ 1 - \cos^3\phi_0 - \sin^2\phi_0\cos\phi_0 \big] = (\theta_2 - \theta_1)\,\frac{a^3}{3}(1 - \cos\phi_0) .
> \end{aligned}
> $$
>
> The same formula holds for $\phi_0 = \pi/2$: the solid is then the part of the ball sector above the $xy$-plane, with volume $\int_{\theta_1}^{\theta_2} \int_0^a \sqrt{a^2 - r^2}\,r\,dr\,d\theta = (\theta_2 - \theta_1)\frac{a^3}{3}$. Reflection in the $xy$-plane preserves volume, so the whole sector $0 \le \phi \le \pi$ has volume $(\theta_2 - \theta_1)\frac{2a^3}{3}$. For $\pi/2 < \phi_0 \le \pi$, the solid $W(a, \phi_0)$ is the whole sector minus the part $\phi_0 < \phi \le \pi$, and that part is the mirror image of $W(a, \pi - \phi_0)$. Hence
>
> $$
> V\big(W(a, \phi_0)\big) = (\theta_2 - \theta_1)\frac{a^3}{3}\big[ 2 - \big(1 - \cos(\pi - \phi_0)\big) \big] = (\theta_2 - \theta_1)\frac{a^3}{3}(1 - \cos\phi_0)
> $$
>
> for every $0 \le \phi_0 \le \pi$.
>
> **Step 2: the wedge.** The wedge is $W(\rho_2, \phi_2)$ with $W(\rho_2, \phi_1)$, $W(\rho_1, \phi_2)$ removed and $W(\rho_1, \phi_1)$ put back, so by Step 1
>
> $$
> \Delta V = \frac{\theta_2 - \theta_1}{3}\Big[ \rho_2^3(\cos\phi_1 - \cos\phi_2) - \rho_1^3(\cos\phi_1 - \cos\phi_2) \Big] = \frac{\rho_2^3 - \rho_1^3}{3}(\cos\phi_1 - \cos\phi_2)(\theta_2 - \theta_1) .
> $$
>
> **Step 3: the Mean Value Theorem** ([[§26 The Mean Value Theorem#^thm-26-2|Theorem §26.2]]) applied to $\rho^3/3$ on $[\rho_1, \rho_2]$ and to $-\cos\phi$ on $[\phi_1, \phi_2]$ gives $\tilde\rho$, $\tilde\phi$ with $\frac{\rho_2^3 - \rho_1^3}{3} = \tilde\rho^{\,2}\,\Delta\rho$ and $\cos\phi_1 - \cos\phi_2 = \sin\tilde\phi\,\Delta\phi$.

^pf-105-1

*Uses:* [[§104 Triple Integrals in Cylindrical Coordinates#^thm-104-1|§104.1]], [[§103 Triple Integrals#^thm-103-4|§103.4]], [[§26 The Mean Value Theorem#^thm-26-2|§26.2]]

> [!theorem] Theorem §105.2: Triple Integration in Spherical Coordinates
> If $f$ is continuous on the spherical wedge $E = \{(\rho, \theta, \phi) \mid a \le \rho \le b,\ \alpha \le \theta \le \beta,\ c \le \phi \le d\}$, then
>
> $$
> \iiint_E f(x, y, z)\,dV = \int_c^d \int_\alpha^\beta \int_a^b f(\rho\sin\phi\cos\theta, \rho\sin\phi\sin\theta, \rho\cos\phi)\,\rho^2\sin\phi\,d\rho\,d\theta\,d\phi . \qquad (3)
> $$
>
> More generally, for a region $E = \{(\rho, \theta, \phi) \mid \alpha \le \theta \le \beta,\ c \le \phi \le d,\ g_1(\theta, \phi) \le \rho \le g_2(\theta, \phi)\}$ the formula is the same except that the limits of integration for $\rho$ are $g_1(\theta, \phi)$ and $g_2(\theta, \phi)$.
>
> *Stewart: 15.8, Formula 3*

^thm-105-2

> [!proof]+ Proof
> *Stewart gives this as a sketch.* Although triple integrals were defined by dividing solids into small boxes, dividing a solid into small spherical wedges always gives the same result (Stewart asserts this: "it can be shown"). Divide $E$ into the wedges $E_{ijk}$ of Definition §105.2. By Lemma §105.1, $\Delta V_{ijk} = \tilde\rho_i^{\,2}\sin\tilde\phi_k\,\Delta\rho\,\Delta\theta\,\Delta\phi$ for some point $(\tilde\rho_i, \tilde\theta_j, \tilde\phi_k)$ of $E_{ijk}$ (any $\tilde\theta_j$ in the $\theta$-interval will do). Let $(x_{ijk}^*, y_{ijk}^*, z_{ijk}^*)$ be the rectangular coordinates of this point. Then
>
> $$
> \begin{aligned}
> \iiint_E f(x, y, z)\,dV &= \lim_{l, m, n \to \infty} \sum_{i=1}^l \sum_{j=1}^m \sum_{k=1}^n f(x_{ijk}^*, y_{ijk}^*, z_{ijk}^*)\,\Delta V_{ijk} \\
> &= \lim_{l, m, n \to \infty} \sum_{i=1}^l \sum_{j=1}^m \sum_{k=1}^n f(\tilde\rho_i\sin\tilde\phi_k\cos\tilde\theta_j, \tilde\rho_i\sin\tilde\phi_k\sin\tilde\theta_j, \tilde\rho_i\cos\tilde\phi_k)\,\tilde\rho_i^{\,2}\sin\tilde\phi_k\,\Delta\rho\,\Delta\theta\,\Delta\phi .
> \end{aligned}
> $$
>
> The last sum is a triple Riemann sum ([[§103 Triple Integrals#^def-103-1|Definition §103.1]]) over the box $[a, b] \times [\alpha, \beta] \times [c, d]$ in $\rho\theta\phi$-space for the continuous function
>
> $$
> F(\rho, \theta, \phi) = f(\rho\sin\phi\cos\theta, \rho\sin\phi\sin\theta, \rho\cos\phi)\,\rho^2\sin\phi ,
> $$
>
> so its limit is $\iiint F\,d\rho\,d\theta\,d\phi$, which is the iterated integral (3) by Fubini's Theorem ([[§103 Triple Integrals#^thm-103-1|Theorem §103.1]]). The general region follows by extending $f$ by $0$ to a wedge containing $E$, exactly as in the proof of [[§100 Double Integrals in Polar Coordinates#^thm-100-2|Theorem §100.2]].

^pf-105-2

*Uses:* [[§105 Triple Integrals in Spherical Coordinates#^def-105-2|Def. §105.2]], [[§105 Triple Integrals in Spherical Coordinates#^lem-105-1|§105.1]], [[§103 Triple Integrals#^def-103-1|Def. §103.1]], [[§103 Triple Integrals#^thm-103-1|§103.1]], [[§100 Double Integrals in Polar Coordinates#^thm-100-2|§100.2]]

> [!remark]- Connections
> - Rigorous treatment: $\rho^2\sin\phi$ is the absolute value of the Jacobian of the spherical-coordinate map ([[§15 Multivariable Integration#^ex-15-6|452 Ex. §15.6]]; computed in [[§106 Change of Variables in Multiple Integrals#^ex-106-5|Example §106.5]]), and Formula 3 is the change of variables theorem [[§15 Multivariable Integration#^thm-15-20|452 Thm. §15.20]]. Hub: [[Polar and spherical coordinates]].
> - PDE version: the factor $\sin\phi$ of the volume element is the weight in the orthogonality of the $P_n(\cos\phi)$, which appears in the coefficients of the potential in a sphere, [[§50★ Some Applications of Legendre Polynomials#^prop-50-1|341 Prop. §50.1]].

> [!remark] Remark: Method — Using Spherical Coordinates
> Formula 3 says: write $x = \rho\sin\phi\cos\theta$, $y = \rho\sin\phi\sin\theta$, $z = \rho\cos\phi$, use the appropriate limits, and replace $dV$ by $\rho^2\sin\phi\,d\rho\,d\theta\,d\phi$ (the volume of the small wedge with sides $d\rho$, $\rho\,d\phi$, $\rho\sin\phi\,d\theta$).
> 1. Use spherical coordinates when cones and spheres form the boundary of the region, and when the integrand involves $x^2 + y^2 + z^2 = \rho^2$.
> 2. Translate the boundary: a sphere $x^2 + y^2 + z^2 = a^2$ is $\rho = a$; a cone $z = k\sqrt{x^2 + y^2}$ ($k > 0$) is $\cot\phi = k$, a constant $\phi$; the cone $z = -\sqrt{x^2 + y^2}$ is $\phi = 3\pi/4$; a sphere through the origin such as $x^2 + y^2 + z^2 = z$ is $\rho = \cos\phi$.
> 3. Read off the ranges, usually in the order $\rho$ (along a ray from the origin), then $\phi$, then $\theta$.

^rem-105-2

> [!example] Example §105.2: An Integral over the Unit Ball
> Evaluate $\displaystyle\iiint_B e^{(x^2 + y^2 + z^2)^{3/2}}\,dV$, where $B$ is the unit ball $\{(x, y, z) \mid x^2 + y^2 + z^2 \le 1\}$.
>
> The boundary of $B$ is a sphere, and the integrand involves $x^2 + y^2 + z^2 = \rho^2$, so use spherical coordinates: $B = \{0 \le \rho \le 1,\ 0 \le \theta \le 2\pi,\ 0 \le \phi \le \pi\}$. By Formula 3,
>
> $$
> \iiint_B e^{(x^2 + y^2 + z^2)^{3/2}}\,dV = \int_0^{\pi} \int_0^{2\pi} \int_0^1 e^{(\rho^2)^{3/2}}\rho^2\sin\phi\,d\rho\,d\theta\,d\phi = \int_0^{\pi} \sin\phi\,d\phi \int_0^{2\pi} d\theta \int_0^1 \rho^2 e^{\rho^3}\,d\rho = \Big[ -\cos\phi \Big]_0^{\pi} (2\pi) \Big[ \tfrac13 e^{\rho^3} \Big]_0^1 = \frac43 \pi(e - 1) .
> $$
>
> In rectangular coordinates this would have been $\int_{-1}^{1} \int_{-\sqrt{1 - x^2}}^{\sqrt{1 - x^2}} \int_{-\sqrt{1 - x^2 - y^2}}^{\sqrt{1 - x^2 - y^2}} e^{(x^2 + y^2 + z^2)^{3/2}}\,dz\,dy\,dx$, extremely awkward.
>
> *Stewart: Example 15.8.3*

^ex-105-2

> [!example] Example §105.3: The Ice-Cream Cone
> Use spherical coordinates to find the volume of the solid that lies above the cone $z = \sqrt{x^2 + y^2}$ and below the sphere $x^2 + y^2 + z^2 = z$.
>
> **The boundary.** The sphere passes through the origin and has center $(0, 0, \tfrac12)$. In spherical coordinates it is $\rho^2 = \rho\cos\phi$, or $\rho = \cos\phi$. The cone is
>
> $$
> \rho\cos\phi = \sqrt{\rho^2\sin^2\phi\cos^2\theta + \rho^2\sin^2\phi\sin^2\theta} = \rho\sin\phi ,
> $$
>
> so $\sin\phi = \cos\phi$, or $\phi = \pi/4$. The solid is
>
> $$
> E = \{(\rho, \theta, \phi) \mid 0 \le \theta \le 2\pi,\ 0 \le \phi \le \pi/4,\ 0 \le \rho \le \cos\phi\} .
> $$
>
> **The volume.**
>
> $$
> V(E) = \iiint_E dV = \int_0^{2\pi} \int_0^{\pi/4} \int_0^{\cos\phi} \rho^2\sin\phi\,d\rho\,d\phi\,d\theta = \int_0^{2\pi} d\theta \int_0^{\pi/4} \sin\phi \Big[ \frac{\rho^3}{3} \Big]_{\rho=0}^{\rho=\cos\phi} d\phi = \frac{2\pi}{3} \int_0^{\pi/4} \sin\phi\cos^3\phi\,d\phi = \frac{2\pi}{3} \Big[ -\frac{\cos^4\phi}{4} \Big]_0^{\pi/4} = \frac{\pi}{8} .
> $$
>
> The integration sweeps out $E$ as follows: $\rho$ along a ray from $0$ to $\cos\phi$, then $\phi$ from $0$ to $\pi/4$ (a fan in a vertical half-plane), then $\theta$ around the $z$-axis.
>
> *Stewart: Example 15.8.4*

^ex-105-3

![[m233-105-2.svg]]
*Example §105.3 in the cross-section by the $xz$-plane. The sphere $x^2 + y^2 + z^2 = z$ passes through the origin and is $\rho = \cos\phi$: along the ray at angle $\phi$ (red) the solid extends from $\rho = 0$ to the sphere. The cone $z = \sqrt{x^2 + y^2}$ is $\phi = \pi/4$. The rays sweep out the shaded fan for $0 \le \phi \le \pi/4$, and rotation in $\theta$ gives the solid.*

> [!example] Example §105.4: Below a Downward Cone
> Use spherical coordinates to find the volume of the solid that lies below the surface $z = -\sqrt{x^2 + y^2}$ and inside the sphere $x^2 + y^2 + z^2 = 9$.
>
> The surface $z = -\sqrt{x^2 + y^2}$ is the half-cone opening downward: $\rho\cos\phi = -\rho\sin\phi$, so $\tan\phi = -1$ and $\phi = 3\pi/4$. Below it means $3\pi/4 \le \phi \le \pi$ (the angle from the positive $z$-axis is larger below the cone). The sphere is $\rho = 3$. So
>
> $$
> V = \int_0^{2\pi} \int_{3\pi/4}^{\pi} \int_0^3 \rho^2\sin\phi\,d\rho\,d\phi\,d\theta = 2\pi \Big[ -\cos\phi \Big]_{3\pi/4}^{\pi} \Big[ \frac{\rho^3}{3} \Big]_0^3 = 2\pi\Big( 1 - \frac{\sqrt2}{2} \Big)(9) = 9\pi\big( 2 - \sqrt2 \big) .
> $$
>
> The same computation with $0 \le \phi \le \pi/3$ and $\rho \le 4$ gives the volume of the part of the ball $\rho \le 4$ above the cone $\phi = \pi/3$: $2\pi(1 - \tfrac12)\frac{64}{3} = \frac{64\pi}{3}$.
>
> *Source: 233 Exam 2 Practice Questions, Q20 (= Practice Final Exam, Q4), and Q19 for the last line*

^ex-105-4

> [!example] Example §105.5: Converting an Iterated Integral to Spherical Coordinates
> Evaluate $\displaystyle\int_0^1 \int_0^{\sqrt{1 - x^2}} \int_{\sqrt{x^2 + y^2}}^{\sqrt{2 - x^2 - y^2}} xy\,dz\,dy\,dx$ by changing it into spherical coordinates.
>
> **The region.** The outer limits describe the quarter disk $x^2 + y^2 \le 1$, $x, y \ge 0$, so $0 \le \theta \le \pi/2$. The lower surface is the cone $z = \sqrt{x^2 + y^2}$, that is, $\phi = \pi/4$; the upper surface is the sphere $x^2 + y^2 + z^2 = 2$, that is, $\rho = \sqrt2$. (They meet where $x^2 + y^2 = 1$, consistent with the quarter disk.) So the region is $0 \le \rho \le \sqrt2$, $0 \le \phi \le \pi/4$, $0 \le \theta \le \pi/2$.
>
> **The integral.** With $xy = \rho^2\sin^2\phi\cos\theta\sin\theta$ and $dV = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$, the integrand factors:
>
> $$
> \int_0^{\pi/2} \int_0^{\pi/4} \int_0^{\sqrt2} \rho^4\sin^3\phi\cos\theta\sin\theta\,d\rho\,d\phi\,d\theta = \int_0^{\pi/2} \sin\theta\cos\theta\,d\theta \int_0^{\pi/4} \sin^3\phi\,d\phi \int_0^{\sqrt2} \rho^4\,d\rho .
> $$
>
> The three factors are $\big[\tfrac12\sin^2\theta\big]_0^{\pi/2} = \tfrac12$; $\int_0^{\pi/4} (1 - \cos^2\phi)\sin\phi\,d\phi = \big[ -\cos\phi + \tfrac13\cos^3\phi \big]_0^{\pi/4} = \big( -\tfrac{\sqrt2}{2} + \tfrac{\sqrt2}{12} \big) - \big( -1 + \tfrac13 \big) = \frac{8 - 5\sqrt2}{12}$; and $\big[\tfrac15\rho^5\big]_0^{\sqrt2} = \frac{4\sqrt2}{5}$. So the integral is
>
> $$
> \frac12 \cdot \frac{8 - 5\sqrt2}{12} \cdot \frac{4\sqrt2}{5} = \frac{(8 - 5\sqrt2)\sqrt2}{30} = \frac{4\sqrt2 - 5}{15} \approx 0.0438 .
> $$
>
> *The posted solution has the same set-up but takes $\cos\phi + \tfrac13\cos^3\phi$ as the antiderivative of $\sin^3\phi$ (the sign of $\cos\phi$ is lost), so its last line is negative; the integrand $xy$ is nonnegative on the region, and the value is $\frac{4\sqrt2 - 5}{15}$.*
>
> *Source: 233 Chapter 15 Review, Q11*

^ex-105-5
