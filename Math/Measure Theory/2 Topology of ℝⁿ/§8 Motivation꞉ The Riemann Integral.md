---
type: section
subject: "[[Measure Theory]]"
chapter: 2
section: 8
tags: [measure-theory, math551]
---
← [[§7 Structure of Open Sets]] · ↑ [[· 2 Topology of ℝⁿ]] · [[§9 Lebesgue Outer Measure]] →

We now begin the transition to measure theory. We start by reviewing the Riemann integral (MATH 451 [[§32 The Definition of the Riemann Integral|§32]]–[[§34 Fundamental Theorem of Calculus|§34]]) and understanding its limitations.

## Definition of the Riemann Integral

> [!definition] Definition §8.1: Partition
> A **partition** of an interval $[a, b]$ is a finite set
>
> $$
> P = \{x_0 = a < x_1 < x_2 < \cdots < x_n = b\}.
> $$
>
> The **mesh** or **norm** of $P$ is $|P| = \sup_{0 \leq j \leq n-1} (x_{j+1} - x_j)$.

^def-8-1

> [!remark]- Connections
> - MATH 451: [[§32 The Definition of the Riemann Integral#^def-32-1|Partitions (451 Def. §32.1)]] and [[§32 The Definition of the Riemann Integral#^def-32-3|Mesh (451 Def. §32.3)]].

> [!definition] Definition §8.2: Upper and Lower Sums
> Let $f: [a, b] \to \mathbb{R}$ be a bounded function and $P = \{x_0, x_1, \ldots, x_n\}$ a partition of $[a, b]$. Define:
>
> $$
> m_j = \inf\{f(x) \mid x \in [x_j, x_{j+1}]\}, \quad M_j = \sup\{f(x) \mid x \in [x_j, x_{j+1}]\}.
> $$
>
> The **lower Riemann sum** is:
>
> $$
> L(f, P) = \sum_{j=0}^{n-1} m_j (x_{j+1} - x_j).
> $$
>
> The **upper Riemann sum** is:
>
> $$
> U(f, P) = \sum_{j=0}^{n-1} M_j (x_{j+1} - x_j).
> $$

^def-8-2

![[m551-8-1.svg]]
*Lower and upper sums for a partition $P = \{x_0, \ldots, x_4\}$: on each $[x_j, x_{j+1}]$ the blue rectangle has height $m_j$ and the full rectangle height $M_j$ (marked for $j = 2$). $L(f,P)$ is the blue area and $U(f,P)$ the blue plus red area; for continuous $f$ the red strips thin out as $|P| \to 0$ (Proposition §8.1).*

> [!remark]- Connections
> - MATH 451: [[§32 The Definition of the Riemann Integral#^def-32-1|Upper and Lower Sums (451 Def. §32.1)]]; MATH 452 multiple-integral version: [[§15 Multivariable Integration#^def-15-8|452 Def. §15.8]].

> [!definition] Definition §8.3: Riemann Integrable
> A bounded function $f: [a, b] \to \mathbb{R}$ is **Riemann integrable** if
>
> $$
> \lim_{|P| \to 0} L(f, P) = \lim_{|P| \to 0} U(f, P).
> $$
>
> In this case, we define the **Riemann integral**:
>
> $$
> \int_a^b f(x) \, dx = \lim_{|P| \to 0} L(f, P) = \lim_{|P| \to 0} U(f, P).
> $$

^def-8-3

> [!remark]- Connections
> - MATH 451 defines it through Riemann sums ([[§32 The Definition of the Riemann Integral#^def-32-3|451 Def. §32.3]]); the mesh form of the Cauchy criterion is [[§32 The Definition of the Riemann Integral#^thm-32-6|Equivalence of the Two Integrals (451 §32.6)]].
> - Restated in [[§15 The General Lebesgue Integral#^rem-15-6|Riemann Integrability via Step Functions]] and compared with the Lebesgue integral in [[Riemann Integrable Implies Lebesgue Integrable|Theorem §15.10]].

> [!remark] Remark
> Equivalently, we can define:
>
> $$
> U(f) = \inf_P \{U(f, P)\}, \quad L(f) = \sup_P \{L(f, P)\}.
> $$
>
> Then $f$ is Riemann integrable if and only if $U(f) = L(f)$.

^rem-8-1

> [!remark]- Connections
> - This is the Darboux integral of MATH 451 ([[§32 The Definition of the Riemann Integral#^def-32-2|451 Def. §32.2]]); the equivalence is [[§32 The Definition of the Riemann Integral#^thm-32-6|451 §32.6]].

## Continuous Functions are Riemann Integrable

> [!theorem] Proposition §8.1
> If $f$ is continuous on $[a, b]$, then $f$ is Riemann integrable.

^prop-8-1

> [!proof]+ Proof
> Since $f$ is continuous on the compact set $[a, b]$ ([[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|Heine–Borel]]), it is [[§19 Uniform Continuity#^thm-19-1|uniformly continuous]].
>
> Let $\epsilon > 0$. By uniform continuity, there exists $\delta > 0$ such that for all $x, y \in [a, b]$:
>
> $$
> |x - y| < \delta \implies |f(x) - f(y)| < \epsilon.
> $$
>
> Take any partition $P = \{x_0, x_1, \ldots, x_n\}$ with $|P| < \delta$.
>
> On each subinterval $[x_j, x_{j+1}]$, since $x_{j+1} - x_j < \delta$, we have $M_j - m_j < \epsilon$.
>
> Thus:
>
> $$
> U(f, P) - L(f, P) = \sum_{j=0}^{n-1} (M_j - m_j)(x_{j+1} - x_j) < \epsilon \sum_{j=0}^{n-1} (x_{j+1} - x_j) = \epsilon(b - a).
> $$
>
> Since $\epsilon > 0$ is arbitrary, $\lim_{|P| \to 0} (U(f, P) - L(f, P)) = 0$. Since $L(f, P) \leq L(f) \leq U(f) \leq U(f, P)$ for every partition $P$ ([[§8 Motivation꞉ The Riemann Integral#^rem-8-1|Remark §8.1]], [[§32 The Definition of the Riemann Integral#^thm-32-6|451 §32.6]]), this gives $U(f) = L(f)$ and $U(f, P) \to U(f)$, $L(f, P) \to L(f)$ as $|P| \to 0$. So both limits in Definition §8.3 exist and are equal, and $f$ is Riemann integrable.

^pf-8-1

*Uses:* [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|§6.4]], [[§19 Uniform Continuity#^thm-19-1|451 §19.1]], [[§8 Motivation꞉ The Riemann Integral#^def-8-2|Def. §8.2]], [[§8 Motivation꞉ The Riemann Integral#^def-8-3|Def. §8.3]], [[§8 Motivation꞉ The Riemann Integral#^rem-8-1|Rem. §8.1]], [[§32 The Definition of the Riemann Integral#^thm-32-6|451 §32.6]]

> [!remark]- Connections
> - MATH 451 version: [[§32 The Definition of the Riemann Integral#^thm-32-7|Continuous Functions Are Integrable (451 §32.7)]].

## Limitations of the Riemann Integral

> [!example] Example §8.1: A Sequence of Riemann Integrable Functions
> Let $\{r_1, r_2, r_3, \ldots\}$ be an enumeration of $\mathbb{Q} \cap [0, 1]$. Define $f_n: [0, 1] \to \mathbb{R}$ by:
>
> $$
> f_n(x) = \begin{cases}
> 1 & \text{if } x = r_j \text{ for some } 1 \leq j \leq n \\
> 0 & \text{otherwise}
> \end{cases}
> $$
>
> Each $f_n$ is Riemann integrable with $\int_0^1 f_n(x) \, dx = 0$.

^ex-8-1

> [!example] Example §8.2: The Dirichlet Function
> Define $f: [0, 1] \to \mathbb{R}$ by:
>
> $$
> f(x) = \begin{cases}
> 1 & \text{if } x \in \mathbb{Q} \cap [0, 1] \\
> 0 & \text{if } x \in [0, 1] \setminus \mathbb{Q}
> \end{cases}
> $$
>
> This function is **not** Riemann integrable.

^ex-8-2

> [!proof]+ Proof
> For any partition $P$, every subinterval $[x_j, x_{j+1}]$ contains both rationals and irrationals (by density: [[§4 The Completeness Axiom#^thm-4-7|of ℚ]], [[§17 Continuous Functions#^rem-17-4|of the irrationals]]).
>
> Thus $m_j = 0$ and $M_j = 1$ for all $j$.
>
> Therefore $L(f, P) = 0$ and $U(f, P) = 1$ for all partitions $P$.
>
> Hence $L(f) = 0 \neq 1 = U(f)$, so $f$ is not Riemann integrable.

^pf-ex-8-2

*Uses:* [[§8 Motivation꞉ The Riemann Integral#^def-8-2|Def. §8.2]], [[§8 Motivation꞉ The Riemann Integral#^rem-8-1|Rem. §8.1]], [[§4 The Completeness Axiom#^thm-4-7|451 §4.7]], [[§17 Continuous Functions#^rem-17-4|451 Rem. §17.4]]

> [!remark]- Connections
> - MATH 451: [[§32 The Definition of the Riemann Integral#^ex-32-3|The Dirichlet function is not integrable (451 Ex. §32.3)]]; all its uses are collected in [[Dirichlet and Thomae functions]].
> - Lebesgue: $\mathbb{Q} \cap [0,1]$ is null ([[§9 Lebesgue Outer Measure#^ex-9-2|Ex. §9.2]]), so $f = 0$ a.e. and its Lebesgue integral is $0$ ([[§14 The Lebesgue Integral for Simple Functions#^prop-14-9|Proposition §14.9]]).

> [!remark] Remark
> Note that $f_n \to f$ pointwise as $n \to \infty$. We have:
> - Each $f_n$ is Riemann integrable
> - The pointwise limit $f$ is **not** Riemann integrable
>
> This shows that the space of Riemann integrable functions is not closed under pointwise limits. This is a fundamental limitation that motivates the development of the Lebesgue integral.

^rem-8-2

![[m551-8-2.svg]]
*Left: $f_5$ from Example §8.1, for an enumeration beginning $\tfrac12, \tfrac13, \tfrac23, \tfrac14, \tfrac34$ — it is $0$ except at five points, so its integral is $0$. Right: the pointwise limit $f$ (Example §8.2) — rationals (red, height $1$) and irrationals (blue, height $0$) are dense in every subinterval, so $M_j = 1$ and $m_j = 0$ for every partition: the upper sum is the whole red area $1$, the lower sum is $0$.*

> [!remark]- Connections
> - MATH 451 only passes to the limit under uniform convergence: [[§33 Properties of the Riemann Integral#^thm-33-12|Integration of Uniform Limits (451 §33.12)]].
> - The Lebesgue answer: pointwise limits of measurable functions are measurable ([[§12 Measurable Functions#^cor-12-8|Corollary §12.8]]), and integrals pass to the limit under the [[Monotone Convergence Theorem (Lebesgue)|Monotone Convergence Theorem]] and the [[Dominated Convergence Theorem|Dominated Convergence Theorem]].
