---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6c
section: C6c.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6c.2 Contractions with External Particles]] · ↑ [[· C6c Feynman Rules for Amplitudes]] · [[§C6c.4 First Order꞉ Enumerate, then Filter]] →

*Sources: Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.6, pp. 109–111, eqs. (4.91), (4.94)–(4.96) · PHY 513 Lecture 16 (Larsen, 2 Nov 2026), Part B, slides 10–14, and transcript · the user's PHY 513 notes, Lecture 16 update, §16.3 · Yu Zhao-Huan, 量子场论讲义, §7.1, p. 268 (boxed contraction rule); §7.1.2, p. 283 and Fig. 7.7 (disconnected terms) · PHY 513, Problem Set 8, Problem 3(d)–(e) (the user's solution, submitted 2026-10-30).*

[[§C6c.2 Contractions with External Particles|§C6c.2]] contracted a field with one external particle and $n$ identical fields with $n$ identical particles. This section puts these contractions into Wick's theorem: an $S$-matrix element between particle states is the sum over the full contractions of fields **and** particles ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]]), which is Yu's contraction rule: every remaining field meets a particle, every particle meets a field, and for bosons no sign arises ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-2|Theorem §C6c.3.2]]). A particle that reaches no vertex gives the $\delta$-line ([[§C6c.3 Wick's Theorem between Particle States#^def-c6c-3-1|Def. §C6c.3.1]]), and every connected piece of a term carries its own momentum delta ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]]), the fact on which the sorting of the terms at first and second order rests ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]]). Yu: §7.1, p. 268; PS §4.6, p. 110; Lecture 16, Part B. The fermionic version, with signs: [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule|§C6d.3]].

**Setup and scope.** As in [[§C6c.2 Contractions with External Particles|§C6c.2]]: free fields in the interaction picture between free, relativistically normalized Fock states over $|0\rangle$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]). [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]], [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-2|Theorem §C6c.3.2]] and [[§C6c.3 Wick's Theorem between Particle States#^def-c6c-3-1|Def. §C6c.3.1]] are statements about free fields and free states: exact, whatever the dynamics. [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]] concerns the terms of the Dyson series between such states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]): exact in [[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]], lowest order in [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]].

## Wick's theorem between particle states

> [!theorem] Theorem §C6c.3.1: Wick's Theorem between Particle States
> Let $|\mathbf k_1\cdots\mathbf k_n\rangle$ and $\langle\mathbf p_1\cdots\mathbf p_m|$ be relativistically normalized free states of one real field. Then
>
> $$
> \langle\mathbf p_1\cdots\mathbf p_m|\,T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_\ell)\}\,|\mathbf k_1\cdots\mathbf k_n\rangle = \sum_{\text{full contractions}}\;\prod_{\text{pairs}}(\text{value}) ,
> $$
>
> the sum over all ways of splitting the $\ell$ fields and the $n + m$ particles into pairs of the four types
>
> $$
> \overbracket{\hat\phi_I(x_a)\hat\phi_I(x_b)} = D_F(x_a - x_b), \quad \overbracket{\hat\phi_I(x)|\mathbf k\rangle} = e^{-ik\cdot x}, \quad \overbracket{\langle\mathbf p|\hat\phi_I(x)} = e^{+ip\cdot x}, \quad \overbracket{\langle\mathbf p|\mathbf k\rangle} = 2E_{\mathbf k}(2\pi)^3\delta^3(\mathbf p - \mathbf k) ,
> $$
>
> with no pair of two incoming or two outgoing particles. Equivalently: in Wick's theorem $T\{\cdots\} = \sum_C\prod D_F\;{:}\text{rest}{:}$ ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]), a normal-ordered remainder contributes only through the terms in which **every** one of its fields is contracted with an external particle ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-2|Theorem §C6c.3.2]]). Several fields and complex fields: the same, with the contractions of [[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]] and [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 3.
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free fields between free states, exact, independent of the dynamics; used with the Dyson series as in the opening.
>
> *Source: PS §4.6, p. 110 ("To evaluate an $S$-matrix element such as (4.92), we simply write down all possible full contractions of the $\phi_I$ operators *and* the external-state momenta"), p. 111 · Yu §7.1, p. 268 (boxed: "a nontrivial $T$-matrix element equals the result of contracting the field operators one by one with the initial- and final-state particles") · PHY 513, Problem Set 8, Problem 3(d)–(e) (the user's "only the Wick terms with exactly $n$ uncontracted fields survive") · proof written here*

^thm-c6c-3-1

> [!derivation]- Derivation
> **Step 1** (Wick). By [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]], an operator identity,
>
> $$
> \langle f|T\{\hat\phi_1\cdots\hat\phi_\ell\}|i\rangle = \sum_C\;\prod_{\{a,b\}\in C}D_F(x_a - x_b)\;\langle f|{:}\textstyle\prod_{c\in R_C}\hat\phi_c{:}|i\rangle , \qquad R_C = \{1, \dots, \ell\}\setminus\cup C .
> $$
>
> **Step 2** (split the remainder). By [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 1,
>
> $$
> {:}\prod_{c\in R}\hat\phi_c{:} = \sum_{A\subseteq R}\;\prod_{a\in A}\hat\phi_a^-\prod_{b\in R\setminus A}\hat\phi_b^+ .
> $$
>
> **Step 3** (the $\hat\phi^+$ on the incoming particles). By [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 1–2, applied once per field (relativistic states, each removal $e^{-ik\cdot x}$),
>
> $$
> \prod_{b\in R\setminus A}\hat\phi_b^+\,|\mathbf k_1\cdots\mathbf k_n\rangle = \sum_{\beta}\;\prod_{b\in R\setminus A}e^{-ik_{\beta(b)}\cdot x_b}\;\bigl|\{\mathbf k_i\}_{i\notin\beta(R\setminus A)}\bigr\rangle ,
> $$
>
> the sum over injective maps $\beta$ from $R\setminus A$ to the incoming particles; no such map if $|R\setminus A| > n$ (a $\hat\phi^+$ meets $|0\rangle$).
>
> **Step 4** (the $\hat\phi^-$ on the outgoing particles). Taking adjoints in Step 3 ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]]),
>
> $$
> \langle\mathbf p_1\cdots\mathbf p_m|\prod_{a\in A}\hat\phi_a^- = \sum_{\alpha}\;\prod_{a\in A}e^{+ip_{\alpha(a)}\cdot x_a}\;\bigl\langle\{\mathbf p_j\}_{j\notin\alpha(A)}\bigr| ,
> $$
>
> $\alpha$ injective from $A$ to the outgoing particles.
>
> **Step 5** (the particles left over). The remaining overlap is ([[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-5|Theorem §C6c.7.5]], relativistic form)
>
> $$
> \langle\mathbf p_{j_1}\cdots\mathbf p_{j_s}|\mathbf k_{i_1}\cdots\mathbf k_{i_{s'}}\rangle = \delta_{ss'}\sum_{\pi\in S_s}\prod_{u=1}^s2E_{\mathbf k_{i_u}}(2\pi)^3\delta^3(\mathbf p_{j_{\pi(u)}} - \mathbf k_{i_u}) ,
> $$
>
> a sum over bijections, each pair $\overbracket{\langle\mathbf p|\mathbf k\rangle}$.
>
> **Step 6** (assemble). A term of Steps 1–5 is a choice $(C, A, \beta, \alpha, \pi)$, and it is the product of the values of the pairs: $C$ (field–field), $\{b, \beta(b)\}$ (field–incoming), $\{\alpha(a), a\}$ (outgoing–field), $\pi$ (outgoing–incoming). Conversely a full contraction determines $C$, $A$ (the fields paired with outgoing particles), $\beta$, $\alpha$, $\pi$ uniquely. So the sum is over full contractions, each once; a remainder field not paired with a particle gives no term (Steps 3–4).
>
> **Step 7** (the case $\ell = 2$, $n = m = 1$). Steps 1–2: $T\{\hat\phi_1\hat\phi_2\} = D_F(x_1 - x_2) + \hat\phi_1^+\hat\phi_2^+ + \hat\phi_2^-\hat\phi_1^+ + \hat\phi_1^-\hat\phi_2^+ + \hat\phi_1^-\hat\phi_2^-$. Between $\langle\mathbf p|$ and $|\mathbf k\rangle$: $\hat\phi^+\hat\phi^+|\mathbf k\rangle = 0$ (one particle, two removals) and $\langle\mathbf p|\hat\phi^-\hat\phi^- = 0$, so
>
> $$
> \langle\mathbf p|T\{\hat\phi_1\hat\phi_2\}|\mathbf k\rangle = \overbracket{\hat\phi_1\hat\phi_2}\,\overbracket{\langle\mathbf p|\mathbf k\rangle} + \overbracket{\langle\mathbf p|\hat\phi_2}\,\overbracket{\hat\phi_1|\mathbf k\rangle} + \overbracket{\langle\mathbf p|\hat\phi_1}\,\overbracket{\hat\phi_2|\mathbf k\rangle} = D_F(x_1 - x_2)\,2E_{\mathbf k}(2\pi)^3\delta^3(\mathbf p - \mathbf k) + e^{ip\cdot x_2}e^{-ik\cdot x_1} + e^{ip\cdot x_1}e^{-ik\cdot x_2} ,
> $$
>
> the three full contractions.
>
> **What the derivation shows.**
> - The vacuum version ([[§C6a.6 Wick's Theorem#^thm-c6a-6-3|Theorem §C6a.6.3]]) is the case $n = m = 0$: then only $R = \varnothing$ survives.
> - The outgoing–incoming pairs are the particles that pass through untouched; with all outgoing momenta different from the incoming ones they vanish, and every particle must attach to a field → [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-2|Theorem §C6c.3.2]].

^der-c6c-3-1

*Uses:* [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]], [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-5|Theorem §C6c.7.5]]

> [!theorem] Theorem §C6c.3.2: The Contraction Rule for S-Matrix Elements
> Expand $\langle\mathbf p_1\cdots\mathbf p_m|\,T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_\ell)\}\,|\mathbf k_1\cdots\mathbf k_n\rangle$ by Wick's theorem, $T\{\cdots\} = \sum_C\prod D_F\;{:}\text{rest}{:}$ ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]). Then
> 1. a normal-ordered remainder contributes only through the terms in which **every** one of its fields is contracted with an external particle ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]]); a remainder of $r$ fields needs $r \le n + m$;
> 2. if no outgoing momentum equals an incoming one, **every particle** is contracted with a field: a nonzero term contracts the fields one by one with the particles and the remaining fields with each other;
> 3. for bosons no sign arises: the order in which the fields and the particles stand does not matter.
>
> For fermions part 3 fails: each contraction pattern carries a sign ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|§C6d.3, Theorem §C6d.3.4]]).
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free fields between free relativistically normalized states, exact, independent of the dynamics; used with the Dyson series as in [[§C6c.2 Contractions with External Particles|§C6c.2]].
>
> *Source: Yu §7.1, p. 268 (boxed: "a nontrivial $T$-matrix element equals the result of contracting the field operators one by one with the initial- and final-state particles"; no extra sign when the fields keep the order of $\mathcal L_{\rm int}$ — the fermion half is §C6d.3) · PS §4.6, p. 110 ("all possible full contractions of the $\phi_I$ operators *and* the external-state momenta") · PHY 513, Problem Set 8, Problem 3(d)–(e) (the user's "only the Wick terms with exactly $n$ uncontracted fields survive") · from the "Equivalently" sentence of [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]] and the "What the derivation shows" of [[§C6c.3 Wick's Theorem between Particle States#^der-c6c-3-1|Derivation §C6c.3.1]] (promoted 2026-11-05)*

^thm-c6c-3-2

> [!derivation]- Derivation
> **Step 1** (part 1). Steps 2–4 of [[§C6c.3 Wick's Theorem between Particle States#^der-c6c-3-1|Derivation §C6c.3.1]]: the remainder is $\sum_A\prod_{a\in A}\hat\phi_a^-\prod_{b\in R\setminus A}\hat\phi_b^+$. A $\hat\phi_b^+$ acting on $|\mathbf k_1\cdots\mathbf k_n\rangle$ removes an incoming particle ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 1); one that finds no particle left reaches $|0\rangle$ and gives $\hat\phi_b^+|0\rangle = 0$. Likewise $\langle\mathbf p_1\cdots\mathbf p_m|\hat\phi_a^-$ removes an outgoing particle, and $\langle0|\hat\phi_a^- = 0$. So every remainder field is paired with a particle, $|R\setminus A| \le n$, $|A| \le m$, and $r = |R| \le n + m$.
>
> **Step 2** (part 2). Step 5 of [[§C6c.3 Wick's Theorem between Particle States#^der-c6c-3-1|Derivation §C6c.3.1]]: the particles not removed by fields pair among themselves as $\overbracket{\langle\mathbf p|\mathbf k\rangle} = 2E_{\mathbf k}(2\pi)^3\delta^3(\mathbf p - \mathbf k)$, which is $0$ for $\mathbf p \ne \mathbf k$. With all outgoing momenta different from the incoming ones such a term vanishes, so in a nonzero term no particle is left over.
>
> **Step 3** (part 3). Every manipulation of Steps 3–5 of [[§C6c.2 Contractions with External Particles#^der-c6c-2-1|Derivation §C6c.2.1]] moves an $\hat a$ through a $\hat\phi^-$ with $\hat aB = B\hat a + [\hat a, B]$: the coefficient of the moved term is $+1$, and the commutator is the c-number $\frac{e^{ik\cdot y}}{\sqrt{2E_{\mathbf k}}}$. The factors that are reordered commute, $[\hat\phi_I^\pm(x), \hat\phi_I^\pm(y)] = 0$, $[\hat a_{\mathbf k}, \hat a_{\mathbf p}] = [\hat a^\dagger_{\mathbf k}, \hat a^\dagger_{\mathbf p}] = 0$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]), and so do the c-number contractions. Hence no step produces a sign, whatever order the fields and particles are written in. For fermions the same moves use anticommutators, $\hat bB = -B\hat b + \{\hat b, B\}$, and each exchange gives $-1$.
>
> **What the derivation shows.**
> - Yu's boxed rule, split into what must be contracted (parts 1–2) and the sign (part 3); how many contractions there are is [[§C6c.2 Contractions with External Particles#^thm-c6c-2-3|Theorem §C6c.2.3]] and Step 3 of [[§C6c.4 First Order꞉ Enumerate, then Filter#^der-c6c-4-1|Derivation §C6c.4.1]].

^der-c6c-3-2

*Uses:* [[§C6c.3 Wick's Theorem between Particle States#^der-c6c-3-1|Derivation §C6c.3.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C6c.2 Contractions with External Particles#^der-c6c-2-1|Derivation §C6c.2.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]

## Which terms are scattering

> [!definition] Definition §C6c.3.1: The δ-Line
> A particle that passes from the initial to the final state without reaching any vertex contributes the overlap of [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]],
>
> $$
> \overbracket{\langle\mathbf p'|\mathbf p\rangle} = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf p') ,
> $$
>
> drawn as a line from the incoming to the outgoing particle, the **$\delta$-line** (dashed in these notes). With $A$, $B$ written on the left and $1$, $2$ on the right, the zeroth-order $2 \to 2$ element is two pictures, $A$–$1$, $B$–$2$ and $A$–$2$, $B$–$1$:
>
> $$
> {}_0\langle\mathbf p_1\mathbf p_2|\mathbf p_A\mathbf p_B\rangle_0 = 2E_A2E_B(2\pi)^6\bigl[\delta^3(\mathbf p_A - \mathbf p_1)\delta^3(\mathbf p_B - \mathbf p_2) + \delta^3(\mathbf p_A - \mathbf p_2)\delta^3(\mathbf p_B - \mathbf p_1)\bigr] .
> $$
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free relativistic states, exact; it appears only in the diagrams of $S$-matrix elements before the terms of the $\mathbb 1$ are dropped ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]]): the rules for $i\mathcal M$ have no $\delta$-lines.
>
> *Source: PHY 513 Lecture 16 (Larsen, 2 Nov 2026), slides 10–11 ("Encode essential combinatorial data in diagrams … Caution: line = $\delta$"), and transcript ("this kind of Feynman rules, where a single line is a delta function, will appear only today") · the user's PHY 513 notes, Lecture 16 update, §16.3, Definition "The $\delta$-line (this lecture only)" and eq. (orderzero) · PS §4.6, p. 109, eq. (4.91), and the diagrams on p. 110*

^def-c6c-3-1

> [!caution] Caution: A line is a δ, not a D_F
> The same drawn line means two things in Lecture 16. In the diagrams of ${}_0\langle f|T\{\cdots\}|i\rangle_0$ two kinds of line look alike. A line from an incoming particle straight to an outgoing one, touching no vertex, is the overlap $\overbracket{\langle\mathbf p|\mathbf k\rangle} = 2E_{\mathbf k}(2\pi)^3\delta^3(\mathbf p - \mathbf k)$; a line between two vertices, or a loop, is $D_F$. The slides: "Caution: line = $\delta$ (not standard rule where line = $D_F$)" (slide 10); "line = $D_F$ in figure 8 but line = $\delta$ inside round brackets" (slide 14); "direct line is a $\delta$-function" (slide 16). In the diagrams of correlation functions every line is a $D_F$ ([[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-4|Theorem §C6a.8.4]]); an external line of an amplitude diagram is neither: a plane wave $e^{\mp ip\cdot x}$ in position space ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2) and $1$ in momentum space. Figure ph-qft-c6b-2-5 and the user's notes draw the $\delta$-lines ([[§C6c.3 Wick's Theorem between Particle States#^def-c6c-3-1|Def. §C6c.3.1]]) dashed and keep solid lines for propagators and wave functions. Diagram rules in which a single line is a delta function appear only in Lecture 16.
>
> *Source: PHY 513 Lecture 16, slides 10, 14, 16, and transcript · the user's PHY 513 notes, Lecture 16 update, §16.3, Caution "The same line means two different things in the lecture" · PS §4.6, eqs. (4.91), (4.96)*

^cau-c6c-3-1

> [!theorem] Theorem §C6c.3.3: Every Connected Piece Carries Its Own Momentum Delta
> Let $|i\rangle = |\mathbf k_1\cdots\mathbf k_n\rangle$, $\langle f| = \langle\mathbf p_1\cdots\mathbf p_m|$ be relativistically normalized free states, and expand ${}_0\langle f|T\{\exp[-i\int_{-T}^{T}dt\,\hat H_I]\}|i\rangle_0$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]], 2) by [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]]: each term is a diagram whose external points are the particles. Split it into its connected pieces. Then each piece with particles carries its own momentum delta: a lone pair $\overbracket{\langle\mathbf p|\mathbf k\rangle} = 2E_{\mathbf k}(2\pi)^3\delta^3(\mathbf p - \mathbf k)$ (a particle attached to no vertex: the $\delta$-line of [[§C6c.3 Wick's Theorem between Particle States#^def-c6c-3-1|Def. §C6c.3.1]]; [[§C6c.3 Wick's Theorem between Particle States#^cau-c6c-3-1|Caution: A line is a δ, not a D_F]]), a piece with vertices $(2\pi)^4\delta^4(\sum k - \sum p)$ over its own particles.
>
> A term with several pieces with particles therefore carries one delta per piece, in independent combinations of the momenta. The same holds for correlation functions in momentum space: [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-2|Theorem §C6c.1.2]] shows it for the free four-point function, two deltas for two components.
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* any polynomial interaction, every order, with the prescription of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]] (and its scope).
>
> *Source: PHY 513 Lecture 16, slides 11, 14 (each $\delta$-line and each vertex piece is a factor of its own) · PS §4.6, eq. (4.96) · Yu §7.1.2, p. 283 and Fig. 7.7 (disconnected terms do not contribute to the $T$-matrix element) · proof written here (Steps 1–2 of the proof of the former single theorem "Which terms of the $S$-matrix element belong to $i\hat T$", split 2026-11-05)*

^thm-c6c-3-3

> [!derivation]- Derivation
> **Step 1** (pieces factor). A term of [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]] is a product of pair values times the vertex integrals $\int\prod_vd^4z_v$. A pair joins two nodes of the same piece, so the integrand is a product over pieces, each depending only on the $z_v$ of its own vertices, and the integral factorizes (each $z_v$ belongs to one piece):
>
> $$
> \text{term} = \prod_{\text{pieces }P}\Bigl(\int\prod_{v\in P}d^4z_v\;\prod_{\text{pairs in }P}(\text{value})\Bigr) .
> $$
>
> **Step 2** (one delta per piece). A lone pair is $\overbracket{\langle\mathbf p|\mathbf k\rangle} = 2E_{\mathbf k}(2\pi)^3\delta^3(\mathbf p - \mathbf k)$ (Theorem §C6c.3.1). For a piece with vertices, insert the Fourier form of each internal line; the particles enter through $e^{-ik\cdot z}$, $e^{+ip\cdot z}$ ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2); each vertex integral gives $(2\pi)^4\delta^4$ of the momenta at that vertex ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-5|Theorem §C6a.12.5]], 1). Doing the internal momentum integrals along a spanning tree of the piece (Step 3 of [[§C6a.12 Feynman Rules for Polynomial Interactions#^der-c6a-12-3|Derivation §C6a.12.3]]) uses all deltas but one, which is $(2\pi)^4\delta^4(\sum_{\rm in}k - \sum_{\rm out}p)$ over the particles of the piece.
>
> **What the derivation shows.**
> - The delta of a piece comes from the external plane waves of that piece alone; particles in different pieces exchange no momentum. Which such terms are not scattering: [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]]; the single piece that remains: [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]].

^der-c6c-3-3

*Uses:* [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-5|Theorem §C6a.12.5]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^der-c6a-12-3|Derivation §C6a.12.3]]

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] — the vertex integrals give momentum deltas.

> [!remark]- Connections
> - With fermions the same theorem holds with a sign for each crossing of contractions — [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|§C6d.3, Theorem §C6d.3.4]].
> - The terms with $\delta$-lines and several pieces are not scattering; the sorting at first order is [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], at second order [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]].
> - The same expansion with a source vertex is exact and solves the classical-source problem — [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route|§C6c.7]].
> - The contraction rule with fermions keeps the fields in the order of $\mathcal L_{\rm int}$ and puts every sign into the crossings — [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-5|Theorem §C6d.3.5]].
