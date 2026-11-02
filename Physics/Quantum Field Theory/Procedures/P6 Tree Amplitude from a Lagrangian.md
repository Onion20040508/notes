---
type: procedure
subject: "[[Quantum Field Theory]]"
level: C
tags: [quantum-field-theory, procedure]
---
# P6 Tree Amplitude from a Lagrangian

Turns an interaction Lagrangian and a process into the lowest-order amplitude $i\mathcal M$: which processes the interaction allows, which diagrams contribute, and the value of each. Inputs: a Lagrangian of scalar fields with a polynomial interaction without derivatives, and the incoming and outgoing particles with their momenta. Derivations are in the sections linked at each step; conventions in [[Larsen PHY 513]]; the output feeds [[P7 From ℳ to σ or Γ]].

## Steps

1. **Read the Lagrangian.** Separate $\mathcal L = \mathcal L_0 + \mathcal L_{\rm int}$; list the fields, their masses and kinds (a real field; $\phi$ and $\phi^\dagger$ of a complex field), and write $\mathcal L_{\rm int} = -\sum_tg_tM_t$ with monomials $M_t = \prod_k\phi_k^{m_{t,k}}$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]]). Name the setup: a Model box of the theory ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]], [[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2|Model §C6a.8.2]], [[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-3|Model §C6a.8.3]], [[§C6b.8 Decay Rates and Widths#^mod-c6b-8-6|Model §C6b.8.6]]), an instance of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]. ^p6-1

2. **Vertex factors.** Each monomial is a vertex with $r_t = \sum_km_{t,k}$ legs and factor $-ig_t\prod_km_{t,k}!$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]): $-\frac{g}{3!}\phi^3 \to -ig$, $-\frac{\lambda}{4!}\phi^4 \to -i\lambda$, $-\mu\Phi\phi^2 \to -2i\mu$, $-\frac\lambda4(\phi^\dagger\phi)^2 \to -i\lambda$. ^p6-2

3. **Enumerate the diagrams.** *First order:* list every split of the legs of $M_t$ into incoming particles, outgoing particles and pairs closed into loops, $\langle f|i\hat T^{(1)}|i\rangle = -ig\prod_k\frac{m_k!}{2^{\ell_k}\ell_k!}D_F^{(m_k)}(0)^{\ell_k}(2\pi)^4\delta^4(\cdots)$ ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-4|Theorem §C6b.2.4]]), then keep what energy-momentum conservation allows on shell ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-5|Theorem §C6b.2.5]]). *Given order* $\prod_tg_t^{n_t}$: count legs $r = \sum_tn_tr_t$, external particles $E$, internal lines $I = \frac{r - E}{2}$ (none if $r - E$ is odd), loops $L = I - \sum_tn_t + 1$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 1–2); draw every fully connected diagram with $L = 0$ whose external points are the labelled particles ([[§C6b.2 Matrix Elements between Particle States#^def-c6b-2-1|Def. §C6b.2.1]]): distribute the particles over the vertices and discard the distributions that leave legs of one vertex to pair among themselves (a vertex with all its legs on particles is a piece of its own: [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 3). ^p6-3

4. **Apply the tree rules to each diagram.** External line $1$; vertex $-ig_t\prod_km_{t,k}!$; internal line $\frac{i}{q^2 - m_j^2 + i\varepsilon}$ with $q$ fixed by conservation at the vertices; $S = 1$ ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-7|Theorem §C6b.2.7]], [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-6|Theorem §C6b.2.6]]). ^p6-4

5. **Sum the channels.** Add all diagrams of the order: for $2 \to 2$ with one internal line, the $s$-, $t$- and $u$-channels, $q = p_A + p_B$, $p_A - p_1$, $p_A - p_2$ ([[§C6b.2 Matrix Elements between Particle States#^ex-c6b-2-4|Example §C6b.2.4]]). For scalar fields every diagram enters with the same sign; relative signs between diagrams come with fermions (the ordering rule of Yu §7.1, p. 268; QFT C7, planned). For identical final particles the exchange $p_1 \leftrightarrow p_2$ is already in the list (it maps $t$ to $u$); it is not added again. ^p6-5

6. **Read off $i\mathcal M$.** The sum multiplies $(2\pi)^4\delta^4(\sum p_{\rm in} - \sum p_{\rm out})$; strip it ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]) and check the dimension, $[\mathcal M] = 4 - N$ for $N$ external particles ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]]). ^p6-6

7. **State the scope.** The result is the lowest order: free relativistic states over $|0\rangle$ stand for the in and out states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]]); beyond it external lines carry $\sqrt Z$ and the physical mass ([[§C6b.9 Amplitudes from Correlation Functions#^cau-c6b-9-2|§C6b.9, Caution: The rule is stated at lowest order]]); an unstable initial particle is outside the asymptotic setup ([[§C6b.8 Decay Rates and Widths#^cau-c6b-8-1|§C6b.8, Caution: Free states in a decay amplitude]]). ^p6-7

## Instances

| Theory, process | Steps 1–2 | Step 3 | Steps 4–6: $i\mathcal M$ |
| --- | --- | --- | --- |
| $\phi^4$, $\phi\phi \to \phi\phi$ | [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1\|Model §C6a.1.1]]; $-i\lambda$ | first order, table of all splits: [[§C6b.2 Matrix Elements between Particle States#^ex-c6b-2-1\|Example §C6b.2.1]] | $-i\lambda$: [[§C6b.2 Matrix Elements between Particle States#^ex-c6b-2-1\|Example §C6b.2.1]]; by amputation [[§C6b.9 Amplitudes from Correlation Functions#^ex-c6b-9-1\|Example §C6b.9.1]]; used in [[§C6b.11 From the Question to the Formula#^ex-c6b-11-3\|Example §C6b.11.3]] |
| $\Phi\phi^2$, $\Phi \to \phi\phi$ | [[§C6b.8 Decay Rates and Widths#^mod-c6b-8-6\|Model §C6b.8.6]]; $-2i\mu$ | first order, table: [[§C6b.2 Matrix Elements between Particle States#^ex-c6b-2-2\|Example §C6b.2.2]]; allowed iff $M > 2m$ | $-2i\mu$: [[§C6b.8 Decay Rates and Widths#^ex-c6b-8-1\|Example §C6b.8.1]] (Problem Set 8, Problem 4); [[§C6b.11 From the Question to the Formula#^ex-c6b-11-2\|Example §C6b.11.2]] |
| Cubic–quartic, $2 \to 2$ at order $g^2$, $\lambda$ | [[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2\|Model §C6a.8.2]]; $-ig$, $-i\lambda$ | $s$, $t$, $u$, contact: [[§C6b.2 Matrix Elements between Particle States#^ex-c6b-2-4\|Example §C6b.2.4]], [[§C6b.11 From the Question to the Formula#^ex-c6b-11-5\|Example §C6b.11.5]] (Problem Set 8, Problem 2(a)) | structure only: four diagrams, $S = 1$ |
| Cubic–quartic, $2 \to 3$ at order $g\lambda$ | as above | ten diagrams in three classes: [[§C6b.2 Matrix Elements between Particle States#^ex-c6b-2-5\|Example §C6b.2.5]] (Problem Set 8, Problem 2(b)) | structure only, $S = 1$ |
| $\phi^3$, first order | [[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2\|Model §C6a.8.2]] at $\lambda = 0$; $-ig$ | every split forbidden on shell: [[§C6b.2 Matrix Elements between Particle States#^ex-c6b-2-3\|Example §C6b.2.3]] | none: the first process is $2 \to 2$ at order $g^2$ |
| Yukawa, QED | QFT C7–C8 (planned) | | |

## Pitfalls

- **Kinematics before dynamics.** A matrix element that $\mathcal L_{\rm int}$ allows may have no on-shell support: every $1 \to n$ with equal masses, every $0 \to n$ ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-5|Theorem §C6b.2.5]]).
- **The factorials.** The vertex factor is $-ig_t\prod_km_{t,k}!$ whatever the normalization of $\mathcal L_{\rm int}$; a coupling written without $\frac{1}{m!}$ ($\mu\Phi\phi^2$) keeps the $m!$ in the vertex ($-2i\mu$).
- **Fully connected only.** Pieces in which a particle passes by, vacuum bubbles and loops on external legs are not part of $\mathcal M$ ([[§C6b.9 Amplitudes from Correlation Functions#^thm-c6b-9-2|Theorem §C6b.9.2]], [[§C6b.9 Amplitudes from Correlation Functions#^cau-c6b-9-1|§C6b.9, Caution: "Connected" here means fully connected]]).
- **No $\frac{1}{S_{\rm id}}$ in $\mathcal M$.** The identical-particle factor belongs to the integrated rate ([[P7 From ℳ to σ or Γ#^p7-7|P7, step 7]]); tree diagrams have $S = 1$.
- **External momenta are labels.** Exchanging two external particles gives another diagram, not a symmetry ([[§C6b.2 Matrix Elements between Particle States#^def-c6b-2-1|Def. §C6b.2.1]], 1).
