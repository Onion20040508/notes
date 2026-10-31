---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6a
section: C6a.5
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6a.4 The Interacting Vacuum and the Two-Point Function]] · ↑ [[· C6a Interactions and Correlation Functions]] · [[§C6a.6 Wick's Theorem]] →

*Sources: the user's PHY 513 notes, Ch. 14 §14.1 (Definition "Positive and negative frequency parts; normal ordering", paragraph "The price of reordering"), §14.2 (Derivation "Two fields (recalled)", Definition "Contraction") · PHY 513 Lecture 14 (Larsen, 26 Oct 2026), Part A, slides 2–3, 6–8, and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.3, pp. 88–89, eqs. (4.32)–(4.37) · Yu Zhao-Huan, 量子场论讲义, §6.3.1, eqs. (6.131)–(6.133), (6.140)–(6.144), (6.154)–(6.165).*

The master formula ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-6|Theorem §C6a.4.6]], for $n$ points [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-7|Theorem §C6a.4.7]]) reduced the interacting correlators to free-vacuum expectation values $\langle0|T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_n)\}|0\rangle$ of the free field. Expanding the exponential in $\lambda$ makes $n$ grow by four at each order: two fields at zeroth order, six at first, ten at second ("go all the way to Christmas", the lecture). Lecture 14 studies the operator $T\{\hat\phi_1\cdots\hat\phi_n\}$ itself, without the vacuum, which is harder but more useful (slide 6). The tool is the split of the free field into positive and negative frequencies ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]) and normal ordering ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]). This section states normal ordering for $n$ fields and computes the price of reordering: moving a $\hat\phi^+$ past a $\hat\phi^-$ costs the number $D_W$, and time ordering turns that cost into $D_F$. It then defines the class's rule for paying it, the contraction: replace a pair of fields by $D_F$ of their two points and normal order the rest. For two fields the rule reproduces the identity $T\{\hat\phi_1\hat\phi_2\} = \,:\!\hat\phi_1\hat\phi_2\!:\, + D_F(x_1 - x_2)$ of C2b ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]]). Yu treats this in §6.3.1, eqs. (6.131)–(6.165), for bosons and fermions at once (a sign $\epsilon_{ab}$ for exchanging fermion fields), in the setting of the Dyson series of the $S$-operator (6.126).

*Conventions* ([[Larsen PHY 513]]): in §C6a.5–§C6a.6 every field is a free field, the interaction-picture field of [[§C6a.2 The Interaction Picture#^thm-c6a-2-1|Theorem §C6a.2.1]], written $\hat\phi$ without the subscript $I$ (slides 8, 10; PS p. 89: "we will often drop the subscript $I$"), and $\hat\phi_i \equiv \hat\phi_I(x_i)$; normal ordering is written with colons, $:\!\cdots\!:$, which the slides and PS write $N(\cdots)$ ([[§C6a.5 Normal Ordering and Contractions#^cau-c6a-5-1|Caution: Names for normal ordering and contractions]]).

## Recap: the free field and its two-point functions

Lecture 14 opens with a two-slide "cheat sheet" (slides 2–3): the master formula, the mode expansion of the interaction-picture field, the Wightman function and the Feynman propagator. The split of the field into the parts that annihilate and create, and the two vacuum conditions that make it useful (slide 6):

![[§C2b.1 Heisenberg Fields#^thm-c2b-1-5]]

Normal ordering, defined on products of ladder operators and extended linearly to products of fields:

![[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1]]

The Feynman propagator, the vacuum expectation value of the time-ordered product, with its four-momentum form $D_F(x - y) = \int\frac{d^4p}{(2\pi)^4}\frac{i}{p^2 - m^2 + i\varepsilon}e^{-ip\cdot(x-y)}$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]):

![[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2]]

## Normal-ordered products of $n$ fields

> [!theorem] Theorem §C6a.5.1: The Normal-Ordered Product of n Free Fields
> For free fields $\hat\phi_i = \hat\phi_i^+ + \hat\phi_i^-$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]) and normal ordering as in [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]:
> 1. $:\!\hat\phi_1\cdots\hat\phi_n\!: = \displaystyle\sum_{A\subseteq\{1,\dots,n\}}\;\prod_{i\in A}\hat\phi_i^-\;\prod_{j\notin A}\hat\phi_j^+$, a sum of $2^n$ terms, each with every $\hat\phi^-$ to the left of every $\hat\phi^+$; the order of the factors within each product is irrelevant.
> 2. $\langle0|:\!\hat\phi_1\cdots\hat\phi_n\!:|0\rangle = 0$ for $n \ge 1$.
> 3. $:\!\hat\phi_{\pi(1)}\cdots\hat\phi_{\pi(n)}\!: = \,:\!\hat\phi_1\cdots\hat\phi_n\!:$ for every permutation $\pi$: inside the colons the fields may be written in any order.
>
> This is the lecture's definition (slide 7: split every field, then "place any $\phi^+$ to the right", "forget that operators do not commute"), shown to agree with the definition by ladder operators.
>
> *Source: PHY 513 Lecture 14, slides 6–7 · the user's PHY 513 notes, Ch. 14 §14.1 (Definition "Positive and negative frequency parts; normal ordering", with its two consequences) · PS §4.3, p. 88, eq. (4.34) · Yu §6.3.1, eqs. (6.140)–(6.144)*

^thm-c6a-5-1

> [!derivation]- Derivation
> **Step 1** (parts of the same kind commute). With $\hat\phi^+(x) = \int\frac{d^3p}{(2\pi)^3}\frac{\hat a_{\mathbf p}e^{-ip\cdot x}}{\sqrt{2E_{\mathbf p}}}$ and $\hat\phi^- = (\hat\phi^+)^\dagger$,
>
> $$
> [\hat\phi^+(x), \hat\phi^+(y)] = \int\frac{d^3p}{(2\pi)^3}\frac{d^3q}{(2\pi)^3}\frac{e^{-ip\cdot x}e^{-iq\cdot y}}{\sqrt{2E_{\mathbf p}2E_{\mathbf q}}}\,[\hat a_{\mathbf p}, \hat a_{\mathbf q}] = 0 ,
> $$
>
> since $[\hat a_{\mathbf p}, \hat a_{\mathbf q}] = 0$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]); taking adjoints, $[\hat\phi^-(x), \hat\phi^-(y)] = 0$. So within $\prod_{i\in A}\hat\phi_i^-$ and within $\prod_{j\notin A}\hat\phi_j^+$ the order does not matter.
>
> **Step 2** (expand, $n = 2$). Label each term by the set $A$ of factors that contribute $\hat\phi^-$:
>
> $$
> \hat\phi_1\hat\phi_2 = (\hat\phi_1^+ + \hat\phi_1^-)(\hat\phi_2^+ + \hat\phi_2^-) = \underbrace{\hat\phi_1^+\hat\phi_2^+}_{A = \varnothing} + \underbrace{\hat\phi_1^+\hat\phi_2^-}_{A = \{2\}} + \underbrace{\hat\phi_1^-\hat\phi_2^+}_{A = \{1\}} + \underbrace{\hat\phi_1^-\hat\phi_2^-}_{A = \{1, 2\}} .
> $$
>
> **Step 3** (order, $n = 2$). Normal ordering ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]) is linear and acts on the mode integrals. Only the $A = \{2\}$ term has an $\hat a$ left of an $\hat a^\dagger$:
>
> $$
> \hat\phi_1^+\hat\phi_2^- = \int\frac{d^3p}{(2\pi)^3}\frac{d^3q}{(2\pi)^3}\frac{e^{-ip\cdot x_1}e^{iq\cdot x_2}}{\sqrt{2E_{\mathbf p}2E_{\mathbf q}}}\,\hat a_{\mathbf p}\hat a^\dagger_{\mathbf q} \;\xrightarrow{\;:\;:\;}\; \int\frac{d^3p}{(2\pi)^3}\frac{d^3q}{(2\pi)^3}\frac{e^{-ip\cdot x_1}e^{iq\cdot x_2}}{\sqrt{2E_{\mathbf p}2E_{\mathbf q}}}\,\hat a^\dagger_{\mathbf q}\hat a_{\mathbf p} = \hat\phi_2^-\hat\phi_1^+ ,
> $$
>
> with no commutator paid; the other three terms are already in order. So
>
> $$
> :\!\hat\phi_1\hat\phi_2\!: = \hat\phi_1^+\hat\phi_2^+ + \hat\phi_2^-\hat\phi_1^+ + \hat\phi_1^-\hat\phi_2^+ + \hat\phi_1^-\hat\phi_2^- ,
> $$
>
> the four terms of part 1 for $A = \varnothing, \{2\}, \{1\}, \{1, 2\}$.
>
> **Step 4** (expand and order, part 1). For $n$ fields the same two moves on $2^n$ terms:
>
> $$
> \hat\phi_1\cdots\hat\phi_n = \prod_{i=1}^n(\hat\phi_i^+ + \hat\phi_i^-) = \sum_{A\subseteq\{1,\dots,n\}}\hat\phi_1^{\pm}\hat\phi_2^{\pm}\cdots\hat\phi_n^{\pm}\Big|_{-\text{ for } i\in A,\ +\text{ for } i\notin A} \;\xrightarrow{\;:\;:\;}\; \sum_A\;\prod_{i\in A}\hat\phi_i^-\;\prod_{j\notin A}\hat\phi_j^+ ,
> $$
>
> each $\hat a^\dagger$ moved left of each $\hat a$ inside the mode integral as in Step 3, which moves every $\hat\phi_i^-$ to the left of every $\hat\phi_j^+$.
>
> **Step 5** (vacuum, part 2). Take the $A$-term of part 1. If $A^c \ne \varnothing$, pick $j_0 \in A^c$ and put $\hat\phi_{j_0}^+$ rightmost (Step 1); if $A^c = \varnothing$, then $A = \{1, \dots, n\} \ne \varnothing$ for $n \ge 1$, and put some $\hat\phi_{i_0}^-$ leftmost ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]):
>
> $$
> A^c \ne \varnothing\colon\ \Bigl(\prod_{i\in A}\hat\phi_i^-\prod_{j\notin A,\,j\ne j_0}\hat\phi_j^+\Bigr)\hat\phi_{j_0}^+|0\rangle = 0; \qquad A^c = \varnothing\colon\ \langle0|\hat\phi_{i_0}^-\prod_{i\ne i_0}\hat\phi_i^- = 0 .
> $$
>
> Every term has zero vacuum expectation value; for $n = 2$, the four terms of Step 3 are $0 + 0 + 0 + 0$ in $\langle0|\cdots|0\rangle$.
>
> **Step 6** (symmetry, part 3). Relabelling the fields by $\pi$ maps the subset $A$ to $\pi(A)$; the term for $\pi(A)$ of the relabelled product contains the same factors as the term for $A$ of the original, in an order that differs only inside the two groups, which is irrelevant by Step 1. For $n = 2$, $\pi = (12)$:
>
> $$
> :\!\hat\phi_2\hat\phi_1\!: = \hat\phi_2^+\hat\phi_1^+ + \hat\phi_1^-\hat\phi_2^+ + \hat\phi_2^-\hat\phi_1^+ + \hat\phi_2^-\hat\phi_1^- = \hat\phi_1^+\hat\phi_2^+ + \hat\phi_1^-\hat\phi_2^+ + \hat\phi_2^-\hat\phi_1^+ + \hat\phi_1^-\hat\phi_2^- = \,:\!\hat\phi_1\hat\phi_2\!: ,
> $$
>
> the first and last terms reordered by Step 1. Summing over all subsets gives the same operator for every $n$.
>
> **What the derivation shows.**
> - "Forget that operators do not commute" is consistent only because the reordering is done once, by definition, never derived from the commutation relations: $:\!\cdots\!:$ is not an operator identity but a new product.
> - Part 2 is the reason for introducing it: normal-ordered products are trivial in the vacuum.

^der-c6a-5-1

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]

> [!theorem] Theorem §C6a.5.2: The Price of Reordering Is the Wightman Function
> $$
> [\hat\phi^+(x), \hat\phi^-(y)] = D_W(x - y)\,\mathbf 1 = \int\frac{d^3p}{(2\pi)^3}\frac{1}{2E_{\mathbf p}}e^{-ip\cdot(x-y)}\,\mathbf 1, \qquad [\hat\phi^+(x), \hat\phi^+(y)] = [\hat\phi^-(x), \hat\phi^-(y)] = 0 ,
> $$
>
> with $D_W$ the Wightman function ([[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]]). Moving a $\hat\phi^+$ to the right of a $\hat\phi^-$ costs this $c$-number. This is Step 3 of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^der-c2b-6-6|Derivation §C2b.6.6]], stated as a result of its own.
>
> *Source: PHY 513 Lecture 14, slide 7 · the user's PHY 513 notes, Ch. 14 §14.1, eq. (phipmcomm) and paragraph "The price of reordering" · PS §4.3, eq. (4.33) · Yu §6.3.1, eq. (6.157)*

^thm-c6a-5-2

> [!derivation]- Derivation
> **Step 1** (insert both expansions, with distinct momenta).
>
> $$
> [\hat\phi^+(x), \hat\phi^-(y)] = \int\frac{d^3p}{(2\pi)^3}\frac{d^3q}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}\sqrt{2E_{\mathbf q}}}\,e^{-ip\cdot x}e^{+iq\cdot y}\,[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] ,
> $$
>
> with $p^0 = E_{\mathbf p}$, $q^0 = E_{\mathbf q}$.
>
> **Step 2** (the commutator). $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)\,\mathbf 1$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]): a number times the identity.
>
> **Step 3** (integrate the delta). Insert Step 2 into Step 1. The delta eliminates $\mathbf q$: $\mathbf q = \mathbf p$, hence $E_{\mathbf q} = E_{\mathbf p}$ and $q^0 = p^0$; the $(2\pi)^3$ cancels the $(2\pi)^{-3}$ of $d^3q$:
>
> $$
> [\hat\phi^+(x), \hat\phi^-(y)] = \int\frac{d^3p}{(2\pi)^3}\int d^3q\,\delta^3(\mathbf p - \mathbf q)\,\frac{e^{-ip\cdot x}e^{iq\cdot y}}{\sqrt{2E_{\mathbf p}}\sqrt{2E_{\mathbf q}}}\,\mathbf 1 = \int\frac{d^3p}{(2\pi)^3}\frac{e^{-ip\cdot x}e^{ip\cdot y}}{\sqrt{2E_{\mathbf p}}\sqrt{2E_{\mathbf p}}}\,\mathbf 1 = \int\frac{d^3p}{(2\pi)^3}\frac{1}{2E_{\mathbf p}}\,e^{-ip\cdot(x - y)}\,\mathbf 1 ,
> $$
>
> the mode integral of $D_W$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]]).
>
> **Step 4** (in what sense). The $\delta$ acts on the smooth integrand after smearing $x$ and $y$ with test functions; the result is the kernel of the tempered distribution $D_W$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]]), and the identity holds between operator-valued distributions ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|Theorem §C2b.1.6]]).
>
> **Step 5** (same kinds). Step 1 of [[§C6a.5 Normal Ordering and Contractions#^der-c6a-5-1|Derivation §C6a.5.1]].
>
> **What the derivation shows.**
> - Each field brings its own momentum integral, $1/\sqrt{2E}$ and plane wave; the commutator of $\hat a$ with $\hat a^\dagger$ removes one integral, sets the momenta equal and combines the rest into $D_W$ (the lecture's answer to the question below).
> - The commutator is a $c$-number: this is what makes the reordering of $n$ fields a combinatorial problem rather than an operator problem.
> - Used next: Wick's theorem ([[§C6a.6 Wick's Theorem|§C6a.6]]).

^der-c6a-5-2

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|Theorem §C2b.1.6]]

> [!remark] Remark: Why the commutator is exactly the Wightman function
> Asked in the lecture: why does $[\phi_1^+, \phi_2^-]$ equal $D_W$? "This one here was basically the $a$ with an $e^{-ipx}$ … This one here was the $a^\dagger$ with an $e^{ipx_2}$ … But then when I take a commutator with $a$ and $a^\dagger$, they become a delta function … They sort of each had an integral, but well, you got an $a^\dagger$, so same integral." Steps 1–3 of [[§C6a.5 Normal Ordering and Contractions#^der-c6a-5-2|Derivation §C6a.5.2]] are that answer written out; the vacuum expectation value of the same identity is the definition of $D_W$ ([[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]]).
>
> *Source: PHY 513 Lecture 14, transcript (question at 26:29) · the user's PHY 513 notes, Ch. 14 §14.1*

^rem-c6a-5-1

## The contraction

> [!remark] Remark: Normal order first, then pay for the reordering
> The lecture's strategy (slide 7): "address time-ordering after normal ordering." Normal ordering is defined by a rule that does not look at times, and normal-ordered products vanish in the vacuum ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 2). So the problem becomes: express what we want, a time-ordered product, through what is easy, normal-ordered products, and keep track of what the reordering costs. Each time a $\hat\phi^+(x_i)$ has to be moved to the right of a $\hat\phi^-(x_j)$, the cost is the commutator $[\hat\phi^+(x_i), \hat\phi^-(x_j)] = D_W(x_i - x_j)$, a number ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-2|Theorem §C6a.5.2]]). Inside a time-ordered product the later field stands to the left, so the cost paid is $D_W$ with the later point first, $\theta(x_i^0 - x_j^0)D_W(x_i - x_j) + \theta(x_j^0 - x_i^0)D_W(x_j - x_i)$, which is $D_F(x_i - x_j)$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]): time ordering turns the cost into the Feynman propagator. "Time order is actually what I want. Normal ordered is what I would like because I'm really good at computing with them … if they weren't already normal ordered … just do it and pay the price."
>
> *Source: PHY 513 Lecture 14, slides 7–8, and transcript · the user's PHY 513 notes, Ch. 14 §14.1 (paragraph "The price of reordering")*

^rem-c6a-5-2

> [!definition] Definition §C6a.5.1: Contraction
> To **contract** a pair $\hat\phi_i, \hat\phi_j$ in a product of free fields means to replace the two fields by the $c$-number $D_F(x_i - x_j)$, the Feynman propagator of their two points ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]). In Wick's theorem ([[§C6a.6 Wick's Theorem|§C6a.6]]) the fields that are not contracted are normal ordered: contracting $\hat\phi_i, \hat\phi_j$ in $\hat\phi_1\cdots\hat\phi_n$ gives the term $D_F(x_i - x_j)\,:\!\prod_{k\ne i,j}\hat\phi_k\!:$, and contracting several disjoint pairs gives one factor $D_F$ for each pair. Since $D_F$ is even, the order of the two fields in a pair does not matter. The slides and PS draw a contraction as a bracket over the pair (figure below); in formulas these notes write it $\overbracket{\hat\phi_i\hat\phi_j} = D_F(x_i - x_j)$, with the contracted pair side by side (allowed: fields inside $:\;:$ may be reordered, [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 3, and a contraction is a number).
>
> *Source: PHY 513 Lecture 14, slide 9 ("'contract' means replace any two fields with $D_F(x_i - x_j)$. Always normal order the remaining fields."), slide 10, and transcript ("What do I mean by contract? Replace by the corresponding $D_F$ … Contract any pair of two indices, and put the rest in normal order form") · the user's PHY 513 notes, Ch. 14 §14.2 (Definition "Contraction", paragraph "Contracting two pairs") · PS §4.3, eqs. (4.35)–(4.36) and p. 89 · Yu §6.3.1, eq. (6.161)*

^def-c6a-5-1

![[ph-qft-c6-5-1.svg]]
*The contraction as drawn on the slides and in PS: (a) a bracket over the pair stands for the $c$-number $D_F(x_i - x_j)$; (b) inside a product the bracket may join fields that are not adjacent, and the rest stays normal ordered ($N(\cdots)$ = the colons $:\!\cdots\!:$ of these notes). Added figure; bracket style of slide 10 and PS p. 89.*

> [!caution] Caution: Names for normal ordering and contractions
> - *Normal ordering:* the slides write $N(\phi_1\cdots\phi_n) = \,:\!\phi_1\cdots\phi_n\!:$ (slide 7); PS write $N(\cdots)$ (eq. (4.34); "in the literature one often sees the notation $:\!\phi_1\phi_2\!:$", footnote p. 88); Yu writes $\mathsf N[\cdots]$, "正规乘积" (normal product, §6.3.1). These notes use the colons only ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]). PS's $N\{\phi_1\cdots\phi_n + \text{all contractions}\}$ means: the normal-ordered product plus, for every set of contracted pairs, the product of their $D_F$'s times the normal-ordered product of the rest.
> - *Contraction:* the slides (slide 10) and PS (eq. (4.35)) draw a bracket over the pair; PS define it by the commutator in the time order of the two fields, which equals $D_F$ (eq. (4.36)). The vault writes the bracket in formulas as $\overbracket{\hat\phi_i\hat\phi_j}$ over a pair written side by side, and draws pairs that cross, as on slide 10, in figures. Yu's bracket is defined as the vacuum expectation value of the time-ordered product, $\langle0|\mathsf T[\Phi_a\Phi_b]|0\rangle$ (eq. (6.161)), with a sign $\epsilon_{ab}$ for fermions (eq. (6.163)); for free scalar fields this is $D_F$ as well ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]). The user's notes describe the contraction of two fields as the number that separates their time-ordered from their normal-ordered product, which agrees by [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]].
>
> *Source: PS §4.3, pp. 88–89 · Yu §6.3.1 · the user's PHY 513 notes, Ch. 14 §14.2 (Definition "Contraction") · PHY 513 Lecture 14, slides 7, 10*

^cau-c6a-5-1

## Two fields

For two fields the rule reproduces the two-field identity of C2b, the example of slide 8. Of the four terms of $\hat\phi_1\hat\phi_2$ ([[§C6a.5 Normal Ordering and Contractions#^der-c6a-5-1|Derivation §C6a.5.1]], Step 2), only $\hat\phi_1^+\hat\phi_2^-$ is out of order ($\hat\phi_1^-\hat\phi_2^-$ counts as ordered, there being no $\hat\phi^+$ to misplace); fixing it costs the commutator ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-2|Theorem §C6a.5.2]]):

$$
\hat\phi_1\hat\phi_2 = \hat\phi_1^+\hat\phi_2^+ + \bigl(\hat\phi_2^-\hat\phi_1^+ + [\hat\phi_1^+, \hat\phi_2^-]\bigr) + \hat\phi_1^-\hat\phi_2^+ + \hat\phi_1^-\hat\phi_2^- = \,:\!\hat\phi_1\hat\phi_2\!:\, + D_W(x_1 - x_2) .
$$

Time order. $:\!\hat\phi_1\hat\phi_2\!: = \,:\!\hat\phi_2\hat\phi_1\!:$ "for any time ordering" ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 3), so with [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]] and the bracket $\overbracket{\hat\phi_1\hat\phi_2} = D_F(x_1 - x_2)$ for the contraction ([[§C6a.5 Normal Ordering and Contractions#^def-c6a-5-1|Def. §C6a.5.1]]):

$$
\begin{aligned}
T\{\hat\phi_1\hat\phi_2\} &= \theta(x_1^0 - x_2^0)\,\hat\phi_1\hat\phi_2 + \theta(x_2^0 - x_1^0)\,\hat\phi_2\hat\phi_1\\
&= \theta(x_1^0 - x_2^0)\bigl(:\!\hat\phi_1\hat\phi_2\!: + D_W(x_1 - x_2)\bigr) + \theta(x_2^0 - x_1^0)\bigl(:\!\hat\phi_2\hat\phi_1\!: + D_W(x_2 - x_1)\bigr)\\
&= \,:\!\hat\phi_1\hat\phi_2\!:\, + \theta(x_1^0 - x_2^0)D_W(x_1 - x_2) + \theta(x_2^0 - x_1^0)D_W(x_2 - x_1) = \,:\!\hat\phi_1\hat\phi_2\!:\, + \overbracket{\hat\phi_1\hat\phi_2} .
\end{aligned}
$$

In the vacuum, $\langle0|:\!\hat\phi_1\hat\phi_2\!:|0\rangle = 0$ ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 2) and $\langle0|T\{\hat\phi_1\hat\phi_2\}|0\rangle = \overbracket{\hat\phi_1\hat\phi_2} = D_F(x_1 - x_2)$. So $T\{\hat\phi_1\hat\phi_2\}$ is the uncontracted normal-ordered term plus the one contraction, which is the theorem proved in C2b (its four-term route is Steps 1–4 of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^der-c2b-6-6|Derivation §C2b.6.6]]):

![[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6]]

(PS §4.3, eqs. (4.33)–(4.37); Yu §6.3.1, eqs. (6.154)–(6.160), (6.165).) The general case, $n$ fields, is Wick's theorem ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]).

> [!caution] Caution: Normal ordering here refers to the free modes
> The split $\hat\phi = \hat\phi^+ + \hat\phi^-$ and the vacuum conditions $\hat\phi^+|0\rangle = 0 = \langle0|\hat\phi^-$ are those of the free field and the free vacuum. The Heisenberg field of the interacting theory has no such split with respect to $|\Omega\rangle$, and none is needed: every statement of §C6a.5–§C6a.11 concerns the free fields $\hat\phi_I$ inside the master formula ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-7|Theorem §C6a.4.7]]), whose vacuum is $|0\rangle$.
>
> *Source: the user's PHY 513 notes, Ch. 14, introduction ("Throughout this chapter every field is an interaction-picture field") · PS §4.3, p. 88 ("This decomposition can be done for any free field")*

^cau-c6a-5-2

> [!caution] Caution: In what sense these identities hold
> $\hat\phi^\pm$ are operator-valued distributions, like $\hat\phi$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|Theorem §C2b.1.6]]). Smeared with test functions in every argument they are operators on states of finitely many particles. Products of fields at *distinct* points, their normal-ordered parts and the $c$-numbers $D_W$, $D_F$ are then well defined, and the identities of this section hold after smearing. At *coincident* points two things differ:
> 1. the normal-ordered product is still defined: its matrix elements are smooth ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-7|Theorem §C2b.6.7]], 1);
> 2. the contraction is not a number. At $\xi = 0$ both terms of $D_F$ are $D_W(0)$, and in the mode integral of [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], with $d^3p = 4\pi p^2\,dp$,
>
> $$
> \text{“}D_F(0)\text{”} = \text{“}D_W(0)\text{”} = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}} = \frac{1}{4\pi^2}\int_0^\infty\frac{p^2\,dp}{\sqrt{p^2 + m^2}} = \infty ,
> $$
>
> the integrand growing like $p$. ($0 \in \operatorname{sing\,supp}D_W$, [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-7|Theorem §C2b.6.7]], 2.)
>
> The four fields at one vertex of $\phi^4$ theory are at coincident points, so contractions among them are formal at this level ([[§C6a.1 From Free to Interacting Fields#^rem-c6a-1-4|§C6a.1, ★ Remark: In what sense φ̂⁴(x) is defined]]). They reappear as the first ultraviolet divergence ([[§C6a.10 Feynman Rules in Momentum Space#^rem-c6a-10-1|§C6a.10, Remark: The first ultraviolet divergence]]).
>
> *Source: written here, from [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-7|Theorem §C2b.6.7]] and [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]*

^cau-c6a-5-3

> [!remark]- Connections
> - Normal ordering the free Hamiltonian removed the zero-point energy; the same reordering, applied to a product of two fields at one point, turns that energy into $D_W$ at coincident points, and applied to time-ordered products it produces $D_F$ — [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-8|Theorem §C2b.6.8]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-3|§C2b.6, Remark: One mechanism, two products]].
> - Positive frequency goes with annihilation, negative with creation; the same split exists for the vector and Dirac fields (Yu eqs. (6.134)–(6.139)), and Wick's theorem for them uses it with signs for fermions — [[§C2b.1 Heisenberg Fields#^rem-c2b-1-3|§C2b.1, Remark: Negative frequency is creation, not negative energy]], [[§C4.8 The Gupta–Bleuler Condition and Physical Photons#^def-c4-8-1|Def. §C4.8.1]], [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-1|Def. §C5a.9.1]].
> - Normal ordering of creation and annihilation operators is the same operation in non-relativistic second quantization; what field theory adds is the relativistic measure $1/2E_{\mathbf p}$ in the commutator — [[§C12.2★ Second Quantization|QM §C12.2★]].
> - The contraction is the Feynman propagator, which is also a Green's function of the Klein–Gordon operator; this is why the lines of Feynman diagrams can be read both as amplitudes and as inverses of the field equation — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|Theorem §C2b.6.5]], [[§C6a.7 Feynman Diagrams for Correlation Functions|§C6a.7]].
