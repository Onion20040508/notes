---
type: section
subject: "[[Measure Theory]]"
chapter: 4
section: 14
tags: [measure-theory, math551]
---
← [[§13 Egorov's and Lusin's Theorems]] · ↑ [[· 4 Integration Theory]] · [[§15 The General Lebesgue Integral]] →

## Definition and Well-Definedness

> [!definition] Definition §14.1: Lebesgue Integral of a Non-Negative Simple Function
> Let $h$ be a non-negative measurable [[§12b Simple Functions and Modes of Convergence#^def-12-6|simple function]] on $\mathbb{R}^n$, let $E \in \mathcal{M}$, $E \subseteq \mathbb{R}^n$. Write
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
> - The representation with disjoint $A_j$ is the [[§12b Simple Functions and Modes of Convergence#^prop-12-13|canonical representation]] ([[§12b Simple Functions and Modes of Convergence#^prop-12-13|Prop. §12.13]]); $m$ is [[§10 Lebesgue Measurable Sets#^def-10-5|Lebesgue measure]] ([[§10 Lebesgue Measurable Sets#^def-10-5|Def. §10.5]]).
> - For $h$ a step function on $[a,b]$ this is a Riemann sum: [[§8 Motivation꞉ The Riemann Integral#^def-8-2|Def. §8.2]], [[§32 The Definition of the Riemann Integral#^ex-32-2|451 Ex. §32.2]].

> [!remark] Remark: Well-Definedness
> A simple function can be written in multiple ways as a linear combination of characteristic functions. We must verify that the integral does not depend on the particular representation.
>
> Suppose $h(x) = a\,\chi_{A_1} + a\,\chi_{A_2}$ with $A_1 \cap A_2 = \emptyset$. Then $h = a\,\chi_{A_1 \cup A_2}$, and:
>
> $$
> \underbrace{a\,m(A_1 \cap E) + a\,m(A_2 \cap E)}_{\text{from } a\,\chi_{A_1} + a\,\chi_{A_2}} = \underbrace{a\,m((A_1 \cup A_2) \cap E)}_{\text{from } a\,\chi_{A_1 \cup A_2}},
> $$
>
> so both representations give the same value of $\int_E h\,dx$, where the equality uses [[§10 Lebesgue Measurable Sets#^lem-10-2|finite additivity of measure]] (since $A_1 \cap E$ and $A_2 \cap E$ are disjoint measurable sets). More generally, any two representations of $h$ can be refined to a common partition, and additivity of measure ensures the integral is the same.

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
> **Scalar multiplication**: Let $h$ be non-negative simple measurable and $\alpha > 0$. Then $\int_E \alpha\, h\,dx = \alpha \int_E h\,dx$ by pulling $\alpha$ outside the sum in the [[§14 The Lebesgue Integral for Simple Functions#^def-14-1|definition]].
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
> By [[§10 Lebesgue Measurable Sets#^lem-10-2|additivity of measure]], since $\{B_k\}$ partitions $\mathbb{R}^n$:
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

*Uses:* [[§14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]], [[§10 Lebesgue Measurable Sets#^lem-10-2|§10.2]]

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

*Uses:* [[§14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]], [[§12 Measurable Functions#^def-12-3|Def. §12.3]], [[Properties of Lebesgue Outer Measure|§9.1]]

## The Integral for Non-Negative Measurable Functions

We now extend the integral from simple functions to general non-negative measurable functions.

> [!definition] Definition §14.2: Lebesgue Integral of a Non-Negative Measurable Function
> Let $E \subseteq \mathbb{R}^n$, $E \in \mathcal{M}$. Let $f$ be a non-negative [[§12 Measurable Functions#^def-12-2|measurable function]] on $E$. We define:
>
> $$
> \int_E f(x)\,dx = \sup\left\{\int_E h(x)\,dx \;\middle|\; h \text{ non-negative simple measurable on } \mathbb{R}^n,\; h(x) \leq f(x) \;\forall\, x \in E\right\}.
> $$

^def-14-2

![[m551-14-1.svg]]
*One admissible $h$ in the supremum. The simple function $h \leq f$ (blue) takes finitely many values $a_j$ on disjoint sets $A_j$, and a level set need not be an interval: here $A_j \cap E$ (red) has three pieces. Its integral is the shaded area $\sum_j a_j\, m(A_j \cap E)$; the integral of $f$ (black) is the supremum of such areas over all simple $h$ that stay below $f$ on $E$.*

> [!remark]- Connections
> - The same “sup from below” shape as the lower Darboux integral: [[§8 Motivation꞉ The Riemann Integral#^rem-8-1|Rem. §8.1]], [[§32 The Definition of the Riemann Integral#^def-32-2|451 Def. §32.2]].

> [!remark] Remark: Why Not Use Approximating Sequences?
> One might try to define $\int_E f\,dx$ as $\lim \int_E h_k\,dx$ for some sequence of simple functions $h_k \nearrow f$. The issue is that we are not yet guaranteed that different approximating sequences give the same limit. The supremum definition avoids this ambiguity. The [[Monotone Convergence Theorem (Lebesgue)|Monotone Convergence Theorem]] below will justify the sequential approach.

^rem-14-2

> [!remark] Remark: Generalization Beyond $\mathbb{R}^n$
> Although we state everything for Lebesgue measure on $\mathbb{R}^n$, nothing in the definitions or proofs above uses the structure of $\mathbb{R}^n$. The simple function integral $\sum a_j\,m(A_j \cap E)$ requires only a measure on a $\sigma$-algebra; the supremum definition requires only measurable functions and the simple integral; the MCT proof uses only monotonicity and [[Continuity of Measure|continuity of measure from below]]—all of which hold in any [[§11 Borel Sets and Measure Spaces#^def-11-7|measure space]] $(X, \mathcal{A}, \mu)$. Replacing $m$ by $\mu$ and writing $\int_E f\,d\mu$ instead of $\int_E f\,dx$, the entire theory (linearity, MCT, and the results that follow) carries over verbatim. The role of $\mathbb{R}^n$ is confined to the *construction* of Lebesgue measure; once we have a measure space in hand, integration theory is purely abstract.

^rem-14-3

> [!theorem] Proposition §14.3: Basic Properties
> Let $f, g$ be non-negative measurable functions on $E \in \mathcal{M}$, $E \subseteq \mathbb{R}^n$. Then:
> - (i) **Monotonicity**: If $f(x) \leq g(x)$ for all $x \in E$, then $\int_E f\,dx \leq \int_E g\,dx$.
> - (ii) **Null sets**: If $m(E) = 0$, then $\int_E f\,dx = 0$.

^prop-14-3

> [!proof]+ Proof
> **(i)** Every simple $h \leq f$ on $E$ also satisfies $h \leq g$ on $E$, so the supremum over $\{h : h \leq f\}$ is at most the supremum over $\{h : h \leq g\}$.
>
> **(ii)** For any simple $h \leq f$ on $E$, we have $\int_E h\,dx = 0$ since $m(E) = 0$ (by the [[§14 The Lebesgue Integral for Simple Functions#^prop-14-2|domain property for simple functions]]). Thus the supremum is $0$.

^pf-14-3

*Uses:* [[§14 The Lebesgue Integral for Simple Functions#^def-14-2|Def. §14.2]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-2|§14.2]]

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
> where the equality uses the [[§14 The Lebesgue Integral for Simple Functions#^prop-14-2|domain restriction property for simple functions]] and the inequality uses [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|monotonicity]]. Taking the supremum over all such $h$: $\int_A f\,dx \leq \int_E f\,\chi_A\,dx$.
>
> **($\geq$):** Let $h$ be a non-negative simple measurable function with $0 \leq h(x) \leq f(x)\,\chi_A(x)$ for all $x \in E$. Then for $x \in A^c$, $h(x) = 0$, so $h(x) = h(x)\,\chi_A(x)$ for all $x \in E$. On $A$, $h(x) \leq f(x)$. Thus:
>
> $$
> \int_E h\,dx = \int_E h\,\chi_A\,dx = \int_A h\,dx \leq \int_A f\,dx.
> $$
>
> Taking the supremum: $\int_E f\,\chi_A\,dx \leq \int_A f\,dx$.

^pf-14-6

*Uses:* [[§14 The Lebesgue Integral for Simple Functions#^def-14-2|Def. §14.2]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-2|§14.2]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]]

> [!theorem] Corollary §14.7: Domain Monotonicity
> Let $E \in \mathcal{M}$, $A \subseteq E$, $A \in \mathcal{M}$, and $f$ a non-negative measurable function on $E$. Then:
>
> $$
> \int_A f\,dx \leq \int_E f\,dx.
> $$

^cor-14-7

> [!proof]+ Proof
> Since $f(x) \geq 0$, we have $f(x)\,\chi_A(x) \leq f(x)$ for all $x \in E$. By [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|monotonicity of the integrand]] and the [[§14 The Lebesgue Integral for Simple Functions#^prop-14-6|domain restriction formula]]:
>
> $$
> \int_A f\,dx = \int_E f\,\chi_A\,dx \leq \int_E f\,dx.
> $$

^pf-14-7

*Uses:* [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-6|§14.6]]

## The Monotone Convergence Theorem

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

*Uses:* [[§14 The Lebesgue Integral for Simple Functions#^def-14-1|Def. §14.1]], [[Continuity of Measure|§11.12]]

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
> Define $f(x) = \lim_{k \to \infty} f_k(x)$. Since $\{f_k\}$ is an increasing sequence of non-negative measurable functions, $f$ is measurable (as the [[§12a Limits and Positive Parts of Measurable Functions#^cor-12-8|pointwise limit of measurable functions]]) and $f(x) \geq 0$.
>
> **Step 1: $\lim_{k \to \infty} \int_E f_k\,dx \leq \int_E f\,dx$.**
>
> By [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|monotonicity of the integral]]: since $f_k(x) \leq f_{k+1}(x) \leq \cdots \leq f(x)$ for all $x \in E$, we have
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
> By [[§14 The Lebesgue Integral for Simple Functions#^def-14-2|definition]], $\int_E f\,dx = \sup\bigl\{\int_E h\,dx \mid h \text{ simple, } 0 \leq h \leq f \text{ on } E\bigr\}$. It suffices to show that for every simple non-negative measurable $h$ with $h(x) \leq f(x)$ for all $x \in E$:
>
> $$
> \int_E h\,dx \leq \lim_{k \to \infty} \int_E f_k\,dx.
> $$
>
> We prove this via the [[§14 The Lebesgue Integral for Simple Functions#^lem-14-5|lemma]] above.

^pf-14-4

*Uses:* [[§12a Limits and Positive Parts of Measurable Functions#^cor-12-8|§12.8]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§14 The Lebesgue Integral for Simple Functions#^def-14-2|Def. §14.2]], [[Monotone Convergence Theorem|451 §10.1]]

> [!proof]+ Proof of the MCT (continued)
> **Applying the lemma.** Fix $c \in (0, 1)$ and define:
>
> $$
> E_k = \{x \in E \mid f_k(x) \geq c\,h(x)\}.
> $$
>
> *$E_k$ is measurable*: Since $f_k$ and $h$ are measurable, [[§12 Measurable Functions#^thm-12-3|so is]] $f_k - c\,h$, and $E_k = \{f_k - c\,h \geq 0\} \cap E$ is measurable.
>
> *$E_k \subseteq E_{k+1}$*: If $f_k(x) \geq c\,h(x)$, then $f_{k+1}(x) \geq f_k(x) \geq c\,h(x)$, so $x \in E_{k+1}$.
>
> *$\bigcup_{k=1}^{\infty} E_k = E$*: Let $x_0 \in E$.
>
> - If $h(x_0) = 0$: then $f_k(x_0) \geq 0 = c \cdot 0 = c\,h(x_0)$ for all $k$, so $x_0 \in E_k$ for all $k$.
> - If $h(x_0) > 0$: then $f(x_0) \geq h(x_0) > 0$ (since $h \leq f$). Since $\lim_{k \to \infty} f_k(x_0) = f(x_0)$ and $c\,h(x_0) < h(x_0) \leq f(x_0)$, there exists $l$ large enough such that $f_k(x_0) \geq c\,h(x_0)$ for all $k \geq l$. Hence $x_0 \in \bigcup_{k=1}^{\infty} E_k$.
>
> Now, on $E_k$ we have $f_k(x) \geq c\,h(x)$ by definition. Since $E_k \subseteq E$, [[§14 The Lebesgue Integral for Simple Functions#^cor-14-7|monotonicity of the domain]] ([[§14 The Lebesgue Integral for Simple Functions#^cor-14-7|Corollary §14.7]] above, whose proof does not use the MCT) gives $\int_E f_k\,dx \geq \int_{E_k} f_k\,dx$. Since $f_k \geq c\,h$ on $E_k$, monotonicity of the integrand ([[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|Proposition §14.3(i)]]) gives $\int_{E_k} f_k\,dx \geq \int_{E_k} c\,h\,dx = c\int_{E_k} h\,dx$. Combining:
>
> $$
> \int_E f_k\,dx \geq \int_{E_k} f_k\,dx \geq c \int_{E_k} h\,dx.
> $$
>
> Taking $k \to \infty$ and applying the [[§14 The Lebesgue Integral for Simple Functions#^lem-14-5|lemma]]:
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

*Uses:* [[§12 Measurable Functions#^thm-12-3|§12.3]], [[§14 The Lebesgue Integral for Simple Functions#^cor-14-7|§14.7]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|§14.3]], [[§14 The Lebesgue Integral for Simple Functions#^prop-14-1|§14.1]], [[§14 The Lebesgue Integral for Simple Functions#^lem-14-5|§14.5]], [[§14 The Lebesgue Integral for Simple Functions#^def-14-2|Def. §14.2]]

![[m551-14-2.svg]]
*The sets $E_k = \{f_k \geq c\,h\}$ in the proof of the MCT. Fix a simple $h \leq f$ (black) and lower it to $c\,h$ (dashed, $c < 1$). Where $f_k$ (blue) dips below $c\,h$ the point is not yet in $E_k$; the red part of the axis is $E_k$, and on it $\int_E f_k \geq c \int_{E_k} h$. As $f_k \nearrow f$ (gray) the dips fill in, so $E_k \nearrow E$. The factor $c < 1$ is essential: where $h = f$, the $f_k$ may approach $f$ from below without ever reaching $h$, but they do eventually pass $c\,h$.*

> [!remark]- Connections
> - Not to be confused with the MATH 451 [[Monotone Convergence Theorem]] for sequences of numbers, which it uses in Step 1.
> - The Riemann integral has no such theorem: [[§8 Motivation꞉ The Riemann Integral#^rem-8-2|Rem. §8.2]] (increasing $f_n \nearrow$ Dirichlet function). Riemann-side exchange of limit and integral needs uniform convergence: [[§33 Properties of the Riemann Integral#^thm-33-12|451 §33.12]].
> - Summarized with Fatou and DCT in [[§15a The Dominated Convergence Theorem#^rem-15-3|Rem. §15.3]]; the $L^p$ theory ([[§19 Normed Linear Spaces and Lᵖ Spaces|§19]]) and Tonelli ([[Tonelli's Theorem|§17.3]]) build on it.

The consequences of the MCT (linearity, MCT II, the induced measure, the decreasing MCT and Fatou's lemma) continue in [[§14a Consequences of the Monotone Convergence Theorem]].
