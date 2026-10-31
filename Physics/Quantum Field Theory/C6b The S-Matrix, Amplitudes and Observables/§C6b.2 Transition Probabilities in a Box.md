---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.1 The S-Matrix and the Invariant Amplitude]] · ↑ [[· C6b The S-Matrix, Amplitudes and Observables]] · [[§C6b.3 The Cross Section]] →

*Sources: Yu Zhao-Huan, 量子场论讲义, §6.5.1 "跃迁概率", pp. 239–242, eqs. (6.276)–(6.306) (page images checked, PDF pp. 247–250); §6.2, eqs. (6.122)–(6.127) (the $S$-operator); §2.3.4, eqs. (2.157), (2.171) (norms) · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), slide 22 ("Derivation similar"), and transcript · the user's PHY 513 notes, Ch. 15 §15.10 (paragraph "Correspondence with Yu") · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.4, p. 96 (the factor $(2\pi)^4\delta^{(4)}(0) = 2T\cdot V$), §4.5, pp. 104–106.*

**What is prepared.** Two particles $A$ and $B$ with sharp momenta $\mathbf p_A$, $\mathbf p_B$, in a periodic box of volume $\tilde V$, evolved from the far past to the far future, a total time $\tilde T$ ([[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]]). **What is measured.** Whether the final state consists of $n$ given particles with momenta in given ranges $d^3p_1, \dots, d^3p_n$, and how often per unit time. This section computes that rate, step by step, in Yu's order (§6.5.1): the transition probability ([[§C6b.2 Transition Probabilities in a Box#^def-c6b-2-1|Def. §C6b.2.1]]), its numerator with the squared delta function made finite by the box ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-2|Theorem §C6b.2.2]]), the norms of the states ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3|Theorem §C6b.2.3]]), the rate per unit time ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4|Theorem §C6b.2.4]]), the number of final states in a momentum range ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-5|Theorem §C6b.2.5]]), the rate into that range ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-6|Theorem §C6b.2.6]]) and the factor for identical final particles ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7|Theorem §C6b.2.7]]). Plane-wave states have infinite norm on all of space, and the square of $\langle f|i\hat T|i\rangle$ contains the square of a delta function; in the box both are finite numbers, proportional to $\tilde V$ and $\tilde V\tilde T$, and all of them cancel in the end. [[§C6b.3 The Cross Section|§C6b.3]] divides the rate by the flux and obtains the cross section. The course derives the same cross section with wave packets and without the box ([[§C6b.4 Wave Packets and the Cross Section|§C6b.4]]–[[§C6b.5 Evaluating the Cross Section|§C6b.5]], "the careful version"); [[§C6b.7 Decay Rates and Widths|§C6b.7]] runs the same chain with one initial particle.

*Conventions* ([[Larsen PHY 513]]): $\tilde V = L^3$ is the volume of the periodic box and $\tilde T$ the duration of the process; the tildes, Yu's, keep them apart from the operator $\hat T$, the time ordering $T\{\cdots\}$ and the half-duration $T$ of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]], with $\tilde T = 2T$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^cau-c6b-1-4|§C6b.1, Caution: Four T's]]). $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$, $E_A \equiv E_{\mathbf p_A}$, $E_j \equiv E_{\mathbf p_j}$. $p_i = p_A + p_B$ and $p_f = \sum_jp_j$ are the total four-momenta of the initial and final states (Yu (6.286)). $S_{\rm id}$ is the identical-particle factor ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^cau-c6b-1-2|§C6b.1, Caution: Four S's]]).

## The model

> [!model] Model §C6b.2.1: Two Particles in a Box
> Two particles $A$, $B$ (masses $m_A$, $m_B$) with sharp momenta scatter into $n$ particles.
> - *Space:* a cube of side $L$, volume $\tilde V = L^3$, with periodic boundary conditions; every particle is a plane wave spread uniformly over the box, one particle per volume $\tilde V$.
> - *Time:* the evolution runs from the far past to the far future; its duration is $\tilde T$.
> - *Hamiltonian:* $\hat H = \hat H_0 + \hat H_{\rm int}$ in the interaction picture; the evolution operator from the far past to the far future is $\hat S = U(+\infty, -\infty)$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]] and its ⚑).
> - *States:* free Fock states of $\hat H_0$, relativistically normalized ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]); the vacuum is $|0\rangle$, the ground state of $\hat H_0$, not the interacting vacuum $|\Omega\rangle$ (Yu (6.284)–(6.285)):
>
> $$
> |i\rangle = \sqrt{2E_A}\sqrt{2E_B}\;\hat a^\dagger_{\mathbf p_A}\hat a^\dagger_{\mathbf p_B}|0\rangle , \qquad |f\rangle = \Bigl(\prod_{j=1}^n\sqrt{2E_j}\;\hat a^\dagger_{\mathbf p_j}\Bigr)|0\rangle .
> $$
>
> - *Final state:* different from the initial one, $f \ne i$ (other particle content, or other momenta).
> - *Applies:* exactly if the interaction is switched off at early and late times, $\hat H_{\rm int}(t) \to 0$ for $|t| \to \infty$, so that the free states are the asymptotic states; for a permanent interaction (a fixed $\hat H$) at lowest order only: beyond it the external particles carry factors $\sqrt Z$ and the physical mass ([[§C6b.8 Amplitudes from Correlation Functions#^cau-c6b-8-2|§C6b.8, Caution: The rule is stated at lowest order]]; [[§C6b.1 The S-Matrix and the Invariant Amplitude#^cau-c6b-1-1|§C6b.1, Caution: "Free" means widely separated]]).
>
> *Source: Yu §6.2, eqs. (6.122)–(6.125) (asymptotic states of free form, $S = U(+\infty, -\infty)$); §6.5.1, eqs. (6.282), (6.284)–(6.285), (6.292) (the box, the states, the duration), (6.295) (periodic boundary conditions)*

^mod-c6b-2-1

## The transition probability

> [!definition] Definition §C6b.2.1: Transition Probability
> *Model:* [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]].
> The **transition probability** from $|i\rangle$ to $|f\rangle$ is the squared overlap of the unit vectors along $\hat S|i\rangle$ and $|f\rangle$:
>
> $$
> P_{fi} = \frac{|\langle f|\hat S|i\rangle|^2}{\langle i|i\rangle\,\langle f|f\rangle} = \Bigl|\Bigl\langle\frac{f}{\sqrt{\langle f|f\rangle}}\Bigr|\hat S\Bigl|\frac{i}{\sqrt{\langle i|i\rangle}}\Bigr\rangle\Bigr|^2 .
> $$
>
> *Source: Yu §6.5.1, eq. (6.276) ("除以它们使得跃迁概率具有合适的归一化": dividing by the self inner products gives the probability its proper normalization)*

^def-c6b-2-1

Why both norms: the Born rule gives probabilities as squared overlaps of *unit* vectors, and the box states have norms $\propto\tilde V$ ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3|Theorem §C6b.2.3]] below). The evolution does not change the norm of the initial vector, by unitarity ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-1|Theorem §C6a.3.1]]; Yu (6.127)):

$$
\langle\hat Si|\hat Si\rangle = \langle i|\hat S^\dagger\hat S|i\rangle = \langle i|\mathbb 1|i\rangle = \langle i|i\rangle ,
$$

so dividing by $\langle i|i\rangle$ normalizes the evolved state as well.

The box turns the delta functions of this section into numbers. The mathematics, with the lattice of momenta derived from the boundary condition and the box in time:

![[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10]]

> [!theorem] Theorem §C6b.2.2: The Squared Amplitude in a Box
> *Model:* [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]]; *applies:* as there.
> For $f \ne i$, with $\mathcal M$ of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]],
> 1. only $i\hat T$ contributes: $\langle f|\hat S|i\rangle = \langle f|i\hat T|i\rangle$, and
>
> $$
> P_{fi} = \frac{|\langle f|i\hat T|i\rangle|^2}{\langle i|i\rangle\,\langle f|f\rangle} ;
> $$
>
> 2. the numerator is
>
> $$
> |\langle f|i\hat T|i\rangle|^2 = \bigl[(2\pi)^4\delta^4(p_i - p_f)\bigr]^2|\mathcal M|^2 = (2\pi)^4\delta^4(0)\cdot(2\pi)^4\delta^4(p_i - p_f)\,|\mathcal M|^2 = \tilde V\tilde T\,(2\pi)^4\delta^4(p_i - p_f)\,|\mathcal M|^2 ,
> $$
>
> with $(2\pi)^4\delta^4(0) = \int d^4x = \tilde V\tilde T$.
>
> *Source: Yu §6.5.1, eqs. (6.276)–(6.283) (page image checked: $(2\pi)^4\delta^{(4)}(0) = \int d^4x = \tilde V\tilde T$, "$\tilde V$ 是空间积分区域的体积，$\tilde T$ 是时间积分范围的长度") · PS §4.4, p. 96*

^thm-c6b-2-2

> [!derivation]- Derivation
> **Step 1** (the $\mathbb 1$ drops out; part 1). By [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]],
>
> $$
> \langle f|\hat S|i\rangle = \langle f|\mathbb 1 + i\hat T|i\rangle = \langle f|i\rangle + \langle f|i\hat T|i\rangle .
> $$
>
> States of different particle content are orthogonal. For the same content, the overlap is a sum of products of $\langle\mathbf p|\mathbf q\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]), which in the box is $2E_{\mathbf p}\tilde V\delta_{\mathbf p\mathbf q}$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10|Theorem §CA.3.10]], 2; [[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]]): it vanishes when the sets of lattice momenta differ. So $\langle f|i\rangle = 0$ for $f \ne i$, and $\langle f|\hat S|i\rangle = \langle f|i\hat T|i\rangle$; inserted in [[§C6b.2 Transition Probabilities in a Box#^def-c6b-2-1|Def. §C6b.2.1]] this is Yu's (6.276). The same statement for the in and out states of the careful route is [[§C6b.4 Wave Packets and the Cross Section#^lem-c6b-4-5|Lemma §C6b.4.5]].
>
> **Step 2** (square the amplitude). By [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], $\langle f|i\hat T|i\rangle = (2\pi)^4\delta^4(p_i - p_f)\,i\mathcal M$. The delta function is real and $|i\mathcal M|^2 = (i\mathcal M)(-i\mathcal M^\ast) = |\mathcal M|^2$:
>
> $$
> |\langle f|i\hat T|i\rangle|^2 = (2\pi)^4\delta^4(p_i - p_f)\,i\mathcal M\cdot(2\pi)^4\delta^4(p_i - p_f)\,(-i\mathcal M^\ast) = \bigl[(2\pi)^4\delta^4(p_i - p_f)\bigr]^2|\mathcal M|^2 .
> $$
>
> **Step 3** (one delta at the zero of the other). Yu uses $g(x)\delta(x) = g(0)\delta(x)$ (his (2.57)) with $g = \delta$: on the support of one factor the other is evaluated at zero (Yu (6.277)),
>
> $$
> \bigl[(2\pi)^4\delta^4(p_i - p_f)\bigr]^2 = (2\pi)^4\delta^4(0)\cdot(2\pi)^4\delta^4(p_i - p_f) .
> $$
>
> On all of spacetime $\delta^2$ and $\delta(0)$ have no value ([[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]], 2–3); in the box this is part 4 of [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10|Theorem §CA.3.10]], $\bigl[(2\pi)^4\delta^4(p - p')\bigr]^2 \leftrightarrow \tilde V\tilde T\,(2\pi)^4\delta^4(p - p')$.
>
> **Step 4** (the value of $(2\pi)^4\delta^4(0)$). The Fourier representation (Yu (6.278)–(6.279); [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]])
>
> $$
> \int d^4x\,e^{\pm ip\cdot x} = \int dx^0\,e^{\pm ip^0x^0}\int d^3x\,e^{\mp i\mathbf p\cdot\mathbf x} = 2\pi\delta(p^0)\cdot(2\pi)^3\delta^3(\mathbf p) = (2\pi)^4\delta^4(p) ,
> $$
>
> at $p = 0$, over the box and the duration, gives (Yu (6.282))
>
> $$
> (2\pi)^4\delta^4(0) = \int_{\tilde V\times\tilde T}d^4x\;e^{i0\cdot x} = \int_{\tilde T}dx^0\int_{\tilde V}d^3x = \tilde V\tilde T .
> $$
>
> Steps 2–4 together: $|\langle f|i\hat T|i\rangle|^2 = \tilde V\tilde T\,(2\pi)^4\delta^4(p_i - p_f)\,|\mathcal M|^2$ (Yu (6.283)).
>
> **What the derivation shows.**
> - The squared amplitude carries one factor $\tilde V\tilde T$; the second delta function survives and becomes part of the phase space ([[§C6b.3 The Cross Section|§C6b.3]], the annotated formula).
> - The same box factor, written $2T\cdot V$, made every vacuum bubble proportional to the volume of spacetime ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]]); $\tilde T = 2T$.

^der-c6b-2-2

*Uses:* [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]], [[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10|Theorem §CA.3.10]]

## The states and their norms

> [!theorem] Theorem §C6b.2.3: Norms of the Box States
> *Model:* [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]] (free, relativistically normalized states over $|0\rangle$).
> 1. One particle: $\langle\mathbf p|\mathbf p\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf 0) = 2E_{\mathbf p}\tilde V$.
> 2. The initial state, for $A \ne B$, or $A = B$ with $\mathbf p_A \ne \mathbf p_B$:
>
> $$
> \langle i|i\rangle = 2E_A\tilde V\cdot2E_B\tilde V = 4E_AE_B\tilde V^2 .
> $$
>
> 3. The final state, if no two identical particles share a momentum:
>
> $$
> \langle f|f\rangle = \prod_{j=1}^n\bigl(2E_j\tilde V\bigr) .
> $$
>
> *Source: Yu §6.5.1, eqs. (6.284)–(6.290) (page image checked); §2.3.4, eqs. (2.157), (2.171)*

^thm-c6b-2-3

> [!derivation]- Derivation
> **Step 1** (one particle; part 1). [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]] at $\mathbf q = \mathbf p$, and the box value $(2\pi)^3\delta^3(\mathbf 0) = \tilde V$ ([[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]]; Yu (6.288)):
>
> $$
> \langle\mathbf p|\mathbf q\rangle\big|_{\mathbf q = \mathbf p} = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf p) = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf 0) = 2E_{\mathbf p}\tilde V .
> $$
>
> **Step 2** (two species; part 2). If $A$ and $B$ are quanta of different fields, the state is a product, $|i\rangle = \sqrt{2E_A}\hat a^\dagger_{\mathbf p_A}|0\rangle_A\otimes\sqrt{2E_B}\hat a^\dagger_{\mathbf p_B}|0\rangle_B = |\mathbf p_A\rangle_A\otimes|\mathbf p_B\rangle_B$ (Yu (6.287)), and the norm of a product is the product of the norms (Yu (6.289)):
>
> $$
> \langle i|i\rangle = \langle\mathbf p_A|\mathbf p_A\rangle_A\,\langle\mathbf p_B|\mathbf p_B\rangle_B = 2E_A\tilde V\cdot2E_B\tilde V = 4E_AE_B\tilde V^2 .
> $$
>
> **Step 3** (one species, $\mathbf p_A \ne \mathbf p_B$; part 2). [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]], 1, with the factors $\sqrt{2E}$ of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], at $\mathbf q_1 = \mathbf p_A$, $\mathbf q_2 = \mathbf p_B$, and $(2\pi)^3\delta^3(\mathbf p - \mathbf q) \leftrightarrow \tilde V\delta_{\mathbf p\mathbf q}$:
>
> $$
> \langle i|i\rangle = 2E_A\,2E_B\,(2\pi)^6\bigl[\delta^3(\mathbf 0)\delta^3(\mathbf 0) + \delta^3(\mathbf p_A - \mathbf p_B)\delta^3(\mathbf p_B - \mathbf p_A)\bigr] \leftrightarrow 4E_AE_B\bigl[\tilde V^2 + \tilde V^2\delta_{\mathbf p_A\mathbf p_B}\bigr] = 4E_AE_B\tilde V^2 ,
> $$
>
> since $\delta_{\mathbf p_A\mathbf p_B} = 0$ (Yu, after (6.289): "若 $\mathbf p_{\mathcal A} \ne \mathbf p_{\mathcal B}$，则根据 (2.171) … 也能推出这个结果").
>
> **Step 4** ($n$ final particles; part 3). Commuting each annihilator through the creators, the overlap of $n$ relativistically normalized quanta of one species is a sum over the $n!$ ways of matching the momenta (the general form of Step 3; written out in [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-4|Derivation §C6b.5.4]], Step 2):
>
> $$
> \langle\mathbf p_1\cdots\mathbf p_n|\mathbf p_1\cdots\mathbf p_n\rangle = \prod_{j=1}^n2E_j\sum_{\pi\in S_n}\prod_{j=1}^n(2\pi)^3\delta^3(\mathbf p_j - \mathbf p_{\pi(j)}) \leftrightarrow \prod_{j=1}^n2E_j\sum_{\pi\in S_n}\prod_{j=1}^n\tilde V\,\delta_{\mathbf p_j\mathbf p_{\pi(j)}} .
> $$
>
> If the momenta are pairwise different, every $\pi \ne \mathrm{id}$ moves some $j$ to $\pi(j) \ne j$ with $\delta_{\mathbf p_j\mathbf p_{\pi(j)}} = 0$; only $\pi = \mathrm{id}$ survives, and the sum is $\prod_j\tilde V$. With several species the state is a product over species, as in Step 2. Either way (Yu (6.290))
>
> $$
> \langle f|f\rangle = \prod_{j=1}^n2E_j\tilde V .
> $$
>
> **What the derivation shows.**
> - Each particle contributes one factor $\tilde V$ to the norm: $\tilde V^2$ for the initial state, $\tilde V^n$ for the final one.
> - Coincident momenta of identical bosons give a larger norm; [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7|Theorem §C6b.2.7]] needs it.

^der-c6b-2-3

*Uses:* [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]], [[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]]

## The rate

> [!theorem] Theorem §C6b.2.4: The Transition Probability Grows Linearly in Time; the Rate
> *Model:* [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]]; *applies:* as there, and for a duration $\tilde T$ long compared with the collision.
> For $f \ne i$ with distinct final momenta,
>
> $$
> P_{fi} = \frac{\tilde T\,(2\pi)^4\delta^4(p_i - p_f)\,|\mathcal M|^2}{4E_AE_B\tilde V\prod_{j=1}^n\bigl(2E_j\tilde V\bigr)} \;\propto\; \tilde T .
> $$
>
> The **rate** for one set of final momenta $\{p_j\}$, the transition probability per unit time, is therefore independent of $\tilde T$:
>
> $$
> R_{\{p_j\}} \equiv \frac{P_{fi}}{\tilde T} = \Bigl[4E_AE_B\tilde V\prod_{j=1}^n\bigl(2E_j\tilde V\bigr)\Bigr]^{-1}(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_{j=1}^np_j\Bigr)\,|\mathcal M|^2 .
> $$
>
> *Source: Yu §6.5.1, eqs. (6.291)–(6.293) (page image checked)*

^thm-c6b-2-4

> [!derivation]- Derivation
> **Step 1** (insert). [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-2|Theorem §C6b.2.2]] for the numerator and [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3|Theorem §C6b.2.3]] for the denominator, then one $\tilde V$ cancelled (Yu (6.291)):
>
> $$
> P_{fi} = \frac{\tilde V\tilde T\,(2\pi)^4\delta^4(p_i - p_f)\,|\mathcal M|^2}{4E_AE_B\tilde V^2\prod_{j=1}^n\bigl(2E_j\tilde V\bigr)} = \frac{\tilde T\,(2\pi)^4\delta^4(p_i - p_f)\,|\mathcal M|^2}{4E_AE_B\tilde V\prod_{j=1}^n\bigl(2E_j\tilde V\bigr)} .
> $$
>
> **Step 2** (divide by the duration). $\tilde T$ appears once, in the numerator; dividing by it removes it (Yu (6.292)), and $p_i - p_f = p_A + p_B - \sum_jp_j$:
>
> $$
> \frac{P_{fi}}{\tilde T} = \frac{(2\pi)^4\delta^4\bigl(p_A + p_B - \sum_jp_j\bigr)\,|\mathcal M|^2}{4E_AE_B\tilde V\prod_{j=1}^n\bigl(2E_j\tilde V\bigr)} .
> $$
>
> **Step 3** (the delta function by components). With $p = (E, \mathbf p)$ (Yu (6.293)),
>
> $$
> \delta^4\Bigl(p_A + p_B - \sum_jp_j\Bigr) = \delta^3\Bigl(\mathbf p_A + \mathbf p_B - \sum_j\mathbf p_j\Bigr)\,\delta\Bigl(E_A + E_B - \sum_jE_j\Bigr) :
> $$
>
> the rate is nonzero only for final momenta that conserve momentum and energy (the kinematic condition $p_A^\mu + p_B^\mu - \sum_jp_j^\mu = 0$, Yu (6.294)).
>
> **What the derivation shows.**
> - Why a rate: $P_{fi}$ grows in proportion to the time during which the particles overlap in the box, so the transition happens at a constant probability per unit time, and that number is the physical one. Quantum mechanics found the same at first order: the transition probability into a continuum grows like $t$ for long times and Fermi's golden rule is its slope ([[§C9.5 Fermi's Golden Rule#^thm-c9-5-1|QM Theorem §C9.5.1]]).
> - The rate still contains $1/\tilde V$ per particle: $n + 1$ powers. The next two theorems remove $n$ of them by counting final states; [[§C6b.3 The Cross Section|§C6b.3]] removes the last one with the flux.

^der-c6b-2-4

*Uses:* [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-2|Theorem §C6b.2.2]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3|Theorem §C6b.2.3]]

## Counting the final states

> [!theorem] Theorem §C6b.2.5: Final States in a Periodic Box
> *Model:* [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]] (each final particle confined to the periodic cube).
> 1. With the periodic boundary condition $\varphi(-L/2) = \varphi(L/2)$ in each direction, the momentum operator $\hat p_x = -i\partial/\partial x$ is Hermitian on the box, and its eigenfunctions $\varphi_{\mathbf p} \propto e^{i\mathbf p\cdot\mathbf x}$ have $\mathbf p = \frac{2\pi}{L}(k_1, k_2, k_3)$, $k_1, k_2, k_3 \in \mathbb Z$.
> 2. A range $d^3p$ of a final particle's momentum contains $\tilde V\,d^3p/(2\pi)^3$ of these states; a sum over the final momenta of $n$ particles becomes
>
> $$
> \sum_{\mathbf p_1, \dots, \mathbf p_n} \;\longrightarrow\; \prod_{j=1}^n\frac{\tilde V}{(2\pi)^3}\int d^3p_j .
> $$
>
> *Source: Yu §6.5.1, eqs. (6.294)–(6.302) (page image checked; Yu cites Zeng Jinyan, Quantum Mechanics I, §4.4.3, for the boundary condition)*

^thm-c6b-2-5

> [!derivation]- Derivation
> **Step 1** (why periodic; part 1). For wave functions $\varphi$, $\psi$ on $[-L/2, L/2]$, integrate by parts:
>
> $$
> \langle\varphi|\hat p_x\psi\rangle - \langle\hat p_x\varphi|\psi\rangle = \int_{-L/2}^{L/2}dx\,\bigl[\varphi^\ast(-i\psi') - (-i\varphi')^\ast\psi\bigr] = -i\int_{-L/2}^{L/2}dx\,(\varphi^\ast\psi)' = -i\bigl[\varphi^\ast\psi\bigr]_{-L/2}^{L/2} .
> $$
>
> If $\varphi$ and $\psi$ both satisfy $\varphi(-L/2) = \varphi(L/2)$ (Yu (6.295)), the boundary term is $\varphi^\ast(L/2)\psi(L/2) - \varphi^\ast(-L/2)\psi(-L/2) = 0$, and $\hat p_x$ is Hermitian.
>
> **Step 2** (the allowed momenta; part 1). The plane wave $\varphi_p = e^{ipx}$ is an eigenfunction of $\hat p_x$ with eigenvalue $p$; it satisfies the boundary condition exactly for $p = 2\pi k/L$, $k \in \mathbb Z$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10|Theorem §CA.3.10]], 1; Yu (6.296)–(6.297)). In three dimensions the condition holds on each pair of opposite faces of the cube (Yu (6.301)).
>
> **Step 3** (the count; part 2). By [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10|Theorem §CA.3.10]], 2, the lattice has one point per cell of volume $(2\pi/L)^3 = (2\pi)^3/\tilde V$ (Yu (6.298)–(6.300) in one dimension), so
>
> $$
> \#\{\text{states with }\mathbf p\in d^3p\} = \frac{d^3p}{(2\pi)^3/\tilde V} = \frac{\tilde V\,d^3p}{(2\pi)^3} , \qquad \sum_{\mathbf p} \longrightarrow \frac{L^3}{(2\pi)^3}\int d^3p = \frac{\tilde V}{(2\pi)^3}\int d^3p
> $$
>
> (Yu (6.302)). The $n$ final particles have independent lattices, so the sum over $(\mathbf p_1, \dots, \mathbf p_n)$ is the product of $n$ such sums.
>
> **What the derivation shows.**
> - The count carries one factor $\tilde V$ per final particle, the same $\tilde V$ that the norm $\langle f|f\rangle$ put in the denominator ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3|Theorem §C6b.2.3]], 3): this is why they cancel.
> - The measure $\frac{d^3p}{(2\pi)^3}$ of the phase space is the density of box states per unit volume.

^der-c6b-2-5

*Uses:* [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10|Theorem §CA.3.10]]

> [!theorem] Theorem §C6b.2.6: The Rate into a Range of Final Momenta
> *Model:* [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]]; *applies:* as there, for final states without identical particles (with them: [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7|Theorem §C6b.2.7]]).
> The rate into final momenta in $d^3p_1\cdots d^3p_n$ is
>
> $$
> dR = \prod_{j=1}^n\frac{\tilde V\,d^3p_j}{(2\pi)^3}\;R_{\{p_j\}} = \frac{1}{4E_AE_B\tilde V}\;\prod_{j=1}^n\frac{d^3p_j}{(2\pi)^3\,2E_j}\;(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_{j=1}^np_j\Bigr)\,|\mathcal M|^2 ,
> $$
>
> and the total rate is $R = \int dR$ over all final momenta. Each factor $\frac{d^3p_j}{(2\pi)^3\,2E_j}$ is the Lorentz-invariant measure on the positive-energy mass shell.
>
> *Source: Yu §6.5.1, eqs. (6.303)–(6.304) (page image checked)*

^thm-c6b-2-6

> [!derivation]- Derivation
> **Step 1** (sum the rate over the states in the range). By [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-5|Theorem §C6b.2.5]], 2, the range contains $\prod_j\tilde V\,d^3p_j/(2\pi)^3$ states, and [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4|Theorem §C6b.2.4]] gives the same rate for each (the range is small):
>
> $$
> dR = \prod_{j=1}^n\frac{\tilde V\,d^3p_j}{(2\pi)^3}\cdot\Bigl[4E_AE_B\tilde V\prod_{j=1}^n\bigl(2E_j\tilde V\bigr)\Bigr]^{-1}(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_jp_j\Bigr)\,|\mathcal M|^2 .
> $$
>
> **Step 2** (each count cancels one final norm). Pair the $j$-th counting factor with the $j$-th norm factor (Yu (6.303)):
>
> $$
> \frac{\tilde V\,d^3p_j}{(2\pi)^3}\cdot\frac{1}{2E_j\tilde V} = \frac{d^3p_j}{(2\pi)^3\,2E_j} ,
> $$
>
> which leaves $\frac{1}{4E_AE_B\tilde V}$ from the initial state: the statement.
>
> **Step 3** (the measure). $\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}} = \frac{d^4p}{(2\pi)^4}\,2\pi\delta(p^2 - m^2)\theta(p^0)$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]]): it covers exactly the four-momenta on the mass shell with positive energy, and it is Lorentz invariant ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]; Yu (6.304), with his (2.159), (2.161)).
>
> **What the derivation shows.**
> - Of the $n + 1$ powers of $1/\tilde V$ in the rate, $n$ are gone; the one left belongs to the initial state, and the flux removes it ([[§C6b.3 The Cross Section|§C6b.3]]).
> - The factor $\frac{1}{2E_j}$ of each final particle is its relativistic normalization; the factor $\frac{1}{(2\pi)^3}$ is the density of states.

^der-c6b-2-6

*Uses:* [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4|Theorem §C6b.2.4]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-5|Theorem §C6b.2.5]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]

> [!theorem] Theorem §C6b.2.7: Identical Particles in the Final State
> *Model:* [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]]; *applies:* as there.
> If the final state contains $n_k$ identical particles of species $k$, integrating $dR$ of [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-6|Theorem §C6b.2.6]] over all final momenta counts every physical final state $n_k!$ times per species, also when identical bosons share a momentum. The total rate is
>
> $$
> R = \frac{1}{S_{\rm id}}\int dR = \frac{1}{S_{\rm id}}\,\frac{1}{4E_AE_B\tilde V}\;\prod_{j=1}^n\int\frac{d^3p_j}{(2\pi)^3\,2E_j}\;(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_jp_j\Bigr)\,|\mathcal M|^2 , \qquad S_{\rm id} = \prod_kn_k! .
> $$
>
> *Source: Yu §6.5.1, eqs. (6.305)–(6.306) and footnote 6 (page image checked) · PS §4.5, p. 108*

^thm-c6b-2-7

> [!derivation]- Derivation
> Take one species with $n$ identical particles; several species give the product of the factors.
>
> **Step 1** (states versus ordered momenta). $|\mathbf p_{\pi(1)}\cdots\mathbf p_{\pi(n)}\rangle = |\mathbf p_1\cdots\mathbf p_n\rangle$ for every permutation $\pi$ ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]], 1): a state is labelled by the multiset $\{\mathbf p_1, \dots, \mathbf p_n\}$, while $\int dR$, by [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-5|Theorem §C6b.2.5]], sums over ordered $n$-tuples of lattice momenta.
>
> **Step 2** (how many tuples per state). Let the multiset contain $r$ different momenta with multiplicities $m_1, \dots, m_r$, $\sum_am_a = n$. The orderings of it number
>
> $$
> \#\{\text{tuples}\} = \frac{n!}{m_1!\cdots m_r!} .
> $$
>
> **Step 3** (the true norm). In the overlap of [[§C6b.2 Transition Probabilities in a Box#^der-c6b-2-3|Derivation §C6b.2.3]], Step 4, a permutation $\pi$ survives if and only if $\mathbf p_{\pi(j)} = \mathbf p_j$ for all $j$, i.e. it only permutes equal momenta among themselves; there are $m_1!\cdots m_r!$ of them, each contributing $\prod_j\tilde V$:
>
> $$
> \langle f|f\rangle = m_1!\cdots m_r!\;\prod_{j=1}^n2E_j\tilde V .
> $$
>
> **Step 4** (compare). The rate into the state is $|\langle f|i\hat T|i\rangle|^2/(\langle i|i\rangle\langle f|f\rangle\tilde T)$ with the true norm, i.e. $R_{\{p_j\}}/(m_1!\cdots m_r!)$, since [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4|Theorem §C6b.2.4]] used $\prod_j2E_j\tilde V$. The tuple sum gives each state the weight
>
> $$
> \frac{n!}{m_1!\cdots m_r!}\cdot R_{\{p_j\}} = n!\cdot\frac{R_{\{p_j\}}}{m_1!\cdots m_r!} = n!\cdot\bigl(\text{rate into the state}\bigr) ,
> $$
>
> the same factor $n!$ for every multiset. So the sum over states is $\frac{1}{n!}$ times the tuple sum, and with [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-6|Theorem §C6b.2.6]] the statement follows (Yu (6.305)–(6.306)). Distinct momenta are Yu's main text; coincident ones his footnote 6 ("内积 $\langle f|f\rangle$ 应改为 (6.290) 式右边的 $n_k!$ 倍").
>
> **What the derivation shows.**
> - Two identical particles: $\{\mathbf p, \mathbf q\}$ with $\mathbf p \ne \mathbf q$ is reached by two tuples with norm factor 1, and $\{\mathbf p, \mathbf p\}$ by one tuple with norm factor $2$; both are weighted $2 = 2!$ times too much.
> - The factor counts final *states*; it is not in $dR$ at a point of phase space ([[§C6b.3 The Cross Section#^thm-c6b-3-6|Theorem §C6b.3.6]]). The careful route gets the same $\frac{1}{S_{\rm id}}$ from the resolution of the identity on $n$-particle states ([[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-4|Theorem §C6b.5.4]]).

^der-c6b-2-7

*Uses:* [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3|Theorem §C6b.2.3]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4|Theorem §C6b.2.4]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-5|Theorem §C6b.2.5]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-6|Theorem §C6b.2.6]]

> [!caution] Caution: Names in Yu's §6.5.1
> Yu writes the initial particles in script, $\mathcal A$, $\mathcal B$, and the identical-particle factor $\mathcal S$ (末态对称性因子, (6.305)); these notes write $A$, $B$ and $S_{\rm id}$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^cau-c6b-1-2|§C6b.1, Caution: Four S's]]). His $T_{fi} = \langle f|T|i\rangle$ is $\langle f|\hat T|i\rangle$ here, and his $R$ (单位时间内的跃迁概率) is the rate $R$ of [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4|Theorem §C6b.2.4]]–[[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7|Theorem §C6b.2.7]]; the calligraphic $\mathcal R$ of [[§C6b.3 The Cross Section|§C6b.3]] is a rate per unit volume. His creation operators carry no hats and no helicity labels (spinless particles here).
>
> *Source: Yu §6.5.1, eqs. (6.273), (6.284), (6.292), (6.305)*

^cau-c6b-2-1

> [!remark]- Connections
> - The box is the regularization of [[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]] and [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10|Theorem §CA.3.10]]: the same $(2\pi)^3\delta^3(\mathbf 0) = \tilde V$ that made the zero-point energy a volume times a density ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]), and the same $(2\pi)^4\delta^4(0)$ as the vacuum bubbles ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]]).
> - A rate linear in the duration, with a density of final states, is Fermi's golden rule; here the density is $\tilde V\,d^3p/(2\pi)^3$ per particle and energy conservation is the $\delta(E_A + E_B - \sum E_j)$ of [[§C6b.2 Transition Probabilities in a Box#^der-c6b-2-4|Derivation §C6b.2.4]], Step 3 — [[§C9.5 Fermi's Golden Rule#^thm-c9-5-1|QM Theorem §C9.5.1]].
> - The careful version of every step, without the box: wave packets of unit norm ([[§C6b.4 Wave Packets and the Cross Section#^thm-c6b-4-2|Theorem §C6b.4.2]]) instead of $\langle i|i\rangle = 4E_AE_B\tilde V^2$, and an integral over the impact parameter instead of $(2\pi)^4\delta^4(0) = \tilde V\tilde T$ — [[§C6b.4 Wave Packets and the Cross Section|§C6b.4]], table in its opening.
> - The decay rate is the same chain with one initial particle, $\langle i|i\rangle = 2E_A\tilde V$ — [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-2|Theorem §C6b.7.2]].
