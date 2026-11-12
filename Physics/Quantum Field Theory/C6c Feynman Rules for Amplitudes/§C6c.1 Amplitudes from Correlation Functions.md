---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6c
section: C6c.1
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.9 Evaluating the Cross Section]] · ↑ [[· C6c Feynman Rules for Amplitudes]] · [[§C6c.2 Contractions with External Particles]] →

*Sources: the user's PHY 513 notes, Ch. 15 §15.9 (Principle "Amplitudes are amputated correlators", Figure "amputate", paragraphs "The $\phi^4$ example (filled in)", "Why it is easier", Caution "The rule is stated at tree level"), §15.10 (Principle "From amplitudes to observables", paragraphs "Next.", "Correspondence with Yu") · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), end of the lecture (no slide; transcript 1:20:00–1:23:00), slides 24–25 (summary), and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.5, p. 99 (eq. (4.58)); §4.6, p. 108 (Lecture 16) · Yu Zhao-Huan, 量子场论讲义, §10.3, eqs. (10.107), (10.121); §10.5.2–§10.5.3, eqs. (10.224)–(10.235); §7.3, eq. (7.121) · PHY 513, Problem Set 8, Problems 2 and 4 (the user's solution).*

Lecture 14 gave Feynman rules for correlation functions ([[§C6a.11 Feynman Rules in Momentum Space#^thm-c6a-11-2|Theorem §C6a.11.2]], [[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-5|Theorem §C6a.12.5]]); [[§C6b.1 The S-Matrix and the Invariant Amplitude|§C6b.1]]–[[§C6b.9 Evaluating the Cross Section|§C6b.9]] need amplitudes $\mathcal M$. The lecture ended with the missing link, stated before its proof because of the homework: the amplitude is the correlation function in momentum space with the propagators of the external lines removed, "strip off the external lines" ([[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]]). In $\phi^4$ theory at first order this leaves the bare vertex, $i\mathcal M = -i\lambda$, and with [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-9|Theorem §C6b.4.9]] the first cross section of the course ([[§C6c.1 Amplitudes from Correlation Functions#^ex-c6c-1-2|Example §C6c.1.2]]). The rule holds as stated at lowest order; in general each external line carries a factor $\sqrt Z$. Lecture 16 reached the same rules by the direct route, expanding the $S$-matrix between particle states ([[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]]), and left the justification of the stripping, the LSZ formula, to the second semester (slide 4: "2nd semester fills the missing link: time ordered correlation functions ⇒ $S$-matrix"). Yu derives it from the LSZ reduction formula (§10.3, eqs. (10.107), (10.121)) and states it for all orders as the rule of amputated diagrams (§10.5.3, eqs. (10.230)–(10.235)), checking it on the same $\phi^4$ vertex (eqs. (10.224)–(10.229)). Problem Set 8 used the rule for other theories; what a diagram of an amplitude is ([[§C6c.6 Feynman Rules for Amplitudes#^def-c6c-6-1|Def. §C6c.6.1]]), the vertex factors of any polynomial interaction ([[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]]), the case $S = 1$ ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-5|Theorem §C6c.5.5]]) and the cubic–quartic diagrams of the problem set are now in [[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]] and [[§C6a.14 Feynman Rules for Polynomial Interactions|§C6a.14]]. **Two routes to $i\mathcal M$.** [[§C6c.2 Contractions with External Particles|§C6c.2]] and [[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]] compute $\langle f|i\hat T|i\rangle$ directly between free particle states and read off the tree-level rules ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]]: external line $1$). The amputation rule of this section reproduces them from the correlation functions of C6a ([[§C6c.1 Amplitudes from Correlation Functions#^ex-c6c-1-1|Example §C6c.1.1]] and [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]] give the same $-i\lambda$), and it is the route that generalizes beyond lowest order: through the LSZ formula, with $\sqrt Z$ per external line and the physical mass.

*Conventions* ([[Larsen PHY 513]]): as in [[§C6a.11 Feynman Rules in Momentum Space|§C6a.11]]; external momenta $p_A$, $p_B$ incoming, $p_1$, $p_2$ outgoing; "external propagator" means $\frac{i}{p^2 - m^2 + i\varepsilon}$ of a line ending at an external point.

> [!theorem] Theorem §C6c.1.1: Amplitudes Are Amputated Correlation Functions
> At lowest order, the amplitude $i\mathcal M$ of a process with $n$ external particles is the connected $n$-point correlation function in momentum space with the $n$ external propagators removed and the overall $(2\pi)^4\delta^4$ stripped off. In a diagram, external lines carry no propagator: initial and final particles are lines ending at a vertex, with no propagator.
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* lowest order in the couplings, with free relativistic states over $|0\rangle$ in place of the in and out states ([[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]]); at that order no $\sqrt Z$ is needed; beyond it each external line carries $\sqrt Z$ and the physical mass, the LSZ formula (named in Lecture 16, slide 4, and left to the second semester; QFT C10, planned; [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|Caution: The rule is stated at lowest order]]).
>
> *Source: PHY 513 Lecture 15, transcript ("The rule is actually that you don't have these. You do have an initial particle, … a final particle, but no propagator, no propagator. So the amplitude is actually the same as the corresponding … $n$-point correlation, but without the $n$ propagators"; "They're related by strip off the external lines") · the user's PHY 513 notes, Ch. 15 §15.9, Principle "Amplitudes are amputated correlators" (stated in the lecture; Lecture 16 derives the tree-level rules directly and defers LSZ: a theorem here, its derivation outlined from Yu) · Yu §10.5.3, eqs. (10.230)–(10.235) · PS §4.6 (Lecture 16)*

^thm-c6c-1-1

> [!derivation]- Derivation (outline, Yu's route through the LSZ formula; the course derives it in the second semester)
> <!-- Lecture 16 (Nov 2) did not derive LSZ: it took the direct route (§C6c.6, Theorem §C6c.6.3) and deferred LSZ to the second semester (slide 4). The LSZ formula itself is QFT C10 (planned). Searched: Yu §10.3 pp. 449–458 (the LSZ derivation from asymptotic in/out fields, leading to eq. (10.107)), §10.5.3 pp. 475–478. -->
> **Step 1** (the LSZ formula, taken from Yu; not derived in these notes yet). The momentum-space correlation function $\tilde G^{(n+m)}(q_1, \dots, q_m, -p_1, \dots, -p_n) = \int\prod_i d^4x_i\,e^{ip_i\cdot x_i}\langle\Omega|T\{\cdots\}|\Omega\rangle$ (Yu eq. (10.112)) has a pole at every external mass shell, and the coefficient of the product of poles is the $T$-matrix element (Yu eq. (10.121)):
>
> $$
> \tilde G^{(n+m)} \xrightarrow{\;p_i^0\to E_{\mathbf p_i},\ q_j^0\to E_{\mathbf q_j}\;} \prod_{j=1}^m\frac{i\sqrt Z}{q_j^2 - m^2 + i\varepsilon}\prod_{i=1}^n\frac{i\sqrt Z}{p_i^2 - m^2 + i\varepsilon}\;\langle\mathbf q_1\cdots|i\hat T|\mathbf p_1\cdots\rangle ,
> $$
>
> $Z$ the residue of the full propagator at its pole ("field-strength renormalization").
>
> **Step 2** (the structure of the diagrams). In the diagrams of $\tilde G$ that connect all external points (Yu eq. (10.231)), each external point is joined to the rest by a full propagator, $\frac{iZ}{p^2 - m^2 + i\varepsilon}$ near its pole; what remains when these are cut off is the **amputated** diagram, and the overall $(2\pi)^4\delta^4$ of momentum conservation ([[§C6a.11 Feynman Rules in Momentum Space#^thm-c6a-11-1|Theorem §C6a.11.1]]) factors out (Yu eq. (10.232)):
>
> $$
> \tilde G^{(n+m)}\big|_{\text{fully connected}} \simeq \prod_{j=1}^m\frac{iZ}{q_j^2 - m^2 + i\varepsilon}\prod_{i=1}^n\frac{iZ}{p_i^2 - m^2 + i\varepsilon}\;(2\pi)^4\delta^4\Bigl(\sum_ip_i - \sum_jq_j\Bigr)\times(\text{amputated diagrams}) .
> $$
>
> **Step 3** (compare the residues). Equate the coefficients of the product of poles in Steps 1 and 2; each external line gives $\frac{iZ}{i\sqrt Z} = \sqrt Z$ (Yu eq. (10.233)):
>
> $$
> \langle\mathbf q_1\cdots|i\hat T|\mathbf p_1\cdots\rangle = \prod_{\text{external}}\frac{iZ}{i\sqrt Z}\;(2\pi)^4\delta^4\Bigl(\sum_ip_i - \sum_jq_j\Bigr)\times(\text{amputated diagrams}) = (\sqrt Z)^{n+m}(2\pi)^4\delta^4(\cdots)\times(\text{amputated diagrams}) ,
> $$
>
> and with [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]
>
> $$
> i\mathcal M = (\sqrt Z)^{n+m}\times(\text{sum of the amputated, fully connected diagrams}) \qquad \text{(Yu eqs. (10.234)–(10.235))} .
> $$
>
> **Step 4** (lowest order). $Z = 1 + O(\text{coupling})$ (in $\phi^4$ theory $1 + O(\lambda^2)$: [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|Caution: The rule is stated at lowest order]], below) and the full propagator is $\tilde D_F$ at lowest order ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]]); "in the leading-order calculation one can take $Z = 1$ and $\delta m^2 = 0$" (Yu, box after eq. (10.228)). Then
>
> $$
> \frac{iZ}{p^2 - m^2 + i\varepsilon} = \tilde D_F(p) + O(\lambda) , \qquad i\mathcal M = 1^{n+m}\times(\text{amputated diagrams}) = \frac{\text{fully connected diagrams of }\tilde G^{(n+m)}}{\prod_{\text{external}}\tilde D_F\cdot(2\pi)^4\delta^4(\cdots)} ,
> $$
>
> the statement.
>
> **What the derivation shows.**
> - The rule rests on the pole structure of the correlation functions at the physical masses; the external propagators are exactly the poles, and their residues are what is stripped.
> - Beyond lowest order the rule needs $\sqrt Z$ per external line and the physical mass in the poles (Caution: The rule is stated at lowest order).

^der-c6c-1-1

*Uses:* [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§C6a.11 Feynman Rules in Momentum Space#^thm-c6a-11-1|Theorem §C6a.11.1]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]]; the LSZ formula (Yu eq. (10.121); QFT C10, planned)

> [!example] Example §C6c.1.1: φφ → φφ at First Order
> ![[ph-qft-c6-16-1.svg]]
> *The rule of Theorem §C6c.1.1 in $\phi^4$ theory. Left: the fully connected first-order diagram of the four-point correlator, with its four external propagators (orange). Right: removing them, and the overall $(2\pi)^4\delta^4$, leaves the bare vertex: $i\mathcal M = -i\lambda$ for $\phi\phi \to \phi\phi$ at this order (Example §C6c.1.1). Added figure, from the user's notes (Figure "amputate").*
>
> In $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]) the fully connected four-point function at first order, Fourier transformed in all four external points with momenta $p_A$, $p_B$ flowing in and $p_1$, $p_2$ flowing out, is
>
> $$
> \Bigl(\prod_{j=1}^4\frac{i}{p_j^2 - m^2 + i\varepsilon}\Bigr)\,(-i\lambda)\,(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2) ,
> $$
>
> with symmetry factor $1$. Removing the four propagators and the delta function ([[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]]) leaves
>
> $$
> i\mathcal M = -i\lambda + O(\lambda^2) ,
> $$
>
> dimensionless, as [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|Theorem §C6b.1.5]] requires, and independent of the momenta.
>
> **Step 1** (first order of the numerator). As in [[§C6a.8 Feynman Diagrams for Correlation Functions#^der-c6a-8-1|Derivation §C6a.8.1]], Steps 1–2, with $\hat\phi_j \equiv \hat\phi_I(x_j)$ for the external points and $\hat\phi_{z_a} \equiv \hat\phi_I(z)$, $a = 1, \dots, 4$, for the four factors of $\hat\phi_I(z)^4$:
>
> $$
> \langle0|T\Bigl\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\Bigl(-\frac{i\lambda}{4!}\int d^4z\,\hat\phi_I(z)^4\Bigr)\Bigr\}|0\rangle = -\frac{i\lambda}{4!}\int d^4z\;\langle0|T\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\,\hat\phi_{z_1}\hat\phi_{z_2}\hat\phi_{z_3}\hat\phi_{z_4}\}|0\rangle .
> $$
>
> **Step 2** (Wick's theorem: time order → normal order plus contractions). By [[§C6a.7 Wick's Theorem#^thm-c6a-7-2|Theorem §C6a.7.2]], with every contracted pair replaced by the propagator of its two points ([[§C6a.6 Normal Ordering and Contractions#^def-c6a-6-1|Def. §C6a.6.1]]) and named under it, $\{i, j\}$ for $\hat\phi_i$ with $\hat\phi_j$ and $\{j, z_a\}$ for $\hat\phi_j$ with $\hat\phi_{z_a}$ (all four $\hat\phi_{z_a}$ sit at $z$), the eight fields give $\binom{8}{2k}(2k - 1)!!$ terms with $k$ contractions:
>
> $$
> \begin{aligned}
> T\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\hat\phi_{z_1}\hat\phi_{z_2}\hat\phi_{z_3}\hat\phi_{z_4}\} ={}& :\!\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\hat\phi_{z_1}\hat\phi_{z_2}\hat\phi_{z_3}\hat\phi_{z_4}\!: &&1\text{ term}\\
> &+ \underbrace{D_F(x_1 - x_2)}_{\{1, 2\}}\,:\!\hat\phi_3\hat\phi_4\hat\phi_{z_1}\hat\phi_{z_2}\hat\phi_{z_3}\hat\phi_{z_4}\!: + \underbrace{D_F(x_1 - z)}_{\{1, z_1\}}\,:\!\hat\phi_2\hat\phi_3\hat\phi_4\hat\phi_{z_2}\hat\phi_{z_3}\hat\phi_{z_4}\!: + \cdots &&\tbinom82 = 28\text{ terms}\\
> &+ \underbrace{D_F(x_1 - z)D_F(x_2 - z)}_{\{1, z_1\}\,\{2, z_2\}}\,:\!\hat\phi_3\hat\phi_4\hat\phi_{z_3}\hat\phi_{z_4}\!: + \cdots &&\tbinom84\cdot3 = 210\text{ terms}\\
> &+ \underbrace{D_F(x_1 - z)D_F(x_2 - z)D_F(x_3 - z)}_{\{1, z_1\}\,\{2, z_2\}\,\{3, z_3\}}\,:\!\hat\phi_4\hat\phi_{z_4}\!: + \cdots &&\tbinom86\cdot15 = 420\text{ terms}\\
> &+ \underbrace{D_F(x_1 - z)D_F(x_2 - z)D_F(x_3 - z)D_F(x_4 - z)}_{\{1, z_1\}\,\{2, z_2\}\,\{3, z_3\}\,\{4, z_4\}} + \cdots &&7!! = 105\text{ terms} .
> \end{aligned}
> $$
>
> **Step 3** (vacuum value). The contractions are numbers; every term with a remainder $:\!\cdots\!:$ of $8$, $6$, $4$ or $2$ fields has $\langle0|:\!\cdots\!:|0\rangle = 0$ ([[§C6a.6 Normal Ordering and Contractions#^thm-c6a-6-1|Theorem §C6a.6.1]], 2; spelled out in [[§C6a.7 Wick's Theorem#^ex-c6a-7-2|Example §C6a.7.2]], Step 3). Only the $7!! = 105$ complete contractions survive ([[§C6a.7 Wick's Theorem#^thm-c6a-7-3|Theorem §C6a.7.3]], [[§CA.8 Pairings, Diagrams and Symmetry Factors#^thm-ca-8-1|Theorem §CA.8.1]]).
>
> **Step 4** (the fully connected ones). A complete contraction containing a pair $\{i, j\}$ of two external fields, a factor $D_F(x_i - x_j)$, has a line from $x_i$ to $x_j$ that touches nothing else: it is not fully connected ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-1|§C6c.1, Caution: "Connected" here means fully connected]]). In the others each $\hat\phi_j$ is contracted with a different $\hat\phi_{z_{\sigma(j)}}$, which uses up all four $\hat\phi_{z_a}$; so they are labelled by the permutations $\sigma \in S_4$, $4! = 24$ of them, and the remaining $105 - 24 = 81$ are not fully connected. With $D_{ja} \equiv D_F(x_j - z_a)$ the contraction of $\sigma$ is $\{1, z_{\sigma(1)}\}\,\{2, z_{\sigma(2)}\}\,\{3, z_{\sigma(3)}\}\,\{4, z_{\sigma(4)}\} \longmapsto D_{1\sigma(1)}D_{2\sigma(2)}D_{3\sigma(3)}D_{4\sigma(4)}$, and the 24 are
>
> $$
> \begin{aligned}
> &D_{11}D_{22}D_{33}D_{44} + D_{11}D_{22}D_{34}D_{43} + D_{11}D_{23}D_{32}D_{44} + D_{11}D_{23}D_{34}D_{42} + D_{11}D_{24}D_{32}D_{43} + D_{11}D_{24}D_{33}D_{42} &&x_1\text{ with }z_1\\
> +{}&D_{12}D_{21}D_{33}D_{44} + D_{12}D_{21}D_{34}D_{43} + D_{12}D_{23}D_{31}D_{44} + D_{12}D_{23}D_{34}D_{41} + D_{12}D_{24}D_{31}D_{43} + D_{12}D_{24}D_{33}D_{41} &&x_1\text{ with }z_2\\
> +{}&D_{13}D_{21}D_{32}D_{44} + D_{13}D_{21}D_{34}D_{42} + D_{13}D_{22}D_{31}D_{44} + D_{13}D_{22}D_{34}D_{41} + D_{13}D_{24}D_{31}D_{42} + D_{13}D_{24}D_{32}D_{41} &&x_1\text{ with }z_3\\
> +{}&D_{14}D_{21}D_{32}D_{43} + D_{14}D_{21}D_{33}D_{42} + D_{14}D_{22}D_{31}D_{43} + D_{14}D_{22}D_{33}D_{41} + D_{14}D_{23}D_{31}D_{42} + D_{14}D_{23}D_{32}D_{41} &&x_1\text{ with }z_4
> \end{aligned}
> $$
>
> (each row: $\hat\phi_1$ with $\hat\phi_{z_a}$, then the $3! = 6$ ways of contracting $\hat\phi_2, \hat\phi_3, \hat\phi_4$ with the other three).
>
> **Step 5** (set $z_a = z$; the coefficient). Every $D_{ja} \to D_F(x_j - z)$, so each of the 24 terms becomes $\prod_{j=1}^4D_F(x_j - z)$ and, with Step 1,
>
> $$
> -\frac{i\lambda}{4!}\int d^4z\;24\prod_{j=1}^4D_F(x_j - z) = -i\lambda\int d^4z\,\prod_{j=1}^4D_F(x_j - z) ,
> $$
>
> coefficient $\frac{24}{1!\,(4!)^1} = 1 = \frac1S$ ([[§C6a.9 Position-Space Feynman Rules#^thm-c6a-9-1|Theorem §C6a.9.1]]): $S = 1$, "the $4!$ ways of attaching four distinct external lines to the vertex cancel the $1/4!$" (Yu eq. (10.224)). Dividing by the denominator of the master formula, $1 + O(\lambda)$, changes nothing at this order: no bubble factor remains ([[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-5|Theorem §C6a.12.5]]).
>
> **Step 6** (momentum space). Insert $D_F(x_j - z) = \int\frac{d^4k_j}{(2\pi)^4}\frac{i\,e^{-ik_j\cdot(x_j - z)}}{k_j^2 - m^2 + i\varepsilon}$ ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]]) and do the $z$ integral ([[§C6a.11 Feynman Rules in Momentum Space#^thm-c6a-11-1|Theorem §C6a.11.1]]):
>
> $$
> -i\lambda\int d^4z\,\prod_{j=1}^4D_F(x_j - z) = \int\prod_{j=1}^4\frac{d^4k_j}{(2\pi)^4}\,\frac{i\,e^{-ik_j\cdot x_j}}{k_j^2 - m^2 + i\varepsilon}\;(-i\lambda)\,(2\pi)^4\delta^4(k_1 + k_2 + k_3 + k_4) .
> $$
>
> Fourier transform the external points, $p_A$, $p_B$ flowing in at $x_1$, $x_2$ and $p_1$, $p_2$ flowing out at $x_3$, $x_4$ (momentum $-p_1$, $-p_2$ entering):
>
> $$
> \int d^4x_1\,e^{ip_A\cdot x_1}e^{-ik_1\cdot x_1} = (2\pi)^4\delta^4(p_A - k_1) , \quad \int d^4x_2\,e^{ip_B\cdot x_2}e^{-ik_2\cdot x_2} = (2\pi)^4\delta^4(p_B - k_2) , \quad \int d^4x_3\,e^{-ip_1\cdot x_3}e^{-ik_3\cdot x_3} = (2\pi)^4\delta^4(p_1 + k_3) ,
> $$
>
> and the same at $x_4$ with $p_2$. These deltas do the four $k_j$ integrals, $k_1 = p_A$, $k_2 = p_B$, $k_3 = -p_1$, $k_4 = -p_2$; the propagators are even in $k$, and the vertex delta becomes $\delta^4(p_A + p_B - p_1 - p_2)$ (Yu eq. (10.229)):
>
> $$
> \frac{i}{p_A^2 - m^2 + i\varepsilon}\,\frac{i}{p_B^2 - m^2 + i\varepsilon}\,\frac{i}{p_1^2 - m^2 + i\varepsilon}\,\frac{i}{p_2^2 - m^2 + i\varepsilon}\;(-i\lambda)\,(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2) ,
> $$
>
> the expression of the statement.
>
> **Step 7** (amputate). Divide by the four external propagators and strip $(2\pi)^4\delta^4$ ([[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]):
>
> $$
> i\mathcal M = \frac{\prod_j\frac{i}{p_j^2 - m^2 + i\varepsilon}\,(-i\lambda)\,(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2)}{\prod_j\frac{i}{p_j^2 - m^2 + i\varepsilon}\cdot(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2)} = -i\lambda .
> $$
>
> Yu, through LSZ: $i\mathcal M = -i\lambda/Z^2 = -i\lambda + O(\lambda^2)$ (eq. (10.228)), "the same as the leading-order result (7.121)".
>
> *Equivalently,* by contractions with the external states: [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]] gives the same $i\mathcal M = -i\lambda$ from $\langle\mathbf p_1\mathbf p_2|i\hat T^{(1)}|\mathbf p_A\mathbf p_B\rangle$; here the $24$ are the bijections of four external points to four legs, there of four particles to four legs.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.9 (paragraph "The $\phi^4$ example (filled in)"), Figure "amputate" · PHY 513 Lecture 15, transcript · Yu §10.5.2, eqs. (10.224)–(10.229); §7.3, eq. (7.121)*

^ex-c6c-1-1

> [!example] Example §C6c.1.2: The φ⁴ Cross Section at Lowest Order
> ![[ph-qft-c6b-9-1.svg]]
> *(a) The single first-order diagram of $\phi\phi \to \phi\phi$: $i\mathcal M = -i\lambda$, $S = 1$, $|\mathcal M|^2 = \lambda^2$. (b) The centre-of-mass frame: the directions $(\theta, \varphi)$ and $(\pi - \theta, \varphi + \pi)$ of $\mathbf p_1$ are the same final state of two identical particles, the factor $\frac{1}{S_{\rm id}} = \frac12$ in $\sigma_{\rm total}$ (Step 3). Added figure.*
>
> For $\phi\phi \to \phi\phi$ at first order, $|\mathcal M|^2 = \lambda^2$ ([[§C6c.1 Amplitudes from Correlation Functions#^ex-c6c-1-1|Example §C6c.1.1]]), and all four masses are equal, so by [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-9|Theorem §C6b.4.9]] the scattering is isotropic in the centre-of-mass frame ("no angular dependence (feature of spin-less particles)", slide 19):
>
> $$
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \frac{\lambda^2}{64\pi^2E_{\rm cm}^2} , \qquad \sigma_{\rm total} = \frac12\cdot4\pi\cdot\frac{\lambda^2}{64\pi^2E_{\rm cm}^2} = \frac{\lambda^2}{32\pi E_{\rm cm}^2} .
> $$
>
> **Step 1** ($|\mathcal M|^2$). From $i\mathcal M = -i\lambda$ with $\lambda$ real, $\mathcal M = -\lambda$ and $|\mathcal M|^2 = (-\lambda)^2 = \lambda^2$.
>
> **Step 2** (differential cross section). Insert into [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-9|Theorem §C6b.4.9]]: $(d\sigma/d\Omega)_{\rm cm} = \lambda^2/(64\pi^2E_{\rm cm}^2)$, independent of $(\theta, \varphi)$.
>
> **Step 3** (total cross section). By [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|Theorem §C6b.9.4]] with $S_{\rm id} = 2! = 2$ for the two identical final particles (integrating over the full sphere counts the configurations $\theta$ and $\pi - \theta$ twice):
>
> $$
> \sigma_{\rm total} = \frac{1}{S_{\rm id}}\int_0^{2\pi}d\varphi\int_0^\pi\sin\theta\,d\theta\;\frac{\lambda^2}{64\pi^2E_{\rm cm}^2} = \frac12\cdot2\pi\cdot2\cdot\frac{\lambda^2}{64\pi^2E_{\rm cm}^2} = \frac{4\pi\lambda^2}{128\pi^2E_{\rm cm}^2} = \frac{\lambda^2}{32\pi E_{\rm cm}^2} .
> $$
>
> The diagram's symmetry factor is $S = 1$; the two factors are different things ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^cau-c6b-1-2|§C6b.1, Caution: Four S's]]). The cross section falls like $1/E_{\rm cm}^2$, as dimensional analysis requires for a dimensionless $\mathcal M$ ([[§C6b.4 Two-Body Scattering Kinematics#^rem-c6b-4-3|§C6b.4, Remark: Why 1/E²: dimensional analysis]]).
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.9 (paragraph "The $\phi^4$ example (filled in)") · PHY 513 Lecture 16, slide 19 ("No angular dependence (feature of spin-less particles). Simple energy dependence (follows by dimensional analysis). Special to $\phi^4$-theory at leading order"; $\sigma_{\rm tot} = \lambda^2/(32\pi E_{\rm cm}^2)$, "note: identical particles") · PS §4.6, p. 112, eqs. (4.99)–(4.100) · checked in `qft-C/tools/l15/checks.py`*

^ex-c6c-1-2

> [!theorem] Theorem §C6c.1.2: The Disconnected Pieces of the Free Four-Point Function Do Not Scatter
> Fourier transform the free four-point function ([[§C6a.8 Feynman Diagrams for Correlation Functions#^ex-c6a-8-1|Example §C6a.8.1]]) with $p_A$, $p_B$ flowing in at $x_1$, $x_2$ and $p_1$, $p_2$ flowing out at $x_3$, $x_4$. Then
>
> $$
> \begin{aligned}
> \int\prod_jd^4x_j\;e^{ip_A\cdot x_1 + ip_B\cdot x_2 - ip_1\cdot x_3 - ip_2\cdot x_4}\,\langle0|T\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\}|0\rangle ={}& \tilde D_F(p_A)\tilde D_F(p_2)\,(2\pi)^8\delta^4(p_A + p_B)\,\delta^4(p_1 + p_2)\\
> &+ \tilde D_F(p_A)\tilde D_F(p_B)\,(2\pi)^8\delta^4(p_A - p_1)\,\delta^4(p_B - p_2)\\
> &+ \tilde D_F(p_A)\tilde D_F(p_B)\,(2\pi)^8\delta^4(p_A - p_2)\,\delta^4(p_B - p_1) .
> \end{aligned}
> $$
>
> On physical momenta ($p^0 = E_{\mathbf p} > 0$) the first term vanishes and the other two are supported on $\{p_1, p_2\} = \{p_A, p_B\}$: none contributes to $\langle f|i\hat T|i\rangle$ away from the forward direction, and none has the form $\delta^4(p_A + p_B - p_1 - p_2)\times$(smooth) of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]].
>
> *Equivalently,* between particle states: each connected piece carries its own momentum delta ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]]); this theorem is its zeroth-order, correlator form.
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* zeroth order, exact for the free field in $|0\rangle$; physical momenta $p^0 = E_{\mathbf p} > 0$.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.9 ("The disconnected pieces of the same correlator, such as $D_F(x_1 - x_3)D_F(x_2 - x_4)$, describe particles that pass through untouched. They belong to the $\mathbb 1$ of $S = \mathbb 1 + iT$") · PS §4.5, p. 99, eq. (4.58)*

^thm-c6c-1-2

> [!derivation]- Derivation
> **Step 1** (the three pairings). By [[§C6a.8 Feynman Diagrams for Correlation Functions#^ex-c6a-8-1|Example §C6a.8.1]],
>
> $$
> \langle0|T\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\}|0\rangle = \underbrace{D_{12}D_{34}}_{\{1, 2\}\,\{3, 4\}} + \underbrace{D_{13}D_{24}}_{\{1, 3\}\,\{2, 4\}} + \underbrace{D_{14}D_{23}}_{\{1, 4\}\,\{2, 3\}} ,
> $$
>
> $D_{ij} = D_F(x_i - x_j)$, the contracted pairs named under each term; each factor of each term involves two of the four points, so the transform factorizes into two two-point transforms.
>
> **Step 2** (one line). Insert $D_F(x_i - x_j) = \int\frac{d^4k}{(2\pi)^4}\tilde D_F(k)\,e^{-ik\cdot(x_i - x_j)}$ ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]]) and do the two position integrals with [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]]; for phases $e^{iq_i\cdot x_i}$, $e^{iq_j\cdot x_j}$ (momenta $q_i$, $q_j$ entering),
>
> $$
> \int d^4x_i\,d^4x_j\;e^{iq_i\cdot x_i + iq_j\cdot x_j}\,D_F(x_i - x_j) = \int\frac{d^4k}{(2\pi)^4}\tilde D_F(k)\,(2\pi)^4\delta^4(q_i - k)\,(2\pi)^4\delta^4(q_j + k) = \tilde D_F(q_i)\,(2\pi)^4\delta^4(q_i + q_j) .
> $$
>
> **Step 3** (the three terms). With $(q_1, q_2, q_3, q_4) = (p_A, p_B, -p_1, -p_2)$ and $\tilde D_F(-k) = \tilde D_F(k)$ ([[§C6a.8 Feynman Diagrams for Correlation Functions#^thm-c6a-8-2|Theorem §C6a.8.2]], 1):
>
> $$
> \begin{aligned}
> D_{12}D_{34} &\to \tilde D_F(p_A)(2\pi)^4\delta^4(p_A + p_B)\cdot\tilde D_F(p_1)(2\pi)^4\delta^4(-p_1 - p_2) , & \tilde D_F(p_1) &= \tilde D_F(p_2)\text{ on the support},\\
> D_{13}D_{24} &\to \tilde D_F(p_A)(2\pi)^4\delta^4(p_A - p_1)\cdot\tilde D_F(p_B)(2\pi)^4\delta^4(p_B - p_2) ,\\
> D_{14}D_{23} &\to \tilde D_F(p_A)(2\pi)^4\delta^4(p_A - p_2)\cdot\tilde D_F(p_B)(2\pi)^4\delta^4(p_B - p_1) ,
> \end{aligned}
> $$
>
> and $\delta^4(-p_1 - p_2) = \delta^4(p_1 + p_2)$: the statement.
>
> **Step 4** (support). $\delta^4(p_A + p_B)$ needs $p_A^0 + p_B^0 = E_{\mathbf p_A} + E_{\mathbf p_B} = 0$, impossible for $E > 0$. The second and third terms need $(p_1, p_2) = (p_A, p_B)$ or $(p_B, p_A)$: final momenta equal to the initial ones, which [[§C6b.8 Wave Packets and the Cross Section#^lem-c6b-8-5|Lemma §C6b.8.5]] excludes from scattering.
>
> **What the derivation shows.**
> - A disconnected piece carries one momentum delta per connected component, two here, instead of the single overall $\delta^4(p_A + p_B - p_1 - p_2)$: particles in separate components keep their momenta. Such pieces belong to the $\mathbb 1$ of $\hat S = \mathbb 1 + i\hat T$ (or to products of lower-point processes), not to $\mathcal M$; PS (4.58) draws them and notes that such diagrams "do not exponentiate or factor; they contribute to the amplitude just as do the fully connected diagrams". Between particle states: [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]].

^der-c6c-1-2

*Uses:* [[§C6a.8 Feynman Diagrams for Correlation Functions#^ex-c6a-8-1|Example §C6a.8.1]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]], [[§C6a.8 Feynman Diagrams for Correlation Functions#^thm-c6a-8-2|Theorem §C6a.8.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]], [[§C6b.8 Wave Packets and the Cross Section#^lem-c6b-8-5|Lemma §C6b.8.5]]

> [!remark] Remark: Disconnected pieces beyond zeroth order
> The four-point correlator also contains disconnected pieces at higher orders, e.g. a line times a line with a tadpole at first order. They describe particles that pass through, at least partly, untouched; each connected component carries its own momentum delta function, and such pieces belong to the $\mathbb 1$ of $\hat S = \mathbb 1 + i\hat T$ (or to products of lower-point processes), not to $\mathcal M$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^der-c6b-1-4|Derivation §C6b.1.4]], second point).
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.9 · PS §4.5, p. 99, eq. (4.58)*

^rem-c6c-1-1

> [!caution] Caution: "Connected" here means fully connected
> For amplitudes the relevant diagrams are **fully connected**: every external point can be reached from every other along the lines (Yu, 完全连通图, after eq. (10.224); PS p. 99). That is stronger than "attached to the external points", the sense in which the slides of Lecture 14 called the bubble-free diagrams "connected" ([[§C6a.12 The iε Limit and Vacuum Bubbles#^cau-c6a-12-1|§C6a.12, Caution: Connected means attached to an external point]]): a line from $x_1$ to $x_3$ next to a tadpole-corrected line from $x_2$ to $x_4$ is attached but not fully connected.
>
> *Source: Yu §10.5.2, after eq. (10.224) · PS §4.5, p. 99 · [[§C6a.12 The iε Limit and Vacuum Bubbles#^cau-c6a-12-1|§C6a.12, Caution: Connected means attached to an external point]]*

^cau-c6c-1-1

> [!caution] Caution: The rule is stated at lowest order
> [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]] is exact at lowest order. Beyond it, loop corrections on an external line are not simply discarded: they renormalize the field, a factor $\sqrt Z$ per external line, and shift the mass to the physical mass at which the poles sit. The precise statement is the LSZ reduction formula (Yu §10.3, eqs. (10.107), (10.121); $i\mathcal M = (\sqrt Z)^{n+2}\times$ amputated diagrams for $2 \to n$, eq. (10.235)), the subject of the second semester. Lecture 16 turned this into the rule that diagrams are amputated ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^def-c6c-5-1|Def. §C6c.5.1]], [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]]); in $\phi^4$ theory $\sqrt Z = 1 + O(\lambda^2)$, since the one-loop tadpole is momentum independent and only shifts the mass (the user's PHY 513 notes, Lecture 16 update, §16.2, "Filled in: what is still being neglected", and §16.7, Caution "What amputation hides").
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.9, Caution "The rule is stated at tree level" · Yu §10.3, §10.5.3, eqs. (10.228), (10.235)*

^cau-c6c-1-2

> [!remark] Remark: Why amplitudes are easier
> Amplitudes are easier to compute than correlation functions. Without the external propagators, a lowest-order process through a single vertex leaves only the vertex factor, a number, and the remaining work in such a problem is the phase space ([[§C6b.4 Two-Body Scattering Kinematics|§C6b.4]]).
>
> *Source: PHY 513 Lecture 15, transcript · the user's PHY 513 notes, Ch. 15 §15.9 (paragraph "Why it is easier")*

^rem-c6c-1-2

> [!remark] Remark: Why the rule was stated early
> Two of the four problems of Problem Set 8 came ahead of the lectures: they use Feynman rules to compute $\mathcal M$ and then $|\mathcal M|^2$, one of them with the decay formula ([[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]]), whereas Lecture 14 gave Feynman rules for correlation functions, not for amplitudes. The work for that week was symmetry factors, some Feynman rules and phase-space factors. The rule of [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]] was stated for that reason, ahead of the direct derivation of the rules in Lecture 16 (the LSZ justification is left to the second semester).
>
> *Source: PHY 513 Lecture 15, transcript (1:20:00) · the user's PHY 513 notes, Ch. 15 §15.9 (opening paragraph)*

^rem-c6c-1-3

> [!remark] Remark: From amplitudes to observables (summary)
> - $\hat S = \mathbb 1 + i\hat T$ and $\langle f|i\hat T|i\rangle = (2\pi)^4\delta^4(p_i - p_f)\,i\mathcal M$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]). "$\mathcal M$ is wave function overlap ${}_{\rm out}\langle\vec p_1\vec p_2\ldots|\vec k_A\vec k_B\ldots\rangle_{\rm in}$ except for removal of: trivial scattering (in = out); overall $\delta$-function that conserves 4-momentum." "Central goal of QFT: compute and analyze $\mathcal M$."
> - Cross section: $d\sigma = \frac{1}{2E_A2E_B|\mathbf v_A - \mathbf v_B|}|\mathcal M|^2d\Pi_n$ ([[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-3|Theorem §C6b.9.3]]); the denominator is the kinematics of the two initial particles, invariant under boosts along the beam ([[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-7|Theorem §C6b.9.7]]).
> - Phase space: $d\Pi_n$ ([[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]]); two bodies in the centre-of-mass frame $\int d\Omega\,\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}}$ ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]]); all masses equal, $(d\sigma/d\Omega)_{\rm cm} = |\mathcal M|^2/(64\pi^2E_{\rm cm}^2)$ ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-9|Theorem §C6b.4.9]]).
> - Decay: $d\Gamma = \frac{1}{2m_A}|\mathcal M|^2d\Pi_n$ ([[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]]); in a propagator the width appears as $p^2 - m^2 + im\Gamma$, and a moving particle decays at the time-dilated rate $\frac{m}{E}\Gamma$ ([[§C6b.7 The Width in the Propagator#^thm-c6b-7-3|Theorem §C6b.7.3]]).
> - Amplitudes are correlation functions with the external propagators stripped off ([[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]]).
>
> *Source: PHY 513 Lecture 15, slides 24–25 ("Summary I: Formula for Cross-section", "Summary II: Relativistic Phase Space Factor") · the user's PHY 513 notes, Ch. 15 §15.10, Principle "From amplitudes to observables" (a summary: a remark here)*

^rem-c6c-1-4

> [!remark] Remark: Feynman rules for amplitudes (next)
> Lecture 16 (Nov 2, PS §4.6) justifies the stripping rule and gives Feynman rules for amplitudes (as announced; in the event it gave the rules by the direct route, [[§C6c.2 Contractions with External Particles|§C6c.2]]–[[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]] (amputation [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors|§C6c.5]], the rules [[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]]), and left LSZ to the second semester), first in $\phi^4$ theory, then for Yukawa theory and QED, where external lines carry spinors and polarization vectors instead of propagators (Yukawa: [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|§C6d.2, Theorem §C6d.2.1]]; QED: [[§C8.4 Feynman Rules for QED#^thm-c8-4-1|§C8.4, Theorem §C8.4.1]]). PS start from the same definition, $\langle\mathbf p_1\mathbf p_2\cdots|S|\mathbf k_A\mathbf k_B\rangle = \lim_{T\to\infty}\langle\mathbf p_1\mathbf p_2\cdots|e^{-iH(2T)}|\mathbf k_A\mathbf k_B\rangle$ (eq. (4.87)), and relate the interacting states to free ones by the same $T \to \infty(1 - i\epsilon)$ device as for the vacuum (eq. (4.88); [[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-1|Theorem §C6a.5.1]]). Lecture 16 states this as a prescription: [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]].
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.10 (paragraph "Next.") · PS §4.6, p. 108, eqs. (4.87)–(4.88) · PHY 513 Lecture 15, transcript · [[PHY 513 Course Log]] (Lecture 16: PS §4.6)*

^rem-c6c-1-5

> [!remark] Remark: Yu's route
> Yu reaches amplitudes from correlation functions through the LSZ reduction formula: the $T$-matrix element is the Fourier transform of the $(n + m)$-point function with a Klein–Gordon operator $\frac{i}{\sqrt Z}(\partial^2 + m^2)$ applied to each external point (eq. (10.107)), equivalently the residue of its poles (eq. (10.121)). He checks it on the $\phi^4$ vertex ($\phi\phi \to \phi\phi$, eqs. (10.224)–(10.229); $(\partial^2 + m^2)D_F = -i\delta^4$, eq. (10.226), removes each external propagator in position space) and states the general rule as "amputated" (切断) diagrams with a factor $\sqrt Z$ per external line (§10.5.3, eqs. (10.230)–(10.235)), for Dirac and vector fields as well (eqs. (10.236)–(10.237)). His momentum-space Feynman rules for $\mathcal M$ (§7.2–§7.3) come first in his order and are justified by this later; the course states the rule in Lecture 15, reaches the same tree-level rules directly in Lecture 16 ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]]) and leaves the LSZ proof to the second semester.
>
> *Source: Yu §10.3, pp. 454–456, eqs. (10.107), (10.121); §10.5.2–§10.5.3, pp. 474–477, eqs. (10.224)–(10.237)*

^rem-c6c-1-6

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]] — the Fourier transforms of the external points give the momentum deltas, one per connected component.
> - [[§CA.8 Pairings, Diagrams and Symmetry Factors#^thm-ca-8-1|Theorem §CA.8.1]] — eight fields have $7!! = 105$ complete contractions.

> [!remark]- Connections
> - The diagrams of a scattering amplitude ([[§C6c.6 Feynman Rules for Amplitudes#^def-c6c-6-1|Def. §C6c.6.1]]), the case $S = 1$ ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-5|Theorem §C6c.5.5]]) and the cubic–quartic diagrams of Problem Set 8 ([[§C6c.6 Feynman Rules for Amplitudes#^ex-c6c-6-1|Example §C6c.6.1]], [[§C6c.6 Feynman Rules for Amplitudes#^ex-c6c-6-2|Example §C6c.6.2]]) are in [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors|§C6c.5]] and [[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]], with the tree-level rules for $i\mathcal M$ that the external-state contractions give (amputation and symmetry factors with the particles held fixed in §C6c.5, the rules in §C6c.6); the vertex factors of a polynomial interaction, $-ig_t\prod_km_{t,k}!$, are [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]], with the Feynman rules for any polynomial interaction.
> - The external propagators that are stripped are the poles of the correlation functions at the particle masses; the same poles appear in the spectral picture of the two-point function, with residue $Z$ — QFT C10 (planned), [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]].
> - In position space, stripping a propagator is applying $(\partial^2 + m^2)$, since $D_F$ is a Green's function of the Klein–Gordon operator — [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription|§C2b.7]].
> - "Fully connected" is stronger than the "attached" of the bubble cancellation; disconnected pieces of the correlator are the $\mathbb 1$ and products of smaller processes — [[§C6a.12 The iε Limit and Vacuum Bubbles#^cau-c6a-12-1|§C6a.12, Caution: Connected means attached to an external point]].
> - The symmetry factor of the diagram and the identical-particle factor of the final state enter the same cross section separately — [[§C6a.9 Position-Space Feynman Rules#^def-c6a-9-1|Def. §C6a.9.1]], [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|Theorem §C6b.9.4]].
> - The contraction of a field with an outgoing particle, which the amputation rule hides, is written out for $n$ particles in both normalizations in [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]]; with it the decay $\Phi \to \phi\phi$ is computed directly from $\langle f|T\exp|i\rangle$ — [[§C6b.6 Decay Kinematics#^ex-c6b-6-1|Example §C6b.6.1]].
> - The first-order amplitude $-i\lambda$ is the analogue of the first Born approximation of quantum mechanics, where the $T$-matrix is replaced by the potential — [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-6|QM Theorem §C10.1.6]].
