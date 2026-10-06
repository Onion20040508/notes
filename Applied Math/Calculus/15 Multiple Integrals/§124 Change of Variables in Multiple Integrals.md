---
type: section
subject: "[[Calculus]]"
chapter: 15
section: 124
stewart: "15.9"
aliases: ["Stewart 15.9"]
tags: [calculus, math233]
---
← [[§123 Triple Integrals in Spherical Coordinates]] · ↑ [[· 15 Multiple Integrals]] · [[§125 Vector Fields]] →

*Stewart, Section 15.9 · MATH 233 (UMass, Spring 2023): this section was not on the course syllabus.*

Polar, cylindrical and spherical coordinates are special cases of one formula. A change of variables $x = g(u, v)$, $y = h(u, v)$ maps a region $S$ of the $uv$-plane onto a region $R$ of the $xy$-plane, and a small rectangle of area $\Delta u\,\Delta v$ is mapped to a curved region of area about $|\partial(x, y)/\partial(u, v)|\,\Delta u\,\Delta v$, where the Jacobian $\partial(x, y)/\partial(u, v)$ is the determinant of the matrix of partial derivatives. So $dA$ is replaced by $|\partial(x, y)/\partial(u, v)|\,du\,dv$: the two-variable analogue of $dx = g'(u)\,du$ in the Substitution Rule. A good change of variables simplifies the region, the integrand, or both. In three variables the Jacobian is a $3 \times 3$ determinant, and computing it for spherical coordinates recovers $\rho^2\sin\phi$.

## Change of Variables in Double Integrals

In one variable, the Substitution Rule ([[§43 The Substitution Rule#^thm-43-3|Theorem §43.3]]) with the roles of $x$ and $u$ reversed reads

$$
\int_a^b f(x)\,dx = \int_c^d f(g(u))\,g'(u)\,du = \int_c^d f(x(u))\,\frac{dx}{du}\,du , \qquad x = g(u),\ a = g(c),\ b = g(d)
$$

(Stewart 15.9, Formulas 1 and 2). The change to polar coordinates ([[§117 Double Integrals in Polar Coordinates#^thm-117-1|Theorem §117.1]]) is already a change of variables for double integrals, $\iint_R f(x, y)\,dA = \iint_S f(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta$, where $S$ is the region of the $r\theta$-plane that corresponds to $R$. In general:

> [!definition] Definition §124.1: Transformations
> A **transformation** $T$ from the $uv$-plane to the $xy$-plane is a function $T(u, v) = (x, y)$ whose domain and range are subsets of $\mathbb{R}^2$, given by equations
>
> $$
> x = g(u, v) , \qquad y = h(u, v) \qquad (3)
> $$
>
> (also written $x = x(u, v)$, $y = y(u, v)$). $T$ is a **$C^1$ transformation** if $g$ and $h$ have continuous first-order partial derivatives. If $T(u_1, v_1) = (x_1, y_1)$, then $(x_1, y_1)$ is the **image** of $(u_1, v_1)$; the **image of a region** $S$ is the set $T(S)$ of the images of all its points. $T$ is **one-to-one** if no two points have the same image. A one-to-one $T$ has an **inverse transformation** $T^{-1}$ from the $xy$-plane to the $uv$-plane, and it may be possible to solve Equations 3 for $u = G(x, y)$, $v = H(x, y)$.
>
> *Stewart: 15.9 (text) and Equation 3*

^def-124-1

> [!example] Example §124.1: The Image of a Square
> A transformation is defined by the equations $x = u^2 - v^2$, $y = 2uv$. Find the image of the square $S = \{(u, v) \mid 0 \le u \le 1,\ 0 \le v \le 1\}$.
>
> The transformation maps the boundary of $S$ onto the boundary of the image, so we find the images of the four sides.
> - $S_1$: $v = 0$, $0 \le u \le 1$. Then $x = u^2$, $y = 0$, so $0 \le x \le 1$: $S_1$ is mapped onto the segment from $(0, 0)$ to $(1, 0)$.
> - $S_2$: $u = 1$, $0 \le v \le 1$. Then $x = 1 - v^2$, $y = 2v$; eliminating $v$ gives $x = 1 - \dfrac{y^2}{4}$, $0 \le x \le 1$, part of a parabola. (4)
> - $S_3$: $v = 1$, $0 \le u \le 1$. Then $x = u^2 - 1$, $y = 2u$, the parabolic arc $x = \dfrac{y^2}{4} - 1$, $-1 \le x \le 0$. (5)
> - $S_4$: $u = 0$, $0 \le v \le 1$. Then $x = -v^2$, $y = 0$, so $-1 \le x \le 0$.
>
> The image of $S$ is the region $R$ bounded by the $x$-axis and the parabolas (4) and (5), that is, by $y^2 = 4 - 4x$ and $y^2 = 4 + 4x$, $y \ge 0$. As we move around the square counterclockwise, we also move around $R$ counterclockwise.
>
> *Stewart: Example 15.9.1*

^ex-124-1

![[m233-106-1.svg]]
*[[§124 Change of Variables in Multiple Integrals#^ex-124-1|Example §124.1]]: the transformation $x = u^2 - v^2$, $y = 2uv$ maps the unit square $S$ onto the region $R$ under two parabolic arcs. Each side of $S$ and its image have the same colour; the bottom side $S_1$ and the left side $S_4$ are both folded onto the $x$-axis, on either side of the origin, and $S_2$, $S_3$ become the arcs $x = 1 - y^2/4$ and $x = y^2/4 - 1$, meeting at $(0, 2)$, the image of the corner $(1, 1)$.*

Now consider how a change of variables affects a double integral. Start with a small rectangle $S$ in the $uv$-plane whose lower left corner is $(u_0, v_0)$ and whose dimensions are $\Delta u$ and $\Delta v$. Its image $R = T(S)$ has the boundary point $(x_0, y_0) = T(u_0, v_0)$. Let

$$
\mathbf r(u, v) = g(u, v)\,\mathbf i + h(u, v)\,\mathbf j
$$

be the position vector of the image of $(u, v)$. The lower side $v = v_0$ of $S$ has image curve $\mathbf r(u, v_0)$, with tangent vector at $(x_0, y_0)$

$$
\mathbf r_u = g_u(u_0, v_0)\,\mathbf i + h_u(u_0, v_0)\,\mathbf j = \frac{\partial x}{\partial u}\,\mathbf i + \frac{\partial y}{\partial u}\,\mathbf j ,
$$

and similarly the left side $u = u_0$ has image curve $\mathbf r(u_0, v)$ with tangent vector $\mathbf r_v = \frac{\partial x}{\partial v}\,\mathbf i + \frac{\partial y}{\partial v}\,\mathbf j$. Approximate $R$ by the parallelogram determined by the secant vectors $\mathbf a = \mathbf r(u_0 + \Delta u, v_0) - \mathbf r(u_0, v_0)$ and $\mathbf b = \mathbf r(u_0, v_0 + \Delta v) - \mathbf r(u_0, v_0)$. Since

$$
\mathbf r_u = \lim_{\Delta u \to 0} \frac{\mathbf r(u_0 + \Delta u, v_0) - \mathbf r(u_0, v_0)}{\Delta u} ,
$$

we have $\mathbf a \approx \Delta u\,\mathbf r_u$, and similarly $\mathbf b \approx \Delta v\,\mathbf r_v$. So $R$ is approximately the parallelogram determined by $\Delta u\,\mathbf r_u$ and $\Delta v\,\mathbf r_v$, whose area ([[§96 The Cross Product#^cor-96-6|Corollary §96.6]]) is

$$
|(\Delta u\,\mathbf r_u) \times (\Delta v\,\mathbf r_v)| = |\mathbf r_u \times \mathbf r_v|\,\Delta u\,\Delta v . \qquad (6)
$$

Computing the cross product,

$$
\mathbf r_u \times \mathbf r_v = \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \\ \dfrac{\partial x}{\partial u} & \dfrac{\partial y}{\partial u} & 0 \\ \dfrac{\partial x}{\partial v} & \dfrac{\partial y}{\partial v} & 0 \end{vmatrix}
= \begin{vmatrix} \dfrac{\partial x}{\partial u} & \dfrac{\partial y}{\partial u} \\ \dfrac{\partial x}{\partial v} & \dfrac{\partial y}{\partial v} \end{vmatrix} \mathbf k
= \begin{vmatrix} \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\ \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} \end{vmatrix} \mathbf k .
$$

![[m233-106-2.svg]]
*Why the Jacobian appears. A small rectangle in the $uv$-plane (left) is mapped by $T$ to a curved quadrilateral (blue, right). Near $(x_0, y_0)$ it is close to the parallelogram (red) spanned by $\Delta u\,\mathbf r_u$ and $\Delta v\,\mathbf r_v$, whose area is $|\mathbf r_u \times \mathbf r_v|\,\Delta u\,\Delta v = |\partial(x, y)/\partial(u, v)|\,\Delta u\,\Delta v$.*

> [!definition] Definition §124.2: The Jacobian
> The **Jacobian** of the transformation $T$ given by $x = g(u, v)$ and $y = h(u, v)$ is
>
> $$
> \frac{\partial(x, y)}{\partial(u, v)} = \begin{vmatrix} \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\[6pt] \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} \end{vmatrix} = \frac{\partial x}{\partial u}\frac{\partial y}{\partial v} - \frac{\partial x}{\partial v}\frac{\partial y}{\partial u} .
> $$
>
> With this notation, Equation 6 gives the approximation
>
> $$
> \Delta A \approx \left| \frac{\partial(x, y)}{\partial(u, v)} \right| \Delta u\,\Delta v \qquad (8)
> $$
>
> to the area $\Delta A$ of the image $R$ of a small rectangle, with the Jacobian evaluated at $(u_0, v_0)$.
>
> *Stewart: 15.9, Definition 7 and Equation 8*

^def-124-2

The Jacobian is named after Carl Gustav Jacob Jacobi (1804–1851); Cauchy first used these determinants, and Jacobi developed them into a method for evaluating multiple integrals.

> [!theorem] Theorem §124.1: Change of Variables in a Double Integral
> Suppose that $T$ is a $C^1$ transformation whose Jacobian is nonzero and that $T$ maps a region $S$ in the $uv$-plane onto a region $R$ in the $xy$-plane. Suppose that $f$ is continuous on $R$ and that $R$ and $S$ are type I or type II plane regions. Suppose also that $T$ is one-to-one, except perhaps on the boundary of $S$. Then
>
> $$
> \iint_R f(x, y)\,dA = \iint_S f\big(x(u, v), y(u, v)\big) \left| \frac{\partial(x, y)}{\partial(u, v)} \right| du\,dv .
> $$
>
> That is, we change from $x$, $y$ to $u$, $v$ by expressing $x$ and $y$ in terms of $u$ and $v$ and writing $dA = \left| \dfrac{\partial(x, y)}{\partial(u, v)} \right| du\,dv$. The absolute value of the Jacobian plays the role of $dx/du$ in the one-variable formula.
>
> *Stewart: 15.9, Theorem 9 (Change of Variables in a Double Integral)*

^thm-124-1

*Stewart omits the proof ("a full proof is given in books on advanced calculus"); see [[§25 Change of Variables on General Domains#^thm-25-3|452 Thm. §25.3]] (for a rectangle, with three proofs, [[§24 The Change of Variables Formula#^thm-24-2|452 Thm. §24.2]]).*

> [!remark] Remark: Why It Works
> Divide $S$ into rectangles $S_{ij}$ with corners $(u_i, v_j)$ and let $R_{ij}$ be their images, with corners $(x_i, y_j) = T(u_i, v_j)$. Applying the approximation (8) to each $R_{ij}$,
>
> $$
> \iint_R f(x, y)\,dA \approx \sum_{i=1}^m \sum_{j=1}^n f(x_i, y_j)\,\Delta A \approx \sum_{i=1}^m \sum_{j=1}^n f\big(g(u_i, v_j), h(u_i, v_j)\big) \left| \frac{\partial(x, y)}{\partial(u, v)} \right| \Delta u\,\Delta v ,
> $$
>
> with the Jacobian evaluated at $(u_i, v_j)$. The last double sum is a Riemann sum for $\iint_S f\big(g(u, v), h(u, v)\big)\,\big|\partial(x, y)/\partial(u, v)\big|\,du\,dv$, which suggests the theorem. What a proof must control is that the errors in (8), each small compared with $\Delta u\,\Delta v$, still add up to something that tends to $0$.

^rem-124-1

> [!remark]- Connections
> - Rigorous treatment: [[§25 Change of Variables on General Domains#^thm-25-3|452 Thm. §25.3]] (general Jordan measurable domains, $T$ a $C^1$ bijection with $C^1$ inverse and $J \ne 0$). Hub: [[Change of Variables Formula (multiple integrals)]].
> - The linear case is where the factor $|\det|$ comes from: a linear map multiplies areas and volumes by $|\det T|$, [[§37 Determinants#^ladr-9-61|LADR 9.61]] and [[§25 Change of Variables on General Domains#^prop-25-5|452 Prop. §25.5]]; for [[§11 Lebesgue Measurable Sets#^def-11-5|Lebesgue measure]] $m(T(R)) = |\det T|\,m(R)$ is proved by row operations inside [[§30 Differentiating the Integral#^thm-30-3|551 Thm. §30.3]]. Approximation (8) says that $T$ is close to its linearization on a small rectangle.
> - Matrix version of the linear case: [[§28 Determinants as Area or Volume#^thm-28-3|235 Thm. §28.3]] and [[§28 Determinants as Area or Volume#^thm-28-4|235 Thm. §28.4]] (a linear map with matrix $A$ multiplies every area or volume by $|\det A|$, the constant Jacobian), worked in [[§28 Determinants as Area or Volume#^ex-28-2|235 Ex. §28.2]].

> [!example] Example §124.2: Polar Coordinates as a Special Case
> The transformation $T$ from the $r\theta$-plane to the $xy$-plane given by $x = g(r, \theta) = r\cos\theta$, $y = h(r, \theta) = r\sin\theta$ maps an ordinary rectangle $S = [a, b] \times [\alpha, \beta]$ in the $r\theta$-plane onto a polar rectangle in the $xy$-plane. Its Jacobian is
>
> $$
> \frac{\partial(x, y)}{\partial(r, \theta)} = \begin{vmatrix} \dfrac{\partial x}{\partial r} & \dfrac{\partial x}{\partial \theta} \\[6pt] \dfrac{\partial y}{\partial r} & \dfrac{\partial y}{\partial \theta} \end{vmatrix} = \begin{vmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{vmatrix} = r\cos^2\theta + r\sin^2\theta = r > 0 ,
> $$
>
> so [[§124 Change of Variables in Multiple Integrals#^thm-124-1|Theorem §124.1]] gives
>
> $$
> \iint_R f(x, y)\,dx\,dy = \iint_S f(r\cos\theta, r\sin\theta) \left| \frac{\partial(x, y)}{\partial(r, \theta)} \right| dr\,d\theta = \int_\alpha^\beta \int_a^b f(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta ,
> $$
>
> which is Formula 15.3.2 ([[§117 Double Integrals in Polar Coordinates#^thm-117-1|Theorem §117.1]]). (If $a = 0$, the Jacobian vanishes and $T$ fails to be one-to-one on the edge $r = 0$ of $S$, which is allowed: it is part of the boundary.)
>
> *Stewart: 15.9 (text)*

^ex-124-2

> [!example] Example §124.3: Integrating over a Parabolic Region
> Use the change of variables $x = u^2 - v^2$, $y = 2uv$ to evaluate $\displaystyle\iint_R y\,dA$, where $R$ is the region bounded by the $x$-axis and the parabolas $y^2 = 4 - 4x$ and $y^2 = 4 + 4x$, $y \ge 0$.
>
> By [[§124 Change of Variables in Multiple Integrals#^ex-124-1|Example §124.1]], $R = T(S)$ for the square $S = [0, 1] \times [0, 1]$; the point of the change of variables is that $S$ is a much simpler region than $R$. The Jacobian is
>
> $$
> \frac{\partial(x, y)}{\partial(u, v)} = \begin{vmatrix} 2u & -2v \\ 2v & 2u \end{vmatrix} = 4u^2 + 4v^2 > 0 .
> $$
>
> By [[§124 Change of Variables in Multiple Integrals#^thm-124-1|Theorem §124.1]],
>
> $$
> \begin{aligned}
> \iint_R y\,dA &= \iint_S 2uv \left| \frac{\partial(x, y)}{\partial(u, v)} \right| dA = \int_0^1 \int_0^1 (2uv)\,4(u^2 + v^2)\,du\,dv = 8\int_0^1 \int_0^1 (u^3v + uv^3)\,du\,dv \\
> &= 8\int_0^1 \Big[ \tfrac14 u^4 v + \tfrac12 u^2 v^3 \Big]_{u=0}^{u=1} dv = \int_0^1 (2v + 4v^3)\,dv = \Big[ v^2 + v^4 \Big]_0^1 = 2 .
> \end{aligned}
> $$
>
> *Stewart: Example 15.9.2*

^ex-124-3

> [!remark] Remark: Method — Choosing a Change of Variables
> [[§124 Change of Variables in Multiple Integrals#^ex-124-3|Example §124.3]] was not difficult because a suitable change of variables was given. Otherwise the first step is to think of one.
> 1. If $f(x, y)$ is difficult to integrate, its form may suggest new variables: expressions that occur together, such as $x + y$ and $x - y$, become $u$ and $v$.
> 2. If the region $R$ is awkward, choose the transformation so that the corresponding region $S$ in the $uv$-plane has a convenient description, ideally a rectangle: if the sides of $R$ lie on curves $G(x, y) = c_1$, $G(x, y) = c_2$, $H(x, y) = c_3$, $H(x, y) = c_4$, try $u = G(x, y)$, $v = H(x, y)$.
> 3. Such a choice gives $u$, $v$ in terms of $x$, $y$, that is, $T^{-1}$. [[§124 Change of Variables in Multiple Integrals#^thm-124-1|Theorem §124.1]] needs $T$: solve for $x$ and $y$, and compute $\partial(x, y)/\partial(u, v)$. (Alternatively, $\partial(x, y)/\partial(u, v) = 1\big/\big(\partial(u, v)/\partial(x, y)\big)$: by the Chain Rule the matrices of partial derivatives of $T$ and $T^{-1}$ are inverse to each other, and the determinant of a product is the product of the determinants.)
> 4. Find $S$ by mapping each boundary curve of $R$, and remember the absolute value of the Jacobian.

^rem-124-2

> [!example] Example §124.4: A Substitution Suggested by the Integrand
> Evaluate $\displaystyle\iint_R e^{(x + y)/(x - y)}\,dA$, where $R$ is the trapezoidal region with vertices $(1, 0)$, $(2, 0)$, $(0, -2)$ and $(0, -1)$.
>
> **The change of variables.** $e^{(x + y)/(x - y)}$ is not easy to integrate, so let
>
> $$
> u = x + y , \qquad v = x - y . \qquad (10)
> $$
>
> These define $T^{-1}$; solving for $x$ and $y$ gives $T$:
>
> $$
> x = \tfrac12 (u + v) , \qquad y = \tfrac12 (u - v) , \qquad (11)
> $$
>
> with Jacobian
>
> $$
> \frac{\partial(x, y)}{\partial(u, v)} = \begin{vmatrix} \tfrac12 & \tfrac12 \\ \tfrac12 & -\tfrac12 \end{vmatrix} = -\frac14 - \frac14 = -\frac12 .
> $$
>
> **The region.** The sides of $R$ lie on the lines $y = 0$, $x - y = 2$, $x = 0$, $x - y = 1$, whose images in the $uv$-plane (by (10) or (11)) are $u = v$, $v = 2$, $u = -v$, $v = 1$. So $S$ is the trapezoid with vertices $(1, 1)$, $(2, 2)$, $(-2, 2)$, $(-1, 1)$:
>
> $$
> S = \{(u, v) \mid 1 \le v \le 2,\ -v \le u \le v\} .
> $$
>
> **The integral.** By [[§124 Change of Variables in Multiple Integrals#^thm-124-1|Theorem §124.1]],
>
> $$
> \iint_R e^{(x + y)/(x - y)}\,dA = \iint_S e^{u/v} \left| -\frac12 \right| du\,dv = \int_1^2 \int_{-v}^{v} e^{u/v}\big(\tfrac12\big)\,du\,dv = \frac12 \int_1^2 \Big[ v e^{u/v} \Big]_{u=-v}^{u=v} dv = \frac12 \int_1^2 (e - e^{-1})\,v\,dv = \frac34 \big( e - e^{-1} \big) .
> $$
>
> *Stewart: Example 15.9.3*

^ex-124-4

## Change of Variables in Triple Integrals

Let $T$ be a one-to-one transformation that maps a region $S$ in $uvw$-space onto a region $R$ in $xyz$-space by means of the equations $x = g(u, v, w)$, $y = h(u, v, w)$, $z = k(u, v, w)$.

> [!definition] Definition §124.3: The Jacobian of a Transformation of Space
> The **Jacobian** of $T$ is the $3 \times 3$ determinant
>
> $$
> \frac{\partial(x, y, z)}{\partial(u, v, w)} = \begin{vmatrix} \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} & \dfrac{\partial x}{\partial w} \\[6pt] \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} & \dfrac{\partial y}{\partial w} \\[6pt] \dfrac{\partial z}{\partial u} & \dfrac{\partial z}{\partial v} & \dfrac{\partial z}{\partial w} \end{vmatrix} . \qquad (12)
> $$
>
> *Stewart: 15.9, Equation 12*

^def-124-3

> [!theorem] Theorem §124.2: Change of Variables in a Triple Integral
> Under hypotheses similar to those of [[§124 Change of Variables in Multiple Integrals#^thm-124-1|Theorem §124.1]],
>
> $$
> \iiint_R f(x, y, z)\,dV = \iiint_S f\big(x(u, v, w), y(u, v, w), z(u, v, w)\big) \left| \frac{\partial(x, y, z)}{\partial(u, v, w)} \right| du\,dv\,dw . \qquad (13)
> $$
>
> *Stewart: 15.9, Formula 13*

^thm-124-2

*Stewart omits the proof; see [[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]] (change of variables in $\mathbb{R}^n$).*

> [!example] Example §124.5: Deriving the Spherical-Coordinate Formula
> Use Formula 13 to derive the formula for triple integration in spherical coordinates.
>
> The change of variables is $x = \rho\sin\phi\cos\theta$, $y = \rho\sin\phi\sin\theta$, $z = \rho\cos\phi$. The Jacobian, expanded along the third row, is
>
> $$
> \begin{aligned}
> \frac{\partial(x, y, z)}{\partial(\rho, \theta, \phi)} &= \begin{vmatrix} \sin\phi\cos\theta & -\rho\sin\phi\sin\theta & \rho\cos\phi\cos\theta \\ \sin\phi\sin\theta & \rho\sin\phi\cos\theta & \rho\cos\phi\sin\theta \\ \cos\phi & 0 & -\rho\sin\phi \end{vmatrix} \\
> &= \cos\phi \begin{vmatrix} -\rho\sin\phi\sin\theta & \rho\cos\phi\cos\theta \\ \rho\sin\phi\cos\theta & \rho\cos\phi\sin\theta \end{vmatrix} - \rho\sin\phi \begin{vmatrix} \sin\phi\cos\theta & -\rho\sin\phi\sin\theta \\ \sin\phi\sin\theta & \rho\sin\phi\cos\theta \end{vmatrix} \\
> &= \cos\phi\big( -\rho^2\sin\phi\cos\phi\sin^2\theta - \rho^2\sin\phi\cos\phi\cos^2\theta \big) - \rho\sin\phi\big( \rho\sin^2\phi\cos^2\theta + \rho\sin^2\phi\sin^2\theta \big) \\
> &= -\rho^2\sin\phi\cos^2\phi - \rho^2\sin\phi\sin^2\phi = -\rho^2\sin\phi .
> \end{aligned}
> $$
>
> Since $0 \le \phi \le \pi$, $\sin\phi \ge 0$, so $\left| \dfrac{\partial(x, y, z)}{\partial(\rho, \theta, \phi)} \right| = |-\rho^2\sin\phi| = \rho^2\sin\phi$, and Formula 13 gives
>
> $$
> \iiint_R f(x, y, z)\,dV = \iiint_S f(\rho\sin\phi\cos\theta, \rho\sin\phi\sin\theta, \rho\cos\phi)\,\rho^2\sin\phi\,d\rho\,d\theta\,d\phi ,
> $$
>
> which is equivalent to Formula 15.8.3 ([[§123 Triple Integrals in Spherical Coordinates#^thm-123-2|Theorem §123.2]]). The same computation with $x = r\cos\theta$, $y = r\sin\theta$, $z = z$ gives $\partial(x, y, z)/\partial(r, \theta, z) = r$, the factor in cylindrical coordinates ([[§122 Triple Integrals in Cylindrical Coordinates#^thm-122-1|Theorem §122.1]]).
>
> *Stewart: Example 15.9.4*

^ex-124-5
