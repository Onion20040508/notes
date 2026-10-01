---
type: section
subject: "[[Functional Analysis]]"
chapter: 4
section: 14
tags: [functional-analysis, math556]
---
← [[§13 Minkowski's Inequality and the Spaces ℓᵖ]] · ↑ [[· 4 Infinite-Dimensional Spaces꞉ ℓᵖ, Lᵖ, and Compactness]] · [[§15 Compactness and the Unit Ball]] →

*Stage: norms — Thread: completeness. Function spaces; $L^p$ as the completion of $C[a,b]$.*

## Definition and the Integral Inequalities

The second way to go to infinite dimensions is to index by a continuum: a function $f$ on $[a, b]$ assigns to each $x$ a value $f(x)$, and functions can be added and scaled, so the functions on $[a,b]$ form a linear space. The analogue of $\sum_i |a_i|^p$ is an integral.

> [!remark] Remark: The Integral as a Sum
> For continuous $f$ on $[a,b]$ and a partition $a = x_0 < x_1 < \cdots < x_n = b$ with $\Delta x_i = x_{i+1} - x_i$,
>
> $$
> \int_a^b |f(x)|\, dx \;\approx\; \sum_{i=0}^{n-1} |f(x_i)|\, \Delta x_i,
> $$
>
> the Riemann sum, which improves as the partition is refined. So $\int |f|^p$ is the continuum version of $\sum |a_i|^p$, with $f(x_i)$ in place of $a_i$ and the widths $\Delta x_i$ as weights.
>
> ![[m556-14-1.svg]]
> *A left-endpoint Riemann sum for $|f|$ on $[a,b]$: rectangles of width $\Delta x_i$ and height $|f(x_i)|$ under the graph $y = |f(x)|$.*

^rem-14-1

> [!definition] Definition §14.1: $L^p(\Omega)$, $L^\infty(\Omega)$ — working definition
> Let $\Omega \subset \mathbb{R}^n$ be a domain. For $1 \le p < \infty$,
>
> $$
> L^p(\Omega) = \Bigl\{ f \text{ integrable on } \Omega : \|f\|_{L^p} := \Bigl( \int_\Omega |f(x)|^p\, dx \Bigr)^{1/p} < \infty \Bigr\},
> $$
>
> and
>
> $$
> L^\infty(\Omega) = \Bigl\{ f \text{ bounded on } \Omega : \|f\|_{L^\infty} := \sup_{x \in \Omega} |f(x)| < \infty \Bigr\}.
> $$
>
> $\|f\|_{L^p}$ is also written $\|f\|_p$.
>
> *Lax: §5.1, example (f)*

^def-14-1

> [!remark]- Connections
> - The rigorous definitions: [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-5|551 Def. §19.5]] ($L^p$, measurable functions) and [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-6|551 Def. §19.6]] ($L^\infty$, essential supremum).
> - The sequence analogue: [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^def-13-1|Def. §13.1]].

> [!remark] Remark: What “Integrable” Means Here
> Wu deliberately left “integrable” unspecified. Rigorously it means Lebesgue integrable (measurable with finite integral of $|f|^p$), functions agreeing outside a set of measure zero are identified, and $\|f\|_{L^\infty}$ is the [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-6|essential supremum]]; without the identification, positivity of the norm fails ($f = 0$ except at one point has $\|f\|_p = 0$). Since MATH 551 is not a prerequisite for this course, she asked us to take “integrable” as “anything you will meet,” with continuous functions as the safe case (continuous on a compact $\Omega$ implies Riemann integrable), and said the theory could be made rigorous later. The full treatment — Lebesgue integral, $L^p$, [[Hölder's Inequality|Hölder]], [[Minkowski's Inequality|Minkowski]], [[Riesz–Fischer Theorem|Riesz–Fischer]], [[Dominated Convergence Theorem|dominated]] and [[Monotone Convergence Theorem (Lebesgue)|monotone convergence]], [[Fatou's Lemma|Fatou]] — is in the MATH 551 notes, Chapters on [[· 4 Integration Theory|Lebesgue integration]] and [[· 6 Lᵖ Spaces|Lᵖ spaces]], and that is the version to rely on. (For those without it: chapter 2 of the posted reference notes.)

^rem-14-2

> [!theorem] Theorem §14.1: Hölder's Inequality for Functions
> Let $1 \le p \le \infty$ and $q$ its conjugate. For $f \in L^p(\Omega)$, $g \in L^q(\Omega)$,
>
> $$
> \int_\Omega |f(x) g(x)|\, dx \le \|f\|_{L^p}\, \|g\|_{L^q}.
> $$

^thm-14-1

> [!proof]+ Proof
> Not proved in lecture; “the same idea, exactly” as Theorem [[§12 Hölder's Inequality for Sequences#^thm-12-1|§12.1]], with the integral in place of the sum: normalize, apply [[§11 Means and Young's Inequality#^lem-11-3|Young]] pointwise, integrate. A full proof is in the MATH 551 notes, Chapter *$L^p$ Spaces*, subsection *Hölder's Inequality* ([[Hölder's Inequality|Theorem: Hölder's Inequality]]).

^pf-14-1

*Uses:* [[§12 Hölder's Inequality for Sequences#^thm-12-1|§12.1]], [[§11 Means and Young's Inequality#^lem-11-3|§11.3]], [[Hölder's Inequality|551 §19.5]]

> [!remark]- Connections
> - Home: [[Hölder's Inequality|551 §19.5]]. The version for continuous functions on $[a,b]$ is proved here as [[§14 The Function Spaces Lᵖ(Ω)#^lem-14-7|§14.7]] (HW3).
> - With $p = q = 2$ it makes the $L^2$ inner product converge: [[§16 Definition and Examples#^ex-16-3|Ex. §16.3]].

> [!theorem] Theorem §14.2: Minkowski's Inequality for Functions
> For $1 \le p \le \infty$ and $f, g \in L^p(\Omega)$,
>
> $$
> \|f + g\|_{L^p} \le \|f\|_{L^p} + \|g\|_{L^p}.
> $$

^thm-14-2

> [!proof]+ Proof
> Not proved in lecture; as for Theorem [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^thm-13-1|§13.1]], with the same truncation issue handled by first assuming $\|f+g\|_p < \infty$ (which follows from $|f+g|^p \le 2^{p-1}(|f|^p + |g|^p)$). A full proof is in the MATH 551 notes, Chapter *$L^p$ Spaces*, subsection *$L^p$ is a Normed Linear Space* ([[Minkowski's Inequality|Theorem: Minkowski's Inequality]], with corollaries for [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-11|finite sums]] and [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-12|series]]).

^pf-14-2

*Uses:* [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^thm-13-1|§13.1]], [[Minkowski's Inequality|551 §19.9]]

> [!remark]- Connections
> - Home: [[Minkowski's Inequality|551 §19.9]]; with it, $L^p$ is a normed linear space, [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-10|551 §19.10]]. The version for continuous functions on $[a,b]$ is Part 1 of the proof of [[§14 The Function Spaces Lᵖ(Ω)#^prop-14-8|§14.8]] (HW3).

## Completeness and Density

> [!theorem] Theorem §14.3: $L^p(\Omega)$ and $L^\infty(\Omega)$ are Banach Spaces
> For $1 \le p \le \infty$, $(L^p(\Omega), \|\cdot\|_{L^p})$ is a complete normed linear space.

^thm-14-3

> [!proof]+ Proof
> Deferred: Wu skipped the proof because it needs real-analysis tools (a candidate limit must be built from an almost-everywhere convergent subsequence, and [[Monotone Convergence Theorem (Lebesgue)|monotone]]/[[Dominated Convergence Theorem|dominated convergence]] used to close the argument). The plan is the same as for $\ell^p$ ([[§13 Minkowski's Inequality and the Spaces ℓᵖ#^thm-13-5|§13.5]]) — find the candidate, then prove convergence — but the candidate is harder to produce. The theorem is Riesz–Fischer; a full proof is in the MATH 551 notes, Chapter *$L^p$ Spaces*, subsection *[[Riesz–Fischer Theorem|The Riesz–Fischer Theorem]]*.

^pf-14-3

*Uses:* [[Riesz–Fischer Theorem|551 §19.18]]

> [!remark]- Connections
> - Home: [[Riesz–Fischer Theorem|551 §19.18]] (stated there for $1 \le p \le \infty$).
> - Used in [[§14 The Function Spaces Lᵖ(Ω)#^prop-14-8|§14.8]] (R2); $L^2$ is a Hilbert space: [[§17 Cauchy–Schwarz and the Induced Norm#^ex-17-1|Ex. §17.1]].

> [!theorem] Theorem §14.4: Density of Smooth Functions
> For $1 \le p < \infty$, $C^\infty(\Omega)$ is dense in $L^p(\Omega)$: for every $f \in L^p(\Omega)$ and $\varepsilon > 0$ there is $\varphi \in C^\infty(\Omega)$ with $\|f - \varphi\|_{L^p} < \varepsilon$.

^thm-14-4

> [!proof]+ Proof
> Deferred. Wu said she would look for a proof that avoids heavy measure theory and present it next lecture if one is available. (The MATH 551 notes, Chapter *$L^p$ Spaces*, subsection *Density and Separability*, [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|prove]] that simple functions, step functions, and compactly supported continuous functions are dense in $L^p$ for $1 \le p < \infty$; smoothing by convolution with a $C^\infty$ bump takes it the rest of the way to $C^\infty$.)

^pf-14-4

*Uses:* [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|551 §19.19]]

> [!remark]- Connections
> - Home of the density results: [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|551 §19.19]] — its (iii), $C_c$ dense, is the form needed where compact support matters; the $L^1$ case is [[Continuous Functions of Compact Support are Dense in L¹|551 §16.7]].
> - Cited in [[§14 The Function Spaces Lᵖ(Ω)#^prop-14-8|§14.8]] (R3), [[§17 Cauchy–Schwarz and the Induced Norm#^ex-17-2|Ex. §17.2]], and [[§20 Orthonormal Sets and Bases#^prop-20-15|§20.15]] (separability of $L^p$).

> [!theorem] Proposition §14.5: Continuous Functions are Not Dense in $L^\infty$
> $C(\Omega)$ is not dense in $L^\infty(\Omega)$.

^prop-14-5

> [!proof]+ Proof
> Take $\Omega = [0,1]$ and the step function $f = \chi_{[1/2, 1]}$, i.e. $f(x) = 0$ for $x < 1/2$ and $f(x) = 1$ for $x \ge 1/2$; $f$ is bounded, so $f \in L^\infty[0,1]$. We claim $\|f - g\|_{L^\infty} \ge 1/2$ for every $g \in C[0,1]$, so no sequence of continuous functions converges to $f$ in $L^\infty$. Suppose instead $\|f - g\|_{L^\infty} = \sup_x |f(x) - g(x)| < 1/2$ for some continuous $g$. Then for $x < 1/2$, $|g(x)| = |f(x) - g(x)| < 1/2$, and for $x \ge 1/2$, $|g(x) - 1| < 1/2$, so $g(x) > 1/2$. By continuity of $g$ at $1/2$, $g(1/2) = \lim_{x \to 1/2^-} g(x) \le 1/2$, while $g(1/2) > 1/2$ from the second condition: a contradiction. (With the Lebesgue definition of $L^\infty$ the same argument works after replacing “for all $x$” by “for almost every $x$” and using that a continuous function satisfying a strict inequality almost everywhere on an interval satisfies the non-strict one everywhere on it.)
>
> Alternatively, as Wu suggested: $C[0,1]$ with the supremum norm is complete (Theorem [[§9 Completeness#^thm-9-1|§9.1]]), hence a closed subspace of $L^\infty[0,1]$ (Lemma [[§9 Completeness#^lem-9-2|§9.2]]), and a closed proper subspace is not dense; $f$ above shows the inclusion is proper.

^pf-14-5

*Uses:* [[§14 The Function Spaces Lᵖ(Ω)#^def-14-1|Def. §14.1]], [[§8 Normed Linear Spaces#^def-8-7|Def. §8.7]], [[§9 Completeness#^thm-9-1|§9.1]], [[§9 Completeness#^lem-9-2|§9.2]]

![[m556-14-3.svg]]
*Why the step $f = \chi_{[1/2,1]}$ has no uniform approximation: a continuous $g$ with $\|f - g\|_{L^\infty} < \tfrac12$ would have to stay in the open gray band around $f$, below $\tfrac12$ on $[0, \tfrac12)$ and above $\tfrac12$ on $[\tfrac12, 1]$. Being continuous, $g$ must reach the level $\tfrac12$, and wherever it does it leaves the band (red). Compare the ramps of [[§14 The Function Spaces Lᵖ(Ω)#^prop-14-8|§14.8]], which do approach a step in $L^p$.*

> [!remark]- Connections
> - The same example in Measure Theory, where the $L^p$ approximation chain breaks at $p = \infty$: [[§19 Normed Linear Spaces and Lᵖ Spaces#^rem-19-4|551 Remark §19]] (The Approximation Chain for $L^p$); a uniform limit of continuous functions is continuous, [[§24 Uniform Convergence#^thm-24-2|451 §24.2]].

> [!remark] Remark
> The failure at $p = \infty$ is the first sign that $L^\infty$ behaves differently from the other $L^p$: uniform approximation cannot smooth out a jump. The pattern “true for $1 \le p < \infty$, false for $p = \infty$” will recur, e.g. in identifying dual spaces.

^rem-14-3

## The Completion of C[a,b] in the Lᵖ Norm

> [!theorem] Lemma §14.6: A Vanishing Integral
> Let $\alpha < \beta$ and let $h : [\alpha,\beta] \to [0,\infty)$ be continuous with $\int_\alpha^\beta h(x)\,dx = 0$. Then $h(x) = 0$ for all $x \in [\alpha,\beta]$.
>
> *Source: HW3, Problem 1*

^lem-14-6

> [!proof]+ Proof
> (HW3, Problem 1.) Suppose $h(x_0) = \eta > 0$ for some $x_0 \in [\alpha,\beta]$. By continuity there is $\delta > 0$ with $h(x) > \eta/2$ for all $x \in I := [x_0 - \delta, x_0 + \delta] \cap [\alpha,\beta]$. Since $\alpha < \beta$, $I$ is an interval of some length $\ell > 0$. As $h \geq 0$ on $[\alpha,\beta]$,
>
> $$
> \int_\alpha^\beta h \geq \int_I h \geq \ell \cdot \frac{\eta}{2} > 0,
> $$
>
> a contradiction.

^pf-14-6

*Uses:* [[§33 Properties of the Riemann Integral#^thm-33-3|451 §33.3]], [[§33 Properties of the Riemann Integral#^thm-33-5|451 §33.5]]

> [!remark]- Connections
> - Home: [[§33 Properties of the Riemann Integral#^thm-33-7|451 §33.7]] (the same statement); the Lebesgue version, with “almost everywhere”: [[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|551 §14.11]].

> [!theorem] Lemma §14.7: Hölder's Inequality for Continuous Functions
> Let $1 < p < \infty$ and $q = p/(p-1)$, so that $\frac1p + \frac1q = 1$. For $u, v \in C([a,b])$,
>
> $$
> \int_a^b |u(x)\,v(x)|\,dx \leq \Bigl( \int_a^b |u|^p \Bigr)^{1/p} \Bigl( \int_a^b |v|^q \Bigr)^{1/q}.
> $$
>
> *Source: HW3, Problem 1*

^lem-14-7

> [!proof]+ Proof
> (HW3, Problem 1.) Write $A = (\int_a^b |u|^p)^{1/p}$ and $B = (\int_a^b |v|^q)^{1/q}$. If $A = 0$, then $|u|^p \equiv 0$ by Lemma [[§14 The Function Spaces Lᵖ(Ω)#^lem-14-6|§14.6]], so $u \equiv 0$ and both sides vanish; likewise if $B = 0$. Otherwise put $U = u/A$ and $V = v/B$, so that $\int_a^b |U|^p = \int_a^b |V|^q = 1$. [[§11 Means and Young's Inequality#^lem-11-3|Young's inequality from class]], $s^{1-\theta} t^{\theta} \leq (1-\theta)\,s + \theta\, t$ for $s, t \geq 0$ and $\theta \in [0,1]$, applied at each $x \in [a,b]$ with $s = |U(x)|^p$, $t = |V(x)|^q$, $\theta = 1/q$ (so $1 - \theta = 1/p$), gives
>
> $$
> |U(x)|\,|V(x)| \leq \frac1p\,|U(x)|^p + \frac1q\,|V(x)|^q.
> $$
>
> Both sides are continuous in $x$; integrating over $[a,b]$ (monotonicity and linearity of the integral),
>
> $$
> \int_a^b |UV| \leq \frac1p + \frac1q = 1,
> $$
>
> and multiplying by $AB$ gives the claim.

^pf-14-7

*Uses:* [[§14 The Function Spaces Lᵖ(Ω)#^lem-14-6|§14.6]], [[§11 Means and Young's Inequality#^lem-11-3|§11.3]], [[§33 Properties of the Riemann Integral#^thm-33-2|451 §33.2]], [[§33 Properties of the Riemann Integral#^thm-33-3|451 §33.3]]

> [!remark]- Connections
> - Home: [[Hölder's Inequality|551 §19.5]] (measurable functions); the sequence version [[§12 Hölder's Inequality for Sequences#^thm-12-1|§12.1]] has the same proof.
> - For $p = q = 2$ and continuous functions: [[§19 Inner Products and Norms#^ladr-6-16|LADR 6.16(b)]].

> [!theorem] Proposition §14.8: $L^p[a,b]$ as a Completion
> Let $1 \le p < \infty$ and let $X = C[a,b]$, the continuous functions on $[a,b]$, with the norm
>
> $$
> \|f\|_p = \Bigl( \int_a^b |f(x)|^p\, dx \Bigr)^{1/p}.
> $$
>
> Then $(X, \|\cdot\|_p)$ is a normed linear space, it is not complete, and its completion is $L^p[a,b]$.
>
> *Source: HW3, Problem 1*
>
> *Lax: §5.1, example (f)*

^prop-14-8

> [!proof]+ Proof
> (HW3, Problem 1.)
> Throughout, $\mathbb{F}$ denotes the scalar field ($\mathbb{R}$ or $\mathbb{C}$), $a < b$, and $X = C([a,b])$ is the space of continuous functions $f : [a,b] \to \mathbb{F}$ with pointwise operations; $X$ is a linear space (Theorem [[§9 Completeness#^thm-9-1|§9.1]], Part 1). Integrals of continuous functions are Riemann integrals. We show that $(X, \|\cdot\|_p)$ is a normed linear space, that it is *not* complete, and that its completion is $L^p([a,b])$.
>
> **Part 1: $\|\cdot\|_p$ is a norm on $X$.**
>
> *Well defined.* For $f \in X$ the function $|f|^p$ is continuous on $[a,b]$, as a composition of continuous maps, hence Riemann integrable with $\int_a^b |f|^p \in [0,\infty)$. So $\|f\|_p$ is a well-defined non-negative real number.
>
> *Positivity.* $\|f\|_p \geq 0$. If $\|f\|_p = 0$, then $\int_a^b |f|^p = 0$, so $|f|^p \equiv 0$ by Lemma [[§14 The Function Spaces Lᵖ(Ω)#^lem-14-6|§14.6]], i.e. $f = 0$. Conversely $\|0\|_p = 0$.
>
> *Homogeneity.* For $c \in \mathbb{F}$,
>
> $$
> \|cf\|_p = \Bigl( \int_a^b |c|^p\,|f|^p \Bigr)^{1/p} = \Bigl( |c|^p \int_a^b |f|^p \Bigr)^{1/p} = |c|\,\|f\|_p.
> $$
>
> *Triangle inequality.* Let $f, g \in X$. If $p = 1$, integrate the pointwise inequality $|f + g| \leq |f| + |g|$. Let $1 < p < \infty$ and $q = p/(p-1)$, so that $(p - 1)\,q = p$. If $\|f + g\|_p = 0$ there is nothing to prove, so assume $\|f + g\|_p > 0$. Pointwise,
>
> $$
> |f + g|^p = |f + g|^{p-1}\,|f + g| \leq |f|\,|f + g|^{p-1} + |g|\,|f + g|^{p-1},
> $$
>
> and every function here is continuous. Integrating, and applying Lemma [[§14 The Function Spaces Lᵖ(Ω)#^lem-14-7|§14.7]] to each term with $u = |f|$ (respectively $u = |g|$) and $v = |f + g|^{p-1}$,
>
> $$
> \|f + g\|_p^p \leq \bigl( \|f\|_p + \|g\|_p \bigr) \Bigl( \int_a^b |f + g|^{(p-1)q} \Bigr)^{1/q} = \bigl( \|f\|_p + \|g\|_p \bigr)\, \|f + g\|_p^{\,p/q}.
> $$
>
> Since $0 < \|f + g\|_p < \infty$ and $p - p/q = 1$, dividing by $\|f + g\|_p^{\,p/q}$ gives $\|f + g\|_p \leq \|f\|_p + \|g\|_p$.
>
> Hence $(X, \|\cdot\|_p)$ is a normed linear space.
>
> **Part 2: $(X, \|\cdot\|_p)$ is not complete.** Let $c = (a+b)/2$ and fix $N_0 \in \mathbb{N}$ with $1/N_0 < b - c$. For $n \geq N_0$ define
>
> $$
> f_n(x) = \begin{cases} 0, & a \leq x \leq c, \\ n(x - c), & c \leq x \leq c + \frac1n, \\ 1, & c + \frac1n \leq x \leq b. \end{cases}
> $$
>
> Each $f_n$ is continuous, since the formulas agree at $x = c$ and at $x = c + \frac1n$, and $0 \leq f_n \leq 1$.
>
> *$\{f_n\}$ is Cauchy.* Let $N \geq N_0$ and $m, n \geq N$. Both $f_m$ and $f_n$ vanish on $[a, c]$ and both equal $1$ on $[c + \frac1N, b]$, because $c + \frac1m \leq c + \frac1N$ and $c + \frac1n \leq c + \frac1N$. So $f_m - f_n = 0$ outside $[c, c + \frac1N]$, and $|f_m - f_n| \leq 1$ everywhere since both take values in $[0,1]$. Hence
>
> $$
> \|f_m - f_n\|_p^p = \int_c^{c + 1/N} |f_m - f_n|^p \leq \frac1N, \qquad \text{i.e.} \qquad \|f_m - f_n\|_p \leq N^{-1/p} \xrightarrow[N \to \infty]{} 0.
> $$
>
> *$\{f_n\}$ has no limit in $X$.* Suppose $f \in X$ with $\|f_n - f\|_p \to 0$.
> - On $[a, c]$ we have $f_n = 0$, so for every $n \geq N_0$,
>
>   $$
>   \int_a^c |f|^p = \int_a^c |f_n - f|^p \leq \|f_n - f\|_p^p.
>   $$
>
>   The left side does not depend on $n$ and the right side tends to $0$, so $\int_a^c |f|^p = 0$, and Lemma [[§14 The Function Spaces Lᵖ(Ω)#^lem-14-6|§14.6]] gives $f = 0$ on $[a, c]$. In particular $f(c) = 0$.
> - Fix $\delta \in (0, b - c)$. For $n \geq N_0$ with $n > 1/\delta$ we have $f_n = 1$ on $[c + \delta, b]$, so
>
>   $$
>   \int_{c + \delta}^b |1 - f|^p = \int_{c + \delta}^b |f_n - f|^p \leq \|f_n - f\|_p^p \xrightarrow[n \to \infty]{} 0.
>   $$
>
>   Hence $\int_{c + \delta}^b |1 - f|^p = 0$, and Lemma [[§14 The Function Spaces Lᵖ(Ω)#^lem-14-6|§14.6]] gives $f = 1$ on $[c + \delta, b]$. Since $\delta \in (0, b - c)$ was arbitrary, $f = 1$ on $(c, b]$.
>
> Then $\lim_{x \to c^+} f(x) = 1 \neq 0 = f(c)$, contradicting the continuity of $f$ at $c$. So $\{f_n\}$ is a Cauchy sequence in $X$ with no limit in $X$, and $(X, \|\cdot\|_p)$ is not complete.
>
> **Part 3: the completion is $L^p([a,b])$.** Here $\overline{Y}$ denotes the completion of a normed linear space $Y$ [[§9 Completeness#^thm-9-3|constructed in class]], the space of equivalence classes of Cauchy sequences with $\|[\{y_n\}]\| = \lim_{n} \|y_n\|$, which is a Banach space (Homework 2, Problem 3).
>
> By Proposition [[§9 Completeness#^prop-9-4|§9.4]], it suffices to embed $X$ isometrically and densely in a Banach space.
>
> Now let $Z = L^p([a,b])$, the Lebesgue measurable functions $F$ on $[a,b]$ with $\int_{[a,b]} |F|^p \, dm < \infty$, modulo equality almost everywhere, normed by $\|F\|_{L^p} = \bigl( \int_{[a,b]} |F|^p\, dm \bigr)^{1/p}$; and let $J : X \to L^p([a,b])$ send $f$ to its class. We use three facts from real analysis, cited from real analysis:
> - (R1) For continuous $f$ on $[a,b]$, the Riemann and Lebesgue integrals of $|f|^p$ [[Riemann Integrable Implies Lebesgue Integrable|coincide]]; hence $\|Jf\|_{L^p} = \|f\|_p$. Clearly $J$ is linear.
> - (R2) ([[Riesz–Fischer Theorem|Riesz–Fischer]]) $L^p([a,b])$ is complete for $1 \leq p < \infty$ (Theorem [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-3|§14.3]]).
> - (R3) $C([a,b])$ is dense in $L^p([a,b])$ for $1 \leq p < \infty$ (Theorem [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-4|§14.4]]).
>
> By (R1)–(R3), $J$ is a norm-preserving linear map of $X$ onto a dense subspace of the Banach space $L^p([a,b])$. By Proposition [[§9 Completeness#^prop-9-4|§9.4]], the completion of $(C([a,b]), \|\cdot\|_p)$ is $L^p([a,b])$.

^pf-14-8

*Uses:* [[§9 Completeness#^thm-9-1|§9.1]], [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], [[§14 The Function Spaces Lᵖ(Ω)#^lem-14-6|§14.6]], [[§14 The Function Spaces Lᵖ(Ω)#^lem-14-7|§14.7]], [[§8 Normed Linear Spaces#^def-8-5|Def. §8.5]], [[§9 Completeness#^def-9-1|Def. §9.1]], [[§9 Completeness#^thm-9-3|§9.3]], [[§9 Completeness#^prop-9-4|§9.4]], [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-3|§14.3]], [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-4|§14.4]], [[Riemann Integrable Implies Lebesgue Integrable|551 §15.10]], [[Riesz–Fischer Theorem|551 §19.18]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|551 §19.19]]

![[m556-14-2.svg]]
*The ramps of Step 2 for $n = 2, 4, 8$ on $[a,b]$, with $c$ the midpoint. They differ from one another only near $c$, so they are Cauchy in $L^p$; an $L^p$ limit would have to be $0$ on $[a,c]$ and $1$ on $(c,b]$ — the step function, which is not continuous.*

> [!remark]- Connections
> - The measure-theoretic facts (R1)–(R3): [[§15 The General Lebesgue Integral#^thm-15-10|551 §15.10]], [[Riesz–Fischer Theorem|551 §19.18]], and [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|551 §19.19]](iii) (compactly supported continuous functions dense).
> - The method as a technique: [[Functional Analysis Problem-Solving Techniques#^ex-t9|Technique T9]] (Incompleteness and Identifying the Completion).

> [!remark] Remark
> This is the example to keep in mind for what the abstract construction of the completion does in practice. Started from continuous functions — concrete, classical objects — and measured in the $L^p$ norm, the completion is forced to contain discontinuous and even badly behaved functions, and it is exactly $L^p$. The ramp functions of Step 2 converge in $L^p$ to the class of the step function $\chi_{(c,b]}$, and Step 2 is precisely the statement that this class contains no continuous representative. Read backwards, the proposition says that $L^p[a,b]$ *could* have been *defined* as the completion of $C[a,b]$ in the $L^p$ norm, with no measure theory at all; that is one standard route to the Lebesgue spaces, and it is the definition Lax adopts (§5.1, example (f)), and it explains Wu's remark that “when we write $L^1[a,b]$, intuitively we are taking this norm.”

^rem-14-4
