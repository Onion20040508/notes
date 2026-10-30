---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 9
section: 62
tags: [differentiable-manifolds, math591]
---
← [[§61 Lie Group Morphisms and Linear Groups]] · ↑ [[· 9 Sard's Theorem]] · [[§63 Sard's Theorem]] →

*Stage: analysis — Sets that are negligible, in Euclidean space and then on manifolds: “this is not really measure theory. It's just the notion of sets of measure zero.”*

> [!definition] Definition §62.1: Measure Zero in $\mathbb{R}^n$
> A set $S \subseteq \mathbb{R}^n$ has **measure zero** if for every $\varepsilon > 0$ there is a countable cover $\{C_a\}$ of $S$ such that each $C_a$ is an open **rectangle**, a product of open intervals $C_a = (\alpha_1, \beta_1) \times \cdots \times (\alpha_n, \beta_n)$, and
>
> $$
> \sum_a \operatorname{Vol}(C_a) < \varepsilon, \qquad \operatorname{Vol}(C_a) = \prod_{i=1}^n (\beta_i - \alpha_i) \ \ \text{(Euclidean volume)}.
> $$
>
> *Lee: Ch. 6, Sets of Measure Zero; Appendix C*

^def-62-1
> [!remark]- Connections
> - Lebesgue measure: $S$ has measure zero exactly when its outer measure is $0$, [[§10 Lebesgue Outer Measure#^def-10-4|551 Def. §10.4]] (covers by closed rectangles, [[§10 Lebesgue Outer Measure#^def-10-3|551 Def. §10.3]], [[§10 Lebesgue Outer Measure#^def-10-1|551 Def. §10.1]]); such sets are measurable, [[§11 Lebesgue Measurable Sets#^ex-11-1|551 Ex. §11.1]].

“They could be closed, but let's say open.” In three dimensions the rectangles are solid boxes. “You should think of them as being very small, very thin. And for example, they cannot contain an open set. But it's much more than that, actually.”

![[m591-58-1.svg]]

A curve $S$ in the plane, covered by rectangles. Refining the cover shrinks the total area: about $0.79$ with $8$ rectangles, about $0.34$ with $32$, and as small as desired with more — so $S$ has measure zero.

![[m591-58-a1.gif|400]]

*(Not from lecture; animation added, vault only.)* A curve (chosen for the picture) covered by $4, 8, \ldots, 256$ rectangles, each the bounding box of one piece. The total area falls from $0.22$ (8 rectangles) to $0.006$ (256): as small as we like, so the curve has measure zero.

> [!theorem] Lemma §62.1: Basic Properties of Measure Zero
> In $\mathbb{R}^n$:
>
> 1. a subset of a set of measure zero has measure zero;
> 2. a countable union of sets of measure zero has measure zero;
> 3. in Definition [[§62 Sets of Measure Zero#^def-62-1|§62.1]], the open rectangles may be replaced by closed rectangles, or by open or closed cubes;
> 4. a nonempty open set does not have measure zero (for $n \ge 1$).
>
> *Lee: Proposition C.18, Exercise 6.1, Corollary C.25*

^lem-62-1
> [!remark]- Connections
> - Items (1)–(2) are monotonicity and countable subadditivity of outer measure, [[§10 Lebesgue Outer Measure#^prop-10-1|551 §10.1]]; countable sets: [[§10 Lebesgue Outer Measure#^ex-10-2|551 Ex. §10.2]]; item (4): the outer measure of a closed rectangle is its volume, [[§10 Lebesgue Outer Measure#^prop-10-2|551 §10.2]].

> [!proof]+ Proof
> *(Not from lecture; filled in. Item (4) is Uribe's “they cannot contain an open set”.)*
>
> *(1)* A cover of the larger set covers the smaller one.
>
> *(2)* Let $S = \bigcup_{k \ge 1} S_k$ with each $S_k$ of measure zero, and $\varepsilon > 0$. Cover $S_k$ by countably many open rectangles of total volume $< \varepsilon/2^k$. All of these together, a countable family, cover $S$ with total volume $< \sum_k \varepsilon/2^k = \varepsilon$.
>
> *(3)* *Closed rectangles.* A closed rectangle $\prod[\alpha_i, \beta_i]$ lies in the open rectangle $\prod(\alpha_i - \eta, \beta_i + \eta)$, whose volume tends to $\prod(\beta_i - \alpha_i)$ as $\eta \to 0$; so given a cover by closed rectangles of total volume $< \varepsilon/2$, enlarging the $a$-th rectangle ($a = 1, 2, \ldots$) so that its volume grows by less than $\varepsilon/2^{a+1}$ gives an open cover of total volume $< \varepsilon$. Conversely an open rectangle lies in its closure, of the same volume.
> *Cubes.* Cubes are rectangles, so a cover by cubes is a cover by rectangles. Conversely, let $R = \prod(\alpha_i, \beta_i)$ with sides $\ell_i = \beta_i - \alpha_i > 0$, and $0 < \delta \le \min_i \ell_i$. The closed cubes of side $\delta$ with corners in $\prod_i (\alpha_i + \delta\mathbb{Z})$ that meet $\overline R$ cover $R$; in the $i$-th direction at most $\lfloor \ell_i / \delta \rfloor + 2 \le \ell_i/\delta + 2 \le 3\ell_i/\delta$ of the intervals $[\alpha_i + t\delta, \alpha_i + (t+1)\delta]$ meet $[\alpha_i, \beta_i]$, so there are at most $\prod_i 3\ell_i/\delta$ such cubes, of total volume at most $3^n \operatorname{Vol}(R)$. Doing this for each rectangle of a cover of total volume $< \varepsilon/3^n$ gives a countable cover by closed cubes of total volume $< \varepsilon$; enlarging them as before gives open cubes.
>
> *(4)* A nonempty open set contains a closed cube $Q$ of some side $s > 0$, so by (1) it suffices to show that $Q$ is not covered by open rectangles of total volume $< s^n = \operatorname{Vol}(Q)$. Suppose $Q \subseteq \bigcup_a C_a$. $Q$ is compact, so finitely many $C_1, \ldots, C_r$ cover it. Cut $\mathbb{R}^n$ by the hyperplanes $x^i =$ (an endpoint of a side of $Q$ or of some $C_b$): this divides $Q$ into finitely many closed grid cells $P$, and each $\overline{C_b} \cap Q$ into cells too, with $\operatorname{Vol}(Q) = \sum_{P \subseteq Q} \operatorname{Vol}(P)$ and $\operatorname{Vol}(C_b) \ge \sum_{P \subseteq \overline{C_b}} \operatorname{Vol}(P)$, since the volume of a rectangle is the sum of the volumes of the cells it is divided into (expand the product of the side lengths). An interior point of a cell $P \subseteq Q$ lies in some $C_b$; no cutting hyperplane passes through the interior of $P$, so $P$ lies on one side of each face of $C_b$, hence $P \subseteq \overline{C_b}$. So every cell of $Q$ is counted in some $\operatorname{Vol}(C_b)$, and $\operatorname{Vol}(Q) \le \sum_{b=1}^r \operatorname{Vol}(C_b) \le \sum_a \operatorname{Vol}(C_a)$.

^pf-62-1

> [!theorem] Lemma §62.2: Smooth Maps Preserve Measure Zero
> Let $U \subseteq \mathbb{R}^n$ be open, $F : U \to \mathbb{R}^n$ smooth, and $S \subseteq U$ a set of measure zero. Then $F(S)$ has measure zero.
>
> *Lee: Proposition 6.5*

^lem-62-2

> [!proof]+ Proof
> *(Lecture 19 gave the idea: “I'm not going to prove this, but I want to tell you the idea of the proof.” The details are filled in.)*
>
> *The idea.* “Differentiable maps, $C^\infty$ maps, are locally Lipschitz”: for every compact $K \subseteq U$ there is a constant $C$ with
>
> $$
> |F(x) - F(y)| \le C\, |x - y| \qquad \text{for all } x, y \in K,
> $$
>
> and “somehow $C$ has to do with — not quite, but it's essentially — the sup of the partial derivatives over $K$.” This “of course implies continuity, but it's a lot more strong”: “it's going to map cubes to cubes of comparable volume.”
>
> *Reduction to a closed cube.* $U$ is the union of the countably many closed cubes with rational corners and rational side lengths that lie in $U$ (each $x \in U$ has an open ball in $U$ about it, and a small rational cube containing $x$ inside that ball). So $F(S) = \bigcup_Q F(S \cap Q)$ over countably many closed cubes $Q \subseteq U$, and by Lemma [[§62 Sets of Measure Zero#^lem-62-1|§62.1]](2) it suffices to show that $F(S \cap Q)$ has measure zero.
>
> *The Lipschitz estimate on $Q$, in the sup norm $\|x\|_\infty = \max_i |x^i|$.* The partial derivatives $\partial F^i/\partial x^j$ are continuous on the compact set $Q$, so $M = \max_{i,j} \sup_Q |\partial F^i/\partial x^j|$ is finite. $Q$ is convex, so for $x, y \in Q$ the segment between them lies in $Q$, and the mean value theorem applied to $t \mapsto F^i(x + t(y - x))$ gives a point $\xi$ on the segment with
>
> $$
> |F^i(y) - F^i(x)| = \Big| \sum_j \frac{\partial F^i}{\partial x^j}(\xi)\, (y^j - x^j) \Big| \le n M\, \|y - x\|_\infty ,
> $$
>
> so $\|F(y) - F(x)\|_\infty \le C \|y - x\|_\infty$ with $C = nM + 1 > 0$.
>
> *Cubes go to cubes.* A cube of side $t$ is a sup-norm ball. Let $\varepsilon > 0$, and by Lemma [[§62 Sets of Measure Zero#^lem-62-1|§62.1]](3) cover $S \cap Q$ by countably many open cubes $Q_a$, of sides $t_a$, with $\sum_a t_a^n < \varepsilon$. For each $a$ with $Q_a \cap Q \ne \varnothing$ pick $c_a \in Q_a \cap Q$. For $x \in Q_a \cap Q$, $\|x - c_a\|_\infty < t_a$, so $\|F(x) - F(c_a)\|_\infty < C t_a$: $F(Q_a \cap Q)$ lies in the open cube of side $2Ct_a$ centred at $F(c_a)$. These cubes cover $F(S \cap Q)$, with total volume $\sum_a (2C t_a)^n < (2C)^n \varepsilon$, as small as desired.

^pf-62-2

*Uses:* [[§62 Sets of Measure Zero#^lem-62-1|§62.1]]

> [!remark] Remark: Continuity Is Not Enough
> “You have to be careful. Just for fun, this is not true”: $F(S)$ may not have measure zero if $F$ is only continuous — “Cantor's function. It's a standard counterexample.” *(Filled in.)* The Cantor function $c : [0,1] \to [0,1]$ is continuous, nondecreasing, and maps the Cantor set, which has measure zero, onto all of $[0,1]$, which does not (Lemma [[§62 Sets of Measure Zero#^lem-62-1|§62.1]](4)). The smoothness used above is exactly the Lipschitz estimate, which $c$ lacks. “As you can see, we're really talking about analysis here.”

^rem-62-1
> [!remark]- Connections
> - The Cantor set [[§14 The Vitali Set and the Cantor Set#^def-14-4|551 Def. §14.4]] ([[§14 The Vitali Set and the Cantor Set#^prop-14-7|551 §14.7]]: measure zero, uncountable) and the Cantor function [[§31 Absolute Continuity#^ex-31-1|551 Ex. §31.1]].

![[m591-58-2.svg]]

*(Not from lecture.)* The Cantor function $c$: constant on each removed middle third, it climbs only on the Cantor set. So $c$ maps a set of measure zero (orange; shown at the second stage of the construction) onto the whole interval $[0,1]$ (teal). Its slopes are unbounded near the Cantor set, which is the Lipschitz estimate of Lemma [[§62 Sets of Measure Zero#^lem-62-2|§62.2]] failing.

*“Because of this lemma, we can define sets of measure zero on a manifold.”*

> [!definition] Definition §62.2: Measure Zero in a Manifold
> Let $M$ be a smooth manifold of dimension $m$ and $S \subseteq M$ any subset (“I'm not assuming it's a submanifold. It's just a set”). $S$ has **measure zero** if $S$ can be covered by coordinate charts $\{(U_\alpha, \varphi_\alpha)\}$, $S \subseteq \bigcup_\alpha U_\alpha$, such that for every $\alpha$ the set $\varphi_\alpha(S \cap U_\alpha) \subseteq \mathbb{R}^m$ has measure zero (Definition [[§62 Sets of Measure Zero#^def-62-1|§62.1]]).
>
> *Lee: Ch. 6, Sets of Measure Zero; Lemma 6.6*

^def-62-2

A student asked whether any number of charts is allowed. “Yeah, but you can always do with a countable [number], because of second countability” — the next lemma.

> [!theorem] Lemma §62.3: Countable Subcovers
> Let $X$ be a second-countable space (Definition [[§1 Point-Set Topology Review#^def-1-6|§1.6]]), $A \subseteq X$, and $\{U_\alpha\}$ a family of open sets covering $A$. Then countably many of the $U_\alpha$ cover $A$.
>
> *Lee: Proposition A.16*

^lem-62-3

> [!proof]+ Proof
> *(Filled in.)* Let $\mathcal{B}$ be a countable basis. For each $B \in \mathcal{B}$ that is contained in some $U_\alpha$, choose one such $U_{\alpha(B)}$; there are countably many choices. If $x \in A$, then $x \in U_\alpha$ for some $\alpha$, and since $\mathcal{B}$ is a basis there is $B \in \mathcal{B}$ with $x \in B \subseteq U_\alpha$; so $B$ was given a set $U_{\alpha(B)} \supseteq B \ni x$. So the chosen sets cover $A$.

^pf-62-3

> [!theorem] Proposition §62.4: Measure Zero Is Seen in Every Chart
> If $S \subseteq M$ has measure zero, then $\varphi(S \cap U)$ has measure zero in $\mathbb{R}^m$ for *every* chart $(U, \varphi)$ of $M$. Consequently subsets and countable unions of sets of measure zero in $M$ have measure zero in $M$.
>
> *Lee: Lemma 6.6, Exercise 6.7*

^prop-62-4

> [!proof]+ Proof
> *(Stated in Lecture 19 as an observation, “by the lemma”; filled in.)* Let $\{(U_\alpha, \varphi_\alpha)\}$ be as in Definition [[§62 Sets of Measure Zero#^def-62-2|§62.2]], and $(U, \varphi)$ any chart. By Lemma [[§62 Sets of Measure Zero#^lem-62-3|§62.3]] (manifolds are second countable), countably many $U_\alpha$ cover $S \cap U$, and
>
> $$
> \varphi(S \cap U \cap U_\alpha) = \big(\varphi \circ \varphi_\alpha^{-1}\big)\big(\varphi_\alpha(S \cap U \cap U_\alpha)\big),
> $$
>
> where the transition map $\varphi \circ \varphi_\alpha^{-1} : \varphi_\alpha(U \cap U_\alpha) \to \varphi(U \cap U_\alpha)$ is a smooth map between open subsets of $\mathbb{R}^m$ (Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]), and $\varphi_\alpha(S \cap U \cap U_\alpha) \subseteq \varphi_\alpha(S \cap U_\alpha)$ has measure zero (Lemma [[§62 Sets of Measure Zero#^lem-62-1|§62.1]](1)). By Lemma [[§62 Sets of Measure Zero#^lem-62-2|§62.2]], each $\varphi(S \cap U \cap U_\alpha)$ has measure zero, and $\varphi(S \cap U)$ is their countable union (Lemma [[§62 Sets of Measure Zero#^lem-62-1|§62.1]](2)).
>
> For the consequences: if $T \subseteq S$, the charts covering $S$ cover $T$, and $\varphi_\alpha(T \cap U_\alpha) \subseteq \varphi_\alpha(S \cap U_\alpha)$. If $S = \bigcup_k S_k$ with each $S_k$ of measure zero, cover $S$ by all charts of $M$: for each chart, $\varphi(S \cap U) = \bigcup_k \varphi(S_k \cap U)$ is a countable union of sets of measure zero, by the first part.

^pf-62-4

*Uses:* [[§62 Sets of Measure Zero#^def-62-2|Def. §62.2]], [[§62 Sets of Measure Zero#^lem-62-3|§62.3]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§62 Sets of Measure Zero#^lem-62-1|§62.1]], [[§62 Sets of Measure Zero#^lem-62-2|§62.2]]

![[m591-58-3.svg]]

The same piece of $S$ seen in two charts. The transition map carries one picture to the other, and it is smooth, so by Lemma [[§62 Sets of Measure Zero#^lem-62-2|§62.2]] measure zero in one picture means measure zero in the other.

> [!theorem] Lemma §62.5: A Fubini Lemma for Compact Sets
> Let $n \ge 2$ and $A \subseteq \mathbb{R}^n = \mathbb{R} \times \mathbb{R}^{n-1}$ compact, such that for every $c \in \mathbb{R}$ the slice $A_c = \{ x \in \mathbb{R}^{n-1} : (c, x) \in A \}$ has measure zero in $\mathbb{R}^{n-1}$. Then $A$ has measure zero in $\mathbb{R}^n$.
>
> *Lee: Lemma 6.2*

^lem-62-5
> [!remark]- Connections
> - Measure theory's version: the cross-section theorem [[§25 Invariance Properties and Fubini's Theorem#^thm-25-4|551 §25.4]] (from Tonelli) gives $m(A)=\int m(A_c)\,dc$ for measurable $A$; Fubini [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 §25.6]].

> [!proof]+ Proof
> *(Not from lecture; filled in, as a tool for Sard's theorem.)* Choose $a < b$ with $A \subseteq [a, b] \times \mathbb{R}^{n-1}$, and let $\delta > 0$.
>
> *Each slice, thickened.* Fix $c \in [a, b]$. $A_c$ is compact (its image $\{c\} \times A_c = A \cap (\{c\} \times \mathbb{R}^{n-1})$ is compact) and has measure zero, so it is covered by countably many open rectangles of total volume $< \delta$, hence by finitely many of them; let $U_c \subseteq \mathbb{R}^{n-1}$ be their union. There is an open interval $J_c \ni c$, which we may take inside $(a - 1, b + 1)$, with $A \cap (J_c \times \mathbb{R}^{n-1}) \subseteq J_c \times U_c$. Otherwise there are points $(c_k, x_k) \in A$ with $c_k \to c$ and $x_k \notin U_c$; by compactness a subsequence converges to some $(c, x) \in A$, with $x \notin U_c$ because the complement of $U_c$ is closed; but $x \in A_c \subseteq U_c$.
>
> *Finitely many strips.* The $J_c$ cover $[a, b]$; take a finite subcover, and from it a minimal one, $J_1, \ldots, J_r$ (for $c_1, \ldots, c_r$). No point lies in three of them: if $x$ lay in three, the one with the smallest left endpoint and the one with the largest right endpoint would both contain $x$, so their union, an interval, would contain the third, contradicting minimality. So $\sum_k \operatorname{length}(J_k) \le 2\,\operatorname{length}\big(\bigcup_k J_k\big) \le 2(b - a + 2)$.
>
> *The cover.* $A \subseteq \bigcup_k J_k \times U_{c_k}$, and $J_k \times U_{c_k}$ is a union of finitely many open rectangles, (interval) $\times$ (rectangle of $U_{c_k}$), of total volume $< \operatorname{length}(J_k)\,\delta$. In total, finitely many open rectangles of total volume $< 2(b - a + 2)\,\delta$, which is as small as desired.

^pf-62-5

![[m591-58-4.svg]]

*(Not from lecture.)* The proof of Lemma [[§62 Sets of Measure Zero#^lem-62-5|§62.5]] for a compact $A$ in the plane ($n = 2$). The slice of $A$ at $c$ (teal) has measure zero, so it is covered by finitely many small intervals, $U_c$. By compactness the same intervals still cover the slices at all $c'$ near $c$, in an interval $J_c$, so $A \cap (J_c \times \mathbb{R})$ lies in the thin boxes $J_c \times U_c$ (orange). Finitely many $J_c$ cover the first coordinate's range, overlapping at most twice, and the total area is at most $2 \times$ (length) $\times$ (the slices' cover size).

> [!remark] Remark: Measure Zero and Lebesgue Measure
> *(Not from lecture.)* Uribe: “this is not really measure theory. It's just the notion of sets of measure zero.” For readers who know Lebesgue measure the dictionary is short.
>
> 1. $S \subseteq \mathbb{R}^n$ has measure zero in the sense of Definition [[§62 Sets of Measure Zero#^def-62-1|§62.1]] exactly when its Lebesgue outer measure is $m^{\ast}(S) = 0$ (outer measure is defined with countable covers by rectangles, open or closed, as in Lemma [[§62 Sets of Measure Zero#^lem-62-1|§62.1]](3)); such sets are Lebesgue measurable.
> 2. Lemma [[§62 Sets of Measure Zero#^lem-62-1|§62.1]](1)–(2) are monotonicity and countable subadditivity of $m^{\ast}$; item (4) is $m^{\ast}(\text{closed rectangle}) =$ its volume.
> 3. Lemma [[§62 Sets of Measure Zero#^lem-62-5|§62.5]] is the cross-section theorem (a consequence of Tonelli's theorem) for a compact, hence measurable, set: $m(A) = \int_{\mathbb{R}} m(A_c)\, dc = 0$. The proof above avoids measurability and integration and uses only compactness.

^rem-62-2
