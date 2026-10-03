---
type: section
subject: "[[Calculus]]"
chapter: 15
section: 103
stewart: "15.6"
aliases: ["Stewart 15.6"]
tags: [calculus, math233]
---
← [[§102 Surface Area]] · ↑ [[· 15 Multiple Integrals]] · [[§104 Triple Integrals in Cylindrical Coordinates]] →

*Stewart, Section 15.6 · MATH 233 (UMass, Spring 2023): Exam 2 Practice Questions (Q16), Chapter 15 Review (Q7).*

Triple integrals of functions $f(x, y, z)$ over solid regions are defined exactly as double integrals were: Riemann sums over small boxes, then extension by $0$ from a box to a general bounded solid. Fubini's Theorem again reduces them to iterated integrals, now in any of six orders. For a solid lying between two surfaces $z = u_1(x, y)$ and $z = u_2(x, y)$ over a plane region $D$, one integrates first in $z$ and then over $D$ as in [[§99 Double Integrals Over General Regions|§99]]; the solid may equally be sliced in the $x$- or $y$-direction. Setting up the limits is the hard step. The triple integral of $1$ is volume, and with a density it gives mass, moments, center of mass and moments of inertia of a solid.

## Triple Integrals over Rectangular Boxes

> [!definition] Definition §103.1: The Triple Integral over a Box
> Let $f$ be defined on a rectangular box
>
> $$
> B = \{(x, y, z) \mid a \le x \le b,\ c \le y \le d,\ r \le z \le s\} . \qquad (1)
> $$
>
> Divide $[a, b]$ into $l$ subintervals $[x_{i-1}, x_i]$ of equal width $\Delta x$, $[c, d]$ into $m$ subintervals of width $\Delta y$, and $[r, s]$ into $n$ subintervals of width $\Delta z$. The planes through the endpoints parallel to the coordinate planes divide $B$ into $lmn$ sub-boxes
>
> $$
> B_{ijk} = [x_{i-1}, x_i] \times [y_{j-1}, y_j] \times [z_{k-1}, z_k] ,
> $$
>
> each of volume $\Delta V = \Delta x\,\Delta y\,\Delta z$. With a sample point $(x_{ijk}^{\ast}, y_{ijk}^{\ast}, z_{ijk}^{\ast})$ in each $B_{ijk}$ we form the **triple Riemann sum** $\sum_{i=1}^l \sum_{j=1}^m \sum_{k=1}^n f(x_{ijk}^{\ast}, y_{ijk}^{\ast}, z_{ijk}^{\ast})\,\Delta V$ (2). The **triple integral** of $f$ over the box $B$ is
>
> $$
> \iiint_B f(x, y, z)\,dV = \lim_{l, m, n \to \infty} \sum_{i=1}^l \sum_{j=1}^m \sum_{k=1}^n f(x_{ijk}^*, y_{ijk}^*, z_{ijk}^*)\,\Delta V \qquad (3)
> $$
>
> if this limit exists. It always exists if $f$ is continuous, and then the sample point $(x_i, y_j, z_k)$ may be used:
>
> $$
> \iiint_B f(x, y, z)\,dV = \lim_{l, m, n \to \infty} \sum_{i=1}^l \sum_{j=1}^m \sum_{k=1}^n f(x_i, y_j, z_k)\,\Delta V .
> $$
>
> *Stewart: 15.6, Equations 1, 2 and Definition 3*

^def-103-1

> [!theorem] Theorem §103.1: Fubini's Theorem for Triple Integrals
> If $f$ is continuous on the rectangular box $B = [a, b] \times [c, d] \times [r, s]$, then
>
> $$
> \iiint_B f(x, y, z)\,dV = \int_r^s \int_c^d \int_a^b f(x, y, z)\,dx\,dy\,dz .
> $$
>
> The iterated integral means: integrate first with respect to $x$ (keeping $y$ and $z$ fixed), then with respect to $y$ (keeping $z$ fixed), finally with respect to $z$. The five other orders give the same value; for instance $\iiint_B f\,dV = \int_a^b \int_r^s \int_c^d f(x, y, z)\,dy\,dz\,dx$.
>
> *Stewart: 15.6, Theorem 4 (Fubini's Theorem for Triple Integrals)*

^thm-103-1

*Stewart omits the proof, as for [[§98 Double Integrals Over Rectangles#^thm-98-3|Theorem §98.3]]. In the Lebesgue setting, splitting $\mathbb{R}^3 = \mathbb{R}^p \times \mathbb{R}^q$ in the ways $1 + 2$ and $2 + 1$ and applying [[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|551 Thm. §17.6]] twice gives every order.*

> [!remark]- Connections
> - Rigorous treatment: [[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|551 Thm. §17.6]] (Fubini, for integrable $f$ on $\mathbb{R}^p \times \mathbb{R}^q$) and [[§17 Invariance Properties and Fubini's Theorem#^thm-17-3|551 Thm. §17.3]] (Tonelli, for $f \ge 0$); a continuous function on a box is integrable there. Hub: [[Fubini's Theorem (Lebesgue)]].

For example (Stewart's Example 15.6.1), on $B = [0, 1] \times [-1, 2] \times [0, 3]$, integrating in the order $x$, $y$, $z$:

$$
\iiint_B xyz^2\,dV = \int_0^3 \int_{-1}^{2} \int_0^1 xyz^2\,dx\,dy\,dz = \int_0^3 \int_{-1}^{2} \frac{yz^2}{2}\,dy\,dz = \int_0^3 \frac{3z^2}{4}\,dz = \frac{27}{4} .
$$

## Triple Integrals over General Regions

> [!definition] Definition §103.2: The Triple Integral over a Bounded Solid
> Let $E$ be a bounded region in three-dimensional space (a solid), enclosed in a box $B$ as in Equation 1. Define $F$ on $B$ to agree with $f$ on $E$ and to be $0$ at the points of $B$ outside $E$. Then
>
> $$
> \iiint_E f(x, y, z)\,dV = \iiint_B F(x, y, z)\,dV .
> $$
>
> This integral exists if $f$ is continuous and the boundary of $E$ is "reasonably smooth". The triple integral has essentially the same properties as the double integral (Stewart's Properties 5–8 of Section 15.2: [[§99 Double Integrals Over General Regions#^thm-99-3|Theorem §99.3]] and [[§99 Double Integrals Over General Regions#^thm-99-4|Theorem §99.4]]).
>
> *Stewart: 15.6 (text)*

^def-103-2

> [!definition] Definition §103.3: Type 1 Solid Region
> A solid region $E$ is of **type 1** if it lies between the graphs of two continuous functions of $x$ and $y$:
>
> $$
> E = \{(x, y, z) \mid (x, y) \in D,\ u_1(x, y) \le z \le u_2(x, y)\} , \qquad (5)
> $$
>
> where $D$ is the projection of $E$ onto the $xy$-plane. The upper boundary of $E$ is the surface $z = u_2(x, y)$ and the lower boundary is the surface $z = u_1(x, y)$.
>
> *Stewart: 15.6, Equation 5*

^def-103-3

> [!theorem] Theorem §103.2: Integrals over Type 1 Regions
> If $f$ is continuous on a type 1 region $E$ given by Equation 5, then
>
> $$
> \iiint_E f(x, y, z)\,dV = \iint_D \left[ \int_{u_1(x, y)}^{u_2(x, y)} f(x, y, z)\,dz \right] dA . \qquad (6)
> $$
>
> In the inner integral $x$ and $y$ are held fixed, so $u_1(x, y)$ and $u_2(x, y)$ are constants. In particular:
>
> - if $D$ is a type I plane region, $E = \{(x, y, z) \mid a \le x \le b,\ g_1(x) \le y \le g_2(x),\ u_1(x, y) \le z \le u_2(x, y)\}$ and
>
> $$
> \iiint_E f(x, y, z)\,dV = \int_a^b \int_{g_1(x)}^{g_2(x)} \int_{u_1(x, y)}^{u_2(x, y)} f(x, y, z)\,dz\,dy\,dx ; \qquad (7)
> $$
>
> - if $D$ is a type II plane region, $E = \{(x, y, z) \mid c \le y \le d,\ h_1(y) \le x \le h_2(y),\ u_1(x, y) \le z \le u_2(x, y)\}$ and
>
> $$
> \iiint_E f(x, y, z)\,dV = \int_c^d \int_{h_1(y)}^{h_2(y)} \int_{u_1(x, y)}^{u_2(x, y)} f(x, y, z)\,dz\,dx\,dy . \qquad (8)
> $$
>
> *Stewart: 15.6, Equations 6, 7 and 8*

^thm-103-2

> [!proof]+ Proof
> *Stewart: "by the same sort of argument that led to (15.2.3), it can be shown"; here is that argument.* Enclose $E$ in a box $B = R \times [r, s]$, where $R = [a, b] \times [c, d]$ is a rectangle containing $D$, and $r \le u_1$, $u_2 \le s$. Let $F$ be $f$ on $E$ and $0$ elsewhere in $B$. By Definition §103.2 and Fubini's Theorem (in the order $z$ first, the remaining double integral over $R$ being an iterated integral too, by [[§98 Double Integrals Over Rectangles#^thm-98-3|Theorem §98.3]]; Fubini's Theorem is used in its general form, since $F$ is bounded and discontinuous at most on the boundary surfaces $z = u_1(x, y)$, $z = u_2(x, y)$ and above the boundary curve of $D$, just as in the proof of [[§99 Double Integrals Over General Regions#^thm-99-1|Theorem §99.1]]),
>
> $$
> \iiint_E f\,dV = \iiint_B F\,dV = \iint_R \left[ \int_r^s F(x, y, z)\,dz \right] dA .
> $$
>
> Fix $(x, y)$ in $R$. If $(x, y)$ is not in $D$, no point $(x, y, z)$ is in $E$, so $F(x, y, z) = 0$ for all $z$ and the inner integral is $0$. If $(x, y)$ is in $D$, then $F(x, y, z) = 0$ for $z < u_1(x, y)$ and for $z > u_2(x, y)$, and $F = f$ in between, so the inner integral is $\int_{u_1(x, y)}^{u_2(x, y)} f(x, y, z)\,dz$. So the function of $(x, y)$ being integrated over $R$ is the extension by $0$ of $(x, y) \mapsto \int_{u_1}^{u_2} f\,dz$ from $D$ to $R$, and by [[§99 Double Integrals Over General Regions#^def-99-1|Definition §99.1]] its integral over $R$ is the integral over $D$ in (6). Formulas 7 and 8 follow by writing the double integral over $D$ as an iterated integral, [[§99 Double Integrals Over General Regions#^thm-99-1|Theorem §99.1]] or [[§99 Double Integrals Over General Regions#^thm-99-2|Theorem §99.2]].

^pf-103-2

*Uses:* [[§103 Triple Integrals#^def-103-2|Def. §103.2]], [[§103 Triple Integrals#^def-103-3|Def. §103.3]], [[§103 Triple Integrals#^thm-103-1|§103.1]], [[§98 Double Integrals Over Rectangles#^thm-98-3|§98.3]], [[§99 Double Integrals Over General Regions#^def-99-1|Def. §99.1]], [[§99 Double Integrals Over General Regions#^thm-99-1|§99.1]], [[§99 Double Integrals Over General Regions#^thm-99-2|§99.2]]

> [!definition] Definition §103.4: Type 2 and Type 3 Solid Regions
> A solid region $E$ is of **type 2** if
>
> $$
> E = \{(x, y, z) \mid (y, z) \in D,\ u_1(y, z) \le x \le u_2(y, z)\} ,
> $$
>
> where $D$ is the projection of $E$ onto the $yz$-plane; the back surface is $x = u_1(y, z)$ and the front surface is $x = u_2(y, z)$. It is of **type 3** if
>
> $$
> E = \{(x, y, z) \mid (x, z) \in D,\ u_1(x, z) \le y \le u_2(x, z)\} ,
> $$
>
> where $D$ is the projection of $E$ onto the $xz$-plane; the left surface is $y = u_1(x, z)$ and the right surface is $y = u_2(x, z)$.
>
> *Stewart: 15.6 (text)*

^def-103-4

> [!theorem] Theorem §103.3: Integrals over Type 2 and Type 3 Regions
> For continuous $f$, on a type 2 region
>
> $$
> \iiint_E f(x, y, z)\,dV = \iint_D \left[ \int_{u_1(y, z)}^{u_2(y, z)} f(x, y, z)\,dx \right] dA , \qquad (10)
> $$
>
> and on a type 3 region
>
> $$
> \iiint_E f(x, y, z)\,dV = \iint_D \left[ \int_{u_1(x, z)}^{u_2(x, z)} f(x, y, z)\,dy \right] dA . \qquad (11)
> $$
>
> In each case there may be two iterated forms, according as $D$ is a type I or type II plane region (as in Equations 7 and 8).
>
> *Stewart: 15.6, Equations 10 and 11*

^thm-103-3

> [!proof]+ Proof
> The proof of Theorem §103.2, with the roles of the coordinates permuted: integrate first in $x$ (type 2) or in $y$ (type 3), which Fubini's Theorem for Triple Integrals allows, and the extension by $0$ cuts the inner integral down to the interval between the two boundary surfaces.

^pf-103-3

*Uses:* [[§103 Triple Integrals#^thm-103-2|§103.2]], [[§103 Triple Integrals#^thm-103-1|§103.1]], [[§103 Triple Integrals#^def-103-4|Def. §103.4]]

> [!remark] Remark: Method — Setting Up a Triple Integral
> 1. **Draw two diagrams**: the solid $E$, and its projection $D$ onto the coordinate plane perpendicular to the direction of the innermost integration.
> 2. **Inner limits.** A line through a point of $D$ in that direction enters $E$ through one boundary surface and leaves through another; solve their equations for the inner variable. These limits contain at most the two outer variables.
> 3. **Middle and outer limits.** Describe $D$ as a type I or type II plane region ([[§99 Double Integrals Over General Regions#^rem-99-1|Method in §99]]): the middle limits contain at most the outer variable, the outer limits are constants.
> 4. **Choose the direction** that makes $D$ and the integrand simple (Examples §103.2 and §103.4). If $D$ is a disk, polar coordinates in that plane may finish the job; in the $xz$-plane, for instance, put $x = r\cos\theta$, $z = r\sin\theta$.

^rem-103-1

> [!example] Example §103.1: A Solid under a Saddle-Shaped Surface
> Evaluate $\displaystyle\iiint_E z\,dV$, where $E$ is the solid in the first octant bounded by the surface $z = 12xy$ and the planes $y = x$, $x = 1$.
>
> The lower boundary of $E$ is the plane $z = 0$ and the upper boundary is $z = 12xy$, so $E$ is type 1 with $u_1 = 0$, $u_2 = 12xy$. Its projection onto the $xy$-plane is the triangle bounded by $y = 0$, $y = x$ and $x = 1$, so
>
> $$
> E = \{(x, y, z) \mid 0 \le x \le 1,\ 0 \le y \le x,\ 0 \le z \le 12xy\} . \qquad (9)
> $$
>
> By Formula 7,
>
> $$
> \begin{aligned}
> \iiint_E z\,dV &= \int_0^1 \int_0^x \int_0^{12xy} z\,dz\,dy\,dx = \int_0^1 \int_0^x \Big[ \frac{z^2}{2} \Big]_{z=0}^{z=12xy} dy\,dx = \frac12 \int_0^1 \int_0^x (12xy)^2\,dy\,dx \\
> &= 72\int_0^1 \int_0^x x^2y^2\,dy\,dx = 72\int_0^1 \Big[ x^2\frac{y^3}{3} \Big]_{y=0}^{y=x} dx = 24\int_0^1 x^5\,dx = 24\Big[ \frac{x^6}{6} \Big]_0^1 = 4 .
> \end{aligned}
> $$
>
> The iterated integral sweeps out $E$ in three stages: $z$ runs from $0$ to $12xy$ with $x$, $y$ fixed (a vertical segment), then $y$ runs from $0$ to $x$ with $x$ fixed (a vertical slab), then $x$ runs from $0$ to $1$.
>
> *Stewart: Example 15.6.2*

^ex-103-1

![[m233-103-1.svg]]
*The solid of Example §103.1 (blue) over its projection $D$ (green). The innermost integral runs along a vertical segment (red) from the floor $z = 0$ to the roof $z = 12xy$; its limits depend on $(x, y)$. The point $(x, y)$ then ranges over the triangle $D$, read off as a type I region: $0 \le y \le x$, $0 \le x \le 1$.*

> [!example] Example §103.2: Projecting onto the Better Plane
> Evaluate $\displaystyle\iiint_E \sqrt{x^2 + z^2}\,dV$, where $E$ is the region bounded by the paraboloid $y = x^2 + z^2$ and the plane $y = 4$.
>
> **As a type 1 region** the projection onto the $xy$-plane is the parabolic region $x^2 \le y \le 4$ (the trace of the paraboloid in $z = 0$ is $y = x^2$), and $z = \pm\sqrt{y - x^2}$, so
>
> $$
> \iiint_E \sqrt{x^2 + z^2}\,dV = \int_{-2}^{2} \int_{x^2}^{4} \int_{-\sqrt{y - x^2}}^{\sqrt{y - x^2}} \sqrt{x^2 + z^2}\,dz\,dy\,dx ,
> $$
>
> correct but extremely difficult to evaluate.
>
> **As a type 3 region** the projection onto the $xz$-plane is the disk $D_3$: $x^2 + z^2 \le 4$ (the trace of the paraboloid in $y = 4$), the left surface is the paraboloid $y = x^2 + z^2$ and the right surface is the plane $y = 4$. By Formula 11,
>
> $$
> \iiint_E \sqrt{x^2 + z^2}\,dV = \iint_{D_3} \left[ \int_{x^2 + z^2}^{4} \sqrt{x^2 + z^2}\,dy \right] dA = \iint_{D_3} (4 - x^2 - z^2)\sqrt{x^2 + z^2}\,dA .
> $$
>
> Now use polar coordinates in the $xz$-plane, $x = r\cos\theta$, $z = r\sin\theta$ ([[§100 Double Integrals in Polar Coordinates#^thm-100-1|Theorem §100.1]]):
>
> $$
> \iiint_E \sqrt{x^2 + z^2}\,dV = \int_0^{2\pi} \int_0^2 (4 - r^2)\,r \cdot r\,dr\,d\theta = \int_0^{2\pi} d\theta \int_0^2 (4r^2 - r^4)\,dr = 2\pi\Big[ \frac{4r^3}{3} - \frac{r^5}{5} \Big]_0^2 = \frac{128\pi}{15} .
> $$
>
> *Stewart: Example 15.6.3*

^ex-103-2

## Changing the Order of Integration

Fubini's Theorem for Triple Integrals gives six orders in which a triple integral can be written as an iterated integral, and one may be much easier than another. To change the order, describe the solid from its limits and project it onto the plane required by the new innermost variable.

> [!example] Example §103.3: Rewriting an Iterated Integral in Two Other Orders
> Express $\displaystyle\int_0^1 \int_0^{x^2} \int_0^y f(x, y, z)\,dz\,dy\,dx$ as a triple integral and rewrite it as an iterated integral (a) integrating first with respect to $x$, then $z$, then $y$; (b) first with respect to $y$, then $x$, then $z$.
>
> **The solid.** The integral is $\iiint_E f\,dV$ with $E = \{0 \le x \le 1,\ 0 \le y \le x^2,\ 0 \le z \le y\}$: the type 1 region between $z = 0$ and $z = y$ over $D_1 = \{0 \le x \le 1,\ 0 \le y \le x^2\}$. So $E$ is the solid enclosed by the planes $z = 0$, $x = 1$, $y = z$ and the parabolic cylinder $y = x^2$ (or $x = \sqrt y$). Its projections onto the three coordinate planes are
>
> $$
> \begin{aligned}
> &\text{onto the } xy\text{-plane:} && D_1 = \{0 \le x \le 1,\ 0 \le y \le x^2\} = \{0 \le y \le 1,\ \sqrt y \le x \le 1\} , \\
> &\text{onto the } yz\text{-plane:} && D_2 = \{0 \le y \le 1,\ 0 \le z \le y\} = \{0 \le z \le 1,\ z \le y \le 1\} , \\
> &\text{onto the } xz\text{-plane:} && D_3 = \{0 \le x \le 1,\ 0 \le z \le x^2\} = \{0 \le z \le 1,\ \sqrt z \le x \le 1\} .
> \end{aligned}
> $$
>
> **(a)** Regard $E$ as type 2: the back surface is $x = \sqrt y$, the front surface is $x = 1$, and the projection onto the $yz$-plane is $D_2$. So $E = \{0 \le y \le 1,\ 0 \le z \le y,\ \sqrt y \le x \le 1\}$ and
>
> $$
> \iiint_E f(x, y, z)\,dV = \int_0^1 \int_0^y \int_{\sqrt y}^{1} f(x, y, z)\,dx\,dz\,dy .
> $$
>
> **(b)** Regard $E$ as type 3: the left surface is the plane $y = z$, the right surface is $y = x^2$, and the projection onto the $xz$-plane is $D_3$. So $E = \{0 \le z \le 1,\ \sqrt z \le x \le 1,\ z \le y \le x^2\}$ and
>
> $$
> \iiint_E f(x, y, z)\,dV = \int_0^1 \int_{\sqrt z}^{1} \int_z^{x^2} f(x, y, z)\,dy\,dx\,dz .
> $$
>
> *Stewart: Example 15.6.4*

^ex-103-3

> [!example] Example §103.4: Choosing an Order That Works
> Evaluate $\displaystyle\iiint_E yz\,e^{x^3}\,dV$, where $E$ is the solid region bounded by the planes $y = 0$, $y = 4$, $z = 0$, $z = x$ and $x = 2$.
>
> **The solid.** For each $x$, the cross-section is the rectangle $0 \le y \le 4$, $0 \le z \le x$, and $x$ runs from $0$ (where $z = x$ meets $z = 0$) to $2$. So $E = \{0 \le x \le 2,\ 0 \le z \le x,\ 0 \le y \le 4\}$.
>
> **The order.** $e^{x^3}$ has no elementary antiderivative, so $x$ must be the *outer* variable; the inner integrations in $y$ and $z$ then produce a power of $x$ to pair with it:
>
> $$
> \iiint_E yz\,e^{x^3}\,dV = \int_0^2 \int_0^x \int_0^4 yz\,e^{x^3}\,dy\,dz\,dx = \int_0^2 e^{x^3} \int_0^x 8z\,dz\,dx = \int_0^2 4x^2 e^{x^3}\,dx = \frac43 \Big[ e^{x^3} \Big]_0^2 = \frac43 \big( e^8 - 1 \big) .
> $$
>
> *Source: 233 Exam 2 Practice Questions, Q16*

^ex-103-4

## Applications of Triple Integrals

For $f \ge 0$, $\int_a^b f\,dx$ is an area and $\iint_D f\,dA$ a volume; $\iiint_E f\,dV$ would be the "hypervolume" of a four-dimensional object, which is not a useful picture ($E$ is only the domain of $f$; the graph of $f$ lies in four-dimensional space). The triple integral is instead interpreted according to what $x$, $y$, $z$ and $f$ mean physically. The simplest case is $f = 1$.

> [!theorem] Theorem §103.4: Volume as a Triple Integral
> The volume of a solid region $E$ is
>
> $$
> V(E) = \iiint_E dV . \qquad (12)
> $$
>
> *Stewart: 15.6, Equation 12*

^thm-103-4

> [!proof]+ Proof
> Stewart's argument for a type 1 region. Putting $f = 1$ in Formula 6,
>
> $$
> \iiint_E 1\,dV = \iint_D \left[ \int_{u_1(x, y)}^{u_2(x, y)} dz \right] dA = \iint_D \big[ u_2(x, y) - u_1(x, y) \big]\,dA ,
> $$
>
> and by [[§98 Double Integrals Over Rectangles#^thm-98-2|Theorem §98.2]] and [[§99 Double Integrals Over General Regions#^def-99-1|Definition §99.1]] (with linearity, [[§99 Double Integrals Over General Regions#^thm-99-3|Theorem §99.3]]) this is the volume that lies between the surfaces $z = u_1(x, y)$ and $z = u_2(x, y)$: the volume under $z = u_2$ minus the volume under $z = u_1$ (when $u_1 \ge 0$; otherwise shift both up by a constant, which does not change the difference).

^pf-103-4

*Uses:* [[§103 Triple Integrals#^thm-103-2|§103.2]], [[§98 Double Integrals Over Rectangles#^thm-98-2|§98.2]], [[§99 Double Integrals Over General Regions#^def-99-1|Def. §99.1]], [[§99 Double Integrals Over General Regions#^thm-99-3|§99.3]]

Triple integrals are not necessary for computing volumes, but they give an alternative way of setting up the calculation (for the tetrahedron below, Stewart's Example 15.6.5 does the same with $x + 2y + z = 2$, $x = 2y$, $x = 0$, $z = 0$ and gets $\frac13$).

> [!example] Example §103.5: A Tetrahedron
> Evaluate $\displaystyle\iiint_T y^2\,dV$, where $T$ is the solid tetrahedron with vertices $(0, 0, 0)$, $(2, 0, 0)$, $(0, 2, 0)$ and $(0, 0, 2)$. What is the volume of this solid?
>
> **The solid.** The face opposite the origin passes through $(2, 0, 0)$, $(0, 2, 0)$, $(0, 0, 2)$, so it is the plane $x + y + z = 2$, and $T = \{x, y, z \ge 0,\ x + y + z \le 2\}$. Since the integrand depends only on $y$, make $y$ the outer variable: for fixed $y$ in $[0, 2]$ the cross-section is the triangle $x, z \ge 0$, $x + z \le 2 - y$, so
>
> $$
> T = \{0 \le y \le 2,\ 0 \le x \le 2 - y,\ 0 \le z \le 2 - x - y\} .
> $$
>
> **The integral.** The inner two integrations give the area of the cross-section, $\int_0^{2-y} (2 - x - y)\,dx = \frac12 (2 - y)^2$, so
>
> $$
> \iiint_T y^2\,dV = \int_0^2 y^2 \cdot \tfrac12 (2 - y)^2\,dy = \frac12 \int_0^2 (4y^2 - 4y^3 + y^4)\,dy = \frac12 \Big( \frac{32}{3} - 16 + \frac{32}{5} \Big) = \frac12 \cdot \frac{16}{15} = \frac{8}{15} .
> $$
>
> **The volume.** By [[§103 Triple Integrals#^thm-103-4|Theorem §103.4]], with the same limits,
>
> $$
> V(T) = \iiint_T dV = \int_0^2 \tfrac12 (2 - y)^2\,dy = \Big[ -\tfrac16 (2 - y)^3 \Big]_0^2 = \frac86 = \frac43 ,
> $$
>
> which agrees with $\frac13 \cdot (\text{base area}) \cdot (\text{height}) = \frac13 \cdot 2 \cdot 2 = \frac43$.
>
> *The posted solution integrates in the order $dz\,dy\,dx$; its last line drops the factor $-\tfrac13$ on the middle term and the sign of the last term (it would give $\frac{88}{15}$), and its antiderivative evaluated correctly gives $\frac{8}{15}$. Its volume $\frac43$ agrees.*
>
> *Source: 233 Chapter 15 Review, Q7*

^ex-103-5

All the applications of double integrals in [[§101 Applications of Double Integrals|§101]] extend to triple integrals. If a solid occupying $E$ has density $\rho(x, y, z)$ (mass per unit volume), divide a box containing $E$ into sub-boxes $B_{ijk}$, let $\rho = 0$ outside $E$, and approximate the mass of the part in $B_{ijk}$ by $\rho(x_{ijk}^*, y_{ijk}^*, z_{ijk}^*)\,\Delta V$; adding and passing to the limit gives the following.

> [!definition] Definition §103.5: Mass, Moments, Center of Mass and Moments of Inertia of a Solid
> For a solid occupying $E$ with density $\rho(x, y, z)$:
>
> - the **mass** is $m = \displaystyle\lim_{l, m, n \to \infty} \sum_{i,j,k} \rho(x_{ijk}^{\ast}, y_{ijk}^{\ast}, z_{ijk}^{\ast})\,\Delta V = \iiint_E \rho(x, y, z)\,dV$; (13)
> - the **moments** about the three coordinate planes are
>
> $$
> M_{yz} = \iiint_E x\,\rho\,dV , \qquad M_{xz} = \iiint_E y\,\rho\,dV , \qquad M_{xy} = \iiint_E z\,\rho\,dV ; \qquad (14)
> $$
>
> - the **center of mass** is $(\bar x, \bar y, \bar z)$ with $\bar x = M_{yz}/m$, $\bar y = M_{xz}/m$, $\bar z = M_{xy}/m$ (15); for constant density it is called the **centroid** of $E$;
> - the **moments of inertia** about the three coordinate axes are
>
> $$
> I_x = \iiint_E (y^2 + z^2)\rho\,dV , \qquad I_y = \iiint_E (x^2 + z^2)\rho\,dV , \qquad I_z = \iiint_E (x^2 + y^2)\rho\,dV . \qquad (16)
> $$
>
> Likewise, a charge density $\sigma(x, y, z)$ gives the total **electric charge** $Q = \iiint_E \sigma\,dV$, and the **joint density function** of three continuous random variables $X$, $Y$, $Z$ is a function $f \ge 0$ with $P\big((X, Y, Z) \in E\big) = \iiint_E f\,dV$ and $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f\,dz\,dy\,dx = 1$; in particular $P(a \le X \le b,\ c \le Y \le d,\ r \le Z \le s) = \int_a^b \int_c^d \int_r^s f\,dz\,dy\,dx$.
>
> *Stewart: 15.6, Equations 13, 14, 15 and 16*

^def-103-5

For example (Stewart's Example 15.6.6), consider the solid of constant density $\rho$ bounded by the parabolic cylinder $x = y^2$ and the planes $x = z$, $z = 0$ and $x = 1$. The lower and upper surfaces are the planes $z = 0$ and $z = x$, and the projection onto the $xy$-plane is the region between $x = y^2$ and $x = 1$, so as a type 1 region

$$
E = \{(x, y, z) \mid -1 \le y \le 1,\ y^2 \le x \le 1,\ 0 \le z \le x\} .
$$

**Mass.** Using the symmetry in $y$ to halve the $y$-interval,

$$
m = \int_{-1}^{1} \int_{y^2}^{1} \int_0^x \rho\,dz\,dx\,dy = \rho\int_{-1}^{1} \int_{y^2}^{1} x\,dx\,dy = \rho\int_{-1}^{1} \Big[ \frac{x^2}{2} \Big]_{x=y^2}^{x=1} dy = \frac{\rho}{2} \int_{-1}^{1} (1 - y^4)\,dy = \rho\int_0^1 (1 - y^4)\,dy = \frac{4\rho}{5} .
$$

**Moments.** $E$ and $\rho$ are symmetric about the $xz$-plane, so $M_{xz} = 0$ and $\bar y = 0$. The other moments are

$$
M_{yz} = \iiint_E x\rho\,dV = \rho\int_{-1}^{1} \int_{y^2}^{1} x^2\,dx\,dy = \frac{2\rho}{3} \int_0^1 (1 - y^6)\,dy = \frac{2\rho}{3} \cdot \frac67 = \frac{4\rho}{7} ,
$$

$$
M_{xy} = \iiint_E z\rho\,dV = \rho\int_{-1}^{1} \int_{y^2}^{1} \Big[ \frac{z^2}{2} \Big]_{z=0}^{z=x} dx\,dy = \frac{\rho}{2} \int_{-1}^{1} \int_{y^2}^{1} x^2\,dx\,dy = \frac{\rho}{3} \int_0^1 (1 - y^6)\,dy = \frac{2\rho}{7} .
$$

Therefore the center of mass is

$$
(\bar x, \bar y, \bar z) = \Big( \frac{M_{yz}}{m}, \frac{M_{xz}}{m}, \frac{M_{xy}}{m} \Big) = \Big( \frac57, 0, \frac{5}{14} \Big) .
$$
