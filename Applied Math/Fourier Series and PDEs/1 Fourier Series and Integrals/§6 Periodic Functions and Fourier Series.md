---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 1
section: 6
powers: "1.1"
aliases: ["Powers 1.1"]
tags: [fourier-series-and-pdes, math341]
---
← [[§5★ Green's Functions]] · ↑ [[· 1 Fourier Series and Integrals]] · [[§7 Arbitrary Period and Half-Range Expansions]] →

*Powers, Section 1.1 · MAT 341 lectures 8.27, 8.29 · HW 1.*

A Taylor series builds a function out of the powers $1, x, x^2, \ldots$; a Fourier series builds a periodic function out of $1, \cos x, \sin x, \cos 2x, \sin 2x, \ldots$, which all have period $2\pi$. This section asks the first of two questions about such a series: if $f(x) = a_0 + \sum (a_n\cos nx + b_n\sin nx)$, what must the coefficients be? The orthogonality relations answer it: multiplying by one of the functions and integrating over a period isolates one coefficient, so each coefficient is an integral of $f$. The second question, whether the series really adds up to $f$, is the subject of [[§8 Convergence of Fourier Series|§8]]–[[§11★ Mean Error and Convergence in Mean|§11★]]. Physically, a periodic signal (an acoustic wave, a vibrating string, a periodic temperature) is split into pure harmonics of frequencies $1, 2, 3, \ldots$ times the fundamental, and this splitting is what turns the heat, wave and potential equations of Chapters 2–4 into ordinary differential equations, one for each harmonic.

## Periodic Functions

> [!definition] Definition §6.1: Periodic Function
> A function $f$ is **periodic with period $p > 0$** if
> 1. $f(x)$ has been defined for all $x$, and
> 2. $f(x + p) = f(x)$ for all $x$.
>
> A periodic function has many periods: if $f(x + p) = f(x)$ for all $x$, then $f(x) = f(x + p) = f(x + 2p) = \cdots = f(x + np)$, and also $f(x - p) = f(x - p + p) = f(x)$, so $f(x) = f(x - p) = \cdots = f(x - np)$. Thus $f(x + np) = f(x)$ for every integer $n$, and $2\pi, 4\pi, \ldots, 2n\pi, \ldots$ are all periods of $\sin x$. Geometrically, the graph of a periodic function is a template over any interval of length $p$, copied up and down the $x$-axis.
>
> For example, $\sin x$ and $\cos x$ have period $2\pi$, $\tan x$ has period $\pi$, and $\sin(2\pi x/p)$, $\cos(2\pi x/p)$ have period $p$. The constant function $f(x) = 1$ has every $p > 0$ as a period (Powers Exercise 1.1.3).
>
> *Powers: 1.1 (text)*

^def-6-1

> [!theorem] Proposition §6.1: Operations on Periodic Functions
> Let $f$ and $g$ be periodic with a common period $p$, and let $a$, $b$ be constants.
> 1. $af(x) + bg(x)$ and $f(x)g(x)$ are periodic with period $p$.
> 2. For a constant $c > 0$, $h(x) = f(cx)$ is periodic with period $p/c$.
> 3. Every term of $a_0 + \sum_{n=1}^{\infty}(a_n\cos nx + b_n\sin nx)$ has period $2\pi$, so if the series converges, its sum is periodic with period $2\pi$. More generally, the terms of $a_0 + \sum_{n=1}^{\infty}(a_n\cos n\lambda x + b_n\sin n\lambda x)$, $\lambda > 0$, all have period $2\pi/\lambda$.
>
> *Powers: Exercise 1.1.6; Source: 341 lectures 8.27, 8.29*

^prop-6-1

> [!proof]+ Proof
> 1. $af(x + p) + bg(x + p) = af(x) + bg(x)$ and $f(x + p)g(x + p) = f(x)g(x)$ for all $x$.
> 2. $h(x + p/c) = f(c(x + p/c)) = f(cx + p) = f(cx) = h(x)$.
> 3. By 2, $\cos nx$ and $\sin nx$ have period $2\pi/n$, hence (Definition §6.1) also period $n \cdot 2\pi/n = 2\pi$; similarly $\cos n\lambda x$ and $\sin n\lambda x$ have period $2\pi/(n\lambda)$, hence $2\pi/\lambda$. Each partial sum has period $2\pi$ by 1, and if $S_N(x) \to S(x)$ for every $x$, then $S(x + 2\pi) = \lim S_N(x + 2\pi) = \lim S_N(x) = S(x)$.

^pf-6-1

*Uses:* [[§6 Periodic Functions and Fourier Series#^def-6-1|Def. §6.1]]

> [!theorem] Proposition §6.2: The Integral Over Any Period
> Suppose $f$ has period $p$ and is integrable over intervals of length $p$. Then for every $c$,
>
> $$
> \int_c^{c + p} f(x)\,dx = \int_0^p f(x)\,dx .
> $$
>
> *Powers: Exercise 1.1.5; Source: 341 HW 1, Problem 2*

^prop-6-2

> [!proof]+ Proof
> **For continuous $f$** (the homework's route). Let $F(x) = \int_x^{x + p} f(t)\,dt = \int_0^{x + p} f(t)\,dt - \int_0^x f(t)\,dt$. By the fundamental theorem of calculus (the Newton–Leibniz formula $\frac{d}{dx}\int_0^x g = g(x)$) and the chain rule,
>
> $$
> F'(x) = f(x + p) - f(x) = 0 ,
> $$
>
> because $f$ has period $p$. A function with zero derivative on $\mathbb{R}$ is constant, so $F(c) = F(0)$, which is the claim.
>
> **In general** (Powers' hint: the integral is a net signed area). Choose the integer $k$ with $kp \le c < (k + 1)p$ and split at $(k + 1)p$:
>
> $$
> \int_c^{c + p} f = \int_c^{(k + 1)p} f + \int_{(k + 1)p}^{c + p} f .
> $$
>
> In the second integral substitute $x = y + p$: it becomes $\int_{kp}^{c} f(y + p)\,dy = \int_{kp}^{c} f(y)\,dy$. Adding, $\int_c^{c + p} f = \int_{kp}^{(k + 1)p} f$, and the substitution $x = y + kp$ (using $f(y + kp) = f(y)$) turns this into $\int_0^p f$. The piece of area cut off at the left end is the same as the piece added at the right end.

^pf-6-2

*Uses:* [[§6 Periodic Functions and Fourier Series#^def-6-1|Def. §6.1]], [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]] (FTC), [[§29 The Mean Value Theorem#^cor-29-4|451 Cor. §29.4]] (zero derivative means constant)

So a Fourier coefficient of a $2\pi$-periodic function may be computed over $(0, 2\pi)$, or over any other interval of length $2\pi$, instead of $(-\pi, \pi)$; [[§6 Periodic Functions and Fourier Series#^ex-6-2|Example §6.2]] uses this.

## Fourier Series

If $f$ is periodic with period $2\pi$, we attempt to represent it in the form of an infinite series

$$
f(x) = a_0 + \sum_{n=1}^{\infty}\big(a_n\cos nx + b_n\sin nx\big) . \qquad (1)
$$

By Proposition §6.1 the right side, if it converges, has period $2\pi$. Two questions must be answered: **(a)** what values must $a_0$, $a_n$, $b_n$ have? **(b)** If the appropriate values are assigned, does the series actually represent $f$? Question (a) looks hopeless, since (1) is one equation in infinitely many unknowns, but the following relations make it easy.

> [!theorem] Proposition §6.3: Orthogonality Relations
> For integers $n, m \ge 0$,
>
> $$
> \int_{-\pi}^{\pi}\sin nx\,dx = 0, \qquad \int_{-\pi}^{\pi}\cos nx\,dx = \begin{cases} 0, & n \ne 0, \\ 2\pi, & n = 0, \end{cases}
> $$
>
> $$
> \int_{-\pi}^{\pi}\sin nx\cos mx\,dx = 0, \qquad
> \int_{-\pi}^{\pi}\sin nx\sin mx\,dx = \begin{cases} 0, & n \ne m, \\ \pi, & n = m \ne 0, \end{cases} \qquad
> \int_{-\pi}^{\pi}\cos nx\cos mx\,dx = \begin{cases} 0, & n \ne m, \\ \pi, & n = m \ne 0 . \end{cases}
> $$
>
> In words: the integral over $(-\pi, \pi)$ of the product of any two *different* functions from the list $1, \cos x, \sin x, \cos 2x, \sin 2x, \ldots$ is zero. (The word *orthogonality* is not meant in the geometric sense here; see Connections.)
>
> *Powers: 1.1, Table 1*

^prop-6-3

> [!proof]+ Proof
> Powers states Table 1 without proof; this is the lecture's "calculation lemma". For an integer $k \ne 0$,
>
> $$
> \int_{-\pi}^{\pi}\cos kx\,dx = \Big[\frac{\sin kx}{k}\Big]_{-\pi}^{\pi} = 0, \qquad \int_{-\pi}^{\pi}\sin kx\,dx = \Big[-\frac{\cos kx}{k}\Big]_{-\pi}^{\pi} = 0 ,
> $$
>
> since $\sin(\pm k\pi) = 0$ and $\cos k\pi = \cos(-k\pi)$; and $\int_{-\pi}^{\pi}\cos 0x\,dx = 2\pi$, $\int_{-\pi}^{\pi}\sin 0x\,dx = 0$. The products reduce to these by the product-to-sum identities
>
> $$
> \cos nx\cos mx = \tfrac12\big[\cos(n - m)x + \cos(n + m)x\big], \quad
> \sin nx\sin mx = \tfrac12\big[\cos(n - m)x - \cos(n + m)x\big], \quad
> \sin nx\cos mx = \tfrac12\big[\sin(n + m)x + \sin(n - m)x\big] .
> $$
>
> Every sine integrates to $0$, so $\int\sin nx\cos mx = 0$ for all $n, m$. If $n \ne m$, both $n - m$ and $n + m$ are nonzero integers and the cosine integrals vanish too. If $n = m \ne 0$, then $\cos(n - m)x = 1$ contributes $\frac12 \cdot 2\pi = \pi$ and $\cos 2nx$ contributes $0$, giving $\pi$ for $\cos^2$ and for $\sin^2$.

^pf-6-3

> [!remark]- Connections
> - The same computation in Stewart: [[§45 Trigonometric Integrals#^rem-45-3|Calc Remark §45.3]]. On $[0, 2\pi]$, as orthogonality in the inner product space $C[0, 2\pi]$ with $\langle f, g\rangle = \int fg$: [[§47 Applications of Inner Product Spaces#^prop-47-2|235 Prop. §47.2]].
> - Normalized, $\frac{1}{\sqrt{2\pi}}, \frac{\cos x}{\sqrt\pi}, \frac{\sin x}{\sqrt\pi}, \ldots$ is an orthonormal list in $C[-\pi, \pi]$, [[§20 Orthonormal Bases#^ladr-6-23|LADR 6.23]](d); in complex form it is the Fourier basis of $L^2[0, 2\pi]$, [[§20 Orthonormal Sets and Bases#^thm-20-11|556 Thm. §20.11]]. So "orthogonal" is meant in exactly the sense of these inner products.
> - See also: [[§42 Definite Integrals of Functions w(t)#^ex-42-4|342 Ex. §42.4]] (orthogonality of $e^{im\theta}$ and $e^{in\theta}$; these relations are its real and imaginary parts).

The idea now is that if (1) is a true equality, both sides must give the same result after the same operation. Multiply both sides by one of the functions in the series and integrate from $-\pi$ to $\pi$; the orthogonality relations kill all but one term. This assumes that the series may be integrated term by term, which is sometimes difficult to justify; it is justified in [[§10 Operations on Fourier Series#^thm-10-4|Theorem §10.4]] (Powers 1.5, Theorem 4).

> [!theorem] Proposition §6.4: Formulas for the Coefficients
> If a function $f$ of period $2\pi$ equals the series (1),
>
> $$
> f(x) = a_0 + \sum_{n=1}^{\infty}\big(a_n\cos nx + b_n\sin nx\big) , \qquad (2)
> $$
>
> and the series may be integrated term by term after multiplication by $1$, $\cos mx$ or $\sin mx$, then the coefficients must be
>
> $$
> a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)\,dx , \qquad (3)
> $$
>
> $$
> a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos nx\,dx , \qquad (4)
> $$
>
> $$
> b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\sin nx\,dx . \qquad (5)
> $$
>
> *Powers: 1.1, Equations (2)–(5)*

^prop-6-4

> [!proof]+ Proof
> **$a_0$.** Multiply (2) by the constant $1 = \cos 0x$ and integrate from $-\pi$ to $\pi$ term by term:
>
> $$
> \int_{-\pi}^{\pi} f(x)\,dx = \int_{-\pi}^{\pi} a_0\,dx + \sum_{n=1}^{\infty}\int_{-\pi}^{\pi}\big(a_n\cos nx + b_n\sin nx\big)\,dx .
> $$
>
> By Proposition §6.3 every integral in the sum is zero, so the right side is $2\pi a_0$, which gives (3).
>
> **$b_m$.** Fix an integer $m \ge 1$, multiply (2) by $\sin mx$ and integrate:
>
> $$
> \int_{-\pi}^{\pi} f(x)\sin mx\,dx = \int_{-\pi}^{\pi} a_0\sin mx\,dx + \sum_{n=1}^{\infty} a_n\int_{-\pi}^{\pi}\cos nx\sin mx\,dx + \sum_{n=1}^{\infty} b_n\int_{-\pi}^{\pi}\sin nx\sin mx\,dx .
> $$
>
> By Proposition §6.3 all terms containing $a_0$ or $a_n$ vanish, and of the terms containing a $b_n$ the only nonzero one is $n = m$ ($n$ is the summation index and runs through $1, 2, \ldots$; $m$ is fixed, so $n = m$ exactly once), where the integral is $\pi$. So $\int_{-\pi}^{\pi} f(x)\sin mx\,dx = \pi b_m$, which is (5).
>
> **$a_m$.** Multiplying (2) by $\cos mx$ ($m \ge 1$) and integrating in the same way leaves only $a_m\int_{-\pi}^{\pi}\cos^2 mx\,dx = \pi a_m$, which is (4).

^pf-6-4

*Uses:* [[§6 Periodic Functions and Fourier Series#^prop-6-3|§6.3]]

> [!definition] Definition §6.2: Fourier Series; Fourier Coefficients
> Let $f$ be periodic with period $2\pi$ (and integrable over a period). The numbers $a_0$, $a_n$, $b_n$ given by (3)–(5) are the **Fourier coefficients** of $f$, and the series
>
> $$
> f(x) \sim a_0 + \sum_{n=1}^{\infty}\big(a_n\cos nx + b_n\sin nx\big)
> $$
>
> is the **Fourier series** of $f$. The sign $\sim$ means that the series *corresponds to* $f$: question (b), whether it equals $f$, has not been answered yet ([[§8 Convergence of Fourier Series#^thm-8-1|Theorem §8.1]]). In words, $a_0$ is the **mean value** of $f$ over one period.
>
> *Powers: 1.1 (text)*

^def-6-2

> [!remark]- Connections
> - With the inner product $\langle f, g\rangle = \int_{-\pi}^{\pi} fg$, (3)–(5) say $a_n = \langle f, \cos nx\rangle/\langle\cos nx, \cos nx\rangle$: each coefficient is the coordinate of $f$ along one orthogonal direction, as for an orthonormal basis in finite dimensions, [[§20 Orthonormal Bases#^ladr-6-30|LADR 6.30]]. Lay derives the same formulas as an orthogonal projection, [[§47 Applications of Inner Product Spaces#^thm-47-3|235 Thm. §47.3]], but writes the constant term as $a_0/2$ with $a_0 = \frac1\pi\int f$; Powers' $a_0$ is that $a_0/2$.
> - Fourier series as expansions in an orthonormal basis of $L^2$, converging in norm: [[§20 Orthonormal Sets and Bases#^rem-20-9|556 Remark: Fourier Series]].

> [!theorem] Proposition §6.5: Special Values of Sine and Cosine
> For $n = 0, \pm1, \pm2, \ldots$,
>
> $$
> \sin n\pi = 0, \qquad \cos n\pi = (-1)^n, \qquad \sin\frac{(2n - 1)\pi}{2} = (-1)^{n + 1}, \qquad \cos\frac{(2n - 1)\pi}{2} = 0 .
> $$
>
> The second pair involves only the *odd* multiples of $\pi/2$; the even multiples are covered by the first pair.
>
> *Powers: 1.1 (text)*

^prop-6-5

> [!proof]+ Proof
> $\sin x = 0$ exactly at the integer multiples of $\pi$, and $\cos n\pi$ alternates $1, -1, 1, \ldots$ because $\cos(x + \pi) = -\cos x$. The odd multiples $(2n - 1)\pi/2$ are the zeros of $\cos x$, and $\sin\frac{(2n - 1)\pi}{2} = \sin\big(n\pi - \frac\pi2\big) = -\cos n\pi = (-1)^{n + 1}$.

^pf-6-5

> [!remark] Remark: Method — Computing a Fourier Series of Period 2π
> 1. Sketch the periodic function over two or three periods, to see its symmetry and its jumps.
> 2. Compute $a_0$, the mean value (3); often it can be read off the sketch.
> 3. Compute $a_n$ and $b_n$ from (4)–(5), integrating separately over the pieces where $f$ has a single formula. Products like $x\cos nx$, $x^2\sin nx$ need integration by parts; then simplify with Proposition §6.5.
> 4. Any interval of length $2\pi$ may replace $(-\pi, \pi)$ (Proposition §6.2), and symmetry can halve the work: odd functions have only sines and even functions only cosines ([[§7 Arbitrary Period and Half-Range Expansions#^thm-7-4|Theorem §7.4]]).
> 5. Write the result with $\sim$, and check it: the coefficients should tend to $0$ ([[§11★ Mean Error and Convergence in Mean#^cor-11-5|Corollary §11.5]]).

^rem-6-1

## Examples

> [!example] Example §6.1: The Sawtooth f(x) = x
> Suppose $f$ is periodic with period $2\pi$ and $f(x) = x$ for $-\pi < x < \pi$. Its graph is a sawtooth: lines of slope $1$ through $0, \pm2\pi, \pm4\pi, \ldots$, jumping down by $2\pi$ at $x = \pm\pi, \pm3\pi, \ldots$ (figure below).
>
> By (3)–(5),
>
> $$
> a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} x\,dx = 0, \qquad
> a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} x\cos nx\,dx = \frac{1}{\pi}\Big[\frac{\cos nx}{n^2} + \frac{x\sin nx}{n}\Big]_{-\pi}^{\pi} = 0
> $$
>
> (the bracket takes the same value at $\pm\pi$), and, integrating by parts with $x\,d\big(-\frac{\cos nx}{n}\big)$,
>
> $$
> b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} x\sin nx\,dx = \frac{1}{\pi}\Big[\frac{\sin nx}{n^2} - \frac{x\cos nx}{n}\Big]_{-\pi}^{\pi} = \frac{1}{\pi}\cdot\frac{-\pi\cos n\pi - \pi\cos n\pi}{n} = -\frac{2\cos n\pi}{n} = \frac{2}{n}(-1)^{n + 1} .
> $$
>
> Thus
>
> $$
> f(x) \sim \sum_{n=1}^{\infty}\frac{2(-1)^{n + 1}}{n}\sin nx = 2\Big(\sin x - \frac12\sin 2x + \frac13\sin 3x - \cdots\Big) .
> $$
>
> *Powers: 1.1, Example; Source: 341 lecture 8.29, Example 1*

^ex-6-1

![[m341-6-1.svg]]
*The sawtooth of Example §6.1 (black) and the partial sums $S_1 = 2\sin x$, $S_3$ and $S_{10}$ of its Fourier series. Inside $(-\pi, \pi)$ the partial sums approach the line $y = x$; at the jumps $x = \pm\pi$ every partial sum is $0$, the midpoint of the jump, and just inside the jumps they overshoot ([[§9 Uniform Convergence#^rem-9-1|Gibbs' phenomenon]]).*

> [!example] Example §6.2: Two Periodic Functions from HW 1
> The following functions are periodic with period $2\pi$. Sketch them on $(-3\pi, 3\pi)$ and find their Fourier series. **(a)** $f(x) = 3x$, $-\pi < x < \pi$. **(b)** $f(x) = x$, $0 < x < 2\pi$.
>
> **(a)** The graph is the sawtooth of Example §6.1 stretched vertically by $3$: segments of slope $3$ rising from $-3\pi$ to $3\pi$ over each period $(-\pi + 2k\pi, \pi + 2k\pi)$. The coefficients are $3$ times those of Example §6.1 (the factor $3$ comes out of each integral):
>
> $$
> a_0 = a_n = 0, \qquad b_n = \frac1\pi\int_{-\pi}^{\pi}3x\sin nx\,dx = \frac{6(-1)^{n + 1}}{n}, \qquad f(x) \sim \sum_{n=1}^{\infty}\frac{6(-1)^{n + 1}}{n}\sin nx .
> $$
>
> **(b)** Now the segments rise from $0$ to $2\pi$ over $(2k\pi, 2(k + 1)\pi)$. By Proposition §6.2 the coefficients may be computed over $(0, 2\pi)$, where $f$ has the single formula $x$:
>
> $$
> a_0 = \frac{1}{2\pi}\int_0^{2\pi} x\,dx = \frac{1}{2\pi}\cdot\frac{(2\pi)^2}{2} = \pi, \qquad
> a_n = \frac1\pi\Big[\frac{\cos nx}{n^2} + \frac{x\sin nx}{n}\Big]_0^{2\pi} = \frac1\pi\Big(\frac{1}{n^2} - \frac{1}{n^2}\Big) = 0,
> $$
>
> $$
> b_n = \frac1\pi\Big[\frac{\sin nx}{n^2} - \frac{x\cos nx}{n}\Big]_0^{2\pi} = \frac1\pi\Big(-\frac{2\pi}{n}\Big) = -\frac2n .
> $$
>
> So $f(x) \sim \pi - \sum_{n=1}^{\infty}\frac2n\sin nx$. Over $(-\pi, \pi)$ instead, $f(x) = 2\pi + x$ on $(-\pi, 0)$ and $x$ on $(0, \pi)$, and splitting the integrals there gives the same coefficients. Check: $f(x) - \pi = x - \pi$ on $(0, 2\pi)$ is the sawtooth of Example §6.1 shifted right by $\pi$, and $\sin n(x - \pi) = (-1)^n\sin nx$ turns $\sum\frac{2(-1)^{n + 1}}{n}\sin n(x - \pi)$ into $-\sum\frac2n\sin nx$.
>
> *The key writes the integrand of $b_n$ in (a) as $3x\sin x$; its result $6(-1)^{n - 1}/n$ is the one above.*
>
> *Source: 341 HW 1, Problem 4*

^ex-6-2

> [!example] Example §6.3: Coefficients in an Orthonormal System
> Let $f_1, f_2, \ldots$ be smooth functions on $[0, 1]$ with
>
> $$
> \int_0^1 f_i^2(x)\,dx = 1, \qquad \int_0^1 f_i(x)f_j(x)\,dx = 0 \quad (i \ne j) .
> $$
>
> If a smooth function $g$ can be written $g(x) = \sum_{i=1}^{\infty} a_if_i(x)$, use the approach of this section to find $a_i$.
>
> Multiply by a fixed $f_j$ and integrate over $[0, 1]$ term by term (assuming, as in Proposition §6.4, that this is allowed):
>
> $$
> \int_0^1 g(x)f_j(x)\,dx = \sum_{i=1}^{\infty} a_i\int_0^1 f_i(x)f_j(x)\,dx = \sum_{i=1}^{\infty} a_i\delta_{ij} = a_j ,
> $$
>
> where $\delta_{ij} = 1$ if $i = j$ and $0$ otherwise. So $a_j = \int_0^1 g(x)f_j(x)\,dx$. Proposition §6.4 is the case of the system $1, \cos nx, \sin nx$ on $(-\pi, \pi)$, which is orthogonal but not normalized; the factors $\frac{1}{2\pi}$ and $\frac1\pi$ in (3)–(5) are $1/\int\phi^2$ for $\phi = 1$ and $\phi = \cos nx, \sin nx$. In the language of inner products, $\{f_i\}$ is an orthonormal set ([[§20 Orthonormal Sets and Bases#^def-20-1|556 Def. §20.1]]) and $a_j = \langle g, f_j\rangle$. The same computation recurs for every eigenfunction expansion in this subject ([[§24 Expansion in Series of Eigenfunctions#^prop-24-1|Proposition §24.1]]).
>
> *Source: 341 HW 1, Problem 3*

^ex-6-3
