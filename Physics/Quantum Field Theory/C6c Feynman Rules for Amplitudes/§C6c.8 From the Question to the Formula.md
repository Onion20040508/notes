---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6c
section: C6c.8
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route]] · ↑ [[· C6c Feynman Rules for Amplitudes]] · [[§C6d.1 Yukawa Theory]] →

*Sources: PHY 513, Problem Set 8, Problems 2(a), 3(a), 3(d)–(e) and 4 (statements, and the user's solutions, submitted 2026-10-30) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.5, pp. 106–108, eqs. (4.79), (4.84)–(4.86) (page images checked) · Yu Zhao-Huan, 量子场论讲义, §6.5.5, eqs. (6.383), (6.385) (page image checked, PDF p. 261) · PHY 513 Lecture 17, slides 19–20, 23 (Example 6) · the homes cited in each step.*

A problem states a question in words: a probability, a lifetime, a cross section, a correlation function, a list of diagrams. The formula that answers it holds only in one setup, so the question has to be translated before anything is computed: **what is prepared, what is measured, in which states and which vacuum, at which order, and whether the object asked for is an observable at all.** [[§C6a.0 Setups and Observables|§C6a.0]] classified the physical situations by how the interaction behaves in time and listed, in its table "From the question to the object", the object each kind of question asks for. This section works five of those questions through, each as an Example with the same chain of labelled steps: *question as asked → physical situation (Model box) → states and vacuum → the object → normalization and measure → theorems → result → pitfalls.* Every step shows its formula and links its home; nothing that a home derives is derived again. The general method is the list below; the examples are its instances, and every row of the §C6a.0 table links the example or procedure that works it. Three procedures carry the recurring computations: [[P5 Symmetry Factor of a Diagram]], [[P6 Tree Amplitude from a Lagrangian]], [[P7 From ℳ to σ or Γ]].

*Conventions* ([[Larsen PHY 513]]): $|0\rangle$ the free vacuum, $|\Omega\rangle$ the interacting one ([[§C6a.0 Setups and Observables#^cau-c6a-0-1|§C6a.0, Caution: Names for the vacua]]); relativistic states $|\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^\dagger_{\mathbf p}|0\rangle$ unless an example says otherwise ([[§C6c.2 Contractions with External Particles#^cau-c6c-2-1|§C6c.2, Caution: Two normalizations of one-particle states]]); $\hat S = \mathbb 1 + i\hat T$, $\langle f|i\hat T|i\rangle = (2\pi)^4\delta^4(\sum p_{\rm in} - \sum p_{\rm out})\,i\mathcal M$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]); $S_{\rm id}$ the identical-particle factor, $S$ the symmetry factor of a diagram ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^cau-c6b-1-2|§C6b.1, Caution: Four S's]]).

## How to translate a question

1. **Does the interaction switch off?** If $\hat H_{\rm int}(t) = 0$ outside a finite time ([[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]]), $|0\rangle$ and the free Fock states are exact and $\hat S = U(+\infty, -\infty)$ to all orders; if it never does ([[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]), they are not — [[§C6a.0 Setups and Observables#^thm-c6a-0-4|Theorem §C6a.0.4]].
2. **What is prepared and what is measured?** One particle at rest that decays ([[§C6b.9 Decay Rates and Widths#^mod-c6b-9-1|Model §C6b.9.1]]), two particles that collide ([[§C6b.4 Transition Probabilities in a Box#^mod-c6b-4-1|Model §C6b.4.1]], [[§C6b.5 The Cross Section#^mod-c6b-5-1|Model §C6b.5.1]], [[§C6b.6 Wave Packets and the Cross Section#^mod-c6b-6-1|Model §C6b.6.1]]), or the vacuum and a source ([[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-1|Theorem §C6c.7.1]]); a probability is a squared overlap of unit vectors, $P_{fi} = |\langle f|\hat S|i\rangle|^2/(\langle f|f\rangle\langle i|i\rangle)$ — [[§C6b.4 Transition Probabilities in a Box#^def-c6b-4-1|Def. §C6b.4.1]].
3. **Which states, in which normalization?** $\hat a^\dagger|0\rangle$ with $\frac{d^3k}{(2\pi)^3}$, or $\sqrt{2E}\,\hat a^\dagger|0\rangle$ with $\frac{d^3k}{(2\pi)^32E}$, and $\frac{1}{n!}$ for $n$ identical particles — [[§C6c.2 Contractions with External Particles#^cau-c6c-2-1|§C6c.2, Caution: Two normalizations of one-particle states]], [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-5|Theorem §C6c.7.5]].
4. **Which vacuum?** The ground state of the Hamiltonian that acts at early and late times: $|0\rangle$ in Model §C6a.0.1, $|\Omega\rangle$ in Model §C6a.0.3 — [[§C6a.0 Setups and Observables#^thm-c6a-0-4|Theorem §C6a.0.4]], [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^def-c6a-4-1|Def. §C6a.4.1]], [[§C6a.0 Setups and Observables#^cau-c6a-0-1|§C6a.0, Caution: Names for the vacua]].
5. **Which order?** Free states in place of in and out states (the course's prescription: free states dressed by $U(0, -T)$, bubbles omitted) are exact in Model §C6a.0.1 and lowest order in Model §C6a.0.3; beyond it $\sqrt Z$ per external line and the physical mass — [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]], [[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|§C2b.1, Caution: With interactions, the one-particle matrix element carries √Z]], [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]].
6. **Is the object an observable?** Probabilities, rates and cross sections are; a correlation function is not, it is the input of amputation — [[§C6b.1 The S-Matrix and the Invariant Amplitude#^rem-c6b-1-2|§C6b.1, Remark: The fundamental observable?]], [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]].
7. **Are there fermions?** Then the question must also fix the spins and the order in which the external states are written, and the answer has signs: relative signs between diagrams are physical (the statistics of identical particles), the overall sign is a convention that drops out of $|\mathcal M|^2$ — [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]], [[§C6d.5 Second Order#^thm-c6d-5-3|Theorem §C6d.5.3]], [[§C6d.5 Second Order#^rem-c6d-5-1|§C6d.5, Remark: The overall sign is a convention]]; worked in Example §C6c.8.6 (PHY 513 Lecture 17, slide 23).

## A source switched off: how many particles?

> [!example] Example §C6c.8.1: The Probability That a Switched Source Creates 0 or n Particles
> ![[ph-qft-c6b-11-1.svg]]
> *The two connected diagrams of a switched source ([[§C6a.0 Setups and Observables#^thm-c6a-0-5|Theorem §C6a.0.5]]): the line $L$ between two source vertices (crosses, at $x$, $y$) and the line from a source vertex to an outgoing particle $\mathbf k$. Added figure.*
>
> **Question as asked.** "Show that the probability that the source creates no particles at all is $P(0) = \bigl|\langle0|\,T\exp\bigl(i\int d^4x\,j(x)\,\phi_I(x)\bigr)|0\rangle\bigr|^2$ … Show that the probability of producing $n$ particles is $P(n) = \frac{1}{n!}\lambda^ne^{-\lambda}$", for $H_{\rm int} = -\int d^3x\,j(x)\phi(x)$ with "$j(x)$ … nonvanishing only during a finite interval of time, so that asymptotic in and out states can be defined" (PHY 513, Problem Set 8, Problem 3(a), (e)).
>
> **Situation** (question 1: yes, it switches off). An external apparatus acts for a finite time, [[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]] (the same system as [[§C2b.5 Green's Functions and Contours#^mod-c2b-5-1|Model §C2b.5.1]]):
>
> $$
> \hat H(t) = \hat H_0 + \hat H_{\rm int}(t) , \qquad \hat H_{\rm int}(t) = -\int d^3x\,j(t, \mathbf x)\,\hat\phi_S(\mathbf x) = 0 \quad (t \notin [t_1, t_2]) .
> $$
>
> **States and vacuum** (questions 3–4). The vacuum of a setup is the ground state of the Hamiltonian at early and late times ([[§C6a.0 Setups and Observables#^der-c6a-0-4|Derivation §C6a.0.4]], "What the derivation shows"). Here that Hamiltonian is $\hat H_0$, so the in and out vacuum is $|0\rangle$ exactly, $\hat H_0|0\rangle = 0$ ([[§C6a.0 Setups and Observables#^thm-c6a-0-4|Theorem §C6a.0.4]], 1). The interacting vacuum $|\Omega\rangle$ ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^def-c6a-4-1|Def. §C6a.4.1]]) is the ground state of a time-independent $\hat H$; no such $\hat H$ acts here, so there is nothing to project onto and no $T \to \infty(1 - i\varepsilon)$. The user's solution: "Since $j$ vanishes outside a finite time interval, the in and out states with no particles are the free vacuum $|0\rangle$, with $\hat H_0|0\rangle = 0$." The final states are free Fock states in the problem's normalization, $|\mathbf k_1\cdots\mathbf k_n\rangle = \hat a^\dagger_{\mathbf k_1}\cdots\hat a^\dagger_{\mathbf k_n}|0\rangle$, not relativistic.
>
> **Object.** With $\hat H_I(t) = e^{i\hat H_0t}\hat H_{\rm int}(t)e^{-i\hat H_0t}$ ([[§C6a.2 The Interaction Picture#^def-c6a-2-3|Def. §C6a.2.3]]) and the time-ordered exponential ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-8|Theorem §C6a.3.8]]; [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-1|Theorem §C6c.7.1]]):
>
> $$
> \hat H_I(t) = -\int d^3x\,j(t, \mathbf x)\,\hat\phi_I(t, \mathbf x) , \qquad \hat S = U(+\infty, -\infty) = T\Bigl\{\exp\Bigl[-i\int dt\,\hat H_I(t)\Bigr]\Bigr\} = T\Bigl\{\exp\Bigl[i\int d^4x\,j(x)\,\hat\phi_I(x)\Bigr]\Bigr\} ,
> $$
>
> $$
> \mathcal A(0) = \langle0|\hat S|0\rangle , \qquad \mathcal A(\mathbf k_1, \dots, \mathbf k_n) = \langle\mathbf k_1\cdots\mathbf k_n|\hat S|0\rangle .
> $$
>
> No denominator: $\hat S$ is unitary and $\sum_fP(f) = \langle0|\hat S^\dagger\hat S|0\rangle = 1$ ([[§C6a.0 Setups and Observables#^der-c6a-0-4|Derivation §C6a.0.4]], Step 5). In the user's words: "The derivation of (a) holds for any free final state, since after the source is switched off the interaction-picture state is $\hat U(+\infty, -\infty)|0\rangle$."
>
> **Normalization and measure** (question 3). In the $\hat a^\dagger|0\rangle$ normalization ([[§C6c.2 Contractions with External Particles#^cau-c6c-2-1|§C6c.2, Caution: Two normalizations of one-particle states]]; [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]]; [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-5|Theorem §C6c.7.5]]):
>
> $$
> \langle\mathbf p|\mathbf k\rangle = (2\pi)^3\delta^3(\mathbf p - \mathbf k) , \qquad \langle\mathbf k|\hat\phi_I(x)|0\rangle = \frac{e^{ik\cdot x}}{\sqrt{2E_{\mathbf k}}} , \qquad \mathbb 1_n = \frac{1}{n!}\int\prod_{i=1}^n\frac{d^3k_i}{(2\pi)^3}\,|\mathbf k_1\cdots\mathbf k_n\rangle\langle\mathbf k_1\cdots\mathbf k_n| ,
> $$
>
> so the probability of the $n$-particle subspace is
>
> $$
> P(n) = \langle0|\hat S^\dagger\,\mathbb 1_n\,\hat S|0\rangle = \frac{1}{n!}\int\prod_{i=1}^n\frac{d^3k_i}{(2\pi)^3}\,\bigl|\mathcal A(\mathbf k_1, \dots, \mathbf k_n)\bigr|^2 , \qquad P(0) = |\mathcal A(0)|^2 .
> $$
>
> **Theorems, two routes.** *Dyson series with source vertices* ([[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route|§C6c.7]]): the only connected diagrams are the line between two sources and the line from a source to an outgoing particle ([[§C6a.0 Setups and Observables#^thm-c6a-0-5|Theorem §C6a.0.5]]), and ([[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-2|Theorem §C6c.7.2]], [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-3|Theorem §C6c.7.3]], [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-6|Theorem §C6c.7.6]])
>
> $$
> \mathcal A(0) = e^{\mathcal A_2} , \qquad 2\operatorname{Re}\mathcal A_2 = -\lambda , \qquad \mathcal A(\mathbf k_1, \dots, \mathbf k_n) = \prod_{i=1}^n\frac{i\tilde j(k_i)}{\sqrt{2E_{\mathbf k_i}}}\,e^{\mathcal A_2} , \qquad k_i^0 = E_{\mathbf k_i} .
> $$
>
> *Heisenberg field and the retarded function* ([[§C2b.8 Particle Production by a Classical Source|§C2b.8]]): the state stays $|0\rangle$ and the late-time operators shift ([[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-1|Theorem §C2b.8.1]], [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-2|Theorem §C2b.8.2]]),
>
> $$
> \hat b_{\mathbf p} = \hat a_{\mathbf p} + \frac{i\tilde j(p)}{\sqrt{2E_{\mathbf p}}} , \qquad \hat b_{\mathbf p}|0\rangle = \frac{i\tilde j(p)}{\sqrt{2E_{\mathbf p}}}\,|0\rangle :
> $$
>
> a coherent state of the out-particles, Poisson with mean $\bar N = \lambda$ ([[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-3|Theorem §C2b.8.3]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-6|Theorem §C2a.6.6]]).
>
> **Result.** $|\mathcal A|^2 = \prod_i\frac{|\tilde j(k_i)|^2}{2E_{\mathbf k_i}}\,e^{2\operatorname{Re}\mathcal A_2}$, and each momentum integral gives $\lambda$:
>
> $$
> P(n) = \frac{e^{-\lambda}}{n!}\prod_{i=1}^n\int\frac{d^3k_i}{(2\pi)^3}\frac{|\tilde j(k_i)|^2}{2E_{\mathbf k_i}} = \frac{\lambda^n}{n!}\,e^{-\lambda} , \qquad P(0) = e^{-\lambda} , \qquad \lambda = \int\frac{d^3k}{(2\pi)^3}\frac{|\tilde j(k)|^2}{2E_{\mathbf k}}\Big|_{k^0 = E_{\mathbf k}} ,
> $$
>
> with the checks $\sum_nP(n) = 1$ and $\bar N = \lambda$ ([[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-7|Theorem §C6c.7.7]]).
>
> **Pitfalls.**
> - *The master formula's habit.* Dividing by the vacuum amplitude, as for a correlator ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-6|Theorem §C6a.4.6]]), would give "$P(0)$" $= |\langle0|\hat S|0\rangle/\langle0|\hat S|0\rangle|^2 = 1$. Here $\langle0|\hat S|0\rangle = \mathcal A(0)$ is itself the physical amplitude, $|\mathcal A(0)| = e^{-\lambda/2} < 1$.
> - *Mixed normalizations.* The amplitudes above with the relativistic measure $\frac{d^3k}{(2\pi)^32E_{\mathbf k}}$ give a wrong factor $\frac{1}{2E_{\mathbf k}}$ per particle ([[§C6c.2 Contractions with External Particles#^cau-c6c-2-1|§C6c.2, Caution: Two normalizations of one-particle states]]).
> - *The $\frac{1}{n!}$.* Integrating each $\mathbf k_i$ freely counts each state $n!$ times; without the $\frac{1}{n!}$, $\sum_n\lambda^ne^{-\lambda} = \frac{e^{-\lambda}}{1 - \lambda} \ne 1$ for $\lambda < 1$, and the sum diverges for $\lambda \ge 1$.
> - *Where $\lambda$ comes from.* Only $\operatorname{Re}\mathcal A_2$ enters $P(0)$, and it is the $\delta(p^2 - m^2)$ part of the $i\varepsilon$ of $D_F$ ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]], 1; [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^der-c6c-7-2|Derivation §C6c.7.2]], Step 5): only the on-shell part of the source radiates.
> - *A static source is another question.* A source that never switches off (★ [[§C6a.0 Setups and Observables#^mod-c6a-0-2|Model §C6a.0.2]]) creates no particles, $\hat S = \mathbb 1$; it moves the vacuum instead.
>
> *Source: PHY 513, Problem Set 8, Problem 3 (statement; the user's solution, parts (a), (d), (e), as written) · PS Problem 4.1 · homes as linked*

^ex-c6c-8-1

## A decay: the lifetime

> [!example] Example §C6c.8.2: The Lifetime of Φ in the Φφ² Theory
> ![[ph-qft-c6b-11-2.svg]]
> *The one tree diagram of $\Phi \to \phi\phi$ at order $\mu$: $\Phi$ (dashed, momentum $K$) in, the two $\phi$'s ($p_1$, $p_2$) out, vertex factor $-2i\mu$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]). Added figure.*
>
> **Question as asked.** "Assume that the Lagrangian responsible for this decay is $\mathcal L = \frac12(\partial_\mu\Phi)^2 - \frac12M^2\Phi^2 + \frac12(\partial_\mu\phi)^2 - \frac12m^2\phi^2 - \mu\,\Phi\phi^2$ … Assuming that [$M > 2m$] is met, calculate the lifetime of the $\Phi$ to the lowest order in $\mu$" (PHY 513, Problem Set 8, Problem 4 = PS Problem 4.2).
>
> **Situation** (question 1: no, it never switches off; question 2: one $\Phi$ at rest, its decays counted per unit time). [[§C6b.9 Decay Rates and Widths#^mod-c6b-9-7|Model §C6b.9.7]], an instance of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]], with the decay setup [[§C6b.9 Decay Rates and Widths#^mod-c6b-9-1|Model §C6b.9.1]]:
>
> $$
> \hat H_{\rm int} = \mu\int d^3x\,\hat\Phi_S(\mathbf x)\,\hat\phi_S(\mathbf x)^2 \quad\text{for all } t , \qquad \Gamma = \frac{\text{decays per unit time}}{\text{number of }\Phi\text{ at rest}} , \qquad \tau = \frac1\Gamma
> $$
>
> ([[§C6b.9 Decay Rates and Widths#^def-c6b-9-1|Def. §C6b.9.1]]). The potential is unbounded below (assumption 2 of Model §C6b.9.7): only the lowest order has a meaning.
>
> **States and vacuum** (questions 3–5). Free relativistic states over the free vacuum $|0\rangle$ in place of the in and out states, valid at lowest order ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]; [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]]), as the decay formula needs ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]):
>
> $$
> |\mathbf K\rangle_\Phi = \sqrt{2E^\Phi_{\mathbf K}}\,\hat b^\dagger_{\mathbf K}|0\rangle , \qquad |\mathbf p_1\mathbf p_2\rangle = \sqrt{2E_{\mathbf p_1}}\sqrt{2E_{\mathbf p_2}}\,\hat a^\dagger_{\mathbf p_1}\hat a^\dagger_{\mathbf p_2}|0\rangle , \qquad K = (M, \mathbf 0) .
> $$
>
> Kinematics first: $1 \to 2$ is allowed iff $M > 2m$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], 2). The user's solution: "The interaction does not switch off, so the free states are not exactly the asymptotic states; to lowest order in $\mu$ this does not matter."
>
> **Object.** The first-order matrix element and the amplitude it defines ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]); the two $\phi$ legs take $\mathbf p_1$, $\mathbf p_2$ in two ways ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-4|Example §C6c.4.4]]):
>
> $$
> \langle\mathbf p_1\mathbf p_2|i\hat T^{(1)}|\mathbf K\rangle_\Phi = -i\mu\int d^4x\,\langle\mathbf p_1\mathbf p_2|\hat\Phi_I(x)\hat\phi_I(x)^2|\mathbf K\rangle_\Phi = -i\mu\int d^4x\;2\,e^{i(p_1 + p_2 - K)\cdot x} = (2\pi)^4\delta^4(K - p_1 - p_2)\,i\mathcal M ,
> $$
>
> $$
> i\mathcal M = -i\mu\cdot1!\,2! = -2i\mu .
> $$
>
> **Normalization and measure** (question 3). The decay formula ([[§C6b.9 Decay Rates and Widths#^thm-c6b-9-5|Theorem §C6b.9.5]]; PS (4.86)) and the $\frac{1}{2!}$ of two identical $\phi$'s ([[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-5|Theorem §C6c.7.5]], [[§C6b.7 Evaluating the Cross Section#^thm-c6b-7-4|Theorem §C6b.7.4]]):
>
> $$
> d\Gamma = \frac{1}{2M}\,|\mathcal M|^2\,d\Pi_2 , \qquad d\Pi_2 = \frac{d^3p_1}{(2\pi)^32E_1}\,\frac{d^3p_2}{(2\pi)^32E_2}\,(2\pi)^4\delta^4(K - p_1 - p_2) , \qquad \Gamma = \frac{1}{2!}\int d\Gamma .
> $$
>
> The $\frac{1}{2M}$ is the $\frac{1}{2E_K}$ of the norm of the initial state at rest ([[§C6b.9 Decay Rates and Widths#^thm-c6b-9-3|Theorem §C6b.9.3]]).
>
> **Theorems.** Two-body phase space at rest ([[§C6b.9 Decay Rates and Widths#^thm-c6b-9-6|Theorem §C6b.9.6]], 1 and 3; Yu (6.383), (6.385)):
>
> $$
> |\mathbf p_1| = \frac M2\,\beta , \qquad \int d\Pi_2 = \frac{|\mathbf p_1|}{4\pi M} = \frac{\beta}{8\pi} , \qquad \beta = \sqrt{1 - \frac{4m^2}{M^2}} .
> $$
>
> **Result.** $|\mathcal M|^2 = 4\mu^2$ does not depend on the direction, so
>
> $$
> \Gamma = \frac12\cdot\frac{1}{2M}\cdot4\mu^2\cdot\frac{\beta}{8\pi} = \frac{\mu^2}{8\pi M}\sqrt{1 - \frac{4m^2}{M^2}} , \qquad \tau = \frac1\Gamma = \frac{8\pi M^2}{\mu^2\sqrt{M^2 - 4m^2}} ,
> $$
>
> the result of [[§C6b.9 Decay Rates and Widths#^ex-c6b-9-1|Example §C6b.9.1]] (the user's solution, step by step). Check: $[\mathcal M] = 4 - 3 = 1 = [\mu]$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|Theorem §C6b.1.5]]), $[\Gamma] = 2 - 1 = 1$.
>
> **Pitfalls.**
> - *The decaying state is not an asymptotic state.* "Since an unstable particle cannot be sent into the infinitely distant past, our definition (4.73) of $\mathcal M(m_A \to \{p_f\})$ in terms of the $S$-matrix makes no sense in this context. Nevertheless formula (4.86) is correct, when $\mathcal M$ is computed according to the Feynman rules" (PS pp. 107–108); $\Phi$ violates assumption 2 of Model §C6a.0.3 ([[§C6b.9 Decay Rates and Widths#^cau-c6b-9-1|§C6b.9, Caution: Free states in a decay amplitude]], [[§C6b.9 Decay Rates and Widths#^cau-c6b-9-2|§C6b.9, Caution: "Corollary of studying interacting wave function (2nd term)"]]).
> - *Two different 2's.* The $2 = 2!$ in $\mathcal M$ counts the ways two distinct particles attach to the two $\phi$ legs (amplitude); the $\frac{1}{2!}$ in $\Gamma$ removes the double counting of $|\mathbf p_1\mathbf p_2\rangle = |\mathbf p_2\mathbf p_1\rangle$ (rate). Together $\frac{1}{2!}|\mathcal M|^2 = 2\mu^2$; dropping one changes $\Gamma$ by a factor 2 or 4.
> - *The frame.* $\frac{1}{2M}$ holds at rest; in a frame where $\Phi$ moves the rate is $\frac{1}{2E_K}|\mathcal M|^2d\Pi_2 = \Gamma/\gamma$, time dilation ([[§C6b.9 Decay Rates and Widths#^thm-c6b-9-11|Theorem §C6b.9.11]]); $\tau$ is the rest-frame lifetime.
> - *The normalization.* With $\hat a^\dagger|0\rangle$ states the matrix element loses $\sqrt{2E}$ per particle and the formula of Theorem §C6b.9.5 no longer applies ([[§C6c.2 Contractions with External Particles#^cau-c6c-2-1|§C6c.2, Caution: Two normalizations of one-particle states]]).
>
> *Source: PHY 513, Problem Set 8, Problem 4 (statement; the user's solution, as written) · PS §4.5, pp. 107–108, eq. (4.86) · Yu §6.5.5, eqs. (6.383), (6.385) · homes as linked*

^ex-c6c-8-2

## A collision: the cross section

> [!example] Example §C6c.8.3: dσ/dΩ for φφ → φφ in φ⁴ Theory
> ![[ph-qft-c6b-11-3.svg]]
> *The one diagram of $\phi\phi \to \phi\phi$ at order $\lambda$: $p_A$, $p_B$ in, $p_1$, $p_2$ out, all on one vertex, $i\mathcal M = -i\lambda$, $S = 1$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]]). Added figure.*
>
> **Question as asked.** "What are $(d\sigma/d\Omega)_{\rm cm}$ and $\sigma$ for $\phi\phi \to \phi\phi$ in $\phi^4$ theory at lowest order?" (the lecture's first cross section, [[§C6c.1 Amplitudes from Correlation Functions#^ex-c6c-1-2|Example §C6c.1.2]]).
>
> **Situation** (question 1: no; question 2: two particles collide, the final momenta are counted per unit time and per unit flux). [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]], an instance of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]], at lowest order; the experiment is [[§C6b.4 Transition Probabilities in a Box#^mod-c6b-4-1|Model §C6b.4.1]] (two particles in a box) with [[§C6b.5 The Cross Section#^mod-c6b-5-1|Model §C6b.5.1]] (beam on a fixed target), or the wave packets of [[§C6b.6 Wave Packets and the Cross Section#^mod-c6b-6-1|Model §C6b.6.1]].
>
> **States and vacuum** (questions 3–5). Free, relativistic, over $|0\rangle$, lowest order ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]; [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]]; Model §C6b.4.1, *Applies*):
>
> $$
> |i\rangle = \sqrt{2E_A}\sqrt{2E_B}\,\hat a^\dagger_{\mathbf p_A}\hat a^\dagger_{\mathbf p_B}|0\rangle , \qquad |f\rangle = \sqrt{2E_1}\sqrt{2E_2}\,\hat a^\dagger_{\mathbf p_1}\hat a^\dagger_{\mathbf p_2}|0\rangle , \qquad \{\mathbf p_1, \mathbf p_2\} \ne \{\mathbf p_A, \mathbf p_B\} .
> $$
>
> **Object.** The transition probability ([[§C6b.4 Transition Probabilities in a Box#^def-c6b-4-1|Def. §C6b.4.1]]); for $f \ne i$ only $i\hat T$ contributes ([[§C6b.4 Transition Probabilities in a Box#^thm-c6b-4-2|Theorem §C6b.4.2]], 1), and the four particles attach to the four legs in $4!$ ways, the only connected, amputated diagram at this order ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]]; the other first-order terms are the $\mathbb 1$ and a bubble, [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]]; [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]]; by amputation, [[§C6c.1 Amplitudes from Correlation Functions#^ex-c6c-1-1|Example §C6c.1.1]]):
>
> $$
> P_{fi} = \frac{|\langle f|i\hat T|i\rangle|^2}{\langle i|i\rangle\,\langle f|f\rangle} , \qquad \langle f|i\hat T|i\rangle = (2\pi)^4\delta^4(p_A + p_B - p_1 - p_2)\,i\mathcal M , \qquad i\mathcal M = -\frac{i\lambda}{4!}\cdot4! = -i\lambda .
> $$
>
> **Normalization and measure** (box route). The squared delta, $(2\pi)^4\delta^4(0) = \tilde V\tilde T$ ([[§C6b.4 Transition Probabilities in a Box#^thm-c6b-4-2|Theorem §C6b.4.2]], 2), the norms ([[§C6b.4 Transition Probabilities in a Box#^thm-c6b-4-3|Theorem §C6b.4.3]]), the rate and the final states per $d^3p$ ([[§C6b.4 Transition Probabilities in a Box#^thm-c6b-4-4|Theorem §C6b.4.4]]–[[§C6b.4 Transition Probabilities in a Box#^thm-c6b-4-6|Theorem §C6b.4.6]]), then the flux $|\mathbf v_B|/\tilde V$ of one $B$ per box in the rest frame of $A$ ([[§C6b.5 The Cross Section#^thm-c6b-5-3|Theorem §C6b.5.3]]) and the invariant form ([[§C6b.5 The Cross Section#^thm-c6b-5-4|Theorem §C6b.5.4]], [[§C6b.5 The Cross Section#^thm-c6b-5-6|Theorem §C6b.5.6]], 2; PS (4.79)):
>
> $$
> P_{fi} = \frac{\tilde V\tilde T\,(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2)\,\lambda^2}{4E_AE_B\tilde V^2\cdot2E_1\tilde V\cdot2E_2\tilde V} , \qquad dR = \frac{\tilde V\,d^3p_1}{(2\pi)^3}\,\frac{\tilde V\,d^3p_2}{(2\pi)^3}\,\frac{P_{fi}}{\tilde T} = \frac{\lambda^2\,d\Pi_2}{4E_AE_B\tilde V} ,
> $$
>
> $$
> d\sigma = \frac{dR\,\tilde V}{|\mathbf v_B|} = \frac{|\mathcal M|^2\,d\Pi_2}{4E_AE_B|\mathbf v_B|} \;\longrightarrow\; d\sigma = \frac{|\mathcal M|^2\,d\Pi_2}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|} \quad(\text{collinear beams, any frame}) .
> $$
>
> **Theorems.** Two-body phase space in the centre-of-mass frame, $\int d\Pi_2\,F = \int d\Omega\,\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}}F$ ([[§C6b.8 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-8-5|Theorem §C6b.8.5]]). All masses equal: $|\mathbf p_1| = |\mathbf p_A| = |\mathbf p_B| \equiv p$ and
>
> $$
> 2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B| = 4E_AE_B\Bigl(\frac{p}{E_A} + \frac{p}{E_B}\Bigr) = 4p\,(E_A + E_B) = 4p\,E_{\rm cm} \quad\Longrightarrow\quad \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \frac{|\mathcal M|^2}{4pE_{\rm cm}}\cdot\frac{p}{16\pi^2E_{\rm cm}} = \frac{|\mathcal M|^2}{64\pi^2E_{\rm cm}^2}
> $$
>
> ([[§C6b.8 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-8-7|Theorem §C6b.8.7]], [[§C6b.8 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-8-8|Theorem §C6b.8.8]]; PS (4.84)–(4.85)).
>
> **Result.** With $|\mathcal M|^2 = \lambda^2$ and $S_{\rm id} = 2!$ for the total cross section ([[§C6b.7 Evaluating the Cross Section#^thm-c6b-7-4|Theorem §C6b.7.4]]):
>
> $$
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \frac{\lambda^2}{64\pi^2E_{\rm cm}^2} , \qquad \sigma = \frac{1}{2!}\int d\Omega\,\frac{\lambda^2}{64\pi^2E_{\rm cm}^2} = \frac12\cdot4\pi\cdot\frac{\lambda^2}{64\pi^2E_{\rm cm}^2} = \frac{\lambda^2}{32\pi E_{\rm cm}^2} ,
> $$
>
> the vault's [[§C6c.1 Amplitudes from Correlation Functions#^ex-c6c-1-2|Example §C6c.1.2]] (the two homes agree) and Lecture 16, slide 19. Check: $[\lambda] = 0$, $[\sigma] = -2$, an area. No angular dependence (spinless particles, lowest order) and $E_{\rm cm}^{-2}$ from dimensional analysis ([[§C6b.8 Lorentz Invariance and Two-Body Phase Space#^rem-c6b-8-2|§C6b.8, Remark: Why 1/E²: dimensional analysis]]).
>
> **Pitfalls.**
> - *Free states are lowest order.* Beyond it each external line carries $\sqrt Z$ and the physical mass, and loops on external legs are not part of $\mathcal M$ ([[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|§C2b.1, Caution: With interactions, the one-particle matrix element carries √Z]]; [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]).
> - *Disconnected pieces are not scattering.* The pieces of the four-point function in which the particles pass by are supported on $\{p_1, p_2\} = \{p_A, p_B\}$ or vanish, and carry two deltas instead of one ([[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-2|Theorem §C6c.1.2]]); they belong to the $\mathbb 1$ of $\hat S$.
> - *The squared delta is not an error.* One factor $(2\pi)^4\delta^4(0) = \tilde V\tilde T$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10|Theorem §CA.3.10]]) is removed by dividing by the time and the flux; it is not dropped by hand.
> - *$\frac{1}{S_{\rm id}}$ belongs to $\sigma$, not to $d\sigma/d\Omega$* at a given angle ([[§C6b.7 Evaluating the Cross Section#^thm-c6b-7-4|Theorem §C6b.7.4]]), and it is not the symmetry factor $S = 1$ of the diagram ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^cau-c6b-1-2|§C6b.1, Caution: Four S's]]).
> - *$|\mathbf v_A - \mathbf v_B|$ is not a relative velocity* ([[§C6b.8 Lorentz Invariance and Two-Body Phase Space#^cau-c6b-8-1|§C6b.8, Caution: The velocity difference is not a relative velocity]]).
>
> *Source: PS §4.5, pp. 106–107, eqs. (4.79), (4.84)–(4.85); §4.6, p. 112, eqs. (4.99)–(4.100) · Yu §6.5.1–§6.5.3 (the box route; homes as linked) · the user's PHY 513 notes, Ch. 15 §15.9 (paragraph "The $\phi^4$ example (filled in)") · PHY 513 Lecture 16, slide 19 ("No angular dependence (feature of spin-less particles). Simple energy dependence (follows by dimensional analysis). Special to $\phi^4$-theory at leading order"; $\sigma_{\rm tot} = \lambda^2/(32\pi E_{\rm cm}^2)$, "note: identical particles")*

^ex-c6c-8-3

## A question that is not an observable

> [!example] Example §C6c.8.4: The Two-Point Correlator of φ⁴ Theory to Order λ
> ![[ph-qft-c6b-11-4.svg]]
> *The diagrams through order $\lambda$: (a) the free line; (b) the tadpole, the one correction that survives; (c) the line times the figure-eight, in the numerator only; (d) the figure-eight of the denominator, which cancels (c). Vertex $z$, external points $x$, $y$ ([[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-1|Theorem §C6a.7.1]]). Added figure.*
>
> **Question as asked.** "Compute $\langle\Omega|T\{\hat\phi_H(x)\hat\phi_H(y)\}|\Omega\rangle$ in $\phi^4$ theory to first order in $\lambda$."
>
> **Situation** (question 1: no; question 6: not an observable). [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]], an instance of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]: $\hat H = \hat H_0 + \frac{\lambda}{4!}\int d^3x\,\hat\phi_S^4$ for all $t$. Nothing is prepared or measured: the object is a vacuum expectation value of Heisenberg fields ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^def-c6a-4-2|Def. §C6a.4.2]]).
>
> **States and vacuum** (question 4). No particle states. The vacuum is $|\Omega\rangle$ ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^def-c6a-4-1|Def. §C6a.4.1]]), not $|0\rangle$: $\hat H$ takes $|0\rangle$ into four-particle states, $\langle\mathbf p_1\cdots\mathbf p_4|\hat H|0\rangle = \lambda(2\pi)^3\delta^3(\mathbf p_1 + \cdots + \mathbf p_4)$ ([[§C6a.0 Setups and Observables#^thm-c6a-0-4|Theorem §C6a.0.4]], 2).
>
> **Object.** The master formula, exact ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-6|Theorem §C6a.4.6]]), with $\hat H_I(t) = \frac{\lambda}{4!}\int d^3z\,\hat\phi_I(t, \mathbf z)^4$:
>
> $$
> \langle\Omega|T\{\hat\phi_H(x)\hat\phi_H(y)\}|\Omega\rangle = \lim_{T\to\infty(1 - i\varepsilon)}\frac{\langle0|T\bigl\{\hat\phi_I(x)\hat\phi_I(y)\exp\bigl[-i\int_{-T}^Tdt\,\hat H_I(t)\bigr]\bigr\}|0\rangle}{\langle0|T\bigl\{\exp\bigl[-i\int_{-T}^Tdt\,\hat H_I(t)\bigr]\bigr\}|0\rangle} .
> $$
>
> **Normalization and measure.** There is no measure: nothing is summed over final states. The normalization is the denominator, the vacuum-to-vacuum amplitude $\langle0|U(T, -T)|0\rangle \to e^{-2iE_0T}|\langle0|\Omega\rangle|^2$ ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-4|Theorem §C6a.4.4]]); the tilt $T \to \infty(1 - i\varepsilon)$ projects onto $|\Omega\rangle$ ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-1|Theorem §C6a.4.1]]) and is the Feynman $i\varepsilon$ ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-1|Theorem §C6a.11.1]]).
>
> **Theorems.** Wick's theorem in the numerator ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]): the 15 complete contractions split $3 + 12$ ([[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-1|Theorem §C6a.7.1]]); the denominator is $1$ plus the vacuum diagrams ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-2|Theorem §C6a.11.2]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^ex-c6a-11-2|Example §C6a.11.2]]); dividing by hand ([[§C6a.7 Feynman Diagrams for Correlation Functions#^cau-c6a-7-3|§C6a.7, Caution: Numerator, not yet the interacting correlator]]):
>
> $$
> V_1 = -\frac{i\lambda}{8}\int d^4z\,D_F(0)^2 , \qquad C_1 = -\frac{i\lambda}{2}\int d^4z\,D_F(x - z)D_F(0)D_F(z - y) ,
> $$
>
> $$
> \frac{D_F(x - y)(1 + V_1) + C_1}{1 + V_1} = D_F(x - y) + C_1(1 - V_1) + O(\lambda^2) = D_F(x - y) + C_1 + O(\lambda^2) .
> $$
>
> To all orders the bubbles factor out of the numerator and cancel ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-4|Theorem §C6a.11.4]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-5|Theorem §C6a.11.5]]).
>
> **Result** ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-4|§C2b.6, Caution: With interactions, the two-point function is not D_F]]; momentum space: [[§C6a.11 The iε Limit and Vacuum Bubbles#^ex-c6a-11-4|Example §C6a.11.4]]):
>
> $$
> \langle\Omega|T\{\hat\phi_H(x)\hat\phi_H(y)\}|\Omega\rangle = D_F(x - y) - \frac{i\lambda}{2}\int d^4z\,D_F(x - z)D_F(0)D_F(z - y) + O(\lambda^2)
> $$
>
> $$
> = \int\frac{d^4p}{(2\pi)^4}\,e^{-ip\cdot(x - y)}\Bigl[\tilde D_F(p) + \tilde D_F(p)\Bigl(-\frac{i\lambda}{2}\int\frac{d^4k}{(2\pi)^4}\tilde D_F(k)\Bigr)\tilde D_F(p) + O(\lambda^2)\Bigr] .
> $$
>
> **Pitfalls.**
> - *Not a probability.* The answer is complex and a distribution in $x - y$; no modulus is squared and no final states are summed. Its use is as input: amputated and taken on the mass shell it gives $i\mathcal M$ ([[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]]), and its pole carries $Z$ and the physical mass ([[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|§C2b.1, Caution: With interactions, the one-particle matrix element carries √Z]]); in condensed matter such functions are the response functions that are measured ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^rem-c6b-1-2|§C6b.1, Remark: The fundamental observable?]]).
> - *$|0\rangle$ without the denominator* keeps diagram (c), whose vertex integral is $\int d^4z\,D_F(0)^2 = D_F(0)^2\cdot2T\cdot V$, proportional to the volume of spacetime ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]]): the numerator alone is not the correlator.
> - *Real $T$.* Without the tilt the limit oscillates and does not project onto $|\Omega\rangle$ ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-1|Theorem §C6a.4.1]]).
> - *$D_F(0)$ diverges* quadratically ([[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-3|Theorem §C6a.10.3]]): the order-$\lambda$ term is formal until the mass is renormalized; the tadpole is a mass shift.
>
> *Source: PHY 513 Lecture 14, slides 15 and 25 · the user's PHY 513 notes, Ch. 14 §14.3, §14.6 · PS §4.4, eqs. (4.43)–(4.44) · homes as linked*

^ex-c6c-8-4

## Which diagrams contribute

> [!example] Example §C6c.8.5: The Diagrams of 2 → 2 in the Cubic–Quartic Theory at Order g² and λ
> ![[ph-qft-c6b-11-5.svg]]
> *The four diagrams of $p_A + p_B \to p_1 + p_2$: the $s$-, $t$- and $u$-channel trees with two cubic vertices (orange) and internal momentum $q$, and the contact diagram with one quartic vertex (blue); each has $S = 1$ ([[§C6c.6 Feynman Rules for Amplitudes#^ex-c6c-6-1|Example §C6c.6.1]]). Added figure.*
>
> **Question as asked.** "For two-particle scattering, $p_A + p_B \to p_1 + p_2$, draw all the Feynman diagrams to $\mathcal O(g^2)$ or $\mathcal O(\lambda)$. It is natural to treat these all diagrams as if they are of the same order, i.e. to think of $\lambda$ as being of order $g^2/m^2$" (PHY 513, Problem Set 8, Problem 2(a)).
>
> **Situation** (question 1: no; question 5: lowest order). [[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2|Model §C6a.8.2]], $\mathcal L_{\rm int} = -\frac{g}{3!}\phi^3 - \frac{\lambda}{4!}\phi^4$, an instance of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]. At order $g$ every process between on-shell particles is forbidden ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-5|Example §C6c.4.5]]), so $g^2$ and $\lambda$ are the lowest orders of $2 \to 2$.
>
> **States and vacuum.** Free relativistic states over $|0\rangle$, valid at lowest order ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]); the external momenta are labels, one per particle, never relabelled, and $\{\mathbf p_1, \mathbf p_2\} \ne \{\mathbf p_A, \mathbf p_B\}$ ([[§C6c.6 Feynman Rules for Amplitudes#^def-c6c-6-1|Def. §C6c.6.1]], 1).
>
> **Object.** The term with $n_3$ cubic and $n_4$ quartic vertices of $\langle\mathbf p_1\mathbf p_2|\hat S|\mathbf p_A\mathbf p_B\rangle$ ([[§C6c.6 Feynman Rules for Amplitudes#^der-c6c-6-2|Derivation §C6c.6.2]], Step 1), of order $g^{n_3}\lambda^{n_4}$:
>
> $$
> \frac{1}{n_3!}\Bigl(\frac{-ig}{3!}\Bigr)^{n_3}\frac{1}{n_4!}\Bigl(\frac{-i\lambda}{4!}\Bigr)^{n_4}\int\prod_{v}d^4z_v\prod_{u}d^4w_u\;\langle\mathbf p_1\mathbf p_2|\,T\Bigl\{\prod_{v=1}^{n_3}\hat\phi_I(z_v)^3\prod_{u=1}^{n_4}\hat\phi_I(w_u)^4\Bigr\}|\mathbf p_A\mathbf p_B\rangle ,
> $$
>
> a sum over full contractions of legs and particles ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]]), each a labelled diagram. $\mathcal M$ keeps the fully connected ones: they alone have the form $(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2)\times$(smooth) of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]].
>
> **Counting** (the translation proper). With $r = 3n_3 + 4n_4$ legs, $4$ of them on the particles, $I = \frac{r - 4}{2}$ internal lines and $L = I - (n_3 + n_4) + 1$ loops:
>
> | $(n_3, n_4)$ | order | $r$ | $I$ | $L$ | fully connected diagrams |
> |---|---|---|---|---|---|
> | $(2, 0)$ | $g^2$ | $6$ | $1$ | $0$ | external particles split $2 + 2$; $p_A$'s partner is $p_B$, $p_1$ or $p_2$: $s$, $t$, $u$ |
> | $(0, 1)$ | $\lambda$ | $4$ | $0$ | $0$ | all four on the vertex: contact |
> | $(1, 1)$ | $g\lambda$ | $7$ | — | — | none: $7 + 4 = 11$ half-edges, odd ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1\|Theorem §CA.7.1]], 1) |
>
> At $(2, 0)$ the split $3 + 1$ is excluded: the vertex with one particle keeps two legs, which can only pair with each other, while the vertex with three has no free leg, so the diagram falls into two pieces. The split $4 + 0$ does not fit on three legs. Of the $9!! = 945$ pairings at order $g^2$ (31 diagrams) exactly these 3 are fully connected, each an orbit of $2!\,(3!)^2 = 72$ ([[§C6c.6 Feynman Rules for Amplitudes#^ex-c6c-6-1|Example §C6c.6.1]]).
>
> **Why the other pieces are excluded.** [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]] and [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]] sort them. Each connected component carries its own momentum delta ([[§C6c.6 Feynman Rules for Amplitudes#^der-c6c-6-2|Derivation §C6c.6.2]], Step 2; [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-2|Theorem §C6c.1.2]]): a particle that passes by keeps its momentum and belongs to the $\mathbb 1$ of $\hat S$; a vacuum piece is a phase ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]]); a loop on an external leg is a mass and $\sqrt Z$ correction, removed by amputation ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^def-c6c-5-1|Def. §C6c.5.1]]; [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]]).
>
> **Theorems.** Vertex factors $-ig$, $-i\lambda$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]); $S = 1$ for each diagram, every cubic vertex carrying $2 = 3 - 1$ external lines and the quartic one $4$ ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-5|Theorem §C6c.5.5]]); the tree rules that turn each diagram into a term of $i\mathcal M$ ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]]; [[P6 Tree Amplitude from a Lagrangian|P6]]); the count of legs, lines and loops ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]]); the enumeration of the trees and the channels ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]]).
>
> **Result.** Four diagrams, as in the figure: $s$ ($q = p_A + p_B$), $t$ ($q = p_A - p_1$), $u$ ($q = p_A - p_2$) at order $g^2$, and the contact diagram at order $\lambda$, each with $S = 1$. Their sum, beyond what the question asks, is $i\mathcal M = -ig^2\bigl[\frac{1}{s - m^2} + \frac{1}{t - m^2} + \frac{1}{u - m^2}\bigr] - i\lambda$ ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]]).
>
> **Pitfalls.**
> - *Relabelling external particles is not a symmetry.* The momenta are labels, so $s$, $t$, $u$ are three diagrams, not one diagram with a factor 3.
> - *"Connected" means fully connected* ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-1|§C6c.1, Caution: "Connected" here means fully connected]]), not "attached to the external points" as for correlators.
> - *Order counting.* A diagram is of order $g^{n_3}\lambda^{n_4}$; with $\lambda \sim g^2/m^2$, $g^2$ and $\lambda$ are one order and $g\lambda$ is the next (it starts $2 \to 3$, [[§C6c.6 Feynman Rules for Amplitudes#^ex-c6c-6-2|Example §C6c.6.2]]).
> - *$S = 1$ is not $S_{\rm id}$.* The $\frac{1}{2!}$ of the two identical final particles enters $\sigma$, not the diagrams ([[§C6b.7 Evaluating the Cross Section#^thm-c6b-7-4|Theorem §C6b.7.4]]).
>
> *Source: PHY 513, Problem Set 8, Problem 2(a) (statement; the user's solution, as written) · homes as linked*

^ex-c6c-8-5

## Fermions: which signs are physical

> [!example] Example §C6c.8.6: f f → f f in Yukawa Theory at Leading Order
> ![[ph-qft-c6d-5-1.svg]]
> *The two diagrams of $f(p) + f(k) \to f(p') + f(k')$ at order $g^2$: the $t$-channel ($p \to p'$, scalar momentum $p - p'$) and the $u$-channel ($p \to k'$, scalar momentum $p - k'$), with a relative minus sign ([[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]]). Added figure.*
>
> This example uses the fermion rules of C6d (Lecture 17), which come after this chapter; it stands here with the other translations.
>
> **Question as asked.** "Fermion scattering at leading nontrivial order: $\text{fermion}(p) + \text{fermion}(k) \to \text{fermion}(p') + \text{fermion}(k')$" in Yukawa theory; find $i\mathcal M$ and say which of its signs can be measured (PHY 513 Lecture 17, slide 19).
>
> **Situation** (question 1: no; question 2: two fermions collide, two fermions are detected). [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], an instance of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] (the coupling never switches off), at lowest order.
>
> **States and vacuum** (questions 3–5 and 7). Free, relativistic, over $|0\rangle$, lowest order ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]); each fermion carries a spin label, suppressed below ($u(p) \equiv u^s(p)$, each spinor with the spin of its particle); the order of the creation operators is part of the question ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]):
>
> $$
> |i\rangle = |\mathbf p, \mathbf k\rangle = \sqrt{2E_{\mathbf p}2E_{\mathbf k}}\,\hat a^\dagger_{\mathbf p}\hat a^\dagger_{\mathbf k}|0\rangle , \qquad \langle f| = \bigl(|\mathbf p', \mathbf k'\rangle\bigr)^\dagger = \sqrt{2E_{\mathbf p'}2E_{\mathbf k'}}\,\langle0|\hat a_{\mathbf k'}\hat a_{\mathbf p'} .
> $$
>
> **Order.** Every external fermion must meet a fermion field, and each vertex $\hat{\bar\psi}\hat\psi\hat\phi$ has two: four external fermions need two vertices. At first order the two fermion fields cannot absorb two fermions and emit two, so the leading nontrivial contribution is second order (slide 19):
>
> $$
> \langle\mathbf p'\mathbf k'|\hat S|\mathbf p\mathbf k\rangle = {}_0\langle\mathbf p'\mathbf k'|\,\frac{1}{2!}(-ig)^2\int d^4x\,d^4y\;T\bigl[(\hat{\bar\psi}_I\hat\psi_I\hat\phi_I)(x)\,(\hat{\bar\psi}_I\hat\psi_I\hat\phi_I)(y)\bigr]\,|\mathbf p\mathbf k\rangle_0 .
> $$
>
> **Who contracts with whom** (slide 20). "$\psi$'s contract with incoming particles, $\bar\psi$'s with outgoing" ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]); the two $\hat\phi$'s have no external scalar and contract with each other into $D_F(x - y)$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]]). The $x \leftrightarrow y$ images cancel the $\frac{1}{2!}$ ([[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]]), leaving two patterns, $t$ and $u$.
>
> **Signs** (slide 20: "Contract leftmost $\psi$ with external particle $|\vec k\rangle$ $\Rightarrow$ reorder $(-)$"). The sign of each pattern is $(-1)^{\#\text{crossings}}$ of its contraction arcs over the operator string ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]): with the states above, $t$ has two crossings ($+$) and $u$ three ($-$) ([[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]], Step 5).
>
> **Result** ([[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]]; PS (4.119)):
>
> $$
> i\mathcal M = (-ig)^2\Bigl[\bar u(p')u(p)\,\frac{i}{(p - p')^2 - m_\phi^2 + i\varepsilon}\,\bar u(k')u(k) - \bar u(k')u(p)\,\frac{i}{(p - k')^2 - m_\phi^2 + i\varepsilon}\,\bar u(p')u(k)\Bigr] .
> $$
>
> **Which signs are physical** (question 6 and slide 23). What is measured is a cross section, which contains only $|\mathcal M|^2$ ([[§C6b.5 The Cross Section#^mod-c6b-5-1|Model §C6b.5.1]]): "Overall sign usually irrelevant (only $|\mathcal M|^2$ appears in cross-section)". The **relative** sign enters $|\mathcal M|^2$ through the interference of the two terms and is fixed by Fermi statistics: exchanging the two identical final fermions with their spins maps one term into the other, and the amplitude must change sign ("Relative signs enforce statistics of identical particles", slide 23; [[§C6d.5 Second Order#^thm-c6d-5-3|Theorem §C6d.5.3]]). The **overall** sign changes with the order of the states: the slide, the board and Yu write $-$ for $t$ and $+$ for $u$ ([[§C6d.5 Second Order#^rem-c6d-5-1|§C6d.5, Remark: The overall sign is a convention]]).
>
> **Pitfalls.**
> - *Each fermion line is a number.* Write it against its arrow, $\bar u(\text{out})\,u(\text{in})$; a chain that does not close into a number signals a mistake ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]).
> - *One propagator per diagram.* The $u$-term has its own $D_F$ at $p - k'$; slide 20's "$D_F(p - p')[\cdots + p \leftrightarrow k]$" factors the $t$-propagator out of both terms ([[§C6d.5 Second Order#^cau-c6d-5-1|§C6d.5, Caution: Slips in the handwritten notes and on slide 20 for this example]]).
> - *No symmetry factor, but $S_{\rm id}$ in $\sigma$.* The diagrams have $S = 1$ ([[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]]); the two identical final fermions still give $\frac{1}{2!}$ in the total cross section ([[§C6b.7 Evaluating the Cross Section#^thm-c6b-7-4|Theorem §C6b.7.4]]).
> - *Spins.* $\mathcal M$ depends on the four spin labels; an unpolarized cross section averages over the initial and sums over the final spins, which turns each chain into a trace (PS §5.1, not yet in the course; [[§C6d.2 Contractions with External Fermions|§C6d.2]], Connections).
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* lowest order ($g^2$), free states over $|0\rangle$ in the stated order.
>
> *Source: PHY 513 Lecture 17, slides 19–20, 23 · the user's PHY 513 notes, Lecture 17 update, §17.6 · PS §4.7, pp. 116–120, eqs. (4.118)–(4.119) · homes as linked*

^ex-c6c-8-6

> [!remark]- Connections
> - The questions of "How to translate a question" (1–6; 7 adds the fermion signs) are the columns of the table of [[§C6a.0 Setups and Observables|§C6a.0]], read as a method; each row there links the example or procedure that works it.
> - Examples 1 and 2 are both "free states, $U(+\infty, -\infty)$, no denominator", but for opposite reasons: exact because the source switches off, and lowest order because the decay is computed at order $\mu$ — [[§C6a.0 Setups and Observables#^thm-c6a-0-4|Theorem §C6a.0.4]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]].
> - The $\frac{1}{n!}$ of Example 1, the $\frac{1}{2!}$ of Examples 2 and 3 and the $S_{\rm id}$ of every cross section are one fact, the symmetry of bosonic states — [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-5|Theorem §C6c.7.5]], [[§C6b.7 Evaluating the Cross Section#^thm-c6b-7-4|Theorem §C6b.7.4]].
> - Example 4's correlator becomes Example 3's amplitude by amputation; the precise statement with $\sqrt Z$ is the LSZ formula (Lecture 16; QFT C10, planned) — [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]].
> - The recurring computations are procedures: symmetry factors [[P5 Symmetry Factor of a Diagram|P5]], tree amplitudes [[P6 Tree Amplitude from a Lagrangian|P6]], cross sections and widths [[P7 From ℳ to σ or Γ|P7]].
