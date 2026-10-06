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

> [!definition] Definition §18.2: Total Variation
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

^def-18-2

> [!remark]- Connections
> - Partitions as in the Riemann integral: [[§8 Motivation꞉ The Riemann Integral#^def-8-1|Def. §8.1]], [[§32 The Definition of the Riemann Integral#^def-32-1|451 Def. §32.1]].

> [!definition] Definition §18.3: Bounded Variation
> If $\bigvee_a^b(f) < \infty$, we say $f$ is of **bounded variation** on $[a, b]$, and write $f \in BV([a, b])$.

^def-18-new1

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

*Uses:* [[Mean Value Theorem|451 §29.3]], [[§18 Differentiation Theory#^def-18-2|Def. §18.2]], [[§18 Differentiation Theory#^def-18-new1|Def. §18.3]]

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

*Uses:* [[§18 Differentiation Theory#^def-18-2|Def. §18.2]], [[§18 Differentiation Theory#^def-18-new1|Def. §18.3]]

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

*Uses:* [[§18 Differentiation Theory#^def-18-2|Def. §18.2]], [[§18 Differentiation Theory#^def-18-new1|Def. §18.3]], [[§15 The General Lebesgue Integral#^thm-15-4|§15.4]], [[§15 The General Lebesgue Integral#^def-15-2|Def. §15.2]], [[§16 The L¹ Space and Density Theorems#^thm-16-6|§16.6]], [[§18 Differentiation Theory#^prop-18-4|§18.4]], [[§15 The General Lebesgue Integral#^prop-15-3|§15.3]]

Dini derivatives and Lebesgue's differentiation theorem continue in [[§18a Lebesgue's Differentiation Theorem]]; differentiation of the integral follows in [[§18b Differentiating the Integral]], and absolute continuity and the FTC in [[§18c Absolute Continuity and the FTC]].
