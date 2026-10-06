---
type: section
subject: "[[Measure Theory]]"
chapter: 4
section: 23
tags: [measure-theory, math551]
---
← [[§22 The General Lebesgue Integral]] · ↑ [[· 4 Integration Theory]] · [[§24 The L¹ Space and Density Theorems]] →

## Dominated Fatou's Lemma and Reverse Fatou

The standard [[Fatou's Lemma|Fatou's lemma]] ([[§20 The Lebesgue Integral for Simple Functions|§20]]) requires $f_k \geq 0$. Under a domination hypothesis, we can extend it to signed functions and also obtain the reverse inequality for $\limsup$.

> [!theorem] Theorem §23.1: Dominated Fatou's Lemma
> Let $\{f_k\}$ be a sequence of measurable functions on $E \in \mathcal{M}$. Suppose there exists $F \in L(E)$ with $F \geq 0$ such that $|f_k(x)| \leq F(x)$ a.e. on $E$ for all $k$. Then:
>
> $$
> \int_E \liminf_{k \to \infty} f_k\,dx \leq \liminf_{k \to \infty} \int_E f_k\,dx.
> $$

^thm-23-1

> [!proof]+ Proof
> Define $h_k = f_k + F$. Since $f_k \geq -|f_k| \geq -F$, we have $h_k \geq 0$. Each $h_k$ is measurable. By the [[Fatou's Lemma|standard Fatou's lemma]] applied to $\{h_k\}$:
>
> $$
> \int_E \liminf_{k \to \infty} (f_k + F)\,dx \leq \liminf_{k \to \infty} \int_E (f_k + F)\,dx.
> $$
>
> The left side equals $\int_E \liminf f_k\,dx + \int_E F\,dx$ (since $F$ does not depend on $k$). The right side equals $\liminf \int_E f_k\,dx + \int_E F\,dx$ (since $\int_E F\,dx$ is a constant). Since $\int_E F\,dx < \infty$, cancel it from both sides.

^pf-23-1

*Uses:* [[§15 Measurable Functions#^thm-15-3|§15.3]], [[Fatou's Lemma|§21.8]], [[§22 The General Lebesgue Integral#^thm-22-2|§22.2]], [[§22 The General Lebesgue Integral#^prop-22-1|§22.1]]

> [!theorem] Theorem §23.2: Reverse Fatou's Lemma
> Under the same hypotheses as above:
>
> $$
> \limsup_{k \to \infty} \int_E f_k\,dx \leq \int_E \limsup_{k \to \infty} f_k\,dx.
> $$

^thm-23-2

> [!proof]+ Proof
> **Step 1: $\int_E \limsup_{k \to \infty} f_k\,dx = \lim_{l \to \infty} \int_E g_l\,dx$.**
>
> Define $g_l(x) = \sup_{k \geq l} f_k(x)$, so that $\limsup_{k \to \infty} f_k(x) = \lim_{l \to \infty} g_l(x)$. Note that $g_l \geq g_{l+1}$ (the supremum is taken over fewer terms as $l$ increases).
>
> Decompose $g_l = g_l^+ - g_l^-$.
>
> *$g_l^+$ is decreasing*: If $g_l(x) \geq 0 > g_{l+1}(x)$, then $g_l^+(x) = g_l(x) \geq 0 = g_{l+1}^+(x)$. If $g_l(x) \geq g_{l+1}(x) \geq 0$, then $g_l^+(x) = g_l(x) \geq g_{l+1}(x) = g_{l+1}^+(x)$. If $0 \geq g_l(x) \geq g_{l+1}(x)$, then $g_l^+(x) = 0 = g_{l+1}^+(x)$. In all cases, $g_l^+ \geq g_{l+1}^+$.
>
> *$g_l^-$ is increasing*: By a similar case analysis, $g_l^- \leq g_{l+1}^-$.
>
> Since $|g_l(x)| = |\sup_{k \geq l} f_k(x)| \leq \sup_{k \geq l} |f_k(x)| \leq F(x)$, we have $g_l^+(x) \leq F(x)$, so $\int_E g_l^+\,dx \leq \int_E F\,dx < \infty$. By the [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-7|MCT for decreasing sequences]] (applicable since $g_l^+$ is decreasing with $\int_E g_1^+ < \infty$):
>
> $$
> \lim_{l \to \infty} \int_E g_l^+\,dx = \int_E \lim_{l \to \infty} g_l^+\,dx.
> $$
>
> By the [[Monotone Convergence Theorem (Lebesgue)|MCT for increasing sequences]] (applied to $g_l^-$):
>
> $$
> \lim_{l \to \infty} \int_E g_l^-\,dx = \int_E \lim_{l \to \infty} g_l^-\,dx.
> $$
>
> By [[§22 The General Lebesgue Integral#^thm-22-2|linearity]] (all integrals are finite):
>
> $$
> \lim_{l \to \infty} \int_E g_l\,dx = \lim_{l \to \infty} \int_E g_l^+\,dx - \lim_{l \to \infty} \int_E g_l^-\,dx = \int_E \lim_{l \to \infty} g_l^+\,dx - \int_E \lim_{l \to \infty} g_l^-\,dx = \int_E \lim_{l \to \infty} g_l\,dx = \int_E \limsup_{k \to \infty} f_k\,dx.
> $$
>
> **Step 2: $\limsup_{k \to \infty} \int_E f_k\,dx \leq \lim_{l \to \infty} \int_E g_l\,dx$.**
>
> Since $g_l(x) = \sup_{k \geq l} f_k(x) \geq f_k(x)$ for all $k \geq l$, by monotonicity $\int_E f_k\,dx \leq \int_E g_l\,dx$ for all $k \geq l$. Taking the supremum over $k \geq l$:
>
> $$
> \sup_{k \geq l} \int_E f_k\,dx \leq \int_E g_l\,dx.
> $$
>
> Taking $l \to \infty$:
>
> $$
> \limsup_{k \to \infty} \int_E f_k\,dx = \lim_{l \to \infty} \sup_{k \geq l} \int_E f_k\,dx \leq \lim_{l \to \infty} \int_E g_l\,dx = \int_E \limsup_{k \to \infty} f_k\,dx.
> $$

^pf-23-2

*Uses:* [[§16 Limits and Positive Parts of Measurable Functions#^thm-16-1|§16.1]], [[§16 Limits and Positive Parts of Measurable Functions#^rem-16-4|Rem. §12.4]], [[§16 Limits and Positive Parts of Measurable Functions#^def-16-1|Def. §16.1]], [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-7|§21.7]], [[Monotone Convergence Theorem (Lebesgue)|§20.7]], [[§22 The General Lebesgue Integral#^thm-22-2|§22.2]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[§10 Monotone Sequences and Cauchy Sequences#^def-10-3|451 Def. §10.3]]

## The Dominated Convergence Theorem

> [!theorem] Theorem §23.3: Dominated Convergence Theorem (DCT)
> Let $\{f_k\}$ be a sequence of measurable functions on $E \in \mathcal{M}$. Suppose:
> - (i) $f_k(x) \to f(x)$ a.e. on $E$,
> - (ii) there exists $F \in L(E)$, $F \geq 0$, such that $|f_k(x)| \leq F(x)$ a.e. on $E$ for all $k$.
>
> Then $f \in L(E)$ and:
>
> $$
> \lim_{k \to \infty} \int_E f_k(x)\,dx = \int_E f(x)\,dx.
> $$

^thm-23-3

> [!proof]+ Proof
> Since $|f_k| \leq F$ a.e. and $f_k \to f$ a.e., we have $|f| \leq F$ a.e., so $f \in L(E)$.
>
> By the [[§23 The Dominated Convergence Theorem#^thm-23-1|dominated Fatou's lemma]] and [[§23 The Dominated Convergence Theorem#^thm-23-2|reverse Fatou's lemma]]:
>
> $$
> \int_E \liminf_{k \to \infty} f_k\,dx \;\leq\; \liminf_{k \to \infty} \int_E f_k\,dx \;\leq\; \limsup_{k \to \infty} \int_E f_k\,dx \;\leq\; \int_E \limsup_{k \to \infty} f_k\,dx.
> $$
>
> Since $f_k \to f$ a.e., $\liminf f_k = \limsup f_k = f$ a.e., so both the leftmost and rightmost terms equal $\int_E f\,dx$. By the [[Squeeze Theorem|squeeze]]:
>
> $$
> \lim_{k \to \infty} \int_E f_k\,dx = \int_E f\,dx.
> $$

^pf-23-3

*Uses:* [[§22 The General Lebesgue Integral#^prop-22-1|§22.1]], [[§23 The Dominated Convergence Theorem#^thm-23-1|§23.1]], [[§23 The Dominated Convergence Theorem#^thm-23-2|§23.2]], [[§17 Simple Functions and Modes of Convergence#^rem-17-7|Rem. §12.7]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-6|451 §10.6]], [[Squeeze Theorem|451 §8.1]]

> [!remark]- Connections
> - MATH 451 exchanges limit and integral only under uniform convergence: [[§25 More on Uniform Convergence#^thm-25-1|451 §25.1]], [[§33 Properties of the Riemann Integral#^thm-33-12|451 §33.12]]. On $[a,b]$, a uniformly convergent sequence of bounded functions is dominated by a constant, so the DCT contains these.
> - The $L^p$ theory ([[§34 Normed Linear Spaces and Lᵖ Spaces|§34]]) leans on the DCT throughout. [[Fubini's Theorem (Lebesgue)|Fubini's Theorem]] ([[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|§25.6]]) does not: it applies [[Tonelli's Theorem]] to $f^+$ and $f^-$ and subtracts.
> - Used in PDEs: differentiation under the integral sign, which shows that the Fourier-integral solution of the semi-infinite rod satisfies the heat equation, [[§32 Semi-Infinite Rod#^thm-32-2|341 Thm. §32.2]], and passes $\partial/\partial x$ through the Laplace transform, [[§66★ Partial Differential Equations#^thm-66-1|341 Thm. §66.1]].
> - Used in Quantum Field Theory: differentiation under the integral sign with a dominating function independent of the parameter, the check behind every exchange of limit, derivative and integral in the field calculations — [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|QFT Theorem §CA.1.1]].

> [!proof]+ Alternative Proof of DCT via Fatou
> Since $|f_k(x) - f(x)| \leq |f_k(x)| + |f(x)| \leq 2g(x)$ a.e. (where $g = F$), define $h_k(x) = 2g(x) - |f_k(x) - f(x)|$. Then $h_k \geq 0$ a.e. and $h_k$ is measurable.
>
> Since $f_k \to f$ a.e., we have $|f_k - f| \to 0$ a.e., so $\liminf_{k \to \infty} h_k(x) = 2g(x)$ a.e. By [[Fatou's Lemma|Fatou's lemma]]:
>
> $$
> \int_E 2g\,dx = \int_E \liminf_{k \to \infty} h_k\,dx \leq \liminf_{k \to \infty} \int_E h_k\,dx = \liminf_{k \to \infty} \left(2\int_E g\,dx - \int_E |f_k - f|\,dx\right).
> $$
>
> Since $\int_E g\,dx < \infty$:
>
> $$
> 2\int_E g\,dx \leq 2\int_E g\,dx - \limsup_{k \to \infty} \int_E |f_k - f|\,dx,
> $$
>
> which gives $\limsup_{k \to \infty} \int_E |f_k - f|\,dx \leq 0$. Since $\int_E |f_k - f|\,dx \geq 0$ for all $k$:
>
> $$
> \lim_{k \to \infty} \int_E |f_k - f|\,dx = 0.
> $$
>
> The conclusion $\lim \int_E f_k\,dx = \int_E f\,dx$ then follows from:
>
> $$
> \left|\int_E f_k\,dx - \int_E f\,dx\right| = \left|\int_E (f_k - f)\,dx\right| \leq \int_E |f_k - f|\,dx \to 0.
> $$

^pf-23-3-2

*Uses:* [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]], [[Fatou's Lemma|§21.8]], [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-2|§21.2]], [[§22 The General Lebesgue Integral#^thm-22-2|§22.2]], [[§22 The General Lebesgue Integral#^prop-22-1|§22.1]]

> [!remark] Remark: $L^1$ Convergence
> The alternative proof actually establishes a stronger conclusion: under the hypotheses of DCT, $\lim_{k \to \infty} \int_E |f_k - f|\,dx = 0$, i.e., $f_k \to f$ in $L^1(E)$ ([[§24 The L¹ Space and Density Theorems#^def-24-4|Def. §24.4]]). This is strictly stronger than $\lim \int f_k = \int f$, which is convergence of the integrals.

^rem-23-4

> [!remark]- Connections
> - This $L^1$ form of the DCT drives the density theorems [[§24 The L¹ Space and Density Theorems#^thm-24-5|§24.5]] and [[§24 The L¹ Space and Density Theorems#^lem-24-1|§24.1]]; its $L^p$ analogue is used in [[§35 Lᵖ as a Banach Space#^thm-35-12|§35.12]].

> [!remark] Remark: Comparison of Convergence Theorems
> The three main convergence theorems each trade hypotheses for generality:
>
> | **Theorem** | **Hypotheses** | **Conclusion** |
> |---|---|---|
> | [[Monotone Convergence Theorem (Lebesgue)\|MCT]] | $0 \leq f_k \nearrow f$ | $\lim \int f_k = \int f$ |
> | [[Fatou's Lemma\|Fatou]] | $f_k \geq 0$ | $\int \liminf f_k \leq \liminf \int f_k$ |
> | [[Dominated Convergence Theorem\|DCT]] | $\vert f_k\vert \leq F \in L$, $f_k \to f$ a.e. | $\lim \int f_k = \int f$ |
>
> The MCT requires monotonicity but no domination. The DCT requires domination but no monotonicity. Fatou is the weakest conclusion but requires the least: only non-negativity (or [[§23 The Dominated Convergence Theorem#^thm-23-1|domination for signed functions]]).

^rem-23-3

![[m551-15-2.svg]]
*Why the DCT needs an integrable dominator. Both sequences tend to $0$ at every point while $\int f_k = 1$ for every $k$, so $\lim \int f_k \neq \int \lim f_k$. (a) The sliding block $f_k = \chi_{[k,k+1]}$ of [[§18 Egorov's and Lusin's Theorems#^rem-18-1|Rem. §13.1]]: the smallest possible dominator $\sup_k f_k = \chi_{[1,\infty)}$ (red) has infinite integral. (b) The bumps $f_k = k\,\chi_{(0,1/k)}$ of [[§21 Consequences of the Monotone Convergence Theorem#^ex-21-1|Ex. §21.1]]: $\sup_k f_k$ is the red staircase, equal to $k$ on $[\frac{1}{k+1}, \frac1k)$, which is at least $\frac1x - 1$ and not integrable near $0$. Any $F$ with $|f_k| \leq F$ lies above the red graph, so no $F \in L$ exists; only Fatou's inequality survives, and it is strict.*

> [!remark]- Connections
> - The MATH 451 row this table replaces: $f_n \to f$ uniformly on $[a,b]$ gives $\lim \int f_n = \int f$ ([[§33 Properties of the Riemann Integral#^thm-33-12|451 §33.12]]; [[§24 Uniform Convergence#^def-24-2|451 Def. §24.2]], [[§17 Simple Functions and Modes of Convergence#^def-17-5|Def. §17.5]]).
> - Why a new integral was needed for such theorems: [[§8 Motivation꞉ The Riemann Integral#^rem-8-2|Rem. §8.2]] (Riemann integrable functions are not closed under pointwise limits).

## Absolute Convergence of Series in $L^1$

> [!theorem] Corollary §23.4: Absolute Convergence in $L^1$
> Let $f_k \in L(E)$ for all $k$, and assume $\sum_{k=1}^{\infty} \int_E |f_k(x)|\,dx < \infty$. Then:
> - (i) $\sum_{k=1}^{\infty} f_k(x)$ converges absolutely for a.e. $x \in E$.
> - (ii) Defining $S(x) = \sum_{k=1}^{\infty} f_k(x)$, we have $S \in L(E)$ and:
>
> $$
> \int_E \sum_{k=1}^{\infty} f_k(x)\,dx = \sum_{k=1}^{\infty} \int_E f_k(x)\,dx.
> $$

^cor-23-4

> [!proof]+ Proof
> Since $|f_k| \in L(E)$ is non-negative measurable, by [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-5|MCT II]]:
>
> $$
> \sum_{k=1}^{\infty} \int_E |f_k|\,dx = \int_E \sum_{k=1}^{\infty} |f_k(x)|\,dx < \infty.
> $$
>
> Therefore $\sum_{k=1}^{\infty} |f_k(x)| < \infty$ a.e. on $E$ ([[§21 Consequences of the Monotone Convergence Theorem#^prop-21-3|integrable non-negative function is a.e. finite]]). This means $\sum f_k(x)$ converges absolutely a.e.
>
> Let $S_m(x) = \sum_{k=1}^{m} f_k(x)$ and $S(x) = \lim_{m \to \infty} S_m(x)$ (defined a.e.). Define $g(x) = \sum_{k=1}^{\infty} |f_k(x)| \in L(E)$. Then $|S_m(x)| \leq \sum_{k=1}^{m} |f_k(x)| \leq g(x)$ for all $x \in E$. Since $S_m \to S$ a.e. and $|S_m| \leq g \in L(E)$, by [[Dominated Convergence Theorem|DCT]]:
>
> $$
> \int_E S\,dx = \lim_{m \to \infty} \int_E S_m\,dx = \lim_{m \to \infty} \sum_{k=1}^{m} \int_E f_k\,dx = \sum_{k=1}^{\infty} \int_E f_k\,dx.
> $$

^pf-23-4

*Uses:* [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-5|§21.5]], [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-3|§21.3]], [[§14 Series#^prop-14-6|451 §14.6]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]], [[Dominated Convergence Theorem|§23.3]], [[§22 The General Lebesgue Integral#^thm-22-2|§22.2]]

> [!remark]- Connections
> - MATH 451 analogue: the [[§25 More on Uniform Convergence#^thm-25-3|Weierstrass M-test]] (451 §25.3) gives term-by-term integration from $\sum \sup |f_k| < \infty$; here $\sum \int |f_k| < \infty$ suffices.
> - $L^p$ version: [[§35 Lᵖ as a Banach Space#^cor-35-7|Corollary §35.7]]; the key step in [[Riesz–Fischer Theorem|Riesz–Fischer]] ([[§35 Lᵖ as a Banach Space#^thm-35-11|§35.11]]).

## Riemann Integrable Functions are Lebesgue Integrable

> [!definition] Definition §23.1: Step Functions
> A function $h: [a,b] \to \mathbb{R}$ is called a **step function** if $h(x) = \sum_{j=1}^{m} a_j\,\chi_{R_j}(x)$ where the $R_j$ are [[§10 Lebesgue Outer Measure#^def-10-1|rectangles]] (intervals) in $[a,b]$.

^def-23-1

> [!remark]- Connections
> - MATH 451 example: [[§32 The Definition of the Riemann Integral#^ex-32-2|451 Ex. §32.2]]. Step functions are dense in $L^1$: [[§24 The L¹ Space and Density Theorems#^thm-24-6|Theorem §24.6]].

> [!remark] Remark: Riemann Integrability via Step Functions
> Let $p = \{x_0 = a < x_1 < \cdots < x_l = b\}$ be a [[§8 Motivation꞉ The Riemann Integral#^def-8-1|partition]] of $[a,b]$. Define the upper and lower sums:
>
> $$
> U(f, p, [a,b]) = \sum_{j=0}^{l-1} M_j(x_{j+1} - x_j), \quad L(f, p, [a,b]) = \sum_{j=0}^{l-1} m_j(x_{j+1} - x_j),
> $$
>
> where $M_j = \sup_{x \in [x_j, x_{j+1}]} f(x)$ and $m_j = \inf_{x \in [x_j, x_{j+1}]} f(x)$. Then $f \in R[a,b]$ iff:
>
> $$
> \lim_{|p| \to 0} U(f, p, [a,b]) = \lim_{|p| \to 0} L(f, p, [a,b]) = \int_{[a,b]}^R f(x)\,dx.
> $$

^rem-23-6

> [!remark]- Connections
> - This is the 551 definition [[§8 Motivation꞉ The Riemann Integral#^def-8-3|Def. §8.3]]; in MATH 451 the Darboux sums are [[§32 The Definition of the Riemann Integral#^def-32-3|451 Def. §32.3]] and the mesh form of the criterion is [[§32 The Definition of the Riemann Integral#^thm-32-6|451 §32.6]].

> [!theorem] Theorem §23.5: Riemann Integrability Implies Lebesgue Integrability
> Let $f$ be [[§8 Motivation꞉ The Riemann Integral#^def-8-3|Riemann integrable]] on $[a, b]$. Then $f$ is Lebesgue integrable on $[a, b]$ and:
>
> $$
> \int_{[a,b]}^R f(x)\,dx = \int_{[a,b]}^L f(x)\,dx.
> $$

^thm-23-5

> [!proof]+ Proof of Theorem
> WLOG assume $[a, b] = [0, 1]$. For each $k \in \mathbb{N}$, consider the dyadic partition $x_j^{(k)} = j/2^k$ for $j = 0, 1, \ldots, 2^k$. Define the upper and lower step functions:
>
> $$
> \psi_k(x) = \sum_{j=0}^{2^k - 1} M_j\,\chi_{[x_j^{(k)}, x_{j+1}^{(k)})}(x), \qquad \varphi_k(x) = \sum_{j=0}^{2^k - 1} m_j\,\chi_{[x_j^{(k)}, x_{j+1}^{(k)})}(x),
> $$
>
> where $M_j = \sup_{[x_j^{(k)}, x_{j+1}^{(k)}]} f$ and $m_j = \inf_{[x_j^{(k)}, x_{j+1}^{(k)}]} f$.
>
> These satisfy $\varphi_k(x) \leq f(x) \leq \psi_k(x)$ for all $x \in [0,1]$ and all $k$, except possibly at $x = 1$ (which lies in none of the half-open intervals, so $\varphi_k(1) = \psi_k(1) = 0$; a single point is a null set, so this is harmless). As $k$ increases (finer partitions), $\psi_k$ decreases and $\varphi_k$ increases:
>
> $$
> \varphi_k \leq \varphi_{k+1} \leq f \leq \psi_{k+1} \leq \psi_k.
> $$
>
> Since $\{\varphi_k\}$ is increasing and bounded above by $f$, and $\{\psi_k\}$ is decreasing and bounded below by $f$, the pointwise limits exist:
>
> $$
> \varphi(x) = \lim_{k \to \infty} \varphi_k(x), \qquad \psi(x) = \lim_{k \to \infty} \psi_k(x),
> $$
>
> with $\varphi(x) \leq f(x) \leq \psi(x)$ for all $x \in [0,1)$.
>
> Since $f$ is Riemann integrable:
>
> $$
> \lim_{k \to \infty} \int_0^1 \psi_k\,dx = \lim_{k \to \infty} \int_0^1 \varphi_k\,dx = \int_{[0,1]}^R f\,dx.
> $$
>
> Now $\psi_k - \varphi_k \geq 0$ and $\psi_k - \varphi_k \searrow \psi - \varphi \geq 0$. Since $\int_0^1 (\psi_1 - \varphi_1)\,dx < \infty$ (both are bounded), by the [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-7|decreasing version of the MCT]] applied to the difference:
>
> $$
> \int_0^1 (\psi - \varphi)\,dx = \lim_{k \to \infty} \int_0^1 (\psi_k - \varphi_k)\,dx = 0.
> $$
>
> Since $\psi - \varphi \geq 0$ and $\int_0^1 (\psi - \varphi)\,dx = 0$, the [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|vanishing integral result]] gives $\psi(x) = \varphi(x)$ a.e. on $[0,1]$.
>
> Since $\varphi(x) \leq f(x) \leq \psi(x)$ and $\varphi = \psi$ a.e., we have $f(x) = \varphi(x) = \psi(x)$ a.e. In particular, $f(x) = \lim_{k \to \infty} \varphi_k(x)$ a.e., and $f$ is measurable, since it equals the measurable function $\varphi$ (a pointwise limit of simple functions) a.e. ([[§16 Limits and Positive Parts of Measurable Functions#^prop-16-7|Prop. §16.7]]).
>
> Since $|\varphi_k(x)| \leq M$ for all $k$ (where $M = \sup_{[0,1]} |f|$) and $m([0,1]) < \infty$, the constant function $M$ dominates. By [[Dominated Convergence Theorem|DCT]]:
>
> $$
> \int_{[0,1]}^L f\,dx = \lim_{k \to \infty} \int_0^1 \varphi_k\,dx = \int_{[0,1]}^R f\,dx.
> $$

^pf-23-5

*Uses:* [[§8 Motivation꞉ The Riemann Integral#^def-8-3|Def. §8.3]], [[§23 The Dominated Convergence Theorem#^rem-23-6|Rem. §15.6]], [[§23 The Dominated Convergence Theorem#^def-23-1|Def. §23.1]], [[§20 The Lebesgue Integral for Simple Functions#^def-20-1|Def. §20.1]], [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-7|§21.7]], [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|§21.4]], [[§16 Limits and Positive Parts of Measurable Functions#^prop-16-7|§16.7]], [[§22 The General Lebesgue Integral#^ex-22-1|Ex. §22.1]], [[Dominated Convergence Theorem|§23.3]], [[§32 The Definition of the Riemann Integral#^lem-32-1|451 §32.1]]

![[m551-15-3.svg]]
*The proof with $k = 3$ (dyadic intervals of length $\frac18$): the lower step function $\varphi_k$ (blue, the infimum on each interval) and the upper step function $\psi_k$ (red, the supremum) trap $f$. The gray area is $\int_0^1 (\psi_k - \varphi_k)$, the gap between the upper and lower sums; Riemann integrability makes it tend to $0$, which forces $\varphi = \psi = f$ a.e., and the DCT with the constant dominator $M$ then gives $\int^L f = \lim \int \varphi_k = \int^R f$.*

> [!remark] Remark
> Recall that Riemann integrability on $[a,b]$ requires $f$ to be bounded: the [[§8 Motivation꞉ The Riemann Integral#^def-8-2|upper and lower sums]] use $M_j = \sup_{[x_j, x_{j+1}]} f$ and $m_j = \inf_{[x_j, x_{j+1}]} f$, which must be finite. Thus $|f| \leq M$ on $[a,b]$ is automatic, not an additional hypothesis. This boundedness is used in the proof to provide a dominator for DCT.

^rem-23-5

> [!remark]- Connections
> - The converse fails: the Dirichlet function ([[§8 Motivation꞉ The Riemann Integral#^ex-8-2|Ex. §8.2]], [[§32 The Definition of the Riemann Integral#^ex-32-3|451 Ex. §32.3]]) is not Riemann integrable but equals $0$ a.e., so its Lebesgue integral is $0$ ([[§22 The General Lebesgue Integral#^prop-22-1|§22.1]](ii)).
> - Multivariable Riemann integral on rectangles: [[§21 The Definition of the Integral#^def-21-6|452 Def. §21.6]]; its Jordan-content framework ([[§20 Multivariable Integration#^def-20-7|452 Def. §20.7]]) is superseded by Lebesgue measure.
> - Stewart's definite integral (Riemann sums): [[§39 The Definite Integral#^def-39-1|Calc Def. §39.1]] (with worked examples).
