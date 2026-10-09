---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.15
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)]] →

*Sources: P. Woit, Quantum Theory, Groups and Representations, §40.4 ("Spin and the Lorentz group": four-vectors as $x^0 + \mathbf x\cdot\boldsymbol\sigma$ and the action $\Omega(\cdot)\Omega^\dagger$) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · through the course homes embedded below: the user's PHY 513 notes, Ch. 7 §7.4, Ch. 8 §8.2; PHY 513 Lecture 7; Yu Zhao-Huan, 量子场论讲义, Exercise 3.7; Peskin & Schroeder, §3.1–§3.2 · the Clifford route and the comparison of conventions written here · for the complexification of real 𝔰𝔩(2,ℂ) and its representations: P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, Exercise 11.4, Remark 17.3 (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf) · P. Woit, Quantum Theory, Groups and Representations, §5.5 · the explicit map and the proof of the second theorem written here.*

What is the spin group of Minkowski space? The course reaches $SL(2, \mathbb C)$ through Hermitian $2\times2$ matrices ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]]–[[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-7|Theorem §CB.15.7]]) and the representations $(j_+, j_-)$ through the complexified algebra ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]). The course's route, with its proofs, is stated here first (the covering map, its kernel and the double cover), and the Clifford route is identified with it in Theorem §CB.15.9. Before both, this section complexifies the real Lie algebra $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ (two copies of $\mathfrak{sl}(2, \mathbb C)$) and splits its representations into a complex-linear and an antilinear part; then it gives the Clifford route: $\mathrm{Cl}^0(1,3) \cong \mathrm{Cl}(3,0) \cong M_2(\mathbb C)$, so $\mathrm{Spin}(1,3)_0 \cong SL(2, \mathbb C)$, with $\rho$ the course's covering map up to the automorphism $\lambda \mapsto (\lambda^\dagger)^{-1}$. The finite-dimensional representations of $SL(2, \mathbb C)$ (pairs of $\mathfrak{sl}(2, \mathbb C)$-representations, the $(j_+, j_-)$, and which of them descend to $SO^+(1,3)$) follow in [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)|§CB.16]]. It is the four-dimensional sequel of [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half|§CB.14]], using [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification|§CB.3]]–[[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra|§CB.5]] (real forms, $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$) and [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.13]].

## The complexification of real 𝔰𝔩(2,ℂ) and its representations

> [!theorem] Theorem §CB.15.1: The Complexification of Real 𝔰𝔩(2,ℂ) Is Two Copies of 𝔰𝔩(2,ℂ)
> The map $\Phi : (\mathfrak{sl}(2, \mathbb C)_{\mathbb R})_{\mathbb C} \to \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$,
>
> $$
> \Phi(X + iY) = \bigl(X + iY,\ \bar X + i\bar Y\bigr) \qquad (X, Y \in \mathfrak{sl}(2, \mathbb C)_{\mathbb R};\ \bar X \text{ the entrywise conjugate}),
> $$
>
> is an isomorphism of complex Lie algebras. So the complexification of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ has complex dimension $6$ and is not $\mathfrak{sl}(2, \mathbb C)$; on the real algebra, $X \mapsto (X, \bar X)$.
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), Exercise 11.4 and Remark 17.3 ($\mathfrak g_{\mathbb C} \cong \mathfrak g\oplus\mathfrak g$ for a complex $\mathfrak g$ regarded as real) · Woit, §5.5 ($\mathfrak{gl}(n, \mathbb C)_{\mathbb C}$ is "built out of two copies") · the explicit map written here*

^thm-cb-15-1

> [!proof]- Proof
> *Source: P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, Exercise 11.4 ("Let $\mathfrak g$ be a complex Lie algebra. Show that $\mathfrak g_{\mathbb C} \cong \mathfrak g\oplus\mathfrak g$") and Remark 17.3 (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf); P. Woit, §5.5, on $\mathfrak{gl}(n, \mathbb C)_{\mathbb C}$ (https://www.math.columbia.edu/~woit/QM/qmbook.pdf). Etingof's statement is an exercise; the solution with the explicit map of the theorem (the second copy written with the conjugate matrix) is written here.*
>
> **Step 1** (what the symbols mean). An element of $(\mathfrak{sl}(2, \mathbb C)_{\mathbb R})_{\mathbb C}$ is a formal $X + iY$ with $X, Y$ traceless complex matrices ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-2|Def. §CB.3.2]]); the $i$ here is the new one, not the matrix scalar. In each component of $\Phi(X + iY)$, "$X + iY$" and "$\bar X + i\bar Y$" are computed with matrix operations, and both are traceless.
>
> **Step 2** (complex-linear). $\Phi$ is real-linear, and with $i(X + iY) = -Y + iX$:
>
> $$
> \Phi(-Y + iX) = \bigl(-Y + iX,\ -\bar Y + i\bar X\bigr) = i\bigl(X + iY,\ \bar X + i\bar Y\bigr) .
> $$
>
> **Step 3** (brackets). On the real algebra, $\Phi(X) = (X, \bar X)$ preserves brackets: $[X, X'] \mapsto ([X, X'], \overline{[X, X']}) = ([X, X'], [\bar X, \bar X'])$, entrywise conjugation being multiplicative. $\Phi$ is the complex-linear extension of this real Lie algebra homomorphism into the complex Lie algebra $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$, and such an extension preserves brackets by the four-term expansion of Step 2 of the proof of [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-9|Theorem §CB.3.9]] (with $d$ replaced by $X \mapsto (X, \bar X)$).
>
> **Step 4** (injective). If $\Phi(X + iY) = 0$, then $X + iY = 0$ and $\bar X + i\bar Y = 0$ as matrices. Conjugating the second entrywise, $X - iY = 0$. Adding and subtracting: $X = 0$, $Y = 0$.
>
> **Step 5** (bijective). $\dim_{\mathbb C}(\mathfrak{sl}(2, \mathbb C)_{\mathbb R})_{\mathbb C} = \dim_{\mathbb R}\mathfrak{sl}(2, \mathbb C)_{\mathbb R} = 6$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]]; [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^def-cb-5-7|Def. §CB.5.7]]) $= \dim_{\mathbb C}(\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C))$, so the injective linear $\Phi$ is bijective: an isomorphism of complex Lie algebras. In particular the complexification has complex dimension $6$ and is not $\mathfrak{sl}(2, \mathbb C)$ (dimension $3$).
>
> **What the proof shows.**
> - ⚑ By-product: "complexify by allowing complex coefficients" fails for an algebra already closed under $i$; the abstract $i$ and the matrix $i$ are different, and the second copy carries the conjugate matrices. This is the algebraic origin of the conjugate representation $\Lambda \mapsto \bar\Lambda$ of $SL(2, \mathbb C)$ (Theorem §CB.15.2).
> - Composed with Theorem §CB.5.8, this gives $\mathfrak{so}(1,3)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ once more, consistently with Theorem §CB.5.1.

^pf-cb-15-1

*Uses:* [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-2|Def. §CB.3.2]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^def-cb-5-7|Def. §CB.5.7]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-9|Theorem §CB.3.9]]

> [!theorem] Theorem §CB.15.2: Representations of Real 𝔰𝔩(2,ℂ): a Complex-Linear and an Antilinear Part
> Let $\rho : \mathfrak{sl}(2, \mathbb C)_{\mathbb R} \to \operatorname{End}_{\mathbb C}(W)$ be a representation on a complex vector space $W$. There are unique maps $\rho_1$, $\rho_2$ with $\rho = \rho_1 + \rho_2$, $\rho_1$ complex-linear and $\rho_2$ complex-antilinear ($\rho_2(iX) = -i\rho_2(X)$), both Lie algebra homomorphisms, and $[\rho_1(X), \rho_2(Y)] = 0$ for all $X, Y$. Conversely every such commuting pair gives a representation. The defining representation $X \mapsto X$ on $\mathbb C^2$ has $\rho_2 = 0$; its complex conjugate $X \mapsto \bar X$ has $\rho_1 = 0$.
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), Exercise 11.4 ("$\mathrm{Rep}_{\mathbb R}G \cong \mathrm{Rep}(\mathfrak g\oplus\mathfrak g)$" for a complex $G$ regarded as real) · written here (from Theorem §CB.15.1 and Theorem §CB.3.9)*

^thm-cb-15-2

> [!proof]- Proof
> *Written here from Theorems §CB.3.9 and §CB.15.1; it is the Lie-algebra half of P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, Exercise 11.4, second sentence (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), which is stated there without proof.*
>
> **Step 1** (pass to two copies). Extend $\rho$ complex-linearly to $\rho_{\mathbb C}$ on $(\mathfrak{sl}(2, \mathbb C)_{\mathbb R})_{\mathbb C}$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-9|Theorem §CB.3.9]]) and set $\sigma = \rho_{\mathbb C}\circ\Phi^{-1}$ with $\Phi$ of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-1|Theorem §CB.15.1]]: a complex-linear representation of $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ on $W$. Put $\sigma_1(A) = \sigma(A, 0)$, $\sigma_2(B) = \sigma(0, B)$. Both are complex-linear representations of $\mathfrak{sl}(2, \mathbb C)$, and they commute: $[\sigma_1(A), \sigma_2(B)] = \sigma([(A, 0), (0, B)]) = \sigma(0) = 0$.
>
> **Step 2** (existence). For $X$ in the real algebra, $\Phi(X) = (X, \bar X) = (X, 0) + (0, \bar X)$, so $\rho(X) = \rho_{\mathbb C}(X) = \sigma_1(X) + \sigma_2(\bar X)$. Put $\rho_1(X) = \sigma_1(X)$ and $\rho_2(X) = \sigma_2(\bar X)$. Then $\rho_1$ is complex-linear; $\rho_2(iX) = \sigma_2(\overline{iX}) = \sigma_2(-i\bar X) = -i\rho_2(X)$ is antilinear; both preserve brackets (for $\rho_2$ because $\overline{[X, Y]} = [\bar X, \bar Y]$); and they commute by Step 1.
>
> **Step 3** (uniqueness). If $\rho = \rho_1 + \rho_2$ with $\rho_1$ complex-linear and $\rho_2$ antilinear, then $\rho(iX) = i\rho_1(X) - i\rho_2(X)$, so $-i\rho(iX) = \rho_1(X) - \rho_2(X)$ and
>
> $$
> \rho_1(X) = \tfrac12\bigl(\rho(X) - i\rho(iX)\bigr), \qquad \rho_2(X) = \tfrac12\bigl(\rho(X) + i\rho(iX)\bigr):
> $$
>
> both are determined by $\rho$.
>
> **Step 4** (converse). If $\rho_1$, $\rho_2$ are bracket-preserving, complex-linear resp. antilinear, and $[\rho_1(X), \rho_2(Y)] = 0$ for all $X, Y$, then $\rho = \rho_1 + \rho_2$ is real-linear and, expanding all four terms and dropping the two mixed ones,
>
> $$
> [\rho(X), \rho(Y)] = [\rho_1X, \rho_1Y] + [\rho_1X, \rho_2Y] + [\rho_2X, \rho_1Y] + [\rho_2X, \rho_2Y] = \rho_1[X, Y] + \rho_2[X, Y] = \rho([X, Y]) .
> $$
>
> **Step 5** (the two examples). For $\rho(X) = X$: $\rho(iX) = iX$, so Step 3 gives $\rho_2(X) = \frac12(X + i\cdot iX) = 0$. For $\rho(X) = \bar X$: $\rho(iX) = -i\bar X$, so $\rho_1(X) = \frac12(\bar X - i(-i\bar X)) = \frac12(\bar X - \bar X) = 0$.
>
> **What the proof shows.**
> - ⚑ By-product: a representation of $SL(2, \mathbb C)$ regarded as a real group is labelled by two complex-linear pieces, one "holomorphic", one "antiholomorphic"; through Theorem §CB.5.8 these become the two commuting angular momenta behind the labels $(j_+, j_-)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-7|Theorem §CB.16.7]]; which of the defining representation and its conjugate is called $(\frac12, 0)$ is a convention fixed there).
> - The decomposition needs $W$ complex; antilinearity of $\rho_2$ is relative to the complex structure of $\mathfrak{sl}(2, \mathbb C)$, not of $W$.

^pf-cb-15-2

*Uses:* [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-9|Theorem §CB.3.9]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-1|Theorem §CB.15.1]]

## Four-vectors as Hermitian matrices

The course reaches $SL(2, \mathbb C) \to SO^+(1,3)$ without the Clifford algebra, through four-vectors as Hermitian $2\times2$ matrices (PHY 513 Lecture 8, Part C; Yu, Exercise 3.7; the user's PHY 513 notes, Ch. 8 §8.2; first written in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]). Both routes are kept; Theorem §CB.15.9 below identifies them.

> [!theorem] Theorem §CB.15.3: Four-Vectors as Hermitian Matrices
> 1. $x \mapsto X = x_\mu\sigma^\mu$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-20|Def. §CB.0.20]]) is a real-linear bijection from $\mathbb R^4$ onto the Hermitian $2\times2$ matrices, with inverse $x^\nu = \frac12\operatorname{tr}(X\bar\sigma^\nu)$, and
>
> $$
> X = \begin{pmatrix} x^0 - x^3 & -x^1 + ix^2 \\ -x^1 - ix^2 & x^0 + x^3 \end{pmatrix}, \qquad \det X = x_\mu x^\mu .
> $$
>
> 2. Likewise $x \mapsto \bar X = x_\mu\bar\sigma^\mu$, with inverse $x^\nu = \frac12\operatorname{tr}(\bar X\sigma^\nu)$ and $\det\bar X = x_\mu x^\mu$.
> 3. $x^0 = \frac12\operatorname{tr}X$, and $x$ is future-directed timelike or null ($x^2 \ge 0$, $x^0 > 0$) iff $X$ is positive semidefinite and nonzero.
>
> *Source: Yu Exercise 3.7, eqs. (3.259)–(3.260) · the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit", part (a)) · part 3 written out here*

^thm-cb-15-3

> [!derivation]- Derivation
> **1. The matrix.** $X = x_0\mathbb 1 + x_i\sigma^i$ with $x_0 = x^0$, $x_i = -x^i$, i.e. $X = x^0\mathbb 1 - x^1\sigma^1 - x^2\sigma^2 - x^3\sigma^3$. Inserting $\sigma^1 = \begin{pmatrix}0&1\\1&0\end{pmatrix}$, $\sigma^2 = \begin{pmatrix}0&-i\\i&0\end{pmatrix}$, $\sigma^3 = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$: the diagonal is $x^0 \mp x^3$; the upper-right entry is $-x^1 - x^2(-i) = -x^1 + ix^2$; the lower-left is $-x^1 - x^2(i) = -x^1 - ix^2$. The two off-diagonal entries are complex conjugates and the diagonal is real: $X$ is Hermitian.
>
> **2. Onto, and the inverse.** Every Hermitian $2\times2$ matrix is $a_0\mathbb 1 + \mathbf a\cdot\boldsymbol\sigma$ with real $a_0, \mathbf a$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], part 4); it is $X$ for $x^0 = a_0$, $\mathbf x = -\mathbf a$. For the inverse, multiply $X = x_\mu\sigma^\mu$ by $\bar\sigma^\nu$ and take the trace: $\operatorname{tr}(X\bar\sigma^\nu) = x_\mu\operatorname{tr}(\sigma^\mu\bar\sigma^\nu) = 2x_\mu g^{\mu\nu} = 2x^\nu$ (Theorem §CB.0.22, 1). So $x$ is recovered from $X$, and the map is injective.
>
> **3. Determinant.** From step 1, $\det X = (x^0 - x^3)(x^0 + x^3) - (-x^1 + ix^2)(-x^1 - ix^2) = (x^0)^2 - (x^3)^2 - \bigl((x^1)^2 + (x^2)^2\bigr) = x_\mu x^\mu$, using $(-x^1 + ix^2)(-x^1 - ix^2) = (x^1)^2 - (ix^2)^2 = (x^1)^2 + (x^2)^2$.
>
> **4. Part 2.** $\bar X = x^0\mathbb 1 + \mathbf x\cdot\boldsymbol\sigma$ is $X$ with $\mathbf x \to -\mathbf x$, so it is Hermitian, the map is onto by the same argument, and $\det\bar X = (x^0)^2 - \mathbf x^2$. The inverse uses $\operatorname{tr}(\bar\sigma^\mu\sigma^\nu) = 2g^{\mu\nu}$, which follows from Theorem §CB.0.22, 1 by cyclicity of the trace.
>
> **5. Part 3.** $\operatorname{tr}X = 2x^0$ (the $\sigma^i$ are traceless). The eigenvalues $\lambda_\pm$ of the Hermitian $X$ are real with $\lambda_+ + \lambda_- = 2x^0$ and $\lambda_+\lambda_- = \det X = x^2$. Both are $\ge 0$ and not both $0$ iff the product is $\ge 0$ and the sum is $> 0$, i.e. iff $x^2 \ge 0$ and $x^0 > 0$.
>
> **What the derivation shows**
> - The Minkowski interval is a determinant, and the forward light cone is the cone of positive semidefinite matrices. Any operation on $X$ that preserves Hermiticity and the determinant therefore preserves the interval: that is how $SL(2, \mathbb C)$ will act (Theorem §CB.15.5).
> - The spatial part alone, $\mathbf x\cdot\boldsymbol\sigma$ (traceless Hermitian), is the dictionary of the rotation case, with $\det(\mathbf x\cdot\boldsymbol\sigma) = -|\mathbf x|^2$ ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]).

^der-cb-15-3

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-20|Def. §CB.0.20]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-22|Theorem §CB.0.22]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]]

## The covering map SL(2,ℂ) → SO⁺(1,3)

> [!theorem] Theorem §CB.15.4: SL(2, C) Is Connected and Simply Connected
> Every $\lambda \in SL(2, \mathbb C)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-2|Def. §CB.1.2]]) is uniquely $\lambda = e^{h}U$ with $U \in SU(2)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]) and $h$ traceless Hermitian, $h = -\frac12\boldsymbol\eta\cdot\boldsymbol\sigma$ for a unique $\boldsymbol\eta \in \mathbb R^3$, and $\lambda \mapsto (\boldsymbol\eta, U)$ is a homeomorphism $SL(2, \mathbb C) \cong \mathbb R^3\times S^3$. Hence $SL(2, \mathbb C)$ is path-connected and simply connected ([[§29 The Fundamental Group#^def-29-3|590 Def. §29.3]]).
>
> *Source: Yu Exercise 3.7(d), eq. (3.265) · the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit", part (d)) · the continuity of the decomposition quoted from the functional calculus*

^thm-cb-15-4

> [!derivation]- Derivation
> **1. The positive part.** $\lambda\lambda^\dagger$ is Hermitian and positive definite: $v^\dagger\lambda\lambda^\dagger v = |\lambda^\dagger v|^2 > 0$ for $v \ne 0$, since $\lambda$ is invertible. By the spectral theorem it is $W\operatorname{diag}(p_1, p_2)W^\dagger$ with $W$ unitary and $p_k > 0$. Set $h = \frac12W\operatorname{diag}(\ln p_1, \ln p_2)W^\dagger$, Hermitian, so that $e^{2h} = \lambda\lambda^\dagger$ ($e^{WDW^\dagger} = We^DW^\dagger$ term by term). It is the unique Hermitian $h$ with $e^{2h} = \lambda\lambda^\dagger$: $e^{2h}$ and $h$ have the same eigenvectors, and $\ln$ is injective on $(0, \infty)$; equivalently $e^h$ is the unique positive square root of $\lambda\lambda^\dagger$ ([[§25 Positive Operators#^ladr-7-39|LADR 7.39]]).
>
> **2. The unitary part.** Put $U = e^{-h}\lambda$. Then $UU^\dagger = e^{-h}\lambda\lambda^\dagger e^{-h} = e^{-h}e^{2h}e^{-h} = \mathbb 1$, so $U$ is unitary and $\lambda = e^hU$: the polar decomposition ([[§28 Consequences of Singular Value Decomposition#^ladr-7-93|LADR 7.93]], here with the positive factor on the left).
>
> **3. Determinants.** $1 = \det\lambda = \det e^h\det U = e^{\operatorname{tr}h}\det U$. Here $e^{\operatorname{tr}h} > 0$ ($h$ Hermitian has real trace) and $|\det U| = 1$; a positive number times a unit-modulus number equals $1$ only if the positive number is $1$ and the phase is $1$. So $\operatorname{tr}h = 0$ and $\det U = 1$: $U \in SU(2)$, and $h$ is traceless Hermitian, $h = \mathbf a\cdot\boldsymbol\sigma$ with $\mathbf a$ real ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], part 4); write $\mathbf a = -\frac12\boldsymbol\eta$.
>
> **4. Uniqueness.** If $\lambda = e^{h'}U'$ is another such decomposition, then $\lambda\lambda^\dagger = e^{h'}U'U'^\dagger e^{h'} = e^{2h'}$, so $h' = h$ by step 1, and $U' = e^{-h}\lambda = U$.
>
> **5. Homeomorphism.** The map $(\boldsymbol\eta, U) \mapsto e^{-\boldsymbol\eta\cdot\boldsymbol\sigma/2}U$ is continuous (products and the exponential series), and by steps 1–4 it is a bijection $\mathbb R^3\times SU(2) \to SL(2, \mathbb C)$. Its inverse $\lambda \mapsto h = \frac12\ln(\lambda\lambda^\dagger)$, $U = e^{-h}\lambda$ is continuous because the logarithm of positive definite matrices is continuous (functional calculus; quoted). $SU(2)$ is homeomorphic to $S^3$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-19|Theorem §CB.1.19]]; [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^der-cb-9-7|Derivation §CB.9.7]], step 1).
>
> **6. Topology.** $\mathbb R^3$ is convex, so path-connected with every loop contractible (straight-line homotopy); $S^3$ is path-connected and simply connected ([[§37 The Fundamental Group of Sⁿ#^thm-37-3|590 Thm. §37.3]]). A product of path-connected spaces is path-connected, and $\pi_1(\mathbb R^3\times S^3) \cong \pi_1(\mathbb R^3)\times\pi_1(S^3) = 1$ ([[§29 The Fundamental Group#^thm-29-7|590 Thm. §29.7]]).
>
> **What the derivation shows**
> - $SL(2, \mathbb C)$ is "rotations times boosts": $U$ will map to a rotation and $e^h$ to a pure boost, the $2\times2$ counterpart of $\Lambda = B(u)R$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]]).
> - The noncompact factor $\mathbb R^3$ is topologically trivial; all the topology sits in the compact factor, and for $SL(2, \mathbb C)$ that factor is the simply connected $S^3$.
> - One input was quoted: the continuity of the matrix logarithm on positive matrices.
> - Used next: connectedness puts the image of the covering map in $SO^+(1,3)$ (Theorem §CB.15.5); simple connectivity makes it the universal cover (Theorem §CB.15.7).

^der-cb-15-4

*Uses:* [[§25 Positive Operators#^ladr-7-39|LADR 7.39]], [[§28 Consequences of Singular Value Decomposition#^ladr-7-93|LADR 7.93]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-19|Theorem §CB.1.19]], [[§37 The Fundamental Group of Sⁿ#^thm-37-3|590 Thm. §37.3]], [[§29 The Fundamental Group#^thm-29-7|590 Thm. §29.7]]; quoted: continuity of the logarithm of positive matrices

> [!theorem] Theorem §CB.15.5: Every Element of SL(2, C) Gives a Lorentz Transformation
> For $\lambda \in SL(2, \mathbb C)$ define $\Lambda(\lambda)$ through the dictionary $x \leftrightarrow x_\mu\sigma^\mu$ of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]] by
>
> $$
> \lambda\,(x_\mu\sigma^\mu)\,\lambda^\dagger = \bigl(\Lambda(\lambda)x\bigr)_\mu\sigma^\mu, \qquad\text{i.e.}\qquad \Lambda(\lambda)^\mu{}_\nu = \tfrac12\operatorname{tr}\bigl(\lambda\sigma_\nu\lambda^\dagger\bar\sigma^\mu\bigr) .
> $$
>
> Then $\Lambda(\lambda)$ is a proper orthochronous Lorentz transformation, $\Lambda(\lambda) \in SO^+(1,3)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]), $\Lambda(\lambda_1\lambda_2) = \Lambda(\lambda_1)\Lambda(\lambda_2)$, $\Lambda(\mathbb 1) = \mathbb 1$, and $\lambda \mapsto \Lambda(\lambda)$ is continuous: a continuous homomorphism $\pi: SL(2, \mathbb C) \to SO^+(1,3)$.
>
> *Source: Yu Exercise 3.7(b)–(c), eqs. (3.261)–(3.264), (d) · the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit", parts (b), (d))*

^thm-cb-15-5

> [!derivation]- Derivation
> **1. A real linear map.** For Hermitian $X$, $(\lambda X\lambda^\dagger)^\dagger = \lambda X^\dagger\lambda^\dagger = \lambda X\lambda^\dagger$ is Hermitian, so by Theorem §CB.15.3 it is $X'$ for a unique real $x'$. $X$ is linear in $x$ and $X \mapsto \lambda X\lambda^\dagger$ is linear, so $x' = \Lambda(\lambda)x$ with $\Lambda(\lambda)$ a real $4\times4$ matrix. Its entries: $X = x_\nu\sigma^\nu = x^\nu\sigma_\nu$, and by the inverse formula $x'^\mu = \frac12\operatorname{tr}(\lambda x^\nu\sigma_\nu\lambda^\dagger\bar\sigma^\mu)$, which gives the trace formula; it is a polynomial in the entries of $\lambda$ and $\lambda^{\ast}$, hence continuous.
>
> **2. The interval is preserved.** $\det X' = \det\lambda\,\det X\,\det\lambda^\dagger = |\det\lambda|^2\det X = \det X$, i.e. $x'^2 = x^2$ (Theorem §CB.15.3). A linear map preserving the quadratic form preserves the bilinear form, by polarization: $x\cdot y = \frac12\bigl((x + y)^2 - x^2 - y^2\bigr)$. So $\Lambda(\lambda)^{\mathsf T}g\Lambda(\lambda) = g$: $\Lambda(\lambda) \in O(1,3)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]).
>
> **3. Homomorphism.** $(\lambda_1\lambda_2)X(\lambda_1\lambda_2)^\dagger = \lambda_1(\lambda_2X\lambda_2^\dagger)\lambda_1^\dagger$: first $x \mapsto \Lambda(\lambda_2)x$, then $\Lambda(\lambda_1)$. By injectivity of $x \mapsto X$, $\Lambda(\lambda_1\lambda_2) = \Lambda(\lambda_1)\Lambda(\lambda_2)$. For $\lambda = \mathbb 1$, $X' = X$, so $\Lambda(\mathbb 1) = \mathbb 1$.
>
> **4. Proper and orthochronous.** $SL(2, \mathbb C)$ is path-connected (Theorem §CB.15.4) and $\pi$ is continuous (step 1), so the image $\pi(SL(2, \mathbb C))$ is a path-connected subset of $O(1,3)$ containing $\pi(\mathbb 1) = \mathbb 1$. It therefore lies in the component of the identity, which is $SO^+(1,3)$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], 2).
>
> **What the derivation shows**
> - Only $|\det\lambda| = 1$ was used for step 2; Yu then fixes the phase by $\det\lambda = 1$, since $\lambda$ and $e^{i\alpha}\lambda$ give the same $\Lambda$. The group $SL(2, \mathbb C)$ is what remains after that redundancy is removed, up to the sign left over in Theorem §CB.15.6.
> - Determinant $+1$ and $\Lambda^0{}_0 > 0$ were not checked by hand: connectedness does it. Directly, $\Lambda^0{}_0 = \frac12\operatorname{tr}(\lambda\lambda^\dagger) > 0$.
> - Used next: the kernel (Theorem §CB.15.6), the link to the parameters $\omega$ (Theorem §C5a.4.2).

^der-cb-15-5

*Uses:* [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]]

> [!theorem] Theorem §CB.15.6: The Kernel Is ±1
> For the homomorphism $\pi$ of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-5|Theorem §CB.15.5]], $\pi(\lambda) = \mathbb 1$ iff $\lambda = \pm\mathbb 1$. Hence $\pi(\lambda) = \pi(\lambda')$ iff $\lambda' = \pm\lambda$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit", part (c)) · Yu Exercise 3.7(d) (paragraph after (3.265))*

^thm-cb-15-6

> [!derivation]- Derivation
> **1. ±1 are in the kernel.** $(\pm\mathbb 1)X(\pm\mathbb 1)^\dagger = X$, and $\det(\pm\mathbb 1) = 1$.
>
> **2. An element of the kernel is unitary.** If $\pi(\lambda) = \mathbb 1$, then $\lambda X\lambda^\dagger = X$ for every Hermitian $X$. Take $X = \mathbb 1$ ($x = (1, \mathbf 0)$): $\lambda\lambda^\dagger = \mathbb 1$, so $\lambda^\dagger = \lambda^{-1}$.
>
> **3. It commutes with everything.** With $\lambda^\dagger = \lambda^{-1}$ the condition reads $\lambda X\lambda^{-1} = X$, i.e. $\lambda X = X\lambda$, for every Hermitian $X$, in particular for $\sigma^1, \sigma^2, \sigma^3$. Together with $\mathbb 1$ these span $M_2(\mathbb C)$ over $\mathbb C$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], part 4), so $\lambda$ commutes with every $2\times2$ matrix; taking the matrix units $E_{12}$, $E_{21}$ forces $\lambda = c\mathbb 1$ (the same conclusion as Schur's lemma, [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-4|Theorem §CB.6.4]]).
>
> **4. The scalar.** $\det(c\mathbb 1) = c^2 = 1$ gives $c = \pm1$.
>
> **5. Fibres.** $\pi(\lambda) = \pi(\lambda')$ iff $\pi(\lambda'\lambda^{-1}) = \mathbb 1$ (homomorphism, Theorem §CB.15.5) iff $\lambda'\lambda^{-1} = \pm\mathbb 1$.
>
> **What the derivation shows**
> - The sign ambiguity is the only one: two spinor matrices $\pm\lambda$ for each Lorentz transformation. This is the matrix origin of "a spinor's matrix is fixed only up to sign" ([[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-4|§C3.3, Remark: Why a spinor's matrix is fixed only up to sign]]).
> - The argument is that of the rotation case ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], 3), with $X = \mathbb 1$ added to force unitarity first.

^der-cb-15-6

*Uses:* [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-5|Theorem §CB.15.5]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]]

The double-cover theorem below is proved with the course's Weyl matrices, the explicit matrices of $(\frac12, 0)$ and $(0, \frac12)$, and their covering property; these are physics statements, proved in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] and shown here because the proof uses them:

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1]]

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1]]

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2]]

> [!theorem] Theorem §CB.15.7: SL(2, C) Is the Double Cover of SO⁺(1,3)
> 1. $\pi: SL(2, \mathbb C) \to SO^+(1,3)$ is onto, and $SO^+(1,3) \cong SL(2, \mathbb C)/\{\pm\mathbb 1\}$.
> 2. $SO^+(1,3)$ is homeomorphic to $\mathbb R^3\times SO(3)$, so its fundamental group ([[§29 The Fundamental Group#^def-29-2|590 Def. §29.2]]) is $\pi_1(SO^+(1,3)) \cong \mathbb Z_2$: it is doubly connected, as anticipated in [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^rem-cb-9-2|§CB.9, Remark: The same pattern for the Lorentz group]]. The non-contractible loops are those homotopic to a rotation through $2\pi$; the lift ([[§32 Lifting and the Fundamental Group of the Circle#^def-32-1|590 Def. §32.1]]) of that loop to $SL(2, \mathbb C)$ starting at $\mathbb 1$, $\theta \mapsto \Lambda_L(\theta\hat{\mathbf z}) = e^{-i\theta\sigma^3/2}$, ends at $-\mathbb 1$.
> 3. Under $\pi$, $U \in SU(2)$ goes to the rotation $\operatorname{diag}(1, R(U))$ of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-20|Theorem §CB.1.20]], and $e^{-\boldsymbol\eta\cdot\boldsymbol\sigma/2}$ to the pure boost $e^{\omega}$ with $\omega_{0i} = \eta_i$, $\omega_{ij} = 0$. $\pi$ is a covering map ([[§31 Covering Spaces#^def-31-2|590 Def. §31.2]]), and since $SL(2, \mathbb C)$ is simply connected ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]]), it is the universal covering group of $SO^+(1,3)$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The left-handed Weyl matrices are this covering": "every element of $\mathrm{SO}^+(1,3)$ is reached … $\mathrm{SO}^+(1,3) \cong \mathbb{RP}^3\times\mathbb R^3$") · Yu Exercise 3.7(d) · Yu §3.2 (the covering group of SO⁺(1,3) named, below Fig. 3.5) · the user's pre-course notes, §5.2 (Remark "SL(2,C) made explicit": kernel and surjectivity "stated, not proved here") · the user's PHY 513 notes, Ch. 7 §7.2 (end of Derivation "Why the sign appears": the topological argument) · that a surjective Lie-group homomorphism with bijective differential is a covering map, quoted*

^thm-cb-15-7

> [!derivation]- Derivation
> **1. Onto.** Every $\Lambda \in SO^+(1,3)$ is a boost times a rotation, $\Lambda = B(u)R$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]]), and each factor is an exponential $e^{\omega_1}$, $e^{\omega_2}$ ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-5|Theorem §CB.4.5]]; a boost along $\hat{\mathbf n}$ is $e^{\omega}$ with $\omega_{0i} = \eta n_i$, as used in [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-12|Derivation §CB.16.12]], step 5). By Theorem §C5a.4.2, $\pi(\Lambda_L(\omega_1)\Lambda_L(\omega_2)) = e^{\omega_1}e^{\omega_2} = \Lambda$.
>
> **2. The quotient.** $\pi$ is an onto homomorphism with kernel $\{\pm\mathbb 1\}$ (Theorem §CB.15.6), so $SL(2, \mathbb C)/\{\pm\mathbb 1\} \cong SO^+(1,3)$ by the first isomorphism theorem ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]).
>
> **3. The topology of SO⁺(1,3).** By [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], $\Lambda = B(u)R$ with $u = \Lambda e_0$, the first column, $u = (\gamma, \mathbf u)$, $\gamma = \sqrt{1 + \mathbf u^2}$. The map $\Lambda \mapsto (\mathbf u, R)$, $R = B(u)^{-1}\Lambda$, is continuous (the entries of $B(u)$ are continuous in $\mathbf u$, $\gamma \ge 1$), and its inverse $(\mathbf u, R) \mapsto B(u)R$ is continuous: a homeomorphism $SO^+(1,3) \cong \mathbb R^3\times SO(3)$. Hence $\pi_1(SO^+(1,3)) \cong \pi_1(\mathbb R^3)\times\pi_1(SO(3)) = 1\times\mathbb Z_2$ ([[§29 The Fundamental Group#^thm-29-7|590 Thm. §29.7]]; [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-7|Theorem §CB.9.7]]), and a loop is non-contractible iff its $SO(3)$ component is, i.e. iff it is homotopic to the $2\pi$ rotation loop.
>
> **4. The lift of the 2π loop.** $\theta \mapsto \Lambda_L(\theta\hat{\mathbf z}) = e^{-i\theta\sigma^3/2}$, $0 \le \theta \le 2\pi$, is continuous, starts at $\mathbb 1$, and lies over the rotation loop by Theorem §C5a.4.2. At $\theta = 2\pi$ it is $\operatorname{diag}(e^{-i\pi}, e^{i\pi}) = -\mathbb 1$ ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]]): a closed loop downstairs whose lift is open. ⚑ By-product: this is the "$2\pi$ rotation $= -1$" of every half-integer representation, now seen as the endpoint of a lift → [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-6|Theorem §CB.16.6]].
>
> **5. The two decompositions match.** For $U \in SU(2)$, $UXU^\dagger = x^0\mathbb 1 - U(\mathbf x\cdot\boldsymbol\sigma)U^\dagger = x^0\mathbb 1 - (R(U)\mathbf x)\cdot\boldsymbol\sigma$ by the definition of $R(U)$ in Theorem §CB.1.20, so $\pi(U) = \operatorname{diag}(1, R(U))$. For $h = -\frac12\boldsymbol\eta\cdot\boldsymbol\sigma$, $e^h = \Lambda_L(\omega)$ with $\boldsymbol\theta = 0$, so $\pi(e^h) = e^{\omega}$, a pure boost (Theorem §C5a.4.2). The polar decomposition $\lambda = e^hU$ of Theorem §CB.15.4 is mapped to "boost times rotation".
>
> **6. Universal cover.** $\pi$ is a continuous surjective homomorphism of Lie groups whose differential at $\mathbb 1$ sends the generator $A_L(\omega)$ to $\omega$ (step 2 of Derivation §C5a.4.2), a bijection between the two six-dimensional algebras; such a map is a covering map (quoted). A simply connected covering space is the universal cover, and its fibre $\{\pm\mathbb 1\}$ has as many points as $\pi_1(SO^+(1,3))$ has elements, consistently with step 3 ([[§32 Lifting and the Fundamental Group of the Circle#^thm-32-4|590 Thm. §32.4]]).
>
> **What the derivation shows**
> - All topology of the Lorentz group is that of its rotation subgroup: boosts form a contractible $\mathbb R^3$, and the cover unwraps only the $SO(3)$ factor into $S^3$. This makes the remark of §C3.1 precise.
> - $SO^+(1,3) \cong \mathbb{RP}^3\times\mathbb R^3$, $SL(2, \mathbb C) \cong S^3\times\mathbb R^3$, the $\pm$ identification acting on the sphere only.
> - One input was quoted: that $\pi$ is a covering map. Everything needed later (onto, kernel, the lift of the $2\pi$ loop) was derived.
> - Used next: integrating $(j_+, j_-)$ (Theorem §CB.16.7).

^der-cb-15-7

*Uses:* [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-6|Theorem §CB.15.6]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-5|Theorem §CB.4.5]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-7|Theorem §CB.9.7]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-20|Theorem §CB.1.20]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]], [[§29 The Fundamental Group#^thm-29-7|590 Thm. §29.7]], [[§32 Lifting and the Fundamental Group of the Circle#^thm-32-4|590 Thm. §32.4]]; quoted: a surjective Lie-group homomorphism with bijective differential is a covering map

That the differential of the covering is the isomorphism of real Lie algebras of [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-8|Theorem §CB.5.8]] (first stated there; moved here in the CB ordering pass, since it needs $\pi$):

> [!theorem] Theorem §CB.15.n1: The Differential of π Is the Isomorphism of Theorem §CB.5.8
> The differential ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]) of the covering $\pi : SL(2, \mathbb C) \to SO^+(1,3)$ of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-7|Theorem §CB.15.7]] is an isomorphism of real Lie algebras $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^def-cb-5-7|Def. §CB.5.7]]); in the conventions of Theorem §CB.15.7 it sends $-\frac i2\sigma^k \mapsto -iJ_k$ and $-\frac12\sigma^k \mapsto -iK_k$. So $\pi_\ast$ is the isomorphism $\varphi$ of [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-8|Theorem §CB.5.8]].
>
> *Source: [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-7|Theorem §CB.15.7]], 3, differentiated (first stated as Theorem §CB.5.8; moved here in the CB ordering pass, 2026-10-08, because it needs the covering map) · Yu, Exercise 3.7 · the user's PHY 513 notes, Ch. 8 §8.2 · conventions checked against [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]] and [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]] (batch 2)*

^thm-cb-15-n1

> [!proof]- Proof
> *Source: the vault's [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-7|Theorem §CB.15.7]], part 3 (from the user's PHY 513 notes, Ch. 8 §8.2, and Yu, Exercise 3.7), differentiated with [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]. Convention check (batch 2): Larsen's register, $\Lambda = e^{-i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\eta\cdot\mathbf K}$ with $-iJ_i = M^{jk}$ ($ijk$ cyclic) and $-iK_i = M^{0i}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]); the statement's two assignments are confirmed in Steps 2–3, so the statement stands unchanged.*
>
> **Step 1** (a real basis). $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ consists of the traceless complex $2\times2$ matrices ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]]); $\sigma^1, \sigma^2, \sigma^3$ are a complex basis of them, so the six matrices $-\frac i2\sigma^k$, $-\frac12\sigma^k$ are a real basis. Likewise $-iJ_k$, $-iK_k$ are a real basis of $\mathfrak{so}(1,3)$.
>
> **Step 2** (rotations). By Theorem §CB.15.7, 3, $\pi(U) = \operatorname{diag}(1, R(U))$ for $U \in SU(2)$, and $R(e^{-is\sigma^k/2})$ is the rotation by $s$ about $x^k$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-20|Theorem §CB.1.20]], 2), which in the vector representation is $e^{-isJ_k} = e^{sM^{ij}}$ ($ijk$ cyclic; [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-5|Theorem §CB.4.5]], 3). By the formula of Theorem §CB.2.3,
>
> $$
> \pi_\ast\bigl(-\tfrac i2\sigma^k\bigr) = \frac{d}{ds}\pi\bigl(e^{-is\sigma^k/2}\bigr)\Big|_{s=0} = \frac{d}{ds}e^{-isJ_k}\Big|_{s=0} = -iJ_k .
> $$
>
> **Step 3** (boosts). By Theorem §CB.15.7, 3, $\pi(e^{-\boldsymbol\eta\cdot\boldsymbol\sigma/2})$ is the pure boost $e^\omega$ with $\omega_{0i} = \eta_i$, $\omega_{ij} = 0$; for $\boldsymbol\eta = s\,\mathbf e_k$ this is $e^{sM^{0k}} = e^{-isK_k}$ (Def. §CB.4.4: $-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu} = -i\boldsymbol\eta\cdot\mathbf K$). Hence
>
> $$
> \pi_\ast\bigl(-\tfrac12\sigma^k\bigr) = \frac{d}{ds}\pi\bigl(e^{-s\sigma^k/2}\bigr)\Big|_{s=0} = \frac{d}{ds}e^{-isK_k}\Big|_{s=0} = -iK_k .
> $$
>
> **Step 4** (isomorphism). $\pi_\ast$ is real-linear and preserves brackets (Theorem §CB.2.3) and maps the real basis of Step 1 onto the real basis of Step 1: it is bijective, hence an isomorphism of real Lie algebras $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-2|Def. §CB.2.2]]). Steps 2–3 are the values of $\varphi$ on that basis, so $\pi_\ast = \varphi$ ([[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-8|Theorem §CB.5.8]]).
>
> **Step 5** (a check on brackets). $[-\frac i2\sigma^1, -\frac i2\sigma^2] = -\frac14[\sigma^1, \sigma^2] = -\frac14\cdot2i\sigma^3 = -\frac i2\sigma^3$, matching $[-iJ_1, -iJ_2] = -[J_1, J_2] = -iJ_3$; and $[-\frac12\sigma^1, -\frac12\sigma^2] = \frac14\cdot2i\sigma^3 = -(-\frac i2\sigma^3)$, matching $[-iK_1, -iK_2] = -[K_1, K_2] = iJ_3 = -(-iJ_3)$ ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-6|Theorem §CB.4.6]]).
>
> **What the proof shows.**
> - ⚑ By-product: in $\mathfrak{sl}(2, \mathbb C)$ a boost generator is a complex multiple of a rotation generator, $-\frac12\sigma^k = -i\bigl(-\frac i2\sigma^k\bigr)$. So multiplication by $i$ on $\mathfrak{sl}(2, \mathbb C)$ becomes, on $\mathfrak{so}(1,3)$, the real-linear map $-iJ_k \mapsto iK_k$, $-iK_k \mapsto -iJ_k$ (it squares to $-\mathbb 1$) — a complex structure on $\mathfrak{so}(1,3)$ that is invisible from its definition → Theorem §CB.15.1.
> - The opposite sign convention for $\mathbf K$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators|§C1a.6]], after Def. §C1a.6.2: some sources use $K^i = \mathcal J^{i0}$) would flip the second assignment.

^pf-cb-15-n1

*Uses:* [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-7|Theorem §CB.15.7]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-8|Theorem §CB.5.8]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-20|Theorem §CB.1.20]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-4|Def. §CB.4.4]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-5|Theorem §CB.4.5]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-2|Def. §CB.2.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-6|Theorem §CB.4.6]]

> [!remark] Remark: The rotation story, one level up
>
> | | rotations | Lorentz transformations |
> |---|---|---|
> | vectors as matrices | $\mathbf x\cdot\boldsymbol\sigma$, traceless Hermitian | $x_\mu\sigma^\mu$, Hermitian |
> | invariant | $-\det = \lvert\mathbf x\rvert^2$ | $\det = x_\mu x^\mu$ |
> | action | $U(\mathbf x\cdot\boldsymbol\sigma)U^\dagger$, $U \in SU(2)$ | $\lambda(x_\mu\sigma^\mu)\lambda^\dagger$, $\lambda \in SL(2, \mathbb C)$ |
> | kernel | $\pm\mathbb 1$ | $\pm\mathbb 1$ |
> | covering space | $S^3$, compact | $S^3\times\mathbb R^3$, not compact |
> | finite-dimensional representations | unitary | not unitary (except trivial) |
>
> The left column is [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]; the right column contains it as the subgroup fixing $x^0 = \frac12\operatorname{tr}X$ (unitary $\lambda$). Two things change: $\lambda^\dagger$ is no longer $\lambda^{-1}$, so $\lambda X\lambda^\dagger$ is not a similarity transformation and the trace (time) is no longer preserved; and the group is not compact, so averaging over it is impossible and unitarity is lost ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-12|Theorem §CB.16.12]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit": "Rotations had $U^\dagger\sigma^iU = R^i{}_j\sigma^j$ … The Lorentz version turns a four-vector into a $2\times2$ matrix")*

^rem-cb-15-1

## The Clifford route

Throughout, $V = \mathbb R^{1,3}$ with $q(x) = g(x, x)$, $g = \operatorname{diag}(+,-,-,-)$, and $e_0, \dots, e_3$ the standard basis ($q(e_0) = 1$, $q(e_i) = -1$).

## The even Clifford algebra of Minkowski space

> [!theorem] Theorem §CB.15.8: Cl⁰(1,3) ≅ Cl(3,0) ≅ M₂(ℂ)
> The elements $f_i = e_ie_0$ ($i = 1, 2, 3$) of $\mathrm{Cl}^0(1,3)$ satisfy $f_i^2 = +1$ and $f_if_j = -f_jf_i$ ($i \ne j$), and $e_i \mapsto f_i$ extends to an isomorphism $\mathrm{Cl}(3,0) \cong \mathrm{Cl}^0(1,3)$ ([[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-16|Theorem §CB.11.16]] with $\epsilon = 1$). Composed with [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-1|Theorem §CB.14.1]] it gives an isomorphism of real algebras $\phi : \mathrm{Cl}^0(1,3) \to M_2(\mathbb C)$, $\phi(f_i) = \sigma^i$, with $\phi(\omega) = i\mathbb 1$ for $\omega = e_0e_1e_2e_3 = f_1f_2f_3$. Under $\phi$ the map $x \mapsto xe_0$, $V \to \mathrm{Cl}^0$, sends $x = x^\mu e_\mu$ to the Hermitian matrix $\tilde x = x^0\mathbb 1 + x^i\sigma^i$, which is $\bar X = x_\mu\bar\sigma^\mu$ of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-20|Def. §CB.0.20]] (not the course's $X = x_\mu\sigma^\mu$).
>
> *Source: written here · the matrices $x^0 + \mathbf x\cdot\boldsymbol\sigma$ for four-vectors: P. Woit, Quantum Theory, Groups and Representations, §40.4*

^thm-cb-15-8

> [!proof]- Proof
> Orthogonal vectors anticommute in $\mathrm{Cl}(1,3)$: $uv + vu = 2B(u, v)$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-8|Theorem §CB.10.8]]), and $e_\mu \perp e_\nu$ for $\mu \ne \nu$. Also $e_0^2 = q(e_0) = 1$ and $e_i^2 = q(e_i) = -1$.
>
> **1. Squares.** $f_i^2 = e_ie_0e_ie_0 = -e_ie_ie_0e_0 = -(-1)(1) = 1$, moving the middle $e_0$ past $e_i$ (one sign).
>
> **2. Anticommutation.** For $i \ne j$: $f_if_j = e_ie_0e_je_0 = -e_ie_je_0e_0 = -e_ie_j$, and likewise $f_jf_i = -e_je_i = e_ie_j$. So $f_if_j = -f_jf_i$. ⚑ By-product: $e_ie_j = -f_if_j$, used for the rotation generators in Theorem §CB.15.10.
>
> **3. The even subalgebra is Cl(3,0).** In Theorem §CB.11.16 take $e_0$ with $q(e_0) = \epsilon = 1$; then $V' = e_0^\perp = \operatorname{span}\{e_1, e_2, e_3\}$ with $q'(v') = -\epsilon q(v') = -q(v')$, so $q'(e_i) = +1$: $(V', q') = \mathbb R^{3,0}$. The isomorphism $\mathrm{Cl}(3,0) \cong \mathrm{Cl}^0(1,3)$ of that theorem is $v' \mapsto v'e_0$, i.e. $e_i \mapsto f_i$; steps 1–2 are the relations it requires.
>
> **4. The matrix algebra.** Theorem §CB.14.1 gives the real-algebra isomorphism $\mathrm{Cl}(3,0) \cong M_2(\mathbb C)$, $e_i \mapsto \sigma^i$. Composing with the inverse of step 3 gives $\phi$ with $\phi(f_i) = \sigma^i$. In particular the $f_i$ generate $\mathrm{Cl}^0(1,3)$ as a real algebra, since the $e_i$ generate $\mathrm{Cl}(3,0)$.
>
> **5. The volume element.** $f_1f_2 = -e_1e_2$ (step 2), so $f_1f_2f_3 = -e_1e_2e_3e_0$. Moving $e_0$ to the front past $e_3$, $e_2$, $e_1$ costs $(-1)^3$: $f_1f_2f_3 = e_0e_1e_2e_3 = \omega$. Hence $\phi(\omega) = \sigma^1\sigma^2\sigma^3 = i\mathbb 1$ (Theorem §CB.14.1).
>
> **6. Four-vectors.** $xe_0 = x^0e_0e_0 + x^ie_ie_0 = x^0 + x^if_i$, so $\phi(xe_0) = x^0\mathbb 1 + x^i\sigma^i$. With $x_0 = x^0$, $x_i = -x^i$ and $\bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma)$ (Def. §CB.0.20), $x_\mu\bar\sigma^\mu = x^0\mathbb 1 + x^i\sigma^i = \bar X$.
>
> **What the proof shows**
> - The course's Hermitian $2\times2$ picture of a four-vector is the Clifford product $xe_0$, read in $\mathrm{Cl}^0 \cong M_2(\mathbb C)$.
> - ⚑ By-product (a convention): the natural Clifford identification gives $\bar X = x_\mu\bar\sigma^\mu$, while the course's covering map is built on $X = x_\mu\sigma^\mu$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]]). The two differ by $\sigma^i \to -\sigma^i$; its effect on the group is worked out in Theorem §CB.15.9, 2.
> - Used next: Theorems §CB.15.9–§CB.15.10, and the Dirac module in §CB.17.

^pf-cb-15-8

*Uses:* [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-8|Theorem §CB.10.8]], [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-16|Theorem §CB.11.16]], [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-1|Theorem §CB.14.1]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-20|Def. §CB.0.20]]

## Spin(1,3) and SL(2,ℂ)

> [!theorem] Theorem §CB.15.9: Spin(1,3)₀ Is SL(2,ℂ), and ρ Is the Course's Covering Map up to λ ↦ (λ†)⁻¹
> 1. The isomorphism $\phi$ of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-8|Theorem §CB.15.8]] restricts to an isomorphism of Lie groups from $\mathrm{Spin}(1,3)_0$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-6|Def. §CB.13.6]]) onto $SL(2, \mathbb C)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-2|Def. §CB.1.2]]).
> 2. For $x \in \mathrm{Spin}(1,3)_0$ and $\lambda = \phi(x)$, $\rho(x)$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-7|Theorem §CB.13.7]]) acts on $\tilde x = x_\mu\bar\sigma^\mu$ (Theorem §CB.15.8) by $\tilde x \mapsto \lambda\tilde x\lambda^\dagger$, and $\ker\rho = \{\pm1\}$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-12|Theorem §CB.13.12]]). The course's covering $\pi : SL(2, \mathbb C) \to SO^+(1,3)$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-5|Theorem §CB.15.5]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-7|Theorem §CB.15.7]]) acts instead on $X = x_\mu\sigma^\mu$ by $X \mapsto \mu X\mu^\dagger$, and
>
> $$
> \rho(x) = \pi\bigl(\theta(\phi(x))\bigr), \qquad \theta(\lambda) = (\lambda^\dagger)^{-1} .
> $$
>
> So the element of $\mathrm{Spin}(1,3)_0$ over $e^\omega$ is sent by $\phi$ to $\pm\Lambda_R(\omega)$ and by $\theta\circ\phi$ to $\pm\Lambda_L(\omega)$ (the Weyl matrices, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]]); $\theta\circ\phi$ is the restriction of the real-algebra isomorphism $\phi' : \mathrm{Cl}^0(1,3) \to M_2(\mathbb C)$ with $\phi'(f_i) = -\sigma^i$, $\phi'(xe_0) = X$, and $\rho = \pi\circ\phi'$ on $\mathrm{Spin}(1,3)_0$.
> 3. $\phi$ maps $\mathrm{Spin}(1,3)$ onto $\{A \in M_2(\mathbb C) : \det A = \pm1\}$. $\mathrm{Spin}(1,3)$ has two components, $\mathrm{Spin}(1,3)_0$ and $e_0e_1\,\mathrm{Spin}(1,3)_0$; $\rho(e_0e_1) = \operatorname{diag}(-1, -1, 1, 1)$, and $\rho$ maps the two components onto $SO^+(1,3)$ and onto $\mathcal P\mathcal T\cdot SO^+(1,3)$, the component of $SO(1,3)$ containing $\mathcal P\mathcal T$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-12|Theorem §CB.2.12]]).
>
> *Source: written here · the action $\Omega(\cdot)\Omega^\dagger$ on $x^0 + \mathbf x\cdot\boldsymbol\sigma$: P. Woit, Quantum Theory, Groups and Representations, §40.4 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the course's covering: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (the user's PHY 513 notes, Ch. 8 §8.2; Yu Exercise 3.7)*

^thm-cb-15-9

> [!proof]- Proof
> Notation: $\tilde v = \phi(ve_0) = v_\mu\bar\sigma^\mu$ for $v \in V$ (Theorem §CB.15.8, 6); $\theta(\lambda) = (\lambda^\dagger)^{-1}$.
>
> **1. Conjugation by e₀.** Since $e_0^2 = 1$, $\kappa(a) = e_0ae_0$ is an algebra automorphism of $\mathrm{Cl}^0(1,3)$: $\kappa(ab) = e_0ae_0e_0be_0 = \kappa(a)\kappa(b)$. On the generators, $\kappa(f_i) = e_0e_ie_0e_0 = e_0e_i = -e_ie_0 = -f_i$.
>
> **2. Its matrix form.** $\tilde\kappa(A) = \sigma^2\bar A\sigma^2$ ($\bar A$ the entrywise conjugate) is a real-algebra automorphism of $M_2(\mathbb C)$: real-linear, $\tilde\kappa(AB) = \sigma^2\bar A\sigma^2\sigma^2\bar B\sigma^2 = \tilde\kappa(A)\tilde\kappa(B)$ because $(\sigma^2)^2 = \mathbb 1$, $\tilde\kappa(\mathbb 1) = \mathbb 1$. By [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-22|Theorem §CB.0.22]], 3, $\sigma^2(\sigma^i)^{\ast}\sigma^2 = -\sigma^i$, so $\tilde\kappa(\sigma^i) = -\sigma^i$. Thus $\phi\circ\kappa$ and $\tilde\kappa\circ\phi$ are real-algebra homomorphisms $\mathrm{Cl}^0 \to M_2(\mathbb C)$ that agree on the generators $f_i$ (both give $-\sigma^i$; Theorem §CB.15.8, 4), hence everywhere: $\phi(\kappa(a)) = \tilde\kappa(\phi(a))$.
>
> **3. On determinant ±1, κ̃ is ±θ.** By [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-15|Theorem §CB.7.15]], 1, applied to $\bar A$: $\bar A^{\mathsf T}\varepsilon\bar A = \overline{\det A}\,\varepsilon$, so for invertible $A$, $\varepsilon\bar A\varepsilon^{-1} = \overline{\det A}\,(\bar A^{\mathsf T})^{-1} = \overline{\det A}\,(A^\dagger)^{-1}$. With $\varepsilon = i\sigma^2$, $\varepsilon^{-1} = -i\sigma^2$, the left side is $\sigma^2\bar A\sigma^2$. Hence
>
> $$
> \tilde\kappa(A) = \overline{\det A}\;\theta(A), \qquad \text{in particular } \tilde\kappa = \theta \text{ on } SL(2, \mathbb C) .
> $$
>
> **4. The determinant of a product of two vectors.** For $u, v \in V$: $uv = (ue_0)(e_0v)$ and $e_0v = e_0(ve_0)e_0 = \kappa(ve_0)$. So $\phi(uv) = \tilde u\,\tilde\kappa(\tilde v)$, and $\det\phi(uv) = \det\tilde u\cdot\overline{\det\tilde v} = q(u)\,q(v)$, since $\det\tilde v = \det(v_\mu\bar\sigma^\mu) = v_\mu v^\mu = q(v)$ is real ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]], 2).
>
> **5. Spin(1,3)₀ lands in SL(2,ℂ).** Every $x \in \mathrm{Spin}(1,3)$ is $u_1u_2\cdots u_{2k}$ with $q(u_i) = \pm1$ (Def. §CB.13.6). Grouping the factors in pairs and using step 4 and $\det(AB) = \det A\det B$: $\det\phi(x) = \prod_iq(u_i) = \pm1$. On $\mathrm{Spin}(1,3)_0$, $\det\circ\phi$ is continuous with values in $\{\pm1\}$ and equals $1$ at $x = 1$; $\mathrm{Spin}(1,3)_0$ is connected ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]], 1), so $\det\phi(x) = 1$.
>
> **6. The action on four-vectors.** For $x \in \mathrm{Spin}(1,3)$ and $v \in V$, $\rho(x)v = xvx^{-1}$ (Theorem §CB.13.7, 2). Inserting $e_0e_0 = 1$: $(\rho(x)v)e_0 = x(ve_0)(e_0x^{-1}e_0) = x\,(ve_0)\,\kappa(x^{-1})$. Apply $\phi$, step 2 and step 3 with $d = \det\phi(x) = \pm1$ (so $\overline{\det\phi(x)^{-1}} = d$ and $\theta(\lambda^{-1}) = \lambda^\dagger$):
>
> $$
> \widetilde{\rho(x)v} = \lambda\,\tilde v\,\tilde\kappa(\lambda^{-1}) = d\,\lambda\,\tilde v\,\lambda^\dagger, \qquad \lambda = \phi(x) .
> $$
>
> For $x \in \mathrm{Spin}(1,3)_0$ ($d = 1$, step 5) this is $\tilde v \mapsto \lambda\tilde v\lambda^\dagger$, the first claim of part 2.
>
> **7. Comparison with π.** $X = v_\mu\sigma^\mu = v^0\mathbb 1 - v^i\sigma^i = \tilde\kappa(\tilde v)$ (step 2, real coefficients). Applying the automorphism $\tilde\kappa$ to step 6 ($d = 1$): $X \mapsto \tilde\kappa(\lambda)\,X\,\tilde\kappa(\lambda^\dagger) = \theta(\lambda)\,X\,\theta(\lambda^\dagger)$, and $\theta(\lambda^\dagger) = \lambda^{-1} = \theta(\lambda)^\dagger$. So $\rho(x)$ acts on $X$ as $X \mapsto \mu X\mu^\dagger$ with $\mu = \theta(\lambda)$, which is the definition of $\pi(\mu)$ (Theorem §CB.15.5): $\rho(x) = \pi(\theta(\phi(x)))$.
>
> **8. Onto SL(2,ℂ).** Let $\mu \in SL(2, \mathbb C)$. $\pi(\theta(\mu)) \in SO^+(1,3)$, and $SO^+(1,3)$ is the identity component of $O(1,3)$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], 2). $V = \mathbb R^{1,3}$ contains the negative definite plane $\operatorname{span}\{e_1, e_2\}$, so $\rho : \mathrm{Spin}(1,3)_0 \to SO^+(1,3)$ is onto and $-1 \in \mathrm{Spin}(1,3)_0$ (Theorem §CB.13.12). Pick $x$ with $\rho(x) = \pi(\theta(\mu))$; by step 7, $\pi(\theta(\phi(x))) = \pi(\theta(\mu))$, so $\theta(\phi(x)) = \pm\theta(\mu)$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-6|Theorem §CB.15.6]]) and $\phi(x) = \pm\mu$ ($\theta$ is a bijection with $\theta(-\lambda) = -\theta(\lambda)$). If the sign is $-$, replace $x$ by $-x \in \mathrm{Spin}(1,3)_0$. So $\phi(\mathrm{Spin}(1,3)_0) = SL(2, \mathbb C)$.
>
> **9. Part 1.** $\phi$ is an injective algebra homomorphism and a linear isomorphism of finite-dimensional spaces, so its restriction to $\mathrm{Spin}(1,3)_0$ is an injective group homomorphism, continuous with continuous inverse, onto $SL(2, \mathbb C)$ by step 8: an isomorphism of Lie groups ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]]).
>
> **10. The kernel and the Weyl matrices.** $\rho(x) = \mathbb 1$ iff $\theta(\phi(x)) = \pm\mathbb 1$ (step 7, Theorem §CB.15.6) iff $\phi(x) = \pm\mathbb 1$ iff $x = \pm1$. Since $\pi(\Lambda_L(\omega)) = e^\omega$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], 1), $\rho(x) = e^\omega$ iff $\theta(\phi(x)) = \pm\Lambda_L(\omega)$ iff $\phi(x) = \pm\theta(\Lambda_L(\omega)) = \pm\Lambda_R(\omega)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], 2). Finally $\phi' = \tilde\kappa\circ\phi$ is a real-algebra isomorphism with $\phi'(f_i) = -\sigma^i$ and $\phi'(xe_0) = \tilde\kappa(\tilde x) = X$, equal to $\theta\circ\phi$ on $\mathrm{Spin}(1,3)_0$ (step 3), so $\rho = \pi\circ\phi'$ there.
>
> **11. Part 3.** By step 5, $\phi(\mathrm{Spin}(1,3)) \subset \{\det = \pm1\}$. $e_0e_1 \in \mathrm{Spin}(1,3)$, $e_0e_1 = -e_1e_0 = -f_1$, $\phi(e_0e_1) = -\sigma^1$ with determinant $-1$, and $(e_0e_1)^2 = -e_0e_0e_1e_1 = 1$. If $y \in \mathrm{Spin}(1,3)$ has $\det\phi(y) = -1$, then $e_0e_1y \in \mathrm{Spin}(1,3)$ has determinant $1$, so $\phi(e_0e_1y) \in SL(2, \mathbb C) = \phi(\mathrm{Spin}(1,3)_0)$ and, $\phi$ being injective, $e_0e_1y \in \mathrm{Spin}(1,3)_0$, i.e. $y \in e_0e_1\mathrm{Spin}(1,3)_0$. The two pieces are the preimages of $\det = 1$ and $\det = -1$, disjoint, open and closed, each connected (homeomorphic to $\mathrm{Spin}(1,3)_0$); their images under $\phi$ fill $\{\det = \pm1\}$ ($\phi(e_0e_1)SL(2, \mathbb C) = \{\det = -1\}$). By Theorem §CB.13.7, 2, $\rho(e_0e_1) = r_{e_0}r_{e_1}$, the product of the reflections $e_0 \mapsto -e_0$ and $e_1 \mapsto -e_1$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-4|Theorem §CB.13.4]]): $\operatorname{diag}(-1, -1, 1, 1)$, with determinant $+1$ and $\Lambda^0{}_0 = -1$, the same signs as $\mathcal P\mathcal T = -\mathbb 1$, so it lies in $\mathcal P\mathcal T\cdot SO^+(1,3)$ (Theorem §CB.2.12, 1–2), and $\rho(e_0e_1\mathrm{Spin}(1,3)_0) = \rho(e_0e_1)\,SO^+(1,3) = \mathcal P\mathcal T\cdot SO^+(1,3)$.
>
> **What the proof shows**
> - The Clifford route and the course's route reach the same group, but the natural identifications differ by the automorphism $\theta(\lambda) = (\lambda^\dagger)^{-1}$, which exchanges $\Lambda_L$ and $\Lambda_R$. ⚑ By-product: "which matrix is $\lambda$" is a convention, fixed in the course by building $\pi$ on $X = x_\mu\sigma^\mu$; the Clifford algebra with $f_i \mapsto \sigma^i$ builds it on $\bar X$. Every later statement that names $(\frac12, 0)$ fixes the convention (Theorem §CB.16.5, Theorem §CB.17.3).
> - Step 6 for $d = -1$ shows that the other component acts by $\tilde v \mapsto -\lambda\tilde v\lambda^\dagger$: the minus sign reverses time, as $\mathcal P\mathcal T$ does.
> - Used next: the Lie algebra version (Theorem §CB.15.10) and the Dirac module restricted to $\mathrm{Spin}(1,3)_0$ (Theorem §CB.17.3).

^pf-cb-15-9

*Uses:* [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-8|Theorem §CB.15.8]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-6|Def. §CB.13.6]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-4|Theorem §CB.13.4]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-7|Theorem §CB.13.7]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-12|Theorem §CB.13.12]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-15|Theorem §CB.7.15]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-22|Theorem §CB.0.22]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-5|Theorem §CB.15.5]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-6|Theorem §CB.15.6]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-12|Theorem §CB.2.12]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]]

> [!theorem] Theorem §CB.15.10: The Three Lie Algebras Agree
> Under $\phi$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-8|Theorem §CB.15.8]]), $\mathfrak{spin}(1,3)$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-13|Def. §CB.13.13]]) maps isomorphically onto $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ ([[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^def-cb-5-7|Def. §CB.5.7]]): $\frac12e_ie_j = -\frac12f_if_j \mapsto -\frac i2\varepsilon_{ijk}\sigma^k$ (rotations) and $\frac12e_ie_0 \mapsto \frac12\sigma^i$ (boosts). The differential $\rho_\ast$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-14|Theorem §CB.13.14]]) is $\rho_\ast(\frac12e_\mu e_\nu) = M_{\mu\nu} = g_{\mu\alpha}g_{\nu\beta}M^{\alpha\beta}$, the generators of [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-2|Def. §CB.4.2]] with lowered indices; so $\rho_\ast\circ\phi^{-1}$ sends $-\frac i2\sigma^k \mapsto -iJ_k$ and $\frac12\sigma^k \mapsto -iK_k$ ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-4|Def. §CB.4.4]]). It equals $\pi_\ast\circ\theta_\ast$, with $\pi_\ast$ the isomorphism of [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-8|Theorem §CB.5.8]] ($-\frac i2\sigma^k \mapsto -iJ_k$, $-\frac12\sigma^k \mapsto -iK_k$) and $\theta_\ast(Y) = -Y^\dagger$ the differential of $\theta(\lambda) = (\lambda^\dagger)^{-1}$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]]).
>
> *Source: written here*

^thm-cb-15-10

> [!proof]- Proof
> **1. A basis.** $\mathfrak{spin}(1,3)$ is spanned by the six products $e_\mu e_\nu$, $\mu < \nu$ (Def. §CB.13.13), and it is the Lie algebra of $\mathrm{Spin}(1,3)$ (Theorem §CB.13.14, 1).
>
> **2. The images.** $\phi(e_ie_0) = \phi(f_i) = \sigma^i$. For $i \ne j$, $e_ie_j = -f_if_j$ (Theorem §CB.15.8, Proof, step 2), and $\sigma^i\sigma^j = i\varepsilon_{ijk}\sigma^k$ for $i \ne j$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], 3), so $\phi(\frac12e_ie_j) = -\frac12\sigma^i\sigma^j = -\frac i2\varepsilon_{ijk}\sigma^k$.
>
> **3. An isomorphism onto 𝔰𝔩(2,ℂ)_ℝ.** The images $\frac12\sigma^k$, $-\frac i2\sigma^k$ ($k = 1, 2, 3$) are a real basis of the traceless matrices, because $\sigma^1, \sigma^2, \sigma^3$ are a complex basis of them (Theorem §CB.0.21, 4). These form $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$, of real dimension $6$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]]). $\phi$ is injective and multiplicative, so it preserves commutators, and its restriction is a Lie algebra isomorphism $\mathfrak{spin}(1,3) \cong \mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ — consistently with $\phi(\mathrm{Spin}(1,3)_0) = SL(2, \mathbb C)$ (Theorem §CB.15.9, 1).
>
> **4. The differential of ρ in components.** By Theorem §CB.13.14, 2, $\rho_\ast(\frac12e_\mu e_\nu)(v) = B(e_\nu, v)e_\mu - B(e_\mu, v)e_\nu = v_\nu e_\mu - v_\mu e_\nu$, i.e. the matrix $(\rho_\ast(\frac12e_\mu e_\nu))^\rho{}_\sigma = \delta^\rho_\mu g_{\nu\sigma} - \delta^\rho_\nu g_{\mu\sigma}$. Lowering both labels of $(M^{\alpha\beta})^\rho{}_\sigma = g^{\alpha\rho}\delta^\beta_\sigma - g^{\beta\rho}\delta^\alpha_\sigma$ (Def. §CB.4.2): $g_{\mu\alpha}g_{\nu\beta}(M^{\alpha\beta})^\rho{}_\sigma = \delta^\rho_\mu g_{\nu\sigma} - \delta^\rho_\nu g_{\mu\sigma}$. So $\rho_\ast(\frac12e_\mu e_\nu) = M_{\mu\nu}$.
>
> **5. Rotations and boosts.** For spatial $i, j$: $M_{ij} = g_{ii}g_{jj}M^{ij} = M^{ij} = -i\mathcal J^{ij} = -i\varepsilon_{ijk}J_k$, since $J_k = \frac12\varepsilon_{klm}\mathcal J^{lm}$ gives $\mathcal J^{ij} = \varepsilon_{ijk}J_k$ (Def. §CB.4.4). With step 2: $\rho_\ast\phi^{-1}(-\frac i2\varepsilon_{ijk}\sigma^k) = -i\varepsilon_{ijk}J_k$, i.e. $-\frac i2\sigma^k \mapsto -iJ_k$. For boosts: $M_{k0} = g_{kk}g_{00}M^{k0} = -M^{k0} = M^{0k} = -i\mathcal J^{0k} = -iK_k$, and $\phi(\frac12e_ke_0) = \frac12\sigma^k$, so $\frac12\sigma^k \mapsto -iK_k$. Check on $v$: $\rho_\ast(\frac12e_ke_0)$ sends $e_0 \mapsto e_k$ and $e_k \mapsto e_0$, the generator of a boost along $+e_k$.
>
> **6. Comparison with the differential of π.** $\theta$ is a continuous homomorphism of $SL(2, \mathbb C)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-7|Theorem §CB.16.7]], Derivation, step 1), and $\theta(e^{sY}) = ((e^{sY})^\dagger)^{-1} = e^{-sY^\dagger}$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], 2 and 4), so $\theta_\ast(Y) = \frac{d}{ds}e^{-sY^\dagger}\big|_0 = -Y^\dagger$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]). Then $\theta_\ast(-\frac i2\sigma^k) = -\frac i2\sigma^k$ and $\theta_\ast(\frac12\sigma^k) = -\frac12\sigma^k$, and Theorem §CB.5.8 gives $\pi_\ast\theta_\ast(-\frac i2\sigma^k) = -iJ_k$, $\pi_\ast\theta_\ast(\frac12\sigma^k) = -iK_k$: the same values as step 5 on a basis, so $\rho_\ast\circ\phi^{-1} = \pi_\ast\circ\theta_\ast$. (This is also the chain rule applied to $\rho = \pi\circ\theta\circ\phi$, Theorem §CB.15.9, 2.)
>
> **What the proof shows**
> - $\rho_\ast(\frac12e_\mu e_\nu) = M_{\mu\nu}$: in the Clifford algebra the generator of the $\mu\nu$-plane is half the product of the two basis vectors, with the metric lowering the labels. Hence $\exp(\frac14\omega^{\mu\nu}e_\mu e_\nu)$ covers $e^\omega = \exp(\frac12\omega_{\mu\nu}M^{\mu\nu})$, used in Theorem §CB.17.3.
> - ⚑ By-product: rotations are the same through $\phi$ and through the course's $\pi$; boosts differ by a sign. That sign is the automorphism $\theta$, i.e. the exchange of $\Lambda_L$ and $\Lambda_R$ (Theorem §CB.15.9, 2).

^pf-cb-15-10

*Uses:* [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-13|Def. §CB.13.13]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-14|Theorem §CB.13.14]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-8|Theorem §CB.15.8]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-2|Def. §CB.4.2]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-4|Def. §CB.4.4]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-8|Theorem §CB.5.8]]

> [!remark]- Connections
> - The two routes to $SL(2, \mathbb C)$ meet at Theorem §CB.15.8: the Hermitian matrix $x^0 + \mathbf x\cdot\boldsymbol\sigma = x_\mu\bar\sigma^\mu$ is the Clifford product $x\,e_0$, and $\lambda\tilde x\lambda^\dagger$ is conjugation in the Clifford algebra read through $e_0$. The course builds its covering on $x_\mu\sigma^\mu$ instead; the two differ by $\lambda \mapsto (\lambda^\dagger)^{-1}$ (Theorem §CB.15.9, 2), which is why the Clifford identification calls $\Lambda_R$ what the course calls $\Lambda_L$.
> - The covering $SL(2, \mathbb C) \to SO^+(1,3)$ restricts on $SU(2)$ to Quantum Mechanics' covering of $SO(3)$, and the polar decomposition $\lambda = e^hU$ is the spinor image of "boost times rotation" — [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-6|REL Theorem §B1.2.6]].
> - **Used in**: Theorems §CB.15.1–§CB.15.2 — [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-2|Def. §CB.1.2]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-7|Theorem §CB.16.7]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]; Theorem §CB.15.3 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]]), [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (embedded; cited in [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-5|Theorem §C5a.5.5]]); Theorem §CB.15.4 — [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]] (its derivation; embedded in [[§C1a.4 The Lorentz Group|§C1a.4]]), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded); Theorem §CB.15.5 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]]); Theorem §CB.15.6 — [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded; cited in [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-4|§C3.3, Remark: Why a spinor's matrix is fixed only up to sign]]), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded); Theorem §CB.15.7 — [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded; cited in [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-4|§C3.3, Remark: Why a spinor's matrix is fixed only up to sign]]), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded), [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]] (cited in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-2|§C5a.0, Remark: What the Clifford relation induces]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-3|§C5a.0, Remark: Four jobs of the γ's]]); §CB.15, Remark: The rotation story, one level up — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded); Theorems §CB.15.8–§CB.15.10 — [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-5|Theorem §CB.15.5]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-6|Theorem §CB.15.6]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-7|Theorem §CB.15.7]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]].
