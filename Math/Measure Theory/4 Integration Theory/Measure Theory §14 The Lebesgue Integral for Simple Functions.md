---
type: section
subject: "[[Measure Theory]]"
chapter: 4
section: 14
tags: [measure-theory, math551]
---
← [[Measure Theory §13 Egorov's and Lusin's Theorems]] · ↑ [[Measure Theory — 4 Integration Theory]] · [[Measure Theory §15 The General Lebesgue Integral]] →

## Definition and Well-Definedness

> [!definition] Definition §14.1: Lebesgue Integral of a Non-Negative Simple Function
> Let $h$ be a non-negative measurable [[Measure Theory §12 Measurable Functions#^def-12-6|simple function]] on $\mathbb{R}^n$, let $E \in \mathcal{M}$, $E \subseteq \mathbb{R}^n$. Write
>
> $$
> h(x) = \sum_{j=1}^{p} a_j \, \chi_{A_j}(x),
> $$
>
> where $a_j \geq 0$, the sets $A_j$ are pairwise disjoint ($A_i \cap A_j = \emptyset$ for $i \neq j$), and $\bigcup_{j=1}^{p} A_j = \mathbb{R}^n$. Then the **Lebesgue integral** (or **L-integral**) of $h$ over $E$ is defined by:
>
> $$
> \int_E h(x)\,dx = \sum_{j=1}^{p} a_j \, m(A_j \cap E).
> $$

^def-14-1

> [!remark]- Connections
> - The representation with disjoint $A_j$ is the [[Measure Theory §12 Measurable Functions#^prop-12-13|canonical representation]] (Prop. §12.13); $m$ is [[Measure Theory §10 Lebesgue Measurable Sets#^def-10-5|Lebesgue measure]] (Def. §10.5).
> - For $h$ a step function on $[a,b]$ this is a Riemann sum: [[Measure Theory §8 Motivation꞉ The Riemann Integral#^def-8-2|Def. §8.2]], [[Single Variable Analysis §32 The Definition of the Riemann Integral#^ex-32-2|451 Ex. §32.2]].

> [!remark] Remark: Well-Definedness
> A simple function can be written in multiple ways as a linear combination of characteristic functions. We must verify that the integral does not depend on the particular representation.
>
> Suppose $h(x) = a\,\chi_{A_1} + a\,\chi_{A_2}$ with $A_1 \cap A_2 = \emptyset$. Then $h = a\,\chi_{A_1 \cup A_2}$, and:
>
> $$
> \int_E h\,dx = a\,m(A_1 \cap E) + a\,m(A_2 \cap E) = a\,m((A_1 \cup A_2) \cap E) = \int_E h\,dx,
> $$
>
> where the second equality uses [[Measure Theory §10 Lebesgue Measurable Sets#^lem-10-2|finite additivity of measure]] (since $A_1 \cap E$ and $A_2 \cap E$ are disjoint measurable sets). More generally, any two representations of $h$ can be refined to a common partition, and additivity of measure ensures the integral is the same.

^rem-14-1

## Linearity of the Integral for Simple Functions

> [!theorem] Proposition §14.1: Linearity
> Let $h_1, h_2$ be non-negative simple measurable functions on $\mathbb{R}^n$, and let $\alpha, \beta \geq 0$. Let $E \in \mathcal{M}$, $E \subseteq \mathbb{R}^n$. Then:
>
> $$
> \int_E \bigl(\alpha\, h_1(x) + \beta\, h_2(x)\bigr)\,dx = \alpha \int_E h_1(x)\,dx + \beta \int_E h_2(x)\,dx.
> $$

^prop-14-1

> [!proof]+ Proof
> **Scalar multiplication**: Let $h$ be non-negative simple measurable and $\alpha > 0$. Then $\int_E \alpha\, h\,dx = \alpha \int_E h\,dx$ by pulling $\alpha$ outside the sum in the [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^def-14-1|definition]].
>
> **Additivity**: Write $h_1(x) = \sum_{j=1}^{p} a_j \, \chi_{A_j}(x)$ and $h_2(x) = \sum_{k=1}^{q} b_k \, \chi_{B_k}(x)$, where $\{A_j\}$ and $\{B_k\}$ are partitions of $\mathbb{R}^n$ into pairwise disjoint measurable sets:
>
> $$
> A_i \cap A_j = \emptyset \;\text{for}\; i \neq j, \quad B_k \cap B_l = \emptyset \;\text{for}\; k \neq l, \quad \bigcup_{j=1}^{p} A_j = \bigcup_{k=1}^{q} B_k = \mathbb{R}^n.
> $$
>
> Form the common refinement: define $C_{jk} = A_j \cap B_k$. Then $\{C_{jk}\}_{j,k}$ is a partition of $\mathbb{R}^n$ into pairwise disjoint measurable sets, and:
>
> $$
> h_1(x) + h_2(x) = \sum_{j=1}^{p} \sum_{k=1}^{q} (a_j + b_k)\,\chi_{C_{jk}}(x).
> $$
>
> Therefore:
>
> $$
> \begin{aligned}
> \int_E (h_1 + h_2)\,dx &= \sum_{j=1}^{p} \sum_{k=1}^{q} (a_j + b_k)\,m(C_{jk} \cap E) \\
> &= \sum_{j=1}^{p} \sum_{k=1}^{q} a_j\,m(A_j \cap B_k \cap E) + \sum_{j=1}^{p} \sum_{k=1}^{q} b_k\,m(A_j \cap B_k \cap E) \\
> &= \sum_{j=1}^{p} a_j \sum_{k=1}^{q} m(A_j \cap B_k \cap E) + \sum_{k=1}^{q} b_k \sum_{j=1}^{p} m(A_j \cap B_k \cap E).
> \end{aligned}
> $$
>
> By [[Measure Theory §10 Lebesgue Measurable Sets#^lem-10-2|additivity of measure]], since $\{B_k\}$ partitions $\mathbb{R}^n$:
>
> $$
> \sum_{k=1}^{q} m(A_j \cap B_k \cap E) = m\!\left(A_j \cap E \cap \bigcup_{k=1}^{q} B_k\right) = m(A_j \cap E).
> $$
>
> Similarly, $\sum_{j=1}^{p} m(A_j \cap B_k \cap E) = m(B_k \cap E)$. Therefore:
>
> $$
> \int_E (h_1 + h_2)\,dx = \sum_{j=1}^{p} a_j\,m(A_j \cap E) + \sum_{k=1}^{q} b_k\,m(B_k \cap E) = \int_E h_1\,dx + \int_E h_2\,dx.
> $$

^pf-14-1

*Uses:* [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]], [[Measure Theory §10 Lebesgue Measurable Sets#^lem-10-2|§10.2]]

## Domain Properties

> [!theorem] Proposition §14.2: Restriction and Null Sets
> Let $h$ be a non-negative simple measurable function on $\mathbb{R}^n$, let $E \subseteq \mathbb{R}^n$ with $E \in \mathcal{M}$, and let $A \subseteq E$ with $A \in \mathcal{M}$. Then:
> - (i) $\displaystyle\int_E h(x)\,\chi_A(x)\,dx = \int_A h(x)\,dx$.
> - (ii) If $m(E) = 0$, then $\displaystyle\int_E h(x)\,dx = 0$.

^prop-14-2

> [!proof]+ Proof
> **(i)** Write $h(x) = \sum_{j=1}^{p} a_j\,\chi_{A_j}(x)$ with $\{A_j\}$ a partition of $\mathbb{R}^n$. Then:
>
> $$
> h(x)\,\chi_A(x) = \sum_{j=1}^{p} a_j\,\chi_{A_j}(x)\,\chi_A(x) = \sum_{j=1}^{p} a_j\,\chi_{A_j \cap A}(x).
> $$
>
> Therefore:
>
> $$
> \int_E h(x)\,\chi_A(x)\,dx = \sum_{j=1}^{p} a_j\,m(A_j \cap A \cap E) = \sum_{j=1}^{p} a_j\,m(A_j \cap A) = \int_A h(x)\,dx,
> $$
>
> where the second equality uses $A \subseteq E$, so $A_j \cap A \cap E = A_j \cap A$.
>
> **(ii)** If $m(E) = 0$, then $m(A_j \cap E) \leq m(E) = 0$ for each $j$, so:
>
> $$
> \int_E h(x)\,dx = \sum_{j=1}^{p} a_j \cdot 0 = 0.
> $$

^pf-14-2

*Uses:* [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]], [[Measure Theory §12 Measurable Functions#^def-12-3|Def. §12.3]], [[Properties of Lebesgue Outer Measure|§9.1]]

## The Integral for Non-Negative Measurable Functions

We now extend the integral from simple functions to general non-negative measurable functions.

> [!definition] Definition §14.2: Lebesgue Integral of a Non-Negative Measurable Function
> Let $E \subseteq \mathbb{R}^n$, $E \in \mathcal{M}$. Let $f$ be a non-negative [[Measure Theory §12 Measurable Functions#^def-12-2|measurable function]] on $E$. We define:
>
> $$
> \int_E f(x)\,dx = \sup\left\{\int_E h(x)\,dx \;\middle|\; h \text{ non-negative simple measurable on } \mathbb{R}^n,\; h(x) \leq f(x) \;\forall\, x \in E\right\}.
> $$

^def-14-2

> [!remark]- Connections
> - The same “sup from below” shape as the lower Darboux integral: [[Measure Theory §8 Motivation꞉ The Riemann Integral#^rem-8-1|Rem. §8.1]], [[Single Variable Analysis §32 The Definition of the Riemann Integral#^def-32-2|451 Def. §32.2]].

> [!remark] Remark: Why Not Use Approximating Sequences?
> One might try to define $\int_E f\,dx$ as $\lim \int_E h_k\,dx$ for some sequence of simple functions $h_k \nearrow f$. The issue is that we are not yet guaranteed that different approximating sequences give the same limit. The supremum definition avoids this ambiguity. The [[Monotone Convergence Theorem (Lebesgue)|Monotone Convergence Theorem]] below will justify the sequential approach.

^rem-14-2

> [!remark] Remark: Generalization Beyond $\mathbb{R}^n$
> Although we state everything for Lebesgue measure on $\mathbb{R}^n$, nothing in the definitions or proofs above uses the structure of $\mathbb{R}^n$. The simple function integral $\sum a_j\,m(A_j \cap E)$ requires only a measure on a $\sigma$-algebra; the supremum definition requires only measurable functions and the simple integral; the MCT proof uses only monotonicity and [[Continuity of Measure|continuity of measure from below]]—all of which hold in any [[Measure Theory §11 Borel Sets and Measure Spaces#^def-11-7|measure space]] $(X, \mathcal{A}, \mu)$. Replacing $m$ by $\mu$ and writing $\int_E f\,d\mu$ instead of $\int_E f\,dx$, the entire theory (linearity, MCT, and the results that follow) carries over verbatim. The role of $\mathbb{R}^n$ is confined to the *construction* of Lebesgue measure; once we have a measure space in hand, integration theory is purely abstract.

^rem-14-3

> [!theorem] Proposition §14.3: Basic Properties
> Let $f, g$ be non-negative measurable functions on $E \in \mathcal{M}$, $E \subseteq \mathbb{R}^n$. Then:
> - (i) **Monotonicity**: If $f(x) \leq g(x)$ for all $x \in E$, then $\int_E f\,dx \leq \int_E g\,dx$.
> - (ii) **Null sets**: If $m(E) = 0$, then $\int_E f\,dx = 0$.

^prop-14-3

> [!proof]+ Proof
> **(i)** Every simple $h \leq f$ on $E$ also satisfies $h \leq g$ on $E$, so the supremum over $\{h : h \leq f\}$ is at most the supremum over $\{h : h \leq g\}$.
>
> **(ii)** For any simple $h \leq f$ on $E$, we have $\int_E h\,dx = 0$ since $m(E) = 0$ (by the [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-2|domain property for simple functions]]). Thus the supremum is $0$.

^pf-14-3

*Uses:* [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^def-14-2|Def. §14.2]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-2|§14.2]]

## The Monotone Convergence Theorem

> [!theorem] Theorem §14.4: Monotone Convergence Theorem (MCT)
> Let $E \subseteq \mathbb{R}^n$, $E \in \mathcal{M}$. Let $\{f_k\}_{k=1}^{\infty}$ be an increasing sequence of non-negative measurable functions on $E$:
>
> $$
> 0 \leq f_1(x) \leq f_2(x) \leq \cdots \quad \text{for all } x \in E.
> $$
>
> Then:
>
> $$
> \lim_{k \to \infty} \int_E f_k(x)\,dx = \int_E \lim_{k \to \infty} f_k(x)\,dx.
> $$

^thm-14-4

> [!proof]+ Proof
> Define $f(x) = \lim_{k \to \infty} f_k(x)$. Since $\{f_k\}$ is an increasing sequence of non-negative measurable functions, $f$ is measurable (as the [[Measure Theory §12 Measurable Functions#^cor-12-8|pointwise limit of measurable functions]]) and $f(x) \geq 0$.
>
> **Step 1: $\lim_{k \to \infty} \int_E f_k\,dx \leq \int_E f\,dx$.**
>
> By [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|monotonicity of the integral]]: since $f_k(x) \leq f_{k+1}(x) \leq \cdots \leq f(x)$ for all $x \in E$, we have
>
> $$
> \int_E f_k\,dx \leq \int_E f_{k+1}\,dx \leq \cdots \leq \int_E f\,dx.
> $$
>
> The sequence $\left\{\int_E f_k\,dx\right\}$ is [[Monotone Convergence Theorem|increasing and bounded above]] by $\int_E f\,dx$, so:
>
> $$
> \lim_{k \to \infty} \int_E f_k\,dx \leq \int_E f\,dx.
> $$
>
> **Step 2: $\lim_{k \to \infty} \int_E f_k\,dx \geq \int_E f\,dx$.**
>
> By [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^def-14-2|definition]], $\int_E f\,dx = \sup\bigl\{\int_E h\,dx \mid h \text{ simple, } 0 \leq h \leq f \text{ on } E\bigr\}$. It suffices to show that for every simple non-negative measurable $h$ with $h(x) \leq f(x)$ for all $x \in E$:
>
> $$
> \int_E h\,dx \leq \lim_{k \to \infty} \int_E f_k\,dx.
> $$
>
> We prove this via the following lemma.

^pf-14-4

*Uses:* [[Measure Theory §12 Measurable Functions#^cor-12-8|§12.8]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^def-14-2|Def. §14.2]], [[Monotone Convergence Theorem|451 §10.1]]

> [!theorem] Lemma §14.5: Integral over Increasing Sets
> Let $E_1 \subseteq E_2 \subseteq \cdots$ be an increasing sequence of measurable sets with $E = \bigcup_{k=1}^{\infty} E_k$. Let $h$ be a non-negative simple measurable function on $\mathbb{R}^n$. Then:
>
> $$
> \int_E h\,dx = \lim_{k \to \infty} \int_{E_k} h\,dx.
> $$

^lem-14-5

> [!proof]+ Proof of Lemma
> Write $h(x) = \sum_{j=1}^{p} a_j\,\chi_{A_j}(x)$. Then:
>
> $$
> \int_{E_k} h\,dx = \sum_{j=1}^{p} a_j\,m(A_j \cap E_k) \xrightarrow{k \to \infty} \sum_{j=1}^{p} a_j\,m(A_j \cap E) = \int_E h\,dx,
> $$
>
> where the limit uses [[Continuity of Measure|continuity of measure from below]]: since $A_j \cap E_k \nearrow A_j \cap E$, we have $m(A_j \cap E_k) \to m(A_j \cap E)$.

^pf-14-5

*Uses:* [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]], [[Continuity of Measure|§11.12]]

> [!proof]+ Proof of the MCT (continued)
> **Applying the lemma.** Fix $c \in (0, 1)$ and define:
>
> $$
> E_k = \{x \in E \mid f_k(x) \geq c\,h(x)\}.
> $$
>
> *$E_k$ is measurable*: Since $f_k$ and $h$ are measurable, [[Measure Theory §12 Measurable Functions#^thm-12-3|so is]] $f_k - c\,h$, and $E_k = \{f_k - c\,h \geq 0\} \cap E$ is measurable.
>
> *$E_k \subseteq E_{k+1}$*: If $f_k(x) \geq c\,h(x)$, then $f_{k+1}(x) \geq f_k(x) \geq c\,h(x)$, so $x \in E_{k+1}$.
>
> *$\bigcup_{k=1}^{\infty} E_k = E$*: Let $x_0 \in E$.
>
> - If $h(x_0) = 0$: then $f_k(x_0) \geq 0 = c \cdot 0 = c\,h(x_0)$ for all $k$, so $x_0 \in E_k$ for all $k$.
> - If $h(x_0) > 0$: then $f(x_0) \geq h(x_0) > 0$ (since $h \leq f$). Since $\lim_{k \to \infty} f_k(x_0) = f(x_0)$ and $c\,h(x_0) < h(x_0) \leq f(x_0)$, there exists $l$ large enough such that $f_k(x_0) \geq c\,h(x_0)$ for all $k \geq l$. Hence $x_0 \in \bigcup_{k=1}^{\infty} E_k$.
>
> Now, on $E_k$ we have $f_k(x) \geq c\,h(x)$ by definition. Since $E_k \subseteq E$, [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^cor-14-7|monotonicity of the domain]] gives $\int_E f_k\,dx \geq \int_{E_k} f_k\,dx$. Since $f_k \geq c\,h$ on $E_k$, monotonicity of the integrand ([[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|Proposition §14.3(i)]]) gives $\int_{E_k} f_k\,dx \geq \int_{E_k} c\,h\,dx = c\int_{E_k} h\,dx$. Combining:
>
> $$
> \int_E f_k\,dx \geq \int_{E_k} f_k\,dx \geq c \int_{E_k} h\,dx.
> $$
>
> Taking $k \to \infty$ and applying the [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^lem-14-5|lemma]]:
>
> $$
> \lim_{k \to \infty} \int_E f_k\,dx \geq c \int_E h\,dx.
> $$
>
> This holds for all $c \in (0, 1)$. Letting $c \to 1^-$:
>
> $$
> \lim_{k \to \infty} \int_E f_k\,dx \geq \int_E h\,dx.
> $$
>
> Since this holds for every simple $h$ with $0 \leq h \leq f$ on $E$, taking the supremum:
>
> $$
> \lim_{k \to \infty} \int_E f_k\,dx \geq \sup\left\{\int_E h\,dx\right\} = \int_E f\,dx.
> $$
>
> Combining Steps 1 and 2: $\displaystyle\lim_{k \to \infty} \int_E f_k\,dx = \int_E f\,dx$.

^pf-14-4-cont

*Uses:* [[Measure Theory §12 Measurable Functions#^thm-12-3|§12.3]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^cor-14-7|§14.7]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-1|§14.1]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^lem-14-5|§14.5]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^def-14-2|Def. §14.2]]

> [!remark]- Connections
> - Not to be confused with the MATH 451 [[Monotone Convergence Theorem]] for sequences of numbers, which it uses in Step 1.
> - The Riemann integral has no such theorem: [[Measure Theory §8 Motivation꞉ The Riemann Integral#^rem-8-2|Rem. §8.2]] (increasing $f_n \nearrow$ Dirichlet function). Riemann-side exchange of limit and integral needs uniform convergence: [[Single Variable Analysis §33 Properties of the Riemann Integral#^thm-33-12|451 §33.12]].
> - Summarized with Fatou and DCT in [[Measure Theory §15 The General Lebesgue Integral#^rem-15-3|Rem. §15.3]]; the $L^p$ theory ([[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces|§19]]) and Tonelli ([[Tonelli's Theorem|§17.3]]) build on it.

## Consequences of the MCT

> [!theorem] Proposition §14.6: Domain Restriction for General Non-Negative Functions
> Let $E \in \mathcal{M}$, $E \subseteq \mathbb{R}^n$. Let $f$ be a non-negative measurable function on $E$, and let $A \subseteq E$ with $A \in \mathcal{M}$. Then:
>
> $$
> \int_A f(x)\,dx = \int_E f(x)\,\chi_A(x)\,dx.
> $$

^prop-14-6

> [!proof]+ Proof
> We show both inequalities.
>
> **($\leq$):** Let $h$ be a non-negative simple measurable function with $0 \leq h(x) \leq f(x)$ for all $x \in A$. Then $h(x)\,\chi_A(x) \leq f(x)\,\chi_A(x)$ for all $x \in E$ (on $A^c$, both sides are $0$; on $A$, $h \leq f$). Since $h\,\chi_A$ is simple:
>
> $$
> \int_A h\,dx = \int_E h\,\chi_A\,dx \leq \int_E f\,\chi_A\,dx,
> $$
>
> where the equality uses the [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-2|domain restriction property for simple functions]] and the inequality uses [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|monotonicity]]. Taking the supremum over all such $h$: $\int_A f\,dx \leq \int_E f\,\chi_A\,dx$.
>
> **($\geq$):** Let $h$ be a non-negative simple measurable function with $0 \leq h(x) \leq f(x)\,\chi_A(x)$ for all $x \in E$. Then for $x \in A^c$, $h(x) = 0$, so $h(x) = h(x)\,\chi_A(x)$ for all $x \in E$. On $A$, $h(x) \leq f(x)$. Thus:
>
> $$
> \int_E h\,dx = \int_E h\,\chi_A\,dx = \int_A h\,dx \leq \int_A f\,dx.
> $$
>
> Taking the supremum: $\int_E f\,\chi_A\,dx \leq \int_A f\,dx$.

^pf-14-6

*Uses:* [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^def-14-2|Def. §14.2]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-2|§14.2]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]]

> [!theorem] Corollary §14.7: Domain Monotonicity
> Let $E \in \mathcal{M}$, $A \subseteq E$, $A \in \mathcal{M}$, and $f$ a non-negative measurable function on $E$. Then:
>
> $$
> \int_A f\,dx \leq \int_E f\,dx.
> $$

^cor-14-7

> [!proof]+ Proof
> Since $f(x) \geq 0$, we have $f(x)\,\chi_A(x) \leq f(x)$ for all $x \in E$. By [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|monotonicity of the integrand]] and the [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-6|domain restriction formula]]:
>
> $$
> \int_A f\,dx = \int_E f\,\chi_A\,dx \leq \int_E f\,dx.
> $$

^pf-14-7

*Uses:* [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-6|§14.6]]

> [!theorem] Theorem §14.8: Linearity of the Integral
> Let $f, g$ be non-negative measurable functions on $E$, $E \in \mathcal{M}$, and $c \geq 0$. Then:
> - (i) $\displaystyle\int_E c\,f(x)\,dx = c\int_E f(x)\,dx$.
> - (ii) $\displaystyle\int_E \bigl(f(x) + g(x)\bigr)\,dx = \int_E f(x)\,dx + \int_E g(x)\,dx$.

^thm-14-8

> [!proof]+ Proof
> **(i)** If $c = 0$, both sides are $0$ (using the [[Measure Theory §12 Measurable Functions#^rem-12-1|convention]] $0 \cdot \infty = 0$). Assume $c > 0$. By definition:
>
> $$
> \int_E c\,f\,dx = \sup\left\{\int_E h\,dx \;\middle|\; h \text{ simple},\; 0 \leq h \leq c\,f \text{ on } E\right\}.
> $$
>
> We show both inequalities.
>
> *$(\leq)$*: Let $h$ be simple with $0 \leq h \leq c\,f$ on $E$. Then $h/c$ is simple with $0 \leq h/c \leq f$ on $E$, so $\int_E (h/c)\,dx \leq \int_E f\,dx$. By [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-1|linearity for simple functions]], $\int_E h\,dx = c\int_E (h/c)\,dx \leq c\int_E f\,dx$. Taking the supremum over all such $h$: $\int_E c\,f\,dx \leq c\int_E f\,dx$.
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

*Uses:* [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^def-14-2|Def. §14.2]], [[Measure Theory §12 Measurable Functions#^rem-12-1|Rem. §12.1]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-1|§14.1]], [[Simple Function Approximation Theorem|§12.14]], [[Monotone Convergence Theorem (Lebesgue)|§14.4]]

> [!remark]- Connections
> - Riemann counterpart: [[Single Variable Analysis §33 Properties of the Riemann Integral#^thm-33-2|451 §33.2]]; extended to signed integrable functions in [[Measure Theory §15 The General Lebesgue Integral#^thm-15-2|Theorem §15.2]].

> [!theorem] Proposition §14.9: Integral over Null Sets and A.E. Equal Functions
> Let $f, g$ be non-negative measurable functions on $E \in \mathcal{M}$.
> - (i) If $m(E) = 0$, then $\int_E f\,dx = 0$.
> - (ii) If $f(x) = g(x)$ [[Measure Theory §12 Measurable Functions#^def-12-5|a.e.]] on $E$, then $\int_E f\,dx = \int_E g\,dx$.

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

*Uses:* [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-2|§14.2]], [[Measure Theory §12 Measurable Functions#^def-12-5|Def. §12.5]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-8|§14.8]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-6|§14.6]]

> [!theorem] Proposition §14.10: Integrability Implies A.E. Finiteness
> Let $f \geq 0$ be measurable on $E \in \mathcal{M}$. If $f$ is integrable on $E$ (i.e., $\int_E f\,dx < \infty$), then $f$ is a.e. finite on $E$. (We adopt the convention $0 \cdot \infty = 0$.)

^prop-14-10

> [!proof]+ Proof
> Let $E_0 = \{x \in E : f(x) = +\infty\}$. We want to show $m(E_0) = 0$.
>
> Since $f(x) \geq f(x)\,\chi_{E \setminus E_0}(x) \geq f(x)\,\chi_{E_0}(x) \geq k\,\chi_{E_0}(x)$ for all $k \in \mathbb{N}$ (because $f = +\infty$ on $E_0$):
>
> $$
> \infty > \int_E f\,dx \geq \int_{E_0} f\,dx \geq \int_E k\,\chi_{E_0}\,dx = k\,m(E_0).
> $$
>
> Thus $m(E_0) \leq \frac{\int_E f\,dx}{k} \to 0$ as $k \to \infty$. Hence $m(E_0) = 0$.

^pf-14-10

*Uses:* [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^cor-14-7|§14.7]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-6|§14.6]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]]

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

*Uses:* [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^cor-14-7|§14.7]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[Properties of Lebesgue Outer Measure|§9.1]]

> [!remark]- Connections
> - Riemann version (continuous $f \geq 0$ with $\int_a^b f = 0$ is identically $0$): [[Single Variable Analysis §33 Properties of the Riemann Integral#^thm-33-7|451 §33.7]]. Without continuity, "$\equiv 0$" weakens to "$= 0$ a.e.".
> - Signed version: [[Measure Theory §15 The General Lebesgue Integral#^prop-15-5|Proposition §15.5]]; used in the proof of [[Riemann Integrable Implies Lebesgue Integrable|Theorem §15.10]] and for $\|f\|_1 = 0$ in [[Measure Theory §16 The L¹ Space and Density Theorems#^thm-16-4|Theorem §16.4]].

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
> where the second equality uses [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-8|linearity of the integral]] for finite sums.

^pf-14-12

*Uses:* [[Monotone Convergence Theorem (Lebesgue)|§14.4]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-8|§14.8]]

> [!remark]- Connections
> - Contrast with MATH 451, where term-by-term integration of a series needs uniform convergence ([[Single Variable Analysis §33 Properties of the Riemann Integral#^thm-33-12|451 §33.12]], e.g. via the [[Single Variable Analysis §25 More on Uniform Convergence#^thm-25-3|Weierstrass M-test]]).
> - Signed version: [[Measure Theory §15 The General Lebesgue Integral#^cor-15-9|Corollary §15.9]].

> [!theorem] Corollary §14.13: Countable Additivity of the Integral over Disjoint Sets
> Let $\{E_k\}_{k=1}^{\infty}$ be a sequence of pairwise disjoint measurable sets in $\mathbb{R}^n$, and let $E = \bigcup_{k=1}^{\infty} E_k$. If $f$ is a non-negative measurable function, then:
>
> $$
> \int_E f\,dx = \sum_{k=1}^{\infty} \int_{E_k} f\,dx.
> $$

^cor-14-13

> [!proof]+ Proof
> Define $f_k(x) = f(x)\,\chi_{E_k}(x)$. Since the $E_k$ are pairwise disjoint, $f(x) = \sum_{k=1}^{\infty} f_k(x)$ for all $x \in E$. By [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-12|MCT II]]:
>
> $$
> \int_E f\,dx = \int_E \sum_{k=1}^{\infty} f_k\,dx = \sum_{k=1}^{\infty} \int_E f_k\,dx = \sum_{k=1}^{\infty} \int_{E_k} f\,dx,
> $$
>
> where the last equality uses $\int_E f_k\,dx = \int_E f\,\chi_{E_k}\,dx = \int_{E_k} f\,dx$.

^pf-14-13

*Uses:* [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-12|§14.12]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-6|§14.6]]

## The Induced Measure

> [!definition] Definition §14.3: Measure Induced by a Non-Negative Function
> Let $f$ be a non-negative measurable function on $\mathbb{R}^n$. Define $\nu: \mathcal{M} \to [0, \infty]$ by:
>
> $$
> \nu(E) = \int_E f(x)\,dx, \qquad E \in \mathcal{M}.
> $$
>
> Then $\nu$ is a [[Measure Theory §11 Borel Sets and Measure Spaces#^def-11-6|measure]] on $(\mathbb{R}^n, \mathcal{M})$.

^def-14-3

> [!remark] Remark
> To verify that $\nu$ is a measure, we check the axioms:
> - (i) $\nu(\emptyset) = \int_\emptyset f\,dx = 0$ ([[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-9|integral over null set]]).
> - (ii) $\nu(E) \geq 0$ for all $E \in \mathcal{M}$ (since $f \geq 0$).
> - (iii) **Countable additivity**: If $\{E_k\}$ are pairwise disjoint measurable sets, then by the [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^cor-14-13|corollary above]]:
>
> $$
> \nu\!\left(\bigcup_{k=1}^{\infty} E_k\right) = \int_{\bigcup E_k} f\,dx = \sum_{k=1}^{\infty} \int_{E_k} f\,dx = \sum_{k=1}^{\infty} \nu(E_k).
> $$
>
> Note that $\nu$ depends on $f$ and is sometimes written $d\nu = f\,dx$. If $f = 1$, then $\nu(E) = m(E)$, recovering Lebesgue measure.

^rem-14-4

> [!remark]- Connections
> - Signed analogue for $f \in L(E)$: [[Measure Theory §15 The General Lebesgue Integral#^rem-15-2|Rem. §15.2]]. Its "small sets have small $\nu$-measure" property is [[Measure Theory §16 The L¹ Space and Density Theorems#^thm-16-1|Theorem §16.1]].

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

> [!remark] Remark: The Nonnegativity Assumption Can Be Dropped
> Once the [[Measure Theory §15 The General Lebesgue Integral#^def-15-1|general Lebesgue integral]] and its [[Measure Theory §15 The General Lebesgue Integral#^thm-15-2|linearity]] are available ([[Measure Theory §15 The General Lebesgue Integral|§15]]), the nonnegativity assumption is unnecessary. For a decreasing sequence $f_1 \geq f_2 \geq \cdots$ of *any* measurable functions with $f_1 \in L(E)$, the same conclusion holds. The proof is identical: define $g_k = f_1 - f_k \geq 0$ (nonneg because $f_k \leq f_1$, *not* because $f_k \geq 0$), apply the increasing MCT to $g_k \nearrow f_1 - f$, then use linearity of the integral to cancel $\int f_1 < \infty$.
>
> This reflects a general pattern:
>
> | | **Increasing** | **Decreasing** |
> |---|---|---|
> | **Condition** | $f_k \geq 0$ (lower bound) | $f_1 \in L$ (integrable upper bound) |
> | **Why** | Integrals well-defined (can be $+\infty$) | Need to subtract; $\infty - \infty$ undefined |
> | **Compare** | [[Continuity of Measure\|Cont. of measure from below]] | [[Measure Theory §11 Borel Sets and Measure Spaces#^prop-11-13\|Cont. of measure from above]] ($m(E_1) < \infty$) |
>
> The increasing case needs a lower bound to ensure integrals exist; the decreasing case needs an *integrable* upper bound to allow subtraction.

^rem-14-5

> [!remark] Remark: Why the Finiteness Hypothesis is Necessary
> Without the assumption $\int_E f_{k_0}\,dx < \infty$, the conclusion can fail. For example, let $f_k = \chi_{(k, \infty)}$ on $\mathbb{R}$. Then $f_k \searrow 0$ pointwise, but $\int_{\mathbb{R}} f_k\,dx = \infty$ for all $k$, so $\lim \int f_k = \infty \neq 0 = \int 0\,dx$.

^rem-14-6

> [!proof]+ Proof
> Since $\{f_k\}$ is decreasing and $f_k \geq f_{k+1} \geq \cdots \geq f \geq 0$ for $k \geq k_0$, we have $\int_E f_k\,dx \leq \int_E f_{k_0}\,dx < \infty$ for all $k \geq k_0$. The limit depends only on the tail, so we may assume WLOG that $k_0 = 1$.
>
> **Main argument.** Define $g_k = f_1 - f_k$ for $k \geq 1$. Since $f_k$ is decreasing, $g_k$ is an increasing sequence of non-negative measurable functions with $g_k \nearrow f_1 - f$ pointwise. By the (increasing) [[Monotone Convergence Theorem (Lebesgue)|MCT]]:
>
> $$
> \lim_{k \to \infty} \int_E g_k\,dx = \int_E (f_1 - f)\,dx.
> $$
>
> Since $f_1 \geq f_k \geq 0$ and $\int f_k \leq \int f_1 < \infty$, by the [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-8|subtraction rule]] ($\int(f - g) = \int f - \int g$ when $f \geq g \geq 0$ and $\int g < \infty$):
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

*Uses:* [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[Monotone Convergence Theorem (Lebesgue)|§14.4]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-8|§14.8]]

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
> - Each $g_l$ is non-negative and measurable ([[Measure Theory §12 Measurable Functions#^thm-12-6|infimum of measurable functions]]).
> - $\liminf_{k \to \infty} f_k(x) = \lim_{l \to \infty} g_l(x)$ (by [[Measure Theory §12 Measurable Functions#^rem-12-4|definition]] of $\liminf$).
> - $g_l(x) \leq g_{l+1}(x)$ for all $x \in E$ (as $l$ increases, the infimum is taken over fewer terms).
>
> By the [[Monotone Convergence Theorem (Lebesgue)|MCT]] applied to the increasing sequence $\{g_l\}$:
>
> $$
> \int_E \liminf_{k \to \infty} f_k\,dx = \int_E \lim_{l \to \infty} g_l\,dx = \lim_{l \to \infty} \int_E g_l\,dx.
> $$
>
> Since $g_l(x) = \inf_{k \geq l} f_k(x) \leq f_k(x)$ for all $k \geq l$, [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|monotonicity of the integral]] gives:
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

*Uses:* [[Measure Theory §12 Measurable Functions#^thm-12-6|§12.6]], [[Measure Theory §12 Measurable Functions#^rem-12-4|Rem. §12.4]], [[Monotone Convergence Theorem (Lebesgue)|§14.4]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[Single Variable Analysis §10 Monotone Sequences and Cauchy Sequences#^def-10-3|451 Def. §10.3]]

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

> [!remark]- Connections
> - The same escaping-mass phenomenon in MATH 451: [[Single Variable Analysis §25 More on Uniform Convergence#^ex-25-1|451 Ex. §25.1]] (the escaping triangle), where the convergence is pointwise but not uniform.
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

*Uses:* [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-8|§14.8]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]]

> [!remark] Remark: Why Sup and Not Inf in the Definition of the Integral?
> For $f \geq 0$ measurable, the integral is defined as:
>
> $$
> \int_E f\,dx = \sup\left\{\int_E h\,dx \;\middle|\; 0 \leq h \leq f,\; h \text{ simple}\right\}.
> $$
>
> One might ask: why not instead take $\inf\!\left\{\int_E h\,dx \mid h \geq f,\; h \text{ simple}\right\}$? The answer is that this infimum does not work in general. For instance, if $f = \chi_V$ where $V$ is a [[Measure Theory §11 Borel Sets and Measure Spaces#^def-11-12|Vitali set]], any simple function $h \geq f$ satisfies $h \geq \chi_V$, but the integral of $h$ does not “see” $V$ in a controlled way. More fundamentally, the sup definition builds the integral from below using functions we understand completely (simple functions), and the [[Monotone Convergence Theorem (Lebesgue)|MCT]] guarantees this sup equals the “true” integral. The inf approach would require an analogous convergence theorem from above, which does not hold without additional integrability hypotheses.

^rem-14-7

> [!remark]- Connections
> - The Riemann integral uses both sides (upper and lower Darboux integrals must agree): [[Measure Theory §8 Motivation꞉ The Riemann Integral#^rem-8-1|Rem. §8.1]], [[Single Variable Analysis §32 The Definition of the Riemann Integral#^def-32-2|451 Def. §32.2]]. The Vitali set is non-measurable by [[The Vitali Set is Not Measurable|Theorem §11.20]].
