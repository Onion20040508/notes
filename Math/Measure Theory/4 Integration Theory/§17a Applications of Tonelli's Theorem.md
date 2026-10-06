---
type: section
subject: "[[Measure Theory]]"
chapter: 4
section: 17
tags: [measure-theory, math551]
---
← [[§17 Invariance Properties and Fubini's Theorem]] · ↑ [[· 4 Integration Theory]] · [[§18 Differentiation Theory]] →

[[Tonelli's Theorem|Tonelli's theorem]], applied to characteristic functions and to functions on product spaces, gives the cross-section theorem, the measurability and measure of product sets, the measure of graphs and subgraphs, and the layer cake formula.

## Applications of Tonelli's Theorem

> [!theorem] Theorem §17.7: Cross-Section Theorem (Restated)
> Let $E \subseteq \mathbb{R}^p \times \mathbb{R}^q$ be measurable. For $x \in \mathbb{R}^p$, define $E(x) = \{y \in \mathbb{R}^q : (x, y) \in E\}$. Then:
> - (i) For a.e. $x \in \mathbb{R}^p$, $E(x)$ is a measurable subset of $\mathbb{R}^q$.
> - (ii) $m(E) = \int_{\mathbb{R}^p} m(E(x))\,dx$.

^thm-17-7

> [!proof]+ Proof
> Apply [[Tonelli's Theorem|Tonelli's theorem]] to $f(x, y) = \chi_E(x, y)$.

^pf-17-7

*Uses:* [[Tonelli's Theorem|§17.3]], [[§12 Measurable Functions#^prop-12-1|§12.1]]

> [!theorem] Lemma §17.9
> If $Z \subseteq \mathbb{R}^p$ has $m(Z) = 0$ and $E \subseteq \mathbb{R}^q$ is measurable with $m(E) < \infty$, then $Z \times E$ is a measure-zero subset of $\mathbb{R}^p \times \mathbb{R}^q$.

^lem-17-9

> [!proof]+ Proof of Lemma
> For any $\varepsilon > 0$, since $m(Z) = 0$, there exists an [[§9 Lebesgue Outer Measure#^def-9-3|L-covering]] $\{I_j\}_{j=1}^{\infty}$ of $Z$ (rectangles in $\mathbb{R}^p$) with $\sum_{j=1}^{\infty} |I_j| < \varepsilon$. Let $\{J_k\}_{k=1}^{\infty}$ be an L-covering of $E$ (rectangles in $\mathbb{R}^q$) with $\sum_{k=1}^{\infty} |J_k| \leq m(E) + 1$.
>
> Then $\{I_j \times J_k\}_{j,k \in \mathbb{N}}$ is an L-covering of $Z \times E$ in $\mathbb{R}^p \times \mathbb{R}^q$:
>
> $$
> m^*(Z \times E) \leq \sum_{j=1}^{\infty} \sum_{k=1}^{\infty} |I_j \times J_k| = \sum_{j=1}^{\infty} \sum_{k=1}^{\infty} |I_j|\,|J_k| = \left(\sum_{j=1}^{\infty} |I_j|\right)\!\left(\sum_{k=1}^{\infty} |J_k|\right) < \varepsilon\,(m(E) + 1).
> $$
>
> Since $\varepsilon > 0$ is arbitrary, $m^*(Z \times E) = 0$, so $Z \times E$ is [[§10 Lebesgue Measurable Sets#^ex-10-1|measurable]] with $m(Z \times E) = 0$.

^pf-17-9

*Uses:* [[§9 Lebesgue Outer Measure#^def-9-3|Def. §9.3]], [[§9 Lebesgue Outer Measure#^def-9-4|Def. §9.4]], [[§9 Lebesgue Outer Measure#^def-9-2|Def. §9.2]], [[§10 Lebesgue Measurable Sets#^ex-10-1|Ex. §10.1]]

> [!theorem] Theorem §17.8: Measurability of Product Sets
> Let $E_1 \subseteq \mathbb{R}^p$ be measurable and $E_2 \subseteq \mathbb{R}^q$ be measurable. Then $E_1 \times E_2$ is a measurable subset of $\mathbb{R}^p \times \mathbb{R}^q$, and:
>
> $$
> m(E_1 \times E_2) = m(E_1)\,m(E_2).
> $$

^thm-17-8

> [!proof]+ Proof
> **Step 1: Decomposition.** For any closed $F \subseteq \mathbb{R}^n$, write $F = \bigcup_{m=1}^{\infty} (F \cap [-m, m]^n)$, a countable union of bounded closed sets. For any measurable $E$, this gives $E = \bigcup_{m=1}^{\infty} F_m \cup Z$, where each $F_m$ is bounded and closed with $m(F_m) < \infty$, and $m(Z) = 0$ ([[Inner Regularity of Lebesgue Measure|§11.10]]).
>
> Applying this to $E_1$ and $E_2$: $E_1 = \bigcup_k F_k^{(1)} \cup Z_1$ and $E_2 = \bigcup_k F_k^{(2)} \cup Z_2$, with $F_k^{(i)}$ bounded closed and $m(Z_i) = 0$. Then:
>
> $$
> E_1 \times E_2 = \left(\bigcup_m \bigcup_k F_m^{(1)} \times F_k^{(2)}\right) \cup \left(\bigcup_m F_m^{(1)} \times Z_2\right) \cup \left(\bigcup_k Z_1 \times F_k^{(2)}\right) \cup (Z_1 \times Z_2).
> $$
>
> Each $F_m^{(1)} \times F_k^{(2)}$ is bounded and closed in $\mathbb{R}^p \times \mathbb{R}^q$, hence [[§11 Borel Sets and Measure Spaces#^cor-11-7|measurable]]. Their countable union is measurable. It suffices to show the remaining terms are measurable sets of measure zero.
>
> **Step 2: Null product lemma.**

^pf-17-8

> [!proof]+ Proof of [[§17a Applications of Tonelli's Theorem#^thm-17-8|Theorem §17.8]] (continued)
> **Step 3: Conclusion.** By the [[§17a Applications of Tonelli's Theorem#^lem-17-9|lemma]], $F_m^{(1)} \times Z_2$, $Z_1 \times F_k^{(2)}$, and $Z_1 \times Z_2$ all have measure zero (for the last, take $E = Z_2$ or use $Z_1 \times Z_2 \subseteq Z_1 \times [-k,k]^q$ and take $k \to \infty$). Their countable unions also have measure zero. Hence $E_1 \times E_2$ is measurable.
>
> **Step 4: The measure formula.** Apply [[Tonelli's Theorem|Tonelli]] to $\chi_{E_1 \times E_2}(x, y) = \chi_{E_1}(x)\,\chi_{E_2}(y)$:
>
> $$
> m(E_1 \times E_2) = \iint \chi_{E_1}(x)\,\chi_{E_2}(y)\,dx\,dy = \int_{\mathbb{R}^p} \chi_{E_1}(x) \left(\int_{\mathbb{R}^q} \chi_{E_2}(y)\,dy\right) dx = \int_{\mathbb{R}^p} \chi_{E_1}(x)\,m(E_2)\,dx = m(E_1)\,m(E_2).
> $$

^pf-17-8-cont

*Uses:* [[Inner Regularity of Lebesgue Measure|§11.10]], [[§11 Borel Sets and Measure Spaces#^cor-11-7|§11.7]], [[§17a Applications of Tonelli's Theorem#^lem-17-9|§17.9]], [[Properties of Lebesgue Outer Measure|§9.1]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]], [[Tonelli's Theorem|§17.3]]

> [!remark]- Connections
> - The case of rectangles is the definition of volume ([[§9 Lebesgue Outer Measure#^def-9-2|Def. §9.2]]); the theorem extends it to all measurable “rectangles” $E_1 \times E_2$.
> - Used in [[§17a Applications of Tonelli's Theorem#^cor-17-10|The Graph Has Measure Zero]], the [[§17a Applications of Tonelli's Theorem#^thm-17-11|Subgraph Theorem]], and [[§18b Differentiating the Integral#^prop-18-24|Measurability of f(x + t)]] ([[§18b Differentiating the Integral#^prop-18-24|§18.24]]).

> [!theorem] Corollary §17.10: The Graph Has Measure Zero
> Let $f$ be a real-valued measurable function on $E$, $E \in \mathcal{M}(\mathbb{R}^n)$. Define the **graph** of $f$ by:
>
> $$
> G_E(f) = \{(x, y) \in \mathbb{R}^{n+1} : x \in E,\; y = f(x)\}.
> $$
>
> Then $G_E(f)$ is a measurable subset of $\mathbb{R}^{n+1}$ with $m(G_E(f)) = 0$.

^cor-17-10

> [!proof]+ Proof
> First assume $m(E) < \infty$. For $\delta > 0$ and $k \in \mathbb{Z}$, define $E_k = \{x \in E : k\delta \leq f(x) < (k+1)\delta\}$. Each $E_k$ is [[§12 Measurable Functions#^prop-12-2|measurable]], and $E = \bigsqcup_{k=-\infty}^{\infty} E_k$ is a disjoint union. Then:
>
> $$
> G_E(f) \subseteq \bigcup_{k=-\infty}^{\infty} \bigl(E_k \times [k\delta, (k+1)\delta]\bigr).
> $$
>
> By the [[§17a Applications of Tonelli's Theorem#^thm-17-8|product set theorem]], each $E_k \times [k\delta, (k+1)\delta]$ is measurable with measure $m(E_k) \cdot \delta$. By [[Properties of Lebesgue Outer Measure|countable subadditivity]]:
>
> $$
> m(G_E(f)) \leq \sum_{k=-\infty}^{\infty} m(E_k) \cdot \delta = \delta \sum_{k=-\infty}^{\infty} m(E_k) = \delta \cdot m(E).
> $$
>
> Since $\delta > 0$ is arbitrary and $m(E) < \infty$, $m(G_E(f)) = 0$.
>
> For general $E$, write $E = \bigcup_{k=1}^{\infty} E_k$ with $m(E_k) < \infty$ (e.g., $E_k = E \cap B(0,k)$). Then $G_E(f) = \bigcup_k G_{E_k}(f)$, each with measure zero, so $m(G_E(f)) = 0$.

^pf-17-10

*Uses:* [[§12 Measurable Functions#^prop-12-2|§12.2]], [[§17a Applications of Tonelli's Theorem#^thm-17-8|§17.8]], [[Properties of Lebesgue Outer Measure|§9.1]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]], [[§10 Lebesgue Measurable Sets#^ex-10-1|Ex. §10.1]]

![[m551-17-2.svg]]
*Why a graph is null (here $n = 1$, $E = [0,1]$). Cut the range into bands $[k\delta, (k+1)\delta]$ (dotted). The part of the graph $G_E(f)$ (red) over $E_k = \{k\delta \leq f < (k+1)\delta\}$ lies in the box $E_k \times [k\delta, (k+1)\delta]$ of measure $\delta\, m(E_k)$. One band is highlighted: its $E_k$ (blue on the axis) has three pieces, since it is a level set rather than an interval. The boxes cover the graph, their total measure is $\delta \sum_k m(E_k)$, and $\delta$ can be taken arbitrarily small.*

> [!remark]- Connections
> - Jordan-content analogue in MATH 452: [[§15 Multivariable Integration#^def-15-13|Jordan Measure Zero]] (452 Def. §15.13).

> [!definition] Definition §17.3: Set Under the Graph
> Let $f$ be a non-negative measurable function on $E$, $E \in \mathcal{M}(\mathbb{R}^n)$. The **set under the graph** (or **subgraph**) of $f$ is:
>
> $$
> \underline{G}(f) = \{(x, y) \in \mathbb{R}^{n+1} : x \in E,\; 0 \leq y < f(x)\}.
> $$

^def-17-3

> [!theorem] Theorem §17.11: The Subgraph Theorem
> Let $f$ be a non-negative measurable function on $E$, $E \in \mathcal{M}(\mathbb{R}^n)$. Then $\underline{G}(f)$ is a measurable subset of $\mathbb{R}^{n+1}$ and:
>
> $$
> m(\underline{G}(f)) = \int_E f(x)\,dx.
> $$

^thm-17-11

> [!proof]+ Proof
> **Step 1: Simple functions.** If $f(x) = \sum_{j=1}^{p} a_j\,\chi_{A_j}(x)$ with $a_j \geq 0$ and $\{A_j\}$ pairwise disjoint measurable, $\bigcup A_j = E$ ([[§12b Simple Functions and Modes of Convergence#^prop-12-13|§12.13]]), then:
>
> $$
> \underline{G}(f) = \bigcup_{j=1}^{p} A_j \times [0, a_j),
> $$
>
> which is measurable (finite union of [[§17a Applications of Tonelli's Theorem#^thm-17-8|product sets]]). Its measure is:
>
> $$
> m(\underline{G}(f)) = \sum_{j=1}^{p} m(A_j) \cdot a_j = \int_E f\,dx.
> $$
>
> **Step 2: General non-negative measurable functions.** Choose simple $\varphi_k \nearrow f$ ([[Simple Function Approximation Theorem|§12.14]]). We claim $\underline{G}(f) = \bigcup_{k=1}^{\infty} \underline{G}(\varphi_k)$.
>
> $(\supseteq)$ is clear: if $(x, y) \in \underline{G}(\varphi_k)$, i.e., $0 \leq y < \varphi_k(x) \leq f(x)$, then $(x, y) \in \underline{G}(f)$.
>
> $(\subseteq)$: Let $(x, y) \in \underline{G}(f)$, i.e., $x \in E$ and $0 \leq y < f(x)$. Since $\lim_{k \to \infty} \varphi_k(x) = f(x) > y$, there exists $m \in \mathbb{N}$ such that $\varphi_m(x) > y$, so $(x, y) \in \underline{G}(\varphi_m)$.
>
> By Step 1, each $\underline{G}(\varphi_k)$ is measurable, so $\underline{G}(f) = \bigcup_k \underline{G}(\varphi_k)$ is measurable. Moreover, $\underline{G}(\varphi_k) \subseteq \underline{G}(\varphi_{k+1})$ (since $\varphi_k \leq \varphi_{k+1}$), so by [[Continuity of Measure|continuity of measure from below]]:
>
> $$
> m(\underline{G}(f)) = \lim_{k \to \infty} m(\underline{G}(\varphi_k)) = \lim_{k \to \infty} \int_E \varphi_k\,dx = \int_E f\,dx,
> $$
>
> where the last equality uses [[Monotone Convergence Theorem (Lebesgue)|MCT]].
>
> *Alternative via Tonelli*: $m(\underline{G}(f)) = \iint_{\mathbb{R}^{n+1}} \chi_{\underline{G}(f)}(x, y)\,dx\,dy = \int_E \left(\int_{\mathbb{R}} \chi_{[0, f(x))}(y)\,dy\right) dx = \int_E f(x)\,dx$.

^pf-17-11

*Uses:* [[§12b Simple Functions and Modes of Convergence#^prop-12-13|§12.13]], [[§17a Applications of Tonelli's Theorem#^thm-17-8|§17.8]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]], [[§14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]], [[Simple Function Approximation Theorem|§12.14]], [[Continuity of Measure|§11.12]], [[Monotone Convergence Theorem (Lebesgue)|§14.4]], [[Tonelli's Theorem|§17.3]]

> [!remark]- Connections
> - “Integral = area under the graph” is the MATH 451 picture of the Riemann integral via [[§32 The Definition of the Riemann Integral#^def-32-1|upper and lower sums]]; here it becomes a theorem about Lebesgue measure in $\mathbb{R}^{n+1}$.
> - Computational version: volume under a graph as a double integral, [[§98 Double Integrals Over Rectangles#^thm-98-2|Calc Thm. §98.2]] (with worked examples).

> [!theorem] Theorem §17.12: Converse: Measurable Subgraph Implies Measurable Function
> Let $f$ be a non-negative real-valued function on $E$, $E \in \mathcal{M}(\mathbb{R}^n)$. If $\underline{G}(f)$ is measurable in $\mathbb{R}^{n+1}$, then $f$ is a measurable function on $E$.

^thm-17-12

> [!remark] Remark
> This is left as an exercise. *Hint*: For any $c \geq 0$, $\{x \in E : f(x) > c\} = \{x \in \mathbb{R}^n : (x, c) \in \underline{G}(f)\}$ is a cross-section of $\underline{G}(f)$ at height $y = c$, which by the [[§17 Invariance Properties and Fubini's Theorem#^thm-17-4|Cross-Section Theorem]] (with the roles of the factors exchanged) is measurable for a.e. $c$. For the remaining $c$, choose such good $c_k \downarrow c$ (the good values are dense) and use $\{f > c\} = \bigcup_k \{f > c_k\}$.

^rem-17-4

> [!definition] Definition §17.4: Distribution Function
> Let $f$ be a measurable function on $E$, $E \in \mathcal{M}$. The **distribution function** of $f$ is:
>
> $$
> f^*(\lambda) = m\{x \in E : |f(x)| > \lambda\}, \qquad \lambda \in \mathbb{R}.
> $$
>
> Note that $f^*$ is a decreasing function of $\lambda$.

^def-17-4

> [!theorem] Theorem §17.13: Layer Cake Formula (Cavalieri's Principle)
> Let $f$ be a measurable function on $E$, $E \in \mathcal{M}(\mathbb{R}^n)$. Then for all $1 \leq p < \infty$:
>
> $$
> \int_E |f(x)|^p\,dx = \int_0^{\infty} p\,\lambda^{p-1}\,m\{x \in E : |f(x)| > \lambda\}\,d\lambda = \int_0^{\infty} p\,\lambda^{p-1}\,f^*(\lambda)\,d\lambda.
> $$

^thm-17-13

> [!proof]+ Proof
> The key idea is to express the superlevel set measure as an integral, then apply Tonelli to swap the order of integration.
>
> **The level set measure as an integral:**
>
> $$
> m\{x \in E : |f(x)| > \lambda\} = \int_E \chi_{\{x \in E : |f(x)| > \lambda\}}(x)\,dx.
> $$
>
> **The right side:**
>
> $$
> \text{RHS} = \int_0^{\infty} p\,\lambda^{p-1} \int_E \chi_{\{|f(x)| > \lambda\}}(x)\,dx\,d\lambda.
> $$
>
> Define $F(x, \lambda) = p\,\lambda^{p-1}\,\chi_{\{(x, \lambda)\,:\, x \in E,\; 0 \leq \lambda < |f(x)|\}}$. Then $F$ is non-negative and measurable on $\mathbb{R}^n \times \mathbb{R}$ ([[§17a Applications of Tonelli's Theorem#^thm-17-11|§17.11]]).
>
> By [[Tonelli's Theorem|Tonelli's theorem]] (swapping order of integration):
>
> $$
> \begin{aligned}
> \int_0^{\infty} p\,\lambda^{p-1} \int_E \chi_{\{|f(x)| > \lambda\}}\,dx\,d\lambda &= \iint_{\mathbb{R}^{n+1}} F(x, \lambda)\,dx\,d\lambda \\
> &= \int_E \left(\int_{\mathbb{R}} F(x, \lambda)\,d\lambda\right) dx \\
> &= \int_E \chi_E(x) \int_0^{|f(x)|} p\,\lambda^{p-1}\,d\lambda\,dx \\
> &= \int_E \chi_E(x)\,|f(x)|^p\,dx = \int_E |f(x)|^p\,dx.
> \end{aligned}
> $$

^pf-17-13

*Uses:* [[Tonelli's Theorem|§17.3]], [[§17a Applications of Tonelli's Theorem#^thm-17-11|§17.11]], [[Riemann Integrable Implies Lebesgue Integrable|§15.10]], [[Fundamental Theorem of Calculus|451 §34.1]]

> [!remark] Remark: Interpretation
> When $p = 1$, the formula reduces to:
>
> $$
> \int_E |f(x)|\,dx = \int_0^{\infty} m\{x \in E : |f(x)| > \lambda\}\,d\lambda = \int_0^{\infty} f^*(\lambda)\,d\lambda.
> $$
>
> This says: the integral of $|f|$ equals the “area under the distribution function curve.” Geometrically, instead of slicing vertically (integrating $|f|$ over $x$), we slice horizontally (integrating the measure of superlevel sets over $\lambda$). This is exactly the Cavalieri principle from calculus, made rigorous via Tonelli.
>
> The layer cake formula is the foundation for defining $L^p$ norms ([[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-new2|Def. §19.6]]) in terms of distribution functions, and is crucial in interpolation theory and harmonic analysis.

^rem-17-5

![[m551-17-3.svg]]
*The layer cake formula for $p = 1$, with $E = [0,1]$. Slicing the region under $|f|$ (blue) horizontally at height $\lambda$ cuts out the superlevel set $\{|f| > \lambda\}$ (red, left); its measure is the value $f^{\ast}(\lambda)$ of the distribution function (red segment, right). Integrating the slice lengths over $\lambda$ gives the area under $f^{\ast}$, which is the area under $|f|$: Tonelli on the subgraph, sliced the other way.*

> [!remark]- Connections
> - The $p = 1$ case is the [[§17a Applications of Tonelli's Theorem#^thm-17-11|Subgraph Theorem]] read with horizontal slices, i.e. the [[§17a Applications of Tonelli's Theorem#^thm-17-7|Cross-Section Theorem]] applied to $\underline{G}(\vert f\vert)$ in the other variable.
> - The $L^p$ spaces it feeds into: [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-5|Def. §19.5]].
