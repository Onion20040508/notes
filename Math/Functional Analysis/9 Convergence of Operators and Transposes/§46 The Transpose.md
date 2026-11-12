---
type: section
subject: "[[Functional Analysis]]"
chapter: 9
section: 46
tags: [functional-analysis, math556]
---
← [[§45 Convergence of Operators]] · ↑ [[· 9 Convergence of Operators and Transposes]] · [[§47 Bras, Kets, and the Riesz Map]] →

*Stage: maps — Thread: functionals. $\langle Mx, \ell \rangle = \langle x, M'\ell \rangle$ defines $M' : Y' \to X'$, with $\|M'\| = \|M\|$, $N(M') = R(M)^\perp$ and $(NM)' = M'N'$; weak convergence passes to transposes, strong convergence does not.*

*Lecture 20 (Thu Nov 12). Sources: the handwritten notes of the lecture and the Otter.ai transcript, which covers the lecture up to the norm of the transpose. The parts of the proofs that the lecture left out, and the results marked as such, are filled in.*

## Definition

For an $n \times n$ real matrix $A = (a_{ij})$, the transpose is $A^T = (a_{ji})$. With $A$ acting on $\mathbb{R}^n$ by $x \mapsto Ax$, the transpose is characterized through the inner product of $\mathbb{R}^n$:

$$
(Ax, y) = y^T A x = (A^T y)^T x = (x, A^T y) \qquad \text{for all } x, y \in \mathbb{R}^n .
$$

A normed linear space has no inner product. As for the Riesz representation, the dual space takes its place: the vector $y$ is replaced by a bounded linear functional $\ell$, and $(Ax, y)$ by $\ell(Mx)$.

> [!theorem] Proposition §46.1: Composing a Functional with a Bounded Map
> Let $X, Y$ be normed linear spaces and $M \in \mathcal{L}(X, Y)$. Then for every $\ell \in Y' = \mathcal{L}(Y, \mathbb{F})$ the composition $\ell M$, $(\ell M)(x) = \ell(Mx)$, belongs to $X'$, and $\|\ell M\| \le \|\ell\|\, \|M\|$.
>
> *Lax: §15.1, (7)*

^prop-46-1

> [!proof]+ Proof
> For $x \in X$, $Mx \in Y$, so $\ell(Mx)$ is defined. *Linear:* for $x_1, x_2 \in X$ and $c_1, c_2 \in \mathbb{F}$, by linearity of $M$ and then of $\ell$, $\ell(M(c_1 x_1 + c_2 x_2)) = \ell(c_1 Mx_1 + c_2 Mx_2) = c_1\, \ell(Mx_1) + c_2\, \ell(Mx_2)$. *Bounded:* by Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]](b), applied first to $\ell$ and then to $M$,
>
> $$
> |(\ell M)(x)| = |\ell(Mx)| \le \|\ell\|\, \|Mx\| \le \|\ell\|\, \|M\|\, \|x\| \qquad \text{for all } x \in X .
> $$
>
> So $\ell M$ is bounded (Definition [[§30 Boundedness and Continuity#^def-30-2|§30.2]]) with $\|\ell M\| \le \|\ell\|\, \|M\|$ (Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]](c)); that is, $\ell M \in X'$.

^pf-46-1

*Uses:* [[§30 Boundedness and Continuity#^prop-30-1|§30.1]], [[§30 Boundedness and Continuity#^def-30-2|Def. §30.2]]

> [!definition] Definition §46.1: Transpose
> Let $X, Y$ be normed linear spaces and $M \in \mathcal{L}(X, Y)$. The **transpose** of $M$ is the map $M' : Y' \to X'$ defined by
>
> $$
> M'\ell = \ell M , \qquad \text{that is,} \qquad (M'\ell)(x) = \ell(Mx) \quad \text{for all } x \in X, \ \ell \in Y' .
> $$
>
> In the notation $\ell(x) = \langle x, \ell \rangle$ for the action of a functional ([[§36 Duality in Normed Spaces|§36]]),
>
> $$
> \langle Mx, \ell \rangle = \langle x, M'\ell \rangle \qquad \text{for all } x \in X, \ \ell \in Y' .
> $$
>
> *Lax: §15.1, (7)–(8)*

^def-46-1

> [!remark]- Connections
> - In finite dimensions: the dual map $T'(\varphi) = \varphi \circ T$, [[§12 Duality#^ladr-3-118|LADR 3.118]]; its matrix is the transpose of the matrix of $T$, [[§12 Duality#^ladr-3-132|LADR 3.132]].
> - The pairing $\langle x, \ell \rangle = \ell(x)$: [[§36 Duality in Normed Spaces|§36]].

By Proposition [[§46 The Transpose#^prop-46-1|§46.1]], $M'\ell$ is indeed an element of $X'$.

> [!remark] Remark: Reading the Definition
> Written as $M'\ell = \ell M$ the definition is hard to remember; written in the pairing it is the matrix formula $(Ax, y) = (x, A^T y)$, with $\langle\,\cdot\,, \cdot\,\rangle$ in place of the inner product and the operator moved from the left slot to the right slot. The prime is the same symbol as for the dual space because the transpose acts between dual spaces: the dual replaces the inner product, and the transpose is how the matrix transpose carries over to normed spaces of infinite dimension. The arrows reverse: $M$ goes from $X$ to $Y$, $M'$ from $Y'$ to $X'$.

^rem-46-1

![[m556-46-1.svg]]

The transpose reverses the arrows. A vector $x$ is moved forward by $M$ and paired with $\ell$ in $Y$, or the functional $\ell$ is pulled back by $M'$ and paired with $x$ in $X$; both give the same number.

## Hilbert–Schmidt Operators

Measure-theoretic facts are used freely in this subsection, as in [[§35 Measures and the Radon–Nikodym Theorem|§35]]; with $\Omega = \mathbb{R}^n$ and Lebesgue measure nothing beyond Fubini's theorem is needed.

> [!definition] Definition §46.2: Hilbert–Schmidt Operator
> Let $(\Omega, \mathcal{B}, \mu)$ be a $\sigma$-finite measure space (for instance $\Omega = \mathbb{R}^n$ with Lebesgue measure), and
>
> $$
> L^2(\mu) = \Bigl\{ f : \Omega \to \mathbb{F} \text{ measurable} \ \Big|\ \int_\Omega |f(x)|^2\, d\mu(x) < \infty \Bigr\} ,
> $$
>
> with functions equal $\mu$-almost everywhere identified; it is a Hilbert space with $(f, g) = \int_\Omega f\, \overline{g}\, d\mu$. Let $K : \Omega \times \Omega \to \mathbb{F}$ belong to $L^2(\Omega \times \Omega, \mu \times \mu)$, that is,
>
> $$
> \|K\|_{L^2(\mu \times \mu)}^2 = \int_\Omega \int_\Omega |K(x, y)|^2\, d\mu(x)\, d\mu(y) < \infty .
> $$
>
> The **Hilbert–Schmidt operator** with **kernel** $K$ is the map $T$ given by
>
> $$
> Tf(x) = \int_\Omega K(x, y)\, f(y)\, d\mu(y), \qquad f \in L^2(\mu),
> $$
>
> at every $x$ where the integral exists.

^def-46-2

> [!remark] Remark: The Kernel as a Matrix
> An integral is a limit of sums. Approximating $Tf(x)$ by a Riemann sum over points $y_1, y_2, \ldots$,
>
> $$
> Tf(x) \approx \sum_j K(x, y_j)\, f(y_j)\, \Delta\mu(y_j) ,
> $$
>
> which has the form of a matrix acting on a vector,
>
> $$
> Ax = \begin{pmatrix} a_{11} & \cdots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{n1} & \cdots & a_{nn} \end{pmatrix} \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} = \begin{pmatrix} \sum_{j=1}^n a_{1j} x_j \\ \vdots \\ \sum_{j=1}^n a_{nj} x_j \end{pmatrix} = \Bigl( \sum_{j=1}^n a_{ij} x_j \Bigr)_{i=1}^n .
> $$
>
> The variable $x$ plays the role of the row index $i$, the variable $y$ of the column index $j$, the kernel $K(x, y)$ of the entries $a_{ij}$, and $f(y)$ of $x_j$. Only $y$ is summed over. The comparison is a guide, not part of any proof.

^rem-46-2

> [!theorem] Proposition §46.2: Hilbert–Schmidt Operators are Bounded
> Let $K$ and $T$ be as in Definition [[§46 The Transpose#^def-46-2|§46.2]], and let $f \in L^2(\mu)$. Then the integral defining $Tf(x)$ converges absolutely for $\mu$-almost every $x$, $Tf \in L^2(\mu)$, and $T : L^2(\mu) \to L^2(\mu)$ is a bounded linear map with
>
> $$
> \|T\| \le \|K\|_{L^2(\mu \times \mu)} .
> $$

^prop-46-2

> [!proof]+ Proof
> **Step 1: the integral exists for almost every $x$.**
> By [[Tonelli's Theorem|Tonelli's theorem]], $x \mapsto k(x) = \bigl( \int_\Omega |K(x, y)|^2\, d\mu(y) \bigr)^{1/2}$ is measurable and $\int_\Omega k(x)^2\, d\mu(x) = \|K\|_{L^2(\mu \times \mu)}^2 < \infty$, so $k(x) < \infty$ for $\mu$-almost every $x$. For such $x$, the Cauchy–Schwarz inequality in $L^2(\mu)$, in the variable $y$ with $x$ fixed (Theorem [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]]), gives
>
> $$
> \int_\Omega |K(x, y)|\, |f(y)|\, d\mu(y) \le \Bigl( \int_\Omega |K(x, y)|^2\, d\mu(y) \Bigr)^{1/2} \Bigl( \int_\Omega |f(y)|^2\, d\mu(y) \Bigr)^{1/2} = k(x)\, \|f\|_{L^2} < \infty .
> $$
>
> So the integral defining $Tf(x)$ converges absolutely, and $|Tf(x)| \le k(x)\, \|f\|_{L^2}$. ($Tf$ is measurable: on $E \times \Omega$ with $\mu(E) < \infty$ the function $K(x, y) f(y)$ is integrable, since $\int_E k\, \|f\|\, d\mu \le \mu(E)^{1/2} \|K\|\, \|f\| < \infty$, so [[Fubini's Theorem (Lebesgue)|Fubini's theorem]] applies there; and $\Omega$ is a countable union of such sets $E$ because $\mu$ is $\sigma$-finite.)
>
> **Step 2: the bound.** Squaring $|Tf(x)| \le k(x)\, \|f\|_{L^2}$ and integrating in $x$, the constant $\|f\|_{L^2}^2$ comes out of the integral:
>
> $$
> \int_\Omega |Tf(x)|^2\, d\mu(x) \le \|f\|_{L^2}^2 \int_\Omega \int_\Omega |K(x, y)|^2\, d\mu(y)\, d\mu(x) = \|K\|_{L^2(\mu \times \mu)}^2\, \|f\|_{L^2}^2 .
> $$
>
> So $Tf \in L^2(\mu)$ and $\|Tf\|_{L^2} \le \|K\|_{L^2(\mu \times \mu)}\, \|f\|_{L^2}$.
>
> **Step 3: linearity.** For $f_1, f_2 \in L^2(\mu)$ and $c_1, c_2 \in \mathbb{F}$, at every $x$ where both integrals exist, $T(c_1 f_1 + c_2 f_2)(x) = c_1\, Tf_1(x) + c_2\, Tf_2(x)$ by linearity of the integral; this holds for almost every $x$, hence in $L^2(\mu)$.
>
> By Steps 2 and 3, $T$ is a bounded linear map (Definition [[§30 Boundedness and Continuity#^def-30-2|§30.2]]) with $\|T\| \le \|K\|_{L^2(\mu \times \mu)}$ (Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]](c)).

^pf-46-2

*Uses:* [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]], [[§30 Boundedness and Continuity#^def-30-2|Def. §30.2]], [[§30 Boundedness and Continuity#^prop-30-1|§30.1]]

> [!remark]- Connections
> - Tools: [[Tonelli's Theorem]], [[Fubini's Theorem (Lebesgue)]].

> [!theorem] Proposition §46.3: The Transpose of a Hilbert–Schmidt Operator
> Let $K$ and $T$ be as in Definition [[§46 The Transpose#^def-46-2|§46.2]]. For $g \in L^2(\mu)$ let $\ell_g(f) = \int_\Omega f\, g\, d\mu$.
>
> 1. $g \mapsto \ell_g$ is an isometric isomorphism (Definition [[§13 The Completion of a Normed Space#^def-13-2|§13.2]]) of $L^2(\mu)$ onto $L^2(\mu)'$.
> 2. Let $T^t$ be the Hilbert–Schmidt operator with the **transposed kernel** $K^t(x, y) = K(y, x)$,
>
> $$
> T^t g(x) = \int_\Omega K(y, x)\, g(y)\, d\mu(y) .
> $$
>
> Then $T' \ell_g = \ell_{T^t g}$ for every $g \in L^2(\mu)$.
>
> So, with $L^2(\mu)'$ identified with $L^2(\mu)$ as in (1), the transpose of $T$ is the Hilbert–Schmidt operator whose kernel is $K$ with its two variables exchanged, as $a_{ij}$ becomes $a_{ji}$ for a matrix.

^prop-46-3

> [!proof]+ Proof
> (1)
> For $g \in L^2(\mu)$, $\ell_g(f) = \int_\Omega f\, \overline{\overline{g}}\, d\mu = (f, \overline{g})$. By the Riesz representation theorem with norms (Theorem [[§31 Dual Spaces#^thm-31-2|§31.2]]), $\ell_g \in L^2(\mu)'$ and $\|\ell_g\| = \|\overline{g}\|_{L^2} = \|g\|_{L^2}$. The map $g \mapsto \ell_g$ is linear (no conjugation occurs), so it is an isometry (Lemma [[§13 The Completion of a Normed Space#^lem-13-2|§13.2]](1)) and in particular one-to-one. It is onto: by the same theorem every $\ell \in L^2(\mu)'$ is $\ell = (\,\cdot\,, h)$ for some $h \in L^2(\mu)$, and $(\,\cdot\,, h) = \ell_{\overline{h}}$.
>
> (2) *$T^t$ is a Hilbert–Schmidt operator.* By Tonelli's theorem $\int_\Omega \int_\Omega |K(y, x)|^2\, d\mu(x)\, d\mu(y) = \|K\|_{L^2(\mu \times \mu)}^2$, so $K^t \in L^2(\mu \times \mu)$, and $T^t$ is bounded by Proposition [[§46 The Transpose#^prop-46-2|§46.2]].
>
> *Exchanging the order of integration.* Let $f, g \in L^2(\mu)$.
> The function $F(x, y) = g(x)\, f(y)$ has, by Tonelli's theorem, $\int\!\!\int |F|^2\, d\mu\, d\mu = \|g\|_{L^2}^2\, \|f\|_{L^2}^2$, so $F \in L^2(\mu \times \mu)$; by the Cauchy–Schwarz inequality in $L^2(\mu \times \mu)$,
>
> $$
> \int_\Omega \int_\Omega |K(x, y)|\, |f(y)|\, |g(x)|\, d\mu(y)\, d\mu(x) \le \|K\|_{L^2(\mu \times \mu)}\, \|g\|_{L^2}\, \|f\|_{L^2} < \infty .
> $$
>
> So $K(x, y)\, f(y)\, g(x)$ is integrable on $\Omega \times \Omega$, and [[Fubini's Theorem (Lebesgue)|Fubini's theorem]] allows the order of integration to be exchanged:
>
> $$
> \begin{aligned}(T'\ell_g)(f) = \ell_g(Tf) &= \int_\Omega \Bigl( \int_\Omega K(x, y)\, f(y)\, d\mu(y) \Bigr) g(x)\, d\mu(x) \\
> &= \int_\Omega \Bigl( \int_\Omega K(x, y)\, g(x)\, d\mu(x) \Bigr) f(y)\, d\mu(y) .\end{aligned}
> $$
>
> The inner integral is a function of $y$; it is $\int_\Omega K^t(y, x)\, g(x)\, d\mu(x) = T^t g(y)$. Hence $(T'\ell_g)(f) = \int_\Omega f(y)\, T^t g(y)\, d\mu(y) = \ell_{T^t g}(f)$. This holds for every $f \in L^2(\mu)$, so $T'\ell_g = \ell_{T^t g}$. Renaming the variables of integration ($x \leftrightarrow y$) gives the formula for $T^t g(x)$ in the statement.

^pf-46-3

*Uses:* [[§31 Dual Spaces#^thm-31-2|§31.2]], [[§13 The Completion of a Normed Space#^lem-13-2|§13.2]], [[§46 The Transpose#^prop-46-2|§46.2]]

![[m556-46-2.svg]]

A kernel and its transpose, drawn like matrices: the value $K(x, y)$ is the colour at row $x$ (downwards) and column $y$ (rightwards), dark for large values, so that row $x$ is the function $y \mapsto K(x, y)$ that is integrated against $f$ in $Tf(x)$. Left: $K(x, y) = e^{-((x - 0.3)^2 + (y - 0.75)^2)/0.02} + 0.6\, e^{-((x - 0.7)^2 + (y - 0.5)^2)/0.01}$ on $[0,1]^2$. Right: $K^t(x, y) = K(y, x)$, the reflection in the diagonal (dashed), as for the transpose of a matrix.

> [!remark] Remark: When Can a Map Equal its Transpose?
> For a matrix, $A$ is called self-adjoint (symmetric) when $A^T = A$, i.e. $a_{ij} = a_{ji}$. For $M \in \mathcal{L}(X, Y)$ the transpose is $M' \in \mathcal{L}(Y', X')$: it acts between other spaces, and $M' = M$ makes no sense unless $Y' = X$ and $X' = Y$. On a Hilbert space $H$, with $H'$ identified with $H$, both $M$ and $M'$ act on $H$, and the question makes sense; self-adjoint operators come later. For a Hilbert–Schmidt operator over $\mathbb{R}$, Proposition [[§46 The Transpose#^prop-46-3|§46.3]] shows that $T' = T$ under the identification there when $K(x, y) = K(y, x)$ almost everywhere. Over $\mathbb{C}$, Lax identifies $H'$ with $H$ through the inner product instead, which is conjugate-linear; then the transpose is replaced by the *adjoint* (Lax §15.1, end of the section), computed in the next example.

^rem-46-3

> [!example] Example §46.1: The Adjoint of a Hilbert–Schmidt Operator
> *(Not from lecture.)* Let $K$ and $T$ be as in Definition [[§46 The Transpose#^def-46-2|§46.2]], and let $T^\ast$ be the Hilbert–Schmidt operator with kernel $\overline{K(y, x)}$,
>
> $$
> T^\ast g(x) = \int_\Omega \overline{K(y, x)}\, g(y)\, d\mu(y) .
> $$
>
> Then $(Tf, g) = (f, T^\ast g)$ for all $f, g \in L^2(\mu)$. So $T^\ast$ is the adjoint of $T$, and $T^\ast = T$ when $K(x, y) = \overline{K(y, x)}$ for almost every $(x, y)$.

^ex-46-1

> [!proof]+ Proof
> $(Tf, g) = \int_\Omega \int_\Omega K(x, y)\, f(y)\, \overline{g(x)}\, d\mu(y)\, d\mu(x)$. The integrand is integrable on $\Omega \times \Omega$, by the estimate in the proof of Proposition [[§46 The Transpose#^prop-46-3|§46.3]] with $\overline{g}$ in place of $g$. Exchanging the order (Fubini) and using $K(x, y)\, \overline{g(x)} = \overline{\overline{K(x, y)}\, g(x)}$,
>
> $$
> (Tf, g) = \int_\Omega f(y)\, \overline{\Bigl( \int_\Omega \overline{K(x, y)}\, g(x)\, d\mu(x) \Bigr)}\, d\mu(y) = \int_\Omega f(y)\, \overline{T^\ast g(y)}\, d\mu(y) = (f, T^\ast g),
> $$
>
> since $T^\ast g(y) = \int_\Omega \overline{K(x, y)}\, g(x)\, d\mu(x)$ (the formula of the statement with $x$ and $y$ renamed). If $K(x, y) = \overline{K(y, x)}$ almost everywhere, the two kernels agree, so $T^\ast g = Tg$ for every $g$.

^pf-ex-46-1

*Uses:* [[§46 The Transpose#^prop-46-3|§46.3]]

## Basic Properties

> [!theorem] Proposition §46.4: Properties of the Transpose
> Let $X, Y$ be normed linear spaces.
>
> 1. Let $M \in \mathcal{L}(X, Y)$. Then $M' \in \mathcal{L}(Y', X')$, and $\|M'\| = \|M\|$.
> 2. Let $M, N \in \mathcal{L}(X, Y)$. Then $(M + N)' = M' + N'$.
>
> *Lax: §15.1, Thm 5(i), (iv)*

^prop-46-4

> [!remark]- Connections
> - In finite dimensions: [[§12 Duality#^ladr-3-120|LADR 3.120]] ((a) sums, (b) scalars, (c) products).

> [!proof]+ Proof
> (1)
> If $X = \{0\}$ or $Y = \{0\}$, then $M = 0$ and $M' = 0$, and both norms are $0$. Assume $X \neq \{0\}$ and $Y \neq \{0\}$.
>
> *$M'$ is linear.* For $\ell_1, \ell_2 \in Y'$, $c_1, c_2 \in \mathbb{F}$ and $x \in X$, by the definition of the operations on $Y'$,
>
> $$
> (M'(c_1 \ell_1 + c_2 \ell_2))(x) = (c_1 \ell_1 + c_2 \ell_2)(Mx) = c_1\, \ell_1(Mx) + c_2\, \ell_2(Mx) = (c_1 M'\ell_1 + c_2 M'\ell_2)(x) .
> $$
>
> *$\|M'\| \le \|M\|$.* Let $\ell \in Y'$. The norm of $M'\ell \in X'$ is a supremum over unit vectors of $X$ (Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]](a)); by $\langle x, M'\ell \rangle = \langle Mx, \ell \rangle$ and Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]](b), applied to $\ell$ and then to $M$,
>
> $$
> \begin{aligned}\|M'\ell\| &= \sup_{x \in X,\ \|x\| = 1} |\langle x, M'\ell \rangle| = \sup_{x \in X,\ \|x\| = 1} |\langle Mx, \ell \rangle| = \sup_{x \in X,\ \|x\| = 1} |\ell(Mx)| \\
> &\le \sup_{\|x\| = 1} \|\ell\|\, \|Mx\| \le \sup_{\|x\| = 1} \|\ell\|\, \|M\|\, \|x\| = \|\ell\|\, \|M\| .\end{aligned}
> $$
>
> So $M'$ is bounded, $M' \in \mathcal{L}(Y', X')$, and $\|M'\| \le \|M\|$ (Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]](c)).
>
> *$\|M\| \le \|M'\|$.* By Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]](a), $\|M\| = \sup_{\|x\| = 1} \|Mx\|$. To bring in the transpose, write the norm of each vector $Mx \in Y$ through functionals: $\|y\| = \max_{\ell \in Y',\ \|\ell\| = 1} |\ell(y)|$ for $y \in Y$ (Theorem [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]]; $Y \neq \{0\}$). Then
>
> $$
> \begin{aligned}\|M\| = \sup_{\substack{x \in X \\ \|x\| = 1}} \|Mx\| &= \sup_{\substack{x \in X \\ \|x\| = 1}}\ \sup_{\substack{\ell \in Y' \\ \|\ell\| = 1}} |\ell(Mx)| = \sup_{\substack{x \in X \\ \|x\| = 1}}\ \sup_{\substack{\ell \in Y' \\ \|\ell\| = 1}} |(M'\ell)(x)| \\
> &\le \sup_{\substack{x \in X \\ \|x\| = 1}}\ \sup_{\substack{\ell \in Y' \\ \|\ell\| = 1}} \|M'\ell\|\, \|x\| \le \sup_{\substack{\ell \in Y' \\ \|\ell\| = 1}} \|M'\ell\| = \|M'\| ,\end{aligned}
> $$
>
> using $|(M'\ell)(x)| \le \|M'\ell\|\, \|x\|$, as $M'\ell \in X'$, and Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]](a) for $M'$ in the last step.
>
> (2)
> For $\ell \in Y'$ and $x \in X$, $((M + N)'\ell)(x) = \ell((M + N)x) = \ell(Mx + Nx) = \ell(Mx) + \ell(Nx) = (M'\ell)(x) + (N'\ell)(x)$, by linearity of $\ell$. So $(M + N)'\ell = M'\ell + N'\ell$ for every $\ell$. In the same way $(cM)' = c\, M'$ for $c \in \mathbb{F}$, so $M \mapsto M'$ is a linear map $\mathcal{L}(X, Y) \to \mathcal{L}(Y', X')$, and by (1) it preserves norms.

^pf-46-4

*Uses:* [[§30 Boundedness and Continuity#^prop-30-1|§30.1]], [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]]

## Null Spaces and Ranges

The annihilator $Y^\perp \subset X'$ was defined for a linear subspace $Y$ of $X$ (Definition [[§36 Duality in Normed Spaces#^def-36-1|§36.1]]); the same formula, $R^\perp = \{ \ell \in X' : \ell(y) = 0 \text{ for all } y \in R \}$, makes sense for any subset $R \subset X$, and it is stated that way in the lecture. The transpose needs the annihilator on the other side of the pairing as well.

> [!definition] Definition §46.3: Annihilator of a Subset of the Dual
> Let $X$ be a normed linear space and $S \subset X'$. The **annihilator** of $S$ is
>
> $$
> {}^\perp S = \{ x \in X : \ell(x) = \langle x, \ell \rangle = 0 \text{ for all } \ell \in S \} ,
> $$
>
> the set of vectors on which every functional in $S$ vanishes.
>
> *Lax: §15.1, before Thm 5*

^def-46-3

> [!theorem] Lemma §46.5: ${}^\perp S$ is a Closed Subspace
> *(Not from lecture.)* Let $X$ be a normed linear space and $S \subset X'$. Then ${}^\perp S$ is a closed linear subspace of $X$.
>
> *Lax: §15.1, before Thm 5 (``clearly'')*

^lem-46-5

> [!proof]+ Proof
> For each $\ell \in S$, the null space $N(\ell) = \{ x : \ell(x) = 0 \}$ is a linear subspace of $X$, and it is closed: if $x_k \in N(\ell)$ and $x_k \to x$, then $\ell(x) = \lim_k \ell(x_k) = 0$, because $\ell$ is continuous (Proposition [[§30 Boundedness and Continuity#^prop-30-2|§30.2]]). ${}^\perp S = \bigcap_{\ell \in S} N(\ell)$ (and ${}^\perp \varnothing = X$). An intersection of linear subspaces is a linear subspace, and an intersection of closed sets is closed.

^pf-46-5

*Uses:* [[§30 Boundedness and Continuity#^prop-30-2|§30.2]]

In the lecture the null space and range of $M \in \mathcal{L}(X, Y)$ are written $N_M$ and $R_M$; these are $N(M) = \{ x \in X : Mx = 0 \}$ and $R(M) = \{ Mx : x \in X \}$ of Definitions [[§39 Solving Mx = y#^def-39-2|§39.2]] and [[§39 Solving Mx = y#^def-39-1|§39.1]]. The same applies to $M' \in \mathcal{L}(Y', X')$: $N(M') \subset Y'$ and $R(M') \subset X'$.

> [!theorem] Theorem §46.6: Null Spaces and Ranges of $M$ and $M'$
> Let $X, Y$ be normed linear spaces and $M \in \mathcal{L}(X, Y)$, so that $M' \in \mathcal{L}(Y', X')$. Then
>
> 1. $N(M) = {}^\perp R(M')$;
> 2. $N(M') = R(M)^\perp$.
>
> *Lax: §15.1, Thm 5(ii), (iii)*

^thm-46-6

> [!remark]- Connections
> - In finite dimensions: [[§12 Duality#^ladr-3-128|LADR 3.128]] (null space of $T'$) and [[§12 Duality#^ladr-3-130|LADR 3.130]] (range of $T'$); there both ranges are closed and dimension counting gives more.

> [!proof]+ Proof
> Both parts come from the defining identity $\langle Mx, \ell \rangle = \langle x, M'\ell \rangle$, for $x \in X$ and $\ell \in Y'$.
>
> (2) *$N(M') \subset R(M)^\perp$.* Let $\ell \in Y'$ with $M'\ell = 0$. We want $\ell \in R(M)^\perp$, i.e. $\ell(y) = 0$ for every $y = Mx \in R(M)$. But $\ell(Mx) = (M'\ell)(x) = 0$ for all $x \in X$.
>
> *$R(M)^\perp \subset N(M')$.* Let $\ell \in R(M)^\perp$, i.e. $\ell(Mx) = 0$ for all $x \in X$. Then $(M'\ell)(x) = \ell(Mx) = 0$ for all $x \in X$, so $M'\ell$ is the zero functional: $\ell \in N(M')$.
>
> (1)
> *$N(M) \subset {}^\perp R(M')$.* Let $Mx = 0$. Every element of $R(M')$ is $M'\ell$ for some $\ell \in Y'$, and $(M'\ell)(x) = \ell(Mx) = \ell(0) = 0$. So $x \in {}^\perp R(M')$.
>
> *${}^\perp R(M') \subset N(M)$.* Let $x \in {}^\perp R(M')$, i.e. $(M'\ell)(x) = 0$ for all $\ell \in Y'$. Then $\ell(Mx) = (M'\ell)(x) = 0$ for every $\ell \in Y'$, so $Mx = 0$, because bounded linear functionals separate points (Corollary [[§36 Duality in Normed Spaces#^cor-36-3|§36.3]], a consequence of Hahn–Banach). So $x \in N(M)$.

^pf-46-6

*Uses:* [[§36 Duality in Normed Spaces#^cor-36-3|§36.3]]

> [!theorem] Corollary §46.7: The Closure of the Range
> *(Not from lecture.)* Let $X, Y$ be normed linear spaces and $M \in \mathcal{L}(X, Y)$.
>
> 1. $\overline{R(M)} = {}^\perp N(M')$: a vector $y \in Y$ is a limit of vectors $Mx$ if and only if $\ell(y) = 0$ for every $\ell \in Y'$ with $M'\ell = 0$.
> 2. If $R(M)$ is closed, then for $y \in Y$ the equation $Mx = y$ has a solution $x \in X$ if and only if $\ell(y) = 0$ for every $\ell \in N(M')$.

^cor-46-7

> [!proof]+ Proof
> (1) $R(M)$ is a linear subspace of $Y$, so the closure of its linear span is $\overline{R(M)}$. By the spanning criterion (Theorem [[§37 Separable Duals and Reflexive Spaces#^thm-37-1|§37.1]], applied to the family of all vectors of $R(M)$), $z \in \overline{R(M)}$ if and only if every $\ell \in Y'$ that vanishes on $R(M)$ also vanishes at $z$. The functionals vanishing on $R(M)$ form $R(M)^\perp$, which is $N(M')$ by Theorem [[§46 The Transpose#^thm-46-6|§46.6]](2). So $z \in \overline{R(M)}$ if and only if $\ell(z) = 0$ for all $\ell \in N(M')$, that is, $z \in {}^\perp N(M')$.
>
> (2) If $R(M)$ is closed, then $R(M) = \overline{R(M)} = {}^\perp N(M')$ by (1), and $Mx = y$ is solvable exactly when $y \in R(M)$.

^pf-46-7

*Uses:* [[§37 Separable Duals and Reflexive Spaces#^thm-37-1|§37.1]], [[§46 The Transpose#^thm-46-6|§46.6]]

> [!remark] Remark: The Solvability of $Mx = y$
> For a matrix $A$ this is the familiar criterion: $Ax = y$ has a solution if and only if $y$ is orthogonal to every solution $z$ of $A^T z = 0$; the range of a matrix is a finite-dimensional subspace, hence closed (Corollary [[§14 New Normed Spaces from Old#^cor-14-6|§14.6]]). In infinite dimensions only the closure of the range is described by $N(M')$, and the criterion of (2) needs the range to be closed, which is the subject of the closed range criterion (Proposition [[§41 The Open Mapping Theorem and Its Consequences#^prop-41-5|§41.5]]). This answers the question of existence in [[§39 Solving Mx = y|§39]] in terms of the transpose.

^rem-46-4

![[m556-46-3.svg]]

The solvability criterion for $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$, with $(\mathbb{R}^2)'$ identified with $\mathbb{R}^2$ by the dot product. The range $R(A)$ is the line spanned by $(2, 1)$ (blue), and $N(A^T)$ is the line spanned by $z = (1, -2)$ (red), the functionals vanishing on $R(A)$. $Ax = y$ is solvable for $y = (2, 1)$, which is orthogonal to $z$, and not for $\tilde y = (2, 2.4)$, which has $(\tilde y, z) \neq 0$.

## Transposes and Convergence

> [!theorem] Proposition §46.8: Weak Convergence Passes to Transposes
> Let $X, Y$ be normed linear spaces, $A_n \in \mathcal{L}(X, Y)$ for $n = 1, 2, \ldots$, and $A \in \mathcal{L}(X, Y)$.
>
> 1. If $X$ is reflexive (Definition [[§37 Separable Duals and Reflexive Spaces#^def-37-1|§37.1]]) and $\mathop{\text{w-lim}}_{n \to \infty} A_n = A$, then $\mathop{\text{w-lim}}_{n \to \infty} A_n' = A'$ in $\mathcal{L}(Y', X')$.
> 2. *(Not from lecture.)* Conversely, for any normed linear spaces $X$ and $Y$: if $\mathop{\text{w-lim}}_{n \to \infty} A_n' = A'$, then $\mathop{\text{w-lim}}_{n \to \infty} A_n = A$.
>
> *Lax: §15.2, Exercise 6 (part (1), for Banach spaces)*

^prop-46-8

> [!proof]+ Proof
> By Definition [[§45 Convergence of Operators#^def-45-3|§45.3]], applied to maps from $Y'$ to $X'$, $A_n' \rightharpoonup A'$ means: for every $\ell \in Y'$ and every $\eta \in (X')' = X''$, $\eta(A_n'\ell) \to \eta(A'\ell)$. Let $i : X \to X''$, $i(x)(m) = m(x)$, be the canonical embedding (Proposition [[§37 Separable Duals and Reflexive Spaces#^prop-37-5|§37.5]]). For $x \in X$ and $\ell \in Y'$,
>
> $$
> i(x)(A_n'\ell) = (A_n'\ell)(x) = \ell(A_n x) , \qquad i(x)(A'\ell) = \ell(Ax) . \tag{$\ast$}
> $$
>
> (1) Let $\ell \in Y'$ and $\eta \in X''$. Since $X$ is reflexive, $\eta = i(x)$ for some $x \in X$. By ($\ast$) and the weak convergence $A_n \rightharpoonup A$, $\eta(A_n'\ell) = \ell(A_n x) \to \ell(Ax) = \eta(A'\ell)$.
>
> (2) Let $x \in X$ and $\ell \in Y'$. The hypothesis, tested with $\eta = i(x) \in X''$, gives $i(x)(A_n'\ell) \to i(x)(A'\ell)$, that is, $\ell(A_n x) \to \ell(Ax)$ by ($\ast$). So $A_n \rightharpoonup A$. Reflexivity is not used: the elements $i(x)$ are always in $X''$; it is needed in (1) only to know that every $\eta \in X''$ is of this form.

^pf-46-8

*Uses:* [[§45 Convergence of Operators#^def-45-3|Def. §45.3]], [[§37 Separable Duals and Reflexive Spaces#^prop-37-5|§37.5]]

> [!example] Example §46.2: Strong Convergence Does Not Pass to Transposes
> Let $X = Y = \ell^2$, which is reflexive (Example [[§37 Separable Duals and Reflexive Spaces#^ex-37-3|§37.3]]), and
>
> $$
> A_n a = (a_n, 0, 0, \ldots) , \qquad a = (a_1, a_2, \ldots) \in \ell^2 ,
> $$
>
> the map that moves the $n$-th entry to the first place and deletes the rest. With $(\ell^2)'$ identified with $\ell^2$, $\ell_b(u) = (u, b) = \sum_j u_j\, \overline{b_j}$ (Example [[§31 Dual Spaces#^ex-31-1|§31.1]]):
>
> 1. $A_n \to 0$ strongly;
> 2. $A_n' \ell_b = \ell_{b_1 e_n}$, where $e_n = (0, \ldots, 0, 1, 0, \ldots)$ has its $1$ in the $n$-th place; for $b_1 \neq 0$ the sequence $\{A_n' \ell_b\}$ does not converge, so $A_n'$ does not converge strongly;
> 3. $A_n' \rightharpoonup 0$ weakly.
>
> *Lax: §15.2, the example after the definitions of strong and weak convergence*

^ex-46-2

> [!proof]+ Proof
> $A_n$ is linear, and $\|A_n a\|_{\ell^2} = |a_n| \le \|a\|_{\ell^2}$, so $A_n \in \mathcal{L}(\ell^2, \ell^2)$.
>
> (1) $\|A_n a - 0\|_{\ell^2} = |a_n| \to 0$ as $n \to \infty$ for every $a \in \ell^2$, since the terms of the convergent series $\sum_j |a_j|^2$ tend to $0$.
>
> (2) For $a, b \in \ell^2$, $(A_n' \ell_b)(a) = \ell_b(A_n a) = (A_n a, b) = a_n\, \overline{b_1} = (a, b_1 e_n) = \ell_{b_1 e_n}(a)$. So $A_n' \ell_b = \ell_{b_1 e_n}$. The map $c \mapsto \ell_c$ preserves norms (Theorem [[§31 Dual Spaces#^thm-31-2|§31.2]]) and $\ell_c - \ell_d = \ell_{c - d}$, so for $n \neq m$
>
> $$
> \|A_n' \ell_b - A_m' \ell_b\| = \|b_1 e_n - b_1 e_m\|_{\ell^2} = \|(0, \ldots, b_1, \ldots, -b_1, \ldots, 0)\|_{\ell^2} = \sqrt{2\, |b_1|^2} = \sqrt{2}\, |b_1| .
> $$
>
> For $b_1 \neq 0$ the sequence $\{A_n' \ell_b\}$ is not Cauchy, hence does not converge in $(\ell^2)'$. So $A_n'$ does not converge strongly (Definition [[§45 Convergence of Operators#^def-45-2|§45.2]]), to $0 = (0)'$ or to anything else.
>
> (3) $A_n \to 0$ strongly, hence weakly (Proposition [[§45 Convergence of Operators#^prop-45-1|§45.1]](2)), and $\ell^2$ is reflexive; by Proposition [[§46 The Transpose#^prop-46-8|§46.8]](1), $A_n' \rightharpoonup 0' = 0$.

^pf-ex-46-2

*Uses:* [[§31 Dual Spaces#^thm-31-2|§31.2]], [[§45 Convergence of Operators#^def-45-2|Def. §45.2]], [[§45 Convergence of Operators#^prop-45-1|§45.1]], [[§46 The Transpose#^prop-46-8|§46.8]]

The same maps show once more that strong convergence does not imply uniform convergence: $\|A_n\| = 1$ for every $n$, since $\|A_n a\| \le \|a\|$ and $A_n e_n = e_1$ (compare Example [[§45 Convergence of Operators#^ex-45-1|§45.1]]). The transpose $A_n'$, read through the identification, sends $b$ to $b_1 e_n$: it moves the first entry out to the $n$-th place, and a vector running off to infinity converges weakly but not strongly, as $e_n$ does.

![[m556-46-a1.gif|460]]

*(Not from lecture; animation added, vault only.)* The maps of Example [[§46 The Transpose#^ex-46-2|§46.2]] for $n = 1, \ldots, 18$. Top: $A_n a = (a_n, 0, 0, \ldots)$ (blue) for $a_i = 0.85^{\,i-1}$ (grey); the single entry shrinks. Bottom: $A_n' b = b_1 e_n$ (red), with $b_1 = 0.75$, moving out to the $n$-th place over a fixed $c \in \ell^2$ (grey). Right: $\|A_n a\| \to 0$; $\|A_n' b\| = |b_1|$ and consecutive terms stay $\sqrt2\,|b_1|$ apart, so there is no strong limit; $|(A_n' b, c)| = |b_1 c_n| \to 0$.

## Composition

> [!definition] Definition §46.4: Composition
> Let $X, Y, Z$ be normed linear spaces, $M \in \mathcal{L}(X, Y)$ and $N \in \mathcal{L}(Y, Z)$. The **composition** (or product) of $N$ and $M$ is the map $NM : X \to Z$, $NM(x) = N(M(x))$.
>
> *Lax: §15.4*

^def-46-4

> [!theorem] Proposition §46.9: Composition and Transpose
> Let $X, Y, Z$ be normed linear spaces, $M \in \mathcal{L}(X, Y)$ and $N \in \mathcal{L}(Y, Z)$.
>
> 1. $NM \in \mathcal{L}(X, Z)$, and $\|NM\| \le \|N\|\, \|M\|$.
> 2. $(NM)' = M'N'$.
>
> *Lax: §15.4, Thm 8*

^prop-46-9

> [!proof]+ Proof
> (1)
> $NM$ is linear, as a composition of linear maps. By Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]](b), applied to $N$ and then to $M$,
>
> $$
> \|NMx\| \le \|N\|\, \|Mx\| \le \|N\|\, \|M\|\, \|x\| \qquad \text{for all } x \in X ,
> $$
>
> so $NM$ is bounded with $\|NM\| \le \|N\|\, \|M\|$ (Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]](c)). Proposition [[§46 The Transpose#^prop-46-1|§46.1]] is the case $Z = \mathbb{F}$, $N = \ell$.
>
> (2) Both sides are maps from $Z'$ to $X'$. Let $x \in X$ and $\ell \in Z'$. Using the defining identity of the transpose three times, for $NM$, for $N$ and for $M$,
>
> $$
> ((NM)'\ell)(x) = \langle x, (NM)'\ell \rangle = \langle (NM)(x), \ell \rangle = \langle N(Mx), \ell \rangle = \langle Mx, N'\ell \rangle = \langle x, M'N'\ell \rangle .
> $$
>
> Since this holds for all $x \in X$, $(NM)'\ell = M'(N'\ell)$; since it holds for all $\ell \in Z'$, $(NM)' = M'N'$. The order is reversed, as for matrices: $(BA)^T = A^T B^T$.

^pf-46-9

*Uses:* [[§30 Boundedness and Continuity#^prop-30-1|§30.1]], [[§46 The Transpose#^prop-46-1|§46.1]]

> [!remark]- Connections
> - In finite dimensions: [[§12 Duality#^ladr-3-120|LADR 3.120]](c).

