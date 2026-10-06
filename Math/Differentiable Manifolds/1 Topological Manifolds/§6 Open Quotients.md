---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 1
section: 6
tags: [differentiable-manifolds, math591]
---
← [[§5 Quotient Maps]] · ↑ [[· 1 Topological Manifolds]] · [[§7 The Regular Value Theorem]] →

*Thread: quotients — When is a quotient Hausdorff? For open relations, exactly when the graph is closed (Theorem [[§6 Open Quotients#^thm-6-1|§6.1]]). Complex projective space, the first manifold built this way, is worked out at the end of the chapter ([[§9 Complex Projective Space|§9]]); the question returns for orbit spaces ([[§12 Group Actions and Orbit Spaces|§12]]) and coset spaces ([[§13 Homogeneous Spaces|§13]]).*

> [!definition] Definition §6.1: Graph of a Relation
> The **graph** of a relation $\sim$ on a set $X$ is
>
> $$
> \Gamma = \{\, (x, y) \in X \times X \mid x \sim y \,\} \subseteq X \times X .
> $$

^def-6-1

> [!theorem] Theorem §6.1: Hausdorff Criterion
> Assume $\sim$ is an *open* equivalence relation on a topological space $X$, and let $\Gamma \subseteq X \times X$ be its graph ([[§6 Open Quotients#^def-6-1|Definition §6.1]]). Then:
>
> $$
> X/{\sim} \text{ is } T_2 \iff \Gamma \text{ is closed in } X \times X.
> $$
>
> *Lee: no counterpart; a course result (see the comparison below Theorem [[§6 Open Quotients#^thm-6-3|§6.3]])*

^thm-6-1

> [!proof]+ Proof (given in full in lecture)
> ($\Leftarrow$) Assume $\Gamma$ is closed. Let $[x] \neq [y]$ in $X/{\sim}$, i.e. $x \not\sim y$, i.e. $(x, y) \notin \Gamma$. Since $\Gamma$ is closed, its complement is an open set containing $(x,y)$, so by the box characterization ([[§3 Subspaces and Products#^prop-3-8|Proposition §3.8]]) there exist neighborhoods $U$ of $x$ and $V$ of $y$ such that
>
> $$
> (U \times V) \cap \Gamma = \emptyset.
> $$
>
> Now push forward: $\pi(U)$ and $\pi(V)$ are open in $X/{\sim}$ *because the relation is open*, and $[x] \in \pi(U)$, $[y] \in \pi(V)$.
>
> **Claim:** $\pi(U) \cap \pi(V) = \emptyset$. If not, there exist $a \in U$, $b \in V$ with $\pi(a) = \pi(b)$. But $\pi(a) = \pi(b)$ means exactly $a \sim b$, i.e. $(a, b) \in \Gamma$; and $(a,b) \in U \times V$, so $(U \times V) \cap \Gamma \neq \emptyset$ — contradiction.
>
> Thus $\pi(U), \pi(V)$ separate $[x]$ and $[y]$, and $X/{\sim}$ is $T_2$.
>
> ($\Rightarrow$) Assume $X/{\sim}$ is $T_2$; we show the complement of $\Gamma$ is open. Take $(x, y) \in (X \times X) \setminus \Gamma$, i.e. $x \not\sim y$, i.e. $\pi(x) \neq \pi(y)$. By assumption there exist neighborhoods $A$ of $\pi(x)$ and $B$ of $\pi(y)$ in $X/{\sim}$ with $A \cap B = \emptyset$. Careful: $A$ and $B$ live in the *quotient*, not in $X$ — so pull back. Since $\pi$ is continuous, $\pi^{-1}(A) \times \pi^{-1}(B)$ is an open neighborhood of $(x, y)$ in $X \times X$.
>
> **Claim:** $\left(\pi^{-1}(A) \times \pi^{-1}(B)\right) \cap \Gamma = \emptyset$. Suppose by contradiction there is $(a, b) \in \Gamma$ with $a \in \pi^{-1}(A)$ and $b \in \pi^{-1}(B)$. Then $\pi(a) \in A$ and $\pi(b) \in B$; but $(a,b) \in \Gamma$ means $a \sim b$, so $\pi(a) = \pi(b)$. This common point lies in $A \cap B$, so $A \cap B \neq \emptyset$ — contradiction.
>
> Hence every point of the complement of $\Gamma$ has a neighborhood inside the complement, so $\Gamma$ is closed. (Note openness of $\sim$ was not used in this direction.)

^pf-6-1

*Uses:* [[§6 Open Quotients#^def-6-1|Def. §6.1]], [[§4 Quotient Spaces and Open Maps#^def-4-3|Def. §4.3]], [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§4 Quotient Spaces and Open Maps#^prop-4-1|§4.1]], [[§3 Subspaces and Products#^prop-3-8|§3.8]], [[§3 Subspaces and Products#^def-3-3|Def. §3.3]], [[§1 Point-Set Topology Review#^def-1-7|Def. §1.7]]

![[m591-3-6.svg]]
*The direction ($\Leftarrow$): a point $(x,y)$ off the closed graph $\Gamma$ has a box $U \times V$ missing $\Gamma$, and then $\pi(U)$ and $\pi(V)$ separate $[x]$ from $[y]$.*

> [!remark]- Connections
> - Applied to orbit spaces: [[§12 Group Actions and Orbit Spaces#^cor-12-4|§12.4]], [[§12 Group Actions and Orbit Spaces#^thm-12-5|§12.5]]; the failure mode is [[§12 Group Actions and Orbit Spaces#^ex-12-6|Ex. §12.6]].
> - Hausdorff spaces in MATH 590: [[§9 Hausdorff Spaces#^def-9-1|590 Def. §9.1]]; for the special case of a quotient onto a Hausdorff space, compare [[§13 Quotient Topology#^cor-13-4|590 §13.4]](2).

> [!remark] Remark: No Hausdorff Hypothesis on $X$
> Mid-statement, Uribe began to add the hypothesis “assume $X$ is Hausdorff”—then stopped: “actually, I don't need that.” The final statement is correct as it stands: no separation assumption on $X$ is required, only openness of the relation. (Openness, moreover, is used only in the direction $\Leftarrow$; the direction $\Rightarrow$ holds for arbitrary equivalence relations, as the [[§6 Open Quotients#^pf-6-1|proof]] shows.)

^rem-6-1

> [!theorem] Corollary §6.2: The Diagonal Criterion
> A topological space $X$ is Hausdorff if and only if the diagonal $\Delta = \{(x,x) \mid x \in X\}$ is closed in $X \times X$.

^cor-6-2

> [!proof]+ Proof
> Apply [[§6 Open Quotients#^thm-6-1|Theorem §6.1]] to the trivial relation, $x \sim y \iff x = y$. It is open, since every set is its own saturation. Its graph is $\Gamma = \Delta$. And $\pi : X \to X/{\sim}$ is a continuous open bijection, hence a homeomorphism, so $X/{\sim}$ is Hausdorff iff $X$ is. This classical characterization is the special case of the theorem with nothing identified; the theorem is its generalization to quotients.

^pf-6-2

*Uses:* [[§6 Open Quotients#^thm-6-1|§6.1]], [[§4 Quotient Spaces and Open Maps#^prop-4-5|§4.5]], [[§6 Open Quotients#^def-6-1|Def. §6.1]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]] (2), [[§1 Point-Set Topology Review#^def-1-7|Def. §1.7]]

> [!remark] Remark: This Is the Tool
> Uribe (emphasized): “this is going to be our tool for figuring out whether a quotient space is $T_2$.” The workflow it suggests, and which the [[§9 Complex Projective Space#^prop-9-1|ℂPⁿ example below]] executes: (i) show the relation is open — usually via the saturation slogan; (ii) show the graph is closed — often by exhibiting $\Gamma$ as a preimage of a closed set, or as a compact set inside a Hausdorff space.

^rem-6-2

> [!theorem] Theorem §6.3: Second Countability of Open Quotients
> If $\sim$ is an open equivalence relation and $X$ is second countable, then $X/{\sim}$ is second countable.
>
> *Lee: no counterpart; a course result*

^thm-6-3

> [!proof]+ Proof (one line in lecture — “project the countable basis”)
> $\pi : X \to X/{\sim}$ is a continuous surjection, and open because $\sim$ is; so [[§5 Quotient Maps#^lem-5-6|Lemma §5.6]] applies and the image of a countable basis of $X$ is a countable basis of $X/{\sim}$.

^pf-6-3

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-3|Def. §4.3]], [[§5 Quotient Maps#^lem-5-6|§5.6]]

> [!remark]- Connections
> - Reused for coset spaces: [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-5|§14.5]] (second countability of $G/H$), and hence for the Grassmannians, [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-8|§14.8]].

**Comparison with Lee.** Lee's Appendix A has no counterpart to Theorems [[§6 Open Quotients#^thm-6-1|§6.1]] and [[§6 Open Quotients#^thm-6-3|§6.3]]: in his book the Hausdorff property and second countability of $\mathbb{RP}^n$ and $\mathbb{CP}^n$ are checked example by example (Example 1.5, Problem 1-9). The course proves one criterion for all open quotients at once and then reuses it for orbit spaces ([[§12 Group Actions and Orbit Spaces|§12]]) and coset spaces ([[§13 Homogeneous Spaces|§13]]) — which is what makes the quotient thread a thread.

> [!example] Example §6.1: The Line with Two Origins — via the Criterion
> Let $X = (\mathbb{R} \times \{1\}) \cup (\mathbb{R} \times \{2\}) \subseteq \mathbb{R}^2$ with the subspace topology (two disjoint copies of $\mathbb{R}$), and $(x,1) \sim (x,2)$ for $x \neq 0$, as in [[§4 Quotient Spaces and Open Maps#^ex-4-1|Example §4.1]]. The graph
>
> $$
> \Gamma = \{(a,b) \in X \times X \mid a = b\} \cup \{\, ((x,i),(x,j)) \mid x \neq 0,\ i \neq j \,\}
> $$
>
> is *not* closed in $X \times X$: the points $\big((\tfrac1n, 1), (\tfrac1n, 2)\big)$ lie in $\Gamma$ for every $n$, and converge in $X \times X$ to $\big((0,1),(0,2)\big)$, which is not in $\Gamma$ (the two origins are distinct and are not identified, the identification being imposed only for $x \neq 0$). A closed set contains the limits of its convergent sequences, so $\Gamma$ is not closed.
>
> The relation is open: the saturation of an open $U \subseteq X$ is $U \cup \sigma(U \setminus (\{0\} \times \{1,2\}))$, where $\sigma(x,i) = (x, 3-i)$ swaps the two copies—a homeomorphism of $X$—so the saturation is a union of two open sets. [[§6 Open Quotients#^thm-6-1|Theorem §6.1]] therefore applies and gives: $X/{\sim}$ is *not* Hausdorff. This recovers [[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]] from the criterion rather than by separating the origins by hand.

^ex-6-1

*Uses:* [[§4 Quotient Spaces and Open Maps#^ex-4-1|Ex. §4.1]], [[§6 Open Quotients#^def-6-1|Def. §6.1]], [[§4 Quotient Spaces and Open Maps#^prop-4-5|§4.5]], [[§6 Open Quotients#^thm-6-1|§6.1]], [[§12 Metric Topology#^lem-12-8|590 §12.8]]

> [!remark]- Connections
> - “A closed set contains the limits of its convergent sequences” is the [[§12 Metric Topology#^lem-12-8|Sequence Lemma, 590 §12.8]].

PSet 1, Problem 2 asks for the non-closedness of $\Gamma$ directly. The sequence argument above needs no metrizability: in any topological space, if $z_n \to z$ with all $z_n$ in a closed set $C$, then $z \in C$ (otherwise the open set $X \setminus C$ would eventually contain the $z_n$).

The application of these criteria to complex projective space $\mathbb{CP}^n$ is collected in [[§9 Complex Projective Space|§9]].

