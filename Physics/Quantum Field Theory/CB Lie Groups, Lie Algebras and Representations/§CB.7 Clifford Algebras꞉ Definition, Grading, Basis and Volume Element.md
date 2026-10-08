---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.7
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.8 Complex Clifford Algebras and Clifford Modules]] →

*Sources: E. Meinrenken, Clifford Algebras and Lie Groups, lecture notes, University of Toronto, Fall 2009, Ch. 1–2 (https://www.math.toronto.edu/mein/teaching/LieClifford/cl12.pdf; convention $vw + wv = 2B(v, w)$, as here) · J. Figueroa-O'Farrill, Spin Geometry, lecture notes, Edinburgh 2010, version of 18 May 2017, Lectures 1–3 (https://empg.maths.ed.ac.uk/Activities/Spin/SpinNotes.pdf, read via the Internet Archive copy of 27 Sep 2024; convention $x^2 = -Q(x)$) · P. Woit, Quantum Theory, Groups and Representations, Ch. 28–29 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf; convention $[\gamma_j, \gamma_k]_+ = 2\delta_{jk}$, as here) · Linear Algebra (LADR) §§11, 35–38 · the user's PHY 513 notes, Ch. 8 · Peskin & Schroeder, §3.2, §3.4 · the rest written here.*

What is the algebra that the Dirac matrices generate, defined without matrices? The spinor chapter meets it as the relation $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]) and as a ★ remark ([[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-2|§C5a.0, ★ Remark: The Clifford algebra is the algebra of square roots of p²]]). This section defines the Clifford algebra $\mathrm{Cl}(V, q)$ of a quadratic space as a quotient of the tensor algebra, states its universal property, and derives its structure: Clifford modules, the $\mathbb Z_2$-grading, the reversal, the basis $e_I$ and $\dim = 2^n$, the identification with $\Lambda V$ as a vector space, the volume element (the abstract $\gamma^5$), the even subalgebra, and the low-dimensional examples. Representations of algebras are [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-7|Def. §CB.3.7]]; exterior powers are [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-12|Def. §CB.4.12]]. The complex theory is [[§CB.8 Complex Clifford Algebras and Clifford Modules|§CB.8]]; the spin group, [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.9]].

<!-- MOVE row (CB-INVENTORY): ★ Remark rem-c5a-0-2 (definition and universal property) is embedded below; its definition and universal property are to be moved here when this section is written (batch 5; SPEC-CB groups the §C5a.0/§C5a.1 moves with batch 6 — settle then); the "what the relation induces" table stays in §C5a.0. -->

## Quadratic spaces, the tensor algebra and quotients

Quadratic forms and their bilinear forms, defined in LADR:

![[§35 Bilinear Forms and Quadratic Forms#^ladr-9-18]]

> [!definition] Definition §CB.7.1: Quadratic Space
> A **quadratic space** $(V, q)$ over $\mathbb K = \mathbb R$ or $\mathbb C$ is a finite-dimensional $\mathbb K$-vector space $V$ with a quadratic form $q$ ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-18|LADR Def. 9.18]]), $q(v) = B(v, v)$ for the symmetric bilinear form $B(v, w) = \frac12\bigl(q(v + w) - q(v) - q(w)\bigr)$. It is **nondegenerate** if $B(v, \cdot) = 0$ implies $v = 0$. A basis $e_1, \dots, e_n$ is **orthogonal** if $B(e_i, e_j) = 0$ for $i \ne j$, **orthonormal** if moreover $q(e_i) = \pm1$ (over $\mathbb C$: $q(e_i) = 1$). $\mathbb R^{r,s}$ denotes $\mathbb R^{r+s}$ with $q(x) = x_1^2 + \cdots + x_r^2 - x_{r+1}^2 - \cdots - x_{r+s}^2$; Minkowski space is $\mathbb R^{1,3}$ with $q(x) = g(x, x)$ ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]]).
>
> *Source (planned): LADR §35 (orthogonal bases: Thm. 9.12) · written here*

^def-cb-7-1

> [!definition] Definition §CB.7.2: Tensor Algebra
> The **tensor algebra** of a $\mathbb K$-vector space $V$ is $T(V) = \bigoplus_{k\ge0}V^{\otimes k}$ ($V^{\otimes0} = \mathbb K$, $V^{\otimes k}$ of [[§38 Tensor Products#^ladr-9-88|LADR Def. 9.88]]), an associative algebra ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-5|Def. §CB.3.5]]) with the product $(v_1\otimes\cdots\otimes v_k)(w_1\otimes\cdots\otimes w_l) = v_1\otimes\cdots\otimes v_k\otimes w_1\otimes\cdots\otimes w_l$ extended bilinearly, and unit $1 \in \mathbb K$.
>
> *Source (planned): written here*

^def-cb-7-2

> [!definition] Definition §CB.7.3: Two-Sided Ideal
> A **two-sided ideal** of an associative algebra $A$ is a subspace $I$ with $aI \subset I$ and $Ia \subset I$ for all $a \in A$. The ideal **generated** by a subset $S$ is the smallest one containing $S$: the span of all $asb$ with $a, b \in A$, $s \in S$.
>
> *Source (planned): written here*

^def-cb-7-3

> [!definition] Definition §CB.7.4: Quotient Algebra
> For a two-sided ideal $I$ of $A$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-3|Def. §CB.7.3]]), the **quotient algebra** $A/I$ is the quotient space ([[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR Def. 3.99]]) with the product $(a + I)(b + I) = ab + I$.
>
> *Source (planned): written here*

^def-cb-7-4

> [!theorem] Theorem §CB.7.5: The Quotient Is an Algebra
> The product of [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-4|Def. §CB.7.4]] is well defined, $A/I$ is an associative algebra with unit $1 + I$, and $a \mapsto a + I$ is a surjective algebra homomorphism ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-6|Def. §CB.3.6]]) with kernel $I$. An algebra homomorphism $f : A \to B$ with $f(I) = 0$ factors uniquely through $A/I$.
>
> *Source (planned): written here*

^thm-cb-7-5

> [!proof]- Proof
> If $a' = a + i$, $b' = b + j$ with $i, j \in I$, then $a'b' = ab + (aj + ib + ij)$, and each of $aj$, $ib$, $ij$ lies in $I$ because $I$ is a two-sided ideal; so $a'b' + I = ab + I$. Associativity, bilinearity and the unit pass from $A$ to the cosets term by term. The map $a \mapsto a + I$ is linear, multiplicative by the definition of the product, onto, and sends $a$ to $0 + I$ iff $a \in I$. If $f(I) = 0$, put $\bar f(a + I) = f(a)$: well defined since $f(a + i) = f(a)$, and an algebra homomorphism because $f$ is; it is the only map with $\bar f(a + I) = f(a)$.

^pf-cb-7-5

## The Clifford algebra and its universal property

> [!definition] Definition §CB.7.6: Clifford Algebra
> The **Clifford algebra** of a quadratic space $(V, q)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-1|Def. §CB.7.1]]) is
>
> $$
> \mathrm{Cl}(V, q) = T(V)/I_q, \qquad I_q = \text{the two-sided ideal generated by } \{v\otimes v - q(v)1 : v \in V\}
> $$
>
> ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-2|Def. §CB.7.2]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-4|Def. §CB.7.4]]). The image of $v \in V$ is written $v$, and the product in $\mathrm{Cl}(V, q)$ by juxtaposition, so $vv = q(v)$. $\mathrm{Cl}(r, s) = \mathrm{Cl}(\mathbb R^{r,s})$; the Clifford algebra of Minkowski space is $\mathrm{Cl}(1,3)$.
>
> *Source: E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2, Def. 2.1 (same convention) · J. Figueroa-O'Farrill, Spin Geometry, §1.2.2 (ideal generated by $x\otimes x + Q(x)$: the opposite sign) · Woit, §29.2*

^def-cb-7-6

> [!caution] Caution: Two sign conventions for the Clifford relation
> These notes use the physics convention $vv = +q(v)$, which with $q = g$ gives $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]; Woit, §29.2, eq. (29.2), and Meinrenken, Def. 2.1, use the same sign). Much of the mathematical literature (e.g. Figueroa-O'Farrill, Spin Geometry, eq. (2); Lawson–Michelsohn) writes $vv = -q(v)$; its $\mathrm{Cl}(V, q)$ is this section's $\mathrm{Cl}(V, -q)$, and labels such as $\mathrm{Cl}_{r,s}$ or $\mathrm{Cl}(r, s)$ then refer to different algebras. Over $\mathbb C$ the two conventions give isomorphic algebras ($v \mapsto iv$). Here $\mathrm{Cl}(r, s)$ always has $r$ generators squaring to $+1$ and $s$ to $-1$: in $\mathrm{Cl}(1,3)$, $(\gamma^0)^2 = +1$, $(\gamma^i)^2 = -1$.
>
> *Source: SPEC-CB decision 6 · Woit, §29.2 (which notes the other convention) · Meinrenken, Clifford Algebras and Lie Groups, Def. 2.1 · Figueroa-O'Farrill, Spin Geometry, eq. (2) and §1.3.2 (his $C\ell(s,t)$, $s$ generators squaring to $-1$, is this section's $\mathrm{Cl}(t,s)$)*

^cau-cb-7-1

> [!theorem] Theorem §CB.7.7: Universal Property of the Clifford Algebra
> Let $A$ be an associative algebra over $\mathbb K$ ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-5|Def. §CB.3.5]]) and $f : V \to A$ a linear map with $f(v)^2 = q(v)1_A$ for all $v \in V$. Then there is a unique algebra homomorphism $\tilde f : \mathrm{Cl}(V, q) \to A$ ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-6|Def. §CB.3.6]]) with $\tilde f(v) = f(v)$ for $v \in V$.
>
> *Source: Meinrenken, Clifford Algebras and Lie Groups, Prop. 2.3 · Figueroa-O'Farrill, Spin Geometry, Def. 1.1, §1.2.2 · the Minkowski case stated in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-2|§C5a.0, ★ Remark]]*

^thm-cb-7-7

> [!proof]- Proof
> *Source: E. Meinrenken, Clifford Algebras and Lie Groups, lecture notes (Toronto, Fall 2009), Ch. 2 §2.2, Prop. 2.3 and its proof (https://www.math.toronto.edu/mein/teaching/LieClifford/cl12.pdf; same sign convention as here) · J. Figueroa-O'Farrill, Spin Geometry, lecture notes (Edinburgh 2010, version of 18 May 2017), §1.2.2, eqs. (12)–(15) (https://empg.maths.ed.ac.uk/Activities/Spin/SpinNotes.pdf, read via the Internet Archive copy of 27 Sep 2024; his relation is $x^2 = -Q(x)$). Both leave Steps 1–2 to the reader; they are written out here.*
>
> **Step 1** (extension to each tensor power). For $k \ge 1$ the map $\Gamma_k(v_1, \dots, v_k) = f(v_1)f(v_2)\cdots f(v_k)$ from $V\times\cdots\times V$ to $A$ is $k$-linear, because $f$ is linear and the product of $A$ is bilinear. By [[§38 Tensor Products#^ladr-9-92|LADR Thm. 9.92]] there is a unique linear map $F_k : V^{\otimes k} \to A$ with
>
> $$
> F_k(v_1\otimes\cdots\otimes v_k) = f(v_1)\cdots f(v_k) .
> $$
>
> Put $F_0(\lambda) = \lambda 1_A$ on $V^{\otimes 0} = \mathbb K$, and let $F : T(V) \to A$ be $F_k$ on the summand $V^{\otimes k}$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-2|Def. §CB.7.2]]), extended linearly.
>
> **Step 2** ($F$ is an algebra homomorphism). For pure tensors $a = v_1\otimes\cdots\otimes v_k$ and $b = w_1\otimes\cdots\otimes w_l$,
>
> $$
> F(ab) = F(v_1\otimes\cdots\otimes v_k\otimes w_1\otimes\cdots\otimes w_l) = f(v_1)\cdots f(v_k)\,f(w_1)\cdots f(w_l) = F(a)F(b),
> $$
>
> and if $k = 0$ or $l = 0$ one factor is a scalar $\lambda$, with $F(\lambda b) = \lambda F(b) = F(\lambda)F(b)$. Both sides of $F(ab) = F(a)F(b)$ are bilinear in $(a, b)$, and the pure tensors span each $V^{\otimes k}$ ([[§38 Tensor Products#^ladr-9-90|LADR Thm. 9.90]]: products of basis vectors are a basis), so $F(ab) = F(a)F(b)$ for all $a, b \in T(V)$; and $F(1) = 1_A$.
>
> **Step 3** ($F$ kills the ideal). On a generator of $I_q$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-6|Def. §CB.7.6]]):
>
> $$
> F\bigl(v\otimes v - q(v)1\bigr) = f(v)f(v) - q(v)1_A = 0
> $$
>
> by the hypothesis $f(v)^2 = q(v)1_A$. Every element of $I_q$ is a sum of terms $a\,s\,b$ with $a, b \in T(V)$ and $s$ a generator ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-3|Def. §CB.7.3]]), and $F(asb) = F(a)F(s)F(b) = F(a)\cdot0\cdot F(b) = 0$ by Step 2. So $F(I_q) = 0$.
>
> **Step 4** (existence). By [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-5|Theorem §CB.7.5]], $F$ factors through $\mathrm{Cl}(V, q) = T(V)/I_q$: there is an algebra homomorphism $\tilde f$ with $\tilde f(x + I_q) = F(x)$. For $v \in V$, $\tilde f(v) = F_1(v) = f(v)$.
>
> **Step 5** (uniqueness). $\mathrm{Cl}(V, q)$ is spanned by the images of pure tensors, i.e. by $1$ and the products $v_1v_2\cdots v_k$ (Step 2's spanning statement, pushed through the quotient map). An algebra homomorphism $g$ with $g(v) = f(v)$ satisfies $g(1) = 1_A$ and $g(v_1\cdots v_k) = g(v_1)\cdots g(v_k) = f(v_1)\cdots f(v_k) = \tilde f(v_1\cdots v_k)$; two linear maps that agree on a spanning set are equal, so $g = \tilde f$.
>
> **What the proof shows.**
> - ⚑ By-product: Steps 1–2 are the universal property of the tensor algebra itself (every linear map $V \to A$ extends uniquely to an algebra homomorphism $T(V) \to A$, Figueroa-O'Farrill eq. (12)); the Clifford algebra adds exactly one relation, and Step 3 is the only place the hypothesis $f(v)^2 = q(v)$ enters.
> - The proof does not show that $V \to \mathrm{Cl}(V, q)$ is injective or that $\mathrm{Cl}(V, q) \ne 0$; that needs a module, Theorem §CB.7.16.
> - Used next: Clifford modules (Theorem §CB.7.10), the grade automorphism and the reversal (Theorems §CB.7.11, §CB.7.14), the even subalgebra (Theorem §CB.7.20), complexification (Theorem §CB.8.3).

^pf-cb-7-7

*Uses:* [[§38 Tensor Products#^ladr-9-92|LADR Thm. 9.92]], [[§38 Tensor Products#^ladr-9-90|LADR Thm. 9.90]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-2|Def. §CB.7.2]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-3|Def. §CB.7.3]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-5|Theorem §CB.7.5]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-6|Def. §CB.7.6]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-6|Def. §CB.3.6]]

> [!theorem] Theorem §CB.7.8: The Anticommutator and the Embedding of V
> In $\mathrm{Cl}(V, q)$, $vw + wv = 2B(v, w)$ for all $v, w \in V$; in an orthogonal basis $e_ie_j = -e_je_i$ ($i \ne j$) and $e_i^2 = q(e_i)$. The map $V \to \mathrm{Cl}(V, q)$ is injective.
>
> *Source: Woit, §29.2, eq. (29.2) · Meinrenken, Clifford Algebras and Lie Groups, Prop. 2.2 (injectivity)*

^thm-cb-7-8

> [!proof]- Proof
> *Source: the anticommutator: Woit, Quantum Theory, Groups and Representations, §29.2, eq. (29.2) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · injectivity: E. Meinrenken, Clifford Algebras and Lie Groups, lecture notes (Toronto, Fall 2009), Ch. 2 §2.1, Prop. 2.2 (https://www.math.toronto.edu/mein/teaching/LieClifford/cl12.pdf), and J. Figueroa-O'Farrill, Spin Geometry, §1.4.4, Lemma 1.7 and the remark after it, both by letting $\mathrm{Cl}(V, q)$ act on $\Lambda V$; that module is constructed in the proof of Theorem §CB.7.16, which uses only Step 1 below.*
>
> **Step 1** (the anticommutator). Apply $uu = q(u)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-6|Def. §CB.7.6]]) to $u = v + w$ and expand the product into its four terms:
>
> $$
> (v + w)(v + w) = vv + vw + wv + ww = q(v) + vw + wv + q(w), \qquad (v + w)(v + w) = q(v + w) .
> $$
>
> Hence $vw + wv = q(v + w) - q(v) - q(w) = 2B(v, w)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-1|Def. §CB.7.1]]). For orthogonal $e_i$, $e_j$ with $i \ne j$ the right side is $0$, so $e_ie_j = -e_je_i$; for $i = j$ it reads $2e_ie_i = 2q(e_i)$.
>
> **Step 2** (injectivity). Choose an orthogonal basis $e_1, \dots, e_n$ of $V$ ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-12|LADR Thm. 9.12]] (a)⇒(d), over $\mathbb R$ or $\mathbb C$; it exists for every symmetric form, degenerate or not). By [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-16|Theorem §CB.7.16]] the $2^n$ products $e_I$ are linearly independent in $\mathrm{Cl}(V, q)$; in particular the $n$ elements $e_{\{1\}} = e_1, \dots, e_{\{n\}} = e_n$ are. The map $V \to \mathrm{Cl}(V, q)$ is linear and sends $v = \sum_iv^ie_i$ to $\sum_iv^ie_i$ computed in $\mathrm{Cl}(V, q)$; if this is $0$, independence gives every $v^i = 0$, so $v = 0$.
>
> **What the proof shows.**
> - Step 1 is the bridge between the abstract relation $vv = q(v)$ and the form in which physics uses it, $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$: polarization turns the square of one vector into the anticommutator of two.
> - ⚑ By-product: injectivity is not automatic from the quotient construction (the ideal $I_q$ mixes degrees $0$ and $2$); it needs a nonzero module in which the vectors act independently, which is why the proof passes through Theorem §CB.7.16.

^pf-cb-7-8

*Uses:* [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-1|Def. §CB.7.1]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-6|Def. §CB.7.6]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-12|LADR Thm. 9.12]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-16|Theorem §CB.7.16]]

## Clifford modules

> [!definition] Definition §CB.7.9: Clifford Module
> A **Clifford module** of $(V, q)$ is a representation of the algebra $\mathrm{Cl}(V, q)$ on a complex vector space $W$ ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-7|Def. §CB.3.7]]): an algebra homomorphism $\gamma : \mathrm{Cl}(V, q) \to \operatorname{End}_{\mathbb C}(W)$. Invariant subspaces, irreducibility, intertwiners and equivalence are those of Def. §CB.3.7.
>
> *Source (planned): written here*

^def-cb-7-9

> [!theorem] Theorem §CB.7.10: A Clifford Module Is a Set of Anticommuting Square Roots
> Clifford modules of $(V, q)$ on $W$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-9|Def. §CB.7.9]]) correspond bijectively, by restriction to $V$, to linear maps $\gamma : V \to \operatorname{End}(W)$ with $\gamma(v)^2 = q(v)\mathbb 1$ for all $v$; equivalently, for a basis $e_\mu$ of $V$ with $B(e_\mu, e_\nu) = g_{\mu\nu}$, to matrices $\gamma_\mu = \gamma(e_\mu)$ with $\gamma_\mu\gamma_\nu + \gamma_\nu\gamma_\mu = 2g_{\mu\nu}\mathbb 1$.
>
> *Source: Meinrenken, Clifford Algebras and Lie Groups, Prop. 2.3 · written here (from Theorem §CB.7.7 and Theorem §CB.7.8)*

^thm-cb-7-10

> [!proof]- Proof
> *Source: E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2 §2.2, Prop. 2.3 (stated there with the anticommutator form of the hypothesis, $f(v_1)f(v_2) + f(v_2)f(v_1) = 2B(v_1, v_2)$) · the specialization to $A = \operatorname{End}(W)$ written here.*
>
> **Step 1** (module → square roots). If $\gamma : \mathrm{Cl}(V, q) \to \operatorname{End}(W)$ is a Clifford module ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-9|Def. §CB.7.9]]), its restriction to $V$ is linear and $\gamma(v)^2 = \gamma(vv) = \gamma(q(v)1) = q(v)\mathbb 1$, since $\gamma$ is multiplicative and unital.
>
> **Step 2** (square roots → module). If $\gamma : V \to \operatorname{End}(W)$ is linear with $\gamma(v)^2 = q(v)\mathbb 1$, [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]] with $A = \operatorname{End}(W)$ (an associative algebra with unit $\mathbb 1$, [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-5|Def. §CB.3.5]]) gives a unique algebra homomorphism $\tilde\gamma : \mathrm{Cl}(V, q) \to \operatorname{End}(W)$ extending it.
>
> **Step 3** (the two operations are inverse). Restricting $\tilde\gamma$ to $V$ gives back $\gamma$ by construction. Conversely, a module $\gamma$ is an algebra homomorphism extending its own restriction, so by the uniqueness in Theorem §CB.7.7 it equals the extension built in Step 2 from that restriction.
>
> **Step 4** (matrix form). Let $e_\mu$ be a basis with $B(e_\mu, e_\nu) = g_{\mu\nu}$ and $\gamma_\mu = \gamma(e_\mu)$. If $\gamma(v)^2 = q(v)\mathbb 1$ for all $v$, apply it to $v = e_\mu + e_\nu$ and expand, as in Step 1 of [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-8|Theorem §CB.7.8]]:
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
> - Used in: Pauli's theorem in general form (Theorem §CB.8.8) and the Dirac maps of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9|Def. §C5a.1.9]].

^pf-cb-7-10

*Uses:* [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-8|Theorem §CB.7.8]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-9|Def. §CB.7.9]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-5|Def. §CB.3.5]]

The Dirac matrices and the Dirac maps, a Clifford module of $\mathrm{Cl}(1,3)$ on spinor space, defined in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]]; the Clifford algebra in physics language, in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]]:

![[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7]]

![[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9]]

![[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-2]]

## Grading and involutions

> [!theorem] Theorem §CB.7.11: The Grade Automorphism
> There is a unique algebra automorphism $\alpha$ of $\mathrm{Cl}(V, q)$ with $\alpha(v) = -v$ for $v \in V$, and $\alpha^2 = \mathbb 1$.
>
> *Source: Figueroa-O'Farrill, Spin Geometry, §1.4.2 · Meinrenken, Clifford Algebras and Lie Groups, §2.2 (the parity automorphism)*

^thm-cb-7-11

> [!proof]- Proof
> *Source: J. Figueroa-O'Farrill, Spin Geometry, §1.4.2 (the automorphism $C\ell(f)$ induced by $f(x) = -x$, with $C\ell(f)\circ C\ell(f) = 1$ by functoriality) · E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2 §2.2 (the parity automorphism $\Pi$).*
>
> **Step 1** (existence). The linear map $f(v) = -v$ from $V$ into $\mathrm{Cl}(V, q)$ satisfies $f(v)^2 = (-v)(-v) = vv = q(v)$. By [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]] there is a unique algebra homomorphism $\alpha : \mathrm{Cl}(V, q) \to \mathrm{Cl}(V, q)$ with $\alpha(v) = -v$.
>
> **Step 2** ($\alpha^2 = \mathbb 1$). $\alpha\circ\alpha$ is an algebra homomorphism with $\alpha(\alpha(v)) = \alpha(-v) = v$. The identity map is also an algebra homomorphism with $v \mapsto v$, and $v \mapsto v$ satisfies the hypothesis of Theorem §CB.7.7; by the uniqueness there, $\alpha\circ\alpha = \mathbb 1$.
>
> **Step 3** (automorphism). By Step 2, $\alpha$ is bijective with inverse $\alpha$, so it is an algebra automorphism. On a product of $k$ vectors, $\alpha(v_1\cdots v_k) = (-v_1)\cdots(-v_k) = (-1)^kv_1\cdots v_k$.
>
> **What the proof shows.**
> - The only input is that $v \mapsto -v$ preserves $q$; the same argument gives an automorphism of $\mathrm{Cl}(V, q)$ for every $R \in O(V, q)$, used in Theorem §CB.7.17 (Figueroa-O'Farrill, §1.4.2: "the orthogonal group acts on the Clifford algebra via automorphisms").

^pf-cb-7-11

*Uses:* [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]]

> [!definition] Definition §CB.7.12: Even and Odd Parts
> The **even part** $\mathrm{Cl}^0(V, q)$ and the **odd part** $\mathrm{Cl}^1(V, q)$ are the $+1$ and $-1$ eigenspaces of $\alpha$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-11|Theorem §CB.7.11]]): the spans of products of an even, resp. odd, number of vectors.
>
> *Source (planned): written here*

^def-cb-7-12

> [!theorem] Theorem §CB.7.13: The ℤ₂-Grading
> $\mathrm{Cl}(V, q) = \mathrm{Cl}^0 \oplus \mathrm{Cl}^1$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-12|Def. §CB.7.12]]), and $\mathrm{Cl}^i\mathrm{Cl}^j \subset \mathrm{Cl}^{i + j \bmod 2}$. In particular $\mathrm{Cl}^0$ is a subalgebra, and products of two vectors, such as $\gamma^\mu\gamma^\nu$ and $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$, are even.
>
> *Source: Figueroa-O'Farrill, Spin Geometry, §1.4.2, eqs. (28)–(29) · Meinrenken, Clifford Algebras and Lie Groups, §2.1*

^thm-cb-7-13

> [!proof]- Proof
> *Source: J. Figueroa-O'Farrill, Spin Geometry, §1.4.2, eqs. (28)–(29) · E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2 §2.1 ("the two summands are spanned by products $v_1\cdots v_k$ with $k$ even, respectively odd").*
>
> **Step 1** (direct sum). For $x \in \mathrm{Cl}(V, q)$ put $x_0 = \frac12(x + \alpha x)$ and $x_1 = \frac12(x - \alpha x)$. Then $x = x_0 + x_1$, and by $\alpha^2 = \mathbb 1$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-11|Theorem §CB.7.11]]) $\alpha x_0 = \frac12(\alpha x + x) = x_0$ and $\alpha x_1 = \frac12(\alpha x - x) = -x_1$. If $y \in \mathrm{Cl}^0\cap\mathrm{Cl}^1$, then $y = \alpha y = -y$, so $y = 0$. Hence $\mathrm{Cl} = \mathrm{Cl}^0\oplus\mathrm{Cl}^1$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-12|Def. §CB.7.12]]).
>
> **Step 2** (the eigenspaces are the even and odd spans). Let $E$ and $O$ be the spans of products of an even, resp. odd, number of vectors. By Theorem §CB.7.11, Step 3, $\alpha = +1$ on $E$ and $-1$ on $O$, so $E \subset \mathrm{Cl}^0$, $O \subset \mathrm{Cl}^1$. $\mathrm{Cl}$ is spanned by $1$ and products of vectors (Step 5 of the proof of [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]]), so $\mathrm{Cl} = E + O$. If $x \in \mathrm{Cl}^0$, write $x = e + o$ with $e \in E$, $o \in O$; then $x - e = o \in \mathrm{Cl}^0\cap\mathrm{Cl}^1 = 0$, so $x = e \in E$. Likewise $\mathrm{Cl}^1 = O$.
>
> **Step 3** (products). If $\alpha x = (-1)^ix$ and $\alpha y = (-1)^jy$, then, $\alpha$ being multiplicative, $\alpha(xy) = \alpha(x)\alpha(y) = (-1)^{i+j}xy$: $\mathrm{Cl}^i\mathrm{Cl}^j \subset \mathrm{Cl}^{i+j \bmod 2}$. With $i = j = 0$, and $1 \in \mathrm{Cl}^0$, $\mathrm{Cl}^0$ is a subalgebra. A product of two vectors lies in $\mathrm{Cl}^0$ by Step 2, and so do their linear combinations $\gamma^\mu\gamma^\nu$ and $\frac i4[\gamma^\mu, \gamma^\nu]$ (in the complexified algebra, where $\alpha$ is extended complex-linearly).
>
> **What the proof shows.**
> - The grading exists although $I_q$ is not homogeneous for the $\mathbb Z$-grading of $T(V)$: its generators $v\otimes v - q(v)1$ mix degrees $2$ and $0$, both even (Figueroa-O'Farrill, §1.2.2). Only the parity survives the quotient.
> - Used in: the even subalgebra (Theorems §CB.7.16, §CB.7.20), the spin group (Def. §CB.9.6) and the Lorentz generators ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]).

^pf-cb-7-13

*Uses:* [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-11|Theorem §CB.7.11]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-12|Def. §CB.7.12]]

> [!theorem] Theorem §CB.7.14: The Reversal
> There is a unique linear map $t : \mathrm{Cl}(V, q) \to \mathrm{Cl}(V, q)$, the **reversal** (transpose), with $t(1) = 1$, $t(v) = v$ for $v \in V$ and $t(xy) = t(y)t(x)$; so $t(v_1v_2\cdots v_k) = v_k\cdots v_2v_1$. It satisfies $t^2 = \mathbb 1$ and $t\alpha = \alpha t$.
>
> *Source: Meinrenken, Clifford Algebras and Lie Groups, §2.7 (transposition) · Figueroa-O'Farrill, Spin Geometry, §3.4 (the check involution)*

^thm-cb-7-14

> [!proof]- Proof
> *Source: E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2 §2.7 (transposition: the anti-automorphism $(v_1\otimes\cdots\otimes v_k)^\top = v_k\otimes\cdots\otimes v_1$ of $T(V)$ preserves $I(V; B)$ and descends) · J. Figueroa-O'Farrill, Spin Geometry, §3.4 (the "check involution"). The route through the opposite algebra, which uses only Theorem §CB.7.7, is written here.*
>
> **Step 1** (the opposite algebra). Let $\mathrm{Cl}^{\mathrm{op}}$ be the vector space $\mathrm{Cl}(V, q)$ with the product $x\cdot_{\mathrm{op}}y = yx$. It is associative, $(x\cdot_{\mathrm{op}}y)\cdot_{\mathrm{op}}z = z(yx) = (zy)x = x\cdot_{\mathrm{op}}(y\cdot_{\mathrm{op}}z)$, bilinear, with the same unit $1$ ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-5|Def. §CB.3.5]]).
>
> **Step 2** (existence). The inclusion $f : V \to \mathrm{Cl}^{\mathrm{op}}$, $f(v) = v$, satisfies $f(v)\cdot_{\mathrm{op}}f(v) = vv = q(v)1$. By [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]] there is a unique algebra homomorphism $t : \mathrm{Cl}(V, q) \to \mathrm{Cl}^{\mathrm{op}}$ with $t(v) = v$. Read in $\mathrm{Cl}(V, q)$: $t$ is linear, $t(1) = 1$ and $t(xy) = t(x)\cdot_{\mathrm{op}}t(y) = t(y)t(x)$. Then by induction on $k$, $t(v_1\cdots v_k) = t(v_2\cdots v_k)\,t(v_1) = v_k\cdots v_2\,v_1$.
>
> **Step 3** (uniqueness). Let $t'$ be linear with $t'(v) = v$, $t'(xy) = t'(y)t'(x)$ and $t'(1) = 1$ (the last condition is automatic as soon as some $v$ has $q(v) \ne 0$, since then $1 = vv/q(v)$ and $t'(1) = t'(v)t'(v)/q(v) = 1$). By induction on $k$, $t'(v_1\cdots v_k) = t'(v_2\cdots v_k)\,t'(v_1) = v_k\cdots v_1 = t(v_1\cdots v_k)$. The products of vectors and $1$ span $\mathrm{Cl}$ (Step 5 of the proof of Theorem §CB.7.7), so $t' = t$.
>
> **Step 4** ($t^2 = \mathbb 1$ and $t\alpha = \alpha t$). $t\circ t$ is linear, multiplicative ($t(t(xy)) = t(t(y)t(x)) = t(t(x))\,t(t(y))$) and fixes $V$; so it is an algebra homomorphism $\mathrm{Cl} \to \mathrm{Cl}$ extending $v \mapsto v$, and by uniqueness in Theorem §CB.7.7 it is $\mathbb 1$. Both $t\alpha$ and $\alpha t$ are linear, reverse products ($t\alpha(xy) = t(\alpha(x)\alpha(y)) = t\alpha(y)\,t\alpha(x)$, and likewise for $\alpha t$, using that $\alpha$ is multiplicative, [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-11|Theorem §CB.7.11]]) and send $v \mapsto -v$; on a product of $k$ vectors both give $(-1)^kv_k\cdots v_1$, so they agree on a spanning set and are equal.
>
> **What the proof shows.**
> - An anti-automorphism is just a homomorphism into the opposite algebra, so the universal property produces it with no computation in $T(V)$.
> - Used next: Clifford conjugation (Def. §CB.7.15), the spinor norm $N(x) = x\,t(x)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-8|Def. §CB.9.8]]) and the inverse of an element of $\mathrm{Spin}$, which is $\pm t(x)$.

^pf-cb-7-14

*Uses:* [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-11|Theorem §CB.7.11]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-5|Def. §CB.3.5]]

> [!definition] Definition §CB.7.15: Clifford Conjugation
> The **Clifford conjugation** is $x \mapsto \bar x = \alpha(t(x))$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-11|Theorem §CB.7.11]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-14|Theorem §CB.7.14]]); $\overline{v_1\cdots v_k} = (-1)^kv_k\cdots v_1$.
>
> *Source (planned): written here*

^def-cb-7-15

## Basis, dimension and the exterior algebra

> [!theorem] Theorem §CB.7.16: Basis and Dimension
> Let $e_1, \dots, e_n$ be an orthogonal basis of $(V, q)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-1|Def. §CB.7.1]]). For $I = \{i_1 < \cdots < i_k\} \subset \{1, \dots, n\}$ put $e_I = e_{i_1}\cdots e_{i_k}$, $e_\varnothing = 1$. The $2^n$ elements $e_I$ form a basis of $\mathrm{Cl}(V, q)$; so $\dim\mathrm{Cl}(V, q) = 2^n$, and $\mathrm{Cl}^0$, $\mathrm{Cl}^1$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-12|Def. §CB.7.12]]) have the bases $e_I$ with $|I|$ even, resp. odd, each of dimension $2^{n-1}$ ($n \ge 1$).
>
> *Source: Woit, §28.1 (spanning) · Meinrenken, Clifford Algebras and Lie Groups, Props. 2.2, 2.6 · Figueroa-O'Farrill, Spin Geometry, §1.4.4, Lemma 1.7 · the $4\times4$ case: [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]]*

^thm-cb-7-16

> [!proof]- Proof
> *Source: spanning: P. Woit, Quantum Theory, Groups and Representations, §28.1 (the basis of $\mathrm{Cliff}(n, \mathbb C)$, by reordering with the anticommutation relations) · independence: E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2 §2.1, Prop. 2.2, and §2.5, Prop. 2.6 and its proof (the action $f(v) = \epsilon(v) + \iota(B^\flat(v))$ of $\mathrm{Cl}(V; B)$ on $\Lambda V$; in an orthogonal basis $\sigma(e_{i_1}\cdots e_{i_k}) = e_{i_1}\wedge\cdots\wedge e_{i_k}$) · J. Figueroa-O'Farrill, Spin Geometry, §1.4.4, Lemma 1.7 (the same module, his sign). The module is written out here in the orthogonal basis, so that only sign bookkeeping is needed. For $4\times4$ Dirac matrices the course proves independence by traces instead ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]]).*
>
> **Step 1** (spanning). $\mathrm{Cl}(V, q)$ is spanned by $1$ and products $v_1\cdots v_k$ (Step 5 of the proof of [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]]). Expanding each $v_a = \sum_iv_a^ie_i$, it is spanned by the words $e_{j_1}e_{j_2}\cdots e_{j_k}$ in the basis vectors. In a word, two adjacent distinct letters may be swapped at the cost of a sign, $e_ie_j = -e_je_i$, and two adjacent equal letters may be replaced by the scalar $e_ie_i = q(e_i)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-8|Theorem §CB.7.8]], Step 1). Sorting the letters by adjacent swaps and then cancelling equal neighbours turns every word into $\pm\bigl(\prod q(e_i)\bigr)e_I$ for some $I$ (or $0$ if some cancelled $q(e_i)$ vanishes). So the $2^n$ elements $e_I$ span $\mathrm{Cl}(V, q)$.
>
> **Step 2** (a $2^n$-dimensional space). Let $W$ be a vector space with basis $f_I$, one vector for each subset $I \subset \{1, \dots, n\}$ ($f_I$ plays the role of $e_{i_1}\wedge\cdots\wedge e_{i_k} \in \Lambda V$). For $i \in \{1, \dots, n\}$ and a subset $I$ let $m_i(I) = \#\{j \in I : j < i\}$, the number of letters of $I$ to the left of the place where $i$ belongs. Define $c_i \in \operatorname{End}(W)$ by
>
> $$
> c_i\,f_I = \begin{cases}(-1)^{m_i(I)}\,f_{I\cup\{i\}} & i \notin I,\\[2pt] (-1)^{m_i(I)}\,q(e_i)\,f_{I\setminus\{i\}} & i \in I.\end{cases}
> $$
>
> (In Meinrenken's language the first line is $\epsilon(e_i)$, wedging $e_i$ in from the left past $m_i(I)$ factors, and the second is the contraction $\iota(B^\flat e_i)$, which removes the factor $e_i$ from position $m_i(I) + 1$ with the sign $(-1)^{m_i(I)}$ and the factor $B(e_i, e_i) = q(e_i)$.)
>
> **Step 3** ($c_i^2 = q(e_i)$). If $i \notin I$: $c_if_I = (-1)^{m}f_{I\cup\{i\}}$ with $m = m_i(I)$; now $i \in I\cup\{i\}$ and $m_i(I\cup\{i\}) = m$ (the letters below $i$ are unchanged), so $c_i^2f_I = (-1)^m(-1)^mq(e_i)f_I = q(e_i)f_I$. If $i \in I$: $c_if_I = (-1)^mq(e_i)f_{I\setminus\{i\}}$, then $c_i$ adds $i$ back with the same sign $(-1)^m$, so again $c_i^2f_I = q(e_i)f_I$.
>
> **Step 4** ($c_ic_j = -c_jc_i$ for $i < j$). Both products send $f_I$ to a multiple of $f_{I\triangle\{i, j\}}$ (symmetric difference), with the same factors $q(e_i)$, $q(e_j)$ (a factor $q(e_i)$ appears iff $i \in I$, whichever operator acts first). Only the signs can differ. Since $j > i$, adding or removing $j$ does not change $m_i$: $m_i(I\triangle\{j\}) = m_i(I)$. Since $i < j$, adding or removing $i$ changes $m_j$ by exactly one: $m_j(I\triangle\{i\}) = m_j(I) \pm 1$. Hence
>
> $$
> c_ic_jf_I:\ (-1)^{m_j(I)}(-1)^{m_i(I)}, \qquad c_jc_if_I:\ (-1)^{m_i(I)}(-1)^{m_j(I)\pm1},
> $$
>
> opposite signs: $c_ic_j + c_jc_i = 0$.
>
> **Step 5** (a Clifford module). Define $\gamma(v) = \sum_iv^ic_i$ for $v = \sum_iv^ie_i$. Expanding the square into all $n^2$ terms and grouping the pairs $\{i, j\}$,
>
> $$
> \gamma(v)^2 = \sum_i(v^i)^2c_i^2 + \sum_{i<j}v^iv^j(c_ic_j + c_jc_i) = \sum_i(v^i)^2q(e_i)\,\mathbb 1 = q(v)\,\mathbb 1,
> $$
>
> by Steps 3–4 and because $q(v) = \sum_{i,j}v^iv^jB(e_i, e_j) = \sum_i(v^i)^2q(e_i)$ in an orthogonal basis. By [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]], $\gamma$ extends to an algebra homomorphism $\gamma : \mathrm{Cl}(V, q) \to \operatorname{End}(W)$.
>
> **Step 6** ($e_I$ acts on $f_\varnothing$ as $f_I$). For $I = \{i_1 < \cdots < i_k\}$, $\gamma(e_I)f_\varnothing = c_{i_1}c_{i_2}\cdots c_{i_k}f_\varnothing$. The operators act from the right: $c_{i_k}f_\varnothing = f_{\{i_k\}}$ ($m = 0$); then $c_{i_{k-1}}$ adds $i_{k-1}$, smaller than every letter present, so again $m = 0$ and the sign is $+$; continuing, $\gamma(e_I)f_\varnothing = f_I$.
>
> **Step 7** (independence, dimension). If $\sum_Ix_Ie_I = 0$ in $\mathrm{Cl}(V, q)$, apply $\gamma$ and evaluate on $f_\varnothing$: $\sum_Ix_If_I = 0$, so every $x_I = 0$. With Step 1, the $e_I$ are a basis and $\dim\mathrm{Cl}(V, q) = 2^n$.
>
> **Step 8** (even and odd parts). $e_I$ is a product of $|I|$ vectors, so $\alpha(e_I) = (-1)^{|I|}e_I$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-11|Theorem §CB.7.11]]). Writing $x = \sum x_Ie_I$, $\alpha x = x$ iff $x_I = 0$ for all odd $|I|$, and $\alpha x = -x$ iff $x_I = 0$ for all even $|I|$: the $e_I$ with $|I|$ even (odd) are a basis of $\mathrm{Cl}^0$ ($\mathrm{Cl}^1$), [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-12|Def. §CB.7.12]]. Their numbers are $\sum_{k\ \mathrm{even}}\binom nk$ and $\sum_{k\ \mathrm{odd}}\binom nk$; these add to $(1 + 1)^n = 2^n$ and differ by $(1 - 1)^n = 0$ for $n \ge 1$, so each is $2^{n-1}$.
>
> **What the proof shows.**
> - ⚑ By-product: $W$ with $f_I \leftrightarrow e_{i_1}\wedge\cdots\wedge e_{i_k}$ is a $2^n$-dimensional module of $\mathrm{Cl}(V, q)$ on $\Lambda V$ (Meinrenken's $f_{\mathrm{Cl}}$), and $x \mapsto \gamma(x)f_\varnothing$ is a linear isomorphism $\mathrm{Cl}(V, q) \to \Lambda V$ (the symbol map); its inverse is the map of Theorem §CB.7.17.
> - The module is not irreducible when $q$ is nondegenerate and $n \ge 2$ (it is $\mathrm{Cl}$ acting on itself, of dimension $2^n > 2^{\lfloor n/2\rfloor}$); its only job is to separate the $e_I$. The irreducible modules come in §CB.8.
> - Nothing used nondegeneracy: for $q = 0$ the same proof shows that $\Lambda V$ itself has the basis $e_I$.

^pf-cb-7-16

*Uses:* [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-8|Theorem §CB.7.8]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-11|Theorem §CB.7.11]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-12|Def. §CB.7.12]]

The sixteen products of Dirac matrices, the $n = 4$ case in matrices, proved in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]]:

![[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6]]

> [!theorem] Theorem §CB.7.17: The Clifford Algebra Is the Exterior Algebra as a Vector Space
> The linear map $\Lambda V \to \mathrm{Cl}(V, q)$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-12|Def. §CB.4.12]]) given on $\Lambda^kV$ by
>
> $$
> v_1\wedge\cdots\wedge v_k \mapsto \frac1{k!}\sum_\pi\operatorname{sgn}(\pi)\,v_{\pi(1)}\cdots v_{\pi(k)}
> $$
>
> is an isomorphism of vector spaces. For an orthogonal basis it maps $e_{i_1}\wedge\cdots\wedge e_{i_k}$ to $e_I$, so $\Lambda^kV$ goes onto the span of the $e_I$ with $|I| = k$; it commutes with the action of $O(V, q)$ on both sides (on $\mathrm{Cl}(V, q)$ by the automorphisms extending $v \mapsto Rv$, Theorem §CB.7.7).
>
> *Source: Meinrenken, Clifford Algebras and Lie Groups, Props. 2.6–2.7 · Figueroa-O'Farrill, Spin Geometry, §1.4.4, eq. (40) · the antisymmetrized products: [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-8|Def. §C5a.1.8]]*

^thm-cb-7-17

> [!proof]- Proof
> *Source: E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2 §2.5, Props. 2.6–2.7 and their proofs (the quantization map $q : \Lambda(V) \to \mathrm{Cl}(V; B)$ is graded antisymmetrization; checked on an orthogonal basis) · J. Figueroa-O'Farrill, Spin Geometry, §1.3.1 and §1.4.4, eq. (40). Equivariance under $O(V, q)$ written here.*
>
> **Step 1** (the map is well defined). Let $\pi_k : V^{\otimes k} \to \mathrm{Cl}(V, q)$ be the restriction of the quotient map $T(V) \to \mathrm{Cl}(V, q)$, $\pi_k(v_1\otimes\cdots\otimes v_k) = v_1\cdots v_k$; it is linear. $\Lambda^kV$ is a subspace of $V^{\otimes k}$ and $v_1\wedge\cdots\wedge v_k = \frac1{k!}\sum_\pi\operatorname{sgn}(\pi)\,v_{\pi(1)}\otimes\cdots\otimes v_{\pi(k)}$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-12|Def. §CB.4.12]]). So the map of the theorem is $Q = \pi_k|_{\Lambda^kV}$, linear, and
>
> $$
> Q(v_1\wedge\cdots\wedge v_k) = \frac1{k!}\sum_\pi\operatorname{sgn}(\pi)\,v_{\pi(1)}\cdots v_{\pi(k)} .
> $$
>
> **Step 2** (spanning set of $\Lambda^kV$). An antisymmetric $t \in \Lambda^kV$ satisfies $t = \frac1{k!}\sum_\pi\operatorname{sgn}(\pi)\,\pi t$, since each term is $\operatorname{sgn}(\pi)^2t = t$. Expand $t = \sum t^{j_1\cdots j_k}e_{j_1}\otimes\cdots\otimes e_{j_k}$ in the basis of [[§38 Tensor Products#^ladr-9-90|LADR Thm. 9.90]]; then $t = \sum t^{j_1\cdots j_k}\,e_{j_1}\wedge\cdots\wedge e_{j_k}$. A wedge with a repeated index is $0$ (the transposition of the two equal slots fixes the tensor and multiplies it by $-1$), and reordering distinct indices into increasing order multiplies the wedge by the sign of the reordering. So the $e_{i_1}\wedge\cdots\wedge e_{i_k}$ with $i_1 < \cdots < i_k$ span $\Lambda^kV$.
>
> **Step 3** (orthogonal basis vectors go to $e_I$). Let $i_1 < \cdots < i_k$ be distinct. In $\mathrm{Cl}(V, q)$ the $e_{i_a}$ pairwise anticommute ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-8|Theorem §CB.7.8]]), so sorting the word $e_{i_{\pi(1)}}\cdots e_{i_{\pi(k)}}$ by adjacent swaps gives $\operatorname{sgn}(\pi)\,e_I$ (each swap is one transposition and one factor $-1$). Hence
>
> $$
> Q(e_{i_1}\wedge\cdots\wedge e_{i_k}) = \frac1{k!}\sum_\pi\operatorname{sgn}(\pi)\operatorname{sgn}(\pi)\,e_I = \frac{k!}{k!}\,e_I = e_I .
> $$
>
> **Step 4** (isomorphism). Let $Q : \Lambda V = \bigoplus_k\Lambda^kV \to \mathrm{Cl}(V, q)$ be the sum of the $Q$'s. By Step 3 it maps the spanning set of Step 2 onto the $2^n$ elements $e_I$, which are linearly independent ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-16|Theorem §CB.7.16]]). A linear relation among the increasing wedges would map to one among the $e_I$, so the wedges are independent too: they are a basis of $\Lambda V$, mapped bijectively onto the basis $e_I$ of $\mathrm{Cl}(V, q)$. So $Q$ is an isomorphism, and $\Lambda^kV$ goes onto $\operatorname{span}\{e_I : |I| = k\}$.
>
> **Step 5** ($O(V, q)$-equivariance). For $R \in O(V, q)$, $q(Rv) = q(v)$, so $v \mapsto Rv$ satisfies the hypothesis of [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]] and extends to an algebra homomorphism $\mathrm{Cl}(R)$ with $\mathrm{Cl}(R)(v_1\cdots v_k) = Rv_1\cdots Rv_k$. On $\Lambda^kV$, $R$ acts by $R^{\otimes k}$, which sends $v_1\wedge\cdots\wedge v_k$ to $Rv_1\wedge\cdots\wedge Rv_k$ (apply $R^{\otimes k}$ term by term in the defining sum). Then
>
> $$
> Q(Rv_1\wedge\cdots\wedge Rv_k) = \frac1{k!}\sum_\pi\operatorname{sgn}(\pi)\,Rv_{\pi(1)}\cdots Rv_{\pi(k)} = \mathrm{Cl}(R)\,Q(v_1\wedge\cdots\wedge v_k),
> $$
>
> and since the wedges span (Step 2, for any basis), $Q\circ R^{\otimes\bullet} = \mathrm{Cl}(R)\circ Q$.
>
> **What the proof shows.**
> - $Q$ is a vector-space isomorphism, not an algebra map: $Q(e_1\wedge e_1) = 0$ but $e_1e_1 = q(e_1)$. The Clifford product is the wedge product plus contractions (Meinrenken, Prop. 2.6: $\sigma(v_1v_2) = v_1\wedge v_2 + B(v_1, v_2)$).
> - ⚑ By-product: because $Q$ commutes with the orthogonal group, the decomposition $\mathrm{Cl} \cong \bigoplus_k\Lambda^kV$ is a decomposition into $O(V, q)$-representations; for $\mathbb R^{1,3}$ it is the classification of the sixteen bilinears as scalar, vector, tensor, axial vector and pseudoscalar (§CB.12).

^pf-cb-7-17

*Uses:* [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-12|Def. §CB.4.12]], [[§38 Tensor Products#^ladr-9-90|LADR Thm. 9.90]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-8|Theorem §CB.7.8]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-16|Theorem §CB.7.16]]

## The volume element

> [!definition] Definition §CB.7.18: Volume Element
> For an orthonormal basis $e_1, \dots, e_n$ of a nondegenerate real quadratic space ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-1|Def. §CB.7.1]]), the **volume element** is $\omega = e_1e_2\cdots e_n \in \mathrm{Cl}(V, q)$.
>
> *Source: Figueroa-O'Farrill, Spin Geometry, §3.3 (before Lemma 3.9) · Meinrenken, Clifford Algebras and Lie Groups, §2.8 (the chirality element)*

^def-cb-7-18

> [!theorem] Theorem §CB.7.19: Properties of the Volume Element
> Let $(V, q) = \mathbb R^{r,s}$, $n = r + s$, and $\omega$ as in [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-18|Def. §CB.7.18]].
> 1. Another orthonormal basis gives $\pm\omega$, the sign being the determinant of the change of basis: $\omega$ depends only on an orientation.
> 2. $\omega^2 = (-1)^{n(n-1)/2}(-1)^s$.
> 3. $\omega v = (-1)^{n-1}v\omega$ for $v \in V$: $\omega$ commutes with $\mathrm{Cl}^0$ always, and anticommutes with $V$ for $n$ even.
> 4. The centre of $\mathrm{Cl}(V, q)$ is $\mathbb R1$ for $n$ even and $\mathbb R1 \oplus \mathbb R\omega$ for $n$ odd; the centre of $\mathrm{Cl}^0$ is $\mathbb R1\oplus\mathbb R\omega$ for $n$ even and $\mathbb R1$ for $n$ odd; in every case the elements of $\mathrm{Cl}^0$ commuting with all of $\mathrm{Cl}(V, q)$ are $\mathbb R1$.
>
> For $\mathrm{Cl}(1,3)$: $\omega = e_0e_1e_2e_3$, $\omega^2 = -1$, and $i\omega$ squares to $1$ (the complex normalization, [[§CB.8 Complex Clifford Algebras and Clifford Modules#^def-cb-8-4|Def. §CB.8.4]]). Its image in a Dirac module depends on the module ([[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵#^cau-cb-12-1|Caution: Two Dirac modules, and the sign of γ⁵]]): the module $e_\mu \mapsto \gamma^\mu$ (upper index; $q(e_0) = 1$, $q(e_i) = -1$) sends $i\omega$ to $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$, while the course's module $e_\mu \mapsto \gamma_\mu$ sends it to $i\gamma_0\gamma_1\gamma_2\gamma_3 = -\gamma^5$, so there $\gamma^5$ is the image of $-i\omega$, the volume element of the opposite orientation (part 1); in both cases $(\gamma^5)^2 = 1$.
>
> *Source: Meinrenken, Clifford Algebras and Lie Groups, §2.8 · Figueroa-O'Farrill, Spin Geometry, Lemma 3.9 and §3.2 · Peskin & Schroeder, §3.4 · part 1 written here*

^thm-cb-7-19

> [!proof]- Proof
> *Source: E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2 §2.8 (chirality element: $\Gamma^2 = (-1)^{n(n-1)/2}\prod_iB(e_i, e_i)$ and $\Gamma v = (-1)^{n-1}v\Gamma$, same sign convention) · J. Figueroa-O'Farrill, Spin Geometry, §3.3, Lemma 3.9 (the same in his convention, $\omega^2 = (-1)^{s + d(d-1)/2}$ with $s$ the number of generators squaring to $-1$) · centre: the basis argument of Figueroa-O'Farrill, §3.2 (proof of Prop. 3.3), organized here as a sign table. Part 1 written here.*
>
> Throughout, $e_1, \dots, e_n$ is an orthonormal basis, $q_i = q(e_i) = \pm1$, $\prod_iq_i = (-1)^s$, and $e_I$ the basis of [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-16|Theorem §CB.7.16]].
>
> **Step 1** (part 1: change of orthonormal basis). Let $f_j = \sum_iA_{ij}e_i$ be another orthonormal basis. The $f_j$ pairwise anticommute ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-8|Theorem §CB.7.8]]), so, exactly as in Step 3 of the proof of [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-17|Theorem §CB.7.17]], $f_1\cdots f_n = Q(f_1\wedge\cdots\wedge f_n)$. Expanding the wedge multilinearly,
>
> $$
> f_1\wedge\cdots\wedge f_n = \sum_{i_1, \dots, i_n}A_{i_11}\cdots A_{i_nn}\,e_{i_1}\wedge\cdots\wedge e_{i_n} = \sum_\sigma\operatorname{sgn}(\sigma)A_{\sigma(1)1}\cdots A_{\sigma(n)n}\,e_1\wedge\cdots\wedge e_n = \det(A)\,e_1\wedge\cdots\wedge e_n :
> $$
>
> terms with a repeated index vanish, a term with distinct indices $i_a = \sigma(a)$ is $\operatorname{sgn}(\sigma)e_1\wedge\cdots\wedge e_n$, and the sum is the formula for the determinant ([[§37 Determinants#^ladr-9-46|LADR Thm. 9.46]], with [[§37 Determinants#^ladr-9-56|LADR 9.56]] for the transpose). Applying $Q$: $f_1\cdots f_n = \det(A)\,\omega$. The Gram matrices $G = (B(e_i, e_j))$ and $G' = (B(f_i, f_j))$ are diagonal with entries $\pm1$ and $G' = A^{\mathsf T}GA$ ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-7|LADR Thm. 9.7]]); taking determinants ([[§37 Determinants#^ladr-9-49|LADR 9.49]]), $\det(A)^2 = \det G'/\det G \in \{\pm1\}$, and a square of a real number is positive, so $\det(A)^2 = 1$ and $\det A = \pm1$.
>
> **Step 2** (part 2: $\omega^2$). Write $\omega^2 = (e_1\cdots e_n)(e_1\cdots e_n)$. Reverse the second block: $e_1e_2\cdots e_n = (-1)^{n(n-1)/2}e_ne_{n-1}\cdots e_1$, because reversing $n$ pairwise anticommuting letters takes $(n-1) + (n-2) + \cdots + 1 = n(n-1)/2$ adjacent swaps. Then collapse from the middle:
>
> $$
> \omega^2 = (-1)^{n(n-1)/2}\,e_1\cdots e_{n-1}(e_ne_n)e_{n-1}\cdots e_1 = (-1)^{n(n-1)/2}q_n\,e_1\cdots e_{n-1}e_{n-1}\cdots e_1 = \cdots = (-1)^{n(n-1)/2}\,q_1q_2\cdots q_n = (-1)^{n(n-1)/2}(-1)^s .
> $$
>
> **Step 3** (part 3: $\omega$ and vectors). Move $e_j$ from the right of $\omega = e_1\cdots e_n$ to the left: it passes $e_n, \dots, e_1$; it anticommutes with the $n - 1$ letters $e_i$, $i \ne j$, and commutes with $e_j$. So $\omega e_j = (-1)^{n-1}e_j\omega$, and by linearity $\omega v = (-1)^{n-1}v\omega$ for all $v \in V$. For a product of two vectors, $\omega(vw) = (-1)^{2(n-1)}(vw)\omega = (vw)\omega$; such products and $1$ span $\mathrm{Cl}^0$ (each even $e_I$ is a product of pairs $e_{i_1}e_{i_2}$, $e_{i_3}e_{i_4}$, …, by Step 8 of the proof of Theorem §CB.7.16), so $\omega$ commutes with $\mathrm{Cl}^0$. For $n$ even, $(-1)^{n-1} = -1$.
>
> **Step 4** (part 4: a sign table). For a basis element $e_I$ and a letter $e_j$, moving $e_j$ through $e_I$ as in Step 3 gives $e_je_I = \varepsilon_j(I)\,e_Ie_j$ with
>
> $$
> \varepsilon_j(I) = (-1)^{|I|}\ (j \notin I), \qquad \varepsilon_j(I) = (-1)^{|I|-1}\ (j \in I) .
> $$
>
> Since $e_j$ is invertible ($e_j^{-1} = q_je_j$), conjugation $x \mapsto e_jxe_j^{-1}$ sends $e_I \mapsto \varepsilon_j(I)e_I$. Write $x = \sum_Ix_Ie_I$. Then $e_jx = xe_j$ iff $\sum_Ix_I(\varepsilon_j(I) - 1)e_I = 0$ iff $x_I = 0$ whenever $\varepsilon_j(I) = -1$ (independence of the $e_I$).
>
> **Step 5** (part 4: the centre of $\mathrm{Cl}$). $x$ commutes with all of $\mathrm{Cl}$ iff it commutes with the generators $e_1, \dots, e_n$, iff $x_I = 0$ unless $\varepsilon_j(I) = +1$ for every $j$. If $|I|$ is even and $I \ne \varnothing$, pick $j \in I$: $\varepsilon_j(I) = -1$. If $|I|$ is odd and some $j \notin I$: $\varepsilon_j(I) = -1$. So only $I = \varnothing$ ($\varepsilon \equiv +1$) and possibly $I = \{1, \dots, n\}$ survive; the latter has $\varepsilon_j = (-1)^{n-1}$ for all $j$, which is $+1$ iff $n$ is odd (for $n$ even, $|I| = n$ is even and nonempty, already excluded). Centre: $\mathbb R1$ ($n$ even), $\mathbb R1\oplus\mathbb R\omega$ ($n$ odd).
>
> **Step 6** (part 4: the centre of $\mathrm{Cl}^0$). $\mathrm{Cl}^0$ is spanned by the $e_I$ with $|I|$ even and generated by $1$ and the $e_ie_j$, $i < j$ (Step 3). An even $x$ commutes with $e_ie_j$ iff $x_I = 0$ unless $\varepsilon_i(I)\varepsilon_j(I) = +1$. For $|I|$ even, $\varepsilon_j(I) = +1$ if $j \notin I$ and $-1$ if $j \in I$, so the product is $+1$ iff $i$, $j$ are both in $I$ or both outside. This holds for all pairs iff $I = \varnothing$ or $I = \{1, \dots, n\}$ (when $n \ge 2$; for $n = 1$, $\mathrm{Cl}^0 = \mathbb R$), and $\{1, \dots, n\}$ is even only for $n$ even. Centre of $\mathrm{Cl}^0$: $\mathbb R1\oplus\mathbb R\omega$ ($n$ even), $\mathbb R1$ ($n$ odd). Finally, an even element commuting with all of $\mathrm{Cl}$ lies in (centre of $\mathrm{Cl}$) $\cap\,\mathrm{Cl}^0$, which is $\mathbb R1$ in both cases, since for $n$ odd $\omega$ is odd.
>
> **Step 7** (the Minkowski case). For $\mathbb R^{1,3}$ with $q(e_0) = 1$, $q(e_i) = -1$: $n = 4$, $s = 3$, $\omega^2 = (-1)^6(-1)^3 = -1$, so $(i\omega)^2 = i^2\omega^2 = 1$. In the module $e_\mu \mapsto \gamma^\mu$, $i\omega \mapsto i\gamma^0\gamma^1\gamma^2\gamma^3 = \gamma^5$. In the course's module $e_\mu \mapsto \gamma_\mu$ ($\gamma_0 = \gamma^0$, $\gamma_i = -\gamma^i$), $i\omega \mapsto i\gamma_0\gamma_1\gamma_2\gamma_3 = i(-1)^3\gamma^0\gamma^1\gamma^2\gamma^3 = -\gamma^5$; by Step 1 this is the volume element of the reversed orientation ([[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵#^cau-cb-12-1|Caution: Two Dirac modules, and the sign of γ⁵]]).
>
> **What the proof shows.**
> - The sign of $\omega^2$ depends only on $n(n-1)/2 + s$: in $\mathrm{Cl}(1,3)$ ($s = 3$) and in $\mathrm{Cl}(3,1)$ ($s = 1$) alike $\omega^2 = -1$, which is why $\gamma^5$ carries a factor $i$ in either metric convention.
> - ⚑ By-product: Step 4's sign table also shows that an odd element anticommuting with every vector is $0$ (for odd $|I|$, $\varepsilon_j(I) = +1$ for $j \in I$); this is used for the kernel of $\mathrm{Pin} \to O(V)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-7|Theorem §CB.9.7]]).
> - Used in: chirality ([[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]]), the complex volume element ([[§CB.8 Complex Clifford Algebras and Clifford Modules#^def-cb-8-4|Def. §CB.8.4]]), the kernel of $\rho$ (Theorem §CB.9.11).

^pf-cb-7-19

*Uses:* [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-8|Theorem §CB.7.8]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-16|Theorem §CB.7.16]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-17|Theorem §CB.7.17]], [[§37 Determinants#^ladr-9-46|LADR Thm. 9.46]], [[§37 Determinants#^ladr-9-49|LADR Thm. 9.49]], [[§37 Determinants#^ladr-9-56|LADR Thm. 9.56]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-7|LADR Thm. 9.7]]

γ⁵ and its properties, the volume element of the Dirac module, in [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] and [[§C5a.11 Gamma-Matrix Technology|§C5a.11]]:

![[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1]]

![[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1]]

![[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-5]]

## The even subalgebra and small examples

> [!theorem] Theorem §CB.7.20: The Even Subalgebra Is a Clifford Algebra of One Dimension Less
> Let $(V, q)$ be nondegenerate real, $e_0 \in V$ with $q(e_0) = \epsilon \in \{\pm1\}$, and $V' = e_0^\perp$ with $q'(v') = -\epsilon\,q(v')$. Then $v' \mapsto v'e_0$ extends to an algebra isomorphism $\mathrm{Cl}(V', q') \cong \mathrm{Cl}^0(V, q)$. In particular $\mathrm{Cl}^0(1,3) \cong \mathrm{Cl}(3,0)$ (with $e_0$ timelike, $f_i = e_ie_0$, $f_i^2 = +1$) and $\mathrm{Cl}^0(3,0) \cong \mathrm{Cl}(0,2)$.
>
> *Source: Figueroa-O'Farrill, Spin Geometry, Prop. 2.8 · Meinrenken, Clifford Algebras and Lie Groups, eq. (19)*

^thm-cb-7-20

> [!proof]- Proof
> *Source: J. Figueroa-O'Farrill, Spin Geometry, §2.3.1, Prop. 2.8 and its proof ($\phi(x) = xe_{s+1}$, Clifford, surjective, dimension count; his $C\ell(s,t) \cong C\ell(s+1,t)^0$ is this statement for $\epsilon = -1$ after his sign change) · E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2 §2.4, eq. (19) (the complex version $e_i \mapsto \sqrt{-1}\,e_ie_{n+1}$).*
>
> **Step 1** ($V'$ is a nondegenerate quadratic space). $V = \mathbb Re_0\oplus V'$, since $v = \frac{B(v, e_0)}{\epsilon}e_0 + \bigl(v - \frac{B(v, e_0)}{\epsilon}e_0\bigr)$ with the second term orthogonal to $e_0$, and $\mathbb Re_0\cap V' = 0$ because $B(e_0, e_0) = \epsilon \ne 0$. If $v' \in V'$ were orthogonal to all of $V'$, it would be orthogonal to $e_0$ too, hence to $V$, so $v' = 0$. Thus $(V', q')$ is nondegenerate of dimension $n - 1$, and $B'(v', w') = -\epsilon B(v', w')$.
>
> **Step 2** (the map is Clifford). Put $f(v') = v'e_0 \in \mathrm{Cl}^0(V, q)$ (even: a product of two vectors, [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-13|Theorem §CB.7.13]]). Since $v' \perp e_0$, $v'e_0 = -e_0v'$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-8|Theorem §CB.7.8]]), and
>
> $$
> f(v')^2 = v'e_0v'e_0 = -v'v'e_0e_0 = -q(v')\,\epsilon = q'(v') .
> $$
>
> By [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]], $f$ extends to an algebra homomorphism $\Phi : \mathrm{Cl}(V', q') \to \mathrm{Cl}^0(V, q)$ (the target is a subalgebra by Theorem §CB.7.13).
>
> **Step 3** (surjective). Take an orthonormal basis $e_1, \dots, e_{n-1}$ of $V'$ (Def. §CB.7.1 and Step 1); with $e_0$ it is an orthonormal basis of $V$. The image of $\Phi$ is a subalgebra containing $e_ie_0$ for $i \ge 1$, hence also $(e_ie_0)(e_je_0) = -e_ie_je_0e_0 = -\epsilon\,e_ie_j$, i.e. every $e_ie_j$ with $i, j \ge 1$, and $e_0e_i = -e_ie_0$. So it contains every product of two basis vectors, hence every even basis element $e_I = (e_{i_1}e_{i_2})(e_{i_3}e_{i_4})\cdots$, which span $\mathrm{Cl}^0(V, q)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-16|Theorem §CB.7.16]], Step 8).
>
> **Step 4** (bijective). $\dim\mathrm{Cl}(V', q') = 2^{n-1} = \dim\mathrm{Cl}^0(V, q)$ (Theorem §CB.7.16), so the surjection $\Phi$ is injective as well.
>
> **Step 5** (the two examples). $\mathbb R^{1,3}$ with $e_0$ timelike: $\epsilon = 1$, $V' = \operatorname{span}(e_1, e_2, e_3)$ with $q(e_i) = -1$, so $q'(e_i) = +1$: $\mathrm{Cl}(V', q') = \mathrm{Cl}(3,0)$, and $f_i = e_ie_0$ has $f_i^2 = -e_ie_ie_0e_0 = -(-1)(1) = 1$. $\mathbb R^{3,0}$ with $e_0 = e_3$: $\epsilon = 1$, $V' = \operatorname{span}(e_1, e_2)$ with $q' = -q$, so $\mathrm{Cl}(V', q') = \mathrm{Cl}(0,2)$.
>
> **What the proof shows.**
> - The even part forgets one dimension and flips the sign of the form on the rest (for timelike $e_0$): this is the algebraic reason the boost generators $\gamma^i\gamma^0$ square to $+1$ like Pauli matrices, and why $\mathrm{Spin}(1,3)$ is built from $\mathrm{Cl}(3,0)\otimes\mathbb C$ (§CB.11).
> - Used in: Theorem §CB.7.21 ($\mathrm{Cl}^0(3,0) \cong \mathbb H$) and the complexified even subalgebra ([[§CB.8 Complex Clifford Algebras and Clifford Modules#^thm-cb-8-9|Theorem §CB.8.9]]).

^pf-cb-7-20

*Uses:* [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-1|Def. §CB.7.1]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-8|Theorem §CB.7.8]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-13|Theorem §CB.7.13]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-16|Theorem §CB.7.16]]

> [!theorem] Theorem §CB.7.21: Clifford Algebras in Low Dimensions
> As real algebras:
>
> | $\mathrm{Cl}(r, s)$ | $\mathrm{Cl}(0,1)$ | $\mathrm{Cl}(1,0)$ | $\mathrm{Cl}(0,2)$ | $\mathrm{Cl}(2,0)$ | $\mathrm{Cl}(1,1)$ | $\mathrm{Cl}(3,0)$ | $\mathrm{Cl}(1,2)$ |
> |---|---|---|---|---|---|---|---|
> | $\cong$ | $\mathbb C$ | $\mathbb R\oplus\mathbb R$ | $\mathbb H$ | $M_2(\mathbb R)$ | $M_2(\mathbb R)$ | $M_2(\mathbb C)$ | $M_2(\mathbb C)$ |
>
> ($\mathbb H$ the quaternions, [[§41 The Unit Quaternions and SU(2)#^def-41-1|591 Def. §41.1]].) In particular $\mathrm{Cl}^0(3,0) \cong \mathbb H$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-20|Theorem §CB.7.20]]), and $\mathrm{Cl}(3,0)$ is realized by the Pauli matrices (§CB.10).
>
> *Source: Woit, §28.2 · Meinrenken, Clifford Algebras and Lie Groups, Prop. 2.4 · Figueroa-O'Farrill, Spin Geometry, §1.3.2*

^thm-cb-7-21

> [!proof]- Proof
> *Source: P. Woit, Quantum Theory, Groups and Representations, §28.2 ($\mathrm{Cliff}(0,1) = \mathbb C$, $\mathrm{Cliff}(0,2) = \mathbb H$, $\mathrm{Cliff}(1,1) = M(2, \mathbb R)$, $\mathrm{Cliff}(3,0) = M(2, \mathbb C)$ with the Pauli matrices; same sign convention) · E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2 §2.3, Prop. 2.4 and its proof (the method: explicit generators plus a dimension count; same convention) · J. Figueroa-O'Farrill, Spin Geometry, §1.3.2 and Thm. 2.7 (whose $C\ell(s,t)$ is this section's $\mathrm{Cl}(t,s)$). The generators for $\mathrm{Cl}(2,0)$ and $\mathrm{Cl}(1,2)$ are chosen here.*
>
> **Step 1** (method). Let $A$ be a real algebra with $\dim A = 2^{r+s}$ and $a_1, \dots, a_{r+s} \in A$ pairwise anticommuting, $a_j^2 = +1$ ($j \le r$), $a_j^2 = -1$ ($j > r$). Then $f(\sum x^je_j) = \sum x^ja_j$ satisfies $f(x)^2 = \sum_j(x^j)^2a_j^2 = q(x)$ (cross terms cancel in pairs, as in Step 5 of the proof of [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-16|Theorem §CB.7.16]]), so [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]] gives a homomorphism $\Phi : \mathrm{Cl}(r, s) \to A$. If the products of the $a_j$ (with $1$) span $A$, $\Phi$ is onto, and since $\dim\mathrm{Cl}(r, s) = 2^{r+s}$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-16|Theorem §CB.7.16]]) it is an isomorphism. The Pauli products used below are $\sigma^j\sigma^k = \delta^{jk}\mathbb 1 + i\varepsilon^{jkl}\sigma^l$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]).
>
> **Step 2** (the generators and spanning products).
>
> | $\mathrm{Cl}(r, s)$ | $A$, $\dim_{\mathbb R}$ | $a_j$ | squares | products spanning $A$ |
> |---|---|---|---|---|
> | $\mathrm{Cl}(0,1)$ | $\mathbb C$, 2 | $i$ | $-1$ | $1, i$ |
> | $\mathrm{Cl}(1,0)$ | $\mathbb R\oplus\mathbb R$, 2 | $(1, -1)$ | $+1$ | $(1,1), (1,-1)$ |
> | $\mathrm{Cl}(0,2)$ | $\mathbb H$, 4 | $i, j$ | $-1, -1$ | $1, i, j, ij = k$ |
> | $\mathrm{Cl}(2,0)$ | $M_2(\mathbb R)$, 4 | $\sigma^1, \sigma^3$ | $+1, +1$ | $\mathbb 1, \sigma^1, \sigma^3, \sigma^1\sigma^3 = -i\sigma^2$ |
> | $\mathrm{Cl}(1,1)$ | $M_2(\mathbb R)$, 4 | $\sigma^1, i\sigma^2$ | $+1, -1$ | $\mathbb 1, \sigma^1, i\sigma^2, \sigma^1(i\sigma^2) = -\sigma^3$ |
> | $\mathrm{Cl}(3,0)$ | $M_2(\mathbb C)$, 8 | $\sigma^1, \sigma^2, \sigma^3$ | $+1$ (3×) | $\mathbb 1, \sigma^k, \sigma^j\sigma^k = i\varepsilon^{jkl}\sigma^l, \sigma^1\sigma^2\sigma^3 = i\mathbb 1$ |
> | $\mathrm{Cl}(1,2)$ | $M_2(\mathbb C)$, 8 | $\sigma^3, i\sigma^1, i\sigma^2$ | $+1, -1, -1$ | $\mathbb 1, \sigma^3, i\sigma^1, i\sigma^2, \sigma^3(i\sigma^1) = -\sigma^2, \sigma^3(i\sigma^2) = \sigma^1, (i\sigma^1)(i\sigma^2) = -i\sigma^3, \sigma^3(i\sigma^1)(i\sigma^2) = -i\mathbb 1$ |
>
> **Step 3** (checks). Anticommutation: $(1,-1)$ is a single generator; $ij + ji = k - k = 0$ ([[§41 The Unit Quaternions and SU(2)#^def-41-1|591 Def. §41.1]]); distinct Pauli matrices anticommute, so $\sigma^1\sigma^3 + \sigma^3\sigma^1 = 0$, $\sigma^1(i\sigma^2) + (i\sigma^2)\sigma^1 = i\{\sigma^1, \sigma^2\} = 0$, $\sigma^3(i\sigma^a) + (i\sigma^a)\sigma^3 = 0$ and $(i\sigma^1)(i\sigma^2) + (i\sigma^2)(i\sigma^1) = -\{\sigma^1, \sigma^2\} = 0$. Squares: $(i\sigma^a)^2 = -(\sigma^a)^2 = -\mathbb 1$. Spanning: the real $2\times2$ matrices $\mathbb 1, \sigma^1, \sigma^3, -i\sigma^2 = \begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}$ are a basis of $M_2(\mathbb R)$ (any $\begin{pmatrix}a & b\\ c & d\end{pmatrix}$ is $\frac{a+d}2\mathbb 1 + \frac{b+c}2\sigma^1 + \frac{a-d}2\sigma^3 + \frac{c-b}2(-i\sigma^2)$); and $\mathbb 1, \sigma^1, \sigma^2, \sigma^3$ are a complex basis of $M_2(\mathbb C)$ (QM Theorem §B6.1.4, 4), so $\mathbb 1, \sigma^k, i\mathbb 1, i\sigma^k$ are a real basis, and both rows for $M_2(\mathbb C)$ produce all eight up to sign. Step 1 now gives each isomorphism.
>
> **Step 4** ($\mathrm{Cl}^0(3,0) \cong \mathbb H$). By [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-20|Theorem §CB.7.20]], $\mathrm{Cl}^0(3,0) \cong \mathrm{Cl}(0,2)$, which is $\mathbb H$ by the third row.
>
> **What the proof shows.**
> - Signature matters over $\mathbb R$: $\mathrm{Cl}(1,0) \not\cong \mathrm{Cl}(0,1)$ (one has zero divisors, $(1,0)(0,1) = 0$, the other is a field), and $\mathrm{Cl}(2,0) \not\cong \mathrm{Cl}(0,2)$ ($M_2(\mathbb R)$ has zero divisors, $\mathbb H$ has none); after complexification the difference disappears (Theorem §CB.8.3).
> - The two-component square roots of [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^ex-c5a-0-1|Example §C5a.0.1]] are modules of $\mathrm{Cl}(1,1)$ and $\mathrm{Cl}(1,2)$ by these rows.

^pf-cb-7-21

*Uses:* [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-16|Theorem §CB.7.16]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-20|Theorem §CB.7.20]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§41 The Unit Quaternions and SU(2)#^def-41-1|591 Def. §41.1]]

The two-component square roots in $1 + 1$ and $2 + 1$ dimensions, which are modules of $\mathrm{Cl}(1,1)$ and $\mathrm{Cl}(1,2)$, in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]]:

![[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^ex-c5a-0-1]]

> [!remark]- ★ Remark: The real classification (not used in the course)
> Every real Clifford algebra $\mathrm{Cl}(r, s)$ (convention of [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^cau-cb-7-1|Caution: Two sign conventions for the Clifford relation]]) is a matrix algebra over $\mathbb R$, $\mathbb C$ or $\mathbb H$, or a sum of two such, determined by $r - s \bmod 8$:
>
> | $r - s \bmod 8$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
> |---|---|---|---|---|---|---|---|---|
> | $\mathrm{Cl}(r, s)$ | $M(\mathbb R)$ | $M(\mathbb R)\oplus M(\mathbb R)$ | $M(\mathbb R)$ | $M(\mathbb C)$ | $M(\mathbb H)$ | $M(\mathbb H)\oplus M(\mathbb H)$ | $M(\mathbb H)$ | $M(\mathbb C)$ |
>
> (matrix sizes fixed by $\dim = 2^{r+s}$). So $\mathrm{Cl}(1,3) \cong M_2(\mathbb H)$ and $\mathrm{Cl}(3,1) \cong M_4(\mathbb R)$: with $\{\gamma^\mu, \gamma^\nu\} = +2g^{\mu\nu}$ and $g = (+,-,-,-)$ there are no real $4\times4$ Dirac matrices, and Majorana matrices are purely imaginary. Stated only (SPEC-CB decision 6), as a pointer for the Majorana field (QFT C9, planned); proof not given here. Source: Figueroa-O'Farrill, Spin Geometry, Thm. 2.7 and the Clifford chessboard of §2.3 (proved there from the periodicities of Thm. 2.3; his $C\ell(s,t)$ is this table's $\mathrm{Cl}(t,s)$, so his $s - t$ is $-(r - s)$ here; the table above is his, translated and checked entry by entry, e.g. his $C\ell(3,1) \cong \mathbb H(2)$ is $\mathrm{Cl}(1,3) \cong M_2(\mathbb H)$).

^rem-cb-7-1

> [!remark]- Connections
> - The universal property (Theorem §CB.7.7) is the whole reason Dirac matrices are unique up to change of basis: a Clifford module is a homomorphism out of one fixed algebra, and §CB.8 shows that algebra (complexified) is a matrix algebra.
> - The volume element is $\gamma^5$ in disguise, up to the orientation sign that depends on the choice of Dirac module (Theorem §CB.7.19; [[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵#^cau-cb-12-1|Caution: Two Dirac modules, and the sign of γ⁵]]), and Theorem §CB.7.20 is the algebraic form of "boosts are $\gamma^0\gamma^i$": the even part of $\mathrm{Cl}(1,3)$ is generated by $e_ie_0$, which square to $+1$ like Pauli matrices (§CB.11).
> - **Used in**: Definitions §CB.7.6–Theorem §CB.7.10 — [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-2|Theorem §C5a.0.2]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-5|Theorem §C5a.1.5]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9|Def. §C5a.1.9]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-4|Def. §C5a.4.4]]; Theorem §CB.7.13 — [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]; Theorems §CB.7.16–§CB.7.17 — [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-8|Def. §C5a.1.8]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]], [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-8|Theorem §C5a.11.8]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]]; Theorem §CB.7.19 — [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-5|Theorem §C5a.11.5]]; Theorem §CB.7.21 — [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^ex-c5a-0-1|Example §C5a.0.1]].
