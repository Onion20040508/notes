---
type: section
subject: "[[Measure Theory]]"
chapter: 4
section: 17
tags: [measure-theory, math551]
---
← [[§16 The L¹ Space and Density Theorems]] · ↑ [[4 Integration Theory]] · [[§18 Differentiation Theory]] →

## Translation Invariance of the Lebesgue Integral

> [!theorem] Theorem §17.1: Translation Invariance
> Let $f \in L(\mathbb{R}^n)$. Then for every $h \in \mathbb{R}^n$, $f(x + h) \in L(\mathbb{R}^n)$ and:
>
> $$
> \int_{\mathbb{R}^n} f(x + h)\,dx = \int_{\mathbb{R}^n} f(x)\,dx.
> $$

^thm-17-1

> [!proof]+ Proof
> **Step 1: Characteristic functions.** Let $f(x) = \chi_E(x)$ for $E \in \mathcal{M}$. Then $f(x + h) = \chi_{E-h}(x)$ (where $E - h = \{x : x + h \in E\}$). Since $E - h \in \mathcal{M}$ and $m(E - h) = m(E)$ ([[§11 Borel Sets and Measure Spaces#^lem-11-15|translation invariance of Lebesgue measure]]):
>
> $$
> \int_{\mathbb{R}^n} \chi_{E-h}\,dx = m(E - h) = m(E) = \int_{\mathbb{R}^n} \chi_E\,dx.
> $$
>
> The result extends to simple functions by [[§14 The Lebesgue Integral for Simple Functions#^prop-14-1|linearity]].
>
> **Step 2: General $f \in L(\mathbb{R}^n)$.** Write $f = f^+ - f^-$, where $f^+, f^- \geq 0$ are both in $L(\mathbb{R}^n)$ ([[§12 Measurable Functions#^def-12-4|Def. §12.4]], [[§15 The General Lebesgue Integral#^def-15-1|Def. §15.1]]).
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

*Uses:* [[§11 Borel Sets and Measure Spaces#^lem-11-15|§11.15]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-1|§14.1]], [[§12 Measurable Functions#^def-12-4|Def. §12.4]], [[§15 The General Lebesgue Integral#^def-15-1|Def. §15.1]], [[Simple Function Approximation Theorem|§12.14]], [[Monotone Convergence Theorem (Lebesgue)|§14.4]]

> [!remark]- Connections
> - The set-level statement: [[§9 Lebesgue Outer Measure#^prop-9-3|Translation Invariance of Outer Measure]] (§9.3) and [[§11 Borel Sets and Measure Spaces#^lem-11-15|of Measure]] (§11.15).
> - The Riemann analogue is the translation $u = x + h$ in the [[Change of Variables Formula (multiple integrals)]] (452), whose Jacobian is $1$.
> - Used in [[§17 Invariance Properties and Fubini's Theorem#^thm-17-2|Average Continuity]] and in the [[§18 Differentiation Theory#^lem-18-25|Averaging Lemma]] (§18.25).

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
> - Used in the [[§18 Differentiation Theory#^lem-18-25|Averaging Lemma]] (§18.25), hence in [[§18 Differentiation Theory#^thm-18-26|Differentiation of the Integral]] (§18.26).

## Tonelli's Theorem: Statement

> [!remark] Remark: The Question
> For $f \in L(\mathbb{R}^n)$ with $\mathbb{R}^n = \mathbb{R}^p \times \mathbb{R}^q$ ($p + q = n$), we ask:
> - (i) For a.e. $x \in \mathbb{R}^p$, is $y \mapsto f(x, y)$ integrable over $\mathbb{R}^q$?
> - (ii) If so, is $F_f(x) = \int_{\mathbb{R}^q} f(x, y)\,dy$ in $L(\mathbb{R}^p)$?
> - (iii) Does $\int_{\mathbb{R}^p} \left(\int_{\mathbb{R}^q} f(x,y)\,dy\right)dx = \iint_{\mathbb{R}^n} f(x,y)\,dx\,dy$?

^rem-17-2

> [!theorem] Theorem §17.3: Tonelli's Theorem
> Let $f$ be a non-negative measurable function on $\mathbb{R}^n = \mathbb{R}^p \times \mathbb{R}^q$, $n = p + q$. Then:
> - (i) For a.e. $x \in \mathbb{R}^p$, the function $y \mapsto f(x, y)$ is a measurable function of $y \in \mathbb{R}^q$.
> - (ii) The function $F_f(x) = \int_{\mathbb{R}^q} f(x, y)\,dy$ is a measurable function of $x \in \mathbb{R}^p$.
> - (iii) $\displaystyle\int_{\mathbb{R}^p} \left(\int_{\mathbb{R}^q} f(x, y)\,dy\right) dx = \iint_{\mathbb{R}^n} f(x, y)\,dx\,dy$.

^thm-17-3

> [!remark]- Connections
> - Riemann counterpart for non-negative integrands in MATH 452: [[§15 Multivariable Integration#^thm-15-12|Fubini–Tonelli: Non-negative Functions]] (452 §15.12).
> - Proved below ([[§17 Invariance Properties and Fubini's Theorem#^pf-17-3|Proof of Tonelli's Theorem]]) through the closure properties of the [[§17 Invariance Properties and Fubini's Theorem#^def-17-2|Tonelli class]].

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
> - This is Tonelli applied to $\chi_E$: see [[§17 Invariance Properties and Fubini's Theorem#^thm-17-7|Cross-Section Theorem (Restated)]] (§17.7) and its proof.
> - Its geometric content is Cavalieri's principle; compare the [[§17 Invariance Properties and Fubini's Theorem#^thm-17-13|Layer Cake Formula]] (§17.13).

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
> **(2)** Assume $f, g \in \mathcal{F}$ and $g \in L(\mathbb{R}^n)$. Since $g \in \mathcal{F}$, there exists a null set $Z_1 \subseteq \mathbb{R}^p$ such that for all $x_0 \in \mathbb{R}^p \setminus Z_1$, $g(x_0, y)$ is measurable w.r.t. $y$, and $F_g$ is measurable with $\int F_g\,dx = \iint g < \infty$. Hence $F_g \in L(\mathbb{R}^p)$, so $F_g$ is [[§14 The Lebesgue Integral for Simple Functions#^prop-14-10|a.e. finite]]: there exists $Z \supseteq Z_1$, $m(Z) = 0$, such that for all $x \in \mathbb{R}^p \setminus Z$, $g(x, y)$ is measurable w.r.t. $y$ and $0 \leq \int g(x,y)\,dy < \infty$.
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
> For $x_0 \notin Z$: $f(x_0, y) = \lim f_k(x_0, y)$ is [[§12 Measurable Functions#^cor-12-8|measurable]] w.r.t. $y$. By [[Monotone Convergence Theorem (Lebesgue)|MCT]] in $y$: $F_f(x) = \lim F_{f_k}(x)$. Since $F_{f_k} \nearrow F_f$ with each $F_{f_k}$ measurable, $F_f$ is measurable. By MCT in $x$:
>
> $$
> \int F_f\,dx = \lim \int F_{f_k}\,dx = \lim \iint f_k = \iint f.
> $$
>
> **(4)** Let $f_k \in \mathcal{F}$ decreasing with $f_1 \in L$. Then $f_1 - f_k \nearrow f_1 - f$ is increasing in $\mathcal{F}$ (by (2)). By (3), $f_1 - f \in \mathcal{F}$. Then $f = f_1 - (f_1 - f) \in \mathcal{F}$ by (2).

^pf-17-5

*Uses:* [[§17 Invariance Properties and Fubini's Theorem#^def-17-2|Def. §17.2]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-10|§14.10]], [[§15 The General Lebesgue Integral#^thm-15-2|§15.2]], [[Properties of Lebesgue Outer Measure|§9.1]], [[§12 Measurable Functions#^cor-12-8|§12.8]], [[Monotone Convergence Theorem (Lebesgue)|§14.4]]

We now prove Tonelli's theorem using these closure properties. Each step requires only one or two properties.

## Proof of Tonelli's Theorem

> [!proof]+ Proof of Tonelli's Theorem
> We show every non-negative measurable function belongs to $\mathcal{F}$.
>
> **Step 1: Rectangles.** $\chi_I \in \mathcal{F}$ for any rectangle $I = I_1 \times I_2$. Direct: $\chi_I(x,y) = \chi_{I_1}(x)\,\chi_{I_2}(y)$, so $F(x) = m(I_2)\,\chi_{I_1}(x)$ and $\int F\,dx = m(I_1)\,m(I_2) = m(I)$.
>
> **Step 2: Open sets.** $\chi_O \in \mathcal{F}$ for any open $O \subseteq \mathbb{R}^n$. Write $O = \bigsqcup_{j=1}^{\infty} I_j$ (countable disjoint half-open rectangles by [[§7 Structure of Open Sets#^prop-7-3|§7]]). Then $\chi_O = \lim_{k \to \infty} \sum_{j=1}^{k} \chi_{I_j}$. Each partial sum is in $\mathcal{F}$ by Step 1, since $\mathcal{F}$ is closed under finite sums: if $f, g \in \mathcal{F}$, then off the union of their two null sets $(f+g)(x, \cdot)$ is measurable and $F_{f+g} = F_f + F_g$, and $\int F_{f+g}\,dx = \int F_f\,dx + \int F_g\,dx = \iint f + \iint g = \iint (f+g)$ by linearity of the integral of non-negative functions ([[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|Theorem §14.8]]). The sequence is increasing, so $\chi_O \in \mathcal{F}$ by property (3).
>
> **Step 3: $G_\delta$ sets.** $\chi_G \in \mathcal{F}$ for any $G_\delta$ set ([[§11 Borel Sets and Measure Spaces#^def-11-8|Def. §11.8]]) $G$ with $m(G) < \infty$. Write $G = \bigcap_{k=1}^{\infty} U_k$ with $U_k$ open. Define $O_k = \bigcap_{j=1}^{k} U_j$ (open, decreasing, $\bigcap O_k = G$). WLOG $m(O_1) < \infty$. Then $\chi_{O_k} \searrow \chi_G$, each $\chi_{O_k} \in \mathcal{F}$ by Step 2, and $\chi_{O_1} \in L$. By property (4), $\chi_G \in \mathcal{F}$.
>
> **Step 4: Null sets.** $\chi_Z \in \mathcal{F}$ for any $Z$ with $m(Z) = 0$. Choose open $O_j \supseteq Z$ with $m(O_j) < 1/j$ ([[Outer Regularity of Lebesgue Measure|§11.8]]). Let $G_0 = \bigcap_j O_j$, a $G_\delta$ set with $G_0 \supseteq Z$ and $m(G_0) = 0$. By Step 3, $\chi_{G_0} \in \mathcal{F}$, so $\int_{\mathbb{R}^p} m((G_0)_x)\,dx = 0$, giving $m((G_0)_x) = 0$ a.e. ([[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|§14.11]]). Since $Z_x \subseteq (G_0)_x$, $m(Z_x) = 0$ a.e., so $\chi_Z \in \mathcal{F}$.
>
> **Step 5: Measurable sets with $m(E) < \infty$.** Write $E = G \setminus Z$ with $G$ a $G_\delta$ set, $m(Z) = 0$ ([[Outer Regularity of Lebesgue Measure|§11.8]]). Then $\chi_E = \chi_G - \chi_Z$, with $\chi_G \in \mathcal{F}$ (Step 3) and $\chi_Z \in \mathcal{F} \cap L$ (Step 4). By property (2), $\chi_E \in \mathcal{F}$.
>
> **Step 6: General measurable sets.** For $E \in \mathcal{M}$, let $E_k = E \cap B(0, k)$. Then $\chi_{E_k} \in \mathcal{F}$ (Step 5) and $\chi_{E_k} \nearrow \chi_E$. By property (3), $\chi_E \in \mathcal{F}$.
>
> **Step 7: Simple functions.** $\varphi = \sum a_j\,\chi_{A_j} \in \mathcal{F}$ by Step 6, property (1), and closure under finite sums (Step 2).
>
> **Step 8: General non-negative measurable functions.** Choose simple $\varphi_k \nearrow f$ ([[Simple Function Approximation Theorem|§12.14]]). Each $\varphi_k \in \mathcal{F}$ (Step 7). By property (3), $f \in \mathcal{F}$.

^pf-17-3

*Uses:* [[§17 Invariance Properties and Fubini's Theorem#^def-17-2|Def. §17.2]], [[§17 Invariance Properties and Fubini's Theorem#^lem-17-5|§17.5]], [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|§14.8]], [[§7 Structure of Open Sets#^prop-7-3|§7.3]], [[§11 Borel Sets and Measure Spaces#^def-11-8|Def. §11.8]], [[Outer Regularity of Lebesgue Measure|§11.8]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|§14.11]], [[Simple Function Approximation Theorem|§12.14]]

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
> Since $|f| = f^+ + f^- \geq 0$ is measurable ([[§12 Measurable Functions#^prop-12-10|§12.10]]) and $\int_{\mathbb{R}^n} |f|\,dx\,dy < \infty$, apply [[Tonelli's Theorem|Tonelli's theorem]] to $|f|$:
>
> $$
> \int_{\mathbb{R}^p} \left(\int_{\mathbb{R}^q} |f(x, y)|\,dy\right) dx = \iint_{\mathbb{R}^n} |f(x, y)|\,dx\,dy < \infty.
> $$
>
> Since the left side is finite, the inner integral $\int_{\mathbb{R}^q} |f(x, y)|\,dy$ must be finite for a.e. $x \in \mathbb{R}^p$ (if it were $+\infty$ on a set of positive measure, the outer integral would be $+\infty$; [[§14 The Lebesgue Integral for Simple Functions#^prop-14-10|§14.10]]). Therefore $f(x, \cdot) \in L(\mathbb{R}^q)$ for a.e. $x$. This proves (i).
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

*Uses:* [[Tonelli's Theorem|§17.3]], [[§12 Measurable Functions#^prop-12-10|§12.10]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-10|§14.10]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§15 The General Lebesgue Integral#^def-15-1|Def. §15.1]], [[§15 The General Lebesgue Integral#^thm-15-2|§15.2]]

> [!remark]- Connections
> - MATH 452 Riemann version: [[Fubini's Theorem]] (452 §15.8), for continuous $f$ on a rectangle, extended to [[§15 Multivariable Integration#^thm-15-9|Type I regions]] (452 §15.9).
> - Used for the volume of sheared rectangles in [[§18 Differentiation Theory#^thm-18-22|Linear Maps Preserve Null Sets]] (§18.22).

> [!remark] Remark: Why Integrability is Essential
> The hypothesis $f \in L(\mathbb{R}^n)$ (equivalently $\iint |f| < \infty$) cannot be dropped. Without it, the subtraction $\int f^+\,dy - \int f^-\,dy$ can be $\infty - \infty$, and the iterated integrals can depend on the order of integration. A classical counterexample ([[§15 Multivariable Integration#^ex-15-2|452 Ex. §15.2]]): on $[0,1]^2$, define $f(x,y) = \frac{x^2 - y^2}{(x^2 + y^2)^2}$. Then $\int_0^1\!\left(\int_0^1 f\,dy\right)dx = \pi/4$ but $\int_0^1\!\left(\int_0^1 f\,dx\right)dy = -\pi/4$.

^rem-17-3

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

> [!proof]+ Proof of Theorem §17.8 (continued)
> **Step 3: Conclusion.** By the [[§17 Invariance Properties and Fubini's Theorem#^lem-17-9|lemma]], $F_m^{(1)} \times Z_2$, $Z_1 \times F_k^{(2)}$, and $Z_1 \times Z_2$ all have measure zero (for the last, take $E = Z_2$ or use $Z_1 \times Z_2 \subseteq Z_1 \times [-k,k]^q$ and take $k \to \infty$). Their countable unions also have measure zero. Hence $E_1 \times E_2$ is measurable.
>
> **Step 4: The measure formula.** Apply [[Tonelli's Theorem|Tonelli]] to $\chi_{E_1 \times E_2}(x, y) = \chi_{E_1}(x)\,\chi_{E_2}(y)$:
>
> $$
> m(E_1 \times E_2) = \iint \chi_{E_1}(x)\,\chi_{E_2}(y)\,dx\,dy = \int_{\mathbb{R}^p} \chi_{E_1}(x) \left(\int_{\mathbb{R}^q} \chi_{E_2}(y)\,dy\right) dx = \int_{\mathbb{R}^p} \chi_{E_1}(x)\,m(E_2)\,dx = m(E_1)\,m(E_2).
> $$

^pf-17-8-cont

*Uses:* [[Inner Regularity of Lebesgue Measure|§11.10]], [[§11 Borel Sets and Measure Spaces#^cor-11-7|§11.7]], [[§17 Invariance Properties and Fubini's Theorem#^lem-17-9|§17.9]], [[Properties of Lebesgue Outer Measure|§9.1]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]], [[Tonelli's Theorem|§17.3]]

> [!remark]- Connections
> - The case of rectangles is the definition of volume ([[§9 Lebesgue Outer Measure#^def-9-2|Def. §9.2]]); the theorem extends it to all measurable “rectangles” $E_1 \times E_2$.
> - Used in [[§17 Invariance Properties and Fubini's Theorem#^cor-17-10|The Graph Has Measure Zero]], the [[§17 Invariance Properties and Fubini's Theorem#^thm-17-11|Subgraph Theorem]], and [[§18 Differentiation Theory#^prop-18-24|Measurability of f(x + t)]] (§18.24).

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
> By the [[§17 Invariance Properties and Fubini's Theorem#^thm-17-8|product set theorem]], each $E_k \times [k\delta, (k+1)\delta]$ is measurable with measure $m(E_k) \cdot \delta$. By [[Properties of Lebesgue Outer Measure|countable subadditivity]]:
>
> $$
> m(G_E(f)) \leq \sum_{k=-\infty}^{\infty} m(E_k) \cdot \delta = \delta \sum_{k=-\infty}^{\infty} m(E_k) = \delta \cdot m(E).
> $$
>
> Since $\delta > 0$ is arbitrary and $m(E) < \infty$, $m(G_E(f)) = 0$.
>
> For general $E$, write $E = \bigcup_{k=1}^{\infty} E_k$ with $m(E_k) < \infty$ (e.g., $E_k = E \cap B(0,k)$). Then $G_E(f) = \bigcup_k G_{E_k}(f)$, each with measure zero, so $m(G_E(f)) = 0$.

^pf-17-10

*Uses:* [[§12 Measurable Functions#^prop-12-2|§12.2]], [[§17 Invariance Properties and Fubini's Theorem#^thm-17-8|§17.8]], [[Properties of Lebesgue Outer Measure|§9.1]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]], [[§10 Lebesgue Measurable Sets#^ex-10-1|Ex. §10.1]]

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
> **Step 1: Simple functions.** If $f(x) = \sum_{j=1}^{p} a_j\,\chi_{A_j}(x)$ with $a_j \geq 0$ and $\{A_j\}$ pairwise disjoint measurable, $\bigcup A_j = E$ ([[§12 Measurable Functions#^prop-12-13|§12.13]]), then:
>
> $$
> \underline{G}(f) = \bigcup_{j=1}^{p} A_j \times [0, a_j),
> $$
>
> which is measurable (finite union of [[§17 Invariance Properties and Fubini's Theorem#^thm-17-8|product sets]]). Its measure is:
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

*Uses:* [[§12 Measurable Functions#^prop-12-13|§12.13]], [[§17 Invariance Properties and Fubini's Theorem#^thm-17-8|§17.8]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]], [[§14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]], [[Simple Function Approximation Theorem|§12.14]], [[Continuity of Measure|§11.12]], [[Monotone Convergence Theorem (Lebesgue)|§14.4]], [[Tonelli's Theorem|§17.3]]

> [!remark]- Connections
> - “Integral = area under the graph” is the MATH 451 picture of the Riemann integral via [[§32 The Definition of the Riemann Integral#^def-32-1|upper and lower sums]]; here it becomes a theorem about Lebesgue measure in $\mathbb{R}^{n+1}$.

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
> Define $F(x, \lambda) = p\,\lambda^{p-1}\,\chi_{\{(x, \lambda)\,:\, x \in E,\; 0 \leq \lambda < |f(x)|\}}$. Then $F$ is non-negative and measurable on $\mathbb{R}^n \times \mathbb{R}$ ([[§17 Invariance Properties and Fubini's Theorem#^thm-17-11|§17.11]]).
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

*Uses:* [[Tonelli's Theorem|§17.3]], [[§17 Invariance Properties and Fubini's Theorem#^thm-17-11|§17.11]], [[Riemann Integrable Implies Lebesgue Integrable|§15.10]], [[Fundamental Theorem of Calculus|451 §34.1]]

> [!remark] Remark: Interpretation
> When $p = 1$, the formula reduces to:
>
> $$
> \int_E |f(x)|\,dx = \int_0^{\infty} m\{x \in E : |f(x)| > \lambda\}\,d\lambda = \int_0^{\infty} f^*(\lambda)\,d\lambda.
> $$
>
> This says: the integral of $|f|$ equals the “area under the distribution function curve.” Geometrically, instead of slicing vertically (integrating $|f|$ over $x$), we slice horizontally (integrating the measure of superlevel sets over $\lambda$). This is exactly the Cavalieri principle from calculus, made rigorous via Tonelli.
>
> The layer cake formula is the foundation for defining $L^p$ norms ([[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-5|Def. §19.5]]) in terms of distribution functions, and is crucial in interpolation theory and harmonic analysis.

^rem-17-5

![[m551-17-3.svg]]
*The layer cake formula for $p = 1$, with $E = [0,1]$. Slicing the region under $|f|$ (blue) horizontally at height $\lambda$ cuts out the superlevel set $\{|f| > \lambda\}$ (red, left); its measure is the value $f^*(\lambda)$ of the distribution function (red segment, right). Integrating the slice lengths over $\lambda$ gives the area under $f^*$, which is the area under $|f|$: Tonelli on the subgraph, sliced the other way.*

> [!remark]- Connections
> - The $p = 1$ case is the [[§17 Invariance Properties and Fubini's Theorem#^thm-17-11|Subgraph Theorem]] read with horizontal slices, i.e. the [[§17 Invariance Properties and Fubini's Theorem#^thm-17-7|Cross-Section Theorem]] applied to $\underline{G}(\vert f\vert)$ in the other variable.
> - The $L^p$ spaces it feeds into: [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-5|Def. §19.5]].
