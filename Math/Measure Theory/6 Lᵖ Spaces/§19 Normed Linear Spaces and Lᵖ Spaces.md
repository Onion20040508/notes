---
type: section
subject: "[[Measure Theory]]"
chapter: 6
section: 19
tags: [measure-theory, math551]
---
← [[§18 Differentiation Theory]] · ↑ [[· 6 Lᵖ Spaces]]

## Normed Linear Spaces

> [!definition] Definition §19.1: Linear Space
> A set $X$ is called a **linear space** (or [[§2 Definition of Vector Space#^ladr-1-20|vector space]]) over $\mathbb{R}$ if for all $v_1, v_2 \in X$ and $c_1, c_2 \in \mathbb{R}$, we have $c_1 v_1 + c_2 v_2 \in X$ (with the usual axioms of vector addition and scalar multiplication).

^def-19-1

> [!remark]- Connections
> - The axioms in full: [[§2 Definition of Vector Space#^ladr-1-20|LADR 1.20]]; the closure condition $c_1v_1 + c_2v_2 \in X$ is the subspace test [[§3 Subspaces#^ladr-1-34|LADR 1.34]].
> - Same definition in 556, over ℝ or ℂ, where subspaces, quotients and complements are developed: [[§1 Linear Spaces#^def-1-1|556 Def. §1.1]].

> [!example] Example §19.1: Linear Spaces in This Course
> $\mathbb{R}^n$, $L^1(E)$ ([[§16 The L¹ Space and Density Theorems#^thm-16-4|Theorem §16.4]]), $BV([a,b])$ ([[§18 Differentiation Theory#^prop-18-4|Proposition §18.4]]), and $AC([a,b])$ ([[§18 Differentiation Theory#^prop-18-11|Proposition §18.11]]) are all linear spaces.

^ex-19-1

> [!definition] Definition §19.2: Norm
> Let $X$ be a linear space. A function $\|\cdot\|: X \to \mathbb{R}$ is called a **norm** if:
> - (i) $\|x\| \geq 0$ for all $x \in X$, and $\|x\| = 0$ if and only if $x = 0$.
> - (ii) $\|x + y\| \leq \|x\| + \|y\|$ for all $x, y \in X$ (triangle inequality).
> - (iii) $\|cx\| = |c|\,\|x\|$ for all $c \in \mathbb{R}$, $x \in X$ (homogeneity).
>
> The pair $(X, \|\cdot\|)$ is called a **normed linear space**.

^def-19-2

> [!remark]- Connections
> - The norm of an inner product space, $\|v\| = \sqrt{\langle v, v\rangle}$ ([[§19 Inner Products and Norms#^ladr-6-7|LADR 6.7]]), satisfies (i), (iii) by [[§19 Inner Products and Norms#^ladr-6-9|LADR 6.9]] and (ii) by the [[Triangle inequality|triangle inequality (LADR 6.17)]].
> - Which norms come from an inner product is decided by the [[§19 Inner Products and Norms#^ladr-6-21|parallelogram equality (LADR 6.21)]]; among the $L^p$ norms only $p = 2$ does.
> - 556 version over ℝ or ℂ, alongside seminorms: [[§8 Normed Linear Spaces#^def-8-1|556 Def. §8.1]], [[§8 Normed Linear Spaces#^def-8-2|556 Def. §8.2]]; that among the $L^p$ norms only $p = 2$ comes from an inner product is [[§17 Cauchy–Schwarz and the Induced Norm#^cor-17-5|556 Cor. §17.5]].

> [!example] Example §19.2: Norms on $\mathbb{R}^n$
> For $\mathbf{x} = (x_1, \ldots, x_n) \in \mathbb{R}^n$: $\|\mathbf{x}\|_2 = \left(\sum_{i=1}^{n} x_i^2\right)^{1/2}$ is the Euclidean norm, and $\|\mathbf{x}\|_1 = \sum_{i=1}^{n} |x_i|$ is the $\ell^1$ norm. Both are norms on $\mathbb{R}^n$.

^ex-19-2

![[m551-19-1.svg]]
*Unit balls $\{\|x\| \leq 1\}$ in $\mathbb{R}^2$: the $\ell^1$ ball is the red diamond and the Euclidean ball the blue disk. The $\ell^4$ ball (dashed) and the square of $\max_i |x_i|$ (gray, the limit $p \to \infty$) show the balls of $\|x\|_p = (\sum_i |x_i|^p)^{1/p}$ growing toward the square as $p$ increases. The shapes differ, but each is convex and symmetric about $0$, as the triangle inequality and homogeneity require.*

> [!remark]- Connections
> - $\|\cdot\|_2$ is the inner-product norm of [[§19 Inner Products and Norms#^ladr-6-8|LADR 6.8(a)]]; its metric is the Euclidean metric of [[§11 Metric Topology#^ex-11-1|590 Ex. §11.1]].
> - Comparing norms on $\mathbb{R}^n$: [[§13 Some Topological Concepts in Metric Spaces#^prop-13-1|451 §13.1]] ($d$ vs. $d_\infty$).

> [!example] Example §19.3: Norms on Function Spaces
> $L^1(E)$: $\|f\|_1 = \int_E |f(x)|\,dx$ ([[§16 The L¹ Space and Density Theorems#^def-16-1|Def. §16.1]]). Then $(L^1(E), \|\cdot\|_1)$ is a normed linear space ([[§16 The L¹ Space and Density Theorems#^thm-16-4|Theorem §16.4]]).
>
> $BV([a,b])$: $\bigvee_a^b(f)$ ([[§18 Differentiation Theory#^def-18-2|Def. §18.2]]) is a norm on $BV([a,b]) / \{\text{constants}\}$ (since $\bigvee_a^b(f) = 0$ iff $f$ is constant, not necessarily zero).

^ex-19-3

> [!remark]- Connections
> - $BV([a,b]) / \{\text{constants}\}$ is a quotient space in the sense of [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]]; homogeneity and the triangle inequality for $\bigvee_a^b$ are [[§18 Differentiation Theory#^prop-18-4|Proposition §18.4]](ii).

> [!theorem] Proposition §19.1: Every Normed Space is a Metric Space
> If $(X, \|\cdot\|)$ is a normed linear space, then $d(x, y) = \|x - y\|$ defines a [[§11 Metric Topology#^def-11-1|metric]] on $X$.

^prop-19-1

> [!proof]+ Proof
> $d(x, y) = \|x - y\| \geq 0$ with equality iff $x = y$ (property (i)). Symmetry: $d(x, y) = \|x - y\| = \|{-(y - x)}\| = |{-1}|\,\|y - x\| = d(y, x)$. Triangle inequality: $d(x, y) = \|x - y\| = \|(x - z) + (z - y)\| \leq \|x - z\| + \|z - y\| = d(x, z) + d(z, y)$.

^pf-19-1

*Uses:* [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-2|Def. §19.2]], [[§11 Metric Topology#^def-11-1|590 Def. §11.1]]

> [!remark]- Connections
> - Metric axioms: [[§11 Metric Topology#^def-11-1|590 Def. §11.1]], [[§13 Some Topological Concepts in Metric Spaces#^def-13-1|451 Def. §13.1]]. The same observation for inner product spaces: [[Triangle inequality|LADR 6.17]].
> - The $L^1$ case was [[§16 The L¹ Space and Density Theorems#^def-16-2|Def. §16.2]].
> - Same statement and proof in 556: [[§8 Normed Linear Spaces#^prop-8-2|556 Prop. §8.2]].

## Completeness and Banach Spaces

> [!definition] Definition §19.3: Convergence and Cauchy Sequences
> Let $(X, \|\cdot\|)$ be a normed linear space. A sequence $\{x_k\}_{k=1}^{\infty} \subseteq X$ **converges** to $a \in X$ if $\lim_{k \to \infty} \|x_k - a\| = 0$. We write $\lim_{k \to \infty} x_k = a$ in $(X, \|\cdot\|)$.
>
> The sequence is a **Cauchy sequence** if for every $\varepsilon > 0$, there exists $N > 0$ such that $\|x_k - x_m\| < \varepsilon$ for all $k, m > N$.

^def-19-3

> [!remark]- Connections
> - These are the metric-space notions of [[§13 Some Topological Concepts in Metric Spaces#^def-13-2|451 Def. §13.2]] for $d(x,y) = \|x - y\|$; on $\mathbb{R}$: [[§10 Monotone Sequences and Cauchy Sequences#^def-10-4|451 Def. §10.4]].
> - 556 versions: [[§8 Normed Linear Spaces#^def-8-4|556 Def. §8.4]] (convergence) and [[§8 Normed Linear Spaces#^def-8-5|556 Def. §8.5]] (Cauchy sequence).

> [!definition] Definition §19.4: Banach Space
> A normed linear space $(X, \|\cdot\|)$ is **complete** if every Cauchy sequence in $X$ converges to a limit in $X$. A complete normed linear space is called a **Banach space**.

^def-19-4

> [!remark]- Connections
> - A Banach space is a normed space that is a [[§13 Some Topological Concepts in Metric Spaces#^def-13-3|complete metric space (451 Def. §13.3)]] under $d(x,y) = \|x - y\|$ ([[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-1|Proposition §19.1]]).
> - 556 version: [[§9 Completeness#^def-9-2|556 Def. §9.2]]; every normed space has a Banach completion ([[§9 Completeness#^thm-9-4|556 Thm. §9.4]]), and $L^p[a,b]$ is the completion of $C[a,b]$ in the $p$-norm ([[§14 The Function Spaces Lᵖ(Ω)#^prop-14-8|556 Prop. §14.8]]).

> [!example] Example §19.4: Banach Spaces
> $(\mathbb{R}^n, \|\cdot\|_1)$ and $(\mathbb{R}^n, \|\cdot\|_2)$ are Banach spaces (completeness of $\mathbb{R}^n$ in any norm; [[§13 Some Topological Concepts in Metric Spaces#^thm-13-2|451 §13.2]]). The [[Riesz–Fischer Theorem|Riesz–Fischer theorem]] states that $(L^1(E), \|\cdot\|_1)$ is a Banach space.

^ex-19-4

## $L^p$ Spaces

> [!definition] Definition §19.5: $L^p$ Space
> Let $E \in \mathcal{M}(\mathbb{R}^n)$ and $1 \leq p < \infty$. A [[§12 Measurable Functions#^def-12-2|measurable function]] $f$ on $E$ belongs to $L^p(E)$ if:
>
> $$
> \int_E |f(x)|^p\,dx < \infty.
> $$
>
> (Note: $|f(x)|^p$ is still measurable since $t \mapsto |t|^p$ is continuous.) We define the $L^p$ **norm** of $f$ by:
>
> $$
> \|f\|_{L^p(E)} = \|f\|_p = \left(\int_E |f(x)|^p\,dx\right)^{1/p}.
> $$

^def-19-5

> [!remark] Remark
> When $p = 1$, this recovers $L^1(E)$ with $\|f\|_1 = \int_E |f|\,dx$ ([[§16 The L¹ Space and Density Theorems#^def-16-1|Def. §16.1]]). The $L^p$ spaces for $p > 1$ are important in functional analysis and PDE theory. The key results (proved later in this section) are:
>
> Hölder's inequality ([[Hölder's Inequality|Theorem §19.5]]): $\|fg\|_1 \leq \|f\|_p \|g\|_q$ where $1/p + 1/q = 1$.
>
> Minkowski's inequality ([[Minkowski's Inequality|Theorem §19.9]]): $\|f + g\|_p \leq \|f\|_p + \|g\|_p$ (the triangle inequality for $\|\cdot\|_p$).
>
> Riesz–Fischer theorem ([[Riesz–Fischer Theorem|Theorem §19.18]]): $(L^p(E), \|\cdot\|_p)$ is a Banach space for all $1 \leq p < \infty$.
>
> The case $p = 2$ is especially important: $L^2(E)$ is a Hilbert space with [[§19 Inner Products and Norms#^ladr-6-2|inner product]] $\langle f, g \rangle = \int_E f(x)\,g(x)\,dx$, and $\|f\|_2 = \langle f, f \rangle^{1/2}$ ([[§19 Inner Products and Norms#^ladr-6-7|LADR 6.7]]).

^rem-19-1

> [!remark]- Connections
> - The Riemann-integral prototype of this inner product and norm: [[§19 Inner Products and Norms#^ladr-6-3|LADR 6.3(c)]], [[§19 Inner Products and Norms#^ladr-6-8|LADR 6.8(b)]].
> - 556's working definition on open sets of ℝⁿ: [[§14 The Function Spaces Lᵖ(Ω)#^def-14-1|556 Def. §14.1]]; with counting measure on ℕ ([[§11 Borel Sets and Measure Spaces#^ex-11-2|Ex. §11.2]]) this definition gives the sequence spaces of [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^def-13-1|556 Def. §13.1]].

> [!example] Example §19.5: $L^p$ Membership Depends on $p$
> Let $E = (0, 1)$ and $g(x) = 1/\sqrt{x}$. Then $g \in L^p((0,1))$ iff $\int_0^1 x^{-p/2}\,dx < \infty$ iff $p/2 < 1$ iff $p < 2$. So $g \in L^1$ but $g \notin L^2$.
>
> Let $E = (0, 1)$ and $f(x) = \ln(1/x)$. Then $f \in L^\infty((0,1))$ ([[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-6|Def. §19.6]])? No: $\ln(1/x) \to \infty$ as $x \to 0^+$. But $\int_0^1 |\ln(1/x)|^p\,dx < \infty$ for all $1 \leq p < \infty$ (since $|\ln(1/x)| \leq c\,|x|^{-\alpha}$ for any $\alpha > 0$).

^ex-19-5

![[m551-19-2.svg]]
*$L^p$ membership depends on $p$. On $(0,1)$ the function $g = 1/\sqrt{x}$ (blue) has finite area $\int_0^1 g = 2$, but squaring makes the singularity worse, and $g^2 = 1/x$ (red) has infinite area. On a set of finite measure, large $p$ punishes tall spikes, which is why $L^{p_2} \subseteq L^{p_1}$ for $p_1 < p_2$ there ([[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-6|Corollary §19.6]]).*

## $L^\infty$ and the Essential Supremum

> [!definition] Definition §19.6: $L^\infty$ Space and Essential Supremum
> Let $E \in \mathcal{M}(\mathbb{R}^n)$ and $f$ a measurable function on $E$. We say $f \in L^\infty(E)$ if there exists a constant $M > 0$ such that $|f(x)| \leq M$ for [[§12 Measurable Functions#^def-12-5|a.e.]] $x \in E$. Such $f$ is called **essentially bounded**.
>
> The **essential supremum** of $|f|$ is:
>
> $$
> \|f\|_\infty = \|f\|_{L^\infty(E)} = \operatorname*{ess\,sup}_{x \in E} |f(x)| = \inf\{M \geq 0 : m(\{x \in E : |f(x)| > M\}) = 0\}.
> $$

^def-19-6

> [!example] Example §19.6
> $f(x) = 1$ for $x \in \mathbb{R} \setminus \mathbb{Q}$, $f(x) = \infty$ for $x \in \mathbb{Q}$. Then $f \in L^\infty(\mathbb{R})$ with $\|f\|_\infty = 1$, since $\{|f| > 1\} = \mathbb{Q}$ has measure zero ([[§9 Lebesgue Outer Measure#^ex-9-2|Example §9.2]]).

^ex-19-6

> [!theorem] Proposition §19.2: The Essential Supremum is Achieved A.E.
> If $f$ is an a.e. finite measurable function on $E$, then $m(\{x \in E : |f(x)| > \|f\|_\infty\}) = 0$.

^prop-19-2

> [!proof]+ Proof
> Let $M_0 = \|f\|_\infty = \inf\{M : m(\{|f| > M\}) = 0\}$. There exists a sequence $M_k \searrow M_0$ with $m(\{|f| > M_k\}) = 0$ for each $k$. Then:
>
> $$
> \{x \in E : |f(x)| > M_0\} = \bigcup_{k=1}^{\infty} \{x \in E : |f(x)| > M_k\},
> $$
>
> so $m(\{|f| > M_0\}) \leq \sum_{k=1}^{\infty} m(\{|f| > M_k\}) = 0$ ([[Properties of Lebesgue Outer Measure|countable subadditivity]]).

^pf-19-2

*Uses:* [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-6|Def. §19.6]], [[Properties of Lebesgue Outer Measure|§9.1]]

## The Limit Theorem: $\lim_{p \to \infty} \|f\|_p = \|f\|_\infty$

> [!theorem] Theorem §19.3
> Let $E$ be measurable with $m(E) < \infty$, and $f$ a measurable function on $E$. Then:
>
> $$
> \lim_{p \to \infty} \|f\|_p = \|f\|_\infty.
> $$

^thm-19-3

> [!proof]+ Proof
> *Step 1: $\limsup_{p \to \infty} \|f\|_p \leq \|f\|_\infty$.* If $\|f\|_\infty = \infty$, this is trivial. If $\|f\|_\infty = M < \infty$, then $|f(x)| \leq M$ a.e. on $E$ ([[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|Proposition §19.2]]), so:
>
> $$
> \int_E |f(x)|^p\,dx \leq M^p\,m(E).
> $$
>
> Therefore $\|f\|_p \leq M\,m(E)^{1/p}$. Since $m(E) < \infty$, $\lim_{p \to \infty} m(E)^{1/p} = 1$, giving $\limsup_{p \to \infty} \|f\|_p \leq M = \|f\|_\infty$.
>
> *Step 2: $\liminf_{p \to \infty} \|f\|_p \geq \|f\|_\infty$.* For any $M_0 < \|f\|_\infty$ (whether $\|f\|_\infty$ is finite or $\infty$), $M_0$ is not an essential bound, so $A = \{x \in E : |f(x)| \geq M_0\}$ has $m(A) > 0$. Then:
>
> $$
> \int_E |f(x)|^p\,dx \geq \int_A M_0^p\,dx = M_0^p\,m(A).
> $$
>
> So $\|f\|_p \geq M_0\,m(A)^{1/p}$. Since $0 < m(A) \leq m(E) < \infty$, $\lim_{p \to \infty} m(A)^{1/p} = 1$, giving $\liminf_{p \to \infty} \|f\|_p \geq M_0$. Since this holds for all $M_0 < \|f\|_\infty$, $\liminf_{p \to \infty} \|f\|_p \geq \|f\|_\infty$.
>
> *Conclusion.* Combining: $\|f\|_\infty \leq \liminf \|f\|_p \leq \limsup \|f\|_p \leq \|f\|_\infty$, so $\lim_{p \to \infty} \|f\|_p = \|f\|_\infty$ ([[§10 Monotone Sequences and Cauchy Sequences#^thm-10-6|451 §10.6]]).

^pf-19-3

*Uses:* [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-6|Def. §19.6]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|§19.2]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-9|§14.9]], [[§14 The Lebesgue Integral for Simple Functions#^cor-14-7|§14.7]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-6|451 §10.6]]

## Hölder's Inequality

> [!definition] Definition §19.7: Conjugate Exponents
> For $1 \leq p \leq \infty$, the **conjugate exponent** $p'$ is defined by:
>
> $$
> \frac{1}{p} + \frac{1}{p'} = 1, \qquad \text{i.e.,} \quad p' = \frac{p}{p - 1}.
> $$
>
> Convention: $p = 1 \Leftrightarrow p' = \infty$, and $p = \infty \Leftrightarrow p' = 1$.

^def-19-7

> [!remark]- Connections
> - Same definition in 556: [[§12 Hölder's Inequality for Sequences#^def-12-2|556 Def. §12.2]].

> [!theorem] Lemma §19.4: Young's Inequality
> For $a, b > 0$ and $0 < \theta < 1$: $a^\theta\,b^{1-\theta} \leq \theta\,a + (1 - \theta)\,b$.

^lem-19-4

> [!proof]+ Proof
> It suffices to show $\ln(a^\theta\,b^{1-\theta}) \leq \ln(\theta\,a + (1 - \theta)\,b)$. The left side is $\theta\ln a + (1-\theta)\ln b$. Since $\ln$ is concave ($\ln(\theta\,a + (1 - \theta)\,b) \geq \theta\,\ln a + (1 - \theta)\,\ln b$ by Jensen's inequality), the result follows.

^pf-19-4

![[m551-19-3.svg]]
*Young's inequality is the concavity of $\ln$ (shown with $\theta = 0.35$). The chord from $(a, \ln a)$ to $(b, \ln b)$ (red) lies below the graph, so at $\theta a + (1-\theta)b$ the chord height $\theta\ln a + (1-\theta)\ln b = \ln(a^\theta b^{1-\theta})$ is below $\ln(\theta a + (1-\theta)b)$. Carrying the chord height across to the graph (dashed) locates $a^\theta b^{1-\theta}$ on the axis, to the left of $\theta a + (1-\theta)b$ because $\ln$ is increasing.*

> [!remark]- Connections
> - Same inequality in 556, proved by the same concavity argument: [[§11 Means and Young's Inequality#^lem-11-3|556 Lemma §11.3]].

> [!theorem] Theorem §19.5: Hölder's Inequality
> Let $f, g$ be measurable functions on $E$. Let $1 \leq p \leq \infty$ and $p'$ its [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-7|conjugate]]. Then:
>
> $$
> \int_E |f(x)\,g(x)|\,dx \leq \|f\|_{L^p(E)}\,\|g\|_{L^{p'}(E)}.
> $$
>
> The case $p = p' = 2$ is the **Cauchy–Schwarz inequality**: $\int_E |fg|\,dx \leq \|f\|_2\,\|g\|_2$.

^thm-19-5

> [!proof]+ Proof
> **Case 1: $\|g\|_{p'} = 0$.** Then $g = 0$ a.e. ([[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|Proposition §14.11]]), so $fg = 0$ a.e., and both sides are $0$.
>
> **Case 2: $\|g\|_{p'} \neq 0$ and $\|f\|_p = \infty$.** The right side is $\infty$, so the inequality holds trivially. (We use the convention $0 \cdot \infty = 0$. By symmetry, if $\|f\|_p = 0$ then $f = 0$ a.e. and both sides are $0$, and if $\|f\|_p \neq 0$ and $\|g\|_{p'} = \infty$ the right side is $\infty$. So from now on both norms lie in $(0, \infty)$.)
>
> **Case 3: $p = 1$, $p' = \infty$.** Since $g \in L^\infty(E)$, $|g(x)| \leq \|g\|_\infty$ a.e. ([[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|Proposition §19.2]]). So:
>
> $$
> \int_E |f\,g|\,dx \leq \int_E |f|\,\|g\|_\infty\,dx = \|f\|_1\,\|g\|_\infty.
> $$
>
> The case $p = \infty$, $p' = 1$ is the same with the roles of $f$ and $g$ exchanged.
>
> **Case 4: $1 < p < \infty$, $1 < p' < \infty$.** Assume $\|f\|_p, \|g\|_{p'} \in (0, \infty)$. Apply [[§19 Normed Linear Spaces and Lᵖ Spaces#^lem-19-4|Young's inequality]] with $\theta = 1/p$, $1 - \theta = 1/p'$, $a = |f(x)|^p / (\|f\|_p)^p$, $b = |g(x)|^{p'} / (\|g\|_{p'})^{p'}$:
>
> $$
> \frac{|f(x)|}{\|f\|_p} \cdot \frac{|g(x)|}{\|g\|_{p'}} = a^{1/p}\,b^{1/p'} \leq \frac{1}{p}\,a + \frac{1}{p'}\,b = \frac{1}{p}\,\frac{|f(x)|^p}{(\|f\|_p)^p} + \frac{1}{p'}\,\frac{|g(x)|^{p'}}{(\|g\|_{p'})^{p'}}.
> $$
>
> Integrating over $E$:
>
> $$
> \frac{1}{\|f\|_p\,\|g\|_{p'}} \int_E |f\,g|\,dx \leq \frac{1}{p}\,\frac{(\|f\|_p)^p}{(\|f\|_p)^p} + \frac{1}{p'}\,\frac{(\|g\|_{p'})^{p'}}{(\|g\|_{p'})^{p'}} = \frac{1}{p} + \frac{1}{p'} = 1.
> $$
>
> Multiplying both sides by $\|f\|_p\,\|g\|_{p'}$:
>
> $$
> \int_E |f\,g|\,dx \leq \|f\|_p\,\|g\|_{p'}.
> $$

^pf-19-5

*Uses:* [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-7|Def. §19.7]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|§14.11]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-9|§14.9]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|§19.2]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^lem-19-4|§19.4]], [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|§14.8]]

> [!remark]- Connections
> - $p = 2$ is the [[Cauchy–Schwarz inequality|Cauchy–Schwarz inequality (LADR 6.14)]] for the $L^2$ inner product of [[§19 Normed Linear Spaces and Lᵖ Spaces#^rem-19-1|the remark above]]; its Riemann-integral form for continuous functions is [[§19 Inner Products and Norms#^ladr-6-16|LADR 6.16(b)]].
> - Used to prove [[Minkowski's Inequality|Minkowski's inequality]], the $L^p$ inclusions ([[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-6|Corollary §19.6]]) and [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-7|interpolation]].
> - Sequence version (counting measure), with the same proof: [[§12 Hölder's Inequality for Sequences#^thm-12-1|556 Thm. §12.1]]; for $p = 2$ it is the Cauchy–Schwarz inequality of every inner product space, [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|556 Thm. §17.1]].

> [!theorem] Corollary §19.6: $L^p$ Inclusion for Finite Measure Spaces
> Assume $m(E) < \infty$. Then for $1 \leq p_1 < p_2 \leq \infty$, $L^{p_2}(E) \subseteq L^{p_1}(E)$, and:
>
> $$
> \|f\|_{p_1} \leq \|f\|_{p_2} \cdot m(E)^{1/p_1 - 1/p_2}.
> $$
>
> (With the convention $1/\infty = 0$.)

^cor-19-6

> [!proof]+ Proof
> **Case 1: $p_2 = \infty$.** $f \in L^\infty(E)$ means $|f(x)| \leq \|f\|_\infty$ a.e. on $E$ ([[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|Proposition §19.2]]). Then:
>
> $$
> \int_E |f|^{p_1}\,dx \leq \int_E (\|f\|_\infty)^{p_1}\,dx = (\|f\|_\infty)^{p_1}\,m(E),
> $$
>
> so $\|f\|_{p_1} \leq \|f\|_\infty \cdot m(E)^{1/p_1}$.
>
> **Case 2: $p_1 = 1$, $p_2 = p < \infty$.** Apply [[Hölder's Inequality|Hölder]] with exponents $p$ and $p'$:
>
> $$
> \int_E |f|\,dx = \int_E |f| \cdot 1\,dx \leq \|f\|_p\,\|1\|_{p'} = \|f\|_p \cdot m(E)^{1/p'}.
> $$
>
> Since $1/p' = 1 - 1/p = 1/1 - 1/p$, this gives $\|f\|_1 \leq \|f\|_p \cdot m(E)^{1 - 1/p}$.
>
> **Case 3: $1 \leq p_1 < p_2 < \infty$.** Take $g(x) = |f(x)|^{p_1}$ and apply [[Hölder's Inequality|Hölder]] with conjugate pair $p_2/p_1 > 1$ and $(p_2/p_1)' = p_2/(p_2 - p_1)$:
>
> $$
> \int_E |f|^{p_1}\,dx = \int_E |f|^{p_1} \cdot 1\,dx \leq \left(\int_E |f|^{p_2}\,dx\right)^{p_1/p_2} \cdot m(E)^{1 - p_1/p_2} = (\|f\|_{p_2})^{p_1} \cdot m(E)^{1 - p_1/p_2}.
> $$
>
> Taking $p_1$-th roots: $\|f\|_{p_1} \leq \|f\|_{p_2} \cdot m(E)^{1/p_1 - 1/p_2}$.

^pf-19-6

*Uses:* [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|§19.2]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-7|Def. §19.7]], [[Hölder's Inequality|§19.5]]

> [!remark] Remark
> The finite measure hypothesis is essential: on $\mathbb{R}$, $f(x) = 1/\sqrt{|x|}$ for $|x| \leq 1$ and $0$ otherwise is in $L^1$ but not $L^2$. On infinite measure spaces the inclusion can reverse: $f(x) = 1/(1 + |x|) \in L^2(\mathbb{R})$ but $\notin L^1(\mathbb{R})$.

^rem-19-2

> [!remark]- Connections
> - For sequences the inclusion runs the other way, $\ell^p \subset \ell^q$ for $p < q$: [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^prop-13-4|556 Prop. §13.4]].

> [!theorem] Proposition §19.7: Interpolation of $L^p$ Norms
> Let $1 \leq r < s \leq \infty$ and $f \in L^r(E) \cap L^s(E)$. Then $f \in L^t(E)$ for all $r < t < s$, with:
>
> $$
> \|f\|_t \leq \|f\|_r^{\theta}\,\|f\|_s^{1-\theta}, \qquad \text{where } \theta \in (0, 1) \text{ satisfies } \frac{1}{t} = \frac{\theta}{r} + \frac{1-\theta}{s}.
> $$

^prop-19-7

> [!proof]+ Proof
> Write $|f(x)|^t = |f(x)|^{\theta t} \cdot |f(x)|^{(1-\theta)t}$. Apply [[Hölder's Inequality|Hölder]] with exponents $p = r/(\theta t)$ and $p' = s/((1-\theta)t)$. Note $1/p + 1/p' = \theta t/r + (1-\theta)t/s = t(1/t) = 1$, confirming these are conjugate. Then:
>
> $$
> \int_E |f|^t\,dx \leq \left(\int_E |f|^r\,dx\right)^{\theta t/r} \left(\int_E |f|^s\,dx\right)^{(1-\theta)t/s} = (\|f\|_r)^{\theta t}\,(\|f\|_s)^{(1-\theta)t}.
> $$
>
> Taking $t$-th roots: $\|f\|_t \leq \|f\|_r^{\theta}\,\|f\|_s^{1-\theta}$.
>
> This uses $\int_E |f|^s\,dx$, so it assumes $s < \infty$. If $s = \infty$, then $\theta = r/t$ and $|f|^t = |f|^r\,|f|^{t-r} \leq |f|^r\,\|f\|_\infty^{t-r}$ a.e. ([[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|Proposition §19.2]]), so $\|f\|_t^t \leq \|f\|_r^r\,\|f\|_\infty^{t-r}$; taking $t$-th roots gives $\|f\|_t \leq \|f\|_r^{\theta}\,\|f\|_\infty^{1-\theta}$.

^pf-19-7

*Uses:* [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-7|Def. §19.7]], [[Hölder's Inequality|§19.5]]

## $L^p$ is a Normed Linear Space

> [!theorem] Proposition §19.8: $L^p$ is a Linear Space
> Let $1 \leq p \leq \infty$. Then $L^p(E)$ is a [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-1|linear space]]: if $f, g \in L^p(E)$ and $c \in \mathbb{R}$, then $cf \in L^p(E)$ and $f + g \in L^p(E)$.

^prop-19-8

> [!proof]+ Proof
> **Scalar multiplication.** For $p = \infty$: $|cf(x)| = |c||f(x)| \leq |c|\|f\|_\infty$ a.e., so $cf \in L^\infty$ with $\|cf\|_\infty \leq |c|\|f\|_\infty$. For $1 \leq p < \infty$: $\int |cf|^p = |c|^p \int |f|^p < \infty$, so $cf \in L^p$.
>
> **Addition.** For $p = \infty$: $|f(x) + g(x)| \leq |f(x)| + |g(x)| \leq \|f\|_\infty + \|g\|_\infty$ a.e., so $f + g \in L^\infty$. For $1 \leq p < \infty$: since $|f + g|^p \leq 2^p(|f|^p + |g|^p)$ (by convexity, or $(a + b)^p \leq 2^{p-1}(a^p + b^p)$ for $a, b \geq 0$):
>
> $$
> \int_E |f + g|^p \leq 2^p \int_E |f|^p + 2^p \int_E |g|^p < \infty.
> $$

^pf-19-8

*Uses:* [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|§19.2]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|§14.8]]

> [!theorem] Theorem §19.9: Minkowski's Inequality
> Let $1 \leq p \leq \infty$, $E \in \mathcal{M}(\mathbb{R}^n)$. For all $f, g$ a.e. finite measurable on $E$:
>
> $$
> \|f + g\|_p \leq \|f\|_p + \|g\|_p.
> $$

^thm-19-9

> [!proof]+ Proof
> **Case 1: $p = 1$.** $\int_E |f + g| \leq \int_E (|f| + |g|) = \int_E |f| + \int_E |g|$. $\checkmark$
>
> **Case 2: $p = \infty$.** $|f(x) + g(x)| \leq |f(x)| + |g(x)| \leq \|f\|_\infty + \|g\|_\infty$ a.e., so $\|f + g\|_\infty \leq \|f\|_\infty + \|g\|_\infty$. $\checkmark$
>
> **Case 3: $1 < p < \infty$.** Write $1/p' = 1 - 1/p = (p-1)/p$. Then:
>
> $$
> \int_E |f + g|^p = \int_E |f + g|^{p-1} \cdot |f + g| \leq \int_E |f + g|^{p-1}|f|\,dx + \int_E |f + g|^{p-1}|g|\,dx.
> $$
>
> Apply [[Hölder's Inequality|Hölder]] to each term with exponents $p$ and $p'$. For the first:
>
> $$
> \int_E |f + g|^{p-1}|f|\,dx \leq \left(\int_E |f + g|^{(p-1)p'}\,dx\right)^{1/p'} \|f\|_p = \left(\int_E |f + g|^p\,dx\right)^{1/p'} \|f\|_p,
> $$
>
> since $(p-1)p' = (p-1) \cdot p/(p-1) = p$. Similarly for the second term. Therefore:
>
> $$
> \int_E |f + g|^p \leq \left(\int_E |f + g|^p\right)^{1/p'} (\|f\|_p + \|g\|_p).
> $$
>
> Dividing both sides by $(\int_E |f + g|^p)^{1/p'}$ (assuming this is finite and nonzero):
>
> $$
> \left(\int_E |f + g|^p\right)^{1 - 1/p'} = \left(\int_E |f + g|^p\right)^{1/p} = \|f + g\|_p \leq \|f\|_p + \|g\|_p.
> $$

^pf-19-9

*Uses:* [[§15 The General Lebesgue Integral#^prop-15-3|§15.3]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|§19.2]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-7|Def. §19.7]], [[Hölder's Inequality|§19.5]], [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|§14.8]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]]

> [!remark]- Connections
> - For $p = 2$ the norm comes from the $L^2$ inner product, and Minkowski is the inner-product [[Triangle inequality|triangle inequality (LADR 6.17)]]; the case $p = 1$ is [[§15 The General Lebesgue Integral#^prop-15-3|Proposition §15.3]].
> - Sequence version, proved by the same split-and-Hölder computation: [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^thm-13-1|556 Thm. §13.1]].

> [!theorem] Theorem §19.10: $L^p$ is a Normed Linear Space
> Let $1 \leq p \leq \infty$. Then $(L^p(E), \|\cdot\|_p)$ is a [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-2|normed linear space]].

^thm-19-10

> [!proof]+ Proof
> We verify the three norm axioms:
> - (i) *Positive definiteness:* $\|f\|_p \geq 0$ is clear. $\|f\|_p = 0 \implies f = 0$ a.e. on $E$ (for $p < \infty$: $\int |f|^p = 0$ with $|f|^p \geq 0$ implies $|f|^p = 0$ a.e. ([[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|Proposition §14.11]]); for $p = \infty$: $\operatorname{ess\,sup}|f| = 0$ means $|f| \leq 0$ a.e.). This is why we work with $L^p$ (equivalence classes mod a.e. equality) rather than $\mathcal{L}^p$.
> - (ii) *Homogeneity:* $\|cf\|_p = |c|\,\|f\|_p$ (from the [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-8|scalar multiplication calculation above]]).
> - (iii) *Triangle inequality:* $\|f + g\|_p \leq \|f\|_p + \|g\|_p$ ([[Minkowski's Inequality|Minkowski's inequality]]).

^pf-19-10

*Uses:* [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-2|Def. §19.2]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|§14.11]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|§19.2]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-8|§19.8]], [[Minkowski's Inequality|§19.9]]

> [!remark]- Connections
> - The case $p = 1$: [[§16 The L¹ Space and Density Theorems#^thm-16-4|Theorem §16.4]].
> - Passing to equivalence classes mod a.e. equality is a quotient by the subspace of null functions, as in [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]].
> - Sequence analogue: [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^prop-13-3|556 Prop. §13.3]] ($\ell^p$ is a normed linear space).

> [!theorem] Corollary §19.11: Minkowski for Finite Sums
> Let $\{f_k\}_{k=1}^m \subseteq L^p(E)$. Then $\left\|\sum_{k=1}^{m} f_k\right\|_p \leq \sum_{k=1}^{m} \|f_k\|_p$.

^cor-19-11

*Uses:* [[Minkowski's Inequality|§19.9]]

This follows by induction on $m$ from the two-function case ([[Minkowski's Inequality|Theorem §19.9]]).

> [!theorem] Corollary §19.12: Minkowski for Nonnegative Series
> Let $\{f_k\}_{k=1}^{\infty}$ be a sequence of nonnegative measurable functions on $E$. Then:
>
> $$
> \left\|\sum_{k=1}^{\infty} f_k\right\|_p \leq \sum_{k=1}^{\infty} \|f_k\|_p.
> $$

^cor-19-12

> [!proof]+ Proof
> For $1 \leq p < \infty$: let $S_m(x) = \sum_{k=1}^m f_k(x)$. Since $f_k \geq 0$, $\{|S_m|^p\}$ is an increasing sequence of nonneg measurable functions with $|S_m|^p \nearrow |\sum f_k|^p$. By [[Monotone Convergence Theorem (Lebesgue)|MCT]]:
>
> $$
> \int_E \left|\sum_{k=1}^{\infty} f_k\right|^p dx = \lim_{m \to \infty} \int_E |S_m|^p\,dx \leq \lim_{m \to \infty} \left(\sum_{k=1}^{m} \|f_k\|_p\right)^p = \left(\sum_{k=1}^{\infty} \|f_k\|_p\right)^p,
> $$
>
> where the inequality uses the [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-11|finite sum corollary]]. Taking $p$-th roots gives the result.
>
> For $p = \infty$: $|\sum f_k(x)| \leq \sum |f_k(x)| \leq \sum \|f_k\|_\infty$ a.e. (each inequality holding a.e.), so $\|\sum f_k\|_\infty \leq \sum \|f_k\|_\infty$.

^pf-19-12

*Uses:* [[Monotone Convergence Theorem (Lebesgue)|§14.4]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-11|§19.11]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|§19.2]]

> [!theorem] Corollary §19.13: Minkowski for General Measurable Series
> Let $\{f_k\}_{k=1}^{\infty}$ be a sequence of measurable functions on $E$, and assume $\sum_{k=1}^{\infty} f_k(x)$ converges for a.e. $x \in E$. Then:
>
> $$
> \left\|\sum_{k=1}^{\infty} f_k\right\|_p \leq \sum_{k=1}^{\infty} \|f_k\|_p.
> $$

^cor-19-13

> [!proof]+ Proof
> We have $|\sum_{k=1}^{\infty} f_k(x)| \leq \sum_{k=1}^{\infty} |f_k(x)|$ for a.e. $x \in E$. By the [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-12|nonnegative series corollary]] applied to $|f_k|$: $\|\sum |f_k|\|_p \leq \sum \|f_k\|_p$. Therefore $\|\sum f_k\|_p \leq \|\sum |f_k|\|_p \leq \sum \|f_k\|_p$.

^pf-19-13

*Uses:* [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-12|§19.12]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-9|§14.9]]

> [!theorem] Corollary §19.14: $L^p$ Absolute Series Test
> Let $\{f_k\}_{k=1}^{\infty} \subseteq L^p(E)$ with $\sum_{k=1}^{\infty} \|f_k\|_p < \infty$. Then:
> - (i) $\sum_{k=1}^{\infty} f_k(x)$ converges absolutely for a.e. $x \in E$.
> - (ii) $\sum_{k=1}^{\infty} f_k \in L^p(E)$ with $\|\sum_{k=1}^{\infty} f_k\|_p \leq \sum_{k=1}^{\infty} \|f_k\|_p$.

^cor-19-14

> [!proof]+ Proof
> **A.e. convergence:** For $1 \leq p < \infty$: by the [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-12|nonnegative series corollary]], $\|\sum |f_k|\|_p \leq \sum \|f_k\|_p < \infty$, so $\sum |f_k(x)|$ is a.e. finite ([[§14 The Lebesgue Integral for Simple Functions#^prop-14-10|integrability implies a.e. finiteness]]), hence $\sum f_k(x)$ converges absolutely a.e.
>
> For $p = \infty$: $\sum |f_k(x)| \leq \sum \|f_k\|_\infty < \infty$ a.e., so $\sum f_k$ converges absolutely a.e.
>
> **Norm bound:** Follows from the [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-13|general measurable series corollary]].

^pf-19-14

*Uses:* [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-12|§19.12]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-10|§14.10]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|§19.2]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-13|§19.13]]

> [!remark]- Connections
> - The case $p = 1$: [[§15 The General Lebesgue Integral#^cor-15-9|Corollary §15.9]].
> - The $L^p$ analogue of [[§14 Series#^prop-14-6|absolute convergence implies convergence (451 §14.6)]]; in a normed space this property is equivalent to completeness, which is how it drives [[Riesz–Fischer Theorem|Riesz–Fischer]].

## $L^p$ Convergence and Completeness

> [!definition] Definition §19.8: $L^p$ Convergence and Completeness
> Let $1 \leq p \leq \infty$ and $\{f_k\}_{k \in \mathbb{N}} \subseteq L^p(E)$.
> - (i) We say $\{f_k\}$ **converges to $f$ in $L^p$** if $f \in L^p(E)$ and $\lim_{k \to \infty} \|f_k - f\|_p = 0$. We write $\lim_{k \to \infty} f_k = f$ in $L^p(E)$.
> - (ii) We say $\{f_k\}$ is **Cauchy in $L^p$** if for every $\varepsilon > 0$, there exists $N \in \mathbb{N}$ such that $\|f_k - f_m\|_p < \varepsilon$ for all $k, m \geq N$.
> - (iii) We say $L^p(E)$ is **complete** if every Cauchy sequence in $L^p(E)$ converges to some $f \in L^p(E)$.

^def-19-8

> [!remark]- Connections
> - The special case of [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-3|Def. §19.3]]–[[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-4|Def. §19.4]] for $\|\cdot\|_p$; for $p = 1$ it is [[§16 The L¹ Space and Density Theorems#^def-16-2|Def. §16.2]].

> [!remark] Remark
> The metric $d(f, g) = \|f - g\|_p$ makes $(L^p(E), d)$ a metric space ([[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-1|Proposition §19.1]]; this follows from the norm axioms verified [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-10|above]]). Completeness of $L^p$ in this metric is the content of the [[Riesz–Fischer Theorem|Riesz–Fischer theorem]] below.

^rem-19-3

> [!theorem] Proposition §19.15: Basic Properties of $L^p$ Convergence
> - (i) *Uniqueness:* If $f_k \to f$ in $L^p(E)$ and $f_k \to g$ in $L^p(E)$, then $f = g$ a.e. on $E$.
> - (ii) *Norm convergence:* If $f_k \to f$ in $L^p(E)$, then $\|f_k\|_p \to \|f\|_p$.

^prop-19-15

> [!proof]+ Proof
> **(i)** $\|f - g\|_p = \|f - f_k + f_k - g\|_p \leq \|f - f_k\|_p + \|f_k - g\|_p \to 0$, so $\|f - g\|_p = 0$, i.e., $f = g$ a.e.
>
> **(ii)** By [[Minkowski's Inequality|Minkowski]]: $|\,\|f_k\|_p - \|f\|_p\,| \leq \|f_k - f\|_p \to 0$.

^pf-19-15

*Uses:* [[Minkowski's Inequality|§19.9]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-10|§19.10]]

> [!remark]- Connections
> - (i) is uniqueness of limits in a metric space ([[§13 Some Topological Concepts in Metric Spaces#^rem-13-4|451 §13 remark]]; [[§8 Hausdorff Spaces#^thm-8-3|590 §8.3]]), with “equal” meaning equal a.e.

## The Riesz–Fischer Theorem

> [!theorem] Lemma §19.16: Cauchy Subsequence Lemma
> Let $1 \leq p < \infty$ and $\{f_k\}$ be a Cauchy sequence in $L^p(E)$. Then there exists a subsequence $\{f_{k_j}\}_{j \in \mathbb{N}}$ and a function $f \in L^p(E)$ such that $f_{k_j}(x) \to f(x)$ for a.e. $x \in E$.

^lem-19-16

> [!proof]+ Proof
> Since $\{f_k\}$ is Cauchy in $L^p$, for each $j \geq 1$ there exists $k_j \in \mathbb{N}$ with $k_1 < k_2 < \cdots$ such that $\|f_k - f_m\|_p < 1/2^j$ for all $k, m \geq k_j$. In particular, $\|f_{k_{j+1}} - f_{k_j}\|_p < 1/2^j$.
>
> Let $g_0 = f_{k_1}$ and $g_j = f_{k_{j+1}} - f_{k_j}$ for $j \geq 1$. Then:
>
> $$
> \sum_{j=0}^{\infty} \|g_j\|_p \leq \|f_{k_1}\|_p + \sum_{j=1}^{\infty} \frac{1}{2^j} < \infty.
> $$
>
> By the $L^p$ absolute series test ([[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-14|Corollary §19.14]]), $\sum_{j=0}^{\infty} g_j(x)$ converges absolutely for a.e. $x \in E$. Define $f(x) = \sum_{j=0}^{\infty} g_j(x)$ where the series converges (and $f(x) = 0$ elsewhere). Since the partial sums telescope:
>
> $$
> f_{k_{l+1}}(x) = \sum_{j=0}^{l} g_j(x) \to f(x) \quad \text{a.e. on } E.
> $$
>
> Moreover, $f \in L^p$: by the $L^p$ absolute series test ([[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-14|Corollary §19.14]]), $\|f\|_p = \|\sum g_j\|_p \leq \sum \|g_j\|_p < \infty$.

^pf-19-16

*Uses:* [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-8|Def. §19.8]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-14|§19.14]]

> [!theorem] Corollary §19.17: $L^p$ Convergence Implies A.E. Convergent Subsequence
> If $f_k \to f$ in $L^p(E)$ ($1 \leq p < \infty$), then there exists a subsequence $\{f_{k_j}\}$ with $f_{k_j}(x) \to f(x)$ for a.e. $x \in E$.

^cor-19-17

> [!proof]+ Proof
> Since $f_k \to f$ in $L^p$, $\{f_k\}$ is Cauchy in $L^p$. By [[§19 Normed Linear Spaces and Lᵖ Spaces#^lem-19-16|the lemma]], there exists a subsequence $\{f_{k_j}\}$ converging a.e. to some $g \in L^p$. By uniqueness of $L^p$ limits ([[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-15|Proposition §19.15]]), $f = g$ a.e., so $f_{k_j} \to f$ a.e.

^pf-19-17

*Uses:* [[Minkowski's Inequality|§19.9]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^lem-19-16|§19.16]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-15|§19.15]]

> [!remark]- Connections
> - The case $p = 1$ is the step “every $L^1$-convergent sequence has a pointwise a.e. convergent subsequence” in [[§18 Differentiation Theory#^thm-18-26|Differentiation of the Integral (§18.26)]].
> - Only a subsequence: $L^p$ convergence does not imply a.e. convergence, and a.e. convergence upgrades to $L^1$ convergence under domination ([[Dominated Convergence Theorem|DCT]]).

> [!theorem] Theorem §19.18: Riesz–Fischer Theorem
> Let $1 \leq p \leq \infty$. Then $L^p(E)$ is a complete metric space (Banach space).

^thm-19-18

> [!proof]+ Proof
> **Case 1: $p = \infty$.** Let $\{f_k\}$ be Cauchy in $L^\infty(E)$: for every $\varepsilon > 0$, there exists $N$ such that $\|f_k - f_m\|_\infty < \varepsilon$ for all $k, m \geq N$.
>
> For each pair $k, m$, let $Z_{k,m} = \{x \in E : |f_k(x) - f_m(x)| > \|f_k - f_m\|_\infty\}$, so $m(Z_{k,m}) = 0$ ([[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|Proposition §19.2]]). Also let $Z_k = \{x \in E : |f_k(x)| > \|f_k\|_\infty\}$, again a null set, and let $Z = \bigcup_{k,m=1}^{\infty} Z_{k,m} \cup \bigcup_{k=1}^{\infty} Z_k$, so that each $f_k$ is bounded on $E \setminus Z$. Then $m(Z) = 0$, and on $E \setminus Z$:
>
> $$
> |f_k(x) - f_m(x)| \leq \|f_k - f_m\|_\infty < \varepsilon \quad \text{for all } k, m \geq N.
> $$
>
> So $\{f_k\}$ is uniformly Cauchy on $E \setminus Z$. By completeness of $\mathbb{R}$ ([[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|451 §10.8]]), there exists a bounded function $f$ on $E \setminus Z$ such that $f_k \to f$ [[§24 Uniform Convergence#^def-24-2|uniformly]] on $E \setminus Z$. Set $f = 0$ on $Z$. Then $f \in L^\infty(E)$ and $\|f_k - f\|_\infty \to 0$.
>
> **Case 2: $1 \leq p < \infty$.** Let $\{f_k\}$ be Cauchy in $L^p(E)$. By the [[§19 Normed Linear Spaces and Lᵖ Spaces#^lem-19-16|Cauchy subsequence lemma]], there exists a subsequence $\{f_{k_j}\}$ and $f \in L^p(E)$ with $f_{k_j} \to f$ a.e.
>
> It remains to show $f_k \to f$ in $L^p$. For every $\varepsilon > 0$, there exists $N$ such that $\|f_k - f_m\|_p < \varepsilon$ for all $k, m \geq N$. Fix $k \geq N$. For any $k_j \geq N$:
>
> $$
> \int_E |f_k - f_{k_j}|^p\,dx \leq \varepsilon^p.
> $$
>
> Since $f_{k_j} \to f$ a.e., by [[Fatou's Lemma|Fatou's lemma]]:
>
> $$
> \int_E |f_k - f|^p\,dx = \int_E \liminf_{j \to \infty} |f_k - f_{k_j}|^p\,dx \leq \liminf_{j \to \infty} \int_E |f_k - f_{k_j}|^p\,dx \leq \varepsilon^p.
> $$
>
> Hence $\|f_k - f\|_p \leq \varepsilon$ for all $k \geq N$, so $f_k \to f$ in $L^p$.

^pf-19-18

*Uses:* [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-8|Def. §19.8]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|§19.2]], [[Properties of Lebesgue Outer Measure|§9.1]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|451 §10.8]], [[§24 Uniform Convergence#^def-24-2|451 Def. §24.2]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^lem-19-16|§19.16]], [[Fatou's Lemma|§14.15]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-9|§14.9]]

> [!remark]- Connections
> - $L^p(E)$ is thus a [[§13 Some Topological Concepts in Metric Spaces#^def-13-3|complete metric space (451 Def. §13.3)]], like $\mathbb{R}^n$ ([[§13 Some Topological Concepts in Metric Spaces#^thm-13-2|451 §13.2]]); for $p = 2$, a complete inner product space (Hilbert space) extending [[§19 Inner Products and Norms#^ladr-6-4|LADR 6.4]].
> - The engine is the absolute series test ([[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-14|§19.14]]), itself built on [[Monotone Convergence Theorem (Lebesgue)|MCT]]; the upgrade from subsequence to full sequence is [[Fatou's Lemma|Fatou]].
> - Sequence analogue: [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^thm-13-5|556 Thm. §13.5]] ($\ell^p$ is a Banach space); for $p = 2$ it makes $L^2$ a Hilbert space in the sense of [[§17 Cauchy–Schwarz and the Induced Norm#^def-17-1|556 Def. §17.1]].

## Density and Separability

> [!definition] Definition §19.9: Dense Sets and Separability
> Let $(X, d)$ be a metric space. A subset $\mathcal{D} \subseteq X$ is **dense** in $X$ if for every $x \in X$, there exists a sequence $\{d_j\} \subseteq \mathcal{D}$ with $d(d_j, x) \to 0$. We say $(X, d)$ is **separable** if there exists a countable dense subset.

^def-19-9

> [!remark]- Connections
> - Topological versions: [[§18 Countability Axioms#^def-18-4|dense (590 Def. §18.4)]] and [[§18 Countability Axioms#^def-18-5|separable (590 Def. §18.5)]]; the sequential form agrees with $\overline{\mathcal{D}} = X$ in a metric space by [[§13 Some Topological Concepts in Metric Spaces#^prop-13-6|451 §13.6]].
> - In metric spaces, separable $\iff$ second countable: [[§18 Countability Axioms#^prop-18-4|590 §18.4]].
> - 556 versions: [[§8 Normed Linear Spaces#^def-8-7|556 Def. §8.7]] (dense, via the closure) and [[§20 Orthonormal Sets and Bases#^def-20-5|556 Def. §20.5]] (separable).

> [!example] Example §19.7
> $\mathbb{R}^n$ is separable: $\mathbb{Q}^n$ is a countable dense subset.

^ex-19-7

> [!remark]- Connections
> - Same example in Topology: [[§18 Countability Axioms#^ex-18-8|590 Ex. §18.8]]; countability of $\mathbb{Q}$: [[§3 Countability of Rationals and Unions#^cor-3-2|Corollary §3.2]].

> [!theorem] Theorem §19.19: Density in $L^p$
> Let $1 \leq p < \infty$. Then:
> - (i) The set of simple functions is dense in $L^p(E)$.
> - (ii) The set of step functions is dense in $L^p(E)$.
> - (iii) The set $C_c(\mathbb{R}^n)$ of compactly supported continuous functions is dense in $L^p(E)$.

^thm-19-19

> [!proof]+ Proof
> **(i) Simple functions are dense in $L^p$.** Let $f \in L^p(E)$. By the [[§12 Measurable Functions#^thm-12-15|Simple Function Approximation Theorem]], there exists a sequence of simple functions $\varphi_k$ with $|\varphi_k(x)| \leq |f(x)|$ for all $x$ and $\varphi_k(x) \to f(x)$ pointwise.
>
> Then $|\varphi_k - f|^p \leq (|\varphi_k| + |f|)^p \leq (2|f|)^p = 2^p|f|^p$. Since $f \in L^p$, $2^p|f|^p \in L^1(E)$. By [[Dominated Convergence Theorem|DCT]]:
>
> $$
> \int_E |\varphi_k - f|^p\,dx \to 0, \qquad \text{i.e.,} \quad \|\varphi_k - f\|_p \to 0.
> $$
>
> **(ii) Step functions are dense in $L^p$.** By (i), it suffices to approximate simple functions by [[§15 The General Lebesgue Integral#^def-15-2|step functions]]. Let $\varphi = \sum_{j=1}^{m} a_j \chi_{S_j}$ with $m(S_j) < \infty$ and the $S_j$ disjoint.
>
> It suffices to approximate each $\chi_S$ (with $m(S) < \infty$) by a step function in $\|\cdot\|_p$. By the approximation theorem ([[§11 Borel Sets and Measure Spaces#^thm-11-11|§11.11]]), for any $\delta > 0$ there exist disjoint rectangles $I_1, \ldots, I_q$ with $m(S \triangle \bigcup I_j) < \delta$ ([[§11 Borel Sets and Measure Spaces#^def-11-9|symmetric difference]]). Let $\psi = \sum \chi_{I_j}$. Then:
>
> $$
> \|\chi_S - \psi\|_p^p = \int |\chi_S - \chi_{\bigcup I_j}|^p\,dx = m(S \triangle \textstyle\bigcup I_j) < \delta,
> $$
>
> since $|\chi_S - \psi|^p = |\chi_S - \psi| = \chi_{S \triangle \bigcup I_j}$. Take $\delta = \varepsilon^p$.
>
> For the general simple function: approximate each $\chi_{S_j}$ by a step function $\psi_j$ with $\|\chi_{S_j} - \psi_j\|_p < \varepsilon/(m \max |a_j|)$, then $\psi = \sum a_j \psi_j$ satisfies $\|\varphi - \psi\|_p \leq \sum |a_j| \|\chi_{S_j} - \psi_j\|_p < \varepsilon$.
>
> **(iii) $C_c(\mathbb{R}^n)$ is dense in $L^p$.** By (ii), it suffices to approximate step functions. By linearity, it suffices to approximate $\chi_R$ for a rectangle $R$ with $m(R) < \infty$.
>
> Construct the same “trapezoidal” continuous approximation $g$ as in the $L^1$ proof ([[Continuous Functions of Compact Support are Dense in L¹|§16.7]]): $g$ is continuous, compactly supported, $0 \leq g \leq 1$, and $|\chi_R(x) - g(x)| \leq 1$ with equality only on transition regions of total measure $\leq C\varepsilon'$. Since $|\chi_R - g|^p \leq |\chi_R - g| \leq 1$ (as $0 \leq g \leq 1$):
>
> $$
> \|\chi_R - g\|_p^p = \int |\chi_R - g|^p\,dx \leq \int |\chi_R - g|\,dx = \|\chi_R - g\|_1 < C\varepsilon'.
> $$
>
> Choose $\varepsilon'$ small enough so that $C\varepsilon' < \varepsilon^p$.

^pf-19-19

*Uses:* [[§12 Measurable Functions#^thm-12-15|§12.15]], [[Dominated Convergence Theorem|§15.8]], [[§15 The General Lebesgue Integral#^def-15-2|Def. §15.2]], [[§11 Borel Sets and Measure Spaces#^thm-11-11|§11.11]], [[§11 Borel Sets and Measure Spaces#^def-11-9|Def. §11.9]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-11|§19.11]], [[Continuous Functions of Compact Support are Dense in L¹|§16.7]]

> [!remark]- Connections
> - The $L^1$ versions: [[§16 The L¹ Space and Density Theorems#^thm-16-5|§16.5]], [[§16 The L¹ Space and Density Theorems#^thm-16-6|§16.6]], [[Continuous Functions of Compact Support are Dense in L¹|§16.7]].
> - 556 strengthens (iii) to smooth compactly supported approximants, [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-4|556 Thm. §14.4]]; the failure for $p = \infty$ is [[§14 The Function Spaces Lᵖ(Ω)#^prop-14-5|556 Prop. §14.5]].

> [!remark] Remark: The Approximation Chain for $L^p$
> We have:
>
> $$
> C_c(\mathbb{R}^n) \;\longrightarrow\; \text{step functions} \;\longrightarrow\; \text{simple functions} \;\longrightarrow\; L^p(E),
> $$
>
> with each class dense in the next in the $L^p$ norm ($1 \leq p < \infty$). This chain fails for $p = \infty$, but not at the last step: simple functions are dense in $L^\infty$ (uniform approximation of bounded functions, [[§12 Measurable Functions#^thm-12-17|Theorem §12.17]], applied off a null set). It breaks at step functions and $C_c$: for $L^\infty$, continuous functions are *not* dense (e.g., $\chi_{[0,1]}$ cannot be uniformly approximated by continuous functions on $\mathbb{R}$).

^rem-19-4

> [!remark]- Connections
> - The $L^1$ chain: [[§16 The L¹ Space and Density Theorems#^rem-16-1|Remark §16]]. Why $\chi_{[0,1]}$ fails in $L^\infty$: a uniform limit of continuous functions is continuous ([[§12 Measurable Functions#^thm-12-16|§12.16]], [[§24 Uniform Convergence#^thm-24-2|451 §24.2]]).

> [!theorem] Corollary §19.20: $L^p$ is Separable for $1 \leq p < \infty$
> Let $1 \leq p < \infty$. Then $L^p(E)$ is [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-9|separable]].

^cor-19-20

> [!proof]+ Proof
> Let $\mathcal{D} = \{\sum_{j=1}^{n} c_j \chi_{I_j} : c_j \in \mathbb{Q},\; I_j \text{ intervals with rational endpoints, mutually disjoint}, \; n \in \mathbb{N}\}$. Then $\mathcal{D}$ is countable (rational coefficients, rational endpoints, finite sums). By density of step functions in $L^p$ ([[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|Theorem §19.19]]), any $f \in L^p$ can be approximated by step functions, which can in turn be approximated by elements of $\mathcal{D}$ (replace real coefficients and endpoints by rational ones). Hence $\mathcal{D}$ is dense.

^pf-19-20

*Uses:* [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-9|Def. §19.9]], [[§3 Countability of Rationals and Unions#^cor-3-2|§3.2]], [[Countable Union of Countable Sets is Countable|§3.1]], [[§1 Countability and Set Theory#^ex-1-3|Ex. §1.3]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|§19.19]]

> [!remark]- Connections
> - Same result in 556, proved with rational rectangles in ℝⁿ: [[§20 Orthonormal Sets and Bases#^prop-20-15|556 Prop. §20.15]]; the case $L^2(\mathbb{R}^n)$ is [[§24 Position Eigenstates and Continuous Resolutions#^thm-24-2|556 Thm. §24.2]].

> [!theorem] Theorem §19.21: $L^\infty$ is Not Separable
> $L^\infty(E)$ is not separable (when $E$ has positive measure).

^thm-19-21

> [!proof]+ Proof
> Consider $E = (0, 1)$ and for each $t \in (0, 1)$, define $f_t = \chi_{(0, t)}$. For $s \neq t$:
>
> $$
> \|f_s - f_t\|_\infty = \|\chi_{(\min(s,t),\, \max(s,t))}\|_\infty = 1.
> $$
>
> So $\{f_t\}_{t \in (0,1)}$ is an [[§4 Uncountability#^ex-4-2|uncountable]] family with pairwise distance $1$. Any dense subset must contain a point within distance $1/2$ of each $f_t$, and since the $1/2$-balls around distinct $f_t$'s are disjoint, the dense subset must be uncountable. For a general $E$ with $m(E) > 0$, the same argument works with $f_t = \chi_{E_0 \cap \{x_1 < t\}}$, where $E_0 \subseteq E$ has $0 < m(E_0) < \infty$: by [[Continuity of Measure|continuity of measure]], $t \mapsto m(E_0 \cap \{x_1 < t\})$ is continuous and increasing, so it takes uncountably many values, and two $f_t$ with different values are at distance $1$.

^pf-19-21

*Uses:* [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-6|Def. §19.6]], [[§4 Uncountability#^ex-4-2|Ex. §4.2]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-9|Def. §19.9]]

> [!remark]- Connections
> - Same uncountable-versus-countable counting as in [[§18 Countability Axioms#^prop-18-4|590 §18.4]](2) ($\mathbb{R}_l$ not second countable); by [[§18 Countability Axioms#^prop-18-4|590 §18.4]](3), $L^\infty$ is also not second countable.
> - Stated without proof in 556 as [[§20 Orthonormal Sets and Bases#^prop-20-16|556 Prop. §20.16]]; the sequence analogue is [[§20 Orthonormal Sets and Bases#^prop-20-14|556 Prop. §20.14]] ($\ell^\infty$ is not separable).
