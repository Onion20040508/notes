---
type: section
subject: "[[Topology]]"
chapter: 2
section: 7
tags: [topology, math590]
---
← [[§6 Closed Sets and Limit Points]] · ↑ [[· 2 Closedness, Continuity, and Hausdorff]] · [[§8 Hausdorff Spaces]] →

## Definitions

> [!definition] Definition §7.1: Interior and Closure
> Let $A \subseteq X$, where $X$ is a topological space.
>
> The **interior** of $A$, denoted $\text{Int}(A)$ or $\mathring{A}$, is the union of all open sets in $X$ contained in $A$.
>
> The **closure** of $A$, denoted $\text{cl}(A)$ or $\overline{A}$, is the intersection of all closed sets in $X$ containing $A$.

^def-7-1

> [!remark]- Connections
> - MATH 451 version: [[§13 Some Topological Concepts in Metric Spaces#^def-13-6|Closure]] in a metric space, with its [[§13 Some Topological Concepts in Metric Spaces#^prop-13-6|Sequential Characterization of the Closure]].
> - In a normed space: the closure as the set of limits of sequences ([[§8 Normed Linear Spaces#^def-8-7|556 Def. §8.7]]), and interior points through balls ([[§8 Normed Linear Spaces#^def-8-9|556 Def. §8.9]]), which are stronger than the algebraic interior points of [[§5 Convex Sets and the Gauge#^def-5-1|556 Def. §5.1]] ([[§8 Normed Linear Spaces#^ex-8-2|556 Ex. §8.2]]).

> [!theorem] Lemma §7.1: Interior and Closure Containment
> Let $A \subseteq X$ be a subset of a topological space. Then:
> 1. $\text{Int}(A) \subseteq A \subseteq \overline{A}$
> 2. If $A$ is open, then $\text{Int}(A) = A$.
> 3. If $A$ is closed, then $\overline{A} = A$.

^lem-7-1

> [!proof]+ Proof
> (1) $\text{Int}(A) \subseteq A$: By definition, $\text{Int}(A)$ is the union of all open sets contained in $A$. If $x \in \text{Int}(A)$, then $x \in U$ for some open $U \subseteq A$, hence $x \in A$.
>
> $A \subseteq \overline{A}$: By definition, $\overline{A}$ is the intersection of all closed sets containing $A$. Every such closed set contains $A$, so their intersection contains $A$.
>
> (2) If $A$ is open, then $A$ is an open set contained in $A$, so $A \subseteq \text{Int}(A)$. Combined with (1), $\text{Int}(A) = A$.
>
> (3) If $A$ is closed, then $A$ is a closed set containing $A$, so $\overline{A} \subseteq A$. Combined with (1), $\overline{A} = A$.

^pf-7-1

> [!remark] Remark
> $\text{Int}(A)$ is open in $X$. $\overline{A}$ is closed in $X$.

^rem-7-1

> [!remark] Remark: Intuition: Room to Wiggle and Reachable by Limits
> Think of $\text{Int}(A)$ as the points where you have “room to wiggle”—you can perturb slightly in any direction and stay in $A$. The closure $\overline{A}$ consists of points “reachable by limits” from $A$: if every neighborhood of $x$ meets $A$, then $x \in \overline{A}$ (this is made precise by [[Closure Characterization|Theorem §7.3]] below). The boundary $\overline{A} \setminus \text{Int}(A)$ is the “edge”—points that are reachable from $A$ but have no wiggle room.
>
> This duality ($\text{Int}$ expands from inside, $\overline{\phantom{A}}$ approaches from outside) is formalized by the identity $X \setminus \text{Int}(A) = \overline{X \setminus A}$: the complement of the interior is the closure of the complement.

^rem-7-2

![[m590-7-1.svg]]
*Three kinds of points for a set $A$ (blue; the solid part of the boundary belongs to $A$, the dashed part does not). The point $p$ has a neighborhood inside $A$, so it has room to wiggle and $p \in \text{Int}(A)$. The point $x$ is not in $A$, yet every neighborhood of it (red) meets $A$ (shaded), so $x \in \overline{A} \setminus \text{Int}(A)$ is on the boundary. The point $y$ has a neighborhood $U$ (gray) that misses $A$, so $y \notin \overline{A}$. This is exactly the test in Theorem §7.3.*

> [!example] Example §7.1
> $A = [0, 1] \subseteq \mathbb{R}$. Then $\text{Int}(A) = (0, 1)$ and $\overline{A} = [0, 1]$.

^ex-7-1

> [!remark] Remark
> If $A \subset Y \subseteq X$ (where $Y$ is a subspace), closure and interior in $Y$ may differ from closure and interior in $X$. Need to clarify which space we're working in.

^rem-7-3

## Closure in Subspaces

> [!theorem] Theorem §7.2: Closure in Subspace
> Let $Y \subseteq X$ be a subspace of $X$, $A \subseteq Y$, $\overline{A}$ = closure of $A$ in $X$. Then the closure of $A$ in $Y$ is equal to $\overline{A} \cap Y$.

^thm-7-2

> [!proof]+ Proof
> Let $B$ be the closure of $A$ in $Y$.
>
> $(\supseteq)$ $\overline{A}$ is closed in $X$ $\Rightarrow$ $\overline{A} \cap Y$ is closed in $Y$. Since $\overline{A} \supseteq A$, and by definition, $B$ is the intersection of all closed sets of $Y$ containing $A$, $\Rightarrow$ $B \subseteq \overline{A} \cap Y$.
>
> $(\subseteq)$ $B$ closed in $Y$ $\Rightarrow$ $B = C \cap Y$, where $C$ is closed in $X$, and $C \supseteq A$ since $B \supseteq A$. Since $\overline{A}$ is the intersection of all such closed sets, $\overline{A} \subseteq C$, thus $\overline{A} \cap Y \subseteq C \cap Y = B$.

^pf-7-2

*Uses:* [[§6 Closed Sets and Limit Points#^thm-6-2|§6.2]]

> [!example] Example §7.2
> $Y = (0, 1] \subseteq \mathbb{R}$. Let $A = (0, \frac{1}{2}) \subseteq Y$.
>
> The closure of $A$ in $\mathbb{R}$ is $[0, \frac{1}{2}]$.
>
> The closure of $A$ in $Y$ is $[0, \frac{1}{2}] \cap Y = (0, \frac{1}{2}]$.

^ex-7-2

## Neighborhoods

> [!definition] Definition §7.2: Intersects and Neighborhood
> We say a set $A$ **intersects** a set $B$ if $A \cap B \neq \emptyset$.
>
> If $U \subseteq X$ is an open set containing $x \in X$, we say “$U$ is a **neighborhood** of $x$”.

^def-7-2

> [!example] Example §7.3
> $(-\varepsilon, \varepsilon)$ is a neighborhood of $0$ in $\mathbb{R}$.

^ex-7-3

## Closure via Neighborhoods

> [!theorem] Theorem §7.3: Closure Characterization
> Let $A \subseteq X$ be a subset of a topological space. Then $x \in \overline{A}$ if and only if every neighborhood of $x$ intersects $A$.

^thm-7-3

> [!proof]+ Proof
> $(\Leftarrow)$ If $x \notin \overline{A}$, then $x \in X \setminus \overline{A}$, which is open in $X$ (since $\overline{A}$ is closed). So $X \setminus \overline{A}$ is a neighborhood of $x$ that doesn't intersect $A$. Equivalently, if every neighborhood of $x$ intersects $A$, then $x \in \overline{A}$.
>
> $(\Rightarrow)$ Conversely, suppose there exists a neighborhood $U$ of $x$ such that $U \cap A = \emptyset$. Then $X \setminus U$ is a closed set containing $A$. By definition of $\overline{A}$, $X \setminus U$ must contain $\overline{A}$. But we know $x \in U$, so $x \notin \overline{A}$.

^pf-7-3

> [!remark]- Connections
> - Used in [[Equivalent Conditions for Continuity|Equivalent Conditions for Continuity]] and [[§7 Interior and Closure#^thm-7-4|Closure and Limit Points]].

## Limit Points

> [!definition] Definition §7.3: Limit Point
> Let $A \subseteq X$, where $X$ is a topological space, and let $x \in X$. We say $x$ is a **limit point** (or **accumulation point**, **cluster point**) of $A$ if every neighborhood of $x$ intersects $A$ in some point other than $x$. That is, $x$ is a limit point if $x \in \overline{A \setminus \{x\}}$.

^def-7-3

> [!remark]- Connections
> - Compactness via limit points: [[§16 Limit Point Compactness#^def-16-1|Limit Point Compact]].
> - Computational version: [[§12★ Regions in the Complex Plane#^def-12-6|342 Def. §12.6]] (accumulation points in the complex plane, via deleted neighborhoods); a singular point that is a limit point of other singular points, so not isolated: [[§74 Isolated Singular Points#^ex-74-3|342 Ex. §74.3]].

> [!example] Example §7.4
> In $\mathbb{R}$, let $B = \{\frac{n+1}{n} \mid n \in \mathbb{Z}_+\}$. What are the limit points of $B$?
>
> $1 \in \mathbb{R}$ is a limit point.

^ex-7-4

![[m590-7-2.svg]]
*$B = \{\tfrac{n+1}{n}\} = \{2, \tfrac32, \tfrac43, \ldots\}$ (blue) piles up at $1$. Every neighborhood $(1-\varepsilon,1+\varepsilon)$ of $1$ (red) contains infinitely many points of $B$, so $1$ is a limit point even though $1\notin B$. A point like $\tfrac32$ is isolated: a small interval around it (blue) meets $B$ only in $\tfrac32$. So $B' = \{1\}$ and $\overline{B} = B \cup \{1\}$.*

> [!example] Example §7.5
> $A = (0,1)$: What are the limit points? Every point in $[0,1]$ is a limit point of $A$.

^ex-7-5

> [!example] Example §7.6
> $\mathbb{Q} \subseteq \mathbb{R}$? Any $x \in \mathbb{R}$! Because $\mathbb{Q}$ is dense in $\mathbb{R}$. $(x - \varepsilon, x + \varepsilon)$ contains some $q \in \mathbb{Q}$.

^ex-7-6

> [!remark]- Connections
> - MATH 451: [[§4 The Completeness Axiom#^thm-4-7|Density of ℚ in ℝ]].
> - Density in general spaces: [[§18 Countability Axioms#^def-18-4|Dense]].

> [!theorem] Theorem §7.4: Closure and Limit Points
> Let $A \subseteq X$ be a subset of a topological space. Let $A'$ = set of all limit points of $A$. Then $\overline{A} = A \cup A'$.

^thm-7-4

> [!proof]+ Proof
> $(\supseteq)$ If $x \in A'$, then every neighborhood of $x$ intersects $A$. $\Rightarrow$ $x \in \overline{A}$. If $x \in A \Rightarrow x \in \overline{A}$. ✓
>
> $(\subseteq)$ Let $x \in \overline{A}$. If $x \in A$, then done. If $x \notin A$, then every neighborhood of $x$ intersects $A$ (since $x \in \overline{A}$), and that intersected point is not $x$, so $x \in A'$. ✓

^pf-7-4

*Uses:* [[§7 Interior and Closure#^thm-7-3|§7.3]], [[§7 Interior and Closure#^lem-7-1|§7.1]]

> [!theorem] Corollary §7.5
> $A \subseteq X$ (topological space) is closed if and only if $A$ contains all of its limit points.

^cor-7-5

> [!proof]+ Proof
> $A$ closed $\Leftrightarrow$ $A = \overline{A} \Leftrightarrow A \supseteq A'$.

^pf-7-5

*Uses:* [[§7 Interior and Closure#^lem-7-1|§7.1]], [[§7 Interior and Closure#^thm-7-4|§7.4]]

> [!remark]- Connections
> - MATH 451 version: [[§13 Some Topological Concepts in Metric Spaces#^prop-13-5|Sequential Characterization of Closedness]].
> - Computational version: [[§12★ Regions in the Complex Plane#^thm-12-2|342 Thm. §12.2]] (the same criterion for sets in the complex plane, with worked examples).

> [!example] Example §7.7: Strange Behavior
> $X = \{a, b, c\}$ with topology $\{\{b\}, \{a,b\}, \{b,c\}, X, \emptyset\}$. Note $\{b\}$ is not closed (its complement $\{a,c\}$ is not open).

^ex-7-7

## Convergence of Sequences

> [!definition] Definition §7.4: Convergence
> Let $\{x_n\}$ be a sequence of points in $X$. We say $x_n \to x$ (“$x_n$ converges to $x$”) if for every neighborhood $U$ of $x$, there is some $N \in \mathbb{Z}$ such that $x_n \in U$ for all $n \geq N$.

^def-7-4

> [!remark]- Connections
> - MATH 451 version: [[§7 Limits of Sequences#^def-7-2|Convergence of a Sequence]], [[§13 Some Topological Concepts in Metric Spaces#^def-13-2|Convergence in a Metric Space]].
> - In metric spaces: [[§11 Metric Topology#^lem-11-8|Sequence Lemma]], [[§11 Metric Topology#^thm-11-9|Continuity and Sequences]].

> [!example] Example §7.8
> $x_n = b \to a, b, c$ in the space $X = \{a,b,c\}$ [[§7 Interior and Closure#^ex-7-7|above]], since every neighborhood of $a$ contains $b$, same for $b$ and $c$.

^ex-7-8

![[m590-7-3.svg]]
*The space of Examples §7.7–7.8. Its open sets are $\emptyset$, $\{b\}$ (red), $\{a,b\}$, $\{b,c\}$ (blue) and $X$. Every nonempty open set contains $b$, so the constant sequence $x_n = b$ lies in every neighborhood of $a$, of $b$ and of $c$, and it converges to all three. Also, $\{a,c\}$ is not among the open sets, so $\{b\}$ is not closed.*

> [!remark]- Connections
> - Contrast: [[§8 Hausdorff Spaces#^thm-8-3|Unique Limits in Hausdorff Spaces]].
