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

*Sources: Yu Zhao-Huan, 量子场论讲义, §7.1.1, pp. 264–272, eqs. (7.21)–(7.43), Fig. 7.1–7.2 (all first-order $T$-matrix elements of Yukawa theory; the kinematic filter, p. 272); §7.3, pp. 291–294, eqs. (7.112)–(7.125), Fig. 7.12–7.14 (boxed rules pp. 292–293) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.4, p. 93; §4.6, pp. 109–112, eqs. (4.92)–(4.98) · PHY 513 Lecture 16 (Larsen, 2 Nov 2026), Part B, slides 10–18, and transcript · the user's PHY 513 notes, Lecture 16 update, §16.3–§16.4 · PHY 513, Problem Set 8, Problem 4 (the user's solution, submitted 2026-10-30).*

At first order the Dyson series has a single vertex, and Yu's procedure is to **enumerate, then filter**: list every matrix element the interaction allows ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]]), then keep those that four-momentum conservation allows on the mass shells ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]]); the two filters are independent ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-3|Theorem §C6c.4.3]]). Worked for $\phi\phi \to \phi\phi$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]]) the procedure shows the first combinatorial lessons, in Yu's order (§7.3): the $4!$ attachments cancel the $\frac{1}{4!}$ of the vertex ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]]); when legs close on each other the cancellation is incomplete, and what is left over is the symmetry factor ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-2|Example §C6c.4.2]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-3|Example §C6c.4.3]]). The first-order terms that are not scattering, $\delta$-lines, forward pieces and bubbles, are collected in [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]] (Lecture 16, slides 10–18). Other theories: $\Phi\phi^2$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-4|Example §C6c.4.4]], Problem Set 8) and $\phi^3$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-5|Example §C6c.4.5]]). The Yukawa version is [[§C6d.4 First Order|§C6d.4]].

**Setup and scope.** [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] (a permanent interaction) with $\phi^4$ ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]) as the running theory, as in Yu §7.3; [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]]–[[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-3|Theorem §C6c.4.3]] for any monomial interaction without derivatives. The matrix elements are the first-order terms of $\langle f|\hat S|i\rangle$ between free relativistic states over $|0\rangle$ in place of the in and out states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]): valid at the lowest order of a process; a loop on a single particle is a mass shift that the lowest-order rules do not track ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]). The kinematic filter ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]]) and the counting theorems are exact.

## First order: enumerate, then filter

> [!theorem] Theorem §C6c.4.1: The First-Order Matrix Elements of a Monomial
> Let $\mathcal L_{\rm int} = -g\,M$, $M = \prod_k\phi_k^{m_k}$ a monomial in real fields without derivatives ([[§C6a.13 Feynman Rules for Polynomial Interactions#^def-c6a-13-1|Def. §C6a.13.1]]). Let $|i\rangle$ and $\langle f|$ hold $n_k$ particles of kind $k$ in total. The formula below is the sum of the terms in which every particle is attached to the vertex (no $\delta$-line, [[§C6c.3 Wick's Theorem between Particle States#^def-c6c-3-1|Def. §C6c.3.1]]); these are all the terms if no outgoing momentum equals an incoming one (where they coincide, as on the support of the $1 \to 1$ element, the terms with $\delta$-lines are added: [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-2|Example §C6c.4.2]], Step 2). Then
>
> $$
> \langle f|i\hat T^{(1)}|i\rangle = -ig\int d^4x\,\langle f|M\bigl(\hat\phi_I(x)\bigr)|i\rangle = -ig\prod_k\frac{m_k!}{2^{\ell_k}\,\ell_k!}\,D_F^{(m_k)}(0)^{\ell_k}\;(2\pi)^4\delta^4\Bigl(\sum_ik_i - \sum_jp_j\Bigr), \qquad \ell_k = \frac{m_k - n_k}{2} ,
> $$
>
> nonzero only if every $m_k - n_k$ is even and $\ge 0$: each leg takes one external particle or is closed with another leg of its kind into a loop. In particular, for a tree ($\ell_k = 0$, every leg on a particle), $i\mathcal M = -ig\prod_km_k!$, the vertex factor ([[§C6a.13 Feynman Rules for Polynomial Interactions#^thm-c6a-13-2|Theorem §C6a.13.2]]).
>
> **Procedure** (Yu's enumerate-then-filter): (1) list every split of the legs of $M$ into incoming particles, outgoing particles and pairs closed into loops, each giving a matrix element above; (2) keep those that four-momentum conservation allows on the mass shell ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]]).
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* first order, free relativistic states over $|0\rangle$ in place of the in and out states (as in the opening: lowest order; a loop $D_F(0)$ on a single particle is a mass shift, [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]); complex fields: the legs $\phi$, $\phi^\dagger$ take particles and antiparticles by [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 3.
>
> *Source: Yu §7.1.1, pp. 264–272 (all first-order $T$-matrix elements of Yukawa theory, eqs. (7.21)–(7.43), Fig. 7.1–7.2; "the 10 Feynman diagrams correspond to 10 dynamically allowed processes; most are kinematically forbidden", p. 272); §7.3, eqs. (7.115)–(7.121) · PS §4.6, eqs. (4.92)–(4.98) · proof written here*

^thm-c6c-4-1

> [!derivation]- Derivation
> **Step 1** (first order). $\hat S = \mathbb 1 + i\hat T$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]]) and the $n = 1$ term of the Dyson series ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]]) with $\hat{\mathcal H}_I = gM(\hat\phi_I)$: $i\hat T^{(1)} = -i\int dt\,\hat H_I(t) = -ig\int d^4x\,M(\hat\phi_I(x))$; one time, so $T\{\cdot\}$ acts trivially.
>
> **Step 2** (Wick between the states). Label the $m_k$ factors of kind $k$ as legs. By [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]] (all fields at $x$; [[§C6a.13 Feynman Rules for Polynomial Interactions#^lem-c6a-13-1|Lemma §C6a.13.1]] for several kinds), $\langle f|M|i\rangle$ is the sum over full contractions of legs and particles. Outgoing–incoming pairs give $\delta^3(\mathbf p - \mathbf k) = 0$ (distinct momenta); leg–leg pairs give $D_F^{(m_k)}(x - x) = D_F^{(m_k)}(0)$ (formal, [[§C6a.5 Normal Ordering and Contractions#^cau-c6a-5-3|§C6a.5, Caution: In what sense these identities hold]]); a particle pairs only with a leg of its kind.
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
> - At first order the operator content of $\mathcal L_{\rm int}$ alone decides which processes have a matrix element; kinematics decides which of them happen → [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-3|Theorem §C6c.4.3]].

^der-c6c-4-1

*Uses:* [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]], [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]], [[§C6a.13 Feynman Rules for Polynomial Interactions#^lem-c6a-13-1|Lemma §C6a.13.1]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]

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
> - A decay needs $M > \sum m_i$ (for two bodies, $M > 2m$); a one-vertex fusion $n \to 1$ is the reverse, possible only at the special incoming momenta with $(\sum p_i)^2 = M^2$ (parts 2–3 of the statement; [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-3|Theorem §C6c.4.3]]).

^der-c6c-4-2

*Uses:* [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^der-c6b-1-6|Derivation §C6b.1.6]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-3|P6, step 3]]

> [!theorem] Theorem §C6c.4.3: The Interaction Decides Which Processes Have a Matrix Element; Kinematics Decides Which Happen
> At first order, with $\mathcal L_{\rm int} = -g\prod_k\phi_k^{m_k}$ as in [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]]:
> 1. a process has a nonzero matrix element $\langle f|i\hat T^{(1)}|i\rangle$ — it is **dynamically allowed** — iff for every kind $k$ the number $n_k$ of its particles (incoming plus outgoing) satisfies $n_k \le m_k$ with $m_k - n_k$ even; this depends only on the operator content of $\mathcal L_{\rm int}$, not on masses or momenta;
> 2. a dynamically allowed process **occurs** iff its momentum delta $\delta^4(\sum k - \sum p)$ has support on the mass shells — it is **kinematically allowed** ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]]); this depends only on the masses (for $n \to 1$ also on the incoming momenta), not on $\mathcal L_{\rm int}$;
> 3. for equal masses $m > 0$ the kinematically allowed one-vertex processes are those with at least two particles on each side, and the forward $1 \to 1$.
>
> | theory | dynamically allowed at first order | kinematically allowed |
> |---|---|---|
> | $\phi^4$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1\|Example §C6c.4.1]]) | $2 \to 2$, $1 \leftrightarrow 3$, $0 \leftrightarrow 4$; with a loop $1 \to 1$, $0 \leftrightarrow 2$; the bubble | $2 \to 2$; $1 \to 1$ forward only |
> | $\Phi\phi^2$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-4\|Example §C6c.4.4]]) | $\Phi \leftrightarrow \phi\phi$, $\phi \leftrightarrow \Phi\phi$, $0 \leftrightarrow \Phi\phi\phi$; with a loop $0 \leftrightarrow \Phi$ | $\Phi \to \phi\phi$ iff $M > 2m$; $\phi\phi \to \Phi$ iff $M > 2m$, at $(p_1 + p_2)^2 = M^2$ |
> | $\phi^3$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-5\|Example §C6c.4.5]]) | $1 \leftrightarrow 2$, $0 \leftrightarrow 3$; with a loop $0 \leftrightarrow 1$ | none |
> | Yukawa ([[§C6d.4 First Order#^ex-c6d-4-1\|§C6d.4, Example §C6d.4.1]]) | ten processes (Yu Fig. 7.1–7.2) | $\phi \to \psi\bar\psi$ and $\psi\bar\psi \to \phi$, iff $m_\phi > 2m_\psi$ |
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* first order, any polynomial interaction without derivatives, free relativistic states over $|0\rangle$ in place of the in and out states (lowest order, as [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]]); part 2 holds at every order.
>
> *Source: Yu §7.1.1, p. 272 ("the 10 Feynman diagrams correspond to 10 dynamically allowed processes; most of them are kinematically forbidden … when $m_\phi > 2m_\psi$, two processes are exceptions") · PHY 513, Problem Set 8, Problem 4 ("provided that $M > 2m$") · from the "What the derivation shows" of [[§C6c.4 First Order꞉ Enumerate, then Filter#^der-c6c-4-1|Derivation §C6c.4.1]]*

^thm-c6c-4-3

> [!derivation]- Derivation
> **Step 1** (part 1). By [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]] the matrix element is $-ig\prod_k\frac{m_k!}{2^{\ell_k}\ell_k!}D_F^{(m_k)}(0)^{\ell_k}\,(2\pi)^4\delta^4(\sum k - \sum p)$ with $\ell_k = \frac{m_k - n_k}{2}$, and it is zero iff some $m_k - n_k$ is odd or negative (no full contraction exists, Step 3 of its derivation). The condition involves only the $m_k$ (from $\mathcal L_{\rm int}$) and the $n_k$ (from the process).
>
> **Step 2** (part 2). The only dependence on the momenta is the factor $(2\pi)^4\delta^4(\sum k - \sum p)$, the external momenta being on shell; [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]] decides whether it has support. The coefficient in front is a nonzero number (a nonzero count times powers of $g$ and $D_F(0)$), so the process occurs iff the delta has support. At higher orders $i\mathcal M$ multiplies the same delta ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]), so the kinematic condition is the same.
>
> **Step 3** (part 3, equal masses). By [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]]: no particles on one side, part 1 there, forbidden; one incoming and $n_{\rm out} \ge 2$ outgoing, $m < n_{\rm out}m$, part 2 there, forbidden; $n_{\rm in} \ge 2$ and one outgoing, part 3 there, forbidden; one on each side, part 4 there, forward. With $n_{\rm in}, n_{\rm out} \ge 2$: in the centre-of-mass frame of the incoming particles take total energy $E_{\rm cm} > n_{\rm out}m$; then $n_{\rm out}$ outgoing particles with $\sum\mathbf p_j = \mathbf 0$ and $\sum_jE_{\mathbf p_j} = E_{\rm cm}$ exist (e.g. equal energies $E_{\rm cm}/n_{\rm out} > m$ on momenta of equal size summing to zero), so the delta has support.
>
> **Step 4** (the table). The rows are the tables of [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]], Step 5, [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-4|Example §C6c.4.4]] and [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-5|Example §C6c.4.5]], and Yu p. 272 for Yukawa theory.
>
> **What the derivation shows.**
> - Yu's two filters are independent: the first is a count of legs, the second the threshold of [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]]; a decay needs both a vertex that couples the particles and $M > \sum m_i$.

^der-c6c-4-3

*Uses:* [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-3|P6, step 3]]

> [!example] Example §C6c.4.1: φφ → φφ at First Order, by Contractions with the External States
> ![[ph-qft-c6b-2-1.svg]]
>
> In $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]), for $\mathbf p_1, \mathbf p_2 \notin \{\mathbf p_A, \mathbf p_B\}$,
>
> $$
> \langle\mathbf p_1\mathbf p_2|i\hat T^{(1)}|\mathbf p_A\mathbf p_B\rangle = -i\lambda\,(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2), \qquad i\mathcal M = -i\lambda ;
> $$
>
> the $4!$ ways of attaching the four particles to the four fields cancel the $\frac{1}{4!}$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]]). The other first-order processes are $1 \leftrightarrow 3$, $0 \leftrightarrow 4$ (forbidden), $0 \leftrightarrow 2$ with a loop (forbidden), $1 \to 1$ with a loop (forward only: a mass shift), and the vacuum bubble.
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
> **Step 3** (between the states). By [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]], all four particles must be paired, and outgoing–incoming pairs vanish ($\mathbf p_1, \mathbf p_2 \notin \{\mathbf p_A, \mathbf p_B\}$). The three kinds of term are the classes of [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]] and [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]]: the bubble with $\delta$-lines (Theorem §C6c.4.6, parts 1–2), the forward pieces (Theorem §C6c.4.6, part 2), the vertex (Theorem §C6c.5.3, part 2):
> - the last three terms: $3D_F(0)^2\langle\mathbf p_1\mathbf p_2|\mathbf p_A\mathbf p_B\rangle = 0$ (a bubble times the "1", PS (4.96));
> - $D_F(0)\langle\mathbf p_1\mathbf p_2|{:}\hat\phi_a\hat\phi_b{:}|\mathbf p_A\mathbf p_B\rangle$: two fields take two particles, the other two would pair with each other: $0$ (PS's four diagrams on p. 111, particles passing by);
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

> [!theorem] Theorem §C6c.4.4: The φ⁴ Vertex Carries No Combinatorial Factor
> In $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]), $\mathcal L_{\rm int} = -\frac{\lambda}{4!}\phi^4$:
> 1. if the four legs of a vertex at $x$ are contracted with four different external particles, the $4!$ ways of attaching them to the four identical fields give equal terms ([[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|Theorem §C6c.2.4]], $n = 4$ at one point), and
>
> $$
> -\frac{i\lambda}{4!}\int d^4x\;\cdot\;4!\;(\cdots) = -i\lambda\int d^4x\;(\cdots) :
> $$
>
> the vertex factor is $-i\lambda$, with no combinatorial factor;
> 2. this is why $\mathcal L_{\rm int}$ carries the $\frac{1}{4!}$: to read the vertex off, strip the four fields from $\mathcal L_{\rm int}$, multiply by $i$ and by the $4!$ permutations of the fields;
> 3. for $\mathcal L_{\rm int} = -g\prod_k\phi_k^{m_k}$ the attachments number $\prod_km_k!$ and the vertex is $-ig\prod_km_k!$ ([[§C6a.13 Feynman Rules for Polynomial Interactions#^thm-c6a-13-2|Theorem §C6a.13.2]]).
>
> If legs of the vertex are joined to each other or the diagram has another symmetry, fewer assignments are distinct and a factor $\frac1S$ is left over ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]]).
>
> *Equivalently,* for correlation functions, with external points in place of particles: the ⚑ by-product of [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]] (the $\frac{1}{4!}$ cancels the $4!$ ways of attaching four distinct lines). The Yukawa vertex: [[§C6d.4 First Order#^thm-c6d-4-4|§C6d.4, Theorem §C6d.4.4]].
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]] (part 3: [[§C6a.13 Feynman Rules for Polynomial Interactions#^def-c6a-13-1|Def. §C6a.13.1]]); *applies:* every order, any vertex whose legs go to particles or to lines that no symmetry of the diagram exchanges (every vertex of a tree: [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-6|Theorem §C6c.5.6]]).
>
> *Source: Yu §7.3, p. 292 after eq. (7.120) ("the four identical fields contracted with the initial and final particles give $4!$ equivalent contractions and a combinatorial factor $4!$, which cancels the $1/4!$ in $\mathcal L_1$; the $1/4!$ is introduced in $\mathcal L_1$ so that the vertex rule (7.120) has no extra combinatorial factor"; on the diagram the four external lines connect in $4\cdot3\cdot2\cdot1 = 4!$ ways), p. 296 ("strip the four fields $\phi$ from $\mathcal L_1 = -\lambda\phi^4/4!$, multiply by $i$ and by the $4!$ permutations of the four $\phi$") · PS §4.4, p. 93 ("This was the reason for the factor of 4! in the $\phi^4$ coupling"); §4.6, eq. (4.98) · from the statement of [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]]*

^thm-c6c-4-4

> [!derivation]- Derivation
> **Step 1** (the four legs). At first order ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]], Step 1) the vertex is $-\frac{i\lambda}{4!}\int d^4x\,\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4$, the four factors of $\hat\phi_I(x)^4$ labelled, all at $x$. Let $P_1, \dots, P_4$ be the four particles they are contracted with.
>
> **Step 2** (the assignments). A full contraction of the legs with $P_1, \dots, P_4$ is a bijection $\sigma$, leg $\sigma(j)$ to $P_j$: $4! = 24$ of them, listed in Step 3 of [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]]. Each gives the same product $\prod_jw_{P_j}(x)$ of wave functions ($e^{-ik\cdot x}$ in, $e^{+ip\cdot x}$ out, [[§C6c.2 Contractions with External Particles#^thm-c6c-2-5|Theorem §C6c.2.5]]), because the four legs sit at the same point $x$: [[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|Theorem §C6c.2.4]] with $n = 4$, $y_1 = \cdots = y_4 = x$.
>
> **Step 3** (the sum). $-\frac{i\lambda}{4!}\int d^4x\sum_{\sigma\in S_4}\prod_jw_{P_j}(x) = -\frac{i\lambda}{4!}\cdot24\int d^4x\prod_jw_{P_j}(x) = -i\lambda\int d^4x\prod_jw_{P_j}(x)$.
>
> **Step 4** (part 2). By Step 3 the factor of the vertex is $i\cdot\bigl(-\frac{\lambda}{4!}\bigr)\cdot4! = -i\lambda$: the coefficient of $\phi^4$ in $\mathcal L_{\rm int}$, times $i$ (from $e^{i\int\mathcal L_{\rm int}}$), times $4!$. A coupling written without the $\frac{1}{4!}$, $-\lambda'\phi^4$, would give the vertex $-i\lambda'\cdot4! = -24i\lambda'$.
>
> **Step 5** (part 3). For several kinds a particle attaches only to a leg of its kind ([[§C6a.13 Feynman Rules for Polynomial Interactions#^lem-c6a-13-1|Lemma §C6a.13.1]]); within kind $k$ there are $m_k!$ bijections, all equal by Step 2, so $\prod_km_k!$ in all and the vertex $-ig\prod_km_k!$, as [[§C6a.13 Feynman Rules for Polynomial Interactions#^thm-c6a-13-2|Theorem §C6a.13.2]] and Step 5 of [[§C6c.4 First Order꞉ Enumerate, then Filter#^der-c6c-4-1|Derivation §C6c.4.1]].
>
> **Step 6** (a closed pair of legs). If legs $1$ and $2$ are contracted with each other ($D_F(0)$) and $3$, $4$ with two particles, the assignments $\sigma$ and $\sigma\circ(1\,2)$ give the same contraction: the $24$ bijections of legs to "partners" give only $\frac{24}{2} = 12$ distinct contractions ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-2|Example §C6c.4.2]]), and $\frac{12}{24} = \frac12$ is left over.
>
> **What the derivation shows.**
> - The cancellation needs four distinguishable partners; with a symmetry it is incomplete, and the leftover is $\frac1S$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]]).

^der-c6c-4-4

*Uses:* [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]], [[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|Theorem §C6c.2.4]], [[§C6c.2 Contractions with External Particles#^thm-c6c-2-5|Theorem §C6c.2.5]], [[§C6a.13 Feynman Rules for Polynomial Interactions#^lem-c6a-13-1|Lemma §C6a.13.1]], [[§C6a.13 Feynman Rules for Polynomial Interactions#^thm-c6a-13-2|Theorem §C6a.13.2]]

> [!example] Example §C6c.4.2: The Tadpole between One-Particle States: S = 2, a Mass Shift
> ![[ph-qft-c6c-4-1.svg]]
>
> In $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]), between one-particle states the first-order matrix element is the tadpole:
>
> $$
> \langle\mathbf k'|i\hat T^{(1)}|\mathbf k\rangle = -\frac{i\lambda}{2}\,D_F(0)\,(2\pi)^4\delta^4(k - k') :
> $$
>
> $C(4, 2)\cdot A(2, 2) = 6\cdot2 = 12$ of the $24$ attachments are distinct, the factor $\frac{12}{24} = \frac12$ is left over, and $S = 2$ (the two ends of the loop). The process is forward only ($k' = k$): no scattering, a shift of the mass.
>
> **Step 1** (the Wick terms). By [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]] with the four factors of $\hat\phi_I(x)^4$ labelled $\hat\phi_1, \dots, \hat\phi_4$ (Step 2 of [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]]), $i\hat T^{(1)} = i\hat T^{(1)}_1 + i\hat T^{(1)}_2 + i\hat T^{(1)}_3$ with no, one and two contractions (Yu (7.115)–(7.118)); the one-contraction term has $C(4, 2) = 6$ equal pieces, one per contracted pair $\{1,2\}$, $\{1,3\}$, $\{1,4\}$, $\{2,3\}$, $\{2,4\}$, $\{3,4\}$:
>
> $$
> i\hat T^{(1)}_2 = -\frac{i\lambda}{4!}\int d^4x\,\bigl(\overbracket{\hat\phi_1\hat\phi_2}\,{:}\hat\phi_3\hat\phi_4{:} + \cdots\bigr)_{6\text{ terms}} = -\frac{i\lambda}{4!}\cdot6\int d^4x\,D_F(0)\,{:}\hat\phi_I(x)^2{:} .
> $$
>
> **Step 2** (which term survives between one-particle states). By [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-2|Theorem §C6c.3.2]], 1, every normal-ordered field must meet a particle: ${:}\hat\phi^4{:}$ has four fields for two particles, $0$; the two-contraction term $3D_F(0)^2\langle\mathbf k'|\mathbf k\rangle$ is the bubble on a $\delta$-line ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-3|Example §C6c.4.3]]); only $i\hat T^{(1)}_2$ remains.
>
> **Step 3** (attach the particles). For the pair $\{1, 2\}$ contracted, the two remaining fields take $|\mathbf k\rangle$ and $\langle\mathbf k'|$ in $A(2, 2) = 2$ ways ([[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|Theorem §C6c.2.4]]):
>
> $$
> \langle\mathbf k'|{:}\hat\phi_3\hat\phi_4{:}|\mathbf k\rangle = \overbracket{\langle\mathbf k'|\hat\phi_3}\,\overbracket{\hat\phi_4|\mathbf k\rangle} + \overbracket{\langle\mathbf k'|\hat\phi_4}\,\overbracket{\hat\phi_3|\mathbf k\rangle} = 2\,e^{i(k' - k)\cdot x} ,
> $$
>
> and the same for each of the six pairs: $6\cdot2 = 12$ full contractions in all.
>
> **Step 4** (vertex integral). With [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]],
>
> $$
> \langle\mathbf k'|i\hat T^{(1)}|\mathbf k\rangle = -\frac{i\lambda}{4!}\cdot6\cdot2\,D_F(0)\int d^4x\,e^{i(k' - k)\cdot x} = -\frac{i\lambda}{2}\,D_F(0)\,(2\pi)^4\delta^4(k - k')
> $$
>
> (Yu (7.124), with $\langle\mathbf k|\cdots|\mathbf k\rangle$). $D_F(0) = D_F(x - x)$ is formal (divergent): [[§C6a.5 Normal Ordering and Contractions#^cau-c6a-5-3|§C6a.5, Caution: In what sense these identities hold]].
>
> **Step 5** (the symmetry factor). Of the $4! = 24$ ways to attach "partners" to the four legs, exchanging the two ends of the loop (legs $1 \leftrightarrow 2$ in the picture with $\{1,2\}$ closed) gives the same contraction, so only $12$ are distinct: $\frac{12}{24} = \frac12 = \frac1S$ with $S = 2$, the symmetry factor of the tadpole with the particles held fixed ([[§C6a.8 Position-Space Feynman Rules#^def-c6a-8-1|Def. §C6a.8.1]]; the same $S = 2$ as the correlator tadpole of [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-1|Example §C6a.9.1]]). Drawn first and evaluated with the vertex $-i\lambda\int d^4x$, the diagram needs $\frac1S$: [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]].
>
> **Step 6** (filter). $\delta^4(k - k')$ with both momenta on shell forces $k' = k$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], 4): the element is forward, part of the $\mathbb 1$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], 2). The loop is momentum independent: it shifts the mass, the correction of the external state that the amplitude rules leave out ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]). In $\phi\phi \to \phi\phi$ the same piece appears with a spectator on a $\delta$-line (the table of [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]]; slide 16).
>
> *Source: Yu §7.3, eqs. (7.117), (7.124), Fig. 7.13 (the combinatorial factors $C_4^2 = 6$ and $A_2^2 = 2$ reduce $4! = 24$ to $2$, "the remaining 2 is called the symmetry factor of the Feynman diagram") · PHY 513 Lecture 16, slides 16–17 ("5 permutations ⇒ factor 6"; "self-energy … contributes to '1'") · the user's PHY 513 notes, Lecture 16 update, §16.4, Caution "The partial-contraction count on the slide"*

^ex-c6c-4-2

> [!theorem] Theorem §C6c.4.5: The Factor Left Over in a Matrix Element Is 1/S
> In $\phi^4$ theory, let $D$ be a diagram of order $n$ of $\langle f|\hat S|i\rangle$ whose external points are the particles, labelled and never relabelled. The full contractions of the $4n$ legs and the particles that give $D$ number
>
> $$
> \frac{n!\,(4!)^n}{S(D)} ,
> $$
>
> $S(D)$ the symmetry factor of $D$ with the particles held fixed ([[§C6a.8 Position-Space Feynman Rules#^def-c6a-8-1|Def. §C6a.8.1]]). With the prefactor $\frac{1}{n!}\bigl(\frac{-i\lambda}{4!}\bigr)^n$ of the Dyson series the contribution of $D$ is
>
> $$
> \frac{1}{n!}\Bigl(\frac{-i\lambda}{4!}\Bigr)^n\cdot\frac{n!\,(4!)^n}{S(D)}\cdot(\text{value of one contraction}) = \frac{(-i\lambda)^n}{S(D)}\,(\text{value of one contraction}) :
> $$
>
> the factor left over in the $T$-matrix calculation is $\frac1S$, the symmetry factor of the diagram. So one may draw $D$ first, write it with the vertex $-i\lambda\int d^4x$ of [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]], and divide by $S$. For a polynomial interaction $n!\,(4!)^n$ becomes $|G_{\mathbf n}| = \prod_tn_t!\,|H_t|^{n_t}$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 1).
>
> *Equivalently,* for correlation functions, the external points held fixed in place of the particles: [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-1|Theorem §C6a.8.1]].
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] with $\phi^4$ ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]); *applies:* every order, free relativistic states over $|0\rangle$ as in [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]; it counts every diagram of $\langle f|\hat S|i\rangle$, before [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]] and [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]] select those of $i\mathcal M$.
>
> *Source: Yu §7.3, p. 293 (boxed: "the factor obtained by analysing the symmetry of the Feynman diagram always agrees with the factor left over in the $T$-matrix calculation"), p. 294 ("if one first draws the Feynman diagram and then writes the $T$-matrix element with the position-space Feynman rules, one must finally divide by the symmetry factor of the Feynman diagram") · PHY 513 Lecture 16, slide 22 ("Symmetry factor: divide by $S$") · proof written here (it is what Step 4 of [[§C6c.6 Feynman Rules for Amplitudes#^der-c6c-6-3|Derivation §C6c.6.3]] cites)*

^thm-c6c-4-5

> [!derivation]- Derivation
> **Step 1** (the prefactor). The Dyson series at order $n$ ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-9|Theorem §C6a.3.9]]) with $\hat{\mathcal H}_I = \frac{\lambda}{4!}\hat\phi_I^4$:
>
> $$
> \langle f|\hat S|i\rangle^{(n)} = \frac{1}{n!}\Bigl(\frac{-i\lambda}{4!}\Bigr)^n\int d^4z_1\cdots d^4z_n\;\langle f|\,T\{\hat\phi_I(z_1)^4\cdots\hat\phi_I(z_n)^4\}\,|i\rangle ,
> $$
>
> and by [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]] the matrix element is the sum over the full contractions of the $4n$ legs and the particles, each a labelled diagram with the particles as external points.
>
> **Step 2** ($\frac1S$). Relabelling the $n$ vertices and the four legs at each vertex, a group of order $n!\,(4!)^n$, maps contractions to contractions with the same integral (Step 5 of [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]]); the particles are not relabelled. By orbit–stabilizer a diagram $D$ arises from $n!\,(4!)^n/S(D)$ contractions ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]), and the prefactor of Step 1 becomes $\frac{1}{S(D)}(-i\lambda)^n$: each vertex $-i\lambda\int d^4x$, the whole $\frac1S$ (slide 22). A symmetry must fix every leg joined to a particle, so only loops and parallel internal lines can contribute to $S$: "$S$ simpler".
>
> **Step 3** (checks at first order). $n = 1$, $n!\,(4!)^n = 24$: the vertex with four particles, $S = 1$, $24$ contractions ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]]); the tadpole, $S = 2$, $12$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-2|Example §C6c.4.2]]); the figure-eight, $S = 8$, $3$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-3|Example §C6c.4.3]]).
>
> **What the derivation shows.**
> - The $\frac1S$ splits into a vertex part, where the $\frac{1}{n!}$ is not cancelled completely ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-2|Theorem §C6c.5.2]]), and a line part, where the $\frac{1}{(4!)^n}$ is not ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]]); with the particles held fixed only some structures can contribute ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-4|Theorem §C6c.5.4]]), and trees have $S = 1$ ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-6|Theorem §C6c.5.6]]).

^der-c6c-4-5

*Uses:* [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-9|Theorem §C6a.3.9]], [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]], [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]

*Procedure:* [[P5 Symmetry Factor of a Diagram|P5]]

> [!example] Example §C6c.4.3: The First-Order Bubble: S = 8 = 2·2·2
> ![[ph-qft-c6c-4-2.svg]]
>
> In $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]) the two-contraction term of $i\hat T^{(1)}$ is the figure-eight vacuum bubble,
>
> $$
> i\hat T^{(1)}_3 = -\frac{i\lambda}{4!}\cdot3\int d^4x\,D_F(0)^2 = -\frac{i\lambda}{8}\,D_F(0)^2\int d^4x , \qquad \langle f|i\hat T^{(1)}_3|i\rangle = -\frac{i\lambda}{8}\,D_F(0)^2\,(2\pi)^4\delta^4(0)\;\langle f|i\rangle :
> $$
>
> $3$ of the $24$ attachments are distinct, $S = 8 = 2\cdot2\cdot2$ (each loop $2$, the exchange of the two loops $2$). Between any states it multiplies the $\mathbb 1$ by a number: a phase of the vacuum, not scattering.
>
> **Step 1** (the three full contractions). With the four factors of $\hat\phi_I(x)^4$ labelled $\hat\phi_1, \dots, \hat\phi_4$, the pairings of four fields are $(2\cdot2 - 1)!! = 3$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]):
>
> $$
> \overbracket{\hat\phi_1\hat\phi_2}\,\overbracket{\hat\phi_3\hat\phi_4} + \overbracket{\hat\phi_1\hat\phi_3}\,\overbracket{\hat\phi_2\hat\phi_4} + \overbracket{\hat\phi_1\hat\phi_4}\,\overbracket{\hat\phi_2\hat\phi_3} = 3\,D_F(0)^2 ,
> $$
>
> each a c-number, so $i\hat T^{(1)}_3 = -\frac{i\lambda}{4!}\cdot3\int d^4x\,D_F(0)^2 = -\frac{i\lambda}{8}D_F(0)^2\int d^4x$ (Yu (7.118), (7.125); PS (4.96)).
>
> **Step 2** (between states). A c-number times the identity: $\langle f|i\hat T^{(1)}_3|i\rangle = -\frac{i\lambda}{8}D_F(0)^2\int d^4x\;\langle f|i\rangle$; the overlap $\langle f|i\rangle$ is a product of $\delta$-lines ([[§C6c.3 Wick's Theorem between Particle States#^def-c6c-3-1|Def. §C6c.3.1]]), and $\int d^4x = (2\pi)^4\delta^4(0)$, the volume of spacetime ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]]). For $2 \to 2$ this is the second row of the table of [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]] (slide 14: "$-\frac18i\lambda$").
>
> **Step 3** (the symmetry factor). $\frac{3}{24} = \frac18 = \frac1S$. On the diagram: each loop has two interchangeable ends ($2\cdot2$) and the two loops at the vertex can be exchanged ($2$), $S = 2\cdot2\cdot2 = 8$ ([[§C6a.9 Symmetry Factors in Practice#^thm-c6a-9-1|Theorem §C6a.9.1]] with $\ell = 2$: $2^2\cdot2! = 8$), the same as for correlation functions ([[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-1|Example §C6a.9.1]]); it confirms [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]] with no particles.
>
> **Step 4** (fate). The bubble has no particles; it is the first-order term of $\langle0|\hat S|0\rangle$, a phase ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]]; the vacuum energy, [[§C6a.11 The iε Limit and Vacuum Bubbles#^ex-c6a-11-2|Example §C6a.11.2]]), omitted by [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], 1.
>
> *Source: Yu §7.3, eqs. (7.118), (7.125), Fig. 7.14 ("the two loops each contribute a factor 2, and the two loops are identical and contribute another 2, so the symmetry factor is $2\cdot2\cdot2 = 8$") · PHY 513 Lecture 16, slide 14 · PS §4.6, eq. (4.96)*

^ex-c6c-4-3

## What is not scattering

> [!theorem] Theorem §C6c.4.6: δ-Lines, Forward Pieces and Vacuum Bubbles Are Not Scattering
> In the expansion of [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]], with each term split into its connected pieces,
> 1. **vacuum bubbles** (pieces without particles) factor out as $\langle0|U(T, -T)|0\rangle$ and are omitted;
> 2. **several pieces with particles**: each conserves momentum separately; if every piece is $1 \to 1$ (a $\delta$-line, or a line with insertions passing through), the final momenta equal the initial ones and the term belongs to the $\mathbb 1$ of $\hat S = \mathbb 1 + i\hat T$; otherwise it is a product of smaller processes; neither has the form $\delta^4(\sum k - \sum p)\times$(smooth) of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]].
>
> Either reason suffices to omit a term; one term can be excluded by both (the figure-eight bubble beside two $\delta$-lines is a bubble and part of the $\mathbb 1$, slide 14).
>
> $\phi^4$, $2 \to 2$, through first order (slides 10–18; PS (4.91)–(4.98)):
>
> | term | pieces | value | class |
> |---|---|---|---|
> | $\lambda^0$ | two $\delta$-lines | $2E_A2E_B(2\pi)^6[\delta^3(\mathbf p_A - \mathbf p_1)\delta^3(\mathbf p_B - \mathbf p_2) + (1 \leftrightarrow 2)]$ | 2: the $\mathbb 1$ |
> | $\lambda$, $3$ full contractions | figure-eight $\times$ two $\delta$-lines | $-\frac{i\lambda}{8}D_F(0)^2\int d^4z\times(\lambda^0\text{ term})$ | 1 and 2 |
> | $\lambda$, $6$ single contractions | loop on a passing line $\times$ a $\delta$-line, four diagrams | each $-\frac{i\lambda}{2}D_F(0)\,(2\pi)^4\delta^4(p_A - p_1)\cdot2E_B(2\pi)^3\delta^3(\mathbf p_B - \mathbf p_2)$ and permutations | 2: forward, the $\mathbb 1$ |
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
> - Two reasons can exclude the same term (slide 14: the bubble and the $\mathbb 1$); either suffices (stated in the theorem).

^der-c6c-4-6

*Uses:* [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-2|Theorem §C6a.11.2]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-4|Theorem §C6a.11.4]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]], [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-2|Theorem §C6c.1.2]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-3|P6, step 3]]

![[ph-qft-c6b-2-5.svg]]
*The classes of [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]] and [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]] for $\phi\phi \to \phi\phi$ (dashed red: $\delta$-lines, [[§C6c.3 Wick's Theorem between Particle States#^def-c6c-3-1|Def. §C6c.3.1]]; blue: vertices). (1) Zeroth order, the particles pass through. (2) The figure-eight bubble times the same (slide 14). (3) A loop on a passing line next to a $\delta$ line, one of four (slide 16): energy conservation forces $p_1 = p_A$. (4) A loop on the leg of $A$ at order $\lambda^2$ (slide 26): a correction of the external state, removed by amputation. (5) The vertex, the only term of $i\hat T$ at first order. Added figure.*

## More theories at first order

> [!example] Example §C6c.4.4: Φφ² at First Order: the Factor 2 of Φ → φφ
> ![[ph-qft-c6b-2-2.svg]]
>
> In [[§C6b.6 Decay Kinematics#^mod-c6b-6-4|Model §C6b.6.4]] ($\mathcal L_{\rm int} = -\mu\Phi\phi^2$, masses $M$, $m$), the first-order processes are:
>
> | in → out | loops | $i\mathcal M$ | kinematics ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2\|Theorem §C6c.4.2]]) |
> |---|---|---|---|
> | $\Phi \to \phi\phi$ | $0$ | $-2i\mu$ | allowed iff $M > 2m$ (part 2) |
> | $\phi\phi \to \Phi$ | $0$ | $-2i\mu$ | allowed iff $M > 2m$, at $(p_1 + p_2)^2 = M^2$ (part 3) |
> | $\phi \to \Phi\phi$, $\Phi\phi \to \phi$ | $0$ | $-2i\mu$ | forbidden, $m < M + m$ (parts 2, 3) |
> | $0 \to \Phi\phi\phi$, $\Phi\phi\phi \to 0$ | $0$ | $-2i\mu$ | forbidden (part 1) |
> | $0 \to \Phi$, $\Phi \to 0$ | $1$ ($\phi$ loop) | $-i\mu D_F^{(m)}(0)$ | forbidden (part 1) |
>
> A $\phi$ leg cannot be left without partner, and the $\Phi$ leg cannot close on a $\phi$ leg ([[§C6a.13 Feynman Rules for Polynomial Interactions#^lem-c6a-13-1|Lemma §C6a.13.1]]); the counts are $\frac{1!\,2!}{2^{\ell}\ell!}$ of [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]].
>
> **The decay.** With the $\Phi$ field $\hat\Phi_x$ and the two $\phi$ fields $\hat\phi_{x1}$, $\hat\phi_{x2}$ of $\hat\Phi\hat\phi^2(x)$, and [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]],
>
> $$
> \langle\mathbf p_1\mathbf p_2|{:}\hat\Phi_x\hat\phi_{x1}\hat\phi_{x2}{:}|\mathbf K\rangle_\Phi = \overbracket{\hat\Phi_x|\mathbf K\rangle}\Bigl(\overbracket{\langle\mathbf p_1|\hat\phi_{x1}}\,\overbracket{\langle\mathbf p_2|\hat\phi_{x2}} + \overbracket{\langle\mathbf p_1|\hat\phi_{x2}}\,\overbracket{\langle\mathbf p_2|\hat\phi_{x1}}\Bigr) = 2\,e^{i(p_1 + p_2 - K)\cdot x} ,
> $$
>
> so $\langle\mathbf p_1\mathbf p_2|i\hat T^{(1)}|\mathbf K\rangle_\Phi = -2i\mu(2\pi)^4\delta^4(K - p_1 - p_2)$, $i\mathcal M = -2i\mu$. The same computation with the operators written out, and the width and lifetime, are [[§C6b.6 Decay Kinematics#^ex-c6b-6-1|Example §C6b.6.1]] (Steps 3–5 for $\mathcal M$).
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
> So the first process of the cubic theory between on-shell particles is at order $g^2$: $2 \to 2$ through two vertices ([[§C6c.6 Feynman Rules for Amplitudes#^ex-c6c-6-1|Example §C6c.6.1]]). Yu's Yukawa analogue ([[§C6d.4 First Order#^ex-c6d-4-1|§C6d.4, Example §C6d.4.1]]): of the ten first-order processes only $\phi \to \psi\bar\psi$ and $\psi\bar\psi \to \phi$ survive, and only for $m_\phi > 2m_\psi$ (p. 272).
>
> *Source: Yu §7.1.1, p. 272 (the Yukawa analogue) · written here from [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]] and [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]]*

^ex-c6c-4-5

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] — the vertex integrals give momentum deltas.
> - [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]] — a delta whose argument has no zero on the mass shell vanishes there: the kinematic filter.
> - [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]] — $2\ell$ legs pair in $(2\ell - 1)!!$ ways: the loops closed at a vertex.
> - [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]] — the relabelling group $|G_{\mathbf n}|$ and orbit–stabilizer behind the coefficient $\frac1S$.

> [!remark]- Connections
> - The $\frac1S$ left over in a matrix element is the $\frac1S$ of correlation functions, with the particles in place of the external points — [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-1|Theorem §C6a.8.1]], [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-1|Example §C6a.9.1]].
> - Yu's first order is Yukawa theory: of ten dynamically allowed processes only $\phi \to f\bar f$ and its inverse survive the filter — [[§C6d.4 First Order#^ex-c6d-4-1|§C6d.4, Example §C6d.4.1]].
> - The kinematic filter is the threshold of a decay, $M > \sum m_i$, the condition of the two-body decay formula — [[§C6b.6 Decay Kinematics#^thm-c6b-6-1|Theorem §C6b.6.1]].
> - The fermion mirror of this section: the Wick split and the eight three-leg elements of Yukawa theory, the rules read off them, the filter keeping two of ten, the tadpoles, the vertex without $\frac{1}{3!}$ and $S = 1$ — [[§C6d.4 First Order#^thm-c6d-4-1|Theorem §C6d.4.1]], [[§C6d.4 First Order#^thm-c6d-4-3|Theorem §C6d.4.3]], [[§C6d.4 First Order#^thm-c6d-4-5|Theorem §C6d.4.5]], [[§C6d.4 First Order#^ex-c6d-4-3|Example §C6d.4.3]], [[§C6d.4 First Order#^thm-c6d-4-4|Theorem §C6d.4.4]], [[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]].
