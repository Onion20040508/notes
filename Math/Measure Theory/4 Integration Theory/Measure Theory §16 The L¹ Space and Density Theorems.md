---
type: section
subject: "[[Measure Theory]]"
chapter: 4
section: 16
tags: [measure-theory, math551]
---
← [[Measure Theory §15 The General Lebesgue Integral]] · ↑ [[Measure Theory — 4 Integration Theory]] · [[Measure Theory §17 Invariance Properties and Fubini's Theorem]] →

## Absolute Continuity of the Integral

> [!theorem] Theorem §16.1: Absolute Continuity of the Integral
> Let $f \in L(E)$, $E \in \mathcal{M}$, $E \subseteq \mathbb{R}^n$. Then for every $\varepsilon > 0$, there exists $\delta > 0$ such that for all $e \subseteq E$, $e \in \mathcal{M}$:
>
> $$
> m(e) < \delta \implies \int_e |f(x)|\,dx < \varepsilon.
> $$

^thm-16-1

> [!proof]+ Proof
> **Step 1: Bounded case.** Assume $f$ is also bounded, i.e., $|f(x)| \leq M$ for all $x \in E$. Then for any measurable $e \subseteq E$:
>
> $$
> \int_e |f|\,dx \leq M\,m(e).
> $$
>
> Given $\varepsilon > 0$, take $\delta = \varepsilon/M$. Then $m(e) < \delta$ implies $\int_e |f|\,dx < \varepsilon$.
>
> **Step 2: General case via truncation.**

^pf-16-1

*Uses:* [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]]

> [!theorem] Lemma §16.2
> Let $f \in L(E)$. Then there exists a sequence of bounded measurable functions $f_k \in L(E)$ with $|f_k(x)| \leq |f(x)|$ for all $x \in E$ and $\lim_{k \to \infty} \int_E |f_k - f|\,dx = 0$.

^lem-16-2

> [!proof]+ Proof of Lemma
> Define:
>
> $$
> f_k(x) = \begin{cases} f(x) & \text{if } |f(x)| \leq k, \\ k & \text{if } f(x) > k, \\ -k & \text{if } f(x) < -k. \end{cases}
> $$
>
> Then $|f_k(x)| \leq k$ (bounded), $|f_k(x)| \leq |f(x)|$ (so $|f_k| \in L(E)$), and $f_k(x) \to f(x)$ pointwise. Since $|f_k - f| \leq 2|f| \in L(E)$, by [[Dominated Convergence Theorem|DCT]]: $\int_E |f_k - f|\,dx \to 0$.

^pf-16-2

*Uses:* [[Measure Theory §15 The General Lebesgue Integral#^prop-15-1|§15.1]], [[Dominated Convergence Theorem|§15.8]]

![[m551-16-1.svg]]
*Truncation at height $k$: $f_k$ (blue) agrees with $f$ (gray) where $|f| \leq k$ and is clipped to $\pm k$ elsewhere, so $f_k$ is bounded and $|f_k| \leq |f|$. The red area is $\int_E |f - f_k|$; it sits over $\{|f| > k\}$ and tends to $0$ by the DCT with dominator $2|f|$. In [[Measure Theory §16 The L¹ Space and Density Theorems#^thm-16-1|Theorem §16.1]] the bounded part is small on small sets because $\int_e |f_k| \leq k\, m(e)$, and the red remainder is small everywhere.*

> [!proof]+ Proof of Theorem §16.1 (continued)
> Now let $\varepsilon > 0$. By the [[Measure Theory §16 The L¹ Space and Density Theorems#^lem-16-2|lemma]], choose $m$ such that $\int_E |f_m - f|\,dx < \varepsilon/2$. Since $|f_m|$ is bounded (by $m$), by Step 1 there exists $\delta > 0$ such that $m(e) < \delta$ implies $\int_e |f_m|\,dx < \varepsilon/2$.
>
> For any measurable $e \subseteq E$ with $m(e) < \delta$:
>
> $$
> \int_e |f|\,dx = \int_e |f| - |f_m| + |f_m|\,dx \leq \int_e \bigl||f| - |f_m|\bigr|\,dx + \int_e |f_m|\,dx.
> $$
>
> Since $\bigl||f(x)| - |f_m(x)|\bigr| \leq |f(x) - f_m(x)|$ (reverse [[Single Variable Analysis §3 The Set ℝ of Real Numbers#^thm-3-3|triangle inequality]]):
>
> $$
> \int_e |f|\,dx \leq \int_e |f - f_m|\,dx + \int_e |f_m|\,dx \leq \int_E |f - f_m|\,dx + \int_e |f_m|\,dx < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
> $$

^pf-16-1-cont

*Uses:* [[Measure Theory §16 The L¹ Space and Density Theorems#^lem-16-2|§16.2]], [[Measure Theory §15 The General Lebesgue Integral#^thm-15-2|§15.2]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^cor-14-7|§14.7]], [[Single Variable Analysis §3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]]

> [!remark]- Connections
> - Gives that $x \mapsto \int_a^x g$ is absolutely continuous ([[Measure Theory §18 Differentiation Theory#^def-18-4|Def. §18.4]], [[Measure Theory §18 Differentiation Theory#^thm-18-12|Theorem §18.12]]); compare uniform continuity: [[Measure Theory §18 Differentiation Theory#^rem-18-7|Rem. §18.7]], [[Single Variable Analysis §19 Uniform Continuity#^def-19-1|451 Def. §19.1]].
> - In the language of [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^def-14-3|Def. §14.3]]: the measure $\nu(e) = \int_e |f|$ is small on sets of small Lebesgue measure.

> [!theorem] Theorem §16.3: Tail Decay of the Integral
> Let $f \in L(E)$. Then for every $\varepsilon > 0$, there exists $R > 0$ such that for all $r > R$:
>
> $$
> \int_{E \cap B(0,r)^c} |f(x)|\,dx < \varepsilon,
> $$
>
> where $B(0, r) = \{x \in \mathbb{R}^n : |x| < r\}$.

^thm-16-3

> [!proof]+ Proof
> Define $f_m(x) = f(x)$ if $|x| \leq m$ and $f_m(x) = 0$ if $|x| > m$, for $x \in E$. Then $f_m \to f$ pointwise and $|f_m| \leq |f| \in L(E)$. By [[Dominated Convergence Theorem|DCT]], $\int_E |f_m - f|\,dx \to 0$. Since $f - f_m = f\,\chi_{\{|x|>m\}}$, we have $\int_{E \cap B(0,m)^c} |f|\,dx \to 0$.

^pf-16-3

*Uses:* [[Dominated Convergence Theorem|§15.8]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-6|§14.6]]

> [!remark]- Connections
> - Together with [[Measure Theory §16 The L¹ Space and Density Theorems#^thm-16-1|Theorem §16.1]], these are the two ways an integrable function can be “cut down” (small sets, far-away sets).
> - Compare the MATH 451 improper integral on $[a, \infty)$: [[Single Variable Analysis §36 Improper Integrals#^def-36-1|451 Def. §36.1]].

## The $L^1$ Space

> [!definition] Definition §16.1: $L^1$ Space and Norm
> Let $E \in \mathcal{M}$, $E \subseteq \mathbb{R}^n$. Define:
>
> $$
> L^1(E) = L(E) = \left\{f: E \to \mathbb{R} \cup \{\pm\infty\} \;\middle|\; f \text{ measurable},\; \int_E |f|\,dx < \infty\right\}.
> $$
>
> For $f \in L^1(E)$, the **$L^1$ norm** is:
>
> $$
> \|f\|_{L^1(E)} = \|f\|_1 = \int_E |f(x)|\,dx.
> $$

^def-16-1

> [!remark]- Connections
> - The case $p = 1$ of [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^def-19-5|Def. §19.5]] ($L^p$ spaces). Same as $L(E)$ of [[Measure Theory §15 The General Lebesgue Integral#^def-15-1|Def. §15.1]] by [[Measure Theory §15 The General Lebesgue Integral#^rem-15-1|Rem. §15.1]].

> [!theorem] Theorem §16.4: $L^1$ is a Normed Vector Space
> Let $f, g \in L^1(E)$ and $a, b \in \mathbb{R}$. Then:
> - (i) $af + bg \in L^1(E)$.
> - (ii) $\|af\|_1 = |a|\,\|f\|_1$.
> - (iii) $\|f + g\|_1 \leq \|f\|_1 + \|g\|_1$  (triangle inequality).
> - (iv) $\|f\|_1 = 0 \iff f = 0$ a.e. on $E$.
>
> Thus $L^1(E)$ is a normed vector space (identifying functions that agree a.e.).

^thm-16-4

> [!remark]- Connections
> - (i)–(ii) are [[Measure Theory §15 The General Lebesgue Integral#^thm-15-2|Theorem §15.2]], (iii) is [[Measure Theory §15 The General Lebesgue Integral#^prop-15-3|Proposition §15.3]], (iv) is [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-11|Proposition §14.11]] with [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-9|§14.9]].
> - Norm axioms: [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^def-19-2|Def. §19.2]]; the linear-algebra model is [[Linear Algebra 6A Inner Products and Norms#^ladr-6-9|LADR 6.9]] and the [[Triangle inequality]] (LADR 6.17), though the $L^1$ norm does not come from an inner product. Generalized in [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-10|Theorem §19.10]].

> [!definition] Definition §16.2: $L^1$ Metric and Convergence
> Define $d(f, g) = \|f - g\|_1 = \int_E |f - g|\,dx$. Then $d$ is a [[Topology §11 Metric Topology#^def-11-1|metric]] on $L^1(E)$ (with the convention that $f = g$ if $f = g$ a.e.), and $(L^1(E), d)$ is a metric space.
>
> We say $f_k \to f$ in $L^1(E)$ if $\lim_{k \to \infty} \|f_k - f\|_1 = \lim_{k \to \infty} \int_E |f_k - f|\,dx = 0$.

^def-16-2

> [!remark]- Connections
> - Metric spaces in MATH 451: [[Single Variable Analysis §13 Some Topological Concepts in Metric Spaces#^def-13-1|451 Def. §13.1]]; normed $\Rightarrow$ metric in general: [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-1|Proposition §19.1]].
> - $(L^1(E), d)$ is complete by [[Riesz–Fischer Theorem|Riesz–Fischer]] (§19.18). The DCT yields $L^1$ convergence: [[Measure Theory §15 The General Lebesgue Integral#^rem-15-4|Rem. §15.4]].

## Density of Simple Functions in $L^1$

> [!theorem] Theorem §16.5: Simple Functions are Dense in $L^1$
> Let $f \in L^1(E)$. Then there exists a sequence of simple functions $\{\varphi_k\}$ with $|\varphi_k(x)| \leq |f(x)|$ for all $x \in E$ and:
>
> $$
> \lim_{k \to \infty} \|\varphi_k - f\|_1 = \lim_{k \to \infty} \int_E |\varphi_k(x) - f(x)|\,dx = 0.
> $$

^thm-16-5

> [!proof]+ Proof
> By the [[Measure Theory §12 Measurable Functions#^thm-12-15|Simple Function Approximation Theorem]], for any measurable $f$ there exists a sequence of simple functions $\varphi_k$ with $|\varphi_k(x)| \leq |f(x)|$ for all $x \in E$ and $\varphi_k(x) \to f(x)$ pointwise. Since $|\varphi_k - f| \leq 2|f| \in L^1(E)$, by [[Dominated Convergence Theorem|DCT]]: $\int_E |\varphi_k - f|\,dx \to 0$.

^pf-16-5

*Uses:* [[Measure Theory §12 Measurable Functions#^thm-12-15|§12.15]], [[Dominated Convergence Theorem|§15.8]]

## Density of Step Functions in $L^1$

> [!theorem] Theorem §16.6: Step Functions are Dense in $L^1$
> Let $f \in L^1(E)$. Then for every $\varepsilon > 0$, there exists a [[Measure Theory §15 The General Lebesgue Integral#^def-15-2|step function]] $\psi$ on $\mathbb{R}^n$ such that $\|f - \psi\|_1 < \varepsilon$.
>
> (Equivalently, there exist step functions $\psi_k$ with $\|\psi_k - f\|_1 \to 0$.)

^thm-16-6

> [!proof]+ Proof
> **Step 1: Approximate $\chi_S$ by step functions.** Let $S \in \mathcal{M}$ with $m(S) < \infty$. We show that for every $\varepsilon > 0$, there exists a step function $\psi$ with $\|\chi_S - \psi\|_1 < \varepsilon$.
>
> *Observation*: For $E_1, E_2 \in \mathcal{M}$, $|\chi_{E_1}(x) - \chi_{E_2}(x)| = \chi_{E_1 \setminus E_2}(x) + \chi_{E_2 \setminus E_1}(x)$, so:
>
> $$
> \int_{\mathbb{R}^n} |\chi_{E_1} - \chi_{E_2}|\,dx = m(E_1 \setminus E_2) + m(E_2 \setminus E_1) = m(E_1 \triangle E_2).
> $$
>
> By the [[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-11|approximation theorem]] ([[Measure Theory §11 Borel Sets and Measure Spaces|§11]]), for any $\varepsilon > 0$ there exist rectangles $R_1, \ldots, R_p$ with $m(S \triangle \bigcup_{j=1}^p R_j) < \varepsilon$. Since $\bigcup_{j=1}^p R_j$ can be written as a union of disjoint rectangles $I_1, \ldots, I_m$ (by splitting overlaps), $\chi_{\bigcup R_j} = \sum_{j=1}^{m} \chi_{I_j}$ is a step function. Thus $\|\chi_S - \psi\|_1 = m(S \triangle \bigcup R_j) < \varepsilon$.
>
> **Step 2: Simple functions $\to$ step functions.** Any simple function $\varphi = \sum a_j \chi_{S_j}$ (with $m(S_j) < \infty$) can be approximated by step functions: approximate each $\chi_{S_j}$ by a step function $\psi_j$ with $\|\chi_{S_j} - \psi_j\|_1 < \varepsilon/(p\,\max|a_j|)$, then $\psi = \sum a_j \psi_j$ is a step function with $\|\varphi - \psi\|_1 < \varepsilon$.
>
> **Step 3: Combine.** Given $f \in L^1(E)$ and $\varepsilon > 0$: by [[Measure Theory §16 The L¹ Space and Density Theorems#^thm-16-5|density of simple functions]], choose $\varphi$ with $\|f - \varphi\|_1 < \varepsilon/2$. By Step 2, choose a step function $\psi$ with $\|\varphi - \psi\|_1 < \varepsilon/2$. Then $\|f - \psi\|_1 < \varepsilon$.

^pf-16-6

*Uses:* [[Measure Theory §11 Borel Sets and Measure Spaces#^def-11-9|Def. §11.9]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-8|§14.8]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]], [[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-11|§11.11]], [[Measure Theory §9 Lebesgue Outer Measure#^def-9-1|Def. §9.1]], [[Measure Theory §16 The L¹ Space and Density Theorems#^thm-16-4|§16.4]], [[Measure Theory §16 The L¹ Space and Density Theorems#^thm-16-5|§16.5]]

![[m551-16-2.svg]]
*Step 1 in the plane: a measurable $S$ with $m(S) < \infty$ (blue boundary) is approximated by finitely many disjoint rectangles $I_1, \dots, I_m$ (gray grid). The step function $\psi = \chi_{\bigcup_j I_j}$ differs from $\chi_S$ exactly on the symmetric difference $S \triangle \bigcup_j I_j$ (red), so $\|\chi_S - \psi\|_1 = m(S \triangle \bigcup_j I_j) < \varepsilon$.*

> [!remark]- Connections
> - Step 1 is the Lebesgue relaxation of Jordan measurability ([[Multivariable Analysis §15 Multivariable Integration#^def-15-5|452 Def. §15.5]]), which demands finite unions of squares approximating from inside *and* outside.
> - The MATH 451 Riemann integral is itself built from step functions: [[Single Variable Analysis §32 The Definition of the Riemann Integral#^ex-32-2|451 Ex. §32.2]], [[Measure Theory §15 The General Lebesgue Integral#^rem-15-6|Rem. §15.6]].

## Density of Compactly Supported Continuous Functions

Recall ([[Measure Theory §12 Measurable Functions#^def-12-7|Definition §12.7]]): a function $g: \mathbb{R}^n \to \mathbb{R}$ is **compactly supported** if $\operatorname{supp} g = \overline{\{x : g(x) \neq 0\}}$ is compact (i.e., [[Measure Theory §6 Open Covers and the Heine–Borel Theorem#^thm-6-4|bounded and closed]] in $\mathbb{R}^n$). Equivalently, $g(x) = 0$ outside some large ball. We write $C_c(\mathbb{R}^n)$ for the space of compactly supported continuous functions.

> [!theorem] Theorem §16.7: Compactly Supported Continuous Functions are Dense in $L^1$
> Let $f \in L^1(E)$. Then for every $\varepsilon > 0$, there exists a compactly supported continuous function $g$ on $\mathbb{R}^n$ such that $\|f - g\|_1 < \varepsilon$.

^thm-16-7

> [!proof]+ Proof
> By [[Measure Theory §16 The L¹ Space and Density Theorems#^thm-16-6|density of step functions]], it suffices to show: for any step function $\psi = \sum_{j=1}^{p} a_j\,\chi_{R_j}$ (with $\{R_j\}$ disjoint rectangles, $m(R_j) < \infty$) and any $\varepsilon > 0$, there exists a compactly supported continuous $g$ with $\|\psi - g\|_1 < \varepsilon$.
>
> By linearity, it suffices to show: for any rectangle $R$ with $m(R) < \infty$ and any $\varepsilon > 0$, there exists a compactly supported continuous $g$ with $\|\chi_R - g\|_1 < \varepsilon$.
>
> **Case $n = 1$**: Let $R = (a, b)$ (open; other types of intervals differ by null sets). Define:
>
> $$
> g(x) = \begin{cases} 1 & x \in (a+\varepsilon', b-\varepsilon'), \\ \text{linear} & x \in (a-\varepsilon', a+\varepsilon') \cup (b-\varepsilon', b+\varepsilon'), \\ 0 & x \leq a - \varepsilon' \text{ or } x \geq b + \varepsilon', \end{cases}
> $$
>
> where $\varepsilon' > 0$ is chosen small enough. Then $g$ is continuous, compactly supported, $0 \leq g \leq 1$, and $|g(x) - \chi_{(a,b)}(x)| \leq 1$ with equality only on the two transition intervals of total length $4\varepsilon'$. Thus $\|\chi_R - g\|_1 \leq 4\varepsilon'$, so choose $\varepsilon' = \varepsilon/4$.
>
> **Case $n = 2$**: If $R = R_1 \times R_2$, let $g_i$ be the compactly supported continuous approximation to $\chi_{R_i}$ from the $n = 1$ case with $\|\chi_{R_i} - g_i\|_1 < \varepsilon'$ and $\sup|g_i| \leq 1$. Define $g(x, y) = g_1(x)\,g_2(y)$. Then:
>
> $$
> \begin{aligned}
> |\chi_R(x,y) - g(x,y)| &= |\chi_{R_1}(x)\chi_{R_2}(y) - g_1(x)g_2(y)| \\
> &\leq |\chi_{R_1}(x) - g_1(x)|\,\chi_{R_2}(y) + |g_1(x)|\,|\chi_{R_2}(y) - g_2(y)|.
> \end{aligned}
> $$
>
> Integrating and using $|g_1| \leq 1$, $m(R_2) < \infty$:
>
> $$
> \|\chi_R - g\|_1 \leq m(R_2)\,\|\chi_{R_1} - g_1\|_1 + \|\chi_{R_2} - g_2\|_1 < \varepsilon'(m(R_2) + 1).
> $$
>
> Choose $\varepsilon'$ small enough to make this $< \varepsilon$.
>
> **General $n$**: By induction, using the product decomposition $R = R_1 \times \cdots \times R_n$ and the same factorization argument.

^pf-16-7

*Uses:* [[Measure Theory §16 The L¹ Space and Density Theorems#^thm-16-6|§16.6]], [[Measure Theory §16 The L¹ Space and Density Theorems#^thm-16-4|§16.4]], [[Measure Theory §15 The General Lebesgue Integral#^prop-15-1|§15.1]], [[Measure Theory §12 Measurable Functions#^def-12-7|Def. §12.7]], [[Measure Theory §9 Lebesgue Outer Measure#^def-9-1|Def. §9.1]], [[Single Variable Analysis §3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]]

![[m551-16-3.svg]]
*The case $n = 1$: the trapezoid $g$ (blue) is $0$ outside $(a - \varepsilon', b + \varepsilon')$, equal to $1$ on $(a + \varepsilon', b - \varepsilon')$, and linear in between, so it is continuous with compact support. It differs from $\chi_{(a,b)}$ (black; hollow dots mark the values not taken at $a$, $b$) only on the two transition intervals, of total length $4\varepsilon'$, and there by at most $1$ (red), so $\|\chi_{(a,b)} - g\|_1 \leq 4\varepsilon'$.*

> [!remark]- Connections
> - Continuous functions are closed under uniform limits ([[Single Variable Analysis §24 Uniform Convergence#^thm-24-2|451 §24.2]], [[Measure Theory §12 Measurable Functions#^thm-12-16|§12.16]]), so the density holds only for the weaker $L^1$ distance (cf. [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^rem-19-4|Rem. §19.4]]).
> - The $n = 2$ step integrates a product $\varphi(x)\,\chi_{R_2}(y)$ one variable at a time, an instance of [[Tonelli's Theorem]] (§17.3), proved only later; the Riemann analogue is the MATH 452 [[Fubini's Theorem]].
> - Used for [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-2|Theorem §17.2]] (average continuity); $L^p$ version [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|Theorem §19.19]]. Topology version of compact = closed and bounded: [[Heine–Borel Theorem]] (590 §15.12).

> [!remark] Remark: The Approximation Chain for $L^1$
> We have now established:
>
> $$
> C_c(\mathbb{R}^n) \;\subseteq\; \text{step functions} \;\subseteq\; \text{simple functions} \;\subseteq\; L^1(E),
> $$
>
> with each class dense in the next. Here $C_c(\mathbb{R}^n)$ denotes the compactly supported continuous functions on $\mathbb{R}^n$. This chain is fundamental for proving results about $L^1$ functions by first establishing them for nicer classes of functions.

^rem-16-1

> [!remark]- Connections
> - The $L^p$ chain: [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^rem-19-4|Rem. §19.4]], [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-20|Corollary §19.20]] (separability).
