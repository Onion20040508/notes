---
type: section
subject: "[[Measure Theory]]"
chapter: 5
section: 31
tags: [measure-theory, math551]
---
← [[§30 Differentiating the Integral]] · ↑ [[· 5 Differentiation and the FTC]] · [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals]] →

Bounded variation is necessary but not sufficient for $f(x) - f(a) = \int_a^x f'$; the missing condition is absolute continuity. This section introduces absolutely continuous functions and their properties.

## The Fundamental Theorem of Calculus: What Goes Wrong?

> [!remark] Remark: The Central Question Revisited
> For $f: [a, b] \to \mathbb{R}$, under what assumptions do we have:
>
> $$
> f(x) - f(a) = \int_a^x f'(t)\,dt \qquad \text{for all } x \in [a, b]? \tag{*}
> $$
>
> If ($\ast$) holds, then $f(x) = f(a) + \int_a^x f'(t)\,dt$, and the integral function $G(x) = \int_a^x f'(t)\,dt$ is in $BV([a, b])$ (by the [[§28 Differentiation Theory#^thm-28-8|Total Variation Theorem]]). So $f \in BV([a, b])$ is *necessary* for ($\ast$).
>
> **Question**: Is $f \in BV([a, b])$ *sufficient* for ($\ast$)?
>
> **Answer**: **No.** The [[§31 Absolute Continuity#^ex-31-1|Cantor function]] provides a counterexample.

^rem-31-5

> [!remark]- Connections
> - ($*$) is FTC I of MATH 451 ([[Fundamental Theorem of Calculus|451 §34.1]]), which assumes $f$ continuous on $[a,b]$ and differentiable everywhere on $(a,b)$ with Riemann-integrable $f'$.

> [!example] Example §31.1: The Cantor Function (Devil's Staircase)
> The **Cantor set** $C \subseteq [0, 1]$ ([[§14 The Vitali Set and the Cantor Set#^def-14-4|Def. §14.4]]) is obtained by repeatedly removing middle thirds: $C = \bigcap_{n=0}^{\infty} C_n$ where $C_0 = [0,1]$, $C_1 = [0, 1/3] \cup [2/3, 1]$, etc. The set $C$ is closed, uncountable, and has $m(C) = 0$ ([[§14 The Vitali Set and the Cantor Set#^prop-14-7|§14.7]]).
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

^ex-31-1

![[m551-18-6.svg]]
*The Cantor function $\varphi$ (blue). It is constant on every removed middle third (for example $\varphi = \frac12$ on $(\frac13, \frac23)$), so $\varphi' = 0$ off $C$. All of its growth happens over $C$: the second stage $C_2$ (red on the axis) consists of four intervals of total length $\frac49$, and over each of them $\varphi$ rises by $\frac14$ (red boxes), a total rise of $1$. At stage $n$ there are $2^n$ boxes of total width $(\frac23)^n \to 0$ and total height still $1$. This is the failure of absolute continuity in [[§31 Absolute Continuity#^rem-31-7|Rem. §18.7]].*

> [!remark]- Connections
> - The Cantor set in MATH 451: [[§13 Some Topological Concepts in Metric Spaces#^rem-13-5|451 Remark §13.5]]; in this course: [[§14 The Vitali Set and the Cantor Set#^prop-14-7|Properties of the Cantor Set]] ([[§14 The Vitali Set and the Cantor Set#^prop-14-7|§14.7]]).
> - $\varphi \in BV$ by [[§28 Differentiation Theory#^ex-28-2|Ex. §28.2]]; it is the singular part in [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-32-3|Lebesgue Decomposition]] ([[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-32-3|§32.3]]) and fails [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-32-6|AC Functions Map Null Sets to Null Sets]] ([[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-32-6|§32.6]]).

> [!remark] Remark
> This shows that BV is not sufficient for the FTC. The missing condition is **absolute continuity**.

^rem-31-6

> [!definition] Definition §31.1: Absolute Continuity
> A function $f: [a, b] \to \mathbb{R}$ is **absolutely continuous** on $[a, b]$ (written $f \in AC([a, b])$) if for every $\varepsilon > 0$ there exists $\delta > 0$ such that for any finite collection of mutually disjoint subintervals $\{(a_k, b_k)\}_{k=1}^{n}$ of $[a, b]$:
>
> $$
> \sum_{k=1}^{n} (b_k - a_k) < \delta \implies \sum_{k=1}^{n} |f(b_k) - f(a_k)| < \varepsilon.
> $$

^def-31-1

> [!remark]- Connections
> - The function-level version of [[§24 The L¹ Space and Density Theorems#^thm-24-2|Absolute Continuity of the Integral]] ([[§24 The L¹ Space and Density Theorems#^thm-24-2|§24.2]]); [[§31 Absolute Continuity#^thm-31-2|Theorem §31.2]] makes the link.
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

^rem-31-7

## Properties of Absolutely Continuous Functions

> [!theorem] Proposition §31.1: Basic Properties of AC Functions
> - (i) If $f \in AC([a, b])$, then $f$ is continuous on $[a, b]$.
> - (ii) If $f, g \in AC([a, b])$ and $c_1, c_2 \in \mathbb{R}$, then $c_1 f + c_2 g \in AC([a, b])$.
> - (iii) If $f \in \operatorname{Lip}([a, b])$ (i.e., $|f(x) - f(y)| \leq M|x - y|$ for all $x, y \in [a, b]$), then $f \in AC([a, b])$.

^prop-31-1

> [!proof]+ Proof
> **(i)** Taking $n = 1$ in the [[§31 Absolute Continuity#^def-31-1|AC definition]]: for every $\varepsilon > 0$, there exists $\delta > 0$ such that $|y - x| < \delta$ implies $|f(y) - f(x)| < \varepsilon$. This is exactly [[§19 Uniform Continuity#^def-19-1|uniform continuity]], which implies continuity.
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

^pf-31-1

*Uses:* [[§31 Absolute Continuity#^def-31-1|Def. §31.1]], [[§19 Uniform Continuity#^def-19-1|451 Def. §19.1]]

> [!theorem] Theorem §31.2: The Integral Function is Absolutely Continuous
> If $g \in L([a, b])$, then $G(x) = \int_a^x g(t)\,dt$ is in $AC([a, b])$.

^thm-31-2

> [!proof]+ Proof
> This is a direct consequence of the absolute continuity of the Lebesgue integral ([[§24 The L¹ Space and Density Theorems#^thm-24-2|§24]]): for every $\varepsilon > 0$, there exists $\delta > 0$ such that $m(A) < \delta$ implies $\int_A |g|\,dt < \varepsilon$. For disjoint intervals $(x_j, y_j)$ with $\sum (y_j - x_j) < \delta$, the set $A = \bigcup_j (x_j, y_j)$ has $m(A) < \delta$, so:
>
> $$
> \sum_{j=1}^{p} |G(y_j) - G(x_j)| = \sum_{j=1}^{p} \left|\int_{x_j}^{y_j} g(t)\,dt\right| \leq \sum_{j=1}^{p} \int_{x_j}^{y_j} |g(t)|\,dt = \int_A |g|\,dt < \varepsilon.
> $$

^pf-31-2

*Uses:* [[§24 The L¹ Space and Density Theorems#^thm-24-2|§24.2]], [[§31 Absolute Continuity#^def-31-1|Def. §31.1]], [[§22 The General Lebesgue Integral#^prop-22-3|§22.3]], [[§22 The General Lebesgue Integral#^thm-22-4|§22.4]]

> [!remark]- Connections
> - MATH 451 counterpart: in FTC II ([[§34 Fundamental Theorem of Calculus#^thm-34-4|451 §34.4]]) the integral function of a bounded integrable $f$ is uniformly continuous (in fact Lipschitz).

> [!theorem] Theorem §31.3: $AC \implies BV$
> If $f \in AC([a, b])$, then $f \in BV([a, b])$.

^thm-31-3

> [!proof]+ Proof
> Take $\varepsilon = 1$ in the [[§31 Absolute Continuity#^def-31-1|AC definition]]: there exists $\delta_0 > 0$ such that for any disjoint intervals $(x_j, y_j) \subseteq (a, b)$ with $\sum (y_j - x_j) < \delta_0$, we have $\sum |f(y_j) - f(x_j)| \leq 1$.
>
> Divide $[a, b]$ into $n$ subintervals $[c_j, c_{j+1}]$ of length $(b - a)/n < \delta_0$ (choose $n$ large enough). Fix any subinterval $[c_j, c_{j+1}]$ and take any partition $c_j = t_0 < t_1 < \cdots < t_m = c_{j+1}$. The intervals $(t_0, t_1), \ldots, (t_{m-1}, t_m)$ are disjoint in $(a, b)$ with total length:
>
> $$
> \sum_{k=0}^{m-1} (t_{k+1} - t_k) = c_{j+1} - c_j = \frac{b-a}{n} < \delta_0.
> $$
>
> So the AC condition applies, giving $\sum_{k=0}^{m-1} |f(t_{k+1}) - f(t_k)| \leq 1$. Since this holds for *every* partition of $[c_j, c_{j+1}]$, taking the supremum: $\bigvee_{c_j}^{c_{j+1}}(f) \leq 1$. By [[§28 Differentiation Theory#^prop-28-5|additivity of total variation]]:
>
> $$
> \bigvee_a^b(f) = \sum_{j=0}^{n-1} \bigvee_{c_j}^{c_{j+1}}(f) \leq n.
> $$

^pf-31-3

*Uses:* [[§31 Absolute Continuity#^def-31-1|Def. §31.1]], [[§28 Differentiation Theory#^def-28-2|Def. §28.2]], [[§28 Differentiation Theory#^def-28-3|Def. §28.3]], [[§28 Differentiation Theory#^prop-28-5|§28.5]]

> [!remark] Remark: The Hierarchy
> Summarizing:
>
> $$
> \operatorname{Lip}([a,b]) \subsetneq AC([a,b]) \subsetneq BV([a,b]) \cap C([a,b]).
> $$
>
> The [[§31 Absolute Continuity#^ex-31-1|Cantor function]] shows $BV \cap C \not\subseteq AC$. The function $\sqrt{x}$ on $[0, 1]$ shows $AC \not\subseteq \operatorname{Lip}$ (it is AC since $\sqrt{x} = \int_0^x \frac{1}{2\sqrt{t}}\,dt$ with $\frac{1}{2\sqrt{t}} \in L$, but $|\sqrt{x}|/|x| \to \infty$).

^rem-31-9

> [!remark]- Connections
> - The inclusions: [[§31 Absolute Continuity#^prop-31-1|§31.1]] (iii) and [[§31 Absolute Continuity#^thm-31-3|§31.3]]; MATH 451 shows $\sqrt{x}$ is uniformly continuous on $[0,\infty)$ ([[§19 Uniform Continuity#^ex-19-5|451 Ex. §19.5]]).

*Chain (power singularities):* [[§36 Power Singularities 1∕xᵃ and ℚ#Power Singularities|Chapter 6]] →

> [!remark] Remark
> If $\tilde{F}(x) = f(x) - f(a) - \int_a^x f'(t)\,dt$, then $\tilde{F}$ is differentiable a.e. with $\tilde{F}' = f' - f' = 0$ a.e. on $(a,b)$. The [[§31 Absolute Continuity#^ex-31-1|Cantor function]] shows $\tilde{F}$ can be non-constant: $\tilde{F} \equiv \varphi$ satisfies $\varphi' = 0$ a.e. but $\varphi(1) - \varphi(0) = 1$. So the FTC fails precisely when $\tilde{F}$ is a “Cantor-like” component.

^rem-31-11

## Non-Constant Functions with Zero Derivative Are Not Absolutely Continuous

> [!theorem] Theorem §31.4
> Assume $f$ is differentiable a.e. on $(a, b)$ with $f'(x) = 0$ for a.e. $x \in (a, b)$, and assume $f$ is not a constant. Then $f$ is not absolutely continuous: there exists $\varepsilon_0 > 0$ such that for every $\delta > 0$, there exist finitely many mutually disjoint subintervals $\{(x_j, y_j)\}_{j=1}^{n}$ of $(a, b)$ with:
>
> $$
> \sum_{j=1}^{n} |y_j - x_j| < \delta \qquad \text{but} \qquad \sum_{j=1}^{n} |f(y_j) - f(x_j)| \geq \varepsilon_0.
> $$

^thm-31-4

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
> Define $\Gamma = \{[x, x+h] : x \in A,\; h > 0,\; [x, x+h] \subseteq (a, c),\; |f(x+h) - f(x)| < r\,h\}$. By the previous display, $\Gamma$ is a [[§28 Differentiation Theory#^def-28-1|Vitali covering]] of $A$.
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

^pf-31-4

*Uses:* [[§28 Differentiation Theory#^def-28-1|Def. §28.1]], [[Vitali Covering Theorem|§28.2]], [[§31 Absolute Continuity#^def-31-1|Def. §31.1]], [[§10 Lebesgue Outer Measure#^prop-10-2|§10.2]], [[Properties of Lebesgue Outer Measure|§10.1]]

> [!remark]- Connections
> - MATH 451 counterpart: [[§29 The Mean Value Theorem#^cor-29-4|Vanishing Derivative Means Constant]] (451 §29.4), proved with the [[Mean Value Theorem]] when $f' = 0$ *everywhere*; the [[§31 Absolute Continuity#^ex-31-1|Cantor function]] shows “a.e.” needs the extra AC hypothesis.
> - Used in the proof of [[Fundamental Theorem of Calculus for Lebesgue Integrals|the FTC for Lebesgue integrals]] ([[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-32-1|§32.1]]).

The Fundamental Theorem of Calculus for Lebesgue integrals and its consequences continue in [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals]].
