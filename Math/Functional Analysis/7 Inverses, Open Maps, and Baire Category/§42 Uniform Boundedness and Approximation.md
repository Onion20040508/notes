---
type: section
subject: "[[Functional Analysis]]"
chapter: 7
section: 42
tags: [functional-analysis, math556]
---
← [[§41 The Open Mapping Theorem and Its Consequences]] · ↑ [[· 7 Inverses, Open Maps, and Baire Category]] · [[§43 Weak and Weak-Star Convergence]] →

*Stage: maps — Thread: completeness. Two complete norms that are comparable or compatible are equivalent; with the norm $\|x\| + \sup_\alpha \|A_\alpha x\|$ this gives the uniform boundedness principle, and from it the convergence of approximations.*

*Lecture 17 (Tue Nov 3). Source: a classmate's handwritten notes of the lecture (five pages, photographed; no transcript). Statements and proofs follow those notes; additions are marked, and Lax's versions are compared where they differ.*

## The Open Mapping Theorem Revisited

The main results of [[§41 The Open Mapping Theorem and Its Consequences|§41]] are the closed graph theorem (Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-4|§41.4]]) and the equivalent norm theorem (Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]). The open mapping theorem has a more general form, announced there in the remark *[[§41 The Open Mapping Theorem and Its Consequences#^rem-41-1|Where Completeness is Used]]*, in which $Y$ need not be complete. Its core is the following lemma.

> [!theorem] Lemma §42.1: The Image of the Unit Ball Contains a Ball About $0$; General Form
> *(Not from lecture; filled in.)* Let $X$ be a Banach space, $Y$ a normed linear space, and $M \in \mathcal{L}(X, Y)$. Assume $R(M)$ is of the second category in $Y$ (Definition [[§40 The Baire Category Theorem#^def-40-3|§40.3]]). Then there is $\delta > 0$ such that
>
> $$
> B(0, \delta) \subset M\bigl( B(0, 1) \bigr) .
> $$

^lem-42-1

> [!proof]+ Proof
> We go through the six steps of the proof of Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]] and check that each holds under the present hypotheses.
>
> **Step 1.** As there, $X = \bigcup_{n=1}^\infty B(0, n)$, so
>
> $$
> R(M) = M(X) = \bigcup_{n=1}^\infty M\bigl( B(0, n) \bigr) .
> $$
>
> If every $M(B(0,n))$ were nowhere dense in $Y$, then $R(M)$ would be a countable union of nowhere dense subsets of $Y$, that is, of the first category (Definition [[§40 The Baire Category Theorem#^def-40-2|§40.2]]), contrary to the assumption. So there is $n \in \mathbb{N}$ such that $M(B(0,n))$ is not nowhere dense: its closure $\overline{M(B(0,n))}$ in $Y$ has an interior point (Definition [[§40 The Baire Category Theorem#^def-40-1|§40.1]]), i.e. there are $z_0 \in Y$ and $r > 0$ with $B(z_0, r) \subset \overline{M(B(0,n))}$. This is the conclusion of Step 1 of the proof of Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]], and Step 1 is the only place where that proof uses the completeness of $Y$ and the assumption $R(M) = Y$.
>
> **Steps 2–4.** These steps use only the linearity of $M$, the symmetry and convexity of the ball $B(0, n)$, and the fact that in a normed linear space limits of sums and of scalar multiples are the sums and scalar multiples of the limits. They hold in the normed space $Y$ without change and give $\delta > 0$ with
>
> $$
> B(0, 3\rho\delta) \subset \overline{M\bigl( B(0, \rho) \bigr)} \qquad \text{for all } \rho > 0 .
> $$
>
> **Steps 5–6.** These steps use this inclusion, the completeness of $X$ (to sum the corrections $x_j$), and the continuity of $M$ (to pass to the limit in $M(\sum_{j=0}^n x_j)$). They give $B(0, \delta) \subset M(B(0, 1))$.

^pf-42-1

*Uses:* [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]], [[§40 The Baire Category Theorem#^def-40-2|Def. §40.2]], [[§40 The Baire Category Theorem#^def-40-1|Def. §40.1]]

> [!theorem] Theorem §42.2: Open Mapping Theorem, General Form
> Let $X$ be a Banach space, $Y$ a normed linear space, and $M \in \mathcal{L}(X, Y)$. Assume $R(M)$ is [[§40 The Baire Category Theorem#^def-40-3|of the second category]] in $Y$ (Definition [[§40 The Baire Category Theorem#^def-40-3|§40.3]]). Then for every open $O \subset X$, $M(O) = \{ Mx : x \in O \}$ is open in $Y$.
>
> *Lax: §15.5, Thm 16 and Exercise 13 (there $Y$ is a Banach space, and the conclusion is $R(M) = Y$)*

^thm-42-2

> [!proof]+ Proof
> *(Stated in lecture without proof; the proof is filled in.)* By Lemma [[§42 Uniform Boundedness and Approximation#^lem-42-1|§42.1]] there is $\delta > 0$ with $B(0, \delta) \subset M(B(0, 1))$. The proof of Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-2|§41.2]] uses only this inclusion and the linearity of $M$: for $O \subset X$ open, $x_0 \in O$ and $r > 0$ with $B(x_0, r) \subset O$, it shows
>
> $$
> B(Mx_0, r\delta) \subset M\bigl( B(x_0, r) \bigr) \subset M(O) .
> $$
>
> So every point $Mx_0$ of $M(O)$ has a ball about it inside $M(O)$, and $M(O)$ is open in $Y$.

^pf-42-2

*Uses:* [[§42 Uniform Boundedness and Approximation#^lem-42-1|§42.1]], [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-2|§41.2]]

> [!theorem] Corollary §42.3: The General Form Forces $M$ Onto
> *(Not from lecture; the statement with $Y$ a Banach space is HW9, Problem 4.)* Let $X$ be a Banach space, $Y$ a normed linear space, and $M \in \mathcal{L}(X, Y)$ with $R(M)$ of the second category in $Y$. Then $M$ is onto. Together with Theorem [[§42 Uniform Boundedness and Approximation#^thm-42-2|§42.2]]: *if $X$ is Banach and $R(M)$ is of the second category, then $M$ is onto and open.*
>
> *Source: HW9, Problem 4 (for $Y$ a Banach space)*

^cor-42-3

> [!proof]+ Proof
> $M(X)$ is a linear subspace of $Y$, since $M$ is linear. It contains a ball about $0$: Lemma [[§42 Uniform Boundedness and Approximation#^lem-42-1|§42.1]] gives $\delta > 0$ with $B(0, \delta) \subset M(B(0, 1)) \subset M(X)$. A linear subspace $V \subset Y$ containing $B(0, \delta)$ is all of $Y$: $0 \in V$, and for $y \neq 0$ the vector $z = \frac{\delta\, y}{2\|y\|}$ has $\|z\| = \frac{\delta}{2} < \delta$, so $z \in V$, and then
>
> $$
> y = \frac{2\|y\|}{\delta} \cdot \frac{\delta\, y}{2\|y\|} = \frac{2\|y\|}{\delta}\, z \in V ,
> $$
>
> because $V$ is closed under scalar multiplication. Hence $M(X) = Y$. That $M$ is open is Theorem [[§42 Uniform Boundedness and Approximation#^thm-42-2|§42.2]].

^pf-42-3

*Uses:* [[§42 Uniform Boundedness and Approximation#^lem-42-1|§42.1]], [[§42 Uniform Boundedness and Approximation#^thm-42-2|§42.2]]

When $Y$ is a Banach space and $M$ is onto, $R(M) = Y$ is of the second category by Baire (Theorem [[§40 The Baire Category Theorem#^thm-40-4|§40.4]]), and Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-2|§41.2]] is recovered from the general form.

> [!theorem] Proposition §42.4: $Y$ Turns Out to Be Complete
> *(Not from lecture; filled in.)* Under the hypotheses of Theorem [[§42 Uniform Boundedness and Approximation#^thm-42-2|§42.2]] ($X$ a Banach space, $Y$ a normed linear space, $M \in \mathcal{L}(X, Y)$, $R(M)$ of the second category in $Y$), $Y$ is a Banach space.

^prop-42-4

> [!proof]+ Proof
> Let $\{y_k\}$ be Cauchy in $Y$, and let $\delta > 0$ be as in Lemma [[§42 Uniform Boundedness and Approximation#^lem-42-1|§42.1]]: $B(0, \delta) \subset M(B(0,1))$. Then $B(0, \rho\delta) \subset M(B(0, \rho))$ for every $\rho > 0$: if $\|y\| < \rho\delta$, then $y/\rho \in B(0, \delta)$, so $y/\rho = Mx$ with $\|x\| < 1$, and $y = M(\rho x)$ with $\|\rho x\| < \rho$.
>
> *Reduction to a subsequence.* It suffices that some subsequence converges, because a Cauchy sequence with a convergent subsequence converges: if $y_{k_j} \to y$, then $\|y_k - y\| \le \|y_k - y_{k_j}\| + \|y_{k_j} - y\|$, and both terms are small for $k$ and $j$ large. Choose $k_1 < k_2 < \cdots$ with $\|y_m - y_n\| < \delta\, 2^{-j}$ for all $m, n \ge k_j$; then $\|y_{k_{j+1}} - y_{k_j}\| < \delta\, 2^{-j}$. Renaming, we may assume $\|y_{k+1} - y_k\| < \delta\, 2^{-k}$ for all $k$.
>
> *Lifting the increments.* Since $y_{k+1} - y_k \in B(0, \delta\, 2^{-k}) \subset M(B(0, 2^{-k}))$, choose $x_k \in X$ with $Mx_k = y_{k+1} - y_k$ and $\|x_k\| < 2^{-k}$. Then $\sum_k \|x_k\| < \infty$, so $\sum_k x_k$ converges in the Banach space $X$ to some $x$ (as in Step 6 of the proof of Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]]).
>
> *Conclusion.* By linearity of $M$ the sum telescopes, and by continuity of $M$,
>
> $$
> y_{K+1} - y_1 = M\Bigl( \sum_{k=1}^{K} x_k \Bigr) \longrightarrow Mx \qquad (K \to \infty),
> $$
>
> so $y_K \to y_1 + Mx$. Hence every Cauchy sequence in $Y$ converges, and $Y$ is a Banach space.

^pf-42-4

*Uses:* [[§42 Uniform Boundedness and Approximation#^lem-42-1|§42.1]], [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]]

> [!remark] Remark: What the General Form Gains
> *(Not from lecture.)* Lax states this theorem with $Y$ a Banach space. Allowing $Y$ to be only normed gains nothing in the end: under the hypothesis, $Y$ *is* complete (Proposition [[§42 Uniform Boundedness and Approximation#^prop-42-4|§42.4]]). So the general form is the open mapping theorem for the Banach spaces $X$ and $Y$ with the hypothesis “onto” replaced by the weaker-looking “range of the second category”. This is Lax's Theorem 16, and in Rudin's *Functional Analysis* (Theorem 2.11) the same argument is carried out for complete metric linear spaces.

^rem-42-1

## A Second Equivalent Norm Theorem

The equivalent norm theorem needs the two norms to be comparable. The following version replaces comparability by a compatibility condition on limits.

> [!theorem] Theorem §42.5: Equivalent Norm Theorem, Second Version
> Let $X$ be a linear space and $\|\cdot\|_1$, $\|\cdot\|_2$ two norms on $X$. Assume $(X, \|\cdot\|_1)$ and $(X, \|\cdot\|_2)$ are complete, and assume further that for every sequence $\{x_n\} \subset X$,
>
> $$
> x_n \to x^{(1)} \text{ in } (X, \|\cdot\|_1) \quad \text{and} \quad x_n \to x^{(2)} \text{ in } (X, \|\cdot\|_2) \implies x^{(1)} = x^{(2)} .
> $$
>
> Then $\|\cdot\|_1$ and $\|\cdot\|_2$ are equivalent.
>
> *Lax: §15.5, Thm 13*

^thm-42-5

> [!proof]+ Proof
> We use the closed graph theorem. $(X, \|\cdot\|_1)$ and $(X, \|\cdot\|_2)$ are Banach spaces by assumption. Consider the identity $i : X \to X$, $x \mapsto x$, as a map $i : (X, \|\cdot\|_1) \to (X, \|\cdot\|_2)$, defined on all of $X$. By the assumption it is a closed linear map: its graph is $G = \{ (x, x) : x \in X \}$, and if $(x_n, x_n) \in G$ converges to $(x^{(1)}, x^{(2)})$ in $(X, \|\cdot\|_1) \times (X, \|\cdot\|_2)$, i.e. $x_n \to x^{(1)}$ in $\|\cdot\|_1$ and $x_n \to x^{(2)}$ in $\|\cdot\|_2$, then $x^{(2)} = x^{(1)} = i(x^{(1)})$. By Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-4|§41.4]], $i : (X, \|\cdot\|_1) \to (X, \|\cdot\|_2)$ is a bounded linear map, so there is $c > 0$ with
>
> $$
> \|x\|_2 \le c\, \|x\|_1 \qquad \text{for all } x \in X .
> $$
>
> By the equivalent norm theorem (Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]), $\|\cdot\|_1$ and $\|\cdot\|_2$ are equivalent.
>
> *(Lax's proof.)* The compatibility condition is symmetric, so the closed graph theorem applies equally to $i : (X, \|\cdot\|_2) \to (X, \|\cdot\|_1)$; Lax obtains both inequalities this way, without the equivalent norm theorem.

^pf-42-5

*Uses:* [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-4|§41.4]], [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]

> [!example] Example §42.1: Two Complete Norms That Are Not Equivalent
> *(Not from lecture.)* Completeness of both norms alone does not suffice in Theorem [[§42 Uniform Boundedness and Approximation#^thm-42-5|§42.5]]; the compatibility condition is needed.
>
> On an infinite-dimensional Banach space $(X, \|\cdot\|_1)$, choose a Hamel basis (a linearly independent set whose finite linear combinations give all of $X$; it exists by Zorn's lemma, by the argument of Example [[§24 The Parallelogram Law and Jordan–von Neumann#^ex-24-1|§24.1]]) normalized to $\|e\|_1 = 1$, pick countably many of its elements $e_1, e_2, \ldots$, and let $\varphi : X \to X$ be the linear map with $\varphi(e_k) = k\, e_k$ that fixes the other basis elements. Put $\|x\|_2 = \|\varphi x\|_1$.
>
> 1. *$\varphi$ is a linear bijection and is unbounded.* Let $\psi$ be the linear map with $\psi(e_k) = e_k / k$ that fixes the other basis elements. Then $\psi\varphi$ and $\varphi\psi$ fix every basis element, so both are the identity, and $\varphi$ is bijective with inverse $\psi$. It is unbounded, since $\|e_k\|_1 = 1$ and $\|\varphi e_k\|_1 = k$.
> 2. *$\|\cdot\|_2$ is a complete norm.* It is a norm: $\|x\|_2 \ge 0$, with $\|x\|_2 = 0$ iff $\varphi x = 0$ iff $x = 0$ ($\varphi$ is one-to-one); homogeneity and the triangle inequality follow from the linearity of $\varphi$ and the corresponding properties of $\|\cdot\|_1$. By definition $\varphi$ is an isometry of $(X, \|\cdot\|_2)$ onto $(X, \|\cdot\|_1)$. If $\{x_n\}$ is Cauchy in $\|\cdot\|_2$, then $\{\varphi x_n\}$ is Cauchy in $\|\cdot\|_1$, so $\varphi x_n \to z$ for some $z \in X$; with $x = \psi z$, $\|x_n - x\|_2 = \|\varphi x_n - z\|_1 \to 0$.
> 3. *The norms are not equivalent.* $\|e_k\|_2 = \|k\, e_k\|_1 = k$ while $\|e_k\|_1 = 1$, so there is no $c$ with $\|x\|_2 \le c\, \|x\|_1$ for all $x$.
> 4. *The compatibility condition fails.* Otherwise Theorem [[§42 Uniform Boundedness and Approximation#^thm-42-5|§42.5]] would make the two complete norms equivalent, contradicting (3).

^ex-42-1

## The Uniform Boundedness Principle

> [!theorem] Theorem §42.6: Uniform Boundedness Principle
> Let $X$ be a Banach space and $Y$ a normed linear space. Assume $\{A_\alpha\}_{\alpha \in \Lambda}$ is a family of bounded linear maps from $X$ to $Y$ satisfying: for every given $x \in X$,
>
> $$
> \sup_{\alpha \in \Lambda} \|A_\alpha x\| < \infty .
> $$
>
> Then there is $C_0 > 0$ such that $\sup_{\alpha \in \Lambda} \|A_\alpha\| \le C_0 < \infty$. In other words: pointwise bounded $\Rightarrow$ uniformly bounded.
>
> *Lax: §10.1, Thms 2–3 (proved from the Baire category principle); §15.3, Thm 7 (for operators, assuming only $|\ell(A_\alpha x)| \le c(x, \ell)$, with $Y$ Banach)*

^thm-42-6

> [!proof]+ Proof
> $(X, \|\cdot\|_X)$ is a Banach space by assumption. Define
>
> $$
> \|x\|_2 = \|x\|_X + \sup_{\alpha \in \Lambda} \|A_\alpha x\|_Y , \qquad x \in X .
> $$
>
> *$\|\cdot\|_2$ is a norm.* It is finite by the assumption of pointwise boundedness. Homogeneity: $\|A_\alpha(ax)\|_Y = |a|\,\|A_\alpha x\|_Y$, and constants pull out of suprema. Triangle inequality: $\|A_\alpha(x + x')\|_Y \le \|A_\alpha x\|_Y + \|A_\alpha x'\|_Y \le \sup_\beta \|A_\beta x\|_Y + \sup_\beta \|A_\beta x'\|_Y$ for every $\alpha$; take the supremum over $\alpha$ and add $\|x + x'\|_X \le \|x\|_X + \|x'\|_X$. Positivity: $\|x\|_2 \ge \|x\|_X$. In particular $\|x\|_X \le \|x\|_2$.
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
> So $x_n \to x_0$ in $\|\cdot\|_2$, and $(X, \|\cdot\|_2)$ is a Banach space. (The limit $A_\alpha x_0$ comes from continuity of $A_\alpha$, not from completeness of $Y$; this is why $Y$ need only be normed.)
>
> *Conclusion.* By the equivalent norm theorem (Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]), there is $C > 0$ such that for all $x \in X$
>
> $$
> \|x\|_2 = \|x\|_X + \sup_{\alpha \in \Lambda} \|A_\alpha x\|_Y \le C\, \|x\|_X .
> $$
>
> Hence $\|A_\alpha x\|_Y \le (C - 1)\|x\|_X$ for all $\alpha$ and $x$, i.e. $\sup_{\alpha \in \Lambda} \|A_\alpha\| \le C - 1 < \infty$. The statement holds with $C_0 = C$.

^pf-42-6

*Uses:* [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]

> [!example] Example §42.2: Pointwise but Not Uniformly Bounded Functionals on $c_{00}$
> *(Not from lecture.)* Completeness of $X$ is needed in Theorem [[§42 Uniform Boundedness and Approximation#^thm-42-6|§42.6]]. Let $c_{00}$ be the finitely supported sequences with $\|x\| = \max_n |x_n|$, and $A_n x = n\, x_n$.
>
> 1. *$c_{00}$ is not complete.* Let $x^{(N)} = (1, \frac12, \ldots, \frac1N, 0, 0, \ldots)$. For $M > N$, $\|x^{(M)} - x^{(N)}\| = \frac{1}{N+1}$, so $\{x^{(N)}\}$ is Cauchy. If $x^{(N)} \to x$ in $c_{00}$, then for each $j$, $|x^{(N)}_j - x_j| \le \|x^{(N)} - x\| \to 0$, so $x_j = \frac1j$ for every $j$, and $x$ is not finitely supported, a contradiction.
> 2. *Each $A_n$ is a bounded linear functional with $\|A_n\| = n$.* $A_n$ is linear, and $|A_n x| = n|x_n| \le n\|x\|$, so $\|A_n\| \le n$; the unit vector $e_n$ gives $A_n e_n = n$, so $\|A_n\| = n$.
> 3. *Pointwise bounded.* Fix $x \in c_{00}$, say $x_j = 0$ for $j > K$. Then $A_n x = 0$ once $n > K$, so $\sup_n |A_n x| = \max_{n \le K} n|x_n| < \infty$.
> 4. *Not uniformly bounded.* $\sup_n \|A_n\| = \sup_n n = \infty$.
>
> So the conclusion of Theorem [[§42 Uniform Boundedness and Approximation#^thm-42-6|§42.6]] fails on the normed space $c_{00}$. The proof breaks at the completeness step: neither $(c_{00}, \|\cdot\|)$ nor $(c_{00}, \|\cdot\|_2)$ is complete (for the second norm, $x^{(N)} = (1, \frac14, \ldots, \frac{1}{N^2}, 0, 0, \ldots)$ is Cauchy, since $\|x^{(M)} - x^{(N)}\|_2 = \frac{1}{(N+1)^2} + \frac{1}{N+1}$ for $M > N$, and has no limit in $c_{00}$, as in (1)), so Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]] does not apply.

^ex-42-2

> [!remark] Remark: Other Proofs of the Principle
> The proof here is the closed-graph route; the more common proof, Lax's (§10.1, Theorem 2), applies Baire directly to the closed sets $\{ x : \sup_\alpha \|A_\alpha x\| \le k \}$: one of them contains a ball, and subadditivity and homogeneity of $x \mapsto \|A_\alpha x\|$ carry the bound to the unit ball. Lax's Theorem 7 of §15.3 assumes even less, only that each $\ell(A_\alpha x)$, $\ell \in Y'$, is bounded, and reduces to the present case by applying the principle twice.

^rem-42-2

## The Banach–Steinhaus Theorem

> [!theorem] Theorem §42.7: Banach–Steinhaus
> Let $X$ be a Banach space and $Y$ a normed linear space. Let $\{A_n\}$ be a sequence of bounded linear maps $X \to Y$, and $A \in \mathcal{L}(X, Y)$. Then $\lim_{n \to \infty} A_n x = Ax$ for all $x \in X$ if and only if
>
> 1. $\sup_{n \in \mathbb{N}} \|A_n\| < \infty$, and
> 2. there is a [[§11 Normed Linear Spaces#^def-11-8|dense subset]] $D$ of $X$ with $\lim_{n \to \infty} A_n x = Ax$ for all $x \in D$.
>
> *Lax: §15.2, Thm 6 (the direction $\Leftarrow$); §15.3, Thm 7 and Cor 7$'$ (the direction $\Rightarrow$)*

^thm-42-7

> [!proof]+ Proof
> **($\Rightarrow$)** By the uniform boundedness principle. For each $x$, the sequence $\{A_n x\}$ converges in $Y$, hence is bounded: $\sup_n \|A_n x\| < \infty$. Theorem [[§42 Uniform Boundedness and Approximation#^thm-42-6|§42.6]] gives (1). (2) holds with $D = X$.
>
> **($\Leftarrow$)** Assume $\sup_n \|A_n\| + \|A\| \le C < \infty$, and that $D$ is a dense subset of $X$ with $A_n y \to Ay$ for every $y \in D$. Let $x \in X$; we want $\|A_n x - Ax\| \to 0$. For every $y \in D$,
>
> $$
> \begin{aligned}\|A_n x - Ax\| &= \|A_n y - Ay + A_n(x - y) - A(x - y)\| \\
> &\le \|A_n y - Ay\| + \bigl( \|A_n\| + \|A\| \bigr) \|x - y\| \\
> &\le \|A_n y - Ay\| + C\, \|x - y\| .\end{aligned}
> $$
>
> Given $\varepsilon > 0$, first choose $y \in D$ with $C\|x - y\| < \varepsilon/2$ (density), then $N$ with $\|A_n y - Ay\| < \varepsilon/2$ for $n > N$. Then $\|A_n x - Ax\| < \varepsilon$ for $n > N$.

^pf-42-7

*Uses:* [[§42 Uniform Boundedness and Approximation#^thm-42-6|§42.6]]

> [!remark] Remark: Which Hypotheses Each Direction Uses
> *(Not from lecture.)* Only ($\Rightarrow$) uses the completeness of $X$, through the uniform boundedness principle; ($\Leftarrow$) is an $\varepsilon/2$ argument valid in any normed spaces. Lax's Theorem 6 (§15.2) is a variant of ($\Leftarrow$) in which no limit $A$ is given (Proposition [[§42 Uniform Boundedness and Approximation#^prop-42-8|§42.8]]); there $Y$ must be complete, since the limit has to be produced.

^rem-42-3

> [!theorem] Proposition §42.8: Banach–Steinhaus Without a Given Limit
> *(Not from lecture.)* Let $X$ be a normed linear space, $Y$ a Banach space, and $\{A_n\}$ a sequence of bounded linear maps $X \to Y$ with $\sup_n \|A_n\| \le C < \infty$. If $\lim_{n \to \infty} A_n y$ exists for every $y$ in a dense subset $D$ of $X$, then $\lim_{n \to \infty} A_n x$ exists for every $x \in X$.
>
> *Lax: §15.2, Thm 6*

^prop-42-8

> [!proof]+ Proof
> Let $x \in X$. Since $Y$ is complete, it suffices to show that $\{A_n x\}$ is Cauchy. For every $y \in D$, by the same $\varepsilon/2$ estimate as in the proof of ($\Leftarrow$) above,
>
> $$
> \begin{aligned}\|A_n x - A_m x\| &\le \|A_n(x - y)\| + \|A_n y - A_m y\| + \|A_m(y - x)\| \\
> &\le 2C\, \|x - y\| + \|A_n y - A_m y\| .\end{aligned}
> $$
>
> Given $\varepsilon > 0$, first choose $y \in D$ with $2C\|x - y\| < \varepsilon/2$ (density), then $N$ with $\|A_n y - A_m y\| < \varepsilon/2$ for $n, m > N$ (the convergent sequence $\{A_n y\}$ is Cauchy). Then $\|A_n x - A_m x\| < \varepsilon$ for $n, m > N$.

^pf-42-8

## The Lax Equivalence Theorem

Consider the equation $Mx = y$, with $M : X \to Y$ one-to-one, onto and bounded. In practice $M$ is replaced by an approximation $M_n : X \to Y$ (a discretization), also one-to-one and onto, and one solves

$$
M_n x_n = y .
$$

*Question:* does $x_n \to x_0$, where $Mx_0 = y$?

> [!theorem] Theorem §42.9: Lax Equivalence Theorem
> Let $X, Y$ be Banach spaces. Assume $M_n \in \mathcal{L}(X, Y)$ for $n \ge 1$ and $M \in \mathcal{L}(X, Y)$, with $M_n : X \to Y$ and $M : X \to Y$ one-to-one and onto. Assume that for every given $x \in X$, $\lim_{n \to \infty} M_n x = Mx$. Then
>
> $$
> \lim_{n \to \infty} M_n^{-1} y = M^{-1} y \quad \text{for all } y \in Y \qquad \iff \qquad \sup_{n} \|M_n^{-1} y\| < \infty \quad \text{for all } y \in Y .
> $$
>
> *Lax: §34.3, Thm 8 (Lax's equivalence theorem, for difference approximations of a semigroup)*

^thm-42-9

> [!proof]+ Proof
> **($\Rightarrow$)** Trivial, because a convergent sequence is bounded.
>
> **($\Leftarrow$)** The open mapping theorem (in the form of Banach's theorem, Theorem [[§39 Solving Mx = y#^thm-39-2|§39.2]]) gives $M_n^{-1} \in \mathcal{L}(Y, X)$ and $M^{-1} \in \mathcal{L}(Y, X)$, and the uniform boundedness principle gives
>
> $$
> \sup_{n \in \mathbb{N}} \|M_n^{-1}\| + \|M^{-1}\| \le C < \infty .
> $$
>
> (Theorem [[§42 Uniform Boundedness and Approximation#^thm-42-6|§42.6]] is applied to the family $\{M_n^{-1}\}$ of bounded linear maps from the Banach space $Y$ to $X$, which is pointwise bounded by assumption.) We want: for every $y \in Y$, $\|M_n^{-1} y - M^{-1} y\| \to 0$. Write
>
> $$
> M_n^{-1} y - M^{-1} y = M_n^{-1}\bigl( y - M_n(M^{-1} y) \bigr) = M_n^{-1}\bigl( M(M^{-1} y) - M_n(M^{-1} y) \bigr) .
> $$
>
> Hence, with $x = M^{-1} y$,
>
> $$
> \|M_n^{-1} y - M^{-1} y\| \le \|M_n^{-1}\|\, \bigl\| M(M^{-1} y) - M_n(M^{-1} y) \bigr\| \le C\, \|M_n x - Mx\| \to 0
> $$
>
> by assumption.

^pf-42-9

*Uses:* [[§39 Solving Mx = y#^thm-39-2|§39.2]], [[§42 Uniform Boundedness and Approximation#^thm-42-6|§42.6]]

> [!remark] Remark: Consistency $+$ Stability $=$ Convergence
> In numerical analysis the three conditions have names. $M_n x \to Mx$ for every $x$ is *consistency*: the discrete operator approximates the true one. $\sup_n \|M_n^{-1}\| < \infty$ is *stability*: errors in the data are amplified by at most a factor independent of $n$, which by the uniform boundedness principle is the same as $\sup_n \|M_n^{-1} y\| < \infty$ for each $y$. $M_n^{-1} y \to M^{-1} y$ is *convergence* of the approximate solutions. The theorem says: for a consistent scheme, stability is equivalent to convergence. The identity $M_n^{-1} - M^{-1} = M_n^{-1}(M - M_n)M^{-1}$ is the heart of the proof. (Lax proved the version for initial value problems in 1956, with Richtmyer. In Lax's book it is Theorem 8 of §34.3: an approximation $u^{(n)} = C_h^n x$ of a semigroup $Z(t)$, consistent with its generator, converges to $Z(t)x$ for all $x$ if and only if it is stable, $|C_h^n| \le \text{const}$ for $nh \le 1$. Necessity is again the uniform boundedness principle, and sufficiency rests on a telescoping identity for $C_h^n - Z(nh)$ of the same kind as the identity above. The version in the lecture is the stationary one, for equations $Mx = y$.)

^rem-42-4
