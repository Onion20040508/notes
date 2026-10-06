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
