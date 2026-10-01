---
type: section
subject: "[[Calculus]]"
chapter: 15
section: 104
stewart: "15.7"
aliases: ["Stewart 15.7"]
tags: [calculus, math233]
---
← [[§103 Triple Integrals]] · ↑ [[· 15 Multiple Integrals]] · [[§105 Triple Integrals in Spherical Coordinates]] →

*Stewart, Section 15.7 · MATH 233 (UMass, Spring 2023): Chapter 15 Review (Q8), Exam 2 Practice Questions (Q18), Practice Final Set 1 (Part I, Q1).*

Cylindrical coordinates are polar coordinates in the $xy$-plane with the height $z$ kept as it is. They fit solids with symmetry about the $z$-axis: cylinders $x^2 + y^2 = c^2$ become $r = c$, cones and paraboloids around the $z$-axis become $z = r$ and $z = r^2$. A triple integral over a type 1 solid whose projection is a polar region is converted by integrating in $z$ first and then using polar coordinates for the double integral, which replaces $dV$ by $r\,dz\,dr\,d\theta$. This is most useful when the integrand involves $x^2 + y^2$.

## Cylindrical Coordinates

> [!definition] Definition §104.1: Cylindrical Coordinates
> In the **cylindrical coordinate system**, a point $P$ in three-dimensional space is represented by the ordered triple $(r, \theta, z)$, where $r$ and $\theta$ are polar coordinates of the projection of $P$ onto the $xy$-plane and $z$ is the directed distance from the $xy$-plane to $P$. To convert from cylindrical to rectangular coordinates,
>
> $$
> x = r\cos\theta , \qquad y = r\sin\theta , \qquad z = z , \qquad (1)
> $$
>
> and from rectangular to cylindrical coordinates,
>
> $$
> r^2 = x^2 + y^2 , \qquad \tan\theta = \frac{y}{x} , \qquad z = z . \qquad (2)
> $$
>
> *Stewart: 15.7, Equations 1 and 2*

^def-104-1

![[m233-104-1.svg]]
*The cylindrical coordinates of a point $P$: polar coordinates $(r, \theta)$ of its projection $(r, \theta, 0)$ onto the $xy$-plane (red), together with its height $z$. The point lies on the cylinder $r = \text{const}$ (blue) about the $z$-axis, on the vertical half-plane $\theta = \text{const}$, and on the horizontal plane $z = \text{const}$.*

As with polar coordinates ([[§65 Polar Coordinates|§65]]), $\theta$ is determined only up to multiples of $2\pi$, and the quadrant of $(x, y)$ must be used to choose $\theta$ from $\tan\theta = y/x$.

The axis of the circular cylinder $x^2 + y^2 = c^2$ is the $z$-axis, and in cylindrical coordinates the cylinder has the very simple equation $r = c$; this is the reason for the name. The graph of $\theta = c$ is a vertical plane through the origin (a half-plane if $r \ge 0$), and the graph of $z = c$ is a horizontal plane.

> [!example] Example §104.1: Converting Points
> **(a)** Plot the point with cylindrical coordinates $(2, 2\pi/3, 1)$ and find its rectangular coordinates.
>
> By Equations 1,
>
> $$
> x = 2\cos\frac{2\pi}{3} = 2\Big(-\frac12\Big) = -1 , \qquad y = 2\sin\frac{2\pi}{3} = 2\Big(\frac{\sqrt3}{2}\Big) = \sqrt3 , \qquad z = 1 ,
> $$
>
> so the point is $(-1, \sqrt3, 1)$: one unit above the point of the $xy$-plane at distance $2$ from the origin in the direction $\theta = 120^\circ$.
>
> **(b)** Find cylindrical coordinates of the point with rectangular coordinates $(3, -3, -7)$.
>
> By Equations 2, $r = \sqrt{3^2 + (-3)^2} = 3\sqrt2$ and $\tan\theta = \frac{-3}{3} = -1$. Since $(3, -3)$ is in quadrant IV of the $xy$-plane, $\theta = \frac{7\pi}{4} + 2n\pi$; and $z = -7$. So one set of cylindrical coordinates is $(3\sqrt2, 7\pi/4, -7)$, another is $(3\sqrt2, -\pi/4, -7)$; as with polar coordinates there are infinitely many choices.
>
> *Stewart: Example 15.7.1*

^ex-104-1

> [!example] Example §104.2: The Surfaces z = r and z = 4r
> **(a)** Describe the surface whose equation in cylindrical coordinates is $z = r$.
>
> The height of each point equals its distance from the $z$-axis. Since $\theta$ does not appear, it can vary, so every horizontal trace in a plane $z = k$ ($k > 0$) is a circle of radius $k$: the surface is a cone. Indeed, from Equations 2, $z^2 = r^2 = x^2 + y^2$, which is a circular cone with axis the $z$-axis ([[§85 Cylinders and Quadric Surfaces|§85]]).
>
> **(b)** Describe the surface whose equation in cylindrical coordinates is $z = 4r$.
>
> The level sets $z = c$ are the circles $r = c/4$ centered on the $z$-axis, so again a cone with vertical axis, now steeper: $z^2 = 16(x^2 + y^2)$. Since $r \ge 0$ forces $z \ge 0$, the equation $z = 4r$ gives only the upper half of this double cone, $z = 4\sqrt{x^2 + y^2}$: a **half-cone** with vertical axis. In spherical coordinates ([[§105 Triple Integrals in Spherical Coordinates|§105]]) it is $\rho\cos\phi = 4\rho\sin\phi$, i.e. $\phi = \operatorname{arccot} 4$.
>
> *The same remark applies to (a): with $r \ge 0$, $z = r$ is the upper half $z = \sqrt{x^2 + y^2}$ of the cone $z^2 = x^2 + y^2$, although Stewart's Figure 15.7.7 shows both halves (the full double cone corresponds to allowing negative $r$).*
>
> *Stewart: Example 15.7.2*
> *Source: 233 Practice Final Set 1, Part I Q1*

^ex-104-2

## Triple Integrals in Cylindrical Coordinates

> [!theorem] Theorem §104.1: Triple Integration in Cylindrical Coordinates
> Suppose that $E$ is a type 1 region whose projection $D$ onto the $xy$-plane is conveniently described in polar coordinates, and $f$ is continuous on $E$:
>
> $$
> E = \{(x, y, z) \mid (x, y) \in D,\ u_1(x, y) \le z \le u_2(x, y)\} , \qquad D = \{(r, \theta) \mid \alpha \le \theta \le \beta,\ h_1(\theta) \le r \le h_2(\theta)\} .
> $$
>
> Then
>
> $$
> \iiint_E f(x, y, z)\,dV = \int_\alpha^\beta \int_{h_1(\theta)}^{h_2(\theta)} \int_{u_1(r\cos\theta,\, r\sin\theta)}^{u_2(r\cos\theta,\, r\sin\theta)} f(r\cos\theta, r\sin\theta, z)\,r\,dz\,dr\,d\theta . \qquad (4)
> $$
>
> *Stewart: 15.7, Formula 4*

^thm-104-1

> [!proof]+ Proof
> By Equation 15.6.6 ([[§103 Triple Integrals#^thm-103-2|Theorem §103.2]]),
>
> $$
> \iiint_E f(x, y, z)\,dV = \iint_D \left[ \int_{u_1(x, y)}^{u_2(x, y)} f(x, y, z)\,dz \right] dA . \qquad (3)
> $$
>
> The function $G(x, y) = \int_{u_1(x, y)}^{u_2(x, y)} f(x, y, z)\,dz$ is a function of $(x, y)$ on the polar region $D$, so by Formula 15.3.3 ([[§100 Double Integrals in Polar Coordinates#^thm-100-2|Theorem §100.2]])
>
> $$
> \iint_D G(x, y)\,dA = \int_\alpha^\beta \int_{h_1(\theta)}^{h_2(\theta)} G(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta ,
> $$
>
> and $G(r\cos\theta, r\sin\theta)\,r = \int_{u_1(r\cos\theta, r\sin\theta)}^{u_2(r\cos\theta, r\sin\theta)} f(r\cos\theta, r\sin\theta, z)\,r\,dz$, which is Formula 4. (Theorem §100.2 was proved for continuous integrands; $G$ is continuous when $f$, $u_1$, $u_2$ are, by the continuity of an integral in its parameter and limits, which Stewart uses without comment.)

^pf-104-1

*Uses:* [[§103 Triple Integrals#^thm-103-2|§103.2]], [[§100 Double Integrals in Polar Coordinates#^thm-100-2|§100.2]], [[§104 Triple Integrals in Cylindrical Coordinates#^def-104-1|Def. §104.1]]

> [!remark] Remark: Method — Using Cylindrical Coordinates
> Formula 4 says: write $x = r\cos\theta$, $y = r\sin\theta$, leave $z$ as it is, use the appropriate limits for $z$, $r$ and $\theta$, and replace $dV$ by $r\,dz\,dr\,d\theta$. A way to remember it: the small cylindrical "box" with sides $dr$, $r\,d\theta$ and $dz$ has volume $dV = r\,dz\,dr\,d\theta$.
> 1. Use cylindrical coordinates when $E$ is easily described in them (symmetry about the $z$-axis: cylinders, cones and paraboloids with vertical axis), and especially when $f(x, y, z)$ involves $x^2 + y^2 = r^2$.
> 2. Find the top and bottom surfaces of $E$ and write them as $z = u(r, \theta)$: these are the $z$-limits.
> 3. Find the projection $D$ (often where two surfaces meet, or the shadow of a cylinder) and describe it by limits for $r$ and $\theta$.
> 4. Don't forget the factor $r$.

^rem-104-1

> [!remark]- Connections
> - Rigorous treatment: the volume element $r\,dr\,d\theta\,dz$ is the absolute value of the Jacobian of $(r, \theta, z) \mapsto (r\cos\theta, r\sin\theta, z)$, and Formula 4 is the change of variables theorem [[§15 Multivariable Integration#^thm-15-20|452 Thm. §15.20]] (see [[§15 Multivariable Integration#^rem-15-5|452 Remark: Notation]] for the volume elements; the calculus version is [[§106 Change of Variables in Multiple Integrals|§106]]).

> [!example] Example §104.3: Under a Paraboloid
> Evaluate $\displaystyle\iiint_E x^2\,dV$, where $E$ is the solid that lies under the paraboloid $z = 4 - x^2 - y^2$ and above the $xy$-plane.
>
> $E$ is symmetric about the $z$-axis and the paraboloid is $z = 4 - r^2$ in cylindrical coordinates. It meets the $xy$-plane in the circle $r^2 = 4$, so $r = 2$, and the projection of $E$ is the disk $r \le 2$:
>
> $$
> E = \{(r, \theta, z) \mid 0 \le \theta \le 2\pi,\ 0 \le r \le 2,\ 0 \le z \le 4 - r^2\} .
> $$
>
> By Formula 4,
>
> $$
> \begin{aligned}
> \iiint_E x^2\,dV &= \int_0^{2\pi} \int_0^2 \int_0^{4 - r^2} (r\cos\theta)^2\,r\,dz\,dr\,d\theta = \int_0^{2\pi} \int_0^2 (r^3\cos^2\theta)(4 - r^2)\,dr\,d\theta \\
> &= \int_0^{2\pi} \cos^2\theta\,d\theta \int_0^2 (4r^3 - r^5)\,dr = \tfrac12 \Big[ \theta + \tfrac12 \sin 2\theta \Big]_0^{2\pi} \Big[ r^4 - \tfrac16 r^6 \Big]_0^2 = \tfrac12 (2\pi)\Big( 16 - \frac{32}{3} \Big) = \frac{16\pi}{3} .
> \end{aligned}
> $$
>
> The iterated integral sweeps out $E$ as follows: $z$ runs from $0$ to $4 - r^2$ with $r$, $\theta$ fixed (a vertical segment), then $r$ from $0$ to $2$ with $\theta$ fixed (a vertical half-plane slice), then $\theta$ from $0$ to $2\pi$.
>
> *Stewart: Example 15.7.3*

^ex-104-3

> [!example] Example §104.4: Mass of a Half-Cylinder Solid
> A solid $E$ lies within the cylinder $x^2 + y^2 = 1$, to the right of the $xz$-plane, below the plane $z = 4$ and above the paraboloid $z = 1 - x^2 - y^2$. The density at any point is proportional to its distance from the axis of the cylinder. Find the mass of $E$.
>
> In cylindrical coordinates the cylinder is $r = 1$ and the paraboloid is $z = 1 - r^2$; "to the right of the $xz$-plane" means $y \ge 0$, that is, $0 \le \theta \le \pi$:
>
> $$
> E = \{(r, \theta, z) \mid 0 \le \theta \le \pi,\ 0 \le r \le 1,\ 1 - r^2 \le z \le 4\} .
> $$
>
> The density is $\rho(x, y, z) = K\sqrt{x^2 + y^2} = Kr$ for a constant $K$. By Formula 15.6.13 ([[§103 Triple Integrals#^def-103-5|Definition §103.5]]),
>
> $$
> \begin{aligned}
> m &= \iiint_E K\sqrt{x^2 + y^2}\,dV = \int_0^{\pi} \int_0^1 \int_{1 - r^2}^{4} (Kr)\,r\,dz\,dr\,d\theta = \int_0^{\pi} \int_0^1 Kr^2\big[ 4 - (1 - r^2) \big]\,dr\,d\theta \\
> &= K\int_0^{\pi} d\theta \int_0^1 (3r^2 + r^4)\,dr = \pi K\Big[ r^3 + \frac{r^5}{5} \Big]_0^1 = \frac{6\pi K}{5} .
> \end{aligned}
> $$
>
> *Stewart: Example 15.7.4*

^ex-104-4

> [!example] Example §104.5: Converting an Iterated Integral
> Evaluate $\displaystyle\int_{-2}^{2} \int_{-\sqrt{4 - x^2}}^{\sqrt{4 - x^2}} \int_{\sqrt{x^2 + y^2}}^{2} (x^2 + y^2)\,dz\,dy\,dx$.
>
> The iterated integral is a triple integral over
>
> $$
> E = \Big\{(x, y, z) \;\Big|\; -2 \le x \le 2,\ -\sqrt{4 - x^2} \le y \le \sqrt{4 - x^2},\ \sqrt{x^2 + y^2} \le z \le 2\Big\} .
> $$
>
> Its projection onto the $xy$-plane is the disk $x^2 + y^2 \le 4$; its lower surface is the cone $z = \sqrt{x^2 + y^2}$ and its upper surface the plane $z = 2$. In cylindrical coordinates $E = \{0 \le \theta \le 2\pi,\ 0 \le r \le 2,\ r \le z \le 2\}$, so
>
> $$
> \int_{-2}^{2} \int_{-\sqrt{4 - x^2}}^{\sqrt{4 - x^2}} \int_{\sqrt{x^2 + y^2}}^{2} (x^2 + y^2)\,dz\,dy\,dx = \int_0^{2\pi} \int_0^2 \int_r^2 r^2 \cdot r\,dz\,dr\,d\theta = \int_0^{2\pi} d\theta \int_0^2 r^3(2 - r)\,dr = 2\pi\Big[ \tfrac12 r^4 - \tfrac15 r^5 \Big]_0^2 = \frac{16\pi}{5} .
> $$
>
> *Stewart: Example 15.7.5*

^ex-104-5

> [!example] Example §104.6: Volume and a Moment for a Paraboloid Bowl
> Let $E$ be the solid bounded by the paraboloid $z = x^2 + y^2$ and the plane $z = 4$. Use cylindrical coordinates to find **(a)** its volume and **(b)** $\iiint_E z\,dV$.
>
> The paraboloid is $z = r^2$; it meets $z = 4$ where $r = 2$. So $E = \{0 \le \theta \le 2\pi,\ 0 \le r \le 2,\ r^2 \le z \le 4\}$.
>
> **(a)**
>
> $$
> V = \int_0^{2\pi} \int_0^2 \int_{r^2}^{4} r\,dz\,dr\,d\theta = 2\pi\int_0^2 (4 - r^2)\,r\,dr = 2\pi\Big[ 2r^2 - \frac{r^4}{4} \Big]_0^2 = 2\pi(8 - 4) = 8\pi .
> $$
>
> **(b)**
>
> $$
> \iiint_E z\,dV = \int_0^{2\pi} \int_0^2 \int_{r^2}^{4} z\,r\,dz\,dr\,d\theta = 2\pi\int_0^2 \tfrac12 (16 - r^4)\,r\,dr = \pi\Big[ 8r^2 - \frac{r^6}{6} \Big]_0^2 = \pi\Big( 32 - \frac{32}{3} \Big) = \frac{64\pi}{3} .
> $$
>
> Together: the centroid of the bowl is on the $z$-axis at height $\bar z = \frac{64\pi/3}{8\pi} = \frac83$, above the midpoint $z = 2$ because the bowl is wider at the top.
>
> *Source: 233 Exam 2 Practice Questions, Q18 (a), and Chapter 15 Review, Q8 (b)*

^ex-104-6
