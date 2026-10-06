---
type: section
subject: "[[Measure Theory]]"
chapter: 3
section: 13
tags: [measure-theory, math551]
---
← [[§12 Borel Sets and Measure Spaces]] · ↑ [[· 3 Measure Theory]] · [[§14 The Vitali Set and the Cantor Set]] →

Every Lebesgue measurable set is very close to a Borel set: it differs from a $G_\delta$ set or an $F_\sigma$ set by a set of measure zero. This section proves these approximation theorems and the continuity of measure along monotone sequences of sets.

## $G_\delta$ and $F_\sigma$ Sets

> [!definition] Definition §13.1: $G_\delta$ Sets
> - A **$G_\delta$ set** is a countable intersection of open sets: $G = \bigcap_{j=1}^{\infty} G_j$ where each $G_j$ is open.

^def-13-1

> [!definition] Definition §13.2: $F_\sigma$ Sets
> - An **$F_\sigma$ set** is a countable union of closed sets: $F = \bigcup_{j=1}^{\infty} F_j$ where each $F_j$ is closed.
>
> Both $G_\delta$ and $F_\sigma$ sets are Borel sets.

^def-13-2

## Approximation of Measurable Sets

> [!theorem] Theorem §13.1: Approximation by Open and $G_\delta$ Sets
> Let $E \in \mathcal{M}$. Then:
> 1. For all $\epsilon > 0$, there exists an open set $G \supseteq E$ such that $m(G \setminus E) < \epsilon$.
> 2. There exists a $G_\delta$ set $H$ with $H \supseteq E$ and $m(H \setminus E) = 0$.
>
>    That is, $E = H \setminus Z$ where $H$ is a $G_\delta$ set and $m(Z) = 0$.

^thm-13-1

> [!proof]+ Proof
> **(1)** *Case: $m(E) < \infty$.*
>
> For any $\epsilon > 0$, there exists an L-covering $\{I_k\}$ of $E$ by open rectangles such that
>
> $$
> m^*(E) + \frac{\epsilon}{2} \geq \sum_k |I_k|.
> $$
>
> Let $G = \bigcup_k I_k$. Then $G$ is open (union of open sets), $G \supseteq E$, and
>
> $$
> m^*(G) = m(G) \leq \sum_k m^*(I_k) = \sum_k |I_k| \leq m(E) + \frac{\epsilon}{2}.
> $$
>
> Thus $m(G \setminus E) = m(G) - m(E) \leq \frac{\epsilon}{2} < \epsilon$.
>
> *Case: $m(E) = \infty$.*
>
> Let $E_k = E \cap B(0, k)$ where $B(0, k)$ is the [[§5 Topology of ℝⁿ#^def-5-1|open ball]] of radius $k$ centered at the origin.
>
> Then $m(E_k) < \infty$ for each $k$. By the finite case, there exists an open set $G_k \supseteq E_k$ with $m(G_k \setminus E_k) < \frac{\epsilon}{2^k}$.
>
> Let $G = \bigcup_k G_k$. Then $G$ is open, $G \supseteq \bigcup_k E_k = E$, and
>
> $$
> G \setminus E \subseteq \bigcup_k (G_k \setminus E_k),
> $$
>
> so $m(G \setminus E) \leq \sum_k m(G_k \setminus E_k) < \sum_k \frac{\epsilon}{2^k} = \epsilon$.
>
> **(2)** By (1), for each $k \in \mathbb{N}$, there exists an open set $O_k \supseteq E$ with $m(O_k \setminus E) < \frac{1}{k}$.
>
> Let $H = \bigcap_{k=1}^{\infty} O_k$. Then $H$ is a $G_\delta$ set, $H \supseteq E$, and
>
> $$
> H \setminus E \subseteq O_k \setminus E \text{ for all } k,
> $$
>
> so $m(H \setminus E) \leq m(O_k \setminus E) < \frac{1}{k}$ for all $k$.
>
> Thus $m(H \setminus E) = 0$.

^pf-13-1

*Uses:* [[§10 Lebesgue Outer Measure#^rem-10-1|Rem. §9.1]], [[§12 Borel Sets and Measure Spaces#^thm-12-6|§12.6]], [[Properties of Lebesgue Outer Measure|§10.1]], [[§10 Lebesgue Outer Measure#^prop-10-2|§10.2]], [[Lebesgue Measurable Sets Form a σ-Algebra|§11.3]], [[§5 Topology of ℝⁿ#^def-5-1|Def. §5.1]], [[§13 Approximation and Continuity of Measure#^def-13-1|Def. §13.1]]

> [!theorem] Proposition §13.2: Outer Approximation of Arbitrary Sets
> Let $A \subseteq \mathbb{R}^n$. Then there exists a $G_\delta$ set $H$ with $H \supseteq A$ and $m^*(A) = m(H)$.

^prop-13-2

> [!proof]+ Proof
> If $m^*(A) = \infty$, take $H = \mathbb{R}^n$ (open, hence $G_\delta$). Otherwise $m^*(A) < \infty$, and the same proof as part (2) of [[Outer Regularity of Lebesgue Measure|the previous theorem]] works: for each $k$, choose an L-cover $\{I_j^{(k)}\}$ of $A$ with $\sum_j |I_j^{(k)}| < m^*(A) + \frac{1}{k}$. Let $G_k = \bigcup_j I_j^{(k)}$, which is open and satisfies $G_k \supseteq A$ and $m(G_k) \leq m^*(A) + \frac{1}{k}$.
>
> Let $H = \bigcap_k G_k$. Then $H$ is a $G_\delta$ set, $H \supseteq A$, and $m(H) \leq m(G_k) < m^*(A) + \frac{1}{k}$ for all $k$. Thus $m(H) \leq m^*(A)$. By monotonicity, $m^*(A) \leq m^*(H) = m(H)$. Therefore $m^*(A) = m(H)$.

^pf-13-2

*Uses:* [[Outer Regularity of Lebesgue Measure|§13.1]], [[§10 Lebesgue Outer Measure#^rem-10-1|Rem. §9.1]], [[Properties of Lebesgue Outer Measure|§10.1]], [[§10 Lebesgue Outer Measure#^prop-10-2|§10.2]], [[§12 Borel Sets and Measure Spaces#^cor-12-7|§12.7]]

> [!theorem] Theorem §13.3: Approximation by Closed and $F_\sigma$ Sets
> Let $E \in \mathcal{M}$. Then:
> 1. For all $\epsilon > 0$, there exists a closed set $F \subseteq E$ such that $m(E \setminus F) < \epsilon$.
> 2. There exists an $F_\sigma$ set $K$ with $K \subseteq E$ and $m(E \setminus K) = 0$.
>
>    That is, $E = K \cup Z$ where $K$ is an $F_\sigma$ set and $m(Z) = 0$.

^thm-13-3

![[m551-11-2.svg]]
*Regularity of Lebesgue measure: a measurable $E$ (black outline) is squeezed between a closed $F \subseteq E$ (blue) and an open $G \supseteq E$ (dashed red), with both shells $E \setminus F$ (orange) and $G \setminus E$ (red) of measure $< \epsilon$ ([[§13 Approximation and Continuity of Measure#^thm-13-1|Theorems §13.1]] and [[§13 Approximation and Continuity of Measure#^thm-13-3|§13.3]], part 1). The inner half comes from the outer one by complements: the proof takes an open set containing $E^c$ and lets $F$ be its complement.*

> [!proof]+ Proof
> **(1)** Since $E \in \mathcal{M}$, we have $E^c \in \mathcal{M}$. By the outer approximation theorem ([[Outer Regularity of Lebesgue Measure|Thm. §13.1]] (1)), there exists an open set $G \supseteq E^c$ with $m(G \setminus E^c) < \epsilon$.
>
> Let $F = G^c$. Then $F$ is closed (complement of open), and $G \supseteq E^c$ implies $G^c \subseteq E$, so $F \subseteq E$.
>
> Now $G \setminus E^c = G \cap E = E \cap (F^c) = E \setminus F$, so:
>
> $$
> m(E \setminus F) = m(G \setminus E^c) < \epsilon.
> $$
>
> **(2)** By (1), for each $j \in \mathbb{N}$, there exists a closed set $F_j \subseteq E$ with $m(E \setminus F_j) < \frac{1}{j}$.
>
> Let $K = \bigcup_{j=1}^{\infty} F_j$. Then $K$ is an $F_\sigma$ set, $K \subseteq E$, and for each $j$:
>
> $$
> E \setminus K \subseteq E \setminus F_j,
> $$
>
> so $m(E \setminus K) \leq m(E \setminus F_j) < \frac{1}{j}$ for all $j$. Thus $m(E \setminus K) = 0$.

^pf-13-3

*Uses:* [[§11 Lebesgue Measurable Sets#^thm-11-1|§11.1]], [[Outer Regularity of Lebesgue Measure|§13.1]], [[§5 Topology of ℝⁿ#^def-5-3|Def. §5.3]], [[Properties of Lebesgue Outer Measure|§10.1]], [[§13 Approximation and Continuity of Measure#^def-13-2|Def. §13.2]]

> [!remark]- Connections
> - Inner approximation by closed sets drives [[Lusin's Theorem|Lusin's Theorem]] ([[§18 Egorov's and Lusin's Theorems#^thm-18-3|§18.3]]).

## Continuity of Measure

> [!theorem] Proposition §13.4: Continuity of Measure from Below
> Let $E_1 \subseteq E_2 \subseteq \cdots$ be measurable sets. Then
>
> $$
> m\left( \bigcup_{n=1}^{\infty} E_n \right) = \lim_{n \to \infty} m(E_n).
> $$

^prop-13-4

> [!proof]+ Proof
> Define the increments:
>
> $$
> F_1 = E_1, \qquad F_n = E_n \setminus E_{n-1} \text{ for } n \geq 2.
> $$
>
> These are pairwise disjoint and measurable, with $\bigcup_{n=1}^{\infty} F_n = \bigcup_{n=1}^{\infty} E_n$ and $\bigcup_{n=1}^{N} F_n = E_N$ for each $N$. By [[Lebesgue Measurable Sets Form a σ-Algebra|countable additivity]]:
>
> $$
> m\left( \bigcup_{n=1}^{\infty} E_n \right) = m\left( \bigcup_{n=1}^{\infty} F_n \right) = \sum_{n=1}^{\infty} m(F_n) = \lim_{N \to \infty} \sum_{n=1}^{N} m(F_n).
> $$
>
> By [[§11 Lebesgue Measurable Sets#^lem-11-2|finite additivity]] (since $F_1, \ldots, F_N$ are pairwise disjoint and measurable):
>
> $$
> \sum_{n=1}^{N} m(F_n) = m\left( \bigcup_{n=1}^{N} F_n \right) = m(E_N).
> $$
>
> Therefore $m\bigl( \bigcup_{n=1}^{\infty} E_n \bigr) = \lim_{N \to \infty} m(E_N)$.

^pf-13-4

*Uses:* [[§11 Lebesgue Measurable Sets#^thm-11-1|§11.1]], [[Lebesgue Measurable Sets Form a σ-Algebra|§11.3]], [[§11 Lebesgue Measurable Sets#^lem-11-2|§11.2]]

> [!remark]- Connections
> - Integral analogues: [[§20 The Lebesgue Integral for Simple Functions#^lem-20-6|Lemma §20.6]] (integral over increasing sets) and the [[Monotone Convergence Theorem (Lebesgue)|Monotone Convergence Theorem]] ([[§20 The Lebesgue Integral for Simple Functions#^thm-20-7|§20.7]]).

> [!theorem] Proposition §13.5: Continuity of Measure from Above
> Let $E_1 \supseteq E_2 \supseteq \cdots$ be measurable sets with $m(E_1) < \infty$. Then
>
> $$
> m\left( \bigcap_{n=1}^{\infty} E_n \right) = \lim_{n \to \infty} m(E_n).
> $$

^prop-13-5

> [!proof]+ Proof
> Define $F_n = E_1 \setminus E_n$. Then $F_1 \subseteq F_2 \subseteq \cdots$ are measurable, and $\bigcup_{n=1}^{\infty} F_n = E_1 \setminus \bigcap_{n=1}^{\infty} E_n$. By [[Continuity of Measure|continuity from below]]:
>
> $$
> m\left( E_1 \setminus \bigcap_{n=1}^{\infty} E_n \right) = \lim_{n \to \infty} m(F_n) = \lim_{n \to \infty} m(E_1 \setminus E_n).
> $$
>
> Since $\bigcap_{n=1}^{\infty} E_n \subseteq E_n \subseteq E_1$ and $m(E_1) < \infty$, we can write $m(E_1 \setminus E_n) = m(E_1) - m(E_n)$ and $m\bigl(E_1 \setminus \bigcap_n E_n\bigr) = m(E_1) - m\bigl(\bigcap_n E_n\bigr)$. Substituting:
>
> $$
> m(E_1) - m\left( \bigcap_{n=1}^{\infty} E_n \right) = \lim_{n \to \infty} \bigl[ m(E_1) - m(E_n) \bigr] = m(E_1) - \lim_{n \to \infty} m(E_n).
> $$
>
> Since $m(E_1) < \infty$, we can cancel it from both sides to obtain $m\bigl( \bigcap_{n=1}^{\infty} E_n \bigr) = \lim_{n \to \infty} m(E_n)$.

^pf-13-5

*Uses:* [[Continuity of Measure|§13.4]], [[§11 Lebesgue Measurable Sets#^thm-11-1|§11.1]], [[Lebesgue Measurable Sets Form a σ-Algebra|§11.3]]

> [!remark]- Connections
> - Used in [[Egorov's Theorem|Egorov's Theorem]] ([[§18 Egorov's and Lusin's Theorems#^thm-18-1|§18.1]]); integral analogue: [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-7|decreasing MCT]] ([[§21 Consequences of the Monotone Convergence Theorem#^thm-21-7|§21.7]]).

> [!remark] Remark
> The hypothesis $m(E_1) < \infty$ in continuity from above is essential. For example, take $E_n = [n, \infty)$. Then $E_1 \supseteq E_2 \supseteq \cdots$, $m(E_n) = \infty$ for all $n$, but $\bigcap_n E_n = \emptyset$, so $m(\bigcap_n E_n) = 0 \neq \infty = \lim_{n \to \infty} m(E_n)$.

^rem-13-5

> [!remark]- Connections
> - Same obstruction for integrals: [[§21 Consequences of the Monotone Convergence Theorem#^rem-21-6|Rem. §14.6]].

## Symmetric Difference and Approximation by Finite Unions of Rectangles

> [!definition] Definition §13.3: Symmetric Difference
> For sets $E, F \subseteq \mathbb{R}^n$, the **symmetric difference** is
>
> $$
> E \triangle F = (E \setminus F) \cup (F \setminus E).
> $$
>
> Equivalently, $E \triangle F$ consists of all points that belong to exactly one of $E$ or $F$.

^def-13-3

> [!remark] Remark: Visualizing Symmetric Difference
> The symmetric difference $E \triangle F$ can be visualized as the “non-overlapping” parts of $E$ and $F$. Note that $m(E \triangle F) = 0$ if and only if $E$ and $F$ agree up to a set of measure zero.

^rem-13-3

> [!theorem] Theorem §13.6: Approximation by Bounded Closed Sets and Finite Unions of Rectangles
> Let $E \in \mathcal{M}$ with $m(E) < \infty$. Then:
> 1. For all $\epsilon > 0$, there exists a **bounded** closed set $K \subseteq E$ such that $m(E \setminus K) < \epsilon$.
> 2. For all $\epsilon > 0$, there exists a set $G$ which is a **finite union of rectangles** such that $m(E \triangle G) < \epsilon$.

^thm-13-6

![[m551-11-3.svg]]
*[[§13 Approximation and Continuity of Measure#^thm-13-6|Theorem §13.6]] (2): a set $E$ of finite measure (blue) and a finite union $G$ of rectangles (black outline). The symmetric difference $E \triangle G$ (red) — the part of $E$ that $G$ misses plus the part of $G$ outside $E$ — can be made to have measure $< \epsilon$. In the proof, $G$ comes from a finite subcover of a compact $K \subseteq E$.*

> [!proof]+ Proof
> **(1)** Since $E$ is measurable, $E^c$ is also measurable. By the approximation theorem (closed sets from below, [[Inner Regularity of Lebesgue Measure|Thm. §13.3]]), there exists a closed set $K \subseteq E$ such that $m(E \setminus K) < \epsilon/2$.
>
> We now ensure boundedness. Define $K_k = K \cap [-k/2, k/2]^n$, which is closed ([[§7 Closed Sets and Limit Points#^thm-7-1|intersection of two closed sets]]) and bounded (subset of $[-k/2, k/2]^n$). Since $K_k \subseteq K \subseteq E$, we have:
>
> $$
> E \setminus K_k = (E \setminus K) \cup (E \setminus [-k/2, k/2]^n).
> $$
>
> By subadditivity:
>
> $$
> m(E \setminus K_k) \leq m(E \setminus K) + m(E \setminus [-k/2, k/2]^n).
> $$
>
> Define $E_k = E \cap ([-k/2, k/2]^n)^c = E \setminus [-k/2, k/2]^n$. Since $([-(k+1)/2, (k+1)/2]^n)^c \subseteq ([-k/2, k/2]^n)^c$, the sequence $E_k$ is decreasing. Since $m(E_1) \leq m(E) < \infty$, by [[§13 Approximation and Continuity of Measure#^prop-13-5|continuity of measure from above]]:
>
> $$
> \lim_{k \to \infty} m(E_k) = m\left(\bigcap_{k=1}^{\infty} E_k\right) = m(E \setminus \mathbb{R}^n) = m(\emptyset) = 0.
> $$
>
> Thus there exists $k_0$ such that $m(E_{k_0}) < \epsilon/2$. Therefore:
>
> $$
> m(E \setminus K_{k_0}) \leq m(E \setminus K) + m(E_{k_0}) < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon.
> $$
>
> Hence $K_{k_0}$ is a bounded closed subset of $E$ with $m(E \setminus K_{k_0}) < \epsilon$.
>
> **(2)** By part (1), there exists a bounded closed set $K \subseteq E$ with $m(E \setminus K) < \epsilon/2$.
>
> Since $m(K) \leq m(E) < \infty$, by [[§10 Lebesgue Outer Measure#^def-10-4|definition of outer measure]] there exists an open L-cover $\{I_k\}_{k=1}^{\infty}$ of $K$ (where each $I_k$ is a rectangle in $\mathbb{R}^n$) such that $\sum_{k=1}^{\infty} |I_k| < m(K) + \epsilon/2$.
>
> Since $K$ is bounded and closed, it is compact by [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|Heine–Borel]]. The open cover $\{I_k\}$ has a finite subcover $\{I_k\}_{k=1}^{j}$. Define $G = \bigcup_{k=1}^{j} I_k$.
>
> Then $K \subseteq G$ and:
>
> $$
> m(G) \leq \sum_{k=1}^{j} m(I_k) \leq \sum_{k=1}^{\infty} |I_k| < m(K) + \frac{\epsilon}{2}.
> $$
>
> Since $K \subseteq G$, we have $m(G \setminus K) = m(G) - m(K) < \epsilon/2$.
>
> Since $K \subseteq G$, we have $m(E \setminus G) \leq m(E \setminus K) < \epsilon/2$.
>
> Since $K \subseteq G$, we have $m(G \setminus E) \leq m(G \setminus K) < \epsilon/2$.
>
> Since $E \setminus G$ and $G \setminus E$ are disjoint:
>
> $$
> m(E \triangle G) = m(E \setminus G) + m(G \setminus E) < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon.
> $$

^pf-13-6

*Uses:* [[Inner Regularity of Lebesgue Measure|§13.3]], [[§7 Closed Sets and Limit Points#^thm-7-1|590 §7.1]], [[Properties of Lebesgue Outer Measure|§10.1]], [[§13 Approximation and Continuity of Measure#^prop-13-5|§13.5]], [[§10 Lebesgue Outer Measure#^rem-10-1|Rem. §9.1]], [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|§6.4]], [[§10 Lebesgue Outer Measure#^prop-10-2|§10.2]], [[§12 Borel Sets and Measure Spaces#^prop-12-5|§12.5]], [[Lebesgue Measurable Sets Form a σ-Algebra|§11.3]], [[§13 Approximation and Continuity of Measure#^def-13-3|Def. §13.3]]

> [!remark]- Connections
> - Function version: [[§24 The L¹ Space and Density Theorems#^thm-24-6|step functions are dense in L¹]] ([[§24 The L¹ Space and Density Theorems#^thm-24-6|Thm. §24.6]]).
> - MATH 452 counterpart: Jordan content is defined by approximating with finite unions of squares, [[§20 Multivariable Integration#^def-20-5|452 Def. §20.5]], [[§20 Multivariable Integration#^def-20-6|452 Def. §20.6]].

> [!remark] Remark
> The symmetric difference characterization is useful because it says that *every measurable set of finite measure can be approximated arbitrarily well by finite unions of rectangles*—the simplest possible sets. This is a powerful structural result showing that the abstract $\sigma$-algebra $\mathcal{M}$ is, in a metric sense, generated by elementary sets.

^rem-13-4

## Continuity of Outer Measure from Below

The following result, not covered in lecture, extends the classical [[Continuity of Measure|continuity from below]] to outer measure applied to possibly non-measurable sets, provided we exhaust by measurable sets.

> [!theorem] Theorem §13.7: Continuity of Outer Measure from Below via Measurable Exhaustion
> Let $M_1 \subseteq M_2 \subseteq \cdots$ be Lebesgue measurable with $m(M_n) < \infty$ and $\bigcup_n M_n \supseteq E$. Then
>
> $$
> \lim_{n \to \infty} m^*(E \cap M_n) = m^*(E),
> $$
>
> whether $m^*(E)$ is finite or infinite.

^thm-13-7

> [!proof]+ Proof
> Since $E \cap M_n \subseteq E$, [[Properties of Lebesgue Outer Measure|monotonicity]] gives $m^*(E \cap M_n) \leq m^*(E)$ for all $n$, so $\lim_{n \to \infty} m^*(E \cap M_n) \leq m^*(E)$. It remains to show $m^*(E) \leq \lim_{n \to \infty} m^*(E \cap M_n)$.
>
> **Case 1: $m^{\ast}(E) < \infty$.**
>
> It suffices to show that $\lim_{n \to \infty} m^*(E \setminus M_n) = 0$. Fix $\epsilon > 0$ and choose an L-cover $\{I_k\}$ of $E$ with $\sum_k |I_k| < m^*(E) + \epsilon$. Since $E \setminus M_n \subseteq \bigcup_k (I_k \setminus M_n)$, by subadditivity:
>
> $$
> m^*(E \setminus M_n) \leq \sum_k m^*(I_k \setminus M_n).
> $$
>
> Since $M_n$ is measurable, the [[§11 Lebesgue Measurable Sets#^def-11-1|Carathéodory condition]] applied to each $I_k$ gives:
>
> $$
> |I_k| = m^*(I_k \cap M_n) + m^*(I_k \setminus M_n),
> $$
>
> so $m^*(I_k \setminus M_n) = |I_k| - m(I_k \cap M_n)$. Define $a_k^{(n)} = |I_k| - m(I_k \cap M_n)$. Then:
>
> $$
> m^*(E \setminus M_n) \leq \sum_{k=1}^{\infty} a_k^{(n)}.
> $$
>
> For each fixed $k$, the sets $I_k \cap M_n$ are measurable, nested ($I_k \cap M_n \subseteq I_k \cap M_{n+1}$), and satisfy $\bigcup_{n=1}^{\infty} (I_k \cap M_n) = I_k \cap \bigl(\bigcup_j M_j\bigr)$. Since $m(I_k \cap M_1) \leq |I_k| < \infty$, [[Continuity of Measure|continuity of measure from below]] gives
>
> $$
> \lim_{n \to \infty} m(I_k \cap M_n) = m\left(I_k \cap \bigcup_j M_j\right).
> $$
>
> Write $a_k = |I_k| - m\bigl(I_k \cap \bigcup_j M_j\bigr)$, so that $\lim_{n \to \infty} a_k^{(n)} = a_k$ for each fixed $k$.
>
> We now show $\lim_{n \to \infty} \sum_{k=1}^{\infty} a_k^{(n)} = \sum_{k=1}^{\infty} a_k$. Note that $0 \leq a_k^{(n)} \leq |I_k|$ for all $k, n$, and $\sum_k |I_k| < \infty$. Given $\delta > 0$, choose $K$ large enough so that $\sum_{k=K+1}^{\infty} |I_k| < \delta/3$. Then for every $n$:
>
> $$
> \sum_{k=K+1}^{\infty} a_k^{(n)} \leq \sum_{k=K+1}^{\infty} |I_k| < \frac{\delta}{3}, \qquad \text{and likewise} \qquad \sum_{k=K+1}^{\infty} a_k < \frac{\delta}{3}.
> $$
>
> Since $\lim_{n \to \infty} a_k^{(n)} = a_k$ for each $k = 1, \ldots, K$, there exists $N$ such that for all $n \geq N$:
>
> $$
> \left| \sum_{k=1}^{K} a_k^{(n)} - \sum_{k=1}^{K} a_k \right| < \frac{\delta}{3}.
> $$
>
> Combining:
>
> $$
> \left| \sum_{k=1}^{\infty} a_k^{(n)} - \sum_{k=1}^{\infty} a_k \right| \leq \left| \sum_{k=1}^{K} a_k^{(n)} - \sum_{k=1}^{K} a_k \right| + \sum_{k=K+1}^{\infty} a_k^{(n)} + \sum_{k=K+1}^{\infty} a_k < \frac{\delta}{3} + \frac{\delta}{3} + \frac{\delta}{3} = \delta.
> $$
>
> Since $\delta > 0$ was arbitrary, $\lim_{n \to \infty} \sum_{k=1}^{\infty} a_k^{(n)} = \sum_{k=1}^{\infty} a_k$.
>
> To bound $\sum_{k=1}^{\infty} a_k$, note that $E \subseteq \bigcup_j M_j$, so:
>
> $$
> m^*(E) \leq m^*\left(\bigcup_k I_k \cap \bigcup_j M_j\right) \leq \sum_k m\left(I_k \cap \bigcup_j M_j\right),
> $$
>
> and therefore:
>
> $$
> \sum_{k=1}^{\infty} a_k = \sum_k |I_k| - \sum_k m\left(I_k \cap \bigcup_j M_j\right) \leq \sum_k |I_k| - m^*(E) < \epsilon.
> $$
>
> Since $\lim_{n \to \infty} \sum_k a_k^{(n)} = \sum_k a_k < \epsilon$, for $n$ sufficiently large we have $m^*(E \setminus M_n) \leq \sum_k a_k^{(n)} < 2\epsilon$. By subadditivity:
>
> $$
> m^*(E) \leq m^*(E \cap M_n) + m^*(E \setminus M_n) < m^*(E \cap M_n) + 2\epsilon.
> $$
>
> Since $\epsilon > 0$ is arbitrary, $\lim_{n \to \infty} m^*(E \cap M_n) = m^*(E)$.
>
> **Case 2: $m^{\ast}(E) = \infty$.**
>
> Suppose for contradiction that $\sup_n m^*(E \cap M_n) = L < \infty$. Define the increments:
>
> $$
> D_1 = E \cap M_1, \qquad D_n = (E \cap M_n) \setminus M_{n-1} \text{ for } n \geq 2.
> $$
>
> These are pairwise disjoint with $\bigcup_n D_n = E$. Since $M_{n-1}$ is measurable and $M_{n-1} \subseteq M_n$, the Carathéodory condition applied to the test set $E \cap M_n$ gives:
>
> $$
> m^*(E \cap M_n) = m^*((E \cap M_n) \cap M_{n-1}) + m^*((E \cap M_n) \setminus M_{n-1}) = m^*(E \cap M_{n-1}) + m^*(D_n).
> $$
>
> Telescoping:
>
> $$
> \sum_{n=1}^{N} m^*(D_n) = m^*(E \cap M_N) \leq L,
> $$
>
> so the series $\sum_n m^*(D_n)$ converges (to at most $L$).
>
> Fix $\epsilon > 0$. For each $n$, choose an L-cover of $D_n$ with total volume less than $m^*(D_n) + \epsilon/2^n$. The union of all these covers is an L-cover of $E = \bigcup_n D_n$ with total volume:
>
> $$
> \sum_n \left(m^*(D_n) + \frac{\epsilon}{2^n}\right) = \sum_n m^*(D_n) + \epsilon \leq L + \epsilon.
> $$
>
> Therefore $m^*(E) \leq L + \epsilon$. Since $\epsilon > 0$ was arbitrary, $m^*(E) \leq L < \infty$, contradicting $m^*(E) = \infty$.
>
> Thus $\sup_n m^*(E \cap M_n) = \infty$, and since $\{m^*(E \cap M_n)\}$ is monotone increasing, $\lim_{n \to \infty} m^*(E \cap M_n) = \infty = m^*(E)$.

^pf-13-7

*Uses:* [[Properties of Lebesgue Outer Measure|§10.1]], [[§10 Lebesgue Outer Measure#^rem-10-1|Rem. §9.1]], [[§10 Lebesgue Outer Measure#^prop-10-2|§10.2]], [[§11 Lebesgue Measurable Sets#^def-11-1|Def. §11.1]], [[§11 Lebesgue Measurable Sets#^thm-11-1|§11.1]], [[§12 Borel Sets and Measure Spaces#^prop-12-5|§12.5]], [[Continuity of Measure|§13.4]], [[§14 Series#^thm-14-1|451 §14.1]], [[Monotone Convergence Theorem|451 Monotone Convergence Theorem]]
