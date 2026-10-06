---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 1
section: 10
powers: "1.2"
aliases: ["Powers 1.2"]
tags: [fourier-series-and-pdes, math341]
---
← [[§9 Periodic Functions and Fourier Series]] · ↑ [[· 1 Fourier Series and Integrals]] · [[§11 Even and Odd Functions; Half-Range Expansions]] →

*Powers, Section 1.2 · MAT 341 lectures 8.29, 9.3 · HW 1.*

Nothing about Fourier series requires the period to be $2\pi$: rescaling $x$ gives series in $\cos(n\pi x/a)$, $\sin(n\pi x/a)$ for functions of any period $2a$. A function given only on a finite interval is handled by making it part of a periodic function, its periodic extension. Symmetry halves the work: even functions have only cosine terms and odd functions only sine terms. Most important for the rest of the book, a function given on $0 < x < a$ can be extended to $-a < x < a$ as an odd or as an even function, which produces its Fourier sine series and its Fourier cosine series, the half-range expansions. These are the series that appear when the heat and wave equations on a rod or string of length $a$ are solved by separation of variables ([[§25 Example꞉ Fixed End Temperatures|§25]], [[§26 Example꞉ Insulated Bar|§26]], [[§38 Solution of the Vibrating String Problem|§38]]): a sine series fits ends held at zero, a cosine series fits insulated ends.

## Functions of Period 2a

Suppose $f$ is periodic with period $2a$ ($2a$ in place of $p$ for later convenience). The functions $1, \sin(\pi x/a), \cos(\pi x/a), \sin(2\pi x/a), \cos(2\pi x/a), \ldots$ all have period $2a$ ([[§9 Periodic Functions and Fourier Series#^prop-9-1|Proposition §9.1]] with $\lambda = \pi/a$, since $2\pi/(\pi/a) = 2a$), and we relate $f$ to a series of them,

$$
f(x) \sim a_0 + \sum_{n=1}^{\infty} a_n\cos\Big(\frac{n\pi x}{a}\Big) + b_n\sin\Big(\frac{n\pi x}{a}\Big) .
$$

> [!theorem] Proposition §14.1: Fourier Coefficients for Period 2a
> The Fourier coefficients of a function $f$ of period $2a$ are
>
> $$
> a_0 = \frac{1}{2a}\int_{-a}^{a} f(x)\,dx, \qquad a_n = \frac1a\int_{-a}^{a} f(x)\cos\Big(\frac{n\pi x}{a}\Big)dx, \qquad b_n = \frac1a\int_{-a}^{a} f(x)\sin\Big(\frac{n\pi x}{a}\Big)dx . \qquad (1)
> $$
>
> They are obtained either by scaling from the formulas of [[§9 Periodic Functions and Fourier Series#^prop-9-4|Proposition §9.4]] or through orthogonality: for $n, m \ge 1$,
>
> $$
> \int_{-a}^{a}\cos\frac{n\pi x}{a}\sin\frac{m\pi x}{a}\,dx = 0, \qquad
> \int_{-a}^{a}\cos\frac{n\pi x}{a}\cos\frac{m\pi x}{a}\,dx = \int_{-a}^{a}\sin\frac{n\pi x}{a}\sin\frac{m\pi x}{a}\,dx = \begin{cases} 0, & n \ne m, \\ a, & n = m, \end{cases}
> $$
>
> and $\int_{-a}^{a}\cos(n\pi x/a)\,dx = \int_{-a}^{a}\sin(n\pi x/a)\,dx = 0$.
>
> *Powers: 1.2, Equation (1); Exercise 1.2.2*

^prop-10-1

> [!proof]+ Proof
> **By scaling.** Let $g(y) = f(ay/\pi)$. By [[§9 Periodic Functions and Fourier Series#^prop-9-1|Proposition §9.1]](2), $g$ has period $2a/(a/\pi) = 2\pi$, and its Fourier series is $g(y) \sim a_0 + \sum(a_n\cos ny + b_n\sin ny)$ with the coefficients of [[§9 Periodic Functions and Fourier Series#^def-9-2|Definition §9.2]]. Substitute $y = \pi x/a$, $dy = (\pi/a)\,dx$; as $y$ runs over $(-\pi, \pi)$, $x$ runs over $(-a, a)$:
>
> $$
> a_n = \frac1\pi\int_{-\pi}^{\pi} g(y)\cos ny\,dy = \frac1\pi\int_{-a}^{a} f(x)\cos\frac{n\pi x}{a}\cdot\frac\pi a\,dx = \frac1a\int_{-a}^{a} f(x)\cos\frac{n\pi x}{a}\,dx ,
> $$
>
> and in the same way $a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} g = \frac{1}{2a}\int_{-a}^{a} f$ and $b_n = \frac1a\int_{-a}^{a} f(x)\sin\frac{n\pi x}{a}\,dx$. In terms of $x$, $\cos ny = \cos(n\pi x/a)$ and $\sin ny = \sin(n\pi x/a)$, which is the series above.
>
> **The orthogonality relations** follow from [[§9 Periodic Functions and Fourier Series#^prop-9-3|Proposition §9.3]] by the same substitution: each integral over $(-a, a)$ equals $a/\pi$ times the corresponding integral over $(-\pi, \pi)$, which turns the values $0$ and $\pi$ into $0$ and $a$. With them, the derivation of [[§9 Periodic Functions and Fourier Series#^prop-9-4|Proposition §9.4]] gives (1) directly.

^pf-10-1

*Uses:* [[§9 Periodic Functions and Fourier Series#^prop-9-1|§9.1]], [[§9 Periodic Functions and Fourier Series#^prop-9-3|§9.3]], [[§9 Periodic Functions and Fourier Series#^prop-9-4|§9.4]], [[§9 Periodic Functions and Fourier Series#^def-9-2|Def. §9.2]]

> [!example] Example §14.1: The Rectified Sine |sin(πx)|
> Find the Fourier series of $f(x) = |\sin(\pi x)|$.
>
> $\sin(\pi x)$ has period $2$, but $|\sin(\pi x)|$ has period $1$, so $a = \frac12$. To do the integrals, get rid of the absolute value: on one period,
>
> $$
> f(x) = \begin{cases} \sin(\pi x), & 0 < x < \frac12, \\ -\sin(\pi x), & -\frac12 < x < 0 . \end{cases}
> $$
>
> Then, since $\cos(\pm\pi/2) = 0$,
>
> $$
> a_0 = \frac11\int_{-1/2}^{1/2}|\sin(\pi x)|\,dx = \int_{-1/2}^{0} -\sin(\pi x)\,dx + \int_0^{1/2}\sin(\pi x)\,dx = \frac{\cos(\pi x)}{\pi}\Big|_{-1/2}^{0} - \frac{\cos(\pi x)}{\pi}\Big|_0^{1/2} = \frac1\pi + \frac1\pi = \frac2\pi .
> $$
>
> For $a_n$, $n\pi x/a = 2n\pi x$, and $f(x)\cos(2n\pi x)$ is even, so the two halves are equal:
>
> $$
> a_n = \frac{2}{1}\int_{-1/2}^{1/2}|\sin(\pi x)|\cos(2n\pi x)\,dx = 4\int_0^{1/2}\sin(\pi x)\cos(2n\pi x)\,dx = 2\int_0^{1/2}\big[\sin((2n + 1)\pi x) - \sin((2n - 1)\pi x)\big]dx .
> $$
>
> With $\int_0^{1/2}\sin(k\pi x)\,dx = \frac{1}{k\pi}\big(1 - \cos\frac{k\pi}{2}\big) = \frac{1}{k\pi}$ for odd $k$,
>
> $$
> a_n = \frac2\pi\Big(\frac{1}{2n + 1} - \frac{1}{2n - 1}\Big) = \frac2\pi\cdot\frac{-2}{4n^2 - 1} = -\frac4\pi\cdot\frac{1}{4n^2 - 1} .
> $$
>
> And $b_n = 0$ for all $n$, because $f(x)\sin(2n\pi x)$ is odd. Consequently
>
> $$
> |\sin(\pi x)| \sim \frac2\pi - \frac4\pi\sum_{n=1}^{\infty}\frac{1}{4n^2 - 1}\cos(2n\pi x) .
> $$
>
> We will see in [[§13 Uniform Convergence#^ex-13-4|Example §13.4]] that $|\sin(\pi x)|$ is equal to its series, and the series converges uniformly.
>
> *Powers: 1.2, first Example*

^ex-10-1

## Periodic Extension

It is often necessary to use a Fourier series for a function defined only on a finite interval. Such a representation is justified by making the given function part of a periodic function.

> [!definition] Definition §10.1: Periodic Extension
> If $f$ is defined on $-a < x < a$, its **periodic extension** $\bar f$ of period $2a$ is defined by
>
> $$
> \bar f(x) = f(x),\ -a < x < a; \qquad \bar f(x) = f(x + 2a),\ -3a < x < -a; \qquad \bar f(x) = f(x - 2a),\ a < x < 3a ,
> $$
>
> and so on up and down the $x$-axis: on each interval $(-a + 2ka, a + 2ka)$, $\bar f(x) = f(x - 2ka)$, whose argument falls in $(-a, a)$, where $f$ was originally given. Graphically, the graph of $f$ on $-a < x < a$ is a template, copied onto abutting intervals of length $2a$. (The values at $x = \pm a, \pm3a, \ldots$ are left open; see [[§12 Convergence of Fourier Series#^rem-12-1|§12]].)
>
> *Powers: 1.2 (text)*

^def-10-1

For the extended function, the coefficient formulas (1) read

$$
a_0 = \frac{1}{2a}\int_{-a}^{a}\bar f(x)\,dx, \qquad a_n = \frac1a\int_{-a}^{a}\bar f(x)\cos\Big(\frac{n\pi x}{a}\Big)dx, \qquad b_n = \frac1a\int_{-a}^{a}\bar f(x)\sin\Big(\frac{n\pi x}{a}\Big)dx . \qquad (2)
$$

They involve $\bar f$ only on $(-a, a)$, where $\bar f = f$. So if we are concerned with $f$ only on its original interval, the periodic extension is strictly formal, and we may write

$$
f(x) \sim a_0 + \sum_{n=1}^{\infty} a_n\cos\Big(\frac{n\pi x}{a}\Big) + b_n\sin\Big(\frac{n\pi x}{a}\Big), \qquad -a < x < a ,
$$

the inequality for $x$ recording that $f$ was defined only on $-a$ to $a$.

> [!example] Example §14.2: A Piecewise Function of Period 4
> Let $f$ be periodic with period $4$ and
>
> $$
> f(x) = \begin{cases} -1, & -2 < x \le 0, \\ x, & 0 < x \le 2 . \end{cases}
> $$
>
> Sketch the graph on $(-6, 6)$ and find the Fourier series.
>
> **Graph.** On each period: a horizontal segment at height $-1$ over $(-2, 0]$, then a segment of slope $1$ from $(0, 0)$ up to $(2, 2)$. So $\bar f$ jumps from $-1$ up to $0$ at $x = 0, \pm4$, and from $2$ down to $-1$ at $x = \pm2, \pm6$. The function given by $x$ on $(0, 2]$ and $-1$ on $(2, 4]$, extended with period $4$, is the same function: it is the same template shifted by one period.
>
> **Coefficients** ($a = 2$, $n\pi x/a = n\pi x/2$).
>
> $$
> a_0 = \frac14\int_{-2}^{0}(-1)\,dx + \frac14\int_0^2 x\,dx = -\frac12 + \frac12 = 0 .
> $$
>
> $$
> a_n = -\frac12\int_{-2}^{0}\cos\frac{n\pi x}{2}\,dx + \frac12\int_0^2 x\cos\frac{n\pi x}{2}\,dx = -\frac12\cdot 0 + \frac12\cdot\Big(\frac{2}{n\pi}\Big)^2\Big[\cos\frac{n\pi x}{2}\Big]_0^2 = \frac{2}{(n\pi)^2}\big[(-1)^n - 1\big] ,
> $$
>
> using $\int_0^2 x\cos\frac{n\pi x}{2}dx = \big[\frac{2x}{n\pi}\sin\frac{n\pi x}{2} + \frac{4}{n^2\pi^2}\cos\frac{n\pi x}{2}\big]_0^2$ and $\sin n\pi = 0$.
>
> $$
> b_n = -\frac12\int_{-2}^{0}\sin\frac{n\pi x}{2}\,dx + \frac12\int_0^2 x\sin\frac{n\pi x}{2}\,dx = \frac{1}{n\pi}\big[1 - (-1)^n\big] - \frac{2(-1)^n}{n\pi} = \frac{1}{n\pi}\big[1 - 3(-1)^n\big] .
> $$
>
> (The first integral is $-\frac12\cdot\big(-\frac{2}{n\pi}\big)\big[\cos\frac{n\pi x}{2}\big]_{-2}^{0} = \frac{1}{n\pi}(1 - (-1)^n)$; the second is $\frac12\big[-\frac{2x}{n\pi}\cos\frac{n\pi x}{2} + \frac{4}{n^2\pi^2}\sin\frac{n\pi x}{2}\big]_0^2 = -\frac{2(-1)^n}{n\pi}$.) So
>
> $$
> f(x) \sim \sum_{n=1}^{\infty}\frac{2}{(n\pi)^2}\big[(-1)^n - 1\big]\cos\frac{n\pi x}{2} + \sum_{n=1}^{\infty}\frac{1}{n\pi}\big[1 - 3(-1)^n\big]\sin\frac{n\pi x}{2} .
> $$
>
> *Source: 341 lecture 9.3, Example 1*

^ex-10-2

*Continued in [[§11 Even and Odd Functions; Half-Range Expansions]]: even and odd functions, odd and even extensions, and the half-range expansions.*
