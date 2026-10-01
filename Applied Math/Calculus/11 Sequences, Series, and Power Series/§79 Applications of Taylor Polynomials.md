---
type: section
subject: "[[Calculus]]"
chapter: 11
section: 79
stewart: "11.11"
aliases: ["Stewart 11.11"]
tags: [calculus]
---
← [[§78 Taylor and Maclaurin Series]] · ↑ [[· 11 Sequences, Series, and Power Series]] · [[§80 Three-Dimensional Coordinate Systems]] →

*Stewart, Section 11.11.*

A Taylor polynomial $T_n$ is a partial sum of a Taylor series, so when $f$ is the sum of its Taylor series, $f(x) \approx T_n(x)$. Polynomials are the simplest functions to compute with, which is why calculators and computers evaluate $\sin$, $e^x$ and their relatives this way. The practical questions are how good the approximation is and how large $n$ must be for a given accuracy; they are answered by bounding the remainder $R_n(x) = f(x) - T_n(x)$, with the Alternating Series Estimation Theorem ([[§73 Alternating Series and Absolute Convergence|§73]]) or Taylor's Inequality ([[§78 Taylor and Maclaurin Series|§78]]). Physicists use the same idea to simplify formulas: keeping the first one or two terms of a Taylor series turns Einstein's kinetic energy into Newton's, and the law of refraction at a curved surface into the lens equation of Gaussian optics.

## Approximating Functions by Polynomials

Suppose $f$ is equal to the sum of its Taylor series at $a$. The $n$th-degree Taylor polynomial ([[§78 Taylor and Maclaurin Series#^def-78-2|Definition §78.2]])

$$
T_n(x) = \sum_{i=0}^{n} \frac{f^{(i)}(a)}{i!} (x - a)^i = f(a) + \frac{f'(a)}{1!} (x - a) + \frac{f''(a)}{2!} (x - a)^2 + \cdots + \frac{f^{(n)}(a)}{n!} (x - a)^n
$$

is its $n$th partial sum, so $T_n(x) \to f(x)$ as $n \to \infty$, and $T_n$ can be used as an approximation: $f(x) \approx T_n(x)$. The first-degree polynomial $T_1(x) = f(a) + f'(a)(x - a)$ is the linearization of $f$ at $a$ ([[§23 Linear Approximations and Differentials|§23]]); $T_1$ and its derivative have the same values at $a$ as $f$ and $f'$. In general:

> [!theorem] Proposition §79.1: Taylor Polynomials Match Derivatives
> The derivatives of $T_n$ at $a$ agree with those of $f$ up to and including the derivatives of order $n$:
>
> $$
> T_n^{(k)}(a) = f^{(k)}(a) \qquad k = 0, 1, \ldots, n .
> $$
>
> *Stewart: 11.11 (text)*

^prop-79-1

> [!proof]+ Proof
> (Stewart: "it can be shown that".) Differentiating $T_n$ term by term $k$ times, the terms with $i < k$ vanish, and for $i \ge k$, $\frac{d^k}{dx^k} (x - a)^i = \frac{i!}{(i-k)!} (x - a)^{i-k}$. So
>
> $$
> T_n^{(k)}(x) = \sum_{i=k}^{n} \frac{f^{(i)}(a)}{(i - k)!} (x - a)^{i-k} .
> $$
>
> At $x = a$ every term with $i > k$ is $0$, leaving $T_n^{(k)}(a) = \frac{f^{(k)}(a)}{0!} = f^{(k)}(a)$.

^pf-79-1

*Uses:* [[§78 Taylor and Maclaurin Series#^def-78-2|Def. §78.2]], [[§14 Derivatives of Polynomials and Exponential Functions|§14]] (Power Rule)

> [!remark] Remark: How Fast Do the Taylor Polynomials of the Exponential Converge?
> For $y = e^x$ at $0$, the graph of $T_1(x) = 1 + x$ is the tangent line at $(0, 1)$, the best linear approximation near $0$; $T_2(x) = 1 + x + x^2/2$ is a parabola and $T_3(x) = 1 + x + x^2/2 + x^3/6$ a cubic that fits the exponential curve more closely, and so on. Numerically:
>
> | | $x = 0.2$ | $x = 3.0$ |
> |---|---|---|
> | $T_2(x)$ | $1.220000$ | $8.500000$ |
> | $T_4(x)$ | $1.221400$ | $16.375000$ |
> | $T_6(x)$ | $1.221403$ | $19.412500$ |
> | $T_8(x)$ | $1.221403$ | $20.009152$ |
> | $T_{10}(x)$ | $1.221403$ | $20.079665$ |
> | $e^x$ | $1.221403$ | $20.085537$ |
>
> At $x = 0.2$ the convergence is very rapid; at $x = 3$ it is much slower. The farther $x$ is from $0$, the more slowly $T_n(x)$ converges to $e^x$.

^rem-79-1

> [!remark] Remark: Method — Estimating the Error of a Taylor Approximation
> To decide how good $f(x) \approx T_n(x)$ is, estimate $|R_n(x)| = |f(x) - T_n(x)|$ in one of three ways:
> 1. Graph $|R_n(x)| = |f(x) - T_n(x)|$ with a calculator or computer and read off the maximum on the interval.
> 2. If the series happens to be alternating, use the Alternating Series Estimation Theorem ([[§73 Alternating Series and Absolute Convergence#^thm-73-2|Theorem §73.2]]): the error is at most the first omitted term.
> 3. In all cases, use Taylor's Inequality ([[§78 Taylor and Maclaurin Series#^thm-78-4|Theorem §78.4]]): if $|f^{(n+1)}(x)| \le M$ on the interval, then $|R_n(x)| \le \dfrac{M}{(n+1)!} |x - a|^{n+1}$. To find $M$, bound $|f^{(n+1)}|$ on the interval, usually at an endpoint where a power of $x$ in a denominator is smallest.
>
> To find how large $n$ must be (or how close $x$ must be to $a$) for a prescribed accuracy, set the bound less than the tolerance and solve.
>
> *Stewart: 11.11 (text)*

^rem-79-2

> [!example] Example §79.1: A Cube Root by Taylor's Inequality
> **(a)** Approximate $f(x) = \sqrt[3]{x}$ by a Taylor polynomial of degree $2$ at $a = 8$. **(b)** How accurate is this approximation when $7 \le x \le 9$?
>
> **(a)**
>
> $$
> \begin{aligned}
> f(x) &= \sqrt[3]{x} = x^{1/3} & f(8) &= 2 \\
> f'(x) &= \tfrac13 x^{-2/3} & f'(8) &= \tfrac13 \cdot \tfrac14 = \tfrac{1}{12} \\
> f''(x) &= -\tfrac29 x^{-5/3} & f''(8) &= -\tfrac29 \cdot \tfrac{1}{32} = -\tfrac{1}{144} \\
> f'''(x) &= \tfrac{10}{27} x^{-8/3}
> \end{aligned}
> $$
>
> So the second-degree Taylor polynomial is
>
> $$
> T_2(x) = f(8) + \frac{f'(8)}{1!} (x - 8) + \frac{f''(8)}{2!} (x - 8)^2 = 2 + \tfrac{1}{12} (x - 8) - \tfrac{1}{288} (x - 8)^2 ,
> $$
>
> and the desired approximation is $\sqrt[3]{x} \approx 2 + \tfrac{1}{12} (x - 8) - \tfrac{1}{288} (x - 8)^2$.
>
> **(b)** The Taylor series is not alternating when $x < 8$, so the Alternating Series Estimation Theorem does not apply. Use Taylor's Inequality with $n = 2$ and $a = 8$:
>
> $$
> |R_2(x)| \le \frac{M}{3!} |x - 8|^3 , \qquad \text{where } |f'''(x)| \le M .
> $$
>
> Because $x \ge 7$, we have $x^{8/3} \ge 7^{8/3}$, and so
>
> $$
> f'''(x) = \frac{10}{27} \cdot \frac{1}{x^{8/3}} \le \frac{10}{27} \cdot \frac{1}{7^{8/3}} < 0.0021 .
> $$
>
> ($7^{8/3} \approx 179.3$.) So take $M = 0.0021$. Also $7 \le x \le 9$ gives $-1 \le x - 8 \le 1$, so $|x - 8| \le 1$, and Taylor's Inequality gives
>
> $$
> |R_2(x)| \le \frac{0.0021}{3!} \cdot 1^3 = \frac{0.0021}{6} < 0.0004 .
> $$
>
> Thus for $7 \le x \le 9$ the approximation in (a) is accurate to within $0.0004$. (Graphing $|R_2(x)| = |\sqrt[3]{x} - T_2(x)|$ on $[7, 9]$ shows that in fact $|R_2(x)| < 0.0003$ there: the graphical estimate is slightly better.)
>
> *Stewart: Example 11.11.1*

^ex-79-1

> [!example] Example §79.2: Sine by an Alternating Series
> **(a)** What is the maximum error possible in using the approximation
>
> $$
> \sin x \approx x - \frac{x^3}{3!} + \frac{x^5}{5!}
> $$
>
> when $-0.3 \le x \le 0.3$? Use it to find $\sin 12°$ correct to six decimal places. **(b)** For what values of $x$ is this approximation accurate to within $0.00005$?
>
> **(a)** The Maclaurin series $\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots$ is alternating for all $x \ne 0$, and for $|x| < 1$ its terms decrease in size, so the Alternating Series Estimation Theorem applies. The error in using the first three terms is at most
>
> $$
> \left| \frac{x^7}{7!} \right| = \frac{|x|^7}{5040} .
> $$
>
> If $-0.3 \le x \le 0.3$, then $|x| \le 0.3$, and the error is smaller than $\dfrac{(0.3)^7}{5040} \approx 4.3 \times 10^{-8}$.
>
> To find $\sin 12°$, convert to radians:
>
> $$
> \sin 12° = \sin\left( \frac{12\pi}{180} \right) = \sin\frac{\pi}{15} \approx \frac{\pi}{15} - \left( \frac{\pi}{15} \right)^3 \frac{1}{3!} + \left( \frac{\pi}{15} \right)^5 \frac{1}{5!} \approx 0.20791169 .
> $$
>
> Since $\pi/15 \approx 0.209 < 0.3$, the error is below $4.3 \times 10^{-8}$, so correct to six decimal places $\sin 12° \approx 0.207912$.
>
> **(b)** The error is smaller than $0.00005$ if
>
> $$
> \frac{|x|^7}{5040} < 0.00005 , \qquad\text{that is,}\qquad |x|^7 < 0.252 \quad\text{or}\quad |x| < (0.252)^{1/7} \approx 0.821 .
> $$
>
> So the approximation is accurate to within $0.00005$ when $|x| < 0.82$.
>
> **By Taylor's Inequality.** Since $f^{(7)}(x) = -\cos x$, $|f^{(7)}(x)| \le 1$ and $|R_6(x)| \le \frac{1}{7!} |x|^7$. (The approximating polynomial is $T_5 = T_6$, as the $x^6$ coefficient is $0$.) This gives the same estimates; so does graphing $|R_6(x)| = |\sin x - (x - \frac16 x^3 + \frac{1}{120} x^5)|$.
>
> *Stewart: Example 11.11.2*

^ex-79-2

The point of expanding about $a$ is to have $x$ close to $a$. To approximate $\sin 72°$, use Taylor polynomials at $a = \pi/3$ rather than $0$: $72°$ is close to $60° = \pi/3$, where the derivatives of $\sin$ are easy to compute ([[§78 Taylor and Maclaurin Series#^ex-78-2|Example §78.2]]). As $n$ increases, the Maclaurin polynomials $T_1, T_3, T_5, T_7$ approximate $\sin x$ well on larger and larger intervals ([[§78 Taylor and Maclaurin Series#^thm-78-7|§78]], figure). Calculators and computers evaluate $\sin$, $e^x$ and Bessel functions this way, typically with a Taylor polynomial modified to spread the error more evenly over an interval.

## Applications to Physics

A physicist often simplifies a function by keeping only the first two or three terms of its Taylor series, that is, by replacing it with a Taylor polynomial, and uses Taylor's Inequality to gauge the accuracy.

> [!example] Example §79.3: Relativistic and Newtonian Kinetic Energy
> In Einstein's special relativity the mass of an object moving with velocity $v$ is
>
> $$
> m = \frac{m_0}{\sqrt{1 - v^2/c^2}} ,
> $$
>
> where $m_0$ is the rest mass and $c$ the speed of light. The kinetic energy is the difference between the total energy and the energy at rest: $K = mc^2 - m_0 c^2$.
>
> **(a)** Show that when $v$ is very small compared with $c$, this agrees with classical Newtonian physics: $K \approx \frac12 m_0 v^2$. **(b)** Use Taylor's Inequality to estimate the difference between these expressions for $K$ when $|v| \le 100$ m/s.
>
> **(a)**
>
> $$
> K = mc^2 - m_0 c^2 = \frac{m_0 c^2}{\sqrt{1 - v^2/c^2}} - m_0 c^2 = m_0 c^2 \left[ \left( 1 - \frac{v^2}{c^2} \right)^{-1/2} - 1 \right] .
> $$
>
> With $x = -v^2/c^2$ (and $|x| < 1$ because $v < c$), expand $(1 + x)^{-1/2}$ by the binomial series ([[§78 Taylor and Maclaurin Series#^thm-78-9|Theorem §78.9]]) with $k = -\frac12$:
>
> $$
> (1 + x)^{-1/2} = 1 - \frac12 x + \frac{\left( -\frac12 \right)\left( -\frac32 \right)}{2!} x^2 + \frac{\left( -\frac12 \right)\left( -\frac32 \right)\left( -\frac52 \right)}{3!} x^3 + \cdots = 1 - \frac12 x + \frac38 x^2 - \frac{5}{16} x^3 + \cdots
> $$
>
> So
>
> $$
> K = m_0 c^2 \left[ \left( 1 + \frac12 \frac{v^2}{c^2} + \frac38 \frac{v^4}{c^4} + \frac{5}{16} \frac{v^6}{c^6} + \cdots \right) - 1 \right] = m_0 c^2 \left( \frac12 \frac{v^2}{c^2} + \frac38 \frac{v^4}{c^4} + \frac{5}{16} \frac{v^6}{c^6} + \cdots \right) .
> $$
>
> If $v$ is much smaller than $c$, all terms after the first are very small compared with the first. Omitting them,
>
> $$
> K \approx m_0 c^2 \left( \frac12 \frac{v^2}{c^2} \right) = \frac12 m_0 v^2 .
> $$
>
> **(b)** With $x = -v^2/c^2$ and $f(x) = m_0 c^2 [(1 + x)^{-1/2} - 1]$, the Newtonian expression is $T_1(x) = m_0 c^2 (-\frac12 x)$, and if $|f''(x)| \le M$, Taylor's Inequality gives
>
> $$
> |R_1(x)| \le \frac{M}{2!} x^2 .
> $$
>
> Here $f''(x) = \frac34 m_0 c^2 (1 + x)^{-5/2}$, and $|v| \le 100$ m/s, so
>
> $$
> |f''(x)| = \frac{3 m_0 c^2}{4 (1 - v^2/c^2)^{5/2}} \le \frac{3 m_0 c^2}{4 (1 - 100^2/c^2)^{5/2}} \qquad (= M) .
> $$
>
> With $c = 3 \times 10^8$ m/s and $x^2 = v^4/c^4 \le 100^4/c^4$,
>
> $$
> |R_1(x)| \le \frac12 \cdot \frac{3 m_0 c^2}{4 (1 - 100^2/c^2)^{5/2}} \cdot \frac{100^4}{c^4} < (4.17 \times 10^{-10})\, m_0 .
> $$
>
> So when $|v| \le 100$ m/s, the error in using the Newtonian expression for kinetic energy is at most $(4.2 \times 10^{-10})\, m_0$. (The two graphs of $K$ against $v$ are practically identical for $v$ much smaller than $c$, and separate as $v \to c$, where the relativistic $K \to \infty$.)
>
> *Stewart: Example 11.11.3*

^ex-79-3

> [!remark]- Remark: Gaussian and Third-Order Optics
> A wave from a point source $S$ meets a spherical interface of radius $R$ centered at $C$, between media with indices of refraction $n_1$ and $n_2$, and the ray $SA$ is refracted toward a point $P$ on the axis. With $\ell_o = SA$, $\ell_i = AP$, $s_o = SV$ and $s_i = VP$ ($V$ the vertex of the interface on the axis) and $\phi$ the angle $ACV$ at the center, Fermat's principle (light minimizes travel time) gives
>
> $$
> \frac{n_1}{\ell_o} + \frac{n_2}{\ell_i} = \frac1R \left( \frac{n_2 s_i}{\ell_i} - \frac{n_1 s_o}{\ell_o} \right) , \qquad (1)
> $$
>
> and the Law of Cosines in triangles $ACS$ and $ACP$ (with $\cos(\pi - \phi) = -\cos\phi$) gives
>
> $$
> \ell_o = \sqrt{R^2 + (s_o + R)^2 - 2R(s_o + R)\cos\phi} , \qquad \ell_i = \sqrt{R^2 + (s_i - R)^2 + 2R(s_i - R)\cos\phi} . \qquad (2)
> $$
>
> Equation (1) is cumbersome. Gauss (1841) used the linear approximation $\cos\phi \approx 1$ for small $\phi$, that is, the Taylor polynomial of degree $1$. Then $\ell_o \approx s_o$, $\ell_i \approx s_i$, and (1) becomes (Stewart, Exercise 34(a))
>
> $$
> \frac{n_1}{s_o} + \frac{n_2}{s_i} = \frac{n_2 - n_1}{R} . \qquad (3)
> $$
>
> This is **Gaussian** or **first-order optics**, the basic tool of lens design. Approximating $\cos\phi$ by its Taylor polynomial of degree $3$ (which equals that of degree $2$, $1 - \phi^2/2$) takes into account rays that strike the surface at greater heights $h$ above the axis, and leads to **third-order optics** (Exercise 34(b)):
>
> $$
> \frac{n_1}{s_o} + \frac{n_2}{s_i} = \frac{n_2 - n_1}{R} + h^2 \left[ \frac{n_1}{2 s_o} \left( \frac{1}{s_o} + \frac1R \right)^2 + \frac{n_2}{2 s_i} \left( \frac1R - \frac{1}{s_i} \right)^2 \right] . \qquad (4)
> $$

^rem-79-3
