---
type: section
subject: "[[Measure Theory]]"
chapter: 5
section: 18
tags: [measure-theory, math551]
---
← [[§18c Absolute Continuity]] · ↑ [[· 5 Differentiation and the FTC]] · [[§18e The Cantor Function]] →

This section answers [[§18c Absolute Continuity#^rem-18-5|the central question revisited]]: under what assumptions does $f(x) - f(a) = \int_a^x f'(t)\,dt$ hold for all $x \in [a, b]$?

## The Fundamental Theorem of Calculus for Lebesgue Integrals

> [!theorem] Theorem §18.13: The Fundamental Theorem of Calculus for Lebesgue Integrals
> Let $f: [a, b] \to \mathbb{R}$. Then the following are equivalent:
> - (i) $f$ is absolutely continuous on $[a, b]$.
> - (ii) $f$ is differentiable a.e., $f' \in L([a, b])$, and $f(x) - f(a) = \int_a^x f'(t)\,dt$ for all $x \in [a, b]$.

^thm-18-13

> [!proof]+ Proof of the Fundamental Theorem of Calculus
> **(ii) $\Rightarrow$ (i):** Assume $f$ is differentiable a.e., $f' \in L([a, b])$, and $f(x) - f(a) = \int_a^x f'(t)\,dt$ for all $x$. Then $f(x) = f(a) + \int_a^x f'(t)\,dt$. Since $f' \in L([a,b])$, the function $x \mapsto \int_a^x f'(t)\,dt$ is in $AC([a, b])$ by [[§18c Absolute Continuity#^thm-18-12|the theorem above]] (integral functions are AC). Adding the constant $f(a)$ preserves absolute continuity ([[§18c Absolute Continuity#^prop-18-11|property (ii)]]). Hence $f \in AC([a, b])$.
>
> **(i) $\Rightarrow$ (ii):** Assume $f \in AC([a, b])$. Then $f \in BV([a, b])$ ([[§18c Absolute Continuity#^thm-18-16|AC ⟹ BV, proved above]]), so $f$ is differentiable a.e. on $(a, b)$ with $f' \in L([a, b])$ (by the [[§18a Lebesgue's Differentiation Theorem#^cor-18-10|BV differentiability corollary]]). It remains to show $f(x) - f(a) = \int_a^x f'(t)\,dt$ for all $x \in [a, b]$.
>
> Define $F(x) = f(x) - f(a) - \int_a^x f'(t)\,dt$. Since $f \in AC([a, b])$ and $\int_a^x f'(t)\,dt \in AC([a, b])$ (by the theorem above: integral functions are AC), and $AC$ is closed under linear combinations (property (ii)), we have $F \in AC([a, b])$.
>
> Moreover, $F'(x) = f'(x) - f'(x) = 0$ a.e. on $(a, b)$ (using the fact that $(\int_a^x f'\,dt)' = f'(x)$ a.e., proved in an earlier subsection; [[§18b Differentiating the Integral#^thm-18-26|§18.26]]).
>
> By the lemma on non-constant functions with zero derivative ([[§18c Absolute Continuity#^thm-18-27|Theorem §18.27]]), if $F$ were not constant, then $F$ would not be absolutely continuous. But $F \in AC([a, b])$, so $F$ must be constant. Since $F(a) = f(a) - f(a) - 0 = 0$, we conclude $F(x) = 0$ for all $x \in [a, b]$, i.e.:
>
> $$
> f(x) - f(a) = \int_a^x f'(t)\,dt \qquad \forall\, x \in [a, b].
> $$

^pf-18-13

*Uses:* [[§18c Absolute Continuity#^thm-18-12|§18.12]], [[§18c Absolute Continuity#^prop-18-11|§18.11]], [[§18c Absolute Continuity#^thm-18-16|§18.16]], [[§18a Lebesgue's Differentiation Theorem#^cor-18-10|§18.10]], [[§18b Differentiating the Integral#^thm-18-26|§18.26]], [[§18c Absolute Continuity#^thm-18-27|§18.27]]

> [!remark]- Connections
> - MATH 451 versions: [[Fundamental Theorem of Calculus]] (FTC I, 451 §34.1: $f$ continuous, differentiable on $(a,b)$, with Riemann-integrable $f'$; FTC II, 451 §34.4: the integral function).
> - The step “$F' = 0$ a.e. and AC ⟹ constant” replaces the 451 [[§29 The Mean Value Theorem#^cor-29-4|Vanishing Derivative Means Constant]] (451 §29.4), which needs $F' = 0$ everywhere.

> [!theorem] Corollary §18.14: Term-by-Term Differentiation of AC Series
> Let $\{g_k\}_{k \in \mathbb{N}}$ be a sequence of $AC$ functions on $[a, b]$, and assume $\sum_{k=1}^{\infty} g_k(c)$ converges for some $c \in [a, b]$ and $\sum_{k=1}^{\infty} \int_a^b |g_k'(x)|\,dx < \infty$. Then:
> - (i) $\sum_{k=1}^{\infty} g_k(x)$ converges for all $x \in [a, b]$.
> - (ii) $\sum_{k=1}^{\infty} g_k \in AC([a, b])$.
> - (iii) $\left(\sum_{k=1}^{\infty} g_k(x)\right)' = \sum_{k=1}^{\infty} g_k'(x)$ a.e. on $(a, b)$.

^cor-18-14

> [!proof]+ Proof
> Since $g_k \in AC$, the [[Fundamental Theorem of Calculus for Lebesgue Integrals|FTC]] gives $g_k(x) = g_k(c) + \int_c^x g_k'(t)\,dt$. Therefore:
>
> $$
> \sum_{k=1}^{\infty} g_k(x) = \sum_{k=1}^{\infty} g_k(c) + \int_c^x \sum_{k=1}^{\infty} g_k'(t)\,dt,
> $$
>
> where the interchange of sum and integral is justified as follows.
>
> **(i)** Since $\sum |g_k'| < \infty$ a.e. (by $\sum \int |g_k'| < \infty$ and [[§14a Consequences of the Monotone Convergence Theorem#^thm-14-12|MCT]]), $\sum g_k'$ converges absolutely a.e. By [[Dominated Convergence Theorem|DCT]] (with dominating function $\sum |g_k'| \in L$):
>
> $$
> \lim_{n \to \infty} \int_c^x \sum_{k=1}^{n} g_k'(t)\,dt = \int_c^x \sum_{k=1}^{\infty} g_k'(t)\,dt.
> $$
>
> Since $\sum g_k(c)$ converges, $\sum g_k(x)$ converges for all $x$.
>
> **(ii)** $\sum g_k(x) = \sum g_k(c) + \int_c^x h(t)\,dt$ where $h = \sum g_k' \in L([a, b])$. The integral function of an $L$ function is $AC$ ([[§18c Absolute Continuity#^thm-18-12|integral functions are AC]]), and adding a constant preserves $AC$. So $\sum g_k \in AC$.
>
> **(iii)** Differentiating, the constant $\sum g_k(c)$ drops out and [[§18b Differentiating the Integral#^thm-18-26|differentiation of the integral]] ([[§18b Differentiating the Integral#^thm-18-26|Theorem §18.26]], proved earlier) gives $(\sum g_k)'(x) = \left(\int_c^x h\,dt\right)' = h(x) = \sum g_k'(x)$ a.e.

^pf-18-14

*Uses:* [[Fundamental Theorem of Calculus for Lebesgue Integrals|§18.13]], [[§14a Consequences of the Monotone Convergence Theorem#^thm-14-12|§14.12]], [[§14a Consequences of the Monotone Convergence Theorem#^prop-14-10|§14.10]], [[Dominated Convergence Theorem|§15.8]], [[§18c Absolute Continuity#^thm-18-12|§18.12]], [[§18c Absolute Continuity#^prop-18-11|§18.11]], [[§18b Differentiating the Integral#^thm-18-26|§18.26]]

> [!remark]- Connections
> - The interchange is [[§15a The Dominated Convergence Theorem#^cor-15-9|Absolute Convergence in L¹]] ([[§15a The Dominated Convergence Theorem#^cor-15-9|§15.9]]).
> - MATH 451 counterpart for power series, where uniform convergence does the work: [[§26 Differentiation and Integration of Power Series#^thm-26-4|Term-by-Term Calculus for Power Series]] (451 §26.4).

> [!theorem] Theorem §18.15: Lebesgue Decomposition of Increasing Functions
> Let $f$ be an increasing function on $[a, b]$. Then $f = g + h$, where:
> - (i) $g$ is increasing and absolutely continuous on $[a, b]$,
> - (ii) $h$ is increasing on $[a, b]$ with $h' = 0$ a.e.

^thm-18-15

> [!proof]+ Proof
> By [[Lebesgue's Differentiation Theorem for Monotone Functions|Lebesgue's differentiation theorem]], $f' \geq 0$ a.e. and $f' \in L([a, b])$. Define:
>
> $$
> g(x) = f(a) + \int_a^x f'(t)\,dt, \qquad h(x) = f(x) - g(x).
> $$
>
> $g$ is increasing (since $f' \geq 0$) and $g \in AC$ ([[§18c Absolute Continuity#^thm-18-12|integral of an L function]]). By [[§18b Differentiating the Integral#^thm-18-26|differentiation of the integral]] ([[§18b Differentiating the Integral#^thm-18-26|Theorem §18.26]], proved earlier; applied to $f'$ extended by $0$ outside $[a, b]$), $g' = f'$ a.e.
>
> $h$ is increasing: for $x < y$, $g(y) - g(x) = \int_x^y f' \leq f(y) - f(x)$ (by [[Lebesgue's Differentiation Theorem for Monotone Functions|Lebesgue's integral inequality for increasing functions]]), so $h(y) - h(x) = (f(y) - f(x)) - (g(y) - g(x)) \geq 0$.
>
> $h' = 0$ a.e.: $h' = f' - g' = f' - f' = 0$ a.e.

^pf-18-15

*Uses:* [[Lebesgue's Differentiation Theorem for Monotone Functions|§18.9]], [[§18c Absolute Continuity#^thm-18-12|§18.12]], [[§18b Differentiating the Integral#^thm-18-26|§18.26]]

> [!remark] Remark
> The function $h$ is called the **singular part** of $f$: it is increasing yet gains all its growth on a set of measure zero ($\{h' > 0\}$ has measure zero). The [[§18c Absolute Continuity#^ex-18-4|Cantor function]] is the prototypical example of a purely singular increasing function.

^rem-18-8

> [!theorem] Lemma §18.17: AC on Subintervals
> If $f$ is AC on $[a, b]$ and $[c, d] \subseteq [a, b]$, then $f$ is AC on $[c, d]$.

^lem-18-17

> [!proof]+ Proof
> Any collection of disjoint intervals in $(c, d)$ is also a collection of disjoint intervals in $(a, b)$, so the same $\delta$ from the [[§18c Absolute Continuity#^def-18-4|AC condition]] on $[a, b]$ works on $[c, d]$.

^pf-18-17

*Uses:* [[§18c Absolute Continuity#^def-18-4|Def. §18.4]]

> [!theorem] Lemma §18.18: Image Measure Bounded by Total Variation
> If $f$ is continuous on $[c, d]$, then $f((c, d))$ is an interval and $m(f((c, d))) \leq \bigvee_c^d(f)$.

^lem-18-18

> [!proof]+ Proof
> Since $f$ is continuous, $f((c, d))$ is an interval ([[Intermediate Value Theorem]]) contained in $[f_{\min}, f_{\max}]$, where $f_{\min}$ and $f_{\max}$ are the minimum and maximum of $f$ on $[c, d]$ ([[Extreme Value Theorem]]). So $m(f((c, d))) \leq f_{\max} - f_{\min}$. Let $x_{\min}, x_{\max} \in [c, d]$ be points where $f$ attains its min and max, with $x_{\min} < x_{\max}$ WLOG. The partition $\Delta = \{c, x_{\min}, x_{\max}, d\}$ gives:
>
> $$
> f_{\max} - f_{\min} = |f(x_{\max}) - f(x_{\min})| \leq |f(x_{\min}) - f(c)| + |f(x_{\max}) - f(x_{\min})| + |f(d) - f(x_{\max})| = v_\Delta(f) \leq \bigvee_c^d(f).
> $$
>
> Hence $m(f((c, d))) \leq \bigvee_c^d(f)$.

^pf-18-18

*Uses:* [[Intermediate Value Theorem|451 §18.3]], [[Extreme Value Theorem|451 §18.1]], [[§9 Lebesgue Outer Measure#^prop-9-2|§9.2]], [[§18 Differentiation Theory#^def-18-2|Def. §18.2]]

> [!remark]- Connections
> - The image of $[c,d]$ is exactly $[f_{\min}, f_{\max}]$: [[§18 Properties of Continuous Functions#^cor-18-5|The Image Is a Closed Interval]] (451 §18.5).

> [!theorem] Theorem §18.19: AC Functions Map Null Sets to Null Sets
> If $f \in AC([a, b])$ and $Z \subseteq [a, b]$ with $m(Z) = 0$, then $m(f(Z)) = 0$.

^thm-18-19

> [!proof]+ Proof
> Since $f \in AC([a, b])$, by the [[Fundamental Theorem of Calculus for Lebesgue Integrals|FTC]], $f' \in L([a, b])$ and $f(x) = f(a) + \int_a^x f'(t)\,dt$. By [[§18d The Fundamental Theorem of Calculus for Lebesgue Integrals#^lem-18-17|the first lemma]], $f$ is AC on any $[c, d] \subseteq [a, b]$, so $f(x) = f(c) + \int_c^x f'(t)\,dt$ on $[c, d]$. Applying the total variation formula for integral functions ([[§18 Differentiation Theory#^thm-18-8|§18.8]]) to $f' \in L([c, d])$:
>
> $$
> \bigvee_c^d(f) = \bigvee_c^d\!\left(f(c) + \int_c^x f'(t)\,dt\right) = \bigvee_c^d\!\left(\int_c^x f'(t)\,dt\right) = \int_c^d |f'(t)|\,dt,
> $$
>
> where the first equality holds because a constant does not affect total variation.
>
> Let $\varepsilon > 0$. Since $|f'| \in L([a, b])$, by [[§16 The L¹ Space and Density Theorems#^thm-16-1|absolute continuity of the Lebesgue integral]], there exists $\delta > 0$ such that for any measurable $E \subseteq [a, b]$ with $m(E) < \delta$:
>
> $$
> \int_E |f'(t)|\,dt < \varepsilon.
> $$
>
> Since $m(Z) = 0$, there exist countably many open intervals $\{I_k\}_{k=1}^{\infty}$ with $Z \subseteq \bigcup_{k=1}^{\infty} I_k$ and $\sum_{k=1}^{\infty} m(I_k) < \delta$ ([[§9 Lebesgue Outer Measure#^def-9-4|Def. §9.4]]). Let $G = (\bigcup_{k=1}^{\infty} I_k) \cap (a, b)$. Then $G$ is open in $(a, b)$, $Z \setminus \{a, b\} \subseteq G$, and $m(G) < \delta$. Write $G$ as a [[Open Sets in ℝ are Countable Unions of Disjoint Open Intervals|countable disjoint union of open intervals]]: $G = \bigcup_{k=1}^{\infty} (a_k, b_k)$.
>
> Since $\{a, b\}$ has measure zero, $m(f(\{a, b\})) = 0$ (finitely many points), so it suffices to show $m(f(Z \setminus \{a, b\})) = 0$. By [[§18d The Fundamental Theorem of Calculus for Lebesgue Integrals#^lem-18-18|the second lemma]] and the total variation identity:
>
> $$
> m(f((a_k, b_k))) \leq \bigvee_{a_k}^{b_k}(f) = \int_{a_k}^{b_k} |f'(t)|\,dt.
> $$
>
> Therefore:
>
> $$
> m(f(Z \setminus \{a, b\})) \leq \sum_{k=1}^{\infty} m(f((a_k, b_k))) \leq \sum_{k=1}^{\infty} \int_{a_k}^{b_k} |f'(t)|\,dt = \int_G |f'(t)|\,dt < \varepsilon.
> $$
>
> Since $\varepsilon > 0$ is arbitrary, $m(f(Z)) = 0$.

^pf-18-19

*Uses:* [[Fundamental Theorem of Calculus for Lebesgue Integrals|§18.13]], [[§18d The Fundamental Theorem of Calculus for Lebesgue Integrals#^lem-18-17|§18.17]], [[§18 Differentiation Theory#^thm-18-8|§18.8]], [[§16 The L¹ Space and Density Theorems#^thm-16-1|§16.1]], [[§9 Lebesgue Outer Measure#^def-9-4|Def. §9.4]], [[Open Sets in ℝ are Countable Unions of Disjoint Open Intervals|§7.1]], [[§18d The Fundamental Theorem of Calculus for Lebesgue Integrals#^lem-18-18|§18.18]], [[Properties of Lebesgue Outer Measure|§9.1]], [[§14a Consequences of the Monotone Convergence Theorem#^cor-14-13|§14.13]], [[§9 Lebesgue Outer Measure#^ex-9-1|Ex. §9.1]]

> [!remark] Remark
> This is a strong property of AC functions: they cannot “spread” null sets. The [[§18c Absolute Continuity#^ex-18-4|Cantor function]], by contrast, maps the Cantor set ($m = 0$) onto $[0, 1]$ ($m = 1$) — another illustration of why $BV \cap C \not\subseteq AC$.

^rem-18-10
