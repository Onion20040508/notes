---
type: section
subject: "[[Measure Theory]]"
chapter: 3
section: 12
tags: [measure-theory, math551]
---
← [[§11 Borel Sets and Measure Spaces]] · ↑ [[3 Measure Theory]] · [[§13 Egorov's and Lusin's Theorems]] →

## Extended Real Numbers

To handle functions that may take infinite values (such as $f(x) = 1/x$ near $0$), we extend the real numbers.

> [!definition] Definition §12.1: Extended Real Numbers
> The **extended real numbers** are
>
> $$
> \overline{\mathbb{R}} = \mathbb{R} \cup \{+\infty, -\infty\}.
> $$
>
> We may also write this as $\mathbb{R} \cup \{\pm\infty\}$.

^def-12-1

> [!remark] Note: Arithmetic Conventions
> We adopt the following conventions for arithmetic in $\overline{\mathbb{R}}$:
> - $+\infty + (+\infty) = +\infty$, $(-\infty) + (-\infty) = -\infty$
> - $(+\infty) \cdot (-\infty) = -\infty$
> - For $x \in \mathbb{R}$: $x + (+\infty) = +\infty$, $x + (-\infty) = -\infty$, $x \pm \infty = \pm\infty$
> - $0 \cdot (\pm\infty) = 0$ (important convention for integration)
> - $(+\infty) - (+\infty)$ is **undefined** (indeterminate form)

^rem-12-1

> [!remark]- Connections
> - MATH 451 treatment of $\pm\infty$: [[§5 The Symbols +∞, −∞#^rem-5-1|451 §5: Arithmetic with infinities]]; the function $1/x$: [[Reciprocal function 1∕x]].
> - The convention $0 \cdot \infty = 0$ is what makes the integral of simple functions well defined: [[§14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]].

## Definition of Measurable Functions

> [!definition] Definition §12.2: Measurable Function
> Let $E \subseteq \mathbb{R}^n$ be a [[§10 Lebesgue Measurable Sets#^def-10-1|measurable]] set and let $f: E \to \overline{\mathbb{R}}$ be an extended real-valued function defined on $E$. We say $f$ is **(Lebesgue) measurable** if for all $c \in \mathbb{R}$,
>
> $$
> \{x \in E \mid f(x) > c\} \in \mathcal{M}
> $$
>
> ($\mathcal{M}$: [[§10 Lebesgue Measurable Sets#^def-10-2|Def. §10.2]]).

^def-12-2

![[m551-12-1.svg]]
*The sets in Definition §12.2 are horizontal slices: $\{f > c\}$ (red, on the $x$-axis) is where the graph lies strictly above the line $y = c$. For this continuous $f$ it is relatively open in $[a,b]$: hollow endpoints where $f = c$, a filled one at $b$ (Example §12.2). For a general measurable $f$ it can be far wilder, but it must still be measurable.*

> [!remark] Remark: Geometric Interpretation
> For a function $f: [a, b] \to \mathbb{R}$, the set $\{x \in [a, b] \mid c_1 < f(x) < c_2\}$ represents the portion of the domain where the graph lies between the horizontal lines $y = c_1$ and $y = c_2$. Measurability ensures that such “horizontal slices” of the domain are always measurable sets.

^rem-12-2

> [!example] Example §12.1: Monotone Functions are Measurable
> Assume $f: [a, b] \to \mathbb{R}$ is monotone. Then $f$ is measurable.
>
> For any $c \in \mathbb{R}$, the set $\{x \in [a, b] \mid f(x) > c\}$ is one of the following:
> - An interval (open, closed, or half-open)
> - The empty set $\emptyset$
> - A single point
>
> In all cases, this set is measurable (intervals and singletons are [[§11 Borel Sets and Measure Spaces#^def-11-2|Borel sets]]; [[§11 Borel Sets and Measure Spaces#^cor-11-7|Cor. §11.7]]).

^ex-12-1

> [!remark]- Connections
> - Monotone functions reappear in differentiation theory: [[§18 Differentiation Theory#^thm-18-1|Monotone Functions Have Countably Many Discontinuities]], [[Lebesgue's Differentiation Theorem for Monotone Functions|Lebesgue's Differentiation Theorem]].

> [!example] Example §12.2: Continuous Functions are Measurable
> If $f: E \to \mathbb{R}$ is continuous (where $E \subseteq \mathbb{R}^n$ is measurable), then $f$ is measurable.
>
> For any $c \in \mathbb{R}$, the set $\{x \in E \mid f(x) > c\} = f^{-1}((c, \infty)) \cap E$ is the intersection of an open set (by [[§9 Continuous Functions#^def-9-1|continuity]]) with the measurable set $E$, hence measurable ([[§11 Borel Sets and Measure Spaces#^thm-11-6|Thm. §11.6]], [[Lebesgue Measurable Sets Form a σ-Algebra|Thm. §10.3]]).

^ex-12-2

> [!remark]- Connections
> - “Open preimage” is relative to $E$: an open set of the [[§5 Subspace Topology#^def-5-1|subspace topology]] on $E$ is $U \cap E$ with $U$ open in $\mathbb{R}^n$.
> - A partial converse: every measurable function is continuous off a set of small measure, [[Lusin's Theorem|Lusin's Theorem]].

> [!definition] Definition §12.3: Characteristic Function
> Let $E \subseteq \mathbb{R}^n$. The **characteristic function** (or **indicator function**) of $E$ is:
>
> $$
> \chi_E(x) = \mathbf{1}_E(x) = \begin{cases} 1 & \text{if } x \in E \\ 0 & \text{if } x \notin E \end{cases}
> $$

^def-12-3

> [!theorem] Proposition §12.1: Characteristic Functions of Measurable Sets
> If $E \in \mathcal{M}$, then $\chi_E$ is a measurable function.

^prop-12-1

> [!proof]+ Proof
> For any $c \in \mathbb{R}$:
>
> $$
> \{x \in \mathbb{R}^n \mid \chi_E(x) > c\} = \begin{cases}
> \emptyset & \text{if } c \geq 1 \\
> E & \text{if } 0 \leq c < 1 \\
> \mathbb{R}^n & \text{if } c < 0
> \end{cases}
> $$
>
> In all cases, the set is measurable (since $E \in \mathcal{M}$ by assumption).

^pf-12-1

*Uses:* [[§12 Measurable Functions#^def-12-2|Def. §12.2]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]]

> [!remark]- Connections
> - The Dirichlet function $\chi_{\mathbb{Q}}$ is measurable (as $\mathbb{Q}$ is countable, hence null) though not Riemann integrable: [[§8 Motivation꞉ The Riemann Integral#^ex-8-2|Ex. §8.2]], [[Dirichlet and Thomae functions]].

## Equivalent Characterizations of Measurability

> [!theorem] Proposition §12.2: Equivalent Conditions for Measurability
> Let $E \in \mathcal{M}$ and $f: E \to \overline{\mathbb{R}}$ be a measurable function. Then the following sets are all measurable:
> 1. $\forall c \in \mathbb{R}$: $\{x \in E \mid f(x) > c\} \in \mathcal{M}$ (definition)
> 2. $\forall c \in \mathbb{R}$: $\{x \in E \mid f(x) < c\} \in \mathcal{M}$
> 3. $\forall c \in \mathbb{R}$: $\{x \in E \mid f(x) \leq c\} \in \mathcal{M}$
> 4. $\forall c \in \mathbb{R}$: $\{x \in E \mid f(x) \geq c\} \in \mathcal{M}$
> 5. $\forall c \in \mathbb{R}$: $\{x \in E \mid f(x) = c\} \in \mathcal{M}$
> 6. $\{x \in E \mid f(x) < +\infty\} \in \mathcal{M}$, $\{x \in E \mid f(x) > -\infty\} \in \mathcal{M}$
> 7. $\{x \in E \mid f(x) = +\infty\} \in \mathcal{M}$, $\{x \in E \mid f(x) = -\infty\} \in \mathcal{M}$
>
> Moreover, any one of conditions (1)–(4) can be used as the definition of measurability.

^prop-12-2

> [!proof]+ Proof
> We derive each condition from (1).
>
> **(4) $\{f \geq c\}$ is measurable:** Observe that
>
> $$
> f(x) \geq c \iff f(x) > c - \frac{1}{k} \text{ for all } k \in \mathbb{N}.
> $$
>
> Therefore:
>
> $$
> \{x \in E \mid f(x) \geq c\} = \bigcap_{k=1}^{\infty} \left\{x \in E \mid f(x) > c - \frac{1}{k}\right\} \in \mathcal{M}
> $$
>
> as a countable intersection of measurable sets.
>
> **(2) $\{f < c\}$ is measurable:**
>
> $$
> \{x \in E \mid f(x) < c\} = E \setminus \{x \in E \mid f(x) \geq c\} \in \mathcal{M}.
> $$
>
> **(3) $\{f \leq c\}$ is measurable:**
>
> $$
> \{x \in E \mid f(x) \leq c\} = E \setminus \{x \in E \mid f(x) > c\} \in \mathcal{M}.
> $$
>
> **(5) $\{f = c\}$ is measurable:**
>
> $$
> \{x \in E \mid f(x) = c\} = \{x \in E \mid f(x) \geq c\} \cap \{x \in E \mid f(x) \leq c\} \in \mathcal{M}.
> $$
>
> **(6) $\{f < +\infty\}$ and $\{f > -\infty\}$ are measurable:**
>
> $$
> f(x) < +\infty \iff \exists k \in \mathbb{N} \text{ such that } f(x) < k.
> $$
>
> Therefore:
>
> $$
> \{x \in E \mid f(x) < +\infty\} = \bigcup_{k=1}^{\infty} \{x \in E \mid f(x) < k\} \in \mathcal{M}.
> $$
>
> Similarly, $\{x \in E \mid f(x) > -\infty\} = \bigcup_{k=1}^{\infty} \{x \in E \mid f(x) > -k\} \in \mathcal{M}$.
>
> **(7) $\{f = +\infty\}$ and $\{f = -\infty\}$ are measurable:**
>
> $$
> \{x \in E \mid f(x) = +\infty\} = E \setminus \{x \in E \mid f(x) < +\infty\} = \bigcap_{k=1}^{\infty} \{x \in E \mid f(x) > k\} \in \mathcal{M}.
> $$
>
> Similarly for $\{f = -\infty\}$.
>
> **Conversely, each of (2)–(4) implies (1):** (3) gives (1) since $\{f > c\} = E \setminus \{f \leq c\}$; (2) gives (4) since $\{f \geq c\} = E \setminus \{f < c\}$; and (4) gives (1) since $\{f > c\} = \bigcup_{k=1}^{\infty} \{f \geq c + \frac{1}{k}\}$. So (1)–(4) are equivalent, and any one of them can serve as the definition.

^pf-12-2

*Uses:* [[§12 Measurable Functions#^def-12-2|Def. §12.2]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]]

## Algebra of Measurable Functions

> [!theorem] Theorem §12.3: Arithmetic Operations Preserve Measurability
> Let $E \in \mathcal{M}$ and assume $f: E \to \mathbb{R}$, $g: E \to \mathbb{R}$ are measurable functions. Then:
> 1. $f + g: E \to \mathbb{R}$ is measurable.
> 2. For all $a \in \mathbb{R}$, $af: E \to \mathbb{R}$ is measurable.
> 3. $fg: E \to \mathbb{R}$ is measurable.

^thm-12-3

> [!proof]+ Proof
> **(2)** is straightforward: if $a = 0$, then $af \equiv 0$ is constant, hence measurable. If $a > 0$:
>
> $$
> \{x \in E \mid af(x) > c\} = \{x \in E \mid f(x) > c/a\} \in \mathcal{M}.
> $$
>
> If $a < 0$:
>
> $$
> \{x \in E \mid af(x) > c\} = \{x \in E \mid f(x) < c/a\} \in \mathcal{M}.
> $$
>
> **(1)** Let $c \in \mathbb{R}$. We want to show $\{x \in E \mid f(x) + g(x) > c\} \in \mathcal{M}$.
>
> *Key observation:* $f(x_0) + g(x_0) > c$ if and only if there exists $r \in \mathbb{Q}$ such that $f(x_0) > r$ and $g(x_0) > c - r$.
>
> *Proof of observation:* If $f(x_0) + g(x_0) > c$, then $f(x_0) > c - g(x_0)$. By [[§4 The Completeness Axiom#^thm-4-7|density of ℚ in ℝ]], there exists $r \in \mathbb{Q}$ with $c - g(x_0) < r < f(x_0)$. Then $f(x_0) > r$ and $g(x_0) > c - r$. The converse is immediate: $f(x_0) > r$ and $g(x_0) > c - r$ implies $f(x_0) + g(x_0) > c$.
>
> Let $\mathbb{Q} = \{r_1, r_2, r_3, \ldots\}$ be [[§3 Countability of Rationals and Unions#^cor-3-2|an enumeration of the rationals]]. Then:
>
> $$
> \{x \in E \mid f(x) + g(x) > c\} = \bigcup_{j=1}^{\infty} \left(\{x \in E \mid f(x) > r_j\} \cap \{x \in E \mid g(x) > c - r_j\}\right) \in \mathcal{M}
> $$
>
> as a countable union of measurable sets.

^pf-12-3

*Uses:* [[§12 Measurable Functions#^def-12-2|Def. §12.2]], [[§12 Measurable Functions#^prop-12-2|§12.2]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]], [[§3 Countability of Rationals and Unions#^cor-3-2|§3.2]], [[§4 The Completeness Axiom#^thm-4-7|451 §4.7]]

> [!remark] Remark: Logic to Set Theory
> The proof illustrates a key technique: translate logical statements (“there exists $r$ such that...”) into set-theoretic operations (countable unions).

^rem-12-3

> [!proof]+ Proof of Theorem §12.3 (continued)
> **(3)** We prove this in two steps.
>
> *Step 1: $f$ measurable implies $f^2$ measurable.*
>
> For any $c \in \mathbb{R}$:
>
> $$
> \{x \in E \mid f(x)^2 > c\} = \begin{cases}
> E & \text{if } c < 0 \\[1ex]
> \{x \in E \mid f(x) > \sqrt{c}\} \cup \{x \in E \mid f(x) < -\sqrt{c}\} & \text{if } c \geq 0
> \end{cases}
> $$
>
> In both cases, the set is measurable. (For $c \geq 0$: $f(x)^2 > c \iff |f(x)| > \sqrt{c} \iff f(x) > \sqrt{c}$ or $f(x) < -\sqrt{c}$.)
>
> *Step 2: Use the polarization identity.*
>
> Since $f + g$ and $f - g$ are measurable by (1), their squares are measurable by Step 1. Then:
>
> $$
> fg = \frac{(f + g)^2 - (f - g)^2}{4}
> $$
>
> is measurable by (2) and (1).

^pf-12-3-cont

*Uses:* [[§12 Measurable Functions#^def-12-2|Def. §12.2]], [[§12 Measurable Functions#^prop-12-2|§12.2]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]]

> [!remark]- Connections
> - The continuous counterpart: [[§17 Continuous Functions#^thm-17-3|451 Theorem §17.3: Arithmetic of Continuous Functions]].
> - The same “∃ ⇒ countable union” translation drives [[§12 Measurable Functions#^thm-12-6|Theorem §12.6]] and the set of convergence ([[§12 Measurable Functions#^prop-12-18|Proposition §12.18]]).

## Measurability on Subsets and Unions

> [!theorem] Proposition §12.4: Union of Domains
> Let $E_1, E_2 \in \mathcal{M}$. Assume $f: E_1 \to \overline{\mathbb{R}}$ and $f: E_2 \to \overline{\mathbb{R}}$ are measurable. Then $f: E_1 \cup E_2 \to \overline{\mathbb{R}}$ is measurable.

^prop-12-4

> [!proof]+ Proof
> For any $c \in \mathbb{R}$:
>
> $$
> \{x \in E_1 \cup E_2 \mid f(x) > c\} = \{x \in E_1 \mid f(x) > c\} \cup \{x \in E_2 \mid f(x) > c\} \in \mathcal{M}.
> $$

^pf-12-4

*Uses:* [[§12 Measurable Functions#^def-12-2|Def. §12.2]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]]

> [!theorem] Proposition §12.5: Restriction to Measurable Subsets
> Assume $f: E \to \overline{\mathbb{R}}$ is measurable, and $A \subseteq E$ with $A \in \mathcal{M}$. Then the restriction $f|_A: A \to \overline{\mathbb{R}}$ is measurable.

^prop-12-5

> [!proof]+ Proof
> For any $c \in \mathbb{R}$:
>
> $$
> \{x \in A \mid f(x) > c\} = A \cap \{x \in E \mid f(x) > c\} \in \mathcal{M}.
> $$

^pf-12-5

*Uses:* [[§12 Measurable Functions#^def-12-2|Def. §12.2]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]]

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

## Simple Functions

> [!definition] Definition §12.6: Simple Function
> A function $f: E \to \mathbb{R}$ is called **simple** if its range $R(f) = \{y \mid y = f(x) \text{ for some } x \in E\}$ has only finitely many elements.

^def-12-6

> [!theorem] Proposition §12.13: Canonical Representation of Simple Functions
> Let $f: E \to \mathbb{R}$ be a simple function with $R(f) = \{a_1, a_2, \ldots, a_n\} \subseteq \mathbb{R}$, where $a_i \neq a_j$ for $i \neq j$. Define
>
> $$
> E_j = \{x \in E \mid f(x) = a_j\}, \quad j = 1, \ldots, n.
> $$
>
> Then $E_i \cap E_j = \emptyset$ for $i \neq j$, $\bigcup_{j=1}^n E_j = E$, and
>
> $$
> f(x) = \sum_{j=1}^{n} a_j \chi_{E_j}(x).
> $$
>
> If $f$ is measurable, then each $E_j \in \mathcal{M}$.

^prop-12-13

> [!remark]- Connections
> - The canonical representation is the one used to define the integral of a simple function: [[§14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]].
> - Measurability of each $E_j$ is condition (5) of [[§12 Measurable Functions#^prop-12-2|Proposition §12.2]].

> [!definition] Definition §12.7: Support of a Function
> Let $f: E \to \overline{\mathbb{R}}$ be an extended real-valued function. The **support** of $f$ is
>
> $$
> \operatorname{supp} f = \overline{\{x \in E \mid f(x) \neq 0\}}.
> $$
>
> We say $f$ is **compactly supported** if $\operatorname{supp} f$ is compact (bounded and closed in $\mathbb{R}^n$, by [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|Heine–Borel]]). Equivalently, $f(x) = 0$ outside some bounded closed set.

^def-12-7

> [!remark]- Connections
> - General-topology form of “compact = bounded and closed”: [[Heine–Borel Theorem]].
> - Compactly supported continuous functions are dense in $L^1$: [[Continuous Functions of Compact Support are Dense in L¹|Theorem §16.7]].

## Approximation by Simple Functions

The following theorem shows that every non-negative measurable function can be approximated from below by simple functions.

> [!theorem] Theorem §12.14: Approximation by Simple Functions: Non-negative Case
> Let $f: E \to \mathbb{R} \cup \{+\infty\}$ be a non-negative measurable function. Then there exists an **increasing** sequence of measurable simple functions $\{\varphi_k\}_{k \geq 1}$ such that:
> 1. $0 \leq \varphi_1(x) \leq \varphi_2(x) \leq \cdots \leq \varphi_k(x) \leq \cdots$ for all $x \in E$.
> 2. $\displaystyle\lim_{k \to \infty} \varphi_k(x) = f(x)$ for all $x \in E$.

^thm-12-14

> [!proof]+ Proof
> For each $k \in \mathbb{N}$, we partition the range $[0, k)$ into $k \cdot 2^{k-1}$ intervals of length $\frac{1}{2^{k-1}}$:
>
> $$
> \left[0, \frac{1}{2^{k-1}}\right), \left[\frac{1}{2^{k-1}}, \frac{2}{2^{k-1}}\right), \ldots, \left[\frac{k \cdot 2^{k-1} - 1}{2^{k-1}}, k\right).
> $$
>
> Define the level sets:
>
> $$
> \begin{aligned}
> E_{kj} &= \left\{x \in E \;\middle|\; \frac{j-1}{2^{k-1}} \leq f(x) < \frac{j}{2^{k-1}}\right\}, \quad j = 1, 2, \ldots, k \cdot 2^{k-1}, \\
> E_k &= \{x \in E \mid f(x) \geq k\}.
> \end{aligned}
> $$
>
> Since $f$ is measurable, each $E_{kj}$ and $E_k$ is [[§12 Measurable Functions#^prop-12-2|measurable]]. Define:
>
> $$
> \varphi_k(x) = \sum_{j=1}^{k \cdot 2^{k-1}} \frac{j-1}{2^{k-1}} \chi_{E_{kj}}(x) + k \cdot \chi_{E_k}(x).
> $$
>
> **Claim 1: $\varphi_k$ is simple and measurable.**
>
> This is clear since $\varphi_k$ is a [[§12 Measurable Functions#^thm-12-3|finite linear combination]] of [[§12 Measurable Functions#^prop-12-1|characteristic functions of measurable sets]].
>
> **Claim 2: $\varphi_k(x) \leq \varphi_{k+1}(x)$ for all $x \in E$.**
>
> When we pass from $k$ to $k+1$, each interval $\left[\frac{j-1}{2^{k-1}}, \frac{j}{2^{k-1}}\right)$ is subdivided into two intervals of half the length:
>
> $$
> E_{kj} = E_{k+1, 2j-1} \cup E_{k+1, 2j},
> $$
>
> where
>
> $$
> E_{k+1, 2j-1} = \left\{x \in E \;\middle|\; \frac{2j-2}{2^k} \leq f(x) < \frac{2j-1}{2^k}\right\}, \quad E_{k+1, 2j} = \left\{x \in E \;\middle|\; \frac{2j-1}{2^k} \leq f(x) < \frac{2j}{2^k}\right\}.
> $$
>
> On $E_{k+1, 2j-1}$: $\varphi_{k+1}(x) = \frac{2j-2}{2^k} = \frac{j-1}{2^{k-1}} = \varphi_k(x)$.
>
> On $E_{k+1, 2j}$: $\varphi_{k+1}(x) = \frac{2j-1}{2^k} > \frac{2j-2}{2^k} = \frac{j-1}{2^{k-1}} = \varphi_k(x)$.
>
> Similarly, $E_k \supseteq E_{k+1}$, and $\varphi_{k+1}(x) \geq \varphi_k(x)$ on $E_k \setminus E_{k+1}$.
>
> **Claim 3: $\varphi_k(x) \to f(x)$ as $k \to \infty$.**
>
> *Case 1: $0 \leq f(x_0) < \infty$.* For $k > f(x_0)$, we have $x_0 \in E_{kj}$ for some $j$, so
>
> $$
> 0 \leq f(x_0) - \varphi_k(x_0) < \frac{1}{2^{k-1}} \to 0 \text{ as } k \to \infty.
> $$
>
> *Case 2: $f(x_0) = +\infty$.* Then $x_0 \in E_k$ for all $k$, so $\varphi_k(x_0) = k \to \infty = f(x_0)$.

^pf-12-14

*Uses:* [[§12 Measurable Functions#^prop-12-2|§12.2]], [[§12 Measurable Functions#^def-12-3|Def. §12.3]], [[§12 Measurable Functions#^prop-12-1|§12.1]], [[§12 Measurable Functions#^thm-12-3|§12.3]], [[§12 Measurable Functions#^def-12-6|Def. §12.6]]

![[m551-12-3.svg]]
*The staircase of Theorem §12.14. $\varphi_2$ (orange, shaded) rounds $f$ (blue) down to the grid of step $\tfrac12$ (gray lines) and is capped at $2$ on $E_2 = \{f \geq 2\}$; $\varphi_3$ (red) uses step $\tfrac14$ and cap $3$. Each step sits over a level set $E_{kj}$, so it is the range that gets partitioned. Halving the step can only raise a value, so $\varphi_2 \leq \varphi_3 \leq f$, and $f - \varphi_k < 2^{-(k-1)}$ wherever $f < k$.*

> [!remark]- Connections
> - Partitions the *range* of $f$, where Darboux sums partition the *domain*: [[§8 Motivation꞉ The Riemann Integral#^def-8-2|Def. §8.2]], [[§32 The Definition of the Riemann Integral|451 §32]].
> - With the [[Monotone Convergence Theorem (Lebesgue)|Monotone Convergence Theorem]] this gives $\int \varphi_k \to \int f$, used for [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|linearity of the integral]].

> [!theorem] Theorem §12.15: Approximation by Simple Functions: General Case
> Let $f: E \to \overline{\mathbb{R}}$ be a measurable function. Then there exists a sequence of measurable simple functions $\{\psi_k\}_{k \geq 1}$ such that:
> 1. $|\psi_k(x)| \leq |f(x)|$ for all $x \in E$ and all $k$.
> 2. $\displaystyle\lim_{k \to \infty} \psi_k(x) = f(x)$ for all $x \in E$.

^thm-12-15

> [!proof]+ Proof
> Write $f = f^+ - f^-$, where $f^+, f^- \geq 0$ are [[§12 Measurable Functions#^prop-12-11|measurable]].
>
> By [[Simple Function Approximation Theorem|the previous theorem]], there exist increasing sequences of non-negative simple functions $\{\varphi_k^{(1)}\}$ and $\{\varphi_k^{(2)}\}$ with
>
> $$
> \varphi_k^{(1)}(x) \to f^+(x), \qquad \varphi_k^{(2)}(x) \to f^-(x) \quad \text{for all } x \in E.
> $$
>
> Define $\psi_k(x) = \varphi_k^{(1)}(x) - \varphi_k^{(2)}(x)$. Then:
> - $\psi_k$ is simple ([[§12 Measurable Functions#^rem-12-6|the difference of two simple functions is simple]]).
> - $\psi_k(x) \to f^+(x) - f^-(x) = f(x)$ for all $x \in E$.
> - $|\psi_k(x)| \leq \varphi_k^{(1)}(x) + \varphi_k^{(2)}(x) \leq f^+(x) + f^-(x) = |f(x)|$.

^pf-12-15

*Uses:* [[§12 Measurable Functions#^prop-12-11|§12.11]], [[Simple Function Approximation Theorem|§12.14]], [[§12 Measurable Functions#^prop-12-10|§12.10]], [[§12 Measurable Functions#^rem-12-6|Rem. §12.6]]

> [!remark] Remark
> The difference of two simple functions is simple: if $\varphi = \sum a_i \chi_{A_i}$ and $\psi = \sum b_j \chi_{B_j}$, then $\varphi - \psi$ takes only finitely many values (at most $|\{a_i\}| \cdot |\{b_j\}|$ distinct values).

^rem-12-6

> [!remark]- Connections
> - Used for density of simple functions: [[§16 The L¹ Space and Density Theorems#^thm-16-5|in L¹ (Theorem §16.5)]] and [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|in Lᵖ (Theorem §19.19)]].

## Modes of Convergence

> [!definition] Definition §12.8: Pointwise and Almost Everywhere Convergence
> Let $\{f_k\}_{k \in \mathbb{N}}$ be a sequence of functions on $E$.
> - We say $f_k \to f$ **pointwise** on $E$ if $\displaystyle\lim_{k \to \infty} f_k(x) = f(x)$ for all $x \in E$.
> - We say $f_k \to f$ **almost everywhere** (a.e.) on $E$ if there exists a measure zero set $Z \subseteq E$ such that $\displaystyle\lim_{k \to \infty} f_k(x) = f(x)$ for all $x \in E \setminus Z$.
>
> We write $f_k \to f$ a.e. on $E$, or $f_k(x) \to f(x)$ for a.e. $x \in E$.

^def-12-8

> [!remark]- Connections
> - MATH 451 version of pointwise convergence: [[§24 Uniform Convergence#^def-24-1|451 Definition §24.1]].

> [!definition] Definition §12.9: Uniform Convergence
> We say $\{f_k\}$ converges **uniformly** to $f$ on $E$ if: for all $\epsilon > 0$, there exists $\ell \in \mathbb{N}$ such that for all $k \geq \ell$,
>
> $$
> \sup_{x \in E} |f_k(x) - f(x)| \leq \epsilon.
> $$

^def-12-9

> [!remark]- Connections
> - MATH 451: [[§24 Uniform Convergence#^def-24-2|451 Definition §24.2]]; the sup form used here is [[§24 Uniform Convergence#^thm-24-1|451 Theorem §24.1: Supremum Criterion]].

> [!example] Example §12.4: Pointwise but Not Uniform Convergence
> Let $f_k(x) = x^k$ for $x \in [0, 1]$. Then:
>
> $$
> f_k(x) \to f(x) = \begin{cases} 0 & \text{if } 0 \leq x < 1 \\ 1 & \text{if } x = 1 \end{cases}
> $$
>
> pointwise on $[0, 1]$.
>
> However, the convergence is **not uniform**. For $0 \leq x < 1$ and $\epsilon > 0$, we need $x^k < \epsilon$, i.e., $k \ln x < \ln \epsilon$, i.e., $k > \frac{\ln \epsilon}{\ln x}$. As $x \to 1^-$, $\ln x \to 0^-$, so $\frac{\ln \epsilon}{\ln x} \to +\infty$. No single $\ell$ works for all $x \in [0, 1)$.

^ex-12-4

> [!remark]- Connections
> - The same example in MATH 451: [[§24 Uniform Convergence#^ex-24-2|451 Example §24.2]].
> - Uniform after removing a small set near $1$: [[§13 Egorov's and Lusin's Theorems#^ex-13-1|Example §13.1]] ([[Egorov's Theorem|Egorov]]).

> [!theorem] Theorem §12.16: Uniform Limit of Continuous Functions
> Let $\{f_k\}_{k \in \mathbb{N}}$ be a sequence of continuous functions on $E$. If $f_k \to f$ uniformly on $E$, then $f$ is continuous on $E$.

^thm-12-16

> [!proof]+ Proof
> This is a [[§24 Uniform Convergence#^thm-24-2|standard result from MATH 451]] (Real Analysis). The key is that uniform convergence allows interchanging limits:
>
> $$
> \lim_{y \to x} f(y) = \lim_{y \to x} \lim_{k \to \infty} f_k(y) = \lim_{k \to \infty} \lim_{y \to x} f_k(y) = \lim_{k \to \infty} f_k(x) = f(x).
> $$

^pf-12-16

*Uses:* [[§24 Uniform Convergence#^thm-24-2|451 §24.2]]

> [!remark]- Connections
> - Used in Step 2 of [[Lusin's Theorem|Lusin's Theorem]].

> [!remark] Remark: A.e. Convergence Preserves Measurability
> If $\{f_k\}$ is a sequence of measurable functions on $E$ and $f_k \to f$ a.e. on $E$, then $f$ is measurable. (This follows from the fact that [[§12 Measurable Functions#^cor-12-8|pointwise limits of measurable functions are measurable]], combined with the proposition that [[§12 Measurable Functions#^prop-12-12|functions equal a.e. to measurable functions are measurable]].)

^rem-12-7

## Uniform Approximation of Bounded Measurable Functions

> [!theorem] Theorem §12.17: Uniform Approximation for Bounded Functions
> Let $f: E \to \mathbb{R}$ be a **bounded** measurable function. Then there exists a sequence of simple measurable functions $\{\psi_k\}$ such that:
> 1. $|\psi_k(x)| \leq |f(x)|$ for all $x \in E$ and all $k$.
> 2. $\psi_k \to f$ **uniformly** on $E$.

^thm-12-17

> [!proof]+ Proof
> Suppose $|f(x)| \leq M$ for all $x \in E$. Then $0 \leq f^+(x) \leq M$ and $0 \leq f^-(x) \leq M$.
>
> Let $\{\varphi_k^{(1)}\}$ and $\{\varphi_k^{(2)}\}$ be the approximating sequences for $f^+$ and $f^-$ from the [[Simple Function Approximation Theorem|approximation theorem]]. For $k > M$, every $x \in E$ satisfies $f^+(x) < k$, so $x \notin E_k$ (the set where $f^+ \geq k$). Thus:
>
> $$
> 0 \leq f^+(x) - \varphi_k^{(1)}(x) \leq \frac{1}{2^{k-1}} \quad \text{for all } x \in E.
> $$
>
> Similarly, $0 \leq f^-(x) - \varphi_k^{(2)}(x) \leq \frac{1}{2^{k-1}}$ for all $x \in E$.
>
> Let $\psi_k = \varphi_k^{(1)} - \varphi_k^{(2)}$. Then:
>
> $$
> \begin{aligned}
> |f(x) - \psi_k(x)| &= |f^+(x) - \varphi_k^{(1)}(x) - (f^-(x) - \varphi_k^{(2)}(x))| \\
> &\leq (f^+(x) - \varphi_k^{(1)}(x)) + (f^-(x) - \varphi_k^{(2)}(x)) \\
> &\leq \frac{1}{2^{k-1}} + \frac{1}{2^{k-1}} = \frac{2}{2^{k-1}} = \frac{1}{2^{k-2}}.
> \end{aligned}
> $$
>
> This bound is independent of $x$, so $\sup_{x \in E} |f(x) - \psi_k(x)| \leq \frac{1}{2^{k-2}} \to 0$ as $k \to \infty$.

^pf-12-17

*Uses:* [[Simple Function Approximation Theorem|§12.14]], [[§12 Measurable Functions#^thm-12-15|§12.15]], [[§12 Measurable Functions#^prop-12-10|§12.10]], [[§12 Measurable Functions#^prop-12-11|§12.11]], [[§12 Measurable Functions#^def-12-9|Def. §12.9]], [[§24 Uniform Convergence#^thm-24-1|451 §24.1]]

> [!remark]- Connections
> - Used in Step 2 of [[Lusin's Theorem|Lusin's Theorem]].

## Set-Theoretic Characterization of Convergence

The following characterization translates the $\epsilon$-$N$ definition of convergence into set-theoretic language, which is essential for proving measurability of limits and for [[Egorov's Theorem|Egorov's theorem]].

> [!theorem] Proposition §12.18: Convergence as Set Membership
> Let $f, f_1, f_2, \ldots$ be functions on $E$ with $f$ finite-valued. Then $f_k(x_0) \to f(x_0)$ as $k \to \infty$ if and only if
>
> $$
> x_0 \in \bigcap_{j=1}^{\infty} \bigcup_{\ell=1}^{\infty} \bigcap_{k=\ell}^{\infty} \left\{ x \in E : |f_k(x) - f(x)| < \frac{1}{j} \right\}.
> $$

^prop-12-18

> [!proof]+ Proof
> The statement $f_k(x_0) \to f(x_0)$ [[§7 Limits of Sequences#^def-7-2|means]]: for all $\epsilon > 0$, there exists $\ell \in \mathbb{N}$ such that for all $k \geq \ell$, $|f_k(x_0) - f(x_0)| < \epsilon$.
>
> Taking $\epsilon = \frac{1}{j}$ for $j \in \mathbb{N}$ [[Archimedean Property|captures all]] $\epsilon > 0$. Thus:
>
> $$
> \begin{aligned}
> f_k(x_0) \to f(x_0) &\Longleftrightarrow \forall j \in \mathbb{N}, \, \exists \ell \in \mathbb{N}, \, \forall k \geq \ell: \, |f_k(x_0) - f(x_0)| < \frac{1}{j} \\
> &\Longleftrightarrow x_0 \in \bigcap_{j=1}^{\infty} \bigcup_{\ell=1}^{\infty} \bigcap_{k=\ell}^{\infty} \left\{ x \in E : |f_k(x) - f(x)| < \frac{1}{j} \right\}.
> \end{aligned}
> $$

^pf-12-18

*Uses:* [[§7 Limits of Sequences#^def-7-2|451 Def. §7.2]], [[Archimedean Property|451 Archimedean Property]]

> [!definition] Definition §12.10: Set of Convergence and Divergence
> Define the **set of convergence**:
>
> $$
> C = \bigcap_{j=1}^{\infty} \bigcup_{\ell=1}^{\infty} \bigcap_{k=\ell}^{\infty} \left\{ x \in E : |f_k(x) - f(x)| < \frac{1}{j} \right\}.
> $$
>
> The **set of divergence** is $E \setminus C$. By De Morgan's laws:
>
> $$
> E \setminus C = \bigcup_{j=1}^{\infty} \bigcap_{\ell=1}^{\infty} \bigcup_{k=\ell}^{\infty} \left\{ x \in E : |f_k(x) - f(x)| \geq \frac{1}{j} \right\}.
> $$
>
> The statement “$f_k \to f$ [[§12 Measurable Functions#^def-12-8|a.e.]] on $E$” is equivalent to $m(E \setminus C) = 0$.

^def-12-10

> [!remark]- Connections
> - The inner unions $\bigcup_{k \geq \ell}\{|f_k - f| \geq 1/j\}$ are exactly the sets $E_\ell^{(j)}$ in the proof of [[Egorov's Theorem|Egorov's Theorem]].
