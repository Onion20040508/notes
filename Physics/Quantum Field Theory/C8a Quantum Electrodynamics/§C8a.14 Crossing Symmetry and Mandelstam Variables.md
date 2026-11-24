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

*Sources: PHY 513 Lecture 21 (Larsen, 18 Nov 2026, "Crossing Symmetry"; a recorded lecture in three parts), slides 17–26 (Part C), and recording, part C · Peskin & Schroeder, An Introduction to Quantum Field Theory, §5.4, pp. 155–158, eqs. (5.67)–(5.73) and the figures of pp. 155–157 · Yu Zhao-Huan, 量子场论讲义, §8.5, eqs. (8.288), (8.290)–(8.296), (8.302)–(8.303), (8.310)–(8.312), (8.315)–(8.318) (page images checked) · closing part, added 2026-11-23 after Problem Set 11 was submitted: PHY 513, Problem Set 11, Problem 3 "Mandelstam variables" (statement, and the user's solution, used as written); Yu §8.5, eqs. (8.297)–(8.301).*

Why could the scattering result be read off from the annihilation result? [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-3|Theorem §C8a.12.3]] found a substitution of momenta that turns one spin-averaged square into the other. This section states the general fact behind it, **crossing symmetry** ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-1|Principle §C8a.14.1]]): a particle in the initial state and its antiparticle in the final state, with the opposite four-momentum, have the same amplitude. Two qualifications come with it. The opposite four-momentum is not physical, so the statement is about the amplitude as an analytic function ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-2|Principle §C8a.14.2]]); and for fermions there is a sign ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-3|Theorem §C8a.14.3]]). The **Mandelstam variables** $s$, $t$, $u$ ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-1|Def. §C8a.14.1]]) are the variables in which crossing is simple: the two processes of this chapter are $\frac{2e^4}{s^2}(t^2 + u^2)$ and $\frac{2e^4}{t^2}(s^2 + u^2)$ ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-4|Theorem §C8a.14.4]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-5|Theorem §C8a.14.5]]), one function with $s$ and $t$ exchanged ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-6|Theorem §C8a.14.6]]). They also name the **channels** of a diagram ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-2|Def. §C8a.14.2]]), each with its own angular dependence ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-7|Theorem §C8a.14.7]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^ex-c8a-14-1|Example §C8a.14.1]]). The variables themselves are not new: they are [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]], with the sum rule of [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], and the channels of the scalar theories are [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]]; this section states them in the form of the lecture and links those homes. A closing part (Problem Set 11, Problem 3) expresses every scalar product of the four momenta through $s$, $t$, $u$ and the masses ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-8|Theorem §C8a.14.8]]) and extends the variables to more than four particles: for five massless particles ten two-particle invariants with $\sum s_{ij} = 0$, five of them independent ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-3|Def. §C8a.14.3]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-9|Theorem §C8a.14.9]]–[[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-11|Theorem §C8a.14.11]]).

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

> [!remark] Remark: Yu's picture of crossing, and the sign for fermions
> Yu states the principle in the same form (his $\Phi$ with $p^\mu$ in the initial state, $\bar\Phi$ with $k^\mu = -p^\mu$ in the final state) and adds a way to picture it: a particle moving forward in time is equivalent to its antiparticle moving backward in time, and such an antiparticle has negative energy and the opposite momentum. This is a picture of the substitution $k = -p$, not a physical state: a real antiparticle has $k^0 > 0$, which is why the amplitude has to be continued analytically ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-2|Principle §C8a.14.2]]).
>
> For a fermion the crossing brings one sign per crossed line ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-3|Theorem §C8a.14.3]]). It is bookkeeping of the same kind as the relative sign between diagrams, which also comes only from the order of fermion operators ([[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]]; [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^rem-c8a-15-3|§C8a.15, Remark: Yu's picture: the same electron line, deformed]]).
>
> *Source: Yu §8.5, eq. (8.288), Figure 8.11 and the two sentences after it · written for the user's question of 2026-11-24*

^rem-c8a-14-3

> [!remark] ★ Remark: Where the general proof of crossing comes from
> The derivation above compares Feynman diagrams and leaves the exact amplitude open. The general argument uses the reduction formula of Lehmann, Symanzik and Zimmermann (LSZ), which writes an $n \to m$ amplitude as the $(n + m)$-point correlation function with one operation per external particle: a Klein–Gordon operator acting on the field of that particle, and a Fourier transform, with $e^{-ip\cdot x}$ for an incoming particle and $e^{+iq\cdot y}$ for an outgoing one. Incoming and outgoing particles are told apart only by the sign in the exponent. Moving a particle of momentum $p$ from the initial state to the final state, as an antiparticle of momentum $k$, is therefore the substitution $p \to -k$ in the same expression, which is the principle. The course does not derive the LSZ formula (second semester; [[§C6c.1 Amplitudes from Correlation Functions|§C6c.1]]), so this is recorded here as where the proof lives, not as a proof.
>
> *Source: Yu §10.3, eq. (10.107) (the LSZ reduction formula for a real scalar field) and the paragraph after it, which ends "这就是由 (8.288) 式描述的交叉对称性"; beyond PHY 513*

^rem-c8a-14-4

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
> 3. $u$ is the third variable: $t$ with the two outgoing momenta exchanged, $k \leftrightarrow k'$. What it means when the two particles are identical: [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^rem-c8a-14-2|Remark: The variable u for identical particles]].
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

## Scalar products in Mandelstam variables, and more than four particles

Two questions about the variables themselves, from Problem Set 11, Problem 3, as the user solved it. First: are $s$, $t$, $u$ enough? Every scalar product of the four momenta of a $2 \to 2$ process is a combination of them and of the masses ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-8|Theorem §C8a.14.8]]), which is why a spin-summed squared amplitude can always be written in them, as in Theorems §C8a.14.4–§C8a.14.5. Second: what replaces them when more particles take part? For five massless particles there are ten two-particle invariants $s_{ij}$ ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-3|Def. §C8a.14.3]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-9|Theorem §C8a.14.9]]), with the one relation $\sum s_{ij} = 0$ in place of $s + t + u = \sum m^2$ ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-10|Theorem §C8a.14.10]]), and five of them are independent ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-11|Theorem §C8a.14.11]]). In this part the momenta are labelled $p_1, p_2$ (incoming) and $p_3, p_4$ (outgoing), as in the problem set and in [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]]; in the course labels of [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-1|Def. §C8a.14.1]] these are $p, p', k, k'$.

> [!theorem] Theorem §C8a.14.8: Every Scalar Product of the Four Momenta in Terms of the Masses and s, t, u
> For a $2 \to 2$ process with incoming momenta $p_1, p_2$ and outgoing momenta $p_3, p_4$, on shell, $p_i^2 = m_i^2$, with $p_1 + p_2 = p_3 + p_4$, and with $s = (p_1 + p_2)^2$, $t = (p_1 - p_3)^2$, $u = (p_1 - p_4)^2$, there are 10 scalar products $p_i\cdot p_j$ with $i \le j$:
> 1. the four with $i = j$ are fixed by the mass shell, $p_i^2 = m_i^2$;
> 2. the six others are
>
> $$
> \begin{aligned}
> p_1\cdot p_2 &= \tfrac12\bigl(s - m_1^2 - m_2^2\bigr) , & p_1\cdot p_3 &= \tfrac12\bigl(m_1^2 + m_3^2 - t\bigr) , & p_1\cdot p_4 &= \tfrac12\bigl(m_1^2 + m_4^2 - u\bigr) ,\\
> p_3\cdot p_4 &= \tfrac12\bigl(s - m_3^2 - m_4^2\bigr) , & p_2\cdot p_4 &= \tfrac12\bigl(m_2^2 + m_4^2 - t\bigr) , & p_2\cdot p_3 &= \tfrac12\bigl(m_2^2 + m_3^2 - u\bigr) .
> \end{aligned}
> $$
>
> So any Lorentz-invariant scalar product of the four momenta is expressed in terms of the four masses and the three Mandelstam invariants: $s$, $t$, $u$ form a complete set of relativistic invariants of the process, and since an unpolarized squared amplitude $\overline{|\mathcal M|^2}$ is a function of these scalar products only, the three variables suffice to express it for any $2 \to 2$ process. By the sum rule ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], 1) two of the three are independent.
>
> *Equivalently,* part 2 is [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]], item 1, with $A, B, 1, 2 \to 1, 2, 3, 4$ (the same six relations, written there with the factor 2 on the left; that theorem adds the $\varepsilon$-contraction of the four momenta). In the massless limit they are $t = -2p\cdot k$, $u = -2p\cdot k'$, $s = 2p\cdot p'$ of Step 2 of [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^der-c8a-14-4|Derivation §C8a.14.4]].
>
> *Model:* any (kinematics); *applies:* on-shell momenta of any $2 \to 2$ process with momentum conservation, independent of the dynamics.
>
> *Source: PHY 513, Problem Set 11, Problem 3(a) (statement: "Show that any possible Lorentz-invariant scalar product of these four momenta can be expressed in terms of the four masses and the three Mandelstam invariants"; the user's solution) · Yu §8.5, eqs. (8.297)–(8.300) and the sentence after them ("因为非极化振幅模方 $\overline{|\mathcal M|^2}$ 只是这些四维动量内积的函数，所以用 3 个 Mandelstam 变量就足以表达任意 $2 \to 2$ 散射过程的 $\overline{|\mathcal M|^2}$"; his labels $k_1, k_2$ in, $p_1, p_2$ out) · PHY 513 Lecture 21, recording, part C (the third variable $u$ completes the set of relativistic invariants) · checked numerically for random masses and momenta (`qft-C/tools/hw11/verify.py`)*

^thm-c8a-14-8

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 3(a).
>
> **Step 1** (count). There are 10 scalar products $p_i\cdot p_j$ with $i \le j$. The four with $i = j$ are fixed by the mass shell, $p_i^2 = m_i^2$.
>
> **Step 2** (expand the definitions).
>
> $$
> \begin{aligned}
> s &= p_1^2 + p_2^2 + 2\,p_1\cdot p_2 &&\Rightarrow\quad p_1\cdot p_2 = \tfrac12\bigl(s - m_1^2 - m_2^2\bigr) ,\\
> t &= p_1^2 + p_3^2 - 2\,p_1\cdot p_3 &&\Rightarrow\quad p_1\cdot p_3 = \tfrac12\bigl(m_1^2 + m_3^2 - t\bigr) ,\\
> u &= p_1^2 + p_4^2 - 2\,p_1\cdot p_4 &&\Rightarrow\quad p_1\cdot p_4 = \tfrac12\bigl(m_1^2 + m_4^2 - u\bigr) .
> \end{aligned}
> $$
>
> **Step 3** (momentum conservation). By $p_1 + p_2 = p_3 + p_4$, equivalently $p_1 - p_3 = p_4 - p_2$ and $p_1 - p_4 = p_3 - p_2$. Hence
>
> $$
> \begin{aligned}
> s &= (p_3 + p_4)^2 = p_3^2 + p_4^2 + 2\,p_3\cdot p_4 &&\Rightarrow\quad p_3\cdot p_4 = \tfrac12\bigl(s - m_3^2 - m_4^2\bigr) ,\\
> t &= (p_4 - p_2)^2 = p_2^2 + p_4^2 - 2\,p_2\cdot p_4 &&\Rightarrow\quad p_2\cdot p_4 = \tfrac12\bigl(m_2^2 + m_4^2 - t\bigr) ,\\
> u &= (p_3 - p_2)^2 = p_2^2 + p_3^2 - 2\,p_2\cdot p_3 &&\Rightarrow\quad p_2\cdot p_3 = \tfrac12\bigl(m_2^2 + m_3^2 - u\bigr) .
> \end{aligned}
> $$
>
> **Step 4.** All 10 scalar products are thus expressed in terms of the four masses and $s$, $t$, $u$. (End of the user's solution of part (a).)
>
> **What the derivation shows**
> - Each Mandelstam variable gives two of the products: one from its definition and one from its second form, which uses momentum conservation (the second forms of [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-1|Def. §C8a.14.1]]).
> - The sum rule, part (b) of the problem, is [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], 1; the user's derivation (expand the three squares, then $p_2 - p_3 - p_4 = -p_1$) is the one given there, and Yu's (8.301)–(8.302).

^der-c8a-14-8

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-1|Def. §C8a.14.1]]

> [!remark] Remark: The variable u for identical particles
> $u$ is the third variable of the set; physically it is the momentum transfer with $k$ and $k'$ exchanged in the final state ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-1|Def. §C8a.14.1]], 3). If the particles that come in with $p$ and $p'$ are truly different, it is natural to regard the outgoing momentum $k$ as belonging to the particle that came in with $p$, and $t$ is the momentum transfer. If the two are the same kind of particle, there is no way of telling which is which, and $u$ is as natural as $t$: a shifted momentum transfer, in which the two particles of the final state have exchanged their identity. For two identical fermions both assignments occur as diagrams, the $t$-channel and the $u$-channel one, with a relative minus sign: [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-1|Theorem §C8b.11.1]] (Yukawa theory) and [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-1|Theorem §C8b.12.1]] (two electrons); for the distinguishable $e^-$ and $\mu^-$ there is one diagram only ([[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-1|Theorem §C8a.12.1]]).
>
> *Source: PHY 513 Lecture 21, recording, part C · the diagrams: PHY 513, Problem Set 11, Problems 1(b) and 2(a) (the user's solutions)*

^rem-c8a-14-2

> [!definition] Definition §C8a.14.3: k-Particle Mandelstam Variables
> For a scattering process with $n$ external particles, label the momenta of the incoming particles as $-p_1$ and $-p_2$, so that all momenta are on an equal footing and momentum conservation reads $\sum_{i=1}^np_i = 0$. The **$k$-particle Mandelstam variables** are
>
> $$
> s_{i_1\dots i_k} \equiv \bigl(p_{i_1} + \dots + p_{i_k}\bigr)^2 ,
> $$
>
> where the $i_1, \dots, i_k$ are distinct.
>
> *Equivalently,* for $n = 4$ in this labelling $s_{12} = s$, $s_{13} = t$, $s_{14} = u$ of [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]]: with $p_1 \to -p_1$, $p_2 \to -p_2$ they are $(p_1 + p_2)^2$, $(p_3 - p_1)^2$, $(p_4 - p_1)^2$. Counting an incoming momentum $p$ as an outgoing momentum $-p$ is the bookkeeping of crossing ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-1|Principle §C8a.14.1]]).
>
> *Model:* any (kinematics); *applies:* any process with momentum conservation; all momenta counted as outgoing.
>
> *Source: PHY 513, Problem Set 11, Problem 3, statement, eq. (5) and the paragraph before it*

^def-c8a-14-3

> [!theorem] Theorem §C8a.14.9: Five Massless Momenta: Every Invariant Is Zero or a Two-Particle Invariant
> Let five massless particles have momenta $p_1, \dots, p_5$, all counted as outgoing: $\sum_{i=1}^5p_i = 0$, $p_i^2 = 0$ (for example two gluons scattering into three gluons). Let $G_{ij} \equiv p_i\cdot p_j$, a symmetric $5\times5$ matrix with $G_{ii} = 0$. Then:
> 1. for a subset $I \subseteq \{1, \dots, 5\}$, $s_I = \bigl(\sum_{i \in I}p_i\bigr)^2 = \sum_{i, j \in I}G_{ij}$, the sum of the entries of the block $I \times I$;
> 2. every row of $G$ sums to zero, $\sum_{j=1}^5G_{ij} = 0$;
> 3. complementary subsets have equal invariants: $s_I = s_J$ for $J$ the complement of $I$;
> 4. hence $s_{12345} = 0$; $s_{ijkl} = s_m = p_m^2 = 0$, with $m$ the remaining index; and $s_{ijk} = s_{lm}$, with $\{l, m\}$ the remaining pair. Every invariant is $0$ or one of the two-particle invariants
>
> $$
> s_{ij} = (p_i + p_j)^2 = 2\,p_i\cdot p_j , \qquad 1 \le i < j \le 5 ,
> $$
>
> of which there are $\binom52 = 10$.
>
> *Model:* any (kinematics); *applies:* five on-shell massless momenta with $\sum p_i = 0$; parts 1–3 for any number of momenta and any masses, with $G_{ii} = m_i^2$.
>
> *Source: PHY 513, Problem Set 11, Problem 3(c) (statement: "What are the Mandelstam invariants in this case? How many are there?"; the user's solution, opening and paragraph "Reduction to two-particle invariants") · checked numerically for all subsets (`qft-C/tools/hw11/verify.py`)*

^thm-c8a-14-9

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 3(c), up to the paragraph "Reduction to two-particle invariants".
>
> **Step 1** (the matrix of products). With all momenta counted as outgoing, $\sum_{i=1}^5p_i = 0$, and all particles are massless, $p_i^2 = 0$. Let $G_{ij} \equiv p_i\cdot p_j$, a symmetric $5\times5$ matrix with $G_{ii} = 0$. For a subset $I \subseteq \{1, \dots, 5\}$,
>
> $$
> s_I = \Bigl(\sum_{i \in I}p_i\Bigr)^2 = \sum_{i, j \in I}G_{ij} ,
> $$
>
> the sum of the entries of the block $I \times I$.
>
> **Step 2** (row sums). By momentum conservation every row of $G$ sums to zero,
>
> $$
> \sum_{j=1}^5G_{ij} = p_i\cdot\sum_{j=1}^5p_j = 0 .
> $$
>
> **Step 3** (complements). Let $J$ be the complement of $I$. Splitting the sum of all entries of $G$ into blocks,
>
> $$
> 0 = \sum_{i, j=1}^5G_{ij} = s_I + s_J + 2\sum_{i \in J}\sum_{j \in I}G_{ij} .
> $$
>
> For $i \in J$ the row sum gives $\sum_{j \in I}G_{ij} = -\sum_{j \in J}G_{ij}$, so the last term is $-2s_J$, and
>
> $$
> s_I = s_J .
> $$
>
> **Step 4** (the list). Hence $s_{12345} = 0$; $s_{ijkl} = s_m = p_m^2 = 0$, with $m$ the remaining index; and $s_{ijk} = s_{lm}$, with $\{l, m\}$ the remaining pair. Every invariant is therefore $0$ or one of the two-particle invariants $s_{ij} = (p_i + p_j)^2 = 2\,p_i\cdot p_j$, $1 \le i < j \le 5$, of which there are $\binom52 = 10$.
>
> **What the derivation shows**
> - $s_I = s_J$ is momentum conservation: $\sum_{i \in I}p_i = -\sum_{i \in J}p_i$, and the two squares are equal. For four particles it is the equality of the two forms of each of $s$, $t$, $u$ ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-1|Def. §C8a.14.1]], 4).

^der-c8a-14-9

*Uses:* [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-3|Def. §C8a.14.3]]

> [!theorem] Theorem §C8a.14.10: The Relation among the Two-Particle Invariants of Five Massless Particles
> In the setting of [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-9|Theorem §C8a.14.9]], with $s_{ji} \equiv s_{ij}$:
> 1. the row sums of $G$ are the five relations
>
> $$
> R_i:\quad \sum_{j \ne i}s_{ij} = 0 , \qquad i = 1, \dots, 5 ;
> $$
>
> 2. each $s_{ij}$ appears in exactly $R_i$ and $R_j$, so adding the five relations gives the analogue of $s + t + u = \sum_im_i^2$,
>
> $$
> \sum_{1 \le i < j \le 5}s_{ij} = 0 .
> $$
>
> *Equivalently,* for four massless particles the same steps give $R_1$: $s_{12} + s_{13} + s_{14} = 0$, which is $s + t + u = 0$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], 1; [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-7|Theorem §C8a.14.7]], 2, at $m = 0$).
>
> *Model:* any (kinematics); *applies:* five on-shell massless momenta with $\sum p_i = 0$.
>
> *Source: PHY 513, Problem Set 11, Problem 3(c) (statement: "Write down a relation similar to (4) that they have to satisfy"; the user's solution, paragraph "Relations") · checked numerically (`qft-C/tools/hw11/verify.py`)*

^thm-c8a-14-10

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 3(c), paragraph "Relations".
>
> **Step 1.** With $G_{ii} = 0$ and $s_{ij} = 2G_{ij}$, the row sums of $G$ ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-9|Theorem §C8a.14.9]], 2) become the five relations $R_i$: $\sum_{j \ne i}s_{ij} = 0$, $i = 1, \dots, 5$, with $s_{ji} \equiv s_{ij}$.
>
> **Step 2.** Each $s_{ij}$ appears in exactly $R_i$ and $R_j$, so adding the five relations gives $2\sum_{1 \le i < j \le 5}s_{ij} = 0$, the relation of part 2.

^der-c8a-14-10

*Uses:* [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-9|Theorem §C8a.14.9]]

> [!theorem] Theorem §C8a.14.11: Five of the Ten Two-Particle Invariants Are Independent
> ![[ph-qft-c8a-14-1.svg]]
> *ADDED figure: the ten invariants $s_{ij}$ as the edges and the diagonals of a pentagon whose corners are the five momenta. The five edges may be chosen freely; each diagonal is then fixed.*
>
> In the setting of [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-9|Theorem §C8a.14.9]], order the invariants as $\vec s = (s_{12}, s_{13}, s_{14}, s_{15}, s_{23}, s_{24}, s_{25}, s_{34}, s_{35}, s_{45})^{\mathsf T} \in \mathbb R^{10}$. Then:
> 1. the five relations $R_1, \dots, R_5$ of [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-10|Theorem §C8a.14.10]] together read $M\vec s = 0$, where row $i$ of $M$ has a $1$ in each column whose pair contains $i$,
>
> $$
> M = \begin{pmatrix}
> 1&1&1&1&0&0&0&0&0&0\\
> 1&0&0&0&1&1&1&0&0&0\\
> 0&1&0&0&1&0&0&1&1&0\\
> 0&0&1&0&0&1&0&1&0&1\\
> 0&0&0&1&0&0&1&0&1&1
> \end{pmatrix} ,
> $$
>
> and the invariants of any physical configuration lie in $\ker M$;
> 2. with $s_{12}$, $s_{23}$, $s_{34}$, $s_{45}$, $s_{15}$ taken as free, the others are
>
> $$
> \begin{aligned}
> s_{13} &= s_{45} - s_{12} - s_{23} , & s_{14} &= s_{23} - s_{45} - s_{15} , & s_{24} &= s_{15} - s_{23} - s_{34} ,\\
> s_{25} &= s_{34} - s_{15} - s_{12} , & s_{35} &= s_{12} - s_{34} - s_{45} ,
> \end{aligned}
> $$
>
> so $\dim\ker M = 5$;
> 3. there are no further constraints: the physical invariants fill a five-dimensional region of $\ker M$, restricted only by inequalities such as $s_{12} = E_{\rm cm}^2 > 0$.
>
> **5 of the ten $s_{ij}$ are independent, for example $s_{12}$, $s_{23}$, $s_{34}$, $s_{45}$, $s_{15}$.**
>
> *Model:* any (kinematics); *applies:* five on-shell massless momenta in four space-time dimensions with $\sum p_i = 0$.
>
> *Source: PHY 513, Problem Set 11, Problem 3(c) (the user's solution, paragraphs "Number of independent invariants", "Basis of the kernel", "No further constraints") · the rank of $M$, the kernel vectors, the five solved invariants on random configurations, and the rank 5 of the Jacobian of the $s_{ij}$ with respect to the parameters of a configuration checked numerically (`qft-C/tools/hw11/verify.py`)*

^thm-c8a-14-11

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 3(c), paragraphs "Number of independent invariants", "Basis of the kernel" and "No further constraints".
>
> **Step 1** (the linear system). Order the invariants as $\vec s = (s_{12}, s_{13}, s_{14}, s_{15}, s_{23}, s_{24}, s_{25}, s_{34}, s_{35}, s_{45})^{\mathsf T} \in \mathbb R^{10}$. The five relations $R_1, \dots, R_5$ together read $M\vec s = 0$, where row $i$ of $M$ has a $1$ in each column whose pair contains $i$: the matrix of the statement. The invariants of any physical configuration therefore lie in $\ker M$.
>
> **Step 2** (free invariants). Take $s_{12}$, $s_{23}$, $s_{34}$, $s_{45}$, $s_{15}$ as free. The relations become
>
> $$
> \begin{aligned}
> R_1:&\quad s_{13} + s_{14} = -s_{12} - s_{15} , & R_4:&\quad s_{14} + s_{24} = -s_{34} - s_{45} ,\\
> R_2:&\quad s_{24} + s_{25} = -s_{12} - s_{23} , & R_5:&\quad s_{25} + s_{35} = -s_{15} - s_{45} ,\\
> R_3:&\quad s_{13} + s_{35} = -s_{23} - s_{34} .
> \end{aligned}
> $$
>
> **Step 3** (solve). The combination $R_1 - R_4 + R_2 - R_5 + R_3$ leaves only $2s_{13}$ on the left, so
>
> $$
> 2s_{13} = (-s_{12} - s_{15}) - (-s_{34} - s_{45}) + (-s_{12} - s_{23}) - (-s_{15} - s_{45}) + (-s_{23} - s_{34}) = 2\bigl(s_{45} - s_{12} - s_{23}\bigr) ,
> $$
>
> and then $R_1$, $R_4$, $R_2$, $R_3$ give the rest: the five expressions of part 2.
>
> **Step 4** (the kernel). Every solution is thus fixed uniquely by the five free invariants, so $\dim\ker M = 5$. Setting one of them to $1$ and the others to $0$ gives a basis of $\ker M$, in the ordering of $\vec s$:
>
> $$
> \begin{aligned}
> s_{12}&:\ (1, -1, 0, 0, 0, 0, -1, 0, 1, 0) , & s_{23}&:\ (0, -1, 1, 0, 1, -1, 0, 0, 0, 0) ,\\
> s_{34}&:\ (0, 0, 0, 0, 0, -1, 1, 1, -1, 0) , & s_{45}&:\ (0, 1, -1, 0, 0, 0, 0, 0, -1, 1) ,\\
> s_{15}&:\ (0, 0, -1, 1, 0, 1, -1, 0, 0, 0) . &&
> \end{aligned}
> $$
>
> **Step 5** (no further constraints). Five massless momenta have $5 \times 3 = 15$ components; momentum conservation removes $4$ and Lorentz transformations, which leave every $s_{ij}$ unchanged, remove $6$, leaving $15 - 4 - 6 = 5$ parameters. The physical invariants therefore fill a five-dimensional region of $\ker M$, restricted only by inequalities such as $s_{12} = E_{\rm cm}^2 > 0$, and 5 of the ten $s_{ij}$ are independent, e.g. $s_{12}$, $s_{23}$, $s_{34}$, $s_{45}$, $s_{15}$. (End of the user's solution of Problem 3.)
>
> **What the derivation shows**
> - The free set is the five neighbouring pairs of the cyclic order $1, 2, 3, 4, 5$, and each solved invariant is a three-particle invariant written out: by [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-9|Theorem §C8a.14.9]], 4, $s_{45} = s_{123} = s_{12} + s_{13} + s_{23}$, which is the first expression of part 2; the others follow by $i \to i + 1$ (the figure).
> - The counting $15 - 4 - 6$ is for four space-time dimensions. For four massless particles it gives $4\times3 - 4 - 6 = 2$, the two independent variables among $s$, $t$, $u$.
> - $\dim\ker M = 10 - \operatorname{rank}M$ with $\operatorname{rank}M = 5$ is the rank–nullity relation ([[Fundamental theorem of linear maps|LADR 3.21]]).

^der-c8a-14-11

*Uses:* [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-9|Theorem §C8a.14.9]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-10|Theorem §C8a.14.10]]

> [!remark]- Connections
> - The Mandelstam variables were introduced as notation in the first problem set, with the sum rule and the elastic form of $t$ — [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]]; this lecture gives them their use.
> - The channels of the scalar theories, with all three propagators in one amplitude — [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]].
> - The sign of $q^2$ separated the annihilation photon from the exchanged photon before the names $s$ and $t$ were used — [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^pr-c8a-6-4|Principle §C8a.6.4]].
> - The two terms of the complex field, one annihilating particles and one creating antiparticles, are what the proof idea exchanges; the Dirac field has the same two terms with the wave functions $u$ and $v$ — [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]].
> - The two completeness relations behind the fermion sign — [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-8|Theorem §C5a.12.8]].
> - Poles of propagators and the $i\varepsilon$ that defines them on the real axis — [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]].
> - Back: the substitution that this section explains — [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-3|Theorem §C8a.12.3]]; the forward peak that the pole at $t = 0$ produces — [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-6|Theorem §C8a.13.6]]. Forward: Compton scattering (Lecture 22; PS §5.5; planned).
> - The six scalar products of a $2 \to 2$ process in terms of $s$, $t$, $u$ were first written for spinless amplitudes, together with the vanishing $\varepsilon$-contraction — [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]]; here as Problem Set 11, Problem 3(a) — [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-8|Theorem §C8a.14.8]].
> - Two identical fermions: both the $t$- and the $u$-channel diagram occur, with a relative minus sign; their helicity amplitudes with a scalar and with a photon exchanged — [[§C8b.11 Helicity Amplitudes in Yukawa Theory|§C8b.11]], [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering|§C8b.12]].
