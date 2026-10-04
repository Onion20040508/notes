---
type: section
subject: "[[Topology]]"
chapter: 6
section: 18
munkres: "§30"
tags: [topology, math590]
---
← [[§17 Local Compactness]] · ↑ [[· 6 Countability and Separation]] · [[§19 Separation Axioms]] →

**Motivation:** When does a space $X$ embed in a metric space?

> [!theorem] Theorem §18.1: Urysohn Metrization Theorem (Preview)
> If $X$ is [[§18 Countability Axioms#^def-18-3|second-countable]] and [[§19 Separation Axioms#^def-19-2|regular]] (T3), then $X$ can be embedded in a metric space (hence is [[§11 Metric Topology#^def-11-4|metrizable]]).

^thm-18-1

> [!remark]- Connections
> - Announced in [[§11 Metric Topology#^rem-11-1|Why Metrizable Spaces are Special]]; its route through normality is sketched in [[§20 Normal Spaces#^rem-20-3|Not Covered: Urysohn's Lemma and Tietze Extension]].

## First and Second Countability

> [!definition] Definition §18.1: Countable Basis at a Point
> A space $X$ has a **countable basis at $x \in X$** if there is a countable collection $\mathcal{B}$ of neighborhoods of $x$ such that every neighborhood of $x$ contains some $B \in \mathcal{B}$.

^def-18-1

> [!definition] Definition §18.2: First-Countable
> $X$ is **first-countable** if $X$ has a [[§18 Countability Axioms#^def-18-1|countable basis]] at each of its points.

^def-18-2

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
> **3. Not every space is first-countable.** The uncountable product $\mathbb{R}^{\mathbb{R}}$ with [[§10 Product Topology on Arbitrary Products#^def-10-1|product topology]] is not first-countable — any neighborhood basis at a point requires uncountably many sets. In such spaces, sequences are inadequate; one needs nets or filters.
>
> **Summary:** First-countable = “locally countably describable” = “sequences work.”

^rem-18-1

> [!remark]- Connections
> - Metric-space versions of point 1: [[§11 Metric Topology#^lem-11-8|Sequence Lemma]] and [[§11 Metric Topology#^thm-11-9|Continuity and Sequences]].

> [!example] Example §18.1
> If $(X, d)$ is a metric space, then $\mathcal{B} = \{B_d(x, 1/n) \mid n \in \mathbb{Z}_+\}$ is a countable basis at $x$.
>
> Thus every metric space is first-countable.

^ex-18-1

> [!example] Example §18.2
> $\mathbb{R}_\ell$ ([[§2 Basis for a Topology#^ex-2-3|lower limit topology]]) is first-countable. Given $x \in \mathbb{R}_\ell$, $\mathcal{B} = \{[x, x + 1/n) \mid n \in \mathbb{Z}_+\}$ is a countable basis at $x$.

^ex-18-2

> [!definition] Definition §18.3: Second-Countable
> $X$ is **second-countable** if $X$ has a countable [[§2 Basis for a Topology#^def-2-1|basis]] for its topology.

^def-18-3

> [!remark] Remark
> Second-countable $\Rightarrow$ first-countable.
>
> *Proof:* If $\mathcal{B}$ is a countable basis for $X$, then for any $x \in X$, $\mathcal{B}_x = \{B \in \mathcal{B} \mid x \in B\}$ is a countable basis at $x$.

^rem-18-2

> [!remark]- Connections
> - One of the three axioms of a topological manifold, [[§2 Topological Manifolds#^def-2-2|591 Def. §2.2]]; for manifolds it forces countably many components, [[§2 Topological Manifolds#^prop-2-6|591 Prop. §2.6]].

> [!example] Example §18.3
> $\mathbb{R}$ is second-countable. $\mathcal{B} = \{(a, b) \mid a, b \in \mathbb{Q}\}$ is a countable basis.

^ex-18-3

> [!example] Example §18.4
> $\mathbb{R}^n$ is second-countable. $\mathcal{B} = \{\prod_{i=1}^{n}(a_i, b_i) \mid a_i, b_i \in \mathbb{Q}\}$ is a countable basis.

^ex-18-4

> [!example] Example §18.5
> $\mathbb{R}^\omega$ (with [[§10 Product Topology on Arbitrary Products#^def-10-1|product topology]]) is second-countable.
>
> $$
> \mathcal{B} = \left\{\prod_{i \in \mathbb{Z}_+} U_i \,\middle|\, U_i = (a_i, b_i) \text{ with } a_i, b_i \in \mathbb{Q} \text{ for finitely many } i, \text{ and } U_i = \mathbb{R} \text{ otherwise}\right\}
> $$
>
> This is countable (countable choice of which finitely many coordinates to restrict, and countable choice of rational endpoints for each).

^ex-18-5

## First-Countable Does Not Imply Second-Countable

> [!remark] Remark
> First-countable $\not\Rightarrow$ second-countable. There exist metric spaces that are not second-countable.

^rem-18-3

> [!example] Example §18.6: $\mathbb{R}^\omega$ with Uniform Metric
> $(\mathbb{R}^\omega, \bar{\rho})$ where $\bar{\rho}(\bar{x}, \bar{y}) = \sup\{\min(d(x_i, y_i), 1)\}$ is first-countable (it's a metric space) but not second-countable.
>
> *Proof that it's not second-countable:*
>
> Consider $\{0, 1\}^\omega \subseteq \mathbb{R}^\omega$ (sequences of 0s and 1s). This has the [[§1 Topological Spaces#^ex-1-3|discrete topology]] under $\bar{\rho}$: if $\bar{a} \neq \bar{b}$, then $\bar{\rho}(\bar{a}, \bar{b}) = 1$, so $B_{\bar{\rho}}(\bar{a}, 1/2) = \{\bar{a}\}$.
>
> $\{0, 1\}^\omega$ is uncountable. By [[§18 Countability Axioms#^lem-18-2|the lemma below]], any space with a countable basis cannot have an uncountable discrete subspace.

^ex-18-6

> [!theorem] Lemma §18.2
> If $X$ has a countable basis and $A$ is a discrete subspace of $X$, then $A$ must be countable.

^lem-18-2

> [!proof]+ Proof
> Let $\mathcal{B}$ be a countable basis for $X$. For each $a \in A$, since $A$ is discrete, $\{a\}$ is open in $A$, so $\{a\} = U \cap A$ for some open $U$ in $X$.
>
> There exists $B_a \in \mathcal{B}$ such that $a \in B_a \subseteq U$, hence $B_a \cap A = \{a\}$.
>
> If $a \neq b$ in $A$, then $B_a \neq B_b$ (since $B_a \cap A = \{a\} \neq \{b\} = B_b \cap A$).
>
> The map $a \mapsto B_a$ is an injection $A \to \mathcal{B}$. Since $\mathcal{B}$ is countable, $A$ is countable.

^pf-18-2

*Uses:* [[§5 Subspace Topology#^def-5-1|Def. §5.1]], [[§2 Basis for a Topology#^def-2-1|Def. §2.1]]

> [!remark]- Connections
> - The same counting in normed spaces: orthonormal vectors are at mutual distance √2, so an orthonormal set in a separable space is countable ([[§32 Position Eigenstates and Continuous Resolutions#^prop-32-1|556 Prop. §32.1]]).
> - The same argument shows L^∞ is not separable: the indicators of (0, t) form an uncountable family at mutual distance 1, [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-21|551 Thm. §19.21]].

## Inheritance Properties

> [!theorem] Theorem §18.3: Subspaces and Products
> 1. If $A \subseteq X$ and $X$ is first-countable (resp. second-countable), then $A$ is first-countable (resp. second-countable).
> 2. A countable product of first-countable (resp. second-countable) spaces is first-countable (resp. second-countable).

^thm-18-3

> [!proof]+ Proof for second-countable
> **(1) Subspaces:** If $\mathcal{B}$ is a countable basis for $X$, then $\{B \cap A \mid B \in \mathcal{B}\}$ is a countable basis for $A$.
>
> **(2) Countable products:** Let $\mathcal{B}_i$ be a countable basis for $X_i$. Then
>
> $$
> \mathcal{B} = \left\{\prod_{i} U_i \,\middle|\, U_i = B_i \in \mathcal{B}_i \text{ for finitely many } i, \text{ and } U_i = X_i \text{ otherwise}\right\}
> $$
>
> is a countable basis for $\prod X_i$.

^pf-18-3

*Uses:* [[§5 Subspace Topology#^lem-5-1|§5.1]], [[§10 Product Topology on Arbitrary Products#^def-10-1|Def. §10.1]]

## Dense Subsets and Lindelöf Spaces

> [!definition] Definition §18.4: Dense
> A subset $A \subseteq X$ is **dense** if $\overline{A} = X$. Equivalently: every nonempty open set in $X$ meets $A$.

^def-18-4

> [!remark]- Connections
> - The equivalence is the [[Closure Characterization|Closure Characterization]] applied at every point.

> [!example] Example §18.7
> $\mathbb{Q}$ is dense in $\mathbb{R}$: every open interval $(a, b)$ contains a rational number ([[§4 The Completeness Axiom#^thm-4-7|Density of ℚ in ℝ]]), so $\overline{\mathbb{Q}} = \mathbb{R}$.

^ex-18-7

> [!definition] Definition §18.5: Separable
> $X$ is **separable** if it has a countable [[§18 Countability Axioms#^def-18-4|dense]] subset: there exists a countable $D \subseteq X$ with $\overline{D} = X$.

^def-18-5

> [!remark]- Connections
> - Separability of sequence and function spaces: [[§24 Orthonormal Sets and Bases#^def-24-5|556 Def. §24.5]], with ℓᵖ and Lᵖ separable for p < ∞ and ℓ^∞, L^∞ not ([[§25 Sequence and Function Spaces#^prop-25-1|556 Prop. §25.1]]–[[§25 Sequence and Function Spaces#^prop-25-5|556 Prop. §25.5]]).
> - The metric-space form, with density by sequences: [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-9|551 Def. §19.9]]; Lᵖ is separable for p < ∞ ([[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-20|551 Cor. §19.20]]) and L^∞ is not ([[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-21|551 Thm. §19.21]]).

> [!example] Example §18.8: Standard Examples
> 1. $\mathbb{R}$ is separable: $D = \mathbb{Q}$.
> 2. $\mathbb{R}^n$ is separable: $D = \mathbb{Q}^n$.
> 3. $\mathbb{R}_l$ ([[§2 Basis for a Topology#^ex-2-3|lower limit topology]]) is separable: $D = \mathbb{Q}$. Every $[a, b)$ contains a rational.

^ex-18-8

> [!theorem] Proposition §18.4: Relationships Between Countability and Separability
> 1. Second countable $\Rightarrow$ separable (pick one point from each basis element).
> 2. Separable does NOT imply second countable in general ($\mathbb{R}_l$ is separable but not second countable).
> 3. In metrizable spaces: separable $\iff$ second countable.

^prop-18-4

> [!proof]+ Proof
> **(1)** is part (a) of [[§18 Countability Axioms#^thm-18-6|the theorem below]].
>
> **(2)** $\mathbb{R}_l$ is separable ($\mathbb{Q}$ is dense). To see it is not second countable: suppose $\{B_n\}$ were a countable basis. For each $x \in \mathbb{R}$, the set $[x, x+1)$ is open, so some $B_{n_x}$ satisfies $x \in B_{n_x} \subseteq [x, x+1)$. Then $\inf B_{n_x} = x$, so different $x$'s give different $B_{n_x}$'s. But there are uncountably many $x$'s and only countably many $B_n$'s — contradiction.
>
> **(3)** $(\Rightarrow)$: Let $D = \{d_1, d_2, \ldots\}$ be a countable dense subset of a metric space $(X, d)$. The collection $\{B(d_i, 1/n) \mid i \in \mathbb{Z}_+, n \in \mathbb{Z}_+\}$ is countable. It is a basis: given $x \in U$ open, choose $\varepsilon > 0$ with $B(x, \varepsilon) \subseteq U$. Pick $d_i \in D$ with $d(x, d_i) < \varepsilon/2$ (density), and $n$ with $1/n < \varepsilon/2$. Then $x \in B(d_i, 1/n) \subseteq B(x, \varepsilon) \subseteq U$.
>
> $(\Leftarrow)$: follows from (1).

^pf-18-4

*Uses:* [[§18 Countability Axioms#^thm-18-6|§18.6]]

![[m590-18-1.svg]]
*Proof of (3), separable $\Rightarrow$ second countable: given $x\in U$, pick $B(x,\varepsilon)\subseteq U$ (dashed), a point $d_i$ of the dense set $D$ (blue) with $d(x,d_i)<\varepsilon/2$, and $\frac1n<\varepsilon/2$. The basis ball $B(d_i,\frac1n)$ (red) contains $x$ and fits inside $B(x,\varepsilon)$ by the triangle inequality. Only countably many such balls exist.*

> [!theorem] Proposition §18.5: Subspaces of Separable Metrizable Spaces
> If $X$ is separable and metrizable, then every subspace $A \subseteq X$ is separable.

^prop-18-5

> [!proof]+ Proof
> $X$ separable and metrizable $\Rightarrow$ $X$ second countable (by [[§18 Countability Axioms#^prop-18-4|the proposition above]]). [[§18 Countability Axioms#^thm-18-3|Subspace of second countable is second countable]] (restrict basis elements via $B_n \cap A$). Second countable $\Rightarrow$ separable ([[§18 Countability Axioms#^prop-18-4|§18.4]] (1)).

^pf-18-5

*Uses:* [[§18 Countability Axioms#^prop-18-4|§18.4]], [[§18 Countability Axioms#^thm-18-3|§18.3]]

> [!definition] Definition §18.6: Lindelöf Space
> $X$ is a **Lindelöf space** if every open cover of $X$ contains a countable subcover.

^def-18-6

> [!remark] Remark
> [[§15 Compact Spaces#^def-15-2|Compact]] $\Rightarrow$ Lindelöf (finite subcover is countable).

^rem-18-4

> [!theorem] Theorem §18.6: Second-Countable Implies Dense Subset and Lindelöf
> Suppose $X$ has a countable basis. Then:
> - **(a)** There exists a countable subset of $X$ that is dense in $X$.
> - **(b)** Every open cover of $X$ has a countable subcover (i.e., $X$ is [[§18 Countability Axioms#^def-18-6|Lindelöf]]).

^thm-18-6

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

^pf-18-6

*Uses:* [[§7 Interior and Closure#^thm-7-3|§7.3]], [[§18 Countability Axioms#^def-18-4|Def. §18.4]]

> [!remark]- Connections
> - For subsets of ℝⁿ, 551 proves the countable subcover of (b) directly: [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-1|551 Thm. §6.1]], using the countable basis of rational balls built in [[§6 Open Covers and the Heine–Borel Theorem#^lem-6-3|551 Lemma §6.3]].
