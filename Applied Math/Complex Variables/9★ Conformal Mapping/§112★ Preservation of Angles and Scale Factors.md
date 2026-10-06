---
type: section
subject: "[[Complex Variables]]"
chapter: 9
section: 112
bc: "112"
aliases: ["B&C 112"]
tags: [complex-variables, math342, extension]
---
← [[§111★ Surfaces for Related Functions]] · ↑ [[· 9★ Conformal Mapping]] · [[§113★ Further Examples (Preservation of Angles and Scale Factors)]] →

*Brown–Churchill, Section 112.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

An analytic function with nonzero derivative turns every curve through a point by the same angle, $\arg f'(z_0)$, and stretches every short segment there by the same factor, $|f'(z_0)|$. Consequently the angle between two curves is preserved in size and in sense: the map is **conformal**. At a critical point, where $f'(z_0) = 0$, angles are instead multiplied by an integer $m \ge 2$. Conformality is what makes analytic maps useful for physics: level curves that cross at right angles (isotherms and heat-flow lines, equipotentials and field lines, streamlines and potential lines) still cross at right angles after the map, so a boundary value problem can be carried to a simpler region and back ([[§116★ Transformations of Harmonic Functions|§116]], [[§117★ Transformations of Boundary Conditions|§117]]).

## Angle of Rotation

Let $C$ be a smooth arc ([[§43 Contours#^def-43-4|Definition §43.4]]), $z = z(t)$ $(a \le t \le b)$, and let $f(z)$ be defined at all points of $C$. Then

$$
w = f[z(t)] \qquad (a \le t \le b)
$$

is a parametric representation of the image $\Gamma$ of $C$ under the transformation $w = f(z)$. Suppose that $C$ passes through a point $z_0 = z(t_0)$ $(a < t_0 < b)$ at which $f$ is analytic and $f'(z_0) \ne 0$. By the chain rule along an arc ([[§43 Contours#^prop-43-5|Proposition §43.5]]), $w(t) = f[z(t)]$ satisfies

$$
w'(t_0) = f'[z(t_0)]\,z'(t_0), \qquad (1)
$$

and so, by the argument of a product ([[§9 Arguments of Products and Quotients#^thm-9-1|Theorem §9.1]]),

$$
\arg w'(t_0) = \arg f'[z(t_0)] + \arg z'(t_0) . \qquad (2)
$$

Since $z'(t_0) \ne 0$ and $f'(z_0) \ne 0$, also $w'(t_0) \ne 0$, so $\Gamma$ has a tangent line at $w_0 = f(z_0)$. By the discussion of unit tangent vectors in [[§43 Contours#^def-43-4|Definition §43.4]], a value $\theta_0$ of $\arg z'(t_0)$ is the angle of inclination of the directed tangent line to $C$ at $z_0$, and a value $\phi_0$ of $\arg w'(t_0)$ is that of the directed tangent line to $\Gamma$ at $w_0$.

> [!definition] Definition §112.1: Angle of Rotation
> If $f$ is analytic at $z_0$ and $f'(z_0) \ne 0$, the **angle of rotation** of the transformation $w = f(z)$ at $z_0$ is
>
> $$
> \psi_0 = \arg f'(z_0) . \qquad (4)
> $$
>
> It is determined up to a multiple of $2\pi$.
>
> *B&C: Sec. 112 (text)*

^def-112-1

> [!theorem] Theorem §112.1: Directions Are Rotated by arg f′(z₀); Angles Are Preserved
> Let $f$ be analytic at $z_0$ with $f'(z_0) \ne 0$.
>
> **(a)** If a smooth arc $C$ through $z_0$ has tangent inclination $\theta_0$ at $z_0$, its image $\Gamma$ has tangent inclination
>
> $$
> \phi_0 = \psi_0 + \theta_0 \qquad (3)
> $$
>
> at $w_0 = f(z_0)$, for a suitable value $\psi_0$ of $\arg f'(z_0)$.
>
> **(b)** If $C_1$ and $C_2$ are smooth arcs through $z_0$, the angle from the image $\Gamma_1$ to the image $\Gamma_2$ at $w_0$ equals the angle from $C_1$ to $C_2$ at $z_0$, in magnitude and in sense:
>
> $$
> \phi_2 - \phi_1 = \theta_2 - \theta_1 .
> $$
>
> *B&C: Sec. 112 (text)*

^thm-112-1

> [!proof]+ Proof
> **(a)** By (2), the number $\phi_0 - \theta_0$, a value of $\arg w'(t_0) - \arg z'(t_0)$, is a value of $\arg f'[z(t_0)] = \arg f'(z_0)$; call it $\psi_0$. Then $\phi_0 = \psi_0 + \theta_0$, which is (3). Geometrically: the directions of $C$ and $\Gamma$ at $z_0$ and $w_0$ differ by the angle of rotation (4) (Fig. 147 in B&C).
>
> **(b)** Let $\theta_1, \theta_2$ be inclinations of the directed tangent lines to $C_1, C_2$ at $z_0$. The number $\psi_0$ in (a) depends only on $f$ and $z_0$, not on the arc, so by (a)
>
> $$
> \phi_1 = \psi_0 + \theta_1 \qquad\text{and}\qquad \phi_2 = \psi_0 + \theta_2
> $$
>
> are inclinations of the directed tangent lines to $\Gamma_1$ and $\Gamma_2$ at $w_0$. Subtracting, $\phi_2 - \phi_1 = \theta_2 - \theta_1$: the angle from $\Gamma_1$ to $\Gamma_2$ is the angle $\alpha$ from $C_1$ to $C_2$, with the same sign.

^pf-112-1

*Uses:* [[§112★ Preservation of Angles and Scale Factors#^def-112-1|Def. §112.1]], [[§43 Contours#^def-43-4|Def. §43.4]] (smooth arcs, unit tangent), [[§43 Contours#^prop-43-5|§43.5]] (chain rule), [[§9 Arguments of Products and Quotients#^thm-9-1|§9.1]] ($\arg(z_1z_2) = \arg z_1 + \arg z_2$)

> [!remark]- Connections
> - Why it works, in matrix form: by the [[§21 Cauchy–Riemann Equations#^def-21-1|Cauchy–Riemann equations]] the Jacobian matrix of $(x, y) \mapsto (u, v)$ at $z_0$ is $\begin{bmatrix} u_x & -v_x \\ v_x & u_x \end{bmatrix}$ with $u_x + iv_x = f'(z_0)$, a rotation–scaling matrix: rotation through $\arg f'(z_0)$ followed by scaling by $|f'(z_0)|$, [[§36 Complex Eigenvalues#^prop-36-3|235 Prop. §36.3]]. A linear map of that form preserves angles; the tangent vector $z'(t_0)$ is carried to $w'(t_0)$ by this matrix ([[§13 The Inverse Function Theorem#^def-13-1|452 Def. §13.1]], the Jacobian).
> - Used in Electromagnetism: analytic maps carry electrostatic solutions to solutions, field lines staying perpendicular to equipotentials — [[§C6.4★ The Complex Potential and the Variational Principle#^thm-c6-4-2|EM Theorem §C6.4.2]].

Because of this angle-preserving property, the following terms are used.

> [!definition] Definition §112.2: Conformal Mapping
> A transformation $w = f(z)$ is **conformal at a point** $z_0$ if $f$ is analytic at $z_0$ and $f'(z_0) \ne 0$. A transformation defined on a domain $D$ is a **conformal transformation**, or **conformal mapping**, of $D$ if it is conformal at each point of $D$; that is, if $f$ is analytic in $D$ and $f'$ has no zeros in $D$.
>
> *B&C: Sec. 112 (text)*

^def-112-2

> [!theorem] Proposition §112.2: Conformal at a Point Implies Conformal Nearby
> If $w = f(z)$ is conformal at $z_0$, then it is conformal at each point of some neighborhood of $z_0$.
>
> *B&C: Sec. 112 (text)*

^prop-112-2

> [!proof]+ Proof
> Since $f$ is analytic at $z_0$, it is analytic in some neighborhood of $z_0$ ([[§25 Analytic Functions#^def-25-1|Definition §25.1]]: analyticity at a point is defined that way). In that neighborhood $f'$ is itself analytic ([[§57 Some Consequences of the Extension#^thm-57-1|Theorem §57.1]]), hence continuous. Since $f'$ is continuous and nonzero at $z_0$, there is a neighborhood of $z_0$ throughout which $f'(z) \ne 0$ ([[§18 Continuity#^thm-18-3|Theorem §18.3]]). In the smaller of the two neighborhoods, $f$ is analytic with nonzero derivative.

^pf-112-2

*Uses:* [[§112★ Preservation of Angles and Scale Factors#^def-112-2|Def. §112.2]], [[§25 Analytic Functions#^def-25-1|Def. §25.1]], [[§57 Some Consequences of the Extension#^thm-57-1|§57.1]], [[§18 Continuity#^thm-18-3|§18.3]]

Each of the elementary functions of Chapter 3 defines a transformation that is conformal in some domain.

> [!example] Example §112.1: The Exponential Map at the Crossing of Two Lines
> Show that $w = e^z$ is conformal everywhere, and check Theorem §112.1 at the crossing point of the lines $x = c_1$ (directed upward) and $y = c_2$ (directed to the right).
>
> **Conformal everywhere.** $(e^z)' = e^z \ne 0$ for every $z$ ([[§30 The Exponential Function#^thm-30-3|Theorem §30.3]]), and $e^z$ is entire.
>
> **The images** ([[§103★ Mappings by the Exponential Function#^ex-103-1|Example §103.1]]). The line $x = c_1$ is $z = c_1 + it$, $t$ increasing; its image $w = e^{c_1}e^{it}$ is the circle $|w| = e^{c_1}$, traversed counterclockwise. The line $y = c_2$ is $z = t + ic_2$; its image $w = e^t e^{ic_2}$ is the ray $\arg w = c_2$, traversed outward.
>
> **Angles at the crossing point** $z_0 = c_1 + ic_2$, $w_0 = e^{c_1}e^{ic_2}$. In the $z$ plane the tangent directions are $i$ (inclination $\theta_1 = \pi/2$) for $x = c_1$ and $1$ ($\theta_2 = 0$) for $y = c_2$, so the angle from the first line to the second is $\theta_2 - \theta_1 = -\pi/2$: a right angle in the negative direction. In the $w$ plane the circle's tangent vector at $w_0$ is $\frac{d}{dt}e^{c_1}e^{it} = ie^{c_1}e^{ic_2}$, with inclination $\phi_1 = c_2 + \pi/2$, and the ray's is $e^{c_1}e^{ic_2}$, with $\phi_2 = c_2$. So $\phi_2 - \phi_1 = -\pi/2$ as well. The angle of rotation is $\arg e^{z_0} = c_2$, and indeed $\phi_1 = c_2 + \theta_1$, $\phi_2 = c_2 + \theta_2$, as (3) requires.
>
> *B&C: Sec. 112, Example 1*

^ex-112-1

> [!example] Example §112.2: Level Curves of u and v Are Orthogonal
> Let $f(z) = u(x, y) + iv(x, y)$ be analytic at $z_0$ with $f'(z_0) \ne 0$, and suppose the level curves $u(x, y) = c_1$ and $v(x, y) = c_2$ are smooth arcs crossing at $z_0$. Show that they cross at right angles.
>
> **By conformality.** The transformation $w = f(z)$ maps the first arc into the vertical line $u = c_1$ and the second into the horizontal line $v = c_2$, which are orthogonal at $w_0 = f(z_0)$. By Theorem §112.1(b) the angle between the arcs at $z_0$ equals the angle between their images, $\pm\pi/2$.
>
> **Directly.** The gradients $\nabla u = (u_x, u_y)$ and $\nabla v = (v_x, v_y)$ are normal to the level curves ([[§95 Directional Derivatives and the Gradient Vector#^thm-95-7|Calc Thm. §95.7]]), and by the Cauchy–Riemann equations $v_x = -u_y$, $v_y = u_x$,
>
> $$
> \nabla u \cdot \nabla v = u_xv_x + u_yv_y = -u_xu_y + u_yu_x = 0 ,
> $$
>
> while $|\nabla u| = |\nabla v| = |f'(z_0)| \ne 0$. For instance, for $f(z) = z^2$ ($u = x^2 - y^2$, $v = 2xy$) at $z_0 = 2 + i$, the hyperbolas $x^2 - y^2 = 3$ and $xy = 2$ have normals $\nabla u = (4, -2)$ and $\nabla v = (2, 4)$, and $(4)(2) + (-2)(4) = 0$. (This was verified in exercises of §27; see [[§27★ Harmonic Functions#^rem-27-1|Remark: Level Curves Are Orthogonal]].)
>
> *B&C: Sec. 112, Example 2*

^ex-112-2

> [!definition] Definition §112.3: Isogonal Mapping
> A mapping that preserves the magnitude of the angle between two smooth arcs, but not necessarily its sense, is called **isogonal**.
>
> *B&C: Sec. 112 (text)*

^def-112-3

> [!example] Example §112.3: Reflection Is Isogonal but Not Conformal
> The transformation $w = \bar z$ is a reflection in the real axis. A directed line with inclination $\theta$ is carried to one with inclination $-\theta$, so the angle $\theta_2 - \theta_1$ from $C_1$ to $C_2$ becomes $-(\theta_2 - \theta_1)$: same magnitude, opposite sense. So $w = \bar z$ is isogonal. It is not conformal, since $\bar z$ is nowhere analytic ($u = x$, $v = -y$ give $u_x = 1 \ne -1 = v_y$). If it is followed by a conformal transformation $g$, the composite $w = g(\bar z)$ reverses the sense of every angle at points where $g' \neq 0$, and is likewise isogonal but not conformal.
>
> *B&C: Sec. 112, Example 3*

^ex-112-3

## Critical Points

> [!definition] Definition §112.4: Critical Point
> If $f$ is not constant and is analytic at $z_0$, and $f'(z_0) = 0$, then $z_0$ is a **critical point** of the transformation $w = f(z)$.
>
> *B&C: Sec. 112 (text)*

^def-112-4

At a critical point the tangent of the image may degenerate ($w'(t_0) = 0$ in (1)), so the direction of an image curve $\Gamma$ at $w_0$ is taken to be the limit of $\arg[w(t) - w_0]$ as $t \to t_0^+$, the direction of the chord from $w_0$ to a nearby later point. For a smooth arc $C$ the same limit for $\arg[z(t) - z_0]$ is the inclination $\theta_0$ of the tangent, because $(z(t) - z_0)/(t - t_0) \to z'(t_0) \ne 0$.

> [!theorem] Theorem §112.3: Angles at a Critical Point Are Multiplied by m
> Let $f$ be analytic at $z_0$ and
>
> $$
> f'(z_0) = f''(z_0) = \cdots = f^{(m-1)}(z_0) = 0, \qquad f^{(m)}(z_0) \ne 0
> $$
>
> for some integer $m \ge 1$, and let $w_0 = f(z_0)$.
>
> **(a)** In some neighborhood of $z_0$,
>
> $$
> f(z) - w_0 = (z - z_0)^m\,\frac{f^{(m)}(z_0)}{m!}\,\big[1 + g(z)\big] ,
> $$
>
> where $g$ is continuous at $z_0$ and $g(z_0) = 0$.
>
> **(b)** If a smooth arc $C$ through $z_0$ has inclination $\theta_0$ at $z_0$, its image $\Gamma$ has direction $\phi_0$ at $w_0$ with
>
> $$
> \phi_0 = m\theta_0 + \arg f^{(m)}(z_0) .
> $$
>
> **(c)** The angle $\alpha$ from a smooth arc $C_1$ to a smooth arc $C_2$ at $z_0$ becomes the angle $m\alpha$ from $\Gamma_1$ to $\Gamma_2$ at $w_0$.
>
> For $m = 1$ the map is conformal at $z_0$ and (b) is (3); for $m \ge 2$, $z_0$ is a critical point and angles there are multiplied by $m$, the smallest positive integer with $f^{(m)}(z_0) \ne 0$. (Such an $m$ exists when $f$ is not constant near $z_0$: if all derivatives vanished, the Taylor series would make $f \equiv w_0$ near $z_0$.)
>
> *B&C: Sec. 112 (text); Sec. 114, Exercise 10*

^thm-112-3

> [!proof]+ Proof
> **(a)** By Taylor's theorem ([[§63 Proof of Taylor's Theorem#^thm-63-1|Theorem §63.1]]) there is a disk $|z - z_0| < R$ in which $f(z) = \sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z - z_0)^n$. The terms with $1 \le n \le m - 1$ vanish, so
>
> $$
> f(z) - w_0 = (z - z_0)^m\sum_{n=m}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z - z_0)^{n-m} = (z - z_0)^m\,\frac{f^{(m)}(z_0)}{m!}\big[1 + g(z)\big],
> \qquad
> g(z) = \frac{m!}{f^{(m)}(z_0)}\sum_{n=m+1}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z - z_0)^{n-m} .
> $$
>
> The series for $g$ is the tail of a convergent power series divided by $(z - z_0)^m$, so it converges in the same disk; its sum is continuous there ([[§70★ Continuity of Sums of Power Series#^thm-70-1|Theorem §70.1]]), and $g(z_0) = 0$ since every term vanishes at $z_0$.
>
> **(b)** Let $z = z(t)$ run along $C$ with $z(t_0) = z_0$, and $t \to t_0^+$. Since $g(z_0) = 0$ and $g$ is continuous, $1 + g(z(t)) \ne 0$ for $t$ near $t_0$, and $z(t) \ne z_0$ for $t \ne t_0$ near $t_0$ (because $(z(t) - z_0)/(t - t_0) \to z'(t_0) \ne 0$); so $f(z(t)) - w_0 \ne 0$ for $t > t_0$ near $t_0$, and by (a) and the argument of a product ([[§9 Arguments of Products and Quotients#^thm-9-1|Theorem §9.1]]),
>
> $$
> \arg\big[f(z(t)) - w_0\big] = m\arg\big[z(t) - z_0\big] + \arg f^{(m)}(z_0) + \arg\big[1 + g(z(t))\big] \qquad (\text{mod } 2\pi) .
> $$
>
> As $t \to t_0^+$: $\arg[z(t) - z_0] \to \theta_0$ (with continuously chosen values), because $(z(t) - z_0)/(t - t_0) \to z'(t_0)$ and $t - t_0 > 0$; and $1 + g(z(t)) \to 1$, so its argument (principal value) tends to $0$. Hence the direction of $\Gamma$ at $w_0$ is $\phi_0 = \lim \arg[f(z(t)) - w_0] = m\theta_0 + \arg f^{(m)}(z_0)$.
>
> **(c)** Apply (b) to $C_1$ and $C_2$ and subtract: $\phi_2 - \phi_1 = m(\theta_2 - \theta_1) = m\alpha$, since the term $\arg f^{(m)}(z_0)$ is the same for both arcs.

^pf-112-3

*Uses:* [[§112★ Preservation of Angles and Scale Factors#^def-112-4|Def. §112.4]], [[§63 Proof of Taylor's Theorem#^thm-63-1|§63.1]] (Taylor's theorem), [[§70★ Continuity of Sums of Power Series#^thm-70-1|§70.1]] (continuity of power series), [[§9 Arguments of Products and Quotients#^thm-9-1|§9.1]]

> [!example] Example §112.4: The Critical Point of 1 + z²
> Show that $z_0 = 0$ is a critical point of $w = 1 + z^2$, and that angles between curves from $0$ are doubled.
>
> **Critical point.** $f'(z) = 2z$ vanishes at $0$, and $f''(0) = 2 \ne 0$, so $m = 2$ in Theorem §112.3.
>
> **Rays.** The transformation is the composition of $Z = z^2$ and $w = 1 + Z$. The ray $\theta = \alpha$ from $0$, $z = re^{i\alpha}$ $(r \ge 0)$, is mapped to $w = 1 + r^2e^{2i\alpha}$, the ray from $w_0 = 1$ with inclination $2\alpha$. So the angle between two rays $\theta = \alpha_1$ and $\theta = \alpha_2$ from $z_0 = 0$ is doubled, $\alpha_2 - \alpha_1 \mapsto 2(\alpha_2 - \alpha_1)$, in agreement with Theorem §112.3(b): $\phi_0 = 2\alpha + \arg 2 = 2\alpha$.
>
> *B&C: Sec. 112, Example 4*

^ex-112-4

![[m342-112-1.svg]]
*The critical point of $w = 1 + z^2$ (Example §112.4). Rays from $z_0 = 0$ at the angles $0, \pi/8, \pi/4, 3\pi/8, \pi/2$ (left) go to rays from $w_0 = 1$ at twice those angles (right), and the quarter circles $|z| = 0.5, 0.8, 1$ go to half circles of radii $0.25, 0.64, 1$ about $1$. Away from $0$ the grid still meets at right angles; only at the critical point is the angle doubled.*

## Scale Factor

> [!theorem] Proposition §112.4: The Scale Factor as a Limit of Length Ratios
> If $f$ is analytic at $z_0$, then
>
> $$
> |f'(z_0)| = \left|\lim_{z\to z_0}\frac{f(z) - f(z_0)}{z - z_0}\right| = \lim_{z\to z_0}\frac{|f(z) - f(z_0)|}{|z - z_0|} . \qquad (5)
> $$
>
> *B&C: Sec. 112, Equation (5)*

^prop-112-4

> [!proof]+ Proof
> The first equality is the definition of the derivative ([[§19 Derivatives#^def-19-1|Definition §19.1]]). For the second: if $F(z) \to L$ as $z \to z_0$, then $|F(z)| \to |L|$, since $\big||F(z)| - |L|\big| \le |F(z) - L|$ by the reverse triangle inequality ([[§5 Triangle Inequality#^cor-5-2|Corollary §5.2]]; [[§18 Continuity#^prop-18-5|Proposition §18.5]]). Apply this to $F(z) = (f(z) - f(z_0))/(z - z_0)$, whose modulus is $|f(z) - f(z_0)|/|z - z_0|$.

^pf-112-4

*Uses:* [[§19 Derivatives#^def-19-1|Def. §19.1]], [[§18 Continuity#^prop-18-5|§18.5]], [[§5 Triangle Inequality#^cor-5-2|§5.2]]

Here $|z - z_0|$ is the length of the segment from $z_0$ to $z$, and $|f(z) - f(z_0)|$ the length of the segment joining their images. So for $z$ near $z_0$ the ratio of the two lengths is approximately $|f'(z_0)|$.

> [!definition] Definition §112.5: Scale Factor
> If $f$ is analytic at $z_0$, the number $|f'(z_0)|$ is the **scale factor** of the transformation $w = f(z)$ at $z_0$. It represents an expansion if $|f'(z_0)| > 1$ and a contraction if $|f'(z_0)| < 1$.
>
> *B&C: Sec. 112 (text)*

^def-112-5

> [!remark] Remark: Small Regions Keep Their Shape
> The angle of rotation $\arg f'(z)$ and the scale factor $|f'(z)|$ vary in general from point to point, but $f'$ is continuous ([[§57 Some Consequences of the Extension#^thm-57-1|Theorem §57.1]]), so at points $z$ near $z_0$ they are approximately $\arg f'(z_0)$ and $|f'(z_0)|$. Hence the image of a small region near $z_0$ **conforms** to the original: it is approximately the original region turned through $\arg f'(z_0)$ and scaled by $|f'(z_0)|$, so it has approximately the same shape. A large region may be transformed into one that bears no resemblance to the original (the strip $0 < y < \pi$ becomes a half plane under $e^z$, [[§103★ Mappings by the Exponential Function#^ex-103-3|Example §103.3]]).

^rem-112-1
