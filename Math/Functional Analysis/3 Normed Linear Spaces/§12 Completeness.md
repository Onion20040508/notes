---
type: section
subject: "[[Functional Analysis]]"
chapter: 3
section: 12
tags: [functional-analysis, math556]
---
← [[§11 Normed Linear Spaces]] · ↑ [[· 3 Normed Linear Spaces]] · [[§13 The Completion of a Normed Space]] →

*Stage: norms — Thread: completeness. Cauchy sequences, Banach spaces, and the completion.*

## Complete Spaces and Banach Spaces

> [!definition] Definition §12.1: Complete Metric Space
> A metric space $(M, d)$ is **complete** if every Cauchy sequence in $M$ converges to a point of $M$.

^def-12-1

> [!remark]- Connections
> - Home of the definition: [[§13 Some Topological Concepts in Metric Spaces#^def-13-4|451 Def. §13.4]]; $\mathbb{R}^n$ is complete: [[§13 Some Topological Concepts in Metric Spaces#^thm-13-2|451 §13.2]].

> [!definition] Definition §12.2: Banach Space
> A complete normed linear space is called a **Banach space**.
>
> *Lax: §5.1, definition of Banach space*

^def-12-2

> [!remark]- Connections
> - In 551: [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-5|551 Def. §34.5]], with examples [[§34 Normed Linear Spaces and Lᵖ Spaces#^ex-34-4|551 Ex. §34.4]] and the [[Riesz–Fischer Theorem]] ($L^p$ is Banach).

> [!theorem] Theorem §12.1: $C[a,b]$ with the Supremum Norm is a Banach Space
> Let $X = C([a,b])$ be the set of continuous functions $f : [a,b] \to \mathbb{F}$, with pointwise operations and
>
> $$
> \|f\|_\infty = \max_{t \in [a,b]} |f(t)|.
> $$
>
> Then $(X, \|\cdot\|_\infty)$ is a Banach space.
>
> *Source: HW2, Problem 1*
> *Lax: §5.1, examples (c)–(e)*

^thm-12-1

> [!proof]+ Proof
> (HW2, Problem 1.) Throughout, $\mathbb{F}$ denotes the scalar field, $\mathbb{R}$ or $\mathbb{C}$, and $|\cdot|$ its absolute value. We show in turn that $X$ is a linear space, that $\|\cdot\|_\infty$ is a norm on $X$, and that $(X, \|\cdot\|_\infty)$ is complete.
>
> **Part 1: $X$ is a linear space.** Define addition and scalar multiplication pointwise: for $f, g \in X$ and $a \in \mathbb{F}$,
>
> $$
> (f + g)(x) = f(x) + g(x), \qquad (af)(x) = a\,f(x) \qquad (x \in [a,b]).
> $$
>
> These are well defined as operations on $X$: a sum of continuous functions is continuous and a scalar multiple of a continuous function is continuous, so $f + g \in X$ and $af \in X$. Let $f, g, h \in X$ and $a, k \in \mathbb{F}$; each identity below is proved by evaluating at an arbitrary $x \in [a,b]$, where it reduces to the corresponding identity in $\mathbb{F}$.
>
> *Commutativity:* $(f + g)(x) = f(x) + g(x) = g(x) + f(x) = (g + f)(x)$, so $f + g = g + f$.
>
> *Associativity:* $\bigl((f + g) + h\bigr)(x) = \bigl(f(x) + g(x)\bigr) + h(x) = f(x) + \bigl(g(x) + h(x)\bigr) = \bigl(f + (g + h)\bigr)(x)$.
>
> *Additive identity:* the constant function $Z(x) = 0$ is continuous, so $Z \in X$, and $(f + Z)(x) = f(x) + 0 = f(x) = 0 + f(x) = (Z + f)(x)$.
>
> *Additive inverse:* $(-f)(x) = -f(x)$ defines $-f \in X$, and $\bigl(f + (-f)\bigr)(x) = f(x) - f(x) = 0 = Z(x) = -f(x) + f(x) = \bigl((-f) + f\bigr)(x)$.
>
> *Compatibility of scalar multiplication:* $\bigl(k(af)\bigr)(x) = k\bigl(a f(x)\bigr) = (ka) f(x) = \bigl((ka)f\bigr)(x)$.
>
> *Distributivity over vector addition:* $\bigl(k(f + g)\bigr)(x) = k\bigl(f(x) + g(x)\bigr) = k f(x) + k g(x) = (kf + kg)(x)$.
>
> *Distributivity over scalar addition:* $\bigl((a + k)f\bigr)(x) = (a + k)f(x) = a f(x) + k f(x) = (af + kf)(x)$.
>
> *Unit:* $(1f)(x) = 1 \cdot f(x) = f(x)$.
>
> Hence $X$ is a linear space over $\mathbb{F}$.
>
> **Part 2: $\|\cdot\|_\infty$ is a norm on $X$.**
>
> *The maximum is attained.* Let $f \in X$. Since $f$ and $|\cdot|$ are continuous, $|f| : [a,b] \to \mathbb{R}$ is continuous, and a continuous real-valued function on the closed bounded interval $[a,b]$ attains its maximum. Hence there is $t_0 \in [a,b]$ with $|f(t_0)| \ge |f(t)|$ for all $t$, so $\|f\|_\infty = |f(t_0)|$ is a well-defined real number, and $|f(t)| \le \|f\|_\infty$ for every $t \in [a,b]$.
>
> *Positivity.* Since $|f(t)| \ge 0$ for every $t$, $\|f\|_\infty \ge 0$. If $\|f\|_\infty = 0$, then $0 \le |f(t)| \le \|f\|_\infty = 0$ for every $t$, so $f(t) = 0 = Z(t)$; hence $f = Z$.
>
> *Homogeneity.* Let $k \in \mathbb{F}$ and let $t_0$ be as above for $f$. For every $t$, $|(kf)(t)| = |k|\,|f(t)| \le |k|\,|f(t_0)| = |(kf)(t_0)|$, so the maximum of $|kf|$ is attained at $t_0$ as well, and $\|kf\|_\infty = |k|\,|f(t_0)| = |k|\,\|f\|_\infty$.
>
> *Triangle inequality.* Let $t_0$ be a point where $|f + g|$ attains its maximum. Then
>
> $$
> \|f + g\|_\infty = |f(t_0) + g(t_0)| \le |f(t_0)| + |g(t_0)| \le \|f\|_\infty + \|g\|_\infty,
> $$
>
> the first inequality being the triangle inequality in $\mathbb{F}$ and the second the bound $|f(t)| \le \|f\|_\infty$, $|g(t)| \le \|g\|_\infty$.
>
> **Part 3: completeness.** Let $\{f_n\}$ be Cauchy in $X$: for every $\varepsilon > 0$ there is $N$ with $\|f_m - f_k\|_\infty < \varepsilon$ for all $m, k \ge N$. We must produce $f \in X$ with $\|f_n - f\|_\infty \to 0$.
>
> *Step 1: pointwise convergence.* Fix $t_0 \in [a,b]$. For all $m, k$,
>
> $$
> 0 \le |f_m(t_0) - f_k(t_0)| = |(f_m - f_k)(t_0)| \le \|f_m - f_k\|_\infty .
> $$
>
> So $\{f_n(t_0)\}$ is a Cauchy sequence of scalars; as $\mathbb{F}$ is complete, it converges. Define $f(t_0) = \lim_n f_n(t_0)$. Doing this for every $t_0$ defines $f : [a,b] \to \mathbb{F}$ with $f_n(t) \to f(t)$ for each $t$.
>
> *Step 2: the convergence is uniform.* Let $\varepsilon > 0$ and choose $N$ with
>
> $$
> |f_m(t) - f_k(t)| \le \|f_m - f_k\|_\infty < \frac{\varepsilon}{2} \qquad \text{for all } m, k > N \text{ and all } t \in [a,b];
> $$
>
> $N$ was obtained from the norm estimate alone, so it does not depend on $t$. Fix $k > N$ and $t \in [a,b]$, and consider $S_m(t) = |f_m(t) - f_k(t)|$ for $m > N$; each is at most $\varepsilon/2$. By the reverse triangle inequality in $\mathbb{F}$,
>
> $$
> \Bigl|\, |f_m(t) - f_k(t)| - |f(t) - f_k(t)| \,\Bigr| \le |f_m(t) - f(t)| \xrightarrow[m \to \infty]{} 0,
> $$
>
> so $S_m(t) \to |f(t) - f_k(t)|$. A limit preserves non-strict inequalities, so $|f(t) - f_k(t)| \le \varepsilon/2 < \varepsilon$. Here $N$ was chosen before $t$ and $k > N$ was arbitrary: for every $\varepsilon > 0$ there is $N$, independent of $t$, with $|f_k(t) - f(t)| < \varepsilon$ for all $k > N$ and all $t$. That is, $f_n \to f$ uniformly on $[a,b]$.
>
> *Step 3: $f$ is continuous.* Fix $x \in [a,b]$ and $\varepsilon > 0$. By Step 2 there is $N$, independent of the point, with $|f_n(t) - f(t)| < \varepsilon/3$ for all $n > N$ and all $t$. Fix one such $n$. Since $f_n$ is continuous at $x$, there is $\delta > 0$ with $|f_n(x) - f_n(y)| < \varepsilon/3$ whenever $|x - y| < \delta$. For such $y$,
>
> $$\begin{aligned}
> |f(x) - f(y)| &\le |f(x) - f_n(x)| + |f_n(x) - f_n(y)| + |f_n(y) - f(y)| < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon,
> \end{aligned}$$
>
> the first and third terms bounded at the two points $x$ and $y$ with the *same* index $n$, which is legitimate because $N$ does not depend on the point. Hence $f$ is continuous at every $x$, i.e. $f \in X$.
>
> *Step 4: $\|f_n - f\|_\infty \to 0$.* Let $\varepsilon > 0$ and $N$ as in Step 2, so $|f_m(t) - f(t)| < \varepsilon$ for all $m > N$ and all $t$. Fix $m > N$. By Step 3, $f_m - f \in X$, so by Part 2 its modulus attains a maximum at some $t_0$, and
>
> $$
> \|f_m - f\|_\infty = |f_m(t_0) - f(t_0)| < \varepsilon .
> $$
>
> Hence $\|f_n - f\|_\infty \to 0$, and every Cauchy sequence in $X$ converges in $X$. With Parts 1 and 2, $(X, \|\cdot\|_\infty)$ is a Banach space.

^pf-12-1

*Uses:* [[§1 Linear Spaces#^def-1-1|Def. §1.1]], [[§11 Normed Linear Spaces#^def-11-1|Def. §11.1]], [[§11 Normed Linear Spaces#^def-11-5|Def. §11.5]], [[§12 Completeness#^def-12-2|Def. §12.2]], [[Extreme Value Theorem|451 Extreme Value Theorem]], [[§10a Cauchy Sequences#^thm-10a-3|451 §10a.3]] (completeness of the scalars)

> [!remark]- Connections
> - Steps 2–3 re-prove the 451 results on uniform convergence: [[§24 Uniform Convergence#^thm-24-1|451 §24.1]] (supremum criterion), [[§24 Uniform Convergence#^thm-24-2|451 §24.2]] (uniform limits preserve continuity).
> - The pattern of the proof: [[Functional Analysis Problem-Solving Techniques#^rem-t5|Technique 5]].
> - Used in ODEs: the Picard iterates for $y' = f(t, y)$ form a Cauchy sequence in $C[-h, h]$ with the supremum norm, and their limit is the solution, [[§14 The Existence and Uniqueness Theorem#^thm-14-7|331 Thm. §14.7]].

> [!remark] Remark
> The proof is the “candidate, then close” pattern ([[Functional Analysis Problem-Solving Techniques#^rem-t5|Technique 5]]) in its simplest form, with one extra step that has no analogue in $\ell^p$ ([[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-5|§18.5]]): the candidate must be shown to lie in the space, and here that is a genuine theorem (a uniform limit of continuous functions is continuous), not a bookkeeping check. The $3\varepsilon$ argument in Step 3 is exactly where uniformity, not just pointwise convergence, is used.

^rem-12-1

> [!remark] Remark
> The hierarchy so far: a linear space has only algebra; a normed linear space adds length and hence topology; a Banach space adds the guarantee that limits exist. Most of the course is about Banach spaces, because that is where analysis — limits of sequences, sums of series, solutions of equations obtained as limits of approximations — can actually be carried out.

^rem-12-2

> [!theorem] Lemma §12.2: Complete Subsets are Closed
> Let $S$ be a subset of a normed linear space (or metric space) $X$ which is complete with the restricted norm (metric). Then $S$ is closed in $X$.

^lem-12-2

> [!proof]+ Proof
> (Not covered in lecture.) Let $s_n \in S$ with $s_n \to x \in X$. By Proposition [[§11 Normed Linear Spaces#^prop-11-5|§11.5]](b), $\{s_n\}$ is Cauchy, so by completeness of $S$ it converges to some $s \in S$. By uniqueness of limits (Proposition [[§11 Normed Linear Spaces#^prop-11-5|§11.5]](a)), $x = s \in S$.

^pf-12-2

*Uses:* [[§11 Normed Linear Spaces#^prop-11-5|§11.5]], [[§11 Normed Linear Spaces#^def-11-6|Def. §11.6]], [[§12 Completeness#^def-12-1|Def. §12.1]]

## Completion of a Metric Space

A metric space that is not complete can be enlarged to one that is, by adjoining the missing limits. Since a missing limit is not an element of $M$, it is represented by the Cauchy sequences that “should” converge to it.

> [!definition] Definition §12.3: Equivalent Cauchy Sequences
> Two Cauchy sequences $\{x_n\}, \{y_n\}$ in a metric space $(M, d)$ are **equivalent**, written $\{x_n\} \sim \{y_n\}$, if
>
> $$
> \lim_{n \to \infty} d(x_n, y_n) = 0.
> $$

^def-12-3

Note that $d(x_n, y_n)$ makes sense whether or not either sequence has a limit in $M$: both terms lie in $M$. The relation says the two sequences are heading for the same place. If one of them converges in $M$, so does the other, to the same limit.

> [!definition] Definition §12.4: Completion
> The **completion** $\overline{M}$ of a metric space $M$ is the set of equivalence classes of Cauchy sequences in $M$ under $\sim$:
>
> $$
> \overline{M} = \bigl\{ [\{x_n\}] : \{x_n\} \text{ Cauchy in } M \bigr\}.
> $$
>
> An element $x \in M$ is identified with the class of the constant sequence $(x, x, x, \ldots)$, which is Cauchy with limit $x$; in this way $M \subset \overline{M}$.
>
> *Lax: §5.1, completion of a metric space*

^def-12-4

> [!remark]- Connections
> - The model: $\mathbb{R}$ as classes of Cauchy sequences of rationals, [[§10a Cauchy Sequences#^rem-10a-4|451 Remark (Cauchy sequences and the construction of the reals)]], carried out with rational tolerances in [[§6★ ℝ from Cauchy Sequences of Rationals|451 §6★]] (why rational: [[§6★ ℝ from Cauchy Sequences of Rationals#^rem-6s-2|451 §6★, order of logic]]).
> - For normed spaces: [[§13 The Completion of a Normed Space#^thm-13-1|§13.1]]; concrete completions: [[§13 The Completion of a Normed Space#^prop-13-2|§13.2]], [[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8|§19.8]].

> [!remark] Remark: Why Classes, and Why the Objects Look Different
> Two points were raised in lecture. First, why equivalence classes: a point $x \in M$ is the limit of many Cauchy sequences (on the real line, $(x, x, \ldots)$ and $(x + 1/n)$ both converge to $x$), and different sequences with the same destination must not be counted as different elements of $\overline{M}$. Second, the elements of $\overline{M}$ are sets of sequences, not points of $M$, so how is $M$ a subset? By the identification $x \leftrightarrow [(x, x, \ldots)]$, which is one-to-one; $M$ is not literally contained in $\overline{M}$ but is embedded in it. This is the same kind of identification as $\mathbb{R} \subset \mathbb{R} \oplus \mathbb{R}^2 = \mathbb{R}^3$ ([[§1 Linear Spaces#^ex-1-2|Ex. §1.2]]).

^rem-12-3

![[m556-9-2.svg]]
*Equivalent Cauchy sequences in the open disk $M$ of [[§12 Completeness#^ex-12-1|Ex. §12.1]]: $x_n$ (blue dots) and $y_n$ (blue squares) both head for the boundary point $p \notin M$, and $d(x_n, y_n) \to 0$ (dotted), so they are one element $[\{x_n\}] = [\{y_n\}]$ of $\overline{M}$, which plays the role of $p$. The sequence $z_n$ (red), heading for $q$, is a different class; a point $x \in M$ is the class of its constant sequence.*

> [!theorem] Proposition §12.3: The Completion is a Complete Metric Space, and $M$ is Dense in It
> Let $(M, d)$ be a metric space. For Cauchy sequences $\{x_n\}, \{y_n\}$ in $M$ put
>
> $$
> \bar d\bigl([\{x_n\}], [\{y_n\}]\bigr) := \lim_{n \to \infty} d(x_n, y_n).
> $$
>
> - (a) The limit exists and depends only on the classes, and $\bar d$ is a metric on $\overline{M}$.
> - (b) $\bar d(x, y) = d(x, y)$ for $x, y \in M$ (identified with constant sequences), so $M \subset \overline{M}$ isometrically.
> - (c) $M$ is dense in $\overline{M}$: if $\xi = [\{x_n\}]$, then $x_k \to \xi$ in $\overline{M}$ as $k \to \infty$.
> - (d) $(\overline{M}, \bar d)$ is complete.

^prop-12-3

> [!proof]+ Proof
> (Not covered in lecture; added because [[§12 Completeness#^ex-12-1|Example §12.1]], [[§13 The Completion of a Normed Space#^rem-13-5|Remark “How Do We Know We Have Not Added Too Much?”]] and the normed case below rely on these facts.)
>
> (a) By the triangle inequality, applied twice, $|d(x_n, y_n) - d(x_m, y_m)| \le d(x_n, x_m) + d(y_n, y_m)$, so $\{d(x_n, y_n)\}$ is a Cauchy sequence of real numbers and converges. If $\{x_n\} \sim \{x_n'\}$ and $\{y_n\} \sim \{y_n'\}$, the same estimate gives $|d(x_n, y_n) - d(x_n', y_n')| \le d(x_n, x_n') + d(y_n, y_n') \to 0$, so the limit depends only on the classes. Symmetry and the triangle inequality hold termwise and pass to the limit, and $\bar d \ge 0$. Finally $\bar d([\{x_n\}], [\{y_n\}]) = 0$ iff $d(x_n, y_n) \to 0$ iff $\{x_n\} \sim \{y_n\}$ iff the two classes are equal.
>
> (b) For constant sequences, $\bar d(x, y) = \lim_n d(x, y) = d(x, y)$.
>
> (c) Let $\varepsilon > 0$ and choose $N$ with $d(x_n, x_m) < \varepsilon$ for all $n, m \ge N$. For $k \ge N$, $\bar d(x_k, \xi) = \lim_n d(x_k, x_n) \le \varepsilon$. Hence $x_k \to \xi$.
>
> (d) Let $\{\xi_m\}$ be a Cauchy sequence in $\overline{M}$. By (c) there are $z_m \in M$ with $\bar d(z_m, \xi_m) < 1/m$. By (b) and the triangle inequality,
>
> $$
> d(z_m, z_k) = \bar d(z_m, z_k) \le \frac{1}{m} + \bar d(\xi_m, \xi_k) + \frac{1}{k},
> $$
>
> so $\{z_m\}$ is Cauchy in $M$; let $\xi = [\{z_m\}] \in \overline{M}$. Then $\bar d(\xi_m, \xi) \le 1/m + \bar d(z_m, \xi)$, and $\bar d(z_m, \xi) \to 0$ as $m \to \infty$ by (c) applied to the representative $\{z_k\}$ of $\xi$. Hence $\xi_m \to \xi$.
>
> For a normed linear space $X$ with the norm of Theorem [[§13 The Completion of a Normed Space#^thm-13-1|§13.1]], $\bigl\| [\{x_n\}] - [\{y_n\}] \bigr\|_{\overline{X}} = \lim_n \|x_n - y_n\| = \bar d\bigl([\{x_n\}], [\{y_n\}]\bigr)$ for the metric $d(x, y) = \|x - y\|$ of $X$, so (c) says that $X$ is dense in $\overline{X}$.

^pf-12-3

*Uses:* [[§12 Completeness#^def-12-3|Def. §12.3]], [[§12 Completeness#^def-12-4|Def. §12.4]], [[§11 Normed Linear Spaces#^def-11-3|Def. §11.3]], [[§10a Cauchy Sequences#^thm-10a-3|451 §10a.3]], [[§13 The Completion of a Normed Space#^thm-13-1|§13.1]]

> [!remark]- Connections
> - The same construction one level down: ℝ as Cauchy classes of ℚ ([[§10a Cauchy Sequences#^rem-10a-4|451 Remark §10.4]]); (c) and (d) for $M = \mathbb{Q}$ are [[§6★ ℝ from Cauchy Sequences of Rationals#^cor-6s-9|451 §6★.9]] and [[§6★ ℝ from Cauchy Sequences of Rationals#^thm-6s-10|451 §6★.10]].
> - The normed version, where the linear structure and the norm are added: Theorem [[§13 The Completion of a Normed Space#^thm-13-1|§13.1]]; uniqueness: Corollary [[§13 The Completion of a Normed Space#^cor-13-3|§13.3]].

> [!example] Example §12.1: Completions of Subsets of $\mathbb{R}^n$
> For subsets of $\mathbb{R}^n$ with the usual metric, completion is closure:
> - $M = (0, 1)$ with $d(x,y) = |x - y|$: $\overline{M} = [0, 1]$. The missing limits are the endpoints, each the limit of Cauchy sequences such as $(1/n)$ and $(1 - 1/n)$.
> - $M = B_1(0) = \{ x \in \mathbb{R}^2 : \|x\| < 1 \}$, the open unit disk: $\overline{M} = \{ \|x\| \le 1 \}$, the closed disk.
>
> In general the completion is abstract and cannot be drawn; the picture to keep is “add the boundary.”
>
> ![[m556-9-1.svg]]
> *In $M = (0,1)$ the Cauchy sequence $x_n = 1/n$ ($n \ge 2$) heads for $0$, which is not in $M$; the completion supplies the missing point.*

^ex-12-1

## Completion of a Normed Linear Space

For a normed linear space $X$, the completion $\overline{X}$ as a metric space should again be a normed linear space, with $X$ sitting inside it as a subspace and with the original norm. The natural candidate for the norm of a class is the limit of the norms of a representative.

> [!theorem] Theorem §13.1: The Completion of a Normed Space is a Banach Space
> Let $(X, \|\cdot\|)$ be a normed linear space and $\overline{X}$ its completion. For a Cauchy sequence $\{x_n\}$ in $X$, write $[\{x_n\}] \in \overline{X}$ for its class, and define
>
> $$
> \bigl\| [\{x_n\}] \bigr\| := \lim_{n \to \infty} \|x_n\|.
> $$
>
> Then $\overline{X}$ is a linear space, this is a well-defined norm on it, $\|[(x, x, \ldots)]\| = \|x\|$ for $x \in X$, and $(\overline{X}, \|\cdot\|)$ is complete.
>
> *Source: HW2, Problem 3*
> *Lax: §5.1, Thm 3*

^thm-13-1

> [!remark] Note: Notation for the Proof
> The norm of $X$ is written $\|\cdot\|$ and the candidate norm on $\overline{X}$ is written $\|\cdot\|_{\overline{X}}$. A sequence in $\overline{X}$ is a sequence of classes; its $m$-th term is written $[\{x^{(m)}_n\}_n]$, where $\{x^{(m)}_n\}_n$ is a Cauchy sequence in $X$ (superscript: which class; subscript: which term of the representative).

^rem-13-1

> [!proof]+ Proof
> (HW2, Problem 3.) Throughout, $\{x_n\}$ denotes a Cauchy sequence in $(X, \|\cdot\|)$ and $[\{x_n\}]$ its class in $\overline{X}$; two Cauchy sequences are equivalent iff $\lim_n \|x_n - y_n\| = 0$.
>
> **Step 1: the limit $\lim_n \|x_n\|$ exists.** For all $m, k$, the reverse triangle inequality (Lemma [[§11 Normed Linear Spaces#^lem-11-3|§11.3]]) gives $\bigl|\,\|x_m\| - \|x_k\|\,\bigr| \le \|x_m - x_k\|$. Given $\varepsilon > 0$, choose $N$ with $\|x_m - x_k\| < \varepsilon$ for all $m, k > N$; then $\bigl|\,\|x_m\| - \|x_k\|\,\bigr| < \varepsilon$ for all $m, k > N$. So $\{\|x_n\|\}$ is a Cauchy sequence of real numbers, and since $\mathbb{R}$ is complete, $\lim_n \|x_n\|$ exists.
>
> **Step 2: $\sim$ is an equivalence relation.** *Reflexive:* $\lim_n \|x_n - x_n\| = \lim_n 0 = 0$. *Symmetric:* since $\|y_n - x_n\| = \|x_n - y_n\|$ for every $n$, $\lim_n \|x_n - y_n\| = 0$ implies $\lim_n \|y_n - x_n\| = 0$. *Transitive:* if $\lim_n \|x_n - y_n\| = 0$ and $\lim_n \|y_n - z_n\| = 0$, then by the triangle inequality
>
> $$
> 0 \le \|x_n - z_n\| \le \|x_n - y_n\| + \|y_n - z_n\| \to 0 + 0 = 0,
> $$
>
> and limits preserve non-strict inequalities, so $\lim_n \|x_n - z_n\| = 0$.
>
> **Step 3: $\|\cdot\|_{\overline{X}}$ is well defined.** Suppose $\{x_n\} \sim \{x_n'\}$. By the reverse triangle inequality, $0 \le \bigl|\,\|x_n\| - \|x_n'\|\,\bigr| \le \|x_n - x_n'\|$, so $\lim_n \bigl(\|x_n\| - \|x_n'\|\bigr) = 0$. Both limits exist by Step 1, so by linearity of limits $\lim_n \|x_n\| - \lim_n \|x_n'\| = 0$. Hence $\|[\{x_n\}]\|_{\overline{X}} = \lim_n \|x_n\|$ does not depend on the representative.
>
> **Step 4: the operations on $\overline{X}$ are well defined.** Define $[\{x_n\}] + [\{y_n\}] = [\{x_n + y_n\}]$ and $a[\{x_n\}] = [\{a x_n\}]$.
>
> *The results are Cauchy sequences.* Given $\varepsilon > 0$, choose $N$ with $\|x_m - x_k\| < \varepsilon/2$ and $\|y_m - y_k\| < \varepsilon/2$ for $m, k > N$; then $\|(x_m + y_m) - (x_k + y_k)\| \le \|x_m - x_k\| + \|y_m - y_k\| < \varepsilon$. For $a \neq 0$, choose $N$ with $\|x_m - x_k\| < \varepsilon/|a|$ for $m, k > N$; then $\|a x_m - a x_k\| = |a|\,\|x_m - x_k\| < \varepsilon$. For $a = 0$ the sequence is constantly $0$, hence Cauchy.
>
> *Independence of representatives.* If $\{x_n\} \sim \{x_n'\}$ and $\{y_n\} \sim \{y_n'\}$, then
>
> $$
> \|(x_n + y_n) - (x_n' + y_n')\| \le \|x_n - x_n'\| + \|y_n - y_n'\| \to 0, \qquad \|a x_n - a x_n'\| = |a|\,\|x_n - x_n'\| \to 0,
> $$
>
> so $\{x_n + y_n\} \sim \{x_n' + y_n'\}$ and $\{a x_n\} \sim \{a x_n'\}$.
>
> **Step 5: $\overline{X}$ is a linear space.** In each line the outer equalities use the definition of the operations on classes and the middle equality is the corresponding axiom of $X$, applied at each index $n$. Let $[\{x_n\}], [\{y_n\}], [\{z_n\}] \in \overline{X}$ and $a, k \in \mathbb{F}$.
>
> *Commutativity:* $[\{x_n\}] + [\{y_n\}] = [\{x_n + y_n\}] = [\{y_n + x_n\}] = [\{y_n\}] + [\{x_n\}]$.
>
> *Associativity:* $\bigl([\{x_n\}] + [\{y_n\}]\bigr) + [\{z_n\}] = [\{(x_n + y_n) + z_n\}] = [\{x_n + (y_n + z_n)\}] = [\{x_n\}] + \bigl([\{y_n\}] + [\{z_n\}]\bigr)$.
>
> *Additive identity:* the constant sequence $\{0\}$ is Cauchy, and $[\{x_n\}] + [\{0\}] = [\{x_n + 0\}] = [\{x_n\}] = [\{0 + x_n\}] = [\{0\}] + [\{x_n\}]$.
>
> *Additive inverse:* $\{-x_n\}$ is Cauchy (Step 4 with $a = -1$), and $[\{x_n\}] + [\{-x_n\}] = [\{x_n - x_n\}] = [\{0\}] = [\{-x_n + x_n\}] = [\{-x_n\}] + [\{x_n\}]$.
>
> *Compatibility:* $k\bigl(a[\{x_n\}]\bigr) = k[\{a x_n\}] = [\{k(a x_n)\}] = [\{(ka)x_n\}] = (ka)[\{x_n\}]$.
>
> *Distributivity over vector addition:* $k\bigl([\{x_n\}] + [\{y_n\}]\bigr) = [\{k(x_n + y_n)\}] = [\{k x_n + k y_n\}] = k[\{x_n\}] + k[\{y_n\}]$.
>
> *Distributivity over scalar addition:* $(a + k)[\{x_n\}] = [\{(a + k)x_n\}] = [\{a x_n + k x_n\}] = a[\{x_n\}] + k[\{x_n\}]$.
>
> *Unit:* $1[\{x_n\}] = [\{1 \cdot x_n\}] = [\{x_n\}]$.
>
> Hence $\overline{X}$ is a linear space over $\mathbb{F}$ with zero element $[\{0\}]$.
>
> **Step 6: $\|\cdot\|_{\overline{X}}$ is a norm.** *Positivity.* Each $\|x_n\| \ge 0$, so $\lim_n \|x_n\| \ge 0$. If $\|[\{x_n\}]\|_{\overline{X}} = 0$, then $\lim_n \|x_n - 0\| = 0$, so $\{x_n\} \sim \{0\}$ and $[\{x_n\}] = [\{0\}]$. Conversely, if $[\{x_n\}] = [\{0\}]$ then $\lim_n \|x_n\| = 0$.
>
> *Homogeneity.* By Step 3 it suffices to compute with one representative: $\|a[\{x_n\}]\|_{\overline{X}} = \lim_n \|a x_n\| = \lim_n |a|\,\|x_n\| = |a| \lim_n \|x_n\| = |a|\,\|[\{x_n\}]\|_{\overline{X}}$.
>
> *Triangle inequality.* For every $n$, $\|x_n + y_n\| \le \|x_n\| + \|y_n\|$; all three limits exist by Step 1, and limits preserve non-strict inequalities, so
>
> $$
> \|[\{x_n\}] + [\{y_n\}]\|_{\overline{X}} = \lim_n \|x_n + y_n\| \le \lim_n \|x_n\| + \lim_n \|y_n\| = \|[\{x_n\}]\|_{\overline{X}} + \|[\{y_n\}]\|_{\overline{X}} .
> $$
>
> *Extension.* For $x \in X$, $\|[(x, x, \ldots)]\|_{\overline{X}} = \lim_n \|x\| = \|x\|$.
>
> **Step 7: construction of a candidate limit.** Let $\bigl([\{x^{(m)}_n\}_n]\bigr)_{m \ge 1}$ be Cauchy in $\overline{X}$. We build a sequence $\{y_j\}$ in $X$ by choosing, for each $j$, a sequence index $M_j$ and a term index $N_j$: one term out of one representative for each $j$, a diagonal choice.
>
> *Choice of the sequence indices.* Applying the Cauchy property with $\varepsilon = 1/j$, there is $m_j$ with $\|[\{x^{(m)}_n\}] - [\{x^{(k)}_n\}]\|_{\overline{X}} < 1/j$ for all $m, k \ge m_j$. Set $M_j = \max\{m_1, \ldots, m_j\}$, so that $M_1 \le M_2 \le \cdots$ and $M_j \ge m_j$. The condition then holds for all indices $\ge M_j$; taking $k = M_j$,
>
> $$
> \bigl\| [\{x^{(M_j)}_n\}] - [\{x^{(m)}_n\}] \bigr\|_{\overline{X}} = \lim_{n \to \infty} \bigl\| x^{(M_j)}_n - x^{(m)}_n \bigr\| < \frac{1}{j} \qquad \text{for all } m \ge M_j. \tag{3.1}
> $$
>
> *Choice of the term indices.* With the $M_j$ fixed, each $\{x^{(M_j)}_n\}_n$ is Cauchy in $X$, so there is $n_j$ with $\|x^{(M_j)}_n - x^{(M_j)}_{n'}\| < 1/j$ for all $n, n' \ge n_j$. Set $N_j = \max\{n_1, \ldots, n_j\}$, so $N_1 \le N_2 \le \cdots$ and
>
> $$
> \bigl\| x^{(M_j)}_n - x^{(M_j)}_{n'} \bigr\| < \frac{1}{j} \qquad \text{for all } n, n' \ge N_j. \tag{3.2}
> $$
>
> *The candidate.* Define $y_j := x^{(M_j)}_{N_j} \in X$, the $N_j$-th term of the $M_j$-th sequence. Property (3.1) compares the sequence $\{x^{(M_j)}_n\}_n$ to every later sequence in the norm of $\overline{X}$; property (3.2) compares terms of that one sequence to each other.
>
> **Step 8: $\{y_j\}$ is Cauchy in $X$.** Let $\varepsilon > 0$ and choose $J$ with $3/J < \varepsilon$. Take $j, k \ge J$; since $\|y_j - y_k\| = \|y_k - y_j\|$ and the case $j = k$ is trivial, assume $j > k \ge J$. For any index $n'$, inserting two intermediate terms,
>
> $$
> \|y_j - y_k\| \le \underbrace{\bigl\| x^{(M_j)}_{N_j} - x^{(M_j)}_{n'} \bigr\|}_{\text{①}} + \underbrace{\bigl\| x^{(M_j)}_{n'} - x^{(M_k)}_{n'} \bigr\|}_{\text{②}} + \underbrace{\bigl\| x^{(M_k)}_{n'} - x^{(M_k)}_{N_k} \bigr\|}_{\text{③}} .
> $$
>
> *Term ①.* Both term indices belong to the single sequence $\{x^{(M_j)}_n\}_n$; by (3.2) at index $j$, if $n' \ge N_j$ then ① $< 1/j$.
>
> *Term ③.* Likewise, by (3.2) at index $k$, if $n' \ge N_k$ then ③ $< 1/k$.
>
> *Term ②.* The two entries come from different sequences at the same term index. Since $j > k$ and $\{M_j\}$ is non-decreasing, $M_j \ge M_k$, so (3.1) at index $k$ applies with $m = M_j$: $\lim_{n} \|x^{(M_k)}_n - x^{(M_j)}_n\| < 1/k$. A sequence of reals whose limit is $< 1/k$ is eventually $< 1/k$, so there is $N$ (depending on $j$ and $k$) with ② $< 1/k$ for all $n' \ge N$.
>
> *Choice of $n'$.* Take $n' \ge \max\{N_j, N_k, N\}$. All three bounds hold, and since $1/j < 1/k \le 1/J$,
>
> $$
> \|y_j - y_k\| < \frac{1}{j} + \frac{1}{k} + \frac{1}{k} \le \frac{3}{J} < \varepsilon .
> $$
>
> Here $n'$ was chosen after $j$ and $k$ were fixed and does not appear in the conclusion. Hence $\{y_j\}$ is Cauchy in $X$, and $[\{y_j\}] \in \overline{X}$.
>
> **Step 9: $[\{x^{(m)}_n\}] \to [\{y_n\}]$ in $\overline{X}$.** Let $\varepsilon > 0$ and fix $j$ with $3/j < \varepsilon$. For any $m \ge M_j$,
>
> $$
> \bigl\| [\{x^{(m)}_n\}] - [\{y_n\}] \bigr\|_{\overline{X}} \le \underbrace{\bigl\| [\{x^{(m)}_n\}] - [\{x^{(M_j)}_n\}] \bigr\|_{\overline{X}}}_{\text{Ⓐ}} + \underbrace{\bigl\| [\{x^{(M_j)}_n\}] - [\{y_n\}] \bigr\|_{\overline{X}}}_{\text{Ⓑ}} . \tag{3.3}
> $$
>
> *Term Ⓐ.* Since $m \ge M_j$, (3.1) at index $j$ gives Ⓐ $< 1/j$.
>
> *Term Ⓑ.* We claim Ⓑ $\le 2/j$. By definition, Ⓑ $= \lim_n \|x^{(M_j)}_n - y_n\| = \lim_n \|x^{(M_j)}_n - x^{(M_n)}_{N_n}\|$, so it suffices to bound $\|x^{(M_j)}_n - x^{(M_n)}_{N_n}\|$ for all large $n$. Let $n \ge \max\{j, N_j\}$. For any auxiliary index $n'$,
>
> $$
> \bigl\| x^{(M_j)}_n - x^{(M_n)}_{N_n} \bigr\| \le \underbrace{\bigl\| x^{(M_j)}_n - x^{(M_j)}_{n'} \bigr\|}_{\text{①}} + \underbrace{\bigl\| x^{(M_j)}_{n'} - x^{(M_n)}_{n'} \bigr\|}_{\text{②}} + \underbrace{\bigl\| x^{(M_n)}_{n'} - x^{(M_n)}_{N_n} \bigr\|}_{\text{③}} .
> $$
>
> For ①: both term indices lie in $\{x^{(M_j)}_n\}_n$, so by (3.2) at index $j$, if $n' \ge N_j$ (and $n \ge N_j$, which holds) then ① $< 1/j$. For ②: since $n \ge j$ and $\{M_n\}$ is non-decreasing, $M_n \ge M_j$, so (3.1) at index $j$ with $m = M_n$ gives $\lim_{n'} \|x^{(M_j)}_{n'} - x^{(M_n)}_{n'}\| < 1/j$, and there is $P$ (depending on $j$ and $n$) with ② $< 1/j$ for all $n' \ge P$. For ③: both term indices lie in $\{x^{(M_n)}_{n'}\}_{n'}$, so by (3.2) at index $n$, if $n' \ge N_n$ then ③ $< 1/n$. Taking $n' \ge \max\{N_j, N_n, P\}$, all three bounds hold and $n'$ disappears:
>
> $$
> \bigl\| x^{(M_j)}_n - x^{(M_n)}_{N_n} \bigr\| < \frac{2}{j} + \frac{1}{n} \qquad \text{for all } n \ge \max\{j, N_j\}.
> $$
>
> Letting $n \to \infty$, Ⓑ $\le 2/j$.
>
> *Conclusion.* By (3.3), for every $m \ge M_j$, $\|[\{x^{(m)}_n\}] - [\{y_n\}]\|_{\overline{X}} < 1/j + 2/j = 3/j < \varepsilon$. So the Cauchy sequence converges in $\overline{X}$ to $[\{y_n\}]$, and $(\overline{X}, \|\cdot\|_{\overline{X}})$ is complete; with Steps 5 and 6 it is a Banach space.

^pf-13-1

*Uses:* [[§11 Normed Linear Spaces#^lem-11-3|§11.3]], [[§11 Normed Linear Spaces#^def-11-1|Def. §11.1]], [[§11 Normed Linear Spaces#^def-11-5|Def. §11.5]], [[§12 Completeness#^def-12-1|Def. §12.1]], [[§12 Completeness#^def-12-3|Def. §12.3]], [[§12 Completeness#^def-12-4|Def. §12.4]], [[§1 Linear Spaces#^def-1-1|Def. §1.1]], [[§10a Cauchy Sequences#^thm-10a-3|451 §10a.3]] (completeness of $\mathbb{R}$)

> [!remark]- Connections
> - The same construction for $\mathbb{Q} \subset \mathbb{R}$: [[§10a Cauchy Sequences#^rem-10a-4|451 Remark (construction of the reals)]]; there $\Phi = \lim$ is [[§6★ ℝ from Cauchy Sequences of Rationals#^thm-6s-12|451 Theorem §6★.12]], and uniqueness is [[§6★ ℝ from Cauchy Sequences of Rationals#^cor-6s-14|451 §6★.14]].
> - The pattern of the proof: [[Functional Analysis Problem-Solving Techniques#^ex-t5|Technique 5, applications]].

> [!remark] Remark: Comparison with the $\ell^p$ Proof
> The structure is the one from Theorem [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-5|§18.5]], with the roles shifted. In $\ell^p$ the candidate came from coordinates and the closing step needed a uniform tail estimate obtained by truncating. Here the candidate is a *diagonal* sequence $y_j = x^{(M_j)}_{N_j}$: one term from each representative, chosen far enough out that within-representative fluctuations (3.2) and between-representative distances (3.1) are both below $1/j$. The closing step is the same three-term triangle inequality used twice, with an auxiliary index $n'$ that is sent far out after everything else is fixed and then disappears. The two monotone index sequences $M_j, N_j$ are what make “$m = M_n \ge M_j$ when $n \ge j$” available; without the $\max$ in their definition the comparisons in (3.1) could not be applied in the direction needed.

^rem-13-2

> [!remark] Remark
> A student asked whether one could define the norm of a class as the norm of its limit. There is no limit in $X$ to speak of — that is the whole reason for the construction — so the definition must be phrased in terms of the sequence itself, and existence of $\lim \|x_n\|$ is then a claim to prove, not a definition. The relevant estimate is the reverse triangle inequality (Lemma [[§11 Normed Linear Spaces#^lem-11-3|§11.3]]), $\bigl|\,\|x_m\| - \|x_k\|\,\bigr| \le \|x_m - x_k\|$, which makes $\{\|x_n\|\}$ a Cauchy sequence of real numbers.

^rem-13-3

## Identifying a Completion

The construction by equivalence classes is abstract, but in practice the completion of a concrete space can almost always be written down as a concrete space. The following proposition is the tool: if the space is already sitting densely inside something complete, that something *is* the completion.

> [!theorem] Proposition §13.2: Identifying a Completion
> Let $(X, \|\cdot\|_X)$ be a normed linear space, $(Z, \|\cdot\|_Z)$ a Banach space, and $J : X \to Z$ a linear map with $\|Jx\|_Z = \|x\|_X$ for all $x \in X$, such that $J(X)$ is dense in $Z$. Then
>
> $$
> \Phi : \overline{X} \to Z, \qquad \Phi\bigl([\{x_n\}]\bigr) = \lim_{n \to \infty} J x_n,
> $$
>
> is an isometric isomorphism of $\overline{X}$ onto $Z$, and it sends the class of the constant sequence $(x, x, \ldots)$ to $Jx$. In particular, if $X \subset Z$ is a dense linear subspace carrying the restricted norm ($J$ the inclusion), then $\overline{X}$ is isometrically isomorphic to $Z$ by an isomorphism that is the identity on $X$.

^prop-13-2

> [!proof]+ Proof
> (Not covered in lecture.) *The limit exists.* If $\{x_n\}$ is Cauchy in $X$, then $\|Jx_n - Jx_m\|_Z = \|J(x_n - x_m)\|_Z = \|x_n - x_m\|_X$, so $\{Jx_n\}$ is Cauchy in $Z$, and it converges because $Z$ is complete.
>
> *Well defined.* If $\{x_n\} \sim \{x_n'\}$ then $\|Jx_n - Jx_n'\|_Z = \|x_n - x_n'\|_X \to 0$, so the two limits coincide.
>
> *Linear.* The operations on $\overline{X}$ are termwise, $J$ is linear, and limits in $Z$ are linear.
>
> *Isometric.* By continuity of the norm (Proposition [[§11 Normed Linear Spaces#^prop-11-4|§11.4]]),
>
> $$
> \|\Phi([\{x_n\}])\|_Z = \lim_n \|Jx_n\|_Z = \lim_n \|x_n\|_X = \|[\{x_n\}]\|,
> $$
>
> the last equality being the definition of the norm on $\overline{X}$. An isometry is injective: $\Phi(\xi) = 0$ forces $\|\xi\| = 0$, hence $\xi = 0$.
>
> *Surjective.* Let $z \in Z$. By density there are $x_n \in X$ with $Jx_n \to z$. A convergent sequence is Cauchy (Proposition [[§11 Normed Linear Spaces#^prop-11-5|§11.5]]), and $\|x_n - x_m\|_X = \|Jx_n - Jx_m\|_Z$, so $\{x_n\}$ is Cauchy in $X$ and $\Phi([\{x_n\}]) = z$.
>
> Finally $\Phi([(x, x, \ldots)]) = \lim_n Jx = Jx$.

^pf-13-2

*Uses:* [[§13 The Completion of a Normed Space#^thm-13-1|§13.1]], [[§12 Completeness#^def-12-3|Def. §12.3]], [[§12 Completeness#^def-12-4|Def. §12.4]], [[§11 Normed Linear Spaces#^prop-11-4|§11.4]], [[§11 Normed Linear Spaces#^prop-11-5|§11.5]], [[§11 Normed Linear Spaces#^def-11-7|Def. §11.7]], [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-1|Def. §3.1]]

> [!remark]- Connections
> - Used for concrete completions: [[§13 The Completion of a Normed Space#^prop-13-4|§13.4]] ($C^1$), [[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8|§19.8]] ($L^p$).

> [!remark] Remark
> The embedding form is needed in practice: an element of $L^p[a,b]$ is a class of functions equal almost everywhere, so $C[a,b]$ is not literally a subset of $L^p[a,b]$; it sits inside via $f \mapsto [f]$. The proposition is the precise meaning of “$Z$ *is* the completion of $X$”: the abstract $\overline{X}$ and the concrete $Z$ are the same Banach space, with $X$ corresponding to $J(X)$.

^rem-13-4

> [!theorem] Corollary §13.3: Uniqueness of the Completion
> Let $X$ be a normed linear space. If $Z_1$ and $Z_2$ are Banach spaces each containing $X$ as a dense subspace with the same norm, then $Z_1$ and $Z_2$ are isometrically isomorphic by a map fixing $X$. In this sense the completion of $X$ is unique.

^cor-13-3

> [!proof]+ Proof
> (Stated in lecture without proof; the proof is not from lecture.) Both are isometrically isomorphic to $\overline{X}$ by Proposition [[§13 The Completion of a Normed Space#^prop-13-2|§13.2]]; compose one isomorphism with the inverse of the other (Lemma [[§3 Linear Maps, Convexity, and Linear Functionals#^lem-3-1|§3.1]]).

^pf-13-3

*Uses:* [[§13 The Completion of a Normed Space#^prop-13-2|§13.2]], [[§3 Linear Maps, Convexity, and Linear Functionals#^lem-3-1|§3.1]]

> [!remark] Remark: “How Do We Know We Have Not Added Too Much?”
> This was asked in lecture, and Corollary [[§13 The Completion of a Normed Space#^cor-13-3|§13.3]] is the answer: there is no freedom. The construction adds only limits of Cauchy sequences in $X$ and identifies two sequences whenever they head for the same place, so nothing extra can appear.
>
> A larger complete space containing $X$ need not be the completion. A student's example: with the usual absolute value, the completion of $\mathbb{Q}$ is $\mathbb{R}$, and $\mathbb{R} \subset \mathbb{C}$ with $\mathbb{C}$ complete — but $\mathbb{C}$ is not the completion of $\mathbb{Q}$, because a Cauchy sequence of rationals cannot converge to a non-real number. Equivalently in Wu's version, $\mathbb{R} \subset \mathbb{R}^2$ is a complete space containing $\mathbb{R}$, and is not its completion. The condition that fails is density.
>
> Also worth separating: the definition of $\overline{X}$ is by equivalence classes, and the description “$X$ together with all its limit points” is a way of thinking, not a definition — before the construction there is no ambient space in which those limit points live. Wu: “the previous one is more precise; the later one is a way of thinking. What is the limit when you don't even have a point?”

^rem-13-5

> [!remark] Remark: The Norm Decides, Not the Set
> A second trap. As *sets*, $C[a,b] \subset L^1[a,b]$, and $L^1[a,b]$ is complete; but $L^1[a,b]$ is not the completion of $\bigl(C[a,b], \|\cdot\|_\infty\bigr)$, which is already complete (Theorem [[§12 Completeness#^thm-12-1|§12.1]]) and is therefore its own completion. The two norms $\|\cdot\|_\infty$ and $\|\cdot\|_{L^1}$ are not [[§14 New Normed Spaces from Old#^def-14-1|equivalent]], so they give different topologies, different Cauchy sequences, and different completions. A normed linear space is the pair $(X, \|\cdot\|)$, never the set alone; the completion is determined by the norm. The same set $C[a,b]$ with the $L^p$ norm, $1 \le p < \infty$, does have completion $L^p[a,b]$ ([[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8|§19.8]]).

^rem-13-6

## An Incomplete Normed Space

> [!example] Example §13.1: $C^2[a,b]$ with a $C^1$ Norm
> Let $C^k[a,b]$ denote the $k$ times continuously differentiable functions on $[a,b]$. The natural norm on $C^2[a,b]$ is
>
> $$
> \|f\|_{C^2[a,b]} = \max_{[a,b]} |f| + \max_{[a,b]} |f'| + \max_{[a,b]} |f''|,
> $$
>
> and $(C^2[a,b], \|\cdot\|_{C^2})$ is complete, by the same argument as for $C[a,b]$ (Theorem [[§12 Completeness#^thm-12-1|§12.1]]) applied to $f$, $f'$, $f''$ simultaneously. But the set $X = C^2[a,b]$ may also be given the smaller norm
>
> $$
> \|f\|_X = \max_{[a,b]} |f| + \max_{[a,b]} |f'|,
> $$
>
> which omits the second derivative, and $(X, \|\cdot\|_X)$ is a normed linear space that is *not* complete. This is another instance of the previous remark: the same set, two inequivalent norms, one complete and one not.

^ex-13-1

> [!theorem] Proposition §13.4: $(C^2[a,b], \|\cdot\|_X)$ is Not Complete
> With $\|f\|_X = \max |f| + \max |f'|$, the space $X = C^2[a,b]$ is not complete, and its completion is $C^1[a,b]$ with the same norm.
>
> *Source: HW3, Problem 2*

^prop-13-4

> [!proof]+ Proof
> (HW3, Problem 2.)
> Throughout, $C^k([a,b])$ ($k = 1, 2$) denotes the functions $f : [a,b] \to \mathbb{F}$ that are $k$ times differentiable on $[a,b]$ (one-sided at the endpoints) with $f^{(k)}$ continuous, and $\|g\|_\infty = \max_{[a,b]} |g|$ for $g \in C([a,b])$; $(C([a,b]), \|\cdot\|_\infty)$ is a Banach space (Theorem [[§12 Completeness#^thm-12-1|§12.1]]). Write $\|f\| = \|f\|_X = \|f\|_\infty + \|f'\|_\infty$. For complex-valued functions, differentiation and integration act on real and imaginary parts, so the fundamental theorem of calculus holds, and $\bigl|\int_\alpha^\beta h\bigr| \leq \int_\alpha^\beta |h|$ for continuous $h$. We show that $(X, \|\cdot\|)$ is a normed linear space, that it is *not* complete, and that its completion is $C^1([a,b])$ with the same norm.
>
> **Part 1: $(X, \|\cdot\|)$ is a normed linear space.** If $f, g \in X$ and $c \in \mathbb{F}$, then $(f + g)' = f' + g'$, $(f+g)'' = f'' + g''$, $(cf)' = cf'$ and $(cf)'' = cf''$, all continuous; so $X$ is a linear subspace of $C([a,b])$, hence a linear space. The norm is well defined because $f$ and $f'$ are continuous on $[a,b]$, so both maxima exist.
>
> *Positivity.* $\|f\| \geq 0$. If $\|f\| = 0$, then $\|f\|_\infty = 0$, since both terms are non-negative; so $f = 0$.
>
> *Homogeneity.* $\|cf\| = \|cf\|_\infty + \|cf'\|_\infty = |c|\,\|f\|_\infty + |c|\,\|f'\|_\infty = |c|\,\|f\|$.
>
> *Triangle inequality.* By the triangle inequality for $\|\cdot\|_\infty$,
>
> $$\|f + g\| = \|f + g\|_\infty + \|f' + g'\|_\infty \leq \|f\|_\infty + \|g\|_\infty + \|f'\|_\infty + \|g'\|_\infty = \|f\| + \|g\|.$$
>
> The same computations, which use only the first derivative, show that $\|\cdot\|$ is also a norm on $C^1([a,b])$. Write $Z = (C^1([a,b]), \|\cdot\|)$; then $X \subset Z$, with the same norm.
>
> **Part 2: $Z$ is complete.** Let $\{f_n\}$ be Cauchy in $Z$. Since $\|f_n - f_m\|_\infty \leq \|f_n - f_m\|$ and $\|f_n' - f_m'\|_\infty \leq \|f_n - f_m\|$, both $\{f_n\}$ and $\{f_n'\}$ are Cauchy in $(C([a,b]), \|\cdot\|_\infty)$, which is complete. So there are $f, g \in C([a,b])$ with
>
> $$\|f_n - f\|_\infty \to 0, \qquad \|f_n' - g\|_\infty \to 0.$$
>
> By the fundamental theorem of calculus, for every $n$ and every $x \in [a,b]$,
>
> $$f_n(x) = f_n(a) + \int_a^x f_n'(t)\,dt.$$
>
> Fix $x$. As $n \to \infty$, $f_n(x) \to f(x)$, $f_n(a) \to f(a)$, and
>
> $$\Bigl| \int_a^x f_n'(t)\,dt - \int_a^x g(t)\,dt \Bigr| \leq \int_a^x |f_n' - g| \leq (b - a)\,\|f_n' - g\|_\infty \to 0.$$
>
> Hence
>
> $$f(x) = f(a) + \int_a^x g(t)\,dt \qquad \text{for all } x \in [a,b].$$
>
> Since $g$ is continuous, the fundamental theorem of calculus shows that $f$ is differentiable on $[a,b]$ with $f' = g$. So $f \in C^1([a,b])$, and
>
> $$\|f_n - f\| = \|f_n - f\|_\infty + \|f_n' - g\|_\infty \to 0.$$
>
> Thus $Z$ is complete.
>
> **Part 3: $X$ is dense in $Z$.** Let $f \in C^1([a,b])$ and $\varepsilon > 0$. Since $f'$ is continuous on $[a,b]$, the [[§27 Weierstrass's Approximation Theorem (Not Covered)|Weierstrass approximation theorem]] (applied to the real and imaginary parts if $\mathbb{F} = \mathbb{C}$) gives a polynomial $P$ with
>
> $$\|P - f'\|_\infty < \frac{\varepsilon}{1 + b - a}.$$
>
> Define
>
> $$q(x) = f(a) + \int_a^x P(t)\,dt, \qquad x \in [a,b].$$
>
> Then $q$ is a polynomial, so $q \in C^2([a,b]) = X$, and $q' = P$. Using $f(x) = f(a) + \int_a^x f'(t)\,dt$,
>
> $$|q(x) - f(x)| = \Bigl| \int_a^x \bigl( P(t) - f'(t) \bigr)\,dt \Bigr| \leq (b - a)\,\|P - f'\|_\infty \qquad \text{for all } x \in [a,b].$$
>
> Hence
>
> $$\|q - f\| = \|q - f\|_\infty + \|P - f'\|_\infty \leq (1 + b - a)\,\|P - f'\|_\infty < \varepsilon.$$
>
> **Part 4: $X \neq Z$.** Let $c = (a+b)/2$ and $\varphi(x) = |x - c|^{3/2}$. For $x \neq c$, the chain rule gives $\varphi'(x) = \frac32 \operatorname{sgn}(x - c)\,|x - c|^{1/2}$. At $x = c$,
>
> $$\Bigl| \frac{\varphi(c + h) - \varphi(c)}{h} \Bigr| = |h|^{1/2} \xrightarrow[h \to 0]{} 0,$$
>
> so $\varphi'(c) = 0$. Thus $\varphi'(x) = \frac32 \operatorname{sgn}(x - c)\,|x - c|^{1/2}$ for all $x$ (with $\operatorname{sgn} 0 = 0$), and $\varphi'$ is continuous on $[a,b]$: it is continuous away from $c$, and $|\varphi'(x)| = \frac32 |x - c|^{1/2} \to 0 = \varphi'(c)$ as $x \to c$. So $\varphi \in C^1([a,b])$. However,
>
> $$\frac{\varphi'(c + h) - \varphi'(c)}{h} = \frac32 \cdot \frac{\operatorname{sgn}(h)\,|h|^{1/2}}{h} = \frac32\,|h|^{-1/2} \xrightarrow[h \to 0]{} \infty,$$
>
> so $\varphi'$ is not differentiable at $c$, and $\varphi \notin C^2([a,b])$.
>
> **Part 5: conclusion.**
>
> *$X$ is not complete.* By Part 3 there are $q_n \in X$ with $\|q_n - \varphi\| \to 0$. The sequence $\{q_n\}$ is Cauchy in $X$, since $\|q_n - q_m\| \leq \|q_n - \varphi\| + \|\varphi - q_m\|$. If it converged in $X$ to some $h \in X$, then, as $X$ carries the norm of $Z$, it would converge in $Z$ to both $h$ and $\varphi$. Limits in a metric space are unique, so $\varphi = h \in X$, contradicting Part 4. Hence $(X, \|\cdot\|)$ is not complete.
>
> *The completion.* The inclusion $J : X \to Z$ is linear and norm-preserving, $J(X) = X$ is dense in $Z$ by Part 3, and $Z$ is a Banach space by Part 2. By Proposition [[§13 The Completion of a Normed Space#^prop-13-2|§13.2]], the completion of $(X, \|\cdot\|)$ is
>
> $$\Bigl( C^1([a,b]),\ \|f\| = \max_{t \in [a,b]} |f(t)| + \max_{t \in [a,b]} |f'(t)| \Bigr).$$

^pf-13-4

*Uses:* [[§12 Completeness#^thm-12-1|§12.1]], [[§13 The Completion of a Normed Space#^prop-13-2|§13.2]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]], [[§11 Normed Linear Spaces#^def-11-1|Def. §11.1]], [[§11 Normed Linear Spaces#^prop-11-5|§11.5]], [[§12 Completeness#^def-12-1|Def. §12.1]], [[Fundamental Theorem of Calculus|451 Fundamental Theorem of Calculus]], [[§33 Properties of the Riemann Integral#^thm-33-4|451 §33.4]], [[§27 Weierstrass's Approximation Theorem (Not Covered)|451 §27 (Weierstrass approximation)]]
