---
type: section
subject: "[[Calculus]]"
chapter: 11
section: 90
stewart: "11.10"
aliases: ["Stewart 11.10"]
tags: [calculus]
---
← [[§89 Representations of Functions as Power Series]] · ↑ [[· 11 Sequences, Series, and Power Series]] · [[§91 Taylor Series of Important Functions]] →

*Stewart, Section 11.10.*

If a function has a power series representation at $a$, its coefficients are forced: $c_n = f^{(n)}(a)/n!$. So there is only one candidate, the Taylor series of $f$, and the question becomes when $f$ actually equals it. That happens exactly when the remainder $R_n(x) = f(x) - T_n(x)$ tends to $0$, and Taylor's Inequality bounds the remainder by the size of the next derivative. This proves the Maclaurin series of $e^x$, $\sin x$ and $\cos x$ for all $x$, and the binomial series of $(1 + x)^k$ for $|x| < 1$. Because the representation is unique, new Taylor series can then be produced from old ones by substitution, multiplication, differentiation and integration, and used to integrate functions like $e^{-x^2}$, to evaluate limits, and to sum series.

## Definitions of Taylor Series and Maclaurin Series

> [!theorem] Theorem §90.1: The Coefficients of a Power Series
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

^thm-90-1

> [!proof]+ Proof
> Write the series out:
>
> $$
> f(x) = c_0 + c_1 (x - a) + c_2 (x - a)^2 + c_3 (x - a)^3 + c_4 (x - a)^4 + \cdots \qquad |x - a| < R . \qquad (1)
> $$
>
> Putting $x = a$, all terms after the first are $0$: $f(a) = c_0$. By [[§89 Representations of Functions as Power Series#^thm-89-1|Theorem §89.1]] we can differentiate term by term on $|x - a| < R$:
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
> so $f'''(a) = 2 \cdot 3 c_3 = 3!\,c_3$. In general (Stewart: "by now you can see the pattern"), [[§89 Representations of Functions as Power Series#^thm-89-1|Theorem §89.1]] applied $k$ times gives, for $|x - a| < R$,
>
> $$
> f^{(k)}(x) = \sum_{n=k}^{\infty} n(n-1)\cdots(n-k+1)\, c_n (x - a)^{n-k} ,
> $$
>
> and at $x = a$ only the term $n = k$ survives: $f^{(k)}(a) = k(k-1)\cdots 1 \cdot c_k = k!\,c_k$. Solving for $c_k$ gives the formula.

^pf-90-1

*Uses:* [[§89 Representations of Functions as Power Series#^thm-89-1|§89.1]]

Substituting this formula for $c_n$ back into the series: *if* $f$ has a power series expansion at $a$, then it must be of the following form.

> [!definition] Definition §106.1: Taylor Series; Maclaurin Series
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

^def-90-1

> [!remark]- Connections
> - Rigorous treatment: [[§31 Taylor's Theorem#^def-31-1|451 Def. §31.1]]. That a Taylor series may converge to something other than $f$: [[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]] ($e^{-1/x^2}$, Stewart's Exercise 96).
> - Complex-variables version: [[§62 Taylor Series#^def-62-1|342 Def. §62.1]] (the same series for a function analytic at $z_0$).

> [!theorem] Corollary §90.2: Uniqueness of Power Series Representations
> The power series representation at $a$ of a function is unique, regardless of how it is found: if $f(x) = \sum c_n (x - a)^n$ for $|x - a| < R$, the series is the Taylor series of $f$ at $a$. In particular, all the power series representations of [[§89 Representations of Functions as Power Series|§89]] are Taylor series of the functions they represent.
>
> *Stewart: 11.10 (text, Note 2)*

^cor-90-2

> [!proof]+ Proof
> By [[§90 Taylor and Maclaurin Series#^thm-90-1|Theorem §90.1]], $c_n = f^{(n)}(a)/n!$ for every $n$, so the coefficients are determined by $f$ alone.

^pf-90-2

*Uses:* [[§90 Taylor and Maclaurin Series#^thm-90-1|§90.1]]

> [!remark]- Connections
> - Complex-variables version: [[§72★ Uniqueness of Series Representations#^thm-72-1|342 Thm. §72.1]] (a power series that converges to $f$ in a disk is the Taylor series of $f$).

> [!remark] Remark: A Taylor Series Need Not Equal Its Function
> [[§90 Taylor and Maclaurin Series#^thm-90-1|Theorem §90.1]] says: *if* $f$ has a power series representation about $a$, then that series is the Taylor series. It does not say that every function equals the sum of its Taylor series. There are functions with derivatives of all orders that are not equal to the sum of their Taylor series, such as $f(x) = e^{-1/x^2}$ for $x \ne 0$, $f(0) = 0$ (Stewart's Exercise 96): all its derivatives at $0$ are $0$, so its Maclaurin series is $0$.

^rem-90-1

> [!example] Example §106.1: Maclaurin Series from the Definition
> **(a)** $f(x) = 1/(1 - x)$ has the power series representation $\sum_{n=0}^{\infty} x^n$ for $|x| < 1$ ([[§89 Representations of Functions as Power Series#^def-89-1|Definition §89.1]]). By [[§90 Taylor and Maclaurin Series#^thm-90-1|Theorem §90.1]] this must be its Maclaurin series. To confirm:
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

^ex-90-1

## When Is a Function Represented by Its Taylor Series?

By [[§90 Taylor and Maclaurin Series#^thm-90-1|Theorem §90.1]] and [[§90 Taylor and Maclaurin Series#^ex-90-1|Example §90.1]](b), *if* $e^x$ has a power series representation at $0$, it is $\sum x^n/n!$. Whether it *does* is the general question: when is a function with derivatives of all orders equal to the sum of its Taylor series?

> [!definition] Definition §106.2: Taylor Polynomial
> The **$n$th-degree Taylor polynomial of $f$ at $a$** is the $n$th partial sum of the Taylor series,
>
> $$
> T_n(x) = \sum_{i=0}^{n} \frac{f^{(i)}(a)}{i!} (x - a)^i = f(a) + \frac{f'(a)}{1!} (x - a) + \frac{f''(a)}{2!} (x - a)^2 + \cdots + \frac{f^{(n)}(a)}{n!} (x - a)^n .
> $$
>
> For example, for $e^x$ at $0$: $T_1(x) = 1 + x$, $T_2(x) = 1 + x + \dfrac{x^2}{2!}$, $T_3(x) = 1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!}$.
>
> *Stewart: 11.10 (text)*

^def-90-2

> [!definition] Definition §106.3: Remainder of the Taylor Series
> The **remainder** of the Taylor series is $R_n(x) = f(x) - T_n(x)$, so that $f(x) = T_n(x) + R_n(x)$.
>
> *Stewart: 11.10 (text)*

^def-90-3

> [!theorem] Theorem §90.3: Remainder Tending to Zero
> If $f(x) = T_n(x) + R_n(x)$, where $T_n$ is the $n$th-degree Taylor polynomial of $f$ at $a$, and if
>
> $$
> \lim_{n \to \infty} R_n(x) = 0
> $$
>
> for $|x - a| < R$, then $f$ is equal to the sum of its Taylor series on the interval $|x - a| < R$.
>
> *Stewart: 11.10, Theorem 8*

^thm-90-3

> [!proof]+ Proof
> $f(x)$ is the sum of its Taylor series exactly when $f(x) = \lim_{n \to \infty} T_n(x)$, the limit of the partial sums. If $R_n(x) \to 0$, then
>
> $$
> \lim_{n \to \infty} T_n(x) = \lim_{n \to \infty} [f(x) - R_n(x)] = f(x) - \lim_{n \to \infty} R_n(x) = f(x) .
> $$

^pf-90-3

*Uses:* [[§90 Taylor and Maclaurin Series#^def-90-2|Def. §90.2]], [[§90 Taylor and Maclaurin Series#^def-90-3|Def. §90.3]], [[§82 Series#^def-82-2|Def. §82.2]], [[§82 Series#^def-82-3|Def. §82.3]], [[§80 Sequences#^thm-80-3|§80.3]]

To show $\lim_{n \to \infty} R_n(x) = 0$ for a specific function we usually use the following bound.

> [!theorem] Theorem §90.4: Taylor's Inequality
> If $|f^{(n+1)}(x)| \le M$ for $|x - a| \le d$, then the remainder $R_n(x)$ of the Taylor series satisfies the inequality
>
> $$
> |R_n(x)| \le \frac{M}{(n+1)!} |x - a|^{n+1} \qquad \text{for } |x - a| \le d .
> $$
>
> *Stewart: 11.10, Taylor's Inequality 9*

^thm-90-4

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

^pf-90-4

*Uses:* [[§41 The Fundamental Theorem of Calculus#^thm-41-2|§41.2]] (FTC Part 2), [[§40 Properties of the Definite Integral#^thm-40-3|§40.3]] (comparison property of integrals), [[§90 Taylor and Maclaurin Series#^def-90-2|Def. §90.2]], [[§90 Taylor and Maclaurin Series#^def-90-3|Def. §90.3]]

> [!remark]- Connections
> - Rigorous treatment: [[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]] (Taylor's theorem with Lagrange remainder, proved from Rolle's theorem; it implies Taylor's Inequality at once and needs no continuity of $f^{(n+1)}$), and [[§31 Taylor's Theorem#^prop-31-1|451 Prop. §31.1]] (= [[§90 Taylor and Maclaurin Series#^thm-90-3|Theorem §90.3]]).

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

^rem-90-2

> [!theorem] Proposition §90.5: Factorials Beat Powers
> $$
> \lim_{n \to \infty} \frac{x^n}{n!} = 0 \qquad \text{for every real number } x . \qquad (10)
> $$
>
> *Stewart: 11.10, Equation 10*

^prop-90-5

> [!proof]+ Proof
> By [[§90 Taylor and Maclaurin Series#^ex-90-1|Example §90.1]](b), the series $\sum x^n/n!$ converges for all $x$, so its $n$th term tends to $0$ by [[§82 Series#^thm-82-4|Theorem §82.4]].

^pf-90-5

*Uses:* [[§90 Taylor and Maclaurin Series#^ex-90-1|Ex. §90.1]], [[§82 Series#^thm-82-4|§82.4]]

> [!theorem] Theorem §90.6: The Exponential Function
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

^thm-90-6

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
> By the Squeeze Theorem, $|R_n(x)| \to 0$, and so $R_n(x) \to 0$ ([[§80 Sequences#^thm-80-5|Theorem §80.5]]), for all $|x| \le d$. Since $d$ is arbitrary, this holds for all $x$, and by [[§90 Taylor and Maclaurin Series#^thm-90-3|Theorem §90.3]] $e^x$ is the sum of its Maclaurin series.

^pf-90-6

*Uses:* [[§90 Taylor and Maclaurin Series#^thm-90-4|§90.4]], [[§90 Taylor and Maclaurin Series#^prop-90-5|§90.5]], [[§90 Taylor and Maclaurin Series#^thm-90-3|§90.3]], [[§80 Sequences#^thm-80-4|§80.4]], [[§80 Sequences#^thm-80-5|§80.5]], [[§90 Taylor and Maclaurin Series#^ex-90-1|Ex. §90.1]]

> [!example] Example §106.2: Taylor Series Away from 0
> **(a)** Find the Taylor series for $f(x) = e^x$ at $a = 2$.
>
> $f^{(n)}(2) = e^2$, so by (6) the Taylor series is
>
> $$
> \sum_{n=0}^{\infty} \frac{f^{(n)}(2)}{n!} (x - 2)^n = \sum_{n=0}^{\infty} \frac{e^2}{n!} (x - 2)^n .
> $$
>
> As in [[§90 Taylor and Maclaurin Series#^ex-90-1|Example §90.1]](b), the Ratio Test gives $R = \infty$ (the ratio is $|x - 2|/(n+1) \to 0$). As in [[§90 Taylor and Maclaurin Series#^thm-90-6|Theorem §90.6]], with $M = e^{2 + d}$ for $|x - 2| \le d$, $R_n(x) \to 0$, so
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
> This holds for all $x$: every derivative of $\sin$ is $\pm\sin$ or $\pm\cos$, so $M = 1$ in Taylor's Inequality and $|R_n(x)| \le |x - \pi/3|^{n+1}/(n+1)! \to 0$ by (10), as in the proof of [[§91 Taylor Series of Important Functions#^thm-91-1|Theorem §91.1]]. The third Taylor polynomial at $\pi/3$ approximates $\sin x$ well near $\pi/3$ but not near $0$; the Maclaurin polynomial does the opposite.
>
> *Stewart: Examples 11.10.4 and 11.10.7*

^ex-90-2

*The section continues in [[§91 Taylor Series of Important Functions]].*
