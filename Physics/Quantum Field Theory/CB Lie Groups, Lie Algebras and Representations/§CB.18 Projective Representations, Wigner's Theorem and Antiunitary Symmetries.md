---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.18
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.19★ The Poincaré Group and Induced Representations]] →

*Sources: R. Simon, N. Mukunda, S. Chaturvedi, V. Srinivasan, arXiv:0808.0779, §III (https://arxiv.org/abs/0808.0779) · V. Bargmann, J. Math. Phys. 5 (1964) 862 and Ann. of Math. 59 (1954) 1 · V. Moretti, arXiv:1508.06951, §3.6 (https://arxiv.org/abs/1508.06951) · B. C. Hall, Quantum Theory for Mathematicians, §16.7.3, §16.9.2 · Quantum Mechanics §C8.1★, §C8.3★ (Sakurai) · Yu Zhao-Huan, 量子场论讲义, §3.3.1, §9.1.2 · the user's PHY 513 notes, Ch. 7 §§7.2, 7.6 · the user's pre-course notes (Weinberg vol. 1, §2.2, App. 2.A; §2.7, App. 2.B, as cited there) · the rest written here.*

Why are the symmetries of quantum mechanics represented by unitary or antiunitary operators, why only up to a phase, and why does that allow, and require, the covering groups SU(2) and SL(2, ℂ)? States are rays, so a symmetry is a map of rays that preserves transition probabilities. Wigner's theorem lifts it to a unitary or antiunitary operator, unique up to a phase (decision SPEC-CB 2: proved here; Quantum Mechanics states it, [[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-1|QM Theorem §C8.1.1]]). A group of symmetries then becomes a projective representation, which for connected groups is unitary and, in finite dimension, lifts to a genuine representation of the universal cover. Groups containing time reversal need antiunitary elements, whose squares are $\pm1$. The section builds on [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings|§CB.2]] (universal covers, the Lie correspondence) and the course's projective representations ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-6|Def. §CB.9.6]]).

## Rays and Wigner's theorem

> [!definition] Definition §CB.18.1: Ray Space and Transition Probability
> For a complex Hilbert space $\mathcal H$, the **ray space** $P(\mathcal H)$ is the set of one-dimensional subspaces $[\psi] = \mathbb C\psi$, $\psi \ne 0$. The **transition probability** of two rays is $\bigl|\langle\psi, \phi\rangle\bigr|^2/(\|\psi\|^2\|\phi\|^2)$, independent of the representatives.
>
> *Source (planned): Woit, §7.4 · Quantum Mechanics §C8.1★*

^def-cb-18-1

> [!definition] Definition §CB.18.2: Wigner Symmetry
> A **Wigner symmetry** of $\mathcal H$ is a bijection $T : P(\mathcal H) \to P(\mathcal H)$ that preserves transition probabilities ([[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^def-cb-18-1|Def. §CB.18.1]]). An operator $U$ **induces** $T$ if $T[\psi] = [U\psi]$ for all $\psi \ne 0$.
>
> *Source (planned): Quantum Mechanics §C8.1★ · written here*

^def-cb-18-2

Antilinear and antiunitary operators and their structure, defined and proved in Quantum Mechanics:

![[§C8.3★ Time Reversal#^def-c8-3-1]]

![[§C8.3★ Time Reversal#^thm-c8-3-1]]

> [!theorem] Theorem §CB.18.3: Wigner's Theorem
> Every Wigner symmetry $T$ of a complex Hilbert space $\mathcal H$ ([[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^def-cb-18-2|Def. §CB.18.2]]) is induced by an operator $U$ that is either unitary or antiunitary ([[§C8.3★ Time Reversal#^def-c8-3-1|QM Def. §C8.3.1]]). $U$ is unique up to a phase $e^{i\alpha}$ among operators of the same kind. If $\dim\mathcal H \ge 2$ the kind (unitary or antiunitary) is determined by $T$, so $U$ is unique up to a phase; if $\dim\mathcal H = 1$, the only Wigner symmetry is the identity, induced by $\mathbb 1$ and by an antiunitary operator.
>
> *Source: R. Simon, N. Mukunda, S. Chaturvedi, V. Srinivasan, "Two elementary proofs of the Wigner theorem on symmetry in quantum mechanics", Phys. Lett. A 372 (2008) 6847, arXiv:0808.0779, §III, Steps 1–6 (https://arxiv.org/abs/0808.0779) · the original complete proof: V. Bargmann, "Note on Wigner's theorem on symmetry operations", J. Math. Phys. 5 (1964) 862–868 · Weinberg vol. 1, App. 2.A, as cited in the user's pre-course notes · the uniqueness written here · stated without proof in [[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-1|QM Theorem §C8.1.1]]*

^thm-cb-18-3

> [!proof]- Proof
> Notation: $\langle\cdot, \cdot\rangle$ is linear in the second slot; for unit vectors $P(\psi, \phi) = |\langle\psi, \phi\rangle|^2$ is the transition probability of [[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^def-cb-18-1|Def. §CB.18.1]]. If $V$ is unitary, $[\psi] \mapsto [V\psi]$ is a Wigner symmetry (it is a bijection of rays, and $|\langle V\psi, V\phi\rangle| = |\langle\psi, \phi\rangle|$), and a composite of Wigner symmetries is one. The route is that of Simon–Mukunda–Chaturvedi–Srinivasan: compose $T$ with unitary symmetries until it fixes a basis and the "equator" vectors of every pair of basis vectors; what is left is the identity or complex conjugation.
>
> Assume first $\dim\mathcal H \ge 2$. Fix an orthonormal basis $\{e_n\}_{n\in I}$ and one index $1 \in I$.
>
> **1. The images of the basis form an orthonormal basis.** Choose unit vectors $e'_n$ with $T[e_n] = [e'_n]$. Then $P(e'_m, e'_n) = P(e_m, e_n) = \delta_{mn}$, so $\{e'_n\}$ is orthonormal. It is complete: if $\chi \perp e'_n$ for all $n$ and $\|\chi\| = 1$, then $[\chi] = T[\psi]$ for a unit $\psi$ ($T$ is onto), and $|\langle e_n, \psi\rangle|^2 = P(e'_n, \chi) = 0$ for every $n$, so $\psi = 0$ by Parseval's identity, a contradiction.
>
> **2. Normalize: fix the basis rays.** Let $V\psi = \sum_n\langle e'_n, \psi\rangle e_n$. By step 1 and Parseval, $V$ is linear, isometric and onto: unitary, with $Ve'_n = e_n$. Put $T_1[\psi] = [V\psi']$ where $T[\psi] = [\psi']$, i.e. $T_1 = V\circ T$ on rays. $T_1$ is a Wigner symmetry with $T_1[e_n] = [e_n]$ for all $n$.
>
> **3. $T_1$ preserves the modulus of every coefficient.** Let $\psi = \sum_nc_ne_n$ be a unit vector and $T_1[\psi] = [\sum_nc'_ne_n]$. Then $|c'_n|^2 = P(e_n, \sum_mc'_me_m) = P(e_n, \psi) = |c_n|^2$, using $T_1[e_n] = [e_n]$. In particular $c'_n = 0$ wherever $c_n = 0$: $T_1$ maps rays in $\operatorname{span}\{e_j, e_k\}$ to rays in the same span.
>
> **4. The equator of a pair.** For $j \ne k$ and $\varphi \in \mathbb R$ put $u_{jk}(\varphi) = \frac1{\sqrt2}(e_j + e^{i\varphi}e_k)$. By step 3, $T_1[u_{jk}(\varphi)] = [ae_j + be_k]$ with $|a| = |b| = \frac1{\sqrt2}$; multiplying the representative by $|a|/a$ makes the first coefficient positive, so $T_1[u_{jk}(\varphi)] = [u_{jk}(f(\varphi))]$ for a unique $f(\varphi) \bmod 2\pi$. Now
>
> $$
> P\bigl(u_{jk}(\varphi_1), u_{jk}(\varphi_2)\bigr) = \tfrac14\bigl|1 + e^{i(\varphi_2 - \varphi_1)}\bigr|^2 = \tfrac12\bigl(1 + \cos(\varphi_1 - \varphi_2)\bigr),
> $$
>
> so preservation of transition probabilities reads $\cos(f(\varphi_1) - f(\varphi_2)) = \cos(\varphi_1 - \varphi_2)$ for all $\varphi_1, \varphi_2$ (Simon et al., eqs. (3.8)–(3.9)).
>
> **5. $f$ is a rotation or a reflection of the circle.** Let $\beta = f(0)$. With $\varphi_2 = 0$: $\cos(f(\varphi) - \beta) = \cos\varphi$, so $f(\varphi) - \beta \equiv s(\varphi)\,\varphi$ with $s(\varphi) \in \{\pm1\}$. Set $\epsilon = s(\pi/2)$, so $f(\pi/2) \equiv \beta + \epsilon\pi/2$. With $\varphi_2 = \pi/2$: $\cos(s(\varphi)\varphi - \epsilon\frac\pi2) = \cos(\varphi - \frac\pi2) = \sin\varphi$. For $\epsilon = \pm1$, $\cos(x - \epsilon\frac\pi2) = \epsilon\sin x$, so the left side is $\epsilon\sin(s(\varphi)\varphi) = \epsilon s(\varphi)\sin\varphi$. Hence $s(\varphi) = \epsilon$ whenever $\sin\varphi \ne 0$; if $\sin\varphi = 0$, then $\varphi \equiv 0$ or $\pi$ and $s(\varphi)\varphi \equiv \epsilon\varphi$ anyway. So, writing $\beta_{jk}$, $\epsilon_{jk}$ for the pair,
>
> $$
> T_1[u_{jk}(\varphi)] = [u_{jk}(\beta_{jk} + \epsilon_{jk}\varphi)] \qquad (\epsilon_{jk} = \pm1) .
> $$
>
> Since $u_{kj}(\varphi) = e^{i\varphi}u_{jk}(-\varphi)$, the two orders of a pair are related by $\beta_{kj} = -\beta_{jk}$, $\epsilon_{kj} = \epsilon_{jk}$.
>
> **6. Remove the phases of the pairs (1, k).** Let $D$ be the diagonal unitary $De_n = e^{-i\delta_n}e_n$ with $\delta_1 = 0$ and $\delta_k = \beta_{1k}$ ($k \ne 1$), and $T_2 = D\circ T_1$. Still $T_2[e_n] = [e_n]$, so step 3 holds for $T_2$. Since $D\,u_{jk}(\chi) = \frac1{\sqrt2}(e^{-i\delta_j}e_j + e^{i\chi - i\delta_k}e_k) = e^{-i\delta_j}u_{jk}(\chi + \delta_j - \delta_k)$,
>
> $$
> T_2[u_{jk}(\varphi)] = [u_{jk}(\beta'_{jk} + \epsilon_{jk}\varphi)], \qquad \beta'_{jk} = \beta_{jk} + \delta_j - \delta_k, \qquad \beta'_{1k} = 0 .
> $$
>
> **7. All the remaining phases vanish.** (If $\dim\mathcal H = 2$ the only pair is $(1, k)$, settled in step 6.) Let $j, k, 1$ be distinct and $r = \frac1{\sqrt3}(e_1 + e_j + e_k)$, a vector with real coefficients. By step 3, $T_2[r] = [\frac1{\sqrt3}\sum_{n\in\{1,j,k\}}e^{i\eta_n}e_n]$ for some phases $\eta_n$. For a pair $(a, b)$ from $\{1, j, k\}$:
>
> $$
> P\bigl(u_{ab}(\varphi), r\bigr) = \tfrac16\bigl|1 + e^{-i\varphi}\bigr|^2 = \tfrac13(1 + \cos\varphi), \qquad P\bigl(u_{ab}(\beta'_{ab} + \epsilon_{ab}\varphi), r''\bigr) = \tfrac16\bigl|e^{i\eta_a} + e^{-i(\beta'_{ab} + \epsilon_{ab}\varphi)}e^{i\eta_b}\bigr|^2 = \tfrac13\bigl(1 + \cos(\eta_b - \eta_a - \beta'_{ab} - \epsilon_{ab}\varphi)\bigr),
> $$
>
> with $r''$ the representative of $T_2[r]$ above. These are equal; at $\varphi = 0$ the first is $\frac23$, so $\cos(\eta_b - \eta_a - \beta'_{ab}) = 1$ and $\beta'_{ab} \equiv \eta_b - \eta_a$. For $(a, b) = (1, j)$ and $(1, k)$, step 6 gives $\eta_j = \eta_1 = \eta_k$; then for $(j, k)$, $\beta'_{jk} \equiv \eta_k - \eta_j = 0$. With $\beta'_{k1} = -\beta'_{1k} = 0$: $T_2[u_{jk}(\varphi)] = [u_{jk}(\epsilon_{jk}\varphi)]$ for every pair. (Simon et al. use one real vector with all coefficients nonzero, their eq. (3.18); a three-term vector for each pair does the same job and works for any orthonormal basis, also a non-countable one.)
>
> **8. Products of two coefficients.** Let $\psi = \sum_nc_ne_n$ be a unit vector, $T_2[\psi] = [\sum_nc''_ne_n]$ with $|c''_n| = |c_n|$ (step 3). For $j \ne k$,
>
> $$
> P(u_{jk}(\varphi), \psi) = \tfrac12\bigl|c_j + e^{-i\varphi}c_k\bigr|^2 = \tfrac12\bigl(|c_j|^2 + |c_k|^2\bigr) + \operatorname{Re}\bigl(e^{-i\varphi}\,\bar c_jc_k\bigr),
> $$
>
> and the same expression with $c''$ and $\epsilon_{jk}\varphi$ for the images (step 7). With $w = \bar c_jc_k$, $w'' = \bar c''_jc''_k$ and $|c''_n| = |c_n|$, equality for all $\varphi$ reads $\operatorname{Re}w\cos\varphi + \operatorname{Im}w\sin\varphi = \operatorname{Re}w''\cos\varphi + \epsilon_{jk}\operatorname{Im}w''\sin\varphi$. At $\varphi = 0$ and $\varphi = \frac\pi2$: $\operatorname{Re}w'' = \operatorname{Re}w$ and $\epsilon_{jk}\operatorname{Im}w'' = \operatorname{Im}w$. So
>
> $$
> \bar c''_jc''_k = \bar c_jc_k \ \text{ if } \epsilon_{jk} = +1, \qquad \bar c''_jc''_k = c_j\bar c_k \ \text{ if } \epsilon_{jk} = -1 \qquad \text{(Simon et al., eq. (3.24))} .
> $$
>
> **9. One sign for all pairs.** Let $j, k, \ell$ be distinct (if $\dim\mathcal H = 2$ there is only one pair and nothing to show). For any vector, $w_{jk}w_{k\ell}w_{\ell j} = \bar c_jc_k\,\bar c_kc_\ell\,\bar c_\ell c_j = |c_jc_kc_\ell|^2$ is real and $\ge 0$, for $c$ and for $c''$ alike. Take $\psi = \frac1{\sqrt3}(e_j + \zeta e_k + \zeta^2e_\ell)$, $\zeta = e^{2\pi i/3}$. Then $w_{jk} = \zeta/3$, $w_{k\ell} = \bar\zeta\zeta^2/3 = \zeta/3$, $w_{\ell j} = \bar\zeta^2/3 = \zeta/3$ (as $\zeta^3 = 1$). By step 8 each $w''$ is $\zeta/3$ or $\bar\zeta/3$ according to the sign of its pair; if $p$ of the three signs are $+1$, $w''_{jk}w''_{k\ell}w''_{\ell j} = \zeta^p\bar\zeta^{3-p}/27 = \zeta^{2p}/27$. This is real and positive only if $3 \mid 2p$, i.e. $p = 0$ or $p = 3$: the three signs are equal (Simon et al., Step 6, with this vector made explicit). Two pairs sharing an index lie in one triple; two disjoint pairs $(j, k)$, $(\ell, m)$ both share an index with $(j, \ell)$. So $\epsilon_{jk} = \epsilon$ for all pairs.
>
> **10. What is left is the identity or complex conjugation.** Let $\psi = \sum c_ne_n$ be a unit vector and pick $m$ with $c_m \ne 0$. If $\epsilon = +1$: $\bar c''_mc''_k = \bar c_mc_k$ for all $k$ (for $k = m$ this is $|c''_m| = |c_m|$), so $c''_k = c_k\,\bar c_m/\bar c''_m = \tau c_k$ with $\tau = c''_m/c_m$, $|\tau| = 1$ (since $\bar c_m/\bar c''_m = 1/\bar\tau = \tau$). Hence $T_2[\psi] = [\psi]$. If $\epsilon = -1$: $\bar c''_mc''_k = c_m\bar c_k$, so $c''_k = \tau'\bar c_k$ with $\tau' = c_m/\bar c''_m$, $|\tau'| = 1$, and $T_2[\psi] = [K\psi]$, $K$ the complex conjugation in the basis $\{e_n\}$ ([[§C8.3★ Time Reversal#^def-c8-3-1|QM Def. §C8.3.1]]).
>
> **11. Existence.** $T_2 = D\circ V\circ T$ on rays, so for unit $\psi$, $T[\psi] = [V^{-1}D^{-1}\psi]$ or $T[\psi] = [V^{-1}D^{-1}K\psi]$; both operators commute with multiplication by positive numbers, so the same holds for every $\psi \ne 0$. $U = V^{-1}D^{-1}$ is unitary; $U = V^{-1}D^{-1}K$ is antiunitary ($K$ is antiunitary and a unitary times an antiunitary operator is antiunitary, [[§C8.3★ Time Reversal#^thm-c8-3-1|QM Theorem §C8.3.1]], 1–2).
>
> **12. Uniqueness.** Let $U$, $U'$ both induce $T$, each unitary or antiunitary, and $A = U'^{-1}U$: linear if they are of the same kind, antilinear otherwise (QM Theorem §C8.3.1, 2), isometric, and $[A\psi] = [\psi]$, i.e. $A\psi = \lambda(\psi)\psi$ with $|\lambda(\psi)| = 1$. For linearly independent $\psi$, $\chi$: $\lambda(\psi + \chi)(\psi + \chi) = A(\psi + \chi) = \lambda(\psi)\psi + \lambda(\chi)\chi$, so $\lambda(\psi) = \lambda(\psi + \chi) = \lambda(\chi)$. For dependent nonzero $\psi$, $\chi$ pick $\xi$ independent of both ($\dim\mathcal H \ge 2$): $\lambda(\psi) = \lambda(\xi) = \lambda(\chi)$. So $\lambda$ is a constant. If $A$ were antilinear, $\lambda\,i\psi = A(i\psi) = -iA\psi = -i\lambda\psi$ would force $\lambda = 0$; so $A$ is linear, the two operators are of the same kind, and $A = \lambda\mathbb 1$, $U = \lambda U'$.
>
> **13. Dimension one.** $\mathcal H = \mathbb C\psi_0$ has one ray, so $T$ is the identity. It is induced by $c\psi_0 \mapsto c\psi_0$ (unitary) and by $c\psi_0 \mapsto \bar c\psi_0$ (antiunitary). Two operators of the same kind differ by $A = U'^{-1}U$ linear on $\mathbb C\psi_0$, i.e. multiplication by a number of modulus $1$.
>
> **What the proof shows**
> - The whole content of "preserving transition probabilities" is used on three kinds of vectors only: basis vectors (step 1), equators of pairs (steps 4–7) and three-term vectors (steps 7, 9). The choice between unitary and antiunitary is the sign $\epsilon$ of step 5, a rotation or a reflection of each equator circle, and step 9 shows that one sign governs all pairs.
> - The sign is intrinsic: the triple product $\langle\psi_1, \psi_2\rangle\langle\psi_2, \psi_3\rangle\langle\psi_3, \psi_1\rangle$ of three rays is preserved by a unitary and conjugated by an antiunitary operator (Bargmann 1964, §1.5); step 9 is this invariant at work.
> - ⚑ By-product: $U$ is fixed only up to a phase, and that phase is what makes a group of symmetries a projective representation ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-6|Def. §CB.9.6]], [[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-1|QM Theorem §C8.1.1]], 3).
> - No continuity, separability or dimension bound was used beyond $\dim\mathcal H \ge 2$ for the uniqueness of the kind. Used next: Theorem §CB.18.4 (connected groups act unitarily).

^pf-cb-18-3

*Uses:* [[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^def-cb-18-1|Def. §CB.18.1]], [[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^def-cb-18-2|Def. §CB.18.2]], [[§C8.3★ Time Reversal#^def-c8-3-1|QM Def. §C8.3.1]], [[§C8.3★ Time Reversal#^thm-c8-3-1|QM Theorem §C8.3.1]]

The statement in Quantum Mechanics:

![[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-1]]

## Projective representations

The course's definition, stated in [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan|§CB.9]], where two-valued representations first appear (half-integer spin):

![[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-6]]

> [!theorem] Theorem §CB.18.4: Connected Groups of Symmetries Act by Unitaries
> Let $G$ be a connected matrix Lie group and $g \mapsto T(g)$ a homomorphism into the group of Wigner symmetries of $\mathcal H$. Then every $T(g)$ is induced by a unitary operator. So a group of symmetries containing an antiunitary one (time reversal) is not connected.
>
> *Source: written here · the same argument: V. Moretti, arXiv:1508.06951, Remark 133(d)*

^thm-cb-18-4

> [!proof]- Proof
> **1. Squares are unitary.** If $U$ is unitary or antiunitary, $U^2$ is unitary: a product of two antiunitary operators is linear and preserves inner products, since $\langle U^2\psi, U^2\phi\rangle = \overline{\langle U\psi, U\phi\rangle} = \overline{\overline{\langle\psi, \phi\rangle}} = \langle\psi, \phi\rangle$.
>
> **2. Every element is a product of squares.** By [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]], 3, $g = e^{X_1}\cdots e^{X_k}$ with $X_i \in \mathfrak g$, and $e^{X_i} = (e^{X_i/2})^2$ (Theorem §CB.1.3, 3).
>
> **3. Conclusion.** Choose for each $e^{X_i/2}$ an inducing operator $U_i$ (Theorem §CB.18.3). Then $T(e^{X_i}) = T(e^{X_i/2})^2$ is induced by $U_i^2$, unitary by step 1, and $T(g)$ by the product $U_1^2\cdots U_k^2$, unitary. If $T(g)$ is induced by a unitary, it is not induced by an antiunitary (uniqueness in Theorem §CB.18.3, $\dim\mathcal H \ge 2$).

^pf-cb-18-4

> [!definition] Definition §CB.18.5: Lift of a Projective Representation
> Let $p : \tilde G \to G$ be a covering homomorphism ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-15|Def. §CB.2.15]]) and $U$ a projective representation of $G$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-6|Def. §CB.9.6]]). A **lift** of $U$ to $\tilde G$ is a genuine continuous representation $\Sigma$ of $\tilde G$ with $U(p(x)) = c(x)\Sigma(x)$, $|c(x)| = 1$, for all $x \in \tilde G$.
>
> *Source (planned): written here*

^def-cb-18-5

> [!theorem] Theorem §CB.18.6: Finite-Dimensional Projective Representations Lift to the Universal Cover
> Let $G$ be a connected matrix Lie group with universal covering group $p : \tilde G \to G$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-15|Def. §CB.2.15]]), and $W$ finite-dimensional. Every continuous homomorphism $\Pi : G \to PGL(W) = GL(W)/\mathbb C^\times\mathbb 1$ (quotient topology) has a lift to a continuous representation $\Sigma : \tilde G \to SL(W)$, i.e. $[\Sigma(x)] = \Pi(p(x))$ for all $x \in \tilde G$ (for a unitary $\Pi$ this is [[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^def-cb-18-5|Def. §CB.18.5]]), and the lift into $SL(W)$ is unique (two lifts differ by a continuous homomorphism $\tilde G \to \{\zeta : \zeta^{\dim W} = 1\}$, constant on the connected $\tilde G$); if the projective representation is unitary, so is $\Sigma$. Instances: $SO(3)$ with $\tilde G = SU(2)$, $SO^+(1,3)$ with $\tilde G = SL(2, \mathbb C)$.
>
> *Source: B. C. Hall, Quantum Theory for Mathematicians (Springer GTM 267, 2013), §16.7.3, Prop. 16.46 and Thm. 16.47 (the unitary case), with the conjugation device of the proof of Prop. 16.44 · the extension to $PGL(W)$ (steps 1–3) written here · the rotation case: [[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^thm-cb-18-7|Theorem §CB.18.7]]*

^thm-cb-18-6

> [!proof]- Proof
> Let $n = \dim W$, $\mathfrak g$ and $\tilde{\mathfrak g}$ the Lie algebras of $G$ and $\tilde G$, and $p_\ast : \tilde{\mathfrak g} \to \mathfrak g$ the differential of $p$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]). For $g \in G$ let $U_g \in GL(W)$ be any representative of $\Pi(g)$. The route is Hall's: turn $\Pi$ into a genuine representation by conjugation, "de-projectivize" its differential by making it traceless, integrate on $\tilde G$.
>
> **1. Conjugation turns Π into a genuine representation.** $\operatorname{Ad} : GL(W) \to GL(\mathfrak{gl}(W))$, $\operatorname{Ad}(A)X = AXA^{-1}$, is a continuous homomorphism. Its kernel is $\mathbb C^\times\mathbb 1$: if $AX = XA$ for all $X$, then $A$ commutes with every matrix, hence is a multiple of $\mathbb 1$ ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-6|Theorem §CB.6.6]], the defining representation of $GL(W)$ being irreducible). So $\operatorname{Ad}$ is constant on the cosets of $\mathbb C^\times\mathbb 1$ and defines a continuous injective homomorphism of $PGL(W)$ (universal property of the quotient topology), and $\Psi(g)X = U_gXU_g^{-1}$ is a well-defined Lie group homomorphism $\Psi : G \to GL(\mathfrak{gl}(W))$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]]). (Hall uses the same map $C_U$ in the proof of Prop. 16.44, for $PU(V)$.)
>
> **2. Its differential consists of derivations.** Let $\psi = \Psi_\ast$, $\psi(X) = \frac{d}{ds}\Psi(e^{sX})\big|_{s=0}$, a Lie algebra homomorphism $\mathfrak g \to \mathfrak{gl}(\mathfrak{gl}(W))$ (Theorem §CB.2.3). Each $\Psi(g)$ is a complex-linear algebra automorphism: $\Psi(g)(AB) = U_gAU_g^{-1}U_gBU_g^{-1} = \Psi(g)(A)\,\Psi(g)(B)$. Differentiating $\Psi(e^{sX})(AB) = \Psi(e^{sX})(A)\,\Psi(e^{sX})(B)$ at $s = 0$ by the product rule: $\psi(X)(AB) = \psi(X)(A)\,B + A\,\psi(X)(B)$. So $\psi(X)$ is a complex-linear derivation of the algebra $\mathfrak{gl}(W) = M_n(\mathbb C)$.
>
> **3. Every derivation of M_n(ℂ) is a commutator (written here).** Let $\delta$ be a complex-linear derivation and $E_{ij}$ the matrix units, $E_{ij}E_{kl} = \delta_{jk}E_{il}$, $\sum_kE_{kk} = \mathbb 1$. Put $Y = \sum_k\delta(E_{k1})E_{1k}$. Applying $\delta$ to $E_{ij}E_{k1} = \delta_{jk}E_{i1}$ gives $E_{ij}\delta(E_{k1}) = \delta_{jk}\delta(E_{i1}) - \delta(E_{ij})E_{k1}$. Then
>
> $$
> [Y, E_{ij}] = \sum_k\delta(E_{k1})E_{1k}E_{ij} - \sum_kE_{ij}\delta(E_{k1})E_{1k} = \delta(E_{i1})E_{1j} - \Bigl(\delta(E_{i1})E_{1j} - \delta(E_{ij})\sum_kE_{k1}E_{1k}\Bigr) = \delta(E_{ij}) ,
> $$
>
> using $E_{1k}E_{ij} = \delta_{ki}E_{1j}$ in the first sum and $\sum_kE_{k1}E_{1k} = \sum_kE_{kk} = \mathbb 1$ in the second. By linearity $\delta = \operatorname{ad}Y$, $\operatorname{ad}Y(X) = [Y, X]$. If $\operatorname{ad}Y = \operatorname{ad}Y'$, then $Y - Y'$ commutes with every matrix and is a multiple of $\mathbb 1$ (step 1).
>
> **4. The traceless lift is a Lie algebra homomorphism.** By steps 2–3, for each $X \in \mathfrak g$ there is exactly one traceless $\sigma(X) \in \mathfrak{sl}(W)$ with $\psi(X) = \operatorname{ad}\sigma(X)$ (replace $Y$ by $Y - \frac1n(\operatorname{tr}Y)\mathbb 1$). For real $a, b$: $\operatorname{ad}(a\sigma(X) + b\sigma(Z)) = \psi(aX + bZ)$ and $a\sigma(X) + b\sigma(Z)$ is traceless, so it equals $\sigma(aX + bZ)$. By the Jacobi identity $\operatorname{ad}$ preserves brackets (Theorem §CB.2.14, 1), so $\operatorname{ad}[\sigma(X), \sigma(Z)] = [\psi(X), \psi(Z)] = \psi([X, Z])$; and $[\sigma(X), \sigma(Z)]$ is traceless (a commutator), so it equals $\sigma([X, Z])$. This is Hall's Prop. 16.46: the projective representation is "de-projectivized" at the Lie algebra level, uniquely once the trace is fixed to $0$.
>
> **5. Integrate on the simply connected cover.** $\tilde\sigma = \sigma\circ p_\ast : \tilde{\mathfrak g} \to \mathfrak{sl}(W)$ is a Lie algebra homomorphism. Since $\tilde G$ is simply connected, there is a unique Lie group homomorphism $\Sigma : \tilde G \to GL(W)$ with $\Sigma_\ast = \tilde\sigma$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-18|Theorem §CB.2.18]]). For $Y \in \tilde{\mathfrak g}$, $\det\Sigma(e^Y) = \det e^{\tilde\sigma(Y)} = e^{\operatorname{tr}\tilde\sigma(Y)} = 1$ ($\det e^A = e^{\operatorname{tr}A}$, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-4|Theorem §CB.1.4]]), and $\tilde G$, connected, consists of products of exponentials ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]], 3), so $\Sigma(\tilde G) \subset SL(W)$.
>
> **6. Σ lifts Π.** $\operatorname{Ad}\circ\Sigma$ and $\Psi\circ p$ are Lie group homomorphisms $\tilde G \to GL(\mathfrak{gl}(W))$. Their differentials agree: $\operatorname{Ad}_\ast = \operatorname{ad}$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-14|Theorem §CB.2.14]], 2, for $GL(W)$; directly, $\frac{d}{ds}e^{sY}Xe^{-sY}\big|_0 = YX - XY$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-3|Theorem §CB.1.3]], 5)), so $(\operatorname{Ad}\circ\Sigma)_\ast = \operatorname{ad}\circ\sigma\circ p_\ast = \psi\circ p_\ast = (\Psi\circ p)_\ast$ (chain rule, Theorem §CB.2.3). $\tilde G$ is connected, so $\operatorname{Ad}\circ\Sigma = \Psi\circ p$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-11|Theorem §CB.2.11]]). Hence $\Sigma(x)U_{p(x)}^{-1}$ commutes with every $X \in \mathfrak{gl}(W)$ and is a scalar $c(x)\mathbb 1$ (step 1): $[\Sigma(x)] = \Pi(p(x))$.
>
> **7. Uniqueness in SL(W).** Let $\Sigma'$ be another lift into $SL(W)$. Then $\Sigma'(x) = c(x)\Sigma(x)$ with $c(x) \in \mathbb C^\times$, and taking determinants $c(x)^n = 1$. The map $x \mapsto c(x)\mathbb 1 = \Sigma'(x)\Sigma(x)^{-1}$ is continuous and a homomorphism: $c(xy)\mathbb 1 = \Sigma'(x)\Sigma'(y)\Sigma(y)^{-1}\Sigma(x)^{-1} = \Sigma'(x)\,c(y)\,\Sigma(x)^{-1} = c(y)c(x)\mathbb 1$. A continuous map from the connected $\tilde G$ into the finite set of $n$-th roots of unity is constant, here $c \equiv c(\mathbb 1) = 1$.
>
> **8. The unitary case.** If every $\Pi(g)$ has a unitary representative $U_g$ (a projective representation in the sense of [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-6|Def. §CB.9.6]]), then $\Sigma(x) = c(x)U_{p(x)}$ by step 6, and $1 = |\det\Sigma(x)| = |c(x)|^n|\det U_{p(x)}| = |c(x)|^n$, so $|c(x)| = 1$ and $\Sigma(x)$ is unitary: $U_{p(x)} = \overline{c(x)}\,\Sigma(x)$ is a lift in the sense of Def. §CB.18.5.
>
> **9. Instances.** $SU(2) \to SO(3)$ is the universal covering group ([[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-7|Theorem §CB.9.7]]), and $SL(2, \mathbb C) \to SO^+(1,3)$ is ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], 3). The rotation case is [[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^thm-cb-18-7|Theorem §CB.18.7]], whose derivation normalizes the determinant on the group instead of the trace on the algebra.
>
> **What the proof shows**
> - Finite dimension enters through the trace (step 4) and the determinant (steps 5, 7): they remove the scalar ambiguity of each generator. ⚑ By-product: in infinite dimension no trace exists, and a scalar added to a bracket may be impossible to remove; that is the hypothesis of Bargmann's theorem (Theorem §CB.18.8 below) and the obstruction in [[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^rem-cb-18-1|§CB.18, ★ Remark: Infinite dimensions, Bargmann, and a phase topology does not explain]].
> - The topology enters only in step 5: on $G$ itself the traceless $\sigma$ need not integrate (it integrates to $SU(2)$, not to $SO(3)$, for half-integer spin); this is the two-valuedness of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], 2.
> - Unitarity was not needed for existence: the non-unitary two-valued Lorentz representations $(j_+, j_-)$ lift to $SL(2, \mathbb C)$ in the same way.

^pf-cb-18-6

*Uses:* [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-3|Theorem §CB.1.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-4|Theorem §CB.1.4]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-14|Theorem §CB.2.14]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-11|Theorem §CB.2.11]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-18|Theorem §CB.2.18]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-6|Theorem §CB.6.6]]

The rotation case, the course's theorem (with Yu's loop argument as a second route), and what changes in infinite dimensions; it is the case $G = SO(3)$ of Theorem §CB.18.6 with the cover $SU(2)$, the sign made explicit:

> [!theorem] Theorem §CB.18.7: Projective Representations of SO(3) Are Representations of SU(2)
> Let $U$ be a continuous finite-dimensional projective representation of $SO(3)$. Then
> 1. there is a genuine representation $\Sigma$ of $SU(2)$ with $U(R(V)) = c(V)\,\Sigma(V)$, $|c(V)| = 1$, for all $V \in SU(2)$;
> 2. if $U$ is irreducible, $\Sigma \cong D^{(j)}$ for one $j$, and the phases can be chosen so that $U(W_2)U(W_1) = \pm U(W_2W_1)$: always $+$ for integer $j$; for half-integer $j$, $-$ exactly when the loop $\mathbb 1 \to W_1 \to W_2W_1 \to \mathbb 1$ (along the paths that define the chosen lifts) is not contractible. No other phase is needed.
>
> In particular $SU(2)$, being simply connected, has no projective representations in finite dimension beyond its genuine ones.
>
> *Source: Yu §3.3.1, eqs. (3.111)–(3.117) · the user's PHY 513 notes, Ch. 7 §7.2 ("Why quantum mechanics allows exactly a sign, and no other phase") · the user's pre-course notes, §2.3 · Hall, Prop. 16.46, Thm. 16.47*

^thm-cb-18-7

> [!derivation]- Derivation
> Let $n = \dim\mathcal H$.
>
> **1. Fix the determinant.** Replace each $U(W)$ by $U'(W) = (\det U(W))^{-1/n}U(W)$, for some choice of the $n$-th root; this is a phase redefinition (Def. §CB.9.6) and gives $\det U'(W) = 1$. Then $U'(W_2)U'(W_1) = c(W_2, W_1)\,U'(W_2W_1)$ with $|c| = 1$, and taking determinants, $1 = c(W_2, W_1)^n\cdot1$. ⚑ By-product: after this normalization every phase is an $n$-th root of unity, a discrete set; finite dimension is used here → [[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^rem-cb-18-1|★ Remark: Infinite dimensions]].
>
> **2. Near the identity, no phase.** Choose the roots so that $U'$ is continuous on a neighbourhood $N$ of $\mathbb 1$ with $U'(\mathbb 1) = \mathbb 1$ (possible since $U$ is continuous into $PU(n)$ and $U(n) \to PU(n)$ has continuous local sections near the identity). Then $c(W_2, W_1)$ is continuous for $W_1, W_2, W_2W_1 \in N$, equals $1$ at $(\mathbb 1, \mathbb 1)$, and takes values in the discrete set of step 1, so $c = 1$ on a neighbourhood: $U'$ is a homomorphism near $\mathbb 1$.
>
> **3. An algebra representation.** For $X \in \mathfrak{so}(3)$ and small $|s|$, $s \mapsto U'(e^{sX})$ satisfies $F(s+t) = F(s)F(t)$ (step 2), and steps 2–6 of Derivation §CB.2.8 use only this local law (continuity suffices for differentiability, Hall Thm. 16.18): $d(X) = \frac{d}{ds}U'(e^{sX})|_0$ is a representation of $\mathfrak{so}(3)$ by traceless anti-Hermitian matrices ($\det = 1$ and unitarity, differentiated).
>
> **4. Integrate on $SU(2)$.** Compose with the isomorphism of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]] to get a representation of $\mathfrak{su}(2)$. It is unitary (anti-Hermitian $d(X)$), so orthogonal complements of invariant subspaces are invariant (as in step 5 of Derivation §CB.6.17, with $d(X)^\dagger = -d(X)$ in place of $D(V)^{-1} = D(V)^\dagger$), and it is a sum of irreducible pieces, each some $D^{(j)}$ (Theorem §CB.9.3). Each integrates to $SU(2)$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]], 1); their sum is a genuine representation $\Sigma$ of $SU(2)$ with $\Sigma(e^X) = e^{d(X)} = U'(R(e^X))$ for small $X$.
>
> **5. Agreement everywhere.** The projective representations $V \mapsto [\Sigma(V)]$ and $V \mapsto [U(R(V))]$ of $SU(2)$ agree on a neighbourhood of $\mathbb 1$. Every $V \in SU(2)$ is $e^X = (e^{X/k})^k$ with $e^{X/k}$ in that neighbourhood for large $k$, and both are compatible with products up to phases, so $U(R(V)) = c(V)\,\Sigma(V)$ for all $V$. Part 1.
>
> **6. Signs.** If $U$ is irreducible, so is $\Sigma$ (same operators up to phases, hence same invariant subspaces), and $\Sigma \cong D^{(j)}$; $\Sigma(-\mathbb 1) = (-1)^{2j}\mathbb 1$ (Theorem §CB.9.8, 1). Choose for each $W \in SO(3)$ one preimage $V_W$, $R(V_W) = W$, and set $U(W) \equiv \Sigma(V_W)$, a phase redefinition by part 1. Both $V_{W_2}V_{W_1}$ and $V_{W_2W_1}$ are preimages of $W_2W_1$, so $V_{W_2}V_{W_1} = \pm V_{W_2W_1}$ and
>
> $$
> U(W_2)\,U(W_1) = \Sigma(V_{W_2}V_{W_1}) = \Sigma(\pm\mathbb 1)\,\Sigma(V_{W_2W_1}) = (\pm1)^{2j}\,U(W_2W_1) .
> $$
>
> For integer $j$ the sign is always $+$: $U$ is a genuine representation of $SO(3)$. For half-integer $j$ it is $-$ exactly when $V_{W_2}V_{W_1}V_{W_2W_1}^{-1} = -\mathbb 1$. Choosing each $V_W$ as the endpoint of the lift of a path from $\mathbb 1$ to $W$, this product is the endpoint of the lift of the loop $\mathbb 1 \to W_1 \to W_2W_1 \to \mathbb 1$, which is $-\mathbb 1$ iff the loop is not contractible ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-7|Theorem §CB.9.7]], 2).
>
> **What the derivation shows**
> - Topology fixes which phases *survive*: on a simply connected group none, on $SO(3)$ a sign. Algebra fixes that no *continuous* phase is forced at all: step 1–2 removed every phase near the identity. That second fact uses finite dimension (the determinant, equivalently the trace: Hall Prop. 16.46 lifts any finite-dimensional projective representation of a Lie algebra to a traceless genuine one, unique because every element of $\mathfrak{so}(3)$ is a combination of commutators, $J^3 = -i[J^1, J^2]$). In infinite dimension one must show instead that a constant added to the brackets can be removed by redefining the generators; for the rotation and Lorentz algebras it can (Bargmann; [[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^rem-cb-18-1|★ Remark: Infinite dimensions]]).
> - Physically: states are rays, so a rotation need only act on rays, and that is exactly what allows half-integer spin. Particles are therefore classified by the genuine irreducible representations of the covering group $SU(2)$ (Yu, below (3.117)).
> - Used next: $U(\Lambda, a)$ on states as a representation of the covering group of the Poincaré group ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^pr-c3-4-1|Principle §C3.4.1]], [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-1|§C3.4, Remark: Why unitary, and why the covering group]]); the little group of a massive particle ([[§C3.6★ Particle States and the Little Group#^thm-c3-6-7|Theorem §C3.6.7]]).

^der-cb-18-7

*Uses:* [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-6|Def. §CB.9.6]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-17|Theorem §CB.6.17]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-7|Theorem §CB.9.7]]

> [!derivation]- Derivation (second route: loops in the group space, Yu and the user's notes)
> **1. The phase belongs to a loop.** From $U(W_2)U(W_1) = e^{i\varphi(W_2, W_1)}U(W_2W_1)$, $e^{i\varphi(W_2, W_1)}\mathbb 1 = U^{-1}(W_2W_1)\,U(W_2)\,U(W_1)$ (Yu (3.114)). Read the products as a path in the group: $\mathbb 1 \to W_1 \to W_2W_1$, closed back to $\mathbb 1$.
>
> **2. Contractible loops carry no phase.** If the loop shrinks continuously to $\mathbb 1$ and the phase varies continuously along the deformation, it ends at $U^{-1}(\mathbb 1)U(\mathbb 1)U(\mathbb 1) = \mathbb 1$: $e^{i\varphi} = 1$ (Yu (3.115)).
>
> **3. Doubled loops.** In $SO(3)$ every loop traversed twice is contractible (Theorem §CB.9.7, 3; Yu Fig. 3.8), so $(e^{i\varphi})^2 = 1$ (Yu (3.116)) and $U(W_2)U(W_1) = \pm U(W_2W_1)$ (Yu (3.117)). In $SU(2)$ every loop shrinks and the phase is $1$.
>
> **What the derivation shows**
> - This is the argument of Yu and of the user's notes. Its step 2 presupposes that the phase depends continuously on the loop, i.e. that a continuous choice of phases has been made; for arbitrary phase choices $\varphi$ need not be continuous. Steps 1–2 of the main derivation supply exactly this (in finite dimension), which the user's pre-course notes mark as "heuristic; the honest statement is a theorem" (Weinberg vol. 1, §2.7 and App. 2.B, cited there).
> - What it does show correctly is where the sign comes from: the phase is a function of the homotopy class of a loop, and $\pi_1(SO(3)) = \mathbb Z_2$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-7|Theorem §CB.9.7]]) leaves room for exactly $\pm1$.

> [!remark]- ★ Remark: Infinite dimensions, Bargmann, and a phase topology does not explain
> On an infinite-dimensional Hilbert space, the space of states of a particle, the determinant trick of step 1 of Derivation §CB.18.7 is unavailable (generators are unbounded, traces undefined). For the rotation and Lorentz groups the conclusion still holds: every continuous projective unitary representation lifts to a genuine one of the covering group (Bargmann's theorem, cited by the user's pre-course notes via Weinberg vol. 1, §2.7 and App. 2.B). It is not automatic: Hall's Ex. 16.56 gives a projective representation of the simply connected group $\mathbb R^2$ that cannot be made genuine, $(T_{(a,b)}\psi)(x) = e^{iax}\psi(x - b)$ with $T_{(a,b)}T_{(a',b')} = e^{-ia'b}T_{(a+a', b+b')}$, i.e. momentum and position translations. Its phase is not topological but algebraic: the generators obey $[\hat x, \hat p] = i$, a bracket whose right side is a multiple of the identity that cannot be absorbed (the canonical commutation relations of [[§C2.2 Translation and Momentum as Its Generator#^thm-c2-2-6|QM Theorem §C2.2.6]], and of the free field, [[§C2a.1 Canonical Quantization of Fields|§C2a.1]]). The rotation and Lorentz algebras admit no such central term: a constant added to any of their brackets can be removed by redefining the generators (their second Lie-algebra cohomology vanishes, Whitehead's lemma for semisimple algebras; Weinberg vol. 1, §2.7, removes the central charges of the Poincaré algebra the same way). That every element is a sum of commutators makes such a redefinition unique, but does not by itself guarantee that one exists (Hall Prop. 16.46 and its remark).
>
> *Source: Hall §16.9.2, Ex. 16.56 · the user's pre-course notes, §2.3 ("Projective representations", bracketed note)*

^rem-cb-18-1

> [!theorem] Theorem §CB.18.8: Bargmann's Theorem
> Let $\tilde G$ be a connected and simply connected Lie group whose Lie algebra $\mathfrak g$ has the property that every real skew-symmetric bilinear form $\beta$ on $\mathfrak g$ with $\beta([X, Y], Z) + \beta([Y, Z], X) + \beta([Z, X], Y) = 0$ is of the form $\beta(X, Y) = f([X, Y])$ for a linear $f : \mathfrak g \to \mathbb R$ (vanishing second cohomology). Then every continuous projective unitary representation of $\tilde G$ on a separable Hilbert space is induced by a continuous unitary representation of $\tilde G$. This holds for $SU(2)$, $SL(2, \mathbb C)$ and the universal cover $\mathbb R^{1,3}\rtimes SL(2, \mathbb C)$ of the Poincaré group (§CB.19★).
>
> *Source: V. Bargmann, "On unitary ray representations of continuous groups", Ann. of Math. 59 (1954) 1–46 (the original theorem and proof) · the statement as Theorem 135 ("Bargmann's criterion") in V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course, arXiv:1508.06951, §3.6 (https://arxiv.org/abs/1508.06951), where continuity means that $g \mapsto |\langle\psi, U(g)\phi\rangle|$ is continuous for all $\psi, \phi$ and the conclusion is equivalence (phases $U'(g) = \chi(g)U(g)$) to a strongly continuous unitary representation; Moretti's Remark 136 notes that $SU(2)$ satisfies the condition · the Poincaré case: Weinberg vol. 1, §2.7 and App. 2.B, as cited in the user's pre-course notes · Hall, Quantum Theory for Mathematicians, §16.9.2, Ex. 16.56 (a simply connected group where the conclusion fails)*

^thm-cb-18-8

> [!proof]- Proof (to be filled)
> *Not proved here: the proof (Bargmann 1954, cited above) needs the local theory of continuous ray representations in infinite dimension (local exponents, their smoothing and their reduction to Lie-algebra cocycles), beyond the finite-dimensional tools of this chapter. That the condition on $\beta$ holds for $\mathfrak{su}(2)$ and $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ is Whitehead's second lemma for semisimple Lie algebras (quoted), for the Poincaré algebra Weinberg's removal of central charges (§2.7). The finite-dimensional analogue is proved in Theorem §CB.18.6.*

<!-- Searched for a freely available proof (2026-10-08): Bargmann 1954 (Ann. Math., paywalled); Hall QTM §16.7–16.9 (states the obstruction, Ex. 16.56, no proof); Moretti arXiv:1508.06951 §3.6 (statement only, cites Barut–Raczka and Moretti's Springer book); Schottenloher, A Mathematical Introduction to Conformal Field Theory, Ch. 4 "Central Extensions of Lie Algebras and Bargmann's Theorem" (author's PDF link returned 404); Weinberg App. 2.B (no free copy). -->

^pf-cb-18-8

## Antiunitary symmetries

> [!definition] Definition §CB.18.9: Unitary–Antiunitary Representation
> Let $G_0 \subset G$ be a subgroup of index $2$. A **unitary–antiunitary representation** (corepresentation) of $(G, G_0)$ on $\mathcal H$ assigns to each $g \in G$ an operator $U(g)$, unitary for $g \in G_0$ and antiunitary for $g \notin G_0$, with $U(g)U(h) = e^{i\varphi(g, h)}U(gh)$. Example: the Lorentz group with $\mathcal T$, $G_0$ the subgroup without time reversal, $U(\mathcal T)$ antiunitary.
>
> *Source (planned): written here · Quantum Mechanics §C8.3★*

^def-cb-18-9

> [!theorem] Theorem §CB.18.10: The Square of an Antiunitary Involution Is ±1
> If $\Theta$ is antiunitary and $\Theta^2 = c\mathbb 1$ for a number $c$, then $c = \pm1$. If $c = -1$, then $\Theta\psi$ is orthogonal to $\psi$ for every $\psi$.
>
> *Source: written here · [[§C8.3★ Time Reversal#^thm-c8-3-7|QM Theorem §C8.3.7]] (Kramers)*

^thm-cb-18-10

> [!proof]- Proof
> **1. c is real.** $\Theta^3 = \Theta\Theta^2 = \Theta(c\mathbb 1) = \bar c\,\Theta$ because $\Theta$ is antilinear, and $\Theta^3 = \Theta^2\Theta = c\,\Theta$. Since $\Theta \ne 0$, $\bar c = c$.
>
> **2. |c| = 1.** $\Theta^2$ is unitary (step 1 of Theorem §CB.18.4), so $\|c\psi\| = \|\psi\|$ and $|c| = 1$. With step 1, $c = \pm1$.
>
> **3. c = −1.** For antiunitary $\Theta$, $\langle\Theta\phi, \Theta\chi\rangle = \overline{\langle\phi, \chi\rangle} = \langle\chi, \phi\rangle$. With $\phi = \Theta\psi$, $\chi = \psi$: $\langle\Theta^2\psi, \Theta\psi\rangle = \langle\psi, \Theta\psi\rangle$, i.e. $-\langle\psi, \Theta\psi\rangle = \langle\psi, \Theta\psi\rangle$, so $\langle\psi, \Theta\psi\rangle = 0$.

^pf-cb-18-10

> [!theorem] Theorem §CB.18.11: An Antiunitary Operator Reversing Spin Squares to (−1)²ʲ
> Let $\Theta$ be antiunitary on the spin-$j$ representation $V_j$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]]) with $\Theta J^a\Theta^{-1} = -J^a$ for $a = 1, 2, 3$. Then $\Theta^2 = (-1)^{2j}\mathbb 1$. In particular an antiunitary time reversal acts on spinors with $\Theta^2 = -1$ and on tensors with $\Theta^2 = +1$.
>
> *Source: [[§C8.3★ Time Reversal#^thm-c8-3-6|QM Theorem §C8.3.6]] (Sakurai §4.4.4: $\Theta = \eta\,e^{-i\pi J_y}K$, $\Theta^2 = (-1)^{2j}$) · the condition $\Theta\mathbf J\Theta^{-1} = -\mathbf J$: Yu Zhao-Huan, 量子场论讲义, §9.1.2, eqs. (9.50)–(9.58) · the ladder-operator proof written here*

^thm-cb-18-11

> [!proof]- Proof
> Use the standard basis $|j, m\rangle$ of $V_j$ and its inner product, in which the $J^a$ are Hermitian ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], 3); $\Theta$ is antiunitary for this inner product.
>
> **1. Θ² is a scalar.** $\Theta^2$ is linear (a product of two antilinear maps) and $\Theta^2J^a\Theta^{-2} = \Theta(-J^a)\Theta^{-1} = -\Theta J^a\Theta^{-1} = J^a$ (the real number $-1$ passes through $\Theta$). So $\Theta^2$ commutes with every $J^a$; $V_j$ is irreducible, so $\Theta^2 = c\mathbb 1$ ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-6|Theorem §CB.6.6]]), and $c = \pm1$ ([[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^thm-cb-18-10|Theorem §CB.18.10]]).
>
> **2. Θ reverses m.** $J^3\,\Theta|j, m\rangle = -\Theta J^3|j, m\rangle = -\Theta\bigl(m|j, m\rangle\bigr) = -m\,\Theta|j, m\rangle$ ($m$ real). The weight spaces are one-dimensional, so $\Theta|j, m\rangle = a_m|j, -m\rangle$, and $|a_m| = 1$ because $\Theta$ preserves norms.
>
> **3. Θ turns J⁺ into −J⁻.** Since $\Theta$ is antilinear, $\Theta(iJ^2)\Theta^{-1} = -i\,\Theta J^2\Theta^{-1} = iJ^2$, so $\Theta J^\pm\Theta^{-1} = \Theta(J^1 \pm iJ^2)\Theta^{-1} = -J^1 \pm iJ^2 = -J^\mp$.
>
> **4. The phases alternate.** Let $N_m = \sqrt{(j - m)(j + m + 1)}$, so $J^+|j, m\rangle = N_m|j, m+1\rangle$ and $J^-|j, -m\rangle = \sqrt{(j - m)(j + m + 1)}\,|j, -m-1\rangle = N_m|j, -m-1\rangle$ (Theorem §CB.9.3, 3). For $m < j$ apply step 3 to $|j, m\rangle$: the left side $\Theta J^+|j, m\rangle = \Theta(N_m|j, m+1\rangle) = N_ma_{m+1}|j, -m-1\rangle$ ($N_m$ real), the right side $-J^-\Theta|j, m\rangle = -a_mJ^-|j, -m\rangle = -a_mN_m|j, -m-1\rangle$. With $N_m \ne 0$: $a_{m+1} = -a_m$, hence $a_m = (-1)^{j-m}a_j$ for $m = j, j-1, \dots, -j$.
>
> **5. The square.** $\Theta^2|j, m\rangle = \Theta(a_m|j, -m\rangle) = \bar a_m\,a_{-m}|j, m\rangle = \overline{(-1)^{j-m}a_j}\,(-1)^{j+m}a_j|j, m\rangle = (-1)^{2j}|a_j|^2|j, m\rangle = (-1)^{2j}|j, m\rangle$, the signs being real ($j \pm m$ are integers).
>
> **What the proof shows**
> - The sign is forced by the ladder structure alone: reversing $m$ antilinearly flips the sign at every rung, and $2j$ rungs separate $m$ from $-m$. No phase convention for $\Theta$ affects it ($a_j$ cancels against its conjugate), in agreement with QM Theorem §C8.3.6 ($\eta$ arbitrary).
> - For half-integer $j$, $\Theta^2 = -1$ and Theorem §CB.18.10 gives $\Theta\psi \perp \psi$: Kramers degeneracy ([[§C8.3★ Time Reversal#^thm-c8-3-7|QM Theorem §C8.3.7]]).

^pf-cb-18-11

*Uses:* [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-6|Theorem §CB.6.6]], [[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^thm-cb-18-10|Theorem §CB.18.10]]

The course's remark on why states carry unitary representations of the covering group is physics: [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-1|§C3.4, Remark: Why unitary, and why the covering group]].

> [!remark]- Connections
> - Theorem §CB.18.4 is why continuous symmetries (rotations, boosts, translations) are unitary and only discrete ones can be antiunitary: time reversal is antiunitary ([[§C8.3★ Time Reversal#^thm-c8-3-3|QM Theorem §C8.3.3]]), parity unitary ([[§C9.3 Parity on States, Spinors and the Dirac Field|§C9.3]]); C, T, CPT follow after Lecture 12 (QFT C9, planned).
> - Theorem §CB.18.6 and Theorem §CB.18.8 are the precise forms of "spin ½ is a representation of SU(2), not SO(3)": the two-valuedness of §C3.1 and §C5a.4 is the projective representation, and its lift is the genuine representation of the covering group (§CB.13).
> - **Used in**: Definitions §CB.18.1–Theorem §CB.18.3 — [[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-1|QM Theorem §C8.1.1]], [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^pr-c3-4-1|Principle §C3.4.1]], [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-1|§C3.4, Remark: Why unitary, why the covering group]]; Theorem §CB.18.4 — [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-2|Theorem §C3.4.2]]; Theorem §CB.18.6 — [[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^thm-cb-18-7|Theorem §CB.18.7]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^rem-cb-9-2|§CB.9, Remark: The same pattern for the Lorentz group]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]; Theorem §CB.18.8 — [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^pr-c3-4-1|Principle §C3.4.1]], [[§C3.6★ Particle States and the Little Group#^pr-c3-6-1|Principle §C3.6.1]]; Theorems §CB.18.10–§CB.18.11 — [[§C8.3★ Time Reversal#^thm-c8-3-6|QM Theorem §C8.3.6]], [[§C8.3★ Time Reversal#^thm-c8-3-7|QM Theorem §C8.3.7]], time reversal in QFT C9 (planned); Theorem §CB.18.7 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded), [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra|§C3.4]] (embedded; cited in [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-1|§C3.4, Remark: Why unitary, and why the covering group]]), [[§C3.6★ Particle States and the Little Group|§C3.6★]] (embedded; cited in [[§C3.6★ Particle States and the Little Group#^thm-c3-6-8|Theorem §C3.6.8]]); Theorem §CB.18.3 — [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra|§C3.4]] (embedded); Theorem §CB.18.4 — [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra|§C3.4]] (embedded); Theorem §CB.18.6 — [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra|§C3.4]] (embedded).
