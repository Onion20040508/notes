---
subject: "[[Single Variable Analysis]]"
section: 26
chapter: 4
tags: [real-analysis, math451]
---
← [[§25 More on Uniform Convergence]] · ↑ [[· 4 Sequences and Series of Functions]] · [[§27 Weierstrass's Approximation Theorem (Not Covered)]] →

We now apply the machinery of §24–§25 to power series — with striking consequences.

> [!theorem] Theorem §26.1: Uniform Convergence on Smaller Closed Intervals
> If $\sum_n a_n x^n$ has radius of convergence $R > 0$, then for every $R_1$ with $0 < R_1 < R$, the series converges uniformly on $[-R_1, R_1]$.

^thm-26-1

> [!proof]+ Proof
> *Step 1:* the series $\sum_n |a_n| x^n$ has the *same* radius of convergence $R$. Why? Because $\bigl||a_n|\bigr|^{1/n} = |a_n|^{1/n}$, so the two series have the same $\beta$, hence the same $R$.
>
> *Step 2:* since $R_1 < R$, the point $x = R_1$ lies inside the interval of convergence of $\sum |a_n| x^n$, so
>
> $$
> \sum_n |a_n| R_1^n \quad \text{converges}.
> $$
>
> *Step 3:* apply the Weierstrass M-test with $M_n = |a_n| R_1^n$: for all $x \in [-R_1, R_1]$,
>
> $$
> |a_n x^n| \leq |a_n| R_1^n.
> $$

^pf-26-1

> [!remark]- Connections
> - Computational version: [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-3|342 Thm. §69.3]] (uniform convergence on closed disks inside the circle of convergence).

> [!theorem] Corollary §26.2: Power Series Are Continuous
> $f(x) = \sum_n a_n x^n$ is a continuous function on $(-R, R)$.

^cor-26-2

> [!proof]+ Proof
> Let $x_0 \in (-R, R)$; choose $R_1$ with $|x_0| < R_1 < R$. On $[-R_1, R_1]$ the series converges uniformly (theorem above), and the partial sums are polynomials, hence continuous — so the sum is continuous on $[-R_1, R_1]$ (§25), in particular at $x_0$. Since $x_0$ was arbitrary and continuity is a pointwise property, $f$ is continuous on $(-R,R)$. (Note: uniformity on all of $(-R,R)$ may fail — §25's geometric example — but is not needed.)

^pf-26-2

> [!remark]- Connections
> - Computational version: [[§70★ Continuity of Sums of Power Series#^thm-70-1|342 Thm. §70.1]] (continuity of the sum of a complex power series).

## Term-by-Term Integration

> [!theorem] Theorem §26.3: Integrating a Uniformly Convergent Series
> Suppose all $g_n$ are continuous on a finite interval $[a,b]$ and $\sum_{n=0}^\infty g_n(x)$ converges uniformly on $[a,b]$. Then
>
> $$
> \int_a^b \sum_{n=0}^\infty g_n(x)\,dx = \sum_{n=0}^\infty \int_a^b g_n(x)\,dx.
> $$

^thm-26-3

> [!proof]+ Proof
> Let $s_n(x) = \sum_{k=0}^n g_k(x)$; then $s_n$ converges uniformly to the sum $g$. By the exchange theorem of §25 and the linearity of the integral over *finite* sums,
>
> $$
> \int_a^b g = \int_a^b \lim_n s_n = \lim_n \int_a^b s_n = \lim_n \sum_{k=0}^n \int_a^b g_k = \sum_{k=0}^\infty \int_a^b g_k.
> $$

^pf-26-3

> [!remark]- Connections
> - In 551 term-by-term integration needs no uniform convergence: for non-negative terms it is [[§14 The Lebesgue Integral for Simple Functions#^thm-14-12|551 Thm. §14.12]] (MCT II), and for absolutely integrable series [[§15 The General Lebesgue Integral#^cor-15-9|551 Cor. §15.9]].
> - Fourier-series version: [[§10 Operations on Fourier Series#^thm-10-3|341 Thm. §10.3]] (a Fourier series may be integrated term by term even when it does not converge uniformly), with worked examples.
> - Computational version for power series along contours: [[§71★ Integration and Differentiation of Power Series#^thm-71-1|342 Thm. §71.1]] (term-by-term integration, with worked examples).

> [!theorem] Theorem §26.4: Term-by-Term Calculus for Power Series
> Let $f(x) = \sum_{n=0}^\infty a_n x^n$ have radius of convergence $R > 0$. Then:
>
> 1. for all $x \in (-R, R)$,
>
>    $$
>    \int_0^x f(t)\,dt = \sum_{n=0}^\infty \frac{a_n}{n+1}\, x^{n+1};
>    $$
>
> 2. $f$ is differentiable on $(-R,R)$, with
>
>    $$
>    f'(x) = \sum_{n=1}^\infty n\, a_n x^{n-1}
>    $$
>
>    (the $n = 0$ term is dropped). Both new series again have radius of convergence $R$.

^thm-26-4

> [!proof]+ Proof
> (1) Fix $x \in (-R,R)$ and choose $R_1$ with $|x| < R_1 < R$. The closed interval between $0$ and $x$ lies in $[-R_1, R_1]$, where the series converges uniformly and the terms $a_n t^n$ are continuous; the previous theorem allows the exchange:
>
> $$
> \int_0^x f(t)\,dt = \int_0^x \sum_{n=0}^\infty a_n t^n\,dt = \sum_{n=0}^\infty \int_0^x a_n t^n\,dt = \sum_{n=0}^\infty \frac{a_n}{n+1} x^{n+1}.
> $$
>
> (2) First: the differentiated series $\sum_{n\geq1} n a_n x^{n-1}$ still has radius of convergence $R$, since
>
> $$
> \limsup_n |n a_n|^{1/n} = \limsup_n\, n^{1/n} |a_n|^{1/n} = \beta,
> $$
>
> using $n^{1/n} \to 1$ (§9). Let $g(x) = \sum_{n\geq1} n a_n x^{n-1}$, continuous on $(-R,R)$ by the corollary. Apply part (1) to $g$: for $x \in (-R,R)$,
>
> $$
> \int_0^x g(t)\,dt = \sum_{n=1}^\infty \frac{n a_n}{n}\, x^{n} = \sum_{n=0}^\infty a_n x^n - a_0 = f(x) - f(0).
> $$
>
> By the **[[Fundamental Theorem of Calculus|Fundamental Theorem of Calculus]]** (used here on credit; proved in Part III), the left side is differentiable in $x$ with derivative $g(x)$; hence so is the right side, and $f'(x) = g(x)$. Done.

^pf-26-4

> [!remark]- Connections
> - The differentiation half has a 551 analogue for series of absolutely continuous functions: [[§18 Differentiation Theory#^cor-18-14|551 Cor. §18.14]].
> - Computational version: [[§77 Representations of Functions as Power Series#^thm-77-1|Calc Thm. §77.1]] (with worked examples).
> - Used in ODEs: each entry of $e^{\mathbf{A}t} = \sum_k \mathbf{A}^kt^k/k!$ is a power series in $t$ with infinite radius, differentiated term by term to get $\Phi' = \mathbf{A}\Phi$: [[§33★ Fundamental Matrices#^def-33-3|331 Def. §33.3]], [[§33★ Fundamental Matrices#^thm-33-3|331 Thm. §33.3]].
> - Fourier-series counterpart: [[§10 Operations on Fourier Series#^thm-10-6|341 Thm. §10.6]] and [[§10 Operations on Fourier Series#^thm-10-7|341 Thm. §10.7]] (differentiation multiplies the $n$th coefficient by $n$, so it needs a continuous periodic extension or fast-decaying coefficients).
> - Used in PDEs: the Bessel series is differentiated term by term to show that $J_\mu$ solves Bessel's equation, [[§45★ Bessel's Equation#^thm-45-2|341 Thm. §45.2]], and to get the derivative formulas, [[§45★ Bessel's Equation#^thm-45-7|341 Thm. §45.7]].
> - Computational version: [[§71★ Integration and Differentiation of Power Series#^thm-71-4|342 Thm. §71.4]] (term-by-term differentiation) and [[§71★ Integration and Differentiation of Power Series#^thm-71-1|342 Thm. §71.1]] (term-by-term integration) for complex power series.

## Harvesting Closed Formulas

> [!example] Example §26.1: Differentiating the geometric series
> Find a closed formula for $\sum_{n=1}^\infty n x^n$, $|x| < 1$. Start from $\sum_{n=0}^\infty x^n = \tfrac{1}{1-x}$ and differentiate term by term (part (2)):
>
> $$
> \sum_{n=1}^\infty n x^{n-1} = \frac{1}{(1-x)^2}.
> $$
>
> Multiply by $x$ (and note the $n = 0$ term vanishes anyway):
>
> $$
> \sum_{n=1}^\infty n x^n = \frac{x}{(1-x)^2}, \qquad |x| < 1. \tag*{$\blacksquare$}
> $$

^ex-26-1

> [!example] Example §26.2: Integrating the geometric series
> Find a closed formula for $\sum_{n=1}^\infty \tfrac{x^n}{n}$, $|x| < 1$. Integrate $\sum_{n=0}^\infty t^n = \tfrac{1}{1-t}$ from $0$ to $x$ (part (1)):
>
> $$
> \sum_{n=0}^\infty \frac{x^{n+1}}{n+1} = \int_0^x \frac{dt}{1-t} = -\ln(1-x),
> $$
>
> and re-index $n+1 \mapsto n$:
>
> $$
> \sum_{n=1}^\infty \frac{x^n}{n} = -\ln(1-x), \qquad |x| < 1.
> $$
>
> (The evaluation of the integral uses the logarithm from calculus, on the usual credit.)

^ex-26-2

> [!example] Example §26.3: The arctangent series (HW)
> The geometric series evaluated at $-t^2$ (a point substitution, legitimate for $|t| < 1$) gives
>
> $$
> \frac{1}{1+t^2} = \sum_{n=0}^\infty (-1)^n t^{2n}, \qquad |t| < 1,
> $$
>
> and term-by-term integration from $0$ to $x$ yields
>
> $$
> \arctan x = \int_0^x \frac{dt}{1+t^2} = \sum_{n=0}^\infty \frac{(-1)^n}{2n+1}\, x^{2n+1}, \qquad |x| < 1
> $$
>
> [the evaluation of the integral uses $\arctan' = \tfrac{1}{1+x^2}$, proved in §29 via the Inverse Function Theorem]. At $x = 1$ the right side becomes Leibniz's celebrated
>
> $$
> 1 - \frac13 + \frac15 - \frac17 + \cdots = \frac\pi4,
> $$
>
> convergent by the Alternating Series Test (§15) — but justifying the *value* at the endpoint, where $|x| < 1$ no longer protects the termwise integration, requires Abel's theorem (Ross §26), which these notes do not cover: one more entry on the ledger.

^ex-26-3

![[m451-26-1.svg]]
*Partial sums $S_N(x) = \sum_{n=0}^{N} \frac{(-1)^n}{2n+1} x^{2n+1}$ for $N = 2, 6, 15$ (blue, darker as $N$ grows) against $\arctan x$ (black). On $(-1,1)$ they close in on $\arctan x$; for $|x| > 1$ (shaded) the terms do not tend to $0$ and the partial sums break away, in directions alternating with the sign of the last term — although $\arctan$ itself is perfectly smooth there. The radius $R = 1$ is a property of the series, not visible in the graph of the function.*

> [!remark]- Connections
> - Worked examples: the derivative of arctan, [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-8|Calc Thm. §19.8]]; the arctangent series by term-by-term integration, [[§77 Representations of Functions as Power Series#^ex-77-3|Calc Ex. §77.3]].

> [!example] Example §26.4: The Taylor series of the logarithm
> Find the Taylor series of $f(x) = \ln(1+x)$ at $0$. It is easier to start with the derivative:
>
> $$
> f'(x) = \frac{1}{1+x} = \frac{1}{1 - (-x)} = \sum_{n=0}^\infty (-x)^n = \sum_{n=0}^\infty (-1)^n x^n, \qquad |x| < 1.
> $$
>
> Integrating from $0$ to $x$:
>
> $$
> \ln(1+x) = \sum_{n=0}^\infty \frac{(-1)^n}{n+1}\, x^{n+1} = \sum_{n=1}^\infty (-1)^{n-1} \frac{x^n}{n}, \qquad |x| < 1. \tag*{$\blacksquare$}
> $$

^ex-26-4

> [!remark]- Connections
> - Worked examples: the logarithm series by term-by-term integration, [[§77 Representations of Functions as Power Series#^ex-77-3|Calc Ex. §77.3]].

> [!example] Example §26.5: Summing numerical series
> The closed formula $\sum_{n\geq1} n x^n = \tfrac{x}{(1-x)^2}$ evaluates series that are not easy to sum directly. At $x = \tfrac12$:
>
> $$
> \sum_{n=1}^\infty \frac{n}{2^n} = \frac{1/2}{(1 - 1/2)^2} = \frac{1/2}{1/4} = 2.
> $$
>
> Similarly, at $x = \tfrac13$:
>
> $$
> \sum_{n=1}^\infty \frac{n}{3^n} = \frac{1/3}{(2/3)^2} = \frac{1/3}{4/9} = \frac34. \tag*{$\blacksquare$}
> $$

^ex-26-5

> [!example] Example §26.6: Iterating the trick (HW)
> Differentiating $\sum_{n \geq 1} n x^n = \tfrac{x}{(1-x)^2}$ once more (term-by-term, same radius $R = 1$) gives $\sum n^2 x^{n-1} = \tfrac{d}{dx} \tfrac{x}{(1-x)^2} = \tfrac{1+x}{(1-x)^3}$, hence
>
> $$
> \sum_{n=1}^\infty n^2 x^n = \frac{x(1+x)}{(1-x)^3}, \qquad |x| < 1.
> $$
>
> At $x = \tfrac12$ and $x = \tfrac13$:
>
> $$
> \sum_{n=1}^\infty \frac{n^2}{2^n} = \frac{\tfrac12 \cdot \tfrac32}{(\tfrac12)^3} = 6, \qquad
> \sum_{n=1}^\infty \frac{n^2}{3^n} = \frac{\tfrac13 \cdot \tfrac43}{(\tfrac23)^3} = \frac32.
> $$
>
> Every further power of $n$ costs one more differentiation; every moment $\sum n^k x^n$ is reachable this way.

^ex-26-6

> [!example] Example §26.7: An integral with no elementary antiderivative (HW)
> The function $e^{-t^2}$ (with $e^y = \sum_{n\geq0} \tfrac{y^n}{n!}$ on the usual credit) famously has no antiderivative expressible in elementary functions — yet its integral has a completely explicit *power series*. Substituting the value $y = -t^2$ into the exponential series (a legitimate evaluation at a point, not a formal manipulation):
>
> $$
> e^{-t^2} = \sum_{n=0}^\infty \frac{(-t^2)^n}{n!} = \sum_{n=0}^\infty \frac{(-1)^n}{n!}\, t^{2n}, \qquad t \in \mathbb{R} \quad (R = +\infty),
> $$
>
> and the term-by-term integration theorem applies on every $[0, x]$:
>
> $$
> F(x) = \int_0^x e^{-t^2}\,dt = \sum_{n=0}^\infty \frac{(-1)^n}{n!} \int_0^x t^{2n}\,dt = \sum_{n=0}^\infty \frac{(-1)^n}{n!\,(2n+1)}\, x^{2n+1}, \qquad x \in \mathbb{R}.
> $$
>
> (Up to normalization this is the Gaussian error function of probability theory.) Power series thus genuinely *extend* the toolkit of named functions: what the elementary closed forms cannot express, a series can.

^ex-26-7

> [!remark]- Connections
> - Computational version: the same integral normalized as the error function, $\operatorname{erf}(x)=\frac{2}{\sqrt\pi}\int_0^xe^{-y^2}\,dy$, [[§28★ The Error Function#^def-28-1|341 Def. §28.1]], used for heat flow in a long rod.

> [!example] Example §26.8: Sine and cosine from scratch (HW)
> The trigonometric functions have run on credit since §17. Here is the first installment of repayment: *define*
>
> $$
> s(x) = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!}\, x^{2n+1}, \qquad
> c(x) = \sum_{n=0}^\infty \frac{(-1)^n}{(2n)!}\, x^{2n},
> $$
>
> and prove $s^2 + c^2 = 1$ using nothing but this chapter — no triangles, no credit.
>
> *Radius.* Both series have gaps, so test the whole terms (§23): for $s$, the ratio of consecutive terms is $\tfrac{|x|^2}{(2n+2)(2n+3)} \to 0$ for every $x$, so $R = +\infty$; likewise for $c$.
>
> *Derivatives.* Term-by-term differentiation is legal on all of $\mathbb{R}$:
>
> $$
> s'(x) = \sum_{n=0}^\infty \frac{(-1)^n (2n+1)}{(2n+1)!}\, x^{2n} = \sum_{n=0}^\infty \frac{(-1)^n}{(2n)!}\, x^{2n} = c(x),
> $$
>
> and, differentiating $c$ (the constant term drops; reindex $n = m+1$):
>
> $$
> c'(x) = \sum_{n=1}^\infty \frac{(-1)^n}{(2n-1)!}\, x^{2n-1} = \sum_{m=0}^\infty \frac{(-1)^{m+1}}{(2m+1)!}\, x^{2m+1} = -s(x).
> $$
>
> *Pythagoras.* Let $F = s^2 + c^2$; by the product rule and the two identities,
>
> $$
> F' = 2ss' + 2cc' = 2sc - 2cs = 0 \quad \text{on } \mathbb{R}.
> $$
>
> A function with vanishing derivative on an interval is constant [borrowed from the [[Mean Value Theorem|MVT]] corollary of §29]; and $F(0) = s(0)^2 + c(0)^2 = 0 + 1 = 1$. So
>
> $$
> s(x)^2 + c(x)^2 = 1 \qquad \text{for all } x \in \mathbb{R}. \tag*{$\blacksquare$}
> $$

^ex-26-8

> [!remark]- Connections
> - Computational version: the derivative of sine, [[§16 Derivatives of Trigonometric Functions#^thm-16-1|Calc Thm. §16.1]]; the Maclaurin series of sine and cosine, [[§78 Taylor and Maclaurin Series#^thm-78-7|Calc Thm. §78.7]], [[§78 Taylor and Maclaurin Series#^thm-78-8|Calc Thm. §78.8]].
> - Computational version: [[§64 Examples (Proof of Taylor's Theorem)#^prop-64-1|342 Prop. §64.1]] (the Maclaurin series of eᶻ, sin z, cos z and others, derived from the complex definitions).

> [!remark] Remark: Repaying the trigonometric debt
> Of course $s = \sin$ and $c = \cos$ — but the point is that the computation above never used that. Ross §37 carries this program to completion: starting from the two series one derives the addition formulas, the existence of $\pi$ (as twice the first positive zero of $c$), and periodicity, so that *every* property of $\sin$ and $\cos$ used on credit in these notes is ultimately redeemable. The same holds for $e^x$ and $\log$ via their series and inverses. The ledger of §34 records what remains outstanding.

^rem-26-1

> [!remark]- Connections
> - Stewart builds the same functions differently: trigonometric functions from angles, [[§119 Trigonometry#^def-119-4|Calc Def. §119.4]]; ln as an integral, [[§121 The Logarithm Defined as an Integral#^def-121-1|Calc Def. §121.1]].
