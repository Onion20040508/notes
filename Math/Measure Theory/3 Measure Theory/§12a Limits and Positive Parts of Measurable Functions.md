---
type: section
subject: "[[Measure Theory]]"
chapter: 3
section: 12
tags: [measure-theory, math551]
---
← [[§12 Measurable Functions]] · ↑ [[· 3 Measure Theory]] · [[§13 Egorov's and Lusin's Theorems]] →

Measurability survives the limiting operations of analysis: suprema and infima, limsup and liminf, and pointwise limits. This section also treats reciprocals and quotients, the positive and negative parts $f^+$ and $f^-$, and properties that hold almost everywhere.

## Suprema, Infima, and Limits of Measurable Functions

> [!theorem] Theorem §12.6: Measurability of Suprema and Infima
> Let $E \in \mathcal{M}$ and let $\{f_k\}_{k \geq 1}$ be a sequence (finite or infinite) of measurable functions on $E$. Then:
> 1. $\displaystyle\sup_{k \geq 1} f_k(x): E \to \overline{\mathbb{R}}$ is measurable.
> 2. $\displaystyle\inf_{k \geq 1} f_k(x): E \to \overline{\mathbb{R}}$ is measurable.

^thm-12-6

> [!proof]+ Proof
> **(1)** Let $c \in \mathbb{R}$. We have:
>
> $$
> \sup_{k \geq 1} f_k(x_0) > c \iff \exists k \geq 1 \text{ such that } f_k(x_0) > c.
> $$
>
> Therefore:
>
> $$
> \left\{x \in E \mid \sup_{k \geq 1} f_k(x) > c\right\} = \bigcup_{k=1}^{\infty} \{x \in E \mid f_k(x) > c\} \in \mathcal{M}
> $$
>
> as a countable union of measurable sets.
>
> **(2)** Note that $\inf_{k \geq 1} f_k(x) = -\sup_{k \geq 1}(-f_k(x))$. Since $-f_k$ is measurable for each $k$ (by [[§12 Measurable Functions#^thm-12-3|scaling]] with $a = -1$), the supremum is measurable by (1), and hence the infimum is measurable.

^pf-12-6

*Uses:* [[§12 Measurable Functions#^def-12-2|Def. §12.2]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]], [[§12 Measurable Functions#^thm-12-3|§12.3]], [[Characterization of the Supremum|451 Characterization of the Supremum]]

> [!theorem] Theorem §12.7: Measurability of Limsup and Liminf
> Let $E \in \mathcal{M}$ and let $\{f_k\}_{k \geq 1}$ be a sequence of measurable functions on $E$. Then:
> 1. $\displaystyle\limsup_{k \to \infty} f_k(x): E \to \overline{\mathbb{R}}$ is measurable.
> 2. $\displaystyle\liminf_{k \to \infty} f_k(x): E \to \overline{\mathbb{R}}$ is measurable.

^thm-12-7

> [!proof]+ Proof
> [[§10 Monotone Sequences and Cauchy Sequences#^def-10-3|Recall the definitions]]:
>
> $$
> \limsup_{k \to \infty} f_k(x) = \inf_{j \geq 1} \sup_{k \geq j} f_k(x), \qquad \liminf_{k \to \infty} f_k(x) = \sup_{j \geq 1} \inf_{k \geq j} f_k(x).
> $$
>
> For each fixed $j$, let $g_j(x) = \sup_{k \geq j} f_k(x)$. By [[§12 Measurable Functions#^thm-12-6|the previous theorem]], each $g_j$ is measurable. Then $\limsup_{k \to \infty} f_k(x) = \inf_{j \geq 1} g_j(x)$ is measurable as the infimum of measurable functions.
>
> Similarly for $\liminf$.

^pf-12-7

*Uses:* [[§12 Measurable Functions#^thm-12-6|§12.6]], [[§10 Monotone Sequences and Cauchy Sequences#^def-10-3|451 Def. §10.3]]

> [!remark] Remark: Recalling Limsup and Liminf for Sequences
> For a sequence $\{a_k\}$ of real numbers:
>
> $$
> \limsup_{k \to \infty} a_k = \lim_{j \to \infty} \sup_{k \geq j} a_k = \inf_{j \geq 1} \sup_{k \geq j} a_k.
> $$
>
> The sequence $b_j = \sup_{k \geq j} a_k$ is [[§10 Monotone Sequences and Cauchy Sequences#^lem-10-4|decreasing]] (as $j$ increases, we take the sup over fewer terms), so [[Monotone Convergence Theorem|the limit equals the infimum]].

^rem-12-4

> [!theorem] Corollary §12.8: Pointwise Limits of Measurable Functions
> If $\{f_k\}$ is a sequence of measurable functions on $E$ and $f_k(x) \to f(x)$ pointwise for all $x \in E$, then $f$ is measurable.

^cor-12-8

> [!proof]+ Proof
> If $f_k \to f$ pointwise, then $f(x) = \lim_{k \to \infty} f_k(x) = \limsup_{k \to \infty} f_k(x) = \liminf_{k \to \infty} f_k(x)$ ([[§10 Monotone Sequences and Cauchy Sequences#^thm-10-6|451 Theorem §10.6]]), which is measurable.

^pf-12-8

*Uses:* [[§12 Measurable Functions#^thm-12-7|§12.7]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-6|451 §10.6]]

> [!remark]- Connections
> - Contrast with continuity: a pointwise limit of continuous functions need not be continuous ([[§24 Uniform Convergence#^ex-24-2|451 Example §24.2]]); measurability survives pointwise limits, continuity needs uniform ones ([[§12 Measurable Functions#^thm-12-16|Theorem §12.16]]).
> - The a.e. version: [[§12 Measurable Functions#^rem-12-7|Remark: A.e. Convergence Preserves Measurability]].

## Reciprocals and Quotients of Measurable Functions

> [!theorem] Proposition §12.9: Measurability of $1/f$
> Let $f$ be a measurable function on $E$ with $f(x) \neq 0$ a.e. on $E$. Then $1/f$ is measurable on $E$.

^prop-12-9

> [!proof]+ Proof
> Let $Z = \{x \in E : f(x) = 0\}$. Since $f$ is measurable, $Z = \{f \leq 0\} \cap \{f \geq 0\}$ is measurable, and $m(Z) = 0$ by hypothesis ([[§12 Measurable Functions#^def-12-5|a.e.]]). Let $E_0 = E \setminus Z$, which is measurable.
>
> Define $g(x) = 1/f(x)$ for $x \in E_0$ and $g(x) = 0$ for $x \in Z$. We show $g$ is measurable on $E$.
>
> For any $c \in \mathbb{R}$, we analyze $\{x \in E : g(x) > c\}$:
>
> $$
> \{x \in E : g(x) > c\} = \{x \in E_0 : 1/f(x) > c\} \cup \{x \in Z : 0 > c\}.
> $$
>
> The second set is either $Z$ (if $c < 0$) or $\emptyset$ (if $c \geq 0$), both measurable.
>
> For the first set, on $E_0$ where $f \neq 0$, we split into $\{f > 0\}$ and $\{f < 0\}$:
>
> $$
> \begin{aligned}
> \{x \in E_0 : 1/f(x) > c\} &= \bigl(\{f > 0\} \cap \{1/f > c\}\bigr) \cup \bigl(\{f < 0\} \cap \{1/f > c\}\bigr) \\
> &= \begin{cases}
> \{f > 0\} \cap \{f < 1/c\} & \text{if } c > 0, \\
> \{f > 0\} \cup \bigl(\{f < 0\} \cap \{f < 1/c\}\bigr) = \{f > 0\} \cup \{f < 1/c\} & \text{if } c < 0, \\
> \{f > 0\} & \text{if } c = 0.
> \end{cases}
> \end{aligned}
> $$
>
> (When $f > 0$: $1/f > c > 0$ iff $f < 1/c$, and $1/f > c$ is automatic if $c \leq 0$. When $f < 0$: $1/f < 0$, so $1/f > c$ is impossible if $c \geq 0$, while for $c < 0$ it holds iff $f < 1/c$, by multiplying by $f < 0$ and then dividing by $c < 0$.)
>
> In every case, the resulting set is a union/intersection of measurable sets $\{f > \alpha\}$, $\{f < \beta\}$, hence measurable. Since $\{g > c\}$ is measurable for all $c$, $g$ is measurable on $E$.

^pf-12-9

*Uses:* [[§12 Measurable Functions#^prop-12-2|§12.2]], [[§12 Measurable Functions#^def-12-5|Def. §12.5]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]], [[§12 Measurable Functions#^def-12-2|Def. §12.2]]

> [!remark] Remark
> Since the product and sum of measurable functions are measurable ([[§12 Measurable Functions#^thm-12-3|Theorem §12.3]]), this immediately gives: if $f$ and $g$ are measurable and $g \neq 0$ a.e., then $f/g = f \cdot (1/g)$ is measurable.

^rem-12-5

## Positive and Negative Parts

> [!definition] Definition §12.4: Positive and Negative Parts
> Let $f: E \to \overline{\mathbb{R}}$ be a function. Define:
>
> $$
> \begin{aligned}
> f^+(x) &= \max\{f(x), 0\} = \begin{cases} f(x) & \text{if } f(x) \geq 0 \\ 0 & \text{if } f(x) < 0 \end{cases} \\[1ex]
> f^-(x) &= \max\{-f(x), 0\} = \begin{cases} 0 & \text{if } f(x) \geq 0 \\ -f(x) & \text{if } f(x) < 0 \end{cases}
> \end{aligned}
> $$
>
> Note that $f^+ \geq 0$ and $f^- \geq 0$.

^def-12-4

![[m551-12-2.svg]]
*Positive and negative parts: $f^+$ (blue) keeps the part of the graph of $f$ above the axis, $f^-$ (red) flips the part below (dashed) upward, and each is $0$ where the other is active. Hence $f = f^+ - f^-$ and $|f| = f^+ + f^-$ (Proposition §12.10).*

> [!theorem] Proposition §12.10: Properties of $f^+$ and $f^-$
> For any $f: E \to \overline{\mathbb{R}}$:
> 1. $f(x) = f^+(x) - f^-(x)$ for all $x \in E$.
> 2. $|f(x)| = f^+(x) + f^-(x)$ for all $x \in E$.

^prop-12-10

> [!proof]+ Proof
> **(1)** If $f(x) \geq 0$: $f^+(x) - f^-(x) = f(x) - 0 = f(x)$. If $f(x) < 0$: $f^+(x) - f^-(x) = 0 - (-f(x)) = f(x)$.
>
> **(2)** If $f(x) \geq 0$: $f^+(x) + f^-(x) = f(x) + 0 = |f(x)|$. If $f(x) < 0$: $f^+(x) + f^-(x) = 0 + (-f(x)) = |f(x)|$.

^pf-12-10

*Uses:* [[§12 Measurable Functions#^def-12-4|Def. §12.4]]

> [!theorem] Proposition §12.11: Measurability of $f^+$ and $f^-$
> $f: E \to \overline{\mathbb{R}}$ is measurable if and only if both $f^+$ and $f^-$ are measurable.

^prop-12-11

> [!proof]+ Proof
> $(\Rightarrow)$ Assume $f$ is measurable. For $c \in \mathbb{R}$:
>
> $$
> \{x \in E \mid f^+(x) > c\} = \begin{cases}
> E & \text{if } c < 0 \\
> \{x \in E \mid f(x) > c\} & \text{if } c \geq 0
> \end{cases}
> $$
>
> Both cases give measurable sets. Similarly for $f^- = (-f)^+$.
>
> $(\Leftarrow)$ If $f^+$ and $f^-$ are measurable, then $f = f^+ - f^-$ is measurable. Here $f^+$ and $f^-$ are never both nonzero, so no $\infty - \infty$ occurs, but they may take the value $+\infty$, so instead of the [[§12 Measurable Functions#^thm-12-3|arithmetic theorem]] (stated for real-valued functions) we argue directly: for $c \in \mathbb{R}$,
>
> $$
> \{x \in E \mid f(x) > c\} = \begin{cases}
> \{x \in E \mid f^+(x) > c\} & \text{if } c \geq 0 \\
> \{x \in E \mid f^-(x) < -c\} & \text{if } c < 0
> \end{cases}
> $$
>
> and both sets are measurable ([[§12 Measurable Functions#^prop-12-2|Prop. §12.2]]).

^pf-12-11

*Uses:* [[§12 Measurable Functions#^def-12-2|Def. §12.2]], [[§12 Measurable Functions#^prop-12-10|§12.10]], [[§12 Measurable Functions#^prop-12-2|§12.2]]

> [!remark]- Connections
> - The splitting $f = f^+ - f^-$ is how the general integral is defined: [[§15 The General Lebesgue Integral#^def-15-1|Def. §15.1]].

## Almost Everywhere (a.e.)

> [!definition] Definition §12.5: Almost Everywhere
> Let $E \in \mathcal{M}$ and let $P(x)$ be a property that may or may not hold at each point $x \in E$. We say $P(x)$ holds **almost everywhere** on $E$ (abbreviated **a.e.**) if
>
> $$
> m\left(\{x \in E \mid P(x) \text{ does not hold}\}\right) = 0.
> $$
>
> We write “$P(x)$ holds for a.e. $x \in E$” or “$P(x)$ a.e. $x \in E$.” (Here $m$ is [[§10 Lebesgue Measurable Sets#^def-10-5|Lebesgue measure]].)

^def-12-5

> [!example] Example §12.3: Common Uses of “Almost Everywhere”
> - $f(x) = g(x)$ a.e. on $E$ means $m(\{x \in E \mid f(x) \neq g(x)\}) = 0$.
> - $f: E \to \overline{\mathbb{R}}$ is **a.e. finite** means $m(\{x \in E \mid |f(x)| = +\infty\}) = 0$.
> - $f_k(x) \to f(x)$ a.e. means $m(\{x \in E \mid f_k(x) \not\to f(x)\}) = 0$.

^ex-12-3

> [!theorem] Proposition §12.12: Functions Equal a.e. to Measurable Functions
> Assume $f: E \to \overline{\mathbb{R}}$ is measurable. If $g(x) = f(x)$ for a.e. $x \in E$, then $g$ is measurable.

^prop-12-12

> [!proof]+ Proof
> Let $A = \{x \in E \mid g(x) \neq f(x)\}$. By assumption, $m(A) = 0$, so $A \in \mathcal{M}$ ([[§10 Lebesgue Measurable Sets#^ex-10-1|measure zero sets are measurable]]).
>
> For any $c \in \mathbb{R}$:
>
> $$
> \{x \in E \mid g(x) > c\} = \{x \in A \mid g(x) > c\} \cup \{x \in E \setminus A \mid g(x) > c\}.
> $$
>
> The first set $\{x \in A \mid g(x) > c\} \subseteq A$ has measure zero, hence is measurable.
>
> For $x \in E \setminus A$, we have $g(x) = f(x)$, so:
>
> $$
> \{x \in E \setminus A \mid g(x) > c\} = \{x \in E \setminus A \mid f(x) > c\} = (E \setminus A) \cap \{x \in E \mid f(x) > c\} \in \mathcal{M}.
> $$
>
> Therefore $\{x \in E \mid g(x) > c\} \in \mathcal{M}$.

^pf-12-12

*Uses:* [[§10 Lebesgue Measurable Sets#^ex-10-1|Ex. §10.1]], [[Properties of Lebesgue Outer Measure|§9.1]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]], [[§12 Measurable Functions#^def-12-2|Def. §12.2]]

> [!remark]- Connections
> - This is where completeness of Lebesgue measure (every subset of a null set is measurable) enters; the integral ignores such changes too: [[§14 The Lebesgue Integral for Simple Functions#^prop-14-9|Proposition §14.9]].
