---
type: section
subject: "[[Measure Theory]]"
chapter: 4
section: 21
tags: [measure-theory, math551]
---
← [[§20 The Lebesgue Integral for Simple Functions]] · ↑ [[· 4 Integration Theory]] · [[§22 The General Lebesgue Integral]] →

The [[Monotone Convergence Theorem (Lebesgue)|Monotone Convergence Theorem]] turns the supremum definition of the integral into limits of integrals of simple functions. Its consequences are linearity of the integral, the behaviour on null sets, the series version MCT II, the measure induced by a non-negative function, a decreasing version, and Fatou's lemma.

## Consequences of the MCT

> [!theorem] Theorem §21.1: Linearity of the Integral
> Let $f, g$ be non-negative measurable functions on $E$, $E \in \mathcal{M}$, and $c \geq 0$. Then:
> - (i) $\displaystyle\int_E c\,f(x)\,dx = c\int_E f(x)\,dx$.
> - (ii) $\displaystyle\int_E \bigl(f(x) + g(x)\bigr)\,dx = \int_E f(x)\,dx + \int_E g(x)\,dx$.

^thm-21-1

> [!proof]+ Proof
> **(i)** If $c = 0$, both sides are $0$ (using the [[§15 Measurable Functions#^rem-15-1|convention]] $0 \cdot \infty = 0$). Assume $c > 0$. By definition:
>
> $$
> \int_E c\,f\,dx = \sup\left\{\int_E h\,dx \;\middle|\; h \text{ simple},\; 0 \leq h \leq c\,f \text{ on } E\right\}.
> $$
>
> We show both inequalities.
>
> *$(\leq)$*: Let $h$ be simple with $0 \leq h \leq c\,f$ on $E$. Then $h/c$ is simple with $0 \leq h/c \leq f$ on $E$, so $\int_E (h/c)\,dx \leq \int_E f\,dx$. By [[§20 The Lebesgue Integral for Simple Functions#^prop-20-1|linearity for simple functions]], $\int_E h\,dx = c\int_E (h/c)\,dx \leq c\int_E f\,dx$. Taking the supremum over all such $h$: $\int_E c\,f\,dx \leq c\int_E f\,dx$.
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

^pf-21-1

*Uses:* [[§20 The Lebesgue Integral for Simple Functions#^def-20-2|Def. §20.2]], [[§15 Measurable Functions#^rem-15-1|Rem. §12.1]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-1|§20.1]], [[Simple Function Approximation Theorem|§17.2]], [[Monotone Convergence Theorem (Lebesgue)|§20.7]]

> [!remark]- Connections
> - Riemann counterpart: [[§33 Properties of the Riemann Integral#^thm-33-2|451 §33.2]]; extended to signed integrable functions in [[§22 The General Lebesgue Integral#^thm-22-2|Theorem §22.2]].

> [!theorem] Proposition §21.2: Integral over Null Sets and A.E. Equal Functions
> Let $f, g$ be non-negative measurable functions on $E \in \mathcal{M}$.
> - (i) If $m(E) = 0$, then $\int_E f\,dx = 0$.
> - (ii) If $f(x) = g(x)$ [[§16 Limits and Positive Parts of Measurable Functions#^def-16-2|a.e.]] on $E$, then $\int_E f\,dx = \int_E g\,dx$.

^prop-21-2

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

^pf-21-2

*Uses:* [[§20 The Lebesgue Integral for Simple Functions#^prop-20-2|§20.2]], [[§16 Limits and Positive Parts of Measurable Functions#^def-16-2|Def. §16.2]], [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|§21.1]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-4|§20.4]]

> [!theorem] Proposition §21.3: Integrability Implies A.E. Finiteness
> Let $f \geq 0$ be measurable on $E \in \mathcal{M}$. If $f$ is integrable on $E$ (i.e., $\int_E f\,dx < \infty$), then $f$ is a.e. finite on $E$. (We adopt the convention $0 \cdot \infty = 0$.)

^prop-21-3

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

^pf-21-3

*Uses:* [[§20 The Lebesgue Integral for Simple Functions#^cor-20-5|§20.5]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-4|§20.4]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[§20 The Lebesgue Integral for Simple Functions#^def-20-1|Def. §20.1]]

> [!theorem] Proposition §21.4: Vanishing Integral for Non-Negative Functions
> Let $f \geq 0$ be measurable on $E$. If $\int_E f\,dx = 0$, then $f(x) = 0$ a.e. on $E$.
>
> Consequently, $\int_A f\,dx = 0$ for all $A \subseteq E$, $A \in \mathcal{M}$.

^prop-21-4

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

^pf-21-4

*Uses:* [[§20 The Lebesgue Integral for Simple Functions#^cor-20-5|§20.5]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[Properties of Lebesgue Outer Measure|§10.1]]

> [!remark]- Connections
> - Riemann version (continuous $f \geq 0$ with $\int_a^b f = 0$ is identically $0$): [[§33 Properties of the Riemann Integral#^thm-33-7|451 §33.7]]. Without continuity, "$\equiv 0$" weakens to "$= 0$ a.e.".
> - Signed version: [[§22 The General Lebesgue Integral#^prop-22-5|Proposition §22.5]]; used in the proof of [[Riemann Integrable Implies Lebesgue Integrable|Theorem §23.5]] and for $\|f\|_1 = 0$ in [[§24 The L¹ Space and Density Theorems#^thm-24-4|Theorem §24.4]].

## MCT II: The Series Version

> [!theorem] Theorem §21.5: MCT II
> Let $\{f_k\}_{k=1}^{\infty}$ be a sequence of non-negative measurable functions on $E \in \mathcal{M}$. Then:
>
> $$
> \sum_{k=1}^{\infty} \int_E f_k(x)\,dx = \int_E \sum_{k=1}^{\infty} f_k(x)\,dx.
> $$

^thm-21-5

> [!proof]+ Proof
> Define the partial sums $S_m(x) = \sum_{k=1}^{m} f_k(x)$. Then $\lim_{m \to \infty} S_m(x) = \sum_{k=1}^{\infty} f_k(x)$, and $S_m \geq 0$, $S_m(x) \leq S_{m+1}(x)$ for all $x \in E$ and all $m$. By the [[Monotone Convergence Theorem (Lebesgue)|MCT]]:
>
> $$
> \int_E \lim_{m \to \infty} S_m\,dx = \lim_{m \to \infty} \int_E S_m\,dx = \lim_{m \to \infty} \sum_{k=1}^{m} \int_E f_k\,dx = \sum_{k=1}^{\infty} \int_E f_k\,dx,
> $$
>
> where the second equality uses [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|linearity of the integral]] for finite sums.

^pf-21-5

*Uses:* [[Monotone Convergence Theorem (Lebesgue)|§20.7]], [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|§21.1]]

> [!remark]- Connections
> - Contrast with MATH 451, where term-by-term integration of a series needs uniform convergence ([[§33 Properties of the Riemann Integral#^thm-33-12|451 §33.12]], e.g. via the [[§25 More on Uniform Convergence#^thm-25-3|Weierstrass M-test]]).
> - Signed version: [[§23 The Dominated Convergence Theorem#^cor-23-4|Corollary §23.4]].

> [!theorem] Corollary §21.6: Countable Additivity of the Integral over Disjoint Sets
> Let $\{E_k\}_{k=1}^{\infty}$ be a sequence of pairwise disjoint measurable sets in $\mathbb{R}^n$, and let $E = \bigcup_{k=1}^{\infty} E_k$. If $f$ is a non-negative measurable function, then:
>
> $$
> \int_E f\,dx = \sum_{k=1}^{\infty} \int_{E_k} f\,dx.
> $$

^cor-21-6

> [!proof]+ Proof
> Define $f_k(x) = f(x)\,\chi_{E_k}(x)$. Since the $E_k$ are pairwise disjoint, $f(x) = \sum_{k=1}^{\infty} f_k(x)$ for all $x \in E$. By [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-5|MCT II]]:
>
> $$
> \int_E f\,dx = \int_E \sum_{k=1}^{\infty} f_k\,dx = \sum_{k=1}^{\infty} \int_E f_k\,dx = \sum_{k=1}^{\infty} \int_{E_k} f\,dx,
> $$
>
> where the last equality uses $\int_E f_k\,dx = \int_E f\,\chi_{E_k}\,dx = \int_{E_k} f\,dx$.

^pf-21-6

*Uses:* [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-5|§21.5]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-4|§20.4]]

## The Induced Measure

> [!definition] Definition §21.1: Measure Induced by a Non-Negative Function
> Let $f$ be a non-negative measurable function on $\mathbb{R}^n$. Define $\nu: \mathcal{M} \to [0, \infty]$ by:
>
> $$
> \nu(E) = \int_E f(x)\,dx, \qquad E \in \mathcal{M}.
> $$
>
> Then $\nu$ is a [[§12 Borel Sets and Measure Spaces#^def-12-6|measure]] on $(\mathbb{R}^n, \mathcal{M})$.

^def-21-1

> [!remark] Remark
> To verify that $\nu$ is a measure, we check the axioms:
> - (i) $\nu(\emptyset) = \int_\emptyset f\,dx = 0$ ([[§21 Consequences of the Monotone Convergence Theorem#^prop-21-2|integral over null set]]).
> - (ii) $\nu(E) \geq 0$ for all $E \in \mathcal{M}$ (since $f \geq 0$).
> - (iii) **Countable additivity**: If $\{E_k\}$ are pairwise disjoint measurable sets, then by the [[§21 Consequences of the Monotone Convergence Theorem#^cor-21-6|corollary above]]:
>
> $$
> \nu\!\left(\bigcup_{k=1}^{\infty} E_k\right) = \int_{\bigcup E_k} f\,dx = \sum_{k=1}^{\infty} \int_{E_k} f\,dx = \sum_{k=1}^{\infty} \nu(E_k).
> $$
>
> Note that $\nu$ depends on $f$ and is sometimes written $d\nu = f\,dx$. If $f = 1$, then $\nu(E) = m(E)$, recovering Lebesgue measure.

^rem-21-4

> [!remark]- Connections
> - Signed analogue for $f \in L(E)$: [[§22 The General Lebesgue Integral#^rem-22-2|Rem. §15.2]]. Its "small sets have small $\nu$-measure" property is [[§24 The L¹ Space and Density Theorems#^thm-24-2|Theorem §24.2]].

## MCT for Decreasing Sequences

> [!theorem] Theorem §21.7: Monotone Convergence Theorem — Decreasing Version
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

^thm-21-7

> [!proof]+ Proof
> Since $\{f_k\}$ is decreasing and $f_k \geq f_{k+1} \geq \cdots \geq f \geq 0$ for $k \geq k_0$, we have $\int_E f_k\,dx \leq \int_E f_{k_0}\,dx < \infty$ for all $k \geq k_0$. The limit depends only on the tail, so we may assume WLOG that $k_0 = 1$.
>
> **Main argument.** Define $g_k = f_1 - f_k$ for $k \geq 1$. Since $f_k$ is decreasing, $g_k$ is an increasing sequence of non-negative measurable functions with $g_k \nearrow f_1 - f$ pointwise. By the (increasing) [[Monotone Convergence Theorem (Lebesgue)|MCT]]:
>
> $$
> \lim_{k \to \infty} \int_E g_k\,dx = \int_E (f_1 - f)\,dx.
> $$
>
> Since $f_1 \geq f_k \geq 0$ and $\int f_k \leq \int f_1 < \infty$, by the [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|subtraction rule]] ($\int(f - g) = \int f - \int g$ when $f \geq g \geq 0$ and $\int g < \infty$; this is [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|Theorem §21.1]] (ii) applied to $f = g + (f - g)$, after subtracting the finite number $\int g$):
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

^pf-21-7

*Uses:* [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[Monotone Convergence Theorem (Lebesgue)|§20.7]], [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|§21.1]]

> [!remark] Remark: The Nonnegativity Assumption Can Be Dropped
> Once the [[§22 The General Lebesgue Integral#^def-22-1|general Lebesgue integral]] and its [[§22 The General Lebesgue Integral#^thm-22-2|linearity]] are available ([[§22 The General Lebesgue Integral|§22]]), the nonnegativity assumption is unnecessary. For a decreasing sequence $f_1 \geq f_2 \geq \cdots$ of *any* measurable functions with $f_1 \in L(E)$, the same conclusion holds. The proof is identical: define $g_k = f_1 - f_k \geq 0$ (nonneg because $f_k \leq f_1$, *not* because $f_k \geq 0$), apply the increasing MCT to $g_k \nearrow f_1 - f$, then use linearity of the integral to cancel $\int f_1 < \infty$.
>
> This reflects a general pattern:
>
> | | **Increasing** | **Decreasing** |
> |---|---|---|
> | **Condition** | $f_k \geq 0$ (lower bound) | $f_1 \in L$ (integrable upper bound) |
> | **Why** | Integrals well-defined (can be $+\infty$) | Need to subtract; $\infty - \infty$ undefined |
> | **Compare** | [[Continuity of Measure\|Cont. of measure from below]] | [[§13 Approximation and Continuity of Measure#^prop-13-5\|Cont. of measure from above]] ($m(E_1) < \infty$) |
>
> The increasing case needs a lower bound to ensure integrals exist; the decreasing case needs an *integrable* upper bound to allow subtraction.

^rem-21-5

> [!remark] Remark: Why the Finiteness Hypothesis is Necessary
> Without the assumption $\int_E f_{k_0}\,dx < \infty$, the conclusion can fail. For example, let $f_k = \chi_{(k, \infty)}$ on $\mathbb{R}$. Then $f_k \searrow 0$ pointwise, but $\int_{\mathbb{R}} f_k\,dx = \infty$ for all $k$, so $\lim \int f_k = \infty \neq 0 = \int 0\,dx$.

^rem-21-6

## Fatou's Lemma

> [!theorem] Theorem §21.8: Fatou's Lemma
> Let $E \in \mathcal{M}$, $E \subseteq \mathbb{R}^n$, and let $\{f_k\}_{k=1}^{\infty}$ be a sequence of non-negative measurable functions on $E$. Then:
>
> $$
> \int_E \liminf_{k \to \infty} f_k(x)\,dx \leq \liminf_{k \to \infty} \int_E f_k(x)\,dx.
> $$

^thm-21-8

> [!proof]+ Proof
> Define $g_l(x) = \inf_{k \geq l} f_k(x)$. Then:
> - Each $g_l$ is non-negative and measurable ([[§16 Limits and Positive Parts of Measurable Functions#^thm-16-1|infimum of measurable functions]]).
> - $\liminf_{k \to \infty} f_k(x) = \lim_{l \to \infty} g_l(x)$ (by [[§16 Limits and Positive Parts of Measurable Functions#^rem-16-4|definition]] of $\liminf$).
> - $g_l(x) \leq g_{l+1}(x)$ for all $x \in E$ (as $l$ increases, the infimum is taken over fewer terms).
>
> By the [[Monotone Convergence Theorem (Lebesgue)|MCT]] applied to the increasing sequence $\{g_l\}$:
>
> $$
> \int_E \liminf_{k \to \infty} f_k\,dx = \int_E \lim_{l \to \infty} g_l\,dx = \lim_{l \to \infty} \int_E g_l\,dx.
> $$
>
> Since $g_l(x) = \inf_{k \geq l} f_k(x) \leq f_k(x)$ for all $k \geq l$, [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|monotonicity of the integral]] gives:
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

^pf-21-8

*Uses:* [[§16 Limits and Positive Parts of Measurable Functions#^thm-16-1|§16.1]], [[§16 Limits and Positive Parts of Measurable Functions#^rem-16-4|Rem. §12.4]], [[Monotone Convergence Theorem (Lebesgue)|§20.7]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[§10 Monotone Sequences and Cauchy Sequences#^def-10-3|451 Def. §10.3]]

> [!example] Example §21.1: Fatou's Inequality Can Be Strict
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

^ex-21-1

![[m551-14-3.svg]]
*Fatou's inequality is strict for $f_k = k\,\chi_{(0,1/k)}$, shown for $k = 1, 2, 4, 8$. Every rectangle has area $\int_0^1 f_k = 1$ (hollow dots: the intervals are open), but they get thinner and each fixed $x$ is eventually outside all of them, so $\lim f_k = 0$ everywhere. The mass piles up at $0$ and vanishes in the limit.*

> [!remark]- Connections
> - The same escaping-mass phenomenon in MATH 451: [[§25 More on Uniform Convergence#^ex-25-1|451 Ex. §25.1]] (the escaping triangle), where the convergence is pointwise but not uniform.
> - No integrable dominator exists here, so the [[Dominated Convergence Theorem|DCT]] does not apply.

> [!example] Example §21.2: Covering Lemma via Integration
> Let $E_1, \ldots, E_n \subseteq [0,1]$ be measurable. Assume every point $x \in [0,1]$ belongs to at least $l$ of the sets $E_k$, $1 \leq k \leq n$. Then at least one $E_i$ has $m(E_i) \geq l/n$.
>
> *Proof.* The hypothesis says $\sum_{k=1}^{n} \chi_{E_k}(x) \geq l$ for all $x \in [0,1]$. Integrating:
>
> $$
> \sum_{k=1}^{n} m(E_k) = \int_0^1 \sum_{k=1}^{n} \chi_{E_k}(x)\,dx \geq \int_0^1 l\,dx = l.
> $$
>
> Since $\sum_{k=1}^n m(E_k) \geq l$, by the pigeonhole principle there exists $1 \leq i \leq n$ with $m(E_i) \geq l/n$.

^ex-21-2

*Uses:* [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|§21.1]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[§20 The Lebesgue Integral for Simple Functions#^def-20-1|Def. §20.1]]

> [!remark] Remark: Why Sup and Not Inf in the Definition of the Integral?
> For $f \geq 0$ measurable, the integral is defined as:
>
> $$
> \int_E f\,dx = \sup\left\{\int_E h\,dx \;\middle|\; 0 \leq h \leq f,\; h \text{ simple}\right\}.
> $$
>
> One might ask: why not instead take $\inf\!\left\{\int_E h\,dx \mid h \geq f,\; h \text{ simple}\right\}$? The answer is that this infimum does not work in general. For instance, if one tried to define it for $f = \chi_V$ where $V$ is a [[§14 The Vitali Set and the Cantor Set#^def-14-3|Vitali set]] (not measurable, so $\chi_V$ lies outside the scope of the definition), any simple function $h \geq f$ satisfies $h \geq \chi_V$, but the integral of $h$ does not “see” $V$ in a controlled way. More fundamentally, the sup definition builds the integral from below using functions we understand completely (simple functions), and the [[Monotone Convergence Theorem (Lebesgue)|MCT]] guarantees this sup equals the “true” integral. The inf approach would require an analogous convergence theorem from above, which does not hold without additional integrability hypotheses.

^rem-21-7

> [!remark]- Connections
> - The Riemann integral uses both sides (upper and lower Darboux integrals must agree): [[§8 Motivation꞉ The Riemann Integral#^rem-8-1|Rem. §8.1]], [[§32 The Definition of the Riemann Integral#^def-32-5|451 Def. §32.5]]. The Vitali set is non-measurable by [[The Vitali Set is Not Measurable|Theorem §14.6]].

*Chain (Vitali set):* ← [[§19 ℚ, Vitali and Cantor Sets, xᵏ and Escaping Mass#The Vitali Set|Chapter 3]]
