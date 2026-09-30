---
type: section
subject: "[[Topology]]"
chapter: 1
section: 5
munkres: "§16"
tags: [topology, math590]
---
← [[Topology §4 Product Topology]] · ↑ [[Topology — 1 Topological Spaces and Constructions]] · [[Topology §6 Closed Sets and Limit Points]] →

## Definition and Basic Properties

> [!definition] Definition §5.1: Subspace Topology
> Let $(X, \mathcal{T})$ be a topological space. If $Y \subseteq X$ is a subset, the collection
>
> $$
> \mathcal{T}_Y = \{Y \cap U \mid U \in \mathcal{T}\}
> $$
>
> is a topology on $Y$, called the **subspace topology**. With this topology, $Y$ is called a **subspace** of $X$.

^def-5-1

> [!remark]- Connections
> - Closed sets of a subspace: [[Topology §6 Closed Sets and Limit Points#^thm-6-2|Closed Sets in Subspaces]]; closures: [[Topology §7 Interior and Closure#^thm-7-2|Closure in Subspace]].
> - Metric version: [[Topology §11 Metric Topology#^thm-11-6|Subspace of Metric Space]].

> [!remark] Remark: Why the Subspace Topology?
> The subspace topology is the *unique* topology on $Y$ that makes the [[Topology §9 Continuous Functions#^thm-9-4|inclusion map]] $\iota: Y \hookrightarrow X$ continuous and satisfies a universal property: a function $f: Z \to Y$ is continuous if and only if $\iota \circ f: Z \to X$ is continuous. In other words, this is the coarsest topology on $Y$ such that “being a subset” respects the topological structure. The key subtlety is that open in $Y$ need not be open in $X$—$[0, \tfrac{1}{2})$ is open in $[0,1)$ but not in $\mathbb{R}$. Getting comfortable with this distinction is essential for working with compactness and connectedness in subspaces.

^rem-5-1

> [!remark]- Connections
> - Compactness in subspaces: [[Topology §15 Compact Spaces#^lem-15-1|Compactness in Subspaces]]; connectedness: [[Topology §13 Connected Spaces#^rem-13-4|Limit Points in X vs. Y]].

> [!example] Example §5.1
> $[0,1) \subseteq \mathbb{R}$. Is $[0, \frac{1}{2}) \subseteq \mathbb{R}$ open in $\mathbb{R}$? No. If $0 \in B \in \mathcal{B}$, then $B \subseteq [0, \frac{1}{2})$ is impossible since $B$ must contain points less than $0$.
>
> Is $[0, \frac{1}{2}) \subseteq [0,1)$ open in $[0,1)$? Yes: $(-1, \frac{1}{2}) \cap [0,1) = [0, \frac{1}{2})$, which is open in $[0,1)$.

^ex-5-1

> [!theorem] Lemma §5.1: Basis for Subspace Topology
> If $\mathcal{B}$ is a basis for the topology of $X$, then $\mathcal{B}_Y = \{B \cap Y \mid B \in \mathcal{B}\}$ is a basis for the subspace topology on $Y$.

^lem-5-1

> [!theorem] Lemma §5.2
> If $Y \subseteq X$, $U$ is open in $Y$, and $Y$ is open in $X$, then $U$ is open in $X$.

^lem-5-2

> [!proof]+ Proof
> $U$ open in $Y$ $\Rightarrow$ $U = V \cap Y$ where $V$ is open in $X$. $\Rightarrow$ $U$ is open in $X$ since $V$ and $Y$ are both open in $X$.
>
> $Y$ open in $X$ $\Rightarrow$ $V \cap Y$ is open in $X$.

^pf-5-2

> [!remark]- Connections
> - Closed analogue: [[Topology §6 Closed Sets and Limit Points#^thm-6-3|Theorem §6.3]].

> [!example] Example §5.2
> $Y = [0,1] \subseteq X = \mathbb{R}$. The subspace topology on $Y$ has basis $\{(a,b) \cap Y \mid a, b \in \mathbb{R}\}$:
> - $(a,b)$ if $a, b \in Y$
> - $[0, b)$ if $b \in Y$, $a \notin Y$
> - $(a, 1]$ if $a \in Y$, $b \notin Y$
> - $\emptyset$ if $a, b \notin Y$
>
> For $[0,1] \subseteq \mathbb{R}$, the subspace topology is the same as the [[Topology §3 Order Topology#^def-3-4|order topology]] on $[0,1]$.

^ex-5-2

> [!example] Example §5.3: Subspace $\neq$ Order Topology: $I \times I$
> Consider $[0,1] \times [0,1] \subseteq \mathbb{R} \times \mathbb{R}$ with [[Topology §3 Order Topology#^def-3-3|dictionary order]]. The subspace topology on $I \times I$ is **not** the same as the order topology on $I \times I$.
>
> Consider $\{\frac{1}{2}\} \times (\frac{1}{2}, 1]$.
>
> $\mathcal{D}$: $\{\frac{1}{2}\} \times (\frac{1}{2}, 1]$ is open in subspace topology: $= U \cap (I \times I)$, where $U = (\frac{1}{2} - \frac{1}{2}, \frac{1}{2} + \frac{1}{2}) \times (\frac{1}{2}, 2) \subseteq \mathbb{R} \times \mathbb{R}$.
>
> $\mathcal{D}$: $\{\frac{1}{2}\} \times (\frac{1}{2}, 1]$ not open in order topology on $I \times I$. The point $\frac{1}{2} \times 1$ is not a max in $I \times I$, so any basis element containing $\frac{1}{2} \times 1$ must contain some $p \times q > \frac{1}{2} \times 1$. But for $\frac{1}{2} \times 1 \in \mathcal{B} \subseteq \{\frac{1}{2}\} \times (\frac{1}{2}, 1]$, we would need $\mathcal{B}$ to contain only points with first coordinate $\frac{1}{2}$, which contradicts containing points greater than $\frac{1}{2} \times 1$.

^ex-5-3
