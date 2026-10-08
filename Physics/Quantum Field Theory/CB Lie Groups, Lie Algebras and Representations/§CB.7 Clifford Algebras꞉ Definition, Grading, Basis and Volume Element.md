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

*Sources (planned for the proofs; each to be checked against the text when the proof is written): P. Woit, Quantum Theory, Groups and Representations, Ch. 28 (§28.1 complex, §28.2 real Clifford algebras; relation $[\gamma_j, \gamma_k]_+ = 2\delta_{jk}$, the physics sign) and Ch. 29 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · J. Figueroa-O'Farrill, Spin Geometry, lecture notes, Edinburgh 2010 (https://empg.maths.ed.ac.uk/Activities/Spin/SpinNotes.pdf; not yet checked — the server was unreachable on 2026-10-08) · D. Tong, Lectures on Quantum Field Theory, chapter "The Dirac Equation" (https://www.damtp.cam.ac.uk/user/tong/qft.html) · Linear Algebra (LADR) §§11, 35–38 · the user's PHY 513 notes, Ch. 8 · Peskin & Schroeder, §3.2, §3.4 · the rest written here.*

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
> *Source (planned): Woit, Ch. 28–29 · Figueroa-O'Farrill, Spin Geometry (to be checked)*

^def-cb-7-6

> [!caution] Caution: Two sign conventions for the Clifford relation
> These notes use the physics convention $vv = +q(v)$, which with $q = g$ gives $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]; Woit, Ch. 28, uses the same sign). Much of the mathematical literature (e.g. Lawson–Michelsohn) writes $vv = -q(v)$; its $\mathrm{Cl}(V, q)$ is this section's $\mathrm{Cl}(V, -q)$, and labels such as $\mathrm{Cl}_{r,s}$ or $\mathrm{Cl}(r, s)$ then refer to different algebras. Over $\mathbb C$ the two conventions give isomorphic algebras ($v \mapsto iv$). Here $\mathrm{Cl}(r, s)$ always has $r$ generators squaring to $+1$ and $s$ to $-1$: in $\mathrm{Cl}(1,3)$, $(\gamma^0)^2 = +1$, $(\gamma^i)^2 = -1$.
>
> *Source: SPEC-CB decision 6 · Woit, Ch. 28 · written here*

^cau-cb-7-1

> [!theorem] Theorem §CB.7.7: Universal Property of the Clifford Algebra
> Let $A$ be an associative algebra over $\mathbb K$ ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-5|Def. §CB.3.5]]) and $f : V \to A$ a linear map with $f(v)^2 = q(v)1_A$ for all $v \in V$. Then there is a unique algebra homomorphism $\tilde f : \mathrm{Cl}(V, q) \to A$ ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-6|Def. §CB.3.6]]) with $\tilde f(v) = f(v)$ for $v \in V$.
>
> *Source (planned): Woit, Ch. 29 · Figueroa-O'Farrill, Spin Geometry (to be checked) · the Minkowski case stated in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-2|§C5a.0, ★ Remark]]*

^thm-cb-7-7

> [!proof]- Proof (to be filled)
> *To be filled (extend $f$ to $T(V)$ multiplicatively, using [[§38 Tensor Products#^ladr-9-92|LADR Thm. 9.92]] on each $V^{\otimes k}$; it kills $I_q$; Theorem §CB.7.5).*

^pf-cb-7-7

> [!theorem] Theorem §CB.7.8: The Anticommutator and the Embedding of V
> In $\mathrm{Cl}(V, q)$, $vw + wv = 2B(v, w)$ for all $v, w \in V$; in an orthogonal basis $e_ie_j = -e_je_i$ ($i \ne j$) and $e_i^2 = q(e_i)$. The map $V \to \mathrm{Cl}(V, q)$ is injective.
>
> *Source (planned): Woit, Ch. 28 · written here*

^thm-cb-7-8

> [!proof]- Proof
> **The anticommutator.** Apply $uu = q(u)$ to $u = v + w$: $(v + w)(v + w) = vv + vw + wv + ww = q(v) + vw + wv + q(w)$, and this equals $q(v + w)$. Hence $vw + wv = q(v + w) - q(v) - q(w) = 2B(v, w)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-1|Def. §CB.7.1]]). For orthogonal $e_i$, $e_j$ ($i \ne j$) the right side is $0$; for $i = j$ it is $2q(e_i)$.
>
> **Injectivity** — *to be filled* (it follows from the basis theorem, Theorem §CB.7.16, whose proof constructs a module in which the images of a basis of $V$ are independent).

^pf-cb-7-8

## Clifford modules

> [!definition] Definition §CB.7.9: Clifford Module
> A **Clifford module** of $(V, q)$ is a representation of the algebra $\mathrm{Cl}(V, q)$ on a complex vector space $W$ ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-7|Def. §CB.3.7]]): an algebra homomorphism $\gamma : \mathrm{Cl}(V, q) \to \operatorname{End}_{\mathbb C}(W)$. Invariant subspaces, irreducibility, intertwiners and equivalence are those of Def. §CB.3.7.
>
> *Source (planned): written here*

^def-cb-7-9

> [!theorem] Theorem §CB.7.10: A Clifford Module Is a Set of Anticommuting Square Roots
> Clifford modules of $(V, q)$ on $W$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-9|Def. §CB.7.9]]) correspond bijectively, by restriction to $V$, to linear maps $\gamma : V \to \operatorname{End}(W)$ with $\gamma(v)^2 = q(v)\mathbb 1$ for all $v$; equivalently, for a basis $e_\mu$ of $V$ with $B(e_\mu, e_\nu) = g_{\mu\nu}$, to matrices $\gamma_\mu = \gamma(e_\mu)$ with $\gamma_\mu\gamma_\nu + \gamma_\nu\gamma_\mu = 2g_{\mu\nu}\mathbb 1$.
>
> *Source (planned): written here (from Theorem §CB.7.7 and Theorem §CB.7.8)*

^thm-cb-7-10

> [!proof]- Proof (to be filled)
> *To be filled (Theorem §CB.7.7 with $A = \operatorname{End}(W)$; the matrix form by polarization as in Theorem §CB.7.8).*

^pf-cb-7-10

The Dirac matrices and the Dirac maps, a Clifford module of $\mathrm{Cl}(1,3)$ on spinor space, defined in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]]; the Clifford algebra in physics language, in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]]:

![[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7]]

![[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9]]

![[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-2]]

## Grading and involutions

> [!theorem] Theorem §CB.7.11: The Grade Automorphism
> There is a unique algebra automorphism $\alpha$ of $\mathrm{Cl}(V, q)$ with $\alpha(v) = -v$ for $v \in V$, and $\alpha^2 = \mathbb 1$.
>
> *Source (planned): Woit, Ch. 29 · written here*

^thm-cb-7-11

> [!proof]- Proof (to be filled)
> *To be filled (Theorem §CB.7.7 applied to $f(v) = -v$; $\alpha^2$ fixes $V$, hence is the identity by uniqueness).*

^pf-cb-7-11

> [!definition] Definition §CB.7.12: Even and Odd Parts
> The **even part** $\mathrm{Cl}^0(V, q)$ and the **odd part** $\mathrm{Cl}^1(V, q)$ are the $+1$ and $-1$ eigenspaces of $\alpha$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-11|Theorem §CB.7.11]]): the spans of products of an even, resp. odd, number of vectors.
>
> *Source (planned): written here*

^def-cb-7-12

> [!theorem] Theorem §CB.7.13: The ℤ₂-Grading
> $\mathrm{Cl}(V, q) = \mathrm{Cl}^0 \oplus \mathrm{Cl}^1$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-12|Def. §CB.7.12]]), and $\mathrm{Cl}^i\mathrm{Cl}^j \subset \mathrm{Cl}^{i + j \bmod 2}$. In particular $\mathrm{Cl}^0$ is a subalgebra, and products of two vectors, such as $\gamma^\mu\gamma^\nu$ and $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$, are even.
>
> *Source (planned): written here*

^thm-cb-7-13

> [!proof]- Proof (to be filled)
> *To be filled ($x = \frac12(x + \alpha x) + \frac12(x - \alpha x)$; $\alpha$ is multiplicative).*

^pf-cb-7-13

> [!theorem] Theorem §CB.7.14: The Reversal
> There is a unique linear map $t : \mathrm{Cl}(V, q) \to \mathrm{Cl}(V, q)$, the **reversal** (transpose), with $t(v) = v$ for $v \in V$ and $t(xy) = t(y)t(x)$; so $t(v_1v_2\cdots v_k) = v_k\cdots v_2v_1$. It satisfies $t^2 = \mathbb 1$ and $t\alpha = \alpha t$.
>
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked) · written here*

^thm-cb-7-14

> [!proof]- Proof (to be filled)
> *To be filled (Theorem §CB.7.7 into the opposite algebra of $\mathrm{Cl}(V, q)$).*

^pf-cb-7-14

> [!definition] Definition §CB.7.15: Clifford Conjugation
> The **Clifford conjugation** is $x \mapsto \bar x = \alpha(t(x))$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-11|Theorem §CB.7.11]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-14|Theorem §CB.7.14]]); $\overline{v_1\cdots v_k} = (-1)^kv_k\cdots v_1$.
>
> *Source (planned): written here*

^def-cb-7-15

## Basis, dimension and the exterior algebra

> [!theorem] Theorem §CB.7.16: Basis and Dimension
> Let $e_1, \dots, e_n$ be an orthogonal basis of $(V, q)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-1|Def. §CB.7.1]]). For $I = \{i_1 < \cdots < i_k\} \subset \{1, \dots, n\}$ put $e_I = e_{i_1}\cdots e_{i_k}$, $e_\varnothing = 1$. The $2^n$ elements $e_I$ form a basis of $\mathrm{Cl}(V, q)$; so $\dim\mathrm{Cl}(V, q) = 2^n$, and $\mathrm{Cl}^0$, $\mathrm{Cl}^1$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-12|Def. §CB.7.12]]) have the bases $e_I$ with $|I|$ even, resp. odd, each of dimension $2^{n-1}$ ($n \ge 1$).
>
> *Source (planned): Woit, Ch. 28 · Figueroa-O'Farrill, Spin Geometry (to be checked) · the $4\times4$ case: [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]]*

^thm-cb-7-16

> [!proof]- Proof (to be filled)
> *To be filled (spanning: reorder with Theorem §CB.7.8; independence: construct a $2^n$-dimensional module on $\Lambda V$, e.g. $\gamma(v) = v\wedge{} + \iota_v$, in which the $e_I$ act independently).*

^pf-cb-7-16

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
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked) · written here · the antisymmetrized products: [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-8|Def. §C5a.1.8]]*

^thm-cb-7-17

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-7-17

## The volume element

> [!definition] Definition §CB.7.18: Volume Element
> For an orthonormal basis $e_1, \dots, e_n$ of a nondegenerate real quadratic space ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-1|Def. §CB.7.1]]), the **volume element** is $\omega = e_1e_2\cdots e_n \in \mathrm{Cl}(V, q)$.
>
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked) · written here*

^def-cb-7-18

> [!theorem] Theorem §CB.7.19: Properties of the Volume Element
> Let $(V, q) = \mathbb R^{r,s}$, $n = r + s$, and $\omega$ as in [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-18|Def. §CB.7.18]].
> 1. Another orthonormal basis gives $\pm\omega$, the sign being the determinant of the change of basis: $\omega$ depends only on an orientation.
> 2. $\omega^2 = (-1)^{n(n-1)/2}(-1)^s$.
> 3. $\omega v = (-1)^{n-1}v\omega$ for $v \in V$: $\omega$ commutes with $\mathrm{Cl}^0$ always, and anticommutes with $V$ for $n$ even.
> 4. The centre of $\mathrm{Cl}(V, q)$ is $\mathbb R1$ for $n$ even and $\mathbb R1 \oplus \mathbb R\omega$ for $n$ odd; the centre of $\mathrm{Cl}^0$ is $\mathbb R1\oplus\mathbb R\omega$ for $n$ even and $\mathbb R1$ for $n$ odd; in every case the elements of $\mathrm{Cl}^0$ commuting with all of $\mathrm{Cl}(V, q)$ are $\mathbb R1$.
>
> For $\mathrm{Cl}(1,3)$: $\omega = e_0e_1e_2e_3$, $\omega^2 = -1$, and $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ is the image of $i\omega$ in a Dirac module with $e_\mu \mapsto \gamma^\mu$ for the standard basis ($q(e_0) = 1$, $q(e_i) = -1$), with $(\gamma^5)^2 = 1$ (the complex normalization, [[§CB.8 Complex Clifford Algebras and Clifford Modules#^def-cb-8-4|Def. §CB.8.4]]).
>
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked) · Peskin & Schroeder, §3.4 · written here*

^thm-cb-7-19

> [!proof]- Proof (to be filled)
> *To be filled (part 2: reorder $e_1\cdots e_ne_1\cdots e_n$ with $n(n-1)/2$ transpositions, then $\prod q(e_i) = (-1)^s$; part 3: moving $e_j$ through $\omega$ crosses $n - 1$ anticommuting factors and one commuting one; part 4 on the basis $e_I$).*

^pf-cb-7-19

γ⁵ and its properties, the volume element of the Dirac module, in [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] and [[§C5a.11 Gamma-Matrix Technology|§C5a.11]]:

![[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1]]

![[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1]]

![[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-5]]

## The even subalgebra and small examples

> [!theorem] Theorem §CB.7.20: The Even Subalgebra Is a Clifford Algebra of One Dimension Less
> Let $(V, q)$ be nondegenerate real, $e_0 \in V$ with $q(e_0) = \epsilon \in \{\pm1\}$, and $V' = e_0^\perp$ with $q'(v') = -\epsilon\,q(v')$. Then $v' \mapsto v'e_0$ extends to an algebra isomorphism $\mathrm{Cl}(V', q') \cong \mathrm{Cl}^0(V, q)$. In particular $\mathrm{Cl}^0(1,3) \cong \mathrm{Cl}(3,0)$ (with $e_0$ timelike, $f_i = e_ie_0$, $f_i^2 = +1$) and $\mathrm{Cl}^0(3,0) \cong \mathrm{Cl}(0,2)$.
>
> *Source (planned): written here · Figueroa-O'Farrill, Spin Geometry (to be checked)*

^thm-cb-7-20

> [!proof]- Proof (to be filled)
> *To be filled ($(v'e_0)^2 = -v'v'e_0e_0 = -\epsilon q(v')$, so Theorem §CB.7.7 gives a homomorphism; dimensions $2^{n-1}$ on both sides, Theorem §CB.7.16, and surjectivity onto the even basis).*

^pf-cb-7-20

> [!theorem] Theorem §CB.7.21: Clifford Algebras in Low Dimensions
> As real algebras:
>
> | $\mathrm{Cl}(r, s)$ | $\mathrm{Cl}(0,1)$ | $\mathrm{Cl}(1,0)$ | $\mathrm{Cl}(0,2)$ | $\mathrm{Cl}(2,0)$ | $\mathrm{Cl}(1,1)$ | $\mathrm{Cl}(3,0)$ | $\mathrm{Cl}(1,2)$ |
> |---|---|---|---|---|---|---|---|
> | $\cong$ | $\mathbb C$ | $\mathbb R\oplus\mathbb R$ | $\mathbb H$ | $M_2(\mathbb R)$ | $M_2(\mathbb R)$ | $M_2(\mathbb C)$ | $M_2(\mathbb C)$ |
>
> ($\mathbb H$ the quaternions, [[§40 The Unit Quaternions and SU(2)#^def-40-1|591 Def. §40.1]].) In particular $\mathrm{Cl}^0(3,0) \cong \mathbb H$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-20|Theorem §CB.7.20]]), and $\mathrm{Cl}(3,0)$ is realized by the Pauli matrices (§CB.10).
>
> *Source (planned): Woit, §28.2 · written here*

^thm-cb-7-21

> [!proof]- Proof (to be filled)
> *To be filled (explicit generators: $i$; $\operatorname{diag}(1, -1)$; $i, j$; $\sigma^1, \sigma^3$; $\sigma^1, i\sigma^2$; $\sigma^1, \sigma^2, \sigma^3$; $\sigma^3, i\sigma^1, i\sigma^2$; then dimension count).*

^pf-cb-7-21

The two-component square roots in $1 + 1$ and $2 + 1$ dimensions, which are modules of $\mathrm{Cl}(1,1)$ and $\mathrm{Cl}(1,2)$, in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]]:

![[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^ex-c5a-0-1]]

> [!remark]- ★ Remark: The real classification (not used in the course)
> Every real Clifford algebra $\mathrm{Cl}(r, s)$ (convention of [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^cau-cb-7-1|Caution: Two sign conventions for the Clifford relation]]) is a matrix algebra over $\mathbb R$, $\mathbb C$ or $\mathbb H$, or a sum of two such, determined by $r - s \bmod 8$:
>
> | $r - s \bmod 8$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
> |---|---|---|---|---|---|---|---|---|
> | $\mathrm{Cl}(r, s)$ | $M(\mathbb R)$ | $M(\mathbb R)\oplus M(\mathbb R)$ | $M(\mathbb R)$ | $M(\mathbb C)$ | $M(\mathbb H)$ | $M(\mathbb H)\oplus M(\mathbb H)$ | $M(\mathbb H)$ | $M(\mathbb C)$ |
>
> (matrix sizes fixed by $\dim = 2^{r+s}$). So $\mathrm{Cl}(1,3) \cong M_2(\mathbb H)$ and $\mathrm{Cl}(3,1) \cong M_4(\mathbb R)$: with $\{\gamma^\mu, \gamma^\nu\} = +2g^{\mu\nu}$ and $g = (+,-,-,-)$ there are no real $4\times4$ Dirac matrices, and Majorana matrices are purely imaginary. Stated only (SPEC-CB decision 6), as a pointer for the Majorana field (QFT C9, planned); proof not given here; source to be checked (Woit §28.2; Figueroa-O'Farrill, Spin Geometry).

^rem-cb-7-1

> [!remark]- Connections
> - The universal property (Theorem §CB.7.7) is the whole reason Dirac matrices are unique up to change of basis: a Clifford module is a homomorphism out of one fixed algebra, and §CB.8 shows that algebra (complexified) is a matrix algebra.
> - The volume element is $\gamma^5$ in disguise (Theorem §CB.7.19), and Theorem §CB.7.20 is the algebraic form of "boosts are $\gamma^0\gamma^i$": the even part of $\mathrm{Cl}(1,3)$ is generated by $e_ie_0$, which square to $+1$ like Pauli matrices (§CB.11).
> - **Used in**: Definitions §CB.7.6–Theorem §CB.7.10 — [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-2|Theorem §C5a.0.2]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-5|Theorem §C5a.1.5]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9|Def. §C5a.1.9]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-4|Def. §C5a.4.4]]; Theorem §CB.7.13 — [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]; Theorems §CB.7.16–§CB.7.17 — [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-8|Def. §C5a.1.8]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]], [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-8|Theorem §C5a.11.8]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]]; Theorem §CB.7.19 — [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-5|Theorem §C5a.11.5]]; Theorem §CB.7.21 — [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^ex-c5a-0-1|Example §C5a.0.1]].
