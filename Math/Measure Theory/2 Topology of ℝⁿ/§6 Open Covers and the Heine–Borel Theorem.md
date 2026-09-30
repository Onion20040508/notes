---
type: section
subject: "[[Measure Theory]]"
chapter: 2
section: 6
tags: [measure-theory, math551]
---
← [[§5 Topology of ℝⁿ]] · ↑ [[2 Topology of ℝⁿ]] · [[§7 Structure of Open Sets]] →

## Open Covers

> [!definition] Definition §6.1: Open Cover
> Let $\mathcal{C}$ be a collection of open sets $\{\mathcal{O}\}$. We say $\mathcal{C}$ is an **open cover** of a set $E$ if
>
> $$
> E \subseteq \bigcup_{\mathcal{O} \in \mathcal{C}} \mathcal{O}.
> $$

^def-6-1

> [!remark]- Connections
> - Topology: this is “$\mathcal{C}$ covers $E$” by open sets of the ambient space ([[§15 Compact Spaces#^def-15-3|590 Def. §15.3]]), equivalent for compactness to open coverings of $E$ itself ([[§15 Compact Spaces#^lem-15-1|590 Lemma §15.1]]).

> [!example] Example §6.1: Open cover of the unit interval
> Let $\mathcal{C} = \{(-1, \frac{1}{2}), (0, 1), (\frac{1}{2}, 2)\}$. Then $\mathcal{C}$ is an open cover of $[0,1]$ since
>
> $$
> [0,1] \subseteq (-1, \tfrac{1}{2}) \cup (0, 1) \cup (\tfrac{1}{2}, 2).
> $$

^ex-6-1

![[m551-6-1.svg]]
*The cover of Example §6.1: the three open intervals (blue, hollow endpoints) stacked above $[0,1]$. Every point of $[0,1]$ lies in at least one of them; the endpoints are the delicate points — $0$ is caught only by $(-1,\tfrac12)$ and $1$ only by $(\tfrac12,2)$.*

> [!example] Example §6.2: Countable open cover from rationals
> Let $\mathbb{Q} = \{r_1, r_2, r_3, \ldots\}$ be an enumeration of the rationals. For $\epsilon > 0$, let
>
> $$
> I_k = (r_k - \tfrac{\epsilon}{2^k}, r_k + \tfrac{\epsilon}{2^k}).
> $$
>
> Then $\mathcal{C} = \{I_k\}_{k=1}^\infty$ is an open cover of $\mathbb{Q}$.

^ex-6-2

![[m551-6-2.svg]]
*The cover of Example §6.2 for the first few rationals of an enumeration (for instance $r_1 = \tfrac12$, $r_2 = \tfrac13$, $r_3 = \tfrac23$, $r_4 = \tfrac14$, $r_5 = \tfrac34$, with $\epsilon = 0.4$). Each $r_k$ (red) gets an interval $I_k$ of length $2\epsilon/2^k$, so the total length is at most $2\epsilon$ although every rational is covered — the idea behind countable sets having measure zero.*

> [!remark]- Connections
> - The enumeration exists by [[§3 Countability of Rationals and Unions#^cor-3-2|Corollary §3.2]]; the same $\epsilon/2^k$ cover shows [[§9 Lebesgue Outer Measure#^ex-9-2|Countable Sets Have Measure Zero]].

> [!theorem] Theorem §6.1: Every Open Cover Has a Countable Subcover
> Every open cover $\mathcal{C}$ has a countable subcover. That is, if $\mathcal{C} = \{\mathcal{O}_\alpha\}_{\alpha \in I}$, then there exists a countable subcollection $\mathcal{C}_1 = \{\mathcal{O}_{\alpha_j}\}_{j \in J}$ with $J \subseteq I$ countable, such that
>
> $$
> \bigcup_{\alpha \in I} \mathcal{O}_\alpha = \bigcup_{j \in J} \mathcal{O}_{\alpha_j}.
> $$

^thm-6-1

> [!remark]- Connections
> - Topology: every subspace of $\mathbb{R}^n$ is [[§18 Countability Axioms#^def-18-6|Lindelöf]], because $\mathbb{R}^n$ is [[§18 Countability Axioms#^ex-18-4|second-countable]] and [[§18 Countability Axioms#^thm-18-6|second-countable spaces are Lindelöf (590 §18.6)]]; the rational balls of the lemmas below are the countable basis.

> [!theorem] Lemma §6.2
> The set $\{B(r, \frac{1}{k}) \mid r \in \mathbb{Q}^n, k \in \mathbb{N}\}$ is countable.

^lem-6-2

> [!proof]+ Proof
> We first establish that open balls are uniquely determined by their center and radius.
>
> **Claim:** If $B(x_1, r_1) = B(x_2, r_2)$ as sets, then $x_1 = x_2$ and $r_1 = r_2$.
>
> **Proof of Claim:**
>
> *Step 1: $x_1 = x_2$.*
>
> Suppose for contradiction that $x_1 \neq x_2$.
>
> Since $x_1 \in B(x_1, r_1) = B(x_2, r_2)$, we have $|x_1 - x_2| < r_2$.
>
> Since $x_2 \in B(x_2, r_2) = B(x_1, r_1)$, we have $|x_2 - x_1| < r_1$.
>
> Let $\epsilon > 0$ be small. Consider the point
>
> $$
> y = x_1 + (r_1 - \epsilon) \cdot \frac{x_1 - x_2}{|x_1 - x_2|}.
> $$
>
> Then $|y - x_1| = r_1 - \epsilon < r_1$, so $y \in B(x_1, r_1)$.
>
> Since $B(x_1, r_1) = B(x_2, r_2)$, we must have $y \in B(x_2, r_2)$, i.e., $|y - x_2| < r_2$.
>
> But
>
> $$
> |y - x_2| = \left| x_1 - x_2 + (r_1 - \epsilon) \cdot \frac{x_1 - x_2}{|x_1 - x_2|} \right| = |x_1 - x_2| + (r_1 - \epsilon),
> $$
>
> so we need $|x_1 - x_2| + r_1 - \epsilon < r_2$.
>
> By symmetry (considering the point $z = x_2 + (r_2 - \epsilon) \cdot \frac{x_2 - x_1}{|x_2 - x_1|}$), we also get $|x_1 - x_2| + r_2 - \epsilon < r_1$.
>
> Adding these two inequalities:
>
> $$
> 2|x_1 - x_2| + r_1 + r_2 - 2\epsilon < r_1 + r_2,
> $$
>
> which gives $|x_1 - x_2| < \epsilon$.
>
> Since $\epsilon > 0$ is arbitrary, we conclude $x_1 = x_2$.
>
> *Step 2: $r_1 = r_2$.*
>
> Now with $x_1 = x_2 = x$, we have $B(x, r_1) = B(x, r_2)$.
>
> Suppose for contradiction that $r_1 \neq r_2$. WLOG assume $r_1 < r_2$.
>
> Choose $y \in \mathbb{R}^n$ with $r_1 < |y - x| < r_2$. Then $y \in B(x, r_2)$ but $y \notin B(x, r_1)$, contradicting $B(x, r_1) = B(x, r_2)$.
>
> Therefore $r_1 = r_2$. This completes the proof of the claim.
>
> **Conclusion:**
>
> The map $(r, k) \mapsto B(r, \frac{1}{k})$ from $\mathbb{Q}^n \times \mathbb{N}$ to $\{B(r, \frac{1}{k}) \mid r \in \mathbb{Q}^n, k \in \mathbb{N}\}$ is a surjection by definition, and by the claim above, it is also an injection.
>
> Since $\mathbb{Q}^n$ is countable (as a finite product of countable sets) and $\mathbb{N}$ is countable, the product $\mathbb{Q}^n \times \mathbb{N}$ is countable.
>
> Therefore $\{B(r, \frac{1}{k}) \mid r \in \mathbb{Q}^n, k \in \mathbb{N}\}$ is countable.

^pf-6-2

*Uses:* [[§5 Topology of ℝⁿ#^def-5-1|Def. §5.1]], [[§3 Countability of Rationals and Unions#^cor-3-2|§3.2]], [[§1 Countability and Set Theory#^ex-1-3|Ex. §1.3]], [[§1 Countability and Set Theory#^def-1-6|Def. §1.6]]

> [!remark]- Connections
> - Listed as an application of [[Measure Theory Problem-Solving Techniques#^ex-19-8|Technique 1 (Ex. §19.8, HW1)]].

> [!theorem] Lemma §6.3
> For any open ball $B(x, \rho)$ with $\rho > 0$, there exist $r \in \mathbb{Q}^n$ and $k \in \mathbb{N}$ such that $x \in B(r, \frac{1}{k}) \subseteq B(x, \rho)$.

^lem-6-3

> [!proof]+ Proof
> Given $B(x, \rho)$, choose $k \in \mathbb{N}$ large enough that $\frac{2}{k} < \rho$, i.e., $k > \frac{2}{\rho}$.
>
> Since $\mathbb{Q}^n$ is dense in $\mathbb{R}^n$ ([[§4 The Completeness Axiom#^thm-4-7|density of ℚ]]), there exists $r \in \mathbb{Q}^n$ with $|r - x| < \frac{1}{k}$.
>
> Then $x \in B(r, \frac{1}{k})$.
>
> We claim $B(r, \frac{1}{k}) \subseteq B(x, \rho)$. Let $y \in B(r, \frac{1}{k})$. Then:
>
> $$
> |y - x| \leq |y - r| + |r - x| < \frac{1}{k} + \frac{1}{k} = \frac{2}{k} < \rho.
> $$
>
> Thus $y \in B(x, \rho)$.

^pf-6-3

*Uses:* [[§5 Topology of ℝⁿ#^def-5-1|Def. §5.1]], [[Archimedean Property|451 §4.5]], [[§4 The Completeness Axiom#^thm-4-7|451 §4.7]], [[Triangle inequality|LADR 6.17]]

![[m551-6-3.svg]]
*Lemma §6.3: with $\tfrac2k < \rho$ and a rational point $r$ within $\tfrac1k$ of $x$, the rational ball $B(r,\tfrac1k)$ (red) contains $x$ and fits inside $B(x,\rho)$ (blue). For any $y$ in it, the detour $y \to r \to x$ is shorter than $\tfrac1k + \tfrac1k < \rho$ — the triangle inequality of the proof.*

> [!remark]- Connections
> - Topology: this is the argument that a separable metric space is second-countable ([[§18 Countability Axioms#^prop-18-4|590 §18.4]] (3)), with $D = \mathbb{Q}^n$ ([[§18 Countability Axioms#^ex-18-8|590 Ex. §18.8]]); so the rational balls form a countable [[§2 Basis for a Topology#^def-2-1|basis]] for $\mathbb{R}^n$.

> [!proof]+ Proof of Theorem 6.1 (Countable Subcover)
> Let $\mathcal{C} = \{\mathcal{O}_\alpha\}_{\alpha \in A}$ be an open cover, i.e., $\bigcup_{\alpha \in A} \mathcal{O}_\alpha = E$ for some set $E$.
>
> Let $x \in E$. Then $x \in \mathcal{O}_{\alpha_0}$ for some $\alpha_0 \in A$. Since $\mathcal{O}_{\alpha_0}$ is [[§5 Topology of ℝⁿ#^def-5-2|open]], there exists $\rho > 0$ such that $B(x, \rho) \subseteq \mathcal{O}_{\alpha_0}$.
>
> By [[§6 Open Covers and the Heine–Borel Theorem#^lem-6-3|Lemma §6.3]], there exist $r_x \in \mathbb{Q}^n$ and $k_x \in \mathbb{N}$ such that $x \in B(r_x, \frac{1}{k_x}) \subseteq B(x, \rho) \subseteq \mathcal{O}_{\alpha_0}$.
>
> Now we have a collection of rational balls:
>
> $$
> \mathcal{C}_1 = \left\{ B\left(r_x, \frac{1}{k_x}\right) \,\bigg|\, x \in E \right\}.
> $$
>
> Since each ball has center in $\mathbb{Q}^n$ and radius $\frac{1}{k}$ for some $k \in \mathbb{N}$, by [[§6 Open Covers and the Heine–Borel Theorem#^lem-6-2|Lemma §6.2]], $\mathcal{C}_1$ is a subset of a countable set, hence countable.
>
> Write $\mathcal{C}_1 = \{B_1, B_2, B_3, \ldots\}$ (finite or countably infinite).
>
> For each $B_j \in \mathcal{C}_1$, choose $\alpha_j \in A$ such that $B_j \subseteq \mathcal{O}_{\alpha_j}$ (such $\alpha_j$ exists by construction).
>
> Then:
>
> $$
> E = \bigcup_{x \in E} \{x\} \subseteq \bigcup_{x \in E} B\left(r_x, \frac{1}{k_x}\right) = \bigcup_{j=1}^\infty B_j \subseteq \bigcup_{j=1}^\infty \mathcal{O}_{\alpha_j} \subseteq \bigcup_{\alpha \in A} \mathcal{O}_\alpha = E.
> $$
>
> Thus $\bigcup_{j=1}^\infty \mathcal{O}_{\alpha_j} = E$, so $\{\mathcal{O}_{\alpha_j}\}_{j=1}^\infty$ is a countable subcover.

^pf-6-1

*Uses:* [[§5 Topology of ℝⁿ#^def-5-2|Def. §5.2]], [[§6 Open Covers and the Heine–Borel Theorem#^lem-6-3|§6.3]], [[§6 Open Covers and the Heine–Borel Theorem#^lem-6-2|§6.2]]

## The Heine–Borel Theorem

> [!theorem] Theorem §6.4: Heine–Borel
> Let $F$ be a bounded closed set in $\mathbb{R}^n$. Then any open cover of $F$ has a finite subcover.

^thm-6-4

> [!proof]+ Proof
> By [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-1|the previous theorem]], we can assume the open cover $\mathcal{C}$ of $F$ is countable: $\mathcal{C} = \{\mathcal{O}_1, \mathcal{O}_2, \mathcal{O}_3, \ldots\}$.
>
> We have $F \subseteq \bigcup_{j=1}^\infty \mathcal{O}_j$. We want to show $F \subseteq \bigcup_{j=1}^{k_0} \mathcal{O}_j$ for some $k_0 \in \mathbb{N}$.
>
> Define $F_k = F \setminus \bigcup_{j=1}^k \mathcal{O}_j$ for each $k \in \mathbb{N}$.
>
> Note that $\bigcup_{j=1}^k \mathcal{O}_j$ is open (finite union of open sets), so $F_k$ is the intersection of a closed set $F$ with a closed set (complement of an open set), hence $F_k$ is closed. Also $F_k$ is bounded (as a subset of the bounded set $F$).
>
> Moreover, $F_1 \supseteq F_2 \supseteq F_3 \supseteq \cdots$ (nested).
>
> **Case 1:** If there exists $k_0 \in \mathbb{N}$ with $F_{k_0} = \emptyset$, then
>
> $$
> F \subseteq \bigcup_{j=1}^{k_0} \mathcal{O}_j,
> $$
>
> and we are done.
>
> **Case 2:** If $F_k \neq \emptyset$ for all $k \in \mathbb{N}$, then by [[§5 Topology of ℝⁿ#^thm-5-2|Cantor's Nested Set Theorem]],
>
> $$
> \bigcap_{k=1}^\infty F_k \neq \emptyset.
> $$
>
> Choose $x_0 \in \bigcap_{k=1}^\infty F_k$. Then $x_0 \in F$ and $x_0 \notin \bigcup_{j=1}^k \mathcal{O}_j$ for all $k$, i.e., $x_0 \notin \bigcup_{j=1}^\infty \mathcal{O}_j$.
>
> But $F \subseteq \bigcup_{j=1}^\infty \mathcal{O}_j$, so $x_0 \in \bigcup_{j=1}^\infty \mathcal{O}_j$. Contradiction.
>
> Thus Case 2 cannot occur, and Case 1 must hold.

^pf-6-4

*Uses:* [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-1|§6.1]], [[§5 Topology of ℝⁿ#^thm-5-2|§5.2]], [[§5 Topology of ℝⁿ#^def-5-3|Def. §5.3]], [[§13 Some Topological Concepts in Metric Spaces#^prop-13-4|451 §13.4]]

![[m551-6-4.svg]]
*The Heine–Borel proof in one dimension, for a closed interval $F$ covered by open intervals $\mathcal{O}_1, \mathcal{O}_2, \ldots$ (blue). Removing the open sets one at a time leaves closed sets $F_k = F \setminus (\mathcal{O}_1 \cup \cdots \cup \mathcal{O}_k)$ (red) that shrink; if none were empty, Cantor's nested set theorem would produce a point of $F$ in no $\mathcal{O}_j$. Here $F_4 = \emptyset$, so $\mathcal{O}_1, \ldots, \mathcal{O}_4$ is a finite subcover.*

> [!remark]- Connections
> - Topology: [[Heine–Borel Theorem]] (590 §15.12) proves compact ⟺ closed and bounded via products of [[§15 Compact Spaces#^thm-15-10|compact closed intervals]] and the [[Tube Lemma]]; here only “closed and bounded ⟹ compact” is proved, through countable subcovers and nested sets (the [[§15 Compact Spaces#^thm-15-5|finite intersection property]] in disguise).
> - Used for the outer measure of closed rectangles ([[§9 Lebesgue Outer Measure#^prop-9-2|Proposition §9.2]]) and for approximation by finite unions of rectangles ([[§11 Borel Sets and Measure Spaces#^thm-11-11|Theorem §11.11]]).
