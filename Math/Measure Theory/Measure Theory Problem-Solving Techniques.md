---
type: summary
subject: "[[Measure Theory]]"
tags: [measure-theory, math551]
---
↑ [[Measure Theory]]

# Problem-Solving Techniques

This appendix distills the recurring proof strategies from homework problems in the course. It is organized by technique rather than by topic, so that patterns become visible across different areas of measure theory.

## Technique 1: Reduction to Known Countability Results

Many problems about the “size” of a set reduce to showing it is a subset of, or in bijection with, a known [[§1 Countability and Set Theory#^def-1-8|countable]] set.

> [!remark] Remark: Strategy
> - (i) **Subset method**: Show $A \subseteq B$ where $B$ is known to be countable. (A subset of a countable set is countable.)
> - (ii) **Bijection/injection method**: Construct an explicit [[§1 Countability and Set Theory#^def-1-3|injection]] $A \hookrightarrow \mathbb{N}$ or a [[§1 Countability and Set Theory#^def-1-6|bijection]] $A \leftrightarrow B$ where $B$ is countable.
> - (iii) **Product + union closure**: Use that $A \times B$ is countable if $A, B$ are countable ([[§1 Countability and Set Theory#^ex-1-3|Example §1.3]]), and $\bigcup_{j=1}^\infty A_j$ is countable if each $A_j$ is countable ([[Countable Union of Countable Sets is Countable|Proposition §3.1]]).
> - (iv) **Induction on complexity**: For families indexed by finite tuples (e.g. $\mathbb{N}^j$), prove countability by induction using the product rule.

^rem-19-5

> [!example] Example T1: Applications (HW1)
> - **Finite binary sequences**: $E = \bigcup_{k=1}^\infty \{0,1\}^k \subseteq \bigcup_{k=1}^\infty \mathbb{N}^k$, which is countable by induction + countable union.
> - **Rational balls**: $\mathcal{B} = \{B(r, 1/k)\}$ is in bijection with $\mathbb{Q}^n \times \mathbb{N}$, which is countable by the product rule ([[§6 Open Covers and the Heine–Borel Theorem#^lem-6-2|Lemma §6.2]]; $\mathbb{Q}$ countable by [[§3 Countability of Rationals and Unions#^cor-3-2|Corollary §3.2]]).

^ex-19-8

> [!remark]- Connections
> - Contrast: infinite binary sequences are uncountable, [[§4 Uncountability#^ex-4-1|Example §4.1]].

## Technique 2: The Cantor–Bernstein Squeeze

To show $A \sim B$ ([[§1 Countability and Set Theory#^def-1-7|Def. §1.7]]), it often suffices to find injections in both directions rather than an explicit bijection.

> [!remark] Remark: Strategy
> Construct injections $f: A \hookrightarrow B$ and $g: B \hookrightarrow A$. The [[Cantor–Bernstein Theorem|Cantor–Bernstein–Schröder theorem]] then gives $A \sim B$.

^rem-19-6

> [!example] Example T2: Application (HW1)
> To show $A \sim B$ when $A \subset B \subset C$ and $A \sim C$: the inclusion $A \hookrightarrow B$ and the restriction of a bijection $C \to A$ to $B$ give the two injections.

^ex-19-9

## Technique 3: Subadditivity and Monotonicity Estimates

The workhorse inequalities of [[§9 Lebesgue Outer Measure#^def-9-4|outer measure]]. Nearly every outer measure problem uses one or both ([[Properties of Lebesgue Outer Measure|Proposition §9.1]]).

> [!remark] Remark: Strategy
> - (i) **Upper bound via subadditivity**: $m^{\ast}(A \cup B) \leq m^{\ast}(A) + m^{\ast}(B)$, and more generally $m^{\ast}\!\bigl(\bigcup_k A_k\bigr) \leq \sum_k m^{\ast}(A_k)$ ([[Properties of Lebesgue Outer Measure|Proposition §9.1]](3)).
> - (ii) **Lower bound via monotonicity**: If $A \subseteq B$, then $m^{\ast}(A) \leq m^{\ast}(B)$ ([[Properties of Lebesgue Outer Measure|Proposition §9.1]](2)).
> - (iii) **Difference estimate**: If $m^{\ast}(A) < \infty$, rewrite $B = (B \setminus A) \cup A$ and use subadditivity to get $m^{\ast}(B \setminus A) \geq m^{\ast}(B) - m^{\ast}(A)$.

^rem-19-7

> [!example] Example T3: Applications (HW2 and HW3)
> - **HW2 P1**: $m^{\ast}(B \setminus A) \geq m^{\ast}(B) - m^{\ast}(A)$ follows from $m^{\ast}(B) \leq m^{\ast}((B \setminus A) \cup A) \leq m^{\ast}(B \setminus A) + m^{\ast}(A)$.
> - **HW2 P2**: $m^{\ast}(E) = 0$ for $E = (\mathbb{Q} \times \mathbb{R}) \cup (\mathbb{R} \times \mathbb{Q})$ by bounding each line $\{q\} \times \mathbb{R}$ with shrinking rectangles, then summing over countably many lines (the same $\varepsilon/2^k$ pattern as [[§9 Lebesgue Outer Measure#^ex-9-2|Example §9.2]]).
> - **HW3 P4**: The intersection bound $m\!\bigl(\bigcap E_j\bigr) > 0$ via De Morgan + subadditivity of the complements.

^ex-19-10

## Technique 4: The Carathéodory Splitting Trick

The [[§10 Lebesgue Measurable Sets#^def-10-1|Carathéodory criterion]] $m^{\ast}(T) = m^{\ast}(T \cap A) + m^{\ast}(T \cap A^c)$ is used in two directions: to *prove* measurability by verifying the criterion for all test sets, and to *exploit* known measurability by splitting a test set.

> [!remark] Remark: Strategy
> - (i) **Proving measurability**: Show $m^{\ast}(T) \geq m^{\ast}(T \cap A) + m^{\ast}(T \cap A^c)$ for all $T$ (the reverse inequality is always free from subadditivity; [[§10 Lebesgue Measurable Sets#^rem-10-1|Remark §10.1]]). Often reduce to showing $m^{\ast}(T \cap A) \leq m^{\ast}(T \cap B)$ for some known measurable $B \supseteq A$ or $B \subseteq A$.
> - (ii) **Using measurability**: If $A$ is measurable, split any test set $T$ as $T = (T \cap A) \cup (T \cap A^c)$ and use additivity.
> - (iii) **Sandwiching via measure-zero differences**: If $A_1 \subseteq A_2$ with $m^{\ast}(A_2 \setminus A_1) = 0$, then $m^{\ast}(T \cap A_2) \leq m^{\ast}(T \cap A_1) + 0$ and the criterion transfers from $A_1$ to $A_2$ (compare [[§10 Lebesgue Measurable Sets#^ex-10-1|Example §10.1]]: null sets are measurable).

^rem-19-8

> [!example] Example T4: Applications (HW3 and HW4)
> - **HW3 P1**: $A_1 \subseteq A_2$, $m^{\ast}(A_2) = m(A_1) < \infty$ implies $m^{\ast}(A_2 \setminus A_1) = 0$, so the Carathéodory criterion for $A_1$ transfers to $A_2$.
> - **HW3 P2**: Inclusion–exclusion $m^{\ast}(A \cup B) = m^{\ast}(A) + m^{\ast}(B) - m^{\ast}(A \cap B)$ by splitting the test set $A \cup B$ along the measurable set $A$.
> - **HW4 P1**: The [[§11 Borel Sets and Measure Spaces#^def-11-12|Vitali]] counterexample uses a test set $T' \subseteq [0,1]$ to show $A_2 = (-\infty,0) \cup V$ fails the Carathéodory criterion.

^ex-19-11

> [!remark]- Connections
> - The abstract version of the criterion: [[§11 Borel Sets and Measure Spaces#^def-11-4|Def. §11.4]] and [[Carathéodory's Theorem|Carathéodory's Theorem]]; the splitting in (ii) is how [[§10 Lebesgue Measurable Sets#^lem-10-2|Lemma §10.2]] and [[Lebesgue Measurable Sets Form a σ-Algebra|Theorem §10.3]] are proved.

## Technique 5: $\varepsilon$-Covering and Approximation

Many results are proved by covering a set with slightly “larger” or “nicer” sets, then taking $\varepsilon \to 0$.

> [!remark] Remark: Strategy
> - (i) **L-cover shrinking**: Cover $E$ by open rectangles $\{I_k\}$ ([[§9 Lebesgue Outer Measure#^def-9-3|L-covering]]) with $\sum |I_k| < m^{\ast}(E) + \varepsilon$, then extract finite subcovers via [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|Heine–Borel]] when $E$ is compact.
> - (ii) **$\varepsilon$-enlargement**: Replace a rectangle $I$ by $I_\varepsilon$ (enlarged by $\varepsilon$ in each direction) to get an open cover; take $\varepsilon \to 0$ at the end.
> - (iii) **Inner approximation**: Approximate $E$ from inside by compact sets $K \subseteq E$ with $m(E \setminus K) < \varepsilon$ ([[Inner Regularity of Lebesgue Measure|Theorem §11.10]], [[§11 Borel Sets and Measure Spaces#^thm-11-11|Theorem §11.11]](1)); then use Heine–Borel on $K$.

^rem-19-9

> [!example] Example T5: Applications (HW2 and HW4)
> - **HW2 P3**: Both the upper bound ($m^{\ast}(\bar{I}) \leq |I|$ via $\varepsilon$-enlargement) and lower bound ($m^{\ast}(\operatorname{int}(I)) \geq |I|$ via inner compact approximation + Heine–Borel + grid lemma); this is [[§9 Lebesgue Outer Measure#^prop-9-2|Proposition §9.2]].
> - **HW4 P3**: Approximate $E$ by bounded closed $K$ (inner regularity), then cover $K$ by finitely many rectangles via Heine–Borel to get $m(E \triangle G) < \varepsilon$ ([[§11 Borel Sets and Measure Spaces#^thm-11-11|Theorem §11.11]]).

^ex-19-12

> [!remark]- Connections
> - Heine–Borel in the Topology subject: [[Heine–Borel Theorem]]; outer approximation by open sets is the mirror image, [[Outer Regularity of Lebesgue Measure|Theorem §11.8]].

## Technique 6: Continuity of Measure and Exhaustion

Continuity from below/above converts infinite problems into limits of finite ones.

> [!remark] Remark: Strategy
> - (i) **Continuity from below** ([[Continuity of Measure|Proposition §11.12]]): For $E_1 \subseteq E_2 \subseteq \cdots$ measurable, $m\!\bigl(\bigcup E_n\bigr) = \lim m(E_n)$.
> - (ii) **Continuity from above** ([[§11 Borel Sets and Measure Spaces#^prop-11-13|Proposition §11.13]]): For $E_1 \supseteq E_2 \supseteq \cdots$ measurable with $m(E_1) < \infty$, $m\!\bigl(\bigcap E_n\bigr) = \lim m(E_n)$.
> - (iii) **Measurable exhaustion of outer measure** ([[§11 Borel Sets and Measure Spaces#^thm-11-14|Theorem §11.14]]): If $M_1 \subseteq M_2 \subseteq \cdots$ are measurable with $\bigcup M_n \supseteq E$, then $m^{\ast}(E \cap M_n) \to m^{\ast}(E)$.
> - (iv) **Counterexample pattern**: Continuity from above *fails* without $m(E_1) < \infty$ ([[§11 Borel Sets and Measure Spaces#^rem-11-5|Remark §11.5]]). Standard counterexample: $E_k = \bigcup_{n=1}^\infty (-\frac{1}{2k}+n, \frac{1}{2k}+n)$, each with $m(E_k) = \infty$, but $\bigcap E_k = \mathbb{Z}^+$ has measure zero.

^rem-19-10

> [!example] Example T6: Applications (HW3 and HW4)
> - **HW3 P3**: The IVT argument for $m^{\ast}(A) = a$ uses measurable exhaustion by $M_n = [-n,n]$ to show $g(x) = m^{\ast}(E \cap [-x,x]) \to m^{\ast}(E)$ ([[§11 Borel Sets and Measure Spaces#^thm-11-14|Theorem §11.14]]; see [[#Technique 10: The Intermediate Value Theorem Bridge|Technique 10]]).
> - **HW4 P2**: Counterexample to continuity from above when $m(E_1) = \infty$.
> - **HW4 P3(a)**: Continuity from above applied to $E_k = E \setminus [-k/2, k/2]^n$ ensures the tail vanishes.

^ex-19-13

## Technique 7: Cardinality/Counting Arguments

When measure-theoretic tools are insufficient, cardinality arguments provide existence results.

> [!remark] Remark: Strategy
> - (i) **Countable vs. uncountable**: If $S$ is countable and $\mathbb{R}$ is uncountable ([[§4 Uncountability#^ex-4-2|Example §4.2]]), then $\mathbb{R} \setminus S \neq \varnothing$. This gives *existence* of points avoiding $S$.
> - (ii) **Difference set trick**: To find $x_0$ with $E \cap (E + x_0) = \varnothing$, observe this holds iff $x_0 \notin E - E = \{e_j - e_k\}$, which is countable when $E$ is.
> - (iii) **Heine–Borel + compactness**: Reduce infinite problems to finite ones via the finite intersection property. For a nested sequence of non-empty compact sets $G_1 \supseteq G_2 \supseteq \cdots$, $\bigcap G_k \neq \varnothing$ ([[§5 Topology of ℝⁿ#^thm-5-2|Cantor's Nested Set Theorem]]).

^rem-19-11

> [!example] Example T7: Applications (HW1 and HW2)
> - **HW2 P5**: $E - E$ is countable (surjective image of $E \times E$; [[§1 Countability and Set Theory#^ex-1-3|Example §1.3]]), so $\mathbb{R} \setminus (E - E) \neq \varnothing$ gives the desired $x_0$.
> - **HW2 P4**: The nested compact sets argument forces $\bigcap G_k \neq \varnothing$, contradicting $\bigcap \mathcal{C} = \varnothing$.

^ex-19-14

> [!remark]- Connections
> - Finite intersection property in Topology: [[§15 Compact Spaces#^thm-15-5|590 §15.5]], nested closed sets [[§15 Compact Spaces#^cor-15-6|590 §15.6]].

## Technique 8: Measurability via Preimage Characterization

To show $f$ is [[§12 Measurable Functions#^def-12-2|measurable]], one shows $\{x : f(x) > c\}$ is measurable for all $c \in \mathbb{R}$.

> [!remark] Remark: Strategy
> - (i) **Continuous functions**: If $f$ is continuous on a measurable domain $E$, then $\{f > c\} = (\text{open set}) \cap E$ is measurable ([[§12 Measurable Functions#^ex-12-2|Example §12.2]]).
> - (ii) **a.e. continuous functions**: Split $E = E_1 \cup E_2$ where $f$ is continuous on $E_1$ and $m(E_2) = 0$. Apply the continuous case on $E_1$; the part in $E_2$ is measurable by completeness of Lebesgue measure ([[§10 Lebesgue Measurable Sets#^ex-10-1|Example §10.1]]; [[§12 Measurable Functions#^prop-12-4|Proposition §12.4]]).
> - (iii) **Pointwise limits**: If $f_k \to f$ pointwise and each $f_k$ is measurable, then $f$ is measurable ([[§12 Measurable Functions#^cor-12-8|Corollary §12.8]]) (since $\{f > c\} = \bigcup_m \bigcap_N \bigcup_{k \geq N} \{f_k > c + 1/m\}$).
> - (iv) **Derivatives**: Write $f'(x) = \lim_{k \to \infty} \frac{f(x + h_k) - f(x)}{h_k}$ as a pointwise limit of continuous (hence measurable) functions. Split the domain if needed to keep difference quotients well-defined.
> - (v) **Sup over uncountable families**: $\sup_{a \in \mathcal{I}} f_a$ need *not* be measurable for uncountable $\mathcal{I}$ (contrast the countable case, [[§12 Measurable Functions#^thm-12-6|Theorem §12.6]]). Counterexample: indicator functions of singletons in a [[§11 Borel Sets and Measure Spaces#^def-11-12|Vitali set]].

^rem-19-12

> [!example] Example T8: Applications (HW4)
> - **HW4 P4(a)**: Continuous $f$ on measurable $E$: open ball argument gives $\{f > c\}$ as intersection of an open set with $E$.
> - **HW4 P4(b)**: a.e. continuous $f$: split into continuous part + measure-zero part, use completeness.
> - **HW4 P5**: Derivative as pointwise limit of difference quotients; split $(a,b)$ into two halves for right/left difference quotients.
> - **HW4 P6**: Vitali-set counterexample for uncountable supremum.

^ex-19-15

> [!remark]- Connections
> - The other preimage tests: [[§12 Measurable Functions#^prop-12-2|Proposition §12.2]]; the set-theoretic translation in (iii) is the “logic to set theory” move of [[§12 Measurable Functions#^rem-12-3|Remark §12.3]] and [[§12 Measurable Functions#^thm-12-7|Theorem §12.7]].

## Technique 9: Vitali Set as Universal Counterexample

The [[§11 Borel Sets and Measure Spaces#^def-11-12|Vitali set]] $V \subset [0,1]$ serves as the go-to non-measurable set ([[The Vitali Set is Not Measurable|Theorem §11.20]]) for constructing counterexamples.

> [!remark] Remark: Strategy
> - (i) **Extending to infinite measure**: $A_2 = (-\infty, 0) \cup V$ has $m^{\ast}(A_2) = \infty$ but is non-measurable. This exploits the fact that $\infty = \infty$ gives no information.
> - (ii) **Indicator function trick**: $\chi_V$ is non-measurable since $\{\chi_V > 1/2\} = V$ ([[§12 Measurable Functions#^def-12-2|Def. §12.2]]). This builds non-measurable *functions* from non-measurable sets.
> - (iii) **Uncountable supremum**: Index singletons of $V$ by $\alpha$, let $f_\alpha = \chi_{\{x_\alpha\}}$ (each measurable). Then $\sup_\alpha f_\alpha = \chi_V$ is non-measurable.

^rem-19-13

## Technique 10: The Intermediate Value Theorem Bridge

When a measure-theoretic quantity depends continuously on a parameter, the IVT ([[Intermediate Value Theorem]]) gives existence of desired intermediate values.

> [!remark] Remark: Strategy
> - (i) Define a function $g(t) = m^*(E \cap S_t)$ where $\{S_t\}$ is a continuous family of sets (e.g., $S_t = [-t, t]$).
> - (ii) Show $g$ is continuous (typically via Lipschitz estimate from [[Properties of Lebesgue Outer Measure|subadditivity]]).
> - (iii) Show $g(0) = 0$ and $\lim_{t \to \infty} g(t) = m^*(E)$ (via [[§11 Borel Sets and Measure Spaces#^thm-11-14|measurable exhaustion]]).
> - (iv) Apply [[Intermediate Value Theorem|IVT]] to conclude: for any $0 < a < m^*(E)$, there exists $t_a$ with $g(t_a) = a$.

^rem-19-14

> [!example] Example T10: Application (HW3)
> **HW3 P3**: For $E \subset \mathbb{R}$ with $m^{\ast}(E) > 0$ and $0 < a < m^{\ast}(E)$, the function $g(x) = m^{\ast}(E \cap [-x,x])$ is continuous with $g(0) = 0$ and $g \to m^{\ast}(E)$. The IVT gives $A = E \cap [-x_a, x_a]$ with $m^{\ast}(A) = a$.

^ex-19-16

## Technique 11: Level Set Exhaustion and Truncation

To reduce a problem about general measurable functions to one about *bounded* measurable functions, exhaust the domain by the level sets $E_n = \{|f| < n\}$.

> [!remark] Remark: Strategy
> - (i) Define $E_n = \{x \in E : |f(x)| < n\}$. Each $E_n$ is measurable ([[§12 Measurable Functions#^prop-12-2|Proposition §12.2]]), and $E_n \nearrow E_0 = \{f \text{ finite}\}$.
> - (ii) If $f$ is [[§12 Measurable Functions#^def-12-5|a.e.]] finite and $m(E) < \infty$, then $m(E_0) = m(E)$, so [[Continuity of Measure|continuity of measure from below]] gives $m(E_0 \setminus E_N) < \varepsilon$ for $N$ large enough.
> - (iii) Define a truncated function $g$ that agrees with $f$ on $E_N$ and is set to a constant (e.g., $N$) elsewhere. Then $g$ is bounded, measurable, and $\{g \neq f\}$ has measure $< \varepsilon$.
>
> This reduces “a.e. finite measurable” to “bounded measurable” at the cost of an arbitrarily small exceptional set—the same “excise a small bad set” philosophy as [[Egorov's Theorem|Egorov]] and [[Lusin's Theorem|Lusin]] ([[§12 Measurable Functions|Sections 12]]–[[§13 Egorov's and Lusin's Theorems|13]]; [[§13 Egorov's and Lusin's Theorems#^rem-13-3|Remark §13.3]]).

^rem-19-15

> [!example] Example T11: Application (HW5)
> **HW5 P1**: Given $f$ a.e. finite and measurable on $E$ with $m(E) < \infty$, the level sets $E_N = \{|f| < N\}$ exhaust $E$ up to a null set. Setting $g = f$ on $E_N$ and $g = N$ elsewhere yields a bounded measurable function with $m(\{g \neq f\}) < \varepsilon$.

^ex-19-17

## Technique 12: Iterated $\varepsilon$-Extraction

When a theorem provides a “good” set for each tolerance $\varepsilon > 0$, applying it repeatedly with $\varepsilon = 1/n$ and taking the union (or intersection) upgrades the conclusion from “arbitrarily small error” to “zero error.”

> [!remark] Remark: Strategy
> - (i) **Given**: A theorem of the form “for every $\delta > 0$, there exists a set $F_\delta$ such that $m(\text{bad set}) < \delta$ and a good property holds on $F_\delta$.”
> - (ii) **Apply** with $\delta = 1/n$ to obtain a sequence $\{F_n\}$ of good sets.
> - (iii) **Take $K = \bigcup_n F_n$** (or $\bigcap_n$ for complements). Then $m(E \setminus K) \leq m(E \setminus F_n) < 1/n$ for all $n$, so $m(E \setminus K) = 0$.
> - (iv) **Conclude**: the good property holds on all of $K$, and $E \setminus K$ is a null set where completeness of Lebesgue measure ([[§10 Lebesgue Measurable Sets#^ex-10-1|Example §10.1]]) handles any remaining issues.
>
> This technique converts “almost” results into “up to a null set” results. The key insight is that the *intersection of countably many measure-$< 1/n$ sets* has measure zero.

^rem-19-16

> [!example] Example T12: Applications (HW5)
> - **HW5 P2**: Apply [[Egorov's Theorem|Egorov's theorem]] with $\varepsilon = 1/n$ to get $A_n$ with $m(A_n) < 1/n$ and $f_k \to f$ uniformly on $E_n = [a,b] \setminus A_n$. Then $m([a,b] \setminus \bigcup E_n) = m(\bigcap A_n) = 0$, and convergence is uniform on each $E_n$.
> - **HW5 P3 (converse of [[Lusin's Theorem|Lusin]])**: Apply the Lusin-type hypothesis with $\delta = 1/j$ to get closed $F_j$ with $f$ continuous on $F_j$ and $m(E \setminus F_j) < 1/j$. Then $K = \bigcup F_j$ satisfies $m(E \setminus K) = 0$, so $f$ is measurable on $K$ (continuous on each $F_j$; [[§12 Measurable Functions#^ex-12-2|Example §12.2]], [[§12 Measurable Functions#^prop-12-4|Proposition §12.4]]) and on $E \setminus K$ (null set, completeness).

^ex-19-18

> [!remark]- Connections
> - The same $1/n$ extraction produces the $G_\delta$/$F_\sigma$ hulls in [[Outer Regularity of Lebesgue Measure|Theorem §11.8]](2) and [[Inner Regularity of Lebesgue Measure|Theorem §11.10]](2).

## Technique 13: Shift-and-Subtract for Monotone Sequences

Many convergence theorems ([[Monotone Convergence Theorem (Lebesgue)|MCT]], [[Fatou's Lemma|Fatou]]) require non-negative functions. When dealing with decreasing or signed sequences, subtract a known integrable function to reduce to the non-negative increasing case.

> [!remark] Remark: Strategy
> Given a *decreasing* sequence $f_k \searrow f$ with $\int f_{k_0} < \infty$: define $g_k = f_{k_0} - f_k \geq 0$, so $g_k \nearrow f_{k_0} - f$. Apply MCT to $\{g_k\}$, then use the subtraction rule ($\int f_{k_0} < \infty$) to recover the result for $\{f_k\}$. For *increasing* sequences with $f_1 \in L(E)$: define $g_k = f_k - f_1 \geq 0$ and apply MCT.

^rem-19-17

> [!example] Example T13
> - **HW6 P1(a)**: MCT for decreasing sequences ([[§14 The Lebesgue Integral for Simple Functions#^thm-14-14|Theorem §14.14]]) — subtract $f_{k_0}$ to get increasing non-negative $g_k = f_{k_0} - f_k$, apply MCT, then use finiteness of $\int f_{k_0}$ to subtract back.
> - **HW8 P1(a)**: MCT for increasing sequences not necessarily non-negative — subtract $f_1 \in L(E)$ to get $g_k = f_k - f_1 \geq 0$, apply MCT, then add $\int f_1$ back ([[§15 The General Lebesgue Integral#^thm-15-2|linearity, Theorem §15.2]]).

^ex-19-19

> [!remark]- Connections
> - The signed decreasing version and the increasing/decreasing hypothesis table: [[§14 The Lebesgue Integral for Simple Functions#^rem-14-5|Remark §14.5]].

## Technique 14: DCT for Parameter-Dependent Integrals

To show continuity (or differentiability) of $F(t) = \int_E f(x, t)\,dx$ in the parameter $t$: take $t_n \to t_0$, verify pointwise convergence $f(x, t_n) \to f(x, t_0)$ for each $x$, find a dominating function $|f(x, t_n)| \leq G(x) \in L(E)$ uniform in $n$, and apply [[Dominated Convergence Theorem|DCT]].

> [!remark] Remark: Strategy
> The dominating function often comes from bounding the parameter range. For example, if $t \in (a, b)$ and the integrand involves $x^t$, bound $x^t \leq x^a + x^b$ (using $x < 1$ vs. $x \geq 1$ case split). The key insight: the dominating function must be independent of $n$.

^rem-19-18

> [!example] Example T14
> - **HW7 P5**: Continuity of $F(t) = \int_0^\infty x^t f(x)\,dx$ on $(a, b)$ — dominate by $(x^a + x^b)|f(x)| \in L$.
> - **HW8 P3**: Continuity of $F(t) = \int_{E \cap [-t,t]^n} f\,dx$ — dominate by $|f| \in L$, then apply [[Intermediate Value Theorem|IVT]] to find $t_0$ with $F(t_0) = r/3$.
> - **HW9 P3**: $\int f \cdot g_\varepsilon \to \int f \cdot \chi_{[a,b]}$ via DCT with trapezoidal bumps $g_\varepsilon \to \chi_{[a,b]}$ a.e. (as in [[Continuous Functions of Compact Support are Dense in L¹|Theorem §16.7]]), dominated by $|f|$.

^ex-19-20

## Technique 15: Density Bootstrap

To prove a result for all $f \in L(E)$: first prove it for a “nice” dense subclass (step functions, $C_c$, or simple functions; [[§16 The L¹ Space and Density Theorems#^thm-16-5|§16.5]], [[§16 The L¹ Space and Density Theorems#^thm-16-6|§16.6]], [[Continuous Functions of Compact Support are Dense in L¹|§16.7]]), then extend to all of $L$ via the density $\|f - \varphi\|_1 < \varepsilon$ and the [[§15 The General Lebesgue Integral#^prop-15-3|triangle inequality]].

> [!remark] Remark: Strategy
> The pattern is: (1) approximate $f$ by a nice function $\varphi$ with $\|f - \varphi\|_1 < \varepsilon/(2C)$ where $C$ is a constant from the problem; (2) handle the “nice” case exactly; (3) bound the error $|T(f) - T(\varphi)|$ using Hölder-type estimates ([[Hölder's Inequality|Theorem §19.5]]). This works whenever the quantity $T(f)$ is continuous in $\|f\|_1$.

^rem-19-19

> [!example] Example T15
> - **HW9 P2**: $\int f \cdot g_k \to 0$ for bounded $g_k$ with $\int_a^c g_k \to 0$ — prove for step functions (telescoping), extend to $L^1$ via $\|f - \varphi\|_1 < \varepsilon/(2M)$.
> - **HW9 P3**: $\int fg = 0$ for all $g \in C_c$ implies $f = 0$ a.e. — prove $\int_a^b f = 0$ via $C_c$ bumps (DCT), extend to step functions (linearity), then show $\int f^2 = 0$ by approximating $f$ by step functions (compare [[§15 The General Lebesgue Integral#^ex-15-2|Example §15.2]]).
> - **Total variation of integrals** ([[§18 Differentiation Theory#^thm-18-8|Section 18, Theorem §18.8]]): $\bigvee(F) \geq \int |f|$ — prove equality for step functions, extend to $L^1$ via $\|f - h\|_1 < \varepsilon$.

^ex-19-21

> [!remark]- Connections
> - The approximation chain being bootstrapped: [[§16 The L¹ Space and Density Theorems#^rem-16-1|Remark §16.1]]; its $L^p$ version [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|Theorem §19.19]]. Another instance: [[§17 Invariance Properties and Fubini's Theorem#^thm-17-2|Average Continuity]].

## Technique 16: Fatou Squeeze on Complementary Sets

To show $\int_e f_k \to \int_e f$ for a measurable subset $e \subseteq E$, when you know $f_k \to f$ a.e. and $\int_E f_k \to \int_E f$: apply [[Fatou's Lemma|Fatou's lemma]] on both $e$ and $E \setminus e$ simultaneously.

> [!remark] Remark: Strategy
> Fatou on $e$: $\int_e f \leq \liminf \int_e f_k$. Fatou on $E \setminus e$: $\int_{E \setminus e} f \leq \liminf \int_{E \setminus e} f_k$. Since $\int_E f_k = \int_e f_k + \int_{E \setminus e} f_k \to \int_E f$ ([[§14 The Lebesgue Integral for Simple Functions#^cor-14-13|Corollary §14.13]]), use the identity $\limsup\, a_k = c - \liminf\, b_k$ (when $a_k + b_k \to c$) to get $\limsup \int_e f_k \leq \int_e f$. The two bounds squeeze: $\lim \int_e f_k = \int_e f$.

^rem-19-20

> [!example] Example T16
> - **HW8 P4**: $f_k \to f$ a.e. on $E$, $\int_E f_k \to \int_E f$ $\Rightarrow$ $\int_e f_k \to \int_e f$ for every measurable $e \subset E$.

^ex-19-22

> [!remark]- Connections
> - The same two-sided squeeze (Fatou + reverse Fatou) proves [[Dominated Convergence Theorem|DCT]] from [[§15 The General Lebesgue Integral#^thm-15-6|Theorem §15.6]] and [[§15 The General Lebesgue Integral#^thm-15-7|Theorem §15.7]].

## Technique 17: Tonelli Swap for Integral Identities

To prove an identity of the form $\int_Y F(y)\,dy = \int_X G(x)\,dx$: express both sides as a double integral $\iint H(x,y)\,dx\,dy$ and swap the order of integration via [[Tonelli's Theorem|Tonelli]] (non-negative case) or [[Fubini's Theorem (Lebesgue)|Fubini]] (integrable case).

> [!remark] Remark: Strategy
> The key step is recognizing that a single integral hides a double integral. Typical pattern: a level-set integral $\int_0^\infty m(\{f > y\})\,dy$ equals $\int_0^\infty \int_E \chi_{\{f > y\}}(x)\,dx\,dy$; swapping gives $\int_E \int_0^{f(x)} dy\,dx = \int_E f$. Always check non-negativity (Tonelli) or integrability (Fubini) before swapping.

^rem-19-21

> [!example] Example T17
> - **HW10 P4**: $\int_0^\infty F(y)\,dy = \int_E fg\,dx$ where $F(y) = \int_{\{g > y\}} f$ — write the LHS as $\iint f(x)\chi_{\{g(x)>y\}}\,dx\,dy$, apply Tonelli, evaluate inner integral $\int_0^{g(x)} dy = g(x)$.
> - **Layer cake formula** ([[§17 Invariance Properties and Fubini's Theorem#^thm-17-13|Section 17, Theorem §17.13]]): $\int_E |f|^p = \int_0^\infty p\lambda^{p-1} m(\{|f| > \lambda\})\,d\lambda$ — same Tonelli swap.
> - **HW9 P4**: $f(x) + g(y)$ integrable on $E \times E$ implies $f, g \in L(E)$ — Fubini gives $\int_E |f(x) + g(y_0)|\,dx < \infty$ for a.e. $y_0$, then triangle inequality.

^ex-19-23

> [!remark]- Connections
> - Measurability of the swapped integrand $\chi_{\{f > y\}}(x)$ is the [[§17 Invariance Properties and Fubini's Theorem#^thm-17-11|Subgraph Theorem]]; the Riemann counterpart of the swap is the MATH 452 [[Fubini's Theorem]]; [[§17 Invariance Properties and Fubini's Theorem#^rem-17-3|Remark §17.3]] shows why integrability is needed for Fubini.

## Technique 18: Explicit Counterexample via Divergent Series

To show a hypothesis is necessary, construct a counterexample where the conclusion fails. A common pattern: build a function (or sequence) using a divergent series ($\sum 1/k$; [[§14 Series#^thm-14-5|451 §14.5]]) or a set of infinite measure to violate the conclusion while satisfying all other hypotheses.

> [!remark] Remark: Strategy
> For “$\int f_{k_0} < \infty$ is necessary”: choose $f_k$ constant on an infinite-measure set so $\int f_k = \infty$ for all $k$ but $f_k \to 0$ ([[§14 The Lebesgue Integral for Simple Functions#^rem-14-6|Remark §14.6]]). For “$g$ must be a.e. bounded”: build $f = \sum \frac{1}{j^2 m(A_j)} \chi_{A_j}$ where $|g| > k_j$ on $A_j$, ensuring $\int |fg| \geq \sum 1/j = \infty$. The convergent series $\sum 1/j^2$ makes $f \in L$; the divergent series $\sum 1/j$ makes $fg \notin L$.

^rem-19-22

> [!example] Example T18
> - **HW6 P1(b)**: $f_k = 1/k$ on $\mathbb{R}$: $\int f_k = \infty$ for all $k$, but $f_k \to 0$ with $\int f = 0$.
> - **HW8 P1(b)**: $f_k = -\chi_{\{|x|>k\}}$: increasing, $\int f_k = -\infty$ for all $k$, but $f_k \to 0$ with $\int f = 0$.
> - **HW8 P5(b)**: If $g$ is unbounded on every co-null set, construct $f = \sum \frac{1}{j^2 m(A_{k_j}')} \chi_{A_{k_j}'}$ with $\int |f| = \sum 1/j^2 < \infty$ but $\int |fg| \geq \sum k_j/j^2 \geq \sum 1/j = \infty$.
> - **HW10 P5(a)**: $f(x) = x\sin(\pi/x)$ not [[§18 Differentiation Theory#^def-18-new1|BV]] — partition at $x_k = 2/(2k+1)$ gives variation $\geq \sum 1/(k+2)$, divergent (compare [[§18 Differentiation Theory#^ex-18-3|Example §18.3]]).

^ex-19-24

> [!remark]- Connections
> - HW8 P5(b) is the converse of the $p = 1$, $p' = \infty$ case of [[Hölder's Inequality|Hölder's inequality]]: $fg \in L$ for all $f \in L$ forces $g \in L^\infty$.

## Technique 19: Pointwise Bounds via Lebesgue Differentiation

To show $|f(x)|^2 \leq g'(x)$ a.e. from an integral inequality: divide by the interval length, take the limit as the interval shrinks to a point, and use the fact that a.e. point is a [[§18 Differentiation Theory#^def-18-5|Lebesgue point]] ([[§18 Differentiation Theory#^thm-18-26|Theorem §18.26]]).

> [!remark] Remark: Strategy
> Given $|\int_a^b f|^2 \leq \Phi(a,b)$ for all $[a,b]$: fix a Lebesgue point $x_0$ of $f$ (a.e. point qualifies), divide by $(b - a)^2$, and take $b \to x_0^+$. The left side becomes $|f(x_0)|^2$ by the Lebesgue point property, the right side becomes a derivative. This converts an integral bound into a pointwise bound, which you can then integrate.

^rem-19-23

> [!example] Example T19
> - **HW12 P4**: $|\int_a^b f|^2 \leq (g(b) - g(a))(b-a)$ with $g$ increasing. Divide by $(b-a)^2$: LHS $\to |f(x_0)|^2$ at Lebesgue points, RHS $\to g'(x_0)$ where $g$ is differentiable ([[Lebesgue's Differentiation Theorem for Monotone Functions|Theorem §18.9]](i)). So $f^2 \leq g'$ a.e., giving $\int f^2 \leq \int g' \leq g(1) - g(0) < \infty$ ([[Lebesgue's Differentiation Theorem for Monotone Functions|Theorem §18.9]](iii)).

^ex-19-25

## Technique 20: Chaining AC $\varepsilon$-$\delta$ Conditions

To show a composition $g \circ f$ is [[§18 Differentiation Theory#^def-18-4|AC]]: use the AC condition for $f$ to translate “small total interval length” into “small total image length,” then feed that into the AC condition for $g$.

> [!remark] Remark: Strategy
> Given $\varepsilon > 0$: (1) get $\delta_2$ from AC of $g$ (with tolerance $\varepsilon$); (2) get $\delta_1$ from AC of $f$ (with tolerance $\delta_2$). Then $\sum |x_{k+1} - x_k| < \delta_1 \implies \sum |f(x_{k+1}) - f(x_k)| < \delta_2 \implies \sum |g(f(x_{k+1})) - g(f(x_k))| < \varepsilon$. Key requirement: $f$ must be [[§18 Properties of Continuous Functions#^def-18-2|strictly monotone]] so the image intervals are disjoint.

^rem-19-24

> [!example] Example T20
> - **HW12 P5**: $f$ strictly increasing AC, $g$ AC $\implies$ $g \circ f$ AC. The strict monotonicity ensures $(f(x_k), f(x_{k+1}))$ are disjoint, so the AC condition for $g$ applies.

^ex-19-26

> [!remark]- Connections
> - AC compared with uniform continuity: [[§18 Differentiation Theory#^rem-18-7|Remark §18.7]].

## Technique 21: FTC + MCT for Series of Monotone AC Functions

To show $\sum f_n \in AC$ when each $f_n$ is increasing and AC: use the [[Fundamental Theorem of Calculus for Lebesgue Integrals|FTC]] to write each $f_n$ as a constant plus an integral, swap sum and integral via MCT ([[§14 The Lebesgue Integral for Simple Functions#^thm-14-12|MCT II]]) (exploiting $f_n' \geq 0$), then recognize the result as a constant plus an integral of an $L^1$ function.

> [!remark] Remark: Strategy
> Write $f_n(x) = f_n(a) + \int_a^x f_n'$. Sum: $\sum f_n(x) = \sum f_n(a) + \sum \int_a^x f_n'$. Since $f_n' \geq 0$ (increasing), MCT gives $\sum \int f_n' = \int \sum f_n'$. Check $\sum f_n' \in L^1$: evaluate at $x = b$ to get $\int_a^b \sum f_n' = \sum(f_n(b) - f_n(a)) < \infty$. Conclude: $\sum f_n = \text{const} + \int(L^1 \text{ function}) \in AC$ ([[§18 Differentiation Theory#^thm-18-12|Theorem §18.12]]).

^rem-19-25

> [!example] Example T21
> - **HW12 P6**: $\sum f_n$ with $f_n$ increasing AC converging pointwise. FTC + MCT gives $\sum f_n(x) = \sum f_n(a) + \int_a^x \sum f_n'$. Finiteness: $\int \sum f_n' = \sum(f_n(b) - f_n(a)) < \infty$ by convergence of the series at $b$ and $a$.
> - **HW11 P4**: Term-by-term differentiation of monotone series (same MCT swap, but the conclusion is $(\sum f_n)' = \sum f_n'$ rather than AC membership).

^ex-19-27

> [!remark]- Connections
> - The general (non-monotone) version: [[§18 Differentiation Theory#^cor-18-14|Corollary §18.14]], which requires $\sum \int |g_k'| < \infty$ in place of $g_k' \geq 0$.
> - The Riemann-integral FTC it upgrades: [[Fundamental Theorem of Calculus]].
