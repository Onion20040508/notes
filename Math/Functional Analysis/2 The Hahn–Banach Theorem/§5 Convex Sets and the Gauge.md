---
type: section
subject: "[[Functional Analysis]]"
chapter: 2
section: 5
tags: [functional-analysis, math556]
---
← [[§4 Proof of the Hahn–Banach Theorem]] · ↑ [[· 2 The Hahn–Banach Theorem]] · [[§6 The Hyperplane Separation Theorem]] →

*Stage: algebra — Thread: convexity. Convex sets and positive homogeneous subadditive functions are two descriptions of one object.*

The three functions $p_1, p_2, p_3$ on $\mathbb{R}^n$ ([[§3 Statement and Motivation#^ex-3-1|Ex. §3.1]]) each came with a convex set $\{p < 1\}$ ([[§3 Statement and Motivation#^ex-3-2|Ex. §3.2]]). This is the beginning of a two-way correspondence between positive homogeneous subadditive functions and convex sets, which is what makes [[§3 Statement and Motivation#^thm-3-2|Hahn–Banach]] a geometric theorem.

## From $p$ to a Convex Set

> [!theorem] Proposition §5.1: Positive Homogeneous Subadditive $p$ Gives a Convex Set
> Let $p : X \to \mathbb{R}$ be positive homogeneous and subadditive, and let
>
> $$
> K = \{ x \in X : p(x) \le 1 \}, \qquad K_0 = \{ x \in X : p(x) < 1 \}.
> $$
>
> Then $K$ and $K_0$ are convex.
>
> *Source: HW1*
>
> *Lax: §3.1, Thm 4*

^prop-5-1

> [!proof]+ Proof
> (HW1.) Let $x_1, x_2 \in K$ and $a \in [0,1]$. If $a = 0$ or $a = 1$ the point $a x_1 + (1-a) x_2$ is $x_2$ or $x_1$, which lies in $K$. For $0 < a < 1$, subadditivity followed by positive homogeneity (with the non-negative scalars $a$ and $1 - a$) gives
>
> $$
> p\bigl(a x_1 + (1-a) x_2\bigr) \le p(a x_1) + p\bigl((1-a) x_2\bigr) = a\,p(x_1) + (1-a)\,p(x_2) \le a \cdot 1 + (1-a) \cdot 1 = 1,
> $$
>
> so $a x_1 + (1-a) x_2 \in K$. For $K_0$ the same chain ends with $< a \cdot 1 + (1-a) \cdot 1 = 1$, strict because $p(x_1) < 1$, $p(x_2) < 1$ and both weights $a, 1-a$ are positive; the endpoint cases $a \in \{0,1\}$ are handled as before.

^pf-5-1

*Uses:* [[§3 Statement and Motivation#^def-3-1|Def. §3.1]], [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Def. §2.3]]

> [!remark]- Connections
> - The unit ball of a norm is convex by this proposition: [[§8 Normed Linear Spaces#^prop-8-1|§8.1]].

> [!remark] Remark
> On the board the set was written with $\le 1$; the homework uses $< 1$. Nothing in the convexity argument distinguishes the two, but they play different roles later: $K_0$ is the set all of whose points are interior (Proposition [[§5 Convex Sets and the Gauge#^prop-5-2|§5.2]]), and it is $K_0$, not $K$, that will be recovered from the gauge as $\{p_K < 1\}$. Both contain $0$, since $p(0) = 0$ (Lemma [[§3 Statement and Motivation#^lem-3-1|§3.1]]).

^rem-5-1

The converse direction — starting from a convex set and producing a $p$ — is the gauge, below. It requires a notion of interior point that makes sense without any topology.

## Interior Points, Algebraically

> [!definition] Definition §5.1: Interior Point
> Let $K \subset X$ be a subset of a linear space and $x_0 \in K$. We say $x_0$ is an **interior point** of $K$ if for every $y \in X$ there exists $\varepsilon = \varepsilon(y) > 0$ such that
>
> $$
> x_0 + t y \in K \qquad \text{for all } |t| < \varepsilon(y).
> $$
>
> *Lax: §3.1, definition of interior point*

^def-5-1

> [!remark]- Connections
> - The topological interior: [[§7 Interior and Closure#^def-7-1|590 Def. §7.1]]; in $\mathbb{R}^n$, [[§2 Open and Closed Sets#^def-2-3|452 Def. §2.3]].
> - Metric interior points are interior points in this sense, not conversely: [[§8 Normed Linear Spaces#^prop-8-7|§8.7]], [[§8 Normed Linear Spaces#^ex-8-2|Ex. §8.2]].

> [!remark] Remark: Comparison with the Classical Notion
> In a metric space, $x_0$ is an interior point of $K$ if some ball around $x_0$ lies in $K$. Here there is no ball. The definition says instead: in every direction $y$, one can move a little way from $x_0$ (in both senses, $t > 0$ and $t < 0$) and stay inside $K$. The allowed distance $\varepsilon(y)$ depends on the direction and is not uniform: $K$ may be very thin in one direction and long in another, and there need be no single $\varepsilon$ that works for all $y$. Whenever both notions make sense, an interior point in the classical sense is one in this sense, but not conversely (Proposition [[§8 Normed Linear Spaces#^prop-8-7|§8.7]] and the example after it, [[§8 Normed Linear Spaces#^ex-8-2|Ex. §8.2]]); this is the only notion available in a bare linear space.
>
> ![[m556-5-1.svg]]
> *Segments $x_0 + ty$, $|t| < \varepsilon(y)$, inside an elongated $K$ in three directions $y$: the allowed length depends on the direction.*

^rem-5-2

> [!theorem] Proposition §5.2: Every Point of $\{p < 1\}$ is Interior
> Let $p : X \to \mathbb{R}$ be positive homogeneous and subadditive, and $K_0 = \{ x \in X : p(x) < 1 \}$. Then every point of $K_0$ is an interior point of $K_0$.
>
> *Lax: §3.1, Thm 4(i)*

^prop-5-2

> [!proof]+ Proof
> (Not reached in lecture; written out here.) Let $x \in K_0$, so $p(x) < 1$, and let $y \in X$. Put $M = \max\{p(y), p(-y), 0\}$, a finite non-negative number, and choose
>
> $$
> \varepsilon(y) = \frac{1 - p(x)}{M + 1} > 0.
> $$
>
> For $|t| < \varepsilon(y)$, write $ty = |t| \cdot (\pm y)$ with the sign of $t$. By subadditivity and positive homogeneity,
>
> $$
> p(x + ty) \le p(x) + |t|\,p(\pm y) \le p(x) + |t| M < p(x) + \varepsilon(y)(M+1) = 1,
> $$
>
> so $x + ty \in K_0$. Hence $x$ is an interior point of $K_0$. (The $+1$ in the denominator only avoids dividing by $0$ when $M = 0$.)

^pf-5-2

*Uses:* [[§3 Statement and Motivation#^def-3-1|Def. §3.1]], [[§5 Convex Sets and the Gauge#^def-5-1|Def. §5.1]]

> [!remark] Remark: Comparison with Lax
> Lax's Theorem 4(i) asserts only that $0$ is an interior point of $\{p < 1\}$, leaving the rest as an exercise. The stronger statement proved here, that every point is interior, is what Corollary [[§5 Convex Sets and the Gauge#^cor-5-8|§5.8]] and the separation theorem ([[§6 The Hyperplane Separation Theorem#^thm-6-1|§6.1]]) use.

^rem-5-3

## The Gauge of a Convex Set

> [!definition] Definition §5.2: Gauge
> Let $K$ be a convex set in a linear space $X$ with $0$ an interior point of $K$. The **gauge** (or Minkowski functional) associated with $K$ is
>
> $$
> p_K(x) = \inf\Bigl\{ a > 0 \;:\; \frac{x}{a} \in K \Bigr\}, \qquad x \in X.
> $$
>
> *Lax: §3.1, equation (8)*

^def-5-2

> [!remark]- Connections
> - Norms are exactly the gauges of their unit balls: [[§8 Normed Linear Spaces#^prop-8-1|§8.1]].

> [!theorem] Proposition §5.3: The Gauge is Finite
> Under the hypotheses of the definition, the set $\{a > 0 : x/a \in K\}$ is nonempty for every $x \in X$, so $p_K(x) < \infty$. More precisely, if $\varepsilon(x) > 0$ is as in the definition of $0$ being an interior point, then $p_K(x) \le 1/\varepsilon(x)$.

^prop-5-3

> [!proof]+ Proof
> Fix $x \in X$. Since $0$ is an interior point of $K$, there is $\varepsilon(x) > 0$ such that $t x \in K$ for all $|t| < \varepsilon(x)$. Take any $t$ with $0 < t < \varepsilon(x)$. Then $t x = x / (1/t) \in K$, so $a = 1/t$ belongs to the set in the definition of $p_K$, and therefore $p_K(x) \le 1/t$. Since this holds for every $t \in (0, \varepsilon(x))$, letting $t \uparrow \varepsilon(x)$ gives $p_K(x) \le 1/\varepsilon(x) < \infty$.

^pf-5-3

*Uses:* [[§5 Convex Sets and the Gauge#^def-5-1|Def. §5.1]], [[§5 Convex Sets and the Gauge#^def-5-2|Def. §5.2]], [[§4 The Completeness Axiom#^cor-4-4|451 §4.4]]

> [!remark] Remark
> $p_K(x)$ measures how far $x$ must be shrunk toward the origin to land in $K$: $x / a \in K$ for all $a$ larger than $p_K(x)$, and for no $a$ smaller. Small $p_K(x)$ means $x$ is well inside $K$ (or that $K$ extends far in the direction of $x$); large $p_K(x)$ means $x$ is far outside. For $x = 0$ every $a > 0$ is admissible, so $p_K(0) = 0$. Note also that $p_K \ge 0$ by construction, unlike a general positive homogeneous subadditive $p$ (both facts are Proposition [[§5 Convex Sets and the Gauge#^prop-5-5|§5.5]](a) below).
>
> ![[m556-5-2.svg]]
> *Along the ray through $x$, the points $tx$ with $t$ small lie in $K$ (this is $0$ being interior, and gives $p_K(x) \le 1/\varepsilon(x)$); the point where the ray leaves $K$ is $x / p_K(x)$.*

^rem-5-4

## The Admissible Set and the Values of the Gauge

The material of this subsection was not covered in lecture; it makes precise the picture above.

> [!remark] Note: Notation
> For $K$ as in the definition of the gauge and $x \in X$, write
>
> $$
> A(x) = \{ a > 0 : x/a \in K \},
> $$
>
> so that $p_K(x) = \inf A(x)$. Proposition [[§5 Convex Sets and the Gauge#^prop-5-3|§5.3]] says $A(x) \neq \varnothing$.

^rem-5-5

> [!theorem] Lemma §5.4: Admissible Scales Form an Upper Set
> If $a \in A(x)$ and $a' > a$, then $a' \in A(x)$. Consequently $A(x)$ is an interval of the form $[p_K(x), \infty)$ or $(p_K(x), \infty)$.

^lem-5-4

> [!proof]+ Proof
> Write $\lambda = a/a' \in (0,1)$. Then
>
> $$
> \frac{x}{a'} = \lambda \cdot \frac{x}{a} + (1 - \lambda) \cdot 0,
> $$
>
> a convex combination of $x/a \in K$ and $0 \in K$. By convexity of $K$, $x/a' \in K$, i.e. $a' \in A(x)$. Thus $A(x)$ contains every number larger than any of its elements; together with $\inf A(x) = p_K(x)$ this gives the stated form, the endpoint being included exactly when $x / p_K(x) \in K$.

^pf-5-4

*Uses:* [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Def. §2.3]], [[§5 Convex Sets and the Gauge#^def-5-2|Def. §5.2]], [[§5 Convex Sets and the Gauge#^prop-5-3|§5.3]]

Both hypotheses on $K$ are used: convexity for the combination, and $0 \in K$ (which follows from $0$ being interior) for the second term.

> [!theorem] Proposition §5.5: Values of the Gauge
> Let $K$ be convex with $0$ an interior point, and $x \in X$.
> - (a) $p_K(x) \ge 0$, and $p_K(0) = 0$.
> - (b) If $x \in K$ then $p_K(x) \le 1$; if $x \notin K$ then $p_K(x) \ge 1$.
> - (c) $p_K(x) = 0$ if and only if the whole ray $\{ sx : s \ge 0 \}$ lies in $K$.
>
> *Lax: §3.1, Thm 3, (10)*

^prop-5-5

> [!proof]+ Proof
> (a) $A(x) \subset (0, \infty)$, so its infimum is $\ge 0$. For $x = 0$, $0/a = 0 \in K$ for every $a > 0$, so $A(0) = (0,\infty)$ and $p_K(0) = 0$.
>
> (b) If $x \in K$ then $1 \in A(x)$, so $p_K(x) \le 1$. If $x \notin K$ then $1 \notin A(x)$, and by Lemma [[§5 Convex Sets and the Gauge#^lem-5-4|§5.4]] no $a \le 1$ lies in $A(x)$ either (if some $a \le 1$ did, then $1 \ge a$ would). Hence $A(x) \subset (1, \infty)$ and $p_K(x) \ge 1$.
>
> (c) $p_K(x) = 0$ iff $A(x)$ contains arbitrarily small $a > 0$, iff (by Lemma [[§5 Convex Sets and the Gauge#^lem-5-4|§5.4]]) $A(x) = (0,\infty)$, iff $x/a \in K$ for all $a > 0$, iff $sx \in K$ for all $s > 0$; and $s = 0$ is included since $0 \in K$.

^pf-5-5

*Uses:* [[§5 Convex Sets and the Gauge#^def-5-2|Def. §5.2]], [[§5 Convex Sets and the Gauge#^lem-5-4|§5.4]]

> [!remark] Remark: Reading the Cases
> Positive homogeneity (Proposition [[§5 Convex Sets and the Gauge#^prop-5-6|§5.6]] below, $p_K(tx) = t\,p_K(x)$) says the gauge is not constant along a ray but *linear* along it: what is constant is the exit point $x^* = x / p_K(x)$ at which the ray through $x$ leaves $K$ (when $p_K(x) > 0$), and $p_K(x)$ counts how many copies of $x^*$ make up $x$.
>
> The two halves of (b) are the same statement seen from opposite sides. In both, $p_K(x)$ is the scale $a$ at which $x/a$ sits on the boundary of $K$:
> - *$x$ outside $K$.* Dividing by $a$ must *shrink* $x$, so $a$ increases from $1$; the points $x/a$ move along the ray toward $0$ and enter $K$ at $a = p_K(x) > 1$. Every larger $a$ is admissible (Lemma [[§5 Convex Sets and the Gauge#^lem-5-4|§5.4]]); no smaller $a$ is, since shrinking can only bring $x$ into $K$, never take it out. The crossing scale is the infimum.
> - *$x$ inside $K$.* Dividing by $a$ must *stretch* $x$, so $a$ decreases from $1$; the points $x/a$ move outward and reach the boundary at $a = p_K(x) < 1$. Every $a$ above this is admissible, no $a$ below it is, and again the crossing scale is the infimum.
>
> ![[m556-5-3.svg]]
> *The two halves of (b). Left, $x \notin K$: as $a$ grows past $p_K(x)$ the point $x/a$ enters $K$. Right, $x \in K$: as $a$ shrinks below $p_K(x)$ the point $x/a$ leaves $K$. In both, $x/p_K(x)$ (red) is where the ray crosses the boundary.*
>
> Two refinements. Whether the crossing scale itself belongs to $A(x)$ depends on whether the boundary point belongs to $K$: for the closed disk $A(x) = [\|x\|, \infty)$, for the open disk $A(x) = (\|x\|, \infty)$; the infimum is the same. And “until the edge” presupposes that the ray exits $K$. If it does not (part (c), and the example below), there is no edge to reach, $a$ can decrease all the way to $0$, and $p_K(x) = 0$ with $x \neq 0$. So $p_K(x) = 0$ does not force $x = 0$; exactly when a gauge is a norm is settled in Proposition [[§8 Normed Linear Spaces#^prop-8-1|§8.1]].

^rem-5-6

> [!example] Example §5.1: A Gauge Vanishing Off the Origin
> Let $X = \mathbb{R}^2$ and $K = \{ (x_1, x_2) : x_1 < 1 \}$, an open half-plane containing $0$ as an interior point. For $x = (x_1, x_2)$ with $x_1 \le 0$, every point $sx$, $s \ge 0$, has first coordinate $sx_1 \le 0 < 1$, so the whole ray lies in $K$ and $p_K(x) = 0$. For $x_1 > 0$, $x/a \in K$ iff $x_1/a < 1$ iff $a > x_1$, so $A(x) = (x_1, \infty)$ and $p_K(x) = x_1$. Altogether $p_K(x) = \max\{x_1, 0\}$: positive homogeneous, subadditive, non-negative, and zero on a whole half-plane.

^ex-5-1

> [!example] Example §5.2: Gauge of the Unit Disk
> Let $X = \mathbb{R}^2$ and $K = \{ x_1^2 + x_2^2 \le 1 \}$, the closed unit disk; $0$ is an interior point in the classical sense, hence in the algebraic sense. For $x = (x_1, x_2)$ and $a > 0$,
>
> $$
> \frac{x}{a} \in K \iff \Bigl(\frac{x_1}{a}\Bigr)^2 + \Bigl(\frac{x_2}{a}\Bigr)^2 \le 1 \iff a^2 \ge x_1^2 + x_2^2 \iff a \ge \sqrt{x_1^2 + x_2^2}.
> $$
>
> The infimum of such $a$ is attained, and
>
> $$
> p_K(x) = \bigl(x_1^2 + x_2^2\bigr)^{1/2} = \|x\|.
> $$
>
> So the gauge of the unit disk recovers the Euclidean length: the function $p_1$ of Example [[§3 Statement and Motivation#^ex-3-1|§3.1]] is the gauge of its own unit ball. Similarly, $p_2$ is the gauge of the square and $p_3$ the gauge of the diamond.

^ex-5-2

> [!example] Example §5.3: Gauge of a Square
> Let $X = \mathbb{R}^2$ and $K = \{ (x_1, x_2) : |x_1| \le 2,\ |x_2| \le 2 \}$, the closed square with vertices $(\pm 2, \pm 2)$; $0$ is an interior point. For $a > 0$,
>
> $$
> \frac{x}{a} \in K \iff \Bigl|\frac{x_1}{a}\Bigr| \le 2 \text{ and } \Bigl|\frac{x_2}{a}\Bigr| \le 2 \iff a \ge \frac{|x_1|}{2} \text{ and } a \ge \frac{|x_2|}{2} \iff a \ge \max\Bigl\{\frac{|x_1|}{2}, \frac{|x_2|}{2}\Bigr\}.
> $$
>
> Both conditions must hold (“and,” not “or”), so the smallest admissible $a$ is the larger of the two lower bounds, and
>
> $$
> p_K(x) = \tfrac{1}{2} \max\{ |x_1|, |x_2| \}.
> $$
>
> This is the function $p_2$ of Example [[§3 Statement and Motivation#^ex-3-1|§3.1]] scaled by $\tfrac12$; the factor records that $K$ is the square of side $4$, not $2$. Once again the gauge is a way of measuring the size of $x$, adapted to the shape of $K$.
>
> ![[m556-5-4.svg]]
> *For $x = (3, \tfrac32)$, $p_K(x) = \tfrac32$ and $x/p_K(x) = (2, 1)$ lies on the boundary. The level sets $\{p_K = c\}$ are the squares of half-side $2c$; the dashed one is $c = \tfrac12$. (The picture drawn in Lecture 3.)*

^ex-5-3

## The Gauge is Positive Homogeneous and Subadditive

> [!theorem] Proposition §5.6: The Gauge is Positive Homogeneous and Subadditive
> Let $K$ be a convex set in $X$ with $0$ an interior point. Then $p_K$ is positive homogeneous and subadditive:
>
> $$
> p_K(bx) = b\, p_K(x) \quad (b \ge 0), \qquad p_K(x + y) \le p_K(x) + p_K(y) \qquad \text{for all } x, y \in X.
> $$
>
> *Lax: §3.1, Thm 2*

^prop-5-6

> [!proof]+ Proof
> **Positive homogeneity.** For $b = 0$ both sides are $0$ by Proposition [[§5 Convex Sets and the Gauge#^prop-5-5|§5.5]](a). For $b > 0$,
>
> $$
> p_K(bx) = \inf\Bigl\{ a > 0 : \frac{bx}{a} \in K \Bigr\} = \inf\Bigl\{ a > 0 : \frac{x}{a/b} \in K \Bigr\}.
> $$
>
> Substituting $a' = a/b$, which runs over $(0,\infty)$ as $a$ does, the set is $\{ b a' : x/a' \in K \} = b\,A(x)$, whose infimum is $b \inf A(x) = b\, p_K(x)$. (Wu left this check to us.)
>
> **Subadditivity.** It is hard to work with the infimum directly, so take arbitrary admissible scales and pass to the infimum at the end. Let $a > 0$, $b > 0$ be such that
>
> $$
> \frac{x}{a} \in K, \qquad \frac{y}{b} \in K,
> $$
>
> so that $p_K(x) \le a$ and $p_K(y) \le b$. It suffices to show $p_K(x + y) \le a + b$, i.e. that $\dfrac{x + y}{a + b} \in K$; the claim then follows by taking the infimum over all such $a$, then over all such $b$. Now
>
> $$
> \frac{x + y}{a + b} = \frac{a}{a + b} \cdot \frac{x}{a} + \frac{b}{a + b} \cdot \frac{y}{b},
> $$
>
> and since $a, b > 0$,
>
> $$
> 0 < \frac{a}{a+b} < 1, \qquad 0 < \frac{b}{a+b} < 1, \qquad \frac{a}{a+b} + \frac{b}{a+b} = 1.
> $$
>
> So $(x + y)/(a + b)$ is a convex combination of the two points $x/a$, $y/b$ of $K$, hence lies in $K$ by convexity. Thus $a + b$ is an admissible scale for $x + y$ and $p_K(x + y) \le a + b$. Taking the infimum over $a \in A(x)$ and then over $b \in A(y)$ gives $p_K(x + y) \le p_K(x) + p_K(y)$.

^pf-5-6

*Uses:* [[§5 Convex Sets and the Gauge#^def-5-2|Def. §5.2]], [[§5 Convex Sets and the Gauge#^prop-5-3|§5.3]], [[§5 Convex Sets and the Gauge#^prop-5-5|§5.5]], [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Def. §2.3]], [[§3 Statement and Motivation#^def-3-1|Def. §3.1]]

> [!remark] Remark
> The two properties come from the two hypotheses on $K$: positive homogeneity is pure bookkeeping with the definition (it would hold for any $K$ for which the infimum is finite), while subadditivity is convexity, used exactly once, with the convexity coefficients $a/(a+b)$ and $b/(a+b)$. Together with Proposition [[§5 Convex Sets and the Gauge#^prop-5-1|§5.1]] this closes the loop: a positive homogeneous subadditive $p$ produces a convex set $\{p < 1\}$, and a convex set (with $0$ interior) produces a positive homogeneous subadditive $p_K$.

^rem-5-7

## Interior Points via the Gauge

> [!theorem] Proposition §5.7: Interior Points of $K$ are Exactly $\{p_K < 1\}$
> Let $K$ be a convex set in $X$ with $0$ an interior point.
> - (1) For all $x \in K$, $p_K(x) \le 1$.
> - (2) $x$ is an interior point of $K$ if and only if $p_K(x) < 1$.
>
> *Lax: §3.1, Thm 3, (10′)*

^prop-5-7

> [!proof]+ Proof
> (1) If $x \in K$ then $x/1 \in K$, so $a = 1$ is admissible and the infimum is at most $1$.
>
> (2) ($\Rightarrow$) Assume $x$ is an interior point of $K$. By (1), $p_K(x) \le 1$; we want strict inequality, i.e. some $a < 1$ with $x/a \in K$. Equivalently, it suffices to find $b > 0$ with $(1 + b)x \in K$, for then $a = 1/(1+b) < 1$ works. Apply the definition of interior point to $x$ in the direction $y = x$ itself: there is $\varepsilon(x) > 0$ such that
>
> $$
> x + bx \in K \qquad \text{for all } |b| < \varepsilon(x).
> $$
>
> In particular $(1 + b)x \in K$ for all $0 < b < \varepsilon(x)$, so
>
> $$
> p_K(x) \le \frac{1}{1 + b} < 1.
> $$
>
> Being interior means $x$ can be pushed a little in *every* direction, including outward along its own ray; that is all this direction uses.
>
> ($\Leftarrow$) Assume $p_K(x) < 1$. By definition of the infimum there is $a$ with $0 < a < 1$ and $x/a \in K$. We must show that for every $y \in X$ there is $\varepsilon(y) > 0$ with $x + ty \in K$ for all $|t| < \varepsilon(y)$.
>
> Fix $y \in X$. Since $0$ is an interior point of $K$, there is $\delta(y) > 0$ such that $ty = 0 + ty \in K$ for all $|t| < \delta(y)$. Now use convexity of $K$ on the two points $x/a \in K$ and $ty \in K$, with coefficients $a$ and $1 - a$ (both in $(0,1)$, summing to $1$):
>
> $$
> a \cdot \frac{x}{a} + (1 - a)\, ty \in K, \qquad \text{i.e.} \qquad x + (1 - a)\, t y \in K \qquad \text{for all } |t| < \delta(y).
> $$
>
> Replacing $(1-a)t$ by $t$, this says $x + ty \in K$ for all $|t| < (1 - a)\,\delta(y)$. So $\varepsilon(y) = (1 - a)\,\delta(y) > 0$ works, and $x$ is an interior point.

^pf-5-7

*Uses:* [[§5 Convex Sets and the Gauge#^def-5-1|Def. §5.1]], [[§5 Convex Sets and the Gauge#^def-5-2|Def. §5.2]], [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Def. §2.3]]

![[m556-5-5.svg]]
*The picture behind ($\Leftarrow$): the segment $\{ty : |t| < \delta(y)\}$ through $0$ lies in $K$, the apex $x/a$ lies in $K$, so by convexity the whole triangle they span lies in $K$. The point $x = a \cdot (x/a) + (1-a) \cdot 0$ sits on the median at fraction $a$ from the apex, and the triangle's cross-section through $x$ parallel to $y$ has half-length $(1 - a)\,\delta(y)$. That cross-section is the wiggle room at $x$ in the direction $y$.*

> [!theorem] Corollary §5.8: Convex Sets of Interior Points are Sublevel Sets
> Let $K \subset X$ be convex with $0 \in K$. The following are equivalent:
> - (i) every point of $K$ is an interior point of $K$;
> - (ii) $K = \{ x \in X : p(x) < 1 \}$ for some positive homogeneous subadditive $p : X \to \mathbb{R}$.
>
> When they hold, one can take $p = p_K$.
>
> *Lax: §3.1, Thms 3–4*

^cor-5-8

> [!proof]+ Proof
> (Not covered in lecture.) (ii)$\Rightarrow$(i) is Proposition [[§5 Convex Sets and the Gauge#^prop-5-2|§5.2]]. (i)$\Rightarrow$(ii): by (i), $0$ is an interior point, so $p_K$ is defined and is positive homogeneous and subadditive (Proposition [[§5 Convex Sets and the Gauge#^prop-5-6|§5.6]]). Since every point of $K$ is interior, $x \in K$ iff $x$ is an interior point of $K$, iff $p_K(x) < 1$ by Proposition [[§5 Convex Sets and the Gauge#^prop-5-7|§5.7]](2).

^pf-5-8

*Uses:* [[§5 Convex Sets and the Gauge#^prop-5-2|§5.2]], [[§5 Convex Sets and the Gauge#^def-5-2|Def. §5.2]], [[§5 Convex Sets and the Gauge#^prop-5-6|§5.6]], [[§5 Convex Sets and the Gauge#^prop-5-7|§5.7]]

> [!remark] Remark
> The corollary is the converse to Proposition [[§5 Convex Sets and the Gauge#^prop-5-1|§5.1]]: the sets $\{p < 1\}$ are exactly the convex sets containing $0$ all of whose points are interior, and each such set is recovered from its own gauge. The hypothesis that $0$ is interior was used in ($\Leftarrow$) of Proposition [[§5 Convex Sets and the Gauge#^prop-5-7|§5.7]] to get the base segment; without it the gauge is not even defined. This is the form in which the separation theorem ([[§6 The Hyperplane Separation Theorem#^thm-6-1|§6.1]]) uses the gauge.

^rem-5-8
