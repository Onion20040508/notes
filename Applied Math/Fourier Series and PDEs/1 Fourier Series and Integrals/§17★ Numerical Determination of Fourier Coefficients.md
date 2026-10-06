---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 1
section: "17★"
powers: "1.8"
aliases: ["Powers 1.8"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§16★ Proof of Convergence]] · ↑ [[· 1 Fourier Series and Integrals]] · [[§18 Fourier Integral]] →

*Powers, Section 1.8.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

Many Fourier coefficient integrals cannot be done in closed form, and often a function is known only through its values at some points, as with measured data. Then the integrals must be approximated numerically, and for a periodic function the crudest rule, the trapezoidal rule, turns out to be the best: the approximate coefficients are plain weighted averages of the sampled values. They have a remarkable property: the trigonometric polynomial built from them passes exactly through the data points. This is the discrete Fourier analysis behind the spectral analysis of sampled periodic signals (tides, seasonal records, vibration measurements), computed in practice by the fast Fourier transform.

## Preparing the Function

The approximation works best when the coefficients being approximated decay quickly, that is, when the function is continuous and periodic ([[§13 Uniform Convergence#^thm-13-3|Theorem §13.3]], [[§14 Operations on Fourier Series#^thm-14-6|Theorem §14.6]]). Jumps can be removed first.

> [!remark] Remark: Method — Removing Jumps Before Numerical Integration
> Let $f$ be sectionally smooth on $-a < x < a$, extended periodically with period $2a$.
> 1. **Interior jumps.** Let $f_1$ be a step function with jumps of the same size and at the same positions as the jumps of $f$ in $-a < x < a$. Its Fourier coefficients can be found by integration. Then $f - f_1$ has no jumps in $-a < x < a$.
> 2. **Jumps at the ends.** The periodic extension of $f - f_1$ may still jump at $x = \pm a$, by $J = (f - f_1)(-a+) - (f - f_1)(a-)$. Let $f_2(x) = cx$ with $c = -J/(2a)$; its periodic extension jumps by $-2ca = J$ at $\pm a$, and its coefficients are known ($b_n = \frac{2ca}{n\pi}(-1)^{n+1}$, $a_n = 0$).
> 3. **The remainder.** $f_3 = f - f_1 - f_2$ is continuous, periodic and sectionally smooth, so its Fourier coefficients approach $0$ rapidly, and its series converges uniformly. Approximate the coefficients of $f_3$ numerically, by the formulas below.
> 4. **Add.** The coefficients of $f$ are those of $f_1$ and $f_2$ (exact) plus those of $f_3$ (approximate).

^rem-17-1

## The Trapezoidal Rule for Fourier Coefficients

Suppose now that $f(x)$ is continuous, sectionally smooth, and periodic with period $2a$, and approximate, for instance,

$$
a_0 = \frac{1}{2a}\int_{-a}^{a} f(x)\,dx .
$$

Cut the interval $-a < x < a$ into $r$ equal subintervals with endpoints $x_0, x_1, \dots, x_r$, where

$$
x_k = -a + k\,\Delta x, \qquad \Delta x = \frac{2a}{r} .
$$

The trapezoidal rule gives

$$
a_0 \cong \frac{1}{2a}\Big(\frac12 f(x_0) + f(x_1) + \cdots + f(x_{r-1}) + \frac12 f(x_r)\Big)\Delta x . \qquad (1)
$$

Since $x_0 = -a$, $x_r = a$ and $f$ is periodic with period $2a$, $f(x_0) = f(x_r)$: the two terms with multiplier $\frac12$ combine. So

$$
a_0 \cong \frac{1}{2a}\big(f(x_1) + f(x_2) + \cdots + f(x_r)\big)\cdot\frac{2a}{r} ,
$$

and the computed value is just the average of the function values. The other coefficients are approximated in the same way: $f(x)\cos(n\pi x/a)$ and $f(x)\sin(n\pi x/a)$ are again periodic, the end terms again combine, and $\frac1a\Delta x = \frac2r$. A caret over the coefficient name marks the approximations.

> [!definition] Definition §17.1: Approximate Fourier Coefficients
> Let $f(x)$ be continuous, sectionally smooth and periodic with period $2a$, and let $x_k = -a + 2ak/r$. The **approximate Fourier coefficients** of $f$ are
>
> $$
> \hat a_0 = \frac1r\big(f(x_1) + \cdots + f(x_r)\big), \qquad (2)
> $$
>
> $$
> \hat a_n = \frac2r\Big(f(x_1)\cos\Big(\frac{n\pi x_1}{a}\Big) + \cdots + f(x_r)\cos\Big(\frac{n\pi x_r}{a}\Big)\Big), \qquad (3)
> $$
>
> $$
> \hat b_n = \frac2r\Big(f(x_1)\sin\Big(\frac{n\pi x_1}{a}\Big) + \cdots + f(x_r)\sin\Big(\frac{n\pi x_r}{a}\Big)\Big). \qquad (4)
> $$
>
> If $r$ is odd, (3) and (4) are used for $n = 1, 2, \dots, (r - 1)/2$, a total of $r$ coefficients. If $r$ is even, (4) gives $\hat b_{r/2} = 0$, and (3) has to be modified for $n = r/2$:
>
> $$
> \hat a_{r/2} = \frac1r\Big(f(x_1)\cos\Big(\frac{r\pi x_1}{2a}\Big) + \cdots + f(x_r)\cos\Big(\frac{r\pi x_r}{2a}\Big)\Big). \qquad (3')
> $$
>
> Again there are $r$ valid coefficients. The formulas remain valid for equally spaced points on $0 \le x \le 2a$,
>
> $$
> x_0 = 0, \quad x_1 = \frac{2a}{r}, \quad x_2 = \frac{4a}{r}, \quad \dots, \quad x_r = 2a . \qquad (5)
> $$
>
> *Powers: 1.8, Summary, Equations (2)–(5) and (3′)*

^def-17-1

> [!remark]- Connections
> - The trapezoidal rule and its error bound $|E_T| \le K(b - a)^3/(12n^2)$: [[§57 Approximate Integration#^def-57-3|Calc Def. §57.3]], [[§57 Approximate Integration#^thm-57-1|Calc Thm. §57.1]]. For a smooth periodic integrand over a full period the actual error is far smaller than this general bound, which is why "one of the crudest numerical integration techniques is the best" here.

> [!example] Example §17.1: Four Samples of x²
> Let $f(x) = x^2$ on $-\pi < x < \pi$, extended with period $2\pi$ (continuous, with corners at $\pm\pi$). Compute the approximate coefficients with $r = 4$ and compare with the exact ones, $a_0 = \frac{\pi^2}{3}$, $a_n = \frac{4(-1)^n}{n^2}$, $b_n = 0$.
>
> **Data.** $a = \pi$, $x_k = -\pi + k\pi/2$: the points $x_1, x_2, x_3, x_4 = -\frac\pi2, 0, \frac\pi2, \pi$ with values $\frac{\pi^2}{4}, 0, \frac{\pi^2}{4}, \pi^2$.
>
> **Coefficients.** By (2), (3) and (3′) ($r = 4$ is even, so $\hat a_2$ uses the factor $\frac1r$):
>
> $$
> \hat a_0 = \frac14\Big(\frac{\pi^2}4 + 0 + \frac{\pi^2}4 + \pi^2\Big) = \frac{3\pi^2}{8}, \qquad
> \hat a_1 = \frac24\Big(\frac{\pi^2}4\cdot 0 + 0\cdot 1 + \frac{\pi^2}4\cdot 0 + \pi^2\cdot(-1)\Big) = -\frac{\pi^2}{2} ,
> $$
>
> $$
> \hat a_2 = \frac14\Big(\frac{\pi^2}4\cos(-\pi) + 0 + \frac{\pi^2}4\cos\pi + \pi^2\cos 2\pi\Big) = \frac14\cdot\frac{\pi^2}{2} = \frac{\pi^2}{8} ,
> $$
>
> and $\hat b_1 = \frac24\big(\frac{\pi^2}{4}(-1) + \frac{\pi^2}{4}(1) + \pi^2\sin\pi\big) = 0$, $\hat b_2 = 0$. These are $r = 4$ coefficients.
>
> **Comparison.** $\hat a_0 \approx 3.70$, $\hat a_1 \approx -4.93$, $\hat a_2 \approx 1.23$, against $a_0 \approx 3.29$, $a_1 = -4$, $a_2 = 1$. Four samples are too few for accuracy.
>
> **Interpolation.** But the trigonometric polynomial $F(x) = \frac{3\pi^2}8 - \frac{\pi^2}2\cos x + \frac{\pi^2}8\cos 2x$ reproduces the data exactly:
>
> $$
> F(0) = \frac{3\pi^2}8 - \frac{\pi^2}2 + \frac{\pi^2}8 = 0, \qquad F\big(\pm\tfrac\pi2\big) = \frac{3\pi^2}8 - \frac{\pi^2}8 = \frac{\pi^2}4, \qquad F(\pi) = \frac{3\pi^2}8 + \frac{\pi^2}2 + \frac{\pi^2}8 = \pi^2 .
> $$
>
> *Powers: 1.8, Equations (2)–(4) and (3′); the function is added*

^ex-17-1

## Half-Range Formulas

When $f(x)$ is given on $0 \le x \le a$ and its cosine or sine coefficients are wanted, the trapezoidal rule is applied on $0 \le x \le a$ itself. Now the end values $f(0)$ and $f(a)$ are not equal in general, and the factors $\frac12$ stay.

> [!definition] Definition §17.2: Approximate Half-Range Coefficients
> Divide $0 \le x \le a$ into $s$ equal subintervals with endpoints $0 = x_0, x_1, \dots, x_s = a$, $x_i = ia/s$. The **approximate Fourier cosine coefficients** of $f$ (or of its even extension) are
>
> $$
> \begin{aligned}
> \hat a_0 &= \frac1s\Big(\frac12 f(x_0) + f(x_1) + \cdots + f(x_{s-1}) + \frac12 f(x_s)\Big), \\
> \hat a_n &= \frac2s\Big(\frac12 f(x_0) + f(x_1)\cos\Big(\frac{n\pi x_1}{a}\Big) + \cdots + \frac12 f(x_s)\cos\Big(\frac{n\pi x_s}{a}\Big)\Big), \qquad n = 1, \dots, s - 1, \\
> \hat a_s &= \frac1s\Big(\frac12 f(x_0) + f(x_1)\cos\Big(\frac{s\pi x_1}{a}\Big) + \cdots + \frac12 f(x_s)\cos\Big(\frac{s\pi x_s}{a}\Big)\Big),
> \end{aligned} \qquad (6)
> $$
>
> and the **approximate Fourier sine coefficients** of $f$ (or of its odd extension) are
>
> $$
> \hat b_n = \frac2s\Big(f(x_1)\sin\Big(\frac{n\pi x_1}{a}\Big) + \cdots + f(x_{s-1})\sin\Big(\frac{n\pi x_{s-1}}{a}\Big)\Big), \qquad n = 1, 2, \dots, s . \qquad (7)
> $$
>
> (The end terms of (7) vanish because $\sin 0 = \sin(n\pi) = 0$. For $n = s$ every term vanishes, since $s\pi x_i/a = i\pi$; so the $s - 1$ interior values determine $s - 1$ sine coefficients.)
>
> *Powers: 1.8, Equations (6) and (7)*

^def-17-2

## Interpolation

> [!theorem] Theorem §17.1: The Approximate Series Interpolates
> Let $\hat a_0, \hat a_1, \hat b_1, \dots$ be the $r$ approximate coefficients calculated from (2)–(4) (with (3′) if $r$ is even), and let
>
> $$
> F(x) = \hat a_0 + \hat a_1\cos\Big(\frac{\pi x}{a}\Big) + \hat b_1\sin\Big(\frac{\pi x}{a}\Big) + \cdots
> $$
>
> be the finite Fourier series using these $r$ coefficients. Then $F$ interpolates $f$ at $x_1, x_2, \dots, x_r$:
>
> $$
> F(x_i) = f(x_i), \qquad i = 1, 2, \dots, r .
> $$
>
> Thus the graph of $F$ cuts the graph of $f$ at the points $x_i$.
>
> *Powers: 1.8 (text)*

^thm-17-1

*Powers omits the proof.*

Example §17.1 shows the theorem at work with $r = 4$. In the next example the half-range cosine version passes through all seven sample points as well (the cosine formulas (6) are (2)–(4) applied to the even extension, sampled at $r = 2s$ points).

> [!example] Example §17.2: Approximate Coefficients of sin(x)/x
> Calculate the approximate Fourier coefficients of $f(x) = \sin(x)/x$ in $-\pi < x < \pi$ (with $f(0) = 1$).
>
> Since $f$ is even, it has a cosine series. The computation is simpler with the half-range formulas (6), taking $s$ even: $s = 6$, $x_0 = 0$, $x_1 = \frac\pi6$, …, $x_5 = \frac{5\pi}6$, $x_6 = \pi$. The numerical information:
>
> | $i$ | $x_i$ | $\cos x_i$ | $\cos 2x_i$ | $\cos 3x_i$ | $\sin(x_i)/x_i$ |
> |---|---|---|---|---|---|
> | 0 | $0$ | 1.0 | 1.0 | 1.0 | 1.0 |
> | 1 | $\pi/6$ | 0.86603 | 0.5 | 0 | 0.95493 |
> | 2 | $\pi/3$ | 0.5 | −0.5 | −1.0 | 0.82699 |
> | 3 | $\pi/2$ | 0 | −1.0 | 0 | 0.63662 |
> | 4 | $2\pi/3$ | −0.5 | −0.5 | 1.0 | 0.41350 |
> | 5 | $5\pi/6$ | −0.86603 | 0.5 | 0 | 0.19099 |
> | 6 | $\pi$ | −1.0 | 1.0 | −1.0 | 0.0 |
>
> For instance
>
> $$
> \hat a_0 = \frac16\Big(\frac12\cdot 1 + 0.95493 + 0.82699 + 0.63662 + 0.41350 + 0.19099 + \frac12\cdot 0\Big) = \frac{3.52303}{6} = 0.58717 .
> $$
>
> The exact coefficients follow from $\sin x\cos nx = \frac12\big(\sin(n + 1)x - \sin(n - 1)x\big)$ and the sine integral $\operatorname{Si}(z) = \int_0^z \frac{\sin t}{t}\,dt$:
>
> $$
> a_0 = \frac1\pi\operatorname{Si}(\pi), \qquad a_n = \frac2\pi\int_0^{\pi}\frac{\sin x}{x}\cos(nx)\,dx = \frac1\pi\Big(\operatorname{Si}\big((n + 1)\pi\big) - \operatorname{Si}\big((n - 1)\pi\big)\Big) .
> $$
>
> | $n$ | $\hat a_n$ | $a_n$ | error |
> |---|---|---|---|
> | 0 | 0.58717 | 0.58949 | 0.00232 |
> | 1 | 0.45611 | 0.45141 | 0.00470 |
> | 2 | −0.06130 | −0.05640 | 0.00490 |
> | 3 | 0.02883 | 0.02356 | 0.00528 |
> | 6 | −0.00701 | −0.00569 | 0.00132 |
>
> ($\hat a_6$ uses the last formula of (6), with the factor $\frac16$.) The figure below shows the difference between $f(x)$ and $F(x) = \hat a_0 + \hat a_1\cos x + \cdots + \hat a_6\cos 6x$, the sum of the Fourier series with the approximate coefficients.
>
> *Powers: 1.8, Example, Tables 3 and 4; Exercise 1.8.1 ($\hat a_6$)*

^ex-17-2

![[m341-13-1.svg]]
*Example §13.2: the error $f(x) - F(x)$ for $f(x) = \sin(x)/x$ and the cosine polynomial $F$ built from the seven approximate coefficients $\hat a_0, \dots, \hat a_6$. The error vanishes at the sample points $x_i = i\pi/6$ (red), as Theorem §17.1 predicts; between them it stays below $0.032$, growing toward $x = \pi$.*

> [!example] Example §17.3: Removing a Jump First
> Approximate the Fourier coefficients of $f(x) = x + x^2$, $-\pi < x < \pi$ (period $2\pi$), with $r = 8$, and compare with the naive use of (2)–(4).
>
> **Prepare** (Remark: Method — Removing Jumps Before Numerical Integration). There are no interior jumps ($f_1 = 0$). At the ends, $f(-\pi+) - f(\pi-) = (\pi^2 - \pi) - (\pi^2 + \pi) = -2\pi$, so $c = 2\pi/(2\pi) = 1$ and $f_2(x) = x$, with exact coefficients $b_n = \frac{2(-1)^{n+1}}{n}$, $a_n = 0$. The remainder $f_3 = x^2$ is continuous and periodic, with exact $a_0 = \frac{\pi^2}3$, $a_n = \frac{4(-1)^n}{n^2}$.
>
> **Approximate $f_3$.** The points are $x_k = -\pi + k\pi/4$, $k = 1, \dots, 8$, with $x_k^2 = \frac{9\pi^2}{16}, \frac{\pi^2}4, \frac{\pi^2}{16}, 0, \frac{\pi^2}{16}, \frac{\pi^2}4, \frac{9\pi^2}{16}, \pi^2$. Then
>
> $$
> \hat a_0 = \frac{11\pi^2}{32} \approx 3.393, \qquad \hat a_1 = -\frac{\pi^2}{4}\Big(1 + \frac{\sqrt2}2\Big) \approx -4.212, \qquad \hat a_2 = \frac{\pi^2}{8} \approx 1.234, \qquad \hat a_3 = -\frac{\pi^2}{4}\Big(1 - \frac{\sqrt2}2\Big) \approx -0.723 ,
> $$
>
> against $3.290$, $-4$, $1$, $-0.444$; the $\hat b_n$ of the even function $x^2$ vanish. Adding the exact coefficients of $f_2$: $f$ has $a_n \approx \hat a_n$ as listed and $b_n = 2, -1, \frac23, \dots$ exactly.
>
> **Naive.** Applying (3) and (4) to $f$ itself, with the one-sided value $f(x_8) = f(\pi-) = \pi + \pi^2$, adds $\frac28\pi\cos(n\pi) = \pm\frac\pi4$ to each $\hat a_n$: $\hat a_1 \approx -4.998$, $\hat a_2 \approx 2.019$, $\hat a_3 \approx -1.508$, errors of about $1$ instead of about $0.2$. (Had the average $\frac12\big(f(\pi-) + f(-\pi+)\big) = \pi^2$ been used at the jump instead, these extra terms would vanish and the $\hat a_n$ would agree with the prepared ones; the sine coefficients below are poor either way.) The sine coefficients come from the samples of $x$ alone:
>
> $$
> \hat b_1 = \frac{\pi(1 + \sqrt2)}{4} \approx 1.896, \qquad \hat b_2 = -\frac\pi4 \approx -0.785, \qquad \hat b_3 = \frac{\pi(\sqrt2 - 1)}{4} \approx 0.325 ,
> $$
>
> against the exact $2$, $-1$, $0.667$: the slowly decaying coefficients of the jump are badly approximated, while the procedure gets them exactly.
>
> *Powers: 1.8, Figure 11 (the procedure); the function is added*

^ex-17-3
