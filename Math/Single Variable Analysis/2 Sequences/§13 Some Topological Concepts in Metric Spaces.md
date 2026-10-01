---
subject: "[[Single Variable Analysis]]"
section: 13
chapter: 2
tags: [real-analysis, math451]
---
← [[§12 Lim Sup and Lim Inf Continued (Skipped)]] · ↑ [[· 2 Sequences]] · [[§14 Series]] →

## Metric Spaces

When we defined convergence of sequences of real numbers, the crucial thing was the absolute value $|s_n - s|$: it measures *how close* $s_n$ is to $s$. As noted in §3, the absolute value gives a distance $d(a,b) = |a - b|$, whose triangle property $d(a,b) \leq d(a,c) + d(c,b)$ reflects the [[Triangle inequality|triangle inequality]] $|a+b| \leq |a| + |b|$. So the crucial structure is the notion of *distance*. Abstracting it gives the notion of a metric space.

> [!definition] Definition §13.1: Metric Space
> A **metric space** is a set $X$ with a function $d: X \times X \to \mathbb{R}$ satisfying three conditions:
>
> 1. for any $x, y \in X$: $d(x,y) \geq 0$, with equality $d(x,y) = 0$ if and only if $x = y$;
>
> 2. $d(x,y) = d(y,x)$;
>
> 3. for any three points $x, y, z \in X$:    $d(x,y) \leq d(x,z) + d(z,y)$.
>
> The function $d$ is called the **distance function**, or the **metric**.

^def-13-1

> [!remark] Remark: Reading the axioms
> (1) is the *separation of points*: two different points must have positive distance. (2) is the *symmetry* of distance — equal in both directions; this may fail in real life (airfares!) and there are meaningful non-symmetric “distances” in mathematics too. (3) is the famous *triangle inequality* — often the condition that is not easy to verify.

^rem-13-1

> [!remark]- Connections
> - In 590 a metric generates a topology: [[§11 Metric Topology#^def-11-1|590 Def. §11.1]] and [[§11 Metric Topology#^def-11-3|590 Def. §11.3]].

> [!example] Example §13.1: The real line
> $X = \mathbb{R}$ with $d(a,b) = |a - b|$: all three conditions were verified in §3.

^ex-13-1

> [!example] Example §13.2: The complex plane
> $X = \mathbb{C}$. We need a notion of absolute value: for $z = x + iy$ with $x, y \in \mathbb{R}$, the *complex conjugate* is $\overline{z} = x - iy$, and the **absolute value** (modulus) is
>
> $$
> |z| = \sqrt{z \overline{z}} = \sqrt{x^2 + y^2}.
> $$
>
> Define $d(z_1, z_2) = |z_1 - z_2|$. Conditions (1), (2) are easy. Condition (3) amounts to $|z_1 + z_2| \leq |z_1| + |z_2|$ — not as easy.

^ex-13-2

> [!remark] Remark: Proof of the complex triangle inequality
> Note $\operatorname{Re} w \leq |w|$ for any $w \in \mathbb{C}$, and $|z \overline{w}| = |z||w|$ (from $|zw|^2 = zw \cdot \overline{zw} = |z|^2 |w|^2$). Then
>
> $$
> |z_1 + z_2|^2 = (z_1 + z_2)\overline{(z_1 + z_2)} = |z_1|^2 + 2 \operatorname{Re}(z_1 \overline{z_2}) + |z_2|^2
> \leq |z_1|^2 + 2 |z_1| |z_2| + |z_2|^2 = (|z_1| + |z_2|)^2,
> $$
>
> and take square roots.

^rem-13-2

> [!example] Example §13.3: Euclidean space
> $X = \mathbb{R}^n$, $n \geq 1$. For $x = (x_1, \ldots, x_n)$ and $y = (y_1, \ldots, y_n)$, define the **Euclidean distance**
>
> $$
> d(x,y) = \sqrt{(x_1 - y_1)^2 + \cdots + (x_n - y_n)^2}.
> $$
>
> Again (1), (2) are easy and (3) is not (its proof goes through the Cauchy–Schwarz inequality; we defer it). When we identify $\mathbb{C} = \mathbb{R}^2$, this agrees with the distance on $\mathbb{C}$ above.

^ex-13-3

> [!example] Example §13.4: The max distance
> Can we define a *different* distance on $\mathbb{R}^n$? Yes:
>
> $$
> d_\infty(x,y) = \max\{|x_1 - y_1|, \ldots, |x_n - y_n|\}.
> $$
>
> Here condition (3) *is* easy to check — it reduces to $\mathbb{R}$ coordinate-wise: for each $i$,
>
> $$
> |x_i - y_i| \leq |x_i - z_i| + |z_i - y_i| \leq d_\infty(x,z) + d_\infty(z,y),
> $$
>
> and taking the maximum over $i$ on the left gives the triangle inequality for $d_\infty$.
>
> ![[m451-13-1.svg]]
> *The unit ball $\{ d(x, 0) \leq 1 \}$ in $\mathbb{R}^2$ for the three metrics: the taxicab diamond ($d_1$) inside the Euclidean disc ($d_2$) inside the max-distance square ($d_\infty$), which in turn sits inside the Euclidean disc of radius $\sqrt2$ (dashed). This nesting is Proposition 13.1 for $n = 2$, $d_\infty \leq d \leq \sqrt2\, d_\infty$: each ball contains a scaled copy of the others, so all three metrics define the same convergent sequences.*

^ex-13-4

> [!remark] Remark: Taxicabs in New York
> The lecture attached the name “New York taxicab distance” here, with the picture: in the Euclidean distance, the shortest path between two points is the straight segment — but a taxicab in Manhattan can only move along a grid. Strictly speaking, the metric matching that picture is the *sum* distance $d_1(x,y) = |x_1 - y_1| + \cdots + |x_n - y_n|$ (total grid driving), which is the one usually called the taxicab metric; the $d_\infty$ defined above is usually called the max (or Chebyshev) distance. Both are legitimate metrics on $\mathbb{R}^n$, both with coordinate-wise-easy triangle inequalities, and everything said below about $d_\infty$ holds for $d_1$ as well.

^rem-13-3

## Convergence and Completeness in Metric Spaces

Once we have a metric space $(X, d)$, we can define convergence of sequences of points of $X$ — the definitions are word-for-word those for $\mathbb{R}$, with $d$ in place of the absolute value.

> [!definition] Definition §13.2: Convergence and Cauchy in a Metric Space
> Let $(s_n)$ be a sequence in a metric space $(X,d)$. We say $s_n \to s$ if for every $\varepsilon > 0$ there exists $N$ such that $d(s_n, s) < \varepsilon$ for all $n \geq N$. The sequence is **Cauchy** if for every $\varepsilon > 0$ there exists $N$ such that $d(s_n, s_m) < \varepsilon$ for all $m, n \geq N$.

^def-13-2

> [!remark] Remark: Positivity and uniqueness of limits
> The requirement $d(x,y) > 0$ for $x \neq y$ is used exactly to prove the *uniqueness of limits*, by the same contradiction proof as in §7 (with $\varepsilon < \tfrac12 d(s,t)$). This is a good place to see what that condition is for; in general topology, the corresponding property of a space is called the *Hausdorff property*.

^rem-13-4

> [!remark]- Connections
> - Same definition in ℝⁿ with the Euclidean norm: [[§1 Sequences and Limits in ℝⁿ#^def-1-1|452 Def. §1.1]].
> - Convergence in any topological space, with neighborhoods in place of ε-balls: [[§7 Interior and Closure#^def-7-4|590 Def. §7.4]].

> [!theorem] Proposition §13.1: Equivalence of the Two Distances
> On $\mathbb{R}^n$,
>
> $$
> d_\infty(x,y) \leq d(x,y) \leq \sqrt{n}\, d_\infty(x,y).
> $$
>
> Consequently, $d$ and $d_\infty$ define the same class of convergent sequences (with the same limits) and the same class of Cauchy sequences.

^prop-13-1

> [!proof]+ Proof
> For the first inequality: the largest $|x_i - y_i|$ satisfies $|x_i - y_i|^2 \leq \sum_j (x_j - y_j)^2$, so $d_\infty \leq d$. For the second: each of the $n$ summands is $\leq d_\infty(x,y)^2$, so $d(x,y)^2 \leq n\, d_\infty(x,y)^2$. Now check by the $(\varepsilon, N)$ definitions: if $d(s_n, s) \to 0$ then $d_\infty(s_n, s) \leq d(s_n,s) \to 0$; conversely if $d_\infty(s_n,s) \to 0$ then $d(s_n,s) \leq \sqrt{n}\, d_\infty(s_n,s) \to 0$ — given $\varepsilon$, apply the $d_\infty$-definition with tolerance $\varepsilon/\sqrt{n}$. The same comparison works for the Cauchy condition.

^pf-13-1

> [!remark]- Connections
> - In 452 the same inequality makes balls and square neighborhoods interchangeable: [[§2 Open and Closed Sets#^def-2-2|452 Def. §2.2]].
> - In 590 the same comparison shows that the Euclidean and square metrics give the same topology: [[§11 Metric Topology#^thm-11-2|590 Thm. §11.2]].

> [!definition] Definition §13.3: Complete Metric Space
> A metric space $(X,d)$ is called **complete** if every Cauchy sequence in $X$ is convergent (to a point of $X$).

^def-13-3

> [!example] Example §13.5: Completeness of the real line
> $(\mathbb{R}, |\cdot|)$ is a complete metric space — this is exactly what we proved in §10 (Cauchy $\Rightarrow$ convergent), and it is equivalent to the [[Completeness Axiom|completeness axiom]] of $\mathbb{R}$.

^ex-13-5

> [!theorem] Theorem §13.2: Completeness of Euclidean Space
> $(\mathbb{R}^n, d)$ is a complete metric space (equivalently, $(\mathbb{R}^n, d_\infty)$ is).

^thm-13-2

> [!proof]+ Proof
> We reduce to $(\mathbb{R}, |\cdot|)$. The key point: a sequence $s_k = (x_{1,k}, \ldots, x_{n,k}) \in \mathbb{R}^n$ converges if and only if every *coordinate sequence* $(x_{i,k})_{k}$ ($i = 1, \ldots, n$) converges in $\mathbb{R}$; and similarly for Cauchy. Both follow from
>
> $$
> |x_{i,k} - x_{i,m}| \leq d_\infty(s_k, s_m) \leq \max_i |x_{i,k} - x_{i,m}|
> $$
>
> (the right-hand inequality being an equality by definition).
>
> So let $(s_k)$ be Cauchy in $\mathbb{R}^n$. Then each coordinate sequence $(x_{i,k})_k$ is Cauchy in $\mathbb{R}$ (left inequality, with $d_\infty \leq d$), hence converges, say $x_{i,k} \to x_i$, by the completeness of $\mathbb{R}$. Assemble $s = (x_1, \ldots, x_n)$. Then
>
> $$
> d(s_k, s) \leq \sqrt{n}\, d_\infty(s_k, s) = \sqrt{n} \max_i |x_{i,k} - x_i| \longrightarrow 0,
> $$
>
> since each of the finitely many coordinates tends to $0$. Hence $s_k \to s$.

^pf-13-2

> [!definition] Definition §13.4: Bounded Sequence in a Metric Space
> A sequence $(s_n)$ in $(X,d)$ is **bounded** if there exist a number $M > 0$ and a point $x_0 \in X$ such that $d(s_n, x_0) \leq M$ for all $n \geq 1$ — a direct generalization of bounded sequences of real numbers.

^def-13-4

> [!theorem] Theorem §13.3: Bolzano–Weierstrass in $\mathbb{R}^n$
> Every bounded sequence in $\mathbb{R}^n$ has a convergent subsequence.

^thm-13-3

> [!proof]+ Proof
> The proof is similar — reduce to $\mathbb{R}$ coordinate by coordinate. If $(s_k)$ is bounded in $\mathbb{R}^n$, each coordinate sequence is bounded in $\mathbb{R}$. By [[Bolzano–Weierstrass Theorem|Bolzano–Weierstrass]] in $\mathbb{R}$, extract a subsequence along which the first coordinates converge; from *that* subsequence, extract a further subsequence along which the second coordinates converge (the first still converge, being a subsequence of a convergent sequence); continue through all $n$ coordinates. After $n$ extractions, all coordinates converge along the final subsequence, which therefore converges in $\mathbb{R}^n$ by the coordinate-wise criterion. So many things in calculus generalize to this topological setting.

^pf-13-3

> [!remark]- Connections
> - Topological counterparts: closed bounded subsets of ℝⁿ are compact, [[§15 Compact Spaces#^thm-15-12|590 Thm. §15.12]] (Heine–Borel), and compact equals sequentially compact for metric spaces, [[§16 Limit Point Compactness#^thm-16-2|590 Thm. §16.2]].

## Open and Closed Sets

Now we can introduce the most important topological notions.

> [!definition] Definition §13.5: Open and Closed Subsets
> Let $(X,d)$ be a metric space. A subset $U \subseteq X$ is called **open** if for every point $x \in U$, there exists a ball of some radius $\varepsilon > 0$ centered at $x$,
>
> $$
> B_d(x, \varepsilon) = \{ y \in X \mid d(y,x) < \varepsilon \},
> $$
>
> that is contained in $U$. A subset $C \subseteq X$ is called **closed** if the complement $X \setminus C$ is open.

^def-13-5

The name “open” comes from open intervals in $\mathbb{R}$. These notions are the most important ones in topology: a *topological space* can be described as a space together with its collection of open subsets — equivalently, of closed subsets, since each collection determines the other by complementation.

> [!remark]- Connections
> - In ℝⁿ, 452 defines open sets by interior points and closed sets as those containing all their boundary points: [[§2 Open and Closed Sets#^def-2-4|452 Def. §2.4]].
> - 590 takes open sets as the primitive notion, [[§1 Topological Spaces#^def-1-1|590 Def. §1.1]]; the open sets defined here form the metric topology, [[§11 Metric Topology#^def-11-3|590 Def. §11.3]].

> [!example] Example §13.6: Open intervals are open
> Every open interval $(a,b) \subseteq \mathbb{R}$ is an open subset. For any $x \in (a,b)$: $x > a$ and $x < b$, so $x - a > 0$ and $b - x > 0$. Take $\varepsilon < \min\{x - a,\, b - x\}$; then $B(x,\varepsilon) = (x - \varepsilon, x + \varepsilon) \subseteq (a,b)$.
>
> We *cannot* do the same with the closed interval $[a,b]$ — the argument fails at the endpoints: every ball around $a$ contains points $< a$, outside $[a,b]$. So closed intervals are not open subsets. (They are closed: the complement $(-\infty, a) \cup (b, +\infty)$ is open by the argument above.)

^ex-13-6

![[m451-13-2.svg]]
*Top: around any $x \in (a,b)$ a ball $B(x,\varepsilon)$ (red) fits inside once $\varepsilon < \min\{x-a,\, b-x\}$ — the endpoints are missing (hollow), so there is always room. Bottom: $[a,b]$ contains its endpoint $a$, and every ball around $a$ pokes out to the left, so $[a,b]$ is not open.*

> [!theorem] Proposition §13.4: Unions of Open Sets
> Any union of open subsets is open. Dually (by complementation), any intersection of closed subsets is closed.

^prop-13-4

> [!proof]+ Proof
> If $x$ belongs to the union, it belongs to one of the open sets $U$, and the ball $B(x,\varepsilon) \subseteq U$ is contained in the union. The dual statement follows by De Morgan's laws.

^pf-13-4

So, e.g., $(0,1) \cup (2,4)$ is open.

> [!remark] Remark: Structure of open and closed subsets of the line
> **Fact:** every open subset of $\mathbb{R}$ is a union of open intervals — possibly infinitely many, but always *countably* many (one can take them disjoint). So open subsets of $\mathbb{R}$ have a simple description. Closed sets, by contrast, can be very complicated. Two illustrations:
>
> - Given any sequence $(s_n)$ in $\mathbb{R}$, its set $S$ of subsequence limits is a closed set (as promised in §11).
>
> - **The Cantor set.** Start with $[0,1]$; remove the open middle third $(\tfrac13, \tfrac23)$, leaving the two closed intervals $[0,\tfrac13]$ and $[\tfrac23, 1]$; do the same to each of them, and continue by induction. What is left in the limit — the intersection of all the stages — is a closed subset of $[0,1]$ (an intersection of closed sets), very complicated but useful. It is *not* a union of closed intervals: in fact it contains no interval at all.

^rem-13-5

![[m451-13-3.svg]]
*The first stages of the Cantor set: each stage removes the open middle third of every remaining interval, so stage $k$ consists of $2^k$ closed intervals of length $3^{-k}$. The Cantor set is what survives all stages.*

> [!remark]- Connections
> - In 590 this property becomes an axiom of a topology, [[§1 Topological Spaces#^def-1-1|590 Def. §1.1]], and its closed-set dual is [[§6 Closed Sets and Limit Points#^thm-6-1|590 Thm. §6.1]].
> - Both facts are proved in 551: open subsets of ℝ as countable disjoint unions of open intervals in [[§7 Structure of Open Sets#^prop-7-1|551 Prop. §7.1]], and the Cantor set (closed, uncountable, null, with no interior) in [[§11 Borel Sets and Measure Spaces#^def-11-13|551 Def. §11.13]] and [[§11 Borel Sets and Measure Spaces#^prop-11-21|551 Prop. §11.21]].

> [!theorem] Proposition §13.5: Sequential Characterization of Closedness
> $C \subseteq X$ is closed if and only if for every convergent sequence $s_n \to s$ in $X$ with all $s_n \in C$, the limit $s$ lies in $C$ too. So a closed set *contains all limits of sequences of its points* — that is why it is called closed.

^prop-13-5

> [!proof]+ Proof
> ($\Rightarrow$) Let $C$ be closed, $s_n \in C$, $s_n \to s$; suppose $s \notin C$. Then $s \in X \setminus C$, which is open, so some ball $B(s, \varepsilon) \subseteq X \setminus C$. But $d(s_n, s) < \varepsilon$ for large $n$, so $s_n \in B(s,\varepsilon) \subseteq X \setminus C$ — contradicting $s_n \in C$. Hence $s \in C$.
>
> ($\Leftarrow$) Suppose $C$ is not closed, i.e. $X \setminus C$ is not open: there is a point $x \in X \setminus C$ such that no ball around $x$ is contained in $X \setminus C$. In particular, for each $n$ the ball $B(x, \tfrac1n)$ meets $C$: choose $s_n \in C \cap B(x, \tfrac1n)$. Then $d(s_n, x) < \tfrac1n \to 0$, so $s_n \to x$, with all $s_n \in C$ but $x \notin C$ — the sequential condition fails. Contrapositively, the sequential condition implies closedness.

^pf-13-5

![[m451-13-4.svg]]
*The ($\Leftarrow$) direction: if $C$ is not closed, some $x \notin C$ (hollow red) has no ball inside the complement, so every ball $B(x, \tfrac1n)$ (dashed) meets $C$; choosing $s_n \in C \cap B(x, \tfrac1n)$ gives a sequence in $C$ converging to a point outside $C$.*

> [!remark]- Connections
> - Topological version, with limit points in place of sequences: [[§7 Interior and Closure#^cor-7-5|590 Cor. §7.5]]; sequences are enough in metrizable spaces by [[§11 Metric Topology#^lem-11-8|590 Lemma §11.8]].

## Closure

One more important notion: how to produce closed sets from arbitrary sets.

> [!definition] Definition §13.6: Closure
> For any subset $Y$ of a metric space $(X,d)$, the **closure** of $Y$, denoted $\overline{Y}$, is the smallest closed subset containing $Y$.

^def-13-6

Why does such a smallest closed superset exist? Consider *all* closed subsets containing $Y$ (there is at least one, namely $X$), and take their intersection: it is closed (intersection of closed sets is closed — the dual of “union of open is open”), it contains $Y$, and it is contained in every closed superset of $Y$. So it is the smallest one.

> [!remark]- Connections
> - 452's version in ℝⁿ: the closure is the set together with its boundary points, [[§2 Open and Closed Sets#^def-2-5|452 Def. §2.5]].
> - Closure in any topological space: [[§7 Interior and Closure#^def-7-1|590 Def. §7.1]].

> [!example] Example §13.7: Closures on the line
> If $Y$ is already closed, $\overline{Y} = Y$. For $Y = (a,b) \subset \mathbb{R}$: $\overline{Y} = [a,b]$. For $Y = \mathbb{Q}$, $X = \mathbb{R}$: what is $\overline{\mathbb{Q}}$? Answer: $\overline{\mathbb{Q}} = \mathbb{R}$ — every real number is a limit of a sequence of rationals, by the density of $\mathbb{Q}$ in $\mathbb{R}$ (§4; choose $s_n \in \mathbb{Q} \cap (x - \tfrac1n, x + \tfrac1n)$).

^ex-13-7

> [!theorem] Proposition §13.6: Sequential Characterization of the Closure
> $$
> \overline{Y} = Y \cup \{ \lim s_n \mid (s_n) \text{ a convergent sequence with all } s_n \in Y \}.
> $$
>
> This makes it clear why $\overline{Y}$ is called the closure: it is $Y$ together with all the limits one can form from within $Y$.

^prop-13-6

> [!remark]- Connections
> - 590's Sequence Lemma, [[§11 Metric Topology#^lem-11-8|590 Lemma §11.8]], gives one inclusion in every space and equality in metrizable ones; the neighborhood form is [[§7 Interior and Closure#^thm-7-3|590 Thm. §7.3]].

> [!example] Example §13.8: Two closures computed (HW)
> **(1)** $S = \left\{ \tfrac1n \mid n \in \mathbb{N} \right\}$:    $\overline S = S \cup \{0\}$.
>
> The set $S \cup \{0\}$ is closed, since its complement
>
> $$
> (-\infty, 0) \ \cup\ \bigcup_{n=1}^{\infty} \left( \frac{1}{n+1},\ \frac1n \right) \ \cup\ (1, \infty)
> $$
>
> is a union of open intervals, hence open. And $0$ must belong to any closed set containing $S$, being the limit of the sequence $\tfrac1n \in S$ (sequential characterization). So $S \cup \{0\}$ is the smallest closed superset.
>
> **(2)** $C = \{ r \in \mathbb{Q} \mid r^2 < 2 \} = \mathbb{Q} \cap (-\sqrt2, \sqrt2)$:    $\overline C = [-\sqrt2, \sqrt2]$.
>
> ($\subseteq$) $[-\sqrt2, \sqrt2]$ is closed and contains $C$: any limit of a sequence in $C$ obeys the bounds $-\sqrt2 \leq \lim \leq \sqrt2$, since limits preserve weak inequalities (§9).
>
> ($\supseteq$) Let $x \in [-\sqrt2, \sqrt2]$. For each $n$, the set $\left(x - \tfrac1n,\ x + \tfrac1n\right) \cap (-\sqrt2, \sqrt2)$ is a nonempty open interval (nonempty even at the endpoints: for $x = \sqrt2$ it contains $(\sqrt2 - \tfrac1n, \sqrt2)$), so the density of $\mathbb{Q}$ (§4) provides $r_n \in \mathbb{Q}$ inside it. Then $r_n \in C$ and $|r_n - x| < \tfrac1n$, so $x = \lim r_n \in \overline C$. (One uniform choice of interval replaces a case analysis over interior points and the two endpoints.)
>
> This is the same set that exhibited the *incompleteness* of $\mathbb{Q}$ in §4: within $\mathbb{Q}$ it has no least upper bound. Taking the closure within $\mathbb{R}$ fills in exactly the two missing points $\pm\sqrt2$.

^ex-13-8
