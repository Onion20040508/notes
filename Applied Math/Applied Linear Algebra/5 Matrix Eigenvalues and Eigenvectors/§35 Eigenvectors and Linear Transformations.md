---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 5
section: 35
lay: "5.4"
aliases: ["Lay 5.4"]
tags: [applied-linear-algebra, math235]
---
← [[§34 Diagonalization]] · ↑ [[· 5 Matrix Eigenvalues and Eigenvectors]] · [[§36 Complex Eigenvalues]] →

*Lay, Section 5.4 · MATH 235 lecture L20.*

This section reads the factorization $A = PDP^{-1}$ as a statement about linear transformations: $\mathbf{x} \mapsto A\mathbf{x}$ and $\mathbf{u} \mapsto D\mathbf{u}$ are the same transformation, described in two coordinate systems. To say this, any linear transformation $T$ between finite-dimensional spaces gets a matrix relative to chosen bases, by recording the coordinate vectors of the images of the basis vectors. For $T(\mathbf{x}) = A\mathbf{x}$ on $\mathbb{R}^n$ and the basis formed by the columns of $P$, that matrix is $P^{-1}AP$. So the matrices similar to $A$ are exactly the matrix representations of $\mathbf{x} \mapsto A\mathbf{x}$, and diagonalizing $A$ means finding a basis in which the representation is diagonal. When no such basis exists, a good basis can still make the matrix triangular (the Jordan form).

## The Matrix of a Linear Transformation

Let $V$ be an $n$-dimensional vector space, $W$ an $m$-dimensional vector space, and $T : V \to W$ a linear transformation. Choose (ordered) bases $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$ for $V$ and $\mathcal{C}$ for $W$. For $\mathbf{x}$ in $V$, the coordinate vector $[\mathbf{x}]_{\mathcal{B}}$ is in $\mathbb{R}^n$ and the coordinate vector $[T(\mathbf{x})]_{\mathcal{C}}$ of its image is in $\mathbb{R}^m$ ([[§26 Coordinate Systems#^def-26-1|Definition §26.1]]).

> [!theorem] Theorem §35.1: The Matrix for T Relative to B and C
> With $V$, $W$, $T$, $\mathcal{B}$, $\mathcal{C}$ as above, let
>
> $$
> M = \big[\, [T(\mathbf{b}_1)]_{\mathcal{C}} \;\; [T(\mathbf{b}_2)]_{\mathcal{C}} \;\; \cdots \;\; [T(\mathbf{b}_n)]_{\mathcal{C}} \,\big] . \qquad (4)
> $$
>
> Then for every $\mathbf{x}$ in $V$,
>
> $$
> [T(\mathbf{x})]_{\mathcal{C}} = M[\mathbf{x}]_{\mathcal{B}} . \qquad (3)
> $$
>
> So, as far as coordinate vectors are concerned, the action of $T$ on $\mathbf{x}$ is left-multiplication by $M$.
>
> *Lay: 5.4, Equations (3) and (4)*

^thm-35-1

> [!proof]+ Proof
> Let $\mathbf{x} = r_1\mathbf{b}_1 + \cdots + r_n\mathbf{b}_n$, so that $[\mathbf{x}]_{\mathcal{B}} = (r_1, \ldots, r_n)$. Since $T$ is linear,
>
> $$
> T(\mathbf{x}) = T(r_1\mathbf{b}_1 + \cdots + r_n\mathbf{b}_n) = r_1T(\mathbf{b}_1) + \cdots + r_nT(\mathbf{b}_n) . \qquad (1)
> $$
>
> The coordinate mapping $\mathbf{w} \mapsto [\mathbf{w}]_{\mathcal{C}}$ from $W$ to $\mathbb{R}^m$ is linear ([[§26 Coordinate Systems#^thm-26-3|Theorem §26.3]]), so (1) gives
>
> $$
> [T(\mathbf{x})]_{\mathcal{C}} = r_1[T(\mathbf{b}_1)]_{\mathcal{C}} + \cdots + r_n[T(\mathbf{b}_n)]_{\mathcal{C}} . \qquad (2)
> $$
>
> The right side of (2) is a linear combination of the columns of $M$ with weights $r_1, \ldots, r_n$, which is $M[\mathbf{x}]_{\mathcal{B}}$ by the definition of a matrix–vector product.

^pf-35-1

*Uses:* [[§26 Coordinate Systems#^thm-26-3|§26.3]] (the coordinate mapping is linear), [[§4 The Matrix Equation Ax = b#^def-4-1|Def. §4.1]] ($A\mathbf{x}$ as a combination of columns)

> [!definition] Definition §35.1: Matrix for T Relative to Bases
> The matrix $M$ of Theorem §35.1 is called the **matrix for $T$ relative to the bases $\mathcal{B}$ and $\mathcal{C}$**, a matrix representation of $T$. Its $j$th column is the $\mathcal{C}$-coordinate vector of the image of the $j$th basis vector $\mathbf{b}_j$.
>
> If $W = V$ and $\mathcal{C} = \mathcal{B}$, then $M$ is called the **matrix for $T$ relative to $\mathcal{B}$**, or simply the **$\mathcal{B}$-matrix for $T$**, and is denoted $[T]_{\mathcal{B}}$. It satisfies
>
> $$
> [T(\mathbf{x})]_{\mathcal{B}} = [T]_{\mathcal{B}}[\mathbf{x}]_{\mathcal{B}} \qquad \text{for all } \mathbf{x} \text{ in } V . \qquad (5)
> $$
>
> When $\mathcal{B}$ and $\mathcal{C}$ are bases of the same space $V$ and $T$ is the identity, $T(\mathbf{x}) = \mathbf{x}$, the matrix $M$ is the change-of-coordinates matrix $P_{\mathcal{C} \leftarrow \mathcal{B}}$ of [[§29 Change of Basis#^def-29-1|Definition §29.1]].
>
> *Lay: 5.4 (text)*

^def-35-1

> [!remark]- Connections
> - Rigorous treatment: [[§9 Matrices#^ladr-3-31|LADR 3.31]] (matrix of a linear map, $\mathcal{M}(T, (v), (w))$, column $k$ = coordinates of $Tv_k$) and, for operators, [[§16 Upper-Triangular Matrices#^ladr-5-35|LADR 5.35]]. Equation (3) is Axler's $\mathcal{M}(Tv) = \mathcal{M}(T)\mathcal{M}(v)$; Lay's $[\,\cdot\,]_{\mathcal{B}}$ is Axler's $\mathcal{M}(\,\cdot\,)$.

> [!example] Example §35.1: Reading Off the Matrix
> Suppose $\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2\}$ is a basis for $V$ and $\mathcal{C} = \{\mathbf{c}_1, \mathbf{c}_2, \mathbf{c}_3\}$ is a basis for $W$, and $T : V \to W$ is linear with
>
> $$
> T(\mathbf{b}_1) = 3\mathbf{c}_1 - 2\mathbf{c}_2 + 5\mathbf{c}_3, \qquad T(\mathbf{b}_2) = 4\mathbf{c}_1 + 7\mathbf{c}_2 - \mathbf{c}_3 .
> $$
>
> The $\mathcal{C}$-coordinate vectors of the images are $[T(\mathbf{b}_1)]_{\mathcal{C}} = (3, -2, 5)$ and $[T(\mathbf{b}_2)]_{\mathcal{C}} = (4, 7, -1)$, so the matrix for $T$ relative to $\mathcal{B}$ and $\mathcal{C}$ is the $3 \times 2$ matrix
>
> $$
> M = \begin{bmatrix} 3 & 4 \\ -2 & 7 \\ 5 & -1 \end{bmatrix} .
> $$
>
> *Lay: Example 5.4.1*

^ex-35-1

> [!example] Example §35.2: The Matrix of Differentiation
> $T : \mathbb{P}_2 \to \mathbb{P}_2$, $T(a_0 + a_1t + a_2t^2) = a_1 + 2a_2t$, is linear (it is differentiation). Find the $\mathcal{B}$-matrix for $T$ when $\mathcal{B} = \{1, t, t^2\}$, and verify (5).
>
> The images of the basis vectors are $T(1) = 0$ (the zero polynomial), $T(t) = 1$ (the constant polynomial $1$) and $T(t^2) = 2t$. Their $\mathcal{B}$-coordinate vectors, found by inspection, are the columns of $[T]_{\mathcal{B}}$:
>
> $$
> [T(1)]_{\mathcal{B}} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}, \quad [T(t)]_{\mathcal{B}} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \quad [T(t^2)]_{\mathcal{B}} = \begin{bmatrix} 0 \\ 2 \\ 0 \end{bmatrix}, \qquad [T]_{\mathcal{B}} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{bmatrix} .
> $$
>
> For a general $\mathbf{p}(t) = a_0 + a_1t + a_2t^2$,
>
> $$
> [T(\mathbf{p})]_{\mathcal{B}} = [a_1 + 2a_2t]_{\mathcal{B}} = \begin{bmatrix} a_1 \\ 2a_2 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{bmatrix}\begin{bmatrix} a_0 \\ a_1 \\ a_2 \end{bmatrix} = [T]_{\mathcal{B}}[\mathbf{p}]_{\mathcal{B}} .
> $$
>
> (The only eigenvalue of this triangular matrix is $0$, with eigenspace spanned by $(1, 0, 0)$, the constants: the polynomials whose derivative is $0 \cdot \mathbf{p}$. So differentiation on $\mathbb{P}_2$ is not diagonalizable.)
>
> *Lay: Example 5.4.2*

^ex-35-2

## Linear Transformations on ℝⁿ

In applied problems a linear transformation of $\mathbb{R}^n$ usually appears first as a matrix transformation $\mathbf{x} \mapsto A\mathbf{x}$. If $A$ is diagonalizable, there is a basis of $\mathbb{R}^n$ consisting of eigenvectors of $A$, and the matrix of $\mathbf{x} \mapsto A\mathbf{x}$ in that basis is diagonal.

> [!theorem] Theorem §35.2: Diagonal Matrix Representation
> Suppose $A = PDP^{-1}$, where $D$ is a diagonal $n \times n$ matrix. If $\mathcal{B}$ is the basis for $\mathbb{R}^n$ formed from the columns of $P$, then $D$ is the $\mathcal{B}$-matrix for the transformation $\mathbf{x} \mapsto A\mathbf{x}$.
>
> More generally, for *any* basis $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$ of $\mathbb{R}^n$ and $P = [\,\mathbf{b}_1 \; \cdots \; \mathbf{b}_n\,]$, the $\mathcal{B}$-matrix of $T(\mathbf{x}) = A\mathbf{x}$ is
>
> $$
> [T]_{\mathcal{B}} = P^{-1}AP . \qquad (6)
> $$
>
> *Lay: Theorem 8 (5.4); 5.4 (text, "Similarity of Matrix Representations")*

^thm-35-2

> [!proof]+ Proof
> Denote the columns of $P$ by $\mathbf{b}_1, \ldots, \mathbf{b}_n$, so that $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$ and $P = [\,\mathbf{b}_1 \; \cdots \; \mathbf{b}_n\,]$. Then $P$ is the change-of-coordinates matrix $P_{\mathcal{B}}$ of [[§26 Coordinate Systems#^def-26-2|Definition §26.2]], and by [[§26 Coordinate Systems#^prop-26-2|Proposition §26.2]]
>
> $$
> P[\mathbf{x}]_{\mathcal{B}} = \mathbf{x} \qquad \text{and} \qquad [\mathbf{x}]_{\mathcal{B}} = P^{-1}\mathbf{x} .
> $$
>
> If $T(\mathbf{x}) = A\mathbf{x}$ for $\mathbf{x}$ in $\mathbb{R}^n$, then
>
> $$
> \begin{aligned}
> [T]_{\mathcal{B}} &= \big[\, [T(\mathbf{b}_1)]_{\mathcal{B}} \;\; \cdots \;\; [T(\mathbf{b}_n)]_{\mathcal{B}} \,\big] && \text{definition of } [T]_{\mathcal{B}} \\
> &= \big[\, [A\mathbf{b}_1]_{\mathcal{B}} \;\; \cdots \;\; [A\mathbf{b}_n]_{\mathcal{B}} \,\big] && \text{since } T(\mathbf{x}) = A\mathbf{x} \\
> &= \big[\, P^{-1}A\mathbf{b}_1 \;\; \cdots \;\; P^{-1}A\mathbf{b}_n \,\big] && \text{change of coordinates} \\
> &= P^{-1}A\,[\,\mathbf{b}_1 \;\; \cdots \;\; \mathbf{b}_n\,] && \text{matrix multiplication} \\
> &= P^{-1}AP . && (6)
> \end{aligned}
> $$
>
> This proves (6), and it used nothing about $D$. If $A = PDP^{-1}$, then $[T]_{\mathcal{B}} = P^{-1}AP = P^{-1}PDP^{-1}P = D$.

^pf-35-2

*Uses:* [[§35 Eigenvectors and Linear Transformations#^def-35-1|Def. §35.1]], [[§26 Coordinate Systems#^prop-26-2|§26.2]] (the change-of-coordinates equation), [[§11 Matrix Operations#^def-11-3|Def. §11.3]] (the product $AB$ column by column)

For example, $A = \begin{bmatrix} 7 & 2 \\ -4 & 1 \end{bmatrix} = PDP^{-1}$ with $P = \begin{bmatrix} 1 & 1 \\ -1 & -2 \end{bmatrix}$, $D = \begin{bmatrix} 5 & 0 \\ 0 & 3 \end{bmatrix}$ ([[§34 Diagonalization#^ex-34-1|Example §34.1]]). The columns $\mathbf{b}_1 = (1, -1)$, $\mathbf{b}_2 = (1, -2)$ of $P$ are eigenvectors of $A$, and by Theorem §35.2, $D$ is the $\mathcal{B}$-matrix of $T(\mathbf{x}) = A\mathbf{x}$ for $\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2\}$. The mappings $\mathbf{x} \mapsto A\mathbf{x}$ and $\mathbf{u} \mapsto D\mathbf{u}$ describe the same linear transformation, relative to different bases (Lay, Example 5.4.3).

## Similarity of Matrix Representations

Formula (6) holds for any basis. So if $A$ is similar to a matrix $C$, $A = PCP^{-1}$, then $C$ is the $\mathcal{B}$-matrix of $\mathbf{x} \mapsto A\mathbf{x}$ for the basis $\mathcal{B}$ formed by the columns of $P$. In a diagram, going around either way gives the same result:

$$
\begin{array}{ccc}
\mathbf{x} & \xrightarrow{\ \text{multiplication by } A\ } & A\mathbf{x} \\[2pt]
{\scriptstyle P^{-1}}\big\downarrow & & \big\uparrow{\scriptstyle P} \\[2pt]
[\mathbf{x}]_{\mathcal{B}} & \xrightarrow{\ \text{multiplication by } C\ } & [A\mathbf{x}]_{\mathcal{B}}
\end{array}
$$

Conversely, for any basis $\mathcal{B}$ of $\mathbb{R}^n$, the $\mathcal{B}$-matrix $P^{-1}AP$ is similar to $A$. Thus **the set of all matrices similar to $A$ coincides with the set of all matrix representations of the transformation $\mathbf{x} \mapsto A\mathbf{x}$**. This is why similar matrices share everything that belongs to the transformation rather than to the coordinates: the characteristic polynomial ([[§33 The Characteristic Equation#^thm-33-6|Theorem §33.6]]), the eigenvalues, the dimensions of the eigenspaces ([[§33 The Characteristic Equation#^prop-33-7|Proposition §33.7]]) and diagonalizability.

> [!remark]- Connections
> - Rigorous treatment: formula (6) is the change-of-basis formula [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]] ($A = C^{-1}BC$, with $C = \mathcal{M}(I, (u), (v))$ the matrix that converts $u$-coordinates into $v$-coordinates); Axler's Example 3.83 is the same computation with $\mathcal{B} = \{(4, 2), (5, 3)\}$.

> [!example] Example §35.3: A Triangular Representation (Jordan Form)
> Let $A = \begin{bmatrix} 4 & -9 \\ 4 & -8 \end{bmatrix}$, $\mathbf{b}_1 = \begin{bmatrix} 3 \\ 2 \end{bmatrix}$, $\mathbf{b}_2 = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$. The characteristic polynomial of $A$ is $(4 - \lambda)(-8 - \lambda) + 36 = \lambda^2 + 4\lambda + 4 = (\lambda + 2)^2$, but
>
> $$
> A + 2I = \begin{bmatrix} 6 & -9 \\ 4 & -6 \end{bmatrix} \sim \begin{bmatrix} 2 & -3 \\ 0 & 0 \end{bmatrix}
> $$
>
> has rank $1$, so the eigenspace for $-2$ is only one-dimensional (spanned by $\mathbf{b}_1 = (3, 2)$) and $A$ is not diagonalizable. Find the $\mathcal{B}$-matrix of $\mathbf{x} \mapsto A\mathbf{x}$ for $\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2\}$.
>
> With $P = [\,\mathbf{b}_1 \;\; \mathbf{b}_2\,] = \begin{bmatrix} 3 & 2 \\ 2 & 1 \end{bmatrix}$, $\det P = 3 - 4 = -1$ and $P^{-1} = \begin{bmatrix} -1 & 2 \\ 2 & -3 \end{bmatrix}$. By (6),
>
> $$
> AP = \begin{bmatrix} 4 & -9 \\ 4 & -8 \end{bmatrix}\begin{bmatrix} 3 & 2 \\ 2 & 1 \end{bmatrix} = \begin{bmatrix} -6 & -1 \\ -4 & 0 \end{bmatrix}, \qquad P^{-1}AP = \begin{bmatrix} -1 & 2 \\ 2 & -3 \end{bmatrix}\begin{bmatrix} -6 & -1 \\ -4 & 0 \end{bmatrix} = \begin{bmatrix} -2 & 1 \\ 0 & -2 \end{bmatrix} .
> $$
>
> This triangular matrix is called the **Jordan form** of $A$. The eigenvalue of $A$ is on the diagonal. Column by column it says $A\mathbf{b}_1 = -2\mathbf{b}_1$ and $A\mathbf{b}_2 = \mathbf{b}_1 - 2\mathbf{b}_2$, that is, $(A + 2I)\mathbf{b}_2 = \mathbf{b}_1$: $\mathbf{b}_2$ is not an eigenvector but is sent to one by $A + 2I$ (a *generalized eigenvector*).
>
> *Lay: Example 5.4.4*

^ex-35-3

Every square matrix is similar to a matrix in Jordan form, using a basis of eigenvectors and generalized eigenvectors (Lay cites Noble–Daniel, *Applied Linear Algebra*, Ch. 9; rigorous treatment [[§30 Consequences of Generalized Eigenspace Decomposition#^ladr-8-46|LADR 8.46]], over $\mathbb{C}$). For $2 \times 2$ matrices the lecture states the complete answer, which can be proved with what we have.

> [!theorem] Theorem §35.3: Normal Forms of 2 × 2 Matrices with Real Eigenvalues
> Let $A$ be a $2 \times 2$ matrix whose characteristic polynomial has real roots.
>
> 1. If $A$ has two eigenvalues $\lambda_1 \ne \lambda_2$, then $A$ is diagonalizable: $P^{-1}AP = \begin{bmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{bmatrix}$ for some invertible $P$.
> 2. If $A$ has only one eigenvalue $\lambda$, then either
>    - (a) $A = \begin{bmatrix} \lambda & 0 \\ 0 & \lambda \end{bmatrix} = \lambda I_2$, or
>    - (b) there is an invertible $P$ with $P^{-1}AP = \begin{bmatrix} \lambda & 1 \\ 0 & \lambda \end{bmatrix}$ (the Jordan normal form).
>
> So every such matrix is similar to $\begin{bmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{bmatrix}$ or to $\begin{bmatrix} \lambda & 1 \\ 0 & \lambda \end{bmatrix}$. (For complex eigenvalues, see [[§36 Complex Eigenvalues#^thm-36-4|Theorem §36.4]].)
>
> *Source: 235 lecture L20*

^thm-35-3

> [!proof]+ Proof
> (1) is [[§34 Diagonalization#^thm-34-2|Theorem §34.2]].
>
> (2) Let $\lambda$ be the only eigenvalue and $N = A - \lambda I$. The eigenvalues of $N$ are those of $A$ minus $\lambda$ (since $N - \mu I = A - (\lambda + \mu)I$), so the only eigenvalue of $N$ is $0$.
>
> If $\dim\operatorname{Nul} N = 2$, then $N = 0$, so $A = \lambda I$: case (a).
>
> Otherwise $\dim\operatorname{Nul} N = 1$ (it is at least $1$ because $\lambda$ is an eigenvalue), so $\operatorname{rank} N = 1$ by the Rank Theorem, and $\operatorname{Col} N$ is a line spanned by some $\mathbf{w} \ne \mathbf{0}$. Since $N\mathbf{w}$ lies in $\operatorname{Col} N$, $N\mathbf{w} = \mu\mathbf{w}$ for some scalar $\mu$; so $\mu$ is an eigenvalue of $N$, hence $\mu = 0$, and $N\mathbf{w} = \mathbf{0}$. Choose $\mathbf{b}_2$ with $N\mathbf{b}_2 = \mathbf{w}$ (possible because $\mathbf{w} \in \operatorname{Col} N$), and put $\mathbf{b}_1 = \mathbf{w}$. Then
>
> $$
> A\mathbf{b}_1 = \lambda\mathbf{b}_1, \qquad A\mathbf{b}_2 = \lambda\mathbf{b}_2 + N\mathbf{b}_2 = \mathbf{b}_1 + \lambda\mathbf{b}_2 .
> $$
>
> The vectors $\mathbf{b}_1, \mathbf{b}_2$ are linearly independent: $\mathbf{b}_1 \ne \mathbf{0}$, and $\mathbf{b}_2$ is not a multiple of $\mathbf{b}_1$ because $N\mathbf{b}_2 = \mathbf{b}_1 \ne \mathbf{0}$ while $N\mathbf{b}_1 = \mathbf{0}$. With $P = [\,\mathbf{b}_1 \;\; \mathbf{b}_2\,]$, which is invertible because its columns are linearly independent (Invertible Matrix Theorem), the two equations say $AP = P\begin{bmatrix} \lambda & 1 \\ 0 & \lambda \end{bmatrix}$; multiplying on the left by $P^{-1}$ gives case (b).

^pf-35-3

*Uses:* [[§34 Diagonalization#^thm-34-2|§34.2]], [[§28 Rank#^thm-28-3|§28.3]] (the Rank Theorem), [[§13 Characterizations of Invertible Matrices#^thm-13-1|§13.1]] (the Invertible Matrix Theorem)

In Example §35.3, $N = A + 2I$ and $N\mathbf{b}_2 = (12 - 9, 8 - 6) = (3, 2) = \mathbf{b}_1$: Lay's basis is exactly the one built in the proof.

> [!remark] Remark: Computing a B-Matrix Efficiently
> To compute $P^{-1}AP$, compute $AP$ and then row reduce the augmented matrix $[\,P \;\; AP\,]$ to $[\,I \;\; P^{-1}AP\,]$. A separate computation of $P^{-1}$ is unnecessary. (Row reduction of $[\,P \;\; B\,]$ to $[\,I \;\; X\,]$ solves $PX = B$, column by column; here $B = AP$.)
>
> *Lay: 5.4, Numerical Note*

^rem-35-1
