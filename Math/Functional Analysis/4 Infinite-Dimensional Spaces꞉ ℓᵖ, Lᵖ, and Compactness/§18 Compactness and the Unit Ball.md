---
type: section
subject: "[[Functional Analysis]]"
chapter: 4
section: 18
tags: [functional-analysis, math556]
---
← [[§17 The Function Spaces Lᵖ(Ω)]] · ↑ [[· 4 Infinite-Dimensional Spaces꞉ ℓᵖ, Lᵖ, and Compactness]] · [[§19 ℝⁿ, C［a,b］, ℓᵖ and Lᵖ]] →

*Stage: norms — Thread: dimension. The first structural difference between finite and infinite dimension.*

The spaces of this chapter are the first infinite-dimensional normed spaces available, so they are the first place where infinite dimension can be seen to make a difference. Here is the most basic such difference. In $\mathbb{R}^n$ a bounded sequence has a convergent subsequence, and this one fact carries much of classical analysis: it is how maxima are shown to be attained, how solutions of equations are extracted from approximating sequences, how limits are produced when no formula for them is available. It fails in every infinite-dimensional normed space, and the failure is not marginal — the closed unit ball, the most basic bounded set there is, is never compact.

## Sequential Compactness

> [!definition] Definition §18.1: Sequentially Compact
> A subset $K$ of a normed linear space (or metric space) $X$ is **sequentially compact**, or here simply **compact**, if every sequence $\{x_n\} \subset K$ has a subsequence $\{x_{n_k}\}$ converging to some $x_0 \in K$.

^def-18-1

> [!remark]- Connections
> - The topological definition: [[§19 Limit Point Compactness#^def-19-3|590 Def. §19.3]].

> [!example] Example §18.1: The Closed Unit Ball in $\mathbb{F}^n$
> In $\mathbb{F}^n$ ($\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$) with any norm, the closed unit ball
>
> $$
> \overline{B_1(0)} = \{ x \in \mathbb{F}^n : \|x\| \le 1 \}
> $$
>
> is compact. Indeed a sequence in it is coordinatewise bounded, so the diagonal extraction used in [[§12 New Normed Spaces from Old#^pf-12-3|Step 5]] of Theorem [[§12 New Normed Spaces from Old#^thm-12-3|§12.3]] — [[Bolzano–Weierstrass Theorem|Bolzano–Weierstrass]] applied $n$ times — produces a subsequence converging coordinatewise, hence in norm, and the limit still satisfies $\|x_0\| \le 1$ by continuity of the norm (Proposition [[§10 Normed Linear Spaces#^prop-10-4|§10.4]]).

^ex-18-1

*Uses:* [[§12 New Normed Spaces from Old#^thm-12-3|§12.3]], [[Bolzano–Weierstrass Theorem|451 §11.5]], [[§10 Normed Linear Spaces#^prop-10-4|§10.4]]

> [!remark]- Connections
> - In $\mathbb{R}^n$ with the Euclidean norm: [[§13 Some Topological Concepts in Metric Spaces#^thm-13-3|451 §13.3]] (Bolzano–Weierstrass in $\mathbb{R}^n$), and closed bounded sets are compact by [[Heine–Borel Theorem|Heine–Borel (590 §18.12)]].

> [!definition] Definition §18.2: Open Set; Open Cover; Compact
> Let $X$ be a normed linear space (or metric space). A subset $U \subset X$ is **open** if every point of $U$ is a metric interior point of $U$ (Definition [[§10 Normed Linear Spaces#^def-10-9|§10.9]]). An **open cover** of $K \subset X$ is a collection of open sets whose union contains $K$. $K$ is **compact** if every open cover of $K$ has a finite subcollection that still covers $K$.

^def-18-2

> [!remark]- Connections
> - Topology: open sets of the [[§12 Metric Topology#^def-12-3|metric topology (590 Def. §12.3)]], covers [[§18 Compact Spaces#^def-18-1|590 Def. §18.1]], compactness [[§18 Compact Spaces#^def-18-2|590 Def. §18.2]].

> [!theorem] Theorem §18.1: Compactness in Metric Spaces
> A subset of a normed linear space (or metric space) is compact if and only if it is sequentially compact.

^thm-18-1

> [!proof]+ Proof
> Not covered in lecture: the question was raised in class and set aside. This is point-set topology; see J. Munkres, *Topology*, [[§19 Limit Point Compactness#^thm-19-4|§28]].

^pf-18-1

*Uses:* [[§19 Limit Point Compactness#^thm-19-4|590 §19.4]]

> [!remark]- Connections
> - Home: [[§19 Limit Point Compactness#^thm-19-4|590 §19.4]] (compact ⇔ limit point compact ⇔ sequentially compact for metrizable spaces).

> [!remark] Remark: Which Compactness
> Only the sequential form is used in these notes, and Theorem [[§18 Compactness and the Unit Ball#^thm-18-1|§18.1]] is not needed for anything that follows; it records that “compact” is unambiguous here.

^rem-18-1

## Riesz's Lemma

Without an inner product there is no notion of perpendicularity, so one cannot ask for a unit vector orthogonal to a subspace. The following lemma is the substitute available in a bare normed space: a unit vector that is at least a fixed distance from the subspace.

> [!theorem] Lemma §18.2: Riesz's Lemma
> Let $(X, \|\cdot\|)$ be a normed linear space and $Y$ a closed proper subspace of $X$. Then there exists $z \in X$ with
>
> $$
> \|z\| = 1 \qquad \text{and} \qquad \operatorname{dist}(z, Y) = \inf_{y \in Y} \|z - y\| \ge \tfrac{1}{2}.
> $$
>
> *Lax: §5.2, Lemma 7*

^lem-18-2

> [!proof]+ Proof
> **Step 1: a point off $Y$, at positive distance.** Since $Y \subsetneq X$, choose $x_0 \in X \setminus Y$ and set
>
> $$
> d = \operatorname{dist}(x_0, Y) = \inf_{y \in Y} \|x_0 - y\|.
> $$
>
> Then $d > 0$. For if $d = 0$, there are $y_n \in Y$ with $\|x_0 - y_n\| \to 0$, i.e. $y_n \to x_0$; since $Y$ is closed (Definition [[§10 Normed Linear Spaces#^def-10-6|§10.6]]) this forces $x_0 \in Y$, contrary to the choice of $x_0$. This is the only place closedness of $Y$ is used, and it is essential.
>
> **Step 2: an almost-minimizing $y_0$.** The infimum $d$ need not be attained, but $2d > d$ is not a lower bound for $\{\|x_0 - y\| : y \in Y\}$, so there is $y_0 \in Y$ with
>
> $$
> d \le a := \|x_0 - y_0\| < 2d.
> $$
>
> (Any factor $>1$ would do here; see Corollary [[§18 Compactness and the Unit Ball#^cor-18-3|§18.3]].) Note $a > 0$.
>
> **Step 3: normalize.** Put
>
> $$
> z = \frac{x_0 - y_0}{\|x_0 - y_0\|} = \frac{x_0 - y_0}{a}, \qquad \text{so } \|z\| = 1
> $$
>
> by homogeneity. For any $y \in Y$,
>
> $$
> z - y = \frac{x_0 - y_0}{a} - y = \frac{1}{a}\bigl( x_0 - (y_0 + a y) \bigr),
> $$
>
> and $y_0 + a y \in Y$ because $Y$ is a subspace. Hence, by homogeneity and the definition of $d$ as an infimum over all of $Y$,
>
> $$
> \|z - y\| = \frac{1}{a}\,\bigl\| x_0 - (y_0 + a y) \bigr\| \ge \frac{d}{a}.
> $$
>
> Taking the infimum over $y \in Y$ and using $a < 2d$,
>
> $$
> \operatorname{dist}(z, Y) \ge \frac{d}{a} > \frac{d}{2d} = \frac{1}{2}.
> $$

^pf-18-2

*Uses:* [[§10 Normed Linear Spaces#^def-10-1|Def. §10.1]], [[§10 Normed Linear Spaces#^def-10-6|Def. §10.6]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]]

![[m556-15-1.svg]]
*The picture drawn in Lecture 6, for $Y$ a line in $\mathbb{R}^2$: $y_0$ is only an almost-closest point, $d \le a = \|x_0 - y_0\| < 2d$, and $z = (x_0 - y_0)/a$ is the unit vector in the same direction. Every point of $Y$ is at distance at least $d/a > \tfrac12$ from $z$; here $z$ lies above the dashed line.*

> [!remark]- Connections
> - In an inner product space the closest point exists ([[§22 Projection and Orthogonal Decomposition#^thm-22-2|§22.2]]) and the unit vector can be taken orthogonal: [[§22 Projection and Orthogonal Decomposition#^thm-22-4|§22.4]], and the remark contrasting the two arguments, [[§22 Projection and Orthogonal Decomposition#^rem-22-6|Remark §22]].

> [!theorem] Corollary §18.3: Riesz's Lemma with Any Constant Below One
> Under the hypotheses of Lemma [[§18 Compactness and the Unit Ball#^lem-18-2|§18.2]], for every $\theta \in (0,1)$ there is $z \in X$ with $\|z\| = 1$ and $\operatorname{dist}(z, Y) \ge \theta$.

^cor-18-3

> [!proof]+ Proof
> Repeat the proof of Lemma [[§18 Compactness and the Unit Ball#^lem-18-2|§18.2]], choosing $y_0$ in Step 2 with $d \le a < d/\theta$, which is possible because $d/\theta > d$. Step 3 then gives $\operatorname{dist}(z, Y) \ge d/a > \theta$. (Not covered in lecture.)

^pf-18-3

*Uses:* [[§18 Compactness and the Unit Ball#^lem-18-2|§18.2]]

> [!theorem] Proposition §18.4: The Constant $\theta = 1$ Cannot Be Attained
> Let $X = \{ f \in C[0,1] : f(0) = 0 \}$ with $\|f\| = \max_{[0,1]} |f|$, and
>
> $$
> Y = \Bigl\{ f \in X : \int_0^1 f(t)\,dt = 0 \Bigr\}.
> $$
>
> Then $X$ is a Banach space, $Y$ is a closed proper subspace of $X$, and
>
> $$
> \operatorname{dist}(f, Y) < 1 \qquad \text{for every } f \in X \text{ with } \|f\| = 1 .
> $$
>
> In particular Corollary [[§18 Compactness and the Unit Ball#^cor-18-3|§18.3]] fails for $\theta = 1$.

^prop-18-4

> [!proof]+ Proof
> Write $\varphi(h) = \int_0^1 h(t)\,dt$ for $h \in C[0,1]$. Then $\varphi$ is linear, and $|\varphi(h)| \le \int_0^1 |h| \le \|h\|$.
>
> **Step 1: $X$ is a Banach space.** $X$ is a linear subspace of the Banach space $(C[0,1], \|\cdot\|_\infty)$ (Theorem [[§11 Completeness#^thm-11-1|§11.1]]), and it is closed: if $f_n \in X$ and $f_n \to f$ uniformly, then $f(0) = \lim_n f_n(0) = 0$. A Cauchy sequence in $X$ is Cauchy in $C[0,1]$, so it converges there, and by closedness its limit lies in $X$. Hence $X$ is complete.
>
> **Step 2: $Y$ is a closed proper subspace.** $Y$ is a subspace by linearity of $\varphi$. If $f_n \in Y$ and $f_n \to f \in X$, then $|\varphi(f)| = |\varphi(f - f_n)| \le \|f - f_n\| \to 0$, so $\varphi(f) = 0$ and $f \in Y$; thus $Y$ is closed. The function $g(t) = t$ lies in $X$ and has $\varphi(g) = \frac12 \neq 0$, so $Y \neq X$.
>
> **Step 3: an upper bound for the distance.** For $n \ge 1$ let $g_n(t) = \min\{nt, 1\}$. Then $g_n \in X$, $\|g_n\| = 1$, and
>
> $$
> \varphi(g_n) = \int_0^{1/n} nt\,dt + \int_{1/n}^1 dt = \frac{1}{2n} + 1 - \frac{1}{n} = 1 - \frac{1}{2n} > 0 .
> $$
>
> Given $f \in X$, put
>
> $$
> y_n = f - \frac{\varphi(f)}{\varphi(g_n)}\, g_n .
> $$
>
> Then $y_n \in X$ and $\varphi(y_n) = \varphi(f) - \varphi(f) = 0$, so $y_n \in Y$. Hence
>
> $$
> \operatorname{dist}(f, Y) \le \|f - y_n\| = \frac{|\varphi(f)|}{\varphi(g_n)}\,\|g_n\| = \frac{|\varphi(f)|}{1 - \frac{1}{2n}} .
> $$
>
> **Step 4: $|\varphi(f)| < 1$ for unit vectors.** Let $f \in X$ with $\|f\| = 1$. Since $f$ is continuous and $f(0) = 0$, there is $\delta \in (0,1]$ with $|f(t)| \le \frac12$ for $0 \le t \le \delta$. Using $|f| \le 1$ on $[\delta, 1]$,
>
> $$
> |\varphi(f)| \le \int_0^\delta |f| + \int_\delta^1 |f| \le \frac{\delta}{2} + (1 - \delta) = 1 - \frac{\delta}{2} .
> $$
>
> **Step 5: conclusion.** Choose $n > 1/\delta$, so that $1 - \frac{1}{2n} > 1 - \frac{\delta}{2}$. By Steps 3 and 4,
>
> $$
> \operatorname{dist}(f, Y) \le \frac{1 - \delta/2}{1 - 1/(2n)} < 1 .
> $$

^pf-18-4

*Uses:* [[§11 Completeness#^thm-11-1|§11.1]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]], [[§10 Normed Linear Spaces#^def-10-6|Def. §10.6]], [[§10 Normed Linear Spaces#^def-10-5|Def. §10.5]], [[§11 Completeness#^def-11-2|Def. §11.2]], [[§33 Properties of the Riemann Integral#^thm-33-2|451 §33.2]], [[§33 Properties of the Riemann Integral#^thm-33-3|451 §33.3]], [[§33 Properties of the Riemann Integral#^thm-33-4|451 §33.4]], [[§33 Properties of the Riemann Integral#^thm-33-5|451 §33.5]]

![[m556-15-2.svg]]
*Why the constant $1$ is not attained. A unit vector $f$ of $X$ (blue) starts at $f(0) = 0$, so it stays below $\tfrac12$ on some $[0, \delta]$, and $\int_0^1 f$ falls short of $1$ by at least the red area $\delta/2$ (Step 4). The ramps $g_n = \min\{nt, 1\}$ (gray) have $\int_0^1 g_n = 1 - \tfrac1{2n}$, which beats $1 - \tfrac\delta2$ once $\tfrac1n < \delta$; subtracting the right multiple of $g_n$ moves $f$ into $Y$ at a cost $|\int_0^1 f| / \int_0^1 g_n < 1$ (Steps 3 and 5).*

> [!remark] Remark: On the Constant
> Since $0 \in Y$, always $\operatorname{dist}(z, Y) \le \|z - 0\| = 1$ for a unit vector $z$. So Corollary [[§18 Compactness and the Unit Ball#^cor-18-3|§18.3]] says $\sup_{\|z\| = 1} \operatorname{dist}(z, Y) = 1$ for every closed proper subspace, and Proposition [[§18 Compactness and the Unit Ball#^prop-18-4|§18.4]] says the supremum need not be attained. The mechanism is visible in Steps 3–4: letting $n \to \infty$ in Step 3 gives $\operatorname{dist}(f, Y) \le |\int_0^1 f|$, so a unit vector at distance $1$ from $Y$ would need $|\int_0^1 f| = 1 = \max |f|$, which forces $|f| \equiv 1$ and is ruled out by $f(0) = 0$.
>
> By contrast, in an inner product space the constant $1$ is attained as soon as a unit vector $z$ orthogonal to $Y$ is available (for a closed proper subspace of a Hilbert space, Theorem [[§22 Projection and Orthogonal Decomposition#^thm-22-4|§22.4]] provides one: take $x_0 \notin Y$ and normalize its $Y^\perp$-component): then $\|z - y\|^2 = \|z\|^2 - (z,y) - (y,z) + \|y\|^2 = 1 + \|y\|^2 \ge 1$ for every $y \in Y$. In general the picture Wu drew is the right one: $z$ is a unit vector pointing “away from” $Y$, and if a first attempt sits too close to $Y$ one slides along until it does not. (Not covered in lecture.)

^rem-18-2

## The Theorem

> [!theorem] Theorem §18.5: The Unit Ball of an Infinite-Dimensional Space is Not Compact
> Let $X$ be an infinite-dimensional normed linear space. Then the closed unit ball
>
> $$
> \overline{B_1(0)} = \{ x \in X : \|x\| \le 1 \}
> $$
>
> is not compact.
>
> *Lax: §5.2, Thm 6*

^thm-18-5

> [!proof]+ Proof
> It suffices to construct a sequence $\{x_n\} \subset X$ with
>
> $$
> \|x_n\| = 1 \text{ for all } n, \qquad \|x_i - x_j\| \ge \tfrac{1}{2} \text{ for all } i \ne j.
> $$
>
> Such a sequence lies in $\overline{B_1(0)}$ and no subsequence of it is Cauchy — the mutual distances never drop below $\tfrac12$ — so no subsequence converges.
>
> The construction is by induction, using Riesz's lemma at each step.
>
> *Base step.* Choose any $x_1 \in X$ with $\|x_1\| = 1$ (possible since $X \ne \{0\}$: take any nonzero vector and divide by its norm).
>
> *Induction step.* Suppose $x_1, \ldots, x_m$ have been constructed with $\|x_i\| = 1$ for $1 \le i \le m$ and $\operatorname{dist}(x_j, Y_{j-1}) \ge \tfrac12$ for $2 \le j \le m$, where $Y_{j-1} = \operatorname{span}\{x_1, \ldots, x_{j-1}\}$. Put
>
> $$
> Y_m = \operatorname{span}\{x_1, \ldots, x_m\}.
> $$
>
> Then:
> - $Y_m$ is *closed*, because it is finite-dimensional (Corollary [[§12 New Normed Spaces from Old#^cor-12-5|§12.5]]);
> - $Y_m$ is a *proper* subspace of $X$, because $\dim Y_m \le m < \infty$ while $X$ is infinite-dimensional, so $X$ cannot equal the span of finitely many vectors.
>
> Riesz's lemma (Lemma [[§18 Compactness and the Unit Ball#^lem-18-2|§18.2]]) applied to $Y_m \subsetneq X$ therefore produces $x_{m+1} \in X$ with $\|x_{m+1}\| = 1$ and $\operatorname{dist}(x_{m+1}, Y_m) \ge \tfrac12$.
>
> *Conclusion.* This produces $\{x_m\}_{m=1}^\infty \subset X$ with $\|x_m\| = 1$ for all $m$, and for $j < m$ we have $x_j \in Y_{m-1}$, hence
>
> $$
> \|x_m - x_j\| \ge \operatorname{dist}(x_m, Y_{m-1}) \ge \tfrac{1}{2}.
> $$

^pf-18-5

*Uses:* [[§18 Compactness and the Unit Ball#^def-18-1|Def. §18.1]], [[§10 Normed Linear Spaces#^prop-10-5|§10.5]], [[§1 Linear Spaces#^def-1-5|Def. §1.5]], [[§12 New Normed Spaces from Old#^cor-12-5|§12.5]], [[§18 Compactness and the Unit Ball#^lem-18-2|§18.2]]

> [!remark]- Connections
> - The finite-dimensional contrast: [[§18 Compactness and the Unit Ball#^ex-18-1|Ex. §18.1]], resting on [[Heine–Borel Theorem|Heine–Borel]] / [[Bolzano–Weierstrass Theorem|Bolzano–Weierstrass]].
> - Hence no infinite-dimensional normed space is locally compact ([[§20 Local Compactness#^def-20-1|590 Def. §20.1]]), since a compact neighborhood of 0 would contain a closed ball; compare ℝ^ω, [[§20 Local Compactness#^ex-20-5|590 Ex. §20.5]].

> [!remark] Remark: Where Infinite-Dimensionality Enters
> This was asked in lecture. The hypothesis is used at exactly one point: to know that $Y_m = \operatorname{span}\{x_1, \ldots, x_m\}$ is a *proper* subspace, so that Riesz's lemma applies and the construction can continue. In a finite-dimensional space the process halts — at some stage $Y_m = X$, and there is no vector left at distance $\tfrac12$ from everything already chosen. Infinite-dimensionality is what guarantees a genuinely new direction at every step. The other hypothesis doing work is Corollary [[§12 New Normed Spaces from Old#^cor-12-5|§12.5]]: without knowing $Y_m$ closed, Riesz's lemma would not apply either.

^rem-18-3

> [!example] Example §18.2: The Separated Sequence in $\ell^p$
> For $\ell^p$ with $1 \le p < \infty$ the construction can be written down without any induction. Let $e_j = (0, \ldots, 0, 1, 0, \ldots)$ with the $1$ in the $j$-th place. Then $\|e_j\|_p = 1$, and for $i \ne j$ the sequence $e_i - e_j$ has exactly two nonzero entries, $\pm 1$, so
>
> $$
> \|e_i - e_j\|_p = \bigl(1^p + 1^p\bigr)^{1/p} = 2^{1/p} > 1 > \tfrac12.
> $$
>
> Hence $\{e_j\}$ has no convergent subsequence, and the closed unit ball of $\ell^p$ is not compact. (In $\ell^\infty$, $\|e_i - e_j\|_\infty = 1$.) The theorem says that every infinite-dimensional normed space contains a sequence behaving like this one, even when no basis is available to write it down.

^ex-18-2

*Uses:* [[§16 Minkowski's Inequality and the Spaces ℓᵖ#^def-16-1|Def. §16.1]], [[§10 Normed Linear Spaces#^prop-10-5|§10.5]], [[§18 Compactness and the Unit Ball#^def-18-1|Def. §18.1]]

> [!remark] Remark: Why This Matters: Toward Weak Convergence
> Compactness is what allows a limit to be produced when no formula for it exists. The model application: to solve an equation $P(x) = 1$ one constructs approximate solutions, $P(x_1) \approx 1$, $P(x_2)$ closer, and so on, with $\|x_j\| \le M$ for all $j$; in finite dimensions the bounded sequence $\{x_j\}$ has a convergent subsequence, and its limit solves the equation provided $P$ is continuous. Theorem [[§18 Compactness and the Unit Ball#^thm-18-5|§18.5]] says this move is unavailable in the function spaces the course is about — $L^p$, $\ell^p$, $C[a,b]$ are all infinite-dimensional.
>
> The response is not to give up on compactness but to weaken the notion of convergence until it returns. A bounded sequence in a suitable infinite-dimensional space does have a subsequence converging *weakly*, and the closed unit ball is compact in a weaker topology. This is the direction the course takes later; the present theorem is what makes it necessary.

^rem-18-4
