---
type: section
subject: "[[Topology]]"
chapter: 2
section: 8
tags: [topology, math590]
---
← [[Topology §7 Interior and Closure]] · ↑ [[Topology — 2 Closedness, Continuity, and Hausdorff]] · [[Topology §9 Continuous Functions]] →

> [!definition] Definition §8.1: Hausdorff Space
> A topological space $X$ is called **Hausdorff** (or $T_2$) if for each pair $x_1$ and $x_2$ of distinct points in $X$, there exist neighborhoods $U_1$ of $x_1$ and $U_2$ of $x_2$ that are disjoint.

^def-8-1

![[m590-8-1.svg]]
*Hausdorff separation: the distinct points $x_1, x_2$ sit in neighborhoods $U_1$ (blue) and $U_2$ (red) that do not meet (dashed boundaries: the sets are open). In the cofinite topology this picture cannot be drawn: two nonempty open sets have finite complements, so they always intersect.*

> [!remark]- Connections
> - Every metric space is Hausdorff: [[Topology §11 Metric Topology#^thm-11-4|Every Metric Space is Hausdorff]].
> - Stronger separation axioms: [[Topology §19 Separation Axioms#^thm-19-1|Separation Hierarchy]].

> [!remark] Remark: Why Hausdorff is the “Reasonable” Separation Axiom
> The Hausdorff property is the minimal assumption that makes a topological space behave like what we expect from analysis:
> - **[[Topology §8 Hausdorff Spaces#^thm-8-3|Unique limits]]:** sequences (and nets) converge to at most one point.
> - **[[Topology §8 Hausdorff Spaces#^thm-8-1|Points are closed]]:** single-point sets $\{x\}$ are closed ($T_1$).
> - **Compact subsets are closed:** compact $\subseteq$ Hausdorff $\Rightarrow$ closed ([[Compact Subspace of a Hausdorff Space is Closed|Theorem §15.4]]).
> - **[[Bijection from Compact to Hausdorff is a Homeomorphism|Bijections behave]]:** continuous bijections from compact to Hausdorff are homeomorphisms.
>
> Without Hausdorff, pathologies arise: in the cofinite topology on $\mathbb{R}$, every sequence with distinct terms converges to *every* point. Most spaces in practice are Hausdorff ([[Topology §11 Metric Topology#^thm-11-4|metric spaces]], manifolds, CW complexes), and the separation axiom hierarchy ([[Topology §19 Separation Axioms|Section 19]]) refines this further.

^rem-8-1

> [!example] Example §8.1
> In $\mathbb{R}$: Given $x \neq y$, take $U_x = (x - \varepsilon, x + \varepsilon)$ and $U_y = (y - \varepsilon, y + \varepsilon)$ where $\varepsilon = \frac{|x-y|}{3}$. These are disjoint.
>
> Counter-example: The cofinite topology on $\mathbb{R}$ is not Hausdorff.

^ex-8-1

> [!theorem] Theorem §8.1: Finite Point Sets are Closed in Hausdorff Spaces
> Every finite point set in a Hausdorff space is closed.

^thm-8-1

> [!proof]+ Proof
> It suffices to show every one-point set $\{x_0\}$ is closed. Show $X \setminus \{x_0\}$ is open. Let $y \in X \setminus \{x_0\}$. Since $X$ is Hausdorff, there exist disjoint neighborhoods $U_x$ of $x_0$ and $U_y$ of $y$ with $U_x \cap U_y = \emptyset$. $\Rightarrow$ $X \setminus \{x_0\} = \bigcup_{y \in X \setminus \{x_0\}} U_y$ is a union of open sets $\Rightarrow$ open.
>
> (Note: each $U_y \subseteq X \setminus \{x_0\}$, and each $y \in X \setminus \{x_0\}$ is in $U_y$ as well.)

^pf-8-1

*Uses:* [[Topology §6 Closed Sets and Limit Points#^thm-6-1|§6.1]]

> [!theorem] Proposition §8.2: $T_1$ Axiom
> Let $X$ be a topological space in which finite point sets are closed. We say $X$ satisfies the $T_1$ axiom.
>
> By [[Topology §8 Hausdorff Spaces#^thm-8-1|the theorem]], Hausdorff $\Rightarrow$ $T_1$ axiom, but not vice versa (e.g., cofinite topology on $\mathbb{R}$).

^prop-8-2

> [!remark]- Connections
> - Restated in the separation axioms: [[Topology §19 Separation Axioms#^def-19-1|T₁ Axiom]], [[Topology §19 Separation Axioms#^rem-19-1|Why T₁ is Part of the Definition]].

> [!theorem] Theorem §8.3: Unique Limits in Hausdorff Spaces
> If $X$ is a Hausdorff space, then a sequence of points of $X$ must converge to at most one point of $X$.

^thm-8-3

> [!proof]+ Proof
> Let $x_n \to x$. If $y \neq x$, take $U_x, U_y$ neighborhoods of $x, y$ disjoint. Since $U_x$ contains all $x_n$ with $n \geq N_1$ for some $N_1$, but if $U_y$ also contains $x_n$ with $n \geq N_2$ for some $N_2$, then $U_x, U_y$ contains all points where $n \geq \max\{N_1, N_2\}$, contradiction.

^pf-8-3

![[m590-8-2.svg]]
*Why a limit is unique: from $N_1$ on, the whole tail of $(x_n)$ is trapped in $U_x$ (blue). Since $U_x \cap U_y = \varnothing$, no tail is left to enter $U_y$ (red), so $x_n \not\to y$. Only finitely many early terms, like $x_1, x_2$, lie outside $U_x$.*

> [!remark]- Connections
> - MATH 451 version: [[Single Variable Analysis §7 Limits of Sequences#^thm-7-1|Uniqueness of Limits]].
> - Fails without Hausdorff: [[Topology §7 Interior and Closure#^ex-7-8|Example §7.8]].
