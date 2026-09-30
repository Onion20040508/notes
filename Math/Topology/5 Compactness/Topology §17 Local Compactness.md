---
type: section
subject: "[[Topology]]"
chapter: 5
section: 17
munkres: "§29"
tags: [topology, math590]
---
← [[Topology §16 Limit Point Compactness]] · ↑ [[Topology — 5 Compactness]] · [[Topology §18 Countability Axioms]] →

## Definition and Examples

> [!definition] Definition §17.1: Locally Compact
> A space $X$ is **locally compact at $x$** if there is some compact subspace $C$ of $X$ that contains a neighborhood of $x$.
>
> $X$ is **locally compact** if it is locally compact at every point $x \in X$.

^def-17-1

> [!remark] Remark: Local vs Global Compactness
> Local compactness is a weaker, “pointwise” version of compactness:
> - **Compact:** The entire space fits in a “finite” structure.
> - **Locally compact:** Around each point, there's a compact neighborhood—but the whole space may be infinite.
>
> **Why it matters:**
> - $\mathbb{R}^n$ is locally compact but not compact ([[Topology §17 Local Compactness#^ex-17-3|Example §17.3]]). Many analysis theorems work because we can “localize” to compact neighborhoods.
> - Locally compact Hausdorff spaces have [[Topology §17 Local Compactness#^thm-17-5|one-point compactifications]], letting us “add a point at infinity” to make them compact.
> - Infinite-dimensional spaces (like $\mathbb{R}^\omega$) often fail local compactness ([[Topology §17 Local Compactness#^ex-17-5|Example §17.5]])—this is a key distinction between finite and infinite dimensions.

^rem-17-1

> [!example] Example §17.1
> $\mathbb{R}$ is locally compact. For any $x \in \mathbb{R}$, we have $x \in (a, b) \subseteq [a, b]$, where $[a, b]$ is [[Topology §15 Compact Spaces#^cor-15-11|compact]].

^ex-17-1

> [!example] Example §17.2
> Any compact space is locally compact. (Take $C = X$ for every point.)

^ex-17-2

> [!example] Example §17.3
> $\mathbb{R}^n$ is locally compact. For any $x = (x_1, \ldots, x_n) \in \mathbb{R}^n$:
>
> $$
> x \in (a_1, b_1) \times \cdots \times (a_n, b_n) \subseteq [a_1, b_1] \times \cdots \times [a_n, b_n]
> $$
>
> where the closed box is compact ([[Topology §15 Compact Spaces#^cor-15-11|finite product of compact intervals]]).

^ex-17-3

> [!example] Example §17.4
> A simply ordered set $X$ with the [[Topology §14 Connected Subspaces of ℝ#^def-14-1|l.u.b. property]] is locally compact (in the order topology).
>
> Given any basis element $(a, b)$, we have $[a, b] \subseteq X$ which is [[Topology §15 Compact Spaces#^thm-15-10|compact]], and $(a, b) \subseteq [a, b]$.

^ex-17-4

> [!example] Example §17.5: $\mathbb{R}^\omega$ is Not Locally Compact
> $\mathbb{R}^\omega$ (with the [[Topology §10 Product Topology on Arbitrary Products#^def-10-1|product topology]]) is not locally compact.
>
> *Proof:* Consider the origin $0 = (0, 0, 0, \ldots)$. We show no compact set contains a neighborhood of $0$.
>
> Any basis element containing $0$ has the form
>
> $$
> B = (a_1, b_1) \times \cdots \times (a_n, b_n) \times \mathbb{R} \times \mathbb{R} \times \cdots
> $$
>
> where $a_i < 0 < b_i$ for $i = 1, \ldots, n$.
>
> Suppose $B \subseteq C$ for some compact $C$. Then $\overline{B} \subseteq \overline{C} = C$ (since compact $\subseteq$ Hausdorff $\Rightarrow$ closed ([[Compact Subspace of a Hausdorff Space is Closed|§15.4]])).
>
> But $\overline{B} = [a_1, b_1] \times \cdots \times [a_n, b_n] \times \mathbb{R} \times \mathbb{R} \times \cdots$
>
> This is not compact: the cover $\{[a_1, b_1] \times \cdots \times [a_n, b_n] \times (-m, m) \times \mathbb{R} \times \cdots \mid m \in \mathbb{Z}_+\}$ by sets open in $\overline{B}$ (where the $(-m, m)$ is in the $(n+1)$-th coordinate) has no finite subcover.
>
> Contradiction. So $\mathbb{R}^\omega$ is not locally compact.

^ex-17-5

## One-Point Compactification

> [!remark] Remark: Goal
> Given a locally compact Hausdorff space $X$, we want to construct a compact Hausdorff space $Y$ containing $X$ with exactly one extra point. This construction has three parts: (1) define the topology on $Y$, (2) verify it has the desired properties, (3) show the construction is essentially unique.

^rem-17-2

### Step 1: Topologizing $Y$

> [!definition] Definition §17.2: One-Point Compactification Topology
> Let $X$ be a topological space. Define $Y = X \cup \{\infty\}$ where $\infty \notin X$. The **one-point compactification topology** on $Y$ consists of two types of open sets:
> - **Type (1):** Sets $U$ that are open in $X$ (these do not contain $\infty$).
> - **Type (2):** Sets of the form $Y \setminus C$ where $C \subseteq X$ is compact (these contain $\infty$).

^def-17-2

> [!theorem] Proposition §17.1: The Collection $\mathcal{T}_Y$ is a Topology
> Let $X$ be a Hausdorff space. Then $\mathcal{T}_Y$ as defined above is a [[Topology §1 Topological Spaces#^def-1-1|topology]] on $Y$.

^prop-17-1

> [!proof]+ Proof
> *$\emptyset$ and $Y$:* $\emptyset$ is open in $X$ (type 1). $Y = Y \setminus \emptyset$ where $\emptyset$ is compact (type 2). ✓
>
> *Finite intersections:* Let $U_1, U_2 \in \mathcal{T}_Y$. Three cases:
> - Both type (1): $U_1 \cap U_2$ is open in $X$, so type (1). ✓
> - $U_1$ type (1), $U_2 = Y \setminus C_2$ type (2): $U_1 \cap (Y \setminus C_2) = U_1 \cap (X \setminus C_2) = U_1 \setminus C_2$. Since $C_2$ is compact in Hausdorff $X$, $C_2$ is closed ([[Compact Subspace of a Hausdorff Space is Closed|§15.4]]), so $U_1 \setminus C_2$ is open in $X$. Type (1). ✓
> - Both type (2): $(Y \setminus C_1) \cap (Y \setminus C_2) = Y \setminus (C_1 \cup C_2)$. Finite union of compact sets is compact. Type (2). ✓
>
> *Arbitrary unions:* Let $\{U_\alpha\} \subseteq \mathcal{T}_Y$. If all are type (1), their union is open in $X$ (type 1). Otherwise, split into $J = \{\alpha : U_\alpha \text{ type (1)}\}$ and $I = \{\alpha : U_\alpha = Y \setminus C_\alpha \text{ type (2)}\}$:
>
> $$
> \bigcup_\alpha U_\alpha = \underbrace{\bigcup_{\alpha \in J} U_\alpha}_{=: V,\text{ open in }X} \cup \underbrace{\bigcup_{\alpha \in I} (Y \setminus C_\alpha)}_{= Y \setminus \bigcap_{\alpha \in I} C_\alpha} = V \cup (Y \setminus C) = Y \setminus (C \setminus V)
> $$
>
> where $C = \bigcap_{\alpha \in I} C_\alpha$. Now $C$ is closed in each $C_\alpha$ ([[Topology §6 Closed Sets and Limit Points#^thm-6-1|intersection of closed sets]] in Hausdorff), hence [[Closed Subspace of a Compact Space is Compact|compact]]. And $C \setminus V$ is a closed subset of $C$ (since $V$ is open), hence compact. So the union is type (2). ✓

^pf-17-1

*Uses:* [[Compact Subspace of a Hausdorff Space is Closed|§15.4]], [[Topology §6 Closed Sets and Limit Points#^thm-6-1|§6.1]], [[Closed Subspace of a Compact Space is Compact|§15.2]]

### Step 2: Verifying the Properties

> [!theorem] Proposition §17.2: $X$ is a Subspace of $Y$
> The [[Topology §5 Subspace Topology#^def-5-1|subspace topology]] on $X \subseteq Y$ equals the original topology on $X$.

^prop-17-2

> [!proof]+ Proof
> $(\subseteq)$: If $V$ is open in $X$, then $V \in \mathcal{T}_Y$ (type 1), so $V = V \cap X$ is in the subspace topology.
>
> $(\supseteq)$: Let $U \in \mathcal{T}_Y$. If $U$ is type (1), then $U \cap X = U$ is open in $X$. If $U = Y \setminus C$ is type (2), then $U \cap X = X \setminus C$, which is open since $C$ is closed in $X$ ([[Compact Subspace of a Hausdorff Space is Closed|compact in Hausdorff]]).

^pf-17-2

*Uses:* [[Topology §5 Subspace Topology#^def-5-1|Def. §5.1]], [[Compact Subspace of a Hausdorff Space is Closed|§15.4]]

> [!theorem] Proposition §17.3: $Y$ is Compact
> If $X$ is any topological space, then $Y = X \cup \{\infty\}$ with the above topology is compact.

^prop-17-3

> [!proof]+ Proof
> Let $\mathcal{A}$ be an open cover of $Y$. Since $\infty \in Y$, some $A \in \mathcal{A}$ contains $\infty$, so $A = Y \setminus C$ for some compact $C \subseteq X$. The remaining sets in $\mathcal{A}$, intersected with $X$, form an open cover of $C$. Since $C$ is compact, finitely many $A_1, \ldots, A_n \in \mathcal{A}$ cover $C$ ([[Topology §15 Compact Spaces#^lem-15-1|Lemma §15.1]]). Then $\{A, A_1, \ldots, A_n\}$ covers $Y$.

^pf-17-3

*Uses:* [[Topology §15 Compact Spaces#^lem-15-1|§15.1]]

> [!theorem] Proposition §17.4: $Y$ is Hausdorff if $X$ is Locally Compact Hausdorff
> If $X$ is locally compact and Hausdorff, then $Y$ is Hausdorff.

^prop-17-4

> [!proof]+ Proof
> Let $x, y \in Y$ with $x \neq y$.
>
> *Case 1: $x, y \in X$.* Since $X$ is [[Topology §8 Hausdorff Spaces#^def-8-1|Hausdorff]], choose disjoint open $U, V$ in $X$ separating $x, y$. These are open in $Y$ (type 1). ✓
>
> *Case 2: $x \in X$, $y = \infty$.* By [[Topology §17 Local Compactness#^def-17-1|local compactness]], there exists compact $C \subseteq X$ containing a neighborhood $U$ of $x$. Then $U$ (type 1, open in $Y$) and $Y \setminus C$ (type 2, open in $Y$) are disjoint neighborhoods of $x$ and $\infty$ respectively. ✓

^pf-17-4

*Uses:* [[Topology §8 Hausdorff Spaces#^def-8-1|Def. §8.1]], [[Topology §17 Local Compactness#^def-17-1|Def. §17.1]]

> [!remark] Remark
> Note where each hypothesis is used: Hausdorff is needed to make $\mathcal{T}_Y$ a topology (compact sets must be closed) and to separate two points in $X$. Local compactness is needed only for the Hausdorff property of $Y$—specifically, to separate $x \in X$ from $\infty$.

^rem-17-3

### Step 3: The Main Theorem

> [!theorem] Theorem §17.5: One-Point Compactification (Munkres 29.1)
> $X$ is locally compact Hausdorff if and only if there exists a space $Y$ satisfying:
> 1. $X$ is a subspace of $Y$.
> 2. $Y \setminus X$ is a single point.
> 3. $Y$ is compact Hausdorff.
>
> Moreover, if $Y$ and $Y'$ are two spaces satisfying (1)–(3), then there is a homeomorphism $h: Y \to Y'$ that equals the identity on $X$.

^thm-17-5

> [!proof]+ Proof of Existence ($\Rightarrow$)
> If $X$ is locally compact Hausdorff, then $Y = X \cup \{\infty\}$ with the topology defined above satisfies (1)–(3) by the four propositions above ([[Topology §17 Local Compactness#^prop-17-1|§17.1]], [[Topology §17 Local Compactness#^prop-17-2|§17.2]], [[Topology §17 Local Compactness#^prop-17-3|§17.3]], [[Topology §17 Local Compactness#^prop-17-4|§17.4]]).

^pf-17-5

*Uses:* [[Topology §17 Local Compactness#^prop-17-1|§17.1]], [[Topology §17 Local Compactness#^prop-17-2|§17.2]], [[Topology §17 Local Compactness#^prop-17-3|§17.3]], [[Topology §17 Local Compactness#^prop-17-4|§17.4]]

> [!proof]+ Proof of Converse ($\Leftarrow$)
> Suppose $Y$ satisfies (1)–(3). Write $Y \setminus X = \{\infty\}$.
>
> **$X$ is Hausdorff:** $X$ is a subspace of the Hausdorff space $Y$, hence Hausdorff.
>
> **$X$ is locally compact:** Given $x \in X$, choose disjoint open sets $U \ni x$ and $V \ni \infty$ in $Y$ (using that $Y$ is Hausdorff). Let $C = Y \setminus V$. Then $C$ is closed in $Y$, hence compact ([[Closed Subspace of a Compact Space is Compact|closed subset of compact]]). Since $\infty \in V$, we have $C \subseteq X$. And $U \cap V = \emptyset$ gives $U \subseteq C$, so $C$ is a compact subset of $X$ containing the neighborhood $U \cap X$ of $x$.

^pf-17-5-2

*Uses:* [[Closed Subspace of a Compact Space is Compact|§15.2]]

> [!proof]+ Proof of Uniqueness
> Let $Y, Y'$ both satisfy (1)–(3), with $Y \setminus X = \{p\}$ and $Y' \setminus X = \{q\}$. Define $h: Y \to Y'$ by $h(x) = x$ for $x \in X$ and $h(p) = q$.
>
> We show $h$ is a homeomorphism by showing $h$ maps open sets to open sets (then symmetry gives $h^{-1}$ continuous; [[Topology §9 Continuous Functions#^prop-9-2|Proposition §9.2]]).
>
> Let $U$ be open in $Y$. If $p \notin U$, then $U \subseteq X$ and $U$ is open in $X$. Since $X$ is open in $Y'$ (because $\{q\}$ is [[Topology §8 Hausdorff Spaces#^thm-8-1|closed in the Hausdorff space]] $Y'$), and $U$ is open in $X$, $U$ is open in $Y'$ ([[Topology §5 Subspace Topology#^lem-5-2|§5.2]]). So $h(U) = U$ is open. ✓
>
> If $p \in U$, then $C = Y \setminus U$ is closed in $Y$, hence [[Closed Subspace of a Compact Space is Compact|compact]]. Since $p \notin C$, we have $C \subseteq X$. So $C$ is a compact subspace of $X$, hence also a compact subspace of $Y'$ (since $X$ is a subspace of $Y'$). Since $Y'$ is Hausdorff, $C$ is closed in $Y'$ ([[Compact Subspace of a Hausdorff Space is Closed|§15.4]]). Thus $h(U) = Y' \setminus C$ is open in $Y'$. ✓
>
> By symmetry (the same argument applies to $h^{-1}$), $h$ is a homeomorphism.

^pf-17-5-3

*Uses:* [[Topology §9 Continuous Functions#^prop-9-2|§9.2]], [[Topology §8 Hausdorff Spaces#^thm-8-1|§8.1]], [[Topology §5 Subspace Topology#^lem-5-2|§5.2]], [[Closed Subspace of a Compact Space is Compact|§15.2]], [[Compact Subspace of a Hausdorff Space is Closed|§15.4]]

> [!definition] Definition §17.3: One-Point Compactification
> The space $Y$ constructed above is called the **one-point compactification** of $X$, often denoted $X^* = X \cup \{\infty\}$.

^def-17-3

> [!remark] Remark
> If $X$ is already compact, the one-point compactification is uninteresting: $\infty$ is an isolated point (since $X$ itself is compact, $Y \setminus X = \{\infty\}$ is open). If $X$ is not compact, then $\infty$ is a [[Topology §7 Interior and Closure#^def-7-3|limit point]] of $X$, so $\overline{X} = Y$.

^rem-17-4

> [!example] Example §17.6: Discrete Subspace of $\mathbb{R}$
> Let $X = \{1/n \mid n \in \mathbb{Z}_+\} \subseteq \mathbb{R}$.
>
> $X$ has the discrete topology (each $\{1/n\} = (1/n - \varepsilon, 1/n + \varepsilon) \cap X$ is open for small $\varepsilon$).
>
> $X$ is locally compact (every point has a compact neighborhood—itself) and Hausdorff (subspace of $\mathbb{R}$), but not compact ($\{\{1/n\}\}$ is an open cover with no finite subcover).
>
> The one-point compactification is $Y = \{0\} \cup \{1/n \mid n \in \mathbb{Z}_+\}$.
>
> In fact, $X$ is homeomorphic to $\mathbb{Z}_+$: the map $1/n \mapsto n$ is a bijection, and both spaces have the discrete topology. Thus $Y$ is the one-point compactification of $\mathbb{Z}_+$.

^ex-17-6

> [!remark]- Connections
> - Compactness of this $Y$ checked directly: [[Topology §15 Compact Spaces#^ex-15-4|Example §15.4]].

> [!example] Example §17.7: One-Point Compactification of $\mathbb{R}$ and $\mathbb{R}^2$
> The one-point compactification of $\mathbb{R}$ is homeomorphic to $S^1$ (the circle).
>
> *Idea:* Stereographic projection from the north pole $N$ of $S^1$ to a tangent line at the south pole gives a homeomorphism $S^1 \setminus \{N\} \cong \mathbb{R}$. Adding back $N$ gives the one-point compactification.
>
> Similarly, the one-point compactification of $\mathbb{R}^2$ is homeomorphic to $S^2$ (the sphere).
>
> *Idea:* Stereographic projection from the north pole gives $S^2 \setminus \{N\} \cong \mathbb{R}^2$. Every ray from $N$ to a point in $\mathbb{R}^2$ intersects the sphere at exactly one point (besides $N$).

^ex-17-7

![[m590-17-1.svg]]
*The one-point compactification of $\mathbb{R}$: projecting from $N$ onto the tangent line at $S$ sends $p\in S^1\setminus\{N\}$ to $x\in\mathbb{R}$. A compact $C=[-M,M]$ (blue) corresponds to a closed arc away from $N$, and its complement (red: two rays plus an open arc through $N$) is exactly a type (2) neighborhood $Y\setminus C$ of $\infty=N$. Going to infinity in either direction means approaching $N$.*

![[m590-17-2.svg]]
*The same picture one dimension up, $\mathbb{R}^2\cup\{\infty\}\cong S^2$: the ray from $N$ through $p$ hits the tangent plane at $w$. The compact disk $C$ of radius $2$ (blue) corresponds to the lower hemisphere, and its complement (red) corresponds to the upper cap around $N$. Neighborhoods of $\infty$ are complements of compact sets.*

## Local Compactness in Hausdorff Spaces

> [!theorem] Theorem §17.6: Characterization of Local Compactness (Munkres 29.2)
> Let $X$ be a Hausdorff space. Then $X$ is locally compact if and only if given $x \in X$ and a neighborhood $U$ of $x$, there is a neighborhood $V$ of $x$ such that $\overline{V}$ is compact and $\overline{V} \subseteq U$.

^thm-17-6

> [!proof]+ Proof
> $(\Leftarrow)$: Clear. The set $C = \overline{V}$ is a compact subspace containing the neighborhood $V$ of $x$, so $X$ is locally compact at $x$.
>
> $(\Rightarrow)$: Suppose $X$ is locally compact. Let $x \in X$ and let $U$ be a neighborhood of $x$. Take the [[Topology §17 Local Compactness#^thm-17-5|one-point compactification]] $Y = X \cup \{\infty\}$, and let $C = Y \setminus U$. Then $C$ is closed in $Y$ (since $U$ is open in $X$ and the topology on $Y$ makes $X$ open in $Y$), so $C$ is a compact subspace of $Y$ ([[Closed Subspace of a Compact Space is Compact|closed subset of compact]]).
>
> Since $Y$ is compact Hausdorff, we can apply Munkres Lemma 26.4 (a point and a disjoint compact set in a Hausdorff space can be separated by open sets) to choose disjoint open sets $V \ni x$ and $W \supseteq C$ in $Y$. Then $\overline{V}$ (closure in $Y$) is compact: it is a closed subset of the compact space $Y$. Furthermore, $\overline{V}$ is disjoint from $C$ since $\overline{V} \subseteq Y \setminus W$ and $W \supseteq C$, so $\overline{V} \subseteq Y \setminus C = U$, as desired.

^pf-17-6

*Uses:* [[Topology §17 Local Compactness#^def-17-1|Def. §17.1]], [[Topology §17 Local Compactness#^thm-17-5|§17.5]], [[Closed Subspace of a Compact Space is Compact|§15.2]]

> [!remark] Remark
> This stronger formulation says: in a locally compact Hausdorff space, not only can you find *some* compact set containing a neighborhood, you can find one *inside any given neighborhood*. The one-point compactification is the key tool—it provides a compact Hausdorff ambient space where standard separation arguments apply.

^rem-17-5

> [!theorem] Corollary §17.7: Subspaces Inherit Local Compactness (Munkres 29.3)
> Let $X$ be locally compact Hausdorff and let $A$ be a subspace of $X$. If $A$ is closed in $X$ or open in $X$, then $A$ is locally compact.

^cor-17-7

> [!proof]+ Proof
> **Case 1: $A$ closed.** Given $x \in A$, let $C$ be a compact subspace of $X$ containing a neighborhood $U$ of $x$ in $X$. Then $C \cap A$ is closed in $C$ (since $A$ is closed in $X$) and thus [[Closed Subspace of a Compact Space is Compact|compact]]. It contains the neighborhood $U \cap A$ of $x$ in $A$. (Note: the Hausdorff condition was not needed here.)
>
> **Case 2: $A$ open.** Given $x \in A$, apply [[Topology §17 Local Compactness#^thm-17-6|Theorem §17.6 (Munkres 29.2)]] to the space $X$: since $A$ is a neighborhood of $x$, there exists a neighborhood $V$ of $x$ in $X$ with $\overline{V}$ compact and $\overline{V} \subseteq A$. Then $C = \overline{V}$ is a compact subspace of $A$ containing the neighborhood $V$ of $x$ in $A$.

^pf-17-7

*Uses:* [[Closed Subspace of a Compact Space is Compact|§15.2]], [[Topology §17 Local Compactness#^thm-17-6|§17.6]]

> [!theorem] Corollary §17.8: Locally Compact Hausdorff Spaces (Munkres 29.4)
> A space $X$ is locally compact Hausdorff if and only if $X$ is homeomorphic to an open subspace of a compact Hausdorff space.

^cor-17-8

> [!proof]+ Proof
> $(\Rightarrow)$: $X$ is an open subspace of its one-point compactification $Y = X \cup \{\infty\}$, which is compact Hausdorff by the [[Topology §17 Local Compactness#^thm-17-5|one-point compactification theorem]].
>
> $(\Leftarrow)$: Suppose $X \cong U \subseteq Y$ where $U$ is open in $Y$ compact Hausdorff. Since $Y$ is compact Hausdorff, $Y$ is [[Topology §17 Local Compactness#^ex-17-2|locally compact]]. By [[Topology §17 Local Compactness#^cor-17-7|Corollary §17.7 (Munkres 29.3)]] (open subspace of locally compact Hausdorff is locally compact), $U$ is locally compact. Since $Y$ is Hausdorff, $U$ inherits the Hausdorff property. So $X$ is locally compact Hausdorff.

^pf-17-8

*Uses:* [[Topology §17 Local Compactness#^thm-17-5|§17.5]], [[Topology §17 Local Compactness#^ex-17-2|Ex. §17.2]], [[Topology §17 Local Compactness#^cor-17-7|§17.7]]
