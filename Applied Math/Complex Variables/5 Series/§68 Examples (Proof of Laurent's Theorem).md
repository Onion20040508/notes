---
type: section
subject: "[[Complex Variables]]"
chapter: 5
section: 68
bc: "68"
aliases: ["B&C 68"]
tags: [complex-variables, math342]
---
← [[§67 Proof of Laurent's Theorem]] · ↑ [[· 5 Series]] · [[§69★ Absolute and Uniform Convergence of Power Series]] →

*Brown–Churchill, Section 68 · MAT 342 HW 10 · Practice Finals (Fall 2002, Spring 2005, Spring 2012).*

Laurent coefficients are almost never computed from the integrals of Laurent's theorem. Instead one manipulates the Maclaurin series of [[§64 Examples (Proof of Taylor's Theorem)#^prop-64-1|Proposition §64.1]] by substitution (often $z \mapsto 1/z$) and multiplication, as in [[§65 Negative Powers of (z − z₀)|§65]] and [[§67 Proof of Laurent's Theorem#^rem-67-1|Remark: Method — Laurent Series in an Annulus]]. Two facts make this legitimate. First, Laurent's theorem ([[§67 Proof of Laurent's Theorem#^thm-67-1|Theorem §67.1]]) predicts the domain: the series of [[§65 Negative Powers of (z − z₀)|§65]] are valid in punctured disks or punctured planes because the functions there have a single singular point at the center, or a nearest one at the outer radius. Second, any convergent series in powers of $z - z_0$ that represents $f$ in an annulus *is* the Laurent series there ([[§72★ Uniqueness of Series Representations#^thm-72-4|Theorem §72.4]], deferred to §72). The integral formula is still useful, but in the opposite direction: once the series is known, its coefficient $b_1$ evaluates $\int_C f(z)\,dz$. This is the idea that Chapter 6 develops into the residue theorem.

> [!example] Example §68.1: One Function Inside and Outside the Unit Circle
> **Problem.** The function
>
> $$
> f(z) = \frac{1}{z(1 + z^2)} = \frac1z\cdot\frac{1}{1 + z^2}
> $$
>
> has singular points $z = 0$ and $z = \pm i$. Find its Laurent series **(a)** in the punctured disk $0 < |z| < 1$ and **(b)** in $1 < |z| < \infty$.
>
> **(a)** Since $|-z^2| < 1$ when $|z| < 1$, substitute $-z^2$ for $z$ in the geometric series $\frac{1}{1 - z} = \sum_{n=0}^{\infty}z^n$ $(|z| < 1)$:
>
> $$
> \frac{1}{1 + z^2} = \sum_{n=0}^{\infty}(-1)^nz^{2n} \qquad (|z| < 1), \qquad\text{so}\qquad f(z) = \frac1z\sum_{n=0}^{\infty}(-1)^nz^{2n} = \sum_{n=0}^{\infty}(-1)^nz^{2n-1} \qquad (0 < |z| < 1) .
> $$
>
> Separating the $n = 0$ term and replacing $n$ by $n + 1$ in the rest, we get the standard form
>
> $$
> f(z) = \sum_{n=0}^{\infty}(-1)^{n+1}z^{2n+1} + \frac1z \qquad (0 < |z| < 1) .
> $$
>
> **(b)** Now $|z| > 1$, so $\big|-\frac{1}{z^2}\big| < 1$; factor out $z^2$ instead:
>
> $$
> f(z) = \frac{1}{z^3}\cdot\frac{1}{1 + \frac{1}{z^2}} = \frac{1}{z^3}\sum_{n=0}^{\infty}\Big(-\frac{1}{z^2}\Big)^n = \sum_{n=0}^{\infty}\frac{(-1)^n}{z^{2n+3}} = \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{z^{2n+1}} \qquad (1 < |z| < \infty) .
> $$
>
> In (b) the series has only negative powers, beginning with $1/z^3$: the coefficient of $1/z$ is $0$. In the exterior domain a contour $C$ around the origin encloses all three singular points $0, \pm i$, and their contributions to $b_1 = \frac{1}{2\pi i}\int_C f(z)\,dz$ cancel (Chapter 6 makes this precise: they are $1$, $-\frac12$, $-\frac12$). In (a) only the singular point $0$ is enclosed, and $b_1 = 1$.
>
> *B&C: Sec. 68, Example 1 and Exercise 3; Source: 342 HW 10*

^ex-68-1

> [!example] Example §68.2: (z + 1)/(z − 1) in the Disk and Outside It
> **Problem.** The function
>
> $$
> f(z) = \frac{z + 1}{z - 1} ,
> $$
>
> with the singular point $z = 1$, is analytic in the domains $D_1\colon |z| < 1$ and $D_2\colon 1 < |z| < \infty$. Find its series in powers of $z$ in each, and the radius of convergence of the first.
>
> **$D_1$.** The series is a Maclaurin series. Write
>
> $$
> f(z) = -(z + 1)\frac{1}{1 - z} = -z\frac{1}{1 - z} - \frac{1}{1 - z} = -\sum_{n=0}^{\infty}z^{n+1} - \sum_{n=0}^{\infty}z^n \qquad (|z| < 1) .
> $$
>
> Replacing $n$ by $n - 1$ in the first series,
>
> $$
> f(z) = -\sum_{n=1}^{\infty}z^n - \sum_{n=0}^{\infty}z^n = -1 - 2\sum_{n=1}^{\infty}z^n \qquad (|z| < 1) .
> $$
>
> The radius of convergence is $1$: the series converges for $|z| < 1$ by Taylor's theorem ($1$ is the distance to the singular point), and diverges for $|z| \ge 1$, where its terms $-2z^n$ do not tend to zero. (Equivalently, $f = 1 + \frac{2}{z - 1} = 1 - \frac{2}{1 - z}$.)
>
> **$D_2$.** Here $|1/z| < 1$, which suggests
>
> $$
> f(z) = \frac{1 + \frac1z}{1 - \frac1z} = \Big(1 + \frac1z\Big)\sum_{n=0}^{\infty}\frac{1}{z^n} = \sum_{n=0}^{\infty}\frac{1}{z^n} + \sum_{n=0}^{\infty}\frac{1}{z^{n+1}} \qquad (1 < |z| < \infty) .
> $$
>
> Substituting $n - 1$ for $n$ in the last series,
>
> $$
> f(z) = \sum_{n=0}^{\infty}\frac{1}{z^n} + \sum_{n=1}^{\infty}\frac{1}{z^n} = 1 + 2\sum_{n=1}^{\infty}\frac{1}{z^n} \qquad (1 < |z| < \infty) .
> $$
>
> The same function has a Maclaurin series in $D_1$ and a Laurent series with no positive powers in $D_2$.
>
> *The Fall 2002 key gives both series correctly but does not state the radius of convergence.*
>
> *B&C: Sec. 68, Example 2; Source: 342 practice final (Fall 2002), Q4*

^ex-68-2

> [!example] Example §68.3: Two Laurent Series of 1/(z²(1 − z))
> **Problem.** Give two Laurent series expansions in powers of $z$ for
>
> $$
> f(z) = \frac{1}{z^2(1 - z)} ,
> $$
>
> and specify the regions in which they are valid.
>
> The singular points are $0$ and $1$, so the regions are $0 < |z| < 1$ and $1 < |z| < \infty$.
>
> **$0 < |z| < 1$.**
>
> $$
> f(z) = \frac{1}{z^2}\sum_{n=0}^{\infty}z^n = \sum_{n=0}^{\infty}z^{n-2} = \frac{1}{z^2} + \frac1z + \sum_{n=0}^{\infty}z^n \qquad (0 < |z| < 1) .
> $$
>
> **$1 < |z| < \infty$.** Here $|1/z| < 1$ and
>
> $$
> f(z) = \frac{1}{z^2}\cdot\frac{-1}{z\big(1 - \frac1z\big)} = -\frac{1}{z^3}\sum_{n=0}^{\infty}\frac{1}{z^n} = -\sum_{n=3}^{\infty}\frac{1}{z^n} \qquad (1 < |z| < \infty) .
> $$
>
> *B&C: Sec. 68, Exercise 4; Source: 342 HW 10*

^ex-68-3

> [!example] Example §68.4: Laurent Coefficients Evaluate Integrals
> By Laurent's theorem, if $f$ is analytic in $0 < |z| < R_2$ and $C$ is a positively oriented simple closed contour around $0$ in that punctured disk, then
>
> $$
> \int_C f(z)\,dz = 2\pi i\,b_1, \qquad b_1 = \text{the coefficient of } \frac1z \text{ in the Laurent series of } f .
> $$
>
> **(a) $e^{1/z}$.** Replacing $z$ by $1/z$ in the Maclaurin series of $e^z$,
>
> $$
> e^{1/z} = \sum_{n=0}^{\infty}\frac{1}{n!\,z^n} = 1 + \frac{1}{1!\,z} + \frac{1}{2!\,z^2} + \frac{1}{3!\,z^3} + \cdots \qquad (0 < |z| < \infty) .
> $$
>
> No positive powers of $z$ appear, and the coefficient of $1/z$ is $1$. So
>
> $$
> \int_C e^{1/z}\,dz = 2\pi i
> $$
>
> for every positively oriented simple closed contour $C$ around the origin.
>
> **(b) Spring 2012.** With $C$ the unit circle, counterclockwise, evaluate
>
> $$
> \frac{1}{2\pi i}\int_C\Big(\frac{1}{z^2} + z + z^3\Big)e^{1/z}\,dz .
> $$
>
> The integrand $g(z)$ is analytic in $0 < |z| < \infty$, and the integral is the coefficient of $1/z$ in its Laurent series. Multiply the series of (a) by each of the three powers and add ([[§61 Convergence of Series#^prop-61-4|Proposition §61.4]]; the result is the Laurent series of $g$ by [[§72★ Uniqueness of Series Representations#^thm-72-4|Theorem §72.4]]). The term $z^{-2}\cdot z^{-n}/n!$ has exponent $-2 - n \le -2$, never $-1$; $z\cdot z^{-n}/n!$ has exponent $-1$ for $n = 2$; $z^3\cdot z^{-n}/n!$ has exponent $-1$ for $n = 4$. Hence
>
> $$
> \frac{1}{2\pi i}\int_C\Big(\frac{1}{z^2} + z + z^3\Big)e^{1/z}\,dz = 0 + \frac{1}{2!} + \frac{1}{4!} = \frac{13}{24}
> $$
>
> (numerical quadrature on the unit circle gives $0.5416667$).
>
> **(c) Spring 2005 and Fall 2002: integrals of $\sin\bar z$ and $e^{\bar z}$.** Let $C$ be the circle $|z| = 1$, counterclockwise.
> - *A conjugate becomes a reciprocal on the circle.* On $C$, $\bar z = e^{-i\theta} = 1/z$, so by the definition of contour integrals $\int_C\sin(\bar z)\,dz = \int_C\sin(1/z)\,dz$; this first part of the exam problem is worked in [[§44 Contour Integrals#^ex-44-4|Example §44.4]](b).
> - *The Laurent series.* From the Maclaurin series of $\sin z$,
>
>   $$
>   \sin\Big(\frac1z\Big) = \sum_{n=0}^{\infty}\frac{(-1)^n}{(2n + 1)!\,z^{2n+1}} = \frac1z - \frac{1}{3!\,z^3} + \frac{1}{5!\,z^5} - \cdots \qquad (0 < |z| < \infty),
>   $$
>
>   with infinitely many negative powers (an essential singular point, [[§78 The Three Types of Isolated Singular Points#^def-78-3|Definition §78.3]]).
> - *The integral.* $b_1 = 1$, so $\int_C\sin(\bar z)\,dz = \int_C\sin(1/z)\,dz = 2\pi i$.
>
> In the Fall 2002 version, $C$ is the circle $|z| = 2$; there $\bar z = 4/z$, so $\int_C e^{\bar z}\,dz = \int_C e^{4/z}\,dz$ ([[§44 Contour Integrals#^ex-44-4|Example §44.4]](a)). The series $e^{4/z} = \sum_{n=0}^{\infty}\frac{4^n}{n!\,z^n}$ $(0 < |z| < \infty)$ has $b_1 = 4$, and the integral is $8\pi i$.
>
> *B&C: Sec. 68, Example 3; Source: 342 practice final (Spring 2012), Q5; 342 practice final (Spring 2005), Q5; 342 practice final (Fall 2002), Q5*

^ex-68-4

> [!example] Example §68.5: A Function That Is Its Own Laurent Series
> The function $f(z) = 1/(z - i)^2$ is already in the form of a Laurent series about $z_0 = i$:
>
> $$
> \frac{1}{(z - i)^2} = \sum_{n=-\infty}^{\infty}c_n(z - i)^n \qquad (0 < |z - i| < \infty),
> $$
>
> with $c_{-2} = 1$ and all other coefficients zero (by uniqueness, [[§72★ Uniqueness of Series Representations#^thm-72-4|Theorem §72.4]]). By expression (5) of [[§66 Laurent Series#^def-66-1|Definition §66.1]],
>
> $$
> c_n = \frac{1}{2\pi i}\int_C\frac{dz}{(z - i)^{n+3}} \qquad (n = 0, \pm1, \pm2, \ldots),
> $$
>
> where $C$ is, for instance, any positively oriented circle $|z - i| = R$. Thus
>
> $$
> \int_C\frac{dz}{(z - i)^{n+3}} = \begin{cases} 0 & \text{when } n \ne -2, \\ 2\pi i & \text{when } n = -2 , \end{cases}
> $$
>
> which is the familiar integral $\int_C(z - z_0)^{m}\,dz$ ($m = -1$ gives $2\pi i$, every other integer $m$ gives $0$; [[§45 Some Examples (Contour Integrals)#^ex-45-5|Example §45.5]]), here read off from a Laurent series instead of computed.
>
> *B&C: Sec. 68, Example 4*

^ex-68-5
