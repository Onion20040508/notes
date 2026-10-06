---
type: section
subject: "[[Calculus]]"
chapter: 15
section: 121
stewart: "15.6"
aliases: ["Stewart 15.6 (cont.)"]
tags: [calculus, math233]
---
← [[§120 Triple Integrals]] · ↑ [[· 15 Multiple Integrals]] · [[§122 Triple Integrals in Cylindrical Coordinates]] →

*Stewart, Section 15.6 · MATH 233 (UMass, Spring 2023): Exam 2 Practice Questions (Q16), Chapter 15 Review (Q7).*

The triple integral of $1$ is volume, and with a density it gives mass, moments, center of mass and moments of inertia of a solid.

## Applications of Triple Integrals

For $f \ge 0$, $\int_a^b f\,dx$ is an area and $\iint_D f\,dA$ a volume; $\iiint_E f\,dV$ would be the "hypervolume" of a four-dimensional object, which is not a useful picture ($E$ is only the domain of $f$; the graph of $f$ lies in four-dimensional space). The triple integral is instead interpreted according to what $x$, $y$, $z$ and $f$ mean physically. The simplest case is $f = 1$.

> [!theorem] Theorem §144.1: Volume as a Triple Integral
> The volume of a solid region $E$ is
>
> $$
> V(E) = \iiint_E dV . \qquad (12)
> $$
>
> *Stewart: 15.6, Equation 12*

^thm-121-1

> [!proof]+ Proof
> Stewart's argument for a type 1 region. Putting $f = 1$ in Formula 6,
>
> $$
> \iiint_E 1\,dV = \iint_D \left[ \int_{u_1(x, y)}^{u_2(x, y)} dz \right] dA = \iint_D \big[ u_2(x, y) - u_1(x, y) \big]\,dA ,
> $$
>
> and by [[§115 Double Integrals Over Rectangles#^thm-115-2|Theorem §115.2]] and [[§116 Double Integrals Over General Regions#^def-116-1|Definition §116.1]] (with linearity, [[§116 Double Integrals Over General Regions#^thm-116-3|Theorem §116.3]]) this is the volume that lies between the surfaces $z = u_1(x, y)$ and $z = u_2(x, y)$: the volume under $z = u_2$ minus the volume under $z = u_1$ (when $u_1 \ge 0$; otherwise shift both up by a constant, which does not change the difference).

^pf-121-1

*Uses:* [[§120 Triple Integrals#^thm-120-2|§120.2]], [[§115 Double Integrals Over Rectangles#^thm-115-2|§115.2]], [[§116 Double Integrals Over General Regions#^def-116-1|Def. §116.1]], [[§116 Double Integrals Over General Regions#^thm-116-3|§116.3]]

Triple integrals are not necessary for computing volumes, but they give an alternative way of setting up the calculation (for the tetrahedron below, Stewart's Example 15.6.5 does the same with $x + 2y + z = 2$, $x = 2y$, $x = 0$, $z = 0$ and gets $\frac13$).

> [!example] Example §144.1: A Tetrahedron
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
> **The volume.** By [[§121 Applications of Triple Integrals#^thm-121-1|Theorem §121.1]], with the same limits,
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

^ex-121-1

All the applications of double integrals in [[§118 Applications of Double Integrals|§118]] extend to triple integrals. If a solid occupying $E$ has density $\rho(x, y, z)$ (mass per unit volume), divide a box containing $E$ into sub-boxes $B_{ijk}$, let $\rho = 0$ outside $E$, and approximate the mass of the part in $B_{ijk}$ by $\rho(x_{ijk}^*, y_{ijk}^*, z_{ijk}^*)\,\Delta V$; adding and passing to the limit gives the following.

> [!definition] Definition §144.1: Mass of a Solid
> For a solid occupying $E$ with density $\rho(x, y, z)$:
>
> - the **mass** is $m = \displaystyle\lim_{l, m, n \to \infty} \sum_{i,j,k} \rho(x_{ijk}^{\ast}, y_{ijk}^{\ast}, z_{ijk}^{\ast})\,\Delta V = \iiint_E \rho(x, y, z)\,dV$; (13)
>
> *Stewart: 15.6, Equations 13, 14, 15 and 16*

^def-121-1

> [!definition] Definition §144.2: Moments of a Solid
> For a solid occupying $E$ with density $\rho(x, y, z)$:
>
> - the **moments** about the three coordinate planes are
>
> $$
> M_{yz} = \iiint_E x\,\rho\,dV , \qquad M_{xz} = \iiint_E y\,\rho\,dV , \qquad M_{xy} = \iiint_E z\,\rho\,dV ; \qquad (14)
> $$
>
> *Stewart: 15.6, Equations 13, 14, 15 and 16*

^def-121-2

> [!definition] Definition §144.3: Center of Mass of a Solid
> For a solid occupying $E$ with density $\rho(x, y, z)$, mass $m$ and moments $M_{yz}$, $M_{xz}$, $M_{xy}$:
>
> - the **center of mass** is $(\bar x, \bar y, \bar z)$ with $\bar x = M_{yz}/m$, $\bar y = M_{xz}/m$, $\bar z = M_{xy}/m$ (15); for constant density it is called the **centroid** of $E$;
>
> *Stewart: 15.6, Equations 13, 14, 15 and 16*

^def-121-3

> [!definition] Definition §144.4: Moments of Inertia of a Solid
> For a solid occupying $E$ with density $\rho(x, y, z)$:
>
> - the **moments of inertia** about the three coordinate axes are
>
> $$
> I_x = \iiint_E (y^2 + z^2)\rho\,dV , \qquad I_y = \iiint_E (x^2 + z^2)\rho\,dV , \qquad I_z = \iiint_E (x^2 + y^2)\rho\,dV . \qquad (16)
> $$
>
> *Stewart: 15.6, Equations 13, 14, 15 and 16*

^def-121-4

> [!definition] Definition §145.1: Electric Charge of a Solid
> Likewise, a charge density $\sigma(x, y, z)$ gives the total **electric charge** $Q = \iiint_E \sigma\,dV$.
>
> *Stewart: 15.6, Equations 13, 14, 15 and 16*

^def-121-5

> [!definition] Definition §145.2: Joint Density Function of Three Random Variables
> The **joint density function** of three [[§65 Probability#^def-65-1|continuous random variables]] $X$, $Y$, $Z$ is a function $f \ge 0$ with $P\big((X, Y, Z) \in E\big) = \iiint_E f\,dV$ and $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f\,dz\,dy\,dx = 1$; in particular $P(a \le X \le b,\ c \le Y \le d,\ r \le Z \le s) = \int_a^b \int_c^d \int_r^s f\,dz\,dy\,dx$.
>
> *Stewart: 15.6, Equations 13, 14, 15 and 16*

^def-121-6

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
