---
subject: "[[Single Variable Analysis]]"
section: 31
chapter: 5
tags: [real-analysis, math451]
---
← [[§30 L'Hospital's Rule]] · ↑ [[· 5 Differentiation]] · [[§32 The Definition of the Riemann Integral]] →

The third main result of the chapter: how to approximate general functions by polynomials — and, in the limit, represent a function by a power series.

## The Taylor Series

Suppose first that $f(x) = \sum_{n=0}^\infty a_n x^n$ converges for $|x| < R$. What are the coefficients, in terms of $f$? By §26, term-by-term differentiation is valid and preserves the radius, so it can be *iterated*:

$$
f(0) = a_0; \qquad f'(x) = \sum_{n\geq1} n a_n x^{n-1}, \quad f'(0) = a_1; \qquad f''(x) = \sum_{n \geq 2} n(n-1) a_n x^{n-2}, \quad f''(0) = 2! \, a_2;
$$

and in general, differentiating $n$ times and evaluating at $0$ kills all terms except the constant one:

$$
f^{(n)}(0) = n!\, a_n, \qquad \text{i.e.} \qquad a_n = \frac{f^{(n)}(0)}{n!}.
$$

So a convergent power series is forced to be $\sum \tfrac{f^{(n)}(0)}{n!} x^n$. This motivates:

> [!definition] Definition §31.1: Taylor Series
> If $f: (-\varepsilon, \varepsilon) \to \mathbb{R}$ has derivatives of all orders at $0$, the series
>
> $$
> \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!}\, x^n
> $$
>
> is called the **Taylor series of $f$ at $0$**. (The $\varepsilon$ signals, as in $\varepsilon$-$\delta$ arguments, that only a small neighborhood matters — how big the domain is, we don't care.) More generally, for $f: (a,b) \to \mathbb{R}$ with derivatives of all orders and $x_0 \in (a,b)$, the **Taylor series at $x_0$** is $\sum_n \tfrac{f^{(n)}(x_0)}{n!} (x - x_0)^n$. We concentrate on $x_0 = 0$.

^def-31-1

> [!remark]- Connections
> - Computational version: [[§78 Taylor and Maclaurin Series#^def-78-1|Calc Def. §78.1]] (with worked examples).

**Question: is $f(x) = \sum_n \tfrac{f^{(n)}(0)}{n!}x^n$ for every $f$ with all derivatives?** No — two distinct problems:

1. the Taylor series may not converge for any $x \neq 0$ (radius $R = 0$);

2. even if $R > 0$, the series may converge to something *other than* $f(x)$.

## The Remainder and Taylor's Theorem

Convergence of the series to $f$ is governed by the partial sums $s_n(x) = \sum_{k=0}^{n} \tfrac{f^{(k)}(0)}{k!}x^k$. Define the **remainder**

$$
R_n(x) = f(x) - s_{n-1}(x) = f(x) - \sum_{k=0}^{n-1} \frac{f^{(k)}(0)}{k!} x^k.
$$

> [!theorem] Proposition §31.1: Convergence via the Remainder
> The Taylor series converges to $f(x)$ if and only if $R_n(x) \to 0$ as $n \to \infty$.

^prop-31-1

> [!proof]+ Proof
> $s_{n-1}(x) = f(x) - R_n(x)$, so $s_{n-1}(x) \to f(x) \iff R_n(x) \to 0$.

^pf-31-1

> [!remark]- Connections
> - Computational version: [[§78 Taylor and Maclaurin Series#^thm-78-3|Calc Thm. §78.3]] (with worked examples).

The problem is now to *estimate* $R_n(x)$. Taylor proved the basic theorem — which is why the series bears his name:

> [!theorem] Theorem §31.2: Taylor's Theorem with Lagrange Remainder
> Suppose $f: (a,b) \to \mathbb{R}$ with $0 \in (a,b)$, and $f', f^{(2)}, \ldots, f^{(n)}$ exist on $(a,b)$. Then for every $x \in (a,b)$ there exists $y$ between $0$ and $x$ such that
>
> $$
> R_n(x) = \frac{f^{(n)}(y)}{n!}\, x^n.
> $$

^thm-31-2

This is quite important and useful: to prove convergence of the Taylor series, we only need to *bound the derivatives* $f^{(n)}$.

> [!proof]+ Proof
> We only need $x \neq 0$: for $x = 0$, $R_n(0) = 0$ and the formula holds trivially. Assume $x > 0$ (the case $x < 0$ is similar).
>
> Since $x^n \neq 0$, there is a *unique* number $M$ solving
>
> $$
> f(x) = \sum_{k=0}^{n-1} \frac{f^{(k)}(0)}{k!}\, x^k + \frac{M x^n}{n!};
> $$
>
> it suffices to show $f^{(n)}(y) = M$ for some $y$ between $0$ and $x$. Following the recurring pattern — define a new function and hunt for critical points — let, for $t \in [0, x]$,
>
> $$
> g(t) = \sum_{k=0}^{n-1} \frac{f^{(k)}(0)}{k!}\, t^k + \frac{M t^n}{n!} - f(t).
> $$
>
> Check the derivatives of $g$ at $0$: for $j < n$, differentiating the polynomial part $j$ times and setting $t = 0$ leaves exactly the coefficient $f^{(j)}(0)$ (the $M$-term contributes $0$ since $j < n$), so
>
> $$
> g^{(j)}(0) = f^{(j)}(0) - f^{(j)}(0) = 0, \qquad j = 0, 1, \ldots, n-1.
> $$
>
> Also $g(x) = 0$, by the choice of $M$.
>
> Now iterate Rolle's theorem. From $g(0) = g(x) = 0$: some $x_1 \in (0, x)$ has $g'(x_1) = 0$. From $g'(0) = g'(x_1) = 0$: some $x_2 \in (0, x_1)$ has $g^{(2)}(x_2) = 0$. By induction, we get $x_n \in (0, x_{n-1}) \subseteq (0, x)$ with
>
> $$
> g^{(n)}(x_n) = 0.
> $$
>
> Finally, differentiating $g$ exactly $n$ times kills the whole polynomial of degree $< n$ and reduces the $M$-term to a constant:
>
> $$
> g^{(n)}(t) = M - f^{(n)}(t), \qquad \text{so} \qquad M = f^{(n)}(x_n).
> $$
>
> Take $y = x_n$. Done!

^pf-31-2

> [!remark] Remark
> If we can show $R_n(x) \to 0$, we solve both problems at one stroke: the Taylor series converges, *and* it converges to $f(x)$.

^rem-31-1

> [!remark]- Connections
> - Two-variable version, proved by applying this theorem along a segment: [[§9 Taylor's Theorem for Multivariable Functions#^thm-9-2|452 Thm. §9.2]].
> - Computational version: Taylor's Inequality, [[§78 Taylor and Maclaurin Series#^thm-78-4|Calc Thm. §78.4]] (with worked examples).

## Two Instructive Examples

> [!example] Example §31.1: The cosine converges to itself everywhere (HW)
> The derivatives of $\cos$ cycle with period four, so at $0$: $\cos^{(2n)}(0) = (-1)^n$, $\cos^{(2n+1)}(0) = 0$, and the Taylor series is
>
> $$
> \sum_{n=0}^\infty \frac{(-1)^n}{(2n)!}\, x^{2n}.
> $$
>
> Does it converge *to* $\cos x$? Every derivative of $\cos$ is $\pm\sin$ or $\pm\cos$, hence bounded by $1$, so the Lagrange remainder obeys, for every $x$,
>
> $$
> |R_n(x)| = \left| \frac{\cos^{(n)}(c)}{n!}\, x^n \right| \leq \frac{|x|^n}{n!} \longrightarrow 0,
> $$
>
> since $\tfrac{|x|^n}{n!}$ is the general term of a series convergent by the ratio test (ratio $\tfrac{|x|}{n+1} \to 0$), and terms of a convergent series tend to zero (§14). So $\cos x$ equals its Taylor series for *all* $x \in \mathbb{R}$ — and, since the derivative bound was all we used, the identical estimate with the bound $e^{|x|}$ in place of $1$ gives $e^x = \sum_{n\geq0} \tfrac{x^n}{n!}$ on all of $\mathbb{R}$ as well; adding and subtracting the series for $e^{\pm x}$ then yields $\cosh x = \sum \tfrac{x^{2n}}{(2n)!}$ and $\sinh x = \sum \tfrac{x^{2n+1}}{(2n+1)!}$ (HW).

^ex-31-1

> [!remark]- Connections
> - Computational version: [[§78 Taylor and Maclaurin Series#^thm-78-8|Calc Thm. §78.8]]; the same estimate for $e^x$, [[§78 Taylor and Maclaurin Series#^thm-78-6|Calc Thm. §78.6]].

> [!example] Example §31.2: The logarithm
> Show that for $x \in [0,1]$, the Taylor series of $f(x) = \log(1+x)$ converges to $\log(1+x)$.
>
> Compute derivatives:
>
> $$
> f'(x) = (1+x)^{-1},\quad f^{(2)}(x) = -(1+x)^{-2},\quad f^{(3)}(x) = 2!\,(1+x)^{-3},\ \ldots
> $$
>
> and in general
>
> $$
> f^{(n)}(x) = (-1)^{n-1}(n-1)!\,(1+x)^{-n}, \qquad f^{(n)}(0) = (-1)^{n-1}(n-1)!.
> $$
>
> With $f(0) = 0$, the Taylor series is
>
> $$
> \sum_{n=1}^\infty \frac{(-1)^{n-1}(n-1)!}{n!}\, x^n = \sum_{n=1}^\infty (-1)^{n-1} \frac{x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots,
> $$
>
> with radius $R = 1$ (as $\left(\tfrac1n\right)^{1/n} \to 1$) — matching the series found in §26. Now, for $x \in [0,1]$, Taylor's theorem gives $y$ with $0 \leq y \leq x$ and
>
> $$
> |R_n(x)| = \left| \frac{(-1)^{n-1}(n-1)!\,(1+y)^{-n}}{n!}\, x^n \right| = \frac1n \left( \frac{x}{1+y} \right)^n \leq \frac1n \longrightarrow 0,
> $$
>
> using $x \leq 1 \leq 1 + y$. So the Taylor series converges to $\log(1+x)$ on $[0,1]$.
>
> *Why does this argument fail on $(-1, 0)$?* There $y$ lies between $x$ and $0$ with $x < 0$, and $\tfrac{|x|}{1+y}$ can exceed $1$ (for $x$ near $-1$ and $y$ near $x$, the denominator is tiny) — the bound on $R_n$ is lost. Yet the conclusion is still *true* on $(-1,0)$! The proof goes by a different route:
>
> $$
> \log(1+x) = \int_0^x \frac{dt}{1+t}, \qquad \frac{1}{1+t} = \sum_{n=0}^\infty (-1)^n t^n \ (|t| < 1),
> $$
>
> and term-by-term integration of power series (§26). So you see — even when something is true, it may not be easy to prove by the standard method.

^ex-31-2

> [!example] Example §31.3: A smooth function that is not its Taylor series
> We construct $g: \mathbb{R} \to \mathbb{R}$ with derivatives of all orders everywhere, whose Taylor series at $0$ converges for all $x$ (radius $R = \infty$) — but not to $g(x)$. Let
>
> $$
> g(x) = e^{-1/x^2} \ (x \neq 0), \qquad g(0) = 0.
> $$
>
> When $x \approx 0$, $\tfrac{1}{x^2}$ is very large, so $e^{-1/x^2}$ is very small — that is why $g$ is continuous at $0$ (and of course everywhere else). At $0$, compute by definition:
>
> $$
> g'(0) = \lim_{x\to0} \frac{e^{-1/x^2}}{x} = 0
> $$
>
> (several ways: substitute $t = \tfrac1x$, so the quotient is $\pm t\, e^{-t^2} \to 0$ as $|t| \to \infty$ — exponential beats polynomial). For $x \neq 0$, $g'(x) = e^{-1/x^2}\cdot\tfrac{2}{x^3}$, and by induction every derivative of $g$ for $x \neq 0$ has the form (rational function)$\cdot e^{-1/x^2}$, whence the same substitution gives
>
> $$
> g^{(n)}(0) = 0 \qquad \text{for all } n.
> $$
>
> So the Taylor series of $g$ at $0$ is $\sum_n 0 \cdot x^n \equiv 0$ — convergent everywhere, but equal to $g(x)$ *only* at $x = 0$, since $g(x) > 0$ for $x \neq 0$. This realizes problem (2). Such functions are very important in advanced mathematics: they are the seeds of *smooth cutoff functions*.

^ex-31-3

![[m451-31-1.svg]]
*The two extremes of §31. Left: the partial sums $s_2, s_4, s_8$ (light blue, blue, red) hug $\cos x$ (black) order by order — the remainder dies everywhere. Right: $e^{-1/x^2}$ and its Taylor series (dashed, identically $0$) are visually indistinguishable near the origin — infinitely flat — yet equal only at the single point $x = 0$.*

> [!remark]- Connections
> - Computational version: Stewart's remark on $e^{-1/x^2}$, [[§78 Taylor and Maclaurin Series#^rem-78-1|Calc Remark §78.1]].
