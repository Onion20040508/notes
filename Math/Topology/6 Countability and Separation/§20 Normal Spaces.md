---
type: section
subject: "[[Topology]]"
chapter: 6
section: 20
munkres: "§32"
tags: [topology, math590]
---
← [[§19 Separation Axioms]] · ↑ [[· 6 Countability and Separation]] · [[§21 Algebra Prerequisites꞉ Groups]] →

> [!remark] Remark: The Road Ahead
> [[§19 Separation Axioms#^def-19-3|Normality]] is the key hypothesis for the deepest results in point-set topology. This section establishes that the spaces we care about most — metrizable spaces, compact Hausdorff spaces — are normal. This sets the stage for [[§20 Normal Spaces#^rem-20-3|Urysohn's Lemma]] (separating closed sets by continuous functions) and the [[§20 Normal Spaces#^rem-20-3|Tietze Extension Theorem]].

^rem-20-1

> [!theorem] Theorem §20.1: Every Metrizable Space is Normal
> Every [[§11 Metric Topology#^def-11-4|metrizable]] space is normal.

^thm-20-1

> [!proof]+ Proof
> Let $(X, d)$ be a metrizable space. We first show $X$ is $T_1$: for any $x \in X$, the set $\{x\}$ is closed since $X \setminus \{x\} = \bigcup_{y \neq x} B(y, d(x,y))$ is open.
>
> Now let $A, Z \subseteq X$ be disjoint closed sets.
>
> **Step 1: Choose separating radii.**
>
> For each $a \in A$: since $A \cap Z = \emptyset$, we have $a \notin Z$, so $a \in X \setminus Z$ which is open. Choose $\varepsilon_a > 0$ such that $B(a, \varepsilon_a) \subseteq X \setminus Z$, i.e., $B(a, \varepsilon_a) \cap Z = \emptyset$.
>
> For each $z \in Z$: since $A \cap Z = \emptyset$, we have $z \notin A$, so $z \in X \setminus A$ which is open. Choose $\varepsilon_z > 0$ such that $B(z, \varepsilon_z) \subseteq X \setminus A$, i.e., $B(z, \varepsilon_z) \cap A = \emptyset$.
>
> **Step 2: Construct open sets with half-radii.**
>
> Let
>
> $$
> U = \bigcup_{a \in A} B\!\left(a, \frac{\varepsilon_a}{2}\right), \qquad V = \bigcup_{z \in Z} B\!\left(z, \frac{\varepsilon_z}{2}\right).
> $$
>
> These are open (as unions of open sets), $U \supseteq A$, and $V \supseteq Z$.
>
> **Step 3: Prove $U \cap V = \emptyset$ via the triangle inequality.**
>
> Suppose for contradiction that $w \in U \cap V$. Then $w \in B(a, \varepsilon_a/2)$ for some $a \in A$ and $w \in B(z, \varepsilon_z/2)$ for some $z \in Z$.
>
> By the triangle inequality:
>
> $$
> d(a, z) \leq d(a, w) + d(w, z) < \frac{\varepsilon_a}{2} + \frac{\varepsilon_z}{2}.
> $$
>
> **Case 1:** $\varepsilon_a \leq \varepsilon_z$. Then $d(a, z) < \varepsilon_a/2 + \varepsilon_z/2 \leq \varepsilon_z$. So $a \in B(z, \varepsilon_z)$. But $B(z, \varepsilon_z) \cap A = \emptyset$ and $a \in A$ — contradiction.
>
> **Case 2:** $\varepsilon_z < \varepsilon_a$. Then $d(a, z) < \varepsilon_a/2 + \varepsilon_z/2 < \varepsilon_a$. So $z \in B(a, \varepsilon_a)$. But $B(a, \varepsilon_a) \cap Z = \emptyset$ and $z \in Z$ — contradiction.
>
> Thus $U \cap V = \emptyset$, and $(X, d)$ is normal.

^pf-20-1

*Uses:* [[§19 Separation Axioms#^def-19-3|Def. §19.3]], [[§11 Metric Topology#^def-11-1|Def. §11.1]], [[§11 Metric Topology#^def-11-3|Def. §11.3]]

![[m590-20-1.svg]]
*The half-radius trick: $B(a,\varepsilon_a)$ misses $Z$ and $B(z,\varepsilon_z)$ misses $A$ (dashed), so $d(a,z)\ge\max(\varepsilon_a,\varepsilon_z)$. The half-balls (solid) have radii adding up to at most $\max(\varepsilon_a,\varepsilon_z)$, so they cannot meet. $U$ and $V$ are the unions of all red and all blue half-balls.*

> [!remark] Remark: Why Half-Radii?
> Using $\varepsilon_a/2$ and $\varepsilon_z/2$ instead of $\varepsilon_a$ and $\varepsilon_z$ is the key trick. With full radii, $U$ and $V$ could overlap: a point near the boundary of $B(a, \varepsilon_a)$ might also be near $Z$. Halving the radii creates a “buffer zone” that the triangle inequality exploits. This is the same idea behind the proof that metric spaces are Hausdorff ([[§11 Metric Topology#^thm-11-4|Theorem §11.4]]), scaled up from points to closed sets.

^rem-20-2

> [!theorem] Theorem §20.2: Every Compact Hausdorff Space is Normal
> Every compact Hausdorff space is normal.

^thm-20-2

> [!proof]+ Proof
> Let $X$ be compact Hausdorff. Since $X$ is Hausdorff, [[§8 Hausdorff Spaces#^thm-8-1|one-point sets are closed]], so $X$ is $T_1$.
>
> Now let $A, B \subseteq X$ be disjoint closed sets. We must find disjoint open sets separating them. The proof proceeds in two stages, each using the same “compact Hausdorff separation” argument from [[Compact Subspace of a Hausdorff Space is Closed|Theorem §15.4]] (compact $\subseteq$ Hausdorff $\Rightarrow$ closed).
>
> **Stage 1: Separate a point from a closed set.** Fix $a \in A$. For each $b \in B$, since $X$ is Hausdorff and $a \neq b$, choose disjoint open sets $U_b \ni a$ and $V_b \ni b$. The collection $\{V_b\}_{b \in B}$ covers $B$. Since $B$ is closed in the compact space $X$, $B$ is [[Closed Subspace of a Compact Space is Compact|compact]]. Extract a finite subcover $V_{b_1}, \ldots, V_{b_n}$.
>
> Let $U_a = \bigcap_{i=1}^{n} U_{b_i}$ and $V_a = \bigcup_{i=1}^{n} V_{b_i}$. Then:
> - $U_a$ is open (finite intersection), $V_a$ is open (union).
> - $a \in U_a$ and $B \subseteq V_a$.
> - $U_a \cap V_a = \emptyset$: if $z \in V_a$, then $z \in V_{b_i}$ for some $i$, and $U_a \subseteq U_{b_i}$, so $z \notin U_a$ (since $U_{b_i} \cap V_{b_i} = \emptyset$).
>
> So for each $a \in A$, we have an open $U_a \ni a$ and an open $V_a \supseteq B$ with $U_a \cap V_a = \emptyset$.
>
> **Stage 2: Separate $A$ from $B$.** The collection $\{U_a\}_{a \in A}$ covers $A$. Since $A$ is closed in a compact space, $A$ is [[Closed Subspace of a Compact Space is Compact|compact]]. Extract a finite subcover $U_{a_1}, \ldots, U_{a_m}$.
>
> Let $U = \bigcup_{j=1}^{m} U_{a_j}$ and $V = \bigcap_{j=1}^{m} V_{a_j}$. Then:
> - $U$ is open (union), $V$ is open (finite intersection).
> - $A \subseteq U$ and $B \subseteq V$ (since $B \subseteq V_{a_j}$ for each $j$).
> - $U \cap V = \emptyset$: if $z \in U$, then $z \in U_{a_j}$ for some $j$, and $V \subseteq V_{a_j}$, so $z \notin V$ (since $U_{a_j} \cap V_{a_j} = \emptyset$).
>
> Thus $X$ is normal.

^pf-20-2

*Uses:* [[§8 Hausdorff Spaces#^thm-8-1|§8.1]], [[§15 Compact Spaces#^lem-15-1|§15.1]], [[§15 Compact Spaces#^thm-15-2|§15.2]], [[§15 Compact Spaces#^thm-15-4|§15.4]], [[§19 Separation Axioms#^def-19-3|Def. §19.3]]

![[m590-20-2.svg]]
*Stage 2 of the proof. Stage 1 gave, for each $a\in A$, disjoint open sets $U_a\ni a$ and $V_a\supseteq B$. Finitely many $U_{a_j}$ (red dashed) cover $A$. Their union is $U$ (red), and the intersection of the matching $V_{a_j}$ (blue dashed) is $V$ (blue). Each $V_{a_j}$ may meet the other $U$'s, like $V_{a_1}$ meeting $U_{a_2}$, but $V$ lies inside every $V_{a_j}$ and so misses all of $U$.*

> [!remark] Remark: Not Covered: Urysohn's Lemma and Tietze Extension
> Normality is the hypothesis for two deep results in Munkres §33–35 that were **not covered in this course**:
> - **Urysohn's Lemma:** If $X$ is normal and $A, B$ are disjoint closed sets, there exists a continuous $f: X \to [0,1]$ with $f(A) = \{0\}$, $f(B) = \{1\}$. (Upgrades separation by open sets to separation by a continuous function.)
> - **Tietze Extension Theorem:** If $X$ is normal and $A \subseteq X$ is closed, any continuous $f: A \to [a,b]$ extends to $F: X \to [a,b]$ with $F|_A = f$.
>
> These lead to the **[[§18 Countability Axioms#^thm-18-1|Urysohn Metrization Theorem]]**: [[§19 Separation Axioms#^def-19-2|regular]] + [[§18 Countability Axioms#^def-18-3|second-countable]] $\Rightarrow$ metrizable. This is why the course established normality of [[§20 Normal Spaces#^thm-20-1|metrizable]] and [[§20 Normal Spaces#^thm-20-2|compact Hausdorff]] spaces — they are the natural domain for these results.

^rem-20-3

> [!remark] Remark: The Two-Stage Pattern
> Both proofs of normality ([[§20 Normal Spaces#^pf-20-1|metrizable]] and [[§20 Normal Spaces#^pf-20-2|compact Hausdorff]]) follow the same template: start with a local separation (point-by-point), then patch to a global separation (for the whole closed set). The difference is the patching mechanism:
> - **Metrizable:** half-radii + triangle inequality ensure disjointness.
> - **Compact Hausdorff:** compactness provides finite subcovers, and the $\bigcap$/$\bigcup$ trick preserves disjointness.
>
> The compact Hausdorff proof uses the same technique as [[Compact Subspace of a Hausdorff Space is Closed|Theorem §15.4]] (compact $\subseteq$ Hausdorff $\Rightarrow$ closed) *twice* — once to separate a point from $B$, once to separate $A$ from $B$. Each stage replaces a single point with a compact set by extracting a finite subcover and taking intersections.

^rem-20-4

> [!remark]- Connections
> - A use of Tietze in measure theory: the continuous restriction to a closed set in Lusin's theorem extends to a continuous function on all of ℝⁿ, [[§13 Egorov's and Lusin's Theorems#^thm-13-3|551 Thm. §13.3]].
