---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 2
section: 11
lay: "2.1"
aliases: ["Lay 2.1"]
tags: [applied-linear-algebra, math235]
---
← [[§10 Linear Models in Business, Science, and Engineering]] · ↑ [[· 2 Matrix Algebra]] · [[§12 The Inverse of a Matrix]] →

*Lay, Section 2.1 · MATH 235 lectures L6, L7.*

Matrices can be added, scaled and multiplied, and these operations obey most of the rules of ordinary algebra. The product $AB$ is defined so that multiplying by $AB$ does what multiplying first by $B$ and then by $A$ does: matrix multiplication *is* composition of linear transformations. Two views of the product are used constantly: each column of $AB$ is $A$ times the corresponding column of $B$, and each entry is a row of $A$ times a column of $B$. Three rules of number algebra fail for matrices ($AB \ne BA$ in general, no cancellation, $AB = 0$ without $A = 0$ or $B = 0$). The section ends with powers $A^k$ and the transpose $A^T$, whose key rule $(AB)^T = B^TA^T$ reverses the order of the factors.

## Matrix Notation

> [!definition] Definition §11.1: Matrix Notation; Diagonal, Identity and Zero Matrices
> An **$m \times n$ matrix** $A$ has $m$ rows and $n$ columns. The scalar in row $i$ and column $j$ is the **$(i, j)$-entry** $a_{ij}$ of $A$, and we write $A = [\,a_{ij}\,]$. Each column is a vector in $\mathbb{R}^m$; with columns $\mathbf{a}_1, \ldots, \mathbf{a}_n$,
>
> $$
> A = \begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n \end{bmatrix}, \qquad a_{ij} = \text{the } i\text{th entry of } \mathbf{a}_j .
> $$
>
> - The **diagonal entries** of $A$ are $a_{11}, a_{22}, a_{33}, \ldots$; they form the **main diagonal**.
> - A **diagonal matrix** is a square $n \times n$ matrix whose nondiagonal entries are all zero. The $n \times n$ **identity matrix** $I_n$ (diagonal entries $1$) is an example.
> - A **zero matrix**, written $0$, is a matrix all of whose entries are zero. Its size is usually clear from the context.
>
> *Lay: 2.1 (text)*

^def-11-1

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
> By Definition §11.3, column $j$ of $AB$ is $A\mathbf{b}_j$, and by the definition of a matrix–vector product, $A\mathbf{b}_j$ is the combination of the columns of $A$ with the entries $b_{1j}, \ldots, b_{nj}$ of $\mathbf{b}_j$ as weights.

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
> $\operatorname{row}_i(A)$ is a $1 \times n$ matrix, so $\operatorname{row}_i(A)\,B$ is a $1 \times p$ matrix. By the row–column rule (Proposition §11.4) its $j$th entry is $a_{i1}b_{1j} + \cdots + a_{in}b_{nj}$, which by the same rule is the $(i, j)$-entry of $AB$, the $j$th entry of $\operatorname{row}_i(AB)$.

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
> so $\mathbf{z} = B(A\mathbf{x}) = (BA)\mathbf{x}$, as Theorem §11.2 predicts. The map applied first, $A$, stands on the right.
>
> *Source: 235 lecture L7*

^ex-11-2

## Properties of Matrix Multiplication

> [!theorem] Theorem §11.6: Properties of Matrix Multiplication
> Let $A$ be an $m \times n$ matrix, and let $B$ and $C$ have sizes for which the indicated sums and products are defined.
>
> a. $A(BC) = (AB)C$ (associative law of multiplication)
> b. $A(B + C) = AB + AC$ (left distributive law)
> c. $(B + C)A = BA + CA$ (right distributive law)
> d. $r(AB) = (rA)B = A(rB)$ for any scalar $r$
> e. $I_mA = A = AI_n$ (identity for matrix multiplication)
>
> *Lay: Theorem 2 (2.1)*

^thm-11-6

> [!proof]+ Proof
> **(a)** Let $C = [\,\mathbf{c}_1 \ \cdots \ \mathbf{c}_p\,]$. By Definition §11.3, $BC = [\,B\mathbf{c}_1 \ \cdots \ B\mathbf{c}_p\,]$, and again by the definition,
>
> $$
> A(BC) = \begin{bmatrix} A(B\mathbf{c}_1) & \cdots & A(B\mathbf{c}_p) \end{bmatrix} = \begin{bmatrix} (AB)\mathbf{c}_1 & \cdots & (AB)\mathbf{c}_p \end{bmatrix} = (AB)C,
> $$
>
> using equation (1) of Theorem §11.2 for each column. (Lay also notes a second proof: matrix multiplication corresponds to composition of functions, and composition of functions is associative.)
>
> **(b)** (Lay's Exercise 29.) By the row–column rule, the $(i, j)$-entry of $A(B + C)$ is
>
> $$
> \sum_{k=1}^n a_{ik}(b_{kj} + c_{kj}) = \sum_{k=1}^n a_{ik}b_{kj} + \sum_{k=1}^n a_{ik}c_{kj},
> $$
>
> the sum of the $(i, j)$-entries of $AB$ and $AC$.
>
> **(c)** (Also Exercise 29.) The same computation with the factor on the right: the $(i, j)$-entry of $(B + C)A$ is $\sum_k (b_{ik} + c_{ik})a_{kj} = \sum_k b_{ik}a_{kj} + \sum_k c_{ik}a_{kj}$.
>
> **(d)** (Exercise 30.) The $(i, j)$-entry of $(rA)B$ is $(ra_{i1})b_{1j} + \cdots + (ra_{in})b_{nj} = r(a_{i1}b_{1j} + \cdots + a_{in}b_{nj})$, which is the $(i, j)$-entry of $r(AB)$. Likewise $a_{i1}(rb_{1j}) + \cdots + a_{in}(rb_{nj})$ is the $(i, j)$-entry of $r(AB)$, so $A(rB) = r(AB)$.
>
> **(e)** (Exercises 31–32.) Column $j$ of $I_mA$ is $I_m\mathbf{a}_j = \mathbf{a}_j$, since $I_m\mathbf{x} = \mathbf{x}$ for every $\mathbf{x} \in \mathbb{R}^m$; so $I_mA = A$. Column $j$ of $AI_n$ is $A\mathbf{e}_j$, where $\mathbf{e}_j$ is column $j$ of $I_n$, and $A\mathbf{e}_j = 0\mathbf{a}_1 + \cdots + 1\mathbf{a}_j + \cdots + 0\mathbf{a}_n = \mathbf{a}_j$; so $AI_n = A$.

^pf-11-6

*Uses:* [[§11 Matrix Operations#^def-11-3|Def. §11.3]], [[§11 Matrix Operations#^thm-11-2|§11.2]], [[§11 Matrix Operations#^prop-11-4|§11.4]], [[§4 The Matrix Equation Ax = b#^def-4-1|Def. §4.1]], [[§4 The Matrix Equation Ax = b#^def-4-4|Def. §4.4]] ($I_m\mathbf{x} = \mathbf{x}$)

> [!remark]- Connections
> - Rigorous treatment: the same laws for linear maps between any vector spaces, [[§7 Vector Space of Linear Maps#^ladr-3-8|LADR 3.8]] (associativity, identity, distributivity); they transfer to matrices through $\mathcal{M}(ST) = \mathcal{M}(S)\mathcal{M}(T)$. Associativity of composition of arbitrary functions: [[§8 Functions#^prop-8-1|250 Prop. §8.1]], which is Lay's second proof of (a).

The associative and distributive laws say that parentheses can be inserted and removed as in number algebra: $ABC$ means either $A(BC)$ or $(AB)C$, and $ABCD$ can be computed as $A(BCD)$, $(ABC)D$, $A(BC)D$ and so on, *as long as the left-to-right order of the factors is kept*. (When $B$ is square and $C$ has fewer columns than $A$ has rows, $A(BC)$ is cheaper to compute than $(AB)C$.)

> [!definition] Definition §11.4: Commuting Matrices
> In the product $AB$, $A$ is **right-multiplied** by $B$ and $B$ is **left-multiplied** by $A$. If $AB = BA$, then $A$ and $B$ **commute** with one another.
>
> *Lay: 2.1 (text)*

^def-11-4

> [!remark] Remark: Warnings
> Three rules of number algebra fail for matrices:
> 1. In general, $AB \ne BA$.
> 2. The cancellation laws do not hold: $AB = AC$ does not in general imply $B = C$.
> 3. If $AB$ is the zero matrix, one cannot conclude in general that $A = 0$ or $B = 0$.
>
> The first is no surprise: the columns of $AB$ are combinations of the columns of $A$, while the columns of $BA$ are built from the columns of $B$. [[§11 Matrix Operations#^ex-11-3|Example §11.3]] shows all three.

^rem-11-2

> [!example] Example §11.3: Matrices That Do Not Commute, and Zero Divisors
> **(a) Numbers.** For $A = \begin{bmatrix} 5 & 1 \\ 3 & -2 \end{bmatrix}$ and $B = \begin{bmatrix} 2 & 0 \\ 4 & 3 \end{bmatrix}$,
>
> $$
> AB = \begin{bmatrix} 10 + 4 & 0 + 3 \\ 6 - 8 & 0 - 6 \end{bmatrix} = \begin{bmatrix} 14 & 3 \\ -2 & -6 \end{bmatrix}, \qquad
> BA = \begin{bmatrix} 10 + 0 & 2 + 0 \\ 20 + 9 & 4 - 6 \end{bmatrix} = \begin{bmatrix} 10 & 2 \\ 29 & -2 \end{bmatrix},
> $$
>
> so $AB \ne BA$.
>
> **(b) Geometry.** Let $R_\varphi = \begin{bmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{bmatrix}$ be the counterclockwise rotation through $\varphi$ and $P = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ the projection onto the $x_1$-axis. Then
>
> $$
> R_\varphi P = \begin{bmatrix} \cos\varphi & 0 \\ \sin\varphi & 0 \end{bmatrix}, \qquad
> PR_\varphi = \begin{bmatrix} \cos\varphi & -\sin\varphi \\ 0 & 0 \end{bmatrix},
> $$
>
> which differ whenever $\sin\varphi \ne 0$. Geometrically: projecting $\mathbf{e}_1$ leaves it alone and rotating then gives $(\cos\varphi, \sin\varphi)$; rotating first and then projecting gives $(\cos\varphi, 0)$ (figure below).
>
> Rotations, on the other hand, commute with each other. By the addition formulas for cosine and sine,
>
> $$
> R_\theta R_\varphi = \begin{bmatrix} \cos\theta\cos\varphi - \sin\theta\sin\varphi & -(\cos\theta\sin\varphi + \sin\theta\cos\varphi) \\ \sin\theta\cos\varphi + \cos\theta\sin\varphi & \cos\theta\cos\varphi - \sin\theta\sin\varphi \end{bmatrix} = \begin{bmatrix} \cos(\theta + \varphi) & -\sin(\theta + \varphi) \\ \sin(\theta + \varphi) & \cos(\theta + \varphi) \end{bmatrix} = R_{\theta + \varphi},
> $$
>
> and $R_{\theta + \varphi} = R_{\varphi + \theta} = R_\varphi R_\theta$: rotating through $\varphi$ and then through $\theta$ is rotating through $\theta + \varphi$, in either order. (The lecture adds that the matrices $\begin{bmatrix} a & -b \\ b & a \end{bmatrix}$ also commute with each other; they multiply like the complex numbers $a + bi$, see [[§53 Complex Numbers#^rem-53-3|§53, Remark: Complex Numbers as 2 × 2 Matrices]].)
>
> **(c) A product can be zero.** Find all $2 \times 2$ matrices $X$ with $AX = 0$, where $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$. Writing $X = \begin{bmatrix} x_{11} & x_{12} \\ x_{21} & x_{22} \end{bmatrix}$,
>
> $$
> AX = \begin{bmatrix} x_{11} + 2x_{21} & x_{12} + 2x_{22} \\ 2x_{11} + 4x_{21} & 2x_{12} + 4x_{22} \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} .
> $$
>
> The second row of equations is twice the first, so the conditions are $x_{11} = -2x_{21}$ and $x_{12} = -2x_{22}$, with $x_{21}$, $x_{22}$ arbitrary:
>
> $$
> X = \begin{bmatrix} -2x_{21} & -2x_{22} \\ x_{21} & x_{22} \end{bmatrix} .
> $$
>
> For instance $x_{21} = 0$, $x_{22} = 1$ gives $X = \begin{bmatrix} 0 & -2 \\ 0 & 1 \end{bmatrix}$: $AX = 0$ although $A \ne 0$ and $X \ne 0$ (warning 3). Also $AX = A \cdot 0$ with $X \ne 0$, so $A$ cannot be cancelled (warning 2). The same happens with $\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 1 & 1 \\ -1 & -1 \end{bmatrix} = 0$ (lecture L9).
>
> *Lay: Example 2.1.7*
> *Source: 235 lectures L7, L9*

^ex-11-3

![[m235-11-1.svg]]
*Example §11.3(b) with $\varphi = 50^\circ$. Top: project, then rotate ($R_\varphi P$): $\mathbf{e}_1$ is unchanged by $P$ and ends at $(\cos\varphi, \sin\varphi)$. Bottom: rotate, then project ($PR_\varphi$): $\mathbf{e}_1$ is rotated and then flattened to $(\cos\varphi, 0)$. The two composites send $\mathbf{e}_1$ to different vectors, so $R_\varphi P \ne PR_\varphi$.*

## Powers of a Matrix

> [!definition] Definition §11.5: Powers of a Matrix
> If $A$ is an $n \times n$ matrix and $k$ is a positive integer, $A^k$ denotes the product of $k$ copies of $A$:
>
> $$
> A^k = \underbrace{A \cdots A}_{k} .
> $$
>
> $A^k\mathbf{x}$ is the result of left-multiplying $\mathbf{x}$ by $A$ repeatedly $k$ times. For $k = 0$, $A^0\mathbf{x}$ should be $\mathbf{x}$ itself, so $A^0$ is interpreted as the identity matrix $I_n$.
>
> *Lay: 2.1 (text)*

^def-11-5

> [!example] Example §11.4: Computing Powers
> **(a) A diagonal matrix.** For $A = \begin{bmatrix} 2 & 0 \\ 0 & -3 \end{bmatrix}$,
>
> $$
> A^2 = \begin{bmatrix} 2 & 0 \\ 0 & -3 \end{bmatrix}\begin{bmatrix} 2 & 0 \\ 0 & -3 \end{bmatrix} = \begin{bmatrix} 2^2 & 0 \\ 0 & (-3)^2 \end{bmatrix}, \qquad
> A^3 = A^2A = \begin{bmatrix} 2^3 & 0 \\ 0 & (-3)^3 \end{bmatrix},
> $$
>
> and in general $A^k = \begin{bmatrix} 2^k & 0 \\ 0 & (-3)^k \end{bmatrix}$: powers of a diagonal matrix are computed entry by entry.
>
> **(b) A column times a row.** Let $\mathbf{x} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$ ($2 \times 1$) and $\mathbf{y}^T = \begin{bmatrix} 3 & 4 \end{bmatrix}$ ($1 \times 2$), and
>
> $$
> A = \mathbf{x}\mathbf{y}^T = \begin{bmatrix} 1 \\ 2 \end{bmatrix}\begin{bmatrix} 3 & 4 \end{bmatrix} = \begin{bmatrix} 1 \cdot 3 & 1 \cdot 4 \\ 2 \cdot 3 & 2 \cdot 4 \end{bmatrix} = \begin{bmatrix} 3 & 4 \\ 6 & 8 \end{bmatrix} .
> $$
>
> By associativity, $A^2 = \mathbf{x}(\mathbf{y}^T\mathbf{x})\mathbf{y}^T$, and the middle factor is a $1 \times 1$ matrix, a number: $\mathbf{y}^T\mathbf{x} = 3 \cdot 1 + 4 \cdot 2 = 11$. So
>
> $$
> A^2 = 11\,\mathbf{x}\mathbf{y}^T = 11A, \qquad A^3 = A^2A = 11A^2 = 11^2A, \qquad A^k = 11^{k-1}A .
> $$
>
> (Check: $A^2 = \begin{bmatrix} 9 + 24 & 12 + 32 \\ 18 + 48 & 24 + 64 \end{bmatrix} = \begin{bmatrix} 33 & 44 \\ 66 & 88 \end{bmatrix} = 11A$.) In general $(\mathbf{x}\mathbf{y}^T)^k = (\mathbf{y}^T\mathbf{x})^{k-1}\,\mathbf{x}\mathbf{y}^T$.
>
> **(c) A nonzero matrix with zero square.** For $J = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$,
>
> $$
> J^2 = \begin{bmatrix} 0 \cdot 0 + 1 \cdot 0 & 0 \cdot 1 + 1 \cdot 0 \\ 0 \cdot 0 + 0 \cdot 0 & 0 \cdot 1 + 0 \cdot 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} .
> $$
>
> *Source: 235 lecture L7*

^ex-11-4

> [!remark]- Remark: Computing a Power Times a Vector
> To compute $A^2\mathbf{x}$ for a $4 \times 4$ matrix $A$, compute $A(A\mathbf{x})$: $A\mathbf{x}$ takes 16 multiplications (4 for each entry) and $A(A\mathbf{x})$ 16 more, 32 in all. Forming $A^2$ first takes 64 multiplications (4 for each of 16 entries), and then $A^2\mathbf{x}$ takes 16 more, 80 in all. (Lay's Practice Problem 2.)

^rem-11-3

## The Transpose of a Matrix

> [!definition] Definition §11.6: Transpose
> Given an $m \times n$ matrix $A$, the **transpose** of $A$ is the $n \times m$ matrix $A^T$ whose columns are formed from the corresponding rows of $A$. Equivalently, the $(i, j)$-entry of $A^T$ is the $(j, i)$-entry of $A$. For a square matrix, $A^T$ is the reflection of $A$ across the main diagonal. For example,
>
> $$
> \begin{bmatrix} a & b \\ c & d \end{bmatrix}^T = \begin{bmatrix} a & c \\ b & d \end{bmatrix}, \qquad
> \begin{bmatrix} -5 & 2 \\ 1 & -3 \\ 0 & 4 \end{bmatrix}^T = \begin{bmatrix} -5 & 1 & 0 \\ 2 & -3 & 4 \end{bmatrix}, \qquad
> \begin{bmatrix} 1 & 1 & 1 & 1 \\ -3 & 5 & -2 & 7 \end{bmatrix}^T = \begin{bmatrix} 1 & -3 \\ 1 & 5 \\ 1 & -2 \\ 1 & 7 \end{bmatrix} .
> $$
>
> *Lay: 2.1, Definition; Example 2.1.8*
> *Source: 235 lecture L8*

^def-11-6

> [!theorem] Theorem §11.7: Properties of the Transpose
> Let $A$ and $B$ denote matrices whose sizes are appropriate for the following sums and products.
>
> $$
> \text{(a) } (A^T)^T = A \qquad \text{(b) } (A + B)^T = A^T + B^T \qquad \text{(c) } (rA)^T = rA^T \text{ for any scalar } r \qquad \text{(d) } (AB)^T = B^TA^T
> $$
>
> Usually $(AB)^T \ne A^TB^T$, even when $A^TB^T$ is defined.
>
> *Lay: Theorem 3 (2.1)*

^thm-11-7

> [!proof]+ Proof
> Write $(M)_{ij}$ for the $(i, j)$-entry of a matrix $M$, so that $(M^T)_{ij} = (M)_{ji}$. Lay calls (a)–(c) straightforward:
>
> **(a)** $((A^T)^T)_{ij} = (A^T)_{ji} = (A)_{ij}$.
>
> **(b)** $((A + B)^T)_{ij} = (A + B)_{ji} = a_{ji} + b_{ji} = (A^T)_{ij} + (B^T)_{ij}$.
>
> **(c)** $((rA)^T)_{ij} = ra_{ji} = r(A^T)_{ij}$.
>
> **(d)** (Lay's Exercise 33.) Let $A$ be $m \times n$ and $B$ be $n \times p$, so both sides are $p \times m$. By the row–column rule,
>
> $$
> ((AB)^T)_{ij} = (AB)_{ji} = \sum_{k=1}^n a_{jk}b_{ki} = \sum_{k=1}^n (B^T)_{ik}(A^T)_{kj} = (B^TA^T)_{ij} .
> $$
>
> In words: row $i$ of $(AB)^T$ is column $i$ of $AB$, transposed.

^pf-11-7

*Uses:* [[§11 Matrix Operations#^def-11-6|Def. §11.6]], [[§11 Matrix Operations#^prop-11-4|§11.4]]

> [!remark]- Connections
> - Rigorous treatment: [[§9 Matrices#^ladr-3-54|LADR 3.54]] (transpose and its properties, including $(AC)^t = C^tA^t$). In LADR the transpose is the matrix of the dual map ([[§12 Duality|LADR §12]]), which explains why it reverses the order of products.

> [!theorem] Corollary §11.8: Transpose of a Product of Several Matrices
> The transpose of a product of matrices equals the product of their transposes in the *reverse* order:
>
> $$
> (A_1A_2 \cdots A_k)^T = A_k^T \cdots A_2^TA_1^T .
> $$
>
> *Lay: 2.1 (text)*

^cor-11-8

> [!proof]+ Proof
> Induction on $k$; the case $k = 2$ is Theorem §11.7(d). If the formula holds for $k - 1$ factors, then by (d) applied to $A_1 \cdots A_{k-1}$ and $A_k$,
>
> $$
> (A_1 \cdots A_{k-1}A_k)^T = A_k^T(A_1 \cdots A_{k-1})^T = A_k^TA_{k-1}^T \cdots A_1^T .
> $$

^pf-11-8

*Uses:* [[§11 Matrix Operations#^thm-11-7|§11.7]], [[§11 Matrix Operations#^thm-11-6|§11.6]] (associativity)

> [!example] Example §11.5: Transposes and Matrix Equations
> **(a)** Simplify $(A - 3B^2)^T$ for $n \times n$ matrices $A$ and $B$. By Theorem §11.7(b), (c) and Corollary §11.8,
>
> $$
> (A - 3B^2)^T = A^T + (-3BB)^T = A^T - 3(BB)^T = A^T - 3B^TB^T = A^T - 3(B^T)^2 .
> $$
>
> **(b)** Given $B = 2A - 3C^T$, find $A$, for $B = \begin{bmatrix} 1 & 0 \\ 4 & -2 \end{bmatrix}$ and $C = \begin{bmatrix} 1 & 2 \\ -1 & 3 \end{bmatrix}$. The rules of Theorem §11.1 allow solving as for numbers: $2A = B + 3C^T$, so $A = \tfrac12(B + 3C^T)$. Here
>
> $$
> C^T = \begin{bmatrix} 1 & -1 \\ 2 & 3 \end{bmatrix}, \qquad B + 3C^T = \begin{bmatrix} 1 + 3 & 0 - 3 \\ 4 + 6 & -2 + 9 \end{bmatrix} = \begin{bmatrix} 4 & -3 \\ 10 & 7 \end{bmatrix}, \qquad A = \begin{bmatrix} 2 & -3/2 \\ 5 & 7/2 \end{bmatrix} .
> $$
>
> Check: $2A - 3C^T = \begin{bmatrix} 4 & -3 \\ 10 & 7 \end{bmatrix} - \begin{bmatrix} 3 & -3 \\ 6 & 9 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 4 & -2 \end{bmatrix} = B$.
>
> **(c)** Vectors are $n \times 1$ matrices, so Theorem §11.7 applies to them. For $A = \begin{bmatrix} 1 & -3 \\ -2 & 4 \end{bmatrix}$ and $\mathbf{x} = \begin{bmatrix} 5 \\ 3 \end{bmatrix}$: $A\mathbf{x} = \begin{bmatrix} 5 - 9 \\ -10 + 12 \end{bmatrix} = \begin{bmatrix} -4 \\ 2 \end{bmatrix}$, so $(A\mathbf{x})^T = \begin{bmatrix} -4 & 2 \end{bmatrix}$, and indeed
>
> $$
> \mathbf{x}^TA^T = \begin{bmatrix} 5 & 3 \end{bmatrix}\begin{bmatrix} 1 & -2 \\ -3 & 4 \end{bmatrix} = \begin{bmatrix} 5 - 9 & -10 + 12 \end{bmatrix} = \begin{bmatrix} -4 & 2 \end{bmatrix} .
> $$
>
> Also $\mathbf{x}\mathbf{x}^T = \begin{bmatrix} 25 & 15 \\ 15 & 9 \end{bmatrix}$ and $\mathbf{x}^T\mathbf{x} = [\,25 + 9\,] = 34$, while $A^T\mathbf{x}^T$ is not defined ($\mathbf{x}^T$ has one row, $A^T$ has two columns).
>
> *Lay: 2.1, Practice Problem 1*
> *Source: 235 checklist (2.1)*

^ex-11-5

> [!remark] Remark: Inner and Outer Products
> For $\mathbf{u}$, $\mathbf{v}$ in $\mathbb{R}^n$ (as $n \times 1$ matrices), the $1 \times 1$ matrix $\mathbf{u}^T\mathbf{v} = u_1v_1 + \cdots + u_nv_n$ is the **scalar product** or **inner product** of $\mathbf{u}$ and $\mathbf{v}$, written as a number ([[§40 Inner Product, Length, and Orthogonality#^def-40-1|Definition §40.1]]). The $n \times n$ matrix $\mathbf{u}\mathbf{v}^T$ is their **outer product**. By Theorem §11.7(d), $\mathbf{v}^T\mathbf{u} = (\mathbf{u}^T\mathbf{v})^T = \mathbf{u}^T\mathbf{v}$ and $\mathbf{v}\mathbf{u}^T = (\mathbf{u}\mathbf{v}^T)^T$. Outer products reappear in the column–row expansion of $AB$ ([[§14 Partitioned Matrices#^thm-14-3|Theorem §14.3]]) and in [[§11 Matrix Operations#^ex-11-4|Example §11.4]](b). (Lay's Exercises 27–28.)

^rem-11-4

> [!remark]- Remark: Numerical Notes
> 1. The fastest way to compute $AB$ on a computer depends on how matrices are stored. The standard high-performance algorithms, such as those in LAPACK, compute $AB$ by columns, as in Definition §11.3 (a C++ version computes it by rows).
> 2. The column definition suits parallel processing: the columns of $B$ are assigned to different processors, which compute the corresponding columns of $AB$ independently and simultaneously.

^rem-11-5
