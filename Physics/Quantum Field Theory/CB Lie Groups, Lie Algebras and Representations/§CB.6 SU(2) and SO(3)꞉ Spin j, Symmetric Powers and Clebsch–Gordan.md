---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element]] →

*Sources: the user's PHY 513 notes, Ch. 7 §7.2 · Quantum Mechanics §B6.3, §C7.1 · Differentiable Manifolds (591) and Group Theory (493), for the descent lemma · P. Woit, Quantum Theory, Groups and Representations, §§8.1–8.2, 9.4, 9.6 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · B. C. Hall, Quantum Theory for Mathematicians, §17.6 · the rest written here.*

What are all finite-dimensional representations of SU(2) and SO(3), how are they built from spin ½, and how do they multiply? The course classifies the irreducible representations of the rotation algebra by highest weight and integrates them to SU(2) and SO(3) ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]]); Quantum Mechanics adds angular momenta ([[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]]). This section puts these in the language of §CB.2–§CB.4: $\mathfrak{sl}(2, \mathbb C)$ and weights, complete reducibility, spin $j$ as the symmetric power $\operatorname{Sym}^{2j}\mathbb C^2$, the Clebsch–Gordan series as a statement about tensor products, and the descent lemma that decides which representations of a covering group are representations of the quotient. The three-dimensional Clifford picture of the same objects is [[§CB.10 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half|§CB.10]].

<!-- MOVE row (CB-INVENTORY): Remark "Spin j is 2j symmetrized spin-½ slots" (rem-c3-1-6) is embedded below; it is to be moved here in batch 4 and upgraded to Theorem §CB.6.5 with proof. -->

## 𝔰𝔩(2,ℂ) and weights

> [!definition] Definition §CB.6.1: The Standard Basis of 𝔰𝔩(2,ℂ)
> The **standard basis** of $\mathfrak{sl}(2, \mathbb C)$ is
>
> $$
> H = \begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix}, \quad E = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix}, \quad F = \begin{pmatrix} 0 & 0 \\ 1 & 0\end{pmatrix}, \qquad [H, E] = 2E, \quad [H, F] = -2F, \quad [E, F] = H .
> $$
>
> Under $\mathfrak{su}(2)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-4|Theorem §CB.2.4]]) and complex-linear extension of a representation ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]]): $H = 2J^3$, $E = J^+$, $F = J^-$ in the physicists' generators of the defining representation.
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §8.1.2 (the basis $S_3$, $S_\pm = S_1 \pm iS_2$ of $\mathfrak{sl}(2, \mathbb C)$, $[S_3, S_\pm] = \pm S_\pm$, $[S_+, S_-] = 2S_3$) · the names $H, E, F$ written here*

^def-cb-6-1

> [!definition] Definition §CB.6.2: Weight and Weight Space
> For a representation of $\mathfrak{sl}(2, \mathbb C)$ (equivalently of $\mathfrak{su}(2)$) on $W$, the **weight space** of weight $m \in \mathbb C$ is $W_m = \{w : J^3w = mw\}$, $J^3 = \frac12H$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-6-1|Def. §CB.6.1]]); $m$ is a **weight** if $W_m \ne 0$, and $\dim W_m$ is its **multiplicity**.
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §8.1.2 (Definition: weights and weight spaces; Woit labels by $k = 2m$, the eigenvalue of $\pi'(2S_3)$) · written here*

^def-cb-6-2

> [!theorem] Theorem §CB.6.3: Finite-Dimensional Representations of 𝔰𝔩(2,ℂ)
> Let $W$ be a finite-dimensional complex-linear representation of $\mathfrak{sl}(2, \mathbb C)$. Then:
> 1. $W$ is completely reducible ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-15|Theorem §CB.3.15]]) and $J^3$ is diagonalizable: $W = \bigoplus_mW_m$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-6-2|Def. §CB.6.2]]);
> 2. every weight lies in $\frac12\mathbb Z$, and $J^\pm W_m \subset W_{m\pm1}$;
> 3. the irreducible ones are the $V_j$ of the course's classification ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]]), with weights $j, j-1, \dots, -j$, each of multiplicity one.
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §8.1.1 (weights and weight spaces) and §8.1.2 (raising and lowering operators: $[S_3, S_+] = S_+$ gives $V_k \to V_{k+2}$ in his normalization; the highest weight theorem) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the classification and its proof: [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]] (from the user's PHY 513 notes, Ch. 7 §7.2) · complete reducibility: [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-15|Theorem §CB.3.15]]*

^thm-cb-6-3

> [!proof]- Proof
> *Woit's route (§8.1): decompose, read off the weights from the irreducible pieces, and shift them with the ladder operators. Woit obtains the weight decomposition from the circle subgroup of the group; here it comes from complete reducibility of the algebra.*
>
> **1. From $\mathfrak{sl}(2, \mathbb C)$ to $\mathfrak{su}(2)$.** $\mathfrak{su}(2)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-4|Theorem §CB.2.4]]), so restricting the complex-linear representation to $\mathfrak{su}(2)$ gives a representation $d$ of $\mathfrak{su}(2)$ with $d_{\mathbb C}$ the original one and the same invariant subspaces and intertwiners ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]]). Via $\mathfrak{su}(2) \cong \mathfrak{so}(3)$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]]) its physicists' generators $J^i$ obey $[J^i, J^j] = i\varepsilon^{ijk}J^k$, and $J^3 = \frac12H$, $J^\pm = J^1 \pm iJ^2$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-6-1|Def. §CB.6.1]]).
>
> **2. Complete reducibility.** By Weyl's unitary trick with $K = SU(2)$ ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-15|Theorem §CB.3.15]]), $W = W^{(1)}\oplus\cdots\oplus W^{(r)}$ with each $W^{(k)}$ invariant and irreducible.
>
> **3. Each piece is some $V_j$.** An irreducible finite-dimensional representation of the rotation algebra is equivalent to $D^{(j)} = V_j$ for one $j \in \{0, \frac12, 1, \dots\}$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]], 2), and $V_j$ has the basis $|j, m\rangle$, $m = j, j-1, \dots, -j$, with $J^3|j, m\rangle = m|j, m\rangle$ (Theorem §C3.1.6, 3; no inner product is used in that derivation). Transport these bases into the $W^{(k)}$ by the equivalences.
>
> **4. Part 1.** The union of the bases of step 3 is a basis of $W$ ([[§6 Dimension#^ladr-2-43|LADR Thm. 2.43]] and the direct sum) consisting of eigenvectors of $J^3$, so $J^3$ is diagonalizable and $W = \bigoplus_mW_m$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-6-2|Def. §CB.6.2]]), $W_m$ spanned by the basis vectors with eigenvalue $m$.
>
> **5. Part 2, weights.** Every eigenvalue in step 4 is some $m$ with $j - m \in \{0, 1, \dots, 2j\}$ and $2j \in \mathbb Z$, so $2m \in \mathbb Z$: $m \in \frac12\mathbb Z$.
>
> **6. Part 2, ladder (Woit §8.1.2).** $[J^3, J^\pm] = \pm J^\pm$ (expand $[J^3, J^1 \pm iJ^2] = iJ^2 \pm i(-iJ^1) = \pm(J^1 \pm iJ^2)$). For $w \in W_m$: $J^3J^\pm w = J^\pm J^3w \pm J^\pm w = (m \pm 1)J^\pm w$, so $J^\pm w \in W_{m\pm1}$ (possibly $0$).
>
> **7. Part 3.** If $W$ is irreducible, $r = 1$ in step 2 and $W \cong V_j$; by step 3 its weights are $j, j-1, \dots, -j$, each once.
>
> **What the proof shows**
> - Half-integrality of the weights and the shift by one are algebraic consequences of the commutation relations and finite dimension; diagonalizability of $J^3$ is not, it needs complete reducibility (in the non-semisimple world a $2\times2$ Jordan block would be allowed).
> - ⚑ By-product: complete reducibility of $\mathfrak{sl}(2, \mathbb C)$-representations is borrowed from the compact group $SU(2)$ (Weyl's trick); the same mechanism gives it for the Lorentz algebra, two copies of $\mathfrak{sl}(2, \mathbb C)$ → [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]].
> - Used next: Theorem §CB.6.4 counts the pieces by their weights.

^pf-cb-6-3

*Uses:* [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-4|Theorem §CB.2.4]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-15|Theorem §CB.3.15]], [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-6-1|Def. §CB.6.1]], [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-6-2|Def. §CB.6.2]], [[§6 Dimension#^ladr-2-43|LADR Thm. 2.43]]

The highest-weight classification, proved in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]] (two routes):

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6]]

> [!theorem] Theorem §CB.6.4: Weight Multiplicities Determine a Representation
> Two finite-dimensional representations of $\mathfrak{sl}(2, \mathbb C)$ are equivalent iff their weight multiplicities agree. With $n_m = \dim W_m$, the number of summands $V_j$ in $W$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-3|Theorem §CB.6.3]]) is $n_j - n_{j+1}$.
>
> *Source: the counting argument of [[§B6.3 Addition of Angular Momenta#^der-b6-3-2|QM Derivation §B6.3.2]], step 2 ($n(m) = \sum_{j \ge |m|}N_j$, hence $N_j = n(j) - n(j+1)$; from the user's series, Part IV, §15, and Greensite §14.1), run on the decomposition of Theorem §CB.6.3 instead of on Hermitian multiplets · P. Woit, Quantum Theory, Groups and Representations, §8.1 (representations are determined by their weights restricted to the circle subgroup), §9.4.1 (the same bookkeeping by highest weights)*

^thm-cb-6-4

> [!proof]- Proof
> *QM's "staircase" count (Derivation §B6.3.2, step 2), with the multiplets supplied by complete reducibility (Theorem §CB.6.3) instead of by Hermitian operators.*
>
> **1. Equivalent representations have the same multiplicities.** Let $S : W \to W'$ be an invertible intertwiner ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-1|Def. §CB.3.1]]). It commutes with $J^3$, so for $w \in W_m$, $J^3Sw = SJ^3w = mSw$: $S(W_m) \subset W'_m$, and likewise $S^{-1}(W'_m) \subset W_m$. So $S$ maps $W_m$ onto $W'_m$ and $\dim W_m = \dim W'_m$.
>
> **2. Multiplicities of a sum.** By Theorem §CB.6.3, $W \cong \bigoplus_ka_kV_k$ ($a_k$ copies of $V_k$, $k \in \frac12\mathbb Z_{\ge0}$), and $V_k$ has the weight $m$ exactly once if $|m| \le k$ and $k - m \in \mathbb Z$, and not otherwise (Theorem §CB.6.3, 3). Weight spaces of a direct sum are the sums of the weight spaces of the summands, so
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
> This is QM Derivation §B6.3.2, step 2, with $N_j = a_j$. In particular the numbers $a_j$ do not depend on the chosen decomposition.
>
> **4. Equal multiplicities give equivalent representations.** If $W$ and $W'$ have the same $n_m$ for all $m$, step 3 gives $a_j = a'_j$ for all $j$; choose equivalences $V_j \to V_j$ copy by copy and add them up: an invertible intertwiner $W \cong \bigoplus a_jV_j = \bigoplus a'_jV_j \cong W'$. With step 1, the equivalence holds iff the multiplicities agree.
>
> **What the proof shows**
> - The weight multiplicities are a complete invariant of finite-dimensional $\mathfrak{sl}(2, \mathbb C)$-representations, the analogue for this algebra of characters for finite groups (Woit §9.4.2 phrases it with characters $\operatorname{tr}e^{i\theta\cdot2J^3}$).
> - ⚑ By-product: the number of copies of each $V_j$ is independent of the decomposition chosen (step 3), so "the multiplicity of spin $j$ in $W$" is well defined.
> - Used next: the Clebsch–Gordan series (Theorem §CB.6.6) and $\operatorname{Sym}^{2j}\mathbb C^2$ (Theorem §CB.6.5, second route).

^pf-cb-6-4

*Uses:* [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-3|Theorem §CB.6.3]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-1|Def. §CB.3.1]], [[§B6.3 Addition of Angular Momenta#^der-b6-3-2|QM Derivation §B6.3.2]]

## Spin j as a symmetric power

The course realizes spin $j$ on polynomials of degree $2j$, and integrates to SU(2) and SO(3), in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7]]

![[§C3.1 Groups, Algebras and Representations of Rotations#^rem-c3-1-6]]

> [!theorem] Theorem §CB.6.5: Spin j Is the Symmetric Power Sym²ʲℂ²
> For $j \in \frac12\mathbb Z_{\ge0}$, the restriction of $D^{\otimes2j}$ ($D$ the defining representation of $SU(2)$ or $SL(2, \mathbb C)$ on $\mathbb C^2$, [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-1|Def. §CB.4.1]]) to $\operatorname{Sym}^{2j}\mathbb C^2$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-11|Def. §CB.4.11]]) is irreducible and equivalent to $V_j$. The identification with homogeneous polynomials of degree $2j$, $P(z) = \psi_{a_1\cdots a_{2j}}z_{a_1}\cdots z_{a_{2j}}$, is an equivalence with the polynomial realization of [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]]; and $-\mathbb 1$ acts as $(-1)^{2j}$.
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §8.2 (the spin-$\frac n2$ representation on homogeneous polynomials of degree $n$ in $z_1, z_2$), §9.6, eq. (9.4) (symmetric tensors correspond to polynomials, $v_j^n \leftrightarrow v_j\otimes\cdots\otimes v_j$) and §9.4.3 ($V^N$ inside $(V^1)^{\otimes N}$ "giving an alternative to the construction using homogeneous polynomials") · irreducibility and the identification with $V_j$: [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]], Derivation, steps 1–6 (from the user's PHY 513 notes, Ch. 7 §7.2) · the slot picture: [[§C3.1 Groups, Algebras and Representations of Rotations#^rem-c3-1-6|§C3.1, Remark: Spin j is 2j symmetrized spin-½ slots]]*

^thm-cb-6-5

> [!proof]- Proof
> *Woit's two descriptions of spin $j$ — homogeneous polynomials (§8.2) and the symmetric part of $2j$ spinor slots (§9.4.3, §9.6) — identified explicitly; irreducibility is then the polynomial result of Theorem §C3.1.7. Steps 1–2 are stated for $\mathbb C^n$ and degree $k$; they are reused for $\mathbb C^3$ in Theorem §CB.6.8.*
>
> **1. Symmetric tensors are polynomials (Woit (9.4)).** For $\psi \in \operatorname{Sym}^k\mathbb C^n$ put $\Phi(\psi)(z) = \sum_{a_1, \dots, a_k}\psi_{a_1\cdots a_k}z_{a_1}\cdots z_{a_k}$, a homogeneous polynomial of degree $k$; $\Phi$ is linear. Group the index tuples by their type $\alpha = (\alpha_1, \dots, \alpha_n)$, $\alpha_i$ = the number of entries equal to $i$, $|\alpha| = k$. All tuples of type $\alpha$ give the monomial $z^\alpha = z_1^{\alpha_1}\cdots z_n^{\alpha_n}$ and, $\psi$ being symmetric ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-11|Def. §CB.4.11]]), the same component $\psi_\alpha$; there are $\frac{k!}{\alpha_1!\cdots\alpha_n!}$ of them. So
>
> $$
> \Phi(\psi)(z) = \sum_{|\alpha| = k}\frac{k!}{\alpha!}\,\psi_\alpha\,z^\alpha, \qquad \alpha! = \alpha_1!\cdots\alpha_n! .
> $$
>
> The monomials are linearly independent, so $\Phi(\psi) = 0$ forces every $\psi_\alpha = 0$, i.e. $\psi = 0$ (a symmetric tensor is determined by one component per type). Every monomial is reached: $z^\alpha = \Phi(\psi)$ for the symmetric $\psi$ with components $\frac{\alpha!}{k!}$ on the tuples of type $\alpha$ and $0$ elsewhere. $\Phi$ is a linear bijection onto the homogeneous polynomials of degree $k$ (both of dimension $\binom{n+k-1}k$, [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-13|Theorem §CB.4.13]], 1).
>
> **2. Φ is equivariant.** For a matrix $U$, $D^{\otimes k}(U)$ acts on components by $(U^{\otimes k}\psi)_{a_1\cdots a_k} = U_{a_1b_1}\cdots U_{a_kb_k}\psi_{b_1\cdots b_k}$ (one factor per slot, [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-1|Def. §CB.4.1]]). Then, summing first over the $a$'s,
>
> $$
> \Phi(U^{\otimes k}\psi)(z) = \psi_{b_1\cdots b_k}\bigl(U_{a_1b_1}z_{a_1}\bigr)\cdots\bigl(U_{a_kb_k}z_{a_k}\bigr) = \psi_{b_1\cdots b_k}(U^{\mathsf T}z)_{b_1}\cdots(U^{\mathsf T}z)_{b_k} = \Phi(\psi)(U^{\mathsf T}z) .
> $$
>
> The right side is the polynomial action $(D(U)P)(z) = P(U^{\mathsf T}z)$ of [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]]. And $\operatorname{Sym}^k\mathbb C^n$ is invariant under $D^{\otimes k}$ (Theorem §CB.4.13, 1), so $\Phi$ is an equivalence of representations.
>
> **3. n = 2, k = 2j: irreducible and equal to $V_j$.** By Theorem §C3.1.7, Derivation, steps 1–5, the polynomial representation on degree-$2j$ polynomials is irreducible under $SU(2)$ and its algebra representation is $D^{(j)} = V_j$. By step 2 the same holds for $\operatorname{Sym}^{2j}\mathbb C^2$. For $SL(2, \mathbb C)$ the formula $P \mapsto P(A^{\mathsf T}z)$ is the same ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], 1); a subspace invariant under $SL(2, \mathbb C)$ is invariant under its subgroup $SU(2)$, so it is irreducible too, and its differential $X \mapsto \sum_{a,b}X_{ba}z_b\partial_a$ (Derivation §C3.1.7, step 3, valid for every complex $2\times2$ matrix) is complex-linear in $X \in \mathfrak{sl}(2, \mathbb C)$, the complex-linear extension of the $\mathfrak{su}(2)$-representation $V_j$.
>
> **4. Second route: weights (Theorem §CB.6.4).** $J^3$ acts by $\frac12(z_1\partial_1 - z_2\partial_2)$ (Derivation §C3.1.7, step 4), so $z_1^{a}z_2^{b}$, $a + b = 2j$, has weight $\frac12(a - b) = a - j$. As $a$ runs over $0, \dots, 2j$ each $m \in \{-j, \dots, j\}$ occurs once: $n_m = 1$ for $|m| \le j$, $m - j \in \mathbb Z$, and $0$ otherwise. By [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-4|Theorem §CB.6.4]] the number of copies of $V_k$ is $n_k - n_{k+1}$, which is $1$ for $k = j$ and $0$ for every other $k$: the representation is $V_j$.
>
> **5. The element −1.** $D^{\otimes2j}(-\mathbb 1) = (-\mathbb 1)^{\otimes2j} = (-1)^{2j}\mathbb 1$: each of the $2j$ slots contributes a factor $-1$ (Derivation §C3.1.7, step 6, in polynomial form: $P(-z) = (-1)^{2j}P(z)$).
>
> **What the proof shows**
> - Spin $j$ is literally $2j$ spin-½ slots, symmetrized: the index picture of [[§C3.1 Groups, Algebras and Representations of Rotations#^rem-c3-1-6|§C3.1, Remark: Spin j is 2j symmetrized spin-½ slots]] is now a theorem, with $\Phi$ the dictionary between the tensor and the polynomial pictures.
> - ⚑ By-product: the sign $(-1)^{2j}$ of a $2\pi$ rotation counts spinor slots; integer spin has an even number of them, which is why it descends to $SO(3)$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-7|Theorem §CB.6.7]]).
> - The same construction for $SL(2, \mathbb C)$ with two kinds of slot gives $(j_+, j_-) \cong \operatorname{Sym}^{2j_+}\mathbb C^2\otimes\operatorname{Sym}^{2j_-}\bar{\mathbb C}^2$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]] realizes the second factor with the matrices $(\lambda^\dagger)^{-1}$, equivalent to $\bar\lambda$; dotted indices, [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-16|Theorem §CB.4.16]]).

^pf-cb-6-5

*Uses:* [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-1|Def. §CB.4.1]], [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-11|Def. §CB.4.11]], [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-13|Theorem §CB.4.13]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-4|Theorem §CB.6.4]]

## The Clebsch–Gordan series

> [!theorem] Theorem §CB.6.6: Clebsch–Gordan Series
> For $j_1, j_2 \in \frac12\mathbb Z_{\ge0}$, as representations of $\mathfrak{sl}(2, \mathbb C)$, $SU(2)$ or $SL(2, \mathbb C)$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-1|Def. §CB.4.1]]),
>
> $$
> V_{j_1}\otimes V_{j_2} \cong \bigoplus_{j = |j_1 - j_2|}^{j_1 + j_2}V_j \qquad (j \text{ in integer steps}) .
> $$
>
> *Source: the home of the series is Quantum Mechanics: [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]] (block form of $\mathscr D^{(j_1)}\otimes\mathscr D^{(j_2)}$) with the count of [[§B6.3 Addition of Angular Momenta#^thm-b6-3-2|QM Theorem §B6.3.2]] (Derivation, step 2), both for Hermitian angular momenta on inner-product spaces · P. Woit, Quantum Theory, Groups and Representations, §9.4.1 (Theorem 9.1, outline by highest weights) and §9.4.2 (proof by characters) · what is new here — no inner product, and the groups $SU(2)$, $SL(2, \mathbb C)$ — written here*

^thm-cb-6-6

> [!proof]- Proof
> *The count is QM's (one home: QM Derivation §B6.3.2, step 2, linked, not repeated). What is added: the decomposition needs no inner product (it uses Theorem §CB.6.4 instead of Hermitian multiplets), and it holds for the groups $SU(2)$ and $SL(2, \mathbb C)$.*
>
> **1. Weights add.** Let $e_{m_1}$, $f_{m_2}$ be the weight bases of $V_{j_1}$, $V_{j_2}$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-3|Theorem §CB.6.3]], 3). On $V_{j_1}\otimes V_{j_2}$ the generator $J^3$ acts by $J^3\otimes\mathbb 1 + \mathbb 1\otimes J^3$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-3|Theorem §CB.4.3]]), so
>
> $$
> J^3(e_{m_1}\otimes f_{m_2}) = (m_1 + m_2)\,e_{m_1}\otimes f_{m_2} ,
> $$
>
> and the $e_{m_1}\otimes f_{m_2}$ are a basis ([[§38 Tensor Products#^ladr-9-74|LADR Thm. 9.74]]). The multiplicity $n(m)$ of the weight $m$ is the number of pairs $(m_1, m_2)$, $|m_1| \le j_1$, $|m_2| \le j_2$, $m_1 + m_2 = m$.
>
> **2. The count (QM).** This is exactly the number $n(m)$ counted in [[§B6.3 Addition of Angular Momenta#^der-b6-3-2|QM Derivation §B6.3.2]], step 2, which finds $n(j) - n(j+1) = 1$ for $j = |j_1 - j_2|, |j_1 - j_2| + 1, \dots, j_1 + j_2$ and $0$ for the other $j \ge 0$ with $j - (j_1 + j_2) \in \mathbb Z$. For $j$ with $j - (j_1 + j_2) \notin \mathbb Z$, no $m_1 + m_2$ equals $j$, so $n(j) = n(j+1) = 0$.
>
> **3. The algebra.** $V_{j_1}\otimes V_{j_2}$ is a complex-linear representation of $\mathfrak{sl}(2, \mathbb C)$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-2|Def. §CB.4.2]]: a sum of complex-linear maps of $X$). By [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-4|Theorem §CB.6.4]] the number of copies of $V_j$ in it is $n(j) - n(j+1)$, which step 2 evaluated: $V_{j_1}\otimes V_{j_2} \cong \bigoplus_{j=|j_1-j_2|}^{j_1+j_2}V_j$ as $\mathfrak{sl}(2, \mathbb C)$-representations, hence (restriction, [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]]) as $\mathfrak{su}(2)$-representations. QM's proof used Hermitian $\mathbf J^2$, $J_z$ to produce the multiplets; here complete reducibility (Theorem §CB.6.3, 1) does it.
>
> **4. SU(2).** As group representations $V_j = \operatorname{Sym}^{2j}\mathbb C^2$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-5|Theorem §CB.6.5]]), and the differential of $V_{j_1}\otimes V_{j_2}$ is the tensor product of the differentials (Theorem §CB.4.3, 2). $SU(2)$ is connected ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|Theorem §C3.1.8]]), so two of its representations are equivalent iff their algebra representations are ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]], 2). Step 3 gives the equivalence of the algebra representations, hence of the group representations.
>
> **5. SL(2, ℂ).** The differentials of $\operatorname{Sym}^{2j}\mathbb C^2$ are complex-linear on $\mathfrak{sl}(2, \mathbb C)$ (Theorem §CB.6.5, step 3), so the differential of $V_{j_1}\otimes V_{j_2}$, and of $\bigoplus V_j$, is the complex-linear representation of step 3 viewed on the real Lie algebra of $SL(2, \mathbb C)$. The intertwiner of step 3 commutes with every $d(X)$, $X \in \mathfrak{sl}(2, \mathbb C)$, so it intertwines the algebra representations of $SL(2, \mathbb C)$. $SL(2, \mathbb C)$ is connected ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]), and Theorem §C3.1.2, 2 again gives the group equivalence.
>
> **What the proof shows**
> - The series is a statement about weights alone; inner products, Hermiticity and the Clebsch–Gordan coefficients are not needed for it (they are needed for the *unitary* change of basis, QM Definition §C7.1.1).
> - ⚑ By-product: because the argument never uses unitarity, it applies verbatim to each $\mathfrak{sl}(2, \mathbb C)$ factor of the complexified Lorentz algebra, where no invariant inner product exists → [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-7|Theorem §C3.3.7]].
> - Woit's character proof (§9.4.2) is the same count written as a product of generating functions: $\chi_{V_{j_1}}\chi_{V_{j_2}} = \sum_j\chi_{V_j}$.

^pf-cb-6-6

*Uses:* [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-2|Def. §CB.4.2]], [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-3|Theorem §CB.4.3]], [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-3|Theorem §CB.6.3]], [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-4|Theorem §CB.6.4]], [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-5|Theorem §CB.6.5]], [[§B6.3 Addition of Angular Momenta#^der-b6-3-2|QM Derivation §B6.3.2]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|Theorem §C3.1.8]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], [[§38 Tensor Products#^ladr-9-74|LADR Thm. 9.74]]

Quantum Mechanics proves the same series for Hermitian angular momenta, with the explicit Clebsch–Gordan coefficients, in [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients|QM §C7.1]]:

![[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2]]

## Descent to a quotient group

> [!theorem] Theorem §CB.6.7: Descent Lemma
> Let $p : \tilde G \to G$ be a surjective Lie group homomorphism ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-12|Def. §CB.1.12]]) that is a covering map (e.g. Theorem §CB.1.23), with kernel $N$. A representation $\tilde D$ of $\tilde G$ is of the form $\tilde D = D\circ p$ for a representation $D$ of $G$ iff $\tilde D(n) = \mathbb 1$ for all $n \in N$; then $D$ is unique, and $D$ is irreducible iff $\tilde D$ is. Instances: $SU(2) \to SO(3)$ and $SL(2, \mathbb C) \to SO^+(1,3)$, $N = \{\pm\mathbb 1\}$, where the condition is $\tilde D(-\mathbb 1) = \mathbb 1$.
>
> *Source: [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]] (the group part) · written here*

^thm-cb-6-7

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

^pf-cb-6-7

> [!theorem] Theorem §CB.6.8: Integer Spin Is Built from Vectors
> 1. $V_1$ is equivalent to the complexified vector representation of $SO(3)$ on $\mathbb C^3$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-22|Def. §CB.2.22]]).
> 2. For every integer $l \ge 0$, $V_l$ is equivalent to the space of traceless symmetric tensors in $\operatorname{Sym}^l\mathbb C^3$, a subrepresentation of $(\mathbb C^3)^{\otimes l}$. So every representation of $SO(3)$ is contained in a sum of tensor powers of the vector representation.
>
> *Source: B. C. Hall, Quantum Theory for Mathematicians, §17.6: Def. 17.11 and Thm. 17.12 (the harmonic polynomials of degree $l$ on $\mathbb R^3$ form an irreducible representation of $SO(3)$ of dimension $2l + 1$), with Lemma 17.13, Cor. 17.14 ($\Delta : P_l \to P_{l-2}$ is onto, via an inner product with $\langle p, \partial_jq\rangle = \langle x_jp, q\rangle$), Lemma 17.16 (the highest weight vector $(x_1 + ix_2)^l$) and Cor. 17.17 · symmetric tensors as polynomials: [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-5|Theorem §CB.6.5]], Proof, steps 1–2 (P. Woit, §9.6, eq. (9.4)) · part 1 also: [[§C3.1 Groups, Algebras and Representations of Rotations#^ex-c3-1-2|Example §C3.1.2]] (the user's PHY 513 notes, Ch. 7 §7.2, four-vector example)*

^thm-cb-6-8

> [!proof]- Proof
> *Hall's proof of Thm. 17.12 (points 1–2), with two changes: harmonic polynomials are first identified with traceless symmetric tensors (steps 1–3), and Hall's analytic (Segal–Bargmann) inner product in Lemma 17.13 is replaced by the combinatorial one he mentions, for which the needed identity is checked on monomials (step 4).*
>
> **1. The traceless symmetric tensors form a subrepresentation.** $SO(3)$ acts on $\mathbb C^3$ by its real matrices (the complexified vector representation, [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-22|Def. §CB.2.22]]) and on $(\mathbb C^3)^{\otimes l}$ by $R^{\otimes l}$; $\operatorname{Sym}^l\mathbb C^3$ is invariant ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-13|Theorem §CB.4.13]], 1). For $l \ge 2$ define the trace $t : \operatorname{Sym}^l\mathbb C^3 \to \operatorname{Sym}^{l-2}\mathbb C^3$, $(tT)_{a_3\cdots a_l} = \sum_iT_{ii\,a_3\cdots a_l}$. It is an intertwiner: using $\sum_iR_{ib_1}R_{ib_2} = (R^{\mathsf T}R)_{b_1b_2} = \delta_{b_1b_2}$,
>
> $$
> \bigl(t\,R^{\otimes l}T\bigr)_{a_3\cdots a_l} = \sum_iR_{ib_1}R_{ib_2}R_{a_3b_3}\cdots R_{a_lb_l}T_{b_1b_2b_3\cdots b_l} = R_{a_3b_3}\cdots R_{a_lb_l}\sum_{b}T_{bb\,b_3\cdots b_l} = \bigl(R^{\otimes(l-2)}\,tT\bigr)_{a_3\cdots a_l} .
> $$
>
> So $S^0_l = \ker t$, the traceless symmetric tensors, is invariant ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-2|Theorem §CB.3.2]]). For $l = 0, 1$ there is no pair of slots to contract and $S^0_l = \operatorname{Sym}^l\mathbb C^3$.
>
> **2. To polynomials.** By Theorem §CB.6.5, Proof, steps 1–2 (with $n = 3$, $k = l$), $\Phi(T)(x) = \sum T_{a_1\cdots a_l}x_{a_1}\cdots x_{a_l}$ is a linear bijection of $\operatorname{Sym}^l\mathbb C^3$ onto the space $P_l$ of homogeneous complex polynomials of degree $l$ in $x \in \mathbb R^3$, and $\Phi(R^{\otimes l}T)(x) = \Phi(T)(R^{\mathsf T}x) = \Phi(T)(R^{-1}x)$: the action $(R\cdot p)(x) = p(R^{-1}x)$ that Hall uses.
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
> **5. $\dim H_l = 2l + 1$ (Hall, Cor. 17.14).** By step 4 the adjoint of $\Delta : P_l \to P_{l-2}$ is multiplication by $|x|^2 : P_{l-2} \to P_l$, which is injective ($|x|^2p = 0$ forces $p = 0$, a product of nonzero polynomials being nonzero). The orthogonal complement of the range of $\Delta$ is the null space of its adjoint ([[§23 Self-Adjoint and Normal Operators#^ladr-7-6|LADR Thm. 7.6]]), here $0$, so $\Delta$ is onto. With $\dim P_l = \binom{l+2}{l} = \frac{(l+2)(l+1)}2$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-13|Theorem §CB.4.13]], 1, and step 2) and the fundamental theorem of linear maps ([[§8 Null Spaces and Ranges#^ladr-3-21|LADR Thm. 3.21]]),
>
> $$
> \dim H_l = \dim P_l - \dim P_{l-2} = \frac{(l+2)(l+1)}2 - \frac{l(l-1)}2 = 2l + 1 \qquad (l \ge 2),
> $$
>
> and $\dim H_0 = 1$, $\dim H_1 = 3$ directly.
>
> **6. The generators as differential operators.** With $R_k(\theta) = e^{-i\theta J_k}$, $(J_k)_{lm} = -i\varepsilon_{klm}$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]]), $R_3(\theta)$ rotates the $(x_1, x_2)$ plane counterclockwise, and $R_3(\theta)^{-1}x = (x_1\cos\theta + x_2\sin\theta,\ -x_1\sin\theta + x_2\cos\theta,\ x_3)$. The generator on polynomials is $D(J_k) = i\frac{d}{d\theta}\bigl(R_k(\theta)\cdot p\bigr)\big|_{\theta=0}$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]], 1, physicists' form), and by the chain rule $\frac{d}{d\theta}p(R_3(\theta)^{-1}x)\big|_0 = x_2\partial_1p - x_1\partial_2p$. The same computation with $R_1(\theta)^{-1}x = (x_1,\ x_2\cos\theta + x_3\sin\theta,\ -x_2\sin\theta + x_3\cos\theta)$ and $R_2(\theta)^{-1}x = (x_1\cos\theta - x_3\sin\theta,\ x_2,\ x_1\sin\theta + x_3\cos\theta)$ gives
>
> $$
> D(J_1) = i(x_3\partial_2 - x_2\partial_3), \qquad D(J_2) = i(x_1\partial_3 - x_3\partial_1), \qquad D(J_3) = i(x_2\partial_1 - x_1\partial_2),
> $$
>
> Hall's $L_k$.
>
> **7. A highest weight vector (Hall, Lemma 17.16).** Let $p_l = (x_1 + ix_2)^l$, $z = x_1 + ix_2$: $\partial_1p_l = lz^{l-1}$, $\partial_2p_l = ilz^{l-1}$, $\partial_3p_l = 0$. Harmonic: $\partial_1^2p_l + \partial_2^2p_l = l(l-1)z^{l-2} + i^2l(l-1)z^{l-2} = 0$. Weight: $D(J_3)p_l = i(x_2 - ix_1)\,lz^{l-1} = i(-i)(x_1 + ix_2)\,lz^{l-1} = l\,p_l$. Raising: $D(J^+) = D(J_1) + iD(J_2) = i(x_3\partial_2 - x_2\partial_3) - (x_1\partial_3 - x_3\partial_1)$, and on $p_l$ the $\partial_3$ terms vanish: $D(J^+)p_l = ix_3\cdot ilz^{l-1} + x_3\cdot lz^{l-1} = -x_3lz^{l-1} + x_3lz^{l-1} = 0$.
>
> **8. Irreducible of spin l (Hall, Cor. 17.17).** $H_l$ is invariant (step 3 and step 1). By [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]], 1, the vectors $D(J^-)^kp_l$, $k = 0, \dots, 2l$, span an irreducible invariant subspace of dimension $2l + 1$ with highest weight $l$, inside $H_l$; by step 5 it is all of $H_l$. So $H_l$ is irreducible and its algebra representation is $V_l = D^{(l)}$ (Theorem §C3.1.6, 2). $SO(3)$ is connected ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|Theorem §C3.1.8]], 2), so as a group representation $H_l$ is equivalent to the spin-$l$ representation of $SO(3)$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]], 2; equivalence from the algebra, [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]], 2). With step 3, $S^0_l \cong H_l \cong V_l$: part 2.
>
> **9. Part 1.** For $l = 1$, $S^0_1 = \mathbb C^3$ (step 1), so $V_1$ is the complexified vector representation; Example §C3.1.2 finds the same by computing the weights $1, 0, -1$ on $\mp(e_1 \pm ie_2)/\sqrt2$, $e_3$.
>
> **10. Every representation of SO(3).** A finite-dimensional representation of $SO(3)$ is a direct sum of $V_{l_k}$ with integer $l_k$ (Theorem §C3.1.7, 3), and $V_{l_k} \cong S^0_{l_k} \subset (\mathbb C^3)^{\otimes l_k}$; so it is equivalent to a subrepresentation of $\bigoplus_k(\mathbb C^3)^{\otimes l_k}$.
>
> **What the proof shows**
> - Integer spin needs no spinors: spin $l$ is the traceless symmetric part of $l$ vector slots, equivalently the harmonic polynomials of degree $l$, whose restrictions to the sphere are the spherical harmonics $Y_l^m$ (Hall, Thm. 17.12, points 3–4).
> - ⚑ By-product: $\operatorname{Sym}^l\mathbb C^3 = S^0_l\oplus|x|^2\operatorname{Sym}^{l-2}\mathbb C^3$ (step 5: the range of $|x|^2$ is the orthogonal complement of $\ker\Delta$), i.e. $\operatorname{Sym}^lV_1 \cong V_l\oplus V_{l-2}\oplus V_{l-4}\oplus\cdots$ — each trace removed is a lower spin (Hall, Cor. 17.15).
> - Half-integer spin is exactly what tensor powers of the vector representation cannot reach ($-\mathbb 1 \in SU(2)$ acts trivially on them); the spinor representations of §CB.9 fill the gap, and the TA's theorem (§CB.10, §CB.12) says spinor ⊗ tensor reaches everything.

^pf-cb-6-8

*Uses:* [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-22|Def. §CB.2.22]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-2|Theorem §CB.3.2]], [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-13|Theorem §CB.4.13]], [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-5|Theorem §CB.6.5]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|Theorem §C3.1.8]], [[§C3.1 Groups, Algebras and Representations of Rotations#^ex-c3-1-2|Example §C3.1.2]], [[§23 Self-Adjoint and Normal Operators#^ladr-7-6|LADR Thm. 7.6]], [[§8 Null Spaces and Ranges#^ladr-3-21|LADR Thm. 3.21]]

The topology behind the descent, proved in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8]]

> [!remark]- Connections
> - Theorem §CB.6.7 is the single mechanism behind three course theorems: integer spin integrates to SO(3) ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]]), integer $(j_+, j_-)$ to $SO^+(1,3)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]), and the general tensor/spinor split ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-6|Theorem §C3.3.6]]).
> - The Clebsch–Gordan series of Theorem §CB.6.6 is used copy by copy for the Lorentz group ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-7|Theorem §C3.3.7]]) and in the 3D and 4D versions of the TA's theorem (Theorem §CB.10.6, Theorem §CB.12.9).
> - **Used in**: Definitions §CB.6.1–§CB.6.2, Theorem §CB.6.3 — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-5|Theorem §C3.3.5]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]] (step 4); Theorem §CB.6.5 — [[§C3.1 Groups, Algebras and Representations of Rotations#^rem-c3-1-6|§C3.1, Remark: Spin j is 2j symmetrized spin-½ slots]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]; Theorem §CB.6.6 — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-5|Theorem §C3.3.5]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-7|Theorem §C3.3.7]], [[§C3.1 Groups, Algebras and Representations of Rotations#^ex-c3-1-2|Example §C3.1.2]]; Theorem §CB.6.7 — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-6|Theorem §C3.3.6]]; Theorem §CB.6.8 — [[§C3.1 Groups, Algebras and Representations of Rotations#^ex-c3-1-2|Example §C3.1.2]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-8|Theorem §C3.6.8]].
