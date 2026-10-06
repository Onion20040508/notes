---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 1
section: "15★"
powers: "1.6"
aliases: ["Powers 1.6"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§14 Operations on Fourier Series]] · ↑ [[· 1 Fourier Series and Integrals]] · [[§16★ Proof of Convergence]] →

*Powers, Section 1.6 · MAT 341 lectures 9.10, 9.12 (remarks).*
★ *Beyond MAT 341: the course did not cover this section beyond remarks in lectures 9.10 and 9.12; it is included from Powers.*

In practice one always computes with a finite piece of a Fourier series. This section measures how well a finite trigonometric sum approximates $f$ by the mean (integral) square error, and shows that among all trigonometric sums of order $N$ the truncated Fourier series is the best one. Since the error cannot be negative, the coefficients satisfy Bessel's inequality, and in the limit the inequality becomes Parseval's equality: the "energy" $\int f^2$ is the sum of the energies of the harmonics. Consequences are that the coefficients tend to zero and that the Fourier series converges to $f$ in the mean, a third kind of convergence beside the pointwise ([[§12 Convergence of Fourier Series|§12]]) and uniform ([[§13 Uniform Convergence|§13]]) ones, which needs only that $\int f^2$ be finite. This is exactly the Hilbert-space picture of Functional Analysis: the truncated series is an orthogonal projection, and Parseval's equality expresses that the trigonometric functions form a complete orthogonal set.

## A Useful Formula

Suppose $f$ is a function defined in the interval $-a < x < a$ for which $\int_{-a}^{a}(f(x))^2\,dx$ is a finite number. Let

$$
f(x) \sim a_0 + \sum_{n=1}^{\infty} a_n\cos\Big(\frac{n\pi x}{a}\Big) + b_n\sin\Big(\frac{n\pi x}{a}\Big)
$$

and let $g(x)$ have a finite Fourier series

$$
g(x) = A_0 + \sum_{n=1}^{N} A_n\cos\Big(\frac{n\pi x}{a}\Big) + B_n\sin\Big(\frac{n\pi x}{a}\Big) .
$$

> [!theorem] Proposition §15.1: Integral of a Product
> With $f$ and $g$ as above,
>
> $$
> \frac1a\int_{-a}^{a}f(x)g(x)\,dx = 2a_0A_0 + \sum_{n=1}^{N}\big(a_nA_n + b_nB_n\big) . \qquad (1)
> $$
>
> *Powers: 1.6, Equation (1)*

^prop-15-1

> [!proof]+ Proof
> The sum defining $g$ is finite, so it can be multiplied by $f$ and integrated term by term with no convergence question:
>
> $$
> \int_{-a}^{a}f(x)g(x)\,dx = A_0\int_{-a}^{a}f(x)\,dx + \sum_{n=1}^{N}A_n\int_{-a}^{a}f(x)\cos\Big(\frac{n\pi x}{a}\Big)dx + \sum_{n=1}^{N}B_n\int_{-a}^{a}f(x)\sin\Big(\frac{n\pi x}{a}\Big)dx .
> $$
>
> The integrals are multiples of the Fourier coefficients of $f$ ([[§10 Arbitrary Period and Half-Range Expansions#^prop-10-1|Proposition §10.1]]): $\int_{-a}^{a}f = 2aa_0$, $\int_{-a}^{a}f\cos\frac{n\pi x}{a} = aa_n$, $\int_{-a}^{a}f\sin\frac{n\pi x}{a} = ab_n$. Dividing by $a$ gives (1). (The integrals exist: $|f| \le \frac12(1 + f^2)$, so $\int|f| < \infty$ when $\int f^2 < \infty$.)

^pf-15-1

*Uses:* [[§10 Arbitrary Period and Half-Range Expansions#^prop-10-1|§10.1]]

## Mean Error

Now suppose we wish to approximate $f(x)$ by a *finite* Fourier series. The difficulty is deciding what "approximate" means. Of the many ways to measure approximation, the easiest to use is the following.

> [!definition] Definition §15.1: Mean Square Error
> For $f$ as above and a finite Fourier series $g$ containing terms up to and including $\cos(N\pi x/a)$ and $\sin(N\pi x/a)$, the **mean (square) error** of the approximation of $f$ by $g$ is
>
> $$
> E_N = \int_{-a}^{a}\big(f(x) - g(x)\big)^2\,dx . \qquad (2)
> $$
>
> Clearly $E_N$ can never be negative, and if $f$ and $g$ are "close", $E_N$ is small.
>
> *Powers: 1.6, Equation (2)*

^def-15-1

The problem is to choose the coefficients of $g$ so as to minimize $E_N$, with $N$ fixed. Expanding the integrand,

$$
E_N = \int_{-a}^{a}f^2(x)\,dx - 2\int_{-a}^{a}f(x)g(x)\,dx + \int_{-a}^{a}g^2(x)\,dx . \qquad (3)
$$

The first integral has nothing to do with $g$; the other two depend on the choice of $g$. The middle one is given by (1), and the last one by (1) with $f$ replaced by $g$ (whose Fourier coefficients are its own $A_0$, $A_n$, $B_n$):

$$
\int_{-a}^{a}g^2(x)\,dx = a\Big[2A_0^2 + \sum_{n=1}^{N}\big(A_n^2 + B_n^2\big)\Big] . \qquad (4)
$$

So $E_N$ is a function of the $2N + 1$ variables $A_0$, $A_n$, $B_n$:

$$
E_N = \int_{-a}^{a}f^2(x)\,dx - 2a\Big[2A_0a_0 + \sum_{n=1}^{N}\big(A_na_n + B_nb_n\big)\Big] + a\Big[2A_0^2 + \sum_{n=1}^{N}\big(A_n^2 + B_n^2\big)\Big] . \qquad (5)
$$

> [!theorem] Theorem §15.2: The Truncated Fourier Series Is the Best Approximation
> Among all finite series $g(x) = A_0 + \sum_{n=1}^{N}A_n\cos(n\pi x/a) + B_n\sin(n\pi x/a)$, the mean error $E_N$ is smallest for the **truncated Fourier series** of $f$,
>
> $$
> g(x) = a_0 + \sum_{n=1}^{N}a_n\cos\Big(\frac{n\pi x}{a}\Big) + b_n\sin\Big(\frac{n\pi x}{a}\Big) ,
> $$
>
> and the minimum value is
>
> $$
> \min(E_N) = \int_{-a}^{a}f^2(x)\,dx - a\Big[2a_0^2 + \sum_{n=1}^{N}\big(a_n^2 + b_n^2\big)\Big] . \qquad (6)
> $$
>
> *Powers: 1.6 (text), Equation (6); Summary, item 1*

^thm-15-2

> [!proof]+ Proof
> **Powers' route.** $E_N$ takes its minimum value where all of its partial derivatives with respect to the variables are zero. From (5),
>
> $$
> \frac{\partial E_N}{\partial A_0} = -4aa_0 + 4aA_0 = 0, \qquad \frac{\partial E_N}{\partial A_n} = -2aa_n + 2aA_n = 0, \qquad \frac{\partial E_N}{\partial B_n} = -2ab_n + 2aB_n = 0 .
> $$
>
> These equations require $A_0 = a_0$, $A_n = a_n$, $B_n = b_n$.
>
> **Why this is a minimum, and the value** (Powers: "after some algebra"; the question of minimum versus maximum is Exercise 1.6.4). Complete the squares in (5): since $2A_0^2 - 4A_0a_0 = 2(A_0 - a_0)^2 - 2a_0^2$ and $A_n^2 - 2A_na_n = (A_n - a_n)^2 - a_n^2$ (likewise for $B_n$),
>
> $$
> E_N = \int_{-a}^{a}f^2\,dx - a\Big[2a_0^2 + \sum_{n=1}^{N}\big(a_n^2 + b_n^2\big)\Big] + a\Big[2(A_0 - a_0)^2 + \sum_{n=1}^{N}\big((A_n - a_n)^2 + (B_n - b_n)^2\big)\Big] .
> $$
>
> The last bracket is $\ge 0$ and equals $0$ exactly when $A_0 = a_0$, $A_n = a_n$, $B_n = b_n$. So the critical point found above is the unique minimum (not a maximum: $E_N$ grows without bound as any coefficient does), and the minimum value is (6).

^pf-15-2

*Uses:* [[§15★ Mean Error and Convergence in Mean#^prop-15-1|§15.1]], [[§15★ Mean Error and Convergence in Mean#^def-15-1|Def. §15.1]]

> [!remark]- Connections
> - The truncated Fourier series is the orthogonal projection of $f$ onto the span of $1, \cos\frac{n\pi x}{a}, \sin\frac{n\pi x}{a}$ ($n \le N$), and the projection is the closest point of a subspace: [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-61|LADR 6.61]], [[§56 Inner Product Spaces#^thm-56-2|235 Thm. §56.2]](3). Lay's "$n$th-order Fourier approximation" and "mean square error" are this $g$ and $\sqrt{E_N}$, [[§57 Applications of Inner Product Spaces#^def-57-4|235 Def. §57.4]], [[§57 Applications of Inner Product Spaces#^def-57-5|235 Def. §57.5]]. The completed square in the proof is Pythagoras: $\|f - g\|^2 = \|f - \operatorname{proj}f\|^2 + \|\operatorname{proj}f - g\|^2$.

## Bessel's Inequality and Parseval's Equality

> [!theorem] Theorem §15.3: Bessel's Inequality
> If $\int_{-a}^{a}f^2(x)\,dx$ is finite, then for every $N$
>
> $$
> \frac1a\int_{-a}^{a}f^2(x)\,dx \ge 2a_0^2 + \sum_{n=1}^{N}\big(a_n^2 + b_n^2\big) , \qquad (7)
> $$
>
> and therefore also in the limit: $\frac1a\int_{-a}^{a}f^2 \ge 2a_0^2 + \sum_{n=1}^{\infty}(a_n^2 + b_n^2)$, the series converging.
>
> *Powers: 1.6, Equation (7)*

^thm-15-3

> [!proof]+ Proof
> Even the minimum error (6) is greater than or equal to zero, since $E_N \ge 0$ for every $g$. Dividing (6) by $a$ gives (7). The partial sums $2a_0^2 + \sum_{n=1}^{N}(a_n^2 + b_n^2)$ increase with $N$ and are bounded by $\frac1a\int f^2$, so the series converges and its sum obeys the same bound.

^pf-15-3

*Uses:* [[§15★ Mean Error and Convergence in Mean#^thm-15-2|§15.2]]

> [!remark]- Connections
> - [[§27 Orthonormal Sets and Bases#^lem-27-2|556 Lem. §27.2]] (finite Bessel inequality, with the same Pythagoras picture) and [[§27 Orthonormal Sets and Bases#^thm-27-5|556 Thm. §27.5]] (Bessel's inequality for any orthonormal set in an inner product space); in finite dimensions, [[§21 Orthonormal Bases#^ladr-6-26|LADR 6.26]]. Here the orthonormal set is $\frac{1}{\sqrt{2a}}, \frac{1}{\sqrt a}\cos\frac{n\pi x}{a}, \frac{1}{\sqrt a}\sin\frac{n\pi x}{a}$, and the coefficients of $f$ along it are $\sqrt{2a}\,a_0$, $\sqrt a\,a_n$, $\sqrt a\,b_n$, which turns (7) into $\sum|(f, e_k)|^2 \le \|f\|^2$.

The actual fact is that, in the limit, the inequality becomes an equality.

> [!theorem] Theorem §15.4: Parseval's Equality
> If $\int_{-a}^{a}f^2(x)\,dx$ is finite, then
>
> $$
> \frac1a\int_{-a}^{a}f^2(x)\,dx = 2a_0^2 + \sum_{n=1}^{\infty}\big(a_n^2 + b_n^2\big) . \qquad (8)
> $$
>
> *Powers: 1.6, Equation (8); Summary, item 2*

^thm-15-4

*Powers omits the proof; see [[§27 Orthonormal Sets and Bases#^thm-27-8|556 Thm. §27.8]] ((1) ⇔ (3): Parseval's equality holds for every vector exactly when the orthonormal set is complete), applied to the trigonometric system, which is complete by [[§27 Orthonormal Sets and Bases#^thm-27-11|556 Thm. §27.11]] (whose completeness step is itself quoted there, via Fejér's theorem).*

> [!remark]- Connections
> - In complex form, $\int_0^{2\pi}|f|^2 = \sum_n|c_n|^2$: [[§27 Orthonormal Sets and Bases#^rem-27-9|556 Remark: Fourier Series]]. Lay states the consequence for continuous $f$ (convergence in the mean) without proof, [[§57 Applications of Inner Product Spaces#^thm-57-4|235 Thm. §57.4]].

> [!theorem] Corollary §15.5: The Coefficients Tend to Zero
> If $\int_{-a}^{a}f^2(x)\,dx$ is finite, the two series $\sum a_n^2$ and $\sum b_n^2$ converge, and therefore
>
> $$
> a_n = \frac1a\int_{-a}^{a}f(x)\cos\Big(\frac{n\pi x}{a}\Big)dx \to 0, \qquad b_n = \frac1a\int_{-a}^{a}f(x)\sin\Big(\frac{n\pi x}{a}\Big)dx \to 0 \qquad\text{as } n \to \infty .
> $$
>
> *Powers: 1.6 (text); Summary, item 3*

^cor-15-5

> [!proof]+ Proof
> By Bessel's inequality (Theorem §15.3) the series of nonnegative terms $\sum(a_n^2 + b_n^2)$ converges; so do $\sum a_n^2$ and $\sum b_n^2$, whose terms are smaller. The terms of a convergent series tend to zero, so $a_n^2 \to 0$ and $b_n^2 \to 0$.

^pf-15-5

*Uses:* [[§15★ Mean Error and Convergence in Mean#^thm-15-3|§15.3]], [[§82 Series#^thm-82-4|Calc Thm. §82.4]] (terms of a convergent series tend to zero)

This is Lemma 3 of Powers 1.7, used in the proof of the convergence theorem, [[§16★ Proof of Convergence#^lem-16-3|Lemma §16.3]]; every sectionally continuous function has $\int f^2$ finite. Properties (8) and Corollary §15.5 are very useful for checking computed values of Fourier coefficients: coefficients that do not tend to zero, or whose squares do not add up to $\frac1a\int f^2$, are wrong.

> [!definition] Definition §15.2: Convergence in the Mean
> A series of functions **converges to $f$ in the mean** on $-a < x < a$ if the mean square error $\int_{-a}^{a}(f - S_N)^2\,dx$ between $f$ and its partial sums $S_N$ tends to zero as $N \to \infty$.
>
> *Powers: 1.6 (text)*

^def-15-2

> [!theorem] Theorem §15.6: Convergence in the Mean
> If $\int_{-a}^{a}f^2(x)\,dx$ is finite, the minimum error is
>
> $$
> \min(E_N) = a\sum_{n=N+1}^{\infty}\big(a_n^2 + b_n^2\big) ,
> $$
>
> which decreases steadily to zero as $N$ increases. That is, the Fourier series of $f$ converges to $f$ in the mean.
>
> *Powers: 1.6 (text); Summary, item 4*

^thm-15-6

> [!proof]+ Proof
> Substituting Parseval's equality (8), $\int_{-a}^{a}f^2 = a\big[2a_0^2 + \sum_{n=1}^{\infty}(a_n^2 + b_n^2)\big]$, into (6) leaves $\min(E_N) = a\sum_{n=N+1}^{\infty}(a_n^2 + b_n^2)$, the tail of a convergent series of nonnegative terms. It does not increase with $N$ and tends to zero. Since $\min(E_N)$ is by (2) the mean square deviation between $f$ and its truncated Fourier series $S_N$, this is Definition §15.2.

^pf-15-6

*Uses:* [[§15★ Mean Error and Convergence in Mean#^thm-15-2|§15.2]], [[§15★ Mean Error and Convergence in Mean#^thm-15-4|§15.4]], [[§15★ Mean Error and Convergence in Mean#^def-15-2|Def. §15.2]]

> [!remark]- Connections
> - In Hilbert-space language this is the completeness relation for the trigonometric orthonormal basis, $\sum_n(f, e_n)e_n = f$ in norm: [[§35 The Completeness Relation#^thm-35-2|556 Thm. §35.2]], with the Fourier basis (there in complex form, $e^{in\theta}/\sqrt{2\pi}$ on $[0, 2\pi]$) as [[§35 The Completeness Relation#^ex-35-2|556 Ex. §35.2]].
> - The converse, that every coefficient sequence with $\sum(a_n^2 + b_n^2) < \infty$ belongs to some $f$ with $\int f^2$ finite, needs a complete space of functions; this holds for the Lebesgue integral, where $L^2$ is complete (Riesz–Fischer, [[§35 Lᵖ as a Banach Space#^thm-35-11|551 Thm. §35.11]]), but not for the Riemann integral.

> [!remark] Remark: Summary
> If $f$ is defined on $-a < x < a$ and $\int_{-a}^{a}f^2\,dx$ is finite, then:
> 1. among all finite series $A_0 + \sum_1^N A_n\cos\frac{n\pi x}{a} + B_n\sin\frac{n\pi x}{a}$, the one that best approximates $f$ in the sense of the error (2) is the truncated Fourier series of $f$ (Theorem §15.2);
> 2. $\frac1a\int_{-a}^{a}f^2\,dx = 2a_0^2 + \sum_1^\infty(a_n^2 + b_n^2)$ (Theorem §15.4);
> 3. $a_n \to 0$ and $b_n \to 0$ as $n \to \infty$ (Corollary §15.5);
> 4. the Fourier series of $f$ converges to $f$ in the sense of the mean (Theorem §15.6).
>
> Square integrability is a much weaker condition than sectional continuity (every sectionally continuous function is square integrable, being bounded); the lecture points to Stein and Shakarchi, *Fourier Analysis*, Section 3.1, for this general setting. Convergence in the mean says nothing about any single point: it allows a large error on a set of small total length. Pointwise convergence ([[§12 Convergence of Fourier Series#^thm-12-1|Theorem §12.1]]) and uniform convergence ([[§13 Uniform Convergence#^thm-13-3|Theorem §13.3]]) need more smoothness but say more.
>
> *Source: 341 lectures 9.10, 9.12 (the last paragraph)*

^rem-15-1

## Examples

> [!example] Example §15.1: Mean Error and Parseval for f(x) = x
> **(a)** For $f(x) = x$, $-1 < x < 1$, the coefficients are $a_0 = a_n = 0$, $b_n = \frac{2(-1)^{n + 1}}{n\pi}$ ([[§11 Even and Odd Functions; Half-Range Expansions#^ex-11-1|Example §11.1]]), and $\int_{-1}^{1}x^2\,dx = \frac23$. With $a = 1$ the minimum mean error (6) is
>
> $$
> \min(E_N) = \frac23 - \sum_{n=1}^{N}\frac{4}{n^2\pi^2} :
> $$
>
> $\min(E_1) = \frac23 - \frac{4}{\pi^2} \approx 0.261$, $\min(E_2) \approx 0.160$, $\min(E_5) \approx 0.073$, $\min(E_{10}) \approx 0.039$, $\min(E_{20}) \approx 0.020$, decreasing to $0$ roughly like $\frac{4}{\pi^2N}$ although the series does not converge uniformly (the periodic extension jumps at $\pm1$). Parseval's equality (8) verifies:
>
> $$
> \frac11\int_{-1}^{1}x^2\,dx = \frac23 = \sum_{n=1}^{\infty}\frac{4}{n^2\pi^2}, \qquad\text{that is,}\qquad \sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6} ,
> $$
>
> the sum found by integration in [[§14 Operations on Fourier Series#^ex-14-1|Example §14.1]].
>
> **(b)** For $f(x) = \sin x$, $-\pi < x < \pi$, the Fourier series is $\sin x$ itself: $b_1 = 1$ and all other coefficients are $0$. Parseval: $\frac1\pi\int_{-\pi}^{\pi}\sin^2x\,dx = \frac1\pi\cdot\pi = 1 = b_1^2$.
>
> *Powers: Exercise 1.6.2*

^ex-15-1

![[m341-11-1.svg]]
*Example §11.1: the minimum mean error $\min(E_N)$ for $f(x) = x$ on $(-1, 1)$, for $N = 1, \ldots, 20$ (dots), compared with $\frac{4}{\pi^2N}$ (curve). The total squared error tends to zero although the partial sums never converge uniformly near the jumps at $\pm1$.*

> [!example] Example §15.2: Parseval for x² and the Sum of 1/n⁴
> The function $f(x) = x^2$, $-\pi < x < \pi$, has $a_0 = \frac{\pi^2}{3}$, $a_n = \frac{4(-1)^n}{n^2}$, $b_n = 0$ ([[§14 Operations on Fourier Series#^ex-14-3|Example §14.3]](II)). Parseval's equality (8) with $a = \pi$:
>
> $$
> \frac1\pi\int_{-\pi}^{\pi}x^4\,dx = \frac{2\pi^4}{5} = 2\Big(\frac{\pi^2}{3}\Big)^2 + \sum_{n=1}^{\infty}\frac{16}{n^4} = \frac{2\pi^4}{9} + 16\sum_{n=1}^{\infty}\frac{1}{n^4} .
> $$
>
> So $16\sum\frac{1}{n^4} = \frac{2\pi^4}{5} - \frac{2\pi^4}{9} = \frac{8\pi^4}{45}$ and $\sum_{n=1}^{\infty}\frac{1}{n^4} = \frac{\pi^4}{90}$, in agreement with the three integrations of [[§14 Operations on Fourier Series#^ex-14-1|Example §14.1]].
>
> *Source: 341 Review Sheet 1, Problem 6(a) (the series); 341 HW 3, Problem 2(c) (the sum, there by integration)*

^ex-15-2

> [!example] Example §15.3: An Integral from Parseval's Equality
> Evaluate $\frac1\pi\int_{-\pi}^{\pi}\big(\ln|2\cos(x/2)|\big)^2\,dx$.
>
> The equality
>
> $$
> \ln\Big|2\cos\Big(\frac x2\Big)\Big| = \sum_{n=1}^{\infty}\frac{(-1)^{n + 1}}{n}\cos nx
> $$
>
> is valid except when $x$ is an odd multiple of $\pi$ (Powers Exercise 1.5.7; it is derived by complex methods in [[§19★ Complex Methods#^ex-19-1|Example §19.1]]). So $a_0 = 0$, $a_n = \frac{(-1)^{n + 1}}{n}$, $b_n = 0$. The function has logarithmic singularities at $\pm\pi$ but its square is integrable, so Parseval's equality applies:
>
> $$
> \frac1\pi\int_{-\pi}^{\pi}\Big(\ln\Big|2\cos\frac x2\Big|\Big)^2dx = \sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6} ,
> $$
>
> using [[§14 Operations on Fourier Series#^ex-14-1|Example §14.1]] (Powers 1.5, Equation (5)). So the integral itself is $\frac{\pi^3}{6} \approx 5.168$, which numerical integration confirms.
>
> *Powers: Exercise 1.6.1*

^ex-15-3

> [!example] Example §15.4: When ∫f² Is Infinite
> **(a)** If a function on $-a < x < a$ has Fourier coefficients $a_n = 0$, $b_n = 1/\sqrt n$, what can be said about $\int_{-a}^{a}f^2\,dx$? If it were finite, Bessel's inequality would make $\sum b_n^2 = \sum\frac1n$ converge, but the harmonic series diverges. So $\int_{-a}^{a}f^2\,dx$ is infinite: $f$ is not square integrable, although its coefficients tend to zero.
>
> **(b)** The Fourier sine coefficients of $f(x) = 1/x$, $-\pi < x < \pi$, do not tend to zero. (Since $f$ is odd, the cosine coefficients may be taken to be zero, although strictly speaking they do not exist.) Substituting $t = nx$ and using $\int_0^\infty\frac{\sin t}{t}dt = \frac\pi2$,
>
> $$
> b_n = \frac1\pi\int_{-\pi}^{\pi}\frac{\sin nx}{x}\,dx = \frac2\pi\int_0^{n\pi}\frac{\sin t}{t}\,dt \longrightarrow \frac2\pi\cdot\frac\pi2 = 1 .
> $$
>
> (Numerically $b_1 \approx 1.179$, $b_2 \approx 0.903$, $b_{20} \approx 0.990$.) This does not contradict Corollary §15.5: $\int_{-\pi}^{\pi}x^{-2}\,dx$ is infinite.
>
> **(c)** For $f(x) = |x|^{1/2}$, $-1 < x < 1$, $\int f^2 = \int|x| = 1$ is finite, so $a_n \to 0$ and $b_n = 0$. For $f(x) = |x|^{-1/2}$, $\int f^2 = \int_{-1}^{1}|x|^{-1}dx$ is infinite and Section 1.6 says nothing; in fact here $a_n = 2\int_0^1 x^{-1/2}\cos(n\pi x)\,dx$ still tends to zero, but only like $\sqrt{2/n}$, so that $\sum a_n^2$ diverges, consistent with $\int f^2 = \infty$.
>
> *Powers: Exercises 1.6.3, 1.6.5, 1.6.6*

^ex-15-4
