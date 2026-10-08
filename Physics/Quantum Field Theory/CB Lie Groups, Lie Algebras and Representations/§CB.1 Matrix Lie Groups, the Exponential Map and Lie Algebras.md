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

*Sources (proofs written from these, each checked against the text): B. C. Hall, An Elementary Introduction to Groups and Representations, Chs. 2–5 (https://arxiv.org/abs/math-ph/0005032) · E. Meinrenken, Lie Groups and Lie Algebras, lecture notes, Toronto, Winter 2026, §§2.2, 2.5–2.6, 4 (https://www.math.toronto.edu/mein/teaching/LectureNotes/lie.pdf) · J. M. Lee, Introduction to Smooth Manifolds, 2nd ed., Props. 7.11, 8.41, 8.48, Thms. 8.46, 21.31 · Zuoqin Wang, Lie Groups (USTC), Lecture 12 · P. Etingof, Lie Groups and Lie Algebras (MIT 18.755), Prop. 3.15 · Differentiable Manifolds (591) §§11, 16, 25, 33, 35, 49–50 · the user's PHY 513 notes, Ch. 7 §7.2 · Yu Zhao-Huan, 量子场论讲义, §3.2 · Peskin & Schroeder, §3.1 · P. Woit, Quantum Theory, Groups and Representations, Ch. 5 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf).*

How do a matrix group and its Lie algebra determine each other, and which statements about representations may be checked on generators alone? The course defines a matrix Lie group and its Lie algebra ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2|Def. §C3.1.2]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3|Def. §C3.1.3]]); the Math vault has Lie groups, Lie algebras and the tangent spaces of the classical groups ([[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-1|591 Def. §50.1]], [[§49 Lie Bracket and Lie Algebra#^def-49-2|591 Def. §49.2]], [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]]). This section supplies what lies between them and what the physics chapters use without proof: the matrix exponential, one-parameter subgroups, why the Lie algebra is a *real* Lie algebra, homomorphisms and their differentials, the identity component, the adjoint representation, and the covering and integration theorems behind SU(2) → SO(3) and SL(2,ℂ) → SO⁺(1,3). Statements are numbered in reading order with one counter per section (Definition §CB.1.1, Theorem §CB.1.2, …); boxes shown as embeds keep their home numbers.

## Recalled: Lie groups, Lie algebras and matrix groups

A Lie group in general, defined in 591:

![[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-1]]

A (real) Lie algebra, defined in 591; the commutator of any associative product is a Lie bracket, proved there ([[§49 Lie Bracket and Lie Algebra#^prop-49-3|591 Prop. §49.3]]):

![[§49 Lie Bracket and Lie Algebra#^def-49-2]]

![[§49 Lie Bracket and Lie Algebra#^prop-49-3]]

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
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §1, eq. (3.1) · Woit, Quantum Theory, Groups and Representations, Ch. 5*

^def-cb-1-1

> [!theorem] Theorem §CB.1.2: Convergence and Algebraic Properties of the Exponential
> For $X, Y \in M_n(\mathbb C)$ and $s, t \in \mathbb R$:
> 1. the series of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]] converges absolutely, uniformly on every bounded set of $X$, and $\|e^X\| \le e^{\|X\|}$; $X \mapsto e^X$ is continuous (indeed smooth);
> 2. $e^0 = \mathbb 1$, and $e^X$ is invertible with $(e^X)^{-1} = e^{-X}$;
> 3. if $XY = YX$, then $e^{X + Y} = e^Xe^Y$; in particular $e^{(s + t)X} = e^{sX}e^{tX}$;
> 4. $e^{SXS^{-1}} = S\,e^X S^{-1}$ for invertible $S$; $(e^X)^{\mathsf T} = e^{X^{\mathsf T}}$, $\overline{e^X} = e^{\bar X}$, $(e^X)^\dagger = e^{X^\dagger}$;
> 5. $s \mapsto e^{sX}$ is differentiable with $\frac{d}{ds}e^{sX} = Xe^{sX} = e^{sX}X$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §1, Props. 3.1, 3.3, 3.4 · Meinrenken, Lie Groups and Lie Algebras, §2.2 (smoothness in X)*

^thm-cb-1-2

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
> **Step 5** (part 3). If $XY = YX$, the binomial theorem holds for $X + Y$: expanding $(X + Y)^m$ into $2^m$ words in $X$ and $Y$ and moving every $X$ to the left (allowed only because $XY = YX$) gives $(X + Y)^m = \sum_{k=0}^m\binom mk X^kY^{m-k}$. Step 4 then reads $e^Xe^Y = \sum_m(X + Y)^m/m! = e^{X + Y}$. ⚑ By-product: without $XY = YX$ this step fails, and the failure is measured by the commutator → [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]]. In particular $sX$ and $tX$ commute, so $e^{(s + t)X} = e^{sX}e^{tX}$.
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
> - Every property except part 3 holds for all matrices; part 3 is exactly where commutativity is needed, and its failure is the subject of Theorem §CB.1.5.
> - Only the submultiplicative norm and completeness are used, so the same proof works for the exponential of any operator on a finite-dimensional space, e.g. of $d(X)$ in a representation ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]]).
> - Used next: the determinant (Theorem §CB.1.3), the logarithm (Theorem §CB.1.4) and the one-parameter subgroups $s \mapsto e^{sX}$ (Theorem §CB.1.7).

^pf-cb-1-2

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]], [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]], [[§24 Uniform Convergence#^thm-24-2|451 Thm. §24.2]], [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]]

> [!theorem] Theorem §CB.1.3: Determinant of an Exponential
> For every $X \in M_n(\mathbb C)$, $\det e^X = e^{\operatorname{tr}X}$. In particular $e^X$ has determinant $1$ when $\operatorname{tr}X = 0$, and $\det e^X > 0$ when $X$ is real.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §4, Thm. 3.10 · used in [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]], Derivation, steps 1–2*

^thm-cb-1-3

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §4, Thm. 3.10 (https://arxiv.org/abs/math-ph/0005032). Hall treats diagonalizable, nilpotent and general $X$ separately; his nilpotent case already uses an upper-triangular form, and that form handles all three cases at once, which is the route followed here.*
>
> **Step 1** (triangular form). $X$ is an operator on the complex space $\mathbb C^n$, so some basis makes its matrix upper triangular ([[§16 Upper-Triangular Matrices#^ladr-5-47|LADR 5.47]]): $X = STS^{-1}$ with $S$ invertible (the change of basis) and $T$ upper triangular, $T_{ij} = 0$ for $i > j$. Its diagonal entries $\lambda_1, \dots, \lambda_n$ are the eigenvalues of $X$ ([[§16 Upper-Triangular Matrices#^ladr-5-41|LADR 5.41]]).
>
> **Step 2** (powers of a triangular matrix). If $A$, $B$ are upper triangular, then for $i > j$ every term of $(AB)_{ij} = \sum_lA_{il}B_{lj}$ vanishes (either $i > l$, so $A_{il} = 0$, or $l \ge i > j$, so $B_{lj} = 0$), and $(AB)_{ii} = \sum_lA_{il}B_{li}$ keeps only $l = i$, giving $A_{ii}B_{ii}$. By induction, $T^k$ is upper triangular with diagonal $\lambda_1^k, \dots, \lambda_n^k$.
>
> **Step 3** (the exponential of $T$). The partial sums $S_N(T) = \sum_{k\le N}T^k/k!$ are upper triangular with diagonal entries $\sum_{k\le N}\lambda_i^k/k!$. Entries converge separately ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], 1), so $e^T$ is upper triangular with diagonal $e^{\lambda_1}, \dots, e^{\lambda_n}$ (the zero entries stay zero in the limit).
>
> **Step 4** (conjugate back). By Theorem §CB.1.2, 4, $e^X = e^{STS^{-1}} = Se^TS^{-1}$. The determinant is multiplicative ([[§37 Determinants#^ladr-9-49|LADR 9.49]]), so $\det e^X = \det S\,\det e^T\,(\det S)^{-1} = \det e^T$, and the determinant of an upper-triangular matrix is the product of its diagonal entries ([[§37 Determinants#^ladr-9-48|LADR 9.48]]):
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
> - $\det\circ\exp = \exp\circ\operatorname{tr}$: the determinant condition of $SL$, $SU$, $SO$ linearizes to a trace condition (used in Theorem §CB.1.11).
> - $\det e^X > 0$ for real $X$: no real exponential reaches a matrix of negative determinant, e.g. a reflection; this is the algebraic shadow of Theorem §CB.1.16, 2.

^pf-cb-1-3

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], [[§16 Upper-Triangular Matrices#^ladr-5-47|LADR 5.47]], [[§16 Upper-Triangular Matrices#^ladr-5-41|LADR 5.41]], [[§37 Determinants#^ladr-9-48|LADR 9.48]], [[§37 Determinants#^ladr-9-49|LADR 9.49]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR 8.49]]

> [!theorem] Theorem §CB.1.4: The Logarithm Near the Identity
> For $A \in M_n(\mathbb C)$ with $\|A - \mathbb 1\| < 1$ the series $\log A = \sum_{k\ge1}\frac{(-1)^{k+1}}{k}(A - \mathbb 1)^k$ converges, $\log$ is continuous there, and $e^{\log A} = A$. For $\|X\| < \log 2$, $\|e^X - \mathbb 1\| < 1$ and $\log e^X = X$. Hence $\exp$ maps a neighbourhood of $0$ in $M_n(\mathbb C)$ homeomorphically onto a neighbourhood of $\mathbb 1$ in $GL(n, \mathbb C)$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §3, Lemma 3.5, Thm. 3.6*

^thm-cb-1-4

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §3, Lemma 3.5 and Thm. 3.6 with their proofs (https://arxiv.org/abs/math-ph/0005032); Hall's Exercise 4 (density of diagonalizable matrices) is done in Step 5, and the homeomorphism of the last sentence in Step 7.*
>
> **Step 1** (convergence and continuity of log). For $\|A - \mathbb 1\| \le r < 1$, Step 1 of the proof of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]] gives $\|(A - \mathbb 1)^k/k\| \le r^k/k$, and $\sum_kr^k/k < \infty$. So the series converges absolutely, uniformly on each set $\|A - \mathbb 1\| \le r$ (Weierstrass M-test, [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]]); its partial sums are polynomials, so $\log$ is continuous on $\{\|A - \mathbb 1\| < 1\}$ ([[§24 Uniform Convergence#^thm-24-2|451 Thm. §24.2]]).
>
> **Step 2** (the scalar case, Hall's Lemma 3.5). For real $x \in (-1, 1)$, $\frac{d}{dx}\log(1 - x) = -\frac1{1-x} = -\sum_{k\ge0}x^k$; integrating term by term from $0$ ([[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]]) and using $\log 1 = 0$ gives $\log(1 - x) = -\sum_{k\ge1}x^k/k$. With $z = 1 - x$ this is the series of the theorem, $\log z = \sum_{k\ge1}(-1)^{k+1}(z - 1)^k/k$, on the real interval $(0, 2)$. The same series defines an analytic function on the disc $|z - 1| < 1$ (radius of convergence $1$), and $e^{\log z}$ is analytic there and equals $z$ on $(0, 2)$; by the identity theorem ([[§CA.4 Contour Integration#^thm-ca-4-3|Theorem §CA.4.3]]) $e^{\log z} = z$ on the whole disc. For $|u| < \log 2$: $|e^u - 1| = |\sum_{k\ge1}u^k/k!| \le \sum_{k\ge1}|u|^k/k! = e^{|u|} - 1 < 1$, so $\log e^u$ is defined; it is analytic in $u$ on the disc $|u| < \log 2$ and equals $u$ for real $u$, hence everywhere there.
>
> **Step 3** (eigenvalues stay in the disc). If $Av = zv$ with $v \ne 0$, then $|(A - \mathbb 1)v| = |z - 1|\,|v|$ and $|(A - \mathbb 1)v| \le \|A - \mathbb 1\|\,|v|$, so $|z - 1| \le \|A - \mathbb 1\| < 1$. Likewise an eigenvalue $u$ of $X$ has $|u| \le \|X\|$.
>
> **Step 4** (diagonalizable $A$). Let $A = CDC^{-1}$ with $D = \operatorname{diag}(z_1, \dots, z_n)$ and $\|A - \mathbb 1\| < 1$. Then $A - \mathbb 1 = C(D - \mathbb 1)C^{-1}$, so $(A - \mathbb 1)^k = C\operatorname{diag}((z_i - 1)^k)C^{-1}$ (as in Step 7 of the proof of Theorem §CB.1.2), and summing (conjugation by $C$ is continuous), $\log A = C\operatorname{diag}(\log z_1, \dots, \log z_n)C^{-1}$, each $\log z_i$ defined by Step 3. By Theorem §CB.1.2, 4 and Step 2,
>
> $$
> e^{\log A} = C\operatorname{diag}\bigl(e^{\log z_1}, \dots, e^{\log z_n}\bigr)C^{-1} = C\operatorname{diag}(z_1, \dots, z_n)C^{-1} = A .
> $$
>
> **Step 5** (general $A$: approximation). Write $A = STS^{-1}$ with $T$ upper triangular ([[§16 Upper-Triangular Matrices#^ladr-5-47|LADR 5.47]]). Add small numbers to the diagonal: $T_m = T + \operatorname{diag}(\varepsilon_{1,m}, \dots, \varepsilon_{n,m})$ with $\varepsilon_{i,m} \to 0$ as $m \to \infty$, chosen so that the diagonal entries of $T_m$ are pairwise distinct. Then $A_m = ST_mS^{-1}$ has $n$ distinct eigenvalues ([[§16 Upper-Triangular Matrices#^ladr-5-41|LADR 5.41]]), so it is diagonalizable ([[§17 Diagonalizable Operators#^ladr-5-58|LADR 5.58]]), and $A_m \to A$. Since $\|A - \mathbb 1\| < 1$ and the norm is continuous, $\|A_m - \mathbb 1\| < 1$ for all large $m$. By Step 4, $e^{\log A_m} = A_m$; by continuity of $\log$ (Step 1) and of $\exp$ (Theorem §CB.1.2, 1), letting $m \to \infty$ gives $e^{\log A} = A$.
>
> **Step 6** (log undoes exp near 0). For $\|X\| < \log 2$, Step 1 of the proof of Theorem §CB.1.2 gives $\|e^X - \mathbb 1\| \le \sum_{k\ge1}\|X\|^k/k! = e^{\|X\|} - 1 < 1$, so $\log e^X$ is defined. If $X = CDC^{-1}$ is diagonalizable with eigenvalues $u_i$, $|u_i| < \log 2$ (Step 3), then $e^X = C\operatorname{diag}(e^{u_i})C^{-1}$ and, as in Step 4, $\log e^X = C\operatorname{diag}(\log e^{u_i})C^{-1} = C\operatorname{diag}(u_i)C^{-1} = X$ by Step 2. A general $X$ with $\|X\| < \log 2$ is the limit of diagonalizable $X_m$ with $\|X_m\| < \log 2$ (Step 5's construction), and $X \mapsto \log e^X$ is continuous on $\{\|X\| < \log 2\}$ (a composition of continuous maps), so $\log e^X = X$.
>
> **Step 7** (exp is a local homeomorphism). Put $U = \{X : \|X\| < \log 2\}$ and $B = \{A : \|A - \mathbb 1\| < 1\}$, both open. By Step 6, $\exp$ maps $U$ into $B$ and $\log\circ\exp = \mathrm{id}$ on $U$, so $\exp|_U$ is injective. Its image is $\exp(U) = \{A \in B : \log A \in U\}$: if $A = e^X$ with $X \in U$, then $\log A = X \in U$; conversely, if $A \in B$ and $\log A \in U$, then $A = e^{\log A}$ by Step 5. This set is open, as the preimage of the open $U$ under the continuous $\log : B \to M_n(\mathbb C)$; it contains $\mathbb 1 = e^0$, and it lies in $GL(n, \mathbb C)$ by Theorem §CB.1.2, 2. The inverse of $\exp|_U$ is $\log|_{\exp(U)}$, continuous by Step 1. So $\exp : U \to \exp(U)$ is a homeomorphism onto a neighbourhood of $\mathbb 1$.
>
> **What the proof shows.**
> - Near the identity every invertible matrix has exactly one small logarithm; this local invertibility is the input to one-parameter subgroups (Theorem §CB.1.7) and to the closed-subgroup theorem (Theorem §CB.1.10).
> - Globally $\exp$ is neither injective ($e^{2\pi i\mathbb 1} = e^0$) nor, on a general matrix group, surjective; only the local statement is used.
> - If $A$ is real, every term of the series is real, so $\log A$ is real (Hall, Thm. 3.6).

^pf-cb-1-4

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]], [[§24 Uniform Convergence#^thm-24-2|451 Thm. §24.2]], [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]], [[§CA.4 Contour Integration#^thm-ca-4-3|Theorem §CA.4.3]], [[§16 Upper-Triangular Matrices#^ladr-5-47|LADR 5.47]], [[§16 Upper-Triangular Matrices#^ladr-5-41|LADR 5.41]], [[§17 Diagonalizable Operators#^ladr-5-58|LADR 5.58]]

> [!theorem] Theorem §CB.1.5: Lie Product Formula and the Commutator as a Second-Order Term
> For $X, Y \in M_n(\mathbb C)$:
> 1. $e^{X + Y} = \lim_{m\to\infty}\bigl(e^{X/m}e^{Y/m}\bigr)^m$;
> 2. $e^{sX}e^{sY} = \exp\bigl(s(X + Y) + \frac{s^2}{2}[X, Y] + O(s^3)\bigr)$ as $s \to 0$ (the first terms of the Baker–Campbell–Hausdorff series);
> 3. $e^{sX}e^{sY}e^{-sX}e^{-sY} = \mathbb 1 + s^2[X, Y] + O(s^3)$ as $s \to 0$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §§3–4, Prop. 3.7, Thm. 3.9 (part 1); Ch. 4 §3, eq. (4.2) and Exercise 4 (part 2) · Meinrenken, Lie Groups and Lie Algebras, proof of Prop. 4.7 (part 3) · the second-order commutator is the content of [[§C3.2 The Lorentz Algebra#^rem-c3-2-2|§C3.2, Remark: Two boosts make a rotation]]*

^thm-cb-1-5

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3, Prop. 3.7 and Thm. 3.9 with proofs, and Ch. 4 §3 (the series form (4.2) of Baker–Campbell–Hausdorff, which Exercise 4 there asks to check by multiplying out power series, as done in Step 5) (https://arxiv.org/abs/math-ph/0005032) · E. Meinrenken, Lie Groups and Lie Algebras (Toronto, Winter 2026), proof of Prop. 4.7, "by Taylor expansions" (https://www.math.toronto.edu/mein/teaching/LectureNotes/lie.pdf), written out in Step 6. Throughout, $a = \|X\| + \|Y\|$ and "$O(s^k)$" means a matrix of norm at most a constant times $|s|^k$ for $|s| \le 1$.*
>
> **Step 1** (the logarithm to first order; Hall, Prop. 3.7). For $\|B\| \le \frac12$, $\log(\mathbb 1 + B) - B = \sum_{k\ge2}(-1)^{k+1}B^k/k$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-4|Theorem §CB.1.4]]), so
>
> $$
> \|\log(\mathbb 1 + B) - B\| \le \|B\|^2\sum_{k\ge2}\frac{\|B\|^{k-2}}{k} \le \|B\|^2\sum_{k\ge2}\frac{(1/2)^{k-2}}{2} = \|B\|^2 .
> $$
>
> In the same way $\|\log(\mathbb 1 + B) - B + \frac12B^2\| \le \|B\|^3\sum_{k\ge3}\frac{(1/2)^{k-3}}{3} \le \|B\|^3$.
>
> **Step 2** (the product to first order). By Step 4 of the proof of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]] with $X/m$, $Y/m$ in place of $X$, $Y$,
>
> $$
> e^{X/m}e^{Y/m} = \mathbb 1 + \frac Xm + \frac Ym + C_m, \qquad C_m = \sum_{k + l \ge 2}\frac{X^kY^l}{m^{k+l}\,k!\,l!}, \qquad \|C_m\| \le \sum_{j\ge2}\frac{(a/m)^j}{j!} \le \frac{a^2e^a}{m^2}
> $$
>
> for $m \ge 1$, using $\sum_{j\ge2}t^j/j! \le t^2\sum_{j\ge2}t^{j-2}/(j-2)! = t^2e^t$ with $t = a/m \le a$.
>
> **Step 3** (take the logarithm). Put $B_m = X/m + Y/m + C_m$; $\|B_m\| \le a/m + a^2e^a/m^2 \to 0$, so $\|B_m\| \le \frac12$ for all large $m$. By Theorem §CB.1.4, $e^{X/m}e^{Y/m} = \exp(\log(\mathbb 1 + B_m))$, and by Step 1, $\log(\mathbb 1 + B_m) = B_m + E_m$ with $\|E_m\| \le \|B_m\|^2 \le \mathrm{const}/m^2$.
>
> **Step 4** (part 1). The $m$ factors of $(e^{X/m}e^{Y/m})^m = \bigl(\exp(B_m + E_m)\bigr)^m$ are exponentials of the same matrix, which commutes with itself, so by Theorem §CB.1.2, 3, $(e^{X/m}e^{Y/m})^m = \exp(m(B_m + E_m)) = \exp(X + Y + mC_m + mE_m)$. Both $mC_m$ and $mE_m$ have norm at most $\mathrm{const}/m \to 0$, and $\exp$ is continuous (Theorem §CB.1.2, 1), so the limit is $e^{X + Y}$.
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
> and exponentiating (Theorem §CB.1.4) gives part 2.
>
> **Step 6** (part 3: the group commutator). Multiply the four series of $e^{sX}e^{sY}e^{-sX}e^{-sY}$ out, as in Step 4 of the proof of Theorem §CB.1.2 applied three times. The terms of total degree $j \ge 3$ in $s$ together have norm at most $\sum_{j\ge3}(2a|s|)^j/j! \le (2a)^3e^{2a}|s|^3$, the degree-$\ge3$ part of the majorant $e^{|s|\|X\|}e^{|s|\|Y\|}e^{|s|\|X\|}e^{|s|\|Y\|} = e^{2a|s|}$; so they are $O(s^3)$. The terms of degree $\le 2$ are:
> - degree $0$: $\mathbb 1$;
> - degree $1$: $sX + sY - sX - sY = 0$;
> - degree $2$ from one factor: $\frac{s^2}2(X^2 + Y^2 + X^2 + Y^2) = s^2(X^2 + Y^2)$;
> - degree $2$ from two factors (first-order term of an earlier factor times first-order term of a later one, six pairs in order): $s^2\bigl(XY - X^2 - XY - YX - Y^2 + XY\bigr) = s^2(XY - YX - X^2 - Y^2)$.
>
> Adding the two degree-2 lines, $X^2 + Y^2$ cancels and $e^{sX}e^{sY}e^{-sX}e^{-sY} = \mathbb 1 + s^2[X, Y] + O(s^3)$.
>
> **What the proof shows.**
> - ⚑ By-product: to first order in $s$ the group law is addition, $e^{sX}e^{sY} = e^{s(X + Y) + O(s^2)}$; the commutator is the first correction, at order $s^2$, and it is all that the group remembers of non-commutativity at that order → [[§C3.2 The Lorentz Algebra#^rem-c3-2-2|§C3.2, Remark: Two boosts make a rotation]].
> - Part 1 builds $e^{X + Y}$ from products of exponentials of $X$ and $Y$ alone; this is why the Lie algebra of a closed group is closed under addition (Theorem §CB.1.8) and why the differential of a homomorphism is additive (Theorem §CB.1.14).
> - Part 3 is the bridge from groups to brackets used in Theorem §CB.1.9, 3.

^pf-cb-1-5

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-4|Theorem §CB.1.4]]

## One-parameter subgroups and the Lie algebra

> [!definition] Definition §CB.1.6: One-Parameter Subgroup
> A **one-parameter subgroup** of $GL(n, \mathbb C)$ is a continuous group homomorphism ([[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]) $\gamma : (\mathbb R, +) \to GL(n, \mathbb C)$: $\gamma(s + t) = \gamma(s)\gamma(t)$, $\gamma(0) = \mathbb 1$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §4, Def. 3.11 · Woit, Quantum Theory, Groups and Representations, Ch. 5*

^def-cb-1-6

> [!theorem] Theorem §CB.1.7: One-Parameter Subgroups Are Exponentials
> If $\gamma$ is a one-parameter subgroup of $GL(n, \mathbb C)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-6|Def. §CB.1.6]]), then $\gamma$ is differentiable and $\gamma(s) = e^{sX}$ for all $s$, with the unique matrix $X = \gamma'(0)$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §4, Def. 3.11, Thm. 3.12, with Prop. 3.8*

^thm-cb-1-7

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3, Thm. 3.12 and its proof (smoothing by a bump function), with Prop. 3.8 (https://arxiv.org/abs/math-ph/0005032).*
>
> **Step 1** (uniqueness). If $\gamma(s) = e^{sX}$ for all $s$, then $X = \gamma'(0)$ by [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], 5. So at most one $X$ works, and only existence remains.
>
> **Step 2** (smoothing). Choose a smooth function $f \ge 0$ on $\mathbb R$ with support in $[-\delta, \delta]$ and $\int f = 1$, where $\delta > 0$ is so small that $\|\gamma(s) - \mathbb 1\| < 1$ for $|s| \le \delta$ (possible since $\gamma$ is continuous and $\gamma(0) = \mathbb 1$). Define $F(t) = \int\gamma(t + s)f(s)\,ds$ (entrywise integrals of continuous functions over $[-\delta, \delta]$).
>
> **Step 3** ($F$ is smooth). Substitute $u = t + s$ (for fixed $t$; $du = ds$, the limits $\pm\delta$ become $t \pm \delta$): $F(t) = \int\gamma(u)f(u - t)\,du$. Now $t$ appears only in the smooth $f$, and on a bounded $t$-interval the integrand's $t$-derivatives $-\gamma(u)f'(u - t)$, $\gamma(u)f''(u - t)$, … are bounded by an integrable function of $u$ (continuous on a compact $u$-interval). Differentiation under the integral ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], 2), repeated, shows that $F$ is smooth.
>
> **Step 4** ($\gamma$ is smooth). By the homomorphism property, $\gamma(t + s) = \gamma(t)\gamma(s)$, so $F(t) = \gamma(t)M$ with the constant matrix $M = \int\gamma(s)f(s)\,ds$. Since $\int f = 1$, $M - \mathbb 1 = \int(\gamma(s) - \mathbb 1)f(s)\,ds$ has norm $\le \sup_{|s|\le\delta}\|\gamma(s) - \mathbb 1\| < 1$, so $M = e^{\log M}$ is invertible ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-4|Theorem §CB.1.4]]; Theorem §CB.1.2, 2). Hence $\gamma(t) = F(t)M^{-1}$ is smooth.
>
> **Step 5** (Taylor at 0). Put $X = \gamma'(0)$. Taylor's theorem with remainder ([[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]], applied to the real and imaginary parts of each entry on $[-1, 1]$) gives a constant $K$ with $\|\gamma(h) - \mathbb 1 - hX\| \le Kh^2$ for $|h| \le 1$.
>
> **Step 6** (the group law and the limit; Hall, Prop. 3.8). Fix $t$. For each integer $m \ge |t|$, $\gamma(t) = \gamma(t/m)^m$ (the homomorphism property applied $m - 1$ times), and by Step 5
>
> $$
> \gamma(t) = \Bigl(\mathbb 1 + \frac{tX}m + C_m\Bigr)^m, \qquad \|C_m\| \le \frac{Kt^2}{m^2} .
> $$
>
> This is the situation of Steps 3–4 of the proof of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], with $tX$ in place of $X + Y$ and $C_m$ again of order $1/m^2$: $B_m = tX/m + C_m$ has $\|B_m\| \le \frac12$ for large $m$, $\mathbb 1 + B_m = \exp(B_m + E_m)$ with $\|E_m\| \le \|B_m\|^2 = O(1/m^2)$, and $(\mathbb 1 + B_m)^m = \exp(tX + mC_m + mE_m) \to e^{tX}$. The left side is $\gamma(t)$ for every $m$, so $\gamma(t) = e^{tX}$.
>
> **What the proof shows.**
> - Continuity alone forces smoothness and the exponential form; nothing about the group beyond the homomorphism property is used.
> - ⚑ By-product: every continuous homomorphism $\mathbb R \to GL(n, \mathbb C)$ has a generator $X = \gamma'(0)$; for a representation this is the statement that represented one-parameter groups are $e^{s\,d(X)}$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]], whose derivation assumed smoothness; this theorem removes the assumption).
> - Used next: the differential of a homomorphism (Theorem §CB.1.14).

^pf-cb-1-7

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-6|Def. §CB.1.6]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-4|Theorem §CB.1.4]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]] (Steps 3–4 of its proof), [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]]

The course defines the Lie algebra of a matrix Lie group through its one-parameter subgroups, in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3]]

> [!theorem] Theorem §CB.1.8: The Lie Algebra Is a Real Lie Algebra
> Let $G$ be a matrix Lie group ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2|Def. §C3.1.2]]) and $\mathfrak g$ its Lie algebra ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3|Def. §C3.1.3]]). Then
> 1. $\mathfrak g$ is a **real** vector subspace of $M_n(\mathbb C)$: $X, Y \in \mathfrak g$ and $a, b \in \mathbb R$ give $aX + bY \in \mathfrak g$; in general $iX \notin \mathfrak g$;
> 2. $gXg^{-1} \in \mathfrak g$ for all $g \in G$, $X \in \mathfrak g$;
> 3. $[X, Y] = XY - YX \in \mathfrak g$ for $X, Y \in \mathfrak g$, so $(\mathfrak g, [\cdot,\cdot])$ is a real Lie algebra ([[§49 Lie Bracket and Lie Algebra#^def-49-2|591 Def. §49.2]], [[§49 Lie Bracket and Lie Algebra#^prop-49-3|591 Prop. §49.3]]).
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §6, Props. 3.14, 3.15, Thm. 3.16, Prop. 3.30 · Woit, §5.5 (the Lie algebra is a real vector space)*

^thm-cb-1-8

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §6, Prop. 3.15, Thm. 3.16 and Prop. 3.30 with proofs (https://arxiv.org/abs/math-ph/0005032); the example in Step 3 is P. Woit's, Quantum Theory, Groups and Representations, §5.5 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf).*
>
> **Step 1** (real multiples). If $X \in \mathfrak g$ and $a \in \mathbb R$, then $e^{s(aX)} = e^{(sa)X} \in G$ for every real $s$, because $sa$ is again real. So $aX \in \mathfrak g$.
>
> **Step 2** (sums, by the Lie product formula). Let $X, Y \in \mathfrak g$ and $s \in \mathbb R$. By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], 1, applied to $sX$, $sY$,
>
> $$
> e^{s(X + Y)} = \lim_{m\to\infty}\bigl(e^{sX/m}e^{sY/m}\bigr)^m .
> $$
>
> Each $e^{sX/m}$, $e^{sY/m}$ lies in $G$ (Step 1 and the definition of $\mathfrak g$), so each product on the right lies in $G$ ($G$ is a group). The limit $e^{s(X + Y)}$ is invertible ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], 2), and $G$ is closed in $GL(n, \mathbb C)$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2|Def. §C3.1.2]]), so $e^{s(X + Y)} \in G$. Hence $X + Y \in \mathfrak g$; with Step 1, $aX + bY \in \mathfrak g$ for real $a$, $b$. ⚑ By-product: this is the one place in the proof where closedness of $G$ enters (a limit of elements of $G$ must stay in $G$); it enters again, more strongly, in the closed-subgroup theorem → [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]].
>
> **Step 3** (in general $iX \notin \mathfrak g$). $X = -\frac i2\sigma^3 \in \mathfrak{su}(2)$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]]), but $iX = \frac12\sigma^3$ is Hermitian and nonzero, so $(iX)^\dagger \ne -iX$, and $e^{s\sigma^3/2} = \operatorname{diag}(e^{s/2}, e^{-s/2})$ is not unitary for $s \ne 0$: $iX \notin \mathfrak{su}(2)$. So $\mathfrak g$ is a real, not a complex, subspace of $M_n(\mathbb C)$.
>
> **Step 4** (part 2). For $g \in G$, $X \in \mathfrak g$ and real $s$, Theorem §CB.1.2, 4 gives $e^{s\,gXg^{-1}} = g\,e^{sX}g^{-1}$, a product of three elements of $G$. So $gXg^{-1} \in \mathfrak g$.
>
> **Step 5** (part 3). Fix $X, Y \in \mathfrak g$. By Step 4 with $g = e^{sX}$, the curve $c(s) = e^{sX}Ye^{-sX}$ lies in $\mathfrak g$ for all $s$. By the product rule and Theorem §CB.1.2, 5,
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
> - The definition through one-parameter subgroups with *real* parameter is what makes $\mathfrak g$ real; the physicists' Hermitian generators $T_a = iX_a$ lie outside $\mathfrak g$ → [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-5|Theorem §CB.2.5]].
> - The bracket comes from conjugation (Step 5): it is the derivative of the adjoint action, made precise in Theorem §CB.1.20.

^pf-cb-1-8

*Uses:* [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2|Def. §C3.1.2]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3|Def. §C3.1.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]], [[§49 Lie Bracket and Lie Algebra#^prop-49-3|591 Prop. §49.3]], [[§49 Lie Bracket and Lie Algebra#^def-49-2|591 Def. §49.2]]

> [!theorem] Theorem §CB.1.9: The Lie Algebra Is the Tangent Space at the Identity
> Let $G$ be a matrix Lie group with Lie algebra $\mathfrak g$.
> 1. $\mathfrak g$ is the set of velocities $\gamma'(0)$ of the differentiable curves $\gamma$ in $M_n(\mathbb C)$ that lie in $G$ and have $\gamma(0) = \mathbb 1$.
> 2. For the classical groups of [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]], $\mathfrak g$ equals 591's geometric tangent space $T^{\mathrm{geo}}_IG$.
> 3. Under the identification of a left-invariant vector field with its value at $\mathbb 1$, the Lie algebra of left-invariant vector fields of [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-4|591 Def. §50.4]] is $\mathfrak g$, and the bracket of vector fields becomes the commutator $XY - YX$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §7, Lemma 3.24 (parts 1–2) · Lee, Introduction to Smooth Manifolds, Props. 8.41, 8.48, Thm. 8.46 (part 3) · 591 §25, §49*

^thm-cb-1-9

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §7, Lemma 3.24 and its proof (https://arxiv.org/abs/math-ph/0005032), for Steps 1–3 · J. M. Lee, Introduction to Smooth Manifolds, 2nd ed., Prop. 8.41 (the bracket of left-invariant fields on GL(n,ℝ)), Prop. 8.48 (GL(n,ℂ)) and Thm. 8.46 (Lie subgroups), for Steps 5–6. Part 3 uses Theorem §CB.1.10, proved next; that proof uses only Step 1 below, so there is no circularity.*
>
> **Step 1** (the limit lemma; Hall, Lemma 3.24). *Let $g_k \in G$, $g_k \to \mathbb 1$, $g_k \ne \mathbb 1$, let $Y_k = \log g_k$ (defined for large $k$, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-4|Theorem §CB.1.4]]), and let $|\cdot|$ be any norm on $M_n(\mathbb C)$. If $Y_k/|Y_k| \to Y$, then $Y \in \mathfrak g$.* Proof: $Y_k \ne 0$ (else $g_k = e^0 = \mathbb 1$), and $Y_k \to \log\mathbb 1 = 0$ by continuity of $\log$. Fix $t \in \mathbb R$ and put $m_k = \lfloor t/|Y_k|\rfloor \in \mathbb Z$; then $|m_k|Y_k| - t| \le |Y_k| \to 0$. Since $e^{Y_k} = g_k$, Theorem §CB.1.2, 3 (for negative $m_k$ with Theorem §CB.1.2, 2) gives $e^{m_kY_k} = g_k^{m_k} \in G$. And $m_kY_k = (m_k|Y_k|)\,(Y_k/|Y_k|) \to tY$, so by continuity of $\exp$, $g_k^{m_k} \to e^{tY}$, which is invertible; $G$ is closed in $GL(n, \mathbb C)$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2|Def. §C3.1.2]]), so $e^{tY} \in G$. As $t$ was arbitrary, $Y \in \mathfrak g$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3|Def. §C3.1.3]]).
>
> **Step 2** (part 1, $\mathfrak g \subset$ velocities). For $X \in \mathfrak g$, $\gamma(s) = e^{sX}$ is differentiable, lies in $G$, has $\gamma(0) = \mathbb 1$ and $\gamma'(0) = X$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], 5).
>
> **Step 3** (part 1, velocities $\subset \mathfrak g$). Let $\gamma$ be differentiable with values in $G$, $\gamma(0) = \mathbb 1$, $V = \gamma'(0)$. If $V = 0$, $V \in \mathfrak g$. Otherwise, for small $|s|$, $\|\gamma(s) - \mathbb 1\| \le \frac12$ and $Y(s) = \log\gamma(s)$ is defined; by Step 1 of the proof of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], $Y(s) = (\gamma(s) - \mathbb 1) + E(s)$ with $\|E(s)\| \le \|\gamma(s) - \mathbb 1\|^2$. Divide by $s$: $(\gamma(s) - \mathbb 1)/s \to V$, and $\|E(s)\|/|s| \le \|\gamma(s) - \mathbb 1\|\cdot\|\gamma(s) - \mathbb 1\|/|s| \to 0\cdot\|V\| = 0$. So $Y(s)/s \to V$. Put $s_k = 1/k$, $g_k = \gamma(s_k) \to \mathbb 1$, $Y_k = Y(s_k)$; for large $k$, $Y_k/s_k$ is close to $V \ne 0$, so $Y_k \ne 0$ and $Y_k/\|Y_k\| = (Y_k/s_k)/\|Y_k/s_k\| \to V/\|V\|$. Step 1 gives $V/\|V\| \in \mathfrak g$, and $V = \|V\|\cdot V/\|V\| \in \mathfrak g$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], 1).
>
> **Step 4** (part 2). The groups of [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]] are closed subgroups of $GL(n, \mathbb C)$, so the above applies. $T^{\mathrm{geo}}_IG$ is the set of velocities of *smooth* curves in $G$ through $\mathbb 1$ ([[§25 The Geometric Tangent Space#^def-25-1|591 Def. §25.1]]). Smooth curves are differentiable, so $T^{\mathrm{geo}}_IG \subset \mathfrak g$ by Step 3; and each $X \in \mathfrak g$ is the velocity of $e^{sX}$, which is smooth (Theorem §CB.1.2, 5, applied repeatedly: $\frac{d^k}{ds^k}e^{sX} = X^ke^{sX}$). So $T^{\mathrm{geo}}_IG = \mathfrak g$.
>
> **Step 5** (part 3 for $GL(n, \mathbb C)$; Lee, Props. 8.41, 8.48). $GL(n, \mathbb C)$ is open in $M_n(\mathbb C) \cong \mathbb R^{2n^2}$, so its tangent space at every point is $M_n(\mathbb C)$. Left translation $L_g$ is the restriction of the linear map $A \mapsto gA$, so its differential is that same map, and a left-invariant field with value $A$ at $\mathbb 1$ is $\mathbf X^A_g = gA$ (the proof of [[§50 Lie Groups and Left-Invariant Vector Fields#^ex-50-1|591 Ex. §50.1]], verbatim over $\mathbb C$). In the global linear coordinates the bracket of vector fields is $[\mathbf X, \mathbf Y]_g = D\mathbf Y_g(\mathbf X_g) - D\mathbf X_g(\mathbf Y_g)$ ([[§49 Lie Bracket and Lie Algebra#^prop-49-2|591 Prop. §49.2]], written with the derivative $D$ of the component functions). For $\mathbf Y = \mathbf X^B$, $g \mapsto gB$ is linear, so $D\mathbf X^B_g(V) = VB$. Hence
>
> $$
> [\mathbf X^A, \mathbf X^B]_g = (gA)B - (gB)A = g(AB - BA) = \mathbf X^{[A, B]}_g ,
> $$
>
> and at $g = \mathbb 1$ the bracket of the fields is the commutator of their values.
>
> **Step 6** (part 3 for $G$; Lee, Thm. 8.46). By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]], $G$ is an embedded submanifold and a Lie group, and its tangent space at $\mathbb 1$ is $\mathfrak g$ (Step 3 of that proof: near $\mathbb 1$, $G$ is the image of $\mathfrak g$ under a diffeomorphism with derivative the identity at $0$). The inclusion $G \to GL(n, \mathbb C)$ is a Lie group homomorphism, and Lee's Thm. 8.46 identifies the left-invariant fields of $G$ with those left-invariant fields of $GL(n, \mathbb C)$ whose value at $\mathbb 1$ lies in $T_{\mathbb 1}G = \mathfrak g$, preserving brackets. With Step 5, identifying a left-invariant field on $G$ with its value at $\mathbb 1$ turns the bracket of vector fields into $XY - YX$.
>
> **What the proof shows.**
> - Three definitions agree: one-parameter subgroups (the course's), velocities of curves (591 §25), left-invariant vector fields (591 §50). The physics chapters may use whichever is convenient.
> - The sign: left-invariant fields give $+[A, B]$; right-invariant fields would give $-[A, B]$ (Meinrenken, Remark 4.9), one more place where a sign convention hides.

^pf-cb-1-9

*Uses:* [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2|Def. §C3.1.2]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3|Def. §C3.1.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-4|Theorem §CB.1.4]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]], [[§25 The Geometric Tangent Space#^def-25-1|591 Def. §25.1]], [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]], [[§50 Lie Groups and Left-Invariant Vector Fields#^ex-50-1|591 Ex. §50.1]], [[§49 Lie Bracket and Lie Algebra#^prop-49-2|591 Prop. §49.2]]

> [!theorem] Theorem §CB.1.10: Closed-Subgroup Theorem
> Every closed subgroup $G$ of $GL(n, \mathbb C)$ is an embedded submanifold of $GL(n, \mathbb C)$ of real dimension $\dim_{\mathbb R}\mathfrak g$, and with this structure a Lie group ([[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-1|591 Def. §50.1]]). There is a neighbourhood $U$ of $0$ in $M_n(\mathbb C)$ such that $\exp$ maps $U \cap \mathfrak g$ homeomorphically onto a neighbourhood of $\mathbb 1$ in $G$.
>
> *Source: Meinrenken, Lie Groups and Lie Algebras, §2.6, Thm. 2.16 (von Neumann's proof) · Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §7, Thm. 3.23 · Lee, Introduction to Smooth Manifolds, Prop. 7.11 · cited in [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2|Def. §C3.1.2]] · 591 when the course reaches it*

^thm-cb-1-10

> [!proof]- Proof
> *Source: E. Meinrenken, Lie Groups and Lie Algebras, lecture notes (Toronto, Winter 2026), §2.6, Thm. 2.16 and its proof (https://www.math.toronto.edu/mein/teaching/LectureNotes/lie.pdf), written there for $GL(n, \mathbb R)$ and carried over verbatim to $GL(n, \mathbb C)$ regarded as an open subset of $M_n(\mathbb C) \cong \mathbb R^{2n^2}$; the same argument is B. C. Hall, An Elementary Introduction to Groups and Representations, Thm. 3.23 (https://arxiv.org/abs/math-ph/0005032). Decision SPEC-CB 7 allowed a clean source proof here; this is it. The Lie group structure (Step 5) is J. M. Lee, Introduction to Smooth Manifolds, 2nd ed., Prop. 7.11.*
>
> **Step 1** (a complement and a map). $\mathfrak g$ is a real subspace of $M_n(\mathbb C)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]]). Regard $M_n(\mathbb C)$ as the real Euclidean space $\mathbb R^{2n^2}$ (real and imaginary parts of the entries), with norm $|\cdot|$, and let $\mathfrak d = \mathfrak g^\perp$ be the orthogonal complement, so $M_n(\mathbb C) = \mathfrak g \oplus \mathfrak d$. Define
>
> $$
> \Phi : M_n(\mathbb C) \to GL(n, \mathbb C), \qquad \Phi(X + Y) = e^Xe^Y \qquad (X \in \mathfrak g,\ Y \in \mathfrak d).
> $$
>
> $\Phi$ is smooth ($\exp$ is smooth, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], 1, and the product is polynomial).
>
> **Step 2** (the derivative at 0 is the identity). For $X \in \mathfrak g$, $\frac{d}{dt}\Phi(tX)|_0 = \frac{d}{dt}e^{tX}|_0 = X$; for $Y \in \mathfrak d$, $\frac{d}{dt}\Phi(tY)|_0 = Y$ (Theorem §CB.1.2, 5). By linearity of the derivative, $D\Phi_0 = \mathrm{id}$ on $\mathfrak g \oplus \mathfrak d$. By the inverse function theorem ([[§33 Local Diffeomorphisms#^thm-33-1|591 Thm. §33.1]]) there is $\varepsilon > 0$ such that $\Phi$ maps the open ball $B_\varepsilon = \{|Z| < \varepsilon\}$ diffeomorphically onto an open neighbourhood of $\mathbb 1$.
>
> **Step 3** (the slice at the identity; Meinrenken's Claim). *There is $r \in (0, \varepsilon]$ with $\Phi(B_r \cap \mathfrak g) = \Phi(B_r) \cap G$.* The inclusion $\subset$ holds for every $r$: for $X \in \mathfrak g$, $\Phi(X) = e^X \in G$. Suppose $\supset$ fails for every $r = \varepsilon/k$, $k = 1, 2, \dots$. Then there are $Z_k \in B_{\varepsilon/k}$ with $\Phi(Z_k) \in G$ but $\Phi(Z_k) \notin \Phi(B_{\varepsilon/k}\cap\mathfrak g)$; as $\Phi$ is injective on $B_\varepsilon$, $Z_k \notin \mathfrak g$. Write $Z_k = X_k + Y_k$ ($X_k \in \mathfrak g$, $Y_k \in \mathfrak d$); then $Y_k \ne 0$, $|Y_k| \le |Z_k| < \varepsilon/k$ (orthogonal decomposition), and $e^{Y_k} = e^{-X_k}\Phi(Z_k) \in G$ (both factors in $G$). The unit vectors $Y_k/|Y_k|$ lie in the unit sphere of $\mathfrak d$, which is compact, so a subsequence converges to some $Y \in \mathfrak d$ with $|Y| = 1$. Along it, $g_k = e^{Y_k} \to \mathbb 1$, and for large $k$, $\log g_k = Y_k$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-4|Theorem §CB.1.4]], since $Y_k \to 0$). Step 1 of the proof of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-9|Theorem §CB.1.9]] (the limit lemma, which uses that $G$ is closed) gives $Y \in \mathfrak g$. So $Y \in \mathfrak g \cap \mathfrak d = \{0\}$, contradicting $|Y| = 1$.
>
> **Step 4** (charts; the embedded submanifold). Let $U_{\mathbb 1} = \Phi(B_r)$ and $\psi = (\Phi|_{B_r})^{-1} : U_{\mathbb 1} \to B_r$, a chart of the open set $GL(n, \mathbb C) \subset M_n(\mathbb C)$. By Step 3, $\psi(U_{\mathbb 1} \cap G) = B_r \cap \mathfrak g$: in linear coordinates adapted to $\mathfrak g \oplus \mathfrak d$, $U_{\mathbb 1} \cap G$ is the set where the $\mathfrak d$-coordinates vanish. For $g \in G$, left multiplication $L_g(A) = gA$ is a linear isomorphism of $M_n(\mathbb C)$ mapping $GL(n, \mathbb C)$ onto itself and $G$ onto itself ($G$ is a group). So $U_g = gU_{\mathbb 1}$ with the chart $\psi\circ L_{g^{-1}}$ satisfies $\psi\circ L_{g^{-1}}(U_g \cap G) = B_r \cap \mathfrak g$. These are adapted charts around every point of $G$: $G$ is a submanifold of $GL(n, \mathbb C)$ ([[§35 Submanifolds#^def-35-1|591 Def. §35.1]]) of dimension $\dim_{\mathbb R}\mathfrak g$.
>
> **Step 5** (a Lie group). Multiplication $GL\times GL \to GL$ and inversion (Cramer's rule) are smooth; their restrictions to $G\times G$ and $G$ are smooth maps into $GL(n, \mathbb C)$ with values in $G$, hence smooth into $G$ ([[§35 Submanifolds#^lem-35-3|591 Lemma §35.3]], 2; Lee, Prop. 7.11). With its subspace topology $G$ is a topological group, so $G$ is a Lie group ([[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-1|591 Def. §50.1]]).
>
> **Step 6** (the exponential chart). On $B_r \cap \mathfrak g$, $\Phi = \exp$. By Steps 2–3, $\exp$ maps $B_r \cap \mathfrak g$ bijectively onto $\Phi(B_r) \cap G$, which is open in $G$ and contains $\mathbb 1$; it is continuous with continuous inverse $\psi|_{\Phi(B_r)\cap G}$. This is the last assertion, with $U = B_r$.
>
> **What the proof shows.**
> - Closedness enters only through the limit lemma (Step 3); for a non-closed subgroup, such as a line of irrational slope on a torus, it fails and the subgroup is not embedded.
> - ⚑ By-product: near $\mathbb 1$, $G$ is exactly $\exp$ of a neighbourhood of $0$ in $\mathfrak g$; every statement "check it on generators" rests on this → Theorems §CB.1.16, §CB.1.17, §CB.1.23.
> - Every matrix Lie group of the course ($SO(3)$, $SU(2)$, $SO^+(1,3)$, $SL(2, \mathbb C)$, $SU(2)\times SU(2)$) is therefore a Lie group in the sense of 591, with no separate regular-value computation needed.

^pf-cb-1-10

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-4|Theorem §CB.1.4]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-9|Theorem §CB.1.9]] (Step 1 of its proof only), [[§33 Local Diffeomorphisms#^thm-33-1|591 Thm. §33.1]], [[§35 Submanifolds#^def-35-1|591 Def. §35.1]], [[§35 Submanifolds#^lem-35-3|591 Lemma §35.3]], [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-1|591 Def. §50.1]]

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
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §§5.2–5.6 · 591 Thm. §25.5 (the real groups) · the user's PHY 513 notes, Ch. 7 §7.2 · [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]] (the Lorentz case)*

^thm-cb-1-11

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3, §§5.2 (GL), 5.3 (SL), 5.4 (U, SU), 5.5 (O, SO), 5.6 (the generalized orthogonal groups O(n;k), here with $\eta$) (https://arxiv.org/abs/math-ph/0005032). Hall's route for each group: write the defining condition for $e^{sX}$; a condition on $X$ that makes it hold for all $s$ is sufficient; differentiating at $s = 0$ shows it is necessary. Hall settles the trace condition with "$s\operatorname{tr}X \in 2\pi i\mathbb Z$ for all $s$"; Step 2 differentiates instead.*
>
> **Step 1** ($GL(n, \mathbb C)$). Every $e^{sX}$ is invertible ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], 2), so $\mathfrak{gl}(n, \mathbb C) = M_n(\mathbb C)$, of real dimension $2n^2$.
>
> **Step 2** ($SL(n, \mathbb C)$). By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-3|Theorem §CB.1.3]], $\det e^{sX} = e^{s\operatorname{tr}X}$. If $\operatorname{tr}X = 0$ this is $1$ for all $s$. Conversely, if $e^{s\operatorname{tr}X} = 1$ for all $s$, differentiating at $s = 0$ gives $\operatorname{tr}X = 0$. One complex linear condition removes two real dimensions: $2n^2 - 2$.
>
> **Step 3** ($U(n)$). By Theorem §CB.1.2, 4, $(e^{sX})^\dagger = e^{sX^\dagger}$, so $e^{sX}$ is unitary iff $e^{sX^\dagger} = (e^{sX})^{-1} = e^{-sX}$. If $X^\dagger = -X$ this holds for all $s$. Conversely, if it holds for all $s$, differentiate at $s = 0$ (Theorem §CB.1.2, 5): $X^\dagger = -X$. Dimension: an anti-Hermitian matrix has imaginary diagonal ($n$ real parameters) and its strictly upper part ($n(n-1)/2$ complex entries) determines the lower part, $n + n(n - 1) = n^2$.
>
> **Step 4** ($SU(n)$). Steps 2 and 3 together. The trace of an anti-Hermitian matrix is imaginary, so $\operatorname{tr}X = 0$ is one real condition: $n^2 - 1$.
>
> **Step 5** ($O(n)$, $SO(n)$). If $e^{sX}$ is real for all $s$, then $X = \frac{d}{ds}e^{sX}|_0$ is real. For real $X$, $e^{sX}$ is orthogonal iff $e^{sX^{\mathsf T}} = e^{-sX}$; as in Step 3 this holds for all $s$ iff $X^{\mathsf T} = -X$. Such $X$ has zero diagonal, so $\operatorname{tr}X = 0$ and $\det e^{sX} = 1$: the same $X$ work for $SO(n)$. Dimension: the strictly upper entries, $n(n-1)/2$.
>
> **Step 6** ($O(1,3)$, $SO^+(1,3)$). $\Lambda \in O(1,3)$ iff $\Lambda^{\mathsf T}\eta\Lambda = \eta$ ([[§C1a.4 The Lorentz Group#^def-c1a-4-4|Def. §C1a.4.4]]). As in Step 5, $X$ is real. If $X^{\mathsf T}\eta + \eta X = 0$, then $X^{\mathsf T} = -\eta X\eta^{-1}$ ($\eta^2 = \mathbb 1$), so $(e^{sX})^{\mathsf T} = e^{sX^{\mathsf T}} = \eta e^{-sX}\eta^{-1}$ (Theorem §CB.1.2, 4), and $(e^{sX})^{\mathsf T}\eta e^{sX} = \eta e^{-sX}\eta^{-1}\eta e^{sX} = \eta$. Conversely, differentiating $(e^{sX})^{\mathsf T}\eta e^{sX} = \eta$ at $s = 0$ (product rule) gives $X^{\mathsf T}\eta + \eta X = 0$. For $SO^+(1,3)$: the condition says $\eta X$ is antisymmetric, so $(\eta X)_{\mu\mu} = \eta_{\mu\mu}X_{\mu\mu} = 0$, $\operatorname{tr}X = 0$ and $\det e^{sX} = 1$; and $s \mapsto (e^{sX})^0{}_0$ is continuous, equals $1$ at $s = 0$, and never lies in $(-1, 1)$ (every Lorentz matrix has $|\Lambda^0{}_0| \ge 1$, [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-4|REL Theorem §B1.2.4]]), so by the intermediate value theorem it stays $\ge 1$: $e^{sX}$ is orthochronous. So $O(1,3)$ and $SO^+(1,3)$ have the same algebra. Dimension: $X \mapsto \eta X$ is a bijection onto the real antisymmetric $4\times4$ matrices, $6$ parameters.
>
> **Step 7** ($SL(2, \mathbb C)$ as a real algebra). By Step 2, $\mathfrak{sl}(2, \mathbb C)$ is the traceless complex $2\times2$ matrices, real dimension $2\cdot4 - 2 = 6$, and $iX$ is traceless whenever $X$ is: closed under $i$, unlike $\mathfrak{su}(2)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], Step 3 of the proof).
>
> **What the proof shows.**
> - Each Lie algebra is the linearization of its group's defining equation at $\mathbb 1$; the dimensions match the manifold dimensions of [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]] (Theorem §CB.1.9, 2).
> - Discrete conditions (the sign of $\det$, orthochronicity) are invisible to the algebra: $O(n)$ and $SO(n)$, $O(1,3)$ and $SO^+(1,3)$ share their algebras → Theorem §CB.1.16.
> - Whether the algebra is closed under $i$ depends on the group, not on whether its matrices are complex: $\mathfrak{su}(2)$ is not, $\mathfrak{sl}(2, \mathbb C)$ is → [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-16|Def. §CB.2.16]].

^pf-cb-1-11

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-3|Theorem §CB.1.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], [[§C1a.4 The Lorentz Group#^def-c1a-4-4|Def. §C1a.4.4]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-4|REL Theorem §B1.2.4]]

The rotation case, proved in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1]]

## Homomorphisms and their differentials

> [!definition] Definition §CB.1.12: Lie Group Homomorphism
> A **Lie group homomorphism** between matrix Lie groups $G$ and $H$ is a continuous group homomorphism $\Phi : G \to H$ ([[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]). It is an **isomorphism of Lie groups** if it is bijective and $\Phi^{-1}$ is continuous.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 2 §6, Def. 2.13*

^def-cb-1-12

> [!definition] Definition §CB.1.13: Lie Algebra Homomorphism
> A **Lie algebra homomorphism** between real Lie algebras $\mathfrak g$ and $\mathfrak h$ ([[§49 Lie Bracket and Lie Algebra#^def-49-2|591 Def. §49.2]]) is a real-linear map $\varphi : \mathfrak g \to \mathfrak h$ with $\varphi([X, Y]) = [\varphi(X), \varphi(Y)]$ for all $X, Y$. A bijective one is an **isomorphism**, written $\mathfrak g \cong \mathfrak h$. (For complex Lie algebras, [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-1|Def. §CB.2.1]], the same words with complex-linear maps.)
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §8, Def. 3.29*

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
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §6, Thm. 3.18 (Steps 1–8 of its proof) · Woit, §5.4*

^thm-cb-1-14

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §6, Thm. 3.18 and its proof, Steps 1–8 (https://arxiv.org/abs/math-ph/0005032), followed step by step.*
>
> **Step 1** (definition of $\varphi$). Fix $X \in \mathfrak g$. Since $sX$ and $tX$ commute, $e^{(s+t)X} = e^{sX}e^{tX}$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], 3), and $\Phi$ is a continuous homomorphism; so $s \mapsto \Phi(e^{sX})$ is a one-parameter subgroup of $GL(n', \mathbb C)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-6|Def. §CB.1.6]]). By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-7|Theorem §CB.1.7]] there is a unique matrix $Z$ with $\Phi(e^{sX}) = e^{sZ}$ for all $s$, namely $Z = \frac{d}{ds}\Phi(e^{sX})|_{s=0}$. Since $e^{sZ} = \Phi(e^{sX}) \in H$ for all $s$, $Z \in \mathfrak h$. Define $\varphi(X) = Z$. Then
>
> $$
> \Phi(e^{sX}) = e^{s\varphi(X)} \quad (s \in \mathbb R), \qquad \varphi(X) = \frac{d}{ds}\Phi(e^{sX})\Big|_{s=0},
> $$
>
> and $s = 1$ gives $\Phi(e^X) = e^{\varphi(X)}$.
>
> **Step 2** (real homogeneity). For $a \in \mathbb R$: $\Phi(e^{s(aX)}) = \Phi(e^{(sa)X}) = e^{sa\varphi(X)} = e^{s(a\varphi(X))}$, so by uniqueness in Step 1, $\varphi(aX) = a\varphi(X)$.
>
> **Step 3** (additivity, by the Lie product formula). By Step 1, then [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], 1, then continuity and the homomorphism property of $\Phi$, then Step 1 again:
>
> $$
> e^{s\varphi(X + Y)} = \Phi\bigl(e^{s(X + Y)}\bigr) = \Phi\Bigl(\lim_{m\to\infty}\bigl(e^{sX/m}e^{sY/m}\bigr)^m\Bigr) = \lim_{m\to\infty}\bigl(\Phi(e^{sX/m})\Phi(e^{sY/m})\bigr)^m = \lim_{m\to\infty}\bigl(e^{s\varphi(X)/m}e^{s\varphi(Y)/m}\bigr)^m ,
> $$
>
> and the last limit is $e^{s(\varphi(X) + \varphi(Y))}$ by Theorem §CB.1.5, 1 once more. Differentiating $e^{s\varphi(X + Y)} = e^{s(\varphi(X) + \varphi(Y))}$ at $s = 0$ gives $\varphi(X + Y) = \varphi(X) + \varphi(Y)$. With Step 2, $\varphi$ is real-linear.
>
> **Step 4** (uniqueness of $\varphi$). If $\psi : \mathfrak g \to \mathfrak h$ is real-linear with $\Phi(e^X) = e^{\psi(X)}$ for all $X$, then $e^{s\psi(X)} = e^{\psi(sX)} = \Phi(e^{sX})$, and differentiating at $s = 0$ gives $\psi(X) = \frac{d}{ds}\Phi(e^{sX})|_0 = \varphi(X)$.
>
> **Step 5** (conjugation). For $g \in G$, $X \in \mathfrak g$: $gXg^{-1} \in \mathfrak g$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], 2), and by Step 1 and Theorem §CB.1.2, 4,
>
> $$
> e^{s\varphi(gXg^{-1})} = \Phi\bigl(e^{s\,gXg^{-1}}\bigr) = \Phi(g\,e^{sX}g^{-1}) = \Phi(g)\,e^{s\varphi(X)}\,\Phi(g)^{-1} = e^{s\,\Phi(g)\varphi(X)\Phi(g)^{-1}} .
> $$
>
> Differentiating at $s = 0$: $\varphi(gXg^{-1}) = \Phi(g)\varphi(X)\Phi(g)^{-1}$.
>
> **Step 6** (brackets). $[X, Y] = \frac{d}{dt}(e^{tX}Ye^{-tX})|_{t=0}$ (Step 5 of the proof of Theorem §CB.1.8), and the curve $t \mapsto e^{tX}Ye^{-tX}$ lies in $\mathfrak g$. A linear map on a finite-dimensional space is continuous, so it commutes with $\frac{d}{dt}$; using Step 5 with $g = e^{tX}$ and $\Phi(e^{tX}) = e^{t\varphi(X)}$:
>
> $$
> \varphi([X, Y]) = \frac{d}{dt}\varphi\bigl(e^{tX}Ye^{-tX}\bigr)\Big|_{t=0} = \frac{d}{dt}\Bigl(e^{t\varphi(X)}\varphi(Y)e^{-t\varphi(X)}\Bigr)\Big|_{t=0} = \varphi(X)\varphi(Y) - \varphi(Y)\varphi(X) .
> $$
>
> So $\varphi$ is a Lie algebra homomorphism ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-13|Def. §CB.1.13]]).
>
> **Step 7** (composition). For $\Psi : H \to K$: $(\Psi\circ\Phi)(e^{sX}) = \Psi(e^{s\Phi_\ast(X)}) = e^{s\Psi_\ast(\Phi_\ast(X))}$, so by uniqueness (Step 1 for $\Psi\circ\Phi$), $(\Psi\circ\Phi)_\ast = \Psi_\ast\circ\Phi_\ast$.
>
> **What the proof shows.**
> - Continuity of $\Phi$ is all that is assumed; Theorem §CB.1.7 supplies the derivatives. In the language of 591, $\varphi$ is the differential of $\Phi$ at $\mathbb 1$ (Step 1's formula).
> - ⚑ By-product: the structure constants of $\mathfrak h$ restricted to the image are those of $\mathfrak g$; for $H = GL(W)$ this is "every representation realizes the same algebra" ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]], whose derivation is the special case).
> - The converse, from algebra homomorphisms to group homomorphisms, needs connectedness for uniqueness (Theorem §CB.1.17) and simple connectivity for existence (Theorem §CB.1.24).

^pf-cb-1-14

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-6|Def. §CB.1.6]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-12|Def. §CB.1.12]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-13|Def. §CB.1.13]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-7|Theorem §CB.1.7]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]]

The case $H = GL(W)$, a representation, is the course's theorem, proved in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2]]

## The identity component

> [!definition] Definition §CB.1.15: Identity Component
> The **identity component** $G_0$ of a matrix Lie group $G$ is the set of $g \in G$ that can be joined to $\mathbb 1$ by a continuous path in $G$. $G$ is **connected** if $G_0 = G$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 2 §4, Def. 2.5, Prop. 2.6 · 591 §16*

^def-cb-1-15

> [!theorem] Theorem §CB.1.16: The Identity Component Is Generated by Exponentials
> Let $G$ be a matrix Lie group with Lie algebra $\mathfrak g$ and identity component $G_0$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-15|Def. §CB.1.15]]).
> 1. $G_0$ is a normal subgroup of $G$ ([[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]]), open and closed in $G$, and its cosets are the path components of $G$.
> 2. $e^X \in G_0$ for every $X \in \mathfrak g$.
> 3. Every $g \in G_0$ is a finite product $g = e^{X_1}e^{X_2}\cdots e^{X_k}$ with $X_i \in \mathfrak g$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 2 §4, Prop. 2.6; Ch. 3, Prop. 3.14, Cor. 3.26 · Lee, Introduction to Smooth Manifolds, Lemma 7.12, Prop. 7.15 · the Lorentz case: [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]]*

^thm-cb-1-16

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Prop. 2.6 (subgroup), Prop. 3.14 (part 2), Cor. 3.26 (part 3) with proofs (https://arxiv.org/abs/math-ph/0005032) · J. M. Lee, Introduction to Smooth Manifolds, 2nd ed., Lemma 7.12 and Prop. 7.15 (normal, open and closed, cosets as components), whose arguments Steps 2 and 4 follow.*
>
> **Step 1** (subgroup; Hall, Prop. 2.6). Let $g, h \in G_0$ with paths $a(t)$, $b(t)$ in $G$ from $\mathbb 1$ to $g$, $h$ ($0 \le t \le 1$). Multiplication and inversion of matrices are continuous, so $a(t)b(t)$ is a path in $G$ from $\mathbb 1$ to $gh$, and $a(t)^{-1}$ a path from $\mathbb 1$ to $g^{-1}$. So $gh, g^{-1} \in G_0$; and $\mathbb 1 \in G_0$ (constant path).
>
> **Step 2** (normal). For $k \in G$ and $g \in G_0$ with path $a(t)$, $ka(t)k^{-1}$ is a path in $G$ from $\mathbb 1$ to $kgk^{-1}$. So $kG_0k^{-1} \subset G_0$ ([[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]]).
>
> **Step 3** (part 2; Hall, Prop. 3.14). For $X \in \mathfrak g$, $s \mapsto e^{sX}$, $0 \le s \le 1$, is a continuous path in $G$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], 1, and the definition of $\mathfrak g$) from $\mathbb 1$ to $e^X$. So $e^X \in G_0$.
>
> **Step 4** (open and closed). By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]] there is a neighbourhood $V = \exp(U \cap \mathfrak g)$ of $\mathbb 1$, open in $G$, and $V \subset G_0$ by Step 3. Left multiplication by $k \in G$ is a homeomorphism of $G$ (continuous, with continuous inverse multiplication by $k^{-1}$), so $kV$ is open. For $g \in G_0$, $gV \subset G_0$ (Step 1) is an open set containing $g$: $G_0$ is open. Every coset $kG_0$ is open for the same reason. The cosets partition $G$, so $G \setminus G_0$ is the union of the cosets other than $G_0$, which is open: $G_0$ is closed.
>
> **Step 5** (cosets are the path components). $k' \in G$ can be joined to $k$ by a path $c(t)$ in $G$ iff $k^{-1}c(t)$ is a path from $\mathbb 1$ to $k^{-1}k'$, i.e. iff $k^{-1}k' \in G_0$, i.e. iff $k' \in kG_0$. So the path component of $k$ is $kG_0$.
>
> **Step 6** (part 3; Hall, Cor. 3.26). Let $E \subset G_0$ be the set of finite products $e^{X_1}\cdots e^{X_k}$, $X_i \in \mathfrak g$ ($E \subset G_0$ by Steps 1 and 3). $E \supset V \ni \mathbb 1$, so $E \ne \varnothing$. *$E$ is open:* for $A \in E$, $AV$ is an open neighbourhood of $A$, and each $Ae^X$ ($e^X \in V$) is again a finite product of exponentials. *$E$ is closed in $G_0$:* if $A \in G_0$ and $A_m \to A$ with $A_m \in E$, then $A_m^{-1}A \to \mathbb 1$, so $A_m^{-1}A \in V$ for some $m$, i.e. $A_m^{-1}A = e^X$ with $X \in \mathfrak g$, and $A = A_me^X \in E$. $G_0$ is path-connected (every point is joined to $\mathbb 1$), hence connected ([[§16 Connected Subspaces of ℝ#^thm-16-4|590 Thm. §16.4]]), so the nonempty open and closed subset $E$ is all of $G_0$ ([[§15 Connected Spaces#^def-15-2|590 Def. §15.2]]).
>
> **What the proof shows.**
> - $G/G_0$ is the group of components; for the Lorentz group it is $\{\pm1\}^2$ ([[§C1a.4 The Lorentz Group#^thm-c1a-4-2|Theorem §C1a.4.2]]), and no exponential leaves $G_0$: $P$ and $T$ are not of the form $e^X$.
> - ⚑ By-product: a single exponential need not suffice (for $SL(2, \mathbb R)$ some elements are not exponentials; Meinrenken, Exercise 4.18), which is why part 3 allows products; for $SO(3)$, $SU(2)$ and $SO^+(1,3)$ one or two factors are enough ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]]).
> - Used next: Theorems §CB.1.17 and §CB.1.23 check statements on exponentials and extend them to $G_0$ by part 3.

^pf-cb-1-16

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-15|Def. §CB.1.15]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]], [[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]], [[§16 Connected Subspaces of ℝ#^thm-16-4|590 Thm. §16.4]], [[§15 Connected Spaces#^def-15-2|590 Def. §15.2]]

The Lorentz group's components and its exponentials, proved in [[§C1a.4 The Lorentz Group|§C1a.4]] and [[§C1a.6 Infinitesimal Lorentz Transformations and Generators|§C1a.6]]:

![[§C1a.4 The Lorentz Group#^thm-c1a-4-3]]

![[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4]]

> [!theorem] Theorem §CB.1.17: A Homomorphism of a Connected Group Is Determined by Its Differential
> Let $G$ be connected and $\Phi, \Psi : G \to H$ Lie group homomorphisms with $\Phi_\ast = \Psi_\ast$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]]). Then $\Phi = \Psi$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 5 §8, Thm. 5.33, 1 (Step 1 of its proof)*

^thm-cb-1-17

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 5 §8, Thm. 5.33, part 1, Step 1 of the proof (https://arxiv.org/abs/math-ph/0005032).*
>
> **Step 1** (products of exponentials). $G$ is connected, so $G = G_0$, and every $g \in G$ is $g = e^{X_1}\cdots e^{X_k}$ with $X_i \in \mathfrak g$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]], 3).
>
> **Step 2** (apply both homomorphisms). By the homomorphism property and [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]],
>
> $$
> \Phi(g) = \Phi(e^{X_1})\cdots\Phi(e^{X_k}) = e^{\Phi_\ast(X_1)}\cdots e^{\Phi_\ast(X_k)} = e^{\Psi_\ast(X_1)}\cdots e^{\Psi_\ast(X_k)} = \Psi(e^{X_1})\cdots\Psi(e^{X_k}) = \Psi(g),
> $$
>
> the middle equality by $\Phi_\ast = \Psi_\ast$.
>
> **What the proof shows.**
> - Connectedness is essential: on $O(1,3)$ the identity map and $\Lambda \mapsto \det(\Lambda)\Lambda$ have the same differential but differ on $P$.
> - For $H = GL(W)$ this is the uniqueness half of "a representation of a connected group is fixed by its generators" ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]], 2).

^pf-cb-1-17

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]]

## The adjoint representation

591 defines the adjoint action for four classical groups:

![[§25 The Geometric Tangent Space#^def-25-2]]

> [!definition] Definition §CB.1.18: Adjoint Representation of a Group
> For a matrix Lie group $G$ with Lie algebra $\mathfrak g$, the **adjoint representation** is $\mathrm{Ad} : G \to GL(\mathfrak g)$, $\mathrm{Ad}_g(X) = gXg^{-1}$, a representation on the real vector space $\mathfrak g$ (well defined by [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], 2).
>
> *Source: 591 Def. §25.2, Prop. §25.6 · Hall, An Elementary Introduction to Groups and Representations, Ch. 3, Def. 3.19, Prop. 3.20*

^def-cb-1-18

> [!definition] Definition §CB.1.19: Adjoint Representation of a Lie Algebra
> For a Lie algebra $\mathfrak g$, $\mathrm{ad} : \mathfrak g \to \operatorname{End}(\mathfrak g)$ is $\mathrm{ad}_X(Y) = [X, Y]$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §8, Def. 3.32*

^def-cb-1-19

> [!theorem] Theorem §CB.1.20: The Differential of Ad Is ad
> 1. $\mathrm{ad}$ is a Lie algebra homomorphism $\mathfrak g \to \mathfrak{gl}(\mathfrak g)$: $\mathrm{ad}_{[X, Y]} = [\mathrm{ad}_X, \mathrm{ad}_Y]$ (the Jacobi identity).
> 2. $\mathrm{Ad}$ is a Lie group homomorphism and $\mathrm{Ad}_\ast = \mathrm{ad}$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]]).
> 3. $e^XYe^{-X} = e^{\mathrm{ad}_X}Y = Y + [X, Y] + \frac1{2!}[X, [X, Y]] + \cdots$ for $X, Y \in \mathfrak g$.
> 4. $\mathrm{Ad}_g[X, Y] = [\mathrm{Ad}_gX, \mathrm{Ad}_gY]$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3, Def. 3.19, Props. 3.20, 3.21, 3.33, eq. (3.17) · the Lorentz case: [[§C3.2 The Lorentz Algebra#^thm-c3-2-2|Theorem §C3.2.2]]*

^thm-cb-1-20

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3, Prop. 3.20 (Ad is a homomorphism), Prop. 3.21 (its differential), Prop. 3.33 (ad and Jacobi) and eq. (3.17) (Ad of an exponential) with proofs (https://arxiv.org/abs/math-ph/0005032).*
>
> **Step 1** (part 1; Hall, Prop. 3.33). For $Z \in \mathfrak g$: $\mathrm{ad}_{[X, Y]}Z = [[X, Y], Z]$ and $[\mathrm{ad}_X, \mathrm{ad}_Y]Z = [X, [Y, Z]] - [Y, [X, Z]]$. Their difference is $[[X, Y], Z] - [X, [Y, Z]] + [Y, [X, Z]] = -\bigl([X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]]\bigr)$ (using $[[X, Y], Z] = -[Z, [X, Y]]$ and $[Y, [X, Z]] = -[Y, [Z, X]]$), which is $0$ by the Jacobi identity ([[§49 Lie Bracket and Lie Algebra#^def-49-2|591 Def. §49.2]]). $\mathrm{ad}$ is linear because the bracket is bilinear.
>
> **Step 2** (Ad is a Lie group homomorphism; Hall, Prop. 3.20). $\mathrm{Ad}_g$ maps $\mathfrak g$ to itself ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], 2) and is real-linear. $\mathrm{Ad}_{gh}X = ghXh^{-1}g^{-1} = \mathrm{Ad}_g(\mathrm{Ad}_hX)$ and $\mathrm{Ad}_{\mathbb 1} = \mathrm{id}$, so $\mathrm{Ad}_{g^{-1}}$ inverts $\mathrm{Ad}_g$ and $\mathrm{Ad} : G \to GL(\mathfrak g)$ is a group homomorphism. Choosing a basis of $\mathfrak g$ identifies $GL(\mathfrak g)$ with $GL(k, \mathbb R)$, $k = \dim\mathfrak g$, a matrix Lie group; the matrix entries of $\mathrm{Ad}_g$ are linear combinations of the entries of $gX_ag^{-1}$, continuous in $g$. So $\mathrm{Ad}$ is a Lie group homomorphism ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-12|Def. §CB.1.12]]), and the Lie algebra of $GL(\mathfrak g)$ is $\mathfrak{gl}(\mathfrak g) = \operatorname{End}(\mathfrak g)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]], first row, over $\mathbb R$).
>
> **Step 3** (part 2: the differential; Hall, Prop. 3.21). By the formula of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]], for $X, Y \in \mathfrak g$,
>
> $$
> \mathrm{Ad}_\ast(X)\,Y = \frac{d}{dt}\mathrm{Ad}_{e^{tX}}(Y)\Big|_{t=0} = \frac{d}{dt}\bigl(e^{tX}Ye^{-tX}\bigr)\Big|_{t=0} = XY - YX = \mathrm{ad}_X(Y),
> $$
>
> the derivative computed as in Step 5 of the proof of Theorem §CB.1.8 (evaluation at $Y$ is linear, so it commutes with $d/dt$).
>
> **Step 4** (part 3; Hall, eq. (3.17)). Theorem §CB.1.14 applied to $\Phi = \mathrm{Ad}$ gives $\mathrm{Ad}(e^X) = e^{\mathrm{Ad}_\ast(X)} = e^{\mathrm{ad}_X}$, an identity between operators on $\mathfrak g$. Apply both sides to $Y$ and expand the exponential series of the operator $\mathrm{ad}_X$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]] on $\operatorname{End}(\mathfrak g)$):
>
> $$
> e^XYe^{-X} = e^{\mathrm{ad}_X}Y = \sum_{k\ge0}\frac{(\mathrm{ad}_X)^kY}{k!} = Y + [X, Y] + \frac1{2!}[X, [X, Y]] + \frac1{3!}[X, [X, [X, Y]]] + \cdots .
> $$
>
> **Step 5** (part 4). $\mathrm{Ad}_g[X, Y] = g(XY - YX)g^{-1} = (gXg^{-1})(gYg^{-1}) - (gYg^{-1})(gXg^{-1}) = [\mathrm{Ad}_gX, \mathrm{Ad}_gY]$, inserting $g^{-1}g = \mathbb 1$ between the factors.
>
> **What the proof shows.**
> - Part 3 expresses a finite conjugation through brackets alone; this is how the generators of any representation transform as a tensor ([[§C3.2 The Lorentz Algebra#^thm-c3-2-2|Theorem §C3.2.2]]).
> - ⚑ By-product: the Jacobi identity is not an extra axiom here: it is the statement that $\mathrm{ad}$ preserves brackets (Step 1), the infinitesimal form of Step 5.

^pf-cb-1-20

*Uses:* [[§49 Lie Bracket and Lie Algebra#^def-49-2|591 Def. §49.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-12|Def. §CB.1.12]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]]

## Coverings and the Lie correspondence

Simple connectivity and covering maps, defined in Topology (590):

![[§29 The Fundamental Group#^def-29-3]]

![[§31 Covering Spaces#^def-31-2]]

> [!definition] Definition §CB.1.21: Universal Covering Group
> A **universal covering group** of a connected matrix Lie group $G$ is a simply connected ([[§29 The Fundamental Group#^def-29-3|590 Def. §29.3]]) matrix Lie group $\tilde G$ with a Lie group homomorphism $p : \tilde G \to G$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-12|Def. §CB.1.12]]) that is a covering map ([[§31 Covering Spaces#^def-31-2|590 Def. §31.2]]).
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 5 §9, Def. 5.36 (there: connected, simply connected, surjective, a local homeomorphism at the identity) · the examples: [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]*

^def-cb-1-21

> [!theorem] Theorem §CB.1.22: Discrete Normal Subgroups of Connected Groups Are Central
> If $G$ is a connected matrix Lie group and $N \subset G$ a normal subgroup that is discrete (each point of $N$ is isolated in $N$), then $N$ lies in the centre of $G$: $ng = gn$ for all $n \in N$, $g \in G$.
>
> *Source: Meinrenken, Lie Groups and Lie Algebras, §2.5, end of the proof of Thm. 2.13*

^thm-cb-1-22

> [!proof]- Proof
> *Source: E. Meinrenken, Lie Groups and Lie Algebras, lecture notes (Toronto, Winter 2026), §2.5, last paragraph of the proof of Thm. 2.13: "if G is connected … the adjoint action must be trivial on π₁(G) (since π₁(G) is discrete)" (https://www.math.toronto.edu/mein/teaching/LectureNotes/lie.pdf); the one-line argument is written out here.*
>
> **Step 1** (a map into $N$). Fix $n \in N$ and define $f : G \to G$, $f(g) = gng^{-1}$. It is continuous (matrix multiplication and inversion are), $f(\mathbb 1) = n$, and $f(G) \subset N$ because $N$ is normal ([[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]]).
>
> **Step 2** (the level set is open). Let $S = f^{-1}(n) = \{g : gng^{-1} = n\}$. If $g_0 \in S$, choose an open $W \subset G$ with $W \cap N = \{n\}$ ($n$ is isolated in $N$). Then $f^{-1}(W)$ is an open neighbourhood of $g_0$, and $f$ maps it into $W \cap N = \{n\}$; so $f^{-1}(W) \subset S$.
>
> **Step 3** (the level set is closed). $S$ is the preimage of the closed set $\{n\}$ under the continuous $f$.
>
> **Step 4** (connectedness). $G$ is connected (path-connected, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-15|Def. §CB.1.15]], hence connected, [[§16 Connected Subspaces of ℝ#^thm-16-4|590 Thm. §16.4]]), and $S$ is nonempty ($\mathbb 1 \in S$), open and closed; so $S = G$ ([[§15 Connected Spaces#^def-15-2|590 Def. §15.2]]). That is, $gng^{-1} = n$, i.e. $gn = ng$, for every $g \in G$.
>
> **What the proof shows.**
> - Applied to kernels of coverings: $\ker(SU(2) \to SO(3)) = \{\pm\mathbb 1\}$ and $\ker(SL(2, \mathbb C) \to SO^+(1,3)) = \{\pm\mathbb 1\}$ are central, as they must be (Theorem §CB.1.23).
> - Discreteness is essential: $SO^+(1,3)$ is a normal subgroup of the connected $SO^+(1,3)$ that is not central.

^pf-cb-1-22

*Uses:* [[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-15|Def. §CB.1.15]], [[§16 Connected Subspaces of ℝ#^thm-16-4|590 Thm. §16.4]], [[§15 Connected Spaces#^def-15-2|590 Def. §15.2]]

> [!theorem] Theorem §CB.1.23: Homomorphisms with Invertible Differential Are Coverings
> Let $\Phi : G \to H$ be a Lie group homomorphism of connected matrix Lie groups whose differential $\Phi_\ast$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]]) is a Lie algebra isomorphism. Then $\Phi$ is surjective, $\ker\Phi$ is a discrete central subgroup of $G$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-22|Theorem §CB.1.22]]), $\Phi$ is a covering map, and $H \cong G/\ker\Phi$ as groups ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]) and homeomorphically.
>
> *Source: Z. Wang, Lie Groups (USTC), Lecture 12, Lemma 1.1 · Lee, Introduction to Smooth Manifolds, Thm. 21.31 · Etingof, Lie Groups and Lie Algebras, Prop. 3.15 (ii) · instances: [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], Theorem §CB.9.12*

^thm-cb-1-23

> [!proof]- Proof
> *Source: Zuoqin Wang, Lie Groups (USTC, Fall 2013), Lecture 12 "Lie's fundamental theorems", Lemma 1.1 and its proof (http://staff.ustc.edu.cn/~wangzuoq/Courses/13F-Lie/Notes/Lec%2012.pdf), for Steps 3–5 · P. Etingof, Lie Groups and Lie Algebras (MIT 18.755 notes, 2024), Prop. 3.15 (ii) (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), for Step 2 · J. M. Lee, Introduction to Smooth Manifolds, 2nd ed., Thm. 21.31 ((d) ⇒ (c) ⇒ (a) ⇒ (b)), the same theorem for general Lie groups. The local homeomorphism (Step 1) is obtained from the exponential charts of Theorem §CB.1.10 instead of the inverse function theorem.*
>
> **Step 1** ($\Phi$ is a homeomorphism near $\mathbb 1$). By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]] for $G$ and for $H$ there are neighbourhoods $U_G$, $U_H$ of $0$ such that $\exp$ maps $U_G \cap \mathfrak g$ homeomorphically onto an open neighbourhood of $\mathbb 1$ in $G$, and likewise for $H$. Put $\varphi = \Phi_\ast$, a linear isomorphism $\mathfrak g \to \mathfrak h$, hence a homeomorphism. Choose an open $W \ni 0$ in $\mathfrak g$ with $W \subset U_G$ and $\varphi(W) \subset U_H$. Then $V = \exp(W)$ is open in $G$, $V' = \exp(\varphi(W))$ is open in $H$, and on $V$, by [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]],
>
> $$
> \Phi(e^X) = e^{\varphi(X)}, \qquad\text{i.e.}\qquad \Phi|_V = \exp_H\circ\varphi\circ(\exp_G|_W)^{-1} : V \to V',
> $$
>
> a composition of three homeomorphisms. So $\Phi$ maps $V$ homeomorphically onto $V'$.
>
> **Step 2** (surjective; Etingof, Prop. 3.15 (ii)). $H$ is connected, so every $h \in H$ is $e^{Y_1}\cdots e^{Y_k}$ with $Y_i \in \mathfrak h$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]], 3). For each $Y_i$, $e^{Y_i/m} \to \mathbb 1$ as $m \to \infty$, so $e^{Y_i/m} \in V' \subset \Phi(G)$ for some $m$, and $e^{Y_i} = (e^{Y_i/m})^m \in \Phi(G)$ ($\Phi(G)$ is a subgroup). Hence $h \in \Phi(G)$.
>
> **Step 3** (the kernel is discrete and central). Let $\Gamma = \ker\Phi$, a normal subgroup ([[§15 Homomorphisms#^def-15-3|493 Def. §15.3]], [[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]]). $\Phi$ is injective on $V$ and $\Phi(\mathbb 1) = \mathbb 1$, so $\Gamma \cap V = \{\mathbb 1\}$. For $a \in \Gamma$, $aV$ is an open neighbourhood of $a$ (left multiplication is a homeomorphism) and $aV \cap \Gamma = a(V \cap a^{-1}\Gamma) = a(V \cap \Gamma) = \{a\}$: every point of $\Gamma$ is isolated. By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-22|Theorem §CB.1.22]] ($G$ connected), $\Gamma$ is central.
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
> - Combined with simple connectivity of $G$, this identifies $G$ as the universal covering group ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-21|Def. §CB.1.21]]).

^pf-cb-1-23

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-22|Theorem §CB.1.22]], [[§15 Homomorphisms#^def-15-3|493 Def. §15.3]], [[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]], [[§31 Covering Spaces#^def-31-2|590 Def. §31.2]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]

> [!theorem] Theorem §CB.1.24: The Lie Correspondence for Simply Connected Groups
> Let $G$ be a simply connected matrix Lie group ([[§29 The Fundamental Group#^def-29-3|590 Def. §29.3]]), $H$ a matrix Lie group, and $\varphi : \mathfrak g \to \mathfrak h$ a Lie algebra homomorphism ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-13|Def. §CB.1.13]]). Then there is a unique Lie group homomorphism $\Phi : G \to H$ with $\Phi_\ast = \varphi$. In particular, with $H = GL(W)$: every finite-dimensional representation of $\mathfrak g$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-6|Def. §C3.1.6]]) is the differential of a unique representation of $G$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 5 §8, Thm. 5.33, 2, Cor. 5.35 (proof not reproduced; see the proof callout) · used for SU(2) in [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]] and for SL(2,ℂ) in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]*

^thm-cb-1-24

> [!proof]- Proof (to be filled)
> *Decision (SPEC-CB, item 7): stated here; the proof (via the Baker–Campbell–Hausdorff formula locally and path lifting, [[§32 Lifting and the Fundamental Group of the Circle#^lem-32-1|590 Lemma §32.1]], globally) is to be filled, or linked to 591 once the course proves it. Uniqueness is Theorem §CB.1.17; only existence is open.*

^pf-cb-1-24

<!-- searched (2026-10-08): Hall, An Elementary Introduction to Groups and Representations (arXiv:math-ph/0005032), Thm. 5.33 (2): proof rests on the BCH integral formula (Thm. 4.3, Cor. 4.4, proved over several pages) and on homotopy steps left as "a standard topological argument"; Meinrenken, Lie Groups and Lie Algebras (Toronto 2026), Thm. 7.8 and Etingof, Lie Groups and Lie Algebras (MIT 18.755), Thm. 9.12 / §10.2.2, and Z. Wang (USTC) Lecture 12, Thm. 1.3: all via the graph subgroup and integration of subalgebras (Frobenius theorem); Lee, Introduction to Smooth Manifolds, Thm. 20.19: same route. No self-contained matrix-group proof that fits CB.1 without first developing BCH or Frobenius; placeholder kept per SPEC-CB decision 7. -->

> [!remark] Remark: Why the algebra is not enough, and what simple connectivity adds
> Theorem §CB.1.17 says that the algebra determines a homomorphism of a *connected* group; Theorem §CB.1.24 says that every algebra homomorphism comes from a group homomorphism only when the group is *simply connected*. The gap between the two is the fundamental group: SO(3) and SU(2) have the same algebra ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]]), but spin ½ integrates only to SU(2) ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|Theorem §C3.1.8]]). Spinor representations are this gap made visible (§CB.9).

^rem-cb-1-1

> [!remark]- Connections
> - The real Lie algebra of Theorem §CB.1.8 is the reason for [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification|§CB.2]]: the physicists' Hermitian generators and the ladder combinations $J^\pm$, $\mathbf J_\pm$ live outside $\mathfrak g$, in $i\mathfrak g$ and in the complexification.
> - Theorem §CB.1.23 is the common shape of SU(2) → SO(3) ([[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]), SL(2,ℂ) → SO⁺(1,3) ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]) and Spin(V) → SO(V) (§CB.9).
> - **Used in**: Definition §CB.1.1–Theorem §CB.1.3 — the exponentials of rotations and boosts and their determinants ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]]), the finite quantum Poincaré transformations ([[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-3|Theorem §C3.5.3]]); Theorem §CB.1.5 — two boosts make a rotation ([[§C3.2 The Lorentz Algebra#^rem-c3-2-2|§C3.2, Remark: Two boosts make a rotation]]); Theorems §CB.1.8–§CB.1.11 — the course's Lie algebras ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3|Def. §C3.1.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]], [[§C1a.4 The Lorentz Group#^def-c1a-4-4|Def. §C1a.4.4]]); Theorem §CB.1.14 — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]], [[§C3.2 The Lorentz Algebra#^def-c3-2-1|Def. §C3.2.1]]; Theorem §CB.1.16 — [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]] (step 5); Theorem §CB.1.20 — the generators transform as a tensor ([[§C3.2 The Lorentz Algebra#^thm-c3-2-2|Theorem §C3.2.2]]), how the quantum generators transform ([[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-4|Theorem §C3.5.4]]); Theorems §CB.1.22–§CB.1.24 — integration of spin $j$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]]), the double covers ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]), integer $(j_+, j_-)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]).
