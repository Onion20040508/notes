---
type: section
subject: "[[Logic and Proofs]]"
chapter: 2
section: "7a"
eccles: "Ch. 7"
aliases: ["Eccles 7 (cont.)"]
tags: [logic-and-proofs, mat250]
---
← [[§7 Quantifiers]] · ↑ [[· 2 Sets and Functions]] · [[§8 Functions]] →

*Eccles, Chapter 7 · MAT 250 HW3 (Exercises 7.2, 7.4, 7.5, 7.7) · MAT 200 HW1 (Problem 3) · MAT 200 Practice Midterm 1 (Problems 5–8, Example from L3) · MAT 200 supplement (Helfer).*

This section studies statements with several quantifiers, where the order of the quantifiers matters. Predicates in two variables define subsets of the Cartesian product, which gives a picture of each quantified statement.

## 7.6 Predicates Involving More Than One Free Variable

> [!remark] Remark: Statements With Two Quantifiers
> A predicate $P(a, b)$ with $a \in A$ and $b \in B$ gives the propositions
>
> $$
> \begin{aligned}
> &\text{(i) } \forall a \in A,\ \forall b \in B,\ P(a, b); && \text{(ii) } \exists a \in A,\ \exists b \in B,\ P(a, b); \\
> &\text{(iii) } \forall a \in A,\ \exists b \in B,\ P(a, b); && \text{(iv) } \exists b \in B,\ \forall a \in A,\ P(a, b); \\
> &\text{(v) } \forall b \in B,\ \exists a \in A,\ P(a, b); && \text{(vi) } \exists a \in A,\ \forall b \in B,\ P(a, b).
> \end{aligned}
> $$
>
> They are read from the left: in (iii), "$\exists b \in B,\ P(a, b)$" is a predicate in the single free variable $a$, and (iii) says it holds for every $a$. So in (iii) the $b$ may depend on $a$, while in (iv) one $b$ must work for every $a$. "$\forall a, b \in A$" abbreviates "$\forall a \in A,\ \forall b \in A$", and similarly for $\exists$. Examples already met: [[§3 Proofs#^prop-3-1|Proposition §3.1]] ($\forall a, b \in \R^+,\ a < b \Rightarrow a^2 < b^2$) and [[§4 Proof by Contradiction#^prop-4-1|Proposition §4.1]] (not $\exists m, n \in \Z,\ 14m + 20n = 101$).
>
> *Eccles: Section 7.6*

^rem-7a-1
> [!theorem] Theorem §7a.1: Interchanging Quantifiers
> Let $P(a, b)$ be a predicate with $a \in A$, $b \in B$.
> 1. $\forall a \in A,\ \forall b \in B,\ P(a, b) \iff \forall b \in B,\ \forall a \in A,\ P(a, b)$.
> 2. $\exists a \in A,\ \exists b \in B,\ P(a, b) \iff \exists b \in B,\ \exists a \in A,\ P(a, b)$.
> 3. $\exists a \in A,\ \forall b \in B,\ P(a, b) \implies \forall b \in B,\ \exists a \in A,\ P(a, b)$.
>
> The converse of 3 is false in general: quantifiers of different kinds may not be interchanged.
>
> *Source: MAT 200 lecture (syllabus week 2: "interchanging quantifiers"); MAT 200 Practice Midterm 1, Problem 6*

^thm-7a-1

> [!proof]+ Proof
> (1) Both sides say that $P(a, b)$ is true for every choice of $a \in A$ and $b \in B$.
>
> (2) Both sides say that $P(a, b)$ is true for at least one choice of $a \in A$ and $b \in B$.
>
> (3) Suppose $\exists a \in A,\ \forall b \in B,\ P(a, b)$, and let $a_0 \in A$ be such that $P(a_0, b)$ holds for all $b \in B$. Given any $b \in B$, the element $a = a_0$ satisfies $P(a, b)$. Hence $\forall b \in B,\ \exists a \in A,\ P(a, b)$.
>
> For the converse, take $A = B = \Z^+$ and $P(a, b)$: $b < a$. Then $\forall b\ \exists a,\ b < a$ is true ($a = b + 1$), but $\exists a\ \forall b,\ b < a$ is false (for each $a$, $b = a$ fails); this is [[§7a Several Quantifiers and the Cartesian Product#^ex-7a-1|Example §7a.1]] (a), (b).

^pf-7a-1

*Uses:* [[§7 Quantifiers#^def-7-1|Def. §7.1]], [[§7 Quantifiers#^def-7-2|Def. §7.2]], [[§7a Several Quantifiers and the Cartesian Product#^ex-7a-1|Ex. §7a.1]]

> [!remark]- Connections
> - The same quantifier move in analysis: continuity at every point ($\forall x\, \forall \varepsilon\, \exists \delta$) versus uniform continuity ($\forall \varepsilon\, \exists \delta\, \forall x$), [[§19 Uniform Continuity#^def-19-1|451 Def. §19.1]]; pointwise versus uniform convergence ($N$ depending on $x$ or not), [[§24 Uniform Convergence#^def-24-2|451 Def. §24.2]].

> [!example] Example §7a.1: The Order of Quantifiers
> Consider the predicate $m < n$ for $m, n \in \Z^+$.
>
> **(a)** $\forall m \in \Z^+,\ \exists n \in \Z^+,\ m < n$ is **true**: it says $\{m \in \Z^+ \mid \exists n \in \Z^+,\ m < n\} = \Z^+$. Given $m \in \Z^+$, put $n = m + 1$; then $n \in \Z^+$ and $m < n$.
>
> **(b)** $\exists n \in \Z^+,\ \forall m \in \Z^+,\ m < n$ is **false**: such an $n$ would exceed every positive integer, including itself. For each $n \in \Z^+$, put $m = n$; then $m \in \Z^+$ and $m \not< n$, a counterexample to $\forall m,\ m < n$.
>
> **(c)** $\forall n \in \Z^+,\ \exists m \in \Z^+,\ m < n$ is **false**: $\{n \in \Z^+ \mid \exists m \in \Z^+,\ m < n\} = \Z^+ - \{1\}$. A counterexample is $n = 1$, since $m \not< 1$ for all $m \in \Z^+$.
>
> **(d)** $\exists m \in \Z^+,\ \forall n \in \Z^+,\ m < n$ is **false**: for each $m \in \Z^+$, put $n = m$; then $m \not< n$.
>
> Compare (b) and (d). Both use the implication $m = n \Rightarrow m \not< n$, but in (b) we start from a general $n$ and *define* $m = n$, while in (d) we start from a general $m$ and define $n = m$: the variable bound by the inner $\forall$ is the one we get to choose.
>
> *Eccles: Examples 7.6.1–7.6.4*

^ex-7a-1

> [!example] Example §7a.2: Quantifiers and ≤ on the Positive Integers
> For $m, n \in \Z^+$:
>
> | statement | value | reason |
> |---|---|---|
> | (i) $\forall m, n \in \Z^+,\ m \le n$ | false | counterexample $m = 2$, $n = 1$ |
> | (ii) $\exists m, n \in \Z^+,\ m \le n$ | true | example $m = n = 1$ |
> | (iii) $\forall m \in \Z^+,\ \exists n \in \Z^+,\ m \le n$ | true | given $m$, take $n = m$ (or $m + 1$) |
> | (iv) $\exists m \in \Z^+,\ \forall n \in \Z^+,\ m \le n$ | true | $m = 1$: every positive integer is $\ge 1$ ([[§5 The Induction Principle#^ex-5-2\|Ex. §5.2]]) |
> | (v) $\forall n \in \Z^+,\ \exists m \in \Z^+,\ m \le n$ | true | given $n$, take $m = n$ (or $m = 1$) |
> | (vi) $\exists n \in \Z^+,\ \forall m \in \Z^+,\ m \le n$ | false | for each $n$, $m = n + 1$ gives $m \not\le n$ |
>
> In (vi) the useful denial $\forall n \in \Z^+,\ \exists m \in \Z^+,\ m > n$ is proved, as in (iii), by the choice $m = n + 1$. Note that (iv) is true and therefore so is (v), by [[§7a Several Quantifiers and the Cartesian Product#^thm-7a-1|§7a.1]](3) with the roles of the variables matched; but (iii) true does not force (vi).
>
> *Source: HW3*
> *Eccles: Exercise 7.2*

^ex-7a-2

> [!example] Example §7a.3: Quantifiers Over the Reals
> | statement | value | reason |
> |---|---|---|
> | (i) $\forall x \in \R,\ \exists y \in \R,\ x + y = 0$ | true | given $x$, take $y = -x$ |
> | (ii) $\exists y \in \R,\ \forall x \in \R,\ x + y = 0$ | false | for each $y$, $x = 1 - y$ gives $x + y = 1 \ne 0$ |
> | (iii) $\forall x \in \R,\ \exists y \in \R,\ xy = 0$ | true | take $y = 0$ |
> | (iv) $\exists y \in \R,\ \forall x \in \R,\ xy = 0$ | true | $y = 0$ works for every $x$ |
> | (v) $\forall x \in \R,\ \exists y \in \R,\ xy = 1$ | false | counterexample $x = 0$: $0 \cdot y = 0 \ne 1$ |
> | (vi) $\exists y \in \R,\ \forall x \in \R,\ xy = 1$ | false | for each $y$, $x = 0$ gives $xy = 0 \ne 1$ |
> | (vii) $\forall n \in \Z^+,\ (n \text{ even or } n \text{ odd})$ | true | "odd" means "not even" ([[§2 Implications#^def-2-8\|Def. §2.8]]), so this is $P \vee \neg P$ |
> | (viii) $(\forall n \in \Z^+,\ n \text{ even}) \text{ or } (\forall n \in \Z^+,\ n \text{ odd})$ | false | $1$ is not even and $2$ is not odd |
>
> In (iii)–(iv) one $y$ serves for all $x$; in (i)–(ii) the $y$ has to depend on $x$. Items (vii) and (viii) show that $\forall$ distributes over "or" in only one direction: (viii) $\Rightarrow$ (vii), but not conversely.
>
> *Source: HW3*
> *Eccles: Exercise 7.4*

^ex-7a-3

> [!example] Example §7a.4: Quantifiers Over Intervals
> Take $x \in [0, 2]$, $y \in [1, 3]$ and the predicate $y < x$.
>
> | statement | value | reason |
> |---|---|---|
> | (a) $\exists x \in [0,2],\ \exists y \in [1,3],\ y < x$ | true | $x = 2$, $y = 1$ |
> | (b) $\forall x \in [0,2],\ \forall y \in [1,3],\ y < x$ | false | denial $\exists x\, \exists y,\ y \ge x$: $x = 0$, $y = 2$ |
> | (c) $\exists x \in [0,2],\ \forall y \in [1,3],\ y < x$ | false | denial $\forall x\, \exists y,\ y \ge x$: take $y = 3 > 2 \ge x$ |
> | (d) $\forall y \in [1,3],\ \exists x \in [0,2],\ y < x$ | false | denial $\exists y\, \forall x,\ y \ge x$: $y = 3$ |
> | (e) $\exists y \in [1,3],\ \forall x \in [0,2],\ y < x$ | false | denial $\forall y\, \exists x,\ y \ge x$: take $x = 0$ |
> | (f) $\forall x \in [0,2],\ \exists y \in [1,3],\ y < x$ | false | denial $\exists x\, \forall y,\ y \ge x$: $x = 0$ |
>
> Geometrically, the truth set $\{(x, y) \in [0,2] \times [1,3] \mid y < x\}$ is the small triangle below the diagonal in the corner near $(2, 1)$. Statement (a) says it is non-empty, (b) that it is the whole rectangle, (c) that it contains a whole vertical segment $\{x\} \times [1, 3]$, (d) that every horizontal segment $[0,2] \times \{y\}$ meets it, (e) that it contains a whole horizontal segment, (f) that every vertical segment meets it. As [[§7a Several Quantifiers and the Cartesian Product#^thm-7a-1|§7a.1]](3) predicts, (c) $\Rightarrow$ (d) and (e) $\Rightarrow$ (f); here all four are false.
>
> *Source: MAT 200 Practice Midterm 1, Problem 6*

^ex-7a-4

> [!example] Example §7a.5: All Quantified Forms of One Predicate
> For real $x, y$ consider $x^2 + xy + 1 = 0$. Solving: for $x \ne 0$ it holds iff $y = -(1 + x^2)/x$; as a quadratic in $x$ it has a real solution iff the discriminant $y^2 - 4 \ge 0$, i.e. $|y| \ge 2$.
>
> | statement | value | reason |
> |---|---|---|
> | (1) $\exists x\, \exists y$ | true | $x = -1$, $y = 2$: $1 - 2 + 1 = 0$ |
> | (2) $\exists y\, \exists x$ | true | equivalent to (1) ([[§7a Several Quantifiers and the Cartesian Product#^thm-7a-1\|§7a.1]](2)) |
> | (3) $\forall x\, \forall y$ | false | $x = y = 0$ gives $1 \ne 0$ |
> | (4) $\forall y\, \forall x$ | false | equivalent to (3) |
> | (5) $\exists x\, \forall y$ | false | denial $\forall x\, \exists y,\ x^2 + xy + 1 \ne 0$: take $y = -x$, giving $1 \ne 0$ |
> | (6) $\forall x\, \exists y$ | false | counterexample $x = 0$: $0 + 0 + 1 \ne 0$ for every $y$ |
> | (7) $\exists y\, \forall x$ | false | denial $\forall y\, \exists x$: take $x = 0$ |
> | (8) $\forall y\, \exists x$ | false | counterexample $y = 0$: $x^2 + 1 \ne 0$ for every $x$ (any $|y| < 2$ works) |
>
> Since (8) is false, so is (5), by [[§7a Several Quantifiers and the Cartesian Product#^thm-7a-1|§7a.1]](3); likewise (6) false forces (7) false.
>
> *Source: MAT 200 Practice Midterm 1, Problem 7*

^ex-7a-5

> [!example] Example §7a.6: Quantifiers With a Parameter
> For real $a$ and $x$ let $p_a(x) = x^2 - 2ax + 4a + 5$. Completing the square,
>
> $$
> p_a(x) = (x - a)^2 + c_a, \qquad c_a = -a^2 + 4a + 5 = -(a - 5)(a + 1),
> $$
>
> so $p_a(x) \ge c_a$ for all $x$, with equality at $x = a$. The values of $a$ for which each statement holds:
>
> **(a)** $\exists x,\ p_a(x) = 0$ $\iff$ $c_a \le 0$ $\iff$ $a \le -1$ or $a \ge 5$. If $c_a \le 0$, then $x = a + \sqrt{-c_a}$ works; if $c_a > 0$ then $p_a(x) \ge c_a > 0$ for all $x$.
>
> **(b)** $\forall x,\ p_a(x) = 0$ holds for **no** $a$: $p_a(a) = c_a$ and $p_a(a + 1) = c_a + 1$ cannot both be $0$.
>
> **(c)** $\exists x,\ p_a(x) > 0$ holds for **all** $a$: take $x = a + |c_a| + 1$; then $(x - a)^2 \ge |c_a| + 1 > -c_a$, so $p_a(x) > 0$.
>
> **(d)** $\forall x,\ p_a(x) > 0$ $\iff$ $c_a > 0$ $\iff$ $-1 < a < 5$. If $c_a > 0$ then $p_a(x) \ge c_a > 0$; if $c_a \le 0$ then $x = a$ is a counterexample.
>
> Note (b) $\Rightarrow$ (a) and (d) $\Rightarrow$ (c), since a universal statement over a non-empty set implies the existential one; and (d) is the negation of (a), as [[§7 Quantifiers#^thm-7-2|Theorem §7.2]] predicts once one notes that $\exists x,\ p_a(x) \le 0$ is equivalent to $\exists x,\ p_a(x) = 0$ here.
>
> *Source: MAT 200 Practice Midterm 1, Problem 8*

^ex-7a-6

## 7.7 The Cartesian Product of Two Sets

> [!definition] Definition §7a.1: Cartesian Product
> Given sets $X$ and $Y$, the **Cartesian product** $X \times Y$ is the set of all **ordered pairs** $(x, y)$ with $x \in X$ and $y \in Y$:
>
> $$
> X \times Y = \{(x, y) \mid x \in X \text{ and } y \in Y\}.
> $$
>
> We write $X^2 = X \times X$. In pictures $X$ is drawn horizontally and $Y$ vertically.
>
> *Eccles: Definition 7.7.1*

^def-7a-1

> [!definition] Definition §7a.2: Ordered Pair
> "Ordered" means that $(x_1, y_1) = (x_2, y_2)$ if and only if $x_1 = x_2$ and $y_1 = y_2$; $x$ and $y$ are the **coordinates** of $(x, y)$.
>
> *Eccles: Definition 7.7.1*

^def-7a-2

> [!example] Example §7a.7: Products
> - For $X = \{a, b, c\}$ and $Y = \{a, b\}$: $X \times Y = \{(a,a), (a,b), (b,a), (b,b), (c,a), (c,b)\}$ and $Y \times X = \{(a,a), (a,b), (a,c), (b,a), (b,b), (b,c)\}$. These are different: $(c, a) \in X \times Y$ but $(c, a) \notin Y \times X$.
> - $\R^2 = \R \times \R$ is the Euclidean plane. A predicate $P(x, y)$ defines a subset $\{(x, y) \in \R^2 \mid P(x, y)\}$, e.g. the unit circle $\{(x, y) \in \R^2 \mid x^2 + y^2 = 1\}$, the set of points satisfying the *equation* $x^2 + y^2 = 1$.
>
> *Eccles: Examples 7.7.2*

^ex-7a-7

> [!example] Example §7a.8: Quantified Statements as Pictures
> A predicate $P(a, b)$ on $A \times B$ determines its truth set $T = \{(a, b) \in A \times B \mid P(a, b)\}$. Write $\{a\} \times B$ for the vertical line through $a$ and $A \times \{b\}$ for the horizontal line through $b$. Then:
> - $\forall a\, \exists b,\ P(a, b)$: every vertical line meets $T$;
> - $\exists a\, \forall b,\ P(a, b)$: some vertical line lies entirely in $T$;
> - $\forall b\, \exists a,\ P(a, b)$: every horizontal line meets $T$;
> - $\exists b\, \forall a,\ P(a, b)$: some horizontal line lies entirely in $T$.
>
> For $m < n$ on $\Z^+ \times \Z^+$ (figure below), this re-proves [[§7a Several Quantifiers and the Cartesian Product#^ex-7a-1|Example §7a.1]]: (a) is true because the column $\{m\} \times \Z^+$ contains $(m, m + 1)$; (b) is false because each row $\Z^+ \times \{n\}$ contains $(n, n) \notin T$; (c) is false because the row $\Z^+ \times \{1\}$ misses $T$; (d) is false because each column $\{m\} \times \Z^+$ contains $(m, m) \notin T$.
>
> *Eccles: Example 7.7.3*

^ex-7a-8

![[m250-7-1.svg]]
*The truth set of $m < n$ in $\Z^+ \times \Z^+$: solid dots above the diagonal. Every column, such as $\{3\} \times \Z^+$ (blue), contains a solid dot, so $\forall m\, \exists n,\ m < n$; the bottom row $\Z^+ \times \{1\}$ (red) contains none, so $\forall n\, \exists m,\ m < n$ fails at $n = 1$.*

> [!example] Example §7a.9: An Implication as a Region of the Plane
> **Problem:** find all points $(x, y)$ for which the propositional form $2x + 3y > 6 \Rightarrow x \le y^2$ is true.
>
> Since $(P \Rightarrow Q) \equiv (\neg P \vee Q)$ ([[§2 Implications#^prop-2-1|Proposition §2.1]]), the truth set is
>
> $$
> \{(x, y) \in \R^2 \mid 2x + 3y \le 6\} \cup \{(x, y) \in \R^2 \mid x \le y^2\} ,
> $$
>
> the union of the closed half-plane on or below the line $2x + 3y = 6$ and the region on or to the left of the parabola $x = y^2$: a disjunction of conditions becomes a union of regions. The implication fails exactly on the complement, where $2x + 3y > 6$ and $x > y^2$: inside the parabola and strictly above the line. The line meets the parabola where $2y^2 + 3y - 6 = 0$, i.e. $y = \frac{-3 \pm \sqrt{57}}{4}$.
>
> *Source: MAT 200 Practice Midterm 1, Problem 5*

^ex-7a-9

![[m250-7-2.svg]]
*The truth set of $2x + 3y > 6 \Rightarrow x \le y^2$ (shaded) is everything except the white region, which lies inside the parabola $x = y^2$ (blue) and above the line $2x + 3y = 6$ (dashed). Its lower-left edge (red, a piece of the line) belongs to the truth set, since there $2x + 3y = 6$ is not $> 6$.*

> [!theorem] Proposition §7a.2: Products, Unions and Intersections
> For all sets $A$, $B$, $C$, $D$:
> 1. $A \times (B \cup C) = (A \times B) \cup (A \times C)$;
> 2. $A \times (B \cap C) = (A \times B) \cap (A \times C)$;
> 3. $(A \times B) \cap (C \times D) = (A \cap C) \times (B \cap D)$;
> 4. $(A \times B) \cup (C \times D) \subseteq (A \cup C) \times (B \cup D)$.
>
> *Eccles: Proposition 7.7.4*

^prop-7a-2

> [!proof]+ Proof
> Each part is proved from the definitions by following an element $(x, y)$; for the equalities both inclusions can be done at once with a chain of equivalences.
>
> (1) $(x, y) \in A \times (B \cup C) \iff x \in A$ and ($y \in B$ or $y \in C$) $\iff$ ($x \in A$ and $y \in B$) or ($x \in A$ and $y \in C$) $\iff (x, y) \in A \times B$ or $(x, y) \in A \times C \iff (x, y) \in (A \times B) \cup (A \times C)$, using the distributive law $P \wedge (Q \vee R) \equiv (P \wedge Q) \vee (P \wedge R)$.
>
> (2) $(x, y) \in A \times (B \cap C) \iff x \in A$ and $y \in B$ and $y \in C \iff (x, y) \in A \times B$ and $(x, y) \in A \times C \iff (x, y) \in (A \times B) \cap (A \times C)$.
>
> (3) $(x, y) \in (A \times B) \cap (C \times D) \iff x \in A$ and $y \in B$ and $x \in C$ and $y \in D \iff x \in A \cap C$ and $y \in B \cap D \iff (x, y) \in (A \cap C) \times (B \cap D)$.
>
> (4) Let $(x, y) \in (A \times B) \cup (C \times D)$. If $(x, y) \in A \times B$, then $x \in A \subseteq A \cup C$ and $y \in B \subseteq B \cup D$, so $(x, y) \in (A \cup C) \times (B \cup D)$. If $(x, y) \in C \times D$, then likewise $x \in C \subseteq A \cup C$ and $y \in D \subseteq B \cup D$.

^pf-7a-2

*Uses:* [[§7a Several Quantifiers and the Cartesian Product#^def-7a-1|Def. §7a.1]], [[§6a Operations on Sets#^def-6a-1|Def. §6a.1]], [[§6a Operations on Sets#^def-6a-3|Def. §6a.3]], [[§6a Operations on Sets#^thm-6a-2|§6a.2]]

> [!example] Example §7a.10: The Inclusion in Part 4 Can Be Strict
> **Claim:** $(A \times B) \cup (C \times D) \subseteq (A \cup C) \times (B \cup D)$, and the two sets need not be equal.
>
> In logical form the inclusion says: for all $x, y$,
>
> $$
> (x \in A \wedge y \in B) \vee (x \in C \wedge y \in D) \ \Rightarrow\ (x \in A \vee x \in C) \wedge (y \in B \vee y \in D).
> $$
>
> Distributing, the left side is equivalent to $(x \in A \vee x \in C) \wedge (x \in A \vee y \in D) \wedge (y \in B \vee x \in C) \wedge (y \in B \vee y \in D)$, a conjunction of four statements whose first and last are the right side; and $P \wedge Q \Rightarrow P$. (This is a second proof of [[§7a Several Quantifiers and the Cartesian Product#^prop-7a-2|§7a.2]](4).)
>
> **Counterexample to equality:** take $A = B = \{1\}$ and $C = D = \{2\}$. Then $(A \times B) \cup (C \times D) = \{(1,1), (2,2)\}$, while $(A \cup C) \times (B \cup D) = \{1, 2\}^2$ also contains $(1, 2)$ and $(2, 1)$. In the plane: two squares on the diagonal versus the large square containing them and the two off-diagonal squares.
>
> *Source: HW3*
> *Eccles: Exercise 7.7*

^ex-7a-10
