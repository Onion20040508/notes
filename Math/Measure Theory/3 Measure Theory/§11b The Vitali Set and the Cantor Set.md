---
type: section
subject: "[[Measure Theory]]"
chapter: 3
section: 11
tags: [measure-theory, math551]
---
← [[§11 Borel Sets and Measure Spaces]] · ↑ [[· 3 Measure Theory]] · [[§12 Measurable Functions]] →

## A Non-Measurable Set: The Vitali Construction

We now show that not every subset of $\mathbb{R}$ is Lebesgue measurable. The construction uses the Axiom of Choice.

> [!theorem] Lemma §11.15: Translation Invariance of Measure
> Let $E \in \mathcal{M}$ and $x_0 \in \mathbb{R}^n$. Define $x_0 + E = \{x_0 + y \mid y \in E\}$. Then $x_0 + E \in \mathcal{M}$ and $m(E) = m(x_0 + E)$.

^lem-11-15

> [!proof]+ Proof
> First, note that outer measure is [[§9 Lebesgue Outer Measure#^prop-9-3|translation invariant]]: $m^*(x_0 + A) = m^*(A)$ for any $A \subseteq \mathbb{R}^n$. This follows because $\{I_k\}$ is an L-cover of $A$ if and only if $\{x_0 + I_k\}$ is an L-cover of $x_0 + A$, and $|x_0 + I_k| = |I_k|$.
>
> Now suppose $E \in \mathcal{M}$. To show $x_0 + E \in \mathcal{M}$, we verify the Carathéodory condition. For any test set $T \subseteq \mathbb{R}^n$, observe that:
> - $T \cap (x_0 + E) = x_0 + ((T - x_0) \cap E)$, so $m^*(T \cap (x_0 + E)) = m^*((T - x_0) \cap E)$.
> - $(x_0 + E)^c = x_0 + E^c$, so $T \cap (x_0 + E)^c = x_0 + ((T - x_0) \cap E^c)$, giving $m^*(T \cap (x_0 + E)^c) = m^*((T - x_0) \cap E^c)$.
>
> Therefore:
>
> $$
> \begin{aligned}
> m^*(T \cap (x_0 + E)) + m^*(T \cap (x_0 + E)^c) &= m^*((T - x_0) \cap E) + m^*((T - x_0) \cap E^c) \\
> &= m^*(T - x_0) \quad \text{(since } E \in \mathcal{M}) \\
> &= m^*(T) \quad \text{(translation invariance of } m^*).
> \end{aligned}
> $$
>
> Thus $x_0 + E \in \mathcal{M}$, and $m(x_0 + E) = m^*(x_0 + E) = m^*(E) = m(E)$.

^pf-11-15

*Uses:* [[§9 Lebesgue Outer Measure#^prop-9-3|§9.3]], [[§10 Lebesgue Measurable Sets#^def-10-1|Def. §10.1]], [[§10 Lebesgue Measurable Sets#^def-10-5|Def. §10.5]]

> [!remark]- Connections
> - Integral version: [[§17 Invariance Properties and Fubini's Theorem#^thm-17-1|Thm. §17.1]]; for invertible linear maps instead of translations: [[§18b Differentiating the Integral#^cor-18-23|Cor. §18.23]].

> [!definition] Definition §11.10: Equivalence Relation
> For $x, y \in [0, 1]$, we say $x$ and $y$ are **equivalent**, written $x \sim y$, if $x - y \in \mathbb{Q}$.

^def-11-10

> [!remark]- Connections
> - The general notion: equivalence relation, [[§22 Partitions and Equivalence Relations#^def-22-new1|250 Def. §22.3]].

> [!theorem] Proposition §11.16: Properties of $\sim$
> The relation $\sim$ is an equivalence relation:
> - Reflexive: $x \sim x$ (since $x - x = 0 \in \mathbb{Q}$).
> - Symmetric: $x \sim y \Rightarrow y \sim x$ (since $x - y \in \mathbb{Q} \Rightarrow y - x \in \mathbb{Q}$).
> - Transitive: $x \sim y$ and $y \sim z \Rightarrow x \sim z$ (since $(x-y) + (y-z) = x - z \in \mathbb{Q}$).

^prop-11-16

> [!definition] Definition §11.11: Equivalence Classes
> For each $x \in [0,1]$, define the equivalence class:
>
> $$
> E_x = \{y \in [0, 1] \mid y \sim x\} = \{y \in [0, 1] \mid x - y \in \mathbb{Q}\}.
> $$

^def-11-11

> [!remark]- Connections
> - The general notion: equivalence class and quotient set, [[§22 Partitions and Equivalence Relations#^def-22-4|250 Def. §22.4]], [[§22 Partitions and Equivalence Relations#^def-22-new2|250 Def. §22.4]].

> [!theorem] Proposition §11.17
> For any $x, y \in [0, 1]$, either $E_x \cap E_y = \emptyset$ or $E_x = E_y$.

^prop-11-17

> [!proof]+ Proof
> Suppose $E_x \cap E_y \neq \emptyset$. Let $z \in E_x \cap E_y$. Then $z \sim x$ and $z \sim y$, so $x - z \in \mathbb{Q}$ and $y - z \in \mathbb{Q}$. Thus $x - y = (x - z) + (z - y) \in \mathbb{Q}$, so $x \sim y$. It follows that $E_x = E_y$.

^pf-11-17

*Uses:* [[§11b The Vitali Set and the Cantor Set#^def-11-10|Def. §11.10]], [[§11b The Vitali Set and the Cantor Set#^prop-11-16|§11.16]], [[§11b The Vitali Set and the Cantor Set#^def-11-11|Def. §11.11]]

> [!remark]- Connections
> - Linear-algebra analogue: the classes are translates of $\mathbb{Q}$ (a $\mathbb{Q}$-subspace of $\mathbb{R}$), and translates of a subspace are equal or disjoint, [[§11 Products and Quotients of Vector Spaces#^ladr-3-101|LADR 3.101]]; the set of classes is a [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|quotient space]] (LADR 3.99).
> - General version: classes are equal or disjoint, [[§22 Partitions and Equivalence Relations#^thm-22-3|250 Thm. §22.3]]; so the classes partition [0, 1], [[§22 Partitions and Equivalence Relations#^cor-22-4|250 Cor. §22.4]].
> - The classes are the cosets x + ℚ of the subgroup ℚ of (ℝ, +), cut down to [0, 1], and cosets partition a group: [[Cosets Partition a Group|493 Prop. §28.2]].

Let $\{E_\alpha \mid \alpha \in I\}$ be the collection of distinct equivalence classes, where $I$ is some index set. Note that $\bigcup_{\alpha \in I} E_\alpha = [0, 1]$.

> [!definition] Definition §11.12: The Vitali Set
> Using the Axiom of Choice, select exactly one element $x_\alpha \in E_\alpha$ from each equivalence class $\alpha \in I$. Define:
>
> $$
> V = \{x_\alpha \mid \alpha \in I\}.
> $$
>
> This is called a **Vitali set**.

^def-11-12

Note that $V \subseteq [0, 1]$.

> [!theorem] Proposition §11.18: Key Property of $V$
> For any $y \in [0, 1]$, there exists a unique $\alpha \in I$ such that $y \in E_\alpha$, and hence $y - x_\alpha \in \mathbb{Q} \cap [-1, 1]$.

^prop-11-18

Let $\mathbb{Q} \cap [-1, 1] = \{r_1, r_2, r_3, \ldots\}$ be an enumeration of the rationals in $[-1, 1]$ (possible since [[§3 Countability of Rationals and Unions#^cor-3-2|ℚ is countable]]).

> [!theorem] Proposition §11.19: Disjoint Translates Cover the Unit Interval
> The translates $\{r_j + V\}_{j=1}^{\infty}$ are pairwise disjoint, and:
>
> $$
> [0, 1] \subseteq \bigcup_{j=1}^{\infty} (r_j + V) \subseteq [-1, 2].
> $$

^prop-11-19

> [!proof]+ Proof
> *Pairwise disjoint:* Suppose $(r_i + V) \cap (r_j + V) \neq \emptyset$ for some $i \neq j$. Then there exist $x_\alpha, x_\beta \in V$ with $r_i + x_\alpha = r_j + x_\beta$. Thus $x_\alpha - x_\beta = r_j - r_i \in \mathbb{Q}$, so $x_\alpha \sim x_\beta$. But $V$ contains exactly one element from each equivalence class, so $x_\alpha = x_\beta$. Then $r_i = r_j$, contradicting $i \neq j$.
>
> *$[0,1] \subseteq \bigcup_j (r_j + V)$:* Let $y \in [0, 1]$. Then $y \in E_\alpha$ for some $\alpha$, and $y - x_\alpha \in \mathbb{Q} \cap [-1, 1]$. So $y - x_\alpha = r_j$ for some $j$, and $y = r_j + x_\alpha \in r_j + V$.
>
> *$\bigcup_j (r_j + V) \subseteq [-1, 2]$:* Since $V \subseteq [0, 1]$ and $r_j \in [-1, 1]$, we have $r_j + V \subseteq [-1, 2]$.

^pf-11-19

*Uses:* [[§11b The Vitali Set and the Cantor Set#^def-11-12|Def. §11.12]], [[§11b The Vitali Set and the Cantor Set#^prop-11-17|§11.17]], [[§11b The Vitali Set and the Cantor Set#^prop-11-18|§11.18]], [[§3 Countability of Rationals and Unions#^cor-3-2|§3.2]]

![[m551-11-4.svg]]
*The Vitali argument: $V$ (red) contains one point from each class of $\sim$, and its rational translates $r_j + V$ (blue; a few of the countably many, with $V = 0 + V$ itself among them) are pairwise disjoint. Together they cover $[0,1]$ (shaded) but stay inside $[-1,2]$. If they all had measure $m(V)$ we would need $1 \leq \sum_j m(V) \leq 3$, which is impossible whether $m(V) = 0$ or $m(V) > 0$. (The tick marks only stand in for $V$, which cannot actually be drawn.)*

> [!theorem] Theorem §11.20: The Vitali Set is Not Measurable
> The Vitali set $V$ is not Lebesgue measurable.

^thm-11-20

> [!proof]+ Proof
> Suppose for contradiction that $V \in \mathcal{M}$. Then by [[§11b The Vitali Set and the Cantor Set#^lem-11-15|translation invariance]], $r_j + V \in \mathcal{M}$ and $m(r_j + V) = m(V)$ for all $j$.
>
> Since the sets $\{r_j + V\}$ are pairwise disjoint and measurable, and $[0, 1] \subseteq \bigcup_j (r_j + V) \subseteq [-1, 2]$ ([[§11b The Vitali Set and the Cantor Set#^prop-11-19|Prop. §11.19]]), we have by [[Lebesgue Measurable Sets Form a σ-Algebra|countable additivity]] and [[Properties of Lebesgue Outer Measure|monotonicity]]:
>
> $$
> 1 = m([0, 1]) \leq m\left(\bigcup_{j=1}^{\infty} (r_j + V)\right) = \sum_{j=1}^{\infty} m(r_j + V) = \sum_{j=1}^{\infty} m(V) \leq m([-1, 2]) = 3.
> $$
>
> *Case 1: $m(V) = 0$.* Then $\sum_{j=1}^{\infty} m(V) = 0$, but $1 \leq 0$. Contradiction.
>
> *Case 2: $m(V) > 0$.* Then $\sum_{j=1}^{\infty} m(V) = \infty$, but $\infty \leq 3$. Contradiction.
>
> In either case we reach a contradiction, so $V \notin \mathcal{M}$.

^pf-11-20

*Uses:* [[§11b The Vitali Set and the Cantor Set#^lem-11-15|§11.15]], [[§11b The Vitali Set and the Cantor Set#^prop-11-19|§11.19]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]], [[Properties of Lebesgue Outer Measure|§9.1]], [[§9 Lebesgue Outer Measure#^prop-9-2|§9.2]]

> [!remark]- Connections
> - The “partition wall” failure described in [[§10 Lebesgue Measurable Sets#^rem-10-2|Rem. §10.2]] (item 4).

> [!remark] Remark
> The existence of non-measurable sets depends on the Axiom of Choice. In fact, it is consistent with ZF (set theory without Choice) that every subset of $\mathbb{R}$ is Lebesgue measurable.

^rem-11-6

> [!remark]- Connections
> - The axiom of choice, in the form of Zorn's lemma, also drives the existence theorems of 556 ([[Hahn–Banach Theorem|Hahn–Banach]], [[Every Subspace Has a Complement|complements]], orthonormal bases): [[Zorn's Lemma|556 Thm. §5.2]].

## The Cantor Set

If $E$ is countable, then $m^{\ast}(E) = 0$ ([[§9 Lebesgue Outer Measure#^ex-9-2|Ex. §9.2]]). A natural question: if $E \subseteq \mathbb{R}$ satisfies $m(E) = 0$, must $E$ be countable? The Cantor set shows the answer is **no**.

> [!definition] Definition §11.13: The Cantor Set
> Define a sequence of sets as follows:
> - $C_0 = [0, 1]$.
> - $C_1 = C_0 \setminus \left(\frac{1}{3}, \frac{2}{3}\right) = \left[0, \frac{1}{3}\right] \cup \left[\frac{2}{3}, 1\right]$.
> - $C_{n+1}$ is obtained from $C_n$ by removing the open middle third of each closed interval in $C_n$.
>
> In general, $C_n$ is a disjoint union of $2^n$ closed intervals, each of length $\frac{1}{3^n}$.
>
> The **Cantor set** is:
>
> $$
> C = \bigcap_{n=0}^{\infty} C_n.
> $$

^def-11-13

![[m551-11-5.svg]]
*The first steps of the Cantor construction: $C_{n+1}$ removes the open middle third (dashed red) of every interval of $C_n$, leaving $2^n$ intervals of length $3^{-n}$ with total length $(2/3)^n \to 0$. The labels under $C_1$ and $C_2$ are the first ternary digits of the points in each interval. Only $0$s and $2$s survive, which is how [[§11b The Vitali Set and the Cantor Set#^prop-11-21|Proposition §11.21]] (4) matches $C$ with binary sequences.*

> [!remark]- Connections
> - First met in MATH 451: [[§13 Some Topological Concepts in Metric Spaces#^rem-13-5|451 Rem. §13.5]].

> [!theorem] Proposition §11.21: Properties of the Cantor Set
> 1. $C$ is closed and bounded (hence [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|compact]]).
> 2. $C$ has no [[§2 Open and Closed Sets#^def-2-3|interior points]].
> 3. $m(C) = 0$.
> 4. $C$ is uncountable.

^prop-11-21

> [!proof]+ Proof
> **(1)** Each $C_n$ is closed (finite union of closed intervals) and bounded, with $C_0 \supseteq C_1 \supseteq C_2 \supseteq \cdots$. The Cantor set $C = \bigcap_n C_n$ is an [[§6 Closed Sets and Limit Points#^thm-6-1|intersection of closed sets]], hence closed. Since $C \subseteq [0, 1]$, it is bounded. Note that $C \neq \emptyset$: for example, $0 \in C_n$ for all $n$, so $0 \in C$. (Alternatively, the [[§5 Topology of ℝⁿ#^thm-5-2|Cantor's Nested Set Theorem]] guarantees $C \neq \emptyset$.)
>
> **(2)** Suppose $x_0 \in C$ is an interior point. Then there exists $\delta > 0$ such that $(x_0 - \delta, x_0 + \delta) \subseteq C$. But $C \subseteq C_n$ for all $n$, and $C_n$ is a disjoint union of closed intervals of length $\frac{1}{3^n}$. For $n$ large enough that $\frac{1}{3^n} < 2\delta$, the interval $(x_0 - \delta, x_0 + \delta)$ has length $2\delta > \frac{1}{3^n}$, so it cannot be contained in any single component of $C_n$. Since the components are disjoint, $(x_0 - \delta, x_0 + \delta) \not\subseteq C_n$, contradicting $(x_0 - \delta, x_0 + \delta) \subseteq C \subseteq C_n$.
>
> **(3)** Since $C$ is closed, it is a [[§11 Borel Sets and Measure Spaces#^ex-11-1|Borel set]], hence [[§11 Borel Sets and Measure Spaces#^cor-11-7|measurable]]. Since $C_n$ consists of $2^n$ disjoint closed intervals each of length $\frac{1}{3^n}$:
>
> $$
> m(C_n) = 2^n \cdot \frac{1}{3^n} = \left(\frac{2}{3}\right)^n \to 0 \text{ as } n \to \infty.
> $$
>
> Since $C \subseteq C_n$ for all $n$, we have $m(C) \leq m(C_n) = \left(\frac{2}{3}\right)^n$ for all $n$. Thus $m(C) = 0$.
>
> **(4)** Every $x \in [0, 1]$ has a ternary expansion $x = \sum_{j=1}^{\infty} \frac{a_j}{3^j}$ where $a_j \in \{0, 1, 2\}$.
>
> *Claim:* $x \in C$ if and only if $x$ has a ternary expansion using only digits $0$ and $2$.
>
> To see this, we prove by induction that $x \in C_n$ iff $x$ has a ternary expansion whose first $n$ digits are each $0$ or $2$.
>
> *Base case ($n=1$):* The set $C_1 = [0, \frac{1}{3}] \cup [\frac{2}{3}, 1]$. If $x \in [0, \frac{1}{3}]$, then $x = \frac{0}{3} + \frac{x'}{3}$ for some $x' \in [0,1]$, so the first ternary digit is $0$. If $x \in [\frac{2}{3}, 1]$, then $x = \frac{2}{3} + \frac{x'}{3}$ for some $x' \in [0,1]$, so the first digit is $2$. Conversely, if the first digit is $0$, then $x \leq \frac{1}{3}$; if it's $2$, then $x \geq \frac{2}{3}$.
>
> *Inductive step:* Assume the claim holds for $C_n$. Each component interval $I$ of $C_n$ has length $\frac{1}{3^n}$, and $C_{n+1} \cap I$ consists of the left and right thirds of $I$. Points in the left third have $(n+1)$-st digit $0$; points in the right third have $(n+1)$-st digit $2$; points of the removed open middle third have $(n+1)$-st digit $1$ in every expansion. (Only the endpoints of the thirds, such as $\frac{1}{9} = 0.01_3 = 0.00\overline{2}_3$, have two expansions; for these we choose the expansion without the digit $1$, which ends in $\overline{2}$ for a right endpoint of a left third and in $\overline{0}$ for a left endpoint of a right third.) Combined with the inductive hypothesis, $x \in C_{n+1}$ iff the first $n+1$ digits are all $0$ or $2$.
>
> Thus $x \in C = \bigcap_n C_n$ iff all ternary digits are $0$ or $2$.
>
> Now define $f: C \to [0, 1]$ by: if $x = \sum_{j=1}^{\infty} \frac{a_j}{3^j}$ with $a_j \in \{0, 2\}$, let $f(x) = \sum_{j=1}^{\infty} \frac{a_j/2}{2^j}$.
>
> (For points with two ternary representations, such as $\frac{1}{3} = 0.1_3 = 0.0\overline{2}_3$, we use the expansion with only $0$s and $2$s.)
>
> This replaces each digit $a_j \in \{0, 2\}$ by $a_j/2 \in \{0, 1\}$ and interprets the result as a binary expansion. Every $y \in [0, 1]$ has a binary expansion $y = \sum_{j=1}^{\infty} \frac{b_j}{2^j}$ with $b_j \in \{0, 1\}$, and setting $a_j = 2b_j$ gives $x \in C$ with $f(x) = y$. Thus $f$ is [[§1 Countability and Set Theory#^def-1-4|surjective]].
>
> Since $f: C \to [0, 1]$ is surjective and $[0, 1]$ is [[§4 Uncountability#^ex-4-2|uncountable]], $C$ must be uncountable.

^pf-11-21

*Uses:* [[§6 Closed Sets and Limit Points#^thm-6-1|590 §6.1]], [[§5 Topology of ℝⁿ#^thm-5-2|§5.2]], [[§11 Borel Sets and Measure Spaces#^ex-11-1|Ex. §11.1]], [[§11 Borel Sets and Measure Spaces#^cor-11-7|§11.7]], [[§9 Lebesgue Outer Measure#^prop-9-2|§9.2]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]], [[Properties of Lebesgue Outer Measure|§9.1]], [[§4 Uncountability#^ex-4-2|Ex. §4.2]], [[§16 Decimal Expansions of Real Numbers (Not Covered)|451 §16]]

> [!remark]- Connections
> - The digit map $f$ is the Cantor function restricted to $C$: [[§18c Absolute Continuity#^ex-18-4|Ex. §18.4]].

> [!remark] Remark
> The Cantor set demonstrates that:
> - Measure zero does not imply countable.
> - A closed set can have empty interior yet be uncountable.
> - The Cantor set has the same cardinality as $\mathbb{R}$ (namely $\mathfrak{c} = 2^{\aleph_0}$), yet has measure zero.

^rem-11-7

> [!remark]- Connections
> - Cardinality $2^{\aleph_0}$: [[§4 Uncountability#^ex-4-1|binary sequences]] ([[§4 Uncountability#^ex-4-1|Ex. §4.1]]); comparing cardinalities: [[Cantor–Bernstein Theorem|Cantor–Bernstein]] ([[§2 The Cantor–Bernstein Theorem#^thm-2-1|§2.1]]).
