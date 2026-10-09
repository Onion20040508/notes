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

What is the spin group of Minkowski space? The course reaches $SL(2, \mathbb C)$ through Hermitian $2\times2$ matrices ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]]–[[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]]) and the representations $(j_+, j_-)$ through the complexified algebra ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]). The course's route, with its proofs, is stated here first (the covering map, its kernel and the double cover), and the Clifford route is identified with it in Theorem §CB.15.12. Before both, this section complexifies the real Lie algebra $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ (two copies of $\mathfrak{sl}(2, \mathbb C)$) and splits its representations into a complex-linear and an antilinear part; then it gives the Clifford route: $\mathrm{Cl}^0(1,3) \cong \mathrm{Cl}(3,0) \cong M_2(\mathbb C)$, so $\mathrm{Spin}(1,3)_0 \cong SL(2, \mathbb C)$, with $\rho$ the course's covering map up to the automorphism $\lambda \mapsto (\lambda^\dagger)^{-1}$. The finite-dimensional representations of $SL(2, \mathbb C)$ (pairs of $\mathfrak{sl}(2, \mathbb C)$-representations, the $(j_+, j_-)$, and which of them descend to $SO^+(1,3)$) follow in [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)|§CB.16]]. It is the four-dimensional sequel of [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half|§CB.14]], using [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification|§CB.3]]–[[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra|§CB.5]] (real forms, $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$) and [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.13]].

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
> - ⚑ By-product: a representation of $SL(2, \mathbb C)$ regarded as a real group is labelled by two complex-linear pieces, one "holomorphic", one "antiholomorphic"; through Theorem §CB.5.8 these become the two commuting angular momenta behind the labels $(j_+, j_-)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]]; which of the defining representation and its conjugate is called $(\frac12, 0)$ is a convention fixed there).
> - The decomposition needs $W$ complex; antilinearity of $\rho_2$ is relative to the complex structure of $\mathfrak{sl}(2, \mathbb C)$, not of $W$.

^pf-cb-15-2

*Uses:* [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-9|Theorem §CB.3.9]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-1|Theorem §CB.15.1]]

## Four-vectors as Hermitian matrices

The course reaches $SL(2, \mathbb C) \to SO^+(1,3)$ without the Clifford algebra, through four-vectors as Hermitian $2\times2$ matrices (PHY 513 Lecture 8, Part C; Yu, Exercise 3.7; the user's PHY 513 notes, Ch. 8 §8.2; first written in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]). Both routes are kept; Theorem §CB.15.12 below identifies them.

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
> - The Minkowski interval is a determinant, and the forward light cone is the cone of positive semidefinite matrices. Any operation on $X$ that preserves Hermiticity and the determinant therefore preserves the interval: that is how $SL(2, \mathbb C)$ will act (Theorem §CB.15.4).
> - The spatial part alone, $\mathbf x\cdot\boldsymbol\sigma$ (traceless Hermitian), is the dictionary of the rotation case, with $\det(\mathbf x\cdot\boldsymbol\sigma) = -|\mathbf x|^2$ ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]).

^der-cb-15-3

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-20|Def. §CB.0.20]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-22|Theorem §CB.0.22]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]]

## The covering map SL(2,ℂ) → SO⁺(1,3)

That $SL(2, \mathbb C)$ is connected and simply connected, with the polar decomposition $\lambda = e^hU$, is [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-9|Theorem §CB.9.9]], moved to [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan|§CB.9]] in the CB ordering pass (after the topology of $SU(2)$), because the Clebsch–Gordan series for $SL(2, \mathbb C)$ uses it.

> [!theorem] Theorem §CB.15.4: Every Element of SL(2, C) Gives a Lorentz Transformation
> For $\lambda \in SL(2, \mathbb C)$ define $\Lambda(\lambda)$ through the dictionary $x \leftrightarrow x_\mu\sigma^\mu$ of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]] by
>
> $$
> \lambda\,(x_\mu\sigma^\mu)\,\lambda^\dagger = \bigl(\Lambda(\lambda)x\bigr)_\mu\sigma^\mu, \qquad\text{i.e.}\qquad \Lambda(\lambda)^\mu{}_\nu = \tfrac12\operatorname{tr}\bigl(\lambda\sigma_\nu\lambda^\dagger\bar\sigma^\mu\bigr) .
> $$
>
> Then $\Lambda(\lambda)$ is a proper orthochronous Lorentz transformation, $\Lambda(\lambda) \in SO^+(1,3)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]), $\Lambda(\lambda_1\lambda_2) = \Lambda(\lambda_1)\Lambda(\lambda_2)$, $\Lambda(\mathbb 1) = \mathbb 1$, and $\lambda \mapsto \Lambda(\lambda)$ is continuous: a continuous homomorphism $\pi: SL(2, \mathbb C) \to SO^+(1,3)$.
>
> *Source: Yu Exercise 3.7(b)–(c), eqs. (3.261)–(3.264), (d) · the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit", parts (b), (d))*

^thm-cb-15-4

> [!derivation]- Derivation
> **1. A real linear map.** For Hermitian $X$, $(\lambda X\lambda^\dagger)^\dagger = \lambda X^\dagger\lambda^\dagger = \lambda X\lambda^\dagger$ is Hermitian, so by Theorem §CB.15.3 it is $X'$ for a unique real $x'$. $X$ is linear in $x$ and $X \mapsto \lambda X\lambda^\dagger$ is linear, so $x' = \Lambda(\lambda)x$ with $\Lambda(\lambda)$ a real $4\times4$ matrix. Its entries: $X = x_\nu\sigma^\nu = x^\nu\sigma_\nu$, and by the inverse formula $x'^\mu = \frac12\operatorname{tr}(\lambda x^\nu\sigma_\nu\lambda^\dagger\bar\sigma^\mu)$, which gives the trace formula; it is a polynomial in the entries of $\lambda$ and $\lambda^{\ast}$, hence continuous.
>
> **2. The interval is preserved.** $\det X' = \det\lambda\,\det X\,\det\lambda^\dagger = |\det\lambda|^2\det X = \det X$, i.e. $x'^2 = x^2$ (Theorem §CB.15.3). A linear map preserving the quadratic form preserves the bilinear form, by polarization: $x\cdot y = \frac12\bigl((x + y)^2 - x^2 - y^2\bigr)$. So $\Lambda(\lambda)^{\mathsf T}g\Lambda(\lambda) = g$: $\Lambda(\lambda) \in O(1,3)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]).
>
> **3. Homomorphism.** $(\lambda_1\lambda_2)X(\lambda_1\lambda_2)^\dagger = \lambda_1(\lambda_2X\lambda_2^\dagger)\lambda_1^\dagger$: first $x \mapsto \Lambda(\lambda_2)x$, then $\Lambda(\lambda_1)$. By injectivity of $x \mapsto X$, $\Lambda(\lambda_1\lambda_2) = \Lambda(\lambda_1)\Lambda(\lambda_2)$. For $\lambda = \mathbb 1$, $X' = X$, so $\Lambda(\mathbb 1) = \mathbb 1$.
>
> **4. Proper and orthochronous.** $SL(2, \mathbb C)$ is path-connected (Theorem §CB.9.9) and $\pi$ is continuous (step 1), so the image $\pi(SL(2, \mathbb C))$ is a path-connected subset of $O(1,3)$ containing $\pi(\mathbb 1) = \mathbb 1$. It therefore lies in the component of the identity, which is $SO^+(1,3)$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], 2).
>
> **What the derivation shows**
> - Only $|\det\lambda| = 1$ was used for step 2; Yu then fixes the phase by $\det\lambda = 1$, since $\lambda$ and $e^{i\alpha}\lambda$ give the same $\Lambda$. The group $SL(2, \mathbb C)$ is what remains after that redundancy is removed, up to the sign left over in Theorem §CB.15.5.
> - Determinant $+1$ and $\Lambda^0{}_0 > 0$ were not checked by hand: connectedness does it. Directly, $\Lambda^0{}_0 = \frac12\operatorname{tr}(\lambda\lambda^\dagger) > 0$.
> - Used next: the kernel (Theorem §CB.15.5), the link to the parameters $\omega$ (Theorem §C5a.4.2).

^der-cb-15-4

*Uses:* [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-9|Theorem §CB.9.9]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]]

> [!theorem] Theorem §CB.15.5: The Kernel Is ±1
> For the homomorphism $\pi$ of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]], $\pi(\lambda) = \mathbb 1$ iff $\lambda = \pm\mathbb 1$. Hence $\pi(\lambda) = \pi(\lambda')$ iff $\lambda' = \pm\lambda$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit", part (c)) · Yu Exercise 3.7(d) (paragraph after (3.265))*

^thm-cb-15-5

> [!derivation]- Derivation
> **1. ±1 are in the kernel.** $(\pm\mathbb 1)X(\pm\mathbb 1)^\dagger = X$, and $\det(\pm\mathbb 1) = 1$.
>
> **2. An element of the kernel is unitary.** If $\pi(\lambda) = \mathbb 1$, then $\lambda X\lambda^\dagger = X$ for every Hermitian $X$. Take $X = \mathbb 1$ ($x = (1, \mathbf 0)$): $\lambda\lambda^\dagger = \mathbb 1$, so $\lambda^\dagger = \lambda^{-1}$.
>
> **3. It commutes with everything.** With $\lambda^\dagger = \lambda^{-1}$ the condition reads $\lambda X\lambda^{-1} = X$, i.e. $\lambda X = X\lambda$, for every Hermitian $X$, in particular for $\sigma^1, \sigma^2, \sigma^3$. Together with $\mathbb 1$ these span $M_2(\mathbb C)$ over $\mathbb C$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], part 4), so $\lambda$ commutes with every $2\times2$ matrix; taking the matrix units $E_{12}$, $E_{21}$ forces $\lambda = c\mathbb 1$ (the same conclusion as Schur's lemma, [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-4|Theorem §CB.6.4]]).
>
> **4. The scalar.** $\det(c\mathbb 1) = c^2 = 1$ gives $c = \pm1$.
>
> **5. Fibres.** $\pi(\lambda) = \pi(\lambda')$ iff $\pi(\lambda'\lambda^{-1}) = \mathbb 1$ (homomorphism, Theorem §CB.15.4) iff $\lambda'\lambda^{-1} = \pm\mathbb 1$.
>
> **What the derivation shows**
> - The sign ambiguity is the only one: two spinor matrices $\pm\lambda$ for each Lorentz transformation. This is the matrix origin of "a spinor's matrix is fixed only up to sign" ([[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-4|§C3.3, Remark: Why a spinor's matrix is fixed only up to sign]]).
> - The argument is that of the rotation case ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], 3), with $X = \mathbb 1$ added to force unitarity first.

^der-cb-15-5

*Uses:* [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]]

The double-cover theorem below is proved with the Weyl matrices, the explicit lifts of the Lorentz exponentials to $SL(2, \mathbb C)$, and their covering property. They were first written in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]], where they are the matrices of the course's left- and right-handed spinors; they are restated here with their proofs (CB ordering pass, 2026-10-08; the three boxes of §C5a.4 were embedded here before):

> [!definition] Definition §CB.15.6: The Weyl Matrices
> For real Lorentz parameters $\omega_{\mu\nu} = -\omega_{\nu\mu}$ ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-2|Def. §CB.4.2]]), with angles $\theta_i = \frac12\varepsilon_{ijk}\omega_{jk}$ and rapidities $\eta_i = \omega_{0i}$ ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-4|Def. §CB.4.4]]), and the Pauli matrices of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-19|Def. §CB.0.19]], the **left- and right-handed Weyl matrices** are
>
> $$
> \Lambda_L(\omega) = \exp\Bigl(-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma\Bigr) = e^{-i(\boldsymbol\theta - i\boldsymbol\eta)\cdot\boldsymbol\sigma/2}, \qquad \Lambda_R(\omega) = \exp\Bigl(-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma\Bigr) = e^{-i(\boldsymbol\theta + i\boldsymbol\eta)\cdot\boldsymbol\sigma/2} .
> $$
>
> *Source: PHY 513 Lecture 8, Part C ("$\psi_L \to e^{-i\vec\theta\cdot\vec\sigma/2 - \vec\eta\cdot\vec\sigma/2}\psi_L$, $\psi_R \to e^{-i\vec\theta\cdot\vec\sigma/2 + \vec\eta\cdot\vec\sigma/2}\psi_R$") · PS §3.2, eqs. (3.36)–(3.37) · the user's PHY 513 notes, Ch. 8 §8.2 ($U_L$, $U_R$, eq. (weyllaws)) · Yu Exercise 3.7(c) · the course's version: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]], the same matrices, introduced there as the matrices of the representations $(\frac12, 0)$ and $(0, \frac12)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]; which one is $(\frac12, 0)$ depends on the sign convention for $\mathbf K$, [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]]).*

^def-cb-15-6

> [!theorem] Theorem §CB.15.7: The Weyl Matrices Lie in SL(2, C)
> For the Weyl matrices of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^def-cb-15-6|Def. §CB.15.6]] and every $\omega$:
> 1. $\det\Lambda_L(\omega) = \det\Lambda_R(\omega) = 1$, so both lie in $SL(2, \mathbb C)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-2|Def. §CB.1.2]]);
> 2. $\Lambda_R(\omega) = \bigl(\Lambda_L(\omega)^\dagger\bigr)^{-1}$;
> 3. $\Lambda_L(\omega)^* = \sigma^2\,\Lambda_R(\omega)\,\sigma^2$;
> 4. for a rotation ($\boldsymbol\eta = 0$) $\Lambda_L = \Lambda_R \in SU(2)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]); for a pure boost ($\boldsymbol\theta = 0$) $\Lambda_L = e^{-\boldsymbol\eta\cdot\boldsymbol\sigma/2}$ and $\Lambda_R = e^{+\boldsymbol\eta\cdot\boldsymbol\sigma/2}$ are Hermitian and positive, not unitary.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "Index calculus for Weyl spinors": "Both have unit determinant", "$U_R = (U_L^\dagger)^{-1}$"; Derivation "The two halves are irreducible, inequivalent, and related by conjugation") · the user's pre-course notes, §5.2 (Remark "SL(2,C) made explicit") · PS eq. (3.38) · the course's version: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], the same statement.*

^thm-cb-15-7

> [!proof]- Proof
> *The derivation of Theorem §C5a.4.1, with the citations replaced by their CB homes.* Write $\Lambda_L = e^{A_L}$, $\Lambda_R = e^{A_R}$ with $A_L = -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma$ and $A_R = -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma$ ($\boldsymbol\theta$, $\boldsymbol\eta$ real).
>
> **1. Determinant.** $\det e^A = e^{\operatorname{tr}A}$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-6|Theorem §CB.1.6]]). The Pauli matrices are traceless ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], 4), so $\operatorname{tr}A_L = \operatorname{tr}A_R = 0$ and both determinants are $e^0 = 1$.
>
> **2. Adjoint and inverse.** Term by term in the exponential series, $(e^A)^\dagger = e^{A^\dagger}$; and $(e^A)^{-1} = e^{-A}$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]]). The $\sigma^i$ are Hermitian and $\boldsymbol\theta$, $\boldsymbol\eta$ real, so $A_L^\dagger = +\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma$: the adjoint flips the sign of the rotation term only. Then $(\Lambda_L^\dagger)^{-1} = e^{-A_L^\dagger} = e^{-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma} = e^{A_R} = \Lambda_R$.
>
> **3. Complex conjugate.** $(e^A)^{\ast} = e^{A^{\ast}}$ term by term, and $A_L^{\ast} = +\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma^{\ast} - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma^{\ast}$. By [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-22|Theorem §CB.0.22]], 3, $\sigma^2(\sigma^i)^{\ast}\sigma^2 = -\sigma^i$, so $\sigma^2A_L^{\ast}\sigma^2 = -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma = A_R$. Since $(\sigma^2)^2 = \mathbb 1$, $(\sigma^2Y\sigma^2)^n = \sigma^2Y^n\sigma^2$ for every $n$, hence $\sigma^2e^{Y}\sigma^2 = e^{\sigma^2Y\sigma^2}$. With $Y = A_L^{\ast}$: $\sigma^2\Lambda_L^{\ast}\sigma^2 = e^{A_R} = \Lambda_R$, i.e. $\Lambda_L^{\ast} = \sigma^2\Lambda_R\sigma^2$. ⚑ By-product: $\sigma^2\psi_L^{\ast}$ transforms like $\psi_R$, since $\sigma^2\psi_L^{\ast} \to \sigma^2\Lambda_L^{\ast}\psi_L^{\ast} = \Lambda_R\,\sigma^2\psi_L^{\ast}$; this is the spin-½ case of [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-13|Theorem §CB.16.13]].
>
> **4. Rotations and boosts.** For $\boldsymbol\eta = 0$, $A_L = A_R = -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma$ is anti-Hermitian and traceless, so $e^{A_L}$ is unitary of determinant $1$: an element of $SU(2)$, the matrix $\exp(-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma)$ of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-19|Theorem §CB.1.19]], 3. For $\boldsymbol\theta = 0$, $A_L = -\frac12\boldsymbol\eta\cdot\boldsymbol\sigma$ is Hermitian with eigenvalues $\mp\frac12|\boldsymbol\eta|$ (by $(\hat{\boldsymbol\eta}\cdot\boldsymbol\sigma)^2 = \mathbb 1$ and trace $0$, Theorem §CB.0.21, 3–4), so $e^{A_L}$ is Hermitian with eigenvalues $e^{\mp|\boldsymbol\eta|/2} > 0$, unitary only for $\boldsymbol\eta = 0$.
>
> **What the proof shows**
> - Both Weyl matrices take values in the same group $SL(2, \mathbb C)$. They differ by the automorphism $\theta(\lambda) = (\lambda^\dagger)^{-1}$ of that group ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^lem-cb-9-11|Lemma §CB.9.11]], 2), which is the identity on $SU(2)$ (rotations) and inverts the Hermitian part (boosts).
> - Equivalence: this is [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]]; there the unit determinant is what makes $\varepsilon$ an invariant of the Weyl spinors (the course's Theorem §C5a.5.3).

^pf-cb-15-7

*Uses:* [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^def-cb-15-6|Def. §CB.15.6]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-6|Theorem §CB.1.6]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-22|Theorem §CB.0.22]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-19|Theorem §CB.1.19]]

> [!theorem] Theorem §CB.15.8: The Weyl Matrices Cover the Vector Representation
> For the Weyl matrices $\Lambda_L(\omega)$, $\Lambda_R(\omega)$ of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^def-cb-15-6|Def. §CB.15.6]] and every $\omega$, with $\Lambda = e^{\omega}$ the vector-representation matrix of the same parameters ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-3|Theorem §CB.4.3]]):
> 1. $\Lambda_L(\omega)\,(x_\mu\sigma^\mu)\,\Lambda_L(\omega)^\dagger = (\Lambda x)_\mu\sigma^\mu$, i.e. $\pi(\Lambda_L(\omega)) = e^{\omega}$ ($\pi$ of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]]); and $\Lambda_R(\omega)\,(x_\mu\bar\sigma^\mu)\,\Lambda_R(\omega)^\dagger = (\Lambda x)_\mu\bar\sigma^\mu$.
> 2. Equivalently, $\bar\sigma^\mu$ and $\sigma^\mu$ are invariant under the Weyl matrices:
>
> $$
> \Lambda_L^\dagger\,\bar\sigma^\mu\,\Lambda_L = \Lambda^\mu{}_\nu\,\bar\sigma^\nu, \qquad \Lambda_R^\dagger\,\sigma^\mu\,\Lambda_R = \Lambda^\mu{}_\nu\,\sigma^\nu .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The left-handed Weyl matrices are this covering", eq. (SL2Ccover); checked numerically there) · Yu Exercise 3.7(e), eqs. (3.267)–(3.268) (rotation about z) · the course's version: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], the same statement.*

^thm-cb-15-8

> [!proof]- Proof
> *The derivation of Theorem §C5a.4.2, with the citations replaced by their CB homes.* Write $\Phi(x) = x_\mu\sigma^\mu$, $\bar\Phi(x) = x_\mu\bar\sigma^\mu$, and $\Lambda_L(s\omega) = e^{sA_L}$, $A_L = -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma$ (the exponent is linear in $\omega$).
>
> **1. The vector side, infinitesimally.** By [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-3|Theorem §CB.4.3]], $\Lambda = e^{\omega}$ with $(\omega x)^\mu = \omega^\mu{}_\nu x^\nu$. Its components, with $\omega^0{}_i = \omega_{0i} = \eta_i$, $\omega^i{}_0 = g^{ii}\omega_{i0} = \eta_i$ and $\omega^i{}_j = -\omega_{ij} = -\varepsilon_{ijk}\theta_k$:
>
> $$
> (\omega x)^0 = \boldsymbol\eta\cdot\mathbf x, \qquad (\omega x)^i = \eta_ix^0 - \varepsilon_{ijk}\theta_kx^j = \eta_ix^0 + (\boldsymbol\theta\times\mathbf x)_i ,
> $$
>
> the last step by relabelling $j \leftrightarrow k$ and $\varepsilon_{ikj} = -\varepsilon_{ijk}$. Hence $\Phi(\omega x) = (\omega x)^0\mathbb 1 - (\omega x)\cdot\boldsymbol\sigma = (\boldsymbol\eta\cdot\mathbf x)\mathbb 1 - (x^0\boldsymbol\eta + \boldsymbol\theta\times\mathbf x)\cdot\boldsymbol\sigma$.
>
> **2. The spinor side, infinitesimally.** Define the linear map $L(M) = A_LM + MA_L^\dagger$ on $M_2(\mathbb C)$. With $A_L^\dagger = \frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma$,
>
> $$
> L(\Phi(x)) = -\tfrac i2\bigl[\boldsymbol\theta\cdot\boldsymbol\sigma, \Phi(x)\bigr] - \tfrac12\bigl\{\boldsymbol\eta\cdot\boldsymbol\sigma, \Phi(x)\bigr\} .
> $$
>
> With $\Phi(x) = x^0\mathbb 1 - \mathbf x\cdot\boldsymbol\sigma$ and the vector form of the Pauli product, $(\mathbf a\cdot\boldsymbol\sigma)(\mathbf b\cdot\boldsymbol\sigma) = (\mathbf a\cdot\mathbf b)\mathbb 1 + i(\mathbf a\times\mathbf b)\cdot\boldsymbol\sigma$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], 3): $[\boldsymbol\theta\cdot\boldsymbol\sigma, \mathbf x\cdot\boldsymbol\sigma] = 2i(\boldsymbol\theta\times\mathbf x)\cdot\boldsymbol\sigma$ and $\{\boldsymbol\eta\cdot\boldsymbol\sigma, \mathbf x\cdot\boldsymbol\sigma\} = 2(\boldsymbol\eta\cdot\mathbf x)\mathbb 1$; $\mathbb 1$ commutes with everything and $\{\boldsymbol\eta\cdot\boldsymbol\sigma, x^0\mathbb 1\} = 2x^0\boldsymbol\eta\cdot\boldsymbol\sigma$. So
>
> $$
> L(\Phi(x)) = -\tfrac i2\bigl(-2i(\boldsymbol\theta\times\mathbf x)\cdot\boldsymbol\sigma\bigr) - \tfrac12\bigl(2x^0\boldsymbol\eta\cdot\boldsymbol\sigma - 2(\boldsymbol\eta\cdot\mathbf x)\mathbb 1\bigr) = (\boldsymbol\eta\cdot\mathbf x)\mathbb 1 - (x^0\boldsymbol\eta + \boldsymbol\theta\times\mathbf x)\cdot\boldsymbol\sigma ,
> $$
>
> using $-\frac i2\cdot(-2i) = -1$. Comparing with step 1: $L\circ\Phi = \Phi\circ\omega$ as maps $\mathbb R^4 \to M_2(\mathbb C)$.
>
> **3. Exponentiate.** Left multiplication $\ell(M) = A_LM$ and right multiplication $r(M) = MA_L^\dagger$ commute as linear maps of $M_2(\mathbb C)$ ($A_L(MA_L^\dagger) = (A_LM)A_L^\dagger$), so $e^{s(\ell + r)} = e^{s\ell}e^{sr}$ (the binomial argument of [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^der-cb-5-3|Derivation §CB.5.3]], step 3), i.e. $e^{sL}(M) = e^{sA_L}Me^{sA_L^\dagger} = \Lambda_L(s\omega)M\Lambda_L(s\omega)^\dagger$ (with $(e^{sA_L})^\dagger = e^{sA_L^\dagger}$). Iterating step 2, $L^n\circ\Phi = \Phi\circ\omega^n$ for every $n$, so summing the series (both converge absolutely; $\Phi$ is linear) $e^{sL}\circ\Phi = \Phi\circ e^{s\omega}$. At $s = 1$: $\Lambda_L(\omega)\Phi(x)\Lambda_L(\omega)^\dagger = \Phi(e^\omega x)$, part 1 for $\Lambda_L$. By the definition of $\pi$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]]), $\pi(\Lambda_L(\omega)) = e^{\omega}$.
>
> **4. The right-handed matrices.** $A_R = -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma$ and $\bar\Phi(x) = x^0\mathbb 1 + \mathbf x\cdot\boldsymbol\sigma$. Then $A_R\bar\Phi + \bar\Phi A_R^\dagger = -\frac i2[\boldsymbol\theta\cdot\boldsymbol\sigma, \bar\Phi] + \frac12\{\boldsymbol\eta\cdot\boldsymbol\sigma, \bar\Phi\} = -\frac i2\cdot2i(\boldsymbol\theta\times\mathbf x)\cdot\boldsymbol\sigma + \frac12\bigl(2x^0\boldsymbol\eta\cdot\boldsymbol\sigma + 2(\boldsymbol\eta\cdot\mathbf x)\mathbb 1\bigr) = (\boldsymbol\eta\cdot\mathbf x)\mathbb 1 + (x^0\boldsymbol\eta + \boldsymbol\theta\times\mathbf x)\cdot\boldsymbol\sigma = \bar\Phi(\omega x)$, the signs of both the rotation and the boost term having flipped relative to step 2 together with the sign of $\mathbf x$ in $\bar\Phi$. Step 3 applies verbatim.
>
> **5. Part 2.** Multiply part 1 by $\bar\sigma^\nu$ and take the trace. The right side gives $\operatorname{tr}(\Phi(\Lambda x)\bar\sigma^\nu) = 2(\Lambda x)^\nu = \Lambda^\nu{}_\mu\operatorname{tr}(\Phi(x)\bar\sigma^\mu)$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]]). The left side, by cyclicity, is $\operatorname{tr}(\Phi(x)\,\Lambda_L^\dagger\bar\sigma^\nu\Lambda_L)$. So $\operatorname{tr}\bigl(X\,(\Lambda_L^\dagger\bar\sigma^\nu\Lambda_L - \Lambda^\nu{}_\mu\bar\sigma^\mu)\bigr) = 0$ for every Hermitian $X$, hence (complex-linearly) for every $X \in M_2(\mathbb C)$, since every matrix is $H_1 + iH_2$ with $H_k$ Hermitian. Taking $X = E_{ji}$ picks out the $(i, j)$ entry of the bracket, so the bracket vanishes. The same with $\Lambda_R$, $\bar\Phi$ and $\operatorname{tr}(\bar X\sigma^\nu) = 2x^\nu$ gives $\Lambda_R^\dagger\sigma^\nu\Lambda_R = \Lambda^\nu{}_\mu\sigma^\mu$.
>
> **6. Check: rotation about z.** $\boldsymbol\theta = \theta\hat{\mathbf z}$: $\Lambda_L = \operatorname{diag}(e^{-i\theta/2}, e^{i\theta/2})$, and in the matrix of Theorem §CB.15.3 the off-diagonal entry $-x^1 + ix^2$ is multiplied by $e^{-i\theta/2}\cdot\overline{e^{i\theta/2}} = e^{-i\theta}$, which is the active rotation $(x^1, x^2) \mapsto (x^1\cos\theta - x^2\sin\theta, x^1\sin\theta + x^2\cos\theta)$ ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-5|Theorem §CB.4.5]], 1). Yu's $\lambda(\theta) = \operatorname{diag}(e^{i\theta/2}, e^{-i\theta/2})$ in (3.267) is $\Lambda_L$ at $-\theta$, the passive rotation of (3.268).
>
> **What the proof shows**
> - The same six numbers $\omega_{\mu\nu}$ produce $\Lambda_L(\omega)$ and $e^\omega$, and the covering map sends one to the other. The half-angles of $\Lambda_L$ become full angles because $\lambda$ acts on $X$ twice, once from each side.
> - $\Lambda_R(\omega) = (\Lambda_L(\omega)^\dagger)^{-1}$ is *not* $\Lambda_L$ of another $\omega$ with the same $\sigma$: it covers $e^\omega$ through $\bar\sigma$.
> - Equivalence: this is [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]]; part 2 there is why $\psi_L^\dagger\bar\sigma^\mu\psi_L$ is a four-vector (the Weyl Lagrangian, §C5a.7).

^pf-cb-15-8

*Uses:* [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^def-cb-15-6|Def. §CB.15.6]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-3|Theorem §CB.4.3]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^der-cb-5-3|Derivation §CB.5.3]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-5|Theorem §CB.4.5]]

> [!theorem] Theorem §CB.15.9: SL(2, C) Is the Double Cover of SO⁺(1,3)
> 1. $\pi: SL(2, \mathbb C) \to SO^+(1,3)$ is onto, and $SO^+(1,3) \cong SL(2, \mathbb C)/\{\pm\mathbb 1\}$.
> 2. $SO^+(1,3)$ is homeomorphic to $\mathbb R^3\times SO(3)$, so its fundamental group ([[§29 The Fundamental Group#^def-29-2|590 Def. §29.2]]) is $\pi_1(SO^+(1,3)) \cong \mathbb Z_2$: it is doubly connected, as anticipated in [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^rem-cb-9-2|§CB.9, Remark: The same pattern for the Lorentz group]]. The non-contractible loops are those homotopic to a rotation through $2\pi$; the lift ([[§32 Lifting and the Fundamental Group of the Circle#^def-32-1|590 Def. §32.1]]) of that loop to $SL(2, \mathbb C)$ starting at $\mathbb 1$, $\theta \mapsto \Lambda_L(\theta\hat{\mathbf z}) = e^{-i\theta\sigma^3/2}$, ends at $-\mathbb 1$.
> 3. Under $\pi$, $U \in SU(2)$ goes to the rotation $\operatorname{diag}(1, R(U))$ of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-20|Theorem §CB.1.20]], and $e^{-\boldsymbol\eta\cdot\boldsymbol\sigma/2}$ to the pure boost $e^{\omega}$ with $\omega_{0i} = \eta_i$, $\omega_{ij} = 0$. $\pi$ is a covering map ([[§31 Covering Spaces#^def-31-2|590 Def. §31.2]]), and since $SL(2, \mathbb C)$ is simply connected ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-9|Theorem §CB.9.9]]), it is the universal covering group of $SO^+(1,3)$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The left-handed Weyl matrices are this covering": "every element of $\mathrm{SO}^+(1,3)$ is reached … $\mathrm{SO}^+(1,3) \cong \mathbb{RP}^3\times\mathbb R^3$") · Yu Exercise 3.7(d) · Yu §3.2 (the covering group of SO⁺(1,3) named, below Fig. 3.5) · the user's pre-course notes, §5.2 (Remark "SL(2,C) made explicit": kernel and surjectivity "stated, not proved here") · the user's PHY 513 notes, Ch. 7 §7.2 (end of Derivation "Why the sign appears": the topological argument) · that a surjective Lie-group homomorphism with bijective differential is a covering map, quoted*

^thm-cb-15-9

> [!derivation]- Derivation
> **1. Onto.** Every $\Lambda \in SO^+(1,3)$ is a boost times a rotation, $\Lambda = B(u)R$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]]), and each factor is an exponential $e^{\omega_1}$, $e^{\omega_2}$ ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-5|Theorem §CB.4.5]], 3–4: a boost along $\hat{\mathbf n}$ is $e^{\omega}$ with $\omega_{0i} = \eta n_i$). By Theorem §CB.15.8, $\pi(\Lambda_L(\omega_1)\Lambda_L(\omega_2)) = e^{\omega_1}e^{\omega_2} = \Lambda$.
>
> **2. The quotient.** $\pi$ is an onto homomorphism with kernel $\{\pm\mathbb 1\}$ (Theorem §CB.15.5), so $SL(2, \mathbb C)/\{\pm\mathbb 1\} \cong SO^+(1,3)$ by the first isomorphism theorem ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]).
>
> **3. The topology of SO⁺(1,3).** By [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], $\Lambda = B(u)R$ with $u = \Lambda e_0$, the first column, $u = (\gamma, \mathbf u)$, $\gamma = \sqrt{1 + \mathbf u^2}$. The map $\Lambda \mapsto (\mathbf u, R)$, $R = B(u)^{-1}\Lambda$, is continuous (the entries of $B(u)$ are continuous in $\mathbf u$, $\gamma \ge 1$), and its inverse $(\mathbf u, R) \mapsto B(u)R$ is continuous: a homeomorphism $SO^+(1,3) \cong \mathbb R^3\times SO(3)$. Hence $\pi_1(SO^+(1,3)) \cong \pi_1(\mathbb R^3)\times\pi_1(SO(3)) = 1\times\mathbb Z_2$ ([[§29 The Fundamental Group#^thm-29-7|590 Thm. §29.7]]; [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]]), and a loop is non-contractible iff its $SO(3)$ component is, i.e. iff it is homotopic to the $2\pi$ rotation loop.
>
> **4. The lift of the 2π loop.** $\theta \mapsto \Lambda_L(\theta\hat{\mathbf z}) = e^{-i\theta\sigma^3/2}$, $0 \le \theta \le 2\pi$, is continuous, starts at $\mathbb 1$, and lies over the rotation loop by Theorem §CB.15.8. At $\theta = 2\pi$ it is $\operatorname{diag}(e^{-i\pi}, e^{i\pi}) = -\mathbb 1$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-19|Theorem §CB.1.19]], 4): a closed loop downstairs whose lift is open. ⚑ By-product: this is the "$2\pi$ rotation $= -1$" of every half-integer representation, now seen as the endpoint of a lift → [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]].
>
> **5. The two decompositions match.** For $U \in SU(2)$, $UXU^\dagger = x^0\mathbb 1 - U(\mathbf x\cdot\boldsymbol\sigma)U^\dagger = x^0\mathbb 1 - (R(U)\mathbf x)\cdot\boldsymbol\sigma$ by the definition of $R(U)$ in Theorem §CB.1.20, so $\pi(U) = \operatorname{diag}(1, R(U))$. For $h = -\frac12\boldsymbol\eta\cdot\boldsymbol\sigma$, $e^h = \Lambda_L(\omega)$ with $\boldsymbol\theta = 0$, so $\pi(e^h) = e^{\omega}$, a pure boost (Theorem §CB.15.8). The polar decomposition $\lambda = e^hU$ of Theorem §CB.9.9 is mapped to "boost times rotation".
>
> **6. Universal cover.** $\pi$ is a continuous surjective homomorphism of Lie groups whose differential at $\mathbb 1$ sends the generator $A_L(\omega)$ to $\omega$ (step 2 of the proof of Theorem §CB.15.8), a bijection between the two six-dimensional algebras; such a map is a covering map (quoted). A simply connected covering space is the universal cover, and its fibre $\{\pm\mathbb 1\}$ has as many points as $\pi_1(SO^+(1,3))$ has elements, consistently with step 3 ([[§32 Lifting and the Fundamental Group of the Circle#^thm-32-4|590 Thm. §32.4]]).
>
> **What the derivation shows**
> - All topology of the Lorentz group is that of its rotation subgroup: boosts form a contractible $\mathbb R^3$, and the cover unwraps only the $SO(3)$ factor into $S^3$. This makes the remark of §C3.1 precise.
> - $SO^+(1,3) \cong \mathbb{RP}^3\times\mathbb R^3$, $SL(2, \mathbb C) \cong S^3\times\mathbb R^3$, the $\pm$ identification acting on the sphere only.
> - One input was quoted: that $\pi$ is a covering map. Everything needed later (onto, kernel, the lift of the $2\pi$ loop) was derived.
> - Used next: integrating $(j_+, j_-)$ (Theorem §CB.16.9).

^der-cb-15-9

*Uses:* [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-9|Theorem §CB.9.9]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-5|Theorem §CB.15.5]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-8|Theorem §CB.15.8]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-5|Theorem §CB.4.5]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-20|Theorem §CB.1.20]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-19|Theorem §CB.1.19]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]], [[§29 The Fundamental Group#^thm-29-7|590 Thm. §29.7]], [[§32 Lifting and the Fundamental Group of the Circle#^thm-32-4|590 Thm. §32.4]]; quoted: a surjective Lie-group homomorphism with bijective differential is a covering map

That the differential of the covering is the isomorphism of real Lie algebras of [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-8|Theorem §CB.5.8]] (first stated there; moved here in the CB ordering pass, since it needs $\pi$):

> [!theorem] Theorem §CB.15.10: The Differential of π Is the Isomorphism of Theorem §CB.5.8
> The differential ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]) of the covering $\pi : SL(2, \mathbb C) \to SO^+(1,3)$ of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]] is an isomorphism of real Lie algebras $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^def-cb-5-7|Def. §CB.5.7]]); in the conventions of Theorem §CB.15.9 it sends $-\frac i2\sigma^k \mapsto -iJ_k$ and $-\frac12\sigma^k \mapsto -iK_k$. So $\pi_\ast$ is the isomorphism $\varphi$ of [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-8|Theorem §CB.5.8]].
>
> *Source: [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]], 3, differentiated (first stated as Theorem §CB.5.8; moved here in the CB ordering pass, 2026-10-08, because it needs the covering map) · Yu, Exercise 3.7 · the user's PHY 513 notes, Ch. 8 §8.2 · conventions checked against [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]] and [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]] (batch 2)*

^thm-cb-15-10

> [!proof]- Proof
> *Source: the vault's [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]], part 3 (from the user's PHY 513 notes, Ch. 8 §8.2, and Yu, Exercise 3.7), differentiated with [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]. Convention check (batch 2): Larsen's register, $\Lambda = e^{-i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\eta\cdot\mathbf K}$ with $-iJ_i = M^{jk}$ ($ijk$ cyclic) and $-iK_i = M^{0i}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]); the statement's two assignments are confirmed in Steps 2–3, so the statement stands unchanged.*
>
> **Step 1** (a real basis). $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ consists of the traceless complex $2\times2$ matrices ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]]); $\sigma^1, \sigma^2, \sigma^3$ are a complex basis of them, so the six matrices $-\frac i2\sigma^k$, $-\frac12\sigma^k$ are a real basis. Likewise $-iJ_k$, $-iK_k$ are a real basis of $\mathfrak{so}(1,3)$.
>
> **Step 2** (rotations). By Theorem §CB.15.9, 3, $\pi(U) = \operatorname{diag}(1, R(U))$ for $U \in SU(2)$, and $R(e^{-is\sigma^k/2})$ is the rotation by $s$ about $x^k$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-20|Theorem §CB.1.20]], 2), which in the vector representation is $e^{-isJ_k} = e^{sM^{ij}}$ ($ijk$ cyclic; [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-5|Theorem §CB.4.5]], 3). By the formula of Theorem §CB.2.3,
>
> $$
> \pi_\ast\bigl(-\tfrac i2\sigma^k\bigr) = \frac{d}{ds}\pi\bigl(e^{-is\sigma^k/2}\bigr)\Big|_{s=0} = \frac{d}{ds}e^{-isJ_k}\Big|_{s=0} = -iJ_k .
> $$
>
> **Step 3** (boosts). By Theorem §CB.15.9, 3, $\pi(e^{-\boldsymbol\eta\cdot\boldsymbol\sigma/2})$ is the pure boost $e^\omega$ with $\omega_{0i} = \eta_i$, $\omega_{ij} = 0$; for $\boldsymbol\eta = s\,\mathbf e_k$ this is $e^{sM^{0k}} = e^{-isK_k}$ (Def. §CB.4.4: $-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu} = -i\boldsymbol\eta\cdot\mathbf K$). Hence
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

^pf-cb-15-10

*Uses:* [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-8|Theorem §CB.5.8]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-20|Theorem §CB.1.20]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-4|Def. §CB.4.4]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-5|Theorem §CB.4.5]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-2|Def. §CB.2.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-6|Theorem §CB.4.6]]

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
> The left column is [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]; the right column contains it as the subgroup fixing $x^0 = \frac12\operatorname{tr}X$ (unitary $\lambda$). Two things change: $\lambda^\dagger$ is no longer $\lambda^{-1}$, so $\lambda X\lambda^\dagger$ is not a similarity transformation and the trace (time) is no longer preserved; and the group is not compact, so averaging over it is impossible and unitarity is lost ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-14|Theorem §CB.16.14]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit": "Rotations had $U^\dagger\sigma^iU = R^i{}_j\sigma^j$ … The Lorentz version turns a four-vector into a $2\times2$ matrix")*

^rem-cb-15-1

## The Clifford route

Throughout, $V = \mathbb R^{1,3}$ with $q(x) = g(x, x)$, $g = \operatorname{diag}(+,-,-,-)$, and $e_0, \dots, e_3$ the standard basis ($q(e_0) = 1$, $q(e_i) = -1$).

## The even Clifford algebra of Minkowski space

> [!theorem] Theorem §CB.15.11: Cl⁰(1,3) ≅ Cl(3,0) ≅ M₂(ℂ)
> The elements $f_i = e_ie_0$ ($i = 1, 2, 3$) of $\mathrm{Cl}^0(1,3)$ satisfy $f_i^2 = +1$ and $f_if_j = -f_jf_i$ ($i \ne j$), and $e_i \mapsto f_i$ extends to an isomorphism $\mathrm{Cl}(3,0) \cong \mathrm{Cl}^0(1,3)$ ([[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-18|Theorem §CB.11.18]] with $\epsilon = 1$). Composed with [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-1|Theorem §CB.14.1]] it gives an isomorphism of real algebras $\phi : \mathrm{Cl}^0(1,3) \to M_2(\mathbb C)$, $\phi(f_i) = \sigma^i$, with $\phi(\omega) = i\mathbb 1$ for $\omega = e_0e_1e_2e_3 = f_1f_2f_3$. Under $\phi$ the map $x \mapsto xe_0$, $V \to \mathrm{Cl}^0$, sends $x = x^\mu e_\mu$ to the Hermitian matrix $\tilde x = x^0\mathbb 1 + x^i\sigma^i$, which is $\bar X = x_\mu\bar\sigma^\mu$ of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-20|Def. §CB.0.20]] (not the course's $X = x_\mu\sigma^\mu$).
>
> *Source: written here · the matrices $x^0 + \mathbf x\cdot\boldsymbol\sigma$ for four-vectors: P. Woit, Quantum Theory, Groups and Representations, §40.4*

^thm-cb-15-11

> [!proof]- Proof
> Orthogonal vectors anticommute in $\mathrm{Cl}(1,3)$: $uv + vu = 2B(u, v)$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-8|Theorem §CB.10.8]]), and $e_\mu \perp e_\nu$ for $\mu \ne \nu$. Also $e_0^2 = q(e_0) = 1$ and $e_i^2 = q(e_i) = -1$.
>
> **1. Squares.** $f_i^2 = e_ie_0e_ie_0 = -e_ie_ie_0e_0 = -(-1)(1) = 1$, moving the middle $e_0$ past $e_i$ (one sign).
>
> **2. Anticommutation.** For $i \ne j$: $f_if_j = e_ie_0e_je_0 = -e_ie_je_0e_0 = -e_ie_j$, and likewise $f_jf_i = -e_je_i = e_ie_j$. So $f_if_j = -f_jf_i$. ⚑ By-product: $e_ie_j = -f_if_j$, used for the rotation generators in Theorem §CB.15.13.
>
> **3. The even subalgebra is Cl(3,0).** In Theorem §CB.11.18 take $e_0$ with $q(e_0) = \epsilon = 1$; then $V' = e_0^\perp = \operatorname{span}\{e_1, e_2, e_3\}$ with $q'(v') = -\epsilon q(v') = -q(v')$, so $q'(e_i) = +1$: $(V', q') = \mathbb R^{3,0}$. The isomorphism $\mathrm{Cl}(3,0) \cong \mathrm{Cl}^0(1,3)$ of that theorem is $v' \mapsto v'e_0$, i.e. $e_i \mapsto f_i$; steps 1–2 are the relations it requires.
>
> **4. The matrix algebra.** Theorem §CB.14.1 gives the real-algebra isomorphism $\mathrm{Cl}(3,0) \cong M_2(\mathbb C)$, $e_i \mapsto \sigma^i$. Composing with the inverse of step 3 gives $\phi$ with $\phi(f_i) = \sigma^i$. In particular the $f_i$ generate $\mathrm{Cl}^0(1,3)$ as a real algebra, since the $e_i$ generate $\mathrm{Cl}(3,0)$.
>
> **5. The volume element.** $f_1f_2 = -e_1e_2$ (step 2), so $f_1f_2f_3 = -e_1e_2e_3e_0$. Moving $e_0$ to the front past $e_3$, $e_2$, $e_1$ costs $(-1)^3$: $f_1f_2f_3 = e_0e_1e_2e_3 = \omega$. Hence $\phi(\omega) = \sigma^1\sigma^2\sigma^3 = i\mathbb 1$ (Theorem §CB.14.1).
>
> **6. Four-vectors.** $xe_0 = x^0e_0e_0 + x^ie_ie_0 = x^0 + x^if_i$, so $\phi(xe_0) = x^0\mathbb 1 + x^i\sigma^i$. With $x_0 = x^0$, $x_i = -x^i$ and $\bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma)$ (Def. §CB.0.20), $x_\mu\bar\sigma^\mu = x^0\mathbb 1 + x^i\sigma^i = \bar X$.
>
> **What the proof shows**
> - The course's Hermitian $2\times2$ picture of a four-vector is the Clifford product $xe_0$, read in $\mathrm{Cl}^0 \cong M_2(\mathbb C)$.
> - ⚑ By-product (a convention): the natural Clifford identification gives $\bar X = x_\mu\bar\sigma^\mu$, while the course's covering map is built on $X = x_\mu\sigma^\mu$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]]). The two differ by $\sigma^i \to -\sigma^i$; its effect on the group is worked out in Theorem §CB.15.12, 2.
> - Used next: Theorems §CB.15.12–§CB.15.13, and the Dirac module in §CB.17.

^pf-cb-15-11

*Uses:* [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-8|Theorem §CB.10.8]], [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-18|Theorem §CB.11.18]], [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-1|Theorem §CB.14.1]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-20|Def. §CB.0.20]]

## Spin(1,3) and SL(2,ℂ)

> [!theorem] Theorem §CB.15.12: Spin(1,3)₀ Is SL(2,ℂ), and ρ Is the Course's Covering Map up to λ ↦ (λ†)⁻¹
> 1. The isomorphism $\phi$ of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-11|Theorem §CB.15.11]] restricts to an isomorphism of Lie groups from $\mathrm{Spin}(1,3)_0$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-7|Def. §CB.13.7]]) onto $SL(2, \mathbb C)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-2|Def. §CB.1.2]]).
> 2. For $x \in \mathrm{Spin}(1,3)_0$ and $\lambda = \phi(x)$, $\rho(x)$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-10|Theorem §CB.13.10]]) acts on $\tilde x = x_\mu\bar\sigma^\mu$ (Theorem §CB.15.11) by $\tilde x \mapsto \lambda\tilde x\lambda^\dagger$, and $\ker\rho = \{\pm1\}$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-15|Theorem §CB.13.15]]). The course's covering $\pi : SL(2, \mathbb C) \to SO^+(1,3)$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]]) acts instead on $X = x_\mu\sigma^\mu$ by $X \mapsto \mu X\mu^\dagger$, and
>
> $$
> \rho(x) = \pi\bigl(\theta(\phi(x))\bigr), \qquad \theta(\lambda) = (\lambda^\dagger)^{-1} .
> $$
>
> So the element of $\mathrm{Spin}(1,3)_0$ over $e^\omega$ is sent by $\phi$ to $\pm\Lambda_R(\omega)$ and by $\theta\circ\phi$ to $\pm\Lambda_L(\omega)$ (the Weyl matrices, [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^def-cb-15-6|Def. §CB.15.6]]); $\theta\circ\phi$ is the restriction of the real-algebra isomorphism $\phi' : \mathrm{Cl}^0(1,3) \to M_2(\mathbb C)$ with $\phi'(f_i) = -\sigma^i$, $\phi'(xe_0) = X$, and $\rho = \pi\circ\phi'$ on $\mathrm{Spin}(1,3)_0$.
> 3. $\phi$ maps $\mathrm{Spin}(1,3)$ onto $\{A \in M_2(\mathbb C) : \det A = \pm1\}$. $\mathrm{Spin}(1,3)$ has two components, $\mathrm{Spin}(1,3)_0$ and $e_0e_1\,\mathrm{Spin}(1,3)_0$; $\rho(e_0e_1) = \operatorname{diag}(-1, -1, 1, 1)$, and $\rho$ maps the two components onto $SO^+(1,3)$ and onto $\mathcal P\mathcal T\cdot SO^+(1,3)$, the component of $SO(1,3)$ containing $\mathcal P\mathcal T$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-12|Theorem §CB.2.12]]).
>
> *Source: written here · the action $\Omega(\cdot)\Omega^\dagger$ on $x^0 + \mathbf x\cdot\boldsymbol\sigma$: P. Woit, Quantum Theory, Groups and Representations, §40.4 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the course's covering: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (the user's PHY 513 notes, Ch. 8 §8.2; Yu Exercise 3.7)*

^thm-cb-15-12

> [!proof]- Proof
> Notation: $\tilde v = \phi(ve_0) = v_\mu\bar\sigma^\mu$ for $v \in V$ (Theorem §CB.15.11, 6); $\theta(\lambda) = (\lambda^\dagger)^{-1}$.
>
> **1. Conjugation by e₀.** Since $e_0^2 = 1$, $\kappa(a) = e_0ae_0$ is an algebra automorphism of $\mathrm{Cl}^0(1,3)$: $\kappa(ab) = e_0ae_0e_0be_0 = \kappa(a)\kappa(b)$. On the generators, $\kappa(f_i) = e_0e_ie_0e_0 = e_0e_i = -e_ie_0 = -f_i$.
>
> **2. Its matrix form.** $\tilde\kappa(A) = \sigma^2\bar A\sigma^2$ ($\bar A$ the entrywise conjugate) is a real-algebra automorphism of $M_2(\mathbb C)$: real-linear, $\tilde\kappa(AB) = \sigma^2\bar A\sigma^2\sigma^2\bar B\sigma^2 = \tilde\kappa(A)\tilde\kappa(B)$ because $(\sigma^2)^2 = \mathbb 1$, $\tilde\kappa(\mathbb 1) = \mathbb 1$. By [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-22|Theorem §CB.0.22]], 3, $\sigma^2(\sigma^i)^{\ast}\sigma^2 = -\sigma^i$, so $\tilde\kappa(\sigma^i) = -\sigma^i$. Thus $\phi\circ\kappa$ and $\tilde\kappa\circ\phi$ are real-algebra homomorphisms $\mathrm{Cl}^0 \to M_2(\mathbb C)$ that agree on the generators $f_i$ (both give $-\sigma^i$; Theorem §CB.15.11, 4), hence everywhere: $\phi(\kappa(a)) = \tilde\kappa(\phi(a))$.
>
> **3. On determinant ±1, κ̃ is ±θ.** By [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-15|Theorem §CB.7.15]], 1, applied to $\bar A$: $\bar A^{\mathsf T}\varepsilon\bar A = \overline{\det A}\,\varepsilon$, so for invertible $A$, $\varepsilon\bar A\varepsilon^{-1} = \overline{\det A}\,(\bar A^{\mathsf T})^{-1} = \overline{\det A}\,(A^\dagger)^{-1}$. With $\varepsilon = i\sigma^2$, $\varepsilon^{-1} = -i\sigma^2$, the left side is $\sigma^2\bar A\sigma^2$. Hence
>
> $$
> \tilde\kappa(A) = \overline{\det A}\;\theta(A), \qquad \text{in particular } \tilde\kappa = \theta \text{ on } SL(2, \mathbb C) .
> $$
>
> **4. The determinant of a product of two vectors.** For $u, v \in V$: $uv = (ue_0)(e_0v)$ and $e_0v = e_0(ve_0)e_0 = \kappa(ve_0)$. So $\phi(uv) = \tilde u\,\tilde\kappa(\tilde v)$, and $\det\phi(uv) = \det\tilde u\cdot\overline{\det\tilde v} = q(u)\,q(v)$, since $\det\tilde v = \det(v_\mu\bar\sigma^\mu) = v_\mu v^\mu = q(v)$ is real ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]], 2).
>
> **5. Spin(1,3)₀ lands in SL(2,ℂ).** Every $x \in \mathrm{Spin}(1,3)$ is $u_1u_2\cdots u_{2k}$ with $q(u_i) = \pm1$ (Def. §CB.13.7). Grouping the factors in pairs and using step 4 and $\det(AB) = \det A\det B$: $\det\phi(x) = \prod_iq(u_i) = \pm1$. On $\mathrm{Spin}(1,3)_0$, $\det\circ\phi$ is continuous with values in $\{\pm1\}$ and equals $1$ at $x = 1$; $\mathrm{Spin}(1,3)_0$ is connected ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]], 1), so $\det\phi(x) = 1$.
>
> **6. The action on four-vectors.** For $x \in \mathrm{Spin}(1,3)$ and $v \in V$, $\rho(x)v = xvx^{-1}$ (Theorem §CB.13.10, 2). Inserting $e_0e_0 = 1$: $(\rho(x)v)e_0 = x(ve_0)(e_0x^{-1}e_0) = x\,(ve_0)\,\kappa(x^{-1})$. Apply $\phi$, step 2 and step 3 with $d = \det\phi(x) = \pm1$ (so $\overline{\det\phi(x)^{-1}} = d$ and $\theta(\lambda^{-1}) = \lambda^\dagger$):
>
> $$
> \widetilde{\rho(x)v} = \lambda\,\tilde v\,\tilde\kappa(\lambda^{-1}) = d\,\lambda\,\tilde v\,\lambda^\dagger, \qquad \lambda = \phi(x) .
> $$
>
> For $x \in \mathrm{Spin}(1,3)_0$ ($d = 1$, step 5) this is $\tilde v \mapsto \lambda\tilde v\lambda^\dagger$, the first claim of part 2.
>
> **7. Comparison with π.** $X = v_\mu\sigma^\mu = v^0\mathbb 1 - v^i\sigma^i = \tilde\kappa(\tilde v)$ (step 2, real coefficients). Applying the automorphism $\tilde\kappa$ to step 6 ($d = 1$): $X \mapsto \tilde\kappa(\lambda)\,X\,\tilde\kappa(\lambda^\dagger) = \theta(\lambda)\,X\,\theta(\lambda^\dagger)$, and $\theta(\lambda^\dagger) = \lambda^{-1} = \theta(\lambda)^\dagger$. So $\rho(x)$ acts on $X$ as $X \mapsto \mu X\mu^\dagger$ with $\mu = \theta(\lambda)$, which is the definition of $\pi(\mu)$ (Theorem §CB.15.4): $\rho(x) = \pi(\theta(\phi(x)))$.
>
> **8. Onto SL(2,ℂ).** Let $\mu \in SL(2, \mathbb C)$. $\pi(\theta(\mu)) \in SO^+(1,3)$, and $SO^+(1,3)$ is the identity component of $O(1,3)$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], 2). $V = \mathbb R^{1,3}$ contains the negative definite plane $\operatorname{span}\{e_1, e_2\}$, so $\rho : \mathrm{Spin}(1,3)_0 \to SO^+(1,3)$ is onto and $-1 \in \mathrm{Spin}(1,3)_0$ (Theorem §CB.13.15). Pick $x$ with $\rho(x) = \pi(\theta(\mu))$; by step 7, $\pi(\theta(\phi(x))) = \pi(\theta(\mu))$, so $\theta(\phi(x)) = \pm\theta(\mu)$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-5|Theorem §CB.15.5]]) and $\phi(x) = \pm\mu$ ($\theta$ is a bijection with $\theta(-\lambda) = -\theta(\lambda)$). If the sign is $-$, replace $x$ by $-x \in \mathrm{Spin}(1,3)_0$. So $\phi(\mathrm{Spin}(1,3)_0) = SL(2, \mathbb C)$.
>
> **9. Part 1.** $\phi$ is an injective algebra homomorphism and a linear isomorphism of finite-dimensional spaces, so its restriction to $\mathrm{Spin}(1,3)_0$ is an injective group homomorphism, continuous with continuous inverse, onto $SL(2, \mathbb C)$ by step 8: an isomorphism of Lie groups ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]]).
>
> **10. The kernel and the Weyl matrices.** $\rho(x) = \mathbb 1$ iff $\theta(\phi(x)) = \pm\mathbb 1$ (step 7, Theorem §CB.15.5) iff $\phi(x) = \pm\mathbb 1$ iff $x = \pm1$. Since $\pi(\Lambda_L(\omega)) = e^\omega$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-8|Theorem §CB.15.8]], 1), $\rho(x) = e^\omega$ iff $\theta(\phi(x)) = \pm\Lambda_L(\omega)$ iff $\phi(x) = \pm\theta(\Lambda_L(\omega)) = \pm\Lambda_R(\omega)$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-7|Theorem §CB.15.7]], 2). Finally $\phi' = \tilde\kappa\circ\phi$ is a real-algebra isomorphism with $\phi'(f_i) = -\sigma^i$ and $\phi'(xe_0) = \tilde\kappa(\tilde x) = X$, equal to $\theta\circ\phi$ on $\mathrm{Spin}(1,3)_0$ (step 3), so $\rho = \pi\circ\phi'$ there.
>
> **11. Part 3.** By step 5, $\phi(\mathrm{Spin}(1,3)) \subset \{\det = \pm1\}$. $e_0e_1 \in \mathrm{Spin}(1,3)$, $e_0e_1 = -e_1e_0 = -f_1$, $\phi(e_0e_1) = -\sigma^1$ with determinant $-1$, and $(e_0e_1)^2 = -e_0e_0e_1e_1 = 1$. If $y \in \mathrm{Spin}(1,3)$ has $\det\phi(y) = -1$, then $e_0e_1y \in \mathrm{Spin}(1,3)$ has determinant $1$, so $\phi(e_0e_1y) \in SL(2, \mathbb C) = \phi(\mathrm{Spin}(1,3)_0)$ and, $\phi$ being injective, $e_0e_1y \in \mathrm{Spin}(1,3)_0$, i.e. $y \in e_0e_1\mathrm{Spin}(1,3)_0$. The two pieces are the preimages of $\det = 1$ and $\det = -1$, disjoint, open and closed, each connected (homeomorphic to $\mathrm{Spin}(1,3)_0$); their images under $\phi$ fill $\{\det = \pm1\}$ ($\phi(e_0e_1)SL(2, \mathbb C) = \{\det = -1\}$). By Theorem §CB.13.10, 2, $\rho(e_0e_1) = r_{e_0}r_{e_1}$, the product of the reflections $e_0 \mapsto -e_0$ and $e_1 \mapsto -e_1$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-4|Theorem §CB.13.4]]): $\operatorname{diag}(-1, -1, 1, 1)$, with determinant $+1$ and $\Lambda^0{}_0 = -1$, the same signs as $\mathcal P\mathcal T = -\mathbb 1$, so it lies in $\mathcal P\mathcal T\cdot SO^+(1,3)$ (Theorem §CB.2.12, 1–2), and $\rho(e_0e_1\mathrm{Spin}(1,3)_0) = \rho(e_0e_1)\,SO^+(1,3) = \mathcal P\mathcal T\cdot SO^+(1,3)$.
>
> **What the proof shows**
> - The Clifford route and the course's route reach the same group, but the natural identifications differ by the automorphism $\theta(\lambda) = (\lambda^\dagger)^{-1}$, which exchanges $\Lambda_L$ and $\Lambda_R$. ⚑ By-product: "which matrix is $\lambda$" is a convention, fixed in the course by building $\pi$ on $X = x_\mu\sigma^\mu$; the Clifford algebra with $f_i \mapsto \sigma^i$ builds it on $\bar X$. Every later statement that names $(\frac12, 0)$ fixes the convention (Theorem §CB.16.7, Theorem §CB.17.3).
> - Step 6 for $d = -1$ shows that the other component acts by $\tilde v \mapsto -\lambda\tilde v\lambda^\dagger$: the minus sign reverses time, as $\mathcal P\mathcal T$ does.
> - Used next: the Lie algebra version (Theorem §CB.15.13) and the Dirac module restricted to $\mathrm{Spin}(1,3)_0$ (Theorem §CB.17.3).

^pf-cb-15-12

*Uses:* [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-11|Theorem §CB.15.11]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-7|Def. §CB.13.7]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-4|Theorem §CB.13.4]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-10|Theorem §CB.13.10]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-15|Theorem §CB.13.15]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-15|Theorem §CB.7.15]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-22|Theorem §CB.0.22]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-7|Theorem §CB.15.7]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-5|Theorem §CB.15.5]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-8|Theorem §CB.15.8]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-12|Theorem §CB.2.12]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]]

> [!theorem] Theorem §CB.15.13: The Three Lie Algebras Agree
> Under $\phi$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-11|Theorem §CB.15.11]]), $\mathfrak{spin}(1,3)$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-13|Def. §CB.13.13]]) maps isomorphically onto $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ ([[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^def-cb-5-7|Def. §CB.5.7]]): $\frac12e_ie_j = -\frac12f_if_j \mapsto -\frac i2\varepsilon_{ijk}\sigma^k$ (rotations) and $\frac12e_ie_0 \mapsto \frac12\sigma^i$ (boosts). The differential $\rho_\ast$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-14|Theorem §CB.13.14]]) is $\rho_\ast(\frac12e_\mu e_\nu) = M_{\mu\nu} = g_{\mu\alpha}g_{\nu\beta}M^{\alpha\beta}$, the generators of [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-2|Def. §CB.4.2]] with lowered indices; so $\rho_\ast\circ\phi^{-1}$ sends $-\frac i2\sigma^k \mapsto -iJ_k$ and $\frac12\sigma^k \mapsto -iK_k$ ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-4|Def. §CB.4.4]]). It equals $\pi_\ast\circ\theta_\ast$, with $\pi_\ast$ the isomorphism of [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-8|Theorem §CB.5.8]] ($-\frac i2\sigma^k \mapsto -iJ_k$, $-\frac12\sigma^k \mapsto -iK_k$) and $\theta_\ast(Y) = -Y^\dagger$ the differential of $\theta(\lambda) = (\lambda^\dagger)^{-1}$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-12|Theorem §CB.15.12]]).
>
> *Source: written here*

^thm-cb-15-13

> [!proof]- Proof
> **1. A basis.** $\mathfrak{spin}(1,3)$ is spanned by the six products $e_\mu e_\nu$, $\mu < \nu$ (Def. §CB.13.13), and it is the Lie algebra of $\mathrm{Spin}(1,3)$ (Theorem §CB.13.14, 1).
>
> **2. The images.** $\phi(e_ie_0) = \phi(f_i) = \sigma^i$. For $i \ne j$, $e_ie_j = -f_if_j$ (Theorem §CB.15.11, Proof, step 2), and $\sigma^i\sigma^j = i\varepsilon_{ijk}\sigma^k$ for $i \ne j$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], 3), so $\phi(\frac12e_ie_j) = -\frac12\sigma^i\sigma^j = -\frac i2\varepsilon_{ijk}\sigma^k$.
>
> **3. An isomorphism onto 𝔰𝔩(2,ℂ)_ℝ.** The images $\frac12\sigma^k$, $-\frac i2\sigma^k$ ($k = 1, 2, 3$) are a real basis of the traceless matrices, because $\sigma^1, \sigma^2, \sigma^3$ are a complex basis of them (Theorem §CB.0.21, 4). These form $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$, of real dimension $6$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]]). $\phi$ is injective and multiplicative, so it preserves commutators, and its restriction is a Lie algebra isomorphism $\mathfrak{spin}(1,3) \cong \mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ — consistently with $\phi(\mathrm{Spin}(1,3)_0) = SL(2, \mathbb C)$ (Theorem §CB.15.12, 1).
>
> **4. The differential of ρ in components.** By Theorem §CB.13.14, 2, $\rho_\ast(\frac12e_\mu e_\nu)(v) = B(e_\nu, v)e_\mu - B(e_\mu, v)e_\nu = v_\nu e_\mu - v_\mu e_\nu$, i.e. the matrix $(\rho_\ast(\frac12e_\mu e_\nu))^\rho{}_\sigma = \delta^\rho_\mu g_{\nu\sigma} - \delta^\rho_\nu g_{\mu\sigma}$. Lowering both labels of $(M^{\alpha\beta})^\rho{}_\sigma = g^{\alpha\rho}\delta^\beta_\sigma - g^{\beta\rho}\delta^\alpha_\sigma$ (Def. §CB.4.2): $g_{\mu\alpha}g_{\nu\beta}(M^{\alpha\beta})^\rho{}_\sigma = \delta^\rho_\mu g_{\nu\sigma} - \delta^\rho_\nu g_{\mu\sigma}$. So $\rho_\ast(\frac12e_\mu e_\nu) = M_{\mu\nu}$.
>
> **5. Rotations and boosts.** For spatial $i, j$: $M_{ij} = g_{ii}g_{jj}M^{ij} = M^{ij} = -i\mathcal J^{ij} = -i\varepsilon_{ijk}J_k$, since $J_k = \frac12\varepsilon_{klm}\mathcal J^{lm}$ gives $\mathcal J^{ij} = \varepsilon_{ijk}J_k$ (Def. §CB.4.4). With step 2: $\rho_\ast\phi^{-1}(-\frac i2\varepsilon_{ijk}\sigma^k) = -i\varepsilon_{ijk}J_k$, i.e. $-\frac i2\sigma^k \mapsto -iJ_k$. For boosts: $M_{k0} = g_{kk}g_{00}M^{k0} = -M^{k0} = M^{0k} = -i\mathcal J^{0k} = -iK_k$, and $\phi(\frac12e_ke_0) = \frac12\sigma^k$, so $\frac12\sigma^k \mapsto -iK_k$. Check on $v$: $\rho_\ast(\frac12e_ke_0)$ sends $e_0 \mapsto e_k$ and $e_k \mapsto e_0$, the generator of a boost along $+e_k$.
>
> **6. Comparison with the differential of π.** $\theta$ is a continuous homomorphism of $SL(2, \mathbb C)$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^lem-cb-9-11|Lemma §CB.9.11]], 2), and $\theta(e^{sY}) = ((e^{sY})^\dagger)^{-1} = e^{-sY^\dagger}$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], 2 and 4), so $\theta_\ast(Y) = \frac{d}{ds}e^{-sY^\dagger}\big|_0 = -Y^\dagger$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]). Then $\theta_\ast(-\frac i2\sigma^k) = -\frac i2\sigma^k$ and $\theta_\ast(\frac12\sigma^k) = -\frac12\sigma^k$, and Theorem §CB.5.8 gives $\pi_\ast\theta_\ast(-\frac i2\sigma^k) = -iJ_k$, $\pi_\ast\theta_\ast(\frac12\sigma^k) = -iK_k$: the same values as step 5 on a basis, so $\rho_\ast\circ\phi^{-1} = \pi_\ast\circ\theta_\ast$. (This is also the chain rule applied to $\rho = \pi\circ\theta\circ\phi$, Theorem §CB.15.12, 2.)
>
> **What the proof shows**
> - $\rho_\ast(\frac12e_\mu e_\nu) = M_{\mu\nu}$: in the Clifford algebra the generator of the $\mu\nu$-plane is half the product of the two basis vectors, with the metric lowering the labels. Hence $\exp(\frac14\omega^{\mu\nu}e_\mu e_\nu)$ covers $e^\omega = \exp(\frac12\omega_{\mu\nu}M^{\mu\nu})$, used in Theorem §CB.17.3.
> - ⚑ By-product: rotations are the same through $\phi$ and through the course's $\pi$; boosts differ by a sign. That sign is the automorphism $\theta$, i.e. the exchange of $\Lambda_L$ and $\Lambda_R$ (Theorem §CB.15.12, 2).

^pf-cb-15-13

*Uses:* [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-13|Def. §CB.13.13]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-14|Theorem §CB.13.14]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-11|Theorem §CB.15.11]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-12|Theorem §CB.15.12]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-2|Def. §CB.4.2]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-4|Def. §CB.4.4]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-8|Theorem §CB.5.8]]

> [!remark]- Connections
> - The two routes to $SL(2, \mathbb C)$ meet at Theorem §CB.15.11: the Hermitian matrix $x^0 + \mathbf x\cdot\boldsymbol\sigma = x_\mu\bar\sigma^\mu$ is the Clifford product $x\,e_0$, and $\lambda\tilde x\lambda^\dagger$ is conjugation in the Clifford algebra read through $e_0$. The course builds its covering on $x_\mu\sigma^\mu$ instead; the two differ by $\lambda \mapsto (\lambda^\dagger)^{-1}$ (Theorem §CB.15.12, 2), which is why the Clifford identification calls $\Lambda_R$ what the course calls $\Lambda_L$.
> - The covering $SL(2, \mathbb C) \to SO^+(1,3)$ restricts on $SU(2)$ to Quantum Mechanics' covering of $SO(3)$, and the polar decomposition $\lambda = e^hU$ is the spinor image of "boost times rotation" — [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-6|REL Theorem §B1.2.6]].
> - **Used in**: Theorems §CB.15.1–§CB.15.2 — [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-2|Def. §CB.1.2]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]; Theorem §CB.15.3 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]]), [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (embedded; cited in [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-5|Theorem §C5a.5.5]]); Theorem §CB.9.9 — [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]] (its derivation; embedded in [[§C1a.4 The Lorentz Group|§C1a.4]]), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded); Theorem §CB.15.4 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]]); Theorem §CB.15.5 — [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded; cited in [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-4|§C3.3, Remark: Why a spinor's matrix is fixed only up to sign]]), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded); Theorem §CB.15.9 — [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded; cited in [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-4|§C3.3, Remark: Why a spinor's matrix is fixed only up to sign]]), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded), [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]] (cited in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-2|§C5a.0, Remark: What the Clifford relation induces]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-3|§C5a.0, Remark: Four jobs of the γ's]]); §CB.15, Remark: The rotation story, one level up — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded); Theorems §CB.15.11–§CB.15.13 — [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-5|Theorem §CB.15.5]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]].
