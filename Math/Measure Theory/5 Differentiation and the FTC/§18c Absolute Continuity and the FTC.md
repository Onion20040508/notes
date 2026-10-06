---
type: section
subject: "[[Measure Theory]]"
chapter: 5
section: 18
tags: [measure-theory, math551]
---
← [[§18b Differentiating the Integral]] · ↑ [[· 5 Differentiation and the FTC]] · [[§19 Normed Linear Spaces and Lᵖ Spaces]] →

Bounded variation is necessary but not sufficient for $f(x) - f(a) = \int_a^x f'$; the missing condition is absolute continuity. This section introduces absolutely continuous functions and proves the Fundamental Theorem of Calculus for Lebesgue integrals.

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
> **Answer**: **No.** The [[§18c Absolute Continuity and the FTC#^ex-18-4|Cantor function]] provides a counterexample.

^rem-18-5

> [!remark]- Connections
> - ($*$) is FTC I of MATH 451 ([[Fundamental Theorem of Calculus|451 §34.1]]), which assumes $f$ continuous on $[a,b]$ and differentiable everywhere on $(a,b)$ with Riemann-integrable $f'$.

> [!example] Example §18.4: The Cantor Function (Devil's Staircase)
> The **Cantor set** $C \subseteq [0, 1]$ ([[§11b The Vitali Set and the Cantor Set#^def-11-13|Def. §11.13]]) is obtained by repeatedly removing middle thirds: $C = \bigcap_{n=0}^{\infty} C_n$ where $C_0 = [0,1]$, $C_1 = [0, 1/3] \cup [2/3, 1]$, etc. The set $C$ is closed, uncountable, and has $m(C) = 0$ ([[§11b The Vitali Set and the Cantor Set#^prop-11-21|§11.21]]).
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
*The Cantor function $\varphi$ (blue). It is constant on every removed middle third (for example $\varphi = \frac12$ on $(\frac13, \frac23)$), so $\varphi' = 0$ off $C$. All of its growth happens over $C$: the second stage $C_2$ (red on the axis) consists of four intervals of total length $\frac49$, and over each of them $\varphi$ rises by $\frac14$ (red boxes), a total rise of $1$. At stage $n$ there are $2^n$ boxes of total width $(\frac23)^n \to 0$ and total height still $1$. This is the failure of absolute continuity in [[§18c Absolute Continuity and the FTC#^rem-18-7|Rem. §18.7]].*

> [!remark]- Connections
> - The Cantor set in MATH 451: [[§13 Some Topological Concepts in Metric Spaces#^rem-13-5|451 Remark §13.5]]; in this course: [[§11b The Vitali Set and the Cantor Set#^prop-11-21|Properties of the Cantor Set]] ([[§11b The Vitali Set and the Cantor Set#^prop-11-21|§11.21]]).
> - $\varphi \in BV$ by [[§18 Differentiation Theory#^ex-18-2|Ex. §18.2]]; it is the singular part in [[§18c Absolute Continuity and the FTC#^thm-18-15|Lebesgue Decomposition]] ([[§18c Absolute Continuity and the FTC#^thm-18-15|§18.15]]) and fails [[§18c Absolute Continuity and the FTC#^thm-18-19|AC Functions Map Null Sets to Null Sets]] ([[§18c Absolute Continuity and the FTC#^thm-18-19|§18.19]]).

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
> - The function-level version of [[§16 The L¹ Space and Density Theorems#^thm-16-1|Absolute Continuity of the Integral]] ([[§16 The L¹ Space and Density Theorems#^thm-16-1|§16.1]]); [[§18c Absolute Continuity and the FTC#^thm-18-12|Theorem §18.12]] makes the link.
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
> None of the reverse implications hold, except that on the compact interval $[a, b]$ continuity already implies uniform continuity ([[§19 Uniform Continuity#^thm-19-1|451 §19.1]]).

^rem-18-7

## Properties of Absolutely Continuous Functions

> [!theorem] Proposition §18.11: Basic Properties of AC Functions
> - (i) If $f \in AC([a, b])$, then $f$ is continuous on $[a, b]$.
> - (ii) If $f, g \in AC([a, b])$ and $c_1, c_2 \in \mathbb{R}$, then $c_1 f + c_2 g \in AC([a, b])$.
> - (iii) If $f \in \operatorname{Lip}([a, b])$ (i.e., $|f(x) - f(y)| \leq M|x - y|$ for all $x, y \in [a, b]$), then $f \in AC([a, b])$.

^prop-18-11

> [!proof]+ Proof
> **(i)** Taking $n = 1$ in the [[§18c Absolute Continuity and the FTC#^def-18-4|AC definition]]: for every $\varepsilon > 0$, there exists $\delta > 0$ such that $|y - x| < \delta$ implies $|f(y) - f(x)| < \varepsilon$. This is exactly [[§19 Uniform Continuity#^def-19-1|uniform continuity]], which implies continuity.
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

*Uses:* [[§18c Absolute Continuity and the FTC#^def-18-4|Def. §18.4]], [[§19 Uniform Continuity#^def-19-1|451 Def. §19.1]]

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

*Uses:* [[§16 The L¹ Space and Density Theorems#^thm-16-1|§16.1]], [[§18c Absolute Continuity and the FTC#^def-18-4|Def. §18.4]], [[§15 The General Lebesgue Integral#^prop-15-3|§15.3]], [[§15 The General Lebesgue Integral#^thm-15-4|§15.4]]

> [!remark]- Connections
> - MATH 451 counterpart: in FTC II ([[§34 Fundamental Theorem of Calculus#^thm-34-4|451 §34.4]]) the integral function of a bounded integrable $f$ is uniformly continuous (in fact Lipschitz).

> [!theorem] Theorem §18.16: $AC \implies BV$
> If $f \in AC([a, b])$, then $f \in BV([a, b])$.

^thm-18-16

> [!proof]+ Proof
> Take $\varepsilon = 1$ in the [[§18c Absolute Continuity and the FTC#^def-18-4|AC definition]]: there exists $\delta_0 > 0$ such that for any disjoint intervals $(x_j, y_j) \subseteq (a, b)$ with $\sum (y_j - x_j) < \delta_0$, we have $\sum |f(y_j) - f(x_j)| \leq 1$.
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

*Uses:* [[§18c Absolute Continuity and the FTC#^def-18-4|Def. §18.4]], [[§18 Differentiation Theory#^def-18-2|Def. §18.2]], [[§18 Differentiation Theory#^def-18-new1|Def. §18.3]], [[§18 Differentiation Theory#^prop-18-5|§18.5]]

> [!remark] Remark: The Hierarchy
> Summarizing:
>
> $$
> \operatorname{Lip}([a,b]) \subsetneq AC([a,b]) \subsetneq BV([a,b]) \cap C([a,b]).
> $$
>
> The [[§18c Absolute Continuity and the FTC#^ex-18-4|Cantor function]] shows $BV \cap C \not\subseteq AC$. The function $\sqrt{x}$ on $[0, 1]$ shows $AC \not\subseteq \operatorname{Lip}$ (it is AC since $\sqrt{x} = \int_0^x \frac{1}{2\sqrt{t}}\,dt$ with $\frac{1}{2\sqrt{t}} \in L$, but $|\sqrt{x}|/|x| \to \infty$).

^rem-18-9

> [!remark]- Connections
> - The inclusions: [[§18c Absolute Continuity and the FTC#^prop-18-11|§18.11]] (iii) and [[§18c Absolute Continuity and the FTC#^thm-18-16|§18.16]]; MATH 451 shows $\sqrt{x}$ is uniformly continuous on $[0,\infty)$ ([[§19 Uniform Continuity#^ex-19-5|451 Ex. §19.5]]).

*Chain (power singularities):* [[§19b Power Singularities 1∕xᵃ and ℚ#Power Singularities|Chapter 6]] →

> [!remark] Remark
> If $\tilde{F}(x) = f(x) - f(a) - \int_a^x f'(t)\,dt$, then $\tilde{F}$ is differentiable a.e. with $\tilde{F}' = f' - f' = 0$ a.e. on $(a,b)$. The [[§18c Absolute Continuity and the FTC#^ex-18-4|Cantor function]] shows $\tilde{F}$ can be non-constant: $\tilde{F} \equiv \varphi$ satisfies $\varphi' = 0$ a.e. but $\varphi(1) - \varphi(0) = 1$. So the FTC fails precisely when $\tilde{F}$ is a “Cantor-like” component.

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
> Fix
>
> $$
> r = \frac{|f(c) - f(a)|}{2(c - a)} > 0.
> $$
>
> For every $x_0 \in A$: $f'(x_0) = 0$ gives $\delta_0 > 0$ such that for all $0 < h < \delta_0$:
>
> $$
> |f(x_0 + h) - f(x_0)| < r\,h.
> $$
>
> Define $\Gamma = \{[x, x+h] : x \in A,\; h > 0,\; [x, x+h] \subseteq (a, c),\; |f(x+h) - f(x)| < r\,h\}$. By the previous display, $\Gamma$ is a [[§18 Differentiation Theory#^def-18-1|Vitali covering]] of $A$.
>
> By the [[Vitali Covering Theorem|Vitali Covering Lemma]]: for every $\delta > 0$, there exist finitely many disjoint intervals $[x_j, x_j + h_j] \in \Gamma$, $j = 1, \ldots, p$, with:
>
> $$
> m\!\left(A \setminus \bigcup_{j=1}^{p} [x_j, x_j + h_j]\right) < \delta.
> $$
>
> Since $m([a,c] \setminus A) = 0$, this gives $m\!\left([a, c] \setminus \bigcup_{j=1}^{p} [x_j, x_j + h_j]\right) < \delta$. It suffices to treat $\delta < c - a$ (gaps that work for a smaller $\delta$ also work for a larger one); then $m(A) = c - a > \delta$ forces $p \geq 1$.
>
> The intervals $[x_j, x_j + h_j] \subseteq (a,c)$ are disjoint, so $\sum h_j \leq c - a$. Ordering them as $a < x_1 < x_1 + h_1 < x_2 < \cdots < x_p + h_p < c$, the “gaps” between them (including the initial and final gaps) are the intervals $(u_i, v_i)$, $i = 0, \ldots, p$, with
>
> $$
> (u_0, v_0) = (a, x_1), \qquad (u_i, v_i) = (x_i + h_i,\ x_{i+1}) \ (1 \leq i < p), \qquad (u_p, v_p) = (x_p + h_p,\ c),
> $$
>
> and their total length is:
>
> $$
> \sum_{i=0}^{p} (v_i - u_i) = (c - a) - \sum_{j=1}^{p} h_j = m\!\left([a, c] \setminus \bigcup_{j=1}^{p} [x_j, x_j + h_j]\right) < \delta.
> $$
>
> By the triangle inequality, the total change of $f$ on $[a, c]$ splits into the changes on the gaps and on the chosen intervals:
>
> $$
> |f(c) - f(a)| \leq \sum_{i=0}^{p} |f(v_i) - f(u_i)| + \sum_{j=1}^{p} |f(x_j + h_j) - f(x_j)| < \sum_{i=0}^{p} |f(v_i) - f(u_i)| + r \sum_{j=1}^{p} h_j \leq \sum_{i=0}^{p} |f(v_i) - f(u_i)| + r(c - a).
> $$
>
> With the choice of $r$ above:
>
> $$
> \sum_{i=0}^{p} |f(v_i) - f(u_i)| \geq |f(c) - f(a)| - r(c - a) = \frac{1}{2}|f(c) - f(a)| > 0.
> $$
>
> Set $\varepsilon_0 = \frac{1}{2}|f(c) - f(a)|$; it does not depend on $\delta$. The gaps $(u_i, v_i)$ are finitely many disjoint subintervals of $(a, b)$ whose total length is $< \delta$ (they form the complement of the chosen Vitali intervals in $[a, c]$), yet the total oscillation $\sum_i |f(v_i) - f(u_i)|$ of $f$ on these gaps is $\geq \varepsilon_0$. This shows $f$ is not absolutely continuous.

^pf-18-27

*Uses:* [[§18 Differentiation Theory#^def-18-1|Def. §18.1]], [[Vitali Covering Theorem|§18.2]], [[§18c Absolute Continuity and the FTC#^def-18-4|Def. §18.4]], [[§9 Lebesgue Outer Measure#^prop-9-2|§9.2]], [[Properties of Lebesgue Outer Measure|§9.1]]

> [!remark]- Connections
> - MATH 451 counterpart: [[§29 The Mean Value Theorem#^cor-29-4|Vanishing Derivative Means Constant]] (451 §29.4), proved with the [[Mean Value Theorem]] when $f' = 0$ *everywhere*; the [[§18c Absolute Continuity and the FTC#^ex-18-4|Cantor function]] shows “a.e.” needs the extra AC hypothesis.
> - Used in the proof of [[Fundamental Theorem of Calculus for Lebesgue Integrals|the FTC for Lebesgue integrals]] ([[§18c Absolute Continuity and the FTC#^thm-18-13|§18.13]]).

## The Fundamental Theorem of Calculus for Lebesgue Integrals

> [!theorem] Theorem §18.13: The Fundamental Theorem of Calculus for Lebesgue Integrals
> Let $f: [a, b] \to \mathbb{R}$. Then the following are equivalent:
> - (i) $f$ is absolutely continuous on $[a, b]$.
> - (ii) $f$ is differentiable a.e., $f' \in L([a, b])$, and $f(x) - f(a) = \int_a^x f'(t)\,dt$ for all $x \in [a, b]$.

^thm-18-13

> [!proof]+ Proof of the Fundamental Theorem of Calculus
> **(ii) $\Rightarrow$ (i):** Assume $f$ is differentiable a.e., $f' \in L([a, b])$, and $f(x) - f(a) = \int_a^x f'(t)\,dt$ for all $x$. Then $f(x) = f(a) + \int_a^x f'(t)\,dt$. Since $f' \in L([a,b])$, the function $x \mapsto \int_a^x f'(t)\,dt$ is in $AC([a, b])$ by [[§18c Absolute Continuity and the FTC#^thm-18-12|the theorem above]] (integral functions are AC). Adding the constant $f(a)$ preserves absolute continuity ([[§18c Absolute Continuity and the FTC#^prop-18-11|property (ii)]]). Hence $f \in AC([a, b])$.
>
> **(i) $\Rightarrow$ (ii):** Assume $f \in AC([a, b])$. Then $f \in BV([a, b])$ ([[§18c Absolute Continuity and the FTC#^thm-18-16|AC ⟹ BV, proved above]]), so $f$ is differentiable a.e. on $(a, b)$ with $f' \in L([a, b])$ (by the [[§18a Lebesgue's Differentiation Theorem#^cor-18-10|BV differentiability corollary]]). It remains to show $f(x) - f(a) = \int_a^x f'(t)\,dt$ for all $x \in [a, b]$.
>
> Define $F(x) = f(x) - f(a) - \int_a^x f'(t)\,dt$. Since $f \in AC([a, b])$ and $\int_a^x f'(t)\,dt \in AC([a, b])$ (by the theorem above: integral functions are AC), and $AC$ is closed under linear combinations (property (ii)), we have $F \in AC([a, b])$.
>
> Moreover, $F'(x) = f'(x) - f'(x) = 0$ a.e. on $(a, b)$ (using the fact that $(\int_a^x f'\,dt)' = f'(x)$ a.e., proved in an earlier subsection; [[§18b Differentiating the Integral#^thm-18-26|§18.26]]).
>
> By the lemma on non-constant functions with zero derivative ([[§18c Absolute Continuity and the FTC#^thm-18-27|Theorem §18.27]]), if $F$ were not constant, then $F$ would not be absolutely continuous. But $F \in AC([a, b])$, so $F$ must be constant. Since $F(a) = f(a) - f(a) - 0 = 0$, we conclude $F(x) = 0$ for all $x \in [a, b]$, i.e.:
>
> $$
> f(x) - f(a) = \int_a^x f'(t)\,dt \qquad \forall\, x \in [a, b].
> $$

^pf-18-13

*Uses:* [[§18c Absolute Continuity and the FTC#^thm-18-12|§18.12]], [[§18c Absolute Continuity and the FTC#^prop-18-11|§18.11]], [[§18c Absolute Continuity and the FTC#^thm-18-16|§18.16]], [[§18a Lebesgue's Differentiation Theorem#^cor-18-10|§18.10]], [[§18b Differentiating the Integral#^thm-18-26|§18.26]], [[§18c Absolute Continuity and the FTC#^thm-18-27|§18.27]]

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
> **(ii)** $\sum g_k(x) = \sum g_k(c) + \int_c^x h(t)\,dt$ where $h = \sum g_k' \in L([a, b])$. The integral function of an $L$ function is $AC$ ([[§18c Absolute Continuity and the FTC#^thm-18-12|integral functions are AC]]), and adding a constant preserves $AC$. So $\sum g_k \in AC$.
>
> **(iii)** Differentiating, the constant $\sum g_k(c)$ drops out and [[§18b Differentiating the Integral#^thm-18-26|differentiation of the integral]] ([[§18b Differentiating the Integral#^thm-18-26|Theorem §18.26]], proved earlier) gives $(\sum g_k)'(x) = \left(\int_c^x h\,dt\right)' = h(x) = \sum g_k'(x)$ a.e.

^pf-18-14

*Uses:* [[Fundamental Theorem of Calculus for Lebesgue Integrals|§18.13]], [[§14a Consequences of the Monotone Convergence Theorem#^thm-14-12|§14.12]], [[§14a Consequences of the Monotone Convergence Theorem#^prop-14-10|§14.10]], [[Dominated Convergence Theorem|§15.8]], [[§18c Absolute Continuity and the FTC#^thm-18-12|§18.12]], [[§18c Absolute Continuity and the FTC#^prop-18-11|§18.11]], [[§18b Differentiating the Integral#^thm-18-26|§18.26]]

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
> $g$ is increasing (since $f' \geq 0$) and $g \in AC$ ([[§18c Absolute Continuity and the FTC#^thm-18-12|integral of an L function]]). By [[§18b Differentiating the Integral#^thm-18-26|differentiation of the integral]] ([[§18b Differentiating the Integral#^thm-18-26|Theorem §18.26]], proved earlier; applied to $f'$ extended by $0$ outside $[a, b]$), $g' = f'$ a.e.
>
> $h$ is increasing: for $x < y$, $g(y) - g(x) = \int_x^y f' \leq f(y) - f(x)$ (by [[Lebesgue's Differentiation Theorem for Monotone Functions|Lebesgue's integral inequality for increasing functions]]), so $h(y) - h(x) = (f(y) - f(x)) - (g(y) - g(x)) \geq 0$.
>
> $h' = 0$ a.e.: $h' = f' - g' = f' - f' = 0$ a.e.

^pf-18-15

*Uses:* [[Lebesgue's Differentiation Theorem for Monotone Functions|§18.9]], [[§18c Absolute Continuity and the FTC#^thm-18-12|§18.12]], [[§18b Differentiating the Integral#^thm-18-26|§18.26]]

> [!remark] Remark
> The function $h$ is called the **singular part** of $f$: it is increasing yet gains all its growth on a set of measure zero ($\{h' > 0\}$ has measure zero). The [[§18c Absolute Continuity and the FTC#^ex-18-4|Cantor function]] is the prototypical example of a purely singular increasing function.

^rem-18-8

> [!theorem] Lemma §18.17: AC on Subintervals
> If $f$ is AC on $[a, b]$ and $[c, d] \subseteq [a, b]$, then $f$ is AC on $[c, d]$.

^lem-18-17

> [!proof]+ Proof
> Any collection of disjoint intervals in $(c, d)$ is also a collection of disjoint intervals in $(a, b)$, so the same $\delta$ from the [[§18c Absolute Continuity and the FTC#^def-18-4|AC condition]] on $[a, b]$ works on $[c, d]$.

^pf-18-17

*Uses:* [[§18c Absolute Continuity and the FTC#^def-18-4|Def. §18.4]]

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
> Since $f \in AC([a, b])$, by the [[Fundamental Theorem of Calculus for Lebesgue Integrals|FTC]], $f' \in L([a, b])$ and $f(x) = f(a) + \int_a^x f'(t)\,dt$. By [[§18c Absolute Continuity and the FTC#^lem-18-17|the first lemma]], $f$ is AC on any $[c, d] \subseteq [a, b]$, so $f(x) = f(c) + \int_c^x f'(t)\,dt$ on $[c, d]$. Applying the total variation formula for integral functions ([[§18 Differentiation Theory#^thm-18-8|§18.8]]) to $f' \in L([c, d])$:
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
> Since $\{a, b\}$ has measure zero, $m(f(\{a, b\})) = 0$ (finitely many points), so it suffices to show $m(f(Z \setminus \{a, b\})) = 0$. By [[§18c Absolute Continuity and the FTC#^lem-18-18|the second lemma]] and the total variation identity:
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

*Uses:* [[Fundamental Theorem of Calculus for Lebesgue Integrals|§18.13]], [[§18c Absolute Continuity and the FTC#^lem-18-17|§18.17]], [[§18 Differentiation Theory#^thm-18-8|§18.8]], [[§16 The L¹ Space and Density Theorems#^thm-16-1|§16.1]], [[§9 Lebesgue Outer Measure#^def-9-4|Def. §9.4]], [[Open Sets in ℝ are Countable Unions of Disjoint Open Intervals|§7.1]], [[§18c Absolute Continuity and the FTC#^lem-18-18|§18.18]], [[Properties of Lebesgue Outer Measure|§9.1]], [[§14a Consequences of the Monotone Convergence Theorem#^cor-14-13|§14.13]], [[§9 Lebesgue Outer Measure#^ex-9-1|Ex. §9.1]]

> [!remark] Remark
> This is a strong property of AC functions: they cannot “spread” null sets. The [[§18c Absolute Continuity and the FTC#^ex-18-4|Cantor function]], by contrast, maps the Cantor set ($m = 0$) onto $[0, 1]$ ($m = 1$) — another illustration of why $BV \cap C \not\subseteq AC$.

^rem-18-10
