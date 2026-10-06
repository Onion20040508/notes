---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 1
section: 9
powers: "1.4"
aliases: ["Powers 1.4"]
tags: [fourier-series-and-pdes, math341]
---
← [[§8 Convergence of Fourier Series]] · ↑ [[· 1 Fourier Series and Integrals]] · [[§10 Operations on Fourier Series]] →

*Powers, Section 1.4 · MAT 341 lectures 9.3, 9.5, 9.10 · HW 2.*

The convergence theorem of [[§8 Convergence of Fourier Series|§8]] works one point at a time. A stronger kind of convergence is uniform convergence on an interval: the largest error of the partial sum $S_N$ over the whole interval tends to zero, so a finite number of terms approximates $f$ to a prescribed accuracy everywhere at once. A uniformly convergent Fourier series must converge to a continuous function, so a function with a jump never has one; near a jump the partial sums overshoot (Gibbs' phenomenon). There are two practical tests. From the coefficients: if $\sum(|a_n| + |b_n|)$ converges, the series converges uniformly (the Weierstrass M-test). From the function: if the periodic extension is continuous with a sectionally continuous derivative, the series converges uniformly to it. Uniform convergence is what licenses the term-by-term operations of [[§10 Operations on Fourier Series|§10]], and hence the verification that series solutions of the heat and wave equations really satisfy them.

## Uniform Convergence

> [!definition] Definition §9.1: Pointwise Convergence
> Let $g_n$ and $g$ be functions on a common domain. $(g_n)$ **converges pointwise** to $g$ if $|g_n(x) - g(x)| \to 0$ as $n \to \infty$ for each $x$ in the domain.
>
> *Source: 341 lecture 9.3*

^def-9-1

> [!definition] Definition §9.1: Uniform Convergence
> Let $g_n$ and $g$ be functions on a common domain. $(g_n)$ **converges uniformly** to $g$ if $\sup_x|g_n(x) - g(x)| \to 0$ as $n \to \infty$, the supremum taken over all $x$ in the domain.
>
> Uniform convergence implies pointwise convergence ([[§9 Uniform Convergence#^def-9-1|Definition §9.1]]), but not conversely.
>
> *Source: 341 lecture 9.3*

^def-9-new1

> [!remark]- Connections
> - Rigorous definitions: [[§24 Uniform Convergence#^def-24-1|451 Def. §24.1]], [[§24 Uniform Convergence#^def-24-2|451 Def. §24.2]] ($N$ independent of $x$); the supremum form used here is [[§24 Uniform Convergence#^thm-24-1|451 Thm. §24.1]]. Ross's standard example of pointwise but not uniform convergence is $x^n$ on $[0, 1]$, [[§24 Uniform Convergence#^ex-24-2|451 Ex. §24.2]].

> [!definition] Definition §9.2: Uniform Convergence of a Fourier Series
> Let
>
> $$
> S_N(x) = a_0 + \sum_{n=1}^{N} a_n\cos\Big(\frac{n\pi x}{a}\Big) + b_n\sin\Big(\frac{n\pi x}{a}\Big)
> $$
>
> be the partial sum of the Fourier series of $f$. The **maximum deviation** between the graphs of $S_N$ and $f$ is
>
> $$
> \delta_N = \max_{-a \le x \le a}|f(x) - S_N(x)| ,
> $$
>
> the maximum taken over all $x$ in the interval, including the endpoints (if $f$ is not continuous, the maximum must be replaced by the supremum, or least upper bound). If $\delta_N \to 0$ as $N$ increases, the series **converges uniformly** on $-a \le x \le a$.
>
> Roughly speaking, if a Fourier series converges uniformly, then the sum of $N$ terms approximates $f(x)$ to within $\pm\delta_N$ at *any and every* point of the interval, and by taking $N$ large enough the error can be made as small as necessary.
>
> *Powers: 1.4 (text)*

^def-9-2

> [!example] Example §9.1: Pointwise but Not Uniform
> On $0 < x < 1$:
> - $g_n(x) = 0$ for $0 < x < 1 - \frac1n$ and $g_n(x) = 1$ for $1 - \frac1n < x < 1$. For each fixed $x$, $g_n(x) = 0$ as soon as $\frac1n < 1 - x$, so $g_n \to g = 0$ pointwise. But $\sup_x|g_n(x) - 0| = 1$ for every $n$: the step slides toward $x = 1$ without shrinking, and the convergence is not uniform.
> - $g_n(x) = \frac1n$ converges to $0$ uniformly: $\sup_x|g_n(x)| = \frac1n \to 0$.
>
> On $-1 < x < 1$, $g_n(x) = 0$ for $x \le 0$, $nx$ for $0 \le x \le \frac1n$, $1$ for $\frac1n < x < 1$ consists of continuous functions converging pointwise to the step $g(x) = 0$ for $x \le 0$, $1$ for $x > 0$; but $\sup_x|g_n(x) - g(x)| = 1$, since $g_n(x) \to 0$ as $x \to 0+$ while $g = 1$ there. The limit is discontinuous, which Theorem §9.1(1) below forbids for a uniform limit.
>
> *Source: 341 lecture 9.3, Examples 1–3*

^ex-9-1

There are two important facts about uniform convergence.

> [!theorem] Theorem §9.1: Uniform Convergence Forces Continuity
> If a Fourier series converges uniformly in a period interval, then
> 1. it must converge to a continuous function, and
> 2. it must converge to the (continuous) function that generates the series.
>
> Thus a function that has a nonremovable discontinuity *cannot* have a uniformly convergent Fourier series. (And not all continuous functions have uniformly convergent Fourier series.)
>
> *Powers: 1.4 (text)*

^thm-9-1

*Powers omits the proof. (1) is [[§25 More on Uniform Convergence#^thm-25-2|451 Thm. §25.2]] applied to the partial sums $S_N$, which are continuous: a uniform limit of continuous functions is continuous, [[§24 Uniform Convergence#^thm-24-2|451 Thm. §24.2]]. For sectionally smooth $f$, (2) follows from (1) and [[§8 Convergence of Fourier Series#^thm-8-1|Theorem §8.1]]: the uniform limit is also the pointwise limit $\frac12(f(x+) + f(x-))$, which must then be continuous.*

> [!remark]- Connections
> - The jump in [[§9 Uniform Convergence#^ex-9-1|Example §9.1]] is the same phenomenon as Ross's $x^n \to$ (a step at $1$), [[§24 Uniform Convergence#^ex-24-2|451 Ex. §24.2]]: a discontinuous limit is a certificate that the convergence is not uniform.

> [!remark] Remark: The Gibbs Phenomenon
> The figure below shows partial sums of the square wave $f(x) = 1$ for $0 < x < \pi$, $-1$ for $-\pi < x < 0$, whose Fourier series is $\frac4\pi\big(\sin x + \frac13\sin 3x + \frac15\sin 5x + \cdots\big)$. For every $N$ there are points near $x = 0$ and $x = \pm\pi$ where $|f(x) - S_N(x)|$ is nearly equal to $1$ (just beside the jump, $S_N$ is near $0$), so $\delta_N \not\to 0$ and the convergence is *not* uniform, as Theorem §9.1 predicts. The graphs also show the partial sums overshooting their mark near $x = 0$: this feature of Fourier series is called **Gibbs' phenomenon**, and it always occurs near a jump. The overshoot does not shrink as $N$ grows; it moves closer to the jump. For the square wave the peak of $S_N$ next to $0$ tends to $\frac2\pi\int_0^\pi\frac{\sin t}{t}\,dt \approx 1.179$: an overshoot of about $9\%$ of the jump $2$.

^rem-9-1

![[m341-9-1.svg]]
*Partial sums $S_3$, $S_{11}$ and $S_{41}$ of the square wave (black). Away from the jumps they settle down to $\pm1$; next to each jump they overshoot to about $1.18$, and the overshoot only moves toward the jump as $N$ grows. Convergence is not uniform.*

On the other hand, for the triangle wave $f(x) = |x|$ (Powers calls it a sawtooth) the maximum deviation occurs at $x = 0$ and tends to zero: the convergence is uniform ([[§9 Uniform Convergence#^ex-9-2|Example §9.2]]). One way of proving uniform convergence is by examining the coefficients.

> [!theorem] Theorem §9.2: Absolutely Summable Coefficients Give Uniform Convergence
> If the series $\sum_{n=1}^{\infty}\big(|a_n| + |b_n|\big)$ converges, then the Fourier series
>
> $$
> a_0 + \sum_{n=1}^{\infty} a_n\cos\Big(\frac{n\pi x}{a}\Big) + b_n\sin\Big(\frac{n\pi x}{a}\Big)
> $$
>
> converges uniformly in the interval $-a \le x \le a$ and, in fact, on the whole interval $-\infty < x < \infty$, to a continuous function.
>
> *Powers: 1.4, Theorem 1; Source: 341 lecture 9.10, Theorem 3*

^thm-9-2

*Powers omits the proof. It is the Weierstrass M-test, [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]], with $M_n = |a_n| + |b_n|$: for every real $x$, $\big|a_n\cos\frac{n\pi x}{a} + b_n\sin\frac{n\pi x}{a}\big| \le |a_n| + |b_n|$, and $\sum M_n < \infty$. The limit is continuous by [[§25 More on Uniform Convergence#^thm-25-2|451 Thm. §25.2]].*

> [!remark]- Connections
> - The M-test with its proof, [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]]; the first of Ross's applications, [[§25 More on Uniform Convergence#^ex-25-3|451 Ex. §25.3]](1), is the Fourier series $\sum\cos(nx)/n^2$. The test is sufficient, not necessary; it says nothing about series such as $\sum\sin(nx)/n$, whose coefficients are not absolutely summable.

> [!example] Example §9.2: The Triangle Wave |x|
> For $f(x) = |x|$, $-\pi < x < \pi$, periodic with period $2\pi$, the Fourier coefficients are
>
> $$
> a_0 = \frac\pi2, \qquad a_n = \frac2\pi\cdot\frac{\cos n\pi - 1}{n^2}, \qquad b_n = 0
> $$
>
> ($f$ is even, so $a_0 = \frac1\pi\int_0^\pi x\,dx = \frac\pi2$ and $a_n = \frac2\pi\int_0^\pi x\cos nx\,dx = \frac2\pi\cdot\frac{(-1)^n - 1}{n^2}$). So
>
> $$
> |x| = \frac\pi2 - \frac4\pi\Big(\cos x + \frac{\cos 3x}{9} + \frac{\cos 5x}{25} + \cdots\Big) .
> $$
>
> **By the coefficients.** $|a_n| \le \frac{4}{\pi n^2}$ and $\sum 1/n^2$ converges, so the series of absolute values of the coefficients converges, and by Theorem §9.2 the Fourier series converges uniformly on $-\pi \le x \le \pi$, to $|x|$ ([[§8 Convergence of Fourier Series#^thm-8-1|Theorem §8.1]]), and in fact to the periodic extension of $|x|$ on the whole real line.
>
> **By the function.** The periodic extension is continuous, because $f(-\pi+) = \pi = f(\pi-)$, and $f$ is sectionally smooth (Theorem §9.3 below).
>
> **The maximum deviation.** $f(x) - S_N(x) = -\frac4\pi\sum_{n\ \text{odd},\ n > N}\frac{\cos nx}{n^2}$ has coefficients of one sign, so its absolute value is at most $\frac4\pi\sum_{n\ \text{odd},\ n > N}\frac{1}{n^2}$, with equality at $x = 0$, where all the cosines equal $1$ (there $S_N(0) > 0 = f(0)$): $\delta_N = \frac4\pi\sum_{n\ \text{odd},\ n > N}\frac{1}{n^2}$. For instance $\delta_1 = \delta_2 = \frac\pi2 - \frac4\pi \approx 0.298$ and $\delta_3 = \delta_4 \approx 0.156$; $\delta_N \to 0$ because it is the tail of a convergent series.
>
> *Powers: 1.4, first Example; Figure 10; Source: 341 lecture 9.10, Example 1*

^ex-9-2

![[m341-9-2.svg]]
*The triangle wave $|x|$ (black) and its partial sums $S_0 = \pi/2$, $S_1$ and $S_3$. The worst error is always at the corner $x = 0$ (and $\pm\pi$), and it shrinks to zero: the convergence is uniform.*

Another way of proving uniform convergence of a Fourier series is by examining the function that generates it.

> [!theorem] Theorem §9.3: Continuous, Sectionally Smooth Functions
> If $f$ is periodic and continuous and has a sectionally continuous derivative, then the Fourier series corresponding to $f$ converges uniformly to $f(x)$ on the entire real axis.
>
> *Powers: 1.4, Theorem 2; Source: 341 lecture 9.5, Main Theorem 2*

^thm-9-3

*Powers omits the proof; no other subject in the vault proves it. The remark below, which is not from Powers, shows how it follows from Theorem §9.2 and two later results of this chapter.*

> [!remark]- Remark: Where Theorem §9.3 Comes From
> Take period $2\pi$. Since $f$ is continuous and $f'$ is sectionally continuous, the Fourier coefficients of $f'$ are $nb_n$ and $-na_n$ ([[§10 Operations on Fourier Series#^thm-10-6|Theorem §10.6]], proof of (8)). Bessel's inequality for $f'$ ([[§11★ Mean Error and Convergence in Mean#^thm-11-3|Theorem §11.3]]) gives $\sum n^2(a_n^2 + b_n^2) \le \frac1\pi\int_{-\pi}^{\pi}(f')^2 < \infty$. By the [[Cauchy–Schwarz inequality]] for sums and $(|a_n| + |b_n|)^2 \le 2(a_n^2 + b_n^2)$,
>
> $$
> \sum_{n=1}^{\infty}\big(|a_n| + |b_n|\big) = \sum_{n=1}^{\infty}\frac1n\cdot n\big(|a_n| + |b_n|\big) \le \Big(\sum_{n=1}^{\infty}\frac{1}{n^2}\Big)^{1/2}\Big(\sum_{n=1}^{\infty} 2n^2\big(a_n^2 + b_n^2\big)\Big)^{1/2} < \infty .
> $$
>
> So the series converges uniformly by Theorem §9.2, and since $f$ is continuous and sectionally smooth its sum is $f(x)$ by [[§8 Convergence of Fourier Series#^thm-8-1|Theorem §8.1]]. Neither later result depends on Theorem §9.3, so the argument is not circular.
>
> *Source: an argument added in these notes (Bessel's inequality for $f'$ and the Cauchy–Schwarz inequality); not in Powers.*

^rem-9-2

While Theorem §9.3 is stated for a periodic function, it may be adapted to a function $f$ given on $-a < x < a$: if the *periodic extension* of $f$ satisfies the conditions of the theorem, the Fourier series of $f$ converges uniformly on $-a \le x \le a$.

> [!example] Example §9.3: Checking the Hypotheses
> Decide whether the Fourier series converges uniformly.
>
> **(a)** $f(x) = x$, $-1 < x < 1$. Although $f$ is continuous and has a continuous derivative on $-1 < x < 1$, its periodic extension is not continuous: it jumps at $\pm1$. The Fourier series cannot converge uniformly in any interval containing $1$ or $-1$, because uniform convergence must produce a continuous function (Theorem §9.1).
>
> **(b)** $f(x) = |\sin x|$, periodic with period $2\pi$, is continuous and has a sectionally continuous derivative ($\pm\cos x$, with jumps at the multiples of $\pi$). Therefore its Fourier series converges uniformly to $f(x)$ everywhere.
>
> **(c)** $f(x) = \frac{\sin x}{x}$ on $(-\pi, \pi)$, $f(0) = 1$, extended with period $2\pi$ ([[§8 Convergence of Fourier Series#^ex-8-5|Example §8.5]]). It is continuous on $(-\pi, \pi)$, and $f(\pi-) = 0 = f(-\pi+)$, so the periodic extension is continuous on $\mathbb{R}$; $f'(x) = \frac{x\cos x - \sin x}{x^2}$ is continuous on $(-\pi, \pi)$ with one-sided limits at $\pm\pi$, hence sectionally continuous. By Theorem §9.3 the series converges uniformly to $f$. (If $f(0) = 0$ is kept, as the problem sheet prints it, the discontinuity at $0$ is removable; Powers removes such discontinuities before applying the theorems.)
>
> **(d)** $f(x) = 1 + 2x - 2x^3$, $-1 < x < 1$. Here $f(-1+) = 1 - 2 + 2 = 1$ and $f(1-) = 1 + 2 - 2 = 1$, so the periodic extension of period $2$ is continuous; $f'(x) = 2 - 6x^2$ is continuous on $(-1, 1)$ with limits $-4$ at both ends, so the derivative of the extension is sectionally continuous (it jumps only where $f'(1-) \ne f'(-1+)$, and here it does not even jump). The series converges uniformly.
>
> *Powers: 1.4, second Example; Exercises 1.4.1(g), 1.4.2; Source: 341 lecture 9.5, Example 2; 341 HW 2, Problem 3(d)*

^ex-9-3

## Functions on an Interval

Here is a restatement of Theorem §9.3 for a function given on the interval $-a < x < a$. The condition at the endpoints replaces the condition of continuity of the periodic extension of $f$.

> [!theorem] Theorem §9.4: Uniform Convergence on −a ≤ x ≤ a
> If $f$ is given on $-a < x < a$, if $f$ is continuous and bounded and has a sectionally continuous derivative, and if $f(-a+) = f(a-)$, then the Fourier series of $f$ converges uniformly to $f$ on the interval $-a \le x \le a$. (The series converges to $f(a-) = f(-a+)$ at $x = \pm a$.)
>
> *Powers: 1.4, Theorem 3*

^thm-9-4

> [!proof]+ Proof
> Since $f'$ is sectionally continuous, it is bounded, so $f$ is uniformly continuous on $(-a, a)$ and the one-sided limits $f(-a+)$, $f(a-)$ exist. (Powers assumes this; it follows from the mean value inequality $|f(x) - f(y)| \le M|x - y|$ with $M$ a bound for $|f'|$.) Define $f(\pm a)$ to be their common value and let $\bar f$ be the periodic extension of period $2a$. At $x = a$, $\bar f(a-) = f(a-)$ and $\bar f(a+) = f(-a+)$, which are equal by hypothesis, and they equal $\bar f(a)$; the same holds at every point $a + 2ka$. Inside the period intervals $\bar f$ is continuous because $f$ is. So $\bar f$ is periodic and continuous, its derivative is sectionally continuous, and Theorem §9.3 gives uniform convergence of the Fourier series to $\bar f$ on the whole line, in particular to $f$ on $-a \le x \le a$, with the value $f(a-) = f(-a+)$ at $\pm a$.

^pf-9-4

*Uses:* [[§9 Uniform Convergence#^thm-9-3|§9.3]], [[§7 Arbitrary Period and Half-Range Expansions#^def-7-1|Def. §7.1]], [[§29 The Mean Value Theorem#^prop-29-8|451 Prop. §29.8]] (mean value inequality)

If an odd periodic function is to be continuous, it must have value $0$ at $x = 0$ and at the endpoints of the symmetric period-interval. Thus the odd periodic extension of a function given in $0 < x < a$ may have jump discontinuities even though $f$ is continuous where originally given. The even periodic extension causes no such difficulty.

> [!theorem] Theorem §9.5: Uniform Convergence of the Sine Series
> If $f$ is given on $0 < x < a$, if $f$ is continuous and bounded and has a sectionally continuous derivative, and if $f(0+) = f(a-) = 0$, then the Fourier sine series of $f$ converges uniformly to $f$ in the interval $0 \le x \le a$. (The series converges to $0$ at $x = 0$ and $x = a$.)
>
> *Powers: 1.4, Theorem 4*

^thm-9-5

> [!proof]+ Proof
> The sine series is the Fourier series of the odd extension $f_o$ on $-a < x < a$ ([[§7a Even and Odd Functions; Half-Range Expansions#^def-7-new1|Definition §7.4]]). $f_o$ is continuous and bounded on $(-a, 0)$ and $(0, a)$, with derivative $f_o'(x) = f'(-x)$ for $-a < x < 0$, hence sectionally continuous. At $0$: $f_o(0+) = f(0+)$ and $f_o(0-) = -f(0+)$, which agree exactly when $f(0+) = 0$; then $f_o$, with $f_o(0) = 0$, is continuous on $(-a, a)$. At the ends: $f_o(a-) = f(a-)$ and $f_o(-a+) = -f(a-)$, which agree exactly when $f(a-) = 0$. So under the hypotheses $f_o$ satisfies Theorem §9.4, and the series converges uniformly to $f_o$ on $-a \le x \le a$, with value $0$ at $x = 0$ and at $x = \pm a$; on $0 \le x \le a$ this is the claim.

^pf-9-5

*Uses:* [[§9 Uniform Convergence#^thm-9-4|§9.4]], [[§7a Even and Odd Functions; Half-Range Expansions#^def-7-3|Def. §7.3]], [[§7a Even and Odd Functions; Half-Range Expansions#^def-7-new1|Def. §7.4]]

> [!theorem] Theorem §9.6: Uniform Convergence of the Cosine Series
> If $f$ is given on $0 < x < a$ and if $f$ is continuous and bounded and has a sectionally continuous derivative, then the Fourier cosine series of $f$ converges uniformly to $f$ in the interval $0 \le x \le a$. (The series converges to $f(0+)$ at $x = 0$ and to $f(a-)$ at $x = a$.)
>
> *Powers: 1.4, Theorem 5*

^thm-9-6

> [!proof]+ Proof
> The cosine series is the Fourier series of the even extension $f_e$. Now $f_e(0+) = f(0+) = f_e(0-)$ and $f_e(a-) = f(a-) = f_e(-a+)$ hold automatically, so, defining $f_e(0) = f(0+)$, $f_e$ is continuous on $(-a, a)$, its derivative $f_e'(x) = -f'(-x)$ ($x < 0$) is sectionally continuous, and $f_e(-a+) = f_e(a-)$. Theorem §9.4 gives uniform convergence to $f_e$ on $-a \le x \le a$, with value $f(0+)$ at $0$ and $f(a-)$ at $\pm a$.

^pf-9-6

*Uses:* [[§9 Uniform Convergence#^thm-9-4|§9.4]], [[§7a Even and Odd Functions; Half-Range Expansions#^def-7-3|Def. §7.3]], [[§7a Even and Odd Functions; Half-Range Expansions#^def-7-4|Def. §7.4]]

For example, $f(x) = x$, $0 < x < 1$ ([[§7a Even and Odd Functions; Half-Range Expansions#^ex-7-3|Example §7.3]]): its cosine series converges uniformly on $0 \le x \le 1$ (Theorem §9.6; the coefficients are $O(1/n^2)$), but its sine series does not, since $f(1-) = 1 \ne 0$.

> [!remark] Remark: Method — Deciding Uniform Convergence
> Given a Fourier series, decide uniform convergence in one of two ways.
> 1. **From the function** (when $f$ is known): sketch the periodic extension (odd or even periodic extension for a sine or cosine series). If it is continuous on $\mathbb{R}$ (for a function on $-a < x < a$: $f(-a+) = f(a-)$; for a sine series: $f(0+) = f(a-) = 0$) and its derivative is sectionally continuous, the convergence is uniform, to $f$ (Theorems §9.3–§9.6). If it has a jump, the convergence is *not* uniform (Theorem §9.1).
> 2. **From the coefficients** (when only the series is known): if $\sum(|a_n| + |b_n|) < \infty$, for instance $|a_n|, |b_n| \le C/n^2$, the convergence is uniform (Theorem §9.2). If the coefficients are only $O(1/n)$, this test says nothing.
>
> Review of the lecture: *sectionally smooth* gives pointwise convergence to $\frac12(f(x+) + f(x-))$; *continuous and sectionally smooth* gives uniform convergence to $f(x)$.
>
> *Source: 341 lecture 9.10 (review)*

^rem-9-3

## Examples

> [!example] Example §9.4: The Rectified Sine |sin x| of Period π
> Let $f$ be periodic with period $\pi$, $f(x) = |\sin x|$ on $(-\pi/2, \pi/2)$. **(a)** Find its Fourier series. **(b)** Does the series converge pointwise to $f(x)$? **(c)** Does it converge uniformly to $f(x)$?
>
> **(a)** Here $a = \pi/2$, so the series is in $\cos 2nx$, $\sin 2nx$. $f$ is even, so $b_n = 0$,
>
> $$
> a_0 = \frac{2}{\pi}\int_0^{\pi/2}\sin x\,dx = \frac2\pi, \qquad a_n = \frac{4}{\pi}\int_0^{\pi/2}\sin x\cos 2nx\,dx = \frac2\pi\int_0^{\pi/2}\big[\sin(2n + 1)x - \sin(2n - 1)x\big]dx = \frac2\pi\Big(\frac{1}{2n + 1} - \frac{1}{2n - 1}\Big) = -\frac4\pi\cdot\frac{1}{4n^2 - 1} ,
> $$
>
> since $\int_0^{\pi/2}\sin kx\,dx = \frac1k$ for odd $k$. So $f(x) \sim \frac2\pi - \frac4\pi\sum_{n=1}^{\infty}\frac{1}{4n^2 - 1}\cos 2nx$, the series of [[§7 Arbitrary Period and Half-Range Expansions#^ex-7-1|Example §7.1]] with $x$ replaced by $x/\pi$.
>
> **(b)** Yes. $f$ is sectionally smooth ($f' = \cos x$ on $(0, \frac\pi2)$, $-\cos x$ on $(-\frac\pi2, 0)$, a corner at $0$), so the series converges to $\frac12(f(x+) + f(x-))$ ([[§8 Convergence of Fourier Series#^thm-8-1|Theorem §8.1]]). Moreover $f(-\frac\pi2+) = 1 = f(\frac\pi2-)$, so the periodic extension is continuous on $\mathbb{R}$, and the limit is $f(x)$ at every point.
>
> **(c)** Yes, for the same reasons: $f$ is continuous on $\mathbb{R}$ with a sectionally continuous derivative (Theorem §9.3). Alternatively, $\sum|a_n| = \frac4\pi\sum\frac{1}{4n^2 - 1}$ converges (Theorem §9.2).
>
> *The key writes the integrand of $a_n$ as $\sin x\cos nx$; the computation that follows, and its result, use $\cos 2nx$.*
>
> *Powers: Exercise 1.1.1(d); Source: 341 HW 2, Problem 1*

^ex-9-4

> [!example] Example §9.5: A Quadratic from Its Series, and the Sum of 1/n²
> The series $\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}\cos nx$ is the Fourier expansion of a function $f$ whose formula on $(-\pi, \pi)$ is $f(x) = A + Bx + Cx^2$. **(a)** Determine $A$, $B$, $C$. **(b)** Does the series converge uniformly?
>
> **(a)** By uniqueness of the coefficients ([[§10 Operations on Fourier Series#^thm-10-5|Theorem §10.5]]), compute the Fourier coefficients of $A + Bx + Cx^2$ and match:
>
> $$
> a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi}(A + Bx + Cx^2)\,dx = A + \frac{\pi^2}{3}C = 0, \qquad
> b_n = \frac1\pi\int_{-\pi}^{\pi}Bx\sin nx\,dx = \frac{2(-1)^{n + 1}}{n}B = 0,
> $$
>
> $$
> a_n = \frac1\pi\int_{-\pi}^{\pi}Cx^2\cos nx\,dx = \frac{4(-1)^n}{n^2}C = \frac{(-1)^n}{n^2}
> $$
>
> ($A$ and $Bx\cos nx$ integrate to zero against $\cos nx$; $\frac1\pi\int_{-\pi}^{\pi}x^2\cos nx\,dx = \frac{4(-1)^n}{n^2}$ by two integrations by parts). So $B = 0$, $C = \frac14$, $A = -\frac{\pi^2}{12}$: $f(x) = \frac{x^2}{4} - \frac{\pi^2}{12}$.
>
> **(b)** Yes, in two ways. $|a_n| = \frac{1}{n^2}$ is summable (Theorem §9.2). Or: $f(-\pi+) = \frac{\pi^2}{6} = f(\pi-)$, so the periodic extension is continuous, and $f'(x) = \frac x2$ is sectionally continuous (Theorem §9.3).
>
> **The sum of $1/n^2$.** Since the series converges to $f$ at every point, including $x = \pi$, where $\cos n\pi = (-1)^n$:
>
> $$
> \frac{\pi^2}{6} = f(\pi) = \sum_{n=1}^{\infty}\frac{(-1)^n(-1)^n}{n^2} = \sum_{n=1}^{\infty}\frac{1}{n^2} .
> $$
>
> Equivalently (the lecture's version), $x^2 = \frac{\pi^2}{3} + \sum_{n=1}^{\infty}\frac{4(-1)^n}{n^2}\cos nx$ uniformly on $[-\pi, \pi]$, and $x = \pi$ gives $\pi^2 = \frac{\pi^2}{3} + 4\sum\frac{1}{n^2}$.
>
> *Powers: Exercise 1.3.7; Source: 341 HW 2, Problem 4; 341 lecture 9.10, Example 2*

^ex-9-5
