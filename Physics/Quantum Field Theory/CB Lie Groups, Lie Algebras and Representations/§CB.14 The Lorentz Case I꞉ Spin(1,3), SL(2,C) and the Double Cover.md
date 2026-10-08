---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.14
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.13 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)]] →

*Sources: P. Woit, Quantum Theory, Groups and Representations, §40.4 ("Spin and the Lorentz group": four-vectors as $x^0 + \mathbf x\cdot\boldsymbol\sigma$ and the action $\Omega(\cdot)\Omega^\dagger$) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · through the course homes embedded below: the user's PHY 513 notes, Ch. 7 §7.4, Ch. 8 §8.2; PHY 513 Lecture 7; Yu Zhao-Huan, 量子场论讲义, Exercise 3.7; Peskin & Schroeder, §3.1–§3.2 · the Clifford route and the comparison of conventions written here · for the complexification of real 𝔰𝔩(2,ℂ) and its representations: P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, Exercise 11.4, Remark 17.3 (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf) · P. Woit, Quantum Theory, Groups and Representations, §5.5 · the explicit map and the proof of the second theorem written here.*

What is the spin group of Minkowski space? The course reaches $SL(2, \mathbb C)$ through Hermitian $2\times2$ matrices ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]]–[[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]) and the representations $(j_+, j_-)$ through the complexified algebra ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]]). This section first complexifies the real Lie algebra $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ (two copies of $\mathfrak{sl}(2, \mathbb C)$) and splits its representations into a complex-linear and an antilinear part; then it gives the Clifford route: $\mathrm{Cl}^0(1,3) \cong \mathrm{Cl}(3,0) \cong M_2(\mathbb C)$, so $\mathrm{Spin}(1,3)_0 \cong SL(2, \mathbb C)$, with $\rho$ the course's covering map up to the automorphism $\lambda \mapsto (\lambda^\dagger)^{-1}$. The finite-dimensional representations of $SL(2, \mathbb C)$ (pairs of $\mathfrak{sl}(2, \mathbb C)$-representations, the $(j_+, j_-)$, and which of them descend to $SO^+(1,3)$) follow in [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)|§CB.15]]. It is the four-dimensional sequel of [[§CB.13 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half|§CB.13]], using [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification|§CB.3]]–[[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms|§CB.4]] (real forms, $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$) and [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.12]].

## The complexification of real 𝔰𝔩(2,ℂ) and its representations

> [!theorem] Theorem §CB.14.1: The Complexification of Real 𝔰𝔩(2,ℂ) Is Two Copies of 𝔰𝔩(2,ℂ)
> The map $\Phi : (\mathfrak{sl}(2, \mathbb C)_{\mathbb R})_{\mathbb C} \to \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$,
>
> $$
> \Phi(X + iY) = \bigl(X + iY,\ \bar X + i\bar Y\bigr) \qquad (X, Y \in \mathfrak{sl}(2, \mathbb C)_{\mathbb R};\ \bar X \text{ the entrywise conjugate}),
> $$
>
> is an isomorphism of complex Lie algebras. So the complexification of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ has complex dimension $6$ and is not $\mathfrak{sl}(2, \mathbb C)$; on the real algebra, $X \mapsto (X, \bar X)$.
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), Exercise 11.4 and Remark 17.3 ($\mathfrak g_{\mathbb C} \cong \mathfrak g\oplus\mathfrak g$ for a complex $\mathfrak g$ regarded as real) · Woit, §5.5 ($\mathfrak{gl}(n, \mathbb C)_{\mathbb C}$ is "built out of two copies") · the explicit map written here*

^thm-cb-14-1

> [!proof]- Proof
> *Source: P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, Exercise 11.4 ("Let $\mathfrak g$ be a complex Lie algebra. Show that $\mathfrak g_{\mathbb C} \cong \mathfrak g\oplus\mathfrak g$") and Remark 17.3 (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf); P. Woit, §5.5, on $\mathfrak{gl}(n, \mathbb C)_{\mathbb C}$ (https://www.math.columbia.edu/~woit/QM/qmbook.pdf). Etingof's statement is an exercise; the solution with the explicit map of the theorem (the second copy written with the conjugate matrix) is written here.*
>
> **Step 1** (what the symbols mean). An element of $(\mathfrak{sl}(2, \mathbb C)_{\mathbb R})_{\mathbb C}$ is a formal $X + iY$ with $X, Y$ traceless complex matrices ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-2|Def. §CB.3.2]]); the $i$ here is the new one, not the matrix scalar. In each component of $\Phi(X + iY)$, "$X + iY$" and "$\bar X + i\bar Y$" are computed with matrix operations, and both are traceless.
>
> **Step 2** (complex-linear). $\Phi$ is real-linear, and with $i(X + iY) = -Y + iX$:
>
> $$
> \Phi(-Y + iX) = \bigl(-Y + iX,\ -\bar Y + i\bar X\bigr) = i\bigl(X + iY,\ \bar X + i\bar Y\bigr) .
> $$
>
> **Step 3** (brackets). On the real algebra, $\Phi(X) = (X, \bar X)$ preserves brackets: $[X, X'] \mapsto ([X, X'], \overline{[X, X']}) = ([X, X'], [\bar X, \bar X'])$, entrywise conjugation being multiplicative. $\Phi$ is the complex-linear extension of this real Lie algebra homomorphism into the complex Lie algebra $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$, and such an extension preserves brackets by the four-term expansion of Step 2 of the proof of [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-6|Theorem §CB.3.6]] (with $d$ replaced by $X \mapsto (X, \bar X)$).
>
> **Step 4** (injective). If $\Phi(X + iY) = 0$, then $X + iY = 0$ and $\bar X + i\bar Y = 0$ as matrices. Conjugating the second entrywise, $X - iY = 0$. Adding and subtracting: $X = 0$, $Y = 0$.
>
> **Step 5** (bijective). $\dim_{\mathbb C}(\mathfrak{sl}(2, \mathbb C)_{\mathbb R})_{\mathbb C} = \dim_{\mathbb R}\mathfrak{sl}(2, \mathbb C)_{\mathbb R} = 6$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-3|Theorem §CB.3.3]]; [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^def-cb-4-5|Def. §CB.4.5]]) $= \dim_{\mathbb C}(\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C))$, so the injective linear $\Phi$ is bijective: an isomorphism of complex Lie algebras. In particular the complexification has complex dimension $6$ and is not $\mathfrak{sl}(2, \mathbb C)$ (dimension $3$).
>
> **What the proof shows.**
> - ⚑ By-product: "complexify by allowing complex coefficients" fails for an algebra already closed under $i$; the abstract $i$ and the matrix $i$ are different, and the second copy carries the conjugate matrices. This is the algebraic origin of the conjugate representation $\Lambda \mapsto \bar\Lambda$ of $SL(2, \mathbb C)$ (Theorem §CB.14.2).
> - Composed with Theorem §CB.4.6, this gives $\mathfrak{so}(1,3)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ once more, consistently with Theorem §CB.4.1.

^pf-cb-14-1

*Uses:* [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-2|Def. §CB.3.2]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^def-cb-4-5|Def. §CB.4.5]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-3|Theorem §CB.3.3]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-6|Theorem §CB.3.6]]

> [!theorem] Theorem §CB.14.2: Representations of Real 𝔰𝔩(2,ℂ): a Complex-Linear and an Antilinear Part
> Let $\rho : \mathfrak{sl}(2, \mathbb C)_{\mathbb R} \to \operatorname{End}_{\mathbb C}(W)$ be a representation on a complex vector space $W$. There are unique maps $\rho_1$, $\rho_2$ with $\rho = \rho_1 + \rho_2$, $\rho_1$ complex-linear and $\rho_2$ complex-antilinear ($\rho_2(iX) = -i\rho_2(X)$), both Lie algebra homomorphisms, and $[\rho_1(X), \rho_2(Y)] = 0$ for all $X, Y$. Conversely every such commuting pair gives a representation. The defining representation $X \mapsto X$ on $\mathbb C^2$ has $\rho_2 = 0$; its complex conjugate $X \mapsto \bar X$ has $\rho_1 = 0$.
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), Exercise 11.4 ("$\mathrm{Rep}_{\mathbb R}G \cong \mathrm{Rep}(\mathfrak g\oplus\mathfrak g)$" for a complex $G$ regarded as real) · written here (from Theorem §CB.14.1 and Theorem §CB.3.6)*

^thm-cb-14-2

> [!proof]- Proof
> *Written here from Theorems §CB.3.6 and §CB.14.1; it is the Lie-algebra half of P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, Exercise 11.4, second sentence (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), which is stated there without proof.*
>
> **Step 1** (pass to two copies). Extend $\rho$ complex-linearly to $\rho_{\mathbb C}$ on $(\mathfrak{sl}(2, \mathbb C)_{\mathbb R})_{\mathbb C}$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-6|Theorem §CB.3.6]]) and set $\sigma = \rho_{\mathbb C}\circ\Phi^{-1}$ with $\Phi$ of [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-1|Theorem §CB.14.1]]: a complex-linear representation of $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ on $W$. Put $\sigma_1(A) = \sigma(A, 0)$, $\sigma_2(B) = \sigma(0, B)$. Both are complex-linear representations of $\mathfrak{sl}(2, \mathbb C)$, and they commute: $[\sigma_1(A), \sigma_2(B)] = \sigma([(A, 0), (0, B)]) = \sigma(0) = 0$.
>
> **Step 2** (existence). For $X$ in the real algebra, $\Phi(X) = (X, \bar X) = (X, 0) + (0, \bar X)$, so $\rho(X) = \rho_{\mathbb C}(X) = \sigma_1(X) + \sigma_2(\bar X)$. Put $\rho_1(X) = \sigma_1(X)$ and $\rho_2(X) = \sigma_2(\bar X)$. Then $\rho_1$ is complex-linear; $\rho_2(iX) = \sigma_2(\overline{iX}) = \sigma_2(-i\bar X) = -i\rho_2(X)$ is antilinear; both preserve brackets (for $\rho_2$ because $\overline{[X, Y]} = [\bar X, \bar Y]$); and they commute by Step 1.
>
> **Step 3** (uniqueness). If $\rho = \rho_1 + \rho_2$ with $\rho_1$ complex-linear and $\rho_2$ antilinear, then $\rho(iX) = i\rho_1(X) - i\rho_2(X)$, so $-i\rho(iX) = \rho_1(X) - \rho_2(X)$ and
>
> $$
> \rho_1(X) = \tfrac12\bigl(\rho(X) - i\rho(iX)\bigr), \qquad \rho_2(X) = \tfrac12\bigl(\rho(X) + i\rho(iX)\bigr):
> $$
>
> both are determined by $\rho$.
>
> **Step 4** (converse). If $\rho_1$, $\rho_2$ are bracket-preserving, complex-linear resp. antilinear, and $[\rho_1(X), \rho_2(Y)] = 0$ for all $X, Y$, then $\rho = \rho_1 + \rho_2$ is real-linear and, expanding all four terms and dropping the two mixed ones,
>
> $$
> [\rho(X), \rho(Y)] = [\rho_1X, \rho_1Y] + [\rho_1X, \rho_2Y] + [\rho_2X, \rho_1Y] + [\rho_2X, \rho_2Y] = \rho_1[X, Y] + \rho_2[X, Y] = \rho([X, Y]) .
> $$
>
> **Step 5** (the two examples). For $\rho(X) = X$: $\rho(iX) = iX$, so Step 3 gives $\rho_2(X) = \frac12(X + i\cdot iX) = 0$. For $\rho(X) = \bar X$: $\rho(iX) = -i\bar X$, so $\rho_1(X) = \frac12(\bar X - i(-i\bar X)) = \frac12(\bar X - \bar X) = 0$.
>
> **What the proof shows.**
> - ⚑ By-product: a representation of $SL(2, \mathbb C)$ regarded as a real group is labelled by two complex-linear pieces, one "holomorphic", one "antiholomorphic"; through Theorem §CB.4.6 these become the two commuting angular momenta behind the labels $(j_+, j_-)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]; which of the defining representation and its conjugate is called $(\frac12, 0)$ is a convention fixed there).
> - The decomposition needs $W$ complex; antilinearity of $\rho_2$ is relative to the complex structure of $\mathfrak{sl}(2, \mathbb C)$, not of $W$.

^pf-cb-14-2

*Uses:* [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-6|Theorem §CB.3.6]], [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-1|Theorem §CB.14.1]]

Throughout, $V = \mathbb R^{1,3}$ with $q(x) = g(x, x)$, $g = \operatorname{diag}(+,-,-,-)$, and $e_0, \dots, e_3$ the standard basis ($q(e_0) = 1$, $q(e_i) = -1$).

## The even Clifford algebra of Minkowski space

> [!theorem] Theorem §CB.14.3: Cl⁰(1,3) ≅ Cl(3,0) ≅ M₂(ℂ)
> The elements $f_i = e_ie_0$ ($i = 1, 2, 3$) of $\mathrm{Cl}^0(1,3)$ satisfy $f_i^2 = +1$ and $f_if_j = -f_jf_i$ ($i \ne j$), and $e_i \mapsto f_i$ extends to an isomorphism $\mathrm{Cl}(3,0) \cong \mathrm{Cl}^0(1,3)$ ([[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-10-10|Theorem §CB.10.10]] with $\epsilon = 1$). Composed with [[§CB.13 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-13-1|Theorem §CB.13.1]] it gives an isomorphism of real algebras $\phi : \mathrm{Cl}^0(1,3) \to M_2(\mathbb C)$, $\phi(f_i) = \sigma^i$, with $\phi(\omega) = i\mathbb 1$ for $\omega = e_0e_1e_2e_3 = f_1f_2f_3$. Under $\phi$ the map $x \mapsto xe_0$, $V \to \mathrm{Cl}^0$, sends $x = x^\mu e_\mu$ to the Hermitian matrix $\tilde x = x^0\mathbb 1 + x^i\sigma^i$, which is $\bar X = x_\mu\bar\sigma^\mu$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]] (not the course's $X = x_\mu\sigma^\mu$).
>
> *Source: written here · the matrices $x^0 + \mathbf x\cdot\boldsymbol\sigma$ for four-vectors: P. Woit, Quantum Theory, Groups and Representations, §40.4*

^thm-cb-14-3

> [!proof]- Proof
> Orthogonal vectors anticommute in $\mathrm{Cl}(1,3)$: $uv + vu = 2B(u, v)$ ([[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-9-8|Theorem §CB.9.8]]), and $e_\mu \perp e_\nu$ for $\mu \ne \nu$. Also $e_0^2 = q(e_0) = 1$ and $e_i^2 = q(e_i) = -1$.
>
> **1. Squares.** $f_i^2 = e_ie_0e_ie_0 = -e_ie_ie_0e_0 = -(-1)(1) = 1$, moving the middle $e_0$ past $e_i$ (one sign).
>
> **2. Anticommutation.** For $i \ne j$: $f_if_j = e_ie_0e_je_0 = -e_ie_je_0e_0 = -e_ie_j$, and likewise $f_jf_i = -e_je_i = e_ie_j$. So $f_if_j = -f_jf_i$. ⚑ By-product: $e_ie_j = -f_if_j$, used for the rotation generators in Theorem §CB.14.5.
>
> **3. The even subalgebra is Cl(3,0).** In Theorem §CB.10.10 take $e_0$ with $q(e_0) = \epsilon = 1$; then $V' = e_0^\perp = \operatorname{span}\{e_1, e_2, e_3\}$ with $q'(v') = -\epsilon q(v') = -q(v')$, so $q'(e_i) = +1$: $(V', q') = \mathbb R^{3,0}$. The isomorphism $\mathrm{Cl}(3,0) \cong \mathrm{Cl}^0(1,3)$ of that theorem is $v' \mapsto v'e_0$, i.e. $e_i \mapsto f_i$; steps 1–2 are the relations it requires.
>
> **4. The matrix algebra.** Theorem §CB.13.1 gives the real-algebra isomorphism $\mathrm{Cl}(3,0) \cong M_2(\mathbb C)$, $e_i \mapsto \sigma^i$. Composing with the inverse of step 3 gives $\phi$ with $\phi(f_i) = \sigma^i$. In particular the $f_i$ generate $\mathrm{Cl}^0(1,3)$ as a real algebra, since the $e_i$ generate $\mathrm{Cl}(3,0)$.
>
> **5. The volume element.** $f_1f_2 = -e_1e_2$ (step 2), so $f_1f_2f_3 = -e_1e_2e_3e_0$. Moving $e_0$ to the front past $e_3$, $e_2$, $e_1$ costs $(-1)^3$: $f_1f_2f_3 = e_0e_1e_2e_3 = \omega$. Hence $\phi(\omega) = \sigma^1\sigma^2\sigma^3 = i\mathbb 1$ (Theorem §CB.13.1).
>
> **6. Four-vectors.** $xe_0 = x^0e_0e_0 + x^ie_ie_0 = x^0 + x^if_i$, so $\phi(xe_0) = x^0\mathbb 1 + x^i\sigma^i$. With $x_0 = x^0$, $x_i = -x^i$ and $\bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma)$ (Def. §C5a.1.10), $x_\mu\bar\sigma^\mu = x^0\mathbb 1 + x^i\sigma^i = \bar X$.
>
> **What the proof shows**
> - The course's Hermitian $2\times2$ picture of a four-vector is the Clifford product $xe_0$, read in $\mathrm{Cl}^0 \cong M_2(\mathbb C)$.
> - ⚑ By-product (a convention): the natural Clifford identification gives $\bar X = x_\mu\bar\sigma^\mu$, while the course's covering map is built on $X = x_\mu\sigma^\mu$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]]). The two differ by $\sigma^i \to -\sigma^i$; its effect on the group is worked out in Theorem §CB.14.4, 2.
> - Used next: Theorems §CB.14.4–§CB.14.5, and the Dirac module in §CB.16.

^pf-cb-14-3

*Uses:* [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-9-8|Theorem §CB.9.8]], [[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-10-10|Theorem §CB.10.10]], [[§CB.13 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-13-1|Theorem §CB.13.1]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]]

## Spin(1,3) and SL(2,ℂ)

> [!theorem] Theorem §CB.14.4: Spin(1,3)₀ Is SL(2,ℂ), and ρ Is the Course's Covering Map up to λ ↦ (λ†)⁻¹
> 1. The isomorphism $\phi$ of [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-3|Theorem §CB.14.3]] restricts to an isomorphism of Lie groups from $\mathrm{Spin}(1,3)_0$ ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-12-6|Def. §CB.12.6]]) onto $SL(2, \mathbb C)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-3|Def. §C5a.4.3]]).
> 2. For $x \in \mathrm{Spin}(1,3)_0$ and $\lambda = \phi(x)$, $\rho(x)$ ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-7|Theorem §CB.12.7]]) acts on $\tilde x = x_\mu\bar\sigma^\mu$ (Theorem §CB.14.3) by $\tilde x \mapsto \lambda\tilde x\lambda^\dagger$, and $\ker\rho = \{\pm1\}$ ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-12|Theorem §CB.12.12]]). The course's covering $\pi : SL(2, \mathbb C) \to SO^+(1,3)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]) acts instead on $X = x_\mu\sigma^\mu$ by $X \mapsto \mu X\mu^\dagger$, and
>
> $$
> \rho(x) = \pi\bigl(\theta(\phi(x))\bigr), \qquad \theta(\lambda) = (\lambda^\dagger)^{-1} .
> $$
>
> So the element of $\mathrm{Spin}(1,3)_0$ over $e^\omega$ is sent by $\phi$ to $\pm\Lambda_R(\omega)$ and by $\theta\circ\phi$ to $\pm\Lambda_L(\omega)$ (the Weyl matrices, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]]); $\theta\circ\phi$ is the restriction of the real-algebra isomorphism $\phi' : \mathrm{Cl}^0(1,3) \to M_2(\mathbb C)$ with $\phi'(f_i) = -\sigma^i$, $\phi'(xe_0) = X$, and $\rho = \pi\circ\phi'$ on $\mathrm{Spin}(1,3)_0$.
> 3. $\phi$ maps $\mathrm{Spin}(1,3)$ onto $\{A \in M_2(\mathbb C) : \det A = \pm1\}$. $\mathrm{Spin}(1,3)$ has two components, $\mathrm{Spin}(1,3)_0$ and $e_0e_1\,\mathrm{Spin}(1,3)_0$; $\rho(e_0e_1) = \operatorname{diag}(-1, -1, 1, 1)$, and $\rho$ maps the two components onto $SO^+(1,3)$ and onto $\mathcal P\mathcal T\cdot SO^+(1,3)$, the component of $SO(1,3)$ containing $\mathcal P\mathcal T$ ([[§C1a.4 The Lorentz Group#^thm-c1a-4-2|Theorem §C1a.4.2]]).
>
> *Source: written here · the action $\Omega(\cdot)\Omega^\dagger$ on $x^0 + \mathbf x\cdot\boldsymbol\sigma$: P. Woit, Quantum Theory, Groups and Representations, §40.4 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the course's covering: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (the user's PHY 513 notes, Ch. 8 §8.2; Yu Exercise 3.7)*

^thm-cb-14-4

> [!proof]- Proof
> Notation: $\tilde v = \phi(ve_0) = v_\mu\bar\sigma^\mu$ for $v \in V$ (Theorem §CB.14.3, 6); $\theta(\lambda) = (\lambda^\dagger)^{-1}$.
>
> **1. Conjugation by e₀.** Since $e_0^2 = 1$, $\kappa(a) = e_0ae_0$ is an algebra automorphism of $\mathrm{Cl}^0(1,3)$: $\kappa(ab) = e_0ae_0e_0be_0 = \kappa(a)\kappa(b)$. On the generators, $\kappa(f_i) = e_0e_ie_0e_0 = e_0e_i = -e_ie_0 = -f_i$.
>
> **2. Its matrix form.** $\tilde\kappa(A) = \sigma^2\bar A\sigma^2$ ($\bar A$ the entrywise conjugate) is a real-algebra automorphism of $M_2(\mathbb C)$: real-linear, $\tilde\kappa(AB) = \sigma^2\bar A\sigma^2\sigma^2\bar B\sigma^2 = \tilde\kappa(A)\tilde\kappa(B)$ because $(\sigma^2)^2 = \mathbb 1$, $\tilde\kappa(\mathbb 1) = \mathbb 1$. By [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-9|Theorem §C5a.1.9]], 3, $\sigma^2(\sigma^i)^{\ast}\sigma^2 = -\sigma^i$, so $\tilde\kappa(\sigma^i) = -\sigma^i$. Thus $\phi\circ\kappa$ and $\tilde\kappa\circ\phi$ are real-algebra homomorphisms $\mathrm{Cl}^0 \to M_2(\mathbb C)$ that agree on the generators $f_i$ (both give $-\sigma^i$; Theorem §CB.14.3, 4), hence everywhere: $\phi(\kappa(a)) = \tilde\kappa(\phi(a))$.
>
> **3. On determinant ±1, κ̃ is ±θ.** By [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-15|Theorem §CB.6.15]], 1, applied to $\bar A$: $\bar A^{\mathsf T}\varepsilon\bar A = \overline{\det A}\,\varepsilon$, so for invertible $A$, $\varepsilon\bar A\varepsilon^{-1} = \overline{\det A}\,(\bar A^{\mathsf T})^{-1} = \overline{\det A}\,(A^\dagger)^{-1}$. With $\varepsilon = i\sigma^2$, $\varepsilon^{-1} = -i\sigma^2$, the left side is $\sigma^2\bar A\sigma^2$. Hence
>
> $$
> \tilde\kappa(A) = \overline{\det A}\;\theta(A), \qquad \text{in particular } \tilde\kappa = \theta \text{ on } SL(2, \mathbb C) .
> $$
>
> **4. The determinant of a product of two vectors.** For $u, v \in V$: $uv = (ue_0)(e_0v)$ and $e_0v = e_0(ve_0)e_0 = \kappa(ve_0)$. So $\phi(uv) = \tilde u\,\tilde\kappa(\tilde v)$, and $\det\phi(uv) = \det\tilde u\cdot\overline{\det\tilde v} = q(u)\,q(v)$, since $\det\tilde v = \det(v_\mu\bar\sigma^\mu) = v_\mu v^\mu = q(v)$ is real ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], 2).
>
> **5. Spin(1,3)₀ lands in SL(2,ℂ).** Every $x \in \mathrm{Spin}(1,3)$ is $u_1u_2\cdots u_{2k}$ with $q(u_i) = \pm1$ (Def. §CB.12.6). Grouping the factors in pairs and using step 4 and $\det(AB) = \det A\det B$: $\det\phi(x) = \prod_iq(u_i) = \pm1$. On $\mathrm{Spin}(1,3)_0$, $\det\circ\phi$ is continuous with values in $\{\pm1\}$ and equals $1$ at $x = 1$; $\mathrm{Spin}(1,3)_0$ is connected ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-5|Theorem §CB.2.5]], 1), so $\det\phi(x) = 1$.
>
> **6. The action on four-vectors.** For $x \in \mathrm{Spin}(1,3)$ and $v \in V$, $\rho(x)v = xvx^{-1}$ (Theorem §CB.12.7, 2). Inserting $e_0e_0 = 1$: $(\rho(x)v)e_0 = x(ve_0)(e_0x^{-1}e_0) = x\,(ve_0)\,\kappa(x^{-1})$. Apply $\phi$, step 2 and step 3 with $d = \det\phi(x) = \pm1$ (so $\overline{\det\phi(x)^{-1}} = d$ and $\theta(\lambda^{-1}) = \lambda^\dagger$):
>
> $$
> \widetilde{\rho(x)v} = \lambda\,\tilde v\,\tilde\kappa(\lambda^{-1}) = d\,\lambda\,\tilde v\,\lambda^\dagger, \qquad \lambda = \phi(x) .
> $$
>
> For $x \in \mathrm{Spin}(1,3)_0$ ($d = 1$, step 5) this is $\tilde v \mapsto \lambda\tilde v\lambda^\dagger$, the first claim of part 2.
>
> **7. Comparison with π.** $X = v_\mu\sigma^\mu = v^0\mathbb 1 - v^i\sigma^i = \tilde\kappa(\tilde v)$ (step 2, real coefficients). Applying the automorphism $\tilde\kappa$ to step 6 ($d = 1$): $X \mapsto \tilde\kappa(\lambda)\,X\,\tilde\kappa(\lambda^\dagger) = \theta(\lambda)\,X\,\theta(\lambda^\dagger)$, and $\theta(\lambda^\dagger) = \lambda^{-1} = \theta(\lambda)^\dagger$. So $\rho(x)$ acts on $X$ as $X \mapsto \mu X\mu^\dagger$ with $\mu = \theta(\lambda)$, which is the definition of $\pi(\mu)$ (Theorem §C5a.4.4): $\rho(x) = \pi(\theta(\phi(x)))$.
>
> **8. Onto SL(2,ℂ).** Let $\mu \in SL(2, \mathbb C)$. $\pi(\theta(\mu)) \in SO^+(1,3)$, and $SO^+(1,3)$ is the identity component of $O(1,3)$ ([[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], 2). $V = \mathbb R^{1,3}$ contains the negative definite plane $\operatorname{span}\{e_1, e_2\}$, so $\rho : \mathrm{Spin}(1,3)_0 \to SO^+(1,3)$ is onto and $-1 \in \mathrm{Spin}(1,3)_0$ (Theorem §CB.12.12). Pick $x$ with $\rho(x) = \pi(\theta(\mu))$; by step 7, $\pi(\theta(\phi(x))) = \pi(\theta(\mu))$, so $\theta(\phi(x)) = \pm\theta(\mu)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]]) and $\phi(x) = \pm\mu$ ($\theta$ is a bijection with $\theta(-\lambda) = -\theta(\lambda)$). If the sign is $-$, replace $x$ by $-x \in \mathrm{Spin}(1,3)_0$. So $\phi(\mathrm{Spin}(1,3)_0) = SL(2, \mathbb C)$.
>
> **9. Part 1.** $\phi$ is an injective algebra homomorphism and a linear isomorphism of finite-dimensional spaces, so its restriction to $\mathrm{Spin}(1,3)_0$ is an injective group homomorphism, continuous with continuous inverse, onto $SL(2, \mathbb C)$ by step 8: an isomorphism of Lie groups ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]]).
>
> **10. The kernel and the Weyl matrices.** $\rho(x) = \mathbb 1$ iff $\theta(\phi(x)) = \pm\mathbb 1$ (step 7, Theorem §C5a.4.5) iff $\phi(x) = \pm\mathbb 1$ iff $x = \pm1$. Since $\pi(\Lambda_L(\omega)) = e^\omega$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]], 1), $\rho(x) = e^\omega$ iff $\theta(\phi(x)) = \pm\Lambda_L(\omega)$ iff $\phi(x) = \pm\theta(\Lambda_L(\omega)) = \pm\Lambda_R(\omega)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], 2). Finally $\phi' = \tilde\kappa\circ\phi$ is a real-algebra isomorphism with $\phi'(f_i) = -\sigma^i$ and $\phi'(xe_0) = \tilde\kappa(\tilde x) = X$, equal to $\theta\circ\phi$ on $\mathrm{Spin}(1,3)_0$ (step 3), so $\rho = \pi\circ\phi'$ there.
>
> **11. Part 3.** By step 5, $\phi(\mathrm{Spin}(1,3)) \subset \{\det = \pm1\}$. $e_0e_1 \in \mathrm{Spin}(1,3)$, $e_0e_1 = -e_1e_0 = -f_1$, $\phi(e_0e_1) = -\sigma^1$ with determinant $-1$, and $(e_0e_1)^2 = -e_0e_0e_1e_1 = 1$. If $y \in \mathrm{Spin}(1,3)$ has $\det\phi(y) = -1$, then $e_0e_1y \in \mathrm{Spin}(1,3)$ has determinant $1$, so $\phi(e_0e_1y) \in SL(2, \mathbb C) = \phi(\mathrm{Spin}(1,3)_0)$ and, $\phi$ being injective, $e_0e_1y \in \mathrm{Spin}(1,3)_0$, i.e. $y \in e_0e_1\mathrm{Spin}(1,3)_0$. The two pieces are the preimages of $\det = 1$ and $\det = -1$, disjoint, open and closed, each connected (homeomorphic to $\mathrm{Spin}(1,3)_0$); their images under $\phi$ fill $\{\det = \pm1\}$ ($\phi(e_0e_1)SL(2, \mathbb C) = \{\det = -1\}$). By Theorem §CB.12.7, 2, $\rho(e_0e_1) = r_{e_0}r_{e_1}$, the product of the reflections $e_0 \mapsto -e_0$ and $e_1 \mapsto -e_1$ ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-4|Theorem §CB.12.4]]): $\operatorname{diag}(-1, -1, 1, 1)$, with determinant $+1$ and $\Lambda^0{}_0 = -1$, the same signs as $\mathcal P\mathcal T = -\mathbb 1$, so it lies in $\mathcal P\mathcal T\cdot SO^+(1,3)$ (Theorem §C1a.4.2, 1–2), and $\rho(e_0e_1\mathrm{Spin}(1,3)_0) = \rho(e_0e_1)\,SO^+(1,3) = \mathcal P\mathcal T\cdot SO^+(1,3)$.
>
> **What the proof shows**
> - The Clifford route and the course's route reach the same group, but the natural identifications differ by the automorphism $\theta(\lambda) = (\lambda^\dagger)^{-1}$, which exchanges $\Lambda_L$ and $\Lambda_R$. ⚑ By-product: "which matrix is $\lambda$" is a convention, fixed in the course by building $\pi$ on $X = x_\mu\sigma^\mu$; the Clifford algebra with $f_i \mapsto \sigma^i$ builds it on $\bar X$. Every later statement that names $(\frac12, 0)$ fixes the convention (Theorem §CB.15.2, Theorem §CB.16.2).
> - Step 6 for $d = -1$ shows that the other component acts by $\tilde v \mapsto -\lambda\tilde v\lambda^\dagger$: the minus sign reverses time, as $\mathcal P\mathcal T$ does.
> - Used next: the Lie algebra version (Theorem §CB.14.5) and the Dirac module restricted to $\mathrm{Spin}(1,3)_0$ (Theorem §CB.16.2).

^pf-cb-14-4

*Uses:* [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-3|Theorem §CB.14.3]], [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-12-6|Def. §CB.12.6]], [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-4|Theorem §CB.12.4]], [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-7|Theorem §CB.12.7]], [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-12|Theorem §CB.12.12]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-15|Theorem §CB.6.15]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-5|Theorem §CB.2.5]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-9|Theorem §C5a.1.9]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-2|Theorem §C1a.4.2]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]]

The course's route — four-vectors as Hermitian matrices, $SL(2, \mathbb C)$ connected and simply connected, the double cover — proved in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (both routes are kept):

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2]]

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3]]

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7]]

> [!theorem] Theorem §CB.14.5: The Three Lie Algebras Agree
> Under $\phi$ ([[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-3|Theorem §CB.14.3]]), $\mathfrak{spin}(1,3)$ ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-12-13|Def. §CB.12.13]]) maps isomorphically onto $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^def-cb-4-5|Def. §CB.4.5]]): $\frac12e_ie_j = -\frac12f_if_j \mapsto -\frac i2\varepsilon_{ijk}\sigma^k$ (rotations) and $\frac12e_ie_0 \mapsto \frac12\sigma^i$ (boosts). The differential $\rho_\ast$ ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-14|Theorem §CB.12.14]]) is $\rho_\ast(\frac12e_\mu e_\nu) = M_{\mu\nu} = g_{\mu\alpha}g_{\nu\beta}M^{\alpha\beta}$, the generators of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]] with lowered indices; so $\rho_\ast\circ\phi^{-1}$ sends $-\frac i2\sigma^k \mapsto -iJ_k$ and $\frac12\sigma^k \mapsto -iK_k$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]). It equals $\pi_\ast\circ\theta_\ast$, with $\pi_\ast$ the isomorphism of [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-6|Theorem §CB.4.6]] ($-\frac i2\sigma^k \mapsto -iJ_k$, $-\frac12\sigma^k \mapsto -iK_k$) and $\theta_\ast(Y) = -Y^\dagger$ the differential of $\theta(\lambda) = (\lambda^\dagger)^{-1}$ ([[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-4|Theorem §CB.14.4]]).
>
> *Source: written here*

^thm-cb-14-5

> [!proof]- Proof
> **1. A basis.** $\mathfrak{spin}(1,3)$ is spanned by the six products $e_\mu e_\nu$, $\mu < \nu$ (Def. §CB.12.13), and it is the Lie algebra of $\mathrm{Spin}(1,3)$ (Theorem §CB.12.14, 1).
>
> **2. The images.** $\phi(e_ie_0) = \phi(f_i) = \sigma^i$. For $i \ne j$, $e_ie_j = -f_if_j$ (Theorem §CB.14.3, Proof, step 2), and $\sigma^i\sigma^j = i\varepsilon_{ijk}\sigma^k$ for $i \ne j$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], 3), so $\phi(\frac12e_ie_j) = -\frac12\sigma^i\sigma^j = -\frac i2\varepsilon_{ijk}\sigma^k$.
>
> **3. An isomorphism onto 𝔰𝔩(2,ℂ)_ℝ.** The images $\frac12\sigma^k$, $-\frac i2\sigma^k$ ($k = 1, 2, 3$) are a real basis of the traceless matrices, because $\sigma^1, \sigma^2, \sigma^3$ are a complex basis of them (QM Theorem §B6.1.4, 4). These form $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$, of real dimension $6$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]). $\phi$ is injective and multiplicative, so it preserves commutators, and its restriction is a Lie algebra isomorphism $\mathfrak{spin}(1,3) \cong \mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ — consistently with $\phi(\mathrm{Spin}(1,3)_0) = SL(2, \mathbb C)$ (Theorem §CB.14.4, 1).
>
> **4. The differential of ρ in components.** By Theorem §CB.12.14, 2, $\rho_\ast(\frac12e_\mu e_\nu)(v) = B(e_\nu, v)e_\mu - B(e_\mu, v)e_\nu = v_\nu e_\mu - v_\mu e_\nu$, i.e. the matrix $(\rho_\ast(\frac12e_\mu e_\nu))^\rho{}_\sigma = \delta^\rho_\mu g_{\nu\sigma} - \delta^\rho_\nu g_{\mu\sigma}$. Lowering both labels of $(M^{\alpha\beta})^\rho{}_\sigma = g^{\alpha\rho}\delta^\beta_\sigma - g^{\beta\rho}\delta^\alpha_\sigma$ (Def. §C1a.6.1): $g_{\mu\alpha}g_{\nu\beta}(M^{\alpha\beta})^\rho{}_\sigma = \delta^\rho_\mu g_{\nu\sigma} - \delta^\rho_\nu g_{\mu\sigma}$. So $\rho_\ast(\frac12e_\mu e_\nu) = M_{\mu\nu}$.
>
> **5. Rotations and boosts.** For spatial $i, j$: $M_{ij} = g_{ii}g_{jj}M^{ij} = M^{ij} = -i\mathcal J^{ij} = -i\varepsilon_{ijk}J_k$, since $J_k = \frac12\varepsilon_{klm}\mathcal J^{lm}$ gives $\mathcal J^{ij} = \varepsilon_{ijk}J_k$ (Def. §C1a.6.2). With step 2: $\rho_\ast\phi^{-1}(-\frac i2\varepsilon_{ijk}\sigma^k) = -i\varepsilon_{ijk}J_k$, i.e. $-\frac i2\sigma^k \mapsto -iJ_k$. For boosts: $M_{k0} = g_{kk}g_{00}M^{k0} = -M^{k0} = M^{0k} = -i\mathcal J^{0k} = -iK_k$, and $\phi(\frac12e_ke_0) = \frac12\sigma^k$, so $\frac12\sigma^k \mapsto -iK_k$. Check on $v$: $\rho_\ast(\frac12e_ke_0)$ sends $e_0 \mapsto e_k$ and $e_k \mapsto e_0$, the generator of a boost along $+e_k$.
>
> **6. Comparison with the differential of π.** $\theta$ is a continuous homomorphism of $SL(2, \mathbb C)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], Derivation, step 1), and $\theta(e^{sY}) = ((e^{sY})^\dagger)^{-1} = e^{-sY^\dagger}$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], 2 and 4), so $\theta_\ast(Y) = \frac{d}{ds}e^{-sY^\dagger}\big|_0 = -Y^\dagger$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]). Then $\theta_\ast(-\frac i2\sigma^k) = -\frac i2\sigma^k$ and $\theta_\ast(\frac12\sigma^k) = -\frac12\sigma^k$, and Theorem §CB.4.6 gives $\pi_\ast\theta_\ast(-\frac i2\sigma^k) = -iJ_k$, $\pi_\ast\theta_\ast(\frac12\sigma^k) = -iK_k$: the same values as step 5 on a basis, so $\rho_\ast\circ\phi^{-1} = \pi_\ast\circ\theta_\ast$. (This is also the chain rule applied to $\rho = \pi\circ\theta\circ\phi$, Theorem §CB.14.4, 2.)
>
> **What the proof shows**
> - $\rho_\ast(\frac12e_\mu e_\nu) = M_{\mu\nu}$: in the Clifford algebra the generator of the $\mu\nu$-plane is half the product of the two basis vectors, with the metric lowering the labels. Hence $\exp(\frac14\omega^{\mu\nu}e_\mu e_\nu)$ covers $e^\omega = \exp(\frac12\omega_{\mu\nu}M^{\mu\nu})$, used in Theorem §CB.16.2.
> - ⚑ By-product: rotations are the same through $\phi$ and through the course's $\pi$; boosts differ by a sign. That sign is the automorphism $\theta$, i.e. the exchange of $\Lambda_L$ and $\Lambda_R$ (Theorem §CB.14.4, 2).

^pf-cb-14-5

*Uses:* [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-12-13|Def. §CB.12.13]], [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-14|Theorem §CB.12.14]], [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-3|Theorem §CB.14.3]], [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-4|Theorem §CB.14.4]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-6|Theorem §CB.4.6]]

> [!remark]- Connections
> - The two routes to $SL(2, \mathbb C)$ meet at Theorem §CB.14.3: the Hermitian matrix $x^0 + \mathbf x\cdot\boldsymbol\sigma = x_\mu\bar\sigma^\mu$ is the Clifford product $x\,e_0$, and $\lambda\tilde x\lambda^\dagger$ is conjugation in the Clifford algebra read through $e_0$. The course builds its covering on $x_\mu\sigma^\mu$ instead; the two differ by $\lambda \mapsto (\lambda^\dagger)^{-1}$ (Theorem §CB.14.4, 2), which is why the Clifford identification calls $\Lambda_R$ what the course calls $\Lambda_L$.
> - **Used in**: Theorems §CB.14.1–§CB.14.2 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-3|Def. §C5a.4.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]; Theorems §CB.14.3–§CB.14.5 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]]
