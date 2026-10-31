---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.8
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.7 Decay Rates and Widths]] · ↑ [[· C6b The S-Matrix, Amplitudes and Observables]] · [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route]] →

*Sources: the user's PHY 513 notes, Ch. 15 §15.9 (Principle "Amplitudes are amputated correlators", Figure "amputate", paragraphs "The $\phi^4$ example (filled in)", "Why it is easier", Caution "The rule is stated at tree level"), §15.10 (Principle "From amplitudes to observables", paragraphs "Next.", "Correspondence with Yu") · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), end of the lecture (no slide; transcript 1:20:00–1:23:00), slides 24–25 (summary), and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.5, p. 99 (eq. (4.58)); §4.6, p. 108 (Lecture 16) · Yu Zhao-Huan, 量子场论讲义, §10.3, eqs. (10.107), (10.121); §10.5.2–§10.5.3, eqs. (10.224)–(10.235); §7.3, eq. (7.121) · PHY 513, Problem Set 8, Problems 2 and 4 (the user's solution).*

Lecture 14 gave Feynman rules for correlation functions ([[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-2|Theorem §C6a.10.2]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-5|Theorem §C6a.11.5]]); [[§C6b.1 The S-Matrix and the Invariant Amplitude|§C6b.1]]–[[§C6b.7 Decay Rates and Widths|§C6b.7]] need amplitudes $\mathcal M$. The lecture ended with the missing link, stated before its proof because of the homework: the amplitude is the correlation function in momentum space with the propagators of the external lines removed, "strip off the external lines" ([[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-1|Theorem §C6b.8.1]]). In $\phi^4$ theory at first order this leaves the bare vertex, $i\mathcal M = -i\lambda$, and with [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-8|Theorem §C6b.6.8]] the first cross section of the course ([[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-2|Example §C6b.8.2]]). The rule holds as stated at lowest order; in general each external line carries a factor $\sqrt Z$. Lecture 16 justifies it. Yu derives it from the LSZ reduction formula (§10.3, eqs. (10.107), (10.121)) and states it for all orders as the rule of amputated diagrams (§10.5.3, eqs. (10.230)–(10.235)), checking it on the same $\phi^4$ vertex (eqs. (10.224)–(10.229)). Problem Set 8 used the rule for other theories; the last subsection makes precise what a diagram of an amplitude is ([[§C6b.8 Amplitudes from Correlation Functions#^def-c6b-8-1|Def. §C6b.8.1]]), gives the vertex factors of any polynomial interaction ([[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-3|Theorem §C6b.8.3]]) and the case $S = 1$ ([[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-4|Theorem §C6b.8.4]]), with the cubic–quartic diagrams of the problem set.

*Conventions* ([[Larsen PHY 513]]): as in [[§C6a.10 Feynman Rules in Momentum Space|§C6a.10]]; external momenta $p_A$, $p_B$ incoming, $p_1$, $p_2$ outgoing; "external propagator" means $\frac{i}{p^2 - m^2 + i\varepsilon}$ of a line ending at an external point.

> [!theorem] Theorem §C6b.8.1: Amplitudes Are Amputated Correlation Functions
> At lowest order, the amplitude $i\mathcal M$ of a process with $n$ external particles is the connected $n$-point correlation function in momentum space with the $n$ external propagators removed and the overall $(2\pi)^4\delta^4$ stripped off. In a diagram, external lines carry no propagator: initial and final particles are lines ending at a vertex, "but no propagator".
>
> *Source: PHY 513 Lecture 15, transcript ("The rule is actually that you don't have these. You do have an initial particle, … a final particle, but no propagator, no propagator. So the amplitude is actually the same as the corresponding … $n$-point correlation, but without the $n$ propagators"; "They're related by strip off the external lines") · the user's PHY 513 notes, Ch. 15 §15.9, Principle "Amplitudes are amputated correlators" (stated in the lecture, justified in Lecture 16: a theorem here, its derivation outlined from Yu) · Yu §10.5.3, eqs. (10.230)–(10.235) · PS §4.6 (Lecture 16)*

^thm-c6b-8-1

> [!derivation]- Derivation (outline, Yu's route through the LSZ formula; to be completed with Lecture 16)
> <!-- To be filled with Lecture 16 (Nov 2): PS §4.6, eqs. (4.87)–(4.104); the LSZ formula itself is QFT C10 (planned). Searched: Yu §10.3 pp. 449–458 (the LSZ derivation from asymptotic in/out fields, leading to eq. (10.107)), §10.5.3 pp. 475–478. -->
> **Step 1** (the LSZ formula, taken from Yu; not derived in these notes yet). The momentum-space correlation function $\tilde G^{(n+m)}(q_1, \dots, q_m, -p_1, \dots, -p_n) = \int\prod_i d^4x_i\,e^{ip_i\cdot x_i}\langle\Omega|T\{\cdots\}|\Omega\rangle$ (Yu eq. (10.112)) has a pole at every external mass shell, and the coefficient of the product of poles is the $T$-matrix element (Yu eq. (10.121)):
>
> $$
> \tilde G^{(n+m)} \xrightarrow{\;p_i^0\to E_{\mathbf p_i},\ q_j^0\to E_{\mathbf q_j}\;} \prod_{j=1}^m\frac{i\sqrt Z}{q_j^2 - m^2 + i\varepsilon}\prod_{i=1}^n\frac{i\sqrt Z}{p_i^2 - m^2 + i\varepsilon}\;\langle\mathbf q_1\cdots|i\hat T|\mathbf p_1\cdots\rangle ,
> $$
>
> $Z$ the residue of the full propagator at its pole ("field-strength renormalization").
>
> **Step 2** (the structure of the diagrams). In the diagrams of $\tilde G$ that connect all external points (Yu eq. (10.231)), each external point is joined to the rest by a full propagator, $\frac{iZ}{p^2 - m^2 + i\varepsilon}$ near its pole; what remains when these are cut off is the **amputated** diagram, and the overall $(2\pi)^4\delta^4$ of momentum conservation ([[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-1|Theorem §C6a.10.1]]) factors out (Yu eq. (10.232)):
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
> **Step 4** (lowest order). $Z = 1 + O(\lambda)$ and the full propagator is $\tilde D_F$ at lowest order ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]); "in the leading-order calculation one can take $Z = 1$ and $\delta m^2 = 0$" (Yu, box after eq. (10.228)). Then
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

^der-c6b-8-1

*Uses:* [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-1|Theorem §C6a.10.1]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]; the LSZ formula (Yu eq. (10.121); QFT C10, planned)

![[ph-qft-c6-16-1.svg]]
*The rule of Theorem §C6b.8.1 in $\phi^4$ theory. Left: the fully connected first-order diagram of the four-point correlator, with its four external propagators (orange). Right: removing them, and the overall $(2\pi)^4\delta^4$, leaves the bare vertex: $i\mathcal M = -i\lambda$ for $\phi\phi \to \phi\phi$ at this order (Example §C6b.8.1). Added figure, from the user's notes (Figure "amputate").*

> [!example] Example §C6b.8.1: φφ → φφ at First Order
> In $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]) the fully connected four-point function at first order, Fourier transformed in all four external points with momenta $p_A$, $p_B$ flowing in and $p_1$, $p_2$ flowing out, is
>
> $$
> \Bigl(\prod_{j=1}^4\frac{i}{p_j^2 - m^2 + i\varepsilon}\Bigr)\,(-i\lambda)\,(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2) ,
> $$
>
> with symmetry factor $1$. Removing the four propagators and the delta function ([[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-1|Theorem §C6b.8.1]]) leaves
>
> $$
> i\mathcal M = -i\lambda + O(\lambda^2) ,
> $$
>
> dimensionless, as [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-3|Theorem §C6b.1.3]] requires, and independent of the momenta.
>
> **Step 1** (first order of the numerator). As in [[§C6a.7 Feynman Diagrams for Correlation Functions#^der-c6a-7-1|Derivation §C6a.7.1]], Steps 1–2, with $\hat\phi_j \equiv \hat\phi_I(x_j)$ for the external points and $\hat\phi_{z_a} \equiv \hat\phi_I(z)$, $a = 1, \dots, 4$, for the four factors of $\hat\phi_I(z)^4$:
>
> $$
> \langle0|T\Bigl\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\Bigl(-\frac{i\lambda}{4!}\int d^4z\,\hat\phi_I(z)^4\Bigr)\Bigr\}|0\rangle = -\frac{i\lambda}{4!}\int d^4z\;\langle0|T\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\,\hat\phi_{z_1}\hat\phi_{z_2}\hat\phi_{z_3}\hat\phi_{z_4}\}|0\rangle .
> $$
>
> **Step 2** (Wick's theorem: time order → normal order plus contractions). By [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]], with $\overbracket{\hat\phi_i\hat\phi_j} = D_F(x_i - x_j)$ for a contracted pair ([[§C6a.5 Normal Ordering and Contractions#^def-c6a-5-1|Def. §C6a.5.1]]), the eight fields give $\binom{8}{2k}(2k - 1)!!$ terms with $k$ brackets:
>
> $$
> \begin{aligned}
> T\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\hat\phi_{z_1}\hat\phi_{z_2}\hat\phi_{z_3}\hat\phi_{z_4}\} ={}& :\!\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\hat\phi_{z_1}\hat\phi_{z_2}\hat\phi_{z_3}\hat\phi_{z_4}\!: &&1\text{ term}\\
> &+ \overbracket{\hat\phi_1\hat\phi_2}\,:\!\hat\phi_3\hat\phi_4\hat\phi_{z_1}\hat\phi_{z_2}\hat\phi_{z_3}\hat\phi_{z_4}\!: + \overbracket{\hat\phi_1\hat\phi_{z_1}}\,:\!\hat\phi_2\hat\phi_3\hat\phi_4\hat\phi_{z_2}\hat\phi_{z_3}\hat\phi_{z_4}\!: + \cdots &&\tbinom82 = 28\text{ terms}\\
> &+ \overbracket{\hat\phi_1\hat\phi_{z_1}}\,\overbracket{\hat\phi_2\hat\phi_{z_2}}\,:\!\hat\phi_3\hat\phi_4\hat\phi_{z_3}\hat\phi_{z_4}\!: + \cdots &&\tbinom84\cdot3 = 210\text{ terms}\\
> &+ \overbracket{\hat\phi_1\hat\phi_{z_1}}\,\overbracket{\hat\phi_2\hat\phi_{z_2}}\,\overbracket{\hat\phi_3\hat\phi_{z_3}}\,:\!\hat\phi_4\hat\phi_{z_4}\!: + \cdots &&\tbinom86\cdot15 = 420\text{ terms}\\
> &+ \overbracket{\hat\phi_1\hat\phi_{z_1}}\,\overbracket{\hat\phi_2\hat\phi_{z_2}}\,\overbracket{\hat\phi_3\hat\phi_{z_3}}\,\overbracket{\hat\phi_4\hat\phi_{z_4}} + \cdots &&7!! = 105\text{ terms} .
> \end{aligned}
> $$
>
> **Step 3** (vacuum value). The brackets are numbers; every term with a remainder $:\!\cdots\!:$ of $8$, $6$, $4$ or $2$ fields has $\langle0|:\!\cdots\!:|0\rangle = 0$ ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 2; spelled out in [[§C6a.6 Wick's Theorem#^ex-c6a-6-2|Example §C6a.6.2]], Step 3). Only the $7!! = 105$ complete contractions survive ([[§C6a.6 Wick's Theorem#^thm-c6a-6-3|Theorem §C6a.6.3]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]).
>
> **Step 4** (the fully connected ones). A complete contraction containing a bracket $\overbracket{\hat\phi_i\hat\phi_j}$ of two external fields has a line from $x_i$ to $x_j$ that touches nothing else: it is not fully connected ([[§C6b.8 Amplitudes from Correlation Functions#^cau-c6b-8-1|§C6b.8, Caution: "Connected" here means fully connected]]). In the others each $\hat\phi_j$ is bracketed with a different $\hat\phi_{z_{\sigma(j)}}$, which uses up all four $\hat\phi_{z_a}$; so they are labelled by the permutations $\sigma \in S_4$, $4! = 24$ of them, and the remaining $105 - 24 = 81$ are not fully connected. With $D_{ja} \equiv D_F(x_j - z_a)$ and $\overbracket{\hat\phi_1\hat\phi_{z_{\sigma(1)}}}\,\overbracket{\hat\phi_2\hat\phi_{z_{\sigma(2)}}}\,\overbracket{\hat\phi_3\hat\phi_{z_{\sigma(3)}}}\,\overbracket{\hat\phi_4\hat\phi_{z_{\sigma(4)}}} = D_{1\sigma(1)}D_{2\sigma(2)}D_{3\sigma(3)}D_{4\sigma(4)}$, the 24 are
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
> (each row: $\hat\phi_1$ with $\hat\phi_{z_a}$, then the $3! = 6$ ways of bracketing $\hat\phi_2, \hat\phi_3, \hat\phi_4$ with the other three).
>
> **Step 5** (set $z_a = z$; the coefficient). Every $D_{ja} \to D_F(x_j - z)$, so each of the 24 terms becomes $\prod_{j=1}^4D_F(x_j - z)$ and, with Step 1,
>
> $$
> -\frac{i\lambda}{4!}\int d^4z\;24\prod_{j=1}^4D_F(x_j - z) = -i\lambda\int d^4z\,\prod_{j=1}^4D_F(x_j - z) ,
> $$
>
> coefficient $\frac{24}{1!\,(4!)^1} = 1 = \frac1S$ ([[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-1|Theorem §C6a.8.1]]): $S = 1$, "the $4!$ ways of attaching four distinct external lines to the vertex cancel the $1/4!$" (Yu eq. (10.224)). Dividing by the denominator of the master formula, $1 + O(\lambda)$, changes nothing at this order: no bubble factor remains ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-5|Theorem §C6a.11.5]]).
>
> **Step 6** (momentum space). Insert $D_F(x_j - z) = \int\frac{d^4k_j}{(2\pi)^4}\frac{i\,e^{-ik_j\cdot(x_j - z)}}{k_j^2 - m^2 + i\varepsilon}$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]) and do the $z$ integral ([[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-1|Theorem §C6a.10.1]]):
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
> **Step 7** (amputate). Divide by the four external propagators and strip $(2\pi)^4\delta^4$ ([[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-1|Theorem §C6b.8.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]):
>
> $$
> i\mathcal M = \frac{\prod_j\frac{i}{p_j^2 - m^2 + i\varepsilon}\,(-i\lambda)\,(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2)}{\prod_j\frac{i}{p_j^2 - m^2 + i\varepsilon}\cdot(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2)} = -i\lambda .
> $$
>
> Yu, through LSZ: $i\mathcal M = -i\lambda/Z^2 = -i\lambda + O(\lambda^2)$ (eq. (10.228)), "the same as the leading-order result (7.121)".
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.9 (paragraph "The $\phi^4$ example (filled in)"), Figure "amputate" · PHY 513 Lecture 15, transcript · Yu §10.5.2, eqs. (10.224)–(10.229); §7.3, eq. (7.121)*

^ex-c6b-8-1

> [!example] Example §C6b.8.2: The φ⁴ Cross Section at Lowest Order
> For $\phi\phi \to \phi\phi$ at first order, $|\mathcal M|^2 = \lambda^2$ ([[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-1|Example §C6b.8.1]]), and all four masses are equal, so by [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-8|Theorem §C6b.6.8]] the scattering is isotropic in the centre-of-mass frame:
>
> $$
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \frac{\lambda^2}{64\pi^2E_{\rm cm}^2} , \qquad \sigma_{\rm total} = \frac12\cdot4\pi\cdot\frac{\lambda^2}{64\pi^2E_{\rm cm}^2} = \frac{\lambda^2}{32\pi E_{\rm cm}^2} .
> $$
>
> **Step 1** ($|\mathcal M|^2$). From $i\mathcal M = -i\lambda$ with $\lambda$ real, $\mathcal M = -\lambda$ and $|\mathcal M|^2 = (-\lambda)^2 = \lambda^2$.
>
> **Step 2** (differential cross section). Insert into [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-8|Theorem §C6b.6.8]]: $(d\sigma/d\Omega)_{\rm cm} = \lambda^2/(64\pi^2E_{\rm cm}^2)$, independent of $(\theta, \varphi)$.
>
> **Step 3** (total cross section). By [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-4|Theorem §C6b.5.4]] with $S_{\rm id} = 2! = 2$ for the two identical final particles (integrating over the full sphere counts the configurations $\theta$ and $\pi - \theta$ twice):
>
> $$
> \sigma_{\rm total} = \frac{1}{S_{\rm id}}\int_0^{2\pi}d\varphi\int_0^\pi\sin\theta\,d\theta\;\frac{\lambda^2}{64\pi^2E_{\rm cm}^2} = \frac12\cdot2\pi\cdot2\cdot\frac{\lambda^2}{64\pi^2E_{\rm cm}^2} = \frac{4\pi\lambda^2}{128\pi^2E_{\rm cm}^2} = \frac{\lambda^2}{32\pi E_{\rm cm}^2} .
> $$
>
> The diagram's symmetry factor is $S = 1$; the two factors are different things ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^cau-c6b-1-2|§C6b.1, Caution: Four S's]]). The cross section falls like $1/E_{\rm cm}^2$, as dimensional analysis requires for a dimensionless $\mathcal M$ ([[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^rem-c6b-6-2|§C6b.6, Remark: Why 1/E²: dimensional analysis]]).
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.9 (paragraph "The $\phi^4$ example (filled in)") · checked in `qft-C/tools/l15/checks.py`*

^ex-c6b-8-2

> [!theorem] Theorem §C6b.8.2: The Disconnected Pieces of the Free Four-Point Function Do Not Scatter
> Fourier transform the free four-point function ([[§C6a.7 Feynman Diagrams for Correlation Functions#^ex-c6a-7-1|Example §C6a.7.1]]) with $p_A$, $p_B$ flowing in at $x_1$, $x_2$ and $p_1$, $p_2$ flowing out at $x_3$, $x_4$. Then
>
> $$
> \begin{aligned}
> \int\prod_jd^4x_j\;e^{ip_A\cdot x_1 + ip_B\cdot x_2 - ip_1\cdot x_3 - ip_2\cdot x_4}\,\langle0|T\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\}|0\rangle ={}& \tilde D_F(p_A)\tilde D_F(p_2)\,(2\pi)^8\delta^4(p_A + p_B)\,\delta^4(p_1 + p_2)\\
> &+ \tilde D_F(p_A)\tilde D_F(p_B)\,(2\pi)^8\delta^4(p_A - p_1)\,\delta^4(p_B - p_2)\\
> &+ \tilde D_F(p_A)\tilde D_F(p_B)\,(2\pi)^8\delta^4(p_A - p_2)\,\delta^4(p_B - p_1) .
> \end{aligned}
> $$
>
> On physical momenta ($p^0 = E_{\mathbf p} > 0$) the first term vanishes and the other two are supported on $\{p_1, p_2\} = \{p_A, p_B\}$: none contributes to $\langle f|i\hat T|i\rangle$ away from the forward direction, and none has the form $\delta^4(p_A + p_B - p_1 - p_2)\times$(smooth) of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-2|Theorem §C6b.1.2]].
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.9 ("The disconnected pieces of the same correlator, such as $D_F(x_1 - x_3)D_F(x_2 - x_4)$, describe particles that pass through untouched. They belong to the $\mathbb 1$ of $S = \mathbb 1 + iT$") · PS §4.5, p. 99, eq. (4.58)*

^thm-c6b-8-2

> [!derivation]- Derivation
> **Step 1** (the three pairings). By [[§C6a.7 Feynman Diagrams for Correlation Functions#^ex-c6a-7-1|Example §C6a.7.1]],
>
> $$
> \langle0|T\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\}|0\rangle = \overbracket{\hat\phi_1\hat\phi_2}\,\overbracket{\hat\phi_3\hat\phi_4} + \overbracket{\hat\phi_1\hat\phi_3}\,\overbracket{\hat\phi_2\hat\phi_4} + \overbracket{\hat\phi_1\hat\phi_4}\,\overbracket{\hat\phi_2\hat\phi_3} = D_{12}D_{34} + D_{13}D_{24} + D_{14}D_{23} ,
> $$
>
> $D_{ij} = D_F(x_i - x_j)$; each factor of each term involves two of the four points, so the transform factorizes into two two-point transforms.
>
> **Step 2** (one line). Insert $D_F(x_i - x_j) = \int\frac{d^4k}{(2\pi)^4}\tilde D_F(k)\,e^{-ik\cdot(x_i - x_j)}$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]) and do the two position integrals with [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]; for phases $e^{iq_i\cdot x_i}$, $e^{iq_j\cdot x_j}$ (momenta $q_i$, $q_j$ entering),
>
> $$
> \int d^4x_i\,d^4x_j\;e^{iq_i\cdot x_i + iq_j\cdot x_j}\,D_F(x_i - x_j) = \int\frac{d^4k}{(2\pi)^4}\tilde D_F(k)\,(2\pi)^4\delta^4(q_i - k)\,(2\pi)^4\delta^4(q_j + k) = \tilde D_F(q_i)\,(2\pi)^4\delta^4(q_i + q_j) .
> $$
>
> **Step 3** (the three terms). With $(q_1, q_2, q_3, q_4) = (p_A, p_B, -p_1, -p_2)$ and $\tilde D_F(-k) = \tilde D_F(k)$ ([[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-2|Theorem §C6a.7.2]], 1):
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
> **Step 4** (support). $\delta^4(p_A + p_B)$ needs $p_A^0 + p_B^0 = E_{\mathbf p_A} + E_{\mathbf p_B} = 0$, impossible for $E > 0$. The second and third terms need $(p_1, p_2) = (p_A, p_B)$ or $(p_B, p_A)$: final momenta equal to the initial ones, which [[§C6b.4 Wave Packets and the Cross Section#^lem-c6b-4-5|Lemma §C6b.4.5]] excludes from scattering.
>
> **What the derivation shows.**
> - A disconnected piece carries one momentum delta per connected component, two here, instead of the single overall $\delta^4(p_A + p_B - p_1 - p_2)$: particles in separate components keep their momenta. Such pieces belong to the $\mathbb 1$ of $\hat S = \mathbb 1 + i\hat T$ (or to products of lower-point processes), not to $\mathcal M$; PS (4.58) draws them and notes that such diagrams "do not exponentiate or factor; they contribute to the amplitude just as do the fully connected diagrams".

^der-c6b-8-2

*Uses:* [[§C6a.7 Feynman Diagrams for Correlation Functions#^ex-c6a-7-1|Example §C6a.7.1]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-2|Theorem §C6a.7.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-2|Theorem §C6b.1.2]], [[§C6b.4 Wave Packets and the Cross Section#^lem-c6b-4-5|Lemma §C6b.4.5]]

> [!remark] Remark: Disconnected pieces beyond zeroth order
> The four-point correlator also contains disconnected pieces at higher orders, e.g. a line times a line with a tadpole at first order. They describe particles that pass through, at least partly, untouched; each connected component carries its own momentum delta function, and such pieces belong to the $\mathbb 1$ of $\hat S = \mathbb 1 + i\hat T$ (or to products of lower-point processes), not to $\mathcal M$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^der-c6b-1-2|Derivation §C6b.1.2]], second point).
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.9 · PS §4.5, p. 99, eq. (4.58)*

^rem-c6b-8-1

> [!caution] Caution: "Connected" here means fully connected
> For amplitudes the relevant diagrams are **fully connected**: every external point can be reached from every other along the lines (Yu, 完全连通图, after eq. (10.224); PS p. 99). That is stronger than "attached to the external points", the sense in which the slides of Lecture 14 called the bubble-free diagrams "connected" ([[§C6a.11 The iε Limit and Vacuum Bubbles#^cau-c6a-11-1|§C6a.11, Caution: Connected means attached to an external point]]): a line from $x_1$ to $x_3$ next to a tadpole-corrected line from $x_2$ to $x_4$ is attached but not fully connected.
>
> *Source: Yu §10.5.2, after eq. (10.224) · PS §4.5, p. 99 · [[§C6a.11 The iε Limit and Vacuum Bubbles#^cau-c6a-11-1|§C6a.11, Caution: Connected means attached to an external point]]*

^cau-c6b-8-1

## Diagrams of scattering amplitudes

> [!definition] Definition §C6b.8.1: Diagram of a Scattering Amplitude
> For a process with initial momenta $p_A, p_B, \dots$ and final momenta $p_1, p_2, \dots$, a **diagram of the amplitude** $i\mathcal M$ is a diagram ([[§C6a.7 Feynman Diagrams for Correlation Functions#^def-c6a-7-1|Def. §C6a.7.1]]; other vertices: [[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]]) such that
> 1. its external points are labelled by the external momenta, one per particle, and are never relabelled;
> 2. it is fully connected ([[§C6b.8 Amplitudes from Correlation Functions#^cau-c6b-8-1|Caution: "Connected" here means fully connected]]);
> 3. its external lines are amputated ([[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-1|Theorem §C6b.8.1]]): each external point is joined by a line without propagator to a vertex, and the momentum of every internal line is fixed by conservation at the vertices.
>
> Its symmetry factor is that of [[§C6a.8 Position-Space Feynman Rules#^def-c6a-8-1|Def. §C6a.8.1]] with the labelled external points held fixed. Diagrams that are not fully connected are excluded: their pieces belong to the $\mathbb 1$ of $\hat S = \mathbb 1 + i\hat T$ or to products of smaller processes ([[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-2|Theorem §C6b.8.2]], [[§C6b.8 Amplitudes from Correlation Functions#^rem-c6b-8-1|Remark: Disconnected pieces beyond zeroth order]]).
>
> *Source: PHY 513, Problem Set 8, Problem 2(a)–(b) (the user's solution: "The four external particles are labeled by their momenta and are never relabeled, so a diagram is determined by which external particles are attached to which vertex"; a vertex with too many external particles leaves two legs "contracted with each other, giving a disconnected diagram that does not contribute to the scattering amplitude") · PHY 513 Lecture 15, transcript ("strip off the external lines") · Yu §7.3 (external lines of $\langle f|iT|i\rangle$)*

^def-c6b-8-1

> [!theorem] Theorem §C6b.8.3: Vertex Factors of a Polynomial Interaction
> Let $\mathcal L_{\rm int} = -\sum_tg_t\,M_t$, each $M_t$ a monomial without derivatives in fields of kinds $k$ ($\phi$, $\Phi$, or $\phi$ and $\phi^\dagger$ of a complex field), with $m_{t,k}$ factors of kind $k$. Then:
> 1. the **vertex factor** of type $t$ is $i$ times the coefficient of $M_t$ in $\mathcal L_{\rm int}$ times the number of ways to attach distinct lines to its legs:
>
> $$
> -ig_t\prod_km_{t,k}! \qquad\text{(times } \textstyle\int d^4z \text{ in position space, } (2\pi)^4\delta^4(\sum p) \text{ in momentum space)} ;
> $$
>
> 2. every diagram enters with $\frac1S\prod_{\text{vertices}}(\text{vertex factor})$ and the rules for lines of [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-2|Theorem §C6a.8.2]], $S$ its symmetry factor ([[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]]).
>
> | $\mathcal L_{\rm int}$ | legs | vertex factor |
> |---|---|---|
> | $-\frac{g}{3!}\phi^3$ | $\phi\phi\phi$ | $-i\frac{g}{3!}\cdot3! = -ig$ |
> | $-\frac{\lambda}{4!}\phi^4$ | $\phi\phi\phi\phi$ | $-i\lambda$ |
> | $-\mu\,\Phi\phi^2$ | $\Phi\phi\phi$ | $-i\mu\cdot1!\cdot2! = -2i\mu$ |
> | $-\frac\lambda4(\phi^\dagger\phi)^2$ | $\phi\phi\phi^\dagger\phi^\dagger$ | $-i\frac\lambda4\cdot2!\cdot2! = -i\lambda$ |
>
> *Source: PHY 513, Problem Set 8, statement of Problem 2 (vertices $-ig$, $-i\lambda$) and Problem 1(b) (vertex $-i\lambda$ for $\frac\lambda4(\phi^\dagger\phi)^2$); the user's solution of Problem 4 ($\mathcal M = -2\mu$, "each of $\hat a_{\mathbf p_1}, \hat a_{\mathbf p_2}$ … pairs with one of the two fields, in 2 ways") · PS §4.4, p. 93 ("the various placements of these contractions into $\phi\phi\phi\phi$ generates a factor of 4!") · proof written here*

^thm-c6b-8-3

> [!derivation]- Derivation
> **Step 1** (the Dyson term). Without derivatives $\hat{\mathcal H}_I = -\mathcal L_{\rm int}$, so with $n_t$ vertices of type $t$ the Dyson series contributes ($\frac{1}{n!}\binom{n}{n_1, n_2, \dots} = \prod_t\frac{1}{n_t!}$ for $n = \sum_tn_t$)
>
> $$
> \prod_t\frac{(-ig_t)^{n_t}}{n_t!}\int\prod_{t,v}d^4z_{t,v}\;\langle0|T\Bigl\{(\text{external fields})\prod_{t,v}M_t(z_{t,v})\Bigr\}|0\rangle .
> $$
>
> **Step 2** (one vertex, distinct lines). At one vertex of type $t$, let $\sum_km_{t,k}$ distinct lines (to different external points or other vertices) end on it, $m_{t,k}$ of them on legs of kind $k$. The contractions realizing this assign the lines of kind $k$ bijectively to the $m_{t,k}$ legs of kind $k$: $\prod_km_{t,k}!$ ways, all with the same integrand. So the vertex contributes $-ig_t\prod_km_{t,k}!$. Example $\mu\Phi\phi^2$ with lines to $\mathbf K$ ($\Phi$) and $\mathbf p_1$, $\mathbf p_2$ ($\phi$): $1!\cdot2! = 2$ ([[§C6b.7 Decay Rates and Widths#^ex-c6b-7-1|Example §C6b.7.1]], Step 4).
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

^der-c6b-8-3

*Uses:* [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]], [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-2|Theorem §C6a.8.2]]

> [!theorem] Theorem §C6b.8.4: Vertices Saturated by External Lines Give S = 1
> If every vertex $v$ of a diagram has valence $r_v \ge 2$ and at least $r_v - 1$ of its legs joined to external points, then $S = 1$; equivalently $N_D = |G|$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]). In particular every tree diagram with one internal line has $S = 1$.
>
> *Source: PHY 513, Problem Set 8, Problem 2(c) (the user's argument: "each vertex has exactly one internal leg … The external particles are never relabeled, so an element of $\mathrm{Stab}(P)$ fixes every leg joined to an external particle. The internal leg is then the only remaining leg at its vertex, so it is fixed as well") · PHY 513 Lecture 14, slide 17 ("Reordering of legs = topologically distinct diagram ⇒ S = 1")*

^thm-c6b-8-4

> [!derivation]- Derivation
> **Step 1** (vertices fixed). Let $g \in \operatorname{Stab}(P)$. Each leg joined to an external point is fixed, and so is its vertex ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 3). Every vertex has $r_v - 1 \ge 1$ such legs, so $g$ permutes no vertices.
>
> **Step 2** (legs fixed). $g$ maps the legs of $v$ to legs of $v$; at least $r_v - 1$ are fixed, so the remaining one (if any) is mapped to itself. Hence $g$ fixes every half-edge: $g = e$, $S = |\operatorname{Stab}(P)| = 1$.
>
> **Step 3** (count). $N_D = |G|/S = |G|$. Example (one cubic and one quartic vertex, five external particles, two on the cubic and three on the quartic vertex): the two at the cubic vertex attach in $3\cdot2$ ways, the three at the quartic vertex in $4\cdot3\cdot2$, the remaining two legs pair in one way: $N_D = 6\cdot24 = 144 = 3!\,4! = |G|$.

^der-c6b-8-4

*Uses:* [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]

> [!example] Example §C6b.8.3: Cubic–Quartic Theory, 2 → 2 at Order g² and λ
> $\mathcal L = \frac12(\partial_\mu\phi)^2 - \frac{m^2}{2}\phi^2 - \frac{g}{3!}\phi^3 - \frac{\lambda}{4!}\phi^4$, vertices $-ig$, $-i\lambda$ ([[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-3|Theorem §C6b.8.3]]); $p_A + p_B \to p_1 + p_2$. A diagram with $n_3$ cubic and $n_4$ quartic vertices is of order $g^{n_3}\lambda^{n_4}$ (Problem Set 8: treat $\lambda \sim g^2/m^2$ as the same order).
> - *$O(g^2)$, two cubic vertices*: $6$ legs, $4$ joined to external lines, so one internal line. If one vertex carried three external particles, the other would carry one, and its two remaining legs would be contracted with each other: not fully connected, excluded ([[§C6b.8 Amplitudes from Correlation Functions#^def-c6b-8-1|Def. §C6b.8.1]]). So each vertex carries two, and $p_A$ shares its vertex with exactly one of $p_B$, $p_1$, $p_2$ (putting $p_A$ on the other vertex only exchanges the vertices): three diagrams.
> - *$O(\lambda)$, one quartic vertex*: all four on it, one diagram.
>
> | diagram | at one vertex | at the other | internal momentum |
> |---|---|---|---|
> | $s$-channel | $p_A, p_B$ | $p_1, p_2$ | $p_A + p_B$ |
> | $t$-channel | $p_A, p_1$ | $p_B, p_2$ | $p_A - p_1$ |
> | $u$-channel | $p_A, p_2$ | $p_B, p_1$ | $p_A - p_2$ |
> | contact | $p_A, p_B, p_1, p_2$ | — | — |
>
> Each has $S = 1$ ([[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-4|Theorem §C6b.8.4]]): the cubic vertices carry $2 = 3 - 1$ external lines, the quartic one $4$. Enumeration: the $9!! = 945$ pairings at order $g^2$ form $31$ diagrams, of which exactly these $3$ are fully connected, each an orbit of $72 = 2!\,(3!)^2 = |G|$.
>
> *Source: PHY 513, Problem Set 8, Problem 2(a) (the user's solution: diagrams drawn and with vertices opened into their legs) · checked with `qft-C/tools/hw8/check_hw8.py`*

^ex-c6b-8-3

> [!example] Example §C6b.8.4: Cubic–Quartic Theory, 2 → 3 at Order gλ
> Same theory, $p_A + p_B \to p_1 + p_2 + p_3$, one cubic and one quartic vertex: $3 + 4 = 7$ legs, $5$ joined to external lines, one internal line. Three external particles on the cubic vertex would leave two legs of the quartic vertex contracted with each other, four on the quartic vertex two legs of the cubic one: not fully connected. So two external particles sit on the cubic vertex and three on the quartic, and a diagram is the choice of the two at the cubic vertex: $\binom52 = 10$. With $u \in \{A, B\}$, $v \ne u$, $i \in \{1, 2, 3\}$, $\{j, k\} = \{1, 2, 3\}\setminus\{i\}$:
>
> | class | at the cubic vertex | number | internal momentum |
> |---|---|---|---|
> | (I) both incoming | $p_A, p_B$ | $1$ | $p_A + p_B$ |
> | (II) one in, one out | $p_u, p_i$ | $2\cdot3 = 6$ | $p_u - p_i$ |
> | (III) both outgoing | $p_j, p_k$ | $3$ | $p_A + p_B - p_i = p_j + p_k$ |
>
> $1 + 6 + 3 = 10$. All have $S = 1$ ([[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-4|Theorem §C6b.8.4]], Step 3: $N_D = 144 = 3!\,4! = |G|$; there is one vertex of each type, so $G$ contains no vertex permutations). Enumeration: the $11!! = 10\,395$ pairings of the $12$ half-edges form $195$ diagrams, exactly $10$ of them fully connected, each an orbit of $144$.
>
> *Source: PHY 513, Problem Set 8, Problem 2(b)–(c) (the user's solution) · checked with `qft-C/tools/hw8/check_hw8.py`*

^ex-c6b-8-4

![[ph-qft-c6-17-1.svg]]
*The diagrams of [[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-3|Example §C6b.8.3]] and [[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-4|Example §C6b.8.4]] (cubic vertices orange, quartic blue; incoming momenta left, outgoing right). Top: $2 \to 2$, the $s$-, $t$-, $u$-channel diagrams at order $g^2$ and the contact diagram at order $\lambda$. Bottom: $2 \to 3$ at order $g\lambda$, one representative of each class (I), (II), (III). Added figure, adapted from the user's solution of PHY 513, Problem Set 8, Problem 2.*

> [!caution] Caution: The rule is stated at lowest order
> [[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-1|Theorem §C6b.8.1]] is exact at lowest order. Beyond it, loop corrections on an external line are not simply discarded: they renormalize the field, a factor $\sqrt Z$ per external line, and shift the mass to the physical mass at which the poles sit. The precise statement is the LSZ reduction formula (Yu §10.3, eqs. (10.107), (10.121); $i\mathcal M = (\sqrt Z)^{n+2}\times$ amputated diagrams for $2 \to n$, eq. (10.235)), taken up in Lecture 16 and the second term.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.9, Caution "The rule is stated at tree level" · Yu §10.3, §10.5.3, eqs. (10.228), (10.235)*

^cau-c6b-8-2

> [!remark] Remark: Why amplitudes are easier
> "It's actually easier than doing these correlation functions." Without the external propagators, a lowest-order process through a single vertex leaves only the vertex factor: "there's nothing left … something like a number", and the remaining work in such a problem is the phase space ([[§C6b.6 Lorentz Invariance and Two-Body Phase Space|§C6b.6]]), "don't sweat over that part".
>
> *Source: PHY 513 Lecture 15, transcript · the user's PHY 513 notes, Ch. 15 §15.9 (paragraph "Why it is easier")*

^rem-c6b-8-2

> [!remark] Remark: Why the rule was stated early
> At the end of the lecture Larsen said that two of the four problems of Problem Set 8 are "premature": they use Feynman rules to compute $\mathcal M$ and then $|\mathcal M|^2$, one of them with the decay formula ([[§C6b.7 Decay Rates and Widths#^thm-c6b-7-4|Theorem §C6b.7.4]]), whereas Lecture 14 gave Feynman rules for correlation functions, not for amplitudes. "What you should do this week is … symmetry factors, a bit of Feynman rules, and a little bit of phase space factors." The rule of [[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-1|Theorem §C6b.8.1]] was stated for that reason, ahead of its justification in Lecture 16.
>
> *Source: PHY 513 Lecture 15, transcript (1:20:00) · the user's PHY 513 notes, Ch. 15 §15.9 (opening paragraph)*

^rem-c6b-8-3

> [!remark] Remark: Summary: from amplitudes to observables
> - $\hat S = \mathbb 1 + i\hat T$ and $\langle f|i\hat T|i\rangle = (2\pi)^4\delta^4(p_i - p_f)\,i\mathcal M$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]). "$\mathcal M$ is wave function overlap ${}_{\rm out}\langle\vec p_1\vec p_2\ldots|\vec k_A\vec k_B\ldots\rangle_{\rm in}$ except for removal of: trivial scattering (in = out); overall $\delta$-function that conserves 4-momentum." "Central goal of QFT: compute and analyze $\mathcal M$."
> - Cross section: $d\sigma = \frac{1}{2E_A2E_B|\mathbf v_A - \mathbf v_B|}|\mathcal M|^2d\Pi_n$ ([[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-2|Theorem §C6b.5.2]]); the denominator is the kinematics of the two initial particles, invariant under boosts along the beam ([[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-2|Theorem §C6b.6.2]]).
> - Phase space: $d\Pi_n$ ([[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^def-c6b-6-1|Def. §C6b.6.1]]); two bodies in the centre-of-mass frame $\int d\Omega\,\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}}$ ([[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-5|Theorem §C6b.6.5]]); all masses equal, $(d\sigma/d\Omega)_{\rm cm} = |\mathcal M|^2/(64\pi^2E_{\rm cm}^2)$ ([[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-8|Theorem §C6b.6.8]]).
> - Decay: $d\Gamma = \frac{1}{2m_A}|\mathcal M|^2d\Pi_n$ ([[§C6b.7 Decay Rates and Widths#^thm-c6b-7-4|Theorem §C6b.7.4]]); in a propagator the width appears as $p^2 - m^2 + im\Gamma$, and a moving particle decays at the time-dilated rate $\frac{m}{E}\Gamma$ ([[§C6b.7 Decay Rates and Widths#^thm-c6b-7-9|Theorem §C6b.7.9]]).
> - Amplitudes are correlation functions with the external propagators stripped off ([[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-1|Theorem §C6b.8.1]]).
>
> *Source: PHY 513 Lecture 15, slides 24–25 ("Summary I: Formula for Cross-section", "Summary II: Relativistic Phase Space Factor") · the user's PHY 513 notes, Ch. 15 §15.10, Principle "From amplitudes to observables" (a summary: a remark here)*

^rem-c6b-8-4

> [!remark] Remark: Next: Feynman rules for amplitudes
> Lecture 16 (Nov 2, PS §4.6) justifies the stripping rule and gives Feynman rules for amplitudes, first in $\phi^4$ theory, then for Yukawa theory and QED, where external lines carry spinors and polarization vectors instead of propagators (QFT C7, planned). PS start from the same definition, $\langle\mathbf p_1\mathbf p_2\cdots|S|\mathbf k_A\mathbf k_B\rangle = \lim_{T\to\infty}\langle\mathbf p_1\mathbf p_2\cdots|e^{-iH(2T)}|\mathbf k_A\mathbf k_B\rangle$ (eq. (4.87)), and relate the interacting states to free ones by the same $T \to \infty(1 - i\epsilon)$ device as for the vacuum (eq. (4.88); [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-1|Theorem §C6a.4.1]]).
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.10 (paragraph "Next.") · PS §4.6, p. 108, eqs. (4.87)–(4.88) · PHY 513 Lecture 15, transcript ("which you don't really [know], but you will on Monday") · [[PHY 513 Course Log]] (Lecture 16: PS §4.6)*

^rem-c6b-8-5

> [!remark] Remark: Yu's route
> Yu reaches amplitudes from correlation functions through the LSZ reduction formula: the $T$-matrix element is the Fourier transform of the $(n + m)$-point function with a Klein–Gordon operator $\frac{i}{\sqrt Z}(\partial^2 + m^2)$ applied to each external point (eq. (10.107)), equivalently the residue of its poles (eq. (10.121)). He checks it on the $\phi^4$ vertex ($\phi\phi \to \phi\phi$, eqs. (10.224)–(10.229); $(\partial^2 + m^2)D_F = -i\delta^4$, eq. (10.226), removes each external propagator in position space) and states the general rule as "amputated" (切断) diagrams with a factor $\sqrt Z$ per external line (§10.5.3, eqs. (10.230)–(10.235)), for Dirac and vector fields as well (eqs. (10.236)–(10.237)). His momentum-space Feynman rules for $\mathcal M$ (§7.2–§7.3) come first in his order and are justified by this later; the course states the rule now and proves it in Lecture 16.
>
> *Source: Yu §10.3, pp. 454–456, eqs. (10.107), (10.121); §10.5.2–§10.5.3, pp. 474–477, eqs. (10.224)–(10.237)*

^rem-c6b-8-6

> [!remark]- Connections
> - The external propagators that are stripped are the poles of the correlation functions at the particle masses; the same poles appear in the spectral picture of the two-point function, with residue $Z$ — QFT C10 (planned), [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]].
> - In position space, stripping a propagator is applying $(\partial^2 + m^2)$, since $D_F$ is a Green's function of the Klein–Gordon operator — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription|§C2b.6]].
> - "Fully connected" is stronger than the "attached" of the bubble cancellation; disconnected pieces of the correlator are the $\mathbb 1$ and products of smaller processes — [[§C6a.11 The iε Limit and Vacuum Bubbles#^cau-c6a-11-1|§C6a.11, Caution: Connected means attached to an external point]].
> - The symmetry factor of the diagram and the identical-particle factor of the final state enter the same cross section separately — [[§C6a.8 Position-Space Feynman Rules#^def-c6a-8-1|Def. §C6a.8.1]], [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-4|Theorem §C6b.5.4]].
> - The contraction of a field with an outgoing particle, which the amputation rule hides, is written out for $n$ particles in both normalizations in [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^lem-c6b-9-4|Lemma §C6b.9.4]]; with it the decay $\Phi \to \phi\phi$ is computed directly from $\langle f|T\exp|i\rangle$ — [[§C6b.7 Decay Rates and Widths#^ex-c6b-7-1|Example §C6b.7.1]].
> - The first-order amplitude $-i\lambda$ is the analogue of the first Born approximation of quantum mechanics, where the $T$-matrix is replaced by the potential — [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-5|QM Theorem §C10.1.5]].
