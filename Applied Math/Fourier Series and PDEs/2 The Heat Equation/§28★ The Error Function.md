---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 2
section: 28
powers: "2.12"
aliases: ["Powers 2.12"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§27 Infinite Rod]] · ↑ [[· 2 The Heat Equation]] · [[§29 The Vibrating String]] →

*Powers, Section 2.12 · MAT 341 HW 9 · Midterm 2, Practice Midterm 2.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers. Examples §28.2–§28.4 revisit course problems (HW 9, Midterm 2, Practice Midterm 2) with the error function and Gaussian integrals.*

The heat-kernel solution of [[§27 Infinite Rod#^thm-27-3|Theorem §27.3]] is a single integral of the initial temperature against a Gaussian, but even for the simplest initial temperatures it cannot be carried out in closed form, because $\int e^{-x^2}dx$ is not an elementary function. This section names that integral, the error function, records its properties (including the value $\int_{-\infty}^\infty e^{-y^2}dy = \sqrt\pi$, proved with polar coordinates), and shows that it is itself a solution of the heat equation: $\operatorname{erf}(x/\sqrt{4kt})$ is the temperature in an infinite rod that starts at $-1$ on the left and $+1$ on the right, and its complement $\operatorname{erfc}(x/\sqrt{4kt})$ describes a semi-infinite body whose surface temperature is suddenly changed. Every piecewise constant initial temperature, and several of the course's Fourier-integral answers, then have closed forms. The combination $x/\sqrt{4kt}$ also explains the $\sqrt t$ law of heat penetration.

## The Error Function

In [[§27 Infinite Rod#^thm-27-3|Theorem §27.3]] the solution of the heat problem

$$
\frac{\partial^2u}{\partial x^2} = \frac1k\frac{\partial u}{\partial t}, \quad -\infty < x < \infty, \ 0 < t, \qquad u(x, 0) = f(x) \qquad (1)\text{–}(2)
$$

was transformed into the form of a single integral,

$$
u(x, t) = \frac{1}{\sqrt{4k\pi t}}\int_{-\infty}^\infty f(x')e^{-(x - x')^2/4kt}\,dx' . \qquad (3)
$$

> [!definition] Definition §28.1: Error Function
> The **error function** is
>
> $$
> \operatorname{erf}(z) = \frac{2}{\sqrt\pi}\int_0^z e^{-y^2}\,dy . \qquad (4)
> $$
>
> *Powers: 2.12, Eq. (4)*

^def-28-1

> [!definition] Definition §28.2: Complementary Error Function
> The **complementary error function** is
>
> $$
> \operatorname{erfc}(z) = \frac{2}{\sqrt\pi}\int_z^\infty e^{-y^2}\,dy . \qquad (9)
> $$
>
> *Powers: 2.12, Eq. (9)*

^def-28-2

> [!theorem] Proposition §28.1: Properties of the Error Function
> - (a) $\operatorname{erf}(0) = 0$, and $\operatorname{erf}$ is an odd function: $\operatorname{erf}(-z) = -\operatorname{erf}(z)$.
> - (b) $\dfrac{d}{dz}\operatorname{erf}(z) = \dfrac{2}{\sqrt\pi}e^{-z^2}$. $\qquad (5)$
> - (c) $\displaystyle\int_a^b e^{-y^2}\,dy = \frac{\sqrt\pi}{2}\big(\operatorname{erf}(b) - \operatorname{erf}(a)\big)$. $\qquad (6)$
> - (d) $\displaystyle\lim_{z \to \infty}\operatorname{erf}(z) = 1$; equivalently $\displaystyle\int_0^\infty e^{-y^2}\,dy = \frac{\sqrt\pi}{2}$ and $\displaystyle\int_{-\infty}^\infty e^{-y^2}\,dy = \sqrt\pi$. $\qquad (7)$
> - (e) $\operatorname{erfc}(z) = 1 - \operatorname{erf}(z)$. $\qquad (10)$
>
> *Powers: 2.12, Eqs. (5)–(10)*

^prop-28-1

> [!proof]+ Proof
> **(a)** $\operatorname{erf}(0)$ is an integral over an interval of length zero. Substituting $y = -\eta$ in $\operatorname{erf}(-z) = \frac{2}{\sqrt\pi}\int_0^{-z}e^{-y^2}dy$ gives $-\frac{2}{\sqrt\pi}\int_0^z e^{-\eta^2}d\eta = -\operatorname{erf}(z)$ (Powers' Exercise 2.12.1).
>
> **(b)** By the [[Fundamental Theorem of Calculus|fundamental theorem of calculus]], since $e^{-y^2}$ is continuous.
>
> **(c)** $\int_a^b = \int_0^b - \int_0^a$, and each is $\frac{\sqrt\pi}2\operatorname{erf}$ of its upper limit.
>
> **(d)** This is the reason for the constant $2/\sqrt\pi$ in (4). The integral $A = \int_0^\infty e^{-y^2}dy$ converges, since $0 < e^{-y^2} \le e^{-y}$ for $y \ge 1$. We show $A = \sqrt\pi/2$. Write $A^2$ as the product of two integrals,
>
> $$
> A^2 = \int_0^\infty e^{-y^2}dy\int_0^\infty e^{-x^2}dx ;
> $$
>
> the name of the variable of integration is immaterial. Powers interprets this as a double integral over the first quadrant of the $x,y$-plane and changes to polar coordinates ($0 < r < \infty$, $0 < \theta < \pi/2$, element of area $r\,dr\,d\theta$):
>
> $$
> A^2 = \int_0^\infty\int_0^\infty e^{-(x^2 + y^2)}\,dx\,dy = \int_0^{\pi/2}\int_0^\infty e^{-r^2}r\,dr\,d\theta . \qquad (8)
> $$
>
> (Powers asserts that the improper integrals may be handled this way; here is why.) For $R > 0$ let $S_R = [0, R]^2$ and let $D_\rho$ be the quarter disk $x, y \ge 0$, $x^2 + y^2 \le \rho^2$. Then $D_R \subset S_R \subset D_{R\sqrt2}$, and the integrand is positive, so
>
> $$
> \iint_{D_R} e^{-(x^2 + y^2)}\,dA \le \Big(\int_0^R e^{-x^2}dx\Big)^2 \le \iint_{D_{R\sqrt2}} e^{-(x^2 + y^2)}\,dA .
> $$
>
> On the bounded region $D_\rho$ the change to polar coordinates is legitimate, and the $r$-integral is elementary (Powers' Exercise 2.12.2):
>
> $$
> \iint_{D_\rho} e^{-(x^2 + y^2)}\,dA = \int_0^{\pi/2}\int_0^\rho e^{-r^2}r\,dr\,d\theta = \frac\pi2\cdot\frac{1 - e^{-\rho^2}}{2} = \frac\pi4\big(1 - e^{-\rho^2}\big) .
> $$
>
> As $R \to \infty$ both bounds tend to $\pi/4$, so $A^2 = \pi/4$ and $A = \sqrt\pi/2$. Hence $\operatorname{erf}(z) \to \frac{2}{\sqrt\pi}A = 1$, and by evenness $\int_{-\infty}^\infty e^{-y^2}dy = 2A = \sqrt\pi$.
>
> **(e)** $\operatorname{erfc}(z) = \frac{2}{\sqrt\pi}\big(\int_0^\infty - \int_0^z\big)e^{-y^2}dy = \frac{2}{\sqrt\pi}A - \operatorname{erf}(z) = 1 - \operatorname{erf}(z)$ by (d).

^pf-28-1

*Uses:* [[§28★ The Error Function#^def-28-1|Def. §28.1]], [[§28★ The Error Function#^def-28-2|Def. §28.2]], [[§100 Double Integrals in Polar Coordinates#^thm-100-1|Calc Thm. §100.1]], [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]] (FTC)

> [!remark]- Connections
> - The Gaussian integral via polar coordinates, with the improper double integral handled rigorously: [[§15 Multivariable Integration#^ex-15-7|452 Ex. §15.7]], using the change of variables [[§15 Multivariable Integration#^thm-15-7|452 Thm. §15.7]]; the computational version of the polar change: [[§100 Double Integrals in Polar Coordinates#^thm-100-1|Calc Thm. §100.1]].
> - $e^{-t^2}$ has no elementary antiderivative, but $\int_0^xe^{-t^2}dt = \frac{\sqrt\pi}{2}\operatorname{erf}(x)$ has a power series valid for all $x$: [[§26 Differentiation and Integration of Power Series#^ex-26-7|451 Ex. §26.7]].

> [!remark] Remark: More Properties
> From Proposition §28.1 (Powers' Exercises 2.12.3 and 2.12.6):
> - $\frac{d}{dz}\operatorname{erfc}(z) = -\frac{2}{\sqrt\pi}e^{-z^2}$, $\operatorname{erfc}(0) = 1$, $\lim_{z \to \infty}\operatorname{erfc}(z) = 0$, $\lim_{z \to -\infty}\operatorname{erfc}(z) = 2$, and $\operatorname{erfc}$ is neither even nor odd.
> - The distribution function of the standard normal distribution of probability ([[§56 Probability#^def-56-6|Calc Def. §56.6]]), $\Phi(x) = \int_{-\infty}^x \frac{1}{\sqrt{2\pi}}e^{-z^2/2}dz$, is $\Phi(x) = \frac12\big[1 + \operatorname{erf}(x/\sqrt2)\big]$.
> - Some values: $\operatorname{erf}(0.5) \approx 0.5205$, $\operatorname{erf}(1) \approx 0.8427$, $\operatorname{erf}(2) \approx 0.9953$; so $\operatorname{erf}(z)$ is within $0.5\%$ of $1$ once $z \ge 2$. Tables and approximations are in Abramowitz and Stegun, *Handbook of Mathematical Functions*.

^rem-28-1

## The Error Function Solves the Heat Equation

> [!theorem] Theorem §28.2: The Solution with Initial Temperature sgn x
> The solution of the problem
>
> $$
> \frac{\partial^2u}{\partial x^2} = \frac1k\frac{\partial u}{\partial t}, \quad -\infty < x < \infty, \ 0 < t, \qquad u(x, 0) = \operatorname{sgn}(x), \quad -\infty < x < \infty \qquad (11)\text{–}(12)
> $$
>
> is $u(x, t) = \operatorname{erf}\big(x/\sqrt{4kt}\big)$. (Here $\operatorname{sgn}(x) = -1$ for $x < 0$ and $+1$ for $x > 0$.)
>
> *Powers: 2.12 (text)*

^thm-28-2

> [!proof]+ Proof
> Start from (3), which applies to bounded $f$ even though $\int|\operatorname{sgn}| = \infty$ ([[§27 Infinite Rod#^rem-27-1|Remark in §27]]):
>
> $$
> u(x, t) = \frac{1}{\sqrt{4\pi kt}}\int_{-\infty}^\infty \operatorname{sgn}(x')e^{-(x - x')^2/4kt}\,dx' . \qquad (13)
> $$
>
> Change the variable of integration to $y = (x' - x)/\sqrt{4kt}$, so $dy = dx'/\sqrt{4kt}$ and $x' = x + y\sqrt{4kt}$:
>
> $$
> u(x, t) = \frac{1}{\sqrt\pi}\int_{-\infty}^\infty \operatorname{sgn}\big(x + y\sqrt{4kt}\big)e^{-y^2}\,dy . \qquad (14)
> $$
>
> Let $z = x/\sqrt{4kt}$. The function $e^{-y^2}$ is even, and the sgn factor changes from $-1$ to $+1$ at $y = -z$. So
>
> $$
> \sqrt\pi\,u = \int_{-z}^\infty e^{-y^2}dy - \int_{-\infty}^{-z}e^{-y^2}dy = \int_{-z}^{z}e^{-y^2}dy + \int_z^\infty e^{-y^2}dy - \int_{-\infty}^{-z}e^{-y^2}dy .
> $$
>
> By evenness, the tail to the left of $-z$ has the same area as the tail to the right of $z$; the two cancel (for $z < 0$ read $\int_{-z}^z$ as $-\int_z^{-z}$, and the same computation applies). Using the symmetry once more to halve the interval of integration and double the result,
>
> $$
> u(x, t) = \frac{1}{\sqrt\pi}\int_{-z}^{z}e^{-y^2}dy = \frac{2}{\sqrt\pi}\int_0^{x/\sqrt{4kt}}e^{-y^2}dy = \operatorname{erf}\big(x/\sqrt{4kt}\big) .
> $$
>
> **Direct check** (Powers' Exercises 2.12.4–2.12.5, "the easy way to prove this statement"). With $z = x/\sqrt{4kt}$ and (5): $u_x = \frac{2}{\sqrt\pi}e^{-z^2}\frac{1}{\sqrt{4kt}}$, $u_{xx} = -\frac{x}{2kt}u_x$, and $u_t = \frac{2}{\sqrt\pi}e^{-z^2}\frac{\partial z}{\partial t} = \frac{2}{\sqrt\pi}e^{-z^2}\Big(-\frac{x}{2t\sqrt{4kt}}\Big) = -\frac{x}{2t}u_x$. So $\frac1ku_t = u_{xx}$. As $t \to 0+$, $z \to +\infty$ for $x > 0$ and $z \to -\infty$ for $x < 0$, so $u \to \pm1 = \operatorname{sgn}(x)$ by Proposition §28.1(a), (d).

^pf-28-2

*Uses:* [[§27 Infinite Rod#^thm-27-3|§27.3]], [[§28★ The Error Function#^prop-28-1|§28.1]], [[§28★ The Error Function#^def-28-1|Def. §28.1]]

![[m341-28-1.svg]]
*The solution $u(x, t) = \operatorname{erf}(x/\sqrt{4kt})$ of Theorem §28.2 on $-2 < x < 2$ for $kt = 0.01$, $0.1$, $1$ and $10$; the initial temperature $\operatorname{sgn}(x)$ is dashed. Every curve passes through the origin with slope $1/\sqrt{\pi kt}$, and as $kt$ increases the graph collapses toward the $x$-axis. The curve for $kt = \frac14$ (not drawn) is the graph of $\operatorname{erf}$ itself.*

> [!theorem] Corollary §28.3: The Semi-Infinite Rod with Constant Data
> - (a) $u(x, t) = \operatorname{erf}\big(x/\sqrt{4kt}\big)$ is the solution of $u_{xx} = \frac1ku_t$, $0 < x$, $0 < t$, with $u(0, t) = 0$ and $u(x, 0) = 1$ for $0 < x$.
> - (b) $u(x, t) = \operatorname{erfc}\big(x/\sqrt{4kt}\big)$ is the solution with zero initial condition and constant boundary condition: $u(0, t) = 1$, $u(x, 0) = 0$ for $0 < x$.
>
> *Powers: 2.12 (text)*

^cor-28-3

> [!proof]+ Proof
> **(a)** Restrict the solution of Theorem §28.2 to $x > 0$. It satisfies the heat equation there, $u(0, t) = \operatorname{erf}(0) = 0$ (Proposition §28.1(a)), and its initial value is $\operatorname{sgn}(x) = 1$ for $x > 0$. (Equivalently: [[§27 Infinite Rod#^prop-27-4|Proposition §27.4]] with $f \equiv 1$, whose odd extension is $\operatorname{sgn}$.)
>
> **(b)** Constants solve the heat equation and the equation is linear, so $1 - \operatorname{erf}(x/\sqrt{4kt}) = \operatorname{erfc}(x/\sqrt{4kt})$ (Proposition §28.1(e)) solves it too; its boundary value is $1 - 0 = 1$ and its initial value is $1 - 1 = 0$.

^pf-28-3

*Uses:* [[§28★ The Error Function#^thm-28-2|§28.2]], [[§28★ The Error Function#^prop-28-1|§28.1]], [[§27 Infinite Rod#^prop-27-4|§27.4]]

> [!remark] Remark: How Fast Heat Penetrates
> Corollary §28.3(b) is the temperature in a deep body at uniform temperature $0$ whose surface is suddenly held at temperature $1$. The solution depends on $x$ and $t$ only through $x/\sqrt{4kt}$. At the depth $x = \sqrt{4kt}$ the temperature has risen to $\operatorname{erfc}(1) \approx 0.157$ of the surface value, and at $x = 2\sqrt{4kt}$ to only $\operatorname{erfc}(2) \approx 0.005$. So a change at the surface is felt to a depth proportional to $\sqrt{kt}$: going twice as deep takes four times as long. For soil, with $k \approx 0.5 \times 10^{-6}\ \mathrm{m^2/s}$ (the value in Powers' Exercise 2.10.6), $\sqrt{4kt}$ is about $0.4$ m after one day and about $8$ m after one year. The same law, with $u = U_b + (U_i - U_b)\operatorname{erf}(x/\sqrt{4kt})$, describes a lake surface held at the freezing temperature $U_b$ (Powers' Exercises 2.12.8–2.12.9): the freezing front, where $u = 0$, moves down like $\sqrt t$.

^rem-28-2

## Examples

> [!example] Example §28.1: The Heated Sections in Closed Form
> **(a) A block on the infinite rod.** If $f = T_0$ on $c < x < d$ and $0$ elsewhere, (3) and the substitution $y = (x' - x)/\sqrt{4kt}$ give
>
> $$
> u(x, t) = \frac{T_0}{\sqrt{4\pi kt}}\int_c^d e^{-(x' - x)^2/4kt}\,dx' = \frac{T_0}{\sqrt\pi}\int_{(c - x)/\sqrt{4kt}}^{(d - x)/\sqrt{4kt}}e^{-y^2}dy = \frac{T_0}{2}\Big[\operatorname{erf}\frac{d - x}{\sqrt{4kt}} - \operatorname{erf}\frac{c - x}{\sqrt{4kt}}\Big]
> $$
>
> by (6). For the hot center section of [[§27 Infinite Rod#^ex-27-1|Example §27.1]] ($c = -a$, $d = a$), formula (8) of [[§27 Infinite Rod#^rem-27-1|§27]] becomes, by oddness,
>
> $$
> u(x, t) = \frac{T_0}{2}\Big[\operatorname{erf}\frac{a - x}{\sqrt{4kt}} + \operatorname{erf}\frac{a + x}{\sqrt{4kt}}\Big] .
> $$
>
> At the center, $u(0, t) = T_0\operatorname{erf}(a/\sqrt{4kt})$; for $kt/a^2 = 1$ this is $T_0\operatorname{erf}(0.5) \approx 0.52T_0$.
>
> **(b) A block at the end of a semi-infinite rod.** For [[§26 Semi-Infinite Rod#^ex-26-1|Example §26.1]] ($f = T_0$ on $0 < x < b$, $u(0, t) = 0$), [[§27 Infinite Rod#^prop-27-4|Proposition §27.4]] amounts to applying (a) to the odd extension, $T_0$ on $(0, b)$ and $-T_0$ on $(-b, 0)$. With $s = \sqrt{4kt}$,
>
> $$
> u = \frac{T_0}{2}\Big[\operatorname{erf}\frac{b - x}{s} + \operatorname{erf}\frac{x}{s}\Big] - \frac{T_0}{2}\Big[\operatorname{erf}\frac{x + b}{s} - \operatorname{erf}\frac{x}{s}\Big] = T_0\Big[\operatorname{erf}\frac{x}{s} - \frac12\operatorname{erf}\frac{x - b}{s} - \frac12\operatorname{erf}\frac{x + b}{s}\Big] .
> $$
>
> This closed form agrees numerically with the Fourier sine integral of [[§26 Semi-Infinite Rod#^ex-26-1|Example §26.1]] (for instance both give $0.1310T_0$ at $x = 1.5b$, $kt = 0.1b^2$), and it was used to draw the figures there and in §27.
>
> *Powers: 2.11, Example and Eq. (8); 2.10, Example*

^ex-28-1

> [!example] Example §28.2: A Fourier Integral Evaluated
> In [[§27 Infinite Rod#^ex-27-3|Example §27.3]](a), $u_t = u_{xx}$ on the infinite rod with $u(x, 0) = 1$ on $0 < x < \pi$ and $0$ elsewhere, the Fourier integral solution was
>
> $$
> u(x, t) = \frac1\pi\int_0^\infty \frac{\sin(\lambda x) + \sin\big(\lambda(\pi - x)\big)}{\lambda}\,e^{-\lambda^2t}\,d\lambda .
> $$
>
> By Example §28.1(a) with $T_0 = 1$, $c = 0$, $d = \pi$, $k = 1$, the same function is
>
> $$
> u(x, t) = \frac12\Big[\operatorname{erf}\frac{x}{2\sqrt t} + \operatorname{erf}\frac{\pi - x}{2\sqrt t}\Big] .
> $$
>
> The two forms agree (for instance both give $0.7404$ at $x = 0.5$, $t = 0.3$). The closed form shows at a glance the symmetry about $x = \pi/2$, the values $u \to 1$ inside and $u \to 0$ outside the block as $t \to 0+$, and $u(0, t) = \frac12\operatorname{erf}(\pi/2\sqrt t)$, which tends to $\frac12$ as $t \to 0+$, the average at the jump.
>
> *Source: 341 HW 9, Problem 3*

^ex-28-2

> [!example] Example §28.3: The Midterm Problem in Closed Form
> For [[§27 Infinite Rod#^ex-27-2|Example §27.2]], $u_t = u_{xx}$ with $u(x, 0) = e^{-x}$ for $x > 0$ and $0$ for $x < 0$, (3) gives
>
> $$
> u(x, t) = \frac{1}{\sqrt{4\pi t}}\int_0^\infty e^{-x'}e^{-(x' - x)^2/4t}\,dx' .
> $$
>
> Complete the square in the exponent: $x' + \frac{(x' - x)^2}{4t} = \frac{(x' - x + 2t)^2}{4t} + x - t$. With $y = (x' - x + 2t)/\sqrt{4t}$,
>
> $$
> u(x, t) = e^{t - x}\frac{1}{\sqrt\pi}\int_{(2t - x)/\sqrt{4t}}^\infty e^{-y^2}\,dy = \frac12e^{t - x}\operatorname{erfc}\Big(\frac{2t - x}{\sqrt{4t}}\Big) .
> $$
>
> Checks: as $t \to 0+$, the argument of erfc tends to $-\infty$ for $x > 0$ (erfc $\to 2$, $u \to e^{-x}$) and to $+\infty$ for $x < 0$ ($u \to 0$). Numerically the closed form agrees with the Fourier integral of [[§27 Infinite Rod#^ex-27-2|Example §27.2]] (both give $0.3673$ at $x = 0.5$, $t = 0.3$). For large $t$ the solution approaches $\frac{1}{\sqrt{4\pi t}}e^{-x^2/4t}$, the heat kernel times the total initial heat $\int f = 1$.
>
> *Source: 341 Midterm 2, Q2*

^ex-28-3

> [!example] Example §28.4: Energy and Entropy of a Spreading Gaussian
> Let $u$ satisfy $u_t = u_{xx}$ on the infinite rod, $u$ bounded, with $u(x, 0) = f_1(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$, the Gaussian distribution with $\sigma = 1$. Find $u$, and compute the energy $E(t) = \int_{-\infty}^\infty u\,dx$ and the entropy $H(t) = -\int_{-\infty}^\infty u\log u\,dx$.
>
> **(a) Solution.** Exactly as in [[§27 Infinite Rod#^ex-27-4|Example §27.4]], the variance grows by $2t$:
>
> $$
> u(x, t) = f_{\sigma(t)}(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-x^2/2\sigma^2}, \qquad \sigma^2 = 1 + 2t .
> $$
>
> **(b) Two Gaussian integrals.** With $x = \sqrt2\sigma y$ and Proposition §28.1(d),
>
> $$
> \int_{-\infty}^\infty e^{-x^2/2\sigma^2}dx = \sqrt2\sigma\sqrt\pi, \qquad \int_{-\infty}^\infty x^2e^{-x^2/2\sigma^2}dx = (\sqrt2\sigma)^3\int_{-\infty}^\infty y^2e^{-y^2}dy = 2\sqrt2\sigma^3\cdot\frac{\sqrt\pi}{2} = \sqrt{2\pi}\,\sigma^3 ,
> $$
>
> where $\int y^2e^{-y^2}dy = \big[-\frac y2e^{-y^2}\big]_{-\infty}^\infty + \frac12\int e^{-y^2}dy = \frac{\sqrt\pi}{2}$ by parts.
>
> **Energy.** $E(t) = \frac{1}{\sqrt{2\pi\sigma^2}}\sqrt{2\pi}\,\sigma = 1$ for all $t$: heat is conserved.
>
> **Entropy.** $\log u = -\frac12\log(2\pi\sigma^2) - \frac{x^2}{2\sigma^2}$, so
>
> $$
> H(t) = \frac12\log(2\pi\sigma^2)\int u\,dx + \frac{1}{2\sigma^2}\int x^2u\,dx = \frac12\log(2\pi\sigma^2) + \frac12 = \frac12\big(\log 2\pi + \log(1 + 2t)\big) + \frac12 ,
> $$
>
> using $\int x^2u\,dx = \frac{1}{\sqrt{2\pi\sigma^2}}\sqrt{2\pi}\sigma^3 = \sigma^2$. The entropy increases monotonically with $t$, as the second law of thermodynamics requires of heat flow, while the energy stays constant.
>
> *The problem defines $H(t) = \int u\log u\,dx$ without the minus sign; the key computes $-\int u\log u\,dx$, as here. With the problem's sign, $H$ decreases monotonically.*
>
> *Source: 341 Practice Midterm 2, Q10(a)–(b) (bonus)*

^ex-28-4
