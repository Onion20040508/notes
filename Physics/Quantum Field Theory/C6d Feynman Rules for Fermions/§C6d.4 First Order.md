---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6d
section: C6d.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule]] · ↑ [[· C6d Feynman Rules for Fermions]] · [[§C6d.5 Second Order]] →

*Sources: Yu Zhao-Huan, 量子场论讲义, §7.1, eqs. (7.5)–(7.7), pp. 261–262; §7.1.1, eqs. (7.21)–(7.58), Fig. 7.1–7.2, pp. 264–273 (the first-order $T$-matrix elements, the position-space rules (7.25)–(7.28), (7.31)–(7.33), the internal lines (7.40)–(7.41), the tadpoles (7.42)–(7.43), the kinematic filter p. 272, the width (7.44)–(7.58)); §7.1.2, p. 275 (the $1/n!$ rule and its footnote), p. 285 (the closed loop) (page images checked) · PHY 513 Lecture 17 (Larsen, 4 Nov 2026), slides 8, 10–12, 16–18, 23, and transcript · the user's PHY 513 notes, Lecture 17 update, §17.2 (Figure "yukvertex"), §17.5, paragraph "Correspondence with Yu" · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.7, pp. 118–120 · the user's discussion with Larsen after Lecture 17 (2026-11-04).*

At first order the Dyson series of Yukawa theory has one vertex, and the procedure of [[§C6c.4 First Order꞉ Enumerate, then Filter|§C6c.4]] applies: list every matrix element the interaction allows, then keep those that kinematics allows. The Wick split of $i\hat T^{(1)}$ ([[§C6d.4 First Order#^thm-c6d-4-1|Theorem §C6d.4.1]]) leaves terms with three external particles and the tadpoles. The eight three-leg matrix elements ([[§C6d.4 First Order#^thm-c6d-4-2|Theorem §C6d.4.2]]) show the position-space rules for external lines and the vertex ([[§C6d.4 First Order#^thm-c6d-4-3|Theorem §C6d.4.3]]), and the vertex carries no $\frac{1}{3!}$ ([[§C6d.4 First Order#^thm-c6d-4-4|Theorem §C6d.4.4]]). Kinematics keeps two of the ten processes ([[§C6d.4 First Order#^thm-c6d-4-5|Theorem §C6d.4.5]]): the decay $\phi \to f\bar f$ ([[§C6d.4 First Order#^ex-c6d-4-1|Example §C6d.4.1]]), whose width needs spin sums and traces ([[§C6d.4 First Order#^ex-c6d-4-2|Example §C6d.4.2]]), and its inverse. A contraction of two fields is an internal line ([[§C6d.4 First Order#^def-c6d-4-1|Def. §C6d.4.1]]–[[§C6d.4 First Order#^def-c6d-4-4|Def. §C6d.4.4]]). The first one closes a fermion line on itself at one vertex: it carries the $-1$ and the trace of every closed fermion loop ([[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]], [[§C6d.4 First Order#^ex-c6d-4-3|Example §C6d.4.3]]). No Yukawa diagram with external particles has a symmetry factor ([[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]]). The scalar counterpart of each box is in [[§C6c.4 First Order꞉ Enumerate, then Filter|§C6c.4]]; second order is [[§C6d.5 Second Order|§C6d.5]], the collected rules [[§C6d.6 Momentum-Space Feynman Rules|§C6d.6]]. Yu works through the same list in §7.1.1; Lecture 17 computes $\phi \to f\bar f$.

**Setup.** [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] at first order: one factor $-ig\int d^4x\,\hat{\bar\psi}\hat\psi\hat\phi$ of the Dyson series ([[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]]) between free relativistic states over $|0\rangle$ ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]). These states stand for the in and out states at lowest order ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]; beyond it $\sqrt Z$, [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]). [[§C6d.4 First Order#^thm-c6d-4-1|Theorem §C6d.4.1]] is an operator identity and [[§C6d.4 First Order#^thm-c6d-4-5|Theorem §C6d.4.5]] pure kinematics, valid at every order. States are ordered fermion, antifermion, scalar; each bra is the adjoint of its ket.

*Conventions* ([[Larsen PHY 513]]): the eight three-leg processes carry Yu's labels (a)–(h) of his Fig. 7.1; his coupling $\kappa$ is $g$; his bras keep the order of the labels, an overall sign different from the vault's ([[§C6d.4 First Order#^cau-c6d-4-1|Caution: Yu's (7.23)–(7.24) and his order of the bra]]).

## The first-order terms

> [!theorem] Theorem §C6d.4.1: The Wick Split of the First-Order Term
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] the first-order term of the Dyson series ([[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]]) splits into a normal-ordered part and a part with one contraction:
>
> $$
> i\hat T^{(1)} = -ig\int d^4x\;T\{\hat{\bar\psi}_a\hat\psi_a\hat\phi(x)\} = i\hat T^{(1)}_1 + i\hat T^{(1)}_2 ,
> $$
>
> $$
> i\hat T^{(1)}_1 = -ig\int d^4x\;{:}\hat{\bar\psi}_a\hat\psi_a\hat\phi{:}(x) , \qquad i\hat T^{(1)}_2 = -ig\int d^4x\;\bigl(-\operatorname{tr}S_F(0)\bigr)\,\hat\phi(x) = +ig\,\operatorname{tr}S_F(0)\int d^4x\;\hat\phi(x) ,
> $$
>
> because the scalar does not contract with a fermion field (the contractions of $\hat\phi$ with $\hat{\bar\psi}$ and with $\hat\psi$ are $0$, [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]]), and the fermion pair at one point, $\hat{\bar\psi}_a(x)$ with $\hat\psi_a(x)$ to its right, contracts to $-S_F(0)_{aa} = -\operatorname{tr}S_F(0)$, $\operatorname{tr}S_F(0) = \int\frac{d^4p}{(2\pi)^4}\frac{4im}{p^2 - m^2 + i\varepsilon}$ (formal: divergent, as $D_F(0)$, [[§C6a.5 Normal Ordering and Contractions#^cau-c6a-5-3|§C6a.5, Caution: In what sense these identities hold]]). Between free particle states ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-5|Theorem §C6d.3.5]], 1):
> 1. $i\hat T^{(1)}_1$ needs three particles, one for each field: one scalar (in or out), and for $\hat\psi$ an incoming fermion or an outgoing antifermion, for $\hat{\bar\psi}$ an outgoing fermion or an incoming antifermion: $2\cdot2\cdot2 = 8$ processes ([[§C6d.4 First Order#^thm-c6d-4-2|Theorem §C6d.4.2]]);
> 2. $i\hat T^{(1)}_2$ needs one scalar, in or out: $2$ processes, the tadpoles ([[§C6d.4 First Order#^ex-c6d-4-3|Example §C6d.4.3]]);
>
> together the ten processes that Yukawa theory allows dynamically at first order (Yu p. 272).
>
> *Equivalently,* the scalar case is [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]]: each leg of the vertex takes a particle or is closed with a leg of its kind into a loop; here only $\hat{\bar\psi}$ and $\hat\psi$ can close.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* the operator identity exact; the matrix elements between free relativistic states over $|0\rangle$ at first order, standing for in and out states at lowest order ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]).
>
> *Source: Yu §7.1, eqs. (7.6)–(7.7), (7.21)–(7.22), pp. 262, 264 ("此处，非平庸的场缩并只有一项，这是因为实标量场 $\phi(x)$ 和 Dirac 旋量场 $\psi(x)$ 具有不相关的产生湮灭算符"; "要得到非平庸的 $T$ 矩阵元 $\langle f|iT_1^{(1)}|i\rangle$，初态和末态中需要包含 3 个粒子，可列出 8 种情况"), eq. (7.42) ($\operatorname{tr}[S_F(0)] = S_{F,aa}(0)$) · PHY 513 Lecture 17, slide 8 ("Each of the three particles are created or annihilated") · proof written here*

^thm-c6d-4-1

> [!derivation]- Derivation
> **Step 1** (first order). By [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]], $i\hat T^{(1)} = -ig\int d^4x\,T\{\hat{\bar\psi}_a\hat\psi_a\hat\phi(x)\}$; the three fields share the point $x$, and the time ordering of fields at one time keeps their written order ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]], last sentence).
>
> **Step 2** (Wick with three fields). The sets $C$ of disjoint pairs of $\{\hat{\bar\psi}_a, \hat\psi_a, \hat\phi\}$ are $\emptyset$, $\{\hat{\bar\psi}_a\hat\psi_a\}$, $\{\hat{\bar\psi}_a\hat\phi\}$, $\{\hat\psi_a\hat\phi\}$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]]):
>
> $$
> T\{\hat{\bar\psi}_a\hat\psi_a\hat\phi\} = {:}\hat{\bar\psi}_a\hat\psi_a\hat\phi{:} + \underbrace{\bigl(-S_F(0)_{aa}\bigr)}_{\hat{\bar\psi}_a\text{ with }\hat\psi_a}\,{:}\hat\phi{:} + \underbrace{0}_{\hat{\bar\psi}_a\text{ with }\hat\phi}\cdot{:}\hat\psi_a{:} + \epsilon\,\underbrace{0}_{\hat\psi_a\text{ with }\hat\phi}\cdot{:}\hat{\bar\psi}_a{:} ,
> $$
>
> each contraction written as its value, with its pair (left field first) named underneath; the value of the first is Step 3. The last two contractions are $0$: $\hat\phi$ and the Dirac fields act on different Fock factors and commute ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]], Step 6 of [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^der-c6d-3-1|Derivation §C6d.3.1]]). In the second term the pair is adjacent and in the written order, $\epsilon(C) = +1$, and ${:}\hat\phi{:} = \hat\phi$.
>
> **Step 3** (the value of the pair). By [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]], the contraction of $\hat{\bar\psi}_b(y)$ with $\hat\psi_a(x)$ to its right is $-S_F(x - y)_{ab}$; at $y = x$ with $b = a$ summed, it is $-\sum_aS_F(0)_{aa} = -\operatorname{tr}S_F(0)$. With the momentum form of $S_F$ ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]]), $S_F(0) = \int\frac{d^4p}{(2\pi)^4}\frac{i(\slashed p + m)}{p^2 - m^2 + i\varepsilon}$, and $\operatorname{tr}\slashed p = 0$, $\operatorname{tr}\mathbb 1 = 4$ ([[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-3|Theorem §C5a.14.3]]): $\operatorname{tr}S_F(0) = \int\frac{d^4p}{(2\pi)^4}\frac{4im}{p^2 - m^2 + i\varepsilon}$. So $i\hat T^{(1)}_2 = -ig\int d^4x\,(-\operatorname{tr}S_F(0))\hat\phi(x)$.
>
> **Step 4** (which states). By [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-5|Theorem §C6d.3.5]], 1, every field of a normal-ordered product meets one particle, and by [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]] $\hat\psi$ meets an incoming fermion ($\hat\psi^+$) or an outgoing antifermion ($\hat\psi^-$), $\hat{\bar\psi}$ an outgoing fermion ($\hat{\bar\psi}^-$) or an incoming antifermion ($\hat{\bar\psi}^+$), $\hat\phi$ an incoming ($\hat\phi^+$) or outgoing ($\hat\phi^-$) scalar ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]]). For $i\hat T^{(1)}_1$: $2\cdot2\cdot2 = 8$ choices; for $i\hat T^{(1)}_2$: $2$.
>
> **What the derivation shows.**
> - The first-order operator content alone decides the list of processes; whether they happen is kinematics → [[§C6d.4 First Order#^thm-c6d-4-5|Theorem §C6d.4.5]].
> - The tadpole carries the first closed fermion loop, with its $-1$ and its trace → [[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]].

^der-c6d-4-1

*Uses:* [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^der-c6d-3-1|Derivation §C6d.3.1]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], [[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-3|Theorem §C5a.14.3]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-5|Theorem §C6d.3.5]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]]

> [!theorem]- ★ Theorem §C6d.4.2: The Eight Three-Leg First-Order Matrix Elements
> ![[ph-qft-c6d-4-2.svg]]
>
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], with a fermion $f(\mathbf p, s)$ or $f(\mathbf q, s')$, an antifermion $\bar f$, a scalar $\phi(\mathbf k)$, states ordered fermion, antifermion, scalar ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]; bra the adjoint of the ket), the eight processes of $i\hat T^{(1)}_1$ ([[§C6d.4 First Order#^thm-c6d-4-1|Theorem §C6d.4.1]]) have, in Yu's labelling (Fig. 7.1),
>
> | | in → out | fields used | chain | $\langle f\vert i\hat T^{(1)}\vert i\rangle$ | crossings | Yu |
> |---|---|---|---|---|---|---|
> | (a) | $f(p)\,\bar f(q)\,\phi(k) \to 0$ | $\hat\psi^+$, $\hat{\bar\psi}^+$, $\hat\phi^+$ | $\bar v(q)u(p)$ | $-ig\,\bar v(q)u(p)\,(2\pi)^4\delta^4(p + q + k)$ | $0$ | (7.23) |
> | (b) | $\phi(k) \to f(p)\,\bar f(q)$ | $\hat{\bar\psi}^-$, $\hat\psi^-$, $\hat\phi^+$ | $\bar u(p)v(q)$ | $-ig\,\bar u(p)v(q)\,(2\pi)^4\delta^4(k - p - q)$ | $0$ | (7.34), $+i\kappa$ |
> | (c) | $f(p) \to f(q)\,\phi(k)$ | $\hat\psi^+$, $\hat{\bar\psi}^-$, $\hat\phi^-$ | $\bar u(q)u(p)$ | $-ig\,\bar u(q)u(p)\,(2\pi)^4\delta^4(p - q - k)$ | $0$ | (7.35) |
> | (d) | $\bar f(p) \to \bar f(q)\,\phi(k)$ | $\hat{\bar\psi}^+$, $\hat\psi^-$, $\hat\phi^-$ | $\bar v(p)v(q)$ | $+ig\,\bar v(p)v(q)\,(2\pi)^4\delta^4(p - q - k)$ | $1$ | (7.36) |
> | (e) | $0 \to f(p)\,\bar f(q)\,\phi(k)$ | $\hat{\bar\psi}^-$, $\hat\psi^-$, $\hat\phi^-$ | $\bar u(p)v(q)$ | $-ig\,\bar u(p)v(q)\,(2\pi)^4\delta^4(p + q + k)$ | $0$ | (7.30), $+i\kappa$ |
> | (f) | $f(p)\,\bar f(q) \to \phi(k)$ | $\hat\psi^+$, $\hat{\bar\psi}^+$, $\hat\phi^-$ | $\bar v(q)u(p)$ | $-ig\,\bar v(q)u(p)\,(2\pi)^4\delta^4(p + q - k)$ | $0$ | (7.37) |
> | (g) | $f(p)\,\phi(k) \to f(q)$ | $\hat\psi^+$, $\hat{\bar\psi}^-$, $\hat\phi^+$ | $\bar u(q)u(p)$ | $-ig\,\bar u(q)u(p)\,(2\pi)^4\delta^4(p + k - q)$ | $0$ | (7.38) |
> | (h) | $\bar f(p)\,\phi(k) \to \bar f(q)$ | $\hat{\bar\psi}^+$, $\hat\psi^-$, $\hat\phi^+$ | $\bar v(p)v(q)$ | $+ig\,\bar v(p)v(q)\,(2\pi)^4\delta^4(p + k - q)$ | $1$ | (7.39) |
>
> (spins: $u(p) \equiv u^s(p)$, $v(q) \equiv v^{s'}(q)$ and so on). Each element is $-ig$ times the chain read against the arrow times $(-1)^{\#\text{crossings}}$ times the momentum delta. Yu's values agree except in (b) and (e), whose bras hold two fermions: his bra keeps the order of the labels and differs from the vault's by $-1$ ([[§C6d.4 First Order#^cau-c6d-4-1|Caution: Yu's (7.23)–(7.24) and his order of the bra]]). (a)–(d) and (e)–(h) are pairwise inverse processes, initial and final states exchanged.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* first order, free relativistic states over $|0\rangle$, exact as matrix elements; which of them describe physical processes is decided by [[§C6d.4 First Order#^thm-c6d-4-5|Theorem §C6d.4.5]].
>
> *Source: Yu §7.1.1, eqs. (7.23), (7.30), (7.34)–(7.39), Fig. 7.1, pp. 264–270 (page images checked) · beyond the course (Lecture 17 computes (b) only, [[§C6d.4 First Order#^ex-c6d-4-1|Example §C6d.4.1]]) · recomputed here in the vault's conventions*

^thm-c6d-4-2

> [!derivation]- Derivation
> **Step 1** (the vertex integral). Each element is $-ig\int d^4x\,\langle f|{:}\hat{\bar\psi}_a\hat\psi_a\hat\phi{:}(x)|i\rangle$ ([[§C6d.4 First Order#^thm-c6d-4-1|Theorem §C6d.4.1]]). The scalar factor is $e^{-ik\cdot x}$ for an incoming and $e^{+ik\cdot x}$ for an outgoing scalar ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2), the fermion factors those of [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], and $\int d^4x\,e^{i(\sum p_{\rm out} - \sum p_{\rm in})\cdot x} = (2\pi)^4\delta^4(\sum p_{\rm in} - \sum p_{\rm out})$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]).
>
> **Step 2** (the fermion strings and their crossings, [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]). The scalar operators commute with the fermion ones and drop out of the sign. Positions in the fermion string:
> - (a), (f): $\hat{\bar\psi}(1)\,\hat\psi(2)\,\hat a^\dagger_{\mathbf p}(3)\,\hat b^\dagger_{\mathbf q}(4)$; pairs $(2, 3)$ ($u(p)e^{-ip\cdot x}$) and $(1, 4)$ ($\bar v(q)e^{-iq\cdot x}$): nested, $0$ crossings.
> - (b), (e): $\hat b_{\mathbf q}(1)\,\hat a_{\mathbf p}(2)\,\hat{\bar\psi}(3)\,\hat\psi(4)$ (bra $\langle0|\hat b_{\mathbf q}\hat a_{\mathbf p}$, the adjoint of $\hat a^\dagger_{\mathbf p}\hat b^\dagger_{\mathbf q}|0\rangle$); pairs $(2, 3)$ ($\bar u(p)e^{ip\cdot x}$) and $(1, 4)$ ($v(q)e^{iq\cdot x}$): nested, $0$.
> - (c), (g): $\hat a_{\mathbf q}(1)\,\hat{\bar\psi}(2)\,\hat\psi(3)\,\hat a^\dagger_{\mathbf p}(4)$; pairs $(1, 2)$ ($\bar u(q)e^{iq\cdot x}$) and $(3, 4)$ ($u(p)e^{-ip\cdot x}$): apart, $0$.
> - (d), (h): $\hat b_{\mathbf q}(1)\,\hat{\bar\psi}(2)\,\hat\psi(3)\,\hat b^\dagger_{\mathbf p}(4)$; the incoming antifermion is absorbed by $\hat{\bar\psi}$, pair $(2, 4)$ ($\bar v(p)e^{-ip\cdot x}$), the outgoing one is created by $\hat\psi$, pair $(1, 3)$ ($v(q)e^{iq\cdot x}$): $1 < 2 < 3 < 4$, **one crossing**, sign $-$.
>
> **Step 3** (the chains). The vertex joins the index of $\hat{\bar\psi}_a$ to that of $\hat\psi_a$: (a), (f) $\bar v_a(q)u_a(p) = \bar v(q)u(p)$; (b), (e) $\bar u_a(p)v_a(q)$; (c), (g) $\bar u_a(q)u_a(p)$; (d), (h) $\bar v_a(p)v_a(q)$: each the row from $\hat{\bar\psi}$ times the column from $\hat\psi$, read against the arrow ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]).
>
> **Step 4** (assemble). E.g. (d): $-ig\cdot(-1)\cdot\bar v(p)v(q)\int d^4x\,e^{-ip\cdot x}e^{iq\cdot x}e^{ik\cdot x} = +ig\,\bar v(p)v(q)\,(2\pi)^4\delta^4(p - q - k)$. (b) is computed term by term in [[§C6d.4 First Order#^thm-c6d-4-4|Theorem §C6d.4.4]] (all eight frequency terms) and [[§C6d.4 First Order#^ex-c6d-4-1|Example §C6d.4.1]].
>
> **Step 5** (Yu's signs). Yu's kets are the vault's ((7.11) = [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]); his bras are $\langle0|\hat a_{\mathbf p}\hat b_{\mathbf q}\cdots$ (7.12). Only (b) and (e) have two fermion operators in the bra; there $\hat a_{\mathbf p}\hat b_{\mathbf q} = -\hat b_{\mathbf q}\hat a_{\mathbf p}$, and his (7.30), (7.34) carry $+i\kappa$ where the table has $-ig$ ($\kappa \leftrightarrow g$). In (d), (h) his "$+i\kappa$" is the same crossing sign as here.
>
> **What the derivation shows.**
> - Every element has the same factor $-ig\int d^4x$; the external lines and the sign carry the differences → [[§C6d.4 First Order#^thm-c6d-4-3|Theorem §C6d.4.3]].
> - An antifermion passing through the vertex gives a crossing, a sign that depends only on how the states are written → [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-5|Theorem §C6d.3.5]], 3.

^der-c6d-4-2

*Uses:* [[§C6d.4 First Order#^thm-c6d-4-1|Theorem §C6d.4.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]], [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]

> [!caution] Caution: Yu's (7.23)–(7.24) and his order of the bra
> The user's notes (paragraph "Correspondence with Yu") cite Yu (7.23)–(7.24), $i\mathcal M = -i\kappa\,\bar vu$, as "the first-order amplitude for a scalar decaying into a fermion pair". On Yu's pages (PDF pp. 272–273) (7.23)–(7.24) are the first case of Fig. 7.1(a): a fermion, an antifermion and a scalar all **incoming**, final state the vacuum, $\langle0|iT_1^{(1)}|\mathbf p^+, \lambda; \mathbf q^-, \lambda'; \mathbf k\rangle$, kinematically forbidden; $\bar v(q)u(p)$ is the chain of an incoming pair. The decay $\phi \to \psi\bar\psi$ is Fig. 7.1(b), eq. (7.34), with $i\mathcal M = +i\kappa\,\bar u(p, \lambda)v(q, \lambda')$ (7.44): an outgoing pair gives $\bar u\cdots v$. Yu's $+$ against the vault's $-ig\,\bar uv$ ([[§C6d.4 First Order#^ex-c6d-4-1|Example §C6d.4.1]]) comes from his special convention (7.12): his bras keep the order of the labels, $\langle\mathbf p^+; \mathbf q^-| \propto \langle0|\hat a_{\mathbf p}\hat b_{\mathbf q}$, which "differs from the usual definition by a minus sign" (Yu p. 262), while PS (4.118) and [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]] take the Hermitian conjugate. For two identical fermions the same convention flips the overall sign of $ff \to ff$ (Yu (7.82) against PS (4.119)).
>
> *Source: Yu §7.1, pp. 262, 264–265, 268, 272, eqs. (7.11)–(7.12), (7.23)–(7.24), (7.34), (7.44), (7.82) (page images checked) · the user's PHY 513 notes, Lecture 17 update, "Correspondence with Yu" · recorded in `qft-C/ERRATA.md`*

^cau-c6d-4-1

> [!theorem] Theorem §C6d.4.3: The External-Line and Vertex Rules Read Off at First Order
> Every first-order matrix element of $i\hat T^{(1)}_1$ ([[§C6d.4 First Order#^thm-c6d-4-1|Theorem §C6d.4.1]]; the eight of [[§C6d.4 First Order#^thm-c6d-4-2|Theorem §C6d.4.2]], of which Lecture 17 computes $\phi \to f\bar f$) is the product of
> 1. one **vertex** $-ig\int d^4x$ ([[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]]), the same for all eight: the vertex needs no time direction, and its three legs are of fixed kinds, dashed $\hat\phi$, solid $\hat\psi$ with the arrow in, solid $\hat{\bar\psi}$ with the arrow out ([[§C6d.1 Yukawa Theory#^def-c6d-1-1|Def. §C6d.1.1]]);
> 2. one **external line** per particle, its wave function at $x$ ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]]):
>
> | | incoming | outgoing |
> |---|---|---|
> | fermion | $u^s(p)\,e^{-ip\cdot x}$ | $\bar u^s(p)\,e^{+ip\cdot x}$ |
> | antifermion | $\bar v^s(p)\,e^{-ip\cdot x}$ | $v^s(p)\,e^{+ip\cdot x}$ |
> | scalar | $e^{-ip\cdot x}$ | $e^{+ip\cdot x}$ |
>
> 3. the fermion factors written **against the arrow**, row · column ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]);
> 4. the **sign** $(-1)^{\#\text{crossings}}$ of the contraction pattern with the states ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]): $-1$ when an antifermion passes through the vertex ((d), (h)), $+1$ otherwise, for states written as in [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]].
>
> These are the position-space rules; drawn first and evaluated by 1–4, a first-order diagram gives its matrix element without any contraction.
>
> *Equivalently,* the scalar case is [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]] with [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]]: the vertex $-ig\prod_km_k!$ times one plane wave per particle; Yukawa has $\prod_km_k! = 1$ ([[§C6d.4 First Order#^thm-c6d-4-4|Theorem §C6d.4.4]]), and fermions add the spinors and the sign.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* first order, free states over $|0\rangle$ (lowest order); items 1–3 hold for every vertex and external line at every order ([[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]]).
>
> *Source: Yu §7.1, boxed rules (7.25)–(7.28) (incoming lines and the vertex, pp. 266–267: "从 Feynman 图 7.1(a) 和 (7.23) 式还可以看出，位置空间中 Yukawa 相互作用的顶点 Feynman 规则为 $-i\kappa\int d^4x$"), (7.31)–(7.33) (outgoing lines, p. 267), p. 270 ("顶点规则只有一种形式 … 不需要为顶点规则指定时间方向") · PHY 513 Lecture 17, slides 8, 10–12 · PS §4.7, p. 118 (rules 2–3) · read off here from the table of [[§C6d.4 First Order#^thm-c6d-4-2|Theorem §C6d.4.2]]*

^thm-c6d-4-3

> [!derivation]- Derivation
> **Step 1** (factorization). By Steps 1–3 of [[§C6d.4 First Order#^der-c6d-4-2|Derivation §C6d.4.2]] each element is $-ig\int d^4x$ times the scalar factor times $(-1)^{\#\text{crossings}}$ times the fermion pair values, each pair value the wave function of its particle ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]).
>
> **Step 2** (one vertex rule). The prefactor is $-ig\int d^4x$ in all eight rows, whatever is incoming or outgoing: it comes from $\hat H_I$ ([[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]]), not from the states.
>
> **Step 3** (the line rules). Row by row the external factors are the six entries of the table: (a) $u(p)e^{-ip\cdot x}$, $\bar v(q)e^{-iq\cdot x}$, $e^{-ik\cdot x}$; (b) $\bar u(p)e^{ip\cdot x}$, $v(q)e^{iq\cdot x}$, $e^{-ik\cdot x}$; (c) $u(p)e^{-ip\cdot x}$, $\bar u(q)e^{iq\cdot x}$, $e^{ik\cdot x}$; (d) $\bar v(p)e^{-ip\cdot x}$, $v(q)e^{iq\cdot x}$, $e^{ik\cdot x}$; (e)–(h) the same with the scalar reversed. Each entry depends only on the particle and its direction.
>
> **Step 4** (the sign). The crossing counts of Step 2 of [[§C6d.4 First Order#^der-c6d-4-2|Derivation §C6d.4.2]]: one crossing exactly when the antifermion's two operators ($\hat b$ in the bra, $\hat b^\dagger$ in the ket) enclose only one of the two field positions.
>
> **What the derivation shows.**
> - The vertex is the interaction, the lines are the free fields: the split that makes rules possible → [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-1|Theorem §C6d.6.1]].

^der-c6d-4-3

*Uses:* [[§C6d.4 First Order#^der-c6d-4-2|Derivation §C6d.4.2]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]

> [!theorem] Theorem §C6d.4.4: The Yukawa Vertex Carries No Combinatorial Factor
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], let $|\mathbf P\rangle = \sqrt{2E_{\mathbf P}}\,\hat a^\dagger_{\phi,\mathbf P}|0\rangle$ be one scalar and $|\mathbf p, s; \mathbf k, r\rangle = \sqrt{2E_{\mathbf p}2E_{\mathbf k}}\,\hat a^{s\dagger}_{\mathbf p}\hat b^{r\dagger}_{\mathbf k}|0\rangle$ a fermion–antifermion pair, fermion first, with bra $\sqrt{2E_{\mathbf p}2E_{\mathbf k}}\,\langle0|\hat b^r_{\mathbf k}\hat a^s_{\mathbf p}$ ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]). Then
>
> $$
> \langle\mathbf p, s; \mathbf k, r|\,\hat{\bar\psi}_a\hat\psi_a\hat\phi(x)\,|\mathbf P\rangle = \bar u^s(p)\,v^r(k)\,e^{i(p + k - P)\cdot x} ,
> $$
>
> a single term with coefficient $1$: each of the three fields is used by exactly one external particle, $\hat\phi^+$ by the scalar, $\hat{\bar\psi}^-$ by the fermion ($\bar u$), $\hat\psi^-$ by the antifermion ($v$), and no field is left for an internal contraction; the number of assignments of fields to particles is $1\cdot1\cdot1 = 1$. Hence
>
> $$
> \langle\mathbf p, s; \mathbf k, r|i\hat T^{(1)}|\mathbf P\rangle = -ig\,\bar u^s(p)v^r(k)\,(2\pi)^4\delta^4(p + k - P) , \qquad i\mathcal M = -ig\,\bar u^s(p)v^r(k) :
> $$
>
> the vertex is $-ig$, not $-ig/3!$. With the opposite order of the pair, $\hat b^\dagger\hat a^\dagger|0\rangle$, the matrix element and $i\mathcal M$ change sign. *Contrast:* for $\mathcal L_{\rm int} = -\frac{g}{3!}\phi^3$ the three identical fields can be assigned to three scalars in $3!$ ways, and $-i\frac{g}{3!}\cdot3! = -ig$; in general $\mathcal L_{\rm int} = -g\prod_k\phi_k^{m_k}$ gives $-ig\prod_km_k!$ ([[§C6a.13 Feynman Rules for Polynomial Interactions#^thm-c6a-13-2|Theorem §C6a.13.2]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]]), and Yukawa theory has $m_{\bar\psi} = m_\psi = m_\phi = 1$. $\hat\psi$ and $\hat{\bar\psi}$ count as different fields, as $\hat\phi$ and $\hat\phi^\dagger$ of a complex scalar do ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 3). This is the vertex-level statement; the diagram-level one, the $\frac{1}{n!}$ against the $n!$ relabellings of vertices, is [[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]].
>
> *Equivalently,* the scalar case is [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]] ($\phi^4$: the $4!$ attachments cancel the $\frac{1}{4!}$); read off $\mathcal L_{\rm int}$ directly, the vertex is [[§C6d.1 Yukawa Theory#^thm-c6d-1-4|Theorem §C6d.1.4]].
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* first order, free states over $|0\rangle$ (the lowest order, as [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]]); the matrix element is a statement about the factor and holds for any momenta; whether the decay is allowed is kinematics, $m_\phi > 2m$ ([[§C6d.4 First Order#^ex-c6d-4-1|Example §C6d.4.1]]).
>
> *Source: the user's discussion with Larsen after Lecture 17 (2026-11-04) ("if we were to write out the vertex explicitly such as $\langle p, k, s, r|\bar\psi\psi\phi|P\rangle$, there's no room for contraction") · written here · PHY 513 Lecture 17, slide 18 ("Fields in $\bar\psi\psi\phi$ cannot substitute for one another in contractions") · PS §4.7, p. 118 (first comment after the rules) · the general count: [[§C6a.13 Feynman Rules for Polynomial Interactions#^thm-c6a-13-2|Theorem §C6a.13.2]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]]*

^thm-c6d-4-4

> [!derivation]- Derivation
> **Step 1** (eight terms). Split each field into its frequency parts ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]]; [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]] for $\hat\phi$):
>
> $$
> \hat{\bar\psi}_a\hat\psi_a\hat\phi = \sum_{\sigma_1, \sigma_2, \sigma_3 = \pm}\hat{\bar\psi}^{\sigma_1}_a\hat\psi^{\sigma_2}_a\hat\phi^{\sigma_3} , \qquad 2\cdot2\cdot2 = 8 \text{ terms.}
> $$
>
> **Step 2** (the scalar factor). The state space is $\mathcal F_\psi \otimes \mathcal F_\phi$ ([[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], 1), the fermion operators act on the first factor and $\hat\phi$ on the second, and $|\mathbf P\rangle$ has no fermions, the bra no scalar. So the matrix element factorizes:
>
> $$
> \langle\mathbf p, s; \mathbf k, r|\,\hat{\bar\psi}_a\hat\psi_a\hat\phi\,|\mathbf P\rangle = \langle\mathbf p, s; \mathbf k, r|\hat{\bar\psi}_a\hat\psi_a|0\rangle_\psi\;\cdot\;\langle0|\hat\phi(x)|\mathbf P\rangle_\phi .
> $$
>
> In the scalar factor $\hat\phi^-|\mathbf P\rangle$ is a two-scalar state, orthogonal to $\langle0|$: $\sigma_3 = -$ gives $0$. $\sigma_3 = +$: $\langle0|\hat\phi^+(x)|\mathbf P\rangle = e^{-iP\cdot x}$ ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2). Four terms remain.
>
> **Step 3** (the fermion factor; no room for contraction). $\hat\psi^+|0\rangle = 0$ ($\hat\psi^+$ holds only $\hat a$'s), so $\sigma_2 = +$ gives $0$: two terms remain, $\hat{\bar\psi}^+\hat\psi^-|0\rangle$ and $\hat{\bar\psi}^-\hat\psi^-|0\rangle$. The first is the would-be internal contraction: $\hat{\bar\psi}^+_a\hat\psi^-_a|0\rangle = \bigl(\{\hat{\bar\psi}^+_a, \hat\psi^-_a\} - \hat\psi^-_a\hat{\bar\psi}^+_a\bigr)|0\rangle = \{\hat{\bar\psi}^+_a, \hat\psi^-_a\}|0\rangle$, a number times $|0\rangle$ (the $\hat b$, $\hat b^\dagger$ anticommutator, [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]; the tadpole contraction of $\hat{\bar\psi}_a$ with $\hat\psi_a$ of [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]]). Its matrix element is that number times $\langle\mathbf p, s; \mathbf k, r|0\rangle = 0$: after the fermions have contracted with each other, $\hat\phi$ is left alone between $\langle\mathbf p, s; \mathbf k, r|$ and $|\mathbf P\rangle$, and $\langle\mathbf p, \mathbf k|\hat\phi|\mathbf P\rangle = 0$ ($\hat\phi$ changes the scalar number by one and the fermion numbers by zero). Exactly one of the eight terms survives, $\sigma = (-, -, +)$. Counting: three fields, three external particles of three kinds; $\hat\phi$ can meet only the scalar, $\hat{\bar\psi}^-$ (with $\hat a^\dagger$) only the fermion, $\hat\psi^-$ (with $\hat b^\dagger$) only the antifermion: $1\cdot1\cdot1 = 1$ assignment.
>
> **Step 4** (evaluate). With the mode expansions (variables $\mathbf q$, $\mathbf l$, spins $s'$, $r'$):
>
> $$
> \langle\mathbf p, s; \mathbf k, r|\hat{\bar\psi}^-_a\hat\psi^-_a|0\rangle = \sqrt{2E_{\mathbf p}2E_{\mathbf k}}\int\frac{d^3q}{(2\pi)^3}\frac{d^3l}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf q}2E_{\mathbf l}}}\sum_{s', r'}\bar u^{s'}_a(q)e^{iq\cdot x}\,v^{r'}_a(l)e^{il\cdot x}\;\langle0|\hat b^r_{\mathbf k}\hat a^s_{\mathbf p}\,\hat a^{s'\dagger}_{\mathbf q}\hat b^{r'\dagger}_{\mathbf l}|0\rangle .
> $$
>
> The operator string: $\hat a^s_{\mathbf p}\hat a^{s'\dagger}_{\mathbf q} = \{\hat a^s_{\mathbf p}, \hat a^{s'\dagger}_{\mathbf q}\} - \hat a^{s'\dagger}_{\mathbf q}\hat a^s_{\mathbf p}$; in the second term $\hat a^s_{\mathbf p}\hat b^{r'\dagger}_{\mathbf l}|0\rangle = -\hat b^{r'\dagger}_{\mathbf l}\hat a^s_{\mathbf p}|0\rangle = 0$. So
>
> $$
> \langle0|\hat b^r_{\mathbf k}\hat a^s_{\mathbf p}\hat a^{s'\dagger}_{\mathbf q}\hat b^{r'\dagger}_{\mathbf l}|0\rangle = (2\pi)^3\delta^{ss'}\delta^3(\mathbf p - \mathbf q)\,\langle0|\hat b^r_{\mathbf k}\hat b^{r'\dagger}_{\mathbf l}|0\rangle = (2\pi)^6\delta^{ss'}\delta^{rr'}\delta^3(\mathbf p - \mathbf q)\delta^3(\mathbf k - \mathbf l) ,
> $$
>
> with sign $+$: the arcs $\hat a_{\mathbf p}$–$\hat a^\dagger_{\mathbf q}$ (positions 2–3) and $\hat b_{\mathbf k}$–$\hat b^\dagger_{\mathbf l}$ (1–4) are nested ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]]). For the ket $\hat b^\dagger_{\mathbf k}\hat a^\dagger_{\mathbf p}|0\rangle$ (bra $\langle0|\hat a\hat b$) the arcs would cross once: sign $-$. The $\delta^3$'s do the integrals ($\mathbf q = \mathbf p$, $\mathbf l = \mathbf k$), the $(2\pi)^6$ cancel, $\sqrt{2E_{\mathbf p}2E_{\mathbf k}}/\sqrt{2E_{\mathbf q}2E_{\mathbf l}} = 1$ on the support ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 1), the Kronecker deltas do the spin sums, and the index $a$ is summed: $\bar u^s(p)v^r(k)\,e^{ip\cdot x}e^{ik\cdot x}$. With Step 2: $\bar u^s(p)v^r(k)\,e^{i(p + k - P)\cdot x}$, the statement.
>
> **Step 5** (the amplitude). By [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]] the first-order term is $-ig\int d^4x$ times this; $\int d^4x\,e^{i(p + k - P)\cdot x} = (2\pi)^4\delta^4(p + k - P)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); stripping the delta ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]) gives $i\mathcal M = -ig\,\bar u^s(p)v^r(k)$, the value [[§C6d.4 First Order#^ex-c6d-4-1|Example §C6d.4.1]] below obtains with the contraction rules.
>
> **Step 6** (contrast: $\phi^3$). For $\mathcal L_{\rm int} = -\frac{g}{3!}\phi^3$ ([[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2|Model §C6a.8.2]] at $\lambda = 0$) and $\langle\mathbf p_1\mathbf p_2|\hat\phi^3(x)|\mathbf P\rangle$: write $\hat\phi^3 = \hat\phi\hat\phi\hat\phi$ (factors 1, 2, 3). The incoming scalar can be absorbed by the $\hat\phi^+$ of any of the three factors, $\mathbf p_1$ created by the $\hat\phi^-$ of either remaining one, $\mathbf p_2$ by the last: $3\cdot2\cdot1 = 3!$ terms, each $e^{i(p_1 + p_2 - P)\cdot x}$ (the self-contraction of two factors leaves $\langle\mathbf p_1\mathbf p_2|\hat\phi|\mathbf P\rangle = 0$, as in Step 3). So $\langle\mathbf p_1\mathbf p_2|i\hat T^{(1)}|\mathbf P\rangle = -i\frac{g}{3!}\cdot3!\,(2\pi)^4\delta^4 = -ig(2\pi)^4\delta^4$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-5|Example §C6c.4.5]]). The $\frac{1}{3!}$ (and $\frac{1}{4!}$ for $\phi^4$) is a convention chosen to cancel the permutations of identical fields; with $\hat{\bar\psi}$, $\hat\psi$, $\hat\phi$ all different there is nothing to cancel, and writing $\frac{g}{3!}\bar\psi\psi\phi$ would only rescale the coupling (vertex $-ig/6$). General count: $-ig\prod_km_k!$ ([[§C6a.13 Feynman Rules for Polynomial Interactions#^thm-c6a-13-2|Theorem §C6a.13.2]]); Yukawa: $\prod_km_k! = 1!\,1!\,1! = 1$.
>
> **What the derivation shows.**
> - The absence of $\frac{1}{3!}$ is a property of the vertex, distinct fields, independent of the diagram it sits in; the absence of symmetry factors in whole diagrams ([[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]]) follows from the same distinctness.
> - The single fermion sign of the vertex is fixed by the order of the external pair; it is the first instance of [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]].

^der-c6d-4-4

*Uses:* [[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]], [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]], [[§C6a.13 Feynman Rules for Polynomial Interactions#^thm-c6a-13-2|Theorem §C6a.13.2]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-2|P6, step 2]]

## The kinematic filter

> [!theorem] Theorem §C6d.4.5: The Kinematic Filter in Yukawa Theory: Two of Ten
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] (fermion mass $m > 0$, scalar mass $m_\phi > 0$, all external particles on shell) the ten dynamically allowed first-order processes ([[§C6d.4 First Order#^thm-c6d-4-1|Theorem §C6d.4.1]]) are filtered by [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]]:
>
> | process | type | [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2\|Theorem §C6c.4.2]] | occurs |
> |---|---|---|---|
> | (a) $f\bar f\phi \to 0$, (e) $0 \to f\bar f\phi$ | $3 \leftrightarrow 0$ | part 1 | never |
> | tadpoles $\phi \to 0$, $0 \to \phi$ ([[§C6d.4 First Order#^ex-c6d-4-3\|Example §C6d.4.3]]) | $1 \leftrightarrow 0$ | part 1 | never |
> | (c) $f \to f\phi$, (d) $\bar f \to \bar f\phi$ | $1 \to 2$, $m < m + m_\phi$ | part 2 | never |
> | (g) $f\phi \to f$, (h) $\bar f\phi \to \bar f$ | $2 \to 1$, $m < m + m_\phi$ | part 3 | never |
> | (b) $\phi \to f\bar f$ | $1 \to 2$ | part 2 | iff $m_\phi > 2m$ |
> | (f) $f\bar f \to \phi$ | $2 \to 1$ | part 3 | iff $m_\phi > 2m$, at $(p + q)^2 = m_\phi^2$ |
>
> So for $m_\phi > 2m$ exactly two first-order processes occur, the decay $\phi \to f\bar f$ and the fusion $f\bar f \to \phi$; for $m_\phi \le 2m$ none does, and every first-order element vanishes on shell. The other eight are dynamically allowed (their matrix elements are not zero as functions of the momenta) and kinematically forbidden.
>
> *Equivalently,* this is the Yukawa row of [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-3|Theorem §C6c.4.3]] (the interaction decides which processes have a matrix element, kinematics which happen), worked out case by case; for scalars the cubic analogue is [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-5|Example §C6c.4.5]].
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* first order, on-shell external particles, free states over $|0\rangle$; the kinematic statements hold at every order ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]]).
>
> *Source: Yu §7.1.1, p. 272 ("图 7.1 和 7.2 中列举的 10 个 Feynman 图对应于 10 个动力学允许的过程。但是，其中大多数过程在运动学上并不允许 … 当 $m_\phi > 2m_\psi$ 时，有 2 个过程是例外的"); Fig. 7.1–7.2 · PHY 513, Problem Set 8, Problem 4 (the scalar analogue: "provided that $M > 2m$") · case by case written here*

^thm-c6d-4-5

> [!derivation]- Derivation
> **Step 1** ($n \leftrightarrow 0$). (a), (e) and the two tadpoles have particles on one side only: the delta $\delta^4(\sum p)$ needs $\sum p^0 = 0$ with every $p^0 = E_{\mathbf p} > 0$, impossible ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], 1).
>
> **Step 2** ($1 \to 2$). In the rest frame of the decaying particle of mass $M$ energy conservation reads $M = E_1 + E_2 \ge m_1 + m_2$. (c): $M = m$, products $m$ and $m_\phi$: $m \ge m + m_\phi$ is false since $m_\phi > 0$. (d) likewise. (b): $M = m_\phi$, products $m$, $m$: possible iff $m_\phi \ge 2m$, and at $m_\phi = 2m$ only with both products at rest, a set of measure zero ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], 2; Step 4 of [[§C6d.4 First Order#^ex-c6d-4-1|Example §C6d.4.1]]).
>
> **Step 3** ($2 \to 1$). In the rest frame of the outgoing particle of mass $M$, $M = E_1 + E_2 \ge m_1 + m_2$. (g): $M = m$, incoming $m$ and $m_\phi$: false. (h) likewise. (f): $M = m_\phi$, incoming $m$, $m$: possible iff $m_\phi > 2m$, for incoming momenta with $(p + q)^2 = m_\phi^2$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], 3).
>
> **Step 4** (count). Steps 1–3 cover the ten processes: $2 + 2$ never by Step 1, $2 + 2$ never by Steps 2–3, and (b), (f) iff $m_\phi > 2m$.
>
> **What the derivation shows.**
> - The only first-order physics of Yukawa theory is the decay of a heavy scalar and its inverse; scattering starts at order $g^2$ → [[§C6d.5 Second Order|§C6d.5]].

^der-c6d-4-5

*Uses:* [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], [[§C6d.4 First Order#^thm-c6d-4-1|Theorem §C6d.4.1]]

> [!example] Example §C6d.4.1: φ → f f̄ at First Order
> ![[ph-qft-c6d-4-1.svg]]
>
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] with $m_\phi > 2m$, a scalar of momentum $k$ decays into a fermion $(p, s)$ and an antifermion $(q, s')$, final state $|\mathbf p, s; \mathbf q, s'\rangle = \sqrt{2E_{\mathbf p}2E_{\mathbf q}}\,\hat a^{s\dagger}_{\mathbf p}\hat b^{s'\dagger}_{\mathbf q}|0\rangle$ ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]). At first order
>
> $$
> i\mathcal M(\phi \to f\bar f) = -ig\;\bar u^s(p)\,v^{s'}(q) ,
> $$
>
> one diagram, the chain $\bar uv$ read against the arrow. Kinematically allowed iff $m_\phi > 2m$.
>
> **Step 1** (the matrix element). By [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]], $\langle\mathbf p, s; \mathbf q, s'|i\hat T^{(1)}|\mathbf k\rangle = -ig\int d^4x\,\langle\mathbf p, s; \mathbf q, s'|\hat{\bar\psi}_a\hat\psi_a\hat\phi(x)|\mathbf k\rangle$, the bra $\sqrt{2E_{\mathbf p}2E_{\mathbf q}}\langle0|\hat b^{s'}_{\mathbf q}\hat a^s_{\mathbf p}$.
>
> **Step 2** (who contracts with whom). The scalar is absorbed by $\hat\phi^+$: $\hat\phi^+(x)|\mathbf k\rangle = e^{-ik\cdot x}|0\rangle$ ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]]). The outgoing fermion needs an $\hat a^\dagger$: $\hat{\bar\psi}^-$; the outgoing antifermion needs a $\hat b^\dagger$: $\hat\psi^-$ ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]). The fermion string is $\langle0|\hat b_{\mathbf q}\hat a_{\mathbf p}\,\hat{\bar\psi}_a\hat\psi_a|0\rangle$ with arcs $\hat a_{\mathbf p}$–$\hat{\bar\psi}$ (positions 2–3) inside $\hat b_{\mathbf q}$–$\hat\psi$ (1–4): no crossing, sign $+$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]).
>
> **Step 3** (values). $\sqrt{2E_{\mathbf p}}\langle0|\hat a^s_{\mathbf p}\hat{\bar\psi}_a(x)|0\rangle = \bar u^s_a(p)e^{ip\cdot x}$ and $\sqrt{2E_{\mathbf q}}\langle0|\hat b^{s'}_{\mathbf q}\hat\psi_a(x)|0\rangle = v^{s'}_a(q)e^{iq\cdot x}$ (Theorem §C6d.2.1); summing over $a$,
>
> $$
> \langle\mathbf p, s; \mathbf q, s'|i\hat T^{(1)}|\mathbf k\rangle = -ig\,\bar u^s(p)v^{s'}(q)\int d^4x\,e^{i(p + q - k)\cdot x} = -ig\,\bar u^s(p)v^{s'}(q)\,(2\pi)^4\delta^4(k - p - q)
> $$
>
> ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); stripping the delta ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]) gives the statement (every one of the eight frequency terms written out: [[§C6d.4 First Order#^thm-c6d-4-4|Theorem §C6d.4.4]]). By the rules ([[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]]) directly: vertex $-ig$, external $\bar u^s(p)$ (outgoing fermion, the arrow's head) and $v^{s'}(q)$ (outgoing antifermion, the arrow's tail), scalar $1$.
>
> **Step 4** (kinematics). In the rest frame of the scalar, $k = (m_\phi, \mathbf 0)$, conservation gives $\mathbf q = -\mathbf p$ and $m_\phi = 2\sqrt{\mathbf p^2 + m^2} \ge 2m$: allowed iff $m_\phi > 2m$ (at $m_\phi = 2m$ only $\mathbf p = 0$, of measure zero), [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], 2. Of the ten first-order processes of Yukawa theory (Yu Fig. 7.1–7.2) only this one and its inverse $f\bar f \to \phi$ survive ([[§C6d.4 First Order#^thm-c6d-4-5|Theorem §C6d.4.5]]; Yu p. 272; scalar analogue: [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-5|§C6c.4, Example §C6c.4.5]]).
>
> **Step 5** (Yu's sign). Yu (7.34), (7.44) find $i\mathcal M = +i\kappa\,\bar u(p, \lambda)v(q, \lambda')$ with his bra $\langle\mathbf p^+, \lambda; \mathbf q^-, \lambda'| \propto \langle0|\hat a_{\mathbf p}\hat b_{\mathbf q}$ (7.12), which is $-1$ times ours ($\hat a\hat b = -\hat b\hat a$): the same amplitude up to the overall sign of the state, $|\mathcal M|^2$ equal ([[§C6d.4 First Order#^cau-c6d-4-1|Caution: Yu's (7.23)–(7.24) and his order of the bra]]).
>
> *Equivalently,* the scalar analogue is [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-4|Example §C6c.4.4]] ($\Phi \to \phi\phi$, $i\mathcal M = -2i\mu$ from two identical fields); the width with spin sums is [[§C6d.4 First Order#^ex-c6d-4-2|Example §C6d.4.2]].
>
> *Source: Yu §7.1, p. 272 ($\phi \to \psi\bar\psi$ allowed for $m_\phi > 2m_\psi$), eqs. (7.34), (7.44), Fig. 7.1(b) · the user's PHY 513 notes, Lecture 17 update, §17.2, Figure "yukvertex" (c), paragraph "Correspondence with Yu" · PHY 513 Lecture 17, transcript ("what really happened was scalar coming in, particle, antiparticle being created") · computed here in the vault's conventions*

^ex-c6d-4-1

> [!example]- ★ Example §C6d.4.2: The Width of φ → f f̄: Spin Sums, Casimir's Trick, Traces
> ![[ph-qft-c6d-4-1.svg]]
>
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] with $m_\phi > 2m$, the leading-order width of the scalar into a fermion–antifermion pair, summed over the final spins, is
>
> $$
> \sum_{s, s'}|\mathcal M|^2 = 4g^2\,(p\cdot q - m^2) = 2g^2m_\phi^2\Bigl(1 - \frac{4m^2}{m_\phi^2}\Bigr) , \qquad \Gamma(\phi \to f\bar f) = \frac{g^2m_\phi}{8\pi}\Bigl(1 - \frac{4m^2}{m_\phi^2}\Bigr)^{3/2} ,
> $$
>
> zero at threshold $m_\phi = 2m$. The spin sum turns $|\bar uv|^2$ into a trace (Casimir's trick, [[§C5a.14 Gamma-Matrix Technology#^rem-c5a-14-3|§C5a.14, Remark: Why traces]]).
>
> **Step 1** (the amplitude). [[§C6d.4 First Order#^ex-c6d-4-1|Example §C6d.4.1]]: $i\mathcal M = -ig\,\bar u^s(p)v^{s'}(q)$, so $\mathcal M = -g\,\bar u^s(p)v^{s'}(q)$ (Yu (7.44) has $+$, his bra; the sign drops out of $|\mathcal M|^2$).
>
> **Step 2** (complex conjugate). $\bar uv = u^\dagger\gamma^0v$ is a $1\times1$ matrix, so $(\bar uv)^\ast = (u^\dagger\gamma^0v)^\dagger = v^\dagger\gamma^{0\dagger}u = v^\dagger\gamma^0u = \bar vu$, using $\gamma^{0\dagger} = \gamma^0$ (the case $\Gamma = \mathbb 1$ of [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|Theorem §C5a.6.4]]). Hence $\mathcal M^\ast = -g\,\bar v^{s'}(q)u^s(p)$ (Yu (7.45)).
>
> **Step 3** (the square as a trace). With the spinor indices written out and summed,
>
> $$
> |\mathcal M|^2 = g^2\,\bar u_a(p)v_a(q)\,\bar v_b(q)u_b(p) = g^2\,u_b(p)\bar u_a(p)\;v_a(q)\bar v_b(q) = g^2\operatorname{tr}\bigl[u(p)\bar u(p)\,v(q)\bar v(q)\bigr] ,
> $$
>
> moving the number $u_b(p)$ to the front; $u\bar u$ and $v\bar v$ are $4\times4$ matrices, the sum over $a$ is a matrix product and the sum over $b$ the trace (Yu (7.46)).
>
> **Step 4** (spin sums). Summing over the final spins with $\sum_su^s(p)\bar u^s(p) = \slashed p + m$ ([[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]]) and $\sum_{s'}v^{s'}(q)\bar v^{s'}(q) = \slashed q - m$ ([[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-8|Theorem §C5a.12.8]]):
>
> $$
> \sum_{s, s'}|\mathcal M|^2 = g^2\operatorname{tr}\bigl[(\slashed p + m)(\slashed q - m)\bigr] = g^2\bigl[\operatorname{tr}(\slashed p\slashed q) - m\operatorname{tr}\slashed p + m\operatorname{tr}\slashed q - m^2\operatorname{tr}\mathbb 1\bigr] .
> $$
>
> **Step 5** (traces). [[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-3|Theorem §C5a.14.3]]: $\operatorname{tr}\slashed p = p_\mu\operatorname{tr}\gamma^\mu = 0$, $\operatorname{tr}(\slashed p\slashed q) = p_\mu q_\nu\operatorname{tr}(\gamma^\mu\gamma^\nu) = 4p\cdot q$, $\operatorname{tr}\mathbb 1 = 4$ (Yu (7.48)–(7.55)): $\sum|\mathcal M|^2 = 4g^2(p\cdot q - m^2)$.
>
> **Step 6** (kinematics). $k = p + q$ with $k^2 = m_\phi^2$, $p^2 = q^2 = m^2$: $m_\phi^2 = 2m^2 + 2p\cdot q$, so $p\cdot q - m^2 = \frac12(m_\phi^2 - 4m^2) = \frac{m_\phi^2}{2}\bigl(1 - \frac{4m^2}{m_\phi^2}\bigr)$ (Yu (7.56)–(7.57)), and $\sum|\mathcal M|^2 = 2g^2m_\phi^2\beta^2$, $\beta = \sqrt{1 - 4m^2/m_\phi^2}$: a constant, independent of the direction of $\mathbf p$.
>
> **Step 7** (the width). The width sums over all final states, spins included ([[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]]). The two products are a fermion and an antifermion, not identical: $S_{\rm id} = 1$. By [[§C6b.6 Decay Kinematics#^thm-c6b-6-3|Theorem §C6b.6.3]] (equal masses, direction-independent $|\mathcal M|^2$):
>
> $$
> \Gamma = \frac{\beta}{16\pi m_\phi}\sum_{s, s'}|\mathcal M|^2 = \frac{\beta}{16\pi m_\phi}\cdot2g^2m_\phi^2\beta^2 = \frac{g^2m_\phi}{8\pi}\,\beta^3 ,
> $$
>
> Yu (7.58) with $\kappa \to g$. At $m_\phi = 2m$, $\beta = 0$ and $\Gamma = 0$: the decay cannot happen ([[§C6d.4 First Order#^thm-c6d-4-5|Theorem §C6d.4.5]]).
>
> *Equivalently,* the scalar analogue is [[§C6b.6 Decay Kinematics#^ex-c6b-6-1|Example §C6b.6.1]] ($\Phi \to \phi\phi$, $|\mathcal M|^2 = 4\mu^2$, $S_{\rm id} = 2$): there no spin sum, here the trace; the power $\beta^3$ against $\beta$ comes from $\bar uv$, which vanishes for both products at rest.
>
> *Source: Yu §7.1.1, eqs. (7.44)–(7.58), pp. 272–273 (page images checked; "这种把非极化振幅模方中的旋量计算转化为求迹运算的方法称为 Casimir 技巧") · beyond the course (Lecture 17 computes the amplitude only) · written out here in the vault's conventions*

^ex-c6d-4-2

## Internal lines and the first closed loop

> [!definition] Definition §C6d.4.1: Internal Line
> A contraction of two fields at vertices is an **internal line** (propagator) of the diagram; a contraction of a field with an external particle is an **external line** ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]). In Yukawa theory the internal lines are the contraction of $\hat\psi(y)$ with $\hat{\bar\psi}(x)$ to its right and the contraction of $\hat\phi(y)$ with $\hat\phi(x)$,
>
> $$
> S_F(y - x) = \int\frac{d^4p}{(2\pi)^4}\,\frac{i(\slashed p + m)}{p^2 - m^2 + i\varepsilon}\,e^{-ip\cdot(y - x)} , \qquad D_F(y - x) = \int\frac{d^4p}{(2\pi)^4}\,\frac{i}{p^2 - m_\phi^2 + i\varepsilon}\,e^{-ip\cdot(y - x)}
> $$
>
> ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]]): a solid line from $x$ to $y$ with the arrow from the $\hat{\bar\psi}$ end to the $\hat\psi$ end and the momentum $p$ along it, and a dashed line. Its momentum is integrated over all four-vectors $p$. An internal line may join a vertex to itself (the tadpole loop, $S_F(0)$).
>
> *Equivalently,* for scalar theories the internal lines of [[§C6a.13 Feynman Rules for Polynomial Interactions#^thm-c6a-13-3|Theorem §C6a.13.3]] ("both ends on legs of vertices").
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* diagrams of matrix elements and of correlation functions alike.
>
> *Source: Yu §7.1, boxed rules (7.40)–(7.41) and p. 270 ("如果一条缩并线的一端连接着场算符，另一端连接着初态或末态，那么它在 Feynman 图上对应于一条入射外线或出射外线。如果一条缩并线的两端都连接着场算符，那么它对应于一条内线") · PHY 513 Lecture 17, slides 16–17 · PS §4.7, p. 118 (rule 1)*

^def-c6d-4-1

> [!definition] Definition §C6d.4.2: Real and Virtual Particles
> A particle on an external line is **real**: its momentum is on shell, $p^2 = m^2$, with $p^0 = E_{\mathbf p} > 0$. A particle on an internal line ([[§C6d.4 First Order#^def-c6d-4-1|Def. §C6d.4.1]]) is **virtual**: its momentum is integrated over all values, or fixed by conservation at the vertices to a value that need not satisfy $p^2 = m^2$ (**off shell**), and its $p^0$ need not be positive; a virtual particle can also be on shell. The mass shell and the terms on shell and off shell are defined, as Lecture 19 introduces them for the virtual photon $\gamma^\ast$, in [[§C8.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^def-c8-6-1|Def. §C8.6.1]] and [[§C8.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^def-c8-6-2|Def. §C8.6.2]].
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], any theory with Feynman rules; *applies:* a name for the two kinds of lines, no dynamics.
>
> *Source: Yu §7.1, p. 270 ("用内线表示的粒子称为虚粒子 (virtual particle)，它描述场在两个时空点之间的传播行为。虚粒子可以是在壳粒子，也可以是离壳粒子。反过来，用外线表示的粒子称为实粒子 (real particle)，它一定是在壳粒子"); p. 267 (external lines are on shell, (1.79)) · PHY 513 Lecture 19 (Larsen, 11 Nov 2026), slide 8 ("it is a virtual particle … Particles mediating an interaction are off-shell")*

^def-c6d-4-2

> [!definition] Definition §C6d.4.3: Loop Momentum
> A **loop momentum** of a diagram is an internal momentum that conservation at the vertices does not fix in terms of the external momenta; it is integrated, $\int\frac{d^4\ell}{(2\pi)^4}$, over all values. A connected diagram with $V$ vertices and $I$ internal lines has $L = I - V + 1$ of them ([[§C6a.13 Feynman Rules for Polynomial Interactions#^thm-c6a-13-3|Theorem §C6a.13.3]], 2).
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], any theory with Feynman rules; *applies:* momentum-space diagrams.
>
> *Source: Yu §7.1, p. 271 ("圈图中出现一个对四维动量 $p^\mu$ 的积分 $\int d^4p/(2\pi)^4$；这个 $p^\mu$ 的值不能通过初末态的四维动量确定，因而是一个未定的四维动量，称为圈动量 (loop momentum)") · PHY 513 Lecture 17, slide 18 ("Loop momenta (not fixed by external momenta) should be integrated over") · PS §4.7, p. 118 (rule 5)*

^def-c6d-4-3

> [!definition] Definition §C6d.4.4: Tree and Loop Diagrams
> A connected diagram is a **tree diagram** if it has no loop momentum, $L = 0$ ([[§C6d.4 First Order#^def-c6d-4-3|Def. §C6d.4.3]]), and an **$L$-loop diagram** if it has $L \ge 1$; in a tree every internal momentum is fixed by the external ones. Closing a fermion line on itself (a closed fermion loop, [[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]]) or joining two lines at two vertices makes a loop.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], any theory with Feynman rules; *applies:* connected diagrams.
>
> *Source: Yu §7.1, p. 271 ("这种包含圈结构的 Feynman 图称为圈图 (loop diagram)。相应地，不包含圈结构的 Feynman 图称为树图 (tree diagram)，例如，图 7.1 中的 8 种 Feynman 图都是树图"), p. 284 ("具有 $n$ 个未定圈动量的圈图称为 $n$ 圈图") · [[§C6a.13 Feynman Rules for Polynomial Interactions#^thm-c6a-13-3|Theorem §C6a.13.3]] (the count $L = I - V + 1$)*

^def-c6d-4-4

> [!theorem] Theorem §C6d.4.6: A Closed Fermion Loop Gives −1 and a Trace
> A closed fermion line through the vertices $x_1, \dots, x_n$, the arrow running $x_n \to x_{n-1} \to \cdots \to x_1 \to x_n$, contributes
>
> $$
> -\operatorname{tr}\bigl[S_F(x_1 - x_2)\,S_F(x_2 - x_3)\cdots S_F(x_{n-1} - x_n)\,S_F(x_n - x_1)\bigr] ,
> $$
>
> in momentum space $-\operatorname{tr}[\tilde S_F(q_1)\cdots\tilde S_F(q_n)]$ with the momenta along the arrow, times the rest of the diagram with no further sign. For $n = 1$ (the tadpole, a $\hat{\bar\psi}\hat\psi$ contracted at its own vertex): $-\operatorname{tr}S_F(0)$.
>
> *Equivalently,* the scalar case is [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-2|Example §C6c.4.2]]: a scalar loop at one vertex is $D_F(0)$, with $S = 2$ and no sign; the first fermion loop is the tadpole of [[§C6d.4 First Order#^ex-c6d-4-3|Example §C6d.4.3]].
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* any diagram with a closed fermion line, any order (QED alike); exact for the term.
>
> *Source: PHY 513 Lecture 17, slide 23 ("Loops of fermion lines have extra '$-$' sign from reorganization of operators when applying Wick's theorem") · PS §4.7, p. 120, eq. (4.120) ("A closed fermion loop always gives a factor of $-1$ and the *trace* of a product of Dirac matrices") · Yu §7.1, eqs. (7.42), (7.100)–(7.101), p. 285 (boxed: "一个封闭的费米子圈贡献一个额外的负号，并且需要对费米子传播子的乘积求迹"); §7.2, rule 12 (p. 288) · proof written here*

^thm-c6d-4-6

> [!derivation]- Derivation
> **Step 1** (gather the loop). By [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]] the packages $\hat{\bar\psi}\hat\psi(x_k)$ move freely; write those of the loop next to each other, in the order $x_1, \dots, x_n$:
>
> $$
> \hat{\bar\psi}_{c_1}\hat\psi_{c_1}(x_1)\;\hat{\bar\psi}_{c_2}\hat\psi_{c_2}(x_2)\cdots\hat{\bar\psi}_{c_n}\hat\psi_{c_n}(x_n) ,
> $$
>
> positions $1, 2, \dots, 2n$ ($\hat{\bar\psi}(x_k)$ at $2k - 1$, $\hat\psi(x_k)$ at $2k$).
>
> **Step 2** (the arcs). The loop contracts $\hat\psi(x_k)$ with $\hat{\bar\psi}(x_{k+1})$, positions $(2k, 2k + 1)$ for $k = 1, \dots, n - 1$, adjacent, and $\hat{\bar\psi}(x_1)$ with $\hat\psi(x_n)$, positions $(1, 2n)$, an arc over all the others. No arcs cross: the sign is $+1$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], 1; or [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]] with $\epsilon(C) = +1$, moving $\hat\psi(x_n)$ past $2n - 2$ operators).
>
> **Step 3** (the values). In written order ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]]): the pair $\hat\psi_{c_k}(x_k)$, $\hat{\bar\psi}_{c_{k+1}}(x_{k+1})$ is written $\hat\psi$ first and has the value $S_F(x_k - x_{k+1})_{c_kc_{k+1}}$; the outer pair $\hat{\bar\psi}_{c_1}(x_1)$, $\hat\psi_{c_n}(x_n)$ is written $\hat{\bar\psi}$ first and has the value $-S_F(x_n - x_1)_{c_nc_1}$. The product, summed over the indices joined at the vertices,
>
> $$
> -S_F(x_1 - x_2)_{c_1c_2}S_F(x_2 - x_3)_{c_2c_3}\cdots S_F(x_{n-1} - x_n)_{c_{n-1}c_n}S_F(x_n - x_1)_{c_nc_1} = -\operatorname{tr}\bigl[S_F(x_1 - x_2)\cdots S_F(x_n - x_1)\bigr] :
> $$
>
> the last index $c_1$ returns to the first, a trace. $n = 1$: the one pair, $\hat{\bar\psi}_c(x)$ with $\hat\psi_c(x)$ to its right, has the value $-S_F(0)_{cc} = -\operatorname{tr}S_F(0)$.
>
> **Step 4** (no sign from the rest). The loop's packages contain an even number of fermion operators and are fully contracted among themselves, so separating them from the rest of the string is an even permutation (Step 1 of [[§C6d.1 Yukawa Theory#^der-c6d-1-2|Derivation §C6d.1.2]]).
>
> **What the derivation shows.**
> - The $-1$ comes from one pair, the one that closes the loop, written $\hat{\bar\psi}$ before $\hat\psi$: PS (4.120) "move $\psi$ all the way around", Yu (7.101) "$-N[\psi_c(z)\bar\psi_a(x)\cdots]$".
> - The trace is the closed spinor chain: an open line is row · matrices · column ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]), a closed one has no ends.

^der-c6d-4-6

*Uses:* [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]], [[§C6d.1 Yukawa Theory#^der-c6d-1-2|Derivation §C6d.1.2]]

> [!example]- ★ Example §C6d.4.3: The Two Tadpoles: a Closed Fermion Loop at One Vertex
> ![[ph-qft-c6d-4-3.svg]]
>
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] the term $i\hat T^{(1)}_2$ of [[§C6d.4 First Order#^thm-c6d-4-1|Theorem §C6d.4.1]] has two matrix elements, a scalar absorbed (a) or emitted (b) by a fermion loop at one vertex:
>
> $$
> \langle0|i\hat T^{(1)}|\mathbf k\rangle = +ig\,(2\pi)^4\delta^4(k)\,\operatorname{tr}S_F(0) , \qquad \langle\mathbf k|i\hat T^{(1)}|0\rangle = +ig\,(2\pi)^4\delta^4(k)\,\operatorname{tr}S_F(0) , \qquad \operatorname{tr}S_F(0) = \int\frac{d^4p}{(2\pi)^4}\,\frac{i\operatorname{tr}(\slashed p + m)}{p^2 - m^2 + i\varepsilon} :
> $$
>
> a closed loop through one vertex, with the $-1$ and the trace of [[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]] at $n = 1$; one loop momentum $p$ ([[§C6d.4 First Order#^def-c6d-4-3|Def. §C6d.4.3]]). Both are one-loop diagrams with one external line (Yu: "tadpole"), and both vanish on shell: $\delta^4(k)$ with $k^0 = E_{\mathbf k} \ge m_\phi > 0$ ([[§C6d.4 First Order#^thm-c6d-4-5|Theorem §C6d.4.5]]).
>
> **Step 1** (the term). $i\hat T^{(1)}_2 = -ig\int d^4x\,\bigl(-\operatorname{tr}S_F(0)\bigr)\,\hat\phi(x)$ ([[§C6d.4 First Order#^thm-c6d-4-1|Theorem §C6d.4.1]]); the contraction of $\hat{\bar\psi}_a(x)$ with $\hat\psi_a(x)$ is $-S_F(x - x)_{aa} = -\operatorname{tr}S_F(0)$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]]: the pair is written $\hat{\bar\psi}$ before $\hat\psi$).
>
> **Step 2** (the scalar). (a): $\langle0|\hat\phi(x)|\mathbf k\rangle = e^{-ik\cdot x}$; (b): $\langle\mathbf k|\hat\phi(x)|0\rangle = e^{ik\cdot x}$ ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2).
>
> **Step 3** (vertex integral). (a): $-ig\cdot(-\operatorname{tr}S_F(0))\int d^4x\,e^{-ik\cdot x} = +ig\operatorname{tr}S_F(0)\,(2\pi)^4\delta^4(k)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); (b) the same with $\delta^4(-k) = \delta^4(k)$ (Yu (7.42)–(7.43)).
>
> **Step 4** (the loop integral). $S_F(0) = \int\frac{d^4p}{(2\pi)^4}\frac{i(\slashed p + m)}{p^2 - m^2 + i\varepsilon}$ ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]] at $x - y = 0$), and $\operatorname{tr}(\slashed p + m) = 4m$ ([[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-3|Theorem §C5a.14.3]]): $\operatorname{tr}S_F(0) = \int\frac{d^4p}{(2\pi)^4}\frac{4im}{p^2 - m^2 + i\varepsilon}$, a formal (divergent) number, as $D_F(0)$ ([[§C6a.5 Normal Ordering and Contractions#^cau-c6a-5-3|§C6a.5, Caution: In what sense these identities hold]]). The momentum $p$ runs round the loop and is fixed by nothing: a loop momentum.
>
> **Step 5** (fate). On shell $k^0 > 0$, so $\delta^4(k) = 0$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], 1): neither tadpole is a process. Inside larger diagrams the same loop hangs on a scalar line of zero momentum ([[§C6d.5 Second Order#^ex-c6d-5-5|Example §C6d.5.5]] (b)).
>
> *Equivalently,* the scalar case is [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-2|Example §C6c.4.2]]: there the loop is $D_F(0)$ with $S = 2$; here it is $-\operatorname{tr}S_F(0)$ with $S = 1$ ([[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]]): the two ends of a fermion loop are different fields.
>
> *Source: Yu §7.1.1, eqs. (7.42)–(7.43), Fig. 7.2, p. 271 ("像图 7.2(a) 和 7.2(b) 这样只包含一条外线的 Feynman 图称为蝌蚪图 (tadpole diagram)"; "一个封闭的费米子圈贡献一个额外的负号，而且需要对费米子传播子（或其乘积）求迹") · beyond the course · written out here*

^ex-c6d-4-3

> [!theorem] Theorem §C6d.4.7: Yukawa Diagrams Have No Symmetry Factors
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] the relabelling group of $n$ vertices is $S_n$ alone, of order $n!$: the three legs $\hat{\bar\psi}$, $\hat\psi$, $\hat\phi$ of a vertex are of three different kinds and "cannot substitute for one another in contractions". The $\frac{1}{n!}$ of the Dyson series is cancelled by the $n!$ ways of relabelling the vertices, with equal values and equal fermion signs, and
>
> $$
> S(D) = 1 \qquad \text{for every diagram } D \text{ each of whose connected pieces contains an external particle or an external field.}
> $$
>
> The vertex-level statement, no $\frac{1}{3!}$ at a single vertex, is [[§C6d.4 First Order#^thm-c6d-4-4|Theorem §C6d.4.4]]. Vacuum bubbles may have $S > 1$: the second-order bubble with one fermion loop through both vertices and a scalar line between them, and the one with a tadpole loop at each vertex joined by the scalar line, both have $S = 2$ (Yu (7.72)–(7.73): "the $1/2!$ is not cancelled").
>
> *Equivalently,* the scalar case is [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]]: there the factor left over is $\frac1S$; in Yukawa theory every diagram with external particles has $S = 1$.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* combinatorics of the Dyson series, every order; the amplitudes of [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]] (connected) always have $S = 1$.
>
> *Source: PHY 513 Lecture 17, slide 18 ("Symmetry factors: none. Fields in $\bar\psi\psi\phi$ cannot substitute for one another in contractions") · PS §4.7, p. 118 ("the $1/n!$ from the Taylor series of the time-ordered exponential is always canceled by the $n!$ ways of interchanging vertices to obtain the same contraction. The diagrams of Yukawa theory never have symmetry factors, since the three fields $(\bar\psi\psi\phi)$ in $H_I$ cannot substitute for one another in contractions") · Yu §7.1, p. 275 (boxed: "$iT^{(n)}$ 中的 $1/n!$ 因子恰好与时空坐标的交换对称性引起的 $n!$ 因子抵消", footnote: "不过，此规律不适用于下文中具有非平庸对称性因子的气泡图"), eqs. (7.72)–(7.73), p. 286 · proof written here with [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]*

^thm-c6d-4-7

> [!derivation]- Derivation
> **Step 1** (vertex data). In the language of [[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]]: kinds $\bar\psi$, $\psi$, $\phi$ with $\psi \smile \bar\psi$, $\phi \smile \phi$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]]: the contractions of $\hat\psi$ with $\hat\psi$, of $\hat{\bar\psi}$ with $\hat{\bar\psi}$ and of a Dirac field with $\hat\phi$ are $0$); one vertex type with three legs of three kinds, $m_{\bar\psi} = m_\psi = m_\phi = 1$. The leg group is trivial, $|H| = 1!\,1!\,1! = 1$, and $|G_n| = n!$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 1).
>
> **Step 2** (equal values on an orbit). Relabelling the vertices permutes the packages $\hat{\bar\psi}\hat\psi\hat\phi(x_k)$ inside $T$ and renames the integration variables. The first is free of sign ([[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]], 1: each package holds two fermion fields), the second leaves the integral unchanged. So the value of a contraction pattern, sign included, is constant on its orbit, and by [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 2,
>
> $$
> \frac{1}{n!}\sum_{\text{patterns}}(\text{value}) = \frac{1}{|G_n|}\sum_P f(P) = \sum_D\frac{f(D)}{S(D)} .
> $$
>
> **Step 3** ($S = 1$ with external points). Let $g \in \operatorname{Stab}(P)$. A vertex with a leg joined to an external point is fixed ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 3). If a vertex $v$ is fixed, so are its three legs ($H$ trivial), and for each leg $h$ with partner $h'$ ($\{h, h'\} \in P$): $\{gh, gh'\} = \{h, gh'\} \in P$ forces $gh' = h'$, so the vertex of $h'$ is fixed. Moving along lines, every vertex connected to $v$ is fixed. If every connected piece contains an external point, every vertex is fixed, hence every half-edge: $g = e$, $S = 1$.
>
> **Step 4** (bubbles). At $n = 2$, no external points: (a) one fermion loop through $x_1$, $x_2$ and a scalar line, $P = \{\{\psi_1, \bar\psi_2\}, \{\psi_2, \bar\psi_1\}, \{\phi_1, \phi_2\}\}$; the exchange $1 \leftrightarrow 2$ maps each block to a block of $P$ ($\{\psi_2, \bar\psi_1\}$, $\{\psi_1, \bar\psi_2\}$, $\{\phi_2, \phi_1\}$), so $S = 2$ and the orbit has $2!/2 = 1$ element. (b) Tadpoles $\{\psi_1, \bar\psi_1\}$, $\{\psi_2, \bar\psi_2\}$ and $\{\phi_1, \phi_2\}$: likewise $S = 2$. These are Yu's $iT^{(2)}_{13}$, $iT^{(2)}_{14}$ (Fig. 7.11), whose $\frac{1}{2!}$ survives; as for QED ([[§C6a.9 Symmetry Factors in Practice#^cau-c6a-9-2|§C6a.9, Caution: "In QED the symmetry factor is always S = 1" holds for diagrams with external points]]).
>
> **What the derivation shows.**
> - Symmetry factors come from leg permutations at a vertex and from automorphisms not pinned by external points; Yukawa theory has no leg permutations, and external particles pin every connected diagram.
> - The fermion sign does not spoil orbit counting because vertices move as even packages.

^der-c6d-4-7

*Uses:* [[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]]

*Procedure:* [[P5 Symmetry Factor of a Diagram#^p5-5|P5, step 5]]

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] — the vertex integrals give the momentum deltas; for $S_F$ they fix the direction of $q$.
> - [[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]] — the relabelling group with leg kinds and orbit–stabilizer, behind $S = 1$.
> - [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]] — the $\delta^3$'s evaluate the smooth factors $\sqrt{2E}$ on their support.

> [!remark]- Connections
> - The absence of symmetry factors is the QED statement of slide 18 of Lecture 14, for the same reason: a vertex with three legs of three kinds; and with the same exception, vacuum bubbles — [[§C6a.9 Symmetry Factors in Practice#^cau-c6a-9-2|§C6a.9, Caution: "In QED the symmetry factor is always S = 1" holds for diagrams with external points]].
> - The decay rate of $\phi \to f\bar f$ needs $\sum_{s, s'}|\bar u^sv^{s'}|^2 = \operatorname{tr}[(\slashed p + m)(\slashed q - m)] = 4(p\cdot q - m^2)$ (spin sums and traces; Yu (7.46)–(7.58) obtains $\Gamma = \frac{g^2m_\phi}{8\pi}(1 - 4m^2/m_\phi^2)^{3/2}$) — [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-8|Theorem §C5a.12.8]], [[§C5a.14 Gamma-Matrix Technology|§C5a.14]], [[§C6b.5 Decay Widths|§C6b.5]]; processes follow the rules (C8 Quantum electrodynamics, planned).
> - Enumerate, then filter, is Yu's first-order method for any interaction; for scalar theories it gives the tables of [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-3|Theorem §C6c.4.3]] and [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]], and Yukawa theory is their last row — [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]].
> - The width of $\phi \to f\bar f$ is the first use of Casimir's trick: a squared spinor chain summed over spins is a trace — [[§C5a.14 Gamma-Matrix Technology#^rem-c5a-14-3|§C5a.14, Remark: Why traces]], [[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-3|Theorem §C5a.14.3]]; the phase space is [[§C6b.6 Decay Kinematics#^thm-c6b-6-1|Theorem §C6b.6.1]].
> - The tadpole's $\operatorname{tr}S_F(0) \propto m$ vanishes for a massless fermion, by $\operatorname{tr}\slashed p = 0$ alone — [[§C6d.4 First Order#^ex-c6d-4-3|Example §C6d.4.3]], [[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-3|Theorem §C5a.14.3]].
> - The exchanged scalar of $ff \to ff$ is a virtual particle with spacelike momentum, $q^2 = t \le 0$, never on shell — [[§C6d.4 First Order#^def-c6d-4-2|Def. §C6d.4.2]], [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]].
> - The external lines read off here are the free-field contractions of [[§C6d.2 Contractions with External Fermions|§C6d.2]]; the collected rules are [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]].
