---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6c
section: C6c.5
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6c.4 First Order꞉ Enumerate, then Filter]] · ↑ [[· C6c Feynman Rules for Amplitudes]] · [[§C6c.6 Feynman Rules for Amplitudes]] →

<!-- SOURCES -->

<!-- OPENING -->

<!-- SETUP -->

## The terms of second order

<!-- NEW thm-c6c-5-1 -->

<!-- NEW thm-c6c-5-2 -->

## Amputation

> [!definition] Definition §C6c.5.1: Amputation of an External Leg
> In a diagram with external particles, start at the tip of an external leg (the end at the particle) and go into the diagram to the **last point at which the diagram can be cut by removing one propagator** such that the cut separates the leg, with everything that hangs on it, from the rest. **Amputating** the leg removes everything between the tip and that cut: the particle is then joined, by a line without propagator, directly to the vertex beyond the cut. A diagram is **amputated** if no leg has anything to remove, i.e. no propagator separates a part holding a single particle from the rest.
>
> What is removed is "interaction corrects external state. Not an interaction between different states" (slide 26). A tree whose vertices all have $r_v \ge 3$ legs is amputated: removing an internal line leaves on each side a vertex with at least two further branches, each ending at a particle, so no line separates a single particle.
>
> *Model:* any (combinatorics); *applies:* diagrams of $S$-matrix elements and of correlation functions alike (for a correlation function the removed part includes the external propagator: [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]]); the removed corrections are not zero: beyond lowest order they return as $\sqrt Z$ per external line and the physical mass ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]; second semester).
>
> *Source: PHY 513 Lecture 16, slide 26 ("Some diagrams encode 'interaction corrects external state' … Amputation: exclude such diagrams. General rule for where to amputate external leg: go from tip to last point where diagram can be cut by removing one propagator. Corrections to external wave functions are interesting and studied in 2nd semester") · the user's PHY 513 notes, Lecture 16 update, §16.7, Definition "Connected and amputated" and paragraph "Why amputated" · PHY 513 Lecture 16, transcript ("What amputation means is that in these kind of diagrams … nothing happens between out here and into the vertex") · PS §4.6, p. 113 ("Starting from the tip of each external leg, find the last point at which the diagram can be cut by removing a single propagator, such that this operation separates the leg from the rest of the diagram. Cut there.") and the figure on p. 114*

^def-c6c-5-1

![[ph-qft-c6b-3-1.svg]]
*Amputation ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^def-c6c-5-1|Def. §C6c.5.1]]). (a) Slide 26: a loop at $z_1$ on the leg of $A$; removing the propagator $z_1z$ separates the leg with its loop. (b) Two loops on the leg: two propagators separate it; the cut is made at the last one, next to the vertex $z$, and both loops go. (c) What remains in both cases is the vertex $-i\lambda$ with $A$ attached directly. Added figure.*

> [!theorem] Theorem §C6c.5.3: External-Leg Corrections Are Removed by Amputation; the Rest Is the T-Matrix Element
> In the expansion of [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]], keep the terms with one piece holding all particles (the others are not scattering: [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]]). Then
> 1. a part hanging on one external leg, separated from the rest by one propagator, is a correction of the external state; its propagator carries the on-shell momentum of the particle, $\frac{i}{k^2 - m^2}\big|_{k^2 = m^2}$, and it is removed by amputation ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^def-c6c-5-1|Def. §C6c.5.1]]);
> 2. the rest, the fully connected amputated diagrams, is $\langle f|i\hat T|i\rangle = (2\pi)^4\delta^4(\sum k - \sum p)\,i\mathcal M$ at the order considered ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]]).
>
> "Connected" and "amputated" are therefore consequences of the expansion, not assumptions.
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* any polynomial interaction, every order, with the prescription of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]] (and its scope); the external-state corrections of part 1 return beyond lowest order as $\sqrt Z$ and the physical mass ([[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|§C2b.1, Caution: With interactions, the one-particle matrix element carries √Z]]; [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]; second semester).
>
> *Source: PHY 513 Lecture 16, slides 25–26 (slide 25: "self-energy: wave function of external state corrected from free to interacting") · PS §4.6, eqs. (4.101)–(4.102) ("Only *fully connected* diagrams, in which all external lines are connected to each other, contribute to the $T$-matrix", p. 111) · the user's PHY 513 notes, Lecture 16 update, §16.7 ("Why connected", "Why amputated") · proof written here*

^thm-c6c-5-3

> [!derivation]- Derivation
> **Step 1** (part 1). Let a propagator $\ell$ separate a part $X$ holding a single particle, of momentum $k$, from the rest. Step 2 of [[§C6c.3 Wick's Theorem between Particle States#^der-c6c-3-3|Derivation §C6c.3.3]] applied to $X$, with $\ell$ as its second external line, fixes the momentum of $\ell$ to $k$, so $\ell$ contributes
>
> $$
> \frac{i}{k^2 - m^2 + i\varepsilon}\Big|_{k^2 = m^2} = \frac{i}{i\varepsilon} \xrightarrow{\varepsilon\to0^+} \infty
> $$
>
> (PS (4.102): "$\frac{1}{p'^2 - m^2}\big|_{p' = p_B} = \frac{1}{0}$"). $X$ turns the free particle into the dressed one ("self-energy: wave function of external state corrected from free to interacting", slide 25), not a scattering between different particles; the amputation of [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^def-c6c-5-1|Def. §C6c.5.1]] removes it.
>
> **Step 2** (part 2). What is left has one piece, so one overall delta (Step 2 of [[§C6c.3 Wick's Theorem between Particle States#^der-c6c-3-3|Derivation §C6c.3.3]]), and no external-state part: by [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]] its sum is $(2\pi)^4\delta^4(\sum k - \sum p)\,i\mathcal M$.
>
> **What the derivation shows.**
> - "Connected" and "amputated" are not extra assumptions: disconnected terms are the $\mathbb 1$, bubbles or smaller processes (each piece its own delta), and external-leg parts are state corrections with an on-shell propagator.

^der-c6c-5-3

*Uses:* [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^def-c6c-5-1|Def. §C6c.5.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-3|P6, step 3]]

## Second-order examples

> [!example] Example §C6c.5.1: φφ → φφ at Order λ²
> ![[ph-qft-c6b-3-3.svg]]
>
> In $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]) the connected, amputated diagrams of $p_A + p_B \to p_1 + p_2$ at order $\lambda^2$ are exactly the three loops (a)–(c), each with $S = 2$, and with $P_s = p_A + p_B$, $P_t = p_A - p_1$, $P_u = p_A - p_2$ the momentum through the loop,
>
> $$
> i\mathcal M^{(2)} = \frac{(-i\lambda)^2}{2}\sum_{P = P_s, P_t, P_u}\int\frac{d^4q}{(2\pi)^4}\,\frac{i}{q^2 - m^2 + i\varepsilon}\,\frac{i}{(P - q)^2 - m^2 + i\varepsilon} ;
> $$
>
> (d)–(f) are not diagrams of $i\mathcal M$. "A total of three diagrams at that order. It's not a humongous number."
>
> **Step 1** (legs and lines). Two quartic vertices, four particles: $\sum r_v = 8 = 4 + 2I$, $I = 2$; connected, $L = I - V + 1 = 1$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 1–2). With $e_v$ particles at vertex $v$, the free legs number $(4 - e_1) + (4 - e_2) = 2I = 4$, so $e_1 + e_2 = 4$:
> - $(e_1, e_2) = (4, 0)$: $v_2$ closes on itself, the figure-eight beside the vertex, (d): not connected ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 3), a vacuum bubble ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], 1);
> - $(3, 1)$: the free leg of $v_1$ goes to $v_2$, the two other free legs of $v_2$ close a loop: a loop on the leg of the single particle at $v_2$, (f), four such diagrams; removing the line $v_2v_1$ separates that particle with its loop: not amputated ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^def-c6c-5-1|Def. §C6c.5.1]]);
> - $(2, 2)$ with a loop at each vertex: two pieces; one incoming and one outgoing particle at each vertex gives (e), two forward pieces, the $\mathbb 1$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], 2); $p_A$, $p_B$ at one vertex gives $\delta^4(p_A + p_B)$, zero on shell ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], 1);
> - $(2, 2)$ with both lines between $v_1$ and $v_2$: connected and amputated; a diagram is the partner of $p_A$ at its vertex, $p_B$ (a), $p_1$ (b), $p_2$ (c).
>
> **Step 2** ($S$). The particles are fixed; the only symmetry is the exchange of the two parallel lines: $S = 2$. Count: $|G| = 2!\,(4!)^2 = 1152$ relabellings, $576$ pairings per channel (the fish of [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-5|Example §C6a.9.5]] (c), with particles for external points), $1152/576 = 2$.
>
> **Step 3** (momenta). By [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]], in (a) $P_s$ enters the vertex of $p_A$, $p_B$ and leaves as $q$ and $P_s - q$ on the two lines; the vertex delta fixes the second line, the other vertex gives the overall $\delta^4(p_A + p_B - p_1 - p_2)$, and one integral $\int\frac{d^4q}{(2\pi)^4}$ is left ($L = 1$). In (b) the vertex of $p_A$ and $p_1$ passes $P_t = p_A - p_1$ into the loop, in (c) $P_u = p_A - p_2$. Each diagram: $\frac12(-i\lambda)^2\int\frac{d^4q}{(2\pi)^4}\frac{i}{q^2 - m^2 + i\varepsilon}\frac{i}{(P - q)^2 - m^2 + i\varepsilon}$; the sum is the statement.
>
> **Step 4** (what the integral does at large $q$). The integrand falls like $\frac{1}{q^4}$, and $\int\frac{d^4q}{q^4}$ diverges logarithmically: making sense of it is renormalization (second semester). The dependence on $P_s^2 = s$, $P_t^2 = t$, $P_u^2 = u$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]]) is the energy dependence the first order lacks.
>
> *Source: PHY 513 Lecture 16, slide 25 (the $s$-channel loop as the connected example; "2nd and 3rd diagram are not connected"), slide 26, and transcript ("total of three diagrams at that order. It's not a humongous number") · the user's PHY 513 notes, Lecture 16 update, §16.8 "Example: $2 \to 2$ at order $\lambda^2$" (eq. (oneloop), "The symmetry factor $2$ (filled in)", "Looking ahead") and Figure "connamp" · PS §4.6, eq. (4.101), p. 112*

^ex-c6c-5-1

<!-- NEW ex-c6c-5-2 -->

## Symmetry factors with the particles held fixed

<!-- NEW thm-c6c-5-4 -->

> [!theorem] Theorem §C6c.5.5: Vertices Saturated by External Lines Give S = 1
> If every vertex $v$ of a diagram has valence $r_v \ge 2$ and at least $r_v - 1$ of its legs joined to external points, then $S = 1$; equivalently $N_D = |G|$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]). In particular every tree diagram with one internal line has $S = 1$.
>
> *Model:* any (combinatorics); *applies:* any diagram with the stated valences, any vertex types.
>
> *Source: PHY 513, Problem Set 8, Problem 2(c) (the user's argument: "each vertex has exactly one internal leg … The external particles are never relabeled, so an element of $\mathrm{Stab}(P)$ fixes every leg joined to an external particle. The internal leg is then the only remaining leg at its vertex, so it is fixed as well") · PHY 513 Lecture 14, slide 17 ("Reordering of legs = topologically distinct diagram ⇒ S = 1")*

^thm-c6c-5-5

> [!derivation]- Derivation
> **Step 1** (vertices fixed). Let $g \in \operatorname{Stab}(P)$. Each leg joined to an external point is fixed, and so is its vertex ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 3). Every vertex has $r_v - 1 \ge 1$ such legs, so $g$ permutes no vertices.
>
> **Step 2** (legs fixed). $g$ maps the legs of $v$ to legs of $v$; at least $r_v - 1$ are fixed, so the remaining one (if any) is mapped to itself. Hence $g$ fixes every half-edge: $g = e$, $S = |\operatorname{Stab}(P)| = 1$.
>
> **Step 3** (count). $N_D = |G|/S = |G|$. Example (one cubic and one quartic vertex, five external particles, two on the cubic and three on the quartic vertex): the two at the cubic vertex attach in $3\cdot2$ ways, the three at the quartic vertex in $4\cdot3\cdot2$, the remaining two legs pair in one way: $N_D = 6\cdot24 = 144 = 3!\,4! = |G|$.

^der-c6c-5-5

*Uses:* [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]

*Procedure:* [[P5 Symmetry Factor of a Diagram#^p5-5|P5, step 5]]

<!-- NEW thm-c6c-5-6 (proof = former Step 4 of der-c6b-3-2, below) -->

<!-- MOVED-STEP4-32 > **Step 4** ($S = 1$ for a tree). Let $D$ be a fully connected diagram without loops (a tree) and $g \in \operatorname{Stab}(P)$. Every leaf of the tree is an external particle (a vertex with a single line would have valence one). Removing an internal line $e$ splits the particles into two nonempty sets $E_1(e) \sqcup E_2(e)$, and different lines give different splits (two lines of a tree are separated by a vertex with a third branch, which holds a particle). $g$ fixes every particle ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 3), so it maps each line to the line with the same split, i.e. to itself, with its ends on their own sides: every line and every vertex is fixed. A tree has no two lines between the same vertices, so the legs of a fixed vertex are fixed too: $g = e$, $S = |\operatorname{Stab}(P)| = 1$ (for one internal line this is [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-5|Theorem §C6c.5.5]]). -->

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]] — the relabelling group and orbit–stabilizer behind $\frac1S$ and behind $S = 1$ for trees.

> [!remark]- Connections
> - Amputated leg corrections are not zero: they return as $\sqrt Z$ per external line and the physical mass, the LSZ formula — [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]].
