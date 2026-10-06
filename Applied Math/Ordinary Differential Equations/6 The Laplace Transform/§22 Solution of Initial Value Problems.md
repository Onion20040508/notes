---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 6
section: 22
bdp: "6.2"
aliases: ["BDP 6.2"]
tags: [ordinary-differential-equations, math331]
---
← [[§21 Definition of the Laplace Transform]] · ↑ [[· 6 The Laplace Transform]] · [[§23 Step Functions]] →

*Boyce–DiPrima, Section 6.2 · MATH 331 Written HW 5 (Problem 2), Final Exam (Fall 2021, Q3), Course Review (Laplace table).*

The Laplace transform turns differentiation into multiplication by $s$: $\mathcal{L}\{f'\} = s\mathcal{L}\{f\} - f(0)$. Applied to a linear equation with constant coefficients, this turns an initial value problem into an algebraic equation for the transform $Y(s)$ of the solution, with the initial conditions built in. Solving for $Y(s)$ is algebra; the work lies in inverting it, which is done by splitting $Y(s)$ (partial fractions, completing the square) into entries of a table of known transforms, Table 6.2.1. Inversion is unambiguous because a continuous function is determined by its transform.

## The Transform of a Derivative

> [!theorem] Theorem §22.1: Transform of a Derivative
> Suppose that $f$ is continuous and $f'$ is piecewise continuous on any interval $0 \le t \le A$. Suppose further that there exist constants $K$, $a$ and $M$ such that $|f(t)| \le Ke^{at}$ for $t \ge M$. Then $\mathcal{L}\{f'(t)\}$ exists for $s > a$, and moreover
>
> $$
> \mathcal{L}\{f'(t)\} = s\mathcal{L}\{f(t)\} - f(0) . \qquad (1)
> $$
>
> *BDP: Theorem 6.2.1*

^thm-22-1

> [!proof]+ Proof
> Fix $s > a$. By [[§21 Definition of the Laplace Transform#^thm-21-2|Theorem §21.2]], $\mathcal{L}\{f(t)\}$ exists, since $f$ is continuous and of exponential order. Consider
>
> $$
> \int_0^A e^{-st}f'(t)\,dt ,
> $$
>
> whose limit as $A \to \infty$, if it exists, is $\mathcal{L}\{f'(t)\}$. Let $t_1 < t_2 < \cdots < t_k$ be the points of discontinuity of $f'$ in $(0, A)$, and put $t_0 = 0$, $t_{k+1} = A$. Then
>
> $$
> \int_0^A e^{-st}f'(t)\,dt = \sum_{i=0}^{k} \int_{t_i}^{t_{i+1}} e^{-st}f'(t)\,dt .
> $$
>
> On each $[t_i, t_{i+1}]$, $f$ is continuous and differentiable inside with $f'$ continuous and bounded there, so integration by parts applies (with $u = e^{-st}$, $dv = f'(t)\,dt$):
>
> $$
> \int_{t_i}^{t_{i+1}} e^{-st}f'(t)\,dt = e^{-st}f(t)\Big|_{t_i}^{t_{i+1}} + s\int_{t_i}^{t_{i+1}} e^{-st}f(t)\,dt .
> $$
>
> Add these. **Because $f$ is continuous**, the boundary terms telescope: the term $e^{-st_i}f(t_i)$ appears once with each sign at every interior point $t_1, \ldots, t_k$, and only the ends survive. The integrals combine into one, so
>
> $$
> \int_0^A e^{-st}f'(t)\,dt = e^{-sA}f(A) - f(0) + s\int_0^A e^{-st}f(t)\,dt . \qquad (2)
> $$
>
> Now let $A \to \infty$. The integral on the right tends to $\mathcal{L}\{f(t)\}$. For $A \ge M$, $|f(A)| \le Ke^{aA}$, so $|e^{-sA}f(A)| \le Ke^{-(s - a)A} \to 0$ because $s > a$. Hence the right side of (2) tends to $s\mathcal{L}\{f(t)\} - f(0)$. So the left side also has a limit, that is, $\mathcal{L}\{f'(t)\}$ exists, and it equals $s\mathcal{L}\{f(t)\} - f(0)$.

^pf-22-1

*Uses:* [[§21 Definition of the Laplace Transform#^thm-21-2|§21.2]], [[§21 Definition of the Laplace Transform#^def-21-4|Def. §21.4]], [[§44 Integration by Parts#^thm-44-1|Calc Thm. §44.1]] (integration by parts)

> [!remark]- Connections
> - Integration by parts with $f$ only piecewise smooth: [[§34 Fundamental Theorem of Calculus#^thm-34-3|451 Thm. §34.3]] requires $u, v$ continuous on $[t_i, t_{i+1}]$, differentiable inside, with integrable derivatives, which is exactly the situation on each piece.
> - Continuity of $f$ is essential: if $f$ jumps at $t_i$, the boundary terms no longer cancel and each jump contributes $-e^{-st_i}\big(f(t_i^+) - f(t_i^-)\big)$; step functions are handled by the shift theorem [[§23 Step Functions#^thm-23-2|Theorem §23.2]] instead.
> - PDE version: [[§53★ Partial Differential Equations#^thm-53-1|341 Thm. §53.1]] (for $u(x, t)$ the $t$-derivatives follow this rule and the $x$-derivatives pass through the transform); the same rule in Powers: [[§51★ Definition and Elementary Properties#^thm-51-4|341 Thm. §51.4]].

Applying (1) to $f'$ (if $f'$ and $f''$ satisfy the conditions imposed on $f$ and $f'$) gives
$$
\mathcal{L}\{f''(t)\} = s\mathcal{L}\{f'(t)\} - f'(0) = s\big(s\mathcal{L}\{f(t)\} - f(0)\big) - f'(0) = s^2\mathcal{L}\{f(t)\} - sf(0) - f'(0) , \qquad (3)
$$
and in general:

> [!theorem] Corollary §22.2: Transform of the nth Derivative
> Suppose that the functions $f, f', \ldots, f^{(n-1)}$ are continuous and that $f^{(n)}$ is piecewise continuous on any interval $0 \le t \le A$. Suppose further that there exist constants $K$, $a$ and $M$ such that $|f(t)| \le Ke^{at}$, $|f'(t)| \le Ke^{at}$, …, $|f^{(n-1)}(t)| \le Ke^{at}$ for $t \ge M$. Then $\mathcal{L}\{f^{(n)}(t)\}$ exists for $s > a$ and is given by
>
> $$
> \mathcal{L}\{f^{(n)}(t)\} = s^n\mathcal{L}\{f(t)\} - s^{n-1}f(0) - \cdots - sf^{(n-2)}(0) - f^{(n-1)}(0) . \qquad (4)
> $$
>
> *BDP: Corollary 6.2.2*

^cor-22-2

> [!proof]+ Proof
> Induction on $n$; the case $n = 1$ is Theorem §22.1. Assume (4) for $n - 1$ (whose hypotheses are contained in those for $n$). Apply [[§22 Solution of Initial Value Problems#^thm-22-1|Theorem §22.1]] to $g = f^{(n-1)}$: it is continuous, $g' = f^{(n)}$ is piecewise continuous, and $|g(t)| \le Ke^{at}$ for $t \ge M$. So for $s > a$,
>
> $$
> \mathcal{L}\{f^{(n)}\} = s\mathcal{L}\{f^{(n-1)}\} - f^{(n-1)}(0) = s\big(s^{n-1}\mathcal{L}\{f\} - s^{n-2}f(0) - \cdots - f^{(n-2)}(0)\big) - f^{(n-1)}(0) ,
> $$
>
> which is (4).

^pf-22-2

*Uses:* [[§22 Solution of Initial Value Problems#^thm-22-1|§22.1]]

## Solving Initial Value Problems

The method is most useful for nonhomogeneous equations (from [[§23 Step Functions|§23]] on), but it is clearest first on homogeneous ones.

> [!example] Example §22.1: The Same Problem Two Ways
> Solve $y'' - y' - 2y = 0$, $y(0) = 1$, $y'(0) = 0$. (5), (6)
>
> **By Chapter 3.** $r^2 - r - 2 = (r - 2)(r + 1) = 0$, so $y = c_1e^{-t} + c_2e^{2t}$. The conditions $c_1 + c_2 = 1$ and $-c_1 + 2c_2 = 0$ give $c_1 = \frac23$, $c_2 = \frac13$:
>
> $$
> y = \frac23 e^{-t} + \frac13 e^{2t} . \qquad (8)
> $$
>
> **By the Laplace transform.** Assume that the solution $y$, with its first two derivatives, satisfies the conditions of Corollary §22.2. Transforming the equation, using linearity ([[§21 Definition of the Laplace Transform#^thm-21-3|Theorem §21.3]]) and (3), with $Y(s) = \mathcal{L}\{y\}$:
>
> $$
> s^2Y - sy(0) - y'(0) - \big(sY - y(0)\big) - 2Y = 0, \quad\text{i.e.}\quad (s^2 - s - 2)Y(s) + (1 - s)y(0) - y'(0) = 0 . \qquad (10)
> $$
>
> With $y(0) = 1$, $y'(0) = 0$:
>
> $$
> Y(s) = \frac{s - 1}{s^2 - s - 2} = \frac{s - 1}{(s - 2)(s + 1)} . \qquad (11)
> $$
>
> **Partial fractions.** Write $\dfrac{s - 1}{(s - 2)(s + 1)} = \dfrac{a}{s - 2} + \dfrac{b}{s + 1}$, so $s - 1 = a(s + 1) + b(s - 2)$ for all $s$. At $s = 2$: $1 = 3a$, $a = \frac13$. At $s = -1$: $-2 = -3b$, $b = \frac23$. So
>
> $$
> Y(s) = \frac{1/3}{s - 2} + \frac{2/3}{s + 1} .
> $$
>
> **Invert.** By [[§21 Definition of the Laplace Transform#^ex-21-2|Example §21.2]], $\frac13 e^{2t}$ has transform $\frac13(s - 2)^{-1}$ and $\frac23 e^{-t}$ has transform $\frac23(s + 1)^{-1}$, so by linearity $y(t) = \frac13 e^{2t} + \frac23 e^{-t}$, as before. It does satisfy the conditions of [[§22 Solution of Initial Value Problems#^cor-22-2|Corollary §22.2]], as assumed.
>
> *BDP: Example 6.2.1*

^ex-22-1

> [!theorem] Proposition §22.3: The Transformed Second-Order Equation
> If the solution $y$ of $ay'' + by' + cy = f(t)$ (14) satisfies the conditions of [[§22 Solution of Initial Value Problems#^cor-22-2|Corollary §22.2]] for $n = 2$, and $F(s) = \mathcal{L}\{f(t)\}$, then $Y(s) = \mathcal{L}\{y\}$ satisfies
>
> $$
> a\big(s^2Y(s) - sy(0) - y'(0)\big) + b\big(sY(s) - y(0)\big) + cY(s) = F(s) , \qquad (15)
> $$
>
> $$
> Y(s) = \frac{(as + b)y(0) + ay'(0)}{as^2 + bs + c} + \frac{F(s)}{as^2 + bs + c} . \qquad (16)
> $$
>
> *BDP: 6.2, Equations (15) and (16)*

^prop-22-3

> [!proof]+ Proof
> Transform both sides of (14). By linearity ([[§21 Definition of the Laplace Transform#^thm-21-3|Theorem §21.3]]) the left side becomes $a\mathcal{L}\{y''\} + b\mathcal{L}\{y'\} + c\mathcal{L}\{y\}$, and [[§22 Solution of Initial Value Problems#^cor-22-2|Corollary §22.2]] with $n = 2$ and $n = 1$ gives (15). Collecting the $Y(s)$ terms, $(as^2 + bs + c)Y(s) = (as + b)y(0) + ay'(0) + F(s)$; dividing by $as^2 + bs + c$ (nonzero for $s$ large) gives (16).

^pf-22-3

*Uses:* [[§22 Solution of Initial Value Problems#^cor-22-2|§22.2]], [[§21 Definition of the Laplace Transform#^thm-21-3|§21.3]]

> [!remark] Remark: Four Features of the Method
> 1. The transform $Y(s)$ is found from an *algebraic* equation, (10) or (15), not a differential equation. This is the key to the usefulness of Laplace transforms for linear constant-coefficient equations.
> 2. The initial conditions are built in, so there is no separate step of determining the arbitrary constants of a general solution.
> 3. Nonhomogeneous equations are handled exactly like homogeneous ones; there is no need to solve the homogeneous equation first.
> 4. The method works the same way for higher-order equations, provided the solution satisfies the conditions of [[§22 Solution of Initial Value Problems#^cor-22-2|Corollary §22.2]] for the appropriate $n$.
>
> The denominator $as^2 + bs + c$ in (16) is the characteristic polynomial of (14). Partial fractions require factoring it, so the transform does not avoid finding the roots of the [[§13 Homogeneous Differential Equations with Constant Coefficients#^def-13-4|characteristic equation]] (for higher-order equations this may require numerical approximation).

^rem-22-1

## The Inverse Transform

> [!definition] Definition §22.1: Inverse Laplace Transform
> Finding $y(t)$ from its transform $Y(s)$ is the **inversion problem**. A function $y(t)$ with $\mathcal{L}\{y(t)\} = Y(s)$ is called the **inverse Laplace transform** of $Y(s)$, written $y(t) = \mathcal{L}^{-1}\{Y(s)\}$; the process is **inverting the transform**.
>
> *BDP: 6.2 (text)*

^def-22-1

> [!remark]- Connections
> - Complex-variables version: [[§95★ Inverse Laplace Transforms#^thm-95-4|342 Thm. §95.4]] (the general inversion formula mentioned below, the Bromwich integral, proved for sectionally smooth $f$ of exponential order).

There is a general formula for the inverse transform, but it requires functions of a complex variable, and BDP does not use it. Instead one relies on the following uniqueness property and a table.

> [!theorem] Theorem §22.4: Uniqueness of the Inverse Transform
> If $f$ and $g$ are continuous functions with the same Laplace transform, then $f$ and $g$ are identical. If $f$ and $g$ are only piecewise continuous, they may differ at one or more points of discontinuity and still have the same transform ([[§21 Definition of the Laplace Transform#^ex-21-3|Example §21.3]]); this lack of uniqueness is of no practical significance.
>
> *BDP: 6.2 (text)*

^thm-22-4

*BDP omits the proof ("it can be shown"); it is Lerch's theorem.*

> [!remark]- Connections
> - Complex-variables version: [[§95★ Inverse Laplace Transforms#^cor-95-5|342 Cor. §95.5]] (Lerch's theorem, proved for sectionally smooth functions of exponential order from the Bromwich inversion formula).

Consistently with this, the solution (8) found in [[§22 Solution of Initial Value Problems#^ex-22-1|Example §22.1]] is continuous and, by the existence and uniqueness theorem for second-order equations ([[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|Theorem §14.1]], Theorem 3.2.1), the initial value problem has no other solution.

> [!theorem] Corollary §22.5: Linearity of the Inverse Transform
> Suppose that $F(s) = F_1(s) + \cdots + F_n(s)$ (17) and that $f_1(t) = \mathcal{L}^{-1}\{F_1(s)\}, \ldots, f_n(t) = \mathcal{L}^{-1}\{F_n(s)\}$ are continuous. Then
>
> $$
> \mathcal{L}^{-1}\{F(s)\} = \mathcal{L}^{-1}\{F_1(s)\} + \cdots + \mathcal{L}^{-1}\{F_n(s)\} ; \qquad (18)
> $$
>
> that is, the inverse Laplace transform is also a linear operator (constant multiples pass through in the same way).
>
> *BDP: 6.2, Equation (18)*

^cor-22-5

> [!proof]+ Proof
> By linearity of $\mathcal{L}$ ([[§21 Definition of the Laplace Transform#^thm-21-3|Theorem §21.3]]), the continuous function $f = f_1 + \cdots + f_n$ has transform $F_1 + \cdots + F_n = F$. By [[§22 Solution of Initial Value Problems#^thm-22-4|Theorem §22.4]], no other continuous function has the transform $F$, so $\mathcal{L}^{-1}\{F\} = f_1 + \cdots + f_n$. Likewise $cf_1$ is the continuous function with transform $cF_1$.

^pf-22-5

*Uses:* [[§21 Definition of the Laplace Transform#^thm-21-3|§21.3]], [[§22 Solution of Initial Value Problems#^thm-22-4|§22.4]]

So there is essentially a one-to-one correspondence between functions and their transforms, which makes a table worth compiling. Read from right to left, it is a table of inverse transforms.

> [!theorem] Theorem §22.6: Table of Elementary Laplace Transforms
> | | $f(t) = \mathcal{L}^{-1}\{F(s)\}$ | $F(s) = \mathcal{L}\{f(t)\}$ | where proved |
> |---|---|---|---|
> | 1 | $1$ | $\dfrac1s$, $\ s > 0$ | [[§21 Definition of the Laplace Transform#^ex-21-2\|Ex. §21.2]] |
> | 2 | $e^{at}$ | $\dfrac{1}{s - a}$, $\ s > a$ | [[§21 Definition of the Laplace Transform#^ex-21-2\|Ex. §21.2]] |
> | 3 | $t^n$, $n$ a positive integer | $\dfrac{n!}{s^{n+1}}$, $\ s > 0$ | proof below |
> | 4 | $t^p$, $p > -1$ | $\dfrac{\Gamma(p + 1)}{s^{p+1}}$, $\ s > 0$ | proof below |
> | 5 | $\sin(at)$ | $\dfrac{a}{s^2 + a^2}$, $\ s > 0$ | [[§21 Definition of the Laplace Transform#^ex-21-4\|Ex. §21.4]] |
> | 6 | $\cos(at)$ | $\dfrac{s}{s^2 + a^2}$, $\ s > 0$ | proof below |
> | 7 | $\sinh(at)$ | $\dfrac{a}{s^2 - a^2}$, $\ s > \lvert a\rvert$ | proof below |
> | 8 | $\cosh(at)$ | $\dfrac{s}{s^2 - a^2}$, $\ s > \lvert a\rvert$ | proof below |
> | 9 | $e^{at}\sin(bt)$ | $\dfrac{b}{(s - a)^2 + b^2}$, $\ s > a$ | proof below |
> | 10 | $e^{at}\cos(bt)$ | $\dfrac{s - a}{(s - a)^2 + b^2}$, $\ s > a$ | proof below |
> | 11 | $t^ne^{at}$, $n$ a positive integer | $\dfrac{n!}{(s - a)^{n+1}}$, $\ s > a$ | proof below |
> | 12 | $u_c(t) = \begin{cases} 0, & t < c \\ 1, & t \ge c \end{cases}$ | $\dfrac{e^{-cs}}{s}$, $\ s > 0$ | [[§23 Step Functions#^thm-23-1\|Thm. §23.1]] |
> | 13 | $u_c(t)f(t - c)$ | $e^{-cs}F(s)$ | [[§23 Step Functions#^thm-23-2\|Thm. §23.2]] (Theorem 6.3.1) |
> | 14 | $e^{ct}f(t)$ | $F(s - c)$ | [[§23 Step Functions#^thm-23-3\|Thm. §23.3]] (Theorem 6.3.2) |
> | 15 | $f(ct)$ | $\dfrac1c F\Big(\dfrac sc\Big)$, $\ c > 0$ | proof below |
> | 16 | $(f * g)(t) = \displaystyle\int_0^t f(t - \tau)g(\tau)\,d\tau$ | $F(s)G(s)$ | [[§26★ The Convolution Integral#^thm-26-2\|Thm. §26.2]] (Theorem 6.6.1) |
> | 17 | $\delta(t - c)$ | $e^{-cs}$ | [[§25 Impulse Functions#^thm-25-2\|Thm. §25.2]] |
> | 18 | $f^{(n)}(t)$ | $s^nF(s) - s^{n-1}f(0) - \cdots - f^{(n-1)}(0)$ | [[§22 Solution of Initial Value Problems#^cor-22-2\|Cor. §22.2]] |
> | 19 | $(-t)^nf(t)$ | $F^{(n)}(s)$ | proof below |
>
> Here $\Gamma(p + 1) = \int_0^\infty e^{-x}x^p\,dx$ is the gamma function; $\Gamma(n + 1) = n!$, so entry 4 contains entry 3.
>
> *BDP: Table 6.2.1*

^thm-22-6

> [!proof]- Proof
> Entries 1, 2, 5 are worked out in §21; entry 18 is [[§22 Solution of Initial Value Problems#^cor-22-2|Corollary §22.2]]; entries 12–14, 16, 17 are proved in the sections listed. The remaining entries:
>
> **3.** For $n \ge 1$, $f(t) = t^n$ is continuous with continuous derivative $nt^{n-1}$ and $f(0) = 0$. Since $e^{\varepsilon t} \ge (\varepsilon t)^n/n!$, we have $t^n \le (n!/\varepsilon^n)e^{\varepsilon t}$ for every $\varepsilon > 0$, so [[§22 Solution of Initial Value Problems#^thm-22-1|Theorem §22.1]] applies for every $s > \varepsilon$, hence for all $s > 0$:
>
> $$
> n\mathcal{L}\{t^{n-1}\} = \mathcal{L}\{(t^n)'\} = s\mathcal{L}\{t^n\} - 0, \qquad \mathcal{L}\{t^n\} = \frac ns\,\mathcal{L}\{t^{n-1}\} .
> $$
>
> Starting from $\mathcal{L}\{1\} = 1/s$, induction gives $\mathcal{L}\{t^n\} = \frac{n}{s}\cdot\frac{n - 1}{s}\cdots\frac1s\cdot\frac1s = \frac{n!}{s^{n+1}}$. (BDP: Problem 6.1.4, by integration by parts, which is the same computation.)
>
> **4.** (BDP: Problems 6.1.23 and 6.1.24.) For $-1 < p < 0$ the integrand $e^{-st}t^p$ is unbounded at $t = 0$, so the integral is improper at both ends; it converges at $0$ because $p > -1$ (compare with $t^p$ near $0$) and at $\infty$ by comparison with $e^{-st/2}$. For $s > 0$ substitute $x = st$, $t = x/s$, $dt = dx/s$:
>
> $$
> \int_0^\infty e^{-st}t^p\,dt = \int_0^\infty e^{-x}\Big(\frac xs\Big)^p\frac{dx}{s} = \frac{1}{s^{p+1}}\int_0^\infty e^{-x}x^p\,dx = \frac{\Gamma(p + 1)}{s^{p+1}} .
> $$
>
> **6.** $f(t) = \sin(at)$ is continuous, bounded (exponential order with exponent $0$), $f(0) = 0$, and $f'(t) = a\cos(at)$. By Theorem §22.1 and entry 5, for $s > 0$: $a\mathcal{L}\{\cos(at)\} = s\cdot\frac{a}{s^2 + a^2} - 0$, so $\mathcal{L}\{\cos(at)\} = \frac{s}{s^2 + a^2}$ for $a \ne 0$; for $a = 0$ it is entry 1.
>
> **7, 8.** With $\sinh(at) = \frac12(e^{at} - e^{-at})$, $\cosh(at) = \frac12(e^{at} + e^{-at})$, linearity and entry 2 give, for $s > a$ and $s > -a$, that is $s > |a|$,
>
> $$
> \mathcal{L}\{\sinh(at)\} = \frac12\Big(\frac{1}{s - a} - \frac{1}{s + a}\Big) = \frac{a}{s^2 - a^2}, \qquad
> \mathcal{L}\{\cosh(at)\} = \frac12\Big(\frac{1}{s - a} + \frac{1}{s + a}\Big) = \frac{s}{s^2 - a^2} .
> $$
>
> **9, 10, 11.** If $F(\sigma) = \mathcal{L}\{f(t)\}$ exists for $\sigma > \sigma_0$, then for $s - a > \sigma_0$
>
> $$
> \mathcal{L}\{e^{at}f(t)\} = \int_0^\infty e^{-st}e^{at}f(t)\,dt = \int_0^\infty e^{-(s - a)t}f(t)\,dt = F(s - a)
> $$
>
> (this one-line computation is entry 14, [[§23 Step Functions#^thm-23-3|Theorem §23.3]]). Apply it to $\sin(bt)$ and $\cos(bt)$ (entries 5, 6, $\sigma_0 = 0$) and to $t^n$ (entry 3): the transforms are $\frac{b}{(s - a)^2 + b^2}$, $\frac{s - a}{(s - a)^2 + b^2}$ and $\frac{n!}{(s - a)^{n+1}}$, for $s > a$. (BDP: Problems 6.1.10, 6.1.11, 6.1.14, done there by integration by parts.)
>
> **15.** (BDP: Problem 6.3.17.) For $c > 0$, substitute $x = ct$, $dt = dx/c$:
>
> $$
> \int_0^\infty e^{-st}f(ct)\,dt = \frac1c\int_0^\infty e^{-(s/c)x}f(x)\,dx = \frac1c F\Big(\frac sc\Big) ,
> $$
>
> valid when $s/c$ is in the domain of $F$.
>
> **19.** (BDP: Problem 6.2.21.) Let $f$ satisfy the conditions of [[§21 Definition of the Laplace Transform#^thm-21-2|Theorem §21.2]] and fix $s > a$. BDP asserts that one may differentiate under the integral sign with respect to $s$; here is why. Put $\delta = \frac12(s - a)$ and let $0 < |h| \le \delta$, so that $s + h > a$ and $F(s + h)$ exists. By Taylor's formula with Lagrange remainder, $e^x = 1 + x + \frac12 x^2e^{\xi}$ with $\xi$ between $0$ and $x$, so $|e^x - 1 - x| \le \frac12 x^2e^{|x|}$. With $x = -ht$,
>
> $$
> \Big|\frac{e^{-(s + h)t} - e^{-st}}{h} + te^{-st}\Big| = \frac{e^{-st}}{|h|}\,\big|e^{-ht} - 1 + ht\big| \le \frac{|h|}{2}\,t^2e^{-(s - \delta)t}, \qquad t \ge 0 .
> $$
>
> Multiplying by $|f(t)|$ and integrating,
>
> $$
> \Big|\frac{F(s + h) - F(s)}{h} - \int_0^\infty e^{-st}\big(-tf(t)\big)\,dt\Big| \le \frac{|h|}{2}\int_0^\infty t^2e^{-(s - \delta)t}|f(t)|\,dt .
> $$
>
> All these integrals converge by [[§21 Definition of the Laplace Transform#^thm-21-1|Theorem §21.1]]: the integrands are piecewise continuous, and for $t \ge M$, $t^2e^{-(s - \delta)t}|f(t)| \le Kt^2e^{-\delta t} \le Ce^{-\delta t/2}$ (as $t^2e^{-\delta t/2}$ is bounded), and likewise $t\,e^{-st}|f(t)| \le Ce^{-\delta t/2}$. Letting $h \to 0$ gives $F'(s) = \mathcal{L}\{-tf(t)\}$ for every $s > a$. Finally, $-tf(t)$ is piecewise continuous and $|-tf(t)| \le Kte^{at} \le K'e^{a't}$ for every $a' > a$ and $t \ge M$, so it again satisfies the conditions of Theorem §21.2 (with any exponent $a' > a$), and induction gives $F^{(n)}(s) = \mathcal{L}\{(-t)^nf(t)\}$ for $s > a$.

^pf-22-6

*Uses:* [[§22 Solution of Initial Value Problems#^thm-22-1|§22.1]], [[§22 Solution of Initial Value Problems#^cor-22-2|§22.2]] (entry 18), [[§21 Definition of the Laplace Transform#^thm-21-3|§21.3]], [[§21 Definition of the Laplace Transform#^ex-21-2|Ex. §21.2]], [[§21 Definition of the Laplace Transform#^ex-21-4|Ex. §21.4]], [[§21 Definition of the Laplace Transform#^thm-21-1|§21.1]] (comparison), [[§21 Definition of the Laplace Transform#^thm-21-2|§21.2]], [[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]] (Taylor's formula, entry 19)

> [!remark]- Connections
> - See also: [[§51★ Definition and Elementary Properties#^thm-51-8|341 Thm. §51.8]] (Powers' table, keyed to the entry numbers here); entry 19 is [[§51★ Definition and Elementary Properties#^thm-51-6|341 Thm. §51.6]], together with its counterpart for division by $t$.
> - Complex-variables version: [[§95★ Inverse Laplace Transforms#^thm-95-6|342 Thm. §95.6]] (entry 11 for complex $a$, and the inverse transform of every proper rational function as a sum of residues), with entry 6 inverted by residues in [[§95★ Inverse Laplace Transforms#^ex-95-1|342 Ex. §95.1]].

> [!remark] Remark: The Course Table
> The table handed out with the course review and attached to the final exams lists entries 1, 3 (with $t$ and $t^2$ separately), 2, 11, 5, 6 (with frequency $\omega$ in place of $a$), 7, 8, 9, 10 (as $e^{at}\cos(\omega t)$, $e^{at}\sin(\omega t)$), 12 (as $u_a(t)$), 17, the derivative rules $\mathcal{L}\{y'\} = s\mathcal{L}\{y\} - y(0)$ and $\mathcal{L}\{y''\} = s^2\mathcal{L}\{y\} - sy(0) - y'(0)$ (entry 18 for $n = 1, 2$), the "$t$-shift" $u_a(t)f(t - a) \leftrightarrow e^{-as}F(s)$ (entry 13) and the "$s$-shift" $e^{at}f(t) \leftrightarrow F(s - a)$ (entry 14). It omits entries 4, 15, 16 and 19.
>
> *Source: 331 Course Review, Table of Laplace Transforms*

^rem-22-2

> [!remark] Remark: Method — Solving an Initial Value Problem by Laplace Transform
> For $ay'' + by' + cy = f(t)$, $y(0) = y_0$, $y'(0) = y_0'$ (or a higher-order analogue):
> 1. **Transform** both sides, using linearity and $\mathcal{L}\{y'\} = sY - y(0)$, $\mathcal{L}\{y''\} = s^2Y - sy(0) - y'(0)$ ([[§22 Solution of Initial Value Problems#^cor-22-2|Corollary §22.2]]), and the table ([[§22 Solution of Initial Value Problems#^thm-22-6|Theorem §22.6]]) for $\mathcal{L}\{f\}$.
> 2. **Insert the initial conditions** and **solve for $Y(s)$**, as in (16).
> 3. **Decompose $Y(s)$** into terms found in the table (next remark).
> 4. **Invert term by term** ([[§22 Solution of Initial Value Problems#^cor-22-5|Corollary §22.5]]) to get $y(t)$.
> 5. **Check** $y(0)$, $y'(0)$, or substitute into the equation.

^rem-22-3

> [!remark] Remark: Method — Inverting a Rational Transform
> To find $\mathcal{L}^{-1}\{P(s)/Q(s)\}$ with $\deg P < \deg Q$:
> 1. **Factor** $Q(s)$ into real linear factors and irreducible quadratics.
> 2. **Partial fractions.** Write $P/Q$ as a sum of terms $\frac{A}{s - r}$ (with powers $\frac{A}{(s - r)^k}$ for repeated roots) and $\frac{as + b}{s^2 + \beta s + \gamma}$ ([[§47 Integration of Rational Functions by Partial Fractions#^thm-47-3|Calc Thm. §47.3]]). Find the constants by substituting convenient values of $s$ (the roots) and by comparing coefficients of like powers of $s$.
> 3. **Complete the square** in each irreducible quadratic, $s^2 + ps + q = (s - a)^2 + b^2$, and rewrite the numerator in the same shift, $\alpha s + \beta = \alpha(s - a) + \frac{\beta + \alpha a}{b}\cdot b$. Then entries 10 and 9 give $\alpha e^{at}\cos(bt) + \frac{\beta + \alpha a}{b}\,e^{at}\sin(bt)$.
> 4. **Read off** the other terms: $\frac{1}{s - r} \to e^{rt}$, $\frac{n!}{(s - r)^{n+1}} \to t^ne^{rt}$; and for quadratics with $a = 0$, entries 5–8. Choosing the form $\frac{as + b}{s^2 \pm c^2}$ rather than splitting into linear factors matches the table's entries for $\sinh$, $\cosh$, $\sin$, $\cos$ directly.

^rem-22-4

> [!remark]- Connections
> - See also: [[§52★ Partial Fractions and Convolutions#^thm-52-2|341 Thm. §52.2]] (Heaviside's formula: when the denominator has only simple roots, real or complex, the inverse transform is $\sum_k \frac{q(r_k)}{p'(r_k)}e^{r_kt}$, with no constants to solve for).
> - Complex-variables version: [[§95★ Inverse Laplace Transforms#^thm-95-6|342 Thm. §95.6]] (part (a) proves the partial fraction decomposition by principal parts and [[§58 Liouville's Theorem and the Fundamental Theorem of Algebra#^thm-58-1|Liouville's theorem]]) and [[§95★ Inverse Laplace Transforms#^rem-95-2|342 Remark: Method — Inverse Laplace Transforms by Residues]] (inverting a rational transform by residues).

> [!example] Example §22.2: A Forced Undamped Oscillator
> Solve $y'' + y = \sin(2t)$, $y(0) = 2$, $y'(0) = 1$. (19), (20)
>
> Assuming $y$ satisfies the conditions of [[§22 Solution of Initial Value Problems#^cor-22-2|Corollary §22.2]], transform, using entry 5 for $\sin(2t)$:
>
> $$
> s^2Y(s) - sy(0) - y'(0) + Y(s) = \frac{2}{s^2 + 4} .
> $$
>
> With the initial conditions, $(s^2 + 1)Y = 2s + 1 + \frac{2}{s^2 + 4}$, so
>
> $$
> Y(s) = \frac{(2s + 1)(s^2 + 4) + 2}{(s^2 + 1)(s^2 + 4)} = \frac{2s^3 + s^2 + 8s + 6}{(s^2 + 1)(s^2 + 4)} . \qquad (21)
> $$
>
> **Partial fractions.** $Y(s) = \frac{as + b}{s^2 + 1} + \frac{cs + d}{s^2 + 4}$ requires
>
> $$
> 2s^3 + s^2 + 8s + 6 = (as + b)(s^2 + 4) + (cs + d)(s^2 + 1) = (a + c)s^3 + (b + d)s^2 + (4a + c)s + (4b + d) \qquad (23)
> $$
>
> for all $s$. Comparing coefficients: $a + c = 2$, $b + d = 1$, $4a + c = 8$, $4b + d = 6$, so $a = 2$, $c = 0$, $b = \frac53$, $d = -\frac23$. (Substituting values of $s$ is less convenient here: no four values give trivial equations.) Thus
>
> $$
> Y(s) = \frac{2s}{s^2 + 1} + \frac{5/3}{s^2 + 1} - \frac{2/3}{s^2 + 4}, \qquad
> y = 2\cos t + \frac53\sin t - \frac13\sin(2t) \qquad (24),\ (25)
> $$
>
> by entries 5 and 6 (the last term is $-\frac13\cdot\frac{2}{s^2 + 4}$).
>
> *BDP: Example 6.2.2*

^ex-22-2

> [!example] Example §22.3: A Fourth-Order Equation
> Solve $y^{(4)} - y = 0$, $y(0) = 0$, $y'(0) = 1$, $y''(0) = 0$, $y'''(0) = 0$. (26), (27)
>
> Assume $y$ satisfies the conditions of [[§22 Solution of Initial Value Problems#^cor-22-2|Corollary §22.2]] for $n = 4$. Transforming,
>
> $$
> s^4Y(s) - s^3y(0) - s^2y'(0) - sy''(0) - y'''(0) - Y(s) = 0 ,
> $$
>
> so $(s^4 - 1)Y = s^2$ and $Y(s) = \dfrac{s^2}{s^4 - 1}$. (28) Since $s^4 - 1 = (s^2 - 1)(s^2 + 1)$, write
>
> $$
> Y(s) = \frac{as + b}{s^2 - 1} + \frac{cs + d}{s^2 + 1}, \qquad (as + b)(s^2 + 1) + (cs + d)(s^2 - 1) = s^2 \qquad (29),\ (30)
> $$
>
> for all $s$. Mix substitution and comparison: $s = 1$ gives $2(a + b) = 1$ and $s = -1$ gives $2(-a + b) = 1$, so $a = 0$, $b = \frac12$; $s = 0$ gives $b - d = 0$, so $d = \frac12$; the $s^3$ coefficients give $a + c = 0$, so $c = 0$. Hence
>
> $$
> Y(s) = \frac{1/2}{s^2 - 1} + \frac{1/2}{s^2 + 1}, \qquad y(t) = \frac12\big(\sinh t + \sin t\big) \qquad (31),\ (32)
> $$
>
> by entries 7 and 5. The form (29) was chosen over $\frac{a}{s - 1} + \frac{b}{s + 1} + \frac{cs + d}{s^2 + 1}$ because the table has entries for both $1/(s^2 \pm 1)$ and $s/(s^2 \pm 1)$.
>
> *BDP: Example 6.2.3*

^ex-22-3

> [!example] Example §22.4: Inverting by Completing the Square
> Compute the inverse Laplace transforms
>
> $$
> \text{(a)}\ \mathcal{L}^{-1}\Big\{\frac{s + 11}{s^2 + 6s + 13}\Big\}, \qquad
> \text{(b)}\ \mathcal{L}^{-1}\Big\{\frac{1}{s^2 + 2s + 2}\Big\}, \qquad
> \text{(c)}\ \mathcal{L}^{-1}\Big\{\frac{5s - \alpha}{s^2 + 4s + 13}\Big\}\ (\alpha \text{ a constant}) .
> $$
>
> The denominators do not factor over the reals (discriminants $36 - 52$, $4 - 8$, $16 - 52$ are negative), so complete the square (step 3 of the method).
>
> **(a)** $s^2 + 6s + 13 = (s + 3)^2 + 2^2$. Rewrite the numerator in the same shift: $s + 11 = (s + 3) + 8 = (s + 3) + 4\cdot 2$. Then
>
> $$
> \frac{s + 11}{(s + 3)^2 + 2^2} = \frac{s + 3}{(s + 3)^2 + 2^2} + 4\cdot\frac{2}{(s + 3)^2 + 2^2} ,
> $$
>
> and entries 10 and 9 with $a = -3$, $b = 2$ give
>
> $$
> \mathcal{L}^{-1}\Big\{\frac{s + 11}{s^2 + 6s + 13}\Big\} = e^{-3t}\big(\cos(2t) + 4\sin(2t)\big) .
> $$
>
> **(b)** $s^2 + 2s + 2 = (s + 1)^2 + 1$, so by entry 9 with $a = -1$, $b = 1$: $\mathcal{L}^{-1}\Big\{\dfrac{1}{(s + 1)^2 + 1}\Big\} = e^{-t}\sin t$.
>
> **(c)** $s^2 + 4s + 13 = (s + 2)^2 + 3^2$ and $5s - \alpha = 5(s + 2) - (10 + \alpha) = 5(s + 2) - \frac{10 + \alpha}{3}\cdot 3$. By entries 10 and 9 with $a = -2$, $b = 3$:
>
> $$
> \mathcal{L}^{-1}\Big\{\frac{5s - \alpha}{s^2 + 4s + 13}\Big\} = 5e^{-2t}\cos(3t) - \frac{10 + \alpha}{3}\,e^{-2t}\sin(3t) .
> $$
>
> *Source: 331 Final (Fall 2021), Q3*
> *Source: 331 Written HW 5, Problem 2(a), (c)*

^ex-22-4

## Vibrations and Circuits

The most important elementary applications are the equations of [[§19 Mechanical and Electrical Vibrations|§19]]: the spring–mass system ([[§19 Mechanical and Electrical Vibrations#^prop-19-1|Proposition §19.1]]) $m\,\dfrac{d^2u}{dt^2} + \gamma\dfrac{du}{dt} + ku = F(t)$ (33), and the series circuit ([[§19 Mechanical and Electrical Vibrations#^prop-19-5|Proposition §19.5]]) $L\dfrac{d^2Q}{dt^2} + R\dfrac{dQ}{dt} + \dfrac1C Q = E(t)$ (34) or, for the current, $L\dfrac{d^2I}{dt^2} + R\dfrac{dI}{dt} + \dfrac1C I = \dfrac{dE}{dt}$ (35), each with initial conditions. They are the same mathematical problem, and [[§22 Solution of Initial Value Problems#^prop-22-3|Proposition §22.3]] solves all of them at once, as soon as $\mathcal{L}\{F\}$ or $\mathcal{L}\{E\}$ is known; most constant-coefficient problems of this chapter can be read as models of one of these systems.
