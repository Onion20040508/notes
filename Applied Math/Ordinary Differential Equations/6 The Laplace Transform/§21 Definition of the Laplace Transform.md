---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 6
section: 21
bdp: "6.1"
aliases: ["BDP 6.1"]
tags: [ordinary-differential-equations, math331]
---
← [[§20 Forced Periodic Vibrations]] · ↑ [[· 6 The Laplace Transform]] · [[§22 Solution of Initial Value Problems]] →

*Boyce–DiPrima, Section 6.1.*

Mechanical and electrical systems are often driven by discontinuous or impulsive forces, for which the methods of Chapter 3 are awkward. The Laplace transform $\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty e^{-st}f(t)\,dt$ turns such problems into algebra. This section reviews improper integrals, defines the transform, and proves that it exists for every piecewise continuous function of exponential order (for $s$ large enough). It then computes the first transforms ($1$, $e^{at}$, $\sin at$, a pulse) and shows that the transform is linear: the starting entries of the table of transforms in [[§22 Solution of Initial Value Problems#^thm-22-6|Theorem §22.6]].

## Improper Integrals

> [!definition] Definition §21.1: Improper Integral over an Unbounded Interval
> If $\int_a^A f(t)\,dt$ exists for each $A > a$, the **improper integral** of $f$ over $[a, \infty)$ is
>
> $$
> \int_a^\infty f(t)\,dt = \lim_{A \to \infty} \int_a^A f(t)\,dt . \qquad (1)
> $$
>
> If the limit exists (as a finite number), the improper integral **converges** to that value; otherwise it **diverges** (fails to exist).
>
> *BDP: 6.1, Equation (1)*

^def-21-1

> [!remark]- Connections
> - See also: [[§51 Improper Integrals#^def-51-1|Calc Def. §51.1]] (Stewart's treatment, with the integrals over $(-\infty, b]$ and $(-\infty, \infty)$). Rigorous treatment: [[§36 Improper Integrals#^def-36-1|451 Def. §36.1]].

> [!example] Example §21.1: Three Improper Integrals
> **(a)** $\displaystyle\int_1^\infty \frac{dt}{t} = \lim_{A \to \infty} \int_1^A \frac{dt}{t} = \lim_{A \to \infty} \ln A = \infty$: the integral **diverges**.
>
> **(b)** For which $c$ does $\displaystyle\int_0^\infty e^{ct}\,dt$ converge? If $c \ne 0$,
>
> $$
> \int_0^\infty e^{ct}\,dt = \lim_{A \to \infty} \frac{e^{ct}}{c}\bigg|_0^A = \lim_{A \to \infty} \frac1c\big(e^{cA} - 1\big) ,
> $$
>
> which converges to $-1/c$ if $c < 0$ and diverges if $c > 0$. If $c = 0$, $\int_0^A 1\,dt = A \to \infty$, so it diverges. **It converges exactly for $c < 0$**, with value $-1/c$. (The same computation over $[M, \infty)$ gives $\int_M^\infty e^{ct}\,dt = -e^{cM}/c$ for $c < 0$.)
>
> **(c)** For which $p$ does $\displaystyle\int_1^\infty t^{-p}\,dt$ converge? For $p \ne 1$,
>
> $$
> \int_1^\infty t^{-p}\,dt = \lim_{A \to \infty} \frac{1}{1 - p}\big(A^{1-p} - 1\big) .
> $$
>
> As $A \to \infty$, $A^{1-p} \to 0$ if $p > 1$ and $A^{1-p} \to \infty$ if $p < 1$. With (a), the integral **converges to $1/(p - 1)$ for $p > 1$ and diverges for $p \le 1$**, just like the series $\sum_{n=1}^\infty n^{-p}$.
>
> *BDP: Examples 6.1.1, 6.1.2 and 6.1.3*

^ex-21-1

> [!definition] Definition §21.2: Piecewise Continuous Function
> A function $f$ is **piecewise continuous** on an interval $\alpha \le t \le \beta$ if the interval can be partitioned by finitely many points $\alpha = t_0 < t_1 < \cdots < t_n = \beta$ so that
> 1. $f$ is continuous on each open subinterval $t_{i-1} < t < t_i$, and
> 2. $f$ approaches a finite limit as the endpoints of each subinterval are approached from within the subinterval.
>
> That is, $f$ is continuous on $[\alpha, \beta]$ except for finitely many [[§10 Continuity#^def-10-3|jump discontinuities]]. If $f$ is piecewise continuous on $\alpha \le t \le \beta$ for every $\beta > \alpha$, it is **piecewise continuous on $t \ge \alpha$**. (The interval may also be open at one or both ends.)
>
> The integral of such an $f$ over $[\alpha, \beta]$ is the sum of the integrals over the subintervals,
>
> $$
> \int_\alpha^\beta f(t)\,dt = \int_{t_0}^{t_1} f(t)\,dt + \cdots + \int_{t_{n-1}}^{t_n} f(t)\,dt , \qquad (2)
> $$
>
> and it does not depend on the values of $f$ at the partition points, or on whether $f$ is defined there at all. So if $f$ is piecewise continuous on $t \ge a$, then $\int_a^A f(t)\,dt$ exists for every $A > a$; whether $\int_a^\infty f(t)\,dt$ converges is a separate question ([[§21 Definition of the Laplace Transform#^ex-21-1|Example §21.1]]).
>
> *BDP: 6.1 (text)*

^def-21-2

When $f$ cannot be integrated in elementary terms, convergence is tested by comparison. The usual comparison functions are $e^{ct}$ and $t^{-p}$ of [[§21 Definition of the Laplace Transform#^ex-21-1|Example §21.1]].

> [!theorem] Theorem §21.1: Comparison Test for Improper Integrals
> Let $f$ be piecewise continuous for $t \ge a$.
> - If $|f(t)| \le g(t)$ for $t \ge M$, for some positive constant $M$, and $\int_M^\infty g(t)\,dt$ converges, then $\int_a^\infty f(t)\,dt$ also converges.
> - If $f(t) \ge g(t) \ge 0$ for $t \ge M$ and $\int_M^\infty g(t)\,dt$ diverges, then $\int_a^\infty f(t)\,dt$ also diverges.
>
> *BDP: Theorem 6.1.1*

^thm-21-1

*BDP omits the proof ("from calculus"), making it plausible by comparing the areas under $g$ and $|f|$. For continuous nonnegative integrands it is [[§51 Improper Integrals#^thm-51-2|Calc Thm. §51.2]], and the same proof works for piecewise continuous ones: if $0 \le h \le g$ on $[M, \infty)$, then $A \mapsto \int_M^A h\,dt$ is increasing, so by the dichotomy [[§36 Improper Integrals#^thm-36-1|451 Thm. §36.1]] it converges or tends to $\infty$, and the bound $\int_M^\infty g\,dt$ excludes $\infty$. The first part reduces to that case: $\int_M^\infty |f|\,dt$ and $\int_M^\infty (f + |f|)\,dt$ converge because $0 \le |f| \le g$ and $0 \le f + |f| \le 2g$, so $\int_M^\infty f\,dt$ converges as their difference, and $\int_a^M f\,dt$ exists by piecewise continuity.*

## The Laplace Transform

> [!definition] Definition §21.3: Integral Transform
> An **integral transform** is a relation
>
> $$
> F(s) = \int_\alpha^\beta K(s, t)f(t)\,dt , \qquad (3)
> $$
>
> where the function $K(s, t)$, the **kernel** of the transformation, and the limits $\alpha$, $\beta$ are given ($\alpha = -\infty$ or $\beta = \infty$ or both are allowed). It transforms the function $f$ into another function $F$, the **transform** of $f$.
>
> *BDP: 6.1 (text)*

^def-21-3

> [!definition] Definition §21.4: The Laplace Transform
> Let $f(t)$ be given for $t \ge 0$. The **Laplace transform** of $f$, denoted $\mathcal{L}\{f(t)\}$ or $F(s)$, is
>
> $$
> \mathcal{L}\{f(t)\} = F(s) = \int_0^\infty e^{-st}f(t)\,dt , \qquad (4)
> $$
>
> for those $s$ for which this improper integral converges. It is the integral transform with kernel $K(s, t) = e^{-st}$, $\alpha = 0$, $\beta = \infty$. In general $s$ may be complex; in this chapter real values of $s$ suffice.
>
> *BDP: 6.1, Equation (4)*

^def-21-4

> [!remark]- Connections
> - PDE version: [[§53★ Partial Differential Equations#^def-53-1|341 Def. §53.1]] (the transform in $t$ of a function $u(x, t)$, which turns heat and wave problems into boundary value problems in $x$, [[§53★ Partial Differential Equations#^rem-53-1|341 Remark: Method — Laplace Transform in t for a Heat or Wave Problem]]); Powers' definition is [[§51★ Definition and Elementary Properties#^def-51-1|341 Def. §51.1]].

> [!remark] Remark: The Idea of the Transform Method
> Solutions of constant-coefficient linear equations are built from exponentials, which is why the exponential kernel $e^{-st}$ suits them. The plan, carried out in [[§22 Solution of Initial Value Problems|§22]]:
> 1. Use (4) to transform an initial value problem for an unknown function $f$ in the $t$-domain into a simpler, indeed algebraic, problem for $F$ in the $s$-domain.
> 2. Solve this algebraic problem to find $F$.
> 3. Recover $f$ from $F$: "inverting the transform".
>
> (The transform is named for P. S. Laplace, who studied the integral (3) in 1782; the method for differential equations is mainly due to Oliver Heaviside, a century later.)

^rem-21-1

> [!definition] Definition §21.5: Exponential Order
> A function $f$ is **of exponential order** (as $t \to \infty$) if there are real constants $K$, $a$, $M$ with $K > 0$ and $M > 0$ such that
>
> $$
> |f(t)| \le Ke^{at} \quad\text{when } t \ge M .
> $$
>
> Not every function is: $f(t) = e^{t^2}$ grows faster than $Ke^{at}$ however large $K$ and $a$ are, since $e^{t^2}/e^{at} = e^{t(t - a)} \to \infty$.
>
> *BDP: 6.1 (text)*

^def-21-5

> [!theorem] Theorem §21.2: Existence of the Laplace Transform
> Suppose that
> 1. $f$ is piecewise continuous on the interval $0 \le t \le A$ for every positive $A$, and
> 2. there exist real constants $K$, $a$ and $M$, with $K$ and $M$ positive, such that $|f(t)| \le Ke^{at}$ when $t \ge M$.
>
> Then the Laplace transform $\mathcal{L}\{f(t)\} = F(s)$, defined by (4), exists for $s > a$.
>
> *BDP: Theorem 6.1.2*

^thm-21-2

> [!proof]+ Proof
> Fix $s > a$. We show that the integral in (4) converges. Split it at $M$:
>
> $$
> \int_0^\infty e^{-st}f(t)\,dt = \int_0^M e^{-st}f(t)\,dt + \int_M^\infty e^{-st}f(t)\,dt . \qquad (5)
> $$
>
> **First integral.** $e^{-st}$ is continuous and $f$ is piecewise continuous on $[0, M]$ by hypothesis 1, so $e^{-st}f(t)$ is piecewise continuous there and the integral exists ([[§21 Definition of the Laplace Transform#^def-21-2|Definition §21.2]]).
>
> **Second integral.** $e^{-st}f(t)$ is piecewise continuous for $t \ge M$, and by hypothesis 2,
>
> $$
> |e^{-st}f(t)| \le Ke^{-st}e^{at} = Ke^{(a - s)t}, \qquad t \ge M .
> $$
>
> By [[§21 Definition of the Laplace Transform#^ex-21-1|Example §21.1]](b) with $c = a - s < 0$, $\int_M^\infty Ke^{(a - s)t}\,dt = Ke^{(a-s)M}/(s - a)$ converges. By the comparison test ([[§21 Definition of the Laplace Transform#^thm-21-1|Theorem §21.1]], with $g(t) = Ke^{(a - s)t}$), $\int_M^\infty e^{-st}f(t)\,dt$ converges.
>
> Since $\int_0^A = \int_0^M + \int_M^A$ for $A > M$, the limit of $\int_0^A e^{-st}f(t)\,dt$ as $A \to \infty$ exists, so $F(s)$ exists.

^pf-21-2

*Uses:* [[§21 Definition of the Laplace Transform#^def-21-2|Def. §21.2]], [[§21 Definition of the Laplace Transform#^ex-21-1|Ex. §21.1]], [[§21 Definition of the Laplace Transform#^thm-21-1|§21.1]]

> [!remark]- Connections
> - For complex $s$ the same comparison, with $\operatorname{Re}s$ in place of $s$, gives absolute convergence for $\operatorname{Re}s > a$; this is where the Bromwich inversion formula of [[§95★ Inverse Laplace Transforms#^thm-95-4|342 Thm. §95.4]] starts.

Functions satisfying the hypotheses of [[§21 Definition of the Laplace Transform#^thm-21-2|Theorem §21.2]] are called **piecewise continuous and of exponential order**. Except in [[§25 Impulse Functions|§25]] (BDP 6.5), the chapter deals almost exclusively with such functions.

> [!example] Example §21.2: The Transforms of 1 and of an Exponential
> **(a)** For $f(t) = 1$, $t \ge 0$, as in [[§21 Definition of the Laplace Transform#^ex-21-1|Example §21.1]](b):
>
> $$
> \mathcal{L}\{1\} = \int_0^\infty e^{-st}\,dt = -\lim_{A \to \infty} \frac{e^{-st}}{s}\bigg|_0^A = \frac1s, \qquad s > 0 .
> $$
>
> **(b)** For $f(t) = e^{at}$, $t \ge 0$, again by [[§21 Definition of the Laplace Transform#^ex-21-1|Example §21.1]](b), now with $c = -(s - a)$:
>
> $$
> \mathcal{L}\{e^{at}\} = \int_0^\infty e^{-st}e^{at}\,dt = \int_0^\infty e^{-(s - a)t}\,dt = \frac{1}{s - a}, \qquad s > a .
> $$
>
> *BDP: Examples 6.1.4 and 6.1.5*

^ex-21-2

> [!remark]- Connections
> - See also: [[§42 Definite Integrals of Functions w(t)#^ex-42-5|342 Ex. §42.5]] (the transform of $1$ for complex $s$ with $\operatorname{Re} s > 0$).

> [!example] Example §21.3: A Unit Pulse
> Find the Laplace transform of
>
> $$
> f(t) = \begin{cases} 1, & 0 \le t < 1, \\ k, & t = 1, \\ 0, & t > 1, \end{cases}
> $$
>
> where $k$ is a constant. (In engineering, $f$ often represents a unit pulse of force or voltage.)
>
> $f$ is piecewise continuous, and by (2)
>
> $$
> \mathcal{L}\{f(t)\} = \int_0^\infty e^{-st}f(t)\,dt = \int_0^1 e^{-st}\,dt = -\frac{e^{-st}}{s}\bigg|_0^1 = \frac{1 - e^{-s}}{s}, \qquad s > 0 .
> $$
>
> The transform does not depend on $k$, the value at the discontinuity; it would be the same if $f$ were undefined at $t = 1$. So functions that differ only at a single point have the same Laplace transform. (This is why the uniqueness statement [[§22 Solution of Initial Value Problems#^thm-22-4|Theorem §22.4]] is made for continuous functions.)
>
> *BDP: Example 6.1.6*

^ex-21-3

> [!theorem] Theorem §21.3: Linearity of the Laplace Transform
> Suppose that $\mathcal{L}\{f_1(t)\}$ exists for $s > a_1$ and $\mathcal{L}\{f_2(t)\}$ exists for $s > a_2$. Then for $s > \max(a_1, a_2)$ and any constants $c_1$, $c_2$,
>
> $$
> \mathcal{L}\{c_1f_1(t) + c_2f_2(t)\} = c_1\mathcal{L}\{f_1(t)\} + c_2\mathcal{L}\{f_2(t)\} . \qquad (6)
> $$
>
> The Laplace transform is a **linear operator**. The same holds for sums of any finite number of terms.
>
> *BDP: 6.1, Equation (6)*

^thm-21-3

> [!proof]+ Proof
> Let $s > \max(a_1, a_2)$, so that both transforms exist. For each finite $A$, linearity of the definite integral gives
>
> $$
> \int_0^A e^{-st}\big(c_1f_1(t) + c_2f_2(t)\big)\,dt = c_1\int_0^A e^{-st}f_1(t)\,dt + c_2\int_0^A e^{-st}f_2(t)\,dt .
> $$
>
> As $A \to \infty$ the right side tends to $c_1\mathcal{L}\{f_1\} + c_2\mathcal{L}\{f_2\}$ (limit of a sum), so the left side has the same limit, which is (6). (BDP writes this directly with the improper integrals; passing through finite $A$ shows why the left side converges.) For more terms, induct on the number of terms.

^pf-21-3

*Uses:* [[§21 Definition of the Laplace Transform#^def-21-4|Def. §21.4]], [[§21 Definition of the Laplace Transform#^def-21-1|Def. §21.1]]

> [!example] Example §21.4: The Transform of a Sine, and a Linear Combination
> **(a)** Find $\mathcal{L}\{\sin(at)\}$ ($a \ne 0$) and the values of $s$ for which it is defined.
>
> $F(s) = \lim_{A \to \infty} \int_0^A e^{-st}\sin(at)\,dt$. Integrating by parts (with $u = e^{-st}$, $dv = \sin(at)\,dt$),
>
> $$
> F(s) = \lim_{A \to \infty}\left[-\frac{e^{-st}\cos(at)}{a}\bigg|_0^A - \frac{s}{a}\int_0^A e^{-st}\cos(at)\,dt\right] = \frac1a - \frac{s}{a}\int_0^\infty e^{-st}\cos(at)\,dt ,
> $$
>
> since for $s > 0$, $|e^{-sA}\cos(aA)/a| \le e^{-sA}/|a| \to 0$. A second integration by parts ($dv = \cos(at)\,dt$; the boundary term $e^{-st}\sin(at)/a$ vanishes at both ends) gives
>
> $$
> F(s) = \frac1a - \frac{s^2}{a^2}\int_0^\infty e^{-st}\sin(at)\,dt = \frac1a - \frac{s^2}{a^2}F(s) .
> $$
>
> Solving, $F(s)\big(1 + s^2/a^2\big) = 1/a$, so
>
> $$
> \mathcal{L}\{\sin(at)\} = \frac{a}{s^2 + a^2}, \qquad s > 0 .
> $$
>
> (In the same way, $\mathcal{L}\{\cos(at)\} = s/(s^2 + a^2)$ for $s > 0$; BDP, Problem 6.1.5. A shorter derivation, from the transform of a derivative, is in the proof of [[§22 Solution of Initial Value Problems#^thm-22-6|Theorem §22.6]], entry 6.)
>
> **(b)** Find the Laplace transform of $f(t) = 5e^{-2t} - 3\sin(4t)$, $t \ge 0$.
>
> By linearity ([[§21 Definition of the Laplace Transform#^thm-21-3|Theorem §21.3]]) and [[§21 Definition of the Laplace Transform#^ex-21-2|Example §21.2]](b) with $a = -2$ and part (a) with $a = 4$,
>
> $$
> \mathcal{L}\{f(t)\} = 5\mathcal{L}\{e^{-2t}\} - 3\mathcal{L}\{\sin(4t)\} = \frac{5}{s + 2} - \frac{12}{s^2 + 16}, \qquad s > 0 ,
> $$
>
> the intersection of $s > -2$ and $s > 0$.
>
> *BDP: Examples 6.1.7 and 6.1.8*

^ex-21-4
