---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.9
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.8 Hermitian Forms, Signature and Pseudo-Unitary Groups]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules]] →

*Sources: the user's PHY 513 notes, Ch. 7 §7.2 · Quantum Mechanics §B6.3, §C7.1 · Differentiable Manifolds (591) and Group Theory (493), for the descent lemma · P. Woit, Quantum Theory, Groups and Representations, §§8.1–8.2, 9.4, 9.6 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · B. C. Hall, Quantum Theory for Mathematicians, §17.6 · the rest written here.*

What are all finite-dimensional representations of SU(2) and SO(3), how are they built from spin ½, and how do they multiply? The course classifies the irreducible representations of the rotation algebra by highest weight and integrates them to SU(2) and SO(3) ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]]); Quantum Mechanics adds angular momenta ([[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]]). This section puts these in the language of §CB.3–§CB.7: $\mathfrak{sl}(2, \mathbb C)$ and weights, complete reducibility, spin $j$ as the symmetric power $\operatorname{Sym}^{2j}\mathbb C^2$, the Clebsch–Gordan series as a statement about tensor products, and the descent lemma that decides which representations of a covering group are representations of the quotient. The three-dimensional Clifford picture of the same objects is [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half|§CB.14]].

## 𝔰𝔩(2,ℂ) and weights

> [!definition] Definition §CB.9.1: The Standard Basis of 𝔰𝔩(2,ℂ)
> The **standard basis** of $\mathfrak{sl}(2, \mathbb C)$ is
>
> $$
> H = \begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix}, \quad E = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix}, \quad F = \begin{pmatrix} 0 & 0 \\ 1 & 0\end{pmatrix}, \qquad [H, E] = 2E, \quad [H, F] = -2F, \quad [E, F] = H .
> $$
>
> Under $\mathfrak{su}(2)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-5|Theorem §CB.3.5]]) and complex-linear extension of a representation ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-9|Theorem §CB.3.9]]): $H = 2J^3$, $E = J^+$, $F = J^-$ in the physicists' generators of the defining representation.
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §8.1.2 (the basis $S_3$, $S_\pm = S_1 \pm iS_2$ of $\mathfrak{sl}(2, \mathbb C)$, $[S_3, S_\pm] = \pm S_\pm$, $[S_+, S_-] = 2S_3$) · the names $H, E, F$ written here*

^def-cb-9-1

> [!definition] Definition §CB.9.2: Weight and Weight Space
> For a representation of $\mathfrak{sl}(2, \mathbb C)$ (equivalently of $\mathfrak{su}(2)$) on $W$, the **weight space** of weight $m \in \mathbb C$ is $W_m = \{w : J^3w = mw\}$, $J^3 = \frac12H$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-1|Def. §CB.9.1]]); $m$ is a **weight** if $W_m \ne 0$, and $\dim W_m$ is its **multiplicity**.
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §8.1.2 (Definition: weights and weight spaces; Woit labels by $k = 2m$, the eigenvalue of $\pi'(2S_3)$) · written here*

^def-cb-9-2

The course's classification, for the rotation algebra with generators $J^i$ and no inner product assumed (PHY 513 Lecture 7; the user's PHY 513 notes, Ch. 7 §7.2; two routes). It is the same statement as Theorem §CB.9.5 below, read through $\mathfrak{so}(3)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)$ with $H = 2J^3$, $E = J^+$, $F = J^-$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-1|Def. §CB.9.1]]): its $D^{(j)}$ are the $V_j$, its highest weight $j$ the top weight of $J^3$. Both proofs are kept.

> [!theorem] Theorem §CB.9.3: The Irreducible Representations of the Rotation Algebra (Highest Weight)
> Let $J^i$ be the generators of a finite-dimensional complex representation of $\mathfrak{so}(3)$, extended to $J^\pm = J^1 \pm iJ^2$; no inner product is assumed.
> 1. **Highest weight.** There is $v_0 \ne 0$ with $J^+v_0 = 0$, $J^3v_0 = jv_0$, and necessarily $2j \in \{0, 1, 2, \dots\}$; the vectors $(J^-)^kv_0$, $k = 0, \dots, 2j$, span an irreducible invariant subspace of dimension $2j + 1$.
> 2. **Classification.** For each $j \in \{0, \frac12, 1, \frac32, \dots\}$ there is exactly one irreducible representation of dimension $2j + 1$ up to equivalence, $D^{(j)}$, labelled by its **highest weight** $j$ (the **spin**); there are no others.
> 3. **Standard basis.** $D^{(j)}$ has a basis $|j, m\rangle$, $m = j, j-1, \dots, -j$, with
>
> $$
> J^3|j, m\rangle = m|j, m\rangle, \qquad J^\pm|j, m\rangle = \sqrt{(j \mp m)(j \pm m + 1)}\;|j, m \pm 1\rangle, \qquad \mathbf J^2 = j(j+1)\,\mathbb 1 ;
> $$
>
> the inner product making this basis orthonormal makes the $J^i$ Hermitian, and is the only such inner product up to a factor.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Derivations "Constructing every irreducible representation: ladder operators", "The representations of the rotation algebra"), eq. (ladder) · PHY 513 Lecture 7 ("Representations of angular momentum": spin $j$, $2j + 1$ states) · Yu §3.3.1, eqs. (3.118)–(3.146) · Hall, Thms. 17.4, 17.6, Props. 17.7–17.9 · Georgi §§3.1–3.3*

^thm-cb-9-3

> [!derivation]- Derivation
> **1. The relations of the complexified algebra.** From $[J^i, J^j] = i\varepsilon^{ijk}J^k$, expanding each bracket bilinearly:
>
> $$
> [J^3, J^\pm] = [J^3, J^1] \pm i[J^3, J^2] = iJ^2 \pm i(-iJ^1) = \pm(J^1 \pm iJ^2) = \pm J^\pm ,
> $$
>
> $$
> [J^+, J^-] = [J^1 + iJ^2, J^1 - iJ^2] = -i[J^1, J^2] + i[J^2, J^1] = -i(iJ^3) + i(-iJ^3) = 2J^3 .
> $$
>
> **2. An eigenvector, and raising.** $J^3$ is an operator on a finite-dimensional nonzero complex space, so it has an eigenvector $v$, $J^3v = \lambda v$ with $\lambda \in \mathbb C$ ([[§15 The Minimal Polynomial#^ladr-5-19|LADR Thm. 5.19]]). By step 1, $J^3J^+v = (J^+J^3 + J^+)v = (\lambda + 1)J^+v$: $J^+v$ is zero or an eigenvector with eigenvalue $\lambda + 1$.
>
> **3. The top of the chain.** Eigenvectors with distinct eigenvalues are independent, and $W$ is finite-dimensional, so $J^3$ has finitely many eigenvalues and the chain $v, J^+v, (J^+)^2v, \dots$ reaches zero: there is $k \ge 0$ with $v_0 \equiv (J^+)^kv \ne 0$, $J^+v_0 = 0$, $J^3v_0 = \mu v_0$, $\mu = \lambda + k$ (a priori complex).
>
> **4. Lowering.** Set $v_k = (J^-)^kv_0$. As in step 2 with the sign reversed, $J^3J^-u = (J^-J^3 - J^-)u$, so $J^3v_k = (\mu - k)v_k$.
>
> **5. Raising a lowered vector.** Claim: $J^+v_k = k(2\mu + 1 - k)\,v_{k-1}$ for $k \ge 1$. For $k = 1$: $J^+J^-v_0 = (J^-J^+ + [J^+, J^-])v_0 = 0 + 2J^3v_0 = 2\mu\,v_0$, which is $1\cdot(2\mu + 1 - 1)v_0$. If it holds for $k$, then
>
> $$
> J^+v_{k+1} = J^+J^-v_k = (J^-J^+ + 2J^3)v_k = k(2\mu + 1 - k)\,J^-v_{k-1} + 2(\mu - k)\,v_k = \bigl[2\mu k + k - k^2 + 2\mu - 2k\bigr]v_k = (k+1)(2\mu - k)\,v_k ,
> $$
>
> using $J^-v_{k-1} = v_k$; and $(k+1)(2\mu - k) = (k+1)(2\mu + 1 - (k+1))$ is the claim for $k + 1$.
>
> **6. Termination fixes $\mu$.** The nonzero $v_k$ have distinct eigenvalues $\mu - k$, so finitely many are nonzero: there is $N \ge 0$ with $v_N \ne 0$, $v_{N+1} = 0$. Step 5 with $k = N + 1$: $0 = J^+v_{N+1} = (N+1)(2\mu - N)\,v_N$. Since $N + 1 > 0$ and $v_N \ne 0$, $\mu = N/2 \equiv j$, and the chain has $N + 1 = 2j + 1$ members. ⚑ By-product: $j$ is a non-negative half-integer as a consequence of *finite dimension alone*; no positivity of norms is used, so the argument applies verbatim to non-unitary representations → [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], 1 (used for each copy of $\mathbf J_\pm$ in [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]).
>
> **7. Invariance and irreducibility.** $\operatorname{span}\{v_0, \dots, v_{2j}\}$ is mapped into itself by $J^3$ (step 4), $J^-$ (definition, $J^-v_{2j} = v_{2j+1} = 0$) and $J^+$ (step 5), hence by $J^1 = \frac12(J^+ + J^-)$ and $J^2 = \frac{1}{2i}(J^+ - J^-)$. If $w = \sum_ka_kv_k \ne 0$ lies in an invariant subspace, let $k_0$ be the largest index with $a_{k_0} \ne 0$; then $(J^+)^{k_0}w = a_{k_0}\prod_{k=1}^{k_0}k(2j + 1 - k)\,v_0$ (the terms with $k < k_0$ are annihilated, since $J^+v_0 = 0$), and every factor $k(2j + 1 - k)$ with $1 \le k \le 2j$ is positive. So $v_0$, and with it every $v_k = (J^-)^kv_0$, lies in the subspace: part 1.
>
> **8. Classification.** If the representation is irreducible, the span of step 7 is all of $W$, so $\dim W = 2j + 1$ and the action on the basis $\{v_k\}$ is fixed by $j$ (steps 4–5). Two irreducible representations of the same dimension therefore have the same $j$, and the map $v_k \mapsto v_k'$ intertwines them (Def. §CB.2.6). Existence for each $j$: define $J^3$, $J^\pm$ on a space with basis $v_0, \dots, v_{2j}$ by steps 4–5; $[J^3, J^\pm] = \pm J^\pm$ holds because $J^\pm$ shift the $J^3$ eigenvalue by $\pm1$, and $[J^+, J^-]v_k = (k+1)(2j - k)v_k - k(2j + 1 - k)v_k = 2(j - k)v_k = 2J^3v_k$. Part 2.
>
> **9. Normalization.** Put $|j, j - k\rangle = c_kv_k$ with $c_0 = 1$ and $c_{k+1} = c_k\big/\sqrt{(k+1)(2j - k)}$. With $m = j - k$, $(k+1)(2j - k) = (j + m)(j - m + 1)$, so $J^-|j, m\rangle = c_kv_{k+1} = \sqrt{(j + m)(j - m + 1)}\,|j, m - 1\rangle$, and by step 5 $J^+|j, m - 1\rangle = c_{k+1}(k+1)(2j - k)v_k = \sqrt{(j + m)(j - m + 1)}\,|j, m\rangle$; renaming $m - 1 \to m$ gives the $J^+$ formula of part 3. For the inner product declaring $\{|j, m\rangle\}$ orthonormal, $J^3$ is real diagonal and the matrices of $J^+$ and $J^-$ are real and transposes of each other, so $J^3$ is Hermitian and $(J^+)^\dagger = J^-$, whence $J^1, J^2$ are Hermitian. Uniqueness up to a factor: Hermitian $J^3$ forces the eigenvectors $v_k$ to be orthogonal, and $(J^+)^\dagger = J^-$ forces $\|v_{k+1}\|^2 = \langle v_k, J^+J^-v_k\rangle = (k+1)(2j - k)\|v_k\|^2$ (Hall Prop. 17.7), so only $\|v_0\|$ is free.
>
> **10. The Casimir.** $\mathbf J^2 = J^-J^+ + (J^3)^2 + J^3$ (expand $J^-J^+ = (J^1)^2 + (J^2)^2 + i[J^1, J^2] = (J^1)^2 + (J^2)^2 - J^3$). On $v_0$: $\mathbf J^2v_0 = (0 + j^2 + j)v_0$. $\mathbf J^2$ is a Casimir, so on the irreducible $D^{(j)}$ it equals $j(j+1)\mathbb 1$ ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-13|Theorem §CB.6.13]]).
>
> **What the derivation shows**
> - Assumptions actually used: complex scalars (an eigenvector exists) and finite dimension (chains terminate). Hermiticity is a *consequence* (step 9), not an input.
> - The label of an irreducible representation is its highest $J^3$ eigenvalue, equivalently its dimension, equivalently its Casimir value; the three agree only for irreducible representations ([[§C3.1 Index Slots, Rotations and Spin in Field Theory#^rem-c3-1-4|Remark: "One representation for each dimension"]]).
> - The algebra produces half-integer $j$ on the same footing as integer $j$; which of them belong to $SO(3)$ is decided by the group → [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]].
> - Used next: $(j_+, j_-)$ for the Lorentz algebra ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]); spin of a massive particle as a representation of its little group ([[§C3.6★ Particle States and the Little Group#^thm-c3-6-8|Theorem §C3.6.8]]).

^der-cb-9-3

*Uses:* [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-3|Def. §CB.3.3]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-7|Def. §CB.3.7]], [[§15 The Minimal Polynomial#^ladr-5-19|LADR Thm. 5.19]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-7|Def. §CB.2.7]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-13|Theorem §CB.6.13]]

> [!derivation]- Derivation (second route: positivity of norms, as in Quantum Mechanics)
> *Source: [[§B5.2 Orbital Angular Momentum and Spherical Harmonics#^der-b5-2-4|QM Derivation §B5.2.4]], [[§B5.2 Orbital Angular Momentum and Spherical Harmonics#^der-b5-2-5|QM Derivation §B5.2.5]]; Sakurai's version [[§C5.3 The Angular-Momentum Spectrum and Rotation Matrices#^rem-c5-3-1|QM Remark: Eigenvalues and ladder matrix elements]]; Yu (3.118)–(3.141); the user's 513 notes, Steps 1–5*
>
> Quantum Mechanics finds the same spectrum for Hermitian $J^i$ on a space with a positive inner product. The steps correspond as follows, with the differences marked.
>
> **1.** Common eigenvectors $|\eta, m\rangle$ of $\mathbf J^2$ and $J^3$, with $\eta, m$ real — *needs* Hermiticity (here: step 2 takes one eigenvector of $J^3$ alone, eigenvalue complex a priori).
>
> **2.** $m$ is bounded because $\eta - m^2 = \|J^1|\eta, m\rangle\|^2 + \|J^2|\eta, m\rangle\|^2 \ge 0$ — *needs* positivity (here: finite dimension bounds the chain, step 3).
>
> **3.** $J^-J^+|m_{\max}\rangle = 0$ and $J^+J^-|m_{\min}\rangle = 0$ give $\eta = m_{\max}(m_{\max} + 1) = m_{\min}(m_{\min} - 1)$, so $m_{\min} = -m_{\max}$ (the other root $m_{\min} = m_{\max} + 1$ is excluded) — the same information as step 6 here, obtained from both ends of the chain instead of from the bottom.
>
> **4.** $|c^\pm_m|^2 = (j \mp m)(j \pm m + 1)$ from $(J^\pm)^\dagger = J^\mp$; the phases are a choice (Condon–Shortley: positive) — here step 9, where the same numbers arise as normalization constants.
>
> **What the derivation shows**
> - Both routes give the same spectrum and the same ladder coefficients; this one buys the bound on $m$ with positivity of norms, the main one with finite dimension.
> - For a compact group the hypotheses of this route are always available (Theorem §CB.6.16); for the finite-dimensional representations of the Lorentz group they are available only after the fact: $\mathbf J_\pm$ are Hermitian with respect to an auxiliary inner product that is not invariant under boosts ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-5|Theorem §CB.16.5]]), and constructing it needs the detour through the compact $SU(2)\times SU(2)$. That is why the main derivation avoids them.

> [!caution] Caution: Phase conventions for the ladder operators
> The coefficients $\sqrt{(j \mp m)(j \pm m + 1)}$ are positive in the Condon–Shortley convention used here, in Quantum Mechanics and in the user's 513 notes. Yu chooses $J^+|j, \sigma\rangle = -\sqrt{(j - \sigma)(j + \sigma + 1)}\,|j, \sigma + 1\rangle$ for $\sigma \ge 0$ and $+$ for $\sigma < 0$ (Yu (3.142)–(3.143)), and the user's pre-course notes follow him. The two bases differ by signs $|j, \sigma\rangle \to \pm|j, \sigma\rangle$, a diagonal change of basis: the representations are equivalent and $j$, the dimension and the Casimir agree, but individual matrix elements (Yu's $\tau^1_{(1)}$, the Clebsch–Gordan coefficients built on it) differ in sign. For $j = \frac12$ the two coincide.
>
> *Source: Yu §3.3.1, eqs. (3.141)–(3.150) · the user's pre-course notes, §2.3 (Note on the phase convention) · the user's PHY 513 notes, Ch. 7 §7.2 (Step 5)*

^cau-cb-9-1

The value of the Casimir operator of [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-15|Theorem §CB.6.15]] on spin $j$ (the $\mathfrak{su}(2)$ example stated there; moved here in the CB ordering pass because it needs part 3 of the theorem above):

> [!theorem] Theorem §CB.9.4: The 𝔰𝔲(2) Casimir on Spin j
> For $\mathfrak{su}(2)$ with the invariant form $B(X, Y) = -2\operatorname{tr}(XY)$ on $2\times2$ matrices, the Casimir operator of [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-15|Theorem §CB.6.15]] is $C_d = -\mathbf J^2$, so $C_d = -j(j+1)\mathbb 1$ on spin $j$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]]).
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), §18.3 · normalization computed in Theorem §CB.6.15, Step 5, and checked against Theorem §CB.9.3 (batch 2) · moved from the Examples of Theorem §CB.6.15 (CB ordering pass, 2026-10-08)*

^thm-cb-9-4

> [!proof]- Proof
> Step 5 of the proof of [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-15|Theorem §CB.6.15]] gives $C_d = \sum_a(-iJ^a)^2 = -\mathbf J^2$, which is $-j(j+1)\mathbb 1$ on spin $j$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], 3).

^pf-cb-9-4

*Uses:* [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-15|Theorem §CB.6.15]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]]

> [!theorem] Theorem §CB.9.5: Finite-Dimensional Representations of 𝔰𝔩(2,ℂ)
> Let $W$ be a finite-dimensional complex-linear representation of $\mathfrak{sl}(2, \mathbb C)$. Then:
> 1. $W$ is completely reducible ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-21|Theorem §CB.6.21]]) and $J^3$ is diagonalizable: $W = \bigoplus_mW_m$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-2|Def. §CB.9.2]]);
> 2. every weight lies in $\frac12\mathbb Z$, and $J^\pm W_m \subset W_{m\pm1}$;
> 3. the irreducible ones are the $V_j$ of the course's classification ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]]), with weights $j, j-1, \dots, -j$, each of multiplicity one.
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §8.1.1 (weights and weight spaces) and §8.1.2 (raising and lowering operators: $[S_3, S_+] = S_+$ gives $V_k \to V_{k+2}$ in his normalization; the highest weight theorem) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the classification and its proof: [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]] (from the user's PHY 513 notes, Ch. 7 §7.2) · complete reducibility: [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-21|Theorem §CB.6.21]]*

^thm-cb-9-5

> [!proof]- Proof
> *Woit's route (§8.1): decompose, read off the weights from the irreducible pieces, and shift them with the ladder operators. Woit obtains the weight decomposition from the circle subgroup of the group; here it comes from complete reducibility of the algebra.*
>
> **1. From $\mathfrak{sl}(2, \mathbb C)$ to $\mathfrak{su}(2)$.** $\mathfrak{su}(2)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-5|Theorem §CB.3.5]]), so restricting the complex-linear representation to $\mathfrak{su}(2)$ gives a representation $d$ of $\mathfrak{su}(2)$ with $d_{\mathbb C}$ the original one and the same invariant subspaces and intertwiners ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-9|Theorem §CB.3.9]]). Via $\mathfrak{su}(2) \cong \mathfrak{so}(3)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-21|Theorem §CB.1.21]]) its physicists' generators $J^i$ obey $[J^i, J^j] = i\varepsilon^{ijk}J^k$, and $J^3 = \frac12H$, $J^\pm = J^1 \pm iJ^2$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-1|Def. §CB.9.1]]).
>
> **2. Complete reducibility.** By Weyl's unitary trick with $K = SU(2)$ ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-21|Theorem §CB.6.21]]), $W = W^{(1)}\oplus\cdots\oplus W^{(r)}$ with each $W^{(k)}$ invariant and irreducible.
>
> **3. Each piece is some $V_j$.** An irreducible finite-dimensional representation of the rotation algebra is equivalent to $D^{(j)} = V_j$ for one $j \in \{0, \frac12, 1, \dots\}$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], 2), and $V_j$ has the basis $|j, m\rangle$, $m = j, j-1, \dots, -j$, with $J^3|j, m\rangle = m|j, m\rangle$ (Theorem §CB.9.3, 3; no inner product is used in that derivation). Transport these bases into the $W^{(k)}$ by the equivalences.
>
> **4. Part 1.** The union of the bases of step 3 is a basis of $W$ ([[§6 Dimension#^ladr-2-43|LADR Thm. 2.43]] and the direct sum) consisting of eigenvectors of $J^3$, so $J^3$ is diagonalizable and $W = \bigoplus_mW_m$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-2|Def. §CB.9.2]]), $W_m$ spanned by the basis vectors with eigenvalue $m$.
>
> **5. Part 2, weights.** Every eigenvalue in step 4 is some $m$ with $j - m \in \{0, 1, \dots, 2j\}$ and $2j \in \mathbb Z$, so $2m \in \mathbb Z$: $m \in \frac12\mathbb Z$.
>
> **6. Part 2, ladder (Woit §8.1.2).** $[J^3, J^\pm] = \pm J^\pm$ (expand $[J^3, J^1 \pm iJ^2] = iJ^2 \pm i(-iJ^1) = \pm(J^1 \pm iJ^2)$). For $w \in W_m$: $J^3J^\pm w = J^\pm J^3w \pm J^\pm w = (m \pm 1)J^\pm w$, so $J^\pm w \in W_{m\pm1}$ (possibly $0$).
>
> **7. Part 3.** If $W$ is irreducible, $r = 1$ in step 2 and $W \cong V_j$; by step 3 its weights are $j, j-1, \dots, -j$, each once.
>
> **What the proof shows**
> - Half-integrality of the weights and the shift by one are algebraic consequences of the commutation relations and finite dimension; diagonalizability of $J^3$ is not, it needs complete reducibility (in the non-semisimple world a $2\times2$ Jordan block would be allowed).
> - ⚑ By-product: complete reducibility of $\mathfrak{sl}(2, \mathbb C)$-representations is borrowed from the compact group $SU(2)$ (Weyl's trick); the same mechanism gives it for the Lorentz algebra, two copies of $\mathfrak{sl}(2, \mathbb C)$ → [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-5|Theorem §CB.16.5]].
> - Used next: Theorem §CB.9.6 counts the pieces by their weights.

^pf-cb-9-5

*Uses:* [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-5|Theorem §CB.3.5]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-9|Theorem §CB.3.9]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-21|Theorem §CB.1.21]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-21|Theorem §CB.6.21]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-1|Def. §CB.9.1]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-2|Def. §CB.9.2]], [[§6 Dimension#^ladr-2-43|LADR Thm. 2.43]]

> [!theorem] Theorem §CB.9.6: Weight Multiplicities Determine a Representation
> Two finite-dimensional representations of $\mathfrak{sl}(2, \mathbb C)$ are equivalent iff their weight multiplicities agree. With $n_m = \dim W_m$, the number of summands $V_j$ in $W$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-5|Theorem §CB.9.5]]) is $n_j - n_{j+1}$.
>
> *Source: the counting argument of [[§B6.3 Addition of Angular Momenta#^der-b6-3-2|QM Derivation §B6.3.2]], step 2 ($n(m) = \sum_{j \ge |m|}N_j$, hence $N_j = n(j) - n(j+1)$; from the user's series, Part IV, §15, and Greensite §14.1), run on the decomposition of Theorem §CB.9.5 instead of on Hermitian multiplets · P. Woit, Quantum Theory, Groups and Representations, §8.1 (representations are determined by their weights restricted to the circle subgroup), §9.4.1 (the same bookkeeping by highest weights)*

^thm-cb-9-6

> [!proof]- Proof
> *QM's "staircase" count (Derivation §B6.3.2, step 2), with the multiplets supplied by complete reducibility (Theorem §CB.9.5) instead of by Hermitian operators.*
>
> **1. Equivalent representations have the same multiplicities.** Let $S : W \to W'$ be an invertible intertwiner ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-2|Def. §CB.6.2]]). It commutes with $J^3$, so for $w \in W_m$, $J^3Sw = SJ^3w = mSw$: $S(W_m) \subset W'_m$, and likewise $S^{-1}(W'_m) \subset W_m$. So $S$ maps $W_m$ onto $W'_m$ and $\dim W_m = \dim W'_m$.
>
> **2. Multiplicities of a sum.** By Theorem §CB.9.5, $W \cong \bigoplus_ka_kV_k$ ($a_k$ copies of $V_k$, $k \in \frac12\mathbb Z_{\ge0}$), and $V_k$ has the weight $m$ exactly once if $|m| \le k$ and $k - m \in \mathbb Z$, and not otherwise (Theorem §CB.9.5, 3). Weight spaces of a direct sum are the sums of the weight spaces of the summands, so
>
> $$
> n_m = \sum_{k \ge |m|,\ k - m \in \mathbb Z}a_k .
> $$
>
> **3. The staircase.** For $j \ge 0$, the sums for $n_j$ and $n_{j+1}$ run over the same integrality class ($k - j \in \mathbb Z$ iff $k - (j+1) \in \mathbb Z$), over $k \ge j$ and $k \ge j + 1$ respectively. All terms with $k \ge j + 1$ cancel:
>
> $$
> n_j - n_{j+1} = a_j .
> $$
>
> In particular the numbers $a_j$ do not depend on the chosen decomposition.
>
> **4. Equal multiplicities give equivalent representations.** If $W$ and $W'$ have the same $n_m$ for all $m$, step 3 gives $a_j = a'_j$ for all $j$; choose equivalences $V_j \to V_j$ copy by copy and add them up: an invertible intertwiner $W \cong \bigoplus a_jV_j = \bigoplus a'_jV_j \cong W'$. With step 1, the equivalence holds iff the multiplicities agree.
>
> **What the proof shows**
> - The weight multiplicities are a complete invariant of finite-dimensional $\mathfrak{sl}(2, \mathbb C)$-representations, the analogue for this algebra of characters for finite groups (Woit §9.4.2 phrases it with characters $\operatorname{tr}e^{i\theta\cdot2J^3}$).
> - ⚑ By-product: the number of copies of each $V_j$ is independent of the decomposition chosen (step 3), so "the multiplicity of spin $j$ in $W$" is well defined.
> - Step 3 is [[§B6.3 Addition of Angular Momenta#^der-b6-3-2|QM Derivation §B6.3.2]], step 2, with $N_j = a_j$ (comparison moved here from step 3, CB ordering pass).
> - Used next: the Clebsch–Gordan series (Theorem §CB.9.14) and $\operatorname{Sym}^{2j}\mathbb C^2$ (Theorem §CB.9.12, second route).

^pf-cb-9-6

*Uses:* [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-5|Theorem §CB.9.5]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-2|Def. §CB.6.2]]

## The topology of SU(2) and SO(3), and two-valued representations

Projective and two-valued representations, as the course defines them (Yu §3.3.1; the user's PHY 513 notes, Ch. 7 §7.2). Half-integer spin below is the first example; their general theory, with Wigner's theorem and the lifting to covering groups, is [[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries|§CB.18]]:

> [!definition] Definition §CB.9.7: Projective Representation
> A **projective representation** of a group $G$ on a Hilbert space $\mathcal H$ is an assignment of unitary operators $U(g)$, $U(\mathbb 1) = \mathbb 1$, obeying the group law up to phases,
>
> $$
> U(g_2)\,U(g_1) = e^{i\varphi(g_2, g_1)}\,U(g_2g_1), \qquad \varphi \text{ real};
> $$
>
> equivalently, a homomorphism into $PU(\mathcal H) = U(\mathcal H)/\{e^{i\alpha}\mathbb 1\}$, i.e. an action on rays. $U'(g) = e^{i\alpha(g)}U(g)$ defines the same projective representation; it is **genuine** if the phases can be chosen so that $\varphi \equiv 0$. A **two-valued** representation is one with $e^{i\varphi} = \pm1$.
>
> *Source: Yu §3.3.1, eqs. (3.110)–(3.113) · the user's PHY 513 notes, Ch. 7 §7.2 (Derivation "Why the sign appears", last paragraph) · the user's pre-course notes, §2.3 ("Projective representations") · Hall, Defs. 16.43, 16.45, 16.55*

^def-cb-9-7

The topology behind the integration and descent theorems of this section, with the course's ball pictures, and the same pattern for the Lorentz group (the user's PHY 513 notes, Ch. 7 §7.2):

> [!theorem] Theorem §CB.9.8: SU(2) Is Simply Connected, SO(3) Is Doubly Connected
> 1. $SU(2)$ is homeomorphic to the 3-sphere $S^3$, hence simply connected.
> 2. $SO(3)$ is homeomorphic to $\mathbb{RP}^3 = S^3/(x \sim -x)$, and $\pi_1(SO(3)) \cong \mathbb Z_2$: a loop at $\mathbb 1$ is contractible iff its lift to $SU(2)$ starting at $\mathbb 1$ ends at $\mathbb 1$.
> 3. The loop of rotations $\theta \mapsto R(\hat n, \theta)$, $0 \le \theta \le 2\pi$, is not contractible; traversed twice ($0 \le \theta \le 4\pi$) it is.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Derivation "Why the sign appears: the topology of SO(3) and SU(2)"; Remark "SO(3) ≅ ℝP³") · Yu §3.2, Figs. 3.3–3.5 · the user's pre-course notes, §2.2 (Remark "Covering-space formulation") · Hall, Ex. 16.34*

^thm-cb-9-8

> [!derivation]- Derivation
> **1. $SU(2) \cong S^3$.** The map $U(a, b) \mapsto (x_0, x_1, x_2, x_3)$ of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-19|Theorem §CB.1.19]], 1, is a bijection onto $S^3$, continuous in both directions (the coordinates are matrix entries). $S^3$ is simply connected ([[§37 The Fundamental Group of Sⁿ#^thm-37-3|590 Thm. §37.3]]; [[§29 The Fundamental Group#^def-29-3|590 Def. §29.3]]).
>
> **2. $SO(3) \cong \mathbb{RP}^3$.** The covering map $R$ is onto and $R(U) = R(U')$ iff $U' = \pm U$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-20|Theorem §CB.1.20]]); in the coordinates of step 1, $U \mapsto -U$ is $x \mapsto -x$. So $R$ induces a continuous bijection from $S^3/(x \sim -x) = P^3$ ([[§38 Fundamental Group of Some Surfaces#^def-38-2|590 Def. §38.2]]) onto $SO(3)$; $P^3$ is compact and $SO(3)$ Hausdorff, so it is a homeomorphism ([[Bijection from Compact to Hausdorff is a Homeomorphism|590, Bijection from compact to Hausdorff]]). $\pi_1(P^n) \cong \mathbb Z/2\mathbb Z$ for $n \ge 2$ ([[§38 Fundamental Group of Some Surfaces#^thm-38-3|590 Thm. §38.3]]).
>
> **3. The lifting criterion.** The quotient map $S^3 \to P^3$ is a covering map with fibre $\{\pm x\}$ (as [[§38 Fundamental Group of Some Surfaces#^thm-38-1|590 Thm. §38.1]] for $n = 2$), and $S^3$ is simply connected, so the lifting correspondence $\pi_1(SO(3), \mathbb 1) \to R^{-1}(\mathbb 1) = \{\mathbb 1, -\mathbb 1\}$, which sends a loop to the endpoint of its lift starting at $\mathbb 1$, is a bijection ([[§32 Lifting and the Fundamental Group of the Circle#^thm-32-4|590 Thm. §32.4]], 2). A loop is contractible iff it is the identity class iff its lift ends at $\mathbb 1$.
>
> **4. The $2\pi$ loop.** $R(e^{-i\theta\hat n\cdot\boldsymbol\sigma/2}) = R(\hat n, \theta)$ (Theorem §CB.1.20, 2), so the lift of $\theta \mapsto R(\hat n, \theta)$ starting at $\mathbb 1$ is $\theta \mapsto e^{-i\theta\hat n\cdot\boldsymbol\sigma/2} = \cos\frac\theta2\,\mathbb 1 - i\sin\frac\theta2\,\hat n\cdot\boldsymbol\sigma$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-19|Theorem §CB.1.19]]), which ends at $\cos\pi\,\mathbb 1 = -\mathbb 1$ for $\theta = 2\pi$: not contractible. For $0 \le \theta \le 4\pi$ the lift ends at $\cos2\pi\,\mathbb 1 = \mathbb 1$: contractible. Since $\pi_1$ has two elements, every non-contractible loop is homotopic to the $2\pi$ loop.
>
> **What the derivation shows**
> - "Doubly connected" (Yu: 连通度为 2) means $|\pi_1| = 2$; "covering group" means the simply connected (universal) cover, with the lifted group structure.
> - The sign of [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]], 2, is the endpoint of the lift: a representation of $SU(2)$ assigns $\pm\mathbb 1$ to the two classes of loops in $SO(3)$, and $D(-\mathbb 1) = (-1)^{2j}$ says which assignment.
> - Used next: why projective representations of $SO(3)$ carry exactly a sign ([[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^thm-cb-18-7|Theorem §CB.18.7]]); the same topology for $SO^+(1,3)$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^rem-cb-9-2|Remark: The same pattern for the Lorentz group]]).

^der-cb-9-8

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-19|Theorem §CB.1.19]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-20|Theorem §CB.1.20]], [[§37 The Fundamental Group of Sⁿ#^thm-37-3|590 Thm. §37.3]], [[§38 Fundamental Group of Some Surfaces#^thm-38-3|590 Thm. §38.3]], [[§32 Lifting and the Fundamental Group of the Circle#^thm-32-4|590 Thm. §32.4]], [[Bijection from Compact to Hausdorff is a Homeomorphism|590, Bijection from compact to Hausdorff]]

> [!remark] Remark: The ball pictures
> ![[ph-qft-c3-1-1.svg]]
> *The group spaces as balls, adapted from the user's 513 notes and Yu Figs. 3.3–3.5. (a) A rotation by $\theta \in [0, \pi]$ about $\hat n$ is the point $\theta\hat n$ of a ball of radius $\pi$; a loop inside it shrinks to $\mathbb 1$. (b) A rotation by $\pi$ about $\hat n$ equals the one about $-\hat n$, so antipodal boundary points are one element; the rotations about $z$ from $0$ to $2\pi$ leave through $P$ and re-enter at $-P$. Under deformation the two boundary points move only as an antipodal pair and can never meet, so the loop cannot be shrunk. (c) $SU(2)$ is a ball of radius $2\pi$ whose whole boundary sphere is the single element $-\mathbb 1$; the same rotations lift to a path from $\mathbb 1$ to $-\mathbb 1$, which closes only at $4\pi$, and that doubled loop shrinks (Yu Fig. 3.8 shows the deformation).*
>
> The ball with antipodal boundary points glued is the upper hemisphere of $S^3$ with antipodal equator points glued, the same space as $\mathbb{RP}^3$; the picture argument "jump points move in pairs" is the lifting argument of Derivation §CB.9.8, step 3, drawn instead of stated ([[Real and complex projective spaces]], [[Spheres Sⁿ]]).
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Figure "so3su2"; Remark "SO(3) ≅ ℝP³", citing Lee, Ex. 21.14) · Yu §3.2, Figs. 3.3–3.5; §3.3.1, Fig. 3.8 · the user's pre-course notes, §2.2*

^rem-cb-9-1

> [!remark] Remark: The same pattern for the Lorentz group
> Every proper orthochronous Lorentz transformation is a boost times a rotation ([[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-6|REL Theorem §B1.2.6]]), and the boosts form a contractible $\mathbb R^3$ (rapidity vectors). So the non-contractible loops of $SO^+(1,3)$ are those of its rotation subgroup: $SO^+(1,3)$ is doubly connected, its simply connected cover is $SL(2, \mathbb C)$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]]), and the half-integer representations $(j_+, j_-)$ with $2(j_+ + j_-)$ odd are two-valued representations of $SO^+(1,3)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]]); Dirac spinors are the first example. What does *not* carry over is unitarity: the cover is not compact, and its finite-dimensional representations are not unitary ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-14|Theorem §CB.16.14]]), so the unitary representations on states must be infinite-dimensional ([[§C3.6★ Particle States and the Little Group|§C3.6★]]).
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (end of Derivation "Why the sign appears")*

^rem-cb-9-2

The same polar decomposition for $SL(2, \mathbb C)$, which the Lorentz sections use (first stated in [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover|§CB.15]]; moved here in the CB ordering pass because the Clebsch–Gordan series below uses its connectedness):

> [!theorem] Theorem §CB.9.9: SL(2, C) Is Connected and Simply Connected
> Every $\lambda \in SL(2, \mathbb C)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-2|Def. §CB.1.2]]) is uniquely $\lambda = e^{h}U$ with $U \in SU(2)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]) and $h$ traceless Hermitian, $h = -\frac12\boldsymbol\eta\cdot\boldsymbol\sigma$ for a unique $\boldsymbol\eta \in \mathbb R^3$, and $\lambda \mapsto (\boldsymbol\eta, U)$ is a homeomorphism $SL(2, \mathbb C) \cong \mathbb R^3\times S^3$. Hence $SL(2, \mathbb C)$ is path-connected and simply connected ([[§29 The Fundamental Group#^def-29-3|590 Def. §29.3]]).
>
> *Source: Yu Exercise 3.7(d), eq. (3.265) · the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit", part (d)) · the continuity of the decomposition quoted from the functional calculus*

^thm-cb-9-9

> [!derivation]- Derivation
> **1. The positive part.** $\lambda\lambda^\dagger$ is Hermitian and positive definite: $v^\dagger\lambda\lambda^\dagger v = |\lambda^\dagger v|^2 > 0$ for $v \ne 0$, since $\lambda$ is invertible. By the spectral theorem it is $W\operatorname{diag}(p_1, p_2)W^\dagger$ with $W$ unitary and $p_k > 0$. Set $h = \frac12W\operatorname{diag}(\ln p_1, \ln p_2)W^\dagger$, Hermitian, so that $e^{2h} = \lambda\lambda^\dagger$ ($e^{WDW^\dagger} = We^DW^\dagger$ term by term). It is the unique Hermitian $h$ with $e^{2h} = \lambda\lambda^\dagger$: $e^{2h}$ and $h$ have the same eigenvectors, and $\ln$ is injective on $(0, \infty)$; equivalently $e^h$ is the unique positive square root of $\lambda\lambda^\dagger$ ([[§25 Positive Operators#^ladr-7-39|LADR 7.39]]).
>
> **2. The unitary part.** Put $U = e^{-h}\lambda$. Then $UU^\dagger = e^{-h}\lambda\lambda^\dagger e^{-h} = e^{-h}e^{2h}e^{-h} = \mathbb 1$, so $U$ is unitary and $\lambda = e^hU$: the polar decomposition ([[§28 Consequences of Singular Value Decomposition#^ladr-7-93|LADR 7.93]], here with the positive factor on the left).
>
> **3. Determinants.** $1 = \det\lambda = \det e^h\det U = e^{\operatorname{tr}h}\det U$. Here $e^{\operatorname{tr}h} > 0$ ($h$ Hermitian has real trace) and $|\det U| = 1$; a positive number times a unit-modulus number equals $1$ only if the positive number is $1$ and the phase is $1$. So $\operatorname{tr}h = 0$ and $\det U = 1$: $U \in SU(2)$, and $h$ is traceless Hermitian, $h = \mathbf a\cdot\boldsymbol\sigma$ with $\mathbf a$ real ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], part 4); write $\mathbf a = -\frac12\boldsymbol\eta$.
>
> **4. Uniqueness.** If $\lambda = e^{h'}U'$ is another such decomposition, then $\lambda\lambda^\dagger = e^{h'}U'U'^\dagger e^{h'} = e^{2h'}$, so $h' = h$ by step 1, and $U' = e^{-h}\lambda = U$.
>
> **5. Homeomorphism.** The map $(\boldsymbol\eta, U) \mapsto e^{-\boldsymbol\eta\cdot\boldsymbol\sigma/2}U$ is continuous (products and the exponential series), and by steps 1–4 it is a bijection $\mathbb R^3\times SU(2) \to SL(2, \mathbb C)$. Its inverse $\lambda \mapsto h = \frac12\ln(\lambda\lambda^\dagger)$, $U = e^{-h}\lambda$ is continuous because the logarithm of positive definite matrices is continuous (functional calculus; quoted). $SU(2)$ is homeomorphic to $S^3$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-19|Theorem §CB.1.19]]; [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^der-cb-9-8|Derivation §CB.9.8]], step 1).
>
> **6. Topology.** $\mathbb R^3$ is convex, so path-connected with every loop contractible (straight-line homotopy); $S^3$ is path-connected and simply connected ([[§37 The Fundamental Group of Sⁿ#^thm-37-3|590 Thm. §37.3]]). A product of path-connected spaces is path-connected, and $\pi_1(\mathbb R^3\times S^3) \cong \pi_1(\mathbb R^3)\times\pi_1(S^3) = 1$ ([[§29 The Fundamental Group#^thm-29-7|590 Thm. §29.7]]).
>
> **What the derivation shows**
> - $SL(2, \mathbb C)$ is "rotations times boosts": $U$ will map to a rotation and $e^h$ to a pure boost, the $2\times2$ counterpart of $\Lambda = B(u)R$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]]).
> - The noncompact factor $\mathbb R^3$ is topologically trivial; all the topology sits in the compact factor, and for $SL(2, \mathbb C)$ that factor is the simply connected $S^3$.
> - One input was quoted: the continuity of the matrix logarithm on positive matrices.
> - Used next: connectedness puts the image of the covering map in $SO^+(1,3)$ (Theorem §CB.15.4); simple connectivity makes it the universal cover (Theorem §CB.15.9).

^der-cb-9-9

*Uses:* [[§25 Positive Operators#^ladr-7-39|LADR 7.39]], [[§28 Consequences of Singular Value Decomposition#^ladr-7-93|LADR 7.93]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-19|Theorem §CB.1.19]], [[§37 The Fundamental Group of Sⁿ#^thm-37-3|590 Thm. §37.3]], [[§29 The Fundamental Group#^thm-29-7|590 Thm. §29.7]]; quoted: continuity of the logarithm of positive matrices

## Spin j as a symmetric power

The course realizes spin $j$ on polynomials of degree $2j$, and integrates to SU(2) and SO(3) (the user's PHY 513 notes, Ch. 7 §7.2):

> [!theorem] Theorem §CB.9.10: Integer and Half-Integer Spin: Integration to SU(2) and SO(3)
> 1. For each $j$, $D^{(j)}$ is the algebra representation of a unique representation of $SU(2)$, realized on the homogeneous polynomials of degree $2j$ in $z = (z_1, z_2)$ by $(D(U)P)(z) = P(U^{\mathsf T}z)$; and $D^{(j)}(-\mathbb 1) = (-1)^{2j}\,\mathbb 1$.
> 2. $D^{(j)}$ comes from a representation of $SO(3)$ if and only if $j$ is an integer. For half-integer $j$, $D^{(j)}(U)$ depends on $U$ and not only on the rotation $R(U)$: the rotation by $2\pi$ is represented by $-\mathbb 1$, a **two-valued representation** of $SO(3)$.
> 3. Every finite-dimensional representation of $SU(2)$ is equivalent to a direct sum of $D^{(j)}$'s; every one of $SO(3)$, to such a sum with integer $j$ only.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Derivation "The representations of the rotation algebra", "Half-integer spin and the group") · Yu §3.2 (below Fig. 3.5: covering group, $n$-valued representations) · the user's pre-course notes, §2.3 ("Spin": $D^{(1/2)}[R_z(2\pi)] = -\mathbb 1$) · Hall, Thm. 16.30, Ex. 16.34, Prop. 17.10*

^thm-cb-9-10

> [!derivation]- Derivation
> **1. The space.** $V_j$ = homogeneous polynomials of degree $2j$ in $z_1, z_2$, with basis $e_m = z_1^{\,j+m}z_2^{\,j-m}$, $m = j, j-1, \dots, -j$: $\dim V_j = 2j + 1$.
>
> **2. A group representation.** $U^{\mathsf T}z$ is linear in $z$, so $P(U^{\mathsf T}z)$ is again homogeneous of degree $2j$. Composition: $(D(U_1)D(U_2)P)(z) = (D(U_2)P)(U_1^{\mathsf T}z) = P(U_2^{\mathsf T}U_1^{\mathsf T}z) = P((U_1U_2)^{\mathsf T}z) = (D(U_1U_2)P)(z)$; $D(\mathbb 1) = \mathbb 1$; $D$ is continuous (polynomial in the entries of $U$). (The transpose is what makes the order come out right; $P(Uz)$ would reverse it.)
>
> **3. Its generators.** For $X \in \mathfrak{su}(2)$, by the chain rule and $(e^{sX})^{\mathsf T} = e^{sX^{\mathsf T}}$,
>
> $$
> d(X)P = \frac{d}{ds}P\bigl(e^{sX^{\mathsf T}}z\bigr)\Big|_{s=0} = \sum_a (X^{\mathsf T}z)_a\,\frac{\partial P}{\partial z_a} = \sum_{a,b}X_{ba}\,z_b\,\frac{\partial P}{\partial z_a} .
> $$
>
> This is complex-linear in $X$, so for every complex $2\times2$ matrix $T$ the physicist's generator ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-5|Def. §CB.2.5]], extended by [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-7|Def. §CB.3.7]]) is $D(T) = i\,d(-iT) = \sum_{a,b}T_{ba}z_b\,\partial_a$.
>
> **4. The ladder.** $\tau^3 = \operatorname{diag}(\frac12, -\frac12)$ gives $D(\tau^3) = \frac12(z_1\partial_1 - z_2\partial_2)$, and $D(\tau^3)e_m = \frac12[(j+m) - (j-m)]e_m = m\,e_m$. $\tau^+ = \tau^1 + i\tau^2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has only $T_{12} = 1$, so $D(\tau^+) = z_1\partial_2$ and $D(\tau^+)e_m = (j - m)\,e_{m+1}$; $\tau^- = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ gives $D(\tau^-) = z_2\partial_1$, $D(\tau^-)e_m = (j + m)\,e_{m-1}$.
>
> **5. It is $D^{(j)}$.** $e_j = z_1^{2j}$ has $D(\tau^+)e_j = 0$ and $D(\tau^3)e_j = j\,e_j$: a highest-weight vector of weight $j$. By [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], 1, the vectors $(z_2\partial_1)^kz_1^{2j} = \frac{(2j)!}{(2j-k)!}z_1^{2j-k}z_2^{\,k}$, $k = 0, \dots, 2j$, span an irreducible subspace; they are nonzero multiples of all basis vectors, so $V_j$ itself is irreducible with highest weight $j$, and its algebra representation is equivalent to $D^{(j)}$ (Theorem §CB.9.3, 2). Uniqueness: $SU(2)$ is connected, so a group representation is fixed by its algebra representation up to the same equivalence ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], 2).
>
> **6. The element $-\mathbb 1$.** $(D(-\mathbb 1)P)(z) = P(-z) = (-1)^{2j}P(z)$ for $P$ homogeneous of degree $2j$. Check through the exponential: $-\mathbb 1 = e^{-2\pi i\tau^3}$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-19|Theorem §CB.1.19]], 4), so $D(-\mathbb 1) = e^{-2\pi iD(\tau^3)}$, which multiplies $e_m$ by $e^{-2\pi im} = (-1)^{2j}$, since $m - j$ is an integer. ⚑ By-product: $-\mathbb 1$ commutes with all of $SU(2)$, so on any irreducible representation it must be a number (Schur, [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-4|Theorem §CB.6.4]]) whose square is $D(\mathbb 1) = \mathbb 1$; the number is $(-1)^{2j}$, the parity of the number of spinor slots → [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^rem-cb-9-3|Remark: Spin j is 2j symmetrized spin-½ slots]].
>
> **7. Integer $j$ descends to $SO(3)$.** If $D(-\mathbb 1) = \mathbb 1$, define $\bar D(R(U)) = D(U)$. This is well defined because $R(U) = R(U')$ iff $U' = \pm U$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-20|Theorem §CB.1.20]], 3) and $D(-U) = D(-\mathbb 1)D(U) = D(U)$; it is a homomorphism, $\bar D(R(U_1)R(U_2)) = \bar D(R(U_1U_2)) = D(U_1U_2) = D(U_1)D(U_2)$; and it is continuous because $R$ is a quotient map, $SO(3) \cong SU(2)/\{\pm\mathbb 1\}$. Its algebra representation is $D^{(j)}$ transported by the isomorphism of Theorem §CB.1.21.
>
> **8. Half-integer $j$ does not.** Suppose $\bar D$ were a representation of $SO(3)$ with algebra representation $D^{(j)}$, $j$ half-integer. Then $\bar D\circ R$ is a representation of $SU(2)$ with the same algebra representation, so (Theorem §CB.2.8, 1, applied to $\bar D\circ R$) $\bar D(R(e^{X})) = e^{d(X)}$ for every $X$. Take $X = -2\pi i\tau^3$: the left side is $\bar D(R(-\mathbb 1)) = \bar D(\mathbb 1) = \mathbb 1$; the right side is $(-1)^{2j}\mathbb 1 = -\mathbb 1$ by step 6. Contradiction. ⚑ By-product: the path $\theta \mapsto e^{-i\theta\tau^3}$, $0 \le \theta \le 2\pi$, runs from $\mathbb 1$ to $-\mathbb 1$ in $SU(2)$ while its image $R_z(\theta)$ returns to $\mathbb 1$: a closed loop in $SO(3)$ whose lift is open. The obstruction is topological → [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]].
>
> **9. Part 3.** A finite-dimensional representation of $SU(2)$ is an orthogonal sum of irreducible ones (Theorem §CB.6.16, 2). Each irreducible piece has an irreducible algebra representation (Theorem §CB.2.8, 2), equivalent to some $D^{(j)}$ (Theorem §CB.9.3, 2), so the piece is equivalent to the representation of step 5 (Theorem §CB.2.8, 2 again). For $SO(3)$, pull back along $R$ (step 7): the pieces have $D(-\mathbb 1) = \mathbb 1$, so integer $j$.
>
> **What the derivation shows**
> - Every irreducible representation of the algebra integrates to $SU(2)$, explicitly; in general this is guaranteed by simple connectivity (Hall Thm. 16.30), which $SU(2)$ has and $SO(3)$ lacks.
> - Spin $j$ lives on symmetric polynomials of degree $2j$ in two spinor variables: $D^{(j)}$ is the symmetrized product of $2j$ spin-$\frac12$ representations → [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^rem-cb-9-3|Remark: Spin j is 2j symmetrized spin-½ slots]].
> - The $(2j+1)\times(2j+1)$ matrices $D^{(j)}(U)$ in the basis $|j, m\rangle$ are the Wigner functions of Quantum Mechanics ([[§C5.3 The Angular-Momentum Spectrum and Rotation Matrices#^def-c5-3-1|QM Def. §C5.3.1]]), and part 2 is the representation-theoretic form of [[§C5.3 The Angular-Momentum Spectrum and Rotation Matrices#^thm-c5-3-4|QM Theorem §C5.3.4]].
> - Used next: projective representations ([[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^thm-cb-18-7|Theorem §CB.18.7]]); the sign $(-1)^{2(j_+ + j_-)}$ of a $2\pi$ rotation in a Lorentz representation ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]]).

^der-cb-9-10

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-21|Theorem §CB.1.21]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-4|Theorem §CB.6.4]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-16|Theorem §CB.6.16]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-19|Theorem §CB.1.19]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-20|Theorem §CB.1.20]]

> [!remark] Remark: Spin j is 2j symmetrized spin-½ slots
> A homogeneous polynomial of degree $2j$ in $(z_1, z_2)$ is the same thing as a totally symmetric tensor $\psi_{a_1\cdots a_{2j}}$ with $2j$ spinor indices, $P(z) = \psi_{a_1\cdots a_{2j}}z_{a_1}\cdots z_{a_{2j}}$, and $D(U)$ acts by one factor $U$ on each index ($U^{\mathsf T}z$ contracted into each slot). So spin $j$ is the symmetric part of $\frac12\otimes\cdots\otimes\frac12$ ($2j$ factors); the antisymmetric combinations of two slots, built with $\varepsilon_{ab}$, are spin $0$ and are what the Clebsch–Gordan series removes ([[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]]). The sign $(-1)^{2j}$ is $(-1)$ to the number of spinor slots. The Lorentz representation $(j_+, j_-)$ is the same construction with two kinds of spinor index, $2j_+$ symmetrized of one kind and $2j_-$ of the other ([[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-2|Def. §C5a.5.2]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]]; [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]).
>
> *Source: Derivation §CB.9.10, steps 1–6 (written here)*

^rem-cb-9-3

The polynomial model of spin $j$ works for every invertible $2\times2$ matrix, not only for $SU(2)$; the next theorem, and the Lorentz sections ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover|§CB.15]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)|§CB.16]]), use it for $SL(2, \mathbb C)$, together with the automorphism $\lambda \mapsto (\lambda^\dagger)^{-1}$ (extracted from step 1 of [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-9|Derivation §CB.16.9]] in the CB ordering pass):

> [!theorem] Lemma §CB.9.11: Polynomials in Two Variables Carry a Representation of GL(2, ℂ)
> 1. For $j \in \frac12\mathbb Z_{\ge0}$ let $V_j$ be the homogeneous polynomials of degree $2j$ in $z = (z_1, z_2)$. For invertible $M \in GL(2, \mathbb C)$, $\bigl(D^{(j)}(M)P\bigr)(z) = P(M^{\mathsf T}z)$ defines a representation ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-4|Def. §CB.2.4]]) of $GL(2, \mathbb C)$ on $V_j$, whose matrix entries are polynomials in the entries of $M$; restricted to $SU(2)$ it is the representation of [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]], 1, and restricted to $SL(2, \mathbb C)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-2|Def. §CB.1.2]]) a representation of $SL(2, \mathbb C)$.
> 2. $\theta(\lambda) = (\lambda^\dagger)^{-1}$ is a continuous homomorphism of $GL(2, \mathbb C)$ to itself that maps $SL(2, \mathbb C)$ onto $SL(2, \mathbb C)$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (spin $j$ on polynomials), Ch. 8 §8.2 · extracted, text unchanged, from step 1 of Derivation §CB.16.9 (CB ordering pass, 2026-10-08); continuity and $\det\theta(\lambda) = \overline{\det\lambda}^{-1}$ added*

^lem-cb-9-11

> [!proof]- Proof
> **1. A representation.** For any invertible $M_1, M_2$: $(D^{(j)}(M_1)D^{(j)}(M_2)P)(z) = (D^{(j)}(M_2)P)(M_1^{\mathsf T}z) = P(M_2^{\mathsf T}M_1^{\mathsf T}z) = P((M_1M_2)^{\mathsf T}z)$, so $D^{(j)}(M_1M_2) = D^{(j)}(M_1)D^{(j)}(M_2)$; $D^{(j)}(M)P$ is again homogeneous of degree $2j$. $D^{(j)}(\mathbb 1) = \mathbb 1$. In the monomial basis $z_1^az_2^{2j-a}$, the coefficients of $P(M^{\mathsf T}z)$ are polynomials in the entries of $M$, so $D^{(j)}$ is continuous; on $SU(2)$ it is the formula of Theorem §CB.9.10, 1.
>
> **2. The map θ.** The map $\lambda \mapsto (\lambda^\dagger)^{-1}$ is a homomorphism: $((\lambda_1\lambda_2)^\dagger)^{-1} = (\lambda_2^\dagger\lambda_1^\dagger)^{-1} = (\lambda_1^\dagger)^{-1}(\lambda_2^\dagger)^{-1}$. It is continuous (adjoint and inversion are), and $\det\theta(\lambda) = 1/\overline{\det\lambda}$, which is $1$ when $\det\lambda = 1$; $\theta(\theta(\lambda)) = \lambda$, so $\theta$ maps $SL(2, \mathbb C)$ onto itself.

^pf-cb-9-11

*Uses:* [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-4|Def. §CB.2.4]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-2|Def. §CB.1.2]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]]

> [!theorem] Theorem §CB.9.12: Spin j Is the Symmetric Power Sym²ʲℂ²
> For $j \in \frac12\mathbb Z_{\ge0}$, the restriction of $D^{\otimes2j}$ ($D$ the defining representation of $SU(2)$ or $SL(2, \mathbb C)$ on $\mathbb C^2$, [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-1|Def. §CB.7.1]]) to $\operatorname{Sym}^{2j}\mathbb C^2$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-11|Def. §CB.7.11]]) is irreducible and equivalent to $V_j$. The identification with homogeneous polynomials of degree $2j$, $P(z) = \psi_{a_1\cdots a_{2j}}z_{a_1}\cdots z_{a_{2j}}$, is an equivalence with the polynomial realization of [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]]; and $-\mathbb 1$ acts as $(-1)^{2j}$.
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §8.2 (the spin-$\frac n2$ representation on homogeneous polynomials of degree $n$ in $z_1, z_2$), §9.6, eq. (9.4) (symmetric tensors correspond to polynomials, $v_j^n \leftrightarrow v_j\otimes\cdots\otimes v_j$) and §9.4.3 ($V^N$ inside $(V^1)^{\otimes N}$ "giving an alternative to the construction using homogeneous polynomials") · irreducibility and the identification with $V_j$: [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]], Derivation, steps 1–6 (from the user's PHY 513 notes, Ch. 7 §7.2) · the slot picture: [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^rem-cb-9-3|§CB.9, Remark: Spin j is 2j symmetrized spin-½ slots]]*

^thm-cb-9-12

> [!proof]- Proof
> *Woit's two descriptions of spin $j$ — homogeneous polynomials (§8.2) and the symmetric part of $2j$ spinor slots (§9.4.3, §9.6) — identified explicitly; irreducibility is then the polynomial result of Theorem §CB.9.10. Steps 1–2 are stated for $\mathbb C^n$ and degree $k$; they are reused for $\mathbb C^3$ in Theorem §CB.9.16.*
>
> **1. Symmetric tensors are polynomials (Woit (9.4)).** For $\psi \in \operatorname{Sym}^k\mathbb C^n$ put $\Phi(\psi)(z) = \sum_{a_1, \dots, a_k}\psi_{a_1\cdots a_k}z_{a_1}\cdots z_{a_k}$, a homogeneous polynomial of degree $k$; $\Phi$ is linear. Group the index tuples by their type $\alpha = (\alpha_1, \dots, \alpha_n)$, $\alpha_i$ = the number of entries equal to $i$, $|\alpha| = k$. All tuples of type $\alpha$ give the monomial $z^\alpha = z_1^{\alpha_1}\cdots z_n^{\alpha_n}$ and, $\psi$ being symmetric ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-11|Def. §CB.7.11]]), the same component $\psi_\alpha$; there are $\frac{k!}{\alpha_1!\cdots\alpha_n!}$ of them. So
>
> $$
> \Phi(\psi)(z) = \sum_{|\alpha| = k}\frac{k!}{\alpha!}\,\psi_\alpha\,z^\alpha, \qquad \alpha! = \alpha_1!\cdots\alpha_n! .
> $$
>
> The monomials are linearly independent, so $\Phi(\psi) = 0$ forces every $\psi_\alpha = 0$, i.e. $\psi = 0$ (a symmetric tensor is determined by one component per type). Every monomial is reached: $z^\alpha = \Phi(\psi)$ for the symmetric $\psi$ with components $\frac{\alpha!}{k!}$ on the tuples of type $\alpha$ and $0$ elsewhere. $\Phi$ is a linear bijection onto the homogeneous polynomials of degree $k$ (both of dimension $\binom{n+k-1}k$, [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-13|Theorem §CB.7.13]], 1).
>
> **2. Φ is equivariant.** For a matrix $U$, $D^{\otimes k}(U)$ acts on components by $(U^{\otimes k}\psi)_{a_1\cdots a_k} = U_{a_1b_1}\cdots U_{a_kb_k}\psi_{b_1\cdots b_k}$ (one factor per slot, [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-1|Def. §CB.7.1]]). Then, summing first over the $a$'s,
>
> $$
> \Phi(U^{\otimes k}\psi)(z) = \psi_{b_1\cdots b_k}\bigl(U_{a_1b_1}z_{a_1}\bigr)\cdots\bigl(U_{a_kb_k}z_{a_k}\bigr) = \psi_{b_1\cdots b_k}(U^{\mathsf T}z)_{b_1}\cdots(U^{\mathsf T}z)_{b_k} = \Phi(\psi)(U^{\mathsf T}z) .
> $$
>
> The right side is the polynomial action $(D(U)P)(z) = P(U^{\mathsf T}z)$ of [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]]. And $\operatorname{Sym}^k\mathbb C^n$ is invariant under $D^{\otimes k}$ (Theorem §CB.7.13, 1), so $\Phi$ is an equivalence of representations.
>
> **3. n = 2, k = 2j: irreducible and equal to $V_j$.** By Theorem §CB.9.10, Derivation, steps 1–5, the polynomial representation on degree-$2j$ polynomials is irreducible under $SU(2)$ and its algebra representation is $D^{(j)} = V_j$. By step 2 the same holds for $\operatorname{Sym}^{2j}\mathbb C^2$. For $SL(2, \mathbb C)$ the formula $P \mapsto P(A^{\mathsf T}z)$ is the same ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^lem-cb-9-11|Lemma §CB.9.11]], 1); a subspace invariant under $SL(2, \mathbb C)$ is invariant under its subgroup $SU(2)$, so it is irreducible too, and its differential $X \mapsto \sum_{a,b}X_{ba}z_b\partial_a$ (Derivation §CB.9.10, step 3, valid for every complex $2\times2$ matrix) is complex-linear in $X \in \mathfrak{sl}(2, \mathbb C)$, the complex-linear extension of the $\mathfrak{su}(2)$-representation $V_j$.
>
> **4. Second route: weights (Theorem §CB.9.6).** $J^3$ acts by $\frac12(z_1\partial_1 - z_2\partial_2)$ (Derivation §CB.9.10, step 4), so $z_1^{a}z_2^{b}$, $a + b = 2j$, has weight $\frac12(a - b) = a - j$. As $a$ runs over $0, \dots, 2j$ each $m \in \{-j, \dots, j\}$ occurs once: $n_m = 1$ for $|m| \le j$, $m - j \in \mathbb Z$, and $0$ otherwise. By [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-6|Theorem §CB.9.6]] the number of copies of $V_k$ is $n_k - n_{k+1}$, which is $1$ for $k = j$ and $0$ for every other $k$: the representation is $V_j$.
>
> **5. The element −1.** $D^{\otimes2j}(-\mathbb 1) = (-\mathbb 1)^{\otimes2j} = (-1)^{2j}\mathbb 1$: each of the $2j$ slots contributes a factor $-1$ (Derivation §CB.9.10, step 6, in polynomial form: $P(-z) = (-1)^{2j}P(z)$).
>
> **What the proof shows**
> - Spin $j$ is literally $2j$ spin-½ slots, symmetrized: the index picture of [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^rem-cb-9-3|§CB.9, Remark: Spin j is 2j symmetrized spin-½ slots]] is now a theorem, with $\Phi$ the dictionary between the tensor and the polynomial pictures.
> - ⚑ By-product: the sign $(-1)^{2j}$ of a $2\pi$ rotation counts spinor slots; integer spin has an even number of them, which is why it descends to $SO(3)$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-15|Theorem §CB.9.15]]).
> - The same construction for $SL(2, \mathbb C)$ with two kinds of slot gives $(j_+, j_-) \cong \operatorname{Sym}^{2j_+}\mathbb C^2\otimes\operatorname{Sym}^{2j_-}\bar{\mathbb C}^2$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]] realizes the second factor with the matrices $(\lambda^\dagger)^{-1}$, equivalent to $\bar\lambda$; dotted indices, [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-16|Theorem §CB.7.16]]).

^pf-cb-9-12

*Uses:* [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-1|Def. §CB.7.1]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-11|Def. §CB.7.11]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-13|Theorem §CB.7.13]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^lem-cb-9-11|Lemma §CB.9.11]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-6|Theorem §CB.9.6]]

## The Clebsch–Gordan series

The count of weights in a tensor product, first done in Quantum Mechanics for addition of angular momenta and restated here (CB ordering pass, 2026-10-08), since the Clebsch–Gordan series below rests on it:

> [!theorem] Lemma §CB.9.13: The Weight Count of a Tensor Product
> For $j_1, j_2 \in \frac12\mathbb Z_{\ge0}$ and $m$ with $m - (j_1 + j_2) \in \mathbb Z$, let $n(m)$ be the number of pairs $(m_1, m_2)$ with $m_i \in \{-j_i, -j_i + 1, \dots, j_i\}$ and $m_1 + m_2 = m$. Then $n(j) - n(j+1) = 1$ for $j = |j_1 - j_2|, |j_1 - j_2| + 1, \dots, j_1 + j_2$, and $n(j) - n(j+1) = 0$ for the other $j \ge 0$ with $j - (j_1 + j_2) \in \mathbb Z$.
>
> *Source: Griffiths §4.4.3; Greensite §14.1, eqs. (14.50)–(14.56); the user's series, Part IV, §15 · the course's version: step 2 of [[§B6.3 Addition of Angular Momenta#^der-b6-3-2|QM Derivation §B6.3.2]], where the same count, $N_j = n(j) - n(j+1)$, gives the multiplicity of total angular momentum $j$*

^lem-cb-9-13

> [!proof]- Proof
> *Step 2 of QM Derivation §B6.3.2, the counting part, unchanged except that the multiplets are not used.*
>
> Take $j_1 \ge j_2$. For given $m \ge 0$, $m_2$ runs over $[-j_2, j_2]$ subject to $m_1 = m - m_2 \in [-j_1, j_1]$. If $m \le j_1 - j_2$, every $m_2$ is allowed: $n(m) = 2j_2 + 1$. If $j_1 - j_2 \le m \le j_1 + j_2$, the condition is $m_2 \ge m - j_1$, so $n(m) = j_1 + j_2 - m + 1$. Above $j_1 + j_2$, $n = 0$. Hence $n(j) - n(j+1) = (j_1 + j_2 - j + 1) - (j_1 + j_2 - j) = 1$ for $j_1 - j_2 \le j \le j_1 + j_2$ (at $j = j_1 + j_2$: $1 - 0$; at $j = j_1 - j_2$: $(2j_2 + 1) - 2j_2$), and $n(j) - n(j+1) = (2j_2 + 1) - (2j_2 + 1) = 0$ for $0 \le j < j_1 - j_2$ (all $j$ here differ from $j_1 + j_2$ by integers, like the $m$'s). For $j_1 < j_2$ exchange the roles.
>
> **What the proof shows**
> - The count uses only the ranges of $m_1$, $m_2$; no inner product and no operator enters, which is why the Clebsch–Gordan series holds for $\mathfrak{sl}(2, \mathbb C)$ and $SL(2, \mathbb C)$ as well.
> - Equivalence: this is the counting half of QM Derivation §B6.3.2, step 2; the other half there ($n(m) = \sum_{j \ge |m|}N_j$) is [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-6|Theorem §CB.9.6]] in CB.

^pf-cb-9-13

> [!theorem] Theorem §CB.9.14: Clebsch–Gordan Series
> For $j_1, j_2 \in \frac12\mathbb Z_{\ge0}$, as representations of $\mathfrak{sl}(2, \mathbb C)$, $SU(2)$ or $SL(2, \mathbb C)$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-1|Def. §CB.7.1]]),
>
> $$
> V_{j_1}\otimes V_{j_2} \cong \bigoplus_{j = |j_1 - j_2|}^{j_1 + j_2}V_j \qquad (j \text{ in integer steps}) .
> $$
>
> *Source: the home of the series is Quantum Mechanics: [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]] (block form of $\mathscr D^{(j_1)}\otimes\mathscr D^{(j_2)}$) with the count of [[§B6.3 Addition of Angular Momenta#^thm-b6-3-2|QM Theorem §B6.3.2]] (Derivation, step 2), both for Hermitian angular momenta on inner-product spaces · P. Woit, Quantum Theory, Groups and Representations, §9.4.1 (Theorem 9.1, outline by highest weights) and §9.4.2 (proof by characters) · what is new here — no inner product, and the groups $SU(2)$, $SL(2, \mathbb C)$ — written here*

^thm-cb-9-14

> [!proof]- Proof
> *The count is QM's (QM Derivation §B6.3.2, step 2), restated in CB as Lemma §CB.9.13 in the CB ordering pass. What is added: the decomposition needs no inner product (it uses Theorem §CB.9.6 instead of Hermitian multiplets), and it holds for the groups $SU(2)$ and $SL(2, \mathbb C)$.*
>
> **1. Weights add.** Let $e_{m_1}$, $f_{m_2}$ be the weight bases of $V_{j_1}$, $V_{j_2}$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-5|Theorem §CB.9.5]], 3). On $V_{j_1}\otimes V_{j_2}$ the generator $J^3$ acts by $J^3\otimes\mathbb 1 + \mathbb 1\otimes J^3$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-3|Theorem §CB.7.3]]), so
>
> $$
> J^3(e_{m_1}\otimes f_{m_2}) = (m_1 + m_2)\,e_{m_1}\otimes f_{m_2} ,
> $$
>
> and the $e_{m_1}\otimes f_{m_2}$ are a basis ([[§38 Tensor Products#^ladr-9-74|LADR Thm. 9.74]]). The multiplicity $n(m)$ of the weight $m$ is the number of pairs $(m_1, m_2)$, $|m_1| \le j_1$, $|m_2| \le j_2$, $m_1 + m_2 = m$.
>
> **2. The count.** This is exactly the number $n(m)$ counted in [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^lem-cb-9-13|Lemma §CB.9.13]], which finds $n(j) - n(j+1) = 1$ for $j = |j_1 - j_2|, |j_1 - j_2| + 1, \dots, j_1 + j_2$ and $0$ for the other $j \ge 0$ with $j - (j_1 + j_2) \in \mathbb Z$. For $j$ with $j - (j_1 + j_2) \notin \mathbb Z$, no $m_1 + m_2$ equals $j$, so $n(j) = n(j+1) = 0$.
>
> **3. The algebra.** $V_{j_1}\otimes V_{j_2}$ is a complex-linear representation of $\mathfrak{sl}(2, \mathbb C)$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-2|Def. §CB.7.2]]: a sum of complex-linear maps of $X$). By [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-6|Theorem §CB.9.6]] the number of copies of $V_j$ in it is $n(j) - n(j+1)$, which step 2 evaluated: $V_{j_1}\otimes V_{j_2} \cong \bigoplus_{j=|j_1-j_2|}^{j_1+j_2}V_j$ as $\mathfrak{sl}(2, \mathbb C)$-representations, hence (restriction, [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-9|Theorem §CB.3.9]]) as $\mathfrak{su}(2)$-representations. QM's proof used Hermitian $\mathbf J^2$, $J_z$ to produce the multiplets; here complete reducibility (Theorem §CB.9.5, 1) does it.
>
> **4. SU(2).** As group representations $V_j = \operatorname{Sym}^{2j}\mathbb C^2$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-12|Theorem §CB.9.12]]), and the differential of $V_{j_1}\otimes V_{j_2}$ is the tensor product of the differentials (Theorem §CB.7.3, 2). $SU(2)$ is connected ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]]), so two of its representations are equivalent iff their algebra representations are ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], 2). Step 3 gives the equivalence of the algebra representations, hence of the group representations.
>
> **5. SL(2, ℂ).** The differentials of $\operatorname{Sym}^{2j}\mathbb C^2$ are complex-linear on $\mathfrak{sl}(2, \mathbb C)$ (Theorem §CB.9.12, step 3), so the differential of $V_{j_1}\otimes V_{j_2}$, and of $\bigoplus V_j$, is the complex-linear representation of step 3 viewed on the real Lie algebra of $SL(2, \mathbb C)$. The intertwiner of step 3 commutes with every $d(X)$, $X \in \mathfrak{sl}(2, \mathbb C)$, so it intertwines the algebra representations of $SL(2, \mathbb C)$. $SL(2, \mathbb C)$ is connected ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-9|Theorem §CB.9.9]]), and Theorem §CB.2.8, 2 again gives the group equivalence.
>
> **What the proof shows**
> - The series is a statement about weights alone; inner products, Hermiticity and the Clebsch–Gordan coefficients are not needed for it (they are needed for the *unitary* change of basis, QM Definition §C7.1.1).
> - ⚑ By-product: because the argument never uses unitarity, it applies verbatim to each $\mathfrak{sl}(2, \mathbb C)$ factor of the complexified Lorentz algebra, where no invariant inner product exists → [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-11|Theorem §CB.16.11]].
> - Woit's character proof (§9.4.2) is the same count written as a product of generating functions: $\chi_{V_{j_1}}\chi_{V_{j_2}} = \sum_j\chi_{V_j}$.

^pf-cb-9-14

*Uses:* [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-2|Def. §CB.7.2]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-3|Theorem §CB.7.3]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-5|Theorem §CB.9.5]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-6|Theorem §CB.9.6]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-12|Theorem §CB.9.12]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^lem-cb-9-13|Lemma §CB.9.13]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-9|Theorem §CB.9.9]], [[§38 Tensor Products#^ladr-9-74|LADR Thm. 9.74]]

Quantum Mechanics proves the same series for Hermitian angular momenta, with the explicit Clebsch–Gordan coefficients, in [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients|QM §C7.1]] ([[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]]); Theorem §CB.9.14 is the same statement without an inner product (the embed of the QM box was replaced by this pointer in the CB ordering pass).

## Descent to a quotient group

> [!theorem] Theorem §CB.9.15: Descent Lemma
> Let $p : \tilde G \to G$ be a surjective Lie group homomorphism ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]]) that is a covering map (e.g. Theorem §CB.2.20), with kernel $N$. A representation $\tilde D$ of $\tilde G$ is of the form $\tilde D = D\circ p$ for a representation $D$ of $G$ iff $\tilde D(n) = \mathbb 1$ for all $n \in N$; then $D$ is unique, and $D$ is irreducible iff $\tilde D$ is. Instances: $SU(2) \to SO(3)$ and $SL(2, \mathbb C) \to SO^+(1,3)$, $N = \{\pm\mathbb 1\}$, where the condition is $\tilde D(-\mathbb 1) = \mathbb 1$.
>
> *Source: [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]] (the group part) · written here*

^thm-cb-9-15

> [!proof]- Proof
> **1. Necessity.** If $\tilde D = D\circ p$ and $n \in N$, then $\tilde D(n) = D(p(n)) = D(\mathbb 1) = \mathbb 1$.
>
> **2. Definition of D.** Suppose $\tilde D(N) = \{\mathbb 1\}$. For $g \in G$ pick $\tilde g$ with $p(\tilde g) = g$ ($p$ is onto) and put $D(g) = \tilde D(\tilde g)$. Another choice is $\tilde gn$ with $n \in N$ ([[§15 Homomorphisms#^def-15-3|493 Def. §15.3]]: $p(\tilde g') = p(\tilde g)$ iff $\tilde g^{-1}\tilde g' \in N$), and $\tilde D(\tilde gn) = \tilde D(\tilde g)\tilde D(n) = \tilde D(\tilde g)$; so $D$ is well defined. This is the first isomorphism theorem applied to $\tilde D$, whose kernel contains $N$ ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]).
>
> **3. Homomorphism.** $p(\tilde g\tilde h) = gh$, so $D(gh) = \tilde D(\tilde g\tilde h) = \tilde D(\tilde g)\tilde D(\tilde h) = D(g)D(h)$, and $D(\mathbb 1) = \tilde D(\mathbb 1) = \mathbb 1$.
>
> **4. Continuity.** Near any $g \in G$ a covering map has a continuous local inverse $s$ (an evenly covered neighbourhood, [[§31 Covering Spaces#^def-31-2|590 Def. §31.2]]), and $D = \tilde D\circ s$ there, a composition of continuous maps.
>
> **5. Uniqueness and irreducibility.** $D(g)$ is forced to be $\tilde D(\tilde g)$, so $D$ is unique; and $D(G) = \tilde D(\tilde G)$ as sets of operators, so the invariant subspaces of $D$ and $\tilde D$ coincide.

^pf-cb-9-15

> [!theorem] Theorem §CB.9.16: Integer Spin Is Built from Vectors
> 1. $V_1$ is equivalent to the complexified vector representation of $SO(3)$ on $\mathbb C^3$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-16|Def. §CB.3.16]]).
> 2. For every integer $l \ge 0$, $V_l$ is equivalent to the space of traceless symmetric tensors in $\operatorname{Sym}^l\mathbb C^3$, a subrepresentation of $(\mathbb C^3)^{\otimes l}$. So every representation of $SO(3)$ is contained in a sum of tensor powers of the vector representation.
>
> *Source: B. C. Hall, Quantum Theory for Mathematicians, §17.6: Def. 17.11 and Thm. 17.12 (the harmonic polynomials of degree $l$ on $\mathbb R^3$ form an irreducible representation of $SO(3)$ of dimension $2l + 1$), with Lemma 17.13, Cor. 17.14 ($\Delta : P_l \to P_{l-2}$ is onto, via an inner product with $\langle p, \partial_jq\rangle = \langle x_jp, q\rangle$), Lemma 17.16 (the highest weight vector $(x_1 + ix_2)^l$) and Cor. 17.17 · symmetric tensors as polynomials: [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-12|Theorem §CB.9.12]], Proof, steps 1–2 (P. Woit, §9.6, eq. (9.4)) · part 1 also: [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^ex-c3-1-1|Example §C3.1.1]] (the user's PHY 513 notes, Ch. 7 §7.2, four-vector example)*

^thm-cb-9-16

> [!proof]- Proof
> *Hall's proof of Thm. 17.12 (points 1–2), with two changes: harmonic polynomials are first identified with traceless symmetric tensors (steps 1–3), and Hall's analytic (Segal–Bargmann) inner product in Lemma 17.13 is replaced by the combinatorial one he mentions, for which the needed identity is checked on monomials (step 4).*
>
> **1. The traceless symmetric tensors form a subrepresentation.** $SO(3)$ acts on $\mathbb C^3$ by its real matrices (the complexified vector representation, [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-16|Def. §CB.3.16]]) and on $(\mathbb C^3)^{\otimes l}$ by $R^{\otimes l}$; $\operatorname{Sym}^l\mathbb C^3$ is invariant ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-13|Theorem §CB.7.13]], 1). For $l \ge 2$ define the trace $t : \operatorname{Sym}^l\mathbb C^3 \to \operatorname{Sym}^{l-2}\mathbb C^3$, $(tT)_{a_3\cdots a_l} = \sum_iT_{ii\,a_3\cdots a_l}$. It is an intertwiner: using $\sum_iR_{ib_1}R_{ib_2} = (R^{\mathsf T}R)_{b_1b_2} = \delta_{b_1b_2}$,
>
> $$
> \bigl(t\,R^{\otimes l}T\bigr)_{a_3\cdots a_l} = \sum_iR_{ib_1}R_{ib_2}R_{a_3b_3}\cdots R_{a_lb_l}T_{b_1b_2b_3\cdots b_l} = R_{a_3b_3}\cdots R_{a_lb_l}\sum_{b}T_{bb\,b_3\cdots b_l} = \bigl(R^{\otimes(l-2)}\,tT\bigr)_{a_3\cdots a_l} .
> $$
>
> So $S^0_l = \ker t$, the traceless symmetric tensors, is invariant ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-3|Theorem §CB.6.3]]). For $l = 0, 1$ there is no pair of slots to contract and $S^0_l = \operatorname{Sym}^l\mathbb C^3$.
>
> **2. To polynomials.** By Theorem §CB.9.12, Proof, steps 1–2 (with $n = 3$, $k = l$), $\Phi(T)(x) = \sum T_{a_1\cdots a_l}x_{a_1}\cdots x_{a_l}$ is a linear bijection of $\operatorname{Sym}^l\mathbb C^3$ onto the space $P_l$ of homogeneous complex polynomials of degree $l$ in $x \in \mathbb R^3$, and $\Phi(R^{\otimes l}T)(x) = \Phi(T)(R^{\mathsf T}x) = \Phi(T)(R^{-1}x)$: the action $(R\cdot p)(x) = p(R^{-1}x)$ that Hall uses.
>
> **3. Traceless is harmonic.** Differentiate $\Phi(T)$ with the product rule; by symmetry of $T$ each of the $l$ terms is the same: $\partial_k\Phi(T) = l\sum T_{k\,a_2\cdots a_l}x_{a_2}\cdots x_{a_l}$, and again $\partial_k\partial_k\Phi(T) = l(l-1)\sum T_{kk\,a_3\cdots a_l}x_{a_3}\cdots x_{a_l}$. Summing over $k$,
>
> $$
> \Delta\,\Phi(T) = l(l-1)\,\Phi(tT) .
> $$
>
> For $l \ge 2$, $l(l-1) \ne 0$ and $\Phi$ is injective on $\operatorname{Sym}^{l-2}$, so $\Delta\Phi(T) = 0$ iff $tT = 0$. Hence $\Phi$ maps $S^0_l$ onto $H_l$, the harmonic polynomials in $P_l$ (Hall's $V_l$, Def. 17.11), equivariantly; for $l \le 1$ both are everything.
>
> **4. An inner product with $\Delta^{\ast} = |x|^2$ (Hall, Lemma 17.13).** On complex polynomials put $\langle x^\alpha, x^\beta\rangle = \alpha!\,\delta_{\alpha\beta}$ for monomials ($\alpha! = \alpha_1!\alpha_2!\alpha_3!$), extended conjugate-linearly in the first and linearly in the second slot: positive definite, monomials orthogonal. On monomials, with $e_j$ the $j$-th unit multi-index,
>
> $$
> \langle x^\alpha, \partial_jx^\beta\rangle = \beta_j\langle x^\alpha, x^{\beta - e_j}\rangle = \beta_j\,\alpha!\,\delta_{\alpha, \beta - e_j}, \qquad \langle x_jx^\alpha, x^\beta\rangle = (\alpha + e_j)!\,\delta_{\alpha + e_j, \beta} = (\alpha_j + 1)\,\alpha!\,\delta_{\alpha + e_j, \beta} ,
> $$
>
> equal because $\beta_j = \alpha_j + 1$ when $\beta = \alpha + e_j$. By linearity $\langle p, \partial_jq\rangle = \langle x_jp, q\rangle$ for all $p, q$; applying it twice and summing over $j$, $\langle p, \Delta q\rangle = \langle |x|^2p, q\rangle$, $|x|^2 = x_1^2 + x_2^2 + x_3^2$.
>
> **5. $\dim H_l = 2l + 1$ (Hall, Cor. 17.14).** By step 4 the adjoint of $\Delta : P_l \to P_{l-2}$ is multiplication by $|x|^2 : P_{l-2} \to P_l$, which is injective ($|x|^2p = 0$ forces $p = 0$, a product of nonzero polynomials being nonzero). The orthogonal complement of the range of $\Delta$ is the null space of its adjoint ([[§23 Self-Adjoint and Normal Operators#^ladr-7-6|LADR Thm. 7.6]]), here $0$, so $\Delta$ is onto. With $\dim P_l = \binom{l+2}{l} = \frac{(l+2)(l+1)}2$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-13|Theorem §CB.7.13]], 1, and step 2) and the fundamental theorem of linear maps ([[§8 Null Spaces and Ranges#^ladr-3-21|LADR Thm. 3.21]]),
>
> $$
> \dim H_l = \dim P_l - \dim P_{l-2} = \frac{(l+2)(l+1)}2 - \frac{l(l-1)}2 = 2l + 1 \qquad (l \ge 2),
> $$
>
> and $\dim H_0 = 1$, $\dim H_1 = 3$ directly.
>
> **6. The generators as differential operators.** With $R_k(\theta) = e^{-i\theta J_k}$, $(J_k)_{lm} = -i\varepsilon_{klm}$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-21|Theorem §CB.1.21]]), $R_3(\theta)$ rotates the $(x_1, x_2)$ plane counterclockwise, and $R_3(\theta)^{-1}x = (x_1\cos\theta + x_2\sin\theta,\ -x_1\sin\theta + x_2\cos\theta,\ x_3)$. The generator on polynomials is $D(J_k) = i\frac{d}{d\theta}\bigl(R_k(\theta)\cdot p\bigr)\big|_{\theta=0}$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], 1, physicists' form), and by the chain rule $\frac{d}{d\theta}p(R_3(\theta)^{-1}x)\big|_0 = x_2\partial_1p - x_1\partial_2p$. The same computation with $R_1(\theta)^{-1}x = (x_1,\ x_2\cos\theta + x_3\sin\theta,\ -x_2\sin\theta + x_3\cos\theta)$ and $R_2(\theta)^{-1}x = (x_1\cos\theta - x_3\sin\theta,\ x_2,\ x_1\sin\theta + x_3\cos\theta)$ gives
>
> $$
> D(J_1) = i(x_3\partial_2 - x_2\partial_3), \qquad D(J_2) = i(x_1\partial_3 - x_3\partial_1), \qquad D(J_3) = i(x_2\partial_1 - x_1\partial_2),
> $$
>
> Hall's $L_k$.
>
> **7. A highest weight vector (Hall, Lemma 17.16).** Let $p_l = (x_1 + ix_2)^l$, $z = x_1 + ix_2$: $\partial_1p_l = lz^{l-1}$, $\partial_2p_l = ilz^{l-1}$, $\partial_3p_l = 0$. Harmonic: $\partial_1^2p_l + \partial_2^2p_l = l(l-1)z^{l-2} + i^2l(l-1)z^{l-2} = 0$. Weight: $D(J_3)p_l = i(x_2 - ix_1)\,lz^{l-1} = i(-i)(x_1 + ix_2)\,lz^{l-1} = l\,p_l$. Raising: $D(J^+) = D(J_1) + iD(J_2) = i(x_3\partial_2 - x_2\partial_3) - (x_1\partial_3 - x_3\partial_1)$, and on $p_l$ the $\partial_3$ terms vanish: $D(J^+)p_l = ix_3\cdot ilz^{l-1} + x_3\cdot lz^{l-1} = -x_3lz^{l-1} + x_3lz^{l-1} = 0$.
>
> **8. Irreducible of spin l (Hall, Cor. 17.17).** $H_l$ is invariant (step 3 and step 1). By [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], 1, the vectors $D(J^-)^kp_l$, $k = 0, \dots, 2l$, span an irreducible invariant subspace of dimension $2l + 1$ with highest weight $l$, inside $H_l$; by step 5 it is all of $H_l$. So $H_l$ is irreducible and its algebra representation is $V_l = D^{(l)}$ (Theorem §CB.9.3, 2). $SO(3)$ is connected ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]], 2), so as a group representation $H_l$ is equivalent to the spin-$l$ representation of $SO(3)$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]], 2; equivalence from the algebra, [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], 2). With step 3, $S^0_l \cong H_l \cong V_l$: part 2.
>
> **9. Part 1.** For $l = 1$, $S^0_1 = \mathbb C^3$ (step 1), so $V_1$ is the complexified vector representation.
>
> **10. Every representation of SO(3).** A finite-dimensional representation of $SO(3)$ is a direct sum of $V_{l_k}$ with integer $l_k$ (Theorem §CB.9.10, 3), and $V_{l_k} \cong S^0_{l_k} \subset (\mathbb C^3)^{\otimes l_k}$; so it is equivalent to a subrepresentation of $\bigoplus_k(\mathbb C^3)^{\otimes l_k}$.
>
> **What the proof shows**
> - The course's computation of part 1: [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^ex-c3-1-1|Example §C3.1.1]] finds the same by computing the weights $1, 0, -1$ on $\mp(e_1 \pm ie_2)/\sqrt2$, $e_3$ (moved here from step 9, CB ordering pass).
> - Integer spin needs no spinors: spin $l$ is the traceless symmetric part of $l$ vector slots, equivalently the harmonic polynomials of degree $l$, whose restrictions to the sphere are the spherical harmonics $Y_l^m$ (Hall, Thm. 17.12, points 3–4).
> - ⚑ By-product: $\operatorname{Sym}^l\mathbb C^3 = S^0_l\oplus|x|^2\operatorname{Sym}^{l-2}\mathbb C^3$ (step 5: the range of $|x|^2$ is the orthogonal complement of $\ker\Delta$), i.e. $\operatorname{Sym}^lV_1 \cong V_l\oplus V_{l-2}\oplus V_{l-4}\oplus\cdots$ — each trace removed is a lower spin (Hall, Cor. 17.15).
> - Half-integer spin is exactly what tensor powers of the vector representation cannot reach ($-\mathbb 1 \in SU(2)$ acts trivially on them); the spinor representations of §CB.13 fill the gap, and the TA's theorem (§CB.14, §CB.17) says spinor ⊗ tensor reaches everything.

^pf-cb-9-16

*Uses:* [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-16|Def. §CB.3.16]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-3|Theorem §CB.6.3]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-13|Theorem §CB.7.13]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-12|Theorem §CB.9.12]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-21|Theorem §CB.1.21]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]], [[§23 Self-Adjoint and Normal Operators#^ladr-7-6|LADR Thm. 7.6]], [[§8 Null Spaces and Ranges#^ladr-3-21|LADR Thm. 3.21]]

The topology behind the descent is [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]], above.

> [!remark]- Connections
> - Theorem §CB.9.15 is the single mechanism behind three course theorems: integer spin integrates to SO(3) ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]]), integer $(j_+, j_-)$ to $SO^+(1,3)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]]), and the general tensor/spinor split ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-10|Theorem §CB.16.10]]).
> - The Clebsch–Gordan series of Theorem §CB.9.14 is used copy by copy for the Lorentz group ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-11|Theorem §CB.16.11]]) and in the 3D and 4D versions of the TA's theorem (Theorem §CB.14.6, Theorem §CB.17.16).
> - **Used in**: Definitions §CB.9.1–§CB.9.2, Theorem §CB.9.5 — [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-14|Theorem §CB.16.14]] (step 4); Theorem §CB.9.12 — [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^rem-cb-9-3|§CB.9, Remark: Spin j is 2j symmetrized spin-½ slots]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]]; Theorem §CB.9.14 — [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-11|Theorem §CB.16.11]], [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^ex-c3-1-1|Example §C3.1.1]]; Theorem §CB.9.15 — [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-10|Theorem §CB.16.10]]; Theorem §CB.9.16 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^ex-c3-1-1|Example §C3.1.1]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-8|Theorem §C3.6.8]]; Definition §CB.9.7 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded), [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded; cited in [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-4|§C3.3, Remark: Why a spinor's matrix is fixed only up to sign]]), [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra|§C3.4]] (embedded; cited in [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-1|§C3.4, Remark: Why unitary, and why the covering group]]), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]), [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]]; Theorem §CB.9.3 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded; cited in [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^rem-c3-1-4|§C3.1, Remark: "One representation for each dimension" needs two qualifiers]], [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^cau-c3-1-4|§C3.1, Caution: Names for the rotation matrices]]), [[§C3.6★ Particle States and the Little Group|§C3.6★]] (embedded; cited in [[§C3.6★ Particle States and the Little Group#^thm-c3-6-8|Theorem §C3.6.8]]), [[§C3.7★ Massless Particles and Helicity|§C3.7★]] (embedded; cited in [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]]), [[§C1a.6 Infinitesimal Lorentz Transformations and Generators|§C1a.6]] (cited in [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^rem-c1a-6-3|§C1a.6, Remark: Why generators]]), [[§C3.3 Primitive and Traceless Moments|EM §C3.3]] (cited in [[§C3.3 Primitive and Traceless Moments#^thm-c3-3-4|EM Theorem §C3.3.4]]); §CB.9, Caution: Phase conventions for the ladder operators — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded); Theorem §CB.9.10 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded), [[§C3.6★ Particle States and the Little Group|§C3.6★]] (embedded; cited in [[§C3.6★ Particle States and the Little Group#^thm-c3-6-8|Theorem §C3.6.8]]), [[§C3.7★ Massless Particles and Helicity|§C3.7★]] (embedded; cited in [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]]); Theorem §CB.9.8 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded), [[§C3.7★ Massless Particles and Helicity|§C3.7★]] (embedded; cited in [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]]), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (cited in the text); §CB.9, Remark: The same pattern for the Lorentz group — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded), [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (cited in [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-4|§C3.3, Remark: Why a spinor's matrix is fixed only up to sign]]), [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra|§C3.4]] (cited in [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-1|§C3.4, Remark: Why unitary, and why the covering group]]), [[§C3.7★ Massless Particles and Helicity|§C3.7★]] (cited in [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]]).
