---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 2
section: 11
lay: "2.1"
aliases: ["Lay 2.1"]
tags: [applied-linear-algebra, math235]
---
← [[§10 Linear Models in Business, Science, and Engineering]] · ↑ [[· 2 Matrix Algebra]] · [[§11a Properties of Matrix Multiplication, Powers, and Transposes]] →

*Lay, Section 2.1 · MATH 235 lectures L6, L7.*

Matrices can be added, scaled and multiplied, and these operations obey most of the rules of ordinary algebra. The product $AB$ is defined so that multiplying by $AB$ does what multiplying first by $B$ and then by $A$ does: matrix multiplication *is* composition of linear transformations. Two views of the product are used constantly: each column of $AB$ is $A$ times the corresponding column of $B$, and each entry is a row of $A$ times a column of $B$. Three rules of number algebra fail for matrices ($AB \ne BA$ in general, no cancellation, $AB = 0$ without $A = 0$ or $B = 0$). The section ends with powers $A^k$ and the transpose $A^T$, whose key rule $(AB)^T = B^TA^T$ reverses the order of the factors.

## Matrix Notation

> [!definition] Definition §11.1: Matrix Notation
> An **$m \times n$ matrix** $A$ has $m$ rows and $n$ columns. The scalar in row $i$ and column $j$ is the **$(i, j)$-entry** $a_{ij}$ of $A$, and we write $A = [\,a_{ij}\,]$. Each column is a vector in $\mathbb{R}^m$; with columns $\mathbf{a}_1, \ldots, \mathbf{a}_n$,
>
> $$
> A = \begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n \end{bmatrix}, \qquad a_{ij} = \text{the } i\text{th entry of } \mathbf{a}_j .
> $$
>
> The **diagonal entries** of $A$ are $a_{11}, a_{22}, a_{33}, \ldots$; they form the **main diagonal**.
>
> *Lay: 2.1 (text)*

^def-11-1

> [!definition] Definition §11.1: Diagonal Matrix; Identity Matrix
> A **diagonal matrix** is a square $n \times n$ matrix whose nondiagonal entries are all zero. The $n \times n$ **identity matrix** $I_n$ (diagonal entries $1$) is an example.
>
> *Lay: 2.1 (text)*

^def-11-new1

> [!definition] Definition §11.1: Zero Matrix
> A **zero matrix**, written $0$, is a matrix all of whose entries are zero. Its size is usually clear from the context.
>
> *Lay: 2.1 (text)*

^def-11-new2

## Sums and Scalar Multiples

> [!definition] Definition §11.2: Equality, Sum and Scalar Multiple of Matrices
> - Two matrices are **equal** if they have the same size and their corresponding columns are equal, that is, their corresponding entries are equal.
> - If $A$ and $B$ are $m \times n$ matrices, their **sum** $A + B$ is the $m \times n$ matrix whose columns are the sums of the corresponding columns of $A$ and $B$. Since vectors are added entrywise, each entry of $A + B$ is the sum of the corresponding entries of $A$ and $B$. The sum is defined only when $A$ and $B$ have the same size.
> - If $r$ is a scalar, the **scalar multiple** $rA$ is the matrix whose columns are $r$ times the corresponding columns of $A$. As with vectors, $-A$ means $(-1)A$ and $A - B$ means $A + (-1)B$.
>
> For example, with $A = \begin{bmatrix} 4 & 0 & 5 \\ -1 & 3 & 2 \end{bmatrix}$, $B = \begin{bmatrix} 1 & 1 & 1 \\ 3 & 5 & 7 \end{bmatrix}$ and $C = \begin{bmatrix} 2 & -3 \\ 0 & 1 \end{bmatrix}$,
>
> $$
> A + B = \begin{bmatrix} 5 & 1 & 6 \\ 2 & 8 & 9 \end{bmatrix}, \qquad
> A - 2B = \begin{bmatrix} 4 & 0 & 5 \\ -1 & 3 & 2 \end{bmatrix} - \begin{bmatrix} 2 & 2 & 2 \\ 6 & 10 & 14 \end{bmatrix} = \begin{bmatrix} 2 & -2 & 3 \\ -7 & -7 & -12 \end{bmatrix},
> $$
>
> while $A + C$ is not defined, because $A$ and $C$ have different sizes.
>
> *Lay: 2.1 (text); Examples 2.1.1 and 2.1.2*

^def-11-2

> [!theorem] Theorem §11.1: Algebraic Properties of Sums and Scalar Multiples
> Let $A$, $B$ and $C$ be matrices of the same size, and let $r$ and $s$ be scalars.
>
> $$
> \begin{aligned}
> &\text{(a) } A + B = B + A && \text{(d) } r(A + B) = rA + rB \\
> &\text{(b) } (A + B) + C = A + (B + C) && \text{(e) } (r + s)A = rA + sA \\
> &\text{(c) } A + 0 = A && \text{(f) } r(sA) = (rs)A
> \end{aligned}
> $$
>
> *Lay: Theorem 1 (2.1)*

^thm-11-1

> [!proof]+ Proof
> In each equation the two sides have the same size, since $A$, $B$ and $C$ do. So it suffices to check that corresponding columns agree, and this follows from the same property of vectors in $\mathbb{R}^m$. For (b): if the $j$th columns of $A$, $B$, $C$ are $\mathbf{a}_j$, $\mathbf{b}_j$, $\mathbf{c}_j$, then the $j$th columns of $(A + B) + C$ and $A + (B + C)$ are
>
> $$
> (\mathbf{a}_j + \mathbf{b}_j) + \mathbf{c}_j \qquad\text{and}\qquad \mathbf{a}_j + (\mathbf{b}_j + \mathbf{c}_j),
> $$
>
> which are equal by associativity of vector addition. The other five properties are checked the same way, column by column, from the corresponding algebraic properties of $\mathbb{R}^m$.

^pf-11-1

*Uses:* [[§11 Matrix Operations#^def-11-2|Def. §11.2]], [[§3 Vector Equations#^thm-3-2|§3.2]] (algebraic properties of $\mathbb{R}^n$)

By (b), a sum $A + B + C$ can be computed in either grouping; the same holds for sums of four or more matrices.

## Matrix Multiplication

When $B$ multiplies $\mathbf{x}$, it produces $B\mathbf{x}$; when $A$ then multiplies $B\mathbf{x}$, the result is $A(B\mathbf{x})$. This is a composition of linear transformations, and the product $AB$ is defined so that a single multiplication by $AB$ does the same thing. If $A$ is $m \times n$, $B = [\,\mathbf{b}_1 \ \cdots \ \mathbf{b}_p\,]$ is $n \times p$ and $\mathbf{x} \in \mathbb{R}^p$, then $B\mathbf{x} = x_1\mathbf{b}_1 + \cdots + x_p\mathbf{b}_p$, and by linearity of $\mathbf{x} \mapsto A\mathbf{x}$,

$$
A(B\mathbf{x}) = x_1 A\mathbf{b}_1 + \cdots + x_p A\mathbf{b}_p = \begin{bmatrix} A\mathbf{b}_1 & A\mathbf{b}_2 & \cdots & A\mathbf{b}_p \end{bmatrix} \mathbf{x} .
$$

So the matrix with columns $A\mathbf{b}_1, \ldots, A\mathbf{b}_p$ does the job.

> [!definition] Definition §11.3: Matrix Product
> If $A$ is an $m \times n$ matrix and $B$ is an $n \times p$ matrix with columns $\mathbf{b}_1, \ldots, \mathbf{b}_p$, then the **product** $AB$ is the $m \times p$ matrix whose columns are $A\mathbf{b}_1, \ldots, A\mathbf{b}_p$:
>
> $$
> AB = A \begin{bmatrix} \mathbf{b}_1 & \mathbf{b}_2 & \cdots & \mathbf{b}_p \end{bmatrix} = \begin{bmatrix} A\mathbf{b}_1 & A\mathbf{b}_2 & \cdots & A\mathbf{b}_p \end{bmatrix} .
> $$
>
> The product is defined only when the number of columns of $A$ equals the number of rows of $B$; then $AB$ has as many rows as $A$ and as many columns as $B$:
>
> $$
> \underset{m \times n}{A}\ \underset{n \times p}{B} = \underset{m \times p}{AB} .
> $$
>
> *Lay: 2.1, Definition*

^def-11-3

> [!remark]- Connections
> - Rigorous treatment: [[§9 Matrices#^ladr-3-41|LADR 3.41]] defines the product by the row–column formula and [[§9 Matrices#^ladr-3-43|LADR 3.43]] proves that it is the matrix of the composite of linear maps, $\mathcal{M}(ST) = \mathcal{M}(S)\mathcal{M}(T)$, for any bases of any finite-dimensional spaces (here: standard bases of $\mathbb{R}^n$). Lay's column definition is [[§9 Matrices#^ladr-3-48|LADR 3.48]].
> - The chain rule says the derivative of a composite is the composite of the derivatives, so its Jacobian matrix is the product of the Jacobian matrices: [[§10 Composition of Functions and the Chain Rule#^thm-10-2|452 Thm. §10.2]].

> [!theorem] Theorem §11.2: Multiplication of Matrices Is Composition
> If $A$ is $m \times n$ and $B$ is $n \times p$, then
>
> $$
> A(B\mathbf{x}) = (AB)\mathbf{x} \qquad \text{for all } \mathbf{x} \in \mathbb{R}^p . \tag{1}
> $$
>
> Consequently, the composite of $\mathbf{x} \mapsto B\mathbf{x}$ followed by $\mathbf{y} \mapsto A\mathbf{y}$ is a linear transformation $\mathbb{R}^p \to \mathbb{R}^m$, and its standard matrix is $AB$.
>
> *Lay: 2.1, Equation (1) and text*

^thm-11-2

> [!proof]+ Proof
> Write $B = [\,\mathbf{b}_1 \ \cdots \ \mathbf{b}_p\,]$ and $\mathbf{x} = (x_1, \ldots, x_p)$. By the definition of $B\mathbf{x}$ as a linear combination of the columns of $B$, and by linearity of multiplication by $A$ ([[§4 The Matrix Equation Ax = b#^thm-4-5|Theorem §4.5]]),
>
> $$
> A(B\mathbf{x}) = A(x_1\mathbf{b}_1 + \cdots + x_p\mathbf{b}_p) = x_1A\mathbf{b}_1 + \cdots + x_pA\mathbf{b}_p .
> $$
>
> The right side is the linear combination of the columns $A\mathbf{b}_1, \ldots, A\mathbf{b}_p$ of $AB$ with weights $x_1, \ldots, x_p$, which is $(AB)\mathbf{x}$ by definition of a matrix–vector product. This proves (1). The map $\mathbf{x} \mapsto A(B\mathbf{x})$ therefore equals $\mathbf{x} \mapsto (AB)\mathbf{x}$, a matrix transformation, which is linear; its standard matrix is $AB$ because a matrix transformation $\mathbf{x} \mapsto M\mathbf{x}$ has standard matrix $M$ (uniqueness in [[§9 The Matrix of a Linear Transformation#^thm-9-1|Theorem §9.1]]).

^pf-11-2

*Uses:* [[§11 Matrix Operations#^def-11-3|Def. §11.3]], [[§4 The Matrix Equation Ax = b#^def-4-1|Def. §4.1]], [[§4 The Matrix Equation Ax = b#^thm-4-5|§4.5]], [[§9 The Matrix of a Linear Transformation#^thm-9-1|§9.1]]

> [!remark] Remark: Composition Reverses the Order
> In $AB$ the transformation applied *first* is $B$, the one on the right. "First $A$, then $B$" is the product $BA$. The lecture puts it this way: composition of linear transformations corresponds to the product of the matrices in the opposite order ([[§11 Matrix Operations#^ex-11-2|Example §11.2]]).

^rem-11-1

> [!theorem] Proposition §11.3: Columns of AB
> Each column of $AB$ is a linear combination of the columns of $A$, using as weights the entries of the corresponding column of $B$: column $j$ of $AB$ is
>
> $$
> A\mathbf{b}_j = b_{1j}\mathbf{a}_1 + b_{2j}\mathbf{a}_2 + \cdots + b_{nj}\mathbf{a}_n .
> $$
>
> *Lay: 2.1 (text)*

^prop-11-3

> [!proof]+ Proof
> By [[§11 Matrix Operations#^def-11-3|Definition §11.3]], column $j$ of $AB$ is $A\mathbf{b}_j$, and by the definition of a matrix–vector product, $A\mathbf{b}_j$ is the combination of the columns of $A$ with the entries $b_{1j}, \ldots, b_{nj}$ of $\mathbf{b}_j$ as weights.

^pf-11-3

*Uses:* [[§11 Matrix Operations#^def-11-3|Def. §11.3]], [[§4 The Matrix Equation Ax = b#^def-4-1|Def. §4.1]]

> [!theorem] Proposition §11.4: Row–Column Rule for Computing AB
> If $AB$ is defined, the entry in row $i$ and column $j$ of $AB$ is the sum of the products of corresponding entries of row $i$ of $A$ and column $j$ of $B$. If $A$ is $m \times n$,
>
> $$
> (AB)_{ij} = a_{i1}b_{1j} + a_{i2}b_{2j} + \cdots + a_{in}b_{nj} = \sum_{k=1}^n a_{ik}b_{kj} .
> $$
>
> *Lay: 2.1, Row–Column Rule for Computing AB*

^prop-11-4

> [!proof]+ Proof
> Column $j$ of $AB$ is $A\mathbf{b}_j$. By the row–vector rule for $A\mathbf{x}$ ([[§4 The Matrix Equation Ax = b#^prop-4-4|Proposition §4.4]]), the $i$th entry of $A\mathbf{b}_j$ is the sum of the products of corresponding entries of row $i$ of $A$ and of the vector $\mathbf{b}_j$, that is, $a_{i1}b_{1j} + \cdots + a_{in}b_{nj}$.

^pf-11-4

*Uses:* [[§11 Matrix Operations#^def-11-3|Def. §11.3]], [[§4 The Matrix Equation Ax = b#^prop-4-4|§4.4]] (row–vector rule)

> [!theorem] Proposition §11.5: Rows of AB
> Writing $\operatorname{row}_i(A)$ for the $i$th row of $A$,
>
> $$
> \operatorname{row}_i(AB) = \operatorname{row}_i(A) \cdot B . \tag{2}
> $$
>
> *Lay: 2.1, Equation (2)*

^prop-11-5

> [!proof]+ Proof
> $\operatorname{row}_i(A)$ is a $1 \times n$ matrix, so $\operatorname{row}_i(A)\,B$ is a $1 \times p$ matrix. By the row–column rule ([[§11 Matrix Operations#^prop-11-4|Proposition §11.4]]) its $j$th entry is $a_{i1}b_{1j} + \cdots + a_{in}b_{nj}$, which by the same rule is the $(i, j)$-entry of $AB$, the $j$th entry of $\operatorname{row}_i(AB)$.

^pf-11-5

*Uses:* [[§11 Matrix Operations#^prop-11-4|§11.4]]

> [!example] Example §11.1: Computing a Product, by Columns and by Entries
> **(a)** Compute $AB$ for $A = \begin{bmatrix} 2 & 3 \\ 1 & -5 \end{bmatrix}$ and $B = \begin{bmatrix} 4 & 3 & 6 \\ 1 & -2 & 3 \end{bmatrix}$.
>
> **By columns.** With $B = [\,\mathbf{b}_1 \ \mathbf{b}_2 \ \mathbf{b}_3\,]$,
>
> $$
> A\mathbf{b}_1 = \begin{bmatrix} 2 & 3 \\ 1 & -5 \end{bmatrix}\begin{bmatrix} 4 \\ 1 \end{bmatrix} = \begin{bmatrix} 11 \\ -1 \end{bmatrix}, \quad
> A\mathbf{b}_2 = \begin{bmatrix} 2 & 3 \\ 1 & -5 \end{bmatrix}\begin{bmatrix} 3 \\ -2 \end{bmatrix} = \begin{bmatrix} 0 \\ 13 \end{bmatrix}, \quad
> A\mathbf{b}_3 = \begin{bmatrix} 2 & 3 \\ 1 & -5 \end{bmatrix}\begin{bmatrix} 6 \\ 3 \end{bmatrix} = \begin{bmatrix} 21 \\ -9 \end{bmatrix},
> $$
>
> so
>
> $$
> AB = \begin{bmatrix} A\mathbf{b}_1 & A\mathbf{b}_2 & A\mathbf{b}_3 \end{bmatrix} = \begin{bmatrix} 11 & 0 & 21 \\ -1 & 13 & -9 \end{bmatrix} .
> $$
>
> **By entries.** The $(1, 3)$-entry uses row 1 of $A$ and column 3 of $B$: $2(6) + 3(3) = 21$. The $(2, 2)$-entry uses row 2 of $A$ and column 2 of $B$: $1(3) + (-5)(-2) = 13$. Both agree with the column computation. Here $BA$ is not defined: $B$ has 3 columns and $A$ has 2 rows.
>
> **(b)** (Lecture.) For $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$ ($3 \times 2$) and $B = \begin{bmatrix} 7 & 8 \\ 9 & 10 \end{bmatrix}$ ($2 \times 2$), the product $AB$ is defined and is $3 \times 2$:
>
> $$
> AB = \begin{bmatrix} 1 \cdot 7 + 2 \cdot 9 & 1 \cdot 8 + 2 \cdot 10 \\ 3 \cdot 7 + 4 \cdot 9 & 3 \cdot 8 + 4 \cdot 10 \\ 5 \cdot 7 + 6 \cdot 9 & 5 \cdot 8 + 6 \cdot 10 \end{bmatrix} = \begin{bmatrix} 25 & 28 \\ 57 & 64 \\ 89 & 100 \end{bmatrix} .
> $$
>
> $BA$ is not defined, since the rows of $B$ have length 2 and the columns of $A$ have length 3. The rule to remember: a product is defined exactly when the length of the rows of the left factor equals the length of the columns of the right factor. Likewise, if $A$ is $3 \times 5$ and $B$ is $5 \times 2$, then $AB$ is $3 \times 2$ and $BA$ is undefined.
>
> **(c)** A single row of a product needs only one row of the left factor (equation (2)). For $A = \begin{bmatrix} 2 & -5 & 0 \\ -1 & 3 & -4 \\ 6 & -8 & -7 \\ -3 & 0 & 9 \end{bmatrix}$ and $B = \begin{bmatrix} 4 & -6 \\ 7 & 1 \\ 3 & 2 \end{bmatrix}$,
>
> $$
> \operatorname{row}_2(AB) = \begin{bmatrix} -1 & 3 & -4 \end{bmatrix} \begin{bmatrix} 4 & -6 \\ 7 & 1 \\ 3 & 2 \end{bmatrix} = \begin{bmatrix} -4 + 21 - 12 & 6 + 3 - 8 \end{bmatrix} = \begin{bmatrix} 5 & 1 \end{bmatrix} .
> $$
>
> *Lay: Examples 2.1.3–2.1.6*
> *Source: 235 lecture L6*

^ex-11-1

> [!example] Example §11.2: The Matrix of a Composition
> Let $\mathbf{y} = A\mathbf{x}$ and $\mathbf{z} = B\mathbf{y}$, where
>
> $$
> A = \begin{bmatrix} 1 & 2 \\ 3 & 5 \end{bmatrix}, \qquad B = \begin{bmatrix} 6 & 7 \\ 8 & 9 \end{bmatrix} .
> $$
>
> Express $\mathbf{z}$ in terms of $\mathbf{x}$.
>
> Componentwise, $y_1 = x_1 + 2x_2$, $y_2 = 3x_1 + 5x_2$, and $z_1 = 6y_1 + 7y_2$, $z_2 = 8y_1 + 9y_2$. Substituting,
>
> $$
> \begin{aligned}
> z_1 &= 6(x_1 + 2x_2) + 7(3x_1 + 5x_2) = (6 \cdot 1 + 7 \cdot 3)x_1 + (6 \cdot 2 + 7 \cdot 5)x_2 = 27x_1 + 47x_2, \\
> z_2 &= 8(x_1 + 2x_2) + 9(3x_1 + 5x_2) = (8 \cdot 1 + 9 \cdot 3)x_1 + (8 \cdot 2 + 9 \cdot 5)x_2 = 35x_1 + 61x_2 .
> \end{aligned}
> $$
>
> The coefficient matrix is exactly the row–column computation of
>
> $$
> BA = \begin{bmatrix} 6 & 7 \\ 8 & 9 \end{bmatrix}\begin{bmatrix} 1 & 2 \\ 3 & 5 \end{bmatrix} = \begin{bmatrix} 6 \cdot 1 + 7 \cdot 3 & 6 \cdot 2 + 7 \cdot 5 \\ 8 \cdot 1 + 9 \cdot 3 & 8 \cdot 2 + 9 \cdot 5 \end{bmatrix} = \begin{bmatrix} 27 & 47 \\ 35 & 61 \end{bmatrix},
> $$
>
> so $\mathbf{z} = B(A\mathbf{x}) = (BA)\mathbf{x}$, as [[§11 Matrix Operations#^thm-11-2|Theorem §11.2]] predicts. The map applied first, $A$, stands on the right.
>
> *Source: 235 lecture L7*

^ex-11-2

*Continued in [[§11a Properties of Matrix Multiplication, Powers, and Transposes]]: the algebraic rules of matrix multiplication, powers of a matrix, and the transpose.*
