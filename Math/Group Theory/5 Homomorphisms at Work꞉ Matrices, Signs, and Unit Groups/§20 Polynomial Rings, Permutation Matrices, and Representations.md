---
type: section
subject: "[[Group Theory]]"
chapter: 5
section: 20
tags: [group-theory, math493]
---
← [[§19 S₃, ℤ∕nℤ and Uₙ]] · ↑ [[· 5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups]] · [[§21 The Sign Homomorphism and the Alternating Group]] →

*Reference: Pinter Ch. 24 (rings of polynomials). Permutation matrices and representations are not treated in Pinter.*

> [!definition] Definition §20.1: Polynomial Ring in Several Variables
> Let $k$ be a [[§3 Basic Examples of Groups#^def-3-3|field]] (e.g. $\mathbb{Q}$). A **monomial** in the variables $x_1, \ldots, x_n$ is a product $x_1^{a_1} x_2^{a_2} \cdots x_n^{a_n}$ with exponents $a_i \in \mathbb{Z}_{\geq 0}$ (the monomial with all $a_i = 0$ is $1$). A **polynomial** is a finite sum of monomials with coefficients in $k$,
>
> $$
> f = \sum_{(a_1, \ldots, a_n)} c_{a_1 \cdots a_n}\, x_1^{a_1} \cdots x_n^{a_n}, \qquad c_{a_1 \cdots a_n} \in k, \text{ only finitely many nonzero}.
> $$
>
> The set of all such polynomials is written $k[x_1, \ldots, x_n]$, the **polynomial ring** in $n$ variables over $k$. Two polynomials are equal iff all their coefficients agree. Addition is coefficientwise, and multiplication is by expanding products of monomials ($x^{a} x^{b} = x^{a+b}$ exponentwise) and collecting like terms.

^def-20-1

> [!remark]- Connections
> - The one-variable polynomials of linear algebra: [[§4 Span and Linear Independence#^ladr-2-10|LADR 2.10]].

> [!definition] Definition §20.2: Commutative Ring (provisional)
> A **commutative ring** is a set $R$ with two operations $+$ and $\cdot$ such that $(R, +)$ is an abelian group with identity $0$, and multiplication is associative, commutative, has an identity $1$, and distributes over addition. Thus a commutative ring satisfies all the [[§3 Basic Examples of Groups#^def-3-3|field axioms]] except that nonzero elements need not have multiplicative inverses. Rings are treated properly later in the course.

^def-20-2

> [!remark] Remark: $k[x_1, \ldots, x_n]$ as a Ring
> $k[x_1, \ldots, x_n]$ is a commutative ring but not a field: $x_1$ has no inverse, since no polynomial $g$ satisfies $x_1 g = 1$ (the product would have degree $\geq 1$). $\mathbb{Z}$ is another example. Polynomials are treated here as *formal expressions* determined by their coefficients, not as functions; over an infinite field the two viewpoints agree, but the formal one is what the algebra uses.

^rem-20-1

> [!definition] Definition §20.3: The Action of $S_n$ on $k[x_1, \ldots, x_n]$
> For $\sigma \in S_n$ and $f \in k[x_1, \ldots, x_n]$, define $\sigma \cdot f$ to be the polynomial obtained from $f$ by replacing each variable $x_i$ by $x_{\sigma(i)}$:
>
> $$
> (\sigma \cdot f)(x_1, \ldots, x_n) = f\big(x_{\sigma(1)}, x_{\sigma(2)}, \ldots, x_{\sigma(n)}\big).
> $$
>
> Concretely, $\sigma$ renames the variables according to the permutation.

^def-20-3

> [!definition] Definition §20.4: Symmetric Polynomial
> A polynomial $f$ is **symmetric** if $\sigma \cdot f = f$ for every $\sigma \in S_n$.

^def-20-4

> [!remark]- Connections
> - The companion notion, *alternating*: [[§21 The Sign Homomorphism and the Alternating Group#^def-21-4|Alternating Polynomial]]; $A_n$ as the stabilizer of $\Delta$: [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-10|Cor. §21.10]].

> [!example] Example §20.1: Permuting Variables
> Let $n = 3$ and $\sigma = (1\,2\,3)$, so $x_1 \mapsto x_2$, $x_2 \mapsto x_3$, $x_3 \mapsto x_1$.
> - $f = x_1 + 2x_2 + 3x_3$: $\ \sigma \cdot f = x_2 + 2x_3 + 3x_1$. Not symmetric.
> - $f = x_1 x_2 + x_2 x_3 + x_1 x_3$: $\ \sigma \cdot f = x_2 x_3 + x_3 x_1 + x_2 x_1 = f$. Checking the transposition $(1\,2)$ as well gives $x_2 x_1 + x_1 x_3 + x_2 x_3 = f$; since $(1\,2)$ and $(1\,2\,3)$ generate $S_3$ ([[§13 The Symmetric Group S₃#^prop-13-1|§13.1]]), $f$ is symmetric. It is the second **elementary symmetric polynomial** $e_2$; the others are $e_1 = x_1 + x_2 + x_3$ and $e_3 = x_1 x_2 x_3$.
> - $\Delta = \prod_{1 \leq i < j \leq n}(x_i - x_j)$ is the polynomial of [[493 Problem Set 1#^hw-1-5|PS 1.5]]. For $n = 2$, $\Delta = x_1 - x_2$, and $(1\,2) \cdot \Delta = x_2 - x_1 = -\Delta$: not symmetric, but changed only by a sign. The behavior of $\Delta$ under general $\sigma$ is the content of that problem ([[§21 The Sign Homomorphism and the Alternating Group#^thm-21-2|Three Formulas for the Sign]]).

^ex-20-1

> [!theorem] Proposition §20.1: Compatibility of the Action with Composition
> For all $\sigma, \tau \in S_n$ and $f \in k[x_1, \ldots, x_n]$:
>
> $$
> e \cdot f = f, \qquad \sigma \cdot (\tau \cdot f) = (\sigma\tau) \cdot f.
> $$
>
> Moreover each map $f \mapsto \sigma \cdot f$ respects sums and products: $\sigma \cdot (f + g) = \sigma \cdot f + \sigma \cdot g$ and $\sigma \cdot (fg) = (\sigma \cdot f)(\sigma \cdot g)$.

^prop-20-1

> [!proof]+ Proof
> $e \cdot f = f$ since renaming each $x_i$ to $x_i$ changes nothing. For the composition rule: $\tau \cdot f = f(x_{\tau(1)}, \ldots, x_{\tau(n)})$, and applying $\sigma$ renames each $x_j$ appearing here to $x_{\sigma(j)}$; the variable in position $i$ is $x_{\tau(i)}$, which becomes $x_{\sigma(\tau(i))} = x_{(\sigma\tau)(i)}$. So $\sigma \cdot (\tau \cdot f) = f(x_{(\sigma\tau)(1)}, \ldots, x_{(\sigma\tau)(n)}) = (\sigma\tau) \cdot f$. Renaming variables commutes with forming sums and products of polynomials, giving the last two identities.

^pf-20-1

*Uses:* [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-3|Def. §20.3]], [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-1|Def. §20.1]]

> [!remark]- Connections
> - These are the action axioms: [[§25 Actions#^ex-25-2|Ex. §25.2]] (4), [[§25 Actions#^def-25-1|Def. §25.1]].

> [!definition] Definition §20.5: The Standard Basis of $k^n$
> Let $k$ be a field. The vector space $k^n$ consists of column vectors $v = (v_1, \ldots, v_n)^{\mathsf{T}}$ with $v_i \in k$, under componentwise addition and scalar multiplication. The **standard basis vector** $e_i$ is the vector with a $1$ in position $i$ and $0$ elsewhere:
>
> $$
> e_1 = \begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}, \quad e_2 = \begin{pmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{pmatrix}, \quad \ldots, \quad e_n = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{pmatrix}.
> $$
>
> Every $v \in k^n$ is uniquely $v = v_1 e_1 + \cdots + v_n e_n$; the $v_i$ are its **coordinates**. The set $\{e_1, \ldots, e_n\}$ is the **standard basis**: it [[§4 Span and Linear Independence#^ladr-2-7|spans]] $k^n$ and is [[§4 Span and Linear Independence#^ladr-2-15|linearly independent]]. In the context of $S_n$, the index set $\{1, \ldots, n\}$ on which permutations act is identified with the standard basis by $i \leftrightarrow e_i$.

^def-20-5

> [!remark]- Connections
> - Linear-algebra home: [[§5 Bases#^ladr-2-27|LADR 2.27]] (a) (standard basis of $\mathbb{F}^n$), [[§5 Bases#^ladr-2-26|LADR 2.26]] (basis), [[§1 Rⁿ and Cⁿ#^ladr-1-11|LADR 1.11]] ($\mathbb{F}^n$, coordinates).
> - Unique coordinates are the [[§5 Bases#^ladr-2-28|Criterion for basis]] (LADR 2.28).

> [!theorem] Theorem §20.2: Linear Extension
> Let $V$ be a vector space over $k$ with basis $b_1, \ldots, b_n$, and let $W$ be any vector space over $k$. For any choice of vectors $w_1, \ldots, w_n \in W$ there is exactly one linear map $T: V \to W$ with $T(b_i) = w_i$ for all $i$, namely
>
> $$
> T(c_1 b_1 + \cdots + c_n b_n) = c_1 w_1 + \cdots + c_n w_n.
> $$
>
> In particular, two linear maps that agree on a basis are equal. When $V = W = k^n$ with the standard basis, the [[§9 Matrices#^ladr-3-31|matrix]] of $T$ has $T(e_i) = w_i$ as its $i$-th column.

^thm-20-2

> [!proof]+ Proof
> **Existence:** Since every $v \in V$ has a unique expression $v = \sum c_i b_i$, the formula defines a function $T$ on all of $V$. It is linear: if $v = \sum c_i b_i$ and $v' = \sum c_i' b_i$, then $v + \lambda v' = \sum (c_i + \lambda c_i') b_i$, so $T(v + \lambda v') = \sum (c_i + \lambda c_i') w_i = T(v) + \lambda T(v')$. And $T(b_i) = w_i$ by taking $c_i = 1$, other coefficients $0$.
>
> **Uniqueness:** If $T'$ is linear with $T'(b_i) = w_i$, then by linearity $T'(\sum c_i b_i) = \sum c_i T'(b_i) = \sum c_i w_i = T(\sum c_i b_i)$, so $T' = T$.
>
> **Matrix:** The $i$-th column of the matrix of $T$ is by definition the coordinate vector of $T(e_i)$, which is $w_i$ itself when $W = k^n$.

^pf-20-2

*Uses:* [[§5 Bases#^ladr-2-28|LADR 2.28]], [[§7 Vector Space of Linear Maps#^ladr-3-1|LADR 3.1]], [[§9 Matrices#^ladr-3-31|LADR 3.31]], [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-5|Def. §20.5]]

> [!remark]- Connections
> - Linear-algebra home: the [[Linear map lemma]] ([[§7 Vector Space of Linear Maps#^ladr-3-4|LADR 3.4]]).
> - Columns of the matrix of a linear map: [[§9 Matrices#^ladr-3-31|LADR 3.31]].

> [!theorem] Corollary §20.3: Permutations of the Basis Give Invertible Linear Maps
> Let $\sigma \in S_n$. There is a unique linear map $T_\sigma: k^n \to k^n$ with $T_\sigma(e_i) = e_{\sigma(i)}$ for all $i$. It is [[§10 Invertibility and Isomorphisms#^ladr-3-59|invertible]], with inverse $T_{\sigma^{-1}}$, and $T_\sigma \circ T_\tau = T_{\sigma\tau}$. Its matrix is the permutation matrix $M(\sigma)$ defined below ([[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-6|Def. §20.6]]).

^cor-20-3

> [!proof]+ Proof
> Existence and uniqueness of $T_\sigma$ are [[§20 Polynomial Rings, Permutation Matrices, and Representations#^thm-20-2|the theorem]] with $w_i = e_{\sigma(i)}$. On basis vectors, $T_\sigma T_\tau (e_i) = T_\sigma(e_{\tau(i)}) = e_{\sigma\tau(i)} = T_{\sigma\tau}(e_i)$, so $T_\sigma T_\tau = T_{\sigma\tau}$ by uniqueness (two linear maps agreeing on a basis are equal). Then $T_\sigma T_{\sigma^{-1}} = T_{e} = \operatorname{id}$ and likewise in the other order, since $T_e$ fixes every basis vector.

^pf-20-3

*Uses:* [[§20 Polynomial Rings, Permutation Matrices, and Representations#^thm-20-2|§20.2]], [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-5|Def. §20.5]], [[§3 Basic Examples of Groups#^def-3-5|Def. §3.5]], [[§7 Vector Space of Linear Maps#^ladr-3-4|LADR 3.4]], [[§10 Invertibility and Isomorphisms#^ladr-3-59|LADR 3.59]]

> [!remark]- Connections
> - Linear-algebra home: [[Linear map lemma]] ([[§7 Vector Space of Linear Maps#^ladr-3-4|LADR 3.4]]) for existence/uniqueness; [[§10 Invertibility and Isomorphisms#^ladr-3-59|LADR 3.59]] for invertibility.

> [!theorem] Proposition §20.4: Permutation Representation of $S_X$
> Let $X$ be a finite set and $k^X$ the $k$-vector space with basis $\{e_x : x \in X\}$ indexed by $X$. Every bijection $\sigma: X \to X$ extends uniquely to a linear map $T_\sigma: k^X \to k^X$ with $T_\sigma(e_x) = e_{\sigma(x)}$, and $\sigma \mapsto T_\sigma$ is an injective homomorphism $S_X \to GL(k^X)$.

^prop-20-4

> [!proof]+ Proof
> As for $X = \{1, \ldots, n\}$: existence and uniqueness of $T_\sigma$ is [[§20 Polynomial Rings, Permutation Matrices, and Representations#^thm-20-2|Linear Extension]]; $T_\sigma T_\tau = T_{\sigma\tau}$ and $T_{\sigma^{-1}} = T_\sigma^{-1}$ are checked on basis vectors, two linear maps agreeing on a basis being equal; and $T_\sigma = T_\tau$ forces $e_{\sigma(x)} = e_{\tau(x)}$ for all $x$, i.e. $\sigma = \tau$.

^pf-20-4

*Uses:* [[§20 Polynomial Rings, Permutation Matrices, and Representations#^thm-20-2|§20.2]], [[§20 Polynomial Rings, Permutation Matrices, and Representations#^cor-20-3|§20.3]], [[§3 Basic Examples of Groups#^def-3-5|Def. §3.5]], [[§15 Homomorphisms#^def-15-1|Def. §15.1]], [[§7 Vector Space of Linear Maps#^ladr-3-4|LADR 3.4]]

> [!remark]- Connections
> - Composed with Cayley's embedding $G \to S_G$ this gives [[§25 Actions#^cor-25-6|Every Finite Group Is a Matrix Group]].

> [!remark] Remark: From a Set to a Vector Space
> The corollary [[§20 Polynomial Rings, Permutation Matrices, and Representations#^cor-20-3|Permutations of the Basis Give Invertible Linear Maps]] is the mechanism by which a permutation of *symbols* becomes a *linear map*: $\sigma$ is only defined on the $n$ basis vectors, and linear extension does the rest. Nothing about $\sigma$ is used except that it is a bijection of the index set, which is why the same construction works for any finite set $X$.

^rem-20-2

> [!definition] Definition §20.6: Permutation Matrices
> For $\sigma \in S_n$, the **permutation matrix** $M(\sigma) \in GL_n(k)$ is the [[§9 Matrices#^ladr-3-31|matrix]] of the linear map $T_\sigma: k^n \to k^n$ of [[§20 Polynomial Rings, Permutation Matrices, and Representations#^cor-20-3|Permutations of the Basis Give Invertible Linear Maps]], i.e. the unique linear map sending each standard basis vector $e_i$ to $e_{\sigma(i)}$. Thus column $i$ of $M(\sigma)$ has a single nonzero entry, a $1$ in row $\sigma(i)$:
>
> $$
> M(\sigma)_{ji} = \begin{cases} 1 & j = \sigma(i), \\ 0 & \text{otherwise.} \end{cases}
> $$
>
> Multiplying a column vector by $M(\sigma)$ moves its $i$-th entry to position $\sigma(i)$.

^def-20-6

> [!remark]- Connections
> - Linear-algebra home: the matrix of a linear map, [[§9 Matrices#^ladr-3-31|LADR 3.31]].
> - Computational version: [[§15 Elementary Matrices and the Inversion Algorithm#^def-15-2|235 Def. §15.2]] (permutation matrices, all six for n = 3).

> [!example] Example §20.2: $M(\sigma)$ for $\sigma = (1\,2\,3)$
> Since $\sigma(1) = 2$, $\sigma(2) = 3$, $\sigma(3) = 1$, the columns are $e_2, e_3, e_1$:
>
> $$
> M(\sigma) = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}, \qquad M(\sigma) \begin{pmatrix} a \\ b \\ c \end{pmatrix} = \begin{pmatrix} c \\ a \\ b \end{pmatrix}.
> $$
>
> The entry $a$ (position $1$) has moved to position $\sigma(1) = 2$, as the definition says. For the transposition $(1\,2)$, $M = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$, which swaps the first two entries of a vector.
>
> **Recipe.** Write the columns $e_{\sigma(1)}, e_{\sigma(2)}, \ldots, e_{\sigma(n)}$ side by side; equivalently, in column $i$ place a $1$ in row $\sigma(i)$. For $\sigma = (1\,4\,2\,3) \in S_4$ ($1 \mapsto 4$, $2 \mapsto 3$, $3 \mapsto 1$, $4 \mapsto 2$) the columns are $e_4, e_3, e_1, e_2$:
>
> $$
> M(\sigma) = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix}, \qquad M(\sigma)\begin{pmatrix} a \\ b \\ c \\ d \end{pmatrix} = \begin{pmatrix} c \\ d \\ b \\ a \end{pmatrix}.
> $$
>
> To read $\sigma$ off a matrix, locate the $1$ in each column: column $i$ has its $1$ in row $\sigma(i)$. Row $j$ has its $1$ in column $\sigma^{-1}(j)$. Any matrix with exactly one $1$ in each row and column, zeros elsewhere, is $M(\sigma)$ for a unique $\sigma$.

^ex-20-2

![[m493-19-1.svg]]
*$M(\sigma)$ for $\sigma = (1\,2\,3)$, as in Ex. §20.2. Column $i$ is $e_{\sigma(i)}$, so its single $1$ (red) sits in row $\sigma(i)$. Multiplying a vector by $M(\sigma)$ therefore carries the entry in position $i$ to position $\sigma(i)$ (right): $a$ moves from $1$ to $2$, $b$ from $2$ to $3$, $c$ from $3$ to $1$.*

> [!theorem] Proposition §20.5: $\sigma \mapsto M(\sigma)$ Is an Injective Homomorphism $S_n \to GL_n(k)$
> For all $\sigma, \tau \in S_n$: $M(\sigma\tau) = M(\sigma) M(\tau)$, $M(e) = I_n$, and $M(\sigma)$ is invertible with $M(\sigma)^{-1} = M(\sigma^{-1}) = M(\sigma)^{\mathsf{T}}$. The map $\sigma \mapsto M(\sigma)$ is injective.

^prop-20-5

> [!proof]+ Proof
> On basis vectors, $M(\sigma)M(\tau) e_i = M(\sigma) e_{\tau(i)} = e_{\sigma(\tau(i))} = e_{(\sigma\tau)(i)} = M(\sigma\tau) e_i$; two matrices agreeing on a basis are equal. $M(e)$ fixes every $e_i$, so $M(e) = I_n$. Then $M(\sigma)M(\sigma^{-1}) = M(\sigma\sigma^{-1}) = I_n$ and likewise on the other side. For the transpose: $M(\sigma)_{ji} = 1$ iff $j = \sigma(i)$ iff $i = \sigma^{-1}(j)$ iff $M(\sigma^{-1})_{ij} = 1$, so $M(\sigma^{-1}) = M(\sigma)^{\mathsf{T}}$; in particular permutation matrices are [[§3 Basic Examples of Groups#^def-3-8|orthogonal]]. Injectivity: if $M(\sigma) = M(\tau)$ then $e_{\sigma(i)} = e_{\tau(i)}$ for all $i$, so $\sigma = \tau$.

^pf-20-5

*Uses:* [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-6|Def. §20.6]], [[§20 Polynomial Rings, Permutation Matrices, and Representations#^thm-20-2|§20.2]], [[§3 Basic Examples of Groups#^def-3-8|Def. §3.8]], [[§9 Matrices#^ladr-3-43|LADR 3.43]], [[§9 Matrices#^ladr-3-54|LADR 3.54]], [[§10 Invertibility and Isomorphisms#^ladr-3-80|LADR 3.80]]

> [!remark]- Connections
> - Linear-algebra home: matrix of a product is the product of the matrices, [[§9 Matrices#^ladr-3-43|LADR 3.43]]; orthogonal (real unitary) matrices, [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR 7.57]].
> - Composed with $\det$ it gives the sign: [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|The Sign Is a Homomorphism]].
> - Computational version: the inverse of a permutation matrix is its transpose, worked in [[§15 Elementary Matrices and the Inversion Algorithm#^ex-15-1|235 Ex. §15.1]](c).

> [!remark] Remark: Row vs. Column Convention
> Some sources define the permutation matrix by rows, “row $i$ is $e_{\sigma(i)}$,” which produces the [[§9 Matrices#^ladr-3-54|transpose]] of ours, i.e. $M(\sigma^{-1})$; under that convention $M(\sigma)M(\tau) = M(\tau\sigma)$, reversed. The column convention above is the one compatible with right-to-left composition, $(f \circ g)(j) = f(g(j))$, as used in this course ([[§10 Cycle Notation and the Group S₃#^rem-10-1|Convention Warning]]). Since $\det M(\sigma^{-1}) = (\det M(\sigma))^{-1}$ ([[§37 Determinants#^ladr-9-49|LADR 9.49]]) and the determinant of a permutation matrix is $\pm 1$, the choice does not affect the determinant.

^rem-20-3

> [!remark]- Connections
> - $\det M(\sigma) = \pm 1$ is proved in [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-2|Three Formulas for the Sign]]; multiplicativity of $\det$: [[§37 Determinants#^ladr-9-49|LADR 9.49]].

> [!definition] Definition §20.7: Representation
> A **representation** of a group $G$ is a homomorphism $G \to GL_n(k)$ for some field $k$ and some $n \geq 1$ (more generally $G \to GL(V)$ for a $k$-vector space $V$). Representations in general are the subject of the second half of the course.

^def-20-7

> [!remark]- Connections
> - Every finite group has a faithful representation: [[§25 Actions#^cor-25-6|Every Finite Group Is a Matrix Group]].
> - One-dimensional representations are characters: [[§46 Characters#^rem-46-4|One-Dimensional Representations]]; $\operatorname{sgn}$ is the first example ([[§21 The Sign Homomorphism and the Alternating Group#^rem-21-3|The Origin of the Names]]).
> - Used in Relativity: each tensor type is a representation of the Lorentz group, which acts on type (m, n) components by m factors of the matrix and n of its inverse transpose — [[§B2.2 Tensors and the Covariance Principle|REL §B2.2]] (Connections), [[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]].
> - Used in Quantum Mechanics: the spin-½ rotation matrices are a representation of $SU(2)$, not of $SO(3)$ — [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]; the product of two angular-momentum representations decomposed into irreducible ones — [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]]; the symmetric group acting on the kets of $N$ particles — [[§C12.1★ Permutation Symmetry and the Symmetrization Postulate#^thm-c12-1-1|QM Theorem §C12.1.1]].
> - Used in Quantum Field Theory: representations of Lie groups and Lie algebras on a carrier space, with equivalence, invariant subspaces, irreducibility and unitarity — [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-5|QFT Def. §C3.1.5]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-7|QFT Def. §C3.1.7]]; and Schur's lemma, which these notes do not contain yet (the representation theory of the second half of the course), so its home in the vault is [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|QFT Theorem §C3.1.3]].

> [!definition] Definition §20.8: Permutation Representation
> The homomorphism $\sigma \mapsto M(\sigma)$, $S_n \to GL_n(k)$, of [[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-5|the proposition just proved]] is the **permutation representation** of $S_n$: it realizes $S_n$ as a group of matrices, with composition of permutations becoming matrix multiplication, and its image is the subgroup of permutation matrices listed among the subgroups of $GL_n(\mathbb{R})$ in [[§5 A Zoo of Subgroups#^ex-5-4|WS 1.7]].

^def-20-8

> [!remark] Remark: Group Actions
> The three ways $S_n$ has appeared — on $\{1, \ldots, n\}$, on $k^n$ via $M(\sigma)$, and on $k[x_1, \ldots, x_n]$ — are instances of a single notion, that of a *group action*, developed in [[· 6 Group Actions, Cosets, and Lagrange's Theorem|Chapter 6]]; the compatibility statements proved above are exactly the [[§25 Actions#^def-25-1|action axioms]].

^rem-20-4

> [!remark]- Connections
> - The three actions reappear as [[§25 Actions#^ex-25-2|Ex. §25.2]] (1), (4).
