---
type: section
subject: "[[Measure Theory]]"
chapter: 2
section: 7
tags: [measure-theory, math551]
---
← [[§6 Open Covers and the Heine–Borel Theorem]] · ↑ [[· 2 Topology of ℝⁿ]] · [[§8 Motivation꞉ The Riemann Integral]] →

> [!theorem] Lemma §7.1
> Any collection of mutually disjoint open intervals on $\mathbb{R}$ is countable.

^lem-7-1

> [!proof]+ Proof
> For each open interval, choose a rational number contained in it ([[§4 The Completeness Axiom#^thm-4-7|density of ℚ]]). Since the intervals are disjoint, different intervals contain different rationals. This gives an injection from the collection of intervals into $\mathbb{Q}$, which is [[§3 Countability of Rationals and Unions#^cor-3-2|countable]].

^pf-7-1

*Uses:* [[§4 The Completeness Axiom#^thm-4-7|451 §4.7]], [[§3 Countability of Rationals and Unions#^cor-3-2|§3.2]], [[§1 Countability and Set Theory#^def-1-3|Def. §1.3]]

> [!theorem] Proposition §7.2: Open Sets in $\mathbb{R}$ are Countable Unions of Disjoint Intervals
> Any open set $O \subseteq \mathbb{R}$ is a countable union of mutually disjoint open intervals.

^prop-7-2

> [!proof]+ Proof of Proposition
> Let $O \subseteq \mathbb{R}$ be open. For each $x \in O$, define:
>
> $$
> a_x = \inf\{a \mid (a, x] \subseteq O\}, \quad b_x = \sup\{b \mid [x, b) \subseteq O\}.
> $$
>
> Here the infimum and supremum are taken in the extended reals, so $a_x = -\infty$ or $b_x = +\infty$ is allowed (e.g. $O = \mathbb{R}$); in every case $(a_x, b_x)$ is an open interval, possibly unbounded.
>
> **Step 1: The sets are non-empty and $a_x < x < b_x$.**
>
> Since $x \in O$ and $O$ is [[§5 Topology of ℝⁿ#^def-5-2|open]], there exists $\epsilon > 0$ with $(x - \epsilon, x + \epsilon) \subseteq O$.
>
> Then $(x - \epsilon, x] \subseteq O$, so $x - \epsilon \in \{a \mid (a, x] \subseteq O\}$. Thus the set is non-empty and $a_x \leq x - \epsilon < x$.
>
> Similarly, $[x, x + \epsilon) \subseteq O$, so $x + \epsilon \in \{b \mid [x, b) \subseteq O\}$. Thus the set is non-empty and $b_x \geq x + \epsilon > x$.
>
> **Step 2: $(a_x, b_x) \subseteq O$.**
>
> Let $y \in (a_x, b_x)$. We show $y \in O$.
>
> *Case 1:* $y \leq x$. Since $y > a_x = \inf\{a \mid (a, x] \subseteq O\}$, there exists $a$ with $a_x \leq a < y$ such that $(a, x] \subseteq O$. Then $y \in (a, x] \subseteq O$.
>
> *Case 2:* $y > x$. Since $y < b_x = \sup\{b \mid [x, b) \subseteq O\}$, there exists $b$ with $y < b \leq b_x$ such that $[x, b) \subseteq O$. Then $y \in [x, b) \subseteq O$.
>
> **Step 3: $a_x \notin O$ and $b_x \notin O$ (hence $(a_x, b_x)$ is maximal).**
>
> If $a_x = -\infty$ there is nothing to prove, so let $a_x$ be real and suppose for contradiction that $a_x \in O$. Since $O$ is open, there exists $\delta > 0$ such that $(a_x - \delta, a_x + \delta) \subseteq O$.
>
> By Step 2, $(a_x, x] \subseteq O$. We claim $(a_x - \delta, x] \subseteq O$.
>
> Let $z \in (a_x - \delta, x]$. Either $z \in (a_x - \delta, a_x + \delta) \subseteq O$, or $z \in (a_x, x] \subseteq O$. Either way, $z \in O$.
>
> Thus $(a_x - \delta, x] \subseteq O$, so $a_x - \delta \in \{a \mid (a, x] \subseteq O\}$. But $a_x - \delta < a_x$, contradicting $a_x = \inf\{a \mid (a, x] \subseteq O\}$.
>
> Therefore $a_x \notin O$. By a symmetric argument, $b_x \notin O$ (when $b_x < \infty$).
>
> **Step 4: $(a_x, b_x)$ is the maximal open interval containing $x$ in $O$.**
>
> Suppose $I = (\alpha, \beta)$ (with $-\infty \leq \alpha < \beta \leq \infty$) is an open interval with $x \in I \subseteq O$. We show $I \subseteq (a_x, b_x)$.
>
> Since $(\alpha, x] \subseteq I \subseteq O$, every real $a$ with $\alpha \leq a < x$ lies in $\{a \mid (a, x] \subseteq O\}$, hence $a_x \leq \alpha$.
>
> Since $[x, \beta) \subseteq I \subseteq O$, every real $b$ with $x < b \leq \beta$ lies in $\{b \mid [x, b) \subseteq O\}$, hence $b_x \geq \beta$.
>
> Therefore $I = (\alpha, \beta) \subseteq (a_x, b_x)$.
>
> **Step 5: Either $(a_x, b_x) = (a_y, b_y)$ or $(a_x, b_x) \cap (a_y, b_y) = \emptyset$.**
>
> Suppose $(a_x, b_x) \cap (a_y, b_y) \neq \emptyset$. Since both are open intervals, their union $(a_x, b_x) \cup (a_y, b_y)$ is also an open interval (the union of two overlapping open intervals is an interval).
>
> This union is an open interval containing $x$ and contained in $O$. By maximality (Step 4), $(a_x, b_x) \cup (a_y, b_y) \subseteq (a_x, b_x)$.
>
> But $(a_x, b_x) \subseteq (a_x, b_x) \cup (a_y, b_y)$, so $(a_x, b_x) = (a_x, b_x) \cup (a_y, b_y)$.
>
> This means $(a_y, b_y) \subseteq (a_x, b_x)$. By the symmetric argument, $(a_x, b_x) \subseteq (a_y, b_y)$.
>
> Therefore $(a_x, b_x) = (a_y, b_y)$.
>
> **Conclusion:** Let $\mathcal{C} = \{(a_x, b_x) \mid x \in O\}$. The distinct intervals in $\mathcal{C}$ are mutually disjoint. By [[§7 Structure of Open Sets#^lem-7-1|the lemma]], this collection is countable. Write $\mathcal{C}_1 = \{(a_j, b_j) \mid j \in J\}$ for the collection of distinct intervals.
>
> Then $O = \bigcup_{x \in O} \{x\} \subseteq \bigcup_{x \in O} (a_x, b_x) = \bigcup_{j \in J} (a_j, b_j) \subseteq O$.
>
> Thus $O = \bigcup_{j \in J} (a_j, b_j)$, a countable union of disjoint open intervals.

^pf-7-2

*Uses:* [[§5 Topology of ℝⁿ#^def-5-2|Def. §5.2]], [[§7 Structure of Open Sets#^lem-7-1|§7.1]], [[Completeness Axiom|451 Def. §4.4]], [[Characterization of the Supremum|451 §4.3]]

![[m551-7-1.svg]]
*An open set $O \subseteq \mathbb{R}$ (blue) and its components. For $x \in O$, stretching left and right as far as $O$ allows gives $(a_x, b_x)$; its endpoints are not in $O$ (red, hollow), since otherwise the interval could be stretched further (Step 3). Distinct components are disjoint and each contains a rational $q_j$ — the injection into $\mathbb{Q}$ of [[§7 Structure of Open Sets#^lem-7-1|Lemma §7.1]] that makes the family countable.*

> [!remark]- Connections
> - MATH 451 states this as a fact without proof: [[§13 Some Topological Concepts in Metric Spaces#^rem-13-5|Structure of open and closed subsets of the line]].
> - Topology: the intervals $(a_x, b_x)$ built above are the maximal connected subsets of $O$ ([[§16 Connected Subspaces of ℝ#^cor-16-2|intervals in ℝ are connected]]).
> - Gives the case $n = 1$ of [[§12 Borel Sets and Measure Spaces#^thm-12-6|Open Sets are Measurable]]; used again in [[§22 The General Lebesgue Integral#^ex-22-2|Example §22.2]].

## Open Sets in $\mathbb{R}^n$

> [!definition] Definition §7.1: Open Rectangles
> An **open rectangle** in $\mathbb{R}^n$ is a set of the form
>
> $$
> \prod_{j=1}^{n} (a_j, b_j) = (a_1, b_1) \times (a_2, b_2) \times \cdots \times (a_n, b_n).
> $$

^def-7-1

> [!remark]- Connections
> - Rectangles and their volumes are the building blocks of outer measure: [[§10 Lebesgue Outer Measure#^def-10-1|Definition §10.1]].
> - Topology: open rectangles with rational endpoints form a countable basis of $\mathbb{R}^n$ ([[§22 Countability Axioms#^ex-22-4|590 Ex. §22.4]]).

> [!definition] Definition §7.2: Half-Open Rectangles
> A **half-open half-closed rectangle** is a set of the form
>
> $$
> \prod_{j=1}^{n} (a_j, b_j] = (a_1, b_1] \times (a_2, b_2] \times \cdots \times (a_n, b_n].
> $$

^def-7-2

![[m551-7-2.svg]]
*Left: a half-open rectangle in $\mathbb{R}^2$ contains its top and right edges (solid) but not its bottom and left edges (dashed); of the four corners only $(b_1, b_2)$ belongs to it. Right: this is what lets a dyadic square $R^{(k)}_{\mathbf{j}}$ split into $2^n = 4$ children $R^{(k+1)}_{2\mathbf{j}+\boldsymbol{\epsilon}}$ with no overlaps and no gaps (property (b) in the proof of [[§7 Structure of Open Sets#^prop-7-3|Proposition §7.3]]) — each shared edge belongs to exactly one child.*

> [!theorem] Proposition §7.3: Open Sets in $\mathbb{R}^n$ as Unions of Rectangles
> Any open set $O \subseteq \mathbb{R}^n$ is a countable union of mutually disjoint half-open half-closed rectangles (more precisely, cubes).

^prop-7-3

> [!proof]+ Proof
> **Step 1: Construct the dyadic partition system.**
>
> For each $k \in \mathbb{N}_0$, define the **dyadic partition of $\mathbb{R}^n$ at scale $2^{-k}$**. For each multi-index $\mathbf{j} = (j_1, \ldots, j_n) \in \mathbb{Z}^n$, define the **dyadic rectangle**:
>
> $$
> R_{\mathbf{j}}^{(k)} = \prod_{i=1}^{n} \left( \frac{j_i}{2^k}, \frac{j_i + 1}{2^k} \right].
> $$
>
> This construction has the following key properties:
> - (a) *Partition property*: For each fixed $k$, the collection $\{R_{\mathbf{j}}^{(k)} : \mathbf{j} \in \mathbb{Z}^n\}$ partitions $\mathbb{R}^n$:
>
>   $$
>   \mathbb{R}^n = \bigsqcup_{\mathbf{j} \in \mathbb{Z}^n} R_{\mathbf{j}}^{(k)}.
>   $$
>
> - (b) *Nesting property*: Each rectangle at scale $k$ is the disjoint union of $2^n$ rectangles at scale $k+1$:
>
>   $$
>   R_{\mathbf{j}}^{(k)} = \bigsqcup_{\boldsymbol{\epsilon} \in \{0,1\}^n} R_{2\mathbf{j} + \boldsymbol{\epsilon}}^{(k+1)}.
>   $$
>
> - (c) *Refinement property*: If $R_{\mathbf{j}}^{(k)}$ and $R_{\mathbf{j}'}^{(k')}$ are two dyadic rectangles (possibly at different scales), then either one contains the other, or they are disjoint.
> - (d) *Diameter bound*: Each $R_{\mathbf{j}}^{(k)}$ has side length $2^{-k}$, hence diameter $\mathrm{diam}(R_{\mathbf{j}}^{(k)}) = \frac{\sqrt{n}}{2^k}$.
>
> **Step 2: For each point in $O$, find a dyadic rectangle contained in $O$.**
>
> Let $x_0 \in O$. Since $O$ is [[§5 Topology of ℝⁿ#^def-5-2|open]], there exists $\varepsilon > 0$ such that $B(x_0, \varepsilon) \subseteq O$.
>
> *Claim*: There exists a dyadic rectangle $R_{\mathbf{j}}^{(k)}$ such that $x_0 \in R_{\mathbf{j}}^{(k)} \subseteq O$.
>
> *Proof of claim*: Choose $k \in \mathbb{N}$ large enough that $\frac{\sqrt{n}}{2^k} < \varepsilon$. Since the dyadic rectangles at scale $k$ partition $\mathbb{R}^n$, there exists a unique $\mathbf{j} \in \mathbb{Z}^n$ such that $x_0 \in R_{\mathbf{j}}^{(k)}$. For any $y \in R_{\mathbf{j}}^{(k)}$:
>
> $$
> \|y - x_0\| \leq \mathrm{diam}(R_{\mathbf{j}}^{(k)}) = \frac{\sqrt{n}}{2^k} < \varepsilon.
> $$
>
> Thus $R_{\mathbf{j}}^{(k)} \subseteq B(x_0, \varepsilon) \subseteq O$. $\diamond$
>
> **Step 3: Select a disjoint subcollection covering $O$.**
>
> Define the collection of **maximal** dyadic rectangles contained in $O$:
>
> $$
> \mathcal{R} = \left\{ R_{\mathbf{j}}^{(k)} : R_{\mathbf{j}}^{(k)} \subseteq O \text{ and the parent } R_{\lfloor \mathbf{j}/2 \rfloor}^{(k-1)} \not\subseteq O \text{ (or } k = 0) \right\}.
> $$
>
> Here $\lfloor \mathbf{j}/2 \rfloor = (\lfloor j_1/2 \rfloor, \ldots, \lfloor j_n/2 \rfloor)$ indexes the unique rectangle at scale $k-1$ containing $R_{\mathbf{j}}^{(k)}$.
>
> *Disjointness*: Let $R, R' \in \mathcal{R}$ with $R \neq R'$. By the refinement property, either $R \subseteq R'$, $R' \subseteq R$, or $R \cap R' = \emptyset$. If $R \subsetneq R'$, then $R' \subseteq O$ contradicts the maximality of $R$ (since $R'$ would be a larger rectangle containing $R$ and contained in $O$). Similarly $R' \subsetneq R$ is impossible. Thus $R \cap R' = \emptyset$.
>
> *Covering property*: We show $\bigcup_{R \in \mathcal{R}} R = O$.
> - ($\subseteq$): Each $R \in \mathcal{R}$ satisfies $R \subseteq O$ by definition.
> - ($\supseteq$): Let $x_0 \in O$. By Step 2, there exists some dyadic rectangle containing $x_0$ and contained in $O$. Among all such rectangles, consider those at the coarsest scale (smallest $k$). This maximal rectangle belongs to $\mathcal{R}$, so $x_0 \in \bigcup_{R \in \mathcal{R}} R$.
>
> **Step 4: Countability.**
>
> The collection $\mathcal{R}$ is countable since $\mathcal{R} \subseteq \bigcup_{k=0}^{\infty} \{R_{\mathbf{j}}^{(k)} : \mathbf{j} \in \mathbb{Z}^n\}$. Each set $\{R_{\mathbf{j}}^{(k)} : \mathbf{j} \in \mathbb{Z}^n\}$ is countable (indexed by $\mathbb{Z}^n$), and a [[Countable Union of Countable Sets is Countable|countable union of countable sets is countable]].
>
> **Conclusion:** We have $O = \bigsqcup_{R \in \mathcal{R}} R$, a countable disjoint union of half-open cubes.

^pf-7-3

*Uses:* [[§5 Topology of ℝⁿ#^def-5-2|Def. §5.2]], [[§5 Topology of ℝⁿ#^def-5-1|Def. §5.1]], [[§7 Structure of Open Sets#^def-7-2|Def. §7.2]], [[Countable Union of Countable Sets is Countable|§3.1]]

![[m551-7-3.svg]]
*The proof of [[§7 Structure of Open Sets#^prop-7-3|Proposition §7.3]] run on an open disc $O$ (dashed boundary), stopped at scale $2^{-4}$: the maximal dyadic squares contained in $O$ (blue, darker = coarser). Large squares fill the interior and ever smaller ones pile up towards the boundary; continuing through all scales, these disjoint squares exhaust $O$ exactly.*

> [!remark]- Connections
> - MATH 452: the same dyadic grid gives the inner Jordan approximations, $\mathcal{S}_i^-$ = dyadic squares inside $D$ ([[§20 Multivariable Integration#^def-20-4|452 Def. §20.4]]); for an open set they exhaust it.
> - Topology: open sets are unions of basis elements ([[§2 Basis for a Topology#^lem-2-1|590 Lemma §2.1]]); here the union is countable and disjoint.
> - Gives the case $n > 1$ of [[§12 Borel Sets and Measure Spaces#^thm-12-6|Open Sets are Measurable]].

> [!remark] Remark: Why Dyadic Subdivision?
> Using powers of $2$ (dyadic subdivision) is essential for the refinement property. If we instead subdivided using intervals of length $\frac{1}{k}$, the partition lines would shift at each scale: the partition at $k=2$ has lines at $0, 0.5, 1, \ldots$ while $k=3$ has lines at $0, 0.33, 0.67, 1, \ldots$. These do not align, breaking the nesting structure, so selecting a disjoint subcollection is no longer automatic. With dyadic subdivision, partition lines at scale $k$ are always a subset of partition lines at scale $k+1$, ensuring the refinement property holds.

^rem-7-1

![[m551-7-4.svg]]
*Top: dyadic grids of mesh $1, \tfrac12, \tfrac14, \tfrac18$ — every line of one scale is still a line at the next (dotted), so two dyadic intervals are either nested or disjoint. Bottom: meshes $\tfrac12$ and $\tfrac13$ as in the remark: $(0,\tfrac12]$ (blue) and $(\tfrac13,\tfrac23]$ (red) overlap (shaded) without either containing the other, and the selection of maximal pieces breaks down.*

> [!remark]- Connections
> - Dyadic partitions reappear in the proof that [[Riemann Integrable Implies Lebesgue Integrable|Riemann Integrability Implies Lebesgue Integrability]].
