---
type: section
subject: "[[Complex Variables]]"
chapter: 5
section: 66
bc: "66"
aliases: ["B&C 66"]
tags: [complex-variables, math342]
---
← [[§65 Negative Powers of (z − z₀)]] · ↑ [[· 5 Series]] · [[§67 Proof of Laurent's Theorem]] →

*Brown–Churchill, Section 66.*

Laurent's theorem is the version of Taylor's theorem for a function that is analytic only in an annulus $R_1 < |z - z_0| < R_2$: such a function is the sum of a series in positive *and* negative powers of $z - z_0$, and its coefficients are contour integrals over any simple closed contour around $z_0$ in the annulus. The most important case is a punctured disk $0 < |z - z_0| < R_2$ around an isolated singular point. There the coefficient $b_1$ of $1/(z - z_0)$ is $\frac{1}{2\pi i}\int_C f(z)\,dz$, which is the starting point of the theory of residues in Chapter 6. This section states the theorem and fixes the notation; the proof is in [[§67 Proof of Laurent's Theorem|§67]], and the examples below use the coefficient formula directly with the unit circle as contour, which turns Laurent coefficients into Fourier coefficients.

## Laurent's Theorem

**Laurent's theorem** ([[§67 Proof of Laurent's Theorem#^thm-67-1|Theorem §67.1]], proved in §67). *Suppose that a function $f$ is analytic throughout an annular domain $R_1 < |z - z_0| < R_2$, centered at $z_0$, and let $C$ denote any positively oriented simple closed contour around $z_0$ and lying in that domain. Then, at each point in the domain, $f(z)$ has the series representation*

$$
f(z) = \sum_{n=0}^{\infty} a_n(z - z_0)^n + \sum_{n=1}^{\infty}\frac{b_n}{(z - z_0)^n} \qquad (R_1 < |z - z_0| < R_2), \qquad (1)
$$

*where*

$$
a_n = \frac{1}{2\pi i}\int_C\frac{f(z)\,dz}{(z - z_0)^{n+1}} \quad (n = 0, 1, 2, \ldots), \qquad b_n = \frac{1}{2\pi i}\int_C\frac{f(z)\,dz}{(z - z_0)^{-n+1}} \quad (n = 1, 2, \ldots) . \qquad (2), (3)
$$

Here $R_1$ may be $0$ and $R_2$ may be $\infty$.

Replacing $n$ by $-n$ in the second series of (1) writes it as $\sum_{n=-\infty}^{-1} b_{-n}(z - z_0)^n$, where $b_{-n} = \frac{1}{2\pi i}\int_C\frac{f(z)\,dz}{(z - z_0)^{n+1}}$ $(n = -1, -2, \ldots)$, the same formula as for $a_n$. This motivates a single doubly infinite series.

> [!definition] Definition §66.1: Laurent Series
> Let $f$ be analytic in the annulus $R_1 < |z - z_0| < R_2$, and let $C$ be a positively oriented simple closed contour around $z_0$ lying in it. The **Laurent series** of $f$ in the annulus is the series
>
> $$
> f(z) = \sum_{n=-\infty}^{\infty} c_n(z - z_0)^n \qquad (R_1 < |z - z_0| < R_2), \qquad (4)
> $$
>
> with
>
> $$
> c_n = \frac{1}{2\pi i}\int_C\frac{f(z)\,dz}{(z - z_0)^{n+1}} \qquad (n = 0, \pm1, \pm2, \ldots) . \qquad (5)
> $$
>
> In the notation of (1), $c_n = a_n$ for $n \ge 0$ and $c_n = b_{-n}$ for $n \le -1$. Either form, (1) or (4), is called a Laurent series; a doubly infinite series $\sum_{n=-\infty}^{\infty}$ means the sum of the two series $\sum_{n \ge 0}$ and $\sum_{n \le -1}$, each of which must converge.
>
> *B&C: Sec. 66 (text), equations (4) and (5)*

^def-66-1

The integrand in (3) can be written $f(z)(z - z_0)^{n-1}$, so the integrals do not depend on the choice of $C$: by the deformation of contours ([[§53 Multiply Connected Domains#^cor-53-2|Corollary §53.2]]), two positively oriented simple closed contours around $z_0$ in the annulus give the same value. The proof in [[§67 Proof of Laurent's Theorem|§67]] uses this.

> [!remark] Remark: Special Cases of the Annulus
> 1. **$f$ analytic in the whole disk $|z - z_0| < R_2$.** Then $f(z)(z - z_0)^{n-1}$ is analytic inside and on $C$ for $n \ge 1$, so every $b_n = 0$ by the Cauchy–Goursat theorem ([[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|Theorem §51.3]]). And since ([[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|Theorem §56.1]])
>
>    $$
>    \frac{1}{2\pi i}\int_C\frac{f(z)\,dz}{(z - z_0)^{n+1}} = \frac{f^{(n)}(z_0)}{n!} \qquad (n = 0, 1, 2, \ldots),
>    $$
>
>    the expansion (1) reduces to the Taylor series about $z_0$ ([[§63 Proof of Taylor's Theorem#^thm-63-1|Theorem §63.1]]).
> 2. **Isolated singular point.** If $f$ fails to be analytic at $z_0$ but is otherwise analytic in $|z - z_0| < R_2$, then $R_1$ can be chosen arbitrarily small, and (1) is valid in the punctured disk $0 < |z - z_0| < R_2$.
> 3. **Exterior of a circle.** If $f$ is analytic at each point of the finite plane exterior to $|z - z_0| = R_1$, the condition of validity is $R_1 < |z - z_0| < \infty$.
> 4. **One singular point.** If $f$ is analytic everywhere in the finite plane except at $z_0$, then (1) is valid in $0 < |z - z_0| < \infty$.
>
> The expansions of [[§65 Negative Powers of (z − z₀)|§65]] are of types 2 and 4. In particular $b_1 = \frac{1}{2\pi i}\int_C f(z)\,dz$, so knowing the coefficient of $1/(z - z_0)$ evaluates the integral ([[§68 Examples (Proof of Laurent's Theorem)#^ex-68-4|Example §68.4]]).

^rem-66-1

## Coefficients on the Unit Circle

When the annulus contains the unit circle $|z| = 1$ and $z_0 = 0$, take $C$ to be that circle, $z = e^{i\phi}$ $(-\pi \le \phi \le \pi)$. Then $dz = ie^{i\phi}\,d\phi$, and (5) becomes

$$
c_n = \frac{1}{2\pi i}\int_{-\pi}^{\pi}\frac{f(e^{i\phi})}{e^{i(n+1)\phi}}\,ie^{i\phi}\,d\phi = \frac{1}{2\pi}\int_{-\pi}^{\pi}f(e^{i\phi})e^{-in\phi}\,d\phi : \qquad (6)
$$

the $n$th Laurent coefficient of $f$ is the $n$th complex Fourier coefficient of the periodic function $\phi \mapsto f(e^{i\phi})$. The three examples are instances of (6).

> [!example] Example §66.1: The Inverse z-Transform
> **Problem.** Suppose that a series $\sum_{n=-\infty}^{\infty} x[n]z^{-n}$ converges to an analytic function $X(z)$ in some annulus $R_1 < |z| < R_2$; $X(z)$ is called the **z-transform** of the sequence $x[n]$ $(n = 0, \pm1, \pm2, \ldots)$. Show that if the annulus contains the unit circle, then
>
> $$
> x[n] = \frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{i\theta})e^{in\theta}\,d\theta \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> **Solution.** Put $m = -n$: the series is $\sum_{m=-\infty}^{\infty}x[-m]z^m$, a series in powers of $z$ converging to $X(z)$ in the annulus. By the uniqueness of Laurent series ([[§72★ Uniqueness of Series Representations#^thm-72-4|Theorem §72.4]]) it is the Laurent series of $X$, so $x[-m] = c_m$ is given by (5), or on the unit circle by (6):
>
> $$
> x[n] = c_{-n} = \frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{i\theta})e^{in\theta}\,d\theta .
> $$
>
> **Check.** For $x[n] = a^n$ $(n \ge 0)$, $x[n] = 0$ $(n < 0)$, with $|a| < 1$: $X(z) = \sum_{n \ge 0}(a/z)^n = \dfrac{z}{z - a}$ for $|z| > |a|$, an annulus containing $|z| = 1$. The formula gives $\frac{1}{2\pi}\int_{-\pi}^{\pi}\frac{e^{i(n+1)\theta}}{e^{i\theta} - a}\,d\theta = \frac{1}{2\pi i}\int_{|z|=1}\frac{z^n\,dz}{z - a}$, which is $a^n$ for $n \ge 0$ by the Cauchy integral formula ([[§54 Cauchy Integral Formula#^thm-54-1|Theorem §54.1]]). For $n = -m \le -1$ it is $0$: the integral of $z^{-m}/(z - a)$ is the same over every circle $|z| = R$ with $R \ge 1$ ([[§53 Multiply Connected Domains#^cor-53-2|Corollary §53.2]]), and by the ML-inequality ([[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]]) it is at most $2\pi R\cdot R^{-m}/(R - |a|) \to 0$ as $R \to \infty$. So the formula returns the signal.
>
> In discrete-time signal processing, $\theta \mapsto X(e^{i\theta})$ is the frequency response, and the formula recovers the signal from it.
>
> *B&C: Sec. 68, Exercise 8*

^ex-66-1

> [!example] Example §66.2: The Bessel Functions as Laurent Coefficients
> **Problem.** Let $z$ be any complex number. **(a)** Show that
>
> $$
> \exp\Big[\frac z2\Big(w - \frac1w\Big)\Big] = \sum_{n=-\infty}^{\infty}J_n(z)w^n \qquad (0 < |w| < \infty), \qquad J_n(z) = \frac{1}{2\pi}\int_{-\pi}^{\pi}\exp\big[-i(n\phi - z\sin\phi)\big]\,d\phi .
> $$
>
> **(b)** Show that $J_n(z) = \dfrac1\pi\displaystyle\int_0^{\pi}\cos(n\phi - z\sin\phi)\,d\phi$ $(n = 0, \pm1, \pm2, \ldots)$.
>
> **(a)** For fixed $z$, the function $F(w) = \exp\big[\frac z2(w - \frac1w)\big]$ is analytic in the punctured plane $0 < |w| < \infty$, as the composition of $\exp$ with a function analytic for $w \ne 0$. Laurent's theorem in the $w$ plane, about the origin with $R_1 = 0$, $R_2 = \infty$, gives $F(w) = \sum_{n=-\infty}^{\infty}c_nw^n$, with $c_n$ given by (6) on the unit circle $w = e^{i\phi}$. There $w - 1/w = e^{i\phi} - e^{-i\phi} = 2i\sin\phi$, so $F(e^{i\phi}) = e^{iz\sin\phi}$ and
>
> $$
> c_n = \frac{1}{2\pi}\int_{-\pi}^{\pi}e^{iz\sin\phi}e^{-in\phi}\,d\phi = \frac{1}{2\pi}\int_{-\pi}^{\pi}\exp\big[-i(n\phi - z\sin\phi)\big]\,d\phi = J_n(z) .
> $$
>
> **(b)** Let $\theta(\phi) = n\phi - z\sin\phi$, an odd function of $\phi$. Then $e^{-i\theta} = \cos\theta - i\sin\theta$, where $\cos\theta(\phi)$ is even in $\phi$ and $\sin\theta(\phi)$ is odd (the identities $\cos(-u) = \cos u$, $\sin(-u) = -\sin u$ hold for complex $u$). For a complex-valued function on $[-\pi, \pi]$, the integral of an even function is twice the integral over $[0, \pi]$ and the integral of an odd function is $0$ ([[§42 Definite Integrals of Functions w(t)|§42]], Exercise 5). Hence
>
> $$
> J_n(z) = \frac{1}{2\pi}\cdot2\int_0^{\pi}\cos(n\phi - z\sin\phi)\,d\phi = \frac1\pi\int_0^{\pi}\cos(n\phi - z\sin\phi)\,d\phi .
> $$
>
> **Check.** At $z = 1.3 + 0.4i$, both integrals agree with the library Bessel function to ten digits for $n = 0, 1, 2, -1, -3$ (e.g. $J_1 = 0.5528578412 + 0.0889345209\,i$), and the Laurent series summed at $w = 0.7 + 0.5i$ reproduces $F(w)$ (mpmath).
>
> These $J_n(z)$ are the Bessel functions of the first kind, and $F$ is their **generating function**. For integer $n$ the integral of (b) is Bessel's integral.
>
> *B&C: Sec. 68, Exercise 9*

^ex-66-2

> [!remark]- Connections
> - The Bessel function $J_n$ appears in 341 as a Frobenius series solution of Bessel's equation, [[§55★ Bessel's Equation#^def-55-2|341 Def. §55.2]]. The two definitions agree: multiplying the series of $e^{zw/2} = \sum_j (z/2)^jw^j/j!$ and $e^{-z/(2w)} = \sum_k(-z/2)^kw^{-k}/k!$, both absolutely convergent, and collecting the terms in $w^n$ ($n \ge 0$, $j = n + k$) gives $\sum_{k \ge 0}\frac{(-1)^k(z/2)^{n+2k}}{k!(n + k)!}$, which is the series of 341; the product of two absolutely convergent series may be rearranged this way (B&C proves the Cauchy product only for power series, [[§73★ Multiplication and Division of Power Series#^thm-73-2|Theorem §73.2]]).

> [!example] Example §66.3: Fourier Series from Laurent Series
> **Problem.** **(a)** Let $f$ be analytic in an annular domain about the origin that includes the unit circle $z = e^{i\phi}$ $(-\pi \le \phi \le \pi)$. Taking that circle as the path in (2) and (3), show that at every point $z$ of the annulus
>
> $$
> f(z) = \frac{1}{2\pi}\int_{-\pi}^{\pi}f(e^{i\phi})\,d\phi + \frac{1}{2\pi}\sum_{n=1}^{\infty}\int_{-\pi}^{\pi}f(e^{i\phi})\Big[\Big(\frac{z}{e^{i\phi}}\Big)^n + \Big(\frac{e^{i\phi}}{z}\Big)^n\Big]\,d\phi .
> $$
>
> **(b)** With $u(\theta) = \operatorname{Re}f(e^{i\theta})$, deduce
>
> $$
> u(\theta) = \frac{1}{2\pi}\int_{-\pi}^{\pi}u(\phi)\,d\phi + \frac1\pi\sum_{n=1}^{\infty}\int_{-\pi}^{\pi}u(\phi)\cos[n(\theta - \phi)]\,d\phi .
> $$
>
> **(a)** By (6), $a_n = c_n = \frac{1}{2\pi}\int_{-\pi}^{\pi}f(e^{i\phi})e^{-in\phi}\,d\phi$ for $n \ge 0$ and $b_n = c_{-n} = \frac{1}{2\pi}\int_{-\pi}^{\pi}f(e^{i\phi})e^{in\phi}\,d\phi$ for $n \ge 1$. Hence $a_nz^n = \frac{1}{2\pi}\int f(e^{i\phi})(z/e^{i\phi})^n\,d\phi$ and $b_n/z^n = \frac{1}{2\pi}\int f(e^{i\phi})(e^{i\phi}/z)^n\,d\phi$. Grouping the $n$th terms of the two convergent series in (1) ([[§61 Convergence of Series#^prop-61-4|Proposition §61.4]]) gives the formula, the $n = 0$ term being $a_0$.
>
> **(b)** Put $z = e^{i\theta}$, a point of the annulus. Then
>
> $$
> \Big(\frac{z}{e^{i\phi}}\Big)^n + \Big(\frac{e^{i\phi}}{z}\Big)^n = e^{in(\theta - \phi)} + e^{-in(\theta - \phi)} = 2\cos[n(\theta - \phi)] ,
> $$
>
> a real function. Take real parts in (a): the real part of a convergent series is the series of real parts ([[§61 Convergence of Series#^thm-61-1|Theorem §61.1]]), and $\operatorname{Re}\int_{-\pi}^{\pi}g(\phi)h(\phi)\,d\phi = \int_{-\pi}^{\pi}\operatorname{Re}g(\phi)\,h(\phi)\,d\phi$ when $h$ is real. This gives the formula for $u(\theta)$.
>
> Expanding $\cos[n(\theta - \phi)] = \cos n\theta\cos n\phi + \sin n\theta\sin n\phi$ shows that this is the Fourier series of $u$ on $-\pi \le \theta \le \pi$, with the usual coefficients ([[§9 Periodic Functions and Fourier Series#^def-9-2|341 Def. §9.2]]). The hypothesis that $u$ is the real part of a function analytic on an annulus is far more than the Fourier convergence theorem needs ([[§16★ Proof of Convergence#^thm-16-4|341 Thm. §16.4]] asks only for sectional smoothness), but the proof here is two lines.
>
> *B&C: Sec. 68, Exercise 10*

^ex-66-3

> [!remark]- Connections
> - Formula (6) identifies the Laurent coefficients on the unit circle with the complex Fourier coefficients of [[§19★ Complex Methods#^def-19-1|341 Def. §19.1]], and the Laurent series with the complex form of the Fourier series, [[§19★ Complex Methods#^thm-19-1|341 Thm. §19.1]]. When $f$ is analytic in the whole disk $|z| < R_2$ with $R_2 > 1$, the negative coefficients vanish and $\operatorname{Re}f(re^{i\theta})$ is the solution of Dirichlet's problem in the unit disk with boundary values $u$, as in [[§48 Potential in a Disk#^thm-48-2|341 Thm. §48.2]].
