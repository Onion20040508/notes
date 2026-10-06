---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 1
section: 14
powers: "1.5"
aliases: ["Powers 1.5"]
tags: [fourier-series-and-pdes, math341]
---
← [[§13 Uniform Convergence]] · ↑ [[· 1 Fourier Series and Integrals]] · [[§15★ Mean Error and Convergence in Mean]] →

*Powers, Section 1.5 · MAT 341 lectures 9.10, 9.12 · HW 3 · Midterm 1 · Review Sheet 1.*

Solving boundary value problems means operating on Fourier series: adding them, multiplying by constants, integrating and, above all, differentiating them term by term, since a series solution of the heat equation is checked by differentiating it twice in $x$ and once in $t$. This section gives conditions under which these operations are legitimate. Linear combinations and term-by-term integration are always allowed for sectionally continuous functions, even when the series does not converge; integration makes series converge better and produces new series and sums such as $\sum 1/n^2 = \pi^2/6$. Term-by-term differentiation is delicate: it requires the periodic extension to be continuous, and it fails, typically producing a divergent series, when the extension jumps. The theorems are not the best possible, and in applications one often operates formally and checks the result afterwards. Throughout, the period is $2\pi$ for typographical convenience; the results remain true for period $2a$, and for a function defined only on a finite interval the periodic extension must fulfill the hypotheses. We refer to a function $f$ with the series

$$
f(x) \sim a_0 + \sum_{n=1}^{\infty} a_n\cos nx + b_n\sin nx . \qquad (1)
$$

## Linearity

> [!theorem] Theorem §18.1: Constant Multiples
> The Fourier series of the function $cf(x)$ has coefficients $ca_0$, $ca_n$ and $cb_n$ ($c$ is constant).
>
> *Powers: 1.5, Theorem 1*

^thm-14-1

> [!proof]+ Proof
> A constant passes through an integral: $\frac1\pi\int_{-\pi}^{\pi}cf(x)\cos nx\,dx = c\cdot\frac1\pi\int_{-\pi}^{\pi}f(x)\cos nx\,dx = ca_n$, and in the same way for $a_0$ and $b_n$.

^pf-14-1

*Uses:* [[§9 Periodic Functions and Fourier Series#^def-9-2|Def. §9.2]]

> [!theorem] Theorem §18.2: Sums
> The Fourier coefficients of the sum $f(x) + g(x)$ are the sums of the corresponding coefficients of $f(x)$ and $g(x)$.
>
> *Powers: 1.5, Theorem 2*

^thm-14-2

> [!proof]+ Proof
> The integral of a sum is the sum of the integrals: $\frac1\pi\int_{-\pi}^{\pi}(f + g)\cos nx\,dx = a_n + a_n'$, where $a_n'$ is the coefficient of $g$, and in the same way for $a_0$ and $b_n$.

^pf-14-2

*Uses:* [[§9 Periodic Functions and Fourier Series#^def-9-2|Def. §9.2]]

These two theorems are so natural that one uses them without thinking about it (for instance in [[§12 Convergence of Fourier Series#^ex-12-4|Example §12.4]]). The theorems that follow are much more difficult to prove, but extremely important.

## Term-by-Term Integration

> [!theorem] Theorem §18.3: Term-by-Term Integration
> If $f(x)$ is periodic and sectionally continuous, then the Fourier series of $f$ may be integrated term by term:
>
> $$
> \int_a^b f(x)\,dx = \int_a^b a_0\,dx + \sum_{n=1}^{\infty}\int_a^b\big(a_n\cos nx + b_n\sin nx\big)\,dx . \qquad (2)
> $$
>
> *Powers: 1.5, Theorem 3; Source: 341 lecture 9.10, Theorem 2*

^thm-14-3

*Powers omits the proof ("much more difficult to prove"); see Remark: Why Theorems §14.3 and §10.4 Hold, an argument that is not from Powers.*

> [!remark]- Connections
> - For a uniformly convergent series of continuous functions term-by-term integration is [[§26 Differentiation and Integration of Power Series#^thm-26-3|451 Thm. §26.3]] (from [[§25 More on Uniform Convergence#^thm-25-1|451 Thm. §25.1]]). Theorem §14.3 is stronger: the Fourier series need not converge at all, let alone uniformly.
> - The lecture's sketch for sectionally smooth $f$ passes the limit through the integral with the dominated convergence theorem, [[§23 The Dominated Convergence Theorem#^thm-23-3|551 Thm. §23.3]]: the partial sums converge to $f$ except at finitely many points, and they are bounded uniformly in $N$ (a fact the sketch needs but does not prove).

> [!theorem] Theorem §14.4: Integrating Against a Second Function
> If $f(x)$ is periodic and sectionally continuous and if $g(x)$ is sectionally continuous for $a \le x \le b$, then
>
> $$
> \int_a^b f(x)g(x)\,dx = \int_a^b a_0g(x)\,dx + \sum_{n=1}^{\infty}\int_a^b\big(a_n\cos nx + b_n\sin nx\big)g(x)\,dx . \qquad (3)
> $$
>
> *Powers: 1.5, Theorem 4; Source: 341 lecture 9.10, Theorem 2*

^thm-14-4

*Powers omits the proof; see the remark below, an argument that is not from Powers.*

In Theorems §14.3 and §10.4, $f$ is only required to be sectionally continuous. It is not necessary that the Fourier series of $f$ converge at all. Nevertheless the theorems guarantee that the series on the right converges and equals the integral on the left. One important application of Theorem §14.4 is the derivation of the coefficient formulas in [[§9 Periodic Functions and Fourier Series#^prop-9-4|Proposition §9.4]]: with $g = 1$, $\cos mx$, $\sin mx$ on $[-\pi, \pi]$ it justifies exactly the term-by-term integrations made there.

> [!remark]- Remark: Why Theorems §14.3 and §10.4 Hold
> Both follow from convergence in the mean, [[§15★ Mean Error and Convergence in Mean#^thm-15-6|Theorem §15.6]] (which rests on Parseval's equality, [[§15★ Mean Error and Convergence in Mean#^thm-15-4|Theorem §15.4]], quoted from Functional Analysis). Let $S_N$ be the partial sums of (1) and suppose first that $[a, b]$ lies in one period interval $[c, c + 2\pi]$. By the [[Cauchy–Schwarz inequality]] for integrals,
>
> $$
> \Big|\int_a^b\big(f - S_N\big)g\,dx\Big| \le \Big(\int_a^b(f - S_N)^2\,dx\Big)^{1/2}\Big(\int_a^b g^2\,dx\Big)^{1/2} \le \Big(\int_c^{c + 2\pi}(f - S_N)^2\,dx\Big)^{1/2}\Big(\int_a^b g^2\,dx\Big)^{1/2} \longrightarrow 0 ,
> $$
>
> since the mean error over a period tends to zero. But $\int_a^b S_Ng$ is the $N$th partial sum of the series in (3), so the series converges to $\int_a^b fg$. A longer interval is a finite union of such pieces. Theorem §14.3 is the case $g = 1$. (For Theorem §14.3 there is also a route inside this chapter: $F(x) = \int_0^x(f - a_0)$ is periodic, continuous and sectionally smooth, so its Fourier series converges uniformly by [[§13 Uniform Convergence#^thm-13-3|Theorem §13.3]], and computing its coefficients by parts gives (2).)
>
> *Source: an argument added in these notes (convergence in the mean and the Cauchy–Schwarz inequality); not in Powers.*

^rem-14-1

> [!example] Example §18.1: Integrating the Sawtooth; Sums of 1/n² and 1/n⁴
> **The series.** The periodic function $g(x)$ with $g(x) = x$ on $0 < x < 2\pi$ has the Fourier series $g(x) \sim \pi - 2\sum_{n=1}^{\infty}\frac{\sin nx}{n}$ ([[§9 Periodic Functions and Fourier Series#^ex-9-2|Example §9.2]](b)). By Theorems §14.1 and §10.2, $f(x) = [\pi - g(x)]/2$ has the series
>
> $$
> f(x) \sim \sum_{n=1}^{\infty}\frac{\sin nx}{n} .
> $$
>
> This manipulation would be simple algebra if $\sim$ were an equality; the theorems say it is legitimate anyway.
>
> **Integrate once.** $f$ satisfies the hypotheses of Theorem §14.3, so we may integrate from $0$ to $b$, using $\int_0^b\frac{\sin nx}{n}dx = \frac{1 - \cos nb}{n^2}$:
>
> $$
> \int_0^b f(x)\,dx = \sum_{n=1}^{\infty}\frac{1 - \cos nb}{n^2} ,
> $$
>
> for any $b$. In $0 \le b \le 2\pi$, $f(x) = (\pi - x)/2$ and the left side is $\frac{\pi b}{2} - \frac{b^2}{4}$. Replacing $b$ by $x$:
>
> $$
> \frac{x(2\pi - x)}{4} = \sum_{n=1}^{\infty}\frac{1}{n^2} - \sum_{n=1}^{\infty}\frac{\cos nx}{n^2}, \qquad 0 \le x \le 2\pi . \qquad (4)
> $$
>
> Outside this interval, the periodic extension of the left side equals the series on the right. The series on the right of (4) is the Fourier series of the function on the left, that is,
>
> $$
> \frac{1}{2\pi}\int_0^{2\pi}\frac{x(2\pi - x)}{4}\,dx = \sum_{n=1}^{\infty}\frac{1}{n^2}, \qquad (5) \qquad\quad
> \frac1\pi\int_0^{2\pi}\frac{x(2\pi - x)}{4}\cos nx\,dx = \frac{-1}{n^2}, \qquad (6) \qquad\quad
> \frac1\pi\int_0^{2\pi}\frac{x(2\pi - x)}{4}\sin nx\,dx = 0 . \qquad (7)
> $$
>
> (6) and (7) can be verified directly, but Theorem §14.4 together with the orthogonality relations also guarantees them.
>
> **$\sum 1/n^2$.** (5) evaluates the series: $\int_0^{2\pi}\big(\frac{\pi x}{2} - \frac{x^2}{4}\big)dx = \pi^3 - \frac{2\pi^3}{3} = \frac{\pi^3}{3}$, so $2\pi\sum\frac{1}{n^2} = \frac{\pi^3}{3}$ and
>
> $$
> \sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6} .
> $$
>
> **Integrate again: $\sum\sin(nt)/n^3$.** Integrating (4) from $0$ to $t$ (Theorem §14.3; here the series even converges uniformly, by [[§13 Uniform Convergence#^thm-13-2|Theorem §13.2]]):
>
> $$
> \frac{\pi t^2}{4} - \frac{t^3}{12} = \frac{\pi^2}{6}t - \sum_{n=1}^{\infty}\frac{\sin nt}{n^3}, \qquad\text{so}\qquad \sum_{n=1}^{\infty}\frac{\sin nt}{n^3} = \frac{t^3}{12} - \frac{\pi t^2}{4} + \frac{\pi^2 t}{6} =: p(t), \qquad 0 \le t \le 2\pi .
> $$
>
> The convergence is uniform: $\sum 1/n^3$ converges ([[§13 Uniform Convergence#^thm-13-2|Theorem §13.2]]); or, $p(0) = 0 = p(2\pi)$ (indeed $\frac{8\pi^3}{12} - \pi^3 + \frac{\pi^3}{3} = 0$), so the periodic extension of $p$ is continuous with a sectionally continuous derivative ([[§13 Uniform Convergence#^thm-13-3|Theorem §13.3]]).
>
> **Integrate a third time: $\sum 1/n^4$.** Integrating from $0$ to $x$, with $\int_0^x\frac{\sin nt}{n^3}dt = \frac{1 - \cos nx}{n^4}$,
>
> $$
> \sum_{n=1}^{\infty}\frac{1}{n^4} - \sum_{n=1}^{\infty}\frac{\cos nx}{n^4} = \frac{x^4}{48} - \frac{\pi x^3}{12} + \frac{\pi^2x^2}{12}, \qquad 0 \le x \le 2\pi .
> $$
>
> Integrating over $0 \le x \le 2\pi$ as for (5), the cosine terms drop out and
>
> $$
> 2\pi\sum_{n=1}^{\infty}\frac{1}{n^4} = \int_0^{2\pi}\Big(\frac{x^4}{48} - \frac{\pi x^3}{12} + \frac{\pi^2x^2}{12}\Big)dx = \frac{2\pi^5}{15} - \frac{\pi^5}{3} + \frac{2\pi^5}{9} = \frac{\pi^5}{45}, \qquad \sum_{n=1}^{\infty}\frac{1}{n^4} = \frac{\pi^4}{90} .
> $$
>
> *Powers: 1.5, first Example; Exercise 1.5.1; Source: 341 lecture 9.10, Example; 341 HW 3, Problem 2*

^ex-14-1

![[m341-10-1.svg]]
*Example §10.1: the periodic function $f$ with $f(x) = (\pi - x)/2$ on $(0, 2\pi)$ (blue), with jumps of size $\pi$ at the multiples of $2\pi$, and its integral $\int_0^x f = x(2\pi - x)/4$ (red), which is continuous with corners there. Integration smooths: the coefficients improve from $1/n$ to $1/n^2$, and the series converges uniformly.*

> [!theorem] Theorem §14.5: Uniqueness of Fourier Series
> If $f(x)$ is periodic and sectionally continuous, its Fourier series is unique. That is to say, only one series can correspond to $f(x)$.
>
> We often use uniqueness this way: if two Fourier series are equal (or correspond to the same function), then the coefficients of like terms must match.
>
> *Powers: 1.5, Theorem 5*

^thm-14-5

> [!proof]+ Proof
> Powers: "a consequence of Theorem 4". Suppose $f$ corresponds to a series $A_0 + \sum(A_n\cos nx + B_n\sin nx)$ in the sense of (3), so that it may be integrated term by term against any sectionally continuous $g$ on $[-\pi, \pi]$. Take $g(x) = \cos mx$ ($m \ge 1$). By the orthogonality relations ([[§9 Periodic Functions and Fourier Series#^prop-9-3|Proposition §9.3]]) every term on the right of (3) vanishes except $A_m\int_{-\pi}^{\pi}\cos^2 mx\,dx = \pi A_m$, so $A_m = \frac1\pi\int_{-\pi}^{\pi}f(x)\cos mx\,dx = a_m$. In the same way $g = \sin mx$ gives $B_m = b_m$, and $g = 1$ gives $A_0 = a_0$. So the coefficients are determined by $f$: they can only be the Fourier coefficients (3)–(5) of [[§9 Periodic Functions and Fourier Series#^def-9-2|Definition §9.2]], and changing $f$ at finitely many points does not change them.

^pf-14-5

*Uses:* [[§14 Operations on Fourier Series#^thm-14-4|§14.4]], [[§9 Periodic Functions and Fourier Series#^prop-9-3|§9.3]], [[§9 Periodic Functions and Fourier Series#^def-9-2|Def. §9.2]], [[§9 Periodic Functions and Fourier Series#^def-9-3|Def. §9.3]]

For example, a trigonometric identity such as $\cos^2 x = \frac12 + \frac12\cos 2x$ *is* the Fourier series of $\cos^2 x$, with no integration (Powers Exercise 1.1.7).

## Term-by-Term Differentiation

The last operation is differentiation, which plays a principal role in applications.

> [!theorem] Theorem §14.6: Term-by-Term Differentiation
> If $f(x)$ is periodic, continuous and sectionally smooth, then the differentiated Fourier series of $f$ converges to $f'(x)$ at every point $x$ where $f''(x)$ exists:
>
> $$
> f'(x) = \sum_{n=1}^{\infty}\big(-na_n\sin nx + nb_n\cos nx\big) . \qquad (8)
> $$
>
> In fact the right side is the Fourier series of $f'$. (For period $2a$, the coefficients are $\frac{n\pi}{a}b_n$ for $\cos\frac{n\pi x}{a}$ and $-\frac{n\pi}{a}a_n$ for $\sin\frac{n\pi x}{a}$.)
>
> *Powers: 1.5, Theorem 6; Source: 341 lecture 9.12, Theorem 3*

^thm-14-6

> [!proof]+ Proof
> Powers omits the proof; part (I) is the lecture's, and part (II) is the lecture's reference to Section 1.7.
>
> **(I) The Fourier series of $f'$ is the differentiated series.** $f'$ exists except at finitely many points per period and is sectionally continuous, so it has Fourier coefficients $\hat a_0$, $\hat a_n$, $\hat b_n$. Let $-\pi = x_0 < x_1 < \cdots < x_k = \pi$ include the points where $f'$ fails to exist; on each $[x_{j-1}, x_j]$, $f$ is continuously differentiable (with one-sided derivatives at the ends), and we may integrate by parts:
>
> $$
> \hat a_n = \frac1\pi\int_{-\pi}^{\pi}f'(x)\cos nx\,dx = \frac1\pi\sum_{j=1}^{k}\Big[f(x)\cos nx\Big]_{x_{j-1}}^{x_j} + \frac n\pi\int_{-\pi}^{\pi}f(x)\sin nx\,dx .
> $$
>
> Because $f$ is *continuous*, the boundary terms telescope to $\frac1\pi\big[f(\pi)\cos n\pi - f(-\pi)\cos(-n\pi)\big]$, which is $0$ because $f(\pi) = f(-\pi)$ by periodicity. Hence $\hat a_n = nb_n$. In the same way
>
> $$
> \hat b_n = \frac1\pi\int_{-\pi}^{\pi}f'(x)\sin nx\,dx = \frac1\pi\Big[f(x)\sin nx\Big]_{-\pi}^{\pi} - \frac n\pi\int_{-\pi}^{\pi}f(x)\cos nx\,dx = -na_n, \qquad \hat a_0 = \frac{1}{2\pi}\big[f(\pi) - f(-\pi)\big] = 0 .
> $$
>
> So $f'(x) \sim \sum_{n=1}^{\infty}(nb_n\cos nx - na_n\sin nx)$, the term-by-term derivative of (1).
>
> **(II) Convergence.** If $f'$ is itself sectionally smooth, [[§12 Convergence of Fourier Series#^thm-12-1|Theorem §12.1]] applied to $f'$ shows that the series (8) converges at every $x$ to $\frac12\big(f'(x+) + f'(x-)\big)$. Where $f''(x)$ exists, $f'$ is differentiable at $x$, hence continuous there, and the sum is $f'(x)$. (Under Powers' weaker hypothesis, that $f$ is only sectionally smooth, convergence where $f''(x)$ exists comes from the local form of the convergence proof of [[§16★ Proof of Convergence#^thm-16-4|Theorem §16.4]], applied to $f'$ at the point $x$.)

^pf-14-6

*Uses:* [[§12 Convergence of Fourier Series#^thm-12-1|§12.1]], [[§16★ Proof of Convergence#^thm-16-4|§16.4]], [[§12 Convergence of Fourier Series#^def-12-4|Def. §12.4]], [[§9 Periodic Functions and Fourier Series#^def-9-2|Def. §9.2]], [[§9 Periodic Functions and Fourier Series#^def-9-3|Def. §9.3]], [[§34 Fundamental Theorem of Calculus#^thm-34-3|451 Thm. §34.3]] (integration by parts)

> [!remark]- Connections
> - For power series, term-by-term differentiation always works inside the interval of convergence, [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]]; for Fourier series it needs the continuity of the periodic extension, because differentiation multiplies the $n$th coefficient by $n$ and so makes convergence worse.

The hypotheses on $f$ itself imply ([[§13 Uniform Convergence#^thm-13-3|Theorem §13.3]]) that the Fourier series of $f$ converges uniformly. The lecture adds that at a corner of $f$, where $f'$ jumps and $f''$ does not exist, the differentiated series still converges, to $\frac12(f'(x+) + f'(x-))$, when $f'$ is sectionally smooth.

> [!remark] Remark: When the Periodic Extension Jumps
> If $f$ (or its periodic extension) fails to be continuous, it is certain that the differentiated series of $f$ will fail to converge, at some points at least. In the proof of Theorem §14.6 the boundary terms then no longer cancel: a jump of $f$ contributes a term that does not tend to zero. For example, $f(x) = (\pi - x)/2$ on $0 < x < 2\pi$ has $f(x) \sim \sum_{n=1}^{\infty}\frac{\sin nx}{n}$ ([[§14 Operations on Fourier Series#^ex-14-1|Example §14.1]]) and $f'(x) = -\frac12$ except at the jumps; but the differentiated series $\sum_{n=1}^{\infty}\cos nx$ diverges at every $x$, since its terms do not tend to zero.

^rem-14-2

> [!example] Example §18.2: Differentiating the Triangle Wave
> Let $f$ be periodic with period $2\pi$ and $f(x) = |x|$ for $-\pi < x < \pi$. This function is continuous and sectionally smooth, and equal to its Fourier series ([[§13 Uniform Convergence#^ex-13-2|Example §13.2]]):
>
> $$
> f(x) = \frac\pi2 - \frac4\pi\Big(\cos x + \frac{\cos 3x}{9} + \frac{\cos 5x}{25} + \cdots\Big) .
> $$
>
> By Theorem §14.6 the differentiated series
>
> $$
> \frac4\pi\Big(\sin x + \frac{\sin 3x}{3} + \frac{\sin 5x}{5} + \cdots\Big)
> $$
>
> converges to $f'(x)$ at every point $x$ where $f''(x)$ exists. The derivative of the triangle wave is the square wave
>
> $$
> f'(x) = \begin{cases} 1, & 0 < x < \pi, \\ -1, & -\pi < x < 0 . \end{cases} \qquad (9)
> $$
>
> Moreover the sine series above is the Fourier series of the square wave $f'$ (indeed $\frac2\pi\int_0^\pi\sin nx\,dx = \frac{2}{n\pi}(1 - (-1)^n)$, which is $\frac{4}{n\pi}$ for odd $n$ and $0$ for even $n$), and it converges to the values given by (9) except at the points where $f'$ has a jump, the multiples of $\pi$, where it converges to $0$. These are precisely the points where $f''(x)$ does not exist.
>
> *Powers: 1.5, second Example; Source: 341 lecture 9.12, Example 1*

^ex-14-2

> [!example] Example §18.3: Odd and Even Extensions of x²
> Let $f(x) = x^2$ for $0 < x < \pi$. **(I)** Let $f$ be odd and periodic with period $2\pi$; **(II)** let $f$ be even and periodic with period $2\pi$. In each case (a) find the Fourier series, (b) differentiate it term by term, (c) find the Fourier series of $f'$, (d) decide whether (b) and (c) coincide, by the differentiation theorem.
>
> **(I) Odd extension.** (a) $a_0 = a_n = 0$ and, integrating by parts twice,
>
> $$
> b_n = \frac2\pi\int_0^\pi x^2\sin nx\,dx = -\frac{2}{n\pi}\Big[x^2\cos nx\Big]_0^\pi + \frac{4}{n^3\pi}\Big[\cos nx\Big]_0^\pi = \frac{2\pi(-1)^{n - 1}}{n} + \frac{4\big[(-1)^n - 1\big]}{n^3\pi} ,
> $$
>
> so $f(x) \sim \sum_{n=1}^{\infty}\Big[\frac{2\pi(-1)^{n - 1}}{n} + \frac{4[(-1)^n - 1]}{n^3\pi}\Big]\sin nx$.
>
> (b) The term-by-term derivative is $\sum_{n=1}^{\infty}\Big[2\pi(-1)^{n - 1} + \frac{4[(-1)^n - 1]}{\pi n^2}\Big]\cos nx$.
>
> (c) $f'(x) = 2x$ on $0 < x < \pi$ and $-2x$ on $-\pi < x < 0$, that is, $f' = 2|x|$, even: $b_n = 0$,
>
> $$
> a_0 = \frac1\pi\int_0^\pi 2x\,dx = \pi, \qquad a_n = \frac2\pi\int_0^\pi 2x\cos nx\,dx = \frac{4}{n^2\pi}\Big[\cos nx\Big]_0^\pi = \frac{4}{n^2\pi}\big[(-1)^n - 1\big], \qquad f'(x) \sim \pi + \sum_{n=1}^{\infty}\frac{4[(-1)^n - 1]}{n^2\pi}\cos nx .
> $$
>
> (d) No. The series in (b) lacks the constant $\pi$ and has the extra terms $2\pi(-1)^{n - 1}\cos nx$, which do not tend to zero, so it diverges. The reason: the odd periodic extension of $x^2$ is not continuous, it jumps from $\pi^2$ to $-\pi^2$ at $x = \pi$, so Theorem §14.6 does not apply. (In the proof of (8) the boundary term is now $\frac1\pi\big[f(\pi-) - f(-\pi+)\big]\cos n\pi = 2\pi(-1)^n$, and indeed $\hat a_n = nb_n + 2\pi(-1)^n$.)
>
> **(II) Even extension.** (a) $f(x) = x^2$ on $-\pi < x < \pi$: $b_n = 0$, $a_0 = \frac1\pi\int_0^\pi x^2\,dx = \frac{\pi^2}{3}$, $a_n = \frac2\pi\int_0^\pi x^2\cos nx\,dx = \frac{4(-1)^n}{n^2}$, so $f(x) \sim \frac{\pi^2}{3} + \sum_{n=1}^{\infty}\frac{4(-1)^n}{n^2}\cos nx$.
>
> (b) The term-by-term derivative is $\sum_{n=1}^{\infty}\frac{4(-1)^{n - 1}}{n}\sin nx$.
>
> (c) $f'(x) = 2x$ on $-\pi < x < \pi$ (undefined at $x = \pi + 2k\pi$), odd: $b_n = \frac2\pi\int_0^\pi 2x\sin nx\,dx = \frac4\pi\cdot\frac{\pi(-1)^{n + 1}}{n} = \frac{4(-1)^{n - 1}}{n}$, so $f'(x) \sim \sum_{n=1}^{\infty}\frac{4(-1)^{n - 1}}{n}\sin nx$.
>
> (d) Yes. The even periodic extension is continuous ($f(\pi-) = \pi^2 = f(-\pi+)$) and sectionally smooth, so by Theorem §14.6 the Fourier series of $f'$ is the term-by-term derivative of the Fourier series of $f$.
>
> *Source: 341 HW 3, Problem 1; 341 Review Sheet 1, Problem 6*

^ex-14-3

> [!example] Example §18.4: A Discontinuous Periodic Extension (Midterm)
> A function is given on $-1 < x < 1$ by $f(x) = x$ on $0 < x \le 1$ and $f(x) = 1$ on $-1 < x \le 0$. Let $\bar f$ be its periodic extension. **(a)** Sketch $\bar f$ for $-3 < x < 3$. **(b)** Find the discontinuities of $\bar f$ on one period $-1 - \varepsilon < x < 1$ and their types. **(c)** Find the Fourier series of $\bar f$. **(d)** Compute $\bar f'$ on $-1 \le x < 1$. **(e)** Find the Fourier series of $\bar f'$. **(f)** Differentiate the series of (c) term by term; is it the series of (e)?
>
> **(a)** On each period: level $1$ over $(-1, 0]$, then the segment from $(0, 0)$ to $(1, 1)$. So the graph drops from $1$ to $0$ at the even integers and continues at level $1$ after each odd integer.
>
> **(b)** Only $x = 0$: $\bar f(0-) = 1$ and $\bar f(0+) = 0$ differ, a jump discontinuity. At $x = -1$, $\bar f(-1-) = f(1-) = 1$ and $\bar f(-1+) = 1 = \bar f(-1)$, so $\bar f$ is continuous there.
>
> **(c)** $a = 1$:
>
> $$
> a_0 = \frac12\int_{-1}^{0}1\,dx + \frac12\int_0^1 x\,dx = \frac12 + \frac14 = \frac34, \qquad
> a_n = \int_{-1}^{0}\cos n\pi x\,dx + \int_0^1 x\cos n\pi x\,dx = 0 + \frac{(-1)^n - 1}{n^2\pi^2},
> $$
>
> $$
> b_n = \int_{-1}^{0}\sin n\pi x\,dx + \int_0^1 x\sin n\pi x\,dx = \frac{(-1)^n - 1}{n\pi} + \frac{(-1)^{n + 1}}{n\pi} = -\frac{1}{n\pi},
> $$
>
> so $\bar f(x) \sim \frac34 + \sum_{n=1}^{\infty}\frac{(-1)^n - 1}{n^2\pi^2}\cos n\pi x - \sum_{n=1}^{\infty}\frac{1}{n\pi}\sin n\pi x$.
>
> **(d)** $\bar f'(x) = 0$ for $-1 < x < 0$, $1$ for $0 < x < 1$; undefined at $x = 0$ (jump) and at $x = -1$ (a corner: slope $1$ on the left, $0$ on the right).
>
> **(e)** $a_0 = \frac12\int_0^1 1\,dx = \frac12$, $a_n = \int_0^1\cos n\pi x\,dx = 0$, $b_n = \int_0^1\sin n\pi x\,dx = \frac{1 - (-1)^n}{n\pi}$, so $\bar f'(x) \sim \frac12 + \sum_{n=1}^{\infty}\frac{1 - (-1)^n}{n\pi}\sin n\pi x$.
>
> **(f)** Differentiating (c) term by term: $\frac{d}{dx}\frac{(-1)^n - 1}{n^2\pi^2}\cos n\pi x = \frac{1 - (-1)^n}{n\pi}\sin n\pi x$ and $\frac{d}{dx}\big(-\frac{1}{n\pi}\sin n\pi x\big) = -\cos n\pi x$, giving
>
> $$
> \sum_{n=1}^{\infty}\frac{1 - (-1)^n}{n\pi}\sin n\pi x - \sum_{n=1}^{\infty}\cos n\pi x .
> $$
>
> This is not the series of (e): the constant $\frac12$ is missing and the divergent $-\sum\cos n\pi x$ appears. The reason: $\bar f$ is not continuous on $\mathbb{R}$ (it jumps at $0$), so the hypotheses of Theorem §14.6 are not satisfied.
>
> *Source: 341 Midterm 1, Q1*

^ex-14-4

Later on it will frequently happen that a function is known only through its Fourier series. Then properties of the function must be obtained by examining its coefficients.

> [!theorem] Theorem §14.7: Smoothness from the Coefficients
> If $f$ is periodic, with Fourier coefficients $a_n$, $b_n$, and if the series
>
> $$
> \sum_{n=1}^{\infty}\big(|n^ka_n| + |n^kb_n|\big)
> $$
>
> converges for some integer $k \ge 1$, then $f$ has continuous derivatives $f', \ldots, f^{(k)}$ whose Fourier series are the differentiated series of $f$.
>
> *Powers: 1.5, Theorem 7; Source: 341 lecture 9.12, Theorem 4*

^thm-14-7

*Powers omits the proof; see Remark: Why Theorem §14.7 Holds, an argument that is not from Powers.*

> [!remark]- Remark: Why Theorem §14.7 Holds
> For $j \le k$, the $j$-times differentiated series has terms bounded by $n^j(|a_n| + |b_n|) \le n^k(|a_n| + |b_n|)$, so by the M-test ([[§13 Uniform Convergence#^thm-13-2|Theorem §13.2]]) it converges uniformly to a continuous function $g_j$; for $j = 0$ the limit is $f$ (at least after correcting $f$ at finitely many points, by [[§13 Uniform Convergence#^thm-13-1|Theorem §13.1]]). Integrating the uniformly convergent series for $g_1$ term by term from $0$ to $x$ ([[§26 Differentiation and Integration of Power Series#^thm-26-3|451 Thm. §26.3]]) gives back the series of $f$, minus its value at $0$: $\int_0^x g_1 = f(x) - f(0)$. By the [[Fundamental Theorem of Calculus|fundamental theorem of calculus]] $f' = g_1$, continuous. Repeat for $g_2, \ldots, g_k$. Finally, a uniformly convergent trigonometric series is the Fourier series of its sum (multiply by $\cos mx$ or $\sin mx$, integrate term by term and use the orthogonality relations), so the differentiated series are the Fourier series of $f', \ldots, f^{(k)}$. This is the argument of [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]](2) for power series.
>
> *Source: an argument added in these notes (the M-test and term-by-term integration of uniformly convergent series); not in Powers.*

^rem-14-3

The lecture adds a simple bound that makes Theorem §14.7 easy to apply.

> [!theorem] Proposition §14.8: Bounded Coefficients
> If $f$ is periodic with period $2a$ and sectionally continuous, then its Fourier coefficients are bounded:
>
> $$
> |a_0|, \ |a_n|, \ |b_n| \le \frac1a\int_{-a}^{a}|f(x)|\,dx .
> $$
>
> Moreover $a_n, b_n \to 0$ as $n \to \infty$ ([[§15★ Mean Error and Convergence in Mean#^cor-15-5|Corollary §15.5]]).
>
> *Source: 341 lecture 9.12*

^prop-14-8

> [!proof]+ Proof
> $|\cos\frac{n\pi x}{a}| \le 1$ and $|\sin\frac{n\pi x}{a}| \le 1$, so $|a_n| \le \frac1a\int_{-a}^{a}|f|$ and $|b_n| \le \frac1a\int_{-a}^{a}|f|$, and $|a_0| \le \frac{1}{2a}\int_{-a}^{a}|f| \le \frac1a\int_{-a}^{a}|f|$. The integral is finite because $f$ is bounded on a period.

^pf-14-8

*Uses:* [[§10 Arbitrary Period and Half-Range Expansions#^prop-10-1|§10.1]], [[§12 Convergence of Fourier Series#^def-12-3|Def. §12.3]]

> [!example] Example §18.5: Rapidly Decaying Coefficients; a Heat Series
> **(a)** Consider the function defined by the series
>
> $$
> f(x) = \sum_{n=1}^{\infty}e^{-n\alpha}\cos nx ,
> $$
>
> where $\alpha$ is a positive parameter. Here $a_0 = 0$, $a_n = e^{-n\alpha}$, $b_n = 0$. The series $\sum n^ke^{-n\alpha}$ converges for any $k$ (by the [[Integral Test|integral test]]; or by the [[Ratio Test|ratio test]], since $\frac{(n + 1)^k}{n^k}e^{-\alpha} \to e^{-\alpha} < 1$). By Theorem §14.7, $f$ has derivatives of all orders, and
>
> $$
> f'(x) = \sum_{n=1}^{\infty} -ne^{-n\alpha}\sin nx, \qquad f''(x) = \sum_{n=1}^{\infty} -n^2e^{-n\alpha}\cos nx .
> $$
>
> **(b)** Let $f$ be odd, periodic and sectionally smooth, $f(x) \sim \sum_{n=1}^{\infty}b_n\sin nx$, and define
>
> $$
> u(x, t) = \sum_{n=1}^{\infty}b_ne^{-n^2t}\sin nx .
> $$
>
> Show: (i) $\frac{\partial^2u}{\partial x^2} = \sum_{n=1}^{\infty}-n^2b_ne^{-n^2t}\sin nx$ for $t > 0$; (ii) $u(0, t) = 0$, $u(\pi, t) = 0$ for $t > 0$; (iii) $u(x, 0) = \frac12\big(f(x+) + f(x-)\big)$; (iv) $\frac{\partial u}{\partial t} = \sum_{n=1}^{\infty}-n^2b_ne^{-n^2t}\sin nx = \frac{\partial^2u}{\partial x^2}$ for $t > 0$.
>
> (i) By Proposition §14.8, $|b_n| \le M$ for some $M$. Fix $t > 0$; for fixed $t$, $u$ is a Fourier sine series in $x$ with coefficients $b_ne^{-n^2t}$, and
>
> $$
> \sum_{n=1}^{\infty}n^2\big|b_ne^{-n^2t}\big| \le M\sum_{n=1}^{\infty}n^2e^{-n^2t} < \infty
> $$
>
> (ratio test: $\frac{(n + 1)^2}{n^2}e^{-(2n + 1)t} \to 0$). By Theorem §14.7 with $k = 2$, $u$ has continuous $x$-derivatives up to order $2$, given by term-by-term differentiation; this is (i).
>
> (ii) For $t > 0$ the series converges (uniformly, by the M-test), and $\sin 0 = \sin n\pi = 0$ term by term.
>
> (iii) At $t = 0$, $u(x, 0) = \sum b_n\sin nx$ is the Fourier series of $f$, which converges to $\frac12(f(x+) + f(x-))$ by [[§12 Convergence of Fourier Series#^thm-12-1|Theorem §12.1]].
>
> (iv) Fix $t_0 > 0$. For $t \ge t_0$ and all $x$, $\big|-n^2b_ne^{-n^2t}\sin nx\big| \le Mn^2e^{-n^2t_0}$, a convergent series of constants, so the $t$-differentiated series converges uniformly on $t \ge t_0$. The argument of Remark: Why Theorem §14.7 Holds, now in the variable $t$, shows that it is $\partial u/\partial t$. Comparing with (i), $u_t = u_{xx}$ for $t > 0$.
>
> So $u$ solves the heat equation $u_t = u_{xx}$ on $0 < x < \pi$ with $u = 0$ at both ends and initial values $f$: this is the solution of [[§25 Example꞉ Fixed End Temperatures#^thm-25-5|Theorem §25.5]], and the verification is the model for all series solutions.
>
> *Powers: 1.5, third Example; Exercise 1.5.9; Source: 341 lecture 9.12, Example 4; 341 HW 3, Problem 3*

^ex-14-5
