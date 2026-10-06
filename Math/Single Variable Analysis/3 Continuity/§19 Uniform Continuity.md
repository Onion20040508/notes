---
subject: "[[Single Variable Analysis]]"
section: 19
chapter: 3
tags: [real-analysis, math451]
---
← [[§18 Properties of Continuous Functions]] · ↑ [[· 3 Continuity]] · [[§20 Limits of Functions]] →

In the $(\varepsilon, \delta)$ definition of continuity, one important point: $\delta$ depends on $\varepsilon$ *and on the point $x_0$*. This was very clear for $f(x) = \sqrt{x}$, where $\delta = \varepsilon\sqrt{x_0}$ shrank as $x_0 \to 0$ (§17). For some applications we want a choice of $\delta$ *independent of $x_0$* — depending only on $\varepsilon$: a uniform criterion for all points of the domain.

> [!definition] Definition §19.1: Uniform Continuity
> $f: \Omega \to \mathbb{R}$ is called **uniformly continuous** if for every $\varepsilon > 0$ there exists $\delta > 0$ such that for *every pair* $x, y \in \Omega$ with $|x - y| < \delta$,
>
> $$
> |f(x) - f(y)| < \varepsilon.
> $$
>
> The idea: whenever $x, y$ are close, $f(x), f(y)$ are close — *no matter where they are*. The condition is uniform, or fair, to every pair.

^def-19-1

> [!remark] Remark
> Compare quantifiers with ordinary continuity: there, “$\forall x_0\, \forall \varepsilon\, \exists \delta$” — here, “$\forall \varepsilon\, \exists \delta\, \forall$ pairs”. Uniform continuity implies continuity at every point (freeze $y = x_0$); the converse fails, as the next example shows.

^rem-19-1

> [!remark]- Connections
> - Strengthened in 551 to absolute continuity, which controls finitely many disjoint intervals at once ($n = 1$ gives this definition): [[§18 Differentiation Theory#^def-18-4|551 Def. §18.4]]; the Cantor function is uniformly but not absolutely continuous ([[§18 Differentiation Theory#^rem-18-7|551 Rem. §18.7]]).

> [!example] Example §19.1: The two faces of the reciprocal
> Prove: $f(x) = \tfrac1x$ is uniformly continuous on $[a, +\infty)$ for every $a > 0$, but *not* on $(0, +\infty)$. (Different domains: different functions, different properties!)
>
> **Uniform continuity on $[a, +\infty)$.** For every pair $x, y \in [a,+\infty)$, bound $|f(x) - f(y)|$ in terms of $|x-y|$, then solve for $\delta$ — the same scheme as before. Start:
>
> $$
> |f(x) - f(y)| = \left| \frac1x - \frac1y \right| = \frac{|y - x|}{|xy|} \leq \frac{|x-y|}{a^2},
> $$
>
> simplifying via the uniform lower bound $xy \geq a^2$ — this is where the domain enters. Setting $\tfrac{|x-y|}{a^2} < \varepsilon$ gives $|x - y| < a^2 \varepsilon$: take
>
> $$
> \delta = a^2 \varepsilon,
> $$
>
> which depends only on $\varepsilon$ (and the fixed $a$). Write-up: for any pair $x, y \in [a,+\infty)$ with $|x-y| < \delta$, the display gives $|f(x)-f(y)| \leq |x-y|/a^2 < \varepsilon$.
>
> **Failure on $(0, +\infty)$.** First, the negation: *not uniformly continuous* means there exists some $\varepsilon_0 > 0$ such that no matter how small $\delta$ is, there is a pair $x, y \in (0,+\infty)$ with $|x - y| < \delta$ but $|f(x) - f(y)| \geq \varepsilon_0$.
>
> Where to find such pairs? In $\tfrac{|y-x|}{|xy|}$, the numerator is small — but the denominator can be *very* small too. Try $y = \tfrac12 x$:
>
> $$
> \frac{|y - x|}{|xy|} = \frac{\tfrac12 x}{x \cdot \tfrac12 x} = \frac1x,
> $$
>
> which is large when $x$ is small. Formally: take $\varepsilon_0 = 1$; for any $\delta > 0$, choose $x < \min\{\delta, 1\}$ and $y = \tfrac12 x$. Then
>
> $$
> |x - y| = \tfrac12 x < \delta, \qquad \text{but} \qquad |f(x) - f(y)| = \frac1x \geq 1 = \varepsilon_0.
> $$
>
> So $f$ is not uniformly continuous on $(0,+\infty)$.
>
> The better understanding: $\tfrac{|y-x|}{|xy|}$ is *not uniformly small* when $|x-y|$ is small — near $0$ the function is too steep. The same argument shows $f(x) = \tfrac1x$ is not uniformly continuous on $(0, 1]$.

^ex-19-1

![[m451-19-1.svg]]
*Why $\tfrac1x$ fails on $(0,+\infty)$: boxes of the same height $2\varepsilon$ (red), each as wide as the graph allows while leaving through the sides. Far out the curve is flat and the box is wide; near $0$ it is steep and the admissible width $2\delta$ shrinks to nothing — no single $\delta$ serves all points. On $[a, +\infty)$ the steepness is capped, and $\delta = a^2\varepsilon$ works everywhere.*

## Continuity on Closed Intervals Implies Uniform Continuity

> [!theorem] Theorem §19.1: Uniform Continuity on Closed Bounded Intervals
> If $f: [a,b] \to \mathbb{R}$ is a continuous function on a closed bounded interval, then $f$ is uniformly continuous.

^thm-19-1

This is another important property of continuous functions on closed bounded intervals — crucial for the Riemann integral $\int_a^b f(x)\,dx$ later.

> [!proof]+ Proof
> It is not clear how to produce a uniform $\delta$ directly, so we prove it by contradiction. If $f$ is not uniformly continuous, there exists $\varepsilon > 0$ such that for every $\delta = \tfrac1n$, $n \in \mathbb{N}$, there is a pair $x_n, y_n \in [a,b]$ with
>
> $$
> |x_n - y_n| < \frac1n \qquad \text{but} \qquad |f(x_n) - f(y_n)| \geq \varepsilon.
> $$
>
> Since $x_n \in [a,b]$ is a bounded sequence, [[Bolzano–Weierstrass Theorem|Bolzano–Weierstrass]] gives a convergent subsequence $x_{n_k} \to x_0$, and $x_0 \in [a,b]$ (limits preserve the endpoint inequalities). Then also $y_{n_k} \to x_0$ — why? — because
>
> $$
> |y_{n_k} - x_0| \leq |y_{n_k} - x_{n_k}| + |x_{n_k} - x_0| < \frac{1}{n_k} + |x_{n_k} - x_0| \longrightarrow 0.
> $$
>
> Since $f$ is continuous at $x_0$: $f(x_{n_k}) \to f(x_0)$ and $f(y_{n_k}) \to f(x_0)$, so
>
> $$
> |f(x_{n_k}) - f(y_{n_k})| \longrightarrow 0,
> $$
>
> contradicting $|f(x_n) - f(y_n)| \geq \varepsilon$ for all $n$.

^pf-19-1

> [!remark] Remark: Why should this be true?
> Giving a proof is not enough — like driving, you need to *feel* it. Here is the suggestive (non-rigorous) picture. Continuity provides, at each point $x_0$, a quantity $\delta = \delta(\varepsilon, x_0) > 0$. The choice is not unique, and it seems reasonable that a “suitable” choice is *continuous* in $x_0$. But a continuous positive function on $[a,b]$ attains a *minimum* ([[Extreme Value Theorem|Extreme Value Theorem]]), which is then positive — and this worst-case value serves as the uniform $\delta$. **This is not a proof** — but it explains the theorem, and the actual proof mirrors it: assuming failure, we hunt down the “bad places” with Bolzano–Weierstrass, just as in the proof of the Extreme Value Theorem itself. Bolzano–Weierstrass is the basis of many results — that is why it is so important.

^rem-19-2

## Uniform Continuity and Cauchy Sequences

> [!example] Example §19.2: Steepness at infinity (HW)
> The closed-interval theorem needs *both* hypotheses: bounded is as essential as closed. On the closed but unbounded set $\mathbb{R}$, even the polynomial $f(x) = x^3$ fails to be uniformly continuous. Following the negation format above, take the pairs
>
> $$
> x_n = n, \qquad y_n = n + \frac1n: \qquad |y_n - x_n| = \frac1n \to 0,
> $$
>
> but
>
> $$
> |f(y_n) - f(x_n)| = \left( n + \tfrac1n \right)^3 - n^3 = 3n + \frac{3}{n} + \frac{1}{n^3} \geq 3.
> $$
>
> So for $\varepsilon_0 = 3$, no $\delta$ can work. Compare the reciprocal example: there the failure was steepness *near $0$* on a bounded set; here it is steepness *at infinity* on a closed set. (On any $[-M, M]$, of course, $x^3$ is uniformly continuous by the theorem.)

^ex-19-2

> [!theorem] Proposition §19.2: Uniform Continuity via Continuous Extension (HW)
> Trivially, if $f$ is uniformly continuous on a set $A$, it is uniformly continuous on every subset of $A$ (the same $\delta$ works). Combining with the theorem: if $f: (a, b] \to \mathbb{R}$ extends to a *continuous* function $\tilde f: [a,b] \to \mathbb{R}$, then $f$ is uniformly continuous on $(a,b]$.

^prop-19-2

> [!proof]+ Proof
> $\tilde f$ is continuous on the finite closed interval $[a,b]$, hence uniformly continuous there by the theorem; and $f = \tilde f$ on the subset $(a,b]$.

^pf-19-2

> [!example] Example §19.3: Extension versus oscillation (HW)
> **(1)** $f(x) = x^2 \sin\tfrac1x$ *is* uniformly continuous on $(0,1]$. Extend by $\tilde f(0) = 0$: continuity at $0$ holds since $|\tilde f(x) - \tilde f(0)| = |x^2 \sin\tfrac1x| \leq x^2$, so $\delta = \sqrt\varepsilon$ works ($\S 17$'s squeeze); on $(0,1]$, $\tilde f = f$ is continuous by the product and composition theorems. Apply the proposition.
>
> **(2)** By contrast, $g(x) = \sin\tfrac{1}{x^2}$ is *not* uniformly continuous on $(0,1]$, although it is bounded and the set is bounded — a third failure mode: *oscillation*. Take the pairs
>
> $$
> x_n = \frac{1}{\sqrt{2\pi n}}, \qquad y_n = \frac{1}{\sqrt{2\pi n + \tfrac\pi2}}:
> \qquad g(x_n) = \sin(2\pi n) = 0, \quad g(y_n) = \sin\left(2\pi n + \tfrac\pi2\right) = 1,
> $$
>
> so $|g(x_n) - g(y_n)| = 1$, while $|x_n - y_n| \leq x_n \to 0$. No continuous extension to $[0,1]$ can exist for this $g$ — and in fact the converse of the proposition is also true (Ross 19.5): a uniformly continuous function on $(a,b]$ *always* extends continuously to $[a,b]$, essentially by the Cauchy-preservation theorem below. Extension and uniform continuity are two descriptions of the same phenomenon.

^ex-19-3

![[m451-19-2.svg]]
*The other two failure modes. Left: steepness at infinity — the pairs $x_n = n$, $y_n = n + \tfrac1n$ (red, $n = 2, 3$) get closer horizontally while $f(y_n) - f(x_n) \geq 3$ (red rises). Right: oscillation on a bounded set — $g = \sin\tfrac{1}{x^2}$ is bounded, yet $x_n = \tfrac{1}{\sqrt{2\pi n}}$ (red dots on the axis) and $y_n = \tfrac{1}{\sqrt{2\pi n + \pi/2}}$ (red dots at height $1$) crowd together as $n$ grows while $|g(x_n) - g(y_n)| = 1$; shaded: the infinitely many oscillations near $0$.*

> [!theorem] Theorem §19.3: Uniformly Continuous Functions Preserve Cauchy Sequences
> If $f: \Omega \to \mathbb{R}$ is uniformly continuous and $(s_n)$ is a Cauchy sequence in $\Omega$, then $(f(s_n))$ is also a Cauchy sequence.

^thm-19-3

> [!proof]+ Proof
> Given $\varepsilon > 0$, we need $N$ such that $|f(s_n) - f(s_m)| < \varepsilon$ for all $m, n \geq N$. Uniform continuity provides $\delta = \delta(\varepsilon) > 0$ such that $|x - y| < \delta$ implies $|f(x) - f(y)| < \varepsilon$ for $x, y \in \Omega$. Since $(s_n)$ is Cauchy, applied with tolerance $\delta$: there exists $N$ such that $|s_n - s_m| < \delta$ for $m, n \geq N$. For such $m, n$: $|f(s_n) - f(s_m)| < \varepsilon$. Done.

^pf-19-3

> [!remark] Remark: Warning with counterexample
> If $f$ is only continuous but not uniformly continuous, the conclusion fails. To build a counterexample, start from our non-uniformly continuous function $f(x) = \tfrac1x$ on $(0,+\infty)$. Which Cauchy sequence to take? The problem with $f$ is near $0$, so take $s_n \to 0$: say $s_n = \tfrac1n$ — Cauchy, since convergent. But
>
> $$
> f(s_n) = n,
> $$
>
> not Cauchy at all (unbounded).

^rem-19-3

> [!theorem] Proposition §19.4: Uniformly Continuous on a Bounded Set Implies Bounded
> Let $\Omega \subseteq \mathbb{R}$ be a bounded set. If $f: \Omega \to \mathbb{R}$ is uniformly continuous, then $f$ is bounded. (An important case: $\Omega = (a,b)$. Without uniform continuity this fails: $f(x) = \tfrac1x$ on $(0,1)$.)

^prop-19-4

> [!proof]+ Proof
> If not, then for every $n \in \mathbb{N}$ there is $x_n \in \Omega$ with $|f(x_n)| \geq n$. Since $\Omega$ is bounded, $(x_n)$ is a bounded sequence; by Bolzano–Weierstrass there is a convergent subsequence $x_{n_k} \to x_0$. Now $x_0$ *may not belong to $\Omega$* — this is exactly why we cannot argue with continuity at $x_0$, and why the Cauchy theorem above is the right tool: $(x_{n_k})$, being convergent, is a Cauchy sequence in $\Omega$, so $(f(x_{n_k}))$ is Cauchy, hence convergent, hence *bounded* (§10, §9). But $|f(x_{n_k})| \geq n_k \to \infty$ — a contradiction.

^pf-19-4

## A Criterion via the Derivative

> [!theorem] Theorem §19.5: Bounded Derivative Implies Uniform Continuity
> Let $f: (a, +\infty) \to \mathbb{R}$ be continuous. If $f$ is differentiable with bounded derivative — $|f'(x)| \leq M$ for all $x$ — then $f$ is uniformly continuous. The same holds on any interval $(a,b)$, $(a,b]$, $[a,b)$ with $f$ differentiable and $f'$ bounded on the interior.

^thm-19-5

> [!proof]+ Proof
> We need the **[[Mean Value Theorem|Mean Value Theorem]]**, which we accept now and prove later ([[· 5 Differentiation|Chapter 5]], §29). For any pair $x, y$ in the interval, the MVT gives a point $c$ between them with
>
> $$
> f(x) - f(y) = f'(c)(x - y), \qquad \text{hence} \qquad |f(x) - f(y)| = |f'(c)|\,|x-y| \leq M |x - y|
> $$
>
> — a simple bound in terms of $|x-y|$. So for every $\varepsilon > 0$, take $\delta = \varepsilon / M$ (if $M = 0$, then $f$ is constant and any $\delta$ works): when $|x - y| < \delta$, $|f(x) - f(y)| \leq M|x-y| < \varepsilon$. Done.

^pf-19-5

> [!example] Example §19.4: Cosine
> $f(x) = \cos x: \mathbb{R} \to \mathbb{R}$ is uniformly continuous: $f'(x) = -\sin x$ is bounded by $1$. (As before, $\sin$, $\cos$ and their derivatives are used on credit here.)

^ex-19-4

> [!remark] Remark: The converse fails
> A uniformly continuous differentiable function need not have bounded derivative. Take $f(x) = \sqrt{x}$ on $[0,1]$: it is continuous on the closed bounded interval, hence uniformly continuous there (theorem above) — and therefore also uniformly continuous on the open interval $(0,1)$. But
>
> $$
> f'(x) = \frac{1}{2\sqrt x}, \qquad x \in (0,1),
> $$
>
> is not bounded.

^rem-19-4

So each of the two theorems covers a region the other misses: near $0$, the closed-interval theorem handles $\sqrt x$ (steep but compact); far out, the derivative $\tfrac{1}{2\sqrt x} \leq \tfrac12$ is bounded on $[1, \infty)$ (HW). Can the two regions be *glued*?

> [!theorem] Proposition §19.6: Gluing Lemma for Uniform Continuity (HW)
> Let $c \in \mathbb{R}$ and let $f$ be uniformly continuous on $A = (-\infty \text{ or } a, c]$ and on $B = [c, b \text{ or } \infty)$. Then $f$ is uniformly continuous on $A \cup B$. The junction point must belong to *both* pieces.

^prop-19-6

> [!proof]+ Proof
> Given $\varepsilon > 0$, uniform continuity on $A$ and on $B$ provides $\delta_A, \delta_B > 0$ for the tolerance $\tfrac\varepsilon2$; take $\delta = \min\{\delta_A, \delta_B\}$. Let $x, y \in A \cup B$ with $|x - y| < \delta$, say $x \leq y$. If both lie in the same piece, then $|f(x) - f(y)| < \tfrac\varepsilon2 < \varepsilon$ directly. Otherwise $x \leq c \leq y$, and the junction point mediates: $|x - c| \leq |x - y| < \delta$ and $|c - y| \leq |x-y| < \delta$, with the pairs $(x, c)$ and $(c, y)$ each inside one piece, so
>
> $$
> |f(x) - f(y)| \leq |f(x) - f(c)| + |f(c) - f(y)| < \frac\varepsilon2 + \frac\varepsilon2 = \varepsilon.
> $$

^pf-19-6

> [!example] Example §19.5: The square root globally
> $f(x) = \sqrt x$ is uniformly continuous on all of $[0, +\infty)$: on $[0,1]$ by the closed-interval theorem, on $[1, +\infty)$ by the bounded-derivative theorem, and on the union by the gluing lemma with $c = 1$. Each of the three results of this section contributes exactly the step the others cannot supply.

^ex-19-5
