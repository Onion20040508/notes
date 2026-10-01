---
type: section
subject: "[[Functional Analysis]]"
chapter: 3
section: 10
tags: [functional-analysis, math556]
---
← [[§9 Completeness]] · ↑ [[· 3 Normed Linear Spaces]] · [[§11 Means and Young's Inequality]] →

*Stage: norms — Thread: dimension. In finite dimensions all norms are equivalent (Theorem [[§10 New Normed Spaces from Old#^thm-10-3|§10.3]]); subspaces, direct sums and quotients acquire norms.*

The constructions of [[· 1 Linear Spaces|Chapter 1]] — subspaces, direct sums, quotients — each acquire a natural norm. The first two are immediate; the quotient requires a hypothesis and a proof.

## Equivalent Norms

> [!definition] Definition §10.1: Equivalent Norms
> Let $X$ be a linear space with two norms $\|\cdot\|_1$ and $\|\cdot\|_2$. They are **equivalent** if there are constants $c_1, c_2 > 0$ such that
>
> $$
> c_1 \|x\|_2 \;\le\; \|x\|_1 \;\le\; c_2 \|x\|_2 \qquad \text{for all } x \in X.
> $$
>
> *Lax: §5.1, (5)*

^def-10-1

> [!remark]- Connections
> - The prototype on $\mathbb{R}^n$: [[§13 Some Topological Concepts in Metric Spaces#^prop-13-1|451 §13.1]] (Euclidean vs. max distance), and in topological terms [[§11 Metric Topology#^lem-11-1|590 §11.1]], [[§11 Metric Topology#^thm-11-2|590 §11.2]].

If $B_1$ and $B_2$ denote the closed unit balls of $\|\cdot\|_1$ and $\|\cdot\|_2$, the definition says exactly that $\tfrac{1}{c_2} B_2 \subset B_1 \subset \tfrac{1}{c_1} B_2$: if $\|x\|_1 \le 1$ then $\|x\|_2 \le 1/c_1$, and if $\|x\|_2 \le 1/c_2$ then $\|x\|_1 \le 1$. Each unit ball is squeezed between two scaled copies of the other.

![[m556-10-1.svg]]
*For the maximum and Euclidean norms on $\mathbb{R}^2$ ([[§8 Normed Linear Spaces#^ex-8-1|Ex. §8.1]]), $\|x\|_\infty \le \|x\|_2 \le \sqrt{2}\,\|x\|_\infty$: the disk contains the dashed square and lies inside the solid one.*

The constants must work for all $x$ at once: the condition says that the ratio $\|x\|_1 / \|x\|_2$ is bounded above and below on $X \setminus \{0\}$. Its meaning is topological.

> [!theorem] Proposition §10.1: Equivalent Norms Have the Same Convergence
> Let $\|\cdot\|_1$ and $\|\cdot\|_2$ be equivalent norms on $X$. Then a sequence converges to $x$ in $\|\cdot\|_1$ iff it converges to $x$ in $\|\cdot\|_2$; a sequence is Cauchy for $\|\cdot\|_1$ iff it is Cauchy for $\|\cdot\|_2$; a subset of $X$ is closed for $\|\cdot\|_1$ iff it is closed for $\|\cdot\|_2$; and $(X, \|\cdot\|_1)$ is complete iff $(X, \|\cdot\|_2)$ is.

^prop-10-1

> [!proof]+ Proof
> (Not covered in lecture.) With $c_1\|x\|_2 \le \|x\|_1 \le c_2\|x\|_2$, we have $\|x_n - x\|_1 \le c_2\|x_n - x\|_2$ and $\|x_n - x\|_2 \le c_1^{-1}\|x_n - x\|_1$, so the two notions of convergence coincide; the same inequalities applied to $x_m - x_k$ give the statement about Cauchy sequences. Closedness (Definition [[§8 Normed Linear Spaces#^def-8-6|§8.6]]) and completeness are defined through convergent and Cauchy sequences alone, so they coincide as well.

^pf-10-1

*Uses:* [[§10 New Normed Spaces from Old#^def-10-1|Def. §10.1]], [[§8 Normed Linear Spaces#^def-8-4|Def. §8.4]], [[§8 Normed Linear Spaces#^def-8-5|Def. §8.5]], [[§8 Normed Linear Spaces#^def-8-6|Def. §8.6]], [[§9 Completeness#^def-9-1|Def. §9.1]]

> [!theorem] Proposition §10.2: Continuity of One Norm with Respect to Another
> Let $\|\cdot\|_1$ and $\|\cdot\|_2$ be norms on $X$. Then $\|x_n - x\|_2 \to 0$ implies $\|x_n\|_1 \to \|x\|_1$ for all sequences if and only if there is a constant $C$ with $\|x\|_1 \le C\|x\|_2$ for all $x \in X$. Consequently the two norms are equivalent iff each is continuous with respect to the other in this sense.

^prop-10-2

> [!proof]+ Proof
> ($\Leftarrow$) By the reverse triangle inequality, $\bigl|\,\|x_n\|_1 - \|x\|_1\,\bigr| \le \|x_n - x\|_1 \le C\|x_n - x\|_2 \to 0$.
>
> ($\Rightarrow$) Suppose no such $C$ exists. Then for each $n$ there is $x_n$ with $\|x_n\|_1 > n\|x_n\|_2$; necessarily $x_n \neq 0$, so $\|x_n\|_2 > 0$. Put $z_n = x_n / (n\|x_n\|_2)$. Then $\|z_n\|_2 = 1/n \to 0$, so $z_n \to 0$ in $\|\cdot\|_2$, while $\|z_n\|_1 = \|x_n\|_1 / (n\|x_n\|_2) > 1$, so $\|z_n\|_1 \not\to 0 = \|0\|_1$. This contradicts the continuity. (Not covered in lecture.)

^pf-10-2

*Uses:* [[§8 Normed Linear Spaces#^lem-8-3|§8.3]], [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], [[§10 New Normed Spaces from Old#^def-10-1|Def. §10.1]]

> [!remark] Remark
> Anything defined in terms of convergence cannot tell equivalent norms apart. Conversely, two norms on one set for which the space is complete under one and not under the other cannot be equivalent — as for $\|\cdot\|_\infty$ and $\|\cdot\|_{L^1}$ on $C[a,b]$.

^rem-10-1

> [!theorem] Theorem §10.3: All Norms on a Finite-Dimensional Space are Equivalent
> Let $X$ be a finite-dimensional linear space over $\mathbb{F}$. Any two norms on $X$ are equivalent.
>
> *Source: HW2, Problem 2(a)*

^thm-10-3

> [!proof]+ Proof
> (HW2, Problem 2(a).) Since $X$ is finite dimensional, it has a basis $\{e_1, \ldots, e_n\}$, and every $x \in X$ can be written uniquely as $x = \sum_{i=1}^n a_i e_i$ with $a_i \in \mathbb{F}$. Two norms $\|\cdot\|_a$ and $\|\cdot\|_b$ on $X$ are equivalent, written $\|\cdot\|_a \sim \|\cdot\|_b$, if there are constants $c, C > 0$ with $c\,\|x\|_a \le \|x\|_b \le C\,\|x\|_a$ for all $x$.
>
> **Step 1: equivalence of norms is an equivalence relation.** *Reflexivity:* $1 \cdot \|x\|_a \le \|x\|_a \le 1 \cdot \|x\|_a$. *Symmetry:* suppose $c_1\|x\|_a \le \|x\|_b \le c_2\|x\|_a$ for all $x$, with $c_1, c_2 > 0$. Dividing the right-hand inequality by $c_2$ gives $\frac{1}{c_2}\|x\|_b \le \|x\|_a$, and dividing the left-hand one by $c_1$ gives $\|x\|_a \le \frac{1}{c_1}\|x\|_b$; hence $\frac{1}{c_2}\|x\|_b \le \|x\|_a \le \frac{1}{c_1}\|x\|_b$. *Transitivity:* if $c_1\|x\|_a \le \|x\|_b \le c_2\|x\|_a$ and $d_1\|x\|_b \le \|x\|_c \le d_2\|x\|_b$ for all $x$, with all four constants positive, then
>
> $$
> d_1 c_1\,\|x\|_a \le d_1\,\|x\|_b \le \|x\|_c \le d_2\,\|x\|_b \le d_2 c_2\,\|x\|_a .
> $$
>
> **Step 2: a reference norm.** Define $\|x\|_1 = \sum_{i=1}^n |a_i|$ for $x = \sum_i a_i e_i$. *Positivity:* each $|a_i| \ge 0$, so $\|x\|_1 \ge 0$; if $\|x\|_1 = 0$ then every $a_i = 0$ and $x = 0$; conversely if $x = 0$ then all $a_i = 0$ by uniqueness of the expansion, and $\|x\|_1 = 0$. *Homogeneity:* $kx = \sum_i (k a_i) e_i$, so $\|kx\|_1 = \sum_i |k a_i| = |k|\,\|x\|_1$. *Triangle inequality:* for $x = \sum a_i e_i$, $y = \sum b_i e_i$, $x + y = \sum (a_i + b_i) e_i$ and $\|x + y\|_1 = \sum_i |a_i + b_i| \le \sum_i (|a_i| + |b_i|) = \|x\|_1 + \|y\|_1$. By Step 1 it suffices to prove that an arbitrary norm $\|\cdot\|'$ on $X$ is equivalent to $\|\cdot\|_1$.
>
> **Step 3: the inequality $C_1\|x\|' \le \|x\|_1$.** Fix a norm $\|\cdot\|'$. For each $i$, both $\|e_i\|'$ and $\|e_i\|_1 = 1$ are positive reals, so there is $c_i > 0$ with $c_i\|e_i\|' = \|e_i\|_1 = 1$. The finite set $\{c_1, \ldots, c_n\}$ has a minimum $C_1 = \min_i c_i > 0$, and for every $i$,
>
> $$
> C_1 \|e_i\|' \le c_i \|e_i\|' = 1 = \|e_i\|_1 .
> $$
>
> Multiplying by $|a_i| \ge 0$ and using homogeneity, $C_1\|a_i e_i\|' = C_1|a_i|\,\|e_i\|' \le |a_i|\,\|e_i\|_1 = |a_i|$. For $x = \sum_i a_i e_i$, subadditivity of $\|\cdot\|'$ and the above, summed over $i$, give
>
> $$
> C_1\|x\|' \le C_1 \sum_{i=1}^n \|a_i e_i\|' \le \sum_{i=1}^n |a_i| = \|x\|_1 .
> $$
>
> **Step 4: $\|\cdot\|'$ is continuous on $(X, \|\cdot\|_1)$.** By Step 3, $\|z\|' \le \frac{1}{C_1}\|z\|_1$ for every $z$. Hence, by the reverse triangle inequality for $\|\cdot\|'$,
>
> $$
> \bigl|\,\|x\|' - \|y\|'\,\bigr| \le \|x - y\|' \le \frac{1}{C_1}\,\|x - y\|_1 .
> $$
>
> Given $\varepsilon > 0$, take $\delta = C_1\varepsilon$: if $\|x - y\|_1 < \delta$ then $\bigl|\,\|x\|' - \|y\|'\,\bigr| < \varepsilon$. So $\|\cdot\|' : X \to \mathbb{R}$ is continuous when distances in $X$ are measured by $\|\cdot\|_1$.
>
> **Step 5: the unit sphere of $\|\cdot\|_1$ is sequentially compact.** Let $S = \{x \in X : \|x\|_1 = 1\}$ and let $\{x^{(k)}\} \subset S$, $x^{(k)} = \sum_i a^{(k)}_i e_i$. Each coordinate sequence is bounded, $|a^{(k)}_i| \le \|x^{(k)}\|_1 = 1$. By [[Bolzano–Weierstrass Theorem|Bolzano–Weierstrass]] in $\mathbb{F}$ applied $n$ times — extract a subsequence along which $a^{(k)}_1$ converges, then a further subsequence along which $a^{(k)}_2$ converges, and so on — there is a subsequence $\{x^{(k_r)}\}$ with $a^{(k_r)}_i \to a_i$ for every $i = 1, \ldots, n$. Put $x = \sum_i a_i e_i$. Then $\|x^{(k_r)} - x\|_1 = \sum_i |a^{(k_r)}_i - a_i| \to 0$ (a finite sum of terms tending to $0$), and $\|x\|_1 = \sum_i |a_i| = \lim_r \sum_i |a^{(k_r)}_i| = 1$, so $x \in S$. Thus every sequence in $S$ has a subsequence converging in $\|\cdot\|_1$ to a point of $S$.
>
> **Step 6: $\|\cdot\|'$ attains a positive minimum on $S$.** Let $c = \inf_{x \in S} \|x\|' \ge 0$. Choose $x^{(k)} \in S$ with $\|x^{(k)}\|' \to c$, and by Step 5 a subsequence $x^{(k_r)} \to x^* \in S$ in $\|\cdot\|_1$. By Step 4, $\|x^{(k_r)}\|' \to \|x^*\|'$, so $\|x^*\|' = c$. Since $x^* \in S$ we have $x^* \ne 0$, hence $c = \|x^*\|' > 0$ by positivity of $\|\cdot\|'$.
>
> **Step 7: $c\,\|x\|_1 \le \|x\|'$.** For $x = 0$ both sides vanish. For $x \ne 0$, $x/\|x\|_1 \in S$, so by homogeneity
>
> $$
> \|x\|' = \|x\|_1 \cdot \Bigl\| \frac{x}{\|x\|_1} \Bigr\|' \ge c\,\|x\|_1.
> $$
>
> With Step 3, $c\|x\|_1 \le \|x\|' \le C_1^{-1}\|x\|_1$ for all $x$, i.e. $\|\cdot\|' \sim \|\cdot\|_1$. By Step 1, any two norms on $X$ are equivalent.

^pf-10-3

*Uses:* [[§10 New Normed Spaces from Old#^def-10-1|Def. §10.1]], [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], [[§8 Normed Linear Spaces#^lem-8-3|§8.3]], [[Bolzano–Weierstrass Theorem|451 Bolzano–Weierstrass]]

> [!remark]- Connections
> - The case $X = \mathbb{R}^n$ with the Euclidean and max norms: [[§13 Some Topological Concepts in Metric Spaces#^prop-13-1|451 §13.1]], [[§11 Metric Topology#^thm-11-2|590 §11.2]]; coordinatewise Bolzano–Weierstrass in $\mathbb{R}^n$: [[§13 Some Topological Concepts in Metric Spaces#^thm-13-3|451 §13.3]].
> - Used for $\ell^p$ and compactness: [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^thm-13-5|§13.5]], [[§15 Compactness and the Unit Ball|§15]].

> [!remark] Remark: Finite Dimension is Necessary
> The two inequalities are of different depth. $C_1\|x\|' \le \|x\|_1$ is pure algebra (Step 3): a norm is controlled by its values on a basis. The reverse inequality needs compactness of the unit sphere, which is exactly what fails in infinite dimensions — the unit sphere of $\ell^1$ contains $e_1, e_2, \ldots$ with $\|e_i - e_j\|_1 = 2$, no convergent subsequence — and correspondingly the theorem fails there: on $\ell^1$ the norms $\|\cdot\|_1$ and $\|\cdot\|_2$ are not equivalent (Proposition [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^prop-13-4|§13.4]](c)). Note also what Step 4 shows: an arbitrary norm is continuous for the $\|\cdot\|_1$-topology before we know the two are equivalent; this is the easy direction of Proposition [[§10 New Normed Spaces from Old#^prop-10-2|§10.2]].

^rem-10-2

> [!theorem] Corollary §10.4: Finite-Dimensional Normed Spaces are Complete
> Every finite-dimensional normed linear space is a Banach space.

^cor-10-4

> [!proof]+ Proof
> (Not covered in lecture.) Let $(Y, \|\cdot\|)$ be finite-dimensional with basis $e_1, \ldots, e_n$, and let $\|\cdot\|_1$ be the coordinate norm of Step 2 above. By Theorem [[§10 New Normed Spaces from Old#^thm-10-3|§10.3]] the two norms are equivalent, so by Proposition [[§10 New Normed Spaces from Old#^prop-10-1|§10.1]] it suffices to show that $(Y, \|\cdot\|_1)$ is complete. If $y_k = \sum_i a^{(k)}_i e_i$ is Cauchy for $\|\cdot\|_1$, then $|a^{(k)}_i - a^{(m)}_i| \le \|y_k - y_m\|_1$, so each coordinate sequence is Cauchy in $\mathbb{F}$ and converges to some $a_i$. Put $y = \sum_i a_i e_i \in Y$; then $\|y_k - y\|_1 = \sum_{i=1}^n |a^{(k)}_i - a_i| \to 0$.

^pf-10-4

*Uses:* [[§10 New Normed Spaces from Old#^thm-10-3|§10.3]], [[§10 New Normed Spaces from Old#^prop-10-1|§10.1]], [[§9 Completeness#^def-9-2|Def. §9.2]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|451 §10.8]] (completeness of the scalars)

> [!remark]- Connections
> - Completeness of $\mathbb{R}^n$ with the Euclidean metric: [[§13 Some Topological Concepts in Metric Spaces#^thm-13-2|451 §13.2]]; with $\|\cdot\|_1$, $\|\cdot\|_2$: [[§19 Normed Linear Spaces and Lᵖ Spaces#^ex-19-4|551 Ex. §19.4]].

> [!theorem] Corollary §10.5: Finite-Dimensional Subspaces are Closed
> Every finite-dimensional linear subspace $Y$ of a normed linear space $(X, \|\cdot\|)$ is closed in $X$.
>
> *Source: HW2, Problem 2(b)*

^cor-10-5

> [!proof]+ Proof
> (HW2, Problem 2(b).) By Corollary [[§10 New Normed Spaces from Old#^cor-10-4|§10.4]], $Y$ with the restricted norm is complete, and a complete subset of a normed space is closed (Lemma [[§9 Completeness#^lem-9-2|§9.2]]).

^pf-10-5

*Uses:* [[§10 New Normed Spaces from Old#^cor-10-4|§10.4]], [[§9 Completeness#^lem-9-2|§9.2]], [[§10 New Normed Spaces from Old#^prop-10-6|§10.6]]

> [!remark] Remark: Finite Dimension is Necessary
> The corollary fails for infinite-dimensional subspaces. The finitely supported sequences $c_{00} = \{ a \in \ell : a_i = 0 \text{ for all but finitely many } i \}$ form a subspace of $\ell^p$, $1 \le p < \infty$, which is not closed: for $a \in \ell^p$ the truncations $(a_1, \ldots, a_n, 0, \ldots)$ lie in $c_{00}$ and converge to $a$, since $\sum_{i > n} |a_i|^p \to 0$, while $a = (2^{-i})_{i \ge 1}$, say, is not finitely supported. This is why Theorem [[§10 New Normed Spaces from Old#^thm-10-8|§10.8]] had to assume $Y$ closed.

^rem-10-3

## Subspaces and Direct Sums

> [!theorem] Proposition §10.6: Subspace Norm
> Let $(X, \|\cdot\|)$ be a normed linear space and $Y$ a linear subspace of $X$. Then $(Y, \|\cdot\|)$, with the norm restricted to $Y$, is a normed linear space.
>
> *Lax: §5.1, construction (i)*

^prop-10-6

> [!proof]+ Proof
> The three axioms hold for all $x, y \in X$, hence for all $x, y \in Y$; nothing to prove.

^pf-10-6

*Uses:* [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]]

> [!theorem] Proposition §10.7: Norms on a Direct Sum
> Let $(X, \|\cdot\|_X)$ and $(Y, \|\cdot\|_Y)$ be normed linear spaces. Each of the following is a norm on $X \oplus Y$:
>
> $$\begin{aligned}
> \|(x, y)\|_2 &= \bigl( \|x\|_X^2 + \|y\|_Y^2 \bigr)^{1/2}, \\
> \|(x, y)\|_\infty &= \max\{ \|x\|_X,\ \|y\|_Y \}, \\
> \|(x, y)\|_1 &= \|x\|_X + \|y\|_Y.
> \end{aligned}$$
>
> *Lax: §5.1, construction (ii) and Exercise 1*

^prop-10-7

> [!proof]+ Proof
> (Left as an exercise in lecture.) Write $\|(x,y)\|_*$ for any of the three, and $N_*$ for the corresponding norm on $\mathbb{R}^2$ ($N_2(s,t) = (s^2 + t^2)^{1/2}$, $N_\infty(s,t) = \max\{|s|,|t|\}$, $N_1(s,t) = |s| + |t|$), so that $\|(x,y)\|_* = N_*(\|x\|_X, \|y\|_Y)$. Each $N_*$ is a norm on $\mathbb{R}^2$ (Examples [[§8 Normed Linear Spaces#^ex-8-1|§8.1]] and [[§3 Statement and Motivation#^ex-3-1|§3.1]]) and is *monotone* on the non-negative quadrant: $0 \le s \le s'$, $0 \le t \le t'$ imply $N_*(s,t) \le N_*(s',t')$, as is clear from the three formulas.
>
> *Positivity.* $\|(x,y)\|_* \ge 0$, and it is $0$ iff $N_*(\|x\|_X, \|y\|_Y) = 0$ iff $\|x\|_X = \|y\|_Y = 0$ iff $x = 0$ and $y = 0$ iff $(x,y) = (0,0)$.
>
> *Homogeneity.* $\|(ax, ay)\|_* = N_*(|a|\,\|x\|_X, |a|\,\|y\|_Y) = |a|\,N_*(\|x\|_X, \|y\|_Y) = |a|\,\|(x,y)\|_*$, by homogeneity of $\|\cdot\|_X$, $\|\cdot\|_Y$ and then of $N_*$ (with the scalar $|a| \ge 0$).
>
> *Subadditivity.* By subadditivity in $X$ and $Y$, $\|x + x'\|_X \le \|x\|_X + \|x'\|_X$ and $\|y + y'\|_Y \le \|y\|_Y + \|y'\|_Y$. By monotonicity and then subadditivity of $N_*$ on $\mathbb{R}^2$,
>
> $$
> \begin{aligned}
> \|(x,y) + (x',y')\|_* &= N_*\bigl(\|x+x'\|_X, \|y+y'\|_Y\bigr) \le N_*\bigl(\|x\|_X + \|x'\|_X,\ \|y\|_Y + \|y'\|_Y\bigr) \\
> &\le N_*(\|x\|_X, \|y\|_Y) + N_*(\|x'\|_X, \|y'\|_Y) = \|(x,y)\|_* + \|(x',y')\|_*.
> \end{aligned}
> $$

^pf-10-7

*Uses:* [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], [[§8 Normed Linear Spaces#^ex-8-1|Ex. §8.1]], [[§3 Statement and Motivation#^ex-3-1|Ex. §3.1]], [[§1 Linear Spaces#^def-1-4|Def. §1.4]]

> [!remark]- Connections
> - The underlying linear space $X \oplus Y = X \times Y$: [[§1 Linear Spaces#^prop-1-3|§1.3]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-87|LADR 3.87]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-89|LADR 3.89]].

These three norms are equivalent to one another (the constants are the ones comparing $\|\cdot\|_1, \|\cdot\|_2, \|\cdot\|_\infty$ on $\mathbb{R}^2$), so which one is used is a matter of convenience. One can equally use the $p$-norm $(\|x\|_X^p + \|y\|_Y^p)^{1/p}$.

## The Quotient Norm

For a quotient $X / Y$, an equivalence class $[x] = x + Y$ contains many elements, each with its own norm. The natural choice of a norm for the class is the smallest length available in it.

> [!theorem] Theorem §10.8: Quotient Norm
> Let $(X, \|\cdot\|)$ be a normed linear space and $Y$ a *closed* linear subspace of $X$. For $[x] \in X / Y$ define
>
> $$
> \bigl\| [x] \bigr\| := \inf_{x' \in [x]} \|x'\| = \inf_{y \in Y} \|x + y\|.
> $$
>
> Then this is a norm on $X / Y$.
>
> *Lax: §5.1, Thm 1*

^thm-10-8

![[m556-10-2.svg]]
*The quotient norm in the plane: the classes are the translates of $Y$ (gray, with $[x]$ in red), and $\|[x]\|$ is the norm of the point $x'$ of $[x]$ closest to $0$.*

The classes are the parallel translates of $Y$; $\|[x]\|$ is the distance from the origin to the translate $[x]$, i.e. the norm of its closest point. With an inner product that point would be the foot of the perpendicular from $0$ (dashed); without one there is no perpendicular, the infimum need not be attained, and only the number $\inf \|x'\|$ is available. This is the same substitution of “quotient” for “orthogonal complement” as in [[§1 Linear Spaces#Quotient Spaces|§1]].

> [!proof]+ Proof
> $\|[x]\|$ is well defined: the set $\{\|x'\| : x' \in [x]\}$ is nonempty and bounded below by $0$, so its infimum is a real number $\ge 0$, and it depends only on the class, not on the representative $x$, since the set does. So $\|\cdot\| : X/Y \to \mathbb{R}_+$.
>
> **Homogeneity.** Let $x_0 \in X$ and $a \in \mathbb{F}$. If $a = 0$ then $[a x_0] = [0] = Y$, and $\inf_{y \in Y} \|y\| = 0$ (attained at $y = 0$), which equals $|0|\,\|[x_0]\|$. If $a \ne 0$: since $Y$ is a subspace, $y \in Y$ iff $y/a \in Y$, so
>
> $$
> [a x_0] = \{ a x_0 + y : y \in Y \} = \{ a(x_0 + y') : y' \in Y \}
> $$
>
> (substitute $y = a y'$). Hence, by homogeneity of the norm on $X$ and the fact that constants pull out of infima,
>
> $$
> \|[a x_0]\| = \inf_{y' \in Y} \|a(x_0 + y')\| = \inf_{y' \in Y} |a|\,\|x_0 + y'\| = |a| \inf_{y' \in Y} \|x_0 + y'\| = |a|\, \|[x_0]\|.
> $$
>
> (Wu described this step as “clear” and left the writing to us.)
>
> **Subadditivity.** Let $[x], [y] \in X/Y$; we show $\|[x + y]\| \le \|[x]\| + \|[y]\|$. Fix $\varepsilon > 0$. Since $\|[x]\|$ is the greatest lower bound of $\{\|x'\| : x' \in [x]\}$, the number $\|[x]\| + \varepsilon$ is not a lower bound, so there is $x_0 \in [x]$ with
>
> $$
> \|x_0\| \le \|[x]\| + \varepsilon;
> $$
>
> likewise there is $y_0 \in [y]$ with $\|y_0\| \le \|[y]\| + \varepsilon$. Now $x_0 + y_0 \in [x + y]$: indeed $(x_0 + y_0) - (x + y) = (x_0 - x) + (y_0 - y) \in Y$, both summands lying in $Y$. Therefore, by definition of the infimum and subadditivity of $\|\cdot\|$ on $X$,
>
> $$
> \|[x + y]\| \le \|x_0 + y_0\| \le \|x_0\| + \|y_0\| \le \|[x]\| + \|[y]\| + 2\varepsilon.
> $$
>
> Since $\varepsilon > 0$ was arbitrary, $\|[x+y]\| \le \|[x]\| + \|[y]\|$.
>
> **Positivity.** Non-negativity was noted above. It remains to show that $\|[x]\| = 0$ implies $[x] = [0]$, i.e. $x \in Y$; this is where closedness of $Y$ is used. Suppose $\|[x]\| = \inf_{x' \in [x]} \|x'\| = 0$. Then there is a sequence $x_n \in [x]$ with $\|x_n\| \to 0$ (an infimum is approached by elements of the set). Since $x_n \in [x]$, we have $x_n - x \in Y$ for every $n$. And
>
> $$
> \bigl\| (x_n - x) - (-x) \bigr\| = \|x_n\| \to 0,
> $$
>
> so the sequence $\{x_n - x\} \subset Y$ converges to $-x$. Because $Y$ is closed, $-x \in Y$, hence $x \in Y$ (subspace), hence $[x] = [0]$.

^pf-10-8

*Uses:* [[§1 Linear Spaces#^def-1-7|Def. §1.7]], [[§1 Linear Spaces#^prop-1-6|§1.6]], [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], [[§8 Normed Linear Spaces#^def-8-6|Def. §8.6]], [[Characterization of the Supremum|451 Characterization of the Supremum]]

> [!remark]- Connections
> - The quotient space itself: [[§1 Linear Spaces#^prop-1-6|§1.6]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-103|LADR 3.103]]; a seminorm made into a norm by passing to a quotient: [[§19 Normed Linear Spaces and Lᵖ Spaces#^ex-19-3|551 Ex. §19.3]] ($BV$ modulo constants).
> - With an inner product the infimum is attained at the foot of the perpendicular: [[§18 Projection and Orthogonal Decomposition#^thm-18-2|§18.2]], [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]].

> [!theorem] Proposition §10.9: The Quotient Seminorm; Closedness is Necessary
> Let $Y$ be any linear subspace of a normed linear space $X$, closed or not. Then $\|[x]\| = \inf_{y \in Y}\|x + y\|$ is a seminorm on $X/Y$, and it is a norm if and only if $Y$ is closed.

^prop-10-9

> [!proof]+ Proof
> Well-definedness, homogeneity and subadditivity were proved in Theorem [[§10 New Normed Spaces from Old#^thm-10-8|§10.8]] without using closedness, so $\|\cdot\|$ is a seminorm; if $Y$ is closed it is a norm by that theorem. Conversely, suppose $Y$ is not closed: there are $y_n \in Y$ with $y_n \to x$ for some $x \notin Y$. Then $x - y_n \in [x]$, so $\|[x]\| \le \|x - y_n\| \to 0$, i.e. $\|[x]\| = 0$, while $[x] \neq [0]$ because $x \notin Y$. So positivity fails. (Not stated in lecture.)

^pf-10-9

*Uses:* [[§10 New Normed Spaces from Old#^thm-10-8|§10.8]], [[§8 Normed Linear Spaces#^def-8-2|Def. §8.2]], [[§8 Normed Linear Spaces#^def-8-6|Def. §8.6]]
