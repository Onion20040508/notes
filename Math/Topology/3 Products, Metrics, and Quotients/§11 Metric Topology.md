---
type: section
subject: "[[Topology]]"
chapter: 3
section: 11
munkres: "§20, §21"
tags: [topology, math590]
---
← [[§10 Product Topology on Arbitrary Products]] · ↑ [[· 3 Products, Metrics, and Quotients]] · [[§12 Quotient Topology]] →

## Metrics and Metric Spaces

> [!definition] Definition §11.1: Metric
> A **metric** on a set $X$ is a function $d: X \times X \to \mathbb{R}$ satisfying:
>
> 1. $d(x, y) \geq 0$ for all $x, y \in X$, and $d(x, y) = 0 \Leftrightarrow x = y$.
> 2. $d(x, y) = d(y, x)$ for all $x, y \in X$. (Symmetry)
> 3. $d(x, y) \leq d(x, z) + d(z, y)$ for all $x, y, z \in X$. (Triangle inequality)

^def-11-1

> [!remark]- Connections
> - MATH 451 version: [[§13 Some Topological Concepts in Metric Spaces#^def-13-1|Definition §13.1: Metric Space]].
> - Normed spaces as metric spaces: [[§8 Normed Linear Spaces#^def-8-3|556 Def. §8.3]] restates this definition, and [[§8 Normed Linear Spaces#^prop-8-2|556 Prop. §8.2]] shows that a norm gives the metric d(x, y) = ‖x − y‖.
> - Every normed space, in particular each Lᵖ, is a metric space: [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-1|551 Prop. §19.1]]; the L¹ metric: [[§16 The L¹ Space and Density Theorems#^def-16-2|551 Def. §16.2]].

> [!example] Example §11.1: Euclidean Metric on $\mathbb{R}^n$
> $x = (x_1, \ldots, x_n), y = (y_1, \ldots, y_n) \in \mathbb{R}^n$.
>
> $$
> d(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}
> $$

^ex-11-1

> [!example] Example §11.2: Square Metric on $\mathbb{R}^n$
> $$
> \rho(x, y) = \max\{|x_1 - y_1|, |x_2 - y_2|, \ldots, |x_n - y_n|\}
> $$

^ex-11-2

## $\varepsilon$-Balls and the Metric Topology

> [!definition] Definition §11.2: $\varepsilon$-Ball
> Given a metric $d$ on $X$, $x \in X$, $\varepsilon > 0$, the **$\varepsilon$-ball centered at $x$** is
>
> $$
> B_d(x, \varepsilon) = \{y \in X \mid d(y, x) < \varepsilon\} \subseteq X
> $$

^def-11-2

> [!remark]- Connections
> - Balls of a norm, and interior points defined through them: [[§8 Normed Linear Spaces#^def-8-9|556 Def. §8.9]].

> [!definition] Definition §11.3: Metric Topology
> If $d$ is a metric on $X$, then the collection of all $\varepsilon$-balls $B_d(x, \varepsilon)$, $x \in X$, $\varepsilon > 0$, is a basis for a topology on $X$, called the **metric topology** induced by $d$.

^def-11-3

> [!proof]+ Proof that $\varepsilon$-balls form a basis
> We check the [[§2 Basis for a Topology#^def-2-1|basis axioms]].
>
> (1) If $x \in X$, then $x \in B_d(x, \varepsilon)$ for any $\varepsilon > 0$. ✓
>
> (2) Let $y \in B_d(x_1, \varepsilon_1) \cap B_d(x_2, \varepsilon_2)$. We need to find $\delta > 0$ such that $B_d(y, \delta) \subseteq B_d(x_1, \varepsilon_1) \cap B_d(x_2, \varepsilon_2)$.
>
> Let $\delta_1 = \varepsilon_1 - d(y, x_1) > 0$ and $\delta_2 = \varepsilon_2 - d(y, x_2) > 0$. Set $\delta = \min(\delta_1, \delta_2)$.
>
> **Claim:** $B_d(y, \delta) \subseteq B_d(x_1, \varepsilon_1)$ (similar for $B_d(x_2, \varepsilon_2)$).
>
> *Proof:* Let $z \in B_d(y, \delta)$. Then
>
> $$
> d(x_1, z) \leq d(x_1, y) + d(y, z) < d(x_1, y) + \delta_1 = d(x_1, y) + \varepsilon_1 - d(y, x_1) = \varepsilon_1
> $$
>
> Similarly for $B_d(x_2, \varepsilon_2) \supseteq B_d(y, \delta)$. So $\mathcal{B}_d$ is indeed a basis.

^pf-def-11-3

*Uses:* [[§2 Basis for a Topology#^def-2-1|Def. §2.1]]

![[m590-11-2.svg]]
*The basis axiom for $\varepsilon$-balls: $y$ lies in both balls (blue, open), at distance $d(x_i, y)$ from each center. The slack left before each boundary is $\delta_i = \varepsilon_i - d(y, x_i)$ (red segments). The ball $B_d(y, \delta)$ with $\delta = \min(\delta_1, \delta_2)$ fits inside both. Here $\delta = \delta_2$, so the small ball touches the boundary of $B_d(x_2, \varepsilon_2)$ from inside without crossing it.*

> [!remark]- Connections
> - MATH 451 open sets in a metric space: [[§13 Some Topological Concepts in Metric Spaces#^def-13-5|Definition §13.5: Open and Closed Subsets]].
> - For the Euclidean metric these are the open sets of ℝⁿ in 551: [[§5 Topology of ℝⁿ#^def-5-2|551 Def. §5.2]] (balls: [[§5 Topology of ℝⁿ#^def-5-1|551 Def. §5.1]]).

## Examples of Metric Spaces

> [!example] Example §11.3: Euclidean Metric Induces Standard Topology
> $\mathbb{R}^n$, $d(x,y) = \|x - y\| = \left(\sum_{i=1}^{n}(x_i - y_i)^2\right)^{1/2}$ induces the standard topology.

^ex-11-3

> [!example] Example §11.4: Discrete Metric
> $X$ any set. Define $d(x,y) = \begin{cases} 0 & x = y \\ 1 & x \neq y \end{cases}$. This induces the [[§1 Topological Spaces#^ex-1-3|discrete topology]].
>
> (Since every singleton $\{x\} = B(x, \frac{1}{2})$ is open.)

^ex-11-4

> [!example] Example §11.5: Sup-Metric on $\mathbb{R}^n$
> $\rho(x,y) = \max_i\{|x_i - y_i|\}$, the “sup-metric.”

^ex-11-5

## Comparing Metric Topologies

> [!theorem] Lemma §11.1: Comparing Metric Topologies
> Let $d$ and $d'$ be two metrics on $X$. Let $\mathcal{T}_d$ and $\mathcal{T}_{d'}$ be the two topologies induced on $X$. Then $\mathcal{T}_{d'}$ is [[§1 Topological Spaces#^def-1-2|finer]] than $\mathcal{T}_d$ if and only if for all $x \in X$ and each $\varepsilon > 0$, there exists $\delta > 0$ such that $B_{d'}(x, \delta) \subseteq B_d(x, \varepsilon)$.

^lem-11-1

> [!proof]+ Proof
> $(\Rightarrow)$ Suppose $\mathcal{T}_{d'}$ finer than $\mathcal{T}_d$. Let $B_d(x, \varepsilon)$ be a basis element of $\mathcal{T}_d$. Then $B_d(x, \varepsilon)$ is open in $\mathcal{T}_d$, hence open in $\mathcal{T}_{d'}$. So there exists $B' \in \mathcal{B}_{d'}$ (some basis for $\mathcal{T}_{d'}$) such that $x \in B' \subseteq B_d(x, \varepsilon)$. Writing $B' = B_{d'}(x', \delta')$, find $B_{d'}(x, \delta) \subseteq B' \subseteq B_d(x, \varepsilon)$.
>
> $(\Leftarrow)$ Conversely, suppose the “$\varepsilon$-$\delta$” condition holds. Want to show $\mathcal{T}_{d'}$ finer than $\mathcal{T}_d$.
>
> Given a basis element $B = B_d(x, \varepsilon)$ for $\mathcal{T}_d$, let $y \in B$. By the triangle inequality, $B_d(y, \varepsilon_y) \subseteq B$ with $\varepsilon_y = \varepsilon - d(x, y) > 0$. By hypothesis (applied at $y$), there exists $\delta_y > 0$ with $B_{d'}(y, \delta_y) \subseteq B_d(y, \varepsilon_y) \subseteq B$. Then $B = \bigcup_{y \in B} B_{d'}(y, \delta_y)$ is open in $\mathcal{T}_{d'}$.

^pf-11-1

*Uses:* [[§2 Basis for a Topology#^lem-2-1|§2.1]], [[§11 Metric Topology#^def-11-3|Def. §11.3]]

> [!remark]- Connections
> - The metric form of [[§2 Basis for a Topology#^lem-2-2|Lemma §2.2: Comparing Topologies via Bases]], with $\varepsilon$-balls as the bases.

> [!theorem] Theorem §11.2: Euclidean and Square Metrics Induce Same Topology
> The topologies on $\mathbb{R}^n$ induced by metrics $d$ (Euclidean) and $\rho$ (square) are the same as the product topology on $\mathbb{R}^n$.

^thm-11-2

> [!proof]+ Proof
> Let $x = (x_1, \ldots, x_n), y = (y_1, \ldots, y_n) \in \mathbb{R}^n$. Can check: $\rho(x,y) \leq d(x,y) \leq \sqrt{n}\,\rho(x,y)$.
>
> 1st inequality $\Rightarrow$ $B_d(x, \varepsilon) \subseteq B_\rho(x, \varepsilon)$ for all $x, \varepsilon$.
>
> 2nd inequality $\Rightarrow$ $B_\rho(x, \frac{\varepsilon}{\sqrt{n}}) \subseteq B_d(x, \varepsilon)$ for all $x, \varepsilon$.
>
> By [[§11 Metric Topology#^lem-11-1|the Lemma]] $\Rightarrow$ $\mathbb{R}^n_d = \mathbb{R}^n_\rho$.
>
> **Next:** Show product topology = topology induced by $\rho$.
>
> Let $B = (a_1, b_1) \times \cdots \times (a_n, b_n)$ be a basis element in product topology.
>
> Let $x \in B$. For each $x_i$, there exists $\varepsilon_i > 0$ such that $(x_i - \varepsilon_i, x_i + \varepsilon_i) \subseteq (a_i, b_i)$.
>
> Let $\varepsilon = \min_i\{\varepsilon_i\}$. Then $B_\rho(x, \varepsilon) \subseteq B$. $\Rightarrow$ $\rho$-metric is finer than product topology.
>
> Conversely, let $B_\rho(x, \varepsilon)$ be a basis element in $\rho$-topology. $B_\rho(x, \varepsilon) = (x_1 - \varepsilon, x_1 + \varepsilon) \times \cdots \times (x_n - \varepsilon, x_n + \varepsilon)$.
>
> $\Rightarrow$ $B_\rho(x, \varepsilon)$ is open in product topology $\Rightarrow$ done.

^pf-11-2

*Uses:* [[§11 Metric Topology#^lem-11-1|§11.1]], [[§2 Basis for a Topology#^lem-2-2|§2.2]], [[§4 Product Topology#^thm-4-1|§4.1]]

![[m590-11-1.svg]]
*The two inequalities as nested balls in $\mathbb{R}^2$ ($n = 2$): $B_\rho(x, \varepsilon/\sqrt2) \subseteq B_d(x, \varepsilon) \subseteq B_\rho(x, \varepsilon)$, a square (red) inside the disc (blue) inside a square (red). Every ball of one metric contains a ball of the other around the same center, which is exactly what [[§11 Metric Topology#^lem-11-1|Lemma §11.1]] needs in both directions.*

> [!remark]- Connections
> - The same inequality in MATH 451: [[§13 Some Topological Concepts in Metric Spaces#^prop-13-1|Proposition §13.1: Equivalence of the Two Distances]].
> - All norms on a finite-dimensional space are equivalent and so give the same topology: [[§10 New Normed Spaces from Old#^thm-10-3|556 Thm. §10.3]] (equivalent norms: [[§10 New Normed Spaces from Old#^def-10-1|556 Def. §10.1]]).

## Metrizable Spaces

> [!definition] Definition §11.4: Metrizable
> If $X$ is a topological space, $X$ is called **metrizable** if there exists a metric on $X$ that induces the topology of $X$.

^def-11-4

> [!remark] Remark: Why Metrizable Spaces are Special
> Metric spaces occupy a sweet spot: general enough to include most spaces in analysis and geometry, but structured enough to behave well. A metrizable space is automatically:
>
> - **Hausdorff** ([[§11 Metric Topology#^thm-11-4|Theorem §11.4]] below)—distinct points can be separated.
> - **First-countable**—countable neighborhood bases at each point, so sequences suffice for topology ([[§18 Countability Axioms|Section 18]]).
> - **Normal**—disjoint closed sets can be separated by open sets (for metrizable spaces).
>
> A major theme of point-set topology is determining *which* topological spaces are metrizable. The answer—[[§18 Countability Axioms#^thm-18-1|Urysohn's metrization theorem]]—says that a regular, second-countable space is metrizable. This connects the countability axioms ([[§18 Countability Axioms|Section 18]]) and separation axioms ([[§19 Separation Axioms|Section 19]]) to the concrete structure of metric spaces.

^rem-11-1

> [!remark]- Connections
> - Normality is proved in [[§20 Normal Spaces#^thm-20-1|Theorem §20.1: Every Metrizable Space is Normal]].
> - Sequences suffice: [[§11 Metric Topology#^lem-11-8|Sequence Lemma]], [[§11 Metric Topology#^thm-11-9|Theorem §11.9]].

> [!remark] Remark
> $\mathbb{R}^\omega$ is harder to deal with since $d$ and $\rho$ do not always make sense (sums/sup may diverge).

^rem-11-2

> [!theorem] Theorem §11.3: $\mathbb{R}^\omega$ is Metrizable
> Let $\bar{d}(a, b) = \min\{|a - b|, 1\}$ be the standard bounded metric on $\mathbb{R}$.
>
> If $x, y \in \mathbb{R}^\omega$, define $D(x, y) = \sup_i\left\{\frac{\bar{d}(x_i, y_i)}{i}\right\}$.
>
> Then $D$ is a metric that induces the product topology on $\mathbb{R}^\omega$.
>
> (If not divided by $i$, then we have uniform metric, which $\neq$ product topology.)

^thm-11-3

> [!proof]+ Proof
> To be completed.

^pf-11-3

## Metric Spaces and Hausdorff

> [!theorem] Theorem §11.4: Every Metric Space is Hausdorff
> Every metric space is [[§8 Hausdorff Spaces#^def-8-1|Hausdorff]].

^thm-11-4

> [!proof]+ Proof
> If $x, y \in (X, d)$, let $\varepsilon = \frac{d(x,y)}{2}$. Then $B(x, \varepsilon) \cap B(y, \varepsilon) = \emptyset$.
>
> Suppose not: if $z \in B(x, \varepsilon) \cap B(y, \varepsilon)$, then by triangle inequality:
>
> $$
> d(x, y) \leq d(x, z) + d(z, y) < \varepsilon + \varepsilon = 2\varepsilon = d(x,y)
> $$
>
> Contradiction.

^pf-11-4

![[m590-11-3.svg]]
*With $\varepsilon = \tfrac{d(x,y)}{2}$ the two open balls just touch. The midpoint (hollow) is at distance exactly $\varepsilon$ from both centers, so it lies in neither ball, and $B(x,\varepsilon) \cap B(y,\varepsilon) = \varnothing$. This is the triangle-inequality argument drawn out.*

> [!theorem] Corollary §11.5
> Any non-Hausdorff space is not metrizable.

^cor-11-5

*Uses:* [[§11 Metric Topology#^thm-11-4|§11.4]]

> [!theorem] Theorem §11.6: Subspace of Metric Space
> If $A$ is a subset of a metric space $(X, d)$, then the [[§5 Subspace Topology#^def-5-1|subspace topology]] on $A$ equals the metric topology induced by $d|_{A \times A}$.

^thm-11-6

> [!proof]+ Proof
> The key observation is that $\varepsilon$-balls behave well under restriction:
>
> $$
> B_{d|_A}(x, \varepsilon) = \{a \in A : d(x, a) < \varepsilon\} = B_d(x, \varepsilon) \cap A
> $$
>
> $(\subseteq)$ Every basis element $B_{d|_A}(x, \varepsilon)$ of the metric topology on $A$ equals $B_d(x, \varepsilon) \cap A$, which is open in the subspace topology.
>
> $(\supseteq)$ Let $U \cap A$ be a subspace-open set, where $U$ is open in $X$. For any $x \in U \cap A$, there exists $\varepsilon > 0$ such that $B_d(x, \varepsilon) \subseteq U$. Then $B_{d|_A}(x, \varepsilon) = B_d(x, \varepsilon) \cap A \subseteq U \cap A$. So $U \cap A$ is open in the metric topology.

^pf-11-6

*Uses:* [[§5 Subspace Topology#^def-5-1|Def. §5.1]]

> [!remark] Remark: Comparison: Subspace Topology Equals...
> Two important cases where the subspace topology coincides with another natural topology:
>
> | **Setting** | **Condition on $A \subseteq X$** | **Result** |
> |:---:|:---:|:---:|
> | Ordered set $X$ | $A$ convex | Subspace top = Order top |
> | Metric space $(X, d)$ | None needed | Subspace top = Metric top |
>
> The metric case is stronger: no convexity condition is required. This is because $\varepsilon$-balls “restrict nicely” ($B_d(x,\varepsilon) \cap A = B_{d|_A}(x,\varepsilon)$), whereas order intervals may not.
>
> **Counterexample for order topology:** $A = \{0\} \cup (1,2) \subseteq \mathbb{R}$. In subspace topology, $\{0\}$ is open. In order topology on $A$, every open set containing $0$ contains a basis element $[0, b) = \{0\} \cup (1, b)$ with $b \in (1,2)$, so it meets $(1,2)$; hence $\{0\}$ is not open.

^rem-11-3

> [!remark]- Connections
> - Convex case: [[§5 Subspace Topology#^ex-5-2|Example §5.2]] ($[0,1] \subseteq \mathbb{R}$); a non-convex failure: [[§5 Subspace Topology#^ex-5-3|Example §5.3]] ($I \times I$).

## Continuity in Metric Spaces

> [!theorem] Theorem §11.7: $\varepsilon$-$\delta$ Characterization of Continuity
> Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces. Let $f: X \to Y$. Then $f$ is [[§9 Continuous Functions#^def-9-1|continuous]] if and only if for all $x \in X$, $\varepsilon > 0$, there exists $\delta > 0$ such that if $d_X(x, y) < \delta$ then $d_Y(f(x), f(y)) < \varepsilon$.

^thm-11-7

> [!proof]+ Proof
> $(\Rightarrow)$ Suppose $f$ is continuous. Given $x \in X$, $\varepsilon > 0$, find $\delta$.
>
> $f^{-1}(B(f(x), \varepsilon))$ is open in $X$ and contains $x$.
>
> Choose $\delta > 0$ such that $B(x, \delta) \subseteq f^{-1}(B(f(x), \varepsilon))$.
>
> Then $d_X(x, y) < \delta \Rightarrow y \in B(x, \delta) \Rightarrow y \in f^{-1}(B(f(x), \varepsilon)) \Rightarrow f(y) \in B(f(x), \varepsilon) \Rightarrow d_Y(f(x), f(y)) < \varepsilon$.
>
> $(\Leftarrow)$ Suppose the “$\varepsilon$-$\delta$” condition holds. Let $V \subseteq Y$ be open. Let $x \in f^{-1}(V)$.
>
> Since $f(x) \in V$, and $V$ is open, there exists a ball $B(f(x), \varepsilon) \subseteq V$ containing $f(x)$.
>
> By “$\varepsilon$-$\delta$”, there exists $B(x, \delta)$ such that $f(B(x, \delta)) \subseteq B(f(x), \varepsilon)$.
>
> But then $x \in B(x, \delta) \subseteq f^{-1}(B(f(x), \varepsilon)) \subseteq f^{-1}(V)$, hence $f^{-1}(V)$ is open.

^pf-11-7

> [!remark]- Connections
> - MATH 451: [[§17 Continuous Functions#^thm-17-1|Theorem §17.1: The Epsilon-Delta Characterization]] on $\mathbb{R}$, and [[§21 More on Metric Spaces꞉ Continuity#^def-21-1|Definition §21.1: Continuous Maps Between Metric Spaces]], where $\varepsilon$-$\delta$ is the definition.

> [!remark] Remark: Recall: Convergence
> $x_n \to x$ if for every open neighborhood $U$ of $x$, there exists $N$ such that $x_n \in U$ for all $n \geq N$.

^rem-11-4

> [!remark]- Connections
> - Originally [[§7 Interior and Closure#^def-7-4|Definition §7.4: Convergence]].

> [!theorem] Lemma §11.8: Sequence Lemma
> Let $A \subseteq X$. If there exists a sequence of points of $A$ converging to $x$, then $x \in \overline{A}$.
>
> Converse is true if $X$ is metrizable.

^lem-11-8

> [!proof]+ Proof
> $(\Rightarrow)$ $a_n \to x$. Every neighborhood of $x$ contains a point of $A$. Thus $x \in \overline{A}$ ([[Closure Characterization|Closure Characterization]]).
>
> $(\Leftarrow)$ Suppose $X$ is metrizable. Let $x \in \overline{A} = A \cup A'$ (limit points; [[§7 Interior and Closure#^thm-7-4|Theorem §7.4]]).
>
> If $x \in A$, let $a_n = x$ for all $n$. Then $a_n \to x$. (Constant sequence.)
>
> If $x \in A'$ (i.e., $x$ is a limit point of $A$), for each $n \in \mathbb{Z}^+$, choose a point $a_n \in B(x, \frac{1}{n}) \cap A$.
>
> (Such $a_n$ exists because $x$ is a limit point, so every neighborhood of $x$ intersects $A$ in a point other than $x$.)
>
> Then $a_n \to x$: given $\varepsilon > 0$, choose $N$ such that $\frac{1}{N} < \varepsilon$. For $n \geq N$, $d(a_n, x) < \frac{1}{n} \leq \frac{1}{N} < \varepsilon$.

^pf-11-8

*Uses:* [[§7 Interior and Closure#^thm-7-3|§7.3]], [[§7 Interior and Closure#^thm-7-4|§7.4]]

> [!remark]- Connections
> - MATH 451 version: [[§13 Some Topological Concepts in Metric Spaces#^prop-13-6|Proposition §13.6: Sequential Characterization of the Closure]].

> [!theorem] Theorem §11.9: Continuity and Sequences
> If $f: X \to Y$ is continuous, then $x_n \to x$ in $X$ implies $f(x_n) \to f(x)$ in $Y$.
>
> Converse is true if $X$ is metrizable.

^thm-11-9

> [!proof]+ Proof
> $(\Rightarrow)$ $f$ is continuous, $x_n \to x$. Let $V$ be a neighborhood of $f(x)$. Then $f^{-1}(V)$ is an open neighborhood of $x$.
>
> There exists $N$ such that for all $n \geq N$, $x_n \in f^{-1}(V)$. Thus $f(x_n) \in V$. Thus $f(x_n) \to f(x)$.
>
> $(\Leftarrow)$ $X$ metrizable and $x_n \to x$ implies $f(x_n) \to f(x)$. Want to show $f$ is continuous.
>
> [[Equivalent Conditions for Continuity|Suffice to show]] for all $A \subseteq X$, $f(\overline{A}) \subseteq \overline{f(A)}$. By [[§11 Metric Topology#^lem-11-8|Sequence Lemma]], if $x \in \overline{A}$ then there exists a sequence $a_n \to x$, $a_n \in A$, then $f(a_n) \to f(x)$. By [[§11 Metric Topology#^lem-11-8|Sequence Lemma]], $f(x) \in \overline{f(A)}$ since $f(a_n) \in f(A)$.
>
> So $f(\overline{A}) \subseteq \overline{f(A)}$.
>
> (Note that we used the metrizable condition in the Sequence Lemma.)

^pf-11-9

*Uses:* [[§9 Continuous Functions#^thm-9-1|§9.1]], [[§11 Metric Topology#^lem-11-8|§11.8]]

> [!remark]- Connections
> - MATH 451 takes the sequential condition as the definition: [[§17 Continuous Functions#^def-17-1|Definition §17.1: Continuity at a Point — Sequential Definition]].
> - Functional analysis takes the sequential condition as the definition of a continuous linear map ([[§21 Boundedness and Continuity#^def-21-1|556 Def. §21.1]]); for linear maps it is equivalent to boundedness ([[§21 Boundedness and Continuity#^prop-21-2|556 Prop. §21.2]]).
