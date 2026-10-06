---
type: section
subject: "[[Group Theory]]"
chapter: 6
section: 24
tags: [group-theory, math493]
---
← [[§23 S₃, Aₙ, Uₙ and GLₙ]] · ↑ [[· 6 Group Actions, Cosets, and Lagrange's Theorem]] · [[§25 Actions]] →

*Reference: Pinter Ch. 12.*

The goal is to decompose a group $G$ into disjoint subsets, given a subgroup $H$ — extending the decomposition of $\mathbb{Z}$ into congruence classes modulo $n$ ([[§6 Divisibility and Congruence#^prop-6-2|§6.2]]), which is the case $G = \mathbb{Z}$, $H = n\mathbb{Z}$. The framework is that of equivalence relations.

> [!definition] Definition §24.1: Equivalence Relation
> A **relation** $\sim$ on a set $X$ is a subset of $X \times X$; we write $x \sim y$ when the pair lies in it. The relation is an **equivalence relation** if it is
> 1. **reflexive:** $x \sim x$ for all $x \in X$;
> 2. **symmetric:** $x \sim y \implies y \sim x$;
> 3. **transitive:** $x \sim y$ and $y \sim z$ $\implies$ $x \sim z$.
>
> The basic example is equality. Order relations ($\leq$ on $\mathbb{Z}$, or divisibility) are typically *not* equivalence relations, failing symmetry.

^def-24-1

> [!remark]- Connections
> - MATH 590 uses equivalence relations to build quotient spaces: [[§12 Quotient Topology#^def-12-3|Quotient Space]] (590 Def. §12.3).
> - Group-theoretic instances: [[§27 Orbits#^prop-27-2|The Orbit Relation]], [[§28 Left and Right Cosets#^def-28-1|Congruence Modulo a Subgroup]].
> - Same definition: [[§22 Partitions and Equivalence Relations#^def-22-3|250 Def. §22.3]], with relations as subsets of $X \times X$ in [[§22 Partitions and Equivalence Relations#^def-22-2|250 Def. §22.2]].

> [!definition] Definition §24.2: Equivalence Class
> Given an equivalence relation $\sim$ on $X$ and $x \in X$, the **equivalence class** of $x$ is
>
> $$
> R_x := \{ y \in X : x \sim y \} \ni x.
> $$

^def-24-2

> [!remark]- Connections
> - Same definition: [[§22 Partitions and Equivalence Relations#^def-22-4|250 Def. §22.4]] (which also names the quotient set).

> [!definition] Definition §24.3: Partition
> A **partition** of a set $X$ is a collection of nonempty subsets of $X$, the **parts**, such that every element of $X$ lies in exactly one part; equivalently, $X$ is the disjoint union of the parts, written $X = \bigsqcup_{i \in I} X_i$.

^def-24-3

> [!remark]- Connections
> - Same definition: [[§22 Partitions and Equivalence Relations#^def-22-1|250 Def. §22.1]].

> [!theorem] Proposition §24.1: Equivalence Classes Partition a Set
> Let $\sim$ be an equivalence relation on $X$. Then
> 1. for $x_1, x_2 \in X$: $R_{x_1} \cap R_{x_2} \neq \varnothing \iff R_{x_1} = R_{x_2} \iff x_1 \sim x_2$;
> 2. $\bigcup_{x \in X} R_x = X$.
>
> Hence the distinct equivalence classes form a partition of $X$.

^prop-24-1

> [!proof]+ Proof
> **(1)** Suppose $y \in R_{x_1} \cap R_{x_2}$, so $x_1 \sim y$ and $x_2 \sim y$; by symmetry and transitivity, $x_1 \sim x_2$. Given $x_1 \sim x_2$, if $z \in R_{x_2}$ then $x_2 \sim z$, so $x_1 \sim z$ by transitivity and $z \in R_{x_1}$; the reverse inclusion follows by symmetry. Finally if $R_{x_1} = R_{x_2}$ then the intersection contains $x_1$, hence is nonempty. **(2)** $x \in R_x$ by reflexivity.

^pf-24-1

*Uses:* [[§24 Equivalence Relations and Partitions#^def-24-1|Def. §24.1]], [[§24 Equivalence Relations and Partitions#^def-24-2|Def. §24.2]], [[§24 Equivalence Relations and Partitions#^def-24-3|Def. §24.3]]

![[m493-22-1.svg]]
*Proposition §24.1: the equivalence classes cut $X$ into disjoint pieces. If $x_1 \sim x_2$, their classes coincide (blue); a point $x_3$ not related to $x_1$ has a class (red) disjoint from it. No two classes partially overlap, and every point lies in its own class.*

> [!remark]- Connections
> - The same pattern in linear algebra: [[§11 Products and Quotients of Vector Spaces#^ladr-3-101|Two translates of a subspace are equal or disjoint]] (LADR 3.101); in MATH 590: [[§12 Quotient Topology#^def-12-3|Quotient Space]] (590 Def. §12.3).
> - Applied to orbits and cosets: [[§27 Orbits#^prop-27-2|The Orbit Relation]], [[§28 Left and Right Cosets#^prop-28-2|Cosets Are the Equivalence Classes]].
> - Elementary version: [[§22 Partitions and Equivalence Relations#^thm-22-3|250 Thm. §22.3]] (classes are equal or disjoint) and [[§22 Partitions and Equivalence Relations#^cor-22-4|250 Cor. §22.4]].

> [!theorem] Proposition §24.2: Partitions Come from Equivalence Relations
> Every partition $X = \bigsqcup_{i \in I} X_i$ arises from a unique equivalence relation, namely “$x \sim y$ iff $x$ and $y$ lie in the same part.” So specifying an equivalence relation on $X$ and specifying a partition of $X$ are the same thing.

^prop-24-2

> [!proof]+ Proof
> The relation is reflexive (each $x$ lies in some part), symmetric (visibly), and transitive (if $x, y$ share a part and $y, z$ share a part, the two parts both contain $y$, hence coincide, the parts being disjoint). Its classes are the parts. It is the only such relation, because an equivalence relation is determined by its classes: $x \sim y$ iff $y$ lies in the class of $x$.

^pf-24-2

*Uses:* [[§24 Equivalence Relations and Partitions#^def-24-1|Def. §24.1]], [[§24 Equivalence Relations and Partitions#^def-24-2|Def. §24.2]], [[§24 Equivalence Relations and Partitions#^def-24-3|Def. §24.3]]

> [!remark]- Connections
> - Elementary version: [[§22 Partitions and Equivalence Relations#^prop-22-2|250 Prop. §22.2]] (a partition gives an equivalence relation) and [[§22 Partitions and Equivalence Relations#^cor-22-4|250 Cor. §22.4]] (the two constructions are mutually inverse).
