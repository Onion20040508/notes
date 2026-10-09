---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.1
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings]] →

*Sources (proofs written from these, each checked against the text): B. C. Hall, An Elementary Introduction to Groups and Representations, Chs. 2–5 (https://arxiv.org/abs/math-ph/0005032) · E. Meinrenken, Lie Groups and Lie Algebras, lecture notes, Toronto, Winter 2026, §§2.2, 2.5–2.6, 4 (https://www.math.toronto.edu/mein/teaching/LectureNotes/lie.pdf) · J. M. Lee, Introduction to Smooth Manifolds, 2nd ed., Props. 7.11, 8.41, 8.48, Thms. 8.46, 21.31 · Zuoqin Wang, Lie Groups (USTC), Lecture 12 · P. Etingof, Lie Groups and Lie Algebras (MIT 18.755), Prop. 3.15 · Differentiable Manifolds (591) §§11, 16, 25, 33, 35, 49–50 · the user's PHY 513 notes, Ch. 7 §7.2 (with the course's definitions and Theorem §CB.1.18 of PHY 513 Lecture 7, Part A), Ch. 1 §1.3 (the matrix groups, first written in [[§C1a.4 The Lorentz Group|§C1a.4]] and moved here in option-1 batch B3) · Yu §1.3, eqs. (1.50)–(1.57) · B. C. Hall, Quantum Theory for Mathematicians, Ch. 16 · H. Georgi, Lie Algebras in Particle Physics (2nd ed.), §§2.1–2.2 · Yu Zhao-Huan, 量子场论讲义, §3.2 · Peskin & Schroeder, §3.1 · P. Woit, Quantum Theory, Groups and Representations, Ch. 5 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf).*

How do a matrix group and its Lie algebra determine each other, and which statements about representations may be checked on generators alone? The course's definitions of a matrix Lie group and of its Lie algebra are stated here ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-3|Def. §CB.1.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|Def. §CB.1.11]]); the Math vault has Lie groups, Lie algebras and the tangent spaces of the classical groups ([[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-1|591 Def. §50.1]], [[§49 Lie Bracket and Lie Algebra#^def-49-2|591 Def. §49.2]], [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]]). This section and [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings|§CB.2]] supply what lies between them and what the physics chapters use without proof. Here: the matrix exponential, one-parameter subgroups, why the Lie algebra is a *real* Lie algebra, the closed-subgroup theorem, the Lie algebra as the tangent space at the identity, and the Lie algebras of the classical groups; in [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings|§CB.2]]: homomorphisms and their differentials, the identity component, the adjoint representation, and the covering and integration theorems behind SU(2) → SO(3) and SL(2,ℂ) → SO⁺(1,3). Statements are numbered in reading order with one counter per section (Definition §CB.1.4, Theorem §CB.1.5, …); boxes shown as embeds keep their home numbers.

## Recalled: Lie groups, Lie algebras and matrix groups

A Lie group in general, defined in 591:

![[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-1]]

A (real) Lie algebra, defined in 591; the commutator of any associative product is a Lie bracket, proved there ([[§49 Lie Bracket and Lie Algebra#^prop-49-3|591 Prop. §49.3]]):

![[§49 Lie Bracket and Lie Algebra#^def-49-2]]

![[§49 Lie Bracket and Lie Algebra#^prop-49-3]]

The matrix groups of the course (first written in [[§C1a.4 The Lorentz Group|§C1a.4]], moved here in option-1 batch B3; their action on spacetime stays there):

> [!definition] Definition §CB.1.1: Matrix Groups
> A set of invertible matrices closed under products and inverses is a group under matrix multiplication ([[§1 The Definition of a Group#^def-1-1|493 Def. §1.1]]; associativity is automatic), and a subset of one that is itself such a group is a subgroup ([[§4 Subgroups#^def-4-1|493 Def. §4.1]]). The ones used in field theory:
> - $O(N)$, $SO(N)$: real $N\times N$ with $O^{\mathsf T}O = \mathbb 1$, and in addition $\det O = 1$ ([[§3 Basic Examples of Groups#^def-3-8|493 Def. §3.8]], [[§3 Basic Examples of Groups#^def-3-9|493 Def. §3.9]]); $U(N)$, $SU(N)$: complex with $U^\dagger U = \mathbb 1$, and in addition $\det U = 1$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-10|591 Def. §11.10]]);
> - $O(1,3)$: real $4\times4$ with $\Lambda^{\mathsf T}g\Lambda = g$; $SO(1,3)$: in addition $\det\Lambda = 1$; $SO^+(1,3)$ (also $SO^\uparrow(1,3)$, $L^\uparrow_+$): in addition $\Lambda^0{}_0 \ge 1$.
>
> $O(1,3)$ is $O(4)$ with the identity form replaced by $g$; there is a chain of subgroups $SO(2) < SO(3) < SO^+(1,3) < SO(1,3) < O(1,3)$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.3 (Definition "Groups, subgroups, and the matrix groups") · Yu §1.3, eqs. (1.50)–(1.57)*

^def-cb-1-1

That $O(1,3)$ is a group, that $\Lambda^{-1} = g^{-1}\Lambda^{\mathsf T}g$ needs no inversion, that $\Lambda^{\mathsf T}$ is again Lorentz ($\Lambda g\Lambda^{\mathsf T} = g$, the "row form"), and that $\det\Lambda = \pm1$ and $|\Lambda^0{}_0| \ge 1$, are [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-3|REL Theorem §B1.2.3]] and [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-4|REL Theorem §B1.2.4]].

The complex special linear group, the group of the course's Weyl matrices ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]) and, through the spin group, of Minkowski space ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover|§CB.15]]):

> [!definition] Definition §CB.1.2: The Group SL(2, C)
> $SL(2, \mathbb C) = \{\lambda \in M_2(\mathbb C) : \det\lambda = 1\}$, the complex $2\times2$ matrices of unit determinant, a group under matrix multiplication.
>
> *Source: the user's pre-course notes, §5.2 (Remark "SL(2,C) made explicit") · Yu Exercise 3.7(c)*

^def-cb-1-2

$SL(2, \mathbb C)$ is a group because $\det(\lambda_1\lambda_2) = \det\lambda_1\det\lambda_2$ and $\det\lambda^{-1} = (\det\lambda)^{-1}$; it has $8 - 2 = 6$ real parameters, as many as $SO^+(1,3)$.

The course's notion of a matrix Lie group (PHY 513 Lecture 7, Part A):

> [!definition] Definition §CB.1.3: Matrix Lie Group
> A **matrix Lie group** is a closed subgroup $G$ of $GL(n, \mathbb C)$; it is a smooth manifold, and $SO(3)$, $SU(2)$, $SO^+(1,3)$ are examples.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Definition "Group, algebra, representation") · Yu §3.2, eqs. (3.35)–(3.36) · PS §3.1, p. 38, eqs. (3.12)–(3.13) · Hall, Defs. 16.1, 16.10, 16.19, Prop. 16.20 · Georgi §§2.1–2.2, eqs. (2.4)–(2.5), (2.18)*

^def-cb-1-3

## The exponential map

> [!definition] Definition §CB.1.4: Matrix Exponential
> For $X \in M_n(\mathbb C)$ the **matrix exponential** is
>
> $$
> e^X = \exp X = \sum_{k=0}^\infty \frac{X^k}{k!}, \qquad X^0 = \mathbb 1 ,
> $$
>
> the limit of the partial sums in the operator norm $\|X\| = \sup_{|v| = 1}|Xv|$ on $M_n(\mathbb C) \cong \mathbb C^{n^2}$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-2|591 Def. §11.2]]); that the limit exists is Theorem §CB.1.5.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §1, eq. (3.1) · Woit, Quantum Theory, Groups and Representations, Ch. 5*

^def-cb-1-4

> [!theorem] Theorem §CB.1.5: Convergence and Algebraic Properties of the Exponential
> For $X, Y \in M_n(\mathbb C)$ and $s, t \in \mathbb R$:
> 1. the series of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-4|Def. §CB.1.4]] converges absolutely, uniformly on every bounded set of $X$, and $\|e^X\| \le e^{\|X\|}$; $X \mapsto e^X$ is continuous (indeed smooth);
> 2. $e^0 = \mathbb 1$, and $e^X$ is invertible with $(e^X)^{-1} = e^{-X}$;
> 3. if $XY = YX$, then $e^{X + Y} = e^Xe^Y$; in particular $e^{(s + t)X} = e^{sX}e^{tX}$;
> 4. $e^{SXS^{-1}} = S\,e^X S^{-1}$ for invertible $S$; $(e^X)^{\mathsf T} = e^{X^{\mathsf T}}$, $\overline{e^X} = e^{\bar X}$, $(e^X)^\dagger = e^{X^\dagger}$;
> 5. $s \mapsto e^{sX}$ is differentiable with $\frac{d}{ds}e^{sX} = Xe^{sX} = e^{sX}X$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §1, Props. 3.1, 3.3, 3.4 · Meinrenken, Lie Groups and Lie Algebras, §2.2 (smoothness in X)*

^thm-cb-1-5

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §1, Props. 3.1–3.4 and their proofs (https://arxiv.org/abs/math-ph/0005032); the exchange of the double series, which Hall leaves to the reader, is written out in Step 4. Smoothness in X: E. Meinrenken, Lie Groups and Lie Algebras, lecture notes (Toronto, Winter 2026), §2.2 (https://www.math.toronto.edu/mein/teaching/LectureNotes/lie.pdf).*
>
> **Step 1** (norm inequalities). For $v \in \mathbb C^n$, $|XYv| \le \|X\|\,|Yv| \le \|X\|\,\|Y\|\,|v|$ and $|(X + Y)v| \le |Xv| + |Yv| \le (\|X\| + \|Y\|)|v|$; taking the supremum over $|v| = 1$,
>
> $$
> \|XY\| \le \|X\|\,\|Y\|, \qquad \|X + Y\| \le \|X\| + \|Y\|, \qquad\text{hence}\qquad \|X^k\| \le \|X\|^k \ \ (k \ge 0)
> $$
>
> by induction on $k$. $M_n(\mathbb C)$ with $\|\cdot\|$ is a finite-dimensional normed space, hence complete: every Cauchy sequence converges (Hall, Prop. 3.2).
>
> **Step 2** (absolute convergence; part 1). By Step 1, $\sum_{k\ge0}\|X^k/k!\| \le \sum_{k\ge0}\|X\|^k/k! = e^{\|X\|} < \infty$. The partial sums $S_N(X) = \sum_{k=0}^N X^k/k!$ are therefore Cauchy: for $N > M$, $\|S_N(X) - S_M(X)\| \le \sum_{k=M+1}^N\|X\|^k/k!$, a tail of a convergent real series. So $e^X = \lim_N S_N(X)$ exists, and $\|e^X\| = \lim_N\|S_N(X)\| \le e^{\|X\|}$. On a bounded set $\|X\| \le R$ the bound $\|X^k/k!\| \le R^k/k!$ does not depend on $X$, and $\sum R^k/k! < \infty$: by the Weierstrass M-test ([[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]], applied to each matrix entry) the convergence is uniform there. Each $S_N$ is a polynomial in the entries of $X$, hence continuous, and a uniform limit of continuous functions is continuous ([[§24 Uniform Convergence#^thm-24-2|451 Thm. §24.2]], entrywise): $X \mapsto e^X$ is continuous. Smoothness: each entry of $e^X$ is a power series in the $2n^2$ real coordinates of $X$ that converges absolutely on all of $M_n(\mathbb C)$ (majorized as above), hence a smooth function of them (Meinrenken, §2.2).
>
> **Step 3** (part 2, first half). $e^0 = \mathbb 1 + 0 + 0 + \cdots = \mathbb 1$, since $0^k = 0$ for $k \ge 1$ and $0^0 = \mathbb 1$ by convention.
>
> **Step 4** (the product of two exponential series). For any $X, Y$, multiply the partial sums:
>
> $$
> S_N(X)\,S_N(Y) = \sum_{k=0}^N\sum_{l=0}^N\frac{X^kY^l}{k!\,l!} = \sum_{m=0}^N\ \sum_{k+l=m}\frac{X^kY^l}{k!\,l!} + \sum_{\substack{k, l \le N\\ k + l > N}}\frac{X^kY^l}{k!\,l!} .
> $$
>
> The last sum has norm at most $\sum_{k + l > N}\frac{\|X\|^k\|Y\|^l}{k!\,l!} = \sum_{m > N}\frac{(\|X\| + \|Y\|)^m}{m!}$ (the real binomial theorem, where everything commutes), a tail of the series for $e^{\|X\| + \|Y\|}$, so it tends to $0$. Letting $N \to \infty$ and using that matrix multiplication is continuous:
>
> $$
> e^Xe^Y = \sum_{m=0}^\infty\ \sum_{k=0}^m\frac{X^kY^{m-k}}{k!\,(m-k)!} = \sum_{m=0}^\infty\frac1{m!}\sum_{k=0}^m\binom mk X^kY^{m-k} .
> $$
>
> **Step 5** (part 3). If $XY = YX$, the binomial theorem holds for $X + Y$: expanding $(X + Y)^m$ into $2^m$ words in $X$ and $Y$ and moving every $X$ to the left (allowed only because $XY = YX$) gives $(X + Y)^m = \sum_{k=0}^m\binom mk X^kY^{m-k}$. Step 4 then reads $e^Xe^Y = \sum_m(X + Y)^m/m! = e^{X + Y}$. ⚑ By-product: without $XY = YX$ this step fails, and the failure is measured by the commutator → [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]]. In particular $sX$ and $tX$ commute, so $e^{(s + t)X} = e^{sX}e^{tX}$.
>
> **Step 6** (part 2, second half). $X$ and $-X$ commute, so by Step 5 and Step 3, $e^Xe^{-X} = e^{X - X} = e^0 = \mathbb 1$, and likewise $e^{-X}e^X = \mathbb 1$: $e^X$ is invertible with inverse $e^{-X}$.
>
> **Step 7** (part 4). $(SXS^{-1})^k = SXS^{-1}SXS^{-1}\cdots SXS^{-1} = SX^kS^{-1}$ (each inner $S^{-1}S = \mathbb 1$), so $S_N(SXS^{-1}) = S\,S_N(X)\,S^{-1}$; the map $A \mapsto SAS^{-1}$ is linear on a finite-dimensional space, hence continuous, and $N \to \infty$ gives $e^{SXS^{-1}} = Se^XS^{-1}$. Likewise $(X^k)^{\mathsf T} = (X^{\mathsf T})^k$, $\overline{X^k} = \bar X^k$, $(X^k)^\dagger = (X^\dagger)^k$, so transposition, entrywise conjugation and the adjoint, each continuous (real-linear), map $S_N(X)$ to $S_N(X^{\mathsf T})$, $S_N(\bar X)$, $S_N(X^\dagger)$; pass to the limit.
>
> **Step 8** (part 5). Each entry $(e^{sX})_{ij} = \sum_k\frac{s^k}{k!}(X^k)_{ij}$ is a power series in the real variable $s$ with infinite radius of convergence ($|(X^k)_{ij}| \le \|X\|^k$). Term-by-term differentiation ([[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]], applied to real and imaginary parts) gives
>
> $$
> \frac{d}{ds}e^{sX} = \sum_{k\ge1}\frac{k\,s^{k-1}}{k!}X^k = X\sum_{k\ge1}\frac{s^{k-1}X^{k-1}}{(k-1)!} = Xe^{sX},
> $$
>
> and pulling the factor $X$ out on the right instead gives $e^{sX}X$.
>
> **What the proof shows.**
> - Every property except part 3 holds for all matrices; part 3 is exactly where commutativity is needed, and its failure is the subject of Theorem §CB.1.8.
> - Only the submultiplicative norm and completeness are used, so the same proof works for the exponential of any operator on a finite-dimensional space, e.g. of $d(X)$ in a representation ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]]).
> - Used next: the determinant (Theorem §CB.1.6), the logarithm (Theorem §CB.1.7) and the one-parameter subgroups $s \mapsto e^{sX}$ (Theorem §CB.1.10).

^pf-cb-1-5

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-4|Def. §CB.1.4]], [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]], [[§24 Uniform Convergence#^thm-24-2|451 Thm. §24.2]], [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]]

> [!theorem] Theorem §CB.1.6: Determinant of an Exponential
> For every $X \in M_n(\mathbb C)$, $\det e^X = e^{\operatorname{tr}X}$. In particular $e^X$ has determinant $1$ when $\operatorname{tr}X = 0$, and $\det e^X > 0$ when $X$ is real.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §4, Thm. 3.10 · used in [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-18|Theorem §CB.1.18]], Derivation, steps 1–2*

^thm-cb-1-6

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §4, Thm. 3.10 (https://arxiv.org/abs/math-ph/0005032). Hall treats diagonalizable, nilpotent and general $X$ separately; his nilpotent case already uses an upper-triangular form, and that form handles all three cases at once, which is the route followed here.*
>
> **Step 1** (triangular form). $X$ is an operator on the complex space $\mathbb C^n$, so some basis makes its matrix upper triangular ([[§16 Upper-Triangular Matrices#^ladr-5-47|LADR 5.47]]): $X = STS^{-1}$ with $S$ invertible (the change of basis) and $T$ upper triangular, $T_{ij} = 0$ for $i > j$. Its diagonal entries $\lambda_1, \dots, \lambda_n$ are the eigenvalues of $X$ ([[§16 Upper-Triangular Matrices#^ladr-5-41|LADR 5.41]]).
>
> **Step 2** (powers of a triangular matrix). If $A$, $B$ are upper triangular, then for $i > j$ every term of $(AB)_{ij} = \sum_lA_{il}B_{lj}$ vanishes (either $i > l$, so $A_{il} = 0$, or $l \ge i > j$, so $B_{lj} = 0$), and $(AB)_{ii} = \sum_lA_{il}B_{li}$ keeps only $l = i$, giving $A_{ii}B_{ii}$. By induction, $T^k$ is upper triangular with diagonal $\lambda_1^k, \dots, \lambda_n^k$.
>
> **Step 3** (the exponential of $T$). The partial sums $S_N(T) = \sum_{k\le N}T^k/k!$ are upper triangular with diagonal entries $\sum_{k\le N}\lambda_i^k/k!$. Entries converge separately ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], 1), so $e^T$ is upper triangular with diagonal $e^{\lambda_1}, \dots, e^{\lambda_n}$ (the zero entries stay zero in the limit).
>
> **Step 4** (conjugate back). By Theorem §CB.1.5, 4, $e^X = e^{STS^{-1}} = Se^TS^{-1}$. The determinant is multiplicative ([[§37 Determinants#^ladr-9-49|LADR 9.49]]), so $\det e^X = \det S\,\det e^T\,(\det S)^{-1} = \det e^T$, and the determinant of an upper-triangular matrix is the product of its diagonal entries ([[§37 Determinants#^ladr-9-48|LADR 9.48]]):
>
> $$
> \det e^X = \prod_{i=1}^ne^{\lambda_i} = e^{\lambda_1 + \cdots + \lambda_n} = e^{\operatorname{tr}T} = e^{\operatorname{tr}X},
> $$
>
> the last step because $\operatorname{tr}(STS^{-1}) = \operatorname{tr}(TS^{-1}S) = \operatorname{tr}T$ ([[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR 8.49]]).
>
> **Step 5** (the two consequences). If $\operatorname{tr}X = 0$, then $\det e^X = e^0 = 1$. If $X$ is real, $\operatorname{tr}X$ is real and $e^{\operatorname{tr}X} > 0$.
>
> **What the proof shows.**
> - $\det\circ\exp = \exp\circ\operatorname{tr}$: the determinant condition of $SL$, $SU$, $SO$ linearizes to a trace condition (used in Theorem §CB.1.17).
> - $\det e^X > 0$ for real $X$: no real exponential reaches a matrix of negative determinant, e.g. a reflection; this is the algebraic shadow of Theorem §CB.2.10, 2.

^pf-cb-1-6

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§16 Upper-Triangular Matrices#^ladr-5-47|LADR 5.47]], [[§16 Upper-Triangular Matrices#^ladr-5-41|LADR 5.41]], [[§37 Determinants#^ladr-9-48|LADR 9.48]], [[§37 Determinants#^ladr-9-49|LADR 9.49]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR 8.49]]

> [!theorem] Theorem §CB.1.7: The Logarithm Near the Identity
> For $A \in M_n(\mathbb C)$ with $\|A - \mathbb 1\| < 1$ the series $\log A = \sum_{k\ge1}\frac{(-1)^{k+1}}{k}(A - \mathbb 1)^k$ converges, $\log$ is continuous there, and $e^{\log A} = A$. For $\|X\| < \log 2$, $\|e^X - \mathbb 1\| < 1$ and $\log e^X = X$. Hence $\exp$ maps a neighbourhood of $0$ in $M_n(\mathbb C)$ homeomorphically onto a neighbourhood of $\mathbb 1$ in $GL(n, \mathbb C)$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §3, Lemma 3.5, Thm. 3.6*

^thm-cb-1-7

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §3, Lemma 3.5 and Thm. 3.6 with their proofs (https://arxiv.org/abs/math-ph/0005032); Hall's Exercise 4 (density of diagonalizable matrices) is done in Step 5, and the homeomorphism of the last sentence in Step 7.*
>
> **Step 1** (convergence and continuity of log). For $\|A - \mathbb 1\| \le r < 1$, Step 1 of the proof of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]] gives $\|(A - \mathbb 1)^k/k\| \le r^k/k$, and $\sum_kr^k/k < \infty$. So the series converges absolutely, uniformly on each set $\|A - \mathbb 1\| \le r$ (Weierstrass M-test, [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]]); its partial sums are polynomials, so $\log$ is continuous on $\{\|A - \mathbb 1\| < 1\}$ ([[§24 Uniform Convergence#^thm-24-2|451 Thm. §24.2]]).
>
> **Step 2** (the scalar case, Hall's Lemma 3.5). For real $x \in (-1, 1)$, $\frac{d}{dx}\log(1 - x) = -\frac1{1-x} = -\sum_{k\ge0}x^k$; integrating term by term from $0$ ([[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]]) and using $\log 1 = 0$ gives $\log(1 - x) = -\sum_{k\ge1}x^k/k$. With $z = 1 - x$ this is the series of the theorem, $\log z = \sum_{k\ge1}(-1)^{k+1}(z - 1)^k/k$, on the real interval $(0, 2)$. The same series defines an analytic function on the disc $|z - 1| < 1$ (radius of convergence $1$), and $e^{\log z}$ is analytic there and equals $z$ on $(0, 2)$; by the identity theorem ([[§CA.4 Contour Integration#^thm-ca-4-3|Theorem §CA.4.3]]) $e^{\log z} = z$ on the whole disc. For $|u| < \log 2$: $|e^u - 1| = |\sum_{k\ge1}u^k/k!| \le \sum_{k\ge1}|u|^k/k! = e^{|u|} - 1 < 1$, so $\log e^u$ is defined; it is analytic in $u$ on the disc $|u| < \log 2$ and equals $u$ for real $u$, hence everywhere there.
>
> **Step 3** (eigenvalues stay in the disc). If $Av = zv$ with $v \ne 0$, then $|(A - \mathbb 1)v| = |z - 1|\,|v|$ and $|(A - \mathbb 1)v| \le \|A - \mathbb 1\|\,|v|$, so $|z - 1| \le \|A - \mathbb 1\| < 1$. Likewise an eigenvalue $u$ of $X$ has $|u| \le \|X\|$.
>
> **Step 4** (diagonalizable $A$). Let $A = CDC^{-1}$ with $D = \operatorname{diag}(z_1, \dots, z_n)$ and $\|A - \mathbb 1\| < 1$. Then $A - \mathbb 1 = C(D - \mathbb 1)C^{-1}$, so $(A - \mathbb 1)^k = C\operatorname{diag}((z_i - 1)^k)C^{-1}$ (as in Step 7 of the proof of Theorem §CB.1.5), and summing (conjugation by $C$ is continuous), $\log A = C\operatorname{diag}(\log z_1, \dots, \log z_n)C^{-1}$, each $\log z_i$ defined by Step 3. By Theorem §CB.1.5, 4 and Step 2,
>
> $$
> e^{\log A} = C\operatorname{diag}\bigl(e^{\log z_1}, \dots, e^{\log z_n}\bigr)C^{-1} = C\operatorname{diag}(z_1, \dots, z_n)C^{-1} = A .
> $$
>
> **Step 5** (general $A$: approximation). Write $A = STS^{-1}$ with $T$ upper triangular ([[§16 Upper-Triangular Matrices#^ladr-5-47|LADR 5.47]]). Add small numbers to the diagonal: $T_m = T + \operatorname{diag}(\varepsilon_{1,m}, \dots, \varepsilon_{n,m})$ with $\varepsilon_{i,m} \to 0$ as $m \to \infty$, chosen so that the diagonal entries of $T_m$ are pairwise distinct. Then $A_m = ST_mS^{-1}$ has $n$ distinct eigenvalues ([[§16 Upper-Triangular Matrices#^ladr-5-41|LADR 5.41]]), so it is diagonalizable ([[§17 Diagonalizable Operators#^ladr-5-58|LADR 5.58]]), and $A_m \to A$. Since $\|A - \mathbb 1\| < 1$ and the norm is continuous, $\|A_m - \mathbb 1\| < 1$ for all large $m$. By Step 4, $e^{\log A_m} = A_m$; by continuity of $\log$ (Step 1) and of $\exp$ (Theorem §CB.1.5, 1), letting $m \to \infty$ gives $e^{\log A} = A$.
>
> **Step 6** (log undoes exp near 0). For $\|X\| < \log 2$, Step 1 of the proof of Theorem §CB.1.5 gives $\|e^X - \mathbb 1\| \le \sum_{k\ge1}\|X\|^k/k! = e^{\|X\|} - 1 < 1$, so $\log e^X$ is defined. If $X = CDC^{-1}$ is diagonalizable with eigenvalues $u_i$, $|u_i| < \log 2$ (Step 3), then $e^X = C\operatorname{diag}(e^{u_i})C^{-1}$ and, as in Step 4, $\log e^X = C\operatorname{diag}(\log e^{u_i})C^{-1} = C\operatorname{diag}(u_i)C^{-1} = X$ by Step 2. A general $X$ with $\|X\| < \log 2$ is the limit of diagonalizable $X_m$ with $\|X_m\| < \log 2$ (Step 5's construction), and $X \mapsto \log e^X$ is continuous on $\{\|X\| < \log 2\}$ (a composition of continuous maps), so $\log e^X = X$.
>
> **Step 7** (exp is a local homeomorphism). Put $U = \{X : \|X\| < \log 2\}$ and $B = \{A : \|A - \mathbb 1\| < 1\}$, both open. By Step 6, $\exp$ maps $U$ into $B$ and $\log\circ\exp = \mathrm{id}$ on $U$, so $\exp|_U$ is injective. Its image is $\exp(U) = \{A \in B : \log A \in U\}$: if $A = e^X$ with $X \in U$, then $\log A = X \in U$; conversely, if $A \in B$ and $\log A \in U$, then $A = e^{\log A}$ by Step 5. This set is open, as the preimage of the open $U$ under the continuous $\log : B \to M_n(\mathbb C)$; it contains $\mathbb 1 = e^0$, and it lies in $GL(n, \mathbb C)$ by Theorem §CB.1.5, 2. The inverse of $\exp|_U$ is $\log|_{\exp(U)}$, continuous by Step 1. So $\exp : U \to \exp(U)$ is a homeomorphism onto a neighbourhood of $\mathbb 1$.
>
> **What the proof shows.**
> - Near the identity every invertible matrix has exactly one small logarithm; this local invertibility is the input to one-parameter subgroups (Theorem §CB.1.10) and to the closed-subgroup theorem (Theorem §CB.1.15).
> - Globally $\exp$ is neither injective ($e^{2\pi i\mathbb 1} = e^0$) nor, on a general matrix group, surjective; only the local statement is used.
> - If $A$ is real, every term of the series is real, so $\log A$ is real (Hall, Thm. 3.6).

^pf-cb-1-7

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]], [[§24 Uniform Convergence#^thm-24-2|451 Thm. §24.2]], [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]], [[§CA.4 Contour Integration#^thm-ca-4-3|Theorem §CA.4.3]], [[§16 Upper-Triangular Matrices#^ladr-5-47|LADR 5.47]], [[§16 Upper-Triangular Matrices#^ladr-5-41|LADR 5.41]], [[§17 Diagonalizable Operators#^ladr-5-58|LADR 5.58]]

> [!theorem] Theorem §CB.1.8: Lie Product Formula and the Commutator as a Second-Order Term
> For $X, Y \in M_n(\mathbb C)$:
> 1. $e^{X + Y} = \lim_{m\to\infty}\bigl(e^{X/m}e^{Y/m}\bigr)^m$;
> 2. $e^{sX}e^{sY} = \exp\bigl(s(X + Y) + \frac{s^2}{2}[X, Y] + O(s^3)\bigr)$ as $s \to 0$ (the first terms of the Baker–Campbell–Hausdorff series);
> 3. $e^{sX}e^{sY}e^{-sX}e^{-sY} = \mathbb 1 + s^2[X, Y] + O(s^3)$ as $s \to 0$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §§3–4, Prop. 3.7, Thm. 3.9 (part 1); Ch. 4 §3, eq. (4.2) and Exercise 4 (part 2) · Meinrenken, Lie Groups and Lie Algebras, proof of Prop. 4.7 (part 3) · the second-order commutator is the content of [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-1|§C3.2, Remark: Two boosts make a rotation]]*

^thm-cb-1-8

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3, Prop. 3.7 and Thm. 3.9 with proofs, and Ch. 4 §3 (the series form (4.2) of Baker–Campbell–Hausdorff, which Exercise 4 there asks to check by multiplying out power series, as done in Step 5) (https://arxiv.org/abs/math-ph/0005032) · E. Meinrenken, Lie Groups and Lie Algebras (Toronto, Winter 2026), proof of Prop. 4.7, "by Taylor expansions" (https://www.math.toronto.edu/mein/teaching/LectureNotes/lie.pdf), written out in Step 6. Throughout, $a = \|X\| + \|Y\|$ and "$O(s^k)$" means a matrix of norm at most a constant times $|s|^k$ for $|s| \le 1$.*
>
> **Step 1** (the logarithm to first order; Hall, Prop. 3.7). For $\|B\| \le \frac12$, $\log(\mathbb 1 + B) - B = \sum_{k\ge2}(-1)^{k+1}B^k/k$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-7|Theorem §CB.1.7]]), so
>
> $$
> \|\log(\mathbb 1 + B) - B\| \le \|B\|^2\sum_{k\ge2}\frac{\|B\|^{k-2}}{k} \le \|B\|^2\sum_{k\ge2}\frac{(1/2)^{k-2}}{2} = \|B\|^2 .
> $$
>
> In the same way $\|\log(\mathbb 1 + B) - B + \frac12B^2\| \le \|B\|^3\sum_{k\ge3}\frac{(1/2)^{k-3}}{3} \le \|B\|^3$.
>
> **Step 2** (the product to first order). By Step 4 of the proof of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]] with $X/m$, $Y/m$ in place of $X$, $Y$,
>
> $$
> e^{X/m}e^{Y/m} = \mathbb 1 + \frac Xm + \frac Ym + C_m, \qquad C_m = \sum_{k + l \ge 2}\frac{X^kY^l}{m^{k+l}\,k!\,l!}, \qquad \|C_m\| \le \sum_{j\ge2}\frac{(a/m)^j}{j!} \le \frac{a^2e^a}{m^2}
> $$
>
> for $m \ge 1$, using $\sum_{j\ge2}t^j/j! \le t^2\sum_{j\ge2}t^{j-2}/(j-2)! = t^2e^t$ with $t = a/m \le a$.
>
> **Step 3** (take the logarithm). Put $B_m = X/m + Y/m + C_m$; $\|B_m\| \le a/m + a^2e^a/m^2 \to 0$, so $\|B_m\| \le \frac12$ for all large $m$. By Theorem §CB.1.7, $e^{X/m}e^{Y/m} = \exp(\log(\mathbb 1 + B_m))$, and by Step 1, $\log(\mathbb 1 + B_m) = B_m + E_m$ with $\|E_m\| \le \|B_m\|^2 \le \mathrm{const}/m^2$.
>
> **Step 4** (part 1). The $m$ factors of $(e^{X/m}e^{Y/m})^m = \bigl(\exp(B_m + E_m)\bigr)^m$ are exponentials of the same matrix, which commutes with itself, so by Theorem §CB.1.5, 3, $(e^{X/m}e^{Y/m})^m = \exp(m(B_m + E_m)) = \exp(X + Y + mC_m + mE_m)$. Both $mC_m$ and $mE_m$ have norm at most $\mathrm{const}/m \to 0$, and $\exp$ is continuous (Theorem §CB.1.5, 1), so the limit is $e^{X + Y}$.
>
> **Step 5** (part 2: the second-order term). As in Step 2, $e^{sX}e^{sY} = \mathbb 1 + B(s)$ with
>
> $$
> B(s) = s(X + Y) + s^2\Bigl(\frac{X^2}2 + XY + \frac{Y^2}2\Bigr) + R_3(s), \qquad \|R_3(s)\| \le \sum_{j\ge3}\frac{(a|s|)^j}{j!} \le a^3e^a|s|^3 ,
> $$
>
> the second-order terms being those with $k + l = 2$: $(k, l) = (2, 0), (1, 1), (0, 2)$. $\|B(s)\| \le \frac12$ for small $|s|$, and Step 1 gives $\log(\mathbb 1 + B(s)) = B(s) - \frac12B(s)^2 + O(s^3)$. Expand the square: $B(s)^2 = s^2(X + Y)^2 + O(s^3)$, and $(X + Y)^2 = X^2 + XY + YX + Y^2$ (all four terms; $XY \ne YX$ in general). So
>
> $$
> \log(e^{sX}e^{sY}) = s(X + Y) + s^2\Bigl(\frac{X^2}2 + XY + \frac{Y^2}2 - \frac{X^2 + XY + YX + Y^2}2\Bigr) + O(s^3) = s(X + Y) + \frac{s^2}2[X, Y] + O(s^3),
> $$
>
> and exponentiating (Theorem §CB.1.7) gives part 2.
>
> **Step 6** (part 3: the group commutator). Multiply the four series of $e^{sX}e^{sY}e^{-sX}e^{-sY}$ out, as in Step 4 of the proof of Theorem §CB.1.5 applied three times. The terms of total degree $j \ge 3$ in $s$ together have norm at most $\sum_{j\ge3}(2a|s|)^j/j! \le (2a)^3e^{2a}|s|^3$, the degree-$\ge3$ part of the majorant $e^{|s|\|X\|}e^{|s|\|Y\|}e^{|s|\|X\|}e^{|s|\|Y\|} = e^{2a|s|}$; so they are $O(s^3)$. The terms of degree $\le 2$ are:
> - degree $0$: $\mathbb 1$;
> - degree $1$: $sX + sY - sX - sY = 0$;
> - degree $2$ from one factor: $\frac{s^2}2(X^2 + Y^2 + X^2 + Y^2) = s^2(X^2 + Y^2)$;
> - degree $2$ from two factors (first-order term of an earlier factor times first-order term of a later one, six pairs in order): $s^2\bigl(XY - X^2 - XY - YX - Y^2 + XY\bigr) = s^2(XY - YX - X^2 - Y^2)$.
>
> Adding the two degree-2 lines, $X^2 + Y^2$ cancels and $e^{sX}e^{sY}e^{-sX}e^{-sY} = \mathbb 1 + s^2[X, Y] + O(s^3)$.
>
> **What the proof shows.**
> - ⚑ By-product: to first order in $s$ the group law is addition, $e^{sX}e^{sY} = e^{s(X + Y) + O(s^2)}$; the commutator is the first correction, at order $s^2$, and it is all that the group remembers of non-commutativity at that order → [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-1|§C3.2, Remark: Two boosts make a rotation]].
> - Part 1 builds $e^{X + Y}$ from products of exponentials of $X$ and $Y$ alone; this is why the Lie algebra of a closed group is closed under addition (Theorem §CB.1.12) and why the differential of a homomorphism is additive (Theorem §CB.2.3).
> - Part 3 is the bridge from groups to brackets used in Theorem §CB.1.16, 3.

^pf-cb-1-8

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-7|Theorem §CB.1.7]]

## One-parameter subgroups and the Lie algebra

> [!definition] Definition §CB.1.9: One-Parameter Subgroup
> A **one-parameter subgroup** of $GL(n, \mathbb C)$ is a continuous group homomorphism ([[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]) $\gamma : (\mathbb R, +) \to GL(n, \mathbb C)$: $\gamma(s + t) = \gamma(s)\gamma(t)$, $\gamma(0) = \mathbb 1$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §4, Def. 3.11 · Woit, Quantum Theory, Groups and Representations, Ch. 5*

^def-cb-1-9

> [!theorem] Theorem §CB.1.10: One-Parameter Subgroups Are Exponentials
> If $\gamma$ is a one-parameter subgroup of $GL(n, \mathbb C)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-9|Def. §CB.1.9]]), then $\gamma$ is differentiable and $\gamma(s) = e^{sX}$ for all $s$, with the unique matrix $X = \gamma'(0)$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §4, Def. 3.11, Thm. 3.12, with Prop. 3.8*

^thm-cb-1-10

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3, Thm. 3.12 and its proof (smoothing by a bump function), with Prop. 3.8 (https://arxiv.org/abs/math-ph/0005032).*
>
> **Step 1** (uniqueness). If $\gamma(s) = e^{sX}$ for all $s$, then $X = \gamma'(0)$ by [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], 5. So at most one $X$ works, and only existence remains.
>
> **Step 2** (smoothing). Choose a smooth function $f \ge 0$ on $\mathbb R$ with support in $[-\delta, \delta]$ and $\int f = 1$, where $\delta > 0$ is so small that $\|\gamma(s) - \mathbb 1\| < 1$ for $|s| \le \delta$ (possible since $\gamma$ is continuous and $\gamma(0) = \mathbb 1$). Define $F(t) = \int\gamma(t + s)f(s)\,ds$ (entrywise integrals of continuous functions over $[-\delta, \delta]$).
>
> **Step 3** ($F$ is smooth). Substitute $u = t + s$ (for fixed $t$; $du = ds$, the limits $\pm\delta$ become $t \pm \delta$): $F(t) = \int\gamma(u)f(u - t)\,du$. Now $t$ appears only in the smooth $f$, and on a bounded $t$-interval the integrand's $t$-derivatives $-\gamma(u)f'(u - t)$, $\gamma(u)f''(u - t)$, … are bounded by an integrable function of $u$ (continuous on a compact $u$-interval). Differentiation under the integral ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], 2), repeated, shows that $F$ is smooth.
>
> **Step 4** ($\gamma$ is smooth). By the homomorphism property, $\gamma(t + s) = \gamma(t)\gamma(s)$, so $F(t) = \gamma(t)M$ with the constant matrix $M = \int\gamma(s)f(s)\,ds$. Since $\int f = 1$, $M - \mathbb 1 = \int(\gamma(s) - \mathbb 1)f(s)\,ds$ has norm $\le \sup_{|s|\le\delta}\|\gamma(s) - \mathbb 1\| < 1$, so $M = e^{\log M}$ is invertible ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-7|Theorem §CB.1.7]]; Theorem §CB.1.5, 2). Hence $\gamma(t) = F(t)M^{-1}$ is smooth.
>
> **Step 5** (Taylor at 0). Put $X = \gamma'(0)$. Taylor's theorem with remainder ([[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]], applied to the real and imaginary parts of each entry on $[-1, 1]$) gives a constant $K$ with $\|\gamma(h) - \mathbb 1 - hX\| \le Kh^2$ for $|h| \le 1$.
>
> **Step 6** (the group law and the limit; Hall, Prop. 3.8). Fix $t$. For each integer $m \ge |t|$, $\gamma(t) = \gamma(t/m)^m$ (the homomorphism property applied $m - 1$ times), and by Step 5
>
> $$
> \gamma(t) = \Bigl(\mathbb 1 + \frac{tX}m + C_m\Bigr)^m, \qquad \|C_m\| \le \frac{Kt^2}{m^2} .
> $$
>
> This is the situation of Steps 3–4 of the proof of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], with $tX$ in place of $X + Y$ and $C_m$ again of order $1/m^2$: $B_m = tX/m + C_m$ has $\|B_m\| \le \frac12$ for large $m$, $\mathbb 1 + B_m = \exp(B_m + E_m)$ with $\|E_m\| \le \|B_m\|^2 = O(1/m^2)$, and $(\mathbb 1 + B_m)^m = \exp(tX + mC_m + mE_m) \to e^{tX}$. The left side is $\gamma(t)$ for every $m$, so $\gamma(t) = e^{tX}$.
>
> **What the proof shows.**
> - Continuity alone forces smoothness and the exponential form; nothing about the group beyond the homomorphism property is used.
> - ⚑ By-product: every continuous homomorphism $\mathbb R \to GL(n, \mathbb C)$ has a generator $X = \gamma'(0)$; for a representation this is the statement that represented one-parameter groups are $e^{s\,d(X)}$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], whose derivation assumed smoothness; this theorem removes the assumption).
> - Used next: the differential of a homomorphism (Theorem §CB.2.3).

^pf-cb-1-10

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-9|Def. §CB.1.9]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-7|Theorem §CB.1.7]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]] (Steps 3–4 of its proof), [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]]

The course defines the Lie algebra of a matrix Lie group through its one-parameter subgroups:

> [!definition] Definition §CB.1.11: Lie Algebra of a Matrix Lie Group
> The **Lie algebra** of a matrix Lie group $G$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-3|Def. §CB.1.3]]) is the real vector space
>
> $$
> \mathfrak g = \{X \in M_n(\mathbb C) : e^{sX} \in G \text{ for all } s \in \mathbb R\} = T_{\mathbb 1}G, \qquad [X, Y] = XY - YX \in \mathfrak g .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Definition "Group, algebra, representation") · Yu §3.2, eqs. (3.35)–(3.36) · PS §3.1, p. 38, eqs. (3.12)–(3.13) · Hall, Defs. 16.1, 16.10, 16.19, Prop. 16.20 · Georgi §§2.1–2.2, eqs. (2.4)–(2.5), (2.18)*

^def-cb-1-11

> [!theorem] Theorem §CB.1.12: The Lie Algebra Is a Real Lie Algebra
> Let $G$ be a matrix Lie group ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-3|Def. §CB.1.3]]) and $\mathfrak g$ its Lie algebra ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|Def. §CB.1.11]]). Then
> 1. $\mathfrak g$ is a **real** vector subspace of $M_n(\mathbb C)$: $X, Y \in \mathfrak g$ and $a, b \in \mathbb R$ give $aX + bY \in \mathfrak g$; in general $iX \notin \mathfrak g$;
> 2. $gXg^{-1} \in \mathfrak g$ for all $g \in G$, $X \in \mathfrak g$;
> 3. $[X, Y] = XY - YX \in \mathfrak g$ for $X, Y \in \mathfrak g$, so $(\mathfrak g, [\cdot,\cdot])$ is a real Lie algebra ([[§49 Lie Bracket and Lie Algebra#^def-49-2|591 Def. §49.2]], [[§49 Lie Bracket and Lie Algebra#^prop-49-3|591 Prop. §49.3]]).
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §6, Props. 3.14, 3.15, Thm. 3.16, Prop. 3.30 · Woit, §5.5 (the Lie algebra is a real vector space)*

^thm-cb-1-12

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §6, Prop. 3.15, Thm. 3.16 and Prop. 3.30 with proofs (https://arxiv.org/abs/math-ph/0005032); the example in Step 3 is P. Woit's, Quantum Theory, Groups and Representations, §5.5 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf).*
>
> **Step 1** (real multiples). If $X \in \mathfrak g$ and $a \in \mathbb R$, then $e^{s(aX)} = e^{(sa)X} \in G$ for every real $s$, because $sa$ is again real. So $aX \in \mathfrak g$.
>
> **Step 2** (sums, by the Lie product formula). Let $X, Y \in \mathfrak g$ and $s \in \mathbb R$. By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], 1, applied to $sX$, $sY$,
>
> $$
> e^{s(X + Y)} = \lim_{m\to\infty}\bigl(e^{sX/m}e^{sY/m}\bigr)^m .
> $$
>
> Each $e^{sX/m}$, $e^{sY/m}$ lies in $G$ (Step 1 and the definition of $\mathfrak g$), so each product on the right lies in $G$ ($G$ is a group). The limit $e^{s(X + Y)}$ is invertible ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], 2), and $G$ is closed in $GL(n, \mathbb C)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-3|Def. §CB.1.3]]), so $e^{s(X + Y)} \in G$. Hence $X + Y \in \mathfrak g$; with Step 1, $aX + bY \in \mathfrak g$ for real $a$, $b$. ⚑ By-product: this is the one place in the proof where closedness of $G$ enters (a limit of elements of $G$ must stay in $G$); it enters again, more strongly, in the closed-subgroup theorem → [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]].
>
> **Step 3** (in general $iX \notin \mathfrak g$). $X = -\frac i2\sigma^3 \in \mathfrak{su}(2)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-18|Theorem §CB.1.18]]), but $iX = \frac12\sigma^3$ is Hermitian and nonzero, so $(iX)^\dagger \ne -iX$, and $e^{s\sigma^3/2} = \operatorname{diag}(e^{s/2}, e^{-s/2})$ is not unitary for $s \ne 0$: $iX \notin \mathfrak{su}(2)$. So $\mathfrak g$ is a real, not a complex, subspace of $M_n(\mathbb C)$.
>
> **Step 4** (part 2). For $g \in G$, $X \in \mathfrak g$ and real $s$, Theorem §CB.1.5, 4 gives $e^{s\,gXg^{-1}} = g\,e^{sX}g^{-1}$, a product of three elements of $G$. So $gXg^{-1} \in \mathfrak g$.
>
> **Step 5** (part 3). Fix $X, Y \in \mathfrak g$. By Step 4 with $g = e^{sX}$, the curve $c(s) = e^{sX}Ye^{-sX}$ lies in $\mathfrak g$ for all $s$. By the product rule and Theorem §CB.1.5, 5,
>
> $$
> c'(0) = \Bigl(Xe^{sX}Ye^{-sX} + e^{sX}Y(-X)e^{-sX}\Bigr)\Big|_{s=0} = XY - YX .
> $$
>
> $c'(0) = \lim_{s\to0}(c(s) - c(0))/s$ is a limit of elements of $\mathfrak g$ (Steps 1–2: $\mathfrak g$ is a real subspace), and a linear subspace of the finite-dimensional space $M_n(\mathbb C)$ is closed. So $[X, Y] \in \mathfrak g$.
>
> **Step 6** (real Lie algebra). The commutator is bilinear, antisymmetric and satisfies the Jacobi identity on all of $M_n(\mathbb C)$ ([[§49 Lie Bracket and Lie Algebra#^prop-49-3|591 Prop. §49.3]]), so its restriction to the real subspace $\mathfrak g$, which it maps into $\mathfrak g$ by Step 5, makes $\mathfrak g$ a real Lie algebra ([[§49 Lie Bracket and Lie Algebra#^def-49-2|591 Def. §49.2]]).
>
> **What the proof shows.**
> - The definition through one-parameter subgroups with *real* parameter is what makes $\mathfrak g$ real; the physicists' Hermitian generators $T_a = iX_a$ lie outside $\mathfrak g$ → [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-6|Theorem §CB.3.6]].
> - The bracket comes from conjugation (Step 5): it is the derivative of the adjoint action, made precise in Theorem §CB.2.17.

^pf-cb-1-12

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-3|Def. §CB.1.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|Def. §CB.1.11]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-18|Theorem §CB.1.18]], [[§49 Lie Bracket and Lie Algebra#^prop-49-3|591 Prop. §49.3]], [[§49 Lie Bracket and Lie Algebra#^def-49-2|591 Def. §49.2]]

A basis of the Lie algebra, its structure constants, and the physicists' Hermitian generators, used from here on (the factor $i$ is analysed in [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification|§CB.3]]):

> [!definition] Definition §CB.1.13: Generators of a Lie Algebra
> A basis $\{X_a\}$ of a Lie algebra $\mathfrak g$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|Def. §CB.1.11]]) is a set of **generators**; $[X_a, X_b] = f_{ab}{}^cX_c$ defines the real **structure constants**. Physicists use $T_a = iX_a$: then $[T_a, T_b] = if_{ab}{}^cT_c$ and group elements near $\mathbb 1$ are $e^{-i\theta^aT_a}$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Definition "Group, algebra, representation") · Yu §3.2, eqs. (3.35)–(3.36) · PS §3.1, p. 38, eqs. (3.12)–(3.13) · Hall, Defs. 16.1, 16.10, 16.19, Prop. 16.20 · Georgi §§2.1–2.2, eqs. (2.4)–(2.5), (2.18)*

^def-cb-1-13

The closed-subgroup theorem and the tangent-space theorem both rest on one limit argument:

> [!theorem] Lemma §CB.1.14: The Limit Lemma
> Let $G$ be a matrix Lie group with Lie algebra $\mathfrak g$. Let $g_k \in G$, $g_k \to \mathbb 1$, $g_k \ne \mathbb 1$, let $Y_k = \log g_k$ (defined for large $k$, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-7|Theorem §CB.1.7]]), and let $|\cdot|$ be any norm on $M_n(\mathbb C)$. If $Y_k/|Y_k| \to Y$, then $Y \in \mathfrak g$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §7, Lemma 3.24*

^lem-cb-1-14

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §7, Lemma 3.24 and its proof (https://arxiv.org/abs/math-ph/0005032); formerly Step 1 of the proof of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]].*
>
> $Y_k \ne 0$ (else $g_k = e^0 = \mathbb 1$), and $Y_k \to \log\mathbb 1 = 0$ by continuity of $\log$. Fix $t \in \mathbb R$ and put $m_k = \lfloor t/|Y_k|\rfloor \in \mathbb Z$; then $|m_k|Y_k| - t| \le |Y_k| \to 0$. Since $e^{Y_k} = g_k$, Theorem §CB.1.5, 3 (for negative $m_k$ with Theorem §CB.1.5, 2) gives $e^{m_kY_k} = g_k^{m_k} \in G$. And $m_kY_k = (m_k|Y_k|)\,(Y_k/|Y_k|) \to tY$, so by continuity of $\exp$, $g_k^{m_k} \to e^{tY}$, which is invertible; $G$ is closed in $GL(n, \mathbb C)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-3|Def. §CB.1.3]]), so $e^{tY} \in G$. As $t$ was arbitrary, $Y \in \mathfrak g$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|Def. §CB.1.11]]).

^pf-cb-1-14

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-7|Theorem §CB.1.7]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-3|Def. §CB.1.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|Def. §CB.1.11]]

> [!theorem] Theorem §CB.1.15: Closed-Subgroup Theorem
> Every closed subgroup $G$ of $GL(n, \mathbb C)$ is an embedded submanifold of $GL(n, \mathbb C)$ of real dimension $\dim_{\mathbb R}\mathfrak g$, and with this structure a Lie group ([[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-1|591 Def. §50.1]]). There is a neighbourhood $U$ of $0$ in $M_n(\mathbb C)$ such that $\exp$ maps $U \cap \mathfrak g$ homeomorphically onto a neighbourhood of $\mathbb 1$ in $G$.
>
> *Source: Meinrenken, Lie Groups and Lie Algebras, §2.6, Thm. 2.16 (von Neumann's proof) · Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §7, Thm. 3.23 · Lee, Introduction to Smooth Manifolds, Prop. 7.11 · cited in [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-3|Def. §CB.1.3]] · 591 when the course reaches it*

^thm-cb-1-15

> [!proof]- Proof
> *Source: E. Meinrenken, Lie Groups and Lie Algebras, lecture notes (Toronto, Winter 2026), §2.6, Thm. 2.16 and its proof (https://www.math.toronto.edu/mein/teaching/LectureNotes/lie.pdf), written there for $GL(n, \mathbb R)$ and carried over verbatim to $GL(n, \mathbb C)$ regarded as an open subset of $M_n(\mathbb C) \cong \mathbb R^{2n^2}$; the same argument is B. C. Hall, An Elementary Introduction to Groups and Representations, Thm. 3.23 (https://arxiv.org/abs/math-ph/0005032). Decision SPEC-CB 7 allowed a clean source proof here; this is it. The Lie group structure (Step 5) is J. M. Lee, Introduction to Smooth Manifolds, 2nd ed., Prop. 7.11.*
>
> **Step 1** (a complement and a map). $\mathfrak g$ is a real subspace of $M_n(\mathbb C)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-12|Theorem §CB.1.12]]). Regard $M_n(\mathbb C)$ as the real Euclidean space $\mathbb R^{2n^2}$ (real and imaginary parts of the entries), with norm $|\cdot|$, and let $\mathfrak d = \mathfrak g^\perp$ be the orthogonal complement, so $M_n(\mathbb C) = \mathfrak g \oplus \mathfrak d$. Define
>
> $$
> \Phi : M_n(\mathbb C) \to GL(n, \mathbb C), \qquad \Phi(X + Y) = e^Xe^Y \qquad (X \in \mathfrak g,\ Y \in \mathfrak d).
> $$
>
> $\Phi$ is smooth ($\exp$ is smooth, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], 1, and the product is polynomial).
>
> **Step 2** (the derivative at 0 is the identity). For $X \in \mathfrak g$, $\frac{d}{dt}\Phi(tX)|_0 = \frac{d}{dt}e^{tX}|_0 = X$; for $Y \in \mathfrak d$, $\frac{d}{dt}\Phi(tY)|_0 = Y$ (Theorem §CB.1.5, 5). By linearity of the derivative, $D\Phi_0 = \mathrm{id}$ on $\mathfrak g \oplus \mathfrak d$. By the inverse function theorem ([[§33 Local Diffeomorphisms#^thm-33-1|591 Thm. §33.1]]) there is $\varepsilon > 0$ such that $\Phi$ maps the open ball $B_\varepsilon = \{|Z| < \varepsilon\}$ diffeomorphically onto an open neighbourhood of $\mathbb 1$.
>
> **Step 3** (the slice at the identity; Meinrenken's Claim). *There is $r \in (0, \varepsilon]$ with $\Phi(B_r \cap \mathfrak g) = \Phi(B_r) \cap G$.* The inclusion $\subset$ holds for every $r$: for $X \in \mathfrak g$, $\Phi(X) = e^X \in G$. Suppose $\supset$ fails for every $r = \varepsilon/k$, $k = 1, 2, \dots$. Then there are $Z_k \in B_{\varepsilon/k}$ with $\Phi(Z_k) \in G$ but $\Phi(Z_k) \notin \Phi(B_{\varepsilon/k}\cap\mathfrak g)$; as $\Phi$ is injective on $B_\varepsilon$, $Z_k \notin \mathfrak g$. Write $Z_k = X_k + Y_k$ ($X_k \in \mathfrak g$, $Y_k \in \mathfrak d$); then $Y_k \ne 0$, $|Y_k| \le |Z_k| < \varepsilon/k$ (orthogonal decomposition), and $e^{Y_k} = e^{-X_k}\Phi(Z_k) \in G$ (both factors in $G$). The unit vectors $Y_k/|Y_k|$ lie in the unit sphere of $\mathfrak d$, which is compact, so a subsequence converges to some $Y \in \mathfrak d$ with $|Y| = 1$. Along it, $g_k = e^{Y_k} \to \mathbb 1$, and for large $k$, $\log g_k = Y_k$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-7|Theorem §CB.1.7]], since $Y_k \to 0$). The limit lemma ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^lem-cb-1-14|Lemma §CB.1.14]], which uses that $G$ is closed) gives $Y \in \mathfrak g$. So $Y \in \mathfrak g \cap \mathfrak d = \{0\}$, contradicting $|Y| = 1$.
>
> **Step 4** (charts; the embedded submanifold). Let $U_{\mathbb 1} = \Phi(B_r)$ and $\psi = (\Phi|_{B_r})^{-1} : U_{\mathbb 1} \to B_r$, a chart of the open set $GL(n, \mathbb C) \subset M_n(\mathbb C)$. By Step 3, $\psi(U_{\mathbb 1} \cap G) = B_r \cap \mathfrak g$: in linear coordinates adapted to $\mathfrak g \oplus \mathfrak d$, $U_{\mathbb 1} \cap G$ is the set where the $\mathfrak d$-coordinates vanish. For $g \in G$, left multiplication $L_g(A) = gA$ is a linear isomorphism of $M_n(\mathbb C)$ mapping $GL(n, \mathbb C)$ onto itself and $G$ onto itself ($G$ is a group). So $U_g = gU_{\mathbb 1}$ with the chart $\psi\circ L_{g^{-1}}$ satisfies $\psi\circ L_{g^{-1}}(U_g \cap G) = B_r \cap \mathfrak g$. These are adapted charts around every point of $G$: $G$ is a submanifold of $GL(n, \mathbb C)$ ([[§35 Regular Submanifolds#^def-35-1|591 Def. §35.1]]) of dimension $\dim_{\mathbb R}\mathfrak g$.
>
> **Step 5** (a Lie group). Multiplication $GL\times GL \to GL$ and inversion (Cramer's rule) are smooth; their restrictions to $G\times G$ and $G$ are smooth maps into $GL(n, \mathbb C)$ with values in $G$, hence smooth into $G$ ([[§35 Regular Submanifolds#^lem-35-3|591 Lemma §35.3]], 2; Lee, Prop. 7.11). With its subspace topology $G$ is a topological group, so $G$ is a Lie group ([[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-1|591 Def. §50.1]]).
>
> **Step 6** (the exponential chart). On $B_r \cap \mathfrak g$, $\Phi = \exp$. By Steps 2–3, $\exp$ maps $B_r \cap \mathfrak g$ bijectively onto $\Phi(B_r) \cap G$, which is open in $G$ and contains $\mathbb 1$; it is continuous with continuous inverse $\psi|_{\Phi(B_r)\cap G}$. This is the last assertion, with $U = B_r$.
>
> **What the proof shows.**
> - Closedness enters only through the limit lemma (Step 3); for a non-closed subgroup, such as a line of irrational slope on a torus, it fails and the subgroup is not embedded.
> - ⚑ By-product: near $\mathbb 1$, $G$ is exactly $\exp$ of a neighbourhood of $0$ in $\mathfrak g$; every statement "check it on generators" rests on this → Theorems §CB.2.10, §CB.2.14, §CB.2.20.
> - Every matrix Lie group of the course ($SO(3)$, $SU(2)$, $SO^+(1,3)$, $SL(2, \mathbb C)$, $SU(2)\times SU(2)$) is therefore a Lie group in the sense of 591, with no separate regular-value computation needed.

^pf-cb-1-15

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-7|Theorem §CB.1.7]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-12|Theorem §CB.1.12]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^lem-cb-1-14|Lemma §CB.1.14]], [[§33 Local Diffeomorphisms#^thm-33-1|591 Thm. §33.1]], [[§35 Regular Submanifolds#^def-35-1|591 Def. §35.1]], [[§35 Regular Submanifolds#^lem-35-3|591 Lemma §35.3]], [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-1|591 Def. §50.1]]

> [!theorem] Theorem §CB.1.16: The Lie Algebra Is the Tangent Space at the Identity
> Let $G$ be a matrix Lie group with Lie algebra $\mathfrak g$.
> 1. $\mathfrak g$ is the set of velocities $\gamma'(0)$ of the differentiable curves $\gamma$ in $M_n(\mathbb C)$ that lie in $G$ and have $\gamma(0) = \mathbb 1$.
> 2. For the classical groups of [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]], $\mathfrak g$ equals 591's geometric tangent space $T^{\mathrm{geo}}_IG$.
> 3. Under the identification of a left-invariant vector field with its value at $\mathbb 1$, the Lie algebra of left-invariant vector fields of [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-4|591 Def. §50.4]] is $\mathfrak g$, and the bracket of vector fields becomes the commutator $XY - YX$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §7, Lemma 3.24 (parts 1–2) · Lee, Introduction to Smooth Manifolds, Props. 8.41, 8.48, Thm. 8.46 (part 3) · 591 §25, §49*

^thm-cb-1-16

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §7, Lemma 3.24 and its proof (https://arxiv.org/abs/math-ph/0005032), for Steps 1–3 · J. M. Lee, Introduction to Smooth Manifolds, 2nd ed., Prop. 8.41 (the bracket of left-invariant fields on GL(n,ℝ)), Prop. 8.48 (GL(n,ℂ)) and Thm. 8.46 (Lie subgroups), for Steps 5–6. Part 3 uses Theorem §CB.1.15, proved just above; that proof uses only the limit lemma, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^lem-cb-1-14|Lemma §CB.1.14]], so there is no circularity.*
>
> **Step 1** (the limit lemma). This is [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^lem-cb-1-14|Lemma §CB.1.14]].
>
> **Step 2** (part 1, $\mathfrak g \subset$ velocities). For $X \in \mathfrak g$, $\gamma(s) = e^{sX}$ is differentiable, lies in $G$, has $\gamma(0) = \mathbb 1$ and $\gamma'(0) = X$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], 5).
>
> **Step 3** (part 1, velocities $\subset \mathfrak g$). Let $\gamma$ be differentiable with values in $G$, $\gamma(0) = \mathbb 1$, $V = \gamma'(0)$. If $V = 0$, $V \in \mathfrak g$. Otherwise, for small $|s|$, $\|\gamma(s) - \mathbb 1\| \le \frac12$ and $Y(s) = \log\gamma(s)$ is defined; by Step 1 of the proof of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], $Y(s) = (\gamma(s) - \mathbb 1) + E(s)$ with $\|E(s)\| \le \|\gamma(s) - \mathbb 1\|^2$. Divide by $s$: $(\gamma(s) - \mathbb 1)/s \to V$, and $\|E(s)\|/|s| \le \|\gamma(s) - \mathbb 1\|\cdot\|\gamma(s) - \mathbb 1\|/|s| \to 0\cdot\|V\| = 0$. So $Y(s)/s \to V$. Put $s_k = 1/k$, $g_k = \gamma(s_k) \to \mathbb 1$, $Y_k = Y(s_k)$; for large $k$, $Y_k/s_k$ is close to $V \ne 0$, so $Y_k \ne 0$ and $Y_k/\|Y_k\| = (Y_k/s_k)/\|Y_k/s_k\| \to V/\|V\|$. Step 1 (Lemma §CB.1.14) gives $V/\|V\| \in \mathfrak g$, and $V = \|V\|\cdot V/\|V\| \in \mathfrak g$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-12|Theorem §CB.1.12]], 1).
>
> **Step 4** (part 2). The groups of [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]] are closed subgroups of $GL(n, \mathbb C)$, so the above applies. $T^{\mathrm{geo}}_IG$ is the set of velocities of *smooth* curves in $G$ through $\mathbb 1$ ([[§25 The Geometric Tangent Space#^def-25-1|591 Def. §25.1]]). Smooth curves are differentiable, so $T^{\mathrm{geo}}_IG \subset \mathfrak g$ by Step 3; and each $X \in \mathfrak g$ is the velocity of $e^{sX}$, which is smooth (Theorem §CB.1.5, 5, applied repeatedly: $\frac{d^k}{ds^k}e^{sX} = X^ke^{sX}$). So $T^{\mathrm{geo}}_IG = \mathfrak g$.
>
> **Step 5** (part 3 for $GL(n, \mathbb C)$; Lee, Props. 8.41, 8.48). $GL(n, \mathbb C)$ is open in $M_n(\mathbb C) \cong \mathbb R^{2n^2}$, so its tangent space at every point is $M_n(\mathbb C)$. Left translation $L_g$ is the restriction of the linear map $A \mapsto gA$, so its differential is that same map, and a left-invariant field with value $A$ at $\mathbb 1$ is $\mathbf X^A_g = gA$ (the proof of [[§50 Lie Groups and Left-Invariant Vector Fields#^ex-50-1|591 Ex. §50.1]], verbatim over $\mathbb C$). In the global linear coordinates the bracket of vector fields is $[\mathbf X, \mathbf Y]_g = D\mathbf Y_g(\mathbf X_g) - D\mathbf X_g(\mathbf Y_g)$ ([[§49 Lie Bracket and Lie Algebra#^prop-49-2|591 Prop. §49.2]], written with the derivative $D$ of the component functions). For $\mathbf Y = \mathbf X^B$, $g \mapsto gB$ is linear, so $D\mathbf X^B_g(V) = VB$. Hence
>
> $$
> [\mathbf X^A, \mathbf X^B]_g = (gA)B - (gB)A = g(AB - BA) = \mathbf X^{[A, B]}_g ,
> $$
>
> and at $g = \mathbb 1$ the bracket of the fields is the commutator of their values.
>
> **Step 6** (part 3 for $G$; Lee, Thm. 8.46). By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]], $G$ is an embedded submanifold and a Lie group, and its tangent space at $\mathbb 1$ is $\mathfrak g$ (Step 3 of that proof: near $\mathbb 1$, $G$ is the image of $\mathfrak g$ under a diffeomorphism with derivative the identity at $0$). The inclusion $G \to GL(n, \mathbb C)$ is a Lie group homomorphism, and Lee's Thm. 8.46 identifies the left-invariant fields of $G$ with those left-invariant fields of $GL(n, \mathbb C)$ whose value at $\mathbb 1$ lies in $T_{\mathbb 1}G = \mathfrak g$, preserving brackets. With Step 5, identifying a left-invariant field on $G$ with its value at $\mathbb 1$ turns the bracket of vector fields into $XY - YX$.
>
> **What the proof shows.**
> - Three definitions agree: one-parameter subgroups (the course's), velocities of curves (591 §25), left-invariant vector fields (591 §50). The physics chapters may use whichever is convenient.
> - The sign: left-invariant fields give $+[A, B]$; right-invariant fields would give $-[A, B]$ (Meinrenken, Remark 4.9), one more place where a sign convention hides.

^pf-cb-1-16

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^lem-cb-1-14|Lemma §CB.1.14]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-3|Def. §CB.1.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|Def. §CB.1.11]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-7|Theorem §CB.1.7]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-12|Theorem §CB.1.12]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]], [[§25 The Geometric Tangent Space#^def-25-1|591 Def. §25.1]], [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]], [[§50 Lie Groups and Left-Invariant Vector Fields#^ex-50-1|591 Ex. §50.1]], [[§49 Lie Bracket and Lie Algebra#^prop-49-2|591 Prop. §49.2]]

> [!theorem] Theorem §CB.1.17: The Lie Algebras of the Classical Groups
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
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §§5.2–5.6 · 591 Thm. §25.5 (the real groups) · the user's PHY 513 notes, Ch. 7 §7.2 · [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]] (the Lorentz case)*

^thm-cb-1-17

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3, §§5.2 (GL), 5.3 (SL), 5.4 (U, SU), 5.5 (O, SO), 5.6 (the generalized orthogonal groups O(n;k), here with $\eta$) (https://arxiv.org/abs/math-ph/0005032). Hall's route for each group: write the defining condition for $e^{sX}$; a condition on $X$ that makes it hold for all $s$ is sufficient; differentiating at $s = 0$ shows it is necessary. Hall settles the trace condition with "$s\operatorname{tr}X \in 2\pi i\mathbb Z$ for all $s$"; Step 2 differentiates instead.*
>
> **Step 1** ($GL(n, \mathbb C)$). Every $e^{sX}$ is invertible ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], 2), so $\mathfrak{gl}(n, \mathbb C) = M_n(\mathbb C)$, of real dimension $2n^2$.
>
> **Step 2** ($SL(n, \mathbb C)$). By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-6|Theorem §CB.1.6]], $\det e^{sX} = e^{s\operatorname{tr}X}$. If $\operatorname{tr}X = 0$ this is $1$ for all $s$. Conversely, if $e^{s\operatorname{tr}X} = 1$ for all $s$, differentiating at $s = 0$ gives $\operatorname{tr}X = 0$. One complex linear condition removes two real dimensions: $2n^2 - 2$.
>
> **Step 3** ($U(n)$). By Theorem §CB.1.5, 4, $(e^{sX})^\dagger = e^{sX^\dagger}$, so $e^{sX}$ is unitary iff $e^{sX^\dagger} = (e^{sX})^{-1} = e^{-sX}$. If $X^\dagger = -X$ this holds for all $s$. Conversely, if it holds for all $s$, differentiate at $s = 0$ (Theorem §CB.1.5, 5): $X^\dagger = -X$. Dimension: an anti-Hermitian matrix has imaginary diagonal ($n$ real parameters) and its strictly upper part ($n(n-1)/2$ complex entries) determines the lower part, $n + n(n - 1) = n^2$.
>
> **Step 4** ($SU(n)$). Steps 2 and 3 together. The trace of an anti-Hermitian matrix is imaginary, so $\operatorname{tr}X = 0$ is one real condition: $n^2 - 1$.
>
> **Step 5** ($O(n)$, $SO(n)$). If $e^{sX}$ is real for all $s$, then $X = \frac{d}{ds}e^{sX}|_0$ is real. For real $X$, $e^{sX}$ is orthogonal iff $e^{sX^{\mathsf T}} = e^{-sX}$; as in Step 3 this holds for all $s$ iff $X^{\mathsf T} = -X$. Such $X$ has zero diagonal, so $\operatorname{tr}X = 0$ and $\det e^{sX} = 1$: the same $X$ work for $SO(n)$. Dimension: the strictly upper entries, $n(n-1)/2$.
>
> **Step 6** ($O(1,3)$, $SO^+(1,3)$). $\Lambda \in O(1,3)$ iff $\Lambda^{\mathsf T}\eta\Lambda = \eta$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]). As in Step 5, $X$ is real. If $X^{\mathsf T}\eta + \eta X = 0$, then $X^{\mathsf T} = -\eta X\eta^{-1}$ ($\eta^2 = \mathbb 1$), so $(e^{sX})^{\mathsf T} = e^{sX^{\mathsf T}} = \eta e^{-sX}\eta^{-1}$ (Theorem §CB.1.5, 4), and $(e^{sX})^{\mathsf T}\eta e^{sX} = \eta e^{-sX}\eta^{-1}\eta e^{sX} = \eta$. Conversely, differentiating $(e^{sX})^{\mathsf T}\eta e^{sX} = \eta$ at $s = 0$ (product rule) gives $X^{\mathsf T}\eta + \eta X = 0$. For $SO^+(1,3)$: the condition says $\eta X$ is antisymmetric, so $(\eta X)_{\mu\mu} = \eta_{\mu\mu}X_{\mu\mu} = 0$, $\operatorname{tr}X = 0$ and $\det e^{sX} = 1$; and $s \mapsto (e^{sX})^0{}_0$ is continuous, equals $1$ at $s = 0$, and never lies in $(-1, 1)$ (every Lorentz matrix has $|\Lambda^0{}_0| \ge 1$, [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-4|REL Theorem §B1.2.4]]), so by the intermediate value theorem it stays $\ge 1$: $e^{sX}$ is orthochronous. So $O(1,3)$ and $SO^+(1,3)$ have the same algebra. Dimension: $X \mapsto \eta X$ is a bijection onto the real antisymmetric $4\times4$ matrices, $6$ parameters.
>
> **Step 7** ($SL(2, \mathbb C)$ as a real algebra). By Step 2, $\mathfrak{sl}(2, \mathbb C)$ is the traceless complex $2\times2$ matrices, real dimension $2\cdot4 - 2 = 6$, and $iX$ is traceless whenever $X$ is: closed under $i$, unlike $\mathfrak{su}(2)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-12|Theorem §CB.1.12]], Step 3 of the proof).
>
> **What the proof shows.**
> - Each Lie algebra is the linearization of its group's defining equation at $\mathbb 1$; the dimensions match the manifold dimensions of [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]] (Theorem §CB.1.16, 2).
> - Discrete conditions (the sign of $\det$, orthochronicity) are invisible to the algebra: $O(n)$ and $SO(n)$, $O(1,3)$ and $SO^+(1,3)$ share their algebras → Theorem §CB.2.10.
> - Whether the algebra is closed under $i$ depends on the group, not on whether its matrices are complex: $\mathfrak{su}(2)$ is not, $\mathfrak{sl}(2, \mathbb C)$ is → [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^def-cb-5-7|Def. §CB.5.7]].

^pf-cb-1-17

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-6|Theorem §CB.1.6]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-12|Theorem §CB.1.12]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-4|REL Theorem §B1.2.4]]

The rotation case, the course's example (PHY 513 Lecture 7, Part A; the user's PHY 513 notes, Ch. 7 §7.2):

> [!theorem] Theorem §CB.1.18: SO(3) and SU(2) Have the Same Lie Algebra
> $\mathfrak{so}(3)$ is the space of real antisymmetric $3\times3$ matrices and $\mathfrak{su}(2)$ that of traceless anti-Hermitian $2\times2$ matrices; both are three-dimensional, with physicist's bases
>
> $$
> (J^k)_{lm} = -i\varepsilon^{klm}\ \ \text{on } \mathbb C^3, \qquad \tau^k = \tfrac12\sigma^k\ \ \text{on } \mathbb C^2, \qquad [J^i, J^j] = i\varepsilon^{ijk}J^k, \qquad [\tau^i, \tau^j] = i\varepsilon^{ijk}\tau^k .
> $$
>
> The map $-i\tau^k \mapsto -iJ^k$ is an isomorphism of Lie algebras, $\mathfrak{su}(2) \cong \mathfrak{so}(3)$: it is the differential at $\mathbb 1$ of the covering map $SU(2) \to SO(3)$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Definition "Group, algebra, representation"; Derivation "The representations of the rotation algebra", Examples) · Yu §3.2, eqs. (3.53)–(3.60) · PS §3.1, eqs. (3.11)–(3.14) · Hall, Prop. 16.22, Ex. 16.34*

^thm-cb-1-18

> [!derivation]- Derivation
> **1. The algebra of $SO(3)$.** If $e^{sX} \in SO(3)$ for all $s$, differentiate $(e^{sX})^{\mathsf T}e^{sX} = \mathbb 1$ at $s = 0$ (product rule, $(e^{sX})^{\mathsf T} = e^{sX^{\mathsf T}}$): $X^{\mathsf T} + X = 0$. Conversely, if $X^{\mathsf T} = -X$, then $(e^{sX})^{\mathsf T} = e^{-sX} = (e^{sX})^{-1}$, and $\det e^{sX} = e^{s\operatorname{tr}X} = 1$ because an antisymmetric matrix has zero diagonal. So $\mathfrak{so}(3)$ is the antisymmetric matrices, the tangent space of [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]]; a real antisymmetric $3\times3$ matrix has three free entries.
>
> **2. The algebra of $SU(2)$.** If $e^{sX} \in SU(2)$ for all $s$, differentiating $(e^{sX})^\dagger e^{sX} = \mathbb 1$ gives $X^\dagger = -X$, and $\det e^{sX} = e^{s\operatorname{tr}X} = 1$ for all $s$ forces $\operatorname{tr}X = 0$; the converse is as in step 1. An anti-Hermitian $2\times2$ matrix has four real parameters (two imaginary diagonal entries, one complex off-diagonal entry); zero trace removes one, leaving three. Since $\sigma^1, \sigma^2, \sigma^3$ are Hermitian, traceless and independent ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]), $\{-i\sigma^k/2\}$ is a basis.
>
> **3. Physicist's bases and brackets.** $(J^k)_{lm} = -i\varepsilon^{klm}$ is $i$ times the real antisymmetric matrix $(A_k)_{lm} = -\varepsilon^{klm}$ of [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-1|QM Theorem §C5.1.1]], whose bracket $[A_i, A_j] = \varepsilon^{ijk}A_k$ gives $[J^i, J^j] = i^2\varepsilon^{ijk}A_k = i\varepsilon^{ijk}J^k$ (worked with $\hbar$ in [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^ex-c5-1-2|QM Example §C5.1.2]]). For $\tau^k$: $\sigma^i\sigma^j = \delta^{ij}\mathbb 1 + i\varepsilon^{ijk}\sigma^k$ (QM Theorem §B6.1.4) gives $[\sigma^i, \sigma^j] = i\varepsilon^{ijk}\sigma^k - i\varepsilon^{jik}\sigma^k = 2i\varepsilon^{ijk}\sigma^k$, and dividing by $4$, $[\tau^i, \tau^j] = i\varepsilon^{ijk}\tau^k$. (The Lecture 7 slide "Representations of angular momentum: examples" prints $\sigma^3$ as the identity matrix; $\sigma^3 = \operatorname{diag}(1, -1)$.)
>
> **4. The isomorphism.** The structure constants agree, so the linear bijection $-i\tau^k \mapsto -iJ^k$ preserves brackets. It is the differential of the covering homomorphism $R : SU(2) \to SO(3)$ of QM Theorem §C5.2.6: by part 2 there, $R(e^{-i\theta\hat n\cdot\boldsymbol\sigma/2}) = R(\hat n, \theta) = e^{-i\theta\hat n\cdot\mathbf J}$, and differentiating at $\theta = 0$ sends $-i\hat n\cdot\boldsymbol\tau$ to $-i\hat n\cdot\mathbf J$. ⚑ By-product: the algebra, which sees only a neighbourhood of $\mathbb 1$, cannot tell the two groups apart; whether a representation of it belongs to $SO(3)$ or only to $SU(2)$ is a global question → [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-7|Theorem §CB.9.7]].
>
> **What the derivation shows**
> - Antisymmetry ($SO$) and anti-Hermiticity with zero trace ($SU$) are the linearized defining conditions; the dimension count $3 = 3$ is why the algebras can coincide.
> - The factor $i$ turns real antisymmetric and anti-Hermitian generators into Hermitian ones; it changes no structure constant → [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^rem-cb-3-1|Remark: The physicist's i]].
> - Used next: every representation of either group is a representation of this one algebra ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]]).

^der-cb-1-18

*Uses:* [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-1|QM Theorem §C5.1.1]], [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^ex-c5-1-2|QM Example §C5.1.2]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]

> [!remark]- Connections
> - The real Lie algebra of Theorem §CB.1.12 is the reason for [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification|§CB.3]]: the physicists' Hermitian generators and the ladder combinations $J^\pm$, $\mathbf J_\pm$ live outside $\mathfrak g$, in $i\mathfrak g$ and in the complexification.
> - **Used in**: Definition §CB.1.1 — [[§C1a.4 The Lorentz Group|§C1a.4]] (embedded), [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (cited in the text), [[§C9.1 Discrete Lorentz Transformations|§C9.1]] (embedded; cited in [[§C9.1 Discrete Lorentz Transformations#^def-c9-1-1|Def. §C9.1.1]]); Definition §CB.1.2 — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]] (cited in [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]]), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]]); Definition §CB.1.4–Theorem §CB.1.6 — the exponentials of rotations and boosts and their determinants ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-18|Theorem §CB.1.18]]), the finite quantum Poincaré transformations ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-3|Theorem §C3.4.3]]); Theorem §CB.1.8 — two boosts make a rotation ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-1|§C3.2, Remark: Two boosts make a rotation]]); Theorems §CB.1.12–§CB.1.17 — the course's Lie algebras ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|Def. §CB.1.11]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]); Definition §CB.1.3 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded); Definition §CB.1.11 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded), [[§C1a.6 Infinitesimal Lorentz Transformations and Generators|§C1a.6]] (embedded); Definition §CB.1.13 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded); Theorem §CB.1.18 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded); Theorem §CB.1.10 — [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra|§C3.4]] (embedded).
