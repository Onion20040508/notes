---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 1
section: 14
powers: "1.9"
aliases: ["Powers 1.9"]
tags: [fourier-series-and-pdes, math341]
---
← [[§13★ Numerical Determination of Fourier Coefficients]] · ↑ [[· 1 Fourier Series and Integrals]] · [[§15★ Complex Methods]] →

*Powers, Section 1.9 · MAT 341 lectures 10.3, 10.22 · HW 9 · Midterm 2 · Practice Midterm 2.*

Fourier series represent periodic functions, and through periodic extension functions on a finite interval. A nonperiodic function on $-\infty < x < \infty$ has no period to expand over, but letting the period $2a$ tend to infinity turns the sum over the frequencies $n\pi/a$ into an integral over all frequencies $\lambda \ge 0$: $f$ becomes a continuous superposition of $\cos(\lambda x)$ and $\sin(\lambda x)$ with weights $A(\lambda)$ and $B(\lambda)$. The Fourier integral theorem makes this precise for sectionally smooth, absolutely integrable functions, and for functions on $0 < x < \infty$ it gives the Fourier cosine and sine integrals. These are the tool for heat conduction in a semi-infinite or infinite rod ([[§26 Semi-Infinite Rod|§26]], [[§27 Infinite Rod|§27]]), and more generally for any problem on an unbounded interval where separation of variables produces a continuum of modes instead of a sequence.

## From Fourier Series to Fourier Integral

Suppose $f(x)$ is defined for $-\infty < x < \infty$ and is sectionally smooth in every finite interval. Then for any $a > 0$, $f$ can be represented in the interval $-a < x < a$ by its Fourier series ([[§12★ Proof of Convergence#^cor-12-5|Corollary §12.5]]):

$$
f(x) = a_0 + \sum_{n=1}^{\infty} a_n\cos\Big(\frac{n\pi x}{a}\Big) + b_n\sin\Big(\frac{n\pi x}{a}\Big), \qquad -a < x < a, \qquad (1)
$$

with $a_0 = \frac{1}{2a}\int_{-a}^{a} f$, $a_n = \frac1a\int_{-a}^{a} f(x)\cos\big(\frac{n\pi x}a\big)dx$, $b_n = \frac1a\int_{-a}^{a} f(x)\sin\big(\frac{n\pi x}a\big)dx$. Let $\lambda_n = n\pi/a$ and define

$$
A_a(\lambda) = \frac1\pi\int_{-a}^{a} f(x)\cos(\lambda x)\,dx, \qquad B_a(\lambda) = \frac1\pi\int_{-a}^{a} f(x)\sin(\lambda x)\,dx . \qquad (3)
$$

Then $a_n = \frac\pi a A_a(\lambda_n)$ and $b_n = \frac\pi a B_a(\lambda_n)$, and the series (1) becomes

$$
f(x) = a_0 + \sum_{n=1}^{\infty}\big[A_a(\lambda_n)\cos(\lambda_n x) + B_a(\lambda_n)\sin(\lambda_n x)\big]\Delta\lambda, \qquad -a < x < a, \qquad (4)
$$

where $\Delta\lambda = \pi/a = \lambda_{n+1} - \lambda_n$.

> [!remark] Remark: Why It Works
> Equation (4) is written to look like a Riemann sum ([[§35 The Definite Integral#^def-35-2|Calc Def. §35.2]]) for an integral over $0 < \lambda < \infty$, with the frequencies $\lambda_n = n\pi/a$ as sample points spaced $\Delta\lambda = \pi/a$ apart. Imagine $a$ increasing to infinity. Then $\Delta\lambda \to 0$, and
>
> $$
> A_a(\lambda) \to A(\lambda) = \frac1\pi\int_{-\infty}^{\infty} f(x)\cos(\lambda x)\,dx, \qquad B_a(\lambda) \to B(\lambda) = \frac1\pi\int_{-\infty}^{\infty} f(x)\sin(\lambda x)\,dx . \qquad (5)\text{–}(6)
> $$
>
> If $\int_{-\infty}^{\infty}|f(x)|\,dx$ is finite, then $|a_0| \le \frac{1}{2a}\int_{-\infty}^{\infty}|f| \to 0$. So (4) suggests
>
> $$
> f(x) = \int_0^{\infty}\big[A(\lambda)\cos(\lambda x) + B(\lambda)\sin(\lambda x)\big]\,d\lambda, \qquad -\infty < x < \infty . \qquad (7)
> $$
>
> This derivation is not a proof: two limits, $a \to \infty$ inside $A_a$ and $\Delta\lambda \to 0$ in the sum, are taken at once, over an infinite range of $\lambda$. But it does suggest the theorem below, and it explains the factor $\frac1\pi$: it is the $\frac1a$ of the series coefficients with $\frac{\pi}{a}$ moved into $\Delta\lambda$.

^rem-14-1

## The Fourier Integral Theorem

> [!definition] Definition §14.1: Fourier Integral Coefficient Functions
> Let $f(x)$ be defined for $-\infty < x < \infty$ with $\int_{-\infty}^{\infty}|f(x)|\,dx$ finite. The functions
>
> $$
> A(\lambda) = \frac1\pi\int_{-\infty}^{\infty} f(x)\cos(\lambda x)\,dx, \qquad B(\lambda) = \frac1\pi\int_{-\infty}^{\infty} f(x)\sin(\lambda x)\,dx \qquad (9)
> $$
>
> are the **Fourier integral coefficient functions** of $f$.
>
> *Powers: 1.9, Equations (8)–(9) and text*

^def-14-1

> [!definition] Definition §14.1: Fourier Integral
> With the coefficient functions of [[§14 Fourier Integral#^def-14-1|Definition §14.1]],
>
> $$
> \int_0^{\infty}\big(A(\lambda)\cos(\lambda x) + B(\lambda)\sin(\lambda x)\big)\,d\lambda
> $$
>
> is the **Fourier integral** of $f$. When it equals $f$ (in the sense of Theorem §14.1), the equation (8) below is the **Fourier integral representation** of $f$.
>
> *Powers: 1.9, Equations (8)–(9) and text*

^def-14-new1

> [!theorem] Theorem §14.1: Fourier Integral Representation Theorem
> Let $f(x)$ be sectionally smooth on every finite interval, and let $\int_{-\infty}^{\infty}|f(x)|\,dx$ be finite. Then at every point $x$,
>
> $$
> \int_0^{\infty}\big(A(\lambda)\cos(\lambda x) + B(\lambda)\sin(\lambda x)\big)\,d\lambda = \frac12\big(f(x+) + f(x-)\big), \qquad -\infty < x < \infty , \qquad (8)
> $$
>
> where $A$ and $B$ are given by (9).
>
> *Powers: 1.9, Fourier Integral Representation Theorem*

^thm-14-1

*Powers omits the proof, and no other subject in the vault proves it. It is the continuous analogue of [[§12★ Proof of Convergence#^thm-12-4|Theorem §12.4]]: Powers' Exercise 1.9.8 rewrites $\int_0^{L}(A\cos\lambda x + B\sin\lambda x)\,d\lambda$ as Fourier's single integral $\frac1\pi\int_{-\infty}^{\infty} f(t)\frac{\sin(L(t - x))}{t - x}\,dt$, whose kernel plays the role of the Dirichlet kernel.*

> [!remark]- Connections
> - The coefficient integrals (9) converge absolutely, since $|f(x)\cos\lambda x| \le |f(x)|$ ([[§36 Improper Integrals#^thm-36-2|451 Thm. §36.2]]), and $|A(\lambda)|, |B(\lambda)| \le \frac1\pi\int|f|$. In complex form this is the boundedness of the Fourier transform from $L^1$ to $L^\infty$, [[§26 Boundedness and Continuity#^ex-26-2|556 Ex. §26.2]], where dominated convergence ([[§15 The General Lebesgue Integral#^thm-15-8|551 Thm. §15.8]]) also shows that $A$ and $B$ are continuous.
> - The two analytic facts a proof needs: $A(\lambda), B(\lambda) \to 0$ as $\lambda \to \infty$ (the Riemann–Lebesgue lemma for absolutely integrable $f$, via the density of step functions, [[§16 The L¹ Space and Density Theorems#^thm-16-6|551 Thm. §16.6]]; the series version is [[§12★ Proof of Convergence#^lem-12-3|Lemma §12.3]]), and the exchange of the $x$- and $\lambda$-integrations in Exercise 1.9.8, which is Fubini's theorem on $\mathbb{R} \times [0, L]$, [[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|551 Thm. §17.6]].
> - Used in Complex Variables: inverting the Laplace transform by the Bromwich integral is this theorem in disguise (its complex form, [[§15★ Complex Methods#^thm-15-2|Theorem §15.2]], applied to $e^{-\gamma t}f(t)$ extended by zero to $t < 0$), [[§95★ Inverse Laplace Transforms#^thm-95-4|342 Thm. §95.4]], whose proof is complete relative to it.

> [!remark] Remark: Reading the Theorem
> - The right side of (8) is the same as in the Fourier series convergence theorem. Since $f$ is sectionally smooth, it equals $f(x)$ except at the jumps, finitely many in each finite interval; so one often writes (7) instead of (8).
> - The outer integral is improper: $\int_0^{\infty} = \lim_{L\to\infty}\int_0^{L}$ ([[§36 Improper Integrals#^def-36-1|451 Def. §36.1]]). It may converge only conditionally, as in Example §14.2, where $A(\lambda)$ decays like $1/\lambda$.
> - $A(\lambda)$ is even and $B(\lambda)$ is odd in $\lambda$. If $f$ is even, $B = 0$ (the integrand $f(x)\sin\lambda x$ is odd); if $f$ is odd, $A = 0$.
> - In practice the theorem is what allows equating a suitable function with its Fourier integral; the integral in (8) usually cannot be evaluated in closed form. Powers' rule of thumb: if $A$ and $B$ have closed forms, the integral (8) usually cannot be carried out by elementary means, and vice versa.

^rem-14-2

> [!remark] Remark: Method — Fourier Integral Representation of f
> In the lecture's shorthand: $f \xrightarrow{\ \frac1\pi\int_{-\infty}^{\infty}\cdots\,dx\ } A(\lambda), B(\lambda) \xrightarrow{\ \int_0^{\infty}\cdots\,d\lambda\ } f$.
> 1. Check the hypotheses: $f$ sectionally smooth on every finite interval and $\int_{-\infty}^{\infty}|f|\,dx < \infty$.
> 2. Compute $A(\lambda)$ and $B(\lambda)$ by (9). Use symmetry first: $B = 0$ for even $f$, $A = 0$ for odd $f$; integrate only over the set where $f \ne 0$. Integrals like $\int_0^\infty e^{-x}\cos\lambda x\,dx$ go by integrating by parts twice.
> 3. Write $f(x) = \int_0^{\infty}\big(A(\lambda)\cos\lambda x + B(\lambda)\sin\lambda x\big)d\lambda$, and note that at a jump the integral gives the average $\frac12(f(x+) + f(x-))$.
> 4. For $f$ given only on $0 < x < \infty$, choose the cosine or sine integral (Definition §14.2); in heat problems the boundary condition at $x = 0$ decides ($u(0, t) = 0$: sine; $u_x(0, t) = 0$: cosine).

^rem-14-3

> [!example] Example §14.1: A One-Sided Exponential
> Let $f(x) = e^{-x}$ for $0 < x$ and $f(x) = 0$ for $x < 0$.
>
> **(a) The series on $-a < x < a$.** For any $a > 0$, integrating $e^{-x}\cos\big(\frac{n\pi x}{a}\big)$ and $e^{-x}\sin\big(\frac{n\pi x}{a}\big)$ over $0 < x < a$ gives
>
> $$
> a_0 = \frac{1 - e^{-a}}{2a}, \qquad a_n = \frac{1 - e^{-a}\cos(n\pi)}{a\big(1 + (n\pi/a)^2\big)}, \qquad b_n = \frac{\big(1 - e^{-a}\cos(n\pi)\big)n\pi}{a^2\big(1 + (n\pi/a)^2\big)} . \qquad (2)
> $$
>
> The series converges to $\frac12$ at $x = 0$ and to $\frac12 e^{-a}$ at $x = a$. In the notation of (3), $A_a(\lambda_n) = \frac a\pi a_n = \frac{1 - e^{-a}\cos n\pi}{\pi(1 + \lambda_n^2)}$, which tends to $\frac{1}{\pi(1 + \lambda^2)}$ as $a \to \infty$, just as the Riemann-sum picture suggests; and $a_0 \to 0$.
>
> **(b) The coefficient functions.** Let $I = \int_0^{\infty} e^{-x}\cos\lambda x\,dx$ and $J = \int_0^{\infty} e^{-x}\sin\lambda x\,dx$. Integrating by parts (the boundary terms at $\infty$ vanish because of $e^{-x}$),
>
> $$
> I = \big[-e^{-x}\cos\lambda x\big]_0^{\infty} - \lambda\int_0^{\infty} e^{-x}\sin\lambda x\,dx = 1 - \lambda J, \qquad J = \big[-e^{-x}\sin\lambda x\big]_0^{\infty} + \lambda\int_0^{\infty} e^{-x}\cos\lambda x\,dx = \lambda I .
> $$
>
> So $I = 1 - \lambda^2 I$, that is $I = \frac{1}{1 + \lambda^2}$ and $J = \frac{\lambda}{1 + \lambda^2}$, and
>
> $$
> A(\lambda) = \frac1\pi\int_0^{\infty} e^{-x}\cos(\lambda x)\,dx = \frac{1}{\pi(1 + \lambda^2)}, \qquad B(\lambda) = \frac1\pi\int_0^{\infty} e^{-x}\sin(\lambda x)\,dx = \frac{\lambda}{\pi(1 + \lambda^2)} .
> $$
>
> **(c) The representation.** $f$ is sectionally smooth with a jump at $0$, and $\int|f| = 1$. By Theorem §14.1,
>
> $$
> \int_0^{\infty}\Big[\frac{1}{\pi(1 + \lambda^2)}\cos(\lambda x) + \frac{\lambda}{\pi(1 + \lambda^2)}\sin(\lambda x)\Big]d\lambda = \begin{cases} e^{-x}, & 0 < x, \\ \frac12, & x = 0, \\ 0, & x < 0 . \end{cases}
> $$
>
> At $x = 0$ this can be checked directly: $\int_0^{\infty}\frac{d\lambda}{\pi(1 + \lambda^2)} = \frac1\pi\cdot\frac\pi2 = \frac12$.
>
> On Midterm 2 these coefficients gave the temperature in an infinite rod ($u_t = u_{xx}$, $u(x, 0) = f(x)$): each mode $\cos\lambda x$, $\sin\lambda x$ decays like $e^{-\lambda^2 t}$, so $u(x, t) = \int_0^{\infty} e^{-\lambda^2 t}\Big(\frac{\cos\lambda x}{\pi(1 + \lambda^2)} + \frac{\lambda\sin\lambda x}{\pi(1 + \lambda^2)}\Big)d\lambda$ ([[§27 Infinite Rod#^thm-27-2|Theorem §27.2]]); the whole midterm problem is [[§27 Infinite Rod#^ex-27-2|Example §27.2]], and its closed form [[§28★ The Error Function#^ex-28-3|Example §28.3]].
>
> *Powers: 1.9, Example 1 · Source: 341 Midterm 2, Q2(c)*

^ex-14-1

> [!example] Example §14.2: A Rectangular Pulse
> The function $f(x) = 1$ for $|x| < 1$, $f(x) = 0$ for $|x| > 1$ is even, so $B(\lambda) = 0$, and
>
> $$
> A(\lambda) = \frac1\pi\int_{-\infty}^{\infty} f(x)\cos(\lambda x)\,dx = \frac1\pi\int_{-1}^{1}\cos(\lambda x)\,dx = \frac{2\sin\lambda}{\pi\lambda} .
> $$
>
> Since $f$ is sectionally smooth with $\int|f| = 2$, the representation is legitimate:
>
> $$
> f(x) = \int_0^{\infty}\frac{2\sin\lambda}{\pi\lambda}\cos(\lambda x)\,d\lambda .
> $$
>
> Actually the integral equals $\frac12$ at $x = \pm1$, so the equality is not strictly correct at these two points. At $x = 0$ it reads $\frac2\pi\int_0^{\infty}\frac{\sin\lambda}{\lambda}\,d\lambda = 1$, which is the Dirichlet integral $\int_0^{\infty}\frac{\sin t}{t}\,dt = \frac\pi2$ (Powers' Exercise 1.9.6). Here $A(\lambda)$ decays only like $1/\lambda$, and the integral converges conditionally. With $\sin\lambda\cos\lambda x = \frac12\big(\sin\lambda(1 + x) + \sin\lambda(1 - x)\big)$, the integral up to $\lambda = L$ is
>
> $$
> \int_0^{L}\frac{2\sin\lambda}{\pi\lambda}\cos(\lambda x)\,d\lambda = \frac1\pi\Big(\operatorname{Si}\big(L(1 + x)\big) + \operatorname{Si}\big(L(1 - x)\big)\Big), \qquad \operatorname{Si}(z) = \int_0^{z}\frac{\sin t}{t}\,dt ,
> $$
>
> shown in the figure.
>
> *Powers: 1.9, Example 2*

^ex-14-2

![[m341-14-1.svg]]
*Example §14.2: the pulse $f$ (dashed) and its truncated Fourier integrals $\int_0^{L}\frac{2\sin\lambda}{\pi\lambda}\cos\lambda x\,d\lambda$ for $L = 4$ and $L = 16$. As $L$ grows they approach $f$ at every point except the jumps, where every truncation passes through the average $\frac12$ (red). Near the jumps they overshoot by about $9\%$ of the jump however large $L$ is (the maximum tends to $\frac12 + \frac1\pi\operatorname{Si}(\pi) \approx 1.09$), the Fourier-integral form of the Gibbs phenomenon.*

> [!remark]- Connections
> - See also: [[§89★ An Indented Path#^ex-89-1|342 Ex. §89.1]] (Dirichlet's integral $\int_0^\infty \frac{\sin x}{x}\,dx = \frac\pi2$, the value at $x = 0$, by an indented contour).

> [!example] Example §14.3: A Triangular Pulse
> Find the Fourier integral representation of $f(x) = 1 - |x|$ for $|x| < 1$, $f(x) = 0$ for $|x| > 1$.
>
> $f$ is even, so $B(\lambda) = \frac1\pi\int f(x)\sin(\lambda x)\,dx = 0$. Integrating by parts,
>
> $$
> A(\lambda) = \frac1\pi\int_{-1}^{1}(1 - |x|)\cos(\lambda x)\,dx = \frac2\pi\int_0^{1}(1 - x)\cos(\lambda x)\,dx = \frac2\pi\Big(\Big[(1 - x)\frac{\sin\lambda x}{\lambda}\Big]_0^1 + \int_0^1\frac{\sin\lambda x}{\lambda}\,dx\Big) = \frac{2(1 - \cos\lambda)}{\pi\lambda^2} .
> $$
>
> $f$ is continuous and sectionally smooth with $\int|f| = 1$, so for every $x$
>
> $$
> f(x) = \int_0^{\infty}\frac{2(1 - \cos\lambda)}{\pi\lambda^2}\cos(\lambda x)\,d\lambda .
> $$
>
> Compared with the pulse of Example §14.2, $A(\lambda) = \frac{4\sin^2(\lambda/2)}{\pi\lambda^2}$ decays like $1/\lambda^2$: removing the jumps makes the integral converge absolutely, as removing jumps speeds up Fourier series ([[§9 Uniform Convergence#^thm-9-3|Theorem §9.3]]). At $x = 0$: $\frac2\pi\int_0^{\infty}\frac{1 - \cos\lambda}{\lambda^2}\,d\lambda = \frac2\pi\cdot\frac\pi2 = 1 = f(0)$.
>
> *Source: 341 HW 9, Problem 1*

^ex-14-3

> [!remark]- Connections
> - See also: [[§89★ An Indented Path#^ex-89-2|342 Ex. §89.2]] (the integral $\int_0^\infty \frac{1 - \cos\lambda}{\lambda^2}\,d\lambda = \frac\pi2$ used at $x = 0$, by an indented contour).

## Cosine and Sine Integrals

If $f(x)$ is defined only for $0 < x < \infty$, one can construct an even or odd extension, whose Fourier integral contains only $\cos(\lambda x)$ or only $\sin(\lambda x)$.

> [!definition] Definition §14.2: Fourier Cosine Integral Representation
> Let $f(x)$ be defined and sectionally smooth for $0 < x < \infty$, and let $\int_0^{\infty}|f(x)|\,dx < \infty$. Then we write the **Fourier cosine integral representation**
>
> $$
> f(x) = \int_0^{\infty} A(\lambda)\cos(\lambda x)\,d\lambda, \quad 0 < x < \infty, \qquad\text{with}\quad A(\lambda) = \frac2\pi\int_0^{\infty} f(x)\cos(\lambda x)\,dx .
> $$
>
> *Powers: 1.9 (boxed summary)*

^def-14-2

> [!definition] Definition §14.2: Fourier Sine Integral Representation
> Let $f(x)$ be defined and sectionally smooth for $0 < x < \infty$, and let $\int_0^{\infty}|f(x)|\,dx < \infty$. Then we write the **Fourier sine integral representation**
>
> $$
> f(x) = \int_0^{\infty} B(\lambda)\sin(\lambda x)\,d\lambda, \quad 0 < x < \infty, \qquad\text{with}\quad B(\lambda) = \frac2\pi\int_0^{\infty} f(x)\sin(\lambda x)\,dx .
> $$
>
> *Powers: 1.9 (boxed summary)*

^def-14-new2

> [!theorem] Corollary §14.2: Cosine and Sine Integrals Converge
> Under the hypotheses of Definition §14.2, at every $x > 0$ both the cosine and the sine integral of $f$ equal $\frac12\big(f(x+) + f(x-)\big)$. At $x = 0$ the cosine integral equals $f(0+)$ and the sine integral equals $0$.
>
> *Powers: 1.9 (text)*

^cor-14-2

> [!proof]+ Proof
> (Powers derives the representations from the even and odd extensions; here are the details.) Sectional smoothness on $0 < x < \infty$ includes that $f(0+)$ exists.
>
> **Cosine.** Let $f_e(x) = f(|x|)$ for $x \ne 0$. It is sectionally smooth on every finite interval and $\int_{-\infty}^{\infty}|f_e| = 2\int_0^{\infty}|f| < \infty$. Since $f_e$ is even, its coefficient $B_e(\lambda) = 0$, and $f_e(x)\cos\lambda x$ is even, so
>
> $$
> A_e(\lambda) = \frac1\pi\int_{-\infty}^{\infty} f_e(x)\cos(\lambda x)\,dx = \frac2\pi\int_0^{\infty} f(x)\cos(\lambda x)\,dx = A(\lambda) .
> $$
>
> [[§14 Fourier Integral#^thm-14-1|Theorem §14.1]] applied to $f_e$ gives $\int_0^{\infty} A(\lambda)\cos(\lambda x)\,d\lambda = \frac12\big(f_e(x+) + f_e(x-)\big)$. For $x > 0$ this is $\frac12\big(f(x+) + f(x-)\big)$; at $x = 0$ it is $\frac12\big(f(0+) + f(0+)\big) = f(0+)$.
>
> **Sine.** Let $f_o(x) = f(x)$ for $x > 0$ and $f_o(x) = -f(-x)$ for $x < 0$. As before $f_o$ satisfies the hypotheses of Theorem §14.1; now $A_o = 0$ and, $f_o(x)\sin\lambda x$ being even, $B_o(\lambda) = \frac2\pi\int_0^{\infty} f(x)\sin(\lambda x)\,dx = B(\lambda)$. Theorem §14.1 gives the claim for $x > 0$, and at $x = 0$ the value $\frac12\big(f(0+) - f(0+)\big) = 0$.

^pf-14-2

*Uses:* [[§14 Fourier Integral#^thm-14-1|§14.1]], [[§14 Fourier Integral#^def-14-1|Def. §14.1]], [[§14 Fourier Integral#^def-14-new1|Def. §14.1]], [[§14 Fourier Integral#^def-14-2|Def. §14.2]], [[§14 Fourier Integral#^def-14-new2|Def. §14.2]]

> [!example] Example §14.4: The Two-Sided Exponential and Its Derivative
> **(a)** Find the Fourier integral representation of $f(x) = e^{-|x|}$. The function is even, so $B(\lambda) = 0$, and by Example §14.1(b)
>
> $$
> A(\lambda) = \frac1\pi\int_{-\infty}^{\infty} e^{-|x|}\cos(\lambda x)\,dx = \frac2\pi\int_0^{\infty} e^{-x}\cos(\lambda x)\,dx = \frac2\pi\cdot\frac{1}{1 + \lambda^2} . \qquad (10)\text{–}(12)
> $$
>
> Since $e^{-|x|}$ is continuous and sectionally smooth,
>
> $$
> e^{-|x|} = \frac2\pi\int_0^{\infty}\frac{\cos(\lambda x)}{1 + \lambda^2}\,d\lambda, \qquad -\infty < x < \infty .
> $$
>
> This is also the Fourier cosine integral of $e^{-x}$, $x > 0$ (Definition §14.2).
>
> **(b)** The odd companion $f_-(x) = e^{-x}$ ($x > 0$), $-e^{x}$ ($x < 0$), which is the sine-integral extension of $e^{-x}$, has $A(\lambda) = 0$ and
>
> $$
> B(\lambda) = \frac2\pi\int_0^{\infty} e^{-x}\sin(\lambda x)\,dx = \frac2\pi\cdot\frac{\lambda}{1 + \lambda^2}, \qquad f_-(x) = \frac2\pi\int_0^{\infty}\frac{\lambda\sin(\lambda x)}{1 + \lambda^2}\,d\lambda \quad (x \ne 0) ,
> $$
>
> with value $0$ at the jump $x = 0$.
>
> **(c)** The derivative of $e^{-|x|}$ is $f'(x) = -e^{-x}$ ($0 < x$), $e^{x}$ ($x < 0$), that is, $f' = -f_-$. Since $f$ is continuous and both $f$ and $f'$ have Fourier integral representations, Theorem §14.3 below differentiates (a) under the integral sign:
>
> $$
> f'(x) = \int_0^{\infty}\frac2\pi\cdot\frac{-\lambda}{1 + \lambda^2}\sin(\lambda x)\,d\lambda ,
> $$
>
> in agreement with (b).
>
> *The lecture's value of $B(\lambda)$ for $f_-$ in (b) carries a sign error ($-\frac2\pi\frac{\lambda}{1 + \lambda^2}$); the integration by parts in Example §14.1(b) gives $+\frac{\lambda}{1 + \lambda^2}$, consistent with (c).*
>
> *Powers: 1.9, Examples 3 and 5 · Source: 341 lecture 10.22, Example 1*

^ex-14-4

> [!remark]- Connections
> - See also: [[§87 Improper Integrals from Fourier Analysis#^ex-87-2|342 Ex. §87.2]] (the integral in (a) evaluated by residues for every $x$, without the Fourier integral theorem); sine integrals like (b), whose integrands decay only like $1/\lambda$, need Jordan's lemma, [[§88★ Jordan's Lemma#^thm-88-2|342 Thm. §88.2]].

> [!example] Example §14.5: A Half Sine Wave, Three Ways
> Let $f(x) = \sin(x)$ for $0 < x < \pi$ and $f(x) = 0$ for $\pi < x$.
>
> **Sine integral.** Since $f = 0$ for $x > \pi$, with $\sin x\sin\lambda x = \frac12\big(\cos(\lambda - 1)x - \cos(\lambda + 1)x\big)$,
>
> $$
> B(\lambda) = \frac2\pi\int_0^{\pi}\sin(x)\sin(\lambda x)\,dx = \frac2\pi\Big[\frac{\sin((\lambda - 1)x)}{2(\lambda - 1)} - \frac{\sin((\lambda + 1)x)}{2(\lambda + 1)}\Big]_0^{\pi} = \frac2\pi\Big[\frac{\sin((\lambda - 1)\pi)}{2(\lambda - 1)} - \frac{\sin((\lambda + 1)\pi)}{2(\lambda + 1)}\Big] .
> $$
>
> With $\sin\big((\lambda \pm 1)\pi\big) = \sin(\lambda\pi \pm \pi) = -\sin(\lambda\pi)$ and a common denominator,
>
> $$
> B(\lambda) = \frac{-2\sin(\lambda\pi)}{\pi(\lambda^2 - 1)}, \qquad f(x) = \int_0^{\infty}\frac{-2\sin(\lambda\pi)}{\pi(\lambda^2 - 1)}\sin(\lambda x)\,d\lambda, \quad 0 < x .
> $$
>
> Since $f$ is continuous for $0 < x$, the equality holds at every point.
>
> **Cosine integral.** Similarly, with $\sin x\cos\lambda x = \frac12\big(\sin(1 + \lambda)x + \sin(1 - \lambda)x\big)$ and $\cos\big((1 \pm \lambda)\pi\big) = -\cos\lambda\pi$,
>
> $$
> A(\lambda) = \frac2\pi\int_0^{\pi}\sin(x)\cos(\lambda x)\,dx = \frac{-2\big(1 + \cos(\lambda\pi)\big)}{\pi(\lambda^2 - 1)}, \qquad f(x) = \int_0^{\infty}\frac{-2\big(1 + \cos(\lambda\pi)\big)}{\pi(\lambda^2 - 1)}\cos(\lambda x)\,d\lambda, \quad 0 < x .
> $$
>
> Both $A$ and $B$ have removable discontinuities at $\lambda = 1$; the values there, $A(1) = 0$ and $B(1) = \frac2\pi\int_0^{\pi}\sin^2 x\,dx = 1$, come from integrating directly (or by l'Hôpital's rule).
>
> **Whole line.** Regard $f$ as a function on $-\infty < x < \infty$, zero for $x < 0$. Then
>
> $$
> A_f(\lambda) = \frac1\pi\int_0^{\pi}\sin x\cos\lambda x\,dx = \frac{1 + \cos(\lambda\pi)}{\pi(1 - \lambda^2)}, \qquad B_f(\lambda) = \frac1\pi\int_0^{\pi}\sin x\sin\lambda x\,dx = \frac{\sin(\lambda\pi)}{\pi(1 - \lambda^2)} ,
> $$
>
> exactly half of the cosine and sine coefficients above. This is no accident: on the whole line $f = \frac12(f_e + f_o)$, the average of its even and odd extensions, so its Fourier integral is the average of the cosine and sine integrals. At $x = 0$ both halves give $0$, and for $x < 0$ they cancel, since there $f_o = -f_e$.
>
> On the Midterm 2 practice sheet these coefficients solved the heat equation $u_t = 2u_{xx}$ with initial temperature $f$: on $x > 0$ with $u(0, t) = 0$ by the sine integral (Problem 7, [[§26 Semi-Infinite Rod#^ex-26-2|Example §26.2]]), and on the whole line by $A_f$, $B_f$ (Problem 8, [[§27 Infinite Rod#^ex-27-3|Example §27.3]](b)); the keys' coefficients agree with the ones above.
>
> *Powers: 1.9, Example 4 · Source: 341 Practice Midterm 2, Problems 7(c) and 8(c)*

^ex-14-5

## Operations on Fourier Integrals

Rules for operations on Fourier integrals generally follow those for Fourier series in [[§10 Operations on Fourier Series|§10]]. In particular:

> [!theorem] Theorem §14.3: Differentiating a Fourier Integral
> If $f(x)$ is continuous and both $f(x)$ and $f'(x)$ have Fourier integral representations, and
>
> $$
> f(x) = \int_0^{\infty}\big[A(\lambda)\cos(\lambda x) + B(\lambda)\sin(\lambda x)\big]\,d\lambda ,
> $$
>
> then
>
> $$
> f'(x) = \int_0^{\infty}\big[-\lambda A(\lambda)\sin(\lambda x) + \lambda B(\lambda)\cos(\lambda x)\big]\,d\lambda .
> $$
>
> *Powers: 1.9 (text)*

^thm-14-3

*Powers omits the proof. The key computation, integration by parts in the coefficient integrals (the coefficients of $f'$ are $\lambda B(\lambda)$ and $-\lambda A(\lambda)$), is carried out in complex form in [[§15★ Complex Methods#^ex-15-4|Example §15.4]](a).*

Example §14.4(c) applies the theorem to $e^{-|x|}$.
