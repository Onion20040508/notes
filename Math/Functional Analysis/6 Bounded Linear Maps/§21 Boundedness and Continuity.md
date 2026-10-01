---
type: section
subject: "[[Functional Analysis]]"
chapter: 6
section: 21
tags: [functional-analysis, math556]
---
← [[§20 Orthonormal Sets and Bases]] · ↑ [[· 6 Bounded Linear Maps]] · [[§22 Bras, Kets, and the Riesz Map]] →

*Stage: maps — Thread: functionals. Linear functionals generalize to linear maps between normed spaces; the bounded functionals of [[§19 Bounded Linear Functionals and the Riesz Representation Theorem|§19]] are the case $Y = \mathbb{F}$.*

Throughout, $(X, \|\cdot\|_X)$ and $(Y, \|\cdot\|_Y)$ are normed linear spaces over the same field $\mathbb{F}$; neither needs to be complete (“no completeness is necessary” for continuity, since only sequences that already converge are involved).

> [!definition] Definition §21.1: Continuous Linear Map
> A map $T : X \to Y$ is **linear** if $T(a_1 x_1 + a_2 x_2) = a_1 T x_1 + a_2 T x_2$ for all $x_1, x_2 \in X$ and $a_1, a_2 \in \mathbb{F}$. It is **continuous** if for every sequence $\{x_j\}_{j \in \mathbb{N}}$ in $X$,
>
> $$
> x_j \to x^{(0)} \text{ in } (X, \|\cdot\|_X) \implies T x_j \to T x^{(0)} \text{ in } (Y, \|\cdot\|_Y).
> $$
>
> *Lax: §15.1, definition of continuous map*

^def-21-1

> [!remark]- Connections
> - Linear maps between linear spaces, without topology: [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-1|Def. §2.1]]; finite-dimensional home [[§7 Vector Space of Linear Maps#^ladr-3-1|LADR 3.1]].
> - Continuity between topological spaces: [[§9 Continuous Functions#^def-9-1|590 Def. §9.1]]; for metric spaces it is equivalent to the sequential condition used here, [[§11 Metric Topology#^thm-11-9|590 Thm. §11.9]].

> [!definition] Definition §21.2: Bounded Linear Map; Operator Norm
> A linear map $T : X \to Y$ is **bounded** if there is $M \ge 0$ with
>
> $$
> \|T x\|_Y \le M\, \|x\|_X \qquad \text{for all } x \in X .
> $$
>
> For a bounded $T$ (and $X \neq \{0\}$) its **norm** is
>
> $$
> \|T\| = \sup_{\substack{x \in X \\ x \neq 0}} \frac{\|T x\|_Y}{\|x\|_X} ;
> $$
>
> if $X = \{0\}$, put $\|T\| = 0$.
>
> *Lax: §15.1, (2) and ($2'$)*

^def-21-2

> [!remark]- Connections
> - Finite-dimensional home (where the sup is a max): [[§27 Consequences of Singular Value Decomposition#^ladr-7-86|LADR 7.86]].
> - The case $Y = \mathbb{F}$: [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^def-19-1|Def. §19.1]]; the case $X = Y = H$ in the companion chapter: [[§23 The Completeness Relation#^def-23-1|Def. §23.1]].

> [!theorem] Proposition §21.1: The Operator Norm
> Let $T : X \to Y$ be a bounded linear map, $X \neq \{0\}$. Then
> - (a) $\|T\| = \sup_{\|x\|_X = 1} \|T x\|_Y$;
> - (b) $\|T x\|_Y \le \|T\|\, \|x\|_X$ for all $x \in X$;
> - (c) $\|T\|$ is the smallest $M$ for which $\|Tx\|_Y \le M \|x\|_X$ holds for all $x$.
>
> *Lax: §15.1, (3) and ($3'$)*

^prop-21-1

> [!proof]+ Proof
> (Stated in lecture; the checks are written out here.) (a) For $x \neq 0$, $u = x/\|x\|_X$ has $\|u\|_X = 1$ and, by linearity and homogeneity, $\|T x\|_Y / \|x\|_X = \|T u\|_Y$. So the ratios over $x \neq 0$ and the values $\|Tu\|_Y$ over unit vectors $u$ form the same set of numbers, and the two suprema agree. Both are finite: if $\|Tx\|_Y \le M\|x\|_X$ for all $x$, every ratio is at most $M$.
>
> (b) For $x = 0$ both sides are $0$, since $T0 = 0$ by linearity. For $x \neq 0$, $\|Tx\|_Y / \|x\|_X \le \|T\|$ by definition of the supremum.
>
> (c) By (b), $M = \|T\|$ works. If $M$ works, every ratio is at most $M$, so $\|T\| \le M$.

^pf-21-1

*Uses:* [[§21 Boundedness and Continuity#^def-21-2|Def. §21.2]], [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]]

![[m556-21-2.svg]]
*The operator norm of a linear map $T$ of the Euclidean plane: the unit circle of $X$ (blue, left) is mapped onto an ellipse (right). By (a), $\|T\|$ is the largest $\|Tu\|_Y$ over unit vectors $u$ — here the long semi-axis, attained at $u_0$ (red). By (b) and (c), the circle $\|y\|_Y = \|T\|$ (red, dashed) is the smallest circle about $0$ containing the image: every $Tu$ lies inside it, and a smaller $M$ would cut off $Tu_0$.*

> [!remark]- Connections
> - Finite-dimensional home: [[§27 Consequences of Singular Value Decomposition#^ladr-7-88|LADR 7.88]].
> - The same statements for the dual norm in the companion chapter: [[§22 Bras, Kets, and the Riesz Map#^lem-22-1|§22.1]].

> [!theorem] Proposition §21.2: Continuous if and only if Bounded
> A linear map $T : X \to Y$ between normed linear spaces is continuous if and only if it is bounded.
>
> *Lax: §15.1, Thm 1*

^prop-21-2

> [!proof]+ Proof
> ($\Leftarrow$, the easy direction.) Let $\|Tx\|_Y \le M \|x\|_X$ for all $x$, and let $x_j \to x^{(0)}$. By linearity,
>
> $$
> \|T x_j - T x^{(0)}\|_Y = \|T(x_j - x^{(0)})\|_Y \le M\, \|x_j - x^{(0)}\|_X \to 0 .
> $$
>
> ($\Rightarrow$) Assume $T$ is continuous but not bounded. Then no $M$ works; in particular, for each $n \in \mathbb{N}$ the constant $M = n$ fails, so there is $x_n \in X$ with
>
> $$
> \|T x_n\|_Y > n\, \|x_n\|_X ,
> $$
>
> and $x_n \neq 0$, since for $x_n = 0$ both sides would be $0$. Let
>
> $$
> y_n = \frac{x_n}{n\, \|x_n\|_X} .
> $$
>
> Then $\|y_n\|_X = \frac{1}{n} \to 0$, so $y_n \to 0$ in $X$. By linearity $T y_n = \frac{1}{n \|x_n\|_X}\, T x_n$, so
>
> $$
> \|T y_n\|_Y = \frac{\|T x_n\|_Y}{n\, \|x_n\|_X} > 1 \qquad \text{for all } n .
> $$
>
> But $T 0 = 0$, so continuity would give $\|T y_n\|_Y = \|T y_n - T0\|_Y \to 0$. This contradicts $\|T y_n\|_Y > 1$. Hence $T$ is bounded.

^pf-21-2

*Uses:* [[§21 Boundedness and Continuity#^def-21-1|Def. §21.1]], [[§21 Boundedness and Continuity#^def-21-2|Def. §21.2]], [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]]

> [!remark]- Connections
> - The case $Y = \mathbb{F}$, proved the same way: [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-19-1|§19.1]].

![[m556-21-1.svg]]
*Left: the sequence $y_n = x_n / (n\|x_n\|_X)$ shrinks to $0$ in $X$. Right: its images $Ty_n$ all lie outside the closed unit ball of $Y$ (red, dashed) around $T0 = 0$.*

The proof of ($\Rightarrow$): an unbounded $T$ sends the sequence $y_n \to 0$ to points that all stay outside the unit ball, so $Ty_n \not\to T0$.

> [!remark] Remark
> For $Y = \mathbb{F}$ this is Proposition [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-19-1|§19.1]] on linear functionals, and $\|T\|$ is then the dual norm of Definition [[§22 Bras, Kets, and the Riesz Map#^def-22-1|§22.1]]. The companion chapter's bounded operators on $H$ (Definition [[§23 The Completeness Relation#^def-23-1|§23.1]]) are the case $X = Y = H$. Since $\|Tx - Tx'\|_Y \le \|T\|\, \|x - x'\|_X$, a bounded linear map is even Lipschitz continuous, uniformly on all of $X$.

^rem-21-1

> [!definition] Definition §21.3: The Space $\mathcal{L}(X, Y)$
> $\mathcal{L}(X, Y)$ is the set of all bounded linear maps $T : X \to Y$, with the pointwise operations $(T_1 + T_2)x = T_1 x + T_2 x$ and $(aT)x = a\, Tx$, and the norm $\|T\|$ of Definition [[§21 Boundedness and Continuity#^def-21-2|§21.2]].
>
> *Lax: §15.1, definition of $\mathcal{L}(X, U)$*

^def-21-3

> [!remark]- Connections
> - Finite-dimensional home (all linear maps, same operations): [[§7 Vector Space of Linear Maps#^ladr-3-5|LADR 3.5]].
> - The dual space $X^* = \mathcal{L}(X, \mathbb{F})$ of the companion chapter: [[§22 Bras, Kets, and the Riesz Map#^def-22-1|Def. §22.1]].

> [!theorem] Theorem §21.3: $\mathcal{L}(X, Y)$ is a Normed Linear Space
> Let $X$ and $Y$ be normed linear spaces.
> - (1) $(\mathcal{L}(X, Y), \|\cdot\|)$ is a normed linear space.
> - (2) If $Y$ is complete, then $\mathcal{L}(X, Y)$ is a Banach space.
>
> *Lax: §15.1, Thms 2–3*

^thm-21-3

> [!proof]+ Proof of (1)
> We may assume $X \neq \{0\}$; otherwise $\mathcal{L}(X, Y) = \{0\}$.
>
> *Linear space.* The set of all maps $X \to Y$ with pointwise operations is a linear space: each of the eight axioms, evaluated at a point $x \in X$, is the corresponding axiom of $Y$ (as in Part 1 of the proof of Theorem [[§9 Completeness#^pf-9-1|§9.1]], with $\mathbb{F}$ replaced by $Y$). $\mathcal{L}(X, Y)$ is a linear subspace of it. The zero map is linear and bounded with $M = 0$. If $T_1, T_2$ are linear, so are $T_1 + T_2$ and $aT_1$: $(T_1 + T_2)(a_1 x_1 + a_2 x_2) = a_1 T_1 x_1 + a_2 T_1 x_2 + a_1 T_2 x_1 + a_2 T_2 x_2 = a_1 (T_1 + T_2) x_1 + a_2 (T_1 + T_2) x_2$, and similarly for $aT_1$. If $\|T_i x\|_Y \le M_i \|x\|_X$, then $\|(T_1 + T_2)x\|_Y \le \|T_1 x\|_Y + \|T_2 x\|_Y \le (M_1 + M_2)\|x\|_X$ and $\|(aT_1)x\|_Y = |a|\,\|T_1 x\|_Y \le |a| M_1 \|x\|_X$.
>
> *Positivity.* $\|T\| \ge 0$ as a supremum of non-negative numbers. If $\|T\| = 0$, then by Proposition [[§21 Boundedness and Continuity#^prop-21-1|§21.1]](b), $\|Tx\|_Y \le 0$ for all $x$, so $Tx = 0$ for all $x$ and $T$ is the zero map; conversely the zero map has norm $0$.
>
> *Homogeneity.* (Left to us in lecture.) By Proposition [[§21 Boundedness and Continuity#^prop-21-1|§21.1]](a), $\|aT\| = \sup_{\|x\|_X = 1} \|a\, Tx\|_Y = \sup_{\|x\|_X = 1} |a|\,\|Tx\|_Y = |a| \sup_{\|x\|_X = 1} \|Tx\|_Y = |a|\,\|T\|$, since multiplying a set of non-negative numbers by $|a| \ge 0$ multiplies its supremum by $|a|$.
>
> *Subadditivity.* By Proposition [[§21 Boundedness and Continuity#^prop-21-1|§21.1]](a),
>
> $$
> \begin{aligned}
> \|T_1 + T_2\| &= \sup_{\|x\|_X = 1} \|T_1 x + T_2 x\|_Y \le \sup_{\|x\|_X = 1} \bigl( \|T_1 x\|_Y + \|T_2 x\|_Y \bigr) \\
> &\le \sup_{\|x\|_X = 1} \|T_1 x\|_Y + \sup_{\|x\|_X = 1} \|T_2 x\|_Y = \|T_1\| + \|T_2\| .
> \end{aligned}
> $$
>
> The first inequality is the triangle inequality in $Y$ at each $x$. The second holds because for every unit $x$, $\|T_1 x\|_Y + \|T_2 x\|_Y \le \|T_1\| + \|T_2\|$, so the right-hand side is an upper bound for the set whose supremum is taken: summing and then taking the supremum gives at most the sum of the separate suprema.

^pf-21-3

*Uses:* [[§9 Completeness#^pf-9-1|§9.1 (Part 1 of the proof)]], [[§1 Linear Spaces#^def-1-1|Def. §1.1]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]], [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], [[§21 Boundedness and Continuity#^def-21-1|Def. §21.1]], [[§21 Boundedness and Continuity#^def-21-2|Def. §21.2]], [[§21 Boundedness and Continuity#^def-21-3|Def. §21.3]], [[§21 Boundedness and Continuity#^prop-21-1|§21.1]]

> [!proof]+ Proof of (2)
> Next lecture.

^pf-21-3-2

> [!remark]- Connections
> - Finite-dimensional home of the norm properties: [[§27 Consequences of Singular Value Decomposition#^ladr-7-87|LADR 7.87]].
> - Banach spaces: [[§9 Completeness#^def-9-2|Def. §9.2]]; the special case $Y = \mathbb{F}$ in the companion chapter: [[§22 Bras, Kets, and the Riesz Map#^def-22-1|Def. §22.1]].

> [!remark] Remark: Comparison with Lax
> Lax states Theorem 1 of §15.1 for Banach spaces $X, U$, but the proof uses no completeness, as Wu remarked. In the ($\Rightarrow$) direction Lax normalizes differently: he rescales $x_n$ to have $|x_n| = 1/\sqrt{n}$, so that $x_n \to 0$ while $|Mx_n| > \sqrt{n} \to \infty$; Wu divides by $n\|x_n\|_X$, so that $\|y_n\|_X = 1/n \to 0$ while $\|Ty_n\|_Y > 1$ merely stays away from $0$. Either contradicts continuity at $0$. Lax proves homogeneity and positivity of the operator norm as “obvious” and leaves subadditivity as his Exercise 1; here it is Wu's board argument.

^rem-21-2
