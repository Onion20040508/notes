---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6a
section: C6a.12
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6a.11 The iε Limit and Vacuum Bubbles]] · ↑ [[· C6a Interactions and Correlation Functions]] · [[§C6a.13 Feynman Rules for Polynomial Interactions]] →

*Sources: Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.4, p. 98, the exponential of the vacuum diagrams (equation before (4.54)) and eqs. (4.55)–(4.56) · the user's PHY 513 notes, Ch. 14 §14.7 ("the bubbles exponentiate") · PHY 513, Problem Set 8, Problem 3(c) (exponentiation of a vacuum series) · Yu Zhao-Huan, 量子场论讲义, §7.1, p. 286, after eq. (7.103) (the bubble diagrams contribute only a phase factor); §10.4, eq. (10.178).*

[[§C6a.11 The iε Limit and Vacuum Bubbles|§C6a.11]] removed the vacuum bubbles: the denominator of the master formula ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-6|Theorem §C6a.4.6]]) is the sum of the diagrams with no external points ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-2|Theorem §C6a.11.2]]), each proportional to the volume of spacetime ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]]), and it cancels against the same factor of the numerator ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-5|Theorem §C6a.11.5]]). What do the cancelled diagrams mean? PS go back to them once they are gone ("we might pause a moment to go back and interpret them physically", p. 98), and this section follows. The sum of all vacuum diagrams is the exponential of the connected ones; comparing its dependence on $T$ with the vacuum projection of [[§C6a.4 The Interacting Vacuum and the Two-Point Function|§C6a.4]] ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-4|Theorem §C6a.4.4]]) identifies the sum of the connected bubbles with $-iE_0\cdot2T$: the bubbles are the energy density of the interacting vacuum. At first order this is [[§C6a.11 The iε Limit and Vacuum Bubbles#^ex-c6a-11-2|Example §C6a.11.2]]. The exponential form is PS's; Problem Set 8, Problem 3(c) used the same mechanism for a classical source ([[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-3|Theorem §C6c.7.3]]); Yu states that the bubbles contribute a phase factor (Remark: Yu's route, below). **Setup** ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]], an instance of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]): as in [[§C6a.11 The iε Limit and Vacuum Bubbles|§C6a.11]], the expansion in $\lambda$ of the denominator of the master formula, a free-vacuum value $\langle0|T\{\cdots\}|0\rangle$; identities hold order by order, as formal power series.

*Conventions* ([[Larsen PHY 513]]): as in [[§C6a.11 The iε Limit and Vacuum Bubbles|§C6a.11]]: $V$ is the volume of space and $2T$ the length of the time interval, both taken finite and then large (a box, [[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]]); $V_i$ (with an index) is a connected vacuum diagram and its value, with its own $\frac{1}{S(V_i)}$, not a volume; $E_0$ is the ground-state energy of $\hat H$ measured from $\hat H_0|0\rangle = 0$ ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^def-c6a-4-1|Def. §C6a.4.1]]; not the zero-point energy, [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^cau-c6a-4-1|§C6a.4, Caution: Two E₀'s]]).

The exponential formula ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-3|Theorem §CA.8.3]]) and the passage from pairings to diagrams ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-7|Theorem §CA.7.7]]) are proved in CA and listed at the end.

## The bubbles exponentiate; the vacuum energy density

> [!theorem] Theorem §C6a.12.1: The Denominator Is the Exponential of the Connected Vacuum Bubbles
> As formal power series in $\lambda$,
>
> $$
> \langle0|T\Bigl\{\exp\Bigl[-i\int_{-T}^Tdt\,\hat H_I(t)\Bigr]\Bigr\}|0\rangle = \exp\Bigl(\sum_iV_i\Bigr), \qquad V_i = \frac{(-i\lambda)^{n_i}}{S(V_i)}\int d^4z_1\cdots d^4z_{n_i}\prod_{\text{lines}}D_F ,
> $$
>
> the sum over the connected vacuum diagrams $V_i$ ([[§C6a.11 The iε Limit and Vacuum Bubbles#^def-c6a-11-1|Def. §C6a.11.1]]), each with its symmetry factor.
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening; in $|0\rangle$.
>
> *Source: PS §4.4, p. 98 (the denominator "is just" the exponential, eq. after (4.53)) · the user's PHY 513 notes, Ch. 14 §14.7 ("the bubbles exponentiate, $\sum$ bubbles $= \exp(\sum$ connected bubbles$)$") · PHY 513, Problem Set 8, Problem 3(c) (the same mechanism for a source)*

^thm-c6a-12-1

> [!derivation]- Derivation
> **Step 1** (as a sum over vacuum diagrams). By [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-2|Theorem §C6a.11.2]] (Step 1 of its derivation), with $w(P) = (-i)^n\int d^4z_1\cdots d^4z_n\prod_{\{h,h'\}\in P}D_F$ for $P \in \mathcal P(X_{\varnothing,n})$,
>
> $$
> \langle0|T\{e^{-i\int\hat H_I}\}|0\rangle = \sum_n\frac{\lambda^n}{n!\,(4!)^n}\sum_Pw(P) = \sum_D\frac{w(D)}{S(D)}\,\lambda^{n(D)}
> $$
>
> ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-7|Theorem §CA.7.7]]).
>
> **Step 2** (hypotheses of the exponential formula). $w$ is constant on orbits (Step 5 of [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]]) and multiplicative over components: no line joins two components, so the integrand is a product of one factor per component in disjoint sets of variables, and the integral factorizes (Fubini, formally as in Step 3 of [[§C6a.11 The iε Limit and Vacuum Bubbles#^der-c6a-11-4|Derivation §C6a.11.4]]); the powers $(-i)^n$ multiply since the vertex numbers add.
>
> **Step 3** (apply). [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-3|Theorem §CA.8.3]], 1, with $t = \lambda$: $\sum_D\frac{w(D)}{S(D)}\lambda^{n(D)} = \exp\bigl(\sum_C\frac{w(C)}{S(C)}\lambda^{n(C)}\bigr) = \exp\bigl(\sum_iV_i\bigr)$.
>
> **Step 4** (check, [[§C6a.11 The iε Limit and Vacuum Bubbles#^ex-c6a-11-1|Example §C6a.11.1]]). Through $\lambda^2$, $\exp(V_1 + V_2^{\rm conn} + \dots) = 1 + V_1 + \bigl(V_2^{\rm conn} + \frac12V_1^2\bigr) + O(\lambda^3)$, with $V_2^{\rm conn} = \frac1{16}(\text{dumbbell}) + \frac1{48}(\text{melon})$ and $\frac12V_1^2 = \frac1{128}(\text{two figure-eights})$: Step 3 of that example.

^der-c6a-12-1

*Uses:* [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-2|Theorem §C6a.11.2]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-7|Theorem §CA.7.7]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-3|Theorem §CA.8.3]]

> [!theorem] Theorem §C6a.12.2: The Vacuum Energy Density
> Write each connected vacuum diagram as $V_i = (2T\cdot V)\,b_{V_i}$ ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]]). The ground-state energy of $\hat H$, measured from $\hat H_0|0\rangle = 0$ ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^def-c6a-4-1|Def. §C6a.4.1]]), is, as a formal series,
>
> $$
> \frac{E_0}{V} = i\sum_ib_{V_i} = i\,\frac{\sum_iV_i}{(2\pi)^4\delta^{(4)}(0)} ,
> $$
>
> independent of $T$ and of the volume: $E_0$ is proportional to the volume of space.
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening; $E_0$ of $|\Omega\rangle$ above $|0\rangle$.
>
> *Source: PS §4.4, p. 98, eqs. (4.55)–(4.56) · [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-4|Theorem §C6a.4.4]]*

^thm-c6a-12-2

> [!derivation]- Derivation
> **Step 1** (two expressions for the denominator). By [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-4|Theorem §C6a.4.4]], as $T \to \infty(1 - i\varepsilon)$, $\langle0|U(T, -T)|0\rangle \to e^{-iE_0(2T)}|\langle0|\Omega\rangle|^2$; by [[§C6a.12 Exponentiation of the Vacuum Bubbles and the Vacuum Energy Density#^thm-c6a-12-1|Theorem §C6a.12.1]] and [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]],
>
> $$
> \exp\Bigl(\sum_iV_i\Bigr) = \exp\Bigl(2T\cdot V\sum_ib_{V_i}\Bigr) \;\propto\; e^{-iE_0(2T)} \qquad \text{(PS (4.55))} .
> $$
>
> **Step 2** (compare the $T$-dependence). Take logarithms (formal series with constant term 0 on the left): $2T\cdot V\sum_ib_{V_i} = -2iE_0T + \log|\langle0|\Omega\rangle|^2$. The left side is linear in $T$; the last term does not depend on $T$. Comparing the coefficients of $T$:
>
> $$
> 2V\sum_ib_{V_i} = -2iE_0 \quad\Longrightarrow\quad \frac{E_0}{V} = i\sum_ib_{V_i} = i\,\frac{\sum_iV_i}{2T\cdot V} ,
> $$
>
> and $2T\cdot V = (2\pi)^4\delta^{(4)}(0)$ in the box ([[§C6a.11 The iε Limit and Vacuum Bubbles#^der-c6a-11-3|Derivation §C6a.11.3]], Step 4): PS (4.56).
>
> **Step 3** (first order). $V_1 = -\frac{i\lambda}{8}D_F(0)^2\cdot2T\cdot V$, so $b_{V_1} = -\frac{i\lambda}{8}D_F(0)^2$ and $E_0/V = i\cdot\bigl(-\frac{i\lambda}{8}D_F(0)^2\bigr) + O(\lambda^2) = \frac\lambda8D_F(0)^2 + O(\lambda^2)$: [[§C6a.11 The iε Limit and Vacuum Bubbles#^ex-c6a-11-2|Example §C6a.11.2]], $\langle0|\hat H_{\rm int}|0\rangle/V$.
>
> ⚑ By-product: $E_0 \propto V$, "reassuring" (PS p. 98): the vacuum energy is extensive, an energy density times the volume, like the zero-point energy ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-8|Theorem §C2b.7.8]]); both are formal (UV divergent through $D_F(0)$ and loops).
>
> **What the derivation shows.**
> - The vacuum bubbles are not junk: their sum is $-iE_0\cdot2T$, the phase of the interacting vacuum, which is exactly why the denominator removes them.

^der-c6a-12-2

*Uses:* [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-4|Theorem §C6a.4.4]], [[§C6a.12 Exponentiation of the Vacuum Bubbles and the Vacuum Energy Density#^thm-c6a-12-1|Theorem §C6a.12.1]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]]

> [!remark] Remark: Yu's route
> In §7.1 (p. 286, after eq. (7.103)) Yu states that all the bubble diagrams of perturbation theory contribute only a phase factor, with no observable effect, and refers to §10.5. There the normalization $\mathcal N$ of the correlation functions, a pure phase (the vacuum-to-vacuum amplitude, eq. (10.178)), is expanded in bubbles (eq. (10.193)) and cancelled by the binomial split ([[§C6a.11 The iε Limit and Vacuum Bubbles#^rem-c6a-11-4|§C6a.11, Remark: Yu's route]]). The exponential form and the reading of the phase are written here after PS: $\exp(\sum_iV_i) \propto e^{-iE_0(2T)}$ (PS (4.55); [[§C6a.12 Exponentiation of the Vacuum Bubbles and the Vacuum Energy Density#^thm-c6a-12-2|Theorem §C6a.12.2]]).
>
> *Source: Yu §7.1, p. 286; §10.4, eq. (10.178); §10.5.1, eq. (10.193) · PS §4.4, p. 98*

^rem-c6a-12-1

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-3|Theorem §CA.8.3]] — the exponential formula: the sum over all vacuum diagrams is the exponential of the sum over connected ones (Theorem §C6a.12.1).
> - [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-7|Theorem §CA.7.7]] — a sum over pairings of a weight constant on orbits, divided by $n!\,(4!)^n$, is the sum over diagrams with $\frac1S$ (Derivation §C6a.12.1).
> - [[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]] — a delta function at zero momentum in a finite box is the volume: $(2\pi)^4\delta^{(4)}(0) = 2T\cdot V$, the divisor that turns the sum of the connected bubbles into an energy density (Theorem §C6a.12.2).

> [!remark]- Connections
> - Vacuum bubbles scale with the volume of spacetime like the zero-point energy with the volume of space; both are energies of the vacuum, one of the free and one of the interacting theory, measured from different zeros — [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-8|Theorem §C2b.7.8]], [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^cau-c6a-4-1|§C6a.4, Caution: Two E₀'s]].
> - First-order perturbation theory of quantum mechanics gives the first term of the series for $E_0$, $\langle0|\hat H_{\rm int}|0\rangle = \frac\lambda8D_F(0)^2\,V$, the figure-eight — [[§C6a.11 The iε Limit and Vacuum Bubbles#^ex-c6a-11-2|Example §C6a.11.2]], [[§B8.1 Nondegenerate Perturbation Theory#^thm-b8-1-1|QM Theorem §B8.1.1]].
> - PS's proof that the bubbles cancel runs through this exponential: the numerator is the sum of the attached diagrams times $\exp(\sum_iV_i)$ — [[§C6a.11 The iε Limit and Vacuum Bubbles#^der-c6a-11-4b|Derivation §C6a.11.4, second route]].
> - The vacuum series of a classical source exponentiates by the same formula; there the only connected vacuum diagram is one line, and the series is $e^{\mathcal A_2}$ — [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-3|Theorem §C6c.7.3]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-3|Theorem §CA.8.3]].
