---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 6
section: 51
powers: "6.1"
aliases: ["Powers 6.1"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§50★ Some Applications of Legendre Polynomials]] · ↑ [[· 6★ Laplace Transform]] · [[§52★ Partial Fractions and Convolutions]] →

*Powers, Section 6.1.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

The Laplace transform $F(s) = \int_0^\infty e^{-st}f(t)\,dt$ trades a function of time for a function of a new variable $s$. Its point is the derivative rule $\mathcal{L}(f') = sF(s) - f(0)$: differentiation in $t$ becomes multiplication by $s$, and the initial value comes along automatically. This section collects Powers' list of properties and his table of transforms. Most of it is developed and proved in [[Ordinary Differential Equations]], [[§21 Definition of the Laplace Transform|§21]]–[[§26★ The Convolution Integral|§26★]] (Boyce–DiPrima, Ch. 6), and each item below links there. What is new here is that $s$ is allowed to be complex, and that the integral rule and the rule for $f(t)/t$ are added. Complex $s$ is what [[§53★ Partial Differential Equations|§53★]] and [[§54★ More Difficult Examples|§54★]] need: there the transform is applied in $t$ to the heat and wave equations, and inverting it means locating complex singularities of $U(x, s)$.

## Definition and Existence

> [!definition] Definition §51.1: The Laplace Transform
> Let $f(t)$ be sectionally continuous in every interval $0 \le t < T$. The **Laplace transform** of $f$, written $\mathcal{L}(f)$ or $F(s)$, is
>
> $$
> \mathcal{L}(f) = F(s) = \int_0^\infty e^{-st}f(t)\,dt . \qquad (1)
> $$
>
> A function of $t$ is denoted by a lowercase letter and its transform by the corresponding capital. The variable $s$ may be real or complex; in computing transforms from the definition it is usually taken real.
>
> *Powers: 6.1, Equation (1)*

^def-51-1

*This is [[§21 Definition of the Laplace Transform#^def-21-4|331 Def. §21.4]] ("sectionally continuous" is piecewise continuous, [[§21 Definition of the Laplace Transform#^def-21-2|331 Def. §21.2]]); there $s$ is real.*

> [!remark]- Connections
> - The Laplace and Fourier transforms are one transform: with $s = \sigma + i\omega$, $F(\sigma + i\omega) = \int_{-\infty}^{\infty} e^{-i\omega t}\big[e^{-\sigma t}f(t)H(t)\big]\,dt$ is $2\pi$ times the complex Fourier coefficient function $C(\omega)$ of $e^{-\sigma t}f(t)$, cut off to $t \ge 0$ ([[§15★ Complex Methods#^def-15-2|Def. §15.2]]; real form [[§14 Fourier Integral#^def-14-1|Def. §14.1]]). The factor $e^{-\sigma t}$ is what makes the integral converge for functions such as $e^{t}$ that have no Fourier transform.

> [!definition] Definition §51.2: Exponential Order
> A function $f(t)$, sectionally continuous on every finite interval $0 \le t < T$, is **of exponential order** if for some constant $k$
>
> $$
> \lim_{t\to\infty} e^{-kt}f(t) = 0 .
> $$
>
> For instance $e^{at}$, $t^n$ and every bounded function are of exponential order, while $\exp(t^2)$ is not: $e^{-kt}e^{t^2} = e^{t(t - k)} \to \infty$ for every $k$.
>
> *Powers: 6.1 (text)*

^def-51-2

*Boyce–DiPrima's version is $|f(t)| \le Ke^{at}$ for $t \ge M$, [[§21 Definition of the Laplace Transform#^def-21-5|331 Def. §21.5]]. Powers' condition implies it with $a = k$ (eventually $|e^{-kt}f(t)| \le 1$), and it implies Powers' condition for every $k > a$.*

> [!theorem] Theorem §51.1: Existence of the Laplace Transform
> Let $f(t)$ be sectionally continuous in every finite interval $0 \le t < T$. If for some constant $k$
>
> $$
> \lim_{t\to\infty} e^{-kt}f(t) = 0 ,
> $$
>
> then the Laplace transform of $f$ exists for $\operatorname{Re}(s) > k$.
>
> *Powers: 6.1, Theorem*

^thm-51-1

*Powers omits the proof. For real $s$ it is [[§21 Definition of the Laplace Transform#^thm-21-2|331 Thm. §21.2]], by comparison with $e^{-(s - k)t}$. The same comparison works for complex $s$, because $|e^{-st}| = e^{-t\operatorname{Re}(s)}$.*

> [!theorem] Theorem §51.2: Linearity
> For constants $c$ and functions $f$, $g$ whose transforms exist,
>
> $$
> \mathcal{L}\big(cf(t)\big) = c\,\mathcal{L}\big(f(t)\big), \qquad (2)
> $$
>
> $$
> \mathcal{L}\big(f(t) + g(t)\big) = \mathcal{L}\big(f(t)\big) + \mathcal{L}\big(g(t)\big) . \qquad (3)
> $$
>
> The constants and functions may be complex.
>
> *Powers: 6.1, Equations (2) and (3)*

^thm-51-2

*The transform inherits these from the integral: [[§21 Definition of the Laplace Transform#^thm-21-3|331 Thm. §21.3]]. For complex-valued $f = f_1 + if_2$ the integral is taken on real and imaginary parts separately, so the same rules hold with complex $c$.*

> [!example] Example §51.1: Transforms from the Exponential
> **The basic pair.** For real $s$,
>
> $$
> \mathcal{L}(1) = \int_0^\infty e^{-st}\cdot 1\,dt = \frac1s, \qquad
> \mathcal{L}\big(e^{at}\big) = \int_0^\infty e^{-st}e^{at}\,dt = -\frac{e^{-(s - a)t}}{s - a}\bigg|_0^\infty = \frac{1}{s - a} ,
> $$
>
> for $s > 0$ and $s > a$ respectively. The second formula holds for complex $a$ and $s$ with $\operatorname{Re}(s) > \operatorname{Re}(a)$, since then $|e^{-(s - a)t}| = e^{-\operatorname{Re}(s - a)t} \to 0$.
>
> **Hyperbolic and trigonometric functions.** By linearity (Theorem §51.2), with complex constants for the sine,
>
> $$
> \mathcal{L}\big(\cosh(at)\big) = \mathcal{L}\Big[\tfrac12\big(e^{at} + e^{-at}\big)\Big] = \frac12\Big(\frac{1}{s - a} + \frac{1}{s + a}\Big) = \frac{s}{s^2 - a^2} ,
> $$
>
> $$
> \mathcal{L}\big(\sin(\omega t)\big) = \mathcal{L}\Big[\tfrac{1}{2i}\big(e^{i\omega t} - e^{-i\omega t}\big)\Big] = \frac{1}{2i}\Big(\frac{1}{s - i\omega} - \frac{1}{s + i\omega}\Big) = \frac{1}{2i}\cdot\frac{2i\omega}{s^2 + \omega^2} = \frac{\omega}{s^2 + \omega^2} .
> $$
>
> The same computations give $\mathcal{L}(\sinh(at)) = a/(s^2 - a^2)$ and $\mathcal{L}(\cos(\omega t)) = s/(s^2 + \omega^2)$.
>
> *Powers: 6.1 (text)*

^ex-51-1

## The Shifting Theorem

> [!theorem] Theorem §51.3: Shifting Theorem
> If $F(s) = \mathcal{L}(f(t))$, then for any constant $b$ (real or complex)
>
> $$
> \mathcal{L}\big(e^{bt}f(t)\big) = \int_0^\infty e^{-st}e^{bt}f(t)\,dt = \int_0^\infty e^{-(s - b)t}f(t)\,dt = F(s - b) .
> $$
>
> *Powers: 6.1 (text)*

^thm-51-3

*The displayed one-line computation is the proof; it is [[§23 Step Functions#^thm-23-3|331 Thm. §23.3]]. It holds wherever $F(s - b)$ exists, so for $\operatorname{Re}(s) > k + \operatorname{Re}(b)$ when $f$ satisfies Theorem §51.1 with constant $k$.*

> [!example] Example §51.2: A Damped Sine
> Since $\mathcal{L}(\sin(\omega t)) = \omega/(s^2 + \omega^2)$ (Example §51.1), the shifting theorem gives
>
> $$
> \mathcal{L}\big(e^{bt}\sin(\omega t)\big) = \frac{\omega}{(s - b)^2 + \omega^2} = \frac{\omega}{s^2 - 2sb + b^2 + \omega^2} .
> $$
>
> In the same way $\mathcal{L}(e^{bt}\cos(\omega t)) = (s - b)/(s^2 - 2bs + b^2 + \omega^2)$ and $\mathcal{L}(e^{bt}t^k) = k!/(s - b)^{k+1}$ (from Example §51.3).
>
> *Powers: 6.1 (text)*

^ex-51-2

## Derivatives and Integrals

> [!theorem] Theorem §51.4: Transform of Derivatives
> If $f(t)$ is continuous and of exponential order, and $f'(t)$ is sectionally continuous, then
>
> $$
> \mathcal{L}\big(f'(t)\big) = -f(0) + s\,\mathcal{L}\big(f(t)\big) .
> $$
>
> (If $f$ has a jump at $t = 0$, $f(0)$ means $f(0+)$.) If $f$ and $f'$ are continuous, $f''$ is sectionally continuous, and all three are of exponential order, then
>
> $$
> \mathcal{L}\big(f''(t)\big) = -f'(0) + s\,\mathcal{L}\big(f'(t)\big) = -f'(0) - sf(0) + s^2\mathcal{L}\big(f(t)\big) .
> $$
>
> In general, if $f$ and its first $n - 1$ derivatives are continuous, $f^{(n)}$ is sectionally continuous, and all are of exponential order,
>
> $$
> \mathcal{L}\big[f^{(n)}(t)\big] = -f^{(n-1)}(0) - sf^{(n-2)}(0) - \cdots - s^{n-1}f(0) + s^n\mathcal{L}\big(f(t)\big) . \qquad (4)
> $$
>
> *Powers: 6.1, Equation (4)*

^thm-51-4

*Powers' proof integrates by parts, $\mathcal{L}(f') = e^{-st}f(t)\big|_0^\infty + s\int_0^\infty e^{-st}f(t)\,dt$, and the boundary term at $\infty$ vanishes for $\operatorname{Re}(s)$ large. This is the proof of [[§22 Solution of Initial Value Problems#^thm-22-1|331 Thm. §22.1]]; formula (4) follows by induction, [[§22 Solution of Initial Value Problems#^cor-22-2|331 Cor. §22.2]].*

> [!example] Example §51.3: Powers of t
> Apply (4) to $f(t) = t^k$, $k$ a nonnegative integer. Here
>
> $$
> f(0) = f'(0) = \cdots = f^{(k-1)}(0) = 0, \qquad f^{(k)}(0) = k!, \qquad f^{(k+1)}(t) = 0 .
> $$
>
> So (4) with $n = k + 1$ reads $\mathcal{L}(0) = -f^{(k)}(0) + s^{k+1}\mathcal{L}(t^k)$, that is, $0 = -k! + s^{k+1}\mathcal{L}(t^k)$, and
>
> $$
> \mathcal{L}\big(t^k\big) = \frac{k!}{s^{k+1}} .
> $$
>
> In particular $\mathcal{L}(t) = 1/s^2$.
>
> *Powers: 6.1 (text)*

^ex-51-3

> [!theorem] Theorem §51.5: Transform of an Integral
> If $f(t)$ is sectionally continuous and of exponential order, then
>
> $$
> \mathcal{L}\Big[\int_0^t f(t')\,dt'\Big] = \frac1s\,\mathcal{L}\big(f(t)\big) . \qquad (5)
> $$
>
> *Powers: 6.1, Equation (5)*

^thm-51-5

> [!proof]+ Proof
> Let $g(t) = \int_0^t f(t')\,dt'$. Since $f$ is sectionally continuous, $g$ is continuous, $g(0) = 0$, and $g'(t) = f(t)$ (at points of continuity of $f$; $g'$ is sectionally continuous). $g$ is of exponential order (Powers assumes this; here is why). By Definition §51.2 there is $k$ with $e^{-kt}f(t) \to 0$, and we may take $k > 0$. Then $|f(t)| \le Me^{kt}$ for all $t \ge 0$, since $f$ is bounded on each finite interval. Hence $|g(t)| \le \int_0^t Me^{kt'}\,dt' \le (M/k)e^{kt}$, and $e^{-k't}g(t) \to 0$ for every $k' > k$. So [[§51★ Definition and Elementary Properties#^thm-51-4|Theorem §51.4]] applies to $g$:
>
> $$
> \mathcal{L}\big(f(t)\big) = \mathcal{L}\big(g'(t)\big) = -g(0) + s\,\mathcal{L}\big(g(t)\big) = s\,\mathcal{L}\Big[\int_0^t f(t')\,dt'\Big] .
> $$
>
> Dividing by $s$ gives (5). (Equivalently, $\int_0^t f = f * 1$ and $\mathcal{L}(1) = 1/s$, by the convolution theorem, [[§26★ The Convolution Integral#^ex-26-1|331 Ex. §26.1]].)

^pf-51-5

*Uses:* [[§51★ Definition and Elementary Properties#^thm-51-4|§51.4]], [[§51★ Definition and Elementary Properties#^def-51-2|Def. §51.2]]

## Differentiation and Integration in s

> [!theorem] Theorem §51.6: Multiplication and Division by t
> If $F(s) = \mathcal{L}(f(t))$, then
>
> $$
> \mathcal{L}\big(tf(t)\big) = -\frac{dF(s)}{ds}, \qquad \mathcal{L}\Big(\frac1t f(t)\Big) = \int_s^\infty F(s')\,ds' . \qquad (6)
> $$
>
> The transform of $f(t)/t$ does not exist unless $f(0) = 0$.
>
> *Powers: 6.1, Equation (6)*

^thm-51-6

> [!proof]+ Proof
> Take $s$ real and larger than the constant $k$ of Theorem §51.1. Powers derives both formulas from
>
> $$
> -\frac{de^{-st}}{ds} = te^{-st}, \qquad \int_s^\infty e^{-s't}\,ds' = \frac1t e^{-st} \quad (t > 0) ,
> $$
>
> by differentiating or integrating under the integral sign in $s$.
>
> **Multiplication by $t$.** Then $-F'(s) = -\frac{d}{ds}\int_0^\infty e^{-st}f(t)\,dt = \int_0^\infty te^{-st}f(t)\,dt = \mathcal{L}(tf(t))$. Differentiating under the integral sign is justified in the proof of [[§22 Solution of Initial Value Problems#^thm-22-6|331 Thm. §22.6]], entry 19.
>
> **Division by $t$.** Suppose $f(t)/t$ has a transform, with $\int_0^\infty e^{-st}|f(t)|/t\,dt < \infty$ (near $t = 0$ this is where $f(0) = 0$ is needed: if $f(0+) \ne 0$, then $|f(t)|/t \ge c/t$ near $0$ and the integral diverges). Then
>
> $$
> \int_s^\infty F(s')\,ds' = \int_s^\infty\!\!\int_0^\infty e^{-s't}f(t)\,dt\,ds' = \int_0^\infty f(t)\int_s^\infty e^{-s't}\,ds'\,dt = \int_0^\infty e^{-st}\,\frac{f(t)}{t}\,dt = \mathcal{L}\Big(\frac1t f(t)\Big) .
> $$
>
> Powers exchanges the order of integration without comment. Here is why it is allowed: the absolute integrand has iterated integral $\int_0^\infty |f(t)|\int_s^\infty e^{-s't}\,ds'\,dt = \int_0^\infty e^{-st}|f(t)|/t\,dt < \infty$, so Fubini's theorem applies.

^pf-51-6

*Uses:* [[§51★ Definition and Elementary Properties#^thm-51-1|§51.1]], [[§22 Solution of Initial Value Problems#^thm-22-6|331 Thm. §22.6]] (entry 19), [[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|551 Thm. §17.6]] (Fubini)

> [!remark]- Connections
> - The exchange of integrals: Tonelli's theorem ([[§17 Invariance Properties and Fubini's Theorem#^thm-17-3|551 Thm. §17.3]]) shows that the absolute integrand is integrable on $[s, \infty) \times (0, \infty)$, and Fubini's theorem ([[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|551 Thm. §17.6]]) then gives equality of the iterated integrals. The Riemann-integral version for nonnegative functions is [[§15 Multivariable Integration#^thm-15-12|452 Thm. §15.12]].

> [!example] Example §51.4: Two Transforms from Differentiating and Integrating in s
> **$t\sin(\omega t)$.** By Theorem §51.6 and Example §51.1,
>
> $$
> \mathcal{L}\big(t\sin(\omega t)\big) = -\frac{d}{ds}\Big(\frac{\omega}{s^2 + \omega^2}\Big) = \frac{2s\omega}{(s^2 + \omega^2)^2} .
> $$
>
> In the same way, $\mathcal{L}(t\cos(\omega t)) = -\frac{d}{ds}\frac{s}{s^2 + \omega^2} = \frac{s^2 - \omega^2}{(s^2 + \omega^2)^2}$.
>
> **$\sin(t)/t$.** Here $f(t) = \sin t$ has $f(0) = 0$, and $|\sin t|/t \le 1$, so the transform exists for $s > 0$. By Theorem §51.6,
>
> $$
> \mathcal{L}\Big(\frac{\sin(t)}{t}\Big) = \int_s^\infty \frac{ds'}{s'^2 + 1} = \frac\pi2 - \tan^{-1}(s) = \tan^{-1}\Big(\frac1s\Big) .
> $$
>
> *Powers: 6.1 (text)*

^ex-51-4

## Tables

> [!theorem] Theorem §51.7: Properties of the Laplace Transform
> | property | | here | 331 home |
> |---|---|---|---|
> | $\mathcal{L}(f) = F(s) = \int_0^\infty e^{-st}f(t)\,dt$ | definition | [[§51★ Definition and Elementary Properties#^def-51-1\|Def. §51.1]] | [[§21 Definition of the Laplace Transform#^def-21-4\|Def. §21.4]] |
> | $\mathcal{L}(cf(t)) = c\mathcal{L}(f(t))$ | linearity | [[§51★ Definition and Elementary Properties#^thm-51-2\|§51.2]] | [[§21 Definition of the Laplace Transform#^thm-21-3\|Thm. §21.3]] |
> | $\mathcal{L}(f(t) + g(t)) = \mathcal{L}(f(t)) + \mathcal{L}(g(t))$ | linearity | [[§51★ Definition and Elementary Properties#^thm-51-2\|§51.2]] | [[§21 Definition of the Laplace Transform#^thm-21-3\|Thm. §21.3]] |
> | $\mathcal{L}(f'(t)) = -f(0) + sF(s)$ | derivative | [[§51★ Definition and Elementary Properties#^thm-51-4\|§51.4]] | [[§22 Solution of Initial Value Problems#^thm-22-1\|Thm. §22.1]] |
> | $\mathcal{L}(f''(t)) = -f'(0) - sf(0) + s^2F(s)$ | derivative | [[§51★ Definition and Elementary Properties#^thm-51-4\|§51.4]] | [[§22 Solution of Initial Value Problems#^cor-22-2\|Cor. §22.2]] |
> | $\mathcal{L}(f^{(n)}(t)) = -f^{(n-1)}(0) - \cdots - s^{n-1}f(0) + s^nF(s)$ | derivative | [[§51★ Definition and Elementary Properties#^thm-51-4\|§51.4]] | [[§22 Solution of Initial Value Problems#^cor-22-2\|Cor. §22.2]] |
> | $\mathcal{L}(e^{bt}f(t)) = F(s - b)$ | shifting | [[§51★ Definition and Elementary Properties#^thm-51-3\|§51.3]] | [[§23 Step Functions#^thm-23-3\|Thm. §23.3]] |
> | $\mathcal{L}\big(\int_0^t f(t')\,dt'\big) = \frac1s F(s)$ | integral | [[§51★ Definition and Elementary Properties#^thm-51-5\|§51.5]] | [[§26★ The Convolution Integral#^ex-26-1\|Ex. §26.1]] |
> | $\mathcal{L}\big(\frac1t f(t)\big) = \int_s^\infty F(s')\,ds'$ | division by $t$ | [[§51★ Definition and Elementary Properties#^thm-51-6\|§51.6]] | — |
> | $\mathcal{L}(tf(t)) = -\frac{dF}{ds}$ | multiplication by $t$ | [[§51★ Definition and Elementary Properties#^thm-51-6\|§51.6]] | [[§22 Solution of Initial Value Problems#^thm-22-6\|Thm. §22.6]] (19) |
>
> *Powers: 6.1, Table 1*

^thm-51-7

> [!theorem] Theorem §51.8: Table of Laplace Transforms
> | $f(t)$ | $F(s)$ | 331 [[§22 Solution of Initial Value Problems#^thm-22-6\|Thm. §22.6]] | | $f(t)$ | $F(s)$ | 331 [[§22 Solution of Initial Value Problems#^thm-22-6\|Thm. §22.6]] |
> |---|---|---|---|---|---|---|
> | $0$ | $0$ | — | | $t^k$ | $\dfrac{k!}{s^{k+1}}$ | 3 |
> | $1$ | $\dfrac1s$ | 1 | | $e^{bt}\cos(\omega t)$ | $\dfrac{s - b}{s^2 - 2bs + b^2 + \omega^2}$ | 10 |
> | $e^{at}$ | $\dfrac{1}{s - a}$ | 2 | | $e^{bt}\sin(\omega t)$ | $\dfrac{\omega}{s^2 - 2bs + b^2 + \omega^2}$ | 9 |
> | $\cosh(at)$ | $\dfrac{s}{s^2 - a^2}$ | 8 | | $e^{bt}t^k$ | $\dfrac{k!}{(s - b)^{k+1}}$ | 11 |
> | $\sinh(at)$ | $\dfrac{a}{s^2 - a^2}$ | 7 | | $e^{at} - 1$ | $\dfrac{a}{s(s - a)}$ | 1, 2 |
> | $\cos(\omega t)$ | $\dfrac{s}{s^2 + \omega^2}$ | 6 | | $t\cos(\omega t)$ | $\dfrac{s^2 - \omega^2}{(s^2 + \omega^2)^2}$ | 6, 19 |
> | $\sin(\omega t)$ | $\dfrac{\omega}{s^2 + \omega^2}$ | 5 | | $t\sin(\omega t)$ | $\dfrac{2s\omega}{(s^2 + \omega^2)^2}$ | 5, 19 |
> | $t$ | $\dfrac{1}{s^2}$ | 3 | | | | |
>
> *Powers: 6.1, Table 2*

^thm-51-8

*Every entry was computed above, in Examples §51.1–§51.4 (for $e^{at} - 1$: $\frac{1}{s - a} - \frac1s = \frac{a}{s(s - a)}$). The column gives the entry of Boyce–DiPrima's table where it is proved.*

> [!remark] Remark: Computing Inverse Transforms
> Solving a problem by Laplace transform ends with finding the function $f(t) = \mathcal{L}^{-1}(F(s))$ whose transform is a given $F(s)$; this is usually the hard part. The methods are:
> 1. **Tables** such as Theorem §51.8. This is the least work and the most popular.
> 2. **Partial fractions**, for rational $F$, and Heaviside's formula: [[§52★ Partial Fractions and Convolutions#^thm-52-2|Theorem §52.2]]. Its extension to transcendental $F$ is the main tool for partial differential equations: [[§53★ Partial Differential Equations#^rem-53-2|§53★]] (Remark: The Extended Heaviside Formula).
> 3. **Convolution**: $F(s)G(s)$ is the transform of $f * g$, [[§52★ Partial Fractions and Convolutions#^thm-52-3|Theorem §52.3]].
> 4. **Integration in the complex plane** (the inversion integral). Powers does not use it, and the vault has no complex analysis; §53★ outlines how it explains the extended Heaviside formula.
>
> That $\mathcal{L}^{-1}$ is well defined at all (two continuous functions with the same transform are equal) is [[§22 Solution of Initial Value Problems#^thm-22-4|331 Thm. §22.4]].

^rem-51-1
