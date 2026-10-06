---
type: section
subject: "[[Topology]]"
chapter: 5
section: 19
munkres: "§28"
tags: [topology, math590]
---
← [[§18 Compact Spaces]] · ↑ [[· 5 Compactness]] · [[§20 Local Compactness]] →

## Definitions

> [!definition] Definition §23.1: Limit Point Compact
> A space $X$ is **limit point compact** if every infinite subset of $X$ has a [[§8 Interior and Closure#^def-8-5|limit point]].

^def-19-1

> [!remark] Remark: Three Notions of Compactness
> There are three related “compactness” notions:
> 1. **[[§18 Compact Spaces#^def-18-2|Compact]]:** Every open cover has a finite subcover.
> 2. **[[§19 Limit Point Compactness#^def-19-1|Limit point compact]]:** Every infinite subset has a limit point.
> 3. **[[§19 Limit Point Compactness#^def-19-3|Sequentially compact]]:** Every sequence has a convergent subsequence.
>
> **In general:** (1) $\Rightarrow$ (2) ([[§19 Limit Point Compactness#^thm-19-1|Theorem §19.1]]), but the other implications can fail.
>
> **For metrizable spaces:** All three are equivalent ([[§19 Limit Point Compactness#^thm-19-4|Theorem §19.4]])! This is why in analysis courses (where spaces are usually metric), these distinctions don't arise.
>
> **Intuition:**
> - Compact = “can't escape to infinity via open sets”
> - Limit point compact = “infinite sets must cluster somewhere”
> - Sequentially compact = “sequences can't escape; they must accumulate”
>
> The equivalence in metric spaces comes from the interplay between the metric and topology: balls give you sequences, and sequences detect limit points.

^rem-19-1

> [!theorem] Theorem §23.1: Compactness Implies Limit Point Compactness
> Compactness implies limit point compactness, but not conversely.

^thm-19-1

> [!proof]+ Proof
> Let $X$ be compact. We show every infinite subset of $X$ has a limit point.
>
> Let $A \subseteq X$ be a set with no limit point. We show $A$ must be finite.
>
> **Step 1:** $A$ is closed.
>
> Since $A$ has no limit points, $A' = \emptyset \subseteq A$. Thus $A$ contains all its limit points, so $A$ is closed ([[§8 Interior and Closure#^cor-8-5|Corollary §8.5]]).
>
> **Step 2:** Each point $a \in A$ has a neighborhood meeting $A$ only at $\{a\}$.
>
> Since $a$ is not a limit point of $A$, there exists a neighborhood $U_a$ of $a$ such that $U_a \cap (A \setminus \{a\}) = \emptyset$, i.e., $U_a \cap A = \{a\}$.
>
> **Step 3:** Construct a finite subcover.
>
> The collection $\{U_a\}_{a \in A} \cup \{X \setminus A\}$ is an open cover of $X$. Since $X$ is compact, there exists a finite subcover, say $U_{a_1}, \ldots, U_{a_n}$ and possibly $X \setminus A$.
>
> **Step 4:** Conclude $A$ is finite.
>
> Every point of $A$ must be covered by some $U_{a_i}$ (since $X \setminus A$ doesn't cover any point of $A$). But $U_{a_i} \cap A = \{a_i\}$. Thus $A \subseteq \{a_1, \ldots, a_n\}$, so $A$ is finite.
>
> By contrapositive: every infinite subset has a limit point, so $X$ is limit point compact.

^pf-19-1

*Uses:* [[§8 Interior and Closure#^def-8-5|Def. §8.5]], [[§8 Interior and Closure#^cor-8-5|§8.5]]

> [!example] Example §23.1: Limit Point Compact but Not Compact
> $Y = \{a, b\}$ with $\mathcal{T}_Y = \{\emptyset, Y\}$ ([[§1 Topological Spaces#^ex-1-2|indiscrete topology]]). $X = \mathbb{Z}_+ \times Y$.
>
> *$X$ is limit point compact:* Let $S \subseteq X$ be infinite. We show $S$ has a limit point.
>
> The only nonempty open set in $Y$ is $Y$ itself, so the only nonempty open sets in $X$ are of the form $U \times Y$ where $U \subseteq \mathbb{Z}_+$.
>
> For any point $n \times a \in X$, every neighborhood contains $\{n\} \times Y = \{n \times a, n \times b\}$. So if $S$ contains any point $n \times a$, then $n \times b$ is a limit point of $S$ (and vice versa). Since $S$ is infinite, it must contain some point, and that point's “partner” is a limit point.
>
> *$X$ is not compact:* $\{\{n\} \times Y \mid n \in \mathbb{Z}_+\}$ is an open cover (each $\{n\} \times Y$ is open since $\{n\}$ is open in the [[§1 Topological Spaces#^ex-1-3|discrete topology]] on $\mathbb{Z}_+$), but has no finite subcover.

^ex-19-1

![[m590-16-1.svg]]
*$X=\mathbb{Z}_+\times\{a,b\}$ with $Y$ indiscrete: the smallest open sets are the columns $\{n\}\times Y$ (blue), so a point can never be separated from its partner. Any set $S$ (red) containing $3\times a$ has $3\times b$ (circled) as a limit point, so $X$ is limit point compact. Still, the columns form an open cover with no finite subcover.*

## Subsequences and Sequential Compactness

> [!definition] Definition §23.2: Subsequence
> If $(x_n)$ is a sequence of points in $X$, and if $n_1 < n_2 < \cdots < n_i < \cdots$ is an increasing sequence of positive integers, then $y_i = x_{n_i}$ is called a **subsequence** of $(x_n)$.

^def-19-2

> [!remark]- Connections
> - Same definition for real sequences: [[§11 Subsequences#^def-11-1|451 Def. §11.1]].

> [!definition] Definition §23.3: Sequentially Compact
> $X$ is **sequentially compact** if every sequence of points of $X$ has a [[§8 Interior and Closure#^def-8-6|convergent]] subsequence.

^def-19-3

> [!remark]- Connections
> - MATH 451: [[Bolzano–Weierstrass Theorem]] (every bounded sequence in $\mathbb{R}$ has a convergent subsequence) and Bolzano–Weierstrass in $\mathbb{R}^n$ ([[§13 Some Topological Concepts in Metric Spaces#^thm-13-3|§13.3]]).
> - The same definition in a normed space: [[§18 Compactness and the Unit Ball#^def-18-1|556 Def. §18.1]]; the closed unit ball of an infinite-dimensional space fails it ([[§18 Compactness and the Unit Ball#^thm-18-5|556 Thm. §18.5]]).

> [!example] Example §23.2
> In $\mathbb{R}$: $x_n = (1, 0, 1, 0, 1, 0, \ldots)$ has a convergent subsequence $y_n = (0, 0, 0, \ldots)$.

^ex-19-2

To complete the equivalence of [[§19 Limit Point Compactness#^thm-19-4|Theorem §19.4]] below, we need $(3) \Rightarrow (1)$. This uses two lemmas, proved first.

> [!theorem] Lemma §23.2: Lebesgue Number Lemma
> Let $(X, d)$ be a sequentially compact metric space and let $\{U_\alpha\}$ be an open cover of $X$. Then there exists $\delta > 0$ (called a **Lebesgue number** for the cover) such that for every subset $A \subseteq X$ with $\text{diam}(A) < \delta$, there exists some $U_\alpha$ containing $A$.

^lem-19-2

![[m590-16-2.svg]]
*A Lebesgue number $\delta$ for the cover $\{U_1,\dots,U_4\}$ of $X$ (blue outline): every set of diameter $<\delta$ (red disks) lies inside a single cover element, even one sitting where several $U$'s overlap, like the disk inside $U_4$ (shaded). The lemma says small sets can never straddle the cover.*

> [!proof]+ Proof
> Suppose no such $\delta$ exists. Then for each $n \in \mathbb{Z}_+$, there exists a set $C_n$ with $\text{diam}(C_n) < 1/n$ that is not contained in any single $U_\alpha$. Choose $x_n \in C_n$ for each $n$.
>
> Since $X$ is sequentially compact, $(x_n)$ has a subsequence $x_{n_i} \to a$ for some $a \in X$. Since $\{U_\alpha\}$ covers $X$, there exists $U_\alpha$ with $a \in U_\alpha$. Since $U_\alpha$ is open, there exists $\varepsilon > 0$ with $B(a, \varepsilon) \subseteq U_\alpha$.
>
> Choose $i$ large enough that $d(x_{n_i}, a) < \varepsilon/2$ and $1/n_i < \varepsilon/2$. Then for any $y \in C_{n_i}$:
>
> $$
> d(y, a) \leq d(y, x_{n_i}) + d(x_{n_i}, a) < \underbrace{\text{diam}(C_{n_i})}_{< 1/n_i < \varepsilon/2} + \frac{\varepsilon}{2} < \varepsilon.
> $$
>
> So $C_{n_i} \subseteq B(a, \varepsilon) \subseteq U_\alpha$, contradicting the choice of $C_{n_i}$.

^pf-19-2

> [!remark]- Connections
> - The subdivision step in the [[Path Lifting Lemma|Path Lifting Lemma]], the [[Homotopy Lifting Lemma|Homotopy Lifting Lemma]], and [[§37 The Fundamental Group of Sⁿ#^thm-37-1|Generation by Open Cover]].

> [!theorem] Lemma §19.3: Sequentially Compact $\Rightarrow$ Totally Bounded
> If $(X, d)$ is sequentially compact, then for every $\varepsilon > 0$, there exist finitely many points $x_1, \ldots, x_n$ such that $X = B(x_1, \varepsilon) \cup \cdots \cup B(x_n, \varepsilon)$.

^lem-19-3

> [!proof]+ Proof
> Suppose not: there exists $\varepsilon > 0$ such that no finite collection of $\varepsilon$-balls covers $X$. Build a sequence inductively: pick $x_1 \in X$. Given $x_1, \ldots, x_n$, since $\{B(x_i, \varepsilon)\}_{i=1}^n$ does not cover $X$, choose $x_{n+1} \notin \bigcup_{i=1}^n B(x_i, \varepsilon)$.
>
> By construction, $d(x_i, x_j) \geq \varepsilon$ for all $i \neq j$. So no subsequence can be [[§13 Some Topological Concepts in Metric Spaces#^def-13-3|Cauchy]], hence no subsequence converges. This contradicts sequential compactness.

^pf-19-3

*Uses:* [[§13 Some Topological Concepts in Metric Spaces#^def-13-3|451 Def. §13.3]]

> [!theorem] Theorem §19.4: Equivalence for Metrizable Spaces
> Let $X$ be a [[§12 Metric Topology#^def-12-4|metrizable]] space. Then the following are equivalent:
> 1. $X$ is [[§18 Compact Spaces#^def-18-2|compact]]
> 2. $X$ is [[§19 Limit Point Compactness#^def-19-1|limit point compact]]
> 3. $X$ is [[§19 Limit Point Compactness#^def-19-3|sequentially compact]]

^thm-19-4

> [!proof]+ Proof of $(2) \Rightarrow (3)$
> Let $(x_n)$ be a sequence in $X$.
>
> **Case 1:** If $A = \{x_n \mid n \in \mathbb{Z}_+\}$ is finite, then some value repeats infinitely often, giving a constant (hence convergent) subsequence.
>
> **Case 2:** Assume $A$ is infinite. By (2), $A$ has a limit point $x \in X$.
>
> Construct a subsequence converging to $x$: Since $x$ is a [[§8 Interior and Closure#^def-8-5|limit point]] of $A$, every neighborhood of $x$ contains infinitely many points of $A$. (If some $B(x, \varepsilon)$ contained only finitely many points $a_1, \ldots, a_m$ of $A \setminus \{x\}$, then for $0 < r \le \varepsilon$ with $r < d(x, a_j)$ for all $j$, the ball $B(x, r)$ would miss $A \setminus \{x\}$, but a limit point requires every neighborhood to intersect $A \setminus \{x\}$.)
>
> In particular, $B(x, 1/i) \cap (A \setminus \{x\})$ is infinite for each $i$. So we can inductively choose:
> - $x_{n_1} \in B(x, 1) \cap A$ with $x_{n_1} \neq x$
> - $x_{n_2} \in B(x, \frac{1}{2}) \cap A$ with $n_2 > n_1$ (possible since infinitely many terms of the sequence lie in $B(x, 1/2)$)
> - $x_{n_i} \in B(x, \frac{1}{i}) \cap A$ with $n_i > n_{i-1}$
>
> Then $d(x_{n_i}, x) < 1/i \to 0$, so $x_{n_1}, x_{n_2}, \ldots$ converges to $x$.

^pf-19-4

*Uses:* [[§19 Limit Point Compactness#^thm-19-1|§19.1]], [[§8 Interior and Closure#^def-8-5|Def. §8.5]]

> [!proof]+ Proof of $(3) \Rightarrow (1)$: Sequentially Compact $\Rightarrow$ Compact
> Let $\{U_\alpha\}$ be an open cover of $X$.
>
> **Step 1:** By the [[Lebesgue Number Lemma|Lebesgue number lemma]], there exists $\delta > 0$ such that every set of diameter $< \delta$ lies inside some $U_\alpha$.
>
> **Step 2:** By [[§19 Limit Point Compactness#^lem-19-3|total boundedness]], there exist $x_1, \ldots, x_n$ such that $X = B(x_1, \delta/3) \cup \cdots \cup B(x_n, \delta/3)$.
>
> **Step 3:** Each $B(x_i, \delta/3)$ has diameter $\leq 2\delta/3 < \delta$, so by the Lebesgue number, each $B(x_i, \delta/3) \subseteq U_{\alpha_i}$ for some $\alpha_i$.
>
> Then $\{U_{\alpha_1}, \ldots, U_{\alpha_n}\}$ is a finite subcover.

^pf-19-4-2

*Uses:* [[§19 Limit Point Compactness#^lem-19-2|§19.2]], [[§19 Limit Point Compactness#^lem-19-3|§19.3]]

> [!remark]- Connections
> - Restated for normed and metric spaces as [[§18 Compactness and the Unit Ball#^thm-18-1|556 Thm. §18.1]] (compact iff sequentially compact), which cites this theorem for its proof.

> [!remark] Remark: Summary of the Equivalence
> For a metrizable space $X$, the proof cycle is:
>
> $$
> \text{Compact} \overset{\text{Thm 16.1}}{\Longrightarrow} \text{Limit point compact} \overset{\text{shrinking balls}}{\Longrightarrow} \text{Sequentially compact} \overset{\text{Lebesgue + total bounded}}{\Longrightarrow} \text{Compact}
> $$
>
> ([[§19 Limit Point Compactness#^thm-19-1|Theorem §19.1]], proof of $(2) \Rightarrow (3)$ ([[§19 Limit Point Compactness#^pf-19-4|proof]]), proof of $(3) \Rightarrow (1)$ ([[§19 Limit Point Compactness#^pf-19-4-2|proof]]).)
>
> The metric is essential at every step: $(2) \Rightarrow (3)$ uses shrinking balls $B(x, 1/i)$ to extract subsequences, and $(3) \Rightarrow (1)$ uses the [[Lebesgue Number Lemma|Lebesgue number lemma]] (diameter estimates) and [[§19 Limit Point Compactness#^lem-19-3|total boundedness]] (finite $\varepsilon$-ball covers). None of these arguments work in a general topological space without a metric.

^rem-19-2
