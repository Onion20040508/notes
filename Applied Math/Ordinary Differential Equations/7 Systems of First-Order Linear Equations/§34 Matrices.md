---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 7
section: 34
bdp: "7.2"
aliases: ["BDP 7.2"]
tags: [ordinary-differential-equations, math331]
---
← [[§33 Introduction to Systems of First-Order Linear Equations]] · ↑ [[· 7 Systems of First-Order Linear Equations]] · [[§35 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors]] →

*Boyce–DiPrima, Section 7.2.*

To write the linear system (14) of [[§33 Introduction to Systems of First-Order Linear Equations#^def-33-5|Definition §33.5]] as one equation $\mathbf{x}' = \mathbf{P}(t)\mathbf{x} + \mathbf{g}(t)$, Chapter 7 uses matrix algebra. This section is BDP's summary of it; the concepts have their home in [[Applied Linear Algebra]] (Lay) and [[Linear Algebra]] (Axler), linked from each box. Two things go beyond a first linear algebra course and are what Chapter 7 needs most: entries may be **complex**, with the conjugate $\overline{\mathbf{A}}$, the adjoint $\mathbf{A}^{\ast}$ and the inner product $(\mathbf{x}, \mathbf{y}) = \sum x_i\overline{y_i}$; and entries may be **functions of $t$**, which are differentiated and integrated entry by entry.

## Matrices, Conjugates and Adjoints

> [!definition] Definition §40.1: Matrix
> Matrices are denoted by boldface capitals $\mathbf{A}, \mathbf{B}, \ldots$ (occasionally Greek: $\mathbf{\Phi}, \mathbf{\Psi}$). An $m \times n$ **matrix** is a rectangular array of $m$ rows and $n$ columns,
>
> $$
> \mathbf{A} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix} = (a_{ij}), \qquad (1)
> $$
>
> whose elements $a_{ij}$ (row $i$, column $j$) may be **complex numbers**.
>
> A **square matrix** has $m = n$ and is said to be of **order** $n$. A (column) **vector** is an $n \times 1$ matrix, denoted by boldface lowercase $\mathbf{x}, \mathbf{y}, \boldsymbol{\xi}, \boldsymbol{\eta}, \ldots$; its transpose $\mathbf{x}^T$ is a $1 \times n$ row vector.
>
> *BDP: 7.2 (text), Equation (1)*

^def-34-1

> [!definition] Definition §40.2: Transpose, Conjugate and Adjoint
> For a matrix $\mathbf{A} = (a_{ij})$ as in (1):
> - The **transpose** of $\mathbf{A} = (a_{ij})$ is $\mathbf{A}^T = (a_{ji})$: rows and columns interchanged.
> - The **conjugate** of $\mathbf{A}$ is $\overline{\mathbf{A}} = (\overline{a_{ij}})$: every element replaced by its complex conjugate.
> - The **adjoint** of $\mathbf{A}$ is the transpose of the conjugate, $\mathbf{A}^{\ast} = \overline{\mathbf{A}}^T$.
>
> For example,
>
> $$
> \mathbf{A} = \begin{pmatrix} 3 & 2 - i \\ 4 + 3i & -5 + 2i \end{pmatrix}:\quad
> \mathbf{A}^T = \begin{pmatrix} 3 & 4 + 3i \\ 2 - i & -5 + 2i \end{pmatrix},\quad
> \overline{\mathbf{A}} = \begin{pmatrix} 3 & 2 + i \\ 4 - 3i & -5 - 2i \end{pmatrix},\quad
> \mathbf{A}^* = \begin{pmatrix} 3 & 4 - 3i \\ 2 + i & -5 - 2i \end{pmatrix}.
> $$
>
> *BDP: 7.2 (text), Equation (1)*

^def-34-2

> [!remark]- Connections
> - Real matrices and the transpose: [[§12 Matrix Operations#^def-12-1|235 Def. §12.1]], [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^def-13-3|235 Def. §13.3]]. Conjugates of complex vectors and matrices: [[§44 Complex Eigenvalues#^def-44-2|235 Def. §44.2]], with the rules $\overline{\mathbf{A}\mathbf{x}} = \overline{\mathbf{A}}\,\overline{\mathbf{x}}$ in [[§44 Complex Eigenvalues#^prop-44-1|235 Prop. §44.1]].
> - BDP's adjoint is Axler's conjugate transpose [[§23 Self-Adjoint and Normal Operators#^ladr-7-7|LADR 7.7]]. The name fits: $\mathbf{A}^*$ is the matrix of the adjoint operator $T^*$ in orthonormal bases ([[§23 Self-Adjoint and Normal Operators#^ladr-7-9|LADR 7.9]]), the operator with $(\mathbf{A}\mathbf{x}, \mathbf{y}) = (\mathbf{x}, \mathbf{A}^*\mathbf{y})$ ([[§23 Self-Adjoint and Normal Operators#^ladr-7-1|LADR 7.1]]).

## Properties of Matrices

> [!definition] Definition §40.3: The Operations of Matrix Algebra
> 1. **Equality.** $m \times n$ matrices $\mathbf{A}$ and $\mathbf{B}$ are equal if $a_{ij} = b_{ij}$ for all $i$ and $j$.
> 2. **Zero.** $\mathbf{0}$ is the matrix (or vector) all of whose elements are zero.
> 3. **Addition.** $\mathbf{A} + \mathbf{B} = (a_{ij} + b_{ij})$ for $m \times n$ matrices. $\qquad (2)$
> 4. **Multiplication by a number.** $\alpha\mathbf{A} = (\alpha a_{ij})$ for a real or complex number $\alpha$; $-\mathbf{A} = (-1)\mathbf{A}$. $\qquad (4), (6)$
> 5. **Subtraction.** $\mathbf{A} - \mathbf{B} = \mathbf{A} + (-\mathbf{B}) = (a_{ij} - b_{ij})$. $\qquad (7), (8)$
> 6. **Multiplication.** If $\mathbf{A}$ is $m \times n$ and $\mathbf{B}$ is $n \times r$ (columns of the first factor = rows of the second), then $\mathbf{C} = \mathbf{AB}$ is the $m \times r$ matrix with
>
> $$
> c_{ij} = \sum_{k=1}^n a_{ik}b_{kj} : \qquad (9)
> $$
>
> the elements of row $i$ of $\mathbf{A}$ times the corresponding elements of column $j$ of $\mathbf{B}$, added.
> 7. **Identity.** The $n \times n$ identity matrix $\mathbf{I}$ has $1$ on the main diagonal and $0$ elsewhere. $\qquad (20)$
>
> *BDP: 7.2 (text), Equations (2), (4), (6)–(9), (20)*

^def-34-3

> [!theorem] Proposition §40.1: Laws of Matrix Algebra
> For matrices of sizes for which the operations are defined, and numbers $\alpha$, $\beta$:
>
> $$
> \mathbf{A} + \mathbf{B} = \mathbf{B} + \mathbf{A}, \quad \mathbf{A} + (\mathbf{B} + \mathbf{C}) = (\mathbf{A} + \mathbf{B}) + \mathbf{C}; \qquad \alpha(\mathbf{A} + \mathbf{B}) = \alpha\mathbf{A} + \alpha\mathbf{B}, \quad (\alpha + \beta)\mathbf{A} = \alpha\mathbf{A} + \beta\mathbf{A}; \qquad (3), (5)
> $$
>
> $$
> (\mathbf{AB})\mathbf{C} = \mathbf{A}(\mathbf{BC}), \qquad \mathbf{A}(\mathbf{B} + \mathbf{C}) = \mathbf{AB} + \mathbf{AC}, \qquad \mathbf{AI} = \mathbf{IA} = \mathbf{A} . \qquad (10), (11), (21)
> $$
>
> But matrix multiplication is **not commutative**: even when $\mathbf{A}$ and $\mathbf{B}$ are square of the same order, in general
>
> $$
> \mathbf{AB} \ne \mathbf{BA} . \qquad (12)
> $$
>
> *BDP: 7.2 (text), Equations (3), (5), (10)–(12), (21)*

^prop-34-1

*BDP states these laws without proof ("by direct calculation"; Problems 7.2.5–7.2.6); see [[§12 Matrix Operations#^thm-12-1|235 Thm. §12.1]] for sums and scalar multiples and [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^thm-13-1|235 Thm. §13.1]] for products. The proofs there use only the field axioms, so they hold verbatim for complex entries.*

> [!remark]- Connections
> - Products: [[§12 Matrix Operations#^def-12-5|235 Def. §12.5]] (column by column) and the row–column rule (9), [[§12 Matrix Operations#^prop-12-4|235 Prop. §12.4]]; non-commuting matrices and zero divisors, [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^ex-13-1|235 Ex. §13.1]]. In Axler, (9) is the definition [[§9 Matrices#^ladr-3-41|LADR 3.41]], motivated by composition of linear maps ([[§9 Matrices#^ladr-3-43|LADR 3.43]]), which is why it is associative and not commutative.

> [!example] Example §40.1: Matrix Multiplication Is Not Commutative
> Let
>
> $$
> \mathbf{A} = \begin{pmatrix} 1 & -2 & 1 \\ 0 & 2 & -1 \\ 2 & 1 & 1 \end{pmatrix}, \qquad \mathbf{B} = \begin{pmatrix} 2 & 1 & -1 \\ 1 & -1 & 0 \\ 2 & -1 & 1 \end{pmatrix}.
> $$
>
> By (9), row by column,
>
> $$
> \mathbf{AB} = \begin{pmatrix} 2 - 2 + 2 & 1 + 2 - 1 & -1 + 0 + 1 \\ 0 + 2 - 2 & 0 - 2 + 1 & 0 + 0 - 1 \\ 4 + 1 + 2 & 2 - 1 - 1 & -2 + 0 + 1 \end{pmatrix} = \begin{pmatrix} 2 & 2 & 0 \\ 0 & -1 & -1 \\ 7 & 0 & -1 \end{pmatrix},
> \qquad
> \mathbf{BA} = \begin{pmatrix} 0 & -3 & 0 \\ 1 & -4 & 2 \\ 4 & -5 & 4 \end{pmatrix}.
> $$
>
> (For instance, the $(1, 1)$ entry of $\mathbf{BA}$ is $2 \cdot 1 + 1 \cdot 0 + (-1) \cdot 2 = 0$.) Clearly $\mathbf{AB} \ne \mathbf{BA}$.
>
> *BDP: Example 7.2.1*

^ex-34-1

## Products of Vectors; the Inner Product

> [!definition] Definition §34.4: Dot Product xᵀy
> For vectors $\mathbf{x}$, $\mathbf{y}$ with $n$ (real or complex) components, the product $\mathbf{x}^T\mathbf{y}$, the $n$-dimensional extension of the dot product, is
>
> $$
> \mathbf{x}^T\mathbf{y} = \sum_{i=1}^n x_iy_i ; \qquad (13)
> $$
>
> *BDP: 7.2 (text), Equations (13) and (15)*

^def-34-4

> [!definition] Definition §34.5: Inner Product
> For vectors $\mathbf{x}$, $\mathbf{y}$ with $n$ (real or complex) components, the **scalar product** or **inner product** is
>
> $$
> (\mathbf{x}, \mathbf{y}) = \sum_{i=1}^n x_i\overline{y_i} ; \qquad (15)
> $$
>
> *BDP: 7.2 (text), Equations (13) and (15)*

^def-34-5

> [!definition] Definition §34.6: Length
> For a vector $\mathbf{x}$ with $n$ (real or complex) components, the **length** or **magnitude** of $\mathbf{x}$ is $\|\mathbf{x}\| = (\mathbf{x}, \mathbf{x})^{1/2}$, with the inner product (15).
>
> *BDP: 7.2 (text), Equations (13) and (15)*

^def-34-6

> [!definition] Definition §34.7: Orthogonality
> Vectors $\mathbf{x}$ and $\mathbf{y}$ are **orthogonal** if $(\mathbf{x}, \mathbf{y}) = 0$, with the inner product (15). For example, $\mathbf{i}, \mathbf{j}, \mathbf{k}$ form an orthogonal set.
>
> *BDP: 7.2 (text), Equations (13) and (15)*

^def-34-7

> [!theorem] Proposition §40.2: Properties of the Two Products
> For vectors $\mathbf{x}, \mathbf{y}, \mathbf{z}$ with $n$ components and a number $\alpha$:
>
> $$
> \mathbf{x}^T\mathbf{y} = \mathbf{y}^T\mathbf{x}, \qquad \mathbf{x}^T(\mathbf{y} + \mathbf{z}) = \mathbf{x}^T\mathbf{y} + \mathbf{x}^T\mathbf{z}, \qquad (\alpha\mathbf{x})^T\mathbf{y} = \alpha(\mathbf{x}^T\mathbf{y}) = \mathbf{x}^T(\alpha\mathbf{y}) ; \qquad (14)
> $$
>
> $$
> (\mathbf{x}, \mathbf{y}) = \mathbf{x}^T\overline{\mathbf{y}} ; \qquad (16)
> $$
>
> $$
> (\mathbf{x}, \mathbf{y}) = \overline{(\mathbf{y}, \mathbf{x})}, \qquad (\mathbf{x}, \mathbf{y} + \mathbf{z}) = (\mathbf{x}, \mathbf{y}) + (\mathbf{x}, \mathbf{z}), \qquad (\alpha\mathbf{x}, \mathbf{y}) = \alpha(\mathbf{x}, \mathbf{y}), \qquad (\mathbf{x}, \alpha\mathbf{y}) = \overline{\alpha}(\mathbf{x}, \mathbf{y}) ; \qquad (17)
> $$
>
> $$
> (\mathbf{x}, \mathbf{x}) = \sum_{i=1}^n x_i\overline{x_i} = \sum_{i=1}^n |x_i|^2 \ge 0, \quad\text{with equality only for } \mathbf{x} = \mathbf{0} . \qquad (18)
> $$
>
> In particular, if $\mathbf{y}$ is real, $(\mathbf{x}, \mathbf{y}) = \mathbf{x}^T\mathbf{y}$. If $\mathbf{x}$ has nonreal entries, $\mathbf{x}^T\mathbf{x} = \sum x_i^2$ (19) need not be real, and can be $0$ for $\mathbf{x} \ne \mathbf{0}$.
>
> *BDP: 7.2 (text), Equations (14) and (16)–(19)*

^prop-34-2

> [!proof]+ Proof
> BDP reads these off from the definitions (13) and (15). (14) holds termwise: $x_iy_i = y_ix_i$, $x_i(y_i + z_i) = x_iy_i + x_iz_i$ and $(\alpha x_i)y_i = \alpha(x_iy_i) = x_i(\alpha y_i)$. (16): $\overline{\mathbf{y}}$ has entries $\overline{y_i}$, so $\mathbf{x}^T\overline{\mathbf{y}} = \sum x_i\overline{y_i}$. (17): $\overline{(\mathbf{y}, \mathbf{x})} = \sum \overline{y_i\overline{x_i}} = \sum \overline{y_i}x_i = (\mathbf{x}, \mathbf{y})$, using $\overline{zw} = \overline{z}\,\overline{w}$ and $\overline{\overline{z}} = z$; additivity is termwise; $(\alpha\mathbf{x}, \mathbf{y}) = \sum \alpha x_i\overline{y_i}$; and $(\mathbf{x}, \alpha\mathbf{y}) = \sum x_i\overline{\alpha y_i} = \overline{\alpha}\sum x_i\overline{y_i}$. (18): $x_i\overline{x_i} = |x_i|^2 \ge 0$, and a sum of nonnegative numbers is $0$ only if each term is, that is, only if every $x_i = 0$. If $\mathbf{y}$ is real, $\overline{\mathbf{y}} = \mathbf{y}$ in (16).

^pf-34-2

*Uses:* [[§34 Matrices#^def-34-4|Def. §34.4]], [[§34 Matrices#^def-34-5|Def. §34.5]], [[§64 Complex Numbers#^prop-64-2|235 Prop. §64.2]] ($z\overline{z} = |z|^2$), [[§64 Complex Numbers#^thm-64-3|235 Thm. §64.3]] (conjugate of a product)

> [!remark]- Connections
> - $(\mathbf{x}, \mathbf{y})$ is the Euclidean inner product on $\mathbb{C}^n$, [[§20 Inner Products and Norms#^ladr-6-3|LADR 6.3]](a), with the same convention as BDP: linear in the first slot, conjugate-linear in the second; (17)–(18) are the axioms [[§20 Inner Products and Norms#^ladr-6-2|LADR 6.2]] and their consequences [[§20 Inner Products and Norms#^ladr-6-6|LADR 6.6]]. Physics puts the conjugate on the other slot (the warning after LADR 6.2).
> - For real vectors it is Lay's inner product $\mathbf{u}\cdot\mathbf{v} = \mathbf{u}^T\mathbf{v}$, [[§49 Inner Product, Length, and Orthogonality#^def-49-1|235 Def. §49.1]], with length and orthogonality [[§49 Inner Product, Length, and Orthogonality#^def-49-2|235 Def. §49.2]], [[§49 Inner Product, Length, and Orthogonality#^def-49-5|235 Def. §49.5]].

> [!example] Example §40.2: The Two Products for Complex Vectors
> Let $\mathbf{x} = \begin{pmatrix} i \\ -2 \\ 1 + i \end{pmatrix}$, $\mathbf{y} = \begin{pmatrix} 2 - i \\ i \\ 3 \end{pmatrix}$, $\mathbf{z} = \begin{pmatrix} 1 \\ 0 \\ i \end{pmatrix}$. Then
>
> $$
> \begin{aligned}
> \mathbf{x}^T\mathbf{y} &= (i)(2 - i) + (-2)(i) + (1 + i)(3) = (2i + 1) - 2i + (3 + 3i) = 4 + 3i, \\
> (\mathbf{x}, \mathbf{y}) &= (i)(2 + i) + (-2)(-i) + (1 + i)(3) = (2i - 1) + 2i + (3 + 3i) = 2 + 7i, \\
> \mathbf{x}^T\mathbf{x} &= (i)^2 + (-2)^2 + (1 + i)^2 = -1 + 4 + 2i = 3 + 2i, \\
> (\mathbf{x}, \mathbf{x}) &= (i)(-i) + (-2)(-2) + (1 + i)(1 - i) = 1 + 4 + 2 = 7, \\
> \mathbf{z}^T\mathbf{z} &= 1 + 0 + i^2 = 0, \qquad (\mathbf{z}, \mathbf{z}) = 1 + 0 + (i)(-i) = 2 .
> \end{aligned}
> $$
>
> So $\mathbf{x}^T\mathbf{x}$ is not real, $\mathbf{z}^T\mathbf{z} = 0$ although $\mathbf{z} \ne \mathbf{0}$, while $(\mathbf{x}, \mathbf{x}) = 7 = \|\mathbf{x}\|^2$ and $(\mathbf{z}, \mathbf{z}) = 2$ are positive lengths squared, as (18) promises. This is why lengths of complex vectors use $(\mathbf{x}, \mathbf{x})$, not $\mathbf{x}^T\mathbf{x}$.
>
> *BDP: 7.2 (text)*

^ex-34-2

## Inverses and Determinants

> [!definition] Definition §34.8: Inverse
> An $n \times n$ matrix $\mathbf{A}$ is **nonsingular** or **invertible** if there is a matrix $\mathbf{B}$ with $\mathbf{AB} = \mathbf{I}$ and $\mathbf{BA} = \mathbf{I}$. Such a $\mathbf{B}$ is unique; it is the **inverse** $\mathbf{A}^{-1}$, and
>
> $$
> \mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I} . \qquad (22)
> $$
>
> Matrices without an inverse are **singular** or **noninvertible**.
>
> *BDP: 7.2 (text), Equations (22)–(23)*

^def-34-8

> [!definition] Definition §34.9: Minor, Cofactor and Determinant
> For an $n \times n$ matrix $\mathbf{A}$: The **minor** $M_{ij}$ of the element $a_{ij}$ is the determinant of the matrix obtained by deleting row $i$ and column $j$ of $\mathbf{A}$; the **cofactor** is
>
> $$
> C_{ij} = (-1)^{i+j}M_{ij} . \qquad (23)
> $$
>
> The **determinant** $\det\mathbf{A}$ is the sum of the elements of any row or column times their cofactors; along the first row, $\det\mathbf{A} = a_{11}C_{11} + a_{12}C_{12} + \cdots + a_{1n}C_{1n}$.
>
> *BDP (p. 290) prints the first-row expansion as $C_{11} + C_{12} + \cdots + C_{1n}$, without the factors $a_{1j}$; the formula above is the correct one.*
> *BDP: 7.2 (text), Equations (22)–(23)*

^def-34-9

> [!theorem] Theorem §40.3: Determinant Test and Cofactor Formula for the Inverse
> $\mathbf{A}$ is nonsingular if and only if $\det\mathbf{A} \ne 0$; equivalently, $\mathbf{A}$ is singular if and only if $\det\mathbf{A} = 0$. When $\det\mathbf{A} \ne 0$, the elements of $\mathbf{B} = \mathbf{A}^{-1}$ are
>
> $$
> b_{ij} = \frac{C_{ji}}{\det\mathbf{A}} . \qquad (24)
> $$
>
> *BDP: 7.2 (text), Equation (24)*

^thm-34-3

*BDP states this without proof ("it can be shown"); see [[§25 Properties of Determinants#^thm-25-3|235 Thm. §25.3]] (invertible $\Leftrightarrow$ $\det \ne 0$), [[§27 Cramer’s Rule, Volume, and Linear Transformations#^thm-27-2|235 Thm. §27.2]] (the inverse formula, with the adjugate, the transposed matrix of cofactors, [[§27 Cramer’s Rule, Volume, and Linear Transformations#^def-27-2|235 Def. §27.2]]) and [[§14 The Inverse of a Matrix#^prop-14-1|235 Prop. §14.1]] (uniqueness of the inverse). The proofs use only field operations, so they hold for complex entries.*

> [!remark]- Connections
> - Cofactor expansion along any row or column: [[§24 Introduction to Determinants#^thm-24-1|235 Thm. §24.1]]. Rigorous treatment over any field: invertible $\Leftrightarrow$ nonzero determinant, [[§37 Determinants#^ladr-9-50|LADR 9.50]]; uniqueness of inverses, [[§10 Invertibility and Isomorphisms#^ladr-3-60|LADR 3.60]]; and a one-sided inverse of a square matrix is two-sided, [[§10 Invertibility and Isomorphisms#^ladr-3-68|LADR 3.68]] (so either condition in [[§34 Matrices#^def-34-8|Definition §34.8]] suffices).

Formula (24) is not an efficient way to compute $\mathbf{A}^{-1}$: for large $n$ the number of multiplications grows like $n!$, against $n^3$ for row reduction.

> [!remark] Remark: Method — Inverse by Row Reduction
> The **elementary row operations** are: (1) interchange two rows; (2) multiply a row by a nonzero scalar; (3) add a multiple of one row to another. A sequence of them that transforms $\mathbf{A}$ into $\mathbf{I}$ transforms $\mathbf{I}$ into $\mathbf{A}^{-1}$ (**row reduction** or **Gaussian elimination**). So:
> 1. Form the augmented matrix $(\mathbf{A} \mid \mathbf{I})$.
> 2. Column by column, get a $1$ in the diagonal position (interchange with a lower row first if the entry is $0$, then scale the row), and then zeros in the other positions of that column.
> 3. When the left half is $\mathbf{I}$, the right half is $\mathbf{A}^{-1}$: $(\mathbf{I} \mid \mathbf{A}^{-1})$.
> 4. If at some stage no row can supply a nonzero diagonal entry (the column is zero from the diagonal down), $\mathbf{A}$ is singular.
>
> Why the right half becomes $\mathbf{A}^{-1}$: each row operation is left multiplication by an elementary matrix, so if $\mathbf{E}_k\cdots\mathbf{E}_1\mathbf{A} = \mathbf{I}$ then $\mathbf{E}_k\cdots\mathbf{E}_1 = \mathbf{A}^{-1}$ and the same product applied to $\mathbf{I}$ gives $\mathbf{A}^{-1}$; this is [[§15 Elementary Matrices and the Inversion Algorithm#^thm-15-3|235 Thm. §15.3]], with [[§15 Elementary Matrices and the Inversion Algorithm#^prop-15-1|235 Prop. §15.1]].

^rem-34-1

> [!example] Example §40.3: Inverting a 3 × 3 Matrix
> Find the inverse of $\mathbf{A} = \begin{pmatrix} 1 & -1 & -1 \\ 3 & -1 & 2 \\ 2 & 2 & 3 \end{pmatrix}$.
>
> $$
> (\mathbf{A} \mid \mathbf{I}) = \left(\begin{array}{ccc|ccc} 1 & -1 & -1 & 1 & 0 & 0 \\ 3 & -1 & 2 & 0 & 1 & 0 \\ 2 & 2 & 3 & 0 & 0 & 1 \end{array}\right).
> $$
>
> **(a)** Add $(-3)$ times row 1 to row 2 and $(-2)$ times row 1 to row 3; **(b)** multiply row 2 by $\frac12$:
>
> $$
> \left(\begin{array}{ccc|ccc} 1 & -1 & -1 & 1 & 0 & 0 \\ 0 & 2 & 5 & -3 & 1 & 0 \\ 0 & 4 & 5 & -2 & 0 & 1 \end{array}\right)
> \;\to\;
> \left(\begin{array}{ccc|ccc} 1 & -1 & -1 & 1 & 0 & 0 \\ 0 & 1 & \frac52 & -\frac32 & \frac12 & 0 \\ 0 & 4 & 5 & -2 & 0 & 1 \end{array}\right).
> $$
>
> **(c)** Add row 2 to row 1 and $(-4)$ times row 2 to row 3; **(d)** multiply row 3 by $-\frac15$:
>
> $$
> \left(\begin{array}{ccc|ccc} 1 & 0 & \frac32 & -\frac12 & \frac12 & 0 \\ 0 & 1 & \frac52 & -\frac32 & \frac12 & 0 \\ 0 & 0 & -5 & 4 & -2 & 1 \end{array}\right)
> \;\to\;
> \left(\begin{array}{ccc|ccc} 1 & 0 & \frac32 & -\frac12 & \frac12 & 0 \\ 0 & 1 & \frac52 & -\frac32 & \frac12 & 0 \\ 0 & 0 & 1 & -\frac45 & \frac25 & -\frac15 \end{array}\right).
> $$
>
> **(e)** Add $(-\frac32)$ times row 3 to row 1 and $(-\frac52)$ times row 3 to row 2:
>
> $$
> \left(\begin{array}{ccc|ccc} 1 & 0 & 0 & \frac{7}{10} & -\frac{1}{10} & \frac{3}{10} \\ 0 & 1 & 0 & \frac12 & -\frac12 & \frac12 \\ 0 & 0 & 1 & -\frac45 & \frac25 & -\frac15 \end{array}\right) = (\mathbf{I} \mid \mathbf{A}^{-1}),
> \qquad
> \mathbf{A}^{-1} = \begin{pmatrix} \frac{7}{10} & -\frac{1}{10} & \frac{3}{10} \\ \frac12 & -\frac12 & \frac12 \\ -\frac45 & \frac25 & -\frac15 \end{pmatrix}.
> $$
>
> Check with (24): $\det\mathbf{A} = 1(-3 - 4) + 1(9 - 4) - 1(6 + 2) = -10$, and for instance $b_{11} = C_{11}/\det\mathbf{A} = (-3 - 4)/(-10) = \frac{7}{10}$. Direct multiplication confirms $\mathbf{A}\mathbf{A}^{-1} = \mathbf{I}$.
>
> *BDP: Example 7.2.2*

^ex-34-3

## Matrix Functions

> [!definition] Definition §34.10: Matrix Functions; Derivative and Integral
> Vectors and matrices whose elements are functions of a real variable $t$ are written
>
> $$
> \mathbf{x}(t) = \begin{pmatrix} x_1(t) \\ \vdots \\ x_n(t) \end{pmatrix}, \qquad \mathbf{A}(t) = \begin{pmatrix} a_{11}(t) & \cdots & a_{1n}(t) \\ \vdots & & \vdots \\ a_{m1}(t) & \cdots & a_{mn}(t) \end{pmatrix}. \qquad (25)
> $$
>
> $\mathbf{A}(t)$ is **continuous** at $t = t_0$, or on an interval $\alpha < t < \beta$, if every element is continuous there. It is **differentiable** if every element is differentiable, and then its derivative and integral are taken element by element:
>
> $$
> \frac{d\mathbf{A}}{dt} = \Big(\frac{da_{ij}}{dt}\Big), \qquad \int_a^b \mathbf{A}(t)\,dt = \Big(\int_a^b a_{ij}(t)\,dt\Big) . \qquad (26), (27)
> $$
>
> Vectors are the special case $n = 1$ of a single column.
>
> *BDP: 7.2 (text), Equations (25)–(27)*

^def-34-10

> [!remark]- Connections
> - The same definitions for vector functions in $\mathbb{R}^3$: [[§101 Derivatives and Integrals of Vector Functions#^thm-101-1|Calc Thm. §101.1]] (differentiate each component) and [[§101 Derivatives and Integrals of Vector Functions#^prop-101-4|Calc Prop. §101.4]] (integrate each component), from the limit definition [[§101 Derivatives and Integrals of Vector Functions#^def-101-1|Calc Def. §101.1]]. A matrix function is a vector function with $mn$ components arranged in a rectangle.

> [!example] Example §34.4: Differentiating and Integrating a Matrix Function
> If $\mathbf{A}(t) = \begin{pmatrix} \sin t & t \\ 1 & \cos t \end{pmatrix}$, then, element by element,
>
> $$
> \mathbf{A}'(t) = \begin{pmatrix} \cos t & 1 \\ 0 & -\sin t \end{pmatrix},
> \qquad
> \int_0^\pi \mathbf{A}(t)\,dt = \begin{pmatrix} \int_0^\pi \sin t\,dt & \int_0^\pi t\,dt \\ \int_0^\pi 1\,dt & \int_0^\pi \cos t\,dt \end{pmatrix} = \begin{pmatrix} 2 & \pi^2/2 \\ \pi & 0 \end{pmatrix}.
> $$
>
> *BDP: 7.2 (text)*

^ex-34-4

> [!theorem] Proposition §34.4: Rules for Differentiating Matrix Functions
> If $\mathbf{A}(t)$ and $\mathbf{B}(t)$ are differentiable and $\mathbf{C}$ is a constant matrix, then (for sizes where the operations are defined)
>
> $$
> \frac{d}{dt}(\mathbf{CA}) = \mathbf{C}\frac{d\mathbf{A}}{dt}, \qquad \frac{d}{dt}(\mathbf{A} + \mathbf{B}) = \frac{d\mathbf{A}}{dt} + \frac{d\mathbf{B}}{dt}, \qquad \frac{d}{dt}(\mathbf{AB}) = \mathbf{A}\frac{d\mathbf{B}}{dt} + \frac{d\mathbf{A}}{dt}\mathbf{B} . \qquad (28)\text{–}(30)
> $$
>
> In (28) and (30) the order of the factors must be kept.
>
> *BDP: 7.2 (text), Equations (28)–(30)*

^prop-34-4

*BDP gives no proof ("many of the rules of elementary calculus extend easily"). Element by element, (30) is the ordinary product rule applied to $(\mathbf{AB})_{ij} = \sum_k a_{ik}b_{kj}$: $\big(\sum_k a_{ik}b_{kj}\big)' = \sum_k a_{ik}b_{kj}' + \sum_k a_{ik}'b_{kj}$, the $(i, j)$ elements of $\mathbf{AB}'$ and $\mathbf{A}'\mathbf{B}$; (28) is the case $\mathbf{A}$ constant, and (29) is the sum rule. The vector-function versions are [[§101 Derivatives and Integrals of Vector Functions#^thm-101-2|Calc Thm. §101.2]].*

> [!remark] Remark: Elementwise and Not Elementwise
> Multiplication by a number, differentiation and integration act on each element separately. Most other operations do not: the square of a matrix is not obtained by squaring its elements, and $\frac{d}{dt}\mathbf{A}^2 = \mathbf{A}\mathbf{A}' + \mathbf{A}'\mathbf{A}$ by (30), which is not $2\mathbf{A}\mathbf{A}'$ unless $\mathbf{A}$ and $\mathbf{A}'$ commute. For example, with $\mathbf{A}(t) = \begin{pmatrix} t & 1 \\ 0 & 0 \end{pmatrix}$, $\mathbf{A}' = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$:
>
> $$
> \mathbf{A}^2 = \begin{pmatrix} t^2 & t \\ 0 & 0 \end{pmatrix}, \quad \frac{d}{dt}\mathbf{A}^2 = \begin{pmatrix} 2t & 1 \\ 0 & 0 \end{pmatrix} = \mathbf{A}\mathbf{A}' + \mathbf{A}'\mathbf{A}, \qquad\text{but}\quad 2\mathbf{A}\mathbf{A}' = \begin{pmatrix} 2t & 0 \\ 0 & 0 \end{pmatrix}.
> $$
>
> The same caution applies to $e^{\mathbf{A}t}$ in [[§39★ Fundamental Matrices#^def-39-3|Definition §39.3]].

^rem-34-2
