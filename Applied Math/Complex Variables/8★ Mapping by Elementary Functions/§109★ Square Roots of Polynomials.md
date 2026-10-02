---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: 109
bc: "109"
aliases: ["B&C 109"]
tags: [complex-variables, math342, extension]
---
← [[§108★ Mappings by Branches of z^(1∕2)]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§110★ Riemann Surfaces]] →

*Brown–Churchill, Section 109.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Square roots of polynomials have several branch points, and the branch cuts can be chosen to join them to each other instead of running to infinity. For $(z^2 - 1)^{1/2}$ the product of suitable branches of $(z - 1)^{1/2}$ and $(z + 1)^{1/2}$ gives a branch $F$ that is analytic everywhere except on the segment $[-1, 1]$ between the branch points: going once around both branch points changes each factor's sign, so the product returns to its value. This $F$ maps the plane minus $[-1, 1]$ one to one onto the plane minus $[-i, i]$, carrying confocal ellipses and hyperbolas to confocal ellipses and hyperbolas. Every quadratic $(z^2 + Az + B)^{1/2}$ reduces to it by linear changes of variable. B&C notes that this and the next two sections are not used much later; they prepare the Riemann surfaces of [[§110★ Riemann Surfaces|§110]] and [[§111★ Surfaces for Related Functions|§111]].

## Square Roots of z − z₀

> [!example] Example §109.1: Branches of (z − z₀)^(1/2)
> The double-valued function $(z - z_0)^{1/2}$ is the translation $Z = z - z_0$ followed by $Z^{1/2}$, so each branch of $Z^{1/2}$ gives a branch of $(z - z_0)^{1/2}$. By [[§108★ Mappings by Branches of z^(1∕2)#^def-108-2|Definition §108.2]], when $Z = Re^{i\theta}$ the branches of $Z^{1/2}$ are $\sqrt R\exp\frac{i\theta}{2}$ ($R > 0$, $\alpha < \theta < \alpha + 2\pi$). With $R = |z - z_0|$, $\Theta = \operatorname{Arg}(z - z_0)$ and $\theta = \arg(z - z_0)$, two branches of $(z - z_0)^{1/2}$ are
>
> $$
> G_0(z) = \sqrt R\exp\frac{i\Theta}{2} \quad (R > 0,\ -\pi < \Theta < \pi) \qquad (1)
> $$
>
> and
>
> $$
> g_0(z) = \sqrt R\exp\frac{i\theta}{2} \quad (R > 0,\ 0 < \theta < 2\pi) . \qquad (2)
> $$
>
> The branch of $Z^{1/2}$ used for $G_0$ is defined except at $Z = 0$ and on the ray $\operatorname{Arg} Z = \pi$, and halves arguments in $(-\pi, \pi)$. So $w = G_0(z)$ maps the domain $|z - z_0| > 0$, $-\pi < \operatorname{Arg}(z - z_0) < \pi$ (the plane cut along the ray running left from $z_0$) one to one onto the right half plane $\operatorname{Re} w > 0$. Likewise $w = g_0(z)$ maps the domain $|z - z_0| > 0$, $0 < \arg(z - z_0) < 2\pi$ (cut along the ray running right from $z_0$) one to one onto the upper half plane $\operatorname{Im} w > 0$.
>
> *B&C: Sec. 109, Example 1*

^ex-109-1

## A Branch of (z² − 1)^(1/2) Cut Between ±1

For $z \ne \pm1$, $(z^2 - 1)^{1/2} = \exp\big[\tfrac12\log(z - 1) + \tfrac12\log(z + 1)\big]$, so

$$
(z^2 - 1)^{1/2} = (z - 1)^{1/2}(z + 1)^{1/2} \qquad (z \ne \pm1) . \qquad (3)
$$

> [!theorem] Proposition §109.1: Products of Branches
> If $f_1(z)$ is a branch of $(z - 1)^{1/2}$ defined on a domain $D_1$ and $f_2(z)$ is a branch of $(z + 1)^{1/2}$ defined on a domain $D_2$, then the product $f(z) = f_1(z)f_2(z)$ is a branch of $(z^2 - 1)^{1/2}$ defined at all points of $D_1 \cap D_2$.
>
> *B&C: Sec. 109 (text)*

^prop-109-1

> [!proof]+ Proof
> A branch is an analytic single-valued function whose values are values of the multiple-valued function ([[§33 Branches and Derivatives of Logarithms#^def-33-2|Definition §33.2]]); here that means $f_1^2 = z - 1$ on $D_1$ and $f_2^2 = z + 1$ on $D_2$. On $D_1 \cap D_2$ the product $f_1f_2$ is analytic and $(f_1f_2)^2 = (z - 1)(z + 1) = z^2 - 1$, so each value is one of the two values of $(z^2 - 1)^{1/2}$, as (3) says. (On each component of $D_1 \cap D_2$ it is a branch in the sense of a domain.)

^pf-109-1

*Uses:* [[§33 Branches and Derivatives of Logarithms#^def-33-2|Def. §33.2]]

Write $r_1 = |z - 1|$, $\theta_1 = \arg(z - 1)$, $r_2 = |z + 1|$, $\theta_2 = \arg(z + 1)$. Taking for both factors the branches of type (2),

$$
f_1(z) = \sqrt{r_1}\exp\frac{i\theta_1}{2} \ (r_1 > 0,\ 0 < \theta_1 < 2\pi), \qquad f_2(z) = \sqrt{r_2}\exp\frac{i\theta_2}{2} \ (r_2 > 0,\ 0 < \theta_2 < 2\pi) .
$$

> [!definition] Definition §109.1: The Branch F of (z² − 1)^(1/2)
> The product of the two branches above is the branch
>
> $$
> f(z) = \sqrt{r_1r_2}\exp\frac{i(\theta_1 + \theta_2)}{2} \qquad (r_k > 0,\ 0 < \theta_k < 2\pi,\ k = 1, 2) \qquad (4)
> $$
>
> of $(z^2 - 1)^{1/2}$, defined everywhere except on the ray $r_2 \ge 0$, $\theta_2 = 0$, which is the portion $x \ge -1$ of the $x$ axis. Its extension
>
> $$
> F(z) = \sqrt{r_1r_2}\exp\frac{i(\theta_1 + \theta_2)}{2} \qquad (r_k > 0,\ 0 \le \theta_k < 2\pi,\ k = 1, 2;\ r_1 + r_2 > 2) \qquad (5)
> $$
>
> is defined on the domain $D_z$ consisting of the whole $z$ plane except the segment $P_2P_1$, $-1 \le x \le 1$, of the $x$ axis. (By the triangle inequality $r_1 + r_2 \ge |(z + 1) - (z - 1)| = 2$, with equality exactly on that segment, so the condition $r_1 + r_2 > 2$ removes just the segment.)
>
> *B&C: Sec. 109, Example 2, Equations (4) and (5)*

^def-109-1

> [!theorem] Theorem §109.2: F Is Analytic off the Segment, and Only There
> The function $F$ of (5) is analytic everywhere in $D_z$. It cannot be extended to a function analytic at any point of the segment $-1 \le x \le 1$; at the interior points of the segment it cannot even be extended continuously.
>
> *B&C: Sec. 109, Example 2*

^thm-109-2

> [!proof]+ Proof
> **Off the ray $x \ge 1$.** On $\mathbb{C} \setminus [-1, \infty)$ the angles in (5) satisfy $0 < \theta_k < 2\pi$, so $F = f$ there, and $f = f_1f_2$ is analytic there by Example §109.1 and Proposition §109.1 ($f_1$ is analytic off $x \ge 1$, $f_2$ off $x \ge -1$).
>
> **Near the ray $r_1 > 0$, $\theta_1 = 0$ (that is, $x > 1$).** Form the product of the branches of type (1):
>
> $$
> G(z) = \sqrt{r_1r_2}\exp\frac{i(\Theta_1 + \Theta_2)}{2}, \qquad \Theta_1 = \operatorname{Arg}(z - 1),\ \Theta_2 = \operatorname{Arg}(z + 1),\ -\pi < \Theta_k < \pi .
> $$
>
> $G$ is analytic in the whole plane except the ray $x \le 1$ of the real axis (where $\Theta_1$ or $\Theta_2$ would be $\pi$). If $z$ lies above or on the ray $x > 1$, then $\theta_k = \Theta_k$ and $F(z) = G(z)$. If $z$ lies below the real axis, then $\theta_k = \Theta_k + 2\pi$, so $\exp(i\theta_k/2) = -\exp(i\Theta_k/2)$ for $k = 1, 2$, and
>
> $$
> \exp\frac{i(\theta_1 + \theta_2)}{2} = \Big(-\exp\frac{i\Theta_1}{2}\Big)\Big(-\exp\frac{i\Theta_2}{2}\Big) = \exp\frac{i(\Theta_1 + \Theta_2)}{2} :
> $$
>
> again $F(z) = G(z)$. So $F = G$ on the domain $\mathbb{C} \setminus (-\infty, 1]$, which contains the ray $x > 1$, and $G$ is analytic there.
>
> The two open sets $\mathbb{C} \setminus [-1, \infty)$ and $\mathbb{C} \setminus (-\infty, 1]$ cover $D_z$, and $F$ is analytic on each; analyticity is a local property, so $F$ is analytic on $D_z$.
>
> **No extension.** Let $-1 < x_0 < 1$. As $z$ approaches $x_0$ from above, $\theta_1 \to \pi$ and $\theta_2 \to 0$, so $F(z) \to \sqrt{r_1r_2}\,e^{i\pi/2} = i\sqrt{1 - x_0^2}$; from below, $\theta_1 \to \pi$ and $\theta_2 \to 2\pi$, so $F(z) \to \sqrt{r_1r_2}\,e^{3\pi i/2} = -i\sqrt{1 - x_0^2}$. Since $1 - x_0^2 > 0$ the two limits differ: the value jumps from $i\sqrt{r_1r_2}$ to numbers near $-i\sqrt{r_1r_2}$ as $z$ moves down across the segment, and no extension is continuous at $x_0$. At the endpoint $z = 1$ (similarly $-1$): an analytic extension would satisfy $F(z)^2 = z^2 - 1$ near $1$, hence $F(1) = 0$ and, differentiating, $2F(z)F'(z) = 2z$; at $z = 1$ this reads $0 = 2$, which is impossible.

^pf-109-2

*Uses:* [[§109★ Square Roots of Polynomials#^def-109-1|Def. §109.1]], [[§109★ Square Roots of Polynomials#^prop-109-1|§109.1]], [[§109★ Square Roots of Polynomials#^ex-109-1|Ex. §109.1]]

> [!theorem] Theorem §109.3: F Maps the Slit z Plane onto the Slit w Plane
> The transformation $w = F(z)$ is a one to one mapping of the domain $D_z$ (the $z$ plane minus the segment $-1 \le x \le 1$) onto the domain $D_w$ (the $w$ plane minus the segment $-1 \le v \le 1$ of the $v$ axis). Its inverse is the branch
>
> $$
> H(w) = \sqrt{\rho_1\rho_2}\exp\frac{i(\phi_1 + \phi_2)}{2} \qquad (6)
> $$
>
> of $(w^2 + 1)^{1/2} = (w - i)^{1/2}(w + i)^{1/2}$, where $w - i = \rho_1\exp(i\phi_1)$, $w + i = \rho_2\exp(i\phi_2)$, $\rho_k > 0$, $-\pi/2 \le \phi_k < 3\pi/2$ ($k = 1, 2$) and $\rho_1 + \rho_2 > 2$.
>
> *B&C: Sec. 109, Example 2*

^thm-109-3

> [!proof]+ Proof
> **How $F$ maps halves.** If $y > 0$, then $0 < \theta_1, \theta_2 < \pi$, so $0 < \frac12(\theta_1 + \theta_2) < \pi$ and $\operatorname{Im} F(z) > 0$. If $y < 0$, then $\pi < \theta_k < 2\pi$, so $\pi < \frac12(\theta_1 + \theta_2) < 2\pi$ and $\operatorname{Im} F(z) < 0$. On the ray $x > 1$, $\theta_1 = \theta_2 = 0$ and $F(z) = \sqrt{r_1r_2} > 0$; on the ray $x < -1$, $\theta_1 = \theta_2 = \pi$ and $F(z) = -\sqrt{r_1r_2} < 0$. On the positive $y$ axis, $r_1 = r_2 = \sqrt{1 + y^2} > 1$ and $\theta_1 + \theta_2 = \pi$, so $F(iy) = i\sqrt{1 + y^2}$: the positive $y$ axis goes onto the part $v > 1$ of the $v$ axis, and likewise the negative $y$ axis onto $v < -1$.
>
> **Into $D_w$.** $F(z)^2 = r_1r_2e^{i(\theta_1 + \theta_2)} = (z - 1)(z + 1) = z^2 - 1$. If $F(z) = iv$ with $-1 \le v \le 1$, then $z^2 = 1 - v^2 \in [0, 1]$ and $z \in [-1, 1]$, which is excluded. So $F(D_z) \subseteq D_w$.
>
> **One to one.** If $F(z_1) = F(z_2)$, then $z_1^2 - 1 = z_2^2 - 1$, so $z_1 = z_2$ or $z_1 = -z_2$. If $z_1 = -z_2 \ne z_2$, the two points lie in opposite half planes, or on the two opposite rays $x > 1$ and $x < -1$; by the first step their images then lie in opposite half planes or on opposite real rays, and cannot be equal. So $z_1 = z_2$.
>
> **Onto, with inverse $H$.** For $w \in D_w$ (so $w \ne \pm i$), $H(w)^2 = \rho_1\rho_2e^{i(\phi_1 + \phi_2)} = (w - i)(w + i) = w^2 + 1$. First, $H(w) \in D_z$: if $H(w) \in [-1, 1]$, then $w^2 = H(w)^2 - 1 \in [-1, 0]$ and $w \in [-i, i]$, which is excluded. Hence $F(H(w))$ is defined, and $F(H(w))^2 = H(w)^2 - 1 = w^2$, so $F(H(w)) = \pm w$. B&C concludes "$= w$" from the way $F$ and $H$ map the upper and lower halves of their domains. Here is a check that avoids the case analysis. The quotient
>
> $$
> q(w) = \frac{F(H(w))}{w} \qquad (w \in D_w,\ \text{note } 0 \notin D_w)
> $$
>
> takes only the values $\pm1$. It is continuous on $D_w$: $F$ is continuous on $D_z$ (Theorem §109.2), and $H$ is continuous on $D_w$, because $\phi_1$ jumps only where $w - i$ crosses the ray $\arg = -\pi/2$, which inside $D_w$ is the ray $u = 0$, $v < -1$, and $\phi_2$ jumps on exactly the same ray; crossing it, both change by $2\pi$, so $\frac12(\phi_1 + \phi_2)$ changes by $2\pi$ and the exponential in (6) does not change. $D_w$ is path connected, hence connected, and a continuous function from a connected space into $\{1, -1\}$ is constant. At $w = 1$: $\phi_1 = -\pi/4$, $\phi_2 = \pi/4$, $\rho_1\rho_2 = 2$, so $H(1) = \sqrt2$, and $F(\sqrt2) = \sqrt{(\sqrt2 - 1)(\sqrt2 + 1)} = 1$. So $q \equiv 1$, that is $F(H(w)) = w$ for every $w \in D_w$. Thus $F$ maps $D_z$ onto $D_w$, and since $F$ is one to one, $H = F^{-1}$.
>
> As a consequence $H$ maps points of $D_w$ above or below the $u$ axis onto points above or below the $x$ axis, the positive $u$ axis into $x > 1$ and the negative $u$ axis into $x < -1$, as B&C states.

^pf-109-3

*Uses:* [[§109★ Square Roots of Polynomials#^thm-109-2|§109.2]], [[§13 Connected Spaces#^thm-13-3|590 Thm. §13.3]] (continuous image of a connected space), [[§14 Connected Subspaces of ℝ#^thm-14-4|590 Thm. §14.4]] (path connected implies connected)

![[m342-109-1.svg]]
*$w = F(z)$, the branch (5) of $(z^2 - 1)^{1/2}$, maps the plane slit along $[-1, 1]$ (orange) onto the plane slit along $[-i, i]$. Writing $z = \cosh\zeta$ gives $F(z) = \sinh\zeta$ (checked numerically for $\operatorname{Re}\zeta > 0$, $0 < \operatorname{Im}\zeta < \pi$), so the ellipses $z = \cosh(c + it)$ with foci $\pm1$ (blue) go onto the ellipses $\sinh(c + it)$ with foci $\pm i$, and the confocal hyperbolas (red) onto confocal hyperbolas. The two edges of the slit $[-1, 1]$ open out into the slit $[-i, i]$.*

## General Quadratics

> [!theorem] Proposition §109.4: Reduction of (z² + Az + B)^(1/2)
> Let $z_1 \ne 0$. Mappings by branches of the double-valued function
>
> $$
> w = (z^2 + Az + B)^{1/2} = \big[(z - z_0)^2 - z_1^2\big]^{1/2}, \qquad A = -2z_0,\ B = z_0^2 - z_1^2 , \qquad (7)
> $$
>
> are the successive transformations
>
> $$
> Z = \frac{z - z_0}{z_1}, \qquad W = (Z^2 - 1)^{1/2}, \qquad w = z_1W . \qquad (8)
> $$
>
> In particular $w = z_1F\big((z - z_0)/z_1\big)$ is a branch of (7), analytic except on the segment joining the zeros $z_0 \pm z_1$, and it maps the complement of that segment one to one onto the $w$ plane minus the segment from $-iz_1$ to $iz_1$.
>
> *(B&C prints $B = z_0^2 = z_1^2$, p. 336; the correct relation is $B = z_0^2 - z_1^2$.)*
>
> *B&C: Sec. 109, Equations (7) and (8)*

^prop-109-4

> [!proof]+ Proof
> $(z - z_0)^2 - z_1^2 = z^2 - 2z_0z + z_0^2 - z_1^2$, which is $z^2 + Az + B$ with the stated $A$, $B$. With $Z = (z - z_0)/z_1$, $z_1^2(Z^2 - 1) = (z - z_0)^2 - z_1^2$, so if $W^2 = Z^2 - 1$ then $(z_1W)^2 = z^2 + Az + B$. The map $z \mapsto Z$ is linear and carries the segment from $z_0 - z_1$ to $z_0 + z_1$ onto $[-1, 1]$; $F$ maps the complement of $[-1, 1]$ one to one onto the complement of $[-i, i]$ (Theorem §109.3); and $W \mapsto z_1W$ carries $[-i, i]$ onto the segment from $-iz_1$ to $iz_1$. Analyticity follows from Theorem §109.2 and the chain rule.

^pf-109-4

*Uses:* [[§109★ Square Roots of Polynomials#^thm-109-2|§109.2]], [[§109★ Square Roots of Polynomials#^thm-109-3|§109.3]], [[§96★ Linear Transformations#^prop-96-1|§96.1]]

## Examples

> [!example] Example §109.2: The First Quadrant onto the First Quadrant
> **(a)** In terms of $r_1, r_2, \theta_1, \theta_2$, the conditions $r_1 > 0$, $0 < \theta_1 + \theta_2 < \pi$ describe the first quadrant $x > 0$, $y > 0$, and $w = F(z)$ maps it onto the first quadrant $u > 0$, $v > 0$.
>
> In the upper half plane $\theta_1 + \theta_2$ is continuous with values in $(0, 2\pi)$. It equals $\pi$ exactly on the positive $y$ axis: $e^{i(\theta_1 + \theta_2)} = (z^2 - 1)/|z^2 - 1|$ is $-1$ only when $z^2$ is real and less than $1$, which for $y > 0$ means $z = iy$. Along a ray $\theta_2 = c$ ($0 < c < \pi/2$), $\theta_1 + \theta_2$ decreases as $z$ moves to the right, tending to $2c < \pi$. So by continuity $\theta_1 + \theta_2 < \pi$ on the whole (connected) first quadrant, and $> \pi$ on the second; also $\theta_1 + \theta_2 > 0$ wherever $y > 0$. Hence the first quadrant is $\{r_1 > 0,\ 0 < \theta_1 + \theta_2 < \pi\}$. On it $\arg F = \frac12(\theta_1 + \theta_2) \in (0, \pi/2)$, so $F$ maps it into the first quadrant. Conversely, if $u, v > 0$, then $z = H(w)$ lies in the upper half plane and $\arg F(z) = \arg w \in (0, \pi/2)$ forces $\theta_1 + \theta_2 < \pi$, so $z$ is in the first quadrant.
>
> **(b)** For $z$ in the first quadrant, with $F(z) = u + iv$,
>
> $$
> u = \frac{1}{\sqrt2}\sqrt{r_1r_2 + x^2 - y^2 - 1}, \qquad v = \frac{1}{\sqrt2}\sqrt{r_1r_2 - x^2 + y^2 + 1}, \qquad (r_1r_2)^2 = (x^2 + y^2 + 1)^2 - 4x^2 .
> $$
>
> Indeed $u^2 - v^2 + 2iuv = F^2 = z^2 - 1 = (x^2 - y^2 - 1) + 2ixy$ and $u^2 + v^2 = |F|^2 = r_1r_2$; adding and subtracting $u^2 - v^2 = x^2 - y^2 - 1$ gives $u^2$ and $v^2$, and $u, v > 0$ fixes the signs. Also $(r_1r_2)^2 = \big[(x - 1)^2 + y^2\big]\big[(x + 1)^2 + y^2\big] = (x^2 + y^2 + 1 - 2x)(x^2 + y^2 + 1 + 2x)$. On the part of the hyperbola $x^2 - y^2 = 1$ in the first quadrant, $u = v = \sqrt{r_1r_2/2}$; as $z$ runs out along it from $1$, $r_1r_2$ increases from $0$ to $\infty$, so the image is the whole ray $v = u$, $u > 0$. (Checked numerically on random points of the quadrant.)
>
> *B&C: Sec. 109, Exercises 1 and 2*

^ex-109-2

> [!example] Example §109.3: A Branch of ((z − 1)/(z + 1))^(1/2) with the Same Cut
> Show that
>
> $$
> w = \Big(\frac{z - 1}{z + 1}\Big)^{1/2} = \sqrt{\frac{r_1}{r_2}}\exp\frac{i(\theta_1 - \theta_2)}{2} \qquad (0 \le \theta_k < 2\pi,\ r_1 + r_2 > 2)
> $$
>
> is a branch with the same domain $D_z$ and branch cut as $F$, that it maps $D_z$ onto the right half plane $\rho > 0$, $-\pi/2 < \phi < \pi/2$ (with $w = 1$ the image of $z = \infty$), and that the inverse is $z = \dfrac{1 + w^2}{1 - w^2}$ ($\operatorname{Re} w > 0$).
>
> Since $z + 1 = r_2e^{i\theta_2}$, the right side equals $F(z)/(z + 1)$, which is analytic on $D_z$ by Theorem §109.2, and its square is $\frac{r_1}{r_2}e^{i(\theta_1 - \theta_2)} = \frac{z - 1}{z + 1}$: a branch. The difference $\theta_1 - \theta_2$ is the signed angle at $z$ subtended by the segment from $-1$ to $1$: in $(0, \pi)$ for $y > 0$, in $(-\pi, 0)$ for $y < 0$, and $0$ on the rays $|x| > 1$. So $|\phi| = \frac12|\theta_1 - \theta_2| < \pi/2$ and $\operatorname{Re} w > 0$. Solving $w^2 = (z - 1)/(z + 1)$ gives $z = (1 + w^2)/(1 - w^2)$. Conversely, for $\operatorname{Re} w > 0$, $w \ne 1$, this $z$ is finite and not in $[-1, 1]$ (otherwise $w^2 = (z - 1)/(z + 1) \le 0$ and $\operatorname{Re} w = 0$); the branch value at $z$ is $\pm w$, and $\operatorname{Re} > 0$ forces $+w$. As $z \to \infty$, $w \to 1$. (This is the composite map of [[§108★ Mappings by Branches of z^(1∕2)#^ex-108-3|Example §108.3]]: both have positive real part and the same square.)
>
> *B&C: Sec. 109, Exercise 6*

^ex-109-3

> [!example] Example §109.4: A Branch of (z² − z₀²)^(1/2)
> Let $z_0 = r_0\exp(i\theta_0) \ne 0$. A branch of $(z^2 - z_0^2)^{1/2}$ whose branch cut is the segment between $z_0$ and $-z_0$ is
>
> $$
> F_0(z) = z_0F(Z), \qquad Z = \frac{z}{z_0} .
> $$
>
> This is Proposition §109.4 with center $0$ and $z_1 = z_0$: $\big(z_0F(Z)\big)^2 = z_0^2(Z^2 - 1) = z^2 - z_0^2$, and $Z = z/z_0$ lies on $[-1, 1]$ exactly when $z$ lies on the segment from $-z_0$ to $z_0$, so $F_0$ is analytic everywhere else.
>
> *B&C: Sec. 109, Exercise 4*

^ex-109-4
