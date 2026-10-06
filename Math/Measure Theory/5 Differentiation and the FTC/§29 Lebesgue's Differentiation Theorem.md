---
type: section
subject: "[[Measure Theory]]"
chapter: 5
section: 29
tags: [measure-theory, math551]
---
← [[§28 Differentiation Theory]] · ↑ [[· 5 Differentiation and the FTC]] · [[§30 Differentiating the Integral]] →

A monotone function is differentiable almost everywhere. The proof compares the four Dini derivatives with the help of the [[Vitali Covering Theorem|Vitali covering theorem]].

## Dini Derivatives

> [!definition] Definition §29.1: Dini Derivatives
> Let $f$ be a real-valued function on $[a, b]$ and $x_0 \in (a, b)$. The four **Dini derivatives** of $f$ at $x_0$ are:
>
> $$
> \begin{aligned}
> D^+ f(x_0) &= \limsup_{h \to 0^+} \frac{f(x_0 + h) - f(x_0)}{h}, &\quad D_+ f(x_0) &= \liminf_{h \to 0^+} \frac{f(x_0 + h) - f(x_0)}{h}, \\[4pt]
> D^- f(x_0) &= \limsup_{h \to 0^+} \frac{f(x_0) - f(x_0 - h)}{h}, &\quad D_- f(x_0) &= \liminf_{h \to 0^+} \frac{f(x_0) - f(x_0 - h)}{h}.
> \end{aligned}
> $$

^def-29-1

> [!remark] Remark: Relationship to Differentiability
> By definition, $D^+ \geq D_+$ and $D^- \geq D_-$ always hold. If $D^+ f(x_0) \leq D_- f(x_0)$ and $D^- f(x_0) \leq D_+ f(x_0)$, then all four Dini derivatives are sandwiched:
>
> $$
> D_+ \leq D^+ \leq D_- \leq D^- \leq D_+,
> $$
>
> which forces $D^+ = D_+ = D^- = D_-$, i.e., $f$ is differentiable at $x_0$ in the extended sense (the common value may be $\pm\infty$; $f'(x_0)$ is a real number when it is finite).
>
> Equivalently: $f$ is *not* differentiable at $x_0$ iff $D^+ > D_-$ or $D^- > D_+$ at $x_0$. In other words, the upper Dini derivative on one side strictly exceeds the lower Dini derivative on the other side.

^rem-29-3

![[m551-18-5.svg]]
*An example of different Dini derivatives: $f(x) = x\sin(1/x)$ for $x > 0$ and $f(x) = 0$ for $x \leq 0$, at $x_0 = 0$. The right difference quotient $\frac{f(h) - f(0)}{h} = \sin(1/h)$ is the slope of the red secant, and as $h \to 0^+$ it sweeps through all of $[-1, 1]$, so $D^+f(0) = 1$ and $D_+f(0) = -1$ (dashed lines). From the left the quotient is $0$, so $D^-f(0) = D_-f(0) = 0$. Since $D^+f(0) = 1 > 0 = D_-f(0)$, $f$ is not differentiable at $0$.*

> [!remark]- Connections
> - One-sided derivatives in MATH 451: the one-sided limits of [[§20 Limits of Functions#^def-20-2|451 Def. §20.2]] applied to the difference quotient; limsup/liminf as in [[§16 Limits and Positive Parts of Measurable Functions#^rem-16-4|Remark: Recalling Limsup and Liminf]].

## Lebesgue's Theorem on Differentiability of Monotone Functions

> [!theorem] Theorem §29.1: Lebesgue's Differentiation Theorem for Monotone Functions
> Let $f$ be a monotone increasing function on $[a, b]$. Then:
> - (i) $f$ is differentiable a.e. on $(a, b)$.
> - (ii) $f' \geq 0$ a.e., and $f' \in L([a, b])$ (i.e., $f'$ is integrable).
> - (iii) $\displaystyle\int_a^b f'(x)\,dx \leq f(b) - f(a)$.

^thm-29-1

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
> We show $m(E_1) = m(E_2) = 0$. If $x_0 \in (a, b) \setminus (E_1 \cup E_2)$, then $D^+ f(x_0) \leq D_- f(x_0)$ and $D^- f(x_0) \leq D_+ f(x_0)$, which forces all four Dini derivatives to be equal (as argued in [[§29 Lebesgue's Differentiation Theorem#^rem-29-3|the remark above]]), so $f$ is differentiable at $x_0$ in the extended sense; that the common value is finite a.e. follows from (ii).
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
> The collection $\Gamma = \{[x_0 - h_j, x_0] : x_0 \in A,\; [x_0 - h_j, x_0] \subseteq G,\; h_j > 0\}$ is a [[§28 Differentiation Theory#^def-28-1|Vitali covering]] of $A$. By the [[Vitali Covering Theorem|Vitali Covering Theorem]], there exist finitely many disjoint intervals $J_1 = [y_1, y_1 + h_1'], \ldots, J_p = [y_p, y_p + h_p']$ in $\Gamma$ with:
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

^pf-29-1

*Uses:* [[§29 Lebesgue's Differentiation Theorem#^def-29-1|Def. §29.1]], [[§3 Countability of Rationals and Unions#^cor-3-2|§3.2]], [[§10 Lebesgue Outer Measure#^def-10-4|Def. §10.4]], [[§28 Differentiation Theory#^def-28-1|Def. §28.1]], [[Vitali Covering Theorem|§28.2]], [[Properties of Lebesgue Outer Measure|§10.1]], [[Lebesgue Measurable Sets Form a σ-Algebra|§11.3]]

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
> We compute $\int_a^b f_n(x)\,dx$ (using [[§25 Invariance Properties and Fubini's Theorem#^thm-25-1|translation invariance]]):
>
> $$
> \begin{aligned}
> \int_a^b f_n(x)\,dx &= n\!\left(\int_a^b f\!\left(x + \tfrac{1}{n}\right)\!dx - \int_a^b f(x)\,dx\right) = n\!\left(\int_{a+1/n}^{b+1/n} f(t)\,dt - \int_a^b f(x)\,dx\right) \\
> &= n\!\left(\int_b^{b+1/n} f(t)\,dt - \int_a^{a+1/n} f(t)\,dt\right).
> \end{aligned}
> $$
>
> By the extension, $f(t) = f(b)$ for $t \in [b, b+1/n]$; since $f$ is increasing, $f(t) \geq f(a)$ for $t \in [a, a+1/n]$. Hence:
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

^pf-29-1-2

*Uses:* [[Fatou's Lemma|§21.8]], [[§25 Invariance Properties and Fubini's Theorem#^thm-25-1|§25.1]], [[§22 The General Lebesgue Integral#^thm-22-2|§22.2]], [[§22 The General Lebesgue Integral#^thm-22-4|§22.4]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[§15 Measurable Functions#^ex-15-1|Ex. §15.1]]

> [!proof]+ Proof of (ii): Integrability of $f'$
> Since $f$ is increasing, $f' \geq 0$ wherever it exists. The integral inequality (iii) gives $\int_a^b f'\,dx \leq f(b) - f(a) < \infty$, so $f' \in L([a, b])$. In particular, $f'$ is finite a.e. ([[§21 Consequences of the Monotone Convergence Theorem#^prop-21-3|integrability implies a.e. finiteness]]).

^pf-29-1-3

*Uses:* [[§22 The General Lebesgue Integral#^def-22-1|Def. §22.1]], [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-3|§21.3]]

> [!remark] Remark
> The inequality in (iii) can be strict: for the [[§31 Absolute Continuity#^ex-31-1|Cantor function]] (“devil's staircase”), $f$ is increasing and continuous on $[0,1]$ with $f(0) = 0$, $f(1) = 1$, but $f' = 0$ a.e., so $\int_0^1 f'\,dx = 0 < 1 = f(1) - f(0)$. A similar statement holds for decreasing functions.

^rem-29-4

> [!remark]- Connections
> - Compare the MATH 451 [[Fundamental Theorem of Calculus]] (FTC I, 451 §34.1): for $f$ continuous on $[a,b]$, differentiable on $(a,b)$, with Riemann-integrable $f'$, equality holds in (iii). The Cantor function shows why only $\leq$ survives here.
> - Monotone functions were already Riemann integrable ([[§33 Properties of the Riemann Integral#^thm-33-1|451 §33.1]]); the new information is about $f'$.

> [!theorem] Corollary §29.2: BV Functions are Differentiable A.E.
> Let $f \in BV([a, b])$. Then $f$ is differentiable a.e. on $(a, b)$, and $f' \in L([a, b])$.

^cor-29-2

> [!proof]+ Proof
> By the [[Jordan Decomposition Theorem|Jordan Decomposition Theorem]], $f = g - h$ where $g, h$ are increasing on $[a, b]$. By [[Lebesgue's Differentiation Theorem for Monotone Functions|Lebesgue's theorem]], $g$ and $h$ are each differentiable a.e. on $(a, b)$, with $g', h' \in L([a, b])$. Hence $f$ is differentiable a.e. with $f' = g' - h' \in L([a, b])$.

^pf-29-2

*Uses:* [[Jordan Decomposition Theorem|§28.7]], [[Lebesgue's Differentiation Theorem for Monotone Functions|§29.1]]
