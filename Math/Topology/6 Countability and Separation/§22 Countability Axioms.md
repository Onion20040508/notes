---
type: section
subject: "[[Topology]]"
chapter: 6
section: 22
munkres: "§30"
tags: [topology, math590]
---
← [[§21 Discrete and Indiscrete Spaces]] · ↑ [[· 6 Countability and Separation]] · [[§23 Separation Axioms]] →

**Motivation:** When does a space $X$ embed in a metric space?

> [!theorem] Theorem §28.1: Urysohn Metrization Theorem (Preview)
> If $X$ is [[§22 Countability Axioms#^def-22-3|second-countable]] and [[§23 Separation Axioms#^def-23-2|regular]] (T3), then $X$ can be embedded in a metric space (hence is [[§12 Metric Topology#^def-12-4|metrizable]]).

^thm-22-1

*Not proved in the course (it needs Urysohn's lemma, [[§24 Normal Spaces#^rem-24-3|not covered]]); see Munkres Theorem 34.1.*

> [!remark]- Connections
> - Announced in [[§12 Metric Topology#^rem-12-1|Why Metrizable Spaces are Special]]; its route through normality is sketched in [[§24 Normal Spaces#^rem-24-3|Not Covered: Urysohn's Lemma and Tietze Extension]].

## First and Second Countability

> [!definition] Definition §28.1: Countable Basis at a Point
> A space $X$ has a **countable basis at $x \in X$** if there is a countable collection $\mathcal{B}$ of neighborhoods of $x$ such that every neighborhood of $x$ contains some $B \in \mathcal{B}$.

^def-22-1

> [!definition] Definition §28.2: First-Countable
> $X$ is **first-countable** if $X$ has a [[§22 Countability Axioms#^def-22-1|countable basis]] at each of its points.

^def-22-2

> [!remark] Remark: Why First-Countability Matters
> First-countability means the local neighborhood structure around each point is “countably describable.” This has important consequences:
>
> **1. Sequences suffice for topology.** In a first-countable space:
> - $x \in \overline{A}$ iff there exists a sequence in $A$ converging to $x$.
> - $f$ is continuous at $x$ iff $x_n \to x$ implies $f(x_n) \to f(x)$.
>
> This is why first-countability makes “analysis-style” sequential arguments work in general topology.
>
> **2. Nested bases exist.** Given a countable basis $\{B_1, B_2, \ldots\}$ at $x$, define $U_n = B_1 \cap \cdots \cap B_n$. Then $\{U_n\}$ is a nested countable basis: $U_1 \supseteq U_2 \supseteq \cdots$, analogous to $\{B(x, 1/n)\}$ in metric spaces.
>
> **3. Not every space is first-countable.** The uncountable product $\mathbb{R}^{\mathbb{R}}$ with [[§11 Product Topology on Arbitrary Products#^def-11-1|product topology]] is not first-countable — any neighborhood basis at a point requires uncountably many sets. In such spaces, sequences are inadequate; one needs nets or filters.
>
> **Summary:** First-countable = “locally countably describable” = “sequences work.”

^rem-22-1

> [!remark]- Connections
> - Metric-space versions of point 1: [[§12 Metric Topology#^lem-12-8|Sequence Lemma]] and [[§12 Metric Topology#^thm-12-9|Continuity and Sequences]].

> [!example] Example §22.1
> If $(X, d)$ is a metric space, then $\mathcal{B} = \{B_d(x, 1/n) \mid n \in \mathbb{Z}_+\}$ is a countable basis at $x$.
>
> Thus every metric space is first-countable.

^ex-22-1

> [!example] Example §22.2
> $\mathbb{R}_\ell$ ([[§2 Basis for a Topology#^ex-2-3|lower limit topology]]) is first-countable. Given $x \in \mathbb{R}_\ell$, $\mathcal{B} = \{[x, x + 1/n) \mid n \in \mathbb{Z}_+\}$ is a countable basis at $x$.

^ex-22-2

> [!definition] Definition §28.3: Second-Countable
> $X$ is **second-countable** if $X$ has a countable [[§2 Basis for a Topology#^def-2-1|basis]] for its topology.

^def-22-3

> [!remark] Remark
> Second-countable $\Rightarrow$ first-countable.
>
> *Proof:* If $\mathcal{B}$ is a countable basis for $X$, then for any $x \in X$, $\mathcal{B}_x = \{B \in \mathcal{B} \mid x \in B\}$ is a countable basis at $x$.

^rem-22-2

> [!remark]- Connections
> - One of the three axioms of a topological manifold, [[§2 Topological Manifolds#^def-2-2|591 Def. §2.2]]; for manifolds it forces countably many components, [[§2 Topological Manifolds#^prop-2-6|591 Prop. §2.6]].

> [!example] Example §22.3
> $\mathbb{R}$ is second-countable. $\mathcal{B} = \{(a, b) \mid a, b \in \mathbb{Q}\}$ is a countable basis (it is indexed by pairs in $\mathbb{Q} \times \mathbb{Q}$, which is countable: [[The Rationals Are Denumerable|250 Thm. §14.10]], [[§14 Counting Infinite Sets#^prop-14-8|250 Prop. §14.8]]).

^ex-22-3

> [!example] Example §22.4
> $\mathbb{R}^n$ is second-countable. $\mathcal{B} = \{\prod_{i=1}^{n}(a_i, b_i) \mid a_i, b_i \in \mathbb{Q}\}$ is a countable basis (indexed by $\mathbb{Q}^{2n}$, countable by [[§14 Counting Infinite Sets#^cor-14-9|250 Cor. §14.9]]).

^ex-22-4

> [!example] Example §22.5
> $\mathbb{R}^\omega$ (with [[§11 Product Topology on Arbitrary Products#^def-11-1|product topology]]) is second-countable.
>
> $$
> \mathcal{B} = \left\{\prod_{i \in \mathbb{Z}_+} U_i \,\middle|\, U_i = (a_i, b_i) \text{ with } a_i, b_i \in \mathbb{Q} \text{ for finitely many } i, \text{ and } U_i = \mathbb{R} \text{ otherwise}\right\}
> $$
>
> This is countable (countable choice of which finitely many coordinates to restrict, and countable choice of rational endpoints for each).

^ex-22-5

## First-Countable Does Not Imply Second-Countable

> [!remark] Remark
> First-countable $\not\Rightarrow$ second-countable. There exist metric spaces that are not second-countable.

^rem-22-3

> [!example] Example §22.6: $\mathbb{R}^\omega$ with Uniform Metric
> $(\mathbb{R}^\omega, \bar{\rho})$ where $\bar{\rho}(\bar{x}, \bar{y}) = \sup\{\min(d(x_i, y_i), 1)\}$ is first-countable (it's a metric space) but not second-countable.
>
> *Proof that it's not second-countable:*
>
> Consider $\{0, 1\}^\omega \subseteq \mathbb{R}^\omega$ (sequences of 0s and 1s). This has the [[§1 Topological Spaces#^ex-1-3|discrete topology]] under $\bar{\rho}$: if $\bar{a} \neq \bar{b}$, then $\bar{\rho}(\bar{a}, \bar{b}) = 1$, so $B_{\bar{\rho}}(\bar{a}, 1/2) = \{\bar{a}\}$.
>
> $\{0, 1\}^\omega$ is uncountable: sending a sequence to the set of indices where it equals $1$ is a bijection onto the power set of $\mathbb{Z}_+$, which is uncountable by [[§14a Uncountable Sets#^thm-14a-3|Cantor's theorem]] (250 Thm. §14a.3). By [[§22 Countability Axioms#^lem-22-2|the lemma below]], any space with a countable basis cannot have an uncountable discrete subspace.

^ex-22-6

> [!theorem] Lemma §28.2
> If $X$ has a countable basis and $A$ is a discrete subspace of $X$, then $A$ must be countable.

^lem-22-2

> [!proof]+ Proof
> Let $\mathcal{B}$ be a countable basis for $X$. For each $a \in A$, since $A$ is discrete, $\{a\}$ is open in $A$, so $\{a\} = U \cap A$ for some open $U$ in $X$.
>
> There exists $B_a \in \mathcal{B}$ such that $a \in B_a \subseteq U$, hence $B_a \cap A = \{a\}$.
>
> If $a \neq b$ in $A$, then $B_a \neq B_b$ (since $B_a \cap A = \{a\} \neq \{b\} = B_b \cap A$).
>
> The map $a \mapsto B_a$ is an injection $A \to \mathcal{B}$. Since $\mathcal{B}$ is countable, $A$ is countable (compose with an injection $\mathcal{B} \to \mathbb{Z}_+$ and apply [[§14 Counting Infinite Sets#^cor-14-6|250 Cor. §14.6]]).

^pf-22-2

*Uses:* [[§5 Subspace Topology#^def-5-1|Def. §5.1]], [[§2 Basis for a Topology#^def-2-1|Def. §2.1]], [[§14 Counting Infinite Sets#^cor-14-6|250 §14.6]]

> [!remark]- Connections
> - The same counting in normed spaces: orthonormal vectors are at mutual distance √2, so an orthonormal set in a separable space is countable ([[§32 Position Eigenstates and Continuous Resolutions#^prop-32-1|556 Prop. §32.1]]).
> - The same argument shows L^∞ is not separable: the indicators of (0, t) form an uncountable family at mutual distance 1, [[§35 Lᵖ as a Banach Space#^thm-35-14|551 Thm. §35.14]].

## Inheritance Properties

> [!theorem] Theorem §28.3: Subspaces and Products
> 1. If $A \subseteq X$ and $X$ is first-countable (resp. second-countable), then $A$ is first-countable (resp. second-countable).
> 2. A countable product of first-countable (resp. second-countable) spaces is first-countable (resp. second-countable).

^thm-22-3

> [!proof]+ Proof for Second-Countable
> **(1) Subspaces:** If $\mathcal{B}$ is a countable basis for $X$, then $\{B \cap A \mid B \in \mathcal{B}\}$ is a countable basis for $A$.
>
> **(2) Countable products:** Let $\mathcal{B}_i$ be a countable basis for $X_i$. Then
>
> $$
> \mathcal{B} = \left\{\prod_{i} U_i \,\middle|\, U_i = B_i \in \mathcal{B}_i \text{ for finitely many } i, \text{ and } U_i = X_i \text{ otherwise}\right\}
> $$
>
> is a countable basis for $\prod X_i$.

^pf-22-3

*Uses:* [[§5 Subspace Topology#^lem-5-1|§5.1]], [[§11 Product Topology on Arbitrary Products#^def-11-1|Def. §11.1]]

*The first-countable case is the same argument with countable bases at a point; see Munkres Theorem 30.2.*

## Dense Subsets and Lindelöf Spaces

> [!definition] Definition §28.4: Dense
> A subset $A \subseteq X$ is **dense** if $\overline{A} = X$. Equivalently: every nonempty open set in $X$ meets $A$.

^def-22-4

> [!remark]- Connections
> - The equivalence is the [[Closure Characterization|Closure Characterization]] applied at every point.

> [!example] Example §22.7
> $\mathbb{Q}$ is dense in $\mathbb{R}$: every open interval $(a, b)$ contains a rational number ([[§4 The Completeness Axiom#^thm-4-7|Density of ℚ in ℝ]]), so $\overline{\mathbb{Q}} = \mathbb{R}$.

^ex-22-7

> [!definition] Definition §28.5: Separable
> $X$ is **separable** if it has a countable [[§22 Countability Axioms#^def-22-4|dense]] subset: there exists a countable $D \subseteq X$ with $\overline{D} = X$.

^def-22-5

> [!remark]- Connections
> - Separability of sequence and function spaces: [[§24 Orthonormal Sets and Bases#^def-24-5|556 Def. §24.5]], with ℓᵖ and Lᵖ separable for p < ∞ and ℓ^∞, L^∞ not ([[§25 Sequence and Function Spaces#^prop-25-1|556 Prop. §25.1]]–[[§25 Sequence and Function Spaces#^prop-25-5|556 Prop. §25.5]]).
> - The metric-space form, with density by sequences: [[§35 Lᵖ as a Banach Space#^def-35-5|551 Def. §35.5]]; Lᵖ is separable for p < ∞ ([[§35 Lᵖ as a Banach Space#^cor-35-13|551 Cor. §35.13]]) and L^∞ is not ([[§35 Lᵖ as a Banach Space#^thm-35-14|551 Thm. §35.14]]).

> [!example] Example §22.8: Standard Examples
> 1. $\mathbb{R}$ is separable: $D = \mathbb{Q}$.
> 2. $\mathbb{R}^n$ is separable: $D = \mathbb{Q}^n$.
> 3. $\mathbb{R}_\ell$ ([[§2 Basis for a Topology#^ex-2-3|lower limit topology]]) is separable: $D = \mathbb{Q}$. Every $[a, b)$ contains a rational.

^ex-22-8

> [!theorem] Proposition §28.4: Relationships Between Countability and Separability
> 1. Second countable $\Rightarrow$ separable (pick one point from each basis element).
> 2. Separable does NOT imply second countable in general ($\mathbb{R}_\ell$ is separable but not second countable).
> 3. In [[§12 Metric Topology#^def-12-4|metrizable]] spaces: separable $\iff$ second countable.

^prop-22-4

> [!proof]+ Proof
> **(1)** is part (a) of [[§22 Countability Axioms#^thm-22-6|the theorem below]].
>
> **(2)** $\mathbb{R}_\ell$ is separable ($\mathbb{Q}$ is dense). To see it is not second countable: suppose $\{B_n\}$ were a countable basis. For each $x \in \mathbb{R}$, the set $[x, x+1)$ is open, so some $B_{n_x}$ satisfies $x \in B_{n_x} \subseteq [x, x+1)$. Then $\inf B_{n_x} = x$, so different $x$'s give different $B_{n_x}$'s. But there are uncountably many $x$'s and only countably many $B_n$'s — contradiction.
>
> **(3)** $(\Rightarrow)$: Let $D = \{d_1, d_2, \ldots\}$ be a countable dense subset of a metric space $(X, d)$. The collection $\{B(d_i, 1/n) \mid i \in \mathbb{Z}_+, n \in \mathbb{Z}_+\}$ is countable. It is a basis: given $x \in U$ open, choose $\varepsilon > 0$ with $B(x, \varepsilon) \subseteq U$. Choose $n$ with $1/n < \varepsilon/2$, then pick $d_i \in D$ with $d(x, d_i) < 1/n$ (density). Then $x \in B(d_i, 1/n)$, and every $y \in B(d_i, 1/n)$ has $d(y, x) \leq d(y, d_i) + d(d_i, x) < 2/n < \varepsilon$, so $B(d_i, 1/n) \subseteq B(x, \varepsilon) \subseteq U$.
>
> $(\Leftarrow)$: follows from (1).

^pf-22-4

*Uses:* [[§22 Countability Axioms#^thm-22-6|§22.6]]

![[m590-18-1.svg]]
*Proof of (3), separable $\Rightarrow$ second countable: given $x\in U$, pick $B(x,\varepsilon)\subseteq U$ (dashed), $\frac1n<\varepsilon/2$, and a point $d_i$ of the dense set $D$ (blue) with $d(x,d_i)<\frac1n$. The basis ball $B(d_i,\frac1n)$ (red) contains $x$ and fits inside $B(x,\varepsilon)$ by the triangle inequality. Only countably many such balls exist.*

> [!theorem] Proposition §28.5: Subspaces of Separable Metrizable Spaces
> If $X$ is separable and [[§12 Metric Topology#^def-12-4|metrizable]], then every subspace $A \subseteq X$ is separable.

^prop-22-5

> [!proof]+ Proof
> $X$ separable and metrizable $\Rightarrow$ $X$ second countable (by [[§22 Countability Axioms#^prop-22-4|the proposition above]]). [[§22 Countability Axioms#^thm-22-3|Subspace of second countable is second countable]] (restrict basis elements via $B_n \cap A$). Second countable $\Rightarrow$ separable ([[§22 Countability Axioms#^prop-22-4|§22.4]] (1)).

^pf-22-5

*Uses:* [[§22 Countability Axioms#^prop-22-4|§22.4]], [[§22 Countability Axioms#^thm-22-3|§22.3]]

> [!definition] Definition §28.6: Lindelöf Space
> $X$ is a **Lindelöf space** if every open cover of $X$ contains a countable subcover.

^def-22-6

> [!remark] Remark
> [[§18 Compact Spaces#^def-18-2|Compact]] $\Rightarrow$ Lindelöf (finite subcover is countable).

^rem-22-4

> [!theorem] Theorem §28.6: Second-Countable Implies Dense Subset and Lindelöf
> Suppose $X$ has a countable basis. Then:
> - **(a)** There exists a countable subset of $X$ that is dense in $X$.
> - **(b)** Every open cover of $X$ has a countable subcover (i.e., $X$ is [[§22 Countability Axioms#^def-22-6|Lindelöf]]).

^thm-22-6

> [!proof]+ Proof
> Let $\{B_n\}_{n \in \mathbb{Z}_+}$ be a countable basis for $X$.
>
> **(a)** Choose $x_n \in B_n$ for each $n$. Let $D = \{x_n\} \subseteq X$.
>
> Given $x \in X$, every basis element containing $x$ intersects $D$ (since $x \in B_n$ implies $x_n \in B_n \cap D$). Thus $x \in \overline{D}$, so $D$ is dense.
>
> **(b)** Let $\mathcal{A}$ be an open cover of $X$.
>
> For each $n \in \mathbb{Z}_+$, choose $A_n \in \mathcal{A}$ such that $B_n \subseteq A_n$ (if such $A_n$ exists). This defines $A_n$ for a countable subset $J \subseteq \mathbb{Z}_+$.
>
> Let $\mathcal{A}' = \{A_n \mid n \in J\}$, a countable subcollection of $\mathcal{A}$.
>
> **Claim:** $\mathcal{A}'$ covers $X$.
>
> Given $x \in X$, choose $A \in \mathcal{A}$ such that $x \in A$. Since $A$ is open, there exists a basis element $B_n$ such that $x \in B_n \subseteq A$. Then $A_n$ is defined and $B_n \subseteq A_n$, so $x \in A_n \in \mathcal{A}'$.

^pf-22-6

*Uses:* [[§8 Interior and Closure#^thm-8-3|§8.3]], [[§22 Countability Axioms#^def-22-4|Def. §22.4]]

> [!remark]- Connections
> - For subsets of ℝⁿ, 551 proves the countable subcover of (b) directly: [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-3|551 Thm. §6.3]], using the countable basis of rational balls built in [[§6 Open Covers and the Heine–Borel Theorem#^lem-6-2|551 Lemma §6.2]].
