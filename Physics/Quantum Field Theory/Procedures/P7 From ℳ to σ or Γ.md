---
type: procedure
subject: "[[Quantum Field Theory]]"
level: C
tags: [quantum-field-theory, procedure]
---
# P7 From ℳ to σ or Γ

Turns an amplitude $\mathcal M$ into an observable: a differential or total cross section for two colliding particles, or a decay rate (width) and lifetime for one. The route is Yu's box ([[§C6b.3 Transition Probabilities in a Box|§C6b.3]]), with every factor traced to the state normalization; the wave-packet version ([[§C6b.5 Wave Packets and the Cross Section|§C6b.5]]–[[§C6b.6 Evaluating the Cross Section|§C6b.6]]) gives the same formula. Input: $i\mathcal M$ from [[P6 Tree Amplitude from a Lagrangian]]; conventions in [[Larsen PHY 513]].

## Steps

1. **State the setup.** Two particles colliding ([[§C6b.3 Transition Probabilities in a Box#^mod-c6b-3-1|Model §C6b.3.1]], beam on target [[§C6b.4 The Cross Section#^mod-c6b-4-1|Model §C6b.4.1]]) or one particle decaying at rest ([[§C6b.8 Decay Rates and Widths#^mod-c6b-8-1|Model §C6b.8.1]]); the frame (rest frame of $A$, centre of mass); the final particles and whether some are identical; that the process is allowed on shell ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-5|Theorem §C6b.2.5]]). The states are free, relativistically normalized, over $|0\rangle$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]). ^p7-1

2. **The transition probability.** $P_{fi} = \dfrac{|\langle f|\hat S|i\rangle|^2}{\langle f|f\rangle\,\langle i|i\rangle}$, and for $f \ne i$ only $i\hat T$ contributes ([[§C6b.3 Transition Probabilities in a Box#^def-c6b-3-1|Def. §C6b.3.1]], [[§C6b.3 Transition Probabilities in a Box#^thm-c6b-3-2|Theorem §C6b.3.2]], 1); $\langle f|i\hat T|i\rangle = (2\pi)^4\delta^4(\sum p_{\rm in} - \sum p_{\rm out})\,i\mathcal M$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]). ^p7-2

3. **Strip the squared delta.** $\bigl[(2\pi)^4\delta^4(P)\bigr]^2 = (2\pi)^4\delta^4(0)\,(2\pi)^4\delta^4(P)$ with $(2\pi)^4\delta^4(0) = \tilde V\tilde T$ ([[§C6b.3 Transition Probabilities in a Box#^thm-c6b-3-2|Theorem §C6b.3.2]], 2; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10|Theorem §CA.3.10]]); the norms are $\langle\mathbf p|\mathbf p\rangle = 2E_{\mathbf p}\tilde V$ per particle ([[§C6b.3 Transition Probabilities in a Box#^thm-c6b-3-3|Theorem §C6b.3.3]]); dividing by $\tilde T$ gives the rate $R = P_{fi}/\tilde T$ ([[§C6b.3 Transition Probabilities in a Box#^thm-c6b-3-4|Theorem §C6b.3.4]]). ^p7-3

4. **Count the final states.** A momentum range $d^3p_j$ holds $\tilde V\,d^3p_j/(2\pi)^3$ box states ([[§C6b.3 Transition Probabilities in a Box#^thm-c6b-3-5|Theorem §C6b.3.5]]); the $\tilde V$'s cancel the final norms and leave the phase space $d\Pi_n = \prod_j\frac{d^3p_j}{(2\pi)^32E_j}(2\pi)^4\delta^4(P - \sum_jp_j)$ ([[§C6b.3 Transition Probabilities in a Box#^thm-c6b-3-6|Theorem §C6b.3.6]], [[§C6b.7 Lorentz Invariance and Two-Body Phase Space#^def-c6b-7-1|Def. §C6b.7.1]]): $dR = \frac{1}{\prod_{\rm in}2E\cdot\tilde V^{n_{\rm in} - 1}}|\mathcal M|^2d\Pi_n$. ^p7-4

5. **Divide by the flux, or by nothing.** Cross section: one $B$ per box of volume $\tilde V$ moving at $|\mathbf v_B|$ on $A$ at rest is a flux $|\mathbf v_B|/\tilde V$, and $d\sigma = dR\,\tilde V/|\mathbf v_B|$ ([[§C6b.4 The Cross Section#^def-c6b-4-1|Def. §C6b.4.1]], [[§C6b.4 The Cross Section#^thm-c6b-4-3|Theorem §C6b.4.3]]). Decay: the rate per particle is already $d\Gamma$ ([[§C6b.8 Decay Rates and Widths#^def-c6b-8-1|Def. §C6b.8.1]], [[§C6b.8 Decay Rates and Widths#^thm-c6b-8-3|Theorem §C6b.8.3]]). ^p7-5

6. **The formulas.** $d\sigma = \dfrac{|\mathcal M|^2\,d\Pi_n}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|}$ and $d\Gamma = \dfrac{|\mathcal M|^2\,d\Pi_n}{2m_A}$ ([[§C6b.4 The Cross Section#^thm-c6b-4-6|Theorem §C6b.4.6]], invariant form [[§C6b.4 The Cross Section#^thm-c6b-4-4|Theorem §C6b.4.4]]; [[§C6b.8 Decay Rates and Widths#^thm-c6b-8-4|Theorem §C6b.8.4]]; PS (4.79), (4.86)). ^p7-6

7. **Identical particles.** After integrating over all final momenta divide by $S_{\rm id} = \prod_kn_k!$: $\sigma = \frac{1}{S_{\rm id}}\int d\sigma$, $\Gamma = \frac{1}{S_{\rm id}}\int d\Gamma$; at a fixed point of phase space there is no factor ([[§C6b.3 Transition Probabilities in a Box#^thm-c6b-3-7|Theorem §C6b.3.7]], [[§C6b.6 Evaluating the Cross Section#^thm-c6b-6-4|Theorem §C6b.6.4]]; PS p. 108: "divide by $n!$ after integrating over all sets of momenta"). ^p7-7

8. **Two-body phase space.** In the centre-of-mass frame $\int d\Pi_2\,F = \int d\Omega\,\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}}F$, $|\mathbf p_1| = \lambda^{1/2}(E_{\rm cm}^2, m_1^2, m_2^2)/2E_{\rm cm}$ ([[§C6b.7 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-7-5|Theorem §C6b.7.5]], [[§C6b.7 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-7-6|Theorem §C6b.7.6]]); hence $(d\sigma/d\Omega)_{\rm cm}$ ([[§C6b.7 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-7-7|Theorem §C6b.7.7]]), $= |\mathcal M|^2/64\pi^2E_{\rm cm}^2$ for equal masses ([[§C6b.7 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-7-8|Theorem §C6b.7.8]]), and for a decay at rest $E_{\rm cm} = m_A$, $\Gamma = \frac{1}{S_{\rm id}}\frac{|\mathbf p_1|}{8\pi m_A^2}|\mathcal M|^2$ when $|\mathcal M|^2$ is isotropic ([[§C6b.8 Decay Rates and Widths#^thm-c6b-8-5|Theorem §C6b.8.5]]). ^p7-8

9. **Check.** Dimensions: $[\mathcal M] = 4 - N$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]]), $[\sigma] = -2$ for every $n$ ([[§C6b.6 Evaluating the Cross Section#^thm-c6b-6-3|Theorem §C6b.6.3]]), $[\Gamma] = 1$ ([[§C6b.8 Decay Rates and Widths#^der-c6b-8-4|Derivation §C6b.8.4]], first ⚑). Lorentz behaviour: $d\Pi_n$ is invariant ([[§C6b.7 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-7-4|Theorem §C6b.7.4]]), $\sigma$ transforms like a transverse area ([[§C6b.7 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-7-2|Theorem §C6b.7.2]]), a moving particle decays at $\Gamma/\gamma$ ([[§C6b.8 Decay Rates and Widths#^thm-c6b-8-10|Theorem §C6b.8.10]]). Units: $1\,\mathrm{GeV}^{-2} = 0.3894\,\mathrm{mb}$ ([[§C6b.4 The Cross Section#^def-c6b-4-2|Def. §C6b.4.2]]); $\hbar\Gamma = 1\,\mathrm{GeV} \Leftrightarrow \tau = 6.582\times10^{-25}\,\mathrm s$ ([[§C6b.8 Decay Rates and Widths|§C6b.8]]). Probabilities add up to one ([[§C6b.6 Evaluating the Cross Section#^thm-c6b-6-5|Theorem §C6b.6.5]]). ^p7-9

## Instances

| Process | Steps 1–2: setup, $\mathcal M$ | Steps 3–6: formula | Steps 7–8: integrate | Result |
| --- | --- | --- | --- | --- |
| $\phi\phi \to \phi\phi$ in $\phi^4$ | collision, CM frame; $\mathcal M = -\lambda$ | box chain written out: [[§C6b.11 From the Question to the Formula#^ex-c6b-11-3\|Example §C6b.11.3]] | equal masses, $S_{\rm id} = 2$: [[§C6b.9 Amplitudes from Correlation Functions#^ex-c6b-9-2\|Example §C6b.9.2]] | $\frac{\lambda^2}{64\pi^2E_{\rm cm}^2}$ per solid angle; $\sigma = \frac{\lambda^2}{32\pi E_{\rm cm}^2}$ |
| $\Phi \to \phi\phi$ in $\Phi\phi^2$ | decay at rest; $\mathcal M = -2\mu$ | [[§C6b.8 Decay Rates and Widths#^thm-c6b-8-4\|Theorem §C6b.8.4]] | $\delta(f(p))$ by hand: [[§C6b.8 Decay Rates and Widths#^ex-c6b-8-1\|Example §C6b.8.1]]; $S_{\rm id} = 2$ | $\Gamma = \frac{\mu^2}{8\pi M}\sqrt{1 - \frac{4m^2}{M^2}}$; [[§C6b.11 From the Question to the Formula#^ex-c6b-11-2\|Example §C6b.11.2]] |
| General two-body decay | decay at rest; any isotropic $\mathcal M$ | [[§C6b.8 Decay Rates and Widths#^thm-c6b-8-4\|Theorem §C6b.8.4]] | [[§C6b.8 Decay Rates and Widths#^thm-c6b-8-5\|Theorem §C6b.8.5]] (Yu (6.383)) | $\Gamma = \frac{1}{S_{\rm id}}\frac{\lvert\mathbf p_1\rvert}{8\pi m_A^2}\lvert\mathcal M\rvert^2$ |
| General $2 \to 2$, CM frame | collision | [[§C6b.7 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-7-7\|Theorem §C6b.7.7]] | [[§C6b.7 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-7-5\|Theorem §C6b.7.5]] | PS (4.84) |
| ★ Several decay channels | [[§C6b.8 Decay Rates and Widths#^thm-c6b-8-7\|★ Theorem §C6b.8.7]] (partial widths add) | | | |
| Three-body decays, QED processes | QFT C8 (planned) | | | |

## Pitfalls

- **Normalization.** The formulas assume relativistically normalized states; amplitudes between $\hat a^\dagger|0\rangle$ states lose $\sqrt{2E}$ per particle ([[§C6b.2 Matrix Elements between Particle States#^cau-c6b-2-1|§C6b.2, Caution: Two normalizations of one-particle states]]).
- **The squared delta.** It is not discarded: one $(2\pi)^4\delta^4(0) = \tilde V\tilde T$ is divided out by the time, the flux and the norms; nothing infinite is left.
- **Four S's.** $S_{\rm id}$ divides integrated rates; the symmetry factor $S$ of a diagram is already in $\mathcal M$; neither is $\hat S$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^cau-c6b-1-2|§C6b.1, Caution: Four S's]]).
- **The velocity difference** $|\mathbf v_A - \mathbf v_B|$ is not a relative velocity and may exceed 1 ([[§C6b.7 Lorentz Invariance and Two-Body Phase Space#^cau-c6b-7-1|§C6b.7, Caution: The velocity difference is not a relative velocity]]).
- **Decays use the rest frame.** $\frac{1}{2m_A}$, not $\frac{1}{2E_A}$; an unstable particle is not an asymptotic state, and the formula holds with $\mathcal M$ from the Feynman rules (PS pp. 107–108; [[§C6b.8 Decay Rates and Widths#^cau-c6b-8-1|§C6b.8, Caution: Free states in a decay amplitude]]).
- **Lowest order.** $\mathcal M$ from free states is the lowest-order amplitude; beyond it $\sqrt Z$ per external line ([[§C6b.9 Amplitudes from Correlation Functions#^cau-c6b-9-2|§C6b.9, Caution: The rule is stated at lowest order]]).
