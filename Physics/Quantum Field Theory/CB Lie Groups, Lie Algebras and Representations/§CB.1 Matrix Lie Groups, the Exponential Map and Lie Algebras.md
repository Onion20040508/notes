---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.1
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification]] →

*Sources (planned for the proofs; each to be checked against the text when the proof is written): Differentiable Manifolds (591) §§11, 16, 25, 48–49 · the user's PHY 513 notes, Ch. 7 §7.2 · Yu Zhao-Huan, 量子场论讲义, §3.2 · Peskin & Schroeder, §3.1 · Hall, Quantum Theory for Mathematicians, Ch. 16 · P. Woit, Quantum Theory, Groups and Representations, Ch. 5 (author's PDF, https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the rest written here.*

How do a matrix group and its Lie algebra determine each other, and which statements about representations may be checked on generators alone? The course defines a matrix Lie group and its Lie algebra ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2|Def. §C3.1.2]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3|Def. §C3.1.3]]); the Math vault has Lie groups, Lie algebras and the tangent spaces of the classical groups ([[§49 Lie Groups and Left-Invariant Vector Fields#^def-49-1|591 Def. §49.1]], [[§48 Lie Bracket and Lie Algebra#^def-48-2|591 Def. §48.2]], [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]]). This section supplies what lies between them and what the physics chapters use without proof: the matrix exponential, one-parameter subgroups, why the Lie algebra is a *real* Lie algebra, homomorphisms and their differentials, the identity component, the adjoint representation, and the covering and integration theorems behind SU(2) → SO(3) and SL(2,ℂ) → SO⁺(1,3). Statements are numbered in reading order with one counter per section (Definition §CB.1.1, Theorem §CB.1.2, …); boxes shown as embeds keep their home numbers.

## Recalled: Lie groups, Lie algebras and matrix groups

A Lie group in general, defined in 591:

![[§49 Lie Groups and Left-Invariant Vector Fields#^def-49-1]]

A (real) Lie algebra, defined in 591; the commutator of any associative product is a Lie bracket, proved there ([[§48 Lie Bracket and Lie Algebra#^prop-48-3|591 Prop. §48.3]]):

![[§48 Lie Bracket and Lie Algebra#^def-48-2]]

![[§48 Lie Bracket and Lie Algebra#^prop-48-3]]

The matrix groups of the course, defined in [[§C1a.4 The Lorentz Group|§C1a.4]], and the course's notion of a matrix Lie group, defined in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C1a.4 The Lorentz Group#^def-c1a-4-4]]

![[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2]]

## The exponential map

> [!definition] Definition §CB.1.1: Matrix Exponential
> For $X \in M_n(\mathbb C)$ the **matrix exponential** is
>
> $$
> e^X = \exp X = \sum_{k=0}^\infty \frac{X^k}{k!}, \qquad X^0 = \mathbb 1 ,
> $$
>
> the limit of the partial sums in the operator norm $\|X\| = \sup_{|v| = 1}|Xv|$ on $M_n(\mathbb C) \cong \mathbb C^{n^2}$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-2|591 Def. §11.2]]); that the limit exists is Theorem §CB.1.2.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · Woit, Ch. 5*

^def-cb-1-1

> [!theorem] Theorem §CB.1.2: Convergence and Algebraic Properties of the Exponential
> For $X, Y \in M_n(\mathbb C)$ and $s, t \in \mathbb R$:
> 1. the series of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]] converges absolutely, uniformly on every bounded set of $X$, and $\|e^X\| \le e^{\|X\|}$; $X \mapsto e^X$ is continuous (indeed smooth);
> 2. $e^0 = \mathbb 1$, and $e^X$ is invertible with $(e^X)^{-1} = e^{-X}$;
> 3. if $XY = YX$, then $e^{X + Y} = e^Xe^Y$; in particular $e^{(s + t)X} = e^{sX}e^{tX}$;
> 4. $e^{SXS^{-1}} = S\,e^X S^{-1}$ for invertible $S$; $(e^X)^{\mathsf T} = e^{X^{\mathsf T}}$, $\overline{e^X} = e^{\bar X}$, $(e^X)^\dagger = e^{X^\dagger}$;
> 5. $s \mapsto e^{sX}$ is differentiable with $\frac{d}{ds}e^{sX} = Xe^{sX} = e^{sX}X$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · Woit, Ch. 5*

^thm-cb-1-2

> [!proof]- Proof (to be filled)
> *To be filled (CB.1–CB.3).*

^pf-cb-1-2

> [!theorem] Theorem §CB.1.3: Determinant of an Exponential
> For every $X \in M_n(\mathbb C)$, $\det e^X = e^{\operatorname{tr}X}$. In particular $e^X$ has determinant $1$ when $\operatorname{tr}X = 0$, and $\det e^X > 0$ when $X$ is real.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · used in [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]], Derivation, steps 1–2*

^thm-cb-1-3

> [!proof]- Proof (to be filled)
> *To be filled (planned route: upper-triangular form, [[§16 Upper-Triangular Matrices|LADR §16]], and $\det$, $\operatorname{tr}$ of a triangular matrix).*

^pf-cb-1-3

> [!theorem] Theorem §CB.1.4: The Logarithm Near the Identity
> For $A \in M_n(\mathbb C)$ with $\|A - \mathbb 1\| < 1$ the series $\log A = \sum_{k\ge1}\frac{(-1)^{k+1}}{k}(A - \mathbb 1)^k$ converges, $\log$ is continuous there, and $e^{\log A} = A$. For $\|X\| < \log 2$, $\|e^X - \mathbb 1\| < 1$ and $\log e^X = X$. Hence $\exp$ maps a neighbourhood of $0$ in $M_n(\mathbb C)$ homeomorphically onto a neighbourhood of $\mathbb 1$ in $GL(n, \mathbb C)$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16*

^thm-cb-1-4

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-1-4

> [!theorem] Theorem §CB.1.5: Lie Product Formula and the Commutator as a Second-Order Term
> For $X, Y \in M_n(\mathbb C)$:
> 1. $e^{X + Y} = \lim_{m\to\infty}\bigl(e^{X/m}e^{Y/m}\bigr)^m$;
> 2. $e^{sX}e^{sY} = \exp\bigl(s(X + Y) + \frac{s^2}{2}[X, Y] + O(s^3)\bigr)$ as $s \to 0$ (the first terms of the Baker–Campbell–Hausdorff series);
> 3. $e^{sX}e^{sY}e^{-sX}e^{-sY} = \mathbb 1 + s^2[X, Y] + O(s^3)$ as $s \to 0$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · the second-order commutator is the content of [[§C3.2 The Lorentz Algebra#^rem-c3-2-2|§C3.2, Remark: Two boosts make a rotation]]*

^thm-cb-1-5

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-1-5

## One-parameter subgroups and the Lie algebra

> [!definition] Definition §CB.1.6: One-Parameter Subgroup
> A **one-parameter subgroup** of $GL(n, \mathbb C)$ is a continuous group homomorphism ([[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]) $\gamma : (\mathbb R, +) \to GL(n, \mathbb C)$: $\gamma(s + t) = \gamma(s)\gamma(t)$, $\gamma(0) = \mathbb 1$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · Woit, Ch. 5*

^def-cb-1-6

> [!theorem] Theorem §CB.1.7: One-Parameter Subgroups Are Exponentials
> If $\gamma$ is a one-parameter subgroup of $GL(n, \mathbb C)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-6|Def. §CB.1.6]]), then $\gamma$ is differentiable and $\gamma(s) = e^{sX}$ for all $s$, with the unique matrix $X = \gamma'(0)$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16*

^thm-cb-1-7

> [!proof]- Proof (to be filled)
> *To be filled (planned route: the logarithm of Theorem §CB.1.4 on a small interval).*

^pf-cb-1-7

The course defines the Lie algebra of a matrix Lie group through its one-parameter subgroups, in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3]]

> [!theorem] Theorem §CB.1.8: The Lie Algebra Is a Real Lie Algebra
> Let $G$ be a matrix Lie group ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2|Def. §C3.1.2]]) and $\mathfrak g$ its Lie algebra ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3|Def. §C3.1.3]]). Then
> 1. $\mathfrak g$ is a **real** vector subspace of $M_n(\mathbb C)$: $X, Y \in \mathfrak g$ and $a, b \in \mathbb R$ give $aX + bY \in \mathfrak g$; in general $iX \notin \mathfrak g$;
> 2. $gXg^{-1} \in \mathfrak g$ for all $g \in G$, $X \in \mathfrak g$;
> 3. $[X, Y] = XY - YX \in \mathfrak g$ for $X, Y \in \mathfrak g$, so $(\mathfrak g, [\cdot,\cdot])$ is a real Lie algebra ([[§48 Lie Bracket and Lie Algebra#^def-48-2|591 Def. §48.2]], [[§48 Lie Bracket and Lie Algebra#^prop-48-3|591 Prop. §48.3]]).
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · Woit, §5.1*

^thm-cb-1-8

> [!proof]- Proof (to be filled)
> *To be filled (planned route: the Lie product formula, Theorem §CB.1.5, 1, for sums; differentiation of $s \mapsto e^{sX}Ye^{-sX}$ at $s = 0$, using that $\mathfrak g$ is closed in $M_n(\mathbb C)$, for brackets).*

^pf-cb-1-8

> [!theorem] Theorem §CB.1.9: The Lie Algebra Is the Tangent Space at the Identity
> Let $G$ be a matrix Lie group with Lie algebra $\mathfrak g$.
> 1. $\mathfrak g$ is the set of velocities $\gamma'(0)$ of the differentiable curves $\gamma$ in $M_n(\mathbb C)$ that lie in $G$ and have $\gamma(0) = \mathbb 1$.
> 2. For the classical groups of [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]], $\mathfrak g$ equals 591's geometric tangent space $T^{\mathrm{geo}}_IG$.
> 3. Under the identification of a left-invariant vector field with its value at $\mathbb 1$, the Lie algebra of left-invariant vector fields of [[§49 Lie Groups and Left-Invariant Vector Fields#^def-49-4|591 Def. §49.4]] is $\mathfrak g$, and the bracket of vector fields becomes the commutator $XY - YX$.
>
> *Source (planned): 591 §25, §49 · Hall, Quantum Theory for Mathematicians, Ch. 16*

^thm-cb-1-9

> [!proof]- Proof (to be filled)
> *To be filled; part 3 will be linked to 591 when the course proves it (591 §49 so far defines the Lie algebra of a Lie group without computing it for matrix groups).*

^pf-cb-1-9

> [!theorem] Theorem §CB.1.10: Closed-Subgroup Theorem
> Every closed subgroup $G$ of $GL(n, \mathbb C)$ is an embedded submanifold of $GL(n, \mathbb C)$ of real dimension $\dim_{\mathbb R}\mathfrak g$, and with this structure a Lie group ([[§49 Lie Groups and Left-Invariant Vector Fields#^def-49-1|591 Def. §49.1]]). There is a neighbourhood $U$ of $0$ in $M_n(\mathbb C)$ such that $\exp$ maps $U \cap \mathfrak g$ homeomorphically onto a neighbourhood of $\mathbb 1$ in $G$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 (cited in [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2|Def. §C3.1.2]]) · 591 when the course reaches it*

^thm-cb-1-10

> [!proof]- Proof (to be filled)
> *Decision (SPEC-CB, item 7): stated here; the proof is to be filled, or linked to 591 once the course proves it.*

^pf-cb-1-10

> [!theorem] Theorem §CB.1.11: The Lie Algebras of the Classical Groups
> With $\eta = \operatorname{diag}(1, -1, -1, -1)$:
>
> | group | Lie algebra | real dimension |
> |---|---|---|
> | $GL(n, \mathbb C)$ | $\mathfrak{gl}(n, \mathbb C) = M_n(\mathbb C)$ | $2n^2$ |
> | $SL(n, \mathbb C)$ | $\mathfrak{sl}(n, \mathbb C) = \{X : \operatorname{tr}X = 0\}$ | $2n^2 - 2$ |
> | $U(n)$ | $\mathfrak u(n) = \{X : X^\dagger = -X\}$ | $n^2$ |
> | $SU(n)$ | $\mathfrak{su}(n) = \{X : X^\dagger = -X,\ \operatorname{tr}X = 0\}$ | $n^2 - 1$ |
> | $O(n)$, $SO(n)$ | $\mathfrak{so}(n) = \{X \in M_n(\mathbb R) : X^{\mathsf T} = -X\}$ | $n(n-1)/2$ |
> | $O(1,3)$, $SO^+(1,3)$ | $\mathfrak{so}(1,3) = \{X \in M_4(\mathbb R) : X^{\mathsf T}\eta + \eta X = 0\}$ | $6$ |
>
> In particular $SL(2, \mathbb C)$, a group of complex matrices, has a Lie algebra of real dimension $6$; it is a real Lie algebra that happens to be closed under multiplication by $i$.
>
> *Source (planned): 591 Thm. §25.5 (the real groups) · the user's PHY 513 notes, Ch. 7 §7.2 · [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]] (the Lorentz case)*

^thm-cb-1-11

> [!proof]- Proof (to be filled)
> *To be filled (planned route: differentiate the defining equation along $e^{sX}$ as in [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]], Derivation, steps 1–2, and use Theorem §CB.1.3 for the determinant condition).*

^pf-cb-1-11

The rotation case, proved in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1]]

## Homomorphisms and their differentials

> [!definition] Definition §CB.1.12: Lie Group Homomorphism
> A **Lie group homomorphism** between matrix Lie groups $G$ and $H$ is a continuous group homomorphism $\Phi : G \to H$ ([[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]). It is an **isomorphism of Lie groups** if it is bijective and $\Phi^{-1}$ is continuous.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16*

^def-cb-1-12

> [!definition] Definition §CB.1.13: Lie Algebra Homomorphism
> A **Lie algebra homomorphism** between real Lie algebras $\mathfrak g$ and $\mathfrak h$ ([[§48 Lie Bracket and Lie Algebra#^def-48-2|591 Def. §48.2]]) is a real-linear map $\varphi : \mathfrak g \to \mathfrak h$ with $\varphi([X, Y]) = [\varphi(X), \varphi(Y)]$ for all $X, Y$. A bijective one is an **isomorphism**, written $\mathfrak g \cong \mathfrak h$. (For complex Lie algebras, [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-1|Def. §CB.2.1]], the same words with complex-linear maps.)
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16*

^def-cb-1-13

> [!theorem] Theorem §CB.1.14: The Differential of a Homomorphism
> Let $\Phi : G \to H$ be a Lie group homomorphism ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-12|Def. §CB.1.12]]). There is a unique real-linear map $\varphi = \Phi_\ast : \mathfrak g \to \mathfrak h$, the **differential** of $\Phi$, with
>
> $$
> \Phi(e^{X}) = e^{\varphi(X)} \quad (X \in \mathfrak g), \qquad \varphi(X) = \frac{d}{ds}\Phi(e^{sX})\Big|_{s=0} .
> $$
>
> Moreover $\varphi$ is a Lie algebra homomorphism ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-13|Def. §CB.1.13]]), $\varphi(gXg^{-1}) = \Phi(g)\varphi(X)\Phi(g)^{-1}$, and $(\Psi\circ\Phi)_\ast = \Psi_\ast\circ\Phi_\ast$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · Woit, §5.4*

^thm-cb-1-14

> [!proof]- Proof (to be filled)
> *To be filled (planned route: $s \mapsto \Phi(e^{sX})$ is a one-parameter subgroup, Theorem §CB.1.7; linearity and brackets from Theorem §CB.1.5).*

^pf-cb-1-14

The case $H = GL(W)$, a representation, is the course's theorem, proved in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2]]

## The identity component

> [!definition] Definition §CB.1.15: Identity Component
> The **identity component** $G_0$ of a matrix Lie group $G$ is the set of $g \in G$ that can be joined to $\mathbb 1$ by a continuous path in $G$. $G$ is **connected** if $G_0 = G$.
>
> *Source (planned): 591 §16 · Hall, Quantum Theory for Mathematicians, Ch. 16*

^def-cb-1-15

> [!theorem] Theorem §CB.1.16: The Identity Component Is Generated by Exponentials
> Let $G$ be a matrix Lie group with Lie algebra $\mathfrak g$ and identity component $G_0$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-15|Def. §CB.1.15]]).
> 1. $G_0$ is a normal subgroup of $G$ ([[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]]), open and closed in $G$, and its cosets are the path components of $G$.
> 2. $e^X \in G_0$ for every $X \in \mathfrak g$.
> 3. Every $g \in G_0$ is a finite product $g = e^{X_1}e^{X_2}\cdots e^{X_k}$ with $X_i \in \mathfrak g$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · the Lorentz case: [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]]*

^thm-cb-1-16

> [!proof]- Proof (to be filled)
> *To be filled (planned route: part 2 by the path $s \mapsto e^{sX}$; part 3 by Theorem §CB.1.10, a neighbourhood of $\mathbb 1$ made of exponentials, and connectedness).*

^pf-cb-1-16

The Lorentz group's components and its exponentials, proved in [[§C1a.4 The Lorentz Group|§C1a.4]] and [[§C1a.6 Infinitesimal Lorentz Transformations and Generators|§C1a.6]]:

![[§C1a.4 The Lorentz Group#^thm-c1a-4-3]]

![[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4]]

> [!theorem] Theorem §CB.1.17: A Homomorphism of a Connected Group Is Determined by Its Differential
> Let $G$ be connected and $\Phi, \Psi : G \to H$ Lie group homomorphisms with $\Phi_\ast = \Psi_\ast$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]]). Then $\Phi = \Psi$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16*

^thm-cb-1-17

> [!proof]- Proof (to be filled)
> *To be filled (planned route: Theorem §CB.1.14 on each factor of Theorem §CB.1.16, 3).*

^pf-cb-1-17

## The adjoint representation

591 defines the adjoint action for four classical groups:

![[§25 The Geometric Tangent Space#^def-25-2]]

> [!definition] Definition §CB.1.18: Adjoint Representation of a Group
> For a matrix Lie group $G$ with Lie algebra $\mathfrak g$, the **adjoint representation** is $\mathrm{Ad} : G \to GL(\mathfrak g)$, $\mathrm{Ad}_g(X) = gXg^{-1}$, a representation on the real vector space $\mathfrak g$ (well defined by [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], 2).
>
> *Source (planned): 591 Def. §25.2, Prop. §25.6 · Hall, Quantum Theory for Mathematicians, Ch. 16*

^def-cb-1-18

> [!definition] Definition §CB.1.19: Adjoint Representation of a Lie Algebra
> For a Lie algebra $\mathfrak g$, $\mathrm{ad} : \mathfrak g \to \operatorname{End}(\mathfrak g)$ is $\mathrm{ad}_X(Y) = [X, Y]$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16*

^def-cb-1-19

> [!theorem] Theorem §CB.1.20: The Differential of Ad Is ad
> 1. $\mathrm{ad}$ is a Lie algebra homomorphism $\mathfrak g \to \mathfrak{gl}(\mathfrak g)$: $\mathrm{ad}_{[X, Y]} = [\mathrm{ad}_X, \mathrm{ad}_Y]$ (the Jacobi identity).
> 2. $\mathrm{Ad}$ is a Lie group homomorphism and $\mathrm{Ad}_\ast = \mathrm{ad}$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]]).
> 3. $e^XYe^{-X} = e^{\mathrm{ad}_X}Y = Y + [X, Y] + \frac1{2!}[X, [X, Y]] + \cdots$ for $X, Y \in \mathfrak g$.
> 4. $\mathrm{Ad}_g[X, Y] = [\mathrm{Ad}_gX, \mathrm{Ad}_gY]$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · the Lorentz case: [[§C3.2 The Lorentz Algebra#^thm-c3-2-2|Theorem §C3.2.2]]*

^thm-cb-1-20

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-1-20

## Coverings and the Lie correspondence

Simple connectivity and covering maps, defined in Topology (590):

![[§29 The Fundamental Group#^def-29-3]]

![[§31 Covering Spaces#^def-31-2]]

> [!definition] Definition §CB.1.21: Universal Covering Group
> A **universal covering group** of a connected matrix Lie group $G$ is a simply connected ([[§29 The Fundamental Group#^def-29-3|590 Def. §29.3]]) matrix Lie group $\tilde G$ with a Lie group homomorphism $p : \tilde G \to G$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-12|Def. §CB.1.12]]) that is a covering map ([[§31 Covering Spaces#^def-31-2|590 Def. §31.2]]).
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · the examples: [[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|591 Thm. §41.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]*

^def-cb-1-21

> [!theorem] Theorem §CB.1.22: Discrete Normal Subgroups of Connected Groups Are Central
> If $G$ is a connected matrix Lie group and $N \subset G$ a normal subgroup that is discrete (each point of $N$ is isolated in $N$), then $N$ lies in the centre of $G$: $ng = gn$ for all $n \in N$, $g \in G$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16*

^thm-cb-1-22

> [!proof]- Proof (to be filled)
> *To be filled (planned route: for fixed $n$, $g \mapsto gng^{-1}$ is a continuous map from the connected $G$ into the discrete $N$, hence constant).*

^pf-cb-1-22

> [!theorem] Theorem §CB.1.23: Homomorphisms with Invertible Differential Are Coverings
> Let $\Phi : G \to H$ be a Lie group homomorphism of connected matrix Lie groups whose differential $\Phi_\ast$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]]) is a Lie algebra isomorphism. Then $\Phi$ is surjective, $\ker\Phi$ is a discrete central subgroup of $G$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-22|Theorem §CB.1.22]]), $\Phi$ is a covering map, and $H \cong G/\ker\Phi$ as groups ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]) and homeomorphically.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · instances: [[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|591 Thm. §41.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], Theorem §CB.9.12*

^thm-cb-1-23

> [!proof]- Proof (to be filled)
> *To be filled (planned route: $\Phi$ is a local homeomorphism at $\mathbb 1$ by Theorem §CB.1.10 and the exponentials; surjectivity from Theorem §CB.1.16, 3; evenly covered neighbourhoods by translation).*

^pf-cb-1-23

> [!theorem] Theorem §CB.1.24: The Lie Correspondence for Simply Connected Groups
> Let $G$ be a simply connected matrix Lie group ([[§29 The Fundamental Group#^def-29-3|590 Def. §29.3]]), $H$ a matrix Lie group, and $\varphi : \mathfrak g \to \mathfrak h$ a Lie algebra homomorphism ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-13|Def. §CB.1.13]]). Then there is a unique Lie group homomorphism $\Phi : G \to H$ with $\Phi_\ast = \varphi$. In particular, with $H = GL(W)$: every finite-dimensional representation of $\mathfrak g$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-6|Def. §C3.1.6]]) is the differential of a unique representation of $G$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · used for SU(2) in [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]] and for SL(2,ℂ) in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]*

^thm-cb-1-24

> [!proof]- Proof (to be filled)
> *Decision (SPEC-CB, item 7): stated here; the proof (via the Baker–Campbell–Hausdorff formula locally and path lifting, [[§32 Lifting and the Fundamental Group of the Circle#^lem-32-1|590 Lemma §32.1]], globally) is to be filled, or linked to 591 once the course proves it.*

^pf-cb-1-24

> [!remark] Remark: Why the algebra is not enough, and what simple connectivity adds
> Theorem §CB.1.17 says that the algebra determines a homomorphism of a *connected* group; Theorem §CB.1.24 says that every algebra homomorphism comes from a group homomorphism only when the group is *simply connected*. The gap between the two is the fundamental group: SO(3) and SU(2) have the same algebra ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]]), but spin ½ integrates only to SU(2) ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|Theorem §C3.1.8]]). Spinor representations are this gap made visible (§CB.9).

^rem-cb-1-1

> [!remark]- Connections
> - The real Lie algebra of Theorem §CB.1.8 is the reason for [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification|§CB.2]]: the physicists' Hermitian generators and the ladder combinations $J^\pm$, $\mathbf J_\pm$ live outside $\mathfrak g$, in $i\mathfrak g$ and in the complexification.
> - Theorem §CB.1.23 is the common shape of SU(2) → SO(3) ([[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|591 Thm. §41.4]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]), SL(2,ℂ) → SO⁺(1,3) ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]) and Spin(V) → SO(V) (§CB.9).
> - **Used in**: Definition §CB.1.1–Theorem §CB.1.3 — the exponentials of rotations and boosts and their determinants ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]]), the finite quantum Poincaré transformations ([[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-3|Theorem §C3.5.3]]); Theorem §CB.1.5 — two boosts make a rotation ([[§C3.2 The Lorentz Algebra#^rem-c3-2-2|§C3.2, Remark: Two boosts make a rotation]]); Theorems §CB.1.8–§CB.1.11 — the course's Lie algebras ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3|Def. §C3.1.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]], [[§C1a.4 The Lorentz Group#^def-c1a-4-4|Def. §C1a.4.4]]); Theorem §CB.1.14 — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]], [[§C3.2 The Lorentz Algebra#^def-c3-2-1|Def. §C3.2.1]]; Theorem §CB.1.16 — [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]] (step 5); Theorem §CB.1.20 — the generators transform as a tensor ([[§C3.2 The Lorentz Algebra#^thm-c3-2-2|Theorem §C3.2.2]]), how the quantum generators transform ([[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-4|Theorem §C3.5.4]]); Theorems §CB.1.22–§CB.1.24 — integration of spin $j$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]]), the double covers ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]), integer $(j_+, j_-)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]).
