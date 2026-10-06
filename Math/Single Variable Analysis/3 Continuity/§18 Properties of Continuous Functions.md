---
type: section
subject: "[[Single Variable Analysis]]"
section: 18
chapter: 3
tags: [real-analysis, math451]
---
← [[§17 Continuous Functions]] · ↑ [[· 3 Continuity]] · [[§19 Uniform Continuity]] →

Now we come to one of the most exciting sections of this course. We have defined continuous functions and have examples. *What can we do with them?* To use them, we need to know their properties — to sharpen our tools. Throughout, the recurring theme: given $f$, the domain $\operatorname{dom}(f) = \Omega$ is part of the definition; now we want to understand the **image**

$$
\operatorname{Im}(f) = \{ f(x) \mid x \in \Omega \}.
$$

## The Extreme Value Theorem

> [!definition] Definition §18.1: Bounded Function
> A function $f: \Omega \to \mathbb{R}$ is called **bounded** if the set $\{f(x) \mid x \in \Omega\}$ is a bounded subset of $\mathbb{R}$: there exists $M > 0$ such that $|f(x)| \leq M$ for all $x \in \Omega$.

^def-18-1

> [!theorem] Theorem §18.1: Extreme Value Theorem
> Let $\Omega = [a,b]$ be a finite closed interval and $f: [a,b] \to \mathbb{R}$ continuous. Then $f$ is bounded and *achieves* its maximum and minimum values: there exist $x_0, y_0 \in [a,b]$ such that for every $x \in [a,b]$,
>
> $$
> f(y_0) \leq f(x) \leq f(x_0),
> $$
>
> i.e. $f(x_0) = \max \operatorname{Im}(f)$ and $f(y_0) = \min \operatorname{Im}(f)$.

^thm-18-1

Boundedness is the basic beginning; the existence of max and min is very important in applications to optimization. In basic calculus one often *assumes* they exist and works on finding them; here we address the more basic problem — existence.

> [!proof]+ Proof
> **Step 1: $f$ is bounded.** How to find a bound $M$? What is its value? No idea — so we prove it by contradiction. If $f$ is not bounded, then for every $n \in \mathbb{N}$ there exists $x_n \in [a,b]$ with
>
> $$
> |f(x_n)| \geq n.
> $$
>
> Since $a \leq x_n \leq b$, the sequence $(x_n)$ is bounded. By the **[[Bolzano–Weierstrass Theorem|Bolzano–Weierstrass Theorem]]** (§11), there is a convergent subsequence $x_{n_k} \to x_0$. *Claim: $x_0 \in [a,b]$* — because $a \leq x_{n_k} \leq b$ and limits preserve the inequalities. Since $f$ is continuous at $x_0$,
>
> $$
> f(x_{n_k}) \longrightarrow f(x_0);
> $$
>
> but $|f(x_{n_k})| \geq n_k \to \infty$, so $(f(x_{n_k}))$ is unbounded — while every convergent sequence is bounded (§9). Contradiction. So $f$ is bounded.
>
> **Step 2: the max is achieved** (the min is the same). By Step 1, $\operatorname{Im}(f)$ is a bounded (nonempty) subset of $\mathbb{R}$, so by the **[[Completeness Axiom|completeness axiom]]**
>
> $$
> M = \sup \operatorname{Im}(f)
> $$
>
> exists. We need $x_0 \in [a,b]$ with $f(x_0) = M$. For any $n \in \mathbb{N}$, $M - \tfrac1n$ is not an upper bound of $\operatorname{Im}(f)$, so some point $x_n \in [a,b]$ has $f(x_n) > M - \tfrac1n$; combined with $f(x_n) \leq M$,
>
> $$
> M - \frac1n < f(x_n) \leq M.
> $$
>
> By Bolzano–Weierstrass again, extract $x_{n_k} \to x_0 \in [a,b]$ (as in Step 1). By continuity, $f(x_{n_k}) \to f(x_0)$; by the [[Squeeze Theorem|Squeeze Theorem]] along the subsequence of the displayed inequalities, $f(x_{n_k}) \to M$. By uniqueness of limits, $f(x_0) = M$. Done!

^pf-18-1

*Uses:* [[Bolzano–Weierstrass Theorem|§11.5]], [[§9 Limit Theorems for Sequences#^prop-9-5|§9.5]], [[§9 Limit Theorems for Sequences#^thm-9-1|§9.1]], [[Completeness Axiom|Def. §4.4]], [[Squeeze Theorem|§8.1]], [[§7 Limits of Sequences#^thm-7-1|§7.1]]

> [!remark]- Connections
> - Abstract form: a continuous image of a compact space is compact, [[§15 Compact Spaces#^thm-15-3|590 Thm. §15.3]], and [a, b] is compact by [[§15 Compact Spaces#^thm-15-12|590 Thm. §15.12]] (Heine–Borel).
> - Computational version: [[§25 Maximum and Minimum Values#^thm-25-1|Calc Thm. §25.1]] (with worked examples).
> - Computational version: [[§18 Continuity#^thm-18-6|342 Thm. §18.6]] (a continuous function on a closed bounded region of ℂ is bounded and its modulus attains a maximum).

> [!remark] Remark: Toward Optimization
> Application (borrowing differentiation from [[· 5 Differentiation|Chapter 5]]): if $f$ is moreover differentiable on $(a,b)$ and the max point $x_0$ lies in the open interval $(a,b)$, then $x_0$ is a critical point, $f'(x_0) = 0$. So to find the maximum: find all critical points in $(a,b)$ and compare their values with the values at the endpoints $a, b$. The theorem above is what guarantees this recipe finds something.

^rem-18-1

> [!remark] Remark: Both Hypotheses Are Needed
> **(1) The interval must be closed (and finite):** $f(x) = \tfrac1x$ on $(0,1]$ is continuous, but $(0,1]$ is not closed, and $f$ is not bounded — $f(\tfrac1n) = n \to \infty$. **(2) The function must be continuous:** $g: [0,1] \to \mathbb{R}$ with $g(0) = 0$, $g(x) = \tfrac1x$ for $x \in (0,1]$ is defined on a finite closed interval but is not continuous at $0$ — and is not bounded.

^rem-18-2

Where *exactly* does the proof need closedness? Reread Step 1 with $(a,b)$ in place of $[a,b]$ (HW): Bolzano–Weierstrass still extracts a convergent subsequence $x_{n_k} \to x_0$ — but the load-bearing step is “*$x_0 \in [a,b]$, since limits preserve the endpoint inequalities*.” For an open interval, $x_0$ may be an endpoint *outside* the domain, and then $f(x_0)$ is not even defined — the continuity argument has nowhere to land. And this failure is universal, not an accident of $\tfrac1x$:

> [!theorem] Proposition §18.2: Non-Closed Sets Always Carry Unbounded Continuous Functions (HW)
> Let $S \subseteq \mathbb{R}$, and suppose some sequence $(x_n)$ in $S$ converges to a point $x_0 \notin S$. Then there exists a continuous unbounded function on $S$.

^prop-18-2

> [!proof]+ Proof
> Take
>
> $$
> f(x) = \frac{1}{x - x_0}.
> $$
>
> Since $x_0 \notin S$, the denominator never vanishes on $S$, so $f$ is defined and continuous on $S$ (quotient of continuous functions, [[§17 Continuous Functions#^thm-17-3|Theorem §17.3]](3)). It is unbounded: given $M > 0$, convergence $x_n \to x_0$ provides $n$ with $0 < |x_n - x_0| < \tfrac1M$, and then
>
> $$
> |f(x_n)| = \frac{1}{|x_n - x_0|} > M.
> $$

^pf-18-2

*Uses:* [[§17 Continuous Functions#^thm-17-3|§17.3]]

So a set on which the boundedness conclusion of the EVT holds for *all* continuous functions must contain all its sequential limits: it must be *closed* in the sense of §13. Closedness alone is not enough — $f(x) = x$ is continuous and unbounded on every unbounded set, such as the closed set $\mathbb{R}$ — and the sets that work are exactly the closed *bounded* ones: for these, Step 1 of the proof above goes through verbatim, the limit $x_0$ landing in the set by [[§13 Some Topological Concepts in Metric Spaces#^prop-13-5|Proposition §13.5]].

## The Intermediate Value Theorem

> [!theorem] Theorem §18.3: Intermediate Value Theorem
> Let $f: [a,b] \to \mathbb{R}$ be continuous. Then $f$ takes every value between $f(a)$ and $f(b)$: for any number $y$ between $f(a)$ and $f(b)$, there exists $x \in [a,b]$ with
>
> $$
> f(x) = y.
> $$

^thm-18-3

> [!proof]+ Proof
> Simplify first. If $f(a) = f(b)$, the statement is clear — the only value between them is $f(a)$ itself, achieved at both endpoints. So assume $f(a) \neq f(b)$; say $f(a) < f(b)$ (the case $f(a) > f(b)$ is the same, e.g. by applying the result to $-f$). If $y = f(a)$ or $y = f(b)$ we are done, so let $f(a) < y < f(b)$.
>
> *The idea:* start at $a$ and move toward $b$. Since the function is continuous — we cannot jump — we must meet the height $y$, like passing every intermediate altitude when climbing a mountain. To catch the moment we reach height $y$, define
>
> $$
> S = \{ x \in [a,b] \mid f(x) < y \}.
> $$
>
> (1) $S \neq \emptyset$: because $a \in S$ ($f(a) < y$). (2) $S$ is bounded: because $[a,b]$ is. By the [[Completeness Axiom|completeness axiom]], $x_0 = \sup S$ exists (and $x_0 \in [a,b]$: it is $\geq a$ since $a \in S$, and $\leq b$ since $b$ is an upper bound).
>
> *Claim: $f(x_0) = y$* — reasonable, since $x_0$ is “the last moment” at height below $y$. We prove the equality by the two inequalities $\leq$ and $\geq$.
>
> ($\leq$) By the [[Characterization of the Supremum|characterization of the supremum]], there exists a sequence $x_n \in S$ with $x_n \to x_0$ (for each $n$, $x_0 - \tfrac1n$ is not an upper bound of $S$). Since $f$ is continuous and $f(x_n) < y$,
>
> $$
> f(x_0) = \lim_{n\to\infty} f(x_n) \leq y.
> $$
>
> ($\geq$) From the inequality just proved, $f(x_0) \leq y < f(b)$, so $x_0 \neq b$, hence $x_0 < b$. Therefore, for all large $n$, $x_0 + \tfrac1n \leq b$, so $x_0 + \tfrac1n \in [a,b]$. Since $x_0 = \sup S$, the point $x_0 + \tfrac1n$ is *not* in $S$, which means
>
> $$
> f\left(x_0 + \tfrac1n\right) \geq y.
> $$
>
> Since $x_0 + \tfrac1n \to x_0$ and $f$ is continuous at $x_0$, $f(x_0 + \tfrac1n) \to f(x_0)$, and limits preserve $\geq$:
>
> $$
> f(x_0) \geq y.
> $$
>
> So finally $f(x_0) = y$. Done!

^pf-18-3

*Uses:* [[Completeness Axiom|Def. §4.4]], [[Characterization of the Supremum|§4.3]], [[§9 Limit Theorems for Sequences#^prop-9-5|§9.5]]

![[m451-18-2.svg]]
*The set $S = \{x \in [a,b] \mid f(x) < y\}$ (red, on the axis) can be a union of several pieces; its endpoints where $f = y$ are excluded (hollow), while $a \in S$ (filled). The proof does not look for the first crossing but for $x_0 = \sup S$: points of $S$ approach it from the left, giving $f(x_0) \leq y$, and every point to its right lies outside $S$, giving $f(x_0) \geq y$.*

> [!remark]- Connections
> - Abstract form: a continuous image of a connected space is connected, [[§13 Connected Spaces#^thm-13-3|590 Thm. §13.3]], giving the IVT for any connected domain, [[§14 Connected Subspaces of ℝ#^thm-14-3|590 Thm. §14.3]].
> - Computational version: [[§10 Continuity#^thm-10-10|Calc Thm. §10.10]] (with worked examples).

> [!theorem] Corollary §18.4: Sign Change Gives a Root
> If $f: [a,b] \to \mathbb{R}$ is continuous and $f(a)$, $f(b)$ have opposite signs, then there exists $x_0 \in [a,b]$ with $f(x_0) = 0$.

^cor-18-4

> [!proof]+ Proof
> $0$ lies between $f(a)$ and $f(b)$; apply the [[Intermediate Value Theorem|Intermediate Value Theorem]].

^pf-18-4

*Uses:* [[Intermediate Value Theorem|§18.3]]

> [!remark]- Connections
> - Worked examples: locating a root by a sign change, [[§10 Continuity#^ex-10-5|Calc Ex. §10.5]].

> [!theorem] Corollary §18.5: The Image Is a Closed Interval
> For continuous $f: [a,b] \to \mathbb{R}$,
>
> $$
> \operatorname{Im}(f) = \bigl[\, \min \operatorname{Im}(f),\ \max \operatorname{Im}(f) \,\bigr]
> $$
>
> — the image is again a finite closed interval. Continuous functions preserve finite closed intervals.

^cor-18-5

> [!proof]+ Proof
> By the [[Extreme Value Theorem|Extreme Value Theorem]] there are points $x_{\min}, x_{\max} \in [a,b]$ achieving $m = \min\operatorname{Im}(f)$ and $M = \max\operatorname{Im}(f)$, and $\operatorname{Im}(f) \subseteq [m, M]$. Conversely, assume $x_{\min} \leq x_{\max}$ (the other case is the same) and apply the Intermediate Value Theorem to the restriction $f: [x_{\min}, x_{\max}] \to \mathbb{R}$: $f$ takes every value between $f(x_{\min}) = m$ and $f(x_{\max}) = M$. So $[m,M] \subseteq \operatorname{Im}(f)$. Amazing! (This preservation property is the beginning of the topological notion of *connectedness*: continuous images of path-connected spaces are path-connected.)

^pf-18-5

*Uses:* [[Extreme Value Theorem|§18.1]], [[Intermediate Value Theorem|§18.3]]

> [!remark] Remark: Descending the Mountain
> The case $f(a) > f(b)$ can also be handled directly, without passing to $-f$: imagine coming *down* from the peak. For $f(a) > y > f(b)$, define instead
>
> $$
> S = \{ x \in [a,b] \mid f(x) > y \}
> $$
>
> — all the times spent *above* height $y$; note $a \in S$. With $x_0 = \sup S$, the same proof as before gives $f(x_0) = y$.

^rem-18-3

## Applications of the Intermediate Value Theorem

> [!remark] Remark: The Bisection Algorithm
> The sign-change corollary can be upgraded to an *algorithm* for approximating the root $x_0$:
>
> 1. Divide $[a,b]$ into two equal subintervals $[a,c]$, $[c,b]$, where $c = \tfrac12(a+b)$.
>
> 2. If $f(c) = 0$, take $x_0 = c$: done. Otherwise, one of the pairs $f(a), f(c)$ or $f(c), f(b)$ has opposite signs — why? because $f(a), f(b)$ do, and $f(c)$ agrees in sign with one of them. Keep the subinterval with the sign change; it contains a zero.
>
> 3. Repeat. Each step halves the interval, so we narrow down $x_0$ quickly (error $\leq (b-a)/2^n$ after $n$ steps).

^rem-18-4

> [!theorem] Theorem §18.6: Fixed Point Theorem on an Interval
> Let $f: [0,1] \to [0,1]$ be a continuous map. Then there exists $x_0 \in [0,1]$ with
>
> $$
> f(x_0) = x_0.
> $$
>
> Such a point — mapped to itself — is called a **fixed point**.

^thm-18-6

> [!proof]+ Proof
> A fixed point of $f$ is a zero of the function $g(x) = f(x) - x$, continuous on $[0,1]$. Check the endpoint values — here the assumption that $f$ maps *into* $[0,1]$ is what matters:
>
> $$
> g(0) = f(0) - 0 = f(0) \geq 0, \qquad g(1) = f(1) - 1 \leq 0.
> $$
>
> If either is zero, we are done. Otherwise $g(0) > 0$ and $g(1) < 0$ have opposite signs, and the sign-change corollary gives $x_0$ with $g(x_0) = 0$, i.e. $f(x_0) = x_0$.

^pf-18-6

*Uses:* [[§18 Properties of Continuous Functions#^cor-18-4|§18.4]]

![[m451-18-1.svg]]
*The graph of $f: [0,1] \to [0,1]$ stays in the unit square: it starts on or above the diagonal and ends on or below it — so it must cross $y = x$. The same picture underlies the chord example below: two continuous curves that swap order must meet.*

> [!remark]- Connections
> - Since [0, 1] is the ball B¹, this is the case n = 0 of the Brouwer fixed point theorem, proved in 590 for the disc and for all balls: [[§26 Deformation Retracts and Homotopy Type#^thm-26-7|590 Thm. §26.7]], [[§26 Deformation Retracts and Homotopy Type#^thm-26-10|590 Thm. §26.10]].

> [!example] Example §18.1: A Chord of Prescribed Length
> Let $f: [0,2] \to \mathbb{R}$ be continuous with $f(0) = f(2)$. Prove there exist $x, y \in [0,2]$ with
>
> $$
> |y - x| = 1 \qquad \text{and} \qquad f(x) = f(y).
> $$
>
> Why should this be true? Draw the graph — a curve returning to its starting height — and slide a horizontal chord of length $1$ along it to convince yourself.
>
> *The real proof.* We need a new function to which the sign-change corollary applies. Define
>
> $$
> g(x) = f(x+1) - f(x), \qquad x \in [0,1]
> $$
>
> — these are exactly the $x$ for which both $f(x)$ and $f(x+1)$ are defined. A zero $x_0$ of $g$ solves the problem, with $(x, y) = (x_0, x_0 + 1)$. Compute the endpoint values:
>
> $$
> g(0) = f(1) - f(0), \qquad
> g(1) = f(2) - f(1) = f(0) - f(1) = -g(0),
> $$
>
> using $f(2) = f(0)$. So $g(0)$ and $g(1)$ are negatives of each other: either both are $0$ (done), or they have opposite signs, and the corollary gives the zero.

^ex-18-1

![[m451-18-3.svg]]
*A curve with $f(0) = f(2)$ and a horizontal chord of length $1$ (red) with both ends on the graph: $f(x_0) = f(x_0 + 1)$. The point $x_0$ is the zero of $g(x) = f(x+1) - f(x)$ on $[0,1]$ provided by the sign-change corollary.*

> [!remark] Remark: Why Fixed Point Theorems Matter
> A fixed point theorem asserts the existence of a solution of an equation $f(x) = x$ — and $f$ can be a continuous map from *any* topological space to itself, not just $[0,1]$. For the unit square, the famous **Brouwer fixed point theorem** says every continuous $f: [0,1]^2 \to [0,1]^2$ has a fixed point; the same holds for the cube $[0,1]^3$ and in every dimension. (A cousin of this circle of ideas is the reason there is a spot on everyone's head where the hair cannot be combed flat.) Only in dimension one is there a simple proof, as above; higher dimensions require advanced tools of topology. In this general form, fixed point theorems are important far beyond mathematics — in economics, game theory, and elsewhere.

^rem-18-5

Both applications above followed one pattern: build an auxiliary difference function and apply the sign-change corollary. The pattern itself deserves a statement:

> [!theorem] Proposition §18.7: Crossing Lemma (HW)
> Let $f, g: [a,b] \to \mathbb{R}$ be continuous with
>
> $$
> f(a) \geq g(a) \qquad \text{and} \qquad f(b) \leq g(b).
> $$
>
> Then $f(x_0) = g(x_0)$ for at least one $x_0 \in [a,b]$: two continuous graphs that start and end on opposite sides must cross.

^prop-18-7

> [!proof]+ Proof
> Let $h = f - g$, continuous on $[a,b]$, with $h(a) \geq 0$ and $h(b) \leq 0$. So $0$ lies between $h(b)$ and $h(a)$, and the Intermediate Value Theorem gives $x_0 \in [a,b]$ with $h(x_0) = 0$, i.e. $f(x_0) = g(x_0)$.

^pf-18-7

*Uses:* [[Intermediate Value Theorem|§18.3]]

> [!remark] Remark
> The Fixed Point Theorem is the special case $g(x) = x$ on $[0,1]$: the hypothesis $f([0,1]) \subseteq [0,1]$ says exactly $f(0) \geq g(0)$ and $f(1) \leq g(1)$. The chord example fits the pattern too, with $f(x+1)$ and $f(x)$ in the two roles.

^rem-18-6

> [!theorem] Proposition §18.8: Odd-Degree Polynomials Have Real Roots (HW)
> Every polynomial $f(x) = a_0 + a_1 x + \cdots + a_{d} x^{d}$ of odd degree $d$ (with $a_d \neq 0$) has at least one real root.

^prop-18-8

> [!proof]+ Proof
> We may assume $a_d > 0$ (otherwise pass to $-f$, which has the same roots). The idea: the leading term dominates far from the origin, so $f$ takes both signs; the IVT does the rest. To make “dominates” rigorous without limits of functions (§20 is still ahead), bound the lower-order part: let $C = |a_0| + \cdots + |a_{d-1}|$; then for $|x| \geq 1$,
>
> $$
> \bigl| a_0 + a_1 x + \cdots + a_{d-1} x^{d-1} \bigr| \leq C\,|x|^{d-1}.
> $$
>
> Take any $x_1 \geq \max\left\{ 1,\ \tfrac{2C}{a_d} \right\}$. Then
>
> $$
> f(x_1) \geq a_d x_1^{d} - C x_1^{d-1} = x_1^{d-1} \bigl( a_d x_1 - C \bigr) > 0,
> $$
>
> and at $x_2 = -x_1$, using that $d$ is *odd* (so $x_2^{d} = -x_1^{d}$),
>
> $$
> f(x_2) \leq -a_d x_1^{d} + C x_1^{d-1} = x_1^{d-1}\bigl( C - a_d x_1 \bigr) < 0.
> $$
>
> Since $f$ is continuous on $[x_2, x_1]$ and $f(x_2) < 0 < f(x_1)$, the sign-change corollary gives $x_0 \in (x_2, x_1)$ with $f(x_0) = 0$.

^pf-18-8

*Uses:* [[Intermediate Value Theorem|§18.3]], [[§18 Properties of Continuous Functions#^cor-18-4|§18.4]]

> [!remark] Remark
> Where does the argument use oddness? Only in the sign flip $(-x_1)^d = -x_1^d$. For even degree the conclusion genuinely fails: $x^2 + 1$ has no real root. And the choice of $x_1$ shows more than existence — all real roots lie in $\left[ -\max\{1, \tfrac{2C}{a_d}\},\ \max\{1, \tfrac{2C}{a_d}\} \right]$, an explicit bound.

^rem-18-7

## Monotone Functions and Inverse Functions

Recall $\operatorname{Im}(f) = f([a,b])$ is a bounded closed interval. Assuming $f(a) \leq f(b)$, is it equal to $[f(a), f(b)]$? *Not in general* — it can be much bigger.

> [!example] Example §18.2: The Image Can Exceed the Endpoint Values
> $f(x) = \sin x$ on $[0, 2\pi]$: here $\operatorname{Im}(f) = [-1, 1]$, but $f(0) = f(2\pi) = 0$, so $[f(a), f(b)] = \{0\}$, a single point.

^ex-18-2

In one special case, equality does hold.

> [!definition] Definition §18.2: Strictly Monotone Functions
> $f: [a,b] \to \mathbb{R}$ is **strictly increasing** if $x_1 > x_2$ implies $f(x_1) > f(x_2)$ (e.g. $2x$, $x^3$), and **strictly decreasing** if $x_1 > x_2$ implies $f(x_1) < f(x_2)$. The two are related by the operations $f \mapsto -f$ and (for positive $f$) $f \mapsto \tfrac1f$: e.g. $e^{-x} = \tfrac{1}{e^x}$ and $-e^x$ are strictly decreasing.

^def-18-2

> [!remark]- Connections
> - Computational version: increasing and decreasing functions, [[§1 Four Ways to Represent a Function#^def-1-8|Calc Def. §1.8]].

> [!theorem] Theorem §18.9: Continuous Inverse Theorem
> If $f: [a,b] \to \mathbb{R}$ is a strictly increasing continuous function, then $\operatorname{Im}(f) = [f(a), f(b)]$, and the inverse function
>
> $$
> f^{-1}: [f(a), f(b)] \to [a,b]
> $$
>
> exists and is a strictly increasing continuous function. (Similarly, for strictly decreasing $f$: $\operatorname{Im}(f) = [f(b), f(a)]$ and $f^{-1}$ is strictly decreasing and continuous.)

^thm-18-9

> [!proof]+ Proof
> **The image.** By strict monotonicity, $f(a)$ is the minimum value and $f(b)$ the maximum; by the closed-interval corollary above, $\operatorname{Im}(f) = [f(a), f(b)]$.
>
> **Existence of $f^{-1}$.** For every $y \in [f(a), f(b)]$ there exists $x \in [a,b]$ with $f(x) = y$ (Intermediate Value Theorem), and this $x$ is *unique*: any other $x_1 \neq x$ has $f(x_1) \neq f(x)$ by strict monotonicity. So $f^{-1}(y) = x$ is well defined.
>
> **Continuity of $f^{-1}$.** Fix $y_0 \in [f(a), f(b)]$ and any sequence $y_n \to y_0$ in $[f(a), f(b)]$; we must show $f^{-1}(y_n) \to f^{-1}(y_0)$. The sequence $x_n = f^{-1}(y_n) \in [a,b]$ is bounded. Suppose it does *not* converge to $f^{-1}(y_0)$. Then there exist $\varepsilon > 0$ and a subsequence with $|x_{n_k} - f^{-1}(y_0)| \geq \varepsilon$ for all $k$; by [[Bolzano–Weierstrass Theorem|Bolzano–Weierstrass]], extract a further subsequence (still denoted $x_{n_k}$) converging to some $x_0 \in [a,b]$, and passing to the limit in the inequality, $|x_0 - f^{-1}(y_0)| \geq \varepsilon$, so
>
> $$
> x_0 \neq f^{-1}(y_0).
> $$
>
> Since $f$ is continuous, $f(x_{n_k}) \to f(x_0)$; but $f(x_{n_k}) = y_{n_k} \to y_0$. By the uniqueness of limits, $y_0 = f(x_0)$, i.e. $x_0 = f^{-1}(y_0)$ — contradicting the display. So $x_n \to f^{-1}(y_0)$, and $f^{-1}$ is continuous at $y_0$.
>
> **$f^{-1}$ is strictly increasing.** By contradiction: if not, there exist $y_1 < y_2$ with $f^{-1}(y_1) \geq f^{-1}(y_2)$. Applying the increasing $f$ preserves $\geq$:
>
> $$
> y_1 = f(f^{-1}(y_1)) \geq f(f^{-1}(y_2)) = y_2,
> $$
>
> a contradiction.

^pf-18-9

*Uses:* [[§18 Properties of Continuous Functions#^cor-18-5|§18.5]], [[Intermediate Value Theorem|§18.3]], [[Bolzano–Weierstrass Theorem|§11.5]], [[§7 Limits of Sequences#^thm-7-1|§7.1]], [[§9 Limit Theorems for Sequences#^prop-9-5|§9.5]]

> [!remark] Remark: Beyond Closed Intervals
> The theorem extends to strictly monotone continuous functions on intervals of any type (open, half-open, infinite): apply it on closed subintervals exhausting the domain. The standard application: granting that $e^x: \mathbb{R} \to (0, +\infty)$ is strictly increasing and continuous (rigorous treatment of $e^x$ later), its inverse
>
> $$
> \log: (0, +\infty) \to \mathbb{R}
> $$
>
> exists and is continuous — finally putting the logarithm, borrowed on credit in §9, on firmer footing (its continuity, at least; its defining properties still await the rigorous $e^x$).

^rem-18-8

> [!remark]- Connections
> - Topological form: a continuous bijection from a compact space to a Hausdorff space is a homeomorphism, [[§15 Compact Spaces#^thm-15-7|590 Thm. §15.7]].
> - Computational version: [[§10 Continuity#^thm-10-5|Calc Thm. §10.5]].
> - Computational version: the logarithm as inverse of the exponential, [[§5 Inverse Functions and Logarithms#^thm-5-4|Calc Thm. §5.4]]; its continuity, [[§10 Continuity#^thm-10-6|Calc Thm. §10.6]].
