---
type: section
subject: "[[Single Variable Analysis]]"
section: "6★"
chapter: 1
aliases: ["Cauchy construction of the reals", "ℝ as Cauchy classes of ℚ"]
tags: [real-analysis, math451, extension]
---
← [[§6 Dedekind Cuts]] · ↑ [[· 1 Introduction]] · [[§7 Limits of Sequences]] →

★ *Beyond MATH 451: the course constructs ℝ only by Dedekind cuts (§6) and names this second route in one sentence ([[§10a Cauchy Sequences#^rem-10-4|§10a Rem. (construction of the reals)]]). The construction and all proofs below were added in the vault, following the standard order (as in Tao, Analysis I, Ch. 5). The last part, which compares the result with the course's ℝ, uses the limit theorems of §9–§10a. Those are derived from the axioms of §3–§4 alone, so the forward references are not circular.*

**Question.** §6 explained why ℝ cannot be defined as "limits of rational sequences" in this course: limits presuppose ℝ. Is there a way to use sequences anyway?

Yes. The *Cauchy* condition ([[§10 Monotone Sequences and Cauchy Sequences#^def-10-4|Def. §10.4]]) compares the terms of a sequence with each other and never mentions a limit. If moreover the tolerances $\varepsilon$ are taken to be *rational*, the condition makes sense inside $\mathbb{Q}$ alone. A real number is then *defined* as the common destination of a family of rational Cauchy sequences, that is, as an equivalence class of them. Where Dedekind cuts complete $\mathbb{Q}$ through its **order**, this route completes it through its **distance** $|p - q|$. The distance route is the one that generalizes to metric and normed spaces ([[§11 Completeness#^def-11-4|556 Def. §11.4]]).

Throughout, $|\cdot|$ on $\mathbb{Q}$ is the absolute value of [[§3 The Set ℝ of Real Numbers#^def-3-4|Def. §3.4]]. Its properties ([[§3 The Set ℝ of Real Numbers#^thm-3-3|Theorem §3.3]], including the [[Triangle inequality|triangle inequality]]) are proved from the order axioms O1–O5 and [[§3 The Set ℝ of Real Numbers#^prop-3-1|Proposition §3.1]] alone, so they hold in every ordered field, in particular in $\mathbb{Q}$. All $\varepsilon, \delta$ below are positive **rationals** unless stated otherwise.

## Cauchy Sequences of Rationals

> [!definition] Definition §6★.1: Rational Cauchy Sequence
> A sequence $(q_n)$ of rational numbers is a **rational Cauchy sequence** if for every rational $\varepsilon > 0$ there is $N$ such that
>
> $$
> |q_n - q_m| < \varepsilon \qquad \text{for all } n, m \geq N.
> $$
>
> Write $\mathcal{C}$ for the set of rational Cauchy sequences.
>
> This is [[§10 Monotone Sequences and Cauchy Sequences#^def-10-4|Def. §10.4]] with $\varepsilon$ restricted to $\mathbb{Q}$; nothing outside $\mathbb{Q}$ is mentioned.

^def-6s-1

> [!definition] Definition §6★.1: Null Sequence
> Let $(q_n)$ be a sequence of rational numbers. It is a **null sequence** if for every rational $\varepsilon > 0$ there is $N$ with $|q_n| < \varepsilon$ for all $n \geq N$. Write $\mathcal{C}$ for the set of rational Cauchy sequences and $\mathcal{N} \subseteq \mathcal{C}$ for the null sequences.

^def-6s-new1

A null sequence is Cauchy: if $|q_n| < \varepsilon/2$ for $n \geq N$, then $|q_n - q_m| \leq |q_n| + |q_m| < \varepsilon$. So $\mathcal{N} \subseteq \mathcal{C}$ indeed.

> [!theorem] Lemma §6★.1: Rational Cauchy Sequences Are Bounded
> If $(q_n) \in \mathcal{C}$, there is a rational $M \geq 1$ with $|q_n| \leq M$ for all $n$.

^lem-6s-1

> [!proof]+ Proof
> Take $\varepsilon = 1$ in the Cauchy condition: there is $N$ with $|q_n - q_N| < 1$ for $n \geq N$, so $|q_n| \leq |q_N| + |q_n - q_N| < |q_N| + 1$ for $n \geq N$ (triangle inequality). Put
>
> $$
> M = \max\{\, |q_1|, \ldots, |q_{N-1}|,\ |q_N| + 1 \,\},
> $$
>
> a maximum of finitely many rationals, hence rational, and $M \geq |q_N| + 1 \geq 1$. Every term is covered: $n < N$ by the first entries, $n \geq N$ by the last. (This is [[§10 Monotone Sequences and Cauchy Sequences#^lem-10-9|Lemma §10.9]] inside $\mathbb{Q}$.)

^pf-6s-1

*Uses:* [[§3 The Set ℝ of Real Numbers#^thm-3-3|§3.3]], [[§6★ ℝ from Cauchy Sequences of Rationals#^def-6s-1|Def. §6★.1]]

> [!definition] Definition §6★.2: Equivalent Rational Cauchy Sequences
> Two sequences $(p_n), (q_n) \in \mathcal{C}$ are **equivalent**, written $(p_n) \sim (q_n)$, if $(p_n - q_n)$ is a null sequence: for every rational $\varepsilon > 0$ there is $N$ with
>
> $$
> |p_n - q_n| < \varepsilon \qquad \text{for all } n \geq N.
> $$

^def-6s-2

> [!theorem] Lemma §6★.2: Equivalence of Cauchy Sequences Is an Equivalence Relation
> The relation $\sim$ on $\mathcal{C}$ is reflexive, symmetric and transitive: an equivalence relation ([[§22 Partitions and Equivalence Relations#^def-22-new1|250 Def. §22.3]]).

^lem-6s-2

> [!proof]+ Proof
> *Reflexive:* $p_n - p_n = 0$ for all $n$. *Symmetric:* $|q_n - p_n| = |p_n - q_n|$. *Transitive:* let $(p_n) \sim (q_n)$ and $(q_n) \sim (r_n)$, and let $\varepsilon > 0$ be rational. Choose $N_1$ with $|p_n - q_n| < \varepsilon/2$ for $n \geq N_1$ and $N_2$ with $|q_n - r_n| < \varepsilon/2$ for $n \geq N_2$. For $n \geq \max(N_1, N_2)$,
>
> $$
> |p_n - r_n| \leq |p_n - q_n| + |q_n - r_n| < \frac\varepsilon2 + \frac\varepsilon2 = \varepsilon.
> $$

^pf-6s-2

*Uses:* [[§6★ ℝ from Cauchy Sequences of Rationals#^def-6s-2|Def. §6★.2]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|§3.3]]

> [!definition] Definition §6★.3: The Cauchy Reals $\widehat{\mathbb{Q}}$
> Let $\widehat{\mathbb{Q}} = \mathcal{C}/\!\sim$ be the set of equivalence classes (the quotient set of [[§22 Partitions and Equivalence Relations#^def-22-new2|250 Def. §22.4]]), and write $[(q_n)]$ for the class of $(q_n)$. A rational $q$ is sent to the class of the constant sequence:
>
> $$
> \iota : \mathbb{Q} \to \widehat{\mathbb{Q}}, \qquad \iota(q) = [(q, q, q, \ldots)].
> $$

^def-6s-3

> [!remark]- Connections
> - The same pattern one level down: 250 builds $\mathbb{Q}$ as classes of pairs of integers, [[§22 Partitions and Equivalence Relations#^def-22-6|250 Def. §22.6]], and checks the field axioms on representatives, [[§22 Partitions and Equivalence Relations#^thm-22-9|250 Thm. §22.9]].
> - The general version: the completion of a metric space, [[§11 Completeness#^def-11-3|556 Def. §11.3]] and [[§11 Completeness#^def-11-4|556 Def. §11.4]], with $M = \mathbb{Q}$. See the remark on the order of logic below.

> [!example] Example §6★.1: One Number, Many Representatives
> - $0.9,\ 0.99,\ 0.999, \ldots$, that is $s_n = 1 - 10^{-n}$, is equivalent to the constant sequence $(1, 1, \ldots)$: the difference $10^{-n}$ is a null sequence (given rational $\varepsilon > 0$, $10^{-n} \leq 1/n < \varepsilon$ once $n > 1/\varepsilon$). So $[(s_n)] = \iota(1)$. This is "$0.999\ldots = 1$" ([[§13 Number Systems#^ex-13-4|250 Ex. §13.4]]) as a statement about representatives.
> - $(1/n)$ and $(-1/n)$ both represent $\iota(0)$, although every term of the first is positive and every term of the second is negative. Strict inequalities between terms do not survive the passage to classes (compare Lemma [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-6|§6★.6]](d)).

^ex-6s-1

## Arithmetic of Classes

> [!theorem] Proposition §6★.3: Operations on Cauchy Sequences Are Well Defined
> Let $(p_n), (q_n), (p_n'), (q_n') \in \mathcal{C}$.
>
> - (a) $(p_n + q_n)$, $(p_n q_n)$ and $(-p_n)$ are rational Cauchy sequences.
> - (b) If $(p_n) \sim (p_n')$ and $(q_n) \sim (q_n')$, then $(p_n + q_n) \sim (p_n' + q_n')$ and $(p_n q_n) \sim (p_n' q_n')$.
>
> Hence the following definitions do not depend on the chosen representatives:
>
> $$
> [(p_n)] + [(q_n)] = [(p_n + q_n)], \qquad [(p_n)]\cdot[(q_n)] = [(p_n q_n)], \qquad -[(p_n)] = [(-p_n)].
> $$

^prop-6s-3

> [!proof]+ Proof
> Fix a rational $\varepsilon > 0$. By [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-1|Lemma §6★.1]] choose rationals $M_p, M_q \geq 1$ with $|p_n| \leq M_p$ and $|q_n| \leq M_q$ for all $n$.
>
> (a) *Sum.* Choose $N$ with $|p_n - p_m| < \varepsilon/2$ and $|q_n - q_m| < \varepsilon/2$ for $n, m \geq N$. Then
>
> $$
> |(p_n + q_n) - (p_m + q_m)| \leq |p_n - p_m| + |q_n - q_m| < \varepsilon.
> $$
>
> *Product.* Add and subtract $p_n q_m$:
>
> $$
> p_n q_n - p_m q_m = p_n (q_n - q_m) + q_m (p_n - p_m),
> $$
>
> so $|p_n q_n - p_m q_m| \leq M_p |q_n - q_m| + M_q |p_n - p_m|$ (Theorem [[§3 The Set ℝ of Real Numbers#^thm-3-3|§3.3]]). Choose $N$ with $|q_n - q_m| < \varepsilon / (2M_p)$ and $|p_n - p_m| < \varepsilon/(2M_q)$ for $n, m \geq N$; then the right side is $< \varepsilon$. *Negative:* $|(-p_n) - (-p_m)| = |p_n - p_m|$.
>
> (b) *Sum.* $(p_n + q_n) - (p_n' + q_n') = (p_n - p_n') + (q_n - q_n')$ is a sum of two null sequences. Choosing $N$ with both terms $< \varepsilon/2$ in absolute value for $n \geq N$ shows it is null.
>
> *Product.* As in (a), $p_n q_n - p_n' q_n' = p_n (q_n - q_n') + q_n' (p_n - p_n')$. With $M_p$ as above and $M_q' \geq 1$ a bound for $(q_n')$,
>
> $$
> |p_n q_n - p_n' q_n'| \leq M_p |q_n - q_n'| + M_q' |p_n - p_n'|,
> $$
>
> and the right side is $< \varepsilon$ once $|q_n - q_n'| < \varepsilon/(2M_p)$ and $|p_n - p_n'| < \varepsilon/(2M_q')$, which holds for all large $n$ because both differences are null.

^pf-6s-3

*Uses:* [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-1|§6★.1]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|§3.3]], [[§6★ ℝ from Cauchy Sequences of Rationals#^def-6s-2|Def. §6★.2]]

> [!theorem] Lemma §6★.4: Bounded Away from Zero
> Let $(q_n) \in \mathcal{C}$ not be a null sequence. Then there are a rational $\delta > 0$ and an $N$ such that
>
> $$
> \text{either} \quad q_n \geq \delta \ \text{ for all } n \geq N, \qquad \text{or} \quad q_n \leq -\delta \ \text{ for all } n \geq N.
> $$

^lem-6s-4

> [!proof]+ Proof
> "Not null" means: there is a rational $\varepsilon_0 > 0$ such that for every $N$ some $n \geq N$ has $|q_n| \geq \varepsilon_0$. By the Cauchy condition with $\varepsilon_0/2$, choose $N$ with $|q_n - q_m| < \varepsilon_0/2$ for all $n, m \geq N$, and then pick $n_0 \geq N$ with $|q_{n_0}| \geq \varepsilon_0$.
>
> If $q_{n_0} \geq \varepsilon_0$, then for every $n \geq N$,
>
> $$
> q_n = q_{n_0} + (q_n - q_{n_0}) > \varepsilon_0 - \frac{\varepsilon_0}{2} = \frac{\varepsilon_0}{2}.
> $$
>
> If $q_{n_0} \leq -\varepsilon_0$, the same computation gives $q_n < -\varepsilon_0/2$ for $n \geq N$. Take $\delta = \varepsilon_0/2$.

^pf-6s-4

*Uses:* [[§6★ ℝ from Cauchy Sequences of Rationals#^def-6s-1|Def. §6★.1]], [[§6★ ℝ from Cauchy Sequences of Rationals#^def-6s-new1|Def. §6★.1]]

> [!theorem] Theorem §6★.5: $\widehat{\mathbb{Q}}$ Is a Field Containing $\mathbb{Q}$
> With the operations of [[§6★ ℝ from Cauchy Sequences of Rationals#^prop-6s-3|Proposition §6★.3]], $0 = \iota(0)$ and $1 = \iota(1)$, the set $\widehat{\mathbb{Q}}$ satisfies the field axioms ([[§3 The Set ℝ of Real Numbers#^def-3-1|Def. §3.1]]). The map $\iota$ is injective and preserves sums and products: $\iota(p + q) = \iota(p) + \iota(q)$ and $\iota(pq) = \iota(p)\iota(q)$.

^thm-6s-5

> [!proof]+ Proof
> *Axioms 1, 2, 5, 6 (commutativity, $0$ and $1$, associativity, distributivity).* Each is an identity that holds term by term in $\mathbb{Q}$ ([[§22 Partitions and Equivalence Relations#^thm-22-9|250 Thm. §22.9]]), so the two sides are represented by the *same* sequence. For example, for distributivity,
>
> $$
> [(p_n)]\bigl([(q_n)] + [(r_n)]\bigr) = [(p_n (q_n + r_n))] = [(p_n q_n + p_n r_n)] = [(p_n)][(q_n)] + [(p_n)][(r_n)],
> $$
>
> and likewise $[(p_n)] + \iota(0) = [(p_n + 0)] = [(p_n)]$ and $[(p_n)]\,\iota(1) = [(p_n)]$.
>
> *Axiom 3 (additive inverses).* $[(p_n)] + [(-p_n)] = [(0, 0, \ldots)] = \iota(0)$.
>
> *Axiom 4 (multiplicative inverses).* Let $x = [(q_n)] \neq \iota(0)$. Then $(q_n) \not\sim (0, 0, \ldots)$, i.e. $(q_n)$ is not null. By [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-4|Lemma §6★.4]] there are a rational $\delta > 0$ and $N$ with $|q_n| \geq \delta$ for $n \geq N$; in particular $q_n \neq 0$ there. Define
>
> $$
> r_n = 1 \ \ (n < N), \qquad r_n = \frac{1}{q_n} \ \ (n \geq N).
> $$
>
> For $n, m \geq N$,
>
> $$
> |r_n - r_m| = \left| \frac{q_m - q_n}{q_n q_m} \right| \leq \frac{|q_n - q_m|}{\delta^2},
> $$
>
> using [[§3 The Set ℝ of Real Numbers#^thm-3-3|Theorem §3.3]](ii) and $|q_n q_m| \geq \delta^2$. Given a rational $\varepsilon > 0$, choose $N' \geq N$ with $|q_n - q_m| < \delta^2 \varepsilon$ for $n, m \geq N'$; then $|r_n - r_m| < \varepsilon$. So $(r_n) \in \mathcal{C}$. Finally $q_n r_n = 1$ for $n \geq N$, so $(q_n r_n) - (1, 1, \ldots)$ is eventually $0$, hence null, and $[(q_n)][(r_n)] = \iota(1)$.
>
> *$0 \neq 1$.* The constant sequence $(1 - 0, 1 - 0, \ldots)$ is not null (take $\varepsilon = 1/2$), so $\iota(1) \neq \iota(0)$.
>
> *The map $\iota$.* $\iota(p) + \iota(q) = [(p + q, p + q, \ldots)] = \iota(p + q)$, and likewise for products. If $\iota(p) = \iota(q)$, the constant sequence $(p - q)$ is null, so $|p - q| < \varepsilon$ for every rational $\varepsilon > 0$. If $p \neq q$, the choice $\varepsilon = |p - q|$ gives $|p - q| < |p - q|$, which is impossible. So $p = q$.

^pf-6s-5

*Uses:* [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-4|§6★.4]], [[§6★ ℝ from Cauchy Sequences of Rationals#^prop-6s-3|§6★.3]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|§3.3]], [[§3 The Set ℝ of Real Numbers#^def-3-1|Def. §3.1]], [[§22 Partitions and Equivalence Relations#^thm-22-9|250 Thm. §22.9]]

From now on $\mathbb{Q}$ is identified with its copy $\iota(\mathbb{Q}) \subseteq \widehat{\mathbb{Q}}$ where convenient, as in [[§11 Completeness#^rem-11-3|556 Remark §11 (why classes)]].

> [!remark] Remark: The Algebra behind the Construction
> With termwise operations, $\mathcal{C}$ is a commutative ring ([[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-2|493 Def. §20.2]]), and the proof of [[§6★ ℝ from Cauchy Sequences of Rationals#^prop-6s-3|Proposition §6★.3]](b) shows that $\mathcal{N}$ is closed under sums and under multiplication by elements of $\mathcal{C}$ (bounded times null is null). In ring language, $\mathcal{N}$ is an *ideal* and $\widehat{\mathbb{Q}} = \mathcal{C}/\mathcal{N}$. On the additive side this is a quotient group in the sense of [[§40 Quotient Groups#^def-40-1|493 Def. §40.1]]: $\mathcal{N}$ is a subgroup ([[§4 Subgroups#^def-4-1|493 Def. §4.1]]) of the abelian group ([[§1 The Definition of a Group#^def-1-2|493 Def. §1.2]]) $(\mathcal{C}, +)$, and $(p_n) \sim (q_n)$ says exactly that the two sequences lie in the same coset of $\mathcal{N}$. [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-4|Lemma §6★.4]] is what makes the quotient a *field* rather than just a ring: a Cauchy sequence outside $\mathcal{N}$ can be inverted (eventually).

^rem-6s-1

## Order

> [!definition] Definition §6★.4: Positive Classes
> A class $x \in \widehat{\mathbb{Q}}$ is **positive**, written $x > 0$, if it has a representative $(q_n)$ with
>
> $$
> q_n \geq \delta \quad \text{for all } n \geq N, \qquad \text{for some rational } \delta > 0 \text{ and some } N.
> $$

^def-6s-4

"Eventually $q_n > 0$" would not do: $(1/n)$ has all terms positive, yet it represents $0$ ([[§6★ ℝ from Cauchy Sequences of Rationals#^ex-6s-1|Example §6★.1]]). Positivity has to be bounded away from zero, as in [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-4|Lemma §6★.4]].

> [!definition] Definition §6★.4: The Order on $\widehat{\mathbb{Q}}$
> For $x, y \in \widehat{\mathbb{Q}}$ define $x < y$ if $y - x > 0$ (positivity as in [[§6★ ℝ from Cauchy Sequences of Rationals#^def-6s-4|Definition §6★.4]]), and $x \leq y$ if $x < y$ or $x = y$.

^def-6s-new2

> [!theorem] Lemma §6★.6: Properties of Positivity
> Let $x, y \in \widehat{\mathbb{Q}}$.
>
> - (a) If $x > 0$, then *every* representative $(q_n')$ of $x$ satisfies $q_n' \geq \delta'$ for all large $n$, for some rational $\delta' > 0$.
> - (b) (*Trichotomy*) Exactly one of $x > 0$, $x = 0$, $-x > 0$ holds.
> - (c) If $x > 0$ and $y > 0$, then $x + y > 0$ and $xy > 0$.
> - (d) If some representative $(q_n)$ of $x$ has $q_n \geq 0$ for all large $n$, then $x \geq 0$.

^lem-6s-6

> [!proof]+ Proof
> (a) Let $(q_n)$ be the representative of the definition, $q_n \geq \delta$ for $n \geq N$, and let $(q_n') \sim (q_n)$. Choose $N'$ with $|q_n' - q_n| < \delta/2$ for $n \geq N'$. For $n \geq \max(N, N')$, $q_n' > q_n - \delta/2 \geq \delta/2$. Take $\delta' = \delta/2$.
>
> (b) *At least one.* If $x \neq 0$, a representative $(q_n)$ is not null, and [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-4|Lemma §6★.4]] gives either $q_n \geq \delta$ eventually ($x > 0$) or $-q_n \geq \delta$ eventually ($-x > 0$, since $(-q_n)$ represents $-x$).
>
> *At most one.* If $x > 0$ and $x = 0$, then by (a) the representative $(0, 0, \ldots)$ of $x$ would satisfy $0 \geq \delta' > 0$. If $x > 0$ and $-x > 0$, then by (a) a single representative $(q_n)$ of $x$ has $q_n \geq \delta'$ and $-q_n \geq \delta''$ for all large $n$, so $0 = q_n + (-q_n) \geq \delta' + \delta'' > 0$. The case $-x > 0$, $x = 0$ is the first case applied to $-x$.
>
> (c) Let $p_n \geq \delta$ for $n \geq N$ and $q_n \geq \delta'$ for $n \geq N'$ (representatives of $x$ and $y$). For $n \geq \max(N, N')$: $p_n + q_n \geq \delta + \delta' > 0$ and $p_n q_n \geq \delta \delta' > 0$ (O5 in $\mathbb{Q}$, applied twice).
>
> (d) By (b), if $x \geq 0$ fails then $-x > 0$, and by (a) $-q_n \geq \delta'$, i.e. $q_n \leq -\delta' < 0$, for all large $n$. This contradicts $q_n \geq 0$ for all large $n$.

^pf-6s-6

*Uses:* [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-4|§6★.4]], [[§6★ ℝ from Cauchy Sequences of Rationals#^def-6s-4|Def. §6★.4]]

> [!theorem] Theorem §6★.7: $\widehat{\mathbb{Q}}$ Is an Ordered Field
> With $\leq$ of [[§6★ ℝ from Cauchy Sequences of Rationals#^def-6s-new2|Def. §6★.4]], $\widehat{\mathbb{Q}}$ satisfies the order axioms O1–O5 ([[§3 The Set ℝ of Real Numbers#^def-3-2|Def. §3.2]]), so it is an ordered field. The embedding preserves order: for $p, q \in \mathbb{Q}$, $p \leq q$ if and only if $\iota(p) \leq \iota(q)$.

^thm-6s-7

> [!proof]+ Proof
> Throughout, $x \leq y$ means: $y - x > 0$ or $y - x = 0$.
>
> *O1 (totality).* Apply trichotomy ([[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-6|Lemma §6★.6]](b)) to $y - x$: either $y - x > 0$ ($x \leq y$), or $y - x = 0$, or $x - y = -(y - x) > 0$ ($y \leq x$).
>
> *O2 (antisymmetry).* If $x \leq y$, $y \leq x$ and $x \neq y$, then $y - x > 0$ and $-(y - x) = x - y > 0$, which trichotomy forbids. So $x = y$.
>
> *O3 (transitivity).* If $x \leq y$ and $y \leq z$, then $z - x = (z - y) + (y - x)$. If either difference is $0$, $z - x$ equals the other, which is $\geq 0$. Otherwise both are positive and so is the sum (Lemma [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-6|§6★.6]](c)).
>
> *O4.* $(y + z) - (x + z) = y - x$.
>
> *O5.* If $x \leq y$ and $0 \leq z$, then $yz - xz = (y - x) z$ (distributivity, [[§6★ ℝ from Cauchy Sequences of Rationals#^thm-6s-5|Theorem §6★.5]]). This is $0$ if $y - x = 0$ or $z = 0$, and positive by Lemma [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-6|§6★.6]](c) otherwise.
>
> *The embedding.* If $p < q$ in $\mathbb{Q}$, then $\iota(q) - \iota(p) = \iota(q - p)$ is represented by the constant sequence $q - p \geq \delta := q - p > 0$, so $\iota(p) < \iota(q)$; and $p = q$ gives $\iota(p) = \iota(q)$. Conversely, if $\iota(p) \leq \iota(q)$ but $p > q$, the first part gives $\iota(q) < \iota(p)$, contradicting O2 and the injectivity of $\iota$.

^pf-6s-7

*Uses:* [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-6|§6★.6]], [[§6★ ℝ from Cauchy Sequences of Rationals#^thm-6s-5|§6★.5]], [[§3 The Set ℝ of Real Numbers#^def-3-2|Def. §3.2]], [[§6★ ℝ from Cauchy Sequences of Rationals#^def-6s-new2|Def. §6★.4]]

Since $\widehat{\mathbb{Q}}$ is an ordered field, it has an absolute value ([[§3 The Set ℝ of Real Numbers#^def-3-4|Def. §3.4]]) with the properties of [[§3 The Set ℝ of Real Numbers#^thm-3-3|Theorem §3.3]]. Because $\iota$ preserves sums, products and order, $|\iota(q)| = \iota(|q|)$. Recall that in any ordered field $|a| \leq c$ if and only if $-c \leq a \leq c$.

## Rational Approximation

> [!theorem] Proposition §6★.8: Rational Approximation in $\widehat{\mathbb{Q}}$
> Let $x = [(q_n)] \in \widehat{\mathbb{Q}}$.
>
> - (a) (*Archimedean*) There is a rational $M$ with $x \leq \iota(M)$; hence $x \leq \iota(k)$ for some integer $k$.
> - (b) If $\varepsilon \in \widehat{\mathbb{Q}}$ is positive, there is a rational $\delta > 0$ with $\iota(\delta) < \varepsilon$.
> - (c) If $\varepsilon > 0$ is rational and $N$ satisfies $|q_n - q_m| < \varepsilon$ for all $n, m \geq N$, then
>
>   $$
>   |x - \iota(q_k)| \leq \iota(\varepsilon) \qquad \text{for every } k \geq N.
>   $$
>
> - (d) (*Density*) If $x < y$ in $\widehat{\mathbb{Q}}$, there is a rational $r$ with $x < \iota(r) < y$.

^prop-6s-8

> [!proof]+ Proof
> (a) By [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-1|Lemma §6★.1]], $|q_n| \leq M$ for all $n$ with $M$ rational. Then $\iota(M) - x$ is represented by $(M - q_n)$, whose terms are all $\geq 0$, so $\iota(M) - x \geq 0$ by [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-6|Lemma §6★.6]](d). Any integer $k \geq M$ then works, since $\iota$ preserves order.
>
> (b) Let $(e_n)$ represent $\varepsilon$ with $e_n \geq \delta_0$ for $n \geq N$ ($\delta_0 > 0$ rational). Put $\delta = \delta_0/2$. Then $\varepsilon - \iota(\delta)$ is represented by $(e_n - \delta_0/2)$, whose terms are $\geq \delta_0/2$ for $n \geq N$, so $\varepsilon - \iota(\delta) > 0$.
>
> (c) Fix $k \geq N$. The class $x - \iota(q_k)$ is represented by the sequence $(q_n - q_k)_{n \geq 1}$. For $n \geq N$, $|q_n - q_k| < \varepsilon$, so both
>
> $$
> \varepsilon - (q_n - q_k) > 0 \qquad \text{and} \qquad \varepsilon + (q_n - q_k) > 0 .
> $$
>
> These sequences represent $\iota(\varepsilon) - (x - \iota(q_k))$ and $\iota(\varepsilon) + (x - \iota(q_k))$. By Lemma [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-6|§6★.6]](d) both classes are $\geq 0$, i.e. $-\iota(\varepsilon) \leq x - \iota(q_k) \leq \iota(\varepsilon)$, which is $|x - \iota(q_k)| \leq \iota(\varepsilon)$. Only the weak inequality survives (compare [[§6★ ℝ from Cauchy Sequences of Rationals#^ex-6s-1|Example §6★.1]]).
>
> (d) By (b) applied to $y - x > 0$, pick a rational $\delta > 0$ with $\iota(\delta) < y - x$. By the Cauchy condition with $\delta/3$ and (c), there is $k$ with $|x - \iota(q_k)| \leq \iota(\delta/3)$. Put $r = q_k + 2\delta/3$. Then
>
> $$
> \iota(r) = \iota(q_k) + \iota(2\delta/3) \geq x - \iota(\delta/3) + \iota(2\delta/3) = x + \iota(\delta/3) > x,
> $$
>
> $$
> \iota(r) \leq x + \iota(\delta/3) + \iota(2\delta/3) = x + \iota(\delta) < x + (y - x) = y .
> $$

^pf-6s-8

*Uses:* [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-1|§6★.1]], [[§6★ ℝ from Cauchy Sequences of Rationals#^lem-6s-6|§6★.6]]

Limits and Cauchy sequences make sense in any ordered field: read [[§7 Limits of Sequences#^def-7-2|Def. §7.2]] and [[§10 Monotone Sequences and Cauchy Sequences#^def-10-4|Def. §10.4]] with $\varepsilon$ ranging over the positive elements of the field.

> [!definition] Definition §6★.5: Convergence in $\widehat{\mathbb{Q}}$
> A sequence $(x_k)$ in $\widehat{\mathbb{Q}}$ **converges** to $x \in \widehat{\mathbb{Q}}$ if for every positive $\varepsilon \in \widehat{\mathbb{Q}}$ there is $K$ with $|x_k - x| < \varepsilon$ for all $k \geq K$.
>
> By [[§6★ ℝ from Cauchy Sequences of Rationals#^prop-6s-8|Proposition §6★.8]](b) it is enough to test $\varepsilon = \iota(\delta)$ with $\delta > 0$ rational.

^def-6s-5

> [!definition] Definition §6★.5: Cauchy Sequences in $\widehat{\mathbb{Q}}$
> Let $(x_k)$ be a sequence in $\widehat{\mathbb{Q}}$. It is **Cauchy** if for every positive $\varepsilon \in \widehat{\mathbb{Q}}$ there is $K$ with $|x_k - x_m| < \varepsilon$ for all $k, m \geq K$.
>
> As for convergence, by [[§6★ ℝ from Cauchy Sequences of Rationals#^prop-6s-8|Proposition §6★.8]](b) it is enough to test $\varepsilon = \iota(\delta)$ with $\delta > 0$ rational.

^def-6s-new3

> [!theorem] Corollary §6★.9: A Class Is the Limit of Its Representative
> If $x = [(q_n)] \in \widehat{\mathbb{Q}}$, then $\iota(q_k) \to x$ in $\widehat{\mathbb{Q}}$ as $k \to \infty$.

^cor-6s-9

> [!proof]+ Proof
> Let $\varepsilon \in \widehat{\mathbb{Q}}$ be positive. By [[§6★ ℝ from Cauchy Sequences of Rationals#^prop-6s-8|Proposition §6★.8]](b) pick a rational $\delta > 0$ with $\iota(\delta) < \varepsilon$, and $N$ with $|q_n - q_m| < \delta$ for $n, m \geq N$. By §6★.8(c), $|x - \iota(q_k)| \leq \iota(\delta) < \varepsilon$ for all $k \geq N$.

^pf-6s-9

*Uses:* [[§6★ ℝ from Cauchy Sequences of Rationals#^prop-6s-8|§6★.8]]

> [!remark]- Connections
> - This is [[§11 Completeness#^prop-11-3|556 Proposition §11.3]](c), "$M$ is dense in $\overline{M}$", for $M = \mathbb{Q}$.

This resolves the circularity that §6 warned about. "The limit of a rational Cauchy sequence" is now a theorem about the class, not a definition of it.

> [!example] Example §6★.2: The Class of √2
> For $n \geq 0$ let $d_n$ be the largest decimal fraction with $n$ digits whose square is at most $2$:
>
> $$
> d_n = \max\Bigl\{ \frac{k}{10^n} : k \in \mathbb{N},\ k^2 \leq 2 \cdot 10^{2n} \Bigr\} \qquad (d_0 = 1,\ d_1 = 1.4,\ d_2 = 1.41, \ldots).
> $$
>
> The set is finite and nonempty ($k \leq 2 \cdot 10^n$, and $k = 10^n$ qualifies), so $d_n$ is a rational in $[1, 2]$, defined without mentioning $\sqrt 2$.
>
> *Cauchy.* Let $n \leq m$. Since $d_n = (10^{m-n} k)/10^m$ is a candidate at level $m$, $d_n \leq d_m$. By maximality $(d_n + 10^{-n})^2 > 2$, and $d_m^2 \leq 2$ with $d_m \geq 0$, so $d_m < d_n + 10^{-n}$. Hence $0 \leq d_m - d_n < 10^{-n} \leq 1/n$ (for $n \geq 1$), which is $< \varepsilon$ once $n > 1/\varepsilon$.
>
> *Its square is 2.* $d_n^2 \leq 2 < (d_n + 10^{-n})^2$ gives $0 \leq 2 - d_n^2 < 2 d_n 10^{-n} + 10^{-2n} \leq 5 \cdot 10^{-n}$, a null sequence. So $(d_n^2) \sim (2, 2, \ldots)$, and $x = [(d_n)]$ satisfies $x^2 = \iota(2)$ and $x > 0$ (all $d_n \geq 1$).
>
> *It is new.* If $x = \iota(q)$ with $q \in \mathbb{Q}$, then $\iota(q^2) = \iota(2)$, so $q^2 = 2$ by injectivity of $\iota$. This contradicts [[§13 Number Systems#^thm-13-4|250 Thm. §13.4]] ($\sqrt 2$ is irrational). So $\widehat{\mathbb{Q}}$ is strictly larger than $\iota(\mathbb{Q})$.
>
> The Babylonian iteration $1, \frac32, \frac{17}{12}, \frac{577}{408}, \ldots$ ($a_{n+1} = \frac{a_n}{2} + \frac{1}{a_n}$) is another representative of the same class: it converges much faster, but it is one element of $\widehat{\mathbb{Q}}$ (both sequences have limit $\sqrt 2$ in ℝ, so they are equivalent by [[§6★ ℝ from Cauchy Sequences of Rationals#^thm-6s-12|Theorem §6★.12]]). Compare the decimal expansion of $\sqrt 2$ in [[§13 Number Systems#^ex-13-3|250 Ex. §13.3]] and decimal expansions in [[§16 Decimal Expansions of Real Numbers (Not Covered)|§16]].

^ex-6s-2

## Completeness

> [!theorem] Theorem §6★.10: $\widehat{\mathbb{Q}}$ Is Cauchy Complete
> Every Cauchy sequence in $\widehat{\mathbb{Q}}$ ([[§6★ ℝ from Cauchy Sequences of Rationals#^def-6s-new3|Def. §6★.5]]) converges in $\widehat{\mathbb{Q}}$.

^thm-6s-10

> [!proof]+ Proof
> Let $(x_k)$ be Cauchy in $\widehat{\mathbb{Q}}$.
>
> *Step 1: rational shadows.* For each $k$ write $x_k = [(q^{(k)}_n)_n]$. By [[§6★ ℝ from Cauchy Sequences of Rationals#^prop-6s-8|Proposition §6★.8]](c) with $\varepsilon = 1/k$, there is $N_k$ with $|x_k - \iota(q^{(k)}_{N_k})| \leq \iota(1/k)$. Put $r_k = q^{(k)}_{N_k} \in \mathbb{Q}$, so
>
> $$
> |x_k - \iota(r_k)| \leq \iota(1/k) \qquad \text{for all } k.
> $$
>
> *Step 2: $(r_k)$ is a rational Cauchy sequence.* Let $\varepsilon > 0$ be rational, and choose an integer $K_1 > 3/\varepsilon$, so that $1/k < \varepsilon/3$ for $k \geq K_1$. Since $(x_k)$ is Cauchy, choose $K_2$ with $|x_k - x_m| < \iota(\varepsilon/3)$ for $k, m \geq K_2$. For $k, m \geq \max(K_1, K_2)$,
>
> $$
> \iota(|r_k - r_m|) = |\iota(r_k) - \iota(r_m)| \leq |\iota(r_k) - x_k| + |x_k - x_m| + |x_m - \iota(r_m)| < \iota\Bigl(\frac\varepsilon3 + \frac\varepsilon3 + \frac\varepsilon3\Bigr) = \iota(\varepsilon),
> $$
>
> and since $\iota$ preserves and reflects order ([[§6★ ℝ from Cauchy Sequences of Rationals#^thm-6s-7|Theorem §6★.7]]), $|r_k - r_m| < \varepsilon$. Let $x = [(r_k)] \in \widehat{\mathbb{Q}}$.
>
> *Step 3: $x_k \to x$.* For every $k$,
>
> $$
> |x_k - x| \leq |x_k - \iota(r_k)| + |\iota(r_k) - x| \leq \iota(1/k) + |\iota(r_k) - x| .
> $$
>
> Given a positive $\varepsilon \in \widehat{\mathbb{Q}}$, pick a rational $\delta > 0$ with $\iota(\delta) < \varepsilon$ (§6★.8(b)). By [[§6★ ℝ from Cauchy Sequences of Rationals#^cor-6s-9|Corollary §6★.9]] applied to $x$ and its representative $(r_k)$, there is $K_3$ with $|\iota(r_k) - x| < \iota(\delta/2)$ for $k \geq K_3$. For $k \geq \max(K_3, 2/\delta + 1)$ also $1/k < \delta/2$, so $|x_k - x| < \iota(\delta) < \varepsilon$.

^pf-6s-10

*Uses:* [[§6★ ℝ from Cauchy Sequences of Rationals#^prop-6s-8|§6★.8]], [[§6★ ℝ from Cauchy Sequences of Rationals#^thm-6s-7|§6★.7]], [[§6★ ℝ from Cauchy Sequences of Rationals#^cor-6s-9|§6★.9]]

> [!remark]- Connections
> - The same diagonal argument, with $z_m$ chosen within $1/m$ of $\xi_m$: [[§11 Completeness#^prop-11-3|556 Proposition §11.3]](d), and for normed spaces [[§11 Completeness#^thm-11-4|556 Theorem §11.4]].
> - In ℝ this is [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|Theorem §10.8]] (Cauchy implies convergent), which the course derives *from* the completeness axiom. Here the logic runs the other way: Cauchy completeness is built in, and the completeness axiom is derived next.

> [!theorem] Theorem §6★.11: $\widehat{\mathbb{Q}}$ Satisfies the Completeness Axiom
> Every nonempty subset $S \subseteq \widehat{\mathbb{Q}}$ that is bounded above has a least upper bound in $\widehat{\mathbb{Q}}$ ([[Completeness Axiom|completeness axiom]], [[§4 The Completeness Axiom#^def-4-4|Def. §4.4]]). So $\widehat{\mathbb{Q}}$ is a complete ordered field.

^thm-6s-11

> [!proof]+ Proof
> *Start.* Pick $s_0 \in S$ and an upper bound $u$ of $S$. By [[§6★ ℝ from Cauchy Sequences of Rationals#^prop-6s-8|Proposition §6★.8]](a) there is a rational $b_0$ with $u \leq \iota(b_0)$, so $\iota(b_0)$ is an upper bound of $S$. Applying §6★.8(a) to $-s_0$ gives a rational $M$ with $-s_0 \leq \iota(M)$. Put $a_0 = -M - 1$; then $\iota(a_0) < s_0$, so $\iota(a_0)$ is *not* an upper bound of $S$. In particular $a_0 < b_0$.
>
> *Bisection.* Given rationals $a_k < b_k$ such that $\iota(b_k)$ is an upper bound of $S$ and $\iota(a_k)$ is not, let $c = \frac{a_k + b_k}{2}$. If $\iota(c)$ is an upper bound of $S$, set $a_{k+1} = a_k$, $b_{k+1} = c$; otherwise set $a_{k+1} = c$, $b_{k+1} = b_k$. By induction, for all $k$:
>
> $$
> a_k \leq a_{k+1} < b_{k+1} \leq b_k, \qquad b_k - a_k = \frac{b_0 - a_0}{2^k}, \qquad \iota(b_k) \text{ is an upper bound of } S,\ \ \iota(a_k) \text{ is not.}
> $$
>
> *Two equivalent Cauchy sequences.* For $m \geq k$, $0 \leq b_k - b_m \leq b_k - a_k = (b_0 - a_0)/2^k \leq (b_0 - a_0)/k$ (as $2^k \geq k$), and likewise $0 \leq a_m - a_k \leq (b_0 - a_0)/k$. Given a rational $\varepsilon > 0$, these are $< \varepsilon$ once $k > (b_0 - a_0)/\varepsilon$. So $(a_k), (b_k) \in \mathcal{C}$, and $(b_k - a_k)$ is null by the same bound, so $(a_k) \sim (b_k)$. Let
>
> $$
> s = [(b_k)] = [(a_k)] \in \widehat{\mathbb{Q}}.
> $$
>
> *$s$ is an upper bound.* Let $y \in S$ and suppose $y > s$. With $\varepsilon = y - s > 0$, [[§6★ ℝ from Cauchy Sequences of Rationals#^cor-6s-9|Corollary §6★.9]] gives $k$ with $|\iota(b_k) - s| < \varepsilon$, so $\iota(b_k) < s + \varepsilon = y$. This contradicts $\iota(b_k)$ being an upper bound. Hence $y \leq s$.
>
> *$s$ is the least upper bound.* Let $v$ be an upper bound of $S$ and suppose $v < s$. With $\varepsilon = s - v > 0$, [[§6★ ℝ from Cauchy Sequences of Rationals#^cor-6s-9|Corollary §6★.9]] applied to the representative $(a_k)$ gives $k$ with $|\iota(a_k) - s| < \varepsilon$, so $\iota(a_k) > s - \varepsilon = v$. As $\iota(a_k)$ is not an upper bound, some $y \in S$ has $y > \iota(a_k) > v$, contradicting that $v$ is an upper bound. Hence $s \leq v$, and $s = \sup S$.

^pf-6s-11

*Uses:* [[§6★ ℝ from Cauchy Sequences of Rationals#^prop-6s-8|§6★.8]], [[§6★ ℝ from Cauchy Sequences of Rationals#^cor-6s-9|§6★.9]]

> [!remark]- Connections
> - The cut route gets the same axiom from the order directly: the supremum of a bounded family of cuts is their union ([[§6 Dedekind Cuts#^prop-6-5|Proposition §6.5]](iv)).
> - Here the supremum is written down directly as the class of the bisection endpoints. In an arbitrary Archimedean ordered field the same bisection works with the limit of $(b_k)$ supplied by Cauchy completeness. Conversely, the course derives Cauchy completeness from the least-upper-bound property ([[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|Theorem §10.8]]). So for an Archimedean ordered field the two forms of completeness are equivalent.

## The Two Routes Give the Same ℝ

From here on, ℝ is the course's ℝ: an ordered field containing $\mathbb{Q}$ and satisfying the completeness axiom (§3–§4). The proofs use [[§4 The Completeness Axiom#^thm-4-7|Theorem §4.7]] (density of $\mathbb{Q}$) and the limit theorems of §9–§10a, all of which are derived from those axioms.

> [!theorem] Theorem §6★.12: The Cauchy Reals Are the Real Numbers
> A rational Cauchy sequence converges in ℝ, and
>
> $$
> \Phi : \widehat{\mathbb{Q}} \to \mathbb{R}, \qquad \Phi\bigl([(q_n)]\bigr) = \lim_{n \to \infty} q_n,
> $$
>
> is a well-defined bijection that preserves sums, products and order, with $\Phi(\iota(q)) = q$ for $q \in \mathbb{Q}$. In short, $\widehat{\mathbb{Q}}$ and ℝ are isomorphic ordered fields, by an isomorphism fixing $\mathbb{Q}$.

^thm-6s-12

> [!proof]+ Proof
> *Rational versus real tolerances.* For a rational sequence, a condition "$|\,\cdot\,| < \varepsilon$ eventually" holds for all real $\varepsilon > 0$ as soon as it holds for all rational $\varepsilon > 0$: given a real $\varepsilon > 0$, [[§4 The Completeness Axiom#^thm-4-7|Theorem §4.7]] gives a rational $\varepsilon'$ with $0 < \varepsilon' < \varepsilon$. The converse is trivial. So a rational Cauchy sequence is Cauchy in ℝ ([[§10 Monotone Sequences and Cauchy Sequences#^def-10-4|Def. §10.4]]), and $(p_n) \sim (q_n)$ if and only if $p_n - q_n \to 0$ in ℝ.
>
> *Well defined.* A rational Cauchy sequence converges in ℝ by [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|Theorem §10.8]]. If $(p_n) \sim (q_n)$, then $p_n - q_n \to 0$, so $\lim p_n = \lim q_n$ by [[§9 Limit Theorems for Sequences#^cor-9-6|Corollary §9.6]] ($\lim (p_n - q_n) = \lim p_n - \lim q_n$).
>
> *Injective.* If $\lim p_n = \lim q_n$, the same corollary gives $p_n - q_n \to 0$, i.e. $(p_n) \sim (q_n)$.
>
> *Surjective.* Let $r \in \mathbb{R}$. By [[§4 The Completeness Axiom#^thm-4-7|Theorem §4.7]], for each $n$ pick $q_n \in \mathbb{Q}$ with $r - 1/n < q_n < r$. Then $|q_n - r| < 1/n$, so $q_n \to r$ (by the [[Archimedean Property|Archimedean property]], $1/n < \varepsilon$ for large $n$). A convergent sequence is Cauchy ([[§10 Monotone Sequences and Cauchy Sequences#^thm-10-7|Theorem §10.7]]), so $(q_n) \in \mathcal{C}$ and $\Phi([(q_n)]) = r$.
>
> *Operations.* $\Phi$ of a sum or product is the limit of termwise sums or products, which is the sum or product of the limits ([[§9 Limit Theorems for Sequences#^thm-9-3|Theorem §9.3]]). The constant sequence $q$ has limit $q$, so $\Phi(\iota(q)) = q$.
>
> *Order.* It suffices to show $x > 0 \iff \Phi(x) > 0$, since $x < y$ means $y - x > 0$ and $\Phi(y - x) = \Phi(y) - \Phi(x)$. If $q_n \geq \delta$ for $n \geq N$, then $\lim q_n \geq \delta > 0$ ([[§9 Limit Theorems for Sequences#^prop-9-5|Proposition §9.5]], limits preserve weak inequalities). Conversely, if $r = \lim q_n > 0$, pick $N$ with $|q_n - r| < r/2$ for $n \geq N$, so $q_n > r/2$; and pick a rational $\delta$ with $0 < \delta < r/2$ ([[§4 The Completeness Axiom#^thm-4-7|Theorem §4.7]]). Then $q_n \geq \delta$ for $n \geq N$, so $[(q_n)] > 0$.

^pf-6s-12

*Uses:* [[§4 The Completeness Axiom#^thm-4-7|§4.7]], [[§10 Monotone Sequences and Cauchy Sequences#^def-10-4|Def. §10.4]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|§10.8]], [[§9 Limit Theorems for Sequences#^cor-9-6|§9.6]], [[Archimedean Property|§4.5]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-7|§10.7]], [[§9 Limit Theorems for Sequences#^thm-9-3|§9.3]], [[§9 Limit Theorems for Sequences#^prop-9-5|§9.5]]

> [!theorem] Corollary §6★.13: Cauchy Classes and Dedekind Cuts
> For $x = [(q_n)] \in \widehat{\mathbb{Q}}$ put
>
> $$
> \Psi(x) = \{\, p \in \mathbb{Q} : \text{there are a rational } \delta > 0 \text{ and } N \text{ with } p + \delta \leq q_n \text{ for all } n \geq N \,\}.
> $$
>
> Then $\Psi(x)$ is the Dedekind cut $S_{\Phi(x)}$ ([[§6 Dedekind Cuts#^def-6-1|Def. §6.1]]), and $\Psi$ is a bijection from $\widehat{\mathbb{Q}}$ onto the set of all subsets of $\mathbb{Q}$ with properties (1)–(3) of [[§6 Dedekind Cuts#^prop-6-1|Proposition §6.1]], such that
>
> $$
> x \leq y \iff \Psi(x) \subseteq \Psi(y), \qquad \Psi(x + y) = \Psi(x) + \Psi(y), \qquad \Psi(\iota(q)) = S_q .
> $$
>
> So the Cauchy route and the cut route produce the same number system, with the same order and addition.

^cor-6s-13

> [!proof]+ Proof
> *$\Psi(x) = S_r$ with $r = \Phi(x) = \lim q_n$.* If $p + \delta \leq q_n$ for $n \geq N$, then $p + \delta \leq r$ ([[§9 Limit Theorems for Sequences#^prop-9-5|Proposition §9.5]]), so $p < r$. Conversely let $p \in \mathbb{Q}$ with $p < r$. Pick a rational $\delta$ with $0 < \delta < (r - p)/2$ ([[§4 The Completeness Axiom#^thm-4-7|Theorem §4.7]]) and $N$ with $|q_n - r| < (r - p)/2$ for $n \geq N$. Then $q_n > r - (r - p)/2 = p + (r - p)/2 > p + \delta$ for $n \geq N$, so $p \in \Psi(x)$.
>
> *$r \mapsto S_r$ is a bijection from ℝ onto the sets with (1)–(3).* Each $S_r$ has (1)–(3) by [[§6 Dedekind Cuts#^prop-6-1|Proposition §6.1]]. This step proves the converse that §6 states without proof. Let $A \subseteq \mathbb{Q}$ have (1)–(3). By (1) pick $a^{\ast} \in \mathbb{Q} \setminus A$. By (2), every $a \in A$ satisfies $a < a^{\ast}$ (if $a^{\ast} \leq a$, then $a^{\ast} \in A$). So $A$ is nonempty and bounded above, and $r = \sup A$ exists by the [[Completeness Axiom|completeness axiom]]. If $a \in A$, then $a \leq r$, and $a \neq r$: otherwise $a$ would be the maximum of $A$, against (3). So $A \subseteq S_r$. If $p \in \mathbb{Q}$ and $p < r$, then $p$ is not an upper bound of $A$ ([[Characterization of the Supremum|characterization of the supremum]]), so $p < a$ for some $a \in A$, and $p \in A$ by (2). So $A = S_r$. Injectivity: if $r_1 < r_2$, [[§4 The Completeness Axiom#^thm-4-7|Theorem §4.7]] gives a rational in $S_{r_2} \setminus S_{r_1}$.
>
> *Order.* $S_{r_1} \subseteq S_{r_2} \iff r_1 \leq r_2$: "$\Leftarrow$" is immediate, and "$\Rightarrow$" is the injectivity argument just given. Combined with [[§6★ ℝ from Cauchy Sequences of Rationals#^thm-6s-12|Theorem §6★.12]], $x \leq y \iff \Phi(x) \leq \Phi(y) \iff \Psi(x) \subseteq \Psi(y)$.
>
> *Addition.* By [[§6★ ℝ from Cauchy Sequences of Rationals#^thm-6s-12|Theorem §6★.12]], $\Psi(x + y) = S_{r_1 + r_2}$ with $r_1 = \Phi(x)$, $r_2 = \Phi(y)$. If $a < r_1$ and $b < r_2$, then $a + b < r_1 + r_2$, so $S_{r_1} + S_{r_2} \subseteq S_{r_1 + r_2}$. Conversely let $q \in \mathbb{Q}$ with $q < r_1 + r_2$, and put $\eta = (r_1 + r_2 - q)/2 > 0$. Pick a rational $a$ with $r_1 - \eta < a < r_1$ and put $b = q - a \in \mathbb{Q}$. Then $b < q - r_1 + \eta = r_2 - \eta < r_2$, so $q = a + b \in S_{r_1} + S_{r_2}$. This proves [[§6 Dedekind Cuts#^prop-6-2|Proposition §6.2]](ii) as well.
>
> Finally $\Psi(\iota(q)) = S_{\Phi(\iota(q))} = S_q$.

^pf-6s-13

*Uses:* [[§9 Limit Theorems for Sequences#^prop-9-5|§9.5]], [[§4 The Completeness Axiom#^thm-4-7|§4.7]], [[§6 Dedekind Cuts#^prop-6-1|§6.1]], [[Completeness Axiom|Def. §4.4]], [[Characterization of the Supremum|§4.3]], [[§6★ ℝ from Cauchy Sequences of Rationals#^thm-6s-12|§6★.12]]

> [!theorem] Corollary §6★.14: Uniqueness of the Complete Ordered Field
> Any two complete ordered fields are isomorphic as ordered fields. In particular the axioms of §3–§4 determine ℝ up to isomorphism, and any model of them (cuts, Cauchy classes, …) is "the" real numbers.

^cor-6s-14

> [!proof]+ Proof
> Let $F$ be a complete ordered field.
>
> *$F$ contains a copy of $\mathbb{Q}$.* In $F$, $0 < 1$ ([[§3 The Set ℝ of Real Numbers#^prop-3-1|Proposition §3.1]](e)), so by O4 and induction $0 < 1 < 1 + 1 < \cdots$. Hence $n \mapsto n \cdot 1_F$ is injective and order-preserving on $\mathbb{Z}$, and it preserves sums and products. The map $m/n \mapsto (m \cdot 1_F)(n \cdot 1_F)^{-1}$ ($n > 0$) is well defined, because $m/n = m'/n'$ means $mn' = m'n$. It is an injective, order-preserving field homomorphism $\mathbb{Q} \to F$ ([[§3 The Set ℝ of Real Numbers#^prop-3-1|Proposition §3.1]](f), (g) for the order). Identify $\mathbb{Q}$ with its image.
>
> *$F \cong \widehat{\mathbb{Q}}$.* The proof of [[§6★ ℝ from Cauchy Sequences of Rationals#^thm-6s-12|Theorem §6★.12]] used about ℝ only that it is an ordered field containing $\mathbb{Q}$ with the completeness axiom, through results derived from these axioms (density [[§4 The Completeness Axiom#^thm-4-7|Theorem §4.7]], the [[Archimedean Property|Archimedean property]] §4.5, limit theorems §9, Cauchy sequences §10a). All of them hold verbatim in $F$. So $\Phi_F : \widehat{\mathbb{Q}} \to F$, $[(q_n)] \mapsto \lim q_n$, is an isomorphism of ordered fields.
>
> *Two fields.* If $F_1, F_2$ are complete ordered fields, then $\Phi_{F_2} \circ \Phi_{F_1}^{-1} : F_1 \to F_2$ is a bijection preserving sums, products and order.

^pf-6s-14

*Uses:* [[§3 The Set ℝ of Real Numbers#^prop-3-1|§3.1]], [[§6★ ℝ from Cauchy Sequences of Rationals#^thm-6s-12|§6★.12]]

> [!remark] Remark: The Order of Logic, and Functional Analysis
> The completion of a metric space in functional analysis ([[§11 Completeness#^def-11-3|556 Def. §11.3]], [[§11 Completeness#^def-11-4|556 Def. §11.4]]) is this construction with $\mathbb{Q}$ replaced by any metric space $M$. It cannot construct ℝ, because its metric $\bar d([\{x_n\}], [\{y_n\}]) = \lim d(x_n, y_n)$ ([[§11 Completeness#^prop-11-3|556 Proposition §11.3]]) is a *real* number, obtained from Cauchy implies convergent in ℝ. That is why this note restricts $\varepsilon$ to $\mathbb{Q}$ and puts the order on $\widehat{\mathbb{Q}}$ by hand ([[§6★ ℝ from Cauchy Sequences of Rationals#^def-6s-new2|Def. §6★.4]]) instead of measuring distances.
>
> Once ℝ exists, the two constructions agree. Applied to $M = \mathbb{Q}$ with $d(p, q) = |p - q|$, 556's equivalence relation is $\sim$ of [[§6★ ℝ from Cauchy Sequences of Rationals#^def-6s-2|Def. §6★.2]] (rational tolerances suffice, as in the proof of [[§6★ ℝ from Cauchy Sequences of Rationals#^thm-6s-12|Theorem §6★.12]]), so 556's completion $\overline{M}$ for $M = \mathbb{Q}$ is $\widehat{\mathbb{Q}}$ as a set (this $\overline{\mathbb{Q}}$ is not the field of algebraic numbers of [[§2 The Set ℚ of Rational Numbers#^def-2-5|Def. §2.5]]). The dictionary:
>
> | Here | Functional Analysis |
> |---|---|
> | [[§6★ ℝ from Cauchy Sequences of Rationals#^cor-6s-9\|Cor. §6★.9]] (a class is the limit of its representative) | [[§11 Completeness#^prop-11-3\|556 Prop. §11.3]](c) ($M$ dense in $\overline{M}$) |
> | [[§6★ ℝ from Cauchy Sequences of Rationals#^thm-6s-10\|Thm. §6★.10]] (Cauchy complete) | [[§11 Completeness#^prop-11-3\|556 Prop. §11.3]](d) ($\overline{M}$ complete) |
> | [[§6★ ℝ from Cauchy Sequences of Rationals#^thm-6s-12\|Thm. §6★.12]] ($\Phi = \lim$ onto ℝ) | [[§11 Completeness#^prop-11-5\|556 Prop. §11.5]] (identifying a completion: $\Phi = \lim J x_n$) |
> | [[§6★ ℝ from Cauchy Sequences of Rationals#^cor-6s-14\|Cor. §6★.14]] (uniqueness) | [[§11 Completeness#^cor-11-6\|556 Cor. §11.6]] (uniqueness of the completion) |
>
> So ℝ *is* the completion of $\mathbb{Q}$, in the sense of [[Completion of a Normed Space|556 §11]]: $\mathbb{Q}$ sits densely in ℝ ([[§4 The Completeness Axiom#^thm-4-7|Theorem §4.7]]), and ℝ is complete ([[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|Theorem §10.8]]). Functional analysis then runs the same machine on function spaces: $L^p[a, b]$ is the completion of $C[a, b]$ under $\|\cdot\|_p$ ([[§17 The Function Spaces Lᵖ(Ω)#^prop-17-8|556 Proposition §17.8]]).

^rem-6s-2

> [!remark] Remark: The Distance Decides
> The construction used only the absolute value $|p - q|$ on $\mathbb{Q}$. With a different absolute value the same steps give a different complete field: the $p$-adic absolute value on $\mathbb{Q}$ produces the $p$-adic numbers $\mathbb{Q}_p$, which cannot be ordered compatibly with the field operations. The cut route has no analogue there, since it uses the order. Functional analysis makes the same point: one space with two norms can have two different completions, e.g. $C[a, b]$ is complete under $\|\cdot\|_\infty$ but completes to $L^1$ under $\|\cdot\|_1$ ([[§11 Completeness#^rem-11-9|556 Remark §11 (the norm decides)]]).

^rem-6s-3
