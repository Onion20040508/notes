---
type: section
subject: "[[Complex Variables]]"
chapter: 6
section: 79
bc: "79"
aliases: ["B&C 79"]
tags: [complex-variables, math342]
---
← [[§78 The Three Types of Isolated Singular Points]] · ↑ [[· 6 Residues and Poles]] · [[§80 Residues at Poles]] →

*Brown–Churchill, Section 79 · MAT 342 HW 11, Practice Final (Spring 2005).*

This section illustrates the three types of isolated singular points of [[§78 The Three Types of Isolated Singular Points|§78]] by writing out Laurent series: a removable singular point, where the principal part vanishes; the essential singular point of $e^{1/z}$, where it never stops; and poles of orders $1$ and $2$. Two observations point ahead to [[§84 Behavior of Functions Near Isolated Singular Points|§84]]: near a pole the function tends to $\infty$, while near an essential singular point it takes nearly every value infinitely often (Picard's theorem). The remaining sections of the chapter develop faster methods for recognizing poles and computing their residues.

## Removable and Essential Singular Points

> [!example] Example §79.1: A Removable Singular Point
> The point $z_0 = 0$ is a removable singular point of
>
> $$
> f(z) = \frac{1 - \cosh z}{z^2} , \qquad (1)
> $$
>
> because, by the Maclaurin series of $\cosh z$,
>
> $$
> f(z) = \frac{1}{z^2}\Big[1 - \Big(1 + \frac{z^2}{2!} + \frac{z^4}{4!} + \frac{z^6}{6!} + \cdots\Big)\Big] = -\frac{1}{2!} - \frac{z^2}{4!} - \frac{z^4}{6!} - \cdots \qquad (0 < |z| < \infty) ,
> $$
>
> a Laurent series with no negative powers. When the value $f(0) = -\frac12$ is assigned, $f$ becomes entire ([[§78 The Three Types of Isolated Singular Points#^prop-78-1|Proposition §78.1]]).
>
> *B&C: Sec. 79, Example 1*

^ex-79-1

The function $e^{1/z}$ of the next example illustrates an important result about essential singular points, known as **Picard's theorem**.

> [!theorem] Theorem §79.1: Picard's Theorem
> In each neighborhood of an essential singular point, a function assumes every finite value, with one possible exception, an infinite number of times.
>
> *B&C: Sec. 79 (text)*

^thm-79-1

*B&C omits the proof.*

B&C refers to Markushevich, *Theory of Functions of a Complex Variable*, Vol. III, Sec. 51, for a proof. The weaker Casorati–Weierstrass theorem, that the values come arbitrarily close to every complex number, is proved in [[§84 Behavior of Functions Near Isolated Singular Points#^thm-84-3|Theorem §84.3]].

> [!example] Example §79.2: The Essential Singular Point of e^(1/z)
> From the Laurent series ([[§68 Examples (Proof of Laurent's Theorem)|§68]], Example 3)
>
> $$
> e^{1/z} = \sum_{n=0}^{\infty}\frac{1}{n!}\cdot\frac{1}{z^n} = 1 + \frac{1}{1!}\cdot\frac1z + \frac{1}{2!}\cdot\frac{1}{z^2} + \cdots \qquad (0 < |z| < \infty), \qquad (2)
> $$
>
> every $b_n = 1/n!$ is nonzero, so $e^{1/z}$ has an essential singular point at $z_0 = 0$, where the residue $b_1$ is $1$.
>
> **Picard's theorem in action.** $e^{1/z}$ assumes the value $-1$ an infinite number of times in each neighborhood of the origin. Indeed, $e^w = -1$ exactly when $w = (2n + 1)\pi i$ ($n = 0, \pm1, \pm2, \ldots$) ([[§30 The Exponential Function|§30]]), so $e^{1/z} = -1$ when
>
> $$
> z = \frac{1}{(2n + 1)\pi i}\cdot\frac ii = -\frac{i}{(2n + 1)\pi} \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> These points have modulus $\frac{1}{|2n + 1|\pi}$, so for $n$ large enough infinitely many of them lie in any given $\varepsilon$ neighborhood of the origin. The same argument works for every value $w_0 \ne 0$ in place of $-1$ (solve $1/z = \log w_0$). Zero is the exceptional value when Picard's theorem is applied to $e^{1/z}$ at the origin, since $e^w$ is never $0$.
>
> *B&C: Sec. 79, Example 2*

^ex-79-2

## Poles

> [!example] Example §79.3: A Double Pole and a Simple Pole
> **(a)** From the representation
>
> $$
> f(z) = \frac{1}{z^2(1 - z)} = \frac{1}{z^2}\big(1 + z + z^2 + z^3 + z^4 + \cdots\big) = \frac{1}{z^2} + \frac1z + 1 + z + z^2 + \cdots \qquad (0 < |z| < 1), \qquad (3)
> $$
>
> $f$ has a pole of order $m = 2$ at the origin, and $\operatorname{Res}_{z=0} f(z) = 1$. Moreover, since
>
> $$
> \lim_{z\to0}\frac{1}{f(z)} = \lim_{z\to0}\big[z^2(1 - z)\big] = 0 ,
> $$
>
> it follows ([[§17 Limits Involving the Point at Infinity#^thm-17-1|Theorem §17.1]]) that
>
> $$
> \lim_{z\to0} f(z) = \infty . \qquad (4)
> $$
>
> **(b)** The function
>
> $$
> f(z) = \frac{z^2 + z - 2}{z + 1} = \frac{z(z + 1) - 2}{z + 1} = z - \frac{2}{z + 1} = -1 + (z + 1) - \frac{2}{z + 1} \qquad (0 < |z + 1| < \infty)
> $$
>
> has a simple pole at $z_0 = -1$, with residue $-2$. Moreover, since
>
> $$
> \lim_{z\to-1}\frac{1}{f(z)} = \lim_{z\to-1}\frac{z + 1}{z^2 + z - 2} = \frac{0}{-2} = 0 ,
> $$
>
> we find that $\lim_{z\to-1} f(z) = \infty$. (5)
>
> Such a limit always occurs at poles, as is shown in [[§84 Behavior of Functions Near Isolated Singular Points#^thm-84-4|Theorem §84.4]].
>
> *B&C: Sec. 79, Examples 3 and 4*

^ex-79-3

## Exercises from the Course

> [!example] Example §79.4: Principal Parts, Orders and Residues
> **(1)** Write the principal part of each function at its isolated singular point and decide whether the point is removable, essential, or a pole:
>
> $$
> \text{(a)}\ z\exp\Big(\frac1z\Big); \qquad \text{(b)}\ \frac{z^2}{1 + z}; \qquad \text{(d)}\ \frac{\cos z}{z} .
> $$
>
> **(2)** Show that the singular point of each function is a pole; find its order $m$ and the residue $B$:
>
> $$
> \text{(b)}\ \frac{1 - \exp(2z)}{z^4}; \qquad \text{(c)}\ \frac{\exp(2z)}{(z - 1)^2} .
> $$
>
> **1(a)** The singular point is $0$. By (2),
>
> $$
> z\,e^{1/z} = \sum_{n=0}^{\infty}\frac{z^{1-n}}{n!} = z + 1 + \frac{1}{2!}\cdot\frac1z + \frac{1}{3!}\cdot\frac{1}{z^2} + \cdots \qquad (0 < |z| < \infty) ,
> $$
>
> with principal part $\displaystyle\sum_{n=2}^{\infty}\frac{1}{n!\,z^{n-1}} = \frac{1}{2!\,z} + \frac{1}{3!\,z^2} + \cdots$. Infinitely many terms: **essential singular point**.
>
> **1(b)** The singular point is $-1$. Writing $z = (z + 1) - 1$, $z^2 = (z + 1)^2 - 2(z + 1) + 1$, so
>
> $$
> \frac{z^2}{1 + z} = (z + 1) - 2 + \frac{1}{z + 1} \qquad (0 < |z + 1| < \infty) ,
> $$
>
> with principal part $\dfrac{1}{z + 1}$: a **simple pole** (residue $1$).
>
> **1(d)** The singular point is $0$, and
>
> $$
> \frac{\cos z}{z} = \frac1z\Big(1 - \frac{z^2}{2!} + \frac{z^4}{4!} - \cdots\Big) = \frac1z - \frac{z}{2!} + \frac{z^3}{4!} - \cdots \qquad (0 < |z| < \infty) ,
> $$
>
> with principal part $\dfrac1z$: a **simple pole** (residue $1$).
>
> **2(b)** Using $e^{2z} = \sum_{n \ge 0}(2z)^n/n!$,
>
> $$
> \frac{1 - e^{2z}}{z^4} = -\frac{1}{z^4}\sum_{n=1}^{\infty}\frac{2^nz^n}{n!} = -\frac{2}{z^3} - \frac{2}{z^2} - \frac{4}{3}\cdot\frac1z - \frac23 - \cdots \qquad (0 < |z| < \infty) .
> $$
>
> The lowest power is $z^{-3}$ (from $n = 1$), so $m = 3$, and the coefficient of $z^{-1}$ ($n = 3$) is $B = -\dfrac{2^3}{3!} = -\dfrac43$.
>
> **2(c)** Expand about $z_0 = 1$: $e^{2z} = e^2e^{2(z - 1)} = e^2\sum_{n \ge 0}\frac{2^n(z - 1)^n}{n!}$, so
>
> $$
> \frac{e^{2z}}{(z - 1)^2} = e^2\sum_{n=0}^{\infty}\frac{2^n}{n!}(z - 1)^{n-2} = \frac{e^2}{(z - 1)^2} + \frac{2e^2}{z - 1} + 2e^2 + \cdots \qquad (0 < |z - 1| < \infty) .
> $$
>
> Hence $m = 2$ and $B = 2e^2$.
>
> *B&C: Sec. 79, Exercises 1(a), (b), (d) and 2(b), (c); Source: 342 HW 11*

^ex-79-4

> [!example] Example §79.5: Singularities of (1 + z) tan z / z⁵
> Given that the Taylor series of $\tan z$ centered at $0$ has the form
>
> $$
> \tan z = z + \frac13z^3 + \frac{2}{15}z^5 + \cdots \quad\text{(terms of order at least seven)},
> $$
>
> **(a)** evaluate $\tan^{(5)}(0)$; **(b)** find the principal part at $z = 0$ of $f(z) = \dfrac{(1 + z)\tan z}{z^5}$; **(c)** find all the singularities of $f$ in the disk $D = \{|z| < 4\}$ and their type; **(d)** find the residue at each of them.
>
> **(a)** The coefficient of $z^5$ in a Taylor series is $\tan^{(5)}(0)/5!$ ([[§62 Taylor Series#^def-62-1|Definition §62.1]] and [[§63 Proof of Taylor's Theorem#^thm-63-1|Theorem §63.1]]), so $\tan^{(5)}(0) = 5!\cdot\frac{2}{15} = 16$.
>
> **(b)** Multiplying out,
>
> $$
> f(z) = \frac{1}{z^5}(1 + z)\Big(z + \frac13z^3 + \frac{2}{15}z^5 + \cdots\Big) = \frac{1}{z^5}\Big(z + z^2 + \frac13z^3 + \frac13z^4 + \frac{2}{15}z^5 + \cdots\Big) ,
> $$
>
> so the principal part at $0$ is
>
> $$
> \frac{1}{z^4} + \frac{1}{z^3} + \frac13\cdot\frac{1}{z^2} + \frac13\cdot\frac1z .
> $$
>
> **(c)** $f(z) = \dfrac{(1 + z)\sin z}{z^5\cos z}$ is analytic except at $z = 0$ and at the zeros $z = \frac\pi2 + k\pi$ of $\cos z$ ([[§38 Zeros and Singularities of Trigonometric Functions|§38]]). In $|z| < 4$ these are $\pm\frac\pi2$ only, since $\frac{3\pi}{2} \approx 4.71 > 4$. By (b), $z = 0$ is a **pole of order $4$**. At $z = \pm\frac\pi2$ the numerator $(1 + z)\sin z/z^5$ is analytic and nonzero ($1 \pm \frac\pi2 \ne 0$, $\sin(\pm\frac\pi2) = \pm1$), while $\cos z$ has a simple zero ($\frac{d}{dz}\cos z = -\sin z = \mp1 \ne 0$); so $\pm\frac\pi2$ are **simple poles** ([[§83 Zeros and Poles#^thm-83-1|Theorem §83.1]]).
>
> **(d)** At $0$ the residue is the coefficient of $1/z$ in (b): $\operatorname{Res}_{z=0} f = \frac13$. At the simple poles, with $p(z) = (1 + z)\sin z/z^5$ and $q(z) = \cos z$, the residue is $p/q'$ ([[§83 Zeros and Poles#^thm-83-2|Theorem §83.2]]):
>
> $$
> \operatorname{Res}_{z=\pi/2} f = \frac{(1 + \frac\pi2)\cdot 1/(\frac\pi2)^5}{-\sin\frac\pi2} = -\frac{1 + \frac\pi2}{(\frac\pi2)^5} = -\frac{16(\pi + 2)}{\pi^5}, \qquad
> \operatorname{Res}_{z=-\pi/2} f = \frac{(1 - \frac\pi2)(-1)/(-\frac\pi2)^5}{-\sin(-\frac\pi2)} = \frac{1 - \frac\pi2}{(\frac\pi2)^5} = \frac{16(2 - \pi)}{\pi^5} .
> $$
>
> *Source: 342 practice final (Spring 2005), Q1*

^ex-79-5

The remaining sections of the chapter develop in greater depth the theory of the three types: [[§80 Residues at Poles|§80]]–[[§83 Zeros and Poles|§83]] give useful and efficient methods for identifying poles and finding the corresponding residues, and [[§84 Behavior of Functions Near Isolated Singular Points|§84]] compares the behavior of functions near the three types.
