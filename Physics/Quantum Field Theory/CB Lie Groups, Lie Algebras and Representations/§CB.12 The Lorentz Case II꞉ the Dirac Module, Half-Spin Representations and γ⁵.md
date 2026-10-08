---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.12
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.13 Projective Representations, Wigner's Theorem and Antiunitary Symmetries]] →

*Sources (planned for the proofs; each to be checked against the text when the proof is written): PHY 513 TA (oral remark, Oct 2026) · Peskin & Schroeder, §§3.2–3.4 · the user's PHY 513 notes, Ch. 8 §§8.1–8.3, §8.9 · PHY 513 Lectures 7–8 · Yu Zhao-Huan, 量子场论讲义, §5.1 · P. Woit, Quantum Theory, Groups and Representations, §41.2 "Dirac γ matrices and Cliff(3,1)", Ch. 47 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · D. Tong, Lectures on Quantum Field Theory, chapter "The Dirac Equation" (https://www.damtp.cam.ac.uk/user/tong/qft.html) · the rest written here.*

What is the Dirac spinor as a representation of $\mathrm{Spin}(1,3)_0 = SL(2, \mathbb C)$, and where do $\gamma^5$, the Weyl halves, the bispinor form of a four-vector and the sixteen bilinears come from? This section specializes the TA's theorem ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-20|Theorem §CB.9.20]]) to Minkowski space: the Dirac module $\mathbb C^4$ restricts to $S^+\oplus S^- = (\frac12, 0)\oplus(0, \frac12)$, split by the complex volume element $\gamma^5$; Clifford multiplication exchanges the halves; the complexified vector is $S^+\otimes S^-$; two-forms are $(1,0)\oplus(0,1)$; the Clifford algebra itself is $\Lambda V$ as a representation, which is the classification of bilinears; and every spinorial representation sits in Dirac ⊗ tensor. It builds on [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)|§CB.11]]; the course's statements are shown as embeds where they become instances.

Notation as in §CB.11: $V = \mathbb R^{1,3}$, standard basis $e_\mu$, and a Dirac module $\gamma$ on $S = \mathbb C^4$ with $\gamma(e_\mu) = \gamma^\mu$.

## The Dirac module and its two halves

The Dirac maps, the Clifford module of the course, and $\gamma^5$, defined in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] and [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (shown in §CB.7); the module is irreducible of dimension $4 = 2^{4/2}$ ([[§CB.8 Complex Clifford Algebras and Clifford Modules#^thm-cb-8-7|Theorem §CB.8.7]]).

> [!theorem] Theorem §CB.12.1: γ⁵ Is the Complex Volume Element
> In the Dirac module, $\gamma(\omega_{\mathbb C}) = \gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ ([[§CB.8 Complex Clifford Algebras and Clifford Modules#^def-cb-8-4|Def. §CB.8.4]], [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]]); hence $(\gamma^5)^2 = \mathbb 1$, $\gamma^5$ anticommutes with every $\gamma^\mu$ and commutes with $\gamma(\mathrm{Cl}^0)$, in particular with every $S^{\mu\nu}$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-19|Theorem §CB.7.19]], 3).
>
> *Source (planned): Peskin & Schroeder, §3.4 · written here*

^thm-cb-12-1

> [!proof]- Proof (to be filled)
> *To be filled (Def. §CB.8.4 with $n = 4$, $s = 3$: $i^{6+3} = i$).*

^pf-cb-12-1

> [!theorem] Theorem §CB.12.2: The Dirac Module Restricted to SL(2,ℂ) Is (½, 0) ⊕ (0, ½)
> Restricted to $\mathrm{Spin}(1,3)_0 \cong SL(2, \mathbb C)$ ([[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)#^thm-cb-11-2|Theorem §CB.11.2]]), the Dirac module is $S = S^+\oplus S^-$, $S^\pm$ the $\pm1$ eigenspaces of $\gamma^5$ ([[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-12-1|Theorem §CB.12.1]]); $S^+$ and $S^-$ are irreducible, two-dimensional and inequivalent ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-20|Theorem §CB.9.20]], 1), one equivalent to $\lambda \mapsto \lambda$ and the other to $\lambda \mapsto (\lambda^\dagger)^{-1}$: they are $(\frac12, 0)$ and $(0, \frac12)$ ([[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)#^thm-cb-11-5|Theorem §CB.11.5]]), in the order fixed by [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]] and [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^cau-c3-3-1|§C3.3, Caution: Which one is (½, 0) depends on the sign of K]].
>
> *Source (planned): PHY 513 TA (oral remark, Oct 2026) · Peskin & Schroeder, §3.2 · written here*

^thm-cb-12-2

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-12-2

The course's two statements of this fact, proved in [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]] and [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]]:

![[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4]]

![[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2]]

> [!theorem] Theorem §CB.12.3: The Two Halves Are Complex Conjugates of Each Other
> As representations of $SL(2, \mathbb C)$, $S^- \cong \overline{S^+}$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-7|Def. §CB.4.7]]) and $S^\pm \cong (S^\pm)^\ast$ via $\varepsilon$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-16|Theorem §CB.4.16]]); more generally $\overline{(j_+, j_-)} \cong (j_-, j_+)$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-8|Theorem §CB.4.8]]).
>
> *Source (planned): the user's PHY 513 notes, Ch. 7 §7.4.6, Ch. 8 §8.2 · [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-9|Theorem §C3.3.9]]*

^thm-cb-12-3

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-12-3

## Clifford multiplication, vectors and two-forms

> [!theorem] Theorem §CB.12.4: Clifford Multiplication Exchanges the Halves Equivariantly
> The map $V\otimes S \to S$, $a\otimes\psi \mapsto \slashed a\psi$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-4|Def. §C5a.4.4]]), is an intertwiner of $SL(2, \mathbb C)$-representations ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-21|Theorem §CB.9.21]]) and maps $V\otimes S^\pm$ to $S^\mp$.
>
> *Source (planned): written here · [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-12|Theorem §C5a.4.12]]*

^thm-cb-12-4

> [!proof]- Proof (to be filled)
> *To be filled (Theorem §CB.9.21 for $\mathbb R^{1,3}$).*

^pf-cb-12-4

The course's statements, in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]:

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11]]

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-12]]

> [!theorem] Theorem §CB.12.5: The Complexified Vector Is S⁺ ⊗ S⁻
> The map $V_{\mathbb C} \to \operatorname{Hom}(S^+, S^-) \cong (S^+)^\ast\otimes S^- \cong S^+\otimes S^-$, $a \mapsto \slashed a|_{S^+}$ ([[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-12-4|Theorem §CB.12.4]], [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-9|Theorem §CB.4.9]], [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-15|Theorem §CB.4.15]]), is an equivalence of $SL(2, \mathbb C)$-representations: $V_{\mathbb C} \cong (\frac12, 0)\otimes(0, \frac12) = (\frac12, \frac12)$. In the chiral basis its matrix is $a_\mu\bar\sigma^\mu$ (or $a_\mu\sigma^\mu$, by the convention of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]]): $\sigma^\mu$ is an invariant tensor ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-10|Def. §CB.4.10]]) with one vector, one undotted and one dotted index.
>
> *Source (planned): the user's PHY 513 notes, Ch. 8 §8.2 · Peskin & Schroeder, §3.2 · written here*

^thm-cb-12-5

> [!proof]- Proof (to be filled)
> *To be filled (intertwiner by Theorem §CB.12.4; injective because $\slashed a\slashed a = q(a)$ and a nonzero complex $a$ with $\slashed a|_{S^+} = 0$ would give $\slashed a = 0$; dimensions $4 = 2\cdot2$).*

^pf-cb-12-5

The course's bispinor and the vector representation $(\frac12, \frac12)$, in [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] and [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra|§C3.3]]:

![[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-6]]

![[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-4]]

> [!theorem] Theorem §CB.12.6: Two-Forms Are (1, 0) ⊕ (0, 1)
> $\Lambda^2V_{\mathbb C} \cong \Lambda^2(S^+\otimes S^-) \cong (\operatorname{Sym}^2S^+\otimes\Lambda^2S^-)\oplus(\Lambda^2S^+\otimes\operatorname{Sym}^2S^-) \cong \operatorname{Sym}^2S^+\oplus\operatorname{Sym}^2S^- = (1, 0)\oplus(0, 1)$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-13|Theorem §CB.4.13]], 3; $\Lambda^2S^\pm$ trivial, [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-15|Theorem §CB.4.15]]). The two summands are the eigenspaces $\star = \pm i$ of duality ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]]), exchanged by complex conjugation; on the real two-forms this is the second case of [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-23|Theorem §CB.2.23]].
>
> *Source (planned): written here · [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-7|Theorem §C3.4.7]], [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]]*

^thm-cb-12-6

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-12-6

## The Clifford algebra as a representation, and the bilinears

> [!theorem] Theorem §CB.12.7: Cl(1,3) ≅ ΛV as a Representation; the Sixteen Bilinears
> 1. $\mathrm{Spin}(1,3)_0$ acts on $\mathrm{Cl}(1,3)$ by $a \mapsto xax^{-1}$; the vector-space isomorphism $\Lambda V \cong \mathrm{Cl}(1,3)$ of [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-17|Theorem §CB.7.17]] intertwines it with $\Lambda\rho$, so $\mathrm{Cl}(1,3)_{\mathbb C} \cong \Lambda^0\oplus\Lambda^1\oplus\Lambda^2\oplus\Lambda^3\oplus\Lambda^4$ of dimensions $1 + 4 + 6 + 4 + 1$.
> 2. $\operatorname{End}(S) \cong \mathrm{Cl}(1,3)_{\mathbb C}$ ([[§CB.8 Complex Clifford Algebras and Clifford Modules#^thm-cb-8-5|Theorem §CB.8.5]]) as representations, with $\operatorname{End}(S) \cong S\otimes S^\ast$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-9|Theorem §CB.4.9]]); through the Dirac form $S^\ast \cong \bar S$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-16|Theorem §CB.9.16]]), so $\bar\psi\Gamma\chi$ with $\Gamma$ in the $\Lambda^k$ piece transforms as a $k$-form: scalar, vector, tensor, axial vector, pseudoscalar ($\Lambda^3 \cong \Lambda^1$ and $\Lambda^4 \cong \Lambda^0$ through $\gamma^5$, up to orientation).
>
> *Source (planned): Peskin & Schroeder, §3.4 · the user's PHY 513 notes, Ch. 8 §8.9 · written here*

^thm-cb-12-7

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-12-7

The course's bilinears, in [[§C5a.6 The Dirac Conjugate and the Bilinears|§C5a.6]]; the invariance of the Dirac form, an instance of [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-16|Theorem §CB.9.16]]:

![[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1]]

![[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3]]

## The TA's theorem for the Lorentz group

> [!theorem] Theorem §CB.12.8: Every Tensorial (j₊, j₋) Lies in a Tensor Power of the Vector
> If $k + l \in \mathbb Z$, then $(k, l)$ is equivalent to a subrepresentation of $V_{\mathbb C}^{\otimes N}$ with $N = 2\max(k, l)$, $V_{\mathbb C} = (\frac12, \frac12)$ ([[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-12-5|Theorem §CB.12.5]]).
>
> *Source (planned): written here (Clebsch–Gordan on each copy, [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-7|Theorem §C3.3.7]], [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-6|Theorem §CB.6.6]])*

^thm-cb-12-8

> [!proof]- Proof (to be filled)
> *To be filled ($(\frac12, \frac12)^{\otimes N}$ contains every $(a, b)$ with $a, b \le N/2$ and $a \equiv b \equiv N/2 \bmod 1$; $k + l \in \mathbb Z$ means $k \equiv l \bmod 1$).*

^pf-cb-12-8

> [!theorem] Theorem §CB.12.9: The TA's Theorem for the Lorentz Group
> Every spinorial irreducible representation $(j_+, j_-)$ ($j_+ + j_- \in \frac12 + \mathbb Z$, [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)#^thm-cb-11-6|Theorem §CB.11.6]]) is equivalent to a subrepresentation of $S\otimes T$, $S = (\frac12, 0)\oplus(0, \frac12)$ the Dirac module and $T$ tensorial: $(j_+, j_-) \subset (\frac12, 0)\otimes(j_+ - \frac12, j_-)$ if $j_+ \ge \frac12$, and $(j_+, j_-) \subset (0, \frac12)\otimes(j_+, j_- - \frac12)$ otherwise; and $T$ lies in a tensor power of $V_{\mathbb C}$ ([[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-12-8|Theorem §CB.12.8]]). With complete reducibility ([[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)#^thm-cb-11-4|Theorem §CB.11.4]]) this proves part 3 of [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-20|Theorem §CB.9.20]] for $\mathbb R^{1,3}$.
>
> *Source: PHY 513 TA (oral remark, Oct 2026) · planned for the proof: [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-7|Theorem §C3.3.7]] · written here*

^thm-cb-12-9

> [!proof]- Proof (to be filled)
> *To be filled ($(\frac12, 0)\otimes(j_+ - \frac12, j_-) \cong (j_+, j_-)\oplus(j_+ - 1, j_-)$ by Theorem §C3.3.7 and Theorem §CB.6.6).*

^pf-cb-12-9

> [!remark]- ★ Remark: Majorana spinors as a real structure (forward pointer)
> $\mathrm{Cl}(1,3) \cong M_2(\mathbb H)$ has no real four-dimensional module ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^rem-cb-7-1|§CB.7, ★ Remark: The real classification]]), but the Dirac module carries a conjugate-linear map $\mathcal C$ commuting with $\mathrm{Spin}(1,3)_0$ and with $\mathcal C^2 = \mathbb 1$ (charge conjugation); its fixed vectors are the Majorana spinors, a real form of $S$ for the group, exchanging $S^+$ with $S^-$ ([[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-12-3|Theorem §CB.12.3]]). To be stated and proved with the Majorana field (QFT C9, planned); [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-6|§C5a.5, ★ Remark: The Majorana basis]].

^rem-cb-12-1

> [!remark]- Connections
> - This section is the TA's picture for the course's spinors in one place: the Dirac module is a Clifford module (C5a.1), restricted to the spin group it is $(\frac12, 0)\oplus(0, \frac12)$ (C5a.3), $\gamma^5$ is the volume element (C5a.5), and vectors and two-forms are bispinors (C3.3, C3.4).
> - Theorem §CB.12.9 is why higher-spin fermion fields (Rarita–Schwinger $\psi_\mu$, a spinor with a vector index) are built as spinor ⊗ tensor and then projected.
> - **Used in**: Theorems §CB.12.1–§CB.12.3 — [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]], [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-2|Def. §C5a.5.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]], [[§C9.4 Fermion Bilinears under Parity|§C9.4]]; Theorem §CB.12.4 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-12|Theorem §C5a.4.12]], [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]]; Theorem §CB.12.5 — [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-6|Theorem §C5a.5.6]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-4|Theorem §C3.3.4]]; Theorem §CB.12.6 — [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-7|Theorem §C3.4.7]], [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]]; Theorem §CB.12.7 — [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3|Theorem §C5a.6.3]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|Theorem §C5a.6.4]], [[§C5a.11 Gamma-Matrix Technology#^rem-c5a-11-3|§C5a.11, ★ Remark: The simplest Fierz identity]]; Theorem §CB.12.9 — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-6|Theorem §C3.3.6]], [[§C3.4 How Fields Transform under the Lorentz Group#^def-c3-4-2|Def. §C3.4.2]].
