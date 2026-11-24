---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8a
section: C8a.14
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C8a.13 The Cross Section for Electron–Muon Scattering|§C8a.13]] · ↑ [[· C8a Quantum Electrodynamics]] · [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square|§C8a.15]] →

*Sources: PHY 513 Lecture 21 (Larsen, 18 Nov 2026, "Crossing Symmetry"; a recorded lecture in three parts), slides 17–26 (Part C), and recording, part C · Peskin & Schroeder, An Introduction to Quantum Field Theory, §5.4, pp. 155–158, eqs. (5.67)–(5.73) and the figures of pp. 155–157 · Yu Zhao-Huan, 量子场论讲义, §8.5, eqs. (8.288), (8.290)–(8.296), (8.302)–(8.303), (8.310)–(8.312), (8.315)–(8.318) (page images checked).*

Why could the scattering result be read off from the annihilation result? [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-3|Theorem §C8a.12.3]] found a substitution of momenta that turns one spin-averaged square into the other. This section states the general fact behind it, **crossing symmetry** ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-1|Principle §C8a.14.1]]): a particle in the initial state and its antiparticle in the final state, with the opposite four-momentum, have the same amplitude. Two qualifications come with it. The opposite four-momentum is not physical, so the statement is about the amplitude as an analytic function ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-2|Principle §C8a.14.2]]); and for fermions there is a sign ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-3|Theorem §C8a.14.3]]). The **Mandelstam variables** $s$, $t$, $u$ ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-1|Def. §C8a.14.1]]) are the variables in which crossing is simple: the two processes of this chapter are $\frac{2e^4}{s^2}(t^2 + u^2)$ and $\frac{2e^4}{t^2}(s^2 + u^2)$ ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-4|Theorem §C8a.14.4]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-5|Theorem §C8a.14.5]]), one function with $s$ and $t$ exchanged ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-6|Theorem §C8a.14.6]]). They also name the **channels** of a diagram ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-2|Def. §C8a.14.2]]), each with its own angular dependence ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-7|Theorem §C8a.14.7]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^ex-c8a-14-1|Example §C8a.14.1]]). The variables themselves are not new: they are [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]], with the sum rule of [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], and the channels of the scalar theories are [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]]; this section states them in the form of the lecture and links those homes.

**Setup.** The general statements ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-1|Principle §C8a.14.1]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-2|Principle §C8a.14.2]]) concern amplitudes computed from Feynman diagrams in any of the theories of the course ([[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]); they are stated as the lecture states them, with the proof idea for a charged scalar field and without a complete proof. The QED statements are for [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]] at order $e^2$, unpolarized, with **all masses neglected** ("the massless limit"). The kinematic statements hold for any $2 \to 2$ process with on-shell momenta.

*Conventions* ([[Larsen PHY 513]]): for a general $2 \to 2$ process the incoming momenta are $p, p'$ and the outgoing ones $k, k'$ (slide 20, PS p. 156). For annihilation these are the labels of [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-2|Theorem §C8a.6.2]], $e^-(p)$, $e^+(p')$, $\mu^-(k)$, $\mu^+(k')$; for scattering they are $p = p_1$, $p' = p_2$, $k = p_1'$, $k' = p_2'$ in the labels of [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution|§C8a.12]], so that $p$ and $k$ are the incoming and the outgoing electron. $\bar\phi$ is the antiparticle of $\phi$; the bar is not a Dirac conjugate. $\theta$ is the angle between $\mathbf k$ and $\mathbf p$ in the centre-of-mass frame.

## Crossing symmetry

> [!principle] Principle §C8a.14.1: Crossing Symmetry
> ![[ph-qft-c8-20-1.svg]]
> *ADDED figure (after PS p. 155): a diagram with an incoming $\phi$ of momentum $p$, and the corresponding diagram with an outgoing $\bar\phi$ of momentum $k = -p$. The blob and the lines $q_1, q_2, q_3$ stand for the rest of the diagram, which is the same in both.*
>
> A particle $\phi$ with four-momentum $p$ in the initial state has the same amplitude as its antiparticle $\bar\phi$ with four-momentum $k = -p$ in the final state, in an otherwise identical process:
>
> $$
> \mathcal M\bigl(\phi(p) + \cdots \to \cdots\bigr) = \mathcal M\bigl(\cdots \to \cdots + \bar\phi(k)\bigr) , \qquad k = -p .
> $$
>
> 1. Both sides are read as functions of the external four-momenta: the right side is the function on the left evaluated at $p = -k$.
> 2. Any external leg may be crossed, and in either direction: an initial particle to a final antiparticle, an initial antiparticle to a final particle, and several legs one after the other.
> 3. No four-momentum is physical on both sides, since $p^0 > 0$ and $k^0 > 0$ cannot both hold with $k = -p$: the statement needs the amplitude continued in its arguments ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-2|Principle §C8a.14.2]]).
> 4. For fermions the simple statement holds up to an overall sign that depends on the conventions for the spinors ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-3|Theorem §C8a.14.3]]).
> 5. It is a statement about the amplitude, not only about its spin-averaged square. This is what makes it strong.
>
> The relation between $e^-e^+ \to \mu^-\mu^+$ and $e^-\mu^- \to e^-\mu^-$ is crossing used twice: the initial $e^+$ becomes a final $e^-$, and the final $\mu^+$ an initial $\mu^-$ ([[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-3|Theorem §C8a.12.3]]).
>
> *Status: a principle with a proof idea. The folded derivation gives the argument of the lecture and of PS for a charged scalar field, diagram by diagram; what it does and does not show is listed at its end.*
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* amplitudes given by Feynman diagrams, order by order; shown below for a charged scalar leg.
>
> *Source: PHY 513 Lecture 21, slide 17 ("A particle (with momentum $p$) in initial state has same S-matrix as an antiparticle (with momentum $k = -p$) in final state: $\mathcal M(\phi(p) + \ldots \to \ldots) = \mathcal M(\ldots \to \ldots + \bar\phi(k))$"), slide 19 ("Crossing symmetry applies without spin-averaging"), slide 26, and recording, part C · PS §5.4, p. 155, eq. (5.67) ("In general, the $S$-matrix for any process involving a particle with momentum $p$ in the initial state is equal to the $S$-matrix for an otherwise identical process but with an antiparticle of momentum $k = -p$ in the final state") · Yu §8.5, eq. (8.288)*

^pr-c8a-14-1

> [!derivation]- Derivation (proof idea, for a charged scalar field)
> **Step 1** (the two terms of the field). The field operator of a charged scalar has two terms ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]]),
>
> $$
> \hat\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(\hat a_{\mathbf p}\,e^{-ip\cdot x} + \hat b^\dagger_{\mathbf p}\,e^{ip\cdot x}\Bigr) :
> $$
>
> the first annihilates a particle, the second creates an antiparticle ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-7|Theorem §C2a.5.7]]).
>
> **Step 2** (an incoming particle). When a particle $\phi$ of momentum $p$ comes in, some vertex must annihilate it. The $\hat a$ term of the $\hat\phi$ at that vertex does so, and what is left is the wave factor $e^{-ip\cdot x}$ ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 3).
>
> **Step 3** (an outgoing antiparticle). Let the same field at the same vertex play its other role: its $\hat b^\dagger$ term creates an antiparticle $\bar\phi$ of momentum $k$ for the final state. What is left is the wave factor $e^{+ik\cdot x}$ ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 3).
>
> **Step 4** (compare). The two factors are equal for $k = -p$. Nothing else in the diagram has changed: the same vertices, the same internal lines. In momentum space the integral over $x$ makes the momenta flowing into the vertex from the rest of the diagram, $q_1 + q_2 + \cdots$, add up to $-p$ in the first case and to $+k$ in the second, the same condition for $k = -p$. A scalar has no further external factor ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]]). So the diagrams of the two processes correspond one to one, and corresponding diagrams are the same function of the momenta.
>
> **What the derivation shows.**
> - Shown: for a spinless charged leg, the Feynman-diagram expressions of the two amplitudes agree diagram by diagram as functions of the momenta. The words above are essentially the whole argument; the details are in PS, p. 155.
> - Not shown: that the function can be continued from one physical region to the other. This is the content of [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-2|Principle §C8a.14.2]], which is stated without proof.
> - Not shown: legs with spin. Their external factors must be compared as well; for a Dirac particle they are $u(p)$ and $v(k)$, and the comparison leaves a sign ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-3|Theorem §C8a.14.3]]).
> - The argument is one about diagrams. A statement about the exact amplitude would need the relation between amplitudes and correlation functions, which the course defers ([[§C6c.1 Amplitudes from Correlation Functions|§C6c.1]]).

^der-c8a-14-1

*Uses:* [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-7|Theorem §C2a.5.7]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]]

> [!principle] Principle §C8a.14.2: The Amplitude Is an Analytic Function of the External Momenta
> As lectured, and stated without proof:
> 1. Real particles have $p^0 > 0$ and $k^0 > 0$, so the substitution $k = -p$ is formal: it takes a formula derived for physical momenta and evaluates it where an energy is negative. Mathematically the amplitude is **analytically continued**: the momenta are allowed to be complex, which connects positive to negative energies.
> 2. $\mathcal M$ is a function of complex external four-momenta.
> 3. This function is analytic: it depends on the complex variables and not on their complex conjugates.
> 4. It is smooth, except for isolated poles and branch cuts. A pole is a place where one divides by a propagator denominator that vanishes; branch cuts come with square roots and, in later calculations, logarithms. Both have physical interpretations.
> 5. An amplitude that has been computed in one kinematic region may therefore be used in others, including regions that are formal for the original process. Analyticity of amplitudes is a powerful technical tool, and it may have a deeper conceptual significance that is not yet fully understood.
>
> *What the notes contain of this.* The tree amplitudes of this chapter and their spin-averaged squares are rational functions of the momenta, polynomials divided by propagator denominators ([[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-4|Theorem §C8a.12.4]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-4|Theorem §C8a.14.4]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-5|Theorem §C8a.14.5]]; for scalars [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]]). For them items 2–4 can be seen directly, with poles and no branch cuts. Branch cuts are not yet treated in these notes.
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* a statement of the lecture about amplitudes in general; verified here only for the tree-level expressions named.
>
> *Source: PHY 513 Lecture 21, slide 18 ("Real particles have $k^0 > 0$, $p^0 > 0$ so substitution $k = -p$ is formal: the amplitude is analytically continued. $\mathcal M$ a function of complex external four-momenta. This function is analytical. It depends on complex variables, not their conjugates. It is smooth, except for isolated poles and branch-cuts with interesting physical interpretations. Analyticity of amplitudes is a powerful technical tool and it may have deeper conceptual significance"), slide 26 ("Same analytical function, but different domain of functions"), and recording, part C · PS §5.4, p. 155 ("there is no value of $p$ for which $p$ and $k$ are both physically allowed … either amplitude can be obtained from the other by analytic continuation") · the paragraph "What the notes contain of this" written here*

^pr-c8a-14-2

> [!theorem] Theorem §C8a.14.3: Crossing a Fermion Changes the Sign of Its Spin Sum
> Under $p \to -k$ the completeness relation of a particle becomes minus that of an antiparticle:
>
> $$
> \sum_{s = 1, 2}u^s(p)\bar u^s(p) = \slashed p + m \;\xrightarrow{\ p\,\to\,-k\ }\; -\slashed k + m = -(\slashed k - m) = -\sum_{r = 1, 2}v^r(k)\bar v^r(k) .
> $$
>
> 1. For fermions the substitution $p \to -k$ is imperfect: it reproduces the spin sum of the crossed leg up to an overall sign, and the overall sign of the amplitude may change. Only the overall sign goes wrong; everything else carries over.
> 2. In a spin-summed $|\mathcal M|^2$ each crossed fermion contributes one factor $-1$, to be cancelled by hand. Two crossed fermions give none: this is why no sign appeared in [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-3|Theorem §C8a.12.3]].
> 3. There are two ways to deal with the sign: modify the conventions for $v(k)$, so that crossing holds exactly, or keep the conventions and account for the minus sign by hand. Often only $|\mathcal M|^2$ is wanted and the second is easier.
> 4. Crossing symmetry applies without spin averaging: it relates the amplitudes themselves, with suitable conventions for $u(p)$ and $v(k)$ ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-1|Principle §C8a.14.1]], 5).
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]] (the spinors); *applies:* the spin sums as functions of the four-momentum; items 2–4 for amplitudes with Dirac fermions.
>
> *Source: PHY 513 Lecture 21, slide 19 ("Completeness relations show substitution $p \to -k$ is imperfect, the overall sign of the amplitude may change: $\sum_{s=1,2}u^s(p)\bar u^s(p) = \slashed p + m$, $\sum_{r=1,2}v^r(k)\bar v^r(k) = \slashed k - m$. Options: Modify conventions for $v(k)$. Account for '$-$' by hand. Crossing symmetry applies without spin-averaging"), and recording, part C · PS §5.4, p. 155, eq. (5.68) ("In practice, it is easiest to cancel by hand one minus sign for each crossed fermion. With appropriate conventions for the spinors $u(p)$ and $v(k)$, it is possible to prove the identity (5.67) without spin-averaging") · Yu §8.5, eq. (8.290) (two crossed fermions, two signs, which cancel); eqs. (8.291)–(8.295) (a convention for $v$, with a choice of branches of the square roots, in which $u(p, \lambda) = v(k, \lambda)$ at $k = -p$)*

^thm-c8a-14-3

> [!derivation]- Derivation
> **Step 1.** $\slashed p = \gamma^\mu p_\mu$ is linear in $p$, so at $p = -k$ it is $-\slashed k$, and $\slashed p + m$ becomes $-\slashed k + m = -(\slashed k - m)$. The two spin sums are [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]] and [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-8|Theorem §C5a.12.8]].
>
> **Step 2** (item 2). After the spin sums a fermion line is a trace that contains one factor $\slashed p \pm m$ for each of its two external legs ([[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-7|Theorem §C8a.7.7]], part 2). Crossing one leg replaces its factor by minus the factor of the crossed leg, and the trace is linear in each factor: one sign. [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^der-c8a-12-3|Derivation §C8a.12.3]], Steps 2–3, are two instances.
>
> **What the derivation shows.**
> - ⚑ By-product: $|\mathcal M|^2$ summed over spins is positive in each physical region, so a crossed expression that comes out negative has missed a sign of this kind.
> - The spinors $u(p)$ and $v(k)$ themselves are not related by this computation; that is the matter of conventions of item 3.

^der-c8a-14-3

*Uses:* [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-8|Theorem §C5a.12.8]], [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-7|Theorem §C8a.7.7]]

## Mandelstam variables

> [!definition] Definition §C8a.14.1: Mandelstam Variables (Course Form)
> ![[ph-qft-c8-20-2.svg]]
> *The labels of a general $2 \to 2$ process, time running upward (after PHY 513 Lecture 21, slide 20, and PS p. 156), and the pair of momenta that enters each variable.*
>
> For a general $2 \to 2$ process with incoming momenta $p, p'$ and outgoing momenta $k, k'$, the **Mandelstam variables** are the scalar combinations
>
> $$
> s = (p + p')^2 = (k + k')^2 , \qquad t = (k - p)^2 = (k' - p')^2 , \qquad u = (k' - p)^2 = (k - p')^2 .
> $$
>
> 1. $s$ is the square of the centre-of-mass energy: in the frame where $\mathbf p + \mathbf p' = \mathbf 0$, $p + p'$ is the total energy. Being an invariant, it measures in every frame how hard the particles hit each other.
> 2. $t$ is the square of the momentum transfer between $p$ and $k$. In a frame where the two energies are equal it is minus the square of the change of three-momentum, and it can be very small.
> 3. $u$ is the third variable: $t$ with the two outgoing momenta exchanged, $k \leftrightarrow k'$.
> 4. The second form of each follows from momentum conservation, $p + p' = k + k'$.
>
> *Equivalently,* this is [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]] with $p_1 = p$, $p_2 = p'$, $p_3 = k$, $p_4 = k'$: the same assignment of $t$ and $u$. Which outgoing momentum is called $k$ is a choice; by convention $t$ is formed from the initial and final momenta of the most similar particles (PS p. 156). The sum rule $s + t + u = \sum_im_i^2$ is [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], part 1: only two of the three are independent.
>
> *Model:* any (kinematics); *applies:* any $2 \to 2$ process with on-shell external momenta and momentum conservation.
>
> *Source: PHY 513 Lecture 21, slide 20 ("Mandelstam variables: scalar combinations of external momenta: $s = (p + p')^2 = (k + k')^2 = (\text{cms energy})^2$, $t = (k - p)^2 = (k' - p')^2 = \text{momentum transfer}$, $u = (k' - p)^2 = (k - p')^2$"), slide 21 ("These kinematic variables are designed for crossing symmetry and for analyticity more generally"), and recording, part C · PS §5.4, p. 156, eq. (5.69) · Yu §8.5, eqs. (8.296), (8.302)–(8.303) (his labels: $k_1, k_2$ in, $p_1, p_2$ out)*

^def-c8a-14-1

> [!definition] Definition §C8a.14.2: Channel
> When a $2 \to 2$ diagram contains exactly one virtual particle, the square of the momentum on its line is one of the Mandelstam variables. The diagram, and the virtual particle, are said to be in the **$s$-channel**, the **$t$-channel** or the **$u$-channel** according to whether that momentum is $p + p'$, $k - p$ or $k' - p$. The channel can be read from the form of the diagram.
>
> *Equivalently,* these are the $s$-, $t$- and $u$-channel exchanges of [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]], there for scalar particles.
>
> *Model:* none (a name); *applies:* tree diagrams of $2 \to 2$ processes with one internal line.
>
> *Source: PHY 513 Lecture 21, slides 21–23 (titles "s-Channel", "t-Channel", "Channels in Yukawa Theory"), and recording, part C · PS §5.4, p. 157 ("When a 2-body → 2-body diagram contains only one virtual particle, it is conventional to describe that particle as being in a certain 'channel'. The channel can be read from the form of the Feynman diagram") · Yu §8.5 (the paragraph before eq. (8.310))*

^def-c8a-14-2

## The two processes in Mandelstam variables

> [!theorem] Theorem §C8a.14.4: Annihilation in the s-Channel
> For $e^-(p) + e^+(p') \to \mu^-(k) + \mu^+(k')$ at order $e^2$ with all masses neglected,
>
> $$
> \frac14\sum_{\rm spins}|\mathcal M|^2 = \frac{2e^4}{s^2}\bigl[t^2 + u^2\bigr] .
> $$
>
> 1. The photon is in the $s$-channel ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-2|Def. §C8a.14.2]]): its momentum is the total momentum, $q^2 = s$, and the factor $\frac{1}{s^2}$ is its propagator squared. The virtual photon carries the entire energy of the process.
> 2. Annihilation is dramatic: the initial particles disappear, and new particles appear.
> 3. The expression has a pole at $s = 0$, a double pole in the square. A physical process never comes near it: $s = E_{\rm cm}^2$ is at least the square of the rest energy of the initial pair, and with the muon mass at least $4m_\mu^2$ ([[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-3|Theorem §C8a.6.3]]). On the physical region the expression is a smooth function of $s$, $t$, $u$.
> 4. In the centre-of-mass frame it is $e^4(1 + \cos^2\theta)$, [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-3|Theorem §C8a.8.3]] at $m_\mu = 0$.
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* order $e^2$, unpolarized, all masses neglected.
>
> *Source: PHY 513 Lecture 21, slide 21 ("$e^-e^+$ Annihilation (in massless limit): $\frac14\sum_{\rm spin}|\mathcal M|^2 = \frac{2e^4}{s^2}[t^2 + u^2]$. Annihilation is dramatic: initial particles disappear. Virtual photon carries entire energy in process. An isolated pole when $s = 0$"), and recording, part C · PS §5.4, p. 156, eq. (5.70) ("In this limit we have $t = -2p\cdot k = -2p'\cdot k'$ and $u = -2p\cdot k' = -2p'\cdot k$, while of course $s = (p + p')^2 = q^2$") · numerical check: `qft-C/tools/l21/verify.py`*

^thm-c8a-14-4

> [!derivation]- Derivation
> **Step 1** (the invariant form). [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|Theorem §C8a.7.6]] with $m_e = m_\mu = 0$ (its item 4): $\frac14\sum|\mathcal M|^2 = \frac{8e^4}{q^4}\bigl[(p\cdot k)(p'\cdot k') + (p\cdot k')(p'\cdot k)\bigr]$, $q = p + p'$.
>
> **Step 2** (the dot products). With all four momenta lightlike, $t = (k - p)^2 = k^2 + p^2 - 2p\cdot k = -2p\cdot k$, and from the second form $t = (k' - p')^2 = -2p'\cdot k'$. In the same way $u = (k' - p)^2 = -2p\cdot k'$ and $u = (k - p')^2 = -2p'\cdot k$; and $s = (p + p')^2 = q^2$.
>
> **Step 3** (insert). $(p\cdot k)(p'\cdot k') = \frac{t}{2}\cdot\frac{t}{2}$ and $(p\cdot k')(p'\cdot k) = \frac{u}{2}\cdot\frac{u}{2}$: $\frac{8e^4}{s^2}\bigl[\bigl(\frac t2\bigr)^2 + \bigl(\frac u2\bigr)^2\bigr] = \frac{2e^4}{s^2}\bigl[t^2 + u^2\bigr]$.
>
> **Step 4** (item 4). With $t = -\frac s2(1 - \cos\theta)$, $u = -\frac s2(1 + \cos\theta)$ ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-7|Theorem §C8a.14.7]] with $m = 0$): $\frac{2e^4}{s^2}\cdot\frac{s^2}{4}\bigl[(1 - \cos\theta)^2 + (1 + \cos\theta)^2\bigr] = e^4(1 + \cos^2\theta)$.
>
> **What the derivation shows.**
> - Which combination stands in the numerator has to be computed; what matters for the physics is the denominator, the $\frac{1}{s^2}$ of the propagator.
> - ⚑ By-product: the expression is symmetric under $t \leftrightarrow u$, the exchange of the names $k$ and $k'$ → [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-6|Theorem §C8a.14.6]], 2.

^der-c8a-14-4

*Uses:* [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|Theorem §C8a.7.6]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-1|Def. §C8a.14.1]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-7|Theorem §C8a.14.7]]

> [!theorem] Theorem §C8a.14.5: Scattering in the t-Channel
> For $e^-(p) + \mu^-(p') \to e^-(k) + \mu^-(k')$ at order $e^2$ with all masses neglected,
>
> $$
> \frac14\sum_{\rm spins}|\mathcal M|^2 = \frac{2e^4}{t^2}\bigl[s^2 + u^2\bigr] .
> $$
>
> 1. The photon is in the $t$-channel: its momentum is the momentum transfer, $q^2 = t$, and the factor $\frac{1}{t^2}$ is its propagator squared. In the words of the slide, the virtual photon carries the interaction energy.
> 2. Scattering is gentle if the particles pass far from one another.
> 3. The expression has an isolated pole at $t = 0$, and $t = 0$ is forward scattering, at the edge of the physical region: hence the large forward scattering of [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-6|Theorem §C8a.13.6]]. There the exchanged particle is nearly on shell: one particle creates a field, the other feels it, and the process is nearly classical.
> 4. In the centre-of-mass frame it is $2e^4\,\frac{4 + (1 + \cos\theta)^2}{(1 - \cos\theta)^2}$ ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-5|Theorem §C8a.13.5]], 3): the angle enters through the numerator and, more strongly, through the denominator.
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* order $e^2$, unpolarized, all masses neglected, $t \ne 0$.
>
> *Source: PHY 513 Lecture 21, slide 22 ("$e^-\mu^-$ Scattering (in massless limit): $\frac14\sum_{\rm spin}|\mathcal M|^2 = \frac{2e^4}{t^2}[s^2 + u^2]$. Scattering is 'gentle' if particles pass far from one another. Virtual photon carries interaction energy. Isolated pole when $t = 0$ ⇒ large forward scattering"), and recording, part C · PS §5.4, p. 157, eq. (5.71) ("You can easily check that this agrees with (5.61) in the massless limit") · numerical check: `qft-C/tools/l21/verify.py`*

^thm-c8a-14-5

> [!derivation]- Derivation
> **Step 1** (the invariant form). [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-4|Theorem §C8a.12.4]] with $m_\mu = 0$, in the labels $p = p_1$, $p' = p_2$, $k = p_1'$, $k' = p_2'$: $\frac14\sum|\mathcal M|^2 = \frac{8e^4}{q^4}\bigl[(p\cdot k')(k\cdot p') + (p\cdot p')(k\cdot k')\bigr]$, $q = p - k$.
>
> **Step 2** (the dot products). With all four momenta lightlike, as in Step 2 of [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^der-c8a-14-4|Derivation §C8a.14.4]]: $p\cdot k' = k\cdot p' = -\frac u2$, and $s = (p + p')^2 = 2p\cdot p'$, $s = (k + k')^2 = 2k\cdot k'$, so $p\cdot p' = k\cdot k' = \frac s2$; $q^2 = (p - k)^2 = t$.
>
> **Step 3** (insert). $\frac{8e^4}{t^2}\bigl[\bigl(\frac u2\bigr)^2 + \bigl(\frac s2\bigr)^2\bigr] = \frac{2e^4}{t^2}\bigl[s^2 + u^2\bigr]$.
>
> **Step 4** (item 4). $s = E_{\rm cm}^2$, $t = -\frac s2(1 - \cos\theta)$, $u = -\frac s2(1 + \cos\theta)$: $\frac{2e^4\,s^2\bigl[1 + \frac14(1 + \cos\theta)^2\bigr]}{\frac14s^2(1 - \cos\theta)^2} = 2e^4\,\frac{4 + (1 + \cos\theta)^2}{(1 - \cos\theta)^2}$.
>
> **What the derivation shows.**
> - ⚑ By-product: the formula is no more complicated than that of annihilation; its angular dependence is, because here the denominator depends on the angle and vanishes in the forward direction.

^der-c8a-14-5

*Uses:* [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-4|Theorem §C8a.12.4]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-1|Def. §C8a.14.1]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-7|Theorem §C8a.14.7]]

> [!theorem] Theorem §C8a.14.6: Crossing Exchanges s and t
> Let $F(a, b, c) \equiv \frac{2e^4}{a^2}\bigl[b^2 + c^2\bigr]$. With the Mandelstam variables of each process,
>
> $$
> \frac14\sum_{\rm spins}|\mathcal M|^2\Big|_{e^-e^+ \to \mu^-\mu^+} = F(s, t, u) , \qquad \frac14\sum_{\rm spins}|\mathcal M|^2\Big|_{e^-\mu^- \to e^-\mu^-} = F(t, s, u) :
> $$
>
> the same function with $s$ and $t$ exchanged. The crossing is: the initial $e^+$ becomes a final $e^-$, and the final $\mu^+$ an initial $\mu^-$.
> 1. If the outgoing $\mu^+$ of the annihilation process carries the momentum $k$, as drawn on the slides, crossing sends $s \to t$, $t \to s$, $u \to u$.
> 2. With the labels of [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-2|Theorem §C8a.6.2]], where the $\mu^-$ carries $k$, the substitution of [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-3|Theorem §C8a.12.3]] sends $s \to t$, $t \to u$, $u \to s$. The result is the same, because $F$ is symmetric in its last two arguments.
> 3. The two formulas are identical as functions. What differs is the region in which each is used: in annihilation the variable in the denominator is necessarily large and positive; in scattering it is negative and may be close to zero. The interpretation of the variables in terms of space-time kinematics has changed, and nothing else.
> 4. The effort of finding the function is therefore spent once.
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* order $e^2$, unpolarized, all masses neglected.
>
> *Source: PHY 513 Lecture 21, slide 24 ("Crossing: $e^+$ initial → $e^-$ final and $\mu^+$ final → $\mu^-$ initial. ⇒ $s \to t$ and $t \to s$"), and recording, part C · PS §5.4, pp. 156–157 ("the crossing relations tell us to change the sign of $p'$, the positron momentum, and reinterpret it as the momentum of the outgoing electron. Therefore $s = (p + p')^2$ becomes what we would now call $t$ … Similarly, $t$ becomes $s$, while $u$ remains unchanged"; "while (5.70) and (5.71) look quite similar, they are physically very different") · item 2 derived here; numerical check: `qft-C/tools/l21/verify.py`*

^thm-c8a-14-6

> [!derivation]- Derivation
> **Step 1** (the variables of the two processes). Annihilation, labels of [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-2|Theorem §C8a.6.2]]: $s = (p + p')^2$, $t = (k - p)^2$, $u = (k' - p)^2$. Scattering, labels of [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution|§C8a.12]] inserted in [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-1|Def. §C8a.14.1]]: $s_{\rm sc} = (p_1 + p_2)^2$, $t_{\rm sc} = (p_1' - p_1)^2$, $u_{\rm sc} = (p_2' - p_1)^2$.
>
> **Step 2** (the substitution). Under $p \to p_1$, $p' \to -p_1'$, $k \to p_2'$, $k' \to -p_2$:
>
> $$
> s \to (p_1 - p_1')^2 = t_{\rm sc} , \qquad t \to (p_2' - p_1)^2 = u_{\rm sc} , \qquad u \to (-p_2 - p_1)^2 = s_{\rm sc} .
> $$
>
> **Step 3** (the function). $F(s, t, u) \to F(t_{\rm sc}, u_{\rm sc}, s_{\rm sc}) = \frac{2e^4}{t_{\rm sc}^2}\bigl[u_{\rm sc}^2 + s_{\rm sc}^2\bigr] = F(t_{\rm sc}, s_{\rm sc}, u_{\rm sc})$, which is [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-5|Theorem §C8a.14.5]]. No sign arises: two fermions are crossed ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-3|Theorem §C8a.14.3]], 2).
>
> **Step 4** (item 1). Calling the outgoing $\mu^+$ $k$ and the $\mu^-$ $k'$ exchanges $t$ and $u$ of the annihilation process and leaves $F(s, t, u)$ unchanged. The crossed muon then carries $k$, and $t = (k - p)^2 \to (-p_2 - p_1)^2 = s_{\rm sc}$, $u = (k' - p)^2 \to (p_2' - p_1)^2 = u_{\rm sc}$.
>
> **What the derivation shows.**
> - The Mandelstam variables turn the substitution of four-vectors into a permutation of three numbers.
> - ⚑ By-product: $s + t + u$ is unchanged by a permutation, so the sum rule holds in each region ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]]).

^der-c8a-14-6

*Uses:* [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-4|Theorem §C8a.14.4]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-5|Theorem §C8a.14.5]], [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-3|Theorem §C8a.12.3]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-1|Def. §C8a.14.1]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams|P8, Shortcut: crossing]]

## Channels and their angular dependence

> [!theorem] Theorem §C8a.14.7: The Mandelstam Variables in the Centre-of-Mass Frame for Equal Masses
> For a $2 \to 2$ process in which all four particles have the same mass $m$, in the centre-of-mass frame with $p = (E, \mathbf p)$ along $\hat{\mathbf z}$, $p' = (E, -\mathbf p)$, $k = (E, \mathbf k)$, $k' = (E, -\mathbf k)$, $|\mathbf k| = |\mathbf p|$, and $\theta$ the angle between $\mathbf k$ and $\mathbf p$:
>
> $$
> s = (2E)^2 = E_{\rm cm}^2 , \qquad t = -2\mathbf p^2(1 - \cos\theta) , \qquad u = -2\mathbf p^2(1 + \cos\theta) .
> $$
>
> 1. $s$ does not depend on the angle. $t \to 0$ for $\theta \to 0$, and $u \to 0$ for $\theta \to \pi$.
> 2. $s + t + u = 4(E^2 - \mathbf p^2) = 4m^2$; in general $s + t + u = \sum_im_i^2$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], 1). The three are therefore not independent variables: $u$ is the sum of the squared masses minus $s$ and $t$, and an amplitude is a function of two variables.
>
> *Equivalently,* $t$ is [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], part 3, and the three values are Step 5 of [[§C6c.6 Feynman Rules for Amplitudes#^der-c6c-6-4|Derivation §C6c.6.4]].
>
> *Model:* any (kinematics); *applies:* on-shell momenta, all four masses equal (in particular all zero).
>
> *Source: PHY 513 Lecture 21, slide 25 ("Center of mass kinematics (all particles the same mass): $p = (E, p\hat z)$, $p' = (E, -p\hat z)$, $k = (E, \vec p)$, $k' = (E, -\vec p)$. $s = (p + p')^2 = (2E)^2 = E_{\rm cm}^2$, $t = (k - p)^2 = -2\vec p^{\,2}(1 - \cos\theta)$, $u = (k' - p)^2 = -2\vec p^{\,2}(1 + \cos\theta)$. Note: $s + t + u = 4(E^2 - \vec p^{\,2}) = 4m^2$. (Generally $s + t + u = \sum_im_i^2$)"; the slide writes $\vec p$ also for the outgoing momentum, here $\mathbf k$), and recording, part C · PS §5.4, pp. 157–158, eqs. (5.72)–(5.73) · Yu §8.5, eqs. (8.315)–(8.318)*

^thm-c8a-14-7

> [!derivation]- Derivation
> **Step 1.** $p + p' = (2E, \mathbf 0)$, so $s = 4E^2$.
>
> **Step 2.** $k - p = (0, \mathbf k - \mathbf p)$: the energies are equal. $t = -|\mathbf k - \mathbf p|^2 = -(\mathbf k^2 + \mathbf p^2 - 2\mathbf k\cdot\mathbf p) = -2\mathbf p^2(1 - \cos\theta)$.
>
> **Step 3.** $k' - p = (0, -\mathbf k - \mathbf p)$: $u = -|\mathbf k + \mathbf p|^2 = -2\mathbf p^2(1 + \cos\theta)$.
>
> **Step 4.** $s + t + u = 4E^2 - 4\mathbf p^2 = 4m^2$.

^der-c8a-14-7

*Uses:* [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-1|Def. §C8a.14.1]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]]

> [!example] Example §C8a.14.1: Channels in Yukawa Theory
> ![[ph-qft-c8-20-3.svg]]
> *The three diagrams with one virtual scalar (dashed), time running upward (after PHY 513 Lecture 21, slide 23, and PS p. 157). Under each: the propagator factor and where it is largest.*
>
> As an illustration, let the exchanged particle be massive, the scalar $\phi$ of Yukawa theory ([[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]) in place of the photon. Its propagator gives, for the three channels of [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-2|Def. §C8a.14.2]],
>
> $$
> s\text{-channel: } \mathcal M \sim \frac{1}{s - m_\phi^2} , \qquad t\text{-channel: } \mathcal M \sim \frac{1}{t - m_\phi^2} , \qquad u\text{-channel: } \mathcal M \sim \frac{1}{u - m_\phi^2} ,
> $$
>
> where $\sim$ keeps the propagator factor only. Each channel has a characteristic angular dependence ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-7|Theorem §C8a.14.7]]):
> 1. $s$-channel: the denominator does not depend on the angle; not much angular dependence comes from it.
> 2. $t$-channel: $t - m_\phi^2 = -\bigl[2\mathbf p^2(1 - \cos\theta) + m_\phi^2\bigr]$; the amplitude is largest in the forward direction.
> 3. $u$-channel: $u - m_\phi^2 = -\bigl[2\mathbf p^2(1 + \cos\theta) + m_\phi^2\bigr]$; the amplitude is largest in the backward direction.
>
> Often several diagrams contribute to a process, but one dominates and gives the characteristic angular dependence: the one whose denominator is closest to zero, that is the one whose exchanged particle is closest to its mass shell. This is why the channels matter experimentally. For photon exchange it happens in scattering and cannot happen in annihilation ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-4|Theorem §C8a.14.4]], 3; [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-5|Theorem §C8a.14.5]], 3). Reading an amplitude by channels is asking about the particle that is exchanged: is it nearly on shell or far from it.
>
> The full amplitudes with these propagators: for scalar particles, [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]]; the $t$-channel exchange of a scalar between two fermions, [[§C8a.4 Feynman Rules for QED#^ex-c8a-4-1|Example §C8a.4.1]] (the Yukawa twin).
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* tree level, the propagator factors only; the angular statements for equal masses in the centre-of-mass frame.
>
> *Source: PHY 513 Lecture 21, slide 23 ("s-channel: $\mathcal M \sim \frac{1}{s - m_\phi^2}$; t-channel: $\mathcal M \sim \frac{1}{t - m_\phi^2}$; u-channel: $\mathcal M \sim \frac{1}{u - m_\phi^2}$. Each 'channel' has characteristic angular dependence. Often: several diagrams contribute but one dominates and gives characteristic angular dependence"), and recording, part C · PS §5.4, p. 157 ("each channel leads to a characteristic angular dependence of the cross section") · Yu §8.5, eqs. (8.310)–(8.312)*

^ex-c8a-14-1

> [!remark] Remark: Lecture 21 at a glance
> - The process: an electron scattering off a muon. The same particles in the initial and the final state; their four-momenta change. $i\mathcal M = \frac{ie^2}{q^2}\bigl[\bar u(p_1')\gamma^\mu u(p_1)\bigr]\bigl[\bar u(p_2')\gamma_\mu u(p_2)\bigr]$, $q = p_1 - p_1'$ ([[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-1|Theorem §C8a.12.1]]).
> - The diagram is nearly identical to that of $e^+e^-$ annihilation, and the algebra is related to it by the substitution $p \to p_1$, $p' \to -p_1'$, $k \to p_2'$, $k' \to -p_2$ ([[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-3|Theorem §C8a.12.3]]): $\frac14\sum|\mathcal M|^2 = \frac{8e^4}{q^4}\bigl[(p_1\cdot p_2')(p_1'\cdot p_2) + (p_1\cdot p_2)(p_1'\cdot p_2') - m_\mu^2\,p_1\cdot p_1'\bigr]$ at $m_e = 0$ ([[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-4|Theorem §C8a.12.4]]).
> - In the centre-of-mass frame $\frac{d\sigma}{d\Omega} = \frac{\alpha^2}{2k^2(E + k)^2(1 - \cos\theta)^2}\bigl[(E + k\cos\theta)^2 + (E + k)^2 - m_\mu^2(1 - \cos\theta)\bigr]$ ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-4|Theorem §C8a.13.4]]); at high energy $\frac{\alpha^2}{2E_{\rm cm}^2}\frac{4 + (1 + \cos\theta)^2}{(1 - \cos\theta)^2}$ ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-5|Theorem §C8a.13.5]]); at small angles $\propto 1/\theta^4$, from a virtual photon nearly on shell ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-6|Theorem §C8a.13.6]]).
> - Crossing symmetry: an initial particle may be exchanged for a final antiparticle with $k = -p$, and the other way round ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-1|Principle §C8a.14.1]]); for fermions up to a sign ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-3|Theorem §C8a.14.3]]).
> - The symmetry is of an unfamiliar kind: the two amplitudes are the same analytic function, evaluated on different domains of its arguments ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-2|Principle §C8a.14.2]]). In Mandelstam variables: $\frac{2e^4}{s^2}(t^2 + u^2)$ and $\frac{2e^4}{t^2}(s^2 + u^2)$, with $s$ and $t$ exchanged ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-6|Theorem §C8a.14.6]]).
>
> *Source: PHY 513 Lecture 21, slide 26 ("Physics process in this lecture: $e^-$ scattering off $\mu^-$. Same particles in initial and final state, 4-momenta change. Feynman diagram nearly identical to $e^-e^+$ annihilation. Algebraic manipulations related by simple substitutions. Crossing symmetry: initial particle to final anti-particle. Same analytical function, but different domain of functions"), and recording, part C*

^rem-c8a-14-1

> [!remark]- Connections
> - The Mandelstam variables were introduced as notation in the first problem set, with the sum rule and the elastic form of $t$ — [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]]; this lecture gives them their use.
> - The channels of the scalar theories, with all three propagators in one amplitude — [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]].
> - The sign of $q^2$ separated the annihilation photon from the exchanged photon before the names $s$ and $t$ were used — [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^pr-c8a-6-4|Principle §C8a.6.4]].
> - The two terms of the complex field, one annihilating particles and one creating antiparticles, are what the proof idea exchanges; the Dirac field has the same two terms with the wave functions $u$ and $v$ — [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]].
> - The two completeness relations behind the fermion sign — [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-8|Theorem §C5a.12.8]].
> - Poles of propagators and the $i\varepsilon$ that defines them on the real axis — [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]].
> - Back: the substitution that this section explains — [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-3|Theorem §C8a.12.3]]; the forward peak that the pole at $t = 0$ produces — [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-6|Theorem §C8a.13.6]]. Forward: Compton scattering (Lecture 22; PS §5.5; planned).
