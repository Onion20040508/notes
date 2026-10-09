---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.10
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element]] →

*Sources: E. Meinrenken, Clifford Algebras and Lie Groups, lecture notes, University of Toronto, Fall 2009, Ch. 1–2 (https://www.math.toronto.edu/mein/teaching/LieClifford/cl12.pdf; convention $vw + wv = 2B(v, w)$, as here) · J. Figueroa-O'Farrill, Spin Geometry, lecture notes, Edinburgh 2010, version of 18 May 2017, Lectures 1–3 (https://empg.maths.ed.ac.uk/Activities/Spin/SpinNotes.pdf, read via the Internet Archive copy of 27 Sep 2024; convention $x^2 = -Q(x)$) · P. Woit, Quantum Theory, Groups and Representations, Ch. 28–29 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf; convention $[\gamma_j, \gamma_k]_+ = 2\delta_{jk}$, as here) · Linear Algebra (LADR) §§11, 35–38 · the user's PHY 513 notes, Ch. 8 · Peskin & Schroeder, §3.2, §3.4 · the rest written here.*

What is the algebra that the Dirac matrices generate, defined without matrices? The spinor chapter meets it as the relation $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]]) and as the algebra of square roots of $p^2$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^rem-cb-10-1|§CB.10, ★ Remark: The Clifford algebra is the algebra of square roots of p²]]). This section defines the Clifford algebra $\mathrm{Cl}(V, q)$ of a quadratic space as a quotient of the tensor algebra, states its universal property, and introduces Clifford modules, with the course's Dirac matrices and Dirac maps as the first example and the first consequences of the Clifford relation; its structure — the $\mathbb Z_2$-grading, the reversal, the basis $e_I$ and $\dim = 2^n$, the identification with $\Lambda V$ as a vector space, the volume element (the abstract $\gamma^5$), the even subalgebra, and the low-dimensional examples — is derived in [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element|§CB.11]]. Representations of algebras are [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-9|Def. §CB.6.9]]; exterior powers are [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-7-12|Def. §CB.7.12]]. The complex theory is [[§CB.12 Complex Clifford Algebras and Clifford Modules|§CB.12]]; the spin group, [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.13]].

## Quadratic spaces, the tensor algebra and quotients

Quadratic forms and their bilinear forms, defined in LADR:

![[§35 Bilinear Forms and Quadratic Forms#^ladr-9-18]]

> [!definition] Definition §CB.10.1: Quadratic Space
> A **quadratic space** $(V, q)$ over $\mathbb K = \mathbb R$ or $\mathbb C$ is a finite-dimensional $\mathbb K$-vector space $V$ with a quadratic form $q$ ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-18|LADR Def. 9.18]]), $q(v) = B(v, v)$ for the symmetric bilinear form $B(v, w) = \frac12\bigl(q(v + w) - q(v) - q(w)\bigr)$. It is **nondegenerate** if $B(v, \cdot) = 0$ implies $v = 0$. A basis $e_1, \dots, e_n$ is **orthogonal** if $B(e_i, e_j) = 0$ for $i \ne j$, **orthonormal** if moreover $q(e_i) = \pm1$ (over $\mathbb C$: $q(e_i) = 1$). $\mathbb R^{r,s}$ denotes $\mathbb R^{r+s}$ with $q(x) = x_1^2 + \cdots + x_r^2 - x_{r+1}^2 - \cdots - x_{r+s}^2$; Minkowski space is $\mathbb R^{1,3}$ with $q(x) = g(x, x)$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]]).
>
> *Source (planned): LADR §35 (orthogonal bases: Thm. 9.12) · written here*

^def-cb-10-1

> [!definition] Definition §CB.10.2: Tensor Algebra
> The **tensor algebra** of a $\mathbb K$-vector space $V$ is $T(V) = \bigoplus_{k\ge0}V^{\otimes k}$ ($V^{\otimes0} = \mathbb K$, $V^{\otimes k}$ of [[§38 Tensor Products#^ladr-9-88|LADR Def. 9.88]]), an associative algebra ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-7|Def. §CB.6.7]]) with the product $(v_1\otimes\cdots\otimes v_k)(w_1\otimes\cdots\otimes w_l) = v_1\otimes\cdots\otimes v_k\otimes w_1\otimes\cdots\otimes w_l$ extended bilinearly, and unit $1 \in \mathbb K$.
>
> *Source (planned): written here*

^def-cb-10-2

> [!definition] Definition §CB.10.3: Two-Sided Ideal
> A **two-sided ideal** of an associative algebra $A$ is a subspace $I$ with $aI \subset I$ and $Ia \subset I$ for all $a \in A$. The ideal **generated** by a subset $S$ is the smallest one containing $S$: the span of all $asb$ with $a, b \in A$, $s \in S$.
>
> *Source (planned): written here*

^def-cb-10-3

> [!definition] Definition §CB.10.4: Quotient Algebra
> For a two-sided ideal $I$ of $A$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-3|Def. §CB.10.3]]), the **quotient algebra** $A/I$ is the quotient space ([[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR Def. 3.99]]) with the product $(a + I)(b + I) = ab + I$.
>
> *Source (planned): written here*

^def-cb-10-4

> [!theorem] Theorem §CB.10.5: The Quotient Is an Algebra
> The product of [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-4|Def. §CB.10.4]] is well defined, $A/I$ is an associative algebra with unit $1 + I$, and $a \mapsto a + I$ is a surjective algebra homomorphism ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-8|Def. §CB.6.8]]) with kernel $I$. An algebra homomorphism $f : A \to B$ with $f(I) = 0$ factors uniquely through $A/I$.
>
> *Source (planned): written here*

^thm-cb-10-5

> [!proof]- Proof
> If $a' = a + i$, $b' = b + j$ with $i, j \in I$, then $a'b' = ab + (aj + ib + ij)$, and each of $aj$, $ib$, $ij$ lies in $I$ because $I$ is a two-sided ideal; so $a'b' + I = ab + I$. Associativity, bilinearity and the unit pass from $A$ to the cosets term by term. The map $a \mapsto a + I$ is linear, multiplicative by the definition of the product, onto, and sends $a$ to $0 + I$ iff $a \in I$. If $f(I) = 0$, put $\bar f(a + I) = f(a)$: well defined since $f(a + i) = f(a)$, and an algebra homomorphism because $f$ is; it is the only map with $\bar f(a + I) = f(a)$.

^pf-cb-10-5

## The Clifford algebra and its universal property

> [!definition] Definition §CB.10.6: Clifford Algebra
> The **Clifford algebra** of a quadratic space $(V, q)$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-1|Def. §CB.10.1]]) is
>
> $$
> \mathrm{Cl}(V, q) = T(V)/I_q, \qquad I_q = \text{the two-sided ideal generated by } \{v\otimes v - q(v)1 : v \in V\}
> $$
>
> ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-2|Def. §CB.10.2]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-4|Def. §CB.10.4]]). The image of $v \in V$ is written $v$, and the product in $\mathrm{Cl}(V, q)$ by juxtaposition, so $vv = q(v)$. $\mathrm{Cl}(r, s) = \mathrm{Cl}(\mathbb R^{r,s})$; the Clifford algebra of Minkowski space is $\mathrm{Cl}(1,3)$.
>
> *Source: E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2, Def. 2.1 (same convention) · J. Figueroa-O'Farrill, Spin Geometry, §1.2.2 (ideal generated by $x\otimes x + Q(x)$: the opposite sign) · Woit, §29.2*

^def-cb-10-6

> [!caution] Caution: Two sign conventions for the Clifford relation
> These notes use the physics convention $vv = +q(v)$, which with $q = g$ gives $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]]; Woit, §29.2, eq. (29.2), and Meinrenken, Def. 2.1, use the same sign). Much of the mathematical literature (e.g. Figueroa-O'Farrill, Spin Geometry, eq. (2); Lawson–Michelsohn) writes $vv = -q(v)$; its $\mathrm{Cl}(V, q)$ is this section's $\mathrm{Cl}(V, -q)$, and labels such as $\mathrm{Cl}_{r,s}$ or $\mathrm{Cl}(r, s)$ then refer to different algebras. Over $\mathbb C$ the two conventions give isomorphic algebras ($v \mapsto iv$). Here $\mathrm{Cl}(r, s)$ always has $r$ generators squaring to $+1$ and $s$ to $-1$: in $\mathrm{Cl}(1,3)$, $(\gamma^0)^2 = +1$, $(\gamma^i)^2 = -1$.
>
> *Source: SPEC-CB decision 6 · Woit, §29.2 (which notes the other convention) · Meinrenken, Clifford Algebras and Lie Groups, Def. 2.1 · Figueroa-O'Farrill, Spin Geometry, eq. (2) and §1.3.2 (his $C\ell(s,t)$, $s$ generators squaring to $-1$, is this section's $\mathrm{Cl}(t,s)$)*

^cau-cb-10-1

> [!theorem] Theorem §CB.10.7: Universal Property of the Clifford Algebra
> Let $A$ be an associative algebra over $\mathbb K$ ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-7|Def. §CB.6.7]]) and $f : V \to A$ a linear map with $f(v)^2 = q(v)1_A$ for all $v \in V$. Then there is a unique algebra homomorphism $\tilde f : \mathrm{Cl}(V, q) \to A$ ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-8|Def. §CB.6.8]]) with $\tilde f(v) = f(v)$ for $v \in V$.
>
> *Source: Meinrenken, Clifford Algebras and Lie Groups, Prop. 2.3 · Figueroa-O'Farrill, Spin Geometry, Def. 1.1, §1.2.2 · the Minkowski case stated in [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^rem-cb-10-1|§CB.10, ★ Remark: The Clifford algebra is the algebra of square roots of p²]]*

^thm-cb-10-7

> [!proof]- Proof
> *Source: E. Meinrenken, Clifford Algebras and Lie Groups, lecture notes (Toronto, Fall 2009), Ch. 2 §2.2, Prop. 2.3 and its proof (https://www.math.toronto.edu/mein/teaching/LieClifford/cl12.pdf; same sign convention as here) · J. Figueroa-O'Farrill, Spin Geometry, lecture notes (Edinburgh 2010, version of 18 May 2017), §1.2.2, eqs. (12)–(15) (https://empg.maths.ed.ac.uk/Activities/Spin/SpinNotes.pdf, read via the Internet Archive copy of 27 Sep 2024; his relation is $x^2 = -Q(x)$). Both leave Steps 1–2 to the reader; they are written out here.*
>
> **Step 1** (extension to each tensor power). For $k \ge 1$ the map $\Gamma_k(v_1, \dots, v_k) = f(v_1)f(v_2)\cdots f(v_k)$ from $V\times\cdots\times V$ to $A$ is $k$-linear, because $f$ is linear and the product of $A$ is bilinear. By [[§38 Tensor Products#^ladr-9-92|LADR Thm. 9.92]] there is a unique linear map $F_k : V^{\otimes k} \to A$ with
>
> $$
> F_k(v_1\otimes\cdots\otimes v_k) = f(v_1)\cdots f(v_k) .
> $$
>
> Put $F_0(\lambda) = \lambda 1_A$ on $V^{\otimes 0} = \mathbb K$, and let $F : T(V) \to A$ be $F_k$ on the summand $V^{\otimes k}$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-2|Def. §CB.10.2]]), extended linearly.
>
> **Step 2** ($F$ is an algebra homomorphism). For pure tensors $a = v_1\otimes\cdots\otimes v_k$ and $b = w_1\otimes\cdots\otimes w_l$,
>
> $$
> F(ab) = F(v_1\otimes\cdots\otimes v_k\otimes w_1\otimes\cdots\otimes w_l) = f(v_1)\cdots f(v_k)\,f(w_1)\cdots f(w_l) = F(a)F(b),
> $$
>
> and if $k = 0$ or $l = 0$ one factor is a scalar $\lambda$, with $F(\lambda b) = \lambda F(b) = F(\lambda)F(b)$. Both sides of $F(ab) = F(a)F(b)$ are bilinear in $(a, b)$, and the pure tensors span each $V^{\otimes k}$ ([[§38 Tensor Products#^ladr-9-90|LADR Thm. 9.90]]: products of basis vectors are a basis), so $F(ab) = F(a)F(b)$ for all $a, b \in T(V)$; and $F(1) = 1_A$.
>
> **Step 3** ($F$ kills the ideal). On a generator of $I_q$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-6|Def. §CB.10.6]]):
>
> $$
> F\bigl(v\otimes v - q(v)1\bigr) = f(v)f(v) - q(v)1_A = 0
> $$
>
> by the hypothesis $f(v)^2 = q(v)1_A$. Every element of $I_q$ is a sum of terms $a\,s\,b$ with $a, b \in T(V)$ and $s$ a generator ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-3|Def. §CB.10.3]]), and $F(asb) = F(a)F(s)F(b) = F(a)\cdot0\cdot F(b) = 0$ by Step 2. So $F(I_q) = 0$.
>
> **Step 4** (existence). By [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-5|Theorem §CB.10.5]], $F$ factors through $\mathrm{Cl}(V, q) = T(V)/I_q$: there is an algebra homomorphism $\tilde f$ with $\tilde f(x + I_q) = F(x)$. For $v \in V$, $\tilde f(v) = F_1(v) = f(v)$.
>
> **Step 5** (uniqueness). $\mathrm{Cl}(V, q)$ is spanned by the images of pure tensors, i.e. by $1$ and the products $v_1v_2\cdots v_k$ (Step 2's spanning statement, pushed through the quotient map). An algebra homomorphism $g$ with $g(v) = f(v)$ satisfies $g(1) = 1_A$ and $g(v_1\cdots v_k) = g(v_1)\cdots g(v_k) = f(v_1)\cdots f(v_k) = \tilde f(v_1\cdots v_k)$; two linear maps that agree on a spanning set are equal, so $g = \tilde f$.
>
> **What the proof shows.**
> - ⚑ By-product: Steps 1–2 are the universal property of the tensor algebra itself (every linear map $V \to A$ extends uniquely to an algebra homomorphism $T(V) \to A$, Figueroa-O'Farrill eq. (12)); the Clifford algebra adds exactly one relation, and Step 3 is the only place the hypothesis $f(v)^2 = q(v)$ enters.
> - The proof does not show that $V \to \mathrm{Cl}(V, q)$ is injective or that $\mathrm{Cl}(V, q) \ne 0$; that needs a module, Theorem §CB.11.6.
> - Used next: Clifford modules (Theorem §CB.10.10), the grade automorphism and the reversal (Theorems §CB.11.1, §CB.11.4), the even subalgebra (Theorem §CB.11.16), complexification (Theorem §CB.12.3).

^pf-cb-10-7

*Uses:* [[§38 Tensor Products#^ladr-9-92|LADR Thm. 9.92]], [[§38 Tensor Products#^ladr-9-90|LADR Thm. 9.90]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-2|Def. §CB.10.2]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-3|Def. §CB.10.3]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-5|Theorem §CB.10.5]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-6|Def. §CB.10.6]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-8|Def. §CB.6.8]]

> [!theorem] Theorem §CB.10.8: The Anticommutator and the Embedding of V
> In $\mathrm{Cl}(V, q)$, $vw + wv = 2B(v, w)$ for all $v, w \in V$; in an orthogonal basis $e_ie_j = -e_je_i$ ($i \ne j$) and $e_i^2 = q(e_i)$. The map $V \to \mathrm{Cl}(V, q)$ is injective.
>
> *Source: Woit, §29.2, eq. (29.2) · Meinrenken, Clifford Algebras and Lie Groups, Prop. 2.2 (injectivity)*

^thm-cb-10-8

> [!proof]- Proof
> *Source: the anticommutator: Woit, Quantum Theory, Groups and Representations, §29.2, eq. (29.2) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · injectivity: E. Meinrenken, Clifford Algebras and Lie Groups, lecture notes (Toronto, Fall 2009), Ch. 2 §2.1, Prop. 2.2 (https://www.math.toronto.edu/mein/teaching/LieClifford/cl12.pdf), and J. Figueroa-O'Farrill, Spin Geometry, §1.4.4, Lemma 1.7 and the remark after it, both by letting $\mathrm{Cl}(V, q)$ act on $\Lambda V$; that module is constructed in the proof of Theorem §CB.11.6, which uses only Step 1 below.*
>
> **Step 1** (the anticommutator). Apply $uu = q(u)$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-6|Def. §CB.10.6]]) to $u = v + w$ and expand the product into its four terms:
>
> $$
> (v + w)(v + w) = vv + vw + wv + ww = q(v) + vw + wv + q(w), \qquad (v + w)(v + w) = q(v + w) .
> $$
>
> Hence $vw + wv = q(v + w) - q(v) - q(w) = 2B(v, w)$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-1|Def. §CB.10.1]]). For orthogonal $e_i$, $e_j$ with $i \ne j$ the right side is $0$, so $e_ie_j = -e_je_i$; for $i = j$ it reads $2e_ie_i = 2q(e_i)$.
>
> **Step 2** (injectivity). Choose an orthogonal basis $e_1, \dots, e_n$ of $V$ ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-12|LADR Thm. 9.12]] (a)⇒(d), over $\mathbb R$ or $\mathbb C$; it exists for every symmetric form, degenerate or not). By [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-6|Theorem §CB.11.6]] the $2^n$ products $e_I$ are linearly independent in $\mathrm{Cl}(V, q)$; in particular the $n$ elements $e_{\{1\}} = e_1, \dots, e_{\{n\}} = e_n$ are. The map $V \to \mathrm{Cl}(V, q)$ is linear and sends $v = \sum_iv^ie_i$ to $\sum_iv^ie_i$ computed in $\mathrm{Cl}(V, q)$; if this is $0$, independence gives every $v^i = 0$, so $v = 0$.
>
> **What the proof shows.**
> - Step 1 is the bridge between the abstract relation $vv = q(v)$ and the form in which physics uses it, $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$: polarization turns the square of one vector into the anticommutator of two.
> - ⚑ By-product: injectivity is not automatic from the quotient construction (the ideal $I_q$ mixes degrees $0$ and $2$); it needs a nonzero module in which the vectors act independently, which is why the proof passes through Theorem §CB.11.6.

^pf-cb-10-8

*Uses:* [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-1|Def. §CB.10.1]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-6|Def. §CB.10.6]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-12|LADR Thm. 9.12]], [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-6|Theorem §CB.11.6]]

## Clifford modules

> [!definition] Definition §CB.10.9: Clifford Module
> A **Clifford module** of $(V, q)$ is a representation of the algebra $\mathrm{Cl}(V, q)$ on a complex vector space $W$ ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-9|Def. §CB.6.9]]): an algebra homomorphism $\gamma : \mathrm{Cl}(V, q) \to \operatorname{End}_{\mathbb C}(W)$. Invariant subspaces, irreducibility, intertwiners and equivalence are those of Def. §CB.6.9.
>
> *Source (planned): written here*

^def-cb-10-9

> [!theorem] Theorem §CB.10.10: A Clifford Module Is a Set of Anticommuting Square Roots
> Clifford modules of $(V, q)$ on $W$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-9|Def. §CB.10.9]]) correspond bijectively, by restriction to $V$, to linear maps $\gamma : V \to \operatorname{End}(W)$ with $\gamma(v)^2 = q(v)\mathbb 1$ for all $v$; equivalently, for a basis $e_\mu$ of $V$ with $B(e_\mu, e_\nu) = g_{\mu\nu}$, to matrices $\gamma_\mu = \gamma(e_\mu)$ with $\gamma_\mu\gamma_\nu + \gamma_\nu\gamma_\mu = 2g_{\mu\nu}\mathbb 1$.
>
> *Source: Meinrenken, Clifford Algebras and Lie Groups, Prop. 2.3 · written here (from Theorem §CB.10.7 and Theorem §CB.10.8)*

^thm-cb-10-10

> [!proof]- Proof
> *Source: E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2 §2.2, Prop. 2.3 (stated there with the anticommutator form of the hypothesis, $f(v_1)f(v_2) + f(v_2)f(v_1) = 2B(v_1, v_2)$) · the specialization to $A = \operatorname{End}(W)$ written here.*
>
> **Step 1** (module → square roots). If $\gamma : \mathrm{Cl}(V, q) \to \operatorname{End}(W)$ is a Clifford module ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-9|Def. §CB.10.9]]), its restriction to $V$ is linear and $\gamma(v)^2 = \gamma(vv) = \gamma(q(v)1) = q(v)\mathbb 1$, since $\gamma$ is multiplicative and unital.
>
> **Step 2** (square roots → module). If $\gamma : V \to \operatorname{End}(W)$ is linear with $\gamma(v)^2 = q(v)\mathbb 1$, [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-7|Theorem §CB.10.7]] with $A = \operatorname{End}(W)$ (an associative algebra with unit $\mathbb 1$, [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-7|Def. §CB.6.7]]) gives a unique algebra homomorphism $\tilde\gamma : \mathrm{Cl}(V, q) \to \operatorname{End}(W)$ extending it.
>
> **Step 3** (the two operations are inverse). Restricting $\tilde\gamma$ to $V$ gives back $\gamma$ by construction. Conversely, a module $\gamma$ is an algebra homomorphism extending its own restriction, so by the uniqueness in Theorem §CB.10.7 it equals the extension built in Step 2 from that restriction.
>
> **Step 4** (matrix form). Let $e_\mu$ be a basis with $B(e_\mu, e_\nu) = g_{\mu\nu}$ and $\gamma_\mu = \gamma(e_\mu)$. If $\gamma(v)^2 = q(v)\mathbb 1$ for all $v$, apply it to $v = e_\mu + e_\nu$ and expand, as in Step 1 of [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-8|Theorem §CB.10.8]]:
>
> $$
> \gamma_\mu^2 + \gamma_\mu\gamma_\nu + \gamma_\nu\gamma_\mu + \gamma_\nu^2 = q(e_\mu + e_\nu)\mathbb 1 = \bigl(q(e_\mu) + 2g_{\mu\nu} + q(e_\nu)\bigr)\mathbb 1,
> $$
>
> and subtracting $\gamma_\mu^2 = q(e_\mu)\mathbb 1$, $\gamma_\nu^2 = q(e_\nu)\mathbb 1$ gives $\gamma_\mu\gamma_\nu + \gamma_\nu\gamma_\mu = 2g_{\mu\nu}\mathbb 1$ (for $\mu = \nu$ this is $2\gamma_\mu^2 = 2g_{\mu\mu}\mathbb 1$ directly). Conversely, if the matrices satisfy the anticommutation relations, then for $v = v^\mu e_\mu$, expanding $\gamma(v)^2 = v^\mu v^\nu\gamma_\mu\gamma_\nu$ and symmetrizing in $\mu\leftrightarrow\nu$,
>
> $$
> \gamma(v)^2 = \tfrac12v^\mu v^\nu(\gamma_\mu\gamma_\nu + \gamma_\nu\gamma_\mu) = v^\mu v^\nu g_{\mu\nu}\mathbb 1 = q(v)\mathbb 1 .
> $$
>
> **What the proof shows.**
> - A set of Dirac matrices is nothing more and nothing less than a module of one fixed algebra: every algebraic consequence of $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ (traces, the sixteen products, $\gamma^5$) holds in every module because it already holds in $\mathrm{Cl}(V, q)$.
> - Used in: Pauli's theorem in general form (Theorem §CB.12.10) and the Dirac maps of [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-13|Def. §CB.10.13]].

^pf-cb-10-10

*Uses:* [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-7|Theorem §CB.10.7]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-8|Theorem §CB.10.8]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-9|Def. §CB.10.9]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-7|Def. §CB.6.7]]

## The Dirac matrices: the course's Clifford module

The course's Clifford module (PHY 513 Lecture 7, Part B): four matrices, or four linear maps on spinor space, with $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$, the relation of Theorem §CB.10.10, 2 for $V = \mathbb R^{1,3}$ (which of $e_\mu \mapsto \gamma_\mu$, $e_\mu \mapsto \gamma^\mu$ is used matters only for signs: [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^cau-cb-17-1|§CB.17, Caution: Two Dirac modules, and the sign of γ⁵]]). The statements were first written in the physics chapter ([[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]]) and keep its notation: $V$ is spinor space, a four-dimensional complex vector space, and the matrices are $n\times n$ until §CB.12 shows $n = 4$.

> [!definition] Definition §CB.10.11: The Dirac Matrices
> **Dirac matrices** ($\gamma$ matrices) are four $n\times n$ complex matrices $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ satisfying the **Clifford** (Dirac) **algebra**
>
> $$
> \{\gamma^\mu, \gamma^\nu\} \equiv \gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2g^{\mu\nu}\,\mathbb 1_n .
> $$
>
> The label $\mu$ is a spacetime index; the rows and columns are spinor indices (index slots: [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^def-c3-1-1|Def. §C3.1.1]]). $g^{\mu\nu}$ is the metric and $\gamma_\mu \equiv g_{\mu\nu}\gamma^\nu$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]]).
>
> *Source: PS §3.2, eq. (3.22) · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The Dirac (Clifford) algebra", eq. (clifford)) · PHY 513 Lecture 7, Part B ("Warning: 4 × 4 identity matrix on RHS usually not written") · Yu §5.1, eq. (5.1)*

^def-cb-10-11

> [!theorem] Theorem §CB.10.12: First Consequences of the Clifford Algebra
> For Dirac matrices ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]]):
> 1. $(\gamma^0)^2 = \mathbb 1$, $(\gamma^i)^2 = -\mathbb 1$, and $\gamma^\mu\gamma^\nu = -\gamma^\nu\gamma^\mu$ for $\mu \ne \nu$; each $\gamma^\mu$ is invertible.
> 2. For every four-vector $a$ with commuting components, $(a_\mu\gamma^\mu)^2 = a_\mu a^\mu\,\mathbb 1$.
> 3. *The split.* Every product of two Dirac matrices is its symmetric part plus its antisymmetric part:
>
> $$
> \gamma^\mu\gamma^\nu = \tfrac12\{\gamma^\mu, \gamma^\nu\} + \tfrac12[\gamma^\mu, \gamma^\nu] = g^{\mu\nu}\,\mathbb 1 + \tfrac12[\gamma^\mu, \gamma^\nu] .
> $$
>
> Contracted with a symmetric tensor only $g^{\mu\nu}\mathbb 1$ survives; contracted with an antisymmetric one only the commutator survives.
>
> *Source: Yu §5.1, eqs. (5.2)–(5.4) · the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Square to ±1, or square root?") · PS §3.2, p. 43 (the same step in Dirac ⇒ Klein–Gordon) · item 3: the user's PHY 513 notes use its symmetric half in Ch. 8 (sections "The Dirac representation", "Dirac implies Klein–Gordon", "Plane waves and an eigenvalue problem") and its antisymmetric half for the slash algebra (Ch. 9 §9.6, Problem Set 5)*

^thm-cb-10-12

> [!derivation]- Derivation
> **1. Squares.** Put $\nu = \mu$: $2(\gamma^\mu)^2 = 2g^{\mu\mu}\mathbb 1$ (no sum), so $(\gamma^0)^2 = g^{00} = 1$ and $(\gamma^i)^2 = g^{ii} = -1$. Hence $(\gamma^0)^{-1} = \gamma^0$ and $(\gamma^i)^{-1} = -\gamma^i$.
>
> **2. Distinct indices.** For $\mu \ne \nu$, $g^{\mu\nu} = 0$, so $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 0$.
>
> **3. Square root.** $(a_\mu\gamma^\mu)^2 = a_\mu a_\nu\gamma^\mu\gamma^\nu$. The coefficient $a_\mu a_\nu$ is symmetric in $\mu\nu$, so only the symmetric part of $\gamma^\mu\gamma^\nu$ contributes: $a_\mu a_\nu\gamma^\mu\gamma^\nu = \frac12a_\mu a_\nu(\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu) = a_\mu a_\nu g^{\mu\nu}\mathbb 1 = a^2\mathbb 1$.
>
> **4. The split.** Add and subtract $\frac12\gamma^\nu\gamma^\mu$: $\gamma^\mu\gamma^\nu = \frac12(\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu) + \frac12(\gamma^\mu\gamma^\nu - \gamma^\nu\gamma^\mu)$. The first bracket is $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}\mathbb 1$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]]). For a symmetric $S_{\mu\nu}$, $S_{\mu\nu}[\gamma^\mu, \gamma^\nu] = 0$: renaming the dummy indices $\mu \leftrightarrow \nu$ turns it into its own negative. For an antisymmetric $A_{\mu\nu}$, $A_{\mu\nu}g^{\mu\nu} = 0$ for the same reason. Step 3 is the case $S_{\mu\nu} = a_\mu a_\nu$.
>
> **What the derivation shows**
> - The algebra says exactly "the $\gamma$'s square to the metric and anticommute"; part 2 is the same statement for every direction at once.
> - Used next: Hermiticity (Theorem §C5a.2.1), the sixteen products (Theorem §CB.11.8), Dirac ⇒ Klein–Gordon ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]]), the slash algebra ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]]).
> - The split is the working trick for products of two γ's. With $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$ it reads $\gamma^\mu\gamma^\nu = g^{\mu\nu} - i\sigma^{\mu\nu}$ ([[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]]); it gives the second form of the spinor generators (Def. §CB.13.15 in §C5a.3), $\slashed a\slashed b = a\cdot b - i\sigma^{\mu\nu}a_\mu b_\nu$ ([[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-1|Theorem §C5a.11.1]]), and, iterated, the reduction of any product of γ's to antisymmetrized products ([[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-8|Theorem §C5a.11.8]]).

^der-cb-10-12

*Uses:* [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]]

## The Clifford action on spinor space

> [!definition] Definition §CB.10.13: The Dirac Maps
> The **Dirac maps** on spinor space $V$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-1|Def. §C5a.1.1]]) are four linear maps $\Gamma^0, \Gamma^1, \Gamma^2, \Gamma^3 \in \operatorname{End}(V)$ with
>
> $$
> \Gamma^\mu\Gamma^\nu + \Gamma^\nu\Gamma^\mu = 2g^{\mu\nu}\,\mathrm{id}_V ,
> $$
>
> $g^{\mu\nu}$ the metric ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]]): a representation of the Clifford algebra on $V$. In a basis their matrices ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-2|Def. §CB.0.2]]) are written $\gamma^\mu$: $\Gamma^\mu e_b = \sum_a(\gamma^\mu)_{ab}e_a$.
>
> *Source: PS §3.2, eq. (3.22), p. 41 ("all 4 × 4 representations of the Dirac algebra are unitarily equivalent") · PHY 513 Lecture 7, Part B ("There are many realizations of $\gamma^\mu$") · Yu §5.1, eq. (5.1) · the basis-free formulation written here*

^def-cb-10-13

> [!theorem] Theorem §CB.10.14: The Matrices of the Dirac Maps in Any Basis
> For the Dirac maps ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-13|Def. §CB.10.13]]):
> 1. in every basis of $V$ the matrices $\gamma^\mu$ are Dirac matrices ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]]), and under a change of basis $\gamma'^\mu = U\gamma^\mu U^{-1}$;
> 2. every operator built from the $\Gamma^\mu$ by sums, products, multiplication by numbers and convergent power series has, in each basis, the matrix given by the same formula in that basis's $\gamma$'s, and these matrices transform as $U(\cdot)U^{-1}$.
>
> *Source: Yu §5.2, eq. (5.72) · the user's PHY 513 notes, Ch. 8 §8.1 ("Uniqueness": "the choice of basis is a convention") · part 2 written here*

^thm-cb-10-14

> [!derivation]- Derivation
> **1. Clifford relation in a basis.** By Theorem §CB.0.3 the matrix of $\Gamma^\mu\Gamma^\nu + \Gamma^\nu\Gamma^\mu$ is $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu$ and that of $2g^{\mu\nu}\mathrm{id}$ is $2g^{\mu\nu}\mathbb 1$; equal operators have equal matrices. The rule $\gamma'^\mu = U\gamma^\mu U^{-1}$ is Theorem §CB.0.5 with $M = \Gamma^\mu$. (Directly: $\{U\gamma^\mu U^{-1}, U\gamma^\nu U^{-1}\} = U\{\gamma^\mu, \gamma^\nu\}U^{-1} = 2g^{\mu\nu}\mathbb 1$, Yu (5.72).)
>
> **2. Products.** If operators $A$, $B$ have matrices $a$, $b$ in the old basis, $AB$ has the matrix $ab$ (Theorem §CB.0.3), and in the new basis, inserting $U^{-1}U = \mathbb 1$ between the factors, $a'b' = UaU^{-1}UbU^{-1} = U(ab)U^{-1}$; sums and multiples go the same way. By induction on the number of factors, every polynomial in the $\Gamma^\mu$ has matrix "the same polynomial in the $\gamma$'s", and computing it from the new $\gamma$'s gives $U(\cdot)U^{-1}$ of the old one. For example $i\gamma'^0\gamma'^1\gamma'^2\gamma'^3 = iU\gamma^0U^{-1}U\gamma^1U^{-1}U\gamma^2U^{-1}U\gamma^3U^{-1} = U(i\gamma^0\gamma^1\gamma^2\gamma^3)U^{-1}$, and $[\gamma'^\mu, \gamma'^\nu] = U[\gamma^\mu, \gamma^\nu]U^{-1}$.
>
> **3. Power series.** For a matrix $A$: $(UAU^{-1})^n = UA^nU^{-1}$ (the inner $U^{-1}U$ cancel), so term by term $\sum_nc_n(UAU^{-1})^n = U\bigl(\sum_nc_nA^n\bigr)U^{-1}$ wherever the series converges absolutely (multiplication by fixed matrices is continuous). In particular $\exp(UAU^{-1}) = U\,e^A\,U^{-1}$.
>
> **What the derivation shows**
> - Only Theorem §CB.0.3 (operators ↔ matrices) and the cancellation $U^{-1}U = \mathbb 1$ are used.
> - Instances defined later: $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ ([[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-11-13|Def. §CB.11.13]]), $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-15|Def. §CB.13.15]]) and $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-18|Def. §CB.13.18]]): computed from the new $\gamma$'s, each is the transformed old one, $\gamma'^5 = U\gamma^5U^{-1}$, $S'^{\mu\nu} = US^{\mu\nu}U^{-1}$, $\Lambda'_{1/2} = U\Lambda_{1/2}U^{-1}$ (steps 2–3).
> - Used next: the eigenvalues ([[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-9|Theorem §CB.11.9]]) and changes of basis as intertwiners (Theorem §CB.12.13).

^der-cb-10-14

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-3|Theorem §CB.0.3]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5|Theorem §CB.0.5]]

The first structural consequence of the relation, in any unital algebra:

> [!theorem] Theorem §CB.10.15: Clifford Generators Are Invertible and Pairwise Non-Commuting
> Let $\gamma^0, \dots, \gamma^3$ satisfy the Clifford relation $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}1$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]]) in an associative algebra with unit $1 \ne 0$: numbers, $n\times n$ matrices, or linear maps on a vector space. Then
> 1. each $\gamma^\mu$ is invertible, with $(\gamma^\mu)^{-1} = g^{\mu\mu}\gamma^\mu$ (no sum);
> 2. $\gamma^\mu\gamma^\nu \ne \gamma^\nu\gamma^\mu$ for every $\mu \ne \nu$;
> 3. no basis makes all four $n\times n$ Dirac matrices diagonal at once: the Dirac maps have no common eigenbasis.
>
> *Source: PS §3.2, p. 41 ("There is no fourth $2\times2$ matrix … that anticommutes with the three Pauli sigma matrices", the matrix version) · the user's PHY 513 notes, Ch. 8 §8.1 ("Square to ±1, or square root?") · the argument written here (first written for the physics statement, [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-2|Theorem §C5a.0.2]])*

^thm-cb-10-15

> [!derivation]- Derivation
> **1. Inverses.** By the relation with $\nu = \mu$, $(\gamma^\mu)^2 = g^{\mu\mu}1$ (no sum), with $g^{\mu\mu} = \pm1$, so $(g^{\mu\mu})^2 = 1$. Then $\gamma^\mu\cdot g^{\mu\mu}\gamma^\mu = g^{\mu\mu}(\gamma^\mu)^2 = (g^{\mu\mu})^2\,1 = 1$, and the same with the factors in the other order: $(\gamma^\mu)^{-1} = g^{\mu\mu}\gamma^\mu$.
>
> **2. Assume two of them commute.** Suppose $\gamma^\mu\gamma^\nu = \gamma^\nu\gamma^\mu$ for some $\mu \ne \nu$. Then $\{\gamma^\mu, \gamma^\nu\} = \gamma^\mu\gamma^\nu + \gamma^\mu\gamma^\nu = 2\gamma^\mu\gamma^\nu$, while the relation gives $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}1 = 0$, because $g$ is diagonal. So $\gamma^\mu\gamma^\nu = 0$.
>
> **3. Then one of them vanishes.** Multiply $\gamma^\mu\gamma^\nu = 0$ on the left by $(\gamma^\mu)^{-1}$ (step 1): $\gamma^\nu = (\gamma^\mu)^{-1}\gamma^\mu\gamma^\nu = (\gamma^\mu)^{-1}\cdot0 = 0$.
>
> **4. Contradiction.** Then $(\gamma^\nu)^2 = 0$, but the relation demands $(\gamma^\nu)^2 = g^{\nu\nu}1 = \pm1 \ne 0$, because $1 \ne 0$. So no two distinct $\gamma$'s commute: part 2.
>
> **5. No common diagonal form.** Diagonal matrices commute: $\operatorname{diag}(a_1, \dots, a_n)\operatorname{diag}(b_1, \dots, b_n) = \operatorname{diag}(a_1b_1, \dots, a_nb_n) = \operatorname{diag}(b_1, \dots, b_n)\operatorname{diag}(a_1, \dots, a_n)$. If one basis made all $\gamma^\mu$ diagonal, they would commute, against part 2. Since a change of basis changes the matrices by $U(\cdot)U^{-1}$ and keeps the relation ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-14|Theorem §CB.10.14]]), this holds in every basis: the Dirac maps have no common eigenbasis.
>
> **What the derivation shows**
> - Only the relation and $1 \ne 0$ were used, and only two of the $\gamma$'s: the conclusion holds in any spacetime dimension with at least one time and one space direction (Example §CB.11.18).
> - Read for the physics: a first-order square root of the Klein–Gordon operator needs matrices, not numbers ([[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-2|Theorem §C5a.0.2]]).

^der-cb-10-15

*Uses:* [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-14|Theorem §CB.10.14]]

In the course's words, the Clifford relation of Minkowski space generates the algebra of square roots of $p^2$: the case $V = \mathbb R^{1,3}$ of Def. §CB.10.6 and Theorem §CB.10.7. The remark below was written in the physics chapter before this section existed; the construction as a quotient of the tensor algebra, which it calls missing from the vault, is Def. §CB.10.6.

> [!remark] ★ Remark: The Clifford algebra is the algebra of square roots of p²
> **The algebra.** On Minkowski space $M$ ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]]) the metric $g$ is a symmetric bilinear form with quadratic form $q(v) = g(v, v)$ ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-9|LADR Def. 9.9]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-18|LADR Def. 9.18]]). The **Clifford algebra** $\mathrm{Cl}(1,3)$ is the associative algebra with unit generated by the vectors $v \in M$, added as in $M$, subject to the single relation
>
> $$
> v\,v = g(v, v)\,1 \qquad (v \in M) :
> $$
>
> every vector is a square root of its own length squared. Replacing $v$ by $v + w$ gives $vw + wv = 2g(v, w)\,1$; on a basis $e_\mu$ of $M$, with $\gamma_\mu$ the image of $e_\mu$ and $\gamma^\mu = g^{\mu\nu}\gamma_\nu$, this is $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]]). Dirac's requirement, a first-order factor of the Klein–Gordon operator, is exactly this relation ([[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]]): $\mathrm{Cl}(1,3)$ is the algebra of square roots of $p^2$ with no further relations.
>
> **Universal property.** If $A$ is an associative algebra with unit and $f : M \to A$ is linear with $f(v)^2 = g(v, v)\,1$ for all $v$, then $f$ extends uniquely to an algebra homomorphism $\mathrm{Cl}(1,3) \to A$. A choice of Dirac matrices is such an $f$, $f(p) = \slashed{p} = p_\mu\gamma^\mu$, into $A = M_4(\mathbb C)$; the Dirac maps are one into $\operatorname{End}(V)$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-13|Def. §CB.10.13]]). Compare the tensor product, which turns bilinear maps into linear ones ([[§38 Tensor Products#^ladr-9-79|LADR Thm. 9.79]]); the construction of $\mathrm{Cl}(1,3)$ as a quotient of the tensor algebra is not in the vault. After complexification $\mathrm{Cl}(1,3)\otimes\mathbb C \cong M_4(\mathbb C)$ ([[§CB.12 Complex Clifford Algebras and Clifford Modules#^rem-cb-12-1|§CB.12, ★ Remark: The complexified Clifford algebra is the full matrix algebra]]).
>
> *Source: written here, on the concrete content of Theorem §C5a.0.1; no course source states the Clifford algebra of a quadratic form or its universal property, and the vault has no Math home for Clifford algebras · the relation: PS §3.2, eq. (3.22) and p. 43; the user's PHY 513 notes, Ch. 8 §8.1 · the rows: the homes linked in the table*

^rem-cb-10-1

> [!remark]- Connections
> - The universal property (Theorem §CB.10.7) is the whole reason Dirac matrices are unique up to change of basis: a Clifford module is a homomorphism out of one fixed algebra, and §CB.12 shows that algebra (complexified) is a matrix algebra.
> - **Used in**: Definitions §CB.10.6–Theorem §CB.10.10 — [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-2|Theorem §C5a.0.2]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-12|Theorem §CB.10.12]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-13|Def. §CB.10.13]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^def-cb-17-1|Def. §CB.17.1]]; Theorem §CB.10.10 — [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]] (embedded); Definition §CB.10.11 — [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded; cited in [[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|Def. §C3.3.2]]), [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]] (embedded; cited in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]]), [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded), [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]] (embedded; cited in [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]]), [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field|§C5a.8]] (embedded; cited in [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-2|Theorem §C5a.8.2]], [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-9|Theorem §C5a.8.9]]), [[§C5a.9 Plane-Wave Solutions|§C5a.9]] (embedded; cited in [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-2|Theorem §C5a.9.2]]), [[§C5a.11 Gamma-Matrix Technology|§C5a.11]] (embedded; cited in [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-1|Theorem §C5a.11.1]], [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-2|Theorem §C5a.11.2]], [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-3|Theorem §C5a.11.3]], [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-8|Theorem §C5a.11.8]]), [[§C5b.2 Mode Expansion and the Anticommutator Algebra|§C5b.2]] (embedded; cited in [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]]), [[§C5b.3 Energy, Momentum and the Zero-Point Energy|§C5b.3]] (embedded; cited in [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-1|Theorem §C5b.3.1]]), [[§C9.4 Fermion Bilinears under Parity|§C9.4]] (embedded; cited in [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-3|Theorem §C9.4.3]]); Theorem §CB.10.12 — [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]] (embedded; cited in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]]), [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded), [[§C5a.2 The Dirac Form|§C5a.2]] (embedded; cited in [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]]), [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]] (embedded; cited in [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]]), [[§C5a.9 Plane-Wave Solutions|§C5a.9]] (embedded; cited in [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]]), [[§C5a.11 Gamma-Matrix Technology|§C5a.11]] (embedded; cited in [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-1|Theorem §C5a.11.1]]); Definition §CB.10.13 — [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]] (embedded; cited in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-1|§C5a.0, Remark: Why the Dirac maps: the logic runs from γ to spinor space]]), [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded); Theorem §CB.10.14 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded), [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]] (embedded; cited in [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-2|Theorem §C5a.7.2]]); Theorem §CB.10.15 — [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]] (embedded; cited in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-2|Theorem §C5a.0.2]]); §CB.10, Remark: The Clifford algebra is the algebra of square roots of p² — [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]] (embedded; cited in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-2|§C5a.0, Remark: What the Clifford relation induces]]).
