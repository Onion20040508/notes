---
type: section
subject: "[[Complex Variables]]"
chapter: 10
section: 119
bc: "119"
aliases: ["B&C 119"]
tags: [complex-variables, math342, extension]
---
← [[§118★ Steady Temperatures]] · ↑ [[· 10★ Applications of Conformal Mapping]] · [[§120★ A Related Problem (Steady Temperatures in a Half Plane)]] →

*Brown–Churchill, Section 119 (with Exercises 9 and 10 of Section 121).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

The first application of the method of [[§117★ Transformations of Boundary Conditions#^rem-117-1|Remark: Method — Solving a Boundary Value Problem by Conformal Mapping]]: the steady temperature in a half plane whose edge is kept at temperature $1$ on a segment and $0$ elsewhere. A logarithm of a linear fractional map opens the half plane into a horizontal strip, with the hot segment going to one edge and the rest of the boundary to the other; in the strip the answer is a linear function of $v$. Back in the half plane the temperature at a point is the angle under which the hot segment is seen, divided by $\pi$, the isotherms are circular arcs through the ends of the segment, and the lines of flow are circles orthogonal to them. The bounded solution is unique, but without boundedness it is not.

## The Problem and Its Solution

> [!example] Example §119.1: A Half Plane with a Heated Segment
> Find the steady temperatures $T(x, y)$ in a thin semi-infinite plate $y \ge 0$ whose faces are insulated and whose edge $y = 0$ is kept at temperature $0$, except on the segment $-1 < x < 1$, where it is kept at temperature $1$ (B&C's Fig. 155). $T$ is to be bounded. (This is natural if the plate is regarded as the limit of plates $0 \le y \le y_0$ whose upper edge is kept at a fixed temperature, as $y_0 \to \infty$; it would even be reasonable to require $T \to 0$ as $y \to \infty$.)
>
> **The Dirichlet problem.**
>
> $$
> T_{xx}(x, y) + T_{yy}(x, y) = 0 \quad (-\infty < x < \infty,\ y > 0), \qquad (1)
> $$
>
> $$
> T(x, 0) = \begin{cases} 1 & \text{when } |x| < 1, \\ 0 & \text{when } |x| > 1, \end{cases} \qquad (2)
> $$
>
> and $|T(x, y)| < M$ for some constant $M$. The plan: map the half plane onto a region of the $uv$ plane by a transformation analytic for $y > 0$ and conformal on $y = 0$ except at $(\pm1, 0)$; solve the new Dirichlet problem there; and carry the solution back with Theorems [[§116★ Transformations of Harmonic Functions#^thm-116-1|§116.1]] and [[§117★ Transformations of Boundary Conditions#^thm-117-2|§117.2]]. (The same letter $T$ is used for the temperature in both planes.)
>
> **The map.** Write $z - 1 = r_1\exp(i\theta_1)$ and $z + 1 = r_2\exp(i\theta_2)$ with $0 \le \theta_k \le \pi$ $(k = 1, 2)$. The transformation
>
> $$
> w = \log\frac{z - 1}{z + 1} = \ln\frac{r_1}{r_2} + i(\theta_1 - \theta_2) \qquad \Big(\frac{r_1}{r_2} > 0,\ -\frac\pi2 < \theta_1 - \theta_2 < \frac{3\pi}{2}\Big) \qquad (3)
> $$
>
> is defined on the half plane $y \ge 0$ except at $z = \pm1$, since $0 \le \theta_1 - \theta_2 \le \pi$ when $y \ge 0$. There it is the principal logarithm of $(z - 1)/(z + 1)$, and the upper half plane $y > 0$ is mapped onto the horizontal strip $0 < v < \pi$ ([[§102★ Examples (Mappings of the Upper Half Plane)#^ex-102-3|Example §102.3]]): $\frac{z - 1}{z + 1}$ maps the upper half plane onto itself and $\operatorname{Log}$ maps that onto the strip. The segment $-1 < x < 1$, where $\theta_1 - \theta_2 = \pi$, goes onto the upper edge $v = \pi$; the rest of the $x$ axis, where $\theta_1 - \theta_2 = 0$, goes onto the lower edge $v = 0$. The map is analytic for $y > 0$ and conformal on $y = 0$ except at $\pm1$, since its derivative $\frac{2}{z^2 - 1}$ is never $0$.
>
> **Solution in the strip.** A bounded harmonic function of $u$ and $v$ that is $0$ on $v = 0$ and $1$ on $v = \pi$ is
>
> $$
> T = \frac1\pi v , \qquad (4)
> $$
>
> harmonic as the imaginary part of the entire function $\frac1\pi w$.
>
> **Back to $x$ and $y$.** By (3),
>
> $$
> w = \ln\left|\frac{z - 1}{z + 1}\right| + i\arg\left(\frac{z - 1}{z + 1}\right), \qquad (5)
> $$
>
> and
>
> $$
> v = \arg\frac{(z - 1)(\bar z + 1)}{(z + 1)(\bar z + 1)} = \arg\frac{x^2 + y^2 - 1 + i2y}{(x + 1)^2 + y^2} , \qquad\text{so}\qquad v = \arctan\Big(\frac{2y}{x^2 + y^2 - 1}\Big) ,
> $$
>
> where the arctangent takes values from $0$ to $\pi$, because $\arg\frac{z - 1}{z + 1} = \theta_1 - \theta_2$ and $0 \le \theta_1 - \theta_2 \le \pi$. (When $x^2 + y^2 = 1$ the quotient is undefined and $v = \pi/2$.) Hence
>
> $$
> T = \frac1\pi\arctan\Big(\frac{2y}{x^2 + y^2 - 1}\Big) \qquad (0 \le \arctan t \le \pi). \qquad (6)
> $$
>
> **Why it is the solution.** The function (4) is harmonic in the strip and (3) is analytic in $y > 0$, so (6) is harmonic in the half plane ([[§116★ Transformations of Harmonic Functions#^thm-116-1|Theorem §116.1]]). The boundary conditions are of the type $h = h_0$, so they are preserved on corresponding parts of the boundaries ([[§117★ Transformations of Boundary Conditions#^thm-117-2|Theorem §117.2]]). And $0 \le T \le 1$. Directly: as $(x, y)$ approaches a point of the segment $|x| < 1$ from above, $x^2 + y^2 - 1 < 0$ and $2y/(x^2 + y^2 - 1) \to 0^-$, so $T \to \frac1\pi\cdot\pi = 1$; near a point with $|x| > 1$ the quotient tends to $0^+$ and $T \to 0$.
>
> **Geometric form.** Since $T = (\theta_1 - \theta_2)/\pi$, and $\theta_1 - \theta_2$ is the angle at $z$ subtended by the segment from $-1$ to $1$, the temperature at a point is that angle divided by $\pi$. (This agrees with the half-plane Poisson integral $\frac1\pi\int_{-1}^{1}\frac{y}{y^2 + (x - s)^2}\,ds = \frac1\pi\big[\arctan\frac{x + 1}{y} - \arctan\frac{x - 1}{y}\big]$; numerically, at $(0.3, 0.5)$ both give $0.685693$, and at $(2, 1)$ both give $0.147584$.)
>
> **Isotherms.** $T = c_1$ $(0 < c_1 < 1)$ means $x^2 + y^2 - 1 = 2y\cot\pi c_1$, that is,
>
> $$
> x^2 + (y - \cot\pi c_1)^2 = \csc^2\pi c_1 ,
> $$
>
> arcs of circles through $(\pm1, 0)$ with centers on the $y$ axis (inscribed-angle theorem: the points from which the segment is seen at the angle $\pi c_1$).
>
> **Any temperature $T_0$.** A constant multiple of a harmonic function is harmonic, so $T = \frac{T_0}{\pi}\arctan\big(\frac{2y}{x^2 + y^2 - 1}\big)$ $(0 \le \arctan t \le \pi)$ gives the steady temperatures when the segment is kept at $T_0$ instead of $1$.
>
> *B&C: Sec. 119 (text)*

^ex-119-1

> [!remark]- Connections
> - The same Dirichlet problem by Fourier integrals: the half-plane Poisson formula $u = \frac1\pi\int f(s)\,\frac{y}{y^2 + (x - s)^2}\,ds$, [[§38 Potential in Unbounded Regions#^rem-38-2|341 Rem. §38.2]]; its example with a single jump at $0$ gives $\frac12 + \frac1\pi\arctan(x/y)$, the one-endpoint version of (6). B&C derives the half-plane formula in [[§139★ Dirichlet Problem for a Half Plane#^thm-139-1|Theorem §139.1]] (Chapter 12).

## Lines of Flow and Uniqueness

> [!example] Example §119.2: The Lines of Flow Are Circles
> For the temperature (6), find a harmonic conjugate from (5) and the lines of flow of heat.
>
> **Conjugate.** $T = \operatorname{Im}\frac1\pi w = \operatorname{Re}\big(-\frac i\pi w\big)$, and $-\frac i\pi w = \frac1\pi v - \frac i\pi u$. So
>
> $$
> S = -\frac1\pi u = -\frac1\pi\ln\left|\frac{z - 1}{z + 1}\right|
> $$
>
> is a harmonic conjugate of $T$ in $y > 0$.
>
> **Lines of flow.** $S = c_2$ means $|z - 1| = k|z + 1|$ with $k = e^{-\pi c_2} > 0$. For $k = 1$ this is the $y$ axis. For $k \ne 1$, squaring, $(x - 1)^2 + y^2 = k^2\big[(x + 1)^2 + y^2\big]$, which rearranges to
>
> $$
> x^2 + y^2 - 2\,\frac{1 + k^2}{1 - k^2}\,x + 1 = 0 , \qquad\text{a circle with center } \Big(\frac{1 + k^2}{1 - k^2}, 0\Big) \text{ and radius } \frac{2k}{|1 - k^2|} .
> $$
>
> For $k < 1$ the center is to the right of $1$ (on the segment $CD$ of the $x$ axis), for $k > 1$ to the left of $-1$ (on $AB$). So the lines of flow are the upper half of the $y$ axis and the upper halves of these circles; each circle separates $1$ from $-1$ and crosses the hot segment, so heat leaves the segment and travels along semicircles to the cold part of the edge. They cut the isotherms at right angles (Proposition [[§118★ Steady Temperatures#^prop-118-2|§118.2]]).
>
> *B&C: Sec. 121, Exercise 9*

^ex-119-2

![[m342-119-1.svg]]
*Example §119.1 and §119.2. Isotherms $T = 0.1, 0.2, \ldots, 0.9$ (blue), arcs of circles through $\pm1$ with centers on the $y$ axis; the hot segment $-1 < x < 1$ (red) is the isotherm $T = 1$. Lines of flow (orange), the $y$ axis and semicircles centered on the $x$ axis outside $[-1, 1]$, carry heat from the segment to the cold edge and cross every isotherm at right angles.*

> [!example] Example §119.3: Without Boundedness the Solution Is Not Unique
> Show that if $T$ is not required to be bounded, the function (4) in the strip can be replaced by
>
> $$
> T = \operatorname{Im}\Big(\frac1\pi w + A\cosh w\Big) = \frac1\pi v + A\sinh u\sin v ,
> $$
>
> $A$ any real constant, so that the Dirichlet problem for the strip (and hence for the half plane) does not have a unique solution.
>
> Since $\cosh(u + iv) = \cosh u\cos v + i\sinh u\sin v$ ([[§39★ Hyperbolic Functions#^prop-39-3|Proposition §39.3]]), the imaginary part is as stated; it is harmonic as the imaginary part of an entire function. On $v = 0$, $\sin v = 0$ and $T = 0$; on $v = \pi$, $\sin v = 0$ and $T = 1$. So every $A$ gives a solution of the strip problem, and composing with (3) a solution of the half-plane problem. For $A \ne 0$ it is unbounded: along $v = \pi/2$, $A\sinh u \to \pm\infty$ as $u \to \pm\infty$, which in the $z$ plane means near the points $z = \mp1$ (where $|(z - 1)/(z + 1)|$ tends to $\infty$ or $0$). The boundedness condition is what singles out (6).
>
> *B&C: Sec. 121, Exercise 10*

^ex-119-3
