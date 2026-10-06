---
type: section
subject: "[[Calculus]]"
chapter: 11
section: 77
stewart: "11.9"
aliases: ["Stewart 11.9"]
tags: [calculus]
---
← [[§76 Power Series]] · ↑ [[· 11 Sequences, Series, and Power Series]] · [[§78 Taylor and Maclaurin Series]] →

*Stewart, Section 11.9.*

Read backwards, the geometric series $\sum x^n = \frac{1}{1-x}$ says that the function $\frac{1}{1-x}$ *is* a power series on $(-1, 1)$. Substituting, multiplying by powers of $x$, and above all differentiating and integrating term by term produce power series for many more functions: $\frac{1}{(1-x)^2}$, $\ln(1 + x)$, $\tan^{-1} x$. Such representations are useful for integrating functions that have no elementary antiderivative and for approximating functions by polynomials, and some important functions, such as the Bessel functions, are *defined* by power series.

## Representations of Functions using Geometric Series

> [!definition] Definition §77.1: Power Series Representation
> If $f(x) = \sum_{n=0}^{\infty} c_n (x - a)^n$ for all $x$ in an interval $I$, the series is a **power series representation** of $f$ on $I$. The basic example is the geometric series ([[§70 Series#^cor-70-2|Corollary §70.2]]), now read as a statement about the function $f(x) = 1/(1 - x)$:
>
> $$
> \frac{1}{1 - x} = 1 + x + x^2 + x^3 + \cdots = \sum_{n=0}^{\infty} x^n \qquad |x| < 1 . \qquad (1)
> $$
>
> Since a sum is the limit of the partial sums, $\frac{1}{1-x} = \lim_{n \to \infty} s_n(x)$ with $s_n(x) = 1 + x + x^2 + \cdots + x^n$: as $n$ increases, the polynomial $s_n(x)$ becomes a better approximation to $f(x)$ for $-1 < x < 1$. (Outside $(-1, 1)$ the partial sums do not approach $f$ at all.)
>
> *Stewart: 11.9, Equation 1 (text)*

^def-77-1

> [!example] Example §77.1: Substituting into the Geometric Series
> **(a)** Express $1/(1 + x^2)$ as the sum of a power series and find the interval of convergence.
>
> Replace $x$ by $-x^2$ in Equation 1:
>
> $$
> \frac{1}{1 + x^2} = \frac{1}{1 - (-x^2)} = \sum_{n=0}^{\infty} (-x^2)^n = \sum_{n=0}^{\infty} (-1)^n x^{2n} = 1 - x^2 + x^4 - x^6 + x^8 - \cdots
> $$
>
> This is a geometric series, so it converges when $|-x^2| < 1$, that is, $x^2 < 1$, or $|x| < 1$. The interval of convergence is $(-1, 1)$. (The Ratio Test would give the same, with more work.)
>
> **(b)** Find a power series representation for $1/(x + 2)$.
>
> To get the form of the left side of Equation 1, first factor a $2$ from the denominator:
>
> $$
> \frac{1}{2 + x} = \frac{1}{2\left( 1 + \dfrac x2 \right)} = \frac{1}{2\left[ 1 - \left( -\dfrac x2 \right) \right]} = \frac12 \sum_{n=0}^{\infty} \left( -\frac x2 \right)^n = \sum_{n=0}^{\infty} \frac{(-1)^n}{2^{n+1}} x^n .
> $$
>
> This converges when $|-x/2| < 1$, that is, $|x| < 2$. The interval of convergence is $(-2, 2)$.
>
> **(c)** Find a power series representation of $x^3/(x + 2)$.
>
> This is $x^3$ times the function in (b). Since $x^3$ does not depend on $n$, it can be moved across the sigma sign ([[§70 Series#^thm-70-6|Theorem §70.6]](i) with $c = x^3$):
>
> $$
> \frac{x^3}{x + 2} = x^3 \sum_{n=0}^{\infty} \frac{(-1)^n}{2^{n+1}} x^n = \sum_{n=0}^{\infty} \frac{(-1)^n}{2^{n+1}} x^{n+3} = \tfrac12 x^3 - \tfrac14 x^4 + \tfrac18 x^5 - \tfrac{1}{16} x^6 + \cdots
> $$
>
> Shifting the index ($n + 3 \to n$), the same series is $\displaystyle\sum_{n=3}^{\infty} \frac{(-1)^{n-1}}{2^{n-2}} x^n$. As in (b), the interval of convergence is $(-2, 2)$.
>
> *Stewart: Examples 11.9.1–11.9.3*

^ex-77-1

## Differentiation and Integration of Power Series

The sum of a power series is a function $f(x) = \sum_{n=0}^{\infty} c_n (x - a)^n$ whose domain is the interval of convergence. It can be differentiated and integrated term by term, like a polynomial (**term-by-term differentiation and integration**).

> [!theorem] Theorem §77.1: Term-by-Term Differentiation and Integration
> If the power series $\sum c_n (x - a)^n$ has radius of convergence $R > 0$, then the function $f$ defined by
>
> $$
> f(x) = c_0 + c_1 (x - a) + c_2 (x - a)^2 + \cdots = \sum_{n=0}^{\infty} c_n (x - a)^n
> $$
>
> is differentiable (and therefore continuous) on the interval $(a - R, a + R)$, and
>
> $$
> \text{(i)}\ \ f'(x) = c_1 + 2c_2 (x - a) + 3c_3 (x - a)^2 + \cdots = \sum_{n=1}^{\infty} n c_n (x - a)^{n-1}
> $$
>
> $$
> \text{(ii)}\ \ \int f(x)\,dx = C + c_0 (x - a) + c_1 \frac{(x - a)^2}{2} + c_2 \frac{(x - a)^3}{3} + \cdots = C + \sum_{n=0}^{\infty} c_n \frac{(x - a)^{n+1}}{n + 1}
> $$
>
> The radii of convergence of the power series in (i) and (ii) are both $R$.
>
> In (i) the sum starts at $n = 1$ because the derivative of the constant term $c_0$ is $0$. In (ii), $\int c_0\,dx = c_0 x + C_1$ is written $c_0 (x - a) + C$ with $C = C_1 + a c_0$, so that all terms have the same form.
>
> *Stewart: 11.9, Theorem 2*

^thm-77-1

*Stewart does not prove this theorem ("which we won't prove"). For series centered at $0$ (the general case follows with $u = x - a$) it is [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]], proved from [[§24 Uniform Convergence#^def-24-2|uniform convergence]] on closed subintervals, [[§26 Differentiation and Integration of Power Series#^thm-26-1|451 Thm. §26.1]].*

> [!remark]- Connections
> - Rigorous treatment: [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]]; continuity of the sum, [[§26 Differentiation and Integration of Power Series#^cor-26-2|451 Cor. §26.2]]. Why this needs care for general series of functions: [[§23 Power Series#^ex-23-10|451 Ex. §23.10]] (derivatives escape the limit).

> [!remark] Remark: Infinite Sums Behave Like Finite Sums — Here
> **1.** Equations (i) and (ii) can be written
>
> $$
> \text{(iii)}\ \ \frac{d}{dx} \left[ \sum_{n=0}^{\infty} c_n (x - a)^n \right] = \sum_{n=0}^{\infty} \frac{d}{dx} \big[ c_n (x - a)^n \big] \qquad
> \text{(iv)}\ \ \int \left[ \sum_{n=0}^{\infty} c_n (x - a)^n \right] dx = \sum_{n=0}^{\infty} \int c_n (x - a)^n\,dx
> $$
>
> For finite sums, the derivative of a sum is the sum of the derivatives and the integral of a sum is the sum of the integrals. (iii) and (iv) say the same for infinite sums, *provided they are power series*. For other series of functions this can fail (Stewart, Exercise 44).
>
> **2.** The *radius* of convergence stays the same, but the *interval* of convergence may not: the original series may converge at an endpoint where the differentiated series diverges (Exercise 45). For example, $\sum x^n / n^2$ converges at $x = 1$, while its derivative $\sum x^{n-1}/n$ diverges there.

^rem-77-1

> [!example] Example §77.2: Differentiating the Geometric Series
> Express $1/(1 - x)^2$ as a power series by differentiating Equation 1. What is the radius of convergence?
>
> Start from $\dfrac{1}{1 - x} = 1 + x + x^2 + x^3 + \cdots = \displaystyle\sum_{n=0}^{\infty} x^n$. Differentiating each side, with Theorem §77.1(i),
>
> $$
> \frac{1}{(1 - x)^2} = 1 + 2x + 3x^2 + \cdots = \sum_{n=1}^{\infty} n x^{n-1} .
> $$
>
> Replacing $n$ by $n + 1$, this is $\displaystyle\frac{1}{(1 - x)^2} = \sum_{n=0}^{\infty} (n + 1) x^n$. By Theorem §77.1 the radius of convergence of the differentiated series is that of the original series, $R = 1$.
>
> *Stewart: Example 11.9.4*

^ex-77-2

> [!example] Example §77.3: Integrating — the Logarithm and the Arctangent
> **(a)** Find a power series representation for $\ln(1 + x)$ and its radius of convergence.
>
> The derivative of $\ln(1 + x)$ is $1/(1 + x)$, and by Equation 1 with $x$ replaced by $-x$,
>
> $$
> \frac{1}{1 + x} = \frac{1}{1 - (-x)} = 1 - x + x^2 - x^3 + \cdots \qquad |x| < 1 .
> $$
>
> Integrating both sides term by term (Theorem §77.1(ii)),
>
> $$
> \ln(1 + x) = \int \frac{1}{1 + x}\,dx = \int (1 - x + x^2 - x^3 + \cdots)\,dx = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots + C = \sum_{n=1}^{\infty} (-1)^{n-1} \frac{x^n}{n} + C
> $$
>
> for $|x| < 1$. (For $|x| < 1$, $1 + x > 0$, so no absolute value is needed in the logarithm.) To determine $C$, put $x = 0$: $\ln(1 + 0) = C$, so $C = 0$ and
>
> $$
> \ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots = \sum_{n=1}^{\infty} (-1)^{n-1} \frac{x^n}{n} \qquad |x| < 1 .
> $$
>
> The radius of convergence is the same as for the original series: $R = 1$.
>
> **(b)** Find a power series representation for $f(x) = \tan^{-1} x$.
>
> Here $f'(x) = 1/(1 + x^2)$, whose series was found in Example §77.1(a). Integrating term by term,
>
> $$
> \tan^{-1} x = \int \frac{1}{1 + x^2}\,dx = \int (1 - x^2 + x^4 - x^6 + \cdots)\,dx = C + x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \cdots
> $$
>
> Putting $x = 0$ gives $C = \tan^{-1} 0 = 0$. Therefore
>
> $$
> \tan^{-1} x = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \cdots = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{2n + 1} .
> $$
>
> Since the radius of convergence of the series for $1/(1 + x^2)$ is $1$, the radius of convergence of this series is also $1$.
>
> *Stewart: Examples 11.9.5 and 11.9.6*

^ex-77-3

> [!remark]- Connections
> - Rigorous treatment of both series: [[§26 Differentiation and Integration of Power Series#^ex-26-4|451 Ex. §26.4]] (the logarithm) and [[§26 Differentiation and Integration of Power Series#^ex-26-3|451 Ex. §26.3]] (the arctangent), by the same term-by-term integration.

> [!remark] Remark: Gregory's Series and the Endpoints
> The series for $\tan^{-1} x$ is **Gregory's series**, after James Gregory (1638–1675). We have shown that it is valid for $-1 < x < 1$. It is also valid for $x = \pm 1$, though this is not easy to prove (it needs Abel's theorem on the continuity of a power series up to an endpoint where it converges; it is not proved in 451 either). At $x = 1$ it gives the **Leibniz formula**
>
> $$
> \frac{\pi}{4} = 1 - \frac13 + \frac15 - \frac17 + \cdots
> $$
>
> In the same way the series for $\ln(1 + x)$ at $x = 1$ gives $\ln 2 = 1 - \frac12 + \frac13 - \frac14 + \cdots$, the sum of the alternating harmonic series used in [[§73 Alternating Series and Absolute Convergence#^rem-73-3|§73]].

^rem-77-2

> [!example] Example §77.4: Integrating a Function with No Simple Antiderivative
> **(a)** Evaluate $\int [1/(1 + x^7)]\,dx$ as a power series.
> **(b)** Use (a) to approximate $\int_0^{0.5} [1/(1 + x^7)]\,dx$ correct to within $10^{-7}$.
>
> **(a)** First express the integrand as a power series, replacing $x$ by $-x^7$ in Equation 1:
>
> $$
> \frac{1}{1 + x^7} = \frac{1}{1 - (-x^7)} = \sum_{n=0}^{\infty} (-x^7)^n = \sum_{n=0}^{\infty} (-1)^n x^{7n} = 1 - x^7 + x^{14} - \cdots
> $$
>
> Now integrate term by term:
>
> $$
> \int \frac{1}{1 + x^7}\,dx = \int \sum_{n=0}^{\infty} (-1)^n x^{7n}\,dx = C + \sum_{n=0}^{\infty} (-1)^n \frac{x^{7n+1}}{7n + 1} = C + x - \frac{x^8}{8} + \frac{x^{15}}{15} - \frac{x^{22}}{22} + \cdots
> $$
>
> This series converges for $|-x^7| < 1$, that is, for $|x| < 1$.
>
> **(b)** In the Fundamental Theorem of Calculus any antiderivative will do, so use the one from (a) with $C = 0$:
>
> $$
> \int_0^{0.5} \frac{1}{1 + x^7}\,dx = \left[ x - \frac{x^8}{8} + \frac{x^{15}}{15} - \frac{x^{22}}{22} + \cdots \right]_0^{1/2} = \frac12 - \frac{1}{8 \cdot 2^8} + \frac{1}{15 \cdot 2^{15}} - \frac{1}{22 \cdot 2^{22}} + \cdots + \frac{(-1)^n}{(7n + 1) 2^{7n+1}} + \cdots
> $$
>
> This infinite series is the exact value of the integral. It is alternating, and its terms $1/[(7n+1) 2^{7n+1}]$ decrease to $0$, so by the Alternating Series Estimation Theorem, if we stop after the term with $n = 3$, the error is smaller than the term with $n = 4$:
>
> $$
> \frac{1}{29 \cdot 2^{29}} \approx 6.4 \times 10^{-11} .
> $$
>
> So
>
> $$
> \int_0^{0.5} \frac{1}{1 + x^7}\,dx \approx \frac12 - \frac{1}{8 \cdot 2^8} + \frac{1}{15 \cdot 2^{15}} - \frac{1}{22 \cdot 2^{22}} \approx 0.49951374 .
> $$
>
> Integrating $1/(1 + x^7)$ in closed form by hand is very difficult, and computer algebra systems return complicated answers; the series is much easier to use.
>
> *Stewart: Example 11.9.7*

^ex-77-4

## Functions Defined by Power Series

Some of the most important functions in the sciences are *defined* by power series and cannot be expressed in terms of elementary functions. Many arise as solutions of differential equations. An example is the class of **Bessel functions**, named after Friedrich Bessel (1784–1846), who met them in solving Kepler's equation for planetary motion; they describe, for instance, the temperature in a circular plate and the vibrations of a drumhead.

> [!example] Example §77.5: The Bessel Function of Order 0
> The Bessel function of order $0$ is defined by
>
> $$
> J_0(x) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{2^{2n} (n!)^2} .
> $$
>
> **(a)** Find the domain of $J_0$. **(b)** Find the derivative of $J_0$.
>
> **(a)** Let $a_n = (-1)^n x^{2n} / [2^{2n} (n!)^2]$. Then
>
> $$
> \left| \frac{a_{n+1}}{a_n} \right| = \left| \frac{(-1)^{n+1} x^{2(n+1)}}{2^{2(n+1)} [(n+1)!]^2} \cdot \frac{2^{2n} (n!)^2}{(-1)^n x^{2n}} \right| = \frac{x^{2n+2}}{2^{2n+2} (n+1)^2 (n!)^2} \cdot \frac{2^{2n} (n!)^2}{x^{2n}} = \frac{x^2}{4(n+1)^2} \to 0 < 1
> $$
>
> for all $x$. By the Ratio Test the series converges for all $x$: the domain of $J_0$ is $(-\infty, \infty) = \mathbb{R}$.
>
> **(b)** By Theorem §77.1, $J_0$ is differentiable for all $x$, and term by term (the $n = 0$ term is the constant $1$):
>
> $$
> J_0'(x) = \sum_{n=0}^{\infty} \frac{d}{dx} \frac{(-1)^n x^{2n}}{2^{2n} (n!)^2} = \sum_{n=1}^{\infty} \frac{(-1)^n 2n x^{2n-1}}{2^{2n} (n!)^2} .
> $$
>
> **Partial sums.** $J_0(x) = \lim_{n \to \infty} s_n(x)$ with $s_n(x) = \sum_{i=0}^{n} \frac{(-1)^i x^{2i}}{2^{2i} (i!)^2}$; since $2^{2i}(i!)^2 = 1, 4, 64, 2304, 147456$ for $i = 0, \ldots, 4$,
>
> $$
> s_0(x) = 1, \quad s_1(x) = 1 - \frac{x^2}{4}, \quad s_2(x) = 1 - \frac{x^2}{4} + \frac{x^4}{64}, \quad s_3(x) = s_2(x) - \frac{x^6}{2304}, \quad s_4(x) = s_3(x) + \frac{x^8}{147456} .
> $$
>
> These polynomials approximate $J_0$, better as more terms are included. The graph of $J_0$ is an oscillation with decreasing amplitude, starting from $J_0(0) = 1$.
>
> *Stewart: Example 11.9.8*

^ex-77-5

> [!remark]- Connections
> - PDE version: [[§45★ Bessel's Equation#^def-45-2|341 Def. §45.2]] ($J_0$ and the other $J_\mu$ as power-series solutions of Bessel's equation, found by the method of Frobenius), with this series, the value $J_0(1)$ and $J_0' = -J_1$ in [[§45★ Bessel's Equation#^ex-45-1|341 Ex. §45.1]] and [[§45★ Bessel's Equation#^thm-45-7|341 Thm. §45.7]].
