---
type: section
subject: "[[Measure Theory]]"
chapter: 6
section: 34
tags: [measure-theory, math551]
---
← [[§33 The Cantor Function]] · ↑ [[· 6 Lᵖ Spaces]] · [[§35 Lᵖ as a Banach Space]] →

## Normed Linear Spaces

> [!definition] Definition §34.1: Linear Space
> A set $X$ is called a **linear space** (or [[§2 Definition of Vector Space#^ladr-1-20|vector space]]) over $\mathbb{R}$ if for all $v_1, v_2 \in X$ and $c_1, c_2 \in \mathbb{R}$, we have $c_1 v_1 + c_2 v_2 \in X$ (with the usual axioms of vector addition and scalar multiplication).

^def-34-1

> [!remark]- Connections
> - The axioms in full: [[§2 Definition of Vector Space#^ladr-1-20|LADR 1.20]]; the closure condition $c_1v_1 + c_2v_2 \in X$ is the subspace test [[§3 Subspaces#^ladr-1-34|LADR 1.34]].
> - Same definition in 556, over ℝ or ℂ, where subspaces, quotients and complements are developed: [[§1 Linear Spaces#^def-1-1|556 Def. §1.1]].

> [!example] Example §34.1: Linear Spaces in This Course
> $\mathbb{R}^n$, $L^1(E)$ ([[§24 The L¹ Space and Density Theorems#^thm-24-4|Theorem §24.4]]), $BV([a,b])$ ([[§28 Differentiation Theory#^prop-28-4|Proposition §28.4]]), and $AC([a,b])$ ([[§31 Absolute Continuity#^prop-31-1|Proposition §31.1]]) are all linear spaces.

^ex-34-1

> [!definition] Definition §34.2: Norm
> Let $X$ be a linear space. A function $\|\cdot\|: X \to \mathbb{R}$ is called a **norm** if:
> - (i) $\|x\| \geq 0$ for all $x \in X$, and $\|x\| = 0$ if and only if $x = 0$.
> - (ii) $\|x + y\| \leq \|x\| + \|y\|$ for all $x, y \in X$ (triangle inequality).
> - (iii) $\|cx\| = |c|\,\|x\|$ for all $c \in \mathbb{R}$, $x \in X$ (homogeneity).
>
> The pair $(X, \|\cdot\|)$ is called a **normed linear space**.

^def-34-2

> [!remark]- Connections
> - The norm of an inner product space, $\|v\| = \sqrt{\langle v, v\rangle}$ ([[§20 Inner Products and Norms#^ladr-6-7|LADR 6.7]]), satisfies (i), (iii) by [[§20 Inner Products and Norms#^ladr-6-9|LADR 6.9]] and (ii) by the [[Triangle inequality|triangle inequality (LADR 6.17)]].
> - Which norms come from an inner product is decided by the [[§20 Inner Products and Norms#^ladr-6-21|parallelogram equality (LADR 6.21)]]; among the $L^p$ norms only $p = 2$ does.
> - 556 version over ℝ or ℂ, alongside seminorms: [[§11 Normed Linear Spaces#^def-11-1|556 Def. §11.1]], [[§11 Normed Linear Spaces#^def-11-2|556 Def. §11.2]]; that among the $L^p$ norms only $p = 2$ comes from an inner product is [[§24 The Parallelogram Law and Jordan–von Neumann#^cor-24-3|556 Cor. §24.3]].

> [!example] Example §34.2: Norms on $\mathbb{R}^n$
> For $\mathbf{x} = (x_1, \ldots, x_n) \in \mathbb{R}^n$: $\|\mathbf{x}\|_2 = \left(\sum_{i=1}^{n} x_i^2\right)^{1/2}$ is the Euclidean norm, and $\|\mathbf{x}\|_1 = \sum_{i=1}^{n} |x_i|$ is the $\ell^1$ norm. Both are norms on $\mathbb{R}^n$.

^ex-34-2

![[m551-19-1.svg]]
*Unit balls $\{\|x\| \leq 1\}$ in $\mathbb{R}^2$: the $\ell^1$ ball is the red diamond and the Euclidean ball the blue disk. The $\ell^4$ ball (dashed) and the square of $\max_i |x_i|$ (gray, the limit $p \to \infty$) show the balls of $\|x\|_p = (\sum_i |x_i|^p)^{1/p}$ growing toward the square as $p$ increases. The shapes differ, but each is convex and symmetric about $0$, as the triangle inequality and homogeneity require.*

> [!remark]- Connections
> - $\|\cdot\|_2$ is the inner-product norm of [[§20 Inner Products and Norms#^ladr-6-8|LADR 6.8(a)]]; its metric is the Euclidean metric of [[§12 Metric Topology#^ex-12-1|590 Ex. §12.1]].
> - Comparing norms on $\mathbb{R}^n$: [[§13 Some Topological Concepts in Metric Spaces#^prop-13-1|451 §13.1]] ($d$ vs. $d_\infty$).

> [!example] Example §34.3: Norms on Function Spaces
> $L^1(E)$: $\|f\|_1 = \int_E |f(x)|\,dx$ ([[§24 The L¹ Space and Density Theorems#^def-24-2|Def. §24.2]]). Then $(L^1(E), \|\cdot\|_1)$ is a normed linear space ([[§24 The L¹ Space and Density Theorems#^thm-24-4|Theorem §24.4]]).
>
> $BV([a,b])$: $\bigvee_a^b(f)$ ([[§28 Differentiation Theory#^def-28-2|Def. §28.2]], [[§28 Differentiation Theory#^def-28-3|Def. §28.3]]) is a norm on $BV([a,b]) / \{\text{constants}\}$ (since $\bigvee_a^b(f) = 0$ iff $f$ is constant, not necessarily zero).

^ex-34-3

> [!remark]- Connections
> - $BV([a,b]) / \{\text{constants}\}$ is a quotient space in the sense of [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]]; homogeneity and the triangle inequality for $\bigvee_a^b$ are [[§28 Differentiation Theory#^prop-28-4|Proposition §28.4]](ii).

> [!theorem] Proposition §34.1: Every Normed Space is a Metric Space
> If $(X, \|\cdot\|)$ is a normed linear space, then $d(x, y) = \|x - y\|$ defines a [[§12 Metric Topology#^def-12-1|metric]] on $X$.

^prop-34-1

> [!proof]+ Proof
> $d(x, y) = \|x - y\| \geq 0$ with equality iff $x = y$ (property (i)). Symmetry: $d(x, y) = \|x - y\| = \|{-(y - x)}\| = |{-1}|\,\|y - x\| = d(y, x)$. Triangle inequality: $d(x, y) = \|x - y\| = \|(x - z) + (z - y)\| \leq \|x - z\| + \|z - y\| = d(x, z) + d(z, y)$.

^pf-34-1

*Uses:* [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-2|Def. §34.2]], [[§12 Metric Topology#^def-12-1|590 Def. §12.1]]

> [!remark]- Connections
> - Metric axioms: [[§12 Metric Topology#^def-12-1|590 Def. §12.1]], [[§13 Some Topological Concepts in Metric Spaces#^def-13-1|451 Def. §13.1]]. The same observation for inner product spaces: [[Triangle inequality|LADR 6.17]].
> - The $L^1$ case was [[§24 The L¹ Space and Density Theorems#^def-24-3|Def. §24.3]].
> - Same statement and proof in 556: [[§11 Normed Linear Spaces#^prop-11-2|556 Prop. §11.2]].

## Completeness and Banach Spaces

> [!definition] Definition §34.3: Convergence
> Let $(X, \|\cdot\|)$ be a normed linear space. A sequence $\{x_k\}_{k=1}^{\infty} \subseteq X$ **converges** to $a \in X$ if $\lim_{k \to \infty} \|x_k - a\| = 0$. We write $\lim_{k \to \infty} x_k = a$ in $(X, \|\cdot\|)$.

^def-34-3

> [!remark]- Connections
> - These are the metric-space notions of [[§13 Some Topological Concepts in Metric Spaces#^def-13-2|451 Def. §13.2]] and [[§13 Some Topological Concepts in Metric Spaces#^def-13-3|451 Def. §13.3]] for $d(x,y) = \|x - y\|$.
> - 556 versions: [[§11 Normed Linear Spaces#^def-11-4|556 Def. §11.4]] (convergence).

> [!definition] Definition §34.4: Cauchy Sequences
> Let $(X, \|\cdot\|)$ be a normed linear space and $\{x_k\}_{k=1}^{\infty} \subseteq X$.
>
> The sequence is a **Cauchy sequence** if for every $\varepsilon > 0$, there exists $N > 0$ such that $\|x_k - x_m\| < \varepsilon$ for all $k, m > N$.

^def-34-4

> [!remark]- Connections
> - Cauchy sequences on $\mathbb{R}$: [[§10a Cauchy Sequences#^def-10a-1|451 Def. §10a.1]].
> - 556 version: [[§11 Normed Linear Spaces#^def-11-5|556 Def. §11.5]] (Cauchy sequence).

> [!definition] Definition §34.5: Banach Space
> A normed linear space $(X, \|\cdot\|)$ is **complete** if every Cauchy sequence in $X$ converges to a limit in $X$. A complete normed linear space is called a **Banach space**.

^def-34-5

> [!remark]- Connections
> - A Banach space is a normed space that is a [[§13 Some Topological Concepts in Metric Spaces#^def-13-4|complete metric space (451 Def. §13.4)]] under $d(x,y) = \|x - y\|$ ([[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-1|Proposition §34.1]]).
> - 556 version: [[§12 Completeness#^def-12-2|556 Def. §12.2]]; every normed space has a Banach completion ([[§13 The Completion of a Normed Space#^thm-13-1|556 Thm. §13.1]]), and $L^p[a,b]$ is the completion of $C[a,b]$ in the $p$-norm ([[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8|556 Prop. §19.8]]).

> [!example] Example §34.4: Banach Spaces
> $(\mathbb{R}^n, \|\cdot\|_1)$ and $(\mathbb{R}^n, \|\cdot\|_2)$ are Banach spaces (completeness of $\mathbb{R}^n$ in any norm; [[§13 Some Topological Concepts in Metric Spaces#^thm-13-2|451 §13.2]]). The [[Riesz–Fischer Theorem|Riesz–Fischer theorem]] states that $(L^1(E), \|\cdot\|_1)$ is a Banach space.

^ex-34-4

## $L^p$ Spaces

> [!definition] Definition §34.6: $L^p$ Space
> Let $E \in \mathcal{M}(\mathbb{R}^n)$ and $1 \leq p < \infty$. A [[§15 Measurable Functions#^def-15-2|measurable function]] $f$ on $E$ belongs to $L^p(E)$ if:
>
> $$
> \int_E |f(x)|^p\,dx < \infty.
> $$
>
> (Note: $|f(x)|^p$ is still measurable since $t \mapsto |t|^p$ is continuous.)

^def-34-6

> [!definition] Definition §34.7: $L^p$ Norm
> Let $E \in \mathcal{M}(\mathbb{R}^n)$, $1 \leq p < \infty$ and $f \in L^p(E)$. We define the $L^p$ **norm** of $f$ by:
>
> $$
> \|f\|_{L^p(E)} = \|f\|_p = \left(\int_E |f(x)|^p\,dx\right)^{1/p}.
> $$

^def-34-7

> [!remark] Remark
> When $p = 1$, this recovers $L^1(E)$ with $\|f\|_1 = \int_E |f|\,dx$ ([[§24 The L¹ Space and Density Theorems#^def-24-1|Def. §24.1]], [[§24 The L¹ Space and Density Theorems#^def-24-2|Def. §24.2]]). The $L^p$ spaces for $p > 1$ are important in functional analysis and PDE theory. The key results (proved later in this section and the next) are:
>
> Hölder's inequality ([[Hölder's Inequality|Theorem §34.5]]): $\|fg\|_1 \leq \|f\|_p \|g\|_q$ where $1/p + 1/q = 1$.
>
> Minkowski's inequality ([[Minkowski's Inequality|Theorem §35.2]]): $\|f + g\|_p \leq \|f\|_p + \|g\|_p$ (the triangle inequality for $\|\cdot\|_p$).
>
> Riesz–Fischer theorem ([[Riesz–Fischer Theorem|Theorem §35.11]]): $(L^p(E), \|\cdot\|_p)$ is a Banach space for all $1 \leq p < \infty$.
>
> The case $p = 2$ is especially important: $L^2(E)$ is a Hilbert space with [[§20 Inner Products and Norms#^ladr-6-2|inner product]] $\langle f, g \rangle = \int_E f(x)\,g(x)\,dx$, and $\|f\|_2 = \langle f, f \rangle^{1/2}$ ([[§20 Inner Products and Norms#^ladr-6-7|LADR 6.7]]).

^rem-34-1

> [!remark]- Connections
> - The Riemann-integral prototype of this inner product and norm: [[§20 Inner Products and Norms#^ladr-6-3|LADR 6.3(c)]], [[§20 Inner Products and Norms#^ladr-6-8|LADR 6.8(b)]].
> - 556's working definition on open sets of ℝⁿ: [[§19 The Function Spaces Lᵖ(Ω)#^def-19-1|556 Def. §19.1]]; with counting measure on ℕ ([[§12 Borel Sets and Measure Spaces#^ex-12-2|Ex. §12.2]]) this definition gives the sequence spaces of [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^def-18-1|556 Def. §18.1]].

> [!example] Example §34.5: $L^p$ Membership Depends on $p$
> Let $E = (0, 1)$ and $g(x) = 1/\sqrt{x}$. Then $g \in L^p((0,1))$ iff $\int_0^1 x^{-p/2}\,dx < \infty$ iff $p/2 < 1$ iff $p < 2$. So $g \in L^1$ but $g \notin L^2$.
>
> Let $E = (0, 1)$ and $f(x) = \ln(1/x)$. Then $f \in L^\infty((0,1))$ ([[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-8|Def. §34.8]])? No: $\ln(1/x) \to \infty$ as $x \to 0^+$. But $\int_0^1 |\ln(1/x)|^p\,dx < \infty$ for all $1 \leq p < \infty$ (since $|\ln(1/x)| \leq c\,|x|^{-\alpha}$ for any $\alpha > 0$).

^ex-34-5

![[m551-19-2.svg]]
*$L^p$ membership depends on $p$. On $(0,1)$ the function $g = 1/\sqrt{x}$ (blue) has finite area $\int_0^1 g = 2$, but squaring makes the singularity worse, and $g^2 = 1/x$ (red) has infinite area. On a set of finite measure, large $p$ punishes tall spikes, which is why $L^{p_2} \subseteq L^{p_1}$ for $p_1 < p_2$ there ([[§34 Normed Linear Spaces and Lᵖ Spaces#^cor-34-6|Corollary §34.6]]).*

## $L^\infty$ and the Essential Supremum

> [!definition] Definition §34.8: $L^\infty$ Space
> Let $E \in \mathcal{M}(\mathbb{R}^n)$ and $f$ a measurable function on $E$. We say $f \in L^\infty(E)$ if there exists a constant $M > 0$ such that $|f(x)| \leq M$ for [[§16 Limits and Positive Parts of Measurable Functions#^def-16-2|a.e.]] $x \in E$. Such $f$ is called **essentially bounded**.

^def-34-8

> [!definition] Definition §34.9: Essential Supremum
> Let $E \in \mathcal{M}(\mathbb{R}^n)$ and $f$ a measurable function on $E$.
>
> The **essential supremum** of $|f|$ is:
>
> $$
> \|f\|_\infty = \|f\|_{L^\infty(E)} = \operatorname*{ess\,sup}_{x \in E} |f(x)| = \inf\{M \geq 0 : m(\{x \in E : |f(x)| > M\}) = 0\}.
> $$

^def-34-9

> [!example] Example §34.6
> $f(x) = 1$ for $x \in \mathbb{R} \setminus \mathbb{Q}$, $f(x) = \infty$ for $x \in \mathbb{Q}$. Then $f \in L^\infty(\mathbb{R})$ with $\|f\|_\infty = 1$, since $\{|f| > 1\} = \mathbb{Q}$ has measure zero ([[§10 Lebesgue Outer Measure#^ex-10-2|Example §10.2]]).

^ex-34-6

> [!theorem] Proposition §34.2: The Essential Supremum is Achieved A.E.
> If $f$ is an a.e. finite measurable function on $E$, then $m(\{x \in E : |f(x)| > \|f\|_\infty\}) = 0$.

^prop-34-2

> [!proof]+ Proof
> Let $M_0 = \|f\|_\infty = \inf\{M : m(\{|f| > M\}) = 0\}$. There exists a sequence $M_k \searrow M_0$ with $m(\{|f| > M_k\}) = 0$ for each $k$. Then:
>
> $$
> \{x \in E : |f(x)| > M_0\} = \bigcup_{k=1}^{\infty} \{x \in E : |f(x)| > M_k\},
> $$
>
> so $m(\{|f| > M_0\}) \leq \sum_{k=1}^{\infty} m(\{|f| > M_k\}) = 0$ ([[Properties of Lebesgue Outer Measure|countable subadditivity]]).

^pf-34-2

*Uses:* [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-9|Def. §34.9]], [[Properties of Lebesgue Outer Measure|§10.1]]

## The Limit Theorem: $\lim_{p \to \infty} \|f\|_p = \|f\|_\infty$

> [!theorem] Theorem §34.3
> Let $E$ be measurable with $m(E) < \infty$, and $f$ a measurable function on $E$. Then:
>
> $$
> \lim_{p \to \infty} \|f\|_p = \|f\|_\infty.
> $$

^thm-34-3

> [!proof]+ Proof
> *Step 1: $\limsup_{p \to \infty} \|f\|_p \leq \|f\|_\infty$.* If $\|f\|_\infty = \infty$, this is trivial. If $\|f\|_\infty = M < \infty$, then $|f(x)| \leq M$ a.e. on $E$ ([[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|Proposition §34.2]]), so:
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

^pf-34-3

*Uses:* [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-9|Def. §34.9]], [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|§34.2]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-2|§21.2]], [[§20 The Lebesgue Integral for Simple Functions#^cor-20-5|§20.5]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-6|451 §10.6]]

## Hölder's Inequality

> [!definition] Definition §34.10: Conjugate Exponents
> For $1 \leq p \leq \infty$, the **conjugate exponent** $p'$ is defined by:
>
> $$
> \frac{1}{p} + \frac{1}{p'} = 1, \qquad \text{i.e.,} \quad p' = \frac{p}{p - 1}.
> $$
>
> Convention: $p = 1 \Leftrightarrow p' = \infty$, and $p = \infty \Leftrightarrow p' = 1$.

^def-34-10

> [!remark]- Connections
> - Same definition in 556: [[§17 Hölder's Inequality for Sequences#^def-17-3|556 Def. §17.3]].

> [!theorem] Lemma §34.4: Young's Inequality
> For $a, b > 0$ and $0 < \theta < 1$: $a^\theta\,b^{1-\theta} \leq \theta\,a + (1 - \theta)\,b$.

^lem-34-4

> [!proof]+ Proof
> It suffices to show $\ln(a^\theta\,b^{1-\theta}) \leq \ln(\theta\,a + (1 - \theta)\,b)$. The left side is $\theta\ln a + (1-\theta)\ln b$. Since $\ln$ is concave ($\ln(\theta\,a + (1 - \theta)\,b) \geq \theta\,\ln a + (1 - \theta)\,\ln b$ by Jensen's inequality), the result follows.

^pf-34-4

![[m551-19-3.svg]]
*Young's inequality is the concavity of $\ln$ (shown with $\theta = 0.35$). The chord from $(a, \ln a)$ to $(b, \ln b)$ (red) lies below the graph, so at $\theta a + (1-\theta)b$ the chord height $\theta\ln a + (1-\theta)\ln b = \ln(a^\theta b^{1-\theta})$ is below $\ln(\theta a + (1-\theta)b)$. Carrying the chord height across to the graph (dashed) locates $a^\theta b^{1-\theta}$ on the axis, to the left of $\theta a + (1-\theta)b$ because $\ln$ is increasing.*

> [!remark]- Connections
> - Same inequality in 556, proved by the same concavity argument: [[§16 Means and Young's Inequality#^lem-16-3|556 Lemma §16.3]].

> [!theorem] Theorem §34.5: Hölder's Inequality
> Let $f, g$ be measurable functions on $E$. Let $1 \leq p \leq \infty$ and $p'$ its [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-10|conjugate]]. Then:
>
> $$
> \int_E |f(x)\,g(x)|\,dx \leq \|f\|_{L^p(E)}\,\|g\|_{L^{p'}(E)}.
> $$
>
> The case $p = p' = 2$ is the **Cauchy–Schwarz inequality**: $\int_E |fg|\,dx \leq \|f\|_2\,\|g\|_2$.

^thm-34-5

> [!proof]+ Proof
> **Case 1: $\|g\|_{p'} = 0$.** Then $g = 0$ a.e. ([[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|Proposition §21.4]]), so $fg = 0$ a.e., and both sides are $0$.
>
> **Case 2: $\|g\|_{p'} \neq 0$ and $\|f\|_p = \infty$.** The right side is $\infty$, so the inequality holds trivially. (We use the convention $0 \cdot \infty = 0$. By symmetry, if $\|f\|_p = 0$ then $f = 0$ a.e. and both sides are $0$, and if $\|f\|_p \neq 0$ and $\|g\|_{p'} = \infty$ the right side is $\infty$. So from now on both norms lie in $(0, \infty)$.)
>
> **Case 3: $p = 1$, $p' = \infty$.** Since $g \in L^\infty(E)$, $|g(x)| \leq \|g\|_\infty$ a.e. ([[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|Proposition §34.2]]). So:
>
> $$
> \int_E |f\,g|\,dx \leq \int_E |f|\,\|g\|_\infty\,dx = \|f\|_1\,\|g\|_\infty.
> $$
>
> The case $p = \infty$, $p' = 1$ is the same with the roles of $f$ and $g$ exchanged.
>
> **Case 4: $1 < p < \infty$, $1 < p' < \infty$.** Assume $\|f\|_p, \|g\|_{p'} \in (0, \infty)$. Apply [[§34 Normed Linear Spaces and Lᵖ Spaces#^lem-34-4|Young's inequality]] with $\theta = 1/p$, $1 - \theta = 1/p'$, $a = |f(x)|^p / (\|f\|_p)^p$, $b = |g(x)|^{p'} / (\|g\|_{p'})^{p'}$:
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

^pf-34-5

*Uses:* [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-10|Def. §34.10]], [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|§21.4]], [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-2|§21.2]], [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|§34.2]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[§34 Normed Linear Spaces and Lᵖ Spaces#^lem-34-4|§34.4]], [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|§21.1]]

> [!remark]- Connections
> - $p = 2$ is the [[Cauchy–Schwarz inequality|Cauchy–Schwarz inequality (LADR 6.14)]] for the $L^2$ inner product of [[§34 Normed Linear Spaces and Lᵖ Spaces#^rem-34-1|the remark above]]; its Riemann-integral form for continuous functions is [[§20 Inner Products and Norms#^ladr-6-16|LADR 6.16(b)]].
> - Used to prove [[Minkowski's Inequality|Minkowski's inequality]], the $L^p$ inclusions ([[§34 Normed Linear Spaces and Lᵖ Spaces#^cor-34-6|Corollary §34.6]]) and [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-7|interpolation]].
> - Sequence version (counting measure), with the same proof: [[§17 Hölder's Inequality for Sequences#^thm-17-1|556 Thm. §17.1]]; the case $p = 2$ is the $L^2$ instance of the Cauchy–Schwarz inequality of every inner product space, [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|556 Thm. §23.1]].

> [!theorem] Corollary §34.6: $L^p$ Inclusion for Finite Measure Spaces
> Assume $m(E) < \infty$. Then for $1 \leq p_1 < p_2 \leq \infty$, $L^{p_2}(E) \subseteq L^{p_1}(E)$, and:
>
> $$
> \|f\|_{p_1} \leq \|f\|_{p_2} \cdot m(E)^{1/p_1 - 1/p_2}.
> $$
>
> (With the convention $1/\infty = 0$.)

^cor-34-6

> [!proof]+ Proof
> **Case 1: $p_2 = \infty$.** $f \in L^\infty(E)$ means $|f(x)| \leq \|f\|_\infty$ a.e. on $E$ ([[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|Proposition §34.2]]). Then:
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

^pf-34-6

*Uses:* [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|§34.2]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-10|Def. §34.10]], [[Hölder's Inequality|§34.5]]

> [!remark] Remark
> The finite measure hypothesis is essential: on $\mathbb{R}$, $f(x) = 1/\sqrt{|x|}$ for $|x| \leq 1$ and $0$ otherwise is in $L^1$ but not $L^2$. On infinite measure spaces the inclusion can reverse: $f(x) = 1/(1 + |x|) \in L^2(\mathbb{R})$ but $\notin L^1(\mathbb{R})$.

^rem-34-2

> [!remark]- Connections
> - For sequences the inclusion runs the other way, $\ell^p \subset \ell^q$ for $p < q$: [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^prop-18-4|556 Prop. §18.4]].

> [!theorem] Proposition §34.7: Interpolation of $L^p$ Norms
> Let $1 \leq r < s \leq \infty$ and $f \in L^r(E) \cap L^s(E)$. Then $f \in L^t(E)$ for all $r < t < s$, with:
>
> $$
> \|f\|_t \leq \|f\|_r^{\theta}\,\|f\|_s^{1-\theta}, \qquad \text{where } \theta \in (0, 1) \text{ satisfies } \frac{1}{t} = \frac{\theta}{r} + \frac{1-\theta}{s}.
> $$

^prop-34-7

> [!proof]+ Proof
> Write $|f(x)|^t = |f(x)|^{\theta t} \cdot |f(x)|^{(1-\theta)t}$. Apply [[Hölder's Inequality|Hölder]] with exponents $p = r/(\theta t)$ and $p' = s/((1-\theta)t)$. Note $1/p + 1/p' = \theta t/r + (1-\theta)t/s = t(1/t) = 1$, confirming these are conjugate. Then:
>
> $$
> \int_E |f|^t\,dx \leq \left(\int_E |f|^r\,dx\right)^{\theta t/r} \left(\int_E |f|^s\,dx\right)^{(1-\theta)t/s} = (\|f\|_r)^{\theta t}\,(\|f\|_s)^{(1-\theta)t}.
> $$
>
> Taking $t$-th roots: $\|f\|_t \leq \|f\|_r^{\theta}\,\|f\|_s^{1-\theta}$.
>
> This uses $\int_E |f|^s\,dx$, so it assumes $s < \infty$. If $s = \infty$, then $\theta = r/t$ and $|f|^t = |f|^r\,|f|^{t-r} \leq |f|^r\,\|f\|_\infty^{t-r}$ a.e. ([[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|Proposition §34.2]]), so $\|f\|_t^t \leq \|f\|_r^r\,\|f\|_\infty^{t-r}$; taking $t$-th roots gives $\|f\|_t \leq \|f\|_r^{\theta}\,\|f\|_\infty^{1-\theta}$.

^pf-34-7

*Uses:* [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-10|Def. §34.10]], [[Hölder's Inequality|§34.5]]

Minkowski's inequality, completeness (Riesz–Fischer) and density in $L^p$ continue in [[§35 Lᵖ as a Banach Space]].
