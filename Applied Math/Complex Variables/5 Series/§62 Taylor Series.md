---
type: section
subject: "[[Complex Variables]]"
chapter: 5
section: 62
bc: "62"
aliases: ["B&C 62"]
tags: [complex-variables, math342]
---
← [[§61 Convergence of Series]] · ↑ [[· 5 Series]] · [[§63 Proof of Taylor's Theorem]] →

*Brown–Churchill, Section 62 · MAT 342 HW 9.*

Taylor's theorem says that a function analytic in a disk is the sum of its Taylor series throughout that disk. In real analysis this fails badly: a function can have derivatives of all orders and a convergent Taylor series that does not converge to it. In complex analysis analyticity alone is enough, and the disk of validity can be read off without any convergence test: it extends from the center to the nearest point where $f$ fails to be analytic. This section states the theorem and the definitions; the proof is in [[§63 Proof of Taylor's Theorem|§63]], and the working expansions are in [[§64 Examples (Proof of Taylor's Theorem)|§64]].

## Taylor's Theorem

**Taylor's theorem** ([[§63 Proof of Taylor's Theorem#^thm-63-1|Theorem §63.1]], proved in §63). *Suppose that a function $f$ is analytic throughout a disk $|z - z_0| < R_0$, centered at $z_0$ and with radius $R_0$. Then $f(z)$ has the power series representation*

$$
f(z) = \sum_{n=0}^{\infty} a_n(z - z_0)^n \qquad (|z - z_0| < R_0), \qquad (1)
$$

*where*

$$
a_n = \frac{f^{(n)}(z_0)}{n!} \qquad (n = 0, 1, 2, \ldots) . \qquad (2)
$$

*That is, series (1) converges to $f(z)$ when $z$ lies in the stated open disk.*

The derivatives $f^{(n)}(z_0)$ all exist because an analytic function has derivatives of all orders ([[§57 Some Consequences of the Extension|§57]], Theorem 1).

> [!definition] Definition §62.1: Taylor Series; Maclaurin Series
> Let $f$ be analytic at $z_0$. The **Taylor series** of $f$ about $z_0$ is the power series
>
> $$
> \sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z - z_0)^n = f(z_0) + \frac{f'(z_0)}{1!}(z - z_0) + \frac{f''(z_0)}{2!}(z - z_0)^2 + \cdots , \qquad (3)
> $$
>
> with the agreement that $f^{(0)}(z_0) = f(z_0)$ and $0! = 1$. When $z_0 = 0$ it is called the **Maclaurin series** of $f$:
>
> $$
> \sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}z^n . \qquad (4)
> $$
>
> *B&C: Sec. 62 (text)*

^def-62-1

> [!remark]- Connections
> - Same definition for real functions: [[§31 Taylor's Theorem#^def-31-1|451 Def. §31.1]]. There, convergence of the series to $f$ must be proved from a remainder estimate ([[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]]), and it can fail for a function with derivatives of all orders: $e^{-1/x^2}$ has Taylor series $0$ at the origin ([[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]]). As a function of a complex variable, $e^{-1/z^2}$ is not even continuous at $0$ (along the imaginary axis it is $e^{1/y^2}$), so it is not analytic there and Taylor's theorem does not apply.

> [!remark] Remark: Where the Taylor Series Converges to f
> Taylor's theorem needs no test for convergence; it only asks where $f$ is analytic.
> 1. **Every function analytic at $z_0$ has a Taylor series about $z_0$ that represents it near $z_0$.** By definition ([[§25 Analytic Functions|§25]]), $f$ is analytic throughout some neighborhood $|z - z_0| < \varepsilon$, and $\varepsilon$ may serve as $R_0$.
> 2. **Entire functions.** If $f$ is entire, $R_0$ can be chosen arbitrarily large, and the condition of validity becomes $|z - z_0| < \infty$: the series converges to $f(z)$ at every point of the finite plane.
> 3. **The disk reaches the nearest singular point.** If $z_1$ is the point nearest to $z_0$ at which $f$ fails to be analytic, then $f$ is analytic in $|z - z_0| < |z_1 - z_0|$, so the Taylor series converges to $f(z)$ in that disk. By [[§71★ Integration and Differentiation of Power Series#^cor-71-3|Corollary §71.3]] this is the largest circle centered at $z_0$ with that property.
>
> Item 3 makes the region of validity predictable before any coefficient is computed.

^rem-62-1

## Coefficients by Differentiation

The examples compute $a_n = f^{(n)}(z_0)/n!$ directly. The more efficient methods of [[§64 Examples (Proof of Taylor's Theorem)|§64]], built on known series, rest on the uniqueness of the representation ([[§72★ Uniqueness of Series Representations#^thm-72-1|Theorem §72.1]]).

> [!example] Example §62.1: Sine and Cosine from Their Derivatives
> **Claim.** If $f(z) = \sin z$, then $f^{(2n)}(0) = 0$ and $f^{(2n+1)}(0) = (-1)^n$; if $f(z) = \cos z$, then $f^{(2n)}(0) = (-1)^n$ and $f^{(2n+1)}(0) = 0$ $(n = 0, 1, 2, \ldots)$. Consequently
>
> $$
> \sin z = \sum_{n=0}^{\infty}(-1)^n\frac{z^{2n+1}}{(2n + 1)!}, \qquad \cos z = \sum_{n=0}^{\infty}(-1)^n\frac{z^{2n}}{(2n)!} \qquad (|z| < \infty) .
> $$
>
> **Derivatives.** By [[§37 The Trigonometric Functions sin z and cos z|§37]], $\frac{d}{dz}\sin z = \cos z$ and $\frac{d}{dz}\cos z = -\sin z$, so the derivatives of $\sin z$ cycle through $\sin z, \cos z, -\sin z, -\cos z$. By induction on $n$,
>
> $$
> \frac{d^{2n}}{dz^{2n}}\sin z = (-1)^n\sin z, \qquad \frac{d^{2n+1}}{dz^{2n+1}}\sin z = (-1)^n\cos z :
> $$
>
> both hold for $n = 0$, and if they hold for $n$, differentiating the second gives $\frac{d^{2n+2}}{dz^{2n+2}}\sin z = (-1)^n(-\sin z) = (-1)^{n+1}\sin z$, and differentiating once more gives $(-1)^{n+1}\cos z$. Evaluating at $0$ with $\sin 0 = 0$, $\cos 0 = 1$ gives the claim for $\sin z$. For $\cos z = \frac{d}{dz}\sin z$, shift by one: $\cos^{(2n)}(z) = \sin^{(2n+1)}(z) = (-1)^n\cos z$ and $\cos^{(2n+1)}(z) = \sin^{(2n+2)}(z) = (-1)^{n+1}\sin z$, which at $0$ are $(-1)^n$ and $0$.
>
> **Series.** Both functions are entire, so by Taylor's theorem their Maclaurin series converge to them everywhere. Only odd powers survive for $\sin z$, with $a_{2n+1} = (-1)^n/(2n + 1)!$, and only even powers for $\cos z$, with $a_{2n} = (-1)^n/(2n)!$.
>
> *B&C: Sec. 65, Exercises 7 and 8(b)*

^ex-62-1

> [!example] Example §62.2: The Largest Disk for tanh z
> **Problem.** What is the largest circle within which the Maclaurin series of $\tanh z$ converges to $\tanh z$? Write the first two nonzero terms of the series.
>
> **The disk.** $\tanh z = \sinh z/\cosh z$ is analytic except where $\cosh z = 0$, that is, at $z = \big(\frac\pi2 + n\pi\big)i$ $(n = 0, \pm1, \pm2, \ldots)$ ([[§39★ Hyperbolic Functions|§39]]). The nearest of these to the origin are $\pm\frac\pi2 i$, at distance $\frac\pi2$. So the Maclaurin series converges to $\tanh z$ in $|z| < \pi/2$ (Remark: Where the Taylor Series Converges to f, item 3), and this is the largest such circle, since $\tanh z$ is not even defined at $\pm\frac\pi2 i$.
>
> **The terms.** Let $f(z) = \tanh z$. Then $f' = \operatorname{sech}^2 z = 1 - f^2$, and differentiating this identity,
>
> $$
> f'' = -2ff', \qquad f''' = -2\big((f')^2 + ff''\big) .
> $$
>
> At $0$: $f(0) = 0$, $f'(0) = 1$, $f''(0) = 0$, $f'''(0) = -2$. Hence $a_1 = 1$, $a_2 = 0$, $a_3 = -2/3! = -\frac13$ (and $a_0 = 0$), so
>
> $$
> \tanh z = z - \frac{z^3}{3} + \cdots \qquad (|z| < \pi/2) .
> $$
>
> (The next term is $\frac{2}{15}z^5$. All even-order coefficients vanish, since $\tanh z$ is odd.)
>
> *B&C: Sec. 65, Exercise 6*

^ex-62-2

> [!example] Example §62.3: The Taylor Series of 1/(z + i) About z = 2
> **Problem.** Find the Taylor series of $f(z) = \dfrac{1}{z + i}$ about $z_0 = 2$ **(a)** by computing derivatives and **(b)** by algebra and the geometric series. **(c)** In what disk does the series converge? How is the radius related to the domain where $f$ is analytic?
>
> **(a) Derivatives.** $f'(z) = -(z + i)^{-2}$, $f''(z) = 2(z + i)^{-3}$, $f'''(z) = -3!\,(z + i)^{-4}$, and by induction
>
> $$
> f^{(n)}(z) = \frac{(-1)^n n!}{(z + i)^{n+1}}, \qquad\text{so}\qquad a_n = \frac{f^{(n)}(2)}{n!} = \frac{(-1)^n}{(2 + i)^{n+1}} .
> $$
>
> (Induction step: $\frac{d}{dz}(-1)^n n!(z + i)^{-n-1} = (-1)^{n+1}(n + 1)!\,(z + i)^{-n-2}$.) So
>
> $$
> \frac{1}{z + i} = \sum_{n=0}^{\infty}\frac{(-1)^n}{(2 + i)^{n+1}}(z - 2)^n = \frac{2 - i}{5} - \frac{3 - 4i}{25}(z - 2) + \cdots ,
> $$
>
> using $\frac{1}{2 + i} = \frac{2 - i}{5}$ and $\frac{1}{(2 + i)^2} = \frac{1}{3 + 4i} = \frac{3 - 4i}{25}$.
>
> **(b) Geometric series.** Write the denominator around the center:
>
> $$
> \frac{1}{z + i} = \frac{1}{(2 + i) + (z - 2)} = \frac{1}{2 + i}\cdot\frac{1}{1 - \big(-\frac{z - 2}{2 + i}\big)} = \frac{1}{2 + i}\sum_{n=0}^{\infty}\Big(-\frac{z - 2}{2 + i}\Big)^n = \sum_{n=0}^{\infty}\frac{(-1)^n}{(2 + i)^{n+1}}(z - 2)^n ,
> $$
>
> by [[§61 Convergence of Series#^ex-61-1|Example §61.1]], valid when $\big|\frac{z - 2}{2 + i}\big| < 1$. The coefficients agree with (a), as they must ([[§72★ Uniqueness of Series Representations#^thm-72-1|Theorem §72.1]]).
>
> **(c) The disk.** The geometric series converges exactly when $|z - 2| < |2 + i| = \sqrt5$: the disk with center $2$ and radius $\sqrt5$. For $|z - 2| \ge \sqrt5$ the terms have modulus $|z - 2|^n/\sqrt5^{\,n+1} \ge 1/\sqrt5$, which does not tend to $0$, so the series diverges there (Corollary §61.2). The radius is the distance from the center $2$ to $-i$, the only point where $f$ fails to be analytic, exactly as Taylor's theorem predicts: the disk is the largest disk about $2$ in which $f$ is analytic, and the singular point $-i$ lies on its boundary circle.
>
> *Source: 342 HW 9, Problem 2*

^ex-62-3

![[m342-62-1.svg]]
*Example §62.3: the Taylor series of $1/(z + i)$ about $2$ converges to the function in the open disk $|z - 2| < \sqrt5$, whose boundary circle passes through the singular point $-i$ (red). The radius was found before computing any coefficient.*
