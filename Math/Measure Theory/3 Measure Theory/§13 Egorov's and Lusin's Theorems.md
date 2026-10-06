---
type: section
subject: "[[Measure Theory]]"
chapter: 3
section: 13
tags: [measure-theory, math551]
---
← [[§12 Measurable Functions]] · ↑ [[· 3 Measure Theory]] · [[§14 The Lebesgue Integral for Simple Functions]] →

## Egorov's Theorem

Egorov's theorem states that on sets of finite measure, [[§12 Measurable Functions#^def-12-8|almost everywhere convergence]] is “almost” [[§12 Measurable Functions#^def-12-9|uniform convergence]].

> [!theorem] Theorem §13.1: Egorov's Theorem
> Let $E \in \mathcal{M}$ with $m(E) < \infty$. Let $f, f_1, f_2, \ldots$ be a sequence of [[§12 Measurable Functions#^ex-12-3|a.e. finite]] [[§12 Measurable Functions#^def-12-2|measurable functions]] on $E$ such that $f_k \to f$ a.e. on $E$.
>
> Then for all $\delta > 0$, there exists a measurable set $E_\delta \subseteq E$ with $m(E_\delta) < \delta$ such that $f_k \to f$ **uniformly** on $E \setminus E_\delta$.

^thm-13-1

> [!proof]+ Proof of Egorov's Theorem
> **Step 1: Reduction to finite-valued $f$.**
>
> Let $A = \{x \in E : |f(x)| = \infty\}$. By assumption, $m(A) = 0$. Let $Z$ be the measure zero set where $f_k \not\to f$. We work on $E_0 = E \setminus (A \cup Z)$, where $f$ is finite-valued and $f_k \to f$ pointwise. Since $m(A \cup Z) = 0$, it suffices to prove the theorem on $E_0$.
>
> WLOG, assume $f(x) \in \mathbb{R}$ for all $x \in E$ and $f_k(x) \to f(x)$ for all $x \in E$.
>
> **Step 2: Define the key sets.**
>
> For $j, \ell \in \mathbb{N}$, [[§12 Measurable Functions#^def-12-10|define]]:
>
> $$
> E_\ell^{(j)} = \bigcup_{k=\ell}^{\infty} \left\{ x \in E : |f_k(x) - f(x)| \geq \frac{1}{j} \right\}.
> $$
>
> **Step 3: Properties of $E_\ell^{(j)}$.**
>
> - (a) *Decreasing in $\ell$*: $E_\ell^{(j)} \supseteq E_{\ell+1}^{(j)}$ since we take fewer sets in the union as $\ell$ increases.
> - (b) *Intersection has measure zero*:
>
>   $$
>   \bigcap_{\ell=1}^{\infty} E_\ell^{(j)} = \left\{ x \in E : |f_k(x) - f(x)| \geq \frac{1}{j} \text{ for infinitely many } k \right\}.
>   $$
>
>   Since $f_k \to f$ pointwise on $E$, for each $x \in E$ and each $j$, eventually $|f_k(x) - f(x)| < \frac{1}{j}$. Thus $\bigcap_{\ell=1}^{\infty} E_\ell^{(j)} = \emptyset$, so $m\left(\bigcap_{\ell=1}^{\infty} E_\ell^{(j)}\right) = 0$.
>
> **Step 4: Apply continuity of measure from above.**
>
> Since $E_\ell^{(j)} \searrow \emptyset$ as $\ell \to \infty$ and $m(E_1^{(j)}) \leq m(E) < \infty$, by [[§11 Borel Sets and Measure Spaces#^prop-11-13|continuity of measure]]:
>
> $$
> \lim_{\ell \to \infty} m(E_\ell^{(j)}) = m\left(\bigcap_{\ell=1}^{\infty} E_\ell^{(j)}\right) = 0.
> $$
>
> **Step 5: Choose $\ell_j$ for each $j$.**
>
> Given $\delta > 0$, for each $j \in \mathbb{N}$, choose $\ell_j$ large enough that:
>
> $$
> m(E_{\ell_j}^{(j)}) < \frac{\delta}{2^j}.
> $$
>
> **Step 6: Define $E_\delta$ and verify uniform convergence.**
>
> Let $E_\delta = \bigcup_{j=1}^{\infty} E_{\ell_j}^{(j)}$. Then:
>
> $$
> m(E_\delta) \leq \sum_{j=1}^{\infty} m(E_{\ell_j}^{(j)}) < \sum_{j=1}^{\infty} \frac{\delta}{2^j} = \delta.
> $$
>
> On $E \setminus E_\delta$:
>
> $$
> E \setminus E_\delta = \bigcap_{j=1}^{\infty} (E \setminus E_{\ell_j}^{(j)}) = \bigcap_{j=1}^{\infty} \bigcap_{k=\ell_j}^{\infty} \left\{ x \in E : |f_k(x) - f(x)| < \frac{1}{j} \right\}.
> $$
>
> This means: for all $j \in \mathbb{N}$ and all $k \geq \ell_j$, we have $|f_k(x) - f(x)| < \frac{1}{j}$ for all $x \in E \setminus E_\delta$.
>
> Given $\epsilon > 0$, choose $j$ with $\frac{1}{j} < \epsilon$. Then for all $k \geq \ell_j$ and all $x \in E \setminus E_\delta$:
>
> $$
> |f_k(x) - f(x)| < \frac{1}{j} < \epsilon.
> $$
>
> The bound $\ell_j$ depends only on $j$ (equivalently, $\epsilon$), not on $x$. This is [[§12 Measurable Functions#^def-12-9|uniform convergence]].

^pf-13-1

*Uses:* [[§12 Measurable Functions#^def-12-2|Def. §12.2]], [[§12 Measurable Functions#^ex-12-3|Ex. §12.3]], [[§12 Measurable Functions#^def-12-8|Def. §12.8]], [[§12 Measurable Functions#^def-12-10|Def. §12.10]], [[§11 Borel Sets and Measure Spaces#^prop-11-13|§11.13]], [[Properties of Lebesgue Outer Measure|§9.1]], [[§12 Measurable Functions#^def-12-9|Def. §12.9]], [[§14 Series#^ex-14-4|451 Ex. §14.4]], [[Archimedean Property|451 Archimedean Property]]

> [!remark]- Connections
> - MATH 451 uniform convergence: [[§24 Uniform Convergence#^def-24-2|451 Definition §24.2]].
> - Applied with $\delta = 1/n$ in [[Measure Theory Problem-Solving Techniques#^ex-19-18|Technique 12: Iterated ε-Extraction (HW5 P2)]].

> [!example] Example §13.1: Illustration of Egorov's Theorem
> Let $f_k(x) = x^k$ for $x \in [0, 1]$. Then $f_k \to f$ pointwise where $f(x) = 0$ for $0 \leq x < 1$ and $f(1) = 1$.
>
> The convergence is **not uniform** on $[0, 1]$ ([[§12 Measurable Functions#^ex-12-4|Example §12.4]]): for $0 \leq x < 1$, we need $x^k < \epsilon$, which requires $k > \frac{\ln \epsilon}{\ln x} \to \infty$ as $x \to 1^-$.
>
> However, for any $\delta > 0$, the convergence **is uniform** on $[0, 1 - \delta]$:
>
> $$
> \sup_{x \in [0, 1-\delta]} x^k = (1 - \delta)^k < \epsilon \quad \text{when } k > \frac{\ln \epsilon}{\ln(1 - \delta)}.
> $$
>
> This bound is independent of $x$, so convergence is uniform on $[0, 1 - \delta]$. Applying this with $\delta/2$ in place of $\delta$, the set $E_\delta = (1 - \delta/2, 1]$ in Egorov's Theorem has measure $\delta/2 < \delta$.

^ex-13-1

![[m551-13-1.svg]]
*Egorov for $f_k(x) = x^k$ on $[0,1]$: the convergence to $0$ on $[0,1)$ is not uniform, since every $x^k$ climbs back to $1$ near $x = 1$. Cutting away a set of length $\delta$ (red) cures this: on $[0, 1-\delta]$ we have $x^k \leq (1-\delta)^k$, which is below $\epsilon$ for all large $k$ (here $k = 16, 32$), at every $x$ at once.*

> [!remark]- Connections
> - MATH 451 version of the non-uniformity: [[§24 Uniform Convergence#^ex-24-2|451 Example §24.2]]; the sup test used here is [[§24 Uniform Convergence#^thm-24-1|451 Theorem §24.1]].

> [!remark] Remark: Finite Measure is Necessary
> The assumption $m(E) < \infty$ is essential. Consider $f_k = \chi_{[k, k+1]}$ on $E = \mathbb{R}$. Then $f_k \to 0$ pointwise (for each $x$, eventually $x \notin [k, k+1]$), but on any set $A$ with $m(\mathbb{R} \setminus A) < \infty$, we have $[k, k+1] \cap A \neq \emptyset$ for large $k$, so $\sup_{x \in A} f_k(x) = 1$ does not converge to $0$.

^rem-13-1

![[m551-13-2.svg]]
*Why Egorov needs $m(E) < \infty$: $f_k = \chi_{[k,k+1]}$ is a bump sliding off to infinity. At each fixed $x$ (red) the values are eventually $0$, so $f_k \to 0$ pointwise, but $\sup f_k = 1$ for every $k$. Removing a set of finite measure cannot stop the bump, which eventually meets whatever remains.*

> [!remark]- Connections
> - Finiteness is exactly the hypothesis of [[§11 Borel Sets and Measure Spaces#^prop-11-13|continuity from above]] used in Step 4; compare [[§14 The Lebesgue Integral for Simple Functions#^rem-14-6|Why the Finiteness Hypothesis is Necessary]] for decreasing MCT.

## Lusin's Theorem

Lusin's theorem states that measurable functions are “almost continuous”: outside a set of arbitrarily small measure, a measurable function agrees with a continuous function.

> [!theorem] Lemma §13.2: Distance Between Disjoint Compact Sets
> Let $F_1, F_2 \subseteq \mathbb{R}^n$ be nonempty, bounded, closed (hence compact, by [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|Heine–Borel]]), and disjoint sets. Then $d(F_1, F_2) > 0$, where
>
> $$
> d(F_1, F_2) = \inf\{d(x, y) : x \in F_1, y \in F_2\}.
> $$

^lem-13-2

> [!proof]+ Proof
> Choose sequences $\{x_j\} \subseteq F_1$ and $\{y_j\} \subseteq F_2$ such that $d(x_j, y_j) \to d(F_1, F_2)$.
>
> Since $F_1$ and $F_2$ are bounded, these sequences are bounded. By the [[§5 Topology of ℝⁿ#^thm-5-1|Bolzano–Weierstrass theorem]], there exist convergent subsequences $x_{j_k} \to x_0$ and $y_{j_k} \to y_0$.
>
> Since $F_1$ and $F_2$ are [[§5 Topology of ℝⁿ#^def-5-3|closed]], $x_0 \in F_1$ and $y_0 \in F_2$.
>
> By continuity of the distance function:
>
> $$
> d(F_1, F_2) = \lim_{k \to \infty} d(x_{j_k}, y_{j_k}) = d(x_0, y_0).
> $$
>
> Since $F_1 \cap F_2 = \emptyset$, we have $x_0 \neq y_0$, so $d(F_1, F_2) = d(x_0, y_0) > 0$.

^pf-13-2

*Uses:* [[Characterization of the Supremum|451 Characterization of the Supremum]], [[§5 Topology of ℝⁿ#^thm-5-1|§5.1]], [[§5 Topology of ℝⁿ#^def-5-3|Def. §5.3]], [[§11 Metric Topology#^thm-11-9|590 §11.9]]

![[m551-13-3.svg]]
*Lemma §13.2. Left: for disjoint compact $F_1$, $F_2$ the infimum of distances is attained at some $x_0 \in F_1$, $y_0 \in F_2$ (by Bolzano–Weierstrass), so $d(F_1, F_2) = d(x_0, y_0) > 0$. Right: without boundedness this fails. The closed sets $F_1$ (a ray of the $x$-axis) and $F_2$ (a branch of a hyperbola) are disjoint, but the gap between them (red) shrinks to $0$.*

> [!remark]- Connections
> - Same compactness-via-sequences mechanism in general metric spaces: [[§16 Limit Point Compactness#^thm-16-2|590 Theorem §16.2]], and the uniform-radius statement [[Lebesgue Number Lemma]].
> - Merely closed disjoint sets can be at distance $0$; they are still separated by open sets since metric spaces are normal: [[§20 Normal Spaces#^thm-20-1|590 Theorem §20.1]].
> - MATH 451 Bolzano–Weierstrass in $\mathbb{R}^n$: [[§13 Some Topological Concepts in Metric Spaces#^thm-13-3|451 Theorem §13.3]].

> [!theorem] Theorem §13.3: Lusin's Theorem
> Let $f$ be a real-valued [[§12 Measurable Functions#^def-12-2|measurable function]] on $E \in \mathcal{M}$.
>
> Then for all $\delta > 0$, there exists a closed set $F \subseteq E$ with $m(E \setminus F) < \delta$ such that $f$ is continuous on $F$.

^thm-13-3

> [!proof]+ Proof
> **Step 1: Simple functions.**
>
> Assume $f$ is a [[§12 Measurable Functions#^prop-12-13|simple measurable function]]:
>
> $$
> f(x) = \sum_{i=1}^{k} a_i \chi_{A_i}(x),
> $$
>
> where $A_1, \ldots, A_k$ are disjoint measurable sets with $\bigcup_{i=1}^{k} A_i \subseteq E$.
>
> Let $A_0 = E \setminus \bigcup_{i=1}^{k} A_i$ (where $f = 0$). By the [[Inner Regularity of Lebesgue Measure|approximation theorem for measurable sets]], for each $i = 0, 1, \ldots, k$, there exists a closed set $F_i \subseteq A_i$ with
>
> $$
> m(A_i \setminus F_i) < \frac{\delta}{k+1}.
> $$
>
> Let $F = \bigcup_{i=0}^{k} F_i$. Then:
>
> $$
> E \setminus F \subseteq \bigcup_{i=0}^{k} (A_i \setminus F_i), \quad \text{so} \quad m(E \setminus F) \leq \sum_{i=0}^{k} m(A_i \setminus F_i) < (k+1) \cdot \frac{\delta}{k+1} = \delta.
> $$
>
> *Claim*: $f$ is continuous on $F$.
>
> *Proof of claim*: Since $A_i$ are disjoint, so are $F_i$. Thus $F_i \cap F_j = \emptyset$ for $i \neq j$. On each $F_i$, $f$ is constant (equal to $a_i$).
>
> To show continuity at $x_0 \in F_i$: by [[§13 Egorov's and Lusin's Theorems#^lem-13-2|Lemma §13.2]], for any bounded region, the distance between $F_i \cap \overline{B(0, R)}$ and $F_j \cap \overline{B(0, R)}$ is positive for $i \neq j$. Thus there exists $r > 0$ such that $B(x_0, r) \cap F \subseteq F_i$, so $f$ is constant on $B(x_0, r) \cap F$.
>
> **Step 2: Bounded measurable functions.**
>
> Assume $f$ is bounded and measurable on $E$.
>
> By the [[§12 Measurable Functions#^thm-12-17|uniform approximation theorem]], there exists a sequence of simple measurable functions $\{\varphi_k\}$ such that $\varphi_k \to f$ uniformly on $E$.
>
> By Step 1, for each $k$, there exists a closed set $F_k \subseteq E$ with $m(E \setminus F_k) < \frac{\delta}{2^k}$ such that $\varphi_k$ is continuous on $F_k$.
>
> Let $F = \bigcap_{k=1}^{\infty} F_k$. Then $F$ is closed, and:
>
> $$
> E \setminus F = \bigcup_{k=1}^{\infty} (E \setminus F_k), \quad \text{so} \quad m(E \setminus F) \leq \sum_{k=1}^{\infty} m(E \setminus F_k) < \sum_{k=1}^{\infty} \frac{\delta}{2^k} = \delta.
> $$
>
> Since $F \subseteq F_k$ for all $k$, each $\varphi_k$ is continuous on $F$. Since $\varphi_k \to f$ uniformly on $E$ (hence on $F$), and [[§12 Measurable Functions#^thm-12-16|uniform limits of continuous functions are continuous]], $f$ is continuous on $F$.
>
> **Step 3: General real-valued measurable functions.**
>
> Let $f$ be a real-valued (possibly unbounded) measurable function on $E$.
>
> Define:
>
> $$
> g(x) = \frac{f(x)}{1 + |f(x)|}.
> $$
>
> Then $|g(x)| < 1$ for all $x$, so $g$ is bounded. Also, $g$ is measurable: $g = h \circ f$ with $h(t) = \frac{t}{1+|t|}$ continuous, so for $c \in \mathbb{R}$ the set $h^{-1}((c, \infty))$ is open, hence a countable union of open intervals $(a_j, b_j)$ ([[Open Sets in ℝ are Countable Unions of Disjoint Open Intervals|Prop. §7.1]]), and $\{g > c\} = \bigcup_j \bigl(\{f > a_j\} \cap \{f < b_j\}\bigr)$ is measurable ([[§12 Measurable Functions#^prop-12-2|Prop. §12.2]]).
>
> By Step 2, there exists a closed set $F \subseteq E$ with $m(E \setminus F) < \delta$ such that $g$ is continuous on $F$.
>
> To recover $f$ from $g$: if $g = \frac{a}{1+|a|}$, then:
>
> $$
> a = \frac{g}{1 - |g|}.
> $$
>
> (If $a > 0$: $g = \frac{a}{1+a}$, so $g + ag = a$, thus $a = \frac{g}{1-g}$. If $a < 0$: $g = \frac{a}{1-a}$, so $g - ag = a$, thus $a = \frac{g}{1+g}$. Both cases give $a = \frac{g}{1-|g|}$.)
>
> Thus $f(x) = \frac{g(x)}{1 - |g(x)|}$ on $F$. Since $g$ is continuous on $F$ and $|g| < 1$, the function $f = \frac{g}{1-|g|}$ is [[§17 Continuous Functions#^thm-17-3|continuous]] on $F$.

^pf-13-3

*Uses:* [[§12 Measurable Functions#^def-12-2|Def. §12.2]], [[§12 Measurable Functions#^prop-12-13|§12.13]], [[Inner Regularity of Lebesgue Measure|§11.10]], [[Properties of Lebesgue Outer Measure|§9.1]], [[§13 Egorov's and Lusin's Theorems#^lem-13-2|§13.2]], [[§5 Topology of ℝⁿ#^def-5-1|Def. §5.1]], [[§12 Measurable Functions#^thm-12-17|§12.17]], [[§12 Measurable Functions#^thm-12-16|§12.16]], [[§12 Measurable Functions#^thm-12-3|§12.3]], [[Open Sets in ℝ are Countable Unions of Disjoint Open Intervals|§7.1]], [[§12 Measurable Functions#^prop-12-2|§12.2]], [[§6 Closed Sets and Limit Points#^thm-6-1|590 §6.1]], [[§9 Continuous Functions#^thm-9-4|590 §9.4]], [[§24 Uniform Convergence#^thm-24-2|451 §24.2]], [[§17 Continuous Functions#^thm-17-2|451 §17.2]], [[§17 Continuous Functions#^thm-17-3|451 §17.3]], [[§14 Series#^ex-14-4|451 Ex. §14.4]]

![[m551-13-4.svg]]
*Step 1 of Lusin's theorem, with the $A_i$ drawn as intervals for simplicity. Inside each $A_i$ we choose a closed $F_i$ (thick) with $m(A_i \setminus F_i)$ small; what is removed, $E \setminus F$ (red), is a small set around the jumps of $f$ (dotted). On $F = F_0 \cup F_1 \cup F_2$ the function equals the constant $a_i$ on each $F_i$, and different $F_i$ are a positive distance apart (Lemma §13.2), so $f|_F$ is locally constant, hence continuous.*

> [!remark]- Connections
> - “Continuous on $F$” means $f|_F$ is continuous in the [[§5 Subspace Topology#^def-5-1|subspace topology]]; by the (not covered) [[§20 Normal Spaces#^rem-20-3|Tietze Extension Theorem]] on the normal space $\mathbb{R}^n$, $f|_F$ then extends to a continuous function on all of $\mathbb{R}^n$.
> - Converse (HW5 P3): [[Measure Theory Problem-Solving Techniques#^ex-19-18|Technique 12: Iterated ε-Extraction]]; continuous approximation in norm: [[Continuous Functions of Compact Support are Dense in L¹|Theorem §16.7]].

> [!remark] Remark: Interpretation of Lusin's Theorem
> Lusin's theorem says that every measurable function is “nearly continuous”: we can remove a set of arbitrarily small measure to make the function continuous. This is often stated as: “Every measurable function is continuous except on a set of arbitrarily small measure.”
>
> Combined with [[Egorov's Theorem|Egorov's theorem]], we see that measurable functions and a.e. convergence are “almost” as well-behaved as continuous functions and uniform convergence.

^rem-13-2

> [!remark] Remark: Core Philosophy of Egorov and Lusin (Sections 12–13)
> The theorems of [[Egorov's Theorem|Egorov]] and [[Lusin's Theorem|Lusin]] share a single organizing principle: **measurability buys near-regularity**. Given any $\delta > 0$, we can excise a set of measure less than $\delta$ from the domain so that the remaining behavior becomes “classical”:
>
> | **Theorem** | **Remove $m < \delta$** | **Upgrade on remainder** |
> |---|---|---|
> | Egorov | $m(E \setminus F) < \delta$ | a.e. convergence $\to$ uniform convergence |
> | Lusin | $m(E \setminus F) < \delta$ | measurable function $\to$ continuous function |
>
> In other words, the “pathology” of measurable functions and pointwise convergence is always confined to an arbitrarily small set. By sacrificing a negligible portion of the domain, we recover the strong analytical tools — uniform convergence and continuity — that make classical analysis work. This perspective recurs throughout measure theory and integration: *measure-theoretic hypotheses yield conclusions that are as strong as their topological counterparts, up to sets of arbitrarily small measure*.

^rem-13-3

> [!remark]- Connections
> - The same “excise a small bad set” strategy: [[Measure Theory Problem-Solving Techniques#^rem-19-15|Technique 11: Level Set Exhaustion and Truncation]] and [[Measure Theory Problem-Solving Techniques#^rem-19-16|Technique 12: Iterated ε-Extraction]].
