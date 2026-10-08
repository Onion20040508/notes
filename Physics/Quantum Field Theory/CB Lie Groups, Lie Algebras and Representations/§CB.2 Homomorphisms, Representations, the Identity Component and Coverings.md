---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification]] →

*Sources (proofs written from these, each checked against the text): B. C. Hall, An Elementary Introduction to Groups and Representations, Chs. 2–5 (https://arxiv.org/abs/math-ph/0005032) · E. Meinrenken, Lie Groups and Lie Algebras, lecture notes, Toronto, Winter 2026, §§2.2, 2.5–2.6, 4 (https://www.math.toronto.edu/mein/teaching/LectureNotes/lie.pdf) · J. M. Lee, Introduction to Smooth Manifolds, 2nd ed., Props. 7.11, 8.41, 8.48, Thms. 8.46, 21.31 · Zuoqin Wang, Lie Groups (USTC), Lecture 12 · P. Etingof, Lie Groups and Lie Algebras (MIT 18.755), Prop. 3.15 · Differentiable Manifolds (591) §§11, 16, 25, 33, 35, 49–50 · the user's PHY 513 notes, Ch. 7 §7.2 · Yu Zhao-Huan, 量子场论讲义, §3.2 · Peskin & Schroeder, §3.1 · P. Woit, Quantum Theory, Groups and Representations, Ch. 5 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf).*

How does a homomorphism of matrix Lie groups act on their Lie algebras, which part of a group do exponentials reach, and when is a homomorphism of Lie algebras the differential of a homomorphism of groups? This section continues [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras|§CB.1]] (the matrix exponential, one-parameter subgroups, the Lie algebra of a matrix Lie group) with homomorphisms and their differentials, the identity component, the adjoint representation, coverings and the Lie correspondence: the theorems behind SU(2) → SO(3) and SL(2,ℂ) → SO⁺(1,3), and behind every statement of the physics chapters that a representation may be checked on generators. The course's definitions of representations of groups and Lie algebras, of equivalence and of irreducibility, and its exponential formula for representations ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]]), are stated here, where they are first needed. Statements are numbered in reading order with one counter per section (Definition §CB.2.1, …); boxes shown as embeds keep their home numbers.

## Homomorphisms and their differentials

> [!definition] Definition §CB.2.1: Lie Group Homomorphism
> A **Lie group homomorphism** between matrix Lie groups $G$ and $H$ is a continuous group homomorphism $\Phi : G \to H$ ([[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]). It is an **isomorphism of Lie groups** if it is bijective and $\Phi^{-1}$ is continuous.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 2 §6, Def. 2.13*

^def-cb-2-1

> [!definition] Definition §CB.2.2: Lie Algebra Homomorphism
> A **Lie algebra homomorphism** between real Lie algebras $\mathfrak g$ and $\mathfrak h$ ([[§49 Lie Bracket and Lie Algebra#^def-49-2|591 Def. §49.2]]) is a real-linear map $\varphi : \mathfrak g \to \mathfrak h$ with $\varphi([X, Y]) = [\varphi(X), \varphi(Y)]$ for all $X, Y$. A bijective one is an **isomorphism**, written $\mathfrak g \cong \mathfrak h$. (For complex Lie algebras, [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-1|Def. §CB.3.1]], the same words with complex-linear maps.)
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §8, Def. 3.29*

^def-cb-2-2

> [!theorem] Theorem §CB.2.3: The Differential of a Homomorphism
> Let $\Phi : G \to H$ be a Lie group homomorphism ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]]). There is a unique real-linear map $\varphi = \Phi_\ast : \mathfrak g \to \mathfrak h$, the **differential** of $\Phi$, with
>
> $$
> \Phi(e^{X}) = e^{\varphi(X)} \quad (X \in \mathfrak g), \qquad \varphi(X) = \frac{d}{ds}\Phi(e^{sX})\Big|_{s=0} .
> $$
>
> Moreover $\varphi$ is a Lie algebra homomorphism ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-2|Def. §CB.2.2]]), $\varphi(gXg^{-1}) = \Phi(g)\varphi(X)\Phi(g)^{-1}$, and $(\Psi\circ\Phi)_\ast = \Psi_\ast\circ\Phi_\ast$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §6, Thm. 3.18 (Steps 1–8 of its proof) · Woit, §5.4*

^thm-cb-2-3

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §6, Thm. 3.18 and its proof, Steps 1–8 (https://arxiv.org/abs/math-ph/0005032), followed step by step.*
>
> **Step 1** (definition of $\varphi$). Fix $X \in \mathfrak g$. Since $sX$ and $tX$ commute, $e^{(s+t)X} = e^{sX}e^{tX}$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-3|Theorem §CB.1.3]], 3), and $\Phi$ is a continuous homomorphism; so $s \mapsto \Phi(e^{sX})$ is a one-parameter subgroup of $GL(n', \mathbb C)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-7|Def. §CB.1.7]]). By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]] there is a unique matrix $Z$ with $\Phi(e^{sX}) = e^{sZ}$ for all $s$, namely $Z = \frac{d}{ds}\Phi(e^{sX})|_{s=0}$. Since $e^{sZ} = \Phi(e^{sX}) \in H$ for all $s$, $Z \in \mathfrak h$. Define $\varphi(X) = Z$. Then
>
> $$
> \Phi(e^{sX}) = e^{s\varphi(X)} \quad (s \in \mathbb R), \qquad \varphi(X) = \frac{d}{ds}\Phi(e^{sX})\Big|_{s=0},
> $$
>
> and $s = 1$ gives $\Phi(e^X) = e^{\varphi(X)}$.
>
> **Step 2** (real homogeneity). For $a \in \mathbb R$: $\Phi(e^{s(aX)}) = \Phi(e^{(sa)X}) = e^{sa\varphi(X)} = e^{s(a\varphi(X))}$, so by uniqueness in Step 1, $\varphi(aX) = a\varphi(X)$.
>
> **Step 3** (additivity, by the Lie product formula). By Step 1, then [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-6|Theorem §CB.1.6]], 1, then continuity and the homomorphism property of $\Phi$, then Step 1 again:
>
> $$
> e^{s\varphi(X + Y)} = \Phi\bigl(e^{s(X + Y)}\bigr) = \Phi\Bigl(\lim_{m\to\infty}\bigl(e^{sX/m}e^{sY/m}\bigr)^m\Bigr) = \lim_{m\to\infty}\bigl(\Phi(e^{sX/m})\Phi(e^{sY/m})\bigr)^m = \lim_{m\to\infty}\bigl(e^{s\varphi(X)/m}e^{s\varphi(Y)/m}\bigr)^m ,
> $$
>
> and the last limit is $e^{s(\varphi(X) + \varphi(Y))}$ by Theorem §CB.1.6, 1 once more. Differentiating $e^{s\varphi(X + Y)} = e^{s(\varphi(X) + \varphi(Y))}$ at $s = 0$ gives $\varphi(X + Y) = \varphi(X) + \varphi(Y)$. With Step 2, $\varphi$ is real-linear.
>
> **Step 4** (uniqueness of $\varphi$). If $\psi : \mathfrak g \to \mathfrak h$ is real-linear with $\Phi(e^X) = e^{\psi(X)}$ for all $X$, then $e^{s\psi(X)} = e^{\psi(sX)} = \Phi(e^{sX})$, and differentiating at $s = 0$ gives $\psi(X) = \frac{d}{ds}\Phi(e^{sX})|_0 = \varphi(X)$.
>
> **Step 5** (conjugation). For $g \in G$, $X \in \mathfrak g$: $gXg^{-1} \in \mathfrak g$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]], 2), and by Step 1 and Theorem §CB.1.3, 4,
>
> $$
> e^{s\varphi(gXg^{-1})} = \Phi\bigl(e^{s\,gXg^{-1}}\bigr) = \Phi(g\,e^{sX}g^{-1}) = \Phi(g)\,e^{s\varphi(X)}\,\Phi(g)^{-1} = e^{s\,\Phi(g)\varphi(X)\Phi(g)^{-1}} .
> $$
>
> Differentiating at $s = 0$: $\varphi(gXg^{-1}) = \Phi(g)\varphi(X)\Phi(g)^{-1}$.
>
> **Step 6** (brackets). $[X, Y] = \frac{d}{dt}(e^{tX}Ye^{-tX})|_{t=0}$ (Step 5 of the proof of Theorem §CB.1.10), and the curve $t \mapsto e^{tX}Ye^{-tX}$ lies in $\mathfrak g$. A linear map on a finite-dimensional space is continuous, so it commutes with $\frac{d}{dt}$; using Step 5 with $g = e^{tX}$ and $\Phi(e^{tX}) = e^{t\varphi(X)}$:
>
> $$
> \varphi([X, Y]) = \frac{d}{dt}\varphi\bigl(e^{tX}Ye^{-tX}\bigr)\Big|_{t=0} = \frac{d}{dt}\Bigl(e^{t\varphi(X)}\varphi(Y)e^{-t\varphi(X)}\Bigr)\Big|_{t=0} = \varphi(X)\varphi(Y) - \varphi(Y)\varphi(X) .
> $$
>
> So $\varphi$ is a Lie algebra homomorphism ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-2|Def. §CB.2.2]]).
>
> **Step 7** (composition). For $\Psi : H \to K$: $(\Psi\circ\Phi)(e^{sX}) = \Psi(e^{s\Phi_\ast(X)}) = e^{s\Psi_\ast(\Phi_\ast(X))}$, so by uniqueness (Step 1 for $\Psi\circ\Phi$), $(\Psi\circ\Phi)_\ast = \Psi_\ast\circ\Phi_\ast$.
>
> **What the proof shows.**
> - Continuity of $\Phi$ is all that is assumed; Theorem §CB.1.8 supplies the derivatives. In the language of 591, $\varphi$ is the differential of $\Phi$ at $\mathbb 1$ (Step 1's formula).
> - ⚑ By-product: the structure constants of $\mathfrak h$ restricted to the image are those of $\mathfrak g$; for $H = GL(W)$ this is "every representation realizes the same algebra" ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], whose derivation is the special case).
> - The converse, from algebra homomorphisms to group homomorphisms, needs connectedness for uniqueness (Theorem §CB.2.11) and simple connectivity for existence (Theorem §CB.2.18).

^pf-cb-2-3

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-7|Def. §CB.1.7]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-2|Def. §CB.2.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-3|Theorem §CB.1.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-6|Theorem §CB.1.6]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]]

A representation is a homomorphism into $GL(W)$. The course's definitions (PHY 513 Lecture 7, Part A; the user's PHY 513 notes, Ch. 7 §7.2), and its theorem that a group representation gives an algebra representation, the case $H = GL(W)$ of Theorem §CB.2.3:

> [!definition] Definition §CB.2.4: Representation of a Group
> A **representation** of a matrix Lie group $G$ on a complex vector space $W$, the **carrier space**, is a continuous homomorphism $D : G \to GL(W)$: $D(gh) = D(g)D(h)$, $D(\mathbb 1) = \mathbb 1$. Its **dimension** is $\dim W$; it is **faithful** if injective.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Definition "Group, algebra, representation", "Representations") · PHY 513 Lecture 7 ("Representations of angular momentum", "Representations of the rotation group") · PS §3.1, eq. (3.10) · Hall, Defs. 16.35–16.36 · Georgi §1.1, (1.B.1)–(1.B.2) · [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-7|493 Def. §20.7]]*

^def-cb-2-4

> [!definition] Definition §CB.2.5: Representation of a Lie Algebra
> A **representation of the Lie algebra** $\mathfrak g$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-9|Def. §CB.1.9]]) on a complex vector space $W$ is a real-linear map $d : \mathfrak g \to \operatorname{End}(W)$ with $d([X, Y]) = [d(X), d(Y)]$; in physicist's form, matrices $D(T_a) \equiv i\,d(-iT_a)$ with $[D(T_a), D(T_b)] = if_{ab}{}^cD(T_c)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|Def. §CB.1.11]]; for rotations: three matrices obeying $[J^i, J^j] = i\varepsilon^{ijk}J^k$). Its dimension is $\dim W$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Definition "Group, algebra, representation", "Representations") · PHY 513 Lecture 7 ("Representations of angular momentum", "Representations of the rotation group") · PS §3.1, eq. (3.10) · Hall, Defs. 16.35–16.36 · Georgi §1.1, (1.B.1)–(1.B.2) · [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-7|493 Def. §20.7]]*

^def-cb-2-5

> [!definition] Definition §CB.2.6: Equivalent Representations
> Let $D$, $D'$ be representations (of a group, [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-4|Def. §CB.2.4]], or of an algebra, [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-5|Def. §CB.2.5]]) on $W$, $W'$. They are **equivalent** if $D'(g) = S\,D(g)\,S^{-1}$ for one fixed invertible $S : W \to W'$: they differ by a change of basis.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Definition, "Equivalence and reducibility") · Georgi §1.4, eqs. (1.10)–(1.14) · Hall, Defs. 16.37–16.38, 16.48, 16.50, Prop. 16.42*

^def-cb-2-6

> [!definition] Definition §CB.2.7: Invariant Subspace; Irreducible Representation
> Let $D$ be a representation on $W$. An **invariant subspace** is a subspace $U \subset W$ with $D(g)U \subset U$ for all $g$ ([[§14 Invariant Subspaces#^ladr-5-2|LADR Def. 5.2]], for all operators at once). $D$ is **irreducible** if $W \ne 0$ and the only invariant subspaces are $0$ and $W$; otherwise **reducible**.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Definition, "Equivalence and reducibility") · Georgi §1.4, eqs. (1.10)–(1.14) · Hall, Defs. 16.37–16.38, 16.48, 16.50, Prop. 16.42*

^def-cb-2-7

> [!theorem] Theorem §CB.2.8: A Group Representation Gives an Algebra Representation
> Let $D : G \to GL(W)$ be a finite-dimensional representation of a matrix Lie group. Then:
> 1. $d(X) = \frac{d}{ds}D(e^{sX})\big|_{s=0}$ is a representation of $\mathfrak g$ on $W$, and $D(e^X) = e^{d(X)}$; in physicist's form $D(e^{-i\theta^aT_a}) = e^{-i\theta^aD(T_a)}$, and the $D(T_a)$ obey the algebra **with the same structure constants** as the $T_a$;
> 2. if $G$ is connected, $D$ is determined by $d$; a subspace is invariant under all $D(g)$ iff under all $d(X)$; and two representations are equivalent ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-6|Def. §CB.2.6]]) iff their algebra representations are.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 ("Exponentiation turns the first into the second near the identity") · PHY 513 Lecture 7 ("All representations realize the abstract algebra") · Yu §3.2, below eq. (3.36) · PS §3.1, p. 39 · Hall, Thm. 16.23, Prop. 16.39 · Georgi §2.2*

^thm-cb-2-8

> [!derivation]- Derivation
> Assume $D$ is smooth (for a continuous homomorphism of matrix Lie groups this is automatic, Hall Thm. 16.23).
>
> **1. A one-parameter group.** Fix $X \in \mathfrak g$ and set $F(s) = D(e^{sX})$. Since $sX$ and $tX$ commute, $e^{(s+t)X} = e^{sX}e^{tX}$, and the homomorphism property gives $F(s+t) = F(s)F(t)$, $F(0) = \mathbb 1$.
>
> **2. It is an exponential.** Differentiate $F(s+t) = F(s)F(t)$ in $t$ at $t = 0$: $F'(s) = F(s)\,d(X)$ with $d(X) \equiv F'(0)$. The linear matrix equation $F' = F\,d(X)$, $F(0) = \mathbb 1$, has the unique solution $F(s) = e^{s\,d(X)}$; at $s = 1$, $D(e^X) = e^{d(X)}$. ⚑ By-product: the exponential form of a represented group element is forced by the group law, not chosen → [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], 1.
>
> **3. Linearity.** $d(X) = \frac{d}{ds}D(\gamma(s))|_{0}$ with $\gamma(s) = e^{sX}$, $\gamma(0) = \mathbb 1$, $\gamma'(0) = X$; by the chain rule ([[Chain Rule for Differentials|591, Chain rule for differentials]]) $d(X) = dD_{\mathbb 1}(X)$, the differential of $D$ at $\mathbb 1$ applied to $X$, which is linear in $X$.
>
> **4. Compatibility with conjugation.** For $g \in G$ and $Y \in \mathfrak g$, $ge^{tY}g^{-1} = e^{t\,gYg^{-1}}$ (insert $g^{-1}g$ between the factors of each power in the exponential series), and $gYg^{-1} \in \mathfrak g$ (Hall Prop. 16.20; [[§25 The Geometric Tangent Space#^prop-25-6|591 Prop. §25.6]]). Apply $D$ and use step 2 on both sides:
>
> $$
> e^{t\,d(gYg^{-1})} = D(e^{t\,gYg^{-1}}) = D(g)\,D(e^{tY})\,D(g)^{-1} = D(g)\,e^{t\,d(Y)}\,D(g)^{-1} .
> $$
>
> Differentiate at $t = 0$: $d(gYg^{-1}) = D(g)\,d(Y)\,D(g)^{-1}$.
>
> **5. Brackets.** Put $g = e^{sX}$ in step 4: $d(e^{sX}Ye^{-sX}) = e^{s\,d(X)}\,d(Y)\,e^{-s\,d(X)}$. Differentiate at $s = 0$. On the left, $d$ is linear on the finite-dimensional space $\mathfrak g$, hence continuous, so it commutes with $d/ds$; and $\frac{d}{ds}(e^{sX}Ye^{-sX})|_0 = XY - YX$ (product rule, both terms). On the right the same product rule gives $d(X)d(Y) - d(Y)d(X)$. Hence $d([X, Y]) = [d(X), d(Y)]$: $d$ is a Lie-algebra representation.
>
> **6. Physicist's form.** With $X_a = -iT_a$ and $D(T_a) \equiv i\,d(X_a)$, linearity gives $d(-i\theta^aT_a) = \theta^a d(X_a) = -i\theta^aD(T_a)$, so $D(e^{-i\theta^aT_a}) = e^{-i\theta^aD(T_a)}$ by step 2. From $[X_a, X_b] = f_{ab}{}^cX_c$ and step 5, $[D(T_a), D(T_b)] = i^2[d(X_a), d(X_b)] = -f_{ab}{}^c\,d(X_c) = if_{ab}{}^c\,D(T_c)$. ⚑ By-product: the structure constants are the same in every representation; they belong to the group, not to the representation. This is the precise content of "all representations realize the abstract algebra" (Lecture 7), and why [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-2|Theorem §CB.4.2]] holds in every representation once it holds in one faithful one → [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], 1.
>
> **7. Connected groups.** Every element of a connected matrix Lie group is a product of exponentials (Hall Cor. 16.28); for $SO(3)$ and $SU(2)$ every element is a single exponential ($R(\hat n, \theta)$, and [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-5|QM Theorem §C5.2.5]], 3). So $D(e^{X_1}\cdots e^{X_k}) = e^{d(X_1)}\cdots e^{d(X_k)}$ is fixed by $d$. If a subspace $U \subset W$ is invariant under every $d(X)$, it is invariant under every power and hence under $e^{d(X)} = \sum_n d(X)^n/n!$ (a subspace of a finite-dimensional space is closed, so the limit of the partial sums stays in it), hence under every $D(g)$. Conversely, if $U$ is invariant under every $D(g)$, it is invariant under $d(X) = \lim_{s\to0}(D(e^{sX}) - \mathbb 1)/s$. The same two arguments applied to $S D_1(g) = D_2(g) S$ and $S d_1(X) = d_2(X) S$ show that a fixed invertible $S$ intertwines the group representations iff it intertwines the algebra representations.
>
> **What the derivation shows**
> - Only the group law and smoothness are used; nothing about unitarity or a Hilbert space.
> - The converse, from an algebra representation to a group representation, is *not* automatic: exponentials of $d(X)$ may fail to respect the global identifications of $G$ ($e^{2\pi X} = \mathbb 1$ in $G$ but $e^{2\pi d(X)} \ne \mathbb 1$). It holds when $G$ is simply connected → [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-7|Theorem §CB.9.7]].
> - Finite dimension is used in steps 2, 5 and 7. On an infinite-dimensional Hilbert space the generators of a unitary representation are unbounded self-adjoint operators defined on a dense domain (Stone's theorem; Hall §16.9.1) → [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra|§C3.4]].
> - Used next: the Lorentz version, generators of an arbitrary representation and their tensor law → [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-1|Def. §CB.4.1]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-4|Theorem §CB.4.4]].

^der-cb-2-8

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-9|Def. §CB.1.9]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-4|Def. §CB.2.4]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-5|Def. §CB.2.5]], [[Chain Rule for Differentials|591, Chain rule for differentials]], [[§25 The Geometric Tangent Space#^prop-25-6|591 Prop. §25.6]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-5|QM Theorem §C5.2.5]]

## The identity component

> [!definition] Definition §CB.2.9: Identity Component
> The **identity component** $G_0$ of a matrix Lie group $G$ is the set of $g \in G$ that can be joined to $\mathbb 1$ by a continuous path in $G$. $G$ is **connected** if $G_0 = G$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 2 §4, Def. 2.5, Prop. 2.6 · 591 §16*

^def-cb-2-9

> [!theorem] Theorem §CB.2.10: The Identity Component Is Generated by Exponentials
> Let $G$ be a matrix Lie group with Lie algebra $\mathfrak g$ and identity component $G_0$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-9|Def. §CB.2.9]]).
> 1. $G_0$ is a normal subgroup of $G$ ([[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]]), open and closed in $G$, and its cosets are the path components of $G$.
> 2. $e^X \in G_0$ for every $X \in \mathfrak g$.
> 3. Every $g \in G_0$ is a finite product $g = e^{X_1}e^{X_2}\cdots e^{X_k}$ with $X_i \in \mathfrak g$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 2 §4, Prop. 2.6; Ch. 3, Prop. 3.14, Cor. 3.26 · Lee, Introduction to Smooth Manifolds, Lemma 7.12, Prop. 7.15 · the Lorentz case: [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]]*

^thm-cb-2-10

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Prop. 2.6 (subgroup), Prop. 3.14 (part 2), Cor. 3.26 (part 3) with proofs (https://arxiv.org/abs/math-ph/0005032) · J. M. Lee, Introduction to Smooth Manifolds, 2nd ed., Lemma 7.12 and Prop. 7.15 (normal, open and closed, cosets as components), whose arguments Steps 2 and 4 follow.*
>
> **Step 1** (subgroup; Hall, Prop. 2.6). Let $g, h \in G_0$ with paths $a(t)$, $b(t)$ in $G$ from $\mathbb 1$ to $g$, $h$ ($0 \le t \le 1$). Multiplication and inversion of matrices are continuous, so $a(t)b(t)$ is a path in $G$ from $\mathbb 1$ to $gh$, and $a(t)^{-1}$ a path from $\mathbb 1$ to $g^{-1}$. So $gh, g^{-1} \in G_0$; and $\mathbb 1 \in G_0$ (constant path).
>
> **Step 2** (normal). For $k \in G$ and $g \in G_0$ with path $a(t)$, $ka(t)k^{-1}$ is a path in $G$ from $\mathbb 1$ to $kgk^{-1}$. So $kG_0k^{-1} \subset G_0$ ([[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]]).
>
> **Step 3** (part 2; Hall, Prop. 3.14). For $X \in \mathfrak g$, $s \mapsto e^{sX}$, $0 \le s \le 1$, is a continuous path in $G$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-3|Theorem §CB.1.3]], 1, and the definition of $\mathfrak g$) from $\mathbb 1$ to $e^X$. So $e^X \in G_0$.
>
> **Step 4** (open and closed). By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-13|Theorem §CB.1.13]] there is a neighbourhood $V = \exp(U \cap \mathfrak g)$ of $\mathbb 1$, open in $G$, and $V \subset G_0$ by Step 3. Left multiplication by $k \in G$ is a homeomorphism of $G$ (continuous, with continuous inverse multiplication by $k^{-1}$), so $kV$ is open. For $g \in G_0$, $gV \subset G_0$ (Step 1) is an open set containing $g$: $G_0$ is open. Every coset $kG_0$ is open for the same reason. The cosets partition $G$, so $G \setminus G_0$ is the union of the cosets other than $G_0$, which is open: $G_0$ is closed.
>
> **Step 5** (cosets are the path components). $k' \in G$ can be joined to $k$ by a path $c(t)$ in $G$ iff $k^{-1}c(t)$ is a path from $\mathbb 1$ to $k^{-1}k'$, i.e. iff $k^{-1}k' \in G_0$, i.e. iff $k' \in kG_0$. So the path component of $k$ is $kG_0$.
>
> **Step 6** (part 3; Hall, Cor. 3.26). Let $E \subset G_0$ be the set of finite products $e^{X_1}\cdots e^{X_k}$, $X_i \in \mathfrak g$ ($E \subset G_0$ by Steps 1 and 3). $E \supset V \ni \mathbb 1$, so $E \ne \varnothing$. *$E$ is open:* for $A \in E$, $AV$ is an open neighbourhood of $A$, and each $Ae^X$ ($e^X \in V$) is again a finite product of exponentials. *$E$ is closed in $G_0$:* if $A \in G_0$ and $A_m \to A$ with $A_m \in E$, then $A_m^{-1}A \to \mathbb 1$, so $A_m^{-1}A \in V$ for some $m$, i.e. $A_m^{-1}A = e^X$ with $X \in \mathfrak g$, and $A = A_me^X \in E$. $G_0$ is path-connected (every point is joined to $\mathbb 1$), hence connected ([[§16 Connected Subspaces of ℝ#^thm-16-4|590 Thm. §16.4]]), so the nonempty open and closed subset $E$ is all of $G_0$ ([[§15 Connected Spaces#^def-15-2|590 Def. §15.2]]).
>
> **What the proof shows.**
> - $G/G_0$ is the group of components; for the Lorentz group it is $\{\pm1\}^2$ ([[§C1a.4 The Lorentz Group#^thm-c1a-4-2|Theorem §C1a.4.2]]), and no exponential leaves $G_0$: $P$ and $T$ are not of the form $e^X$.
> - ⚑ By-product: a single exponential need not suffice (for $SL(2, \mathbb R)$ some elements are not exponentials; Meinrenken, Exercise 4.18), which is why part 3 allows products; for $SO(3)$, $SU(2)$ and $SO^+(1,3)$ one or two factors are enough ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]]).
> - Used next: Theorems §CB.2.11 and §CB.2.17 check statements on exponentials and extend them to $G_0$ by part 3.

^pf-cb-2-10

*Uses:* [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-9|Def. §CB.2.9]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-3|Theorem §CB.1.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-13|Theorem §CB.1.13]], [[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]], [[§16 Connected Subspaces of ℝ#^thm-16-4|590 Thm. §16.4]], [[§15 Connected Spaces#^def-15-2|590 Def. §15.2]]

The Lorentz group's components and its exponentials, proved in [[§C1a.4 The Lorentz Group|§C1a.4]] and [[§C1a.6 Infinitesimal Lorentz Transformations and Generators|§C1a.6]]:

![[§C1a.4 The Lorentz Group#^thm-c1a-4-3]]

![[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4]]

> [!theorem] Theorem §CB.2.11: A Homomorphism of a Connected Group Is Determined by Its Differential
> Let $G$ be connected and $\Phi, \Psi : G \to H$ Lie group homomorphisms with $\Phi_\ast = \Psi_\ast$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]). Then $\Phi = \Psi$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 5 §8, Thm. 5.33, 1 (Step 1 of its proof)*

^thm-cb-2-11

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 5 §8, Thm. 5.33, part 1, Step 1 of the proof (https://arxiv.org/abs/math-ph/0005032).*
>
> **Step 1** (products of exponentials). $G$ is connected, so $G = G_0$, and every $g \in G$ is $g = e^{X_1}\cdots e^{X_k}$ with $X_i \in \mathfrak g$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]], 3).
>
> **Step 2** (apply both homomorphisms). By the homomorphism property and [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]],
>
> $$
> \Phi(g) = \Phi(e^{X_1})\cdots\Phi(e^{X_k}) = e^{\Phi_\ast(X_1)}\cdots e^{\Phi_\ast(X_k)} = e^{\Psi_\ast(X_1)}\cdots e^{\Psi_\ast(X_k)} = \Psi(e^{X_1})\cdots\Psi(e^{X_k}) = \Psi(g),
> $$
>
> the middle equality by $\Phi_\ast = \Psi_\ast$.
>
> **What the proof shows.**
> - Connectedness is essential: on $O(1,3)$ the identity map and $\Lambda \mapsto \det(\Lambda)\Lambda$ have the same differential but differ on $P$.
> - For $H = GL(W)$ this is the uniqueness half of "a representation of a connected group is fixed by its generators" ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], 2).

^pf-cb-2-11

*Uses:* [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]]

## The adjoint representation

591 defines the adjoint action for four classical groups:

![[§25 The Geometric Tangent Space#^def-25-2]]

> [!definition] Definition §CB.2.12: Adjoint Representation of a Group
> For a matrix Lie group $G$ with Lie algebra $\mathfrak g$, the **adjoint representation** is $\mathrm{Ad} : G \to GL(\mathfrak g)$, $\mathrm{Ad}_g(X) = gXg^{-1}$, a representation on the real vector space $\mathfrak g$ (well defined by [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]], 2).
>
> *Source: 591 Def. §25.2, Prop. §25.6 · Hall, An Elementary Introduction to Groups and Representations, Ch. 3, Def. 3.19, Prop. 3.20*

^def-cb-2-12

> [!definition] Definition §CB.2.13: Adjoint Representation of a Lie Algebra
> For a Lie algebra $\mathfrak g$, $\mathrm{ad} : \mathfrak g \to \operatorname{End}(\mathfrak g)$ is $\mathrm{ad}_X(Y) = [X, Y]$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §8, Def. 3.32*

^def-cb-2-13

> [!theorem] Theorem §CB.2.14: The Differential of Ad Is ad
> 1. $\mathrm{ad}$ is a Lie algebra homomorphism $\mathfrak g \to \mathfrak{gl}(\mathfrak g)$: $\mathrm{ad}_{[X, Y]} = [\mathrm{ad}_X, \mathrm{ad}_Y]$ (the Jacobi identity).
> 2. $\mathrm{Ad}$ is a Lie group homomorphism and $\mathrm{Ad}_\ast = \mathrm{ad}$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]).
> 3. $e^XYe^{-X} = e^{\mathrm{ad}_X}Y = Y + [X, Y] + \frac1{2!}[X, [X, Y]] + \cdots$ for $X, Y \in \mathfrak g$.
> 4. $\mathrm{Ad}_g[X, Y] = [\mathrm{Ad}_gX, \mathrm{Ad}_gY]$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3, Def. 3.19, Props. 3.20, 3.21, 3.33, eq. (3.17) · the Lorentz case: [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-4|Theorem §CB.4.4]]*

^thm-cb-2-14

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3, Prop. 3.20 (Ad is a homomorphism), Prop. 3.21 (its differential), Prop. 3.33 (ad and Jacobi) and eq. (3.17) (Ad of an exponential) with proofs (https://arxiv.org/abs/math-ph/0005032).*
>
> **Step 1** (part 1; Hall, Prop. 3.33). For $Z \in \mathfrak g$: $\mathrm{ad}_{[X, Y]}Z = [[X, Y], Z]$ and $[\mathrm{ad}_X, \mathrm{ad}_Y]Z = [X, [Y, Z]] - [Y, [X, Z]]$. Their difference is $[[X, Y], Z] - [X, [Y, Z]] + [Y, [X, Z]] = -\bigl([X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]]\bigr)$ (using $[[X, Y], Z] = -[Z, [X, Y]]$ and $[Y, [X, Z]] = -[Y, [Z, X]]$), which is $0$ by the Jacobi identity ([[§49 Lie Bracket and Lie Algebra#^def-49-2|591 Def. §49.2]]). $\mathrm{ad}$ is linear because the bracket is bilinear.
>
> **Step 2** (Ad is a Lie group homomorphism; Hall, Prop. 3.20). $\mathrm{Ad}_g$ maps $\mathfrak g$ to itself ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]], 2) and is real-linear. $\mathrm{Ad}_{gh}X = ghXh^{-1}g^{-1} = \mathrm{Ad}_g(\mathrm{Ad}_hX)$ and $\mathrm{Ad}_{\mathbb 1} = \mathrm{id}$, so $\mathrm{Ad}_{g^{-1}}$ inverts $\mathrm{Ad}_g$ and $\mathrm{Ad} : G \to GL(\mathfrak g)$ is a group homomorphism. Choosing a basis of $\mathfrak g$ identifies $GL(\mathfrak g)$ with $GL(k, \mathbb R)$, $k = \dim\mathfrak g$, a matrix Lie group; the matrix entries of $\mathrm{Ad}_g$ are linear combinations of the entries of $gX_ag^{-1}$, continuous in $g$. So $\mathrm{Ad}$ is a Lie group homomorphism ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]]), and the Lie algebra of $GL(\mathfrak g)$ is $\mathfrak{gl}(\mathfrak g) = \operatorname{End}(\mathfrak g)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]], first row, over $\mathbb R$).
>
> **Step 3** (part 2: the differential; Hall, Prop. 3.21). By the formula of [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], for $X, Y \in \mathfrak g$,
>
> $$
> \mathrm{Ad}_\ast(X)\,Y = \frac{d}{dt}\mathrm{Ad}_{e^{tX}}(Y)\Big|_{t=0} = \frac{d}{dt}\bigl(e^{tX}Ye^{-tX}\bigr)\Big|_{t=0} = XY - YX = \mathrm{ad}_X(Y),
> $$
>
> the derivative computed as in Step 5 of the proof of Theorem §CB.1.10 (evaluation at $Y$ is linear, so it commutes with $d/dt$).
>
> **Step 4** (part 3; Hall, eq. (3.17)). Theorem §CB.2.3 applied to $\Phi = \mathrm{Ad}$ gives $\mathrm{Ad}(e^X) = e^{\mathrm{Ad}_\ast(X)} = e^{\mathrm{ad}_X}$, an identity between operators on $\mathfrak g$. Apply both sides to $Y$ and expand the exponential series of the operator $\mathrm{ad}_X$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-2|Def. §CB.1.2]] on $\operatorname{End}(\mathfrak g)$):
>
> $$
> e^XYe^{-X} = e^{\mathrm{ad}_X}Y = \sum_{k\ge0}\frac{(\mathrm{ad}_X)^kY}{k!} = Y + [X, Y] + \frac1{2!}[X, [X, Y]] + \frac1{3!}[X, [X, [X, Y]]] + \cdots .
> $$
>
> **Step 5** (part 4). $\mathrm{Ad}_g[X, Y] = g(XY - YX)g^{-1} = (gXg^{-1})(gYg^{-1}) - (gYg^{-1})(gXg^{-1}) = [\mathrm{Ad}_gX, \mathrm{Ad}_gY]$, inserting $g^{-1}g = \mathbb 1$ between the factors.
>
> **What the proof shows.**
> - Part 3 expresses a finite conjugation through brackets alone; this is how the generators of any representation transform as a tensor ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-4|Theorem §CB.4.4]]).
> - ⚑ By-product: the Jacobi identity is not an extra axiom here: it is the statement that $\mathrm{ad}$ preserves brackets (Step 1), the infinitesimal form of Step 5.

^pf-cb-2-14

*Uses:* [[§49 Lie Bracket and Lie Algebra#^def-49-2|591 Def. §49.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-2|Def. §CB.1.2]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]

## Coverings and the Lie correspondence

Simple connectivity and covering maps, defined in Topology (590):

![[§29 The Fundamental Group#^def-29-3]]

![[§31 Covering Spaces#^def-31-2]]

> [!definition] Definition §CB.2.15: Universal Covering Group
> A **universal covering group** of a connected matrix Lie group $G$ is a simply connected ([[§29 The Fundamental Group#^def-29-3|590 Def. §29.3]]) matrix Lie group $\tilde G$ with a Lie group homomorphism $p : \tilde G \to G$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]]) that is a covering map ([[§31 Covering Spaces#^def-31-2|590 Def. §31.2]]).
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 5 §9, Def. 5.36 (there: connected, simply connected, surjective, a local homeomorphism at the identity) · the examples: [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]*

^def-cb-2-15

> [!theorem] Theorem §CB.2.16: Discrete Normal Subgroups of Connected Groups Are Central
> If $G$ is a connected matrix Lie group and $N \subset G$ a normal subgroup that is discrete (each point of $N$ is isolated in $N$), then $N$ lies in the centre of $G$: $ng = gn$ for all $n \in N$, $g \in G$.
>
> *Source: Meinrenken, Lie Groups and Lie Algebras, §2.5, end of the proof of Thm. 2.13*

^thm-cb-2-16

> [!proof]- Proof
> *Source: E. Meinrenken, Lie Groups and Lie Algebras, lecture notes (Toronto, Winter 2026), §2.5, last paragraph of the proof of Thm. 2.13: "if G is connected … the adjoint action must be trivial on π₁(G) (since π₁(G) is discrete)" (https://www.math.toronto.edu/mein/teaching/LectureNotes/lie.pdf); the one-line argument is written out here.*
>
> **Step 1** (a map into $N$). Fix $n \in N$ and define $f : G \to G$, $f(g) = gng^{-1}$. It is continuous (matrix multiplication and inversion are), $f(\mathbb 1) = n$, and $f(G) \subset N$ because $N$ is normal ([[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]]).
>
> **Step 2** (the level set is open). Let $S = f^{-1}(n) = \{g : gng^{-1} = n\}$. If $g_0 \in S$, choose an open $W \subset G$ with $W \cap N = \{n\}$ ($n$ is isolated in $N$). Then $f^{-1}(W)$ is an open neighbourhood of $g_0$, and $f$ maps it into $W \cap N = \{n\}$; so $f^{-1}(W) \subset S$.
>
> **Step 3** (the level set is closed). $S$ is the preimage of the closed set $\{n\}$ under the continuous $f$.
>
> **Step 4** (connectedness). $G$ is connected (path-connected, [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-9|Def. §CB.2.9]], hence connected, [[§16 Connected Subspaces of ℝ#^thm-16-4|590 Thm. §16.4]]), and $S$ is nonempty ($\mathbb 1 \in S$), open and closed; so $S = G$ ([[§15 Connected Spaces#^def-15-2|590 Def. §15.2]]). That is, $gng^{-1} = n$, i.e. $gn = ng$, for every $g \in G$.
>
> **What the proof shows.**
> - Applied to kernels of coverings: $\ker(SU(2) \to SO(3)) = \{\pm\mathbb 1\}$ and $\ker(SL(2, \mathbb C) \to SO^+(1,3)) = \{\pm\mathbb 1\}$ are central, as they must be (Theorem §CB.2.17).
> - Discreteness is essential: $SO^+(1,3)$ is a normal subgroup of the connected $SO^+(1,3)$ that is not central.

^pf-cb-2-16

*Uses:* [[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-9|Def. §CB.2.9]], [[§16 Connected Subspaces of ℝ#^thm-16-4|590 Thm. §16.4]], [[§15 Connected Spaces#^def-15-2|590 Def. §15.2]]

> [!theorem] Theorem §CB.2.17: Homomorphisms with Invertible Differential Are Coverings
> Let $\Phi : G \to H$ be a Lie group homomorphism of connected matrix Lie groups whose differential $\Phi_\ast$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]) is a Lie algebra isomorphism. Then $\Phi$ is surjective, $\ker\Phi$ is a discrete central subgroup of $G$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-16|Theorem §CB.2.16]]), $\Phi$ is a covering map, and $H \cong G/\ker\Phi$ as groups ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]) and homeomorphically.
>
> *Source: Z. Wang, Lie Groups (USTC), Lecture 12, Lemma 1.1 · Lee, Introduction to Smooth Manifolds, Thm. 21.31 · Etingof, Lie Groups and Lie Algebras, Prop. 3.15 (ii) · instances: [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], Theorem §CB.13.12*

^thm-cb-2-17

> [!proof]- Proof
> *Source: Zuoqin Wang, Lie Groups (USTC, Fall 2013), Lecture 12 "Lie's fundamental theorems", Lemma 1.1 and its proof (http://staff.ustc.edu.cn/~wangzuoq/Courses/13F-Lie/Notes/Lec%2012.pdf), for Steps 3–5 · P. Etingof, Lie Groups and Lie Algebras (MIT 18.755 notes, 2024), Prop. 3.15 (ii) (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), for Step 2 · J. M. Lee, Introduction to Smooth Manifolds, 2nd ed., Thm. 21.31 ((d) ⇒ (c) ⇒ (a) ⇒ (b)), the same theorem for general Lie groups. The local homeomorphism (Step 1) is obtained from the exponential charts of Theorem §CB.1.13 instead of the inverse function theorem.*
>
> **Step 1** ($\Phi$ is a homeomorphism near $\mathbb 1$). By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-13|Theorem §CB.1.13]] for $G$ and for $H$ there are neighbourhoods $U_G$, $U_H$ of $0$ such that $\exp$ maps $U_G \cap \mathfrak g$ homeomorphically onto an open neighbourhood of $\mathbb 1$ in $G$, and likewise for $H$. Put $\varphi = \Phi_\ast$, a linear isomorphism $\mathfrak g \to \mathfrak h$, hence a homeomorphism. Choose an open $W \ni 0$ in $\mathfrak g$ with $W \subset U_G$ and $\varphi(W) \subset U_H$. Then $V = \exp(W)$ is open in $G$, $V' = \exp(\varphi(W))$ is open in $H$, and on $V$, by [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]],
>
> $$
> \Phi(e^X) = e^{\varphi(X)}, \qquad\text{i.e.}\qquad \Phi|_V = \exp_H\circ\varphi\circ(\exp_G|_W)^{-1} : V \to V',
> $$
>
> a composition of three homeomorphisms. So $\Phi$ maps $V$ homeomorphically onto $V'$.
>
> **Step 2** (surjective; Etingof, Prop. 3.15 (ii)). $H$ is connected, so every $h \in H$ is $e^{Y_1}\cdots e^{Y_k}$ with $Y_i \in \mathfrak h$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]], 3). For each $Y_i$, $e^{Y_i/m} \to \mathbb 1$ as $m \to \infty$, so $e^{Y_i/m} \in V' \subset \Phi(G)$ for some $m$, and $e^{Y_i} = (e^{Y_i/m})^m \in \Phi(G)$ ($\Phi(G)$ is a subgroup). Hence $h \in \Phi(G)$.
>
> **Step 3** (the kernel is discrete and central). Let $\Gamma = \ker\Phi$, a normal subgroup ([[§15 Homomorphisms#^def-15-3|493 Def. §15.3]], [[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]]). $\Phi$ is injective on $V$ and $\Phi(\mathbb 1) = \mathbb 1$, so $\Gamma \cap V = \{\mathbb 1\}$. For $a \in \Gamma$, $aV$ is an open neighbourhood of $a$ (left multiplication is a homeomorphism) and $aV \cap \Gamma = a(V \cap a^{-1}\Gamma) = a(V \cap \Gamma) = \{a\}$: every point of $\Gamma$ is isolated. By [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-16|Theorem §CB.2.16]] ($G$ connected), $\Gamma$ is central.
>
> **Step 4** ($V'$ is evenly covered; Wang, Lemma 1.1). *Claim:* $\Phi^{-1}(V') = \bigcup_{a\in\Gamma}aV$, a disjoint union of open sets each mapped homeomorphically onto $V'$.
> - $\supset$: for $u \in V$, $\Phi(au) = \Phi(a)\Phi(u) = \Phi(u) \in V'$.
> - $\subset$: if $\Phi(g) \in V'$, there is $u \in V$ with $\Phi(u) = \Phi(g)$ (Step 1); then $a = gu^{-1}$ has $\Phi(a) = \mathbb 1$, so $a \in \Gamma$ and $g = au \in aV$.
> - disjoint: if $au_1 = bu_2$ with $a, b \in \Gamma$, $u_1, u_2 \in V$, then $\Phi(u_1) = \Phi(u_2)$, so $u_1 = u_2$ (injectivity on $V$) and $a = b$.
> - homeomorphic: $\Phi|_{aV} = \Phi|_V\circ L_{a^{-1}}|_{aV}$ because $\Phi(au) = \Phi(u)$; a composition of homeomorphisms $aV \to V \to V'$.
>
> **Step 5** (every point is evenly covered). Let $h \in H$; by Step 2, $h = \Phi(g_0)$. Then $hV'$ is an open neighbourhood of $h$, and $\Phi^{-1}(hV') = g_0\Phi^{-1}(V') = \bigcup_{a\in\Gamma}g_0aV$ (since $\Phi(g) \in hV'$ iff $\Phi(g_0^{-1}g) \in V'$), a disjoint union of open sets, each mapped homeomorphically onto $hV'$ by $g_0au \mapsto h\Phi(u)$. So $\Phi$ is a covering map ([[§31 Covering Spaces#^def-31-2|590 Def. §31.2]]).
>
> **Step 6** ($H \cong G/\Gamma$). By the first isomorphism theorem ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]) and Step 2, $\bar\Phi(g\Gamma) = \Phi(g)$ is a group isomorphism $G/\Gamma \to H$. With the quotient topology on $G/\Gamma$ it is continuous (a map out of a quotient is continuous iff its composite with the projection, here $\Phi$, is) and open: an open set of $G/\Gamma$ is the image of an open $O \subset G$, and $\bar\Phi$ maps it to $\Phi(O)$, which is open because $\Phi$ is a local homeomorphism (Steps 4–5). A continuous open bijection is a homeomorphism.
>
> **What the proof shows.**
> - Everything follows from "local homeomorphism at $\mathbb 1$ + group structure": the group law moves the evenly covered neighbourhood of $\mathbb 1$ to every point.
> - ⚑ By-product: the number of sheets is $|\ker\Phi|$; for $SU(2) \to SO(3)$ and $SL(2, \mathbb C) \to SO^+(1,3)$ it is $2$, the "two-valuedness" of spinors.
> - Combined with simple connectivity of $G$, this identifies $G$ as the universal covering group ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-15|Def. §CB.2.15]]).

^pf-cb-2-17

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-13|Theorem §CB.1.13]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-16|Theorem §CB.2.16]], [[§15 Homomorphisms#^def-15-3|493 Def. §15.3]], [[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]], [[§31 Covering Spaces#^def-31-2|590 Def. §31.2]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]

> [!theorem] Theorem §CB.2.18: The Lie Correspondence for Simply Connected Groups
> Let $G$ be a simply connected matrix Lie group ([[§29 The Fundamental Group#^def-29-3|590 Def. §29.3]]), $H$ a matrix Lie group, and $\varphi : \mathfrak g \to \mathfrak h$ a Lie algebra homomorphism ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-2|Def. §CB.2.2]]). Then there is a unique Lie group homomorphism $\Phi : G \to H$ with $\Phi_\ast = \varphi$. In particular, with $H = GL(W)$: every finite-dimensional representation of $\mathfrak g$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-5|Def. §CB.2.5]]) is the differential of a unique representation of $G$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 5 §8, Thm. 5.33, 2, Cor. 5.35 (proof not reproduced; see the proof callout) · used for SU(2) in [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]] and for SL(2,ℂ) in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]*

^thm-cb-2-18

> [!proof]- Proof (to be filled)
> *Decision (SPEC-CB, item 7): stated here; the proof (via the Baker–Campbell–Hausdorff formula locally and path lifting, [[§32 Lifting and the Fundamental Group of the Circle#^lem-32-1|590 Lemma §32.1]], globally) is to be filled, or linked to 591 once the course proves it. Uniqueness is Theorem §CB.2.11; only existence is open.*

^pf-cb-2-18

<!-- searched (2026-10-08): Hall, An Elementary Introduction to Groups and Representations (arXiv:math-ph/0005032), Thm. 5.33 (2): proof rests on the BCH integral formula (Thm. 4.3, Cor. 4.4, proved over several pages) and on homotopy steps left as "a standard topological argument"; Meinrenken, Lie Groups and Lie Algebras (Toronto 2026), Thm. 7.8 and Etingof, Lie Groups and Lie Algebras (MIT 18.755), Thm. 9.12 / §10.2.2, and Z. Wang (USTC) Lecture 12, Thm. 1.3: all via the graph subgroup and integration of subalgebras (Frobenius theorem); Lee, Introduction to Smooth Manifolds, Thm. 20.19: same route. No self-contained matrix-group proof that fits CB.1–CB.2 without first developing BCH or Frobenius; placeholder kept per SPEC-CB decision 7. -->

> [!remark] Remark: Why the algebra is not enough, and what simple connectivity adds
> Theorem §CB.2.11 says that the algebra determines a homomorphism of a *connected* group; Theorem §CB.2.18 says that every algebra homomorphism comes from a group homomorphism only when the group is *simply connected*. The gap between the two is the fundamental group: SO(3) and SU(2) have the same algebra ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]]), but spin ½ integrates only to SU(2) ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-7|Theorem §CB.9.7]]). Spinor representations are this gap made visible (§CB.13).

^rem-cb-2-1

> [!remark]- Connections
> - Theorem §CB.2.17 is the common shape of SU(2) → SO(3) ([[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]), SL(2,ℂ) → SO⁺(1,3) ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]) and Spin(V) → SO(V) (§CB.13).
> - **Used in**: Theorem §CB.2.3 — [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-1|Def. §CB.4.1]]; Theorem §CB.2.10 — [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-11|Theorem §CB.16.11]] (step 5); Theorem §CB.2.14 — the generators transform as a tensor ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-4|Theorem §CB.4.4]]), how the quantum generators transform ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-4|Theorem §C3.4.4]]); Theorems §CB.2.16–§CB.2.18 — integration of spin $j$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]]), the double covers ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]), integer $(j_+, j_-)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]); Definition §CB.2.4 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded; cited in [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^def-c3-1-1|Def. §C3.1.1]]), [[§C3.6★ Particle States and the Little Group|§C3.6★]] (embedded; cited in [[§C3.6★ Particle States and the Little Group#^thm-c3-6-4|Theorem §C3.6.4]]), [[§C1b.1 Fields and Their Transformation Laws|§C1b.1]] (embedded; cited in [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]]); Definition §CB.2.5 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded); Theorem §CB.2.8 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded; cited in [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^rem-c3-1-1|§C3.1, Remark: One symbol for each realization of the generators]]); Definition §CB.2.6 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded), [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded; cited in [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-5|Theorem §C3.3.5]]); Definition §CB.2.7 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded), [[§C3.6★ Particle States and the Little Group|§C3.6★]] (embedded; cited in [[§C3.6★ Particle States and the Little Group#^thm-c3-6-2|Theorem §C3.6.2]]).
