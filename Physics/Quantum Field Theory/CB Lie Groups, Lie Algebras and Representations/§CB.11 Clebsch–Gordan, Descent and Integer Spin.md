---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.11
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.12 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules]] →

*Sources: Quantum Mechanics §B6.3, §C7.1 · P. Woit, Quantum Theory, Groups and Representations, §§9.4, 9.6 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · B. C. Hall, Quantum Theory for Mathematicians, §17.6 · Group Theory (493) and Topology (590), for the descent lemma · the user's PHY 513 notes, Ch. 7 §7.2 (the four-vector example) · the rest written here.*

How do two representations of $SU(2)$ multiply, which representations of a covering group are representations of the quotient, and how is integer spin built from vectors? [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers|§CB.10]] classified the irreducible representations of $\mathfrak{sl}(2, \mathbb C)$ by highest weight ([[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-6|Theorem §CB.10.6]]), showed that the weight multiplicities determine a representation ([[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-7|Theorem §CB.10.7]]) and realized spin $j$ as $\operatorname{Sym}^{2j}\mathbb C^2$ ([[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-15|Theorem §CB.10.15]]). This section uses them for the Clebsch–Gordan series as a statement about tensor products, with no inner product (Quantum Mechanics adds angular momenta in [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]]); for the descent lemma, which decides which representations of a covering group come from the quotient; and for the realization of every integer spin on traceless symmetric tensors of the vector representation. The Lorentz group uses all three in [[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)|§CB.18]], the three- and four-dimensional forms of the TA's theorem in [[§CB.16 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half|§CB.16]] and [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.19]].

## The Clebsch–Gordan series

The count of weights in a tensor product, first done in Quantum Mechanics for addition of angular momenta and restated here, since the Clebsch–Gordan series below rests on it:

> [!theorem] Lemma §CB.11.1: The Weight Count of a Tensor Product
> For $j_1, j_2 \in \frac12\mathbb Z_{\ge0}$ and $m$ with $m - (j_1 + j_2) \in \mathbb Z$, let $n(m)$ be the number of pairs $(m_1, m_2)$ with $m_i \in \{-j_i, -j_i + 1, \dots, j_i\}$ and $m_1 + m_2 = m$. Then $n(j) - n(j+1) = 1$ for $j = |j_1 - j_2|, |j_1 - j_2| + 1, \dots, j_1 + j_2$, and $n(j) - n(j+1) = 0$ for the other $j \ge 0$ with $j - (j_1 + j_2) \in \mathbb Z$.
>
> *Source: Griffiths §4.4.3; Greensite §14.1, eqs. (14.50)–(14.56); the user's series, Part IV, §15 · the course's version: step 2 of [[§B6.3 Addition of Angular Momenta#^der-b6-3-2|QM Derivation §B6.3.2]], where the same count, $N_j = n(j) - n(j+1)$, gives the multiplicity of total angular momentum $j$*

^lem-cb-11-1

> [!proof]- Proof
> *Step 2 of QM Derivation §B6.3.2, the counting part, unchanged except that the multiplets are not used.*
>
> Take $j_1 \ge j_2$. For given $m \ge 0$, $m_2$ runs over $[-j_2, j_2]$ subject to $m_1 = m - m_2 \in [-j_1, j_1]$. If $m \le j_1 - j_2$, every $m_2$ is allowed: $n(m) = 2j_2 + 1$. If $j_1 - j_2 \le m \le j_1 + j_2$, the condition is $m_2 \ge m - j_1$, so $n(m) = j_1 + j_2 - m + 1$. Above $j_1 + j_2$, $n = 0$. Hence $n(j) - n(j+1) = (j_1 + j_2 - j + 1) - (j_1 + j_2 - j) = 1$ for $j_1 - j_2 \le j \le j_1 + j_2$ (at $j = j_1 + j_2$: $1 - 0$; at $j = j_1 - j_2$: $(2j_2 + 1) - 2j_2$), and $n(j) - n(j+1) = (2j_2 + 1) - (2j_2 + 1) = 0$ for $0 \le j < j_1 - j_2$ (all $j$ here differ from $j_1 + j_2$ by integers, like the $m$'s). For $j_1 < j_2$ exchange the roles.
>
> **What the proof shows**
> - The count uses only the ranges of $m_1$, $m_2$; no inner product and no operator enters, which is why the Clebsch–Gordan series holds for $\mathfrak{sl}(2, \mathbb C)$ and $SL(2, \mathbb C)$ as well.
> - Equivalence: this is the counting half of QM Derivation §B6.3.2, step 2; the other half there ($n(m) = \sum_{j \ge |m|}N_j$) is [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-7|Theorem §CB.10.7]] in CB.

^pf-cb-11-1

> [!theorem] Theorem §CB.11.2: Clebsch–Gordan Series
> For $j_1, j_2 \in \frac12\mathbb Z_{\ge0}$, as representations of $\mathfrak{sl}(2, \mathbb C)$, $SU(2)$ or $SL(2, \mathbb C)$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-1|Def. §CB.8.1]]),
>
> $$
> V_{j_1}\otimes V_{j_2} \cong \bigoplus_{j = |j_1 - j_2|}^{j_1 + j_2}V_j \qquad (j \text{ in integer steps}) .
> $$
>
> *Source: the home of the series is Quantum Mechanics: [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]] (block form of $\mathscr D^{(j_1)}\otimes\mathscr D^{(j_2)}$) with the count of [[§B6.3 Addition of Angular Momenta#^thm-b6-3-2|QM Theorem §B6.3.2]] (Derivation, step 2), both for Hermitian angular momenta on inner-product spaces · P. Woit, Quantum Theory, Groups and Representations, §9.4.1 (Theorem 9.1, outline by highest weights) and §9.4.2 (proof by characters) · what is new here — no inner product, and the groups $SU(2)$, $SL(2, \mathbb C)$ — written here*

^thm-cb-11-2

> [!proof]- Proof
> *The count is QM's (QM Derivation §B6.3.2, step 2), restated in CB as Lemma §CB.11.1. What is added: the decomposition needs no inner product (it uses Theorem §CB.10.7 instead of Hermitian multiplets), and it holds for the groups $SU(2)$ and $SL(2, \mathbb C)$.*
>
> **1. Weights add.** Let $e_{m_1}$, $f_{m_2}$ be the weight bases of $V_{j_1}$, $V_{j_2}$ ([[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-6|Theorem §CB.10.6]], 3). On $V_{j_1}\otimes V_{j_2}$ the generator $J^3$ acts by $J^3\otimes\mathbb 1 + \mathbb 1\otimes J^3$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-3|Theorem §CB.8.3]]), so
>
> $$
> J^3(e_{m_1}\otimes f_{m_2}) = (m_1 + m_2)\,e_{m_1}\otimes f_{m_2} ,
> $$
>
> and the $e_{m_1}\otimes f_{m_2}$ are a basis ([[§38 Tensor Products#^ladr-9-74|LADR Thm. 9.74]]). The multiplicity $n(m)$ of the weight $m$ is the number of pairs $(m_1, m_2)$, $|m_1| \le j_1$, $|m_2| \le j_2$, $m_1 + m_2 = m$.
>
> **2. The count.** This is exactly the number $n(m)$ counted in [[§CB.11 Clebsch–Gordan, Descent and Integer Spin#^lem-cb-11-1|Lemma §CB.11.1]], which finds $n(j) - n(j+1) = 1$ for $j = |j_1 - j_2|, |j_1 - j_2| + 1, \dots, j_1 + j_2$ and $0$ for the other $j \ge 0$ with $j - (j_1 + j_2) \in \mathbb Z$. For $j$ with $j - (j_1 + j_2) \notin \mathbb Z$, no $m_1 + m_2$ equals $j$, so $n(j) = n(j+1) = 0$.
>
> **3. The algebra.** $V_{j_1}\otimes V_{j_2}$ is a complex-linear representation of $\mathfrak{sl}(2, \mathbb C)$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-2|Def. §CB.8.2]]: a sum of complex-linear maps of $X$). By [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-7|Theorem §CB.10.7]] the number of copies of $V_j$ in it is $n(j) - n(j+1)$, which step 2 evaluated: $V_{j_1}\otimes V_{j_2} \cong \bigoplus_{j=|j_1-j_2|}^{j_1+j_2}V_j$ as $\mathfrak{sl}(2, \mathbb C)$-representations, hence (restriction, [[§CB.4 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-4-10|Theorem §CB.4.10]]) as $\mathfrak{su}(2)$-representations. QM's proof used Hermitian $\mathbf J^2$, $J_z$ to produce the multiplets; here complete reducibility (Theorem §CB.10.6, 1) does it.
>
> **4. SU(2).** As group representations $V_j = \operatorname{Sym}^{2j}\mathbb C^2$ ([[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-15|Theorem §CB.10.15]]), and the differential of $V_{j_1}\otimes V_{j_2}$ is the tensor product of the differentials (Theorem §CB.8.3, 2). $SU(2)$ is connected ([[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-11|Theorem §CB.10.11]]), so two of its representations are equivalent iff their algebra representations are ([[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-10|Theorem §CB.3.10]], 2). Step 3 gives the equivalence of the algebra representations, hence of the group representations.
>
> **5. SL(2, ℂ).** The differentials of $\operatorname{Sym}^{2j}\mathbb C^2$ are complex-linear on $\mathfrak{sl}(2, \mathbb C)$ (Theorem §CB.10.15, step 3), so the differential of $V_{j_1}\otimes V_{j_2}$, and of $\bigoplus V_j$, is the complex-linear representation of step 3 viewed on the real Lie algebra of $SL(2, \mathbb C)$. The intertwiner of step 3 commutes with every $d(X)$, $X \in \mathfrak{sl}(2, \mathbb C)$, so it intertwines the algebra representations of $SL(2, \mathbb C)$. $SL(2, \mathbb C)$ is connected ([[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-12|Theorem §CB.10.12]]), and Theorem §CB.3.10, 2 again gives the group equivalence.
>
> **What the proof shows**
> - The series is a statement about weights alone; inner products, Hermiticity and the Clebsch–Gordan coefficients are not needed for it (they are needed for the *unitary* change of basis, QM Definition §C7.1.1).
> - ⚑ By-product: because the argument never uses unitarity, it applies verbatim to each $\mathfrak{sl}(2, \mathbb C)$ factor of the complexified Lorentz algebra, where no invariant inner product exists → [[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-18-12|Theorem §CB.18.12]].
> - Woit's character proof (§9.4.2) is the same count written as a product of generating functions: $\chi_{V_{j_1}}\chi_{V_{j_2}} = \sum_j\chi_{V_j}$.

^pf-cb-11-2

*Uses:* [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-2|Def. §CB.8.2]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-3|Theorem §CB.8.3]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-6|Theorem §CB.10.6]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-7|Theorem §CB.10.7]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-15|Theorem §CB.10.15]], [[§CB.11 Clebsch–Gordan, Descent and Integer Spin#^lem-cb-11-1|Lemma §CB.11.1]], [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-10|Theorem §CB.3.10]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-11|Theorem §CB.10.11]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-12|Theorem §CB.10.12]], [[§38 Tensor Products#^ladr-9-74|LADR Thm. 9.74]]

Quantum Mechanics proves the same series for Hermitian angular momenta, with the explicit Clebsch–Gordan coefficients, in [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients|QM §C7.1]] ([[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]]); Theorem §CB.11.2 is the same statement without an inner product.

## Descent to a quotient group

> [!theorem] Theorem §CB.11.3: Descent Lemma
> Let $p : \tilde G \to G$ be a surjective Lie group homomorphism ([[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-3-1|Def. §CB.3.1]]) that is a covering map (e.g. Theorem §CB.3.20), with kernel $N$. A representation $\tilde D$ of $\tilde G$ is of the form $\tilde D = D\circ p$ for a representation $D$ of $G$ iff $\tilde D(n) = \mathbb 1$ for all $n \in N$; then $D$ is unique, and $D$ is irreducible iff $\tilde D$ is. Instances: $SU(2) \to SO(3)$ and $SL(2, \mathbb C) \to SO^+(1,3)$, $N = \{\pm\mathbb 1\}$, where the condition is $\tilde D(-\mathbb 1) = \mathbb 1$.
>
> *Source: [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]] (the group part) · written here*

^thm-cb-11-3

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

^pf-cb-11-3

*Uses:* [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-3-1|Def. §CB.3.1]], [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-3-6|Def. §CB.3.6]], [[§15 Homomorphisms#^def-15-3|493 Def. §15.3]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]], [[§31 Covering Spaces#^def-31-2|590 Def. §31.2]]

> [!theorem] Theorem §CB.11.4: Integer Spin Is Built from Vectors
> 1. $V_1$ is equivalent to the complexified vector representation of $SO(3)$ on $\mathbb C^3$ ([[§CB.4 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-4-17|Def. §CB.4.17]]).
> 2. For every integer $l \ge 0$, $V_l$ is equivalent to the space of traceless symmetric tensors in $\operatorname{Sym}^l\mathbb C^3$, a subrepresentation of $(\mathbb C^3)^{\otimes l}$. So every representation of $SO(3)$ is contained in a sum of tensor powers of the vector representation.
>
> *Source: B. C. Hall, Quantum Theory for Mathematicians, §17.6: Def. 17.11 and Thm. 17.12 (the harmonic polynomials of degree $l$ on $\mathbb R^3$ form an irreducible representation of $SO(3)$ of dimension $2l + 1$), with Lemma 17.13, Cor. 17.14 ($\Delta : P_l \to P_{l-2}$ is onto, via an inner product with $\langle p, \partial_jq\rangle = \langle x_jp, q\rangle$), Lemma 17.16 (the highest weight vector $(x_1 + ix_2)^l$) and Cor. 17.17 · symmetric tensors as polynomials: [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-15|Theorem §CB.10.15]], Proof, steps 1–2 (P. Woit, §9.6, eq. (9.4)) · part 1 also: [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^ex-c3-1-1|Example §C3.1.1]] (the user's PHY 513 notes, Ch. 7 §7.2, four-vector example)*

^thm-cb-11-4

> [!proof]- Proof
> *Hall's proof of Thm. 17.12 (points 1–2), with two changes: harmonic polynomials are first identified with traceless symmetric tensors (steps 1–3), and Hall's analytic (Segal–Bargmann) inner product in Lemma 17.13 is replaced by the combinatorial one he mentions, for which the needed identity is checked on monomials (step 4).*
>
> **1. The traceless symmetric tensors form a subrepresentation.** $SO(3)$ acts on $\mathbb C^3$ by its real matrices (the complexified vector representation, [[§CB.4 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-4-17|Def. §CB.4.17]]) and on $(\mathbb C^3)^{\otimes l}$ by $R^{\otimes l}$; $\operatorname{Sym}^l\mathbb C^3$ is invariant ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-13|Theorem §CB.8.13]], 1). For $l \ge 2$ define the trace $t : \operatorname{Sym}^l\mathbb C^3 \to \operatorname{Sym}^{l-2}\mathbb C^3$, $(tT)_{a_3\cdots a_l} = \sum_iT_{ii\,a_3\cdots a_l}$. It is an intertwiner: using $\sum_iR_{ib_1}R_{ib_2} = (R^{\mathsf T}R)_{b_1b_2} = \delta_{b_1b_2}$,
>
> $$
> \bigl(t\,R^{\otimes l}T\bigr)_{a_3\cdots a_l} = \sum_iR_{ib_1}R_{ib_2}R_{a_3b_3}\cdots R_{a_lb_l}T_{b_1b_2b_3\cdots b_l} = R_{a_3b_3}\cdots R_{a_lb_l}\sum_{b}T_{bb\,b_3\cdots b_l} = \bigl(R^{\otimes(l-2)}\,tT\bigr)_{a_3\cdots a_l} .
> $$
>
> So $S^0_l = \ker t$, the traceless symmetric tensors, is invariant ([[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-7-3|Theorem §CB.7.3]]). For $l = 0, 1$ there is no pair of slots to contract and $S^0_l = \operatorname{Sym}^l\mathbb C^3$.
>
> **2. To polynomials.** By Theorem §CB.10.15, Proof, steps 1–2 (with $n = 3$, $k = l$), $\Phi(T)(x) = \sum T_{a_1\cdots a_l}x_{a_1}\cdots x_{a_l}$ is a linear bijection of $\operatorname{Sym}^l\mathbb C^3$ onto the space $P_l$ of homogeneous complex polynomials of degree $l$ in $x \in \mathbb R^3$, and $\Phi(R^{\otimes l}T)(x) = \Phi(T)(R^{\mathsf T}x) = \Phi(T)(R^{-1}x)$: the action $(R\cdot p)(x) = p(R^{-1}x)$ that Hall uses.
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
> **5. $\dim H_l = 2l + 1$ (Hall, Cor. 17.14).** By step 4 the adjoint of $\Delta : P_l \to P_{l-2}$ is multiplication by $|x|^2 : P_{l-2} \to P_l$, which is injective ($|x|^2p = 0$ forces $p = 0$, a product of nonzero polynomials being nonzero). The orthogonal complement of the range of $\Delta$ is the null space of its adjoint ([[§23 Self-Adjoint and Normal Operators#^ladr-7-6|LADR Thm. 7.6]]), here $0$, so $\Delta$ is onto. With $\dim P_l = \binom{l+2}{l} = \frac{(l+2)(l+1)}2$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-13|Theorem §CB.8.13]], 1, and step 2) and the fundamental theorem of linear maps ([[§8 Null Spaces and Ranges#^ladr-3-21|LADR Thm. 3.21]]),
>
> $$
> \dim H_l = \dim P_l - \dim P_{l-2} = \frac{(l+2)(l+1)}2 - \frac{l(l-1)}2 = 2l + 1 \qquad (l \ge 2),
> $$
>
> and $\dim H_0 = 1$, $\dim H_1 = 3$ directly.
>
> **6. The generators as differential operators.** With $R_k(\theta) = e^{-i\theta J_k}$, $(J_k)_{lm} = -i\varepsilon_{klm}$ ([[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-4|Theorem §CB.2.4]]), $R_3(\theta)$ rotates the $(x_1, x_2)$ plane counterclockwise, and $R_3(\theta)^{-1}x = (x_1\cos\theta + x_2\sin\theta,\ -x_1\sin\theta + x_2\cos\theta,\ x_3)$. The generator on polynomials is $D(J_k) = i\frac{d}{d\theta}\bigl(R_k(\theta)\cdot p\bigr)\big|_{\theta=0}$ ([[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-10|Theorem §CB.3.10]], 1, physicists' form), and by the chain rule $\frac{d}{d\theta}p(R_3(\theta)^{-1}x)\big|_0 = x_2\partial_1p - x_1\partial_2p$. The same computation with $R_1(\theta)^{-1}x = (x_1,\ x_2\cos\theta + x_3\sin\theta,\ -x_2\sin\theta + x_3\cos\theta)$ and $R_2(\theta)^{-1}x = (x_1\cos\theta - x_3\sin\theta,\ x_2,\ x_1\sin\theta + x_3\cos\theta)$ gives
>
> $$
> D(J_1) = i(x_3\partial_2 - x_2\partial_3), \qquad D(J_2) = i(x_1\partial_3 - x_3\partial_1), \qquad D(J_3) = i(x_2\partial_1 - x_1\partial_2),
> $$
>
> Hall's $L_k$.
>
> **7. A highest weight vector (Hall, Lemma 17.16).** Let $p_l = (x_1 + ix_2)^l$, $z = x_1 + ix_2$: $\partial_1p_l = lz^{l-1}$, $\partial_2p_l = ilz^{l-1}$, $\partial_3p_l = 0$. Harmonic: $\partial_1^2p_l + \partial_2^2p_l = l(l-1)z^{l-2} + i^2l(l-1)z^{l-2} = 0$. Weight: $D(J_3)p_l = i(x_2 - ix_1)\,lz^{l-1} = i(-i)(x_1 + ix_2)\,lz^{l-1} = l\,p_l$. Raising: $D(J^+) = D(J_1) + iD(J_2) = i(x_3\partial_2 - x_2\partial_3) - (x_1\partial_3 - x_3\partial_1)$, and on $p_l$ the $\partial_3$ terms vanish: $D(J^+)p_l = ix_3\cdot ilz^{l-1} + x_3\cdot lz^{l-1} = -x_3lz^{l-1} + x_3lz^{l-1} = 0$.
>
> **8. Irreducible of spin l (Hall, Cor. 17.17).** $H_l$ is invariant (step 3 and step 1). By [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-3|Theorem §CB.10.3]], 1, the vectors $D(J^-)^kp_l$, $k = 0, \dots, 2l$, span an irreducible invariant subspace of dimension $2l + 1$ with highest weight $l$, inside $H_l$; by step 5 it is all of $H_l$. So $H_l$ is irreducible and its algebra representation is $V_l = D^{(l)}$ (Theorem §CB.10.3, 2). $SO(3)$ is connected ([[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-11|Theorem §CB.10.11]], 2), so as a group representation $H_l$ is equivalent to the spin-$l$ representation of $SO(3)$ ([[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-13|Theorem §CB.10.13]], 2; equivalence from the algebra, [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-10|Theorem §CB.3.10]], 2). With step 3, $S^0_l \cong H_l \cong V_l$: part 2.
>
> **9. Part 1.** For $l = 1$, $S^0_1 = \mathbb C^3$ (step 1), so $V_1$ is the complexified vector representation.
>
> **10. Every representation of SO(3).** A finite-dimensional representation of $SO(3)$ is a direct sum of $V_{l_k}$ with integer $l_k$ (Theorem §CB.10.13, 3), and $V_{l_k} \cong S^0_{l_k} \subset (\mathbb C^3)^{\otimes l_k}$; so it is equivalent to a subrepresentation of $\bigoplus_k(\mathbb C^3)^{\otimes l_k}$.
>
> **What the proof shows**
> - The course's computation of part 1: [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^ex-c3-1-1|Example §C3.1.1]] finds the same by computing the weights $1, 0, -1$ on $\mp(e_1 \pm ie_2)/\sqrt2$, $e_3$.
> - Integer spin needs no spinors: spin $l$ is the traceless symmetric part of $l$ vector slots, equivalently the harmonic polynomials of degree $l$, whose restrictions to the sphere are the spherical harmonics $Y_l^m$ (Hall, Thm. 17.12, points 3–4).
> - ⚑ By-product: $\operatorname{Sym}^l\mathbb C^3 = S^0_l\oplus|x|^2\operatorname{Sym}^{l-2}\mathbb C^3$ (step 5: the range of $|x|^2$ is the orthogonal complement of $\ker\Delta$), i.e. $\operatorname{Sym}^lV_1 \cong V_l\oplus V_{l-2}\oplus V_{l-4}\oplus\cdots$ — each trace removed is a lower spin (Hall, Cor. 17.15).
> - Half-integer spin is exactly what tensor powers of the vector representation cannot reach ($-\mathbb 1 \in SU(2)$ acts trivially on them); the spinor representations of §CB.15 fill the gap, and the TA's theorem (§CB.16, §CB.19) says spinor ⊗ tensor reaches everything.

^pf-cb-11-4

*Uses:* [[§CB.4 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-4-17|Def. §CB.4.17]], [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-7-3|Theorem §CB.7.3]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-13|Theorem §CB.8.13]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-15|Theorem §CB.10.15]], [[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-4|Theorem §CB.2.4]], [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-10|Theorem §CB.3.10]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-3|Theorem §CB.10.3]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-13|Theorem §CB.10.13]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-11|Theorem §CB.10.11]], [[§23 Self-Adjoint and Normal Operators#^ladr-7-6|LADR Thm. 7.6]], [[§8 Null Spaces and Ranges#^ladr-3-21|LADR Thm. 3.21]]

The topology behind the descent is [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-11|Theorem §CB.10.11]] in [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers|§CB.10]].

> [!remark]- Connections
> - Theorem §CB.11.3 is the single mechanism behind three course theorems: integer spin integrates to SO(3) ([[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-13|Theorem §CB.10.13]]), integer $(j_+, j_-)$ to $SO^+(1,3)$ ([[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-18-9|Theorem §CB.18.9]]), and the general tensor/spinor split ([[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-18-11|Theorem §CB.18.11]]).
> - The Clebsch–Gordan series of Theorem §CB.11.2 is used copy by copy for the Lorentz group ([[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-18-12|Theorem §CB.18.12]]) and in the 3D and 4D versions of the TA's theorem (Theorem §CB.16.6, Theorem §CB.19.16).
> - **Used in**: Lemma §CB.11.1 — [[§CB.11 Clebsch–Gordan, Descent and Integer Spin#^thm-cb-11-2|Theorem §CB.11.2]]; Theorem §CB.11.2 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (cited in [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^ex-c3-1-1|Example §C3.1.1]]), [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (cited in [[§C3.3 How Fields Transform under the Lorentz Group#^der-c3-3-7b|Derivation §C3.3.7, second route]]; Mathematical background), [[§CB.16 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-16-6|Theorem §CB.16.6]], [[§CB.17 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover|§CB.17]] (text), [[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-18-8|Theorem §CB.18.8]], [[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-18-12|Theorem §CB.18.12]], [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-15|Theorem §CB.19.15]], [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-16|Theorem §CB.19.16]]; Theorem §CB.11.3 — [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-15-23|Def. §CB.15.23]], [[§CB.16 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-16-6|Theorem §CB.16.6]], [[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-18-16|Theorem §CB.18.16]], [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-17|Theorem §CB.19.17]]; Theorem §CB.11.4 — [[§CB.16 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-16-6|Theorem §CB.16.6]], [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-17|Theorem §CB.19.17]].
