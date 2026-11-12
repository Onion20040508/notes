---
type: section
subject: "[[Functional Analysis]]"
chapter: 9
section: 47
tags: [functional-analysis, math556, companion]
---
← [[§46 The Transpose]] · ↑ [[· 10 Functional Analysis and Quantum Mechanics]] · [[§48 The Completeness Relation]] →

*Companion — Thread: functionals. Bras as elements of the dual space.*

> [!remark] Remark: Conventions
> Mathematics and physics put the conjugate on different slots of the inner product. In these notes $(x, y)$ is linear in $x$ and conjugate-linear in $y$ (Definition [[§22 Definition and Examples#^def-22-1|§22.1]]); Dirac's $\langle y | x \rangle$ is linear in $x$ and conjugate-linear in $y$. The dictionary, used throughout this chapter, is
>
> $$
> \langle y | x \rangle = (x, y) .
> $$
>
> The state space of a quantum system is a Hilbert space $H$ over $\mathbb{C}$, in practice [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|separable]]; for a particle in $\mathbb{R}^n$ it is $L^2(\mathbb{R}^n)$.

^rem-47-1

## The Dual Space

Recall (Definition [[§31 Dual Spaces#^def-31-1|§31.1]]) that for a normed linear space $X$ over $\mathbb{F}$ the set of bounded linear functionals on $X$ (Definition [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-1|§26.1]]), $X' = \mathcal{L}(X, \mathbb{F})$, with pointwise addition and scalar multiplication and with the norm $\|\ell\| = \sup_{x \neq 0} |\ell(x)|/\|x\|$, is the dual space of $X$; it is a normed linear space (Theorem [[§30 Boundedness and Continuity#^thm-30-8|§30.8]]). Physics texts often write $H^{\ast}$ for the dual of a Hilbert space $H$; these notes write $H'$ throughout.

In this chapter a constant $c \ge 0$ is called *admissible* for $\ell \in X'$ if $|\ell(x)| \le c\,\|x\|$ for all $x \in X$. By Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]], parts (b) and (c), applied to the bounded linear map $\ell : X \to \mathbb{F}$, the norm $\|\ell\|$ is itself an admissible constant, $|\ell(x)| \le \|\ell\|\,\|x\|$ for all $x$, and it is the smallest one:

$$
\|\ell\| = \min\{ c \ge 0 : |\ell(x)| \le c\,\|x\| \text{ for all } x \in X \} .
$$

(For $X = \{0\}$, which Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]] excludes, $\ell = 0$ and $\|\ell\| = 0$ by Definition [[§30 Boundedness and Continuity#^def-30-3|§30.3]], and both statements hold trivially.)

> [!remark]- Connections
> - The same space in Chapter 6: $X' = \mathcal{L}(X, \mathbb{F})$, [[§30 Boundedness and Continuity#^def-30-4|Def. §30.4]] with [[§30 Boundedness and Continuity#^def-30-2|Def. §30.2]].
> - The algebraic dual (no boundedness) in finite dimensions: [[§12 Duality#^ladr-3-110|LADR 3.110]]; [[§21 Linear Algebra Toolkit#^def-21-1|591 Def. §21.1]].
> - The same norm in Chapter 6: the operator norm for $Y = \mathbb{F}$, [[§30 Boundedness and Continuity#^def-30-3|Def. §30.3]].
> - The operator norm in finite dimensions: [[§28 Consequences of Singular Value Decomposition#^ladr-7-86|LADR 7.86]], [[§28 Consequences of Singular Value Decomposition#^ladr-7-87|LADR 7.87]].

## The Riesz Map

> [!theorem] Theorem §47.1: The Riesz Map
> Let $H$ be a Hilbert space and define $R : H \to H'$ by $R(a) = \ell_a$, $\ell_a(x) = (x, a)$. Then:
> 1. $R$ is a bijection;
> 2. $R$ is *conjugate-linear*: $R(ca + b) = \bar{c}\, R(a) + R(b)$ for $a, b \in H$, $c \in \mathbb{F}$;
> 3. $R$ is isometric: $\|R(a)\| = \|a\|$.

^thm-47-1

> [!proof]+ Proof
> $R(a) \in H'$ is part (1) of the Riesz representation theorem (Theorem [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-5|§26.5]]); every $\ell \in H'$ equals $R(a)$ for exactly one $a$ by part (2); so $R$ is a bijection. Conjugate-linearity is conjugate-linearity of the inner product in its second argument: $(x, ca + b) = \bar{c}(x, a) + (x, b)$. For the isometry, [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|Cauchy–Schwarz]] shows $c = \|a\|$ is admissible for $\ell_a$, so $\|\ell_a\| \le \|a\|$; conversely, if $c$ is admissible then $\|a\|^2 = \ell_a(a) \le c\,\|a\|$, so $c \ge \|a\|$ when $a \neq 0$ (and the case $a = 0$ is trivial).

^pf-47-1

*Uses:* [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-5|§26.5]], [[§22 Definition and Examples#^def-22-1|Def. §22.1]], [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]], [[§31 Dual Spaces#^def-31-1|Def. §31.1]]

> [!remark]- Connections
> - Finite-dimensional version: [[Riesz representation theorem]] ([[§21 Orthonormal Bases#^ladr-6-42|LADR 6.42]], [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-58|LADR 6.58]]).

> [!remark] Remark
> The Riesz map needs no basis, only the inner product; in this sense a Hilbert space is canonically identified with its dual. Contrast [[§21 Linear Algebra Toolkit#^prop-21-2|MATH 591]]: a finite-dimensional vector space is isomorphic to its dual, but only after choosing a basis — the inner product is exactly the extra structure that removes the choice. The price is that $R$ is conjugate-linear, so over $\mathbb{C}$ the identification is with the complex conjugate space $\overline{H}$; in finite dimensions this is the conjugate transpose (Example [[§47 Bras, Kets, and the Riesz Map#^ex-47-1|§47.1]]). For an arbitrary Banach space there is no inner product, and the dual space is a genuinely new object ([[§31 Dual Spaces|§31]], [[§36 Duality in Normed Spaces|§36]]).

^rem-47-2

> [!remark]- Connections
> - The basis-dependent isomorphism $V \cong V^{\ast}$: [[§21 Linear Algebra Toolkit#^prop-21-2|591 §21.2]] (dual basis), [[§12 Duality#^ladr-3-110|LADR 3.110]]; isomorphisms from non-degenerate pairings: [[§21 Linear Algebra Toolkit#^thm-21-5|591 §21.5]].

> [!example] Example §47.1: The Riesz Map on $\mathbb{C}^n$ is the Conjugate Transpose
> Let $H = \mathbb{C}^n$ with $(x, a) = \sum_{j=1}^n x_j\, \bar{a}_j$, and write vectors as columns. The functional corresponding to a column vector $a$ is the conjugate transpose $a^\dagger = \bar{a}^{T}$, a row vector acting by matrix multiplication:
>
> $$
> R(a)(x) = \ell_a(x) = (x, a) = \sum_{j=1}^n \bar{a}_j\, x_j = a^\dagger x .
> $$
>
> The conjugation is what makes $R$ conjugate-linear (Theorem [[§47 Bras, Kets, and the Riesz Map#^thm-47-1|§47.1]](2)): $(ca)^\dagger = \bar{c}\, a^\dagger$, so $R(ca) = \bar{c}\, R(a)$.

^ex-47-1

## Dirac Notation

> [!definition] Definition §47.1: Kets and Bras
> Let $H$ be a Hilbert space. For $a \in H$, the **ket** $|a\rangle$ denotes $a$ itself, and the **bra** $\langle a|$ denotes the functional $R(a) = \ell_a \in H'$, so that
>
> $$
> \langle a | x \rangle := \langle a|\,(x) = (x, a) .
> $$

^def-47-1

> [!definition] Definition §47.2: Outer Products
> Let $H$ be a Hilbert space, with kets and bras as in Definition [[§47 Bras, Kets, and the Riesz Map#^def-47-1|§47.1]]. For $a, b \in H$, the **outer product** $|a\rangle\langle b|$ is the map
>
> $$
> |a\rangle\langle b| : H \to H, \qquad x \mapsto \langle b | x \rangle\, a = (x, b)\, a .
> $$

^def-47-2

> [!remark] Remark
> Theorem [[§47 Bras, Kets, and the Riesz Map#^thm-47-1|§47.1]] is the precise content of the physicists' rule that “every bra is the adjoint of a ket, and every linear functional is a bra”: the second half is [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-5|Riesz's theorem]] and is false without completeness and boundedness. The rule $\langle ca| = \bar{c}\,\langle a|$ is conjugate-linearity of $R$. The outer product $|a\rangle\langle b|$ is a bounded operator of rank at most one (Proposition [[§47 Bras, Kets, and the Riesz Map#^prop-47-2|§47.2]]).

^rem-47-3

> [!theorem] Proposition §47.2: Outer Products are Bounded of Rank at Most One
> Let $H$ be a Hilbert space and $a, b \in H$. The outer product $|a\rangle\langle b|$ (Definition [[§47 Bras, Kets, and the Riesz Map#^def-47-2|§47.2]]) is linear, has range in $\operatorname{span}\{a\}$, and satisfies
>
> $$
> \bigl\|\, |a\rangle\langle b|\,x \bigr\| \le \|a\|\,\|b\|\,\|x\| \qquad \text{for all } x \in H .
> $$
>
> So it is a bounded linear map $H \to H$ of rank at most one.

^prop-47-2

> [!proof]+ Proof
> *Linear in $x$:* the inner product is linear in its first argument, so $|a\rangle\langle b|\,(\alpha x + \beta y) = (\alpha x + \beta y, b)\, a = \alpha (x, b)\, a + \beta (y, b)\, a$. *Range:* each value $(x, b)\, a$ is a scalar multiple of $a$, so the range lies in $\operatorname{span}\{a\}$, of dimension at most one. *Bound:* by Cauchy–Schwarz (Theorem [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]]), $\|(x, b)\, a\| = |(x, b)|\,\|a\| \le \|x\|\,\|b\|\,\|a\|$.

^pf-47-2

*Uses:* [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]]

> [!remark]- Connections
> - Used in Quantum Mechanics: Dirac's axioms for kets, bras and operators, of which Theorem [[§47 Bras, Kets, and the Riesz Map#^thm-47-1|§47.1]] and Definitions [[§47 Bras, Kets, and the Riesz Map#^def-47-1|§47.1]] and [[§47 Bras, Kets, and the Riesz Map#^def-47-2|§47.2]] are the rigorous content — [[§C1.2 Kets, Bras, Operators and Matrix Representations#^pr-c1-2-1|QM Principle §C1.2.1]], [[§C1.2 Kets, Bras, Operators and Matrix Representations#^rem-c1-2-1|QM Remark: What the axioms add to level B, and what they are rigorously]].
