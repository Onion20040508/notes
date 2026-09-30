---
type: section
subject: "[[Linear Algebra]]"
chapter: 3
section: "3C"
tags: [linear-algebra]
---
← [[Linear Algebra 3B Null Spaces and Ranges]] · ↑ [[Linear Algebra — 3 Linear Maps]] · [[Linear Algebra 3D Invertibility and Isomorphisms]] →

> [!definition] 3.29 Matrix, Aj,k
> For integers $m,n\ge0$, an *$m$-by-$n$ matrix* $A$ is a rectangular array of elements of $\F$ with $m$ rows and $n$ columns:
> $$
> A=\begin{pmatrix}A_{1,1}&\cdots&A_{1,n}\\ \vdots&&\vdots\\ A_{m,1}&\cdots&A_{m,n}\end{pmatrix}.
> $$
> $A_{j,k}$ is the entry in row $j$, column $k$. $\F^{m,n}$ denotes the set of $m$-by-$n$ matrices.

^ladr-3-29

> [!remark]- Connections
> - Matrices of linear maps: [[Linear Algebra 3C Matrices#^ladr-3-31|Matrix of a linear map, M(T)]]. Vector space structure: [[Linear Algebra 3C Matrices#^ladr-3-34|Matrix addition]], [[Linear Algebra 3C Matrices#^ladr-3-36|Scalar multiplication of a matrix]], [[Linear Algebra 3C Matrices#^ladr-3-40|Dim Fᵐ’ⁿ = mn]].

> [!example] 3.30 Aj,kequals entry in row j, column k of A (p. 69)

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
> - Well defined and bijective in $T$ because of [[Linear map lemma]] and [[Linear Algebra 2B Bases#^ladr-2-28|Criterion for basis]].
> - Compatible with the algebra: [[Linear Algebra 3C Matrices#^ladr-3-35|Matrix of the sum of linear maps]], [[Linear Algebra 3C Matrices#^ladr-3-38|The matrix of a scalar times a linear map]], [[Linear Algebra 3C Matrices#^ladr-3-43|Matrix of product of linear maps (LADR 3.43)]]. Acts on coordinates: [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-76|Linear maps act like matrix multiplication]].
> - Depends on the bases: [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-84|Change-of-basis formula (LADR 3.84)]]. Much of Chapters 5–8 is about choosing bases that make $\mathcal{M}(T)$ simple.

> [!example] 3.32 The matrix of a linear map from F² to F³ (p. 70)

^ladr-3-32

> [!example] 3.33 Matrix of the differentiation map from P3(R) to P2(R) (p. 70)

^ladr-3-33

> [!definition] 3.34 Matrix addition
> The sum of two matrices of the same size is computed entrywise: $(A+C)_{j,k}=A_{j,k}+C_{j,k}$.

^ladr-3-34

> [!remark]- Connections
> - Matches addition of maps: [[Linear Algebra 3C Matrices#^ladr-3-35|Matrix of the sum of linear maps]].

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
> - With [[Linear Algebra 3C Matrices#^ladr-3-38|The matrix of a scalar times a linear map]]: $\mathcal{M}$ is linear, one half of [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-72|Dim L(V, W) = (dim V)(dim W)]].

> [!definition] 3.36 Scalar multiplication of a matrix
> For $\lambda\in\F$ and a matrix $A$, $\lambda A$ is computed entrywise: $(\lambda A)_{j,k}=\lambda A_{j,k}$.

^ladr-3-36

> [!remark]- Connections
> - Matches scalar multiples of maps: [[Linear Algebra 3C Matrices#^ladr-3-38|The matrix of a scalar times a linear map]].

> [!example] 3.37 Addition and scalar multiplication of matrices (p. 72)

^ladr-3-37

> [!theorem] 3.38 The matrix of a scalar times a linear map
> If $\lambda\in\F$ and $T\in\Lin(V,W)$, then $\mathcal{M}(\lambda T)=\lambda\mathcal{M}(T)$.

^ladr-3-38

> [!proof]+
> *(Filled in.)* $(\lambda T)v_k=\lambda\sum_jA_{j,k}w_j=\sum_j(\lambda A_{j,k})w_j$.

> [!remark]- Connections
> - With [[Linear Algebra 3C Matrices#^ladr-3-35|Matrix of the sum of linear maps]]: $\mathcal{M}:\Lin(V,W)\to\F^{m,n}$ is linear ([[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-72|Dim L(V, W) = (dim V)(dim W)]]).

> [!remark] 3.39 Notation: Fᵐ,n (p. 72)

^ladr-3-39

> [!theorem] 3.40 Dim Fᵐ’ⁿ = mn
> For positive integers $m,n$, $\F^{m,n}$ with entrywise addition and scalar multiplication is a vector space of dimension $mn$.

^ladr-3-40

> [!proof]+
> *(Filled in.)* The axioms hold entrywise because they hold in $\F$; the zero is the all-$0$ matrix. Let $E^{(j,k)}$ be the matrix with $1$ in entry $(j,k)$ and $0$ elsewhere. Every $A$ equals $\sum_{j,k}A_{j,k}E^{(j,k)}$, and this representation is unique (the coefficients are read off entrywise), so the $mn$ matrices $E^{(j,k)}$ form a basis ([[Linear Algebra 2B Bases#^ladr-2-28|Criterion for basis]]).

*Uses:* [[Linear Algebra 2B Bases#^ladr-2-28|2.28]]

> [!remark]- Connections
> - Combined with $\Lin(V,W)\cong\F^{m,n}$: [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-72|Dim L(V, W) = (dim V)(dim W)]].

> [!definition] 3.41 Matrix multiplication
> If $A$ is $m$-by-$n$ and $B$ is $n$-by-$p$, then $AB$ is the $m$-by-$p$ matrix with
> $$
> (AB)_{j,k}=\sum_{r=1}^{n}A_{j,r}B_{r,k}.
> $$

^ladr-3-41

> [!remark] Why this definition
> It is forced by requiring $\mathcal{M}(ST)=\mathcal{M}(S)\mathcal{M}(T)$; see the computation in [[Linear Algebra 3C Matrices#^ladr-3-43|Matrix of product of linear maps (LADR 3.43)]]. The product is defined only when the number of columns of $A$ equals the number of rows of $B$.

> [!remark]- Connections
> - Other ways to read the product: [[Linear Algebra 3C Matrices#^ladr-3-46|Entry of matrix product equals row times column]], [[Linear Algebra 3C Matrices#^ladr-3-48|Column of matrix product equals matrix times column]], [[Linear Algebra 3C Matrices#^ladr-3-50|Linear combination of columns]], [[Linear Algebra 3C Matrices#^ladr-3-51|Matrix multiplication as linear combinations of columns]].

> [!example] 3.42 Matrix multiplication (p. 73)

^ladr-3-42

> [!theorem] 3.43 Matrix of product of linear maps
> If $T\in\Lin(U,V)$ and $S\in\Lin(V,W)$, then $\mathcal{M}(ST)=\mathcal{M}(S)\mathcal{M}(T)$ (bases $u_1,\dots,u_p$; $v_1,\dots,v_n$; $w_1,\dots,w_m$).

^ladr-3-43

> [!proof]+
> Let $\mathcal{M}(S)=A$, $\mathcal{M}(T)=B$. For each $k$,
> $$
> (ST)u_k=S\Big(\sum_{r}B_{r,k}v_r\Big)=\sum_rB_{r,k}Sv_r=\sum_rB_{r,k}\sum_jA_{j,r}w_j=\sum_j\Big(\sum_rA_{j,r}B_{r,k}\Big)w_j .
> $$
> So the $(j,k)$ entry of $\mathcal{M}(ST)$ is $\sum_rA_{j,r}B_{r,k}=(AB)_{j,k}$ ([[Linear Algebra 3C Matrices#^ladr-3-41|Matrix multiplication]]).

*Uses:* [[Linear Algebra 3C Matrices#^ladr-3-41|3.41]]

> [!remark]- Connections
> - Restated with explicit bases in [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-81|Matrix of product of linear maps (LADR 3.81)]]; used for change of basis [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-84|Change-of-basis formula (LADR 3.84)]] and [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-86|Matrix of inverse equals inverse of matrix]].

> [!remark] 3.44 Notation: Aj,⋅, A⋅,k (p. 74)

^ladr-3-44

> [!example] 3.45 Aj,⋅equals j (p. 74)

^ladr-3-45

> [!theorem] 3.46 Entry of matrix product equals row times column
> If $A$ is $m$-by-$n$ and $B$ is $n$-by-$p$, then $(AB)_{j,k}=A_{j,\cdot}\,B_{\cdot,k}$: the $(j,k)$ entry of $AB$ is row $j$ of $A$ times column $k$ of $B$.

^ladr-3-46

> [!proof]+
> Both sides equal $A_{j,1}B_{1,k}+\dots+A_{j,n}B_{n,k}$ by [[Linear Algebra 3C Matrices#^ladr-3-41|Matrix multiplication]], the right side being a $1$-by-$n$ times $n$-by-$1$ product.

*Uses:* [[Linear Algebra 3C Matrices#^ladr-3-41|3.41]]

> [!remark]- Connections
> - Column version: [[Linear Algebra 3C Matrices#^ladr-3-48|Column of matrix product equals matrix times column]].

> [!theorem] 3.48 Column of matrix product equals matrix times column
> If $A$ is $m$-by-$n$ and $B$ is $n$-by-$p$, then $(AB)_{\cdot,k}=A\,B_{\cdot,k}$: column $k$ of $AB$ is $A$ times column $k$ of $B$.

^ladr-3-48

> [!proof]+
> Both are $m$-by-$1$, and the entry in row $j$ of each is $\sum_rA_{j,r}B_{r,k}$.

> [!remark]- Connections
> - Combined with [[Linear Algebra 3C Matrices#^ladr-3-50|Linear combination of columns]] gives [[Linear Algebra 3C Matrices#^ladr-3-51|Matrix multiplication as linear combinations of columns]].

> [!example] 3.49 Product of a 3-by-2 matrix and a 2-by-1 matrix (p. 75)

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
> - Why $\range$ of a matrix map is the column space; used in [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-76|Linear maps act like matrix multiplication]] and [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-78|Dimension of range T equals column rank of M(T)]].

> [!theorem] 3.51 Matrix multiplication as linear combinations of columns
> Let $C$ be $m$-by-$c$ and $R$ be $c$-by-$n$.
> - (a) Column $k$ of $CR$ is a linear combination of the columns of $C$, with coefficients from column $k$ of $R$.
> - (b) Row $j$ of $CR$ is a linear combination of the rows of $R$, with coefficients from row $j$ of $C$.

^ladr-3-51

> [!proof]+
> (a) Column $k$ of $CR$ is $CR_{\cdot,k}$ ([[Linear Algebra 3C Matrices#^ladr-3-48|Column of matrix product equals matrix times column]]), which is $\sum_rR_{r,k}C_{\cdot,r}$ by [[Linear Algebra 3C Matrices#^ladr-3-50|Linear combination of columns]].
>
> (b) *(Filled in; Axler leaves the row versions as exercises.)* The entry of row $j$ of $CR$ in column $k$ is $\sum_rC_{j,r}R_{r,k}$, which is the column-$k$ entry of $\sum_rC_{j,r}R_{r,\cdot}$. Hence $(CR)_{j,\cdot}=\sum_rC_{j,r}R_{r,\cdot}$.

*Uses:* [[Linear Algebra 3C Matrices#^ladr-3-48|3.48]], [[Linear Algebra 3C Matrices#^ladr-3-50|3.50]]

> [!remark]- Connections
> - The tool behind [[Linear Algebra 3C Matrices#^ladr-3-56|Column–row factorization]] and [[Linear Algebra 3C Matrices#^ladr-3-57|Column rank equals row rank (LADR 3.57)]].

> [!definition] 3.52 Column rank, row rank
> For $A\in\F^{m,n}$: the *column rank* of $A$ is the dimension of the span of its columns in $\F^{m,1}$; the *row rank* is the dimension of the span of its rows in $\F^{1,n}$.

^ladr-3-52

> [!remark] Bounds
> Both are at most $\min\{m,n\}$.

> [!remark]- Connections
> - They are equal: [[Linear Algebra 3C Matrices#^ladr-3-57|Column rank equals row rank (LADR 3.57)]], hence [[Linear Algebra 3C Matrices#^ladr-3-58|Rank]]. Column rank $=\dim\range T$: [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-78|Dimension of range T equals column rank of M(T)]].

> [!example] 3.53 Column rank and row rank of a 2-by-4 matrix (p. 77)

^ladr-3-53

> [!definition] 3.54 Transpose, Aᵗ
> The *transpose* $A^t$ of an $m$-by-$n$ matrix $A$ is the $n$-by-$m$ matrix with $(A^t)_{k,j}=A_{j,k}$: rows and columns are interchanged.

^ladr-3-54

> [!remark]- Connections
> - Swaps row rank and column rank (used in [[Linear Algebra 3C Matrices#^ladr-3-57|Column rank equals row rank (LADR 3.57)]]). Complex analogue with conjugation: [[Linear Algebra 7A Self-Adjoint and Normal Operators#^ladr-7-7|Conjugate transpose, A∗]]; its map-level meaning is the dual map ([[Linear Algebra 3F Duality#^ladr-3-118|Dual map, T′]]) or adjoint ([[Linear Algebra 7A Self-Adjoint and Normal Operators#^ladr-7-1|Adjoint, T∗]]).

> [!example] 3.55 Transpose of a matrix (p. 78)

^ladr-3-55

> [!theorem] 3.56 Column–row factorization
> Suppose $A\in\F^{m,n}$ has column rank $c\ge1$. Then $A=CR$ for some $C\in\F^{m,c}$ and $R\in\F^{c,n}$.

^ladr-3-56

> [!proof]+
> Reduce the list of columns $A_{\cdot,1},\dots,A_{\cdot,n}$ to a basis of their span ([[Every spanning list contains a basis]]); it has length $c$. Let $C$ be the $m$-by-$c$ matrix with these basis vectors as columns. Each column $A_{\cdot,k}$ is a linear combination of the columns of $C$; put its coefficients into column $k$ of a $c$-by-$n$ matrix $R$. Then $A=CR$ by [[Linear Algebra 3C Matrices#^ladr-3-51|Matrix multiplication as linear combinations of columns]](a).

*Uses:* [[Every spanning list contains a basis|2.30]], [[Linear Algebra 3C Matrices#^ladr-3-51|3.51]]

> [!remark]- Connections
> - Immediately gives [[Linear Algebra 3C Matrices#^ladr-3-57|Column rank equals row rank (LADR 3.57)]]. Refinements with orthonormal columns: [[Linear Algebra 7D Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-58|QR factorization]], and the SVD [[Linear Algebra 7E Singular Value Decomposition#^ladr-7-80|Matrix version of SVD]].

> [!theorem] 3.57 Column rank equals row rank
> For every $A\in\F^{m,n}$, the column rank of $A$ equals the row rank of $A$.

^ladr-3-57

> [!proof]+
> Let $c$ be the column rank and $A=CR$ as in [[Linear Algebra 3C Matrices#^ladr-3-56|Column–row factorization]]. By [[Linear Algebra 3C Matrices#^ladr-3-51|Matrix multiplication as linear combinations of columns]](b) every row of $A$ is a linear combination of the $c$ rows of $R$, so row rank $\le c=$ column rank. Applying this to $A^t$:
> $$
> \text{col rank}(A)=\text{row rank}(A^t)\le\text{col rank}(A^t)=\text{row rank}(A).
> $$

*Uses:* [[Linear Algebra 3C Matrices#^ladr-3-56|3.56]], [[Linear Algebra 3C Matrices#^ladr-3-51|3.51]]

> [!remark]- Connections
> - Allows [[Linear Algebra 3C Matrices#^ladr-3-58|Rank]]. Alternative proof via duality: [[Linear Algebra 3F Duality#^ladr-3-133|Column rank equals row rank (LADR 3.133)]].

> [!definition] 3.58 Rank
> The *rank* of $A\in\F^{m,n}$ is its column rank (equivalently, by [[Linear Algebra 3C Matrices#^ladr-3-57|Column rank equals row rank (LADR 3.57)]], its row rank).

^ladr-3-58

> [!remark]- Connections
> - Rank–nullity for matrices: [[Fundamental theorem of linear maps]] with [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-78|Dimension of range T equals column rank of M(T)]] gives $n=\dim\nullsp A+\operatorname{rank}A$.
