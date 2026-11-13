---
type: section
subject: "[[Group Theory]]"
chapter: 12
section: 68
tags: [group-theory, math493]
---
← [[§67 Characters of Representations]] · ↑ [[· 12 Characters]] · [[§69 Dual Representations]] →

*Source: Lecture and Worksheet 16, *Actions on matrix spaces* (Wed Nov 11): WS 16.1, WS 16.2 and the worksheet's theorem. WS 16.3–16.5 were not reached in class (the lecture of Fri Nov 13 recalled the statements of WS 16.3 and WS 16.5 without proof); they are stated in the last subsection of this section with proofs that are filled in. Reference: Axler, *Linear Algebra Done Right* (matrices of linear maps, eigenvalues, trace).*

Theorem [[§66 Invariant Vectors#^thm-66-10|§66.10]] computes the dimension of the invariant vectors of any representation from its character. This section applies it to the representation $\operatorname{Hom}(V, W)$, whose invariant vectors are the homomorphisms of representations $V \to W$. The result is a formula for the number of independent homomorphisms between two representations in terms of their characters. Over $\mathbb{R}$ and $\mathbb{C}$ the formula simplifies, because there $\chi_V(g^{-1})$ is $\chi_V(g)$ or its complex conjugate.

## Two More Descriptions of the Trace

The trace of a linear map $A: V \to V$ of a finite-dimensional vector space is $\sum_i A_{ii}$, computed in any basis of $V$, and $\operatorname{Tr}(SAS^{-1}) = \operatorname{Tr}(A)$ (Definition [[§66 Invariant Vectors#^def-66-2|§66.2]], Corollary [[§66 Invariant Vectors#^cor-66-2|§66.2]]). This definition does not depend on the basis, but it uses one. In answer to the question whether a basis is needed to make sense of the trace, the lecture of 11/11 recalled the definition and stated two further descriptions of the trace, without proof. They are written here for $n \times n$ matrices over a field $k$; for a linear map, take its matrix in any basis.

> [!theorem] Proposition §68.1: The Trace Is the Coefficient of $t$ in $\det(I + tA)$
> Let $A$ be an $n \times n$ matrix over $k$. Then $\det(I + tA)$ is a polynomial in $t$ with constant term $1$, and its coefficient of $t$ is $\operatorname{Tr}(A)$:
>
> $$
> \det(I + tA) = 1 + t\operatorname{Tr}(A) + (\text{terms divisible by } t^2).
> $$
>
> Over $\mathbb{R}$, this says $\operatorname{Tr}(A) = \dfrac{d}{dt}\det(I + tA)\Big|_{t=0}$. In physical terms: if a material is distorted so that the point at position $x$ moves to $x + tAx$, then $\operatorname{Tr}(A)$ is the rate at which volumes change at $t = 0$, because the linear map $I + tA$ multiplies volumes by $\det(I + tA)$ (for small $t$).
>
> *Source: lecture 11/11 (stated)*

^prop-68-1

> [!proof]+ Proof
> *Idea:* In the permutation formula for the determinant, every permutation other than the identity uses at least two off-diagonal entries of $I + tA$, each of which is a multiple of $t$.
>
> *(Not from class; filled in.)* Write $B = I + tA$. Its entries are polynomials in $t$: $B_{ii} = 1 + tA_{ii}$, and $B_{ij} = tA_{ij}$ for $i \neq j$. By the permutation formula for the determinant (a standard fact of linear algebra; Axler, Ch. 9),
>
> $$
> \det B = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \prod_{i=1}^n B_{i\sigma(i)}.
> $$
>
> *The terms with $\sigma \neq e$.* Such a $\sigma$ moves at least two indices: if $\sigma(i) = j \neq i$, then $\sigma(j) \neq j$, because $\sigma$ is injective and $j$ is already the image of $i$. So the product $\prod_i B_{i\sigma(i)}$ contains at least two off-diagonal entries, each a multiple of $t$, and the term is divisible by $t^2$.
>
> *The term with $\sigma = e$.* It is
>
> $$
> \prod_{i=1}^n (1 + tA_{ii}) = 1 + t\sum_{i=1}^n A_{ii} + (\text{terms divisible by } t^2).
> $$
>
> Adding up gives the formula. Over $\mathbb{R}$, the derivative at $t = 0$ of a polynomial $1 + c_1t + c_2t^2 + \cdots$ is $c_1$.

^pf-68-1

> [!remark]- Connections
> - Linear Algebra: the permutation formula for the determinant is [[§37 Determinants#^ladr-9-46|LADR 9.46]].
> - The same derivative at any invertible $g$, $\frac{d}{dt}\big|_{t=0}\det(g + tA) = \det(g)\operatorname{Tr}(g^{-1}A)$: [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|591 Prop. §12.1]].

![[m493-68-3.svg]]

*(The lecture of 11/11 drew the unit square and its slightly distorted image, with $e_1$ moved to $e_1 + tAe_1$; the matrix, the numbers and the labels are added.)* Proposition [[§68 Homomorphisms Between Representations#^prop-68-1|§68.1]] for $n = 2$ over $\mathbb{R}$, where $\det(I + tA) = (1 + ta_{11})(1 + ta_{22}) - t^2a_{12}a_{21} = 1 + t\operatorname{Tr}A + t^2\det A$ is the area of the image of the unit square under $I + tA$ (for small $t$). To first order in $t$ the area changes only through the stretches $ta_{11}$ and $ta_{22}$ of the two sides; the off-diagonal entries tilt the sides and change the area only at order $t^2$. For the matrix shown and $t = \frac14$: $1 + 0.4 + 0.028125 = 1.428125$.

> [!theorem] Proposition §68.2: The Trace Is the Only Linear Function That Vanishes on All $AB - BA$
> Let $n \geq 1$, and let $E_{ij}$ be the $n \times n$ matrix with the entry $1$ in position $(i, j)$ and $0$ elsewhere (a *matrix unit*).
>
> 1. The trace is a linear function from the $n \times n$ matrices over $k$ to $k$ with $\operatorname{Tr}(AB - BA) = 0$ for all $A$, $B$, and $\operatorname{Tr}(E_{11}) = 1$.
> 2. It is the only one: if $f$ is a linear function from the $n \times n$ matrices to $k$ with $f(AB - BA) = 0$ for all $A$, $B$ and $f(E_{11}) = 1$, then $f = \operatorname{Tr}$.
> 3. The matrices $AB - BA$ span the space of $n \times n$ matrices of trace zero. This is a subspace of dimension $n^2 - 1$ of the $n^2$-dimensional space of all $n \times n$ matrices.
>
> *Source: lecture 11/11 (stated)*

^prop-68-2

> [!proof]+ Proof
> *Idea:* Every off-diagonal matrix unit, and every difference $E_{ii} - E_{jj}$, is of the form $AB - BA$.
>
> *(Not from class; filled in.)* **(1)** The trace is linear, because the diagonal entries of $aA + bB$ are $aA_{ii} + bB_{ii}$. $\operatorname{Tr}(AB) = \operatorname{Tr}(BA)$ is Proposition [[§66 Invariant Vectors#^prop-66-1|§66.1]], and $E_{11}$ has the single diagonal entry $1$.
>
> **(2)** The matrix units multiply by the rule $E_{ij}E_{kl} = E_{il}$ if $j = k$, and $E_{ij}E_{kl} = 0$ if $j \neq k$: the $(a, b)$ entry of the product is $\sum_c (E_{ij})_{ac}(E_{kl})_{cb}$, and the only possibly nonzero summand has $a = i$, $c = j = k$, $b = l$.
>
> *Off-diagonal units.* For $i \neq j$, $E_{ii}E_{ij} = E_{ij}$ and $E_{ij}E_{ii} = 0$, so $E_{ij} = E_{ii}E_{ij} - E_{ij}E_{ii}$ and $f(E_{ij}) = 0$.
>
> *Diagonal units.* For $i \neq j$, $E_{ij}E_{ji} = E_{ii}$ and $E_{ji}E_{ij} = E_{jj}$, so $E_{ii} - E_{jj} = E_{ij}E_{ji} - E_{ji}E_{ij}$ and $f(E_{ii}) = f(E_{jj})$. Hence $f(E_{ii}) = f(E_{11}) = 1$ for every $i$.
>
> *Conclusion.* Every matrix is $A = \sum_{i,j} A_{ij}E_{ij}$, so by linearity $f(A) = \sum_{i,j} A_{ij}f(E_{ij}) = \sum_i A_{ii} = \operatorname{Tr}(A)$.
>
> **(3)** Let $Z$ be the span of all matrices $AB - BA$. By (1), every matrix in $Z$ has trace zero. Conversely, let $C$ be a matrix of trace zero. Then
>
> $$
> C = \sum_{i \neq j} C_{ij}E_{ij} + \sum_{i=2}^n C_{ii}\,(E_{ii} - E_{11}),
> $$
>
> because the coefficient of $E_{11}$ on the right is $-\sum_{i \geq 2} C_{ii}$, which equals $C_{11}$ since $\operatorname{Tr}(C) = 0$. By the two steps of (2), every $E_{ij}$ with $i \neq j$ and every $E_{ii} - E_{11}$ is of the form $AB - BA$. So $C \in Z$.
>
> *The dimension.* By the display, the $n^2 - n$ matrices $E_{ij}$ with $i \neq j$ and the $n - 1$ matrices $E_{ii} - E_{11}$ with $i \geq 2$ span the matrices of trace zero. They are linearly independent: in a linear combination of them, the coefficient of $E_{ij}$ ($i \neq j$) and the coefficient of $E_{ii} - E_{11}$ ($i \geq 2$) are the $(i, j)$ entry and the $(i, i)$ entry of the resulting matrix, so all coefficients are zero if the matrix is zero. Their number is $(n^2 - n) + (n - 1) = n^2 - 1$.

^pf-68-2

*Uses:* [[§66 Invariant Vectors#^prop-66-1|§66.1]]

> [!remark]- Connections
> - Linear Algebra: the trace is linear, [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-56|LADR 8.56]]; since it vanishes on every $ST - TS$, the identity is never of that form when $\dim V \neq 0$ in $k$, [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-57|LADR 8.57]].

> [!remark] Remark: Commutators in a Group and in a Ring
> The abelianization of a group sets every commutator $ghg^{-1}h^{-1}$ equal to the identity (Definition [[§47 Commutators#^def-47-3|§47.3]]); this forces the multiplication to be commutative. For matrices, where there is an addition as well as a multiplication, the corresponding step is to set every $AB - BA$ equal to zero, that is, to pass to the quotient of the vector space of $n \times n$ matrices by the span of all $AB - BA$. By Proposition [[§68 Homomorphisms Between Representations#^prop-68-2|§68.2]](3) this span has codimension one, and it is the kernel of the trace.
>
> The condition $\operatorname{Tr}(E_{11}) = 1$ is a normalization: every multiple $c \cdot \operatorname{Tr}$ also vanishes on all $AB - BA$. A second normalization with the same effect is that the trace of an idempotent is the dimension of its image (Proposition [[§66 Invariant Vectors#^prop-66-4|§66.4]]); $E_{11}$ is an idempotent with a one-dimensional image. The identity $\operatorname{Tr}(AB) = \operatorname{Tr}(BA)$ is the fundamental property of the trace: little can be done with the trace without it.
>
> *Source: lecture 11/11*

^rem-68-1

## The Representation $\operatorname{Hom}(V, W)$

> [!definition] Definition §68.1: The Representation $\operatorname{Hom}(V, W)$
> Let $V$ and $W$ be vector spaces over the same field $k$, and let $\operatorname{Hom}(V, W)$ be the vector space of linear maps $\alpha: V \to W$. If $V$ and $W$ are representations of a group $G$, set, for $g \in G$ and $\alpha \in \operatorname{Hom}(V, W)$,
>
> $$
> g \ast \alpha = \rho_W(g) \circ \alpha \circ \rho_V(g^{-1}).
> $$
>
> *Source: WS 16; lecture 11/11*

^def-68-1

If $V$ and $W$ are finite-dimensional, then in bases of $V$ and $W$ a linear map $\alpha: V \to W$ is a $(\dim W) \times (\dim V)$ matrix, so $\dim \operatorname{Hom}(V, W) = \dim V \cdot \dim W$ *(board 11/11)*. With $n = \dim V$ and $m = \dim W$, the rule $g \ast \alpha = \rho_W(g) \circ \alpha \circ \rho_V(g^{-1})$ is the product of an $m \times m$ matrix, an $m \times n$ matrix and an $n \times n$ matrix *(board 11/13)*.

**Transcription note.** Worksheet 16 prints $g \ast \alpha = \rho_V(g) \circ \alpha \circ \rho_W(g^{-1})$. For $\alpha: V \to W$ these maps cannot be composed unless $V = W$: $\rho_W(g^{-1})$ acts on $W$, but $\alpha$ is defined on $V$. With $V$ and $W$ exchanged, as in Definition [[§68 Homomorphisms Between Representations#^def-68-1|§68.1]], the composition makes sense, and the invariant maps are the $\alpha$ with $\alpha \circ \rho_V = \rho_W \circ \alpha$, as the worksheet says next and as the board of 11/11 has it. The exchange also affects WS 16.2 (Proposition [[§68 Homomorphisms Between Representations#^prop-68-5|§68.5]]) but not the worksheet's theorem (Theorem [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]]). The handwritten notes of 11/11 write $\operatorname{Hom}_G(V, W) = \{\alpha: U \to V \mid \ldots\}$; $\alpha: V \to W$ is meant.

> [!definition] Definition §68.2: $\operatorname{Hom}_G(V, W)$
> Let $V$ and $W$ be representations of $G$. The set of homomorphisms of $G$-representations $V \to W$ (Definition [[§61 Representations and Subrepresentations#^def-61-4|§61.4]]), that is, of linear maps $\alpha: V \to W$ with
>
> $$
> \alpha\big(\rho_V(g)(v)\big) = \rho_W(g)\big(\alpha(v)\big) \qquad \text{for all } g \in G \text{ and } v \in V,
> $$
>
> is written $\operatorname{Hom}_G(V, W)$.
>
> *Source: WS 16; board 11/11*

^def-68-2

![[m493-68-1.svg]]

*(Board 11/11.)* The condition of Definition [[§68 Homomorphisms Between Representations#^def-68-2|§68.2]]: for every $g \in G$ the square commutes, that is, applying $g$ and then $\alpha$ gives the same as applying $\alpha$ and then $g$.

> [!theorem] Proposition §68.3: $\operatorname{Hom}(V, W)$ Is a Representation; Its Invariants
> Let $V$ and $W$ be representations of $G$.
>
> 1. The rule of Definition [[§68 Homomorphisms Between Representations#^def-68-1|§68.1]] is an action of $G$ on $\operatorname{Hom}(V, W)$ by linear maps. So $\operatorname{Hom}(V, W)$ is a representation of $G$.
> 2. Its invariant vectors are exactly the homomorphisms of $G$-representations: $\operatorname{Hom}(V, W)^G = \operatorname{Hom}_G(V, W)$.
>
> *Source: WS 16.1; worksheet session 11/11*

^prop-68-3

> [!proof]+ Proof
> *Idea:* The action axioms hold because $\rho_V$ and $\rho_W$ are homomorphisms; and $g \ast \alpha = \alpha$ rearranges to $\rho_W(g) \circ \alpha = \alpha \circ \rho_V(g)$.
>
> *(Worksheet session 11/11.)* **(1)** Since $\rho_V(e) = \mathrm{id}_V$ and $\rho_W(e) = \mathrm{id}_W$, $e \ast \alpha = \mathrm{id}_W \circ \alpha \circ \mathrm{id}_V = \alpha$. Since $\rho_V$ and $\rho_W$ are homomorphisms (Proposition [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]]) and $(gh)^{-1} = h^{-1}g^{-1}$,
>
> $$
> (gh) \ast \alpha = \rho_W(g)\,\rho_W(h) \circ \alpha \circ \rho_V(h^{-1})\,\rho_V(g^{-1}) = g \ast (h \ast \alpha).
> $$
>
> Each map $\alpha \mapsto g \ast \alpha$ is linear, because composition is linear in the middle factor.
>
> **(2)** Since $\rho_V(g^{-1}) = \rho_V(g)^{-1}$, the equation $g \ast \alpha = \alpha$ reads $\rho_W(g) \circ \alpha \circ \rho_V(g)^{-1} = \alpha$. Composing on the right with $\rho_V(g)$, it is equivalent to $\rho_W(g) \circ \alpha = \alpha \circ \rho_V(g)$. This holds for all $g \in G$ exactly when $\alpha \in \operatorname{Hom}_G(V, W)$ (Definition [[§68 Homomorphisms Between Representations#^def-68-2|§68.2]]).

^pf-68-3

*Uses:* [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]], [[§68 Homomorphisms Between Representations#^def-68-2|Def. §68.2]]

Written as $(g \cdot A)(w) = g\,A(g^{-1}w)$, this is Proposition [[§66 Invariant Vectors#^prop-66-9|§66.9]](1) and (2), with $V$, $W$ in place of $W$, $W'$. In particular $\operatorname{Hom}_G(V, W)$ is a subspace of $\operatorname{Hom}(V, W)$ (Lemma [[§66 Invariant Vectors#^lem-66-5|§66.5]]).

> [!remark] Remark: The Side of the Inverse
> In $g \ast \alpha = \rho_W(g) \circ \alpha \circ \rho_V(g^{-1})$ the factor without an inverse has to be the one on the left, for the rule to be a left action: in the computation of $(gh) \ast \alpha$ in the proof of Proposition [[§68 Homomorphisms Between Representations#^prop-68-3|§68.3]](1), the factors on the left appear in the order $\rho_W(g)\,\rho_W(h)$, and the inverses restore this order on the right. That the factor on the left belongs to $W$ and not to $V$ is a consequence of the convention of writing a function to the left of its argument, $\alpha(v)$: the map that is applied last is written first.
>
> More generally, if $G$ acts on $V$ and a second group $H$ acts on $W$, then $G \times H$ acts on $\operatorname{Hom}(V, W)$. This was announced as a homework problem and is not written out here. The inverse on the side of $V$ is explained by the dual representation ([[§69 Dual Representations|§69]]).
>
> *Source: lecture 11/13*

^rem-68-2

## The Character of $\operatorname{Hom}(V, W)$ and the Dimension Formula

> [!theorem] Lemma §68.4: The Trace of $X \mapsto RXS$
> Let $R$ be an $m \times m$ matrix and $S$ an $n \times n$ matrix over $k$, and let
>
> $$
> L(X) = RXS
> $$
>
> on the space of $m \times n$ matrices $X$ over $k$. Then $L$ is linear, and $\operatorname{Tr}(L) = \operatorname{Tr}(R)\operatorname{Tr}(S)$.
>
> *Source: WS 16.2, the computation; board 11/11*

^lem-68-4

> [!proof]+ Proof
> *Idea:* With the entries of $X$ as coordinates, the matrix of $L$ has the entry $R_{i'i}S_{jj'}$ in row $(i', j')$ and column $(i, j)$; its diagonal entries $R_{ii}S_{jj}$ add up to a product of two sums.
>
> *(Board 11/11, following the worksheet's hint to name the matrices.)* $L$ is linear, because the matrix product is linear in the middle factor. The entries of $RXS$ are
>
> $$
> (RXS)_{i'j'} = \sum_{i=1}^m \sum_{j=1}^n R_{i'i}\,X_{ij}\,S_{jj'}.
> $$
>
> A basis of the $m \times n$ matrices is given by the matrix units $E_{ij}$, $1 \leq i \leq m$, $1 \leq j \leq n$ (the entry $1$ in position $(i, j)$ and $0$ elsewhere). Since $X = \sum_{i,j} X_{ij}E_{ij}$, the coordinates of $X$ in this basis are its $mn$ entries, written as a column $X_{11}, X_{12}, \ldots, X_{mn}$. In these coordinates the displayed formula says that the matrix of $L$, an $mn \times mn$ matrix, has the entry
>
> $$
> R_{i'i}\,S_{jj'} \qquad \text{in row (output) } (i', j') \text{ and column (input) } (i, j).
> $$
>
> A check by counting: $R$ has $m^2$ entries and $S$ has $n^2$, so there are $m^2n^2$ products $R_{i'i}S_{jj'}$; an $mn \times mn$ matrix has $m^2n^2$ entries, one place for each product. The diagonal entries of this matrix are those with $(i', j') = (i, j)$, namely $R_{ii}S_{jj}$. The trace of $L$ is their sum (Definition [[§66 Invariant Vectors#^def-66-2|§66.2]]):
>
> $$
> \operatorname{Tr}(L) = \sum_{i=1}^m \sum_{j=1}^n R_{ii}S_{jj} = \Big(\sum_{i=1}^m R_{ii}\Big)\Big(\sum_{j=1}^n S_{jj}\Big) = \operatorname{Tr}(R)\operatorname{Tr}(S).
> $$

^pf-68-4

*Uses:* [[§66 Invariant Vectors#^def-66-2|Def. §66.2]]

> [!example] Example §68.1: The Case $m = 2$ and $n = 3$
> The board's example:
>
> $$
> \begin{pmatrix} R_{11} & R_{12} \\ R_{21} & R_{22} \end{pmatrix} \begin{pmatrix} X_{11} & X_{12} & X_{13} \\ X_{21} & X_{22} & X_{23} \end{pmatrix} \begin{pmatrix} S_{11} & S_{12} & S_{13} \\ S_{21} & S_{22} & S_{23} \\ S_{31} & S_{32} & S_{33} \end{pmatrix}.
> $$
>
> With $X$ written as the column $(X_{11}, X_{12}, X_{13}, X_{21}, X_{22}, X_{23})$, the map $X \mapsto RXS$ is a $6 \times 6$ matrix. Its first row gives the entry $(RXS)_{11}$:
>
> $$
> (RXS)_{11} = R_{11}S_{11}X_{11} + R_{11}S_{21}X_{12} + R_{11}S_{31}X_{13} + R_{12}S_{11}X_{21} + R_{12}S_{21}X_{22} + R_{12}S_{31}X_{23}.
> $$
>
> The six diagonal entries are $R_{11}S_{11}$, $R_{11}S_{22}$, $R_{11}S_{33}$, $R_{22}S_{11}$, $R_{22}S_{22}$, $R_{22}S_{33}$, with sum $(R_{11} + R_{22})(S_{11} + S_{22} + S_{33})$.
>
> *Source: board 11/11*

^ex-68-1

![[m493-68-2.svg]]

*(Not from lecture; figure added. The board wrote the first row.)* The whole $6 \times 6$ matrix of $X \mapsto RXS$ in Example [[§68 Homomorphisms Between Representations#^ex-68-1|§68.1]]. Columns are indexed by the entries of $X$ (inputs), rows by the entries of $RXS$ (outputs). The matrix consists of four $3 \times 3$ blocks $R_{i'i}\,S^T$, one for each entry of $R$. The diagonal entries (red) are the products $R_{ii}S_{jj}$.

> [!remark] Remark: Matrices of Compositions
> The bookkeeping in Lemma [[§68 Homomorphisms Between Representations#^lem-68-4|§68.4]] uses the convention that the matrix of a linear map has one row for each output coordinate and one column for each input coordinate. The rows and columns need not be numbered $1, 2, \ldots$: they can be indexed by any finite sets. For finite sets $I$, $J$, $K$ and linear maps $\mathbb{R}^I \xrightarrow{A} \mathbb{R}^J \xrightarrow{B} \mathbb{R}^K$ the composite has the entries
>
> $$
> (B \circ A)_{ki} = \sum_{j \in J} B_{kj}A_{ji} \qquad (k \in K,\ i \in I),
> $$
>
> a sum over the index in the middle. The entry formula for $RXS$ is this rule applied twice.
>
> This answers the question, asked in the lecture, how the entries of $X$ should be arranged into a column. No arrangement is needed: the coordinates of $X$ are indexed by the set of pairs $(i, j)$. The trace of a linear map $\mathbb{R}^I \to \mathbb{R}^I$ with matrix $A$ is $\sum_{i \in I} A_{ii}$, the sum over $i$ of the coefficient with which the $i$-th coordinate of the input enters the $i$-th coordinate of the output. It does not depend on the order in which the elements of $I$ are listed. In Example [[§68 Homomorphisms Between Representations#^ex-68-1|§68.1]] the entries are listed row by row only in order to write down a $6 \times 6$ matrix.
>
> *Source: lecture 11/11*

^rem-68-3

> [!remark] Remark: The Summation Convention
> In the notation of physics the summation signs are omitted: an index that occurs twice in a product is summed over. The three formulas of this subsection become
>
> $$
> (B \circ A)_{ki} = B_{kj}A_{ji}, \qquad (RXS)_{i'j'} = R_{i'i}X_{ij}S_{jj'}, \qquad \operatorname{Tr}(X \mapsto RXS) = R_{ii}S_{jj}.
> $$
>
> The notation gives a check of index computations: every index that is summed occurs exactly twice, and the remaining indices are the same on both sides of an equation.
>
> *Source: lecture 11/11*

^rem-68-4

> [!remark]- Connections
> - Relativity: the convention with upper and lower indices, where a summed index occurs once upstairs and once downstairs, is [[§B1.1 The Metric and Index Notation#^def-b1-1-2|Relativity Def. §B1.1.2]]. Here all indices are written downstairs.

> [!theorem] Proposition §68.5: The Character of $\operatorname{Hom}(V, W)$
> Let $V$ and $W$ be finite-dimensional representations of $G$ over $k$. Then for every $g \in G$
>
> $$
> \chi_{\operatorname{Hom}(V, W)}(g) = \operatorname{Tr}\rho_{\operatorname{Hom}(V, W)}(g) = \big(\operatorname{Tr}\rho_W(g)\big)\big(\operatorname{Tr}\rho_V(g^{-1})\big) = \chi_W(g)\,\chi_V(g^{-1}).
> $$
>
> *Source: WS 16.2, with $V$ and $W$ exchanged (see the transcription note above); board 11/11*

^prop-68-5

> [!proof]+ Proof
> *(Board 11/11.)* Choose a basis of $V$ and a basis of $W$, and let $n = \dim V$, $m = \dim W$. Then a linear map $\alpha: V \to W$ is an $m \times n$ matrix $X$, and composition of maps is the product of matrices (the remark *Matrices of Compositions*). So $g \ast \alpha = \rho_W(g) \circ \alpha \circ \rho_V(g^{-1})$ is the matrix $RXS$, with $R$ the matrix of $\rho_W(g)$ and $S$ the matrix of $\rho_V(g^{-1})$. By Lemma [[§68 Homomorphisms Between Representations#^lem-68-4|§68.4]], the trace of $\alpha \mapsto g \ast \alpha$ is $\operatorname{Tr}(R)\operatorname{Tr}(S) = \chi_W(g)\,\chi_V(g^{-1})$ (Definition [[§67 Characters of Representations#^def-67-1|§67.1]]).

^pf-68-5

*Uses:* [[§68 Homomorphisms Between Representations#^lem-68-4|§68.4]], [[§67 Characters of Representations#^def-67-1|Def. §67.1]]

Worksheet 16.2 prints $\operatorname{Tr}\rho_{\operatorname{Hom}(V, W)}(g) = (\operatorname{Tr}\rho_V(g))(\operatorname{Tr}\rho_W(g^{-1}))$, which is the formula for the action as the worksheet prints it. The two versions differ by replacing $g$ with $g^{-1}$, and they have the same sum over $G$. So the theorem holds as printed.

> [!theorem] Theorem §68.6: Dimension of $\operatorname{Hom}_G(V, W)$
> Let $k$ be a field containing $\mathbb{Q}$, let $G$ be a finite group, and let $V$ and $W$ be finite-dimensional representations of $G$ over $k$, with characters $\chi_V$ and $\chi_W$. Then
>
> $$
> \dim \operatorname{Hom}_G(V, W) = \frac{1}{|G|}\sum_{g \in G} \chi_V(g^{-1})\,\chi_W(g) = \frac{1}{|G|}\sum_{g \in G} \chi_V(g)\,\chi_W(g^{-1}).
> $$
>
> The first form is the board's, the second the worksheet's.
>
> *Source: WS 16, theorem; lecture 11/11*

^thm-68-6

> [!proof]+ Proof
> *Idea:* $\operatorname{Hom}_G(V, W)$ is the space of invariant vectors of $\operatorname{Hom}(V, W)$, whose dimension is the average of the character of $\operatorname{Hom}(V, W)$.
>
> *(Lecture 11/11; the last step written out.)* $\operatorname{Hom}(V, W)$ is a representation of $G$ of finite dimension $\dim V \cdot \dim W$, and $\operatorname{Hom}_G(V, W) = \operatorname{Hom}(V, W)^G$ (WS 16.1, Proposition [[§68 Homomorphisms Between Representations#^prop-68-3|§68.3]]). By Dimension of the Invariants (WS 15.6, Theorem [[§66 Invariant Vectors#^thm-66-10|§66.10]]) and WS 16.2 (Proposition [[§68 Homomorphisms Between Representations#^prop-68-5|§68.5]]),
>
> $$
> \dim \operatorname{Hom}_G(V, W) = \frac{1}{|G|}\sum_{g \in G} \chi_{\operatorname{Hom}(V, W)}(g) = \frac{1}{|G|}\sum_{g \in G} \chi_W(g)\,\chi_V(g^{-1}),
> $$
>
> which is the first form. Inversion $g \mapsto g^{-1}$ is a bijection of $G$, so the sum does not change when $g$ is replaced by $g^{-1}$ in every term; this gives the second form.

^pf-68-6

*Uses:* [[§68 Homomorphisms Between Representations#^prop-68-3|§68.3]], [[§66 Invariant Vectors#^thm-66-10|§66.10]], [[§68 Homomorphisms Between Representations#^prop-68-5|§68.5]]

> [!theorem] Corollary §68.7: Homomorphisms in Both Directions
> In the setting of Theorem [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]], $\dim \operatorname{Hom}_G(V, W) = \dim \operatorname{Hom}_G(W, V)$.
>
> *Source: not from class*

^cor-68-7

> [!proof]+ Proof
> *(Not from class.)* By the first form of Theorem [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]] for the pair $(W, V)$, $\dim \operatorname{Hom}_G(W, V) = \frac{1}{|G|}\sum_{g} \chi_W(g^{-1})\,\chi_V(g)$. This is the second form of $\dim \operatorname{Hom}_G(V, W)$.

^pf-68-7

*Uses:* [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]]

> [!example] Example §68.2: $\operatorname{Hom}_G$ for $S_3$
> *(Not from class.)* Over $\mathbb{R}$, take the characters of $S_3$ from Example [[§67 Characters of Representations#^ex-67-1|§67.1]], as values on the classes of $e$, $(1\,2)$, $(1\,2\,3)$, of sizes $1$, $3$, $2$: trivial $(1, 1, 1)$, sign $(1, -1, 1)$, $U = (1,1,1)^\perp$ with $(2, 0, -1)$, and $\mathbb{R}^3$ with $(3, 1, 0)$. In $S_3$ the inverse $g^{-1}$ has the same [[§33 Conjugacy Classes#^def-33-2|cycle type]] as $g$, so it is conjugate to $g$ (Theorem [[§33 Conjugacy Classes#^thm-33-3|§33.3]]), and $\chi(g^{-1}) = \chi(g)$ for every character (Proposition [[§67 Characters of Representations#^prop-67-1|§67.1]](2)). A sum over $G$ of a function that is constant on [[§33 Conjugacy Classes#^def-33-1|conjugacy classes]] is the sum over the classes of (class size) $\times$ (value). So Theorem [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]] gives $\dim\operatorname{Hom}_{S_3}(V, W) = \frac16\big(\chi_V(e)\chi_W(e) + 3\,\chi_V((1\,2))\chi_W((1\,2)) + 2\,\chi_V((1\,2\,3))\chi_W((1\,2\,3))\big)$:
>
> | $\dim\operatorname{Hom}_{S_3}(V, W)$ | triv | sign | $U$ | $\mathbb{R}^3$ |
> |---|---|---|---|---|
> | triv | $1$ | $0$ | $0$ | $1$ |
> | sign | $0$ | $1$ | $0$ | $0$ |
> | $U$ | $0$ | $0$ | $1$ | $1$ |
> | $\mathbb{R}^3$ | $1$ | $0$ | $1$ | $2$ |
>
> 1. $\dim \operatorname{Hom}_{S_3}(U, U) = \frac16(2 \cdot 2 + 3 \cdot 0 \cdot 0 + 2 \cdot (-1)(-1)) = 1$. The homomorphisms $U \to U$ are the multiples of the identity.
> 2. $\dim \operatorname{Hom}_{S_3}(\mathrm{triv}, U) = \frac16(1 \cdot 2 + 3 \cdot 1 \cdot 0 + 2 \cdot 1 \cdot (-1)) = 0$, and $\dim \operatorname{Hom}_{S_3}(\mathrm{triv}, \mathrm{sign}) = \frac16(1 - 3 + 2) = 0$: the only homomorphism is $0$.
> 3. $\dim \operatorname{Hom}_{S_3}(\mathbb{R}^3, \mathbb{R}^3) = \frac16(3 \cdot 3 + 3 \cdot 1 \cdot 1 + 2 \cdot 0 \cdot 0) = 2$. Two independent homomorphisms are the identity and the averaging operator $\pi$ of Example [[§66 Invariant Vectors#^ex-66-4|§66.4]], whose matrix is $\frac13$ times the all-ones matrix; $\pi$ commutes with every $\rho(g)$ (the proof of Corollary [[§66 Invariant Vectors#^cor-66-8|§66.8]]) and is not a multiple of the identity.
> 4. The row of $\mathbb{R}^3$ is the sum of the rows of triv and $U$, because $\chi_{\mathbb{R}^3} = \chi_{\mathrm{triv}} + \chi_U$ (Proposition [[§67 Characters of Representations#^prop-67-2|§67.2]]) and the formula is additive in $\chi_V$.
>
> *Source: not from class; the table checked by computer*

^ex-68-2

## Characters at $g^{-1}$ over $\mathbb{R}$ and $\mathbb{C}$

The formula of Theorem [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]] simplifies when the field is $\mathbb{R}$ or $\mathbb{C}$. Worksheet 16.3–16.5 were not reached in class. The lecture of 11/13 recalled the statements of WS 16.3 and WS 16.5 (for a finite group, $\chi(g^{-1}) = \chi(g)$ over $\mathbb{R}$ and $\chi(g^{-1}) = \overline{\chi(g)}$ over $\mathbb{C}$) without proof; the proofs in this subsection are filled in. In terms of the dual representation, the two statements say $\chi_{V^\vee} = \chi_V$ and $\chi_{V^\vee} = \overline{\chi_V}$ (Corollary [[§69 Dual Representations#^cor-69-6|§69.6]]).

> [!theorem] Proposition §68.8: Real Characters Are Invariant under Inversion
> Let $G$ be a finite group and $V$ a finite-dimensional representation of $G$ over $\mathbb{R}$. Choose a basis of $V$ in which $G$ acts by orthogonal matrices (Corollary [[§63 Invariant Inner Products and Maschke over ℝ#^cor-63-7|§63.7]]). In this basis, for every $g \in G$,
>
> $$
> \rho_V(g^{-1}) = \rho_V(g)^{-1} = \rho_V(g)^T.
> $$
>
> Consequently $\chi_V(g^{-1}) = \chi_V(g)$ for every $g \in G$.
>
> *Source: WS 16.3*

^prop-68-8

> [!proof]+ Proof
> *(Filled in.)* *Why such a basis exists.* This is Finite Groups Act by Orthogonal Matrices (Corollary [[§63 Invariant Inner Products and Maschke over ℝ#^cor-63-7|§63.7]]): $G$ preserves the averaged inner product (Proposition [[§63 Invariant Inner Products and Maschke over ℝ#^prop-63-5|§63.5]]), and in a basis that is orthonormal for it every $\rho_V(g)$ is an orthogonal matrix.
>
> *The two equalities.* Since $\rho_V$ is a homomorphism (Proposition [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]]), $\rho_V(g^{-1})\rho_V(g) = \rho_V(e) = I$, so $\rho_V(g^{-1}) = \rho_V(g)^{-1}$. Write $M = \rho_V(g)$. It is orthogonal, $M^TM = I$, so $M^{-1} = M^T$.
>
> *The characters.* A matrix and its transpose have the same diagonal entries, so $\operatorname{Tr}(M^T) = \operatorname{Tr}(M)$ (Definition [[§66 Invariant Vectors#^def-66-1|§66.1]]). The trace of a linear map does not depend on the basis (Corollary [[§66 Invariant Vectors#^cor-66-2|§66.2]]), so it may be computed in this basis:
>
> $$
> \chi_V(g^{-1}) = \operatorname{Tr}\rho_V(g^{-1}) = \operatorname{Tr}(M^T) = \operatorname{Tr}(M) = \chi_V(g).
> $$

^pf-68-8

*Uses:* [[§63 Invariant Inner Products and Maschke over ℝ#^cor-63-7|§63.7]], [[§63 Invariant Inner Products and Maschke over ℝ#^prop-63-5|§63.5]], [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]], [[§66 Invariant Vectors#^def-66-1|Def. §66.1]], [[§66 Invariant Vectors#^cor-66-2|§66.2]]

> [!theorem] Proposition §68.9: Matrices of Finite Order
> Let $A$ be an $n \times n$ complex matrix with $A^m = I$ for some positive integer $m$.
>
> 1. $A$ is diagonalizable, and every eigenvalue $\lambda$ of $A$ satisfies $\lambda^m = 1$; in particular $|\lambda| = 1$.
> 2. $\operatorname{Tr}(A^{-1}) = \overline{\operatorname{Tr}(A)}$.
>
> *Source: WS 16.4*

^prop-68-9

> [!proof]+ Proof
> *Idea:* $A$ generates a representation of the finite group $\mathbb{Z}/m\mathbb{Z}$ on $\mathbb{C}^n$; Maschke's theorem splits off one eigenvector at a time. On the unit circle, $\lambda^{-1} = \bar\lambda$.
>
> *(Filled in; the worksheet's hint for (2) is to use the eigenvalues.)* $A$ is invertible, with inverse $A^{m-1}$.
>
> **(1) Eigenvalues.** Let $Av = \lambda v$ with $v \neq 0$. Then $v = A^mv = \lambda^m v$, so $\lambda^m = 1$. Taking absolute values, $|\lambda|^m = 1$, and $|\lambda|$ is a nonnegative real number, so $|\lambda| = 1$.
>
> **(1) Diagonalizable.** We show by induction on $\dim U$ that every subspace $U \subseteq \mathbb{C}^n$ with $AU \subseteq U$ has a basis of eigenvectors of $A$; the case $U = \mathbb{C}^n$ is the claim. If $U = \{0\}$ there is nothing to show. Let $U \neq \{0\}$. The rule $j \mapsto (A|_U)^j$ is well defined on $j \bmod m$, because $A^m = I$, and it is a homomorphism $\mathbb{Z}/m\mathbb{Z} \to GL(U)$. So $U$ is a representation of the finite group $\mathbb{Z}/m\mathbb{Z}$ over $\mathbb{C}$ (Proposition [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]]), and its subrepresentations are the subspaces $U' \subseteq U$ with $AU' \subseteq U'$ (such a subspace is preserved by every power of $A$). A linear map from a nonzero finite-dimensional complex vector space to itself has an eigenvector (Axler, Ch. 5); let $v \in U$ be an eigenvector of $A|_U$. The line $\mathbb{C}v$ is a subrepresentation. Since $|\mathbb{Z}/m\mathbb{Z}| = m \neq 0$ in $\mathbb{C}$, Maschke's theorem (Theorem [[§62 Direct Sums and Maschke's Theorem#^thm-62-10|§62.10]]) gives a subrepresentation $U'$ with $U = \mathbb{C}v \oplus U'$. Then $AU' \subseteq U'$ and $\dim U' = \dim U - 1$, so by induction $U'$ has a basis of eigenvectors of $A$. Together with $v$ it is a basis of $U$ (Bases of a Direct Sum, Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-1|§62.1]]).
>
> **(2)** By (1) there is an invertible matrix $P$ with $A = PDP^{-1}$, $D = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$, where the $\lambda_i$ are the eigenvalues of $A$ with multiplicity. Then $A^{-1} = PD^{-1}P^{-1}$ with $D^{-1} = \operatorname{diag}(\lambda_1^{-1}, \ldots, \lambda_n^{-1})$. Since $|\lambda_i| = 1$, $\lambda_i\overline{\lambda_i} = |\lambda_i|^2 = 1$, so $\lambda_i^{-1} = \overline{\lambda_i}$. By The Trace of a Diagonalizable Matrix (Proposition [[§66 Invariant Vectors#^prop-66-3|§66.3]], PS 8.5(3)), applied to $A^{-1}$ and to $A$,
>
> $$
> \operatorname{Tr}(A^{-1}) = \sum_{i=1}^n \lambda_i^{-1} = \sum_{i=1}^n \overline{\lambda_i} = \overline{\sum_{i=1}^n \lambda_i} = \overline{\operatorname{Tr}(A)}.
> $$

^pf-68-9

*Uses:* [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]], [[§62 Direct Sums and Maschke's Theorem#^thm-62-10|§62.10]], [[§62 Direct Sums and Maschke's Theorem#^prop-62-1|§62.1]], [[§66 Invariant Vectors#^prop-66-3|§66.3]]

> [!remark]- Connections
> - Linear Algebra: an operator on a nonzero finite-dimensional complex vector space has an eigenvalue (Axler, Ch. 5). A second route to (1): the [[§15 The Minimal Polynomial#^ladr-5-24|minimal polynomial]] of $A$ divides $x^m - 1$, which has $m$ distinct roots, and an operator whose minimal polynomial has distinct roots is diagonalizable.

![[m493-66-1.svg]]

*(Not from lecture; figure added.)* Proposition [[§68 Homomorphisms Between Representations#^prop-68-9|§68.9]] for $A = \operatorname{diag}(\lambda_1, \lambda_2)$ with $\lambda_1 = e^{2\pi i/6}$ and $\lambda_2 = e^{2\pi i \cdot 2/6}$, so that $A^6 = I$. The eigenvalues of a matrix with $A^6 = I$ are among the six marked points of the unit circle. Inverting a point of the unit circle reflects it in the real axis (dashed), which is complex conjugation. So the eigenvalues of $A^{-1}$ (red) are the conjugates of those of $A$ (blue), and the two traces are conjugate: $i\sqrt{3}$ and $-i\sqrt{3}$.

> [!theorem] Corollary §68.10: Complex Characters under Inversion
> Let $G$ be a finite group and $V$ a finite-dimensional complex representation of $G$. Then for every $g \in G$
>
> $$
> \chi_V(g^{-1}) = \overline{\chi_V(g)}.
> $$
>
> *Source: WS 16.5*

^cor-68-10

> [!proof]+ Proof
> *(Filled in.)* Choose a basis of $V$ and let $A$ be the matrix of $\rho_V(g)$ in it. Let $m = |G|$. Then $g^m = e$ (Corollary [[§29 The Index and Lagrange's Theorem#^cor-29-3|§29.3]]), so $A^m$ is the matrix of $\rho_V(g)^m = \rho_V(g^m) = \rho_V(e)$, the identity matrix. The matrix of $\rho_V(g^{-1}) = \rho_V(g)^{-1}$ is $A^{-1}$. By Proposition [[§68 Homomorphisms Between Representations#^prop-68-9|§68.9]](2),
>
> $$
> \chi_V(g^{-1}) = \operatorname{Tr}(A^{-1}) = \overline{\operatorname{Tr}(A)} = \overline{\chi_V(g)}.
> $$

^pf-68-10

*Uses:* [[§29 The Index and Lagrange's Theorem#^cor-29-3|§29.3]], [[§68 Homomorphisms Between Representations#^prop-68-9|§68.9]]

> [!proof]+ Second proof (unitary matrices; outline)
> *(The route Worksheet 16 mentions for readers who know sesquilinear forms. It rests on the statement in the remark *Why Not Bilinear, and Unitary Matrices* in [[§64 Sesquilinear and Hermitian Forms|§64]], whose averaging argument is not written out in these notes.)* A finite group acting on a finite-dimensional complex vector space preserves a positive definite Hermitian form, and in a basis that is orthonormal for it (Proposition [[§64 Sesquilinear and Hermitian Forms#^prop-64-4|§64.4]]) every $M = \rho_V(g)$ is unitary, $M^\dagger M = I$ (Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-4|§64.4]]). As in the proof of Proposition [[§68 Homomorphisms Between Representations#^prop-68-8|§68.8]], $\rho_V(g^{-1}) = M^{-1} = M^\dagger$. The diagonal entries of $M^\dagger = \bar M^T$ are the conjugates of those of $M$, so $\chi_V(g^{-1}) = \operatorname{Tr}(M^\dagger) = \overline{\operatorname{Tr}(M)} = \overline{\chi_V(g)}$.

^pf-68-10-2

*Uses:* [[§64 Sesquilinear and Hermitian Forms#^prop-64-4|§64.4]], [[§64 Sesquilinear and Hermitian Forms#^def-64-4|Def. §64.4]], [[§68 Homomorphisms Between Representations#^prop-68-8|§68.8]]

> [!theorem] Corollary §68.11: Dimension of $\operatorname{Hom}_G(V, W)$ over $\mathbb{R}$ and $\mathbb{C}$
> Let $G$ be a finite group and let $V$, $W$ be finite-dimensional representations of $G$ over $k$.
>
> 1. If $k = \mathbb{R}$, then $\dim \operatorname{Hom}_G(V, W) = \dfrac{1}{|G|}\displaystyle\sum_{g \in G} \chi_V(g)\,\chi_W(g)$.
> 2. If $k = \mathbb{C}$, then $\dim \operatorname{Hom}_G(V, W) = \dfrac{1}{|G|}\displaystyle\sum_{g \in G} \chi_V(g)\,\overline{\chi_W(g)}$.
>
> *Source: WS 16: the simplification announced before WS 16.3; the two formulas are not printed on the worksheet*

^cor-68-11

> [!proof]+ Proof
> *(Filled in.)* Both fields contain $\mathbb{Q}$, so Theorem [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]] applies. Substitute $\chi_W(g^{-1}) = \chi_W(g)$ over $\mathbb{R}$ (Proposition [[§68 Homomorphisms Between Representations#^prop-68-8|§68.8]]) and $\chi_W(g^{-1}) = \overline{\chi_W(g)}$ over $\mathbb{C}$ (Corollary [[§68 Homomorphisms Between Representations#^cor-68-10|§68.10]]).

^pf-68-11

*Uses:* [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]], [[§68 Homomorphisms Between Representations#^prop-68-8|§68.8]], [[§68 Homomorphisms Between Representations#^cor-68-10|§68.10]]
