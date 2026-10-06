---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 1
section: 7
powers: "1.2"
aliases: ["Powers 1.2 (cont.)"]
tags: [fourier-series-and-pdes, math341]
---
← [[§7 Arbitrary Period and Half-Range Expansions]] · ↑ [[· 1 Fourier Series and Integrals]] →

*Powers, Section 1.2 · MAT 341 lectures 8.29, 9.3 · HW 1.*

Symmetry halves the work: even functions have only cosine terms and odd functions only sine terms. Most important for the rest of the book, a function given on $0 < x < a$ can be extended to $-a < x < a$ as an odd or as an even function, which produces its Fourier sine series and its Fourier cosine series, the half-range expansions. These are the series that appear when the heat and wave equations on a rod or string of length $a$ are solved by separation of variables ([[§19 Example꞉ Fixed End Temperatures|§19]], [[§20 Example꞉ Insulated Bar|§20]], [[§30 Solution of the Vibrating String Problem|§30]]): a sine series fits ends held at zero, a cosine series fits insulated ends.

## Even and Odd Functions

The cosine is symmetric about the vertical axis and the sine is antisymmetric. These properties are useful in evaluating the coefficients.

> [!definition] Definition §7.2: Even and Odd Functions
> A function $g$ is **even** if $g(-x) = g(x)$; a function $h$ is **odd** if $h(-x) = -h(x)$. A function must be defined on a symmetric interval, say $-c < x < c$ (where $c$ might be $\infty$), to qualify as even or odd.
>
> An even function is symmetric about the vertical axis, an odd function symmetric in the origin. For example, $\sin kx$, $x$, $x^3$ and every other odd power of $x$ are odd on $-\infty < x < \infty$; $\cos kx$, $|x|$, $1 = x^0$, $x^2$ and every other even power of $x$ are even.
>
> *Powers: 1.2, Definition*

^def-7-2

> [!remark]- Connections
> - See also: [[§1 Four Ways to Represent a Function#^def-1-7|Calc Def. §1.7]] (the same definition) and [[§22 Projection and Orthogonal Decomposition#^prop-22-7|556 Prop. §22.7]] (in $L^2[-1, 1]$ the even and the odd functions are orthogonal complements and every $f$ is uniquely $f_e + f_o$; the cosine and sine parts of a Fourier series are the series of $f_e$ and $f_o$).

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

*Uses:* [[§7a Even and Odd Functions; Half-Range Expansions#^def-7-2|Def. §7.2]]

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

*Uses:* [[§7a Even and Odd Functions; Half-Range Expansions#^def-7-2|Def. §7.2]]

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

*Uses:* [[§7 Arbitrary Period and Half-Range Expansions#^prop-7-1|§7.1]], [[§7a Even and Odd Functions; Half-Range Expansions#^prop-7-2|§7.2]], [[§7a Even and Odd Functions; Half-Range Expansions#^thm-7-3|§7.3]]

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

> [!definition] Definition §7.4: Fourier Cosine Series
> If $f$ is given for $0 < x < a$, its **Fourier cosine series** is
>
> $$
> f(x) \sim a_0 + \sum_{n=1}^{\infty} a_n\cos\Big(\frac{n\pi x}{a}\Big), \quad 0 < x < a, \qquad a_0 = \frac1a\int_0^a f(x)\,dx, \quad a_n = \frac2a\int_0^a f(x)\cos\Big(\frac{n\pi x}{a}\Big)dx .
> $$
>
> *Powers: 1.2 (text)*

^def-7-4

> [!definition] Definition §7.4: Fourier Sine Series
> If $f$ is given for $0 < x < a$, its **Fourier sine series** is
>
> $$
> f(x) \sim \sum_{n=1}^{\infty} b_n\sin\Big(\frac{n\pi x}{a}\Big), \quad 0 < x < a, \qquad b_n = \frac2a\int_0^a f(x)\sin\Big(\frac{n\pi x}{a}\Big)dx .
> $$
>
> These two representations, the cosine series of [[§7a Even and Odd Functions; Half-Range Expansions#^def-7-4|Definition §7.4]] and the sine series, are called **half-range expansions**. They are the Fourier series of the even and the odd extension of $f$; the book needs them more than any other kind of Fourier series.
>
> *Powers: 1.2 (text)*

^def-7-new1

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
> So there are six correspondences (equalities by [[§8 Convergence of Fourier Series#^thm-8-1|Theorem §8.1]], except at the jumps of $\bar f_o$); the ranges of $x$ are crucial:
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
> So $f_e(x) \sim \frac13 + \sum_{n=1}^{\infty}\frac{4(-1)^n}{(n\pi)^2}\cos(n\pi x)$. The cosine coefficients decay like $1/n^2$, the sine coefficients only like $1/n$: the even extension is continuous, the odd one is not. [[§9 Uniform Convergence#^thm-9-1|Theorem §9.1]] and [[§9 Uniform Convergence#^thm-9-3|Theorem §9.3]] make this observation precise.
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
