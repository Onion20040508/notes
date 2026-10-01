---
type: section
subject: "[[Linear Algebra]]"
chapter: 5
section: 15
aliases: ["LADR 5B", "5B The Minimal Polynomial"]
tags: [linear-algebra]
---
← [[§14 Invariant Subspaces]] · ↑ [[· 5 Eigenvalues and Eigenvectors]] · [[§16 Upper-Triangular Matrices]] →

> [!theorem] Theorem 5.19: Existence of eigenvalues
> Every operator on a finite-dimensional nonzero complex vector space has an eigenvalue.

^ladr-5-19

> [!remark] Remark: Both hypotheses are needed
> Over $\R$: rotation by $90^\circ$ on $\R^2$ has no eigenvalue. In infinite dimensions: multiplication by $z$ on $\Poly(\C)$ has no eigenvalue.

> [!proof]+ Proof
> Let $\dim V=n>0$, $T\in\Lin(V)$, and $v\ne0$. The $n+1$ vectors $v,Tv,\dots,T^nv$ are linearly dependent, so some nonconstant polynomial $p$ satisfies $p(T)v=0$; take one of smallest degree. By [[Fundamental theorem of algebra, first version]] it has a zero $\lambda\in\C$, and by [[§13 Polynomials#^ladr-4-6|Each zero of a polynomial corresponds to a degree-one factor]] $p(z)=(z-\lambda)q(z)$. Then, using [[§14 Invariant Subspaces#^ladr-5-17|Multiplicative properties]],
> $$
> 0=p(T)v=(T-\lambda I)\big(q(T)v\big).
> $$
> Since $\deg q<\deg p$, $q(T)v\ne0$, so $q(T)v$ is an eigenvector with eigenvalue $\lambda$.

*Uses:* [[Fundamental theorem of algebra, first version|4.12]], [[§13 Polynomials#^ladr-4-6|4.6]], [[§14 Invariant Subspaces#^ladr-5-17|5.17]]

> [!example] Example 5.20: An operator on a complex vector space with no eigenvalues (p. 143)
> $T\in\Lin(\Poly(\C))$, $(Tp)(z)=zp(z)$. For $p\ne0$, $\deg Tp=\deg p+1$, so $Tp$ is never a multiple of $p$: $T$ has **no eigenvalues**, even over $\C$. This does not contradict [[Existence of eigenvalues|5.19]] because $\Poly(\C)$ is infinite-dimensional. (Compare the position operator $\hat x$ in quantum mechanics, which has no eigenvectors in $L^2$.)

^ladr-5-20

> [!definition] Definition 5.21: Monic polynomial
> A *monic* polynomial is one whose highest-degree coefficient is $1$.

^ladr-5-21

> [!remark]- Connections
> - Normalizes the minimal polynomial so it is unique: [[Existence, uniqueness, and degree of minimal polynomial]], [[§15 The Minimal Polynomial#^ladr-5-24|Minimal polynomial]].

> [!theorem] Theorem 5.22: Existence, uniqueness, and degree of minimal polynomial
> If $V$ is finite-dimensional and $T\in\Lin(V)$, there is a unique monic $p\in\Poly(\F)$ of smallest degree with $p(T)=0$. Moreover $\deg p\le\dim V$.

^ladr-5-22

> [!remark] Remark: Crude bound versus sharp bound
> $\dim\Lin(V)=(\dim V)^2$ ([[§10 Invertibility and Isomorphisms#^ladr-3-72|Dim L(V, W) = (dim V)(dim W)]]) gives an annihilating polynomial of degree $\le(\dim V)^2$ for free; this result sharpens it to $\dim V$ without determinants.

> [!proof]+ Proof
> **Existence with the bound**, by induction on $\dim V$ (for all operators on all spaces over $\F$ of smaller dimension). If $\dim V=0$, take $p=1$. Otherwise pick $v\ne0$. The list $v,Tv,\dots,T^{\dim V}v$ is dependent, so by [[Linear dependence lemma]] there is a smallest $m\le\dim V$ with
> $$
> c_0v+c_1Tv+\dots+c_{m-1}T^{m-1}v+T^mv=0 .
> $$
> Let $q(z)=c_0+\dots+c_{m-1}z^{m-1}+z^m$. Then $q(T)(T^kv)=T^k(q(T)v)=0$ for all $k$, and $v,\dots,T^{m-1}v$ is independent (minimality of $m$), so $\dim\nullsp q(T)\ge m$ and $\dim\range q(T)\le\dim V-m$ ([[Fundamental theorem of linear maps]]). $\range q(T)$ is invariant ([[§14 Invariant Subspaces#^ladr-5-18|Null space and range of p(T) are invariant under T]]), so by induction there is a monic $s$ with $\deg s\le\dim V-m$ and $s(T|_{\range q(T)})=0$. Then $(sq)(T)v'=s(T)(q(T)v')=0$ for every $v'\in V$, and $sq$ is monic of degree $\le\dim V$.
>
> **Smallest degree and uniqueness.** *(Filled in.)* Among monic polynomials annihilating $T$ take one of smallest degree. If $p_1,p_2$ both qualify, $p_1-p_2$ has smaller degree and annihilates $T$; if it were nonzero, dividing by its leading coefficient would give a monic annihilator of smaller degree. So $p_1=p_2$.

*Uses:* [[Linear dependence lemma|2.19]], [[Fundamental theorem of linear maps|3.21]], [[§14 Invariant Subspaces#^ladr-5-18|5.18]]

> [!definition] Definition 5.24: Minimal polynomial
> For finite-dimensional $V$ and $T\in\Lin(V)$, the *minimal polynomial* of $T$ is the unique monic polynomial $p$ of smallest degree with $p(T)=0$.

^ladr-5-24

> [!remark] Remark: Computing it
> Find the smallest $m$ for which $c_0I+c_1T+\dots+c_{m-1}T^{m-1}=-T^m$ is solvable. Faster in practice: solve $c_0v+\dots+c_{n-1}T^{n-1}v=-T^nv$ for one vector $v$; if the solution is unique, $c_0,\dots,c_{n-1},1$ are the coefficients.

> [!remark]- Connections
> - Well defined by [[Existence, uniqueness, and degree of minimal polynomial]]. Eigenvalues are its zeros ([[§15 The Minimal Polynomial#^ladr-5-27|Eigenvalues are the zeros of the minimal polynomial]]); it divides every annihilating polynomial ([[§15 The Minimal Polynomial#^ladr-5-29|Q(T) = 0 ⟺ q is a polynomial multiple of the minimal polynomial]]); diagonalizability criterion: [[§17 Diagonalizable Operators#^ladr-5-62|Necessary and sufficient condition for diagonalizability]].

> [!example] Example 5.26: Minimal polynomial of an operator on F⁵ (p. 146)
> Let $T\in\Lin(\F^5)$ have matrix (standard basis)
> $$
> \mathcal{M}(T)=\begin{pmatrix}0&0&0&0&-3\\1&0&0&0&6\\0&1&0&0&0\\0&0&1&0&0\\0&0&0&1&0\end{pmatrix}.
> $$
> Use the fast method of [[§15 The Minimal Polynomial#^ladr-5-24|5.24]] with $v=e_1$: $Te_1=e_2$, $T^2e_1=e_3$, $T^3e_1=e_4$, $T^4e_1=e_5$, and $T^5e_1=Te_5=-3e_1+6e_2$. So
> $$
> 3e_1-6Te_1+T^5e_1=0 .
> $$
> Since $e_1,Te_1,\dots,T^4e_1$ is the standard basis (independent), this is the only relation of degree $\le5$, and the minimal polynomial is $z^5-6z+3$. (A matrix of this shape is a *companion matrix*: its last column lists the coefficients.)

^ladr-5-26

> [!theorem] Theorem 5.27: Eigenvalues are the zeros of the minimal polynomial
> Let $V$ be finite-dimensional and $T\in\Lin(V)$ with minimal polynomial $p$.
> - (a) The zeros of $p$ are exactly the eigenvalues of $T$.
> - (b) If $\F=\C$, then $p(z)=(z-\lambda_1)\cdots(z-\lambda_m)$ where $\lambda_1,\dots,\lambda_m$ lists all eigenvalues of $T$, possibly with repetitions.

^ladr-5-27

> [!proof]+ Proof
> (a) If $p(\lambda)=0$, write $p=(z-\lambda)q$ with $q$ monic ([[§13 Polynomials#^ladr-4-6|Each zero of a polynomial corresponds to a degree-one factor]]). Then $0=(T-\lambda I)(q(T)v)$ for all $v$. Since $\deg q<\deg p$, $q(T)\ne0$, so some $q(T)v\ne0$ is an eigenvector for $\lambda$.
>
> Conversely, if $Tv=\lambda v$ with $v\ne0$, then $T^kv=\lambda^kv$, so $0=p(T)v=p(\lambda)v$ and $p(\lambda)=0$.
>
> (b) Combine (a) with the factorization [[§13 Polynomials#^ladr-4-13|Fundamental theorem of algebra, second version]].

*Uses:* [[§13 Polynomials#^ladr-4-6|4.6]], [[§13 Polynomials#^ladr-4-13|4.13]]

> [!remark]- Connections
> - Alternative proof of [[§14 Invariant Subspaces#^ladr-5-12|Operator cannot have more eigenvalues than dimension of vector space]] via [[§13 Polynomials#^ladr-4-8|Degree m implies at most m zeros]]. Invertibility test: [[§15 The Minimal Polynomial#^ladr-5-32|T not invertible ⟺ constant term of minimal polynomial of T is 0]].

> [!example] Example 5.28: An operator whose eigenvalues cannot be found exactly (p. 147)
> $T(z_1,\dots,z_5)=(-3z_5,\ z_1+6z_5,\ z_2,\ z_3,\ z_4)$ on $\C^5$ is the operator of [[§15 The Minimal Polynomial#^ladr-5-26|5.26]], with minimal polynomial $z^5-6z+3$. Its eigenvalues are the zeros of that polynomial ([[§15 The Minimal Polynomial#^ladr-5-27|5.27]]), and none of them can be written with radicals. Numerically they are approximately
> $$
> -1.67,\quad 0.51,\quad 1.40,\quad -0.12\pm1.59\,i .
> $$
> The nonreal pair is conjugate, as [[§13 Polynomials#^ladr-4-14|4.14]] predicts for real coefficients. Eigenvalues exist ([[Existence of eigenvalues|5.19]]) but in general can only be computed numerically.

^ladr-5-28

%% ex:5.28-fig %%
> [!example] Example: The zeros of $z^5-6z+3$
> Three real zeros (blue) and one nonreal pair (red), mirror images of each other in the real axis ([[§13 Polynomials#^ladr-4-14|4.14]]).
>
> ![[ladr-5.28-roots.svg|320]]

> [!theorem] Theorem 5.29: Q(T) = 0 ⟺ q is a polynomial multiple of the minimal polynomial
> Let $V$ be finite-dimensional, $T\in\Lin(V)$, $q\in\Poly(\F)$. Then $q(T)=0$ iff $q$ is a polynomial multiple of the minimal polynomial $p$ of $T$.

^ladr-5-29

> [!proof]+ Proof
> ($\Rightarrow$) By [[§13 Polynomials#^ladr-4-9|Division algorithm for polynomials]], $q=ps+r$ with $\deg r<\deg p$. Then $0=q(T)=p(T)s(T)+r(T)=r(T)$. If $r\ne0$, dividing by its leading coefficient gives a monic annihilator of degree $<\deg p$, impossible. So $r=0$ and $q=ps$.
>
> ($\Leftarrow$) If $q=ps$ then $q(T)=p(T)s(T)=0$ ([[§14 Invariant Subspaces#^ladr-5-17|Multiplicative properties]]).

*Uses:* [[§13 Polynomials#^ladr-4-9|4.9]], [[§14 Invariant Subspaces#^ladr-5-17|5.17]]

> [!remark]- Connections
> - Minimal polynomial of a restriction divides: [[§15 The Minimal Polynomial#^ladr-5-31|Minimal polynomial of a restriction operator]]. With Cayley–Hamilton: minimal polynomial divides the characteristic polynomial ([[§29 Generalized Eigenspace Decomposition#^ladr-8-30|Characteristic polynomial is a multiple of minimal polynomial]]).

> [!theorem] Theorem 5.31: Minimal polynomial of a restriction operator
> If $V$ is finite-dimensional, $T\in\Lin(V)$, and $U$ is invariant under $T$, then the minimal polynomial of $T$ is a polynomial multiple of the minimal polynomial of $T|_U$.

^ladr-5-31

> [!proof]+ Proof
> Let $p$ be the minimal polynomial of $T$. Then $p(T)u=0$ for all $u\in U$, i.e. $p(T|_U)=0$. Apply [[§15 The Minimal Polynomial#^ladr-5-29|Q(T) = 0 ⟺ q is a polynomial multiple of the minimal polynomial]] to $T|_U$.

*Uses:* [[§15 The Minimal Polynomial#^ladr-5-29|5.29]]

> [!remark]- Connections
> - Used in the diagonalizability of restrictions: [[§17 Diagonalizable Operators#^ladr-5-65|Restriction of diagonalizable operator to invariant subspace]].

> [!theorem] Theorem 5.32: T not invertible ⟺ constant term of minimal polynomial of T is 0
> For finite-dimensional $V$ and $T\in\Lin(V)$: $T$ is not invertible $\iff$ the constant term of the minimal polynomial of $T$ is $0$.

^ladr-5-32

> [!remark] Remark: Inverse as a polynomial
> *(Filled in.)* If $p(z)=c_0+c_1z+\dots+z^m$ with $c_0\ne0$, then $T\big(c_1I+\dots+T^{m-1}\big)=-c_0I$, so $T^{-1}=-\tfrac1{c_0}\big(c_1I+c_2T+\dots+T^{m-1}\big)$ is a polynomial in $T$.

> [!proof]+ Proof
> $T$ not invertible $\iff0$ is an eigenvalue ([[§14 Invariant Subspaces#^ladr-5-7|Equivalent conditions to be an eigenvalue]]) $\iff0$ is a zero of $p$ ([[§15 The Minimal Polynomial#^ladr-5-27|Eigenvalues are the zeros of the minimal polynomial]](a)) $\iff p(0)=0$, and $p(0)$ is the constant term.

*Uses:* [[§14 Invariant Subspaces#^ladr-5-7|5.7]], [[§15 The Minimal Polynomial#^ladr-5-27|5.27]]

> [!remark]- Connections
> - Determinant analogue: [[Invertible ⟺ nonzero determinant]].

> [!theorem] Theorem 5.33: Even-dimensional null space
> Let $\F=\R$, $V$ finite-dimensional, $T\in\Lin(V)$, and $b,c\in\R$ with $b^2<4c$. Then $\dim\nullsp(T^2+bT+cI)$ is even.

^ladr-5-33

> [!proof]+ Proof
> $\nullsp(T^2+bT+cI)$ is invariant ([[§14 Invariant Subspaces#^ladr-5-18|Null space and range of p(T) are invariant under T]]); restricting to it, we may assume $T^2+bT+cI=0$ and must show $\dim V$ is even.
>
> $T$ has no eigenvectors: if $Tv=\lambda v$ then $0=(\lambda^2+b\lambda+c)v=\big((\lambda+\tfrac b2)^2+c-\tfrac{b^2}4\big)v$ and the scalar is positive, so $v=0$.
>
> Let $U$ be an invariant subspace of largest possible even dimension. If $U\ne V$, pick $w\notin U$ and let $W=\Span(w,Tw)$. $W$ is invariant since $T(Tw)=-bTw-cw$, and $\dim W=2$ (else $w$ is an eigenvector). $U\cap W=\{0\}$: it is invariant and properly contained in $W$ (as $w\notin U$), so if nonzero it would be a $1$-dimensional invariant subspace, i.e. an eigenvector line. By [[§6 Dimension#^ladr-2-43|Dimension of a sum]], $\dim(U+W)=\dim U+2$, and $U+W$ is invariant and even-dimensional, contradicting maximality. So $U=V$.

*Uses:* [[§14 Invariant Subspaces#^ladr-5-18|5.18]], [[§6 Dimension#^ladr-2-43|2.43]]

> [!remark]- Connections
> - Key lemma for [[§15 The Minimal Polynomial#^ladr-5-34|Operators on odd-dimensional vector spaces have eigenvalues]]. Complex-conjugate eigenvalue pairs of a real operator show up as such 2-dimensional invariant blocks.

> [!theorem] Theorem 5.34: Operators on odd-dimensional vector spaces have eigenvalues
> Every operator on an odd-dimensional vector space has an eigenvalue.

^ladr-5-34

> [!remark] Remark: Sharp
> In every even dimension there are real operators without eigenvalues (block-diagonal rotations).

> [!proof]+ Proof
> Over $\C$ this is [[Existence of eigenvalues]], so let $\F=\R$, $n=\dim V$ odd, and induct on $n$ in steps of $2$ ($n=1$ is trivial). Let $p$ be the minimal polynomial of $T$. If $x-\lambda$ divides $p$ for some real $\lambda$, then $\lambda$ is an eigenvalue ([[§15 The Minimal Polynomial#^ladr-5-27|Eigenvalues are the zeros of the minimal polynomial]](a)). Otherwise, by [[§13 Polynomials#^ladr-4-16|Factorization of a polynomial over R]], $p(x)=q(x)(x^2+bx+c)$ with $b^2<4c$ and $q$ monic. Then $q(T)$ vanishes on $\range(T^2+bT+cI)$; since $\deg q<\deg p$, this range is not all of $V$.
>
> By [[Fundamental theorem of linear maps]], $\dim V=\dim\nullsp(T^2+bT+cI)+\dim\range(T^2+bT+cI)$. The null space has even dimension ([[§15 The Minimal Polynomial#^ladr-5-33|Even-dimensional null space]]), so the range has odd dimension $<n$. It is invariant ([[§14 Invariant Subspaces#^ladr-5-18|Null space and range of p(T) are invariant under T]]), so by induction $T$ restricted to it has an eigenvalue, which is an eigenvalue of $T$.

*Uses:* [[Existence of eigenvalues|5.19]], [[§15 The Minimal Polynomial#^ladr-5-27|5.27]], [[§13 Polynomials#^ladr-4-16|4.16]], [[Fundamental theorem of linear maps|3.21]], [[§15 The Minimal Polynomial#^ladr-5-33|5.33]], [[§14 Invariant Subspaces#^ladr-5-18|5.18]]

> [!remark]- Connections
> - Physics: a rotation of $\R^3$ has a real eigenvalue by this result, necessarily $\pm1$ (norm-preserving; cf. [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-54|Eigenvalues of unitary operators have absolute value 1]]). For a proper rotation ($\det=1$), since the eigenvalues have modulus $1$, nonreal ones come in conjugate pairs with product $1$, and their product is $1$, the eigenvalue $1$ must occur: the rotation axis.
