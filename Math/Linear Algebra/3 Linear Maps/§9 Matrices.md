---
type: section
subject: "[[Linear Algebra]]"
chapter: 3
section: 9
aliases: ["LADR 3C", "3C Matrices"]
tags: [linear-algebra]
---
← [[§8 Null Spaces and Ranges]] · ↑ [[· 3 Linear Maps]] · [[§10 Invertibility and Isomorphisms]] →

> [!definition] 3.29 Matrix, Aj,k
> For integers $m,n\ge0$, an *$m$-by-$n$ matrix* $A$ is a rectangular array of elements of $\F$ with $m$ rows and $n$ columns:
> $$
> A=\begin{pmatrix}A_{1,1}&\cdots&A_{1,n}\\ \vdots&&\vdots\\ A_{m,1}&\cdots&A_{m,n}\end{pmatrix}.
> $$
> $A_{j,k}$ is the entry in row $j$, column $k$. $\F^{m,n}$ denotes the set of $m$-by-$n$ matrices.

^ladr-3-29

> [!remark]- Connections
> - Matrices of linear maps: [[§9 Matrices#^ladr-3-31|Matrix of a linear map, M(T)]]. Vector space structure: [[§9 Matrices#^ladr-3-34|Matrix addition]], [[§9 Matrices#^ladr-3-36|Scalar multiplication of a matrix]], [[§9 Matrices#^ladr-3-40|Dim Fᵐ’ⁿ = mn]].

> [!example] 3.30 $A_{j,k}$ equals entry in row $j$, column $k$ of $A$ (p. 69)
> First index = row, second = column. For
> $$
> A=\begin{pmatrix}8&4&5-3i\\1&9&7\end{pmatrix},
> $$
> $A_{2,3}=7$ (row $2$, column $3$).

^ladr-3-30

> [!definition] 3.31 Matrix of a linear map, M(T)
> Let $T\in\Lin(V,W)$, $v_1,\dots,v_n$ a basis of $V$ and $w_1,\dots,w_m$ a basis of $W$. The *matrix of $T$* with respect to these bases is the $m$-by-$n$ matrix $\mathcal{M}(T)$ with entries defined by
> $$
> Tv_k=A_{1,k}w_1+\dots+A_{m,k}w_m .
> $$
> When the bases need to be shown: $\mathcal{M}\big(T,(v_1,\dots,v_n),(w_1,\dots,w_m)\big)$.

^ladr-3-31

> [!remark] How to remember
> Column $k$ of $\mathcal{M}(T)$ holds the coordinates of $Tv_k$ in the basis $w_1,\dots,w_m$. Write the $v$'s across the top and the $w$'s down the side.

> [!remark]- Connections
> - Well defined and bijective in $T$ because of [[Linear map lemma]] and [[§5 Bases#^ladr-2-28|Criterion for basis]].
> - Compatible with the algebra: [[§9 Matrices#^ladr-3-35|Matrix of the sum of linear maps]], [[§9 Matrices#^ladr-3-38|The matrix of a scalar times a linear map]], [[§9 Matrices#^ladr-3-43|Matrix of product of linear maps (LADR 3.43)]]. Acts on coordinates: [[§10 Invertibility and Isomorphisms#^ladr-3-76|Linear maps act like matrix multiplication]].
> - Depends on the bases: [[§10 Invertibility and Isomorphisms#^ladr-3-84|Change-of-basis formula (LADR 3.84)]]. Much of Chapters 5–8 is about choosing bases that make $\mathcal{M}(T)$ simple.

%% ex:3.31-fig %%
> [!example] Reading $\mathcal{M}(T)$
> The $v$'s label the columns and the $w$'s label the rows. Column $k$ (red) lists the coefficients of $Tv_k$ in the basis $w_1,\dots,w_m$.
>
> ![[ladr-3.31-matrix-columns.svg|400]]

> [!example] 3.32 The matrix of a linear map from F² to F³ (p. 70)
> $T(x,y)=(x+3y,\ 2x+5y,\ 7x+9y)$ from $\F^2$ to $\F^3$. Since $T(1,0)=(1,2,7)$ and $T(0,1)=(3,5,9)$, the standard-basis matrix has these as its columns:
> $$
> \mathcal{M}(T)=\begin{pmatrix}1&3\\2&5\\7&9\end{pmatrix}.
> $$

^ladr-3-32

> [!example] 3.33 Matrix of the differentiation map from P3(R) to P2(R) (p. 70)
> $D\in\Lin(\Poly_3(\R),\Poly_2(\R))$, $Dp=p'$. With the standard bases $1,x,x^2,x^3$ and $1,x,x^2$, since $(x^n)'=nx^{n-1}$:
> $$
> \mathcal{M}(D)=\begin{pmatrix}0&1&0&0\\0&0&2&0\\0&0&0&3\end{pmatrix}.
> $$
> Column $k$ holds the coordinates of $D(x^{k-1})$.

^ladr-3-33

> [!definition] 3.34 Matrix addition
> The sum of two matrices of the same size is computed entrywise: $(A+C)_{j,k}=A_{j,k}+C_{j,k}$.

^ladr-3-34

> [!remark]- Connections
> - Matches addition of maps: [[§9 Matrices#^ladr-3-35|Matrix of the sum of linear maps]].

> [!theorem] 3.35 Matrix of the sum of linear maps
> If $S,T\in\Lin(V,W)$ (same bases throughout), then $\mathcal{M}(S+T)=\mathcal{M}(S)+\mathcal{M}(T)$.

^ladr-3-35

> [!proof]+
> *(Filled in.)* Let $\mathcal{M}(S)=A$, $\mathcal{M}(T)=C$. Then
> $$
> (S+T)v_k=Sv_k+Tv_k=\sum_j A_{j,k}w_j+\sum_jC_{j,k}w_j=\sum_j(A_{j,k}+C_{j,k})w_j,
> $$
> so column $k$ of $\mathcal{M}(S+T)$ is column $k$ of $A+C$.

> [!remark]- Connections
> - With [[§9 Matrices#^ladr-3-38|The matrix of a scalar times a linear map]]: $\mathcal{M}$ is linear, one half of [[§10 Invertibility and Isomorphisms#^ladr-3-72|Dim L(V, W) = (dim V)(dim W)]].

> [!definition] 3.36 Scalar multiplication of a matrix
> For $\lambda\in\F$ and a matrix $A$, $\lambda A$ is computed entrywise: $(\lambda A)_{j,k}=\lambda A_{j,k}$.

^ladr-3-36

> [!remark]- Connections
> - Matches scalar multiples of maps: [[§9 Matrices#^ladr-3-38|The matrix of a scalar times a linear map]].

> [!example] 3.37 Addition and scalar multiplication of matrices (p. 72)
> $$
> 2\begin{pmatrix}3&1\\-1&5\end{pmatrix}+\begin{pmatrix}4&2\\1&6\end{pmatrix}
> =\begin{pmatrix}6&2\\-2&10\end{pmatrix}+\begin{pmatrix}4&2\\1&6\end{pmatrix}
> =\begin{pmatrix}10&4\\-1&16\end{pmatrix}.
> $$

^ladr-3-37

> [!theorem] 3.38 The matrix of a scalar times a linear map
> If $\lambda\in\F$ and $T\in\Lin(V,W)$, then $\mathcal{M}(\lambda T)=\lambda\mathcal{M}(T)$.

^ladr-3-38

> [!proof]+
> *(Filled in.)* $(\lambda T)v_k=\lambda\sum_jA_{j,k}w_j=\sum_j(\lambda A_{j,k})w_j$.

> [!remark]- Connections
> - With [[§9 Matrices#^ladr-3-35|Matrix of the sum of linear maps]]: $\mathcal{M}:\Lin(V,W)\to\F^{m,n}$ is linear ([[§10 Invertibility and Isomorphisms#^ladr-3-72|Dim L(V, W) = (dim V)(dim W)]]).

> [!remark] 3.39 Notation: Fᵐ,n (p. 72)

^ladr-3-39

> [!theorem] 3.40 Dim Fᵐ’ⁿ = mn
> For positive integers $m,n$, $\F^{m,n}$ with entrywise addition and scalar multiplication is a vector space of dimension $mn$.

^ladr-3-40

> [!proof]+
> *(Filled in.)* The axioms hold entrywise because they hold in $\F$; the zero is the all-$0$ matrix. Let $E^{(j,k)}$ be the matrix with $1$ in entry $(j,k)$ and $0$ elsewhere. Every $A$ equals $\sum_{j,k}A_{j,k}E^{(j,k)}$, and this representation is unique (the coefficients are read off entrywise), so the $mn$ matrices $E^{(j,k)}$ form a basis ([[§5 Bases#^ladr-2-28|Criterion for basis]]).

*Uses:* [[§5 Bases#^ladr-2-28|2.28]]

> [!remark]- Connections
> - Combined with $\Lin(V,W)\cong\F^{m,n}$: [[§10 Invertibility and Isomorphisms#^ladr-3-72|Dim L(V, W) = (dim V)(dim W)]].

> [!definition] 3.41 Matrix multiplication
> If $A$ is $m$-by-$n$ and $B$ is $n$-by-$p$, then $AB$ is the $m$-by-$p$ matrix with
> $$
> (AB)_{j,k}=\sum_{r=1}^{n}A_{j,r}B_{r,k}.
> $$

^ladr-3-41

> [!remark] Why this definition
> It is forced by requiring $\mathcal{M}(ST)=\mathcal{M}(S)\mathcal{M}(T)$; see the computation in [[§9 Matrices#^ladr-3-43|Matrix of product of linear maps (LADR 3.43)]]. The product is defined only when the number of columns of $A$ equals the number of rows of $B$.

> [!remark]- Connections
> - Other ways to read the product: [[§9 Matrices#^ladr-3-46|Entry of matrix product equals row times column]], [[§9 Matrices#^ladr-3-48|Column of matrix product equals matrix times column]], [[§9 Matrices#^ladr-3-50|Linear combination of columns]], [[§9 Matrices#^ladr-3-51|Matrix multiplication as linear combinations of columns]].

> [!example] 3.42 Matrix multiplication (p. 73)
> A $3$-by-$2$ times a $2$-by-$4$ matrix is $3$-by-$4$:
> $$
> \begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}\begin{pmatrix}6&5&4&3\\2&1&0&-1\end{pmatrix}
> =\begin{pmatrix}10&7&4&1\\26&19&12&5\\42&31&20&9\end{pmatrix}.
> $$
> Matrix multiplication is associative and distributive but not commutative.

^ladr-3-42

> [!theorem] 3.43 Matrix of product of linear maps
> If $T\in\Lin(U,V)$ and $S\in\Lin(V,W)$, then $\mathcal{M}(ST)=\mathcal{M}(S)\mathcal{M}(T)$ (bases $u_1,\dots,u_p$; $v_1,\dots,v_n$; $w_1,\dots,w_m$).

^ladr-3-43

> [!proof]+
> Let $\mathcal{M}(S)=A$, $\mathcal{M}(T)=B$. For each $k$,
> $$
> (ST)u_k=S\Big(\sum_{r}B_{r,k}v_r\Big)=\sum_rB_{r,k}Sv_r=\sum_rB_{r,k}\sum_jA_{j,r}w_j=\sum_j\Big(\sum_rA_{j,r}B_{r,k}\Big)w_j .
> $$
> So the $(j,k)$ entry of $\mathcal{M}(ST)$ is $\sum_rA_{j,r}B_{r,k}=(AB)_{j,k}$ ([[§9 Matrices#^ladr-3-41|Matrix multiplication]]).

*Uses:* [[§9 Matrices#^ladr-3-41|3.41]]

> [!remark]- Connections
> - Restated with explicit bases in [[§10 Invertibility and Isomorphisms#^ladr-3-81|Matrix of product of linear maps (LADR 3.81)]]; used for change of basis [[§10 Invertibility and Isomorphisms#^ladr-3-84|Change-of-basis formula (LADR 3.84)]] and [[§10 Invertibility and Isomorphisms#^ladr-3-86|Matrix of inverse equals inverse of matrix]].

> [!remark] 3.44 Notation: Aj,⋅, A⋅,k (p. 74)

^ladr-3-44

> [!example] 3.45 $A_{j,\cdot}$ equals $j$th row of $A$ and $A_{\cdot,k}$ equals $k$th column of $A$ (p. 74)
> For $A=\begin{pmatrix}8&4&5\\1&9&7\end{pmatrix}$: row $A_{2,\cdot}=\begin{pmatrix}1&9&7\end{pmatrix}$ and column $A_{\cdot,2}=\begin{pmatrix}4\\9\end{pmatrix}$.
>
> A $1$-by-$n$ times an $n$-by-$1$ matrix is $1$-by-$1$ and is identified with its entry: $\begin{pmatrix}3&4\end{pmatrix}\begin{pmatrix}6\\2\end{pmatrix}=26$. This is the $(2,1)$ entry of the product in [[§9 Matrices#^ladr-3-42|3.42]] ([[§9 Matrices#^ladr-3-46|3.46]]):
>
> ![[ladr-3.45-row-times-column.svg|480]]

^ladr-3-45

> [!theorem] 3.46 Entry of matrix product equals row times column
> If $A$ is $m$-by-$n$ and $B$ is $n$-by-$p$, then $(AB)_{j,k}=A_{j,\cdot}\,B_{\cdot,k}$: the $(j,k)$ entry of $AB$ is row $j$ of $A$ times column $k$ of $B$.

^ladr-3-46

> [!proof]+
> Both sides equal $A_{j,1}B_{1,k}+\dots+A_{j,n}B_{n,k}$ by [[§9 Matrices#^ladr-3-41|Matrix multiplication]], the right side being a $1$-by-$n$ times $n$-by-$1$ product.

*Uses:* [[§9 Matrices#^ladr-3-41|3.41]]

> [!remark]- Connections
> - Column version: [[§9 Matrices#^ladr-3-48|Column of matrix product equals matrix times column]].

> [!theorem] 3.48 Column of matrix product equals matrix times column
> If $A$ is $m$-by-$n$ and $B$ is $n$-by-$p$, then $(AB)_{\cdot,k}=A\,B_{\cdot,k}$: column $k$ of $AB$ is $A$ times column $k$ of $B$.

^ladr-3-48

> [!proof]+
> Both are $m$-by-$1$, and the entry in row $j$ of each is $\sum_rA_{j,r}B_{r,k}$.

> [!remark]- Connections
> - Combined with [[§9 Matrices#^ladr-3-50|Linear combination of columns]] gives [[§9 Matrices#^ladr-3-51|Matrix multiplication as linear combinations of columns]].

> [!example] 3.49 Product of a 3-by-2 matrix and a 2-by-1 matrix (p. 75)
> $$
> \begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}\begin{pmatrix}5\\1\end{pmatrix}
> =\begin{pmatrix}7\\19\\31\end{pmatrix}
> =5\begin{pmatrix}1\\3\\5\end{pmatrix}+1\begin{pmatrix}2\\4\\6\end{pmatrix}:
> $$
> matrix times column is a combination of the columns, with coefficients from the column ([[§9 Matrices#^ladr-3-50|3.50]]).

^ladr-3-49

> [!theorem] 3.50 Linear combination of columns
> If $A$ is $m$-by-$n$ and $b=(b_1,\dots,b_n)^t$ is $n$-by-$1$, then
> $$
> Ab=b_1A_{\cdot,1}+\dots+b_nA_{\cdot,n},
> $$
> a linear combination of the columns of $A$ with coefficients from $b$.

^ladr-3-50

> [!proof]+
> Row $k$ of $Ab$ is $A_{k,1}b_1+\dots+A_{k,n}b_n$, which is also row $k$ of $b_1A_{\cdot,1}+\dots+b_nA_{\cdot,n}$.

> [!remark]- Connections
> - Why $\range$ of a matrix map is the column space; used in [[§10 Invertibility and Isomorphisms#^ladr-3-76|Linear maps act like matrix multiplication]] and [[§10 Invertibility and Isomorphisms#^ladr-3-78|Dimension of range T equals column rank of M(T)]].

> [!theorem] 3.51 Matrix multiplication as linear combinations of columns
> Let $C$ be $m$-by-$c$ and $R$ be $c$-by-$n$.
> - (a) Column $k$ of $CR$ is a linear combination of the columns of $C$, with coefficients from column $k$ of $R$.
> - (b) Row $j$ of $CR$ is a linear combination of the rows of $R$, with coefficients from row $j$ of $C$.

^ladr-3-51

> [!proof]+
> (a) Column $k$ of $CR$ is $CR_{\cdot,k}$ ([[§9 Matrices#^ladr-3-48|Column of matrix product equals matrix times column]]), which is $\sum_rR_{r,k}C_{\cdot,r}$ by [[§9 Matrices#^ladr-3-50|Linear combination of columns]].
>
> (b) *(Filled in; Axler leaves the row versions as exercises.)* The entry of row $j$ of $CR$ in column $k$ is $\sum_rC_{j,r}R_{r,k}$, which is the column-$k$ entry of $\sum_rC_{j,r}R_{r,\cdot}$. Hence $(CR)_{j,\cdot}=\sum_rC_{j,r}R_{r,\cdot}$.

*Uses:* [[§9 Matrices#^ladr-3-48|3.48]], [[§9 Matrices#^ladr-3-50|3.50]]

> [!remark]- Connections
> - The tool behind [[§9 Matrices#^ladr-3-56|Column–row factorization]] and [[§9 Matrices#^ladr-3-57|Column rank equals row rank (LADR 3.57)]].

> [!definition] 3.52 Column rank, row rank
> For $A\in\F^{m,n}$: the *column rank* of $A$ is the dimension of the span of its columns in $\F^{m,1}$; the *row rank* is the dimension of the span of its rows in $\F^{1,n}$.

^ladr-3-52

> [!remark] Bounds
> Both are at most $\min\{m,n\}$.

> [!remark]- Connections
> - They are equal: [[§9 Matrices#^ladr-3-57|Column rank equals row rank (LADR 3.57)]], hence [[§9 Matrices#^ladr-3-58|Rank]]. Column rank $=\dim\range T$: [[§10 Invertibility and Isomorphisms#^ladr-3-78|Dimension of range T equals column rank of M(T)]].

> [!example] 3.53 Column rank and row rank of a 2-by-4 matrix (p. 77)
> $A=\begin{pmatrix}4&7&1&8\\3&5&2&9\end{pmatrix}$.
> - Column rank: the columns lie in $\F^{2,1}$, so the rank is $\le2$; $\binom43,\binom75$ are not multiples, so it is $2$.
> - Row rank: the two rows are not multiples of each other, so it is $2$.
>
> Equal, as [[§9 Matrices#^ladr-3-57|3.57]] guarantees in general.

^ladr-3-53

> [!definition] 3.54 Transpose, Aᵗ
> The *transpose* $A^t$ of an $m$-by-$n$ matrix $A$ is the $n$-by-$m$ matrix with $(A^t)_{k,j}=A_{j,k}$: rows and columns are interchanged.

^ladr-3-54

> [!remark]- Connections
> - Swaps row rank and column rank (used in [[§9 Matrices#^ladr-3-57|Column rank equals row rank (LADR 3.57)]]). Complex analogue with conjugation: [[§22 Self-Adjoint and Normal Operators#^ladr-7-7|Conjugate transpose, A∗]]; its map-level meaning is the dual map ([[§12 Duality#^ladr-3-118|Dual map, T′]]) or adjoint ([[§22 Self-Adjoint and Normal Operators#^ladr-7-1|Adjoint, T∗]]).

> [!example] 3.55 Transpose of a matrix (p. 78)
> $$
> A=\begin{pmatrix}5&-7\\3&8\\-4&2\end{pmatrix}\ (3\text{-by-}2),\qquad A^t=\begin{pmatrix}5&3&-4\\-7&8&2\end{pmatrix}\ (2\text{-by-}3).
> $$
> Rules: $(A+B)^t=A^t+B^t$, $(\lambda A)^t=\lambda A^t$, $(AC)^t=C^tA^t$ (order reverses, as for dual maps in [[§12 Duality#^ladr-3-120|3.120]]).

^ladr-3-55

> [!theorem] 3.56 Column–row factorization
> Suppose $A\in\F^{m,n}$ has column rank $c\ge1$. Then $A=CR$ for some $C\in\F^{m,c}$ and $R\in\F^{c,n}$.

^ladr-3-56

> [!proof]+
> Reduce the list of columns $A_{\cdot,1},\dots,A_{\cdot,n}$ to a basis of their span ([[Every spanning list contains a basis]]); it has length $c$. Let $C$ be the $m$-by-$c$ matrix with these basis vectors as columns. Each column $A_{\cdot,k}$ is a linear combination of the columns of $C$; put its coefficients into column $k$ of a $c$-by-$n$ matrix $R$. Then $A=CR$ by [[§9 Matrices#^ladr-3-51|Matrix multiplication as linear combinations of columns]](a).

*Uses:* [[Every spanning list contains a basis|2.30]], [[§9 Matrices#^ladr-3-51|3.51]]

> [!remark]- Connections
> - Immediately gives [[§9 Matrices#^ladr-3-57|Column rank equals row rank (LADR 3.57)]]. Refinements with orthonormal columns: [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-58|QR factorization]], and the SVD [[§26 Singular Value Decomposition#^ladr-7-80|Matrix version of SVD]].

> [!theorem] 3.57 Column rank equals row rank
> For every $A\in\F^{m,n}$, the column rank of $A$ equals the row rank of $A$.

^ladr-3-57

> [!proof]+
> Let $c$ be the column rank and $A=CR$ as in [[§9 Matrices#^ladr-3-56|Column–row factorization]]. By [[§9 Matrices#^ladr-3-51|Matrix multiplication as linear combinations of columns]](b) every row of $A$ is a linear combination of the $c$ rows of $R$, so row rank $\le c=$ column rank. Applying this to $A^t$:
> $$
> \text{col rank}(A)=\text{row rank}(A^t)\le\text{col rank}(A^t)=\text{row rank}(A).
> $$

*Uses:* [[§9 Matrices#^ladr-3-56|3.56]], [[§9 Matrices#^ladr-3-51|3.51]]

> [!remark]- Connections
> - Allows [[§9 Matrices#^ladr-3-58|Rank]]. Alternative proof via duality: [[§12 Duality#^ladr-3-133|Column rank equals row rank (LADR 3.133)]].

> [!definition] 3.58 Rank
> The *rank* of $A\in\F^{m,n}$ is its column rank (equivalently, by [[§9 Matrices#^ladr-3-57|Column rank equals row rank (LADR 3.57)]], its row rank).

^ladr-3-58

> [!remark]- Connections
> - Rank–nullity for matrices: [[Fundamental theorem of linear maps]] with [[§10 Invertibility and Isomorphisms#^ladr-3-78|Dimension of range T equals column rank of M(T)]] gives $n=\dim\nullsp A+\operatorname{rank}A$.
