---
type: section
subject: "[[Linear Algebra]]"
chapter: 3
section: 11
aliases: ["LADR 3E", "3E Products and Quotients of Vector Spaces"]
tags: [linear-algebra]
---
← [[§10 Invertibility and Isomorphisms]] · ↑ [[· 3 Linear Maps]] · [[§12 Duality]] →

> [!definition] 3.87 Product of vector spaces
> For vector spaces $V_1,\dots,V_m$ over $\F$, the *product* is
> $$
> V_1\times\dots\times V_m=\{(v_1,\dots,v_m) : v_k\in V_k\},
> $$
> with componentwise operations $(u_1,\dots,u_m)+(v_1,\dots,v_m)=(u_1+v_1,\dots,u_m+v_m)$ and $\lambda(v_1,\dots,v_m)=(\lambda v_1,\dots,\lambda v_m)$.

^ladr-3-87

> [!remark] Different spaces allowed
> The factors need not be subspaces of a common space; e.g. $\Poly_5(\R)\times\R^3$ consists of pairs (polynomial, vector).

> [!remark]- Connections
> - A vector space: [[§11 Products and Quotients of Vector Spaces#^ladr-3-89|Product of vector spaces is a vector space]]. Dimension: [[§11 Products and Quotients of Vector Spaces#^ladr-3-92|Dimension of a product is the sum of dimensions]]. Relation to sums inside one space: [[§11 Products and Quotients of Vector Spaces#^ladr-3-93|Products and direct sums]].

> [!theorem] 3.89 Product of vector spaces is a vector space
> If $V_1,\dots,V_m$ are vector spaces over $\F$, then $V_1\times\dots\times V_m$ is a vector space over $\F$.

^ladr-3-89

> [!proof]+
> *(Filled in; left to the reader in Axler.)* Every axiom of [[§2 Definition of Vector Space#^ladr-1-20|Vector space]] is checked slot by slot, where it holds because it holds in each $V_k$. The additive identity is $(0,\dots,0)$ (the $k$-th $0$ in $V_k$) and the inverse of $(v_1,\dots,v_m)$ is $(-v_1,\dots,-v_m)$.

*Uses:* [[§2 Definition of Vector Space#^ladr-1-20|1.20]]

> [!remark]- Connections
> - Same pattern as $\F^n=\F\times\dots\times\F$ ([[§1 Rⁿ and Cⁿ#^ladr-1-11|Fⁿ, coordinate]]).

> [!example] 3.90 $\R^2\times\R^3$ and $\R^5$ (p. 97)
> $\R^2\times\R^3\ne\R^5$: elements of the first are pairs $\big((x_1,x_2),(x_3,x_4,x_5)\big)$, elements of the second are lists of length $5$. But
> $$
> \big((x_1,x_2),(x_3,x_4,x_5)\big)\longmapsto(x_1,x_2,x_3,x_4,x_5)
> $$
> is an isomorphism so natural that one usually treats it as a relabeling.

^ladr-3-90

> [!example] 3.91 A basis of P2(R) × R2 (p. 97)
> $(1,(0,0)),\ (x,(0,0)),\ (x^2,(0,0)),\ (0,(1,0)),\ (0,(0,1))$ is a basis of $\Poly_2(\R)\times\R^2$, as in the proof of [[§11 Products and Quotients of Vector Spaces#^ladr-3-92|3.92]]: $\dim=3+2=5$.

^ladr-3-91

> [!theorem] 3.92 Dimension of a product is the sum of dimensions
> If $V_1,\dots,V_m$ are finite-dimensional, then $V_1\times\dots\times V_m$ is finite-dimensional and
> $$
> \dim(V_1\times\dots\times V_m)=\dim V_1+\dots+\dim V_m .
> $$

^ladr-3-92

> [!remark] Contrast with tensor products
> Dimensions add for products (and direct sums) but multiply for tensor products ([[§35 Tensor Products#^ladr-9-72|Dimension of the tensor product of two vector spaces]]). In quantum mechanics, combining independent systems uses the tensor product, not the product.

> [!proof]+
> Choose a basis of each $V_k$. For each basis vector $e$ of $V_k$, take the element of the product with $e$ in slot $k$ and $0$ elsewhere. *(Filled in.)* These span: $(v_1,\dots,v_m)$ is the sum over $k$ of ($v_k$ expanded in its basis, placed in slot $k$). They are independent: a vanishing combination vanishes slot by slot, and in slot $k$ it is a combination of a basis of $V_k$. So they form a basis, of length $\sum_k\dim V_k$.

> [!remark]- Connections
> - Used in [[§11 Products and Quotients of Vector Spaces#^ladr-3-94|A sum is a direct sum if and only if dimensions add up]] and in the alternative proof of [[§6 Dimension#^ladr-2-43|Dimension of a sum]].

> [!theorem] 3.93 Products and direct sums
> Let $V_1,\dots,V_m$ be subspaces of $V$ and define $\Gamma:V_1\times\dots\times V_m\to V_1+\dots+V_m$ by
> $$
> \Gamma(v_1,\dots,v_m)=v_1+\dots+v_m .
> $$
> Then $V_1+\dots+V_m$ is a direct sum if and only if $\Gamma$ is injective.

^ladr-3-93

> [!remark] Always surjective
> $\Gamma$ is onto by the definition of the sum, so "injective" can be replaced by "invertible": a direct sum is canonically isomorphic to the product.

> [!proof]+
> By [[§8 Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]], $\Gamma$ is injective iff the only way to write $0=v_1+\dots+v_m$ with $v_k\in V_k$ is with all $v_k=0$. By [[Condition for a direct sum]] this is exactly the condition for a direct sum.

*Uses:* [[§8 Null Spaces and Ranges#^ladr-3-15|3.15]], [[Condition for a direct sum|1.45]]

> [!remark]- Connections
> - Dimension version: [[§11 Products and Quotients of Vector Spaces#^ladr-3-94|A sum is a direct sum if and only if dimensions add up]].

> [!theorem] 3.94 A sum is a direct sum if and only if dimensions add up
> Suppose $V$ is finite-dimensional and $V_1,\dots,V_m$ are subspaces. Then $V_1+\dots+V_m$ is a direct sum if and only if
> $$
> \dim(V_1+\dots+V_m)=\dim V_1+\dots+\dim V_m .
> $$

^ladr-3-94

> [!remark] Case $m=2$
> Also follows from [[§3 Subspaces#^ladr-1-46|Direct sum of two subspaces]] and [[§6 Dimension#^ladr-2-43|Dimension of a sum]]: the sum is direct iff $V_1\cap V_2=\{0\}$ iff $\dim(V_1\cap V_2)=0$.

> [!proof]+
> $\Gamma$ in [[§11 Products and Quotients of Vector Spaces#^ladr-3-93|Products and direct sums]] is surjective, so by [[Fundamental theorem of linear maps]] it is injective iff $\dim(V_1+\dots+V_m)=\dim(V_1\times\dots\times V_m)$. Combine with [[§11 Products and Quotients of Vector Spaces#^ladr-3-93|Products and direct sums]] and [[§11 Products and Quotients of Vector Spaces#^ladr-3-92|Dimension of a product is the sum of dimensions]].

*Uses:* [[§11 Products and Quotients of Vector Spaces#^ladr-3-93|3.93]], [[Fundamental theorem of linear maps|3.21]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-92|3.92]]

> [!remark]- Connections
> - Used to show eigenspace and generalized-eigenspace decompositions fill $V$: [[§17 Diagonalizable Operators#^ladr-5-54|Sum of eigenspaces is a direct sum]], [[Generalized eigenspace decomposition]].

> [!remark] 3.95 Notation: V + U (p. 98)

^ladr-3-95

> [!example] 3.96 Sum of a vector and a one-dimensional subspace of R² (p. 99)
> $U=\{(x,2x):x\in\R\}$ is the line through $0$ of slope $2$. The translate $(17,20)+U$ is the parallel line through $(17,20)$. Since $(10,20)\in U$, it is $U$ moved $7$ units to the right.

^ladr-3-96

> [!definition] 3.97 Translate
> For $v\in V$ and a subset $U\subseteq V$, the set $v+U=\{v+u : u\in U\}$ is a *translate* of $U$.

^ladr-3-97

> [!remark] Picture
> For $U$ a line through $0$ in $\R^2$, the translates of $U$ are the lines parallel to $U$.

> [!remark]- Connections
> - Translates of a subspace partition $V$: [[§11 Products and Quotients of Vector Spaces#^ladr-3-101|Two translates of a subspace are equal or disjoint]]. They are the points of [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|Quotient space, V∕U]]. Solution sets of solvable inhomogeneous systems are translates of the null space.

> [!example] 3.98 Translates (p. 99)
> - For the line $U$ of [[§11 Products and Quotients of Vector Spaces#^ladr-3-96|3.96]], the translates of $U$ are all lines of slope $2$; for any line $U$ through $0$ in $\R^2$, they are all lines parallel to $U$.
> - For the plane $U=\{(x,y,0)\}$ in $\R^3$, the translates are the planes parallel to the $xy$-plane; likewise for any plane through $0$ in $\R^3$.

^ladr-3-98

> [!definition] 3.99 Quotient space, V∕U
> For a subspace $U$ of $V$, the *quotient space* $V/U$ is the set of all translates of $U$:
> $$
> V/U=\{v+U : v\in V\}.
> $$

^ladr-3-99

> [!remark]- Connections
> - Operations: [[§11 Products and Quotients of Vector Spaces#^ladr-3-102|Addition and scalar multiplication on V∕U]]. A vector space: [[§11 Products and Quotients of Vector Spaces#^ladr-3-103|Quotient space is a vector space]]. Dimension: [[§11 Products and Quotients of Vector Spaces#^ladr-3-105|Dimension of quotient space]].
> - Same construction as quotient groups and rings in abstract algebra (MATH 591 algebra part): $U$ plays the role of the normal subgroup/ideal.

> [!example] 3.100 Quotient spaces (p. 100)
> - $U=\{(x,2x)\}$: $\R^2/U$ is the set of all lines of slope $2$. Each line is **one point** of the quotient.
> - $U$ a line through $0$ in $\R^3$: $\R^3/U$ is the set of lines parallel to $U$ (a $2$-dimensional space, [[§11 Products and Quotients of Vector Spaces#^ladr-3-105|3.105]]).
> - $U$ a plane through $0$ in $\R^3$: $\R^3/U$ is the set of planes parallel to $U$ ($1$-dimensional).
>
> Two vectors give the same point of $V/U$ exactly when their difference lies in $U$ ([[§11 Products and Quotients of Vector Spaces#^ladr-3-101|3.101]]):
>
> ![[ladr-3.100-translates.svg|380]]

^ladr-3-100

> [!theorem] 3.101 Two translates of a subspace are equal or disjoint
> Let $U$ be a subspace of $V$ and $v,w\in V$. Then
> $$
> v-w\in U\iff v+U=w+U\iff (v+U)\cap(w+U)\neq\varnothing .
> $$

^ladr-3-101

> [!remark] Consequence
> Two translates of a subspace are equal or disjoint, so the translates partition $V$; "$v\sim w\iff v-w\in U$" is the corresponding equivalence relation.

> [!proof]+
> If $v-w\in U$ and $u\in U$, then $v+u=w+\big((v-w)+u\big)\in w+U$; so $v+U\subseteq w+U$, and symmetrically, hence equality. Equality trivially gives a nonempty intersection. If $v+u_1=w+u_2$ with $u_1,u_2\in U$, then $v-w=u_2-u_1\in U$.

> [!remark]- Connections
> - The key to well-definedness in [[§11 Products and Quotients of Vector Spaces#^ladr-3-103|Quotient space is a vector space]] and to $\nullsp\pi=U$ in [[§11 Products and Quotients of Vector Spaces#^ladr-3-105|Dimension of quotient space]].

> [!definition] 3.102 Addition and scalar multiplication on V∕U
> For a subspace $U$ of $V$, define on $V/U$:
> $$
> (v+U)+(w+U)=(v+w)+U,\qquad \lambda(v+U)=(\lambda v)+U .
> $$

^ladr-3-102

> [!remark] Needs checking
> A translate has many representatives, so one must show these formulas do not depend on the choices; this is done in [[§11 Products and Quotients of Vector Spaces#^ladr-3-103|Quotient space is a vector space]].

> [!remark]- Connections
> - Makes $\pi$ linear: [[§11 Products and Quotients of Vector Spaces#^ladr-3-104|Quotient map, π]].

> [!theorem] 3.103 Quotient space is a vector space
> If $U$ is a subspace of $V$, then $V/U$ with the operations of [[§11 Products and Quotients of Vector Spaces#^ladr-3-102|Addition and scalar multiplication on V∕U]] is a vector space.

^ladr-3-103

> [!proof]+
> **Well defined.** Suppose $v_1+U=v_2+U$ and $w_1+U=w_2+U$. By [[§11 Products and Quotients of Vector Spaces#^ladr-3-101|Two translates of a subspace are equal or disjoint]], $v_1-v_2,\ w_1-w_2\in U$, so $(v_1+w_1)-(v_2+w_2)\in U$ and $(v_1+w_1)+U=(v_2+w_2)+U$. Likewise $\lambda v_1-\lambda v_2=\lambda(v_1-v_2)\in U$ gives $(\lambda v_1)+U=(\lambda v_2)+U$.
>
> **Axioms.** *(Filled in.)* Each axiom for $V/U$ follows from the same axiom in $V$ applied to representatives, e.g. $(v+U)+(w+U)=(v+w)+U=(w+v)+U=(w+U)+(v+U)$. The zero is $0+U=U$ and $-(v+U)=(-v)+U$.

*Uses:* [[§11 Products and Quotients of Vector Spaces#^ladr-3-101|3.101]]

> [!remark]- Connections
> - Dimension: [[§11 Products and Quotients of Vector Spaces#^ladr-3-105|Dimension of quotient space]].

%% ex:3.103-fig %%
> [!example] Well-definedness, pictured
> In $\R^2$ with $U$ a line through $0$: $v_1,v_2$ lie on the same translate (blue), and so do $w_1,w_2$ (red). The sums $v_1+w_1$ and $v_2+w_2$ are different vectors, but they lie on the same translate (green), because $(v_1+w_1)-(v_2+w_2)=(v_1-v_2)+(w_1-w_2)\in U$. So the sum of two translates does not depend on the representatives.
>
> ![[ladr-3.103-well-defined.svg|400]]

> [!definition] 3.104 Quotient map, π
> For a subspace $U$ of $V$, the *quotient map* $\pi:V\to V/U$ is $\pi(v)=v+U$.

^ladr-3-104

> [!remark] Linear
> *(Filled in.)* $\pi(v+w)=(v+w)+U=(v+U)+(w+U)=\pi(v)+\pi(w)$ and $\pi(\lambda v)=\lambda\pi(v)$, directly from [[§11 Products and Quotients of Vector Spaces#^ladr-3-102|Addition and scalar multiplication on V∕U]].

> [!remark]- Connections
> - $\nullsp\pi=U$ and $\range\pi=V/U$: used in [[§11 Products and Quotients of Vector Spaces#^ladr-3-105|Dimension of quotient space]]. Factors every map through it: [[First isomorphism theorem]].

> [!theorem] 3.105 Dimension of quotient space
> If $V$ is finite-dimensional and $U$ is a subspace of $V$, then
> $$
> \dim V/U=\dim V-\dim U .
> $$

^ladr-3-105

> [!proof]+
> Let $\pi$ be the quotient map ([[§11 Products and Quotients of Vector Spaces#^ladr-3-104|Quotient map, π]]). $v+U=0+U\iff v\in U$ by [[§11 Products and Quotients of Vector Spaces#^ladr-3-101|Two translates of a subspace are equal or disjoint]], so $\nullsp\pi=U$; and $\range\pi=V/U$ by definition. Apply [[Fundamental theorem of linear maps]]: $\dim V=\dim U+\dim V/U$.

*Uses:* [[§11 Products and Quotients of Vector Spaces#^ladr-3-104|3.104]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-101|3.101]], [[Fundamental theorem of linear maps|3.21]]

> [!remark]- Connections
> - Compare with a complement $W$ ([[§5 Bases#^ladr-2-33|Every subspace of V is part of a direct sum equal to V]]): $V/U\cong W$, but the quotient needs no choice.
> - Dual counterpart: $\dim U^0=\dim V-\dim U$ ([[§12 Duality#^ladr-3-125|Dimension of the annihilator]]).

> [!remark] 3.106 Notation: ̃T (p. 102)

^ladr-3-106

> [!theorem] 3.107 Null space and range of $\tilde T$
> Let $T\in\Lin(V,W)$ and define $\tilde T:V/(\nullsp T)\to W$ by $\tilde T(v+\nullsp T)=Tv$. Then
> - (a) $\tilde T\circ\pi=T$, where $\pi:V\to V/(\nullsp T)$ is the quotient map;
> - (b) $\tilde T$ is injective;
> - (c) $\range\tilde T=\range T$;
> - (d) $V/(\nullsp T)$ and $\range T$ are isomorphic.

^ladr-3-107

> [!remark] First isomorphism theorem
> (d) is the vector-space case of $G/\ker\varphi\cong\operatorname{im}\varphi$. Taking dimensions with [[§11 Products and Quotients of Vector Spaces#^ladr-3-105|Dimension of quotient space]] recovers [[Fundamental theorem of linear maps]].

> [!proof]+
> *(Filled in: Axler 3.106.)* $\tilde T$ is well defined: if $v+\nullsp T=w+\nullsp T$ then $v-w\in\nullsp T$ ([[§11 Products and Quotients of Vector Spaces#^ladr-3-101|Two translates of a subspace are equal or disjoint]]), so $Tv=Tw$. It is linear because $T$ is and the operations on the quotient are computed on representatives.
>
> (a) $\tilde T(\pi(v))=\tilde T(v+\nullsp T)=Tv$.
>
> (b) If $\tilde T(v+\nullsp T)=0$ then $Tv=0$, so $v\in\nullsp T$ and $v+\nullsp T=0+\nullsp T$ ([[§11 Products and Quotients of Vector Spaces#^ladr-3-101|Two translates of a subspace are equal or disjoint]]). Thus $\nullsp\tilde T$ is trivial.
>
> (c) Immediate from the definition.
>
> (d) By (b) and (c), $\tilde T$ viewed as a map onto $\range T$ is an isomorphism.

*Uses:* [[§11 Products and Quotients of Vector Spaces#^ladr-3-101|3.101]]

%% ex:3.107-diff %%
> [!example] Differentiation, and "up to a constant"
> Let $D\in\Lin(\Poly_3(\R))$, $Dp=p'$. Then $\nullsp D$ is the constants and $\range D=\Poly_2(\R)$. The quotient $\Poly_3(\R)/\nullsp D$ is "polynomials up to an additive constant", and $\tilde D(p+\nullsp D)=p'$ is an isomorphism onto $\Poly_2(\R)$. Its inverse sends $q$ to the coset $\int q+\nullsp D$, i.e. "$\int q+C$": an indefinite integral is precisely an element of this quotient. Dimensions: $4-1=3$, as [[Fundamental theorem of linear maps|3.21]] predicts.
>
> The general picture: $T$ factors as surjection, isomorphism, inclusion.
>
> ![[ladr-3.107-first-iso.svg|320]]

