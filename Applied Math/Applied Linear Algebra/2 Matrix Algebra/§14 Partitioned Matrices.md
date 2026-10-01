---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 2
section: 14
lay: "2.4"
aliases: ["Lay 2.4"]
tags: [applied-linear-algebra, math235]
---
← [[§13 Characterizations of Invertible Matrices]] · ↑ [[· 2 Matrix Algebra]] · [[§15 Matrix Factorizations]] →

*Lay, Section 2.4.*

Viewing a matrix as a list of columns has been so useful that it pays to cut matrices into other rectangular pieces, or blocks. Partitioned matrices are added, scaled and multiplied block by block, as if the blocks were numbers, provided the partitions match and the order of factors inside each block product is kept. The most general view of a product is then the column–row expansion: $AB$ is the sum of the outer products (column $k$ of $A$)(row $k$ of $B$). Block equations also give inverses of structured matrices, such as block upper triangular ones. Partitions appear throughout modern applications, both to expose structure and to let computers work on a few blocks at a time.

## Partitioned Matrices

> [!definition] Definition §14.1: Partitioned (Block) Matrix
> A **partition** of a matrix $A$ divides it by horizontal and vertical rules into rectangular **blocks** (submatrices). Written in terms of its blocks, $A$ is a **partitioned** or **block matrix**; for instance a $2 \times 3$ block matrix is
>
> $$
> A = \begin{bmatrix} A_{11} & A_{12} & A_{13} \\ A_{21} & A_{22} & A_{23} \end{bmatrix} .
> $$
>
> The blocks in a block row have the same number of rows, and the blocks in a block column have the same number of columns.
>
> *Lay: 2.4 (text)*

^def-14-1

> [!example] Example §14.1: A Partition into Six Blocks
> The $3 \times 6$ matrix
>
> $$
> A = \left[\begin{array}{ccc|cc|c} 3 & 0 & -1 & 5 & 9 & -2 \\ -5 & 2 & 4 & 0 & -3 & 1 \\ \hline -8 & -6 & 3 & 1 & 7 & -4 \end{array}\right]
> $$
>
> is the $2 \times 3$ block matrix $\begin{bmatrix} A_{11} & A_{12} & A_{13} \\ A_{21} & A_{22} & A_{23} \end{bmatrix}$ with blocks
>
> $$
> A_{11} = \begin{bmatrix} 3 & 0 & -1 \\ -5 & 2 & 4 \end{bmatrix}, \quad A_{12} = \begin{bmatrix} 5 & 9 \\ 0 & -3 \end{bmatrix}, \quad A_{13} = \begin{bmatrix} -2 \\ 1 \end{bmatrix},
> $$
>
> $$
> A_{21} = \begin{bmatrix} -8 & -6 & 3 \end{bmatrix}, \quad A_{22} = \begin{bmatrix} 1 & 7 \end{bmatrix}, \quad A_{23} = \begin{bmatrix} -4 \end{bmatrix} .
> $$
>
> Partitions also arise from the structure of a model. The matrix of a circuit board built mainly from three microchips might be a $3 \times 3$ block matrix $[\,A_{ij}\,]$ whose diagonal blocks $A_{11}$, $A_{22}$, $A_{33}$ describe the three chips and whose other blocks describe the interconnections between them.
>
> *Lay: Examples 2.4.1 and 2.4.2*

^ex-14-1

> [!theorem] Proposition §14.1: Sums and Scalar Multiples Block by Block
> If $A$ and $B$ are the same size and are partitioned in exactly the same way, then $A + B$, partitioned the same way, has as blocks the (matrix) sums of the corresponding blocks of $A$ and $B$. A scalar multiple $rA$ is also computed block by block: its blocks are $r$ times the blocks of $A$.
>
> *Lay: 2.4 (text)*

^prop-14-1

> [!proof]+ Proof
> Matrices are added and scaled entry by entry (Definition §11.2), and each block of $A + B$ consists of the entries of $A + B$ in certain positions, which are the sums of the entries of $A$ and $B$ in the same positions, that is, of the corresponding blocks. The same argument applies to $rA$.

^pf-14-1

*Uses:* [[§11 Matrix Operations#^def-11-2|Def. §11.2]]

## Multiplication of Partitioned Matrices

> [!definition] Definition §14.2: Conformable Partitions
> Partitions of $A$ and $B$ are **conformable for block multiplication** if the column partition of $A$ matches the row partition of $B$: the columns of $A$ are divided into groups of sizes $n_1, \ldots, n_r$ (left to right), and the rows of $B$ into groups of the same sizes $n_1, \ldots, n_r$ (top to bottom).
>
> *Lay: 2.4 (text)*

^def-14-2

> [!theorem] Proposition §14.2: Block Multiplication
> If the partitions of $A$ and $B$ are conformable for block multiplication, then $AB$ can be computed by the usual row–column rule as if the blocks were scalars: with $A = [\,A_{st}\,]$ and $B = [\,B_{tu}\,]$ ($t = 1, \ldots, r$), the $(s, u)$-block of $AB$ is
>
> $$
> (AB)_{su} = A_{s1}B_{1u} + A_{s2}B_{2u} + \cdots + A_{sr}B_{ru} .
> $$
>
> In each block product, the block from $A$ must stay on the left, since matrix multiplication is not commutative.
>
> *Lay: 2.4 (text)*

^prop-14-2

*Lay omits the proof ("it can be shown"); the remark below gives the reason.*

> [!remark] Remark: Why It Works
> By the row–column rule, $(AB)_{ij} = \sum_{k=1}^n a_{ik}b_{kj}$. Split this sum according to the groups of columns of $A$ (equivalently, rows of $B$): $\sum_{k} = \sum_{t=1}^r \sum_{k \in \text{group } t}$. If row $i$ lies in block row $s$ of $A$ and column $j$ in block column $u$ of $B$, then the inner sum $\sum_{k \in \text{group } t} a_{ik}b_{kj}$ is a row of $A_{st}$ times a column of $B_{tu}$, which is the corresponding entry of $A_{st}B_{tu}$. Adding over $t$, the entries of $AB$ in block $(s, u)$ are those of $\sum_t A_{st}B_{tu}$. Conformability is exactly what makes every product $A_{st}B_{tu}$ defined.

^rem-14-1

> [!example] Example §14.2: A Block Product
> Let
>
> $$
> A = \left[\begin{array}{ccc|cc} 2 & -3 & 1 & 0 & -4 \\ 1 & 5 & -2 & 3 & -1 \\ \hline 0 & -4 & -2 & 7 & -1 \end{array}\right] = \begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix}, \qquad
> B = \left[\begin{array}{cc} 6 & 4 \\ -2 & 1 \\ -3 & 7 \\ \hline -1 & 3 \\ 5 & 2 \end{array}\right] = \begin{bmatrix} B_1 \\ B_2 \end{bmatrix} .
> $$
>
> The 5 columns of $A$ are split $3 + 2$, and so are the 5 rows of $B$: the partitions are conformable, and
>
> $$
> AB = \begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix}\begin{bmatrix} B_1 \\ B_2 \end{bmatrix} = \begin{bmatrix} A_{11}B_1 + A_{12}B_2 \\ A_{21}B_1 + A_{22}B_2 \end{bmatrix} .
> $$
>
> **Top block.**
>
> $$
> A_{11}B_1 = \begin{bmatrix} 2 & -3 & 1 \\ 1 & 5 & -2 \end{bmatrix}\begin{bmatrix} 6 & 4 \\ -2 & 1 \\ -3 & 7 \end{bmatrix} = \begin{bmatrix} 12 + 6 - 3 & 8 - 3 + 7 \\ 6 - 10 + 6 & 4 + 5 - 14 \end{bmatrix} = \begin{bmatrix} 15 & 12 \\ 2 & -5 \end{bmatrix},
> $$
>
> $$
> A_{12}B_2 = \begin{bmatrix} 0 & -4 \\ 3 & -1 \end{bmatrix}\begin{bmatrix} -1 & 3 \\ 5 & 2 \end{bmatrix} = \begin{bmatrix} -20 & -8 \\ -3 - 5 & 9 - 2 \end{bmatrix} = \begin{bmatrix} -20 & -8 \\ -8 & 7 \end{bmatrix},
> $$
>
> so $A_{11}B_1 + A_{12}B_2 = \begin{bmatrix} -5 & 4 \\ -6 & 2 \end{bmatrix}$.
>
> **Bottom block.** $A_{21}B_1 = \begin{bmatrix} 0 + 8 + 6 & 0 - 4 - 14 \end{bmatrix} = \begin{bmatrix} 14 & -18 \end{bmatrix}$ and $A_{22}B_2 = \begin{bmatrix} -7 - 5 & 21 - 2 \end{bmatrix} = \begin{bmatrix} -12 & 19 \end{bmatrix}$, so $A_{21}B_1 + A_{22}B_2 = \begin{bmatrix} 2 & 1 \end{bmatrix}$. Altogether
>
> $$
> AB = \left[\begin{array}{cc} -5 & 4 \\ -6 & 2 \\ \hline 2 & 1 \end{array}\right] .
> $$
>
> *Lay: Example 2.4.3*

^ex-14-2

The row–column rule for block matrices is the most general way to view a product. Four views met so far are special partitions: (1) $A\mathbf{x}$ as a combination of the columns of $A$; (2) the column definition of $AB$; (3) the row–column rule for the entries of $AB$; (4) the rows of $AB$ as rows of $A$ times $B$. A fifth view uses $A$ partitioned into columns and $B$ into rows. Here $\operatorname{col}_k(A)$ is the $k$th column of $A$ and $\operatorname{row}_k(B)$ the $k$th row of $B$.

> [!theorem] Theorem §14.3: Column–Row Expansion of AB
> If $A$ is $m \times n$ and $B$ is $n \times p$, then
>
> $$
> AB = \begin{bmatrix} \operatorname{col}_1(A) & \operatorname{col}_2(A) & \cdots & \operatorname{col}_n(A) \end{bmatrix} \begin{bmatrix} \operatorname{row}_1(B) \\ \operatorname{row}_2(B) \\ \vdots \\ \operatorname{row}_n(B) \end{bmatrix} = \operatorname{col}_1(A)\operatorname{row}_1(B) + \cdots + \operatorname{col}_n(A)\operatorname{row}_n(B) . \tag{1}
> $$
>
> Each term is an $m \times p$ outer product ([[§11 Matrix Operations#^rem-11-4|§11, Remark: Inner and Outer Products]]).
>
> *Lay: Theorem 10 (2.4)*

^thm-14-3

> [!proof]+ Proof
> For each row index $i$ and column index $j$, the $(i, j)$-entry of $\operatorname{col}_k(A)\operatorname{row}_k(B)$ is the product of $a_{ik}$ from $\operatorname{col}_k(A)$ and $b_{kj}$ from $\operatorname{row}_k(B)$. Hence the $(i, j)$-entry of the sum in (1) is
>
> $$
> \underset{(k = 1)}{a_{i1}b_{1j}} + \underset{(k = 2)}{a_{i2}b_{2j}} + \cdots + \underset{(k = n)}{a_{in}b_{nj}},
> $$
>
> which is also the $(i, j)$-entry of $AB$, by the row–column rule.

^pf-14-3

*Uses:* [[§11 Matrix Operations#^prop-11-4|§11.4]]

> [!example] Example §14.3: A Product as a Sum of Outer Products
> Let $A = \begin{bmatrix} -3 & 1 & 2 \\ 1 & -4 & 5 \end{bmatrix}$ and $B = \begin{bmatrix} a & b \\ c & d \\ e & f \end{bmatrix}$. Then
>
> $$
> \operatorname{col}_1(A)\operatorname{row}_1(B) = \begin{bmatrix} -3 \\ 1 \end{bmatrix}\begin{bmatrix} a & b \end{bmatrix} = \begin{bmatrix} -3a & -3b \\ a & b \end{bmatrix}, \qquad
> \operatorname{col}_2(A)\operatorname{row}_2(B) = \begin{bmatrix} 1 \\ -4 \end{bmatrix}\begin{bmatrix} c & d \end{bmatrix} = \begin{bmatrix} c & d \\ -4c & -4d \end{bmatrix},
> $$
>
> $$
> \operatorname{col}_3(A)\operatorname{row}_3(B) = \begin{bmatrix} 2 \\ 5 \end{bmatrix}\begin{bmatrix} e & f \end{bmatrix} = \begin{bmatrix} 2e & 2f \\ 5e & 5f \end{bmatrix} .
> $$
>
> Thus
>
> $$
> \sum_{k=1}^3 \operatorname{col}_k(A)\operatorname{row}_k(B) = \begin{bmatrix} -3a + c + 2e & -3b + d + 2f \\ a - 4c + 5e & b - 4d + 5f \end{bmatrix},
> $$
>
> which is $AB$ by the row–column rule. The $(1, 1)$-entry of $AB$ is the sum of the $(1, 1)$-entries of the three outer products, and so on.
>
> *Lay: Example 2.4.4*

^ex-14-3

## Inverses of Partitioned Matrices

> [!definition] Definition §14.3: Block Upper Triangular and Block Diagonal Matrices
> A partitioned matrix of the form
>
> $$
> A = \begin{bmatrix} A_{11} & A_{12} \\ 0 & A_{22} \end{bmatrix}
> $$
>
> with square diagonal blocks is **block upper triangular**. A **block diagonal matrix** is a partitioned matrix with zero blocks off the main diagonal (of blocks).
>
> *Lay: 2.4 (text)*

^def-14-3

> [!theorem] Proposition §14.4: Inverse of a Block Upper Triangular Matrix
> Let $A = \begin{bmatrix} A_{11} & A_{12} \\ 0 & A_{22} \end{bmatrix}$ with $A_{11}$ of size $p \times p$ and $A_{22}$ of size $q \times q$. If $A$ is invertible, then $A_{11}$ and $A_{22}$ are invertible and
>
> $$
> A^{-1} = \begin{bmatrix} A_{11} & A_{12} \\ 0 & A_{22} \end{bmatrix}^{-1} = \begin{bmatrix} A_{11}^{-1} & -A_{11}^{-1}A_{12}A_{22}^{-1} \\ 0 & A_{22}^{-1} \end{bmatrix} .
> $$
>
> Conversely, if $A_{11}$ and $A_{22}$ are invertible, then $A$ is invertible, with this inverse.
>
> *Lay: Example 2.4.5*

^prop-14-4

> [!proof]+ Proof
> Denote $A^{-1}$ by $B$ and partition $B$ like $A$, so that
>
> $$
> \begin{bmatrix} A_{11} & A_{12} \\ 0 & A_{22} \end{bmatrix}\begin{bmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{bmatrix} = \begin{bmatrix} I_p & 0 \\ 0 & I_q \end{bmatrix} . \tag{2}
> $$
>
> Computing the left side by block multiplication and equating blocks gives four equations:
>
> $$
> \begin{aligned}
> A_{11}B_{11} + A_{12}B_{21} &= I_p && (3) \\
> A_{11}B_{12} + A_{12}B_{22} &= 0 && (4) \\
> A_{22}B_{21} &= 0 && (5) \\
> A_{22}B_{22} &= I_q && (6)
> \end{aligned}
> $$
>
> By itself, (6) does not show that $A_{22}$ is invertible. But $A_{22}$ and $B_{22}$ are square, so by the Invertible Matrix Theorem (Corollary §13.2) equation (6) shows that $A_{22}$ is invertible and $B_{22} = A_{22}^{-1}$. Next, left-multiply (5) by $A_{22}^{-1}$: $B_{21} = A_{22}^{-1}0 = 0$, so (3) simplifies to $A_{11}B_{11} + 0 = I_p$. Since $A_{11}$ is square, this shows (Corollary §13.2 again) that $A_{11}$ is invertible and $B_{11} = A_{11}^{-1}$. Finally, (4) gives
>
> $$
> A_{11}B_{12} = -A_{12}B_{22} = -A_{12}A_{22}^{-1} \qquad\text{and}\qquad B_{12} = -A_{11}^{-1}A_{12}A_{22}^{-1} .
> $$
>
> **Converse.** (Not in Lay.) If $A_{11}$ and $A_{22}$ are invertible, call the displayed matrix $B$. Block multiplication gives
>
> $$
> AB = \begin{bmatrix} A_{11}A_{11}^{-1} & -A_{11}A_{11}^{-1}A_{12}A_{22}^{-1} + A_{12}A_{22}^{-1} \\ 0 & A_{22}A_{22}^{-1} \end{bmatrix} = \begin{bmatrix} I_p & 0 \\ 0 & I_q \end{bmatrix},
> $$
>
> so $A$ is invertible with $A^{-1} = B$ by Corollary §13.2.

^pf-14-4

*Uses:* [[§14 Partitioned Matrices#^prop-14-2|§14.2]], [[§13 Characterizations of Invertible Matrices#^cor-13-2|§13.2]]

> [!theorem] Proposition §14.5: Block Diagonal Matrices
> A block diagonal matrix (with square diagonal blocks) is invertible if and only if each block on the diagonal is invertible. Then its inverse is block diagonal, with the inverses of the diagonal blocks on the diagonal.
>
> *Lay: 2.4 (text)*

^prop-14-5

> [!proof]+ Proof
> (Lay leaves this to Exercises 13–14.) Two diagonal blocks: $A = \begin{bmatrix} A_{11} & 0 \\ 0 & A_{22} \end{bmatrix}$ is block upper triangular with $A_{12} = 0$, so by Proposition §14.4 it is invertible exactly when $A_{11}$ and $A_{22}$ are, and then $A^{-1} = \begin{bmatrix} A_{11}^{-1} & 0 \\ 0 & A_{22}^{-1} \end{bmatrix}$. With $k$ diagonal blocks, group the last $k - 1$ blocks into one block diagonal block $A'$ and use induction on $k$: $A = \begin{bmatrix} A_{11} & 0 \\ 0 & A' \end{bmatrix}$ is invertible iff $A_{11}$ and $A'$ are, and, by the induction hypothesis, $A'$ is invertible iff its $k - 1$ diagonal blocks are, with $A'^{-1}$ block diagonal with the inverses of those blocks on the diagonal. Then $A^{-1} = \begin{bmatrix} A_{11}^{-1} & 0 \\ 0 & A'^{-1} \end{bmatrix}$ has the stated form.

^pf-14-5

*Uses:* [[§14 Partitioned Matrices#^prop-14-4|§14.4]]

> [!example] Example §14.4: Two Block Computations
> **(a)** Show that $\begin{bmatrix} I & 0 \\ A & I \end{bmatrix}$ is invertible and find its inverse (here $A$ is $q \times p$, and the two identity blocks are $I_p$ and $I_q$, so the whole matrix is square).
>
> Try $\begin{bmatrix} I & 0 \\ -A & I \end{bmatrix}$: by block multiplication
>
> $$
> \begin{bmatrix} I & 0 \\ A & I \end{bmatrix}\begin{bmatrix} I & 0 \\ -A & I \end{bmatrix} = \begin{bmatrix} I \cdot I + 0(-A) & I \cdot 0 + 0 \cdot I \\ A \cdot I + I(-A) & A \cdot 0 + I \cdot I \end{bmatrix} = \begin{bmatrix} I & 0 \\ 0 & I \end{bmatrix} .
> $$
>
> The matrix is square, so by Corollary §13.2 it is invertible and its inverse is $\begin{bmatrix} I & 0 \\ -A & I \end{bmatrix}$: the block analogue of the inverse $E_{21}(-a)$ of a replacement matrix $E_{21}(a)$.
>
> **(b)** Compute $X^TX$ for $X = \begin{bmatrix} X_1 & X_2 \end{bmatrix}$ partitioned into two blocks of columns. The transpose of a partitioned matrix is the transposed array of transposed blocks, so $X^T = \begin{bmatrix} X_1^T \\ X_2^T \end{bmatrix}$, and
>
> $$
> X^TX = \begin{bmatrix} X_1^T \\ X_2^T \end{bmatrix}\begin{bmatrix} X_1 & X_2 \end{bmatrix} = \begin{bmatrix} X_1^TX_1 & X_1^TX_2 \\ X_2^TX_1 & X_2^TX_2 \end{bmatrix} .
> $$
>
> The partitions are conformable: the columns of $X^T$ and the rows of $X$ are each left as a single group, so this is a $2 \times 1$ block matrix times a $1 \times 2$ block matrix, and each block of the product is a single block product. (This matrix reappears in least squares, as the matrix $A^TA$ of the normal equations $A^TA\mathbf{x} = A^T\mathbf{b}$, [[§44 Least-Squares Problems#^def-44-2|Definition §44.2]].)
>
> *Lay: Practice Problems 2.4.1 and 2.4.2*

^ex-14-4

> [!remark]- Remark: Numerical Notes
> 1. When matrices are too large for a computer's high-speed memory, partitioning lets the computer work with only two or three submatrices at a time. One linear programming team partitioned a problem with 837 rows and more than 12,750,000 columns into 837 rows and 51 block columns; the solution took about 4 minutes on a Cray supercomputer.
> 2. Some high-speed computers, particularly those with vector pipeline architecture, perform matrix calculations more efficiently with algorithms that use partitioned matrices.
> 3. Professional software for high-performance numerical linear algebra, such as LAPACK, makes intensive use of partitioned matrix calculations.

^rem-14-2
