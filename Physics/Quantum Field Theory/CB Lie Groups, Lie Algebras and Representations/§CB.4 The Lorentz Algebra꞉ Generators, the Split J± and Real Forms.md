---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs]] →

*Sources (proofs written from these, each checked against the text): B. C. Hall, An Elementary Introduction to Groups and Representations, Chs. 3, 5 (https://arxiv.org/abs/math-ph/0005032) · P. Woit, Quantum Theory, Groups and Representations, §§5.5, 21.2, 40.2 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, §9.4, Exercise 11.4, Remark 17.3 (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf) · the user's PHY 513 notes, Ch. 7 §§7.2, 7.4 (J± and "the algebra decomposes") · PHY 513 Lecture 7 · PHY 513, Problem Set 5, Problem 1 (as the user wrote it) · Yu Zhao-Huan, 量子场论讲义, §3.2, Exercises 3.1, 3.7 · Peskin & Schroeder, §3.1 · for the generators and the Lorentz algebra: the user's PHY 513 notes, Ch. 1 §1.6, Ch. 7 §7.3; PHY 513, Problem Set 4, Problem 5 (as the user wrote it; submitted); Yu §3.1–§3.2 · the rest written here.*

Which commutation relations must the six Lorentz generators obey in every representation, which real Lie algebra do they form, and in which sense is it "two copies of the rotation algebra"? The section opens with the Lorentz algebra as the course derives it (PHY 513 Lecture 7, Part B; Problem Sets 4 and 5): the generators of a representation, their commutation relations with three derivations, the tensor law of the generators, and the vanishing of one-dimensional representations. With the complexification and the real forms of [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification|§CB.3]], this section splits the complexified Lorentz algebra by $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ into two commuting copies of $\mathfrak{sl}(2, \mathbb C)$, contrasts the Euclidean $\mathfrak{so}(4)$, which splits already over $\mathbb R$, shows that $\mathfrak{so}(1,3)$ and $\mathfrak{so}(4)$ are two real forms of one complex algebra (and that $\mathfrak{sl}(2, \mathbb C)$ has two real forms of its own), identifies the real Lie algebra of $SL(2, \mathbb C)$ with the Lorentz algebra, and proves that real forms have the same representations, the input to Weyl's unitary trick in [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs|§CB.5]]. The physics that uses it, the indices of fields and their labels $(j_+, j_-)$, is [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]]. The complexification of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ and its representations continue in [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover|§CB.14]].

*Conventions* (the course's, [[Larsen PHY 513]]): active reading; $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$; $J_i = \frac12\varepsilon_{ijk}\mathcal J^{jk}$, $K_i = \mathcal J^{0i}$ (Peskin–Schroeder's sign; Problem Set 5 uses the opposite one, [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|Caution: Which one is (½, 0) depends on the sign of K]]); $\theta_i = \frac12\varepsilon_{ijk}\omega_{jk}$, $\eta_i = \omega_{0i}$; $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$. Latin indices are Euclidean labels, summed when repeated. In the first part (Definition §CB.4.1 to Theorem §CB.4.5) $V$ denotes the complex carrier space of a representation $D$, not Minkowski space; the generators carry no hat, as everywhere in CB.

## Generators and the Lorentz algebra

> [!definition] Definition §CB.4.1: Generators of a Representation
> Let $D$ be a representation of $SO^+(1,3)$ on a finite-dimensional complex vector space $V$. Its **generators** are the six matrices $D(\mathcal J^{\mu\nu}) = -D(\mathcal J^{\nu\mu})$ on $V$ defined by
>
> $$
> D(e^{s\omega}) = \mathbb 1 - \frac{is}{2}\,\omega_{\mu\nu}\,D(\mathcal J^{\mu\nu}) + O(s^2) \quad\text{for every antisymmetric } \omega_{\mu\nu}, \qquad\text{so that}\qquad D(e^{\omega}) = \exp\Bigl(-\frac i2\,\omega_{\mu\nu}D(\mathcal J^{\mu\nu})\Bigr) .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.3 (Derivation "The Lorentz algebra from the group law alone"; Principle "How the parameters enter", eq. (Dlambda)) · PHY 513 Lecture 7, Part B ("All representations realize the abstract algebra") · PS §3.1, eqs. (3.13), (3.17) · Yu §3.2, eqs. (3.35)–(3.36)*

^def-cb-4-1

For the vector representation, $D(\Lambda) = \Lambda$, the generators are the $4\times4$ matrices $\mathcal J^{\mu\nu}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-2|Theorem §C1a.6.2]]). (The Lecture 7 slide "Vector Representation" prints their both-lower form as $i(\delta^\nu_\alpha\delta^\nu_\beta - \delta^\nu_\beta\delta^\mu_\alpha)$, with $\nu$ repeated; Peskin–Schroeder's (3.18) is $i(\delta^\mu_\alpha\delta^\nu_\beta - \delta^\mu_\beta\delta^\nu_\alpha)$.) The exponential formula holds because $s \mapsto D(e^{s\omega})$ and $s \mapsto \exp(-\frac{is}{2}\omega_{\mu\nu}D(\mathcal J^{\mu\nu}))$ are both one-parameter groups of matrices ($e^{s\omega}e^{t\omega} = e^{(s+t)\omega}$) with the same derivative at $s = 0$, and such a group is fixed by that derivative ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]]; for rotations, [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-3|QM Theorem §C5.1.3]]). The notation $D(\mathcal J^{\mu\nu})$ names *which* generator by its label pair and *how* it is realized by $D$; the realizations met in the course (the abstract $J^{\mu\nu}$, the orbital $L^{\mu\nu}$, the matrices $\mathcal J^{\mu\nu}$ and $S^{\mu\nu}$) are listed in [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^rem-c3-1-1|§C3.1, Remark: One symbol for each realization of the generators]].

> [!theorem] Theorem §CB.4.2: The Lorentz Algebra
> The generators $D(\mathcal J^{\mu\nu})$ of every representation ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^def-cb-4-1|Def. §CB.4.1]]), written $\mathcal J^{\mu\nu}$, among them the $4\times4$ matrices of the vector representation ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]), obey
>
> $$
> [\mathcal J^{\mu\nu}, \mathcal J^{\rho\sigma}] = i\bigl(g^{\nu\rho}\mathcal J^{\mu\sigma} - g^{\mu\rho}\mathcal J^{\nu\sigma} - g^{\nu\sigma}\mathcal J^{\mu\rho} + g^{\mu\sigma}\mathcal J^{\nu\rho}\bigr),
> $$
>
> equivalently, in terms of the rotation and boost generators $J_i = \frac12\varepsilon_{ijk}\mathcal J^{jk}$, $K_i = \mathcal J^{0i}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]),
>
> $$
> [J_i, J_j] = i\varepsilon_{ijk}J_k, \qquad [J_i, K_j] = i\varepsilon_{ijk}K_k, \qquad [K_i, K_j] = -i\varepsilon_{ijk}J_k ,
> $$
>
> The complex combinations $\mathbf J_\pm$ that split this algebra into two commuting angular momenta are [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-7|Theorem §CB.4.7]].
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.6 (Principle "The Lorentz algebra in terms of rotations and boosts", eq. (JKalgebra); checked numerically there in the vector representation, and checked again here) · PHY 513, Problem Set 4, Problem 5, eq. (15) (statement) · Yu §3.1, eq. (3.63)*

^thm-cb-4-2

> [!derivation]- Derivation (from the group law: every representation)
> Let $D$ be a representation of $SO^+(1,3)$ on a finite-dimensional complex space, $D(\Lambda_1)D(\Lambda_2) = D(\Lambda_1\Lambda_2)$, $D(\mathbb 1) = \mathbb 1$, differentiable at the identity. Its generators $J^{\mu\nu} \equiv D(\mathcal J^{\mu\nu}) = -J^{\nu\mu}$ are defined by the first-order term along one-parameter subgroups, $D(e^{s\omega}) = \mathbb 1 - \frac{is}{2}\,\omega_{\mu\nu}J^{\mu\nu} + O(s^2)$ for every antisymmetric $\omega_{\mu\nu}$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^def-cb-4-1|Def. §CB.4.1]]); for the vector representation $D(\Lambda) = \Lambda$ they are the $\mathcal J^{\mu\nu}$ of Def. §C1a.6.1 (Theorem §C1a.6.2).
>
> **1. Conjugate a one-parameter subgroup.** Fix $\Lambda \in SO^+(1,3)$ and an antisymmetric $\omega'_{\mu\nu}$. The path $s \mapsto e^{s\omega'}$ lies in $SO^+(1,3)$ (Theorem §C1a.6.4), and conjugation passes through the power series, $(\Lambda^{-1}A\Lambda)^n = \Lambda^{-1}A^n\Lambda$, so
>
> $$
> \Lambda^{-1}e^{s\omega'}\Lambda = e^{s\,\Lambda^{-1}\omega'\Lambda} .
> $$
>
> **2. Lower the indices of the conjugated matrix.** From $\Lambda^{\mathsf T}g\Lambda = g$ ([[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]]), $\Lambda^{-1} = g^{-1}\Lambda^{\mathsf T}g$, i.e. $(\Lambda^{-1})^\kappa{}_\alpha = g^{\kappa\tau}\Lambda^\lambda{}_\tau\,g_{\lambda\alpha}$. Then
>
> $$
> (\Lambda^{-1}\omega'\Lambda)_{\mu\nu} \equiv g_{\mu\kappa}(\Lambda^{-1})^\kappa{}_\alpha\,\omega'^\alpha{}_\beta\,\Lambda^\beta{}_\nu = g_{\mu\kappa}g^{\kappa\tau}\Lambda^\lambda{}_\tau\,g_{\lambda\alpha}\,\omega'^\alpha{}_\beta\,\Lambda^\beta{}_\nu = \Lambda^\lambda{}_\mu\,\omega'_{\lambda\beta}\,\Lambda^\beta{}_\nu ,
> $$
>
> using $g_{\mu\kappa}g^{\kappa\tau} = \delta_\mu{}^\tau$ and $g_{\lambda\alpha}\omega'^\alpha{}_\beta = \omega'_{\lambda\beta}$. Exchanging $\mu \leftrightarrow \nu$ and renaming the dummies $\lambda \leftrightarrow \beta$ gives $\Lambda^\beta{}_\nu\,\omega'_{\beta\lambda}\,\Lambda^\lambda{}_\mu = -\Lambda^\lambda{}_\mu\,\omega'_{\lambda\beta}\,\Lambda^\beta{}_\nu$: the conjugated matrix is again antisymmetric with lower indices, i.e. again in the Lie algebra (Theorem §C1a.6.1).
>
> **3. The group law, to first order in s.** The representation property, used twice with $D(\Lambda^{-1}) = D(\Lambda)^{-1}$, gives $D(\Lambda)^{-1}D(e^{s\omega'})D(\Lambda) = D(\Lambda^{-1}e^{s\omega'}\Lambda) = D(e^{s\Lambda^{-1}\omega'\Lambda})$. Expand both sides with the definition of the generators and drop $O(s^2)$:
>
> $$
> \mathbb 1 - \frac{is}{2}\,\omega'_{\rho\sigma}\,D(\Lambda)^{-1}J^{\rho\sigma}D(\Lambda) = \mathbb 1 - \frac{is}{2}\,(\Lambda^{-1}\omega'\Lambda)_{\mu\nu}J^{\mu\nu} = \mathbb 1 - \frac{is}{2}\,\omega'_{\rho\sigma}\,\Lambda^\rho{}_\mu\Lambda^\sigma{}_\nu\,J^{\mu\nu} ,
> $$
>
> the last step inserting step 2 and renaming the dummies $\lambda \to \rho$, $\beta \to \sigma$.
>
> **4. Compare coefficients: the tensor law.** Both coefficients of $\omega'_{\rho\sigma}$ are antisymmetric in $\rho\sigma$ ($J^{\rho\sigma}$ is; in $\Lambda^\rho{}_\mu\Lambda^\sigma{}_\nu J^{\mu\nu}$ exchange $\rho \leftrightarrow \sigma$ and rename $\mu \leftrightarrow \nu$). An antisymmetric $X^{\rho\sigma}$ with $\omega'_{\rho\sigma}X^{\rho\sigma} = 0$ for every antisymmetric $\omega'$ vanishes: the choice $\omega'_{01} = -\omega'_{10} = 1$, all else $0$, gives $2X^{01} = 0$, and likewise for each of the six pairs. Hence, for every finite $\Lambda$,
>
> $$
> D(\Lambda)^{-1}\,J^{\rho\sigma}\,D(\Lambda) = \Lambda^\rho{}_\mu\,\Lambda^\sigma{}_\nu\,J^{\mu\nu} .
> $$
>
> ⚑ By-product: the generators of any representation transform under conjugation as a tensor with two upper indices → [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-4|Theorem §CB.4.4]].
>
> **5. Make Λ infinitesimal: the left side.** Put $\Lambda = e^{t\omega}$ and keep first order in $t$ (absorbed into $\omega$ below): $D(\Lambda) = \mathbb 1 - \frac i2\omega_{\alpha\beta}J^{\alpha\beta} + O(\omega^2)$ and $D(\Lambda)^{-1} = \mathbb 1 + \frac i2\omega_{\alpha\beta}J^{\alpha\beta} + O(\omega^2)$ (their product is $\mathbb 1 + O(\omega^2)$). Expanding the triple product into its four terms and dropping the one of second order,
>
> $$
> \Bigl(\mathbb 1 + \tfrac i2\omega_{\alpha\beta}J^{\alpha\beta}\Bigr)J^{\rho\sigma}\Bigl(\mathbb 1 - \tfrac i2\omega_{\alpha\beta}J^{\alpha\beta}\Bigr) = J^{\rho\sigma} + \tfrac i2\omega_{\alpha\beta}J^{\alpha\beta}J^{\rho\sigma} - \tfrac i2\omega_{\alpha\beta}J^{\rho\sigma}J^{\alpha\beta} + O(\omega^2) = J^{\rho\sigma} + \tfrac i2\,\omega_{\alpha\beta}\,[J^{\alpha\beta}, J^{\rho\sigma}] + O(\omega^2) .
> $$
>
> **6. The right side.** With $\Lambda^\rho{}_\mu = \delta^\rho{}_\mu + \omega^\rho{}_\mu + O(\omega^2)$, the product has four terms:
>
> $$
> (\delta^\rho{}_\mu + \omega^\rho{}_\mu)(\delta^\sigma{}_\nu + \omega^\sigma{}_\nu)J^{\mu\nu} = J^{\rho\sigma} + \omega^\rho{}_\mu J^{\mu\sigma} + \omega^\sigma{}_\nu J^{\rho\nu} + \omega^\rho{}_\mu\omega^\sigma{}_\nu J^{\mu\nu} ;
> $$
>
> the last is second order and is dropped.
>
> **7. Write the right side with the lower-index ω, antisymmetrized.** Raise with the metric and rename the dummy $\mu \to \beta$: $\omega^\rho{}_\mu J^{\mu\sigma} = g^{\rho\alpha}\omega_{\alpha\beta}J^{\beta\sigma}$. Write it as two halves and in the second rename $\alpha \leftrightarrow \beta$, then use $\omega_{\beta\alpha} = -\omega_{\alpha\beta}$:
>
> $$
> g^{\rho\alpha}\omega_{\alpha\beta}J^{\beta\sigma} = \tfrac12\,\omega_{\alpha\beta}\bigl(g^{\rho\alpha}J^{\beta\sigma} - g^{\rho\beta}J^{\alpha\sigma}\bigr), \qquad \omega^\sigma{}_\nu J^{\rho\nu} = g^{\sigma\alpha}\omega_{\alpha\beta}J^{\rho\beta} = \tfrac12\,\omega_{\alpha\beta}\bigl(g^{\sigma\alpha}J^{\rho\beta} - g^{\sigma\beta}J^{\rho\alpha}\bigr) .
> $$
>
> **8. Compare coefficients again.** Steps 5–7 and the $J^{\rho\sigma}$ on both sides cancelling:
>
> $$
> \tfrac i2\,\omega_{\alpha\beta}\,[J^{\alpha\beta}, J^{\rho\sigma}] = \tfrac12\,\omega_{\alpha\beta}\bigl(g^{\rho\alpha}J^{\beta\sigma} - g^{\rho\beta}J^{\alpha\sigma} + g^{\sigma\alpha}J^{\rho\beta} - g^{\sigma\beta}J^{\rho\alpha}\bigr) .
> $$
>
> Both coefficients of $\omega_{\alpha\beta}$ are antisymmetric in $\alpha\beta$ (on the right, exchanging $\alpha \leftrightarrow \beta$ maps the four terms to minus themselves in the order 2, 1, 4, 3), so by the argument of step 4, after multiplying by $-2i$,
>
> $$
> [J^{\alpha\beta}, J^{\rho\sigma}] = -i\bigl(g^{\rho\alpha}J^{\beta\sigma} - g^{\rho\beta}J^{\alpha\sigma} + g^{\sigma\alpha}J^{\rho\beta} - g^{\sigma\beta}J^{\rho\alpha}\bigr) .
> $$
>
> **9. Rename to the standard form.** Rename $\alpha \to \mu$, $\beta \to \nu$, use $g^{\rho\mu} = g^{\mu\rho}$ etc., and distribute the $-i$:
>
> $$
> [J^{\mu\nu}, J^{\rho\sigma}] = i\bigl(g^{\nu\rho}J^{\mu\sigma} - g^{\mu\rho}J^{\nu\sigma} - g^{\mu\sigma}J^{\rho\nu} + g^{\nu\sigma}J^{\rho\mu}\bigr) .
> $$
>
> In the last two terms use the antisymmetry $J^{\rho\nu} = -J^{\nu\rho}$ and $J^{\rho\mu} = -J^{\mu\rho}$: $-g^{\mu\sigma}J^{\rho\nu} = +g^{\mu\sigma}J^{\nu\rho}$ and $+g^{\nu\sigma}J^{\rho\mu} = -g^{\nu\sigma}J^{\mu\rho}$. Reordering gives the covariant relation of Theorem §CB.4.2.
>
> **What the derivation shows**
> - Nothing but the multiplication law of the group and the definition of the generators entered, so the six generators of *every* representation obey the same relation with the same structure constants: the $4\times4$ matrices $\mathcal J^{\mu\nu}$ (checked directly in the second route below), the orbital operators on functions ([[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-2|Theorem §C3.3.2]]), the Dirac matrices $S^{\mu\nu}$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]) and the Hilbert-space charges ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-5|Theorem §C3.4.5]], where the same argument is run with unitary operators $U(\Lambda)$, as in Yu §3.2).
> - The finite identity of step 4 is the stronger statement; the algebra is its first-order part → [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^rem-cb-4-2|§CB.4, Remark: The algebra is the infinitesimal tensor law]].
> - Assumptions: $D$ is differentiable at the identity and multiplicative near it. For the spinor representations, defined on $SO^+(1,3)$ only up to a sign ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-6|Theorem §CB.15.6]]), the sign of $D(\Lambda)$ cancels between $D(\Lambda)^{-1}$ and $D(\Lambda)$ in step 4, and steps 5–9 use only elements near the identity, where the sign is fixed to $+$ by continuity.
> - Used next: the reduction to $\mathbf J$, $\mathbf K$ and $\mathbf J_\pm$ (third derivation below), and the classification of [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]].
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.3 (Derivation "The Lorentz algebra from the group law alone") · Yu §3.2, eqs. (3.30)–(3.33) (the same computation for the operators on states)*

^der-cb-4-2

*Uses:* [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^def-cb-4-1|Def. §CB.4.1]]

> [!derivation]- Derivation (second route: direct computation in the vector representation)
> This is the user's submitted solution of PHY 513 Problem Set 4, Problem 5(a), in the notation of this note. Work with the real matrices $M^{\mu\nu}$ of Def. §C1a.6.1, $\mathcal J^{\mu\nu} = iM^{\mu\nu}$, so that $[\mathcal J^{\mu\nu}, \mathcal J^{\rho\sigma}] = i^2[M^{\mu\nu}, M^{\rho\sigma}]$; the factor $i^2$ is restored in step 7. Generator labels are $\mu\nu$, $\rho\sigma$; matrix indices $\alpha, \beta, \gamma$, with $\gamma$ summed.
>
> **1. The matrix commutator.** Its $(\alpha, \beta)$ entry is $([M^{\mu\nu}, M^{\rho\sigma}])^\alpha{}_\beta = (M^{\mu\nu})^\alpha{}_\gamma(M^{\rho\sigma})^\gamma{}_\beta - (M^{\rho\sigma})^\alpha{}_\gamma(M^{\mu\nu})^\gamma{}_\beta$, with $(M^{\mu\nu})^\alpha{}_\gamma = g^{\mu\alpha}\delta^\nu{}_\gamma - g^{\nu\alpha}\delta^\mu{}_\gamma$ and $(M^{\rho\sigma})^\gamma{}_\beta = g^{\rho\gamma}\delta^\sigma{}_\beta - g^{\sigma\gamma}\delta^\rho{}_\beta$.
>
> **2. The first product, all four terms.**
>
> $$
> (M^{\mu\nu})^\alpha{}_\gamma(M^{\rho\sigma})^\gamma{}_\beta = g^{\mu\alpha}\delta^\nu{}_\gamma g^{\rho\gamma}\delta^\sigma{}_\beta - g^{\mu\alpha}\delta^\nu{}_\gamma g^{\sigma\gamma}\delta^\rho{}_\beta - g^{\nu\alpha}\delta^\mu{}_\gamma g^{\rho\gamma}\delta^\sigma{}_\beta + g^{\nu\alpha}\delta^\mu{}_\gamma g^{\sigma\gamma}\delta^\rho{}_\beta .
> $$
>
> **3. Sum over γ.** Each $\delta^\cdot{}_\gamma$ sets $\gamma$ equal to its other index:
>
> $$
> (M^{\mu\nu}M^{\rho\sigma})^\alpha{}_\beta = g^{\mu\alpha}g^{\rho\nu}\delta^\sigma{}_\beta - g^{\mu\alpha}g^{\sigma\nu}\delta^\rho{}_\beta - g^{\nu\alpha}g^{\rho\mu}\delta^\sigma{}_\beta + g^{\nu\alpha}g^{\sigma\mu}\delta^\rho{}_\beta .
> $$
>
> **4. The second product.** It is the first with the labels exchanged, $\mu \leftrightarrow \rho$, $\nu \leftrightarrow \sigma$:
>
> $$
> (M^{\rho\sigma}M^{\mu\nu})^\alpha{}_\beta = g^{\rho\alpha}g^{\mu\sigma}\delta^\nu{}_\beta - g^{\rho\alpha}g^{\nu\sigma}\delta^\mu{}_\beta - g^{\sigma\alpha}g^{\mu\rho}\delta^\nu{}_\beta + g^{\sigma\alpha}g^{\nu\rho}\delta^\mu{}_\beta .
> $$
>
> **5. Subtract: eight terms.**
>
> $$
> \begin{aligned}
> ([M^{\mu\nu}, M^{\rho\sigma}])^\alpha{}_\beta = {}& g^{\mu\alpha}g^{\rho\nu}\delta^\sigma{}_\beta - g^{\mu\alpha}g^{\sigma\nu}\delta^\rho{}_\beta - g^{\nu\alpha}g^{\rho\mu}\delta^\sigma{}_\beta + g^{\nu\alpha}g^{\sigma\mu}\delta^\rho{}_\beta \\
> & - g^{\rho\alpha}g^{\mu\sigma}\delta^\nu{}_\beta + g^{\rho\alpha}g^{\nu\sigma}\delta^\mu{}_\beta + g^{\sigma\alpha}g^{\mu\rho}\delta^\nu{}_\beta - g^{\sigma\alpha}g^{\nu\rho}\delta^\mu{}_\beta .
> \end{aligned}
> $$
>
> **6. Pair the terms by the metric that carries only labels.** Pairing the first with the eighth, the second with the sixth, the third with the seventh and the fourth with the fifth (and using $g^{\rho\nu} = g^{\nu\rho}$ etc.),
>
> $$
> \begin{aligned}
> ([M^{\mu\nu}, M^{\rho\sigma}])^\alpha{}_\beta &= g^{\nu\rho}\bigl(g^{\mu\alpha}\delta^\sigma{}_\beta - g^{\sigma\alpha}\delta^\mu{}_\beta\bigr) + g^{\nu\sigma}\bigl(g^{\rho\alpha}\delta^\mu{}_\beta - g^{\mu\alpha}\delta^\rho{}_\beta\bigr) + g^{\mu\rho}\bigl(g^{\sigma\alpha}\delta^\nu{}_\beta - g^{\nu\alpha}\delta^\sigma{}_\beta\bigr) + g^{\mu\sigma}\bigl(g^{\nu\alpha}\delta^\rho{}_\beta - g^{\rho\alpha}\delta^\nu{}_\beta\bigr) \\
> &= g^{\nu\rho}(M^{\mu\sigma})^\alpha{}_\beta + g^{\nu\sigma}(M^{\rho\mu})^\alpha{}_\beta + g^{\mu\rho}(M^{\sigma\nu})^\alpha{}_\beta + g^{\mu\sigma}(M^{\nu\rho})^\alpha{}_\beta ,
> \end{aligned}
> $$
>
> each bracket being an entry of $M$ by Def. §C1a.6.1. With $M^{\rho\mu} = -M^{\mu\rho}$ and $M^{\sigma\nu} = -M^{\nu\sigma}$, as matrices
>
> $$
> [M^{\mu\nu}, M^{\rho\sigma}] = g^{\nu\rho}M^{\mu\sigma} - g^{\mu\rho}M^{\nu\sigma} - g^{\nu\sigma}M^{\mu\rho} + g^{\mu\sigma}M^{\nu\rho} .
> $$
>
> **7. Restore i.** $[\mathcal J^{\mu\nu}, \mathcal J^{\rho\sigma}] = i^2[M^{\mu\nu}, M^{\rho\sigma}] = i\bigl(g^{\nu\rho}\,iM^{\mu\sigma} - g^{\mu\rho}\,iM^{\nu\sigma} - g^{\nu\sigma}\,iM^{\mu\rho} + g^{\mu\sigma}\,iM^{\nu\rho}\bigr) = i\bigl(g^{\nu\rho}\mathcal J^{\mu\sigma} - g^{\mu\rho}\mathcal J^{\nu\sigma} - g^{\nu\sigma}\mathcal J^{\mu\rho} + g^{\mu\sigma}\mathcal J^{\nu\rho}\bigr)$.
>
> **What the derivation shows**
> - The real matrices obey the algebra without any $i$: $[M^{\mu\nu}, M^{\rho\sigma}] = g^{\nu\rho}M^{\mu\sigma} - \dots$ is the real Lie algebra $\mathfrak{so}(1,3)$, and the $i$'s of the covariant relation are the price of the Hermitian convention $\mathcal J = iM$, as in Quantum Mechanics ([[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^rem-c5-1-1|QM ★ Remark: The Lie algebra of SO(3)]]).
> - Using the mixed-index matrices avoids raising and lowering matrix indices; with Peskin–Schroeder's both-lower form the product rule is $(AB)_{\alpha\gamma} = A_{\alpha\beta}B^\beta{}_\gamma$, and the computation is the same.
> - It confirms the group-law derivation in one representation, as it must; it does not by itself say anything about other representations.
>
> *Source: the user's write-up of PHY 513, Problem Set 4, Problem 5(a) (submitted) · Yu §4.1, eqs. (4.5)–(4.6) · the user's pre-course notes, §2.2 (Example "The vector-representation matrices satisfy the algebra")*

^der-cb-4-2b

*Uses:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]

> [!derivation]- Derivation (the J, K form and the J± split)
> This is the user's submitted solution of PHY 513 Problem Set 5, Problem 1(a), written with $K_i = \mathcal J^{0i}$ (Def. §C1a.6.2); the problem set defines $K_i = \mathcal J^{i0}$, which changes nothing in the relations below (each is unchanged by $\mathbf K \to -\mathbf K$), but exchanges $\mathbf J_+ \leftrightarrow \mathbf J_-$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]]). Here $\mathcal J^{\mu\nu}$ are the generators in any representation. Latin indices run over $1, 2, 3$, are summed when repeated, and their position carries no meaning; between spatial generator labels the metric is $g^{ij} = -\delta_{ij}$, and $g^{0i} = 0$, $g^{00} = 1$.
>
> **1. Invert the definitions.** $\varepsilon_{ijk}J_k = \frac12\varepsilon_{ijk}\varepsilon_{kab}\mathcal J^{ab} = \frac12(\delta_{ia}\delta_{jb} - \delta_{ib}\delta_{ja})\mathcal J^{ab} = \frac12(\mathcal J^{ij} - \mathcal J^{ji}) = \mathcal J^{ij}$, using $\varepsilon_{ijk}\varepsilon_{kab} = \delta_{ia}\delta_{jb} - \delta_{ib}\delta_{ja}$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], three-dimensional form). Also $\mathcal J^{i0} = -\mathcal J^{0i} = -K_i$ and $\mathcal J^{aa} = 0$ (antisymmetry).
>
> **2. Rotations with rotations.** The $\varepsilon$'s are numbers, so $[J_i, J_j] = \frac14\varepsilon_{ikl}\varepsilon_{jmn}[\mathcal J^{kl}, \mathcal J^{mn}]$, and the covariant relation with all labels spatial gives
>
> $$
> [\mathcal J^{kl}, \mathcal J^{mn}] = i\bigl(g^{lm}\mathcal J^{kn} - g^{km}\mathcal J^{ln} - g^{ln}\mathcal J^{km} + g^{kn}\mathcal J^{lm}\bigr) = i\bigl(-\delta_{lm}\mathcal J^{kn} + \delta_{km}\mathcal J^{ln} + \delta_{ln}\mathcal J^{km} - \delta_{kn}\mathcal J^{lm}\bigr) .
> $$
>
> Contract each $\delta$ with the $\varepsilon$'s; each of the four terms equals $\mathcal J^{ij}$:
>
> $$
> \begin{aligned}
> -\varepsilon_{ikl}\varepsilon_{jln}\mathcal J^{kn} &= \varepsilon_{lik}\varepsilon_{ljn}\mathcal J^{kn} = (\delta_{ij}\delta_{kn} - \delta_{in}\delta_{kj})\mathcal J^{kn} = \delta_{ij}\mathcal J^{kk} - \mathcal J^{ji} = \mathcal J^{ij}, \\
> \varepsilon_{ikl}\varepsilon_{jkn}\mathcal J^{ln} &= \varepsilon_{kli}\varepsilon_{knj}\mathcal J^{ln} = (\delta_{ln}\delta_{ij} - \delta_{lj}\delta_{in})\mathcal J^{ln} = \delta_{ij}\mathcal J^{ll} - \mathcal J^{ji} = \mathcal J^{ij}, \\
> \varepsilon_{ikl}\varepsilon_{jml}\mathcal J^{km} &= \varepsilon_{lik}\varepsilon_{ljm}\mathcal J^{km} = (\delta_{ij}\delta_{km} - \delta_{im}\delta_{kj})\mathcal J^{km} = \delta_{ij}\mathcal J^{kk} - \mathcal J^{ji} = \mathcal J^{ij}, \\
> -\varepsilon_{ikl}\varepsilon_{jmk}\mathcal J^{lm} &= -\varepsilon_{kli}\varepsilon_{kjm}\mathcal J^{lm} = -(\delta_{lj}\delta_{im} - \delta_{lm}\delta_{ij})\mathcal J^{lm} = -\mathcal J^{ji} + \delta_{ij}\mathcal J^{ll} = \mathcal J^{ij},
> \end{aligned}
> $$
>
> where the first line used $\varepsilon_{ikl} = \varepsilon_{lik}$ (cyclic) and $\varepsilon_{jln} = -\varepsilon_{ljn}$, the others only cyclic permutations, and every line $\mathcal J^{kk} = 0$, $\mathcal J^{ji} = -\mathcal J^{ij}$. Hence $[J_i, J_j] = \frac i4\cdot4\,\mathcal J^{ij} = i\varepsilon_{ijk}J_k$ by step 1.
>
> **3. Rotations with boosts.** $[J_i, K_j] = \frac12\varepsilon_{ikl}[\mathcal J^{kl}, \mathcal J^{0j}]$, and the covariant relation with $(\mu\nu\rho\sigma) = (kl0j)$ gives, since $g^{l0} = g^{k0} = 0$,
>
> $$
> [\mathcal J^{kl}, \mathcal J^{0j}] = i\bigl(g^{l0}\mathcal J^{kj} - g^{k0}\mathcal J^{lj} - g^{lj}\mathcal J^{k0} + g^{kj}\mathcal J^{l0}\bigr) = i\bigl(\delta_{lj}\mathcal J^{k0} - \delta_{kj}\mathcal J^{l0}\bigr) = i\bigl(-\delta_{lj}K_k + \delta_{kj}K_l\bigr) .
> $$
>
> Contracting with $\frac12\varepsilon_{ikl}$: $[J_i, K_j] = \frac i2\bigl(-\varepsilon_{ikj}K_k + \varepsilon_{ijl}K_l\bigr) = \frac i2\bigl(\varepsilon_{ijk}K_k + \varepsilon_{ijk}K_k\bigr) = i\varepsilon_{ijk}K_k$, using $\varepsilon_{ikj} = -\varepsilon_{ijk}$ and renaming $l \to k$. So $\mathbf K$ is a vector under rotations.
>
> **4. Boosts with boosts.** With $(\mu\nu\rho\sigma) = (0i0j)$, $g^{i0} = g^{0j} = 0$, $g^{00} = 1$, $\mathcal J^{00} = 0$:
>
> $$
> [K_i, K_j] = [\mathcal J^{0i}, \mathcal J^{0j}] = i\bigl(g^{i0}\mathcal J^{0j} - g^{00}\mathcal J^{ij} - g^{ij}\mathcal J^{00} + g^{0j}\mathcal J^{i0}\bigr) = -i\,\mathcal J^{ij} = -i\varepsilon_{ijk}J_k .
> $$
>
> ⚑ By-product: the minus sign, $g^{00} = +1$ against $g^{ij} = -\delta_{ij}$, is the only place where the Minkowski signature enters → [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-1|Remark: Two boosts make a rotation]].
>
> **5. The reversed mixed commutator.** $[K_i, J_j] = -[J_j, K_i] = -i\varepsilon_{jik}K_k = i\varepsilon_{ijk}K_k$.
>
> ⚑ By-product: steps 6–7 below, the split into two commuting angular momenta, are the content of [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-7|Theorem §CB.4.7]], part 1, whose derivation uses them.
>
> **6. The two copies commute.** With $J_{\pm i} = \frac12(J_i \pm iK_i)$ and bilinearity, all four terms:
>
> $$
> [J_{+i}, J_{-j}] = \tfrac14\bigl([J_i, J_j] - i[J_i, K_j] + i[K_i, J_j] + [K_i, K_j]\bigr) = \tfrac14\bigl(i\varepsilon_{ijk}J_k + \varepsilon_{ijk}K_k - \varepsilon_{ijk}K_k - i\varepsilon_{ijk}J_k\bigr) = 0 ,
> $$
>
> using steps 2–5 term by term: $-i[J_i, K_j] = -i\cdot i\varepsilon_{ijk}K_k = \varepsilon_{ijk}K_k$; $i[K_i, J_j] = i\cdot i\varepsilon_{ijk}K_k = -\varepsilon_{ijk}K_k$; $[iK_i, -iK_j] = (i)(-i)[K_i, K_j] = [K_i, K_j] = -i\varepsilon_{ijk}J_k$.
>
> **7. Each copy is an angular momentum.** Same signs in both slots:
>
> $$
> [J_{\pm i}, J_{\pm j}] = \tfrac14\bigl([J_i, J_j] \pm i[J_i, K_j] \pm i[K_i, J_j] + (\pm i)^2[K_i, K_j]\bigr) = \tfrac14\bigl(i\varepsilon_{ijk}J_k \mp \varepsilon_{ijk}K_k \mp \varepsilon_{ijk}K_k + i\varepsilon_{ijk}J_k\bigr) = \tfrac i2\varepsilon_{ijk}\bigl(J_k \pm iK_k\bigr) = i\varepsilon_{ijk}J_{\pm k},
> $$
>
> with $(\pm i)\cdot i = \mp1$ in the two mixed terms and $(\pm i)^2\cdot(-i) = +i$ in the last; in the third step $\mp\frac12\varepsilon_{ijk}K_k = \frac i2\varepsilon_{ijk}(\pm iK_k)$.
>
> **8. Equivalence.** The change of basis is invertible over $\mathbb C$: $\mathbf J = \mathbf J_+ + \mathbf J_-$, $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$. Each of the fifteen commutators of the six $\mathcal J^{\mu\nu}$ is, up to sign, one of $[J_i, J_j]$, $[J_i, K_j]$, $[K_i, K_j]$, so the covariant relation, the $\mathbf J$, $\mathbf K$ relations and the $\mathbf J_\pm$ relations say the same thing (the converse direction is computed in [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-7|Theorem §CB.4.7]]).
>
> **What the derivation shows**
> - $\mathbf J$ closes on itself (the rotation subalgebra); $\mathbf K$ does not.
> - The split needs the complex combinations $\mathbf J \pm i\mathbf K$; with real coefficients no pair of commuting rotation algebras exists, because of the sign in step 4 (for $SO(4)$, where $[K_i, K_j] = +i\varepsilon_{ijk}J_k$, the real combinations $\frac12(\mathbf J \pm \mathbf K)$ do the job).
> - Used next: the classification of all finite-dimensional representations by two spins ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-15-2|Def. §CB.15.2]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-4|Theorem §CB.15.4]]).
>
> *Source: the user's write-up of PHY 513, Problem Set 5, Problem 1(a) (submitted) · the user's PHY 513 notes, Ch. 7 §7.4 (Derivation "The rotation–boost algebra and its complex split") · Yu §3.2, eqs. (3.39)–(3.41), (3.61)–(3.63), and Exercise 3.1 · the user's pre-course notes, §2.2 (Note "Deriving the component form")*

^der-cb-4-2c

*Uses:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]]

> [!remark] Remark: Where the Lorentz algebra is derived
> The three folded derivations under Theorem §CB.4.2 prove it: from the group law alone, hence in every representation at once (the user's PHY 513 notes, Ch. 7 §7.3; the same argument for the operators on states is Yu §3.2); by direct matrix computation in the vector representation (the user's submitted solution of PHY 513 Problem Set 4, Problem 5(a)); and the reduction to $\mathbf J$, $\mathbf K$ with the split into $\mathbf J_\pm$ (the user's submitted solution of Problem Set 5, Problem 1(a); Yu eqs. (3.39), (3.61)–(3.63) and Exercise 3.1). The finite statement behind the first route, that the generators of any representation transform as a tensor, is [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-4|Theorem §CB.4.4]]; what the $\mathbf J_\pm$ split buys, the classification of all finite-dimensional representations by two spins $(j_+, j_-)$, is [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]].
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.6; Ch. 7 §§7.3–7.4 · the user's write-ups of PHY 513 Problem Set 4, Problem 5(a), and Problem Set 5, Problem 1(a) (both submitted)*

^rem-cb-4-1

> [!definition] Definition §CB.4.3: Representation of the Lorentz Algebra
> Six matrices $D(\mathcal J^{\mu\nu}) = -D(\mathcal J^{\nu\mu})$ on a complex vector space $V$ that obey the covariant relation of [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]] form a **representation of the Lorentz algebra** on $V$ (a representation of a Lie algebra in the sense of [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-5|Def. §CB.2.5]]). Its rotation and boost generators are $J_i = \frac12\varepsilon_{ijk}D(\mathcal J^{jk})$ and $K_i = D(\mathcal J^{0i})$, and its complex combinations $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.3 (Principle "How the parameters enter"), §7.4 ("The rotation–boost algebra and its complex split") · PHY 513 Lecture 7, Part B ("All representations realize the abstract algebra") · PS §3.1, eqs. (3.13), (3.17) · Yu §3.2, eqs. (3.35)–(3.36)*

^def-cb-4-3

> [!theorem] Theorem §CB.4.4: The Generators Transform as a Tensor
> 1. For every representation $D$ and every $\Lambda \in SO^+(1,3)$,
>
> $$
> D(\Lambda)^{-1}\,D(\mathcal J^{\rho\sigma})\,D(\Lambda) = \Lambda^\rho{}_\mu\,\Lambda^\sigma{}_\nu\,D(\mathcal J^{\mu\nu}) .
> $$
>
> 2. In particular, for a rotation $R$ ($\Lambda^0{}_0 = 1$, $\Lambda^i{}_j = R_{ij}$), $\mathbf J$ and $\mathbf K$ are vector operators: $D(R)^{-1}J_iD(R) = R_{ij}J_j$ and $D(R)^{-1}K_iD(R) = R_{ij}K_j$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.3, eq. (gentensor) · Yu §3.1, eq. (3.22) (the same law for the operators on states)*

^thm-cb-4-4

> [!derivation]- Derivation
> **1. Part 1.** This is steps 1–4 of [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^der-cb-4-2|Derivation §CB.4.2 (from the group law)]]: conjugate the one-parameter subgroup $e^{s\omega'}$ by $\Lambda$, lower the indices of $\Lambda^{-1}\omega'\Lambda$ to get $\Lambda^\rho{}_\mu\,\omega'_{\rho\sigma}\,\Lambda^\sigma{}_\nu$, apply $D$ and compare the coefficients of $\omega'_{\rho\sigma}$ at first order in $s$. Nothing in those steps depends on $D$ beyond $D(\Lambda_1)D(\Lambda_2) = D(\Lambda_1\Lambda_2)$; the sign ambiguity of a two-valued $D$ (Theorem §CB.15.6) cancels between $D(\Lambda)^{-1}$ and $D(\Lambda)$.
>
> **2. K under a rotation.** Put $(\rho, \sigma) = (0, i)$ in part 1. Since $\Lambda^0{}_\mu = \delta^0{}_\mu$ for a rotation, only $\mu = 0$ survives, and then $\nu$ must be spatial ($D(\mathcal J^{00}) = 0$): $D(R)^{-1}K_iD(R) = \Lambda^i{}_j\,D(\mathcal J^{0j}) = R_{ij}K_j$.
>
> **3. J under a rotation.** With $J_i = \frac12\varepsilon_{ijk}D(\mathcal J^{jk})$ and part 1 with spatial labels,
>
> $$
> D(R)^{-1}J_iD(R) = \tfrac12\varepsilon_{ijk}R_{jl}R_{km}\,D(\mathcal J^{lm}) .
> $$
>
> **4. The ε–determinant identity.** For any $3\times3$ matrix, $\varepsilon_{ajk}R_{an}R_{jl}R_{km} = (\det R)\,\varepsilon_{nlm}$ (the determinant as a triple product). Multiply by $R_{in}$, sum over $n$, and use $R_{in}R_{an} = \delta_{ia}$ ($RR^{\mathsf T} = \mathbb 1$): $\varepsilon_{ijk}R_{jl}R_{km} = (\det R)\,R_{in}\varepsilon_{nlm}$. With $\det R = 1$, step 3 becomes $R_{in}\cdot\frac12\varepsilon_{nlm}D(\mathcal J^{lm}) = R_{in}J_n$.
>
> **What the derivation shows**
> - The label pair of a generator is a pair of spacetime indices: it transforms with $\Lambda^\rho{}_\mu\Lambda^\sigma{}_\nu$, whatever space $D$ acts on. That is why the index rules of special relativity may be used on generator labels ([[§C3.1 Index Slots, Rotations and Spin in Field Theory#^def-c3-1-1|Def. §C3.1.1]]).
> - Part 2 is the vector-operator law of Quantum Mechanics, now for matrices acting on the indices of a field and with $\mathbf K$ included ([[§C7.2 Tensor Operators and the Wigner–Eckart Theorem#^def-c7-2-1|QM Def. §C7.2.1]]). Under a boost $\mathbf J$ and $\mathbf K$ mix, because $\Lambda^0{}_i \ne 0$.
> - Used next: its first-order form is the algebra ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^rem-cb-4-2|Remark: The algebra is the infinitesimal tensor law]]); for the operators on states the same law is [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-4|Theorem §C3.4.4]].

^der-cb-4-4

*Uses:* [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^der-cb-4-2|Derivation §CB.4.2]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^def-cb-4-1|Def. §CB.4.1]], [[§C7.2 Tensor Operators and the Wigner–Eckart Theorem#^def-c7-2-1|QM Def. §C7.2.1]]

> [!remark] Remark: The algebra is the infinitesimal tensor law
> Put $\Lambda = 1 + \omega$ in Theorem §CB.4.4: the left side becomes $D(\mathcal J^{\rho\sigma}) + \frac i2\omega_{\alpha\beta}[D(\mathcal J^{\alpha\beta}), D(\mathcal J^{\rho\sigma})]$, the right side $D(\mathcal J^{\rho\sigma})$ plus $\omega$ acting on the two labels as on a two-index tensor, and equating them is the covariant relation of [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]] (steps 5–9 of its derivation). So "$[J^{\mu\nu}, J^{\rho\sigma}]$ is a combination of $g$'s and $J$'s" says no more than "the generators rotate into each other like an antisymmetric tensor". The algebra acting on itself in this way is its **adjoint representation**; for the Lorentz group it is the antisymmetric two-tensor, the representation of the field strength ([[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]]).
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.3 ("This is the Lorentz algebra: the infinitesimal form of the statement that the generators transform as a tensor")*

^rem-cb-4-2

> [!theorem] Theorem §CB.4.5: One-Dimensional Representations of the Lorentz Algebra Are Zero
> Every one-dimensional representation of the Lorentz algebra is zero: six numbers $D(\mathcal J^{\mu\nu})$ that obey the relations of [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]] all vanish.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.5 (Principle "Components and functions: the scalar field carries the trivial representation") · PHY 513, Problem Set 5, Problem 1(b) (spin 0: "the generators are numbers, which commute", as the user wrote it) · Yu §4.2.1, eq. (4.27)*

^thm-cb-4-5

> [!derivation]- Derivation
> **1. Numbers commute.** In one dimension the six generators are complex numbers, so every commutator vanishes.
>
> **2. The rotation generators vanish.** $[J_1, J_2] = iJ_3$, $[J_2, J_3] = iJ_1$, $[J_3, J_1] = iJ_2$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]]) with left sides $0$ give $\mathbf J = 0$.
>
> **3. The boost generators vanish.** $[J_1, K_2] = iK_3$, $[J_2, K_3] = iK_1$, $[J_3, K_1] = iK_2$ (the relation $[J_i, K_j] = i\varepsilon_{ijk}K_k$) with left sides $0$ give $\mathbf K = 0$.
>
> **What the derivation shows**
> - Only the brackets $[J_i, J_j]$ and $[J_i, K_j]$ are used: every generator is a commutator of two others, so a representation in which all generators commute, in particular every one-dimensional one, is zero (written here).
> - Its physical reading, the scalar field: [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-4|Theorem §C3.3.4]].

^der-cb-4-5

*Uses:* [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]]

## The Lorentz algebra: the split J± = ½(J ± iK) and the conjugation picture

> [!theorem] Theorem §CB.4.6: The Split of the Complexified Lorentz Algebra
> Let $J_i$, $K_i$ be the rotation and boost generators of the vector representation ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]), so that $-iJ_i$, $-iK_i$ are a basis of $\mathfrak{so}(1,3)$ and $J_i, K_i \in i\,\mathfrak{so}(1,3) \subset \mathfrak{so}(1,3)_{\mathbb C}$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-6|Theorem §CB.3.6]]). In $\mathfrak{so}(1,3)_{\mathbb C}$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-5|Theorem §CB.3.5]]) put
>
> $$
> J_{\pm i} = \tfrac12\bigl(J_i \pm iK_i\bigr) .
> $$
>
> 1. **Both directions.** $J_i = J_{+i} + J_{-i}$ and $K_i = -i\bigl(J_{+i} - J_{-i}\bigr)$; so $\{J_{+i}, J_{-i}\}$ is a complex basis of $\mathfrak{so}(1,3)_{\mathbb C}$, while no nonzero complex combination of the $J_{+i}$ alone lies in $\mathfrak{so}(1,3)$ or in $i\,\mathfrak{so}(1,3)$.
> 2. **Two commuting copies of 𝔰𝔩(2,ℂ).** $[J_{+i}, J_{+j}] = i\varepsilon_{ijk}J_{+k}$, $[J_{-i}, J_{-j}] = i\varepsilon_{ijk}J_{-k}$, $[J_{+i}, J_{-j}] = 0$. Hence $\mathfrak a_\pm = \operatorname{span}_{\mathbb C}\{J_{\pm i}\}$ are ideals ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-9|Def. §CB.3.9]]), $\mathfrak{so}(1,3)_{\mathbb C} = \mathfrak a_+ \oplus \mathfrak a_-$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-10|Def. §CB.3.10]]), and $J_{\pm i} \mapsto \frac12\sigma^i$ is an isomorphism $\mathfrak a_\pm \cong \mathfrak{sl}(2, \mathbb C) \cong \mathfrak{su}(2)_{\mathbb C}$, the complexified rotation algebra ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-5|Theorem §CB.3.5]]).
> 3. **The conjugation exchanges the copies.** The conjugation $c$ of $\mathfrak{so}(1,3)_{\mathbb C}$ with fixed set $\mathfrak{so}(1,3)$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]]) satisfies $c(J_{\pm i}) = -J_{\mp i}$, so $c(\mathfrak a_\pm) = \mathfrak a_\mp$, and
>
> $$
> \mathfrak{so}(1,3) = \{A + c(A) : A \in \mathfrak a_+\} .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4 (Derivation "The rotation–boost algebra and its complex split") · PHY 513, Problem Set 5, Problem 1(a) (as the user wrote it) · Woit, §40.2 (the split $A_j$, $B_j$ and $\mathfrak{so}(3,1)\otimes\mathbb C = \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$) · Yu, Exercise 3.1 · written here (parts 1 and 3)*

^thm-cb-4-6

> [!proof]- Proof
> *Source: the user's PHY 513 notes, Ch. 7 §7.4, Derivation "The rotation–boost algebra and its complex split" (the brackets of part 2, as in [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^der-cb-4-2c|Derivation §CB.4.2 (the J, K form and the J± split)]], steps 6–8) · P. Woit, Quantum Theory, Groups and Representations, §40.2 (the same split in the real basis $l_j = -iJ_j$, $k_j = -iK_j$; "this construction … requires that we complexify") (https://www.math.columbia.edu/~woit/QM/qmbook.pdf). Parts 1 and 3 are written here from Theorems §CB.3.4–§CB.3.6.*
>
> **Step 1** (where $J_i$, $K_i$ live). $-iJ_i$, $-iK_i$ are the generators $M^{jk}$, $M^{0i}$ of the vector representation ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]), a real basis of $\mathfrak{so}(1,3)$, hence a complex basis of $\mathfrak{so}(1,3)_{\mathbb C}$, which [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-5|Theorem §CB.3.5]] realizes inside $M_4(\mathbb C)$. So $J_i = i(-iJ_i)$, $K_i = i(-iK_i)$ lie in $i\,\mathfrak{so}(1,3)$, and $\{J_i, K_i\}$ is also a complex basis. Their brackets, computed as $4\times4$ matrices, are ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]])
>
> $$
> [J_i, J_j] = i\varepsilon_{ijk}J_k, \qquad [J_i, K_j] = i\varepsilon_{ijk}K_k, \qquad [K_i, J_j] = i\varepsilon_{ijk}K_k, \qquad [K_i, K_j] = -i\varepsilon_{ijk}J_k ,
> $$
>
> the third from the second by antisymmetry and $\varepsilon_{jik} = -\varepsilon_{ijk}$.
>
> **Step 2** (part 1: both directions). Adding and subtracting the definitions, $J_{+i} + J_{-i} = J_i$ and $J_{+i} - J_{-i} = iK_i$, so $K_i = -i(J_{+i} - J_{-i})$. The change of basis $\{J_i, K_i\} \leftrightarrow \{J_{+i}, J_{-i}\}$ is invertible over $\mathbb C$, so $\{J_{\pm i}\}$ is a complex basis of $\mathfrak{so}(1,3)_{\mathbb C}$.
>
> **Step 3** (part 2: the copies commute; user's notes, step 6). By bilinearity, all four terms, and Step 1:
>
> $$
> [J_{+i}, J_{-j}] = \tfrac14\bigl([J_i, J_j] - i[J_i, K_j] + i[K_i, J_j] + [K_i, K_j]\bigr) = \tfrac14\bigl(i\varepsilon_{ijk}J_k + \varepsilon_{ijk}K_k - \varepsilon_{ijk}K_k - i\varepsilon_{ijk}J_k\bigr) = 0 .
> $$
>
> **Step 4** (part 2: each copy is an angular momentum; user's notes, step 7). With the same sign in both slots, $(\pm i)^2 = -1$:
>
> $$
> [J_{\pm i}, J_{\pm j}] = \tfrac14\bigl([J_i, J_j] \pm i[J_i, K_j] \pm i[K_i, J_j] - [K_i, K_j]\bigr) = \tfrac14\bigl(2i\varepsilon_{ijk}J_k \mp 2\varepsilon_{ijk}K_k\bigr) = i\varepsilon_{ijk}\cdot\tfrac12\bigl(J_k \pm iK_k\bigr) = i\varepsilon_{ijk}J_{\pm k} ,
> $$
>
> using $\mp\varepsilon K_k = i\varepsilon(\pm iK_k)$.
>
> **Step 5** (part 2: ideals and the isomorphism). By Steps 3–4, $[\mathfrak a_\pm, \mathfrak a_\pm] \subset \mathfrak a_\pm$ and $[\mathfrak a_\mp, \mathfrak a_\pm] = 0$, so $[\mathfrak{so}(1,3)_{\mathbb C}, \mathfrak a_\pm] \subset \mathfrak a_\pm$: both are ideals ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-9|Def. §CB.3.9]]), and with Step 2 the space is their direct sum, a direct sum of Lie algebras ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-10|Def. §CB.3.10]]). The matrices $\tau^i = \frac12\sigma^i$ are a complex basis of the traceless $2\times2$ matrices $\mathfrak{sl}(2, \mathbb C)$ (three independent traceless matrices, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]]: complex dimension $3$) with $[\tau^i, \tau^j] = i\varepsilon_{ijk}\tau^k$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]]). The linear bijection $J_{\pm i} \mapsto \tau^i$ matches the brackets of Step 4 on a basis, hence everywhere: $\mathfrak a_\pm \cong \mathfrak{sl}(2, \mathbb C)$, which is $\mathfrak{su}(2)_{\mathbb C}$ by Theorem §CB.3.5.
>
> **Step 6** (part 3: the conjugation). $J_i, K_i \in i\,\mathfrak{so}(1,3)$, so $c(J_i) = -J_i$, $c(K_i) = -K_i$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-6|Theorem §CB.3.6]], 2). $c$ is conjugate-linear, so
>
> $$
> c(J_{\pm i}) = \tfrac12\bigl(c(J_i) \mp i\,c(K_i)\bigr) = \tfrac12\bigl(-J_i \pm iK_i\bigr) = -J_{\mp i},
> $$
>
> and $c$ maps the complex span $\mathfrak a_\pm$ onto $\mathfrak a_\mp$.
>
> **Step 7** (part 3: the real algebra). For $A \in \mathfrak a_+$, $c(A + cA) = cA + A$ ($c^2 = \mathbb 1$), so $A + cA \in \mathfrak{so}(1,3)$, the fixed set of $c$. The real-linear map $A \mapsto A + cA$ is injective: $A + cA = 0$ gives $A = -cA \in \mathfrak a_+ \cap \mathfrak a_- = \{0\}$. Both spaces have real dimension $6$, so it is onto: $\mathfrak{so}(1,3) = \{A + c(A) : A \in \mathfrak a_+\}$.
>
> **Step 8** (the rest of part 1). If $A \in \mathfrak a_+$ lies in $\mathfrak{so}(1,3)$, then $A = cA \in \mathfrak a_-$, so $A = 0$; if it lies in $i\,\mathfrak{so}(1,3)$, then $A = -cA \in \mathfrak a_-$, so again $A = 0$.
>
> **What the proof shows.**
> - ⚑ By-product: the split exists only after complexifying; neither copy contains a nonzero real Lorentz generator (Step 8). Each real generator is a pair $A + c(A)$, one component in each copy, tied together by conjugation: the "complex angles $\boldsymbol\theta \mp i\boldsymbol\eta$, complex conjugates of each other" of the user's notes, Ch. 7 §7.4.
> - The brackets were computed in the vector representation, but by [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]] they hold in every representation; that is [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-7|Theorem §CB.4.7]].

^pf-cb-4-6

*Uses:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-9|Def. §CB.3.9]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-10|Def. §CB.3.10]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-5|Theorem §CB.3.5]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-6|Theorem §CB.3.6]]

The representation-level statement, a pair of commuting angular momenta on a complex space, in the course's form (PHY 513, Problem Set 5, Problem 1(a), as the user wrote it), and the factorization of every Lorentz transformation that follows:

> [!theorem] Theorem §CB.4.7: A Representation of the Lorentz Algebra Is a Pair of Commuting Angular Momenta
> 1. If six matrices $D(\mathcal J^{\mu\nu})$ represent the Lorentz algebra on a complex vector space $V$, then $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ obey (the split computed in steps 6–7 of [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^der-cb-4-2c|Derivation §CB.4.2 (the J, K form)]])
>
> $$
> [J_{+i}, J_{+j}] = i\varepsilon_{ijk}J_{+k}, \qquad [J_{-i}, J_{-j}] = i\varepsilon_{ijk}J_{-k}, \qquad [J_{+i}, J_{-j}] = 0 .
> $$
>
> 2. Conversely, if two triples $A_i$, $B_i$ of matrices on $V$ obey $[A_i, A_j] = i\varepsilon_{ijk}A_k$, $[B_i, B_j] = i\varepsilon_{ijk}B_k$, $[A_i, B_j] = 0$, then $\mathbf J = \mathbf A + \mathbf B$, $\mathbf K = -i(\mathbf A - \mathbf B)$, i.e. $D(\mathcal J^{jk}) = \varepsilon_{jkl}J_l$, $D(\mathcal J^{0i}) = K_i$, is a representation of the Lorentz algebra, with $\mathbf J_+ = \mathbf A$, $\mathbf J_- = \mathbf B$. The two constructions are inverse to each other.
>
> The combinations $\mathbf J_\pm$ are not in the real Lorentz algebra $\mathfrak{so}(1,3)$ but in its complexification $\mathfrak{so}(1,3)_{\mathbb C}$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-6|Theorem §CB.4.6]]), and $D(\mathbf J_\pm)$ means the complex-linear extension of $D$; the correspondence is between representations on a *complex* vector space $V$, where $i\,D(\mathbf K)$ is defined ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-8|Theorem §CB.3.8]]).
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4 (Derivation "The rotation–boost algebra and its complex split": "The change of basis is invertible") · PHY 513, Problem Set 5, Problem 1(a) (as the user wrote it) · Yu, Exercise 3.1, eqs. (3.219)–(3.220)*

^thm-cb-4-7

> [!derivation]- Derivation
> **1. Part 1.** This is [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^der-cb-4-2c|Derivation §CB.4.2 (the J, K form and the J± split)]], steps 2–7, which used only the covariant relation, so it holds for the generators of any representation.
>
> **2. Converse, rotations with rotations.** Expand the commutator into its four terms; the two mixed ones vanish because $[A_i, B_j] = 0$ and $[B_i, A_j] = -[A_j, B_i] = 0$:
>
> $$
> [J_i, J_j] = [A_i + B_i, A_j + B_j] = [A_i, A_j] + [A_i, B_j] + [B_i, A_j] + [B_i, B_j] = i\varepsilon_{ijk}(A_k + B_k) = i\varepsilon_{ijk}J_k .
> $$
>
> **3. Rotations with boosts.** $[J_i, K_j] = -i[A_i + B_i, A_j - B_j] = -i\bigl([A_i, A_j] - [A_i, B_j] + [B_i, A_j] - [B_i, B_j]\bigr) = -i\bigl(i\varepsilon_{ijk}A_k - i\varepsilon_{ijk}B_k\bigr) = \varepsilon_{ijk}(A_k - B_k)$. Since $i\varepsilon_{ijk}K_k = i\varepsilon_{ijk}(-i)(A_k - B_k) = \varepsilon_{ijk}(A_k - B_k)$, this is $[J_i, K_j] = i\varepsilon_{ijk}K_k$.
>
> **4. Boosts with boosts.** $[K_i, K_j] = (-i)^2[A_i - B_i, A_j - B_j] = -\bigl([A_i, A_j] - [A_i, B_j] - [B_i, A_j] + [B_i, B_j]\bigr) = -i\varepsilon_{ijk}(A_k + B_k) = -i\varepsilon_{ijk}J_k$.
>
> **5. Back to the covariant form.** Steps 2–4 are the three relations of Theorem §CB.4.2 in $\mathbf J$, $\mathbf K$ form; by step 8 of Derivation §CB.4.2 (the J, K form) they are equivalent to the covariant relation for $D(\mathcal J^{jk}) = \varepsilon_{jkl}J_l$, $D(\mathcal J^{0i}) = K_i$ (step 1 there shows $\mathcal J^{jk} = \varepsilon_{jkl}J_l$ is the inverse of $J_i = \frac12\varepsilon_{ijk}\mathcal J^{jk}$).
>
> **6. Inverse constructions.** $\frac12(\mathbf J \pm i\mathbf K) = \frac12\bigl(\mathbf A + \mathbf B \pm i(-i)(\mathbf A - \mathbf B)\bigr) = \frac12\bigl(\mathbf A + \mathbf B \pm (\mathbf A - \mathbf B)\bigr)$, which is $\mathbf A$ for the upper sign and $\mathbf B$ for the lower. Conversely $\mathbf J_+ + \mathbf J_- = \mathbf J$ and $-i(\mathbf J_+ - \mathbf J_-) = -i(i\mathbf K) = \mathbf K$.
>
> **What the derivation shows**
> - To give a representation of the Lorentz algebra is exactly to give two commuting representations of the rotation algebra on the same space. The search for all representations becomes the search for pairs of angular momenta, which Quantum Mechanics has already solved.
> - The dictionary uses $i$: $\mathbf A$ and $\mathbf B$ are complex combinations of rotations and boosts, so this is a statement about the complexified algebra ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-1|Caution: The algebra decomposes; it is not "reducible"]]).
> - Used next: the factorization of $D(\Lambda)$ (Theorem §CB.4.8) and the representations $(j_+, j_-)$ (Def. §CB.15.2).

^der-cb-4-7

*Uses:* [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^der-cb-4-2c|Derivation §CB.4.2 (the J, K form and the J± split)]]

> [!theorem] Theorem §CB.4.8: Every Lorentz Transformation Factorizes
> In every finite-dimensional representation, with $\theta_i = \frac12\varepsilon_{ijk}\omega_{jk}$ and $\eta_i = \omega_{0i}$,
>
> $$
> D(e^{\omega}) = e^{-i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\eta\cdot\mathbf K} = e^{-i(\boldsymbol\theta - i\boldsymbol\eta)\cdot\mathbf J_+}\;e^{-i(\boldsymbol\theta + i\boldsymbol\eta)\cdot\mathbf J_-} ,
> $$
>
> and the two factors commute: a Lorentz transformation acts as two commuting "rotations" through the complex-conjugate angles $\boldsymbol\theta - i\boldsymbol\eta$ and $\boldsymbol\theta + i\boldsymbol\eta$. A rotation has real, equal angles in both; a boost has imaginary ones.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.2 (Principle "Every Lorentz transformation factorizes", eq. (lorentzfactor); checked numerically there) · PHY 513, Problem Set 5, Problem 1(b) (the substitution, as the user wrote it)*

^thm-cb-4-8

> [!derivation]- Derivation
> **1. The exponent in J, K.** By Def. §CB.4.1, $D(e^\omega) = \exp(-\frac i2\omega_{\mu\nu}D(\mathcal J^{\mu\nu}))$. The regrouping of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], $-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu} = -i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\eta\cdot\mathbf K$, is linear in the generators, so it holds with $D(\mathcal J^{\mu\nu})$ in place of $\mathcal J^{\mu\nu}$.
>
> **2. Substitute.** With $\mathbf J = \mathbf J_+ + \mathbf J_-$ and $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$ (Theorem §CB.4.7), the four terms are
>
> $$
> -i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\eta\cdot\mathbf K = -i\boldsymbol\theta\cdot\mathbf J_+ - i\boldsymbol\theta\cdot\mathbf J_- - \boldsymbol\eta\cdot\mathbf J_+ + \boldsymbol\eta\cdot\mathbf J_- ,
> $$
>
> using $-i\cdot(-i) = -1$. Collect: $-i\boldsymbol\theta\cdot\mathbf J_+ - \boldsymbol\eta\cdot\mathbf J_+ = -i(\boldsymbol\theta - i\boldsymbol\eta)\cdot\mathbf J_+$ (since $-i\cdot(-i\boldsymbol\eta) = -\boldsymbol\eta$) and $-i\boldsymbol\theta\cdot\mathbf J_- + \boldsymbol\eta\cdot\mathbf J_- = -i(\boldsymbol\theta + i\boldsymbol\eta)\cdot\mathbf J_-$ (since $-i\cdot i\boldsymbol\eta = \boldsymbol\eta$).
>
> **3. The exponential splits.** Write $X = -i(\boldsymbol\theta - i\boldsymbol\eta)\cdot\mathbf J_+$, $Y = -i(\boldsymbol\theta + i\boldsymbol\eta)\cdot\mathbf J_-$. Every $J_{+i}$ commutes with every $J_{-j}$, so $XY = YX$, and the binomial theorem holds for $(X + Y)^n$. Then
>
> $$
> e^{X + Y} = \sum_{n=0}^\infty\frac{1}{n!}\sum_{k=0}^n\binom nk X^kY^{n-k} = \sum_{k=0}^\infty\sum_{l=0}^\infty\frac{X^k}{k!}\frac{Y^l}{l!} = e^Xe^Y ,
> $$
>
> where $l = n - k$ and the double series may be rearranged because it converges absolutely (in any matrix norm, $\sum\lVert X\rVert^k\lVert Y\rVert^l/k!\,l! = e^{\lVert X\rVert + \lVert Y\rVert}$). The same argument gives $e^Xe^Y = e^{Y + X} = e^Ye^X$.
>
> **4. Rotations and boosts.** For $\boldsymbol\eta = 0$ both angles equal $\boldsymbol\theta$. For $\boldsymbol\theta = 0$ the angles are $-i\boldsymbol\eta$ and $+i\boldsymbol\eta$; in a spin-$j$ rotation matrix ([[§C5.3 The Angular-Momentum Spectrum and Rotation Matrices#^def-c5-3-1|QM Def. §C5.3.1]]) an imaginary angle turns $\cos$ and $\sin$ into $\cosh$ and $\sinh$, the rapidity's hyperbolic functions. ⚑ By-product: the two angles are complex conjugates of each other; that is the trace of the real group inside the complexified algebra, and it is why complex conjugation will exchange the two copies → [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-10|Theorem §CB.15.10]].
>
> **What the derivation shows**
> - $\boldsymbol\theta$, $\boldsymbol\eta$ are the parameters of a single exponential; a product of a rotation and a boost has other parameters, because $\mathbf J$ and $\mathbf K$ do not commute. It is $\mathbf J_+$ and $\mathbf J_-$ that commute, so the factorization is exact.
> - In $(j_+, j_-)$ (Def. §CB.15.2) the first factor is a spin-$j_+$ rotation matrix at the complex angle $\boldsymbol\theta - i\boldsymbol\eta$ and the second a spin-$j_-$ one at $\boldsymbol\theta + i\boldsymbol\eta$: every finite-dimensional Lorentz matrix is a product of two Wigner matrices at complex angles.
> - Used next: the spinor representations (Theorem §C3.2.1) and the field strength ([[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]]).

^der-cb-4-8

*Uses:* [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^def-cb-4-1|Def. §CB.4.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-7|Theorem §CB.4.7]]

> [!theorem] Theorem §CB.4.9: The Euclidean 𝔰𝔬(4) Splits Already over ℝ
> In $\mathfrak{so}(4)$ (real antisymmetric $4\times4$ matrices, coordinates $x^0, \dots, x^3$) let $J_i$ be the physicists' generators of rotations of $x^1, x^2, x^3$ and $\tilde K_i$ those of rotations in the $(x^0, x^i)$ planes, with signs chosen so that
>
> $$
> [J_i, J_j] = i\varepsilon_{ijk}J_k, \qquad [J_i, \tilde K_j] = i\varepsilon_{ijk}\tilde K_k, \qquad [\tilde K_i, \tilde K_j] = +i\varepsilon_{ijk}J_k .
> $$
>
> Then $A_{\pm i} = \frac12(J_i \pm \tilde K_i)$, with **no** $i$, obey $[A_{\pm i}, A_{\pm j}] = i\varepsilon_{ijk}A_{\pm k}$ and $[A_{+i}, A_{-j}] = 0$, and $-iA_{\pm i} \in \mathfrak{so}(4)$. So $\mathfrak{so}(4) = \mathfrak b_+ \oplus \mathfrak b_-$ with real ideals $\mathfrak b_\pm = \operatorname{span}_{\mathbb R}\{-iA_{\pm i}\} \cong \mathfrak{su}(2)$; and $\mathfrak{so}(4)_{\mathbb C} = (\mathfrak b_+)_{\mathbb C} \oplus (\mathfrak b_-)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$, with the conjugation of $\mathfrak{so}(4)_{\mathbb C}$ mapping each summand to itself.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.6 · Woit, §21.2 (the split $M = \frac12(L + K)$, $N = \frac12(L - K)$ of $\mathfrak{so}(4)$) · [[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-5|QM Theorem §C8.1.5]] (the same split for the Coulomb problem) · the explicit generators written here*

^thm-cb-4-9

> [!proof]- Proof
> *Source: P. Woit, Quantum Theory, Groups and Representations, §21.2 "so(4) symmetry and the Coulomb potential": from $[L_j, L_k] = i\epsilon_{jkl}L_l$, $[L_j, K_k] = i\epsilon_{jkl}K_l$, $[K_j, K_k] = i\epsilon_{jkl}L_l$ "one has" the two commuting copies $M$, $N$ (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the user's PHY 513 notes, Ch. 7 §7.4.6 ("That happens for $\mathfrak{so}(4)$, the Euclidean case, where the two copies are real"). The explicit choice of $J_i$, $\tilde K_i$ that realizes the hypothesis (Steps 1–3) is written here.*
>
> **Step 1** (a basis of $\mathfrak{so}(4)$). For $0 \le a, b \le 3$ let $E_{ab} = e_ae_b^{\mathsf T} - e_be_a^{\mathsf T}$, real antisymmetric; $\{E_{ab}\}_{a<b}$ is a basis of $\mathfrak{so}(4)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]]). Multiplying out with $e_b^{\mathsf T}e_c = \delta_{bc}$ (all four products in each of $E_{ab}E_{cd}$ and $E_{cd}E_{ab}$) gives
>
> $$
> [E_{ab}, E_{cd}] = \delta_{bc}E_{ad} - \delta_{ac}E_{bd} - \delta_{bd}E_{ac} + \delta_{ad}E_{bc} .
> $$
>
> **Step 2** (the generators). Put $J_1 = -iE_{23}$, $J_2 = -iE_{31}$, $J_3 = -iE_{12}$ (i.e. $J_i = -\frac i2\varepsilon_{ijk}E_{jk}$; then $-iJ_3 = -E_{12}$ is the generator $M^{12}$ of the active rotation of $(x^1, x^2)$, [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], so on $x^1, x^2, x^3$ these are the rotation generators $(J^k)_{lm} = -i\varepsilon^{klm}$ of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]]) and $\tilde K_i = -iE_{0i}$. Then by Step 1:
> - $[J_1, J_2] = (-i)^2[E_{23}, E_{31}] = -E_{21} = E_{12} = iJ_3$;
> - $[\tilde K_1, \tilde K_2] = (-i)^2[E_{01}, E_{02}] = -(-E_{12}) = E_{12} = iJ_3$;
> - $[J_1, \tilde K_2] = -[E_{23}, E_{02}] = -(-E_{03}) = E_{03} = i\tilde K_3$; $[J_2, \tilde K_1] = -[E_{31}, E_{01}] = -E_{03} = -i\tilde K_3$; $[J_1, \tilde K_1] = -[E_{23}, E_{01}] = 0$.
>
> **Step 3** (all index pairs). The cyclic relabelling $\pi$: $0 \mapsto 0$, $1 \mapsto 2$, $2 \mapsto 3$, $3 \mapsto 1$ is realized by the orthogonal permutation matrix $Pe_a = e_{\pi(a)}$, and $PE_{ab}P^{-1} = Pe_ae_b^{\mathsf T}P^{\mathsf T} - \cdots = E_{\pi(a)\pi(b)}$. So $X \mapsto PXP^{-1}$ (a Lie algebra automorphism, [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-14|Theorem §CB.2.14]], 4) sends $J_1 \mapsto J_2 \mapsto J_3 \mapsto J_1$ and $\tilde K_1 \mapsto \tilde K_2 \mapsto \tilde K_3 \mapsto \tilde K_1$, while $\varepsilon_{ijk}$ is invariant under cyclic relabelling. Applying it once and twice to the identities of Step 2, and using antisymmetry of the bracket for $[J_j, J_i]$, $[\tilde K_j, \tilde K_i]$, gives for all $i, j$
>
> $$
> [J_i, J_j] = i\varepsilon_{ijk}J_k, \qquad [J_i, \tilde K_j] = i\varepsilon_{ijk}\tilde K_k, \qquad [\tilde K_i, \tilde K_j] = +i\varepsilon_{ijk}J_k ,
> $$
>
> the hypothesis of the theorem. The sign of the last bracket differs from the Lorentz case ($-i\varepsilon_{ijk}J_k$, [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]]) because $(E_{0i})^2$ is negative on its plane, $(M^{0i})^2$ positive ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]).
>
> **Step 4** (the split with no $i$; Woit). With $A_{\pm i} = \frac12(J_i \pm \tilde K_i)$ and $[\tilde K_i, J_j] = -[J_j, \tilde K_i] = i\varepsilon_{ijk}\tilde K_k$:
>
> $$
> [A_{\pm i}, A_{\pm j}] = \tfrac14\bigl(i\varepsilon_{ijk}J_k \pm i\varepsilon_{ijk}\tilde K_k \pm i\varepsilon_{ijk}\tilde K_k + i\varepsilon_{ijk}J_k\bigr) = i\varepsilon_{ijk}A_{\pm k},
> $$
>
> $$
> [A_{+i}, A_{-j}] = \tfrac14\bigl(i\varepsilon_{ijk}J_k - i\varepsilon_{ijk}\tilde K_k + i\varepsilon_{ijk}\tilde K_k - i\varepsilon_{ijk}J_k\bigr) = 0 .
> $$
>
> **Step 5** (real ideals). $-iA_{\pm i} = \frac12(-iJ_i \mp i\tilde K_i) = \frac12\bigl(-\tfrac12\varepsilon_{ijk}E_{jk} \mp E_{0i}\bigr)$ is a real antisymmetric matrix, so $-iA_{\pm i} \in \mathfrak{so}(4)$. By Step 4, $[-iA_{\pm i}, -iA_{\pm j}] = -[A_{\pm i}, A_{\pm j}] = \varepsilon_{ijk}(-iA_{\pm k})$ and $[-iA_{+i}, -iA_{-j}] = 0$: $\mathfrak b_\pm = \operatorname{span}_{\mathbb R}\{-iA_{\pm i}\}$ are commuting subalgebras with the structure constants $\varepsilon_{ijk}$ of $\mathfrak{su}(2)$ in the basis $-i\tau^k$ (Theorem §CB.1.16), so $\mathfrak b_\pm \cong \mathfrak{su}(2)$. Since $J_i = A_{+i} + A_{-i}$ and $\tilde K_i = A_{+i} - A_{-i}$, the six $-iA_{\pm i}$ span the six $-iJ_i$, $-i\tilde K_i$, i.e. all of $\mathfrak{so}(4)$; six vectors spanning a six-dimensional space are a basis, so $\mathfrak{so}(4) = \mathfrak b_+ \oplus \mathfrak b_-$, and each $\mathfrak b_\pm$ is an ideal ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-9|Def. §CB.3.9]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-10|Def. §CB.3.10]]).
>
> **Step 6** (complexification and conjugation). Complex combinations of the basis of Step 5 give $\mathfrak{so}(4)_{\mathbb C} = (\mathfrak b_+)_{\mathbb C}\oplus(\mathfrak b_-)_{\mathbb C}$, and $(\mathfrak b_\pm)_{\mathbb C} \cong \mathfrak{su}(2)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-5|Theorem §CB.3.5]]). The conjugation fixes $\mathfrak b_\pm \subset \mathfrak{so}(4)$ and, being conjugate-linear, maps $(\mathfrak b_\pm)_{\mathbb C} = \mathfrak b_\pm + i\mathfrak b_\pm$ to itself.
>
> **What the proof shows.**
> - ⚑ By-product: one sign, $[\tilde K_i, \tilde K_j] = +i\varepsilon_{ijk}J_k$ versus $-i\varepsilon_{ijk}J_k$ for boosts, decides whether the split is real (here) or needs complexification (Theorem §CB.4.6).
> - The real split is why $SU(2)\times SU(2)$ covers $SO(4)$ and why the hydrogen spectrum is organized by two angular momenta ([[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-5|QM Theorem §C8.1.5]]; Woit §21.2).

^pf-cb-4-9

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-14|Theorem §CB.2.14]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-9|Def. §CB.3.9]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-10|Def. §CB.3.10]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-5|Theorem §CB.3.5]]

> [!theorem] Theorem §CB.4.10: 𝔰𝔬(1,3) and 𝔰𝔬(4) Are Two Real Forms of One Complex Algebra
> 1. $J_{\pm i} \mapsto A_{\pm i}$ extends to an isomorphism of complex Lie algebras $\mathfrak{so}(1,3)_{\mathbb C} \cong \mathfrak{so}(4)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-6|Theorem §CB.4.6]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-9|Theorem §CB.4.9]]); under it $\mathfrak{so}(1,3)$ and $\mathfrak{so}(4)$ are real forms ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-12|Def. §CB.3.12]]) of the same complex algebra.
> 2. Their conjugations differ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-13|Theorem §CB.3.13]]): that of $\mathfrak{so}(4)$ maps each $\mathfrak{sl}(2, \mathbb C)$ summand to itself, that of $\mathfrak{so}(1,3)$ exchanges the two.
> 3. $\mathfrak{so}(1,3)$ is simple as a real Lie algebra ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-11|Def. §CB.3.11]]). In particular $\mathfrak{so}(1,3) \not\cong \mathfrak{su}(2)\oplus\mathfrak{su}(2) \cong \mathfrak{so}(4)$: the real Lorentz algebra is **not** two copies of the rotation algebra; only its complexification is two copies of the complexified rotation algebra $\mathfrak{sl}(2, \mathbb C)$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §§7.4.1, 7.4.6 ("The accurate statement is that the algebra … decomposes") · Woit, §§21.2, 40.2 · Etingof, Lie Groups and Lie Algebras, §9.4, Remark 17.3 · written here (the proof)*

^thm-cb-4-10

> [!proof]- Proof
> *Written here, along the route recorded in batch 1 (an ideal of $\mathfrak{so}(1,3)$ complexifies to a $c$-stable ideal of $\mathfrak a_+\oplus\mathfrak a_-$). Context: P. Etingof, Lie Groups and Lie Algebras (MIT 18.755), §9.4 (real forms as fixed sets of antilinear involutions) and Remark 17.3 ("if $\mathfrak g$ is a simple complex Lie algebra regarded as a real Lie algebra then $\mathfrak g_{\mathbb C} \cong \mathfrak g\oplus\mathfrak g$ is semisimple but not simple") (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf); P. Woit, §40.2 and §21.2 for the two splits. No source found with this proof for $\mathfrak{so}(1,3)$ itself.*
>
> **Step 1** (part 1). $\{J_{\pm i}\}$ and $\{A_{\pm i}\}$ are complex bases of $\mathfrak{so}(1,3)_{\mathbb C}$ and $\mathfrak{so}(4)_{\mathbb C}$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-6|Theorem §CB.4.6]], 1; Step 5 of the proof of [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-9|Theorem §CB.4.9]]) with identical brackets: $[X_{\pm i}, X_{\pm j}] = i\varepsilon_{ijk}X_{\pm k}$, $[X_{+i}, X_{-j}] = 0$ for $X = J$ and for $X = A$. So the complex-linear bijection $\alpha : J_{\pm i} \mapsto A_{\pm i}$ preserves brackets on a basis, hence everywhere. Each of $\mathfrak{so}(1,3)$, $\mathfrak{so}(4)$ is a real form of its own complexification (the fixed set of $c$, [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]]), and $\alpha^{-1}(\mathfrak{so}(4))$ is a real form of $\mathfrak{so}(1,3)_{\mathbb C}$ isomorphic to $\mathfrak{so}(4)$; with Theorem §CB.4.6, 2, both are real forms of $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$.
>
> **Step 2** (part 2). Transported by $\alpha$, the conjugation of $\mathfrak{so}(4)_{\mathbb C}$ becomes $\sigma' = \alpha^{-1}c_{(4)}\alpha$, which maps each $\mathfrak a_\pm = \alpha^{-1}((\mathfrak b_\pm)_{\mathbb C})$ to itself (Theorem §CB.4.9, Step 6 of its proof), while the conjugation $c$ of $\mathfrak{so}(1,3)_{\mathbb C}$ exchanges $\mathfrak a_+$ and $\mathfrak a_-$ (Theorem §CB.4.6, 3). The two conjugations differ, as they must for non-isomorphic real forms ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-13|Theorem §CB.3.13]]); that the real forms are indeed non-isomorphic is Step 6.
>
> **Step 3** ($\mathfrak{sl}(2, \mathbb C)$ is simple). Basis $H = \operatorname{diag}(1, -1)$, $E = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $F = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$; multiplying out, $[H, E] = 2E$, $[H, F] = -2F$, $[E, F] = H$. Let $I \ne 0$ be an ideal and $X = aE + bH + cF \in I$, $X \ne 0$. Then $[E, X] = b[E, H] + c[E, F] = -2bE + cH \in I$ and $[E, [E, X]] = c[E, H] = -2cE \in I$. If $c \ne 0$, $E \in I$. If $c = 0$, $b \ne 0$: $[E, X] = -2bE$, so $E \in I$. If $b = c = 0$: $X = aE$, $a \ne 0$, so $E \in I$. In every case $E \in I$, then $H = [E, F] \in I$ and $F = -\frac12[H, F] \in I$: $I = \mathfrak{sl}(2, \mathbb C)$. It is not abelian, so it is simple ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-11|Def. §CB.3.11]]).
>
> **Step 4** (the ideals of $\mathfrak a_+\oplus\mathfrak a_-$). Let $I$ be an ideal of $\mathfrak a_+\oplus\mathfrak a_-$ (each $\mathfrak a_\pm \cong \mathfrak{sl}(2, \mathbb C)$, simple by Step 3, hence with trivial centre, since the centre is an ideal $\ne \mathfrak a_\pm$). If some $(x_+, x_-) \in I$ has $x_+ \ne 0$, pick $y \in \mathfrak a_+$ with $[y, x_+] \ne 0$; then $[(y, 0), (x_+, x_-)] = ([y, x_+], 0) \in I \cap \mathfrak a_+$, a nonzero ideal of $\mathfrak a_+$ (brackets with $\mathfrak a_-$ vanish), so $\mathfrak a_+ \subset I$. Likewise for the minus component. Hence $I \in \{0, \mathfrak a_+, \mathfrak a_-, \mathfrak a_+\oplus\mathfrak a_-\}$.
>
> **Step 5** (part 3: $\mathfrak{so}(1,3)$ is simple). Let $\mathfrak i$ be an ideal of $\mathfrak{so}(1,3)$ and $\mathfrak i_{\mathbb C} = \mathfrak i + i\mathfrak i \subset \mathfrak{so}(1,3)_{\mathbb C}$. It is a complex ideal: for $X, Y \in \mathfrak{so}(1,3)$, $A, B \in \mathfrak i$, $[X + iY, A + iB] = ([X, A] - [Y, B]) + i([X, B] + [Y, A]) \in \mathfrak i + i\mathfrak i$. It is $c$-stable: $c(A + iB) = A - iB$. By Step 4 it is $0$, $\mathfrak a_+$, $\mathfrak a_-$ or everything, and $c(\mathfrak a_\pm) = \mathfrak a_\mp \ne \mathfrak a_\pm$ excludes the middle two. Since $\mathfrak i = \mathfrak i_{\mathbb C} \cap \mathfrak{so}(1,3)$ (the $c$-fixed part of $A + iB$ is $A$), $\mathfrak i = 0$ or $\mathfrak i = \mathfrak{so}(1,3)$. And $\mathfrak{so}(1,3)$ is not abelian ($[-iJ_1, -iJ_2] = -iJ_3 \ne 0$). So it is simple.
>
> **Step 6** (not two rotation algebras). $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ has the ideal $\mathfrak{su}(2)\oplus0$, neither $0$ nor everything, so it is not simple, and by Step 5 it is not isomorphic to $\mathfrak{so}(1,3)$. By Theorem §CB.4.9 it is isomorphic to $\mathfrak{so}(4)$.
>
> **What the proof shows.**
> - ⚑ By-product: "the Lorentz algebra is two copies of the rotation algebra" is true only after complexification; the real algebra is simple, and the two copies are glued by the conjugation → [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^rem-cb-4-3|§CB.4, Remark: What the split does and does not mean]].
> - Simplicity of $\mathfrak{so}(1,3)$ is the hypothesis of Theorem §CB.5.23 (no finite-dimensional unitary representations).

^pf-cb-4-10

*Uses:* [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-11|Def. §CB.3.11]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-13|Theorem §CB.3.13]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-6|Theorem §CB.4.6]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-9|Theorem §CB.4.9]]

The course's remark on what the split does and does not mean (PHY 513 Lecture 7; the user's PHY 513 notes, Ch. 7 §7.4.6; see also [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-1|§C3.2, Caution: The algebra decomposes; it is not "reducible"]]):

> [!remark] Remark: What the split does and does not mean
> It is not a split of the Lorentz group into two independent rotation groups. For the Euclidean $\mathfrak{so}(4)$ the two copies are real and the group is (up to a sign) $SU(2)\times SU(2)$; here the copies need $i$, the two angles are tied by complex conjugation (Theorem §CB.4.8), and the group is $SL(2, \mathbb C)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]). In a finite-dimensional representation $\mathbf J_\pm$ can be chosen Hermitian, honest spin matrices, and boosts are real exponentials of them. In a unitary representation on a Hilbert space the opposite holds: $\mathbf J$ and $\mathbf K$ are both Hermitian, so $\mathbf J_+^\dagger = \mathbf J_-$, Hermitian conjugation exchanges the copies, and no finite spin labels either of them. That is why particle states are classified differently, by the little groups of Wigner ([[§C3.6★ Particle States and the Little Group#^def-c3-6-2|Def. §C3.6.2]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-4|Theorem §C3.6.4]]).
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.6 ("What the split does and does not mean")*

^rem-cb-4-3

> [!theorem] Theorem §CB.4.11: Two Real Forms of 𝔰𝔩(2,ℂ)
> $\mathfrak{su}(2)$ and $\mathfrak{sl}(2, \mathbb R)$ are real forms of $\mathfrak{sl}(2, \mathbb C)$, with conjugations $X \mapsto -X^\dagger$ and $X \mapsto \bar X$. They are not isomorphic: $\mathfrak{su}(2)$ has no element $X \ne 0$ for which $\mathrm{ad}_X$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-13|Def. §CB.2.13]]) has a nonzero real eigenvalue, while $H = \operatorname{diag}(1, -1) \in \mathfrak{sl}(2, \mathbb R)$ has $\mathrm{ad}_H$-eigenvalues $0, \pm2$. Moreover $\mathfrak{sl}(2, \mathbb R) \cong \mathfrak{so}(1,2)$ and $\mathfrak{su}(2) \cong \mathfrak{so}(3)$.
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), §9.4 (the same argument for $\mathfrak u(n) \not\cong \mathfrak{gl}(n, \mathbb R)$, via $\mathrm{ad}$) · Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §9 (real forms, Exercise 11) · written here (the details)*

^thm-cb-4-11

> [!proof]- Proof
> *Source: P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, §9.4: "$\mathfrak u(n) \not\cong \mathfrak{gl}_n(\mathbb R)$, since in the first algebra any element $x$ with nilpotent $\mathrm{ad}\,x$ must be zero, while in the second one it does not have to" (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf); Steps 2–3 run this argument with real eigenvalues of $\mathrm{ad}$ in place of nilpotency. The conjugations and the isomorphism with $\mathfrak{so}(1,2)$ are written here.*
>
> **Step 1** (the two conjugations). On $\mathfrak{sl}(2, \mathbb C)$ put $\sigma_1(X) = -X^\dagger$ and $\sigma_2(X) = \bar X$. Both map traceless matrices to traceless ones ($\operatorname{tr}X^\dagger = \operatorname{tr}\bar X = \overline{\operatorname{tr}X}$), are conjugate-linear and square to $\mathbb 1$. Brackets: $[\sigma_1X, \sigma_1Y] = X^\dagger Y^\dagger - Y^\dagger X^\dagger = (YX - XY)^\dagger = -[X, Y]^\dagger = \sigma_1[X, Y]$, and $\overline{XY - YX} = \bar X\bar Y - \bar Y\bar X$. Fixed sets: $-X^\dagger = X$ with $\operatorname{tr}X = 0$ is $\mathfrak{su}(2)$; $\bar X = X$ with $\operatorname{tr}X = 0$ is $\mathfrak{sl}(2, \mathbb R)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]]). By [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-13|Theorem §CB.3.13]] both are real forms of $\mathfrak{sl}(2, \mathbb C)$.
>
> **Step 2** (in $\mathfrak{su}(2)$, $\mathrm{ad}$ has no nonzero real eigenvalue). On $\mathfrak{su}(2)$ let $B(X, Y) = -\operatorname{tr}(XY)$. It is real: $\overline{\operatorname{tr}(XY)} = \operatorname{tr}((XY)^\dagger) = \operatorname{tr}(Y^\dagger X^\dagger) = \operatorname{tr}(YX) = \operatorname{tr}(XY)$ for anti-Hermitian $X$, $Y$. It is positive definite: $B(X, X) = -\operatorname{tr}(X^2) = \operatorname{tr}(X^\dagger X) = \sum_{ij}|X_{ij}|^2$. It is invariant: $B([Z, X], Y) + B(X, [Z, Y]) = -\operatorname{tr}(ZXY - XZY + XZY - XYZ) = -\operatorname{tr}(ZXY) + \operatorname{tr}(XYZ) = 0$ by cyclicity of the trace. So for $Z \in \mathfrak{su}(2)$, if $\mathrm{ad}_ZX = \lambda X$ with $\lambda \in \mathbb R$, $X \ne 0$ in $\mathfrak{su}(2)$:
>
> $$
> \lambda B(X, X) = B([Z, X], X) = -B(X, [Z, X]) = -\lambda B(X, X) \quad\Longrightarrow\quad \lambda = 0 .
> $$
>
> **Step 3** (in $\mathfrak{sl}(2, \mathbb R)$ it has). With $E$, $F$ as in Step 3 of the proof of [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-10|Theorem §CB.4.10]] (real matrices), $\mathrm{ad}_HE = 2E$, $\mathrm{ad}_HF = -2F$, $\mathrm{ad}_HH = 0$: eigenvalues $0, \pm2$. A Lie algebra isomorphism $f : \mathfrak{sl}(2, \mathbb R) \to \mathfrak{su}(2)$ would satisfy $\mathrm{ad}_{f(H)}f(E) = f([H, E]) = 2f(E)$ with $f(E) \ne 0$, contradicting Step 2. So $\mathfrak{su}(2) \not\cong \mathfrak{sl}(2, \mathbb R)$.
>
> **Step 4** ($\mathfrak{sl}(2, \mathbb R) \cong \mathfrak{so}(1,2)$). In $\mathfrak{so}(1,2)$, $\eta = \operatorname{diag}(1, -1, -1)$, the generators of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]] (same formula, three dimensions) are $M^{01} = e_0e_1^{\mathsf T} + e_1e_0^{\mathsf T}$, $M^{02} = e_0e_2^{\mathsf T} + e_2e_0^{\mathsf T}$, $M^{12} = e_2e_1^{\mathsf T} - e_1e_2^{\mathsf T}$, and multiplying out (with $e_a^{\mathsf T}e_b = \delta_{ab}$)
>
> $$
> [M^{01}, M^{02}] = -M^{12}, \qquad [M^{12}, M^{01}] = M^{02}, \qquad [M^{12}, M^{02}] = -M^{01} .
> $$
>
> In $\mathfrak{sl}(2, \mathbb R)$ put $B_1 = \frac12H$, $B_2 = \frac12(E + F)$, $R = \frac12(F - E)$. With $[H, E] = 2E$, $[H, F] = -2F$, $[E, F] = H$: $[B_1, B_2] = \frac14(2E - 2F) = -R$; $[R, B_1] = \frac14([F, H] - [E, H]) = \frac14(2F + 2E) = B_2$; $[R, B_2] = \frac14([F, E] - [E, F]) = -\frac12H = -B_1$. The linear bijection $B_1 \mapsto M^{01}$, $B_2 \mapsto M^{02}$, $R \mapsto M^{12}$ matches all brackets on a basis: an isomorphism.
>
> **Step 5** ($\mathfrak{su}(2) \cong \mathfrak{so}(3)$). This is [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]].
>
> **What the proof shows.**
> - Compactness is visible in the algebra: an invariant positive-definite form (Step 2) forbids real $\mathrm{ad}$-eigenvalues; a "boost" ($H$, or $M^{01}$) has them. The same test shows $\mathfrak{so}(1,3)$ has no invariant inner product → Theorem §CB.5.23.
> - ⚑ By-product: one complex algebra $\mathfrak{sl}(2, \mathbb C)$, two real forms: rotations of $\mathbb R^3$ and Lorentz transformations of $\mathbb R^{1,2}$.

^pf-cb-4-11

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-13|Theorem §CB.3.13]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-10|Theorem §CB.4.10]] (Step 3 of its proof), [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]]

## 𝔰𝔩(2,ℂ) as a real Lie algebra

> [!definition] Definition §CB.4.12: Underlying Real Lie Algebra
> The **underlying real Lie algebra** (realification) $\mathfrak h_{\mathbb R}$ of a complex Lie algebra $\mathfrak h$ is $\mathfrak h$ with scalars restricted to $\mathbb R$; $\dim_{\mathbb R}\mathfrak h_{\mathbb R} = 2\dim_{\mathbb C}\mathfrak h$. The Lie algebra of the matrix Lie group $SL(2, \mathbb C)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-3|Def. §C5a.4.3]]) is $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$, of real dimension $6$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]]).
>
> *Source: written here*

^def-cb-4-12

> [!theorem] Theorem §CB.4.13: The Real Lie Algebra of SL(2,ℂ) Is the Lorentz Algebra
> The differential ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]) of the covering $\pi : SL(2, \mathbb C) \to SO^+(1,3)$ of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]] is an isomorphism of real Lie algebras $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^def-cb-4-12|Def. §CB.4.12]]); in the conventions of Theorem §C5a.4.7 it sends $-\frac i2\sigma^k \mapsto -iJ_k$ and $-\frac12\sigma^k \mapsto -iK_k$.
>
> *Source: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], 3, differentiated · Yu, Exercise 3.7 · the user's PHY 513 notes, Ch. 8 §8.2 · conventions checked against [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]] and [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]] (batch 2)*

^thm-cb-4-13

> [!proof]- Proof
> *Source: the vault's [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], part 3 (from the user's PHY 513 notes, Ch. 8 §8.2, and Yu, Exercise 3.7), differentiated with [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]. Convention check (batch 2): Larsen's register, $\Lambda = e^{-i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\eta\cdot\mathbf K}$ with $-iJ_i = M^{jk}$ ($ijk$ cyclic) and $-iK_i = M^{0i}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]); the statement's two assignments are confirmed in Steps 2–3, so the statement stands unchanged.*
>
> **Step 1** (a real basis). $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ consists of the traceless complex $2\times2$ matrices ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]]); $\sigma^1, \sigma^2, \sigma^3$ are a complex basis of them, so the six matrices $-\frac i2\sigma^k$, $-\frac12\sigma^k$ are a real basis. Likewise $-iJ_k$, $-iK_k$ are a real basis of $\mathfrak{so}(1,3)$.
>
> **Step 2** (rotations). By Theorem §C5a.4.7, 3, $\pi(U) = \operatorname{diag}(1, R(U))$ for $U \in SU(2)$, and $R(e^{-is\sigma^k/2})$ is the rotation by $s$ about $x^k$ ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], 2), which in the vector representation is $e^{-isJ_k} = e^{sM^{ij}}$ ($ijk$ cyclic; [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], 3). By the formula of Theorem §CB.2.3,
>
> $$
> \pi_\ast\bigl(-\tfrac i2\sigma^k\bigr) = \frac{d}{ds}\pi\bigl(e^{-is\sigma^k/2}\bigr)\Big|_{s=0} = \frac{d}{ds}e^{-isJ_k}\Big|_{s=0} = -iJ_k .
> $$
>
> **Step 3** (boosts). By Theorem §C5a.4.7, 3, $\pi(e^{-\boldsymbol\eta\cdot\boldsymbol\sigma/2})$ is the pure boost $e^\omega$ with $\omega_{0i} = \eta_i$, $\omega_{ij} = 0$; for $\boldsymbol\eta = s\,\mathbf e_k$ this is $e^{sM^{0k}} = e^{-isK_k}$ (Def. §C1a.6.2: $-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu} = -i\boldsymbol\eta\cdot\mathbf K$). Hence
>
> $$
> \pi_\ast\bigl(-\tfrac12\sigma^k\bigr) = \frac{d}{ds}\pi\bigl(e^{-s\sigma^k/2}\bigr)\Big|_{s=0} = \frac{d}{ds}e^{-isK_k}\Big|_{s=0} = -iK_k .
> $$
>
> **Step 4** (isomorphism). $\pi_\ast$ is real-linear and preserves brackets (Theorem §CB.2.3) and maps the real basis of Step 1 onto the real basis of Step 1: it is bijective, hence an isomorphism of real Lie algebras $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-2|Def. §CB.2.2]]).
>
> **Step 5** (a check on brackets). $[-\frac i2\sigma^1, -\frac i2\sigma^2] = -\frac14[\sigma^1, \sigma^2] = -\frac14\cdot2i\sigma^3 = -\frac i2\sigma^3$, matching $[-iJ_1, -iJ_2] = -[J_1, J_2] = -iJ_3$; and $[-\frac12\sigma^1, -\frac12\sigma^2] = \frac14\cdot2i\sigma^3 = -(-\frac i2\sigma^3)$, matching $[-iK_1, -iK_2] = -[K_1, K_2] = iJ_3 = -(-iJ_3)$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]]).
>
> **What the proof shows.**
> - ⚑ By-product: in $\mathfrak{sl}(2, \mathbb C)$ a boost generator is a complex multiple of a rotation generator, $-\frac12\sigma^k = -i\bigl(-\frac i2\sigma^k\bigr)$. So multiplication by $i$ on $\mathfrak{sl}(2, \mathbb C)$ becomes, on $\mathfrak{so}(1,3)$, the real-linear map $-iJ_k \mapsto iK_k$, $-iK_k \mapsto -iJ_k$ (it squares to $-\mathbb 1$) — a complex structure on $\mathfrak{so}(1,3)$ that is invisible from its definition → Theorem §CB.14.1.
> - The opposite sign convention for $\mathbf K$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators|§C1a.6]], after Def. §C1a.6.2: some sources use $K^i = \mathcal J^{i0}$) would flip the second assignment.

^pf-cb-4-13

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-2|Def. §CB.2.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]]

> [!theorem] Theorem §CB.4.14: Real Forms Have the Same Representations
> If $\mathfrak g_1$ and $\mathfrak g_2$ are real forms of the same complex Lie algebra $\mathfrak h$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-12|Def. §CB.3.12]]), then restriction and complex-linear extension ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-8|Theorem §CB.3.8]]) give bijections between the representations of $\mathfrak g_1$ on complex spaces, the complex-linear representations of $\mathfrak h$, and the representations of $\mathfrak g_2$ on complex spaces, preserving invariant subspaces, irreducibility, direct sums and intertwiners. Example: the finite-dimensional complex representations of $\mathfrak{so}(1,3)$, $\mathfrak{so}(4)$, $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ and $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ correspond to one another (Theorems §CB.4.10, §CB.4.13).
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 5 §1, Prop. 5.5 (each correspondence) · Woit, §5.5 · written here (the composition)*

^thm-cb-4-14

> [!proof]- Proof
> *Written here as a composition of two instances of [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-8|Theorem §CB.3.8]] (B. C. Hall, An Elementary Introduction to Groups and Representations, Prop. 5.5, https://arxiv.org/abs/math-ph/0005032; P. Woit, §5.5, whose example is exactly this use: representations of $\mathfrak{su}(2)$ through $\mathfrak{sl}(2, \mathbb C)$).*
>
> **Step 1** (from $\mathfrak g_1$ to $\mathfrak h$). $\mathfrak g_1$ is a real form of $\mathfrak h$, so $X + iY \mapsto X + iY$ is an isomorphism $(\mathfrak g_1)_{\mathbb C} \cong \mathfrak h$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-12|Def. §CB.3.12]]). Composing with it, Theorem §CB.3.8 says: a representation $d$ of $\mathfrak g_1$ on a complex space $W$ extends uniquely to the complex-linear representation $\tilde d(X + iY) = d(X) + i\,d(Y)$ of $\mathfrak h$ ($X, Y \in \mathfrak g_1$), and every complex-linear representation of $\mathfrak h$ arises so, by restriction to $\mathfrak g_1 \subset \mathfrak h$.
>
> **Step 2** (from $\mathfrak h$ to $\mathfrak g_2$). The same for $\mathfrak g_2$: restriction of complex-linear representations of $\mathfrak h$ to $\mathfrak g_2$ is a bijection onto the representations of $\mathfrak g_2$ on complex spaces, with inverse the complex-linear extension.
>
> **Step 3** (composition). $d \mapsto \tilde d|_{\mathfrak g_2}$ is a bijection from representations of $\mathfrak g_1$ to representations of $\mathfrak g_2$ on the same space $W$, inverse to the analogous map in the other direction. Invariant subspaces, irreducibility, direct sums and intertwiners are preserved at each of the two steps (Theorem §CB.3.8, 2), hence by the composition.
>
> **Step 4** (the example). $\mathfrak{so}(1,3)$ and $\mathfrak{so}(4)$ are real forms of one complex algebra ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-10|Theorem §CB.4.10]], 1). A Lie algebra isomorphism $f : \mathfrak g \to \mathfrak g'$ turns representations of $\mathfrak g'$ into those of $\mathfrak g$ by $d' \mapsto d'\circ f$, bijectively and preserving all four structures; apply it to $\mathfrak{so}(4) \cong \mathfrak{su}(2)\oplus\mathfrak{su}(2)$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-9|Theorem §CB.4.9]]) and $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-13|Theorem §CB.4.13]]).
>
> **What the proof shows.**
> - Only the complex-linear algebra structure is transported; unitarity and integrability to a group are not (Remark below; [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-5-22|Theorem §CB.5.22]] uses this theorem together with the compact group to recover complete reducibility).
> - ⚑ By-product: the finite-dimensional representations of the Lorentz algebra are classified by those of $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$, i.e. by pairs of spins → [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-4|Theorem §CB.15.4]].

^pf-cb-4-14

*Uses:* [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-12|Def. §CB.3.12]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-8|Theorem §CB.3.8]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-9|Theorem §CB.4.9]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-10|Theorem §CB.4.10]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-13|Theorem §CB.4.13]]

> [!remark] Remark: What the correspondence does not transport
> Theorem §CB.4.14 transports the algebra of the representations, not unitarity and not the group: a representation of $\mathfrak{so}(4)$ that is unitary for $SU(2)\times SU(2)$ becomes a representation of $\mathfrak{so}(1,3)$ whose boosts are not unitary ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-11|Theorem §CB.15.11]]). Complete reducibility does survive, which is Weyl's unitary trick ([[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs|§CB.5]]): it needs the compact-group theorem of §CB.5, so it is stated there, after that theorem, and not here.

^rem-cb-4-4

> [!remark]- Connections
> - The same algebra, $\mathfrak{so}(4) \cong \mathfrak{su}(2)\oplus\mathfrak{su}(2)$ over $\mathbb R$, is the hidden symmetry of the hydrogen atom ([[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-5|QM Theorem §C8.1.5]]): there the split needs no $i$ (Theorem §CB.4.9), for the Lorentz algebra it does (Theorem §CB.4.10).
> - **Used in**: Theorem §CB.4.6 — [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-7|Theorem §CB.4.7]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-8|Theorem §CB.4.8]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-15-2|Def. §CB.15.2]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^rem-cb-15-2|§CB.15, Remark: What the labels (j₊, j₋) mean]], [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]]; Theorems §CB.4.9–§CB.4.10 — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-1|§C3.2, Caution: The algebra decomposes; it is not "reducible"]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^rem-cb-4-3|§CB.4, Remark: What the split does and does not mean]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-4|Theorem §CB.15.4]]; Theorem §CB.4.13 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-3|Def. §C5a.4.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]
