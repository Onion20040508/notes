---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.8
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.7 The Dirac Equation and Its Lagrangian]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.9 Canonical Structure and Noether Currents of the Dirac Field]] →

*Sources: the user's PHY 513 notes, Ch. 8 §8.2 ("This is the Dirac invariant"), §8.10 (The Weyl form of the Dirac equation) and the paragraph "Why 'left' and 'right'" · PHY 513 Lecture 8 (Larsen), Part C · PHY 513 Lecture 13 (Larsen, 14 Oct 2026), transcript (the question at the start of the lecture) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.2, eqs. (3.36), (3.39)–(3.40), (3.42)–(3.44), and §3.3, p. 47 · Yu Zhao-Huan, 量子场论讲义, §5.3, eqs. (5.113)–(5.115) · the user's pre-course notes, §5.3 ("Weyl spinors").*

How does the Dirac equation look in the two Weyl halves, and what is left of it at $m = 0$? The Dirac equation and its covariance are [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]] and [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]], its Lagrangian [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; the Weyl halves of spinor space, the eigenspaces of $\gamma^5$, are [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]. This section writes the bilinears and the Dirac equation in Weyl components, where only the mass couples the two halves, states the Weyl fields of a massless spinor, and shows that their plane waves have fixed helicity (Lecture 8, Part C; the user's notes, Ch. 8 §8.10). The helicity spinors of the massive field and the massless limit of the Dirac spinors are [[§C5a.13 Helicity Spinors and the Massless Limit|§C5a.13]].

**Setup.** Classical and free, with commuting complex components, in flat spacetime; no quantum states yet: the free Dirac field [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]] for the decomposition and, for $m = 0$, the Weyl fields [[§C5a.8 The Weyl Form and the Weyl Equations#^mod-c5a-8-3|Model §C5a.8.3]]. The Weyl decomposition (Theorem §C5a.8.1) is an identity for every $C^1$ field, off shell; Theorems §C5a.8.2 and §C5a.8.4 are about solutions. All results are exact.

*Conventions* ([[Larsen PHY 513]]): as in [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]].

## The mathematics used here

The Weyl form splits spinor space by $\gamma^5$; Model §C5a.8.3 has no parity symmetry because parity exchanges the two copies, and the ★ remark on a Majorana mass uses that complex conjugation exchanges them:

![[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-4]]

![[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^pf-cb-18-4]]

![[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-13]]

![[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-17-13]]

![[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-14]]

![[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-17-14]]

Mass breaks chiral symmetry because $\gamma^0$, the matrix of the invariant form, swaps the Weyl blocks; in group language this is the pseudo-unitarity of $\Lambda_{1/2}$:

![[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-13]]

![[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-18-13]]

![[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-18-13b]]

## The Weyl form and the Weyl equations

> [!theorem] Theorem §C5a.8.1: Bilinears in Weyl Components
> For $\psi = (\psi_L, \psi_R)$, $\chi = (\chi_L, \chi_R)$ in the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]; Weyl halves [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]; $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]), $\bar\psi = (\psi_R^\dagger, \psi_L^\dagger)$ ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]) and
>
> $$
> \bar\psi\chi = \psi_R^\dagger\chi_L + \psi_L^\dagger\chi_R, \qquad \bar\psi\gamma^\mu\chi = \psi_L^\dagger\bar\sigma^\mu\chi_L + \psi_R^\dagger\sigma^\mu\chi_R ,
> $$
>
> $$
> \bar\psi\gamma^\mu\gamma^5\chi = -\psi_L^\dagger\bar\sigma^\mu\chi_L + \psi_R^\dagger\sigma^\mu\chi_R, \qquad \bar\psi\,i\gamma^5\chi = i\bigl(\psi_L^\dagger\chi_R - \psi_R^\dagger\chi_L\bigr) .
> $$
>
> Hence the Dirac Lagrangian ([[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]) is
>
> $$
> \mathcal L = i\psi_L^\dagger\bar\sigma^\mu\partial_\mu\psi_L + i\psi_R^\dagger\sigma^\mu\partial_\mu\psi_R - m\bigl(\psi_L^\dagger\psi_R + \psi_R^\dagger\psi_L\bigr) :
> $$
>
> the kinetic terms keep the chiralities apart, the mass term pairs them.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]] (the form of $\mathcal L$); *applies:* chiral basis; the bilinear identities hold for any spinors, the form of $\mathcal L$ for every $C^1$ field (off shell).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 ("This is the Dirac invariant": $\bar\psi\chi = \psi_R^\dagger\chi_L + \psi_L^\dagger\chi_R$), §8.10 · PS §3.2, eqs. (3.36), (3.42)*

^thm-c5a-8-1

> [!derivation]- Derivation
> In the chiral basis $\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$, $\gamma^\mu = \begin{pmatrix}0 & \sigma^\mu\\ \bar\sigma^\mu & 0\end{pmatrix}$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]), $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]).
>
> **1. The conjugate row.** $\psi^\dagger = (\psi_L^\dagger, \psi_R^\dagger)$; multiplying by $\gamma^0$ swaps the blocks: $\bar\psi = (\psi_R^\dagger, \psi_L^\dagger)$.
>
> **2. Scalar.** $\bar\psi\chi = \psi_R^\dagger\chi_L + \psi_L^\dagger\chi_R$.
>
> **3. Vector.** $\gamma^\mu\chi = (\sigma^\mu\chi_R,\ \bar\sigma^\mu\chi_L)$, so $\bar\psi\gamma^\mu\chi = \psi_R^\dagger\sigma^\mu\chi_R + \psi_L^\dagger\bar\sigma^\mu\chi_L$.
>
> **4. Axial vector.** $\gamma^5\chi = (-\chi_L, \chi_R)$, then $\gamma^\mu\gamma^5\chi = (\sigma^\mu\chi_R,\ -\bar\sigma^\mu\chi_L)$, so $\bar\psi\gamma^\mu\gamma^5\chi = \psi_R^\dagger\sigma^\mu\chi_R - \psi_L^\dagger\bar\sigma^\mu\chi_L$.
>
> **5. Pseudoscalar.** $\bar\psi\gamma^5\chi = (\psi_R^\dagger, \psi_L^\dagger)(-\chi_L, \chi_R) = -\psi_R^\dagger\chi_L + \psi_L^\dagger\chi_R$; multiply by $i$.
>
> **6. The Lagrangian.** Step 3 with $\chi \to \partial_\mu\psi$ (the blocks of $\partial_\mu\psi$ are $\partial_\mu\psi_L$, $\partial_\mu\psi_R$) gives the kinetic terms; step 2 with $\chi = \psi$ gives the mass term.
>
> **What the derivation shows**
> - The invariant form $\gamma^0$ of [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-13|Theorem §CB.18.13]] *is* the pairing of a left- with a right-handed slot ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-4|Theorem §C5a.5.4]]): a Lorentz scalar without derivatives must couple $\psi_L$ to $\psi_R$, so a Dirac mass needs both ([[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-2|§C5a.5, Remark: Kinematics allows one handedness, a mass needs both]]).
> - The vector current splits into a left and a right current with no cross terms; the axial current is their difference. Both statements are basis independent by [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]]: $\bar\psi\gamma^\mu\psi = \bar\psi\gamma^\mu P_L\psi + \bar\psi\gamma^\mu P_R\psi$.

^der-c5a-8-1

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]

> [!theorem] Theorem §C5a.8.2: The Dirac Equation in Two-Component Form
> For $\psi = (\psi_L, \psi_R)$ in the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]), the Dirac equation ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]]) is equivalent to
>
> $$
> i\bar\sigma^\mu\partial_\mu\psi_L = m\,\psi_R, \qquad i\sigma^\mu\partial_\mu\psi_R = m\,\psi_L ,
> $$
>
> with $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]], i.e. $i(\partial_0 - \boldsymbol\sigma\cdot\nabla)\psi_L = m\psi_R$, $i(\partial_0 + \boldsymbol\sigma\cdot\nabla)\psi_R = m\psi_L$. The kinetic operators act within each Weyl block; only the mass couples them.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* classical, chiral basis, every $C^1$ field (the two forms of the equation are equivalent), exact.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.10 (Derivation "The Dirac equation in two-component form", eq. (weylcoupled)) · PHY 513 Lecture 8, Part C ("Dirac Equation in 2-Component Form") · PS §3.2, eqs. (3.39), (3.43) · Yu §5.3, eqs. (5.113)–(5.114)*

^thm-c5a-8-2

> [!derivation]- Derivation
> **1. The operator in blocks.** With $\gamma^\mu = \begin{pmatrix}0 & \sigma^\mu\\ \bar\sigma^\mu & 0\end{pmatrix}$ and $-m\mathbb 1_4 = \operatorname{diag}(-m\mathbb 1_2, -m\mathbb 1_2)$,
>
> $$
> i\gamma^\mu\partial_\mu - m = \begin{pmatrix}-m & i\sigma^\mu\partial_\mu\\ i\bar\sigma^\mu\partial_\mu & -m\end{pmatrix} .
> $$
>
> **2. Act on the column.** $\begin{pmatrix}-m & i\sigma\cdot\partial\\ i\bar\sigma\cdot\partial & -m\end{pmatrix}\begin{pmatrix}\psi_L\\ \psi_R\end{pmatrix} = \begin{pmatrix}i\sigma^\mu\partial_\mu\psi_R - m\psi_L\\ i\bar\sigma^\mu\partial_\mu\psi_L - m\psi_R\end{pmatrix}$, which vanishes exactly when both stated equations hold.
>
> **3. In components.** $\sigma^\mu\partial_\mu = \mathbb 1\partial_0 + \sigma^i\partial_i = \partial_0 + \boldsymbol\sigma\cdot\nabla$ and $\bar\sigma^\mu\partial_\mu = \partial_0 - \boldsymbol\sigma\cdot\nabla$ (no metric: upper index on $\sigma$, lower on $\partial$; [[§C5a.7 The Dirac Equation and Its Lagrangian#^cau-c5a-7-1|§C5a.7, Caution: γ^μ∂_μ has a plus sign]]).
>
> **What the derivation shows**
> - Representation theory allows the two blocks to be treated separately ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]); the equation of motion couples them, through the mass and only through it (figure).
> - The same equations follow by varying $\psi_L^\dagger$ and $\psi_R^\dagger$ in the Lagrangian of [[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-1|Theorem §C5a.8.1]].

^der-c5a-8-2

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]]

![[ph-qft-c5-4-1.svg]]
*The Dirac equation in two-component form: the Weyl halves are separate representations, and the mass is the only coupling between them (adapted from the user's PHY 513 notes, Ch. 8 §8.10).*

> [!model] Model §C5a.8.3: The Weyl Fields
> A **left-handed Weyl field** is a two-component field $\psi_L$ in $(\frac12, 0)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-8|Theorem §C3.2.8]]; Weyl matrices [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]]) with
>
> $$
> \mathcal L_L = i\psi_L^\dagger\bar\sigma^\mu\partial_\mu\psi_L, \qquad i\bar\sigma^\mu\partial_\mu\psi_L = 0 ;
> $$
>
> a **right-handed Weyl field** $\psi_R$ in $(0, \frac12)$ has $\mathcal L_R = i\psi_R^\dagger\sigma^\mu\partial_\mu\psi_R$ and $i\sigma^\mu\partial_\mu\psi_R = 0$. These are the **Weyl equations**.
>
> *Assumptions:* $m = 0$ (the two blocks of [[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-2|Theorem §C5a.8.2]] decouple, and either may be kept alone, consistently both as a representation and dynamically); classical, free; no parity symmetry (parity exchanges the two, [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-13|Theorem §CB.17.13]]).
> *Source: the user's PHY 513 notes, Ch. 8 §8.10 (Principle "The Weyl equations", eq. (weyl)) · PHY 513 Lecture 8, Part C ("Weyl Equation") · PS §3.2, eqs. (3.40), (3.44) · Yu §5.3, eq. (5.115)*

^mod-c5a-8-3

The 513 notes box the Weyl equations as a principle; here they are a model, the massless idealization of the Dirac theory (or, in the Standard Model, the starting point). Each component of a Weyl solution obeys the massless Klein–Gordon equation, by $(\sigma\cdot\partial)(\bar\sigma\cdot\partial) = \partial^2$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]]), the two-component version of [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]].

> [!theorem] Theorem §C5a.8.4: Weyl Plane Waves Have Fixed Helicity
> Let $\psi_L = \xi\,e^{-ip\cdot x}$ with $p^0 > 0$ and a constant nonzero two-spinor $\xi$. It solves the left-handed Weyl equation ([[§C5a.8 The Weyl Form and the Weyl Equations#^mod-c5a-8-3|Model §C5a.8.3]]) if and only if $p^2 = 0$ ($p^0 = \lvert\mathbf p\rvert$) and
>
> $$
> \bigl(\hat{\mathbf p}\cdot\boldsymbol\sigma\bigr)\,\xi = -\xi :
> $$
>
> helicity ([[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]]) $h = \hat{\mathbf p}\cdot\frac{\boldsymbol\sigma}2 = -\frac12$. For $\psi_R = \eta\,e^{-ip\cdot x}$, $p^2 = 0$ and $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\eta = +\eta$, $h = +\frac12$. One Weyl field has one helicity for its positive-frequency solutions.
>
> *Model:* [[§C5a.8 The Weyl Form and the Weyl Equations#^mod-c5a-8-3|Model §C5a.8.3]]; *applies:* classical, $m = 0$, plane-wave solutions of positive frequency $p^0 > 0$, exact.
>
> *Source: the user's pre-course notes, §5.3 ("Weyl spinors": "$(E + \boldsymbol\sigma\cdot\mathbf p)\eta = 0$, i.e. $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\eta = -\eta$: helicity $-\frac12$") · Yu §5.3 (paragraph after eq. (5.115)) · the user's PHY 513 notes, Ch. 8 §8.10 (Principle "The Weyl equations": "a single Weyl field describes a massless particle of one helicity")*

^thm-c5a-8-4

> [!derivation]- Derivation
> **1. The derivative.** $\partial_\mu e^{-ip\cdot x} = -ip_\mu e^{-ip\cdot x}$, so $i\bar\sigma^\mu\partial_\mu\psi_L = i(-i)\bar\sigma^\mu p_\mu\,\xi\,e^{-ip\cdot x} = (\bar\sigma^\mu p_\mu)\xi\,e^{-ip\cdot x}$. The exponential never vanishes: the equation is $(\bar\sigma^\mu p_\mu)\xi = 0$.
>
> **2. The matrix.** $\bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma)$ and $p_\mu = (p^0, -\mathbf p)$, so $\bar\sigma^\mu p_\mu = p^0 + \boldsymbol\sigma\cdot\mathbf p$ (two minus signs).
>
> **3. A nonzero solution needs $p^2 = 0$.** $\det(p^0 + \boldsymbol\sigma\cdot\mathbf p) = (p^0)^2 - \mathbf p^2 = p^2$ (the eigenvalues of $\boldsymbol\sigma\cdot\mathbf p$ are $\pm\lvert\mathbf p\rvert$, since $(\boldsymbol\sigma\cdot\mathbf p)^2 = \mathbf p^2$ and $\operatorname{tr}\boldsymbol\sigma\cdot\mathbf p = 0$). A nonzero kernel requires $p^2 = 0$; with $p^0 > 0$, $p^0 = \lvert\mathbf p\rvert$ and $\mathbf p \ne 0$.
>
> **4. The kernel.** $(\lvert\mathbf p\rvert + \boldsymbol\sigma\cdot\mathbf p)\xi = 0$; divide by $\lvert\mathbf p\rvert$: $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\xi = -\xi$, a one-dimensional kernel.
>
> **5. Right-handed.** $\sigma^\mu p_\mu = p^0 - \boldsymbol\sigma\cdot\mathbf p$; the same steps give $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\eta = +\eta$.
>
> **6. Helicity.** For spin $\frac12$ the spin operator in each Weyl block is $\frac12\boldsymbol\sigma$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]]), so the spin along $\hat{\mathbf p}$ is $\hat{\mathbf p}\cdot\boldsymbol\sigma/2 = \mp\frac12$ ([[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]]).
>
> **What the derivation shows**
> - Chirality and helicity coincide for massless positive-frequency solutions: left-handed means helicity $-\frac12$. For the negative-frequency solutions $\xi\,e^{+ip\cdot x}$ the condition is the same, $(p^0 + \boldsymbol\sigma\cdot\mathbf p)\xi = 0$ (step 1 with $p \to -p$ gives $-(\bar\sigma\cdot p)\xi = 0$); after quantization they describe the antiparticle, which carries the opposite helicity $+\frac12$ ([[§C5b.4 Fermions, Fock Space and the Pauli Principle|§C5b.4]]): the neutrino–antineutrino pair of [[§C3.7★ Massless Particles and Helicity|§C3.7★]].
> - ⚑ By-product: half the components of a Weyl spinor are removed for each momentum; a Weyl field has one physical polarization per momentum, the minimal content of a massless spin-½ particle (the little-group count of [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]]).
> - For massive Dirac spinors helicity is frame dependent; it approaches chirality at high energy ([[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-4|Theorem §C5a.13.4]]).
> - Assumption: the plane wave solves the Weyl equation pointwise; as a field on spacetime it is not square integrable but a tempered distribution, and the equation holds also in $\mathcal S'$, as for the Dirac plane waves ([[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-5|§C5a.7, Remark: In what sense the equations hold]]).

^der-c5a-8-4

*Uses:* [[§C5a.8 The Weyl Form and the Weyl Equations#^mod-c5a-8-3|Model §C5a.8.3]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]]

> [!remark] Remark: Why "left-handed"
> The name comes from the massless solutions. By [[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-4|Theorem §C5a.8.4]], a positive-frequency solution of the left-handed Weyl equation, $\bar\sigma\cdot p\,\xi = 0$ with $p^0 = |\mathbf p|$, has $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\xi = -\xi$: its spin points against its momentum, helicity $-\frac12$. Curl the fingers of the left hand in the sense of the spin's rotation; the thumb then points along the motion — the screw sense of a left-handed helix. For a right-handed field the spin points along the momentum (right-hand rule). The label of the representation ($(\frac12, 0)$, $\gamma^5 = -1$: chirality, [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]]) was named after this property of its massless particles. With a mass the two notions separate: chirality is a Lorentz-invariant label of the field's representation, helicity a frame-dependent property of a state (a massive particle can be overtaken, which reverses $\hat{\mathbf p}$), and the mass term couples the two chiralities ([[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-2|§C5a.5, Remark: Kinematics allows one handedness, a mass needs both]]; helicity of the massive spinors: [[§C5a.13 Helicity Spinors and the Massless Limit|§C5a.13]]). In the massless limit of the Dirac spinors, negative helicity lives entirely in the left-handed half; the negative-frequency spinors are placed in the halves by [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-4|Theorem §C5a.13.4]], 3.
>
> The same question was asked at the start of Lecture 13, and Larsen answered it this way: a single Weyl field describes a massless particle, which moves at the speed of light, so "they really do have a well-defined direction of motion that all frames agree on, and right-handed means spin in the right-handed direction"; the name is not a convention. He added a warning: for antiparticles, wave-function spin and physical spin disagree ([[§C9.8 Physical Spin versus Wave-Function Spin|§C9.8]]), so the antiparticle of a left-handed field is right-handed — the antineutrino of the left-handed neutrino. "That will be a source of some confusion, but hopefully not too much."
>
> *Source: the user's question while working on Problem Set 7 (2026-10-13: "why is it called left-handed") · PHY 513 Lecture 13 (Larsen, 14 Oct 2026), transcript (question at the start of the lecture) · the user's PHY 513 notes, Ch. 8 (paragraph "Why 'left' and 'right'", added with Lecture 13) · the user's pre-course notes, §5.3 ("Weyl spinors") · PS §3.3, p. 47 (the high-energy limit as the origin of the names) · the screw-sense convention written here*

^rem-c5a-8-1

> [!remark] Remark: When the Weyl description is useful
> Not for the electron of Dirac's problem: in hydrogen the electron's kinetic energy is tiny compared with its mass, and the mass couples the two halves at full strength. It is natural where the mass is zero or small, as for neutrinos: in the Standard Model the neutrinos are massless and only left-handed ones exist. Their observed small masses require going beyond it. A mass of the form of [[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-2|Theorem §C5a.8.2]], a *Dirac* mass, needs a separate right-handed field.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.10 (paragraph "When is the Weyl description useful?") · PHY 513 Lecture 8, Part C*

^rem-c5a-8-2

> [!remark]- ★ Remark: A Majorana mass needs no second field
> By [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-6|Theorem §C3.2.6]] and [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-4|Theorem §C5a.5.4]], $\sigma^2\psi_L^{\ast}$ transforms like a right-handed spinor, so a single left-handed field can supply its own partner: $\psi_L^{\mathsf T}\varepsilon\,\psi_L$ is Lorentz invariant, because $\Lambda_L^{\mathsf T}\varepsilon\Lambda_L = (\det\Lambda_L)\varepsilon = \varepsilon$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]]). This is a *Majorana* mass. For commuting components it vanishes identically, $\psi^{\mathsf T}\varepsilon\psi = \psi_1\psi_2 - \psi_2\psi_1 = 0$ (with $\varepsilon^{12} = 1$); it exists only for anticommuting fields ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]; Majorana fields, QFT C9, planned). Whether neutrino masses are of Dirac or Majorana type is not known.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.10 (Caution "'A neutrino mass needs a right-handed neutrino'")*

^rem-c5a-8-3

> [!remark]- Connections
> - Chirality is a property of the Lorentz representation, helicity of a state; the Weyl equation ties them for massless particles, which is why a single Weyl field realizes one helicity of Wigner's massless classification — [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]], [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-4|Theorem §C5a.13.4]].
> - Mass breaks chiral symmetry because it pairs left with right; the same statement in group language is that $\gamma^0$, the invariant form, swaps the Weyl blocks — [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-13|Theorem §CB.18.13]], [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-2|§C5a.5, Remark: Kinematics allows one handedness, a mass needs both]].
