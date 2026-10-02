---
type: section
subject: "[[Measure Theory]]"
chapter: 4
section: 15
tags: [measure-theory, math551]
---
← [[§14 The Lebesgue Integral for Simple Functions]] · ↑ [[· 4 Integration Theory]] · [[§16 The L¹ Space and Density Theorems]] →

We now extend the Lebesgue integral from non-negative functions to general measurable functions that may take negative values.

## Definition and Integrability

> [!definition] Definition §15.1: Lebesgue Integral of a General Measurable Function
> Let $f$ be a measurable function on $E$, $E \in \mathcal{M}$. Recall the [[§12 Measurable Functions#^def-12-4|decomposition]] $f(x) = f^+(x) - f^-(x)$, where:
>
> $$
> f^+(x) = \max\{f(x), 0\}, \qquad f^-(x) = \max\{-f(x), 0\}.
> $$
>
> Assume at least one of $\int_E f^+\,dx$ and $\int_E f^-\,dx$ is finite. We define:
>
> $$
> \int_E f(x)\,dx = \int_E f^+(x)\,dx - \int_E f^-(x)\,dx.
> $$
>
> If both $f^+ \in L(E)$ and $f^- \in L(E)$ (i.e., both integrals are finite), we say $f$ is **integrable** on $E$, written $f \in L(E)$.

^def-15-1

![[m551-15-1.svg]]
*The positive and negative parts. Left: $\int_E f$ is the blue area above the axis, $\int_E f^+$, minus the red area below it, $\int_E f^-$. Right: $f^+ = \max\{f, 0\}$ (blue) and $f^- = \max\{-f, 0\}$ (red) are both non-negative, so their integrals are already defined by [[§14 The Lebesgue Integral for Simple Functions#^def-14-2|Def. §14.2]]; the only case left undefined is when both areas are infinite.*

> [!remark] Remark: Characterization of Integrability
> Since $|f(x)| = f^+(x) + f^-(x)$, we have:
>
> $$
> f \in L(E) \iff \int_E |f(x)|\,dx < \infty.
> $$
>
> This is because $\int_E |f|\,dx = \int_E f^+\,dx + \int_E f^-\,dx$, so $\int_E |f|\,dx < \infty$ iff both $\int_E f^+\,dx < \infty$ and $\int_E f^-\,dx < \infty$.

^rem-15-1

> [!remark]- Connections
> - Contrast with MATH 451, where $|f|$ Riemann integrable does not follow from the definition but must be proved ([[§33 Properties of the Riemann Integral#^thm-33-4|451 §33.4]]), and where conditionally convergent improper integrals exist ([[§36 Improper Integrals|451 §36]]); the Lebesgue integral is an *absolute* integral.
> - $L(E)$ is the space $L^1(E)$ of [[§16 The L¹ Space and Density Theorems#^def-16-1|Def. §16.1]].
> - Riemann-side counterpart: improper integrals, [[§51 Improper Integrals#^def-51-1|Calc Def. §51.1]], which may converge without ∫|f| < ∞.

## Properties of the General Integral

> [!theorem] Proposition §15.1: Basic Properties
> Let $f$ be measurable on $E \in \mathcal{M}$.
> - (i) If $m(E) = 0$, then $\int_E f\,dx = 0$ (since $\int_E f^+ = \int_E f^- = 0$).
> - (ii) If $f = g$ a.e. on $E$ and $f, g$ are measurable, then $\int_E f\,dx = \int_E g\,dx$.
> - (iii) If $f \in L(E)$, then $f$ is a.e. finite on $E$.
> - (iv) If $|f(x)| \leq g(x)$ a.e. on $E$ and $g \in L(E)$, then $f \in L(E)$.

^prop-15-1

> [!proof]+ Proof
> **(i)** and **(ii)** follow from the [[§14 The Lebesgue Integral for Simple Functions#^prop-14-9|corresponding properties for non-negative functions]] applied to $f^+$ and $f^-$ separately.
>
> **(iii)** $f \in L(E) \Rightarrow |f| \in L(E)$ (since $\int_E |f|\,dx < \infty$). Since $|f| \geq 0$ is integrable, $|f|$ is a.e. finite (by [[§14 The Lebesgue Integral for Simple Functions#^prop-14-10|Proposition §14.10]]), hence $f$ is a.e. finite.
>
> **(iv)** $\int_E |f|\,dx \leq \int_E g\,dx < \infty$, so $f \in L(E)$.

^pf-15-1

*Uses:* [[§14 The Lebesgue Integral for Simple Functions#^prop-14-9|§14.9]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-10|§14.10]], [[§15 The General Lebesgue Integral#^rem-15-1|Rem. §15.1]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]]

> [!example] Example §15.1: Bounded Measurable Functions on Finite Measure Sets
> If $g$ is a bounded measurable function on $E$ with $m(E) < \infty$, then $g \in L(E)$. Indeed, $|g(x)| \leq M$ for all $x \in E$, so $\int_E |g|\,dx \leq M \cdot m(E) < \infty$.

^ex-15-1

> [!remark]- Connections
> - Supplies the constant dominator in the proof of [[Riemann Integrable Implies Lebesgue Integrable|Theorem §15.10]] (Riemann ⟹ Lebesgue).

## Linearity of the General Integral

> [!theorem] Theorem §15.2: Linearity
> Let $f \in L(E)$, $g \in L(E)$, $E \in \mathcal{M}$, and $c \in \mathbb{R}$. Then:
> - (i) $c\,f \in L(E)$ and $\displaystyle\int_E c\,f\,dx = c\int_E f\,dx$.
> - (ii) $f + g \in L(E)$ and $\displaystyle\int_E (f + g)\,dx = \int_E f\,dx + \int_E g\,dx$.

^thm-15-2

> [!proof]+ Proof
> **(i)** If $c > 0$: $(cf)^+ = c\,f^+$ and $(cf)^- = c\,f^-$. Then:
>
> $$
> \int_E cf\,dx = \int_E c\,f^+\,dx - \int_E c\,f^-\,dx = c\int_E f^+\,dx - c\int_E f^-\,dx = c\int_E f\,dx.
> $$
>
> If $c < 0$: $(cf)^+(x) = \max\{cf(x), 0\} = -c\max\{-f(x), 0\} = -c\,f^-(x)$, and similarly $(cf)^- = -c\,f^+$. Then:
>
> $$
> \int_E cf\,dx = \int_E (-c)\,f^-\,dx - \int_E (-c)\,f^+\,dx = (-c)\int_E f^-\,dx - (-c)\int_E f^+\,dx = c\int_E f\,dx.
> $$
>
> If $c = 0$: both sides are $0$.
>
> **(ii)** Since $f, g \in L(E)$, we have $|f + g| \leq |f| + |g|$, so:
>
> $$
> \int_E |f + g|\,dx \leq \int_E |f|\,dx + \int_E |g|\,dx < \infty,
> $$
>
> hence $f + g \in L(E)$. In particular, $(f+g)^+$ and $(f+g)^-$ are both finite-valued integrals.
>
> From $f + g = (f+g)^+ - (f+g)^-$ and $f + g = f^+ - f^- + g^+ - g^-$, we get:
>
> $$
> (f+g)^+ + f^- + g^- = (f+g)^- + f^+ + g^+.
> $$
>
> Both sides are sums of non-negative measurable functions, so by [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|linearity for non-negative functions]]:
>
> $$
> \int_E (f+g)^+\,dx + \int_E f^-\,dx + \int_E g^-\,dx = \int_E (f+g)^-\,dx + \int_E f^+\,dx + \int_E g^+\,dx.
> $$
>
> Since all six integrals are finite (because $f, g, f+g \in L(E)$), we can rearrange:
>
> $$
> \int_E (f+g)^+\,dx - \int_E (f+g)^-\,dx = \int_E f^+\,dx - \int_E f^-\,dx + \int_E g^+\,dx - \int_E g^-\,dx,
> $$
>
> which gives $\int_E (f+g)\,dx = \int_E f\,dx + \int_E g\,dx$.

^pf-15-2

*Uses:* [[§15 The General Lebesgue Integral#^def-15-1|Def. §15.1]], [[§12 Measurable Functions#^def-12-4|Def. §12.4]], [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|§14.8]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§15 The General Lebesgue Integral#^rem-15-1|Rem. §15.1]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]]

> [!remark]- Connections
> - Riemann counterpart: [[§33 Properties of the Riemann Integral#^thm-33-2|451 §33.2]]. Linearity makes $L^1(E)$ a vector space ([[§16 The L¹ Space and Density Theorems#^thm-16-4|Theorem §16.4]]).

> [!theorem] Proposition §15.3: Triangle Inequality
> Let $f, g$ be measurable on $E$. Then $\int_E |f + g|\,dx \leq \int_E |f|\,dx + \int_E |g|\,dx$.

^prop-15-3

> [!proof]+ Proof
> Since $|f(x) + g(x)| \leq |f(x)| + |g(x)|$ for all $x$, the result follows from [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|monotonicity of the integral for non-negative functions]].

^pf-15-3

*Uses:* [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|§14.8]]

> [!remark]- Connections
> - This is the triangle inequality of the $L^1$ norm ([[§16 The L¹ Space and Density Theorems#^thm-16-4|Theorem §16.4]](iii)); its $L^p$ version is [[Minkowski's Inequality|Minkowski's inequality]] (§19.9). Norm axioms in LADR: [[§19 Inner Products and Norms#^ladr-6-9|LADR 6.9]], [[Triangle inequality|LADR 6.17]].

## Countable Additivity and Domain Restriction

> [!theorem] Theorem §15.4: Countable Additivity of the General Integral
> Let $E_k \in \mathcal{M}$, $k = 1, 2, \ldots$, be pairwise disjoint, and let $E = \bigcup_{k=1}^{\infty} E_k$. If $f \in L(E)$, then:
>
> $$
> \int_E f\,dx = \sum_{k=1}^{\infty} \int_{E_k} f\,dx.
> $$

^thm-15-4

> [!proof]+ Proof
> Apply [[§14 The Lebesgue Integral for Simple Functions#^cor-14-13|countable additivity for non-negative functions]] to $f^+$ and $f^-$ separately:
>
> $$
> \int_E f^+\,dx = \sum_{k=1}^{\infty} \int_{E_k} f^+\,dx, \qquad \int_E f^-\,dx = \sum_{k=1}^{\infty} \int_{E_k} f^-\,dx.
> $$
>
> Both series on the right converge (since $\sum \int_{E_k} f^+ = \int_E f^+ < \infty$, and similarly for $f^-$). Subtracting:
>
> $$
> \int_E f\,dx = \int_E f^+\,dx - \int_E f^-\,dx = \sum_{k=1}^{\infty} \int_{E_k} f^+\,dx - \sum_{k=1}^{\infty} \int_{E_k} f^-\,dx = \sum_{k=1}^{\infty} \int_{E_k} f\,dx.
> $$

^pf-15-4

*Uses:* [[§14 The Lebesgue Integral for Simple Functions#^cor-14-13|§14.13]], [[§15 The General Lebesgue Integral#^def-15-1|Def. §15.1]], [[§14 Series#^prop-14-3|451 §14.3]]

> [!remark] Remark: Domain Restriction and Signed Induced Measure
> If $f \in L(E)$ and $A \subseteq E$, $A \in \mathcal{M}$, then $f \in L(A)$ (since $\int_A |f|\,dx \leq \int_E |f|\,dx < \infty$).
>
> If $f \in L(E)$, the map $\nu(A) = \int_A f\,dx$ defines a **signed measure** on measurable subsets of $E$: it satisfies $\nu(\emptyset) = 0$ and countable additivity, but can take negative values (unlike a [[§11 Borel Sets and Measure Spaces#^def-11-6|measure]]). This generalizes the [[§14 The Lebesgue Integral for Simple Functions#^def-14-3|induced measure from §14]].

^rem-15-2

> [!remark]- Connections
> - Finite version for the Riemann integral over almost disjoint Jordan measurable domains: [[§15 Multivariable Integration#^thm-15-4|452 Thm. §15.4]].

## Vanishing Integral Implies A.E. Zero

The non-negative case was proved in [[§14 The Lebesgue Integral for Simple Functions|§14]] ([[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|Proposition §14.11]]): if $f \geq 0$ and $\int_E f\,dx = 0$, then $f = 0$ a.e. We now extend to general measurable functions.

> [!theorem] Proposition §15.5: General Measurable Functions
> Let $f$ be measurable on $E$. If $\int_A f\,dx = 0$ for all $A \subseteq E$, $A \in \mathcal{M}$, then $f(x) = 0$ a.e. on $E$.

^prop-15-5

> [!proof]+ Proof
> Apply to $f^+$ and $f^-$ separately. Let $E_+ = \{x \in E : f(x) > 0\}$ and $E_- = \{x \in E : f(x) < 0\}$, both measurable. Then:
>
> $$
> 0 = \int_{E_+} f\,dx = \int_{E_+} f^+\,dx \implies f^+ = 0 \text{ a.e. on } E_+,
> $$
>
> which means $m(E_+) = 0$. Similarly, $0 = \int_{E_-} f\,dx = -\int_{E_-} f^-\,dx$ gives $m(E_-) = 0$. Hence $f = 0$ a.e. on $E$.

^pf-15-5

*Uses:* [[§12 Measurable Functions#^def-12-2|Def. §12.2]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|§14.11]]

> [!example] Example §15.2: Application: Vanishing Integrals over Intervals
> Let $f \in L([a,b])$. If $\int_a^c f(x)\,dx = 0$ for all $a \leq c \leq b$, then $f(x) = 0$ a.e. on $[a,b]$.

^ex-15-2

> [!proof]+ Proof
> It suffices to show $f^+ = 0$ a.e. and $f^- = 0$ a.e. separately. We show $f^+ = 0$ a.e.; the argument for $f^-$ is identical.
>
> Let $E_+ = \{x \in (a,b) : f(x) > 0\}$. Suppose for contradiction that $m(E_+) > 0$.
>
> **Step 1: $\int_F f\,dx = 0$ for every closed $F \subseteq [a,b]$.**
>
> Let $F \subseteq [a,b]$ be closed. The open set $(a,b) \setminus F$ can be written as a [[Open Sets in ℝ are Countable Unions of Disjoint Open Intervals|countable disjoint union of open intervals]]: $(a,b) \setminus F = \bigcup_{i=1}^{\infty} (a_i, b_i)$, where $a \leq a_i < b_i \leq b$ for each $i$.
>
> For each interval $(a_i, b_i)$, since $a_i, b_i \in [a,b]$:
>
> $$
> \int_{(a_i, b_i)} f\,dx = \int_{[a, b_i]} f\,dx - \int_{[a, a_i]} f\,dx = 0 - 0 = 0.
> $$
>
> (Here $\int_{[a, c]} f\,dx = \int_a^c f\,dx = 0$ by hypothesis, and the single points $\{a_i\}, \{b_i\}$ have measure zero so do not affect the integrals.)
>
> By [[§15 The General Lebesgue Integral#^thm-15-4|countable additivity of the integral]] over the disjoint sets $(a_i, b_i)$:
>
> $$
> \int_{(a,b) \setminus F} f\,dx = \sum_{i=1}^{\infty} \int_{(a_i, b_i)} f\,dx = 0.
> $$
>
> Since $\int_{[a,b]} f\,dx = 0$ and $\{a\}, \{b\}$ have measure zero:
>
> $$
> \int_F f\,dx = \int_{[a,b]} f\,dx - \int_{(a,b) \setminus F} f\,dx = 0.
> $$
>
> **Step 2: Contradiction.**
>
> By [[Inner Regularity of Lebesgue Measure|inner regularity]], there exists a closed set $F \subseteq E_+$ with $m(F) > 0$. On $F$, $f(x) > 0$ (since $F \subseteq E_+$), so $f^+(x) = f(x) > 0$ on $F$.
>
> By Step 1, $\int_F f\,dx = 0$, hence $\int_F f^+\,dx = \int_F f\,dx + \int_F f^-\,dx = 0 + 0 = 0$ (since $f^- = 0$ on $F \subseteq E_+$). But $f^+ > 0$ on $F$ with $m(F) > 0$, so by the [[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|previous proposition]] (non-negative function with zero integral $\Rightarrow$ a.e. zero), $f^+ = 0$ a.e. on $F$. This contradicts $f^+ > 0$ everywhere on $F$.
>
> Hence $m(E_+) = 0$, so $f^+ = 0$ a.e. Similarly $f^- = 0$ a.e., giving $f = 0$ a.e.

^pf-ex-15-2

*Uses:* [[Open Sets in ℝ are Countable Unions of Disjoint Open Intervals|§7.1]], [[§9 Lebesgue Outer Measure#^ex-9-1|Ex. §9.1]], [[§15 The General Lebesgue Integral#^prop-15-1|§15.1]], [[§15 The General Lebesgue Integral#^thm-15-2|§15.2]], [[§15 The General Lebesgue Integral#^thm-15-4|§15.4]], [[Inner Regularity of Lebesgue Measure|§11.10]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|§14.11]]

> [!remark]- Connections
> - With $F(x) = \int_a^x f$, this says $F \equiv 0 \Rightarrow f = 0$ a.e., the uniqueness half of the Lebesgue [[Fundamental Theorem of Calculus for Lebesgue Integrals|Fundamental Theorem of Calculus]] (§18.13); compare the MATH 451 [[Fundamental Theorem of Calculus]].

## Dominated Fatou's Lemma and Reverse Fatou

The standard [[Fatou's Lemma|Fatou's lemma]] ([[§14 The Lebesgue Integral for Simple Functions|§14]]) requires $f_k \geq 0$. Under a domination hypothesis, we can extend it to signed functions and also obtain the reverse inequality for $\limsup$.

> [!theorem] Theorem §15.6: Dominated Fatou's Lemma
> Let $\{f_k\}$ be a sequence of measurable functions on $E \in \mathcal{M}$. Suppose there exists $F \in L(E)$ with $F \geq 0$ such that $|f_k(x)| \leq F(x)$ a.e. on $E$ for all $k$. Then:
>
> $$
> \int_E \liminf_{k \to \infty} f_k\,dx \leq \liminf_{k \to \infty} \int_E f_k\,dx.
> $$

^thm-15-6

> [!proof]+ Proof
> Define $h_k = f_k + F$. Since $f_k \geq -|f_k| \geq -F$, we have $h_k \geq 0$. Each $h_k$ is measurable. By the [[Fatou's Lemma|standard Fatou's lemma]] applied to $\{h_k\}$:
>
> $$
> \int_E \liminf_{k \to \infty} (f_k + F)\,dx \leq \liminf_{k \to \infty} \int_E (f_k + F)\,dx.
> $$
>
> The left side equals $\int_E \liminf f_k\,dx + \int_E F\,dx$ (since $F$ does not depend on $k$). The right side equals $\liminf \int_E f_k\,dx + \int_E F\,dx$ (since $\int_E F\,dx$ is a constant). Since $\int_E F\,dx < \infty$, cancel it from both sides.

^pf-15-6

*Uses:* [[§12 Measurable Functions#^thm-12-3|§12.3]], [[Fatou's Lemma|§14.15]], [[§15 The General Lebesgue Integral#^thm-15-2|§15.2]], [[§15 The General Lebesgue Integral#^prop-15-1|§15.1]]

> [!theorem] Theorem §15.7: Reverse Fatou's Lemma
> Under the same hypotheses as above:
>
> $$
> \limsup_{k \to \infty} \int_E f_k\,dx \leq \int_E \limsup_{k \to \infty} f_k\,dx.
> $$

^thm-15-7

> [!proof]+ Proof
> **Step 1: $\int_E \limsup_{k \to \infty} f_k\,dx = \lim_{l \to \infty} \int_E g_l\,dx$.**
>
> Define $g_l(x) = \sup_{k \geq l} f_k(x)$, so that $\limsup_{k \to \infty} f_k(x) = \lim_{l \to \infty} g_l(x)$. Note that $g_l \geq g_{l+1}$ (the supremum is taken over fewer terms as $l$ increases).
>
> Decompose $g_l = g_l^+ - g_l^-$.
>
> *$g_l^+$ is decreasing*: If $g_l(x) \geq 0 > g_{l+1}(x)$, then $g_l^+(x) = g_l(x) \geq 0 = g_{l+1}^+(x)$. If $g_l(x) \geq g_{l+1}(x) \geq 0$, then $g_l^+(x) = g_l(x) \geq g_{l+1}(x) = g_{l+1}^+(x)$. If $0 \geq g_l(x) \geq g_{l+1}(x)$, then $g_l^+(x) = 0 = g_{l+1}^+(x)$. In all cases, $g_l^+ \geq g_{l+1}^+$.
>
> *$g_l^-$ is increasing*: By a similar case analysis, $g_l^- \leq g_{l+1}^-$.
>
> Since $|g_l(x)| = |\sup_{k \geq l} f_k(x)| \leq \sup_{k \geq l} |f_k(x)| \leq F(x)$, we have $g_l^+(x) \leq F(x)$, so $\int_E g_l^+\,dx \leq \int_E F\,dx < \infty$. By the [[§14 The Lebesgue Integral for Simple Functions#^thm-14-14|MCT for decreasing sequences]] (applicable since $g_l^+$ is decreasing with $\int_E g_1^+ < \infty$):
>
> $$
> \lim_{l \to \infty} \int_E g_l^+\,dx = \int_E \lim_{l \to \infty} g_l^+\,dx.
> $$
>
> By the [[Monotone Convergence Theorem (Lebesgue)|MCT for increasing sequences]] (applied to $g_l^-$):
>
> $$
> \lim_{l \to \infty} \int_E g_l^-\,dx = \int_E \lim_{l \to \infty} g_l^-\,dx.
> $$
>
> By [[§15 The General Lebesgue Integral#^thm-15-2|linearity]] (all integrals are finite):
>
> $$
> \lim_{l \to \infty} \int_E g_l\,dx = \lim_{l \to \infty} \int_E g_l^+\,dx - \lim_{l \to \infty} \int_E g_l^-\,dx = \int_E \lim_{l \to \infty} g_l^+\,dx - \int_E \lim_{l \to \infty} g_l^-\,dx = \int_E \lim_{l \to \infty} g_l\,dx = \int_E \limsup_{k \to \infty} f_k\,dx.
> $$
>
> **Step 2: $\limsup_{k \to \infty} \int_E f_k\,dx \leq \lim_{l \to \infty} \int_E g_l\,dx$.**
>
> Since $g_l(x) = \sup_{k \geq l} f_k(x) \geq f_k(x)$ for all $k \geq l$, by monotonicity $\int_E f_k\,dx \leq \int_E g_l\,dx$ for all $k \geq l$. Taking the supremum over $k \geq l$:
>
> $$
> \sup_{k \geq l} \int_E f_k\,dx \leq \int_E g_l\,dx.
> $$
>
> Taking $l \to \infty$:
>
> $$
> \limsup_{k \to \infty} \int_E f_k\,dx = \lim_{l \to \infty} \sup_{k \geq l} \int_E f_k\,dx \leq \lim_{l \to \infty} \int_E g_l\,dx = \int_E \limsup_{k \to \infty} f_k\,dx.
> $$

^pf-15-7

*Uses:* [[§12 Measurable Functions#^thm-12-6|§12.6]], [[§12 Measurable Functions#^rem-12-4|Rem. §12.4]], [[§12 Measurable Functions#^def-12-4|Def. §12.4]], [[§14 The Lebesgue Integral for Simple Functions#^thm-14-14|§14.14]], [[Monotone Convergence Theorem (Lebesgue)|§14.4]], [[§15 The General Lebesgue Integral#^thm-15-2|§15.2]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§10 Monotone Sequences and Cauchy Sequences#^def-10-3|451 Def. §10.3]]

## The Dominated Convergence Theorem

> [!theorem] Theorem §15.8: Dominated Convergence Theorem (DCT)
> Let $\{f_k\}$ be a sequence of measurable functions on $E \in \mathcal{M}$. Suppose:
> - (i) $f_k(x) \to f(x)$ a.e. on $E$,
> - (ii) there exists $F \in L(E)$, $F \geq 0$, such that $|f_k(x)| \leq F(x)$ a.e. on $E$ for all $k$.
>
> Then $f \in L(E)$ and:
>
> $$
> \lim_{k \to \infty} \int_E f_k(x)\,dx = \int_E f(x)\,dx.
> $$

^thm-15-8

> [!proof]+ Proof
> Since $|f_k| \leq F$ a.e. and $f_k \to f$ a.e., we have $|f| \leq F$ a.e., so $f \in L(E)$.
>
> By the [[§15 The General Lebesgue Integral#^thm-15-6|dominated Fatou's lemma]] and [[§15 The General Lebesgue Integral#^thm-15-7|reverse Fatou's lemma]]:
>
> $$
> \int_E \liminf_{k \to \infty} f_k\,dx \;\leq\; \liminf_{k \to \infty} \int_E f_k\,dx \;\leq\; \limsup_{k \to \infty} \int_E f_k\,dx \;\leq\; \int_E \limsup_{k \to \infty} f_k\,dx.
> $$
>
> Since $f_k \to f$ a.e., $\liminf f_k = \limsup f_k = f$ a.e., so both the leftmost and rightmost terms equal $\int_E f\,dx$. By the [[Squeeze Theorem|squeeze]]:
>
> $$
> \lim_{k \to \infty} \int_E f_k\,dx = \int_E f\,dx.
> $$

^pf-15-8

*Uses:* [[§15 The General Lebesgue Integral#^prop-15-1|§15.1]], [[§15 The General Lebesgue Integral#^thm-15-6|§15.6]], [[§15 The General Lebesgue Integral#^thm-15-7|§15.7]], [[§12 Measurable Functions#^rem-12-7|Rem. §12.7]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-6|451 §10.6]], [[Squeeze Theorem|451 §8.1]]

> [!remark]- Connections
> - MATH 451 exchanges limit and integral only under uniform convergence: [[§25 More on Uniform Convergence#^thm-25-1|451 §25.1]], [[§33 Properties of the Riemann Integral#^thm-33-12|451 §33.12]]. On $[a,b]$, a uniformly convergent sequence of bounded functions is dominated by a constant, so the DCT contains these.
> - The $L^p$ theory ([[§19 Normed Linear Spaces and Lᵖ Spaces|§19]]) leans on the DCT throughout. [[Fubini's Theorem (Lebesgue)|Fubini's Theorem]] (§17.6) does not: it applies [[Tonelli's Theorem]] to $f^+$ and $f^-$ and subtracts.
> - Used in PDEs: differentiation under the integral sign, which shows that the Fourier-integral solution of the semi-infinite rod satisfies the heat equation, [[§26 Semi-Infinite Rod#^thm-26-2|341 Thm. §26.2]], and passes $\partial/\partial x$ through the Laplace transform, [[§53★ Partial Differential Equations#^thm-53-1|341 Thm. §53.1]].
> - Used in Quantum Field Theory: differentiation under the integral sign with a dominating function independent of the parameter, the check behind every exchange of limit, derivative and integral in the field calculations — [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|QFT Theorem §CA.1.1]].

> [!remark] Remark: Comparison of Convergence Theorems
> The three main convergence theorems each trade hypotheses for generality:
>
> | **Theorem** | **Hypotheses** | **Conclusion** |
> |---|---|---|
> | [[Monotone Convergence Theorem (Lebesgue)\|MCT]] | $0 \leq f_k \nearrow f$ | $\lim \int f_k = \int f$ |
> | [[Fatou's Lemma\|Fatou]] | $f_k \geq 0$ | $\int \liminf f_k \leq \liminf \int f_k$ |
> | [[Dominated Convergence Theorem\|DCT]] | $\vert f_k\vert \leq F \in L$, $f_k \to f$ a.e. | $\lim \int f_k = \int f$ |
>
> The MCT requires monotonicity but no domination. The DCT requires domination but no monotonicity. Fatou is the weakest conclusion but requires the least: only non-negativity (or [[§15 The General Lebesgue Integral#^thm-15-6|domination for signed functions]]).

^rem-15-3

![[m551-15-2.svg]]
*Why the DCT needs an integrable dominator. Both sequences tend to $0$ at every point while $\int f_k = 1$ for every $k$, so $\lim \int f_k \neq \int \lim f_k$. (a) The sliding block $f_k = \chi_{[k,k+1]}$ of [[§13 Egorov's and Lusin's Theorems#^rem-13-1|Rem. §13.1]]: the smallest possible dominator $\sup_k f_k = \chi_{[1,\infty)}$ (red) has infinite integral. (b) The bumps $f_k = k\,\chi_{(0,1/k)}$ of [[§14 The Lebesgue Integral for Simple Functions#^ex-14-1|Ex. §14.1]]: $\sup_k f_k$ is the red staircase, equal to $k$ on $[\frac{1}{k+1}, \frac1k)$, which is at least $\frac1x - 1$ and not integrable near $0$. Any $F$ with $|f_k| \leq F$ lies above the red graph, so no $F \in L$ exists; only Fatou's inequality survives, and it is strict.*

> [!remark]- Connections
> - The MATH 451 row this table replaces: $f_n \to f$ uniformly on $[a,b]$ gives $\lim \int f_n = \int f$ ([[§33 Properties of the Riemann Integral#^thm-33-12|451 §33.12]]; [[§24 Uniform Convergence#^def-24-2|451 Def. §24.2]], [[§12 Measurable Functions#^def-12-9|Def. §12.9]]).
> - Why a new integral was needed for such theorems: [[§8 Motivation꞉ The Riemann Integral#^rem-8-2|Rem. §8.2]] (Riemann integrable functions are not closed under pointwise limits).

> [!proof]+ Alternative Proof of DCT via Fatou
> Since $|f_k(x) - f(x)| \leq |f_k(x)| + |f(x)| \leq 2g(x)$ a.e. (where $g = F$), define $h_k(x) = 2g(x) - |f_k(x) - f(x)|$. Then $h_k \geq 0$ a.e. and $h_k$ is measurable.
>
> Since $f_k \to f$ a.e., we have $|f_k - f| \to 0$ a.e., so $\liminf_{k \to \infty} h_k(x) = 2g(x)$ a.e. By [[Fatou's Lemma|Fatou's lemma]]:
>
> $$
> \int_E 2g\,dx = \int_E \liminf_{k \to \infty} h_k\,dx \leq \liminf_{k \to \infty} \int_E h_k\,dx = \liminf_{k \to \infty} \left(2\int_E g\,dx - \int_E |f_k - f|\,dx\right).
> $$
>
> Since $\int_E g\,dx < \infty$:
>
> $$
> 2\int_E g\,dx \leq 2\int_E g\,dx - \limsup_{k \to \infty} \int_E |f_k - f|\,dx,
> $$
>
> which gives $\limsup_{k \to \infty} \int_E |f_k - f|\,dx \leq 0$. Since $\int_E |f_k - f|\,dx \geq 0$ for all $k$:
>
> $$
> \lim_{k \to \infty} \int_E |f_k - f|\,dx = 0.
> $$
>
> The conclusion $\lim \int_E f_k\,dx = \int_E f\,dx$ then follows from:
>
> $$
> \left|\int_E f_k\,dx - \int_E f\,dx\right| = \left|\int_E (f_k - f)\,dx\right| \leq \int_E |f_k - f|\,dx \to 0.
> $$

^pf-15-8-2

*Uses:* [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]], [[Fatou's Lemma|§14.15]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-9|§14.9]], [[§15 The General Lebesgue Integral#^thm-15-2|§15.2]], [[§15 The General Lebesgue Integral#^prop-15-1|§15.1]]

> [!remark] Remark: $L^1$ Convergence
> The alternative proof actually establishes a stronger conclusion: under the hypotheses of DCT, $\lim_{k \to \infty} \int_E |f_k - f|\,dx = 0$, i.e., $f_k \to f$ in $L^1(E)$ ([[§16 The L¹ Space and Density Theorems#^def-16-2|Def. §16.2]]). This is strictly stronger than $\lim \int f_k = \int f$, which is convergence of the integrals.

^rem-15-4

> [!remark]- Connections
> - This $L^1$ form of the DCT drives the density theorems [[§16 The L¹ Space and Density Theorems#^thm-16-5|§16.5]] and [[§16 The L¹ Space and Density Theorems#^lem-16-2|§16.2]]; its $L^p$ analogue is used in [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|§19.19]].

## Absolute Convergence of Series in $L^1$

> [!theorem] Corollary §15.9: Absolute Convergence in $L^1$
> Let $f_k \in L(E)$ for all $k$, and assume $\sum_{k=1}^{\infty} \int_E |f_k(x)|\,dx < \infty$. Then:
> - (i) $\sum_{k=1}^{\infty} f_k(x)$ converges absolutely for a.e. $x \in E$.
> - (ii) Defining $S(x) = \sum_{k=1}^{\infty} f_k(x)$, we have $S \in L(E)$ and:
>
> $$
> \int_E \sum_{k=1}^{\infty} f_k(x)\,dx = \sum_{k=1}^{\infty} \int_E f_k(x)\,dx.
> $$

^cor-15-9

> [!proof]+ Proof
> Since $|f_k| \in L(E)$ is non-negative measurable, by [[§14 The Lebesgue Integral for Simple Functions#^thm-14-12|MCT II]]:
>
> $$
> \sum_{k=1}^{\infty} \int_E |f_k|\,dx = \int_E \sum_{k=1}^{\infty} |f_k(x)|\,dx < \infty.
> $$
>
> Therefore $\sum_{k=1}^{\infty} |f_k(x)| < \infty$ a.e. on $E$ ([[§14 The Lebesgue Integral for Simple Functions#^prop-14-10|integrable non-negative function is a.e. finite]]). This means $\sum f_k(x)$ converges absolutely a.e.
>
> Let $S_m(x) = \sum_{k=1}^{m} f_k(x)$ and $S(x) = \lim_{m \to \infty} S_m(x)$ (defined a.e.). Define $g(x) = \sum_{k=1}^{\infty} |f_k(x)| \in L(E)$. Then $|S_m(x)| \leq \sum_{k=1}^{m} |f_k(x)| \leq g(x)$ for all $x \in E$. Since $S_m \to S$ a.e. and $|S_m| \leq g \in L(E)$, by [[Dominated Convergence Theorem|DCT]]:
>
> $$
> \int_E S\,dx = \lim_{m \to \infty} \int_E S_m\,dx = \lim_{m \to \infty} \sum_{k=1}^{m} \int_E f_k\,dx = \sum_{k=1}^{\infty} \int_E f_k\,dx.
> $$

^pf-15-9

*Uses:* [[§14 The Lebesgue Integral for Simple Functions#^thm-14-12|§14.12]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-10|§14.10]], [[§14 Series#^prop-14-6|451 §14.6]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]], [[Dominated Convergence Theorem|§15.8]], [[§15 The General Lebesgue Integral#^thm-15-2|§15.2]]

> [!remark]- Connections
> - MATH 451 analogue: the [[§25 More on Uniform Convergence#^thm-25-3|Weierstrass M-test]] (451 §25.3) gives term-by-term integration from $\sum \sup |f_k| < \infty$; here $\sum \int |f_k| < \infty$ suffices.
> - $L^p$ version: [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-14|Corollary §19.14]]; the key step in [[Riesz–Fischer Theorem|Riesz–Fischer]] (§19.18).

## Riemann Integrable Functions are Lebesgue Integrable

> [!definition] Definition §15.2: Step Functions
> A function $h: [a,b] \to \mathbb{R}$ is called a **step function** if $h(x) = \sum_{j=1}^{m} a_j\,\chi_{R_j}(x)$ where the $R_j$ are [[§9 Lebesgue Outer Measure#^def-9-1|rectangles]] (intervals) in $[a,b]$.

^def-15-2

> [!remark]- Connections
> - MATH 451 example: [[§32 The Definition of the Riemann Integral#^ex-32-2|451 Ex. §32.2]]. Step functions are dense in $L^1$: [[§16 The L¹ Space and Density Theorems#^thm-16-6|Theorem §16.6]].

> [!theorem] Theorem §15.10: Riemann Integrability Implies Lebesgue Integrability
> Let $f$ be [[§8 Motivation꞉ The Riemann Integral#^def-8-3|Riemann integrable]] on $[a, b]$. Then $f$ is Lebesgue integrable on $[a, b]$ and:
>
> $$
> \int_{[a,b]}^R f(x)\,dx = \int_{[a,b]}^L f(x)\,dx.
> $$

^thm-15-10

> [!remark] Remark
> Recall that Riemann integrability on $[a,b]$ requires $f$ to be bounded: the [[§8 Motivation꞉ The Riemann Integral#^def-8-2|upper and lower sums]] use $M_j = \sup_{[x_j, x_{j+1}]} f$ and $m_j = \inf_{[x_j, x_{j+1}]} f$, which must be finite. Thus $|f| \leq M$ on $[a,b]$ is automatic, not an additional hypothesis. This boundedness is used in the proof to provide a dominator for DCT.

^rem-15-5

> [!remark] Remark: Riemann Integrability via Step Functions
> Let $p = \{x_0 = a < x_1 < \cdots < x_l = b\}$ be a [[§8 Motivation꞉ The Riemann Integral#^def-8-1|partition]] of $[a,b]$. Define the upper and lower sums:
>
> $$
> U(f, p, [a,b]) = \sum_{j=0}^{l-1} M_j(x_{j+1} - x_j), \quad L(f, p, [a,b]) = \sum_{j=0}^{l-1} m_j(x_{j+1} - x_j),
> $$
>
> where $M_j = \sup_{x \in [x_j, x_{j+1}]} f(x)$ and $m_j = \inf_{x \in [x_j, x_{j+1}]} f(x)$. Then $f \in R[a,b]$ iff:
>
> $$
> \lim_{|p| \to 0} U(f, p, [a,b]) = \lim_{|p| \to 0} L(f, p, [a,b]) = \int_{[a,b]}^R f(x)\,dx.
> $$

^rem-15-6

> [!remark]- Connections
> - This is the 551 definition [[§8 Motivation꞉ The Riemann Integral#^def-8-3|Def. §8.3]]; in MATH 451 the Darboux sums are [[§32 The Definition of the Riemann Integral#^def-32-1|451 Def. §32.1]] and the mesh form of the criterion is [[§32 The Definition of the Riemann Integral#^thm-32-6|451 §32.6]].

> [!proof]+ Proof of Theorem
> WLOG assume $[a, b] = [0, 1]$. For each $k \in \mathbb{N}$, consider the dyadic partition $x_j^{(k)} = j/2^k$ for $j = 0, 1, \ldots, 2^k$. Define the upper and lower step functions:
>
> $$
> \psi_k(x) = \sum_{j=0}^{2^k - 1} M_j\,\chi_{[x_j^{(k)}, x_{j+1}^{(k)})}(x), \qquad \varphi_k(x) = \sum_{j=0}^{2^k - 1} m_j\,\chi_{[x_j^{(k)}, x_{j+1}^{(k)})}(x),
> $$
>
> where $M_j = \sup_{[x_j^{(k)}, x_{j+1}^{(k)}]} f$ and $m_j = \inf_{[x_j^{(k)}, x_{j+1}^{(k)}]} f$.
>
> These satisfy $\varphi_k(x) \leq f(x) \leq \psi_k(x)$ for all $x \in [0,1]$ and all $k$, except possibly at $x = 1$ (which lies in none of the half-open intervals, so $\varphi_k(1) = \psi_k(1) = 0$; a single point is a null set, so this is harmless). As $k$ increases (finer partitions), $\psi_k$ decreases and $\varphi_k$ increases:
>
> $$
> \varphi_k \leq \varphi_{k+1} \leq f \leq \psi_{k+1} \leq \psi_k.
> $$
>
> Since $\{\varphi_k\}$ is increasing and bounded above by $f$, and $\{\psi_k\}$ is decreasing and bounded below by $f$, the pointwise limits exist:
>
> $$
> \varphi(x) = \lim_{k \to \infty} \varphi_k(x), \qquad \psi(x) = \lim_{k \to \infty} \psi_k(x),
> $$
>
> with $\varphi(x) \leq f(x) \leq \psi(x)$ for all $x \in [0,1)$.
>
> Since $f$ is Riemann integrable:
>
> $$
> \lim_{k \to \infty} \int_0^1 \psi_k\,dx = \lim_{k \to \infty} \int_0^1 \varphi_k\,dx = \int_{[0,1]}^R f\,dx.
> $$
>
> Now $\psi_k - \varphi_k \geq 0$ and $\psi_k - \varphi_k \searrow \psi - \varphi \geq 0$. Since $\int_0^1 (\psi_1 - \varphi_1)\,dx < \infty$ (both are bounded), by the [[§14 The Lebesgue Integral for Simple Functions#^thm-14-14|decreasing version of the MCT]] applied to the difference:
>
> $$
> \int_0^1 (\psi - \varphi)\,dx = \lim_{k \to \infty} \int_0^1 (\psi_k - \varphi_k)\,dx = 0.
> $$
>
> Since $\psi - \varphi \geq 0$ and $\int_0^1 (\psi - \varphi)\,dx = 0$, the [[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|vanishing integral result]] gives $\psi(x) = \varphi(x)$ a.e. on $[0,1]$.
>
> Since $\varphi(x) \leq f(x) \leq \psi(x)$ and $\varphi = \psi$ a.e., we have $f(x) = \varphi(x) = \psi(x)$ a.e. In particular, $f(x) = \lim_{k \to \infty} \varphi_k(x)$ a.e., and $f$ is measurable, since it equals the measurable function $\varphi$ (a pointwise limit of simple functions) a.e. ([[§12 Measurable Functions#^prop-12-12|Prop. §12.12]]).
>
> Since $|\varphi_k(x)| \leq M$ for all $k$ (where $M = \sup_{[0,1]} |f|$) and $m([0,1]) < \infty$, the constant function $M$ dominates. By [[Dominated Convergence Theorem|DCT]]:
>
> $$
> \int_{[0,1]}^L f\,dx = \lim_{k \to \infty} \int_0^1 \varphi_k\,dx = \int_{[0,1]}^R f\,dx.
> $$

^pf-15-10

*Uses:* [[§8 Motivation꞉ The Riemann Integral#^def-8-3|Def. §8.3]], [[§15 The General Lebesgue Integral#^rem-15-6|Rem. §15.6]], [[§15 The General Lebesgue Integral#^def-15-2|Def. §15.2]], [[§14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]], [[§14 The Lebesgue Integral for Simple Functions#^thm-14-14|§14.14]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|§14.11]], [[§12 Measurable Functions#^prop-12-12|§12.12]], [[§15 The General Lebesgue Integral#^ex-15-1|Ex. §15.1]], [[Dominated Convergence Theorem|§15.8]], [[§32 The Definition of the Riemann Integral#^lem-32-2|451 §32.2]]

![[m551-15-3.svg]]
*The proof with $k = 3$ (dyadic intervals of length $\frac18$): the lower step function $\varphi_k$ (blue, the infimum on each interval) and the upper step function $\psi_k$ (red, the supremum) trap $f$. The gray area is $\int_0^1 (\psi_k - \varphi_k)$, the gap between the upper and lower sums; Riemann integrability makes it tend to $0$, which forces $\varphi = \psi = f$ a.e., and the DCT with the constant dominator $M$ then gives $\int^L f = \lim \int \varphi_k = \int^R f$.*

> [!remark]- Connections
> - The converse fails: the Dirichlet function ([[§8 Motivation꞉ The Riemann Integral#^ex-8-2|Ex. §8.2]], [[§32 The Definition of the Riemann Integral#^ex-32-3|451 Ex. §32.3]]) is not Riemann integrable but equals $0$ a.e., so its Lebesgue integral is $0$ ([[§15 The General Lebesgue Integral#^prop-15-1|§15.1]](ii)).
> - Multivariable Riemann integral on rectangles: [[§15 Multivariable Integration#^def-15-10|452 Def. §15.10]]; its Jordan-content framework ([[§15 Multivariable Integration#^def-15-5|452 Def. §15.5]]) is superseded by Lebesgue measure.
> - Stewart's definite integral (Riemann sums): [[§35 The Definite Integral#^def-35-1|Calc Def. §35.1]] (with worked examples).
