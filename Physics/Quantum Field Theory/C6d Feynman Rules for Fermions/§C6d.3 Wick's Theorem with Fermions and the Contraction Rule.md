---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6d
section: C6d.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6d.2 Contractions with External Fermions]] · ↑ [[· C6d Feynman Rules for Fermions]] · [[§C6d.4 First Order]] →

*Sources: PHY 513 Lecture 17 (Larsen, 4 Nov 2026), slides 15–17 and 21–23, and transcript · the user's PHY 513 notes, Lecture 17 update, §17.4 (Definition "The two propagators", Caution "$\psi\bar\psi$ is a matrix, not a number", paragraph "Where the fermion signs go"), §17.6 (Derivation "The relative sign (filled in)") · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.7, pp. 115–116, eqs. (4.105)–(4.111); pp. 119–120, eqs. (4.118)–(4.120) · Yu Zhao-Huan, 量子场论讲义, §6.3, eqs. (6.138)–(6.144) (fermionic normal products), §6.3.2 (the proof with the signs $\epsilon_{ab}$); §6.4.5, eq. (6.257); §7.1, p. 268 (boxed contraction rule), eqs. (7.42), (7.100)–(7.101) (closed loops).*

Wick's theorem trades a time-ordered product for normal-ordered products and contractions ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]). With fermions every reordering of two fermion fields costs a sign, built into the fermionic time ordering ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]]) and normal ordering ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]): "whenever time-ordering, normal ordering, or contraction requires reordering of fields ⇒ include explicit sign" (slide 22). This section defines the contraction ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^def-c6d-3-1|Def. §C6d.3.1]]), proves the two-field case of slide 21 ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]]) and the general theorem of slide 22 ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^ex-c6d-3-1|Example §C6d.3.1]]), and turns the signs of a fully contracted term into a count of crossing arcs ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]), the technique behind the relative sign of [[§C6d.5 Second Order|§C6d.5]] and the "$-$" of a closed fermion loop ([[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]]). Read as a recipe for $T$-matrix elements the crossing theorem is Yu's contraction rule ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-5|Theorem §C6d.3.5]]), the fermion form of [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-2|Theorem §C6c.3.2]]; the closed loop's $-1$ is proved in [[§C6d.4 First Order|§C6d.4]], where it first occurs. The value of the fermion contraction is the Dirac Feynman propagator $S_F$, [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], derived there from the mode expansion and from $D_F$ (slide 17: "Two independent derivations of the propagator (see HW)"). Yu proves bosons and fermions together in §6.3 ([[§C6a.6 Wick's Theorem#^rem-c6a-6-3|§C6a.6, Remark: Yu's route]]); PS state the fermionic version in §4.7, eqs. (4.105)–(4.111).

**Setup.** As in [[§C6a.6 Wick's Theorem|§C6a.6]]: identities between free (interaction-picture) fields, $\hat\psi$, $\hat{\bar\psi}$ of [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]] and $\hat\phi$ of [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]], valid in any state and independent of the dynamics; vacuum values in $|0\rangle$; between particle states with the states of [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]].

*Conventions* ([[Larsen PHY 513]]): $\hat\Phi_i$ stands for one of $\hat\psi_a(x_i)$, $\hat{\bar\psi}_b(x_i)$, $\hat\phi(x_i)$; $\epsilon_{ij} = -1$ if $\hat\Phi_i$ and $\hat\Phi_j$ are both fermion fields, $+1$ otherwise; $[A, B\}_\epsilon = AB - \epsilon BA$ (anticommutator for two fermion operators, commutator otherwise); $\hat\Phi^\pm$ the frequency parts ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]); normal ordering $:\;:$ with the sign of every fermion exchange ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]; the slides' $N[\cdots]$). A contraction is written as the value it equals, with its two fields named in their order, the left one first: for two fermion fields the value changes sign when they are exchanged ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^def-c6d-3-1|Def. §C6d.3.1]]). The bracket that the slides and PS draw over the pair appears in figures only.

## The contraction and the two-point case

> [!definition] Definition §C6d.3.1: Contraction of Two Free Fields, Fermions Included
> The **contraction** of two free fields $\hat\Phi_i$, $\hat\Phi_j$, taken in this order ($\hat\Phi_i$ written to the left of $\hat\Phi_j$), is the difference
>
> $$
> T\{\hat\Phi_i\hat\Phi_j\} - \,:\!\hat\Phi_i\hat\Phi_j\!: ,
> $$
>
> with the fermionic time ordering of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]] and the fermionic normal ordering of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]. For scalars this is [[§C6a.5 Normal Ordering and Contractions#^def-c6a-5-1|Def. §C6a.5.1]]. Its values are [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]]: in every case a $c$-number, equal to the vacuum value $\langle0|T\{\hat\Phi_i\hat\Phi_j\}|0\rangle$. As in Def. §C6a.5.1, formulas show a contraction as the value it equals ($S_F(x - y)_{ab}$, $D_F(x - y)$, a spinor times a plane wave), never as a bracket over the pair, and name the pair in words or by its positions; for two unspecified fields the value is written $\langle0|T\{\hat\Phi_i\hat\Phi_j\}|0\rangle$. The order of the two fields belongs to the name: for two fermion fields the contraction of $\hat\Phi_j$ with $\hat\Phi_i$ to its right is minus the contraction of $\hat\Phi_i$ with $\hat\Phi_j$ to its right.
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]], [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free fields, any state.
>
> *Source: PHY 513 Lecture 17, slide 21 ("$T(\psi(x)\bar\psi(y)) = N(\psi(x)\bar\psi(y))$ + contraction") · PS §4.7, p. 116, eq. (4.107) · Yu §6.3, eq. (6.161) (the contraction as a vacuum value; [[§C6a.6 Wick's Theorem#^rem-c6a-6-3|§C6a.6, Remark: Yu's route]])*

^def-c6d-3-1

> [!theorem] Theorem §C6d.3.1: Wick's Theorem for Two Fermion Fields; the Fermion Contractions
> For free Dirac fields the contraction of $\hat\psi_a(x)$ with $\hat{\bar\psi}_b(y)$ to its right is $S_F(x - y)_{ab}$:
>
> $$
> T\{\hat\psi_a(x)\hat{\bar\psi}_b(y)\} = \,:\!\hat\psi_a(x)\hat{\bar\psi}_b(y)\!:\; + S_F(x - y)_{ab} , \qquad S_F(x - y)_{ab} = \begin{cases}\langle0|\hat\psi_a(x)\hat{\bar\psi}_b(y)|0\rangle , & x^0 > y^0\\ -\langle0|\hat{\bar\psi}_b(y)\hat\psi_a(x)|0\rangle , & y^0 > x^0\end{cases} ,
> $$
>
> a $c$-number, the Dirac Feynman propagator $S_F(x - y)_{ab} = \langle0|T\{\hat\psi_a(x)\hat{\bar\psi}_b(y)\}|0\rangle$ of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], whose momentum-space form $\int\frac{d^4p}{(2\pi)^4}\frac{i(\slashed{p} + m)_{ab}}{p^2 - m^2 + i\varepsilon}e^{-ip\cdot(x - y)}$ is stated there (slide 17). The other pairs (the pair, left field first, $\longmapsto$ its contraction):
>
> $$
> \hat{\bar\psi}_b(y),\ \hat\psi_a(x) \;\longmapsto\; -S_F(x - y)_{ab} , \qquad \hat\psi,\ \hat\psi \;\longmapsto\; 0 , \qquad \hat{\bar\psi},\ \hat{\bar\psi} \;\longmapsto\; 0 , \qquad \hat\psi,\ \hat\phi \;\longmapsto\; 0 , \qquad \hat{\bar\psi},\ \hat\phi \;\longmapsto\; 0 , \qquad \hat\phi(x),\ \hat\phi(y) \;\longmapsto\; D_F(x - y) :
> $$
>
> "contract any $\psi$ with any $\bar\psi$ (in that order)"; "$\psi\psi$ and $\bar\psi\bar\psi$ do not give contractions" (slide 22).
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free fields, $x^0 \ne y^0$ (the function $S_F$ itself is defined for all $x - y$ as a distribution, [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]]); an operator identity, any state.
>
> *Source: PHY 513 Lecture 17, slide 21 (statement and "Proof: (assuming $x^0 > y^0$) … Only 2nd term is not normal-ordered … Note: explicit '$-$' for normal-ordered term"), slide 22, slide 16 ("$\psi(x)\bar\psi(y)$ contracted $= \frac{i(\slashed p + m)}{p^2 - m^2 + i\epsilon}$") · the user's PHY 513 notes, Lecture 17 update, §17.4, Definition "The two propagators" (eq. (SF), the fermionic $T$) · PS §4.7, p. 116, eqs. (4.107)–(4.109) · Yu §6.4.5, eqs. (6.257)–(6.258) · the case $y^0 > x^0$ and the vanishing contractions written here*

^thm-c6d-3-1

> [!derivation]- Derivation
> **Step 1** (case $x^0 > y^0$; slide 21). $T\{\hat\psi_a(x)\hat{\bar\psi}_b(y)\} = \hat\psi_a(x)\hat{\bar\psi}_b(y)$. Split both fields ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]]; indices suppressed):
>
> $$
> \hat\psi(x)\hat{\bar\psi}(y) = \hat\psi^+(x)\hat{\bar\psi}^+(y) + \hat\psi^+(x)\hat{\bar\psi}^-(y) + \hat\psi^-(x)\hat{\bar\psi}^+(y) + \hat\psi^-(x)\hat{\bar\psi}^-(y) .
> $$
>
> Only the second term has an annihilation part ($\hat\psi^+$: $\hat a$'s) left of a creation part ($\hat{\bar\psi}^-$: $\hat a^\dagger$'s). Rewrite it: $\hat\psi^+(x)\hat{\bar\psi}^-(y) = \{\hat\psi^+(x), \hat{\bar\psi}^-(y)\} - \hat{\bar\psi}^-(y)\hat\psi^+(x)$. The normal-ordered product is, by [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]] (one exchange, one sign),
>
> $$
> :\!\hat\psi(x)\hat{\bar\psi}(y)\!: = \hat\psi^+(x)\hat{\bar\psi}^+(y) - \hat{\bar\psi}^-(y)\hat\psi^+(x) + \hat\psi^-(x)\hat{\bar\psi}^+(y) + \hat\psi^-(x)\hat{\bar\psi}^-(y) ,
> $$
>
> so $T\{\hat\psi\hat{\bar\psi}\} - :\!\hat\psi\hat{\bar\psi}\!: = \{\hat\psi^+(x), \hat{\bar\psi}^-(y)\}$: "explicit '$-$' for normal-ordered term".
>
> **Step 2** (a $c$-number). $\{\hat\psi^+_a(x), \hat{\bar\psi}^-_b(y)\}$ is a double integral of $u^r_a(p)\bar u^s_b(q)e^{-ip\cdot x + iq\cdot y}\{\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}\}$, and $\{\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}\} = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$ is a number ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]): the anticommutator is a multiple of the identity. A multiple of the identity equals its vacuum value; taking $\langle0|\cdots|0\rangle$ of Step 1, where $\langle0|:\cdots:|0\rangle = 0$, gives $\{\hat\psi^+(x), \hat{\bar\psi}^-(y)\} = \langle0|\hat\psi(x)\hat{\bar\psi}(y)|0\rangle = \langle0|T\{\hat\psi(x)\hat{\bar\psi}(y)\}|0\rangle$. (Evaluating the spin sum in this vacuum value is the derivation of $S_F$ in [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]] (Problem Set 9, Problem 1(a)); it is not needed here.)
>
> **Step 3** (case $y^0 > x^0$). $T\{\hat\psi(x)\hat{\bar\psi}(y)\} = -\hat{\bar\psi}(y)\hat\psi(x)$ ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]]) $= -\hat{\bar\psi}^+\hat\psi^+ - \hat{\bar\psi}^+\hat\psi^- - \hat{\bar\psi}^-\hat\psi^+ - \hat{\bar\psi}^-\hat\psi^-$ (arguments $y$, $x$). The non-normal term is $\hat{\bar\psi}^+(y)\hat\psi^-(x) = \{\hat{\bar\psi}^+(y), \hat\psi^-(x)\} - \hat\psi^-(x)\hat{\bar\psi}^+(y)$. Two annihilation parts anticommute exactly, $\{\hat{\bar\psi}^+, \hat\psi^+\} = 0$ (they contain $\hat b$ and $\hat a$; $\{\hat b, \hat a\} = 0$), and so do two creation parts: $-\hat{\bar\psi}^+\hat\psi^+ = \hat\psi^+\hat{\bar\psi}^+$, $-\hat{\bar\psi}^-\hat\psi^- = \hat\psi^-\hat{\bar\psi}^-$. Hence
>
> $$
> T\{\hat\psi(x)\hat{\bar\psi}(y)\} = \hat\psi^+\hat{\bar\psi}^+ + \hat\psi^-\hat{\bar\psi}^+ - \hat{\bar\psi}^-\hat\psi^+ + \hat\psi^-\hat{\bar\psi}^- - \{\hat{\bar\psi}^+(y), \hat\psi^-(x)\} = \,:\!\hat\psi(x)\hat{\bar\psi}(y)\!:\; - \{\hat{\bar\psi}^+(y), \hat\psi^-(x)\} ,
> $$
>
> and the contraction is $-\{\hat{\bar\psi}^+(y), \hat\psi^-(x)\} = -\langle0|\hat{\bar\psi}(y)\hat\psi(x)|0\rangle$ (a $c$-number by the $\hat b$, $\hat b^\dagger$ anticommutator, as in Step 2) $= \langle0|T\{\hat\psi(x)\hat{\bar\psi}(y)\}|0\rangle$.
>
> **Step 4** (one function). Both cases give $\langle0|T\{\hat\psi_a(x)\hat{\bar\psi}_b(y)\}|0\rangle$, which is the definition of $S_F(x - y)_{ab}$ in [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]] (slide 21: "$= S_F(x - y)$, definition").
>
> **Step 5** (the order $\hat{\bar\psi}\hat\psi$). $T\{\hat{\bar\psi}_b(y)\hat\psi_a(x)\} = -T\{\hat\psi_a(x)\hat{\bar\psi}_b(y)\}$ and $:\!\hat{\bar\psi}_b\hat\psi_a\!: = -:\!\hat\psi_a\hat{\bar\psi}_b\!:$ (one exchange each), so their difference is $-S_F(x - y)_{ab}$.
>
> **Step 6** (the zero contractions). For $\hat\psi_a(x)\hat\psi_b(y)$, $x^0 > y^0$, the only non-normal term is $\hat\psi^+_a(x)\hat\psi^-_b(y)$, and $\{\hat\psi^+_a, \hat\psi^-_b\}$ contains only $\{\hat a, \hat b^\dagger\} = 0$; the other time order and $\hat{\bar\psi}\hat{\bar\psi}$ ($\{\hat b, \hat a^\dagger\} = 0$) alike. A Dirac and a scalar field act on different Fock factors and commute: $T = :\;:$, contraction $0$. The scalar contraction is [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-6|Theorem §C2b.7.6]].
>
> **What the derivation shows.**
> - As for the scalar, the contraction is "the price of reordering": an anticommutator of a positive- with a negative-frequency part, a number, which the time ordering turns into the Feynman function.
> - ⚑ By-product: a fermion contraction is antisymmetric in its two fields; the sign is a matter of writing order, never of time order → [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]].

^der-c6d-3-1

*Uses:* [[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-6|Theorem §C2b.7.6]]

> [!caution] Caution: S_F is a 4 × 4 matrix; do not contract its indices
> $\hat\psi_a$ is a column, $\hat{\bar\psi}_b$ a row, written in the contraction in the reverse order compared with the scalar $\bar\psi\psi$; their contraction $S_F(x - y)_{ab}$ is a $4\times4$ matrix, matching $i(\slashed p + m)_{ab}$ with $\slashed p = \gamma^\nu p_\nu$ and $m$ times the unit matrix. Its two indices are not contracted with each other, even where that looks possible; otherwise the rule makes no sense. Write the indices $ab$ explicitly; the indices are contracted only along a fermion line, by the vertices ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]).
>
> *Source: PHY 513 Lecture 17, transcript (about 53–56 min) · the user's PHY 513 notes, Lecture 17 update, §17.4, Caution "$\psi\bar\psi$ is a matrix, not a number"*

^cau-c6d-3-1

## The general theorem

> [!theorem] Theorem §C6d.3.2: Wick's Theorem with Fermions
> For free fields $\hat\Phi_1, \dots, \hat\Phi_n$ at pairwise different times,
>
> $$
> T\{\hat\Phi_1\cdots\hat\Phi_n\} = \sum_C\;\epsilon(C)\prod_{\{i<j\}\in C}\langle0|T\{\hat\Phi_i\hat\Phi_j\}|0\rangle\;:\!\prod_{k\notin\cup C}\hat\Phi_k\!: ,
> $$
>
> the sum over all sets $C$ of disjoint pairs, each contraction taken in the written order ($i < j$: the factor $\langle0|T\{\hat\Phi_i\hat\Phi_j\}|0\rangle$ is the contraction of $\hat\Phi_i$ with $\hat\Phi_j$ to its right, [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^def-c6d-3-1|Def. §C6d.3.1]]) with the values of [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]], the uncontracted fields normal ordered in their written order, and
>
> $$
> \epsilon(C) = \text{the sign of the permutation of the fermion fields that brings every pair of } C \text{ next to each other (in written order) at the front, the uncontracted fields keeping their order.}
> $$
>
> In words (slide 22): "$T[\psi_1\bar\psi_2\psi_3\bar\psi_4\ldots] = N[\psi_1\bar\psi_2\psi_3\bar\psi_4\ldots]$ + all possible contractions … Whenever time-ordering, normal ordering, or contraction requires reordering of fields ⇒ include explicit sign." For scalar fields alone $\epsilon(C) = 1$ and this is [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]. Vacuum values: only $C$ with every field contracted survive. Contractions at a common time inside one package ($\hat{\bar\psi}\hat\psi$ at one vertex) are made in the written order: the contraction of $\hat{\bar\psi}_a(x)$ with $\hat\psi_a(x)$ to its right is $-S_F(0)_{aa} = -\operatorname{tr}S_F(0)$ (Yu (7.42)).
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]], [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free fields, an operator identity, any state, independent of the dynamics; used inside the Dyson series of [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]].
>
> *Source: PHY 513 Lecture 17, slide 22 (general statement and the example of [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^ex-c6d-3-1|Example §C6d.3.1]]), slide 15 ("Wick's theorem: trade for normal-ordering + 'contractions'"), slide 23 ("All signs determined unambiguously by Wick's theorem") · the user's PHY 513 notes, Lecture 17 update, §17.4 ("Pick a pair, replace it by its contraction, normal order the rest, and repeat for all pairs") · PS §4.7, p. 116, eqs. (4.110)–(4.111) ("The proof is essentially unchanged from the bosonic case, since all extra minus signs are accounted for by the above definitions") · Yu §6.3.1, eq. (6.166) with the signs of (6.140)–(6.143); §6.3.2, (6.169)–(6.193) · proof written here, PS's route of [[§C6a.6 Wick's Theorem#^der-c6a-6-2b|Derivation §C6a.6.2b]] with signs*

^thm-c6d-3-2

> [!derivation]- Derivation
> **Step 1** (both sides change alike under exchange). Exchange two neighbouring fields $\hat\Phi_i$, $\hat\Phi_{i+1}$ in the written order. The left side changes by $\epsilon_{i,i+1}$: $T$ is the product in time order times the sign of the permutation used, and the new written order differs by one exchange ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]]). Each term on the right changes by the same $\epsilon_{i,i+1}$: (a) both uncontracted: $:\;:$ changes by $\epsilon_{i,i+1}$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]); (b) contracted with each other: the pair is written in the other order, and $\langle0|T\{\hat\Phi_{i+1}\hat\Phi_i\}|0\rangle = \epsilon_{i,i+1}\langle0|T\{\hat\Phi_i\hat\Phi_{i+1}\}|0\rangle$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]], Step 5), $\epsilon(C)$ unchanged; (c) otherwise $\epsilon(C)$ is the sign of a permutation composed with the exchange, so it changes by $\epsilon_{i,i+1}$. Hence it suffices to prove the theorem for $x_1^0 > x_2^0 > \cdots > x_n^0$.
>
> **Step 2** (start). $n = 1$: $T\{\hat\Phi_1\} = \hat\Phi_1 = \,:\!\hat\Phi_1\!:$. $n = 2$: [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]] (and [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-6|Theorem §C2b.7.6]] for scalars).
>
> **Step 3** (prepend the latest field). With $x_1^0$ the latest, $T\{\hat\Phi_1\cdots\hat\Phi_n\} = \hat\Phi_1\,T\{\hat\Phi_2\cdots\hat\Phi_n\}$, no sign ($\hat\Phi_1$ is already in place). By the induction hypothesis,
>
> $$
> T\{\hat\Phi_1\cdots\hat\Phi_n\} = \bigl(\hat\Phi_1^- + \hat\Phi_1^+\bigr)\sum_{C'}\epsilon(C')\prod_{\{i<j\}\in C'}\langle0|T\{\hat\Phi_i\hat\Phi_j\}|0\rangle\;:\!R(C')\!: ,
> $$
>
> $C'$ over the sets of pairs of $\{2, \dots, n\}$, $R(C')$ the uncontracted ones in written order; the contractions are $c$-numbers and commute with everything.
>
> **Step 4** ($\hat\Phi_1^-$). A creation part on the left is in normal order: $\hat\Phi_1^-:\!R\!: = \,:\!\hat\Phi_1^-R\!:$ (no exchange, no sign).
>
> **Step 5** ($\hat\Phi_1^+$). For $l \in R$ write $:\!R\!: = \eta_l\,:\!\hat\Phi_l\,R_{\ne l}\!:$, $\eta_l = \prod_k\epsilon_{kl}$ over the $k \in R$ written before $l$ (moving $\hat\Phi_l$ to the front of the normal-ordered product), and $:\!\hat\Phi_lR_{\ne l}\!: = \hat\Phi_l^-:\!R_{\ne l}\!: + :\!\hat\Phi_l^+R_{\ne l}\!:$. Moving $\hat\Phi_1^+$ to the right through a normal-ordered product, it passes annihilation parts at the cost $\epsilon$ only ($[\hat\Phi_1^+, \hat\Phi_k^+\}_\epsilon = 0$: annihilation parts (anti)commute exactly), and each creation part $\hat\Phi_l^-$ leaves the number
>
> $$
> \hat\Phi_1^+\hat\Phi_l^- = \epsilon_{1l}\,\hat\Phi_l^-\hat\Phi_1^+ + [\hat\Phi_1^+, \hat\Phi_l^-\}_\epsilon , \qquad [\hat\Phi_1^+, \hat\Phi_l^-\}_\epsilon = \langle0|T\{\hat\Phi_1\hat\Phi_l\}|0\rangle \quad (x_1^0 > x_l^0) ,
> $$
>
> the last equality being Step 1 of [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^der-c6d-3-1|Derivation §C6d.3.1]] in general form ($T - :\;:$ equals the reordered non-normal term): the number is the contraction of $\hat\Phi_1$ with $\hat\Phi_l$ to its right. Collecting: $\hat\Phi_1^+:\!R\!: = \,:\!\hat\Phi_1^+R\!: + \sum_{l\in R}\eta_l\,\langle0|T\{\hat\Phi_1\hat\Phi_l\}|0\rangle\,:\!R_{\ne l}\!:$, the first term because $\hat\Phi_1^+$ carried to the right end is in normal order with exactly the sign of $:\!\hat\Phi_1^+R\!:$.
>
> **Step 6** (the signs match). Steps 4–5 give $:\!\hat\Phi_1R\!:$ (for $C = C'$) and the terms $\epsilon(C')\eta_l\prod_{\{i<j\}\in C'}\langle0|T\{\hat\Phi_i\hat\Phi_j\}|0\rangle\,\langle0|T\{\hat\Phi_1\hat\Phi_l\}|0\rangle:\!R_{\ne l}\!:$ (for $C = C'\cup\{\{1, l\}\}$). The permutation of $\epsilon(C)$ for $C = C'\cup\{\{1, l\}\}$ is: first that of $C'$ on $2, \dots, n$ (sign $\epsilon(C')$), giving $\hat\Phi_1$, the pairs of $C'$, then $R$; then $\hat\Phi_l$ moved left to sit after $\hat\Phi_1$, past the pairs of $C'$ (each pair holds $0$ or $2$ fermion fields: no sign) and past the fields of $R$ before $l$ (sign $\eta_l$). So $\epsilon(C) = \epsilon(C')\eta_l$, and every set $C$ of pairs of $\{1, \dots, n\}$ appears once (Step 6 of [[§C6a.6 Wick's Theorem#^der-c6a-6-2|Derivation §C6a.6.2]]).
>
> **Step 7** (vacuum values). $\langle0|:\cdots:|0\rangle = 0$ for any nonempty normal-ordered product ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]): only full contractions survive.
>
> **What the derivation shows.**
> - The bosonic proof goes through with one change: every move past a fermion operator costs $-1$, and every commutator becomes an anticommutator. PS: "all extra minus signs are accounted for by the above definitions".
> - ⚑ By-product: the sign of a term is a property of the pattern of contractions in the written order → [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]] (crossings).

^der-c6d-3-2

*Uses:* [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-6|Theorem §C2b.7.6]], [[§C6a.6 Wick's Theorem#^der-c6a-6-2|Derivation §C6a.6.2]], [[§C6a.6 Wick's Theorem#^der-c6a-6-2b|Derivation §C6a.6.2b]]

> [!example] Example §C6d.3.1: Four Fermion Fields
> With $\hat\psi_i \equiv \hat\psi(x_i)$, $\hat{\bar\psi}_i \equiv \hat{\bar\psi}(x_i)$, $S_F(i - j) \equiv S_F(x_i - x_j)$ (spinor indices suppressed), [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]] gives (slide 22)
>
> $$
> \begin{aligned}
> T[\hat\psi_1\hat{\bar\psi}_2\hat\psi_3\hat{\bar\psi}_4] = {}& :\!\hat\psi_1\hat{\bar\psi}_2\hat\psi_3\hat{\bar\psi}_4\!:\\
> & + :\!\hat\psi_1\hat{\bar\psi}_2\!:S_F(3 - 4) + :\!\hat\psi_3\hat{\bar\psi}_4\!:S_F(1 - 2) - :\!\hat\psi_1\hat{\bar\psi}_4\!:S_F(3 - 2) - :\!\hat\psi_3\hat{\bar\psi}_2\!:S_F(1 - 4)\\
> & + S_F(1 - 2)S_F(3 - 4) - S_F(1 - 4)S_F(3 - 2) .
> \end{aligned}
> $$
>
> **Step 1** (which pairs). Of the six pairs, $\{1, 3\}$ ($\hat\psi\hat\psi$) and $\{2, 4\}$ ($\hat{\bar\psi}\hat{\bar\psi}$) contract to $0$; the others are $\{1, 2\}$, $\{3, 4\}$, $\{1, 4\}$, $\{2, 3\}$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]]).
>
> **Step 2** (one contraction). $\{1, 2\}$: already in front, $\epsilon = +1$, value $S_F(1 - 2)$, rest $:\!\hat\psi_3\hat{\bar\psi}_4\!:$. $\{3, 4\}$: move the block $\hat\psi_3\hat{\bar\psi}_4$ past $\hat\psi_1\hat{\bar\psi}_2$, $4$ exchanges, $\epsilon = +1$; rest $:\!\hat\psi_1\hat{\bar\psi}_2\!:$. $\{1, 4\}$: move $\hat{\bar\psi}_4$ left past $\hat\psi_3$, $\hat{\bar\psi}_2$: $2$ exchanges, $\epsilon = +1$, value $S_F(1 - 4)$; the rest in written order is $:\!\hat{\bar\psi}_2\hat\psi_3\!: = -:\!\hat\psi_3\hat{\bar\psi}_2\!:$. $\{2, 3\}$: move the block $\hat{\bar\psi}_2\hat\psi_3$ past $\hat\psi_1$: $2$ exchanges, $\epsilon = +1$; the pair is written $\hat{\bar\psi}_2\hat\psi_3$, $\hat{\bar\psi}$ first, value $-S_F(3 - 2)$; rest $:\!\hat\psi_1\hat{\bar\psi}_4\!:$.
>
> **Step 3** (two contractions). $\{\{1, 2\}, \{3, 4\}\}$: $\epsilon = +1$, $S_F(1 - 2)S_F(3 - 4)$. $\{\{1, 4\}, \{2, 3\}\}$: bring $\hat{\bar\psi}_4$ next to $\hat\psi_1$ ($2$ exchanges, $+1$): $\hat\psi_1\hat{\bar\psi}_4\hat{\bar\psi}_2\hat\psi_3$; values $S_F(1 - 4)$ for $\hat\psi_1$ with $\hat{\bar\psi}_4$ and $-S_F(3 - 2)$ for $\hat{\bar\psi}_2$ with $\hat\psi_3$ to its right, product $-S_F(1 - 4)S_F(3 - 2)$. The other pairings contain a zero pair.
>
> **Step 4** (count). $1 + 4 + 2 = 7$ nonzero terms, as on the slide. The vacuum value keeps the last line: $\langle0|T[\hat\psi_1\hat{\bar\psi}_2\hat\psi_3\hat{\bar\psi}_4]|0\rangle = S_F(1 - 2)S_F(3 - 4) - S_F(1 - 4)S_F(3 - 2)$, antisymmetric under $\hat\psi_1 \leftrightarrow \hat\psi_3$, as Fermi statistics demands.
>
> *Source: PHY 513 Lecture 17, slide 22 (the example, all seven terms) · the signs derived here*

^ex-c6d-3-1

## The sign of a term between particle states

> [!theorem] Lemma §C6d.3.3: Vacuum Values of Fermion Operator Strings; Crossing Signs
> 1. (*Crossings.*) Draw a pairing $P$ of positions $1, \dots, 2N$ in a row as arcs above the row. The sign of the permutation that brings every pair next to each other (in its order) is $(-1)^{\operatorname{cr}(P)}$, $\operatorname{cr}(P)$ the number of pairs of arcs that cross.
> 2. (*Vacuum values.*) Let $\hat O_1, \dots, \hat O_{2N}$ each be a linear combination (after smearing) of fermion annihilation and creation operators, e.g. $\sqrt{2E}\hat a^s_{\mathbf p}$, $\sqrt{2E}\hat b^{s\dagger}_{\mathbf p}$, or a component of $\hat\psi^\pm(x)$, $\hat{\bar\psi}^\pm(x)$. Then
>
> $$
> \langle0|\hat O_1\hat O_2\cdots\hat O_{2N}|0\rangle = \sum_P\,(-1)^{\operatorname{cr}(P)}\prod_{\{i<j\}\in P}\langle0|\hat O_i\hat O_j|0\rangle ,
> $$
>
> the sum over all pairings of the $2N$ positions; an odd number of operators has vacuum value $0$.
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free fermion operators in the free vacuum $|0\rangle$, exact; part 1 is combinatorics.
>
> *Source: PS §4.7, p. 119 ("can be untangled by moving $\bar\psi_y$ two spaces to the left, and so picks up a factor of $(-1)^2 = +1$") · the user's PHY 513 notes, Lecture 17 update, §17.6, Derivation "The relative sign (filled in)" ("when all pairs are drawn as arcs above the row, the sign of the term is $(-1)^{\text{number of crossings}}$, the number of transpositions needed to make every pair adjacent") · Yu §7.1, p. 268 ("调换场算符将纠缠的缩并线解开") · proof written here*

^lem-c6d-3-3

> [!derivation]- Derivation
> **Step 1** (part 1, the arc at position 1). Let $\{1, j\} \in P$. Move the operator at $j$ left to position $2$: it passes the $j - 2$ operators at $2, \dots, j - 1$, a sign $(-1)^{j-2}$. Among these, the ones whose partner also lies in $2, \dots, j - 1$ come in pairs (an even number); each of the others has its partner beyond $j$ (it cannot be $1$), so its arc crosses $\{1, j\}$. Hence $j - 2 \equiv c_{1j} \pmod 2$, $c_{1j}$ the number of arcs crossing $\{1, j\}$.
>
> **Step 2** (induction). After the move, the remaining $2N - 2$ positions keep their relative order and their arcs cross each other as before: $(-1)^{\operatorname{cr}(P)} = (-1)^{c_{1j}}(-1)^{\operatorname{cr}(P')}$ with $P' = P\setminus\{\{1, j\}\}$. Induction on $N$ (for $N = 1$: no crossing, no move) gives part 1.
>
> **Step 3** (part 2, peel off $\hat O_1$). Write $\hat O_1 = \hat O_1^+ + \hat O_1^-$ (annihilation and creation parts). $\langle0|\hat O_1^- = 0$. Anticommute $\hat O_1^+$ to the right: $\hat O_1^+\hat O_j = -\hat O_j\hat O_1^+ + \{\hat O_1^+, \hat O_j\}$; the anticommutator is a number (of the form $\{\hat a, \hat a^\dagger\}$ or $\{\hat b, \hat b^\dagger\}$, [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]), equal to its vacuum value $\langle0|\hat O_1^+\hat O_j^-|0\rangle = \langle0|\hat O_1\hat O_j|0\rangle$ (annihilation parts anticommute exactly, $\{\hat O_1^+, \hat O_j^+\} = 0$). After $\hat O_1^+$ has passed all operators it annihilates $|0\rangle$:
>
> $$
> \langle0|\hat O_1\cdots\hat O_{2N}|0\rangle = \sum_{j=2}^{2N}(-1)^{j-2}\,\langle0|\hat O_1\hat O_j|0\rangle\,\langle0|\hat O_2\cdots\widehat{\hat O_j}\cdots\hat O_{2N}|0\rangle ,
> $$
>
> the hat meaning "omitted".
>
> **Step 4** (induction). By the hypothesis for $2N - 2$ operators and Step 1 ($(-1)^{j-2} = (-1)^{c_{1j}}$), each term is $(-1)^{\operatorname{cr}(P)}\prod_P\langle0|\hat O_i\hat O_j|0\rangle$ for the pairing $P = \{\{1, j\}\}\cup P'$; every pairing arises once. For an odd number the recursion ends at one operator, $\langle0|\hat O|0\rangle = 0$.
>
> **What the derivation shows.**
> - "The number of interchanges needed to untangle the contractions" (PS) is the number of crossings modulo $2$: a picture, not a computation.

^der-c6d-3-3

*Uses:* [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]

> [!theorem] Theorem §C6d.3.4: The Sign of a Fully Contracted Term between Particle States
> Let $|i\rangle$, $\langle f|$ be fermion and scalar states written as in [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]] (bra: annihilators $A$; ket: creators $B$), and consider a term of $\langle f|T\{\hat{\mathcal H}_I(x_1)\cdots\hat{\mathcal H}_I(x_n)\}|i\rangle$ in [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] in which every field is contracted, with another field or with an external particle (no external particle paired with another: those are the $\delta$-lines of [[§C6c.3 Wick's Theorem between Particle States#^def-c6c-3-1|Def. §C6c.3.1]]). Write the fermion operators in one row,
>
> $$
> \langle0|\;A\;\bigl[\hat{\bar\psi}\hat\psi\bigr]_{x_1}\cdots\bigl[\hat{\bar\psi}\hat\psi\bigr]_{x_n}\;B\;|0\rangle ,
> $$
>
> the packages in any order, and draw each pair as an arc above the row (the figure after the derivation shows two such rows). Then the term is
>
> $$
> (-1)^{\#\text{crossings}}\times\prod_{\text{pairs}}(\text{value, in the written order}) ,
> $$
>
> with the values $+S_F(x - y)$ for a pair that stands in the row as $\hat\psi(x)$ before $\hat{\bar\psi}(y)$ and $-S_F(x - y)$ for a pair that stands as $\hat{\bar\psi}(y)$ before $\hat\psi(x)$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]]), the external spinors times plane waves of [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], and the scalar contractions ($D_F$, $e^{\mp ip\cdot x}$) without sign. Equivalently, $(-1)^{\#\text{crossings}}$ is the sign of the permutation that makes every contracted pair adjacent (each pair in its order in the row). The crossings are counted and the values are read in the same row: exchanging two packages can change the number of crossings by an odd number, and then a field–field pair stands in the opposite order and its value changes sign with it; the product does not depend on the order of the packages.
>
> *Equivalently,* the scalar case is [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]]: the same full contractions of fields and particles, every term with sign $+$.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* free fields between free states, exact for each term; with the scope of the Dyson series between free states ([[§C6c.2 Contractions with External Particles|§C6c.2]], lowest order of a process exact).
>
> *Source: PHY 513 Lecture 17, slide 18 ("Sign of amplitude: determine from explicit contractions if it is needed"), slide 20 ("Contract leftmost $\psi$ with external particle $|\vec k\rangle$ ⇒ reorder $(-)$"), slide 23, and transcript ("The one place where you get a problem is contracting exactly this with these external states") · the user's PHY 513 notes, Lecture 17 update, §17.6, Derivation "The relative sign (filled in)" (a derivation there, promoted to a theorem here; its Jordan–Wigner check) · PS §4.7, p. 119, eq. (4.118) and the two contractions after it · Yu §7.1, p. 268 (boxed: "当场算符次序保持相互作用拉氏量中的次序时，不会出现额外的负号") · proof written here*

^thm-c6d-3-4

> [!derivation]- Derivation
> **Step 1** (fix a time order). In the region $x_{\sigma(1)}^0 > \cdots > x_{\sigma(n)}^0$ of the vertex integrals, $T\{\hat{\mathcal H}_I(x_1)\cdots\} = \hat{\mathcal H}_I(x_{\sigma(1)})\cdots\hat{\mathcal H}_I(x_{\sigma(n)})$, an ordinary product, with no sign ([[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]], 2). The scalar fields commute with the fermion operators and factor out; their contractions are those of [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]].
>
> **Step 2** (the fermion string). The fermion part is $\langle0|A\,F_{\sigma(1)}\cdots F_{\sigma(n)}\,B|0\rangle$, $F_k = \hat{\bar\psi}_a\hat\psi_a(x_k)$, every operator a linear combination of $\hat a$, $\hat a^\dagger$, $\hat b$, $\hat b^\dagger$ (split each field into $\pm$ parts, [[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]]). By [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], 2, it is the sum over pairings of $(-1)^{\operatorname{cr}}\prod\langle0|\hat O_i\hat O_j|0\rangle$; the term of the theorem is the pairing $P$ that realizes the given contractions.
>
> **Step 3** (the pair values). External with field: $\langle0|\hat\psi(x)\sqrt{2E}\hat a^{s\dagger}_{\mathbf p}|0\rangle = u^s(p)e^{-ip\cdot x}$, $\langle0|\sqrt{2E}\hat a^s_{\mathbf p}\hat{\bar\psi}(x)|0\rangle = \bar u^s(p)e^{ip\cdot x}$, $\langle0|\sqrt{2E}\hat b^s_{\mathbf p}\hat\psi(x)|0\rangle = v^s(p)e^{ip\cdot x}$, $\langle0|\hat{\bar\psi}(x)\sqrt{2E}\hat b^{s\dagger}_{\mathbf p}|0\rangle = \bar v^s(p)e^{-ip\cdot x}$ ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]). Field with field, the left one at the later time (Step 1): $\langle0|\hat\psi(x)\hat{\bar\psi}(y)|0\rangle = \langle0|T\{\hat\psi(x)\hat{\bar\psi}(y)\}|0\rangle = S_F(x - y)$ for $x^0 > y^0$, and $\langle0|\hat{\bar\psi}(y)\hat\psi(x)|0\rangle = -\langle0|T\{\hat\psi(x)\hat{\bar\psi}(y)\}|0\rangle = -S_F(x - y)$ for $y^0 > x^0$ ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]]): the values of the theorem, with no reference to the region.
>
> **Step 4** (the written order instead of the time order). Steps 2–3 give, in the region of Step 1, $(-1)^{c_T}\prod(\text{values in the order of the time-ordered row})$, $c_T$ the number of crossings of $P$ in the time-ordered row. Passing from the time-ordered row to the written row permutes whole packages, each with two fermion operators: an even permutation of the row (Step 1 of [[§C6d.1 Yukawa Theory#^der-c6d-1-2|Derivation §C6d.1.2]]). A pair keeps its two members, but a field–field pair from two different packages may now stand in the opposite left–right order; let $r$ be the number of such pairs. The arrangement "all pairs adjacent, each pair in its row order" of the written row differs from that of the time-ordered row by one transposition inside each reversed pair, $r$ in all (the order of the adjacent pairs among themselves does not matter: a pair is two operators). So, by [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], 1, the number $c_W$ of crossings in the written row obeys
>
> $$
> (-1)^{c_W} = (+1)\cdot(-1)^{c_T}\cdot(-1)^r .
> $$
>
> The value of each reversed pair, read in its row order, changes sign as well: read as $\hat{\bar\psi}(y)$ before $\hat\psi(x)$ it is $-S_F(x - y)$, read as $\hat\psi(x)$ before $\hat{\bar\psi}(y)$ it is $+S_F(x - y)$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]]), so the product of the values changes by $(-1)^r$ too. Hence
>
> $$
> (-1)^{c_W}\prod(\text{values in the written order}) = (-1)^{c_T}\prod(\text{values in the time order}) :
> $$
>
> the product is the same for every order of the packages, although neither factor is. Pairs with an external operator never change their order ($A$ stays left of every field, $B$ right), nor does a pair inside one package. Example (one open line through two vertices): the row $\hat a\,[\hat{\bar\psi}\hat\psi]_x[\hat{\bar\psi}\hat\psi]_y\,\hat a^\dagger$ with the pairs $(\hat a, \hat{\bar\psi}_x)$, $(\hat\psi_x, \hat{\bar\psi}_y)$, $(\hat\psi_y, \hat a^\dagger)$ at positions $(1, 2)$, $(3, 4)$, $(5, 6)$ has no crossing, and the field–field pair reads $\hat\psi_x\hat{\bar\psi}_y$, value $+S_F(x - y)$; with the packages exchanged, $\hat a\,[\hat{\bar\psi}\hat\psi]_y[\hat{\bar\psi}\hat\psi]_x\,\hat a^\dagger$, the same pairs sit at $(1, 4)$, $(2, 5)$, $(3, 6)$, three crossings, and the field–field pair reads $\hat{\bar\psi}_y\hat\psi_x$, value $-S_F(x - y)$: $(+1)(+S_F) = (-1)^3(-S_F)$. Every region gives the same expression, which is the statement.
>
> **What the derivation shows.**
> - ⚑ Neither the number of crossings nor the pair values are separately independent of the order in which the packages are written: each changes by $-1$ for every field–field pair whose left–right order is reversed (Step 4). Only the product $(-1)^{\#\text{crossings}}\prod(\text{values in the written order})$ is; crossings must be counted in the same row in which the values are read (stated in the theorem).
> - Inside $T$ the packages move freely; only the contractions with the fixed external operators $A$ and $B$ can produce an overall or relative sign: "the only place where a sign must be tracked is the contraction with the external states" (the user's notes, §17.6). → [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-5|Theorem §C6d.3.5]]
> - Used next: the relative sign of $ff \to ff$ (2 vs 3 crossings, [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]]) and the closed loop ([[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]]).

^der-c6d-3-4

*Uses:* [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]], [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]], [[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]], [[§C6d.1 Yukawa Theory#^der-c6d-1-2|Derivation §C6d.1.2]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-5|P6, step 5]]

![[ph-qft-c6d-3-1.svg]]
*[[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]] for $f(p) + f(k) \to f(p') + f(k')$ ([[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]]): the eight fermion operators of $\langle0|\hat a_{\mathbf k'}\hat a_{\mathbf p'}[\hat{\bar\psi}\hat\psi]_x[\hat{\bar\psi}\hat\psi]_y\hat a^\dagger_{\mathbf p}\hat a^\dagger_{\mathbf k}|0\rangle$ with the contractions as arcs. Top, the $t$-pattern ($p \to p'$ at $x$, $k \to k'$ at $y$): two crossings, sign $+$. Bottom, the $u$-pattern ($p \to k'$, $k \to p'$): three crossings, sign $-$. Added figure.*

## The contraction rule

> [!theorem] Theorem §C6d.3.5: The Contraction Rule for T-Matrix Elements with Fermions
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] let $|i\rangle$, $\langle f|$ be free states written as in [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]] (the bra the adjoint of the ket), no outgoing momentum equal to an incoming one, and expand $\langle f|\,T\{\hat{\mathcal H}_I(x_1)\cdots\hat{\mathcal H}_I(x_n)\}\,|i\rangle$ by [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]]. Then
> 1. a nonzero term contracts every field that is not contracted with another field **one by one with the external particles**, and every particle with a field (as [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-2|Theorem §C6c.3.2]], parts 1–2: the frequency parts only decide which particle a field can meet, [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]);
> 2. if the fields are kept in the order of $\mathcal L_{\rm int}$, $\hat{\bar\psi}_a\hat\psi_a\hat\phi$ at every vertex (the vertices in any order), the term is the product of the contraction values taken in the written order ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]) times $(-1)^{\#\text{crossings}}$ of its contraction lines ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]): **no further sign** comes from splitting the fields into frequency parts, from the normal ordering, or from moving fields to contract them from the inside out;
> 3. since the packages $\hat{\bar\psi}\hat\psi\hat\phi(x_k)$ move freely ([[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]]), two terms can differ in sign only through the way their fermion fields are contracted, with the external fermions (the overall sign and the relative signs between diagrams, [[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]]) or around a closed loop ($-1$, [[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]]).
>
> In Yu's words: a nontrivial $T$-matrix element equals the result of contracting the field operators one by one with the initial- and final-state particles, and when the field operators keep the order of the interaction Lagrangian no extra minus sign appears. Yu's bra keeps the order of the labels ([[§C6d.4 First Order#^cau-c6d-4-1|§C6d.4, Caution: Yu's (7.23)–(7.24) and his order of the bra]]), so his lines cross where the vault's do not, and his overall signs differ.
>
> *Equivalently,* the scalar case is [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-2|Theorem §C6c.3.2]]: parts 1–2 are the same, and its part 3 ("for bosons no sign arises") becomes the crossing sign of part 2 here.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* free fields between free states, exact for each term, used inside the Dyson series with the scope of [[§C6c.2 Contractions with External Particles|§C6c.2]] (lowest order of a process exact).
>
> *Source: Yu §7.1, p. 268 (boxed: "非平庸的 $T$ 矩阵元等于将场算符与初末态粒子一一缩并之后的结果，而且，当场算符次序保持相互作用拉氏量中的次序时，不会出现额外的负号"; "这就是 $T$ 矩阵元的缩并规律"), eq. (7.30) and the paragraphs after it (pp. 267–268) · PHY 513 Lecture 17, slide 18 ("Sign of amplitude: determine from explicit contractions if it is needed"), and transcript ("The one place where you get a problem is contracting exactly this with these external states") · the user's PHY 513 notes, Lecture 17 update, §17.6 ("the only place where a sign must be tracked is the contraction with the external states") · from the "What the derivation shows" of [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^der-c6d-3-4|Derivation §C6d.3.4]]*

^thm-c6d-3-5

> [!derivation]- Derivation
> **Step 1** (part 1). Between the states, every field left in a normal-ordered product must meet a particle: its annihilation part must find a creation operator of $|i\rangle$ to its right, its creation part an annihilation operator of $\langle f|$ to its left, or it annihilates $|0\rangle$ / $\langle0|$ ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]]; for fermions the moves cost signs only, Step 1 of [[§C6d.2 Contractions with External Fermions#^der-c6d-2-2|Derivation §C6d.2.2]]). A particle that meets no field would pair with a particle of the other state, $\langle\mathbf p|\mathbf k\rangle \propto \delta^3(\mathbf p - \mathbf k) = 0$ by assumption. Which particle a field can meet is fixed by [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]: $\hat\psi$ an incoming fermion or an outgoing antifermion, $\hat{\bar\psi}$ an outgoing fermion or an incoming antifermion, $\hat\phi$ a scalar.
>
> **Step 2** (part 2). Fix a full contraction pattern. By [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]] its term is $(-1)^{\#\text{crossings}}\prod(\text{values in the written order})$, the string written $\langle0|A\,[\hat{\bar\psi}\hat\psi]_{x_1}\cdots[\hat{\bar\psi}\hat\psi]_{x_n}\,B|0\rangle$ with the packages in the order of $\mathcal L_{\rm int}$. The derivation of that theorem evaluates the vacuum value directly ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], 2); the frequency split and the normal ordering of Yu's (7.6) are intermediate steps of the same vacuum value and cannot change it. Contracting "from the inside out" ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-2|Theorem §C6d.2.2]]) is the special case of nested arcs, which do not cross.
>
> **Step 3** (Yu's example (7.30), in the vault's convention). $\langle\mathbf p, s; \mathbf q, s'; \mathbf k|\,{:}\hat{\bar\psi}_a\hat\psi_a\hat\phi{:}(x)\,|0\rangle$, bra $\sqrt{8E_{\mathbf p}E_{\mathbf q}E_{\mathbf k}}\,\langle0|\hat a_{\phi,\mathbf k}\hat b^{s'}_{\mathbf q}\hat a^s_{\mathbf p}$ ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]). Fermion string: $\hat b_{\mathbf q}(1)\,\hat a_{\mathbf p}(2)\,\hat{\bar\psi}_a(3)\,\hat\psi_a(4)$, pairs $(2, 3)$ (outgoing fermion, $\bar u^s_a(p)e^{ip\cdot x}$) and $(1, 4)$ (outgoing antifermion, $v^{s'}_a(q)e^{iq\cdot x}$): nested, no crossing. The term is $\bar u^s(p)v^{s'}(q)\,e^{i(p + q + k)\cdot x}$ with sign $+$. With Yu's bra $\langle0|\hat a_{\mathbf p}\hat b_{\mathbf q}\hat a_{\phi,\mathbf k}$ the pairs become $(1, 3)$ and $(2, 4)$, which cross once: his $(7.30)$ has the opposite sign, $+i\kappa\,\bar u(p)v(q)$ against the vault's $-ig\,\bar u(p)v(q)$.
>
> **Step 4** (part 3). Exchanging two packages costs no sign ([[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]], 1), so the written order of the vertices is free; an internal contraction inside a fully contracted closed line gives the sign of [[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]] whatever the order. What remains are the arcs to the fixed operators $A$, $B$ of the states.
>
> **What the derivation shows.**
> - Yu's rule is the crossing theorem read as a recipe: keep $\mathcal L_{\rm int}$'s order, draw the lines, untangle them, count.

^der-c6d-3-5

*Uses:* [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-2|Theorem §C6d.2.2]], [[§C6d.2 Contractions with External Fermions#^der-c6d-2-2|Derivation §C6d.2.2]], [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]], [[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]]

> [!remark] Remark: Where the fermion signs go
> When the time order is reversed, the contraction is still the time-ordered vacuum value, with no extra commutator terms. The reordering sign is built into the definition of $T$ and so into $S_F$ with its $i\varepsilon$. This seldom matters, because bilinears move as packages ([[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]]). Signs must be tracked by hand where packages are opened against fixed operators: the external states ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]), giving relative signs between diagrams ([[§C6d.5 Second Order#^thm-c6d-5-3|Theorem §C6d.5.3]]) and an overall sign; and closed loops ([[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]]). "All signs determined unambiguously by Wick's theorem" (slide 23).
>
> *Source: PHY 513 Lecture 17, slide 23, and transcript (about 56–58 min) · the user's PHY 513 notes, Lecture 17 update, §17.4, paragraph "Where the fermion signs go"*

^rem-c6d-3-1

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.8 Pairings, Diagrams and Symmetry Factors#^def-ca-8-1|Def. §CA.8.1]], [[§CA.8 Pairings, Diagrams and Symmetry Factors#^thm-ca-8-1|Theorem §CA.8.1]] — a full contraction is a pairing (CA); the sign of a pairing as the parity of its crossings is [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], proved in this section.

> [!remark]- Connections
> - The fermionic theorem is the bosonic one with signs; for fields that are all scalars it reduces to it, and Yu proves both at once with a sign $\epsilon_{ab}$ per exchange — [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]], [[§C6a.6 Wick's Theorem#^rem-c6a-6-3|§C6a.6, Remark: Yu's route]].
> - The antisymmetry of the four-point function under $\hat\psi_1 \leftrightarrow \hat\psi_3$ is the Pauli principle of the many-fermion states, here in the correlation functions — [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]]; the same sign makes fermionic time ordering Lorentz invariant — [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-2|Theorem §C5b.8.2]].
> - In the path integral the fermion fields are Grassmann numbers and every sign of this section is automatic; the closed-loop $-1$ is why integrating out a fermion gives a determinant to a positive power, where a boson gives an inverse power — QFT C11 (planned), [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]] (★ Grassmann boxes).
> - The trace of a closed loop is evaluated with the trace theorems of the $\gamma$ matrices — [[§C5a.14 Gamma-Matrix Technology|§C5a.14]].
> - Yu's contraction rule is the scalar rule plus the crossing sign; with the vault's bras, contractions from the inside out cost nothing — [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-5|Theorem §C6d.3.5]], [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-2|Theorem §C6c.3.2]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-2|Theorem §C6d.2.2]].
