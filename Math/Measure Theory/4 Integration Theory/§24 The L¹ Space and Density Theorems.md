---
type: section
subject: "[[Measure Theory]]"
chapter: 4
section: 24
tags: [measure-theory, math551]
---
← [[§23 The Dominated Convergence Theorem]] · ↑ [[· 4 Integration Theory]] · [[§25 Invariance Properties and Fubini's Theorem]] →

## Absolute Continuity of the Integral

> [!theorem] Lemma §24.1
> Let $f \in L(E)$. Then there exists a sequence of bounded measurable functions $f_k \in L(E)$ with $|f_k(x)| \leq |f(x)|$ for all $x \in E$ and $\lim_{k \to \infty} \int_E |f_k - f|\,dx = 0$.

^lem-24-1

> [!proof]+ Proof of Lemma
> Define:
>
> $$
> f_k(x) = \begin{cases} f(x) & \text{if } |f(x)| \leq k, \\ k & \text{if } f(x) > k, \\ -k & \text{if } f(x) < -k. \end{cases}
> $$
>
> Then $|f_k(x)| \leq k$ (bounded), $|f_k(x)| \leq |f(x)|$ (so $|f_k| \in L(E)$), and $f_k(x) \to f(x)$ pointwise. Since $|f_k - f| \leq 2|f| \in L(E)$, by [[Dominated Convergence Theorem|DCT]]: $\int_E |f_k - f|\,dx \to 0$.

^pf-24-1

*Uses:* [[§22 The General Lebesgue Integral#^prop-22-1|§22.1]], [[Dominated Convergence Theorem|§23.3]]

![[m551-16-1.svg]]
*Truncation at height $k$: $f_k$ (blue) agrees with $f$ (gray) where $|f| \leq k$ and is clipped to $\pm k$ elsewhere, so $f_k$ is bounded and $|f_k| \leq |f|$. The red area is $\int_E |f - f_k|$; it sits over $\{|f| > k\}$ and tends to $0$ by the DCT with dominator $2|f|$. In [[§24 The L¹ Space and Density Theorems#^thm-24-2|Theorem §24.2]] the bounded part is small on small sets because $\int_e |f_k| \leq k\, m(e)$, and the red remainder is small everywhere.*

> [!theorem] Theorem §24.2: Absolute Continuity of the Integral
> Let $f \in L(E)$, $E \in \mathcal{M}$, $E \subseteq \mathbb{R}^n$. Then for every $\varepsilon > 0$, there exists $\delta > 0$ such that for all $e \subseteq E$, $e \in \mathcal{M}$:
>
> $$
> m(e) < \delta \implies \int_e |f(x)|\,dx < \varepsilon.
> $$

^thm-24-2

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

^pf-24-2

*Uses:* [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[§20 The Lebesgue Integral for Simple Functions#^def-20-1|Def. §20.1]]

> [!proof]+ Proof of [[§24 The L¹ Space and Density Theorems#^thm-24-2|Theorem §24.2]] (continued)
> Now let $\varepsilon > 0$. By the [[§24 The L¹ Space and Density Theorems#^lem-24-1|lemma]], choose $k$ such that $\int_E |f_k - f|\,dx < \varepsilon/2$. Since $|f_k|$ is bounded (by $k$), by Step 1 there exists $\delta > 0$ such that $m(e) < \delta$ implies $\int_e |f_k|\,dx < \varepsilon/2$.
>
> For any measurable $e \subseteq E$ with $m(e) < \delta$:
>
> $$
> \int_e |f|\,dx = \int_e |f| - |f_k| + |f_k|\,dx \leq \int_e \bigl||f| - |f_k|\bigr|\,dx + \int_e |f_k|\,dx.
> $$
>
> Since $\bigl||f(x)| - |f_k(x)|\bigr| \leq |f(x) - f_k(x)|$ (reverse [[§3 The Set ℝ of Real Numbers#^thm-3-3|triangle inequality]]):
>
> $$
> \int_e |f|\,dx \leq \int_e |f - f_k|\,dx + \int_e |f_k|\,dx \leq \int_E |f - f_k|\,dx + \int_e |f_k|\,dx < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
> $$

^pf-24-2-cont

*Uses:* [[§24 The L¹ Space and Density Theorems#^lem-24-1|§24.1]], [[§22 The General Lebesgue Integral#^thm-22-2|§22.2]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[§20 The Lebesgue Integral for Simple Functions#^cor-20-5|§20.5]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]]

> [!remark]- Connections
> - Gives that $x \mapsto \int_a^x g$ is absolutely continuous ([[§31 Absolute Continuity#^def-31-1|Def. §31.1]], [[§31 Absolute Continuity#^thm-31-2|Theorem §31.2]]); compare uniform continuity: [[§31 Absolute Continuity#^rem-31-7|Rem. §18.7]], [[§19 Uniform Continuity#^def-19-1|451 Def. §19.1]].
> - In the language of [[§21 Consequences of the Monotone Convergence Theorem#^def-21-1|Def. §21.1]]: the measure $\nu(e) = \int_e |f|$ is small on sets of small Lebesgue measure.

> [!theorem] Theorem §24.3: Tail Decay of the Integral
> Let $f \in L(E)$. Then for every $\varepsilon > 0$, there exists $R > 0$ such that for all $r > R$:
>
> $$
> \int_{E \cap B(0,r)^c} |f(x)|\,dx < \varepsilon,
> $$
>
> where $B(0, r) = \{x \in \mathbb{R}^n : |x| < r\}$.

^thm-24-3

> [!proof]+ Proof
> Define $f_m(x) = f(x)$ if $|x| < m$ and $f_m(x) = 0$ if $|x| \geq m$, for $x \in E$. Then $f_m \to f$ pointwise and $|f_m| \leq |f| \in L(E)$. By [[Dominated Convergence Theorem|DCT]], $\int_E |f_m - f|\,dx \to 0$. Since $f - f_m = f\,\chi_{B(0,m)^c}$, we have $\int_{E \cap B(0,m)^c} |f|\,dx \to 0$ as $m \to \infty$ through the integers. Choose an integer $R$ with $\int_{E \cap B(0,R)^c} |f|\,dx < \varepsilon$. For real $r > R$ we have $B(0,r)^c \subseteq B(0,R)^c$, so by [[§20 The Lebesgue Integral for Simple Functions#^cor-20-5|domain monotonicity]] $\int_{E \cap B(0,r)^c} |f|\,dx \leq \int_{E \cap B(0,R)^c} |f|\,dx < \varepsilon$.

^pf-24-3

*Uses:* [[Dominated Convergence Theorem|§23.3]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-4|§20.4]], [[§20 The Lebesgue Integral for Simple Functions#^cor-20-5|§20.5]]

> [!remark]- Connections
> - Together with [[§24 The L¹ Space and Density Theorems#^thm-24-2|Theorem §24.2]], these are the two ways an integrable function can be “cut down” (small sets, far-away sets).
> - Compare the MATH 451 improper integral on $[a, \infty)$: [[§36 Improper Integrals#^def-36-1|451 Def. §36.1]].

## The $L^1$ Space

> [!definition] Definition §24.1: $L^1$ Space
> Let $E \in \mathcal{M}$, $E \subseteq \mathbb{R}^n$. Define:
>
> $$
> L^1(E) = L(E) = \left\{f: E \to \mathbb{R} \cup \{\pm\infty\} \;\middle|\; f \text{ measurable},\; \int_E |f|\,dx < \infty\right\}.
> $$

^def-24-1

> [!remark]- Connections
> - The case $p = 1$ of [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-6|Def. §34.6]] ($L^p$ spaces). Same as $L(E)$ of [[§22 The General Lebesgue Integral#^def-22-1|Def. §22.1]] by [[§22 The General Lebesgue Integral#^rem-22-1|Rem. §15.1]].

> [!definition] Definition §24.2: $L^1$ Norm
> For $f \in L^1(E)$, the **$L^1$ norm** is:
>
> $$
> \|f\|_{L^1(E)} = \|f\|_1 = \int_E |f(x)|\,dx.
> $$

^def-24-2

> [!theorem] Theorem §24.4: $L^1$ is a Normed Vector Space
> Let $f, g \in L^1(E)$ and $a, b \in \mathbb{R}$. Then:
> - (i) $af + bg \in L^1(E)$.
> - (ii) $\|af\|_1 = |a|\,\|f\|_1$.
> - (iii) $\|f + g\|_1 \leq \|f\|_1 + \|g\|_1$  (triangle inequality).
> - (iv) $\|f\|_1 = 0 \iff f = 0$ a.e. on $E$.
>
> Thus $L^1(E)$ is a normed vector space (identifying functions that agree a.e.).

^thm-24-4

> [!remark]- Connections
> - (i)–(ii) are [[§22 The General Lebesgue Integral#^thm-22-2|Theorem §22.2]], (iii) is [[§22 The General Lebesgue Integral#^prop-22-3|Proposition §22.3]], (iv) is [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|Proposition §21.4]] with [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-2|§21.2]].
> - Norm axioms: [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-2|Def. §34.2]]; the linear-algebra model is [[§20 Inner Products and Norms#^ladr-6-9|LADR 6.9]] and the [[Triangle inequality]] (LADR 6.17), though the $L^1$ norm does not come from an inner product. Generalized in [[§35 Lᵖ as a Banach Space#^thm-35-3|Theorem §35.3]].

> [!definition] Definition §24.3: $L^1$ Metric
> Define $d(f, g) = \|f - g\|_1 = \int_E |f - g|\,dx$. Then $d$ is a [[§12 Metric Topology#^def-12-1|metric]] on $L^1(E)$ (with the convention that $f = g$ if $f = g$ a.e.), and $(L^1(E), d)$ is a metric space.

^def-24-3

> [!remark]- Connections
> - Metric spaces in MATH 451: [[§13 Some Topological Concepts in Metric Spaces#^def-13-1|451 Def. §13.1]]; normed $\Rightarrow$ metric in general: [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-1|Proposition §34.1]].
> - $(L^1(E), d)$ is complete by [[Riesz–Fischer Theorem|Riesz–Fischer]] ([[§35 Lᵖ as a Banach Space#^thm-35-11|§35.11]]).

> [!definition] Definition §24.4: Convergence in $L^1$
> We say $f_k \to f$ in $L^1(E)$ if $\lim_{k \to \infty} \|f_k - f\|_1 = \lim_{k \to \infty} \int_E |f_k - f|\,dx = 0$.

^def-24-4

> [!remark]- Connections
> - The DCT yields $L^1$ convergence: [[§23 The Dominated Convergence Theorem#^rem-23-4|Rem. §15.4]].

## Density of Simple Functions in $L^1$

> [!theorem] Theorem §24.5: Simple Functions are Dense in $L^1$
> Let $f \in L^1(E)$. Then there exists a sequence of simple functions $\{\varphi_k\}$ with $|\varphi_k(x)| \leq |f(x)|$ for all $x \in E$ and:
>
> $$
> \lim_{k \to \infty} \|\varphi_k - f\|_1 = \lim_{k \to \infty} \int_E |\varphi_k(x) - f(x)|\,dx = 0.
> $$

^thm-24-5

> [!proof]+ Proof
> By the [[§17 Simple Functions and Modes of Convergence#^thm-17-3|Simple Function Approximation Theorem]], for any measurable $f$ there exists a sequence of simple functions $\varphi_k$ with $|\varphi_k(x)| \leq |f(x)|$ for all $x \in E$ and $\varphi_k(x) \to f(x)$ pointwise. Since $|\varphi_k - f| \leq 2|f| \in L^1(E)$, by [[Dominated Convergence Theorem|DCT]]: $\int_E |\varphi_k - f|\,dx \to 0$.

^pf-24-5

*Uses:* [[§17 Simple Functions and Modes of Convergence#^thm-17-3|§17.3]], [[Dominated Convergence Theorem|§23.3]]

## Density of Step Functions in $L^1$

> [!theorem] Theorem §24.6: Step Functions are Dense in $L^1$
> Let $f \in L^1(E)$. Then for every $\varepsilon > 0$, there exists a [[§23 The Dominated Convergence Theorem#^def-23-1|step function]] $\psi$ on $\mathbb{R}^n$ such that $\|f - \psi\|_1 < \varepsilon$.
>
> (Equivalently, there exist step functions $\psi_k$ with $\|\psi_k - f\|_1 \to 0$.)

^thm-24-6

> [!proof]+ Proof
> **Step 1: Approximate $\chi_S$ by step functions.** Let $S \in \mathcal{M}$ with $m(S) < \infty$. We show that for every $\varepsilon > 0$, there exists a step function $\psi$ with $\|\chi_S - \psi\|_1 < \varepsilon$.
>
> *Observation*: For $E_1, E_2 \in \mathcal{M}$, $|\chi_{E_1}(x) - \chi_{E_2}(x)| = \chi_{E_1 \setminus E_2}(x) + \chi_{E_2 \setminus E_1}(x)$, so:
>
> $$
> \int_{\mathbb{R}^n} |\chi_{E_1} - \chi_{E_2}|\,dx = m(E_1 \setminus E_2) + m(E_2 \setminus E_1) = m(E_1 \triangle E_2).
> $$
>
> By the [[§13 Approximation and Continuity of Measure#^thm-13-6|approximation theorem]] ([[§12 Borel Sets and Measure Spaces|§12]]), for any $\varepsilon > 0$ there exist rectangles $R_1, \ldots, R_p$ with $m(S \triangle \bigcup_{j=1}^p R_j) < \varepsilon$. Since $\bigcup_{j=1}^p R_j$ can be written as a union of disjoint rectangles $I_1, \ldots, I_m$ (by splitting overlaps), $\chi_{\bigcup R_j} = \sum_{j=1}^{m} \chi_{I_j}$ is a step function. Thus $\|\chi_S - \psi\|_1 = m(S \triangle \bigcup R_j) < \varepsilon$.
>
> **Step 2: Simple functions $\to$ step functions.** Any simple function $\varphi = \sum a_j \chi_{S_j}$ (with $m(S_j) < \infty$) can be approximated by step functions: approximate each $\chi_{S_j}$ by a step function $\psi_j$ with $\|\chi_{S_j} - \psi_j\|_1 < \varepsilon/(p\,\max|a_j|)$, then $\psi = \sum a_j \psi_j$ is a step function with $\|\varphi - \psi\|_1 < \varepsilon$.
>
> **Step 3: Combine.** Given $f \in L^1(E)$ and $\varepsilon > 0$: by [[§24 The L¹ Space and Density Theorems#^thm-24-5|density of simple functions]], choose $\varphi$ with $\|f - \varphi\|_1 < \varepsilon/2$. By Step 2, choose a step function $\psi$ with $\|\varphi - \psi\|_1 < \varepsilon/2$. Then $\|f - \psi\|_1 < \varepsilon$.

^pf-24-6

*Uses:* [[§13 Approximation and Continuity of Measure#^def-13-3|Def. §13.3]], [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|§21.1]], [[§20 The Lebesgue Integral for Simple Functions#^def-20-1|Def. §20.1]], [[§13 Approximation and Continuity of Measure#^thm-13-6|§13.6]], [[§10 Lebesgue Outer Measure#^def-10-1|Def. §10.1]], [[§24 The L¹ Space and Density Theorems#^thm-24-4|§24.4]], [[§24 The L¹ Space and Density Theorems#^thm-24-5|§24.5]]

![[m551-16-2.svg]]
*Step 1 in the plane: a measurable $S$ with $m(S) < \infty$ (blue boundary) is approximated by finitely many disjoint rectangles $I_1, \dots, I_m$ (gray grid). The step function $\psi = \chi_{\bigcup_j I_j}$ differs from $\chi_S$ exactly on the symmetric difference $S \triangle \bigcup_j I_j$ (red), so $\|\chi_S - \psi\|_1 = m(S \triangle \bigcup_j I_j) < \varepsilon$.*

> [!remark]- Connections
> - Step 1 is the Lebesgue relaxation of Jordan measurability ([[§20 Multivariable Integration#^def-20-7|452 Def. §20.7]]), which demands finite unions of squares approximating from inside *and* outside.
> - The MATH 451 Riemann integral is itself built from step functions: [[§32 The Definition of the Riemann Integral#^ex-32-2|451 Ex. §32.2]], [[§23 The Dominated Convergence Theorem#^rem-23-6|Rem. §15.6]].
> - Used in PDEs: the standard route to the Riemann–Lebesgue lemma (check step functions by direct integration, then approximate); its case of sectionally continuous functions on an interval is [[§16★ Proof of Convergence#^lem-16-3|341 Lemma §16.3]] (proved there from [[§15★ Mean Error and Convergence in Mean#^thm-15-3|Bessel's inequality]]), and it is one of the two analytic facts behind the Fourier integral theorem, [[§18 Fourier Integral#^thm-18-1|341 Thm. §18.1]].

## Density of Compactly Supported Continuous Functions

Recall ([[§17 Simple Functions and Modes of Convergence#^def-17-2|Definition §17.2]]): a function $g: \mathbb{R}^n \to \mathbb{R}$ is **compactly supported** if $\operatorname{supp} g = \overline{\{x : g(x) \neq 0\}}$ is compact (i.e., [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|bounded and closed]] in $\mathbb{R}^n$). Equivalently, $g(x) = 0$ outside some large ball. We write $C_c(\mathbb{R}^n)$ for the space of compactly supported continuous functions.

> [!theorem] Theorem §24.7: Compactly Supported Continuous Functions are Dense in $L^1$
> Let $f \in L^1(E)$. Then for every $\varepsilon > 0$, there exists a compactly supported continuous function $g$ on $\mathbb{R}^n$ such that $\|f - g\|_1 < \varepsilon$.

^thm-24-7

> [!proof]+ Proof
> By [[§24 The L¹ Space and Density Theorems#^thm-24-6|density of step functions]], it suffices to show: for any step function $\psi = \sum_{j=1}^{p} a_j\,\chi_{R_j}$ (with $\{R_j\}$ disjoint rectangles, $m(R_j) < \infty$) and any $\varepsilon > 0$, there exists a compactly supported continuous $g$ with $\|\psi - g\|_1 < \varepsilon$.
>
> By linearity, it suffices to show: for any rectangle $R$ with $m(R) < \infty$ and any $\varepsilon > 0$, there exists a compactly supported continuous $g$ with $\|\chi_R - g\|_1 < \varepsilon$.
>
> **Case $n = 1$**: Let $R = (a, b)$ (open; other types of intervals differ by null sets). Define:
>
> $$
> g(x) = \begin{cases} 1 & x \in (a+\varepsilon', b-\varepsilon'), \\ \text{linear} & x \in (a-\varepsilon', a+\varepsilon') \cup (b-\varepsilon', b+\varepsilon'), \\ 0 & x \leq a - \varepsilon' \text{ or } x \geq b + \varepsilon', \end{cases}
> $$
>
> where $0 < \varepsilon' < (b - a)/2$, so that $a + \varepsilon' < b - \varepsilon'$. Then $g$ is continuous, compactly supported, $0 \leq g \leq 1$, and $|g(x) - \chi_{(a,b)}(x)| \leq 1$, and $g - \chi_{(a,b)}$ vanishes outside the two transition intervals, of total length $4\varepsilon'$. Thus $\|\chi_R - g\|_1 \leq 4\varepsilon'$, so choose $\varepsilon' < \min\{\varepsilon/4, (b-a)/2\}$.
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
> Integrating (one variable at a time, which uses [[Tonelli's Theorem]] ([[§25 Invariance Properties and Fubini's Theorem#^thm-25-3|§25.3]]), proved later) and using $m(R_2) < \infty$ and $\|g_1\|_1 \leq \|\chi_{R_1}\|_1 + \|\chi_{R_1} - g_1\|_1 < m(R_1) + \varepsilon'$:
>
> $$
> \|\chi_R - g\|_1 \leq m(R_2)\,\|\chi_{R_1} - g_1\|_1 + \|g_1\|_1\,\|\chi_{R_2} - g_2\|_1 < \varepsilon'(m(R_2) + m(R_1) + \varepsilon').
> $$
>
> Choose $\varepsilon'$ small enough to make this $< \varepsilon$.
>
> **General $n$**: By induction, using the product decomposition $R = R_1 \times \cdots \times R_n$ and the same factorization argument.

^pf-24-7

*Uses:* [[§24 The L¹ Space and Density Theorems#^thm-24-6|§24.6]], [[§24 The L¹ Space and Density Theorems#^thm-24-4|§24.4]], [[§22 The General Lebesgue Integral#^prop-22-1|§22.1]], [[§17 Simple Functions and Modes of Convergence#^def-17-2|Def. §17.2]], [[§10 Lebesgue Outer Measure#^def-10-1|Def. §10.1]], [[Tonelli's Theorem|§25.3]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]]

![[m551-16-3.svg]]
*The case $n = 1$: the trapezoid $g$ (blue) is $0$ outside $(a - \varepsilon', b + \varepsilon')$, equal to $1$ on $(a + \varepsilon', b - \varepsilon')$, and linear in between, so it is continuous with compact support. It differs from $\chi_{(a,b)}$ (black; hollow dots mark the values not taken at $a$, $b$) only on the two transition intervals, of total length $4\varepsilon'$, and there by at most $1$ (red), so $\|\chi_{(a,b)} - g\|_1 \leq 4\varepsilon'$.*

> [!remark]- Connections
> - Continuous functions are closed under uniform limits ([[§24 Uniform Convergence#^thm-24-2|451 §24.2]], [[§17 Simple Functions and Modes of Convergence#^thm-17-4|§17.4]]), so the density holds only for the weaker $L^1$ distance (cf. [[§35 Lᵖ as a Banach Space#^rem-35-4|Rem. §19.4]]).
> - The $n = 2$ step integrates a product $\varphi(x)\,\chi_{R_2}(y)$ one variable at a time, an instance of [[Tonelli's Theorem]] ([[§25 Invariance Properties and Fubini's Theorem#^thm-25-3|§25.3]]), proved only later; the Riemann analogue is the MATH 452 [[Fubini's Theorem]].
> - Used for [[§25 Invariance Properties and Fubini's Theorem#^thm-25-2|Theorem §25.2]] (average continuity); $L^p$ version [[§35 Lᵖ as a Banach Space#^thm-35-12|Theorem §35.12]]. Topology version of compact = closed and bounded: [[Heine–Borel Theorem]] (590 §18.12).
> - For all $1 \le p < \infty$, with smooth compactly supported approximants: [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-4|556 Thm. §19.4]].

> [!remark] Remark: The Approximation Chain for $L^1$
> We have now established:
>
> $$
> C_c(\mathbb{R}^n) \;\longrightarrow\; \text{step functions} \;\longrightarrow\; \text{simple functions} \;\longrightarrow\; L^1(E),
> $$
>
> with each class dense in the next (in the $L^1$ norm): every function of a class is an $L^1$-limit of functions of the previous class. The classes are not nested (a continuous function is not a step function). Here $C_c(\mathbb{R}^n)$ denotes the compactly supported continuous functions on $\mathbb{R}^n$. This chain is fundamental for proving results about $L^1$ functions by first establishing them for nicer classes of functions.

^rem-24-1

> [!remark]- Connections
> - The $L^p$ chain: [[§35 Lᵖ as a Banach Space#^rem-35-4|Rem. §19.4]], [[§35 Lᵖ as a Banach Space#^cor-35-13|Corollary §35.13]] (separability).
