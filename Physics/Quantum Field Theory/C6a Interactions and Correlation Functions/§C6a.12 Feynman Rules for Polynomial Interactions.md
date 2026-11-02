---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6a
section: C6a.12
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6a.11 The iε Limit and Vacuum Bubbles]] · ↑ [[· C6a Interactions and Correlation Functions]] · [[§C6b.1 The S-Matrix and the Invariant Amplitude]] →

*Sources: Yu Zhao-Huan, 量子场论讲义, §6.3.1, eq. (6.166) (one Wick theorem for any set of fields); §7.2, pp. 287–288 (momentum-space rules 6–12; the vertex as $i$ times the interaction term with the field operators stripped); §7.3, pp. 291–292, eqs. (7.112)–(7.120), p. 296 (boxed: vertex $-i\lambda$ and "divide by the symmetry factor"; "multiply by the $4!$ permutations of the four $\phi$"); §7.4, pp. 296–300, eqs. (7.133)–(7.143) and momentum-space rules 1–5 (complex scalar) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.4, pp. 92–95, eq. (4.47); §4.6, pp. 114–115 (the $\phi^4$ rules) · PHY 513, Problem Set 8, Problems 1(b), 2 and 4 (statements; the user's solutions, submitted 2026-10-30) · the user's note "Symmetry Factors and the Orbit–Stabilizer Theorem" (Oct 2026), §8 · PHY 513 Lecture 14 (Larsen, 26 Oct 2026), slides 16–20.*

[[§C6a.8 Position-Space Feynman Rules|§C6a.8]] and [[§C6a.10 Feynman Rules in Momentum Space|§C6a.10]] derived the Feynman rules for one theory, $\phi^4$ ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]): one real field, one vertex with four legs and coefficient $\frac{\lambda}{4!}$. Problem Set 8 used three more instances of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]: the cubic–quartic theory ([[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2|Model §C6a.8.2]]), the complex scalar with $(\phi^\dagger\phi)^2$ ([[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-3|Model §C6a.8.3]]) and two fields with $\Phi\phi^2$ ([[§C6b.9 Decay Rates and Widths#^mod-c6b-9-6|Model §C6b.9.6]]). This section states the rules for every polynomial interaction without derivatives. **Unchanged** from $\phi^4$: the Dyson series, Wick's theorem, one propagator per contraction, momentum conservation at each vertex, one $\int\frac{d^4k}{(2\pi)^4}$ per loop, and $\frac1S$ from orbit–stabilizer. **New**:
1. several field types, each with its own propagator; fields of different types never contract ([[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]]);
2. complex fields, whose lines are oriented ([[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-2|Theorem §C6a.7.2]], 3);
3. monomials of any degree, with vertex factor $-ic\prod_in_i!$ for $\mathcal L_{\rm int} \ni -c\prod_i\phi_i^{n_i}$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]);
4. vertices with legs of several kinds ([[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]]), so fewer relabellings and smaller symmetry factors.

The rules for $S$-matrix elements, with external lines instead of external points, are in [[§C6b.3 Feynman Rules for Amplitudes|§C6b.3]] (the external-state contractions they rest on in [[§C6b.2 Matrix Elements between Particle States|§C6b.2]]). Yu states the rules case by case for $S$-matrix elements: Yukawa in §7.2, $\phi^4$ in §7.3, the lines of complex scalars and vectors in §7.4 (Remark: Yu's route, below).

**Setup** ([[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] with $\mathcal L_{\rm int}$ a polynomial without derivatives): as in [[§C6a.7 Feynman Diagrams for Correlation Functions|§C6a.7]]–[[§C6a.10 Feynman Rules in Momentum Space|§C6a.10]], the expansion in the couplings of the numerator of the master formula ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-7|Theorem §C6a.4.7]]), free-vacuum values $\langle0|T\{\cdots\}|0\rangle$ of interaction-picture fields; the correlator in $|\Omega\rangle$ is numerator over denominator ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-5|Theorem §C6a.11.5]]); identities hold order by order, as formal power series.

*Conventions* ([[Larsen PHY 513]]): real fields $\hat\phi_j$ of mass $m_j$; a complex field $\hat\phi$ with particles $\hat a^\dagger$ and antiparticles $\hat b^\dagger$ ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]]); $D_F^{(m)}$ the Feynman propagator of mass $m$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]); $\mathcal L_{\rm int} = -\sum_tg_tM_t$, $\hat{\mathcal H}_I = -\mathcal L_{\rm int}(\hat\phi_I)$ (no derivatives); a complex line points from its $\hat\phi^\dagger$ end to its $\hat\phi$ end.

The counting is that of [[§C6a.8 Position-Space Feynman Rules|§C6a.8]] with more kinds of legs, proved in [[§CA.8 Splitting Pairings and the Exponential Formula|§CA.8]] and listed at the end. A contraction pattern with several vertex types and several kinds of legs is a pairing of half-edges that respects a compatibility relation between kinds ([[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]]); relabelling the $n_t$ vertices of each type and the legs of equal kind at each vertex is a group of order

$$
|G_{\mathbf n}| = \prod_tn_t!\,\Bigl(\prod_km_{t,k}!\Bigr)^{n_t} ,
$$

the inverse of the prefactor; by orbit–stabilizer a diagram $D$ is produced by $|G_{\mathbf n}|/S(D)$ of the contractions, as $n!\,(4!)^n/S(D)$ for $\phi^4$ ([[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-1|Theorem §C6a.8.1]]; [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]; $|G_{\mathbf n}| = n!\,(3!)^n$ for $\phi^3$ and $n!\,(2!\,2!)^n$ for $(\phi^\dagger\phi)^2$). In momentum space the plane waves meeting at a vertex integrate to a delta function, $\int d^4z\,e^{ip\cdot z} = (2\pi)^4\delta^4(p)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]).

## Lines and vertices

> [!theorem] Lemma §C6a.12.1: The Contractions of Several Free Fields
> Let $\hat\phi_1, \dots, \hat\phi_N$ be free real fields of masses $m_1, \dots, m_N$ and $\hat\phi$ a free complex field of mass $m$, all with independent mode operators. Then
> 1. $\langle0|T\{\hat\phi_i(x)\hat\phi_j(y)\}|0\rangle = \delta_{ij}\,D_F^{(m_i)}(x - y)$;
> 2. $\langle0|T\{\hat\phi(x)\hat\phi^\dagger(y)\}|0\rangle = D_F^{(m)}(x - y)$, $\langle0|T\{\hat\phi\hat\phi\}|0\rangle = \langle0|T\{\hat\phi^\dagger\hat\phi^\dagger\}|0\rangle = 0$ ([[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-2|Theorem §C6a.7.2]], 3), and $\langle0|T\{\hat\phi^{(\dagger)}(x)\hat\phi_j(y)\}|0\rangle = 0$;
> 3. Wick's theorem ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]) holds for any product of these fields, with the contraction of a pair equal to its value in 1–2:
>
> $$
> \overbracket{\hat\phi_i(x)\hat\phi_j(y)} = \delta_{ij}D_F^{(m_i)}(x - y), \qquad \overbracket{\hat\phi(x)\hat\phi^\dagger(y)} = D_F^{(m)}(x - y), \qquad \overbracket{\hat\phi(x)\hat\phi(y)} = \overbracket{\hat\phi^\dagger(x)\hat\phi^\dagger(y)} = 0 .
> $$
>
> So a diagram has one kind of line per field type: undirected for a real field, oriented from the $\hat\phi^\dagger$ end to the $\hat\phi$ end for a complex one, each carrying the $D_F$ of its own mass.
>
> *Model:* the free fields ([[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]] for each $\hat\phi_j$, [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]]); *applies:* free vacuum $|0\rangle$, exact; independent of the interaction in which the lines appear.
>
> *Source: Yu §6.3.1, eq. (6.166) (Wick's theorem for any set of fields $\Phi_a$); §6.4, eqs. (6.210), (6.222); §7.4, eq. (7.143) · PHY 513, Problem Set 8, Problem 4 (two fields $\Phi$, $\phi$) and Problem 1(b) (complex scalar) · proof written here*

^lem-c6a-12-1

> [!derivation]- Derivation
> **Step 1** (independent oscillators). The free Lagrangian is a sum, $\mathcal L_0 = \sum_j\bigl(\frac12(\partial\phi_j)^2 - \frac12m_j^2\phi_j^2\bigr) + \cdots$, so $\pi_j = \dot\phi_j$ and the equal-time relations of [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]] hold field by field, $[\hat\phi_i(\mathbf x), \hat\pi_j(\mathbf y)] = i\delta_{ij}\delta^3(\mathbf x - \mathbf y)$, $[\hat\phi_i, \hat\phi_j] = [\hat\pi_i, \hat\pi_j] = 0$. Mode by mode ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]):
>
> $$
> \hat\phi_j(x) = \int\frac{d^3p}{(2\pi)^3}\frac{\hat a_{j,\mathbf p}e^{-ip\cdot x} + \hat a^\dagger_{j,\mathbf p}e^{ip\cdot x}}{\sqrt{2E_{j,\mathbf p}}}, \qquad [\hat a_{i,\mathbf p}, \hat a^\dagger_{j,\mathbf q}] = \delta_{ij}(2\pi)^3\delta^3(\mathbf p - \mathbf q), \qquad [\hat a_{i,\mathbf p}, \hat a_{j,\mathbf q}] = 0 ,
> $$
>
> $E_{j,\mathbf p} = \sqrt{\mathbf p^2 + m_j^2}$, $p^0 = E_{j,\mathbf p}$; the complex field's $\hat a_{\mathbf p}$, $\hat b_{\mathbf p}$ ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]]) commute with all $\hat a_{j,\mathbf q}$, $\hat a^\dagger_{j,\mathbf q}$ for the same reason.
>
> **Step 2** (part 1). For $x^0 > y^0$, $\langle0|\hat\phi_i(x)$ keeps only the $\hat a_i$ term ($\langle0|\hat a^\dagger = 0$) and $\hat\phi_j(y)|0\rangle$ only the $\hat a_j^\dagger$ term:
>
> $$
> \langle0|\hat\phi_i(x)\hat\phi_j(y)|0\rangle = \int\frac{d^3p}{(2\pi)^3}\frac{d^3q}{(2\pi)^3}\frac{e^{-ip\cdot x}e^{iq\cdot y}}{\sqrt{2E_{i,\mathbf p}2E_{j,\mathbf q}}}\,\langle0|\hat a_{i,\mathbf p}\hat a^\dagger_{j,\mathbf q}|0\rangle = \delta_{ij}\int\frac{d^3p}{(2\pi)^3}\frac{e^{-ip\cdot(x - y)}}{2E_{i,\mathbf p}} = \delta_{ij}\,D_W^{(m_i)}(x - y) ,
> $$
>
> using $\langle0|\hat a_{i,\mathbf p}\hat a^\dagger_{j,\mathbf q}|0\rangle = \langle0|[\hat a_{i,\mathbf p}, \hat a^\dagger_{j,\mathbf q}]|0\rangle = \delta_{ij}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ and [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]]. The same for $y^0 > x^0$ with $x \leftrightarrow y$; with $\theta$'s, $\langle0|T\{\hat\phi_i(x)\hat\phi_j(y)\}|0\rangle = \delta_{ij}\bigl[\theta(x^0 - y^0)D_W^{(m_i)}(x - y) + \theta(y^0 - x^0)D_W^{(m_i)}(y - x)\bigr] = \delta_{ij}D_F^{(m_i)}(x - y)$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]).
>
> **Step 3** (part 2). The complex-field statements are [[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-2|Theorem §C6a.7.2]], 3 (Steps 5–6 of its derivation). For a complex and a real field, Step 2 with $\langle0|\hat a_{\mathbf p}\hat a^\dagger_{j,\mathbf q}|0\rangle = \langle0|\hat a^\dagger_{j,\mathbf q}\hat a_{\mathbf p}|0\rangle = 0$ and $\langle0|\hat b_{\mathbf p}\hat a^\dagger_{j,\mathbf q}|0\rangle = 0$ (commuting operators, Step 1) gives $0$ in both time orders.
>
> **Step 4** (part 3). The derivation of [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]] uses of the fields only: the split $\hat\phi = \hat\phi^+ + \hat\phi^-$ with $\hat\phi^+|0\rangle = 0 = \langle0|\hat\phi^-$, $[\hat\phi_a^-, \hat\phi_b^-] = 0$, and that $[\hat\phi_a^+(x), \hat\phi_b^-(y)]$ is a number equal to $\langle0|\hat\phi_a(x)\hat\phi_b(y)|0\rangle$ (Step 4 of [[§C6a.6 Wick's Theorem#^der-c6a-6-1|Derivation §C6a.6.1]]). All three hold for any pair of the fields here, by Step 1:
>
> $$
> [\hat\phi_i^+(x), \hat\phi_j^-(y)] = \int\frac{d^3p}{(2\pi)^3}\frac{d^3q}{(2\pi)^3}\frac{e^{-ip\cdot x}e^{iq\cdot y}}{\sqrt{2E_{i,\mathbf p}2E_{j,\mathbf q}}}[\hat a_{i,\mathbf p}, \hat a^\dagger_{j,\mathbf q}] = \delta_{ij}D_W^{(m_i)}(x - y) = \langle0|\hat\phi_i(x)\hat\phi_j(y)|0\rangle ,
> $$
>
> and likewise $[\hat\phi^+(x), \hat\phi^{\dagger-}(y)] = D_W^{(m)}(x - y)$ ($\hat a$ with $\hat a^\dagger$), $[\hat\phi^+(x), \hat\phi^-(y)] = 0$ ($\hat a$ with $\hat b^\dagger$), $[\hat\phi^{(\dagger)+}, \hat\phi_j^-] = 0$. So the induction of [[§C6a.6 Wick's Theorem#^der-c6a-6-2|Derivation §C6a.6.2]] runs unchanged, each contraction being the time-ordered vacuum value of its pair.
>
> **What the derivation shows.**
> - "One propagator per field type" is the independence of the mode operators of different fields; the zero of $\hat\phi\hat\phi$ is charge conservation ([[§C6a.7 Feynman Diagrams for Correlation Functions#^der-c6a-7-2|Derivation §C6a.7.2]], Step 5).
> - Nothing depends on the interaction: the line rules come from $\mathcal L_0$ alone (Yu p. 292, p. 296).

^der-c6a-12-1

*Uses:* [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]], [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]], [[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-2|Theorem §C6a.7.2]], [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]], [[§C6a.6 Wick's Theorem#^lem-c6a-6-1|Lemma §C6a.6.1]]

> [!definition] Definition §C6a.12.1: Vertex Data of a Polynomial Interaction
> Let the fields be as in [[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]] and
>
> $$
> \mathcal L_{\rm int} = -\sum_tg_t\,M_t , \qquad M_t = \prod_k\phi_k^{m_{t,k}} ,
> $$
>
> each $M_t$ a monomial without derivatives in the **field symbols** $k$ (a real field $\phi_j$; $\phi$ and $\phi^\dagger$ of a complex field), $g_t$ a real coupling. The **vertex data** of $\mathcal L_{\rm int}$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]]) are:
> 1. the kinds $K$ = the field symbols, with $k \smile k'$ iff their contraction is nonzero (Lemma §C6a.12.1): $\phi_j \smile \phi_j$, $\phi \smile \phi^\dagger$;
> 2. one vertex type $t$ per monomial, with $r_t = \sum_km_{t,k}$ legs, $m_{t,k}$ of them of kind $k$, drawn as a point where $r_t$ lines end;
> 3. an external field $\hat\phi_k(x)$ is an external point of kind $k$.
>
> | $\mathcal L_{\rm int}$ | kinds | legs of the vertex |
> |---|---|---|
> | $-\frac{\lambda}{4!}\phi^4$ | $\phi$ | $\phi\phi\phi\phi$ |
> | $-\frac{g}{3!}\phi^3 - \frac{\lambda}{4!}\phi^4$ | $\phi$ | $\phi\phi\phi$; $\phi\phi\phi\phi$ |
> | $-\mu\,\Phi\phi^2$ | $\Phi$, $\phi$ | $\Phi\phi\phi$ |
> | $-\frac\lambda4(\phi^\dagger\phi)^2$ | $\phi \smile \phi^\dagger$ | $\phi\phi\phi^\dagger\phi^\dagger$ |
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* any polynomial interaction without derivatives of real and complex scalar fields; combinatorial, every order.
>
> *Source: Yu §7.1, p. 266 (the three field operators of $\mathcal L_Y$ "correspond to the three line-ends at the vertex"), §7.2, p. 288 · PHY 513, Problem Set 8, Problems 1(b), 2, 4 (statements) · the user's note "Symmetry Factors and the Orbit–Stabilizer Theorem" (Oct 2026), §8 · made precise here*

^def-c6a-12-1

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-1|P6, step 1]]

> [!theorem] Theorem §C6a.12.2: Vertex Factors of a Polynomial Interaction
> Let $\mathcal L_{\rm int} = -\sum_tg_t\,M_t$, each $M_t$ a monomial without derivatives in fields of kinds $k$ ($\phi$, $\Phi$, or $\phi$ and $\phi^\dagger$ of a complex field), with $m_{t,k}$ factors of kind $k$ (the vertex data of [[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]]). Then:
> 1. the **vertex factor** of type $t$ is $i$ times the coefficient of $M_t$ in $\mathcal L_{\rm int}$ times the number of ways to attach distinct lines to its legs:
>
> $$
> -ig_t\prod_km_{t,k}! \qquad\text{(times } \textstyle\int d^4z \text{ in position space, } (2\pi)^4\delta^4(\sum p) \text{ in momentum space)} ;
> $$
>
> 2. every diagram enters with $\frac1S\prod_{\text{vertices}}(\text{vertex factor})$ and the rules for lines of [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-4|Theorem §C6a.8.4]] (several fields: [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-4|Theorem §C6a.12.4]]), $S$ its symmetry factor ([[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]]).
>
> In the notation of the fields themselves: a term $-c\prod_i\phi_i^{n_i}$ of $\mathcal L_{\rm int}$ ($\phi_i$ distinct field symbols) has the vertex factor $-ic\prod_in_i!$.
>
> | $\mathcal L_{\rm int}$ | legs | vertex factor |
> |---|---|---|
> | $-\frac{g}{3!}\phi^3$ (in [[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2\|Model §C6a.8.2]]) | $\phi\phi\phi$ | $-i\frac{g}{3!}\cdot3! = -ig$ |
> | $-\frac{\lambda}{4!}\phi^4$ ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1\|Model §C6a.1.1]]; [[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2\|Model §C6a.8.2]]) | $\phi\phi\phi\phi$ | $-i\lambda$ |
> | $-\mu\,\Phi\phi^2$ ([[§C6b.9 Decay Rates and Widths#^mod-c6b-9-6\|Model §C6b.9.6]]) | $\Phi\phi\phi$ | $-i\mu\cdot1!\cdot2! = -2i\mu$ |
> | $-\frac\lambda4(\phi^\dagger\phi)^2$ ([[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-3\|Model §C6a.8.3]]) | $\phi\phi\phi^\dagger\phi^\dagger$ | $-i\frac\lambda4\cdot2!\cdot2! = -i\lambda$ |
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* any polynomial interaction without derivatives, every order; combinatorial.
>
> *Source: PHY 513, Problem Set 8, statement of Problem 2 (vertices $-ig$, $-i\lambda$) and Problem 1(b) (vertex $-i\lambda$ for $\frac\lambda4(\phi^\dagger\phi)^2$); the user's solution of Problem 4 ($\mathcal M = -2\mu$, "each of $\hat a_{\mathbf p_1}, \hat a_{\mathbf p_2}$ … pairs with one of the two fields, in 2 ways") · PS §4.4, p. 93 ("the various placements of these contractions into $\phi\phi\phi\phi$ generates a factor of 4!") · proof written here*

^thm-c6a-12-2

> [!derivation]- Derivation
> **Step 1** (the Dyson term). Without derivatives $\hat{\mathcal H}_I = -\mathcal L_{\rm int}$, so with $n_t$ vertices of type $t$ the Dyson series contributes ($\frac{1}{n!}\binom{n}{n_1, n_2, \dots} = \prod_t\frac{1}{n_t!}$ for $n = \sum_tn_t$)
>
> $$
> \prod_t\frac{(-ig_t)^{n_t}}{n_t!}\int\prod_{t,v}d^4z_{t,v}\;\langle0|T\Bigl\{(\text{external fields})\prod_{t,v}M_t(z_{t,v})\Bigr\}|0\rangle .
> $$
>
> **Step 2** (one vertex, distinct lines). At one vertex of type $t$, let $\sum_km_{t,k}$ distinct lines (to different external points or other vertices) end on it, $m_{t,k}$ of them on legs of kind $k$. The contractions realizing this assign the lines of kind $k$ bijectively to the $m_{t,k}$ legs of kind $k$: $\prod_km_{t,k}!$ ways, all with the same integrand. So the vertex contributes $-ig_t\prod_km_{t,k}!$. Example $\mu\Phi\phi^2$ with lines to $\mathbf K$ ($\Phi$) and $\mathbf p_1$, $\mathbf p_2$ ($\phi$): $1!\cdot2! = 2$ ([[§C6b.9 Decay Rates and Widths#^ex-c6b-9-1|Example §C6b.9.1]], Step 4).
>
> *Real field* (cubic vertex at $z$, legs $\hat\phi_{z1}, \hat\phi_{z2}, \hat\phi_{z3}$, lines to distinct points $a$, $b$, $c$): the $3! = 6$ contractions are
>
> $$
> \sum_{\sigma\in S_3}\overbracket{\hat\phi_a\hat\phi_{z\sigma(1)}}\,\overbracket{\hat\phi_b\hat\phi_{z\sigma(2)}}\,\overbracket{\hat\phi_c\hat\phi_{z\sigma(3)}} , \qquad (\sigma(1)\sigma(2)\sigma(3)) \in \{123, 132, 213, 231, 312, 321\} ,
> $$
>
> each $D_F(a - z)D_F(b - z)D_F(c - z)$, so $-i\frac{g}{3!}\cdot3! = -ig$.
>
> *Complex field* ($(\phi^\dagger\phi)^2$ at $z$, legs $\hat\phi^\dagger_{z1}, \hat\phi^\dagger_{z2}, \hat\phi_{z1}, \hat\phi_{z2}$, lines to $\hat\phi(x_1)$, $\hat\phi(x_2)$, $\hat\phi^\dagger(y_1)$, $\hat\phi^\dagger(y_2)$): a $\hat\phi(x_i)$ contracts only with a $\hat\phi^\dagger_z$ leg and a $\hat\phi^\dagger(y_j)$ only with a $\hat\phi_z$ leg ([[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]], 2), so the attachments are $S_2\times S_2$, not $S_4$:
>
> $$
> \sum_{\sigma,\tau\in S_2}\overbracket{\hat\phi(x_1)\hat\phi^\dagger_{z\sigma(1)}}\,\overbracket{\hat\phi(x_2)\hat\phi^\dagger_{z\sigma(2)}}\,\overbracket{\hat\phi_{z\tau(1)}\hat\phi^\dagger(y_1)}\,\overbracket{\hat\phi_{z\tau(2)}\hat\phi^\dagger(y_2)} = 2!\,2!\;D_F(x_1 - z)D_F(x_2 - z)D_F(z - y_1)D_F(z - y_2) ,
> $$
>
> the four terms $(\sigma, \tau) = (e, e), (e, (12)), ((12), e), ((12), (12))$; with $-\frac{i\lambda}{4}$ the vertex factor is $-i\frac\lambda4\cdot2!\cdot2! = -i\lambda$. The other $4! - 4 = 20$ assignments of four lines to four legs pair a $\hat\phi$ with a $\hat\phi$ and vanish.
>
> **Step 3** (part 2). By [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 1–2, the contractions of one diagram number $N_D = |G|/S$ with $|G| = \prod_tn_t!\,\bigl(\prod_km_{t,k}!\bigr)^{n_t}$, all with the same integrand (Step 5 of [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]]):
>
> $$
> \prod_t\frac{(-ig_t)^{n_t}}{n_t!}\cdot\frac{|G|}{S} = \frac1S\prod_t\Bigl(-ig_t\prod_km_{t,k}!\Bigr)^{n_t} .
> $$
>
> For $\phi^4$, $g = \frac{\lambda}{4!}$: $\frac1S(-i\lambda)^n$, [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-1|Theorem §C6a.8.1]].
>
> **What the derivation shows.**
> - The $\frac{1}{3!}$, $\frac{1}{4!}$, $\frac14$ of the Lagrangians are chosen to cancel the attachment count; $\mu\Phi\phi^2$ is not normalized that way, hence the $2$.

^der-c6a-12-2

*Uses:* [[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]], [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-4|Theorem §C6a.8.4]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-2|P6, step 2]]

> [!theorem] Theorem §C6a.12.3: Counting Legs, Lines and Loops
> Let a diagram ([[§C6a.7 Feynman Diagrams for Correlation Functions#^def-c6a-7-1|Def. §C6a.7.1]]; vertex types of [[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]]) have $V$ vertices, vertex $v$ with $r_v$ legs, $E$ external points (or external particles), each joined by its line to a vertex, $I$ internal lines (both ends on legs of vertices; a loop at one vertex counts), and $C$ connected pieces (as a graph). Then
> 1. (legs) every leg ends one line, so
>
> $$
> \sum_vr_v = E + 2I , \qquad I = \frac12\Bigl(\sum_tn_tr_t - E\Bigr) \quad (n_t \text{ vertices of type } t) :
> $$
>
> the order $(n_t)$ and $E$ fix $I$ (no diagram if $\sum_tn_tr_t - E$ is odd or negative);
> 2. (loops) the number of independent loops is
>
> $$
> L = I - V + C ; \qquad L = I - V + 1 \ \text{(connected)}, \qquad I = V - 1 \ \text{(connected tree, } L = 0) ;
> $$
>
> 3. (connectedness) in a connected diagram with $V \ge 2$ every vertex has a leg on an internal line to another vertex, so it carries at most $r_v - 1$ external points. A vertex carrying all $r_v$ forms a piece of its own with its external points, and the $2I$ legs not on external points pair among the other vertices: the diagram is disconnected. A connected diagram with $V = 2$ and $I = 1$ has exactly $r_v - 1$ external points at each vertex.
>
> | order, process | $\sum_tn_tr_t$ | $E$ | $I$ | $L$ (connected) |
> |---|---|---|---|---|
> | $g^2$ (two cubic vertices), $2 \to 2$ | $6$ | $4$ | $1$ | $0$ |
> | $\lambda$ (one quartic vertex), $2 \to 2$ | $4$ | $4$ | $0$ | $0$ |
> | $g\lambda$, $2 \to 3$ | $7$ | $5$ | $1$ | $0$ |
> | $\lambda$, two-point (tadpole) | $4$ | $2$ | $1$ | $1$ |
> | $\lambda^2$, four-point (fish) | $8$ | $4$ | $2$ | $1$ |
>
> *Model:* any (combinatorics); *applies:* every diagram of a polynomial interaction, of correlation functions (external points) and of amplitudes (external particles) alike, any order; a line joining two external points directly is not covered (it is a piece of its own without vertex).
>
> *Source: PS §10.1, eq. (10.2) ($L = P_e + P_\gamma - V + 1$: "each propagator has a momentum integral, each vertex has a delta function, and one delta function merely enforces overall momentum conservation") and p. 321 (for $\phi^n$: "$L = P - V + 1$. There are $n$ lines meeting at each vertex, so $nV = N + 2P$") · PHY 513, Problem Set 8, Problem 2(a)–(b) (the user's solution: "Two cubic vertices have $6$ legs; $4$ are joined to the external lines, which leaves two legs and hence one internal line. If one vertex carried more than two external particles, the two remaining legs would sit on the same vertex and be contracted with each other, giving a disconnected diagram") · the user's PHY 513 notes, Lecture 16 update, §16.6, Derivation "From position space to momentum space", step 4 ("one $\int\frac{d^4q}{(2\pi)^4}$ per loop that is left undetermined, and one overall $(2\pi)^4\delta^4(\sum p)$") and §16.8 (two vertices, two propagators, one undetermined momentum) · proof written here*

^thm-c6a-12-3

> [!derivation]- Derivation
> **Step 1** (part 1, the legs). In a complete contraction every field is paired exactly once ([[§C6a.6 Wick's Theorem#^thm-c6a-6-3|Theorem §C6a.6.3]]), so every leg of a vertex is the end of exactly one line. Count the line-ends that sit on vertices: an external line has one (its other end is the external point), an internal line two (a loop at $v$ has both ends at $v$):
>
> $$
> \sum_vr_v = E\cdot1 + I\cdot2 , \qquad \sum_vr_v = \sum_tn_tr_t \quad\Longrightarrow\quad I = \frac12\Bigl(\sum_tn_tr_t - E\Bigr) .
> $$
>
> Two cubic vertices and four particles: $6 = 4 + 2I$, $I = 1$.
>
> **Step 2** (a tree has one edge fewer than nodes). Regard the diagram as a graph: nodes the $V$ vertices and the $E$ external points, edges the $I + E$ lines. A tree (connected, no cycle) with $N \ge 1$ nodes has $N - 1$ edges: for $N = 1$ none; for $N \ge 2$, a longest path ends at a node $u$ of degree $1$ (a second edge at $u$ would extend the path or close a cycle), and deleting $u$ and its edge leaves a tree with $N - 1$ nodes, so by induction $(N - 2) + 1 = N - 1$ edges.
>
> **Step 3** (part 2, independent loops). A connected piece with $N$ nodes and $M$ edges contains a spanning tree (delete edges lying on cycles one at a time until none is left; deleting an edge of a cycle keeps the piece connected), with $N - 1$ edges by Step 2. Each of the other $M - N + 1$ edges $e$ closes exactly one cycle $c_e$ with the tree (the tree path between its ends, plus $e$), and $c_e$ contains $e$ and no other non-tree edge, so these cycles are independent; this number is the number of momenta a connected piece leaves unfixed after momentum conservation at its vertices (Step 6 of [[§C6a.10 Feynman Rules in Momentum Space#^der-c6a-10-2|Derivation §C6a.10.2]]). Summing over the $C$ pieces, with $N = V + E$ and $M = I + E$ in total,
>
> $$
> L = \sum_{\text{pieces}}(M - N + 1) = (I + E) - (V + E) + C = I - V + C .
> $$
>
> For $C = 1$: $L = I - V + 1$; a tree has $L = 0$, so $I = V - 1$. The external points are leaves and drop out.
>
> **Step 4** (part 3, a vertex needs an internal line). Let the diagram be connected with $V \ge 2$, and take a vertex $v$ and another vertex $w$. A path from $v$ to $w$ leaves $v$ along a line whose other end is not an external point (an external point has a single line, so no path continues through it) and not $v$ itself (a loop returns to $v$): it ends at another vertex. So $v$ has a leg on an internal line, and at most $r_v - 1$ legs on external points.
>
> **Step 5** (part 3, the disconnected case). If $v$ carries $r_v$ external points, every leg of $v$ ends at an external point, and these have no other line: $v$ with its points is a connected piece, and the other vertices lie outside it, so the diagram is disconnected. The legs not on external points are then $\sum_{w \ne v}(r_w - e_w) = \sum_wr_w - E = 2I$ (Step 1), all at vertices $w \ne v$, and they pair among themselves. With two cubic vertices and four particles, three on $v_1$: one particle and $2I = 2$ legs on $v_2$, and the two legs close a loop at $v_2$, the piece "$v_2$ with a tadpole loop" beside "$v_1$ with three particles".
>
> **Step 6** (part 3, $V = 2$, $I = 1$). In a connected diagram the one internal line joins $v_1$ to $v_2$ (a loop at $v_1$ would leave $v_2$ with every leg on an external point, disconnected by Step 5). So each vertex has exactly one leg on the internal line and $r_v - 1$ on external points: the hypothesis of [[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-1|Theorem §C6b.3.1]] ($S = 1$).
>
> **What the derivation shows.**
> - The order and the number of external particles fix $I$ and, for a connected diagram, $L$: at order $g^2$ and $\lambda$ for $2 \to 2$ and at order $g\lambda$ for $2 \to 3$ every connected diagram is a tree, which is why Problem Set 8, Problem 2 had only trees, each with $S = 1$.
> - The count of loops is the count of free momentum integrals ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-5|Theorem §C6a.12.5]], 2); the external points, leaves of the graph, never close a loop.

^der-c6a-12-3

*Uses:* [[§C6a.7 Feynman Diagrams for Correlation Functions#^def-c6a-7-1|Def. §C6a.7.1]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]], [[§C6a.6 Wick's Theorem#^thm-c6a-6-3|Theorem §C6a.6.3]], [[§C6a.10 Feynman Rules in Momentum Space#^der-c6a-10-2|Derivation §C6a.10.2]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-3|P6, step 3]]

## The rules

> [!theorem] Theorem §C6a.12.4: Feynman Rules for a Polynomial Interaction in Position Space
> With the vertex data of [[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]], the numerator of the master formula with external fields $\hat\phi_{k_1}(x_1), \dots, \hat\phi_{k_r}(x_r)$,
>
> $$
> \langle0|T\Bigl\{\hat\phi_{k_1}(x_1)\cdots\hat\phi_{k_r}(x_r)\exp\Bigl[i\int d^4z\,\mathcal L_{\rm int}(\hat\phi_I(z))\Bigr]\Bigr\}|0\rangle ,
> $$
>
> is, as a formal power series in the $g_t$, the sum of all diagrams with these external points and any numbers $n_t$ of vertices of each type, each diagram the product of:
>
> | element | factor |
> |---|---|
> | line of the real field $\phi_j$ between $a$ and $b$ | $D_F^{(m_j)}(a - b)$ |
> | line of a complex field, arrow from $b$ ($\phi^\dagger$ end) to $a$ ($\phi$ end) | $D_F^{(m)}(a - b)$ |
> | vertex of type $t$ at $z$ | $\bigl(-ig_t\prod_km_{t,k}!\bigr)\int d^4z$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2\|Theorem §C6a.12.2]]) |
> | external point | $1$ |
> | the whole diagram | $\frac1S$, $S = \lvert\operatorname{Stab}(P)\rvert$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2\|Def. §CA.8.2]]) |
>
> A line joins two line-ends of compatible kinds: two ends of the same real field, or the $\phi$ end and the $\phi^\dagger$ end of one complex field; at a vertex of type $t$, $m_{t,k}$ lines end on legs of kind $k$. For a complex field two arrows meet head to tail at each $\phi^\dagger\phi$ pair of legs, so charge flows through every vertex of $(\phi^\dagger\phi)^2$.
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* as in the opening: the numerator, all orders as a formal power series, in $|0\rangle$; each line is the free-field, free-vacuum propagator ([[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]]); for $\phi^4$ it is [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-4|Theorem §C6a.8.4]].
>
> *Source: PS §4.4, p. 94 (rules 1–4 for $\phi^4$); §4.6, p. 114 · Yu §7.1, eqs. (7.25)–(7.28), (7.40)–(7.41) (position-space rules); §7.3, eq. (7.120); §7.4, eq. (7.143) · PHY 513, Problem Set 8, Problems 1(b), 2(c) (the user's "$|G|$ is again the inverse of the prefactor") · the user's note "Symmetry Factors and the Orbit–Stabilizer Theorem" (Oct 2026), §8 · proof written here, generalizing [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]]*

^thm-c6a-12-4

> [!derivation]- Derivation
> **Step 1** (the Dyson term). $\hat{\mathcal H}_I = \sum_tg_tM_t(\hat\phi_I)$, so $-i\int dt\,\hat H_I = \sum_t(-ig_t)\int d^4z\,M_t(\hat\phi_I(z))$ ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]]). Expanding the exponential of a sum of commuting terms inside $T$ and collecting $n_t$ factors of type $t$ ($n = \sum_tn_t$; the multinomial coefficient $\frac{n!}{\prod_tn_t!}$ counts the orders in which the types occur):
>
> $$
> \frac{1}{n!}\Bigl(\sum_t(-ig_t)\int M_t\Bigr)^n = \sum_{\sum n_t = n}\frac{1}{n!}\frac{n!}{\prod_tn_t!}\prod_t\Bigl((-ig_t)\int M_t\Bigr)^{n_t} = \sum_{\sum n_t = n}\prod_t\frac{(-ig_t)^{n_t}}{n_t!}\int\prod_{t,v}d^4z_{t,v}\,\prod_{t,v}M_t(\hat\phi_I(z_{t,v})) .
> $$
>
> **Step 2** (Wick with kinds). Write each $M_t(z_{t,v})$ as its $r_t$ factors, one field per leg $(t, v, a)$ of kind $\kappa_t(a)$. By [[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]], 3, and [[§C6a.6 Wick's Theorem#^thm-c6a-6-3|Theorem §C6a.6.3]], the vacuum value is the sum over complete pairings of all half-edges, a pair of incompatible kinds giving $0$: only $P \in \mathcal P_\smile(X_{E,\mathbf n})$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]]) survive,
>
> $$
> \langle0|T\Bigl\{\prod_{h\in X_{E,\mathbf n}}\hat\phi_h\Bigr\}|0\rangle = \sum_{P\in\mathcal P_\smile(X_{E,\mathbf n})}\;\prod_{\{h,h'\}\in P}\overbracket{\hat\phi_h\hat\phi_{h'}} .
> $$
>
> Example: $\Phi\phi^2$ at first order with external fields $\hat\phi(x)$, $\hat\phi(y)$, $\hat\Phi(w)$ and the legs $\hat\Phi_z$, $\hat\phi_{z_1}$, $\hat\phi_{z_2}$ of one vertex at $z$. $\hat\Phi(w)$ can only pair with $\hat\Phi_z$; the four $\phi$-kind fields have $3!! = 3$ pairings:
>
> $$
> \begin{aligned}
> \langle0|T\{\hat\phi(x)\hat\phi(y)\hat\Phi(w)\,\hat\Phi_z\hat\phi_{z_1}\hat\phi_{z_2}\}|0\rangle ={}& \overbracket{\hat\Phi(w)\hat\Phi_z}\Bigl[\overbracket{\hat\phi(x)\hat\phi_{z_1}}\,\overbracket{\hat\phi(y)\hat\phi_{z_2}} + \overbracket{\hat\phi(x)\hat\phi_{z_2}}\,\overbracket{\hat\phi(y)\hat\phi_{z_1}} + \overbracket{\hat\phi(x)\hat\phi(y)}\,\overbracket{\hat\phi_{z_1}\hat\phi_{z_2}}\Bigr]\\
> ={}& D_F^{(M)}(w - z)\bigl[2\,D_F^{(m)}(x - z)D_F^{(m)}(y - z) + D_F^{(m)}(x - y)D_F^{(m)}(0)\bigr] ,
> \end{aligned}
> $$
>
> and the pairings $\{\hat\Phi(w), \hat\phi_{z_a}\}$ are absent because $\overbracket{\hat\Phi\hat\phi} = 0$.
>
> **Step 3** (invariance). Let $g \in G_{\mathbf n}$ permute the vertices within each type and, at each vertex, the legs of each kind among themselves. All legs of one kind at $z_{t,v}$ carry the same operator $\hat\phi_k(z_{t,v})$, so as in Step 5 of [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]] the integrand of $g\cdot P$ is that of $P$ with the variables $z_{t,v}$ renamed within each type, and $\int\prod d^4z$ is unchanged (block permutation, $|\det| = 1$, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]). For a complex line the renaming keeps the order $D_F(\phi\text{ end} - \phi^\dagger\text{ end})$, since $g$ preserves kinds.
>
> **Step 4** (orbits). By [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 1–2, the pairings of one diagram $D$ number $N_D = |G_{\mathbf n}|/S(D)$, with $|G_{\mathbf n}| = \prod_tn_t!\,\bigl(\prod_km_{t,k}!\bigr)^{n_t}$, all with the same integral $I(D)$.
>
> **Step 5** (cancel). Steps 1–4:
>
> $$
> \prod_t\frac{(-ig_t)^{n_t}}{n_t!}\sum_D\frac{\prod_tn_t!\,\bigl(\prod_km_{t,k}!\bigr)^{n_t}}{S(D)}\,I(D) = \sum_D\frac{1}{S(D)}\prod_t\Bigl(-ig_t\prod_km_{t,k}!\Bigr)^{n_t}I(D) ,
> $$
>
> each vertex carrying the factor of [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]] and $\int d^4z$, each line its contraction from [[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]], each external point nothing (it is not integrated). In the example of Step 2, $|G_1| = 1!\,(1!\,2!) = 2$: the first diagram has $N = 2$, $S = 1$, value $(-2i\mu)\int d^4z\,D_F^{(M)}(w - z)D_F^{(m)}(x - z)D_F^{(m)}(y - z)$; the second $N = 1$, $S = 2$, value $\frac{-2i\mu}{2}\int d^4z\,D_F^{(M)}(w - z)D_F^{(m)}(x - y)D_F^{(m)}(0)$, matching $-i\mu\cdot2$ and $-i\mu\cdot1$ of Step 2.
>
> **Step 6** (sum). Summing over all $(n_t)$ lists each diagram once, its vertex numbers being part of it (Step 3 of [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-4|Derivation §C6a.8.4]]).
>
> **What the derivation shows.**
> - What changes from $\phi^4$: the propagator of each line depends on its field, pairings are restricted by kinds, and $n!\,(4!)^n$ becomes $|G_{\mathbf n}|$; the cancellation of Step 5 is complete for vertices exactly when the Lagrangian carries $\frac{1}{\prod_km_{t,k}!}$, which is why $\frac{g}{3!}$, $\frac{\lambda}{4!}$, $\frac\lambda4 = \frac{\lambda}{2!\,2!}$ are chosen and $\mu\Phi\phi^2$ gives $-2i\mu$.
> - Kinds make $S$ smaller: a symmetry must map each leg to a leg of the same kind ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 3), so oriented loops cannot be flipped ([[§C6a.9 Symmetry Factors in Practice#^thm-c6a-9-2|Theorem §C6a.9.2]]).

^der-c6a-12-4

*Uses:* [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]], [[§C6a.6 Wick's Theorem#^thm-c6a-6-3|Theorem §C6a.6.3]], [[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]

*Procedure:* [[P5 Symmetry Factor of a Diagram#^p5-1|P5, steps 1–2]]

> [!theorem] Theorem §C6a.12.5: Feynman Rules for a Polynomial Interaction in Momentum Space
> Each diagram of [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-4|Theorem §C6a.12.4]] equals the following expression:
>
> | element | factor |
> |---|---|
> | line of a field of mass $m_j$, momentum $p$ | $\dfrac{i}{p^2 - m_j^2 + i\varepsilon}$ |
> | vertex of type $t$ | $-ig_t\prod_km_{t,k}!$ |
> | external point $x$, momentum $p$ entering the diagram at $x$ | $e^{-ip\cdot x}$ |
>
> 1. at each vertex the momenta of its $r_t$ lines are conserved, a factor $(2\pi)^4\delta^4(\sum p_{\rm in} - \sum p_{\rm out})$; the direction assigned to a momentum is arbitrary, also on an oriented line (its value is even in $p$);
> 2. every momentum not fixed by conservation is integrated with $\int\frac{d^4p}{(2\pi)^4}$: in each connected piece with $V$ vertices, $I$ internal lines and $r \ge 1$ external points, $L = I - V + 1$ loop momenta ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 2) and $r - 1$ external ones;
> 3. the result is divided by $S$.
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* as in the opening; each line is the free-field $\tilde D_F$ of its own mass ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]); for $\phi^4$ it is [[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-2|Theorem §C6a.10.2]].
>
> *Source: PS §4.4, p. 95 (rules 1–6 for $\phi^4$) · Yu §7.2, rules 6–11 (pp. 287–288); §7.3, p. 296; §7.4, rules 1–5 (p. 300; complex scalar lines, the momentum drawn along the arrow) · proof written here, generalizing [[§C6a.10 Feynman Rules in Momentum Space#^der-c6a-10-2|Derivation §C6a.10.2]]*

^thm-c6a-12-5

> [!derivation]- Derivation
> **Step 1** (each line in Fourier form). By [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]] with the mass of the line, for a line $\ell$ from $a_\ell$ to $b_\ell$,
>
> $$
> D_F^{(m_\ell)}(a_\ell - b_\ell) = \int\frac{d^4p_\ell}{(2\pi)^4}\,\frac{i}{p_\ell^2 - m_\ell^2 + i\varepsilon}\,e^{-ip_\ell\cdot a_\ell}e^{+ip_\ell\cdot b_\ell} .
> $$
>
> For a complex line $a_\ell$ is its $\phi$ end; reversing the momentum, $p_\ell \to -p_\ell$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1), gives the same integrand with $e^{+ip_\ell\cdot a_\ell}e^{-ip_\ell\cdot b_\ell}$ because $(-p)^2 = p^2$: the momentum may be taken along the arrow or against it.
>
> **Step 2** (one vertex). At a vertex $z$ of type $t$, with the momenta $p_1, \dots, p_{r_t}$ of its lines oriented into $z$, the $z$-dependence is $\prod_{a=1}^{r_t}e^{ip_a\cdot z}$ (a loop at $z$ contributes $e^{ik\cdot z}e^{-ik\cdot z} = 1$), and with [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] (integral done first, as in Step 3 of [[§C6a.10 Feynman Rules in Momentum Space#^der-c6a-10-1|Derivation §C6a.10.1]])
>
> $$
> \Bigl(-ig_t\prod_km_{t,k}!\Bigr)\int d^4z\,e^{i(p_1 + \cdots + p_{r_t})\cdot z} = \Bigl(-ig_t\prod_km_{t,k}!\Bigr)(2\pi)^4\delta^4(p_1 + \cdots + p_{r_t}) .
> $$
>
> For $r_t = 3$ (cubic, $\Phi\phi^2$): $(2\pi)^4\delta^4(p_1 + p_2 + p_3)$; for $r_t = 4$: [[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-1|Theorem §C6a.10.1]].
>
> **Step 3** (count the integrals). Each delta does one momentum integral, its $(2\pi)^4$ cancelling that integral's $(2\pi)^{-4}$. In a connected piece with $V = \sum_tn_t$ vertices, $I$ internal lines and $r \ge 1$ external points, the $V$ deltas are independent (Step 6 of [[§C6a.10 Feynman Rules in Momentum Space#^der-c6a-10-2|Derivation §C6a.10.2]]; it used no valence), so of the $I + r$ line momenta
>
> $$
> (I + r) - V = (I - V + 1) + (r - 1) = L + (r - 1)
> $$
>
> remain, $L = M - N + 1$ the number of independent cycles of a graph with $N = V + r$ nodes and $M = I + r$ edges ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 2, Step 3 of its derivation). For the cubic exchange line between two vertices with two external points each ($V = 2$, $I = 1$, $r = 4$): $L = 0$, three integrals, the external momenta but one.
>
> **Step 4** (external points, $S$). As Steps 5 and 7 of [[§C6a.10 Feynman Rules in Momentum Space#^der-c6a-10-2|Derivation §C6a.10.2]]: the plane wave $e^{-ip\cdot x}$ stays at each external point, and $\frac1S$ is a number.
>
> **What the derivation shows.**
> - Only the valence of a vertex and the mass of a line enter; the vertex delta is translation invariance, whatever the monomial.

^der-c6a-12-5

*Uses:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C6a.10 Feynman Rules in Momentum Space#^der-c6a-10-1|Derivation §C6a.10.1]], [[§C6a.10 Feynman Rules in Momentum Space#^der-c6a-10-2|Derivation §C6a.10.2]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-4|Theorem §C6a.12.4]]

![[ph-qft-c6a-12-1.svg]]
*The rules of [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-4|Theorem §C6a.12.4]] and [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-5|Theorem §C6a.12.5]] as a picture. Top: the lines, one per field type (solid $\phi$, dashed $\Phi$, arrowed for a complex field, from the $\phi^\dagger$ end to the $\phi$ end), with their position- and momentum-space values. Bottom: the vertices of the four theories of C6, each $-i$ times its coupling times the number of ways to attach distinct lines to its legs. Added figure.*

## Examples

The examples of Problem Set 8 are already worked: the oriented tadpole, fish and sunset in [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-7|Example §C6a.9.7]] (with [[§C6a.9 Symmetry Factors in Practice#^thm-c6a-9-2|Theorem §C6a.9.2]]), and the cubic–quartic scattering diagrams in [[§C6b.3 Feynman Rules for Amplitudes#^ex-c6b-3-1|Example §C6b.3.1]] and [[§C6b.3 Feynman Rules for Amplitudes#^ex-c6b-3-2|Example §C6b.3.2]]. The two below are correlation functions not computed there.

> [!example] Example §C6a.12.1: The Cubic–Quartic Two-Point Function at Order g²
> ![[ph-qft-c6a-12-2.svg]]
>
> In [[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2|Model §C6a.8.2]], with $D_{ab} \equiv D_F(a - b)$ and the vertices at $z_1$, $z_2$, the order-$g^2$ term of $\langle0|T\{\hat\phi_I(x)\hat\phi_I(y)\,e^{-i\int\hat H_I}\}|0\rangle$ is
>
> $$
> (-ig)^2\int d^4z_1\,d^4z_2\Bigl[\frac12D_{xz_1}D_{z_1z_2}^2D_{z_2y} + \frac12D_{xz_1}D_{yz_1}D_{z_1z_2}D_{z_2z_2} + \frac14D_{xz_1}D_{z_1z_1}D_{yz_2}D_{z_2z_2} + D_{xy}\Bigl(\frac18D_{z_1z_1}D_{z_1z_2}D_{z_2z_2} + \frac{1}{12}D_{z_1z_2}^3\Bigr)\Bigr] :
> $$
>
> the bubble ($S = 2$), the tadpole on the line ($S = 2$), two one-point tadpoles ($S = 4$), and the free line times the dumbbell ($S = 8$) and the theta ($S = 12$). At order $g$ the two-point function has no term (five fields, odd); the vertex factor is $-i\frac{g}{3!}\cdot3! = -ig$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]).
>
> **Step 1** (Dyson term). One vertex type, $n_3 = 2$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-4|Theorem §C6a.12.4]], Step 1), with $\hat\phi_{ia} \equiv \hat\phi_I(z_i)$, $a = 1, 2, 3$:
>
> $$
> \frac{1}{2!}\Bigl(\frac{-ig}{3!}\Bigr)^2\int d^4z_1\,d^4z_2\,\langle0|T\{\hat\phi_x\hat\phi_y\,\hat\phi_{11}\hat\phi_{12}\hat\phi_{13}\,\hat\phi_{21}\hat\phi_{22}\hat\phi_{23}\}|0\rangle = \frac{(-ig)^2}{72}\int d^4z_1\,d^4z_2\sum_P(\cdots) ,
> $$
>
> eight fields, $7!! = 105$ complete pairings ([[§C6a.6 Wick's Theorem#^thm-c6a-6-3|Theorem §C6a.6.3]]).
>
> **Step 2** (classify by the partners of $\hat\phi_x$ and $\hat\phi_y$). Three classes:
> - (A) both to one vertex: the vertex ($2$), the leg of $x$ ($3$), the leg of $y$ ($2$): $12$ ways. The remaining leg $c$ of that vertex and the three legs of the other give $3$ pairings, each $\{c, \text{one leg}\}$ plus the other two legs paired; e.g. for $x \to 11$, $y \to 12$:
>
> $$
> \overbracket{\hat\phi_x\hat\phi_{11}}\,\overbracket{\hat\phi_y\hat\phi_{12}}\Bigl[\overbracket{\hat\phi_{13}\hat\phi_{21}}\,\overbracket{\hat\phi_{22}\hat\phi_{23}} + \overbracket{\hat\phi_{13}\hat\phi_{22}}\,\overbracket{\hat\phi_{21}\hat\phi_{23}} + \overbracket{\hat\phi_{13}\hat\phi_{23}}\,\overbracket{\hat\phi_{21}\hat\phi_{22}}\Bigr] = 3\,D_{xz_1}D_{yz_1}D_{z_1z_2}D_{z_2z_2} .
> $$
>
> Tadpole on the line: $12\cdot3 = 36$ pairings.
> - (B) to different vertices: which vertex takes $x$ ($2$), the legs of $x$ and $y$ ($3\cdot3$): $18$ ways. Two legs $a_1, a_2$ remain at the vertex of $x$ and $b_1, b_2$ at the other; their $3$ pairings, e.g. for $x \to 11$, $y \to 21$:
>
> $$
> \overbracket{\hat\phi_{12}\hat\phi_{22}}\,\overbracket{\hat\phi_{13}\hat\phi_{23}} + \overbracket{\hat\phi_{12}\hat\phi_{23}}\,\overbracket{\hat\phi_{13}\hat\phi_{22}} + \overbracket{\hat\phi_{12}\hat\phi_{13}}\,\overbracket{\hat\phi_{22}\hat\phi_{23}} = 2D_{z_1z_2}^2 + D_{z_1z_1}D_{z_2z_2} .
> $$
>
> Bubble: $18\cdot2 = 36$ pairings; two one-point tadpoles: $18\cdot1 = 18$.
> - (C) $\overbracket{\hat\phi_x\hat\phi_y}$: the six legs have $5!! = 15$ pairings; all three lines between the vertices, $3! = 6$ (the legs of $z_2$ matched to $11, 12, 13$); one loop at each vertex and one line, $3\cdot3 = 9$ (the leg of each vertex on the line). Theta $6$, dumbbell $9$.
>
> Check: $36 + 36 + 18 + 15 = 105$.
>
> **Step 3** (coefficients). $\frac{N_D}{72}$ with $|G_2| = 2!\,(3!)^2 = 72$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 1): $\frac{36}{72} = \frac12$, $\frac{36}{72} = \frac12$, $\frac{18}{72} = \frac14$, $\frac{9}{72} = \frac18$, $\frac{6}{72} = \frac{1}{12}$, so $S = 2, 2, 4, 8, 12$, the statement.
>
> **Step 4** (the same $S$ as stabilizers). Bubble: exchange of the two parallel lines, $|\operatorname{Stab}| = 2$. Tadpole on the line: flip of the loop, $2$. Two one-point tadpoles: the two flips, $2\cdot2 = 4$ (the vertices carry different external points and are not exchanged). Dumbbell: two flips and the exchange of the vertices, $2\cdot2\cdot2 = 8$. Theta: the $3!$ permutations of the three lines and the exchange of the vertices, $6\cdot2 = 12$. The same orbit–stabilizer count as [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-2|Example §C6a.9.2]] for $\phi^4$.
>
> *Source: written here from [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-4|Theorem §C6a.12.4]]; checked by enumeration (`qft-C/tools/step3/check_step3.py`: $105$ pairings, orbits $36, 36, 18, 9, 6$)*

^ex-c6a-12-1

> [!example] Example §C6a.12.2: The Complex Four-Point Function at First Order
> ![[ph-qft-c6a-12-3.svg]]
>
> In [[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-3|Model §C6a.8.3]], with $D_{ab} \equiv D_F(a - b)$, the numerator for $\hat\phi(x_1)\hat\phi(x_2)\hat\phi^\dagger(y_1)\hat\phi^\dagger(y_2)$ is, through order $\lambda$,
>
> $$
> \begin{aligned}
> &D_{x_1y_1}D_{x_2y_2} + D_{x_1y_2}D_{x_2y_1}\\
> &+ (-i\lambda)\int d^4z\Bigl[D_{x_1z}D_{x_2z}D_{zy_1}D_{zy_2} + \sum_{(i,j)}D_{x_iy_j}\,D_{x_{i'}z}D_{zz}D_{zy_{j'}} + \frac12\bigl(D_{x_1y_1}D_{x_2y_2} + D_{x_1y_2}D_{x_2y_1}\bigr)D_{zz}^2\Bigr] ,
> \end{aligned}
> $$
>
> the sum over the four pairs $(i, j)$, with $i'$, $j'$ the other indices: the vertex with two arrows in (from $y_1$, $y_2$) and two out (to $x_1$, $x_2$), $S = 1$; a line times an oriented tadpole, $S = 1$; two lines times the figure-eight, $S = 2$.
>
> **Step 1** (zeroth order). Only $\hat\phi\hat\phi^\dagger$ pairs contract ([[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]], 2): each $\hat\phi(x_i)$ with a different $\hat\phi^\dagger(y_j)$, $2! = 2$ pairings, not $3!! = 3$ as for a real field:
>
> $$
> \overbracket{\hat\phi(x_1)\hat\phi^\dagger(y_1)}\,\overbracket{\hat\phi(x_2)\hat\phi^\dagger(y_2)} + \overbracket{\hat\phi(x_1)\hat\phi^\dagger(y_2)}\,\overbracket{\hat\phi(x_2)\hat\phi^\dagger(y_1)} = D_{x_1y_1}D_{x_2y_2} + D_{x_1y_2}D_{x_2y_1} .
> $$
>
> **Step 2** (first order). $-i\int dt\,\hat H_I = \frac{-i\lambda}{4}\int d^4z\,\hat\phi^\dagger_{z1}\hat\phi^\dagger_{z2}\hat\phi_{z1}\hat\phi_{z2}$, all at $z$. The four $\hat\phi$'s ($x_1, x_2, z1, z2$) are matched bijectively to the four $\hat\phi^\dagger$'s ($y_1, y_2, z1^\dagger, z2^\dagger$): $4! = 24$ pairings, in three classes.
> - (a) $\hat\phi(x_1)$, $\hat\phi(x_2)$ to the two $\hat\phi^\dagger_z$ ($2$ ways), $\hat\phi^\dagger(y_1)$, $\hat\phi^\dagger(y_2)$ to the two $\hat\phi_z$ ($2$ ways):
>
> $$
> \sum_{\sigma,\tau\in S_2}\overbracket{\hat\phi(x_1)\hat\phi^\dagger_{z\sigma(1)}}\,\overbracket{\hat\phi(x_2)\hat\phi^\dagger_{z\sigma(2)}}\,\overbracket{\hat\phi_{z\tau(1)}\hat\phi^\dagger(y_1)}\,\overbracket{\hat\phi_{z\tau(2)}\hat\phi^\dagger(y_2)} = 4\,D_{x_1z}D_{x_2z}D_{zy_1}D_{zy_2} .
> $$
>
> - (b) one direct line $\overbracket{\hat\phi(x_i)\hat\phi^\dagger(y_j)}$ ($4$ choices of $(i, j)$), the other $\hat\phi(x_{i'})$ to a $\hat\phi^\dagger_z$ ($2$), $\hat\phi^\dagger(y_{j'})$ to a $\hat\phi_z$ ($2$), the last $\hat\phi_z$ with the last $\hat\phi^\dagger_z$ ($1$): $4$ each, $16$ in all, each $D_{x_iy_j}D_{x_{i'}z}D_{zz}D_{zy_{j'}}$.
> - (c) both external pairs direct (the $2$ terms of Step 1), and the vertex closed on itself, $\overbracket{\hat\phi_{z1}\hat\phi^\dagger_{z1}}\,\overbracket{\hat\phi_{z2}\hat\phi^\dagger_{z2}} + \overbracket{\hat\phi_{z1}\hat\phi^\dagger_{z2}}\,\overbracket{\hat\phi_{z2}\hat\phi^\dagger_{z1}} = 2D_{zz}^2$: $2\cdot2 = 4$.
>
> Check: $4 + 16 + 4 = 24$.
>
> **Step 3** (coefficients). With $\frac{-i\lambda}{4} = \frac{-i\lambda}{2!\,2!}$: (a) $\frac{4}{4} = 1$, (b) $\frac44 = 1$, (c) $\frac24 = \frac12$. $|G_1| = 2!\,2! = 4$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 1), so $S = 4/N_D = 1, 1, 2$.
>
> **Step 4** (stabilizers). (a), (b): every leg of the vertex is joined to an external point or, in (b), the loop joins the remaining $\hat\phi$ leg to the remaining $\hat\phi^\dagger$ leg; a symmetry fixes legs joined to external points ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 3), and the loop's two ends have different kinds, so it cannot be flipped: $S = 1$ (the real $\phi^4$ tadpole has $S = 2$). (c): exchanging the two $\hat\phi$ legs together with the two $\hat\phi^\dagger$ legs maps the pairing $\{\{z1, z1^\dagger\}, \{z2, z2^\dagger\}\}$ to itself: $S = 2$ (the real figure-eight has $S = 8$).
>
> The connected part, $-i\lambda\int d^4z\,D_{x_1z}D_{x_2z}D_{zy_1}D_{zy_2}$, shows the vertex factor $-i\frac\lambda4\cdot2!\cdot2! = -i\lambda$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]).
>
> *Source: written here from [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-4|Theorem §C6a.12.4]]; checked by enumeration (`qft-C/tools/step3/check_step3.py`: $24$ pairings in $7$ diagrams, orbits $4$ (five times) and $2$ (twice))*

^ex-c6a-12-2

> [!remark] Remark: Yu's route
> Yu derives the rules from $T$-matrix elements, theory by theory: for Yukawa theory the vertex is $\mathcal L_Y = -\kappa\phi\bar\psi\psi$ with the field operators stripped, times $i$ (p. 288); for $\phi^4$ one also multiplies by the $4!$ permutations of the four identical fields (p. 296, after the boxed rules); the line rules "are fixed by the free part of the Lagrangian and do not depend on the interaction" (p. 292), and §7.4 lists them for complex scalars (eqs. (7.135)–(7.143), momentum-space rules 1–5, p. 300) and vectors. This section states the vertex rule once for every monomial and derives the line rules and the $\frac1S$ from Wick's theorem with kinds, for correlation functions; the $S$-matrix form is [[§C6b.3 Feynman Rules for Amplitudes|§C6b.3]].
>
> *Source: Yu §7.2, pp. 287–288; §7.3, pp. 292, 296; §7.4, pp. 296–300*

^rem-c6a-12-1

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]] — a contraction pattern with several vertex types and several kinds of legs is a pairing of half-edges that respects a compatibility relation between kinds.
> - [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]] — the relabelling group, its order, and orbit–stabilizer for it.
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] — the plane waves meeting at a vertex integrate to a delta function.

> [!remark]- Connections
> - The prefactor of the Dyson series is the inverse order of the relabelling group exactly when the Lagrangian is normalized with the factorials of its legs; this is the content of "divide by $S$" for every theory — [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], [[§C6a.8 Position-Space Feynman Rules#^rem-c6a-8-2|§C6a.8, Remark: The same proof for other vertices]].
> - Fewer kinds of legs that can be exchanged means smaller symmetry factors; for QED the leg group is trivial and $S = 1$ for every diagram with external points — [[§C6a.9 Symmetry Factors in Practice#^cau-c6a-9-2|§C6a.9, Caution: "In QED the symmetry factor is always S = 1" holds for diagrams with external points]].
> - The line rules depend only on $\mathcal L_0$, the vertex rules only on $\mathcal L_{\rm int}$; Dirac and vector lines replace $D_F$ by $S_F$ and the vector propagator (QFT C7, planned) — [[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-2|Theorem §C6a.7.2]].
> - The same vertex factors and lines, with external particles instead of external points, give the Feynman rules for $i\mathcal M$ — [[§C6b.3 Feynman Rules for Amplitudes|§C6b.3]].
