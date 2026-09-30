---
type: section
subject: "[[Topology]]"
chapter: 5
section: 15
munkres: "§26, §27"
tags: [topology, math590]
---
← [[Topology §14 Connected Subspaces of ℝ]] · ↑ [[Topology — 5 Compactness]] · [[Topology §16 Limit Point Compactness]] →

$[a, b] \subseteq \mathbb{R}$ compact $\Rightarrow$ [[Extreme Value Theorem]].

## Definition and Examples

> [!definition] Definition §15.1: Covering
> A collection $\mathcal{A}$ of subsets of $X$ is a **covering of $X$** if the union of elements of $\mathcal{A}$ equals $X$, i.e., $\bigcup_{A \in \mathcal{A}} A = X$.
>
> It is an **open covering** if elements of $\mathcal{A}$ are open subsets of $X$.

^def-15-1

> [!definition] Definition §15.2: Compact
> A space $X$ is **compact** if every open covering of $X$ contains a finite subcollection that also covers $X$. (Finite subcover of $X$.)

^def-15-2

> [!remark] Remark: Why Compactness Matters
> Compactness is the topological generalization of “finiteness.” It captures the essential properties of closed bounded sets in $\mathbb{R}^n$ that make analysis work:
>
> **1. Compactness = “almost finite.”** A compact space behaves like a finite space in many ways: every open cover reduces to a finite one, every sequence has a convergent subsequence (in metric spaces, [[Topology §16 Limit Point Compactness#^thm-16-2|Theorem §16.2]]), and continuous functions achieve their bounds.
>
> **2. Key theorems that require compactness:**
> - *[[Extreme Value Theorem]]:* $f: X \to \mathbb{R}$ continuous, $X$ compact $\Rightarrow$ $f$ achieves max and min.
> - *Uniform continuity:* $f: X \to Y$ continuous, $X$ compact metric $\Rightarrow$ $f$ uniformly continuous.
> - *Closed and bounded:* In $\mathbb{R}^n$, compact $\Leftrightarrow$ closed and bounded ([[Heine–Borel Theorem|Heine-Borel]]).
>
> **3. Why open covers?** The definition may seem odd, but open covers capture “local-to-global” behavior. If a property holds “locally” (on each open set of a cover), compactness lets you patch finitely many local pieces into a global result.
>
> **4. Compactness is a topological property.** Unlike “bounded” (which requires a metric), compactness is preserved by homeomorphisms and makes sense in any topological space.

^rem-15-1

> [!remark]- Connections
> - MATH 451 versions on $[a,b]$: [[Extreme Value Theorem]], [[Single Variable Analysis §19 Uniform Continuity#^thm-19-1|Uniform Continuity on Closed Bounded Intervals]].

> [!example] Example §15.1
> $\mathbb{R}$ is not compact. $\mathcal{A} = \{(n, n+3) \mid n \in \mathbb{Z}\}$ is an open covering of $\mathbb{R}$, but no finite subcover covers $\mathbb{R}$.

^ex-15-1

> [!example] Example §15.2
> Any finite topological space is compact. Any open cover is already finite.

^ex-15-2

> [!example] Example §15.3
> The interval $(0, 1] \subseteq \mathbb{R}$ is not compact. $\mathcal{A} = \{(\frac{1}{n}, 1] \mid n \in \mathbb{Z}_+\}$ is an open covering, no finite subcover.

^ex-15-3

![[m590-15-1.svg]]
*The cover $\{(\frac1n,1]\}$ of $(0,1]$ (gray) creeps toward $0$ but never reaches it: any finitely many members have union $(\frac1N,1]$ for the largest $N$ used, so a whole interval $(0,\frac1N]$ (red) stays uncovered. The missing endpoint $0$ is exactly what destroys compactness.*

> [!example] Example §15.4
> $X = \{0\} \cup \{\frac{1}{n} \mid n \in \mathbb{Z}_+\} \subseteq \mathbb{R}$. $X$ is compact.

^ex-15-4

> [!proof]+ Proof
> Let $\mathcal{A}$ be an open covering of $X$. There exists element $U \in \mathcal{A}$ with $0 \in U$.
>
> Since $U$ is open in the [[Topology §5 Subspace Topology#^def-5-1|subspace topology]] of $X$, we have $U = V \cap X$ for some open $V$ in $\mathbb{R}$. Since $0 \in V$ and $V$ is open in $\mathbb{R}$, there exists $\varepsilon > 0$ such that $(-\varepsilon, \varepsilon) \subseteq V$.
>
> Thus $U$ contains all points $\frac{1}{n}$ with $\frac{1}{n} < \varepsilon$, i.e., all but finitely many points of $X$. Let $y_1, \ldots, y_k$ be the finitely many points of $X$ not in $U$.
>
> For each $y_i$, choose $U_{y_i} \in \mathcal{A}$ containing $y_i$. Then $\{U, U_{y_1}, \ldots, U_{y_k}\}$ is a finite subcover of $X$.

^pf-ex-15-4

*Uses:* [[Topology §5 Subspace Topology#^def-5-1|Def. §5.1]]

![[m590-15-2.svg]]
*Why $\{0\}\cup\{\frac1n\}$ is compact: the one set $U\ni 0$ (red) contains $(-\varepsilon,\varepsilon)\cap X$ and so swallows the entire tail of the sequence; only finitely many points $y_1,\dots,y_k$ (here $1,\frac12,\frac13$) are left, and one more cover element each (gray) finishes the job.*

> [!remark]- Connections
> - This $X$ reappears as the one-point compactification of $\{1/n\} \cong \mathbb{Z}_+$: [[Topology §17 Local Compactness#^ex-17-6|Example §17.6]].

## Compactness in Subspaces

> [!definition] Definition §15.3: Covers a Subspace
> If $Y \subseteq X$ is a subspace, a collection $\mathcal{A}$ of subsets of $X$ is said to **cover** $Y$ if the union of its elements contains $Y$: $\bigcup_{A \in \mathcal{A}} A \supseteq Y$.

^def-15-3

> [!remark] Remark: Covering of $X$ vs. Covers $Y$
> These are different notions:
> - **Covering of $X$**: The sets in $\mathcal{A}$ are subsets of $X$, and their union *equals* $X$.
> - **Covers $Y$** (where $Y \subseteq X$): The sets in $\mathcal{A}$ may be subsets of a larger ambient space $X$, and their union only needs to *contain* $Y$.
>
> **Example:** $Y = [0,1] \subseteq \mathbb{R}$.
> - $\{(-1, 0.6), (0.4, 2)\}$ **covers** $Y$ (union contains $[0,1]$), but is NOT a covering **of** $Y$ (the sets aren't subsets of $Y$).
> - $\{[0, 0.6), (0.4, 1]\}$ is a covering **of** $Y$ (sets are subsets of $Y$, union equals $Y$).
>
> [[Topology §15 Compact Spaces#^lem-15-1|The lemma below]] shows that for compactness, these two perspectives are equivalent.

^rem-15-2

> [!theorem] Lemma §15.1: Compactness in Subspaces
> Let $Y$ be a subspace of $X$. Then $Y$ is compact if and only if every covering of $Y$ by open sets of $X$ contains a finite subcollection covering $Y$.

^lem-15-1

> [!proof]+ Proof
> $(\Rightarrow)$ Let $\mathcal{A} = \{A_\alpha\}_{\alpha \in J}$ be open sets in $X$ covering $Y$, and suppose $Y$ is compact.
>
> Then $\{A_\alpha \cap Y\}$ is a collection of open sets in $Y$ (by definition of [[Topology §5 Subspace Topology#^def-5-1|subspace topology]]) that covers $Y$. Since $Y$ is compact, there exists a finite subcover $A_{\alpha_1} \cap Y, \ldots, A_{\alpha_n} \cap Y$.
>
> Since $Y \subseteq \bigcup_{i=1}^n (A_{\alpha_i} \cap Y) \subseteq \bigcup_{i=1}^n A_{\alpha_i}$, the sets $A_{\alpha_1}, \ldots, A_{\alpha_n}$ cover $Y$.
>
> $(\Leftarrow)$ Let $\mathcal{A}' = \{A_\alpha'\}$ be open sets in $Y$ which cover $Y$. Want to show there exists a finite subcover.
>
> By definition of subspace topology, each $A_\alpha' = A_\alpha \cap Y$ for some open $A_\alpha$ in $X$. The collection $\{A_\alpha\}$ covers $Y$ (since $\{A_\alpha'\}$ does).
>
> By hypothesis, there exists a finite subcollection $A_{\alpha_1}, \ldots, A_{\alpha_n}$ covering $Y$.
>
> Then $A_{\alpha_1}' = A_{\alpha_1} \cap Y, \ldots, A_{\alpha_n}' = A_{\alpha_n} \cap Y$ is a finite subcover of $Y$.

^pf-15-1

*Uses:* [[Topology §5 Subspace Topology#^def-5-1|Def. §5.1]]

> [!remark] Remark: The Subspace-Covering Correspondence
> This lemma reflects a deeper structural correspondence. Let $Y \subseteq X$ be a subspace.
>
> **Two Perspectives on Open Sets:**
>
> | | **Intrinsic** | **Extrinsic** |
> |---|---|---|
> | Objects | Open sets in $Y$ | Open sets in $X$ |
> | Coverings | $\{U_\alpha\}$ with $\bigcup U_\alpha = Y$ | $\{V_\alpha\}$ with $\bigcup V_\alpha \supseteq Y$ |
> | Terminology | “Covering **of** $Y$” | “Covers $Y$” |
>
> **The Bridge (Restriction):** There is a natural surjection
>
> $$
> r: \{\text{open sets in } X\} \to \{\text{open sets in } Y\}, \quad V \mapsto V \cap Y
> $$
>
> Every open set in $Y$ arises this way (by definition of [[Topology §5 Subspace Topology#^def-5-1|subspace topology]]).
>
> **The Correspondence:**
>
> $$
> \begin{aligned}
> \{V_\alpha\} \text{ covers } Y \text{ in } X \quad &\xrightarrow{\quad r \quad} \quad \{V_\alpha \cap Y\} \text{ is a covering of } Y \\
> \{U_\alpha\} \text{ covering of } Y \quad &\xrightarrow{\text{extend}} \quad \{V_\alpha\} \text{ covers } Y \text{ (where } V_\alpha \cap Y = U_\alpha\text{)}
> \end{aligned}
> $$
>
> **Key Property:** Finite subcovers correspond:
>
> $$
> \{V_\alpha\} \text{ has finite subcollection covering } Y \iff \{V_\alpha \cap Y\} \text{ has finite subcover of } Y
> $$
>
> **Why This Matters:**
> - *Compactness is intrinsic* — it doesn't depend on the ambient space.
> - *But the extrinsic view is often more useful:*
>     - “Closed $\subseteq$ Compact $\Rightarrow$ Compact ([[Closed Subspace of a Compact Space is Compact|§15.2]])”: Add $X \setminus Y$ to get a cover of $X$.
>     - “Compact $\subseteq$ Hausdorff $\Rightarrow$ Closed ([[Compact Subspace of a Hausdorff Space is Closed|§15.4]])”: Use Hausdorff property of $X$ to separate points.

^rem-15-3

## Compact Subspaces and Closed Sets

> [!theorem] Theorem §15.2: Closed Subspace of Compact is Compact
> Every closed subspace of a compact space is compact.

^thm-15-2

> [!proof]+ Proof
> $Y$ closed in compact $X$. Want to show $Y$ compact. Let $\mathcal{A}$ be a covering of $Y$ by open sets in $X$ ([[Topology §15 Compact Spaces#^lem-15-1|Lemma §15.1]]).
>
> $\mathcal{B} = \mathcal{A} \cup \{X \setminus Y\}$ is an open cover of $X$. (Note: $X \setminus Y$ is open since $Y$ is [[Topology §6 Closed Sets and Limit Points#^def-6-1|closed]].)
>
> $X$ compact $\Rightarrow$ there exists a finite subcover $\{B_1, \ldots, B_n\} \subseteq \mathcal{B}$ covering $X$.
>
> Each $B_i$ is either an element of $\mathcal{A}$ or equals $X \setminus Y$. Since $Y \cap (X \setminus Y) = \emptyset$, the elements from $\mathcal{A}$ in this finite collection must cover $Y$. Thus $\mathcal{A}$ has a finite subcollection covering $Y$.

^pf-15-2

*Uses:* [[Topology §15 Compact Spaces#^lem-15-1|§15.1]], [[Topology §6 Closed Sets and Limit Points#^def-6-1|Def. §6.1]]

> [!theorem] Theorem §15.3: Continuous Image of Compact is Compact
> The image of a compact space under a continuous map is compact.

^thm-15-3

> [!proof]+ Proof
> $f: X \to Y$ continuous, $X$ compact. WTS $f(X)$ compact.
>
> Let $\mathcal{A}$ be an open covering of $f(X)$ (by sets open in $f(X)$, or equivalently by sets open in $Y$, by [[Topology §15 Compact Spaces#^lem-15-1|Lemma §15.1]]).
>
> Consider $\{f^{-1}(A) \mid A \in \mathcal{A}\}$. Each $f^{-1}(A)$ is open in $X$ (since $f$ is [[Topology §9 Continuous Functions#^def-9-1|continuous]]). This collection covers $X$: if $x \in X$, then $f(x) \in f(X) \subseteq \bigcup \mathcal{A}$, so $f(x) \in A$ for some $A \in \mathcal{A}$, hence $x \in f^{-1}(A)$.
>
> $X$ compact $\Rightarrow$ there exists a finite subcover $f^{-1}(A_1), \ldots, f^{-1}(A_n)$.
>
> Then $A_1, \ldots, A_n$ cover $f(X)$: if $y \in f(X)$, then $y = f(x)$ for some $x \in X$. Since $x \in f^{-1}(A_i)$ for some $i$, we have $y = f(x) \in A_i$.

^pf-15-3

*Uses:* [[Topology §15 Compact Spaces#^lem-15-1|§15.1]], [[Topology §9 Continuous Functions#^def-9-1|Def. §9.1]]

> [!remark]- Connections
> - With $Y = \mathbb{R}$ this is the source of the MATH 451 [[Extreme Value Theorem]]: $f([a,b])$ is compact, hence closed and bounded ([[Heine–Borel Theorem|Heine-Borel]]).

> [!theorem] Theorem §15.4: Compact Subspace of Hausdorff is Closed
> Every compact subspace of a Hausdorff space is closed.

^thm-15-4

> [!proof]+ Proof
> $Y$ compact $\subseteq X$ [[Topology §8 Hausdorff Spaces#^def-8-1|Hausdorff]]. We prove $X \setminus Y$ is open.
>
> Let $x \in X \setminus Y$. We'll show there exists a neighborhood of $x$ disjoint from $Y$.
>
> For each $y \in Y$, since $X$ is Hausdorff and $x \neq y$, there exist disjoint open neighborhoods $U_y \ni x$ and $V_y \ni y$.
>
> The collection $\{V_y\}_{y \in Y}$ is an open cover of $Y$. Since $Y$ is compact, there exists a finite subcover $V_{y_1}, \ldots, V_{y_n}$ ([[Topology §15 Compact Spaces#^lem-15-1|Lemma §15.1]]).
>
> Let $V = \bigcup_{i=1}^{n} V_{y_i}$ and $U = \bigcap_{i=1}^{n} U_{y_i}$.
>
> Then $V \supseteq Y$ (since $\{V_{y_i}\}$ covers $Y$), and $U$ is an open neighborhood of $x$ (finite intersection of open sets containing $x$).
>
> **Claim:** $U \cap V = \emptyset$.
>
> *Proof:* If $z \in V$, then $z \in V_{y_i}$ for some $i$. Since $U_{y_i} \cap V_{y_i} = \emptyset$ and $U \subseteq U_{y_i}$, we have $z \notin U$.
>
> Thus $U$ is an open neighborhood of $x$ disjoint from $Y$. Since $x \in X \setminus Y$ was arbitrary, $X \setminus Y$ is open, so $Y$ is closed.

^pf-15-4

*Uses:* [[Topology §8 Hausdorff Spaces#^def-8-1|Def. §8.1]], [[Topology §15 Compact Spaces#^lem-15-1|§15.1]]

![[m590-15-3.svg]]
*The proof in one picture: for each $y\in Y$ Hausdorff gives disjoint $U_y\ni x$ (gray) and $V_y\ni y$ (blue); compactness cuts the $V_y$ down to finitely many, so the intersection $U=\bigcap U_{y_i}$ (red) is still open. It is a neighborhood of $x$ missing all of $Y$. Without the finite subcover we would need $\bigcap_{y\in Y}U_y$, and an infinite intersection of open sets need not be open.*

> [!remark]- Connections
> - The same point-by-point separation argument, applied twice, proves [[Topology §20 Normal Spaces#^thm-20-2|Every Compact Hausdorff Space is Normal]].

> [!remark] Remark: Summary: Compact and Closed
> - $A$ closed $\subseteq X$ compact $\Rightarrow$ $A$ compact ([[Closed Subspace of a Compact Space is Compact|Theorem §15.2]]).
> - $B$ compact $\subseteq Y$ Hausdorff $\Rightarrow$ $B$ closed ([[Compact Subspace of a Hausdorff Space is Closed|Theorem §15.4]]).

^rem-15-4

> [!remark] Remark: Book Material
> [[Topology §15 Compact Spaces#^thm-15-5|The following theorem]] (Munkres 26.9) was not covered in lecture but is important. It will be removed if covered later, or kept as supplementary material.

^rem-15-5

> [!definition] Definition §15.4: Finite Intersection Property
> A collection $\mathcal{C}$ of subsets of $X$ is said to have the **finite intersection property** (FIP) if for every finite subcollection $\{C_1, \ldots, C_n\}$ of $\mathcal{C}$, the intersection $C_1 \cap \cdots \cap C_n$ is nonempty.

^def-15-4

> [!theorem] Theorem §15.5: Compactness via Finite Intersection Property
> Let $X$ be a topological space. Then $X$ is compact if and only if for every collection $\mathcal{C}$ of closed sets in $X$ having the finite intersection property, the intersection $\bigcap_{C \in \mathcal{C}} C$ is nonempty.

^thm-15-5

> [!proof]+ Proof
> The proof uses contrapositive and complements. Given a collection $\mathcal{A}$ of subsets of $X$, let $\mathcal{C} = \{X \setminus A \mid A \in \mathcal{A}\}$ be the collection of complements. Then:
> 1. $\mathcal{A}$ is a collection of open sets $\Longleftrightarrow$ $\mathcal{C}$ is a collection of closed sets.
> 2. $\mathcal{A}$ covers $X$ $\Longleftrightarrow$ $\bigcap_{C \in \mathcal{C}} C = \emptyset$. (De Morgan: $X \setminus \bigcup \mathcal{A} = \bigcap \mathcal{C}$.)
> 3. A finite subcollection $\{A_1, \ldots, A_n\}$ covers $X$ $\Longleftrightarrow$ the corresponding intersection $C_1 \cap \cdots \cap C_n = \emptyset$ (where $C_i = X \setminus A_i$).
>
> Now we translate:
>
> **Compact:** “Every open cover has a finite subcover.”
>
> **Contrapositive:** “If no finite subcollection of $\mathcal{A}$ covers $X$, then $\mathcal{A}$ does not cover $X$.”
>
> **Via complements:** “If every finite intersection of elements of $\mathcal{C}$ is nonempty, then $\bigcap \mathcal{C}$ is nonempty.”
>
> This is exactly the FIP condition.

^pf-15-5

> [!theorem] Corollary §15.6: Nested Sequence of Closed Sets
> Let $X$ be a compact space. If $C_1 \supseteq C_2 \supseteq C_3 \supseteq \cdots$ is a nested sequence of nonempty closed sets in $X$, then $\bigcap_{n=1}^{\infty} C_n \neq \emptyset$.

^cor-15-6

> [!proof]+ Proof
> The collection $\mathcal{C} = \{C_n\}_{n \in \mathbb{Z}_+}$ automatically has the [[Topology §15 Compact Spaces#^def-15-4|FIP]]: any finite subcollection $\{C_{n_1}, \ldots, C_{n_k}\}$ has intersection $C_{\max\{n_i\}} \neq \emptyset$ (since the sets are nested and each $C_n$ is nonempty).
>
> By [[Topology §15 Compact Spaces#^thm-15-5|the theorem]], $\bigcap_{n=1}^{\infty} C_n \neq \emptyset$.

^pf-15-6

*Uses:* [[Topology §15 Compact Spaces#^def-15-4|Def. §15.4]], [[Topology §15 Compact Spaces#^thm-15-5|§15.5]]

> [!theorem] Theorem §15.7: Bijection from Compact to Hausdorff
> Let $f: X \to Y$ be a bijective continuous function. If $X$ is compact and $Y$ is Hausdorff, then $f$ is a homeomorphism.

^thm-15-7

> [!remark] Remark: Why This Theorem is Powerful
> Normally, showing $f$ is a homeomorphism requires proving $f^{-1}$ is continuous—often tedious. This theorem gives it for free when $X$ is compact and $Y$ is Hausdorff.
>
> **The key insight:** Compactness of $X$ and Hausdorffness of $Y$ force $f$ to be a closed map:
>
> $$
> A \text{ closed in } X \overset{\text{compact}}{\Longrightarrow} A \text{ compact} \overset{f \text{ cts}}{\Longrightarrow} f(A) \text{ compact} \overset{\text{Hausdorff}}{\Longrightarrow} f(A) \text{ closed in } Y
> $$
>
> **Applications:**
> - Proving quotient maps are homeomorphisms (when the quotient is Hausdorff).
> - Showing that a continuous bijection from $S^1$ to $S^1$ is automatically a homeomorphism.
> - Verifying that “gluing” constructions yield the expected spaces.

^rem-15-6

> [!proof]+ Proof
> Since $f$ is a continuous bijection, we only need to show $f^{-1}$ is continuous, i.e., $f$ is an [[Topology §12 Quotient Topology#^def-12-4|open map]] ([[Topology §9 Continuous Functions#^prop-9-2|Proposition §9.2]]), or equivalently, $f$ is a closed map.
>
> We show $f$ is a closed map. Let $A$ be closed in $X$.
> 1. $A$ is compact ([[Closed Subspace of a Compact Space is Compact|closed subset of compact space is compact]]).
> 2. $f(A)$ is compact ([[Continuous Image of a Compact Space is Compact|continuous image of compact is compact]]).
> 3. $f(A)$ is closed ([[Compact Subspace of a Hausdorff Space is Closed|compact subset of Hausdorff space is closed]]).
>
> Thus $f$ maps closed sets to closed sets, so $f$ is a closed map, hence a homeomorphism.

^pf-15-7

*Uses:* [[Topology §12 Quotient Topology#^def-12-4|Def. §12.4]], [[Topology §9 Continuous Functions#^prop-9-2|§9.2]], [[Closed Subspace of a Compact Space is Compact|§15.2]], [[Continuous Image of a Compact Space is Compact|§15.3]], [[Compact Subspace of a Hausdorff Space is Closed|§15.4]]

> [!remark]- Connections
> - The compact-to-Hausdorff shortcut for quotient maps: [[Topology §12 Quotient Topology#^thm-12-5|Product of Quotient Maps (Compact-Hausdorff Case)]].
> - Used to get local homeomorphisms in $p: \mathbb{R} \to S^1$ is a Covering Map ([[Topology §24 Covering Spaces#^thm-24-2|§24.2]]).

> [!theorem] Theorem §15.8: Finite Product of Compact Spaces
> The product of finitely many compact spaces is compact.

^thm-15-8

To prove this, we first establish a key lemma:

> [!theorem] Lemma §15.9: Tube Lemma
> Let $X$ and $Y$ be topological spaces with $Y$ compact. If $N$ is an open set of $X \times Y$ containing the “slice” $x_0 \times Y = \{x_0\} \times Y$, then $N$ contains some “tube” $W \times Y$ about $x_0 \times Y$, where $W$ is a neighborhood of $x_0$ in $X$.

^lem-15-9

> [!remark] Remark: Tube Lemma Intuition
> The Tube Lemma says: if an open set $N$ contains a vertical slice $\{x_0\} \times Y$, it must contain a “fattened” tube $W \times Y$ around that slice.
>
> *Why is compactness of $Y$ essential?* Without compactness, the open set $N$ might “pinch” closer and closer to the slice as you move along $Y$, never leaving room for a uniform tube. Compactness forces the “pinching” to stop after finitely many steps, guaranteeing a tube of positive width.
>
> *Counterexample without compactness:* Let $Y = \mathbb{R}$, $X = \mathbb{R}$, and $N = \{(x, y) : |x| < 1/(|y|+1)\}$. Then $N$ contains $\{0\} \times \mathbb{R}$, but no tube $(-\varepsilon, \varepsilon) \times \mathbb{R}$ fits inside $N$.

^rem-15-7

![[m590-15-5.svg]]
*The counterexample with $Y=\mathbb{R}$: the open set $N=\{|x|<1/(|y|+1)\}$ (blue) contains the slice $\{0\}\times\mathbb{R}$ but pinches toward it as $|y|\to\infty$. Every candidate tube $(-\varepsilon,\varepsilon)\times\mathbb{R}$ (red dashed) escapes $N$ once $|y|>\frac1\varepsilon-1$ (red regions). Covering the non-compact slice takes infinitely many basis boxes, and their widths have no positive lower bound.*

> [!proof]+ Proof
> For each $y \in Y$, the point $(x_0, y) \in N$. Since $N$ is open, there exists a [[Topology §4 Product Topology#^def-4-1|basis element]] $B_y \times C_y$ such that $(x_0, y) \in B_y \times C_y \subseteq N$.
>
> The collection $\{C_y\}_{y \in Y}$ is an open covering of $Y$. Since $Y$ is compact, there exists a finite subcover $C_{y_1}, \ldots, C_{y_n}$.
>
> Let $W = B_{y_1} \cap \cdots \cap B_{y_n}$. This is a finite intersection of open sets containing $x_0$, so $W$ is an open neighborhood of $x_0$.
>
> **Claim:** $W \times Y \subseteq N$.
>
> *Proof of claim:* Let $(x, y) \in W \times Y$. Since $\{C_{y_i}\}$ covers $Y$, we have $y \in C_{y_j}$ for some $j$. Since $x \in W \subseteq B_{y_j}$, we have $(x, y) \in B_{y_j} \times C_{y_j} \subseteq N$.

^pf-15-9

*Uses:* [[Topology §4 Product Topology#^def-4-1|Def. §4.1]]

![[m590-15-4.svg]]
*The tube lemma: each point of the slice $x_0\times Y$ (blue line) sits in a basis box $B_{y_i}\times C_{y_i}\subseteq N$ (dashed); finitely many $C_{y_i}$ cover $Y$ by compactness, and $W=\bigcap B_{y_i}$ is the narrowest of the box widths. A point of the tube $W\times Y$ (red) lies in whichever box has its height in $C_{y_j}$, hence in $N$ (blue region).*

> [!proof]+ Proof of Finite Product Theorem
> Suffices to prove for two spaces (then use induction). Let $X, Y$ be compact. Let $\mathcal{A}$ be an open covering of $X \times Y$. We show $\mathcal{A}$ has a finite subcover.
>
> **Step 1:** Fix $x \in X$. The slice $x \times Y$ is homeomorphic to $Y$, hence compact. Since $\mathcal{A}$ covers $x \times Y$, there exists a finite subcollection $A_1, \ldots, A_m \in \mathcal{A}$ covering $x \times Y$ ([[Topology §15 Compact Spaces#^lem-15-1|Lemma §15.1]]).
>
> Let $N_x = A_1 \cup \cdots \cup A_m$. Then $N_x$ is open and $x \times Y \subseteq N_x$.
>
> **Step 2:** By the [[Tube Lemma|Tube Lemma]], there exists an open neighborhood $W_x$ of $x$ such that $W_x \times Y \subseteq N_x$. Thus $W_x \times Y$ is covered by finitely many elements of $\mathcal{A}$.
>
> **Step 3:** The collection $\{W_x\}_{x \in X}$ is an open cover of $X$. Since $X$ is compact, there exists a finite subcover $W_{x_1}, \ldots, W_{x_k}$.
>
> Then $X \times Y = \bigcup_{i=1}^{k} (W_{x_i} \times Y)$, and each $W_{x_i} \times Y$ is covered by finitely many elements of $\mathcal{A}$. Hence $X \times Y$ is covered by finitely many elements of $\mathcal{A}$.

^pf-15-8

*Uses:* [[Topology §15 Compact Spaces#^lem-15-1|§15.1]], [[Tube Lemma|§15.9]]

## Compact Subspaces of $\mathbb{R}$

> [!theorem] Theorem §15.10: Closed Intervals are Compact
> $X$ = simply ordered set with [[Topology §14 Connected Subspaces of ℝ#^def-14-1|l.u.b. property]]. In [[Topology §3 Order Topology#^def-3-4|order topology]], each closed interval $[a, b]$ in $X$ is compact.

^thm-15-10

> [!proof]+ Proof
> Let $a < b$. Let $\mathcal{A}$ be a covering of $[a, b]$ by sets open in $[a, b]$.
>
> *Note:* Since $[a,b]$ is convex in $X$, the subspace topology equals the order topology on $[a,b]$.
>
> **Outline:**
> 1. If $x \in [a, b)$, show there exists $y > x$ such that $[x, y]$ is covered by $\leq 2$ sets in $\mathcal{A}$.
> 2. Let $C = \{y \in [a, b] \mid [a, y] \text{ has a finite subcover by } \mathcal{A}\}$. Show $C \neq \emptyset$.
> 3. Let $c = \sup C$. Show $c \in C$.
> 4. Show $c = b$.
>
> **Proof of (1):** Let $x \in [a, b)$.
>
> *Case 1:* If $x$ has an immediate successor $y \in X$ (i.e., $(x,y) = \emptyset$), then $[x, y] = \{x, y\}$, which is covered by at most 2 elements of $\mathcal{A}$.
>
> *Case 2:* If $x$ has no immediate successor, choose $U \in \mathcal{A}$ with $x \in U$. Since $U$ is open in $[a,b]$, it contains a basis element around $x$. Since $x < b$ and $x$ has no immediate successor, $U$ contains some interval $[x, e)$ for some $e \in (x, b]$. Choose any $y \in (x, e)$. Then $[x, y] \subseteq [x, e) \subseteq U$, so $[x,y]$ is covered by 1 element.
>
> *Remark:* In $\mathbb{R}$, only Case 2 occurs since no real number has an immediate successor.
>
> **Proof of (2):** $a \in C$ since $[a, a] = \{a\}$ is covered by any single element of $\mathcal{A}$ containing $a$. So $C \neq \emptyset$.
>
> **Proof of (3):** $C$ is bounded above by $b$, and $X$ has the l.u.b. property, so $c = \sup C$ exists with $a \leq c \leq b$.
>
> Choose $A_c \in \mathcal{A}$ containing $c$. Since $A_c$ is open in $[a,b]$:
> - If $c = a$: $A_c$ contains $[a, e)$ for some $e > a$.
> - If $a < c \leq b$: $A_c$ contains $(d, c]$ for some $d < c$ (or $(d, e)$ containing $c$ if $c < b$).
>
> In either case, there exists $d < c$ such that $(d, c] \subseteq A_c$ (taking $d = a$ if $c = a$).
>
> *Claim:* $c \in C$.
>
> Since $c = \sup C$ and $d < c$, there must exist some $z \in C$ with $z > d$. (Otherwise $d$ would be an upper bound for $C$ smaller than $c$, contradicting $c = \sup C$.)
>
> Since $z \in C$, the interval $[a, z]$ is covered by finitely many (say $n$) elements of $\mathcal{A}$.
>
> Now $[a, c] = [a, z] \cup [z, c]$, and $[z, c] \subseteq (d, c] \subseteq A_c$. So $[a, c]$ is covered by $n + 1$ elements of $\mathcal{A}$, hence $c \in C$.
>
> **Proof of (4):** Suppose $c < b$. Then $c \in [a, b)$, so by Step (1), there exists $y > c$ with $y \in [a, b]$ such that $[c, y]$ is covered by $\leq 2$ elements of $\mathcal{A}$.
>
> Since $c \in C$ (by Step 3), $[a, c]$ has a finite subcover. Then $[a, y] = [a, c] \cup [c, y]$ also has a finite subcover, so $y \in C$.
>
> But $y > c = \sup C$, contradiction. Therefore $c = b$.
>
> Since $c = b \in C$, the interval $[a, b]$ has a finite subcover.

^pf-15-10

*Uses:* [[Topology §14 Connected Subspaces of ℝ#^def-14-1|Def. §14.1]], [[Topology §3 Order Topology#^def-3-4|Def. §3.4]]

> [!theorem] Corollary §15.11
> $[a, b] \subseteq \mathbb{R}$ is compact. Also, $\prod_{i=1}^{n} [a_i, b_i] \subseteq \mathbb{R}^n$ is compact.

^cor-15-11

> [!theorem] Theorem §15.12: Heine-Borel Theorem for $\mathbb{R}^n$
> $A \subseteq \mathbb{R}^n$ is compact if and only if $A$ is closed and bounded (with respect to the Euclidean metric $d$ or the square metric $\rho$).

^thm-15-12

> [!remark] Remark: Why Heine-Borel is Fundamental
> Heine-Borel characterizes compactness in $\mathbb{R}^n$ using familiar concepts:
>
> **1. Both conditions are necessary:**
> - *Not closed $\Rightarrow$ not compact:* $(0,1)$ is bounded but not compact (sequence $1/n$ has no limit in $(0,1)$).
> - *Not bounded $\Rightarrow$ not compact:* $\mathbb{R}$ is closed but not compact (cover by $(n, n+2)$ has no finite subcover).
>
> **2. The magic of $\mathbb{R}^n$:** Heine-Borel fails in general metric spaces! Example: $\mathbb{Z}$ with [[Topology §11 Metric Topology#^ex-11-4|discrete metric]] is closed and bounded (diam $\leq 1$) but not compact.
>
> **3. What makes $\mathbb{R}^n$ special:** The [[Topology §14 Connected Subspaces of ℝ#^def-14-1|least upper bound property]] of $\mathbb{R}$ ensures [[Topology §15 Compact Spaces#^thm-15-10|closed intervals are compact]]. This propagates to boxes via [[Topology §15 Compact Spaces#^thm-15-8|finite products]], then to all closed bounded sets.

^rem-15-8

> [!remark] Remark: Metric Equivalence
> Recall: $d(x,y) = \sqrt{\sum (x_i - y_i)^2}$ and $\rho(x,y) = \max_i |x_i - y_i|$ ([[Topology §11 Metric Topology#^ex-11-1|Example §11.1]], [[Topology §11 Metric Topology#^ex-11-2|Example §11.2]]).
>
> These metrics satisfy $\rho(x,y) \leq d(x,y) \leq \sqrt{n} \cdot \rho(x,y)$.
>
> Thus “bounded w.r.t. $d$” $\Leftrightarrow$ “bounded w.r.t. $\rho$”.

^rem-15-9

> [!remark]- Connections
> - Same inequality, used there for topologies: [[Topology §11 Metric Topology#^thm-11-2|Euclidean and Square Metrics Induce Same Topology]].
> - MATH 451 version: [[Single Variable Analysis §13 Some Topological Concepts in Metric Spaces#^prop-13-1|Equivalence of the Two Distances]].

> [!proof]+ Proof
> $(\Rightarrow)$ Suppose $A$ is compact.
>
> *$A$ is closed:* $\mathbb{R}^n$ is Hausdorff ([[Topology §11 Metric Topology#^thm-11-4|it's a metric space]]), and compact $\subseteq$ Hausdorff $\Rightarrow$ closed ([[Compact Subspace of a Hausdorff Space is Closed|§15.4]]).
>
> *$A$ is bounded:* The collection $\{B_\rho(0, m) \mid m \in \mathbb{Z}_+\}$ is an open cover of $\mathbb{R}^n$, hence covers $A$. Since $A$ is compact, there exists a finite subcover $B_\rho(0, m_1), \ldots, B_\rho(0, m_k)$ ([[Topology §15 Compact Spaces#^lem-15-1|Lemma §15.1]]).
>
> Let $M = \max\{m_1, \ldots, m_k\}$. Then $A \subseteq B_\rho(0, M)$, so $\rho(x, 0) < M$ for all $x \in A$. Thus $A$ is bounded.
>
> $(\Leftarrow)$ Suppose $A$ is closed and bounded w.r.t. $\rho$.
>
> *Key step:* Since $A$ is bounded, there exists $N > 0$ such that $\rho(x, 0) \leq N$ for all $x \in A$. This means each coordinate $|x_i| \leq N$, so $A \subseteq [-N, N]^n$.
>
> Now $[-N, N]^n = \prod_{i=1}^{n} [-N, N]$ is compact ([[Topology §15 Compact Spaces#^cor-15-11|finite product of compact intervals]]).
>
> *Claim:* $A$ is closed in $[-N, N]^n$.
>
> *Proof:* $A$ is closed in $\mathbb{R}^n$, so $A = C \cap \mathbb{R}^n = C$ for some closed $C$ in $\mathbb{R}^n$ (namely $C = A$). Then $A \cap [-N,N]^n = A$ (since $A \subseteq [-N,N]^n$) is [[Topology §6 Closed Sets and Limit Points#^thm-6-2|closed in the subspace]] $[-N,N]^n$.
>
> Therefore $A$ is a [[Closed Subspace of a Compact Space is Compact|closed subset of a compact space, hence compact]].

^pf-15-12

*Uses:* [[Topology §11 Metric Topology#^thm-11-4|§11.4]], [[Compact Subspace of a Hausdorff Space is Closed|§15.4]], [[Topology §15 Compact Spaces#^lem-15-1|§15.1]], [[Topology §15 Compact Spaces#^cor-15-11|§15.11]], [[Topology §6 Closed Sets and Limit Points#^thm-6-2|§6.2]], [[Closed Subspace of a Compact Space is Compact|§15.2]]

> [!remark] Remark: Filling the Gap: Balls vs. Boxes
> **Q:** The ball $B_\rho(0, N)$ is not a closed interval. How do we use compactness of $[a,b]$?
>
> **A:** We don't need balls to be boxes! The key insight is:
> 1. Bounded $\Rightarrow$ contained in some closed box $[-N, N]^n$
> 2. Closed boxes are compact ([[Topology §15 Compact Spaces#^cor-15-11|product of compact intervals]])
> 3. [[Closed Subspace of a Compact Space is Compact|Closed subset of compact is compact]]
>
> The shape of $A$ doesn't matter—only that it fits inside a compact box.

^rem-15-10
