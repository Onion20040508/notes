---
type: section
subject: "[[Measure Theory]]"
chapter: 3
section: 11
tags: [measure-theory, math551]
---
← [[§10 Lebesgue Outer Measure]] · ↑ [[· 3 Measure Theory]] · [[§12 Borel Sets and Measure Spaces]] →

## The Problem with Outer Measure

A natural question arises: if $A_1, A_2 \subseteq \mathbb{R}^n$ with $A_1 \cap A_2 = \emptyset$, is $m^*(A_1 \cup A_2) = m^*(A_1) + m^*(A_2)$?

The answer is **no** in general. [[§10 Lebesgue Outer Measure#^def-10-4|Outer measure]] is only [[Properties of Lebesgue Outer Measure|subadditive]], not additive. To obtain additivity, we must restrict to a special class of sets called **measurable sets**.

## The Carathéodory Criterion

> [!definition] Definition §11.1: Lebesgue Measurable Set
> A set $E \subseteq \mathbb{R}^n$ is called **Lebesgue measurable** (or **L-measurable**) if for every $T \subseteq \mathbb{R}^n$, we have
>
> $$
> m^*(T) = m^*(T \cap E) + m^*(T \cap E^c).
> $$
>
> This is called the **Carathéodory criterion**.

^def-11-1

![[m551-10-1.svg]]
*The Carathéodory criterion: a test set $T$ (black outline) is cut by $E$ (blue) into $T \cap E$ (dark blue) and $T \cap E^c$ (red). $E$ is measurable when, for every such $T$, the outer measures of the two pieces add up exactly to $m^{\ast}(T)$; the inequality $\leq$ is automatic by subadditivity ([[§11 Lebesgue Measurable Sets#^rem-11-1|Remark §10.1]]).*

> [!remark] Remark
> By [[Properties of Lebesgue Outer Measure|subadditivity]], $m^*(T) \leq m^*(T \cap E) + m^*(T \cap E^c)$ always holds.
>
> Thus to show $E$ is measurable, it suffices to show that for all $T \subseteq \mathbb{R}^n$:
>
> $$
> m^*(T) \geq m^*(T \cap E) + m^*(T \cap E^c).
> $$

^rem-11-1

> [!remark] Remark: Geometric and Topological Motivation for the Carathéodory Criterion
> At first glance, the Carathéodory criterion appears purely algebraic and unmotivated: why should measurability require testing against *every* subset $T \subseteq \mathbb{R}^n$? The following perspectives reveal its geometric content.
>
> **1. The separation principle.** A measurable set $E$ should “cleanly separate” any region of space into the part inside $E$ and the part outside, with no measure lost or created at the boundary. The criterion $m^{\ast}(T) = m^{\ast}(T \cap E) + m^{\ast}(T \cap E^c)$ says precisely this: $E$ splits every test set $T$ additively. If the boundary of $E$ were “fuzzy”—trapping measure in a way that neither side can claim—one would find a test set $T$ straddling that boundary with strict inequality $m^{\ast}(T) < m^{\ast}(T \cap E) + m^{\ast}(T \cap E^c)$.
>
> **2. Analogy with topological separation.** In topology, a *[[§15 Connected Spaces#^def-15-1|separation]]* of $X$ is a decomposition $X = U \cup V$ with $U, V$ open and disjoint—the two pieces do not interfere. The Carathéodory criterion is the measure-theoretic analogue: $E$ “separates” any test set into two pieces whose outer measures do not interfere (they add exactly). Topological separation says the boundary between $U$ and $V$ is empty; measure-theoretic separation says the boundary of $E$ is negligible from the perspective of outer measure.
>
> **3. Why quantify over all $T$?** One might hope it suffices to check $m^{\ast}(\mathbb{R}^n) = m^{\ast}(E) + m^{\ast}(E^c)$, but this is trivially satisfied whenever either side is infinite. The universal quantifier over $T$ demands the splitting work *locally*—for arbitrarily small test sets zooming into the boundary of $E$. This is analogous to how closedness in topology is not a global property but a local one ([[§13 Some Topological Concepts in Metric Spaces#^prop-13-5|every convergent sequence]] near the boundary must land inside). It is also precisely this universal quantifier that forces $\mathcal{M}$ to be a [[Lebesgue Measurable Sets Form a σ-Algebra|σ-algebra automatically]].
>
> **4. Equivalent “partition wall” formulation.** The Carathéodory criterion is equivalent to: for all $A \subseteq E$ and $B \subseteq E^c$,
>
> $$
> m^*(A \cup B) = m^*(A) + m^*(B).
> $$
>
> This says that sets on opposite sides of $E$'s boundary do not interact metrically—$E$ acts as a perfect partition wall. Non-measurable sets like the [[§14 The Vitali Set and the Cantor Set#^def-14-3|Vitali set]] fail this because they have a fractal-like, interlocking structure with their complement: no matter how one attempts the separation, some measure is always trapped at the interface.

^rem-11-2

> [!remark]- Connections
> - Jordan-content counterpart, which asks inner and outer content to agree: [[§20 Multivariable Integration#^def-20-7|452 Def. §20.7]].

> [!example] Example §11.1: Sets of Measure Zero are Measurable
> If $m^*(E) = 0$, then $E$ is L-measurable.

^ex-11-1

> [!proof]+ Proof
> Let $T \subseteq \mathbb{R}^n$. Since $T \cap E \subseteq E$, by [[Properties of Lebesgue Outer Measure|monotonicity]] $m^*(T \cap E) \leq m^*(E) = 0$, so $m^*(T \cap E) = 0$.
>
> Since $T \cap E^c \subseteq T$, by monotonicity $m^*(T \cap E^c) \leq m^*(T)$.
>
> Thus $m^*(T \cap E) + m^*(T \cap E^c) = 0 + m^*(T \cap E^c) \leq m^*(T)$.
>
> Combined with the reverse inequality from subadditivity, $E$ is measurable.

^pf-ex-11-1

*Uses:* [[Properties of Lebesgue Outer Measure|§10.1]], [[§11 Lebesgue Measurable Sets#^def-11-1|Def. §11.1]], [[§11 Lebesgue Measurable Sets#^rem-11-1|Rem. §10.1]]

> [!remark]- Connections
> - Examples: finite and countable sets ([[§10 Lebesgue Outer Measure#^ex-10-2|Ex. §10.2]]) and the [[§14 The Vitali Set and the Cantor Set#^prop-14-7|Cantor set]].
> - Underlies “almost everywhere”: [[§16 Limits and Positive Parts of Measurable Functions#^def-16-2|Def. §16.2]].

> [!definition] Definition §11.2: The Collection of Measurable Sets
> We denote the collection of all L-measurable sets by $\mathcal{M}$:
>
> $$
> \mathcal{M} = \{E \subseteq \mathbb{R}^n \mid E \text{ is L-measurable}\}.
> $$

^def-11-2

## Basic Properties of Measurable Sets

> [!theorem] Theorem §11.1: Closure Properties of $\mathcal{M}$
> The collection $\mathcal{M}$ satisfies:
> 1. If $E \in \mathcal{M}$, then $E^c \in \mathcal{M}$.
> 2. If $E_1, E_2 \in \mathcal{M}$, then $E_1 \cup E_2 \in \mathcal{M}$.
> 3. If $E_1, E_2 \in \mathcal{M}$, then $E_1 \cap E_2 \in \mathcal{M}$ and $E_1 \setminus E_2 \in \mathcal{M}$.

^thm-11-1

> [!proof]+ Proof
> **(1)** The Carathéodory criterion is symmetric in $E$ and $E^c$: if $m^{\ast}(T) = m^{\ast}(T \cap E) + m^{\ast}(T \cap E^c)$ for all $T$, then the same equation holds with $E$ replaced by $E^c$.
>
> **(3)** Assuming (1) and (2): $E_1 \cap E_2 = (E_1^c \cup E_2^c)^c \in \mathcal{M}$. Also $E_1 \setminus E_2 = E_1 \cap E_2^c \in \mathcal{M}$.
>
> **(2)** Let $E_1, E_2 \in \mathcal{M}$ and $T \subseteq \mathbb{R}^n$. We may assume $m^{\ast}(T) < \infty$.
>
> We must show $m^*(T) \geq m^*(T \cap (E_1 \cup E_2)) + m^*(T \cap (E_1 \cup E_2)^c)$.
>
> Since $E_1 \in \mathcal{M}$:
>
> $$
> m^*(T \cap (E_1 \cup E_2)) = m^*((T \cap (E_1 \cup E_2)) \cap E_1) + m^*((T \cap (E_1 \cup E_2)) \cap E_1^c)
> $$
>
> $$
> = m^*(T \cap E_1) + m^*(T \cap E_2 \cap E_1^c).
> $$
>
> Since $E_2 \in \mathcal{M}$:
>
> $$
> m^*(T \cap E_1^c \cap E_2) = m^*(T \cap E_1^c) - m^*(T \cap E_1^c \cap E_2^c)
> $$
>
> (This follows from applying the Carathéodory criterion with $E_2$ to the set $T \cap E_1^c$.)
>
> Now, since $E_1 \in \mathcal{M}$:
>
> $$
> m^*(T) = m^*(T \cap E_1) + m^*(T \cap E_1^c).
> $$
>
> Combining these and noting that $(E_1 \cup E_2)^c = E_1^c \cap E_2^c$:
>
> $$
> m^*(T \cap (E_1 \cup E_2)) + m^*(T \cap (E_1 \cup E_2)^c) = m^*(T \cap E_1) + m^*(T \cap E_1^c \cap E_2) + m^*(T \cap E_1^c \cap E_2^c)
> $$
>
> $$
> = m^*(T \cap E_1) + m^*(T \cap E_1^c) = m^*(T).
> $$

^pf-11-1

*Uses:* [[§11 Lebesgue Measurable Sets#^def-11-1|Def. §11.1]], [[§11 Lebesgue Measurable Sets#^rem-11-1|Rem. §10.1]]

![[m551-10-2.svg]]
*The proof of [[§11 Lebesgue Measurable Sets#^thm-11-1|Theorem §11.1]] (2): first split $T$ by $E_1$ (blue versus the rest), then split the rest $T \cap E_1^c$ by $E_2$ (green versus red). Blue and green together form $T \cap (E_1 \cup E_2)$, red is $T \cap (E_1 \cup E_2)^c$, and both splits are additive because $E_1$ and $E_2$ are measurable.*

## Algebras and $\sigma$-Algebras

> [!definition] Definition §11.3: Algebra
> Let $X$ be a set. A collection $\mathcal{A}$ of subsets of $X$ is called an **algebra** if:
> 1. $E \in \mathcal{A} \Rightarrow E^c \in \mathcal{A}$
> 2. $E_1, E_2 \in \mathcal{A} \Rightarrow E_1 \cup E_2 \in \mathcal{A}$
>
> Consequently, $E_1 \setminus E_2 \in \mathcal{A}$ and $E_1 \cap E_2 \in \mathcal{A}$ for $E_1, E_2 \in \mathcal{A}$.

^def-11-3

> [!remark] Remark
> We avoid uncountable unions of sets because uncountable sums make no sense in general.

^rem-11-3

> [!definition] Definition §11.4: $\sigma$-Algebra
> An algebra $\mathcal{A}$ is called a **$\sigma$-algebra** if additionally:
> 3. $E_j \in \mathcal{A}$ for $j = 1, 2, \ldots \Rightarrow \bigcup_{j=1}^{\infty} E_j \in \mathcal{A}$

^def-11-4

> [!remark]- Connections
> - Compare the axioms of a topology (arbitrary unions, finite intersections, no complements): [[§1 Topological Spaces#^def-1-1|590 Def. §1.1]]; the two meet in the [[§12 Borel Sets and Measure Spaces#^def-12-2|Borel σ-algebra]].

> [!example] Example §11.2: Examples of $\sigma$-Algebras
> For any set $X$:
> - $\mathcal{P}(X) = \{A \mid A \subseteq X\}$ (the [[§4 Uncountability#^def-4-1|power set]]) is a $\sigma$-algebra.
> - $\mathcal{A} = \{\emptyset, X\}$ is a $\sigma$-algebra (the trivial $\sigma$-algebra).

^ex-11-2

## $\mathcal{M}$ is a $\sigma$-Algebra

> [!theorem] Lemma §11.2: Finite Additivity for Disjoint Measurable Sets
> Let $E_1, E_2, \ldots, E_k \in \mathcal{M}$ be pairwise disjoint. Then for any $T \subseteq \mathbb{R}^n$:
>
> $$
> m^*\left( T \cap \bigcup_{j=1}^{k} E_j \right) = \sum_{j=1}^{k} m^*(T \cap E_j).
> $$

^lem-11-2

> [!proof]+ Proof
> We proceed by induction on $k$.
>
> **Base case ($k = 1$):** Trivial.
>
> **Base case ($k = 2$):** Let $E_1, E_2 \in \mathcal{M}$ with $E_1 \cap E_2 = \emptyset$. For any $T \subseteq \mathbb{R}^n$:
>
> $$
> m^*(T \cap (E_1 \cup E_2)) = m^*((T \cap (E_1 \cup E_2)) \cap E_1) + m^*((T \cap (E_1 \cup E_2)) \cap E_1^c)
> $$
>
> $$
> = m^*(T \cap E_1) + m^*(T \cap E_2),
> $$
>
> where the last equality uses $E_1 \cap E_2 = \emptyset$.
>
> **Inductive step:** Assume the result holds for $k - 1$. Then:
>
> $$
> m^*\left( T \cap \bigcup_{j=1}^{k} E_j \right) = m^*\left( T \cap \left( \bigcup_{j=1}^{k-1} E_j \cup E_k \right) \right)
> $$
>
> $$
> = m^*\left( T \cap \bigcup_{j=1}^{k-1} E_j \right) + m^*(T \cap E_k) = \sum_{j=1}^{k-1} m^*(T \cap E_j) + m^*(T \cap E_k) = \sum_{j=1}^{k} m^*(T \cap E_j).
> $$

^pf-11-2

*Uses:* [[§11 Lebesgue Measurable Sets#^def-11-1|Def. §11.1]], [[§11 Lebesgue Measurable Sets#^thm-11-1|§11.1]]

> [!theorem] Theorem §11.3: $\mathcal{M}$ is a $\sigma$-Algebra with Countable Additivity
> The collection $\mathcal{M}$ of L-measurable sets is a $\sigma$-algebra. Moreover, if $E_j \in \mathcal{M}$ for $j = 1, 2, \ldots$ are pairwise disjoint, then
>
> $$
> m^*\left( \bigcup_{j=1}^{\infty} E_j \right) = \sum_{j=1}^{\infty} m^*(E_j).
> $$

^thm-11-3

> [!proof]+ Proof
> **Case 1: Disjoint sets.**
>
> Assume $E_j \in \mathcal{M}$ for $j = 1, 2, \ldots$ are pairwise disjoint. Let $S_k = \bigcup_{j=1}^{k} E_j$ and $S = \bigcup_{j=1}^{\infty} E_j$.
>
> By [[§11 Lebesgue Measurable Sets#^thm-11-1|Theorem §11.1 (2)]] (and induction), $E_j \in \mathcal{M} \Rightarrow S_k \in \mathcal{M}$. Thus for any $T \subseteq \mathbb{R}^n$, using [[§11 Lebesgue Measurable Sets#^lem-11-2|the lemma]] for the second equality:
>
> $$
> m^*(T) = m^*(T \cap S_k) + m^*(T \cap S_k^c) = \sum_{j=1}^{k} m^*(T \cap E_j) + m^*(T \cap S_k^c).
> $$
>
> Since $S_k \subseteq S$, we have $S^c \subseteq S_k^c$, so $m^*(T \cap S^c) \leq m^*(T \cap S_k^c)$.
>
> Thus:
>
> $$
> m^*(T) \geq \sum_{j=1}^{k} m^*(T \cap E_j) + m^*(T \cap S^c).
> $$
>
> Letting $k \to \infty$:
>
> $$
> m^*(T) \geq \sum_{j=1}^{\infty} m^*(T \cap E_j) + m^*(T \cap S^c) \geq m^*\left( T \cap \bigcup_{j=1}^{\infty} E_j \right) + m^*(T \cap S^c) = m^*(T \cap S) + m^*(T \cap S^c).
> $$
>
> This shows $S = \bigcup_{j=1}^{\infty} E_j \in \mathcal{M}$.
>
> For countable additivity, take $T = S$. Then $T \cap S = S$ and $T \cap S^c = \emptyset$, so:
>
> $$
> m^*(S) \geq \sum_{j=1}^{\infty} m^*(E_j).
> $$
>
> The reverse inequality follows from countable subadditivity. Thus $m^*(\bigcup_j E_j) = \sum_j m^*(E_j)$.
>
> **Case 2: General (not necessarily disjoint) sets.**
>
> Assume $E_j \in \mathcal{M}$ for $j = 1, 2, \ldots$. Define:
>
> $$
> F_1 = E_1, \quad F_k = E_k \setminus \bigcup_{j=1}^{k-1} E_j \text{ for } k \geq 2.
> $$
>
> Then $\{F_k\}$ is a disjoint sequence of measurable sets (using [[§11 Lebesgue Measurable Sets#^thm-11-1|closure properties]] of $\mathcal{M}$), and $\bigcup_{k=1}^{\infty} F_k = \bigcup_{j=1}^{\infty} E_j$.
>
> By Case 1, $\bigcup_{j=1}^{\infty} E_j = \bigcup_{k=1}^{\infty} F_k \in \mathcal{M}$.

^pf-11-3

*Uses:* [[§11 Lebesgue Measurable Sets#^lem-11-2|§11.2]], [[§11 Lebesgue Measurable Sets#^thm-11-1|§11.1]], [[Properties of Lebesgue Outer Measure|§10.1]], [[§11 Lebesgue Measurable Sets#^def-11-1|Def. §11.1]], [[§11 Lebesgue Measurable Sets#^rem-11-1|Rem. §10.1]], [[§11 Lebesgue Measurable Sets#^def-11-4|Def. §11.4]]

![[m551-10-3.svg]]
*Disjointification (Case 2 of [[§11 Lebesgue Measurable Sets#^thm-11-3|Theorem §11.3]]): $F_1 = E_1$ (blue), $F_2 = E_2 \setminus E_1$ (green), $F_3 = E_3 \setminus (E_1 \cup E_2)$ (orange). Each point of $\bigcup_j E_j$ lands in exactly one $F_k$ — the one for the first $E_k$ containing it — so the $F_k$ are disjoint with the same union, and Case 1 applies.*

> [!remark]- Connections
> - The same argument, for an arbitrary outer measure: [[Carathéodory's Theorem|Carathéodory's Theorem]] ([[§12 Borel Sets and Measure Spaces#^thm-12-2|§12.2]]).
> - Consequences: [[Continuity of Measure|continuity from below]] and [[§13 Approximation and Continuity of Measure#^prop-13-5|from above]].

## Lebesgue Measure

> [!definition] Definition §11.5: Lebesgue Measure
> For $E \in \mathcal{M}$, we define the **Lebesgue measure** of $E$ by
>
> $$
> m(E) = m^*(E).
> $$

^def-11-5

> [!remark] Remark
> Lebesgue measure $m$ restricted to $\mathcal{M}$ has the crucial property of **countable additivity** ([[Lebesgue Measurable Sets Form a σ-Algebra|Thm. §11.3]]):
>
> $$
> m\left( \bigcup_{j=1}^{\infty} E_j \right) = \sum_{j=1}^{\infty} m(E_j)
> $$
>
> for pairwise disjoint $E_j \in \mathcal{M}$. This is what outer measure $m^*$ lacks for general sets.

^rem-11-4

> [!remark]- Connections
> - $(\mathbb{R}^n, \mathcal{M}, m)$ is the model [[§12 Borel Sets and Measure Spaces#^def-12-7|measure space]] ([[§12 Borel Sets and Measure Spaces#^def-12-7|Def. §12.7]]).
> - MATH 452 counterpart for Jordan measurable sets: [[§20 Multivariable Integration#^thm-20-1|452 §20.1]] (additivity of Jordan measure).
