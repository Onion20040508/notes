---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.7
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.8 Hermitian Forms, Signature and Pseudo-Unitary Groups]] →

*Sources: Linear Algebra (LADR) §12 (duality), §36 (alternating forms), §38 (tensor products) · Relativity §B1.2, §B2.2 (invariant tensors) · Group Theory (493) §21 (the sign) · the user's PHY 513 notes, Ch. 1 §1.5, Ch. 7 §7.4.5–§7.4.6, Ch. 8 §8.2 · Yu Zhao-Huan, 量子场论讲义, §9.6.1 · P. Woit, Quantum Theory, Groups and Representations, §§4.2, 4.6.2, 9.1, 9.4, 16.1.1, 41.1 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · P. Etingof et al., Introduction to Representation Theory, §§2.1–2.2, 2.10 (arXiv:0901.0827) · K. E. Smith, Groups and their Representations, Ch. 4 §§2, 5.2 · S. Wadsley, Representation Theory (Cambridge lecture notes), Lectures 11–12 · H. K. Dreiner, H. E. Haber, S. P. Martin, Two-component spinor techniques (arXiv:0812.1594), §2.1 · the rest written here.*

How are new representations made from given ones, and what are index slots, dotted indices and invariant symbols in that language? The course has tensors as multilinear maps, index slots and the slot rule ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-9|Def. §CB.0.9]], [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^def-c3-1-1|Def. §C3.1.1]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-10|Theorem §CB.0.10]]); the Math vault has duals and tensor products of vector spaces ([[§12 Duality#^ladr-3-110|LADR Def. 3.110]], [[§38 Tensor Products#^ladr-9-71|LADR Def. 9.71]]). This section makes each operation on spaces an operation on representations — tensor product, outer tensor product, dual, complex conjugate, $\operatorname{Hom}$, symmetric and exterior powers — and identifies the invariant tensors ($g$, $\varepsilon^{\mu\nu\rho\sigma}$, $\varepsilon_{ab}$) as intertwiners. It builds on [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification|§CB.3]] (the conjugation of $\mathfrak g_{\mathbb C}$) and [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs|§CB.6]] (Burnside, Schur).

## Recalled: duals, tensors and index slots

The dual space and tensors as multilinear maps, defined in [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors|§CB.0]] (in the spacetime notation of [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]]); the tensor product of two spaces, defined in LADR:

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-7]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-9]]

![[§38 Tensor Products#^ladr-9-71]]

Index slots, the course's bookkeeping of which representation acts on which index, are physics notation, defined in [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^def-c3-1-1|Def. §C3.1.1]].

## Tensor products

> [!definition] Definition §CB.7.1: Tensor Product of Group Representations
> If $D_1$, $D_2$ are representations of a group $G$ on $W_1$, $W_2$, their **tensor product** is the representation of $G$ on $W_1\otimes W_2$ ([[§38 Tensor Products#^ladr-9-71|LADR Def. 9.71]]) with $(D_1\otimes D_2)(g)(w_1\otimes w_2) = D_1(g)w_1\otimes D_2(g)w_2$.
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §9.4 (Definition: tensor product representation of a group) · the user's PHY 513 notes, Ch. 7 §7.4.5*

^def-cb-7-1

> [!definition] Definition §CB.7.2: Tensor Product of Lie Algebra Representations
> If $d_1$, $d_2$ are representations of a Lie algebra $\mathfrak g$ on $W_1$, $W_2$, their **tensor product** is $(d_1\otimes d_2)(X) = d_1(X)\otimes\mathbb 1 + \mathbb 1\otimes d_2(X)$ on $W_1\otimes W_2$.
>
> *Source: Woit, §9.4 ($\pi'_{V\otimes W}(X) = \pi'_V(X)\otimes\mathbb 1_W + \mathbb 1_V\otimes\pi'_W(X)$)*

^def-cb-7-2

> [!theorem] Theorem §CB.7.3: The Differential of a Tensor Product Is the Leibniz Rule
> 1. Definitions §CB.7.1 and §CB.7.2 give representations.
> 2. If $d_i$ is the differential of $D_i$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]), then $d_1\otimes d_2$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-2|Def. §CB.7.2]]) is the differential of $D_1\otimes D_2$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-1|Def. §CB.7.1]]); equivalently $e^{d_1(X)\otimes\mathbb 1 + \mathbb 1\otimes d_2(X)} = e^{d_1(X)}\otimes e^{d_2(X)}$. In physicists' form, generators add: $D(T_a) = D_1(T_a)\otimes\mathbb 1 + \mathbb 1\otimes D_2(T_a)$.
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §9.4 (definition of the tensor product representation and the product-rule computation of its Lie algebra representation; https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the exponential identity and the bracket check: [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^der-c7-1-1|QM Derivation §C7.1.1]] · the tensor law: [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-14|Theorem §CB.0.14]]*

^thm-cb-7-3

> [!proof]- Proof
> *Woit's argument (§9.4), with the checks he leaves to the reader written out.*
>
> **1. $D_1\otimes D_2$ is a representation.** For each $g$, $(w_1, w_2) \mapsto D_1(g)w_1\otimes D_2(g)w_2$ is bilinear, so it defines a unique linear map of $W_1\otimes W_2$ ([[§38 Tensor Products#^ladr-9-79|LADR Thm. 9.79]]). On products,
>
> $$
> (D_1\otimes D_2)(g)\,(D_1\otimes D_2)(h)\,(w_1\otimes w_2) = D_1(g)D_1(h)w_1\otimes D_2(g)D_2(h)w_2 = D_1(gh)w_1\otimes D_2(gh)w_2 = (D_1\otimes D_2)(gh)\,(w_1\otimes w_2) ,
> $$
>
> and the products $e_i\otimes f_k$ of basis vectors are a basis of $W_1\otimes W_2$ ([[§38 Tensor Products#^ladr-9-74|LADR Thm. 9.74]]), so the two linear maps agree. $(D_1\otimes D_2)(\mathbb 1) = \mathbb 1\otimes\mathbb 1 = \mathbb 1$. In the basis $e_i\otimes f_k$ the matrix entries are $D_1(g)_{ij}D_2(g)_{kl}$, products of continuous functions of $g$: the map is continuous.
>
> **2. $d_1\otimes d_2$ is a Lie algebra representation.** It is real-linear in $X$. Write $A_X = d_1(X)\otimes\mathbb 1$, $B_X = \mathbb 1\otimes d_2(X)$ and expand the bracket into its four terms:
>
> $$
> [A_X + B_X, A_Y + B_Y] = [A_X, A_Y] + [A_X, B_Y] + [B_X, A_Y] + [B_X, B_Y] .
> $$
>
> First term: $(d_1(X)\otimes\mathbb 1)(d_1(Y)\otimes\mathbb 1) - (d_1(Y)\otimes\mathbb 1)(d_1(X)\otimes\mathbb 1) = [d_1(X), d_1(Y)]\otimes\mathbb 1 = d_1([X, Y])\otimes\mathbb 1$, since $d_1$ is a representation. Second term: $(d_1(X)\otimes\mathbb 1)(\mathbb 1\otimes d_2(Y)) = d_1(X)\otimes d_2(Y) = (\mathbb 1\otimes d_2(Y))(d_1(X)\otimes\mathbb 1)$, so $[A_X, B_Y] = 0$; likewise $[B_X, A_Y] = 0$. Fourth term: $\mathbb 1\otimes d_2([X, Y])$. The sum is $(d_1\otimes d_2)([X, Y])$ (the same computation as $[J_i, J_j]$ for $\mathbf J = \mathbf J_1 + \mathbf J_2$ in QM Derivation §C7.1.1). Part 1 is proved.
>
> **3. The differential (Woit's computation).** Let $d$ be the differential of $D_1\otimes D_2$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]). By [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], 1, $D_i(e^{sX}) = e^{s\,d_i(X)}$, so on a product vector
>
> $$
> (D_1\otimes D_2)(e^{sX})\,(w_1\otimes w_2) = e^{s\,d_1(X)}w_1\otimes e^{s\,d_2(X)}w_2 .
> $$
>
> The map $(u_1, u_2) \mapsto u_1\otimes u_2$ is bilinear on finite-dimensional spaces, so the product rule applies; with $\frac{d}{ds}e^{s\,d_i(X)}w_i\big|_{s=0} = d_i(X)w_i$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], 5),
>
> $$
> d(X)\,(w_1\otimes w_2) = \frac{d}{ds}\Bigl(e^{s\,d_1(X)}w_1\otimes e^{s\,d_2(X)}w_2\Bigr)\Big|_{s=0} = d_1(X)w_1\otimes w_2 + w_1\otimes d_2(X)w_2 = (A_X + B_X)(w_1\otimes w_2) .
> $$
>
> Both sides are linear in the tensor and agree on the basis $e_i\otimes f_k$, so $d(X) = (d_1\otimes d_2)(X)$.
>
> **4. The exponential identity.** $A_X$ and $B_X$ commute (step 2), so $e^{A_X + B_X} = e^{A_X}e^{B_X}$ (Theorem §CB.1.5, 3). Since $(d_1(X)\otimes\mathbb 1)^k = d_1(X)^k\otimes\mathbb 1$ for every $k$, the partial sums of $e^{A_X}$ are $\bigl(\sum_{k\le N}d_1(X)^k/k!\bigr)\otimes\mathbb 1$, and in the limit $e^{A_X} = e^{d_1(X)}\otimes\mathbb 1$ (in the basis $e_i\otimes f_k$ the matrix of $M\otimes\mathbb 1$ depends linearly, hence continuously, on $M$). Likewise $e^{B_X} = \mathbb 1\otimes e^{d_2(X)}$, and
>
> $$
> e^{d_1(X)\otimes\mathbb 1 + \mathbb 1\otimes d_2(X)} = (e^{d_1(X)}\otimes\mathbb 1)(\mathbb 1\otimes e^{d_2(X)}) = e^{d_1(X)}\otimes e^{d_2(X)} .
> $$
>
> **5. Physicists' form.** With $T_a = iX_a$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-13|Def. §CB.1.13]]) the generator in a representation is $D(T_a) = i\,d(X_a)$, so by step 3 $D(T_a) = i\,d_1(X_a)\otimes\mathbb 1 + \mathbb 1\otimes i\,d_2(X_a) = D_1(T_a)\otimes\mathbb 1 + \mathbb 1\otimes D_2(T_a)$.
>
> **What the proof shows**
> - The Leibniz rule is forced: the two factors are moved by the same group element, and the derivative of a product of two curves has two terms. Nothing beyond bilinearity of $\otimes$ is used.
> - The finite and infinitesimal forms agree only because $d_1(X)\otimes\mathbb 1$ and $\mathbb 1\otimes d_2(X)$ act on different factors and therefore commute (step 4); this is why the total angular momentum of a composite system is the generator of its joint rotation ([[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-1|QM Theorem §C7.1.1]]).
> - Used next: weights add under tensor products (Theorem §CB.9.10), and the tensor law of indices is the case of several vector and covector slots ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-14|Theorem §CB.0.14]]).

^pf-cb-7-3

*Uses:* [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-1|Def. §CB.7.1]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-2|Def. §CB.7.2]], [[§38 Tensor Products#^ladr-9-74|LADR Thm. 9.74]], [[§38 Tensor Products#^ladr-9-79|LADR Thm. 9.79]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-13|Def. §CB.1.13]]

> [!definition] Definition §CB.7.4: Outer Tensor Product
> If $D_1$ is a representation of $G_1$ on $W_1$ and $D_2$ one of $G_2$ on $W_2$, their **outer tensor product** $D_1\boxtimes D_2$ is the representation of $G_1\times G_2$ on $W_1\otimes W_2$ with $(g_1, g_2) \mapsto D_1(g_1)\otimes D_2(g_2)$; for Lie algebras, $\mathfrak g_1\oplus\mathfrak g_2$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-11|Def. §CB.3.11]]) acts by $(X_1, X_2) \mapsto d_1(X_1)\otimes\mathbb 1 + \mathbb 1\otimes d_2(X_2)$.
>
> *Source: written here*

^def-cb-7-4

> [!theorem] Theorem §CB.7.5: Irreducible Representations of a Direct Sum Are Outer Tensor Products
> Let $\mathfrak h_1$, $\mathfrak h_2$ be complex Lie algebras and consider finite-dimensional complex-linear representations.
> 1. If $W_1$, $W_2$ are irreducible representations of $\mathfrak h_1$, $\mathfrak h_2$, then $W_1\boxtimes W_2$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-4|Def. §CB.7.4]]) is an irreducible representation of $\mathfrak h_1\oplus\mathfrak h_2$.
> 2. Every irreducible representation of $\mathfrak h_1\oplus\mathfrak h_2$ is equivalent to such a $W_1\boxtimes W_2$, with $W_1$, $W_2$ unique up to equivalence.
>
> The same holds for real Lie algebras and their representations on complex spaces, and for groups $G_1\times G_2$.
>
> *Source: P. Etingof et al., Introduction to Representation Theory, §2.10, Thm. 2.26 (irreducible representations of a tensor product of algebras; part 1 by the density theorem, Thm. 2.5), with Cor. 2.4 and the Remark in §2.1 (the evaluation map $\operatorname{Hom}_A(X, V)\otimes X \to V$) for part 2 (arXiv:0901.0827, https://arxiv.org/abs/0901.0827) · Burnside's theorem: [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-11|Theorem §CB.6.11]] · the Lorentz case: [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-3|Theorem §CB.16.3]]*

^thm-cb-7-5

> [!proof]- Proof
> *Part 1 is Etingof's proof of Thm. 2.26 (i). For part 2 Etingof passes to the semisimple quotient by the radical, a tool not set up in CB; the evaluation-map argument below uses only his Cor. 2.4 (the density statement: an element of the algebra moves linearly independent vectors to arbitrary ones) and Schur's lemma.*
>
> **0. The algebra generated by a set of operators.** For a set $\mathcal S$ of operators on a finite-dimensional complex space $U$, let $A(\mathcal S) \subset \operatorname{End}(U)$ be the set of complex linear combinations of finite products of elements of $\mathcal S$, together with $\mathbb 1$: a subalgebra containing $\mathbb 1$. A subspace is invariant under every element of $\mathcal S$ iff it is invariant under every element of $A(\mathcal S)$ (sums, scalar multiples and products of operators preserving it preserve it). So $U$ is irreducible under $\mathcal S$ iff it is irreducible under $A(\mathcal S)$, and then $A(\mathcal S) = \operatorname{End}(U)$ by Burnside's theorem ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-11|Theorem §CB.6.11]]).
>
> **1. Part 1: the two factor algebras.** On $W_1\boxtimes W_2$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-4|Def. §CB.7.4]]) the element $(X_1, 0)$ acts by $d_1(X_1)\otimes\mathbb 1$ and $(0, X_2)$ by $\mathbb 1\otimes d_2(X_2)$. Products of operators $d_1(X)\otimes\mathbb 1$ are $(d_1(X)d_1(Y)\cdots)\otimes\mathbb 1$, so the algebra $\mathcal A$ generated by the action contains $a_1\otimes\mathbb 1$ for every $a_1 \in A(d_1(\mathfrak h_1))$, which is $\operatorname{End}(W_1)$ by step 0 ($W_1$ irreducible). Likewise $\mathbb 1\otimes a_2 \in \mathcal A$ for every $a_2 \in \operatorname{End}(W_2)$.
>
> **2. Part 1: all operators.** Hence $\mathcal A$ contains every product $(a_1\otimes\mathbb 1)(\mathbb 1\otimes a_2) = a_1\otimes a_2$, in particular $E^{(1)}_{ij}\otimes E^{(2)}_{kl}$ for the matrix units in bases $e_i$ of $W_1$, $f_k$ of $W_2$. In the basis $e_i\otimes f_k$ of $W_1\otimes W_2$ ([[§38 Tensor Products#^ladr-9-74|LADR Thm. 9.74]]) these are exactly the matrix units ($e_j\otimes f_l \mapsto e_i\otimes f_k$, all other basis vectors to $0$), which span all operators ([[§9 Matrices#^ladr-3-40|LADR Thm. 3.40]]). So $\mathcal A = \operatorname{End}(W_1\otimes W_2)$. If $U \ne 0$ is invariant, pick $u \ne 0$ in $U$; for any $w$ some operator maps $u$ to $w$, so $U$ is everything. $W_1\boxtimes W_2$ is irreducible.
>
> **3. Part 2: the two commuting actions.** Let $M$ be an irreducible finite-dimensional representation $d$ of $\mathfrak h_1\oplus\mathfrak h_2$ and put $\rho_1(X_1) = d(X_1, 0)$, $\rho_2(X_2) = d(0, X_2)$. They commute: $[\rho_1(X_1), \rho_2(X_2)] = d\bigl([(X_1, 0), (0, X_2)]\bigr) = d(0) = 0$, the bracket of [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-11|Def. §CB.3.11]] being componentwise. $\rho_1$, $\rho_2$ are representations of $\mathfrak h_1$, $\mathfrak h_2$, and $d(X_1, X_2) = \rho_1(X_1) + \rho_2(X_2)$.
>
> **4. Part 2: a candidate for each factor.** $M \ne 0$, so among the nonzero $\rho_1$-invariant subspaces there is one of smallest dimension, $V$; it is irreducible under $\mathfrak h_1$. Let $H = \operatorname{Hom}_{\mathfrak h_1}(V, M)$, the intertwiners $f : V \to M$, $f\rho_1(X)|_V = \rho_1(X)f$ ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-2|Def. §CB.6.2]]); it contains the inclusion $\iota$, so $H \ne 0$. Define $(X_2\cdot f) = \rho_2(X_2)\circ f$. This is again in $H$, because $\rho_2(X_2)$ commutes with every $\rho_1(X)$ (step 3); it is linear in $f$ and $X_2$, and $[X_2, Y_2]\cdot f = [\rho_2(X_2), \rho_2(Y_2)]f = X_2\cdot(Y_2\cdot f) - Y_2\cdot(X_2\cdot f)$: a representation of $\mathfrak h_2$ on $H$.
>
> **5. Part 2: the evaluation map.** $(v, f) \mapsto f(v)$ is bilinear, so it defines a linear $\mathrm{ev} : V\otimes H \to M$, $v\otimes f \mapsto f(v)$ (LADR Thm. 9.79). It intertwines $V\boxtimes H$ with $M$: for $(X_1, X_2)$,
>
> $$
> \mathrm{ev}\bigl(\rho_1(X_1)v\otimes f + v\otimes\rho_2(X_2)f\bigr) = f(\rho_1(X_1)v) + \rho_2(X_2)f(v) = \rho_1(X_1)f(v) + \rho_2(X_2)f(v) = d(X_1, X_2)\,\mathrm{ev}(v\otimes f) ,
> $$
>
> using that $f$ is an intertwiner; both sides are linear, so this holds on all of $V\otimes H$. Its image contains $\mathrm{ev}(v\otimes\iota) = v \ne 0$ and is invariant ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-3|Theorem §CB.6.3]]); $M$ is irreducible, so $\mathrm{ev}$ is onto.
>
> **6. Part 2: ev is injective (Etingof's Cor. 2.4).** Let $\mathrm{ev}(t) = 0$. Expanding in a basis of $V$, $t = \sum_{i=1}^rv_i\otimes f_i$ with $v_1, \dots, v_r$ linearly independent (LADR Thm. 9.74), and $\sum_if_i(v_i) = 0$. Fix $k$ and any $u \in V$. Extend the $v_i$ to a basis; there is an operator $a$ of $V$ with $av_i = \delta_{ik}u$, and by step 0 ($V$ irreducible) $a = P(\rho_1|_V)$ for some linear combination $P$ of products of operators $\rho_1(X)|_V$. Let $P(\rho_1)$ be the same combination of the $\rho_1(X)$ on $M$. Each $f_i$ intertwines $\rho_1$, hence every product and combination of them: $f_i\circ P(\rho_1|_V) = P(\rho_1)\circ f_i$. Apply $P(\rho_1)$ to $\sum_if_i(v_i) = 0$:
>
> $$
> 0 = \sum_iP(\rho_1)f_i(v_i) = \sum_if_i(av_i) = f_k(u) .
> $$
>
> So $f_k = 0$ for every $k$, and $t = 0$. With step 5, $\mathrm{ev}$ is an equivalence $V\boxtimes H \cong M$.
>
> **7. Part 2: H is irreducible.** If $H' \subset H$ were invariant with $0 \ne H' \ne H$, then $V\otimes H'$ would be invariant under $V\boxtimes H$ (the formula of step 5's left side preserves it) with $0 < \dim V\dim H' < \dim V\dim H$, and its image under the equivalence a proper nonzero invariant subspace of $M$. So $W_1 = V$, $W_2 = H$ are irreducible and $M \cong W_1\boxtimes W_2$.
>
> **8. Part 2: uniqueness.** Suppose $W_1\boxtimes W_2 \cong W_1'\boxtimes W_2'$, all four irreducible. Restricted to $\mathfrak h_1$, $W_1\otimes W_2 = \bigoplus_k W_1\otimes f_k$ ($f_k$ a basis of $W_2$) is a direct sum of copies of $W_1$, and $W_1'\otimes f'_1$ is carried by the equivalence onto an irreducible $\mathfrak h_1$-invariant subspace $U \cong W_1'$ of it. Some projection $\pi_k : U \to W_1\otimes f_k \cong W_1$ along the other summands is nonzero (else $U = 0$); it is an intertwiner between irreducible representations, hence invertible by Schur's lemma ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-4|Theorem §CB.6.4]], 1). So $W_1' \cong W_1$; the same argument with the roles of the factors exchanged gives $W_2' \cong W_2$.
>
> **9. Real Lie algebras and groups.** Steps 0–8 use only: the sets of operators $\rho_1$, $\rho_2$ and the algebras they generate, that the two sets commute, Burnside and Schur. For a real Lie algebra acting on complex spaces the same words apply; for groups put $\rho_1(g_1) = D(g_1, 1)$, $\rho_2(g_2) = D(1, g_2)$, which commute because $(g_1, 1)(1, g_2) = (1, g_2)(g_1, 1)$, let $g_2$ act on $H$ by $f \mapsto \rho_2(g_2)\circ f$, and replace the sum $\rho_1 + \rho_2$ in step 5 by the product $D(g_1, g_2) = \rho_1(g_1)\rho_2(g_2)$: $\mathrm{ev}(\rho_1(g_1)v\otimes\rho_2(g_2)f) = \rho_2(g_2)f(\rho_1(g_1)v) = \rho_1(g_1)\rho_2(g_2)f(v)$.
>
> **What the proof shows**
> - ⚑ By-product: the irreducible piece is the *outer* product, with each factor acting on its own slot; for the Lorentz algebra $\mathfrak{so}(1,3)_{\mathbb C} = \mathfrak a_+\oplus\mathfrak a_-$ this is why its irreducible representations are labelled by a *pair* $(j_+, j_-)$ → [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-3|Theorem §CB.16.3]].
> - Complex scalars are essential: Burnside's theorem and Schur's lemma both fail over $\mathbb R$ (the rotations of $\mathbb R^2$ have no invariant line, yet they generate only the commutative algebra of matrices $\begin{pmatrix} a & -b \\ b & a\end{pmatrix}$, not all of $M_2(\mathbb R)$).
> - No complete reducibility is assumed: the restriction of $M$ to $\mathfrak h_1$ turns out to be a sum of copies of one irreducible, but that is an output (step 6).

^pf-cb-7-5

*Uses:* [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-11|Theorem §CB.6.11]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-3|Theorem §CB.6.3]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-2|Def. §CB.6.2]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-4|Theorem §CB.6.4]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-11|Def. §CB.3.11]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-4|Def. §CB.7.4]], [[§38 Tensor Products#^ladr-9-74|LADR Thm. 9.74]], [[§38 Tensor Products#^ladr-9-79|LADR Thm. 9.79]], [[§9 Matrices#^ladr-3-40|LADR Thm. 3.40]]

## Duals and complex conjugates

> [!definition] Definition §CB.7.6: Dual Representation
> The **dual** (contragredient) of a representation $D$ on $W$ is the representation $D^\ast$ on the dual space $W'$ ([[§12 Duality#^ladr-3-110|LADR Def. 3.110]]) with $D^\ast(g) = D(g^{-1})'$, the dual map ([[§12 Duality#^ladr-3-118|LADR Def. 3.118]]) of $D(g^{-1})$: $(D^\ast(g)\varphi)(w) = \varphi(D(g^{-1})w)$. For a Lie algebra, $d^\ast(X) = -d(X)'$. In a basis and its dual basis the matrices are $(D(g)^{-1})^{\mathsf T}$ and $-d(X)^{\mathsf T}$.
>
> *Source: Woit, §4.2 (Definition: dual or contragredient representation, $(\pi^{-1})^{\mathsf t}(g)$) · written here*

^def-cb-7-6

> [!definition] Definition §CB.7.7: Complex-Conjugate Representation
> The **complex conjugate** $\bar W$ of a complex vector space $W$ is the set $W$ with the same addition and scalar multiplication $\lambda\cdot_{\bar W}w = \bar\lambda w$. The **complex-conjugate representation** of a representation $D$ on $W$ is $\bar D(g) = D(g)$ regarded as a map of $\bar W$; for a Lie algebra (real, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-12|Theorem §CB.1.12]]), $\bar d(X) = d(X)$ on $\bar W$. In a basis the matrices are $\overline{D(g)}$ and $\overline{d(X)}$ (entrywise conjugates).
>
> *Source: written here*

^def-cb-7-7

> [!theorem] Theorem §CB.7.8: Conjugation of a Representation Is Conjugation of the Algebra
> Let $d$ be a representation of a real Lie algebra $\mathfrak g$ on $W$, $d_{\mathbb C}$ its complex-linear extension ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-9|Theorem §CB.3.9]]) and $c$ the conjugation of $\mathfrak g_{\mathbb C}$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]]). Then the complex-linear extension of $\bar d$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-7|Def. §CB.7.7]]) is
>
> $$
> (\bar d)_{\mathbb C}(Z) = d_{\mathbb C}(cZ) \quad \text{as maps of the set } W, \qquad Z \in \mathfrak g_{\mathbb C} .
> $$
>
> Consequences: for $\mathfrak{so}(1,3)$, whose conjugation exchanges $\mathfrak a_\pm$ ([[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-1|Theorem §CB.5.1]], 3), the conjugate representation exchanges the roles of $\mathbf J_+$ and $\mathbf J_-$; for $\mathfrak{su}(2)$ it maps each $\mathfrak{sl}(2, \mathbb C)$-representation to one with the same Casimir.
>
> *Source: the Lorentz case, [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-11|Theorem §CB.16.11]], Derivation, steps 2–3 (from the user's PHY 513 notes, Ch. 7 §7.4.6: "complex conjugation turns θ − iη into θ + iη"), here in basis-free form · P. Woit, Quantum Theory, Groups and Representations, §41.1 (conjugation of the group matrices flips the sign of the weights)*

^thm-cb-7-8

> [!proof]- Proof
> *The argument of Derivation §CB.16.11, steps 2–3, without a basis: there, conjugating the matrices; here, changing the scalar multiplication.*
>
> **1. $\bar d$ is a representation on $\bar W$.** Each $d(X)$ is additive, and for $\lambda \in \mathbb C$, $d(X)(\lambda\cdot_{\bar W}w) = d(X)(\bar\lambda w) = \bar\lambda\,d(X)w = \lambda\cdot_{\bar W}d(X)w$: $d(X)$ is complex-linear on $\bar W$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-7|Def. §CB.7.7]]). $X \mapsto d(X)$ is real-linear and preserves brackets, since the maps and their compositions are the same maps of the set $W$.
>
> **2. Its complex-linear extension.** By [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-9|Theorem §CB.3.9]], 1, applied on $\bar W$, $(\bar d)_{\mathbb C}(X + iY) = \bar d(X) + i\cdot_{\bar W}\bar d(Y)$, where $i\cdot_{\bar W}$ is multiplication by $i$ in $\bar W$, i.e. by $\bar i = -i$ in $W$. As maps of the set $W$,
>
> $$
> (\bar d)_{\mathbb C}(X + iY) = d(X) - i\,d(Y) = d_{\mathbb C}(X - iY) = d_{\mathbb C}\bigl(c(X + iY)\bigr) ,
> $$
>
> with $c(X + iY) = X - iY$ the conjugation of $\mathfrak g_{\mathbb C}$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]]). This is the formula.
>
> **3. In a basis.** If $e_1, \dots, e_n$ is a basis of $W$, it is also a basis of $\bar W$, and $w = \sum_aw_ae_a$ in $W$ reads $w = \sum_a\bar w_a\cdot_{\bar W}e_a$ in $\bar W$: the coordinates are conjugated, and so is every matrix, $\overline{d(X)}$, as Def. §CB.7.7 states. Step 2 then reads $(\bar d)_{\mathbb C}(Z) = \overline{d_{\mathbb C}(cZ)}$ as matrices, which for the Lorentz generators is $\bar{\mathbf J}_\pm = -(\mathbf J_\mp)^{\ast}$ of Derivation §CB.16.11, step 3.
>
> **4. The Lorentz algebra.** $c(J_{\pm i}) = -J_{\mp i}$ ([[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-1|Theorem §CB.5.1]], 3), so by step 2 $(\bar d)_{\mathbb C}(J_{+i}) = -d_{\mathbb C}(J_{-i})$ and $(\bar d)_{\mathbb C}(J_{-i}) = -d_{\mathbb C}(J_{+i})$ as maps of $W$: on $\bar W$ the copy $\mathfrak a_+$ acts through the operators by which $\mathfrak a_-$ acted on $W$, and conversely. The roles of $\mathbf J_+$ and $\mathbf J_-$ are exchanged.
>
> **5. $\mathfrak{su}(2)$.** The physicists' generators $J_a = iX_a$, $X_a \in \mathfrak{su}(2)$, satisfy $c(J_a) = -iX_a = -J_a$, so $(\bar d)_{\mathbb C}(J_a) = -d_{\mathbb C}(J_a)$ as maps of $W$, and the Casimir operator $\sum_a(\bar d)_{\mathbb C}(J_a)^2 = \sum_a d_{\mathbb C}(J_a)^2$ is the same map of the set $W$.
>
> **What the proof shows**
> - Conjugating a representation is not conjugating the group element: the algebra element stays, the scalar multiplication on the space is reversed, and this acts on $\mathfrak g_{\mathbb C}$ as the conjugation $c$ that fixes the real form.
> - ⚑ By-product: whether conjugation produces a new representation depends on how $c$ acts on $\mathfrak g_{\mathbb C}$. For the Lorentz algebra $c$ swaps the two ideals, so $(j_+, j_-) \mapsto (j_-, j_+)$; for $\mathfrak{su}(2)$ it preserves the only ideal, so every $V_j$ is self-conjugate → [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-15|Theorem §CB.7.15]], 3 (spin ½ explicitly).
> - Self-conjugacy of spin $j$ (moved here from step 5 in the CB ordering pass: it uses the classification of §CB.9, later): On an irreducible $V_j$ it is $j(j+1)\,\mathbb 1$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], 3), a real multiple of the identity, hence the same multiple in $\bar W$; the conjugate is irreducible (same invariant subspaces, as subsets) of dimension $2j + 1$, so it is again $V_j$ (Theorem §CB.9.3, 2).
> - Used in: [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-11|Theorem §CB.16.11]] (the Lorentz case with explicit matrices), Theorem §CB.7.16 (dotted indices).

^pf-cb-7-8

*Uses:* [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-7|Def. §CB.7.7]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-9|Theorem §CB.3.9]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-1|Theorem §CB.5.1]]

## Hom spaces, invariants and powers

> [!theorem] Theorem §CB.7.9: Hom(V, W) ≅ V* ⊗ W, and Its Invariants Are the Intertwiners
> For representations $D_V$, $D_W$ of $G$, $g\cdot T = D_W(g)\,T\,D_V(g)^{-1}$ is a representation on $\operatorname{Hom}(V, W)$; the linear isomorphism $V'\otimes W \to \operatorname{Hom}(V, W)$, $\varphi\otimes w \mapsto (v \mapsto \varphi(v)w)$, is an equivalence with $D_V^\ast\otimes D_W$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-1|Def. §CB.7.1]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-6|Def. §CB.7.6]]); and $T$ is fixed by every $g$ iff $T$ is an intertwiner ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-2|Def. §CB.6.2]]). The Lie algebra version: $X\cdot T = d_W(X)T - T\,d_V(X)$.
>
> *Source: K. E. Smith, Groups and their Representations, Ch. 4 §5.2 (the representation $g\cdot\varphi = g\circ\varphi\circ g^{-1}$ on $\operatorname{Hom}_{\mathbb C}(V, W)$; its fixed vectors are the $G$-linear maps, "Prove it!") · P. Woit, Quantum Theory, Groups and Representations, §9.1 (the isomorphism $V^{\ast}\otimes W \cong$ linear maps $V \to W$, $l\otimes w \mapsto (v \mapsto l(v)w)$) and §4.2 (the dual representation) · the slot rule: [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-10|Theorem §CB.0.10]]*

^thm-cb-7-9

> [!proof]- Proof
> *Smith's representation on Hom and Woit's isomorphism, with the verifications both leave to the reader written out.*
>
> **1. A representation on Hom(V, W).** $T \mapsto D_W(g)TD_V(g)^{-1}$ is linear in $T$. For $g, h \in G$,
>
> $$
> g\cdot(h\cdot T) = D_W(g)D_W(h)\,T\,D_V(h)^{-1}D_V(g)^{-1} = D_W(gh)\,T\,\bigl(D_V(g)D_V(h)\bigr)^{-1} = (gh)\cdot T ,
> $$
>
> and $\mathbb 1\cdot T = T$; the matrix of $g\cdot T$ is a product of matrices depending continuously on $g$ ($D_V(g)^{-1} = D_V(g^{-1})$).
>
> **2. The map Ψ is an isomorphism.** $(\varphi, w) \mapsto (v \mapsto \varphi(v)w)$ is bilinear, so it defines a linear $\Psi : V'\otimes W \to \operatorname{Hom}(V, W)$ ([[§38 Tensor Products#^ladr-9-79|LADR Thm. 9.79]]). Take a basis $e_1, \dots, e_n$ of $V$ with dual basis $e^1, \dots, e^n$ ([[§12 Duality#^ladr-3-116|LADR Thm. 3.116]]) and a basis $f_1, \dots, f_m$ of $W$. Then $\Psi(e^i\otimes f_k)$ maps $e_j \mapsto e^i(e_j)f_k = \delta_{ij}f_k$: its matrix is the matrix unit $E_{ki}$. The $e^i\otimes f_k$ are a basis of $V'\otimes W$ ([[§38 Tensor Products#^ladr-9-74|LADR Thm. 9.74]]) and the $mn$ matrix units a basis of $\mathbb C^{m,n}$ ([[§9 Matrices#^ladr-3-40|LADR Thm. 3.40]]), which is identified with $\operatorname{Hom}(V, W)$ by taking matrices. $\Psi$ maps a basis onto a basis, so it is an isomorphism.
>
> **3. Ψ is an equivalence.** By [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-6|Def. §CB.7.6]], $(D_V^{\ast}(g)\varphi)(v) = \varphi(D_V(g)^{-1}v)$. On a product vector, for every $v \in V$,
>
> $$
> \Psi\bigl(D_V^{\ast}(g)\varphi\otimes D_W(g)w\bigr)(v) = \varphi\bigl(D_V(g)^{-1}v\bigr)\,D_W(g)w = D_W(g)\Bigl[\varphi\bigl(D_V(g)^{-1}v\bigr)w\Bigr] = \bigl(D_W(g)\,\Psi(\varphi\otimes w)\,D_V(g)^{-1}\bigr)(v) ,
> $$
>
> using linearity of $D_W(g)$ to move the number $\varphi(\cdots)$ through it. So $\Psi\circ(D_V^{\ast}\otimes D_W)(g)$ and $(g\cdot\,)\circ\Psi$ agree on the products $\varphi\otimes w$, which span $V'\otimes W$, hence everywhere ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-1|Def. §CB.7.1]] for the tensor product).
>
> **4. Fixed vectors are intertwiners (Smith's "prove it").** $g\cdot T = T$ means $D_W(g)TD_V(g)^{-1} = T$; multiplying on the right by $D_V(g)$ gives $D_W(g)T = TD_V(g)$, and multiplying that on the right by $D_V(g)^{-1}$ gives back the first. So $T$ is fixed by every $g$ iff $T$ intertwines $D_V$ and $D_W$ ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-2|Def. §CB.6.2]]).
>
> **5. The Lie algebra version.** For $X \in \mathfrak g$, $e^{sX}\cdot T = e^{s\,d_W(X)}\,T\,e^{-s\,d_V(X)}$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], 1, and $(e^{A})^{-1} = e^{-A}$, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], 2). Differentiating the product at $s = 0$ with Theorem §CB.1.5, 5 (two terms, one for each factor depending on $s$):
>
> $$
> X\cdot T = \frac{d}{ds}\Bigl(e^{s\,d_W(X)}\,T\,e^{-s\,d_V(X)}\Bigr)\Big|_{s=0} = d_W(X)\,T - T\,d_V(X) .
> $$
>
> This is the differential of the representation of step 1, hence a representation of $\mathfrak g$ (Theorem §CB.2.8, 1). $X\cdot T = 0$ for all $X$ iff $d_W(X)T = Td_V(X)$ for all $X$, the intertwiner condition for the algebra. The same differentiation applied to step 3 shows that $\Psi$ also intertwines the algebra representations, with $d_V^{\ast}(X) = -d_V(X)'$ (Def. §CB.7.6).
>
> **What the proof shows**
> - ⚑ By-product: "invariant tensor with one $V'$ slot and one $W$ slot" and "intertwiner $V \to W$" are one notion, so the invariant symbols of physics ($\delta^\mu{}_\nu$, $(\gamma^\mu)^a{}_b$, $(\sigma^\mu)_{a\dot b}$) are intertwiners between the representations carried by their slots → [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-10|Def. §CB.7.10]]; in components this is the slot rule ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-10|Theorem §CB.0.10]]).
> - The inverse $D_V(g)^{-1}$ on the source slot is what the dual representation supplies; nothing else about $V$ or $W$ is used (no inner product, no irreducibility).
> - Used next: Schur's lemma becomes a statement about invariant tensors (one invariant in $V'\otimes V$ for irreducible $V$, namely $\mathbb 1$); [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]] ($\gamma^\mu$ as an invariant).

^pf-cb-7-9

*Uses:* [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-1|Def. §CB.7.1]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-6|Def. §CB.7.6]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-2|Def. §CB.6.2]], [[§38 Tensor Products#^ladr-9-74|LADR Thm. 9.74]], [[§38 Tensor Products#^ladr-9-79|LADR Thm. 9.79]], [[§12 Duality#^ladr-3-116|LADR Thm. 3.116]], [[§9 Matrices#^ladr-3-40|LADR Thm. 3.40]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]]

The course's slot rule, the component form of this theorem, stated in [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors|§CB.0]] (first written for spinor space):

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-10]]

> [!definition] Definition §CB.7.10: Invariant Tensor
> An **invariant tensor** of a representation $D$ on a tensor space $\mathcal T$ (a tensor product of copies of $W$, $W'$, $\bar W$, $\bar W'$) is a $t \in \mathcal T$ with $D(g)t = t$ for all $g$; for a Lie algebra, $d(X)t = 0$ for all $X$. By [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-9|Theorem §CB.7.9]], an invariant tensor in $V'\otimes W$ is the same thing as an intertwiner $V \to W$.
>
> *Source: written here*

^def-cb-7-10

> [!definition] Definition §CB.7.11: Symmetric Power
> The **$k$-th symmetric power** $\operatorname{Sym}^kW \subset W^{\otimes k}$ is the subspace of tensors fixed by every permutation of the $k$ factors.
>
> *Source: Woit, §9.2 (the symmetric subspace $S^n(H)$ of $H^{\otimes n}$), §9.6 · S. Wadsley, Representation Theory, Lecture 12 (the same definition) · written here*

^def-cb-7-11

> [!definition] Definition §CB.7.12: Exterior Power
> The **$k$-th exterior power** $\Lambda^kW \subset W^{\otimes k}$ is the subspace of tensors $t$ with $\pi t = \operatorname{sgn}(\pi)\,t$ for every permutation $\pi$ of the $k$ factors ([[§36 Alternating Multilinear Forms#^ladr-9-32|LADR Def. 9.32]] for the sign); $w_1\wedge\cdots\wedge w_k = \frac1{k!}\sum_\pi\operatorname{sgn}(\pi)\,w_{\pi(1)}\otimes\cdots\otimes w_{\pi(k)}$. The **exterior algebra** is $\Lambda W = \bigoplus_{k=0}^{\dim W}\Lambda^kW$ with the product $\wedge$.
>
> *Source: Woit, §9.2 (the antisymmetric subspace $\Lambda^n(H)$), §9.6, eq. (9.6) (the wedge product with $\frac1{n!}$) · S. Wadsley, Representation Theory, Lecture 12 · LADR §36 (alternating forms, the dual picture) · written here*

^def-cb-7-12

> [!theorem] Theorem §CB.7.13: Symmetric and Exterior Powers Are Subrepresentations
> 1. $\operatorname{Sym}^kW$ and $\Lambda^kW$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-11|Def. §CB.7.11]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-12|Def. §CB.7.12]]) are invariant under $D^{\otimes k}$; $\dim\operatorname{Sym}^kW = \binom{n + k - 1}{k}$, $\dim\Lambda^kW = \binom nk$ for $\dim W = n$.
> 2. $W\otimes W = \operatorname{Sym}^2W\oplus\Lambda^2W$ as representations.
> 3. For representations $A$ of $G_1$ and $B$ of $G_2$: $\Lambda^2(A\otimes B) \cong (\operatorname{Sym}^2A\boxtimes\Lambda^2B)\oplus(\Lambda^2A\boxtimes\operatorname{Sym}^2B)$ and $\operatorname{Sym}^2(A\otimes B) \cong (\operatorname{Sym}^2A\boxtimes\operatorname{Sym}^2B)\oplus(\Lambda^2A\boxtimes\Lambda^2B)$ as representations of $G_1\times G_2$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-4|Def. §CB.7.4]]).
>
> *Source: parts 1–2: S. Wadsley, Representation Theory (Cambridge Part II lecture notes), Lectures 11–12 (the swap $\sigma$ commutes with $G$; $S^nV$, $\Lambda^nV$ are subrepresentations; the bases of $S^nV$ and $\Lambda^nV$, given there as a hint; https://www.dpmms.cam.ac.uk/~sjw47/RepThLectures.pdf) and the Part II Representation Theory notes, §9.3, Lemma ($V^{\otimes2} = S^2V\oplus\Lambda^2V$, $\dim = \frac12n(n \pm 1)$; https://dec41.user.srcf.net/notes/II_L/representation_theory_thm_proof.pdf) · part 3: proof to be filled · the two-index case: [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-5|Theorem §C1a.5.5]]*

^thm-cb-7-13

> [!proof]- Proof
> *Parts 1–2 follow Wadsley, Lectures 11–12, with his hint for the bases written out.*
>
> **1. The permutation operators.** For a permutation $\pi$ of $\{1, \dots, k\}$, $(w_1, \dots, w_k) \mapsto w_{\pi^{-1}(1)}\otimes\cdots\otimes w_{\pi^{-1}(k)}$ is $k$-linear, so it defines a linear $\sigma_\pi$ on $W^{\otimes k}$ ([[§38 Tensor Products#^ladr-9-92|LADR Thm. 9.92]]). With $u_i = w_{\rho^{-1}(i)}$, $\sigma_\pi\sigma_\rho(w_1\otimes\cdots) = \sigma_\pi(u_1\otimes\cdots) = \bigotimes_iu_{\pi^{-1}(i)} = \bigotimes_iw_{\rho^{-1}\pi^{-1}(i)} = \sigma_{\pi\rho}(w_1\otimes\cdots)$, so $\sigma_\pi\sigma_\rho = \sigma_{\pi\rho}$. Definitions §CB.7.11–§CB.7.12 read $\operatorname{Sym}^kW = \{t : \sigma_\pi t = t\ \forall\pi\}$, $\Lambda^kW = \{t : \sigma_\pi t = \operatorname{sgn}(\pi)t\ \forall\pi\}$.
>
> **2. Invariance (Wadsley's argument).** On products, $\sigma_\pi D^{\otimes k}(g)(w_1\otimes\cdots\otimes w_k) = \bigotimes_iD(g)w_{\pi^{-1}(i)} = D^{\otimes k}(g)\sigma_\pi(w_1\otimes\cdots\otimes w_k)$; products span ([[§38 Tensor Products#^ladr-9-90|LADR Thm. 9.90]]), so $\sigma_\pi$ commutes with every $D^{\otimes k}(g)$ ($D^{\otimes k}$ the iterated product of [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-1|Def. §CB.7.1]]). If $\sigma_\pi t = \epsilon(\pi)t$ for all $\pi$ ($\epsilon = 1$ or $\operatorname{sgn}$), then $\sigma_\pi D^{\otimes k}(g)t = D^{\otimes k}(g)\sigma_\pi t = \epsilon(\pi)D^{\otimes k}(g)t$: $\operatorname{Sym}^kW$ and $\Lambda^kW$ are invariant.
>
> **3. Two projections.** Put $P_\epsilon = \frac1{k!}\sum_\pi\epsilon(\pi)\sigma_\pi$. For fixed $\rho$, $\pi \mapsto \rho\pi$ is a bijection of the permutations and $\epsilon(\rho\pi) = \epsilon(\rho)\epsilon(\pi)$ (the sign is a homomorphism, [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|493 Thm. §21.3]]; $\epsilon(\rho)^2 = 1$), so
>
> $$
> \sigma_\rho P_\epsilon = \frac1{k!}\sum_\pi\epsilon(\pi)\sigma_{\rho\pi} = \epsilon(\rho)\,\frac1{k!}\sum_\pi\epsilon(\rho\pi)\sigma_{\rho\pi} = \epsilon(\rho)P_\epsilon ,
> $$
>
> and in the same way $P_\epsilon\sigma_\rho = \epsilon(\rho)P_\epsilon$ (reindex $\pi \mapsto \pi\rho$). So the image of $P_\epsilon$ lies in the corresponding space; and for $t$ in that space each term is $\epsilon(\pi)\sigma_\pi t = \epsilon(\pi)^2t = t$, so $P_\epsilon t = t$. Hence $\operatorname{Sym}^kW = P_1(W^{\otimes k})$ and $\Lambda^kW = P_{\operatorname{sgn}}(W^{\otimes k})$, each spanned by the images of the basis tensors $e_I = e_{i_1}\otimes\cdots\otimes e_{i_k}$ (LADR Thm. 9.90), $e_1, \dots, e_n$ a basis of $W$.
>
> **4. Which images are needed.** $\sigma_\pi e_I = e_{i_{\pi^{-1}(1)}}\otimes\cdots$ is the basis tensor of the rearranged index tuple, and $P_\epsilon\sigma_\pi = \epsilon(\pi)P_\epsilon$ (step 3). So $P_1e_I$ depends only on the multiset $\{i_1, \dots, i_k\}$, and $P_{\operatorname{sgn}}e_I = \pm P_{\operatorname{sgn}}e_J$ with $J$ the increasing rearrangement of $I$. If two entries of $I$ are equal, the transposition $\tau$ exchanging their positions has $\sigma_\tau e_I = e_I$, so $P_{\operatorname{sgn}}e_I = P_{\operatorname{sgn}}\sigma_\tau e_I = -P_{\operatorname{sgn}}e_I$, i.e. $P_{\operatorname{sgn}}e_I = 0$. Spanning sets: $\{P_1e_I : i_1 \le \cdots \le i_k\}$ for $\operatorname{Sym}^kW$, $\{P_{\operatorname{sgn}}e_I : i_1 < \cdots < i_k\}$ for $\Lambda^kW$ (Wadsley's hint).
>
> **5. They are independent.** $P_1e_I$ is a combination, with positive coefficients, of the basis tensors $e_{I'}$ whose index tuples $I'$ are rearrangements of $I$; for different multisets these sets of basis tensors are disjoint, and the $e_{I'}$ are independent, so the $P_1e_I$ are independent. For strictly increasing $J$ the entries are distinct, so $\sigma_\pi e_J = e_J$ only for $\pi = \mathrm{id}$: the coefficient of $e_J$ in $P_{\operatorname{sgn}}e_J$ is $\frac1{k!} \ne 0$, and again different $J$ involve disjoint sets of basis tensors.
>
> **6. Count.** Non-decreasing $k$-tuples from $\{1, \dots, n\}$ are the multisets of size $k$: putting $k$ balls into $n$ boxes is choosing the positions of $n - 1$ separators among $n + k - 1$ places, $\binom{n + k - 1}{k}$ ways. Strictly increasing $k$-tuples are the $k$-element subsets: $\binom nk$. Part 1 is proved.
>
> **7. Part 2 (Wadsley; Part II notes, Lemma §9.3).** For $k = 2$ there is one transposition, the swap $\sigma$, $\sigma^2 = \mathbb 1$. Every $t$ splits as $t = \frac12(t + \sigma t) + \frac12(t - \sigma t)$, with $\sigma$ fixing the first part and negating the second; if $t \in \operatorname{Sym}^2W\cap\Lambda^2W$, then $t = \sigma t = -t$, so $t = 0$. Hence $W\otimes W = \operatorname{Sym}^2W\oplus\Lambda^2W$, a direct sum of invariant subspaces (step 2), i.e. of representations. Check: $\binom{n+1}2 + \binom n2 = n^2$.
>
> **8. Part 3.** *To be filled.* The planned route: the reordering isomorphism $(A\otimes B)^{\otimes2} \cong A^{\otimes2}\otimes B^{\otimes2}$ is an equivalence of representations of $G_1\times G_2$ that carries the swap of the two $A\otimes B$ factors to $\sigma_A\otimes\sigma_B$; splitting $A^{\otimes2}$ and $B^{\otimes2}$ by part 2, the $(-1)$- and $(+1)$-eigenspaces of $\sigma_A\otimes\sigma_B$ are the two sums of the statement.
> <!-- searched: Woit (qmbook §§9.4–9.6, §41.1), Etingof et al. (arXiv:0901.0827), Wadsley's and the Part II Cambridge notes, Teleman's Representation Theory notes, Grinberg "A few classical results on tensor, symmetric and exterior powers", K. Conrad "Bases of symmetric and exterior powers", web search for Λ²(V⊗W) = Λ²V⊗S²W ⊕ S²V⊗Λ²W: no free text with a proof found; Fulton–Harris (not freely available) not checked. -->
>
> **What the proof shows**
> - The symmetric and exterior powers are cut out by the action of the permutation group on slots, which commutes with the group acting on each slot; any such "slot symmetry" gives subrepresentations. This is the same mechanism as Theorem §C1a.5.5 for two Lorentz indices.
> - ⚑ By-product: the symmetrizer $P_1$ and antisymmetrizer $P_{\operatorname{sgn}}$ are intertwiners (they commute with $D^{\otimes k}$, step 2), so $\operatorname{Sym}^kW$ and $\Lambda^kW$ are images of invariant projections, the form in which spin $j$ is built from $2j$ spinor slots → [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-9|Theorem §CB.9.9]].
> - For $k > 2$, $\operatorname{Sym}^kW\oplus\Lambda^kW \ne W^{\otimes k}$ (dimensions $\binom{n+k-1}k + \binom nk < n^k$ for $n \ge 2$): the rest consists of mixed symmetry types.

^pf-cb-7-13

*Uses:* [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-1|Def. §CB.7.1]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-11|Def. §CB.7.11]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-12|Def. §CB.7.12]], [[§38 Tensor Products#^ladr-9-90|LADR Thm. 9.90]], [[§38 Tensor Products#^ladr-9-92|LADR Thm. 9.92]], [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|493 Thm. §21.3]]

## Invariant tensors of the Lorentz group and of SL(2,ℂ)

> [!theorem] Theorem §CB.7.14: The Metric and the Levi-Civita Symbol Are Invariant Tensors
> 1. $g_{\mu\nu} \in (V')^{\otimes2}$ and $g^{\mu\nu} \in V^{\otimes2}$ ($V = \mathbb R^{1,3}$) are invariant tensors ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-10|Def. §CB.7.10]]) of $O(1,3)$; equivalently $g : V \to V'$ is an intertwiner, so $V \cong V^\ast$ as representations.
> 2. $\varepsilon^{\mu\nu\rho\sigma} \in \Lambda^4V$ satisfies $\Lambda\cdot\varepsilon = (\det\Lambda)\,\varepsilon$: it is invariant under $SO(1,3)$ and changes sign under $\mathcal P$ and $\mathcal T$.
>
> *Source: the metric: [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-2|REL Theorem §B2.2.2]], 1, and [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|Theorem §C1a.5.2]] · the Levi-Civita symbol: [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-4|REL Theorem §B2.2.4]] (proved there by the Leibniz formula) and [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]] · the user's PHY 513 notes, Ch. 1 §1.5*

^thm-cb-7-14

> [!proof]- Proof
> *Both facts are proved in their homes (REL Theorems §B2.2.2 and §B2.2.4, Theorem §C1a.5.2); this proof restates them as statements about the representations $\Lambda^{\otimes k}$ and $(\Lambda^{\ast})^{\otimes k}$ of [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-1|Def. §CB.7.1]] and [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-6|Def. §CB.7.6]].*
>
> **1. The action on the slots.** On $V^{\otimes2}$ and $(V')^{\otimes2}$ the group acts by $\Lambda\otimes\Lambda$ and $\Lambda^{\ast}\otimes\Lambda^{\ast}$, $\Lambda^{\ast}$ having the matrix $(\Lambda^{-1})^{\mathsf T}$ in the dual basis. In components this is the tensor law ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-14|Theorem §CB.0.14]]): $(\Lambda\cdot g)_{\mu\nu} = (\Lambda^{-1})^\rho{}_\mu(\Lambda^{-1})^\sigma{}_\nu\,g_{\rho\sigma}$, the matrix $(\Lambda^{-1})^{\mathsf T}g\,\Lambda^{-1}$; and $(\Lambda\cdot g^{-1})^{\mu\nu} = \Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma\,g^{\rho\sigma}$, the matrix $\Lambda g^{-1}\Lambda^{\mathsf T}$.
>
> **2. $g_{\mu\nu}$ is invariant.** $\Lambda \in O(1,3)$ means $\Lambda^{\mathsf T}g\Lambda = g$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]). $O(1,3)$ is a group ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-13|Theorem §CB.0.13]], 1), so $\Lambda^{-1} \in O(1,3)$ and $(\Lambda^{-1})^{\mathsf T}g\,\Lambda^{-1} = g$: by step 1, $\Lambda\cdot g = g$.
>
> **3. $g^{\mu\nu}$ is invariant.** Invert both sides of $\Lambda^{\mathsf T}g\Lambda = g$: $\Lambda^{-1}g^{-1}(\Lambda^{\mathsf T})^{-1} = g^{-1}$. Multiply by $\Lambda$ on the left and by $\Lambda^{\mathsf T}$ on the right: $g^{-1} = \Lambda g^{-1}\Lambda^{\mathsf T}$, which by step 1 is $\Lambda\cdot g^{-1} = g^{-1}$.
>
> **4. Lowering is an intertwiner.** The map $x \mapsto x^\flat = g(x, \cdot\,)$ is an isomorphism $V \to V'$ with matrix $g$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-12|Theorem §CB.0.12]]). It intertwines $\Lambda$ with $\Lambda^{\ast}$ iff $(\Lambda^{-1})^{\mathsf T}g = g\Lambda$, i.e. (multiply on the left by $\Lambda^{\mathsf T}$) $g = \Lambda^{\mathsf T}g\Lambda$, the defining condition. So $V \cong V^{\ast}$ as representations of $O(1,3)$. Equivalently, by [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-9|Theorem §CB.7.9]], the invariant $g \in V'\otimes V' \cong \operatorname{Hom}(V, V')$ of step 2 is this intertwiner.
>
> **5. The Levi-Civita symbol.** $\varepsilon^{\mu\nu\rho\sigma}$ is totally antisymmetric, so it lies in $\Lambda^4V$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-12|Def. §CB.7.12]]; $\dim\Lambda^4V = \binom44 = 1$, Theorem §CB.7.13, 1), and $\Lambda^{\otimes4}$ acts on it by $(\Lambda\cdot\varepsilon)^{\mu\nu\rho\sigma} = \Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta\Lambda^\rho{}_\gamma\Lambda^\sigma{}_\delta\,\varepsilon^{\alpha\beta\gamma\delta}$. By the argument of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-18|Theorem §CB.0.18]], 1, with rows in place of columns (antisymmetry of the left side in $\mu\nu\rho\sigma$, then the Leibniz formula for its $0123$ component), this equals $(\det\Lambda)\,\varepsilon^{\mu\nu\rho\sigma}$.
>
> **6. Signs.** $\det\Lambda = 1$ on $SO(1,3)$, so $\varepsilon$ is invariant there. $\mathcal P = \operatorname{diag}(1, -1, -1, -1)$ and $\mathcal T = \operatorname{diag}(-1, 1, 1, 1)$ have determinant $-1$, so $\mathcal P\cdot\varepsilon = \mathcal T\cdot\varepsilon = -\varepsilon$.
>
> **What the proof shows**
> - The course's versions (moved here from steps 2 and 5, CB ordering pass): step 2 is [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-2|REL Theorem §B2.2.2]], 1 (the components of the metric are the same in every inertial frame); step 5 is [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-4|REL Theorem §B2.2.4]], 1.
> - "Invariant tensor" is the representation-theoretic name for "has the same components in every inertial frame"; $g$ is invariant under all of $O(1,3)$, $\varepsilon$ only under $SO(1,3)$.
> - ⚑ By-product: $\Lambda^4V$ is the one-dimensional representation $\Lambda \mapsto \det\Lambda$, the same mechanism that makes $\Lambda^2\mathbb C^2$ the determinant representation of $GL(2, \mathbb C)$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-15|Theorem §CB.7.15]], 1); pseudoscalars are vectors of this representation.
> - $V \cong V^{\ast}$ comes from an invariant nondegenerate form; for $SL(2, \mathbb C)$ the form is antisymmetric ($\varepsilon_{ab}$, Theorem §CB.7.15, 2), which is the origin of the sign rules of spinor indices.

^pf-cb-7-14

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-12|Theorem §CB.0.12]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-14|Theorem §CB.0.14]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-13|Theorem §CB.0.13]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-18|Theorem §CB.0.18]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-9|Theorem §CB.7.9]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-13|Theorem §CB.7.13]]

> [!theorem] Theorem §CB.7.15: ε on ℂ² and SL(2,ℂ) = Sp(2,ℂ)
> Let $\varepsilon = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix}$, the alternating form $\varepsilon(u, v) = u^{\mathsf T}\varepsilon v$ on $\mathbb C^2$.
> 1. $A^{\mathsf T}\varepsilon A = (\det A)\,\varepsilon$ for every $A \in M_2(\mathbb C)$; so $SL(2, \mathbb C) = \{A : A^{\mathsf T}\varepsilon A = \varepsilon\} = Sp(2, \mathbb C)$, and $\Lambda^2\mathbb C^2$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-12|Def. §CB.7.12]]) is the representation $A \mapsto \det A$, trivial on $SL(2, \mathbb C)$.
> 2. $\varepsilon : \mathbb C^2 \to (\mathbb C^2)'$ is an intertwiner from the defining representation of $SL(2, \mathbb C)$ to its dual ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-6|Def. §CB.7.6]]): $(A^{-1})^{\mathsf T} = \varepsilon A\varepsilon^{-1}$.
> 3. For $A \in SU(2)$, $\bar A = (A^{-1})^{\mathsf T} = \varepsilon A\varepsilon^{-1}$: the defining representation of $SU(2)$ is equivalent to its dual and to its conjugate ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-7|Def. §CB.7.7]]).
>
> *Source: part 1: P. Woit, Quantum Theory, Groups and Representations, §16.1.1, eq. (16.4) ($Sp(2, \mathbb R) = SL(2, \mathbb R)$ by the same computation; §41.1 notes that it shows $SL(2, \mathbb C)$-invariance of $\varepsilon$) · the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "Index calculus for Weyl spinors": $M^{\mathsf T}EM = (\det M)E$) · part 2: Yu Zhao-Huan, 量子场论讲义, §9.6.1, eq. (9.354) ($\sigma^2d(\Lambda)\sigma^2 = d^{-1\mathsf T}(\Lambda)$, with $\varepsilon = i\sigma^2$, eq. (9.360)) · part 3: Woit, §4.6.2 (for unitary matrices the dual representation is the conjugate) and §41.1 (the explicit conjugation by $\varepsilon$) · $\Lambda^2$: S. Wadsley, Representation Theory, Lecture 12 (exercise: $\Lambda^{\dim V}V$ is $\det\rho$)*

^thm-cb-7-15

> [!proof]- Proof
> *Woit's and the 513 notes' computation for part 1; parts 2–3 follow from it as in Yu §9.6.1 and Woit §4.6.2.*
>
> **1. Part 1: the product.** Write $A = \begin{pmatrix} \alpha & \beta \\ \gamma & \delta\end{pmatrix}$. Then
>
> $$
> A^{\mathsf T}\varepsilon = \begin{pmatrix} \alpha & \gamma \\ \beta & \delta\end{pmatrix}\begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix} = \begin{pmatrix} -\gamma & \alpha \\ -\delta & \beta\end{pmatrix}, \qquad A^{\mathsf T}\varepsilon A = \begin{pmatrix} -\gamma\alpha + \alpha\gamma & -\gamma\beta + \alpha\delta \\ -\delta\alpha + \beta\gamma & -\delta\beta + \beta\delta\end{pmatrix} = \begin{pmatrix} 0 & \det A \\ -\det A & 0\end{pmatrix} = (\det A)\,\varepsilon .
> $$
>
> **2. Part 1: $SL(2, \mathbb C) = Sp(2, \mathbb C)$.** Since $\varepsilon \ne 0$, $A^{\mathsf T}\varepsilon A = \varepsilon$ iff $\det A = 1$.
>
> **3. Part 1: $\Lambda^2\mathbb C^2$.** $\dim\Lambda^2\mathbb C^2 = \binom22 = 1$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-13|Theorem §CB.7.13]], 1), spanned by $e_1\otimes e_2 - e_2\otimes e_1$. With $Ae_1 = \alpha e_1 + \gamma e_2$, $Ae_2 = \beta e_1 + \delta e_2$, expand all eight terms:
>
> $$
> Ae_1\otimes Ae_2 - Ae_2\otimes Ae_1 = (\alpha\beta - \beta\alpha)\,e_1\otimes e_1 + (\alpha\delta - \beta\gamma)\,e_1\otimes e_2 + (\gamma\beta - \delta\alpha)\,e_2\otimes e_1 + (\gamma\delta - \delta\gamma)\,e_2\otimes e_2 = (\det A)\,(e_1\otimes e_2 - e_2\otimes e_1) .
> $$
>
> So $A^{\otimes2}$ acts on $\Lambda^2\mathbb C^2$ by $\det A$, trivially on $SL(2, \mathbb C)$.
>
> **4. Part 2.** For $\det A = 1$, part 1 gives $A^{\mathsf T}\varepsilon A = \varepsilon$. Multiply on the left by $(A^{\mathsf T})^{-1}$: $\varepsilon A = (A^{\mathsf T})^{-1}\varepsilon$; then on the right by $\varepsilon^{-1}$:
>
> $$
> \varepsilon A\varepsilon^{-1} = (A^{\mathsf T})^{-1} = (A^{-1})^{\mathsf T} .
> $$
>
> The dual representation has matrix $(A^{-1})^{\mathsf T}$ in the dual basis ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-6|Def. §CB.7.6]]); the map with matrix $\varepsilon$ from $\mathbb C^2$ to $(\mathbb C^2)'$ therefore satisfies $(A^{-1})^{\mathsf T}\varepsilon = \varepsilon A$: it is an invertible intertwiner ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-2|Def. §CB.6.2]]). As a functional, the column $\varepsilon u$ is $v \mapsto (\varepsilon u)^{\mathsf T}v = -u^{\mathsf T}\varepsilon v = \varepsilon(v, u)$, the form with $u$ in the second slot. This is Yu's (9.354), $\sigma^2d\,\sigma^2 = d^{-1\mathsf T}$, with $\varepsilon = i\sigma^2$ and $\varepsilon^{-1} = -\varepsilon = -i\sigma^2$.
>
> **5. Part 3.** For $A \in SU(2)$, $A^{-1} = A^\dagger = \bar A^{\mathsf T}$, so $(A^{-1})^{\mathsf T} = \bar A$ (Woit §4.6.2). With part 2, $\bar A = \varepsilon A\varepsilon^{-1}$: $\varepsilon$ is an equivalence from the defining representation to its conjugate ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-7|Def. §CB.7.7]]; in a basis the conjugate representation has the matrices $\bar A$) as well as to its dual. Woit §41.1 checks it on $A = \begin{pmatrix} \alpha & \beta \\ -\bar\beta & \bar\alpha\end{pmatrix}$: $\varepsilon A\varepsilon^{-1} = \begin{pmatrix} \bar\alpha & \bar\beta \\ -\beta & \alpha\end{pmatrix} = \bar A$.
>
> **What the proof shows**
> - ⚑ By-product: the invariant pairing of two spinors is antisymmetric, $\varepsilon(u, v) = -\varepsilon(v, u)$, so $\varepsilon(u, u) = 0$ for commuting components; this is why the invariant $\eta^a\eta_a$ of a single Weyl spinor vanishes unless its components anticommute (Yu §9.6.1, eqs. (9.371)–(9.372); the user's PHY 513 notes, Ch. 8 §8.2).
> - Unit determinant is exactly invariance of $\varepsilon$: in two dimensions "special linear" and "symplectic" coincide.
> - Part 3 fails for $SL(2, \mathbb C)$: there $(A^{-1})^{\mathsf T} \ne \bar A$ in general, and the conjugate is a genuinely different representation → Theorem §CB.7.16.

^pf-cb-7-15

> [!proof]- Proof (second route: the course's computation)
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "Index calculus for Weyl spinors": "$M^{\mathsf T}EM = (\det M)E$"), as written for the course's spinor indices in [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], part 1, with $E = \varepsilon$ and $M = A$.*
>
> **1. The determinant identity.** Write $M = \begin{pmatrix}m_{11}&m_{12}\\m_{21}&m_{22}\end{pmatrix}$. Then $EM = \begin{pmatrix}m_{21}&m_{22}\\-m_{11}&-m_{12}\end{pmatrix}$ and
>
> $$
> M^{\mathsf T}EM = \begin{pmatrix}m_{11}&m_{21}\\m_{12}&m_{22}\end{pmatrix}\begin{pmatrix}m_{21}&m_{22}\\-m_{11}&-m_{12}\end{pmatrix} = \begin{pmatrix}m_{11}m_{21} - m_{21}m_{11} & m_{11}m_{22} - m_{21}m_{12}\\ m_{12}m_{21} - m_{22}m_{11} & m_{12}m_{22} - m_{22}m_{12}\end{pmatrix} = (\det M)\,E .
> $$
>
> **What the proof shows**
> - Invariance of $\varepsilon$ is exactly $\det = 1$: $SL(2, \mathbb C)$ is the group of complex $2\times2$ matrices preserving an antisymmetric form, $Sp(2, \mathbb C)$.

^pf-cb-7-15b

*Uses:* [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-6|Def. §CB.7.6]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-7|Def. §CB.7.7]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-13|Theorem §CB.7.13]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-2|Def. §CB.6.2]]

> [!theorem] Theorem §CB.7.16: The Four Two-Dimensional Representations of SL(2,ℂ)
> On $\mathbb C^2$ the matrices $A$, $(A^{-1})^{\mathsf T}$, $\bar A$ and $(A^\dagger)^{-1}$ ($A \in SL(2, \mathbb C)$) give the defining representation, its dual, its conjugate and the dual of the conjugate. They fall into exactly two equivalence classes: $A \cong (A^{-1})^{\mathsf T}$ and $\bar A \cong (A^\dagger)^{-1}$, both via $\varepsilon$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-15|Theorem §CB.7.15]]); $A \not\cong \bar A$, since $\operatorname{tr}A \ne \operatorname{tr}\bar A$ for $A = \operatorname{diag}(2i, -\frac i2)$. In index language: undotted indices carry $A$, dotted indices carry $\bar A$, and $\varepsilon$ raises and lowers each kind without mixing them.
>
> *Source: Yu Zhao-Huan, 量子场论讲义, §9.6.1, eqs. (9.354)–(9.356), Fig. 9.1 (the four representations and the two equivalences), eqs. (9.358), (9.363)–(9.364), (9.376), (9.380)–(9.381) (index placement) · P. Woit, Quantum Theory, Groups and Representations, §41.1 (the four representations $S_L$, $S_L^{\ast}$, $S_R$, $S_R^{\ast}$; conjugation cannot turn all $SL(2, \mathbb C)$ matrices into their conjugates because it preserves eigenvalues) · H. K. Dreiner, H. E. Haber, S. P. Martin, Two-component spinor techniques…, Phys. Rept. 494 (2010), §2.1, eqs. (2.18)–(2.22), (2.103)–(2.104) (arXiv:0812.1594) · the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The two halves are irreducible, inequivalent, and related by conjugation")*

^thm-cb-7-16

> [!proof]- Proof
> *Yu's two equivalences (§9.6.1) and Woit's eigenvalue argument (§41.1), with the trace as the invariant.*
>
> **1. The four are representations, and which is which.** $A \mapsto (A^{-1})^{\mathsf T}$ is the dual ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-6|Def. §CB.7.6]]); $A \mapsto \bar A$ is the conjugate ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-7|Def. §CB.7.7]]; entrywise conjugation respects products, $\overline{AB} = \bar A\bar B$). The dual of the conjugate has matrix $(\bar A^{-1})^{\mathsf T} = \bigl(\overline{A^{-1}}\bigr)^{\mathsf T} = (A^{-1})^\dagger = (A^\dagger)^{-1}$.
>
> **2. First equivalence.** $(A^{-1})^{\mathsf T} = \varepsilon A\varepsilon^{-1}$ for all $A \in SL(2, \mathbb C)$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-15|Theorem §CB.7.15]], 2): the defining representation is equivalent to its dual (Yu (9.354)).
>
> **3. Second equivalence.** $\det\bar A = \overline{\det A} = 1$, so $\bar A \in SL(2, \mathbb C)$ and step 2 applies to it: $(\bar A^{-1})^{\mathsf T} = \varepsilon\bar A\varepsilon^{-1}$, i.e. $(A^\dagger)^{-1} = \varepsilon\bar A\varepsilon^{-1}$ by step 1. The conjugate is equivalent to its dual, again via $\varepsilon$ ($\varepsilon$ is real, so it is its own conjugate; Yu (9.356)).
>
> **4. $A \not\cong \bar A$.** Suppose an invertible $S$ had $S A S^{-1} = \bar A$ for every $A \in SL(2, \mathbb C)$. The trace is invariant under conjugation, $\operatorname{tr}(SAS^{-1}) = \operatorname{tr}A$ (it is the trace of the operator, independent of the basis; K. E. Smith, Groups and their Representations, Ch. 4 §2, Def. 2.1), so $\operatorname{tr}A = \operatorname{tr}\bar A$ for all $A$. But $A_0 = \operatorname{diag}(2i, -\frac i2)$ has $\det A_0 = 2i\cdot(-\frac i2) = 1$ and $\operatorname{tr}A_0 = \frac{3i}2$, while $\operatorname{tr}\bar A_0 = -2i + \frac i2 = -\frac{3i}2$. Contradiction. (Woit's form: conjugation by $S$ preserves the eigenvalues $2i, -\frac i2$ of $A_0$, while $\bar A_0$ has eigenvalues $-2i, \frac i2$. The 513 notes' form, on generators: an intertwiner commuting with the rotation generators $\frac12\sigma^k$ is a multiple of $\mathbb 1$ by Schur, and then the boost generators $\mp\frac i2\sigma^k$ of the two halves cannot match.)
>
> **5. Exactly two classes.** Equivalence is transitive, so $\{A, (A^{-1})^{\mathsf T}\}$ (step 2) and $\{\bar A, (A^\dagger)^{-1}\}$ (step 3) are each inside one class; by step 4 the two classes are different.
>
> **6. Index language (Yu §9.6.1).** Write a vector of the defining representation with a lower undotted index, $\eta'_a = A_a{}^b\eta_b$ (Yu (9.358)). Raising with $\varepsilon^{ab}$ (the matrix $\varepsilon$, Yu (9.360)), $\eta^a = \varepsilon^{ab}\eta_b$ transforms by $\varepsilon A\varepsilon^{-1} = (A^{-1})^{\mathsf T}$ (step 2; Yu (9.363)–(9.364)): an upper undotted index carries the dual. The conjugate $\eta^\dagger_{\dot a} = (\eta_a)^{\ast}$ transforms by $\bar A$ (Yu (9.376)): a lower dotted index; raising it with $\varepsilon^{\dot a\dot b}$ gives $(A^\dagger)^{-1}$ (step 3; Yu (9.380)–(9.381)). The contraction $\eta^a\zeta_a$ is invariant, $(A^{-1})^{\mathsf T}$ and $A$ pairing to $\mathbb 1$ (Yu (9.370)), and likewise for dotted indices. No equivalence connects the undotted pair with the dotted pair (step 4), so no index operation turns one kind into the other: $\varepsilon$ raises and lowers within each kind.
>
> **What the proof shows**
> - ⚑ By-product: $SL(2, \mathbb C)$ has two inequivalent two-dimensional representations, $(\frac12, 0)$ and $(0, \frac12)$, each self-dual via $\varepsilon$ and conjugate to the other; a Lorentz-invariant contraction pairs undotted with undotted or dotted with dotted, never mixed → [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-4|Theorem §C5a.5.4]].
> - For the subgroup $SU(2)$ all four coincide up to equivalence (Theorem §CB.7.15, 3): the distinction between dotted and undotted indices is invisible under rotations and appears only with boosts. Consistently, the trace test of step 4 is blind on $SU(2)$, where $\operatorname{tr}A = \alpha + \bar\alpha$ is real.
> - Conventions differ between sources (Dreiner–Haber–Martin raise with $\varepsilon^{12} = +1$ like Yu but put the lowered index on $\psi_\alpha$ transforming by $M$, as here); the equivalence classes do not depend on them.

^pf-cb-7-16

*Uses:* [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-6|Def. §CB.7.6]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-7|Def. §CB.7.7]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-15|Theorem §CB.7.15]]

The course's dotted and undotted indices and the invariant pairings are the component form of Theorems §CB.7.15–§CB.7.16, physics notation for the Weyl spinors: [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-2|Def. §C5a.5.2]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]] (its part 1 is Theorem §CB.7.15, 1, whose second proof above is the course's computation) and [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-4|Theorem §C5a.5.4]].

## Two-index tensors of the Lorentz group

Two facts about $V\otimes V$, $V = \mathbb R^{1,3}$, first written for spacetime tensors in [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] and restated here with their proofs (CB ordering pass, 2026-10-08), because the decomposition of two-index tensors into irreducible pieces ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.17]]) starts from them:

> [!theorem] Theorem §CB.7.17: The Trace, Symmetric and Antisymmetric Parts Do Not Mix
> Every two-tensor $T^{\mu\nu}$ on $V = \mathbb R^{1,3}$ splits uniquely as
>
> $$
> T^{\mu\nu} = \underbrace{\Bigl(T^{(\mu\nu)} - \tfrac14g^{\mu\nu}T^\rho{}_\rho\Bigr)}_{\text{symmetric traceless: }9} + \underbrace{T^{[\mu\nu]}}_{\text{antisymmetric: }6} + \underbrace{\tfrac14g^{\mu\nu}T^\rho{}_\rho}_{\text{trace: }1},
> $$
>
> $T^{(\mu\nu)} = \frac12(T^{\mu\nu} + T^{\nu\mu})$, $T^{[\mu\nu]} = \frac12(T^{\mu\nu} - T^{\nu\mu})$, and each of the three subspaces is mapped into itself by $\Lambda\otimes\Lambda$ for every $\Lambda \in O(1,3)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]; the tensor law of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-14|Theorem §CB.0.14]]).
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 ("Irreducible pieces of a two-tensor"), eq. (decomposition) · PHY 513 Lecture 1, Part C ("Irreducible parts of two-tensor representation") · the course's version: [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-5|Theorem §C1a.5.5]], the same statement.*

^thm-cb-7-17

> [!proof]- Proof
> *The derivation of Theorem §C1a.5.5, with the two facts it took from Relativity proved in place (steps 1–2) and the invariance of the metric cited from Theorem §CB.7.14.*
>
> **1. Symmetric and antisymmetric.** The split $T = T^{(\,)} + T^{[\,]}$ is unique: a tensor that is both symmetric and antisymmetric is $0$. A symmetric (antisymmetric) tensor stays so under every $\Lambda$: exchanging $\mu \leftrightarrow \nu$ in $\Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma T^{\rho\sigma}$ is the same as exchanging the dummies $\rho \leftrightarrow \sigma$, which turns $T^{\rho\sigma}$ into $T^{\sigma\rho} = \pm T^{\rho\sigma}$.
>
> **2. The trace is a scalar.** $g_{\mu\nu}T'^{\mu\nu} = g_{\mu\nu}\Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma T^{\rho\sigma} = g_{\rho\sigma}T^{\rho\sigma}$ by the defining condition $\Lambda^{\mathsf T}g\Lambda = g$ (Def. §CB.1.1); only the symmetric part contributes to it: $g_{\mu\nu}T^{[\mu\nu]} = g_{\nu\mu}T^{[\nu\mu]} = -g_{\mu\nu}T^{[\mu\nu]}$ (rename the dummies, then use the symmetry of $g$ and the antisymmetry of $T^{[\,]}$), so it vanishes.
>
> **3. Split off the trace.** Write $t = T^\rho{}_\rho$ and $S^{\mu\nu} = T^{(\mu\nu)} - \frac14g^{\mu\nu}t$. Then $g_{\mu\nu}S^{\mu\nu} = t - \frac14\cdot4\,t = 0$, using $g_{\mu\nu}g^{\mu\nu} = \delta^\mu{}_\mu = 4$. The trace part $\frac14g^{\mu\nu}t$ transforms to $\frac14g^{\mu\nu}t$ ($g^{\mu\nu}$ is invariant, [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-14|Theorem §CB.7.14]], 1; $t$ is a scalar by step 2). A traceless symmetric tensor stays symmetric (step 1) and traceless (step 2). Uniqueness: the trace part is fixed by $t$, the rest by step 1.
>
> **4. Count.** Symmetric: $4 + 6 = 10$ entries, minus one trace condition: $9$; antisymmetric: $6$; trace: $1$; total $16$.
>
> **What the proof shows**
> - The $16\times16$ matrix $\Lambda^\mu{}_\lambda\Lambda^\nu{}_\sigma$ is block diagonal in this basis: "symmetric and antisymmetric parts do not mix". That each piece is irreducible is representation theory ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-12|Theorem §CB.17.12]]).
> - Equivalence: this is [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-5|Theorem §C1a.5.5]]; the physics section identifies the six antisymmetric components with $\mathbf E$ and $\mathbf B$.

^pf-cb-7-17

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-14|Theorem §CB.0.14]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-14|Theorem §CB.7.14]]

> [!theorem] Theorem §CB.7.18: Duality Squares to −1 on Antisymmetric Tensors
> On antisymmetric $A^{\mu\nu}$ let $(\star A)^{\mu\nu} = \frac12\varepsilon^{\mu\nu\rho\sigma}A_{\rho\sigma}$, with $\varepsilon$ of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-16|Def. §CB.0.16]]. Then:
> 1. $\star\star A = -A$;
> 2. $\star(\Lambda A) = (\det\Lambda)\,\Lambda(\star A)$ for $\Lambda \in O(1,3)$: duality commutes with proper Lorentz transformations and anticommutes with $\mathcal P$ and $\mathcal T$;
> 3. over $\mathbb C$, the six-dimensional space is the direct sum of the eigenspaces $\star A = \pm iA$, each three-dimensional and mapped into itself by every $\Lambda$ with $\det\Lambda = 1$; $\mathcal P$ exchanges them.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Derivation "Contracting Levi-Civita symbols", four-dimensional example; "Irreducible pieces of a two-tensor") · the course's version: [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-6|Theorem §C1a.5.6]], the same statement.*

^thm-cb-7-18

> [!proof]- Proof
> *The derivation of Theorem §C1a.5.6 with the citations replaced (the pseudotensor law is Theorem §CB.7.14, 2; the contraction identity Theorem §CB.0.17).*
>
> **1. Lower the dual.** $(\star A)_{\rho\sigma} = g_{\rho\kappa}g_{\sigma\lambda}\frac12\varepsilon^{\kappa\lambda\alpha\beta}A_{\alpha\beta} = \frac12\varepsilon_{\rho\sigma}{}^{\alpha\beta}A_{\alpha\beta} = \frac12\varepsilon_{\rho\sigma\alpha\beta}A^{\alpha\beta}$: moving the contracted pair $\alpha\beta$ down on $\varepsilon$ and up on $A$ leaves the sum unchanged, because $g^{\alpha\gamma}g_{\gamma\delta} = \delta^\alpha{}_\delta$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]]).
>
> **2. Apply twice.** $(\star\star A)^{\mu\nu} = \frac12\varepsilon^{\mu\nu\rho\sigma}(\star A)_{\rho\sigma} = \frac14\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\rho\sigma\alpha\beta}A^{\alpha\beta}$.
>
> **3. Bring the contracted pair to the front.** $\varepsilon^{\mu\nu\rho\sigma} = \varepsilon^{\rho\sigma\mu\nu}$: the permutation $(\mu\nu\rho\sigma) \to (\rho\sigma\mu\nu)$ is the product of the transpositions of the first with the third slot and the second with the fourth, even.
>
> **4. Contract.** By [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-17|Theorem §CB.0.17]], 1 (two contracted pairs, upper and lower roles exchanged, which is the same identity), $\varepsilon^{\rho\sigma\mu\nu}\varepsilon_{\rho\sigma\alpha\beta} = -2(\delta^\mu_\alpha\delta^\nu_\beta - \delta^\mu_\beta\delta^\nu_\alpha)$. So $(\star\star A)^{\mu\nu} = -\frac12(A^{\mu\nu} - A^{\nu\mu}) = -A^{\mu\nu}$, by antisymmetry. ⚑ By-product: the $-1$ is $\det g$ again; in Euclidean four dimensions $\star\star = +1$ and the eigenvalues are real (self-dual and anti-self-dual forms) → part 3.
>
> **5. Part 2.** Multiply the pseudotensor law $\Lambda^\mu{}_\kappa\Lambda^\nu{}_\lambda\Lambda^\rho{}_\alpha\Lambda^\sigma{}_\beta\varepsilon^{\kappa\lambda\alpha\beta} = \det\Lambda\,\varepsilon^{\mu\nu\rho\sigma}$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-14|Theorem §CB.7.14]], 2) by $\Lambda_\rho{}^\gamma\Lambda_\sigma{}^\delta$ and use $\Lambda^\rho{}_\alpha\Lambda_\rho{}^\gamma = \delta_\alpha{}^\gamma$ ($\Lambda_\rho{}^\gamma = (\Lambda^{-1})^\gamma{}_\rho$, [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-13|Theorem §CB.0.13]], 2): $\Lambda^\mu{}_\kappa\Lambda^\nu{}_\lambda\varepsilon^{\kappa\lambda\gamma\delta} = \det\Lambda\,\varepsilon^{\mu\nu\rho\sigma}\Lambda_\rho{}^\gamma\Lambda_\sigma{}^\delta$. With $(\Lambda A)_{\rho\sigma} = \Lambda_\rho{}^\gamma\Lambda_\sigma{}^\delta A_{\gamma\delta}$ and $(\det\Lambda)^2 = 1$:
>
> $$
> (\star\Lambda A)^{\mu\nu} = \tfrac12\varepsilon^{\mu\nu\rho\sigma}\Lambda_\rho{}^\gamma\Lambda_\sigma{}^\delta A_{\gamma\delta} = \det\Lambda\;\Lambda^\mu{}_\kappa\Lambda^\nu{}_\lambda\,\tfrac12\varepsilon^{\kappa\lambda\gamma\delta}A_{\gamma\delta} = \det\Lambda\;(\Lambda\star A)^{\mu\nu} .
> $$
>
> **6. Part 3.** $\star$ is a real linear map with $\star^2 = -1$, so over $\mathbb C$ its eigenvalues are $\pm i$ and $A = \frac12(A - i\star A) + \frac12(A + i\star A)$ splits $A$ into a $(+i)$- and a $(-i)$-eigenvector (check: $\star(A - i\star A) = \star A + iA = i(A - i\star A)$). Complex conjugation commutes with the real map $\star$ and exchanges the two eigenspaces, so they have equal dimension, $6/2 = 3$. A $\Lambda$ with $\det\Lambda = 1$ commutes with $\star$ (part 2), hence preserves each eigenspace; $\mathcal P$ anticommutes, hence sends $\star A = iA$ to $\star(\mathcal PA) = -i\mathcal PA$.
>
> **What the proof shows**
> - Taking the dual twice returns $-A$, not $A$: the Minkowski sign.
> - The two three-dimensional halves are, as representations, $(1, 0)$ and $(0, 1)$ ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-11|Theorem §CB.17.11]]); for the field tensor they are built from $\mathbf E \pm i\mathbf B$ (the course's [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]]).
> - Equivalence: this is [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-6|Theorem §C1a.5.6]] with its derivation.

^pf-cb-7-18

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-16|Def. §CB.0.16]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-17|Theorem §CB.0.17]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-13|Theorem §CB.0.13]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-14|Theorem §CB.7.14]]

> [!remark]- Connections
> - Theorem §CB.7.8 is why complex conjugation and parity both exchange $(j_+, j_-) \leftrightarrow (j_-, j_+)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-10|Theorem §CB.16.10]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-11|Theorem §CB.16.11]]): conjugation acts on the algebra through $c$, parity through an automorphism; both swap $\mathfrak a_+$ and $\mathfrak a_-$.
> - Theorem §CB.7.13, 3 with $A = S^+$, $B = S^-$ is the decomposition of two-forms into self-dual and anti-self-dual parts (§CB.17; [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]]).
> - **Used in**: Definitions §CB.7.1–Theorem §CB.7.3 — [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-14|Theorem §CB.0.14]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-5|Theorem §C3.3.5]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|Theorem §C3.3.6]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-8|Theorem §C3.6.8]]; Theorem §CB.7.5 — [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-3|Theorem §CB.16.3]]; Definitions §CB.7.6–Theorem §CB.7.8 — [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-11|Theorem §CB.16.11]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-6|Def. §CB.0.6]], [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-2|Def. §C5a.5.2]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]; Theorem §CB.7.9 — [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-10|Theorem §CB.0.10]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]]; Theorem §CB.7.13 — [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-5|Theorem §C1a.5.5]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-12|Theorem §CB.17.12]]; Theorem §CB.7.14 — [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|Theorem §C1a.5.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]]; Theorem §CB.7.15 — [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (embedded; cited in [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]]); Theorems §CB.7.15–§CB.7.16 — [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-4|Theorem §C5a.5.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]; Theorem §CB.7.16 — [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (embedded).
