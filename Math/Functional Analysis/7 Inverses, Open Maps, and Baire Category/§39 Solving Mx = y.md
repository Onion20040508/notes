---
type: section
subject: "[[Functional Analysis]]"
chapter: 7
section: 39
tags: [functional-analysis, math556]
---
← [[§38 ℝⁿ, Cᵐ and Lᵖ]] · ↑ [[· 7 Inverses, Open Maps, and Baire Category]] · [[§40 The Baire Category Theorem]] →

*Stage: maps — Thread: completeness. Existence, uniqueness and stability for a bounded linear equation; the first two are algebra, the third needs completeness.*

> [!remark] Remark: Midterm Remarks
> Wu began with two midterm problems.
>
> 1. *The completion of $C^1[a,b]$ under $\|f\| = \max_{[a,b]} |f|$ is $C[a,b]$.* All that was needed: $C^1[a,b]$ is dense in $(C[a,b], \|\cdot\|_\infty)$, because already the polynomials are dense in this norm (Weierstrass), and $C[a,b]$ is complete (Theorem [[§12 Completeness#^thm-12-1|§12.1]]); so $C[a,b]$ is the completion (Proposition [[§13 The Completion of a Normed Space#^prop-13-2|§13.2]]). Wu: the abstract completion by equivalence classes of Cauchy sequences is not needed in practice; one identifies a complete space in which the given space is dense.
> 2. *If $\{e_\alpha\}_{\alpha \in \Lambda}$ are nonzero vectors of a Hilbert space with $(x, y) = \sum_{\alpha \in \Lambda} (x, e_\alpha)\, \overline{(y, e_\alpha)}$ for all $x, y$, then $\{e_\alpha\}$ is a complete orthonormal set.* Most solutions proved completeness but not orthonormality, which was not assumed. A student asked about $e_\alpha = 0$; Wu: the vectors are assumed nonzero (a zero vector cannot belong to an orthonormal set). The full problem is on this week's homework.

^rem-39-1

## Three Questions

Let $X, Y$ be normed linear spaces and $M : X \to Y$ a bounded linear map (without boundedness “life would be too difficult”). Consider the equation

$$
M x = y . \tag{$\ast$}
$$

1. *Existence.* For given $y \in Y$, is there a solution $x \in X$ of $(\ast)$? For every $y$: yes if and only if $R(M) = Y$.
2. *Uniqueness.* Is the solution unique? Yes if and only if $N(M) = \{0\}$.
3. *Stability.* Assume $M : X \to Y$ is one-to-one and onto, so that $M^{-1} : Y \to X$ exists and $(\ast)$ is solved by $x = M^{-1} y$. Does a small error in $y$ imply a small error in $x$? Yes if $M^{-1}$ is continuous.

> [!definition] Definition §39.1: Range; Null Space
> Let $M : X \to Y$ be a linear map. The **range** of $M$ is $R(M) = \{ Mx : x \in X \}$. The **null space** (or **kernel**, or null set) of $M$ is $N(M) = \{ x \in X : Mx = 0 \}$.

^def-39-1

(For (2): if $Mx_1 = Mx_2 = y$ then $M(x_1 - x_2) = 0$, so $N(M) = \{0\}$ forces $x_1 = x_2$; conversely, if $0 \ne w \in N(M)$ and $Mx = y$, then $x + w$ is a second solution. (1) is the definition of $R(M)$.) Question (3) is the one that matters in practice: data are never exact, and one hopes that the computed solution is close to the true one. Continuity of $M^{-1}$ is exactly this: for every $\varepsilon > 0$ there is $\delta > 0$ such that $\|y_1 - y_2\| < \delta$ implies $\|M^{-1} y_1 - M^{-1} y_2\| < \varepsilon$. This is called **stability**. In finite dimensions $M$ is a matrix and all three questions are linear algebra; the first two can be fixed in general, as follows, while the third is hard.

## Quotienting Out the Null Space

> [!theorem] Theorem §39.1: Null Space and the Induced Map
> Let $X, Y$ be normed linear spaces and $M \in \mathcal{L}(X, Y)$. Then:
>
> 1. The null space $N = N(M)$ is a closed linear subspace of $X$.
> 2. There is a natural definition of $M$ on $X/N$: the map $M_0 : X/N \to Y$, $M_0[x] = Mx$, is a bounded linear map and is one-to-one, and $M_0 : X/N \to R(M)$ is one-to-one and onto. Moreover $\|M_0\| = \|M\|$.

^thm-39-1

> [!proof]+ Proof
> (1)
> *Linear subspace:* $M0 = 0$, and if $Mx_1 = Mx_2 = 0$ then $M(c_1 x_1 + c_2 x_2) = c_1 Mx_1 + c_2 Mx_2 = 0$. *Closed:* if $x_n \in N$ and $x_n \to x_0$, then, $M$ being bounded and hence continuous (Proposition [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-1|§26.1]]), $0 = Mx_n \to Mx_0$, so $Mx_0 = 0$.
>
> (2) Since $N$ is closed, $X/N$ is a normed linear space (Theorem [[§14 New Normed Spaces from Old#^thm-14-8|§14.8]]): its elements are the equivalence classes $[x] = \{ x + w : w \in N \}$, $x \in X$, with $[x_1] = [x_2]$ if and only if $x_1 - x_2 \in N$, and
>
> $$
> \|[x]\| = \inf_{x' \in [x]} \|x'\| = \inf_{w \in N} \|x + w\| .
> $$
>
> Define $M_0[x] = Mx$ for all $x \in X$.
>
> **Well defined, and one-to-one.** Since $M$ is linear,
>
> $$
> M x_1 = M x_2 \iff M(x_1 - x_2) = 0 \iff x_1 - x_2 \in N \iff [x_1] = [x_2] .
> $$
>
> The implication “$\Leftarrow$” says the value $Mx$ does not depend on the representative $x$ of $[x]$: $M_0$ is well defined. The implication “$\Rightarrow$” says $M_0[x_1] = M_0[x_2]$ forces $[x_1] = [x_2]$: $M_0$ is one-to-one.
>
> **Linear.**
> $M_0(c_1[x_1] + c_2[x_2]) = M_0[c_1 x_1 + c_2 x_2] = M(c_1 x_1 + c_2 x_2) = c_1 M_0[x_1] + c_2 M_0[x_2]$.
>
> **Bounded.** For every $w \in N$, $Mx = M(x + w)$, so
>
> $$
> \|M_0[x]\|_Y = \|Mx\|_Y = \|M(x + w)\|_Y \le \|M\|\, \|x + w\|_X \qquad \text{for all } w \in N .
> $$
>
> Taking the infimum over $w \in N$,
>
> $$
> \|M_0[x]\|_Y \le \|M\| \inf_{w \in N} \|x + w\|_X = \|M\|\, \|[x]\| .
> $$
>
> So $M_0 : X/N \to Y$ is bounded, and $\|M_0\| \le \|M\|$.
>
> **Onto $R(M)$.** The values of $M_0$ are the values $Mx$ of $M$, so $M_0(X/N) = R(M)$; with one-to-one, $M_0 : X/N \to R(M)$ is a bijection.
>
> **$\|M_0\| = \|M\|$.**
> Since $\|[x]\| \le \|x\|$ (take $w = 0$ in the infimum), for every $x \in X$
>
> $$
> \|Mx\| = \|M_0[x]\| \le \|M_0\|\, \|[x]\| \le \|M_0\|\, \|x\| ,
> $$
>
> so $\|M\| = \sup_{\|x\| = 1} \|Mx\| \le \|M_0\|$. With the previous step, $\|M_0\| = \|M\|$.

^pf-39-1

*Uses:* [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-1|§26.1]], [[§14 New Normed Spaces from Old#^thm-14-8|§14.8]]

> [!remark] Remark: The First Isomorphism Theorem, with Norms
> Algebraically, Theorem [[§39 Solving Mx = y#^thm-39-1|§39.1]](2) is the first isomorphism theorem of linear algebra: $X/N(M) \cong R(M)$. Wu: the null space often represents a symmetry of the problem, and quotienting it out removes the non-uniqueness; restricting the target to $R(M)$ removes the non-existence. What the theorem does not give is a bounded inverse: $M_0^{-1} : R(M) \to X/N$ is linear but need not be bounded, and $R(M)$ need not be closed in $Y$. If $X$ and $Y$ are Banach spaces and $R(M)$ is closed, then $X/N$ and $R(M)$ are Banach spaces, and Banach's theorem below shows that $M_0^{-1}$ is bounded. So question (3) is the real one.

^rem-39-2

![[m556-39-1.svg]]

Theorem [[§39 Solving Mx = y#^thm-39-1|§39.1]] as a diagram: $M$ factors as the quotient map $x \mapsto [x]$, the one-to-one and onto map $M_0$, and the inclusion of $R(M)$ in $Y$. Passing to $X/N(M)$ removes non-uniqueness, shrinking the target to $R(M)$ removes non-existence; whether $M_0^{-1}$ is bounded is question (3).

## Banach's Theorem and Open Maps

> [!theorem] Theorem §39.2: Banach's Inverse Mapping Theorem
> Let $X, Y$ be Banach spaces and $M : X \to Y$ a bounded linear map. Assume $M$ is one-to-one and onto. Then $M^{-1} : Y \to X$ is also a bounded linear map.
>
> *Lax: §15.5, Thm 11*

^thm-39-2

The proof will be given after the Baire category theorem ([[§41 The Open Mapping Theorem and Its Consequences#^pf-39-2|§41]], Lecture 16). Wu stressed that the inverse is *not* assumed to be bounded, and that it is important that *both* $X$ and $Y$ are Banach spaces.
($M^{-1}$ is linear: given $y_1, y_2 \in Y$, put $x_i = M^{-1} y_i$; then $M(c_1 x_1 + c_2 x_2) = c_1 y_1 + c_2 y_2$, so $M^{-1}(c_1 y_1 + c_2 y_2) = c_1 x_1 + c_2 x_2$.) So the content of the theorem is boundedness, i.e. continuity, of $M^{-1}$, and continuity can be expressed through open sets:

$$
\begin{aligned}M^{-1} : Y \to X \text{ bounded} &\iff M^{-1} \text{ continuous} \\
&\iff \text{for every open } O \subset X,\ (M^{-1})^{-1}(O) = M(O) \text{ is open in } Y .\end{aligned}
$$

> [!theorem] Lemma §39.3: Continuity by Open Sets
> A map $f$ between metric spaces is (sequentially) continuous if and only if $f^{-1}(U)$ is open for every open $U$.

^lem-39-3

> [!proof]+ Proof
> (Not covered in lecture; MATH 451.) ($\Rightarrow$) Let $U$ be open and $x \in f^{-1}(U)$. If no ball $B(x, 1/n)$ were contained in $f^{-1}(U)$, there would be $x_n$ with $d(x_n, x) < 1/n$ and $f(x_n) \notin U$; then $x_n \to x$, so $f(x_n) \to f(x) \in U$, and since $U$ is open, $f(x_n) \in U$ for large $n$ — a contradiction. ($\Leftarrow$) Let $x_n \to x$ and $\varepsilon > 0$. The set $f^{-1}(B(f(x), \varepsilon))$ is open and contains $x$, so it contains some $B(x, \delta)$; for large $n$, $x_n \in B(x, \delta)$, so $d(f(x_n), f(x)) < \varepsilon$.

^pf-39-3

> [!definition] Definition §39.2: Open Map
> Let $X, Y$ be normed linear spaces (or metric spaces). A map $M : X \to Y$ is **open** if for every open $O \subset X$ the image $M(O)$ is open in $Y$.
>
> *Lax: §15.5, Thm 10 (the open mapping principle)*

^def-39-2

So a bounded linear bijection $M$ has a bounded inverse exactly when $M$ is an open map, and Banach's theorem is a consequence of the open mapping theorem: *if $X, Y$ are Banach spaces and $M : X \to Y$ is a bounded linear map that is one-to-one and onto, then $M$ is open*. This is what will be proved.
(The standard open mapping theorem assumes only that $M$ is onto; one-to-one is needed only to speak of $M^{-1}$.)

## Closed Maps

> [!definition] Definition §39.3: Closed Map
> Let $X, Y$ be normed linear spaces and let $D(M) \subset X$ be the domain of a linear map $M$ (a linear subspace on which $M$ is defined, possibly not all of $X$). $M : D(M) \to Y$ is a **closed map** if its **graph**
>
> $$
> G(M) = \{ (x, Mx) : x \in D(M) \}
> $$
>
> is a closed set in $X \times Y$. That is: for any sequence $\{x_n\}_{n=1}^\infty$ in $D(M)$, if $x_n \to x_0$ in $X$ and $Mx_n \to y_0$ in $Y$, then $x_0 \in D(M)$ and $y_0 = Mx_0$.
>
> *Lax: §15.5, definition before Thm 12*

^def-39-3

(Here $X \times Y$ carries one of the equivalent norms of Proposition [[§14 New Normed Spaces from Old#^prop-14-7|§14.7]], say $\|(x, y)\| = \|x\|_X + \|y\|_Y$, so that $(x_n, y_n) \to (x_0, y_0)$ if and only if $x_n \to x_0$ and $y_n \to y_0$. A set is closed if it contains the limits of its convergent sequences (Definition [[§11 Normed Linear Spaces#^def-11-6|§11.6]]); for the graph, the limit $(x_0, y_0)$ of $(x_n, Mx_n)$ lies in $G(M)$ exactly when $x_0 \in D(M)$ and $y_0 = Mx_0$. In words: if a sequence in the graph has a limit, the limit is in the graph.)

> [!example] Example §39.1: Continuous Maps are Closed
> If $M : X \to Y$ is continuous (with $D(M) = X$), then $M$ is closed: if $x_n \to x_0$, continuity gives $Mx_n \to Mx_0$, and limits are unique, so $y_0 = Mx_0$.
> The domain matters: for $D(M)$ not closed, a continuous $M$ need not be closed. For example, let $D(M)$ be the polynomials in $X = Y = C[0,1]$ with the maximum norm, and $Mx = x$. The Taylor polynomials $x_n$ of $e^t$ converge to $e^t$ uniformly, and so do $Mx_n = x_n$, but $e^t \notin D(M)$.

^ex-39-1

![[m556-39-2.svg]]

Closedness of a graph, in a picture. Left: the points $(x_n, Mx_n)$ of the graph converge, and the limit lies on the graph. Right: the example above, $Mx = x$ on the polynomials in $C[0,1]$; the Taylor polynomials $x_n$ of $e^t$ give points $(x_n, x_n)$ of the graph converging to $(e^t, e^t)$, which is missing, since $e^t$ is not a polynomial. $M$ is continuous but not closed: its domain is not closed.

> [!remark] Remark: Why Not “Closed Sets to Closed Sets”
> A student asked why a closed map is not defined, by analogy with open maps, as one taking closed sets to closed sets. Wu: that is a different notion, not equivalent to this one, and it is not what will be used; the graph definition is.
> For instance, the projection $P(x, y) = x$ from $\mathbb{R}^2$ to $\mathbb{R}$ is continuous, hence closed in the graph sense, but it maps the closed set $\{ (x, y) : xy = 1 \}$ onto $\mathbb{R} \setminus \{0\}$, which is not closed.

^rem-39-3

A closed map need not be continuous. Wu: this is why one cares about such a weak notion — differentiation, the most important operator in analysis, is not bounded, but it is closed.

> [!example] Example §39.2: Differentiation is Closed
> Let $X = Y = C[0,1]$ with $\|x\| = \max_{t \in [0,1]} |x(t)|$, and
>
> $$
> (Mx)(t) = \frac{d}{dt}\, x(t) = x'(t), \qquad D(M) = C^1[0,1] .
> $$
>
> Then $M : D(M) \to Y$ is a closed map. It is linear, and it is not bounded (homework; compare Proposition [[§30 Boundedness and Continuity#^prop-30-3|§30.3]]).

^ex-39-2

> [!proof]+ Proof
> Let $(x_n, x_n')$ be a sequence in $G(M)$, and assume $(x_n, x_n') \to (x_0, y_0) \in C[0,1] \times C[0,1]$. We want $y_0 = x_0'$, i.e. $x_0 \in C^1[0,1]$ and $x_0' = y_0$.
>
> Let $y_n = x_n' \in C[0,1]$; by assumption $\{x_n'\}$ converges in $C[0,1]$ to $y_0$, i.e.
>
> $$
> \max_{t \in [0,1]} |x_n'(t) - y_0(t)| \to 0 \qquad (n \to \infty) .
> $$
>
> Let
>
> $$
> \bar x(t) = \int_0^t y_0(s)\, ds ;
> $$
>
> we want to show $\bar x(t) = x_0(t) - x_0(0)$. For each fixed $t \in [0,1]$,
>
> $$
> \Bigl| \int_0^t \bigl( x_n'(s) - y_0(s) \bigr)\, ds \Bigr| \le \int_0^t |x_n'(s) - y_0(s)|\, ds \le \max_{s \in [0,1]} |x_n'(s) - y_0(s)| ,
> $$
>
> since $t \le 1$; taking the supremum over $t$,
>
> $$
> \sup_{t \in [0,1]} \Bigl| \int_0^t \bigl( x_n'(s) - y_0(s) \bigr)\, ds \Bigr| \le \max_{s \in [0,1]} |x_n'(s) - y_0(s)| \to 0 .
> $$
>
> But $x_n \in C^1[0,1]$, so by the fundamental theorem of calculus
>
> $$
> \int_0^t \bigl( x_n'(s) - y_0(s) \bigr)\, ds = x_n(t) - x_n(0) - \bar x(t) .
> $$
>
> Now also $\max_{[0,1]} |x_n(t) - x_0(t)| \to 0$, so $x_n(t) - x_n(0) - \bar x(t) \to x_0(t) - x_0(0) - \bar x(t)$ for each $t$. Limits are unique, so $x_0(t) - x_0(0) - \bar x(t) = 0$:
>
> $$
> x_0(t) = x_0(0) + \bar x(t) = x_0(0) + \int_0^t y_0(s)\, ds \qquad \text{for all } t \in [0,1] .
> $$
>
> Since $y_0$ is continuous, the fundamental theorem of calculus gives $x_0 \in C^1[0,1]$ and $x_0'(t) = y_0(t)$.

^pf-ex-39-2

> [!remark] Remark: Which $C^1$; the Graph Norm
> A student asked whether $C^1$ is meant classically; Wu: yes, classical $C^1$. Asked why the domain is $C^1$ when there are differentiable functions that are not $C^1$: the domain may be chosen smaller than the largest possible one, “as long as I don't make it larger”; here only $C^1$ matters.
> The proof is the argument that $C^1[a,b]$ is complete in the norm $\max|f| + \max|f'|$ (Part 2 of the proof of Proposition [[§13 The Completion of a Normed Space#^prop-13-4|§13.4]]). That is no coincidence: a linear map is closed exactly when its domain is complete in the *graph norm* $\|x\| + \|Mx\|$, provided $X$ and $Y$ are complete. Note that $D(M) = C^1[0,1]$ is not closed in $C[0,1]$ (it is dense), which is how a closed map can fail to be continuous.

^rem-39-4
