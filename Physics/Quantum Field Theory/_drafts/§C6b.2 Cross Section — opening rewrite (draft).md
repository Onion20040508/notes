---
type: draft
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c, draft]
---
> [!warning] Draft — APPLIED 2026-10-31 (kept as a record)
> Applied in the C6b restructure "Yu's route is the main line" (plan `qft-C/C6-RESTRUCTURE-PLAN.md`, last section; map `qft-C/C6B-YU-MAP.json`): parts (i)–(ii) became [[§C6b.2 Transition Probabilities in a Box|§C6b.2]] and [[§C6b.3 The Cross Section|§C6b.3]] (the annotated formula ends §C6b.3); part (iii) became the opening table of [[§C6b.4 Wave Packets and the Cross Section|§C6b.4]], the careful version; every item of the audit (iv) is fixed in §C6b.1 and §C6b.4–§C6b.7 (and a CA home, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10|Theorem §CA.3.10]]). Section numbers in this draft were rewritten by the renumbering (old §C6b.2–§C6b.7 → §C6b.4–§C6b.9); its own box IDs (`dr-xs-…`) were never vault IDs. Do not cite this note; cite the sections above.

*Sources: Yu Zhao-Huan, 量子场论讲义, §6.5.1–§6.5.2, pp. 239–244, eqs. (6.276)–(6.321) (page images checked, PDF pp. 247–252) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.5, pp. 102–106, eqs. (4.65)–(4.80) · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), slides 8, 11–16 · the user's PHY 513 notes, Ch. 15 §15.2–§15.5 and §15.10 (paragraph "Correspondence with Yu").*

The cross section $d\sigma = \frac{1}{2E_A2E_B|\mathbf v_A - \mathbf v_B|}|\mathcal M|^2d\Pi_n$ ([[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-2|Theorem §C6b.5.2]]) has six factors besides $|\mathcal M|^2$. In the wave-packet derivation of [[§C6b.4 Wave Packets and the Cross Section|§C6b.4]]–[[§C6b.5 Evaluating the Cross Section|§C6b.5]], each of them appears in the middle of a fourteen-fold integral. This opening first derives the same formula by Yu's box route (i). Every factor there is a visible ratio of the box volume $\tilde V$, the duration $\tilde T$ and the normalizations of the states, and all powers of $\tilde V$ and $\tilde T$ cancel. It then writes the result once with each factor labelled by the step that produced it (ii), and explains what the careful wave-packet route adds, step by step (iii). Part (iv) lists what the current §C6b.1–§C6b.7 use without a stated origin.

*Conventions* ([[Larsen PHY 513]]): $\tilde V = L^3$ is the volume of a periodic box and $\tilde T$ the duration of the process. $\tilde T = 2T$ in the notation of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]] and [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]]; the tilde keeps both apart from $\hat T$ and $T\{\cdots\}$. Relativistic normalization holds ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]). $\mathbf v = \mathbf p/E$. In Steps 1–6, $A$ is at rest (Yu's fixed target) and the beam $B$ moves along $z$. $S_{\rm id}$ is the identical-particle factor ([[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-4|Theorem §C6b.5.4]]).

## (i) Every factor of dσ, in one picture

Plane-wave states have infinite norm, and the square of $\langle f|i\hat T|i\rangle$ contains the square of a $\delta^4$. In a box both are finite numbers. So: put the two particles in a box, compute the probability of a transition and the rate per unit time, count the final states, and divide by the flux.

> [!definition] Set-up: a box of volume Ṽ for a time T̃
> A cube of side $L$, volume $\tilde V = L^3$, with periodic boundary conditions, so the momenta are $\mathbf p \in \frac{2\pi}{L}\mathbb Z^3$. The process lasts a time $\tilde T$, and the time direction is treated like the spatial box. Then ([[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]] in space; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] at $p = 0$ on the box in spacetime; Yu (6.278)–(6.282))
>
> $$
> (2\pi)^3\delta^3(\mathbf 0) = \int_{\tilde V}d^3x = \tilde V , \qquad 2\pi\,\delta(0) = \int_{\tilde T}dt = \tilde T , \qquad (2\pi)^4\delta^4(0) = \int d^4x = \tilde V\tilde T ,
> $$
>
> and, as $L \to \infty$, a sum over the allowed momenta becomes an integral ([[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]]; Yu (6.302)):
>
> $$
> \sum_{\mathbf p} \;\longrightarrow\; \tilde V\int\frac{d^3p}{(2\pi)^3} , \qquad (2\pi)^3\delta^3(\mathbf p - \mathbf p') \;\longleftrightarrow\; \tilde V\,\delta_{\mathbf p\mathbf p'} .
> $$
>
> These are identities of the finite box. On all of space, $\delta^2$ and $\delta(0)$ have no value ([[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]); (iii) says how the wave packets avoid them.

^dr-xs-0

> [!derivation] Step 1 (the states and their norms)
> *Why:* a probability needs normalized states, and the norm of a momentum state is $\propto\delta^3(\mathbf 0)$, which is finite in the box.
>
> The initial state of two particles, and its norm ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]] at coincident momenta; Yu (6.284), (6.288)–(6.289)):
>
> $$
> |i\rangle = |\mathbf p_A\mathbf p_B\rangle = \sqrt{2E_A}\sqrt{2E_B}\;\hat a^\dagger_{A,\mathbf p_A}\hat a^\dagger_{B,\mathbf p_B}|0\rangle , \qquad \langle\mathbf p_A|\mathbf p_A\rangle = 2E_A(2\pi)^3\delta^3(\mathbf 0) = 2E_A\tilde V ,
> $$
>
> $$
> \langle i|i\rangle = \langle\mathbf p_A|\mathbf p_A\rangle\,\langle\mathbf p_B|\mathbf p_B\rangle = 2E_A\tilde V\cdot2E_B\tilde V = 4E_AE_B\tilde V^2 .
> $$
>
> For identical $A$, $B$ with $\mathbf p_A \ne \mathbf p_B$ the exchange term of the overlap ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]) contains $\delta_{\mathbf p_A\mathbf p_B} = 0$, and the result is the same. The final state of $n$ particles with distinct momenta (Yu (6.285), (6.290)):
>
> $$
> |f\rangle = \prod_{j=1}^n\sqrt{2E_j}\,\hat a^\dagger_{\mathbf p_j}|0\rangle , \qquad \langle f|f\rangle = \prod_{j=1}^n\bigl(2E_j\tilde V\bigr) .
> $$

^dr-xs-1

> [!derivation] Step 2 (the transition probability)
> *Why:* the Born rule for vectors that are not unit vectors divides by both norms, and the squared amplitude contains one $\delta^4$ too many, which the box turns into $\tilde V\tilde T$.
>
> The evolved state is $\hat S|i\rangle$, with $\langle\hat Si|\hat Si\rangle = \langle i|\hat S^\dagger\hat S|i\rangle = \langle i|i\rangle$ (unitarity: [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-1|Theorem §C6a.3.1]]; Yu (6.127)). The probability of finding it in $|f\rangle$ is the squared overlap of the unit vectors. For $f \ne i$ only $i\hat T$ contributes ([[§C6b.4 Wave Packets and the Cross Section#^lem-c6b-4-5|Lemma §C6b.4.5]]; Yu (6.276)):
>
> $$
> P_{fi} = \frac{|\langle f|\hat S|i\rangle|^2}{\langle f|f\rangle\,\langle i|i\rangle} = \frac{|\langle f|i\hat T|i\rangle|^2}{\langle i|i\rangle\,\langle f|f\rangle} .
> $$
>
> By [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], with $p_i = p_A + p_B$, $p_f = \sum_jp_j$, the numerator is a squared delta function. In the box $(2\pi)^4\delta^4(p_i - p_f) \leftrightarrow \tilde V\tilde T\,\delta_{p_ip_f}$ (Set-up), and $\delta_{p_ip_f}^2 = \delta_{p_ip_f}$, so
>
> $$
> \bigl[(2\pi)^4\delta^4(p_i - p_f)\bigr]^2 \leftrightarrow (\tilde V\tilde T)^2\,\delta_{p_ip_f} = \tilde V\tilde T\cdot\bigl[\tilde V\tilde T\,\delta_{p_ip_f}\bigr] \leftrightarrow (2\pi)^4\delta^4(0)\cdot(2\pi)^4\delta^4(p_i - p_f) ,
> $$
>
> $$
> |\langle f|i\hat T|i\rangle|^2 = \bigl[(2\pi)^4\delta^4(p_i - p_f)\bigr]^2|\mathcal M|^2 = \tilde V\tilde T\,(2\pi)^4\delta^4(p_i - p_f)\,|\mathcal M|^2
> $$
>
> (Yu (6.277), (6.283)). With Step 1 (Yu (6.291)):
>
> $$
> P_{fi} = \frac{\tilde V\tilde T\,(2\pi)^4\delta^4(p_i - p_f)\,|\mathcal M|^2}{4E_AE_B\tilde V^2\prod_{j=1}^n(2E_j\tilde V)} = \frac{\tilde T\,(2\pi)^4\delta^4(p_i - p_f)\,|\mathcal M|^2}{4E_AE_B\tilde V\prod_{j=1}^n(2E_j\tilde V)} .
> $$

^dr-xs-2

> [!derivation] Step 3 (per unit time)
> *Why:* $P_{fi}$ grows in proportion to the duration $\tilde T$, so the process happens at a constant rate, and the rate is the physical quantity.
>
> For one set of final momenta $\{\mathbf p_j\}$ (Yu (6.292)):
>
> $$
> R_{\{p_j\}} = \frac{P_{fi}}{\tilde T} = \frac{(2\pi)^4\delta^4\bigl(p_A + p_B - \sum_jp_j\bigr)\,|\mathcal M|^2}{4E_AE_B\tilde V\prod_{j=1}^n(2E_j\tilde V)} .
> $$

^dr-xs-3

> [!derivation] Step 4 (count the final states)
> *Why:* a detector accepts a range $d^3p_j$ of each final momentum, and in the box that range contains a finite number of states. The rate into the range is the sum of Step 3 over them.
>
> In one dimension, periodicity $\psi(-L/2) = \psi(L/2)$ of $\psi \propto e^{ipx}$ gives $e^{ipL} = 1$, so $p_k = \frac{2\pi}{L}k$, $k \in \mathbb Z$. The spacing is $\Delta p = \frac{2\pi}{L}$, so $\sum_k = \frac{L}{2\pi}\sum_k\Delta p \to \frac{L}{2\pi}\int dp$ (Yu (6.295)–(6.300)). In three dimensions $d^3p_j$ contains $\tilde V\frac{d^3p_j}{(2\pi)^3}$ states (Yu (6.302)). Summing Step 3 over them:
>
> $$
> dR = \prod_{j=1}^n\frac{\tilde V\,d^3p_j}{(2\pi)^3}\;R_{\{p_j\}} = \frac{1}{4E_AE_B\tilde V}\;\prod_{j=1}^n\frac{d^3p_j}{(2\pi)^3\,2E_j}\;(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_jp_j\Bigr)\,|\mathcal M|^2 ,
> $$
>
> because each counting factor cancels the $\tilde V$ of one final-state norm:
>
> $$
> \frac{\tilde V\,d^3p_j}{(2\pi)^3}\cdot\frac{1}{2E_j\tilde V} = \frac{d^3p_j}{(2\pi)^3\,2E_j}
> $$
>
> (Yu (6.303)). With $n_k$ identical particles of species $k$, integrating over all momenta counts each state $n_k!$ times, so the total rate is $\frac{1}{S_{\rm id}}\int dR$, $S_{\rm id} = \prod_kn_k!$ ([[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-4|Theorem §C6b.5.4]]; Yu (6.305)–(6.306)).

^dr-xs-4

> [!derivation] Step 5 (divide by the flux)
> *Why:* the cross section is the event rate with the set-up divided out ([[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-1|Def. §C6b.4.1]]): the rate per target particle divided by the flux of beam particles.
>
> A beam of $B$ particles with density $n_B$ and speed $|\mathbf v_B|$ sweeps, in time $t$, the volume $a|\mathbf v_B|t$ behind an area $a$. So $N_B = n_Ba|\mathbf v_B|t$ particles cross $a$, and the flux is (Yu (6.307))
>
> $$
> j_B = \frac{N_B}{a\,t} = n_B\,|\mathbf v_B| .
> $$
>
> On $N_A$ target particles the event count is $N = \sigma N_Aj_Bt$ (Yu (6.308); [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-1|Def. §C6b.4.1]]), so the rate per target particle is $R = \sigma j_B$. In the box there is one $A$ and one $B$, so $N_A = 1$ and $n_B = 1/\tilde V$:
>
> $$
> j_B = \frac{|\mathbf v_B|}{\tilde V} , \qquad \sigma = \frac{R}{j_B} = \frac{R\,\tilde V}{|\mathbf v_B|} .
> $$
>
> Yu writes the same with rates per unit volume: $\mathcal R = n_An_B|\mathbf v_B|\sigma$, $n_A = n_B = 1/\tilde V$, $\mathcal R = R/\tilde V$, and $\sigma = \frac{\mathcal R}{n_An_B|\mathbf v_B|} = \frac{R}{\tilde V}\cdot\frac{\tilde V^2}{|\mathbf v_B|} = \frac{R\tilde V}{|\mathbf v_B|}$ (Yu (6.312)–(6.313)).

^dr-xs-5

> [!derivation] Step 6 (the result in the rest frame of A; Ṽ and T̃ cancel)
> Insert Step 4 into Step 5, differential in the final momenta:
>
> $$
> d\sigma = \frac{\tilde V}{|\mathbf v_B|}\,dR = \frac{1}{4E_AE_B\,|\mathbf v_B|}\;\prod_{j=1}^n\frac{d^3p_j}{(2\pi)^3\,2E_j}\;(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_jp_j\Bigr)\,|\mathcal M|^2 , \qquad \sigma = \frac{1}{S_{\rm id}}\int d\sigma
> $$
>
> (Yu (6.313) for $\sigma$, (6.320)–(6.321)). Every power of $\tilde V$ and $\tilde T$ has cancelled:
>
> | step | factor | power of $\tilde V$ | power of $\tilde T$ |
> |---|---|---|---|
> | 2 | $(2\pi)^4\delta^4(0) = \tilde V\tilde T$ | $+1$ | $+1$ |
> | 1, 2 | $1/\langle i\vert i\rangle = 1/(4E_AE_B\tilde V^2)$ | $-2$ | $0$ |
> | 1, 2 | $1/\langle f\vert f\rangle = 1/\prod_j(2E_j\tilde V)$ | $-n$ | $0$ |
> | 3 | per unit time, $1/\tilde T$ | $0$ | $-1$ |
> | 4 | state counting, $\prod_j\tilde V\,d^3p_j/(2\pi)^3$ | $+n$ | $0$ |
> | 5 | per unit flux, $\tilde V/\lvert\mathbf v_B\rvert$ | $+1$ | $0$ |
> | | total | $1 - 2 - n + n + 1 = 0$ | $1 - 1 = 0$ |

^dr-xs-6

> [!derivation] Step 7 (any frame with collinear beams)
> *Why:* Yu's set-up has $A$ at rest; colliders work in the centre-of-mass frame.
>
> At rest $\mathbf v_A = \mathbf 0$ and $E_A = m_A$, so $|\mathbf v_B| = |\mathbf v_A - \mathbf v_B|$ and $4E_AE_B = 2E_A\,2E_B$. Step 6 becomes
>
> $$
> d\sigma = \frac{1}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|}\,|\mathcal M|^2\,d\Pi_n , \qquad d\Pi_n = \prod_{j=1}^n\frac{d^3p_j}{(2\pi)^3\,2E_j}\,(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_jp_j\Bigr)
> $$
>
> ([[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^def-c6b-6-1|Def. §C6b.6.1]]). Every factor on the right is unchanged by a boost along the beam:
> - $E_AE_B|\mathbf v_A - \mathbf v_B| = \sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2}$ ([[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-2|Theorem §C6b.6.2]], 1; [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-3|Theorem §C6b.6.3]]);
> - $|\mathcal M|^2$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]]);
> - $d\Pi_n$ ([[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-4|Theorem §C6b.6.4]]).
>
> The same expression therefore gives $d\sigma$ in every frame reached from the rest frame of $A$ by such a boost, the centre-of-mass frame included. The wave-packet route obtains it directly in any collinear frame ([[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-2|Theorem §C6b.5.2]]). Yu instead replaces $|\mathbf v_B|$ by the Møller velocity, which makes $\sigma$ Lorentz invariant by definition (Yu (6.315)–(6.316)). For collinear beams the two agree ([[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-3|Theorem §C6b.6.3]]).

^dr-xs-7

> [!theorem] Result: the cross section from the box
> For $2 \to n$ scattering with collinear beams and a final state different from the initial one,
>
> $$
> d\sigma = \frac{1}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|}\;|\mathcal M(p_A, p_B \to \{p_j\})|^2\;d\Pi_n , \qquad \sigma = \frac{1}{S_{\rm id}}\int d\sigma .
> $$
>
> The box volume and the duration have cancelled. This is [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-2|Theorem §C6b.5.2]] (PS (4.79); Yu (6.320) with $v_{\rm Møl}$).
>
> *Source: Yu §6.5.1–§6.5.2, eqs. (6.276)–(6.321) · PS §4.5, eq. (4.79)*

^dr-xs-r

## (ii) The annotated formula

$$
d\sigma = \underbrace{\underbrace{\frac{1}{2E_A\,2E_B}}_{\text{(a)}}\;\underbrace{\frac{1}{|\mathbf v_A - \mathbf v_B|}}_{\text{(b)}}}_{\text{flux factor}}\;\;\underbrace{|\mathcal M|^2}_{\text{(c) dynamics}}\;\;\underbrace{\prod_{j=1}^n\underbrace{\frac{d^3p_j}{(2\pi)^3}}_{\text{(d)}}\,\underbrace{\frac{1}{2E_j}}_{\text{(e)}}\;\underbrace{(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_jp_j\Bigr)}_{\text{(f)}}}_{\text{phase space }d\Pi_n}
$$

| label | factor | where it comes from | box step | careful route |
|---|---|---|---|---|
| (a) | $\frac{1}{2E_A\,2E_B}$ | the norm of the initial state, $\langle i\vert i\rangle = 2E_A\tilde V\cdot2E_B\tilde V$: relativistic normalization of the two incoming particles | [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-1\|Step 1]], [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-2\|Step 2]] | the packet factor $1/\sqrt{2E}$ of [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-3\|Def. §C6b.4.3]], squared in [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-2\|Derivation §C6b.5.2]], Step 6 |
| (b) | $\frac{1}{\lvert\mathbf v_A - \mathbf v_B\rvert}$ | the flux $j_B = n_B\lvert\mathbf v_B\rvert = \lvert\mathbf v_B\rvert/\tilde V$: cross section = rate / flux; in a moving frame, the boost-invariant combination | [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-5\|Step 5]], [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-7\|Step 7]] | the Jacobian of the longitudinal delta functions, [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-1\|Theorem §C6b.5.1]] |
| (c) | $\lvert\mathcal M\rvert^2$ | the squared amplitude after the $\delta^4$ is taken out | [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-2\|Step 2]] | $\mathcal M\bar{\mathcal M}^\ast$ at $\bar k = k$, [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-2\|Derivation §C6b.5.2]], Steps 2, 5–6 |
| (d) | $\frac{d^3p_j}{(2\pi)^3}$ | the number of box states in $d^3p_j$, $\tilde V\,d^3p_j/(2\pi)^3$, with $\tilde V$ cancelled | [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-4\|Step 4]] | the completeness measure in $\mathcal P(\mathbf b)$, [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-5\|Def. §C6b.4.5]] |
| (e) | $\frac{1}{2E_j}$ | the norm of the final state, $\langle f\vert f\rangle = \prod_j2E_j\tilde V$ | [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-1\|Step 1]], [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-2\|Step 2]] | the same measure ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2\|Def. §C2a.4.2]]) |
| (f) | $(2\pi)^4\delta^4(\cdots)$ | the second copy of $\delta^4$ in the squared amplitude; the first became $\tilde V\tilde T$ | [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-2\|Step 2]] | the $\delta^4$ of the unbarred amplitude, never used up ([[§C6b.5 Evaluating the Cross Section#^der-c6b-5-2\|Derivation §C6b.5.2]], Step 9) |

Two more factors do not appear in $d\sigma$. The $\frac{1}{S_{\rm id}}$ enters only when $d\sigma$ is integrated over all final momenta ([[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-4|Step 4]]). The box volume $\tilde V$ and the duration $\tilde T$ cancel ([[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-6|Step 6]], table).

## (iii) What the careful route adds

The box route squares a delta function. $(2\pi)^4\delta^4(0) = \tilde V\tilde T$ holds in a finite box, but on all of spacetime $\delta^2$ has no value ([[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]). Plane waves also fill the box uniformly, so the transverse offset of $B$ from $A$, the impact parameter, is never fixed. It is averaged with the uniform density $1/\tilde V$, and that average is the $n_B = 1/\tilde V$ of [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-5|Step 5]]. The wave-packet route of [[§C6b.4 Wave Packets and the Cross Section|§C6b.4]]–[[§C6b.5 Evaluating the Cross Section|§C6b.5]] works with normalizable states, $\langle\phi_{\mathbf p}|\phi_{\mathbf p}\rangle = 1$ ([[§C6b.4 Wave Packets and the Cross Section#^thm-c6b-4-2|Theorem §C6b.4.2]]), so no $\delta(0)$ ever appears. It fixes the impact parameter $\mathbf b$ and then integrates over it at unit density, which turns a probability into an area ([[§C6b.4 Wave Packets and the Cross Section#^thm-c6b-4-4|Theorem §C6b.4.4]]):

$$
\text{box: } \sigma = \frac{R}{j_B} , \quad j_B = \frac{|\mathbf v_B|}{\tilde V} \qquad\longleftrightarrow\qquad \text{packets: } d\sigma = \int d^2b\;\mathcal P(\mathbf b) , \quad N_{\rm events} = n_B\int d^2b\,\mathcal P(\mathbf b) .
$$

The first $\delta^4$ of the squared amplitude is not evaluated at zero. Together with $\int d^2b$, it does the six integrals over the conjugate copy $\bar k$:

$$
\text{box: } (2\pi)^4\delta^4(0) = \tilde V\tilde T \qquad\longleftrightarrow\qquad \text{packets: } \int d^2b\,e^{-i\mathbf b\cdot(\mathbf k_B - \bar{\mathbf k}_B)} = (2\pi)^2\delta^2(\mathbf k_B^\perp - \bar{\mathbf k}_B^\perp) \ \text{ and } \ (2\pi)^4\delta^4\Bigl(\bar k_A + \bar k_B - \sum_jp_j\Bigr) .
$$

Each step of the careful derivation, and the factor it produces:

| careful route (box) | what it does | factor | box counterpart |
|---|---|---|---|
| [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-3\|Def. §C6b.4.3]], [[§C6b.4 Wave Packets and the Cross Section#^thm-c6b-4-2\|Theorem §C6b.4.2]] | $\vert\phi_{\mathbf p}\rangle = \int\frac{d^3k}{(2\pi)^3}\frac{\phi(\mathbf k)}{\sqrt{2E_{\mathbf k}}}\vert\mathbf k\rangle$ with norm 1 | (a), via $1/\sqrt{2E}$ | [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-1\|Step 1]], $\langle i\vert i\rangle = 4E_AE_B\tilde V^2$ |
| [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-4\|Def. §C6b.4.4]], [[§C6b.4 Wave Packets and the Cross Section#^thm-c6b-4-3\|Theorem §C6b.4.3]] | the phase $e^{-i\mathbf b\cdot\mathbf k_B}$ displaces $B$ by $\mathbf b \perp \hat{\mathbf z}$ | none yet: fixes the offset | the uniform position of $B$ in the box, density $1/\tilde V$ |
| [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-5\|Def. §C6b.4.5]] | $\mathcal P(\mathbf b) = \prod_j\frac{d^3p_j}{(2\pi)^32E_j}\lvert\langle\mathbf p_1\cdots\vert\phi_A\phi_B\rangle\rvert^2$ | (d), (e) | [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-1\|Step 1]] ($\langle f\vert f\rangle$), [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-4\|Step 4]] (counting) |
| [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-6\|Def. §C6b.4.6]], [[§C6b.4 Wave Packets and the Cross Section#^thm-c6b-4-4\|Theorem §C6b.4.4]] | $d\sigma = \int d^2b\,\mathcal P(\mathbf b)$: events per unit flux | the definition of $\sigma$ | [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-5\|Step 5]], $\sigma = R/j_B$ |
| [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-2\|Derivation §C6b.5.2]], Step 1 | $\int d^2b\,e^{-i\mathbf b\cdot(\mathbf k_B - \bar{\mathbf k}_B)} = (2\pi)^2\delta^2(\mathbf k_B^\perp - \bar{\mathbf k}_B^\perp)$ | none: the two copies agree transversely | part of $(2\pi)^4\delta^4(0) = \tilde V\tilde T$ ([[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-2\|Step 2]]) |
| [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-2\|Derivation §C6b.5.2]], Step 2 ([[§C6b.4 Wave Packets and the Cross Section#^lem-c6b-4-5\|Lemma §C6b.4.5]]) | the amplitude and its conjugate, each with a $\delta^4$ | (c) as $\mathcal M\bar{\mathcal M}^\ast$; (f) | [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-2\|Step 2]], the squared $\delta^4$ |
| [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-2\|Derivation §C6b.5.2]], Step 3 | transverse parts of the barred $\delta^4$ fix $\bar{\mathbf k}_A^\perp$, $\bar{\mathbf k}_B^\perp$ | none | the transverse part of $\tilde V$ |
| [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-1\|Theorem §C6b.5.1]] (Step 4) | $\int d\bar k_A^zd\bar k_B^z\,\delta(\bar k_A^z + \bar k_B^z - P^z)\,\delta(\bar E_A + \bar E_B - E) = 1/\lvert\bar v_A^z - \bar v_B^z\rvert$ | (b) | [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-3\|Step 3]] (per unit time) and [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-5\|Step 5]] (per unit flux) |
| [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-2\|Derivation §C6b.5.2]], Steps 5–6 | $\bar k = k$; $\Phi\bar\Phi = \lvert\phi_A\rvert^2\lvert\phi_B\rvert^2/(2E_A2E_B)$, $\mathcal M\bar{\mathcal M}^\ast = \lvert\mathcal M\rvert^2$ | (a), (c) | [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-1\|Step 1]], [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-2\|Step 2]] |
| [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-2\|Derivation §C6b.5.2]], Steps 7–8 | smoothness: other factors at $p_A$, $p_B$; $\int\frac{d^3k}{(2\pi)^3}\lvert\phi\rvert^2 = 1$ | none: the packet shapes drop out | none: plane waves have sharp momenta from the start |
| [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-2\|Derivation §C6b.5.2]], Step 9 | read off; the unbarred $\delta^4$ remains | (f) | [[§C6b.2 Cross Section — opening rewrite (draft)#^dr-xs-2\|Step 2]], the second $\delta^4$ |

What the careful route adds, in short:
- no $\delta(0)$ and no box;
- the impact parameter, and with it the meaning of $\sigma$ as an area;
- the velocity factor as a Jacobian, in any collinear frame directly;
- the assumptions made explicit: narrow packets, smooth $\mathcal M$ and smooth detector acceptance, no forward scattering.

## (iv) Audit: what appears without a stated origin

From reading the current [[§C6b.1 The S-Matrix and the Invariant Amplitude|§C6b.1]]–[[§C6b.7 Decay Rates and Widths|§C6b.7]] (line numbers of 2026-10-31). The last column says where this demo already answers the item; "rollout" means the C6b rewrite still has to.

| # | box | line | item | what is missing | answered |
|---|---|---|---|---|---|
| 1 | [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1\|Def. §C6b.1.1]] | 24 | the states in $\lim_T\langle\mathbf p_1\cdots\vert e^{-i\hat H\,2T}\vert\mathbf p_A\cdots\rangle$ | which states these are (Schrödinger-picture packets prepared at $-T$ and read at $+T$, PS (4.70)); if they were eigenstates of $\hat H$, the exponential would be a phase | rollout |
| 2 | [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1\|Def. §C6b.1.1]] | 21 | $T$ = half the duration | four $T$'s ($T$, $\tilde T = 2T$, $\hat T$, $T\{\}$) without a caution; [[§C6b.1 The S-Matrix and the Invariant Amplitude#^cau-c6b-1-3\|§C6b.1, Caution: Names for the S-matrix, the T-matrix and the amplitude]] covers only $\hat S$, $\hat T$ | Conventions here; rollout |
| 3 | [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2\|Def. §C6b.1.2]] | 108 | the $i$ in $\hat S = \mathbb 1 + i\hat T$ | why $i$: the $n \ge 1$ terms of the Dyson series start with $-i\int\hat H_I$ (Yu (6.272)), so $i\hat T$ carries the $(-i)^n$ | rollout |
| 4 | [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3\|Def. §C6b.1.3]] | 197 | $(2\pi)^4$ and $i\mathcal M$ | $(2\pi)^4\delta^4$ is what a vertex integral $\int d^4x\,e^{ip\cdot x}$ produces ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3\|Theorem §CA.3.3]]); $i\mathcal M$ so that a vertex $-i\lambda$ gives $i\mathcal M = -i\lambda$. Neither is said at the definition | rollout |
| 5 | [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-1\|Def. §C6b.4.1]] | 25 | $N_{\rm events} = \sigma N_Aj_Bt$ | the assumptions behind linearity in $N_A$ and $j_B$ (thin target, independent single scatterings) | rollout |
| 6 | [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-3\|Def. §C6b.4.3]] | 69 | the $1/\sqrt{2E_{\mathbf k}}$ in the packet | the reason (the norm becomes $\int\frac{d^3k}{(2\pi)^3}\lvert\phi\rvert^2$) comes only after, in [[§C6b.4 Wave Packets and the Cross Section#^thm-c6b-4-2\|Theorem §C6b.4.2]]; that it is the origin of $\frac{1}{2E_A2E_B}$ in $d\sigma$ is never said there | (ii) row (a); (iii) |
| 7 | [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-3\|Def. §C6b.4.3]] | 69 | the profile $\phi(\mathbf k)$ and $\int\frac{d^3k}{(2\pi)^3}\lvert\phi\rvert^2 = 1$ | the normalization's later role (it collapses the six $k$ integrals, [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-2\|Derivation §C6b.5.2]], Step 8) is not announced | (iii) |
| 8 | [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-3\|Def. §C6b.4.3]]; [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-2\|Derivation §C6b.5.2]], Step 7 | 72; 215 | "sharply peaked", "vary slowly on the scale of the packet widths" | no scale: the momentum width must be small against the scale on which $\mathcal M$, $E$, $\mathbf v$ vary; no error estimate | rollout |
| 9 | [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-4\|Def. §C6b.4.4]] | 122 | the impact parameter $\mathbf b$ | why only a transverse shift (a shift along $z$ only delays the collision); why the state is then integrated over $\mathbf b$ (the reason is in [[§C6b.4 Wave Packets and the Cross Section#^thm-c6b-4-4\|Theorem §C6b.4.4]], after) | (iii), in part |
| 10 | [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-5\|Def. §C6b.4.5]] | 181 | the measure $\prod\frac{d^3p_i}{(2\pi)^32E_i}$ in $\mathcal P(\mathbf b)$ | its origin (completeness) is stated after the box, line 188; $\frac{1}{S_{\rm id}}$ for identical final particles is not mentioned until [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-4\|Theorem §C6b.5.4]] | (i) Step 4; (ii) rows (d), (e) |
| 11 | [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-6\|Def. §C6b.4.6]] | 194 | $d\sigma = \int d^2b\,\mathcal P(\mathbf b)$ | a definition whose reason (uniform density of incident particles, event count $n_B\int d^2b\,\mathcal P$) follows in [[§C6b.4 Wave Packets and the Cross Section#^thm-c6b-4-4\|Theorem §C6b.4.4]]: the "why" comes second | (i) Step 5; (iii) |
| 12 | [[§C6b.4 Wave Packets and the Cross Section\|§C6b.4]], Conventions | 16 | $\mathbf v = \mathbf k/E$ "is the velocity" | that $\mathbf k/E = \partial E/\partial\mathbf k$ is the group velocity of the packet is not said; only $\mathbf k = \gamma m\mathbf v$ in [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-1\|Derivation §C6b.5.1]], Step 5 | rollout |
| 13 | [[§C6b.5 Evaluating the Cross Section\|§C6b.5]], opening display | 20 | the barred variables $\bar{\mathbf k}_A$, $\bar{\mathbf k}_B$ | named "a second, complex-conjugated copy", without the formula $\bigl\lvert\int d^3k\,f(\mathbf k)\bigr\rvert^2 = \int d^3k\,d^3\bar k\,f(\mathbf k)f^\ast(\bar{\mathbf k})$ | rollout |
| 14 | [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-1\|Theorem §C6b.5.1]] | 49 | $P^z$, $E$, $g$; "longitudinal integrals" | $P^z$ and $E$ are defined only in [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-2\|Derivation §C6b.5.2]], Step 2 ($P = \sum_ip_i$); why the integrals split into transverse and longitudinal (the $\mathbf b$-integral constrains only $\perp$) is not said at the theorem | rollout |
| 15 | [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-1\|Derivation §C6b.5.1]] | 107 | the Jacobian $= 1/\lvert\mathbf v_A - \mathbf v_B\rvert$ | called "kinematics" but never connected to the flux $j_B = n_B\lvert\mathbf v\rvert$ of [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-1\|Def. §C6b.4.1]]: why a Jacobian is a flux | (ii) row (b); (iii) |
| 16 | [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-2\|Theorem §C6b.5.2]] | 125 | the first brace, "kinematics of the initial particles" | it lumps the state normalization $\frac{1}{2E_A2E_B}$ (Step 6) with the flux $\frac{1}{\lvert\mathbf v_A - \mathbf v_B\rvert}$ (Step 4); the separate origins are only inside the derivation | (ii) |
| 17 | [[§C6b.5 Evaluating the Cross Section\|§C6b.5]] opening, [[§C6b.5 Evaluating the Cross Section#^rem-c6b-5-2\|§C6b.5, Remark: Yu's route]], [[§C6b.7 Decay Rates and Widths#^der-c6b-7-4\|Derivation §C6b.7.4]] | 14, 401; 47 | $(2\pi)^4\delta^4(0) = \tilde V\tilde T$ | cited to [[§CA.2 Generalized Functions#^thm-ca-2-10\|Theorem §CA.2.10]], which states only $(2\pi)^3\delta^3(\mathbf 0) \leftrightarrow V$; $2\pi\delta(0) = \tilde T$ and the 4D form have no CA home; [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3\|Theorem §C6a.11.3]] writes the same as $2T\cdot V$ | (i) Set-up (cites [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3\|Theorem §CA.3.3]]); a CA box at rollout |
| 18 | [[§C6b.5 Evaluating the Cross Section#^rem-c6b-5-2\|§C6b.5, Remark: Yu's route]] | 401 | $n_{\mathcal A}$, $n_{\mathcal B}$, $\mathcal R$, $\sigma = \mathcal R/(n_{\mathcal A}n_{\mathcal B}\lvert\mathbf v_{\mathcal B}\rvert)$, $\langle i\vert i\rangle = 4E_{\mathcal A}E_{\mathcal B}\tilde V^2$ | used without definitions; the state counting $\sum \to \tilde V\int\frac{d^3p}{(2\pi)^3}$ given only by equation numbers | (i) Steps 1–6 |
| 19 | [[§C6b.6 Lorentz Invariance and Two-Body Phase Space\|§C6b.6]] opening; [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-1\|Theorem §C6b.6.1]] | 14; 24 | "a trick: undo the velocities", $\varepsilon_{xy\mu\nu}p_A^\mu p_B^\nu$ | why an $\varepsilon$-tensor component is the natural object (the dual of the transverse area element $dx\wedge dy$) appears only in [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^der-c6b-6-2\|Derivation §C6b.6.2]], Step 3 | rollout |
| 20 | [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-2\|Theorem §C6b.6.2]], 2 | 72 | "transforms like an area element … as $\sigma$ does" | no formula for how $\sigma$ transforms; the link between $F_{12}$ and the $d^2b$ of [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-6\|Def. §C6b.4.6]] is one sentence; why $d\sigma$ is boost invariant along $z$ is read off the formula only | (i) Step 7, in part |
| 21 | [[§C6b.7 Decay Rates and Widths#^def-c6b-7-1\|Def. §C6b.7.1]] | 21 | "quoted as the width, an energy" | why a rate is an energy ($\hbar = 1$; the full width at half maximum of [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-10\|Theorem §C6b.7.10]], later) is not said at the definition | rollout |
| 22 | [[§C6b.7 Decay Rates and Widths#^der-c6b-7-4\|Derivation §C6b.7.4]], Step 2 | 63–66 | $P_{fi} = \lvert\langle f\vert i\hat T\vert i\rangle\rvert^2/(\langle i\vert i\rangle\langle f\vert f\rangle)$ | why one divides by the norms (Born rule for non-unit vectors) and that $\langle\hat Si\vert\hat Si\rangle = \langle i\vert i\rangle$ (unitarity) | (i) Step 2 |
| 23 | [[§C6b.7 Decay Rates and Widths#^der-c6b-7-4\|Derivation §C6b.7.4]], Step 3 | 69 | "$P_{fi}$ grows linearly with $\tilde T$" | that the linear growth is what makes a rate meaningful (long-time limit, as in the golden rule, [[§C9.5 Fermi's Golden Rule#^thm-c9-5-1\|QM Theorem §C9.5.1]]) | (i) Step 3, in part |
| 24 | [[§C6b.7 Decay Rates and Widths#^mod-c6b-7-7\|Model §C6b.7.7]] | 297 | $+im\Gamma$ "which radiative corrections produce" | the origin is only in a folded ★ remark (Yu §10.6); at the model the course gives no reason beyond the slide | rollout |
