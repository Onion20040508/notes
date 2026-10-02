---
type: section
subject: "[[Complex Variables]]"
chapter: 5
section: 71
bc: "71"
aliases: ["B&C 71"]
tags: [complex-variables, math342, extension]
---
← [[§70★ Continuity of Sums of Power Series]] · ↑ [[· 5 Series]] · [[§72★ Uniqueness of Series Representations]] →

*Brown–Churchill, Section 71 · MAT 342 HW 10 · Practice Final (Fall 1999).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Inside its circle of convergence a power series may be integrated term by term along any contour, even after multiplication by a continuous function $g$. Two consequences follow. The sum of a power series is analytic: integrating against $g \equiv 1$ shows that every closed contour integral of the sum vanishes, and Morera's theorem applies. A power series may also be differentiated term by term: integrating against the Cauchy kernel $g(s) = \frac{1}{2\pi i}(s - z)^{-2}$ turns both sides into derivatives. Together with Taylor's theorem this gives an exact description of the Taylor series of an analytic function: it converges to $f$ in the largest disk about $z_0$ in which $f$ is analytic, and in no larger disk. HW 10 uses these facts to differentiate known series and to show that functions such as $(1 - \cos z)/z^2$, suitably defined at $0$, are entire.

Throughout, let

$$
S(z) = \sum_{n=0}^{\infty}a_n(z - z_0)^n \qquad (1)
$$

be a power series with circle of convergence $|z - z_0| = R$, so that $S$ is continuous for $|z - z_0| < R$ ([[§70★ Continuity of Sums of Power Series#^thm-70-1|Theorem §70.1]]).

## Term-by-Term Integration and Analyticity

> [!theorem] Theorem §71.1: Term-by-Term Integration
> Let $C$ denote any contour interior to the circle of convergence of the power series (1), and let $g(z)$ be any function that is continuous on $C$. The series formed by multiplying each term of the power series by $g(z)$ can be integrated term by term over $C$; that is,
>
> $$
> \int_C g(z)S(z)\,dz = \sum_{n=0}^{\infty}a_n\int_C g(z)(z - z_0)^n\,dz . \qquad (2)
> $$
>
> *B&C: Sec. 71, Theorem 1*

^thm-71-1

> [!proof]+ Proof
> Since both $g(z)$ and the sum $S(z)$ are continuous on $C$, the integral over $C$ of the product
>
> $$
> g(z)S(z) = \sum_{n=0}^{N-1}a_ng(z)(z - z_0)^n + g(z)\rho_N(z) ,
> $$
>
> where $\rho_N(z)$ is the remainder after $N$ terms, exists. The terms of the finite sum are also continuous on $C$, so their integrals exist; consequently the integral of $g(z)\rho_N(z)$ exists, and
>
> $$
> \int_C g(z)S(z)\,dz = \sum_{n=0}^{N-1}a_n\int_C g(z)(z - z_0)^n\,dz + \int_C g(z)\rho_N(z)\,dz . \qquad (3)
> $$
>
> Let $M$ be the maximum value of $|g(z)|$ on $C$ and $L$ the length of $C$. The contour $C$ is the image of a closed interval under a continuous map, so $|z - z_0|$ attains a maximum $R_1$ on $C$, and $R_1 < R$ because $C$ is interior to the circle of convergence. By the uniform convergence of the power series on $|z - z_0| \le R_1$ ([[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-3|Theorem §69.3]]; B&C cites §69 without making the closed disk explicit), for each $\varepsilon > 0$ there is a positive integer $N_\varepsilon$ such that, for all points $z$ on $C$,
>
> $$
> |\rho_N(z)| < \varepsilon \qquad\text{whenever}\qquad N > N_\varepsilon .
> $$
>
> Since $N_\varepsilon$ is independent of $z$, the ML-inequality ([[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]]) gives
>
> $$
> \Big|\int_C g(z)\rho_N(z)\,dz\Big| \le M\varepsilon L \qquad\text{whenever}\qquad N > N_\varepsilon ;
> $$
>
> that is, $\lim_{N\to\infty}\int_C g(z)\rho_N(z)\,dz = 0$. It follows from (3) that
>
> $$
> \int_C g(z)S(z)\,dz = \lim_{N\to\infty}\sum_{n=0}^{N-1}a_n\int_C g(z)(z - z_0)^n\,dz ,
> $$
>
> which is equation (2).

^pf-71-1

*Uses:* [[§70★ Continuity of Sums of Power Series#^thm-70-1|§70.1]], [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-3|§69.3]], [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|§47.2]] (ML-inequality), [[§44 Contour Integrals#^thm-44-2|§44.2]] (existence and linearity of contour integrals)

> [!theorem] Corollary §71.2: The Sum of a Power Series Is Analytic
> The sum $S(z)$ of power series (1) is analytic at each point $z$ interior to the circle of convergence of that series.
>
> *B&C: Sec. 71, Corollary*

^cor-71-2

> [!proof]+ Proof
> Take $g(z) = 1$ in [[§71★ Integration and Differentiation of Power Series#^thm-71-1|Theorem §71.1]]. *(B&C writes "if $|g(z)| = 1$", p. 214; the argument needs $g(z) = 1$.)* Each function $(z - z_0)^n$ $(n = 0, 1, 2, \ldots)$ is entire, so for every closed contour $C$ lying in the open disk bounded by the circle of convergence,
>
> $$
> \int_C(z - z_0)^n\,dz = 0 \qquad (n = 0, 1, 2, \ldots)
> $$
>
> (it has the antiderivative $(z - z_0)^{n+1}/(n + 1)$, [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]]). By equation (2), then, $\int_C S(z)\,dz = 0$ for every such contour. Since $S$ is continuous in the disk ([[§70★ Continuity of Sums of Power Series#^thm-70-1|Theorem §70.1]]), Morera's theorem ([[§57 Some Consequences of the Extension#^thm-57-3|Theorem §57.3]]) shows that $S$ is analytic throughout the disk.

^pf-71-2

*Uses:* [[§71★ Integration and Differentiation of Power Series#^thm-71-1|§71.1]], [[§70★ Continuity of Sums of Power Series#^thm-70-1|§70.1]], [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|§49.1]], [[§57 Some Consequences of the Extension#^thm-57-3|§57.3]] (Morera's theorem)

The corollary is often helpful in establishing the analyticity of functions and in evaluating limits ([[§71★ Integration and Differentiation of Power Series#^ex-71-1|Example §71.1]]). It also settles a question left open in [[§62 Taylor Series#^rem-62-1|§62]]. By Taylor's theorem, the Taylor series of $f$ about $z_0$ converges to $f(z)$ inside the circle centered at $z_0$ and passing through the nearest point $z_1$ at which $f$ fails to be analytic. No larger circle has this property.

> [!theorem] Corollary §71.3: The Taylor Disk Cannot Be Enlarged
> Let the Taylor series of $f$ about $z_0$ converge to $f(z)$ in $|z - z_0| < |z_1 - z_0|$, where $z_1$ is a point at which $f$ is not analytic. Then there is no circle $|z - z_0| = R$ with $R > |z_1 - z_0|$ such that the Taylor series converges to $f(z)$ at each point $z$ interior to it.
>
> *B&C: Sec. 71 (text)*

^cor-71-3

> [!proof]+ Proof
> If there were such a circle, the sum $S(z)$ of the Taylor series would be analytic in $|z - z_0| < R$ by [[§71★ Integration and Differentiation of Power Series#^cor-71-2|Corollary §71.2]], and $f(z) = S(z)$ throughout that disk. The point $z_1$ is inside the disk, so $f$ would coincide with an analytic function on a neighborhood of $z_1$, and so would be analytic at $z_1$. But $f$ is not analytic at $z_1$.

^pf-71-3

*Uses:* [[§71★ Integration and Differentiation of Power Series#^cor-71-2|§71.2]], [[§63 Proof of Taylor's Theorem#^thm-63-1|§63.1]]

> [!remark]- Remark: A Taylor Series Can Converge Further, to Something Else
> Corollary §71.3 is about convergence *to $f$*. The series itself may converge in a larger disk. Expand $\operatorname{Log}z$ about $z_0 = -1 + i$. The nearest points where $\operatorname{Log}$ fails to be analytic are on its branch cut, the ray $x \le 0$, $y = 0$; the closest is $-1$, at distance $1$. Since $\frac{d}{dz}\operatorname{Log}z = 1/z$, the series is $\operatorname{Log}z_0 + \sum_{n \ge 1}\frac{(-1)^{n+1}}{nz_0^n}(z - z_0)^n$, whose terms are those of the logarithm series of [[§71★ Integration and Differentiation of Power Series#^ex-71-4|Example §71.4]] scaled by $z_0$; it converges in the larger disk $|z - z_0| < |z_0| = \sqrt2$, which reaches the genuine singular point $0$. In that disk its sum is the branch of $\log z$ that agrees with $\operatorname{Log}z$ in the upper half plane, and below the cut it equals $\operatorname{Log}z + 2\pi i$. So in the disk of radius $\sqrt2$ the series does not converge to $\operatorname{Log}z$, in agreement with the corollary. The branch cut, not the series, limits the disk.

^rem-71-1

## Term-by-Term Differentiation

> [!theorem] Theorem §71.4: Term-by-Term Differentiation
> The power series (1) can be differentiated term by term. That is, at each point $z$ interior to the circle of convergence of that series,
>
> $$
> S'(z) = \sum_{n=1}^{\infty}na_n(z - z_0)^{n-1} . \qquad (6)
> $$
>
> *B&C: Sec. 71, Theorem 2*

^thm-71-4

> [!proof]+ Proof
> Let $z$ be any point interior to the circle of convergence. Let $C$ be a positively oriented simple closed contour surrounding $z$ and interior to that circle; for instance the circle $|s - z| = \delta$ with $0 < \delta < R - |z - z_0|$. Define
>
> $$
> g(s) = \frac{1}{2\pi i}\cdot\frac{1}{(s - z)^2} \qquad (7)
> $$
>
> at each point $s$ on $C$. Since $g$ is continuous on $C$, [[§71★ Integration and Differentiation of Power Series#^thm-71-1|Theorem §71.1]] gives
>
> $$
> \int_C g(s)S(s)\,ds = \sum_{n=0}^{\infty}a_n\int_C g(s)(s - z_0)^n\,ds . \qquad (8)
> $$
>
> Now $S$ is analytic inside and on $C$ ([[§71★ Integration and Differentiation of Power Series#^cor-71-2|Corollary §71.2]]), so the integral representation for derivatives ([[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|Theorem §56.1]]) gives
>
> $$
> \int_C g(s)S(s)\,ds = \frac{1}{2\pi i}\int_C\frac{S(s)\,ds}{(s - z)^2} = S'(z) .
> $$
>
> Furthermore, since each $(s - z_0)^n$ is entire, the same formula gives
>
> $$
> \int_C g(s)(s - z_0)^n\,ds = \frac{1}{2\pi i}\int_C\frac{(s - z_0)^n}{(s - z)^2}\,ds = \frac{d}{dz}(z - z_0)^n \qquad (n = 0, 1, 2, \ldots) .
> $$
>
> Thus equation (8) reduces to $S'(z) = \sum_{n=0}^{\infty}a_n\frac{d}{dz}(z - z_0)^n$, which is equation (6), the $n = 0$ term being zero.

^pf-71-4

*Uses:* [[§71★ Integration and Differentiation of Power Series#^thm-71-1|§71.1]], [[§71★ Integration and Differentiation of Power Series#^cor-71-2|§71.2]], [[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|§56.1]]

Since $S'$ is again analytic in the disk, the theorem can be applied repeatedly: $S$ has derivatives of all orders there, each given by a term-by-term differentiated series ([[§72★ Uniqueness of Series Representations#^ex-72-3|Example §72.3]]).

> [!remark]- Connections
> - The real counterparts are [[§26 Differentiation and Integration of Power Series#^thm-26-3|451 Thm. §26.3]] (integrating a uniformly convergent series) and [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]] (term-by-term calculus for power series), with the exchange of limit and integral [[§25 More on Uniform Convergence#^thm-25-1|451 Thm. §25.1]]. In 451, differentiating term by term needs a separate argument about the derived series; here it follows from integration, because the Cauchy integral formula expresses a derivative as an integral. The calculus statement is [[§77 Representations of Functions as Power Series#^thm-77-1|Calc Thm. §77.1]].

## Examples

> [!example] Example §71.1: Removable Singularities Give Entire Functions
> **(a)** The function defined by
>
> $$
> f(z) = \begin{cases} (\sin z)/z & \text{when } z \ne 0, \\ 1 & \text{when } z = 0 \end{cases}
> $$
>
> is entire. The Maclaurin series $\sin z = \sum_{n=0}^{\infty}(-1)^n\frac{z^{2n+1}}{(2n + 1)!}$ (4) is valid for every $z$, so the series
>
> $$
> \sum_{n=0}^{\infty}(-1)^n\frac{z^{2n}}{(2n + 1)!} = 1 - \frac{z^2}{3!} + \frac{z^4}{5!} - \cdots , \qquad (5)
> $$
>
> obtained by dividing each side of (4) by $z$, converges to $f(z)$ when $z \ne 0$. It also converges to $f(z)$ when $z = 0$, where its value is $1$. Hence $f$ is represented by the convergent series (5) for all $z$, and $f$ is entire by Corollary §71.2. Since $f$ is continuous at $0$,
>
> $$
> \lim_{z\to0}\frac{\sin z}{z} = \lim_{z\to0}f(z) = f(0) = 1 ,
> $$
>
> a result known beforehand as the derivative $\lim_{z\to0}\frac{\sin z - \sin 0}{z - 0} = \cos 0 = 1$.
>
> **(b)** The function defined by
>
> $$
> f(z) = \begin{cases} (1 - \cos z)/z^2 & \text{when } z \ne 0, \\ 1/2 & \text{when } z = 0 \end{cases}
> $$
>
> is entire. From the series of $\cos z$, $1 - \cos z = \sum_{n=1}^{\infty}(-1)^{n+1}\frac{z^{2n}}{(2n)!}$, so for $z \ne 0$
>
> $$
> f(z) = \sum_{n=1}^{\infty}(-1)^{n+1}\frac{z^{2n-2}}{(2n)!} = \frac12 - \frac{z^2}{24} + \frac{z^4}{720} - \cdots .
> $$
>
> The series converges for all $z$, and at $z = 0$ its value is $\frac{1}{2!} = \frac12 = f(0)$. So $f$ is the sum of a power series with infinite circle of convergence, and $f$ is entire by Corollary §71.2.
>
> *B&C: Sec. 71, Example 1; Sec. 72, Exercise 4; Source: 342 HW 10*

^ex-71-1

> [!example] Example §71.2: Differentiating Known Series
> **(a) $1/z^2$ about $z_0 = 1$.** By [[§64 Examples (Proof of Taylor's Theorem)#^ex-64-1|Example §64.1]], $\frac1z = \sum_{n=0}^{\infty}(-1)^n(z - 1)^n$ $(|z - 1| < 1)$. Differentiating each side (Theorem §71.4),
>
> $$
> -\frac{1}{z^2} = \sum_{n=1}^{\infty}(-1)^nn(z - 1)^{n-1} \qquad (|z - 1| < 1), \qquad\text{or}\qquad \frac{1}{z^2} = \sum_{n=0}^{\infty}(-1)^n(n + 1)(z - 1)^n \qquad (|z - 1| < 1),
> $$
>
> after replacing $n$ by $n + 1$ and multiplying by $-1$.
>
> **(b) Powers of $1/(1 - z)$.** Differentiating $\frac{1}{1 - z} = \sum_{n=0}^{\infty}z^n$ $(|z| < 1)$ once and twice,
>
> $$
> \frac{1}{(1 - z)^2} = \sum_{n=1}^{\infty}nz^{n-1} = \sum_{n=0}^{\infty}(n + 1)z^n, \qquad \frac{2}{(1 - z)^3} = \sum_{n=1}^{\infty}n(n + 1)z^{n-1} = \sum_{n=0}^{\infty}(n + 1)(n + 2)z^n \qquad (|z| < 1) .
> $$
>
> *B&C: Sec. 71, Example 2; Sec. 72, Exercise 1; Source: 342 HW 10*

^ex-71-2

> [!example] Example §71.3: 1/z² About z₀ = 2
> **Problem.** Find the Taylor series of $\frac1z = \frac{1}{2 + (z - 2)} = \frac12\cdot\frac{1}{1 + (z - 2)/2}$ about $z_0 = 2$; then differentiate it to show that
>
> $$
> \frac{1}{z^2} = \frac14\sum_{n=0}^{\infty}(-1)^n(n + 1)\Big(\frac{z - 2}{2}\Big)^n \qquad (|z - 2| < 2) .
> $$
>
> Since $\big|\frac{z - 2}{2}\big| < 1$ when $|z - 2| < 2$,
>
> $$
> \frac1z = \frac12\sum_{n=0}^{\infty}\Big(-\frac{z - 2}{2}\Big)^n = \sum_{n=0}^{\infty}\frac{(-1)^n}{2^{n+1}}(z - 2)^n \qquad (|z - 2| < 2) .
> $$
>
> Differentiating term by term,
>
> $$
> -\frac{1}{z^2} = \sum_{n=1}^{\infty}\frac{(-1)^nn}{2^{n+1}}(z - 2)^{n-1} = \sum_{n=0}^{\infty}\frac{(-1)^{n+1}(n + 1)}{2^{n+2}}(z - 2)^n ,
> $$
>
> so $\dfrac{1}{z^2} = \sum_{n=0}^{\infty}\dfrac{(-1)^n(n + 1)}{2^{n+2}}(z - 2)^n = \dfrac14\sum_{n=0}^{\infty}(-1)^n(n + 1)\Big(\dfrac{z - 2}{2}\Big)^n$. The first terms $\frac14 - \frac14(z - 2) + \frac{3}{16}(z - 2)^2 - \frac18(z - 2)^3$ agree with sympy.
>
> *B&C: Sec. 72, Exercise 3; Source: 342 HW 10*

^ex-71-3

> [!example] Example §71.4: The Logarithm by Integration
> **(a) The series of $\operatorname{Log}z$ about $1$.** In the $w$ plane, integrate the Taylor series
>
> $$
> \frac1w = \sum_{n=0}^{\infty}(-1)^n(w - 1)^n \qquad (|w - 1| < 1)
> $$
>
> along a contour $C$ from $w = 1$ to $w = z$ interior to its circle of convergence (say the segment). By Theorem §71.1 with $g = 1$,
>
> $$
> \int_C\frac{dw}{w} = \sum_{n=0}^{\infty}(-1)^n\int_C(w - 1)^n\,dw = \sum_{n=0}^{\infty}(-1)^n\frac{(z - 1)^{n+1}}{n + 1} .
> $$
>
> The disk $|w - 1| < 1$ lies in the right half plane, away from the branch cut of $\operatorname{Log}w$, and $\operatorname{Log}w$ is an antiderivative of $1/w$ there, so the left side is $\operatorname{Log}z - \operatorname{Log}1 = \operatorname{Log}z$ ([[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]]). Replacing $n$ by $n - 1$,
>
> $$
> \operatorname{Log}z = \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}(z - 1)^n \qquad (|z - 1| < 1) .
> $$
>
> **(b) $\operatorname{Log}z/(z - 1)$ is analytic.** Let $f(z) = \operatorname{Log}z/(z - 1)$ for $z \ne 1$ and $f(1) = 1$. Away from $z = 1$, $f$ is a quotient of analytic functions in the domain $0 < |z| < \infty$, $-\pi < \operatorname{Arg}z < \pi$. In the disk $|z - 1| < 1$, (a) gives $f(z) = \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}(z - 1)^{n-1}$ for $z \ne 1$, and the series has the value $1 = f(1)$ at $z = 1$. So near $1$, $f$ is the sum of a power series, hence analytic (Corollary §71.2). Thus $f$ is analytic throughout the domain.
>
> **(c) Fall 1999: the Laurent series of $\operatorname{Log}z/(z - i)$ about $z_0 = i$.** The open disk $|z - i| < 1$ does not meet the branch cut ($|x - i| = \sqrt{x^2 + 1} \ge 1$ for real $x$), so $\operatorname{Log}$ is analytic there. As in (a), expand $\frac1w = \frac{1}{i + (w - i)} = \sum_{n=0}^{\infty}\frac{(-1)^n}{i^{n+1}}(w - i)^n$ $(|w - i| < 1)$ and integrate from $i$ to $z$:
>
> $$
> \operatorname{Log}z = \operatorname{Log}i + \sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n\,i^n}(z - i)^n = \frac{i\pi}{2} - i(z - i) + \frac12(z - i)^2 + \frac i3(z - i)^3 - \cdots \qquad (|z - i| < 1) .
> $$
>
> Dividing by $z - i$,
>
> $$
> \frac{\operatorname{Log}z}{z - i} = \frac{i\pi/2}{z - i} + \sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n\,i^n}(z - i)^{n-1} = \frac{i\pi/2}{z - i} - i + \frac12(z - i) + \frac i3(z - i)^2 - \cdots \qquad (0 < |z - i| < 1) .
> $$
>
> (Coefficients checked against sympy's expansion of $\operatorname{Log}z$ at $i$.)
>
> *B&C: Sec. 72, Exercises 6 and 7; Source: 342 practice final (Fall 1999), Q6(a) (part (c))*

^ex-71-4
