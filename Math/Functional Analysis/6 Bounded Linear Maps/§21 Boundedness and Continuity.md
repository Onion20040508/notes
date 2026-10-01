---
type: section
subject: "[[Functional Analysis]]"
chapter: 6
section: 21
tags: [functional-analysis, math556]
---
← [[§20 Orthonormal Sets and Bases]] · ↑ [[· 6 Bounded Linear Maps]] · [[§22 Dual Spaces]] →

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
> - The case $Y = \mathbb{F}$: [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^def-19-1|Def. §19.1]]; the case $X = Y = H$ in the companion chapter: [[§25 The Completeness Relation#^def-25-1|Def. §25.1]].

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
> - The same statements for the dual norm in the companion chapter: [[§24 Bras, Kets, and the Riesz Map#^lem-24-1|§24.1]].

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
> For $Y = \mathbb{F}$ this is Proposition [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-19-1|§19.1]] on linear functionals, and $\|T\|$ is then the dual norm of Definition [[§24 Bras, Kets, and the Riesz Map#^def-24-1|§24.1]]. The companion chapter's bounded operators on $H$ (Definition [[§25 The Completeness Relation#^def-25-1|§25.1]]) are the case $X = Y = H$. Since $\|Tx - Tx'\|_Y \le \|T\|\, \|x - x'\|_X$, a bounded linear map is even Lipschitz continuous, uniformly on all of $X$.

^rem-21-1

## Examples

Wu opened Lecture 10 with examples: “in reality we actually need to work on linear maps because nonlinear ones are very difficult.” Whether a map is bounded depends on the norms, not only on the formula.

> [!example] Example §21.1: Differentiation is Bounded from $C^m$ to $C^{m-1}$
> Let $\Omega \subset \mathbb{R}^n$ be bounded and open, and let $C^m(\overline{\Omega})$ be the functions on $\Omega$ whose partial derivatives $\partial^\alpha f$ of all orders $|\alpha| \le m$ exist, are continuous, and extend continuously to the compact set $\overline{\Omega}$, with the norm
>
> $$
> \|f\|_{C^m(\overline{\Omega})} = \sum_{|\alpha| \le m} \|\partial^\alpha f\|_{L^\infty(\Omega)}, \qquad \|g\|_{L^\infty(\Omega)} = \max_{x \in \overline{\Omega}} |g(x)| .
> $$
>
> For $m \ge 1$, $Tf = \partial_{x_1} f$ is a linear map $C^m(\overline{\Omega}) \to C^{m-1}(\overline{\Omega})$, and it is bounded with $\|T\| \le 1$:
>
> $$
> \|Tf\|_{C^{m-1}(\overline{\Omega})} \le \|f\|_{C^m(\overline{\Omega})} \qquad \text{for all } f \in C^m(\overline{\Omega}).
> $$

^ex-21-1

> [!proof]+ Proof
> Linearity is linearity of differentiation. For a multi-index $\beta$ with $|\beta| \le m - 1$, $\partial^\beta(\partial_{x_1} f) = \partial^{\beta + e_1} f$, where $\beta + e_1$ has order $|\beta| + 1 \le m$, and distinct $\beta$ give distinct $\beta + e_1$. So the terms of
>
> $$
> \|Tf\|_{C^{m-1}} = \sum_{|\beta| \le m-1} \|\partial^{\beta + e_1} f\|_{L^\infty}
> $$
>
> are some of the terms of $\|f\|_{C^m} = \sum_{|\alpha| \le m} \|\partial^\alpha f\|_{L^\infty}$, all non-negative, and the inequality follows.

^pf-ex-21-1

*Uses:* [[§21 Boundedness and Continuity#^def-21-2|Def. §21.2]]

> [!remark] Remark
> Wu noted that $C^m(\overline{\Omega})$ is complete in this norm and left that to the class; it is not needed for the example. For $m = 1$ and $\Omega = (a,b)$ it is Part 2 of the proof of Proposition [[§9 Completeness#^pf-9-7|§9.7]].

^rem-21-2

> [!theorem] Proposition §21.3: Differentiation is Unbounded in the Maximum Norm
> Give $C^\infty(\overline{\Omega})$ the norm $\|f\| = \max_{x \in \overline{\Omega}} |f(x)|$ (a norm under which $C^\infty(\overline{\Omega})$ is not complete). Then $Tf = \partial_{x_1} f$ is a linear map $C^\infty(\overline{\Omega}) \to C^\infty(\overline{\Omega})$ that is *not* bounded: there is no $M$ with $\max_{\overline{\Omega}} |\partial_{x_1} f| \le M \max_{\overline{\Omega}} |f|$ for all $f$.

^prop-21-3

> [!proof]+ Proof
> Homework; to be added after submission.

^pf-21-3

> [!remark] Remark
> The two examples have the same formula and opposite answers. In the first, the norm of the target counts one derivative fewer than the norm of the domain, so the derivative taken by $T$ is already paid for; in the second, both norms see only the values of $f$, and “you cannot control derivatives by functions.”

^rem-21-3

> [!example] Example §21.2: The Fourier Transform from $L^1$ to $L^\infty$
> For $f \in L^1(\mathbb{R}^n)$ define
>
> $$
> \mathcal{F}(f)(x) = \int_{\mathbb{R}^n} e^{-i x \cdot \xi} f(\xi)\, d\xi, \qquad x \cdot \xi = \sum_{j=1}^n x_j \xi_j .
> $$
>
> Then $\mathcal{F} : L^1(\mathbb{R}^n) \to L^\infty(\mathbb{R}^n)$ is a bounded linear map with
>
> $$
> \|\mathcal{F}(f)\|_{L^\infty(\mathbb{R}^n)} \le \|f\|_{L^1(\mathbb{R}^n)} .
> $$
>
> *Lax: §16.1, Thm 1(i); §16.3.1*

^ex-21-2

> [!proof]+ Proof
> For fixed $x$, $|e^{-ix\cdot\xi} f(\xi)| = |f(\xi)|$ since $|e^{-ix\cdot\xi}| = 1$, so the integrand is integrable and
>
> $$
> |\mathcal{F}(f)(x)| \le \int_{\mathbb{R}^n} |f(\xi)|\, d\xi = \|f\|_{L^1}
> $$
>
> for every $x$. Changing $f$ on a null set does not change the integral, so $\mathcal{F}$ is defined on classes, and it is linear by linearity of the integral. $\mathcal{F}(f)$ is measurable (in fact continuous: if $x_k \to x$, the integrands converge pointwise and are dominated by $|f|$, so the [[Dominated Convergence Theorem|dominated convergence theorem]] gives $\mathcal{F}(f)(x_k) \to \mathcal{F}(f)(x)$). Hence $\mathcal{F}(f) \in L^\infty$ with $\|\mathcal{F}(f)\|_{L^\infty} \le \|f\|_{L^1}$.

^pf-ex-21-2

*Uses:* [[§14 The Function Spaces Lᵖ(Ω)#^def-14-1|Def. §14.1]], [[§21 Boundedness and Continuity#^def-21-2|Def. §21.2]], [[§15 The General Lebesgue Integral#^prop-15-1|551 §15.1]], [[§15 The General Lebesgue Integral#^thm-15-2|551 §15.2]], [[Dominated Convergence Theorem]]

> [!theorem] Proposition §21.4: Linear Maps on Finite-Dimensional Spaces are Bounded
> Let $X$ and $Y$ be normed linear spaces with $\dim X < \infty$. Every linear map $T : X \to Y$ is bounded.

^prop-21-4

> [!proof]+ Proof
> (Left to the class in lecture.) Let $e_1, \ldots, e_n$ be a basis of $X$ and $\|x\|_1 = \sum_i |a_i|$ for $x = \sum_i a_i e_i$ (Step 2 of the proof of Theorem [[§10 New Normed Spaces from Old#^pf-10-3|§10.3]]). By linearity and the triangle inequality,
>
> $$
> \|Tx\|_Y = \Bigl\| \sum_i a_i\, T e_i \Bigr\|_Y \le \sum_i |a_i|\, \|T e_i\|_Y \le \Bigl( \max_i \|T e_i\|_Y \Bigr) \|x\|_1 .
> $$
>
> By Theorem [[§10 New Normed Spaces from Old#^thm-10-3|§10.3]], $\|x\|_1 \le C\|x\|_X$ for some $C$, so $\|Tx\|_Y \le C \max_i \|Te_i\|_Y\, \|x\|_X$.

^pf-21-4

*Uses:* [[§10 New Normed Spaces from Old#^thm-10-3|§10.3]], [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], [[§21 Boundedness and Continuity#^def-21-2|Def. §21.2]]

> [!remark]- Connections
> - Finite-dimensional home (inner product spaces, where the operator norm is a maximum): [[§27 Consequences of Singular Value Decomposition#^ladr-7-86|LADR 7.86]].

> [!definition] Definition §21.3: The Space $\mathcal{L}(X, Y)$
> $\mathcal{L}(X, Y)$ is the set of all bounded linear maps $T : X \to Y$, with the pointwise operations $(T_1 + T_2)x = T_1 x + T_2 x$ and $(aT)x = a\, Tx$, and the norm $\|T\|$ of Definition [[§21 Boundedness and Continuity#^def-21-2|§21.2]].
>
> *Lax: §15.1, definition of $\mathcal{L}(X, U)$*

^def-21-3

> [!remark]- Connections
> - Finite-dimensional home (all linear maps, same operations): [[§7 Vector Space of Linear Maps#^ladr-3-5|LADR 3.5]].
> - The dual space $X^* = \mathcal{L}(X, \mathbb{F})$ of the companion chapter: [[§24 Bras, Kets, and the Riesz Map#^def-24-1|Def. §24.1]].

> [!theorem] Theorem §21.5: $\mathcal{L}(X, Y)$ is a Normed Linear Space
> Let $X$ and $Y$ be normed linear spaces.
> - (1) $(\mathcal{L}(X, Y), \|\cdot\|)$ is a normed linear space.
> - (2) If $Y$ is complete, then $\mathcal{L}(X, Y)$ is a Banach space.
>
> *Lax: §15.1, Thms 2–3*

^thm-21-5

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

^pf-21-5

*Uses:* [[§9 Completeness#^pf-9-1|§9.1 (Part 1 of the proof)]], [[§1 Linear Spaces#^def-1-1|Def. §1.1]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]], [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], [[§21 Boundedness and Continuity#^def-21-1|Def. §21.1]], [[§21 Boundedness and Continuity#^def-21-2|Def. §21.2]], [[§21 Boundedness and Continuity#^def-21-3|Def. §21.3]], [[§21 Boundedness and Continuity#^prop-21-1|§21.1]]

> [!proof]+ Proof of (2)
> (Lecture 10.) Assume $Y$ is complete, and let $\{T_n\}$ be a Cauchy sequence in $\mathcal{L}(X, Y)$: for every $\varepsilon > 0$ there is $N$ with $\|T_n - T_k\| < \varepsilon$ for all $n, k \ge N$.
>
> **Step 1: pointwise limits.** Fix $x_0 \in X$. By Proposition [[§21 Boundedness and Continuity#^prop-21-1|§21.1]](b),
>
> $$
> \|T_n x_0 - T_k x_0\|_Y = \|(T_n - T_k) x_0\|_Y \le \|T_n - T_k\|\, \|x_0\|_X \le \varepsilon\, \|x_0\|_X \qquad (n, k \ge N),
> $$
>
> so $\{T_n x_0\}$ is a Cauchy sequence in $Y$. Since $Y$ is complete, it converges. Define
>
> $$
> T x_0 = \lim_{n \to \infty} T_n x_0 \qquad (x_0 \in X).
> $$
>
> This is the candidate.
>
> **Step 2: $T$ is linear.** For $a_1, a_2 \in \mathbb{F}$ and $x_1, x_2 \in X$, $T_n(a_1 x_1 + a_2 x_2) = a_1 T_n x_1 + a_2 T_n x_2$. As $n \to \infty$ the left side converges to $T(a_1 x_1 + a_2 x_2)$ and the right side to $a_1 T x_1 + a_2 T x_2$ (since $\|(a_1 T_n x_1 + a_2 T_n x_2) - (a_1 T x_1 + a_2 T x_2)\|_Y \le |a_1|\,\|T_n x_1 - T x_1\|_Y + |a_2|\,\|T_n x_2 - T x_2\|_Y \to 0$). Limits are unique, so $T(a_1 x_1 + a_2 x_2) = a_1 T x_1 + a_2 T x_2$.
>
> **Step 3: the uniform estimate.** Let $\varepsilon > 0$ and $N$ as above. For every $x \in X$ and $n, k \ge N$, $\|T_n x - T_k x\|_Y \le \varepsilon\,\|x\|_X$. Fix $x$ and $k \ge N$. For any $n \ge N$, by the triangle inequality,
>
> $$
> \|T x - T_k x\|_Y \le \|T x - T_n x\|_Y + \|T_n x - T_k x\|_Y \le \|T_n x - T x\|_Y + \varepsilon\, \|x\|_X .
> $$
>
> The left side does not depend on $n$; letting $n \to \infty$, the first term on the right tends to $0$ by Step 1, so
>
> $$
> \|T_k x - T x\|_Y \le \varepsilon\, \|x\|_X \qquad \text{for all } x \in X \text{ and all } k \ge N .
> $$
>
> **Step 4: conclusion.** By Step 2, $T_k - T$ is linear, and by Step 3 it is bounded with $\|T_k - T\| \le \varepsilon$ for $k \ge N$. Since $\mathcal{L}(X, Y)$ is a linear space (part (1)) and $T_k, T_k - T \in \mathcal{L}(X, Y)$, also $T = T_k - (T_k - T) \in \mathcal{L}(X, Y)$. Finally $\|T_k - T\| \le \varepsilon$ for all $k \ge N$ says $T_k \to T$ in $\mathcal{L}(X, Y)$. So every Cauchy sequence converges, and $\mathcal{L}(X, Y)$ is a Banach space.

^pf-21-5-2

*Uses:* [[§21 Boundedness and Continuity#^prop-21-1|§21.1]], [[§21 Boundedness and Continuity#^thm-21-5|§21.5 (1)]], [[§21 Boundedness and Continuity#^def-21-2|Def. §21.2]], [[§21 Boundedness and Continuity#^def-21-3|Def. §21.3]], [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], [[§8 Normed Linear Spaces#^def-8-4|Def. §8.4]], [[§8 Normed Linear Spaces#^def-8-5|Def. §8.5]], [[§8 Normed Linear Spaces#^prop-8-5|§8.5]], [[§9 Completeness#^def-9-1|Def. §9.1]], [[§9 Completeness#^def-9-2|Def. §9.2]]

> [!remark]- Connections
> - Finite-dimensional home of the norm properties: [[§27 Consequences of Singular Value Decomposition#^ladr-7-87|LADR 7.87]].
> - Banach spaces: [[§9 Completeness#^def-9-2|Def. §9.2]]; the special case $Y = \mathbb{F}$ in the companion chapter: [[§24 Bras, Kets, and the Riesz Map#^def-24-1|Def. §24.1]].
> - Part (2) with $Y = \mathbb{F}$: the dual is always a Banach space, [[§22 Dual Spaces#^cor-22-1|§22.1]].

> [!remark] Remark: Why $\varepsilon$ Does Not Depend on $x$
> A student asked whether $\varepsilon$ in Step 3 varies with $x$. It does not: $N$ is chosen from $\|T_n - T_k\| < \varepsilon$ alone, and $\|T_n - T_k\|$ is the supremum of $\|T_n x - T_k x\|_Y/\|x\|_X$ over all $x$, so the single inequality $\|T_n x - T_k x\|_Y \le \varepsilon\|x\|_X$ holds for every $x$ at once. That is what makes $\|T_k - T\| \le \varepsilon$ legitimate at the end. If $N$ depended on $x$, the conclusion would only be pointwise convergence. Wu compared the argument to the proof that a uniformly Cauchy sequence of functions converges uniformly ([[§24 Uniform Convergence#^def-24-2|MATH 451]]): first a pointwise limit, then the uniform bound passes to the limit. The same pattern was used in Part 3 of the proof of Theorem [[§9 Completeness#^pf-9-1|§9.1]].

^rem-21-4

> [!remark] Remark: Comparison with Lax
> Lax states Theorem 1 of §15.1 for Banach spaces $X, U$, but the proof uses no completeness, as Wu remarked. In the ($\Rightarrow$) direction Lax normalizes differently: he rescales $x_n$ to have $|x_n| = 1/\sqrt{n}$, so that $x_n \to 0$ while $|Mx_n| > \sqrt{n} \to \infty$; Wu divides by $n\|x_n\|_X$, so that $\|y_n\|_X = 1/n \to 0$ while $\|Ty_n\|_Y > 1$ merely stays away from $0$. Either contradicts continuity at $0$. Lax proves homogeneity and positivity of the operator norm as “obvious” and leaves subadditivity as his Exercise 1; here it is Wu's board argument.

^rem-21-5
