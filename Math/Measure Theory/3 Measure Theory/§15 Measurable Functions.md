---
type: section
subject: "[[Measure Theory]]"
chapter: 3
section: 15
tags: [measure-theory, math551]
---
← [[§14 The Vitali Set and the Cantor Set]] · ↑ [[· 3 Measure Theory]] · [[§16 Limits and Positive Parts of Measurable Functions]] →

## Extended Real Numbers

To handle functions that may take infinite values (such as $f(x) = 1/x$ near $0$), we extend the real numbers.

> [!definition] Definition §15.1: Extended Real Numbers
> The **extended real numbers** are
>
> $$
> \overline{\mathbb{R}} = \mathbb{R} \cup \{+\infty, -\infty\}.
> $$
>
> We may also write this as $\mathbb{R} \cup \{\pm\infty\}$.

^def-15-1

> [!remark] Note: Arithmetic Conventions
> We adopt the following conventions for arithmetic in $\overline{\mathbb{R}}$:
> - $+\infty + (+\infty) = +\infty$, $(-\infty) + (-\infty) = -\infty$
> - $(+\infty) \cdot (-\infty) = -\infty$
> - For $x \in \mathbb{R}$: $x + (+\infty) = +\infty$, $x + (-\infty) = -\infty$, $x \pm \infty = \pm\infty$
> - $0 \cdot (\pm\infty) = 0$ (important convention for integration)
> - $(+\infty) - (+\infty)$ is **undefined** (indeterminate form)

^rem-15-1

> [!remark]- Connections
> - MATH 451 treatment of $\pm\infty$: [[§5 The Symbols +∞, −∞#^rem-5-1|451 §5: Arithmetic with infinities]]; the function $1/x$: [[Reciprocal function 1∕x]].
> - The convention $0 \cdot \infty = 0$ is what makes the integral of simple functions well defined: [[§20 The Lebesgue Integral for Simple Functions#^def-20-1|Def. §20.1]].

## Definition of Measurable Functions

> [!definition] Definition §15.2: Measurable Function
> Let $E \subseteq \mathbb{R}^n$ be a [[§11 Lebesgue Measurable Sets#^def-11-1|measurable]] set and let $f: E \to \overline{\mathbb{R}}$ be an extended real-valued function defined on $E$. We say $f$ is **(Lebesgue) measurable** if for all $c \in \mathbb{R}$,
>
> $$
> \{x \in E \mid f(x) > c\} \in \mathcal{M}
> $$
>
> ($\mathcal{M}$: [[§11 Lebesgue Measurable Sets#^def-11-2|Def. §11.2]]).

^def-15-2

![[m551-12-1.svg]]
*The sets in [[§15 Measurable Functions#^def-15-2|Definition §15.2]] are horizontal slices: $\{f > c\}$ (red, on the $x$-axis) is where the graph lies strictly above the line $y = c$. For this continuous $f$ it is relatively open in $[a,b]$: hollow endpoints where $f = c$, a filled one at $b$ ([[§15 Measurable Functions#^ex-15-2|Example §15.2]]). For a general measurable $f$ it can be far wilder, but it must still be measurable.*

> [!remark] Remark: Geometric Interpretation
> For a function $f: [a, b] \to \mathbb{R}$, the set $\{x \in [a, b] \mid c_1 < f(x) < c_2\}$ represents the portion of the domain where the graph lies between the horizontal lines $y = c_1$ and $y = c_2$. Measurability ensures that such “horizontal slices” of the domain are always measurable sets.

^rem-15-2

> [!example] Example §15.1: Monotone Functions are Measurable
> Assume $f: [a, b] \to \mathbb{R}$ is monotone. Then $f$ is measurable.
>
> For any $c \in \mathbb{R}$, the set $\{x \in [a, b] \mid f(x) > c\}$ is one of the following:
> - An interval (open, closed, or half-open)
> - The empty set $\emptyset$
> - A single point
>
> In all cases, this set is measurable (intervals and singletons are [[§12 Borel Sets and Measure Spaces#^def-12-2|Borel sets]]; [[§12 Borel Sets and Measure Spaces#^cor-12-7|Cor. §12.7]]).

^ex-15-1

> [!remark]- Connections
> - Monotone functions reappear in differentiation theory: [[§28 Differentiation Theory#^thm-28-1|Monotone Functions Have Countably Many Discontinuities]], [[Lebesgue's Differentiation Theorem for Monotone Functions|Lebesgue's Differentiation Theorem]].

> [!example] Example §15.2: Continuous Functions are Measurable
> If $f: E \to \mathbb{R}$ is continuous (where $E \subseteq \mathbb{R}^n$ is measurable), then $f$ is measurable.
>
> For any $c \in \mathbb{R}$, the set $\{x \in E \mid f(x) > c\} = f^{-1}((c, \infty)) \cap E$ is the intersection of an open set (by [[§10 Continuous Functions#^def-10-1|continuity]]) with the measurable set $E$, hence measurable ([[§12 Borel Sets and Measure Spaces#^thm-12-6|Thm. §12.6]], [[Lebesgue Measurable Sets Form a σ-Algebra|Thm. §11.3]]).

^ex-15-2

> [!remark]- Connections
> - “Open preimage” is relative to $E$: an open set of the [[§5 Subspace Topology#^def-5-1|subspace topology]] on $E$ is $U \cap E$ with $U$ open in $\mathbb{R}^n$.
> - A partial converse: every measurable function is continuous off a set of small measure, [[Lusin's Theorem|Lusin's Theorem]].

> [!definition] Definition §15.3: Characteristic Function
> Let $E \subseteq \mathbb{R}^n$. The **characteristic function** (or **indicator function**) of $E$ is:
>
> $$
> \chi_E(x) = \mathbf{1}_E(x) = \begin{cases} 1 & \text{if } x \in E \\ 0 & \text{if } x \notin E \end{cases}
> $$

^def-15-3

> [!remark]- Connections
> - Same notion for a subset of any set: [[§12★ Counting Functions and Subsets#^def-12-4|250 Def. §12.4]].

> [!theorem] Proposition §15.1: Characteristic Functions of Measurable Sets
> If $E \in \mathcal{M}$, then $\chi_E$ is a measurable function.

^prop-15-1

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

^pf-15-1

*Uses:* [[§15 Measurable Functions#^def-15-2|Def. §15.2]], [[Lebesgue Measurable Sets Form a σ-Algebra|§11.3]]

> [!remark]- Connections
> - The Dirichlet function $\chi_{\mathbb{Q}}$ is measurable (as $\mathbb{Q}$ is countable, hence null) though not Riemann integrable: [[§8 Motivation꞉ The Riemann Integral#^ex-8-2|Ex. §8.2]], [[Dirichlet and Thomae functions]].

## Equivalent Characterizations of Measurability

> [!theorem] Proposition §15.2: Equivalent Conditions for Measurability
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

^prop-15-2

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

^pf-15-2

*Uses:* [[§15 Measurable Functions#^def-15-2|Def. §15.2]], [[Lebesgue Measurable Sets Form a σ-Algebra|§11.3]]

## Algebra of Measurable Functions

> [!theorem] Theorem §15.3: Arithmetic Operations Preserve Measurability
> Let $E \in \mathcal{M}$ and assume $f: E \to \mathbb{R}$, $g: E \to \mathbb{R}$ are measurable functions. Then:
> 1. $f + g: E \to \mathbb{R}$ is measurable.
> 2. For all $a \in \mathbb{R}$, $af: E \to \mathbb{R}$ is measurable.
> 3. $fg: E \to \mathbb{R}$ is measurable.

^thm-15-3

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

^pf-15-3

*Uses:* [[§15 Measurable Functions#^def-15-2|Def. §15.2]], [[§15 Measurable Functions#^prop-15-2|§15.2]], [[Lebesgue Measurable Sets Form a σ-Algebra|§11.3]], [[§3 Countability of Rationals and Unions#^cor-3-2|§3.2]], [[§4 The Completeness Axiom#^thm-4-7|451 §4.7]]

> [!proof]+ Proof of [[§15 Measurable Functions#^thm-15-3|Theorem §15.3]] (continued)
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

^pf-15-3-cont

*Uses:* [[§15 Measurable Functions#^def-15-2|Def. §15.2]], [[§15 Measurable Functions#^prop-15-2|§15.2]], [[Lebesgue Measurable Sets Form a σ-Algebra|§11.3]]

> [!remark] Remark: Logic to Set Theory
> The proof illustrates a key technique: translate logical statements (“there exists $r$ such that...”) into set-theoretic operations (countable unions).

^rem-15-3

> [!remark]- Connections
> - The continuous counterpart: [[§17 Continuous Functions#^thm-17-3|451 Theorem §17.3: Arithmetic of Continuous Functions]].
> - The same “∃ ⇒ countable union” translation drives [[§16 Limits and Positive Parts of Measurable Functions#^thm-16-1|Theorem §16.1]] and the set of convergence ([[§17 Simple Functions and Modes of Convergence#^prop-17-6|Proposition §17.6]]).

## Measurability on Subsets and Unions

> [!theorem] Proposition §15.4: Union of Domains
> Let $E_1, E_2 \in \mathcal{M}$. Assume $f: E_1 \to \overline{\mathbb{R}}$ and $f: E_2 \to \overline{\mathbb{R}}$ are measurable. Then $f: E_1 \cup E_2 \to \overline{\mathbb{R}}$ is measurable.

^prop-15-4

> [!proof]+ Proof
> For any $c \in \mathbb{R}$:
>
> $$
> \{x \in E_1 \cup E_2 \mid f(x) > c\} = \{x \in E_1 \mid f(x) > c\} \cup \{x \in E_2 \mid f(x) > c\} \in \mathcal{M}.
> $$

^pf-15-4

*Uses:* [[§15 Measurable Functions#^def-15-2|Def. §15.2]], [[Lebesgue Measurable Sets Form a σ-Algebra|§11.3]]

> [!theorem] Proposition §15.5: Restriction to Measurable Subsets
> Assume $f: E \to \overline{\mathbb{R}}$ is measurable, and $A \subseteq E$ with $A \in \mathcal{M}$. Then the restriction $f|_A: A \to \overline{\mathbb{R}}$ is measurable.

^prop-15-5

> [!proof]+ Proof
> For any $c \in \mathbb{R}$:
>
> $$
> \{x \in A \mid f(x) > c\} = A \cap \{x \in E \mid f(x) > c\} \in \mathcal{M}.
> $$

^pf-15-5

*Uses:* [[§15 Measurable Functions#^def-15-2|Def. §15.2]], [[Lebesgue Measurable Sets Form a σ-Algebra|§11.3]]

Limits, quotients, positive and negative parts and almost-everywhere properties continue in [[§16 Limits and Positive Parts of Measurable Functions]]; simple functions and modes of convergence follow in [[§17 Simple Functions and Modes of Convergence]].
