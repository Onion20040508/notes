---
type: section
subject: "[[Measure Theory]]"
chapter: 4
section: 17
tags: [measure-theory, math551]
---
← [[§16 The L¹ Space and Density Theorems]] · ↑ [[· 4 Integration Theory]] · [[§18 Differentiation Theory]] →

## Translation Invariance of the Lebesgue Integral

> [!theorem] Theorem §17.1: Translation Invariance
> Let $f \in L(\mathbb{R}^n)$. Then for every $h \in \mathbb{R}^n$, $f(x + h) \in L(\mathbb{R}^n)$ and:
>
> $$
> \int_{\mathbb{R}^n} f(x + h)\,dx = \int_{\mathbb{R}^n} f(x)\,dx.
> $$

^thm-17-1

> [!proof]+ Proof
> **Step 1: Characteristic functions.** Let $f(x) = \chi_E(x)$ for $E \in \mathcal{M}$. Then $f(x + h) = \chi_{E-h}(x)$ (where $E - h = \{x : x + h \in E\}$). Since $E - h \in \mathcal{M}$ and $m(E - h) = m(E)$ ([[§11b The Vitali Set and the Cantor Set#^lem-11-15|translation invariance of Lebesgue measure]]):
>
> $$
> \int_{\mathbb{R}^n} \chi_{E-h}\,dx = m(E - h) = m(E) = \int_{\mathbb{R}^n} \chi_E\,dx.
> $$
>
> The result extends to simple functions by [[§14 The Lebesgue Integral for Simple Functions#^prop-14-1|linearity]].
>
> **Step 2: General $f \in L(\mathbb{R}^n)$.** Write $f = f^+ - f^-$, where $f^+, f^- \geq 0$ are both in $L(\mathbb{R}^n)$ ([[§12a Limits and Positive Parts of Measurable Functions#^def-12-4|Def. §12.4]], [[§15 The General Lebesgue Integral#^def-15-1|Def. §15.1]]).
>
> *For $f^+$*: By the [[Simple Function Approximation Theorem|Simple Function Approximation Theorem]], there exists an increasing sequence of non-negative simple functions $\varphi_k \nearrow f^+$ pointwise. Then $\varphi_k(x + h) \nearrow f^+(x + h)$ pointwise (shifting preserves monotonicity and limits). Each $\varphi_k(\cdot + h)$ is a simple function (it is $\sum a_j \chi_{A_j - h}$, a linear combination of characteristic functions of translated sets), so by Step 1:
>
> $$
> \int_{\mathbb{R}^n} \varphi_k(x + h)\,dx = \int_{\mathbb{R}^n} \varphi_k(x)\,dx.
> $$
>
> Since $\varphi_k(x+h) \nearrow f^+(x+h)$ with $\varphi_k(x+h) \geq 0$, applying [[Monotone Convergence Theorem (Lebesgue)|MCT]] to the left side:
>
> $$
> \int_{\mathbb{R}^n} f^+(x + h)\,dx = \lim_{k \to \infty} \int_{\mathbb{R}^n} \varphi_k(x + h)\,dx.
> $$
>
> Applying MCT to the right side (with $\varphi_k \nearrow f^+$):
>
> $$
> \lim_{k \to \infty} \int_{\mathbb{R}^n} \varphi_k(x)\,dx = \int_{\mathbb{R}^n} f^+(x)\,dx.
> $$
>
> Combining: $\int_{\mathbb{R}^n} f^+(x+h)\,dx = \int_{\mathbb{R}^n} f^+(x)\,dx < \infty$, so $f^+(x+h) \in L(\mathbb{R}^n)$.
>
> *For $f^-$*: The identical argument (with $\psi_k \nearrow f^-$) gives $\int_{\mathbb{R}^n} f^-(x+h)\,dx = \int_{\mathbb{R}^n} f^-(x)\,dx < \infty$, so $f^-(x+h) \in L(\mathbb{R}^n)$.
>
> *Conclusion*: Since $f(x+h) = f^+(x+h) - f^-(x+h)$ with both parts in $L(\mathbb{R}^n)$, we have $f(x+h) \in L(\mathbb{R}^n)$ and:
>
> $$
> \int_{\mathbb{R}^n} f(x+h)\,dx = \int_{\mathbb{R}^n} f^+(x+h)\,dx - \int_{\mathbb{R}^n} f^-(x+h)\,dx = \int_{\mathbb{R}^n} f^+(x)\,dx - \int_{\mathbb{R}^n} f^-(x)\,dx = \int_{\mathbb{R}^n} f(x)\,dx.
> $$

^pf-17-1

*Uses:* [[§11b The Vitali Set and the Cantor Set#^lem-11-15|§11.15]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-1|§14.1]], [[§12a Limits and Positive Parts of Measurable Functions#^def-12-4|Def. §12.4]], [[§15 The General Lebesgue Integral#^def-15-1|Def. §15.1]], [[Simple Function Approximation Theorem|§12.14]], [[Monotone Convergence Theorem (Lebesgue)|§14.4]]

> [!remark]- Connections
> - The set-level statement: [[§9 Lebesgue Outer Measure#^prop-9-3|Translation Invariance of Outer Measure]] ([[§9 Lebesgue Outer Measure#^prop-9-3|§9.3]]) and [[§11b The Vitali Set and the Cantor Set#^lem-11-15|of Measure]] ([[§11b The Vitali Set and the Cantor Set#^lem-11-15|§11.15]]).
> - The Riemann analogue is the translation $u = x + h$ in the [[Change of Variables Formula (multiple integrals)]] (452), whose Jacobian is $1$.
> - Used in [[§17 Invariance Properties and Fubini's Theorem#^thm-17-2|Average Continuity]] and in the [[§18b Differentiating the Integral#^lem-18-25|Averaging Lemma]] ([[§18b Differentiating the Integral#^lem-18-25|§18.25]]).

## Average Continuity ($L^1$ Continuity of Translation)

> [!theorem] Theorem §17.2: Average Continuity
> Let $f \in L(\mathbb{R}^n)$. Then:
>
> $$
> \lim_{|h| \to 0} \int_{\mathbb{R}^n} |f(x + h) - f(x)|\,dx = 0.
> $$

^thm-17-2

> [!proof]+ Proof
> **Step 1: Compactly supported continuous functions.** Assume $f$ is compactly supported and continuous on $\mathbb{R}^n$, with $\operatorname{supp} f \subseteq B(0, R)$ for some $R > 0$.
>
> Since $f$ is uniformly continuous on $\mathbb{R}^n$ (continuous with compact support; [[§15 Compact Spaces#^rem-15-1|compact ⇒ uniformly continuous]]), for every $\varepsilon > 0$ there exists $\delta > 0$ with $\delta < 1$ such that $|h| < \delta$ implies $\sup_{x \in \mathbb{R}^n} |f(x+h) - f(x)| < \varepsilon / m(B(0, R+1))$.
>
> For $|h| < \delta < 1$, $\operatorname{supp} f(\cdot + h) \subseteq B(0, R+1)$, so:
>
> $$
> \int_{\mathbb{R}^n} |f(x+h) - f(x)|\,dx = \int_{B(0, R+1)} |f(x+h) - f(x)|\,dx \leq \int_{B(0, R+1)} \frac{\varepsilon}{m(B(0, R+1))}\,dx = \varepsilon.
> $$
>
> **Step 2: General $f \in L(\mathbb{R}^n)$.** For any $\varepsilon > 0$, by density of $C_c(\mathbb{R}^n)$ in $L^1$ ([[Continuous Functions of Compact Support are Dense in L¹|§16.7]]), choose $g \in C_c(\mathbb{R}^n)$ with $\int_{\mathbb{R}^n} |f(x) - g(x)|\,dx < \varepsilon$.
>
> Then:
>
> $$
> |f(x+h) - f(x)| \leq |f(x+h) - g(x+h)| + |g(x+h) - g(x)| + |g(x) - f(x)|.
> $$
>
> Integrating and using [[§17 Invariance Properties and Fubini's Theorem#^thm-17-1|translation invariance]] ($\int |f(x+h) - g(x+h)|\,dx = \int |f - g|\,dx$):
>
> $$
> \int_{\mathbb{R}^n} |f(x+h) - f(x)|\,dx \leq 2\int_{\mathbb{R}^n} |f - g|\,dx + \int_{\mathbb{R}^n} |g(x+h) - g(x)|\,dx < 2\varepsilon + \int_{\mathbb{R}^n} |g(x+h) - g(x)|\,dx.
> $$
>
> By Step 1, there exists $\delta > 0$ such that $|h| < \delta$ implies $\int |g(x+h) - g(x)|\,dx < \varepsilon$. Hence:
>
> $$
> |h| < \delta \implies \int_{\mathbb{R}^n} |f(x+h) - f(x)|\,dx < 3\varepsilon.
> $$

^pf-17-2

*Uses:* [[§15 Compact Spaces#^rem-15-1|590 Rem. §15.1]], [[Continuous Functions of Compact Support are Dense in L¹|§16.7]], [[§17 Invariance Properties and Fubini's Theorem#^thm-17-1|§17.1]], [[§15 The General Lebesgue Integral#^prop-15-3|§15.3]]

> [!remark] Remark
> Average continuity is a key example of the [[§16 The L¹ Space and Density Theorems#^rem-16-1|approximation chain]] strategy in action: prove the result for $C_c$ (where uniform continuity is available), then extend to $L^1$ by density.

^rem-17-1

> [!remark]- Connections
> - Uniform continuity on a compact set is the MATH 451 fact [[§19 Uniform Continuity#^thm-19-1|Uniform Continuity on Closed Bounded Intervals]] in one variable; the $\mathbb{R}^n$ version comes from compactness ([[Heine–Borel Theorem]]).
> - Used in the [[§18b Differentiating the Integral#^lem-18-25|Averaging Lemma]] ([[§18b Differentiating the Integral#^lem-18-25|§18.25]]), hence in [[§18b Differentiating the Integral#^thm-18-26|Differentiation of the Integral]] ([[§18b Differentiating the Integral#^thm-18-26|§18.26]]).

## Tonelli's Theorem: The Question

> [!remark] Remark: The Question
> For $f \in L(\mathbb{R}^n)$ with $\mathbb{R}^n = \mathbb{R}^p \times \mathbb{R}^q$ ($p + q = n$), we ask:
> - (i) For a.e. $x \in \mathbb{R}^p$, is $y \mapsto f(x, y)$ integrable over $\mathbb{R}^q$?
> - (ii) If so, is $F_f(x) = \int_{\mathbb{R}^q} f(x, y)\,dy$ in $L(\mathbb{R}^p)$?
> - (iii) Does $\int_{\mathbb{R}^p} \left(\int_{\mathbb{R}^q} f(x,y)\,dy\right)dx = \iint_{\mathbb{R}^n} f(x,y)\,dx\,dy$?

^rem-17-2

Tonelli's theorem, which answers these questions for non-negative $f$, is stated as [[§17 Invariance Properties and Fubini's Theorem#^thm-17-3|Theorem §17.3]] below, directly before its proof, once the Tonelli class and its closure properties are in place.

## The Tonelli Class and Its Closure Properties

> [!definition] Definition §17.1: Cross-Sections
> For a set $E \subseteq \mathbb{R}^p \times \mathbb{R}^q$, the **cross-section** at $x \in \mathbb{R}^p$ is:
>
> $$
> E_x = \{y \in \mathbb{R}^q : (x, y) \in E\}.
> $$

^def-17-1

> [!theorem] Theorem §17.4: Cross-Section Theorem
> Let $E \in \mathcal{M}$ in $\mathbb{R}^p \times \mathbb{R}^q$. Then:
> - (i) For a.e. $x \in \mathbb{R}^p$, $E_x \in \mathcal{M}$ in $\mathbb{R}^q$.
> - (ii) $x \mapsto m(E_x)$ is a measurable function of $x \in \mathbb{R}^p$.
> - (iii) $\displaystyle\int_{\mathbb{R}^p} m(E_x)\,dx = m(E)$.

^thm-17-4

![[m551-17-1.svg]]
*A cross-section: the vertical line over $x \in \mathbb{R}^p$ meets $E$ in $E_x$ (red; here two segments). The theorem says that integrating the sizes $m(E_x)$ over $x$ recovers $m(E)$ (Cavalieri's principle); it is Tonelli's theorem for $f = \chi_E$.*

> [!remark]- Connections
> - This is Tonelli applied to $\chi_E$: see [[§17a Applications of Tonelli's Theorem#^thm-17-7|Cross-Section Theorem (Restated)]] ([[§17a Applications of Tonelli's Theorem#^thm-17-7|§17.7]]) and its proof.
> - Its geometric content is Cavalieri's principle; compare the [[§17a Applications of Tonelli's Theorem#^thm-17-13|Layer Cake Formula]] ([[§17a Applications of Tonelli's Theorem#^thm-17-13|§17.13]]).
> - Computational version: volume by slicing, V = ∫ A(x) dx, [[§40 Volumes#^def-40-2|Calc Def. §40.2]] (with worked examples).

> [!definition] Definition §17.2: The Tonelli Class $\mathcal{F}$
> Define $\mathcal{F}$ to be the class of all non-negative measurable functions $f$ on $\mathbb{R}^n = \mathbb{R}^p \times \mathbb{R}^q$ satisfying conclusions (i), (ii), (iii) of [[Tonelli's Theorem|Tonelli's theorem]]. Tonelli's theorem states that $\mathcal{F}$ contains all non-negative measurable functions.

^def-17-2

> [!theorem] Lemma §17.5: Closure Properties of $\mathcal{F}$
> 1. **Scaling**: If $f \in \mathcal{F}$ and $a \geq 0$, then $af \in \mathcal{F}$.
> 2. **Subtraction**: If $f, g \in \mathcal{F}$, $g \in L(\mathbb{R}^n)$, and $f(x,y) - g(x,y) \geq 0$ for all $(x,y) \in \mathbb{R}^n$, then $f - g \in \mathcal{F}$.
> 3. **Increasing limits**: If $\{f_k\} \subset \mathcal{F}$ is increasing (i.e., $f_k \leq f_{k+1}$), then $\lim_{k \to \infty} f_k \in \mathcal{F}$.
> 4. **Decreasing limits**: If $\{f_k\} \subset \mathcal{F}$ is decreasing and $f_1 \in L(\mathbb{R}^n)$, then $\lim_{k \to \infty} f_k \in \mathcal{F}$.

^lem-17-5

> [!proof]+ Proof
> **(1)** is immediate from the definition (scale all three conclusions by $a$).
>
> **(2)** Assume $f, g \in \mathcal{F}$ and $g \in L(\mathbb{R}^n)$. Since $g \in \mathcal{F}$, there exists a null set $Z_1 \subseteq \mathbb{R}^p$ such that for all $x_0 \in \mathbb{R}^p \setminus Z_1$, $g(x_0, y)$ is measurable w.r.t. $y$, and $F_g$ is measurable with $\int F_g\,dx = \iint g < \infty$. Hence $F_g \in L(\mathbb{R}^p)$, so $F_g$ is [[§14a Consequences of the Monotone Convergence Theorem#^prop-14-10|a.e. finite]]: there exists $Z \supseteq Z_1$, $m(Z) = 0$, such that for all $x \in \mathbb{R}^p \setminus Z$, $g(x, y)$ is measurable w.r.t. $y$ and $0 \leq \int g(x,y)\,dy < \infty$.
>
> Similarly, $f \in \mathcal{F}$ gives a null set $Z_2$ outside which $f(x, y)$ is measurable w.r.t. $y$. Let $Z' = Z \cup Z_2$, $m(Z') = 0$.
>
> For $x \in \mathbb{R}^p \setminus Z'$: $f - g$ is measurable w.r.t. $y$, and $F_{f-g}(x) = F_f(x) - F_g(x)$ is well-defined ($F_g(x) < \infty$) and measurable. Finally:
>
> $$
> \int_{\mathbb{R}^p} F_{f-g}\,dx = \int F_f\,dx - \int F_g\,dx = \iint f - \iint g = \iint (f - g).
> $$
>
> **(3)** Let $f_k \in \mathcal{F}$ with $f_k \leq f_{k+1}$ and $f = \lim f_k$. For each $k$, there exists a null set $Z_k$ with $f_k(x_0, y)$ measurable w.r.t. $y$ for $x_0 \notin Z_k$. Let $Z = \bigcup Z_k$, $m(Z) = 0$.
>
> For $x_0 \notin Z$: $f(x_0, y) = \lim f_k(x_0, y)$ is [[§12a Limits and Positive Parts of Measurable Functions#^cor-12-8|measurable]] w.r.t. $y$. By [[Monotone Convergence Theorem (Lebesgue)|MCT]] in $y$: $F_f(x) = \lim F_{f_k}(x)$. Since $F_{f_k} \nearrow F_f$ with each $F_{f_k}$ measurable, $F_f$ is measurable. By MCT in $x$:
>
> $$
> \int F_f\,dx = \lim \int F_{f_k}\,dx = \lim \iint f_k = \iint f.
> $$
>
> **(4)** Let $f_k \in \mathcal{F}$ decreasing with $f_1 \in L$. Then $f_1 - f_k \nearrow f_1 - f$ is increasing in $\mathcal{F}$ (by (2)). By (3), $f_1 - f \in \mathcal{F}$. Then $f = f_1 - (f_1 - f) \in \mathcal{F}$ by (2).

^pf-17-5

*Uses:* [[§17 Invariance Properties and Fubini's Theorem#^def-17-2|Def. §17.2]], [[§14a Consequences of the Monotone Convergence Theorem#^prop-14-10|§14.10]], [[§15 The General Lebesgue Integral#^thm-15-2|§15.2]], [[Properties of Lebesgue Outer Measure|§9.1]], [[§12a Limits and Positive Parts of Measurable Functions#^cor-12-8|§12.8]], [[Monotone Convergence Theorem (Lebesgue)|§14.4]]

## Statement and Proof of Tonelli's Theorem

We now prove Tonelli's theorem using these closure properties. Each step requires only one or two properties.

> [!theorem] Theorem §17.3: Tonelli's Theorem
> Let $f$ be a non-negative measurable function on $\mathbb{R}^n = \mathbb{R}^p \times \mathbb{R}^q$, $n = p + q$. Then:
> - (i) For a.e. $x \in \mathbb{R}^p$, the function $y \mapsto f(x, y)$ is a measurable function of $y \in \mathbb{R}^q$.
> - (ii) The function $F_f(x) = \int_{\mathbb{R}^q} f(x, y)\,dy$ is a measurable function of $x \in \mathbb{R}^p$.
> - (iii) $\displaystyle\int_{\mathbb{R}^p} \left(\int_{\mathbb{R}^q} f(x, y)\,dy\right) dx = \iint_{\mathbb{R}^n} f(x, y)\,dx\,dy$.

^thm-17-3

> [!proof]+ Proof of Tonelli's Theorem
> We show every non-negative measurable function belongs to $\mathcal{F}$.
>
> **Step 1: Rectangles.** $\chi_I \in \mathcal{F}$ for any rectangle $I = I_1 \times I_2$. Direct: $\chi_I(x,y) = \chi_{I_1}(x)\,\chi_{I_2}(y)$, so $F(x) = m(I_2)\,\chi_{I_1}(x)$ and $\int F\,dx = m(I_1)\,m(I_2) = m(I)$.
>
> **Step 2: Open sets.** $\chi_O \in \mathcal{F}$ for any open $O \subseteq \mathbb{R}^n$. Write $O = \bigsqcup_{j=1}^{\infty} I_j$ (countable disjoint half-open rectangles by [[§7 Structure of Open Sets#^prop-7-3|§7]]). Then $\chi_O = \lim_{k \to \infty} \sum_{j=1}^{k} \chi_{I_j}$. Each partial sum is in $\mathcal{F}$ by Step 1, since $\mathcal{F}$ is closed under finite sums: if $f, g \in \mathcal{F}$, then off the union of their two null sets $(f+g)(x, \cdot)$ is measurable and $F_{f+g} = F_f + F_g$, and $\int F_{f+g}\,dx = \int F_f\,dx + \int F_g\,dx = \iint f + \iint g = \iint (f+g)$ by linearity of the integral of non-negative functions ([[§14a Consequences of the Monotone Convergence Theorem#^thm-14-8|Theorem §14.8]]). The sequence is increasing, so $\chi_O \in \mathcal{F}$ by property (3).
>
> **Step 3: $G_\delta$ sets.** $\chi_G \in \mathcal{F}$ for any $G_\delta$ set ([[§11a Approximation and Continuity of Measure#^def-11-8|Def. §11.8]]) $G$ with $m(G) < \infty$. Write $G = \bigcap_{k=1}^{\infty} U_k$ with $U_k$ open. Define $O_k = \bigcap_{j=1}^{k} U_j$ (open, decreasing, $\bigcap O_k = G$). WLOG $m(O_1) < \infty$. Then $\chi_{O_k} \searrow \chi_G$, each $\chi_{O_k} \in \mathcal{F}$ by Step 2, and $\chi_{O_1} \in L$. By property (4), $\chi_G \in \mathcal{F}$.
>
> **Step 4: Null sets.** $\chi_Z \in \mathcal{F}$ for any $Z$ with $m(Z) = 0$. Choose open $O_j \supseteq Z$ with $m(O_j) < 1/j$ ([[Outer Regularity of Lebesgue Measure|§11.8]]). Let $G_0 = \bigcap_j O_j$, a $G_\delta$ set with $G_0 \supseteq Z$ and $m(G_0) = 0$. By Step 3, $\chi_{G_0} \in \mathcal{F}$, so $\int_{\mathbb{R}^p} m((G_0)_x)\,dx = 0$, giving $m((G_0)_x) = 0$ a.e. ([[§14a Consequences of the Monotone Convergence Theorem#^prop-14-11|§14.11]]). Since $Z_x \subseteq (G_0)_x$, $m(Z_x) = 0$ a.e., so $\chi_Z \in \mathcal{F}$.
>
> **Step 5: Measurable sets with $m(E) < \infty$.** Write $E = G \setminus Z$ with $G$ a $G_\delta$ set, $m(Z) = 0$ ([[Outer Regularity of Lebesgue Measure|§11.8]]). Then $\chi_E = \chi_G - \chi_Z$, with $\chi_G \in \mathcal{F}$ (Step 3) and $\chi_Z \in \mathcal{F} \cap L$ (Step 4). By property (2), $\chi_E \in \mathcal{F}$.
>
> **Step 6: General measurable sets.** For $E \in \mathcal{M}$, let $E_k = E \cap B(0, k)$. Then $\chi_{E_k} \in \mathcal{F}$ (Step 5) and $\chi_{E_k} \nearrow \chi_E$. By property (3), $\chi_E \in \mathcal{F}$.
>
> **Step 7: Simple functions.** $\varphi = \sum a_j\,\chi_{A_j} \in \mathcal{F}$ by Step 6, property (1), and closure under finite sums (Step 2).
>
> **Step 8: General non-negative measurable functions.** Choose simple $\varphi_k \nearrow f$ ([[Simple Function Approximation Theorem|§12.14]]). Each $\varphi_k \in \mathcal{F}$ (Step 7). By property (3), $f \in \mathcal{F}$.

^pf-17-3

*Uses:* [[§17 Invariance Properties and Fubini's Theorem#^def-17-2|Def. §17.2]], [[§17 Invariance Properties and Fubini's Theorem#^lem-17-5|§17.5]], [[§14a Consequences of the Monotone Convergence Theorem#^thm-14-8|§14.8]], [[§7 Structure of Open Sets#^prop-7-3|§7.3]], [[§11a Approximation and Continuity of Measure#^def-11-8|Def. §11.8]], [[Outer Regularity of Lebesgue Measure|§11.8]], [[§14a Consequences of the Monotone Convergence Theorem#^prop-14-11|§14.11]], [[Simple Function Approximation Theorem|§12.14]]

> [!remark]- Connections
> - Riemann counterpart for non-negative integrands in MATH 452: [[§15 Multivariable Integration#^thm-15-12|Fubini–Tonelli: Non-negative Functions]] (452 §15.12).
> - Proved above ([[§17 Invariance Properties and Fubini's Theorem#^pf-17-3|Proof of Tonelli's Theorem]]) through the closure properties of the [[§17 Invariance Properties and Fubini's Theorem#^def-17-2|Tonelli class]].
> - Computational version for continuous functions on boxes: [[§98 Double Integrals Over Rectangles#^thm-98-3|Calc Thm. §98.3]] and [[§103 Triple Integrals#^thm-103-1|Calc Thm. §103.1]] (with worked examples).
> - Used in ODEs: an absolute bound on the wedge $0 \le \tau \le t$ makes the order of integration reversible in the convolution theorem for Laplace transforms, [[§26★ The Convolution Integral#^thm-26-2|331 Thm. §26.2]].
> - Used in PDEs: checking the integrability hypothesis of Fubini's theorem when the order of integration is reversed in [[§27 Infinite Rod#^thm-27-3|341 Thm. §27.3]] and [[§51★ Definition and Elementary Properties#^thm-51-6|341 Thm. §51.6]].

## Fubini's Theorem

> [!theorem] Theorem §17.6: Fubini's Theorem
> Let $f \in L(\mathbb{R}^n)$ where $\mathbb{R}^n = \mathbb{R}^p \times \mathbb{R}^q$, $n = p + q$. Then:
> - (i) For a.e. $x \in \mathbb{R}^p$, $f(x, \cdot) \in L(\mathbb{R}^q)$.
> - (ii) The function $F_f(x) = \int_{\mathbb{R}^q} f(x, y)\,dy$ (defined a.e.) is in $L(\mathbb{R}^p)$.
> - (iii) $\displaystyle\int_{\mathbb{R}^p} \left(\int_{\mathbb{R}^q} f(x, y)\,dy\right) dx = \iint_{\mathbb{R}^n} f(x, y)\,dx\,dy = \int_{\mathbb{R}^q} \left(\int_{\mathbb{R}^p} f(x, y)\,dx\right) dy$.

^thm-17-6

> [!proof]+ Proof
> **Step 1: Integrability of the slices.**
>
> Since $|f| = f^+ + f^- \geq 0$ is measurable ([[§12a Limits and Positive Parts of Measurable Functions#^prop-12-10|§12.10]]) and $\int_{\mathbb{R}^n} |f|\,dx\,dy < \infty$, apply [[Tonelli's Theorem|Tonelli's theorem]] to $|f|$:
>
> $$
> \int_{\mathbb{R}^p} \left(\int_{\mathbb{R}^q} |f(x, y)|\,dy\right) dx = \iint_{\mathbb{R}^n} |f(x, y)|\,dx\,dy < \infty.
> $$
>
> Since the left side is finite, the inner integral $\int_{\mathbb{R}^q} |f(x, y)|\,dy$ must be finite for a.e. $x \in \mathbb{R}^p$ (if it were $+\infty$ on a set of positive measure, the outer integral would be $+\infty$; [[§14a Consequences of the Monotone Convergence Theorem#^prop-14-10|§14.10]]). Therefore $f(x, \cdot) \in L(\mathbb{R}^q)$ for a.e. $x$. This proves (i).
>
> **Step 2: Apply Tonelli to $f^+$ and $f^-$ separately.**
>
> Both $f^+, f^- \geq 0$ are measurable, so Tonelli applies to each:
>
> *For $f^+$*: Tonelli gives that $x \mapsto \int_{\mathbb{R}^q} f^+(x,y)\,dy$ is measurable and:
>
> $$
> \int_{\mathbb{R}^p} \left(\int_{\mathbb{R}^q} f^+(x, y)\,dy\right) dx = \iint_{\mathbb{R}^n} f^+(x, y)\,dx\,dy.
> $$
>
> Since $f^+ \leq |f|$ and $\iint |f| < \infty$, we have $\iint f^+ < \infty$ ([[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]]), so $\int_{\mathbb{R}^q} f^+(x,y)\,dy < \infty$ for a.e. $x$ and $x \mapsto \int f^+\,dy$ is in $L(\mathbb{R}^p)$.
>
> *For $f^-$*: Identically, $x \mapsto \int_{\mathbb{R}^q} f^-(x,y)\,dy$ is measurable, in $L(\mathbb{R}^p)$, and:
>
> $$
> \int_{\mathbb{R}^p} \left(\int_{\mathbb{R}^q} f^-(x, y)\,dy\right) dx = \iint_{\mathbb{R}^n} f^-(x, y)\,dx\,dy.
> $$
>
> **Step 3: Subtract.**
>
> For a.e. $x$, both $\int f^+(x,y)\,dy$ and $\int f^-(x,y)\,dy$ are finite (by Step 1), so:
>
> $$
> F_f(x) = \int_{\mathbb{R}^q} f(x, y)\,dy = \int_{\mathbb{R}^q} f^+(x, y)\,dy - \int_{\mathbb{R}^q} f^-(x, y)\,dy
> $$
>
> is well-defined (no $\infty - \infty$ ambiguity). Since each term is measurable and in $L(\mathbb{R}^p)$, so is $F_f$. This proves (ii).
>
> Subtracting the two Tonelli equalities:
>
> $$
> \begin{aligned}
> \int_{\mathbb{R}^p} F_f(x)\,dx &= \int_{\mathbb{R}^p} \left(\int_{\mathbb{R}^q} f^+\,dy\right) dx - \int_{\mathbb{R}^p} \left(\int_{\mathbb{R}^q} f^-\,dy\right) dx \\
> &= \iint_{\mathbb{R}^n} f^+\,dx\,dy - \iint_{\mathbb{R}^n} f^-\,dx\,dy = \iint_{\mathbb{R}^n} f\,dx\,dy.
> \end{aligned}
> $$
>
> All subtractions are valid since every term is finite. This proves the first equality in (iii).
>
> The second equality in (iii) follows by applying the same argument with the roles of $x \in \mathbb{R}^p$ and $y \in \mathbb{R}^q$ interchanged.

^pf-17-6

*Uses:* [[Tonelli's Theorem|§17.3]], [[§12a Limits and Positive Parts of Measurable Functions#^prop-12-10|§12.10]], [[§14a Consequences of the Monotone Convergence Theorem#^prop-14-10|§14.10]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§15 The General Lebesgue Integral#^def-15-1|Def. §15.1]], [[§15 The General Lebesgue Integral#^thm-15-2|§15.2]]

> [!remark]- Connections
> - MATH 452 Riemann version: [[Fubini's Theorem]] (452 §15.8), for continuous $f$ on a rectangle, extended to [[§15 Multivariable Integration#^thm-15-9|Type I regions]] (452 §15.9).
> - Used for the volume of sheared rectangles in [[§18b Differentiating the Integral#^thm-18-22|Linear Maps Preserve Null Sets]] ([[§18b Differentiating the Integral#^thm-18-22|§18.22]]).
> - Computational version for continuous functions on boxes: [[§98 Double Integrals Over Rectangles#^thm-98-3|Calc Thm. §98.3]] and [[§103 Triple Integrals#^thm-103-1|Calc Thm. §103.1]] (with worked examples).
> - Used in ODEs: reversing the order of integration proves the algebraic properties of convolution, [[§26★ The Convolution Integral#^prop-26-1|331 Prop. §26.1]], and the convolution theorem $\mathcal{L}\{f * g\} = F(s)G(s)$, [[§26★ The Convolution Integral#^thm-26-2|331 Thm. §26.2]].
> - Used in PDEs: reversing the order of integration turns the Fourier-integral solution of the infinite rod into heat-kernel form, [[§27 Infinite Rod#^thm-27-3|341 Thm. §27.3]]; it also gives the convolution step when the heat equation is solved by Fourier transform, [[§15★ Complex Methods#^ex-15-4|341 Ex. §15.4]], and the Laplace transform of $f(t)/t$, [[§51★ Definition and Elementary Properties#^thm-51-6|341 Thm. §51.6]].

> [!remark] Remark: Why Integrability is Essential
> The hypothesis $f \in L(\mathbb{R}^n)$ (equivalently $\iint |f| < \infty$) cannot be dropped. Without it, the subtraction $\int f^+\,dy - \int f^-\,dy$ can be $\infty - \infty$, and the iterated integrals can depend on the order of integration. A classical counterexample ([[§15 Multivariable Integration#^ex-15-2|452 Ex. §15.2]]): on $[0,1]^2$, define $f(x,y) = \frac{x^2 - y^2}{(x^2 + y^2)^2}$. Then $\int_0^1\!\left(\int_0^1 f\,dy\right)dx = \pi/4$ but $\int_0^1\!\left(\int_0^1 f\,dx\right)dy = -\pi/4$.

^rem-17-3

Applications of Tonelli's theorem (product sets, graphs and subgraphs, the layer cake formula) continue in [[§17a Applications of Tonelli's Theorem]].
