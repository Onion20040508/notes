---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.9
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element]] →

*Sources: E. Meinrenken, Clifford Algebras and Lie Groups, lecture notes, University of Toronto, Fall 2009, Ch. 1–2 (https://www.math.toronto.edu/mein/teaching/LieClifford/cl12.pdf; convention $vw + wv = 2B(v, w)$, as here) · J. Figueroa-O'Farrill, Spin Geometry, lecture notes, Edinburgh 2010, version of 18 May 2017, Lectures 1–3 (https://empg.maths.ed.ac.uk/Activities/Spin/SpinNotes.pdf, read via the Internet Archive copy of 27 Sep 2024; convention $x^2 = -Q(x)$) · P. Woit, Quantum Theory, Groups and Representations, Ch. 28–29 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf; convention $[\gamma_j, \gamma_k]_+ = 2\delta_{jk}$, as here) · Linear Algebra (LADR) §§11, 35–38 · the user's PHY 513 notes, Ch. 8 · Peskin & Schroeder, §3.2, §3.4 · the rest written here.*

What is the algebra that the Dirac matrices generate, defined without matrices? The spinor chapter meets it as the relation $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]) and as a ★ remark ([[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-2|§C5a.0, ★ Remark: The Clifford algebra is the algebra of square roots of p²]]). This section defines the Clifford algebra $\mathrm{Cl}(V, q)$ of a quadratic space as a quotient of the tensor algebra, states its universal property, and introduces Clifford modules; its structure — the $\mathbb Z_2$-grading, the reversal, the basis $e_I$ and $\dim = 2^n$, the identification with $\Lambda V$ as a vector space, the volume element (the abstract $\gamma^5$), the even subalgebra, and the low-dimensional examples — is derived in [[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element|§CB.10]]. Representations of algebras are [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-5-10|Def. §CB.5.10]]; exterior powers are [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-6-12|Def. §CB.6.12]]. The complex theory is [[§CB.11 Complex Clifford Algebras and Clifford Modules|§CB.11]]; the spin group, [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.12]].

<!-- MOVE row (CB-INVENTORY): ★ Remark rem-c5a-0-2 (definition and universal property) is embedded below; its definition and universal property are to be moved here when this section is written (batch 5; SPEC-CB groups the §C5a.0/§C5a.1 moves with batch 6 — settle then); the "what the relation induces" table stays in §C5a.0. -->

## Quadratic spaces, the tensor algebra and quotients

Quadratic forms and their bilinear forms, defined in LADR:

![[§35 Bilinear Forms and Quadratic Forms#^ladr-9-18]]

> [!definition] Definition §CB.9.1: Quadratic Space
> A **quadratic space** $(V, q)$ over $\mathbb K = \mathbb R$ or $\mathbb C$ is a finite-dimensional $\mathbb K$-vector space $V$ with a quadratic form $q$ ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-18|LADR Def. 9.18]]), $q(v) = B(v, v)$ for the symmetric bilinear form $B(v, w) = \frac12\bigl(q(v + w) - q(v) - q(w)\bigr)$. It is **nondegenerate** if $B(v, \cdot) = 0$ implies $v = 0$. A basis $e_1, \dots, e_n$ is **orthogonal** if $B(e_i, e_j) = 0$ for $i \ne j$, **orthonormal** if moreover $q(e_i) = \pm1$ (over $\mathbb C$: $q(e_i) = 1$). $\mathbb R^{r,s}$ denotes $\mathbb R^{r+s}$ with $q(x) = x_1^2 + \cdots + x_r^2 - x_{r+1}^2 - \cdots - x_{r+s}^2$; Minkowski space is $\mathbb R^{1,3}$ with $q(x) = g(x, x)$ ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]]).
>
> *Source (planned): LADR §35 (orthogonal bases: Thm. 9.12) · written here*

^def-cb-9-1

> [!definition] Definition §CB.9.2: Tensor Algebra
> The **tensor algebra** of a $\mathbb K$-vector space $V$ is $T(V) = \bigoplus_{k\ge0}V^{\otimes k}$ ($V^{\otimes0} = \mathbb K$, $V^{\otimes k}$ of [[§38 Tensor Products#^ladr-9-88|LADR Def. 9.88]]), an associative algebra ([[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-5-8|Def. §CB.5.8]]) with the product $(v_1\otimes\cdots\otimes v_k)(w_1\otimes\cdots\otimes w_l) = v_1\otimes\cdots\otimes v_k\otimes w_1\otimes\cdots\otimes w_l$ extended bilinearly, and unit $1 \in \mathbb K$.
>
> *Source (planned): written here*

^def-cb-9-2

> [!definition] Definition §CB.9.3: Two-Sided Ideal
> A **two-sided ideal** of an associative algebra $A$ is a subspace $I$ with $aI \subset I$ and $Ia \subset I$ for all $a \in A$. The ideal **generated** by a subset $S$ is the smallest one containing $S$: the span of all $asb$ with $a, b \in A$, $s \in S$.
>
> *Source (planned): written here*

^def-cb-9-3

> [!definition] Definition §CB.9.4: Quotient Algebra
> For a two-sided ideal $I$ of $A$ ([[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-3|Def. §CB.9.3]]), the **quotient algebra** $A/I$ is the quotient space ([[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR Def. 3.99]]) with the product $(a + I)(b + I) = ab + I$.
>
> *Source (planned): written here*

^def-cb-9-4

> [!theorem] Theorem §CB.9.5: The Quotient Is an Algebra
> The product of [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-4|Def. §CB.9.4]] is well defined, $A/I$ is an associative algebra with unit $1 + I$, and $a \mapsto a + I$ is a surjective algebra homomorphism ([[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-5-9|Def. §CB.5.9]]) with kernel $I$. An algebra homomorphism $f : A \to B$ with $f(I) = 0$ factors uniquely through $A/I$.
>
> *Source (planned): written here*

^thm-cb-9-5

> [!proof]- Proof
> If $a' = a + i$, $b' = b + j$ with $i, j \in I$, then $a'b' = ab + (aj + ib + ij)$, and each of $aj$, $ib$, $ij$ lies in $I$ because $I$ is a two-sided ideal; so $a'b' + I = ab + I$. Associativity, bilinearity and the unit pass from $A$ to the cosets term by term. The map $a \mapsto a + I$ is linear, multiplicative by the definition of the product, onto, and sends $a$ to $0 + I$ iff $a \in I$. If $f(I) = 0$, put $\bar f(a + I) = f(a)$: well defined since $f(a + i) = f(a)$, and an algebra homomorphism because $f$ is; it is the only map with $\bar f(a + I) = f(a)$.

^pf-cb-9-5

## The Clifford algebra and its universal property

> [!definition] Definition §CB.9.6: Clifford Algebra
> The **Clifford algebra** of a quadratic space $(V, q)$ ([[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-1|Def. §CB.9.1]]) is
>
> $$
> \mathrm{Cl}(V, q) = T(V)/I_q, \qquad I_q = \text{the two-sided ideal generated by } \{v\otimes v - q(v)1 : v \in V\}
> $$
>
> ([[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-2|Def. §CB.9.2]], [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-4|Def. §CB.9.4]]). The image of $v \in V$ is written $v$, and the product in $\mathrm{Cl}(V, q)$ by juxtaposition, so $vv = q(v)$. $\mathrm{Cl}(r, s) = \mathrm{Cl}(\mathbb R^{r,s})$; the Clifford algebra of Minkowski space is $\mathrm{Cl}(1,3)$.
>
> *Source: E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2, Def. 2.1 (same convention) · J. Figueroa-O'Farrill, Spin Geometry, §1.2.2 (ideal generated by $x\otimes x + Q(x)$: the opposite sign) · Woit, §29.2*

^def-cb-9-6

> [!caution] Caution: Two sign conventions for the Clifford relation
> These notes use the physics convention $vv = +q(v)$, which with $q = g$ gives $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]; Woit, §29.2, eq. (29.2), and Meinrenken, Def. 2.1, use the same sign). Much of the mathematical literature (e.g. Figueroa-O'Farrill, Spin Geometry, eq. (2); Lawson–Michelsohn) writes $vv = -q(v)$; its $\mathrm{Cl}(V, q)$ is this section's $\mathrm{Cl}(V, -q)$, and labels such as $\mathrm{Cl}_{r,s}$ or $\mathrm{Cl}(r, s)$ then refer to different algebras. Over $\mathbb C$ the two conventions give isomorphic algebras ($v \mapsto iv$). Here $\mathrm{Cl}(r, s)$ always has $r$ generators squaring to $+1$ and $s$ to $-1$: in $\mathrm{Cl}(1,3)$, $(\gamma^0)^2 = +1$, $(\gamma^i)^2 = -1$.
>
> *Source: SPEC-CB decision 6 · Woit, §29.2 (which notes the other convention) · Meinrenken, Clifford Algebras and Lie Groups, Def. 2.1 · Figueroa-O'Farrill, Spin Geometry, eq. (2) and §1.3.2 (his $C\ell(s,t)$, $s$ generators squaring to $-1$, is this section's $\mathrm{Cl}(t,s)$)*

^cau-cb-9-1

> [!theorem] Theorem §CB.9.7: Universal Property of the Clifford Algebra
> Let $A$ be an associative algebra over $\mathbb K$ ([[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-5-8|Def. §CB.5.8]]) and $f : V \to A$ a linear map with $f(v)^2 = q(v)1_A$ for all $v \in V$. Then there is a unique algebra homomorphism $\tilde f : \mathrm{Cl}(V, q) \to A$ ([[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-5-9|Def. §CB.5.9]]) with $\tilde f(v) = f(v)$ for $v \in V$.
>
> *Source: Meinrenken, Clifford Algebras and Lie Groups, Prop. 2.3 · Figueroa-O'Farrill, Spin Geometry, Def. 1.1, §1.2.2 · the Minkowski case stated in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-2|§C5a.0, ★ Remark]]*

^thm-cb-9-7

> [!proof]- Proof
> *Source: E. Meinrenken, Clifford Algebras and Lie Groups, lecture notes (Toronto, Fall 2009), Ch. 2 §2.2, Prop. 2.3 and its proof (https://www.math.toronto.edu/mein/teaching/LieClifford/cl12.pdf; same sign convention as here) · J. Figueroa-O'Farrill, Spin Geometry, lecture notes (Edinburgh 2010, version of 18 May 2017), §1.2.2, eqs. (12)–(15) (https://empg.maths.ed.ac.uk/Activities/Spin/SpinNotes.pdf, read via the Internet Archive copy of 27 Sep 2024; his relation is $x^2 = -Q(x)$). Both leave Steps 1–2 to the reader; they are written out here.*
>
> **Step 1** (extension to each tensor power). For $k \ge 1$ the map $\Gamma_k(v_1, \dots, v_k) = f(v_1)f(v_2)\cdots f(v_k)$ from $V\times\cdots\times V$ to $A$ is $k$-linear, because $f$ is linear and the product of $A$ is bilinear. By [[§38 Tensor Products#^ladr-9-92|LADR Thm. 9.92]] there is a unique linear map $F_k : V^{\otimes k} \to A$ with
>
> $$
> F_k(v_1\otimes\cdots\otimes v_k) = f(v_1)\cdots f(v_k) .
> $$
>
> Put $F_0(\lambda) = \lambda 1_A$ on $V^{\otimes 0} = \mathbb K$, and let $F : T(V) \to A$ be $F_k$ on the summand $V^{\otimes k}$ ([[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-2|Def. §CB.9.2]]), extended linearly.
>
> **Step 2** ($F$ is an algebra homomorphism). For pure tensors $a = v_1\otimes\cdots\otimes v_k$ and $b = w_1\otimes\cdots\otimes w_l$,
>
> $$
> F(ab) = F(v_1\otimes\cdots\otimes v_k\otimes w_1\otimes\cdots\otimes w_l) = f(v_1)\cdots f(v_k)\,f(w_1)\cdots f(w_l) = F(a)F(b),
> $$
>
> and if $k = 0$ or $l = 0$ one factor is a scalar $\lambda$, with $F(\lambda b) = \lambda F(b) = F(\lambda)F(b)$. Both sides of $F(ab) = F(a)F(b)$ are bilinear in $(a, b)$, and the pure tensors span each $V^{\otimes k}$ ([[§38 Tensor Products#^ladr-9-90|LADR Thm. 9.90]]: products of basis vectors are a basis), so $F(ab) = F(a)F(b)$ for all $a, b \in T(V)$; and $F(1) = 1_A$.
>
> **Step 3** ($F$ kills the ideal). On a generator of $I_q$ ([[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-6|Def. §CB.9.6]]):
>
> $$
> F\bigl(v\otimes v - q(v)1\bigr) = f(v)f(v) - q(v)1_A = 0
> $$
>
> by the hypothesis $f(v)^2 = q(v)1_A$. Every element of $I_q$ is a sum of terms $a\,s\,b$ with $a, b \in T(V)$ and $s$ a generator ([[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-3|Def. §CB.9.3]]), and $F(asb) = F(a)F(s)F(b) = F(a)\cdot0\cdot F(b) = 0$ by Step 2. So $F(I_q) = 0$.
>
> **Step 4** (existence). By [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-9-5|Theorem §CB.9.5]], $F$ factors through $\mathrm{Cl}(V, q) = T(V)/I_q$: there is an algebra homomorphism $\tilde f$ with $\tilde f(x + I_q) = F(x)$. For $v \in V$, $\tilde f(v) = F_1(v) = f(v)$.
>
> **Step 5** (uniqueness). $\mathrm{Cl}(V, q)$ is spanned by the images of pure tensors, i.e. by $1$ and the products $v_1v_2\cdots v_k$ (Step 2's spanning statement, pushed through the quotient map). An algebra homomorphism $g$ with $g(v) = f(v)$ satisfies $g(1) = 1_A$ and $g(v_1\cdots v_k) = g(v_1)\cdots g(v_k) = f(v_1)\cdots f(v_k) = \tilde f(v_1\cdots v_k)$; two linear maps that agree on a spanning set are equal, so $g = \tilde f$.
>
> **What the proof shows.**
> - ⚑ By-product: Steps 1–2 are the universal property of the tensor algebra itself (every linear map $V \to A$ extends uniquely to an algebra homomorphism $T(V) \to A$, Figueroa-O'Farrill eq. (12)); the Clifford algebra adds exactly one relation, and Step 3 is the only place the hypothesis $f(v)^2 = q(v)$ enters.
> - The proof does not show that $V \to \mathrm{Cl}(V, q)$ is injective or that $\mathrm{Cl}(V, q) \ne 0$; that needs a module, Theorem §CB.10.6.
> - Used next: Clifford modules (Theorem §CB.9.10), the grade automorphism and the reversal (Theorems §CB.10.1, §CB.10.4), the even subalgebra (Theorem §CB.10.10), complexification (Theorem §CB.11.3).

^pf-cb-9-7

*Uses:* [[§38 Tensor Products#^ladr-9-92|LADR Thm. 9.92]], [[§38 Tensor Products#^ladr-9-90|LADR Thm. 9.90]], [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-2|Def. §CB.9.2]], [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-3|Def. §CB.9.3]], [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-9-5|Theorem §CB.9.5]], [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-6|Def. §CB.9.6]], [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-5-9|Def. §CB.5.9]]

> [!theorem] Theorem §CB.9.8: The Anticommutator and the Embedding of V
> In $\mathrm{Cl}(V, q)$, $vw + wv = 2B(v, w)$ for all $v, w \in V$; in an orthogonal basis $e_ie_j = -e_je_i$ ($i \ne j$) and $e_i^2 = q(e_i)$. The map $V \to \mathrm{Cl}(V, q)$ is injective.
>
> *Source: Woit, §29.2, eq. (29.2) · Meinrenken, Clifford Algebras and Lie Groups, Prop. 2.2 (injectivity)*

^thm-cb-9-8

> [!proof]- Proof
> *Source: the anticommutator: Woit, Quantum Theory, Groups and Representations, §29.2, eq. (29.2) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · injectivity: E. Meinrenken, Clifford Algebras and Lie Groups, lecture notes (Toronto, Fall 2009), Ch. 2 §2.1, Prop. 2.2 (https://www.math.toronto.edu/mein/teaching/LieClifford/cl12.pdf), and J. Figueroa-O'Farrill, Spin Geometry, §1.4.4, Lemma 1.7 and the remark after it, both by letting $\mathrm{Cl}(V, q)$ act on $\Lambda V$; that module is constructed in the proof of Theorem §CB.10.6, which uses only Step 1 below.*
>
> **Step 1** (the anticommutator). Apply $uu = q(u)$ ([[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-6|Def. §CB.9.6]]) to $u = v + w$ and expand the product into its four terms:
>
> $$
> (v + w)(v + w) = vv + vw + wv + ww = q(v) + vw + wv + q(w), \qquad (v + w)(v + w) = q(v + w) .
> $$
>
> Hence $vw + wv = q(v + w) - q(v) - q(w) = 2B(v, w)$ ([[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-1|Def. §CB.9.1]]). For orthogonal $e_i$, $e_j$ with $i \ne j$ the right side is $0$, so $e_ie_j = -e_je_i$; for $i = j$ it reads $2e_ie_i = 2q(e_i)$.
>
> **Step 2** (injectivity). Choose an orthogonal basis $e_1, \dots, e_n$ of $V$ ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-12|LADR Thm. 9.12]] (a)⇒(d), over $\mathbb R$ or $\mathbb C$; it exists for every symmetric form, degenerate or not). By [[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-10-6|Theorem §CB.10.6]] the $2^n$ products $e_I$ are linearly independent in $\mathrm{Cl}(V, q)$; in particular the $n$ elements $e_{\{1\}} = e_1, \dots, e_{\{n\}} = e_n$ are. The map $V \to \mathrm{Cl}(V, q)$ is linear and sends $v = \sum_iv^ie_i$ to $\sum_iv^ie_i$ computed in $\mathrm{Cl}(V, q)$; if this is $0$, independence gives every $v^i = 0$, so $v = 0$.
>
> **What the proof shows.**
> - Step 1 is the bridge between the abstract relation $vv = q(v)$ and the form in which physics uses it, $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$: polarization turns the square of one vector into the anticommutator of two.
> - ⚑ By-product: injectivity is not automatic from the quotient construction (the ideal $I_q$ mixes degrees $0$ and $2$); it needs a nonzero module in which the vectors act independently, which is why the proof passes through Theorem §CB.10.6.

^pf-cb-9-8

*Uses:* [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-1|Def. §CB.9.1]], [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-6|Def. §CB.9.6]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-12|LADR Thm. 9.12]], [[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-10-6|Theorem §CB.10.6]]

## Clifford modules

> [!definition] Definition §CB.9.9: Clifford Module
> A **Clifford module** of $(V, q)$ is a representation of the algebra $\mathrm{Cl}(V, q)$ on a complex vector space $W$ ([[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-5-10|Def. §CB.5.10]]): an algebra homomorphism $\gamma : \mathrm{Cl}(V, q) \to \operatorname{End}_{\mathbb C}(W)$. Invariant subspaces, irreducibility, intertwiners and equivalence are those of Def. §CB.5.10.
>
> *Source (planned): written here*

^def-cb-9-9

> [!theorem] Theorem §CB.9.10: A Clifford Module Is a Set of Anticommuting Square Roots
> Clifford modules of $(V, q)$ on $W$ ([[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-9|Def. §CB.9.9]]) correspond bijectively, by restriction to $V$, to linear maps $\gamma : V \to \operatorname{End}(W)$ with $\gamma(v)^2 = q(v)\mathbb 1$ for all $v$; equivalently, for a basis $e_\mu$ of $V$ with $B(e_\mu, e_\nu) = g_{\mu\nu}$, to matrices $\gamma_\mu = \gamma(e_\mu)$ with $\gamma_\mu\gamma_\nu + \gamma_\nu\gamma_\mu = 2g_{\mu\nu}\mathbb 1$.
>
> *Source: Meinrenken, Clifford Algebras and Lie Groups, Prop. 2.3 · written here (from Theorem §CB.9.7 and Theorem §CB.9.8)*

^thm-cb-9-10

> [!proof]- Proof
> *Source: E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2 §2.2, Prop. 2.3 (stated there with the anticommutator form of the hypothesis, $f(v_1)f(v_2) + f(v_2)f(v_1) = 2B(v_1, v_2)$) · the specialization to $A = \operatorname{End}(W)$ written here.*
>
> **Step 1** (module → square roots). If $\gamma : \mathrm{Cl}(V, q) \to \operatorname{End}(W)$ is a Clifford module ([[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-9|Def. §CB.9.9]]), its restriction to $V$ is linear and $\gamma(v)^2 = \gamma(vv) = \gamma(q(v)1) = q(v)\mathbb 1$, since $\gamma$ is multiplicative and unital.
>
> **Step 2** (square roots → module). If $\gamma : V \to \operatorname{End}(W)$ is linear with $\gamma(v)^2 = q(v)\mathbb 1$, [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-9-7|Theorem §CB.9.7]] with $A = \operatorname{End}(W)$ (an associative algebra with unit $\mathbb 1$, [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-5-8|Def. §CB.5.8]]) gives a unique algebra homomorphism $\tilde\gamma : \mathrm{Cl}(V, q) \to \operatorname{End}(W)$ extending it.
>
> **Step 3** (the two operations are inverse). Restricting $\tilde\gamma$ to $V$ gives back $\gamma$ by construction. Conversely, a module $\gamma$ is an algebra homomorphism extending its own restriction, so by the uniqueness in Theorem §CB.9.7 it equals the extension built in Step 2 from that restriction.
>
> **Step 4** (matrix form). Let $e_\mu$ be a basis with $B(e_\mu, e_\nu) = g_{\mu\nu}$ and $\gamma_\mu = \gamma(e_\mu)$. If $\gamma(v)^2 = q(v)\mathbb 1$ for all $v$, apply it to $v = e_\mu + e_\nu$ and expand, as in Step 1 of [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-9-8|Theorem §CB.9.8]]:
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
> - Used in: Pauli's theorem in general form (Theorem §CB.11.8) and the Dirac maps of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9|Def. §C5a.1.9]].

^pf-cb-9-10

*Uses:* [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-9-7|Theorem §CB.9.7]], [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-9-8|Theorem §CB.9.8]], [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-9-9|Def. §CB.9.9]], [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-5-8|Def. §CB.5.8]]

The Dirac matrices and the Dirac maps, a Clifford module of $\mathrm{Cl}(1,3)$ on spinor space, defined in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]]; the Clifford algebra in physics language, in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]]:

![[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7]]

![[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9]]

![[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-2]]

> [!remark]- Connections
> - The universal property (Theorem §CB.9.7) is the whole reason Dirac matrices are unique up to change of basis: a Clifford module is a homomorphism out of one fixed algebra, and §CB.11 shows that algebra (complexified) is a matrix algebra.
> - **Used in**: Definitions §CB.9.6–Theorem §CB.9.10 — [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-2|Theorem §C5a.0.2]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-5|Theorem §C5a.1.5]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9|Def. §C5a.1.9]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-4|Def. §C5a.4.4]]
