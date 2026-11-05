---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6c
section: C6c.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6c.3 Wick's Theorem between Particle States]] · ↑ [[· C6c Feynman Rules for Amplitudes]] · [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors]] →

<!-- SOURCES -->

<!-- OPENING -->

<!-- SETUP -->

## First order: enumerate, then filter

> [!theorem] Theorem §C6c.4.1: The First-Order Matrix Elements of a Monomial
> Let $\mathcal L_{\rm int} = -g\,M$, $M = \prod_k\phi_k^{m_k}$ a monomial in real fields without derivatives ([[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]]). Let $|i\rangle$ and $\langle f|$ hold $n_k$ particles of kind $k$ in total, with no outgoing momentum equal to an incoming one. Then
>
> $$
> \langle f|i\hat T^{(1)}|i\rangle = -ig\int d^4x\,\langle f|M\bigl(\hat\phi_I(x)\bigr)|i\rangle = -ig\prod_k\frac{m_k!}{2^{\ell_k}\,\ell_k!}\,D_F^{(m_k)}(0)^{\ell_k}\;(2\pi)^4\delta^4\Bigl(\sum_ik_i - \sum_jp_j\Bigr), \qquad \ell_k = \frac{m_k - n_k}{2} ,
> $$
>
> nonzero only if every $m_k - n_k$ is even and $\ge 0$: each leg takes one external particle or is closed with another leg of its kind into a loop. In particular, for a tree ($\ell_k = 0$, every leg on a particle), $i\mathcal M = -ig\prod_km_k!$, the vertex factor ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]).
>
> **Procedure** (Yu's enumerate-then-filter): (1) list every split of the legs of $M$ into incoming particles, outgoing particles and pairs closed into loops, each giving a matrix element above; (2) keep those that four-momentum conservation allows on the mass shell ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]]).
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* first order, free relativistic states over $|0\rangle$ in place of the in and out states (as in the opening: lowest order; a loop $D_F(0)$ on a single particle is a mass shift, [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]); complex fields: the legs $\phi$, $\phi^\dagger$ take particles and antiparticles by [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 3.
>
> *Source: Yu §7.1.1, pp. 264–272 (all first-order $T$-matrix elements of Yukawa theory, eqs. (7.21)–(7.43), Fig. 7.1–7.2; "the 10 Feynman diagrams correspond to 10 dynamically allowed processes; most are kinematically forbidden", p. 272); §7.3, eqs. (7.115)–(7.121) · PS §4.6, eqs. (4.92)–(4.98) · proof written here*

^thm-c6c-4-1

> [!derivation]- Derivation
> **Step 1** (first order). $\hat S = \mathbb 1 + i\hat T$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]]) and the $n = 1$ term of the Dyson series ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]]) with $\hat{\mathcal H}_I = gM(\hat\phi_I)$: $i\hat T^{(1)} = -i\int dt\,\hat H_I(t) = -ig\int d^4x\,M(\hat\phi_I(x))$; one time, so $T\{\cdot\}$ acts trivially.
>
> **Step 2** (Wick between the states). Label the $m_k$ factors of kind $k$ as legs. By [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]] (all fields at $x$; [[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]] for several kinds), $\langle f|M|i\rangle$ is the sum over full contractions of legs and particles. Outgoing–incoming pairs give $\delta^3(\mathbf p - \mathbf k) = 0$ (distinct momenta); leg–leg pairs give $D_F^{(m_k)}(x - x) = D_F^{(m_k)}(0)$ (formal, [[§C6a.5 Normal Ordering and Contractions#^cau-c6a-5-3|§C6a.5, Caution: In what sense these identities hold]]); a particle pairs only with a leg of its kind.
>
> **Step 3** (count, per kind). The $n_k$ distinct particles of kind $k$ go injectively to the $m_k$ legs, $m_k(m_k - 1)\cdots(m_k - n_k + 1) = \frac{m_k!}{(2\ell_k)!}$ ways; the remaining $2\ell_k$ legs pair in $(2\ell_k - 1)!! = \frac{(2\ell_k)!}{2^{\ell_k}\ell_k!}$ ways ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]); the product is $\frac{m_k!}{2^{\ell_k}\ell_k!}$. If $m_k - n_k$ is odd or negative, no full contraction exists. Kinds are independent.
>
> **Step 4** (the vertex integral). Every term carries $\prod_ie^{-ik_i\cdot x}\prod_je^{+ip_j\cdot x}$ ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2), and with [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]
>
> $$
> \int d^4x\,e^{i(\sum_jp_j - \sum_ik_i)\cdot x} = (2\pi)^4\delta^4\Bigl(\sum_ik_i - \sum_jp_j\Bigr) .
> $$
>
> **Step 5** (tree). $\ell_k = 0$ for all $k$: $\langle f|i\hat T^{(1)}|i\rangle = -ig\prod_km_k!\,(2\pi)^4\delta^4(\cdots)$, and [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]] gives $i\mathcal M = -ig\prod_km_k!$. Checks ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]]): $\phi^4$, $m = 4$, $n = 4$: $\frac{\lambda}{4!}\cdot24$; $n = 2$: $\frac{4!}{2} = 12$ (the tadpole, $\frac{12}{24} = \frac12$); $n = 0$: $\frac{4!}{4\cdot2} = 3$ (the figure-eight, $\frac{3}{24} = \frac18$), the counts of [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-1|Example §C6a.9.1]].
>
> **What the derivation shows.**
> - At first order the operator content of $\mathcal L_{\rm int}$ alone decides which processes have a matrix element; kinematics decides which of them happen.

^der-c6c-4-1

*Uses:* [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]], [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-3|P6, step 3]]

> [!theorem] Theorem §C6c.4.2: The Kinematic Filter
> Let all external particles be on shell, $p^0 = E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2} > 0$. Then $\delta^4\bigl(\sum_{\rm in}p - \sum_{\rm out}p\bigr)$ restricted to the mass shells
> 1. vanishes if one side has no particles and the other has at least one ($0 \to n$, $n \to 0$);
> 2. vanishes for one incoming particle of mass $M > 0$ and outgoing masses $m_1, \dots, m_n$, $n \ge 2$, if $M < \sum_im_i$; for $M = \sum_im_i$ it is supported on the set where every product is at rest in the frame of the decaying particle, of measure zero in the final momenta;
> 3. vanishes for $n \ge 2$ incoming particles of masses $m_i$ and one outgoing of mass $M > 0$ if $M < \sum_im_i$ (part 2 reversed);
> 4. for one incoming and one outgoing particle, requires $p_{\rm out} = p_{\rm in}$: forward, with equal masses.
>
> For equal masses $m > 0$ every $1 \to n$ and $n \to 1$ with $n \ge 2$ is forbidden.
>
> *Model:* any (kinematics); *applies:* on-shell external momenta, any theory; it filters the matrix elements of [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]] at every order.
>
> *Source: Yu §7.1.1, p. 272 ("most of these processes are kinematically not allowed, because the initial and final states cannot satisfy energy-momentum conservation at the same time … when $m_\phi > 2m_\psi$, two processes are exceptions"); §6.5.4, threshold (6.378) · PHY 513, Problem Set 8, Problem 4 ("provided that $M > 2m$") · proof written here*

^thm-c6c-4-2

> [!derivation]- Derivation
> **Step 1** (part 1). Each $p^0 = E_{\mathbf p} > 0$, so a nonempty side has $\sum p^0 > 0$ and the empty side $0$: $\sum_{\rm in}p^0 - \sum_{\rm out}p^0 \ne 0$ on the whole mass shell, and the delta vanishes there ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]]).
>
> **Step 2** (frame). The support condition $\Delta \equiv \sum_{\rm in}p - \sum_{\rm out}p = 0$ is Lorentz covariant, $\Lambda\Delta = 0 \Leftrightarrow \Delta = 0$, and $\delta^4(\Lambda\Delta) = \delta^4(\Delta)$ (Step 3 of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^der-c6b-1-6|Derivation §C6b.1.6]]): it may be checked in any frame.
>
> **Step 3** (part 2). In the rest frame of the incoming particle, $p_{\rm in} = (M, \mathbf 0)$. Conservation requires
>
> $$
> M = \sum_{i=1}^nE_{\mathbf p_i} = \sum_{i=1}^n\sqrt{\mathbf p_i^2 + m_i^2} \ \ge\ \sum_{i=1}^nm_i , \qquad \sum_i\mathbf p_i = \mathbf 0 ,
> $$
>
> with equality iff every $\mathbf p_i = \mathbf 0$. So for $M < \sum m_i$ no momenta satisfy it, and for $M = \sum m_i$ only $\mathbf p_1 = \cdots = \mathbf p_n = \mathbf 0$, one point.
>
> **Step 4** (part 3). The same in the rest frame of the outgoing particle, $p_{\rm out} = (M, \mathbf 0)$, with the roles of in and out exchanged.
>
> **Step 5** (part 4). $p_{\rm in} = p_{\rm out}$ as four-vectors; then $m_{\rm in}^2 = p_{\rm in}^2 = p_{\rm out}^2 = m_{\rm out}^2$ and $\mathbf p_{\rm out} = \mathbf p_{\rm in}$.
>
> **Step 6** (equal masses). $M = m < nm$ for $n \ge 2$: parts 2–3.
>
> **What the derivation shows.**
> - A decay needs $M > \sum m_i$ (for two bodies, $M > 2m$); a one-vertex fusion $n \to 1$ is the reverse, possible only at the special incoming momenta with $(\sum p_i)^2 = M^2$.

^der-c6c-4-2

*Uses:* [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^der-c6b-1-6|Derivation §C6b.1.6]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-3|P6, step 3]]

<!-- NEW thm-c6c-4-3 -->

> [!example] Example §C6c.4.1: φφ → φφ at First Order, by Contractions with the External States
> ![[ph-qft-c6b-2-1.svg]]
>
> In $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]), for $\mathbf p_1, \mathbf p_2 \notin \{\mathbf p_A, \mathbf p_B\}$,
>
> $$
> \langle\mathbf p_1\mathbf p_2|i\hat T^{(1)}|\mathbf p_A\mathbf p_B\rangle = -i\lambda\,(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2), \qquad i\mathcal M = -i\lambda ;
> $$
>
> the $4!$ ways of attaching the four particles to the four fields cancel the $\frac{1}{4!}$. The other first-order processes are $1 \leftrightarrow 3$, $0 \leftrightarrow 4$ (forbidden), $0 \leftrightarrow 2$ with a loop (forbidden), $1 \to 1$ with a loop (forward only: a mass shift), and the vacuum bubble.
>
> **Step 1** (first order). [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]], Step 1, with the four factors of $\hat\phi_I(x)^4$ labelled $\hat\phi_1, \dots, \hat\phi_4$ (all at $x$):
>
> $$
> \langle\mathbf p_1\mathbf p_2|i\hat T^{(1)}|\mathbf p_A\mathbf p_B\rangle = -\frac{i\lambda}{4!}\int d^4x\,\langle\mathbf p_1\mathbf p_2|T\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\}|\mathbf p_A\mathbf p_B\rangle .
> $$
>
> **Step 2** (Wick: time order → normal order plus contractions). By [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]], with $\overbracket{\hat\phi_a\hat\phi_b} = D_F(0)$,
>
> $$
> T\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\} = {:}\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4{:} + \bigl(\overbracket{\hat\phi_1\hat\phi_2}\,{:}\hat\phi_3\hat\phi_4{:} + \cdots\bigr)_{6\text{ terms}} + \bigl(\overbracket{\hat\phi_1\hat\phi_2}\,\overbracket{\hat\phi_3\hat\phi_4} + \overbracket{\hat\phi_1\hat\phi_3}\,\overbracket{\hat\phi_2\hat\phi_4} + \overbracket{\hat\phi_1\hat\phi_4}\,\overbracket{\hat\phi_2\hat\phi_3}\bigr)
> $$
>
> (PS (4.95)).
>
> **Step 3** (between the states). By [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]], all four particles must be paired, and outgoing–incoming pairs vanish ($\mathbf p_1, \mathbf p_2 \notin \{\mathbf p_A, \mathbf p_B\}$):
> - the last three terms: $3D_F(0)^2\langle\mathbf p_1\mathbf p_2|\mathbf p_A\mathbf p_B\rangle = 0$ (a bubble times the "1", PS (4.96));
> - $D_F(0)\langle\mathbf p_1\mathbf p_2|{:}\hat\phi_a\hat\phi_b{:}|\mathbf p_A\mathbf p_B\rangle$: two fields take two particles, the other two would pair with each other: $0$ (PS's four diagrams on p. 111, particles passing by) — the classes of [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]] and [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]]: the bubble with $\delta$-lines (Theorem §C6c.4.6, parts 1–2), the forward pieces (part 2), the vertex (Theorem §C6c.5.3, part 2);
> - ${:}\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4{:}$: every field takes one particle. With $\sigma \in S_4$ giving the fields of $\mathbf p_1, \mathbf p_2, \mathbf p_A, \mathbf p_B$,
>
> $$
> \langle\mathbf p_1\mathbf p_2|{:}\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4{:}|\mathbf p_A\mathbf p_B\rangle = \sum_{\sigma\in S_4}\overbracket{\langle\mathbf p_1|\hat\phi_{\sigma(1)}}\,\overbracket{\langle\mathbf p_2|\hat\phi_{\sigma(2)}}\,\overbracket{\hat\phi_{\sigma(3)}|\mathbf p_A\rangle}\,\overbracket{\hat\phi_{\sigma(4)}|\mathbf p_B\rangle} = \sum_{\sigma\in S_4}e^{ip_1\cdot x}e^{ip_2\cdot x}e^{-ip_A\cdot x}e^{-ip_B\cdot x} ,
> $$
>
> the $24$ assignments $(\sigma(1)\sigma(2)\sigma(3)\sigma(4))$:
>
> $$
> \begin{aligned}
> &1234,\ 1243,\ 1324,\ 1342,\ 1423,\ 1432, && 2134,\ 2143,\ 2314,\ 2341,\ 2413,\ 2431,\\
> &3124,\ 3142,\ 3214,\ 3241,\ 3412,\ 3421, && 4123,\ 4132,\ 4213,\ 4231,\ 4312,\ 4321 ,
> \end{aligned}
> $$
>
> each the same plane wave, since all four fields sit at $x$.
>
> **Step 4** (vertex integral). [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]:
>
> $$
> -\frac{i\lambda}{4!}\cdot24\int d^4x\,e^{i(p_1 + p_2 - p_A - p_B)\cdot x} = -i\lambda\,(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2) ,
> $$
>
> and [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]] gives $i\mathcal M = -i\lambda$ (PS (4.98); Yu (7.119), (7.121)).
>
> **Step 5** (enumerate, then filter). The splits of the four legs ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]]), with [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]] for equal masses $m$:
>
> | in → out | loops | matrix element | kinematics |
> |---|---|---|---|
> | $2 \to 2$ | $0$ | $-i\lambda\,(2\pi)^4\delta^4$ | allowed |
> | $1 \to 3$, $3 \to 1$ | $0$ | $-i\lambda\,(2\pi)^4\delta^4$ | forbidden, $m < 3m$ (parts 2, 3) |
> | $0 \to 4$, $4 \to 0$ | $0$ | $-i\lambda\,(2\pi)^4\delta^4$ | forbidden (part 1) |
> | $1 \to 1$ | $1$ | $-\frac{i\lambda}{2}D_F(0)\,(2\pi)^4\delta^4$ | forward only (part 4): no scattering, a mass shift |
> | $0 \to 2$, $2 \to 0$ | $1$ | $-\frac{i\lambda}{2}D_F(0)\,(2\pi)^4\delta^4$ | forbidden (part 1) |
> | $0 \to 0$ | $2$ | $-\frac{i\lambda}{8}D_F(0)^2\,(2\pi)^4\delta^4(0)$ | the vacuum bubble, a phase ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3\|Theorem §C6a.11.3]]) |
>
> *Two routes, one answer.* [[§C6c.1 Amplitudes from Correlation Functions#^ex-c6c-1-1|Example §C6c.1.1]] gets $i\mathcal M = -i\lambda$ from the four-point correlation function by amputation ([[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]]); there the $24$ are the bijections of four external points to four legs, here of four particles to four legs.
>
> *Source: PS §4.6, eqs. (4.92)–(4.98), pp. 110–112 · Yu §7.3, eqs. (7.115)–(7.121) · the table written here from [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]] and [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]]*

^ex-c6c-4-1

## Combinatorial factors at first order

<!-- NEW thm-c6c-4-4 -->

<!-- NEW ex-c6c-4-2 -->

<!-- NEW thm-c6c-4-5 (proof = former Step 4 of der-c6b-3-3, below) -->

<!-- MOVED-STEP4-33 > **Step 4** ($\frac1S$). Relabelling the $n$ vertices and the four legs at each vertex, a group of order $n!\,(4!)^n$, maps contractions to contractions with the same integral (Step 5 of [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]]); the particles are not relabelled. By orbit–stabilizer a diagram $D$ arises from $n!\,(4!)^n/S(D)$ contractions ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]), and the prefactor of Step 1 becomes $\frac{1}{S(D)}(-i\lambda)^n$: each vertex $-i\lambda\int d^4x$, the whole $\frac1S$ (slide 22). A symmetry must fix every leg joined to a particle, so only loops and parallel internal lines can contribute to $S$: "$S$ simpler". -->

<!-- NEW ex-c6c-4-3 -->

## What is not scattering

> [!theorem] Theorem §C6c.4.6: δ-Lines, Forward Pieces and Vacuum Bubbles Are Not Scattering
> In the expansion of [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]], with each term split into its connected pieces,
> 1. **vacuum bubbles** (pieces without particles) factor out as $\langle0|U(T, -T)|0\rangle$ and are omitted;
> 2. **several pieces with particles**: each conserves momentum separately; if every piece is $1 \to 1$ (a $\delta$ line, or a line with insertions passing through), the final momenta equal the initial ones and the term belongs to the $\mathbb 1$ of $\hat S = \mathbb 1 + i\hat T$; otherwise it is a product of smaller processes; neither has the form $\delta^4(\sum k - \sum p)\times$(smooth) of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]];
>
> Either reason suffices to omit a term; one term can be excluded by both (the figure-eight bubble beside two $\delta$-lines is a bubble and part of the $\mathbb 1$, slide 14).
>
> $\phi^4$, $2 \to 2$, through first order (slides 10–18; PS (4.91)–(4.98)):
>
> | term | pieces | value | class |
> |---|---|---|---|
> | $\lambda^0$ | two $\delta$ lines | $2E_A2E_B(2\pi)^6[\delta^3(\mathbf p_A - \mathbf p_1)\delta^3(\mathbf p_B - \mathbf p_2) + (1 \leftrightarrow 2)]$ | 2: the $\mathbb 1$ |
> | $\lambda$, $3$ full contractions | figure-eight $\times$ two $\delta$ lines | $-\frac{i\lambda}{8}D_F(0)^2\int d^4z\times(\lambda^0\text{ term})$ | 1 and 2 |
> | $\lambda$, $6$ single contractions | loop on a passing line $\times$ a $\delta$ line, four diagrams | each $-\frac{i\lambda}{2}D_F(0)\,(2\pi)^4\delta^4(p_A - p_1)\cdot2E_B(2\pi)^3\delta^3(\mathbf p_B - \mathbf p_2)$ and permutations | 2: forward, the $\mathbb 1$ |
> | $\lambda$, no contraction | one vertex | $-i\lambda\,(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2)$ | scattering: $i\mathcal M = -i\lambda$ ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3\|Theorem §C6c.5.3]], 2) |
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* any polynomial interaction, every order, with the prescription of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]] (and its scope).
>
> *Source: PHY 513 Lecture 16, slides 10–18 (slide 11: "This is part of '1' in $\mathcal S = 1 + i\mathcal T$ ⇒ omit this contribution when computing '$i\mathcal T$'"; slide 14: "Overall figure 8 = vacuum bubble ⇒ omit … same momenta in initial+final states ⇒ contribution to '1' … Either 1. or 2. justifies omitting this diagram"; slide 17: "Self-energy (bubble on line) conserves energy ⇒ same momentum in initial and final state ⇒ diagram contributes to '1' in $\mathcal S = 1 + i\mathcal T$ ⇒ omit. Remark: self-energy corrects free state → interacting state") · PS §4.6, pp. 109–113, eqs. (4.90)–(4.98) · the user's PHY 513 notes, Lecture 16 update, §16.3–§16.4 (Table "The first-order matrix element, term by term"; Caution "The partial-contraction count on the slide") · PHY 513 Lecture 16, transcript (the figure-eight term "should absolutely not be part of my Feynman rules for two reasons, at least") · proof written here*

^thm-c6c-4-6

> [!derivation]- Derivation
> **Step 1** (part 1, bubbles). The pieces without particles share no line with the others; summed over all terms they factor out exactly as in [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-4|Theorem §C6a.11.4]], and their sum is $\langle0|U(T, -T)|0\rangle$ ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-2|Theorem §C6a.11.2]]), the normalization that [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]], 2, omits (Step 4 of its derivation).
>
> **Step 2** (part 2). A $1 \to 1$ piece carries $\delta^4(k - p)$ (or $\delta^3(\mathbf p - \mathbf k)$) with $k$, $p$ on the mass shell, so $p = k$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], 4): if every piece is $1 \to 1$, every final momentum equals an initial one, the "nothing happened" part of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]]. Otherwise there are at least two deltas in independent combinations of the momenta, and the term is a product of processes on subsets of the particles; it is not $\delta^4(\sum k - \sum p)$ times a smooth function, the form of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]] that defines $\mathcal M$ ([[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-2|Theorem §C6c.1.2]] for the free four-point function).
>
> **Step 3** (the table). Zeroth order: $T\{\cdots\} \to 1$ and
>
> $$
> {}_0\langle\mathbf p_1\mathbf p_2|\mathbf p_A\mathbf p_B\rangle_0 = \sqrt{2E_12E_22E_A2E_B}\,\langle0|\hat a_1\hat a_2\hat a^\dagger_A\hat a^\dagger_B|0\rangle = 2E_A2E_B(2\pi)^6\bigl[\delta^3(\mathbf p_A - \mathbf p_1)\delta^3(\mathbf p_B - \mathbf p_2) + \delta^3(\mathbf p_A - \mathbf p_2)\delta^3(\mathbf p_B - \mathbf p_1)\bigr]
> $$
>
> (slide 10, PS (4.91)), two $1 \to 1$ pieces per term. First order, with the Wick expansion of [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]], Step 2:
> - full contractions: $-\frac{i\lambda}{4!}\cdot3D_F(0)^2\int d^4z\;{}_0\langle\mathbf p_1\mathbf p_2|\mathbf p_A\mathbf p_B\rangle_0 = -\frac{i\lambda}{8}D_F(0)^2\int d^4z\times(\text{zeroth order})$ (slide 14: "$-\frac18i\lambda$");
> - one contraction, $\overbracket{\hat\phi_a\hat\phi_b}\,{:}\hat\phi_c\hat\phi_d{:}$, $6$ terms: the two remaining fields take one incoming and one outgoing particle ($2$ ways for each of the $4$ choices $(A, 1)$, $(A, 2)$, $(B, 1)$, $(B, 2)$), the other two particles overlap; for $(A, 1)$
>
> $$
> -\frac{i\lambda}{4!}\cdot6\cdot2\,D_F(0)\int d^4z\,e^{-ip_A\cdot z}e^{ip_1\cdot z}\;\overbracket{\langle\mathbf p_2|\mathbf p_B\rangle} = -\frac{i\lambda}{2}D_F(0)\,(2\pi)^4\delta^4(p_A - p_1)\,2E_B(2\pi)^3\delta^3(\mathbf p_B - \mathbf p_2)
> $$
>
> (slide 16: "5 permutations ⇒ factor 6"; the $6$ counts the contracted pair, each picture gets $6\cdot2 = 12$ pairings, $\frac{12}{4!} = \frac12 = \frac1S$ of the tadpole: the user's notes, Caution "The partial-contraction count on the slide"), forward;
> - no contraction: $4!$ attachments, $-i\lambda(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2)$ (Example §C6c.4.1, Steps 3–4; slide 18).
>
> **What the derivation shows.**
> - Two reasons can exclude the same term (slide 14: the bubble and the $\mathbb 1$); either suffices.

^der-c6c-4-6

*Uses:* [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-2|Theorem §C6a.11.2]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-4|Theorem §C6a.11.4]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]], [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-2|Theorem §C6c.1.2]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-3|P6, step 3]]

![[ph-qft-c6b-2-5.svg]]
*The classes of [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]] and [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]] for $\phi\phi \to \phi\phi$ (dashed red: $\delta$-lines, [[§C6c.3 Wick's Theorem between Particle States#^def-c6c-3-1|Def. §C6c.3.1]]; blue: vertices). (1) Zeroth order, the particles pass through. (2) The figure-eight bubble times the same (slide 14). (3) A loop on a passing line next to a $\delta$ line, one of four (slide 16): energy conservation forces $p_1 = p_A$. (4) A loop on the leg of $A$ at order $\lambda^2$ (slide 26): a correction of the external state, removed by amputation. (5) The vertex, the only term of $i\hat T$ at first order. Added figure.*

## More theories at first order

> [!example] Example §C6c.4.4: Φφ² at First Order: the Factor 2 of Φ → φφ
> ![[ph-qft-c6b-2-2.svg]]
>
> In [[§C6b.9 Decay Rates and Widths#^mod-c6b-9-7|Model §C6b.9.7]] ($\mathcal L_{\rm int} = -\mu\Phi\phi^2$, masses $M$, $m$), the first-order processes are:
>
> | in → out | loops | $i\mathcal M$ | kinematics ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2\|Theorem §C6c.4.2]]) |
> |---|---|---|---|
> | $\Phi \to \phi\phi$ | $0$ | $-2i\mu$ | allowed iff $M > 2m$ (part 2) |
> | $\phi\phi \to \Phi$ | $0$ | $-2i\mu$ | allowed for $(p_1 + p_2)^2 = M^2$ (part 3) |
> | $\phi \to \Phi\phi$, $\Phi\phi \to \phi$ | $0$ | $-2i\mu$ | forbidden, $m < M + m$ (parts 2, 3) |
> | $0 \to \Phi\phi\phi$, $\Phi\phi\phi \to 0$ | $0$ | $-2i\mu$ | forbidden (part 1) |
> | $0 \to \Phi$, $\Phi \to 0$ | $1$ ($\phi$ loop) | $-i\mu D_F^{(m)}(0)$ | forbidden (part 1) |
>
> A $\phi$ leg cannot be left without partner, and the $\Phi$ leg cannot close on a $\phi$ leg ([[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]]); the counts are $\frac{1!\,2!}{2^{\ell}\ell!}$ of [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]].
>
> **The decay.** With the $\Phi$ field $\hat\Phi_x$ and the two $\phi$ fields $\hat\phi_{x1}$, $\hat\phi_{x2}$ of $\hat\Phi\hat\phi^2(x)$, and [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]],
>
> $$
> \langle\mathbf p_1\mathbf p_2|{:}\hat\Phi_x\hat\phi_{x1}\hat\phi_{x2}{:}|\mathbf K\rangle_\Phi = \overbracket{\hat\Phi_x|\mathbf K\rangle}\Bigl(\overbracket{\langle\mathbf p_1|\hat\phi_{x1}}\,\overbracket{\langle\mathbf p_2|\hat\phi_{x2}} + \overbracket{\langle\mathbf p_1|\hat\phi_{x2}}\,\overbracket{\langle\mathbf p_2|\hat\phi_{x1}}\Bigr) = 2\,e^{i(p_1 + p_2 - K)\cdot x} ,
> $$
>
> so $\langle\mathbf p_1\mathbf p_2|i\hat T^{(1)}|\mathbf K\rangle_\Phi = -2i\mu(2\pi)^4\delta^4(K - p_1 - p_2)$, $i\mathcal M = -2i\mu$. The same computation with the operators written out, and the width and lifetime, are [[§C6b.9 Decay Rates and Widths#^ex-c6b-9-1|Example §C6b.9.1]] (Steps 3–5 for $\mathcal M$).
>
> *Source: PHY 513, Problem Set 8, Problem 4 (the user's solution: "each of $\hat a_{\mathbf p_1}, \hat a_{\mathbf p_2}$ … pairs with one of the two fields, in 2 ways") · PS Problem 4.2 · the table written here*

^ex-c6c-4-4

> [!example] Example §C6c.4.5: The Cubic Interaction at First Order: Everything Is Forbidden
> ![[ph-qft-c6b-2-3.svg]]
>
> For $\mathcal L_{\rm int} = -\frac{g}{3!}\phi^3$ (the cubic vertex of [[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2|Model §C6a.8.2]]) and on-shell particles of mass $m > 0$, every first-order matrix element with no forward pair vanishes:
>
> | in → out | loops | count $\frac{3!}{2^\ell\ell!}$ | matrix element | kinematics ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2\|Theorem §C6c.4.2]]) |
> |---|---|---|---|---|
> | $1 \to 2$, $2 \to 1$ | $0$ | $6$ | $-ig\,(2\pi)^4\delta^4$ | forbidden, $m < 2m$ (parts 2, 3) |
> | $0 \to 3$, $3 \to 0$ | $0$ | $6$ | $-ig\,(2\pi)^4\delta^4$ | forbidden (part 1) |
> | $0 \to 1$, $1 \to 0$ | $1$ | $3$ | $-\frac{ig}{2}D_F(0)\,(2\pi)^4\delta^4$ | forbidden (part 1) |
>
> **Step 1** (enumerate). Three legs: $n$ particles and $\ell$ loops with $n + 2\ell = 3$, so $(n, \ell) = (3, 0)$ or $(1, 1)$; the $n$ particles split into in and out in all ways ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]]). Coefficients: $-i\frac{g}{3!}\cdot6 = -ig$ and $-i\frac{g}{3!}\cdot3 = -\frac{ig}{2}$.
>
> **Step 2** (filter). $1 \to 2$ in the rest frame of the incoming particle: $m = E_{\mathbf p_1} + E_{\mathbf p_2} \ge 2m$, impossible for $m > 0$ (Theorem §C6c.4.2, Step 3); $2 \to 1$ likewise in the rest frame of the outgoing one; $0 \leftrightarrow 3$ and $0 \leftrightarrow 1$: positive energy on one side only.
>
> So the first process of the cubic theory between on-shell particles is at order $g^2$: $2 \to 2$ through two vertices ([[§C6c.6 Feynman Rules for Amplitudes#^ex-c6c-6-1|Example §C6c.6.1]]). Yu's Yukawa analogue ([[§C6d.4 Feynman Rules for Yukawa Theory#^ex-c6d-4-1|§C6d.4, Example §C6d.4.1]]): of the ten first-order processes only $\phi \to \psi\bar\psi$ and $\psi\bar\psi \to \phi$ survive, and only for $m_\phi > 2m_\psi$ (p. 272).
>
> *Source: Yu §7.1.1, p. 272 (the Yukawa analogue) · written here from [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]] and [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]]*

^ex-c6c-4-5

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] — the vertex integrals give momentum deltas.

> [!remark]- Connections
> - The kinematic filter is the threshold of a decay, $M > \sum m_i$, the condition of the two-body decay formula — [[§C6b.9 Decay Rates and Widths#^thm-c6b-9-6|Theorem §C6b.9.6]].
