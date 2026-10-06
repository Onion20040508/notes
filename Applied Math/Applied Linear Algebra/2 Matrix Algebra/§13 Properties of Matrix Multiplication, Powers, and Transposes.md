---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 2
section: 13
lay: "2.1"
aliases: ["Lay 2.1 (cont.)"]
tags: [applied-linear-algebra, math235]
---
← [[§12 Matrix Operations]] · ↑ [[· 2 Matrix Algebra]] · [[§14 The Inverse of a Matrix]] →

*Lay, Section 2.1 · MATH 235 lectures L6, L7.*

Matrices can be added, scaled and multiplied, and these operations obey most of the rules of ordinary algebra. Three rules of number algebra fail for matrices ($AB \ne BA$ in general, no cancellation, $AB = 0$ without $A = 0$ or $B = 0$). The section ends with powers $A^k$ and the transpose $A^T$, whose key rule $(AB)^T = B^TA^T$ reverses the order of the factors.

## Properties of Matrix Multiplication

> [!theorem] Theorem §13.1: Properties of Matrix Multiplication
> Let $A$ be an $m \times n$ matrix, and let $B$ and $C$ have sizes for which the indicated sums and products are defined.
>
> a. $A(BC) = (AB)C$ (associative law of multiplication)
> b. $A(B + C) = AB + AC$ (left distributive law)
> c. $(B + C)A = BA + CA$ (right distributive law)
> d. $r(AB) = (rA)B = A(rB)$ for any scalar $r$
> e. $I_mA = A = AI_n$ (identity for matrix multiplication)
>
> *Lay: Theorem 2 (2.1)*

^thm-13-1

> [!proof]+ Proof
> **(a)** Let $C = [\,\mathbf{c}_1 \ \cdots \ \mathbf{c}_p\,]$. By [[§12 Matrix Operations#^def-12-5|Definition §12.5]], $BC = [\,B\mathbf{c}_1 \ \cdots \ B\mathbf{c}_p\,]$, and again by the definition,
>
> $$
> A(BC) = \begin{bmatrix} A(B\mathbf{c}_1) & \cdots & A(B\mathbf{c}_p) \end{bmatrix} = \begin{bmatrix} (AB)\mathbf{c}_1 & \cdots & (AB)\mathbf{c}_p \end{bmatrix} = (AB)C,
> $$
>
> using equation (1) of [[§12 Matrix Operations#^thm-12-2|Theorem §12.2]] for each column. (Lay also notes a second proof: matrix multiplication corresponds to composition of functions, and composition of functions is associative.)
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

^pf-13-1

*Uses:* [[§12 Matrix Operations#^def-12-5|Def. §12.5]], [[§12 Matrix Operations#^thm-12-2|§12.2]], [[§12 Matrix Operations#^prop-12-4|§12.4]], [[§5 The Matrix Equation Ax = b#^def-5-1|Def. §5.1]], [[§5 The Matrix Equation Ax = b#^def-5-4|Def. §5.4]] ($I_m\mathbf{x} = \mathbf{x}$)

> [!remark]- Connections
> - Rigorous treatment: the same laws for linear maps between any vector spaces, [[§7 Vector Space of Linear Maps#^ladr-3-8|LADR 3.8]] (associativity, identity, distributivity); they transfer to matrices through $\mathcal{M}(ST) = \mathcal{M}(S)\mathcal{M}(T)$. Associativity of composition of arbitrary functions: [[§8 Functions#^prop-8-1|250 Prop. §8.1]], which is Lay's second proof of (a).

The associative and distributive laws say that parentheses can be inserted and removed as in number algebra: $ABC$ means either $A(BC)$ or $(AB)C$, and $ABCD$ can be computed as $A(BCD)$, $(ABC)D$, $A(BC)D$ and so on, *as long as the left-to-right order of the factors is kept*. (When $B$ is square and $C$ has fewer columns than $A$ has rows, $A(BC)$ is cheaper to compute than $(AB)C$.)

> [!definition] Definition §13.1: Commuting Matrices
> In the product $AB$, $A$ is **right-multiplied** by $B$ and $B$ is **left-multiplied** by $A$. If $AB = BA$, then $A$ and $B$ **commute** with one another.
>
> *Lay: 2.1 (text)*

^def-13-1

> [!remark] Remark: Warnings
> Three rules of number algebra fail for matrices:
> 1. In general, $AB \ne BA$.
> 2. The cancellation laws do not hold: $AB = AC$ does not in general imply $B = C$.
> 3. If $AB$ is the zero matrix, one cannot conclude in general that $A = 0$ or $B = 0$.
>
> The first is no surprise: the columns of $AB$ are combinations of the columns of $A$, while the columns of $BA$ are built from the columns of $B$. [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^ex-13-1|Example §13.1]] shows all three.

^rem-13-1
> [!example] Example §13.1: Matrices That Do Not Commute, and Zero Divisors
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
> and $R_{\theta + \varphi} = R_{\varphi + \theta} = R_\varphi R_\theta$: rotating through $\varphi$ and then through $\theta$ is rotating through $\theta + \varphi$, in either order. (The lecture adds that the matrices $\begin{bmatrix} a & -b \\ b & a \end{bmatrix}$ also commute with each other; they multiply like the complex numbers $a + bi$, see [[§64 Complex Numbers#^rem-64-3|§64, Remark: Complex Numbers as 2 × 2 Matrices]].)
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

^ex-13-1

![[m235-11-1.svg]]
*[[§13 Properties of Matrix Multiplication, Powers, and Transposes#^ex-13-1|Example §13.1]](b) with $\varphi = 50^\circ$. Top: project, then rotate ($R_\varphi P$): $\mathbf{e}_1$ is unchanged by $P$ and ends at $(\cos\varphi, \sin\varphi)$. Bottom: rotate, then project ($PR_\varphi$): $\mathbf{e}_1$ is rotated and then flattened to $(\cos\varphi, 0)$. The two composites send $\mathbf{e}_1$ to different vectors, so $R_\varphi P \ne PR_\varphi$.*

## Powers of a Matrix

> [!definition] Definition §13.2: Powers of a Matrix
> If $A$ is an $n \times n$ matrix and $k$ is a positive integer, $A^k$ denotes the product of $k$ copies of $A$:
>
> $$
> A^k = \underbrace{A \cdots A}_{k} .
> $$
>
> $A^k\mathbf{x}$ is the result of left-multiplying $\mathbf{x}$ by $A$ repeatedly $k$ times. For $k = 0$, $A^0\mathbf{x}$ should be $\mathbf{x}$ itself, so $A^0$ is interpreted as the identity matrix $I_n$.
>
> *Lay: 2.1 (text)*

^def-13-2

> [!example] Example §13.2: Computing Powers
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

^ex-13-2

> [!remark]- Remark: Computing a Power Times a Vector
> To compute $A^2\mathbf{x}$ for a $4 \times 4$ matrix $A$, compute $A(A\mathbf{x})$: $A\mathbf{x}$ takes 16 multiplications (4 for each entry) and $A(A\mathbf{x})$ 16 more, 32 in all. Forming $A^2$ first takes 64 multiplications (4 for each of 16 entries), and then $A^2\mathbf{x}$ takes 16 more, 80 in all. (Lay's Practice Problem 2.)

^rem-13-2
## The Transpose of a Matrix

> [!definition] Definition §13.3: Transpose
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

^def-13-3

> [!theorem] Theorem §13.2: Properties of the Transpose
> Let $A$ and $B$ denote matrices whose sizes are appropriate for the following sums and products.
>
> $$
> \text{(a) } (A^T)^T = A \qquad \text{(b) } (A + B)^T = A^T + B^T \qquad \text{(c) } (rA)^T = rA^T \text{ for any scalar } r \qquad \text{(d) } (AB)^T = B^TA^T
> $$
>
> Usually $(AB)^T \ne A^TB^T$, even when $A^TB^T$ is defined.
>
> *Lay: Theorem 3 (2.1)*

^thm-13-2

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

^pf-13-2

*Uses:* [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^def-13-3|Def. §13.3]], [[§12 Matrix Operations#^prop-12-4|§12.4]]

> [!remark]- Connections
> - Rigorous treatment: [[§9 Matrices#^ladr-3-54|LADR 3.54]] (transpose and its properties, including $(AC)^t = C^tA^t$). In LADR the transpose is the matrix of the dual map ([[§12 Duality#^ladr-3-118|LADR 3.118]], [[§12 Duality#^ladr-3-132|LADR 3.132]]), which explains why it reverses the order of products: $(ST)' = T'S'$, [[§12 Duality#^ladr-3-120|LADR 3.120]](c).

> [!theorem] Corollary §13.3: Transpose of a Product of Several Matrices
> The transpose of a product of matrices equals the product of their transposes in the *reverse* order:
>
> $$
> (A_1A_2 \cdots A_k)^T = A_k^T \cdots A_2^TA_1^T .
> $$
>
> *Lay: 2.1 (text)*

^cor-13-3

> [!proof]+ Proof
> Induction on $k$; the case $k = 2$ is [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^thm-13-2|Theorem §13.2]](d). If the formula holds for $k - 1$ factors, then by (d) applied to $A_1 \cdots A_{k-1}$ and $A_k$,
>
> $$
> (A_1 \cdots A_{k-1}A_k)^T = A_k^T(A_1 \cdots A_{k-1})^T = A_k^TA_{k-1}^T \cdots A_1^T .
> $$

^pf-13-3

*Uses:* [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^thm-13-2|§13.2]], [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^thm-13-1|§13.1]] (associativity)

> [!example] Example §13.3: Transposes and Matrix Equations
> **(a)** Simplify $(A - 3B^2)^T$ for $n \times n$ matrices $A$ and $B$. By [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^thm-13-2|Theorem §13.2]](b), (c) and [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^cor-13-3|Corollary §13.3]],
>
> $$
> (A - 3B^2)^T = A^T + (-3BB)^T = A^T - 3(BB)^T = A^T - 3B^TB^T = A^T - 3(B^T)^2 .
> $$
>
> **(b)** Given $B = 2A - 3C^T$, find $A$, for $B = \begin{bmatrix} 1 & 0 \\ 4 & -2 \end{bmatrix}$ and $C = \begin{bmatrix} 1 & 2 \\ -1 & 3 \end{bmatrix}$. The rules of [[§12 Matrix Operations#^thm-12-1|Theorem §12.1]] allow solving as for numbers: $2A = B + 3C^T$, so $A = \tfrac12(B + 3C^T)$. Here
>
> $$
> C^T = \begin{bmatrix} 1 & -1 \\ 2 & 3 \end{bmatrix}, \qquad B + 3C^T = \begin{bmatrix} 1 + 3 & 0 - 3 \\ 4 + 6 & -2 + 9 \end{bmatrix} = \begin{bmatrix} 4 & -3 \\ 10 & 7 \end{bmatrix}, \qquad A = \begin{bmatrix} 2 & -3/2 \\ 5 & 7/2 \end{bmatrix} .
> $$
>
> Check: $2A - 3C^T = \begin{bmatrix} 4 & -3 \\ 10 & 7 \end{bmatrix} - \begin{bmatrix} 3 & -3 \\ 6 & 9 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 4 & -2 \end{bmatrix} = B$.
>
> **(c)** Vectors are $n \times 1$ matrices, so [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^thm-13-2|Theorem §13.2]] applies to them. For $A = \begin{bmatrix} 1 & -3 \\ -2 & 4 \end{bmatrix}$ and $\mathbf{x} = \begin{bmatrix} 5 \\ 3 \end{bmatrix}$: $A\mathbf{x} = \begin{bmatrix} 5 - 9 \\ -10 + 12 \end{bmatrix} = \begin{bmatrix} -4 \\ 2 \end{bmatrix}$, so $(A\mathbf{x})^T = \begin{bmatrix} -4 & 2 \end{bmatrix}$, and indeed
>
> $$
> \mathbf{x}^TA^T = \begin{bmatrix} 5 & 3 \end{bmatrix}\begin{bmatrix} 1 & -2 \\ -3 & 4 \end{bmatrix} = \begin{bmatrix} 5 - 9 & -10 + 12 \end{bmatrix} = \begin{bmatrix} -4 & 2 \end{bmatrix} .
> $$
>
> Also $\mathbf{x}\mathbf{x}^T = \begin{bmatrix} 25 & 15 \\ 15 & 9 \end{bmatrix}$ and $\mathbf{x}^T\mathbf{x} = [\,25 + 9\,] = 34$, while $A^T\mathbf{x}^T$ is not defined ($\mathbf{x}^T$ has one row, $A^T$ has two columns).
>
> *Lay: 2.1, Practice Problem 1*
> *Source: 235 checklist (2.1)*

^ex-13-3

> [!remark] Remark: Inner and Outer Products
> For $\mathbf{u}$, $\mathbf{v}$ in $\mathbb{R}^n$ (as $n \times 1$ matrices), the $1 \times 1$ matrix $\mathbf{u}^T\mathbf{v} = u_1v_1 + \cdots + u_nv_n$ is the **scalar product** or **inner product** of $\mathbf{u}$ and $\mathbf{v}$, written as a number ([[§49 Inner Product, Length, and Orthogonality#^def-49-1|Definition §49.1]]). The $n \times n$ matrix $\mathbf{u}\mathbf{v}^T$ is their **outer product**. By [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^thm-13-2|Theorem §13.2]](d), $\mathbf{v}^T\mathbf{u} = (\mathbf{u}^T\mathbf{v})^T = \mathbf{u}^T\mathbf{v}$ and $\mathbf{v}\mathbf{u}^T = (\mathbf{u}\mathbf{v}^T)^T$. Outer products reappear in the column–row expansion of $AB$ ([[§17 Partitioned Matrices#^thm-17-3|Theorem §17.3]]) and in [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^ex-13-2|Example §13.2]](b). (Lay's Exercises 27–28.)

^rem-13-3
> [!remark]- Remark: Numerical Notes
> 1. The fastest way to compute $AB$ on a computer depends on how matrices are stored. The standard high-performance algorithms, such as those in LAPACK, compute $AB$ by columns, as in [[§12 Matrix Operations#^def-12-5|Definition §12.5]] (a C++ version computes it by rows).
> 2. The column definition suits parallel processing: the columns of $B$ are assigned to different processors, which compute the corresponding columns of $AB$ independently and simultaneously.

^rem-13-4