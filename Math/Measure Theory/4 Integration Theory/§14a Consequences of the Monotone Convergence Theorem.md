---
type: section
subject: "[[Measure Theory]]"
chapter: 4
section: 14
tags: [measure-theory, math551]
---
← [[§14 The Lebesgue Integral for Simple Functions]] · ↑ [[· 4 Integration Theory]] · [[§15 The General Lebesgue Integral]] →

The [[Monotone Convergence Theorem (Lebesgue)|Monotone Convergence Theorem]] turns the supremum definition of the integral into limits of integrals of simple functions. Its consequences are linearity of the integral, the behaviour on null sets, the series version MCT II, the measure induced by a non-negative function, a decreasing version, and Fatou's lemma.

## Consequences of the MCT

> [!theorem] Theorem §14.8: Linearity of the Integral
> Let $f, g$ be non-negative measurable functions on $E$, $E \in \mathcal{M}$, and $c \geq 0$. Then:
> - (i) $\displaystyle\int_E c\,f(x)\,dx = c\int_E f(x)\,dx$.
> - (ii) $\displaystyle\int_E \bigl(f(x) + g(x)\bigr)\,dx = \int_E f(x)\,dx + \int_E g(x)\,dx$.

^thm-14-8

> [!proof]+ Proof
> **(i)** If $c = 0$, both sides are $0$ (using the [[§12 Measurable Functions#^rem-12-1|convention]] $0 \cdot \infty = 0$). Assume $c > 0$. By definition:
>
> $$
> \int_E c\,f\,dx = \sup\left\{\int_E h\,dx \;\middle|\; h \text{ simple},\; 0 \leq h \leq c\,f \text{ on } E\right\}.
> $$
>
> We show both inequalities.
>
> *$(\leq)$*: Let $h$ be simple with $0 \leq h \leq c\,f$ on $E$. Then $h/c$ is simple with $0 \leq h/c \leq f$ on $E$, so $\int_E (h/c)\,dx \leq \int_E f\,dx$. By [[§14 The Lebesgue Integral for Simple Functions#^prop-14-1|linearity for simple functions]], $\int_E h\,dx = c\int_E (h/c)\,dx \leq c\int_E f\,dx$. Taking the supremum over all such $h$: $\int_E c\,f\,dx \leq c\int_E f\,dx$.
>
> *$(\geq)$*: Let $h$ be simple with $0 \leq h \leq f$ on $E$. Then $c\,h$ is simple with $0 \leq c\,h \leq c\,f$ on $E$, so $\int_E c\,h\,dx \leq \int_E c\,f\,dx$. By linearity for simple functions, $c\int_E h\,dx = \int_E c\,h\,dx \leq \int_E c\,f\,dx$. Taking the supremum over all such $h$: $c\int_E f\,dx \leq \int_E c\,f\,dx$.
>
> **(ii)** Let $\{\varphi_k\}$ and $\{\psi_k\}$ be increasing sequences of non-negative simple measurable functions with $\lim_{k \to \infty} \varphi_k(x) = f(x)$ and $\lim_{k \to \infty} \psi_k(x) = g(x)$ (which exist by the [[Simple Function Approximation Theorem|Simple Function Approximation Theorem]]). Then $\{\varphi_k + \psi_k\}$ is an increasing sequence of non-negative simple measurable functions with $\varphi_k + \psi_k \nearrow f + g$. By linearity for simple functions and the [[Monotone Convergence Theorem (Lebesgue)|MCT]]:
>
> $$
> \begin{aligned}
> \int_E (f + g)\,dx &= \lim_{k \to \infty} \int_E (\varphi_k + \psi_k)\,dx = \lim_{k \to \infty} \left(\int_E \varphi_k\,dx + \int_E \psi_k\,dx\right) \\
> &= \lim_{k \to \infty} \int_E \varphi_k\,dx + \lim_{k \to \infty} \int_E \psi_k\,dx = \int_E f\,dx + \int_E g\,dx.
> \end{aligned}
> $$

^pf-14-8

*Uses:* [[§14 The Lebesgue Integral for Simple Functions#^def-14-2|Def. §14.2]], [[§12 Measurable Functions#^rem-12-1|Rem. §12.1]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-1|§14.1]], [[Simple Function Approximation Theorem|§12.14]], [[Monotone Convergence Theorem (Lebesgue)|§14.4]]

> [!remark]- Connections
> - Riemann counterpart: [[§33 Properties of the Riemann Integral#^thm-33-2|451 §33.2]]; extended to signed integrable functions in [[§15 The General Lebesgue Integral#^thm-15-2|Theorem §15.2]].

> [!theorem] Proposition §14.9: Integral over Null Sets and A.E. Equal Functions
> Let $f, g$ be non-negative measurable functions on $E \in \mathcal{M}$.
> - (i) If $m(E) = 0$, then $\int_E f\,dx = 0$.
> - (ii) If $f(x) = g(x)$ [[§12 Measurable Functions#^def-12-5|a.e.]] on $E$, then $\int_E f\,dx = \int_E g\,dx$.

^prop-14-9

> [!proof]+ Proof
> **(i)** For any simple $h$ with $0 \leq h \leq f$ on $E$, $\int_E h\,dx = 0$ (since $m(E) = 0$). The supremum is $0$.
>
> **(ii)** Let $E_0 = \{x \in E : f(x) \neq g(x)\}$. By assumption, $m(E_0) = 0$. Using the identity $\chi_{E_0} + \chi_{E \setminus E_0} = \chi_E$:
>
> $$
> \int_E f\,dx = \int_E f\,\chi_{E_0}\,dx + \int_E f\,\chi_{E \setminus E_0}\,dx = \int_{E_0} f\,dx + \int_{E \setminus E_0} f\,dx = 0 + \int_{E \setminus E_0} f\,dx.
> $$
>
> Similarly, $\int_E g\,dx = \int_{E \setminus E_0} g\,dx$. Since $f = g$ on $E \setminus E_0$, the integrals agree.

^pf-14-9

*Uses:* [[§14 The Lebesgue Integral for Simple Functions#^prop-14-2|§14.2]], [[§12 Measurable Functions#^def-12-5|Def. §12.5]], [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|§14.8]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-6|§14.6]]

> [!theorem] Proposition §14.10: Integrability Implies A.E. Finiteness
> Let $f \geq 0$ be measurable on $E \in \mathcal{M}$. If $f$ is integrable on $E$ (i.e., $\int_E f\,dx < \infty$), then $f$ is a.e. finite on $E$. (We adopt the convention $0 \cdot \infty = 0$.)

^prop-14-10

> [!proof]+ Proof
> Let $E_0 = \{x \in E : f(x) = +\infty\}$. We want to show $m(E_0) = 0$.
>
> Since $f(x) \geq f(x)\,\chi_{E_0}(x) \geq k\,\chi_{E_0}(x)$ for all $k \in \mathbb{N}$ (because $f = +\infty$ on $E_0$):
>
> $$
> \infty > \int_E f\,dx \geq \int_{E_0} f\,dx \geq \int_E k\,\chi_{E_0}\,dx = k\,m(E_0).
> $$
>
> Thus $m(E_0) \leq \frac{\int_E f\,dx}{k} \to 0$ as $k \to \infty$. Hence $m(E_0) = 0$.

^pf-14-10

*Uses:* [[§14 The Lebesgue Integral for Simple Functions#^cor-14-7|§14.7]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-6|§14.6]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]]

> [!theorem] Proposition §14.11: Vanishing Integral for Non-Negative Functions
> Let $f \geq 0$ be measurable on $E$. If $\int_E f\,dx = 0$, then $f(x) = 0$ a.e. on $E$.
>
> Consequently, $\int_A f\,dx = 0$ for all $A \subseteq E$, $A \in \mathcal{M}$.

^prop-14-11

> [!proof]+ Proof
> Let $E_0 = \{x \in E : f(x) > 0\}$. We want to show $m(E_0) = 0$.
>
> Define $E_k = \{x \in E : f(x) > 1/k\}$ for $k \in \mathbb{N}$. Then $E_0 = \bigcup_{k=1}^{\infty} E_k$ (every $x \in E_0$ has $f(x) > 0$, so $f(x) > 1/k$ for $k$ large enough).
>
> Since $f \geq 0$:
>
> $$
> 0 = \int_E f\,dx \geq \int_{E_k} f\,dx \geq \frac{1}{k}\,m(E_k),
> $$
>
> so $m(E_k) = 0$ for all $k$. By [[Properties of Lebesgue Outer Measure|countable subadditivity]]: $m(E_0) \leq \sum_{k=1}^{\infty} m(E_k) = 0$.

^pf-14-11

*Uses:* [[§14 The Lebesgue Integral for Simple Functions#^cor-14-7|§14.7]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[Properties of Lebesgue Outer Measure|§9.1]]

> [!remark]- Connections
> - Riemann version (continuous $f \geq 0$ with $\int_a^b f = 0$ is identically $0$): [[§33 Properties of the Riemann Integral#^thm-33-7|451 §33.7]]. Without continuity, "$\equiv 0$" weakens to "$= 0$ a.e.".
> - Signed version: [[§15 The General Lebesgue Integral#^prop-15-5|Proposition §15.5]]; used in the proof of [[Riemann Integrable Implies Lebesgue Integrable|Theorem §15.10]] and for $\|f\|_1 = 0$ in [[§16 The L¹ Space and Density Theorems#^thm-16-4|Theorem §16.4]].

## MCT II: The Series Version

> [!theorem] Theorem §14.12: MCT II
> Let $\{f_k\}_{k=1}^{\infty}$ be a sequence of non-negative measurable functions on $E \in \mathcal{M}$. Then:
>
> $$
> \sum_{k=1}^{\infty} \int_E f_k(x)\,dx = \int_E \sum_{k=1}^{\infty} f_k(x)\,dx.
> $$

^thm-14-12

> [!proof]+ Proof
> Define the partial sums $S_m(x) = \sum_{k=1}^{m} f_k(x)$. Then $\lim_{m \to \infty} S_m(x) = \sum_{k=1}^{\infty} f_k(x)$, and $S_m \geq 0$, $S_m(x) \leq S_{m+1}(x)$ for all $x \in E$ and all $m$. By the [[Monotone Convergence Theorem (Lebesgue)|MCT]]:
>
> $$
> \int_E \lim_{m \to \infty} S_m\,dx = \lim_{m \to \infty} \int_E S_m\,dx = \lim_{m \to \infty} \sum_{k=1}^{m} \int_E f_k\,dx = \sum_{k=1}^{\infty} \int_E f_k\,dx,
> $$
>
> where the second equality uses [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|linearity of the integral]] for finite sums.

^pf-14-12

*Uses:* [[Monotone Convergence Theorem (Lebesgue)|§14.4]], [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|§14.8]]

> [!remark]- Connections
> - Contrast with MATH 451, where term-by-term integration of a series needs uniform convergence ([[§33 Properties of the Riemann Integral#^thm-33-12|451 §33.12]], e.g. via the [[§25 More on Uniform Convergence#^thm-25-3|Weierstrass M-test]]).
> - Signed version: [[§15 The General Lebesgue Integral#^cor-15-9|Corollary §15.9]].

> [!theorem] Corollary §14.13: Countable Additivity of the Integral over Disjoint Sets
> Let $\{E_k\}_{k=1}^{\infty}$ be a sequence of pairwise disjoint measurable sets in $\mathbb{R}^n$, and let $E = \bigcup_{k=1}^{\infty} E_k$. If $f$ is a non-negative measurable function, then:
>
> $$
> \int_E f\,dx = \sum_{k=1}^{\infty} \int_{E_k} f\,dx.
> $$

^cor-14-13

> [!proof]+ Proof
> Define $f_k(x) = f(x)\,\chi_{E_k}(x)$. Since the $E_k$ are pairwise disjoint, $f(x) = \sum_{k=1}^{\infty} f_k(x)$ for all $x \in E$. By [[§14 The Lebesgue Integral for Simple Functions#^thm-14-12|MCT II]]:
>
> $$
> \int_E f\,dx = \int_E \sum_{k=1}^{\infty} f_k\,dx = \sum_{k=1}^{\infty} \int_E f_k\,dx = \sum_{k=1}^{\infty} \int_{E_k} f\,dx,
> $$
>
> where the last equality uses $\int_E f_k\,dx = \int_E f\,\chi_{E_k}\,dx = \int_{E_k} f\,dx$.

^pf-14-13

*Uses:* [[§14 The Lebesgue Integral for Simple Functions#^thm-14-12|§14.12]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-6|§14.6]]

## The Induced Measure

> [!definition] Definition §14.3: Measure Induced by a Non-Negative Function
> Let $f$ be a non-negative measurable function on $\mathbb{R}^n$. Define $\nu: \mathcal{M} \to [0, \infty]$ by:
>
> $$
> \nu(E) = \int_E f(x)\,dx, \qquad E \in \mathcal{M}.
> $$
>
> Then $\nu$ is a [[§11 Borel Sets and Measure Spaces#^def-11-6|measure]] on $(\mathbb{R}^n, \mathcal{M})$.

^def-14-3

> [!remark] Remark
> To verify that $\nu$ is a measure, we check the axioms:
> - (i) $\nu(\emptyset) = \int_\emptyset f\,dx = 0$ ([[§14 The Lebesgue Integral for Simple Functions#^prop-14-9|integral over null set]]).
> - (ii) $\nu(E) \geq 0$ for all $E \in \mathcal{M}$ (since $f \geq 0$).
> - (iii) **Countable additivity**: If $\{E_k\}$ are pairwise disjoint measurable sets, then by the [[§14 The Lebesgue Integral for Simple Functions#^cor-14-13|corollary above]]:
>
> $$
> \nu\!\left(\bigcup_{k=1}^{\infty} E_k\right) = \int_{\bigcup E_k} f\,dx = \sum_{k=1}^{\infty} \int_{E_k} f\,dx = \sum_{k=1}^{\infty} \nu(E_k).
> $$
>
> Note that $\nu$ depends on $f$ and is sometimes written $d\nu = f\,dx$. If $f = 1$, then $\nu(E) = m(E)$, recovering Lebesgue measure.

^rem-14-4

> [!remark]- Connections
> - Signed analogue for $f \in L(E)$: [[§15 The General Lebesgue Integral#^rem-15-2|Rem. §15.2]]. Its "small sets have small $\nu$-measure" property is [[§16 The L¹ Space and Density Theorems#^thm-16-1|Theorem §16.1]].

## MCT for Decreasing Sequences

> [!theorem] Theorem §14.14: Monotone Convergence Theorem — Decreasing Version
> Let $\{f_k\}$ be a sequence of non-negative measurable functions on $E \in \mathcal{M}$ with:
>
> $$
> f_k(x) \geq f_{k+1}(x) \quad \text{for all } x \in E,\; k \in \mathbb{N}, \qquad \lim_{k \to \infty} f_k(x) = f(x).
> $$
>
> Assume there exists $k_0 \in \mathbb{N}$ such that $\int_E f_{k_0}\,dx < \infty$. Then:
>
> $$
> \lim_{k \to \infty} \int_E f_k(x)\,dx = \int_E f(x)\,dx.
> $$

^thm-14-14

> [!proof]+ Proof
> Since $\{f_k\}$ is decreasing and $f_k \geq f_{k+1} \geq \cdots \geq f \geq 0$ for $k \geq k_0$, we have $\int_E f_k\,dx \leq \int_E f_{k_0}\,dx < \infty$ for all $k \geq k_0$. The limit depends only on the tail, so we may assume WLOG that $k_0 = 1$.
>
> **Main argument.** Define $g_k = f_1 - f_k$ for $k \geq 1$. Since $f_k$ is decreasing, $g_k$ is an increasing sequence of non-negative measurable functions with $g_k \nearrow f_1 - f$ pointwise. By the (increasing) [[Monotone Convergence Theorem (Lebesgue)|MCT]]:
>
> $$
> \lim_{k \to \infty} \int_E g_k\,dx = \int_E (f_1 - f)\,dx.
> $$
>
> Since $f_1 \geq f_k \geq 0$ and $\int f_k \leq \int f_1 < \infty$, by the [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|subtraction rule]] ($\int(f - g) = \int f - \int g$ when $f \geq g \geq 0$ and $\int g < \infty$; this is [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|Theorem §14.8]] (ii) applied to $f = g + (f - g)$, after subtracting the finite number $\int g$):
>
> **Left side**:
>
> $$
> \lim_{k \to \infty} \int_E g_k\,dx = \lim_{k \to \infty} \left(\int_E f_1\,dx - \int_E f_k\,dx\right) = \int_E f_1\,dx - \lim_{k \to \infty} \int_E f_k\,dx.
> $$
>
> **Right side**:
>
> $$
> \int_E (f_1 - f)\,dx = \int_E f_1\,dx - \int_E f\,dx.
> $$
>
> Setting them equal:
>
> $$
> \int_E f_1\,dx - \lim_{k \to \infty} \int_E f_k\,dx = \int_E f_1\,dx - \int_E f\,dx.
> $$
>
> Since $\int_E f_1\,dx < \infty$, cancel it from both sides:
>
> $$
> \lim_{k \to \infty} \int_E f_k\,dx = \int_E f\,dx.
> $$

^pf-14-14

*Uses:* [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[Monotone Convergence Theorem (Lebesgue)|§14.4]], [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|§14.8]]

> [!remark] Remark: The Nonnegativity Assumption Can Be Dropped
> Once the [[§15 The General Lebesgue Integral#^def-15-1|general Lebesgue integral]] and its [[§15 The General Lebesgue Integral#^thm-15-2|linearity]] are available ([[§15 The General Lebesgue Integral|§15]]), the nonnegativity assumption is unnecessary. For a decreasing sequence $f_1 \geq f_2 \geq \cdots$ of *any* measurable functions with $f_1 \in L(E)$, the same conclusion holds. The proof is identical: define $g_k = f_1 - f_k \geq 0$ (nonneg because $f_k \leq f_1$, *not* because $f_k \geq 0$), apply the increasing MCT to $g_k \nearrow f_1 - f$, then use linearity of the integral to cancel $\int f_1 < \infty$.
>
> This reflects a general pattern:
>
> | | **Increasing** | **Decreasing** |
> |---|---|---|
> | **Condition** | $f_k \geq 0$ (lower bound) | $f_1 \in L$ (integrable upper bound) |
> | **Why** | Integrals well-defined (can be $+\infty$) | Need to subtract; $\infty - \infty$ undefined |
> | **Compare** | [[Continuity of Measure\|Cont. of measure from below]] | [[§11 Borel Sets and Measure Spaces#^prop-11-13\|Cont. of measure from above]] ($m(E_1) < \infty$) |
>
> The increasing case needs a lower bound to ensure integrals exist; the decreasing case needs an *integrable* upper bound to allow subtraction.

^rem-14-5

> [!remark] Remark: Why the Finiteness Hypothesis is Necessary
> Without the assumption $\int_E f_{k_0}\,dx < \infty$, the conclusion can fail. For example, let $f_k = \chi_{(k, \infty)}$ on $\mathbb{R}$. Then $f_k \searrow 0$ pointwise, but $\int_{\mathbb{R}} f_k\,dx = \infty$ for all $k$, so $\lim \int f_k = \infty \neq 0 = \int 0\,dx$.

^rem-14-6

## Fatou's Lemma

> [!theorem] Theorem §14.15: Fatou's Lemma
> Let $E \in \mathcal{M}$, $E \subseteq \mathbb{R}^n$, and let $\{f_k\}_{k=1}^{\infty}$ be a sequence of non-negative measurable functions on $E$. Then:
>
> $$
> \int_E \liminf_{k \to \infty} f_k(x)\,dx \leq \liminf_{k \to \infty} \int_E f_k(x)\,dx.
> $$

^thm-14-15

> [!proof]+ Proof
> Define $g_l(x) = \inf_{k \geq l} f_k(x)$. Then:
> - Each $g_l$ is non-negative and measurable ([[§12 Measurable Functions#^thm-12-6|infimum of measurable functions]]).
> - $\liminf_{k \to \infty} f_k(x) = \lim_{l \to \infty} g_l(x)$ (by [[§12 Measurable Functions#^rem-12-4|definition]] of $\liminf$).
> - $g_l(x) \leq g_{l+1}(x)$ for all $x \in E$ (as $l$ increases, the infimum is taken over fewer terms).
>
> By the [[Monotone Convergence Theorem (Lebesgue)|MCT]] applied to the increasing sequence $\{g_l\}$:
>
> $$
> \int_E \liminf_{k \to \infty} f_k\,dx = \int_E \lim_{l \to \infty} g_l\,dx = \lim_{l \to \infty} \int_E g_l\,dx.
> $$
>
> Since $g_l(x) = \inf_{k \geq l} f_k(x) \leq f_k(x)$ for all $k \geq l$, [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|monotonicity of the integral]] gives:
>
> $$
> \int_E g_l\,dx \leq \int_E f_k\,dx \quad \text{for all } k \geq l.
> $$
>
> Taking the infimum over $k \geq l$:
>
> $$
> \int_E g_l\,dx \leq \inf_{k \geq l} \int_E f_k\,dx.
> $$
>
> Taking $l \to \infty$:
>
> $$
> \int_E \liminf_{k \to \infty} f_k\,dx = \lim_{l \to \infty} \int_E g_l\,dx \leq \lim_{l \to \infty} \inf_{k \geq l} \int_E f_k\,dx = \liminf_{k \to \infty} \int_E f_k\,dx.
> $$

^pf-14-15

*Uses:* [[§12 Measurable Functions#^thm-12-6|§12.6]], [[§12 Measurable Functions#^rem-12-4|Rem. §12.4]], [[Monotone Convergence Theorem (Lebesgue)|§14.4]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§10 Monotone Sequences and Cauchy Sequences#^def-10-3|451 Def. §10.3]]

> [!example] Example §14.1: Fatou's Inequality Can Be Strict
> Define $f_k: [0, 1] \to \mathbb{R}$ by:
>
> $$
> f_k(x) = k\,\chi_{(0, 1/k)}(x) = \begin{cases} k & \text{if } 0 < x < 1/k, \\ 0 & \text{otherwise.} \end{cases}
> $$
>
> For every $x_0 \in [0, 1]$: if $x_0 = 0$, then $f_k(x_0) = 0$ for all $k$; if $0 < x_0 \leq 1$, then for $k > 1/x_0$ we have $x_0 \geq 1/k$, so $f_k(x_0) = 0$ eventually. Thus $\lim_{k \to \infty} f_k(x_0) = 0$ for all $x_0 \in [0,1]$.
>
> **Left side**: $\int_0^1 \liminf_{k \to \infty} f_k\,dx = \int_0^1 0\,dx = 0$.
>
> **Right side**: $\int_0^1 f_k\,dx = k \cdot m\!\bigl((0, 1/k)\bigr) = k \cdot \frac{1}{k} = 1$ for all $k$, so $\liminf_{k \to \infty} \int_0^1 f_k\,dx = 1$.
>
> Therefore $0 = \int_0^1 \liminf f_k\,dx < \liminf \int_0^1 f_k\,dx = 1$. The inequality is strict because the “mass” of $f_k$ escapes to the left, concentrating on ever-smaller intervals.

^ex-14-1

![[m551-14-3.svg]]
*Fatou's inequality is strict for $f_k = k\,\chi_{(0,1/k)}$, shown for $k = 1, 2, 4, 8$. Every rectangle has area $\int_0^1 f_k = 1$ (hollow dots: the intervals are open), but they get thinner and each fixed $x$ is eventually outside all of them, so $\lim f_k = 0$ everywhere. The mass piles up at $0$ and vanishes in the limit.*

> [!remark]- Connections
> - The same escaping-mass phenomenon in MATH 451: [[§25 More on Uniform Convergence#^ex-25-1|451 Ex. §25.1]] (the escaping triangle), where the convergence is pointwise but not uniform.
> - No integrable dominator exists here, so the [[Dominated Convergence Theorem|DCT]] does not apply.

> [!example] Example §14.2: Covering Lemma via Integration
> Let $E_1, \ldots, E_n \subseteq [0,1]$ be measurable. Assume every point $x \in [0,1]$ belongs to at least $l$ of the sets $E_k$, $1 \leq k \leq n$. Then at least one $E_i$ has $m(E_i) \geq l/n$.
>
> *Proof.* The hypothesis says $\sum_{k=1}^{n} \chi_{E_k}(x) \geq l$ for all $x \in [0,1]$. Integrating:
>
> $$
> \sum_{k=1}^{n} m(E_k) = \int_0^1 \sum_{k=1}^{n} \chi_{E_k}(x)\,dx \geq \int_0^1 l\,dx = l.
> $$
>
> Since $\sum_{k=1}^n m(E_k) \geq l$, by the pigeonhole principle there exists $1 \leq i \leq n$ with $m(E_i) \geq l/n$.

^ex-14-2

*Uses:* [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|§14.8]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]]

> [!remark] Remark: Why Sup and Not Inf in the Definition of the Integral?
> For $f \geq 0$ measurable, the integral is defined as:
>
> $$
> \int_E f\,dx = \sup\left\{\int_E h\,dx \;\middle|\; 0 \leq h \leq f,\; h \text{ simple}\right\}.
> $$
>
> One might ask: why not instead take $\inf\!\left\{\int_E h\,dx \mid h \geq f,\; h \text{ simple}\right\}$? The answer is that this infimum does not work in general. For instance, if one tried to define it for $f = \chi_V$ where $V$ is a [[§11 Borel Sets and Measure Spaces#^def-11-12|Vitali set]] (not measurable, so $\chi_V$ lies outside the scope of the definition), any simple function $h \geq f$ satisfies $h \geq \chi_V$, but the integral of $h$ does not “see” $V$ in a controlled way. More fundamentally, the sup definition builds the integral from below using functions we understand completely (simple functions), and the [[Monotone Convergence Theorem (Lebesgue)|MCT]] guarantees this sup equals the “true” integral. The inf approach would require an analogous convergence theorem from above, which does not hold without additional integrability hypotheses.

^rem-14-7

> [!remark]- Connections
> - The Riemann integral uses both sides (upper and lower Darboux integrals must agree): [[§8 Motivation꞉ The Riemann Integral#^rem-8-1|Rem. §8.1]], [[§32 The Definition of the Riemann Integral#^def-32-2|451 Def. §32.2]]. The Vitali set is non-measurable by [[The Vitali Set is Not Measurable|Theorem §11.20]].
