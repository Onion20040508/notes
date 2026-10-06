---
type: section
subject: "[[Measure Theory]]"
chapter: 3
section: 10
tags: [measure-theory, math551]
---
← [[§9 The Rationals ℚ]] · ↑ [[· 3 Measure Theory]] · [[§11 Lebesgue Measurable Sets]] →

## The Lebesgue Idea

In Riemann integration ([[§8 Motivation꞉ The Riemann Integral|§8]]; [[§32 The Definition of the Riemann Integral|451 §32]]), we partition the *domain* (the $x$-axis). Lebesgue's key insight was to instead partition the *range* (the $y$-axis).

Given a function $f: [a,b] \to \mathbb{R}$, partition $-\infty < y_1 < y_2 < \cdots < y_r < +\infty$ and consider the sets $S_j = \{x \mid x \in [a,b], y_j < f(x) \leq y_{j+1}\}$.

Then the area under the graph of $f$ is approximately $\sum_j y_j \cdot m(S_j)$, where $m(S_j)$ is the “measure” of $S_j$.

![[m551-9-1.svg]]
*Riemann versus Lebesgue for the same $f$ on $[a,b]$. Left: Riemann (Darboux) sums cut the $x$-axis into subintervals (blue rectangles). Right: Lebesgue cuts the $y$-axis instead; the band $y_j < y \leq y_{j+1}$ (red) pulls back to $S_j = \{x \in [a,b] \mid y_j < f(x) \leq y_{j+1}\}$, here a union of three intervals (filled endpoint: included, hollow: excluded). Measuring sets like $S_j$ is what the rest of the chapter is for.*

This approach requires us to develop a theory of **measure** for subsets of $\mathbb{R}^n$.

## Rectangles and Their Volume

> [!definition] Definition §10.1: Rectangles in $\mathbb{R}^n$
> A **rectangle** in $\mathbb{R}^n$ is a set of the form
>
> $$
> I = (a_1, b_1) \times (a_2, b_2) \times \cdots \times (a_n, b_n)
> $$
>
> where $a_j < b_j$ for all $j$. We write:
> - $\mathring{I} = (a_1, b_1) \times \cdots \times (a_n, b_n)$ for the **interior** (open rectangle; the set of [[§2 Open and Closed Sets#^def-2-3|interior points]], 452 Def. §2.5); for $I$ as above $\mathring{I} = I$, and the notation is useful for the closed or half-open rectangle with the same edges, whose interior is again this open rectangle
> - $\bar{I} = [a_1, b_1] \times \cdots \times [a_n, b_n]$ for the **closure** (closed rectangle; [[§2 Open and Closed Sets#^def-2-8|452 Def. §2.8]])

^def-10-1

> [!definition] Definition §10.2: Volume of a Rectangle
> The **volume** of a rectangle $I = (a_1, b_1) \times \cdots \times (a_n, b_n)$ is
>
> $$
> |I| = (b_1 - a_1)(b_2 - a_2) \cdots (b_n - a_n) = \prod_{j=1}^{n} (b_j - a_j).
> $$

^def-10-2

> [!remark]- Connections
> - MATH 452 counterpart, where area of a rectangle is likewise defined by hand: [[§20 Multivariable Integration#^def-20-2|452 Def. §20.2]].
> - How a linear map rescales volume: [[§37 Determinants#^ladr-9-61|LADR 9.61]], used for null sets in [[§30 Differentiating the Integral#^thm-30-3|Thm. §30.3]].

## Outer Measure

> [!definition] Definition §10.3: L-covering
> Let $A \subseteq \mathbb{R}^n$. A **Lebesgue covering** (or **L-covering**) of $A$ is a countable collection $\{I_k\}$ of open rectangles such that $A \subseteq \bigcup_k I_k$.

^def-10-3

> [!definition] Definition §10.4: Outer Measure
> Let $A \subseteq \mathbb{R}^n$. The **outer measure** of $A$ is
>
> $$
> m^*(A) = \inf \left\{ \sum_{k=1}^{\infty} |I_k| \,\bigg|\, \{I_k\} \text{ is an L-covering of } A \right\}.
> $$

^def-10-4

> [!remark]- Connections
> - MATH 452 counterpart using finite grids of squares instead of countable coverings: [[§20 Multivariable Integration#^def-20-6|outer Jordan content]] (452 Def. §20.6).
> - Axiomatized in [[§12 Borel Sets and Measure Spaces#^def-12-3|Def. §12.3]] (outer measure on an arbitrary set).

> [!remark] Remark
> For outer measure, we have either $\sum_k |I_k| = \infty$ for every L-covering $\{I_k\}$ of $A$ (so $m^*(A) = \infty$), or $m^*(A) < \infty$. In the latter case, for every $\epsilon > 0$, there exists an L-covering $\{I_k\}$ of $A$ such that
>
> $$
> m^*(A) + \epsilon > \sum_k |I_k|.
> $$

^rem-10-1

## Examples of Outer Measure

> [!example] Example §10.1: Finite Sets Have Measure Zero
> Let $A = \{x_1, x_2, \ldots, x_k\}$ be a finite set of points in $\mathbb{R}^n$. Then $m^*(A) = 0$.

^ex-10-1

> [!proof]+ Proof
> Let $\epsilon > 0$. For each point $x_j$, we can cover it with an open rectangle of arbitrarily small volume. Thus the infimum over all such coverings is $0$.

^pf-ex-10-1

*Uses:* [[§10 Lebesgue Outer Measure#^def-10-4|Def. §10.4]]

> [!example] Example §10.2: Countable Sets Have Measure Zero
> Let $A = \{x_1, x_2, x_3, \ldots\}$ be a [[§1 Countability and Set Theory#^def-1-1|countable]] set of points in $\mathbb{R}^n$. Then $m^*(A) = 0$.

^ex-10-2

> [!proof]+ Proof
> Let $\epsilon > 0$. Write $x_k = (x_k^{(1)}, x_k^{(2)}, \ldots, x_k^{(n)})$.
>
> For each $k$, define the open rectangle
>
> $$
> I_k = \left( x_k^{(1)} - \frac{\epsilon}{2^k}, x_k^{(1)} + \frac{\epsilon}{2^k} \right) \times \cdots \times \left( x_k^{(n)} - \frac{\epsilon}{2^k}, x_k^{(n)} + \frac{\epsilon}{2^k} \right).
> $$
>
> Then $x_k \in I_k$ and $|I_k| = \left( \frac{2\epsilon}{2^k} \right)^n$.
>
> The collection $\{I_k\}$ is an L-covering of $A$, and (summing a [[§14 Series#^ex-14-4|geometric series]])
>
> $$
> \sum_{k=1}^{\infty} |I_k| = \sum_{k=1}^{\infty} \left( \frac{2\epsilon}{2^k} \right)^n = (2\epsilon)^n \sum_{k=1}^{\infty} \frac{1}{2^{kn}} = (2\epsilon)^n \cdot \frac{1/2^n}{1 - 1/2^n} = (2\epsilon)^n \cdot \frac{1}{2^n - 1}.
> $$
>
> As $\epsilon \to 0^+$, this sum tends to $0$.
>
> Therefore $m^*(A) = 0$.

^pf-ex-10-2

*Uses:* [[§10 Lebesgue Outer Measure#^def-10-3|Def. §10.3]], [[§10 Lebesgue Outer Measure#^def-10-4|Def. §10.4]], [[§14 Series#^ex-14-4|451 Ex. §14.4]]

![[m551-9-2.svg]]
*The covering of [[§10 Lebesgue Outer Measure#^ex-10-2|Example §10.2]] for $n = 2$: the $k$-th point $x_k$ (red) gets an open square $I_k$ (dashed) of half-side $\epsilon/2^k$, so the squares shrink geometrically. Their total area is $(2\epsilon)^2 \cdot \tfrac{1}{2^2 - 1}$, which tends to $0$ with $\epsilon$ — however the points are arranged, even densely as with $\mathbb{Q}^2$.*

> [!remark]- Connections
> - $\mathbb{Q}$ is countable ([[§3 Countability of Rationals and Unions#^cor-3-2|Cor. §3.2]]), so it is a null set; the [[Dirichlet and Thomae functions|Dirichlet function]] of [[§8 Motivation꞉ The Riemann Integral#^ex-8-2|Ex. §8.2]] is its indicator on $[0,1]$.
> - The converse fails: the [[§14 The Vitali Set and the Cantor Set#^prop-14-7|Cantor set]] is uncountable and null.

## Properties of Outer Measure

> [!theorem] Proposition §10.1: Basic Properties of Outer Measure
> The outer measure $m^*$ satisfies:
> 1. $m^*(\emptyset) = 0$ and $m^*(A) \geq 0$ for all $A \subseteq \mathbb{R}^n$.
> 2. **Monotonicity:** If $A_1 \subseteq A_2$, then $m^{\ast}(A_1) \leq m^{\ast}(A_2)$.
> 3. **Countable subadditivity:** $m^{\ast}\left( \bigcup_{i=1}^{\infty} A_i \right) \leq \sum_{i=1}^{\infty} m^{\ast}(A_i)$.

^prop-10-1

> [!proof]+ Proof
> **(1)** Clear from the definition.
>
> **(2)** Let $\{I_k\}$ be an L-covering of $A_2$. Since $A_1 \subseteq A_2$, $\{I_k\}$ is also an L-covering of $A_1$. Thus
>
> $$
> \{L\text{-coverings of } A_1\} \supseteq \{L\text{-coverings of } A_2\},
> $$
>
> so taking infimum: $m^*(A_1) \leq m^*(A_2)$.
>
> **(3)** If there exists $i$ with $m^{\ast}(A_i) = \infty$, the inequality holds trivially.
>
> Assume $m^*(A_i) < \infty$ for all $i$. Let $\epsilon > 0$. For each $i$, there exists an L-covering $\{I_k^{(i)}\}_{k=1}^{\infty}$ of $A_i$ such that
>
> $$
> \sum_k |I_k^{(i)}| \leq m^*(A_i) + \frac{\epsilon}{2^i}.
> $$
>
> The collection $\bigcup_{i=1}^{\infty} \{I_k^{(i)}\}_k$ is countable (a [[Countable Union of Countable Sets is Countable|countable union of countable sets]]) and is an L-covering of $\bigcup_{i=1}^{\infty} A_i$.
>
> Thus
>
> $$
> m^*\left( \bigcup_{i=1}^{\infty} A_i \right) \leq \sum_{i=1}^{\infty} \sum_k |I_k^{(i)}| \leq \sum_{i=1}^{\infty} \left( m^*(A_i) + \frac{\epsilon}{2^i} \right) = \sum_{i=1}^{\infty} m^*(A_i) + \epsilon.
> $$
>
> Since $\epsilon > 0$ is arbitrary, $m^*\left( \bigcup_{i=1}^{\infty} A_i \right) \leq \sum_{i=1}^{\infty} m^*(A_i)$.

^pf-10-1

*Uses:* [[§10 Lebesgue Outer Measure#^def-10-3|Def. §10.3]], [[§10 Lebesgue Outer Measure#^def-10-4|Def. §10.4]], [[§10 Lebesgue Outer Measure#^rem-10-1|Rem. §9.1]], [[Countable Union of Countable Sets is Countable|§3.1]]

> [!remark]- Connections
> - These three properties become the axioms of a general outer measure: [[§12 Borel Sets and Measure Spaces#^def-12-3|Def. §12.3]].

## Outer Measure of Rectangles

> [!theorem] Proposition §10.2: Outer Measure of Closed Rectangles
> Let $\bar{I} = [a_1, b_1] \times \cdots \times [a_n, b_n]$ be a closed bounded rectangle in $\mathbb{R}^n$. Then
>
> $$
> m^*(\bar{I}) = |I| = \prod_{j=1}^{n} (b_j - a_j).
> $$
>
> The same holds for any bounded rectangle (open, closed, or half-open).

^prop-10-2

> [!proof]+ Proof
> **Upper bound:** For any $\epsilon > 0$, we can cover $\bar{I}$ by a single open rectangle
>
> $$
> I_\epsilon = (a_1 - \epsilon, b_1 + \epsilon) \times \cdots \times (a_n - \epsilon, b_n + \epsilon).
> $$
>
> Then $|I_\epsilon| = \prod_{j=1}^{n} (b_j - a_j + 2\epsilon)$.
>
> As $\epsilon \to 0^+$, $|I_\epsilon| \to |I|$.
>
> Thus $m^*(\bar{I}) \leq |I|$.
>
> **Lower bound:** Let $\{I_k\}$ be any L-covering of $\bar{I}$. We must show $\sum_k |I_k| \geq |\bar{I}| = |I|$.
>
> Since $\bar{I}$ is closed and bounded, it is compact by [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|Heine–Borel]]. The open rectangles $\{I_k\}$ form an open cover of $\bar{I}$, so there exists a finite subcover $\{I_{k_1}, I_{k_2}, \ldots, I_{k_m}\}$ with
>
> $$
> \bar{I} \subseteq \bigcup_{j=1}^{m} I_{k_j}.
> $$
>
> Thus $\sum_k |I_k| \geq \sum_{j=1}^{m} |I_{k_j}| \geq |\bar{I}|$ (the last inequality uses the fact that a finite union of open rectangles covering a closed rectangle has total volume at least the volume of the rectangle).
>
> Therefore $m^*(\bar{I}) = \inf \sum_k |I_k| \geq |I|$.
>
> Combining: $m^*(\bar{I}) = |I|$.
>
> If $J$ is an open or half-open rectangle with the same edges, then $J \subseteq \bar{I}$ gives $m^*(J) \leq |I|$ by [[§10 Lebesgue Outer Measure#^prop-10-1|monotonicity]]; conversely, for small $\delta > 0$, $J$ contains the closed rectangle $\prod_{j} [a_j + \delta, b_j - \delta]$, so $m^*(J) \geq \prod_{j} (b_j - a_j - 2\delta) \to |I|$ as $\delta \to 0^+$. Hence $m^*(J) = |I|$.

^pf-10-2

*Uses:* [[§10 Lebesgue Outer Measure#^def-10-4|Def. §10.4]], [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|§6.4]], [[§10 Lebesgue Outer Measure#^prop-10-1|§10.1]]

![[m551-9-3.svg]]
*The two halves of [[§10 Lebesgue Outer Measure#^prop-10-2|Proposition §10.2]]. Left (upper bound): a single open rectangle $I_\epsilon$ (dashed red), enlarged by $\epsilon$ on every side, already covers $\bar I$, and $|I_\epsilon| \to |I|$. Right (lower bound): by Heine–Borel any L-covering of $\bar I$ has a finite subcover $I_{k_1}, \dots, I_{k_m}$ (dashed red); overlaps (darker) are counted more than once, so the total volume can only exceed $|I|$ — the claim whose proof [[§10 Lebesgue Outer Measure#^rem-10-2|Remark §9.2]] omits.*

> [!remark]- Connections
> - Topology version of the compactness step: [[Heine–Borel Theorem]].
> - MATH 452 counterpart: [[§20 Multivariable Integration#^def-20-7|Jordan content (452 Def. §20.7)]], built from rectangles whose area is defined by hand ([[§20 Multivariable Integration#^def-20-2|452 Def. §20.2]]).

> [!remark] Remark
> The lower bound argument uses [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|Heine–Borel]] crucially. The claim that a finite union of open rectangles covering $\bar{I}$ has total volume $\geq |\bar{I}|$ requires additional justification (which we omit here).

^rem-10-2

## Translation Invariance

> [!theorem] Proposition §10.3: Translation Invariance of Outer Measure
> Let $A \subseteq \mathbb{R}^n$ and $x_0 \in \mathbb{R}^n$. Define $x_0 + A = \{x_0 + y \mid y \in A\}$.
>
> Then $m^*(x_0 + A) = m^*(A)$.

^prop-10-3

> [!proof]+ Proof
> Let $\{I_k\}$ be an L-covering of $A$. Then $\{x_0 + I_k\}$ is an L-covering of $x_0 + A$.
>
> Since translation preserves volume, $|x_0 + I_k| = |I_k|$ for each $k$.
>
> Thus $\sum_k |x_0 + I_k| = \sum_k |I_k|$.
>
> Taking infimum over all L-coverings: $m^*(x_0 + A) \leq m^*(A)$.
>
> By symmetry (applying the same argument with $-x_0$): $m^*(A) = m^*(-x_0 + (x_0 + A)) \leq m^*(x_0 + A)$.
>
> Therefore $m^*(x_0 + A) = m^*(A)$.

^pf-10-3

*Uses:* [[§10 Lebesgue Outer Measure#^def-10-2|Def. §10.2]], [[§10 Lebesgue Outer Measure#^def-10-3|Def. §10.3]], [[§10 Lebesgue Outer Measure#^def-10-4|Def. §10.4]]

> [!remark]- Connections
> - Measurable sets are carried to measurable sets: [[§14 The Vitali Set and the Cantor Set#^lem-14-1|Lemma §14.1]]; key input to the [[The Vitali Set is Not Measurable|Vitali set]].
> - Translation invariance of the integral: [[§25 Invariance Properties and Fubini's Theorem#^thm-25-1|Thm. §25.1]].
