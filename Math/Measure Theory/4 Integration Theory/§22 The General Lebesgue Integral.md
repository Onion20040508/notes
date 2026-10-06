---
type: section
subject: "[[Measure Theory]]"
chapter: 4
section: 22
tags: [measure-theory, math551]
---
← [[§21 Consequences of the Monotone Convergence Theorem]] · ↑ [[· 4 Integration Theory]] · [[§23 The Dominated Convergence Theorem]] →

We now extend the Lebesgue integral from non-negative functions to general measurable functions that may take negative values.

## Definition and Integrability

> [!definition] Definition §22.1: Lebesgue Integral of a General Measurable Function
> Let $f$ be a measurable function on $E$, $E \in \mathcal{M}$. Recall the [[§16 Limits and Positive Parts of Measurable Functions#^def-16-1|decomposition]] $f(x) = f^+(x) - f^-(x)$, where:
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

^def-22-1

![[m551-15-1.svg]]
*The positive and negative parts. Left: $\int_E f$ is the blue area above the axis, $\int_E f^+$, minus the red area below it, $\int_E f^-$. Right: $f^+ = \max\{f, 0\}$ (blue) and $f^- = \max\{-f, 0\}$ (red) are both non-negative, so their integrals are already defined by [[§20 The Lebesgue Integral for Simple Functions#^def-20-2|Def. §20.2]]; the only case left undefined is when both areas are infinite.*

> [!remark] Remark: Characterization of Integrability
> Since $|f(x)| = f^+(x) + f^-(x)$, we have:
>
> $$
> f \in L(E) \iff \int_E |f(x)|\,dx < \infty.
> $$
>
> This is because $\int_E |f|\,dx = \int_E f^+\,dx + \int_E f^-\,dx$, so $\int_E |f|\,dx < \infty$ iff both $\int_E f^+\,dx < \infty$ and $\int_E f^-\,dx < \infty$.

^rem-22-1

> [!remark]- Connections
> - Contrast with MATH 451, where $|f|$ Riemann integrable does not follow from the definition but must be proved ([[§33 Properties of the Riemann Integral#^thm-33-4|451 §33.4]]), and where conditionally convergent improper integrals exist ([[§36 Improper Integrals|451 §36]]); the Lebesgue integral is an *absolute* integral.
> - $L(E)$ is the space $L^1(E)$ of [[§24 The L¹ Space and Density Theorems#^def-24-1|Def. §24.1]].
> - Riemann-side counterpart: improper integrals, [[§58 Improper Integrals#^def-58-1|Calc Def. §58.1]], which may converge without ∫|f| < ∞.

## Properties of the General Integral

> [!theorem] Proposition §22.1: Basic Properties
> Let $f$ be measurable on $E \in \mathcal{M}$.
> - (i) If $m(E) = 0$, then $\int_E f\,dx = 0$ (since $\int_E f^+ = \int_E f^- = 0$).
> - (ii) If $f = g$ a.e. on $E$ and $f, g$ are measurable, then $\int_E f\,dx = \int_E g\,dx$.
> - (iii) If $f \in L(E)$, then $f$ is a.e. finite on $E$.
> - (iv) If $|f(x)| \leq g(x)$ a.e. on $E$ and $g \in L(E)$, then $f \in L(E)$.

^prop-22-1

> [!proof]+ Proof
> **(i)** and **(ii)** follow from the [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-2|corresponding properties for non-negative functions]] applied to $f^+$ and $f^-$ separately.
>
> **(iii)** $f \in L(E) \Rightarrow |f| \in L(E)$ (since $\int_E |f|\,dx < \infty$). Since $|f| \geq 0$ is integrable, $|f|$ is a.e. finite (by [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-3|Proposition §21.3]]), hence $f$ is a.e. finite.
>
> **(iv)** $\int_E |f|\,dx \leq \int_E g\,dx < \infty$, so $f \in L(E)$.

^pf-22-1

*Uses:* [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-2|§21.2]], [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-3|§21.3]], [[§22 The General Lebesgue Integral#^rem-22-1|Rem. §15.1]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]]

> [!example] Example §22.1: Bounded Measurable Functions on Finite Measure Sets
> If $g$ is a bounded measurable function on $E$ with $m(E) < \infty$, then $g \in L(E)$. Indeed, $|g(x)| \leq M$ for all $x \in E$, so $\int_E |g|\,dx \leq M \cdot m(E) < \infty$.

^ex-22-1

> [!remark]- Connections
> - Supplies the constant dominator in the proof of [[Riemann Integrable Implies Lebesgue Integrable|Theorem §23.5]] (Riemann ⟹ Lebesgue).

## Linearity of the General Integral

> [!theorem] Theorem §22.2: Linearity
> Let $f \in L(E)$, $g \in L(E)$, $E \in \mathcal{M}$, and $c \in \mathbb{R}$. Then:
> - (i) $c\,f \in L(E)$ and $\displaystyle\int_E c\,f\,dx = c\int_E f\,dx$.
> - (ii) $f + g \in L(E)$ and $\displaystyle\int_E (f + g)\,dx = \int_E f\,dx + \int_E g\,dx$.

^thm-22-2

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
> Both sides are sums of non-negative measurable functions, so by [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|linearity for non-negative functions]]:
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

^pf-22-2

*Uses:* [[§22 The General Lebesgue Integral#^def-22-1|Def. §22.1]], [[§16 Limits and Positive Parts of Measurable Functions#^def-16-1|Def. §16.1]], [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|§21.1]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[§22 The General Lebesgue Integral#^rem-22-1|Rem. §15.1]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]]

> [!remark]- Connections
> - Riemann counterpart: [[§33 Properties of the Riemann Integral#^thm-33-2|451 §33.2]]. Linearity makes $L^1(E)$ a vector space ([[§24 The L¹ Space and Density Theorems#^thm-24-4|Theorem §24.4]]).

> [!theorem] Proposition §22.3: Triangle Inequality
> Let $f, g$ be measurable on $E$. Then $\int_E |f + g|\,dx \leq \int_E |f|\,dx + \int_E |g|\,dx$.

^prop-22-3

> [!proof]+ Proof
> Since $|f(x) + g(x)| \leq |f(x)| + |g(x)|$ for all $x$, the result follows from [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|monotonicity of the integral for non-negative functions]].

^pf-22-3

*Uses:* [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|§21.1]]

> [!remark]- Connections
> - This is the triangle inequality of the $L^1$ norm ([[§24 The L¹ Space and Density Theorems#^thm-24-4|Theorem §24.4]](iii)); its $L^p$ version is [[Minkowski's Inequality|Minkowski's inequality]] ([[§35 Lᵖ as a Banach Space#^thm-35-2|§35.2]]). Norm axioms in LADR: [[§20 Inner Products and Norms#^ladr-6-9|LADR 6.9]], [[Triangle inequality|LADR 6.17]].

## Countable Additivity and Domain Restriction

> [!theorem] Theorem §22.4: Countable Additivity of the General Integral
> Let $E_k \in \mathcal{M}$, $k = 1, 2, \ldots$, be pairwise disjoint, and let $E = \bigcup_{k=1}^{\infty} E_k$. If $f \in L(E)$, then:
>
> $$
> \int_E f\,dx = \sum_{k=1}^{\infty} \int_{E_k} f\,dx.
> $$

^thm-22-4

> [!proof]+ Proof
> Apply [[§21 Consequences of the Monotone Convergence Theorem#^cor-21-6|countable additivity for non-negative functions]] to $f^+$ and $f^-$ separately:
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

^pf-22-4

*Uses:* [[§21 Consequences of the Monotone Convergence Theorem#^cor-21-6|§21.6]], [[§22 The General Lebesgue Integral#^def-22-1|Def. §22.1]], [[§14 Series#^prop-14-3|451 §14.3]]

> [!remark] Remark: Domain Restriction and Signed Induced Measure
> If $f \in L(E)$ and $A \subseteq E$, $A \in \mathcal{M}$, then $f \in L(A)$ (since $\int_A |f|\,dx \leq \int_E |f|\,dx < \infty$).
>
> If $f \in L(E)$, the map $\nu(A) = \int_A f\,dx$ defines a **signed measure** on measurable subsets of $E$: it satisfies $\nu(\emptyset) = 0$ and countable additivity, but can take negative values (unlike a [[§12 Borel Sets and Measure Spaces#^def-12-6|measure]]). This generalizes the [[§21 Consequences of the Monotone Convergence Theorem#^def-21-1|induced measure from §14]].

^rem-22-2

> [!remark]- Connections
> - Finite version for the Riemann integral over almost disjoint Jordan measurable domains: [[§22 Properties of the Integral#^thm-22-3|452 Thm. §22.3]].

## Vanishing Integral Implies A.E. Zero

The non-negative case was proved in [[§20 The Lebesgue Integral for Simple Functions|§20]] ([[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|Proposition §21.4]]): if $f \geq 0$ and $\int_E f\,dx = 0$, then $f = 0$ a.e. We now extend to general measurable functions.

> [!theorem] Proposition §22.5: General Measurable Functions
> Let $f$ be measurable on $E$. If $\int_A f\,dx = 0$ for all $A \subseteq E$, $A \in \mathcal{M}$, then $f(x) = 0$ a.e. on $E$.

^prop-22-5

> [!proof]+ Proof
> Apply to $f^+$ and $f^-$ separately. Let $E_+ = \{x \in E : f(x) > 0\}$ and $E_- = \{x \in E : f(x) < 0\}$, both measurable. Then:
>
> $$
> 0 = \int_{E_+} f\,dx = \int_{E_+} f^+\,dx \implies f^+ = 0 \text{ a.e. on } E_+,
> $$
>
> which means $m(E_+) = 0$. Similarly, $0 = \int_{E_-} f\,dx = -\int_{E_-} f^-\,dx$ gives $m(E_-) = 0$. Hence $f = 0$ a.e. on $E$.

^pf-22-5

*Uses:* [[§15 Measurable Functions#^def-15-2|Def. §15.2]], [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|§21.4]]

> [!example] Example §22.2: Application: Vanishing Integrals over Intervals
> Let $f \in L([a,b])$. If $\int_a^c f(x)\,dx = 0$ for all $a \leq c \leq b$, then $f(x) = 0$ a.e. on $[a,b]$.

^ex-22-2

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
> By [[§22 The General Lebesgue Integral#^thm-22-4|countable additivity of the integral]] over the disjoint sets $(a_i, b_i)$:
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
> By Step 1, $\int_F f\,dx = 0$, hence $\int_F f^+\,dx = \int_F f\,dx + \int_F f^-\,dx = 0 + 0 = 0$ (since $f^- = 0$ on $F \subseteq E_+$). But $f^+ > 0$ on $F$ with $m(F) > 0$, so by the [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|previous proposition]] (non-negative function with zero integral $\Rightarrow$ a.e. zero), $f^+ = 0$ a.e. on $F$. This contradicts $f^+ > 0$ everywhere on $F$.
>
> Hence $m(E_+) = 0$, so $f^+ = 0$ a.e. Similarly $f^- = 0$ a.e., giving $f = 0$ a.e.

^pf-ex-22-2

*Uses:* [[Open Sets in ℝ are Countable Unions of Disjoint Open Intervals|§7.2]], [[§10 Lebesgue Outer Measure#^ex-10-1|Ex. §10.1]], [[§22 The General Lebesgue Integral#^prop-22-1|§22.1]], [[§22 The General Lebesgue Integral#^thm-22-2|§22.2]], [[§22 The General Lebesgue Integral#^thm-22-4|§22.4]], [[Inner Regularity of Lebesgue Measure|§13.3]], [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|§21.4]]

> [!remark]- Connections
> - With $F(x) = \int_a^x f$, this says $F \equiv 0 \Rightarrow f = 0$ a.e., the uniqueness half of the Lebesgue [[Fundamental Theorem of Calculus for Lebesgue Integrals|Fundamental Theorem of Calculus]] ([[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-32-1|§32.1]]); compare the MATH 451 [[Fundamental Theorem of Calculus]].

Dominated and reverse Fatou, the Dominated Convergence Theorem and its applications continue in [[§23 The Dominated Convergence Theorem]].
