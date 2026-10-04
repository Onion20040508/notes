---
type: section
subject: "[[Functional Analysis]]"
chapter: 2
section: 7
tags: [functional-analysis, math556]
---
← [[§6 Convex Sets and the Gauge]] · ↑ [[· 2 The Hahn–Banach Theorem]] · [[§8 The Complex Hahn–Banach Theorem]] →

*Stage: algebra — Threads meet: functionals $\times$ convexity. Hahn–Banach applied to a gauge.*

This is the first application of [[§4 Statement and Motivation#^thm-4-2|Hahn–Banach]], and the reason the theorem was stated with a general $p$ rather than a norm: the $p$ that gets used is the [[§6 Convex Sets and the Gauge#^def-6-2|gauge]] of a convex set. Recall (Definition [[§4 Statement and Motivation#^def-4-2|§4.2]]) that for a nonzero linear functional $\ell : X \to \mathbb{R}$ and $c \in \mathbb{R}$, $\{\ell = c\}$ is a hyperplane and $\{\ell < c\}$, $\{\ell > c\}$ are the two half-spaces it bounds; in $\mathbb{R}^n$, with $\ell(x) = a \cdot x$, which side is “$> c$” is determined by the direction of $a$.

> [!theorem] Theorem §7.1: Hyperplane Separation; Geometric Hahn–Banach
> Let $X$ be a linear space over $\mathbb{R}$, let $K \subset X$ be a nonempty convex set in which every point is an interior point, and let $y_0 \in X$ with $y_0 \notin K$. Then there is a hyperplane that separates $y_0$ from $K$: there exist a linear functional $\ell : X \to \mathbb{R}$ and $c_0 \in \mathbb{R}$ such that
>
> $$
> \ell(y_0) = c_0 \qquad \text{but} \qquad \ell(x) < c_0 \quad \text{for all } x \in K.
> $$
>
> *Lax: §3.2, Thm 5*

^thm-7-1

> [!remark] Remark: Comparison with Lax
> The statement is Lax's Theorem 5, including the hypothesis that $K$ is nonempty, which the proof needs in Step 1 (to translate a point of $K$ to the origin) and which was missing from an earlier version of these notes. Lax continues with two strengthenings not covered in lecture: Corollary 5′, for a convex set with only *one* interior point (with the weaker conclusion $\ell(x) \le \ell(y)$), and Theorem 6, separating two disjoint convex sets, one of which has an interior point.

^rem-7-1

In words: $y_0$ lies *on* the hyperplane $\{\ell = c_0\}$, and all of $K$ lies strictly on one side of it. The point $y_0$ may be a boundary point of $K$ (it is excluded from $K$ only because $K$ has no boundary points), and the statement still holds; the hyperplane is then a supporting hyperplane at $y_0$.

![[m556-6-1.svg]]
*Left: the point $y_0$ lies on the hyperplane $\{\ell = c_0\}$ (red), and $K$ — dashed, since every point of $K$ is interior — lies strictly in the half-space $\{\ell < c_0\}$. Right: $y_0$ may sit on the edge of $K$ (it is still not in $K$); the hyperplane is then a supporting hyperplane, touching $K$'s boundary at $y_0$ without meeting $K$.*

> [!proof]+ Proof
> **Step 1: Reduction to $0 \in K$.** Assume first that $0 \in K$; the general case is Step 4.
>
> **Step 2: A functional on a line.** Let $Y = \operatorname{span}\{y_0\} = \{ a y_0 : a \in \mathbb{R} \}$ and define $\ell : Y \to \mathbb{R}$ by
>
> $$
> \ell(a y_0) = a, \qquad \text{i.e. } \ell(y_0) = 1.
> $$
>
> This is a linear functional on $Y$ (the representation $a y_0$ is unique since $y_0 \neq 0$, as $y_0 \notin K \ni 0$).
>
> **Step 3: Domination by the gauge.** Since $0 \in K$ is an interior point, the gauge $p_K$ is defined, positive homogeneous, and subadditive (Proposition [[§6 Convex Sets and the Gauge#^prop-6-6|§6.6]]). Because every point of $K$ is interior, Corollary [[§6 Convex Sets and the Gauge#^cor-6-8|§6.8]] gives
>
> $$
> x \in K \iff p_K(x) < 1.
> $$
>
> As $y_0 \notin K$, this forces $p_K(y_0) \ge 1$. Hence for $a > 0$, by positive homogeneity,
>
> $$
> \ell(a y_0) = a \le a\, p_K(y_0) = p_K(a y_0),
> $$
>
> and for $a \le 0$,
>
> $$
> \ell(a y_0) = a \le 0 \le p_K(a y_0),
> $$
>
> since $p_K \ge 0$. So $\ell \le p_K$ on $Y$. By the Hahn–Banach theorem (Theorem [[§4 Statement and Motivation#^thm-4-2|§4.2]]), $\ell$ extends to a linear functional $L$ on $X$ with $L(x) \le p_K(x)$ for all $x \in X$. For this $L$,
>
> $$
> L(y_0) = \ell(y_0) = 1, \qquad L(x) \le p_K(x) < 1 \quad \text{for all } x \in K,
> $$
>
> which is the claim with $c_0 = 1$ and $L$ in the role of the functional in the statement.
>
> **Step 4: The general case.** (Left to us in lecture; written out here.) If $0 \notin K$, pick any $x_1 \in K$ and translate: $K' = K - x_1 = \{ x - x_1 : x \in K \}$. Translation preserves convexity, sends interior points to interior points (the definition of interior point involves only differences $x_0 + ty$), and sends $x_1$ to $0$, so $K'$ is convex with every point interior and $0 \in K'$; also $y_0 - x_1 \notin K'$. Steps 2–3 give a linear $L : X \to \mathbb{R}$ with $L(y_0 - x_1) = 1$ and $L(x - x_1) < 1$ for all $x \in K$. By linearity, with $c_0 = 1 + L(x_1)$,
>
> $$
> L(y_0) = c_0, \qquad L(x) < c_0 \quad \text{for all } x \in K.
> $$

^pf-7-1

*Uses:* [[§4 Statement and Motivation#^thm-4-2|§4.2]], [[§6 Convex Sets and the Gauge#^def-6-1|Def. §6.1]], [[§6 Convex Sets and the Gauge#^def-6-2|Def. §6.2]], [[§6 Convex Sets and the Gauge#^prop-6-5|§6.5]], [[§6 Convex Sets and the Gauge#^prop-6-6|§6.6]], [[§6 Convex Sets and the Gauge#^cor-6-8|§6.8]], [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Def. §2.3]]

> [!remark] Remark
> Everything in the proof was already in place; the theorem is an assembly. The gauge converts the geometric hypothesis (convex, all points interior, $y_0$ outside) into an inequality $p_K(y_0) \ge 1 = \ell(y_0)$ on a one-dimensional subspace; Hahn–Banach extends $\ell$ without breaking $\ell \le p_K$; and the description $K = \{p_K < 1\}$ converts the inequality back into geometry. The hyperplane is $\{\ell = 1\}$ in the normalized case; there is nothing canonical about it, since the extension is not unique. This is the sense in which a convex set can be described by hyperplanes: it lies on one side of a supporting hyperplane at every point outside it.

^rem-7-2
