---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C1a
section: C1a.7
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C1a.6 Infinitesimal Lorentz Transformations and Generators]] · ↑ [[· C1a Preliminaries]] · [[§C1b.1 Fields and Their Transformation Laws]] →

*Sources: the user's PHY 513 notes, Ch. 1 §1.7; Ch. 3 §3.3 (Derivation "The Euler–Lagrange equation for other kinds of field", vector field) · PHY 513 Lecture 1 (Larsen), Part C ("Example: Relativistic Electrodynamics"); Problem Set 2, Problem 4 (statement), as recorded in the user's notes · Yu Zhao-Huan, 量子场论讲义, §1.5, eqs. (1.122)–(1.151) · the user's pre-course notes, §1.2 ("Rationalized natural units").*

How do electric and magnetic fields look in the language of field theory, and what about electrodynamics is the template for every field to come? The field tensor, its transformation, the two invariants, the four-current and Maxwell's equations as tensor equations are at home in Relativity level B, in SI units with $c$ explicit ([[§B4.2 The Electromagnetic Field Tensor|REL §B4.2]]; the coupling to a charge, [[§B3.2 The Charged Particle|REL §B3.2]]; the equations themselves, [[§B8.4 Maxwell's Equations#^pr-b8-4-2|EM Principle §B8.4.2]]). Theorem §C1a.7.1 and the first half of Theorem §C1a.7.2 are [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-7|REL Theorem §B4.2.7]] and [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-3|REL Theorem §B4.2.3]] transcribed to Heaviside–Lorentz units with $c = 1$; their computations are repeated only as the index template of field theory. What this section adds is what quantum field theory needs: Heaviside–Lorentz natural units and their dictionary to SI, the field tensor and Maxwell's equations in those units, the dual and the invariants with $\varepsilon^{0123} = +1$ against Peskin–Schroeder, the self-dual combinations $\mathbf E \pm i\mathbf B$, the lecture's boost example done consistently, and the lessons the example teaches for field theory.

## Units and the field tensor

> [!definition] Definition §C1a.7.1: Heaviside–Lorentz Natural Units
> Electromagnetic quantities in field theory are measured in **Heaviside–Lorentz** (rationalized) units, $\varepsilon_0 = \mu_0 = 1$, together with $\hbar = c = 1$ ([[§C1a.2 Natural Units and Dimensional Analysis#^def-c1a-2-1|Def. §C1a.2.1]]). Maxwell's equations and the force law then read
>
> $$
> \nabla\cdot\mathbf E = \rho, \quad \nabla\cdot\mathbf B = 0, \quad \nabla\times\mathbf E = -\partial_t\mathbf B, \quad \nabla\times\mathbf B = \mathbf J + \partial_t\mathbf E, \qquad \mathbf F = q(\mathbf E + \mathbf v\times\mathbf B),
> $$
>
> with no $4\pi$ in the field equations; it appears instead in Coulomb's law, $\Phi = Q/4\pi r$, and in the fine-structure constant, $\alpha = e^2/4\pi \approx 1/137.036$, so $e = \sqrt{4\pi\alpha} \approx 0.303$.
>
> *Source: the user's pre-course notes, §1.2 ("Rationalized natural units") · [[Larsen PHY 513]] (units row) · the user's PHY 513 notes, Ch. 1 §1.7 ("in Heaviside–Lorentz units")*

^def-c1a-7-1

How SI and Gaussian formulas turn into these, and back, is [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-4|Theorem §C1a.7.4]] at the end of this note.

> [!definition] Definition §C1a.7.2: Four-Potential and Field Tensor in Natural Units
> With $A^\mu = (\Phi, \mathbf A)$, $\mathbf E = -\nabla\Phi - \partial_t\mathbf A$, $\mathbf B = \nabla\times\mathbf A$ (Heaviside–Lorentz, $c = 1$),
>
> $$
> F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu, \qquad F^{0i} = -E^i, \quad F^{ij} = -\varepsilon_{ijk}B^k; \qquad F_{0i} = E^i, \quad F_{ij} = -\varepsilon_{ijk}B^k,
> $$
>
> $$
> F_{\mu\nu} = \begin{pmatrix} 0 & E_x & E_y & E_z \\ -E_x & 0 & -B_z & B_y \\ -E_y & B_z & 0 & -B_x \\ -E_z & -B_y & B_x & 0 \end{pmatrix}, \qquad E^i = F^{i0}, \quad B^i = -\tfrac12\varepsilon_{ijk}F^{jk} .
> $$
>
> $F$ is unchanged by the gauge transformation $A^\mu \to A^\mu + \partial^\mu\lambda$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.7, eqs. (Fmunu), (Fupper), (FfromA) · PHY 513 Lecture 1, Part C (Jackson §11.10) · PHY 513, Problem Set 2, Problem 4(b) (identification $E_i = -F^{0i}$, $\varepsilon_{ijk}B_k = -F^{ij}$) · Yu §1.5, eqs. (1.124)–(1.132), (1.139)*

^def-c1a-7-2

The components, their raising and lowering, gauge invariance and the matrix are [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-1|REL Theorem §B4.2.1]] with $c = 1$ and the SI fields replaced by Heaviside–Lorentz ones; with Theorem §C1a.7.4 one finds $F_{\rm REL}^{\mu\nu} = \sqrt{\mu_0}\,F^{\mu\nu}$ (and $c$ restored). Raising both indices flips the sign of the time–space entries only, so $\mathbf E$ (in the time–space entries) changes sign between $F_{\mu\nu}$ and $F^{\mu\nu}$ and $\mathbf B$ (in the space–space entries) does not. The convention dependence of every sign traces to one source, the sign in $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$. Under a Lorentz transformation $F_{\mu\nu} \to \Lambda_\mu{}^\lambda\Lambda_\nu{}^\sigma F_{\lambda\sigma}$, the general law ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]]; explicit fields, [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-2|REL Theorem §B4.2.2]]). $F$ is not a product of two vectors ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-4|§C1a.5, Caution: A tensor is not a product of vectors]]).

> [!caution] Caution: Conventions for F across the sources
> The matrix above is the lecture's (Jackson's, in Peskin–Schroeder's conventions) and Yu's (1.132), and agrees with Relativity level B after $c = 1$ and the SI-to-HL rescaling. Griffiths' $F^{\mu\nu}$ has the opposite overall sign (mostly-plus metric), as [[§B4.2 The Electromagnetic Field Tensor#^cau-b4-2-1|REL Caution: Sign conventions for the field tensor]] records. Anything with one $\varepsilon$, the dual $\tilde F$ and $\mathbf E\cdot\mathbf B$ terms, has the opposite sign in Peskin–Schroeder, whose $\varepsilon^{0123} = -1$ ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]).
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.7 (after eq. (Finvariants); Derivation "Maxwell's equations in covariant form", dual) · Yu §1.5, eq. (1.132)*

^cau-c1a-7-1

## Maxwell's equations, duality and the invariants

> [!theorem] Theorem §C1a.7.1: Maxwell's Equations in Heaviside–Lorentz Form
> With the four-current $J^\mu = (\rho, \mathbf J)$ and $\tilde F^{\mu\nu} = \frac12\varepsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}$, Maxwell's equations are
>
> $$
> \partial_\mu F^{\mu\nu} = J^\nu, \qquad \partial_\mu\tilde F^{\mu\nu} = 0 \quad\Longleftrightarrow\quad \partial^\rho F^{\mu\nu} + \partial^\mu F^{\nu\rho} + \partial^\nu F^{\rho\mu} = 0 \ \ \text{(Bianchi identity)} .
> $$
>
> The first contains Gauss ($\nu = 0$) and Ampère–Maxwell ($\nu = j$); the second holds identically when $F$ comes from a potential. Consistency of the first requires $\partial_\nu J^\nu = 0$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.7 (Derivation "Maxwell's equations in covariant form"), eq. (Maxwell) · Yu §1.5, eqs. (1.123), (1.128), (1.137), (1.151)*

^thm-c1a-7-1

> [!derivation]- Derivation
> *This is the derivation of [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-7|REL Theorem §B4.2.7]] translated by the dictionary of Theorem §C1a.7.4 ($F_{\rm REL} = \sqrt{\mu_0}F$, $c = 1$), written out once more as the worked instance of the index moves of the Remark below.*
>
> **1. Split the contracted index (no signs).** $\partial_\mu F^{\mu\nu} = \partial_0F^{0\nu} + \partial_iF^{i\nu}$, a plain sum ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-1|§C1a.5, Caution: A contraction is a plain sum]]); $\partial_i = \partial/\partial x^i$ has no sign.
>
> **2. $\nu = 0$.** $F^{00} = 0$, and antisymmetry gives $F^{i0} = -F^{0i} = E^i$: $\partial_\mu F^{\mu0} = \partial_iE^i = \nabla\cdot\mathbf E$. Setting it equal to $J^0 = \rho$ is Gauss's law.
>
> **3. $\nu = j$.** $\partial_0F^{0j} = -\partial_tE^j$. And $\partial_iF^{ij} = -\varepsilon_{ijk}\partial_iB^k$; put the free index $j$ in the first slot of $\varepsilon$, one transposition: $-\varepsilon_{ijk} = \varepsilon_{jik}$, so $\partial_iF^{ij} = \varepsilon_{jik}\partial_iB^k = (\nabla\times\mathbf B)^j$. Setting $-\partial_tE^j + (\nabla\times\mathbf B)^j = J^j$ is Ampère–Maxwell.
>
> **4. The dual vanishes identically.** With $F_{\rho\sigma} = \partial_\rho A_\sigma - \partial_\sigma A_\rho$,
>
> $$
> \partial_\mu\tilde F^{\mu\nu} = \tfrac12\varepsilon^{\mu\nu\rho\sigma}\bigl(\partial_\mu\partial_\rho A_\sigma - \partial_\mu\partial_\sigma A_\rho\bigr) = 0 ,
> $$
>
> each term being the symmetric $\partial_\mu\partial_\rho$ (resp. $\partial_\mu\partial_\sigma$, equal mixed partials, [[§6 Equality of Mixed Partials#^thm-6-1|452 Thm. §6.1]]) contracted with the antisymmetric $\varepsilon$ ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]], 2).
>
> **5. Equivalence with the cyclic form.** The cyclic sum $C^{\rho\mu\nu} = \partial^\rho F^{\mu\nu} + \partial^\mu F^{\nu\rho} + \partial^\nu F^{\rho\mu}$ is totally antisymmetric (exchanging two indices permutes its terms and flips each $F$), so it has four independent components, one for each omitted index; and $\varepsilon_{\kappa\rho\mu\nu}C^{\rho\mu\nu} = 3\,\varepsilon_{\kappa\rho\mu\nu}\partial^\rho F^{\mu\nu} = 6\,\partial^\rho\tilde F_{\kappa\rho}$, each of the three terms giving the same contraction after cyclic relabelling (an even permutation). Conversely $C$ is recovered from its four $\varepsilon$-contractions (Theorem §C1a.5.4, part 1). So the four equations $\partial_\mu\tilde F^{\mu\nu} = 0$ are the four independent cyclic identities; their components are $\nabla\cdot\mathbf B = 0$ ($ijk$) and Faraday's law (one time index), as in [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-7|REL Theorem §B4.2.7]] with $c = 1$.
>
> **6. Current conservation.** Apply $\partial_\nu$ to the first equation: $\partial_\nu\partial_\mu F^{\mu\nu} = 0$, symmetric times antisymmetric. So $\partial_\nu J^\nu = \partial_t\rho + \nabla\cdot\mathbf J = 0$ ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-7|§C1a.5, Caution: The Hessian is not the wave operator]]).
>
> **What the derivation shows**
> - Charge conservation is not an extra law but a consistency condition of Maxwell's equations; in a Lagrangian theory it is also the condition for the coupling $-J^\mu A_\mu$ to be gauge invariant (Remark below).
> - The two halves have different origins: the Bianchi identity is geometry (an identity for any $F$ from a potential), the inhomogeneous equation is dynamics. Both sides of each are tensors of one type, so the equations hold in every frame without any transformation of $\mathbf E$ and $\mathbf B$ ([[§B2.2 Tensors and the Covariance Principle#^pr-b2-2-9|REL Principle §B2.2.9]]).
> - Used next: the Maxwell Lagrangian (Remark below), the energy–momentum tensor of the field ([[§C1b.6 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^ex-c1b-6-3|Example §C1b.6.3]]).

^der-c1a-7-1

*Uses:* [[§C1a.7 Relativistic Electrodynamics in Index Form#^def-c1a-7-2|Def. §C1a.7.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-1|§C1a.5, Caution: A contraction is a plain sum; the signs live in the components]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]], [[§6 Equality of Mixed Partials#^thm-6-1|452 Thm. §6.1]], [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-7|REL Theorem §B4.2.7]]

> [!theorem] Theorem §C1a.7.2: Duality Exchanges E and B; the Two Invariants
> With $\varepsilon^{0123} = +1$:
> 1. $\tilde F^{0i} = -B^i$, $\tilde F^{ij} = \varepsilon_{ijk}E^k$: the dual is $F$ with $\mathbf E \to \mathbf B$, $\mathbf B \to -\mathbf E$, and $\tilde{\tilde F} = -F$.
> 2. The invariants are
>
> $$
> F_{\mu\nu}F^{\mu\nu} = 2(\mathbf B^2 - \mathbf E^2), \qquad F_{\mu\nu}\tilde F^{\mu\nu} = -4\,\mathbf E\cdot\mathbf B, \qquad \varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} = -8\,\mathbf E\cdot\mathbf B, \qquad \tilde F_{\mu\nu}\tilde F^{\mu\nu} = -F_{\mu\nu}F^{\mu\nu} :
> $$
>
> a scalar and a pseudoscalar. In Peskin–Schroeder's convention the pseudoscalar is $+8\,\mathbf E\cdot\mathbf B$; the scalar does not change.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.7, eq. (Finvariants); Derivation "Maxwell's equations in covariant form" (dual components); Ch. 1 §1.5 (Derivation "Contracting Levi-Civita symbols", four-dimensional example) · Yu §1.5, eqs. (1.146)–(1.149)*

^thm-c1a-7-2

> [!derivation]- Derivation
> *Steps 1–4 are the computations of [[§B4.2 The Electromagnetic Field Tensor#^def-b4-2-3|REL Def. §B4.2.3]] and [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-3|REL Theorem §B4.2.3]] with $c = 1$; steps 5–6 are new here.*
>
> **1. $\tilde F^{0i}$.** In $\frac12\varepsilon^{0i\rho\sigma}F_{\rho\sigma}$ only spatial $\rho\sigma = jk$ contribute, and $\varepsilon^{0ijk} = \varepsilon_{ijk}$ (the three-dimensional symbol, $\varepsilon_{123} = 1$; [[§B2.2 Tensors and the Covariance Principle#^def-b2-2-2|REL Def. §B2.2.2]]). With $F_{jk} = -\varepsilon_{jkl}B^l$ and $\varepsilon_{ijk}\varepsilon_{jkl} = \varepsilon_{ijk}\varepsilon_{ljk} = 2\delta_{il}$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], 2): $\tilde F^{0i} = \frac12\varepsilon_{ijk}(-\varepsilon_{jkl}B^l) = -B^i$.
>
> **2. $\tilde F^{ij}$.** Exactly one of $\rho, \sigma$ is $0$: $\tilde F^{ij} = \frac12(\varepsilon^{ij0k}F_{0k} + \varepsilon^{ijk0}F_{k0}) = \varepsilon^{ij0k}F_{0k}$, using $\varepsilon^{ijk0}F_{k0} = (-\varepsilon^{ij0k})(-F_{0k})$. Moving $0$ to the front takes two transpositions: $\varepsilon^{ij0k} = \varepsilon^{0ijk} = \varepsilon_{ijk}$. With $F_{0k} = E^k$: $\tilde F^{ij} = \varepsilon_{ijk}E^k$. Comparing with $F^{0i} = -E^i$, $F^{ij} = -\varepsilon_{ijk}B^k$: $\tilde F$ is $F$ with $\mathbf E \to \mathbf B$ and $\mathbf B \to -\mathbf E$. Applying the substitution twice gives $\mathbf E \to -\mathbf E$, $\mathbf B \to -\mathbf B$: $\tilde{\tilde F} = -F$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]], 1).
>
> **3. $F_{\mu\nu}F^{\mu\nu}$.** Split into time–space and space–space terms, the former appearing twice ($0i$ and $i0$): $2F_{0i}F^{0i} + F_{ij}F^{ij} = 2E^i(-E^i) + \varepsilon_{ijk}\varepsilon_{ijl}B^kB^l = -2\mathbf E^2 + 2\mathbf B^2$, using $\varepsilon_{ijk}\varepsilon_{ijl} = 2\delta_{kl}$; the $ij$ sum counts each magnetic component twice.
>
> **4. $F_{\mu\nu}\tilde F^{\mu\nu}$.** Same split: $2F_{0i}\tilde F^{0i} + F_{ij}\tilde F^{ij} = 2E^i(-B^i) + (-\varepsilon_{ijk}B^k)(\varepsilon_{ijl}E^l) = -2\mathbf E\cdot\mathbf B - 2\mathbf E\cdot\mathbf B = -4\,\mathbf E\cdot\mathbf B$. Since $F_{\mu\nu}\tilde F^{\mu\nu} = \frac12\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$, the $\varepsilon$-contraction is $-8\,\mathbf E\cdot\mathbf B$. (Directly: $\varepsilon$ kills any term with two time indices, so exactly one of the pairs $\mu\nu$, $\rho\sigma$ contains a $0$; the four placements give $4\varepsilon^{0ijk}F_{0i}F_{jk} = 4\varepsilon_{ijk}E^i(-\varepsilon_{jkl}B^l) = -8\,\mathbf E\cdot\mathbf B$.)
>
> **5. $\tilde F_{\mu\nu}\tilde F^{\mu\nu}$.** By step 2, $\tilde F$ is $F$ with $(\mathbf E, \mathbf B) \to (\mathbf B, -\mathbf E)$, so by step 3 $\tilde F\tilde F = 2(\mathbf E^2 - \mathbf B^2) = -FF$. (Index route: $\frac14\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu\alpha\beta}F^{\rho\sigma}F_{\alpha\beta} = -\frac12(F^{\rho\sigma}F_{\rho\sigma} - F^{\rho\sigma}F_{\sigma\rho}) = -F^{\rho\sigma}F_{\rho\sigma}$ by Theorem §C1a.5.4.)
>
> **6. Convention.** Each $\varepsilon$ flips sign with $\varepsilon^{0123} \to -1$ ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]); $FF$ and $\tilde F\tilde F$ contain two or none.
>
> **What the derivation shows**
> - The scalar is the Maxwell Lagrangian up to $-\frac14$: $-\frac14F_{\mu\nu}F^{\mu\nu} = \frac12(\mathbf E^2 - \mathbf B^2)$, kinetic minus potential.
> - The pseudoscalar $\mathbf E\cdot\mathbf B$ is odd under $P$ (polar $\mathbf E$, axial $\mathbf B$) and a total derivative, $\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} = 4\partial_\mu(\varepsilon^{\mu\nu\rho\sigma}A_\nu\partial_\rho A_\sigma)$ (by step 4 of the derivation of Theorem §C1a.7.1), so it does not change the field equations ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|Theorem §C1b.2.5]]).
> - The invariant classes of fields (purely electric or magnetic frames, null fields) follow from these two numbers ([[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-4|REL Theorem §B4.2.4]]).

^der-c1a-7-2

*Uses:* [[§C1a.7 Relativistic Electrodynamics in Index Form#^def-c1a-7-2|Def. §C1a.7.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]], [[§B2.2 Tensors and the Covariance Principle#^def-b2-2-2|REL Def. §B2.2.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]

> [!theorem] Theorem §C1a.7.3: E ± iB: the Self-Dual Halves of F
> 1. $F + i\tilde F$ and $F - i\tilde F$ are eigenvectors of duality with eigenvalues $-i$ and $+i$, and are fixed by the complex three-vectors $\mathbf E + i\mathbf B$ and $\mathbf E - i\mathbf B$: $(F + i\tilde F)^{0j} = -(\mathbf E + i\mathbf B)^j$, $(F + i\tilde F)^{jk} = i\varepsilon_{jkl}(\mathbf E + i\mathbf B)^l$, and the complex conjugate for $F - i\tilde F$.
> 2. A proper Lorentz transformation maps $\mathbf E + i\mathbf B$ to $O(\Lambda)(\mathbf E + i\mathbf B)$ with a complex $3\times3$ matrix satisfying $O^{\mathsf T}O = \mathbb 1$; parity sends $\mathbf E + i\mathbf B \to -(\mathbf E - i\mathbf B)$, exchanging the halves.
> 3. The two invariants are one complex invariant: $(\mathbf E + i\mathbf B)\cdot(\mathbf E + i\mathbf B) = \mathbf E^2 - \mathbf B^2 + 2i\,\mathbf E\cdot\mathbf B = -\frac12F_{\mu\nu}F^{\mu\nu} - \frac i2F_{\mu\nu}\tilde F^{\mu\nu}$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 ("Irreducible pieces of a two-tensor": "For the field strength … built from E + iB and E − iB") · the components and items 2–3 derived here (item 2 checked numerically)*

^thm-c1a-7-3

> [!derivation]- Derivation
> **1. Eigenvectors.** By [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]], $\star\tilde F = \tilde{\tilde F} = -F$, so $\star(F + i\tilde F) = \tilde F - iF = -i(F + i\tilde F)$ and $\star(F - i\tilde F) = \tilde F + iF = i(F - i\tilde F)$.
>
> **2. Components.** From [[§C1a.7 Relativistic Electrodynamics in Index Form#^def-c1a-7-2|Def. §C1a.7.2]] and [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|Theorem §C1a.7.2]], 1: $(F + i\tilde F)^{0j} = -E^j - iB^j = -(\mathbf E + i\mathbf B)^j$ and $(F + i\tilde F)^{jk} = -\varepsilon_{jkl}B^l + i\varepsilon_{jkl}E^l = i\varepsilon_{jkl}(E^l + iB^l)$. So $\mathbf Z = \mathbf E + i\mathbf B \mapsto F + i\tilde F$ is a complex-linear bijection from $\mathbb C^3$ onto the $(-i)$-eigenspace, which is three-dimensional (Theorem §C1a.5.7, 3).
>
> **3. The action of Λ.** For $\det\Lambda = 1$, $\Lambda$ commutes with $\star$ (Theorem §C1a.5.7, 2) and is real, so $\Lambda(F + i\tilde F) = \Lambda F + i\star(\Lambda F)$ lies in the same eigenspace; through the bijection of step 2 it acts on $\mathbf Z$ as a complex-linear map $O(\Lambda)$. Step 4 shows $\mathbf Z\cdot\mathbf Z$ is invariant for every $\mathbf Z$, so by polarization $O\mathbf Z\cdot O\mathbf Z' = \mathbf Z\cdot\mathbf Z'$ for all $\mathbf Z, \mathbf Z'$, i.e. $O^{\mathsf T}O = \mathbb 1$ (bilinear, not sesquilinear). Parity: $P$ sends $\mathbf E \to -\mathbf E$, $\mathbf B \to \mathbf B$ (polar and axial), so $\mathbf E + i\mathbf B \to -\mathbf E + i\mathbf B = -(\mathbf E - i\mathbf B)$.
>
> **4. The complex invariant.** $\mathbf Z\cdot\mathbf Z = \mathbf E^2 - \mathbf B^2 + 2i\,\mathbf E\cdot\mathbf B$; by Theorem §C1a.7.2, 2, $\mathbf E^2 - \mathbf B^2 = -\frac12FF$ and $\mathbf E\cdot\mathbf B = -\frac14F\tilde F$, each invariant under $\det\Lambda = 1$.
>
> **What the derivation shows**
> - Rotations act on $\mathbf Z$ as real rotations; boosts act as rotations by imaginary angles: the Lorentz algebra over $\mathbb C$ is two copies of the rotation algebra, and the field strength carries one copy on $\mathbf E + i\mathbf B$ and the other on $\mathbf E - i\mathbf B$; in representation language these are $(1, 0)$ and $(0, 1)$, with $\mathbf E - i\mathbf B$ the $(1, 0)$ half in these conventions ([[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-7|Theorem §C3.4.7]], [[§C3.4 How Fields Transform under the Lorentz Group#^cau-c3-4-1|§C3.4, Caution: Which half of F is called (1, 0)]]).
> - Electromagnetic duality of the source-free equations, $\mathbf E \to \mathbf B$, $\mathbf B \to -\mathbf E$, is multiplication of $\mathbf Z$ by $-i$; continuous duality rotations $\mathbf Z \to e^{-i\alpha}\mathbf Z$ preserve the vacuum equations and the energy density $\frac12|\mathbf Z|^2$.

^der-c1a-7-3

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]], [[§C1a.7 Relativistic Electrodynamics in Index Form#^def-c1a-7-2|Def. §C1a.7.2]], [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|Theorem §C1a.7.2]]

## The lecture's boost example

> [!example] Example §C1a.7.1: The Lecture's Boost Example, Done with the Active Boost
> Take the active boost along $z$, $\Lambda^0{}_0 = \Lambda^3{}_3 = \gamma$, $\Lambda^0{}_3 = \Lambda^3{}_0 = \gamma v$ ([[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]]). The new $E_x$ is $F'_{01} = \Lambda_0{}^\lambda\Lambda_1{}^\sigma F_{\lambda\sigma}$. The second index $1$ forces $\sigma = 1$ with $\Lambda_1{}^1 = 1$; the first can come from $\lambda = 0$ or $3$. The lowered-index entries are those of $\Lambda^{-1}$, $\Lambda_\mu{}^\nu = (\Lambda^{-1})^\nu{}_\mu$ ([[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-3|REL Theorem §B1.2.3]]): $\Lambda_0{}^0 = \gamma$, $\Lambda_0{}^3 = g_{00}\Lambda^0{}_3g^{33} = -\gamma v$. With $F_{31} = -\varepsilon_{312}B^2 = -B_y$:
>
> $$
> E'_x = \Lambda_0{}^0\Lambda_1{}^1F_{01} + \Lambda_0{}^3\Lambda_1{}^1F_{31} = \gamma E_x + (-\gamma v)(-B_y) = \gamma\,(E_x + vB_y) .
> $$
>
> Only the entries of the $(t, z)$ block with one time and one spatial index enter. Check against [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-2|REL Theorem §B4.2.2]]: the active boost by $+v\hat{\mathbf z}$ is the passive transformation to a frame moving with $\mathbf u = -v\hat{\mathbf z}$, and $\mathbf E'_\perp = \gamma(\mathbf E + \mathbf u\times\mathbf B)_\perp$ gives $E'_x = \gamma(E_x - u_zB_y) = \gamma(E_x + vB_y)$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.7 (Derivation "Boost along z: the transformed E_x"), eq. (Exprime) · PHY 513 Lecture 1, Part C ("Example (Lorentz along z-axis)") · checked numerically*

^ex-c1a-7-1

> [!caution] Caution: The sign of the v × B term
> The Lecture 1 slide writes $E'_x = \gamma(E_x - vB_y)$ for this example. That corresponds to $\Lambda_0{}^3 = +\gamma v$, i.e. to the passive boost $t' = \gamma(t - vz)$, to a frame moving with $+v\hat{\mathbf z}$, while the slide's boost matrix is the active one. Neither sign is wrong in its own convention; mixing the two within one calculation is ([[§C1a.4 The Lorentz Group#^cau-c1a-4-1|§C1a.4, Caution: Active and passive readings]]). In field theory explicit transformations of $\mathbf E$ and $\mathbf B$ are almost never needed; what matters is that no equation is written whose two sides transform differently.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.7 (Caution "The sign of the v×B term depends on a convention") · PHY 513 Lecture 1, Part C*

^cau-c1a-7-2

> [!remark] Remark: Index techniques in Maxwell's equations
> Electromagnetism is the first place where every index move is needed at once; each is general, $F$ only the example (the derivation of Theorem §C1a.7.1 uses all four).
> 1. **Split a contracted index into time and space, with no signs**: $\partial_\mu F^{\mu\nu} = \partial_0F^{0\nu} + \partial_iF^{i\nu}$; then fix the free index, $\nu = 0$ and $\nu = j$ being separate equations, and let $F^{00} = 0$ kill a term.
> 2. **Use antisymmetry to reach the identification**: $F^{i0} = -F^{0i} = E^i$; the identification is stated for one ordering.
> 3. **Put the free index in the first slot of $\varepsilon$ before naming a curl**: $(\nabla\times\mathbf B)^j = \varepsilon_{jik}\partial_iB^k$; a term arriving as $\varepsilon_{ijk}\partial_iB^k$ is $-(\nabla\times\mathbf B)^j$. This is where Ampère's sign comes from.
> 4. **Count one metric sign per lowered spatial index**: $F_{0j} = -F^{0j}$, $F_{ij} = +F^{ij}$, $F^i{}_j = -F^{ij}$. This is how $F_{\rho\sigma}F^{\rho\sigma} = 2(\mathbf B^2 - \mathbf E^2)$ and the Poynting component $T^{0i} = F^{0j}F^{ij}$ come out ([[§C1b.6 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^rem-c1b-6-5|§C1b.6, Remark: Index moves for the electromagnetic tensor]]).
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.7 (Derivation "Index techniques in Maxwell's equations (Problem Set 2)") · PHY 513, Problem Set 2, Problem 4*

^rem-c1a-7-1

> [!remark] Remark: Electrodynamics as the template for field theory
> - **Redundancy.** The potential $A^\mu$ has four components but $A^\mu \to A^\mu + \partial^\mu\lambda$ changes nothing physical: the field strength is what is observed, and the potential is the variable in which the theory is local. Every gauge theory of the course has this structure (QFT C4: [[§C4.1 The Vector Field and Its Lorentz Transformation#^rem-c4-1-2|§C4.1, Remark: Four components, three or two states]], [[§C4.5 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^def-c4-5-1|Def. §C4.5.1]]; C8 planned).
> - **Dynamics from an action.** $\partial_\mu F^{\mu\nu} = J^\nu$ is the Euler–Lagrange equation of $\mathcal L = -\frac14F_{\mu\nu}F^{\mu\nu} - J^\mu A_\mu$, with the sixteen $\partial_\mu A_\nu$ as variables: $\partial\mathcal L/\partial(\partial_\mu A_\nu) = -F^{\mu\nu}$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-12|Theorem §C1a.5.12]], 4) and $\partial\mathcal L/\partial A_\nu = -J^\nu$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]]).
> - **Three statements, one fact.** $F$ contains only derivatives of $A$, so the only undifferentiated $A$ is in the coupling; a mass term $\frac12m^2A_\mu A^\mu$ would supply one and is exactly what gauge invariance forbids. "No bare $A$ in $F$", "the photon is massless" and "the theory is gauge invariant" are one fact (massive vector fields: [[§C4.2★ The Proca Field#^mod-c4-2-1|Model §C4.2.1]], [[§C4.2★ The Proca Field#^rem-c4-2-1|§C4.2★, Remark: Why F² plus a mass term]]; that the mass term breaks gauge invariance: [[§C4.5 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-5-3|Theorem §C4.5.3]]).
> - **Coupling requires conservation.** Under a gauge transformation the coupling changes by $-J^\mu\partial_\mu\lambda = -\partial_\mu(J^\mu\lambda) + \lambda\,\partial_\mu J^\mu$, a total derivative exactly when $\partial_\mu J^\mu = 0$: the same condition Maxwell's equations impose (Theorem §C1a.7.1), and the one Noether's theorem delivers for a U(1) symmetry of matter ([[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]]).
> - **A constraint, not an evolution.** $F_{00} = 0$, so $\partial_tA_0$ never appears in $\mathcal L$: $A_0$ has no conjugate momentum, and its equation (Gauss's law) constrains the initial data instead of evolving them, the classical shadow of gauge invariance ([[§C1b.4 Hamiltonian Field Theory|§C1b.4]]).
> - **Covariance at work.** $\partial_\mu F^{\mu\nu}$ and $J^\nu$ are both four-vectors, so the equation holds in all frames once it holds in one; no transformation of $\mathbf E$ and $\mathbf B$ is ever needed. This is the covariance principle applied to the equations that started relativity.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.7 ("Gauge invariance", "Inhomogeneous equations", closing paragraph); Ch. 3 §3.3 (Derivation "The Euler–Lagrange equation for other kinds of field", vector field)*

^rem-c1a-7-2

## Back to SI and Gaussian units

> [!theorem] Theorem §C1a.7.4: The SI–Heaviside–Lorentz Dictionary
> With $c$ kept explicit, the substitutions
>
> $$
> \mathbf E_{\rm HL} = \sqrt{\varepsilon_0}\,\mathbf E_{\rm SI}, \qquad \mathbf B_{\rm HL} = \frac{\mathbf B_{\rm SI}}{\sqrt{\mu_0}}, \qquad (q, \rho, \mathbf J)_{\rm HL} = \frac{(q, \rho, \mathbf J)_{\rm SI}}{\sqrt{\varepsilon_0}}
> $$
>
> turn SI electrodynamics into $\nabla\cdot\mathbf E = \rho$, $\nabla\times\mathbf B - \frac1c\partial_t\mathbf E = \frac1c\mathbf J$, $\nabla\times\mathbf E = -\frac1c\partial_t\mathbf B$, $\nabla\cdot\mathbf B = 0$, $\mathbf F = q(\mathbf E + \frac{\mathbf v}{c}\times\mathbf B)$, energy density $\frac12(E^2 + B^2)$ and $\alpha = e^2/4\pi\hbar c$; setting $\hbar = c = 1$ gives Def. §C1a.7.1. Gaussian units differ by $\sqrt{4\pi}$: $\mathbf E_{\rm G} = \sqrt{4\pi}\,\mathbf E_{\rm HL}$, $q_{\rm G} = q_{\rm HL}/\sqrt{4\pi}$.
>
> *Source: the user's pre-course notes, §1.2 ("Rationalized natural units"; $\alpha = e^2/4\pi\varepsilon_0\hbar c$) · the dictionary derived here*

^thm-c1a-7-4

> [!derivation]- Derivation
> **1. Gauss.** SI: $\nabla\cdot\mathbf E_{\rm SI} = \rho_{\rm SI}/\varepsilon_0$. Substitute $\mathbf E_{\rm SI} = \mathbf E/\sqrt{\varepsilon_0}$, $\rho_{\rm SI} = \sqrt{\varepsilon_0}\,\rho$: $\nabla\cdot\mathbf E/\sqrt{\varepsilon_0} = \rho/\sqrt{\varepsilon_0}$, i.e. $\nabla\cdot\mathbf E = \rho$.
>
> **2. Ampère–Maxwell.** SI: $\nabla\times\mathbf B_{\rm SI} - \mu_0\varepsilon_0\partial_t\mathbf E_{\rm SI} = \mu_0\mathbf J_{\rm SI}$. Substitute $\mathbf B_{\rm SI} = \sqrt{\mu_0}\,\mathbf B$, $\mathbf E_{\rm SI} = \mathbf E/\sqrt{\varepsilon_0}$, $\mathbf J_{\rm SI} = \sqrt{\varepsilon_0}\,\mathbf J$ and divide by $\sqrt{\mu_0}$: $\nabla\times\mathbf B - \sqrt{\mu_0\varepsilon_0}\,\partial_t\mathbf E = \sqrt{\mu_0\varepsilon_0}\,\mathbf J$, and $\sqrt{\mu_0\varepsilon_0} = 1/c$.
>
> **3. Faraday and no monopoles.** $\nabla\times\mathbf E_{\rm SI} = -\partial_t\mathbf B_{\rm SI}$ becomes $\nabla\times\mathbf E/\sqrt{\varepsilon_0} = -\sqrt{\mu_0}\,\partial_t\mathbf B$, i.e. $\nabla\times\mathbf E = -\frac1c\partial_t\mathbf B$; $\nabla\cdot\mathbf B = 0$ is homogeneous.
>
> **4. Force and energy.** $q_{\rm SI}\mathbf E_{\rm SI} = \sqrt{\varepsilon_0}q\,\mathbf E/\sqrt{\varepsilon_0} = q\mathbf E$; $q_{\rm SI}\mathbf v\times\mathbf B_{\rm SI} = \sqrt{\varepsilon_0\mu_0}\,q\,\mathbf v\times\mathbf B = q\frac{\mathbf v}{c}\times\mathbf B$. $\frac12(\varepsilon_0E_{\rm SI}^2 + B_{\rm SI}^2/\mu_0) = \frac12(E^2 + B^2)$.
>
> **5. Coulomb and $\alpha$.** The SI potential energy of two charges, $q_{1,\rm SI}q_{2,\rm SI}/4\pi\varepsilon_0r = q_1q_2/4\pi r$; so $\alpha = e_{\rm SI}^2/4\pi\varepsilon_0\hbar c = e^2/4\pi\hbar c$. Gaussian units put $q_{\rm G}^2 = q^2/4\pi$ so that the Coulomb energy is $q_{1,\rm G}q_{2,\rm G}/r$, and $E_{\rm G} = \sqrt{4\pi}E$ so that $q_{\rm G}E_{\rm G} = qE$.
>
> **What the derivation shows**
> - Heaviside–Lorentz is SI with the constants absorbed into the fields symmetrically: $\varepsilon_0$ into $\mathbf E$ and the charges, $\mu_0$ into $\mathbf B$; the combination $\mu_0\varepsilon_0 = 1/c^2$ is what remains, and it disappears with $c = 1$.
> - The $4\pi$ moves from the field equations (Gaussian) to Coulomb's law (Heaviside–Lorentz): rationalized units keep the Lagrangian $-\frac14F_{\mu\nu}F^{\mu\nu}$ free of $4\pi$, which is why field theory uses them.
> - Restoring $\hbar$ and $c$ in a natural-units formula is [[P4 Restoring ħ and c|P4]]; this theorem supplies the electromagnetic part.

^der-c1a-7-4

*Uses:* [[§C1a.7 Relativistic Electrodynamics in Index Form#^def-c1a-7-1|Def. §C1a.7.1]], [[§B8.4 Maxwell's Equations#^pr-b8-4-2|EM Principle §B8.4.2]]

> [!remark]- Connections
> - Relativity level B derives the same tensor in SI units from the variation of a charge's coupling $-q\int A_\mu dx^\mu$, and obtains the transformation of $\mathbf E$ and $\mathbf B$, the invariant classes and the field of a moving charge; with Theorem §C1a.7.4 all of it carries over by $F_{\rm REL} = \sqrt{\mu_0}F$ and $c = 1$ — [[§B3.2 The Charged Particle#^thm-b3-2-5|REL Theorem §B3.2.5]], [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-2|REL Theorem §B4.2.2]], [[§B4.2 The Electromagnetic Field Tensor#^ex-b4-2-1|REL Example §B4.2.1]].
> - In the Lorenz gauge $\partial_\mu A^\mu = 0$ the inhomogeneous equation becomes $\partial^2 A^\nu = J^\nu$: four massless Klein–Gordon equations with a source, solved by the retarded Green's function of [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]] at $m = 0$ — [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-7|REL Theorem §B4.2.7]], [[§B11.1★ Potentials, Gauges and Retarded Potentials#^def-b11-1-1|EM Def. §B11.1.1]].
> - The Bianchi identity is $d(dA) = 0$ for the two-form $F = dA$, and on a region without holes every closed $F$ is exact (Poincaré lemma); the exceptions on regions with holes are physics (monopoles, the Aharonov–Bohm phase) — [[§39 Closed and Exact Forms#^prop-39-7|452 Prop. §39.7]], [[§C4.3 Potentials, Gauge Transformations and the Aharonov–Bohm Effect|QM §C4.3]].
> - $\mathbf E\cdot\mathbf B \propto \varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ is a total derivative, so it is invisible to the classical equations; in non-abelian gauge theories and with fermions the same density produces the axial anomaly and the $\theta$ term (beyond the course).
> - The energy–momentum tensor of the field, $T^{00} = \frac12(\mathbf E^2 + \mathbf B^2)$ and the Poynting vector $T^{0i} = (\mathbf E\times\mathbf B)^i$ in Heaviside–Lorentz units, comes from Noether's theorem plus the Belinfante improvement — [[§C1b.6 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^ex-c1b-6-3|Example §C1b.6.3]], [[§B9.1 Charge, Energy and Poynting's Theorem|EM §B9.1]].
> - Heaviside–Lorentz units make $\alpha = e^2/4\pi$ and put the $4\pi$ into Coulomb's law; the Coulomb potential $1/4\pi r$ is the static massless Green's function, the $m \to 0$ limit of the Yukawa potential $e^{-mr}/4\pi r$ — [[§B4.1 The Klein–Gordon Equation#^rem-b4-1-4|REL Remark: Static solutions and the Yukawa potential]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]].
> - Electromagnetism level C: the same theory in SI units with the action as the principle — the Maxwell action, the gauge-invariant quadratic Lagrangians (no mass term), the inhomogeneous equations as Euler–Lagrange equations, Gauss's law as a constraint, and the energy–momentum tensor with sources — [[§C1.1 Building the Maxwell Action#^pr-c1-1-4|EM Principle §C1.1.4]], [[§C1.1 Building the Maxwell Action#^thm-c1-1-2|EM Theorem §C1.1.2]], [[§C1.2 The Field Equations and the Bianchi Identity#^thm-c1-2-2|EM Theorem §C1.2.2]], [[§C1.2 The Field Equations and the Bianchi Identity#^thm-c1-2-3|EM Theorem §C1.2.3]], [[§C1.5 The Electromagnetic Energy–Momentum Tensor#^def-c1-5-1|EM Def. §C1.5.1]], [[§C1.5 The Electromagnetic Energy–Momentum Tensor#^thm-c1-5-4|EM Theorem §C1.5.4]].
> - Electromagnetism level C: the static case, the Coulomb potential as the fundamental solution of the Laplacian, and the Green functions that boundaries select (with the normalization dictionary to the $-i$ convention used here) — [[§C2.1 The Static Limit and the Field of a Charge Distribution#^rem-c2-1-1|EM Remark: The Coulomb potential as a fundamental solution]], [[§C7.3 Green Functions for Poisson’s Equation#^def-c7-3-1|EM Def. §C7.3.1]], [[§C7.3 Green Functions for Poisson’s Equation#^cau-c7-3-1|EM Caution: Normalizations of the Green function]], [[§C7.3 Green Functions for Poisson’s Equation#^thm-c7-3-1|EM Theorem §C7.3.1]].
