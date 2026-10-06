---
type: section
subject: "[[Linear Algebra]]"
chapter: 5
section: 14
aliases: ["LADR 5A", "5A Invariant Subspaces"]
tags: [linear-algebra]
---
← [[§13 Polynomials]] · ↑ [[· 5 Eigenvalues and Eigenvectors]] · [[§15 The Minimal Polynomial]] →

> [!definition] Definition 5.1: Operator
> An *operator* is a linear map from a vector space to itself; $\Lin(V)=\Lin(V,V)$.

^ladr-5-1

> [!remark] Remark: Why operators get a richer theory
> Operators can be composed with themselves, so powers $T^m$ and polynomials $p(T)$ make sense (see [[§14 Invariant Subspaces#^ladr-5-17|Multiplicative properties]]). If $V=V_1\oplus\dots\oplus V_m$ with each $V_k$ invariant, understanding $T$ reduces to understanding each $T|_{V_k}$ ([[§14 Invariant Subspaces#^ladr-5-2|Invariant subspace]]).

> [!remark]- Connections
> - Physics: observables and Hamiltonians are operators; their spectral theory is Chapters 5–7.

> [!definition] Definition 5.2: Invariant subspace
> For $T\in\Lin(V)$, a subspace $U$ of $V$ is *invariant under $T$* if $Tu\in U$ for every $u\in U$; equivalently $T|_U$ is an operator on $U$.

^ladr-5-2

> [!remark] Remark: Examples
> $\{0\}$, $V$, $\nullsp T$ and $\range T$ are always invariant ([[§14 Invariant Subspaces#^ladr-5-4|5.4]]). More generally $\nullsp p(T)$ and $\range p(T)$ are ([[§14 Invariant Subspaces#^ladr-5-18|Null space and range of p(T) are invariant under T]]).

> [!remark]- Connections
> - One-dimensional invariant subspaces are exactly eigenvector lines: [[§14 Invariant Subspaces#^ladr-5-5|Eigenvalue]], [[§14 Invariant Subspaces#^ladr-5-8|Eigenvector]].
> - Restriction and minimal polynomials: [[§15 The Minimal Polynomial#^ladr-5-31|Minimal polynomial of a restriction operator]]. Physics: symmetry sectors are invariant subspaces of the Hamiltonian.

> [!example] Example 5.3: Subspace invariant under differentiation operator (p. 133)
> For $D\in\Lin(\Poly(\R))$, $Dp=p'$, the subspace $\Poly_4(\R)$ is invariant: differentiating does not raise degree. More generally every $\Poly_m(\R)$ is invariant, which is exactly what let [[§10 Invertibility and Isomorphisms#^ladr-3-67|3.67]] restrict to a finite-dimensional piece.

^ladr-5-3

> [!example] Example 5.4: Four invariant subspaces, not necessarily all different (p. 133)
> For every $T\in\Lin(V)$ the subspaces $\{0\}$, $V$, $\nullsp T$ and $\range T$ are invariant:
> - $u\in\nullsp T\Rightarrow Tu=0\in\nullsp T$;
> - $u\in\range T\Rightarrow Tu\in\range T$ trivially.
>
> They need not be interesting: for invertible $T$, $\nullsp T=\{0\}$ and $\range T=V$. Whether *other* invariant subspaces exist is a real question. In finite dimensions the answer is yes once $\dim V>1$ over $\C$ ([[Existence of eigenvalues|5.19]]) or $\dim V>2$ over $\R$.

^ladr-5-4

> [!definition] Definition 5.5: Eigenvalue
> For $T\in\Lin(V)$, $\lambda\in\F$ is an *eigenvalue* of $T$ if there is $v\in V$, $v\ne0$, with $Tv=\lambda v$.

^ladr-5-5

> [!remark] Remark: Why $v\ne0$
> $T0=\lambda0$ for every $\lambda$. With $v\ne0$, $\Span(v)$ is a one-dimensional invariant subspace, and conversely every such subspace comes from an eigenvector.

> [!remark]- Connections
> - Equivalent conditions: [[§14 Invariant Subspaces#^ladr-5-7|Equivalent conditions to be an eigenvalue]]. Existence over $\C$: [[Existence of eigenvalues]]. Zeros of the minimal polynomial: [[§15 The Minimal Polynomial#^ladr-5-27|Eigenvalues are the zeros of the minimal polynomial]].
> - Computational version: [[§32 Eigenvectors and Eigenvalues#^def-32-1|235 Def. §32.1]] (eigenvalues and eigenvectors of an $n\times n$ matrix, with worked examples).
> - Computational version: [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^def-29-4|331 Def. §29.4]] (the eigenvalues of a matrix as the roots of $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$, with worked examples).
> - Computational version: eigenvalues and eigenfunctions of differential operators with boundary conditions, such as $\phi''+\lambda^2\phi=0$ with fixed or insulated ends, [[§3★ Boundary Value Problems#^def-3-3|341 Def. §3.3]], [[§20 Example꞉ Insulated Bar#^def-20-1|341 Def. §20.1]], computed in worked examples.

> [!example] Example 5.6: Eigenvalue (p. 134)
> $T(x,y,z)=(7x+3z,\ 3x+6y+9z,\ -6y)$ on $\F^3$. Then
> $$
> T(3,1,-1)=(18,6,-6)=6\,(3,1,-1),
> $$
> so $6$ is an eigenvalue with eigenvector $(3,1,-1)$. Checking a guessed eigenvector is easy; finding eigenvalues is the hard direction (see [[§15 The Minimal Polynomial#^ladr-5-27|5.27]]).

^ladr-5-6

> [!theorem] Theorem 5.7: Equivalent conditions to be an eigenvalue
> Let $V$ be finite-dimensional, $T\in\Lin(V)$, $\lambda\in\F$. The following are equivalent:
> - (a) $\lambda$ is an eigenvalue of $T$;
> - (b) $T-\lambda I$ is not injective;
> - (c) $T-\lambda I$ is not surjective;
> - (d) $T-\lambda I$ is not invertible.

^ladr-5-7

> [!remark] Remark: Infinite dimensions
> (c) and (d) are then not equivalent to (a): this is why the spectrum of an operator on a Hilbert space ([[§21 Cauchy–Schwarz and the Induced Norm#^def-21-1|556 Def. §21.1]]) can contain points that are not eigenvalues (continuous spectrum).

> [!proof]+ Proof
> (a)$\iff$(b): $Tv=\lambda v\iff(T-\lambda I)v=0$, so a nonzero eigenvector is a nonzero element of $\nullsp(T-\lambda I)$ ([[§8 Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]]). (b)$\iff$(c)$\iff$(d) by [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]].

*Uses:* [[§8 Null Spaces and Ranges#^ladr-3-15|3.15]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]]

> [!remark]- Connections
> - Used in [[§15 The Minimal Polynomial#^ladr-5-32|T not invertible ⟺ constant term of minimal polynomial of T is 0]]. Determinant version: $\det(T-\lambda I)=0$ ([[Invertible ⟺ nonzero determinant]]).
> - Computational version: [[§33 The Characteristic Equation#^thm-33-4|235 Thm. §33.4]] ($\lambda$ is an eigenvalue of $A$ iff $\det(A-\lambda I)=0$, i.e. iff $A-\lambda I$ is not invertible) and [[§32 Eigenvectors and Eigenvalues#^thm-32-2|235 Thm. §32.2]] (the case $\lambda=0$).

> [!definition] Definition 5.8: Eigenvector
> If $\lambda$ is an eigenvalue of $T\in\Lin(V)$, a vector $v$ is an *eigenvector* for $\lambda$ if $v\ne0$ and $Tv=\lambda v$; equivalently $v\in\nullsp(T-\lambda I)\setminus\{0\}$.

^ladr-5-8

> [!remark]- Connections
> - Eigenvectors for distinct eigenvalues are independent: [[Linearly independent eigenvectors]]. The eigenspace $E(\lambda,T)=\nullsp(T-\lambda I)$: [[§17 Diagonalizable Operators#^ladr-5-52|Eigenspace, E(λ, T)]].
> - Computational version: [[§32 Eigenvectors and Eigenvalues#^def-32-1|235 Def. §32.1]] (eigenvectors of a matrix, found by row reducing $A-\lambda I$).

%% ex:5.8-plane %%
> [!example] Example: Eigenvectors in the plane
> Let $T(x,y)=(2x+y,\ x+2y)$ on $\R^2$. Then $T(1,1)=3(1,1)$ and $T(1,-1)=(1,-1)$: the lines $E(3,T)=\Span(1,1)$ and $E(1,T)=\Span(1,-1)$ are invariant, and on them $T$ just stretches (by $3$) or does nothing. A vector off these lines, like $x=(1,0)\mapsto(2,1)$, changes direction.
>
> $T$ maps the unit circle to an ellipse whose axes lie along the eigenvector lines, with semi-axes $3$ and $1$:
>
> ![[ladr-5.8-eigenlines.svg|360]]
>
> This matrix is symmetric, and the eigenvector lines are perpendicular. That is not a coincidence: see [[Real spectral theorem|7.29]], the real spectral theorem.

> [!example] Example 5.9: Eigenvalues and eigenvectors (p. 135)
> $T(w,z)=(-z,w)$ on $\F^2$.
>
> **(a) $\F=\R$.** $T$ is rotation by $90^\circ$ counterclockwise. No nonzero vector is sent to a multiple of itself, so $T$ has no eigenvalues:
>
> ![[ladr-5.9-rotation.svg|300]]
>
> **(b) $\F=\C$.** $T(w,z)=\lambda(w,z)$ means $-z=\lambda w$ and $w=\lambda z$. Then $-z=\lambda^2z$, and $z\ne0$ (otherwise $w=0$ too), so $\lambda^2=-1$: $\lambda=\pm i$. The eigenvectors are
> $$
> (w,-iw)\ \text{for }\lambda=i,\qquad (w,iw)\ \text{for }\lambda=-i,\qquad w\ne0 .
> $$
> The same operator has no eigenvalues over $\R$ and two over $\C$: eigenvalues depend on the field, which is why [[Existence of eigenvalues|5.19]] needs $\F=\C$. Physics: these complex eigenvectors are the circular polarization states of a rotation, $e^{\pm i\theta}$.

^ladr-5-9

> [!theorem] Theorem 5.11: Linearly independent eigenvectors
> Every list of eigenvectors of $T\in\Lin(V)$ corresponding to distinct eigenvalues is linearly independent.

^ladr-5-11

> [!proof]+ Proof
> Suppose not, and let $m$ be the smallest length of a linearly dependent list $v_1,\dots,v_m$ of eigenvectors with distinct eigenvalues $\lambda_1,\dots,\lambda_m$ ($m\ge2$, since eigenvectors are nonzero). Then $a_1v_1+\dots+a_mv_m=0$ with all $a_k\ne0$ (by minimality). Apply $T-\lambda_mI$:
> $$
> a_1(\lambda_1-\lambda_m)v_1+\dots+a_{m-1}(\lambda_{m-1}-\lambda_m)v_{m-1}=0 ,
> $$
> with all coefficients nonzero. This is a shorter dependent list, a contradiction.

> [!remark]- Connections
> - Computational version: [[§32 Eigenvectors and Eigenvalues#^thm-32-3|235 Thm. §32.3]] (the same statement for an $n\times n$ matrix).
> - Matrix version: [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-4|331 Thm. §29.4]] (with worked examples).

> [!theorem] Theorem 5.12: Operator cannot have more eigenvalues than dimension of vector space
> If $V$ is finite-dimensional, each operator on $V$ has at most $\dim V$ distinct eigenvalues.

^ladr-5-12

> [!proof]+ Proof
> Take one eigenvector for each of $m$ distinct eigenvalues. They are linearly independent by [[Linearly independent eigenvectors]], so $m\le\dim V$ by [[Length of linearly independent list ≤ length of spanning list]].

*Uses:* [[Linearly independent eigenvectors|5.11]], [[Length of linearly independent list ≤ length of spanning list|2.22]]

> [!remark]- Connections
> - Alternative proof: zeros of the minimal polynomial ([[§15 The Minimal Polynomial#^ladr-5-27|Eigenvalues are the zeros of the minimal polynomial]], [[Existence, uniqueness, and degree of minimal polynomial]], [[§13 Polynomials#^ladr-4-8|Degree m implies at most m zeros]]). With exactly $\dim V$ eigenvalues, $T$ is diagonalizable ([[§17 Diagonalizable Operators#^ladr-5-58|Enough eigenvalues implies diagonalizability]]).
> - Computational version: [[§32 Eigenvectors and Eigenvalues#^cor-32-4|235 Cor. §32.4]] (an $n\times n$ matrix has at most $n$ distinct eigenvalues).

> [!remark] Notation 5.13: Tᵐ (p. 137)
> For $T\in\Lin(V)$ and a positive integer $m$, $T^m=T\cdots T$ ($m$ factors); $T^0=I$; and if $T$ is invertible, $T^{-m}=(T^{-1})^m$.

^ladr-5-13

> [!remark] Notation 5.14: p(T) (p. 137)
> For $T\in\Lin(V)$ and $p\in\Poly(\F)$ with $p(z)=a_0+a_1z+\dots+a_mz^m$, $p(T)$ is the operator $a_0I+a_1T+\dots+a_mT^m$ on $V$.

^ladr-5-14

> [!example] Example 5.15: A polynomial applied to the differentiation operator (p. 138)
> With $D$ = differentiation on $\Poly(\R)$ and $p(x)=7-3x+5x^2$:
> $$
> p(D)=7I-3D+5D^2,\qquad \big(p(D)\big)q=7q-3q'+5q'' .
> $$
> For fixed $T$, the map $p\mapsto p(T)$ from $\Poly(\F)$ to $\Lin(V)$ is linear (and multiplicative, [[§14 Invariant Subspaces#^ladr-5-17|5.17]]). Physics: constant-coefficient linear ODEs are exactly equations $p(D)y=f$.

^ladr-5-15

> [!definition] Definition 5.16: Product of polynomials
> For $p,q\in\Poly(\F)$, the product $pq\in\Poly(\F)$ is $(pq)(z)=p(z)q(z)$.

^ladr-5-16

> [!remark] Remark: Polynomials of an operator
> For $T\in\Lin(V)$: $T^0=I$, $T^m=T\cdots T$ ($m$ factors), and for $p(z)=\sum_ja_jz^j$ one sets $p(T)=\sum_ja_jT^j$ ([[§14 Invariant Subspaces#^ladr-5-13|5.13]], [[§14 Invariant Subspaces#^ladr-5-14|5.14]]). The map $p\mapsto p(T)$ is linear ([[§14 Invariant Subspaces#^ladr-5-15|5.15]]).

> [!remark]- Connections
> - Multiplicativity: [[§14 Invariant Subspaces#^ladr-5-17|Multiplicative properties]].

> [!theorem] Theorem 5.17: Multiplicative properties
> For $p,q\in\Poly(\F)$ and $T\in\Lin(V)$:
> - (a) $(pq)(T)=p(T)q(T)$;
> - (b) $p(T)q(T)=q(T)p(T)$.

^ladr-5-17

> [!remark] Remark: Informally
> Expanding a product by distributivity does not care whether the symbol is $z$ or $T$: all powers of one operator commute.

> [!proof]+ Proof
> (a) With $p(z)=\sum_ja_jz^j$ and $q(z)=\sum_kb_kz^k$, $(pq)(z)=\sum_{j,k}a_jb_kz^{j+k}$, so
> $$
> (pq)(T)=\sum_{j,k}a_jb_kT^{j+k}=\Big(\sum_ja_jT^j\Big)\Big(\sum_kb_kT^k\Big)=p(T)q(T).
> $$
> (b) $p(T)q(T)=(pq)(T)=(qp)(T)=q(T)p(T)$ by (a) twice.

> [!remark]- Connections
> - Used constantly: [[§14 Invariant Subspaces#^ladr-5-18|Null space and range of p(T) are invariant under T]], [[Existence of eigenvalues]], [[§15 The Minimal Polynomial#^ladr-5-29|q(T) = 0 ⟺ q is a polynomial multiple of the minimal polynomial]].

> [!theorem] Theorem 5.18: Null space and range of p(T) are invariant under T
> For $T\in\Lin(V)$ and $p\in\Poly(\F)$, the subspaces $\nullsp p(T)$ and $\range p(T)$ are invariant under $T$.

^ladr-5-18

> [!proof]+ Proof
> If $p(T)u=0$ then $p(T)(Tu)=T(p(T)u)=T0=0$ (since $T$ commutes with $p(T)$, [[§14 Invariant Subspaces#^ladr-5-17|Multiplicative properties]]). If $u=p(T)v$ then $Tu=p(T)(Tv)\in\range p(T)$.

*Uses:* [[§14 Invariant Subspaces#^ladr-5-17|5.17]]

> [!remark]- Connections
> - Produces the invariant subspaces used in [[Existence, uniqueness, and degree of minimal polynomial]], [[§15 The Minimal Polynomial#^ladr-5-33|Even-dimensional null space]], [[§15 The Minimal Polynomial#^ladr-5-34|Operators on odd-dimensional vector spaces have eigenvalues]]; eigenspaces and generalized eigenspaces are special cases.
