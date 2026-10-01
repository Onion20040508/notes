---
type: section
subject: "[[Measure Theory]]"
chapter: 2
section: 5
tags: [measure-theory, math551]
---
← [[§4 Uncountability]] · ↑ [[· 2 Topology of ℝⁿ]] · [[§6 Open Covers and the Heine–Borel Theorem]] →

## Open and Closed Sets

> [!definition] Definition §5.1: Open Ball
> For $x \in \mathbb{R}^n$ and $r > 0$, the **open ball** centered at $x$ with radius $r$ is
>
> $$
> B(x, r) = \{y \in \mathbb{R}^n \mid |y - x| < r\}.
> $$

^def-5-1

> [!remark]- Connections
> - Topology: the [[§11 Metric Topology#^def-11-2|ε-ball (590 Def. §11.2)]] of a metric; the balls form a basis for the [[§11 Metric Topology#^def-11-3|metric topology]].
> - MATH 452: [[§2 Open and Closed Sets#^def-2-1|Open Ball (452 Def. §2.1)]].
> - Linear algebra: $|y - x|$ is the Euclidean norm of the dot product, [[6A Inner Products and Norms#^ladr-6-7|Norm (LADR 6.7)]].

> [!definition] Definition §5.2: Open Set
> A set $\mathcal{O} \subseteq \mathbb{R}^n$ is **open** if for every $x \in \mathcal{O}$, there exists $r > 0$ such that $B(x, r) \subseteq \mathcal{O}$.

^def-5-2

> [!remark]- Connections
> - MATH 451 metric-space version: [[§13 Some Topological Concepts in Metric Spaces#^def-13-5|Open and Closed Subsets (451 Def. §13.5)]].
> - Topology: the open sets of the metric topology, i.e. unions of basis balls ([[§2 Basis for a Topology#^lem-2-1|590 Lemma §2.1]]); for $n = 1$ the [[§1 Topological Spaces#^ex-1-5|standard topology on ℝ]].

> [!definition] Definition §5.3: Closed Set
> A set $F \subseteq \mathbb{R}^n$ is **closed** if for any sequence $\{x_n\} \subseteq F$ with $x_n \to x$, we have $x \in F$.
>
> Equivalently, $F$ is closed if and only if $F^c = \mathbb{R}^n \setminus F$ is open.

^def-5-3

![[m551-5-1.svg]]
*Left: $\mathcal{O}$ is open when every point has a ball $B(x,r)$ inside it (red); near the boundary (dashed, not part of $\mathcal{O}$) the radius must shrink, but it stays positive. Right: $F$ is closed when limits of sequences in $F$ stay in $F$ — here $x_k \to x$ with $x$ on the boundary, which $F$ contains (solid).*

> [!remark]- Connections
> - The equivalence is [[§13 Some Topological Concepts in Metric Spaces#^prop-13-5|Sequential Characterization of Closedness (451 §13.5)]].
> - Topology takes the complement form as the definition ([[§6 Closed Sets and Limit Points#^def-6-1|590 Def. §6.1]]); the sequential form holds in metric spaces by the [[§11 Metric Topology#^lem-11-8|Sequence Lemma]].

> [!theorem] Theorem §5.1: Bolzano–Weierstrass
> Let $\{x_k\}_{k=1}^\infty$ be a bounded sequence in $\mathbb{R}^n$. Then there exists a subsequence $\{x_{k_j}\}_{j=1}^\infty$ that converges to some $x_0 \in \mathbb{R}^n$.

^thm-5-1

> [!remark] Remark
> This is a direct generalization of [[Bolzano–Weierstrass Theorem|Bolzano–Weierstrass]] in $\mathbb{R}$, which you proved in MATH 451. The idea is to apply the 1-dimensional result coordinate by coordinate, extracting subsequences iteratively.

^rem-5-1

> [!proof]+ Proof
> Write each element of the sequence as $x_k = (x_k^{(1)}, x_k^{(2)}, \ldots, x_k^{(n)}) \in \mathbb{R}^n$.
>
> Since $\{x_k\}$ is bounded in $\mathbb{R}^n$, there exists $M > 0$ such that $|x_k| \leq M$ for all $k$. This implies each coordinate sequence $\{x_k^{(i)}\}_{k=1}^\infty$ is bounded in $\mathbb{R}$ (since $|x_k^{(i)}| \leq |x_k| \leq M$).
>
> **Step 1 (First coordinate):** The sequence $\{x_k^{(1)}\}_{k=1}^\infty$ is bounded in $\mathbb{R}$. By [[Bolzano–Weierstrass Theorem|Bolzano–Weierstrass]] in $\mathbb{R}$, there exists a subsequence $\{x_{k_j^1}^{(1)}\}_{j=1}^\infty$ that converges to some $a_1 \in \mathbb{R}$.
>
> Let $S_1 = \{k_j^1 : j \in \mathbb{N}\}$ denote the indices of this subsequence.
>
> **Step 2 (Second coordinate):** Consider the subsequence $\{x_k\}_{k \in S_1}$. The second coordinates $\{x_k^{(2)}\}_{k \in S_1}$ form a bounded sequence in $\mathbb{R}$. By Bolzano–Weierstrass in $\mathbb{R}$, there exists a further subsequence indexed by $S_2 \subseteq S_1$ such that $\{x_k^{(2)}\}_{k \in S_2}$ converges to some $a_2 \in \mathbb{R}$.
>
> Note: Since $S_2 \subseteq S_1$, the first coordinates $\{x_k^{(1)}\}_{k \in S_2}$ still converge to $a_1$ ([[§11 Subsequences#^thm-11-1|subsequences of a convergent sequence]]).
>
> **Steps 3 through $n$:** Continue this process. At step $i$, extract a subsequence $S_i \subseteq S_{i-1}$ such that $\{x_k^{(i)}\}_{k \in S_i}$ converges to some $a_i \in \mathbb{R}$.
>
> **Final subsequence:** After $n$ steps, we have nested index sets $S_n \subseteq S_{n-1} \subseteq \cdots \subseteq S_1 \subseteq \mathbb{N}$.
>
> For the subsequence $\{x_k\}_{k \in S_n}$, all coordinates converge:
>
> $$
> x_k^{(i)} \to a_i \quad \text{for each } i = 1, 2, \ldots, n.
> $$
>
> **Conclusion:** Since convergence in $\mathbb{R}^n$ is equivalent to coordinate-wise convergence ([[§13 Some Topological Concepts in Metric Spaces#^prop-13-1|451 §13.1]]), we have
>
> $$
> x_k \to x_0 = (a_1, a_2, \ldots, a_n) \in \mathbb{R}^n \quad \text{as } k \to \infty \text{ along } S_n.
> $$

^pf-5-1

*Uses:* [[Bolzano–Weierstrass Theorem|451 §11.5]], [[§11 Subsequences#^thm-11-1|451 §11.1]], [[§13 Some Topological Concepts in Metric Spaces#^prop-13-1|451 §13.1]]

![[m551-5-2.svg]]
*The iterated extraction for $n = 2$: from all indices keep $S_1$, along which the first coordinates converge; from $S_1$ keep $S_2 \subseteq S_1$, along which the second coordinates converge as well (red). Thinning a sequence never spoils a limit it already has, so after $n$ rounds every coordinate converges along $S_n$.*

> [!remark]- Connections
> - MATH 451 states and proves it the same way: [[§13 Some Topological Concepts in Metric Spaces#^thm-13-3|Bolzano–Weierstrass in ℝⁿ (451 §13.3)]].
> - Topology: in metric spaces compact ⟺ sequentially compact ([[§16 Limit Point Compactness#^thm-16-2|590 §16.2]]); with [[Heine–Borel Theorem|Heine–Borel]] this is the statement that closed bounded subsets of $\mathbb{R}^n$ are sequentially compact.
> - Used later for [[§13 Egorov's and Lusin's Theorems#^lem-13-2|Distance Between Disjoint Compact Sets]].

## Nested Set Theorem

> [!theorem] Theorem §5.2: Cantor's Nested Set Theorem
> Assume that $\{F_k\}_{k=1}^\infty$ is a sequence of non-empty, bounded, and closed sets in $\mathbb{R}^n$ with
>
> $$
> F_1 \supseteq F_2 \supseteq F_3 \supseteq \cdots \supseteq F_k \supseteq F_{k+1} \supseteq \cdots
> $$
>
> Then $\bigcap_{j=1}^\infty F_j \neq \emptyset$.

^thm-5-2

> [!proof]+ Proof
> Since $F_k \neq \emptyset$, we can choose $x_k \in F_k$ for each $k$.
>
> The sequence $\{x_k\}_{k=1}^\infty$ is contained in $F_1$ (since $x_k \in F_k \subseteq F_1$ for all $k$), so $\{x_k\}$ is bounded.
>
> By [[§5 Topology of ℝⁿ#^thm-5-1|Bolzano–Weierstrass]], there exists a convergent subsequence $\{x_{k_j}\}_{j=1}^\infty \to x_0$ for some $x_0 \in \mathbb{R}^n$.
>
> **Claim:** $x_0 \in \bigcap_{j=1}^\infty F_j$.
>
> Fix any $m \in \mathbb{N}$. For $j$ large enough that $k_j > m$, we have $x_{k_j} \in F_{k_j} \subseteq F_m$.
>
> So $\{x_{k_j}\}_{j=N}^\infty \subseteq F_m$ for some $N$, and this subsequence converges to $x_0$.
>
> Since $F_m$ is [[§5 Topology of ℝⁿ#^def-5-3|closed]], $x_0 \in F_m$.
>
> Since this holds for all $m$, we have $x_0 \in \bigcap_{j=1}^\infty F_j$.

^pf-5-2

*Uses:* [[§5 Topology of ℝⁿ#^thm-5-1|§5.1]], [[§5 Topology of ℝⁿ#^def-5-3|Def. §5.3]]

![[m551-5-3.svg]]
*Nested closed bounded sets $F_1 \supseteq F_2 \supseteq F_3 \supseteq \cdots$ with a chosen point $x_k \in F_k$ (black). All $x_k$ lie in the bounded set $F_1$, so a subsequence converges to some $x_0$ (red); for each $m$ the tail of that subsequence lies in $F_m$, and $F_m$ is closed, so $x_0 \in F_m$ for every $m$.*

> [!remark]- Connections
> - Topology version for any compact space: [[§15 Compact Spaces#^cor-15-6|Nested Sequence of Closed Sets (590 §15.6)]], a case of the [[§15 Compact Spaces#^thm-15-5|finite intersection property criterion]].
> - The key step in the proof of [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|Heine–Borel]].
