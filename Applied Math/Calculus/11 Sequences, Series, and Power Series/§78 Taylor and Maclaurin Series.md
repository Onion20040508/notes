---
type: section
subject: "[[Calculus]]"
chapter: 11
section: 78
stewart: "11.10"
aliases: ["Stewart 11.10"]
tags: [calculus]
---
← [[§77 Representations of Functions as Power Series]] · ↑ [[· 11 Sequences, Series, and Power Series]] · [[§79 Applications of Taylor Polynomials]] →

*Stewart, Section 11.10.*

If a function has a power series representation at $a$, its coefficients are forced: $c_n = f^{(n)}(a)/n!$. So there is only one candidate, the Taylor series of $f$, and the question becomes when $f$ actually equals it. That happens exactly when the remainder $R_n(x) = f(x) - T_n(x)$ tends to $0$, and Taylor's Inequality bounds the remainder by the size of the next derivative. This proves the Maclaurin series of $e^x$, $\sin x$ and $\cos x$ for all $x$, and the binomial series of $(1 + x)^k$ for $|x| < 1$. Because the representation is unique, new Taylor series can then be produced from old ones by substitution, multiplication, differentiation and integration, and used to integrate functions like $e^{-x^2}$, to evaluate limits, and to sum series.

## Definitions of Taylor Series and Maclaurin Series

> [!theorem] Theorem §78.1: The Coefficients of a Power Series
> If $f$ has a power series representation (expansion) at $a$, that is, if
>
> $$
> f(x) = \sum_{n=0}^{\infty} c_n (x - a)^n \qquad |x - a| < R ,
> $$
>
> then its coefficients are given by the formula
>
> $$
> c_n = \frac{f^{(n)}(a)}{n!} .
> $$
>
> (With the conventions $0! = 1$ and $f^{(0)} = f$, this includes $n = 0$.)
>
> *Stewart: 11.10, Theorem 5*

^thm-78-1

> [!proof]+ Proof
> Write the series out:
>
> $$
> f(x) = c_0 + c_1 (x - a) + c_2 (x - a)^2 + c_3 (x - a)^3 + c_4 (x - a)^4 + \cdots \qquad |x - a| < R . \qquad (1)
> $$
>
> Putting $x = a$, all terms after the first are $0$: $f(a) = c_0$. By [[§77 Representations of Functions as Power Series#^thm-77-1|Theorem §77.1]] we can differentiate term by term on $|x - a| < R$:
>
> $$
> f'(x) = c_1 + 2c_2 (x - a) + 3c_3 (x - a)^2 + 4c_4 (x - a)^3 + \cdots \qquad (2)
> $$
>
> and $x = a$ gives $f'(a) = c_1$. Differentiating (2),
>
> $$
> f''(x) = 2c_2 + 2 \cdot 3 c_3 (x - a) + 3 \cdot 4 c_4 (x - a)^2 + \cdots \qquad (3)
> $$
>
> so $f''(a) = 2c_2$. Once more,
>
> $$
> f'''(x) = 2 \cdot 3 c_3 + 2 \cdot 3 \cdot 4 c_4 (x - a) + 3 \cdot 4 \cdot 5 c_5 (x - a)^2 + \cdots \qquad (4)
> $$
>
> so $f'''(a) = 2 \cdot 3 c_3 = 3!\,c_3$. In general (Stewart: "by now you can see the pattern"), Theorem §77.1 applied $k$ times gives, for $|x - a| < R$,
>
> $$
> f^{(k)}(x) = \sum_{n=k}^{\infty} n(n-1)\cdots(n-k+1)\, c_n (x - a)^{n-k} ,
> $$
>
> and at $x = a$ only the term $n = k$ survives: $f^{(k)}(a) = k(k-1)\cdots 1 \cdot c_k = k!\,c_k$. Solving for $c_k$ gives the formula.

^pf-78-1

*Uses:* [[§77 Representations of Functions as Power Series#^thm-77-1|§77.1]]

Substituting this formula for $c_n$ back into the series: *if* $f$ has a power series expansion at $a$, then it must be of the following form.

> [!definition] Definition §78.1: Taylor Series; Maclaurin Series
> The **Taylor series of the function $f$ at $a$** (or **about $a$**, or **centered at $a$**) is
>
> $$
> \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x - a)^n = f(a) + \frac{f'(a)}{1!} (x - a) + \frac{f''(a)}{2!} (x - a)^2 + \frac{f'''(a)}{3!} (x - a)^3 + \cdots \qquad (6)
> $$
>
> For the special case $a = 0$ it is called the **Maclaurin series** of $f$:
>
> $$
> \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n = f(0) + \frac{f'(0)}{1!} x + \frac{f''(0)}{2!} x^2 + \cdots \qquad (7)
> $$
>
> The names honor Brook Taylor (1685–1731) and Colin Maclaurin (1698–1746), although the idea goes back to Newton, Gregory and Johann Bernoulli.
>
> *Stewart: 11.10, Equations 6 and 7 (text)*

^def-78-1

> [!remark]- Connections
> - Rigorous treatment: [[§31 Taylor's Theorem#^def-31-1|451 Def. §31.1]]. That a Taylor series may converge to something other than $f$: [[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]] ($e^{-1/x^2}$, Stewart's Exercise 96).

> [!theorem] Corollary §78.2: Uniqueness of Power Series Representations
> The power series representation at $a$ of a function is unique, regardless of how it is found: if $f(x) = \sum c_n (x - a)^n$ for $|x - a| < R$, the series is the Taylor series of $f$ at $a$. In particular, all the power series representations of [[§77 Representations of Functions as Power Series|§77]] are Taylor series of the functions they represent.
>
> *Stewart: 11.10 (text, Note 2)*

^cor-78-2

> [!proof]+ Proof
> By Theorem §78.1, $c_n = f^{(n)}(a)/n!$ for every $n$, so the coefficients are determined by $f$ alone.

^pf-78-2

*Uses:* [[§78 Taylor and Maclaurin Series#^thm-78-1|§78.1]]

> [!remark]- Connections
> - Complex-variables version: [[§72★ Uniqueness of Series Representations#^thm-72-1|342 Thm. §72.1]] (a power series that converges to $f$ in a disk is the Taylor series of $f$).

> [!remark] Remark: A Taylor Series Need Not Equal Its Function
> Theorem §78.1 says: *if* $f$ has a power series representation about $a$, then that series is the Taylor series. It does not say that every function equals the sum of its Taylor series. There are functions with derivatives of all orders that are not equal to the sum of their Taylor series, such as $f(x) = e^{-1/x^2}$ for $x \ne 0$, $f(0) = 0$ (Stewart's Exercise 96): all its derivatives at $0$ are $0$, so its Maclaurin series is $0$.

^rem-78-1

> [!example] Example §78.1: Maclaurin Series from the Definition
> **(a)** $f(x) = 1/(1 - x)$ has the power series representation $\sum_{n=0}^{\infty} x^n$ for $|x| < 1$ ([[§77 Representations of Functions as Power Series#^def-77-1|Definition §77.1]]). By Theorem §78.1 this must be its Maclaurin series. To confirm:
>
> $$
> f(x) = \frac{1}{1 - x}, \quad f'(x) = \frac{1}{(1 - x)^2}, \quad f''(x) = \frac{1 \cdot 2}{(1 - x)^3}, \quad f'''(x) = \frac{1 \cdot 2 \cdot 3}{(1 - x)^4}, \quad \ldots, \quad f^{(n)}(x) = \frac{n!}{(1 - x)^{n+1}} ,
> $$
>
> so $f^{(n)}(0) = n!$, $c_n = n!/n! = 1$, and by (7) the Maclaurin series is $\sum_{n=0}^{\infty} x^n$.
>
> **(b)** Find the Maclaurin series of $f(x) = e^x$ and its radius of convergence.
>
> $f^{(n)}(x) = e^x$, so $f^{(n)}(0) = e^0 = 1$ for all $n$. The Maclaurin series is
>
> $$
> \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots
> $$
>
> With $a_n = x^n/n!$,
>
> $$
> \left| \frac{a_{n+1}}{a_n} \right| = \left| \frac{x^{n+1}}{(n+1)!} \cdot \frac{n!}{x^n} \right| = \frac{|x|}{n + 1} \to 0 < 1 ,
> $$
>
> so by the Ratio Test the series converges for all $x$: $R = \infty$.
>
> *Stewart: Examples 11.10.1 and 11.10.2*

^ex-78-1

## When Is a Function Represented by Its Taylor Series?

By Theorem §78.1 and Example §78.1(b), *if* $e^x$ has a power series representation at $0$, it is $\sum x^n/n!$. Whether it *does* is the general question: when is a function with derivatives of all orders equal to the sum of its Taylor series?

> [!definition] Definition §78.2: Taylor Polynomial; Remainder
> The **$n$th-degree Taylor polynomial of $f$ at $a$** is the $n$th partial sum of the Taylor series,
>
> $$
> T_n(x) = \sum_{i=0}^{n} \frac{f^{(i)}(a)}{i!} (x - a)^i = f(a) + \frac{f'(a)}{1!} (x - a) + \frac{f''(a)}{2!} (x - a)^2 + \cdots + \frac{f^{(n)}(a)}{n!} (x - a)^n .
> $$
>
> The **remainder** of the Taylor series is $R_n(x) = f(x) - T_n(x)$, so that $f(x) = T_n(x) + R_n(x)$.
>
> For example, for $e^x$ at $0$: $T_1(x) = 1 + x$, $T_2(x) = 1 + x + \dfrac{x^2}{2!}$, $T_3(x) = 1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!}$.
>
> *Stewart: 11.10 (text)*

^def-78-2

> [!theorem] Theorem §78.3: Remainder Tending to Zero
> If $f(x) = T_n(x) + R_n(x)$, where $T_n$ is the $n$th-degree Taylor polynomial of $f$ at $a$, and if
>
> $$
> \lim_{n \to \infty} R_n(x) = 0
> $$
>
> for $|x - a| < R$, then $f$ is equal to the sum of its Taylor series on the interval $|x - a| < R$.
>
> *Stewart: 11.10, Theorem 8*

^thm-78-3

> [!proof]+ Proof
> $f(x)$ is the sum of its Taylor series exactly when $f(x) = \lim_{n \to \infty} T_n(x)$, the limit of the partial sums. If $R_n(x) \to 0$, then
>
> $$
> \lim_{n \to \infty} T_n(x) = \lim_{n \to \infty} [f(x) - R_n(x)] = f(x) - \lim_{n \to \infty} R_n(x) = f(x) .
> $$

^pf-78-3

*Uses:* [[§78 Taylor and Maclaurin Series#^def-78-2|Def. §78.2]], [[§70 Series#^def-70-2|Def. §70.2]], [[§69 Sequences#^thm-69-3|§69.3]]

To show $\lim_{n \to \infty} R_n(x) = 0$ for a specific function we usually use the following bound.

> [!theorem] Theorem §78.4: Taylor's Inequality
> If $|f^{(n+1)}(x)| \le M$ for $|x - a| \le d$, then the remainder $R_n(x)$ of the Taylor series satisfies the inequality
>
> $$
> |R_n(x)| \le \frac{M}{(n+1)!} |x - a|^{n+1} \qquad \text{for } |x - a| \le d .
> $$
>
> *Stewart: 11.10, Taylor's Inequality 9*

^thm-78-4

> [!proof]+ Proof
> (The proof integrates with Part 2 of the Fundamental Theorem of Calculus, so $f^{(n+1)}$ is taken to be continuous on $[a - d, a + d]$; Stewart uses this tacitly.)
>
> **The case $n = 1$ (Stewart's proof).** Assume $|f''(x)| \le M$. In particular $f''(x) \le M$, so for $a \le x \le a + d$
>
> $$
> \int_a^x f''(t)\,dt \le \int_a^x M\,dt .
> $$
>
> An antiderivative of $f''$ is $f'$, so by Part 2 of the Fundamental Theorem of Calculus
>
> $$
> f'(x) - f'(a) \le M(x - a) \qquad\text{or}\qquad f'(x) \le f'(a) + M(x - a) .
> $$
>
> Thus
>
> $$
> \int_a^x f'(t)\,dt \le \int_a^x [f'(a) + M(t - a)]\,dt , \qquad
> f(x) - f(a) \le f'(a)(x - a) + M \frac{(x - a)^2}{2} ,
> $$
>
> that is, $f(x) - f(a) - f'(a)(x - a) \le \dfrac{M}{2} (x - a)^2$. But $R_1(x) = f(x) - T_1(x) = f(x) - f(a) - f'(a)(x - a)$, so $R_1(x) \le \dfrac{M}{2} (x - a)^2$. The same argument with $f''(x) \ge -M$ gives $R_1(x) \ge -\dfrac{M}{2} (x - a)^2$. So $|R_1(x)| \le \dfrac{M}{2} |x - a|^2$ for $a \le x \le a + d$.
>
> **General $n$, $x \ge a$.** Stewart: "the result for any $n$ is proved in a similar way by integrating $n + 1$ times." Here is that argument. Let
>
> $$
> g(x) = \frac{M}{(n+1)!} (x - a)^{n+1} - R_n(x) .
> $$
>
> Since $T_n$ is a polynomial of degree $n$ whose derivatives at $a$ of orders $0, \ldots, n$ agree with those of $f$, we have $R_n^{(j)}(a) = 0$ for $j = 0, \ldots, n$ and $R_n^{(n+1)} = f^{(n+1)}$. Hence $g^{(j)}(a) = 0$ for $j = 0, \ldots, n$, and $g^{(n+1)}(t) = M - f^{(n+1)}(t) \ge 0$. For $a \le x \le a + d$, the Fundamental Theorem gives $g^{(n)}(x) = \int_a^x g^{(n+1)}(t)\,dt \ge 0$; then $g^{(n-1)}(x) = \int_a^x g^{(n)}(t)\,dt \ge 0$; and after $n + 1$ integrations, $g(x) \ge 0$, that is, $R_n(x) \le \frac{M}{(n+1)!} (x - a)^{n+1}$. The same argument applied to $\frac{M}{(n+1)!} (x - a)^{n+1} + R_n(x)$, whose $(n+1)$st derivative is $M + f^{(n+1)} \ge 0$, gives $R_n(x) \ge -\frac{M}{(n+1)!} (x - a)^{n+1}$.
>
> **$x < a$.** (Stewart: "similar calculations show that this inequality is also true for $x < a$.") Apply the case just proved to $F(t) = f(2a - t)$. Then $F^{(k)}(t) = (-1)^k f^{(k)}(2a - t)$, so $|F^{(n+1)}| \le M$ on $[a - d, a + d]$, and the Taylor polynomial of $F$ at $a$ is $T_n(2a - t)$; hence the remainder of $F$ at $t$ is $R_n(2a - t)$. For $a - d \le x < a$, put $t = 2a - x \in (a, a + d]$: $|R_n(x)| \le \frac{M}{(n+1)!} (t - a)^{n+1} = \frac{M}{(n+1)!} |x - a|^{n+1}$.

^pf-78-4

*Uses:* [[§36 The Fundamental Theorem of Calculus#^thm-36-2|§36.2]] (FTC Part 2), [[§35 The Definite Integral#^thm-35-6|§35.6]] (comparison property of integrals), [[§78 Taylor and Maclaurin Series#^def-78-2|Def. §78.2]]

> [!remark]- Connections
> - Rigorous treatment: [[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]] (Taylor's theorem with Lagrange remainder, proved from Rolle's theorem; it implies Taylor's Inequality at once and needs no continuity of $f^{(n+1)}$), and [[§31 Taylor's Theorem#^prop-31-1|451 Prop. §31.1]] (= Theorem §78.3).

> [!remark]- Remark: Formulas for the Remainder
> As alternatives to Taylor's Inequality there are exact formulas. If $f^{(n+1)}$ is continuous on an interval $I$ containing $a$ and $x$, then
>
> $$
> R_n(x) = \frac{1}{n!} \int_a^x (x - t)^n f^{(n+1)}(t)\,dt \qquad \text{(integral form)},
> $$
>
> and there is a number $z$ between $x$ and $a$ with
>
> $$
> R_n(x) = \frac{f^{(n+1)}(z)}{(n+1)!} (x - a)^{n+1} \qquad \text{(Lagrange's form)},
> $$
>
> which extends the Mean Value Theorem (the case $n = 0$). Stewart gives the proofs on his website.

^rem-78-2

> [!theorem] Proposition §78.5: Factorials Beat Powers
> $$
> \lim_{n \to \infty} \frac{x^n}{n!} = 0 \qquad \text{for every real number } x . \qquad (10)
> $$
>
> *Stewart: 11.10, Equation 10*

^prop-78-5

> [!proof]+ Proof
> By Example §78.1(b), the series $\sum x^n/n!$ converges for all $x$, so its $n$th term tends to $0$ by [[§70 Series#^thm-70-4|Theorem §70.4]].

^pf-78-5

*Uses:* [[§78 Taylor and Maclaurin Series#^ex-78-1|Ex. §78.1]], [[§70 Series#^thm-70-4|§70.4]]

> [!theorem] Theorem §78.6: The Exponential Function
> $e^x$ is equal to the sum of its Maclaurin series:
>
> $$
> e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} \qquad \text{for all } x . \qquad (11)
> $$
>
> In particular, with $x = 1$,
>
> $$
> e = \sum_{n=0}^{\infty} \frac{1}{n!} = 1 + \frac{1}{1!} + \frac{1}{2!} + \frac{1}{3!} + \cdots \qquad (12)
> $$
>
> *Stewart: 11.10, Equations 11 and 12 (Example 11.10.3)*

^thm-78-6

> [!proof]+ Proof
> Let $f(x) = e^x$, so $f^{(n+1)}(x) = e^x$ for all $n$. If $d$ is any positive number and $|x| \le d$, then $|f^{(n+1)}(x)| = e^x \le e^d$. So Taylor's Inequality with $a = 0$ and $M = e^d$ says
>
> $$
> |R_n(x)| \le \frac{e^d}{(n+1)!} |x|^{n+1} \qquad \text{for } |x| \le d .
> $$
>
> The same constant $M = e^d$ works for every $n$. By (10),
>
> $$
> \lim_{n \to \infty} \frac{e^d}{(n+1)!} |x|^{n+1} = e^d \lim_{n \to \infty} \frac{|x|^{n+1}}{(n+1)!} = 0 .
> $$
>
> By the Squeeze Theorem, $|R_n(x)| \to 0$, and so $R_n(x) \to 0$ ([[§69 Sequences#^thm-69-5|Theorem §69.5]]), for all $|x| \le d$. Since $d$ is arbitrary, this holds for all $x$, and by Theorem §78.3 $e^x$ is the sum of its Maclaurin series.

^pf-78-6

*Uses:* [[§78 Taylor and Maclaurin Series#^thm-78-4|§78.4]], [[§78 Taylor and Maclaurin Series#^prop-78-5|§78.5]], [[§78 Taylor and Maclaurin Series#^thm-78-3|§78.3]], [[§69 Sequences#^thm-69-4|§69.4]], [[§69 Sequences#^thm-69-5|§69.5]], [[§78 Taylor and Maclaurin Series#^ex-78-1|Ex. §78.1]]

> [!example] Example §78.2: Taylor Series Away from 0
> **(a)** Find the Taylor series for $f(x) = e^x$ at $a = 2$.
>
> $f^{(n)}(2) = e^2$, so by (6) the Taylor series is
>
> $$
> \sum_{n=0}^{\infty} \frac{f^{(n)}(2)}{n!} (x - 2)^n = \sum_{n=0}^{\infty} \frac{e^2}{n!} (x - 2)^n .
> $$
>
> As in Example §78.1(b), the Ratio Test gives $R = \infty$ (the ratio is $|x - 2|/(n+1) \to 0$). As in Theorem §78.6, with $M = e^{2 + d}$ for $|x - 2| \le d$, $R_n(x) \to 0$, so
>
> $$
> e^x = \sum_{n=0}^{\infty} \frac{e^2}{n!} (x - 2)^n \qquad \text{for all } x . \qquad (13)
> $$
>
> The Maclaurin series (11) is better for $x$ near $0$, and (13) for $x$ near $2$.
>
> **(b)** Represent $f(x) = \sin x$ as the sum of its Taylor series centered at $\pi/3$.
>
> $$
> f\big(\tfrac{\pi}{3}\big) = \sin\tfrac{\pi}{3} = \tfrac{\sqrt3}{2}, \quad f'\big(\tfrac{\pi}{3}\big) = \cos\tfrac{\pi}{3} = \tfrac12, \quad f''\big(\tfrac{\pi}{3}\big) = -\sin\tfrac{\pi}{3} = -\tfrac{\sqrt3}{2}, \quad f'''\big(\tfrac{\pi}{3}\big) = -\cos\tfrac{\pi}{3} = -\tfrac12 ,
> $$
>
> and the pattern repeats. So the Taylor series at $\pi/3$ is
>
> $$
> \frac{\sqrt3}{2} + \frac{1}{2 \cdot 1!} \left( x - \frac{\pi}{3} \right) - \frac{\sqrt3}{2 \cdot 2!} \left( x - \frac{\pi}{3} \right)^2 - \frac{1}{2 \cdot 3!} \left( x - \frac{\pi}{3} \right)^3 + \cdots
> $$
>
> Separating the terms that contain $\sqrt3$ (even powers, $f^{(2n)}(\pi/3) = (-1)^n \frac{\sqrt3}{2}$) from the others (odd powers, $f^{(2n+1)}(\pi/3) = (-1)^n \frac12$),
>
> $$
> \sin x = \sum_{n=0}^{\infty} \frac{(-1)^n \sqrt3}{2(2n)!} \left( x - \frac{\pi}{3} \right)^{2n} + \sum_{n=0}^{\infty} \frac{(-1)^n}{2(2n+1)!} \left( x - \frac{\pi}{3} \right)^{2n+1} .
> $$
>
> This holds for all $x$: every derivative of $\sin$ is $\pm\sin$ or $\pm\cos$, so $M = 1$ in Taylor's Inequality and $|R_n(x)| \le |x - \pi/3|^{n+1}/(n+1)! \to 0$ by (10), as in the proof of Theorem §78.7. The third Taylor polynomial at $\pi/3$ approximates $\sin x$ well near $\pi/3$ but not near $0$; the Maclaurin polynomial does the opposite.
>
> *Stewart: Examples 11.10.4 and 11.10.7*

^ex-78-2

## Taylor Series of Important Functions

> [!theorem] Theorem §78.7: Sine
> $$
> \sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!} \qquad \text{for all } x . \qquad (15)
> $$
>
> *Stewart: 11.10, Equation 15 (Example 11.10.5)*

^thm-78-7

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
> By (10) the right side tends to $0$ as $n \to \infty$, so $|R_n(x)| \to 0$ by the Squeeze Theorem, and $R_n(x) \to 0$. By Theorem §78.3, $\sin x$ is equal to the sum of its Maclaurin series, for all $x$.

^pf-78-7

*Uses:* [[§78 Taylor and Maclaurin Series#^thm-78-4|§78.4]], [[§78 Taylor and Maclaurin Series#^prop-78-5|§78.5]], [[§78 Taylor and Maclaurin Series#^thm-78-3|§78.3]], [[§69 Sequences#^thm-69-4|§69.4]], [[§16 Derivatives of Trigonometric Functions#^thm-16-1|§16.1]], [[§16 Derivatives of Trigonometric Functions#^thm-16-2|§16.2]] (derivatives of sine and cosine)

![[m233-78-1.svg]]
*$\sin x$ (black) and its Maclaurin polynomials $T_1(x) = x$, $T_3(x) = x - \frac{x^3}{3!}$, $T_5$ and $T_9$. Each polynomial follows the sine curve on a larger interval around $0$ before it breaks away: for fixed $x$ the error $|R_n(x)| \le |x|^{n+1}/(n+1)!$ tends to $0$, but more slowly for larger $|x|$.*

> [!theorem] Theorem §78.8: Cosine
> $$
> \cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!} \qquad \text{for all } x . \qquad (16)
> $$
>
> *Stewart: 11.10, Equation 16 (Example 11.10.6)*

^thm-78-8

> [!proof]+ Proof
> One could proceed directly as for sine, but it is easier to differentiate the Maclaurin series for $\sin x$ term by term ([[§77 Representations of Functions as Power Series#^thm-77-1|Theorem §77.1]]):
>
> $$
> \cos x = \frac{d}{dx} (\sin x) = \frac{d}{dx} \left( x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots \right) = 1 - \frac{3x^2}{3!} + \frac{5x^4}{5!} - \frac{7x^6}{7!} + \cdots = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots
> $$
>
> since $(2n+1)/(2n+1)! = 1/(2n)!$. By Theorem §77.1 the differentiated series converges to the derivative of $\sin x$, namely $\cos x$, and its radius of convergence is unchanged, so it converges for all $x$.

^pf-78-8

*Uses:* [[§78 Taylor and Maclaurin Series#^thm-78-7|§78.7]], [[§77 Representations of Functions as Power Series#^thm-77-1|§77.1]]

> [!remark]- Connections
> - Rigorous treatment of (11), (15) and (16): [[§31 Taylor's Theorem#^ex-31-1|451 Ex. §31.1]] (cosine and $e^x$ through the remainder, as here). In 451 the series can instead serve as *definitions* of sine and cosine: [[§26 Differentiation and Integration of Power Series#^ex-26-8|451 Ex. §26.8]].
> - See also: [[§53 Complex Numbers#^rem-53-1|235 Remark: Euler's Formula]] ($e^{i\varphi} = \cos\varphi + i\sin\varphi$ by splitting the series (11) at $x = i\varphi$ into the series (16) and (15)), and [[§38 Applications to Differential Equations#^def-38-3|235 Def. §38.3]] (the complex exponential $e^{(a+bi)t} = e^{at}(\cos bt + i\sin bt)$, used for complex eigenvalues of $\mathbf{x}' = A\mathbf{x}$).
> - ODE version: [[§15 Complex Roots of the Characteristic Equation#^def-15-1|331 Def. §15.1]] (Euler's formula, motivated by these three series in [[§15 Complex Roots of the Characteristic Equation#^rem-15-1|331 Remark: Where Euler's Formula Comes From]]) and [[§33★ Fundamental Matrices#^def-33-3|331 Def. §33.3]] (the matrix exponential, the series (11) with $\mathbf{A}t$ in place of $x$, which converges and satisfies $\Phi' = \mathbf{A}\Phi$ by [[§33★ Fundamental Matrices#^thm-33-3|331 Thm. §33.3]]).
> - Complex-variables version: [[§64 Examples (Proof of Taylor's Theorem)#^prop-64-1|342 Prop. §64.1]] (the series (11), (15) and (16) for complex $z$, proved by Taylor's theorem for analytic functions); splitting (11) at $z = i\theta$ gives Euler's formula, [[§7 Exponential Form#^def-7-2|342 Def. §7.2]].

These series, found by Newton by other methods, say that everything about $e^x$, $\sin x$ and $\cos x$ is determined by their derivatives at the single number $0$.

> [!definition] Definition §78.3: Binomial Coefficients; Binomial Series
> For any real number $k$ and integer $n \ge 0$, the **binomial coefficients** are
>
> $$
> \binom{k}{n} = \frac{k(k-1)(k-2)\cdots(k - n + 1)}{n!} , \qquad \binom{k}{0} = 1 .
> $$
>
> The **binomial series** is the Maclaurin series of $(1 + x)^k$, which is $\sum_{n=0}^{\infty} \binom{k}{n} x^n$ (Theorem §78.9).
>
> *Stewart: 11.10 (text)*

^def-78-3

> [!theorem] Theorem §78.9: The Binomial Series
> If $k$ is any real number and $|x| < 1$, then
>
> $$
> (1 + x)^k = \sum_{n=0}^{\infty} \binom{k}{n} x^n = 1 + kx + \frac{k(k-1)}{2!} x^2 + \frac{k(k-1)(k-2)}{3!} x^3 + \cdots \qquad (17)
> $$
>
> If $k$ is a nonnegative integer, $\binom{k}{n} = 0$ for $n > k$ (the numerator contains the factor $k - k$), the series terminates, and (17) is the ordinary Binomial Theorem. At the endpoints the series converges at $x = 1$ if $-1 < k \le 0$, and at both endpoints if $k \ge 0$.
>
> *Stewart: 11.10, The Binomial Series 17 (Example 11.10.8)*

^thm-78-9

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
> **The sum is $(1 + x)^k$.** Stewart notes that showing $R_n(x) \to 0$ is quite difficult and outlines an easier proof in Exercise 97, which we carry out. Let $g(x) = \sum_{n=0}^{\infty} \binom{k}{n} x^n$ for $|x| < 1$. By Theorem §77.1, $g'(x) = \sum_{n=1}^{\infty} n \binom{k}{n} x^{n-1}$, so
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
> so $h$ is constant on $(-1, 1)$ ([[§26 The Mean Value Theorem#^thm-26-3|Theorem §26.3]]), and $h(x) = h(0) = g(0) = 1$. Hence $g(x) = (1 + x)^k$ for $|x| < 1$.
>
> (The endpoint behavior stated in the theorem is quoted from Stewart without proof.)

^pf-78-9

*Uses:* [[§78 Taylor and Maclaurin Series#^def-78-1|Def. §78.1]], [[§78 Taylor and Maclaurin Series#^def-78-3|Def. §78.3]], [[§74 The Ratio and Root Tests#^thm-74-1|§74.1]], [[§77 Representations of Functions as Power Series#^thm-77-1|§77.1]], [[§26 The Mean Value Theorem#^thm-26-3|§26.3]] (a function with zero derivative is constant)

> [!remark] Remark: Important Maclaurin Series
> For future reference (Stewart's Table 1), the Maclaurin series found here and in [[§77 Representations of Functions as Power Series|§77]], with their radii of convergence:
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

^rem-78-3

## New Taylor Series from Old

By Corollary §78.2, however a power series representation of $f$ is obtained, it is the Taylor series of $f$. So new Taylor series can be found by manipulating the series in the table instead of using the coefficient formula. As in [[§77 Representations of Functions as Power Series|§77]], we can replace $x$ by an expression $c x^m$, multiply or divide by such an expression, and differentiate or integrate term by term. Series can also be added and subtracted ([[§70 Series#^thm-70-6|Theorem §70.6]]), multiplied and divided.

> [!theorem] Theorem §78.10: Multiplying and Dividing Power Series
> If $f(x) = \sum c_n x^n$ and $g(x) = \sum b_n x^n$ both converge for $|x| < R$, and the series are multiplied as if they were polynomials, the resulting series also converges for $|x| < R$ and represents $f(x) g(x)$. For division, if $b_0 \ne 0$, the series obtained by long division converges to $f(x)/g(x)$ for sufficiently small $|x|$.
>
> *Stewart: 11.10 (text)*

^thm-78-10

*Stewart states this without proof ("there is a theorem which states that"); it is not proved in 451.*

> [!remark]- Connections
> - Complex-variables version: [[§73★ Multiplication and Division of Power Series#^thm-73-2|342 Thm. §73.2]] (the Cauchy product converges to $fg$) and [[§73★ Multiplication and Division of Power Series#^prop-73-3|342 Prop. §73.3]] (division), both proved there.

> [!example] Example §78.3: Substituting, Multiplying, Recognizing
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

^ex-78-3

> [!example] Example §78.4: Integrals and Limits by Series
> **(a)** Evaluate $\int e^{-x^2}\,dx$ as an infinite series, and **(b)** evaluate $\int_0^1 e^{-x^2}\,dx$ correct to within an error of $0.001$.
>
> $e^{-x^2}$ has no elementary antiderivative ([[§48 Strategy for Integration#^thm-48-2|Theorem §48.2]]); following Newton, expand and integrate term by term. Replacing $x$ by $-x^2$ in the series for $e^x$, for all $x$,
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
> for $x \ne 0$. The right side is a power series, hence continuous ([[§77 Representations of Functions as Power Series#^thm-77-1|Theorem §77.1]]), so
>
> $$
> \lim_{x \to 0} \frac{e^x - 1 - x}{x^2} = \frac{1}{2!} + 0 + 0 + \cdots = \frac12 .
> $$
>
> (L'Hospital's Rule, applied twice, gives the same.)
>
> *Stewart: Examples 11.10.13 and 11.10.14*

^ex-78-4

> [!example] Example §78.5: Multiplying and Dividing Series
> Find the first three nonzero terms in the Maclaurin series for **(a)** $e^x \sin x$ and **(b)** $\tan x$.
>
> **(a)** Multiply the series, collecting like terms as for polynomials (Theorem §78.10):
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

^ex-78-5
