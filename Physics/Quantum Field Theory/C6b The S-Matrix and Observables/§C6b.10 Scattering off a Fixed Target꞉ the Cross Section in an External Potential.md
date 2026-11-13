---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.10
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.9 Evaluating the Cross Section]] · ↑ [[· C6b The S-Matrix and Observables]] · [[§C6c.1 Amplitudes from Correlation Functions]] →

*Sources: PHY 513, Problem Set 10 ("Scattering Processes"), Problem 2(b) (statement, Larsen; the user's solution, 2026-11-13) · Peskin & Schroeder, An Introduction to Quantum Field Theory, Problem 4.4(b), pp. 129–130; §4.5, pp. 102–106, eqs. (4.65)–(4.79) (the two-particle derivation that is adapted) · the homes cited in each box.*

The cross-section formula of [[§C6b.3 The Cross Section|§C6b.3]] and [[§C6b.9 Evaluating the Cross Section|§C6b.9]] is for two particles of the theory colliding: the target $A$ is a state, it recoils, and four-momentum is conserved. Problem Set 10, Problem 2 asks for the cross section in a different situation: one particle scattering off a fixed classical background field, "rather than off another particle". The target is then a given function $A(\mathbf x)$ in the Hamiltonian, not a particle. This section adapts the wave-packet derivation of [[§C6b.8 Wave Packets and the Cross Section|§C6b.8]]–[[§C6b.9 Evaluating the Cross Section|§C6b.9]] to it, as the user wrote it for Problem 2(b). What changes is stated in [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^mod-c6b-10-1|Model §C6b.10.1]]: energy is conserved and three-momentum is not, so the matrix element has one delta function instead of four, and the amplitude $\mathcal M$ is defined differently ([[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^def-c6b-10-1|Def. §C6b.10.1]]). The derivation has two steps that are results of their own, the two roots of the energy delta functions ([[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-2|Theorem §C6b.10.2]]) and the reflected packet ([[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^lem-c6b-10-3|Lemma §C6b.10.3]]); the cross section is [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-4|Theorem §C6b.10.4]], its flux factor is read in [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-5|Theorem §C6b.10.5]], and after the integral over the magnitude of the final momentum it becomes $d\sigma/d\Omega = |\mathcal M|^2/16\pi^2$ ([[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-6|Theorem §C6b.10.6]]). The formulas hold for any theory and any spin; the amplitude for an electron in a Coulomb field is computed in [[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula|§C8.10]].

**The mathematical picture.** A potential that depends on $\mathbf x$ and not on $t$ leaves, of the four translations, only the translations in time as symmetries. One conserved charge remains, the energy, where the collision of two particles has four ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]]). In momentum space the final states allowed by the one conservation law form the sphere $|\mathbf p_f| = |\mathbf p_i|$, a two-dimensional surface in the three-dimensional space of $\mathbf p_f$: one delta function removes one of the three integrals over $\mathbf p_f$, and a function of the direction, $d\sigma/d\Omega$, is left. For two particles in and two out, four delta functions remove four of six integrals, and again two angles are left.

![[ph-qft-c6b-10-1.svg]]
*ADDED figure (not from the problem set): (a) the wave packet, displaced by the impact parameter $\mathbf b$ from the axis through the fixed centre, is scattered into the solid angle $d\Omega$ at the angle $\theta$; (b) in momentum space the profile $\phi$ is concentrated near $\mathbf p_i$, the final momentum lies on the sphere $|\mathbf p_f| = |\mathbf p_i|$, and the reflected momentum $\tilde{\mathbf k} = (\mathbf k^\perp, -k^z)$, the second root of the energy delta function, lies near $-\mathbf p_i$, a distance $2|\mathbf p_i|$ from the packet ([[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^lem-c6b-10-3|Lemma §C6b.10.3]]).*

**Setup.** [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^mod-c6b-10-1|Model §C6b.10.1]]: one particle of mass $m$, a time-independent external potential, first order in the potential; free relativistic one-particle states $|\mathbf k\rangle$ over $|0\rangle$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]; a spin label is suppressed), wave packets as in [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-2|Def. §C6b.8.2]]. All statements are independent of how $\mathcal M$ is computed.

*Conventions* ([[Larsen PHY 513]]): beam along the $z$-axis through the centre of the potential; $\perp$ marks the components $(x, y)$; $E_{\mathbf k} = \sqrt{\mathbf k^2 + m^2}$; $E_i = E_{\mathbf p_i}$, $E_f = E_{\mathbf p_f}$; $v_i = |\mathbf p_i|/E_i$ is the speed of the incoming particle. The second, complex-conjugated copy of the packet integral has the variable $\mathbf k'$, as in the solution ([[§C6b.9 Evaluating the Cross Section|§C6b.9]] writes $\bar{\mathbf k}$); $\tilde{\mathbf k} \equiv (\mathbf k^\perp, -k^z)$ is $\mathbf k$ with its $z$ component reversed. The problem set's $\langle p'|iT|p\rangle$ is $\langle\mathbf p'|i\hat T|\mathbf p\rangle$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]]).

## The model and the amplitude

> [!model] Model §C6b.10.1: One Particle in a Time-Independent External Potential
> - *Hamiltonian:* $\hat H = \hat H_0 + \hat H_{\rm int}$ with $\hat H_{\rm int} = \int d^3x\,\hat{\mathcal O}(\mathbf x)\,A(\mathbf x)$, where $A(\mathbf x)$ is a given function, not an operator, independent of $t$, and $\hat{\mathcal O}$ is built from the fields of the scattered particle. Instance: $\hat H_I = \int d^3x\,e\,\hat{\bar\psi}\gamma^\mu\hat\psi\,A_\mu(\mathbf x)$ ([[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula#^mod-c8-10-1|Model §C8.10.1]]).
> - *Symmetry:* $\hat H$ does not depend on $t$, so time translations are a symmetry and the energy is conserved. $\hat H$ depends on $\mathbf x$ explicitly, through $A(\mathbf x)$, so space translations are not a symmetry and the three-momentum is not conserved ([[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-5|Theorem §C1b.7.5]], last sentence; [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-6|Theorem §C1b.7.6]]). The potential supplies any momentum $\mathbf q = \mathbf p_f - \mathbf p_i$ and no energy.
> - *Target:* a fixed classical source. It is not a particle of the theory: it has no state, no momentum and no recoil. In [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]] and [[§C6b.8 Wave Packets and the Cross Section#^mod-c6b-8-1|Model §C6b.8.1]] the target $A$ is a particle with a state $|\mathbf p_A\rangle$.
> - *Beam:* one particle in a wave packet ([[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-2|Def. §C6b.8.2]]) sharply peaked at $\mathbf p_i = |\mathbf p_i|\hat{\mathbf z}$, displaced by an impact parameter $\mathbf b \perp \hat{\mathbf z}$ from the axis through the centre of the potential ([[§C6b.8 Wave Packets and the Cross Section#^thm-c6b-8-3|Theorem §C6b.8.3]]); the particles of the beam arrive at uniform density in the transverse plane.
> - *Final states:* one particle of momentum $\mathbf p_f$, away from the forward direction.
> - *Applies:* first order in the potential, with free relativistic states over $|0\rangle$ in place of the in and out states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]); the packet is far from the region where the potential acts at early and late times. The vacuum value of $\hat H_{\rm int}$ is removed by normal ordering ([[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8-10-3|Theorem §C8.10.3]]).
>
> *Source: PHY 513, Problem Set 10, Problem 2 (statement: "an electron scattering off a fixed classical background field, rather than off another particle"; "Energy is then conserved but three-momentum is not") · PS Problem 4.4, p. 129 ("treat the field as a given, classical potential $A_\mu(x)$") · the list written here from the homes linked*

^mod-c6b-10-1

In the classification of [[§C6a.0 Setups and Observables|§C6a.0]] this is an external apparatus that acts for ever, as in ★ [[§C6a.0 Setups and Observables#^mod-c6a-0-2|Model §C6a.0.2]], but through a term bilinear in the fields instead of a linear one: it scatters a particle that is already there, where a linear source creates particles.

> [!definition] Definition §C6b.10.1: The Amplitude ℳ for a Time-Independent External Potential
> In [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^mod-c6b-10-1|Model §C6b.10.1]] the matrix element of $i\hat T$ between one-particle states is proportional to a delta function of the energy alone, and the **amplitude** $\mathcal M$ is defined by
>
> $$
> \langle\mathbf p'|i\hat T|\mathbf p\rangle = i\mathcal M\;2\pi\delta(E_f - E_i) , \qquad E_i = E_{\mathbf p} , \quad E_f = E_{\mathbf p'} .
> $$
>
> The delta function comes from the integral over time: at first order $\langle\mathbf p'|i\hat T|\mathbf p\rangle = -i\int dt\,e^{i(E_f - E_i)t}\,\langle\mathbf p'|\hat H_{\rm int}|\mathbf p\rangle$ with a time-independent $\hat H_{\rm int}$ (for a potential in one-particle quantum mechanics: [[§C6d.7 The Yukawa Potential#^thm-c6d-7-5|Theorem §C6d.7.5]], 1; for the Dirac field: [[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8-10-4|Theorem §C8.10.4]]). $\mathcal M = \mathcal M(p_f, p_i)$ depends on both momenta.
>
> *Model:* [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^mod-c6b-10-1|Model §C6b.10.1]]; *applies:* relativistically normalized one-particle states; a definition, at any order at which the element is proportional to $\delta(E_f - E_i)$.
>
> *Source: PHY 513, Problem Set 10, Problem 2(b) (statement: "we define $\mathcal M$ by $\langle p'|iT|p\rangle = i\mathcal M\,2\pi\delta(E_f - E_i)$") · PS Problem 4.4(b), p. 129 ("It is then natural to define $\langle p'|iT|p\rangle \equiv i\mathcal M\cdot(2\pi)\delta(E_f - E_i)$")*

^def-c6b-10-1

> [!caution] Caution: This ℳ is not the ℳ of two-particle scattering
> The amplitude of [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^def-c6b-10-1|Def. §C6b.10.1]] and the invariant amplitude of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]] carry the same letter and are different objects.
> 1. *Delta functions.* Here one, $2\pi\delta(E_f - E_i)$; there four, $(2\pi)^4\delta^4(p_A + p_B - \sum p_j)$.
> 2. *Mass dimension.* A relativistically normalized one-particle state has dimension $-1$ ($\langle\mathbf p|\mathbf p'\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf p')$ has dimension $1 - 3 = -2$), so $\langle\mathbf p'|i\hat T|\mathbf p\rangle$ has dimension $-2$; $\delta(E_f - E_i)$ has dimension $-1$; hence
>
> $$
> [\mathcal M] = -2 - (-1) = -1 \quad \text{here}, \qquad [\mathcal M] = 4 - N = 0 \quad \text{for } 2 \to 2
> $$
>
> ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|Theorem §C6b.1.5]]; dimensions of fields and couplings: [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]]). Check on the Coulomb amplitude of [[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8-10-8|Theorem §C8.10.8]]: $e\,\bar u'\gamma^0u\,Ze/|\mathbf q|^2$ has dimension $0 + 1 + 0 - 2 = -1$.
> 3. *Formula.* Each $\mathcal M$ goes with its own cross-section formula: $d\sigma/d\Omega = |\mathcal M|^2/16\pi^2$ here ([[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-6|Theorem §C6b.10.6]]), $|\mathcal M|^2/64\pi^2E_{\rm cm}^2$ for $2 \to 2$ with equal masses in the centre-of-mass frame ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-9|Theorem §C6b.4.9]]). Both right-hand sides have dimension $-2$.
>
> *Source: PHY 513, Problem Set 10, Problem 2(b) · the dimension count written here*

^cau-c6b-10-1

## Two steps of the derivation

> [!theorem] Theorem §C6b.10.2: The Two Energy Delta Functions and Their Two Roots
> Let $E_{\mathbf k} = \sqrt{|\mathbf k^\perp|^2 + (k^z)^2 + m^2}$ and let $\mathbf k'$ have the same transverse part as $\mathbf k$, $\mathbf k' = (\mathbf k^\perp, k'^z)$, with $k^z \ne 0$.
> 1. On the support of $\delta(E_f - E_{\mathbf k})$ the energy $E_f$ in a second delta function may be replaced by $E_{\mathbf k}$:
>
> $$
> \delta(E_f - E_{\mathbf k})\,\delta(E_f - E_{\mathbf k'}) = \delta(E_f - E_{\mathbf k})\,\delta(E_{\mathbf k} - E_{\mathbf k'})
> $$
>
> ([[§CA.2 Generalized Functions#^lem-ca-2-3|Lemma §CA.2.3]]).
> 2. As a function of $k'^z$, $E_{\mathbf k'}$ equals $E_{\mathbf k}$ at two roots, $k'^z = \pm k^z$, and at both $\bigl|\partial E_{\mathbf k'}/\partial k'^z\bigr| = |k^z|/E_{\mathbf k}$. Hence
>
> $$
> \delta(E_{\mathbf k} - E_{\mathbf k'}) = \frac{E_{\mathbf k}}{|k^z|}\Bigl[\delta(k'^z - k^z) + \delta(k'^z + k^z)\Bigr]
> $$
>
> ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2).
> 3. The factor is one over the $z$ component of the velocity, $E_{\mathbf k}/|k^z| = 1/|v^z|$. The first root is $\mathbf k' = \mathbf k$; the second is $\mathbf k' = \tilde{\mathbf k} \equiv (\mathbf k^\perp, -k^z)$, the momentum with its $z$ component reversed. Both have $E_{\mathbf k'} = E_{\mathbf k}$.
>
> *Model:* any (kinematics of one particle of mass $m \ge 0$); *applies:* identities of distributions, part 1 in the variables $(E_{\mathbf k}, E_{\mathbf k'})$, part 2 in $k'^z$ at fixed $\mathbf k$ with $k^z \ne 0$; independent of the dynamics.
>
> *Source: PHY 513, Problem Set 10, Problem 2(b1) (the user's solution, paragraph "Energy delta functions")*

^thm-c6b-10-2

> [!derivation]- Derivation
> As the user wrote it for Problem 2(b1).
>
> **Step 1** (part 1). Integrate both sides against a test function $f(E_{\mathbf k}, E_{\mathbf k'})$. The left side sets both arguments equal to $E_f$:
>
> $$
> \int dE_{\mathbf k}\,dE_{\mathbf k'}\;\delta(E_f - E_{\mathbf k})\,\delta(E_f - E_{\mathbf k'})\,f(E_{\mathbf k}, E_{\mathbf k'}) = f(E_f, E_f) .
> $$
>
> On the right side the second delta function sets $E_{\mathbf k'} = E_{\mathbf k}$ and the first then sets $E_{\mathbf k} = E_f$:
>
> $$
> \int dE_{\mathbf k}\,dE_{\mathbf k'}\;\delta(E_f - E_{\mathbf k})\,\delta(E_{\mathbf k} - E_{\mathbf k'})\,f(E_{\mathbf k}, E_{\mathbf k'}) = \int dE_{\mathbf k}\,\delta(E_f - E_{\mathbf k})\,f(E_{\mathbf k}, E_{\mathbf k}) = f(E_f, E_f) .
> $$
>
> Both sides give $f(E_f, E_f)$ for every $f$, so they are the same distribution.
>
> **Step 2** (the roots). Since $\mathbf k'^\perp = \mathbf k^\perp$,
>
> $$
> E_{\mathbf k'} = \sqrt{|\mathbf k^\perp|^2 + (k'^z)^2 + m^2} ,
> $$
>
> which depends on $k'^z$ only through $(k'^z)^2$. It equals $E_{\mathbf k} = \sqrt{|\mathbf k^\perp|^2 + (k^z)^2 + m^2}$ exactly when $(k'^z)^2 = (k^z)^2$: the two roots $k'^z = \pm k^z$.
>
> **Step 3** (the derivative at the roots).
>
> $$
> \frac{\partial E_{\mathbf k'}}{\partial k'^z} = \frac{k'^z}{\sqrt{|\mathbf k^\perp|^2 + (k'^z)^2 + m^2}} = \frac{k'^z}{E_{\mathbf k'}} , \qquad \Bigl|\frac{\partial E_{\mathbf k'}}{\partial k'^z}\Bigr|_{k'^z = \pm k^z} = \frac{|k^z|}{E_{\mathbf k}} .
> $$
>
> **Step 4** (part 2). With $g(k'^z) = E_{\mathbf k} - E_{\mathbf k'}$, whose zeros $\pm k^z$ are simple for $k^z \ne 0$, the rule $\delta(g(x)) = \sum_{x_0}\delta(x - x_0)/|g'(x_0)|$ ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2) gives
>
> $$
> \delta(E_{\mathbf k} - E_{\mathbf k'}) = \frac{\delta(k'^z - k^z)}{|k^z|/E_{\mathbf k}} + \frac{\delta(k'^z + k^z)}{|k^z|/E_{\mathbf k}} = \frac{E_{\mathbf k}}{|k^z|}\Bigl[\delta(k'^z - k^z) + \delta(k'^z + k^z)\Bigr] .
> $$
>
> **Step 5** (part 3). For a particle of mass $m$ and velocity $\mathbf v$, $\mathbf k = \gamma m\mathbf v$ and $E_{\mathbf k} = \gamma m$, so $k^z/E_{\mathbf k} = v^z$.
>
> **What the derivation shows.**
> - One delta function of the energy, one Jacobian: the factor $1/v$ of the cross section ([[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-5|Theorem §C6b.10.5]]).
> - The second root is not an artefact: the same energy is reached by the momentum reversed along the beam. Whether it contributes is decided by the packet → [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^lem-c6b-10-3|Lemma §C6b.10.3]].
> - At $k^z = 0$ the two roots merge and the zero is not simple; a beam has $k^z = |\mathbf p_i| \ne 0$.

^der-c6b-10-2

*Uses:* [[§CA.2 Generalized Functions#^lem-ca-2-3|Lemma §CA.2.3]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]]

> [!theorem] Lemma §C6b.10.3: The Reflected Packet Does Not Contribute
> Let the profile $\phi(\mathbf k)$ be sharply peaked around $\mathbf p_i = |\mathbf p_i|\hat{\mathbf z}$, with a momentum spread small compared with $|\mathbf p_i|$. Then $\phi(\mathbf k)$ is nonzero only near $\mathbf p_i$ and $\phi(\tilde{\mathbf k})$, $\tilde{\mathbf k} = (\mathbf k^\perp, -k^z)$, only near $(\mathbf p_i^\perp, -p_i^z)$, a distance $2|\mathbf p_i|$ away. The two have disjoint supports, so
>
> $$
> \phi(\mathbf k)\,\phi^\ast(\tilde{\mathbf k}) = 0 :
> $$
>
> the term of the second root of [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-2|Theorem §C6b.10.2]] vanishes.
>
> *Equivalently,* this is the one-particle form of [[§C6b.9 Evaluating the Cross Section#^lem-c6b-9-2|Lemma §C6b.9.2]]. There the two longitudinal constraints of two colliding packets have a second, "reflected" zero, with $A$ and $B$ exchanged in direction, and it is suppressed because $\phi_A^\ast(\bar{\mathbf k}_A) \approx 0$ away from the peak of $\phi_A$; here the second zero is the beam momentum reversed, and the same factor, the conjugated profile at a point far from its peak, removes it.
>
> *Model:* [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^mod-c6b-10-1|Model §C6b.10.1]]; *applies:* exactly for a profile that vanishes outside a ball of radius less than $|\mathbf p_i|$ around $\mathbf p_i$; for a profile with tails the product is small instead of zero (a Gaussian of width $\Delta k$: at most of relative size $e^{-|\mathbf p_i|^2/\Delta k^2}$).
>
> *Source: PHY 513, Problem Set 10, Problem 2(b1) (the user's solution, paragraph "Sharply peaked packet") · the comparison and the Gaussian bound written here*

^lem-c6b-10-3

> [!derivation]- Derivation
> **Step 1** (the supports). Let $\phi$ vanish outside the ball $|\mathbf k - \mathbf p_i| < \rho$ with $\rho < |\mathbf p_i|$. If $\phi(\mathbf k) \ne 0$, then $|k^z - p_i^z| < \rho$, so $k^z > |\mathbf p_i| - \rho > 0$. If $\phi(\tilde{\mathbf k}) \ne 0$, then $|{-k^z} - p_i^z| < \rho$, so $k^z < -|\mathbf p_i| + \rho < 0$. No $\mathbf k$ satisfies both, and the product vanishes for every $\mathbf k$.
>
> **Step 2** (a profile with tails; written here). For $\phi(\mathbf k) \propto e^{-|\mathbf k - \mathbf p_i|^2/2\Delta k^2}$,
>
> $$
> \phi(\mathbf k)\,\phi^\ast(\tilde{\mathbf k}) \propto e^{-[|\mathbf k^\perp|^2 + (k^z - p_i^z)^2]/2\Delta k^2}\;e^{-[|\mathbf k^\perp|^2 + (k^z + p_i^z)^2]/2\Delta k^2} = e^{-[|\mathbf k^\perp|^2 + (k^z)^2 + (p_i^z)^2]/\Delta k^2} \le e^{-|\mathbf p_i|^2/\Delta k^2} ,
> $$
>
> using $(k^z - p)^2 + (k^z + p)^2 = 2(k^z)^2 + 2p^2$. The product is exponentially small in $(|\mathbf p_i|/\Delta k)^2$.
>
> **What the derivation shows.**
> - "Sharply peaked" is used twice in the cross section: here, to remove the second root, and afterwards to evaluate the smooth factors at $\mathbf p_i$ ([[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-4|Theorem §C6b.10.4]], Step 9).

^der-c6b-10-3

*Uses:* [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-2|Theorem §C6b.10.2]], [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-2|Def. §C6b.8.2]]

## The cross section

> [!theorem] Theorem §C6b.10.4: The Cross Section off a Fixed Target
> In [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^mod-c6b-10-1|Model §C6b.10.1]]:
> 1. *The inputs.* The incoming state is the wave packet of [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-2|Def. §C6b.8.2]], displaced by the impact parameter $\mathbf b \perp \mathbf p_i$ ([[§C6b.8 Wave Packets and the Cross Section#^thm-c6b-8-3|Theorem §C6b.8.3]]),
>
> $$
> |\phi_{\mathbf b}\rangle = \int\frac{d^3k}{(2\pi)^3}\,\frac{\phi(\mathbf k)}{\sqrt{2E_{\mathbf k}}}\,e^{-i\mathbf b\cdot\mathbf k}\,|\mathbf k\rangle , \qquad \int\frac{d^3k}{(2\pi)^3}\,|\phi(\mathbf k)|^2 = 1 ,
> $$
>
> and the cross section is the scattering probability integrated over the impact parameter ([[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-4|Def. §C6b.8.4]], [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-5|Def. §C6b.8.5]]; PS (4.75)), the sum over final states being the integral over $\mathbf p_f$ with the one-particle measure ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]]):
>
> $$
> \sigma = \int d^2b\;\mathcal P(\mathbf b) , \qquad \mathcal P(\mathbf b) = \int\frac{d^3p_f}{(2\pi)^3}\,\frac{1}{2E_f}\;\bigl|\langle\mathbf p_f|i\hat T|\phi_{\mathbf b}\rangle\bigr|^2 .
> $$
>
> 2. *The result.* With $\mathcal M$ of [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^def-c6b-10-1|Def. §C6b.10.1]] and $v_i = |\mathbf p_i|/E_i$,
>
> $$
> d\sigma = \frac{1}{v_i}\,\frac{1}{2E_i}\,\frac{d^3p_f}{(2\pi)^3}\,\frac{1}{2E_f}\,|\mathcal M(p_i \to p_f)|^2\;2\pi\delta(E_f - E_i) .
> $$
>
> All dependence on the shape of the packet has disappeared.
>
> *Assumptions* (each used once in the derivation): (1) a packet sharply peaked around $\mathbf p_i = |\mathbf p_i|\hat{\mathbf z}$, with a spread small compared with $|\mathbf p_i|$ ([[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^lem-c6b-10-3|Lemma §C6b.10.3]]); (2) $\mathcal M(p_f, k)$, $E_{\mathbf k}$ and $k^z$ vary slowly on the scale of that spread; (3) a final direction away from the beam direction, so that only $i\hat T$ contributes ([[§C6b.8 Wave Packets and the Cross Section#^lem-c6b-8-5|Lemma §C6b.8.5]]: the term $\langle\mathbf p_f|\mathbf k\rangle$ of $\hat S$ is proportional to $\delta^3(\mathbf p_f - \mathbf k)$).
>
> *Model:* [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^mod-c6b-10-1|Model §C6b.10.1]]; *applies:* as there; any spin (for fixed spin states of the initial and the final particle; unpolarized: [[§C6b.3 The Cross Section#^def-c6b-3-5|Def. §C6b.3.5]] with one initial particle), any velocity.
>
> *Source: PHY 513, Problem Set 10, Problem 2(b1) (statement and the user's solution) · PS Problem 4.4(b), pp. 129–130 ("This formula is a natural modification of (4.79)"); §4.5, eqs. (4.65)–(4.79)*

^thm-c6b-10-4

> [!derivation]- Derivation
> As the user wrote it for Problem 2(b1): the derivation of [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-3|Theorem §C6b.9.3]] with one packet instead of two.
>
> **Step 1** (incoming state). There is a single incoming particle, described by a normalizable wave packet $\phi(\mathbf k)$ peaked around the beam momentum $\mathbf p_i$ and displaced by the impact parameter $\mathbf b \perp \mathbf p_i$: the state $|\phi_{\mathbf b}\rangle$ of part 1. The factor $1/\sqrt{2E_{\mathbf k}}$ compensates the relativistic normalization of $|\mathbf k\rangle$, so that $\langle\phi_{\mathbf b}|\phi_{\mathbf b}\rangle = 1$ ([[§C6b.8 Wave Packets and the Cross Section#^thm-c6b-8-2|Theorem §C6b.8.2]]; the phase drops out of the norm), and $e^{-i\mathbf b\cdot\mathbf k}$ translates the packet by $\mathbf b$ in the plane transverse to the beam ([[§C6b.8 Wave Packets and the Cross Section#^thm-c6b-8-3|Theorem §C6b.8.3]]).
>
> **Step 2** (cross section). As in PS (4.75), the cross section is the scattering probability integrated over the impact parameter, part 1. The final state is a single particle, so the sum over final states is the integral over $\mathbf p_f$ with the one-particle measure. Exchanging the order of the integrals, the contribution from final momenta in $d^3p_f$ around $\mathbf p_f$ is
>
> $$
> d\sigma = \frac{d^3p_f}{(2\pi)^3}\,\frac{1}{2E_f}\int d^2b\;\bigl|\langle\mathbf p_f|i\hat T|\phi_{\mathbf b}\rangle\bigr|^2 .
> $$
>
> **Step 3** (amplitude). Insert the wave packet and the definition of $\mathcal M$ ([[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^def-c6b-10-1|Def. §C6b.10.1]]), which depends on the momenta, $\mathcal M = \mathcal M(p_f, k)$:
>
> $$
> \langle\mathbf p_f|i\hat T|\phi_{\mathbf b}\rangle = \int\frac{d^3k}{(2\pi)^3}\,\frac{\phi(\mathbf k)}{\sqrt{2E_{\mathbf k}}}\,e^{-i\mathbf b\cdot\mathbf k}\,\langle\mathbf p_f|i\hat T|\mathbf k\rangle = \int\frac{d^3k}{(2\pi)^3}\,\frac{\phi(\mathbf k)}{\sqrt{2E_{\mathbf k}}}\,e^{-i\mathbf b\cdot\mathbf k}\;i\mathcal M(p_f, k)\,2\pi\delta(E_f - E_{\mathbf k}) .
> $$
>
> **Step 4** (the square). Its square is the integral times its complex conjugate, in which the integration variable is called $\mathbf k'$; $(i)(-i) = 1$:
>
> $$
> \bigl|\langle\mathbf p_f|i\hat T|\phi_{\mathbf b}\rangle\bigr|^2 = \int\frac{d^3k}{(2\pi)^3}\frac{d^3k'}{(2\pi)^3}\;\frac{\phi(\mathbf k)\,\phi^\ast(\mathbf k')}{\sqrt{2E_{\mathbf k}}\sqrt{2E_{\mathbf k'}}}\;e^{-i\mathbf b\cdot(\mathbf k - \mathbf k')}\;\mathcal M(p_f, k)\,\mathcal M^\ast(p_f, k')\;(2\pi)^2\,\delta(E_f - E_{\mathbf k})\,\delta(E_f - E_{\mathbf k'}) .
> $$
>
> **Step 5** (impact parameter integral). Take the beam along $z$, so $\mathbf b = (b^x, b^y, 0)$ and $\mathbf b\cdot(\mathbf k - \mathbf k') = b^x(k^x - k'^x) + b^y(k^y - k'^y)$. The only dependence on $\mathbf b$ is in the exponential, and ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]] in two dimensions)
>
> $$
> \int d^2b\;e^{-i\mathbf b\cdot(\mathbf k - \mathbf k')} = (2\pi)^2\,\delta(k^x - k'^x)\,\delta(k^y - k'^y) \equiv (2\pi)^2\,\delta^2(\mathbf k^\perp - \mathbf k'^\perp) .
> $$
>
> **Step 6** (the transverse $\mathbf k'$ integral). Writing $d^3k' = d^2k'^\perp\,dk'^z$, this delta function does the $\mathbf k'^\perp$ integral, its $(2\pi)^2$ cancelling that of $\frac{d^2k'^\perp}{(2\pi)^2}$, and sets $\mathbf k'^\perp = \mathbf k^\perp$:
>
> $$
> d\sigma = \frac{d^3p_f}{(2\pi)^3}\,\frac{1}{2E_f}\int\frac{d^3k}{(2\pi)^3}\int\frac{dk'^z}{2\pi}\;\frac{\phi(\mathbf k)\,\phi^\ast(\mathbf k')}{\sqrt{2E_{\mathbf k}}\sqrt{2E_{\mathbf k'}}}\;\mathcal M(p_f, k)\,\mathcal M^\ast(p_f, k')\;(2\pi)^2\,\delta(E_f - E_{\mathbf k})\,\delta(E_f - E_{\mathbf k'})\bigg|_{\mathbf k' = (\mathbf k^\perp,\,k'^z)} .
> $$
>
> **Step 7** (energy delta functions). On the support of $\delta(E_f - E_{\mathbf k})$ replace $E_f$ by $E_{\mathbf k}$ in the second factor, and resolve $\delta(E_{\mathbf k} - E_{\mathbf k'})$ in $k'^z$ ([[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-2|Theorem §C6b.10.2]], 1 and 2):
>
> $$
> \delta(E_f - E_{\mathbf k})\,\delta(E_f - E_{\mathbf k'}) = \delta(E_f - E_{\mathbf k})\,\delta(E_{\mathbf k} - E_{\mathbf k'}) , \qquad \delta(E_{\mathbf k} - E_{\mathbf k'}) = \frac{E_{\mathbf k}}{|k^z|}\Bigl[\delta(k'^z - k^z) + \delta(k'^z + k^z)\Bigr] .
> $$
>
> ⚑ By-product: two roots, one Jacobian → [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-2|Theorem §C6b.10.2]]. Inserted into $d\sigma$:
>
> $$
> d\sigma = \frac{d^3p_f}{(2\pi)^3}\,\frac{1}{2E_f}\int\frac{d^3k}{(2\pi)^3}\int\frac{dk'^z}{2\pi}\;\frac{\phi(\mathbf k)\,\phi^\ast(\mathbf k')}{\sqrt{2E_{\mathbf k}}\sqrt{2E_{\mathbf k'}}}\;\mathcal M(p_f, k)\,\mathcal M^\ast(p_f, k')\;(2\pi)^2\,\delta(E_f - E_{\mathbf k})\,\frac{E_{\mathbf k}}{|k^z|}\Bigl[\delta(k'^z - k^z) + \delta(k'^z + k^z)\Bigr]\bigg|_{\mathbf k' = (\mathbf k^\perp,\,k'^z)} .
> $$
>
> **Step 8** (the $k'^z$ integral). The delta functions do the $k'^z$ integral: the first root gives $\mathbf k' = \mathbf k$, and the second $\mathbf k' = \tilde{\mathbf k} \equiv (\mathbf k^\perp, -k^z)$, with the $z$ component flipped. Both have $E_{\mathbf k'} = E_{\mathbf k}$, so $\sqrt{2E_{\mathbf k}}\sqrt{2E_{\mathbf k'}} = 2E_{\mathbf k}$, and of $(2\pi)^2/2\pi$ one factor $2\pi$ is left:
>
> $$
> d\sigma = \frac{d^3p_f}{(2\pi)^3}\,\frac{1}{2E_f}\int\frac{d^3k}{(2\pi)^3}\;\frac{E_{\mathbf k}}{|k^z|}\,\frac{1}{2E_{\mathbf k}}\;\Bigl[\phi(\mathbf k)\phi^\ast(\mathbf k)\,\mathcal M(p_f, k)\,\mathcal M^\ast(p_f, k) + \phi(\mathbf k)\phi^\ast(\tilde{\mathbf k})\,\mathcal M(p_f, k)\,\mathcal M^\ast(p_f, \tilde k)\Bigr]\,2\pi\delta(E_f - E_{\mathbf k}) .
> $$
>
> **Step 9** (sharply peaked packet). The wave packet is taken sharply peaked around $\mathbf p_i = |\mathbf p_i|\hat{\mathbf z}$, with momentum spread small compared with $|\mathbf p_i|$ and with the scale over which $\mathcal M(p_f, k)$, $E_{\mathbf k}$ and $k^z$ vary. Then $\phi(\mathbf k)\phi^\ast(\tilde{\mathbf k}) = 0$ and the cross term vanishes (⚑ By-product → [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^lem-c6b-10-3|Lemma §C6b.10.3]]). In the remaining term $|\phi(\mathbf k)|^2$ acts as $(2\pi)^3\delta^3(\mathbf k - \mathbf p_i)$, consistent with $\int\frac{d^3k}{(2\pi)^3}|\phi(\mathbf k)|^2 = 1$, and evaluates the rest of the integrand at $\mathbf k = \mathbf p_i$ (the smoothness step of [[§C6b.9 Evaluating the Cross Section#^der-c6b-9-3|Derivation §C6b.9.3]], Steps 7–8, with its error $O((\Delta k)^2/K^2)$), where $E_{\mathbf k} = E_i$ and $|k^z|/E_{\mathbf k} = |\mathbf p_i|/E_i = v_i$:
>
> $$
> d\sigma = \frac{d^3p_f}{(2\pi)^3}\,\frac{1}{2E_f}\cdot\frac{1}{v_i}\cdot\frac{1}{2E_i}\cdot|\mathcal M(p_f, p_i)|^2\cdot2\pi\delta(E_f - E_i) = \frac{1}{v_i}\,\frac{1}{2E_i}\,\frac{d^3p_f}{(2\pi)^3}\,\frac{1}{2E_f}\,|\mathcal M|^2\,2\pi\delta(E_f - E_i) .
> $$
>
> The integrals are exchanged freely: the profile is smooth and rapidly decreasing, and every delta function is used against it ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-7|Theorem §CA.4.7]]).
>
> **What the derivation shows.**
> - Of the two energy delta functions of the squared amplitude, one is used up on the second copy of the packet and the other stays in $d\sigma$: no $\delta(0)$ appears, as in [[§C6b.9 Evaluating the Cross Section#^der-c6b-9-3|Derivation §C6b.9.3]].
> - Count of integrals: $2 + 3 + 3$ ($\mathbf b$, $\mathbf k$, $\mathbf k'$). The $\mathbf b$-integral gives two delta functions, which do $d^2k'^\perp$; one energy delta function does $dk'^z$; the three over $\mathbf k$ collapse by the normalization of the packet.
> - ⚑ By-product: the initial-state factor is $\frac{1}{v_i}\cdot\frac{1}{2E_i}$, one velocity and one energy → [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-5|Theorem §C6b.10.5]].

^der-c6b-10-4

*Uses:* [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-2|Def. §C6b.8.2]], [[§C6b.8 Wave Packets and the Cross Section#^thm-c6b-8-2|Theorem §C6b.8.2]], [[§C6b.8 Wave Packets and the Cross Section#^thm-c6b-8-3|Theorem §C6b.8.3]], [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-4|Def. §C6b.8.4]], [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-5|Def. §C6b.8.5]], [[§C6b.8 Wave Packets and the Cross Section#^lem-c6b-8-5|Lemma §C6b.8.5]], [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^def-c6b-10-1|Def. §C6b.10.1]], [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-2|Theorem §C6b.10.2]], [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^lem-c6b-10-3|Lemma §C6b.10.3]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-7|Theorem §CA.4.7]]

*Procedure:* [[P7 From ℳ to σ or Γ#^p7-6|P7, step 6]]

> [!theorem] Theorem §C6b.10.5: The Flux Factor of a Fixed Target Is One over a Single Velocity
> The factor of $d\sigma$ that belongs to the initial state is
>
> $$
> \frac{1}{v_i}\cdot\frac{1}{2E_i} \quad \text{(fixed target)} \qquad \text{against} \qquad \frac{1}{|\mathbf v_A - \mathbf v_B|}\cdot\frac{1}{2E_A\,2E_B} \quad \text{(two particles)} ,
> $$
>
> the first from [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-4|Theorem §C6b.10.4]], the second from [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-3|Theorem §C6b.9.3]].
>
> 1. $\frac{1}{2E_i}$ is the square of the factor $1/\sqrt{2E_{\mathbf k}}$ of the one packet. There is no $\frac{1}{2E}$ for the target: it is not a state and has no normalization.
> 2. $\frac{1}{v_i}$ is the Jacobian of one delta function of the energy in one longitudinal momentum, $|\partial E_{\mathbf k'}/\partial k'^z|^{-1} = E_{\mathbf k}/|k^z|$ ([[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-2|Theorem §C6b.10.2]]). For two particles the Jacobian of the two longitudinal constraints is $1/|\bar v_A^z - \bar v_B^z|$ ([[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-1|Theorem §C6b.9.1]]): there both momenta move, here only one does.
> 3. $v_i$ is the flux of one beam particle per unit volume, the role of $|\mathbf v_B|$ in the box route for a target at rest ([[§C6b.3 The Cross Section#^def-c6b-3-1|Def. §C6b.3.1]], [[§C6b.3 The Cross Section#^thm-c6b-3-4|Theorem §C6b.3.4]]).
>
> *Proof:* parts 1 and 2 are Steps 8–9 and Step 7 of [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^der-c6b-10-4|Derivation §C6b.10.4]], read against Step 6 and Step 4 of [[§C6b.9 Evaluating the Cross Section#^der-c6b-9-3|Derivation §C6b.9.3]]; part 3 is [[§C6b.3 The Cross Section#^def-c6b-3-1|Def. §C6b.3.1]] with density one per unit volume, $j = v_i$.
>
> *Model:* [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^mod-c6b-10-1|Model §C6b.10.1]] against [[§C6b.8 Wave Packets and the Cross Section#^mod-c6b-8-1|Model §C6b.8.1]]; *applies:* as the two theorems compared.
>
> *Source: PHY 513, Problem Set 10, Problem 2(b1) (the user's solution, last step: "$|k^z|/E_{\mathbf k} = |\mathbf p_i|/E_i = v_i$") · the comparison written here*

^thm-c6b-10-5

## The differential cross section

> [!theorem] Theorem §C6b.10.6: The Differential Cross Section off a Fixed Target
> Integrating [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-4|Theorem §C6b.10.4]] over the magnitude of $\mathbf p_f$,
>
> $$
> \frac{d\sigma}{d\Omega} = \frac{1}{16\pi^2}\,|\mathcal M|^2 , \qquad |\mathbf p_f| = |\mathbf p_i| ,
> $$
>
> with $d\Omega$ the solid angle around the direction of $\mathbf p_f$ and $\mathcal M$ of [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^def-c6b-10-1|Def. §C6b.10.1]] evaluated at $E_f = E_i$. Only the exact relation $v_i = |\mathbf p_i|/E_i$ is used, so the formula holds for relativistic particles.
>
> *Model:* [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^mod-c6b-10-1|Model §C6b.10.1]]; *applies:* as [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-4|Theorem §C6b.10.4]]; any velocity; the final particle has the mass of the initial one.
>
> *Source: PHY 513, Problem Set 10, Problem 2(b2) (statement: "This expression holds also for relativistic electrons"; the user's solution) · PS Problem 4.4(b), p. 130 ("Integrate over $|p_f|$ to find a simple expression for $d\sigma/d\Omega$")*

^thm-c6b-10-6

> [!derivation]- Derivation
> As the user wrote it for Problem 2(b2).
>
> **Step 1** (spherical coordinates). Let $\rho_f \equiv |\mathbf p_f|$. In spherical coordinates in momentum space,
>
> $$
> d^3p_f = \rho_f^2\,d\rho_f\,d\Omega ,
> $$
>
> where $d\Omega$ is the solid angle around the direction of $\mathbf p_f$, and $E_f = \sqrt{\rho_f^2 + m^2}$ depends only on $\rho_f$.
>
> **Step 2** (the delta function). As a function of $\rho_f \ge 0$, $E_f - E_i$ vanishes only at $\rho_0 = |\mathbf p_i|$, where
>
> $$
> \frac{dE_f}{d\rho_f}\bigg|_{\rho_0} = \frac{\rho_0}{E_i} = \frac{|\mathbf p_i|}{E_i} = v_i ,
> $$
>
> so by $\delta(g(\rho)) = \delta(\rho - \rho_0)/|g'(\rho_0)|$ ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2),
>
> $$
> \delta(E_f - E_i) = \frac{1}{v_i}\,\delta\bigl(\rho_f - |\mathbf p_i|\bigr) .
> $$
>
> **Step 3** (insert). Into the result of [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-4|Theorem §C6b.10.4]]:
>
> $$
> d\sigma = \frac{1}{v_i}\,\frac{1}{2E_i}\,\frac{\rho_f^2\,d\rho_f\,d\Omega}{(2\pi)^3}\,\frac{1}{2E_f}\,|\mathcal M|^2\;\frac{2\pi}{v_i}\,\delta\bigl(\rho_f - |\mathbf p_i|\bigr) .
> $$
>
> **Step 4** (the $\rho_f$ integral). The delta function sets $\rho_f = |\mathbf p_i|$, so $E_f = \sqrt{|\mathbf p_i|^2 + m^2} = E_i$, and the $\rho_f$ integral leaves
>
> $$
> \frac{d\sigma}{d\Omega} = \frac{1}{v_i^2}\,\frac{1}{2E_i}\,\frac{|\mathbf p_i|^2}{(2\pi)^3}\,\frac{1}{2E_i}\,2\pi\,|\mathcal M|^2 = \frac{|\mathbf p_i|^2}{v_i^2E_i^2}\,\frac{|\mathcal M|^2}{16\pi^2} ,
> $$
>
> with $\frac{2\pi}{4\,(2\pi)^3} = \frac{1}{16\pi^2}$.
>
> **Step 5** (the velocity). For a particle of mass $m$ and speed $v$, $|\mathbf p| = \gamma mv$ and $E = \gamma m$, so $v_iE_i = |\mathbf p_i|$ and
>
> $$
> \frac{d\sigma}{d\Omega} = \frac{1}{16\pi^2}\,|\mathcal M|^2 .
> $$
>
> Only the exact relation $v_i = |\mathbf p_i|/E_i$ was used, so this holds for relativistic particles.
>
> **What the derivation shows.**
> - The velocity appears twice, once from the flux ([[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-5|Theorem §C6b.10.5]]) and once from the density of final states $d\rho_f/dE_f = 1/v_i$; with the two factors $\frac{1}{2E}$ and $\rho_f^2 = |\mathbf p_i|^2$ they cancel exactly: no kinematic factor is left in front of $|\mathcal M|^2$.
> - The energy shell is the sphere $|\mathbf p_f| = |\mathbf p_i|$: the scattering is elastic, whatever the potential.

^der-c6b-10-6

*Uses:* [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-4|Theorem §C6b.10.4]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]]

*Procedure:* [[P7 From ℳ to σ or Γ#^p7-6|P7, step 6]]

> [!remark] Remark: Next to the two-particle formula
> For two particles of equal masses in the centre-of-mass frame the corresponding formula is $\frac{d\sigma}{d\Omega} = \frac{|\mathcal M|^2}{64\pi^2E_{\rm cm}^2}$ ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-9|Theorem §C6b.4.9]]). The two formulas contain different amplitudes: the $\mathcal M$ of [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^def-c6b-10-1|Def. §C6b.10.1]] has dimension $-1$ and no kinematic factor is needed to make an area of $|\mathcal M|^2$; the invariant amplitude of $2 \to 2$ scattering is dimensionless and $E_{\rm cm}^{-2}$ supplies the area ([[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^cau-c6b-10-1|§C6b.10, Caution: This ℳ is not the ℳ of two-particle scattering]]; [[§C6b.4 Two-Body Scattering Kinematics#^rem-c6b-4-3|§C6b.4, Remark: Why 1/E²: dimensional analysis]]).
>
> *Source: PHY 513, Problem Set 10, Problem 2(b2) · comparison written here*

^rem-c6b-10-1

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]] — $\delta(g(x)) = \sum_{x_0}\delta(x - x_0)/|g'(x_0)|$ over the simple zeros: the two roots $k'^z = \pm k^z$ with the Jacobian $E_{\mathbf k}/|k^z|$ ([[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-2|Theorem §C6b.10.2]]), and $\delta(E_f - E_i) = \delta(\rho_f - |\mathbf p_i|)/v_i$ (Derivation §C6b.10.6, Step 2).
> - [[§CA.2 Generalized Functions#^lem-ca-2-3|Lemma §CA.2.3]] — on the support of one delta function its argument may be substituted into a second one: $\delta(E_f - E_{\mathbf k})\delta(E_f - E_{\mathbf k'}) = \delta(E_f - E_{\mathbf k})\delta(E_{\mathbf k} - E_{\mathbf k'})$.
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]] — plane waves integrate to a delta function, in two dimensions: $\int d^2b\,e^{-i\mathbf b\cdot(\mathbf k - \mathbf k')} = (2\pi)^2\delta^2(\mathbf k^\perp - \mathbf k'^\perp)$ (Derivation §C6b.10.4, Step 5).
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-7|Theorem §CA.4.7]] — the order of the eight integrals may be exchanged, every delta function being used against the smooth, rapidly decreasing profile.

> [!remark]- Connections
> - The classical cross section is defined for exactly this situation, a beam on a fixed centre of force, and is an area in the plane of impact parameters; here the same area is an integral of probabilities — [[§B4.2 Scattering Cross-Sections and Rutherford Scattering#^def-b4-2-1|CM Def. §B4.2.1]], [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-1|Def. §C6b.8.1]].
> - One-particle quantum mechanics treats the same situation with a transition rate divided by a probability current, and its first Born approximation is the first-order element of this section — [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^def-c10-1-1|QM Def. §C10.1.1]], [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-6|QM Theorem §C10.1.6]], [[§C6d.7 The Yukawa Potential#^thm-c6d-7-5|Theorem §C6d.7.5]].
> - A fixed potential "absorbs any momentum": the three momentum delta functions of two-particle scattering are the recoil of the target, absent here — [[§C6d.7 The Yukawa Potential#^thm-c6d-7-5|Theorem §C6d.7.5]], 2, [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]].
> - An external source that is linear in the field creates particles instead of scattering them, and also supplies momentum at its vertex — [[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]], [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^def-c6c-7-1|Def. §C6c.7.1]].
> - The amplitude for an electron in an external electromagnetic potential, the Coulomb field and the Rutherford and Mott formulas — [[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula|§C8.10]], [[§C8.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field|§C8.11]].
