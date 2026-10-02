---
type: section
subject: "[[Complex Variables]]"
chapter: 12
section: 136
bc: "136"
aliases: ["B&C 136"]
tags: [complex-variables, math342, extension]
---
← [[§135★ Dirichlet Problem for a Disk]] · ↑ [[· 12★ Integral Formulas of the Poisson Type]] · [[§137★ Related Boundary Value Problems]] →

*Brown–Churchill, Section 136.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

These examples use the two forms of the solution of the Dirichlet problem for a disk from [[§135★ Dirichlet Problem for a Disk|§135★]]. For boundary values that are constant on arcs, the Poisson integral can be evaluated with an explicit antiderivative of the kernel, and the answer comes out as an arctangent whose level curves are circular arcs through the ends of the arcs; this reproduces by integration what [[§123★ Examples (Electrostatic Potential)|§123★]] found by conformal mapping. For a boundary value like $A\cos\theta$ the series form gives the answer at once. Physically: the potential inside a split cylinder, and steady temperatures in a cylinder or a plate heated along an arc.

> [!theorem] Lemma §136.1: An Antiderivative of the Poisson Kernel
> For $0 \le r < 1$,
>
> $$
> \int P(1, r, \psi)\,d\psi = 2\arctan\Big(\frac{1 + r}{1 - r}\tan\frac\psi2\Big) , \qquad (2)
> $$
>
> where $P(1, r, \psi) = \dfrac{1 - r^2}{1 + r^2 - 2r\cos\psi}$: the right side is an antiderivative of $P$ on each interval containing no odd multiple of $\pi$. At $\psi = \pi$ (mod $2\pi$) it jumps by $-2\pi$.
>
> *B&C: Sec. 136, equation (2) and Exercise 3*

^lem-136-1

> [!proof]+ Proof
> Let $c = (1 + r)/(1 - r)$ and differentiate the right side with respect to $\psi$:
>
> $$
> \frac{d}{d\psi}2\arctan\Big(c\tan\frac\psi2\Big) = \frac{2}{1 + c^2\tan^2(\psi/2)}\cdot\frac c2\sec^2\frac\psi2 = \frac{c}{\cos^2(\psi/2) + c^2\sin^2(\psi/2)} .
> $$
>
> With $\cos^2\frac\psi2 = \frac{1 + \cos\psi}{2}$ and $\sin^2\frac\psi2 = \frac{1 - \cos\psi}{2}$ the denominator is $\frac12\big[(1 + c^2) + (1 - c^2)\cos\psi\big]$. Multiply numerator and denominator by $(1 - r)^2$: since $c(1 - r)^2 = 1 - r^2$, $(1 + c^2)(1 - r)^2 = 2(1 + r^2)$ and $(1 - c^2)(1 - r)^2 = -4r$,
>
> $$
> \frac{2c}{(1 + c^2) + (1 - c^2)\cos\psi} = \frac{2(1 - r^2)}{2(1 + r^2) - 4r\cos\psi} = P(1, r, \psi) .
> $$
>
> As $\psi \to \pi^-$, $\tan(\psi/2) \to +\infty$ and the right side of (2) tends to $\pi$; as $\psi \to \pi^+$ it tends to $-\pi$.

^pf-136-1

*Uses:* [[§134★ Poisson Integral Formula#^def-134-2|Def. §134.2]]

> [!example] Example §136.1: A Split Cylinder
> Find the potential $V(r, \theta)$ inside a long hollow circular cylinder of unit radius, split lengthwise into two equal parts, when $V = 0$ on the upper half of the boundary $r = 1$ and $V = 1$ on the lower half.
>
> **The integral.** In (1) of [[§135★ Dirichlet Problem for a Disk#^def-135-1|Definition §135.1]] write $V$ for $U$, $r_0 = 1$, and $F(\phi) = 0$ for $0 < \phi < \pi$, $F(\phi) = 1$ for $\pi < \phi < 2\pi$:
>
> $$
> V(r, \theta) = \frac{1}{2\pi}\int_\pi^{2\pi}P(1, r, \phi - \theta)\,d\phi = \frac{1}{2\pi}\int_{\pi - \theta}^{2\pi - \theta}P(1, r, \psi)\,d\psi . \qquad (1)
> $$
>
> **The antiderivative.** By Lemma §136.1, with $c = (1 + r)/(1 - r)$,
>
> $$
> \pi V(r, \theta) = \arctan\Big(c\tan\frac{2\pi - \theta}{2}\Big) - \arctan\Big(c\tan\frac{\pi - \theta}{2}\Big)
> $$
>
> up to an added multiple of $\pi$: the interval of integration may contain an odd multiple of $\pi$, where the antiderivative jumps by $2\pi$, and half of that is $\pi$. That does not affect $\tan\pi V$.
>
> **Simplifying.** (B&C's Exercise 4.) Call the two arctangents $\alpha$ and $\beta$. Then $\tan\alpha = c\tan(\pi - \frac\theta2) = -c\tan\frac\theta2$ and $\tan\beta = c\tan(\frac\pi2 - \frac\theta2) = c\cot\frac\theta2$. By $\tan(\alpha - \beta) = \frac{\tan\alpha - \tan\beta}{1 + \tan\alpha\tan\beta}$ and $\tan x + \cot x = \frac{2}{\sin2x}$,
>
> $$
> \tan\pi V = \frac{-c\big(\tan\frac\theta2 + \cot\frac\theta2\big)}{1 - c^2} = \frac{-c}{1 - c^2}\cdot\frac{2}{\sin\theta} .
> $$
>
> Here $1 - c^2 = \frac{(1 - r)^2 - (1 + r)^2}{(1 - r)^2} = \frac{-4r}{(1 - r)^2}$, so $\frac{-c}{1 - c^2} = \frac{(1 + r)(1 - r)}{4r} = \frac{1 - r^2}{4r}$, and
>
> $$
> \tan\pi V = \frac{1 - r^2}{2r\sin\theta} .
> $$
>
> **The branch.** Since $P > 0$ and $P$ has mean $1$ ([[§134★ Poisson Integral Formula#^prop-134-2|Proposition §134.2]]), (1) gives $0 < V < 1$, so $\pi V$ is the angle in $(0, \pi)$ with the tangent just found:
>
> $$
> V(r, \theta) = \frac1\pi\arctan\Big(\frac{1 - r^2}{2r\sin\theta}\Big) \qquad (0 \le \arctan t \le \pi) . \qquad (3)
> $$
>
> B&C calls the restriction on the arctangent "physically evident"; the bounds $0 < V < 1$ make it a consequence of the kernel's properties. In the upper half, $\sin\theta > 0$ and $V < \frac12$; in the lower half $V > \frac12$; on the horizontal diameter $V = \frac12$ (with $\arctan(\pm\infty) = \pi/2$), as in [[§135★ Dirichlet Problem for a Disk#^ex-135-2|Example §135.2]].
>
> **Rectangular coordinates.** $\dfrac{1 - r^2}{2r\sin\theta} = \dfrac{1 - x^2 - y^2}{2y}$, so $V = \frac1\pi\arctan\dfrac{1 - x^2 - y^2}{2y}$, the solution (5) found by conformal mapping in [[§123★ Examples (Electrostatic Potential)|§123★]], Example 1.
>
> *Check:* at $r = 0.5$, $\theta = 1$, quadrature of (1) and formula (3) both give $V = 0.231725$; at $r = 0.3$, $\theta = 4$, both give $0.647326$.
>
> *B&C: Sec. 136, Example 1; Exercises 3 and 4*

^ex-136-1

> [!remark]- Connections
> - The same problem, rotated by a quarter turn ($V = 1$ on the right half), is [[§39 Potential in a Disk#^ex-39-1|341 Ex. §39.1]], solved there by the Fourier series of the boundary values and summed to $\frac12 + \frac1\pi\arg\frac{c + iz}{c - iz}$; its figure shows the circular level curves.

> [!example] Example §136.2: A Cylinder with Surface Temperature A cos θ
> Find the steady temperatures $T(r, \theta)$ in a solid cylinder $r \le r_0$ of infinite length when $T(r_0, \theta) = A\cos\theta$ for a constant $A$.
>
> **Series.** By (8)–(10) of [[§135★ Dirichlet Problem for a Disk#^prop-135-4|Proposition §135.4]] with $T$ for $U$,
>
> $$
> T(r, \theta) = \frac12a_0 + \sum_{n=1}^{\infty}\Big(\frac{r}{r_0}\Big)^n(a_n\cos n\theta + b_n\sin n\theta) \qquad (r < r_0) . \qquad (4)
> $$
>
> **Coefficients.** (B&C's Exercise 8.) $a_0 = \frac A\pi\int_0^{2\pi}\cos\phi\,d\phi = 0$. For $n \ge 1$, $2\cos\phi\cos n\phi = \cos(n - 1)\phi + \cos(n + 1)\phi$, and $\int_0^{2\pi}\cos k\phi\,d\phi$ is $2\pi$ for $k = 0$ and $0$ for $k \ge 1$, so
>
> $$
> a_n = \frac A\pi\int_0^{2\pi}\cos\phi\cos n\phi\,d\phi = \begin{cases} A & \text{if } n = 1, \\ 0 & \text{if } n > 1. \end{cases}
> $$
>
> And $2\cos\phi\sin n\phi = \sin(n + 1)\phi - \sin(1 - n)\phi$, whose integral over $[0, 2\pi]$ is $0$, so $b_n = 0$ for all $n$.
>
> **Solution.** Substituting into (4),
>
> $$
> T(r, \theta) = \frac{A}{r_0}(r\cos\theta) = \frac{A}{r_0}x . \qquad (5)
> $$
>
> It is harmonic (linear), equals $A\cos\theta$ on $r = r_0$, and has mean $0$ at the center. Since $\partial T/\partial y = 0$, no heat flows across the plane $y = 0$ ([[§118★ Steady Temperatures|§118★]]).
>
> *B&C: Sec. 136, Example 2; Exercise 8*

^ex-136-2

> [!example] Example §136.3: A Disk Heated along an Arc
> Let $T$ be the steady temperatures in a disk $r \le 1$ with insulated faces, when $T = 1$ on the arc $0 < \theta < 2\theta_0$ ($0 < \theta_0 < \pi/2$) of the edge and $T = 0$ on the rest of the edge. Show that
>
> $$
> T(x, y) = \frac1\pi\arctan\Big[\frac{(1 - x^2 - y^2)\,y_0}{(x - 1)^2 + (y - y_0)^2 - y_0^2}\Big] \qquad (0 \le \arctan t \le \pi) ,
> $$
>
> where $y_0 = \tan\theta_0$, and verify the boundary conditions. The case $\theta_0 = \pi/4$ ($y_0 = 1$), $V = 1$ on the first-quadrant arc, gives B&C's
>
> $$
> V(x, y) = \frac1\pi\arctan\Big[\frac{1 - x^2 - y^2}{(x - 1)^2 + (y - 1)^2 - 1}\Big] .
> $$
>
> **The integral.** As in Example §136.1, with $F = 1$ on $(0, 2\theta_0)$ and Lemma §136.1, up to a multiple of $\pi$,
>
> $$
> \pi T = \alpha - \beta, \qquad \tan\alpha = c\tan\Big(\theta_0 - \frac\theta2\Big), \qquad \tan\beta = c\tan\Big(-\frac\theta2\Big), \qquad c = \frac{1 + r}{1 - r} .
> $$
>
> **Simplifying.** Write $a = \theta_0 - \frac\theta2$ and $b = \frac\theta2$, so $a + b = \theta_0$. Then
>
> $$
> \tan\pi T = \frac{c(\tan a + \tan b)}{1 - c^2\tan a\tan b} = \frac{c\sin\theta_0}{\cos a\cos b - c^2\sin a\sin b} ,
> $$
>
> using $\tan a + \tan b = \frac{\sin(a + b)}{\cos a\cos b}$. With $\cos a\cos b = \frac12\big[\cos(\theta_0 - \theta) + \cos\theta_0\big]$ and $\sin a\sin b = \frac12\big[\cos(\theta_0 - \theta) - \cos\theta_0\big]$ (since $a - b = \theta_0 - \theta$), the denominator is $\frac12\big[(1 - c^2)\cos(\theta_0 - \theta) + (1 + c^2)\cos\theta_0\big]$. Multiplying by $(1 - r)^2$ as in Lemma §136.1,
>
> $$
> \tan\pi T = \frac{(1 - r^2)\sin\theta_0}{(1 + r^2)\cos\theta_0 - 2r\cos(\theta_0 - \theta)} = \frac{(1 - r^2)\,y_0}{1 + r^2 - 2r(\cos\theta + y_0\sin\theta)} ,
> $$
>
> dividing by $\cos\theta_0$. In rectangular coordinates the denominator is $1 + x^2 + y^2 - 2x - 2y_0y = (x - 1)^2 + (y - y_0)^2 - y_0^2$, which gives the formula; again $0 < T < 1$ fixes the arctangent in $[0, \pi]$.
>
> **Boundary conditions.** On $x^2 + y^2 = 1$ the numerator vanishes, and the denominator is $2 - 2(\cos\theta + y_0\sin\theta) = 2 - 2\cos(\theta - \theta_0)/\cos\theta_0$. It is negative exactly when $\cos(\theta - \theta_0) > \cos\theta_0$, that is, on the arc $0 < \theta < 2\theta_0$. Approaching the edge from inside, the numerator is small and positive, so $\tan\pi T \to 0^-$ on the arc, giving $\pi T \to \pi$, $T \to 1$; and $\tan\pi T \to 0^+$ off the arc, giving $T \to 0$. At the center $r = 0$ the formula gives $\tan\pi T = y_0 = \tan\theta_0$, so $T = \theta_0/\pi$, the fraction $2\theta_0/2\pi$ of the edge that is heated, as [[§135★ Dirichlet Problem for a Disk#^cor-135-2|Corollary §135.2]] requires.
>
> *Check:* at $(x, y) = (0.6, 0.6)$ with $\theta_0 = \pi/4$, quadrature of the Poisson integral and the formula both give $V = 0.875666$.
>
> *B&C: Sec. 136, Exercises 1 and 2*

^ex-136-3

![[m342-136-1.svg]]
*Level curves $V = 0.1, \ldots, 0.9$ of the potential in the unit disk with $V = 1$ on the first-quadrant arc (red) and $V = 0$ on the rest of the circle (blue), Example §136.3 with $\theta_0 = \pi/4$. Every level curve is a circular arc through the two points $1$ and $i$ where the boundary value jumps; the value at the center is $\frac14$.*
