---
type: section
subject: "[[Functional Analysis]]"
chapter: 2
section: 3
tags: [functional-analysis, math556]
---
← [[§2 Linear Maps, Convexity, and Linear Functionals]] · ↑ [[· 2 The Hahn–Banach Theorem]] · [[§4 Proof of the Hahn–Banach Theorem]] →

*Stage: algebra — Thread: functionals. The extension problem, with $\ell$ dominated by a positive homogeneous subadditive $p$.*

## Positive Homogeneous Subadditive Functions

> [!definition] Definition §3.1: Positive Homogeneous; Subadditive
> Let $X$ be a linear space over $\mathbb{R}$. A function $p : X \to \mathbb{R}$ is
> - (1) **positive homogeneous** if $p(ax) = a\,p(x)$ for all $a \geq 0$ and all $x \in X$;
> - (2) **subadditive** if $p(x + y) \leq p(x) + p(y)$ for all $x, y \in X$.
>
> *Lax: §3.1, conditions (1)–(2) of Thm 1*

^def-3-1

> [!remark]- Connections
> - Norms have both properties, with $|a|$ for every scalar: [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-2|551 Def. §19.2]]; in this course [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], compared with these functions in [[§8 Normed Linear Spaces#^rem-8-2|Relation to Chapter 2]].
> - The complex-homogeneous version: [[§7 The Complex Hahn–Banach Theorem#^thm-7-1|§7.1]], [[§7 The Complex Hahn–Banach Theorem#^lem-7-2|§7.2]].

> [!remark] Remark
> Positive homogeneity only involves scalars $a \geq 0$: multiplying $x$ by a non-negative real number pulls that number out of $p$. Nothing is said about negative scalars, and $p$ is *not* required to be non-negative. (For a norm, non-negativity is part of the definition; here it is not assumed.)

^rem-3-1

> [!theorem] Lemma §3.1: $p(0) = 0$
> If $p : X \to \mathbb{R}$ is positive homogeneous, then $p(0) = 0$.

^lem-3-1

> [!proof]+ Proof
> Take any $x \in X$. Positive homogeneity with $a = 0$ (allowed, since $a \ge 0$) gives
>
> $$
> p(0) = p(0 \cdot x) = 0 \cdot p(x) = 0.
> $$

^pf-3-1

*Uses:* [[§3 Statement and Motivation#^def-3-1|Def. §3.1]]

> [!remark] Remark: Comparison with Lax
> Lax requires $p(ax) = a\,p(x)$ only for $a > 0$. The two definitions agree: for $a > 0$ alone, $p(0) = p(2 \cdot 0) = 2p(0)$ gives $p(0) = 0$, which is the case $a = 0$.

^rem-3-2

Subadditivity is not needed. Note also that the argument uses $p(x) \in \mathbb{R}$: the product $0 \cdot p(x)$ is $0$ only because $p(x)$ is a finite number, which is why the gauge later must first be shown finite ([[§5 Convex Sets and the Gauge#^prop-5-3|§5.3]]).

> [!example] Example §3.1: Three Examples on $\mathbb{R}^n$
> On $X = \mathbb{R}^n$, the following are positive homogeneous and subadditive:
> - (a) $p_1(x) = \Bigl(\sum_{i=1}^n x_i^2\Bigr)^{1/2} = \|x\|$, the Euclidean length. For $a \geq 0$,
>
>   $$
>   p_1(ax) = \Bigl(\sum_{i=1}^n a^2 x_i^2\Bigr)^{1/2} = a\,\|x\|,
>   $$
>
>   and $\|x + y\| \leq \|x\| + \|y\|$ is the [[Triangle inequality|triangle inequality]].
> - (b) $p_2(x) = \max_{1 \leq i \leq n} |x_i|$. For $a \geq 0$, $\max_i |a x_i| = a \max_i |x_i|$; and $|x_i + y_i| \leq |x_i| + |y_i| \leq p_2(x) + p_2(y)$ for each $i$, so $p_2(x + y) \leq p_2(x) + p_2(y)$.
> - (c) $p_3(x) = |x_1| + \cdots + |x_n|$. For $a \geq 0$, $\sum_i |a x_i| = a \sum_i |x_i|$; and $\sum_i |x_i + y_i| \leq \sum_i (|x_i| + |y_i|) = p_3(x) + p_3(y)$.
>
> Each of these is in fact a norm, so a positive homogeneous subadditive function is “like a norm.” Norms will be introduced later ([[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]]); for now only these two properties are needed.

^ex-3-1

> [!remark]- Connections
> - The same three norms on $\mathbb{R}^n$: [[§19 Normed Linear Spaces and Lᵖ Spaces#^ex-19-2|551 Ex. §19.2]], [[§13 Some Topological Concepts in Metric Spaces#^prop-13-1|451 §13.1]]; the triangle inequality for $p_1$: [[Triangle inequality|LADR 6.17]].
> - In this course as norms: [[§8 Normed Linear Spaces#^ex-8-1|Ex. §8.1]].

> [!example] Example §3.2: The Sets $\{p < 1\}$ in $\mathbb{R}^2$
> For each of the three examples, the set $\{x \in \mathbb{R}^2 : p(x) < 1\}$ is:
> - (a) $p_1 < 1$: the open unit disk $x_1^2 + x_2^2 < 1$;
> - (b) $p_2 < 1$: the open square $|x_1| < 1$, $|x_2| < 1$;
> - (c) $p_3 < 1$: the open diamond $|x_1| + |x_2| < 1$, with vertices $(\pm 1, 0)$, $(0, \pm 1)$.
>
> ![[m556-3-1.svg]]
> *The three sets $\{p < 1\}$ in $\mathbb{R}^2$: the disk, the square and the diamond.*
>
> All three sets are convex. This is not a coincidence: there is a correspondence between convex sets and positive homogeneous subadditive functions, to be made precise [[§5 Convex Sets and the Gauge#^cor-5-8|later in the course]]. In finite dimensions the picture already suggests it.

^ex-3-2

> [!remark]- Connections
> - The closed unit balls of the same norms: [[§19 Normed Linear Spaces and Lᵖ Spaces#^ex-19-2|551 Ex. §19.2]].
> - The correspondence: [[§5 Convex Sets and the Gauge#^prop-5-1|§5.1]], [[§5 Convex Sets and the Gauge#^ex-5-2|Ex. §5.2]], [[§5 Convex Sets and the Gauge#^cor-5-8|§5.8]].

## The Hahn–Banach Theorem (Real Version)

> [!theorem] Theorem §3.2: Hahn–Banach
> Let $X$ be a linear space over $\mathbb{R}$, and let $p : X \to \mathbb{R}$ be positive homogeneous and subadditive. Let $Y$ be a linear subspace of $X$ and $\ell : Y \to \mathbb{R}$ a linear functional on $Y$ satisfying
>
> $$
> \ell(y) \leq p(y) \qquad \text{for all } y \in Y.
> $$
>
> Then $\ell$ can be extended to a linear functional on $X$: there is a linear functional $L : X \to \mathbb{R}$ with $L|_Y = \ell$ and
>
> $$
> L(x) \leq p(x) \qquad \text{for all } x \in X.
> $$
>
> *Lax: §3.1, Thm 1*

^thm-3-2

> [!remark]- Connections
> - Proof: [[§4 Proof of the Hahn–Banach Theorem#^pf-3-2|§4]]. Applied to a gauge: [[§6 The Hyperplane Separation Theorem#^thm-6-1|§6.1]]. Complex scalars: [[§7 The Complex Hahn–Banach Theorem#^thm-7-1|§7.1]].

> [!remark] Note: Notation
> Throughout these notes a functional given on a subspace is written $\ell$ and its extension $L$. Wu and Lax keep the name $\ell$ for the extension; the distinction is kept here because several proofs manipulate both at once.

^rem-3-3

The proof is given in [[§4 Proof of the Hahn–Banach Theorem|§4]]. The complex version will be stated later ([[§7 The Complex Hahn–Banach Theorem#^thm-7-1|§7.1]]).

> [!remark] Remark: Reading the Statement
> The data are: a linear space $X$; a function $p$ on all of $X$ that behaves like a norm; a linear functional $\ell$ defined only on a subspace $Y$; and a compatibility condition $\ell \leq p$ on $Y$. The conclusion is that $\ell$ extends linearly to an $L$ on all of $X$ without ever exceeding $p$. Since we have no way to write down linear functionals on an abstract $X$ directly (contrast with $\mathbb{R}^n$, [[§2 Linear Maps, Convexity, and Linear Functionals#^ex-2-2|Ex. §2.2]]), the theorem is the fundamental device for producing them: define $\ell$ on a small subspace where it is understood, dominate it by $p$, and extend.

^rem-3-4

## Geometric Meaning: Hyperplanes and Half-Spaces

> [!example] Example §3.3: Level Sets of Linear Functionals on $\mathbb{R}^n$
> Let $\ell(x) = a \cdot x$ on $\mathbb{R}^n$ with $a \neq 0$.
> - $\{ \ell(x) = 0 \}$ is the set of vectors perpendicular to $a$: a plane through the origin (for $n = 3$).
> - $\{ \ell(x) = c \}$ is a plane not necessarily through the origin, parallel to the previous one.
> - $\{ \ell(x) < c \}$ and $\{ \ell(x) > c \}$ are the two sides of that plane; if $a$ points “upward,” then $\{\ell < c\}$ is everything below the plane and $\{\ell > c\}$ everything above.

^ex-3-3

> [!definition] Definition §3.2: Hyperplane; Half-Space
> Let $\ell$ be a nonzero linear functional on a linear space $X$ over $\mathbb{R}$ and $c \in \mathbb{R}$. The set $\{ x \in X : \ell(x) = c \}$ is called a **hyperplane**, and the sets $\{ \ell(x) < c \}$, $\{ \ell(x) > c \}$ are the two **half-spaces** it bounds.
>
> *Lax: §3.2, hyperplanes*

^def-3-2

> [!remark]- Connections
> - Linear functionals: [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-5|Def. §2.5]], [[§12 Duality#^ladr-3-108|LADR 3.108]]; on $\mathbb{R}^n$ they are the $x \mapsto a \cdot x$ of [[§12 Duality#^ladr-3-109|LADR 3.109]].
> - On a Hilbert space, the kernel $\{\ell = 0\}$ of a bounded functional has codimension one: [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-19-4|§19.4]].

> [!remark] Remark
> Linear functionals are thus directly tied to geometry: a linear functional and a constant determine a hyperplane and its two half-spaces. Combined with the [[§3 Statement and Motivation#^thm-3-2|Hahn–Banach theorem]], this is what makes it possible to separate convex sets by hyperplanes in general linear spaces ([[§6 The Hyperplane Separation Theorem#^thm-6-1|§6.1]]), a theme that will recur.

^rem-3-5
