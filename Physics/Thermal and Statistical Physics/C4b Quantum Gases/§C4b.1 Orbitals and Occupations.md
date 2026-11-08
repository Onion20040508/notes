---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4b
section: C4b.1
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4a.11 A Coin, a Polymer, an Einstein Solid and Adsorption]] · ↑ [[· C4b Quantum Gases]] · [[§C4b.2 One Orbital in the Grand Ensemble]] →

*Sources: Mao, PHY 510 notes, §4.5.1–§4.5.2, eqs. (4.93)–(4.99) and boxes "Orbital label versus occupation number", "Wave–particle duality" · PHY 510 Lecture 10/6.*

An ideal quantum gas is many noninteracting particles in one-particle orbitals. Two separate problems are hidden in it: which orbitals exist, a wave problem in a box, and how many particles occupy each, a statistical problem. Solving them in that order lets one method serve for atoms, electrons, photons and phonons. This section does the first: modes of a box, labelled by $\ell$, each carrying quanta of energy $\hbar\omega_\ell$. Level B starts quantum statistics from occupation numbers directly ([[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^def-b10-1-1|Def. §B10.1.1]]); level C makes the wave-to-particle step explicit.

**Setup.** A cube of side $L$, volume $V = L^3$, periodic boundary conditions; a linear wave equation with plane-wave solutions. No statistics and no dispersion are chosen yet.

> [!definition] Definition §C4b.1.1: Orbital and Occupation Number
> An **orbital** $\ell$ is one complete one-particle state: a spatial wave pattern together with any internal label (spin, polarization). Its **occupation number** $n_\ell$ is how many particles are in it. A many-body occupation state is the list $\{n_\ell\}$ ([[§C3.5 Many-Particle States#^def-c3-5-3|Def. §C3.5.3]]). Changing $n_\ell$ changes neither the orbital nor its one-particle energy $\epsilon_\ell$; for example $n_{(1,0,0)} = 2$ means two bosons in the orbital with spatial label $(1, 0, 0)$.
>
> *Source: Mao §4.5.1, box "Orbital label ℓ versus occupation number n_ℓ"*

^def-c4b-1-1

> [!theorem] Theorem §C4b.1.1: Modes of a Periodic Box
> The spatial modes $\Psi_\ell(\mathbf r, t) = \phi_\ell(\mathbf r)e^{-i\omega_\ell t}$ with $-\nabla^2\phi_\ell = k_\ell^2\phi_\ell$ and $\phi_\ell(\mathbf r + L\mathbf e_\alpha) = \phi_\ell(\mathbf r)$ are
>
> $$
> \phi_\ell(\mathbf r) = \frac{1}{\sqrt V}e^{i\mathbf k_\ell\cdot\mathbf r}, \qquad \mathbf k_\ell = \frac{2\pi}{L}(\ell_x, \ell_y, \ell_z), \qquad \ell_\alpha \in \mathbb Z .
> $$
>
> The frequency comes from the wave equation through a dispersion relation: $\omega = ck$ for electromagnetic waves, $\omega = \hbar k^2/(2m)$ for free matter waves. Hard walls give standing waves with the same leading density of modes in a large box.
>
> *Model:* homogeneous linear waves in a periodic cube; *applies:* any dispersion $\omega(k)$.
>
> *Source: Mao §4.5.2, eqs. (4.93)–(4.97) · level B: [[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^thm-b10-1-5|Theorem §B10.1.5]]*

^thm-c4b-1-1

> [!derivation]- Derivation
> **Step 1.** Periodicity in direction $\alpha$ requires $e^{ik_{\ell,\alpha}L} = 1$, so $k_{\ell,\alpha}L = 2\pi\ell_\alpha$ with $\ell_\alpha \in \mathbb Z$.
>
> **Step 2.** $\int_V|e^{i\mathbf k\cdot\mathbf r}|^2d^3r = V$, so $1/\sqrt V$ normalizes.
>
> **Step 3.** Inserting $e^{i(\mathbf k\cdot\mathbf r - \omega t)}$ into $\partial_t^2E = c^2\nabla^2E$ gives $\omega^2 = c^2k^2$; into $i\hbar\partial_t\Psi = -\frac{\hbar^2}{2m}\nabla^2\Psi$ it gives $\hbar\omega = \hbar^2k^2/(2m)$.

^der-c4b-1-1

> [!principle] Principle §C4b.1.2: Excitations of a Mode Come in Quanta
> A fixed mode $\ell$ can be excited only in whole units. With $n_\ell = 0, 1, 2, \dots$ quanta its energy above the empty mode is
>
> $$
> E_{\ell,n_\ell} - E_{\ell,0} = n_\ell\,\epsilon_\ell, \qquad \epsilon_\ell = \hbar\omega_\ell, \qquad \mathbf p_\ell = \hbar\mathbf k_\ell .
> $$
>
> One quantum is identified with one particle in orbital $\ell$: photons for the electromagnetic field, phonons for elastic waves, atoms or electrons for matter waves. The empty-mode energy $E_{\ell,0}$, which may include a zero-point part, is a constant subtracted when counting thermal energies. Which values of $n_\ell$ are allowed depends on Bose or Fermi statistics ([[§C3.5 Many-Particle States#^pr-c3-5-1|Principle §C3.5.1]]).
>
> *Domain:* quantum input; a classical wave equation with boundary conditions fixes the modes but allows any amplitude.
>
> *Source: Mao §4.5.2, eqs. (4.98)–(4.99) and box "Wave–particle duality"*

^pr-c4b-1-2

> [!remark] Remark: Why a quantum of a wave counts as a particle
> Adding one quantum to a travelling mode changes its energy by $\hbar\omega_\ell$ and its momentum by $\hbar\mathbf k_\ell$, which is what one emitted or absorbed particle carries; detectors register these as separate, countable clicks. The wave pattern governs propagation and interference, and so where detection is likely; a quantum in a plane-wave orbital has no position before it is detected. The two descriptions are aspects of one excitation. For matter, the Schrödinger wave function is already a probability amplitude, so the step here is from one particle to many.

^rem-c4b-1-1

> [!caution] Caution: Do not mix up which orbital with how many
> $\ell$ labels a state and $n_\ell$ counts particles in it. With internal degeneracy $g_s$ (spin, polarization), each spatial $\mathbf k$ gives $g_s$ distinct orbitals.

^cau-c4b-1-1

> [!remark]- Connections
> - The many-body states $\{n_\ell\}$ are the Fock states of second quantization — [[§C12.2★ Second Quantization#^def-c12-2-1|QM Def. §C12.2.1]]; the quantized field version is QFT's mode expansion — [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-1|QFT Theorem §C2a.2.1]].
> - Statistics enters in the next step, one orbital at a time — [[§C4b.2 One Orbital in the Grand Ensemble|§C4b.2]].
