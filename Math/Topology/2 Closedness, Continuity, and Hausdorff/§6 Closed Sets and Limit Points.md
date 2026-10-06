---
type: section
subject: "[[Topology]]"
chapter: 2
section: 6
munkres: "§17"
tags: [topology, math590]
---
← [[§5a Discrete, Indiscrete, Lower Limit and K-Topologies]] · ↑ [[· 2 Closedness, Continuity, and Hausdorff]] · [[§7 Interior and Closure]] →

## Closed Sets

> [!definition] Definition §6.1: Closed Set
> A subset $A \subseteq X$ is **closed** if $X \setminus A$ is open.

^def-6-1

> [!remark]- Connections
> - MATH 451 version: [[§13 Some Topological Concepts in Metric Spaces#^def-13-5|Open and Closed Subsets]] of a metric space.
> - The sequential definition in ℝⁿ, with this one as its equivalent form: [[§5 Topology of ℝⁿ#^def-5-3|551 Def. §5.3]].
> - The sequential definition in a normed space: [[§10 Normed Linear Spaces#^def-10-6|556 Def. §10.6]]; it agrees with this one in metric spaces by [[§7 Interior and Closure#^cor-7-5|Cor. §7.5]] and the [[§11 Metric Topology#^lem-11-8|Sequence Lemma]].

> [!example] Example §6.1
> $[a, b] \subseteq \mathbb{R}$ is closed.

^ex-6-1

> [!example] Example §6.2
> $\{x \times y \in \mathbb{R}^2 \mid x \leq 0 \text{ and } y \leq 0\} \subseteq \mathbb{R}^2$ is closed.
>
> Its complement is the union of two open sets: $\mathbb{R} \times (0, \infty) \cup (0, \infty) \times \mathbb{R}$.

^ex-6-2

![[m590-6-1.svg]]
*The closed quadrant $\{x\le 0,\ y\le 0\}$ (blue, including its two boundary rays) and its complement: the union of the open half-planes $\mathbb{R}\times(0,\infty)$ and $(0,\infty)\times\mathbb{R}$ (red hatching, crossed where the two overlap).*

> [!example] Example §6.3
> In the [[§1 Topological Spaces#^ex-1-3|discrete topology]] on a set $X$, every set $X \setminus A$ is open $\Rightarrow$ every subset $A \subseteq X$ is closed.

^ex-6-3

*Chain: earlier in [[§5a Discrete, Indiscrete, Lower Limit and K-Topologies|Chapter 1]] · later in [[§12a ℝ^ω, Discrete Spaces and the Torus|Chapter 3]] · [[Discrete and indiscrete topologies|all appearances]]*

> [!example] Example §6.4
> $Y = [0,1] \cup (2,3) \subseteq \mathbb{R}$ with [[§5 Subspace Topology#^def-5-1|subspace topology]].
>
> $[0,1]$ is closed in $Y$ since its complement $(2,3)$ is open in $Y$.
>
> $(2,3)$: $(-1, 2) \cap Y = [0,1]$ is open in $Y$, so $(2,3)$ is closed.

^ex-6-4

> [!theorem] Theorem §6.1: Properties of Closed Sets
> Let $X$ be a topological space.
> 1. $\emptyset$ and $X$ are closed.
> 2. Arbitrary intersections of closed sets are closed. (If $Z_\alpha$ is closed for each $\alpha \in A$, then $\bigcap_{\alpha \in A} Z_\alpha$ is closed.)
> 3. Finite unions of closed sets are closed. (If $Z_1, \ldots, Z_n$ are closed, then $Z_1 \cup \cdots \cup Z_n$ is closed.)

^thm-6-1

> [!proof]+ Proof
> 1. $X \setminus X = \emptyset$ is open, $X \setminus \emptyset = X$ is open.
> 2. $\bigcap_{\alpha \in A} Z_\alpha = \bigcap_{\alpha} (X \setminus U_\alpha) = X \setminus \left(\bigcup_{\alpha \in A} U_\alpha\right)$ is closed, where $U_\alpha = X \setminus Z_\alpha$ is open.
> 3. $Z_1 \cup \cdots \cup Z_n = X \setminus \left(\bigcap_{i=1}^n (X \setminus Z_i)\right)$. Since each $X \setminus Z_i$ is open, and finite intersections of open sets are open, the complement is closed.

^pf-6-1

> [!remark]- Connections
> - Dual of the axioms in [[§1 Topological Spaces#^def-1-1|Definition §1.1]]; MATH 451 version: [[§13 Some Topological Concepts in Metric Spaces#^prop-13-4|Unions of Open Sets]].

## Closed Sets in Subspaces

> [!theorem] Theorem §6.2: Closed Sets in Subspaces
> Let $Y \subseteq X$ (subspace). Then $A \subseteq Y$ is closed in $Y$ if and only if $A$ equals the intersection of a closed set of $X$ with $Y$.

^thm-6-2

> [!proof]+ Proof
> $(\Leftarrow)$ Suppose $A = C \cap Y$, where $C$ is closed in $X$. Then $Y \setminus A = Y \setminus (C \cap Y) = (X \setminus C) \cap Y$, which is open in $Y$. Hence $A$ is closed in $Y$.
>
> $(\Rightarrow)$ Suppose $A$ is closed in $Y$. Then $Y \setminus A$ is open in $Y$, so $Y \setminus A = Y \cap U$ for some $U$ open in $X$. Now:
>
> $$
> A = Y \setminus (Y \setminus A) = Y \setminus (Y \cap U) = Y \cap (Y \cap U)^c = Y \cap (Y^c \cup U^c) = Y \cap U^c = Y \cap (X \setminus U)
> $$
>
> Since $U$ is open in $X$, $X \setminus U$ is closed in $X$. Thus $A = Y \cap (\text{closed set in } X)$.
>
> *Remark on notation:* Here $B^c$ denotes the complement of $B$ in the ambient space $X$, so $A \setminus B = A \cap B^c$. The key step $Y \cap (Y^c \cup U^c) = Y \cap U^c$ follows since $Y \cap Y^c = \emptyset$.

^pf-6-2

*Uses:* [[§5 Subspace Topology#^def-5-1|Def. §5.1]]

> [!remark]- Connections
> - The open version is the definition: [[§5 Subspace Topology#^def-5-1|Subspace Topology]]. Closures: [[§7 Interior and Closure#^thm-7-2|Closure in Subspace]].

> [!theorem] Theorem §6.3
> Let $Y \subseteq X$ be a subspace. If $A$ is closed in $Y$, and $Y$ is closed in $X$, then $A$ is closed in $X$.

^thm-6-3

> [!proof]+ Proof
> By [[§6 Closed Sets and Limit Points#^thm-6-2|Theorem §6.2]], $A = C \cap Y$ for some $C$ closed in $X$. Since $C$ and $Y$ are both closed in $X$, their intersection $A = C \cap Y$ is closed in $X$.

^pf-6-3

*Uses:* [[§6 Closed Sets and Limit Points#^thm-6-2|§6.2]], [[§6 Closed Sets and Limit Points#^thm-6-1|§6.1]]

> [!remark]- Connections
> - Open analogue: [[§5 Subspace Topology#^lem-5-2|Lemma §5.2]]. Used in the [[Pasting Lemma|Pasting Lemma]].
