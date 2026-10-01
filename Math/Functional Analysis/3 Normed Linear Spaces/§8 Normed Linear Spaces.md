---
type: section
subject: "[[Functional Analysis]]"
chapter: 3
section: 8
tags: [functional-analysis, math556]
---
← [[§7 The Complex Hahn–Banach Theorem]] · ↑ [[· 3 Normed Linear Spaces]] · [[§9 Completeness]] →

*Stage: norms — Thread: convexity. A norm is a symmetric gauge (Proposition [[§8 Normed Linear Spaces#^prop-8-1|§8.1]]); with it come distance, convergence and closed sets.*

> [!remark] Note: Notation
> Wu writes norms as $|x|$ on the board. These notes use $\|x\|$, reserving $|\cdot|$ for the modulus of a scalar; the two appear side by side in the homogeneity axiom.

^rem-8-1

## Definition and Examples

> [!definition] Definition §8.1: Norm; Normed Linear Space
> Let $X$ be a linear space over $\mathbb{F}$ ($= \mathbb{R}$ or $\mathbb{C}$). A function $\|\cdot\| : X \to \mathbb{R}_+ = \{a \in \mathbb{R} : a \ge 0\}$ is a **norm** if
> - (1) **positivity**: $\|x\| \ge 0$ for all $x \in X$, and $\|x\| = 0$ if and only if $x = 0$;
> - (2) **homogeneity**: $\|ax\| = |a|\, \|x\|$ for all $a \in \mathbb{F}$, $x \in X$;
> - (3) **subadditivity** (triangle inequality): $\|x + y\| \le \|x\| + \|y\|$ for all $x, y \in X$.
>
> The pair $(X, \|\cdot\|)$ is a **normed linear space**. When the norm is understood one writes simply $X$.
>
> *Lax: §5.1, (1)–(3)*

^def-8-1

> [!remark]- Connections
> - The 551 definition (real scalars): [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-2|551 Def. §19.2]]; the norm of an inner product space is the case treated in [[§19 Inner Products and Norms#^ladr-6-7|LADR 6.7]] (triangle inequality [[Triangle inequality|LADR 6.17]]).
> - Inner-product norms in this course: [[§17 Cauchy–Schwarz and the Induced Norm|§17]].

> [!definition] Definition §8.2: Seminorm
> A function $q : X \to \mathbb{R}_+$ on a linear space $X$ over $\mathbb{F}$ is a **seminorm** if it satisfies homogeneity and subadditivity, (2) and (3) of Definition [[§8 Normed Linear Spaces#^def-8-1|§8.1]], but not necessarily positivity: $q(x) = 0$ is allowed for some $x \neq 0$.

^def-8-2

> [!theorem] Proposition §8.1: Norms and Gauges
> Let $X$ be a linear space over $\mathbb{R}$.
> - (a) Every norm on $X$ is positive homogeneous and subadditive.
> - (b) If $\|\cdot\|$ is a norm on $X$ and $K = \{ x : \|x\| < 1 \}$ or $K = \{ x : \|x\| \le 1 \}$, then $K$ is convex, $0$ is an interior point of $K$, and $p_K = \|\cdot\|$.
> - (c) Conversely, let $K$ be convex with $0$ an interior point. Then $p_K$ is a norm if and only if $K$ contains no full ray (for every $x \neq 0$ there is $s > 0$ with $sx \notin K$) and $p_K(-x) = p_K(x)$ for all $x$. The last condition holds in particular when $K = -K$.

^prop-8-1

> [!proof]+ Proof
> (Not covered in lecture.) (a) Positive homogeneity is homogeneity restricted to $a \ge 0$; subadditivity is an axiom.
>
> (b) $K$ is convex by Proposition [[§5 Convex Sets and the Gauge#^prop-5-1|§5.1]] with $p = \|\cdot\|$. Given $y \in X$, put $\varepsilon(y) = 1/(\|y\| + 1)$; for $|t| < \varepsilon(y)$, $\|ty\| = |t|\,\|y\| < 1$, so $ty \in K$, and $0$ is an interior point. For $a > 0$, $x/a \in K$ iff $\|x\| < a$ (respectively $\|x\| \le a$), so $A(x) = (\|x\|, \infty)$ (respectively $[\|x\|, \infty)$), and in either case $p_K(x) = \inf A(x) = \|x\|$.
>
> (c) By Propositions [[§5 Convex Sets and the Gauge#^prop-5-6|§5.6]] and [[§5 Convex Sets and the Gauge#^prop-5-5|§5.5]](a), $p_K$ is non-negative, positive homogeneous and subadditive, and by Proposition [[§5 Convex Sets and the Gauge#^prop-5-5|§5.5]](c), $p_K(x) = 0$ iff the ray $\{sx : s \ge 0\}$ lies in $K$; so $p_K$ satisfies positivity iff $K$ contains no full ray. If moreover $p_K(-x) = p_K(x)$, then for $a < 0$, $p_K(ax) = p_K(|a|(-x)) = |a|\,p_K(-x) = |a|\,p_K(x)$, which with positive homogeneity gives homogeneity for all real $a$, and $p_K$ is a norm. Conversely a norm satisfies positivity and $\|{-x}\| = \|x\|$. Finally, if $K = -K$ then $x/a \in K$ iff $-x/a \in K$, so $A(-x) = A(x)$ and $p_K(-x) = p_K(x)$.

^pf-8-1

*Uses:* [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], [[§3 Statement and Motivation#^def-3-1|Def. §3.1]], [[§5 Convex Sets and the Gauge#^def-5-1|Def. §5.1]], [[§5 Convex Sets and the Gauge#^def-5-2|Def. §5.2]], [[§5 Convex Sets and the Gauge#^prop-5-1|§5.1]], [[§5 Convex Sets and the Gauge#^prop-5-5|§5.5]], [[§5 Convex Sets and the Gauge#^prop-5-6|§5.6]]

> [!remark] Remark: Relation to the Functions $p$ of Chapter 2
> By (a), every [[§3 Statement and Motivation#^thm-3-2|Hahn–Banach]] statement applies with $p = \|\cdot\|$ or $p = C\|\cdot\|$. The converse of (a) is false, and not only because a positive homogeneous subadditive $p$ may take negative values: even a non-negative one with $p(x) = 0 \Rightarrow x = 0$ need not be a norm, since nothing forces $p(-x) = p(x)$. On $\mathbb{R}$, $p(x) = \max\{x, 0\} + 2\max\{-x, 0\}$ is such a function, with $p(1) = 1 \neq 2 = p(-1)$. By (b) and (c), norms on a real space correspond to convex sets with $0$ interior that contain no full ray and are symmetric; the unit ball is the geometric picture of the norm, as with the disk, square and diamond of Example [[§3 Statement and Motivation#^ex-3-2|§3.2]].

^rem-8-2

> [!example] Example §8.1: Norms on $\mathbb{R}^n$
> On $X = \mathbb{R}^n$, the following are norms:
>
> $$\begin{aligned}
> \|x\|_2 &= \bigl(x_1^2 + \cdots + x_n^2\bigr)^{1/2} && \text{(Euclidean, or $\ell^2$, norm)} \\
> \|x\|_\infty &= \max_{1 \le i \le n} |x_i| && \text{($\ell^\infty$, or maximum, norm)} \\
> \|x\|_1 &= |x_1| + \cdots + |x_n| && \text{($\ell^1$ norm)} \\
> \|x\|_p &= \Bigl( \sum_{i=1}^n |x_i|^p \Bigr)^{1/p}, \quad 1 \le p < \infty && \text{($\ell^p$ norm).}
> \end{aligned}$$
>
> For $\|\cdot\|_2$, $\|\cdot\|_\infty$, $\|\cdot\|_1$ the axioms were checked in Example [[§3 Statement and Motivation#^ex-3-1|§3.1]] (as $p_1, p_2, p_3$; positivity is immediate). That $\|\cdot\|_p$ is subadditive for general $p$ is [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^thm-13-1|Minkowski's inequality]], proved in [[· 4 Infinite-Dimensional Spaces꞉ ℓᵖ, Lᵖ, and Compactness|Chapter 4]]; the other axioms are immediate. Thus one linear space carries many norms, and $\mathbb{R}^n$ alone is not enough to see what a norm can do; the point of the definition is infinite-dimensional spaces.
>
> *Lax: §5.1, examples (a)–(b), for sequences*

^ex-8-1

> [!remark]- Connections
> - The same norms in 551: [[§19 Normed Linear Spaces and Lᵖ Spaces#^ex-19-2|551 Ex. §19.2]] (unit-ball figure); as metrics on $\mathbb{R}^n$: [[§11 Metric Topology#^ex-11-1|590 Ex. §11.1]], [[§11 Metric Topology#^ex-11-5|590 Ex. §11.5]], [[§13 Some Topological Concepts in Metric Spaces#^ex-13-4|451 Ex. §13.4]].
> - Minkowski's inequality for $L^p$ functions in 551: [[Minkowski's Inequality|551 §19.9]]; the version for sums used here is [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^thm-13-1|§13.1]].

## The Induced Metric

> [!definition] Definition §8.3: Metric Space
> A **metric** on a set $M$ is a function $d : M \times M \to \mathbb{R}$ such that for all $x, y, z \in M$:
> - (i) $d(x, y) \ge 0$, and $d(x, y) = 0$ if and only if $x = y$;
> - (ii) $d(x, y) = d(y, x)$;
> - (iii) $d(x, y) \le d(x, z) + d(z, y)$.
>
> $(M, d)$ is a **metric space**. A metric space need not be a linear space.

^def-8-3

> [!remark]- Connections
> - Home of the definition: [[§11 Metric Topology#^def-11-1|590 Def. §11.1]], [[§13 Some Topological Concepts in Metric Spaces#^def-13-1|451 Def. §13.1]].

> [!theorem] Proposition §8.2: A Normed Space is a Metric Space
> Let $(X, \|\cdot\|)$ be a normed linear space and define $d(x, y) = \|x - y\|$ for $x, y \in X$. Then $(X, d)$ is a metric space.
>
> *Lax: §5.1, (4)*

^prop-8-2

> [!proof]+ Proof
> (Stated without proof in lecture; the check is routine.) (i) $d(x,y) = \|x - y\| \ge 0$, and it is $0$ iff $x - y = 0$ iff $x = y$, by positivity. (ii) $d(y, x) = \|y - x\| = \|(-1)(x - y)\| = |{-1}|\, \|x - y\| = d(x, y)$, by homogeneity with $a = -1$; a student asked whether symmetry is automatic, and this is why it is. (iii) $d(x, y) = \|(x - z) + (z - y)\| \le \|x - z\| + \|z - y\| = d(x, z) + d(z, y)$, by subadditivity.

^pf-8-2

*Uses:* [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], [[§8 Normed Linear Spaces#^def-8-3|Def. §8.3]]

> [!remark]- Connections
> - Same statement and proof in 551: [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-1|551 §19.1]].

The metric is translation invariant, $d(x + z, y + z) = d(x, y)$, and homogeneous, $d(ax, ay) = |a|\,d(x,y)$; a general metric on a linear space need not be either. Everything available in a metric space — limits, open and closed sets, continuity — is now available in $X$.

## Convergence and Cauchy Sequences

> [!definition] Definition §8.4: Convergence
> Let $X$ be a normed linear space. A sequence $\{x_n\}_{n=1}^\infty \subset X$ **converges** to $x_0 \in X$, written $x_n \to x_0$, if
>
> $$
> \lim_{n \to \infty} \|x_n - x_0\| = 0.
> $$

^def-8-4

> [!remark]- Connections
> - In 551: [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-3|551 Def. §19.3]]; in a metric space: [[§13 Some Topological Concepts in Metric Spaces#^def-13-2|451 Def. §13.2]].
> - Convergence in a topological space: [[§7 Interior and Closure#^def-7-4|590 Def. §7.4]], which for the norm metric is this definition.

> [!theorem] Lemma §8.3: Reverse Triangle Inequality
> For all $x, y$ in a normed linear space $X$,
>
> $$
> \bigl|\, \|x\| - \|y\| \,\bigr| \;\le\; \|x - y\|.
> $$

^lem-8-3

> [!proof]+ Proof
> By subadditivity applied to $x = (x - y) + y$,
>
> $$
> \|x\| \le \|x - y\| + \|y\|, \qquad \text{i.e.} \qquad \|x\| - \|y\| \le \|x - y\|.
> $$
>
> Exchanging $x$ and $y$ and using $\|y - x\| = \|x - y\|$ (homogeneity with $a = -1$),
>
> $$
> \|y\| - \|x\| \le \|x - y\|.
> $$
>
> The two together bound the absolute value.

^pf-8-3

*Uses:* [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]]

> [!theorem] Proposition §8.4: A Norm is Continuous
> Let $(X, \|\cdot\|)$ be a normed linear space. Then $\|\cdot\| : X \to \mathbb{R}$ is uniformly continuous: for every $\varepsilon > 0$ there is $\delta > 0$ — indeed $\delta = \varepsilon$ works — such that
>
> $$
> \|x - y\| < \delta \implies \bigl|\, \|x\| - \|y\| \,\bigr| < \varepsilon \qquad \text{for all } x, y \in X.
> $$
>
> In particular, if $x_n \to x_0$ in $X$ then $\|x_n\| \to \|x_0\|$ in $\mathbb{R}$.

^prop-8-4

> [!proof]+ Proof
> Given $\varepsilon > 0$ take $\delta = \varepsilon$. If $\|x - y\| < \delta$ then by Lemma [[§8 Normed Linear Spaces#^lem-8-3|§8.3]], $\bigl|\|x\| - \|y\|\bigr| \le \|x - y\| < \varepsilon$. The $\delta$ does not depend on $x$ or $y$, so the continuity is uniform; the constant $1$ in the lemma says $\|\cdot\|$ is Lipschitz. For the last claim apply this with $y = x_0$ and $x = x_n$.

^pf-8-4

*Uses:* [[§8 Normed Linear Spaces#^lem-8-3|§8.3]], [[§8 Normed Linear Spaces#^def-8-4|Def. §8.4]]

> [!remark] Remark: What This Does and Does Not Say
> The statement is not circular, although it can sound so. It compares two metric spaces: $X$ with $d(x,y) = \|x - y\|$, and $\mathbb{R}$ with $|s - t|$; neither metric is defined in terms of the continuity being asserted. Only subadditivity and homogeneity are used — positivity is not — so the same proof shows any seminorm, and any positive homogeneous subadditive $p$ that happens to satisfy $p(-x) = p(x)$, is $1$-Lipschitz.
>
> The question has content whenever a second topology is present. Whether a norm $\|\cdot\|_1$ is continuous with respect to another norm $\|\cdot\|_2$ is settled by Proposition [[§10 New Normed Spaces from Old#^prop-10-2|§10.2]]: exactly when $\|x\|_1 \le C\|x\|_2$ for some constant $C$, which is one half of equivalence of the two norms; on $\mathbb{R}^n$ this always holds, in infinite dimensions it need not. Later in the course $X$ will also carry the weak topology, in which the norm is *not* continuous. (Not covered in lecture.)

^rem-8-3

> [!definition] Definition §8.5: Cauchy Sequence
> A sequence $\{x_n\} \subset X$ is **Cauchy** if for every $\varepsilon > 0$ there is $N = N(\varepsilon) \in \mathbb{N}$ such that
>
> $$
> \|x_m - x_k\| < \varepsilon \qquad \text{for all } m, k \ge N.
> $$

^def-8-5

> [!remark]- Connections
> - In 551: [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-3|551 Def. §19.3]]; on $\mathbb{R}$: [[§10 Monotone Sequences and Cauchy Sequences#^def-10-4|451 Def. §10.4]]; in a metric space: [[§13 Some Topological Concepts in Metric Spaces#^def-13-2|451 Def. §13.2]].

> [!theorem] Proposition §8.5: Limits are Unique; Convergent Sequences are Cauchy
> Let $\{x_n\}$ be a sequence in a normed linear space $X$.
> - (a) If $x_n \to x$ and $x_n \to x'$, then $x = x'$.
> - (b) If $x_n \to x$, then $\{x_n\}$ is Cauchy.

^prop-8-5

> [!proof]+ Proof
> (Not covered in lecture.) (a) $\|x - x'\| \le \|x - x_n\| + \|x_n - x'\| \to 0$, so $\|x - x'\| = 0$ and $x = x'$ by positivity. (b) Given $\varepsilon > 0$, choose $N$ with $\|x_n - x\| < \varepsilon/2$ for $n \ge N$; then for $m, k \ge N$, $\|x_m - x_k\| \le \|x_m - x\| + \|x - x_k\| < \varepsilon$.

^pf-8-5

*Uses:* [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], [[§8 Normed Linear Spaces#^def-8-4|Def. §8.4]], [[§8 Normed Linear Spaces#^def-8-5|Def. §8.5]]

> [!remark]- Connections
> - The real-line and metric versions: [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-7|451 §10.7]] (convergent implies Cauchy), [[§13 Some Topological Concepts in Metric Spaces#^rem-13-4|451, uniqueness of limits]].
> - Part (a) holds in every Hausdorff space ([[§8 Hausdorff Spaces#^thm-8-3|590 Thm. §8.3]]), and metric spaces are Hausdorff ([[§11 Metric Topology#^thm-11-4|590 Thm. §11.4]]).

> [!remark] Remark
> Convergence refers to a limit *in $X$*; a Cauchy sequence has its terms approaching one another with no limit mentioned. The converse of (b) fails: a Cauchy sequence may fail to converge because the point it is heading toward is missing from $X$ — the standard example being a sequence of rationals approaching $\sqrt{2}$ inside $\mathbb{Q}$. Spaces without this defect are the subject of the [[§9 Completeness|next section]]. Both statements, and their proofs, hold verbatim in any metric space.

^rem-8-4

> [!definition] Definition §8.6: Closed Subset
> A subset $S$ of a normed linear space (or metric space) $X$ is **closed** if it contains the limits of all its convergent sequences: whenever $\{s_n\} \subset S$ and $s_n \to x$ with $x \in X$, then $x \in S$.

^def-8-6

> [!remark]- Connections
> - The topological definition (complement open) and its sequential characterization in metric spaces: [[§13 Some Topological Concepts in Metric Spaces#^def-13-5|451 Def. §13.5]], [[§13 Some Topological Concepts in Metric Spaces#^prop-13-5|451 §13.5]]; in $\mathbb{R}^n$: [[§2 Open and Closed Sets#^def-2-4|452 Def. §2.4]].
> - The topological definition (complement open): [[§6 Closed Sets and Limit Points#^def-6-1|590 Def. §6.1]]; in metric spaces it agrees with this one by [[§7 Interior and Closure#^cor-7-5|590 Cor. §7.5]] and the Sequence Lemma ([[§11 Metric Topology#^lem-11-8|590 Lemma §11.8]]).

> [!definition] Definition §8.7: Closure; Dense Subset
> Let $S$ be a subset of a normed linear space (or metric space) $X$. The **closure** $\overline{S}$ of $S$ is the set of all limits of convergent sequences in $S$:
>
> $$
> \overline{S} = \{ x \in X : x = \lim_{n \to \infty} s_n \text{ for some sequence } s_n \in S \} .
> $$
>
> $S$ is **dense** in $X$ if $\overline{S} = X$.
>
> *Lax: §5.1, before Thm 2; “dense” in the definition of separable space*

^def-8-7

> [!remark]- Connections
> - The closure as smallest closed superset, and its sequential description: [[§13 Some Topological Concepts in Metric Spaces#^def-13-6|451 Def. §13.6]], [[§13 Some Topological Concepts in Metric Spaces#^prop-13-6|451 §13.6]]; in $\mathbb{R}^n$: [[§2 Open and Closed Sets#^def-2-5|452 Def. §2.5]].
> - Topological closure and density: [[§7 Interior and Closure#^def-7-1|590 Def. §7.1]] (smallest closed superset), described by limits of sequences in metric spaces by the Sequence Lemma ([[§11 Metric Topology#^lem-11-8|590 Lemma §11.8]]); dense: [[§18 Countability Axioms#^def-18-4|590 Def. §18.4]].

> [!theorem] Proposition §8.6: Properties of the Closure
> Let $S$ be a subset of a normed linear space $X$.
> - (a) $S \subset \overline{S}$, and $\overline{S}$ is closed.
> - (b) $S$ is closed if and only if $S = \overline{S}$.
> - (c) If $T$ is closed and $S \subset T$, then $\overline{S} \subset T$; so $\overline{S}$ is the smallest closed set containing $S$.
> - (d) If $S$ is a linear subspace, so is $\overline{S}$.
>
> *Lax: §5.1, Thm 2 (part (d))*

^prop-8-6

> [!proof]+ Proof
> (Not covered in lecture.) (a) $s \in S$ is the limit of the constant sequence $s, s, \ldots$. Let $x_k \in \overline{S}$ with $x_k \to x$. For each $k$ choose $s_k \in S$ with $\|s_k - x_k\| < 1/k$; then $\|s_k - x\| \le 1/k + \|x_k - x\| \to 0$, so $x \in \overline{S}$.
>
> (b) By Definition [[§8 Normed Linear Spaces#^def-8-6|§8.6]], $S$ is closed iff every limit of a sequence in $S$ lies in $S$, i.e. iff $\overline{S} \subset S$; with (a), iff $\overline{S} = S$.
>
> (c) A limit of a sequence in $S$ is a limit of a sequence in $T$, hence lies in $T$ since $T$ is closed.
>
> (d) $0 \in S \subset \overline{S}$. If $s_n \to x$ and $t_n \to y$ with $s_n, t_n \in S$, and $a, b \in \mathbb{F}$, then $a s_n + b t_n \in S$ and
>
> $$
> \|(a s_n + b t_n) - (ax + by)\| \le |a|\,\|s_n - x\| + |b|\,\|t_n - y\| \to 0,
> $$
>
> so $ax + by \in \overline{S}$.

^pf-8-6

*Uses:* [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], [[§8 Normed Linear Spaces#^def-8-6|Def. §8.6]], [[§8 Normed Linear Spaces#^def-8-7|Def. §8.7]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]]

> [!definition] Definition §8.8: Closed Linear Span
> The **closed linear span** of a subset $S$ of a normed linear space $X$ is $\overline{\operatorname{span}}\, S := \overline{\operatorname{span} S}$. By Proposition [[§8 Normed Linear Spaces#^prop-8-6|§8.6]](a),(c),(d), it is a closed linear subspace of $X$, and it is the smallest closed linear subspace containing $S$.
>
> *Lax: §6.4, closed linear span*

^def-8-8

> [!remark]- Connections
> - The (algebraic) span it closes up: [[§1 Linear Spaces#^def-1-5|Def. §1.5]], [[§4 Span and Linear Independence#^ladr-2-6|LADR 2.6]].

> [!definition] Definition §8.9: Open Ball; Metric Interior Point
> For $x_0 \in X$ and $r > 0$, the **open ball** of radius $r$ about $x_0$ is $B_r(x_0) = \{ x \in X : \|x - x_0\| < r \}$. A point $x_0$ of a subset $K \subset X$ is a **metric interior point** of $K$ if $B_r(x_0) \subset K$ for some $r > 0$.

^def-8-9

> [!remark]- Connections
> - Balls in a metric space and in $\mathbb{R}^n$: [[§11 Metric Topology#^def-11-2|590 Def. §11.2]], [[§2 Open and Closed Sets#^def-2-1|452 Def. §2.1]], [[§2 Open and Closed Sets#^def-2-3|452 Def. §2.3]] (interior points).

> [!theorem] Proposition §8.7: Metric Interior Points are Interior Points
> Let $K$ be a subset of a normed linear space $X$. Every metric interior point of $K$ is an interior point of $K$ in the sense of Definition [[§5 Convex Sets and the Gauge#^def-5-1|§5.1]].

^prop-8-7

> [!proof]+ Proof
> Let $B_r(x_0) \subset K$ and $y \in X$. If $y = 0$, then $x_0 + ty = x_0 \in K$ for all $t$. If $y \neq 0$, put $\varepsilon(y) = r/\|y\|$; for $|t| < \varepsilon(y)$, $\|(x_0 + ty) - x_0\| = |t|\,\|y\| < r$, so $x_0 + ty \in B_r(x_0) \subset K$. (Not covered in lecture.)

^pf-8-7

*Uses:* [[§8 Normed Linear Spaces#^def-8-9|Def. §8.9]], [[§5 Convex Sets and the Gauge#^def-5-1|Def. §5.1]], [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]]

> [!example] Example §8.2: An Interior Point that is Not a Metric Interior Point
> In $\mathbb{R}^2$ with the Euclidean norm, let $P = \{ (s, s^2) : s \neq 0 \}$ and $K = \mathbb{R}^2 \setminus P$. Then $0 \in K$ is an interior point of $K$ but not a metric interior point.
>
> *Not metric interior.* $(1/n, 1/n^2) \in P$, so $(1/n, 1/n^2) \notin K$, while $\|(1/n, 1/n^2)\| \to 0$; so no ball $B_r(0)$ lies in $K$.
>
> *Interior.* For $y = 0$ there is nothing to check. Let $y = (y_1, y_2) \neq 0$. A point $ty$ lies in $P$ iff $t y_1 = s$ and $t y_2 = s^2$ for some $s \neq 0$, which forces $t \neq 0$, $y_1 \neq 0$ and $y_2 = t y_1^2$, i.e. $t = y_2 / y_1^2$. So the line $\{ty : t \in \mathbb{R}\}$ meets $P$ in at most one point, at a parameter $t^* \neq 0$, and $\varepsilon(y) = |t^*|$ works (any $\varepsilon(y)$ works if the line misses $P$).
>
> The definition of [[§5 Convex Sets and the Gauge#^def-5-1|interior point]] tests one line at a time, and the parabola approaches $0$ along no single line. The set $K$ is not convex.

^ex-8-2

![[m556-8-1.svg]]
*The parabola $P$ (red) is removed from the plane. A line through $0$ meets $P$ at most once (red dots), so $0$ can move some distance along every line without leaving $K$ (blue: $|t| < |t^*|$ on one line): $0$ is an interior point. But the points $(1/n, 1/n^2)$ of $P$ enter every ball $B_r(0)$ (dashed), so $0$ is not a metric interior point.*
