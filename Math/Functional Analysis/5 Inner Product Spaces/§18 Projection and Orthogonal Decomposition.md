---
type: section
subject: "[[Functional Analysis]]"
chapter: 5
section: 18
tags: [functional-analysis, math556]
---
← [[§17 Cauchy–Schwarz and the Induced Norm]] · ↑ [[· 5 Inner Product Spaces]] · [[§19 Bounded Linear Functionals and the Riesz Representation Theorem]] →

*Stage: inner products — Threads meet: convexity $\times$ completeness. Closest points; the orthogonal complement replaces the quotient of [[§1 Linear Spaces#Quotient Spaces|§1]].*

Everything from here on uses completeness, and the results are the ones for which Hilbert spaces are named. Wu's comment on the method: much of what is proved below is familiar from $\mathbb{R}^n$, and the proofs there never used finite-dimensionality — so they go through unchanged. The one new ingredient is that a closest point must be *produced* as a limit, which is where completeness enters.

## Continuity of the Inner Product

> [!theorem] Lemma §18.1: The Inner Product is Continuous
> Let $(X, (\cdot,\cdot))$ be an inner product space. If $x_n \to x_0$ and $y_n \to y_0$ in $X$, then $(x_n, y_n) \to (x_0, y_0)$ in $\mathbb{F}$.
>
> *Lax: §6.1, Exercise 2*

^lem-18-1

> [!proof]+ Proof
> Insert $(x_0, y_n)$ and use sesquilinearity in each slot:
>
> $$
> (x_n, y_n) - (x_0, y_0) = (x_n - x_0,\, y_n) + (x_0,\, y_n - y_0).
> $$
>
> By the triangle inequality in $\mathbb{F}$ and Cauchy–Schwarz (Theorem [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|§17.1]]),
>
> $$
> \bigl| (x_n, y_n) - (x_0, y_0) \bigr| \le \|x_n - x_0\|\,\|y_n\| + \|x_0\|\,\|y_n - y_0\| .
> $$
>
> The second term tends to $0$ because $\|y_n - y_0\| \to 0$ and $\|x_0\|$ is a fixed number. For the first term, $\|x_n - x_0\| \to 0$, and the factor $\|y_n\|$ is bounded: $\|y_n\| \le \|y_n - y_0\| + \|y_0\| \le M$ for some $M$, since a sequence tending to $0$ is bounded. So the first term is at most $M\|x_n - x_0\| \to 0$.

^pf-18-1

*Uses:* [[§16 Definition and Examples#^def-16-1|Def. §16.1]], [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|§17.1]], [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-2|§17.2]], [[§8 Normed Linear Spaces#^def-8-4|Def. §8.4]]

> [!remark] Remark
> The point Wu made in class: the factor $\|y_n\|$ cannot be dropped and cannot a priori be assumed bounded; that it is bounded follows from convergence of $y_n$, by subadditivity. Continuity in each variable separately ($x_n \to x_0$ with $y$ fixed) is the special case $y_n = y_0$, and is what is used below. Continuity of the norm (Proposition [[§8 Normed Linear Spaces#^prop-8-4|§8.4]]) is the case $y_n = x_n$, $y_0 = x_0$.

^rem-18-1

## The Projection Theorem

> [!theorem] Theorem §18.2: Closest Point in a Closed Convex Set
> Let $H$ be a Hilbert space and $K \subset H$ a nonempty closed convex subset. For every $x_0 \in H$ there is a unique $y_0 \in K$ such that
>
> $$
> \|x_0 - y_0\| = \operatorname{dist}(x_0, K) := \inf_{y \in K} \|x_0 - y\| .
> $$
>
> *Lax: §6.2, Thm 2*

^thm-18-2

![[m556-18-1.svg]]
*A minimizing sequence $y_n \in K$ (gray dashes) with $\|x_0 - y_n\| \to \operatorname{dist}(x_0, K)$, converging to the closest point $y_0$ (red). The dotted arc is the sphere of radius $\operatorname{dist}(x_0, K)$ about $x_0$: it touches $K$ only at $y_0$. The proof has to produce $y_0$ as a limit, which is where completeness and closedness enter.*

> [!proof]+ Proof
> If $x_0 \in K$, take $y_0 = x_0$; it is unique since $\|x_0 - y\| = 0$ forces $y = x_0$. So assume $x_0 \notin K$ and put $d = \operatorname{dist}(x_0, K)$.
>
> **Step 1: $d > 0$.** If $d = 0$ there would be $y_n \in K$ with $\|x_0 - y_n\| \to 0$, i.e. $y_n \to x_0$, and closedness of $K$ would give $x_0 \in K$.
>
> **Step 2: a minimizing sequence.** Since $d$ is the greatest lower bound of $\{\|x_0 - y\| : y \in K\}$, for each $m \in \mathbb{N}$ there is $y_m \in K$ with
>
> $$
> d^2 \le \|x_0 - y_m\|^2 < d^2 + \frac{1}{m}. \tag{5.2}
> $$
>
> (The first inequality holds for every point of $K$.) We show $\{y_m\}$ is Cauchy; it then converges by completeness of $H$, and its limit lies in $K$ by closedness.
>
> **Step 3: Cauchy, via the parallelogram law.** Fix $m, n$. Apply the parallelogram law (Proposition [[§17 Cauchy–Schwarz and the Induced Norm#^prop-17-3|§17.3]](a)) to $a = x_0 - y_m$ and $b = x_0 - y_n$, so that $a + b = 2x_0 - (y_m + y_n)$ and $a - b = y_n - y_m$:
>
> $$
> \|2x_0 - (y_m + y_n)\|^2 + \|y_n - y_m\|^2 = 2\|x_0 - y_m\|^2 + 2\|x_0 - y_n\|^2 .
> $$
>
> The first term is $4\,\bigl\| x_0 - \tfrac{y_m + y_n}{2} \bigr\|^2$, and the midpoint $\tfrac{y_m + y_n}{2}$ lies in $K$ by convexity, so this term is at least $4d^2$. Rearranging and using (5.2),
>
> $$
> \|y_n - y_m\|^2 = 2\|x_0 - y_m\|^2 + 2\|x_0 - y_n\|^2 - 4\,\Bigl\| x_0 - \frac{y_m + y_n}{2} \Bigr\|^2 < 2\Bigl( d^2 + \frac1m \Bigr) + 2\Bigl( d^2 + \frac1n \Bigr) - 4d^2 = \frac2m + \frac2n ,
> $$
>
> which tends to $0$ as $m, n \to \infty$. So $\{y_m\}$ is Cauchy.
>
> **Step 4: the limit is a closest point.** By completeness there is $y_0 \in H$ with $y_m \to y_0$, and $y_0 \in K$ because $K$ is closed. By continuity of the norm (Proposition [[§8 Normed Linear Spaces#^prop-8-4|§8.4]]), $x_0 - y_m \to x_0 - y_0$ gives
>
> $$
> \|x_0 - y_0\|^2 = \lim_{m \to \infty} \|x_0 - y_m\|^2 = d^2 ,
> $$
>
> the last equality by (5.2). (Wu noted at this point that a continuity lemma was needed and supplied Lemma [[§18 Projection and Orthogonal Decomposition#^lem-18-1|§18.1]]; continuity of the norm suffices here.)
>
> **Step 5: uniqueness.** Let $y_0, y_1 \in K$ both satisfy $\|x_0 - y_0\| = \|x_0 - y_1\| = d$. The parallelogram law with $a = x_0 - y_0$, $b = x_0 - y_1$ gives
>
> $$
> \|2x_0 - (y_0 + y_1)\|^2 + \|y_0 - y_1\|^2 = 2d^2 + 2d^2 = 4d^2 .
> $$
>
> As in Step 3, the first term is $4\|x_0 - \tfrac{y_0 + y_1}{2}\|^2 \ge 4d^2$, since the midpoint is in $K$. So $\|y_0 - y_1\|^2 \le 0$, i.e. $y_0 = y_1$.

^pf-18-2

*Uses:* [[§17 Cauchy–Schwarz and the Induced Norm#^def-17-1|Def. §17.1]], [[§17 Cauchy–Schwarz and the Induced Norm#^prop-17-3|§17.3]], [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Def. §2.3]], [[§8 Normed Linear Spaces#^def-8-5|Def. §8.5]], [[§8 Normed Linear Spaces#^def-8-6|Def. §8.6]], [[§8 Normed Linear Spaces#^prop-8-4|§8.4]]

> [!remark]- Connections
> - The finite-dimensional case, minimizing distance to a subspace: [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-61|LADR 6.61]].
> - The minimize-then-perturb pattern: [[Functional Analysis Problem-Solving Techniques#^rem-t11|Technique 11]].
> - Computational version: [[§42 Orthogonal Projections#^thm-42-3|235 Thm. §42.3]] (the case of a subspace of ℝⁿ, where the closest point is the orthogonal projection, with worked distances).

> [!remark] Remark: Where Each Hypothesis Enters
> Convexity puts the midpoint $\tfrac{y_m + y_n}{2}$ in $K$, which is what makes the cross term in the parallelogram law large and forces $\|y_n - y_m\|$ small; this is the whole mechanism, and it is why the parallelogram law — hence an inner product, not merely a norm — is needed. Completeness of $H$ turns the Cauchy sequence into a limit; closedness of $K$ keeps that limit in $K$. The theorem fails without each: in $\ell^1$ (no inner product) closest points need not be unique; in an incomplete inner product space a minimizing sequence need not converge; for $K$ open the infimum need not be attained. The same midpoint argument gives uniqueness.

^rem-18-2

![[m556-18-4.svg]]
*Uniqueness needs the inner product. The same half-plane $K$ (blue) and the same point $x_0$, with the ball of radius $\operatorname{dist}(x_0, K)$ in two norms (dashed). The round Euclidean ball touches $K$ at a single point $y_0$ (red); the $\ell^1$ ball has a flat edge lying along the boundary of $K$, so every point of that segment (red) is a closest point. The midpoint of two of them is just as close, which the parallelogram law forbids in a Hilbert space.*

> [!remark] Remark: Comparison with Lax
> The statement and proof are Lax's Theorem 6.2, which assumes $K$ nonempty; the hypothesis is needed (for $K = \varnothing$ the infimum is $+\infty$) and was missing from an earlier version of these notes. Lax also proves the same result in any *uniformly convex* Banach space (§5.2, Theorem 8), where the parallelogram law is replaced by a quantitative form of the strict convexity of the unit ball; Hilbert spaces are the model case. Not covered in lecture.

^rem-18-3

## Orthogonal Complements

> [!definition] Definition §18.1: Orthogonality; Orthogonal Complement
> Let $(X, (\cdot,\cdot))$ be an inner product space. Two vectors $x, y \in X$ are **orthogonal** (or perpendicular), written $x \perp y$, if $(x, y) = 0$. For a subset $M \subset X$, the **orthogonal complement** of $M$ is
>
> $$
> M^\perp = \{ v \in X : (v, y) = 0 \text{ for all } y \in M \} .
> $$
>
> *Lax: §6.1 and §6.2, definitions*

^def-18-1

> [!remark]- Connections
> - The finite-dimensional home: [[§19 Inner Products and Norms#^ladr-6-10|LADR 6.10]] (orthogonal), [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-46|LADR 6.46]] (orthogonal complement).
> - Computational version: [[§40 Inner Product, Length, and Orthogonality#^def-40-5|235 Def. §40.5]] (orthogonal vectors), [[§40 Inner Product, Length, and Orthogonality#^def-40-6|235 Def. §40.6]] (orthogonal complement of a subspace of ℝⁿ).

Note that $M$ is any subset, not necessarily a subspace, and that $x \perp y$ iff $y \perp x$ by skew-symmetry.

> [!theorem] Proposition §18.3: $M^\perp$ is a Closed Subspace
> For every subset $M$ of an inner product space $X$, $M^\perp$ is a closed linear subspace of $X$.
>
> *Lax: §6.2, Thm 3(i)*

^prop-18-3

> [!proof]+ Proof
> *Subspace.* If $v_1, v_2 \in M^\perp$ and $a, b \in \mathbb{F}$, then for every $y \in M$, $(av_1 + bv_2, y) = a(v_1, y) + b(v_2, y) = 0$ by linearity in the first slot; and $0 \in M^\perp$.
>
> *Closed.* Let $v_n \in M^\perp$ with $v_n \to v$ in $X$. For each $y \in M$, Lemma [[§18 Projection and Orthogonal Decomposition#^lem-18-1|§18.1]] (with $y_n = y$ constant) gives $(v, y) = \lim_n (v_n, y) = 0$. So $v \in M^\perp$.

^pf-18-3

*Uses:* [[§18 Projection and Orthogonal Decomposition#^def-18-1|Def. §18.1]], [[§18 Projection and Orthogonal Decomposition#^lem-18-1|§18.1]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]], [[§8 Normed Linear Spaces#^def-8-6|Def. §8.6]]

> [!remark]- Connections
> - The finite-dimensional home: [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-48|LADR 6.48]].
> - Computational version: [[§40 Inner Product, Length, and Orthogonality#^thm-40-5|235 Thm. §40.5]] (in ℝⁿ the complement is a subspace, tested on a spanning set).

> [!definition] Definition §18.2: Internal Direct Sum
> Let $Y_1, Y_2$ be linear subspaces of a linear space $X$. We write $X = Y_1 \oplus Y_2$, and call $X$ the **internal direct sum** of $Y_1$ and $Y_2$, if for every $x \in X$ there are unique $y_1 \in Y_1$ and $y_2 \in Y_2$ with $x = y_1 + y_2$.

^def-18-2

> [!remark]- Connections
> - Axler's definition: [[§3 Subspaces#^ladr-1-41|LADR 1.41]]; for two subspaces, [[§3 Subspaces#^ladr-1-46|LADR 1.46]] (and [[Condition for a direct sum|LADR 1.45]]).

> [!remark] Remark: Internal and External
> By Proposition [[§1 Linear Spaces#^prop-1-3|§1.3]], $X = Y_1 \oplus Y_2$ holds iff $Y_1 + Y_2 = X$ and $Y_1 \cap Y_2 = \{0\}$, and then $(y_1, y_2) \mapsto y_1 + y_2$ is an isomorphism from the external direct sum of Definition [[§1 Linear Spaces#^def-1-4|§1.4]] onto $X$; so the same symbol for the two notions causes no harm. This is the definition of Axler raised as a question in the first lecture; Wu introduced it here because the theorem below needs it. In the language of [[§1 Linear Spaces#Complements and the Isomorphism X ≅ X/Y ⊕ Y|§1]], $X = Y \oplus W$ says exactly that $W$ is a complement of $Y$.

^rem-18-4

> [!theorem] Theorem §18.4: Orthogonal Decomposition
> Let $H$ be a Hilbert space and $Y \subset H$ a closed linear subspace. Then
> - (1) $H = Y \oplus Y^\perp$ (Definition [[§18 Projection and Orthogonal Decomposition#^def-18-2|§18.2]]): every $x \in H$ can be written in exactly one way as $x = y + v$ with $y \in Y$, $v \in Y^\perp$;
> - (2) $(Y^\perp)^\perp = Y$.
>
> *Lax: §6.2, Thm 3*

^thm-18-4

![[m556-18-2.svg]]
*The decomposition $x_0 = y_0 + v$: $y_0 \in Y$ is the closest point of $Y$ to $x_0$ (Theorem [[§18 Projection and Orthogonal Decomposition#^thm-18-2|§18.2]]), and the error $v = x_0 - y_0$ (red arrow) is perpendicular to $Y$, i.e. parallel to the line $Y^\perp$.*

> [!proof]+ Proof
> **(1), existence.** Since $Y$ is a linear subspace it is convex, and it is closed by hypothesis. By Theorem [[§18 Projection and Orthogonal Decomposition#^thm-18-2|§18.2]] there is a unique $y_0 \in Y$ with $\|x_0 - y_0\| = \operatorname{dist}(x_0, Y)$. Put $v = x_0 - y_0$, so $x_0 = y_0 + v$. It remains to show $v \in Y^\perp$, i.e. $(v, y) = 0$ for every $y \in Y$.
>
> *Perturbing the minimizer.* Fix $y \in Y$ and $t \in \mathbb{F}$. Since $y_0 + ty \in Y$ (a subspace), the minimality of $y_0$ gives
>
> $$
> \|v\|^2 = \|x_0 - y_0\|^2 \le \|x_0 - (y_0 + ty)\|^2 = \|v - ty\|^2 .
> $$
>
> Expanding the right side by [[§17 Cauchy–Schwarz and the Induced Norm#^pf-17-1|(5.1)]] with $-t$ in place of $t$,
>
> $$
> \|v - ty\|^2 = \|v\|^2 - 2\operatorname{Re}\bigl( \bar{t}\,(v, y) \bigr) + |t|^2\|y\|^2 ,
> $$
>
> so, for all $t \in \mathbb{F}$,
>
> $$
> |t|^2 \|y\|^2 - 2\operatorname{Re}\bigl( \bar{t}\,(v,y) \bigr) \ge 0 . \tag{5.3}
> $$
>
> *Choosing $t$.* Suppose $(v, y) \neq 0$; then $y \neq 0$. Write $(v, y) = e^{i\theta}\,|(v,y)|$ and take $t = s\,e^{i\theta}$ with $s > 0$ real, so that $\bar{t}\,(v,y) = s\,|(v,y)|$ is real and (5.3) reads
>
> $$
> s^2\|y\|^2 - 2s\,|(v,y)| \ge 0, \qquad \text{i.e.} \qquad s\,\|y\|^2 \ge 2\,|(v,y)| .
> $$
>
> This fails for $0 < s < 2|(v,y)| / \|y\|^2$ — explicitly, $s = |(v,y)|/\|y\|^2$ gives $s^2\|y\|^2 - 2s|(v,y)| = -|(v,y)|^2/\|y\|^2 < 0$ — a contradiction. Hence $(v, y) = 0$ for every $y \in Y$, and $v \in Y^\perp$. (Wu: “you are required to write down precisely how small is enough.”)
>
> **(1), uniqueness.** Suppose $x = y + v = y' + v'$ with $y, y' \in Y$ and $v, v' \in Y^\perp$. Then $y - y' = v' - v$ lies in $Y \cap Y^\perp$ (both are subspaces, Proposition [[§18 Projection and Orthogonal Decomposition#^prop-18-3|§18.3]]). But if $w \in Y \cap Y^\perp$ then $(w, w) = 0$ by definition of $Y^\perp$ with $w$ as the element of $Y$, so $w = 0$ by positivity. Hence $y = y'$ and $v = v'$.
>
> **(2).** $Y \subset (Y^\perp)^\perp$ is the definition: an element of $Y$ is orthogonal to every element of $Y^\perp$. Conversely let $x \in (Y^\perp)^\perp$. By (1), $x = y + v$ with $y \in Y$, $v \in Y^\perp$. Take the inner product with $v$:
>
> $$
> (x, v) = (y, v) + (v, v) = 0 + (v, v),
> $$
>
> using $y \perp v$. But $(x, v) = 0$, because $x \in (Y^\perp)^\perp$ and $v \in Y^\perp$. So $(v, v) = 0$, $v = 0$, and $x = y \in Y$.

^pf-18-4

*Uses:* [[§18 Projection and Orthogonal Decomposition#^thm-18-2|§18.2]], [[§17 Cauchy–Schwarz and the Induced Norm#^pf-17-1|§17.1 (5.1)]], [[§18 Projection and Orthogonal Decomposition#^prop-18-3|§18.3]], [[§18 Projection and Orthogonal Decomposition#^def-18-1|Def. §18.1]], [[§18 Projection and Orthogonal Decomposition#^def-18-2|Def. §18.2]], [[§16 Definition and Examples#^def-16-1|Def. §16.1]], [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Def. §2.3]]

> [!remark]- Connections
> - Announced in Chapter 1 as the missing hypothesis of [[§1 Linear Spaces#^cor-1-13|§1.13]] (orthogonal complement as a model of the quotient).
> - The finite-dimensional home: [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-49|LADR 6.49]] ($V = U \oplus U^\perp$), [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-52|LADR 6.52]] ($(U^\perp)^\perp = U$), [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-55|LADR 6.55]] (orthogonal projection).
> - Used for the Riesz representation theorem: [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-19-4|§19.4]].
> - Computational version: [[§42 Orthogonal Projections#^thm-42-1|235 Thm. §42.1]] (the ℝⁿ case, with the projection computed from an orthogonal basis) and, for (2), [[§40 Inner Product, Length, and Orthogonality#^cor-40-8|235 Cor. §40.8]].

> [!remark] Remark: The Promise of Lecture 1 is Kept
> Corollary [[§1 Linear Spaces#^cor-1-13|§1.13]] (Lecture 1) said: *if* $X = Y + Y^\perp$, then $Y^\perp$ is a complement of $Y$ and $X/Y \cong Y^\perp$. The theorem just proved supplies the hypothesis for every closed subspace of a Hilbert space, so in that setting the quotient $X/Y$ really is the orthogonal complement, as the picture in [[§1 Linear Spaces#Quotient Spaces|§1]] suggested; the [[§1 Linear Spaces#^rem-1-10|remark following Corollary §1.13]] identified exactly this theorem as the missing piece. The hypotheses are sharp: $c_{00} \subset \ell^2$ (not closed) has $c_{00}^\perp = \{0\}$, so $c_{00} + c_{00}^\perp \neq \ell^2$, while $(c_{00}^\perp)^\perp = \ell^2 \neq c_{00}$ — both (1) and (2) fail. For an arbitrary subset $M$, $(M^\perp)^\perp = \overline{\operatorname{span}}\, M$ (Theorem [[§18 Projection and Orthogonal Decomposition#^thm-18-6|§18.6]]).

^rem-18-5

> [!remark] Remark
> The proof of (1) is the first-variation argument of calculus, in the form “at a minimum the derivative vanishes”: $y_0$ minimizes $y \mapsto \|x_0 - y\|^2$ over $Y$, so moving $y_0$ along any direction $y \in Y$ cannot decrease the value, and [[§18 Projection and Orthogonal Decomposition#^pf-18-4|(5.3)]] is the statement that the linear term in $t$ of the expansion must vanish. The rotation $t = s e^{i\theta}$ is [[Functional Analysis Problem-Solving Techniques#^rem-t8|Technique 8]] again. Riesz's lemma (Lemma [[§15 Compactness and the Unit Ball#^lem-15-2|§15.2]]) was the substitute for this argument in a bare normed space; here the constant $\tfrac12$ improves to an exact orthogonal vector, as the [[§15 Compactness and the Unit Ball#^rem-15-2|remark]] after Proposition [[§15 Compactness and the Unit Ball#^prop-15-4|§15.4]] anticipated.

^rem-18-6

## The Double Complement

> [!theorem] Lemma §18.5: A Set and Its Closed Span Have the Same Complement
> For any subset $M$ of an inner product space $X$, $M^\perp = \bigl( \overline{\operatorname{span}}\, M \bigr)^\perp$.
>
> *Source: HW4, Problem 2, Step 1*

^lem-18-5

> [!proof]+ Proof
> (HW4, Problem 2, Step 1.) Let $Y = \overline{\operatorname{span}}\, M$. Since $M \subset Y$, every vector orthogonal to $Y$ is orthogonal to $M$. Conversely, let $v \in M^\perp$. For a finite combination $z = \sum_i a_i m_i$ with $m_i \in M$, $(z, v) = \sum_i a_i (m_i, v) = \sum_i a_i\,\overline{(v, m_i)} = 0$, so $v \perp \operatorname{span} M$; and if $z_n \to y$ with $z_n \in \operatorname{span} M$, then $(y, v) = \lim_n (z_n, v) = 0$ by Lemma [[§18 Projection and Orthogonal Decomposition#^lem-18-1|§18.1]]. So $v \in Y^\perp$.

^pf-18-5

*Uses:* [[§18 Projection and Orthogonal Decomposition#^def-18-1|Def. §18.1]], [[§1 Linear Spaces#^prop-1-5|§1.5]], [[§8 Normed Linear Spaces#^def-8-8|Def. §8.8]], [[§8 Normed Linear Spaces#^prop-8-6|§8.6]], [[§18 Projection and Orthogonal Decomposition#^lem-18-1|§18.1]]

> [!remark]- Connections
> - Re-proved for orthonormal sets: [[§20 Orthonormal Sets and Bases#^prop-20-9|§20.9]].
> - Computational version: [[§40 Inner Product, Length, and Orthogonality#^thm-40-5|235 Thm. §40.5]](1) (orthogonality to a subspace of ℝⁿ is tested on a spanning set).

> [!theorem] Theorem §18.6: The Double Complement
> For any subset $M$ of a Hilbert space $H$,
>
> $$
> (M^\perp)^\perp = \overline{\operatorname{span}}\, M .
> $$
>
> In particular $M^\perp = \{0\}$ if and only if $\operatorname{span} M$ is dense in $H$.
>
> *Source: HW4, Problem 2*
>
> *Lax: §6.4, Thm 7*

^thm-18-6

> [!proof]+ Proof
> (HW4, Problem 2.) $Y = \overline{\operatorname{span}}\, M$ is a closed linear subspace (Definition [[§8 Normed Linear Spaces#^def-8-8|§8.8]]). By Lemma [[§18 Projection and Orthogonal Decomposition#^lem-18-5|§18.5]] and Theorem [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]](2),
>
> $$
> (M^\perp)^\perp = (Y^\perp)^\perp = Y .
> $$
>
> For the last statement: if $M^\perp = \{0\}$ then $Y = \{0\}^\perp = H$; conversely, if $Y = H$ then $M^\perp = Y^\perp = H^\perp = \{0\}$, since a vector orthogonal to itself is $0$.

^pf-18-6

*Uses:* [[§8 Normed Linear Spaces#^def-8-8|Def. §8.8]], [[§8 Normed Linear Spaces#^def-8-7|Def. §8.7]], [[§18 Projection and Orthogonal Decomposition#^lem-18-5|§18.5]], [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]], [[§16 Definition and Examples#^def-16-1|Def. §16.1]]

> [!remark]- Connections
> - The finite-dimensional home: [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-52|LADR 6.52]], [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-54|LADR 6.54]].
> - The special case of an orthonormal set, re-proved: [[§20 Orthonormal Sets and Bases#^prop-20-9|§20.9]]; as an application of [[Functional Analysis Problem-Solving Techniques#^ex-t14|Technique 14]].
> - Computational version: [[§40 Inner Product, Length, and Orthogonality#^cor-40-8|235 Cor. §40.8]] (the double complement in ℝⁿ) and [[§40 Inner Product, Length, and Orthogonality#^thm-40-6|235 Thm. §40.6]] (the complement of the rows of a matrix is its null space).

> [!remark] Remark
> Without completeness only one inclusion survives: $\overline{\operatorname{span}}\, M \subset (M^\perp)^\perp$ holds in any inner product space, because $(M^\perp)^\perp$ is a closed subspace (Proposition [[§18 Projection and Orthogonal Decomposition#^prop-18-3|§18.3]]) containing $M$. The reverse inclusion is where Theorem [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]](2), and hence completeness, is used. The last statement of the theorem is the general form of Proposition [[§20 Orthonormal Sets and Bases#^prop-20-9|§20.9]]: an orthonormal set is complete exactly when its span is dense.

^rem-18-7

## Example: Even and Odd Functions

> [!theorem] Proposition §18.7: Even and Odd Functions
> In $L^2[-1,1]$ let $E$ be the set of even functions ($f(-x) = f(x)$ a.e.) and $O$ the set of odd functions ($f(-x) = -f(x)$ a.e.). Then:
> - (a) $E^\perp = O$ and $O^\perp = E$;
> - (b) $E$ and $O$ are closed subspaces, and $L^2[-1,1] = E \oplus O$: every $f$ is uniquely $f = f_e + f_o$ with
>
> $$
> f_e(x) = \tfrac12\bigl( f(x) + f(-x) \bigr) \in E, \qquad f_o(x) = \tfrac12\bigl( f(x) - f(-x) \bigr) \in O ,
> $$
>
> and $f_e$ is the closest point of $E$ to $f$.
>
> *Source: HW4, Problem 1 (for $E^\perp = O$)*

^prop-18-7

> [!proof]+ Proof
> (HW4, Problem 1, for $E^\perp = O$.)
> Throughout, $\mathbb{F}$ is $\mathbb{R}$ or $\mathbb{C}$, $L^2 = L^2[-1,1]$ with $(f,g) = \int_{-1}^1 f\,\bar{g}\,dx$, and elements of $L^2$ are functions up to equality almost everywhere. A function $f \in L^2$ is *even* if $f(-x) = f(x)$ for a.e. $x$, and *odd* if $f(-x) = -f(x)$ for a.e. $x$. We show that
>
> $$
> S^\perp = \{ g \in L^2[-1,1] : g \text{ is odd} \}.
> $$
>
> We use one fact from real analysis: Lebesgue measure on $[-1,1]$ is invariant under $x \mapsto -x$, so for integrable $h$, $\int_{-1}^1 h(-x)\,dx = \int_{-1}^1 h(x)\,dx$, and $x \mapsto -x$ maps null sets to null sets.
>
> **Step 1: the reflection.** For $f \in L^2$ put $(Rf)(x) = f(-x)$. This is well defined on classes (reflection preserves null sets), $Rf \in L^2$ with $\int |Rf|^2 = \int |f|^2$, and $R$ is linear with $R(Rf) = f$. By definition, $f$ is even iff $Rf = f$ and odd iff $Rf = -f$. For $f \in L^2$ put
>
> $$
> f_e = \tfrac12 (f + Rf), \qquad f_o = \tfrac12 (f - Rf).
> $$
>
> Then $f_e, f_o \in L^2$, $f = f_e + f_o$, $R f_e = \tfrac12(Rf + f) = f_e$ and $R f_o = \tfrac12(Rf - f) = -f_o$; so $f_e$ is even and $f_o$ is odd.
>
> **Step 2: odd functions lie in $S^\perp$.** Let $f \in S$ and $g$ odd. The function $h = f\bar{g}$ is integrable (by the Cauchy–Schwarz inequality in $L^2$) and $h(-x) = f(-x)\overline{g(-x)} = -f(x)\overline{g(x)} = -h(x)$ for a.e. $x$. By reflection invariance,
>
> $$
> (f, g) = \int_{-1}^1 h(x)\,dx = \int_{-1}^1 h(-x)\,dx = -\int_{-1}^1 h(x)\,dx = -(f, g),
> $$
>
> so $(f, g) = 0$. Hence $g \in S^\perp$. By the conjugate symmetry $(g,f) = \overline{(f,g)}$, also $(g, f) = 0$.
>
> **Step 3: every element of $S^\perp$ is odd.** Let $g \in S^\perp$ and write $g = g_e + g_o$ as in Step 1. Since $g_e \in S$, the definition of $S^\perp$ gives $(g, g_e) = 0$. On the other hand, by Step 2 (with $f = g_e$ even and $g_o$ odd), $(g_o, g_e) = 0$, so
>
> $$
> 0 = (g, g_e) = (g_e, g_e) + (g_o, g_e) = \|g_e\|^2 .
> $$
>
> Hence $g_e = 0$ in $L^2$, i.e. $g = g_o$ is odd.
>
> By Steps 2 and 3, $E^\perp = O$.
>
> **Step 4: $O^\perp = E$.** By Step 2 every even function is orthogonal to every odd function, so $E \subset O^\perp$. If $g \in O^\perp$, write $g = g_e + g_o$; since $g_o \in O$, $0 = (g, g_o) = (g_e, g_o) + (g_o, g_o) = \|g_o\|^2$, so $g = g_e \in E$. (Not part of the homework.)
>
> **Step 5: (b).** By (a) and Proposition [[§18 Projection and Orthogonal Decomposition#^prop-18-3|§18.3]], $E = O^\perp$ and $O = E^\perp$ are closed subspaces. The decomposition $f = f_e + f_o$ of Step 1 has $f_e \in E$ and $f_o \in O = E^\perp$, so it is the decomposition of Theorem [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]] for $Y = E$; its uniqueness is part of that theorem, and $f_e$ is the closest point of $E$ to $f$ by the proof of that theorem. (Not part of the homework.)

^pf-18-7

*Uses:* [[§16 Definition and Examples#^ex-16-3|Ex. §16.3]], [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|§17.1]], [[§18 Projection and Orthogonal Decomposition#^def-18-1|Def. §18.1]], [[§18 Projection and Orthogonal Decomposition#^prop-18-3|§18.3]], [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]]

> [!remark]- Connections
> - The parity operator in the quantum mechanics chapter: [[§25 The Completeness Relation#^ex-25-1|Ex. §25.1]]; the method: [[Functional Analysis Problem-Solving Techniques#^ex-t14|Technique 14]].

![[m556-18-3.svg]]
*$e^x$ on $[-1,1]$ (black) with its even part $\cosh x$ (red) and odd part $\sinh x$ (blue); at every $x$ the red and blue values add up to the black one.*

For $f(x) = e^x$ the decomposition is $e^x = \cosh x + \sinh x$: the even part is the orthogonal projection of $e^x$ onto $E$, and the odd part is orthogonal to every even function.

## An Application: A Sharp Integral Inequality

> [!theorem] Proposition §18.8: A Sharp Integral Inequality
> Let $f \in C^2([a,b])$ with $f(a) = f(b) = 0$, $f'(a) = 1$, $f'(b) = 0$, and $L = b - a$. Then
>
> $$
> \int_a^b |f''(x)|^2\,dx \ge \frac{4}{L},
> $$
>
> with equality for $f_*(x) = (x - a)\bigl( 1 - \tfrac{x-a}{L} \bigr)^2$.
>
> *Source: HW4, Problem 4*

^prop-18-8

> [!proof]+ Proof
> (HW4, Problem 4.)
> Write $L = b - a > 0$. Functions may be real or complex valued; all integrals are Riemann integrals of continuous functions. We use the Cauchy–Schwarz inequality for the inner product $(u, v) = \int_a^b u\,\bar{v}\,dx$ on $C([a,b])$ (the restriction of the $L^2$ inner product; Theorem [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|§17.1]]).
>
> **Step 1: an identity for $f''$.** Let $g(x) = 1 - \dfrac{3(x - a)}{2L}$, a real polynomial with $g(a) = 1$ and $g'(x) = -\dfrac{3}{2L}$. Since $f' \in C^1([a,b])$ and $g \in C^1([a,b])$, integration by parts gives
>
> $$
> \int_a^b f''(x)\,g(x)\,dx = \bigl[ f'(x)\,g(x) \bigr]_a^b - \int_a^b f'(x)\,g'(x)\,dx .
> $$
>
> The boundary term is $f'(b)g(b) - f'(a)g(a) = 0 \cdot g(b) - 1 \cdot 1 = -1$. Since $g'$ is the constant $-\frac{3}{2L}$, the fundamental theorem of calculus gives
>
> $$
> \int_a^b f'(x)\,g'(x)\,dx = -\frac{3}{2L}\bigl( f(b) - f(a) \bigr) = 0 .
> $$
>
> Hence
>
> $$
> \int_a^b f''(x)\,g(x)\,dx = -1 .
> $$
>
> **Step 2: the norm of $g$.** With $t = x - a$,
>
> $$
> \int_a^b |g(x)|^2\,dx = \int_0^L \Bigl( 1 - \frac{3t}{2L} \Bigr)^2 dt = \int_0^L \Bigl( 1 - \frac{3t}{L} + \frac{9t^2}{4L^2} \Bigr) dt = L - \frac{3L}{2} + \frac{3L}{4} = \frac{L}{4} .
> $$
>
> **Step 3: Cauchy–Schwarz.** Since $g$ is real, $\int_a^b f'' g\,dx = (f'', g)$. By Step 1 and Cauchy–Schwarz,
>
> $$
> 1 = \bigl| (f'', g) \bigr| \le \Bigl( \int_a^b |f''|^2\,dx \Bigr)^{1/2} \Bigl( \int_a^b |g|^2\,dx \Bigr)^{1/2} = \Bigl( \int_a^b |f''|^2\,dx \Bigr)^{1/2} \sqrt{\frac{L}{4}} .
> $$
>
> Squaring and rearranging,
>
> $$
> \int_a^b |f''(x)|^2\,dx \ge \frac{4}{L} = \frac{4}{b - a}.
> $$
>
> **Step 4: sharpness.** (Not part of the homework.) Let $f_{\ast}(x) = (x - a)\bigl(1 - \frac{x - a}{L}\bigr)^2$. With $t = x - a$, $f_{\ast} = t - \frac{2t^2}{L} + \frac{t^3}{L^2}$, so $f_{\ast}(a) = 0$ and $f_{\ast}(b) = L - 2L + L = 0$; $f_{\ast}' = 1 - \frac{4t}{L} + \frac{3t^2}{L^2}$ equals $1$ at $t = 0$ and $1 - 4 + 3 = 0$ at $t = L$; and $f_{\ast}'' = -\frac{4}{L} + \frac{6t}{L^2} = -\frac{4}{L}\,g$. Hence, by Step 2,
>
> $$
> \int_a^b |f_*''|^2\,dx = \frac{16}{L^2} \int_a^b g^2\,dx = \frac{16}{L^2} \cdot \frac{L}{4} = \frac{4}{L}.
> $$

^pf-18-8

*Uses:* [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|§17.1]], [[§16 Definition and Examples#^ex-16-3|Ex. §16.3]], [[§34 Fundamental Theorem of Calculus#^thm-34-3|451 §34.3]], [[Fundamental Theorem of Calculus|451 §34.4]]

> [!remark]- Connections
> - The method: [[Functional Analysis Problem-Solving Techniques#^ex-t13|Technique 13]]; the finite-dimensional minimization it rests on: [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-61|LADR 6.61]].

> [!remark] Remark: Where $g$ Comes From
> The boundary conditions fix two inner products of $h = f''$ with fixed functions: $\int_a^b h = f'(b) - f'(a) = -1$, and, by Taylor's formula with integral remainder, $\int_a^b (b - x)\,h(x)\,dx = f(b) - f(a) - f'(a)L = -L$. Let $Y = \operatorname{span}\{1, x\}$, a closed (finite-dimensional) subspace of $L^2[a,b]$, and decompose $h = h_Y + h_\perp$ with $h_Y \in Y$, $h_\perp \perp Y$. The two constraints involve only $h_Y$, while $\|h\|^2 = \|h_Y\|^2 + \|h_\perp\|^2 \ge \|h_Y\|^2$ by [[§20 Orthonormal Sets and Bases#^lem-20-1|Pythagoras]]. So the minimum of $\|h\|$ under the constraints is attained by an element of $Y$ — a linear function — and that is why testing against a linear $g$ loses nothing. This is the [[§18 Projection and Orthogonal Decomposition#^thm-18-2|projection theorem]] at work: the constraint set is a closed affine subspace, and its point closest to $0$ lies in the orthogonal complement of the directions along it. It is also a first example of the calculus of variations recast in a Hilbert space.

^rem-18-8
