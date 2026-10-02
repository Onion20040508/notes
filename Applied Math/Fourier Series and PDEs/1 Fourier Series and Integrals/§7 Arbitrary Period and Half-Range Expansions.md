---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 1
section: 7
powers: "1.2"
aliases: ["Powers 1.2"]
tags: [fourier-series-and-pdes, math341]
---
← [[§6 Periodic Functions and Fourier Series]] · ↑ [[· 1 Fourier Series and Integrals]] · [[§8 Convergence of Fourier Series]] →

*Powers, Section 1.2 · MAT 341 lectures 8.29, 9.3 · HW 1.*

Nothing about Fourier series requires the period to be $2\pi$: rescaling $x$ gives series in $\cos(n\pi x/a)$, $\sin(n\pi x/a)$ for functions of any period $2a$. A function given only on a finite interval is handled by making it part of a periodic function, its periodic extension. Symmetry halves the work: even functions have only cosine terms and odd functions only sine terms. Most important for the rest of the book, a function given on $0 < x < a$ can be extended to $-a < x < a$ as an odd or as an even function, which produces its Fourier sine series and its Fourier cosine series, the half-range expansions. These are the series that appear when the heat and wave equations on a rod or string of length $a$ are solved by separation of variables ([[§19 Example꞉ Fixed End Temperatures|§19]], [[§20 Example꞉ Insulated Bar|§20]], [[§30 Solution of the Vibrating String Problem|§30]]): a sine series fits ends held at zero, a cosine series fits insulated ends.

## Functions of Period 2a

Suppose $f$ is periodic with period $2a$ ($2a$ in place of $p$ for later convenience). The functions $1, \sin(\pi x/a), \cos(\pi x/a), \sin(2\pi x/a), \cos(2\pi x/a), \ldots$ all have period $2a$ ([[§6 Periodic Functions and Fourier Series#^prop-6-1|Proposition §6.1]] with $\lambda = \pi/a$, since $2\pi/(\pi/a) = 2a$), and we relate $f$ to a series of them,

$$
f(x) \sim a_0 + \sum_{n=1}^{\infty} a_n\cos\Big(\frac{n\pi x}{a}\Big) + b_n\sin\Big(\frac{n\pi x}{a}\Big) .
$$

> [!theorem] Proposition §7.1: Fourier Coefficients for Period 2a
> The Fourier coefficients of a function $f$ of period $2a$ are
>
> $$
> a_0 = \frac{1}{2a}\int_{-a}^{a} f(x)\,dx, \qquad a_n = \frac1a\int_{-a}^{a} f(x)\cos\Big(\frac{n\pi x}{a}\Big)dx, \qquad b_n = \frac1a\int_{-a}^{a} f(x)\sin\Big(\frac{n\pi x}{a}\Big)dx . \qquad (1)
> $$
>
> They are obtained either by scaling from the formulas of [[§6 Periodic Functions and Fourier Series#^prop-6-4|Proposition §6.4]] or through orthogonality: for $n, m \ge 1$,
>
> $$
> \int_{-a}^{a}\cos\frac{n\pi x}{a}\sin\frac{m\pi x}{a}\,dx = 0, \qquad
> \int_{-a}^{a}\cos\frac{n\pi x}{a}\cos\frac{m\pi x}{a}\,dx = \int_{-a}^{a}\sin\frac{n\pi x}{a}\sin\frac{m\pi x}{a}\,dx = \begin{cases} 0, & n \ne m, \\ a, & n = m, \end{cases}
> $$
>
> and $\int_{-a}^{a}\cos(n\pi x/a)\,dx = \int_{-a}^{a}\sin(n\pi x/a)\,dx = 0$.
>
> *Powers: 1.2, Equation (1); Exercise 1.2.2*

^prop-7-1

> [!proof]+ Proof
> **By scaling.** Let $g(y) = f(ay/\pi)$. By [[§6 Periodic Functions and Fourier Series#^prop-6-1|Proposition §6.1]](2), $g$ has period $2a/(a/\pi) = 2\pi$, and its Fourier series is $g(y) \sim a_0 + \sum(a_n\cos ny + b_n\sin ny)$ with the coefficients of [[§6 Periodic Functions and Fourier Series#^def-6-2|Definition §6.2]]. Substitute $y = \pi x/a$, $dy = (\pi/a)\,dx$; as $y$ runs over $(-\pi, \pi)$, $x$ runs over $(-a, a)$:
>
> $$
> a_n = \frac1\pi\int_{-\pi}^{\pi} g(y)\cos ny\,dy = \frac1\pi\int_{-a}^{a} f(x)\cos\frac{n\pi x}{a}\cdot\frac\pi a\,dx = \frac1a\int_{-a}^{a} f(x)\cos\frac{n\pi x}{a}\,dx ,
> $$
>
> and in the same way $a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} g = \frac{1}{2a}\int_{-a}^{a} f$ and $b_n = \frac1a\int_{-a}^{a} f(x)\sin\frac{n\pi x}{a}\,dx$. In terms of $x$, $\cos ny = \cos(n\pi x/a)$ and $\sin ny = \sin(n\pi x/a)$, which is the series above.
>
> **The orthogonality relations** follow from [[§6 Periodic Functions and Fourier Series#^prop-6-3|Proposition §6.3]] by the same substitution: each integral over $(-a, a)$ equals $a/\pi$ times the corresponding integral over $(-\pi, \pi)$, which turns the values $0$ and $\pi$ into $0$ and $a$. With them, the derivation of [[§6 Periodic Functions and Fourier Series#^prop-6-4|Proposition §6.4]] gives (1) directly.

^pf-7-1

*Uses:* [[§6 Periodic Functions and Fourier Series#^prop-6-1|§6.1]], [[§6 Periodic Functions and Fourier Series#^prop-6-3|§6.3]], [[§6 Periodic Functions and Fourier Series#^prop-6-4|§6.4]], [[§6 Periodic Functions and Fourier Series#^def-6-2|Def. §6.2]]

> [!example] Example §7.1: The Rectified Sine |sin(πx)|
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
> We will see in [[§9 Uniform Convergence|§9]] that $|\sin(\pi x)|$ is equal to its series, and the series converges uniformly.
>
> *Powers: 1.2, first Example*

^ex-7-1

## Periodic Extension

It is often necessary to use a Fourier series for a function defined only on a finite interval. Such a representation is justified by making the given function part of a periodic function.

> [!definition] Definition §7.1: Periodic Extension
> If $f$ is defined on $-a < x < a$, its **periodic extension** $\bar f$ of period $2a$ is defined by
>
> $$
> \bar f(x) = f(x),\ -a < x < a; \qquad \bar f(x) = f(x + 2a),\ -3a < x < -a; \qquad \bar f(x) = f(x - 2a),\ a < x < 3a ,
> $$
>
> and so on up and down the $x$-axis: on each interval $(-a + 2ka, a + 2ka)$, $\bar f(x) = f(x - 2ka)$, whose argument falls in $(-a, a)$, where $f$ was originally given. Graphically, the graph of $f$ on $-a < x < a$ is a template, copied onto abutting intervals of length $2a$. (The values at $x = \pm a, \pm3a, \ldots$ are left open; see [[§8 Convergence of Fourier Series#^rem-8-1|§8]].)
>
> *Powers: 1.2 (text)*

^def-7-1

For the extended function, the coefficient formulas (1) read

$$
a_0 = \frac{1}{2a}\int_{-a}^{a}\bar f(x)\,dx, \qquad a_n = \frac1a\int_{-a}^{a}\bar f(x)\cos\Big(\frac{n\pi x}{a}\Big)dx, \qquad b_n = \frac1a\int_{-a}^{a}\bar f(x)\sin\Big(\frac{n\pi x}{a}\Big)dx . \qquad (2)
$$

They involve $\bar f$ only on $(-a, a)$, where $\bar f = f$. So if we are concerned with $f$ only on its original interval, the periodic extension is strictly formal, and we may write

$$
f(x) \sim a_0 + \sum_{n=1}^{\infty} a_n\cos\Big(\frac{n\pi x}{a}\Big) + b_n\sin\Big(\frac{n\pi x}{a}\Big), \qquad -a < x < a ,
$$

the inequality for $x$ recording that $f$ was defined only on $-a$ to $a$.

> [!example] Example §7.2: A Piecewise Function of Period 4
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

^ex-7-2

## Even and Odd Functions

The cosine is symmetric about the vertical axis and the sine is antisymmetric. These properties are useful in evaluating the coefficients.

> [!definition] Definition §7.2: Even and Odd Functions
> A function $g$ is **even** if $g(-x) = g(x)$; a function $h$ is **odd** if $h(-x) = -h(x)$. A function must be defined on a symmetric interval, say $-c < x < c$ (where $c$ might be $\infty$), to qualify as even or odd.
>
> An even function is symmetric about the vertical axis, an odd function symmetric in the origin. For example, $\sin kx$, $x$, $x^3$ and every other odd power of $x$ are odd on $-\infty < x < \infty$; $\cos kx$, $|x|$, $1 = x^0$, $x^2$ and every other even power of $x$ are even.
>
> *Powers: 1.2, Definition*

^def-7-2

> [!theorem] Proposition §7.2: Even and Odd Parts; Products
> Most functions are neither even nor odd, but any function defined on a symmetric interval is the sum of an even and an odd function:
>
> $$
> f(x) = \frac12\big(f(x) + f(-x)\big) + \frac12\big(f(x) - f(-x)\big) .
> $$
>
> Even and odd functions keep their symmetry under these operations:
>
> $$
> \text{even} + \text{even} = \text{even}, \quad \text{odd} + \text{odd} = \text{odd}, \quad \text{even}\times\text{even} = \text{even}, \quad \text{odd}\times\text{odd} = \text{even}, \quad \text{odd}\times\text{even} = \text{odd} .
> $$
>
> For example, $e^x = \cosh x + \sinh x$ is the decomposition of $e^x$ (Powers Exercise 1.2.4).
>
> *Powers: 1.2 (text)*

^prop-7-2

> [!proof]+ Proof
> Powers says "it is easy to show". Let $E(x) = \frac12(f(x) + f(-x))$ and $O(x) = \frac12(f(x) - f(-x))$. Then $E(-x) = \frac12(f(-x) + f(x)) = E(x)$ and $O(-x) = \frac12(f(-x) - f(x)) = -O(x)$, and $E + O = f$. For the rules, let $g_1, g_2$ be even and $h_1, h_2$ odd: $(g_1 + g_2)(-x) = g_1(x) + g_2(x)$; $(h_1 + h_2)(-x) = -(h_1 + h_2)(x)$; $g_1(-x)g_2(-x) = g_1(x)g_2(x)$; $h_1(-x)h_2(-x) = (-h_1(x))(-h_2(x)) = h_1(x)h_2(x)$; $h_1(-x)g_1(-x) = -h_1(x)g_1(x)$.

^pf-7-2

*Uses:* [[§7 Arbitrary Period and Half-Range Expansions#^def-7-2|Def. §7.2]]

> [!theorem] Theorem §7.3: Integrals of Even and Odd Functions
> Let $g$ be an even function defined on a symmetric interval $-a < x < a$. Then
>
> $$
> \int_{-a}^{a} g(x)\,dx = 2\int_0^a g(x)\,dx .
> $$
>
> Let $h$ be an odd function defined on a symmetric interval $-a < x < a$. Then
>
> $$
> \int_{-a}^{a} h(x)\,dx = 0 .
> $$
>
> *Powers: 1.2, Theorem 1*

^thm-7-3

> [!proof]+ Proof
> Powers leaves this as Exercise 1.2.14 ("the integral as a sum of signed areas": the area over $(-a, 0)$ is the mirror image of the area over $(0, a)$, with the same sign for even functions and the opposite sign for odd ones). In formulas: substitute $x = -y$ in the integral over $(-a, 0)$,
>
> $$
> \int_{-a}^{0} f(x)\,dx = \int_{a}^{0} f(-y)(-dy) = \int_0^a f(-y)\,dy ,
> $$
>
> which is $\int_0^a g$ for $f = g$ even and $-\int_0^a h$ for $f = h$ odd. Add $\int_0^a f$.

^pf-7-3

*Uses:* [[§7 Arbitrary Period and Half-Range Expansions#^def-7-2|Def. §7.2]]

> [!remark]- Connections
> - Stewart's version, with the same substitution: [[§38 The Substitution Rule#^thm-38-4|Calc Thm. §38.4]] (even and odd functions: [[§1 Four Ways to Represent a Function#^def-1-7|Calc Def. §1.7]]).

Now suppose $g$ is even on $-a < x < a$. Since the sine is odd, $g(x)\sin(n\pi x/a)$ is odd, so by Theorem §7.3

$$
b_n = \frac1a\int_{-a}^{a} g(x)\sin\Big(\frac{n\pi x}{a}\Big)dx = 0 :
$$

all the sine coefficients are zero. Since the cosine is even, so is $g(x)\cos(n\pi x/a)$, and $a_n = \frac1a\int_{-a}^{a} g(x)\cos\frac{n\pi x}{a}dx = \frac2a\int_0^a g(x)\cos\frac{n\pi x}{a}dx$: the cosine coefficients can be computed from an integral over $0$ to $a$. Parallel results hold for odd functions.

> [!theorem] Theorem §7.4: Fourier Series of Even and Odd Functions
> If $g$ is even on $-a < x < a$ ($g(-x) = g(x)$), then
>
> $$
> g(x) \sim a_0 + \sum_{n=1}^{\infty} a_n\cos\Big(\frac{n\pi x}{a}\Big), \quad -a < x < a, \qquad\text{where}\qquad a_0 = \frac1a\int_0^a g(x)\,dx, \quad a_n = \frac2a\int_0^a g(x)\cos\Big(\frac{n\pi x}{a}\Big)dx .
> $$
>
> If $h$ is odd on $-a < x < a$ ($h(-x) = -h(x)$), then
>
> $$
> h(x) \sim \sum_{n=1}^{\infty} b_n\sin\Big(\frac{n\pi x}{a}\Big), \quad -a < x < a, \qquad\text{where}\qquad b_n = \frac2a\int_0^a h(x)\sin\Big(\frac{n\pi x}{a}\Big)dx .
> $$
>
> *Powers: 1.2, Theorem 2*

^thm-7-4

> [!proof]+ Proof
> **$g$ even.** By Proposition §7.2, $g(x)\sin\frac{n\pi x}{a}$ is odd and $g(x)\cos\frac{n\pi x}{a}$ is even. By Theorem §7.3 applied to (1): $b_n = 0$; $a_0 = \frac{1}{2a}\int_{-a}^{a} g = \frac{1}{2a}\cdot 2\int_0^a g = \frac1a\int_0^a g$; $a_n = \frac1a\cdot 2\int_0^a g(x)\cos\frac{n\pi x}{a}dx$.
>
> **$h$ odd.** Now $h$ and $h(x)\cos\frac{n\pi x}{a}$ are odd and $h(x)\sin\frac{n\pi x}{a}$ is even, so $a_0 = a_n = 0$ and $b_n = \frac1a\cdot 2\int_0^a h(x)\sin\frac{n\pi x}{a}dx$.

^pf-7-4

*Uses:* [[§7 Arbitrary Period and Half-Range Expansions#^prop-7-1|§7.1]], [[§7 Arbitrary Period and Half-Range Expansions#^prop-7-2|§7.2]], [[§7 Arbitrary Period and Half-Range Expansions#^thm-7-3|§7.3]]

## Half-Range Expansions

Very frequently, a function given on an interval $0 < x < a$ must be represented by a Fourier series. There are infinitely many ways to do this, but two are especially simple and useful: extend the given function to $-a < x < a$ so that the extension is odd, or so that it is even.

> [!definition] Definition §7.3: Odd and Even Extensions
> Let $f$ be given for $0 < x < a$. The **odd extension** of $f$ is
>
> $$
> f_o(x) = \begin{cases} f(x), & 0 < x < a, \\ -f(-x), & -a < x < 0, \end{cases}
> $$
>
> and the **even extension** of $f$ is
>
> $$
> f_e(x) = \begin{cases} f(x), & 0 < x < a, \\ f(-x), & -a < x < 0 . \end{cases}
> $$
>
> If $-a < x < 0$ then $0 < -x < a$, so the values on the right are known from $f$. Graphically, the even extension reflects the graph of $f$ in the vertical axis; the odd extension reflects it first in the vertical axis and then in the horizontal axis. The periodic extensions of $f_o$ and $f_e$, of period $2a$, are the **odd periodic extension** $\bar f_o$ and the **even periodic extension** $\bar f_e$ of $f$. (The lecture also sets $f_o(0) = 0$, the only value that keeps $f_o$ odd, and $f_e(0) = f(0)$ when $f$ is given on $[0, a)$.)
>
> *Powers: 1.2, Definition; Source: 341 lecture 8.29*

^def-7-3

By Theorem §7.4, since $f_e$ is even and $f_o$ is odd,

$$
f_e(x) \sim a_0 + \sum_{n=1}^{\infty} a_n\cos\Big(\frac{n\pi x}{a}\Big), \qquad f_o(x) \sim \sum_{n=1}^{\infty} b_n\sin\Big(\frac{n\pi x}{a}\Big), \qquad -a < x < a .
$$

If the series converge, they represent periodic functions of period $2a$: the cosine series represents the even periodic extension $\bar f_e$, the sine series the odd periodic extension $\bar f_o$. When the problem is to represent $f$ on $0 < x < a$, where it was originally given, either may be used, because both $f_e$ and $f_o$ coincide with $f$ there.

> [!definition] Definition §7.4: Half-Range Expansions; Fourier Sine and Cosine Series
> If $f$ is given for $0 < x < a$, its **Fourier cosine series** is
>
> $$
> f(x) \sim a_0 + \sum_{n=1}^{\infty} a_n\cos\Big(\frac{n\pi x}{a}\Big), \quad 0 < x < a, \qquad a_0 = \frac1a\int_0^a f(x)\,dx, \quad a_n = \frac2a\int_0^a f(x)\cos\Big(\frac{n\pi x}{a}\Big)dx ,
> $$
>
> and its **Fourier sine series** is
>
> $$
> f(x) \sim \sum_{n=1}^{\infty} b_n\sin\Big(\frac{n\pi x}{a}\Big), \quad 0 < x < a, \qquad b_n = \frac2a\int_0^a f(x)\sin\Big(\frac{n\pi x}{a}\Big)dx .
> $$
>
> These two representations are called **half-range expansions**. They are the Fourier series of the even and the odd extension of $f$; the book needs them more than any other kind of Fourier series.
>
> *Powers: 1.2 (text)*

^def-7-4

> [!remark] Remark: Method — Choosing an Even or Odd Extension
> To expand a function $f$ given on $0 < x < a$:
> 1. Decide which extension is wanted. For a boundary value problem the boundary conditions decide: a sine series vanishes at $x = 0$ and $x = a$ (ends held at temperature zero, a string with fixed ends), a cosine series has zero derivative there (insulated ends); see [[§19 Example꞉ Fixed End Temperatures|§19]] and [[§20 Example꞉ Insulated Bar|§20]]. Otherwise either will do.
> 2. Sketch the odd or even periodic extension, of period $2a$, over a few periods; note where it jumps (the odd extension jumps at $x = 0$ unless $f(0+) = 0$).
> 3. Compute the coefficients from the formulas of Definition §7.4, which use $f$ only on $(0, a)$; there is no need to write down the extension.
> 4. Read off where the series converges to $f$ from the sketch ([[§8 Convergence of Fourier Series#^thm-8-1|Theorem §8.1]]).

^rem-7-1

## Examples

> [!example] Example §7.3: The Function x on (−1, 1) and on (0, 1)
> **(a) Period 2.** Let $f(x) = x$ for $-1 < x < 1$. Its periodic extension of period $2$ is a sawtooth (as in [[§6 Periodic Functions and Fourier Series#^ex-6-1|Example §6.1]], with period $2$). Since $f$ is odd, $a_0 = a_n = 0$, and with $a = 1$
>
> $$
> b_n = \int_{-1}^{1} x\sin(n\pi x)\,dx = -\frac{2\cos n\pi}{n\pi} = \frac2\pi\cdot\frac{(-1)^{n + 1}}{n} .
> $$
>
> **(b) Half-range expansions.** Now let $f(x) = x$ for $0 < x < 1$ only. Its odd periodic extension is the sawtooth of (a), so the sine series has the same coefficients:
>
> $$
> b_n = 2\int_0^1 x\sin(n\pi x)\,dx = -\frac{2}{n\pi}\cos n\pi .
> $$
>
> Its even periodic extension is a triangle wave, $|x|$ on $-1 < x < 1$ repeated with period $2$, and the cosine coefficients are
>
> $$
> a_0 = \int_0^1 x\,dx = \frac12, \qquad a_n = 2\int_0^1 x\cos(n\pi x)\,dx = 2\Big[\frac{x\sin n\pi x}{n\pi} + \frac{\cos n\pi x}{n^2\pi^2}\Big]_0^1 = -\frac{2}{n^2\pi^2}\big(1 - \cos n\pi\big) .
> $$
>
> So there are six correspondences (shown in [[§8 Convergence of Fourier Series|§8]]–[[§9 Uniform Convergence|§9]] to be equalities, except at the jumps of $\bar f_o$); the ranges of $x$ are crucial:
>
> $$
> \sum_{n=1}^{\infty}\frac{-2\cos n\pi}{n\pi}\sin(n\pi x) \sim \begin{cases} f(x) = x, & 0 < x < 1, \\ f_o(x) = x, & -1 < x < 1, \\ \bar f_o(x), & -\infty < x < \infty, \end{cases}
> \qquad
> \frac12 - \sum_{n=1}^{\infty}\frac{2(1 - \cos n\pi)}{n^2\pi^2}\cos(n\pi x) \sim \begin{cases} f(x) = x, & 0 < x < 1, \\ f_e(x) = |x|, & -1 < x < 1, \\ \bar f_e(x), & -\infty < x < \infty . \end{cases}
> $$
>
> *Powers: 1.2, second and third Examples; Source: 341 lecture 8.29, Example 2*

^ex-7-3

![[m341-7-1.svg]]
*Example §7.3: the odd periodic extension $\bar f_o$ (top) and the even periodic extension $\bar f_e$ (bottom) of $f(x) = x$, $0 < x < 1$ (heavy). The odd one is a sawtooth with jumps at the odd integers, where the sine series converges to the midpoint $0$ (dots); the even one is a continuous triangle wave with corners. The sine series represents the top function, the cosine series the bottom one, and both equal $x$ on $0 < x < 1$.*

> [!example] Example §7.4: Odd and Even Extensions of x²
> Let $f(x) = x^2$, $0 < x < 1$. Find the Fourier series of its odd and even extensions.
>
> **Odd extension** $f_o(x) = x^2$ for $0 < x < 1$, $-x^2$ for $-1 < x < 0$; its periodic extension has jumps at the odd integers (from $1$ to $-1$). Here $a_0 = a_n = 0$ and, integrating by parts twice,
>
> $$
> b_n = 2\int_0^1 x^2\sin(n\pi x)\,dx = \frac{2}{n\pi}\Big[-x^2\cos(n\pi x)\Big]_0^1 + \frac{2}{n\pi}\int_0^1 2x\cos(n\pi x)\,dx = \frac{2(-1)^{n + 1}}{n\pi} - \frac{4}{(n\pi)^2}\int_0^1\sin(n\pi x)\,dx = \frac{2(-1)^{n + 1}}{n\pi} + \frac{4}{(n\pi)^3}\big[(-1)^n - 1\big] .
> $$
>
> So $f_o(x) \sim \sum_{n=1}^{\infty}\Big\{\frac{2(-1)^{n + 1}}{n\pi} + \frac{4}{(n\pi)^3}\big[(-1)^n - 1\big]\Big\}\sin(n\pi x)$.
>
> **Even extension** $f_e(x) = x^2$ on $-1 < x < 1$, whose periodic extension is continuous (a chain of parabolic arches). Here $b_n = 0$ and
>
> $$
> a_0 = \frac11\int_0^1 x^2\,dx = \frac13, \qquad a_n = 2\int_0^1 x^2\cos(n\pi x)\,dx = \frac{2}{n\pi}\Big[x^2\sin(n\pi x)\Big]_0^1 - \frac{2}{n\pi}\int_0^1 2x\sin(n\pi x)\,dx = \frac{4}{(n\pi)^2}\Big[x\cos(n\pi x)\Big]_0^1 - \frac{4}{(n\pi)^2}\int_0^1\cos(n\pi x)\,dx = \frac{4(-1)^n}{(n\pi)^2} .
> $$
>
> So $f_e(x) \sim \frac13 + \sum_{n=1}^{\infty}\frac{4(-1)^n}{(n\pi)^2}\cos(n\pi x)$. The cosine coefficients decay like $1/n^2$, the sine coefficients only like $1/n$: the even extension is continuous, the odd one is not. [[§9 Uniform Convergence|§9]] makes this observation precise.
>
> *Source: 341 lecture 9.3, Example 2*

^ex-7-4

> [!example] Example §7.5: Odd Periodic Extension of a Triangle
> A function is given on $0 < x < 2$ by
>
> $$
> f(x) = \begin{cases} x, & 0 < x < 1, \\ 2 - x, & 1 < x < 2 . \end{cases}
> $$
>
> **(a)** Sketch the odd periodic extension $\bar f_o$ for $-4 < x < 4$. **(b)** Compute all Fourier coefficients of $\bar f_o$.
>
> **(a)** On $(0, 2)$ the graph is a tent rising from $(0, 0)$ to $(1, 1)$ and falling to $(2, 0)$; the odd extension adds an inverted tent on $(-2, 0)$ through $(-1, -1)$; repeating with period $4$ gives a continuous zigzag with peaks $1$ at $x = 1, -3$ and troughs $-1$ at $x = -1, 3$, crossing zero at the even integers.
>
> **(b)** Here $a = 2$ and $\bar f_o$ is odd, so $a_0 = a_n = 0$ and
>
> $$
> b_n = \frac22\Big[\int_0^1 x\sin\frac{n\pi x}{2}\,dx + \int_1^2 (2 - x)\sin\frac{n\pi x}{2}\,dx\Big] .
> $$
>
> With $\int x\sin kx\,dx = \frac{\sin kx}{k^2} - \frac{x\cos kx}{k}$ and $k = n\pi/2$, the first integral is $\frac{\sin k}{k^2} - \frac{\cos k}{k}$. In the second substitute $u = 2 - x$: since $\sin\frac{n\pi(2 - u)}{2} = \sin(n\pi - ku) = -(-1)^n\sin ku$, it equals $-(-1)^n\int_0^1 u\sin ku\,du = -(-1)^n\big(\frac{\sin k}{k^2} - \frac{\cos k}{k}\big)$. Now $\sin k = \sin\frac{n\pi}{2}$ is $0$ for even $n$, and $\cos k = 0$ for odd $n$. For odd $n$, $-(-1)^n = 1$ and the two integrals add to $\frac{2\sin k}{k^2}$; for even $n$ they cancel. In both cases
>
> $$
> b_n = \frac{8}{n^2\pi^2}\sin\frac{n\pi}{2}, \qquad \bar f_o(x) \sim \sum_{n=1}^{\infty}\frac{8}{n^2\pi^2}\sin\frac{n\pi}{2}\sin\frac{n\pi x}{2} = \sum_{k=1}^{\infty}\frac{8(-1)^{k - 1}}{(2k - 1)^2\pi^2}\sin\frac{(2k - 1)\pi x}{2} .
> $$
>
> *Source: 341 HW 1, Problem 5*

^ex-7-5
