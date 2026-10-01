---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 2
section: 15
lay: "2.5"
aliases: ["Lay 2.5"]
tags: [applied-linear-algebra, math235]
---
← [[§14 Partitioned Matrices]] · ↑ [[· 2 Matrix Algebra]] · [[§16 The Leontief Input–Output Model]] →

*Lay, Section 2.5 · MATH 235 lecture L9.*

Matrix multiplication combines data; a factorization $A = BC$ analyzes it, splitting $A$ into pieces with more useful structure. This section is about the LU factorization $A = LU$, with $L$ unit lower triangular and $U$ an echelon form of $A$. It is what computer programs use to solve many systems $A\mathbf{x} = \mathbf{b}_1, A\mathbf{x} = \mathbf{b}_2, \ldots$ with the same coefficient matrix: each system becomes two triangular systems, which are cheap to solve. The factorization costs nothing extra, since $L$ simply records the multipliers used while row reducing $A$ to $U$. A second application factors the transfer matrix of an electrical network into the matrices of simple circuits. Other factorizations come later: QR ([[§43 The Gram–Schmidt Process#^thm-43-3|Theorem §43.3]]), $PDP^{-1}$ ([[§34 Diagonalization|§34]]), the spectral decomposition ([[§48★ Diagonalization of Symmetric Matrices#^thm-48-4|Theorem §48.4]]) and the SVD ([[§51★ The Singular Value Decomposition#^thm-51-4|Theorem §51.4]]).

## The LU Factorization

A **factorization** of a matrix $A$ is an equation that expresses $A$ as a product of two or more matrices. The LU factorization is motivated by a common industrial and business problem: solving a sequence of equations with the same coefficient matrix,

$$
A\mathbf{x} = \mathbf{b}_1, \quad A\mathbf{x} = \mathbf{b}_2, \quad \ldots, \quad A\mathbf{x} = \mathbf{b}_p . \tag{1}
$$

When $A$ is invertible one could compute $A^{-1}$ and then $A^{-1}\mathbf{b}_1$, $A^{-1}\mathbf{b}_2$, and so on (as the lecture suggests in [[§12 The Inverse of a Matrix#^ex-12-2|Example §12.2]]). It is more efficient to solve the first equation by row reduction, obtaining an LU factorization of $A$ at the same time, and to solve the others with the factorization.

> [!definition] Definition §15.1: Unit Lower Triangular Matrix; LU Factorization
> A square matrix $L$ is **lower triangular** if all its entries above the main diagonal are zero, and **unit lower triangular** if moreover all its diagonal entries are $1$.
>
> Let $A$ be an $m \times n$ matrix. An **LU factorization** of $A$ is an equation
>
> $$
> A = LU,
> $$
>
> where $L$ is an $m \times m$ unit lower triangular matrix and $U$ is an $m \times n$ echelon form of $A$:
>
> $$
> A = \underbrace{\begin{bmatrix} 1 & 0 & 0 & 0 \\ * & 1 & 0 & 0 \\ * & * & 1 & 0 \\ * & * & * & 1 \end{bmatrix}}_{L} \underbrace{\begin{bmatrix} \blacksquare & * & * & * & * \\ 0 & \blacksquare & * & * & * \\ 0 & 0 & 0 & \blacksquare & * \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}}_{U} \qquad (\blacksquare \ne 0) .
> $$
>
> $L$ is invertible (it row reduces to $I$ by downward replacements, Proposition §15.1).
>
> *Lay: 2.5 (text)*

^def-15-1

When $A = LU$, the equation $A\mathbf{x} = \mathbf{b}$ can be written $L(U\mathbf{x}) = \mathbf{b}$. Writing $\mathbf{y}$ for $U\mathbf{x}$, we find $\mathbf{x}$ by solving the pair of equations

$$
L\mathbf{y} = \mathbf{b}, \qquad U\mathbf{x} = \mathbf{y} . \tag{2}
$$

The map $\mathbf{x} \mapsto A\mathbf{x}$ is factored as $\mathbf{x} \mapsto \mathbf{y} = U\mathbf{x}$ followed by $\mathbf{y} \mapsto L\mathbf{y} = \mathbf{b}$. Each equation in (2) is easy to solve because $L$ and $U$ are triangular.

> [!remark] Remark: Method — Solving Ax = b with an LU Factorization
> 1. **Forward substitution.** Solve $L\mathbf{y} = \mathbf{b}$ for $\mathbf{y}$ by row reducing $[\,L \ \ \mathbf{b}\,]$ to $[\,I \ \ \mathbf{y}\,]$. Since $L$ is unit lower triangular, the zeros below each pivot of $L$ are created by downward replacements and only the last column changes: $y_1 = b_1$, then $y_2 = b_2 - l_{21}y_1$, and in general $y_i = b_i - \sum_{k < i} l_{ik}y_k$.
> 2. **Back substitution.** Solve $U\mathbf{x} = \mathbf{y}$ by the backward phase of row reduction on $[\,U \ \ \mathbf{y}\,]$, from the bottom pivot up.
> 3. For further right sides $\mathbf{b}_2, \mathbf{b}_3, \ldots$ reuse the same $L$ and $U$.

^rem-15-1

> [!example] Example §15.1: Solving a System with a Given LU Factorization
> It can be verified that
>
> $$
> A = \begin{bmatrix} 3 & -7 & -2 & 2 \\ -3 & 5 & 1 & 0 \\ 6 & -4 & 0 & -5 \\ -9 & 5 & -5 & 12 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ 2 & -5 & 1 & 0 \\ -3 & 8 & 3 & 1 \end{bmatrix}\begin{bmatrix} 3 & -7 & -2 & 2 \\ 0 & -2 & -1 & 2 \\ 0 & 0 & -1 & 1 \\ 0 & 0 & 0 & -1 \end{bmatrix} = LU .
> $$
>
> Use this to solve $A\mathbf{x} = \mathbf{b}$ for $\mathbf{b} = (-9, 5, 7, 11)$.
>
> **$L\mathbf{y} = \mathbf{b}$.** Forward substitution:
>
> $$
> \begin{aligned}
> y_1 &= -9, \\
> y_2 &= 5 + y_1 = 5 - 9 = -4, \\
> y_3 &= 7 - 2y_1 + 5y_2 = 7 + 18 - 20 = 5, \\
> y_4 &= 11 + 3y_1 - 8y_2 - 3y_3 = 11 - 27 + 32 - 15 = 1 .
> \end{aligned}
> $$
>
> So $[\,L \ \ \mathbf{b}\,] \sim [\,I \ \ \mathbf{y}\,]$ with $\mathbf{y} = (-9, -4, 5, 1)$. This takes only 6 multiplications and 6 additions, because the arithmetic happens only in the last column.
>
> **$U\mathbf{x} = \mathbf{y}$.** Back substitution, from the last row of $[\,U \ \ \mathbf{y}\,]$ up:
>
> $$
> \begin{aligned}
> -x_4 &= 1 &&\Rightarrow\ x_4 = -1, \\
> -x_3 + x_4 &= 5 &&\Rightarrow\ x_3 = x_4 - 5 = -6, \\
> -2x_2 - x_3 + 2x_4 &= -4 &&\Rightarrow\ -2x_2 = -4 + x_3 - 2x_4 = -4 - 6 + 2 = -8,\ x_2 = 4, \\
> 3x_1 - 7x_2 - 2x_3 + 2x_4 &= -9 &&\Rightarrow\ 3x_1 = -9 + 28 - 12 + 2 = 9,\ x_1 = 3 .
> \end{aligned}
> $$
>
> So $\mathbf{x} = (3, 4, -6, -1)$. This backward phase takes 4 divisions, 6 multiplications and 6 additions. Finding $\mathbf{x}$ costs 28 arithmetic operations ("flops") in all, excluding the cost of $L$ and $U$; row reducing $[\,A \ \ \mathbf{b}\,]$ to $[\,I \ \ \mathbf{x}\,]$ takes 62.
>
> *Lay: Example 2.5.1*

^ex-15-1

## An LU Factorization Algorithm

> [!theorem] Proposition §15.1: Products and Inverses of Unit Lower Triangular Matrices
> The product of two $n \times n$ unit lower triangular matrices is unit lower triangular. A unit lower triangular matrix is invertible, and its inverse is unit lower triangular.
>
> *Lay: 2.5 (text)*

^prop-15-1

> [!proof]+ Proof
> (Lay states this and points to Exercise 19.) Let $L$, $M$ be unit lower triangular: $l_{ik} = 0$ for $k > i$ and $l_{ii} = 1$, likewise for $M$. By the row–column rule $(LM)_{ij} = \sum_k l_{ik}m_{kj}$, and a term can be nonzero only if $k \le i$ (else $l_{ik} = 0$) and $k \ge j$ (else $m_{kj} = 0$). If $j > i$ no $k$ satisfies both, so $(LM)_{ij} = 0$; if $j = i$ only $k = i$ does, so $(LM)_{ii} = l_{ii}m_{ii} = 1$. So $LM$ is unit lower triangular.
>
> For the inverse, row reduce $L$ to $I$ column by column: for $j = 1, \ldots, n - 1$, subtract $l_{ij}$ times row $j$ from each row $i > j$. When column $j$ is treated, row $j$ has already become $\mathbf{e}_j^T$ (its entries left of the diagonal were cleared earlier, and its diagonal entry is $1$), so each operation changes only column $j$ and leaves the earlier columns cleared. Each operation is a replacement adding a multiple of a row to a row *below* it, whose elementary matrix $E_{ij}(-l_{ij})$ ($i > j$) is unit lower triangular. Thus $E_p \cdots E_1L = I$, so $L$ is invertible with $L^{-1} = E_p \cdots E_1$ (Corollary §13.2), a product of unit lower triangular matrices, hence unit lower triangular by the first part.

^pf-15-1

*Uses:* [[§11 Matrix Operations#^prop-11-4|§11.4]], [[§12 The Inverse of a Matrix#^prop-12-6|§12.6]], [[§13 Characterizations of Invertible Matrices#^cor-13-2|§13.2]]

> [!theorem] Theorem §15.2: Existence of an LU Factorization
> Suppose an $m \times n$ matrix $A$ can be reduced to an echelon form $U$ using only row replacements that add a multiple of one row to another row *below* it. Then there are unit lower triangular elementary matrices $E_1, \ldots, E_p$ with
>
> $$
> E_p \cdots E_1A = U, \tag{3}
> $$
>
> and $A = LU$ with
>
> $$
> L = (E_p \cdots E_1)^{-1}, \tag{4}
> $$
>
> an $m \times m$ unit lower triangular matrix. The same row operations that reduce $A$ to $U$ reduce $L$ to $I$; and conversely, any $L$ that is reduced to $I$ by this same sequence of operations is the $L$ of (4).
>
> *Lay: 2.5 (text)*

^thm-15-2

> [!proof]+ Proof
> Each allowed replacement, adding $a$ times row $j$ to row $i > j$, is left multiplication by $E_{ij}(a)$ (Proposition §12.6), which is unit lower triangular because its one off-diagonal entry is in position $(i, j)$ with $i > j$. This gives (3). By Proposition §15.1 the product $E_p \cdots E_1$ is unit lower triangular and invertible, and so is its inverse $L$; multiplying (3) on the left by $L$ gives $A = LU$. Also
>
> $$
> E_p \cdots E_1L = (E_p \cdots E_1)(E_p \cdots E_1)^{-1} = I,
> $$
>
> so the operations in (3) reduce $L$ to $I$. Conversely, if a matrix $L$ satisfies $(E_p \cdots E_1)L = I$ for the same $E_1, \ldots, E_p$, then $L$ is invertible by the Invertible Matrix Theorem (Corollary §13.2), with $E_p \cdots E_1 = L^{-1}$. By (3), $L^{-1}A = U$, so $A = LU$.

^pf-15-2

*Uses:* [[§12 The Inverse of a Matrix#^prop-12-6|§12.6]], [[§15 Matrix Factorizations#^prop-15-1|§15.1]], [[§13 Characterizations of Invertible Matrices#^cor-13-2|§13.2]]

> [!remark] Remark: Method — LU Factorization
> 1. Reduce $A$ to an echelon form $U$ by a sequence of row replacement operations (each adding a multiple of a row to a row below it), if possible.
> 2. Place entries in $L$ such that the *same sequence of row operations* reduces $L$ to $I$. In practice: at each pivot column, take the entries of the current matrix from the pivot down (the entries used to choose the row operations), divide them by the pivot, and place the result into the corresponding column of $L$, on and below the diagonal. If $A$ has fewer pivot columns than rows, fill the remaining columns of $L$ from the identity matrix.
>
> Step 1 is not always possible (a row interchange may be needed); when it is, Theorem §15.2 shows that step 2 produces an acceptable $L$. Each entry of $L$ below the diagonal is the multiplier $\ell$ in the operation "row $i$ $-$ $\ell$ · (pivot row)" that cleared that position.
>
> *Lay: 2.5, Algorithm for an LU Factorization*

^rem-15-2

> [!example] Example §15.2: Finding an LU Factorization
> Find an LU factorization of
>
> $$
> A = \begin{bmatrix} 2 & 4 & -1 & 5 & -2 \\ -4 & -5 & 3 & -8 & 1 \\ 2 & -5 & -4 & 1 & 8 \\ -6 & 0 & 7 & -3 & 1 \end{bmatrix} .
> $$
>
> $A$ has four rows, so $L$ is $4 \times 4$. Row reduce $A$ using only downward replacements, recording at each pivot column the entries from the pivot down:
>
> $$
> A \xrightarrow[R_4 + 3R_1]{R_2 + 2R_1,\ R_3 - R_1}
> \begin{bmatrix} 2 & 4 & -1 & 5 & -2 \\ 0 & 3 & 1 & 2 & -3 \\ 0 & -9 & -3 & -4 & 10 \\ 0 & 12 & 4 & 12 & -5 \end{bmatrix}
> \xrightarrow[R_4 - 4R_2]{R_3 + 3R_2}
> \begin{bmatrix} 2 & 4 & -1 & 5 & -2 \\ 0 & 3 & 1 & 2 & -3 \\ 0 & 0 & 0 & 2 & 1 \\ 0 & 0 & 0 & 4 & 7 \end{bmatrix}
> \xrightarrow{R_4 - 2R_3}
> \begin{bmatrix} 2 & 4 & -1 & 5 & -2 \\ 0 & 3 & 1 & 2 & -3 \\ 0 & 0 & 0 & 2 & 1 \\ 0 & 0 & 0 & 0 & 5 \end{bmatrix} = U .
> $$
>
> The recorded columns are $(2, -4, 2, -6)$ in column 1, $(3, -9, 12)$ in column 2, $(2, 4)$ in column 4 and $(5)$ in column 5. Divide each by its pivot:
>
> $$
> \begin{bmatrix} 2 \\ -4 \\ 2 \\ -6 \end{bmatrix} \div 2 = \begin{bmatrix} 1 \\ -2 \\ 1 \\ -3 \end{bmatrix}, \quad
> \begin{bmatrix} 3 \\ -9 \\ 12 \end{bmatrix} \div 3 = \begin{bmatrix} 1 \\ -3 \\ 4 \end{bmatrix}, \quad
> \begin{bmatrix} 2 \\ 4 \end{bmatrix} \div 2 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}, \quad
> [\,5\,] \div 5 = [\,1\,],
> $$
>
> and place them in the columns of $L$ from the diagonal down:
>
> $$
> L = \begin{bmatrix} 1 & 0 & 0 & 0 \\ -2 & 1 & 0 & 0 \\ 1 & -3 & 1 & 0 \\ -3 & 4 & 2 & 1 \end{bmatrix} .
> $$
>
> Compare the first columns of $A$ and $L$: the row operations that create zeros in the first column of $A$ also create zeros in the first column of $L$, and the same holds for the later columns. Multiplying out confirms $LU = A$; for instance row 4 of $LU$ is $-3(2, 4, -1, 5, -2) + 4(0, 3, 1, 2, -3) + 2(0, 0, 0, 2, 1) + 1(0, 0, 0, 0, 5) = (-6, 0, 7, -3, 1)$.
>
> *Lay: Example 2.5.2*

^ex-15-2

> [!example] Example §15.3: An LU Factorization with Fewer Pivots Than Rows
> Find an LU factorization of
>
> $$
> A = \begin{bmatrix} 2 & -4 & -2 & 3 \\ 6 & -9 & -5 & 8 \\ 2 & -7 & -3 & 9 \\ 4 & -2 & -2 & -1 \\ -6 & 3 & 3 & 4 \end{bmatrix} .
> $$
>
> Row reduce with downward replacements:
>
> $$
> A \xrightarrow[R_4 - 2R_1,\ R_5 + 3R_1]{R_2 - 3R_1,\ R_3 - R_1}
> \begin{bmatrix} 2 & -4 & -2 & 3 \\ 0 & 3 & 1 & -1 \\ 0 & -3 & -1 & 6 \\ 0 & 6 & 2 & -7 \\ 0 & -9 & -3 & 13 \end{bmatrix}
> \xrightarrow[R_4 - 2R_2,\ R_5 + 3R_2]{R_3 + R_2}
> \begin{bmatrix} 2 & -4 & -2 & 3 \\ 0 & 3 & 1 & -1 \\ 0 & 0 & 0 & 5 \\ 0 & 0 & 0 & -5 \\ 0 & 0 & 0 & 10 \end{bmatrix}
> \xrightarrow[R_5 - 2R_3]{R_4 + R_3}
> \begin{bmatrix} 2 & -4 & -2 & 3 \\ 0 & 3 & 1 & -1 \\ 0 & 0 & 0 & 5 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} = U .
> $$
>
> Column 3 has no pivot; the third pivot is the $5$ in column 4. The pivot columns give
>
> $$
> \begin{bmatrix} 2 \\ 6 \\ 2 \\ 4 \\ -6 \end{bmatrix} \div 2 = \begin{bmatrix} 1 \\ 3 \\ 1 \\ 2 \\ -3 \end{bmatrix}, \qquad
> \begin{bmatrix} 3 \\ -3 \\ 6 \\ -9 \end{bmatrix} \div 3 = \begin{bmatrix} 1 \\ -1 \\ 2 \\ -3 \end{bmatrix}, \qquad
> \begin{bmatrix} 5 \\ -5 \\ 10 \end{bmatrix} \div 5 = \begin{bmatrix} 1 \\ -1 \\ 2 \end{bmatrix} .
> $$
>
> These fill only the first three columns of the $5 \times 5$ matrix $L$; the last two columns come from $I_5$:
>
> $$
> L = \begin{bmatrix} 1 & 0 & 0 & 0 & 0 \\ 3 & 1 & 0 & 0 & 0 \\ 1 & -1 & 1 & 0 & 0 \\ 2 & 2 & -1 & 1 & 0 \\ -3 & -3 & 2 & 0 & 1 \end{bmatrix}, \qquad
> U = \begin{bmatrix} 2 & -4 & -2 & 3 \\ 0 & 3 & 1 & -1 \\ 0 & 0 & 0 & 5 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> Check, row 5 of $LU$: $-3(2, -4, -2, 3) - 3(0, 3, 1, -1) + 2(0, 0, 0, 5) = (-6, 12 - 9, 6 - 3, -9 + 3 + 10) = (-6, 3, 3, 4)$.
>
> *Lay: Practice Problem 2.5*

^ex-15-3

> [!remark] Remark: Permuted LU Factorizations
> In practical work row interchanges are nearly always needed, because *partial pivoting* (choosing, among the possible pivots in a column, an entry of largest absolute value) is used for accuracy. The algorithm is then modified to produce an $L$ that is **permuted lower triangular**: a rearrangement (permutation) of its rows makes it unit lower triangular. The resulting **permuted LU factorization** solves $A\mathbf{x} = \mathbf{b}$ as before, except that the reduction of $[\,L \ \ \mathbf{b}\,]$ to $[\,I \ \ \mathbf{y}\,]$ follows the order of the pivots in $L$, from left to right, starting with the pivot in the first column. "LU factorization" usually includes this possibility. In matrix terms, a permutation matrix $P$ ([[§12 The Inverse of a Matrix#^def-12-4|Definition §12.4]]) puts the rows in order, $PA = L'U$ with $L'$ unit lower triangular; compare the lecture's description of row reduction as a product of replacement and permutation matrices ([[§12 The Inverse of a Matrix#^rem-12-2|§12, Remark: An Invertible Matrix Is a Product of Elementary Matrices]]).

^rem-15-3

> [!remark]- Remark: Numerical Notes — Operation Counts
> For an $n \times n$ dense matrix $A$ (most entries nonzero) with $n$ moderately large, say $n \ge 30$ (a *flop* is one $+$, $-$, $\times$ or $\div$):
> 1. Computing an LU factorization of $A$ takes about $2n^3/3$ flops (about the same as row reducing $[\,A \ \ \mathbf{b}\,]$), whereas finding $A^{-1}$ requires about $2n^3$ flops.
> 2. Solving $L\mathbf{y} = \mathbf{b}$ and $U\mathbf{x} = \mathbf{y}$ requires about $2n^2$ flops, because any $n \times n$ triangular system can be solved in about $n^2$ flops.
> 3. Multiplying $\mathbf{b}$ by $A^{-1}$ also takes about $2n^2$ flops, but the result may be less accurate than the one obtained from $L$ and $U$, because of roundoff in computing both $A^{-1}$ and $A^{-1}\mathbf{b}$.
> 4. If $A$ is sparse (mostly zero entries), then $L$ and $U$ may be sparse too, whereas $A^{-1}$ is likely to be dense. Then solving $A\mathbf{x} = \mathbf{b}$ with an LU factorization is *much* faster than using $A^{-1}$.

^rem-15-4

## A Matrix Factorization in Electrical Engineering

> [!definition] Definition §15.2: Transfer Matrix; Series and Shunt Circuits
> Consider an electric circuit with input and output terminals. Record the input voltage and current by $\begin{bmatrix} v_1 \\ i_1 \end{bmatrix}$ (volts, amps) and the output voltage and current by $\begin{bmatrix} v_2 \\ i_2 \end{bmatrix}$. If the transformation $\begin{bmatrix} v_1 \\ i_1 \end{bmatrix} \mapsto \begin{bmatrix} v_2 \\ i_2 \end{bmatrix}$ is linear, its matrix $A$, with
>
> $$
> \begin{bmatrix} v_2 \\ i_2 \end{bmatrix} = A\begin{bmatrix} v_1 \\ i_1 \end{bmatrix},
> $$
>
> is the **transfer matrix** of the circuit. A **ladder network** connects circuits in series, so that the output of one is the input of the next. A **series circuit** has one resistor $R_1$ (ohms) in the line; a **shunt circuit** has one resistor $R_2$ across the two lines. By Ohm's law and Kirchhoff's laws, their transfer matrices are
>
> $$
> \underbrace{\begin{bmatrix} 1 & -R_1 \\ 0 & 1 \end{bmatrix}}_{\text{series circuit}} \qquad\text{and}\qquad \underbrace{\begin{bmatrix} 1 & 0 \\ -1/R_2 & 1 \end{bmatrix}}_{\text{shunt circuit}} .
> $$
>
> *Lay: 2.5 (text)*

^def-15-2

> [!example] Example §15.4: Designing a Ladder Network
> **(a)** Compute the transfer matrix of the ladder network formed by a series circuit (resistance $R_1$) followed by a shunt circuit (resistance $R_2$).
>
> Let $A_1$ and $A_2$ be the transfer matrices of the series and shunt circuits. An input vector $\mathbf{x}$ is transformed first into $A_1\mathbf{x}$ and then into $A_2(A_1\mathbf{x})$. Connecting circuits in series is composing linear transformations, so the transfer matrix of the network is (note the order)
>
> $$
> A_2A_1 = \begin{bmatrix} 1 & 0 \\ -1/R_2 & 1 \end{bmatrix}\begin{bmatrix} 1 & -R_1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & -R_1 \\ -1/R_2 & 1 + R_1/R_2 \end{bmatrix} . \tag{5}
> $$
>
> **(b)** Design a ladder network whose transfer matrix is $\begin{bmatrix} 1 & -8 \\ -.5 & 5 \end{bmatrix}$.
>
> Factor this matrix as in (5): find $R_1$, $R_2$ with
>
> $$
> \begin{bmatrix} 1 & -R_1 \\ -1/R_2 & 1 + R_1/R_2 \end{bmatrix} = \begin{bmatrix} 1 & -8 \\ -.5 & 5 \end{bmatrix} .
> $$
>
> The $(1, 2)$-entries give $R_1 = 8$ ohms, and the $(2, 1)$-entries give $1/R_2 = .5$, so $R_2 = 1/.5 = 2$ ohms. Then the $(2, 2)$-entry is $1 + 8/2 = 5$, as required, so the network of (a) with these resistances has the desired transfer matrix.
>
> A transfer matrix summarizes the input–output behavior of a network (its design specifications) without reference to its interior. To build a network with specified properties, an engineer first determines whether such a network can be constructed (realized), and then tries to factor the transfer matrix into matrices of smaller circuits that may already be manufactured. For alternating current, the entries are usually rational complex-valued functions. A standard problem is to find a *minimal realization*, using the smallest number of electrical components.
>
> *Lay: Example 2.5.3*

^ex-15-4
