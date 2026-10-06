---
type: section
subject: "[[Calculus]]"
chapter: 11
section: "69a"
stewart: "11.1"
aliases: ["Stewart 11.1 (cont.)"]
tags: [calculus]
---
← [[§69 Sequences]] · ↑ [[· 11 Sequences, Series, and Power Series]] · [[§70 Series]] →

*Stewart, Section 11.1.*

The one genuinely new tool for sequences is the Monotonic Sequence Theorem: a bounded monotonic sequence converges even when we cannot compute its limit. It rests on the Completeness Axiom, and it is what later makes series with positive terms tractable ([[§70 Series|§70]], [[§71 The Integral Test and Estimates of Sums|§71]]).

## Monotonic and Bounded Sequences

> [!definition] Definition §69.5: Increasing, Decreasing, Monotonic
> A sequence $\{a_n\}$ is **increasing** if $a_n < a_{n+1}$ for all $n \ge 1$, that is, $a_1 < a_2 < a_3 < \cdots$. It is **decreasing** if $a_n > a_{n+1}$ for all $n \ge 1$. It is **monotonic** if it is either increasing or decreasing.
>
> For instance, $\left\{ \frac{3}{n+5} \right\}$ is decreasing: $\dfrac{3}{n+5} > \dfrac{3}{n+6} = \dfrac{3}{(n+1)+5}$, since the second denominator is larger.
>
> *Stewart: 11.1, Definition 10; Example 11.1.12*

^def-69-5

> [!example] Example §69.4: Showing a Sequence Is Decreasing
> Show that $a_n = \dfrac{n}{n^2 + 1}$ is decreasing.
>
> **Solution 1 (compare $a_n$ and $a_{n+1}$).** We must show $a_n > a_{n+1}$, that is, $\dfrac{n}{n^2+1} > \dfrac{n+1}{(n+1)^2 + 1}$. The denominators are positive, so cross-multiplying gives an equivalent inequality:
>
> $$
> \begin{aligned}
> n\big[(n+1)^2 + 1\big] > (n+1)(n^2 + 1)
> &\iff n^3 + 2n^2 + 2n > n^3 + n^2 + n + 1 \\
> &\iff n^2 + n > 1 .
> \end{aligned}
> $$
>
> Since $n \ge 1$, $n^2 + n \ge 2 > 1$ is true. So $a_n > a_{n+1}$ for all $n$.
>
> **Solution 2 (the derivative of a related function).** Let $f(x) = \dfrac{x}{x^2+1}$. By the Quotient Rule,
>
> $$
> f'(x) = \frac{(x^2 + 1) - x \cdot 2x}{(x^2+1)^2} = \frac{1 - x^2}{(x^2+1)^2} < 0 \qquad \text{whenever } x^2 > 1 .
> $$
>
> So $f$ is decreasing on $(1, \infty)$, and, being continuous at $1$, on $[1, \infty)$ ([[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-1|Theorem §27.1]]). Hence $a_n = f(n) > f(n+1) = a_{n+1}$ for all $n \ge 1$.
>
> *Stewart: Example 11.1.13*

^ex-69-4

> [!definition] Definition §69.6: Bounded Sequence
> A sequence $\{a_n\}$ is **bounded above** if there is a number $M$ such that $a_n \le M$ for all $n \ge 1$, and **bounded below** if there is a number $m$ such that $m \le a_n$ for all $n \ge 1$. If it is bounded above and below, it is a **bounded sequence**.
>
> For instance, $a_n = n$ is bounded below ($a_n > 0$) but not above, and $a_n = n/(n+1)$ is bounded since $0 < a_n < 1$.
>
> *Stewart: 11.1, Definition 11*

^def-69-6

Neither condition alone forces convergence: $(-1)^n$ is bounded but divergent, and $a_n = n$ is monotonic but $n \to \infty$. Together they do. If $\{a_n\}$ increases and $a_n \le M$ for all $n$, the terms are forced to crowd together below $M$ and approach some number $L \le M$. Making this precise needs a property of the real numbers.

> [!definition] Definition §69.7: Least Upper Bound
> A number $b$ is a **least upper bound** of a set $S$ of real numbers if $b$ is an upper bound for $S$ ($x \le b$ for all $x$ in $S$) and $b \le M$ for every other upper bound $M$ of $S$.
>
> *Stewart: 11.1 (text)*

^def-69-7

> [!definition] Definition §69.8: The Completeness Axiom
> **Completeness Axiom.** If $S$ is a nonempty set of real numbers that has an upper bound $M$ ($x \le M$ for all $x$ in $S$), then $S$ has a least upper bound $b$.
>
> The axiom expresses the fact that there is no gap or hole in the real number line ([[§116 Numbers, Inequalities, and Absolute Values#^def-116-2|Definition §116.2]]). In the same way, a nonempty set with a lower bound has a **greatest lower bound**.
>
> *Stewart: 11.1 (text)*

^def-69-new1

> [!theorem] Theorem §69.9: Monotonic Sequence Theorem
> Every bounded, monotonic sequence is convergent.
>
> In particular, a sequence that is increasing and bounded above converges, and a sequence that is decreasing and bounded below converges.
>
> *Stewart: 11.1, Theorem 12*

^thm-69-9

> [!proof]+ Proof
> **Increasing.** Suppose $\{a_n\}$ is increasing and bounded above. The set $S = \{a_n \mid n \ge 1\}$ is nonempty and has an upper bound, so by the Completeness Axiom it has a least upper bound $L$. Let $\varepsilon > 0$. Then $L - \varepsilon$ is *not* an upper bound for $S$, since $L$ is the *least* upper bound. Therefore
>
> $$
> a_N > L - \varepsilon \qquad \text{for some integer } N .
> $$
>
> The sequence is increasing, so $a_n \ge a_N$ for every $n > N$. Thus if $n > N$, then $a_n > L - \varepsilon$, and $a_n \le L$ because $L$ is an upper bound, so
>
> $$
> 0 \le L - a_n < \varepsilon , \qquad\text{that is,}\qquad |L - a_n| < \varepsilon \quad \text{whenever } n > N .
> $$
>
> So $\lim_{n \to \infty} a_n = L$.
>
> **Decreasing.** Stewart says that a similar proof, using the greatest lower bound, works. Equivalently: if $\{a_n\}$ is decreasing and bounded below by $m$, then $\{-a_n\}$ is increasing and bounded above by $-m$, so $-a_n \to L'$ for some $L'$ by the first part, and $a_n \to -L'$ by the Constant Multiple Law.

^pf-69-9

*Uses:* [[§69a Monotonic and Bounded Sequences#^def-69-7|Def. §69.7]], [[§69a Monotonic and Bounded Sequences#^def-69-new1|Def. §69.8]], [[§69a Monotonic and Bounded Sequences#^def-69-5|Def. §69.5]], [[§69a Monotonic and Bounded Sequences#^def-69-6|Def. §69.6]], [[§69 Sequences#^def-69-3|Def. §69.3]], [[§69 Sequences#^thm-69-3|§69.3]]

> [!remark]- Connections
> - Rigorous treatment: [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-1|451 Thm. §10.1]] (Monotone Convergence Theorem, same proof; hub [[Monotone Convergence Theorem]]); an unbounded monotone sequence tends to $\pm\infty$, [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-3|451 Thm. §10.3]].
> - The Completeness Axiom it rests on: [[§4 The Completeness Axiom#^def-4-4|451 Def. §4.4]] (with the supremum, [[§4 The Completeness Axiom#^def-4-3|451 Def. §4.3]]); hub [[Completeness Axiom]]. The geometric sequence of [[§69 Sequences#^thm-69-8|Theorem §69.8]]: [[§9 Limit Theorems for Sequences#^ex-9-10|451 Ex. §9.10]], collected in [[Geometric series]].

> [!example] Example §69.5: A Recursive Sequence
> Investigate the sequence defined by the *recurrence relation*
>
> $$
> a_1 = 2, \qquad a_{n+1} = \tfrac12 (a_n + 6) \qquad \text{for } n = 1, 2, 3, \ldots
> $$
>
> **First terms.** $a_1 = 2$, $a_2 = \frac12(2 + 6) = 4$, $a_3 = \frac12(4 + 6) = 5$, $a_4 = 5.5$, $a_5 = 5.75$, $a_6 = 5.875$, $a_7 = 5.9375$, $a_8 = 5.96875$, $a_9 = 5.984375$. They suggest that the sequence increases towards $6$.
>
> **Increasing, by induction.** $a_2 = 4 > 2 = a_1$. If $a_{k+1} > a_k$, then $a_{k+1} + 6 > a_k + 6$, so $\frac12(a_{k+1} + 6) > \frac12(a_k + 6)$, that is, $a_{k+2} > a_{k+1}$. So $a_{n+1} > a_n$ for all $n$.
>
> **Bounded, by induction.** Being increasing, the sequence is bounded below by $a_1 = 2$. Upper bound: $a_1 = 2 < 6$. If $a_k < 6$, then $a_k + 6 < 12$, so $a_{k+1} = \frac12(a_k + 6) < \frac12 (12) = 6$. So $a_n < 6$ for all $n$.
>
> **The limit.** By the Monotonic Sequence Theorem, $L = \lim_{n \to \infty} a_n$ exists. The theorem does not say what $L$ is, but now the recurrence relation does. As $n \to \infty$ also $n + 1 \to \infty$, so $a_{n+1} \to L$ too (if $|a_n - L| < \varepsilon$ for $n > N$, then also $|a_{n+1} - L| < \varepsilon$ for $n > N$). Taking limits on both sides of the recurrence, with the Limit Laws,
>
> $$
> L = \lim_{n \to \infty} a_{n+1} = \lim_{n \to \infty} \tfrac12 (a_n + 6) = \tfrac12 \Big( \lim_{n \to \infty} a_n + 6 \Big) = \tfrac12 (L + 6) .
> $$
>
> Solving $L = \frac12 (L + 6)$ gives $2L = L + 6$, so $L = 6$, as predicted.
>
> *Stewart: Example 11.1.14*

^ex-69-5

> [!remark] Remark: Method — Finding the Limit of a Sequence
> 1. **Rational expressions in $n$** (also with roots): divide numerator and denominator by the highest power of $n$ in the denominator and use the Limit Laws with $1/n^r \to 0$ ([[§69 Sequences#^ex-69-1|Example §69.1]]).
> 2. **Indeterminate forms with a real-variable formula** ($\ln n / n$, $n^{1/n}$, …): find $\lim_{x \to \infty} f(x)$ by l'Hospital's Rule and transfer it with [[§69 Sequences#^thm-69-1|Theorem §69.1]].
> 3. **Factorials, $(-1)^n$ and other integer-only expressions:** bound $a_n$ between simpler sequences and squeeze, or show $|a_n| \to 0$ ([[§69 Sequences#^ex-69-3|Example §69.3]]). Compare with $r^n$ ([[§69 Sequences#^thm-69-8|Theorem §69.8]]).
> 4. **A continuous function of a convergent sequence:** move the limit inside ([[§69 Sequences#^thm-69-6|Theorem §69.6]]).
> 5. **Recursive sequences:** show by induction that the sequence is monotonic and bounded, conclude that $L$ exists, then let $n \to \infty$ in the recurrence and solve for $L$ ([[§69a Monotonic and Bounded Sequences#^ex-69-5|Example §69.5]]). Solving for $L$ before knowing that the limit exists can give a wrong answer.
> 6. **Divergence:** exhibit two different values approached infinitely often, as for $(-1)^n$, or show $a_n \to \pm\infty$.

^rem-69-2
