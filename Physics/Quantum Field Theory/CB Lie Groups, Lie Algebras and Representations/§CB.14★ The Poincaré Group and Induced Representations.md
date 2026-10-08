---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.14
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.13 Projective Representations, Wigner's Theorem and Antiunitary Symmetries]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.15 Grassmann Algebras]] →

*Sources (planned for the proofs; each to be checked against the text when the proof is written): P. Woit, Quantum Theory, Groups and Representations, Ch. 18 (semi-direct products), Ch. 20 (§20.4 "Representations of N ⋊ K, N commutative"), Ch. 42 (the Poincaré group and its irreducible representations) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the user's PHY 513 notes, Ch. 7 §7.7 · Yu Zhao-Huan, 量子场论讲义, §3.3 · Group Theory (493) §§25–30, §§38–41 · the rest written here.*

★ Beyond the course's mathematics: PHY 513 uses the results (Wigner's classification, [[§C3.6★ Particle States and the Little Group|§C3.6★]]–[[§C3.7★ Massless Particles and Helicity|§C3.7★]]) but not the general theory of induced representations (decision SPEC-CB 4).

What is the Poincaré group as a group, and how are all its irreducible unitary representations built from the orbits of momenta and the little groups? The Poincaré group is a semidirect product of translations and Lorentz transformations; its unitary representations restrict on translations to momenta, the Lorentz group moves the momenta along orbits ([[§C1a.4 The Lorentz Group#^thm-c1a-4-4|Theorem §C1a.4.4]]), and a representation of the stabilizer of one momentum — the little group — induces a representation of the whole group. This section states the general construction (Wigner–Mackey) of which the course's induced representation ([[§C3.6★ Particle States and the Little Group#^thm-c3-6-4|Theorem §C3.6.4]]) is the case $\mathbb R^{1,3}\rtimes SL(2, \mathbb C)$, and computes the little groups inside $SL(2, \mathbb C)$. It builds on [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)|§CB.11]] and [[§CB.13 Projective Representations, Wigner's Theorem and Antiunitary Symmetries|§CB.13]] (Bargmann: why genuine representations of the cover suffice).

## Semidirect products and the Poincaré group

> [!definition] Definition §CB.14.1: Semidirect Product
> Let $N$ and $H$ be groups and $\varphi : H \to \operatorname{Aut}(N)$ a homomorphism. The **semidirect product** $N\rtimes_\varphi H$ is the set $N\times H$ with the product $(n, h)(n', h') = (n\,\varphi_h(n'), hh')$.
>
> *Source (planned): Woit, §18.2 · written here*

^def-cb-14-1

> [!theorem] Theorem §CB.14.2: The Semidirect Product Is a Group with N Normal
> $N\rtimes_\varphi H$ ([[§CB.14★ The Poincaré Group and Induced Representations#^def-cb-14-1|Def. §CB.14.1]]) is a group with identity $(1, 1)$ and $(n, h)^{-1} = (\varphi_{h^{-1}}(n^{-1}), h^{-1})$; $N\times\{1\}$ is a normal subgroup ([[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]]), $\{1\}\times H$ a subgroup, and the quotient ([[§40 Quotient Groups#^def-40-1|493 Def. §40.1]]) is isomorphic to $H$. Conjugation of $N$ by $H$ is $\varphi$: $(1, h)(n, 1)(1, h)^{-1} = (\varphi_h(n), 1)$.
>
> *Source (planned): Woit, §18.2 · written here*

^thm-cb-14-2

> [!proof]- Proof (to be filled)
> *To be filled (associativity uses that $\varphi$ is a homomorphism; the quotient via the projection $(n, h) \mapsto h$ and [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]).*

^pf-cb-14-2

> [!definition] Definition §CB.14.3: The Poincaré Group
> The **(proper orthochronous) Poincaré group** is $\mathbb R^{1,3}\rtimes SO^+(1,3)$ ([[§CB.14★ The Poincaré Group and Induced Representations#^def-cb-14-1|Def. §CB.14.1]]), with $\varphi_\Lambda(a) = \Lambda a$: the transformations $x \mapsto \Lambda x + a$, composed as $(a, \Lambda)(a', \Lambda') = (a + \Lambda a', \Lambda\Lambda')$.
>
> *Source (planned): Woit, Ch. 42 · the user's PHY 513 notes, Ch. 7 §7.5*

^def-cb-14-3

> [!definition] Definition §CB.14.4: The Double Cover of the Poincaré Group
> $\mathbb R^{1,3}\rtimes SL(2, \mathbb C)$ with $\varphi_\lambda(a) = \pi(\lambda)a$, $\pi$ the covering of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]] (equivalently $\rho$ of [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)#^thm-cb-11-2|Theorem §CB.11.2]]). The map $(a, \lambda) \mapsto (a, \pi(\lambda))$ is a two-to-one covering homomorphism onto the Poincaré group ([[§CB.14★ The Poincaré Group and Induced Representations#^def-cb-14-3|Def. §CB.14.3]]); the source is simply connected, the universal covering group ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-21|Def. §CB.1.21]]).
>
> *Source (planned): Woit, Ch. 42 · written here*

^def-cb-14-4

> [!theorem] Theorem §CB.14.5: The Poincaré Group as a Matrix Lie Group, and Its Lie Algebra
> $(a, \Lambda) \mapsto \begin{pmatrix}\Lambda & a\\ 0 & 1\end{pmatrix} \in GL(5, \mathbb R)$ is an isomorphism of the Poincaré group onto a closed subgroup of $GL(5, \mathbb R)$. Its Lie algebra ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3|Def. §C3.1.3]]) is $\{\begin{pmatrix}\omega & b\\ 0 & 0\end{pmatrix} : \omega \in \mathfrak{so}(1,3), b \in \mathbb R^4\}$, ten-dimensional, whose brackets in the physicists' generators are the Poincaré algebra ([[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-5|Theorem §C3.5.5]]).
>
> *Source (planned): Woit, §18.3, §42.1 · written here*

^thm-cb-14-5

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-14-5

The Poincaré algebra in the course, in [[§C3.5 Quantum Poincaré Transformations|§C3.5]]:

![[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-5]]

## Orbits, stabilizers and little groups

Orbits and stabilizers, defined in Group Theory; the orbits of $SO^+(1,3)$ on momenta, proved in [[§C1a.4 The Lorentz Group|§C1a.4]]; the little group, defined in [[§C3.6★ Particle States and the Little Group|§C3.6★]]:

![[§27 Orbits#^def-27-1]]

![[§26 Stabilizers and Fixed Points#^def-26-1]]

![[§C1a.4 The Lorentz Group#^thm-c1a-4-4]]

![[§C3.6★ Particle States and the Little Group#^def-c3-6-2]]

> [!definition] Definition §CB.14.6: Characters of the Translations and the Dual Action
> For $p \in \mathbb R^{1,3}$ the **character** $\chi_p(a) = e^{ip\cdot a}$ is a continuous homomorphism $\mathbb R^{1,3} \to U(1)$, and every continuous homomorphism $\mathbb R^{1,3} \to U(1)$ is one $\chi_p$. $H = SO^+(1,3)$ or $SL(2, \mathbb C)$ acts on characters by $(h\cdot\chi_p)(a) = \chi_p(\varphi_{h^{-1}}(a)) = \chi_{\Lambda p}(a)$, i.e. on momenta by $p \mapsto \Lambda p$ ($\Lambda = \pi(h)$ for $SL(2, \mathbb C)$).
>
> *Source (planned): Woit, §20.4 · written here (sign of $p\cdot a$ to be matched to [[§C3.5 Quantum Poincaré Transformations#^pr-c3-5-1|Principle §C3.5.1]])*

^def-cb-14-6

> [!definition] Definition §CB.14.7: The Euclidean Group of the Plane
> $ISO(2) = E(2) = \mathbb R^2\rtimes SO(2)$ ([[§CB.14★ The Poincaré Group and Induced Representations#^def-cb-14-1|Def. §CB.14.1]]), with $SO(2)$ acting by rotation; its double cover is $\mathbb C\rtimes U(1)$ with $e^{i\theta/2}$ acting on $\mathbb C$ by multiplication with $e^{i\theta}$.
>
> *Source (planned): Woit, §18.1 · written here*

^def-cb-14-7

> [!theorem] Theorem §CB.14.8: The Little Groups in SL(2,ℂ)
> For the action of $SL(2, \mathbb C)$ on momenta (Def. §CB.14.6):
> 1. the stabilizer of $k = (m, 0, 0, 0)$, $m > 0$, is $SU(2)$, the double cover of the little group $SO(3)$;
> 2. the stabilizer of $k = (\kappa, 0, 0, \kappa)$, $\kappa > 0$, is conjugate in $SL(2, \mathbb C)$ to $\Bigl\{\begin{pmatrix} e^{i\theta/2} & z\\ 0 & e^{-i\theta/2}\end{pmatrix} : \theta \in \mathbb R, z \in \mathbb C\Bigr\}$, isomorphic to the double cover $\mathbb C\rtimes U(1)$ of $ISO(2)$ ([[§CB.14★ The Poincaré Group and Induced Representations#^def-cb-14-7|Def. §CB.14.7]]).
>
> *Source (planned): Woit, Ch. 42 · the user's PHY 513 notes, Ch. 7 §7.7 · [[§C3.6★ Particle States and the Little Group#^thm-c3-6-6|Theorem §C3.6.6]], [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-1|Theorem §C3.7.1]]*

^thm-cb-14-8

> [!proof]- Proof (to be filled)
> *To be filled ($\lambda\tilde k\lambda^\dagger = \tilde k$ with $\tilde k = m\mathbb 1$ means $\lambda\lambda^\dagger = \mathbb 1$; with $\tilde k$ of rank one, $\lambda$ fixes its image line up to a phase).*

^pf-cb-14-8

## Induced representations

> [!definition] Definition §CB.14.9: Induced Representation of ℝⁿ ⋊ H
> Let $G = \mathbb R^n\rtimes H$ with $H$ a matrix Lie group acting linearly on $\mathbb R^n$ and on momenta as in Def. §CB.14.6; let $\mathcal O$ be an $H$-orbit of momenta with an $H$-invariant measure $\mu$, $k \in \mathcal O$, $H_k$ the stabilizer of $k$, $\sigma$ a unitary representation of $H_k$ on a Hilbert space $\mathcal K$, and $p \mapsto L(p) \in H$ a measurable choice with $L(p)k = p$. The **induced representation** acts on $L^2(\mathcal O, \mu; \mathcal K)$ by
>
> $$
> \bigl(U(a, h)\psi\bigr)(p) = e^{ip\cdot a}\,\sigma\bigl(W(h, p)\bigr)\,\psi(h^{-1}p), \qquad W(h, p) = L(p)^{-1}\,h\,L(h^{-1}p) \in H_k .
> $$
>
> *Source (planned): Woit, §20.4, Ch. 42 · the course's form: [[§C3.6★ Particle States and the Little Group#^thm-c3-6-4|Theorem §C3.6.4]] (signs and normalization to be matched when the proof is written)*

^def-cb-14-9

> [!theorem] Theorem §CB.14.10: The Induced Representation Is Unitary
> $U$ of [[§CB.14★ The Poincaré Group and Induced Representations#^def-cb-14-9|Def. §CB.14.9]] is a unitary representation of $G$; $W(h, p)$ lies in $H_k$ and satisfies $W(hh', p) = W(h, p)W(h', h^{-1}p)$; a different choice of $L$ or of $k \in \mathcal O$ gives an equivalent representation.
>
> *Source (planned): Woit, §20.4 · the course: [[§C3.6★ Particle States and the Little Group#^thm-c3-6-3|Theorem §C3.6.3]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-4|Theorem §C3.6.4]]*

^thm-cb-14-10

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-14-10

> [!theorem] Theorem §CB.14.11: Irreducibility (Mackey)
> The induced representation of [[§CB.14★ The Poincaré Group and Induced Representations#^def-cb-14-9|Def. §CB.14.9]] is irreducible if and only if $\sigma$ is irreducible; induced representations from different orbits, or from inequivalent $\sigma$, are inequivalent.
>
> *Source (planned): Woit, §20.4 (to be checked whether proved there) · Mackey's theory*

^thm-cb-14-11

> [!proof]- Proof (to be filled)
> *To be filled, or stated with a precise reference.*

^pf-cb-14-11

> [!theorem] Theorem §CB.14.12: Every Irreducible Unitary Representation Is Induced (Wigner–Mackey)
> If the $H$-orbits on momenta are locally closed (true for the Lorentz group acting on $\mathbb R^{1,3}$), every irreducible unitary representation of $\mathbb R^n\rtimes H$ is equivalent to an induced representation (Def. §CB.14.9) from exactly one orbit $\mathcal O$ and one irreducible $\sigma$, up to equivalence. For $\mathbb R^{1,3}\rtimes SL(2, \mathbb C)$ this is Wigner's classification of particles by mass and spin or helicity.
>
> *Source (planned): Woit, Ch. 42 · Mackey's theory · the course: [[§C3.6★ Particle States and the Little Group#^pr-c3-6-1|Principle §C3.6.1]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-2|Theorem §C3.6.2]]*

^thm-cb-14-12

> [!proof]- Proof (to be filled)
> *Stated only, with a precise reference to be added (beyond the course).*

^pf-cb-14-12

The course's induced representation and its little groups, in [[§C3.6★ Particle States and the Little Group|§C3.6★]] and [[§C3.7★ Massless Particles and Helicity|§C3.7★]]:

![[§C3.6★ Particle States and the Little Group#^thm-c3-6-4]]

![[§C3.7★ Massless Particles and Helicity#^thm-c3-7-1]]

> [!remark]- Connections
> - The semidirect structure is why momentum labels states first and spin second: translations form an abelian normal subgroup, so they can be diagonalized first ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-4|Theorem §CB.3.4]] in its infinite-dimensional form), and the Lorentz group only permutes their eigenvalues.
> - The double cover of $ISO(2)$ in Theorem §CB.14.8 is why helicities of massless particles may be half-integers ([[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]]).
> - **Used in**: Definitions §CB.14.1–§CB.14.4 — [[§C3.5 Quantum Poincaré Transformations#^pr-c3-5-1|Principle §C3.5.1]], [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-5|Theorem §C3.5.5]]; Theorem §CB.14.8 — [[§C3.6★ Particle States and the Little Group#^thm-c3-6-6|Theorem §C3.6.6]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-7|Theorem §C3.6.7]], [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-1|Theorem §C3.7.1]], [[§C4.3★ Massive Polarization Vectors and Plane Waves|§C4.3★]]; Definition §CB.14.9–Theorem §CB.14.12 — [[§C3.6★ Particle States and the Little Group#^thm-c3-6-4|Theorem §C3.6.4]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-5|Theorem §C3.6.5]], [[§C3.6★ Particle States and the Little Group#^pr-c3-6-1|Principle §C3.6.1]], [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]].
