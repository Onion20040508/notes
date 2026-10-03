---
type: section
subject: "[[Functional Analysis]]"
chapter: 7
section: 24
tags: [functional-analysis, math556, companion]
---
← [[§23 Sesquilinear Forms and the Lax–Milgram Theorem]] · ↑ [[· 7 Functional Analysis and Quantum Mechanics]] · [[§25 The Completeness Relation]] →

*Companion — Thread: functionals. Bras as elements of the dual space.*

> [!remark] Remark: Conventions
> Mathematics and physics put the conjugate on different slots of the inner product. In these notes $(x, y)$ is linear in $x$ and conjugate-linear in $y$ (Definition [[§16 Definition and Examples#^def-16-1|§16.1]]); Dirac's $\langle y | x \rangle$ is linear in $x$ and conjugate-linear in $y$. The dictionary, used throughout this chapter, is
>
> $$
> \langle y | x \rangle = (x, y) .
> $$
>
> The state space of a quantum system is a Hilbert space $H$ over $\mathbb{C}$, in practice separable; for a particle in $\mathbb{R}^n$ it is $L^2(\mathbb{R}^n)$.

^rem-24-1

## The Dual Space

> [!definition] Definition §24.1: Dual Space and Dual Norm
> Let $X$ be a normed linear space over $\mathbb{F}$. The **dual space** $X^{\ast}$ is the set of bounded linear functionals on $X$ (Definition [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^def-19-1|§19.1]]), with pointwise addition and scalar multiplication. For $\ell \in X^{\ast}$, its **norm** is
>
> $$
> \|\ell\| = \inf\{ c \ge 0 : |\ell(x)| \le c\,\|x\| \text{ for all } x \in X \} .
> $$

^def-24-1

> [!remark]- Connections
> - The same space in Chapter 6: $X^* = \mathcal{L}(X, \mathbb{F})$, [[§21 Boundedness and Continuity#^def-21-3|Def. §21.3]] with [[§21 Boundedness and Continuity#^def-21-2|Def. §21.2]].
> - The algebraic dual (no boundedness) in finite dimensions: [[§12 Duality#^ladr-3-110|LADR 3.110]]; [[§17 Linear Algebra Toolkit#^def-17-1|591 Def. §17.1]].

> [!theorem] Lemma §24.1: The Dual Norm
> For $\ell \in X^*$, the infimum $\|\ell\|$ is itself an admissible constant: $|\ell(x)| \le \|\ell\|\,\|x\|$ for all $x$. Moreover $X^*$ is a linear space and $\|\cdot\|$ is a norm on it.

^lem-24-1

> [!proof]+ Proof
> Fix $x$. For every admissible $c$, $|\ell(x)| \le c\|x\|$; taking the infimum over $c$ gives $|\ell(x)| \le \|\ell\|\,\|x\|$. If $c_1, c_2$ are admissible for $\ell_1, \ell_2$, then $|(\ell_1 + \ell_2)(x)| \le (c_1 + c_2)\|x\|$ and $|(k\ell_1)(x)| \le |k| c_1 \|x\|$; so $X^*$ is closed under the operations, and taking infima gives subadditivity and $\|k\ell\| \le |k|\,\|\ell\|$, with equality for $k \neq 0$ by applying the same to $k^{-1}(k\ell)$. If $\|\ell\| = 0$ then $|\ell(x)| \le 0$ for all $x$, so $\ell = 0$.

^pf-24-1

*Uses:* [[§24 Bras, Kets, and the Riesz Map#^def-24-1|Def. §24.1]], [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]]

> [!remark]- Connections
> - The same statement for all bounded linear maps: [[§21 Boundedness and Continuity#^prop-21-1|§21.1]], [[§21 Boundedness and Continuity#^thm-21-5|§21.5]].
> - The operator norm in finite dimensions: [[§27 Consequences of Singular Value Decomposition#^ladr-7-86|LADR 7.86]], [[§27 Consequences of Singular Value Decomposition#^ladr-7-87|LADR 7.87]].

## The Riesz Map

> [!theorem] Theorem §24.2: The Riesz Map
> Let $H$ be a Hilbert space and define $R : H \to H^{\ast}$ by $R(a) = \ell_a$, $\ell_a(x) = (x, a)$. Then $R$ is a bijection, it is *conjugate-linear*,
>
> $$
> R(ca + b) = \bar{c}\, R(a) + R(b) \qquad (a, b \in H,\ c \in \mathbb{F}),
> $$
>
> and it is isometric: $\|R(a)\| = \|a\|$.

^thm-24-2

> [!proof]+ Proof
> $R(a) \in H^*$ is part (1) of the Riesz representation theorem (Theorem [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-19-2|§19.2]]); every $\ell \in H^*$ equals $R(a)$ for exactly one $a$ by part (2); so $R$ is a bijection. Conjugate-linearity is conjugate-linearity of the inner product in its second argument: $(x, ca + b) = \bar{c}(x, a) + (x, b)$. For the isometry, [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|Cauchy–Schwarz]] shows $c = \|a\|$ is admissible for $\ell_a$, so $\|\ell_a\| \le \|a\|$; conversely, if $c$ is admissible then $\|a\|^2 = \ell_a(a) \le c\,\|a\|$, so $c \ge \|a\|$ when $a \neq 0$ (and the case $a = 0$ is trivial).

^pf-24-2

*Uses:* [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-19-2|§19.2]], [[§16 Definition and Examples#^def-16-1|Def. §16.1]], [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|§17.1]], [[§24 Bras, Kets, and the Riesz Map#^def-24-1|Def. §24.1]]

> [!remark]- Connections
> - Finite-dimensional version: [[Riesz representation theorem]] ([[§20 Orthonormal Bases#^ladr-6-42|LADR 6.42]], [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-58|LADR 6.58]]).

> [!remark] Remark
> The Riesz map needs no basis, only the inner product; in this sense a Hilbert space is canonically identified with its dual. Contrast [[§17 Linear Algebra Toolkit#^prop-17-2|MATH 591]]: a finite-dimensional vector space is isomorphic to its dual, but only after choosing a basis — the inner product is exactly the extra structure that removes the choice. The price is that $R$ is conjugate-linear, so over $\mathbb{C}$ the identification is with the complex conjugate space $\overline{H}$. In finite dimensions this is the familiar fact that the functional corresponding to a column vector $a$ is the conjugate transpose $a^\dagger$. For an arbitrary Banach space there is no inner product, and the dual space is a genuinely new object; this is where the course is heading.

^rem-24-2

> [!remark]- Connections
> - The basis-dependent isomorphism $V \cong V^*$: [[§17 Linear Algebra Toolkit#^prop-17-2|591 §17.2]] (dual basis), [[§12 Duality#^ladr-3-110|LADR 3.110]]; isomorphisms from non-degenerate pairings: [[§17 Linear Algebra Toolkit#^thm-17-5|591 §17.5]].

## Dirac Notation

> [!definition] Definition §24.2: Kets, Bras, and Outer Products
> Let $H$ be a Hilbert space. For $a \in H$, the **ket** $|a\rangle$ denotes $a$ itself, and the **bra** $\langle a|$ denotes the functional $R(a) = \ell_a \in H^{\ast}$, so that
>
> $$
> \langle a | x \rangle := \langle a|\,(x) = (x, a) .
> $$
>
> For $a, b \in H$, the **outer product** $|a\rangle\langle b|$ is the map
>
> $$
> |a\rangle\langle b| : H \to H, \qquad x \mapsto \langle b | x \rangle\, a = (x, b)\, a .
> $$

^def-24-2

> [!remark] Remark
> Theorem [[§24 Bras, Kets, and the Riesz Map#^thm-24-2|§24.2]] is the precise content of the physicists' rule that “every bra is the adjoint of a ket, and every linear functional is a bra”: the second half is [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-19-2|Riesz's theorem]] and is false without completeness and boundedness. The rule $\langle ca| = \bar{c}\,\langle a|$ is conjugate-linearity of $R$. The outer product $|a\rangle\langle b|$ is linear in $x$, has range in $\operatorname{span}\{a\}$, and satisfies $\|\,|a\rangle\langle b|\,x\| \le \|a\|\,\|b\|\,\|x\|$ by [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|Cauchy–Schwarz]]; it is a bounded operator of rank at most one.

^rem-24-3

> [!remark]- Connections
> - Used in Quantum Mechanics: Dirac's axioms for kets, bras and operators, of which Theorem §24.2 and Definition §24.2 are the rigorous content — [[§C1.2 Kets, Bras, Operators and Matrix Representations#^pr-c1-2-1|QM Principle §C1.2.1]], [[§C1.2 Kets, Bras, Operators and Matrix Representations#^rem-c1-2-1|QM Remark: What the axioms add to level B, and what they are rigorously]].
