---
type: section
subject: "[[Measure Theory]]"
chapter: 5
section: 18
tags: [measure-theory, math551]
---
← [[§17 Invariance Properties and Fubini's Theorem]] · ↑ [[· 5 Differentiation and the FTC]] · [[§19 Normed Linear Spaces and Lᵖ Spaces]] →

## Motivation: The Fundamental Theorem of Calculus

> [!remark] Remark: The Central Question
> Let $f \in L([a, b])$ and define:
>
> $$
> F(x) = \int_a^x f(t)\,dt = \int_{[a,x]} f(t)\,dt, \qquad a \leq x \leq b.
> $$
>
> Is $F$ differentiable, and if so, is $F'(x) = f(x)$ a.e.?
>
> Writing $f = f^+ - f^-$ ([[§12 Measurable Functions#^def-12-4|Def. §12.4]]), we have $F(x) = F_1(x) - F_2(x)$ where $F_1(x) = \int_a^x f^+(t)\,dt$ and $F_2(x) = \int_a^x f^-(t)\,dt$ are both increasing functions. So the question reduces to understanding the differentiability of monotone functions.

^rem-18-1

> [!remark]- Connections
> - For continuous $f$ the answer is the MATH 451 [[Fundamental Theorem of Calculus]] (FTC II, 451 §34.4): $F' = f$ at every point of continuity.
> - Answered in general by [[§18 Differentiation Theory#^thm-18-26|Differentiation of the Integral]] (§18.26).

## Monotone Functions and Continuity

> [!theorem] Theorem §18.1: Monotone Functions Have Countably Many Discontinuities
> Let $f$ be a monotone function on $[a, b]$. Then $f$ is continuous on $[a, b]$ except at countably many points.

^thm-18-1

> [!proof]+ Proof
> WLOG assume $f$ is increasing. At each point $x_0 \in (a, b)$, the [[§20 Limits of Functions#^def-20-2|left and right limits]] exist:
>
> $$
> f(x_0^-) = \lim_{x \to x_0^-} f(x), \qquad f(x_0^+) = \lim_{x \to x_0^+} f(x),
> $$
>
> and $f(x_0^-) \leq f(x_0) \leq f(x_0^+)$. The function $f$ is discontinuous at $x_0$ if and only if $f(x_0^-) \neq f(x_0^+)$ ([[§20 Limits of Functions#^thm-20-2|451 §20.2]]), i.e., the “jump” $J(x_0) = f(x_0^+) - f(x_0^-)$ is positive.
>
> For each $n \in \mathbb{N}$, define $D_n = \{x \in (a, b) : J(x) > 1/n\}$. If $x_1 < x_2 < \cdots < x_k$ are points in $D_n$, then the jumps are disjoint in the range of $f$:
>
> $$
> \sum_{i=1}^{k} J(x_i) \leq f(b) - f(a).
> $$
>
> Since each $J(x_i) > 1/n$, we get $k < n(f(b) - f(a))$. So $D_n$ is finite. The set of all discontinuities in $(a, b)$ is $D = \bigcup_{n=1}^{\infty} D_n$, a [[Countable Union of Countable Sets is Countable|countable union of finite sets, hence countable]]. Adding the endpoints $a$ and $b$ (where $f$ may also be discontinuous) changes this by at most two points.

^pf-18-1

*Uses:* [[§20 Limits of Functions#^def-20-2|451 Def. §20.2]], [[§20 Limits of Functions#^thm-20-2|451 §20.2]], [[Countable Union of Countable Sets is Countable|§3.1]]

![[m551-18-2.svg]]
*An increasing $f$ with jumps at $x_1, x_2, x_3$ (hollow dots: one-sided limits; filled dots: the values of $f$). Each jump $J(x_i) = f(x_i^+) - f(x_i^-)$ occupies its own interval on the vertical axis (red). Because $f$ is increasing these intervals are disjoint and lie inside $[f(a), f(b)]$, so the jumps add up to at most $f(b) - f(a)$ and only finitely many can exceed $\frac1n$.*

> [!remark]- Connections
> - MATH 451 states this fact without proof alongside [[§33 Properties of the Riemann Integral#^thm-33-1|Monotonic Functions Are Integrable]] (451 §33.1).
> - Monotone functions are also [[§12 Measurable Functions#^ex-12-1|measurable]] (Ex. §12.1).

## Vitali Covering

> [!definition] Definition §18.1: Vitali Covering
> Let $E \subseteq \mathbb{R}$ and let $\Gamma = \{I_\alpha\}_{\alpha \in \mathcal{J}}$ be a collection of closed intervals of positive length ($|I_\alpha| > 0$). We say $\Gamma$ is a **Vitali covering** of $E$ if for every $x \in E$ and every $\varepsilon > 0$, there exists $I \in \Gamma$ such that $|I| < \varepsilon$ and $x \in I$.

^def-18-1

> [!example] Example §18.1: A Vitali Covering
> $\Gamma = \{[r - 1/m, r + 1/m] \cap [0,1] : r \in \mathbb{Q} \cap [0,1],\; m \in \mathbb{N}\}$ is a Vitali covering of $[0, 1]$: for any $x \in [0,1]$ and $\varepsilon > 0$, choose $r \in \mathbb{Q}$ close to $x$ and $m$ large enough.

^ex-18-1

> [!remark] Remark: Notation
> For a closed interval $I \subseteq \mathbb{R}$, let $\hat{I}$ denote the interval concentric with $I$ and with $|\hat{I}| = 5|I|$ (i.e., scaled by factor $5$ about the center).

^rem-18-2

> [!theorem] Theorem §18.2: Vitali Covering Theorem
> Let $E \subseteq \mathbb{R}$ with $m^*(E) < \infty$. Assume $\Gamma$ is a Vitali covering of $E$. Then for every $\varepsilon > 0$, there exist finitely many mutually disjoint intervals $I_1, I_2, \ldots, I_n \in \Gamma$ such that:
>
> $$
> m^*\!\left(E \setminus \bigcup_{j=1}^{n} I_j\right) < \varepsilon.
> $$

^thm-18-2

> [!proof]+ Proof
> Since $m^*(E) < \infty$, there exists an open set $G \supseteq E$ with $m(G) < \infty$ ([[§9 Lebesgue Outer Measure#^def-9-4|Def. §9.4]]). WLOG assume every $I \in \Gamma$ satisfies $I \subseteq G$ and $I$ is closed (if not, replace $\Gamma$ by $\{I \in \Gamma : I \subseteq G\}$, which is still a Vitali covering since $G$ is open).
>
> **Step 1.** Since every $I \in \Gamma$ satisfies $I \subseteq G$, we have $m(I) = |I| \leq m(G) < \infty$ ([[§9 Lebesgue Outer Measure#^prop-9-2|§9.2]]). Let $\delta_0 = \sup\{|I| : I \in \Gamma\}$. Take $I_1 \in \Gamma$ with $|I_1| > \frac{1}{2}\delta_0$.
>
> **Step 2 (Inductive selection).** Suppose we have chosen $I_1, \ldots, I_n$ mutually disjoint, $I_j \in \Gamma$. Define:
>
> $$
> \delta_n = \sup\left\{|I| \;\middle|\; I \in \Gamma,\; I \cap I_j = \emptyset \;\forall\, 1 \leq j \leq n\right\}.
> $$
>
> Take $I_{n+1} \in \Gamma$ with $I_{n+1} \cap I_j = \emptyset$ for $1 \leq j \leq n$ and $|I_{n+1}| > \frac{1}{2}\delta_n$.
>
> **Case 1:** There exists $n$ such that $E \subseteq \bigcup_{j=1}^{n} I_j$. Then $m^{\ast}(E \setminus \bigcup_{j=1}^{n} I_j) = 0 < \varepsilon$, done.
>
> **Case 2:** $E \not\subseteq \bigcup_{j=1}^{n} I_j$ for all $n$. We obtain an infinite sequence $\{I_j\}_{j=1}^{\infty}$ of mutually disjoint intervals in $\Gamma$ with $\bigcup_{j=1}^{\infty} I_j \subseteq G$. Since the $I_j$ are disjoint ([[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]]):
>
> $$
> m\!\left(\bigcup_{j=1}^{\infty} I_j\right) = \sum_{j=1}^{\infty} |I_j| \leq m(G) < \infty.
> $$
>
> In particular, $\sum_{j=1}^{\infty} |I_j| < \infty$, so for any $\varepsilon > 0$, there exists $n_0$ such that $\sum_{j=n_0+1}^{\infty} |I_j| < \varepsilon/5$.
>
> **Claim:** $E \setminus \bigcup_{j=1}^{n_0} I_j \subseteq \bigcup_{j=n_0+1}^{\infty} \hat{I}_j$.
>
> *Proof of claim*: Let $x_0 \in E \setminus \bigcup_{j=1}^{n_0} I_j$. Since each $I_j$ is closed, $\operatorname{dist}(x_0, \bigcup_{j=1}^{n_0} I_j) > 0$. Since $\Gamma$ is a Vitali covering, there exists $J \in \Gamma$ with $x_0 \in J$, $|J| > 0$, and $J \cap I_j = \emptyset$ for $1 \leq j \leq n_0$.
>
> Since $\sum |I_j| < \infty$ and $|I_n| > \frac{1}{2}\delta_{n-1}$, we have $\delta_n \to 0$. So there exists $k > n_0$ such that $|J| > \delta_k$ (otherwise $|J| \leq \delta_n$ for all $n > n_0$, giving $|J| = 0$, contradiction).
>
> Let $m$ be the smallest index $\geq n_0 + 1$ such that $J \cap I_m \neq \emptyset$ (such $m$ exists because $|J| > \delta_k$ implies $J$ must intersect some $I_m$ with $n_0 < m \leq k$, by the maximality of $\delta_{m-1}$). Then $|J| \leq \delta_{m-1} < 2|I_m|$ (by the selection rule $|I_m| > \frac{1}{2}\delta_{m-1}$).
>
> Since $J \cap I_m \neq \emptyset$ and $|J| < 2|I_m|$, the interval $J$ is contained in $\hat{I}_m$ (the interval concentric with $I_m$ scaled by factor $5$). In particular, $x_0 \in J \subseteq \hat{I}_m \subseteq \bigcup_{j=n_0+1}^{\infty} \hat{I}_j$.
>
> **Conclusion:**
>
> $$
> m^*\!\left(E \setminus \bigcup_{j=1}^{n_0} I_j\right) \leq m^*\!\left(\bigcup_{j=n_0+1}^{\infty} \hat{I}_j\right) \leq \sum_{j=n_0+1}^{\infty} |\hat{I}_j| = 5 \sum_{j=n_0+1}^{\infty} |I_j| < 5 \cdot \frac{\varepsilon}{5} = \varepsilon.
> $$

^pf-18-2

*Uses:* [[§9 Lebesgue Outer Measure#^def-9-4|Def. §9.4]], [[§18 Differentiation Theory#^def-18-1|Def. §18.1]], [[§9 Lebesgue Outer Measure#^prop-9-2|§9.2]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]], [[Properties of Lebesgue Outer Measure|§9.1]]

![[m551-18-1.svg]]
*The Vitali covering argument. (a) The set $E$ (black) and a Vitali covering $\Gamma$ (blue; a genuine one has arbitrarily short intervals around every point of $E$). (b) Greedy selection: each new interval is disjoint from the earlier ones and longer than half of any remaining candidate, giving $I_1, I_2, I_3$. A point $x_0 \in E$ not covered by $I_1$ (take $n_0 = 1$) lies in some $J \in \Gamma$ (red, dashed) disjoint from $I_1$; here $J$ first meets $I_2$. (c) The selection rule gives $|J| \leq \delta_1 < 2|I_2|$, and an interval that meets $I_2$ and is shorter than $2|I_2|$ lies inside the $5\times$ dilation $\hat I_2$ (shaded). So the dilations $\hat I_j$, $j > n_0$, cover everything that $I_1, \dots, I_{n_0}$ miss, at total cost $5\sum_{j > n_0} |I_j|$.*

> [!remark]- Connections
> - Used twice in [[Lebesgue's Differentiation Theorem for Monotone Functions|Lebesgue's Differentiation Theorem]] (§18.9) and once in [[§18 Differentiation Theory#^thm-18-27|Theorem §18.27]] (non-constant functions with zero derivative).
> - Compare the compactness arguments of [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|Heine–Borel]] (§6.4): there a finite subcover, here finitely many *disjoint* intervals covering all but a small set.

## Functions of Bounded Variation

> [!definition] Definition §18.2: Total Variation and Bounded Variation
> Let $f$ be a real-valued function on $[a, b]$. For a partition $\Delta: a = x_0 < x_1 < \cdots < x_n = b$, define:
>
> $$
> v_\Delta = \sum_{j=0}^{n-1} |f(x_{j+1}) - f(x_j)|.
> $$
>
> The **total variation** of $f$ on $[a, b]$ is:
>
> $$
> \bigvee_a^b(f) = \sup\{v_\Delta : \Delta \text{ a partition of } [a, b]\}.
> $$
>
> If $\bigvee_a^b(f) < \infty$, we say $f$ is of **bounded variation** on $[a, b]$, and write $f \in BV([a, b])$.

^def-18-2

> [!remark]- Connections
> - Partitions as in the Riemann integral: [[§8 Motivation꞉ The Riemann Integral#^def-8-1|Def. §8.1]], [[§32 The Definition of the Riemann Integral#^def-32-1|451 Def. §32.1]].

> [!example] Example §18.2: Monotone Functions are BV
> If $f$ is increasing on $[a, b]$, then for any partition:
>
> $$
> v_\Delta = \sum_{j=0}^{n-1} |f(x_{j+1}) - f(x_j)| = \sum_{j=0}^{n-1} (f(x_{j+1}) - f(x_j)) = f(b) - f(a) \geq 0.
> $$
>
> So $\bigvee_a^b(f) = f(b) - f(a) < \infty$. Similarly for decreasing functions.

^ex-18-2

> [!theorem] Proposition §18.3: Differentiable Functions with Bounded Derivative are BV
> If $f$ is differentiable on $[a, b]$ with $|f'(x)| \leq M$ for all $x \in [a, b]$, then $f \in BV([a, b])$.

^prop-18-3

> [!proof]+ Proof
> By the [[Mean Value Theorem]], $|f(x_{j+1}) - f(x_j)| = |f'(\theta_j)|(x_{j+1} - x_j) \leq M(x_{j+1} - x_j)$. So:
>
> $$
> v_\Delta = \sum_{j=0}^{n-1} |f(x_{j+1}) - f(x_j)| \leq M \sum_{j=0}^{n-1} (x_{j+1} - x_j) = M(b - a).
> $$
>
> Hence $\bigvee_a^b(f) \leq M(b - a) < \infty$.

^pf-18-3

*Uses:* [[Mean Value Theorem|451 §29.3]], [[§18 Differentiation Theory#^def-18-2|Def. §18.2]]

> [!remark]- Connections
> - The same MVT estimate gives [[§29 The Mean Value Theorem#^prop-29-8|the Mean Value Inequality]] (451 §29.8) and [[§19 Uniform Continuity#^thm-19-5|Bounded Derivative Implies Uniform Continuity]] (451 §19.5); in the language below, $f$ is Lipschitz, hence [[§18 Differentiation Theory#^prop-18-11|AC]] (§18.11).

> [!example] Example §18.3: A Continuous Function Not in BV
> Define $f(x) = \sqrt{x}\sin(\pi/x)$ for $0 < x \leq 1$ and $f(0) = 0$. Then $f$ is continuous on $[0, 1]$ but $f \notin BV([0, 1])$: the oscillations near $0$ accumulate enough variation to make $\bigvee_0^1(f) = \infty$.

^ex-18-3

![[m551-18-3.svg]]
*$f(x) = \sqrt{x}\,\sin(\pi/x)$ (blue) oscillates between $\pm\sqrt{x}$ (dashed). At $x_k = \frac{2}{2k+1}$ it touches the envelope, alternately from above and below, so a partition through these points (red polygon) has $v_\Delta \geq \sum_k \sqrt{x_k}$, a series comparable to $\sum_k k^{-1/2}$, which diverges. The amplitude $\sqrt{x} \to 0$ makes $f$ continuous at $0$, but not fast enough to keep the variation finite.*

> [!remark]- Connections
> - Another rung of the MATH 451 ladder of damped oscillations: [[sin(1∕x) family]].

> [!theorem] Proposition §18.4: Properties of BV Functions
> - (i) If $f \in BV([a, b])$, then $f$ is bounded on $[a, b]$.
> - (ii) If $f, g \in BV([a, b])$ and $c_1, c_2 \in \mathbb{R}$, then $c_1 f + c_2 g \in BV([a, b])$, with:
>
> $$
> \bigvee_a^b(cf) = |c|\,\bigvee_a^b(f), \qquad \bigvee_a^b(f + g) \leq \bigvee_a^b(f) + \bigvee_a^b(g).
> $$

^prop-18-4

> [!proof]+ Proof
> **(i)** For any $x \in (a, b]$, the partition $\Delta: a < x < b$ gives:
>
> $$
> |f(x) - f(a)| \leq |f(x) - f(a)| + |f(b) - f(x)| = v_\Delta(f) \leq \bigvee_a^b(f) < \infty.
> $$
>
> So $|f(x)| \leq |f(a)| + \bigvee_a^b(f) < \infty$ for all $x \in [a, b]$.
>
> **(ii)** The scaling identity $\bigvee_a^b(cf) = |c|\,\bigvee_a^b(f)$ is immediate. For the triangle inequality, let $\Delta$ be any partition:
>
> $$
> v_\Delta(f + g) = \sum_{i=0}^{n-1} |(f + g)(x_{i+1}) - (f + g)(x_i)| \leq \sum_{i=0}^{n-1} |f(x_{i+1}) - f(x_i)| + \sum_{i=0}^{n-1} |g(x_{i+1}) - g(x_i)| = v_\Delta(f) + v_\Delta(g).
> $$
>
> Taking the supremum over $\Delta$: $\bigvee_a^b(f + g) \leq \bigvee_a^b(f) + \bigvee_a^b(g) < \infty$.

^pf-18-4

*Uses:* [[§18 Differentiation Theory#^def-18-2|Def. §18.2]]

> [!theorem] Proposition §18.5: Additivity of Total Variation
> Let $f \in BV([a, b])$ and $a < c < b$. Then:
>
> $$
> \bigvee_a^b(f) = \bigvee_a^c(f) + \bigvee_c^b(f).
> $$

^prop-18-5

> [!proof]+ Proof
> **($\geq$):** For any $\varepsilon > 0$, choose a partition $\Delta_1$ of $[a, c]$ with $v_{\Delta_1}(f) > \bigvee_a^c(f) - \varepsilon$, and a partition $\Delta_2$ of $[c, b]$ with $v_{\Delta_2}(f) > \bigvee_c^b(f) - \varepsilon$. Then $\Delta = \Delta_1 \cup \Delta_2$ is a partition of $[a, b]$ with:
>
> $$
> v_\Delta(f) = v_{\Delta_1}(f) + v_{\Delta_2}(f) > \bigvee_a^c(f) + \bigvee_c^b(f) - 2\varepsilon.
> $$
>
> Since $v_\Delta(f) \leq \bigvee_a^b(f)$, letting $\varepsilon \to 0$ gives $\bigvee_a^b(f) \geq \bigvee_a^c(f) + \bigvee_c^b(f)$.
>
> **($\leq$):** For any $\varepsilon > 0$, choose a partition $\Delta: a = x_0 < x_1 < \cdots < x_n = b$ with $v_\Delta(f) > \bigvee_a^b(f) - \varepsilon$. Let $\Delta' = \Delta \cup \{c\}$ (refine by adding $c$). Observe that $v_{\Delta'}(f) \geq v_\Delta(f)$ (refining a partition can only increase the variation, since $|f(x_{i+1}) - f(x_i)| \leq |f(x_{i+1}) - f(c)| + |f(c) - f(x_i)|$ by the triangle inequality).
>
> The partition $\Delta'$ splits into $\Delta_1$ (the points $\leq c$) and $\Delta_2$ (the points $\geq c$):
>
> $$
> v_{\Delta'}(f) = v_{\Delta_1}(f) + v_{\Delta_2}(f) \leq \bigvee_a^c(f) + \bigvee_c^b(f).
> $$
>
> So $\bigvee_a^b(f) - \varepsilon < v_\Delta(f) \leq v_{\Delta'}(f) \leq \bigvee_a^c(f) + \bigvee_c^b(f)$. Letting $\varepsilon \to 0$ gives $\bigvee_a^b(f) \leq \bigvee_a^c(f) + \bigvee_c^b(f)$.

^pf-18-5

*Uses:* [[§18 Differentiation Theory#^def-18-2|Def. §18.2]]

> [!remark]- Connections
> - The refinement step mirrors the MATH 451 [[§32 The Definition of the Riemann Integral#^lem-32-2|Refinement Lemma]] (451 §32.2) for upper and lower sums.

> [!theorem] Corollary §18.6: The Variation Function is Increasing
> If $f \in BV([a,b])$, then the function $T(x) = \bigvee_a^x(f)$ is increasing on $[a, b]$.

^cor-18-6

> [!proof]+ Proof
> For $a \leq x_1 < x_2 \leq b$, by [[§18 Differentiation Theory#^prop-18-5|additivity]]: $\bigvee_a^{x_2}(f) = \bigvee_a^{x_1}(f) + \bigvee_{x_1}^{x_2}(f) \geq \bigvee_a^{x_1}(f)$.

^pf-18-6

*Uses:* [[§18 Differentiation Theory#^prop-18-5|§18.5]]

> [!theorem] Theorem §18.7: Jordan Decomposition Theorem
> Let $f \in BV([a, b])$. Then there exist increasing functions $g, h$ on $[a, b]$ such that $f(x) = g(x) - h(x)$ for all $x \in [a, b]$.
>
> Conversely, $f \in BV([a, b])$ if and only if $f$ is the difference of two increasing functions.

^thm-18-7

> [!proof]+ Proof
> **($\Rightarrow$)** Let $g(x) = \bigvee_a^x(f)$ and $h(x) = \bigvee_a^x(f) - f(x)$. Then $g$ is increasing (by [[§18 Differentiation Theory#^cor-18-6|the corollary above]]). We show $h$ is increasing: for $a \leq x_1 < x_2 \leq b$,
>
> $$
> \begin{aligned}
> h(x_2) - h(x_1) &= \bigvee_a^{x_2}(f) - f(x_2) - \bigvee_a^{x_1}(f) + f(x_1) = \bigvee_{x_1}^{x_2}(f) - (f(x_2) - f(x_1)).
> \end{aligned}
> $$
>
> Since the partition $\Delta: x_1 < x_2$ gives $|f(x_2) - f(x_1)| \leq \bigvee_{x_1}^{x_2}(f)$, we have $f(x_2) - f(x_1) \leq |f(x_2) - f(x_1)| \leq \bigvee_{x_1}^{x_2}(f)$. Hence $h(x_2) - h(x_1) \geq 0$, so $h$ is increasing.
>
> Since $f(x) = g(x) - h(x)$ with $g, h$ increasing, the decomposition is established.
>
> **($\Leftarrow$)** If $f = g - h$ with $g, h$ increasing, then $\bigvee_a^b(f) \leq \bigvee_a^b(g) + \bigvee_a^b(h) = (g(b) - g(a)) + (h(b) - h(a)) < \infty$.

^pf-18-7

*Uses:* [[§18 Differentiation Theory#^cor-18-6|§18.6]], [[§18 Differentiation Theory#^prop-18-5|§18.5]], [[§18 Differentiation Theory#^prop-18-4|§18.4]], [[§18 Differentiation Theory#^ex-18-2|Ex. §18.2]]

![[m551-18-4.svg]]
*The Jordan decomposition of $f(x) = \sin 2\pi x$ on $[0,1]$ (black). The variation function $g(x) = \bigvee_0^x(f)$ (blue) increases by $|f'|$: it rises with $f$ on $[0, \frac14]$, keeps rising while $f$ falls on $[\frac14, \frac34]$, and ends at $\bigvee_0^1(f) = 4$. The difference $h = g - f$ (red) is flat where $f$ increases and climbs at twice the rate at which $f$ falls; both $g$ and $h$ are increasing, and $f = g - h$.*

> [!theorem] Theorem §18.8: Total Variation of the Integral Function
> Let $f \in L([a, b])$ and define $F(x) = \int_a^x f(t)\,dt$ for $x \in [a, b]$. Then $F \in BV([a, b])$ and:
>
> $$
> \bigvee_a^b(F) = \int_a^b |f(t)|\,dt.
> $$

^thm-18-8

> [!proof]+ Proof
> **Upper bound ($\bigvee_a^b(F) \leq \int_a^b |f|\,dt$):** For any partition $\Delta: a = x_0 < x_1 < \cdots < x_n = b$:
>
> $$
> v_\Delta(F) = \sum_{i=0}^{n-1} |F(x_{i+1}) - F(x_i)| = \sum_{i=0}^{n-1} \left|\int_{x_i}^{x_{i+1}} f(t)\,dt\right| \leq \sum_{i=0}^{n-1} \int_{x_i}^{x_{i+1}} |f(t)|\,dt = \int_a^b |f(t)|\,dt.
> $$
>
> Taking the supremum: $\bigvee_a^b(F) \leq \int_a^b |f(t)|\,dt < \infty$, so $F \in BV$.
>
> **Lower bound ($\bigvee_a^b(F) \geq \int_a^b |f|\,dt$):**
>
> *Step 1: Step functions.* Assume $f(x) = \sum_{i=0}^{n-1} c_i\,\chi_{[x_i, x_{i+1})}$ is a [[§15 The General Lebesgue Integral#^def-15-2|step function]] on the partition $\Delta: a = x_0 < \cdots < x_n = b$. Then:
>
> $$
> v_\Delta(F) = \sum_{i=0}^{n-1} |F(x_{i+1}) - F(x_i)| = \sum_{i=0}^{n-1} \left|\int_{x_i}^{x_{i+1}} c_i\,dt\right| = \sum_{i=0}^{n-1} |c_i|(x_{i+1} - x_i) = \int_a^b |f(t)|\,dt.
> $$
>
> So $\bigvee_a^b(F) \geq v_\Delta(F) = \int_a^b |f|\,dt$.
>
> *Step 2: General $f \in L([a,b])$.* For any $\varepsilon > 0$, by [[§16 The L¹ Space and Density Theorems#^thm-16-6|density of step functions in L¹]], there exists a step function $h$ with $\int_a^b |f(t) - h(t)|\,dt < \varepsilon$. Let $H(x) = \int_a^x h(t)\,dt$. By Step 1, $\bigvee_a^b(H) \geq \int_a^b |h|\,dt$.
>
> By the [[§18 Differentiation Theory#^prop-18-4|triangle inequality for total variation]] and the upper bound:
>
> $$
> \int_a^b |f|\,dt \leq \int_a^b |f - h|\,dt + \int_a^b |h|\,dt < \varepsilon + \bigvee_a^b(H) \leq \varepsilon + \bigvee_a^b(F) + \bigvee_a^b(H - F).
> $$
>
> Since $H(x) - F(x) = \int_a^x (h(t) - f(t))\,dt$, the upper bound gives $\bigvee_a^b(H - F) \leq \int_a^b |h - f|\,dt < \varepsilon$. Hence:
>
> $$
> \int_a^b |f|\,dt < \varepsilon + \bigvee_a^b(F) + \varepsilon = \bigvee_a^b(F) + 2\varepsilon.
> $$
>
> Letting $\varepsilon \to 0$: $\int_a^b |f|\,dt \leq \bigvee_a^b(F)$.

^pf-18-8

*Uses:* [[§18 Differentiation Theory#^def-18-2|Def. §18.2]], [[§15 The General Lebesgue Integral#^thm-15-4|§15.4]], [[§15 The General Lebesgue Integral#^def-15-2|Def. §15.2]], [[§16 The L¹ Space and Density Theorems#^thm-16-6|§16.6]], [[§18 Differentiation Theory#^prop-18-4|§18.4]], [[§15 The General Lebesgue Integral#^prop-15-3|§15.3]]

## Dini Derivatives

> [!definition] Definition §18.3: Dini Derivatives
> Let $f$ be a real-valued function on $[a, b]$ and $x_0 \in (a, b)$. The four **Dini derivatives** of $f$ at $x_0$ are:
>
> $$
> \begin{aligned}
> D^+ f(x_0) &= \limsup_{h \to 0^+} \frac{f(x_0 + h) - f(x_0)}{h}, &\quad D_+ f(x_0) &= \liminf_{h \to 0^+} \frac{f(x_0 + h) - f(x_0)}{h}, \\[4pt]
> D^- f(x_0) &= \limsup_{h \to 0^+} \frac{f(x_0) - f(x_0 - h)}{h}, &\quad D_- f(x_0) &= \liminf_{h \to 0^+} \frac{f(x_0) - f(x_0 - h)}{h}.
> \end{aligned}
> $$

^def-18-3

> [!remark] Remark: Relationship to Differentiability
> By definition, $D^+ \geq D_+$ and $D^- \geq D_-$ always hold. If $D^+ f(x_0) \leq D_- f(x_0)$ and $D^- f(x_0) \leq D_+ f(x_0)$, then all four Dini derivatives are sandwiched:
>
> $$
> D_+ \leq D^+ \leq D_- \leq D^- \leq D_+,
> $$
>
> which forces $D^+ = D_+ = D^- = D_-$, i.e., $f$ is differentiable at $x_0$ in the extended sense (the common value may be $\pm\infty$; $f'(x_0)$ is a real number when it is finite).
>
> Equivalently: $f$ is *not* differentiable at $x_0$ iff $D^+ > D_-$ or $D^- > D_+$ at $x_0$. In other words, some upper Dini derivative strictly exceeds the corresponding lower one.

^rem-18-3

![[m551-18-5.svg]]
*An example of different Dini derivatives: $f(x) = x\sin(1/x)$ for $x > 0$ and $f(x) = 0$ for $x \leq 0$, at $x_0 = 0$. The right difference quotient $\frac{f(h) - f(0)}{h} = \sin(1/h)$ is the slope of the red secant, and as $h \to 0^+$ it sweeps through all of $[-1, 1]$, so $D^+f(0) = 1$ and $D_+f(0) = -1$ (dashed lines). From the left the quotient is $0$, so $D^-f(0) = D_-f(0) = 0$. Since $D^+f(0) = 1 > 0 = D_-f(0)$, $f$ is not differentiable at $0$.*

> [!remark]- Connections
> - One-sided derivatives in MATH 451: the one-sided limits of [[§20 Limits of Functions#^def-20-2|451 Def. §20.2]] applied to the difference quotient; limsup/liminf as in [[§12 Measurable Functions#^rem-12-4|Remark: Recalling Limsup and Liminf]].

## Lebesgue's Theorem on Differentiability of Monotone Functions

> [!theorem] Theorem §18.9: Lebesgue's Differentiation Theorem for Monotone Functions
> Let $f$ be a monotone increasing function on $[a, b]$. Then:
> - (i) $f$ is differentiable a.e. on $(a, b)$.
> - (ii) $f' \geq 0$ a.e., and $f' \in L([a, b])$ (i.e., $f'$ is integrable).
> - (iii) $\displaystyle\int_a^b f'(x)\,dx \leq f(b) - f(a)$.

^thm-18-9

> [!remark] Remark
> The inequality in (iii) can be strict: for the [[§18 Differentiation Theory#^ex-18-4|Cantor function]] (“devil's staircase”), $f$ is increasing and continuous on $[0,1]$ with $f(0) = 0$, $f(1) = 1$, but $f' = 0$ a.e., so $\int_0^1 f'\,dx = 0 < 1 = f(1) - f(0)$. A similar statement holds for decreasing functions.

^rem-18-4

> [!proof]+ Proof of (i): A.E. Differentiability
> Let $f$ be increasing on $[a, b]$. Define the “bad” sets:
>
> $$
> \begin{aligned}
> E_1 &= \{x \in (a, b) : D^+ f(x) > D_- f(x)\}, \\
> E_2 &= \{x \in (a, b) : D^- f(x) > D_+ f(x)\}.
> \end{aligned}
> $$
>
> We show $m(E_1) = m(E_2) = 0$. If $x_0 \in (a, b) \setminus (E_1 \cup E_2)$, then $D^+ f(x_0) \leq D_- f(x_0)$ and $D^- f(x_0) \leq D_+ f(x_0)$, which forces all four Dini derivatives to be equal (as argued in [[§18 Differentiation Theory#^rem-18-3|the remark above]]), so $f$ is differentiable at $x_0$ in the extended sense; that the common value is finite a.e. follows from (ii).
>
> **Showing $m(E_1) = 0$.** Write $E_1$ as a countable union:
>
> $$
> E_1 = \bigcup_{\substack{r, s \in \mathbb{Q} \\ r > s}} A_{r,s}, \qquad A_{r,s} = \{x \in (a, b) : D^+ f(x) > r > s > D_- f(x)\}.
> $$
>
> It suffices to show $m(A_{r,s}) = 0$ for each fixed $r > s$ rational.
>
> Fix $r, s \in \mathbb{Q}$ with $r > s$. Let $A = A_{r,s}$. Suppose for contradiction that $m^*(A) > 0$.
>
> **Step 1: Apply Vitali to the $D_-$ condition.**
>
> For any $\varepsilon > 0$, choose an open set $G \supseteq A$ with $m(G) < (1 + \varepsilon)\,m^*(A)$. Since $D_- f(x) < s$ for all $x \in A$, for each $x_0 \in A$ there exist arbitrarily small $h_j > 0$ such that:
>
> $$
> \frac{f(x_0) - f(x_0 - h_j)}{h_j} < s, \quad \text{i.e.,} \quad f(x_0) - f(x_0 - h_j) < s\,h_j.
> $$
>
> The collection $\Gamma = \{[x_0 - h_j, x_0] : x_0 \in A,\; [x_0 - h_j, x_0] \subseteq G,\; h_j > 0\}$ is a [[§18 Differentiation Theory#^def-18-1|Vitali covering]] of $A$. By the [[Vitali Covering Theorem|Vitali Covering Theorem]], there exist finitely many disjoint intervals $J_1 = [y_1, y_1 + h_1'], \ldots, J_p = [y_p, y_p + h_p']$ in $\Gamma$ with:
>
> $$
> m^*\!\left(A \setminus \bigcup_{j=1}^{p} J_j\right) < \varepsilon.
> $$
>
> Let $B = A \cap \bigcup_{j=1}^{p} J_j$, so $m^*(B) \geq m^*(A) - \varepsilon$.
>
> Each $J_j$ has endpoint $y_j + h_j' \in A$ and satisfies $f(y_j + h_j') - f(y_j) < s\,h_j'$. Therefore:
>
> $$
> \sum_{j=1}^{p} \bigl(f(y_j + h_j') - f(y_j)\bigr) < s \sum_{j=1}^{p} h_j' = s \sum_{j=1}^{p} |J_j|.  \tag{*}
> $$
>
> **Step 2: Apply Vitali to the $D^+$ condition.**
>
> Remove from $B$ the right endpoints of $J_1, \ldots, J_p$ (finitely many points, a null set, so $m^*(B)$ is unchanged). For each remaining $x \in B$, $x$ lies in some $J_j$ but is not its right endpoint, and $D^+ f(x) > r$. So there exist arbitrarily small $h > 0$ with $[x, x+h] \subseteq \bigcup_{j=1}^{p} J_j$ and:
>
> $$
> \frac{f(x + h) - f(x)}{h} > r.
> $$
>
> The collection $\Gamma_1 = \{[x, x+h] : x \in B,\; [x,x+h] \subseteq \bigcup_{j=1}^p J_j,\; h > 0,\; f(x+h)-f(x) > rh\}$ is a Vitali covering of $B$. By Vitali, there exist disjoint $I_1 = [x_1, x_1 + k_1], \ldots, I_q = [x_q, x_q + k_q]$ in $\Gamma_1$ with $m^*(B \setminus \bigcup I_i) < \varepsilon$. Each satisfies $f(x_i + k_i) - f(x_i) > r\,k_i$, so:
>
> $$
> \sum_{i=1}^{q} r\,k_i < \sum_{i=1}^{q} \bigl(f(x_i + k_i) - f(x_i)\bigr).  \tag{**}
> $$
>
> **Step 3: Compare the two bounds.**
>
> Since each $I_i \subseteq \bigcup_j J_j$ and the $\{J_j\}$ are disjoint, the intervals $\{I_i\}$ that fall inside a given $J_j$ are disjoint subintervals of $J_j$. By monotonicity of $f$, the sum of $f(x_i + k_i) - f(x_i)$ over those $I_i \subseteq J_j$ is at most $f(y_j + h_j') - f(y_j)$ (telescoping within $J_j$). Therefore:
>
> $$
> \sum_{i=1}^{q} \bigl(f(x_i + k_i) - f(x_i)\bigr) \leq \sum_{j=1}^{p} \bigl(f(y_j + h_j') - f(y_j)\bigr).
> $$
>
> Combining ($*$) and ($**$):
>
> $$
> r \sum_{i=1}^{q} k_i < \sum_{j=1}^{p} \bigl(f(y_j + h_j') - f(y_j)\bigr) < s \sum_{j=1}^{p} h_j'.
> $$
>
> Now $\sum k_i = m(\bigcup I_i)$ and $\sum h_j' = m(\bigcup J_j) \leq m(G) < (1+\varepsilon)\,m^*(A)$. Also $m^*(B) \geq m^*(A) - \varepsilon$ and $m^*(B \setminus \bigcup I_i) < \varepsilon$, so $\sum k_i \geq m^*(B) - \varepsilon \geq m^*(A) - 2\varepsilon$.
>
> Therefore:
>
> $$
> r\,(m^*(A) - 2\varepsilon) \leq r \sum k_i < s(1 + \varepsilon)\,m^*(A).
> $$
>
> Letting $\varepsilon \to 0$: $r\,m^*(A) \leq s\,m^*(A)$. Since $r > s$, this gives $m^*(A) \leq 0$, contradicting $m^*(A) > 0$.
>
> Hence $m(A_{r,s}) = 0$ for all $r > s$, so $m(E_1) = 0$. The proof that $m(E_2) = 0$ is similar (swap the roles of left and right).

^pf-18-9

*Uses:* [[§18 Differentiation Theory#^def-18-3|Def. §18.3]], [[§3 Countability of Rationals and Unions#^cor-3-2|§3.2]], [[§9 Lebesgue Outer Measure#^def-9-4|Def. §9.4]], [[§18 Differentiation Theory#^def-18-1|Def. §18.1]], [[Vitali Covering Theorem|§18.2]], [[Properties of Lebesgue Outer Measure|§9.1]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]]

> [!proof]+ Proof of (iii): The Integral Inequality
> Extend $f$ by setting $f(x) = f(b)$ for $x > b$. Define the difference quotients:
>
> $$
> f_n(x) = \frac{f(x + 1/n) - f(x)}{1/n} = n\!\left(f\!\left(x + \tfrac{1}{n}\right) - f(x)\right).
> $$
>
> Since $f$ is differentiable a.e. (by (i)), $\lim_{n \to \infty} f_n(x) = f'(x)$ for a.e. $x \in (a, b)$. Since $f$ is increasing, $f_n(x) \geq 0$ for all $x \in [a, b]$.
>
> By [[Fatou's Lemma|Fatou's lemma]]:
>
> $$
> \int_a^b f'(x)\,dx = \int_a^b \liminf_{n \to \infty} f_n(x)\,dx \leq \liminf_{n \to \infty} \int_a^b f_n(x)\,dx.
> $$
>
> We compute $\int_a^b f_n(x)\,dx$ (using [[§17 Invariance Properties and Fubini's Theorem#^thm-17-1|translation invariance]]):
>
> $$
> \begin{aligned}
> \int_a^b f_n(x)\,dx &= n\!\left(\int_a^b f\!\left(x + \tfrac{1}{n}\right)\!dx - \int_a^b f(x)\,dx\right) = n\!\left(\int_{a+1/n}^{b+1/n} f(t)\,dt - \int_a^b f(x)\,dx\right) \\
> &= n\!\left(\int_b^{b+1/n} f(t)\,dt - \int_a^{a+1/n} f(t)\,dt\right).
> \end{aligned}
> $$
>
> Since $f$ is increasing, $f(t) \geq f(b)$ for $t \in [b, b+1/n]$ (using the extension $f(t) = f(b)$ for $t > b$, so actually $f(t) = f(b)$), and $f(t) \leq f(a + 1/n)$ for $t \in [a, a+1/n]$. More precisely:
>
> $$
> \int_b^{b+1/n} f(t)\,dt = f(b) \cdot \frac{1}{n}, \qquad \int_a^{a+1/n} f(t)\,dt \geq f(a) \cdot \frac{1}{n}.
> $$
>
> Therefore:
>
> $$
> \int_a^b f_n(x)\,dx \leq n\!\left(\frac{f(b)}{n} - \frac{f(a)}{n}\right) = f(b) - f(a).
> $$
>
> Combining: $\int_a^b f'(x)\,dx \leq \liminf_{n \to \infty} \int_a^b f_n\,dx \leq f(b) - f(a)$.

^pf-18-9-2

*Uses:* [[Fatou's Lemma|§14.15]], [[§17 Invariance Properties and Fubini's Theorem#^thm-17-1|§17.1]], [[§15 The General Lebesgue Integral#^thm-15-2|§15.2]], [[§15 The General Lebesgue Integral#^thm-15-4|§15.4]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§12 Measurable Functions#^ex-12-1|Ex. §12.1]]

> [!proof]+ Proof of (ii): Integrability of $f'$
> Since $f$ is increasing, $f' \geq 0$ wherever it exists. The integral inequality (iii) gives $\int_a^b f'\,dx \leq f(b) - f(a) < \infty$, so $f' \in L([a, b])$. In particular, $f'$ is finite a.e. ([[§14 The Lebesgue Integral for Simple Functions#^prop-14-10|integrability implies a.e. finiteness]]).

^pf-18-9-3

*Uses:* [[§15 The General Lebesgue Integral#^def-15-1|Def. §15.1]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-10|§14.10]]

> [!remark]- Connections
> - Compare the MATH 451 [[Fundamental Theorem of Calculus]] (FTC I, 451 §34.1): for $f$ continuous on $[a,b]$, differentiable on $(a,b)$, with Riemann-integrable $f'$, equality holds in (iii). The Cantor function shows why only $\leq$ survives here.
> - Monotone functions were already Riemann integrable ([[§33 Properties of the Riemann Integral#^thm-33-1|451 §33.1]]); the new information is about $f'$.

> [!theorem] Corollary §18.10: BV Functions are Differentiable A.E.
> Let $f \in BV([a, b])$. Then $f$ is differentiable a.e. on $(a, b)$, and $f' \in L([a, b])$.

^cor-18-10

> [!proof]+ Proof
> By the [[Jordan Decomposition Theorem|Jordan Decomposition Theorem]], $f = g - h$ where $g, h$ are increasing on $[a, b]$. By [[Lebesgue's Differentiation Theorem for Monotone Functions|Lebesgue's theorem]], $g$ and $h$ are each differentiable a.e. on $(a, b)$, with $g', h' \in L([a, b])$. Hence $f$ is differentiable a.e. with $f' = g' - h' \in L([a, b])$.

^pf-18-10

*Uses:* [[Jordan Decomposition Theorem|§18.7]], [[Lebesgue's Differentiation Theorem for Monotone Functions|§18.9]]

## The Fundamental Theorem of Calculus: What Goes Wrong?

> [!remark] Remark: The Central Question Revisited
> For $f: [a, b] \to \mathbb{R}$, under what assumptions do we have:
>
> $$
> f(x) - f(a) = \int_a^x f'(t)\,dt \qquad \text{for all } x \in [a, b]? \tag{*}
> $$
>
> If ($\ast$) holds, then $f(x) = f(a) + \int_a^x f'(t)\,dt$, and the integral function $G(x) = \int_a^x f'(t)\,dt$ is in $BV([a, b])$ (by the [[§18 Differentiation Theory#^thm-18-8|Total Variation Theorem]]). So $f \in BV([a, b])$ is *necessary* for ($\ast$).
>
> **Question**: Is $f \in BV([a, b])$ *sufficient* for ($\ast$)?
>
> **Answer**: **No.** The [[§18 Differentiation Theory#^ex-18-4|Cantor function]] provides a counterexample.

^rem-18-5

> [!remark]- Connections
> - ($*$) is FTC I of MATH 451 ([[Fundamental Theorem of Calculus|451 §34.1]]), which assumes $f$ continuous on $[a,b]$ and differentiable everywhere on $(a,b)$ with Riemann-integrable $f'$.

> [!example] Example §18.4: The Cantor Function (Devil's Staircase)
> The **Cantor set** $C \subseteq [0, 1]$ ([[§11 Borel Sets and Measure Spaces#^def-11-13|Def. §11.13]]) is obtained by repeatedly removing middle thirds: $C = \bigcap_{n=0}^{\infty} C_n$ where $C_0 = [0,1]$, $C_1 = [0, 1/3] \cup [2/3, 1]$, etc. The set $C$ is closed, uncountable, and has $m(C) = 0$ ([[§11 Borel Sets and Measure Spaces#^prop-11-21|§11.21]]).
>
> The **Cantor function** $\varphi: [0, 1] \to [0, 1]$ is defined via the ternary expansion: for $x \in C$, write $x = \sum_{i=1}^{\infty} 2a_i / 3^i$ (with $a_i \in \{0, 1\}$), and set $\varphi(x) = \sum_{i=1}^{\infty} a_i / 2^i$. Extend $\varphi$ to $[0, 1]$ by constancy on each removed interval. Then:
>
> - (i) $\varphi$ is continuous and increasing on $[0, 1]$, so $\varphi \in BV([0, 1])$.
> - (ii) $\varphi(0) = 0$ and $\varphi(1) = 1$.
> - (iii) $\varphi'(x) = 0$ for all $x \in [0, 1] \setminus C$, i.e., $\varphi' = 0$ a.e. (since $m(C) = 0$).
>
> Therefore:
>
> $$
> \int_0^1 \varphi'(t)\,dt = 0 \neq 1 = \varphi(1) - \varphi(0).
> $$
>
> The FTC ($*$) fails for $\varphi$, even though $\varphi \in BV$. The function “gains value” entirely on the Cantor set, which has measure zero — invisible to the Lebesgue integral.

^ex-18-4

![[m551-18-6.svg]]
*The Cantor function $\varphi$ (blue). It is constant on every removed middle third (for example $\varphi = \frac12$ on $(\frac13, \frac23)$), so $\varphi' = 0$ off $C$. All of its growth happens over $C$: the second stage $C_2$ (red on the axis) consists of four intervals of total length $\frac49$, and over each of them $\varphi$ rises by $\frac14$ (red boxes), a total rise of $1$. At stage $n$ there are $2^n$ boxes of total width $(\frac23)^n \to 0$ and total height still $1$. This is the failure of absolute continuity in [[§18 Differentiation Theory#^rem-18-7|Rem. §18.7]].*

> [!remark]- Connections
> - The Cantor set in MATH 451: [[§13 Some Topological Concepts in Metric Spaces#^rem-13-5|451 Remark §13.5]]; in this course: [[§11 Borel Sets and Measure Spaces#^prop-11-21|Properties of the Cantor Set]] (§11.21).
> - $\varphi \in BV$ by [[§18 Differentiation Theory#^ex-18-2|Ex. §18.2]]; it is the singular part in [[§18 Differentiation Theory#^thm-18-15|Lebesgue Decomposition]] (§18.15) and fails [[§18 Differentiation Theory#^thm-18-19|AC Functions Map Null Sets to Null Sets]] (§18.19).

> [!remark] Remark
> This shows that BV is not sufficient for the FTC. The missing condition is **absolute continuity**.

^rem-18-6

> [!definition] Definition §18.4: Absolute Continuity
> A function $f: [a, b] \to \mathbb{R}$ is **absolutely continuous** on $[a, b]$ (written $f \in AC([a, b])$) if for every $\varepsilon > 0$ there exists $\delta > 0$ such that for any finite collection of mutually disjoint subintervals $\{(a_k, b_k)\}_{k=1}^{n}$ of $[a, b]$:
>
> $$
> \sum_{k=1}^{n} (b_k - a_k) < \delta \implies \sum_{k=1}^{n} |f(b_k) - f(a_k)| < \varepsilon.
> $$

^def-18-4

> [!remark]- Connections
> - The function-level version of [[§16 The L¹ Space and Density Theorems#^thm-16-1|Absolute Continuity of the Integral]] (§16.1); [[§18 Differentiation Theory#^thm-18-12|Theorem §18.12]] makes the link.
> - With $n = 1$ it is [[§19 Uniform Continuity#^def-19-1|uniform continuity]] (451 Def. §19.1).

> [!remark] Remark: Comparison with Uniform Continuity
> Taking $n = 1$, absolute continuity implies uniform continuity. The converse is false: the Cantor function $\varphi$ is uniformly continuous on $[0, 1]$ (continuous on a compact set; [[§19 Uniform Continuity#^thm-19-1|451 §19.1]]) but *not* absolutely continuous — the Cantor set $C$ has $m(C) = 0$, so it can be covered by disjoint intervals of arbitrarily small total length, yet $\varphi$ gains all its value on $C$.
>
> The hierarchy of regularity is:
>
> $$
> \text{absolutely continuous} \implies \text{BV} \implies \text{differentiable a.e.}
> $$
>
> $$
> \text{absolutely continuous} \implies \text{uniformly continuous} \implies \text{continuous.}
> $$
>
> None of the reverse implications hold.

^rem-18-7

## Properties of Absolutely Continuous Functions

> [!theorem] Proposition §18.11: Basic Properties of AC Functions
> - (i) If $f \in AC([a, b])$, then $f$ is continuous on $[a, b]$.
> - (ii) If $f, g \in AC([a, b])$ and $c_1, c_2 \in \mathbb{R}$, then $c_1 f + c_2 g \in AC([a, b])$.
> - (iii) If $f \in \operatorname{Lip}([a, b])$ (i.e., $|f(x) - f(y)| \leq M|x - y|$ for all $x, y \in [a, b]$), then $f \in AC([a, b])$.

^prop-18-11

> [!proof]+ Proof
> **(i)** Taking $n = 1$ in the [[§18 Differentiation Theory#^def-18-4|AC definition]]: for every $\varepsilon > 0$, there exists $\delta > 0$ such that $|y - x| < \delta$ implies $|f(y) - f(x)| < \varepsilon$. This is exactly [[§19 Uniform Continuity#^def-19-1|uniform continuity]], which implies continuity.
>
> **(ii)** Given $\varepsilon > 0$, choose $\delta_f, \delta_g > 0$ from the AC condition for $f$ and $g$ respectively (with $\varepsilon$ replaced by $\varepsilon/(2\max(|c_1|, 1))$ and $\varepsilon/(2\max(|c_2|, 1))$). Let $\delta = \min(\delta_f, \delta_g)$. For any disjoint intervals $(x_j, y_j) \subseteq (a, b)$ with $\sum (y_j - x_j) < \delta$:
>
> $$
> \sum_{j=1}^{p} |c_1 f(y_j) + c_2 g(y_j) - c_1 f(x_j) - c_2 g(x_j)| \leq |c_1| \sum |f(y_j) - f(x_j)| + |c_2| \sum |g(y_j) - g(x_j)| < \varepsilon.
> $$
>
> **(iii)** If $f \in \operatorname{Lip}([a, b])$ with constant $M$, then for any disjoint intervals with $\sum (y_j - x_j) < \delta$:
>
> $$
> \sum_{j=1}^{p} |f(y_j) - f(x_j)| \leq M \sum_{j=1}^{p} |y_j - x_j| < M\delta.
> $$
>
> Taking $\delta = \varepsilon/M$ gives $f \in AC([a, b])$.

^pf-18-11

*Uses:* [[§18 Differentiation Theory#^def-18-4|Def. §18.4]], [[§19 Uniform Continuity#^def-19-1|451 Def. §19.1]]

> [!theorem] Theorem §18.12: The Integral Function is Absolutely Continuous
> If $g \in L([a, b])$, then $G(x) = \int_a^x g(t)\,dt$ is in $AC([a, b])$.

^thm-18-12

> [!proof]+ Proof
> This is a direct consequence of the absolute continuity of the Lebesgue integral ([[§16 The L¹ Space and Density Theorems#^thm-16-1|§16]]): for every $\varepsilon > 0$, there exists $\delta > 0$ such that $m(A) < \delta$ implies $\int_A |g|\,dt < \varepsilon$. For disjoint intervals $(x_j, y_j)$ with $\sum (y_j - x_j) < \delta$, the set $A = \bigcup_j (x_j, y_j)$ has $m(A) < \delta$, so:
>
> $$
> \sum_{j=1}^{p} |G(y_j) - G(x_j)| = \sum_{j=1}^{p} \left|\int_{x_j}^{y_j} g(t)\,dt\right| \leq \sum_{j=1}^{p} \int_{x_j}^{y_j} |g(t)|\,dt = \int_A |g|\,dt < \varepsilon.
> $$

^pf-18-12

*Uses:* [[§16 The L¹ Space and Density Theorems#^thm-16-1|§16.1]], [[§18 Differentiation Theory#^def-18-4|Def. §18.4]], [[§15 The General Lebesgue Integral#^prop-15-3|§15.3]], [[§15 The General Lebesgue Integral#^thm-15-4|§15.4]]

> [!remark]- Connections
> - MATH 451 counterpart: in FTC II ([[§34 Fundamental Theorem of Calculus#^thm-34-4|451 §34.4]]) the integral function of a bounded integrable $f$ is uniformly continuous (in fact Lipschitz).

## The Fundamental Theorem of Calculus for Lebesgue Integrals

> [!theorem] Theorem §18.13: The Fundamental Theorem of Calculus for Lebesgue Integrals
> Let $f: [a, b] \to \mathbb{R}$. Then the following are equivalent:
> - (i) $f$ is absolutely continuous on $[a, b]$.
> - (ii) $f$ is differentiable a.e., $f' \in L([a, b])$, and $f(x) - f(a) = \int_a^x f'(t)\,dt$ for all $x \in [a, b]$.

^thm-18-13

> [!proof]+ Proof of the Fundamental Theorem of Calculus
> **(ii) $\Rightarrow$ (i):** Assume $f$ is differentiable a.e., $f' \in L([a, b])$, and $f(x) - f(a) = \int_a^x f'(t)\,dt$ for all $x$. Then $f(x) = f(a) + \int_a^x f'(t)\,dt$. Since $f' \in L([a,b])$, the function $x \mapsto \int_a^x f'(t)\,dt$ is in $AC([a, b])$ by [[§18 Differentiation Theory#^thm-18-12|the theorem above]] (integral functions are AC). Adding the constant $f(a)$ preserves absolute continuity ([[§18 Differentiation Theory#^prop-18-11|property (ii)]]). Hence $f \in AC([a, b])$.
>
> **(i) $\Rightarrow$ (ii):** Assume $f \in AC([a, b])$. Then $f \in BV([a, b])$ ([[§18 Differentiation Theory#^thm-18-16|AC ⟹ BV, proved below]]), so $f$ is differentiable a.e. on $(a, b)$ with $f' \in L([a, b])$ (by the [[§18 Differentiation Theory#^cor-18-10|BV differentiability corollary]]). It remains to show $f(x) - f(a) = \int_a^x f'(t)\,dt$ for all $x \in [a, b]$.
>
> Define $F(x) = f(x) - f(a) - \int_a^x f'(t)\,dt$. Since $f \in AC([a, b])$ and $\int_a^x f'(t)\,dt \in AC([a, b])$ (by the theorem above: integral functions are AC), and $AC$ is closed under linear combinations (property (ii)), we have $F \in AC([a, b])$.
>
> Moreover, $F'(x) = f'(x) - f'(x) = 0$ a.e. on $(a, b)$ (using the fact that $(\int_a^x f'\,dt)' = f'(x)$ a.e., proved in a later subsection; [[§18 Differentiation Theory#^thm-18-26|§18.26]]).
>
> By the lemma on non-constant functions with zero derivative ([[§18 Differentiation Theory#^thm-18-27|Theorem §18.27]]), if $F$ were not constant, then $F$ would not be absolutely continuous. But $F \in AC([a, b])$, so $F$ must be constant. Since $F(a) = f(a) - f(a) - 0 = 0$, we conclude $F(x) = 0$ for all $x \in [a, b]$, i.e.:
>
> $$
> f(x) - f(a) = \int_a^x f'(t)\,dt \qquad \forall\, x \in [a, b].
> $$

^pf-18-13

*Uses:* [[§18 Differentiation Theory#^thm-18-12|§18.12]], [[§18 Differentiation Theory#^prop-18-11|§18.11]], [[§18 Differentiation Theory#^thm-18-16|§18.16]], [[§18 Differentiation Theory#^cor-18-10|§18.10]], [[§18 Differentiation Theory#^thm-18-26|§18.26]], [[§18 Differentiation Theory#^thm-18-27|§18.27]]

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
> **(i)** Since $\sum |g_k'| < \infty$ a.e. (by $\sum \int |g_k'| < \infty$ and [[§14 The Lebesgue Integral for Simple Functions#^thm-14-12|MCT]]), $\sum g_k'$ converges absolutely a.e. By [[Dominated Convergence Theorem|DCT]] (with dominating function $\sum |g_k'| \in L$):
>
> $$
> \lim_{n \to \infty} \int_c^x \sum_{k=1}^{n} g_k'(t)\,dt = \int_c^x \sum_{k=1}^{\infty} g_k'(t)\,dt.
> $$
>
> Since $\sum g_k(c)$ converges, $\sum g_k(x)$ converges for all $x$.
>
> **(ii)** $\sum g_k(x) = \sum g_k(c) + \int_c^x h(t)\,dt$ where $h = \sum g_k' \in L([a, b])$. The integral function of an $L$ function is $AC$ ([[§18 Differentiation Theory#^thm-18-12|integral functions are AC]]), and adding a constant preserves $AC$. So $\sum g_k \in AC$.
>
> **(iii)** Differentiating: $(\sum g_k)' = h' = (\int_c^x h\,dt)' = h(x) = \sum g_k'(x)$ a.e.

^pf-18-14

*Uses:* [[Fundamental Theorem of Calculus for Lebesgue Integrals|§18.13]], [[§14 The Lebesgue Integral for Simple Functions#^thm-14-12|§14.12]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-10|§14.10]], [[Dominated Convergence Theorem|§15.8]], [[§18 Differentiation Theory#^thm-18-12|§18.12]], [[§18 Differentiation Theory#^prop-18-11|§18.11]], [[§18 Differentiation Theory#^thm-18-26|§18.26]]

> [!remark]- Connections
> - The interchange is [[§15 The General Lebesgue Integral#^cor-15-9|Absolute Convergence in L¹]] (§15.9).
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
> $g$ is increasing (since $f' \geq 0$) and $g \in AC$ ([[§18 Differentiation Theory#^thm-18-12|integral of an L function]]). By the [[Fundamental Theorem of Calculus for Lebesgue Integrals|FTC]], $g' = f'$ a.e.
>
> $h$ is increasing: for $x < y$, $g(y) - g(x) = \int_x^y f' \leq f(y) - f(x)$ (by [[Lebesgue's Differentiation Theorem for Monotone Functions|Lebesgue's integral inequality for increasing functions]]), so $h(y) - h(x) = (f(y) - f(x)) - (g(y) - g(x)) \geq 0$.
>
> $h' = 0$ a.e.: $h' = f' - g' = f' - f' = 0$ a.e.

^pf-18-15

*Uses:* [[Lebesgue's Differentiation Theorem for Monotone Functions|§18.9]], [[§18 Differentiation Theory#^thm-18-12|§18.12]], [[Fundamental Theorem of Calculus for Lebesgue Integrals|§18.13]]

> [!remark] Remark
> The function $h$ is called the **singular part** of $f$: it is increasing yet gains all its growth on a set of measure zero ($\{h' > 0\}$ has measure zero). The [[§18 Differentiation Theory#^ex-18-4|Cantor function]] is the prototypical example of a purely singular increasing function.

^rem-18-8

> [!theorem] Theorem §18.16: $AC \implies BV$
> If $f \in AC([a, b])$, then $f \in BV([a, b])$.

^thm-18-16

> [!proof]+ Proof
> Take $\varepsilon = 1$ in the [[§18 Differentiation Theory#^def-18-4|AC definition]]: there exists $\delta_0 > 0$ such that for any disjoint intervals $(x_j, y_j) \subseteq (a, b)$ with $\sum (y_j - x_j) < \delta_0$, we have $\sum |f(y_j) - f(x_j)| \leq 1$.
>
> Divide $[a, b]$ into $n$ subintervals $[c_j, c_{j+1}]$ of length $(b - a)/n < \delta_0$ (choose $n$ large enough). Fix any subinterval $[c_j, c_{j+1}]$ and take any partition $c_j = t_0 < t_1 < \cdots < t_m = c_{j+1}$. The intervals $(t_0, t_1), \ldots, (t_{m-1}, t_m)$ are disjoint in $(a, b)$ with total length:
>
> $$
> \sum_{k=0}^{m-1} (t_{k+1} - t_k) = c_{j+1} - c_j = \frac{b-a}{n} < \delta_0.
> $$
>
> So the AC condition applies, giving $\sum_{k=0}^{m-1} |f(t_{k+1}) - f(t_k)| \leq 1$. Since this holds for *every* partition of $[c_j, c_{j+1}]$, taking the supremum: $\bigvee_{c_j}^{c_{j+1}}(f) \leq 1$. By [[§18 Differentiation Theory#^prop-18-5|additivity of total variation]]:
>
> $$
> \bigvee_a^b(f) = \sum_{j=0}^{n-1} \bigvee_{c_j}^{c_{j+1}}(f) \leq n.
> $$

^pf-18-16

*Uses:* [[§18 Differentiation Theory#^def-18-4|Def. §18.4]], [[§18 Differentiation Theory#^def-18-2|Def. §18.2]], [[§18 Differentiation Theory#^prop-18-5|§18.5]]

> [!remark] Remark: The Hierarchy
> Summarizing:
>
> $$
> \operatorname{Lip}([a,b]) \subsetneq AC([a,b]) \subsetneq BV([a,b]) \cap C([a,b]).
> $$
>
> The [[§18 Differentiation Theory#^ex-18-4|Cantor function]] shows $BV \cap C \not\subseteq AC$. The function $\sqrt{x}$ on $[0, 1]$ shows $AC \not\subseteq \operatorname{Lip}$ (it is AC since $\sqrt{x} = \int_0^x \frac{1}{2\sqrt{t}}\,dt$ with $\frac{1}{2\sqrt{t}} \in L$, but $|\sqrt{x}|/|x| \to \infty$).

^rem-18-9

> [!remark]- Connections
> - The inclusions: [[§18 Differentiation Theory#^prop-18-11|§18.11]] (iii) and [[§18 Differentiation Theory#^thm-18-16|§18.16]]; MATH 451 shows $\sqrt{x}$ is uniformly continuous on $[0,\infty)$ ([[§19 Uniform Continuity#^ex-19-5|451 Ex. §19.5]]).

> [!theorem] Lemma §18.17: AC on Subintervals
> If $f$ is AC on $[a, b]$ and $[c, d] \subseteq [a, b]$, then $f$ is AC on $[c, d]$.

^lem-18-17

> [!proof]+ Proof
> Any collection of disjoint intervals in $(c, d)$ is also a collection of disjoint intervals in $(a, b)$, so the same $\delta$ from the [[§18 Differentiation Theory#^def-18-4|AC condition]] on $[a, b]$ works on $[c, d]$.

^pf-18-17

*Uses:* [[§18 Differentiation Theory#^def-18-4|Def. §18.4]]

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
> Since $f \in AC([a, b])$, by the [[Fundamental Theorem of Calculus for Lebesgue Integrals|FTC]], $f' \in L([a, b])$ and $f(x) = f(a) + \int_a^x f'(t)\,dt$. By [[§18 Differentiation Theory#^lem-18-17|the first lemma]], $f$ is AC on any $[c, d] \subseteq [a, b]$, so $f(x) = f(c) + \int_c^x f'(t)\,dt$ on $[c, d]$. Applying the total variation formula for integral functions ([[§18 Differentiation Theory#^thm-18-8|§18.8]]) to $f' \in L([c, d])$:
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
> Since $\{a, b\}$ has measure zero, $m(f(\{a, b\})) = 0$ (finitely many points), so it suffices to show $m(f(Z \setminus \{a, b\})) = 0$. By [[§18 Differentiation Theory#^lem-18-18|the second lemma]] and the total variation identity:
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

*Uses:* [[Fundamental Theorem of Calculus for Lebesgue Integrals|§18.13]], [[§18 Differentiation Theory#^lem-18-17|§18.17]], [[§18 Differentiation Theory#^thm-18-8|§18.8]], [[§16 The L¹ Space and Density Theorems#^thm-16-1|§16.1]], [[§9 Lebesgue Outer Measure#^def-9-4|Def. §9.4]], [[Open Sets in ℝ are Countable Unions of Disjoint Open Intervals|§7.1]], [[§18 Differentiation Theory#^lem-18-18|§18.18]], [[Properties of Lebesgue Outer Measure|§9.1]], [[§14 The Lebesgue Integral for Simple Functions#^cor-14-13|§14.13]], [[§9 Lebesgue Outer Measure#^ex-9-1|Ex. §9.1]]

> [!remark] Remark
> This is a strong property of AC functions: they cannot “spread” null sets. The [[§18 Differentiation Theory#^ex-18-4|Cantor function]], by contrast, maps the Cantor set ($m = 0$) onto $[0, 1]$ ($m = 1$) — another illustration of why $BV \cap C \not\subseteq AC$.

^rem-18-10

## Measurability Under Continuous and Linear Maps

> [!theorem] Theorem §18.20: Continuous Maps Preserve Bounded Closed Sets
> Let $T: \mathbb{R}^n \to \mathbb{R}^n$ be a continuous map. Then for every bounded closed set $F \subseteq \mathbb{R}^n$, the image $T(F)$ is bounded and closed.

^thm-18-20

> [!proof]+ Proof
> Since $F$ is bounded and closed in $\mathbb{R}^n$, $F$ is compact ([[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|Heine–Borel]]). Since $T$ is continuous, $T(F)$ is compact ([[Continuous Image of a Compact Space is Compact]]). Since $\mathbb{R}^n$ is a metric space, compact subsets are bounded and closed ([[Heine–Borel Theorem]]).

^pf-18-20

*Uses:* [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|§6.4]], [[Continuous Image of a Compact Space is Compact|590 §15.3]], [[Heine–Borel Theorem|590 §15.12]]

> [!theorem] Theorem §18.21: Continuous Maps Preserving Null Sets Preserve Measurability
> Let $T: \mathbb{R}^n \to \mathbb{R}^n$ be a continuous map. Assume $T$ maps measure-zero sets to measure-zero sets: $m^*(Z) = 0 \implies m^*(T(Z)) = 0$. Then for every $E \in \mathcal{M}(\mathbb{R}^n)$, we have $T(E) \in \mathcal{M}(\mathbb{R}^n)$.

^thm-18-21

> [!proof]+ Proof
> Write $E = \bigcup_{m=1}^{\infty} F_m \cup Z$, where each $F_m$ is bounded and closed with $m(F_m) < \infty$, and $m(Z) = 0$ ([[Inner Regularity of Lebesgue Measure|§11.10]], as in the proof of [[§17 Invariance Properties and Fubini's Theorem#^thm-17-8|§17.8]]). Then $T(E) = \bigcup_{m=1}^{\infty} T(F_m) \cup T(Z)$. By [[§18 Differentiation Theory#^thm-18-20|the previous theorem]], each $T(F_m)$ is bounded and closed, hence [[§11 Borel Sets and Measure Spaces#^cor-11-7|measurable]]. By hypothesis, $m^*(T(Z)) = 0$, so $T(Z)$ is [[§10 Lebesgue Measurable Sets#^ex-10-1|measurable]]. A countable union of measurable sets is measurable, so $T(E) \in \mathcal{M}(\mathbb{R}^n)$.

^pf-18-21

*Uses:* [[Inner Regularity of Lebesgue Measure|§11.10]], [[§18 Differentiation Theory#^thm-18-20|§18.20]], [[§11 Borel Sets and Measure Spaces#^cor-11-7|§11.7]], [[§10 Lebesgue Measurable Sets#^ex-10-1|Ex. §10.1]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]]

> [!remark]- Connections
> - MATH 452 analogue for Jordan content: [[§15 Multivariable Integration#^prop-15-16|C¹ Diffeomorphisms Preserve Jordan Measurability]] (452 §15.16).
> - Applied to AC functions via [[§18 Differentiation Theory#^thm-18-19|§18.19]] (for $n = 1$) and to linear maps via [[§18 Differentiation Theory#^thm-18-22|§18.22]].

> [!theorem] Theorem §18.22: Linear Maps Preserve Null Sets
> Let $T: \mathbb{R}^n \to \mathbb{R}^n$ be a linear map. Then $m^*(Z) = 0 \implies m^*(T(Z)) = 0$.

^thm-18-22

> [!proof]+ Proof
> **Case 1: $T$ is not invertible.** Then $\det T = 0$ ([[Invertible ⟺ nonzero determinant|LADR 9.50]]), so $T(\mathbb{R}^n)$ is a proper linear subspace of $\mathbb{R}^n$ (dimension $< n$). A $k$-dimensional subspace of $\mathbb{R}^n$ with $k < n$ has $n$-dimensional Lebesgue measure zero (it is contained in a countable union of “flat” rectangles with one side of length $0$). Since $T(Z) \subseteq T(\mathbb{R}^n)$, we have $m^{\ast}(T(Z)) = 0$.
>
> **Case 2: $T$ is invertible.** We show $m(T(R)) = |\!\det T|\,m(R)$ for any rectangle $R$, then use L-coverings.
>
> *Measure of parallelotopes.* Factor $T$ into elementary row operations (which generate all invertible linear maps): scaling one coordinate by $c$ multiplies volume by $|c|$ and determinant by $c$; adding a multiple of one coordinate to another is a shear with determinant $1$ that preserves volume (by [[Fubini's Theorem (Lebesgue)|Fubini]]: the cross-sectional area at each height is unchanged); swapping two coordinates has determinant $-1$ and preserves volume. Since both $m(T(\cdot))$ and $|\!\det T|\,m(\cdot)$ are multiplicative under composition ([[§34 Determinants#^ladr-9-49|LADR 9.49]]), $m(T(R)) = |\!\det T|\,m(R)$. (Here the composition step needs the volume formula for images of general sets, not only of rectangles, since after the first factor the image of $R$ is no longer a rectangle. What the null-set argument below actually uses is $m^{\ast}(E(A)) \leq |\!\det E|\,m^{\ast}(A)$ for each elementary map $E$ and every $A \subseteq \mathbb{R}^n$: for scalings and swaps this holds because $E$ maps L-coverings to L-coverings, scaling each volume by $|\!\det E|$, and for a shear one applies the cross-section argument to an open $G \supseteq A$ with $m(G) \leq m^{\ast}(A) + \varepsilon$, whose image $E(G)$ is open with the same cross-sectional measures. Composing gives $m^{\ast}(T(A)) \leq |\!\det T|\,m^{\ast}(A)$; the equality for all measurable sets is [[§34 Determinants#^ladr-9-61|LADR 9.61]].)
>
> *Null sets.* For any $\varepsilon > 0$, choose an [[§9 Lebesgue Outer Measure#^def-9-3|L-covering]] $\{R_j\}_{j=1}^{\infty}$ of $Z$ with $\sum m(R_j) < \varepsilon$. Then $\{T(R_j)\}$ covers $T(Z)$, so by [[Properties of Lebesgue Outer Measure|subadditivity]]:
>
> $$
> m^*(T(Z)) \leq \sum_{j=1}^{\infty} m(T(R_j)) = |\!\det T| \sum_{j=1}^{\infty} m(R_j) < |\!\det T|\,\varepsilon.
> $$
>
> Since $\varepsilon > 0$ is arbitrary, $m^*(T(Z)) = 0$.

^pf-18-22

*Uses:* [[Invertible ⟺ nonzero determinant|LADR 9.50]], [[§9 Lebesgue Outer Measure#^def-9-4|Def. §9.4]], [[Fubini's Theorem (Lebesgue)|§17.6]], [[§34 Determinants#^ladr-9-49|LADR 9.49]], [[§9 Lebesgue Outer Measure#^def-9-3|Def. §9.3]], [[Properties of Lebesgue Outer Measure|§9.1]]

> [!remark]- Connections
> - The formula $m(T(R)) = \vert\det T\vert\, m(R)$ is [[§34 Determinants#^ladr-9-61|LADR 9.61]] (a linear map scales volume by the absolute value of its determinant), which LADR proves via singular values rather than elementary operations.
> - In MATH 452 it is [[§15 Multivariable Integration#^prop-15-19|Determinants Measure Volume Distortion]] (452 §15.19), the linear case of the [[Change of Variables Formula (multiple integrals)]].

> [!theorem] Corollary §18.23: Composition with Invertible Linear Maps Preserves Measurability
> Let $f$ be a measurable function on $\mathbb{R}^n$ and $T: \mathbb{R}^n \to \mathbb{R}^n$ an invertible linear map. Then $f \circ T$ is measurable on $\mathbb{R}^n$.

^cor-18-23

> [!proof]+ Proof
> For any $\alpha \in \mathbb{R}$:
>
> $$
> \{x \in \mathbb{R}^n : (f \circ T)(x) > \alpha\} = (f \circ T)^{-1}((\alpha, \infty)) = T^{-1}(f^{-1}((\alpha, \infty))).
> $$
>
> Since $f$ is [[§12 Measurable Functions#^def-12-2|measurable]], $A = f^{-1}((\alpha, \infty)) \in \mathcal{M}(\mathbb{R}^n)$. Since $T^{-1}$ is an invertible linear map (hence continuous and [[§18 Differentiation Theory#^thm-18-22|preserving null sets]]), $T^{-1}(A) \in \mathcal{M}(\mathbb{R}^n)$ by [[§18 Differentiation Theory#^thm-18-21|the theorem above]]. So $f \circ T$ is measurable.

^pf-18-23

*Uses:* [[§12 Measurable Functions#^def-12-2|Def. §12.2]], [[§18 Differentiation Theory#^thm-18-22|§18.22]], [[§18 Differentiation Theory#^thm-18-21|§18.21]]

> [!theorem] Proposition §18.24: Measurability of $f(x + t)$ on $\mathbb{R}^2$
> If $f$ is a measurable function on $\mathbb{R}$, then $(x, t) \mapsto f(x + t)$ is a measurable function on $\mathbb{R}^2$.

^prop-18-24

> [!proof]+ Proof
> Define $F: \mathbb{R}^2 \to \mathbb{R}$ by $F(x, y) = f(x)$. Then $F$ is measurable on $\mathbb{R}^2$: for each $\alpha$, $\{(x,y) : F(x,y) > \alpha\} = \{x : f(x) > \alpha\} \times \mathbb{R}$, which is measurable ([[§17 Invariance Properties and Fubini's Theorem#^thm-17-8|product of a measurable set with ℝ]]).
>
> Define the invertible linear map $T: \mathbb{R}^2 \to \mathbb{R}^2$ by $T(x, t) = (x + t,\; x - t)$, so $T^{-1}(u, v) = ((u+v)/2,\; (u-v)/2)$. Then:
>
> $$
> F(T(x, t)) = F(x + t,\; x - t) = f(x + t).
> $$
>
> By [[§18 Differentiation Theory#^cor-18-23|the corollary above]], $F \circ T$ is measurable on $\mathbb{R}^2$.

^pf-18-24

*Uses:* [[§12 Measurable Functions#^def-12-2|Def. §12.2]], [[§17 Invariance Properties and Fubini's Theorem#^thm-17-8|§17.8]], [[§18 Differentiation Theory#^cor-18-23|§18.23]]

## Differentiating the Integral: $F'(x) = f(x)$ A.E.

The other direction of the FTC asks: if we *start* with an integrable function and form its integral, can we recover it by differentiating?

> [!theorem] Lemma §18.25: Averaging Lemma
> Let $f \in L(\mathbb{R})$. Define the **average function**:
>
> $$
> F_h(x) = \frac{1}{h}\int_0^h f(x + t)\,dt \qquad (h > 0).
> $$
>
> Then $\lim_{h \to 0} \int_{\mathbb{R}} |F_h(x) - f(x)|\,dx = 0$, i.e., $F_h \to f$ in $L^1(\mathbb{R})$.

^lem-18-25

> [!proof]+ Proof
> *$F_h \in L^1(\mathbb{R})$*: By the triangle inequality and [[Tonelli's Theorem|Tonelli]] (swapping the order of integration):
>
> $$
> \int_{\mathbb{R}} |F_h(x)|\,dx \leq \frac{1}{h}\int_0^h \int_{\mathbb{R}} |f(x+t)|\,dx\,dt = \frac{1}{h}\int_0^h \|f\|_1\,dt = \|f\|_1 < \infty,
> $$
>
> where we used [[§17 Invariance Properties and Fubini's Theorem#^thm-17-1|translation invariance]] ($\int |f(x+t)|\,dx = \int |f(x)|\,dx = \|f\|_1$). So $F_h \in L^1(\mathbb{R})$.
>
> *$\|F_h - f\|_1 \to 0$*: Note:
>
> $$
> F_h(x) - f(x) = \frac{1}{h}\int_0^h f(x+t)\,dt - f(x) = \frac{1}{h}\int_0^h \bigl(f(x+t) - f(x)\bigr)\,dt.
> $$
>
> Therefore:
>
> $$
> \int_{\mathbb{R}} |F_h(x) - f(x)|\,dx \leq \frac{1}{h}\int_0^h \int_{\mathbb{R}} |f(x+t) - f(x)|\,dx\,dt,
> $$
>
> where we used the triangle inequality under the integral and swapped the order of integration (justified by Tonelli, since $g(x,t) = |f(x+t) - f(x)|$ is measurable on $\mathbb{R}^2$).
>
> *Measurability of $g$*: By [[§18 Differentiation Theory#^prop-18-24|the proposition above]], $(x, t) \mapsto f(x+t)$ is measurable on $\mathbb{R}^2$. Since $f(x)$ is also measurable on $\mathbb{R}^2$ (constant in $t$), $g(x, t) = |f(x+t) - f(x)|$ is [[§12 Measurable Functions#^thm-12-3|measurable]].
>
> By the [[§17 Invariance Properties and Fubini's Theorem#^thm-17-2|average continuity theorem]] ([[§17 Invariance Properties and Fubini's Theorem|§17]]), for every $\varepsilon > 0$ there exists $\delta > 0$ such that $|t| < \delta$ implies $\int_{\mathbb{R}} |f(x+t) - f(x)|\,dx < \varepsilon$. So for $0 < h < \delta$:
>
> $$
> \int_{\mathbb{R}} |F_h(x) - f(x)|\,dx \leq \frac{1}{h}\int_0^h \varepsilon\,dt = \varepsilon.
> $$

^pf-18-25

*Uses:* [[Tonelli's Theorem|§17.3]], [[§15 The General Lebesgue Integral#^prop-15-3|§15.3]], [[§17 Invariance Properties and Fubini's Theorem#^thm-17-1|§17.1]], [[§16 The L¹ Space and Density Theorems#^def-16-1|Def. §16.1]], [[§18 Differentiation Theory#^prop-18-24|§18.24]], [[§12 Measurable Functions#^thm-12-3|§12.3]], [[§17 Invariance Properties and Fubini's Theorem#^thm-17-2|§17.2]]

> [!theorem] Theorem §18.26: Differentiation of the Integral
> Let $f \in L(\mathbb{R})$. Define $F(x) = \int_a^x f(t)\,dt$. Then $F$ is differentiable a.e. and $F'(x) = f(x)$ a.e.

^thm-18-26

> [!proof]+ Proof
> By the [[§18 Differentiation Theory#^lem-18-25|Averaging Lemma]], $F_h \to f$ in $L^1$ as $h \to 0$. In particular, there exists a sequence $h_n \to 0$ such that $F_{h_n} \to f$ pointwise a.e. (every $L^1$-convergent sequence has a pointwise a.e. convergent subsequence; [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-17|§19.17]]).
>
> But:
>
> $$
> F_{h_n}(x) = \frac{1}{h_n}\int_0^{h_n} f(x+t)\,dt = \frac{1}{h_n}\int_x^{x+h_n} f(t)\,dt = \frac{F(x + h_n) - F(x)}{h_n}.
> $$
>
> So $\frac{F(x+h_n) - F(x)}{h_n} \to f(x)$ a.e. along the sequence $\{h_n\}$.
>
> To promote this to a full derivative (limit as $h \to 0$, not just along a sequence): we already know $F \in BV([a,b])$ (by the [[§18 Differentiation Theory#^thm-18-8|Total Variation Theorem]]), hence $F$ is differentiable a.e. (by [[Lebesgue's Differentiation Theorem for Monotone Functions|Lebesgue's theorem]]; [[§18 Differentiation Theory#^cor-18-10|§18.10]]). Where $F'(x)$ exists, it must equal $f(x)$ (since the subsequential limit $f(x)$ is the only possible limit). Therefore $F'(x) = f(x)$ a.e.

^pf-18-26

*Uses:* [[§18 Differentiation Theory#^lem-18-25|§18.25]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-17|§19.17]], [[§18 Differentiation Theory#^thm-18-8|§18.8]], [[Lebesgue's Differentiation Theorem for Monotone Functions|§18.9]], [[§18 Differentiation Theory#^cor-18-10|§18.10]]

> [!remark]- Connections
> - MATH 451 counterpart: FTC II ([[§34 Fundamental Theorem of Calculus#^thm-34-4|451 §34.4]]) gives $F'(x_0) = f(x_0)$ at every point where $f$ is continuous; here continuity is dropped at the cost of “a.e.”.
> - Completes the proof of [[Fundamental Theorem of Calculus for Lebesgue Integrals|the FTC for Lebesgue integrals]] (§18.13).

> [!definition] Definition §18.5: Lebesgue Point
> Let $f \in L(\mathbb{R})$ and define $F(x) = \int_a^x f(t)\,dt$. A point $x_0$ is called a **Lebesgue point** of $f$ if $F'(x_0)$ exists and $F'(x_0) = f(x_0)$, i.e.:
>
> $$
> \lim_{h \to 0} \frac{1}{h}\int_0^h f(x_0 + t)\,dt = f(x_0).
> $$
>
> [[§18 Differentiation Theory#^thm-18-26|The theorem above]] shows that a.e. point is a Lebesgue point of $f$. (This is weaker than the standard notion of a Lebesgue point, which asks that $\lim_{h \to 0} \frac{1}{2h}\int_{-h}^{h} |f(x_0 + t) - f(x_0)|\,dt = 0$; that stronger property also holds at a.e. point, but it is not needed here.)

^def-18-5

![[m551-18-7.svg]]
*Averages over shrinking windows. With $F_h(x_0) = \frac1h\int_0^h f(x_0 + t)\,dt$ as in the [[§18 Differentiation Theory#^lem-18-25|Averaging Lemma]], the average height of $f$ (blue) over $[x_0, x_0 + h]$ is the dashed level, and over the shorter window $[x_0, x_0 + h']$ it is the red one. Each average is a difference quotient of the integral function, so $x_0$ is a Lebesgue point exactly when these averages tend to $f(x_0)$ as the window shrinks; by [[§18 Differentiation Theory#^thm-18-26|Theorem §18.26]] this happens at a.e. $x_0$.*

> [!remark] Remark
> If $\tilde{F}(x) = f(x) - f(a) - \int_a^x f'(t)\,dt$, then $\tilde{F}$ is differentiable a.e. with $\tilde{F}' = f' - f' = 0$ a.e. on $(a,b)$. The [[§18 Differentiation Theory#^ex-18-4|Cantor function]] shows $\tilde{F}$ can be non-constant: $\tilde{F} \equiv \varphi$ satisfies $\varphi' = 0$ a.e. but $\varphi(1) - \varphi(0) = 1$. So the FTC fails precisely when $\tilde{F}$ is a “Cantor-like” component.

^rem-18-11

## Non-Constant Functions with Zero Derivative Are Not Absolutely Continuous

> [!theorem] Theorem §18.27
> Assume $f$ is differentiable a.e. on $(a, b)$ with $f'(x) = 0$ for a.e. $x \in (a, b)$, and assume $f$ is not a constant. Then $f$ is not absolutely continuous: there exists $\varepsilon_0 > 0$ such that for every $\delta > 0$, there exist finitely many mutually disjoint subintervals $\{(x_j, y_j)\}_{j=1}^{n}$ of $(a, b)$ with:
>
> $$
> \sum_{j=1}^{n} |y_j - x_j| < \delta \qquad \text{but} \qquad \sum_{j=1}^{n} |f(y_j) - f(x_j)| \geq \varepsilon_0.
> $$

^thm-18-27

> [!proof]+ Proof
> Since $f$ is not constant, there exists $c \in (a, b]$ with $f(c) \neq f(a)$; if $f(c) = f(a)$ for every $c \in (a, b)$, take $c = b$ (the argument below works verbatim with $c = b$). Let $A = \{x \in (a, c) : f'(x) = 0\}$. Since $f' = 0$ a.e., we have $m([a, c] \setminus A) = 0$, so $m(A) = c - a$.
>
> For every $x_0 \in A$: $f'(x_0) = 0$ means for every $r > 0$, there exists $\delta_0 > 0$ such that for all $0 < h < \delta_0$:
>
> $$
> |f(x_0 + h) - f(x_0)| < r\,h.
> $$
>
> Define $\Gamma = \{[x, x+h] : x \in A,\; [x, x+h] \subseteq (a, c),\; |f(x+h) - f(x)| < r\,|h|\}$. For any $r > 0$, $\Gamma$ is a [[§18 Differentiation Theory#^def-18-1|Vitali covering]] of $A$.
>
> By the [[Vitali Covering Theorem|Vitali Covering Lemma]]: for every $\delta > 0$, there exist finitely many disjoint intervals $[x_j, x_j + h_j] \in \Gamma$, $j = 1, \ldots, p$, with:
>
> $$
> m\!\left(A \setminus \bigcup_{j=1}^{p} [x_j, x_j + h_j]\right) < \delta.
> $$
>
> Since $m([a,c] \setminus A) = 0$, this gives $m\!\left([a, c] \setminus \bigcup_{j=1}^{p} [x_j, x_j + h_j]\right) < \delta$.
>
> The intervals $[x_j, x_j + h_j] \subseteq (a,c)$ are disjoint, so $\sum h_j \leq c - a$. Ordering them as $a < x_1 < x_1 + h_1 < x_2 < \cdots < x_p + h_p < c$, the “gaps” between them (including the initial and final gaps) have total length:
>
> $$
> \sum_{j=0}^{p} |(\text{gaps})| = (c - a) - \sum_{j=1}^{p} h_j.
> $$
>
> By the triangle inequality:
>
> $$
> |f(c) - f(a)| \leq \sum_{j=0}^{p} |f(\text{gap endpoints})| + \sum_{j=1}^{p} |f(x_j + h_j) - f(x_j)|.
> $$
>
> More precisely, the total oscillation of $f$ on $[a, c]$ decomposes as:
>
> $$
> |f(c) - f(a)| \leq \sum_{\text{gaps}} |f \text{ change}| + \sum_{j=1}^{p} |f(x_j + h_j) - f(x_j)| < \sum_{\text{gaps}} |f \text{ change}| + r \sum_{j=1}^{p} h_j \leq \sum_{\text{gaps}} |f \text{ change}| + r(c - a).
> $$
>
> Take $r = \frac{|f(c) - f(a)|}{2(c - a)}$. Then:
>
> $$
> \sum_{\text{gaps}} |f \text{ change}| \geq |f(c) - f(a)| - r(c - a) = \frac{1}{2}|f(c) - f(a)| > 0.
> $$
>
> Set $\varepsilon_0 = \frac{1}{2}|f(c) - f(a)|$. The “gaps” are finitely many disjoint subintervals of $[a, c]$ whose total length is $< \delta$ (since they form the complement of the Vitali cover), yet the total oscillation of $f$ on these gaps is $\geq \varepsilon_0$. This shows $f$ is not absolutely continuous.

^pf-18-27

*Uses:* [[§18 Differentiation Theory#^def-18-1|Def. §18.1]], [[Vitali Covering Theorem|§18.2]], [[§18 Differentiation Theory#^def-18-4|Def. §18.4]], [[§9 Lebesgue Outer Measure#^prop-9-2|§9.2]], [[Properties of Lebesgue Outer Measure|§9.1]]

> [!remark]- Connections
> - MATH 451 counterpart: [[§29 The Mean Value Theorem#^cor-29-4|Vanishing Derivative Means Constant]] (451 §29.4), proved with the [[Mean Value Theorem]] when $f' = 0$ *everywhere*; the [[§18 Differentiation Theory#^ex-18-4|Cantor function]] shows “a.e.” needs the extra AC hypothesis.
> - Used in the proof of [[Fundamental Theorem of Calculus for Lebesgue Integrals|the FTC for Lebesgue integrals]] (§18.13).
