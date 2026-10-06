---
type: section
subject: "[[Linear Algebra]]"
chapter: 3
section: 8
aliases: ["LADR 3B", "3B Null Spaces and Ranges"]
tags: [linear-algebra]
---
← [[§7 Vector Space of Linear Maps]] · ↑ [[· 3 Linear Maps]] · [[§9 Matrices]] →

> [!definition] Definition 3.11: Null space, null T
> For $T\in\Lin(V,W)$, the *null space* of $T$ is
> $$
> \nullsp T=\{v\in V : Tv=0\}.
> $$

^ladr-3-11

> [!remark]- Connections
> - A subspace: [[§8 Null Spaces and Ranges#^ladr-3-13|The null space is a subspace]]. Detects injectivity: [[§8 Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]]. Its dimension enters [[Fundamental theorem of linear maps]].
> - Called the kernel elsewhere; quotient by it: [[First isomorphism theorem]].
> - Group version: the kernel and image of a homomorphism, [[§15 Homomorphisms#^def-15-2|493 Def. §15.2]].
> - Computational version: [[§24 Null Spaces, Column Spaces, and Linear Transformations#^def-24-5|235 Def. §24.5]] (kernel); for x ↦ Ax it is Nul A, [[§24 Null Spaces, Column Spaces, and Linear Transformations#^def-24-1|235 Def. §24.1]].

> [!example] Example 3.12: Null space (p. 59)
> - The zero map $V\to W$ has $\nullsp 0=V$.
> - $\varphi\in\Lin(\C^3,\C)$, $\varphi(z_1,z_2,z_3)=z_1+2z_2+3z_3$: $\nullsp\varphi$ is the plane $\{z_1+2z_2+3z_3=0\}$.
> - Differentiation $D$ on $\Poly(\R)$: $\nullsp D$ is the constant polynomials.
> - Multiplication by $x^2$: $\nullsp T=\{0\}$, since $x^2p(x)=0$ for all $x$ forces $p=0$.
> - Backward shift on $\F^\infty$: $\nullsp T=\{(a,0,0,\dots):a\in\F\}$.
>
> "Null" means zero; elsewhere this is called the *kernel*.

^ladr-3-12

> [!theorem] Theorem 3.13: The null space is a subspace
> If $T\in\Lin(V,W)$, then $\nullsp T$ is a subspace of $V$.

^ladr-3-13

> [!proof]+ Proof
> $T(0)=0$ by [[§7 Vector Space of Linear Maps#^ladr-3-10|Linear maps take 0 to 0]], so $0\in\nullsp T$. If $u,v\in\nullsp T$ then $T(u+v)=Tu+Tv=0$. If $u\in\nullsp T$, $\lambda\in\F$, then $T(\lambda u)=\lambda Tu=0$. By [[§3 Subspaces#^ladr-1-34|Conditions for a subspace]], $\nullsp T$ is a subspace.

*Uses:* [[§7 Vector Space of Linear Maps#^ladr-3-10|3.10]], [[§3 Subspaces#^ladr-1-34|1.34]]

> [!remark]- Connections
> - Companion: [[§8 Null Spaces and Ranges#^ladr-3-18|The range is a subspace]].
> - Group version: kernel and image of a homomorphism are subgroups, [[§15 Homomorphisms#^prop-15-2|493 Prop. §15.2]].
> - Computational version: [[§24 Null Spaces, Column Spaces, and Linear Transformations#^thm-24-1|235 Thm. §24.1]] (Nul A is a subspace; also [[§18 Subspaces of ℝⁿ#^thm-18-2|235 Thm. §18.2]]) and [[§24 Null Spaces, Column Spaces, and Linear Transformations#^thm-24-5|235 Thm. §24.5]] (kernel and range).
> - ODE example: the solutions of $L[y] = 0$ form the null space of the differential operator $L$, the principle of superposition, [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-2|331 Thm. §14.2]].

> [!definition] Definition 3.14: Injective
> A function $T:V\to W$ is *injective* if $Tu=Tv$ implies $u=v$; equivalently, distinct inputs give distinct outputs.

^ladr-3-14

> [!remark]- Connections
> - For linear maps it suffices to test $0$: [[§8 Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]].
> - Elementary version, for arbitrary functions: [[§9 Injections, Surjections and Bijections#^def-9-1|250 Def. §9.1]], part 1.
> - In ℝⁿ: [[§9 The Matrix of a Linear Transformation#^def-9-3|235 Def. §9.3]] (one-to-one).

> [!theorem] Theorem 3.15: Injectivity ⟺ null space equals {0}
> Let $T\in\Lin(V,W)$. Then $T$ is injective if and only if $\nullsp T=\{0\}$.

^ladr-3-15

> [!proof]+ Proof
> ($\Rightarrow$) $\{0\}\subseteq\nullsp T$ by [[§7 Vector Space of Linear Maps#^ladr-3-10|Linear maps take 0 to 0]]. If $v\in\nullsp T$ then $Tv=0=T(0)$, so $v=0$ by injectivity.
>
> ($\Leftarrow$) If $Tu=Tv$ then $T(u-v)=Tu-Tv=0$, so $u-v\in\nullsp T=\{0\}$, i.e. $u=v$.

*Uses:* [[§7 Vector Space of Linear Maps#^ladr-3-10|3.10]]

> [!remark]- Connections
> - Same 'uniqueness at $0$' principle as [[Condition for a direct sum]] and [[§4 Span and Linear Independence#^ladr-2-15|Linearly independent]].
> - Used in [[§8 Null Spaces and Ranges#^ladr-3-22|Linear map to a lower-dimensional space is not injective]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]], [[§10 Invertibility and Isomorphisms#^ladr-3-68|ST = I ⟺ TS = I (on vector spaces of the same dimension)]].
> - Group version: a homomorphism is injective iff its kernel is trivial, [[§15 Homomorphisms#^prop-15-3|493 Prop. §15.3]] (hub [[Injective iff Trivial Kernel]]).
> - Computational version: [[§9 The Matrix of a Linear Transformation#^thm-9-2|235 Thm. §9.2]] (one-to-one iff T(x) = 0 has only the trivial solution), tested on the standard matrix in [[§9 The Matrix of a Linear Transformation#^thm-9-3|235 Thm. §9.3]](b).

> [!definition] Definition 3.16: Range
> For $T\in\Lin(V,W)$, the *range* of $T$ is
> $$
> \range T=\{Tv : v\in V\}\subseteq W.
> $$

^ladr-3-16

> [!remark] Remark: Spanned by images of a basis
> If $v_1,\dots,v_n$ spans $V$, then $\range T=\Span(Tv_1,\dots,Tv_n)$, since $T(\sum c_kv_k)=\sum c_kTv_k$.

> [!remark]- Connections
> - A subspace: [[§8 Null Spaces and Ranges#^ladr-3-18|The range is a subspace]]. Surjectivity: [[§8 Null Spaces and Ranges#^ladr-3-19|Surjective]]. Dimension = column rank of the matrix: [[§10 Invertibility and Isomorphisms#^ladr-3-78|Dimension of range T equals column rank of M(T)]].
> - Computational version: [[§24 Null Spaces, Column Spaces, and Linear Transformations#^def-24-5|235 Def. §24.5]] (range); for x ↦ Ax it is Col A, [[§24 Null Spaces, Column Spaces, and Linear Transformations#^def-24-2|235 Def. §24.2]].

> [!example] Example 3.17: Range (p. 61)
> - The zero map has $\range 0=\{0\}$.
> - $T(x,y)=(2x,5y,x+y)$ from $\R^2$ to $\R^3$: $\range T=\{(2x,5y,x+y):x,y\in\R\}$, a plane in $\R^3$.
> - Differentiation $D$ on $\Poly(\R)$: $\range D=\Poly(\R)$, since every polynomial has a polynomial antiderivative.

^ladr-3-17

> [!theorem] Theorem 3.18: The range is a subspace
> If $T\in\Lin(V,W)$, then $\range T$ is a subspace of $W$.

^ladr-3-18

> [!proof]+ Proof
> $0=T(0)\in\range T$ by [[§7 Vector Space of Linear Maps#^ladr-3-10|Linear maps take 0 to 0]]. If $w_1=Tv_1$, $w_2=Tv_2$, then $w_1+w_2=T(v_1+v_2)\in\range T$. If $w=Tv$ then $\lambda w=T(\lambda v)\in\range T$. Conclude by [[§3 Subspaces#^ladr-1-34|Conditions for a subspace]].

*Uses:* [[§7 Vector Space of Linear Maps#^ladr-3-10|3.10]], [[§3 Subspaces#^ladr-1-34|1.34]]

> [!remark]- Connections
> - Companion: [[§8 Null Spaces and Ranges#^ladr-3-13|The null space is a subspace]].
> - Computational version: [[§24 Null Spaces, Column Spaces, and Linear Transformations#^thm-24-3|235 Thm. §24.3]] (Col A is a subspace) and [[§24 Null Spaces, Column Spaces, and Linear Transformations#^thm-24-5|235 Thm. §24.5]].

> [!definition] Definition 3.19: Surjective
> A function $T:V\to W$ is *surjective* if $\range T=W$.

^ladr-3-19

> [!remark] Remark: Depends on the target
> Differentiation $\Poly_5(\R)\to\Poly_5(\R)$ is not surjective ($x^5$ is missed), but as a map $\Poly_5(\R)\to\Poly_4(\R)$ it is.

> [!remark]- Connections
> - Dimension obstruction: [[§8 Null Spaces and Ranges#^ladr-3-24|Linear map to a higher-dimensional space is not surjective]]. Equivalent to injectivity when dimensions agree: [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]].
> - Elementary version, for arbitrary functions: [[§9 Injections, Surjections and Bijections#^def-9-1|250 Def. §9.1]], part 2.
> - In ℝⁿ: [[§9 The Matrix of a Linear Transformation#^def-9-2|235 Def. §9.2]] (onto).

> [!example] Example 3.20: Surjectivity depends on the target space (p. 62)
> $D\in\Lin(\Poly_5(\R))$, $Dp=p'$, is not surjective: $x^5$ is not in the range, since derivatives of polynomials of degree $\le5$ have degree $\le4$. But $S\in\Lin(\Poly_5(\R),\Poly_4(\R))$, $Sp=p'$, is surjective. Surjectivity is a property of the map *together with its target* ([[§8 Null Spaces and Ranges#^ladr-3-19|3.19]]).

^ladr-3-20

> [!theorem] Theorem 3.21: Fundamental theorem of linear maps
> Suppose $V$ is finite-dimensional and $T \in \Lin(V, W)$. Then $\range T$ is finite-dimensional and
> $$
> \dim V = \dim \nullsp T + \dim \range T.
> $$

^ladr-3-21

> [!proof]+ Proof
> *(First step filled in: Axler takes the finite-dimensionality of $\nullsp T$ for granted; the rest follows Axler's proof.)* $\nullsp T$ is a subspace of the finite-dimensional space $V$, hence finite-dimensional by [[§4 Span and Linear Independence#^ladr-2-25|Finite-dimensional subspaces]]. Let $u_1, \dots, u_m$ be a basis of $\nullsp T$, so $\dim \nullsp T = m$.
>
> By [[Every linearly independent list extends to a basis]], extend it to a basis $u_1, \dots, u_m, v_1, \dots, v_n$ of $V$, so $\dim V = m + n$. It remains to show that $Tv_1, \dots, Tv_n$ is a basis of $\range T$.
>
> **Spanning.** Any $v \in V$ can be written $v = a_1 u_1 + \dots + a_m u_m + b_1 v_1 + \dots + b_n v_n$. Applying $T$ kills every $u_k$ since $u_k \in \nullsp T$, so
> $$
> Tv = b_1 Tv_1 + \dots + b_n Tv_n .
> $$
> Hence $Tv_1, \dots, Tv_n$ spans $\range T$; in particular $\range T$ is finite-dimensional.
>
> **Linear independence.** Suppose $c_1 Tv_1 + \dots + c_n Tv_n = 0$. By linearity $T(c_1 v_1 + \dots + c_n v_n) = 0$, so $c_1 v_1 + \dots + c_n v_n \in \nullsp T$ and we can write
> $$
> c_1 v_1 + \dots + c_n v_n = d_1 u_1 + \dots + d_m u_m .
> $$
> Moving everything to one side gives a linear combination of the basis $u_1, \dots, u_m, v_1, \dots, v_n$ equal to $0$, so all $c_j$ (and $d_k$) are $0$.
>
> Therefore $\dim \range T = n$, and $\dim V = m + n = \dim \nullsp T + \dim \range T$.

*Uses:* [[§4 Span and Linear Independence#^ladr-2-25|2.25]], [[Every linearly independent list extends to a basis|2.32]]

> [!remark] Remark: Hypotheses
> Only $V$ is assumed finite-dimensional; $W$ may be infinite-dimensional. That is why "$\range T$ is finite-dimensional" is part of the conclusion rather than automatic.

%% ex:3.21-fig %%

> [!remark]- Connections
> - Group analogue for finite groups: |G| = |Ker α| · |Im α|, [[§41 The First and Second Isomorphism Theorems#^cor-41-2|493 Cor. §41.2]].
> - Matrix version: [[§19 Dimension and Rank#^thm-19-2|235 Thm. §19.2]] and [[§28 Rank#^thm-28-3|235 Thm. §28.3]] (the Rank Theorem, rank A + dim Nul A = n, with worked examples).

> [!example] Example: The proof, pictured
> A map $T:\R^3\to\R^2$ with $\dim\nullsp T=1$. The basis $u_1$ of $\nullsp T$ (red) is extended by $v_1,v_2$ to a basis of $V$. All of $\nullsp T$ collapses to $0$, while $Tv_1,Tv_2$ (blue) form a basis of $\range T$. So $3=1+2$.
>
> ![[ladr-3.21-ftlm.svg|520]]

> [!theorem] Theorem 3.22: Linear map to a lower-dimensional space is not injective
> If $V,W$ are finite-dimensional and $\dim V>\dim W$, then no linear map $V\to W$ is injective.

^ladr-3-22

> [!proof]+ Proof
> For $T\in\Lin(V,W)$, by [[Fundamental theorem of linear maps]] and [[§6 Dimension#^ladr-2-37|Dimension of a subspace]]:
> $$
> \dim\nullsp T=\dim V-\dim\range T\ \ge\ \dim V-\dim W\ >\ 0 .
> $$
> So $\nullsp T\neq\{0\}$ and $T$ is not injective by [[§8 Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]].

*Uses:* [[Fundamental theorem of linear maps|3.21]], [[§6 Dimension#^ladr-2-37|2.37]], [[§8 Null Spaces and Ranges#^ladr-3-15|3.15]]

> [!remark]- Connections
> - Linear equations: [[§8 Null Spaces and Ranges#^ladr-3-26|Homogeneous system of linear equations]].
> - Matrix version: [[§28 Rank#^cor-28-4|235 Cor. §28.4]] (dim Nul A ≥ n − m, so x ↦ Ax is not one-to-one when n > m).

> [!example] Example 3.23: Linear map from F⁴ to F³ is not injective (p. 63)
> $T(z_1,z_2,z_3,z_4)=(\sqrt7z_1+\pi z_2+z_4,\ 97z_1+3z_2+2z_3,\ z_2+6z_3+7z_4)$ maps $\F^4\to\F^3$, so it is not injective by [[§8 Null Spaces and Ranges#^ladr-3-22|3.22]], with no computation at all. This is the typical use of [[Fundamental theorem of linear maps|3.21]]: dimension counts decide injectivity and surjectivity before any calculation.

^ladr-3-23

> [!theorem] Theorem 3.24: Linear map to a higher-dimensional space is not surjective
> If $V,W$ are finite-dimensional and $\dim V<\dim W$, then no linear map $V\to W$ is surjective.

^ladr-3-24

> [!proof]+ Proof
> For $T\in\Lin(V,W)$, by [[Fundamental theorem of linear maps]],
> $$
> \dim\range T=\dim V-\dim\nullsp T\ \le\ \dim V\ <\ \dim W,
> $$
> so $\range T\neq W$.

*Uses:* [[Fundamental theorem of linear maps|3.21]]

> [!remark]- Connections
> - Linear equations: [[§8 Null Spaces and Ranges#^ladr-3-28|Inhomogeneous system of linear equations]].
> - Matrix version: [[§28 Rank#^cor-28-4|235 Cor. §28.4]] (rank A ≤ n < m, so x ↦ Ax is not onto).

> [!theorem] Theorem 3.26: Homogeneous system of linear equations
> A homogeneous system of linear equations with more variables than equations has nonzero solutions.

^ladr-3-26

> [!proof]+ Proof
> Write the system $\sum_{k=1}^n A_{j,k}x_k=0$ ($j=1,\dots,m$) as $T(x)=0$, where $T:\F^n\to\F^m$,
> $$
> T(x_1,\dots,x_n)=\Big(\sum_{k}A_{1,k}x_k,\ \dots,\ \sum_{k}A_{m,k}x_k\Big).
> $$
> $T$ is linear and nonzero solutions are nonzero elements of $\nullsp T$. If $n>m$, $T$ is not injective by [[§8 Null Spaces and Ranges#^ladr-3-22|Linear map to a lower-dimensional space is not injective]], so $\nullsp T\neq\{0\}$ ([[§8 Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]]).

*Uses:* [[§8 Null Spaces and Ranges#^ladr-3-22|3.22]], [[§8 Null Spaces and Ranges#^ladr-3-15|3.15]]

> [!remark]- Connections
> - Also provable by Gaussian elimination; here it is pure dimension counting. Companion: [[§8 Null Spaces and Ranges#^ladr-3-28|Inhomogeneous system of linear equations]].
> - Computational version: [[§7 Linear Independence#^thm-7-6|235 Thm. §7.6]] (more columns than rows means dependent columns), via free variables, [[§5 Solution Sets of Linear Systems#^cor-5-1|235 Cor. §5.1]].

> [!theorem] Theorem 3.28: Inhomogeneous system of linear equations
> An inhomogeneous system of linear equations with more equations than variables has no solution for some choice of the constant terms.

^ladr-3-28

> [!proof]+ Proof
> With $T:\F^n\to\F^m$ as in [[§8 Null Spaces and Ranges#^ladr-3-26|Homogeneous system of linear equations]], the system $\sum_kA_{j,k}x_k=c_j$ is solvable exactly when $(c_1,\dots,c_m)\in\range T$. If $n<m$, $T$ is not surjective by [[§8 Null Spaces and Ranges#^ladr-3-24|Linear map to a higher-dimensional space is not surjective]], so some $(c_1,\dots,c_m)$ is not in the range.

*Uses:* [[§8 Null Spaces and Ranges#^ladr-3-26|3.26]], [[§8 Null Spaces and Ranges#^ladr-3-24|3.24]]

> [!remark]- Connections
> - Companion: [[§8 Null Spaces and Ranges#^ladr-3-26|Homogeneous system of linear equations]].
> - Computational version: [[§4 The Matrix Equation Ax = b#^thm-4-3|235 Thm. §4.3]] (Ax = b is solvable for every b iff A has a pivot in every row, impossible when m > n).
