---
type: section
subject: "[[Calculus]]"
chapter: 11
section: 91
stewart: "11.10"
aliases: ["Stewart 11.10 (cont.)"]
tags: [calculus]
---
← [[§90 Taylor and Maclaurin Series]] · ↑ [[· 11 Sequences, Series, and Power Series]] · [[§92 Applications of Taylor Polynomials]] →

*Stewart, Section 11.10.*

Taylor's Inequality ([[§90 Taylor and Maclaurin Series#^thm-90-4|Theorem §90.4]]) proves the Maclaurin series of $\sin x$ and $\cos x$ for all $x$, and the binomial series of $(1 + x)^k$ for $|x| < 1$. Because the representation is unique, new Taylor series can then be produced from old ones by substitution, multiplication, differentiation and integration, and used to integrate functions like $e^{-x^2}$, to evaluate limits, and to sum series.

## Taylor Series of Important Functions

> [!theorem] Theorem §107.1: Sine
> $$
> \sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!} \qquad \text{for all } x . \qquad (15)
> $$
>
> *Stewart: 11.10, Equation 15 (Example 11.10.5)*

^thm-91-1

> [!proof]+ Proof
> **The Maclaurin series.** Arrange the computation in two columns:
>
> $$
> \begin{aligned}
> f(x) &= \sin x & f(0) &= 0 \\
> f'(x) &= \cos x & f'(0) &= 1 \\
> f''(x) &= -\sin x & f''(0) &= 0 \\
> f'''(x) &= -\cos x & f'''(0) &= -1 \\
> f^{(4)}(x) &= \sin x & f^{(4)}(0) &= 0
> \end{aligned}
> $$
>
> The derivatives repeat in a cycle of four, so the Maclaurin series is
>
> $$
> f(0) + \frac{f'(0)}{1!} x + \frac{f''(0)}{2!} x^2 + \frac{f'''(0)}{3!} x^3 + \cdots = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!} .
> $$
>
> **It represents $\sin x$.** $f^{(n+1)}(x)$ is $\pm\sin x$ or $\pm\cos x$, so $|f^{(n+1)}(x)| \le 1$ for all $x$, and we can take $M = 1$ in Taylor's Inequality:
>
> $$
> |R_n(x)| \le \frac{M}{(n+1)!} |x^{n+1}| = \frac{|x|^{n+1}}{(n+1)!} . \qquad (14)
> $$
>
> By (10) the right side tends to $0$ as $n \to \infty$, so $|R_n(x)| \to 0$ by the Squeeze Theorem, and $R_n(x) \to 0$. By [[§90 Taylor and Maclaurin Series#^thm-90-3|Theorem §90.3]], $\sin x$ is equal to the sum of its Maclaurin series, for all $x$.

^pf-91-1

*Uses:* [[§90 Taylor and Maclaurin Series#^thm-90-4|§90.4]], [[§90 Taylor and Maclaurin Series#^prop-90-5|§90.5]], [[§90 Taylor and Maclaurin Series#^thm-90-3|§90.3]], [[§80 Sequences#^thm-80-4|§80.4]], [[§19 Derivatives of Trigonometric Functions#^thm-19-1|§19.1]], [[§19 Derivatives of Trigonometric Functions#^thm-19-2|§19.2]] (derivatives of sine and cosine)

![[m233-78-1.svg]]
*$\sin x$ (black) and its Maclaurin polynomials $T_1(x) = x$, $T_3(x) = x - \frac{x^3}{3!}$, $T_5$ and $T_9$. Each polynomial follows the sine curve on a larger interval around $0$ before it breaks away: for fixed $x$ the error $|R_n(x)| \le |x|^{n+1}/(n+1)!$ tends to $0$, but more slowly for larger $|x|$.*

> [!theorem] Theorem §107.2: Cosine
> $$
> \cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!} \qquad \text{for all } x . \qquad (16)
> $$
>
> *Stewart: 11.10, Equation 16 (Example 11.10.6)*

^thm-91-2

> [!proof]+ Proof
> One could proceed directly as for sine, but it is easier to differentiate the Maclaurin series for $\sin x$ term by term ([[§89 Representations of Functions as Power Series#^thm-89-1|Theorem §89.1]]):
>
> $$
> \cos x = \frac{d}{dx} (\sin x) = \frac{d}{dx} \left( x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots \right) = 1 - \frac{3x^2}{3!} + \frac{5x^4}{5!} - \frac{7x^6}{7!} + \cdots = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots
> $$
>
> since $(2n+1)/(2n+1)! = 1/(2n)!$. By [[§89 Representations of Functions as Power Series#^thm-89-1|Theorem §89.1]] the differentiated series converges to the derivative of $\sin x$, namely $\cos x$, and its radius of convergence is unchanged, so it converges for all $x$.

^pf-91-2

*Uses:* [[§91 Taylor Series of Important Functions#^thm-91-1|§91.1]], [[§89 Representations of Functions as Power Series#^thm-89-1|§89.1]]

> [!remark]- Connections
> - Rigorous treatment of (11), (15) and (16): [[§31 Taylor's Theorem#^ex-31-1|451 Ex. §31.1]] (cosine and $e^x$ through the remainder, as here). In 451 the series can instead serve as *definitions* of sine and cosine: [[§26 Differentiation and Integration of Power Series#^ex-26-8|451 Ex. §26.8]].
> - See also: [[§64 Complex Numbers#^rem-64-1|235 Remark: Euler's Formula]] ($e^{i\varphi} = \cos\varphi + i\sin\varphi$ by splitting the series (11) at $x = i\varphi$ into the series (16) and (15)), and [[§46 Applications to Differential Equations#^def-46-3|235 Def. §46.3]] (the complex exponential $e^{(a+bi)t} = e^{at}(\cos bt + i\sin bt)$, used for complex eigenvalues of $\mathbf{x}' = A\mathbf{x}$).
> - ODE version: [[§19 Complex Roots of the Characteristic Equation#^def-19-1|331 Def. §19.1]] (Euler's formula, motivated by these three series in [[§19 Complex Roots of the Characteristic Equation#^rem-19-1|331 Remark: Where Euler's Formula Comes From]]) and [[§39★ Fundamental Matrices#^def-39-3|331 Def. §39.3]] (the matrix exponential, the series (11) with $\mathbf{A}t$ in place of $x$, which converges and satisfies $\Phi' = \mathbf{A}\Phi$ by [[§39★ Fundamental Matrices#^thm-39-3|331 Thm. §39.3]]).
> - Complex-variables version: [[§64 Examples (Proof of Taylor's Theorem)#^prop-64-1|342 Prop. §64.1]] (the series (11), (15) and (16) for complex $z$, proved by [[Taylor's Theorem for Analytic Functions|Taylor's theorem for analytic functions]]); splitting (11) at $z = i\theta$ gives Euler's formula, [[§7 Exponential Form#^def-7-4|342 Def. §7.4]].

These series, found by Newton by other methods, say that everything about $e^x$, $\sin x$ and $\cos x$ is determined by their derivatives at the single number $0$.

> [!definition] Definition §107.1: Binomial Coefficients
> For any real number $k$ and integer $n \ge 0$, the **binomial coefficients** are
>
> $$
> \binom{k}{n} = \frac{k(k-1)(k-2)\cdots(k - n + 1)}{n!} , \qquad \binom{k}{0} = 1 .
> $$
>
> *Stewart: 11.10 (text)*

^def-91-1

> [!definition] Definition §107.2: Binomial Series
> The **binomial series** is the Maclaurin series of $(1 + x)^k$, which is $\sum_{n=0}^{\infty} \binom{k}{n} x^n$ ([[§91 Taylor Series of Important Functions#^thm-91-3|Theorem §91.3]]).
>
> *Stewart: 11.10 (text)*

^def-91-2

> [!theorem] Theorem §107.3: The Binomial Series
> If $k$ is any real number and $|x| < 1$, then
>
> $$
> (1 + x)^k = \sum_{n=0}^{\infty} \binom{k}{n} x^n = 1 + kx + \frac{k(k-1)}{2!} x^2 + \frac{k(k-1)(k-2)}{3!} x^3 + \cdots \qquad (17)
> $$
>
> If $k$ is a nonnegative integer, $\binom{k}{n} = 0$ for $n > k$ (the numerator contains the factor $k - k$), the series terminates, and (17) is the ordinary Binomial Theorem ([[Binomial Theorem|250 Thm. §12.10]]). At the endpoints the series converges at $x = 1$ if $-1 < k \le 0$, and at both endpoints if $k \ge 0$.
>
> *Stewart: 11.10, The Binomial Series 17 (Example 11.10.8)*

^thm-91-3

> [!proof]+ Proof
> **The Maclaurin series** (Stewart's Example 8). Computing derivatives,
>
> $$
> \begin{aligned}
> f(x) &= (1 + x)^k & f(0) &= 1 \\
> f'(x) &= k(1 + x)^{k-1} & f'(0) &= k \\
> f''(x) &= k(k-1)(1 + x)^{k-2} & f''(0) &= k(k-1) \\
> f'''(x) &= k(k-1)(k-2)(1 + x)^{k-3} & f'''(0) &= k(k-1)(k-2) \\
> f^{(n)}(x) &= k(k-1)\cdots(k - n + 1)(1 + x)^{k-n} & f^{(n)}(0) &= k(k-1)\cdots(k - n + 1)
> \end{aligned}
> $$
>
> so the Maclaurin series of $(1 + x)^k$ is $\displaystyle\sum_{n=0}^{\infty} \frac{k(k-1)\cdots(k - n + 1)}{n!} x^n = \sum_{n=0}^{\infty} \binom{k}{n} x^n$.
>
> **Radius of convergence.** If $k$ is a nonnegative integer the series is finite. Otherwise no term is $0$, and with $a_n = \binom{k}{n} x^n$,
>
> $$
> \left| \frac{a_{n+1}}{a_n} \right| = \left| \frac{k(k-1)\cdots(k - n + 1)(k - n) x^{n+1}}{(n+1)!} \cdot \frac{n!}{k(k-1)\cdots(k - n + 1) x^n} \right| = \frac{|k - n|}{n + 1} |x| = \frac{\left| 1 - \dfrac kn \right|}{1 + \dfrac1n} |x| \to |x| .
> $$
>
> By the Ratio Test the series converges if $|x| < 1$ and diverges if $|x| > 1$.
>
> **The sum is $(1 + x)^k$.** Stewart notes that showing $R_n(x) \to 0$ is quite difficult and outlines an easier proof in Exercise 97, which we carry out. Let $g(x) = \sum_{n=0}^{\infty} \binom{k}{n} x^n$ for $|x| < 1$. By [[§89 Representations of Functions as Power Series#^thm-89-1|Theorem §89.1]], $g'(x) = \sum_{n=1}^{\infty} n \binom{k}{n} x^{n-1}$, so
>
> $$
> (1 + x) g'(x) = \sum_{n=0}^{\infty} (n+1) \binom{k}{n+1} x^n + \sum_{n=0}^{\infty} n \binom{k}{n} x^n = \sum_{n=0}^{\infty} \left[ (k - n) \binom{k}{n} + n \binom{k}{n} \right] x^n = k\, g(x) ,
> $$
>
> using $(n+1)\binom{k}{n+1} = (k - n)\binom{k}{n}$, which is the definition of $\binom{k}{n+1}$. Now let $h(x) = (1 + x)^{-k} g(x)$. Then
>
> $$
> h'(x) = -k(1 + x)^{-k-1} g(x) + (1 + x)^{-k} g'(x) = (1 + x)^{-k-1} \big[ (1 + x) g'(x) - k\,g(x) \big] = 0 ,
> $$
>
> so $h$ is constant on $(-1, 1)$ ([[§29 Rolle's Theorem and the Mean Value Theorem#^thm-29-3|Theorem §29.3]]), and $h(x) = h(0) = g(0) = 1$. Hence $g(x) = (1 + x)^k$ for $|x| < 1$.
>
> (The endpoint behavior stated in the theorem is quoted from Stewart without proof.)

^pf-91-3

*Uses:* [[§90 Taylor and Maclaurin Series#^def-90-1|Def. §90.1]], [[§91 Taylor Series of Important Functions#^def-91-1|Def. §91.1]], [[§91 Taylor Series of Important Functions#^def-91-2|Def. §91.2]], [[§86 The Ratio and Root Tests#^thm-86-1|§86.1]], [[§89 Representations of Functions as Power Series#^thm-89-1|§89.1]], [[§29 Rolle's Theorem and the Mean Value Theorem#^thm-29-3|§29.3]] (a function with zero derivative is constant)

> [!remark] Remark: Important Maclaurin Series
> For future reference (Stewart's Table 1), the Maclaurin series found here and in [[§89 Representations of Functions as Power Series|§89]], with their radii of convergence:
>
> $$
> \begin{aligned}
> \frac{1}{1 - x} &= \sum_{n=0}^{\infty} x^n = 1 + x + x^2 + x^3 + \cdots & R &= 1 \\
> e^x &= \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots & R &= \infty \\
> \sin x &= \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots & R &= \infty \\
> \cos x &= \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots & R &= \infty \\
> \tan^{-1} x &= \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{2n+1} = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \cdots & R &= 1 \\
> \ln(1 + x) &= \sum_{n=1}^{\infty} (-1)^{n-1} \frac{x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots & R &= 1 \\
> (1 + x)^k &= \sum_{n=0}^{\infty} \binom{k}{n} x^n = 1 + kx + \frac{k(k-1)}{2!} x^2 + \frac{k(k-1)(k-2)}{3!} x^3 + \cdots & R &= 1
> \end{aligned}
> $$

^rem-91-3

## New Taylor Series from Old

By [[§90 Taylor and Maclaurin Series#^cor-90-2|Corollary §90.2]], however a power series representation of $f$ is obtained, it is the Taylor series of $f$. So new Taylor series can be found by manipulating the series in the table instead of using the coefficient formula. As in [[§89 Representations of Functions as Power Series|§89]], we can replace $x$ by an expression $c x^m$, multiply or divide by such an expression, and differentiate or integrate term by term. Series can also be added and subtracted ([[§82 Series#^thm-82-6|Theorem §82.6]]), multiplied and divided.

> [!theorem] Theorem §107.4: Multiplying and Dividing Power Series
> If $f(x) = \sum c_n x^n$ and $g(x) = \sum b_n x^n$ both converge for $|x| < R$, and the series are multiplied as if they were polynomials, the resulting series also converges for $|x| < R$ and represents $f(x) g(x)$. For division, if $b_0 \ne 0$, the series obtained by long division converges to $f(x)/g(x)$ for sufficiently small $|x|$.
>
> *Stewart: 11.10 (text)*

^thm-91-4

*Stewart states this without proof ("there is a theorem which states that"); it is not proved in 451.*

> [!remark]- Connections
> - Complex-variables version: [[§73★ Multiplication and Division of Power Series#^thm-73-2|342 Thm. §73.2]] (the Cauchy product converges to $fg$) and [[§73★ Multiplication and Division of Power Series#^prop-73-3|342 Prop. §73.3]] (division), both proved there.

> [!example] Example §107.1: Substituting, Multiplying, Recognizing
> **(a)** Find the Maclaurin series and radius of convergence of $f(x) = 1/\sqrt{4 - x}$.
>
> Rewrite $f$ so that the binomial series applies:
>
> $$
> \frac{1}{\sqrt{4 - x}} = \frac{1}{\sqrt{4\left( 1 - \dfrac x4 \right)}} = \frac{1}{2\sqrt{1 - \dfrac x4}} = \frac12 \left( 1 - \frac x4 \right)^{-1/2} .
> $$
>
> Use the binomial series with $k = -\frac12$ and $x$ replaced by $-x/4$:
>
> $$
> \frac{1}{\sqrt{4 - x}} = \frac12 \sum_{n=0}^{\infty} \binom{-\frac12}{n} \left( -\frac x4 \right)^n = \frac12 \left[ 1 + \left( -\frac12 \right)\left( -\frac x4 \right) + \frac{\left( -\frac12 \right)\left( -\frac32 \right)}{2!} \left( -\frac x4 \right)^2 + \frac{\left( -\frac12 \right)\left( -\frac32 \right)\left( -\frac52 \right)}{3!} \left( -\frac x4 \right)^3 + \cdots \right] .
> $$
>
> In the $n$th term, the $n$ factors $-\frac12, -\frac32, \ldots, -\frac{2n-1}{2}$ give $(-1)^n \frac{1 \cdot 3 \cdots (2n-1)}{2^n}$, and $(-x/4)^n = (-1)^n x^n / 4^n$; the signs cancel and $2^n 4^n = 8^n$. So
>
> $$
> \frac{1}{\sqrt{4 - x}} = \frac12 \left[ 1 + \frac18 x + \frac{1 \cdot 3}{2!\,8^2} x^2 + \frac{1 \cdot 3 \cdot 5}{3!\,8^3} x^3 + \cdots + \frac{1 \cdot 3 \cdot 5 \cdots (2n-1)}{n!\,8^n} x^n + \cdots \right] .
> $$
>
> By (17) this converges when $|-x/4| < 1$, that is, $|x| < 4$: $R = 4$.
>
> **(b)** Find the Maclaurin series for $x \cos x$ and for $\ln(1 + 3x^2)$.
>
> Multiplying the series for $\cos x$ by $x$:
>
> $$
> x \cos x = x \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!} = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n)!} \qquad \text{for all } x .
> $$
>
> Replacing $x$ by $3x^2$ in the series for $\ln(1 + x)$:
>
> $$
> \ln(1 + 3x^2) = \sum_{n=1}^{\infty} (-1)^{n-1} \frac{(3x^2)^n}{n} = \sum_{n=1}^{\infty} (-1)^{n-1} \frac{3^n x^{2n}}{n} .
> $$
>
> This converges for $|3x^2| < 1$, that is, $|x| < 1/\sqrt3$: $R = 1/\sqrt3$.
>
> **(c)** Find the function represented by $\displaystyle\sum_{n=0}^{\infty} (-1)^n \frac{2^n x^n}{n!}$.
>
> $\displaystyle\sum_{n=0}^{\infty} (-1)^n \frac{2^n x^n}{n!} = \sum_{n=0}^{\infty} \frac{(-2x)^n}{n!}$ is the series for $e^x$ with $x$ replaced by $-2x$, so it represents $e^{-2x}$.
>
> **(d)** Find the sum of $\dfrac{1}{1 \cdot 2} - \dfrac{1}{2 \cdot 2^2} + \dfrac{1}{3 \cdot 2^3} - \dfrac{1}{4 \cdot 2^4} + \cdots$.
>
> In sigma notation, $\displaystyle\sum_{n=1}^{\infty} (-1)^{n-1} \frac{1}{n \cdot 2^n} = \sum_{n=1}^{\infty} (-1)^{n-1} \frac{\left( \frac12 \right)^n}{n}$, which is the series for $\ln(1 + x)$ at $x = \frac12$ (inside $|x| < 1$). So the sum is $\ln\left( 1 + \frac12 \right) = \ln\frac32$.
>
> *Stewart: Examples 11.10.9–11.10.12*

^ex-91-1

> [!example] Example §107.2: Integrals and Limits by Series
> **(a)** Evaluate $\int e^{-x^2}\,dx$ as an infinite series, and **(b)** evaluate $\int_0^1 e^{-x^2}\,dx$ correct to within an error of $0.001$.
>
> $e^{-x^2}$ has no elementary antiderivative ([[§55 Strategy for Integration#^thm-55-2|Theorem §55.2]]); following Newton, expand and integrate term by term. Replacing $x$ by $-x^2$ in the series for $e^x$, for all $x$,
>
> $$
> e^{-x^2} = \sum_{n=0}^{\infty} \frac{(-x^2)^n}{n!} = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{n!} = 1 - \frac{x^2}{1!} + \frac{x^4}{2!} - \frac{x^6}{3!} + \cdots
> $$
>
> **(a)** Integrating term by term,
>
> $$
> \int e^{-x^2}\,dx = C + x - \frac{x^3}{3 \cdot 1!} + \frac{x^5}{5 \cdot 2!} - \frac{x^7}{7 \cdot 3!} + \cdots + (-1)^n \frac{x^{2n+1}}{(2n+1)\,n!} + \cdots ,
> $$
>
> which converges for all $x$ because the series for $e^{-x^2}$ does.
>
> **(b)** By the Fundamental Theorem of Calculus, with $C = 0$,
>
> $$
> \int_0^1 e^{-x^2}\,dx = \left[ x - \frac{x^3}{3 \cdot 1!} + \frac{x^5}{5 \cdot 2!} - \frac{x^7}{7 \cdot 3!} + \frac{x^9}{9 \cdot 4!} - \cdots \right]_0^1 = 1 - \frac13 + \frac{1}{10} - \frac{1}{42} + \frac{1}{216} - \cdots \approx 0.7475 ,
> $$
>
> stopping after $\frac{1}{216}$. The series is alternating with decreasing terms, so by the Alternating Series Estimation Theorem the error is less than the next term, $\dfrac{1}{11 \cdot 5!} = \dfrac{1}{1320} < 0.001$.
>
> **(c)** Evaluate $\displaystyle\lim_{x \to 0} \frac{e^x - 1 - x}{x^2}$.
>
> By the Maclaurin series for $e^x$,
>
> $$
> \frac{e^x - 1 - x}{x^2} = \frac{\left( 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots \right) - 1 - x}{x^2} = \frac{1}{x^2} \left( \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots \right) = \frac{1}{2!} + \frac{x}{3!} + \frac{x^2}{4!} + \cdots
> $$
>
> for $x \ne 0$. The right side is a power series, hence continuous ([[§89 Representations of Functions as Power Series#^thm-89-1|Theorem §89.1]]), so
>
> $$
> \lim_{x \to 0} \frac{e^x - 1 - x}{x^2} = \frac{1}{2!} + 0 + 0 + \cdots = \frac12 .
> $$
>
> ([[§31 Indeterminate Forms and L'Hospital's Rule#^thm-31-2|L'Hospital's Rule]], applied twice, gives the same.)
>
> *Stewart: Examples 11.10.13 and 11.10.14*

^ex-91-2

> [!example] Example §107.3: Multiplying and Dividing Series
> Find the first three nonzero terms in the Maclaurin series for **(a)** $e^x \sin x$ and **(b)** $\tan x$.
>
> **(a)** Multiply the series, collecting like terms as for polynomials ([[§91 Taylor Series of Important Functions#^thm-91-4|Theorem §91.4]]):
>
> $$
> e^x \sin x = \left( 1 + x + \tfrac12 x^2 + \tfrac16 x^3 + \cdots \right)\left( x - \tfrac16 x^3 + \cdots \right) .
> $$
>
> Multiplying by $x$ gives $x + x^2 + \frac12 x^3 + \frac16 x^4 + \cdots$, and by $-\frac16 x^3$ gives $-\frac16 x^3 - \frac16 x^4 - \cdots$. Adding, the $x^3$ coefficient is $\frac12 - \frac16 = \frac13$:
>
> $$
> e^x \sin x = x + x^2 + \tfrac13 x^3 + \cdots
> $$
>
> **(b)** $\tan x = \dfrac{\sin x}{\cos x} = \dfrac{x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots}{1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots}$. Divide as in long division of polynomials, by $1 - \frac12 x^2 + \frac{1}{24} x^4 - \cdots$:
> - First quotient term $x$: subtract $x\left( 1 - \frac12 x^2 + \frac{1}{24} x^4 \right) = x - \frac12 x^3 + \frac{1}{24} x^5$ from $x - \frac16 x^3 + \frac{1}{120} x^5$, leaving $\frac13 x^3 - \frac{1}{30} x^5 + \cdots$ (as $-\frac16 + \frac12 = \frac13$ and $\frac{1}{120} - \frac{1}{24} = -\frac{1}{30}$).
> - Next term $\frac13 x^3$: subtract $\frac13 x^3 - \frac16 x^5 + \cdots$, leaving $\left( -\frac{1}{30} + \frac16 \right) x^5 = \frac{2}{15} x^5 + \cdots$.
> - Next term $\frac{2}{15} x^5$.
>
> $$
> \tan x = x + \tfrac13 x^3 + \tfrac{2}{15} x^5 + \cdots
> $$
>
> *Stewart: Example 11.10.15*

^ex-91-3
