---
type: section
subject: "[[Functional Analysis]]"
chapter: 7
section: 42
tags: [functional-analysis, math556]
---
← [[§41 The Open Mapping Theorem and Its Consequences]] · ↑ [[· 7 Inverses, Open Maps, and Baire Category]] · [[§43 Weak and Weak-Star Convergence]] →

*Stage: maps — Thread: completeness. Two complete norms that are compatible are equivalent; with the norm $\|x\| + \sup_\alpha \|A_\alpha x\|$ this gives the uniform boundedness principle, and from it the convergence of approximations.*

*Lecture 17 (Tue Nov 3). Source: a classmate's handwritten notes of the lecture (five pages, photographed; no transcript). Statements and proofs follow those notes; additions are marked, and Lax's versions are compared where they differ.*

## The Open Mapping Theorem Revisited

The lecture began by restating the main results of [[§41 The Open Mapping Theorem and Its Consequences|§41]] (the closed graph theorem, Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-4|§41.4]], and the equivalent norm theorem, Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]), together with the more general form of the open mapping theorem announced there, in which $Y$ need not be complete.

> [!theorem] Theorem §42.1: Open Mapping Theorem, General Form
> Let $X$ be a Banach space, $Y$ a normed linear space, and $T \in \mathcal{L}(X, Y)$. Assume $R(T)$ is of the second category in $Y$. Then for every open $O \subset X$, $T(O) = \{ Tx : x \in O \}$ is open in $Y$.
>
> *Lax: §15.5, Thm 16 and Exercise 13 (there $Y$ is a Banach space, and the conclusion is $R(T) = Y$)*

^thm-42-1

> [!proof]+ Proof
> (Stated in lecture, as the weakening announced in the remark *Where Completeness is Used* in [[§41 The Open Mapping Theorem and Its Consequences|§41]].) Only Step 1 of the proof of Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]] used the completeness of $Y$, and only to know that the union $\bigcup_n T(B(0,n))$ is of the second category. Here $R(T) = T(X) = \bigcup_{n=1}^\infty T(B(0,n))$ is of the second category by assumption, so some $T(B(0,n))$ is not nowhere dense in $Y$, i.e. $\overline{T(B(0,n))}$ (closure in $Y$) has an interior point. Steps 2–4 use only the linearity of $T$ and properties of closures in the normed space $Y$; Steps 5–6 use the completeness of $X$ and the continuity of $T$. So $B(0, \delta) \subset T(B(0, 1))$ for some $\delta > 0$, and the proof of Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-2|§41.2]] from Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]], which uses only linearity, shows that $T$ is open.

^pf-42-1

*Uses:* [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]], [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-2|§41.2]]

> [!remark] Remark: The Hypothesis Forces $T$ Onto
> The hypothesis forces $T$ to be onto: $T(X)$ is a linear subspace of $Y$ containing a ball $B(0, \delta)$, and a subspace containing a ball about $0$ is everything ($y = \frac{2\|y\|}{\delta} \cdot \frac{\delta\, y}{2\|y\|}$ for $y \neq 0$). So the general form says: *if $X$ is Banach and $R(T)$ is of the second category, then $T$ is onto and open.* When $Y$ is Banach and $T$ is onto, $R(T) = Y$ is of the second category by Baire, and Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-2|§41.2]] is recovered.

^xrem-42-1

> [!remark] Remark: $Y$ Turns Out to Be Complete
> *(Not from lecture; filled in.)* Lax states this theorem with $Y$ a Banach space. Allowing $Y$ to be only normed gains nothing in the end: under the hypothesis, $Y$ *is* complete. Let $\{y_k\}$ be Cauchy in $Y$ and $\delta$ as in the proof ($B(0, \delta) \subset T(B(0,1))$, so $B(0, \rho\delta) \subset T(B(0, \rho))$ for $\rho > 0$). Pass to a subsequence with $\|y_{k+1} - y_k\| < \delta\, 2^{-k}$; it suffices that this subsequence converges, because a Cauchy sequence with a convergent subsequence converges. Choose $x_k \in X$ with $Tx_k = y_{k+1} - y_k$ and $\|x_k\| < 2^{-k}$. Then $\sum_k \|x_k\| < \infty$, so $\sum_k x_k$ converges in the Banach space $X$ to some $x$ (as in Step 6 of the proof of Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]]), and by continuity and linearity of $T$,
>
> $$
> y_{K+1} - y_1 = T\Bigl( \sum_{k=1}^{K} x_k \Bigr) \longrightarrow Tx \qquad (K \to \infty),
> $$
>
> so $y_K \to y_1 + Tx$. Hence $Y$ is a Banach space, and the general form is the open mapping theorem for the Banach spaces $X$ and $Y$ with the hypothesis “onto” replaced by the weaker-looking “range of the second category”. This is Lax's Theorem 16, and in Rudin's *Functional Analysis* (Theorem 2.11) the same argument is carried out for complete metric linear spaces.

^xrem-42-2

## A Second Equivalent Norm Theorem

The equivalent norm theorem needs the two norms to be comparable. The following version replaces comparability by a compatibility condition on limits.

> [!theorem] Theorem §42.4: Equivalent Norm Theorem, Second Version
> Let $X$ be a linear space and $\|\cdot\|_1$, $\|\cdot\|_2$ two norms on $X$. Assume $(X, \|\cdot\|_1)$ and $(X, \|\cdot\|_2)$ are complete, and assume further that for every sequence $\{x_n\} \subset X$,
>
> $$
> x_n \to x^{(1)} \text{ in } (X, \|\cdot\|_1) \quad \text{and} \quad x_n \to x^{(2)} \text{ in } (X, \|\cdot\|_2) \implies x^{(1)} = x^{(2)} .
> $$
>
> Then $\|\cdot\|_1$ and $\|\cdot\|_2$ are equivalent.
>
> *Lax: §15.5, Thm 13*

^thm-42-4

> [!proof]+ Proof
> We use the closed graph theorem. $(X, \|\cdot\|_1)$ and $(X, \|\cdot\|_2)$ are Banach spaces by assumption. Consider the identity $i : X \to X$, $x \mapsto x$, as a map $i : (X, \|\cdot\|_1) \to (X, \|\cdot\|_2)$, defined on all of $X$. By the assumption it is a closed linear map:
> its graph is $G = \{ (x, x) : x \in X \}$, and if $(x_n, x_n) \in G$ converges to $(x^{(1)}, x^{(2)})$ in $(X, \|\cdot\|_1) \times (X, \|\cdot\|_2)$, i.e. $x_n \to x^{(1)}$ in $\|\cdot\|_1$ and $x_n \to x^{(2)}$ in $\|\cdot\|_2$, then $x^{(2)} = x^{(1)} = i(x^{(1)})$. By Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-4|§41.4]], $i : (X, \|\cdot\|_1) \to (X, \|\cdot\|_2)$ is a bounded linear map, so there is $c > 0$ with
>
> $$
> \|x\|_2 \le c\, \|x\|_1 \qquad \text{for all } x \in X .
> $$
>
> By the equivalent norm theorem (Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]), $\|\cdot\|_1$ and $\|\cdot\|_2$ are equivalent.
>
> *(Lax's proof.)* The compatibility condition is symmetric, so the closed graph theorem applies equally to $i : (X, \|\cdot\|_2) \to (X, \|\cdot\|_1)$; Lax obtains both inequalities this way, without the equivalent norm theorem.

^pf-42-4

*Uses:* [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-4|§41.4]], [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]

> [!remark] Remark: The Compatibility Condition is Needed
> Completeness of both norms alone does not suffice. On an infinite-dimensional Banach space $(X, \|\cdot\|_1)$, choose a Hamel basis normalized to $\|e\|_1 = 1$, pick countably many of its elements $e_1, e_2, \ldots$, and let $\varphi$ be the linear map with $\varphi(e_k) = k\, e_k$ that fixes the other basis elements. It is a linear bijection (its inverse multiplies $e_k$ by $1/k$) and is unbounded. *(Not from lecture.)* Then $\|x\|_2 = \|\varphi x\|_1$ is a complete norm ($\varphi$ is an isometry of $(X, \|\cdot\|_2)$ onto $(X, \|\cdot\|_1)$), but $\|e_k\|_2 = k$ while $\|e_k\|_1 = 1$, so the norms are not equivalent; the compatibility condition fails.

^xrem-42-3

## The Uniform Boundedness Principle

> [!theorem] Theorem §42.5: Uniform Boundedness Principle
> Let $X$ be a Banach space and $Y$ a normed linear space. Assume $\{A_\alpha\}_{\alpha \in \Lambda}$ is a family of bounded linear maps from $X$ to $Y$ satisfying: for every given $x \in X$,
>
> $$
> \sup_{\alpha \in \Lambda} \|A_\alpha x\| < \infty .
> $$
>
> Then there is $C_0 > 0$ such that $\sup_{\alpha \in \Lambda} \|A_\alpha\| \le C_0 < \infty$. In other words: pointwise bounded $\Rightarrow$ uniformly bounded.
>
> *Lax: §10.1, Thms 2–3 (proved from the Baire category principle); §15.3, Thm 7 (for operators, assuming only $|\ell(A_\alpha x)| \le c(x, \ell)$, with $Y$ Banach)*

^thm-42-5

> [!proof]+ Proof
> $(X, \|\cdot\|_X)$ is a Banach space by assumption. Define
>
> $$
> \|x\|_2 = \|x\|_X + \sup_{\alpha \in \Lambda} \|A_\alpha x\|_Y , \qquad x \in X .
> $$
>
> *$\|\cdot\|_2$ is a norm* (left as an exercise).
> It is finite by the assumption of pointwise boundedness. Homogeneity: $\|A_\alpha(ax)\|_Y = |a|\,\|A_\alpha x\|_Y$, and constants pull out of suprema. Triangle inequality: $\|A_\alpha(x + x')\|_Y \le \|A_\alpha x\|_Y + \|A_\alpha x'\|_Y \le \sup_\beta \|A_\beta x\|_Y + \sup_\beta \|A_\beta x'\|_Y$ for every $\alpha$; take the supremum over $\alpha$ and add $\|x + x'\|_X \le \|x\|_X + \|x'\|_X$. Positivity: $\|x\|_2 \ge \|x\|_X$. In particular $\|x\|_X \le \|x\|_2$.
>
> *$(X, \|\cdot\|_2)$ is complete.* Let $\{x_n\}$ be Cauchy in $(X, \|\cdot\|_2)$: for every $\varepsilon > 0$ there is $N$ such that for all $n, m > N$
>
> $$
> \|x_n - x_m\|_2 = \|x_n - x_m\|_X + \sup_{\alpha \in \Lambda} \|A_\alpha x_n - A_\alpha x_m\|_Y < \varepsilon . \tag{$\ast$}
> $$
>
> Hence $\|x_n - x_m\|_X < \varepsilon$ and $\|A_\alpha x_n - A_\alpha x_m\|_Y < \varepsilon$ for all $\alpha \in \Lambda$ and $n, m > N$: $\{x_n\}$ is Cauchy in $(X, \|\cdot\|_X)$ (and each $\{A_\alpha x_n\}$ is Cauchy in $Y$). Since $(X, \|\cdot\|_X)$ is complete, there is $x_0 \in X$ with $x_n \to x_0$ in $(X, \|\cdot\|_X)$. Each $A_\alpha \in \mathcal{L}(X, Y)$ is continuous, so $A_\alpha x_n \to A_\alpha x_0$ in $(Y, \|\cdot\|_Y)$ for every $\alpha \in \Lambda$. By $(\ast)$, for all $n, m > N$ and every $\alpha$,
>
> $$
> \|x_n - x_m\|_X + \|A_\alpha x_n - A_\alpha x_m\|_Y < \varepsilon .
> $$
>
> Let $m \to \infty$: $\|x_n - x_0\|_X + \|A_\alpha x_n - A_\alpha x_0\|_Y \le \varepsilon$ for every $\alpha$ and $n > N$. Taking the supremum over $\alpha$,
>
> $$
> \|x_n - x_0\|_X + \sup_{\alpha \in \Lambda} \|A_\alpha x_n - A_\alpha x_0\|_Y = \|x_n - x_0\|_2 \le \varepsilon \qquad (n > N) .
> $$
>
> So $x_n \to x_0$ in $\|\cdot\|_2$, and $(X, \|\cdot\|_2)$ is a Banach space.
> (The limit $A_\alpha x_0$ comes from continuity of $A_\alpha$, not from completeness of $Y$; this is why $Y$ need only be normed.)
>
> *Conclusion.* By the equivalent norm theorem (Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]), there is $C_0 > 0$ such that for all $x \in X$
>
> $$
> \|x\|_2 = \|x\|_X + \sup_{\alpha \in \Lambda} \|A_\alpha x\|_Y \le C_0\, \|x\|_X .
> $$
>
> Hence $\|A_\alpha x\|_Y \le (C_0 - 1)\|x\|_X$ for all $\alpha$ and $x$, i.e. $\sup_{\alpha \in \Lambda} \|A_\alpha\| \le C_0 - 1 < \infty$.

^pf-42-5

*Uses:* [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]

> [!remark] Remark: Completeness of $X$ is Needed
> Let $c_{00}$ be the finitely supported sequences with $\|x\| = \max_n |x_n|$ (not complete), and $A_n x = n\, x_n$, a bounded linear functional with $\|A_n\| = n$. For each fixed $x \in c_{00}$, $A_n x = 0$ once $n$ exceeds the support of $x$, so $\sup_n |A_n x| < \infty$; but $\sup_n \|A_n\| = \infty$. The proof breaks exactly at the completeness of $(X, \|\cdot\|_2)$. The proof here is the closed-graph route; the more common proof, Lax's (§10.1, Theorem 2), applies Baire directly to the closed sets $\{ x : \sup_\alpha \|A_\alpha x\| \le k \}$: one of them contains a ball, and subadditivity and homogeneity of $x \mapsto \|A_\alpha x\|$ carry the bound to the unit ball. Lax's Theorem 7 of §15.3 assumes even less, only that each $\ell(A_\alpha x)$, $\ell \in Y'$, is bounded, and reduces to the present case by applying the principle twice.

^xrem-42-4

## The Banach–Steinhaus Theorem

> [!theorem] Theorem §42.6: Banach–Steinhaus
> Let $X$ be a Banach space and $Y$ a normed linear space. Let $\{A_n\}$ be a sequence of bounded linear maps $X \to Y$, and $A \in \mathcal{L}(X, Y)$. Then $\lim_{n \to \infty} A_n x = Ax$ for all $x \in X$ if and only if
>
> 1. $\sup_{n \in \mathbb{N}} \|A_n\| < \infty$, and
> 2. $\lim_{n \to \infty} A_n x = Ax$ for all $x \in D$, where $D$ is a dense subset of $X$.
>
> *Lax: §15.2, Thm 6 (the direction $\Leftarrow$); §15.3, Thm 7 and Cor 7$'$ (the direction $\Rightarrow$)*

^thm-42-6

> [!proof]+ Proof
> **($\Rightarrow$)** By the uniform boundedness principle.
> For each $x$, the sequence $\{A_n x\}$ converges in $Y$, hence is bounded: $\sup_n \|A_n x\| < \infty$. Theorem [[§42 Uniform Boundedness and Approximation#^thm-42-5|§42.5]] gives (1). (2) holds with $D = X$.
>
> **($\Leftarrow$)** Assume $\sup_n \|A_n\| + \|A\| \le M < \infty$, and that $D$ is a dense subset of $X$ with $A_n y \to Ay$ for every $y \in D$. Let $x \in X$; we want $\|A_n x - Ax\| \to 0$. For every $y \in D$,
>
> $$
> \begin{aligned}\|A_n x - Ax\| &= \|A_n y - Ay + A_n(x - y) - A(x - y)\| \\
> &\le \|A_n y - Ay\| + \bigl( \|A_n\| + \|A\| \bigr) \|x - y\| \\
> &\le \|A_n y - Ay\| + M\, \|x - y\| .\end{aligned}
> $$
>
> Given $\varepsilon > 0$, first choose $y \in D$ with $M\|x - y\| < \varepsilon/2$ (density), then $N$ with $\|A_n y - Ay\| < \varepsilon/2$ for $n > N$. Then $\|A_n x - Ax\| < \varepsilon$ for $n > N$.

^pf-42-6

*Uses:* [[§42 Uniform Boundedness and Approximation#^thm-42-5|§42.5]]

> [!remark] Remark: Which Hypotheses Each Direction Uses
> *(Not from lecture.)* Only ($\Rightarrow$) uses the completeness of $X$, through the uniform boundedness principle; ($\Leftarrow$) is an $\varepsilon/2$ argument valid in any normed spaces. Lax's Theorem 6 (§15.2) is a variant of ($\Leftarrow$) in which no limit $A$ is given: if $\sup_n \|A_n\| < \infty$ and $\lim A_n x$ exists for $x$ in a dense set, then it exists for all $x$; there $Y$ must be complete, since the limit has to be produced (the same $\varepsilon/2$ estimate shows that $\{A_n x\}$ is Cauchy).

^rem-42-3

## The Lax Equivalence Theorem

Consider the equation $Tx = y$, with $T : X \to Y$ one-to-one, onto and bounded. In practice $T$ is replaced by an approximation $T_n : X \to Y$ (a discretization), also one-to-one and onto, and one solves

$$
T_n x_n = y .
$$

*Question:* does $x_n \to x_0$, where $Tx_0 = y$?

> [!theorem] Theorem §42.8: Lax Equivalence Theorem
> Let $X, Y$ be Banach spaces. Assume $T_n \in \mathcal{L}(X, Y)$ for $n \ge 1$ and $T \in \mathcal{L}(X, Y)$, with $T_n : X \to Y$ and $T : X \to Y$ one-to-one and onto. Assume that for every given $x \in X$, $\lim_{n \to \infty} T_n x = Tx$. Then
>
> $$
> \lim_{n \to \infty} T_n^{-1} y = T^{-1} y \quad \text{for all } y \in Y \qquad \iff \qquad \sup_{n} \|T_n^{-1} y\| < \infty \quad \text{for all } y \in Y .
> $$
>
> *Lax: §34.3, Thm 8 (Lax's equivalence theorem, for difference approximations of a semigroup)*

^thm-42-8

> [!proof]+ Proof
> **($\Rightarrow$)** Trivial, because a convergent sequence is bounded.
>
> **($\Leftarrow$)** The open mapping theorem (in the form of Banach's theorem, Theorem [[§39 Solving Mx = y#^thm-39-2|§39.2]]) gives $T_n^{-1} \in \mathcal{L}(Y, X)$ and $T^{-1} \in \mathcal{L}(Y, X)$, and the uniform boundedness principle gives
>
> $$
> \sup_{n \in \mathbb{N}} \|T_n^{-1}\| + \|T^{-1}\| \le M < \infty .
> $$
>
> (Theorem [[§42 Uniform Boundedness and Approximation#^thm-42-5|§42.5]] is applied to the family $\{T_n^{-1}\}$ of bounded linear maps from the Banach space $Y$ to $X$, which is pointwise bounded by assumption.) We want: for every $y \in Y$, $\|T_n^{-1} y - T^{-1} y\| \to 0$. Write
>
> $$
> T_n^{-1} y - T^{-1} y = T_n^{-1}\bigl( y - T_n(T^{-1} y) \bigr) = T_n^{-1}\bigl( T(T^{-1} y) - T_n(T^{-1} y) \bigr) .
> $$
>
> Hence, with $x = T^{-1} y$,
>
> $$
> \|T_n^{-1} y - T^{-1} y\| \le \|T_n^{-1}\|\, \bigl\| T(T^{-1} y) - T_n(T^{-1} y) \bigr\| \le M\, \|T_n x - Tx\| \to 0
> $$
>
> by assumption.

^pf-42-8

*Uses:* [[§39 Solving Mx = y#^thm-39-2|§39.2]], [[§42 Uniform Boundedness and Approximation#^thm-42-5|§42.5]]

> [!remark] Remark: Consistency $+$ Stability $=$ Convergence
> In numerical analysis the three conditions have names. $T_n x \to Tx$ for every $x$ is *consistency*: the discrete operator approximates the true one. $\sup_n \|T_n^{-1}\| < \infty$ is *stability*: errors in the data are not amplified uniformly in $n$, which by the uniform boundedness principle is the same as $\sup_n \|T_n^{-1} y\| < \infty$ for each $y$. $T_n^{-1} y \to T^{-1} y$ is *convergence* of the approximate solutions. The theorem says: for a consistent scheme, stability is equivalent to convergence. The identity $T_n^{-1} - T^{-1} = T_n^{-1}(T - T_n)T^{-1}$ is the heart of the proof. (Lax proved the version for initial value problems in 1956, with Richtmyer. In Lax's book it is Theorem 8 of §34.3: an approximation $u^{(n)} = C_h^n x$ of a semigroup $Z(t)$, consistent with its generator, converges to $Z(t)x$ for all $x$ if and only if it is stable, $|C_h^n| \le \text{const}$ for $nh \le 1$. Necessity is again the uniform boundedness principle, and sufficiency rests on a telescoping identity for $C_h^n - Z(nh)$ of the same kind as the identity above. The version in the lecture is the stationary one, for equations $Tx = y$.)

^rem-42-4
