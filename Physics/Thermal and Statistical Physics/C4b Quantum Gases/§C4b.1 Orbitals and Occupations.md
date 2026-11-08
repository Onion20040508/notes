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

For particles that do not interact, the grand partition function will turn out to be a product over one-particle states, $\Xi = \prod_\ell\Xi_\ell$ ([[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-1|Theorem §C4b.3.1]]). That product splits the ideal quantum gas into two independent tasks, and this chapter takes them in turn:

1. **list the one-particle states** — a wave problem in a box, the same for atoms, electrons, photons and phonons (this section);
2. **find the occupation of each** — one grand-canonical sum per state ([[§C4b.2 One Orbital in the Grand Ensemble|§C4b.2]]).

Level B starts quantum statistics from occupation numbers directly ([[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^def-b10-1-1|Def. §B10.1.1]]); level C first derives the modes and their quanta.

**Setup.** A cube of side $L$, volume $V = L^3$, periodic boundary conditions; a linear wave equation with plane-wave solutions. No statistics and no dispersion are chosen yet.

> [!definition] Definition §C4b.1.1: Orbital and Occupation Number
> An **orbital** $\ell$ is one complete one-particle state: a spatial wave pattern together with any internal label (spin, polarization). Its **occupation number** $n_\ell$ is how many particles are in it. A many-body occupation state is the list $\{n_\ell\}$ ([[§C3.5 Many-Particle States#^def-c3-5-3|Def. §C3.5.3]]). The label and the count are independent data: $\epsilon_\ell$ belongs to the label, and the list $n_{(1,0,0)} = 2$, all other $n_\ell = 0$, is a two-boson state built from one orbital.
>
> *Source: Mao §4.5.1, box "Orbital label ℓ versus occupation number n_ℓ"*

^def-c4b-1-1

> [!theorem] Theorem §C4b.1.1: Modes of a Periodic Box
> The spatial modes $\Psi_\ell(\mathbf r, t) = \phi_\ell(\mathbf r)e^{-i\omega_\ell t}$ with $-\nabla^2\phi_\ell = k_\ell^2\phi_\ell$ and $\phi_\ell(\mathbf r + L\mathbf e_\alpha) = \phi_\ell(\mathbf r)$ are
>
> $$
> \phi_\ell(\mathbf r) = \frac{1}{\sqrt V}e^{i\mathbf k_\ell\cdot\mathbf r}, \qquad \mathbf k_\ell = \frac{2\pi}{L}(\ell_x, \ell_y, \ell_z), \qquad \ell_\alpha \in \mathbb Z ,
> $$
>
> with frequency fixed by the dispersion relation of the wave equation: $\omega = ck$ for electromagnetic waves, $\omega = \hbar k^2/(2m)$ for free matter waves.
>
> *Model:* homogeneous linear waves in a periodic cube; *applies:* any dispersion $\omega(k)$.
>
> *Source: Mao §4.5.2, eqs. (4.93)–(4.97) · level B (counting): [[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^thm-b10-1-5|Theorem §B10.1.5]]*

^thm-c4b-1-1

> [!derivation]- Derivation
> **Step 0** (completeness). The functions $e^{i\mathbf k_\ell\cdot\mathbf r}/\sqrt V$ form an orthonormal basis of the periodic functions on the cube (Fourier series), and each is an eigenfunction of $-\nabla^2$ with eigenvalue $|\mathbf k_\ell|^2$. So every periodic eigenfunction for $k^2$ is a combination of the plane waves with $|\mathbf k_\ell|^2 = k^2$, and the plane waves may be taken as the modes.
>
> **Step 1.** Periodicity in direction $\alpha$ requires $e^{ik_{\ell,\alpha}L} = 1$, so $k_{\ell,\alpha}L = 2\pi\ell_\alpha$ with $\ell_\alpha \in \mathbb Z$.
>
> **Step 2.** $\int_V|e^{i\mathbf k\cdot\mathbf r}|^2d^3r = V$, so $1/\sqrt V$ normalizes.
>
> **Step 3.** Inserting $e^{i(\mathbf k\cdot\mathbf r - \omega t)}$ into $\partial_t^2E = c^2\nabla^2E$ gives $\omega^2 = c^2k^2$; into $i\hbar\partial_t\Psi = -\frac{\hbar^2}{2m}\nabla^2\Psi$ it gives $\hbar\omega = \hbar^2k^2/(2m)$.

^der-c4b-1-1

> [!remark] Remark: Hard walls instead of periodic ones
> With $\phi = 0$ on the walls the modes are products of $\sin(\pi n_\alpha x_\alpha/L)$, $n_\alpha \ge 1$: one point per $(\pi/L)^3$, but only in the octant $k_\alpha > 0$. Per unit $d^3k$ over all directions this is $\tfrac18(L/\pi)^3 = V/(2\pi)^3$, the periodic count, up to surface corrections of relative size $1/(kL)$ ([[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^thm-b10-1-5|Theorem §B10.1.5]]).

^rem-c4b-1-1

> [!principle] Principle §C4b.1.2: Excitations of a Mode Come in Quanta
> A fixed mode $\ell$ is excited only in whole units: its energy above the empty mode is
>
> $$
> E_{\ell,n_\ell} - E_{\ell,0} = n_\ell\,\epsilon_\ell, \qquad \epsilon_\ell = \hbar\omega_\ell, \qquad \mathbf p_\ell = \hbar\mathbf k_\ell ,
> $$
>
> with $n_\ell \in \{0, 1, 2, \dots\}$ for bosons and $n_\ell \in \{0, 1\}$ for fermions ([[§C3.5 Many-Particle States#^pr-c3-5-1|Principle §C3.5.1]]). One quantum in mode $\ell$ is one particle in orbital $\ell$: a photon (electromagnetic field), a phonon (elastic waves), an atom or electron (matter waves). ($E_{\ell,0}$, the empty-mode or zero-point energy, e.g. $\tfrac12\hbar\omega_\ell$ for an oscillator mode, [[§B4.1 Ladder Operators and the Spectrum#^thm-b4-1-4|QM Theorem §B4.1.4]], is the same in every state and is dropped.)
>
> *Domain:* quantum input. Classically a mode's amplitude, and so its energy, is continuous; the integer $n_\ell$ is not a consequence of the wave equation.
>
> *Source: Mao §4.5.2, eqs. (4.98)–(4.99) and box "Wave–particle duality"*

^pr-c4b-1-2

> [!remark] Remark: Why a quantum of a wave counts as a particle
> Per added quantum, $\Delta E = \hbar\omega_\ell$ and $\Delta\mathbf p = \hbar\mathbf k_\ell$: the Einstein and de Broglie relations of one emitted or absorbed particle ([[§A1.2 The Photoelectric Effect#^pr-a1-2-3|QM Principle §A1.2.3]], [[§A3.1 De Broglie's Matter Waves#^pr-a3-1-1|QM Principle §A3.1.1]]); where it is found follows from $|\phi_\ell|^2 = 1/V$, uniform over the box ([[§A3.2 Wave–Particle Duality#^def-a3-2-2|QM Def. §A3.2.2]]).

^rem-c4b-1-2

> [!caution] Caution: Do not mix up which orbital with how many
> $\ell$ labels a state and $n_\ell$ counts particles in it. If $g_s$ internal states (spin, polarization) share the same dispersion, each spatial $\mathbf k$ carries $g_s$ distinct orbitals of equal energy, and $g_s$ appears as an overall factor in every count; otherwise each branch is counted separately.

^cau-c4b-1-1

> [!remark]- Connections
> - The many-body states $\{n_\ell\}$ are the Fock states of second quantization — [[§C12.2★ Second Quantization#^def-c12-2-1|QM Def. §C12.2.1]]; in QFT the quanta of the field are particles and one mode holds any number of them — [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-1|QFT Theorem §C2a.4.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|QFT Theorem §C2a.4.2]].
> - Statistics enters in the next step, one orbital at a time — [[§C4b.2 One Orbital in the Grand Ensemble|§C4b.2]].
