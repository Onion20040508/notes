---
type: section
subject: "[[Topology]]"
chapter: 6
section: 19
munkres: "§31"
tags: [topology, math590]
---
← [[§18 Countability Axioms]] · ↑ [[· 6 Countability and Separation]] · [[§20 Normal Spaces]] →

## The Separation Hierarchy

> [!definition] Definition §19.1: $T_1$ Axiom
> $X$ is **$T_1$** if single-point sets $\{x\}$ are closed for all $x \in X$.

^def-19-1

> [!remark]- Connections
> - First met in [[§8 Hausdorff Spaces#^prop-8-2|§8.2 (T₁ Axiom)]], where [[§8 Hausdorff Spaces#^thm-8-1|Finite Point Sets are Closed in Hausdorff Spaces]] shows Hausdorff $\Rightarrow$ $T_1$.

> [!definition] Definition §19.2: Regular
> $X$ is **regular** if $X$ is [[§19 Separation Axioms#^def-19-1|T₁]] and for each pair of a point $x \in X$ and a closed set $B$ with $x \notin B$, there exist disjoint open sets $U \ni x$ and $V \supseteq B$.

^def-19-2

> [!definition] Definition §19.3: Normal
> $X$ is **normal** if $X$ is [[§19 Separation Axioms#^def-19-1|T₁]] and for each pair of disjoint closed sets $A$ and $B$, there exist disjoint open sets $U \supseteq A$ and $V \supseteq B$.

^def-19-3

![[m590-19-1.svg]]
*The separation hierarchy. Dashed curves are open sets, solid-bordered regions are closed sets. $T_1$: every $y\ne x$ has a neighborhood $V_y$ missing $x$, which is the same as $\{x\}$ being closed. Hausdorff: two points get disjoint neighborhoods. Regular: a point and a closed set $B$ do. Normal: two disjoint closed sets $A,B$ do.*

> [!remark] Remark: Why $T_1$ is Part of the Definition
> The $T_1$ axiom (singletons are closed) is *built into* the definitions of regular and normal. This is Munkres's convention, and it is essential: without $T_1$, the implications [[§19 Separation Axioms#^thm-19-1|Normal ⇒ Regular ⇒ Hausdorff]] would fail. For example, the separation property for closed sets is vacuously easy in the [[§1 Topological Spaces#^ex-1-2|indiscrete topology]] (the only closed sets are $\emptyset$ and $X$, so there are no nontrivial disjoint closed sets to separate), but the indiscrete topology is not even [[§8 Hausdorff Spaces#^def-8-1|Hausdorff]]. Including $T_1$ prevents such degeneracies.

^rem-19-1

> [!remark] Remark: Why the Separation Hierarchy Matters
> The separation axioms answer a fundamental question: *how well can we separate things with open sets?* The hierarchy $T_1 \Leftarrow$ Hausdorff $\Leftarrow$ Regular $\Leftarrow$ Normal represents increasing levels of “niceness”:
> - $T_1$: points are closed (minimal decency).
> - Hausdorff: distinct points have disjoint neighborhoods ([[§8 Hausdorff Spaces#^thm-8-3|unique limits]]).
> - Regular: a point and a closed set can be separated (stronger local behavior).
> - Normal: two disjoint closed sets can be separated (the threshold for powerful theorems).
>
> Normality is the gateway to the deepest results in point-set topology: **[[§20 Normal Spaces#^rem-20-3|Urysohn's Lemma]]** (disjoint closed sets can be separated by a continuous function $f: X \to [0,1]$) and the **[[§20 Normal Spaces#^rem-20-3|Tietze Extension Theorem]]** (continuous functions on closed subsets extend to the whole space). These, in turn, lead to the [[§18 Countability Axioms#^thm-18-1|Urysohn metrization theorem]]. These implications are strict — each level genuinely adds power: the cofinite topology on $\mathbb{R}$ is $T_1$ but not Hausdorff ([[§8 Hausdorff Spaces#^prop-8-2|§8.2]]), $\mathbb{R}_K$ is Hausdorff but not regular ([[§19 Separation Axioms#^ex-19-1|Example §19.1]] below), and $\mathbb{R}_\ell \times \mathbb{R}_\ell$ is regular but not normal (a standard example, Munkres §31; not proved here).

^rem-19-2

> [!theorem] Theorem §19.1: Separation Hierarchy
> $$
> \text{Normal} \Rightarrow \text{Regular} \Rightarrow \text{Hausdorff} \Rightarrow T_1
> $$
>
> None of the reverse implications holds in general.

^thm-19-1

> [!proof]+ Proof
> **Normal $\Rightarrow$ Regular:** Let $x \in X$ and $B$ be a closed set with $x \notin B$. Since $X$ is normal, it is $T_1$ by definition, so $\{x\}$ is closed. Now $\{x\}$ and $B$ are disjoint closed sets, so by the normality separation property, there exist disjoint open sets $U \supseteq \{x\}$ and $V \supseteq B$. The $T_1$ property also carries over, so $X$ is regular.
>
> **Regular $\Rightarrow$ Hausdorff:** Given distinct $x, y \in X$. Since $X$ is regular, it is $T_1$ by definition, so $\{y\}$ is closed. Since $x \notin \{y\}$, the regularity separation property gives disjoint open sets separating $x$ and $\{y\}$.
>
> **Hausdorff $\Rightarrow$ $T_1$:** Given $x \in X$, for each $y \neq x$, Hausdorff gives disjoint open $U_y \ni x$ and $V_y \ni y$. Then $X \setminus \{x\} = \bigcup_{y \neq x} V_y$ is open, so $\{x\}$ is closed.

^pf-19-1

*Uses:* [[§19 Separation Axioms#^def-19-1|Def. §19.1]], [[§19 Separation Axioms#^def-19-2|Def. §19.2]], [[§19 Separation Axioms#^def-19-3|Def. §19.3]], [[§8 Hausdorff Spaces#^def-8-1|Def. §8.1]]

> [!remark]- Connections
> - The last step reproves [[§8 Hausdorff Spaces#^thm-8-1|Finite Point Sets are Closed in Hausdorff Spaces]]. Strictness: [[§19 Separation Axioms#^ex-19-1|Example §19.1]] (Hausdorff ⇏ regular); the other two are cited in [[§19 Separation Axioms#^rem-19-2|the remark above]].

> [!remark] Remark
> [[§19 Separation Axioms#^pf-19-1|The proofs]] are not circular: each implication uses the $T_1$ axiom that is *part of the definition* of the stronger property. Normal $\Rightarrow$ Regular uses “$\{x\}$ is closed” (from $T_1$ in the definition of normal) to turn a point-vs-set problem into a set-vs-set problem. Regular $\Rightarrow$ Hausdorff uses “$\{y\}$ is closed” (from $T_1$ in the definition of regular) to turn a point-vs-point problem into a point-vs-set problem.

^rem-19-3

## Examples

> [!example] Example §19.1: $\mathbb{R}_K$ is Hausdorff but Not Regular
> Let $\mathbb{R}_K$ be $\mathbb{R}$ with basis consisting of:
> - Intervals $(a, b)$, and
> - Sets of the form $(a, b) \setminus K$, where $K = \{1/n \mid n \in \mathbb{Z}_+\}$.
>
> $\mathbb{R}_{std}$ is Hausdorff. $\mathbb{R}_K$ is [[§2 Basis for a Topology#^ex-2-5|finer]] than $\mathbb{R}_{std}$ (more open sets), so $\mathbb{R}_K$ is also Hausdorff.
>
> **Claim:** $\mathbb{R}_K$ is not regular.
>
> *Proof:* $K$ is closed in $\mathbb{R}_K$: the complement $\mathbb{R} \setminus K$ is open (it equals $\bigcup_{m \in \mathbb{Z}_+} ((-m, m) \setminus K)$, a union of basis elements).
>
> Consider the point $0 \notin K$. We show there do not exist disjoint open sets $U \ni 0$ and $V \supseteq K$.
>
> Suppose such $U, V$ exist. A basis element containing $0$ and lying in $U$ must be of the form $(a, b) \setminus K$ where $a < 0 < b$ (since any basis element $(a,b)$ containing $0$ would contain points of $K$).
>
> Since $a < 0 < b$, there exists $n$ such that $1/n \in (a, b)$. Since $1/n \in K \subseteq V$, there exists a basis element containing $1/n$ and lying in $V$; it must be of the form $(c, d)$, since the sets $(c,d) \setminus K$ miss $1/n$.
>
> Now find $z \in U \cap V$: choose $z$ with $\max(c, 1/(n+1)) < z < 1/n$.
>
> Then $z \in (c, d)$ so $z \in V$. Also $z \in (a, b)$ and $z \notin K$ (since $z < 1/n$ and $z > 1/(n+1)$), so $z \in (a,b) \setminus K \subseteq U$.
>
> Thus $z \in U \cap V$, contradicting $U \cap V = \emptyset$. So $\mathbb{R}_K$ is not regular. $\square$

^ex-19-1

![[m590-19-2.svg]]
*Why $\mathbb{R}_K$ is not regular: a neighborhood $U$ of $0$ (red) can remove the points of $K=\{\frac1n\}$ (blue dots), but it must contain an interval $(a,b)\setminus K$. Any open $V\supseteq K$ (blue) contains a small interval around each $\frac1n$, and just below $\frac1n$ (here $\frac13$) that interval meets $(a,b)\setminus K$ at a point $z$. So $U\cap V\neq\emptyset$.*

> [!remark]- Connections
> - $\mathbb{R}_K$ is the [[§2 Basis for a Topology#^ex-2-4|K-Topology]] of §2.

> [!example] Example §19.2: $\mathbb{R}_\ell$ is Normal
> $\mathbb{R}_\ell$ ([[§2 Basis for a Topology#^ex-2-3|lower limit topology]], basis $\{[a, b)\}$) is normal.
>
> *Proof:* One-point sets are closed ($\mathbb{R}_\ell$ is [[§2 Basis for a Topology#^ex-2-5|finer]] than $\mathbb{R}_{std}$, so $T_1$).
>
> Let $A, B$ be disjoint closed sets in $\mathbb{R}_\ell$. Then $A = \overline{A}$ and $B = \overline{B}$.
>
> For each $a \in A$, since $a \notin B = \overline{B}$, there exists a basis element $[a, x_a)$ disjoint from $B$.
>
> For each $b \in B$, since $b \notin A = \overline{A}$, there exists a basis element $[b, x_b)$ disjoint from $A$.
>
> Let $U = \bigcup_{a \in A} [a, x_a)$ and $V = \bigcup_{b \in B} [b, x_b)$.
>
> Then $U$ and $V$ are open, $U \supseteq A$, and $V \supseteq B$.
>
> **Claim:** $U \cap V = \emptyset$.
>
> *Proof:* Suppose $z \in U \cap V$. Then $z \in [a, x_a)$ for some $a \in A$ and $z \in [b, x_b)$ for some $b \in B$.
>
> If $a \leq b$: then $b \in [a, x_a)$, but $[a, x_a)$ is disjoint from $B$, contradiction.
>
> If $b < a$: then $a \in [b, x_b)$, but $[b, x_b)$ is disjoint from $A$, contradiction.
>
> Thus $U \cap V = \emptyset$, and $\mathbb{R}_\ell$ is normal. $\square$

^ex-19-2

![[m590-19-3.svg]]
*Normality of $\mathbb{R}_\ell$: each $a\in A$ gets a basis interval $[a,x_a)$ (red) missing $B$, and each $b\in B$ gets $[b,x_b)$ (blue) missing $A$. Every interval must stop before it reaches a point of the other set (dashed: not allowed). So if a red and a blue interval met, the one starting further left would contain the other's left endpoint.*

## Characterization of Regular and Normal Spaces

> [!theorem] Lemma §19.2: Closure Characterization
> Let $X$ be a $T_1$-space (one-point sets are closed).
> - **(a)** $X$ is regular if and only if given $x \in X$ and a neighborhood $U$ of $x$, there exists a neighborhood $V$ of $x$ such that $\overline{V} \subseteq U$.
> - **(b)** $X$ is normal if and only if given a closed set $A$ and an open set $U$ containing $A$, there exists an open set $V$ containing $A$ such that $\overline{V} \subseteq U$.

^lem-19-2

> [!proof]+ Proof
> **(a) $(\Rightarrow)$** Suppose $X$ is regular. Let $x \in X$ and $U$ be a neighborhood of $x$.
>
> $X \setminus U$ is closed and does not contain $x$. By regularity, there exist disjoint open sets $V \ni x$ and $W \supseteq X \setminus U$.
>
> Then $\overline{V} \subseteq X \setminus W$ (since $V \cap W = \emptyset$ implies no point of $W$ is in $\overline{V}$).
>
> Since $W \supseteq X \setminus U$, we have $X \setminus W \subseteq U$, so $\overline{V} \subseteq U$.
>
> **(a) $(\Leftarrow)$** Let $x \in X$ and $B$ be a closed set not containing $x$.
>
> $X \setminus B$ is a neighborhood of $x$. By hypothesis, there exists neighborhood $V$ of $x$ such that $\overline{V} \subseteq X \setminus B$.
>
> The open sets $V$ and $X \setminus \overline{V}$ are disjoint (clearly), $V \ni x$, and $X \setminus \overline{V} \supseteq B$ (since $\overline{V} \subseteq X \setminus B$ means $B \subseteq X \setminus \overline{V}$).
>
> Thus $X$ is regular.
>
> **(b)** Similar, replacing point $x$ with closed set $A$.
>
> **(b) $(\Rightarrow)$** Suppose $X$ is normal. Let $A$ be closed and $U$ be an open set containing $A$.
>
> $X \setminus U$ is closed and disjoint from $A$. By normality, there exist disjoint open sets $V \supseteq A$ and $W \supseteq X \setminus U$.
>
> Then $\overline{V} \subseteq X \setminus W$ (since $V \cap W = \emptyset$). Since $W \supseteq X \setminus U$, we have $X \setminus W \subseteq U$, so $\overline{V} \subseteq U$.
>
> **(b) $(\Leftarrow)$** Let $A, B$ be disjoint closed sets.
>
> $X \setminus B$ is an open set containing $A$. By hypothesis, there exists open $V \supseteq A$ such that $\overline{V} \subseteq X \setminus B$.
>
> The open sets $V$ and $X \setminus \overline{V}$ are disjoint, $V \supseteq A$, and $X \setminus \overline{V} \supseteq B$.
>
> Thus $X$ is normal.

^pf-19-2

*Uses:* [[§19 Separation Axioms#^def-19-2|Def. §19.2]], [[§19 Separation Axioms#^def-19-3|Def. §19.3]], [[§7 Interior and Closure#^thm-7-3|§7.3]]

![[m590-19-4.svg]]
*The closure characterization, (a) for regular and (b) for normal. The open set $W$ (hatched) contains $X\setminus U$ and is disjoint from $V$, so $\overline V$ (red) cannot reach $W$. The result is the nesting $x\in V\subseteq\overline V\subseteq U$ in (a) and $A\subseteq V\subseteq\overline V\subseteq U$ in (b), with $U$ dashed blue.*
