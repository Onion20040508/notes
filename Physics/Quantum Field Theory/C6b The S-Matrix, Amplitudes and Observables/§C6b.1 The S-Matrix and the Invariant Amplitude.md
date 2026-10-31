---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.1
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6a.11 The iε Limit and Vacuum Bubbles]] · ↑ [[· C6b The S-Matrix, Amplitudes and Observables]] · [[§C6b.2 Transition Probabilities in a Box]] →

*Sources: the user's PHY 513 notes, Ch. 15 §15.1 (Definition "The $S$-matrix", paragraphs "'Matrix' is a historical term", "The fundamental observable?", "Relation to Chapter 13 (filled in)", Definition "The invariant amplitude $\mathcal M$", Derivation "Three properties of $\mathcal M$ (filled in)", Principle "Dynamics versus kinematics") · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), Part A, slides 4–7, and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.5, pp. 102–104, eqs. (4.70)–(4.73) · Yu Zhao-Huan, 量子场论讲义, §6.2, eqs. (6.122)–(6.127); §6.5, eqs. (6.272)–(6.275).*

Lectures 13–14 built the Feynman rules for correlation functions $\langle\Omega|T\{\hat\phi_H(x_1)\cdots\hat\phi_H(x_n)\}|\Omega\rangle$ ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-5|Theorem §C6a.11.5]]). "It's completely the right idea. It's just that … that's not what you really want": nobody measures a correlation function. Lecture 15 asks what we do want to compute, and the answer of particle physics is the cross section and the decay rate. This section sets up the object they are made from. Particles that are widely separated early evolve into particles that are widely separated late; the linear map between the two is the $S$-matrix ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]]). Removing the part in which nothing happens and the overall delta function of four-momentum conservation leaves one function, the invariant amplitude $\mathcal M$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]), the only place where the dynamics enters. The next sections turn $\mathcal M$ into cross sections, first by Yu's box route ([[§C6b.2 Transition Probabilities in a Box|§C6b.2]], [[§C6b.3 The Cross Section|§C6b.3]]), then by the course's wave packets ([[§C6b.4 Wave Packets and the Cross Section|§C6b.4]], [[§C6b.5 Evaluating the Cross Section|§C6b.5]]), with Lorentz invariance and two-body phase space in [[§C6b.6 Lorentz Invariance and Two-Body Phase Space|§C6b.6]], and decay rates ([[§C6b.7 Decay Rates and Widths|§C6b.7]]), and [[§C6b.8 Amplitudes from Correlation Functions|§C6b.8]] states how $\mathcal M$ is read off from the correlation functions of Lecture 14. Yu treats the $S$-matrix in §6.2, eqs. (6.122)–(6.127), defining it as the interaction-picture evolution operator $U(+\infty, -\infty)$ between asymptotic states, and the split $S = \mathbb I + iT$ with the invariant amplitude in §6.5, eqs. (6.272)–(6.275), in the setting of the Dyson series of the $S$-operator.

**The setup of this chapter: what is prepared, what is measured, which theory.** Prepared: a few particles with nearly definite momenta, far apart in the far past (two for a scattering, one for a decay). Measured: the particles that emerge in the far future, counted in ranges of momentum; the observables are counting rates, the cross section and the decay rate. The theory: a Hamiltonian $\hat H = \hat H_0 + \hat H_{\rm int}$. Two settings run through C6b, and each formula says which it uses:
- *the interacting theory* ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]], the wave packets of [[§C6b.4 Wave Packets and the Cross Section|§C6b.4]]): the in and out states are states of the full $\hat H$ that look like free, widely separated particles at $\mp\infty$; the vacuum is $|\Omega\rangle$; the interaction is never switched off;
- *the free-state setting* (Yu's box, [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]]; the decay chain, [[§C6b.7 Decay Rates and Widths#^mod-c6b-7-1|Model §C6b.7.1]]; the amplitudes of [[§C6b.8 Amplitudes from Correlation Functions|§C6b.8]]): the in and out states are free Fock states $\sqrt{2E}\,\hat a^\dagger\cdots|0\rangle$ of $\hat H_0$ over the free vacuum $|0\rangle$, and $\hat S = U(+\infty, -\infty)$ in the interaction picture ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]]).

The two agree exactly when $\hat H_{\rm int}(t) \to 0$ for $|t| \to \infty$ (a source or interaction switched on and off, as in [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route|§C6b.9]]); for a permanent interaction they agree at lowest order, and beyond it the external particles carry $\sqrt Z$ and the physical mass ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^cau-c6b-1-1|Caution: "Free" means widely separated]], below; [[§C6b.8 Amplitudes from Correlation Functions#^cau-c6b-8-2|§C6b.8, Caution: The rule is stated at lowest order]]).

*Conventions* ([[Larsen PHY 513]]): $\hbar = c = 1$; states normalized relativistically, $\langle\mathbf p|\mathbf q\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]); the $S$-matrix and the $T$-matrix are operators and carry hats, $\hat S$, $\hat T$ (the slides write $\mathcal S$, $\mathcal T$: Caution: Names for the S-matrix, the T-matrix and the amplitude, below); $\mathcal M$ is a number.

## The S-matrix

> [!definition] Definition §C6b.1.1: The S-Matrix
> A general scattering process takes free initial particles, momenta $\mathbf p_A, \mathbf p_B, \dots$, to free final particles, momenta $\mathbf p_1, \mathbf p_2, \dots$; "free" means widely separated. The initial time is $-T$, the final time $+T$, with $T$ large and positive: the time evolution is over $\Delta t = 2T$. The amplitude of the process is
>
> $$
> {}_{\rm out}\langle\mathbf p_1\mathbf p_2\cdots|\mathbf p_A\mathbf p_B\cdots\rangle_{\rm in} = \lim_{T\to\infty}\langle\mathbf p_1\mathbf p_2\cdots|e^{-i\hat H\,2T}|\mathbf p_A\mathbf p_B\cdots\rangle \equiv \langle\mathbf p_1\mathbf p_2\cdots|\hat S|\mathbf p_A\mathbf p_B\cdots\rangle ,
> $$
>
> with $\hat H$ the full Hamiltonian. The **$S$-matrix** $\hat S$ is the map between free particles early and late, a linear operator.
>
> *Source: PHY 513 Lecture 15, slide 4 ("A general scattering process: Free initial particles to free final particles … 'Initial' time $= -T$, 'final' time $+T$. $T$ large and positive. Time evolution over $\Delta t = 2T$ … The $\mathcal S$-matrix = map between free particles early and late. Comment: 'matrix' is a historical term = linear operator"), and transcript ("what I mean by free is not even necessarily that … the guys were created by a dagger … it's more just that they started out being widely separated") · the user's PHY 513 notes, Ch. 15 §15.1, eq. (Smatrixdef) · PS §4.5, eqs. (4.70)–(4.71) · Yu §6.2, eqs. (6.123)–(6.124)*

^def-c6b-1-1

> [!caution] Caution: "Free" means widely separated, not created by $\hat a^\dagger$ from the free vacuum
> The in and out states of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]] are states of the *interacting* theory that look like free, widely separated particles at $-T$ (in) or at $+T$ (out): "they don't know each other, and then they come together." They are eigenstates of $\hat H$, not of $\hat H_0$, and "in" and "out" states with the same labels are different states, "because there's been all this time evolution". PS say the same: $|\mathbf k\rangle$ in their wave packet (4.65) "is a one-particle state of momentum $\mathbf k$ in the interacting theory", and in the free theory one would have $|\mathbf k\rangle = \sqrt{2E_{\mathbf k}}\,\hat a^\dagger_{\mathbf k}|0\rangle$. Relating these states to the free states $\hat a^\dagger\cdots|0\rangle$ is the same problem that the $T \to \infty(1 - i\varepsilon)$ limit solved for the vacuum ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-1|Theorem §C6a.4.1]]); for particle states it is solved by the LSZ formula (Lecture 16 and QFT C10, planned).
>
> *Source: PHY 513 Lecture 15, transcript · PS §4.5, p. 102 (after eq. (4.65)), p. 108 (eqs. (4.87)–(4.88)) · the user's PHY 513 notes, Ch. 15 §15.1*

^cau-c6b-1-1


Which states stand in the middle expression of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]]: not the in and out states themselves, but states of the interacting theory given at one reference time, wave packets of the particles (PS (4.70)); $e^{-i\hat H\,2T}$ carries the one prepared at $-T$ to the one read at $+T$. They cannot be eigenstates of $\hat H$: if $\hat H|i\rangle = E_i|i\rangle$, then
$$
\langle f|e^{-i\hat H\,2T}|i\rangle = \sum_{k\ge0}\frac{(-2iT)^k}{k!}\langle f|\hat H^k|i\rangle = \sum_{k\ge0}\frac{(-2iTE_i)^k}{k!}\langle f|i\rangle = e^{-2iE_iT}\langle f|i\rangle ,
$$
a phase times the overlap: nothing would scatter.

> [!remark] Remark: "Matrix" is a historical term
> "It's back when people … consider[ed] matrices advanced math … Linear operators, they are matrices … We should call it a linear operator. That's really what we mean." Its matrix elements between basis states, $S_{fi} = \langle f|\hat S|i\rangle$, are what Yu arranges into a matrix with $f$ as the row index and $i$ as the column index (eq. (6.123)). The letter is Heisenberg's (*Streumatrix*, scattering matrix).
>
> *Source: PHY 513 Lecture 15, slide 4, and transcript · Yu §6.2, after eq. (6.123) · the user's PHY 513 notes, Ch. 15 §15.1*

^rem-c6b-1-1

> [!remark] Remark: The fundamental observable?
> "If I give you the input, you compute the output. It's sort of what the theory does": the $S$-matrix describes all possible scattering processes, and slide 5 calls it "the fundamental observable in quantum field theory". The lecture qualified this at once: it is "a justifiable answer because there are other justifiable answers". In condensed matter physics one rarely scatters particles; one has a material in some quantum state, "wiggles" it and asks how it responds. Those observables are **response functions**, Green's functions, not the $S$-matrix, so calling the $S$-matrix *the* observable is "a little bit prejudiced", though natural in high-energy physics. The correlation functions of Lecture 14 are the Green's functions of that other point of view ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-7|Theorem §C6a.4.7]]).
>
> *Source: PHY 513 Lecture 15, slide 5, and transcript · the user's PHY 513 notes, Ch. 15 §15.1 (paragraph "The fundamental observable?")*

^rem-c6b-1-2

The interaction picture of Lecture 13 gives a second expression for the same matrix elements, between free states, which is Yu's starting point.

> [!theorem] Theorem §C6b.1.1: S-Matrix Elements and the Interaction-Picture Evolution Operator
> *Setup:* $\hat H = \hat H_0 + \hat H_{\rm int}$, interaction picture; free states. *Applies:* the identity holds for any $\hat H$; it identifies the $\hat S$ of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]] with $U(+\infty, -\infty)$ between free states, up to the phase, only where free states may replace the in and out states: exactly if $\hat H_{\rm int}(t) \to 0$ for $|t| \to \infty$, for a permanent interaction at lowest order only ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^cau-c6b-1-1|Caution: "Free" means widely separated]]; [[§C6b.8 Amplitudes from Correlation Functions#^cau-c6b-8-2|§C6b.8, Caution: The rule is stated at lowest order]]).
>
> Let $|i\rangle$, $|f\rangle$ be eigenstates of $\hat H_0$ with energies $E_i$, $E_f$, and let $U(t, t')$ be the evolution operator of [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-2|Def. §C6a.3.2]]. Then
>
> $$
> \langle f|U(T, -T)|i\rangle = e^{i(E_f + E_i)T}\,\langle f|e^{-i\hat H\,2T}|i\rangle :
> $$
>
> between eigenstates of $\hat H_0$ the two matrix elements differ by a phase, which drops out of every probability.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.1 (paragraph "Relation to Chapter 13 (filled in)") · Yu §6.2, eqs. (6.122)–(6.125) (the $S$-operator $S = U(+\infty, -\infty)$)*

^thm-c6b-1-1

> [!derivation]- Derivation
> **Step 1** (the definition at $t = T$, $t' = -T$). [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-2|Def. §C6a.3.2]] with $t - t' = 2T$ gives
>
> $$
> U(T, -T) = e^{i\hat H_0T}\,e^{-i\hat H\,2T}\,e^{-i\hat H_0(-T)} = e^{i\hat H_0T}\,e^{-i\hat H\,2T}\,e^{i\hat H_0T} .
> $$
>
> **Step 2** (act on the eigenstates). With $\hat H_0|i\rangle = E_i|i\rangle$, $\hat H_0|f\rangle = E_f|f\rangle$ and the power series of the exponential,
>
> $$
> e^{i\hat H_0T}|i\rangle = \sum_{k\ge0}\frac{(iT)^k}{k!}\hat H_0^k|i\rangle = \sum_{k\ge0}\frac{(iT)^k}{k!}E_i^k|i\rangle = e^{iE_iT}|i\rangle , \qquad \langle f|e^{i\hat H_0T} = \bigl(e^{-i\hat H_0T}|f\rangle\bigr)^\dagger = \bigl(e^{-iE_fT}|f\rangle\bigr)^\dagger = e^{iE_fT}\langle f| ,
> $$
>
> the second because $\hat H_0$ is self-adjoint and $E_f$ is real.
>
> **Step 3** (combine). Sandwich Step 1 between $\langle f|$ and $|i\rangle$ and use Step 2 on the outer factors:
>
> $$
> \langle f|U(T, -T)|i\rangle = \bigl(\langle f|e^{i\hat H_0T}\bigr)\,e^{-i\hat H\,2T}\,\bigl(e^{i\hat H_0T}|i\rangle\bigr) = e^{iE_fT}\,e^{iE_iT}\,\langle f|e^{-i\hat H\,2T}|i\rangle = e^{i(E_f + E_i)T}\,\langle f|e^{-i\hat H\,2T}|i\rangle ,
> $$
>
> and $|e^{i(E_f + E_i)T}| = 1$, so $|\langle f|U(T, -T)|i\rangle|^2 = |\langle f|e^{-i\hat H\,2T}|i\rangle|^2$.
>
> ⚑ By-product: with $T \to \infty$ this suggests $\hat S = U(+\infty, -\infty) = T\{\exp[-i\int_{-\infty}^{\infty}dt\,\hat H_I(t)]\}$ ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]]), Yu's definition (eqs. (6.125)–(6.126)), which makes Dyson's series a series for $\hat S$. It is heuristic: the phase oscillates without a limit as $T \to \infty$, and the true in and out states are eigenstates of $\hat H$, not $\hat H_0$ (Caution: "Free" means widely separated, above). → Remark: Yu's route, below.
>
> **What the derivation shows.**
> - Between free states, the $S$-matrix of the course and Yu's $U(+\infty, -\infty)$ agree up to a phase.
> - What the phase hides, the difference between free and interacting asymptotic states, is the subject of LSZ (Lecture 16; QFT C10, planned).

^der-c6b-1-1

*Uses:* [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-2|Def. §C6a.3.2]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]]

## S = 1 + iT and the amplitude

> [!definition] Definition §C6b.1.2: The T-Matrix
> If in = out, nothing happened; if in ≠ out, the interactions did something. The two outcomes are separated by removing the "1":
>
> $$
> \hat S = \mathbb 1 + i\hat T .
> $$
>
> $\mathbb 1$ is the "nothing happened" part and the **$T$-matrix** $\hat T$ the "stuff happened" part.
>
> *Source: PHY 513 Lecture 15, slide 6 ("in = out ⇒ nothing happens ⇒ remove '1': $\mathcal S = 1 + i\mathcal T$; in ≠ out ⇒ interactions ⇒ $i\mathcal T$"), and transcript ("one is that sometimes maybe literally nothing happens … the $T$ is the stuff happened part") · the user's PHY 513 notes, Ch. 15 §15.1, eq. (SoneiT) · PS §4.5, eq. (4.72) · Yu §6.5, eqs. (6.272)–(6.274)*

^def-c6b-1-2


Why the $i$ in $\hat S = \mathbb 1 + i\hat T$: in the interaction picture ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]]; Yu (6.126), (6.272)) every term of the Dyson series after the first starts with a factor $-i$,
$$
\hat S = \sum_{n\ge0}\frac{(-i)^n}{n!}\int dt_1\cdots dt_n\,T\{\hat H_I(t_1)\cdots\hat H_I(t_n)\} = \mathbb 1 - i\int dt\,\hat H_I(t) + O(\hat H_I^2) \quad\Rightarrow\quad i\hat T = -i\int dt\,\hat H_I(t) + O(\hat H_I^2) ,
$$
so $\hat T = -\int dt\,\hat H_I(t) + O(\hat H_I^2)$ starts with no $i$: the $i$ is split off so that $\hat T$ is the interaction itself at first order. Yu: "$iT$ 包含所有 $n \ge 1$ 的项".

> [!theorem] Theorem §C6b.1.2: The S-Matrix Conserves Four-Momentum
> Assume the theory is translation invariant: the four-momentum $\hat P^\mu = (\hat H, \hat{\mathbf P})$ satisfies $[\hat H, \hat P^\mu] = 0$, and the in and out states are eigenstates of $\hat P^\mu$ with eigenvalues $p_i = \sum_{A, B, \dots}p$ and $p_f = \sum_{1, 2, \dots}p$. Then $[\hat S, \hat P^\mu] = 0$, and every matrix element of $i\hat T$ between such states, as a distribution in the momenta, is of the form
>
> $$
> \langle\mathbf p_1\mathbf p_2\cdots|i\hat T|\mathbf p_A\mathbf p_B\cdots\rangle = \delta^4(p_i - p_f)\;C(p_A, p_B, \dots; p_1, p_2, \dots) ,
> $$
>
> with a coefficient $C$ assumed smooth in the momenta on the surface $p_i = p_f$.
>
> *Source: PHY 513 Lecture 15, slide 6 ("$\mathcal T$ conserves energy-momentum so remove $\delta$-function"), and transcript ("this is a relativistic theory, and therefore, the final outcome has the same total four momentum as the incoming … this whole thing here will be proportional to a delta function") · the user's PHY 513 notes, Ch. 15 §15.1, Derivation "Three properties of $\mathcal M$ (filled in)", first paragraph · PS §4.5, p. 104 · stated as a distribution here*

^thm-c6b-1-2

> [!derivation]- Derivation
> **Step 1** ($\hat S$ commutes with $\hat P^\mu$). $\hat P^\mu$ is conserved because the theory is invariant under translations in space and time (Noether, [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum|§C1b.7]]; the generator form [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-2|Theorem §C3.5.2]]): $[\hat H, \hat P^\mu] = 0$. By induction on $k$,
>
> $$
> [\hat H^k, \hat P^\mu] = \hat H\,[\hat H^{k-1}, \hat P^\mu] + [\hat H, \hat P^\mu]\,\hat H^{k-1} = \hat H\cdot0 + 0\cdot\hat H^{k-1} = 0 ,
> $$
>
> and term by term in the exponential series,
>
> $$
> \bigl[e^{-i\hat H\,2T}, \hat P^\mu\bigr] = \sum_{k\ge0}\frac{(-2iT)^k}{k!}\,[\hat H^k, \hat P^\mu] = 0 \qquad\text{for every } T .
> $$
>
> In the limit $T \to \infty$ of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]] (taken in matrix elements between its states), $\hat S\hat P^\mu = \hat P^\mu\hat S$.
>
> **Step 2** (matrix elements). Sandwich $\hat S\hat P^\mu - \hat P^\mu\hat S = 0$ between $\langle f|$ and $|i\rangle$, using $\hat P^\mu|i\rangle = p_i^\mu|i\rangle$ and $\langle f|\hat P^\mu = p_f^\mu\langle f|$ ($\hat P^\mu$ self-adjoint, eigenvalues real):
>
> $$
> 0 = \langle f|\hat S\hat P^\mu|i\rangle - \langle f|\hat P^\mu\hat S|i\rangle = p_i^\mu\langle f|\hat S|i\rangle - p_f^\mu\langle f|\hat S|i\rangle = (p_i - p_f)^\mu\,\langle f|\hat S|i\rangle \qquad (\mu = 0, 1, 2, 3) .
> $$
>
> The same computation with $\mathbb 1$ in place of $\hat S$ gives $(p_i - p_f)^\mu\langle f|i\rangle = 0$. Subtracting, with $i\hat T = \hat S - \mathbb 1$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]]):
>
> $$
> (p_i - p_f)^\mu\,\langle f|i\hat T|i\rangle = (p_i - p_f)^\mu\langle f|\hat S|i\rangle - (p_i - p_f)^\mu\langle f|i\rangle = 0 .
> $$
>
> **Step 3** (support). Change variables from the momenta to $\Delta = p_i - p_f$ and the remaining independent momenta, a linear change of variables with constant Jacobian ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 1). Write $A(\Delta) \equiv \langle f|i\hat T|i\rangle$, a distribution in $\Delta$ with the remaining momenta as parameters. Step 2 reads $\Delta^\mu A = 0$ for $\mu = 0, \dots, 3$. Let $\varphi$ be a test function with $0 \notin \operatorname{supp}\varphi$. On $\operatorname{supp}\varphi$ some $\Delta^\mu \ne 0$, so $\varphi = \sum_\mu\Delta^\mu\psi_\mu$ with smooth $\psi_\mu = \varphi\,\Delta^\mu/|\Delta|_E^2$ ($|\Delta|_E^2 = \sum_\nu(\Delta^\nu)^2$, Euclidean), and
>
> $$
> A[\varphi] = \sum_\mu A[\Delta^\mu\psi_\mu] = \sum_\mu(\Delta^\mu A)[\psi_\mu] = 0 :
> $$
>
> $\operatorname{supp}A \subseteq \{\Delta = 0\}$.
>
> **Step 4** (only δ itself survives). By [[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]], $A = \sum_{|\alpha|\le N}c_\alpha\,\partial^\alpha\delta^4(\Delta)$, with multi-indices $\alpha = (\alpha_0, \dots, \alpha_3)$ and $\partial^\alpha = \partial_{\Delta^0}^{\alpha_0}\cdots\partial_{\Delta^3}^{\alpha_3}$. Multiplication by $\Delta^\mu$ on each term, from the definition of the derivative of a distribution ([[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]]) and the Leibniz rule at $\Delta = 0$:
>
> $$
> \bigl(\Delta^\mu\,\partial^\alpha\delta^4\bigr)[\varphi] = (-1)^{|\alpha|}\,\partial^\alpha(\Delta^\mu\varphi)\big|_{\Delta=0} = (-1)^{|\alpha|}\,\alpha_\mu\,\partial^{\alpha - e_\mu}\varphi\big|_{\Delta=0} = -\alpha_\mu\,\bigl(\partial^{\alpha - e_\mu}\delta^4\bigr)[\varphi] ,
> $$
>
> since every Leibniz term in which no derivative hits $\Delta^\mu$ still carries a factor $\Delta^\mu = 0$. So $\Delta^\mu\partial^\alpha\delta^4 = -\alpha_\mu\,\partial^{\alpha - e_\mu}\delta^4$; the lowest cases are $\Delta^\mu\delta^4(\Delta) = 0$ and $\Delta^\mu\partial_{\Delta^\nu}\delta^4(\Delta) = -\delta^\mu_\nu\,\delta^4(\Delta)$. Hence
>
> $$
> 0 = \Delta^\mu A = -\sum_{|\alpha|\le N,\ \alpha_\mu\ge1}\alpha_\mu\,c_\alpha\,\partial^{\alpha - e_\mu}\delta^4(\Delta) .
> $$
>
> The derivatives $\partial^\beta\delta^4$ for distinct $\beta$ are linearly independent (test them on $\varphi = \Delta^\beta$ near 0), and $\alpha \mapsto \alpha - e_\mu$ is injective, so $\alpha_\mu c_\alpha = 0$ for every $\alpha$ and $\mu$. Every $\alpha \ne 0$ has some $\alpha_\mu \ge 1$: $c_\alpha = 0$ for $|\alpha| \ge 1$, and
>
> $$
> A = c_0\,\delta^4(\Delta) = \delta^4(p_i - p_f)\;C(p_A, p_B, \dots; p_1, p_2, \dots) .
> $$
>
> The coefficient $C = c_0$ depends on the remaining momenta; that it is smooth there is the assumption in the statement.
>
> **What the derivation shows.**
> - The delta function is forced by symmetry alone, "before we even discuss what theory we're talking about"; only its coefficient knows the dynamics.
> - The assumption that $C$ is smooth excludes further delta functions, which come from parts of the process in which some particles do not interact at all (disconnected pieces, [[§C6b.8 Amplitudes from Correlation Functions|§C6b.8]]).

^der-c6b-1-2

*Uses:* [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]], [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-2|Theorem §C3.5.2]], [[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]], [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]]

> [!definition] Definition §C6b.1.3: The Invariant Amplitude
> Since $\hat T$ conserves energy-momentum ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-2|Theorem §C6b.1.2]]), the delta function is removed:
>
> $$
> \langle\mathbf p_1\mathbf p_2\cdots|i\hat T|\mathbf p_A\mathbf p_B\cdots\rangle = (2\pi)^4\delta^4\Bigl(\sum_{A, B, \dots}p - \sum_{1, 2, \dots}p\Bigr)\;i\mathcal M(p_A, p_B, \dots \to p_1, p_2, \dots) .
> $$
>
> The **amplitude** $\mathcal M$, the "invariant matrix element", is dynamical data.
>
> *Source: PHY 513 Lecture 15, slide 6 ("$\langle\vec p_1\vec p_2\ldots|i\mathcal T|\vec p_A\vec p_B\ldots\rangle = (2\pi)^4\delta^{(4)}(\sum_{A,B,\ldots}p - \sum_{1,2,\ldots}p)\,i\mathcal M$. Amplitude $\mathcal M$ = 'invariant matrix element'. The amplitude is dynamical data."), and transcript ("The coefficient of that we call $M$") · the user's PHY 513 notes, Ch. 15 §15.1, eq. (Mdef) · PS §4.5, eq. (4.73) · Yu §6.5, eq. (6.275)*

^def-c6b-1-3


Where the $(2\pi)^4$ and the $i$ of $i\mathcal M$ come from: at first order $\langle f|i\hat T|i\rangle = -i\int d^4x\,\langle f|\hat{\mathcal H}_I(x)|i\rangle$, and every external particle contributes a plane wave $e^{\pm ip\cdot x}$ ([[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^lem-c6b-9-4|Lemma §C6b.9.4]]), so the vertex integral is ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]])
$$
\int d^4x\;e^{i(\sum_{\rm out}p - \sum_{\rm in}p)\cdot x} = (2\pi)^4\delta^4\Bigl(\sum_{\rm in}p - \sum_{\rm out}p\Bigr) .
$$
The $i$ is kept with $\mathcal M$ so that a vertex $-i\lambda$ gives $i\mathcal M = -i\lambda$, $\mathcal M = -\lambda$ ([[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-1|Example §C6b.8.1]]); $(2\pi)^4\delta^4(0)$, which squaring this delta function produces, is the spacetime volume of a box, $\tilde V\tilde T$, with $2\pi\delta(0) = \tilde T$ the duration ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10|Theorem §CA.3.10]]; [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-2|Theorem §C6b.2.2]]).

> [!remark] Remark: What "dynamical" means
> "By dynamical data, we mean things that depend on … the potentials. It's not something you can just get by energy conservation. It should depend on … what theory [we are talking] about." Everything else in a cross section or a decay rate, the $\mathbb 1$, the delta function, the normalization of the states, the phase space, is kinematics and is the same in every theory. So $\mathcal M$ "is kind of the proper matrix element that we actually really want", and the Feynman rules are rules for computing it ([[§C6b.8 Amplitudes from Correlation Functions|§C6b.8]]).
>
> *Source: PHY 513 Lecture 15, transcript · the user's PHY 513 notes, Ch. 15 §15.1*

^rem-c6b-1-3

> [!theorem] Theorem §C6b.1.3: The Mass Dimension of the Amplitude
> For a process with $N$ external particles in total (initial plus final),
>
> $$
> [\mathcal M] = 4 - N .
> $$
>
> For $2 \to 2$ scattering $\mathcal M$ is dimensionless, as is the coupling $\lambda$ of $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-2|Theorem §C6a.1.2]]).
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.1, Derivation "Three properties of $\mathcal M$ (filled in)", second paragraph*

^thm-c6b-1-3

> [!derivation]- Derivation
> **Step 1** (one-particle states). With $[E] = 1$ and $[\delta^3(\mathbf p)] = -3$, the normalization of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]] gives
>
> $$
> 2\,[|\mathbf p\rangle] = [\langle\mathbf p|\mathbf q\rangle] = \bigl[2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)\bigr] = 1 + (-3) = -2 \quad\Rightarrow\quad [|\mathbf p\rangle] = -1 .
> $$
>
> **Step 2** ($k$-particle states). For $k = 2$ the overlap is ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]] with the factors $\sqrt{2E}$ of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]])
>
> $$
> \langle\mathbf p_1\mathbf p_2|\mathbf q_1\mathbf q_2\rangle = \sqrt{2E_{\mathbf p_1}2E_{\mathbf p_2}2E_{\mathbf q_1}2E_{\mathbf q_2}}\;(2\pi)^6\bigl[\delta^3(\mathbf p_1 - \mathbf q_1)\delta^3(\mathbf p_2 - \mathbf q_2) + \delta^3(\mathbf p_1 - \mathbf q_2)\delta^3(\mathbf p_2 - \mathbf q_1)\bigr] ,
> $$
>
> of dimension $\frac12(1 + 1 + 1 + 1) - 3 - 3 = -4$, so $[|\mathbf p_1\mathbf p_2\rangle] = -2$. In general each particle brings $\sqrt{2E}\cdot\sqrt{2E}$ and one $\delta^3$ to the overlap, dimension $k\cdot1 - 3k = -2k$, so $[|\mathbf p_1\cdots\mathbf p_k\rangle] = -k$.
>
> **Step 3** ($\hat S$ and $\hat T$ are dimensionless). $[\hat H] = 1$ and $[T] = -1$, so the exponent of $e^{-i\hat H\,2T}$ is dimensionless and $[\hat S] = 0$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]]); $i\hat T = \hat S - \mathbb 1$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]]) gives $[\hat T] = 0$.
>
> **Step 4** (both sides of Def. §C6b.1.3). With $k_i$ initial and $k_f$ final particles, $N = k_i + k_f$:
>
> $$
> \underbrace{-k_f}_{\langle\mathbf p_1\cdots|} + \underbrace{0}_{i\hat T} + \underbrace{(-k_i)}_{|\mathbf p_A\cdots\rangle} = -N \;=\; \underbrace{0}_{(2\pi)^4} + \underbrace{(-4)}_{\delta^4} + [\mathcal M] \quad\Rightarrow\quad [\mathcal M] = 4 - N .
> $$
>
> **What the derivation shows.**
> - The dimension of $\mathcal M$ is fixed by the number of external particles alone; for $N = 4$ the amplitude is dimensionless, so at lowest order in $\phi^4$ theory it can only be a number times $\lambda$ ([[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-1|Example §C6b.8.1]]).

^der-c6b-1-3

*Uses:* [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]]

> [!theorem] Theorem §C6b.1.4: The Amplitude of Spinless Particles Is Lorentz Invariant
> If $\hat S$ commutes with the unitary representation $U(\Lambda)$ of the proper orthochronous Lorentz group on the in and out states, and the particles are spinless, then
>
> $$
> \mathcal M(\Lambda p_A, \Lambda p_B, \dots \to \Lambda p_1, \Lambda p_2, \dots) = \mathcal M(p_A, p_B, \dots \to p_1, p_2, \dots) \qquad \text{for every } \Lambda \in SO^+(1, 3) .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.1, Derivation "Three properties of $\mathcal M$ (filled in)", third paragraph · PHY 513 Lecture 15, slide 6 ("invariant matrix element") · Yu §6.5, after eq. (6.275) ("$\mathcal M$ 是 Lorentz 不变的")*

^thm-c6b-1-4

> [!derivation]- Derivation
> **Step 1** (states). For a spinless particle, at $a = 0$ ([[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-4|Theorem §C3.5.4]], 1–2),
>
> $$
> U(\Lambda)|\mathbf p_A\mathbf p_B\cdots\rangle = |\Lambda\mathbf p_A\,\Lambda\mathbf p_B\cdots\rangle , \qquad \langle\mathbf p_1\mathbf p_2\cdots|U(\Lambda)^\dagger = \bigl(U(\Lambda)|\mathbf p_1\mathbf p_2\cdots\rangle\bigr)^\dagger = \langle\Lambda\mathbf p_1\,\Lambda\mathbf p_2\cdots| .
> $$
>
> **Step 2** (invariance of the matrix element). $U(\Lambda)$ is unitary and $U(\Lambda)^\dagger\hat SU(\Lambda) = \hat S$; with $U^\dagger\mathbb 1U = U^\dagger U = \mathbb 1$,
>
> $$
> U(\Lambda)^\dagger\,i\hat T\,U(\Lambda) = U(\Lambda)^\dagger\hat SU(\Lambda) - U(\Lambda)^\dagger\mathbb 1U(\Lambda) = \hat S - \mathbb 1 = i\hat T .
> $$
>
> With Step 1,
>
> $$
> \langle\Lambda\mathbf p_1\cdots|i\hat T|\Lambda\mathbf p_A\cdots\rangle = \langle\mathbf p_1\cdots|U(\Lambda)^\dagger\,i\hat T\,U(\Lambda)|\mathbf p_A\cdots\rangle = \langle\mathbf p_1\cdots|i\hat T|\mathbf p_A\cdots\rangle .
> $$
>
> **Step 3** (the delta function is invariant). With $\Delta = \sum_{A,B,\dots}p - \sum_{1,2,\dots}p$, linearity of $\Lambda$ gives $\sum_{A,B,\dots}\Lambda p - \sum_{1,2,\dots}\Lambda p = \Lambda\Delta$, and ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 1; $\det\Lambda = 1$ for $\Lambda \in SO^+(1, 3)$)
>
> $$
> \delta^4(\Lambda\Delta) = |\det\Lambda|^{-1}\,\delta^4(\Delta) = \delta^4(\Delta) .
> $$
>
> **Step 4** (compare the coefficients). Write both sides of Step 2 with [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]] and use Step 3:
>
> $$
> (2\pi)^4\delta^4(\Delta)\;i\mathcal M(\Lambda p_A, \dots \to \Lambda p_1, \dots) = (2\pi)^4\delta^4(\Lambda\Delta)\;i\mathcal M(\Lambda p_A, \dots) = (2\pi)^4\delta^4(\Delta)\;i\mathcal M(p_A, \dots \to p_1, \dots) .
> $$
>
> The coefficient of $\delta^4(\Delta)$ is unique on the surface $\Delta = 0$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-2|Theorem §C6b.1.2]], Step 4), so $\mathcal M(\Lambda p) = \mathcal M(p)$ there.
>
> **What the derivation shows.**
> - The relativistic normalization ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]]) is what makes the coefficient invariant: with non-relativistic normalization, factors $E/E'$ would appear.
> - With spin, $\mathcal M$ carries spinor or polarization labels, and it transforms with the representation matrices of the external particles instead of being invariant.

^der-c6b-1-4

*Uses:* [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-4|Theorem §C3.5.4]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-2|Theorem §C6b.1.2]]

> [!theorem] Theorem §C6b.1.5: Spinless 2 → 2 Kinematics in Terms of s and t
> For $A + B \to 1 + 2$ with on-shell momenta, $p^2 = m^2$, and $p_A + p_B = p_1 + p_2$, let $s = (p_A + p_B)^2$, $t = (p_A - p_1)^2$, $u = (p_A - p_2)^2$ ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]]). Then
> 1. the six scalar products are
>
> $$
> \begin{aligned}
> 2p_A\cdot p_B &= s - m_A^2 - m_B^2 , & 2p_A\cdot p_1 &= m_A^2 + m_1^2 - t , & 2p_A\cdot p_2 &= m_A^2 + m_2^2 - u ,\\
> 2p_1\cdot p_2 &= s - m_1^2 - m_2^2 , & 2p_B\cdot p_2 &= m_B^2 + m_2^2 - t , & 2p_B\cdot p_1 &= m_B^2 + m_1^2 - u ,
> \end{aligned}
> $$
>
> and $u = m_A^2 + m_B^2 + m_1^2 + m_2^2 - s - t$;
> 2. $\varepsilon_{\mu\nu\rho\sigma}p_A^\mu p_B^\nu p_1^\rho p_2^\sigma = 0$.
>
> Hence a spinless amplitude ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]]) that depends on the momenta through scalar products and $\varepsilon$-contractions is a function of $s$ and $t$ alone.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.1, Derivation "Three properties of $\mathcal M$ (filled in)", third paragraph ("a function of the invariants $p_i\cdot p_j$") · written here from [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]]*

^thm-c6b-1-5

> [!derivation]- Derivation
> **Step 1** (expand the squares). With $p_i^2 = m_i^2$,
>
> $$
> s = (p_A + p_B)^2 = m_A^2 + m_B^2 + 2p_A\cdot p_B , \qquad t = (p_A - p_1)^2 = m_A^2 + m_1^2 - 2p_A\cdot p_1 , \qquad u = (p_A - p_2)^2 = m_A^2 + m_2^2 - 2p_A\cdot p_2 ,
> $$
>
> which are the first row of part 1 solved for the products.
>
> **Step 2** (conservation gives the second row). $p_1 + p_2 = p_A + p_B$, $p_B - p_2 = p_1 - p_A$ and $p_B - p_1 = p_2 - p_A$, so
>
> $$
> s = (p_1 + p_2)^2 = m_1^2 + m_2^2 + 2p_1\cdot p_2 , \qquad t = (p_B - p_2)^2 = m_B^2 + m_2^2 - 2p_B\cdot p_2 , \qquad u = (p_B - p_1)^2 = m_B^2 + m_1^2 - 2p_B\cdot p_1 .
> $$
>
> **Step 3** (the sum rule). [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], 1, with $1, 2, 3, 4 \to A, B, 1, 2$: $s + t + u = m_A^2 + m_B^2 + m_1^2 + m_2^2$.
>
> **Step 4** (the ε-invariant). Substitute $p_2 = p_A + p_B - p_1$ and use linearity:
>
> $$
> \varepsilon_{\mu\nu\rho\sigma}p_A^\mu p_B^\nu p_1^\rho p_2^\sigma = \varepsilon_{\mu\nu\rho\sigma}p_A^\mu p_B^\nu p_1^\rho p_A^\sigma + \varepsilon_{\mu\nu\rho\sigma}p_A^\mu p_B^\nu p_1^\rho p_B^\sigma - \varepsilon_{\mu\nu\rho\sigma}p_A^\mu p_B^\nu p_1^\rho p_1^\sigma = 0 + 0 - 0 ,
> $$
>
> each term contracting a symmetric product $p^\mu p^\sigma$ with an antisymmetric symbol ([[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-1|Example §C1a.5.1]]).
>
> **Step 5** (consequence). By parts 1–2 every scalar product and the only $\varepsilon$-contraction of the four momenta are functions of $s$, $t$ and the masses. (That a Lorentz-invariant function of vectors depends on them only through scalar products and $\varepsilon$-contractions is the first fundamental theorem of invariant theory for the orthogonal group, H. Weyl, *The Classical Groups*, Ch. II; standard, not proved here: hence the hypothesis in the statement.)
>
> **What the derivation shows.**
> - Two invariants describe $2 \to 2$ kinematics; in the centre-of-mass frame $s = E_{\rm cm}^2$ and $t$ fixes the scattering angle ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], 3).

^der-c6b-1-5

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-1|Example §C1a.5.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]]

> [!remark] Remark: The big picture
> - Spectrum and interactions (a Lagrangian) ⇒ Feynman rules. "Next few lectures: Feynman rules in different theories."
> - Feynman rules compute amplitudes $i\mathcal M$, "usually the most laborious step when analyzing a process".
> - The amplitude $i\mathcal M$ and general principles (such as kinematics) ⇒ physical variables: cross sections, decay widths, … "The focus of this lecture."
>
> The Feynman rules are the content of the dynamical theory: which lines exist, how they attach, "sometimes … oriented lines … that all have an arrow". Lecture 14 gave one example ([[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-2|Theorem §C6a.10.2]]). Lecture 15 assumes $\mathcal M$ is known, "which you don't really, but you will on Monday", and asks what to do with it: $\mathcal M$ is "similar to a wave function", its square "something like a probability, but it's not exactly that": the cross section "is not a probability, but it's kind of more probability".
>
> *Source: PHY 513 Lecture 15, slide 7 ("The Big Picture"), and transcript · the user's PHY 513 notes, Ch. 15 §15.1, Principle "Dynamics versus kinematics" and Figure "bigpicture" (a programmatic statement, kept here as a remark)*

^rem-c6b-1-4

> [!caution] Caution: Four S's
> From this section on, four different objects are called $S$:
> 1. the **$S$-matrix** $\hat S$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]]), an operator, hatted here;
> 2. the **symmetry factor** $S = |\operatorname{Aut}|$ of a Feynman diagram ([[§C6a.8 Position-Space Feynman Rules#^def-c6a-8-1|Def. §C6a.8.1]]), a positive integer from overcounted contractions;
> 3. the **identical-particle factor** $S_{\rm id} = \prod_kn_k!$ for $n_k$ identical particles of species $k$ in a final state ([[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-4|Theorem §C6b.5.4]]), a positive integer from overcounted final states; the user's notes write $S$, Yu $\mathcal S$ (eq. (6.305));
> 4. the **scalar bilinear** $\mathsf S = \bar\psi\psi$ ([[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]]), sans-serif.
>
> The action $S = \int d^4x\,\mathcal L$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-2|Def. §C1b.2.2]]) is a fifth; the lecture: "probably with a fancy calligraphic $S$ … not to be confused with action". Factors 2 and 3 can occur in the same calculation ([[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-2|Example §C6b.8.2]]: $S = 1$ for the diagram, $S_{\rm id} = 2$ for the final state).
>
> *Source: PHY 513 Lecture 15, transcript · the user's PHY 513 notes, Ch. 15 §15.4 (paragraph "Identical particles (filled in)": "This $S$ is unrelated to the $S$-matrix and to the symmetry factor of a diagram"), PART 2 (e) (notation table) · Yu §6.5, eq. (6.305) · [[§C6a.8 Position-Space Feynman Rules#^cau-c6a-8-1|§C6a.8, Caution: Three S's]]*

^cau-c6b-1-2

> [!caution] Caution: Names for the S-matrix, the T-matrix and the amplitude
> - Slides: calligraphic $\mathcal S = 1 + i\mathcal T$, $\mathcal M$ (slides 4, 6). In these notes the calligraphic $\mathcal T$ is time reversal ([[Larsen PHY 513]], row "Discrete Lorentz transformations") and $\mathcal S$ the Schwartz space of test functions ([[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]]), so the operators are written $\hat S$, $\hat T$.
> - PS: $S$, $T$, $S = \mathbf 1 + iT$ (eqs. (4.71)–(4.73)), $\mathcal M$ "invariant matrix element"; $\delta^{(4)}(k_{\mathcal A} + k_{\mathcal B} - \sum p_f)$.
> - Yu: $S$-operator $S$, $S = \mathbb I + iT$ (eq. (6.272)), $T_{fi} = \langle f|T|i\rangle$ (eq. (6.273)), $iT_{fi} = (2\pi)^4\delta^{(4)}(p_i - p_f)\,i\mathcal M$ (eq. (6.275)); $\mathcal M$ is 不变矩阵元 or 不变散射振幅 (invariant scattering amplitude).
> - The user's notes: $S$, $T$, $\mathbb 1$; "a third use of $T$, after large time and time ordering".
> - Quantum Mechanics (Sakurai) normalizes differently: $S_{ni} = \delta_{ni} - 2\pi i\,\delta(E_n - E_i)\,T_{ni}$ ([[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-1|QM Theorem §C10.1.1]]): only energy is conserved (a fixed potential breaks translation invariance), and the sign and the $2\pi$ differ. The scattering amplitude $f$ of quantum mechanics is the analogue of $\mathcal M$ (PS p. 104).
>
> *Source: PHY 513 Lecture 15, slides 4, 6 · PS §4.5, eqs. (4.71)–(4.73), p. 104 · Yu §6.5, eqs. (6.272)–(6.275) · the user's PHY 513 notes, PART 2 (e)*

^cau-c6b-1-3

> [!caution] Caution: Four T's
> From this section on, four objects are written with $T$:
> 1. the half-duration $T$ of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]], the evolution running from $-T$ to $+T$; PS write the same, and the vacuum bubbles of [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]] are proportional to $2T$;
> 2. Yu's full duration $\tilde T = 2T$, which appears in the box route ([[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]]) as $2\pi\delta(0) = \tilde T$;
> 3. the $T$-matrix $\hat T$, an operator, hatted ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]]); the slides write $\mathcal T$, which in these notes is time reversal;
> 4. time ordering $T\{\cdots\}$, as in the time-ordered exponential ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]]).
>
> The user's notes call $\hat T$ "a third use of $T$, after large time and time ordering"; $\tilde T$ is the fourth.
>
> *Source: the user's PHY 513 notes, PART 2 (e) · Yu §6.5.1, eq. (6.282) · PS §4.5, eq. (4.70)*

^cau-c6b-1-4

> [!remark] Remark: Yu's route
> Yu introduces the $S$-matrix in §6.2 directly in the interaction picture. Particles prepared far apart are "asymptotic states" (渐近态), of the same form as multiparticle states of the free theory; the state $|\Psi(t)\rangle = \lim_{t_0\to-\infty}U(t, t_0)|i\rangle$ (eq. (6.122)) is projected on a final state in the far future, $S_{fi} = \lim\langle f|U(t, t_0)|i\rangle$ (eq. (6.123)), so $S_{fi} = \langle f|S|i\rangle$ (eq. (6.124)) with $S = U(+\infty, -\infty)$ (eq. (6.125)), Dyson's series (eq. (6.126)) and unitarity $S^\dagger S = \mathbb I$ (eq. (6.127)). The course defines $\hat S$ by the full evolution $e^{-i\hat H\,2T}$ between in and out states, as PS do (eqs. (4.70)–(4.71)); the two agree up to a phase between free states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]]). Yu then splits $S = \mathbb I + iT$ in §6.5 because the $n = 0$ term of the Dyson series is $\mathbb I$ ("$iT$ 包含所有 $n \ge 1$ 的项"), which is the course's "nothing happened" part read off the series.
>
> *Source: Yu §6.2, pp. 216–217, eqs. (6.122)–(6.127); §6.5, p. 238, eqs. (6.272)–(6.275)*

^rem-c6b-1-5

> [!remark]- Connections
> - In quantum mechanics the same $S$, $T$ split runs with only energy conserved, and the golden rule is its first order — [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-1|QM Theorem §C10.1.1]], [[§C9.5 Fermi's Golden Rule#^thm-c9-5-1|QM Theorem §C9.5.1]].
> - The problem of relating interacting asymptotic states to free states is the particle version of the vacuum projection of Lecture 13 — [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-1|Theorem §C6a.4.1]]; its solution, the LSZ formula, connects $\mathcal M$ to the correlation functions — [[§C6b.8 Amplitudes from Correlation Functions|§C6b.8]], QFT C10 (planned).
> - The delta function of four-momentum conservation is the same translation invariance that gives momentum conservation at every vertex of a diagram — [[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-1|Theorem §C6a.10.1]].
> - Lorentz invariance of $\mathcal M$ rests on the relativistic normalization chosen in Lecture 4 — [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]].
> - Correlation functions and the $S$-matrix are the two observables of the two points of view of Remark: The fundamental observable? — [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-7|Theorem §C6a.4.7]].
