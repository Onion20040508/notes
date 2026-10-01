---
subject: "[[Single Variable Analysis]]"
section: 34
chapter: 6
tags: [real-analysis, math451]
---
← [[§33 Properties of the Riemann Integral]] · ↑ [[· 6 Integration]] · [[§35 Riemann–Stieltjes Integrals]] →

The last main section — and the moment the oldest debts of these notes are repaid.

## The First Fundamental Theorem

> [!theorem] Theorem §34.1: Fundamental Theorem of Calculus I
> Assume $g: [a,b] \to \mathbb{R}$ is continuous, differentiable on $(a,b)$, and $g'$ is integrable on $[a,b]$. Then
>
> $$
> \int_a^b g'(x)\,dx = g(b) - g(a).
> $$

^thm-34-1

We all know this — but how to *prove* it? The integral $\int_a^b g'$ is defined via upper and lower sums $U(g', P)$, $L(g', P)$; the key is to trap $g(b) - g(a)$ between the *same* sums.

> [!proof]+ Proof
> Let $\varepsilon > 0$. Since $g'$ is integrable, the Cauchy criterion provides a partition
>
> $$
> P: \quad a = t_0 < t_1 < \cdots < t_n = b, \qquad U(g', P) - L(g', P) < \varepsilon.
> $$
>
> Telescope the increment of $g$ along the partition, and apply the **[[Mean Value Theorem|Mean Value Theorem]]** on each subinterval ($g$ is continuous on $[t_{k-1}, t_k]$ and differentiable inside):
>
> $$
> g(b) - g(a) = \sum_{k=1}^n \bigl( g(t_k) - g(t_{k-1}) \bigr) = \sum_{k=1}^n g'(x_k)\,(t_k - t_{k-1})
> $$
>
> for some points $x_k \in (t_{k-1}, t_k)$ — the middle expression is a *Riemann sum* for $g'$. Now bracket each term:
>
> $$
> m\bigl(g', [t_{k-1},t_k]\bigr)(t_k - t_{k-1}) \ \leq\ g'(x_k)(t_k - t_{k-1}) \ \leq\ M\bigl(g', [t_{k-1},t_k]\bigr)(t_k - t_{k-1}),
> $$
>
> and sum:
>
> $$
> L(g', P) \ \leq\ g(b) - g(a) \ \leq\ U(g', P).
> $$
>
> But also, by the definition of the Darboux integral,
>
> $$
> L(g', P) \ \leq\ \int_a^b g'\,dx \ \leq\ U(g', P).
> $$
>
> Both numbers lie in an interval of length $< \varepsilon$, so (sandwich)
>
> $$
> \left| \int_a^b g'\,dx - \bigl( g(b) - g(a) \bigr) \right| < \varepsilon.
> $$
>
> Since $\varepsilon$ is arbitrary, the difference is $0$. Done.

^pf-34-1

![[m451-34-2.svg]]
*The proof of FTC I: on each $[t_{k-1}, t_k]$ the Mean Value Theorem gives a point $x_k$ where the tangent (red) is parallel to the chord (dashed), so $g(t_k) - g(t_{k-1}) = g'(x_k)(t_k - t_{k-1})$. Summed, the increments telescope to $g(b) - g(a)$ — while the right side becomes a Riemann sum for $g'$, trapped between $L(g', P)$ and $U(g', P)$.*

## Integration by Parts

Integration by parts needs a preliminary: products of integrable functions are integrable.

> [!theorem] Lemma §34.2: Products of Integrable Functions
> If $f, g: [a,b] \to \mathbb{R}$ are integrable, then $f^2$ and $fg$ are integrable.

^lem-34-2

> [!proof]+ Proof
> *Step 1: $f^2$.* Let $B$ bound $|f|$. From the factorization $f(x)^2 - f(y)^2 = \bigl(f(x)+f(y)\bigr)\bigl(f(x)-f(y)\bigr)$, on any subinterval $I$,
>
> $$
> \bigl| f(x)^2 - f(y)^2 \bigr| \leq 2B\, |f(x) - f(y)| \leq 2B\bigl( M(f,I) - m(f,I) \bigr),
> $$
>
> and taking the sup over pairs, $M(f^2, I) - m(f^2, I) \leq 2B\bigl(M(f,I) - m(f,I)\bigr)$. Hence
>
> $$
> U(f^2, P) - L(f^2, P) \leq 2B\bigl( U(f,P) - L(f,P) \bigr),
> $$
>
> and the Cauchy criterion transfers from $f$ to $f^2$ (choose $P$ with $U - L < \tfrac{\varepsilon}{2B}$).
>
> *Step 2: $fg$.* Use the polarization identity
>
> $$
> fg = \frac14\Bigl( (f+g)^2 - (f-g)^2 \Bigr):
> $$
>
> $f \pm g$ are integrable (linearity), their squares are integrable (Step 1), and linear combinations of integrable functions are integrable.

^pf-34-2

> [!theorem] Theorem §34.3: Integration by Parts
> If $u, v: [a,b] \to \mathbb{R}$ are continuous, differentiable on $(a,b)$, and $u', v'$ are integrable on $[a,b]$, then
>
> $$
> \int_a^b u(x)v'(x)\,dx = u(b)v(b) - u(a)v(a) - \int_a^b u'(x)v(x)\,dx.
> $$
>
> The point: trade the integrand $uv'$ for $u'v$, hoping it is simpler.

^thm-34-3

> [!proof]+ Proof
> By the lemma, $uv'$ and $u'v$ are integrable (each factor is integrable: $u, v$ are continuous, $u', v'$ by hypothesis). Apply [[Fundamental Theorem of Calculus|FTC]] I to $g = uv$: by the product rule $g' = u'v + uv'$, which is integrable, so
>
> $$
> u(b)v(b) - u(a)v(a) = g(b) - g(a) = \int_a^b g'\,dx = \int_a^b u'v\,dx + \int_a^b uv'\,dx,
> $$
>
> and rearrange.

^pf-34-3

## The Second Fundamental Theorem

> [!theorem] Theorem §34.4: Fundamental Theorem of Calculus II
> If $f: [a,b] \to \mathbb{R}$ is bounded and integrable, then
>
> $$
> F(x) = \int_a^x f(t)\,dt
> $$
>
> is a continuous function of $x$ on $[a,b]$. If moreover $f$ is continuous at $x_0$, then $F$ is differentiable at $x_0$ with
>
> $$
> F'(x_0) = f(x_0).
> $$
>
> Likewise, $G(x) = \int_x^b f(t)\,dt$ satisfies $G'(x_0) = -f(x_0)$ (since $G = \int_a^b f - F$).

^thm-34-4

> [!remark] Remark: Orientation convention
> For $x < y$ we set $\int_y^x f = -\int_x^y f$; then additivity $\int_a^x = \int_a^y + \int_y^x$ holds for any order of the points, and the estimates below are valid regardless of the side from which $x$ approaches $x_0$.

^rem-34-1

> [!proof]+ Proof
> **Continuity of $F$.** Let $M$ bound $|f|$. For any $x, y$,
>
> $$
> |F(x) - F(y)| = \left| \int_y^x f(t)\,dt \right| \leq \left| \int_y^x M\,dt \right| = M\,|x - y|,
> $$
>
> so $F$ is Lipschitz — in particular (uniformly) continuous.
>
> **Differentiability at a continuity point.** For $x \neq x_0$, using $\int_{x_0}^x f(x_0)\,dt = f(x_0)(x - x_0)$,
>
> $$
> \frac{F(x) - F(x_0)}{x - x_0} - f(x_0) = \frac{1}{x - x_0}\int_{x_0}^x \bigl( f(t) - f(x_0) \bigr)\,dt.
> $$
>
> Since $f$ is continuous at $x_0$: for every $\varepsilon > 0$ there is $\delta > 0$ with $|f(t) - f(x_0)| < \varepsilon$ whenever $|t - x_0| < \delta$. If $|x - x_0| < \delta$, then every $t$ between $x_0$ and $x$ also satisfies $|t - x_0| < \delta$, so
>
> $$
> \left| \frac{1}{x - x_0}\int_{x_0}^x \bigl(f(t) - f(x_0)\bigr)\,dt \right| \leq \frac{1}{|x - x_0|} \left| \int_{x_0}^x \varepsilon\,dt \right| = \varepsilon.
> $$
>
> Hence the difference quotient tends to $f(x_0)$: $F'(x_0) = f(x_0)$. Done.

^pf-34-4

![[m451-34-1.svg]]
*The proof in one strip: $F(x)$ is the shaded area, and the increment $F(x+h) - F(x)$ is the thin strip — of area $f(x) h$ up to an error controlled by the continuity of $f$ at $x$. Dividing by $h$: $F'(x) = f(x)$.*

> [!example] Example §34.1: FTC I from FTC II when the derivative is continuous (HW)
> The two halves of the FTC are not independent: if $g'$ is *continuous*, FTC I follows from FTC II in three lines. Set $G(x) = \int_a^x g'(t)\,dt$. By FTC II, $G$ is continuous on $[a,b]$ and $G' = g'$ on $(a,b)$; so $G - g$ has vanishing derivative on $(a,b)$ and is constant there (§29), and the constancy extends to the closed interval by continuity of $G - g$. Evaluating the constant at both ends,
>
> $$
> G(b) - g(b) = G(a) - g(a) = 0 - g(a), \qquad \text{i.e.} \qquad \int_a^b g'(t)\,dt = G(b) = g(b) - g(a).
> $$

^ex-34-1

> [!remark] Remark
> So why did FTC I get its own telescoping proof? Because its hypothesis is weaker: $g'$ need only be *integrable*. Discontinuous derivatives genuinely occur (§28's middle rung $x^2\sin\tfrac1x$ has a derivative with no limit at $0$), and at a discontinuity point FTC II is silent about $G'$ — the shortcut above collapses. The telescope, using only the MVT on each subinterval, never needs to differentiate $G$ at all. A theorem proved twice, under different hypotheses, is really two theorems.

^rem-34-2

> [!example] Example §34.2: Variable limits and the chain rule
> Assume $f$ is continuous on $\mathbb{R}$. Show $G(x) = \displaystyle\int_0^{\sin x} f(t)\,dt$ is differentiable and compute $G'$.
>
> Write $G = F \circ \sin$, where $F(u) = \int_0^u f(t)\,dt$. By FTC II, $F' = f$ everywhere (continuity of $f$); by the chain rule (§28),
>
> $$
> G'(x) = F'(\sin x)\cdot(\sin x)' = f(\sin x)\,\cos x. \tag*{$\blacksquare$}
> $$

^ex-34-2

One step deserves scrutiny (HW): the claim “$F' = f$ *everywhere*” — FTC II was stated on an interval $[a,b]$, while here $u = \sin x$ roams over $[-1,1]$, on both sides of the base point $0$. The global statement is true and worth recording: *for $f$ continuous on $\mathbb{R}$ and any fixed base point $a$, the function $F(u) = \int_a^u f\,dt$ (orientation convention for $u < a$) is differentiable on all of $\mathbb{R}$ with $F' = f$.* For $u > a$, apply FTC II on an interval $[a, b]$ containing $u$ in its interior. For $u < a$, take $[c, a] \ni u$: the convention gives $F(u) = -\int_u^a f\,dt$, and the second half of FTC II (the decreasing-limit function $G$, with its minus sign) yields $F'(u) = -(-f(u)) = f(u)$. The two signs — orientation and endpoint-direction — cancel exactly.

> [!example] Example §34.3: A sliding window (HW)
> Let $f$ be continuous on $\mathbb{R}$ and
>
> $$
> F(x) = \int_{x-1}^{x+1} f(t)\,dt
> $$
>
> — the integral over a window of width $2$ sliding along the line. Both limits move at once; split at any base point using the global antiderivative $F_0(u) = \int_0^u f\,dt$ just discussed:
>
> $$
> F(x) = F_0(x+1) - F_0(x-1),
> $$
>
> and the chain rule gives differentiability on all of $\mathbb{R}$ with
>
> $$
> F'(x) = f(x+1) \cdot 1 - f(x-1) \cdot 1 = f(x+1) - f(x-1)
> $$
>
> — the window's rate of change is what enters at the front edge minus what leaves at the back.

^ex-34-3

> [!remark] Remark: Integration smooths
> Note the regularity ledger of the sliding window: $f$ was merely *continuous*, yet $F$ is *continuously differentiable* — integration bought one full degree of smoothness for free (FTC II's continuity clause shows this already for $F_0$: integrable $\Rightarrow$ the integral function is Lipschitz; continuous $\Rightarrow$ it is $C^1$). Averaging a function over a moving window to gain regularity is the germ of *mollification*, a standard device of analysis.

^rem-34-3

> [!remark] Remark: Closing the ledger
> FTC II is exactly the statement borrowed in §26 to prove term-by-term differentiation of power series ($\tfrac{d}{dx}\int_0^x g = g$ for continuous $g$); FTC I underwrites every explicit evaluation of integrals used in §15 (the integral test computation), §25–§26, and §31. All of those credits are now paid off. Two loans remain open at semester's end, both from sections not covered: the rigorous construction of decimal expansions (§16), and the rigorous definitions of $e^x$, $\log$, $\sin$, $\cos$ with their derivatives (Ross §37) — everything in these notes uses of them only the properties cited at the point of borrowing. (A first installment on the trigonometric loan is paid in §26: the series-defined $s$ and $c$ satisfy $s' = c$, $c' = -s$, and $s^2 + c^2 = 1$ by pure power-series calculus. And the improper-integral symbol $\int_1^\infty$, used by §15's integral test, is formally defined and its p-integral computed in §36.)

^rem-34-4
