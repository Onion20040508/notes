---
type: section
subject: "[[Linear Algebra]]"
chapter: 3
section: "3B"
tags: [linear-algebra]
---
← [[Linear Algebra 3A Vector Space of Linear Maps]] · ↑ [[Linear Algebra — 3 Linear Maps]] · [[Linear Algebra 3C Matrices]] →

> [!definition] 3.11 Null space, null T
> For $T\in\Lin(V,W)$, the *null space* of $T$ is
> $$
> \nullsp T=\{v\in V : Tv=0\}.
> $$

^ladr-3-11

> [!remark]- Connections
> - A subspace: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-13|The null space is a subspace]]. Detects injectivity: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]]. Its dimension enters [[Fundamental theorem of linear maps]].
> - Called the kernel elsewhere; quotient by it: [[First isomorphism theorem]].

> [!example] 3.12 Null space (p. 59)
> - The zero map $V\to W$ has $\nullsp 0=V$.
> - $\varphi\in\Lin(\C^3,\C)$, $\varphi(z_1,z_2,z_3)=z_1+2z_2+3z_3$: $\nullsp\varphi$ is the plane $\{z_1+2z_2+3z_3=0\}$.
> - Differentiation $D$ on $\Poly(\R)$: $\nullsp D$ is the constant polynomials.
> - Multiplication by $x^2$: $\nullsp T=\{0\}$, since $x^2p(x)=0$ for all $x$ forces $p=0$.
> - Backward shift on $\F^\infty$: $\nullsp T=\{(a,0,0,\dots):a\in\F\}$.
>
> "Null" means zero; elsewhere this is called the *kernel*.

^ladr-3-12

> [!theorem] 3.13 The null space is a subspace
> If $T\in\Lin(V,W)$, then $\nullsp T$ is a subspace of $V$.

^ladr-3-13

> [!proof]+
> $T(0)=0$ by [[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-10|Linear maps take 0 to 0]], so $0\in\nullsp T$. If $u,v\in\nullsp T$ then $T(u+v)=Tu+Tv=0$. If $u\in\nullsp T$, $\lambda\in\F$, then $T(\lambda u)=\lambda Tu=0$. By [[Linear Algebra 1C Subspaces#^ladr-1-34|Conditions for a subspace]], $\nullsp T$ is a subspace.

*Uses:* [[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-10|3.10]], [[Linear Algebra 1C Subspaces#^ladr-1-34|1.34]]

> [!remark]- Connections
> - Companion: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-18|The range is a subspace]].

> [!definition] 3.14 Injective
> A function $T:V\to W$ is *injective* if $Tu=Tv$ implies $u=v$; equivalently, distinct inputs give distinct outputs.

^ladr-3-14

> [!remark]- Connections
> - For linear maps it suffices to test $0$: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]].

> [!theorem] 3.15 Injectivity ⟺ null space equals {0}
> Let $T\in\Lin(V,W)$. Then $T$ is injective if and only if $\nullsp T=\{0\}$.

^ladr-3-15

> [!proof]+
> ($\Rightarrow$) $\{0\}\subseteq\nullsp T$ by [[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-10|Linear maps take 0 to 0]]. If $v\in\nullsp T$ then $Tv=0=T(0)$, so $v=0$ by injectivity.
>
> ($\Leftarrow$) If $Tu=Tv$ then $T(u-v)=Tu-Tv=0$, so $u-v\in\nullsp T=\{0\}$, i.e. $u=v$.

*Uses:* [[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-10|3.10]]

> [!remark]- Connections
> - Same 'uniqueness at $0$' principle as [[Condition for a direct sum]] and [[Linear Algebra 2A Span and Linear Independence#^ladr-2-15|Linearly independent]].
> - Used in [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-22|Linear map to a lower-dimensional space is not injective]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]], [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-68|ST = I ⟺ TS = I (on vector spaces of the same dimension)]].

> [!definition] 3.16 Range
> For $T\in\Lin(V,W)$, the *range* of $T$ is
> $$
> \range T=\{Tv : v\in V\}\subseteq W.
> $$

^ladr-3-16

> [!remark] Spanned by images of a basis
> If $v_1,\dots,v_n$ spans $V$, then $\range T=\Span(Tv_1,\dots,Tv_n)$, since $T(\sum c_kv_k)=\sum c_kTv_k$.

> [!remark]- Connections
> - A subspace: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-18|The range is a subspace]]. Surjectivity: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-19|Surjective]]. Dimension = column rank of the matrix: [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-78|Dimension of range T equals column rank of M(T)]].

> [!example] 3.17 Range (p. 61)
> - The zero map has $\range 0=\{0\}$.
> - $T(x,y)=(2x,5y,x+y)$ from $\R^2$ to $\R^3$: $\range T=\{(2x,5y,x+y):x,y\in\R\}$, a plane in $\R^3$.
> - Differentiation $D$ on $\Poly(\R)$: $\range D=\Poly(\R)$, since every polynomial has a polynomial antiderivative.

^ladr-3-17

> [!theorem] 3.18 The range is a subspace
> If $T\in\Lin(V,W)$, then $\range T$ is a subspace of $W$.

^ladr-3-18

> [!proof]+
> $0=T(0)\in\range T$ by [[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-10|Linear maps take 0 to 0]]. If $w_1=Tv_1$, $w_2=Tv_2$, then $w_1+w_2=T(v_1+v_2)\in\range T$. If $w=Tv$ then $\lambda w=T(\lambda v)\in\range T$. Conclude by [[Linear Algebra 1C Subspaces#^ladr-1-34|Conditions for a subspace]].

*Uses:* [[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-10|3.10]], [[Linear Algebra 1C Subspaces#^ladr-1-34|1.34]]

> [!remark]- Connections
> - Companion: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-13|The null space is a subspace]].

> [!definition] 3.19 Surjective
> A function $T:V\to W$ is *surjective* if $\range T=W$.

^ladr-3-19

> [!remark] Depends on the target
> Differentiation $\Poly_5(\R)\to\Poly_5(\R)$ is not surjective ($x^5$ is missed), but as a map $\Poly_5(\R)\to\Poly_4(\R)$ it is.

> [!remark]- Connections
> - Dimension obstruction: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-24|Linear map to a higher-dimensional space is not surjective]]. Equivalent to injectivity when dimensions agree: [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]].

> [!example] 3.20 Surjectivity depends on the target space (p. 62)
> $D\in\Lin(\Poly_5(\R))$, $Dp=p'$, is not surjective: $x^5$ is not in the range, since derivatives of polynomials of degree $\le5$ have degree $\le4$. But $S\in\Lin(\Poly_5(\R),\Poly_4(\R))$, $Sp=p'$, is surjective. Surjectivity is a property of the map *together with its target* ([[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-19|3.19]]).

^ladr-3-20

> [!theorem] 3.21 Fundamental theorem of linear maps
> Suppose $V$ is finite-dimensional and $T \in \Lin(V, W)$. Then $\range T$ is finite-dimensional and
> $$
> \dim V = \dim \nullsp T + \dim \range T.
> $$

^ladr-3-21

> [!remark] Hypotheses
> Only $V$ is assumed finite-dimensional; $W$ may be infinite-dimensional. That is why "$\range T$ is finite-dimensional" is part of the conclusion rather than automatic.

> [!proof]+
> *(Filled in; implicit in Axler.)* $\nullsp T$ is a subspace of the finite-dimensional space $V$, hence finite-dimensional by [[Linear Algebra 2A Span and Linear Independence#^ladr-2-25|Finite-dimensional subspaces]]. Let $u_1, \dots, u_m$ be a basis of $\nullsp T$, so $\dim \nullsp T = m$.
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

*Uses:* [[Every linearly independent list extends to a basis|2.32]]

%% ex:3.21-fig %%
> [!example] The proof, pictured
> A map $T:\R^3\to\R^2$ with $\dim\nullsp T=1$. The basis $u_1$ of $\nullsp T$ (red) is extended by $v_1,v_2$ to a basis of $V$. All of $\nullsp T$ collapses to $0$, while $Tv_1,Tv_2$ (blue) form a basis of $\range T$. So $3=1+2$.
>
> ![[ladr-3.21-ftlm.svg|520]]

> [!theorem] 3.22 Linear map to a lower-dimensional space is not injective
> If $V,W$ are finite-dimensional and $\dim V>\dim W$, then no linear map $V\to W$ is injective.

^ladr-3-22

> [!proof]+
> For $T\in\Lin(V,W)$, by [[Fundamental theorem of linear maps]] and [[Linear Algebra 2C Dimension#^ladr-2-37|Dimension of a subspace]]:
> $$
> \dim\nullsp T=\dim V-\dim\range T\ \ge\ \dim V-\dim W\ >\ 0 .
> $$
> So $\nullsp T\neq\{0\}$ and $T$ is not injective by [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]].

*Uses:* [[Fundamental theorem of linear maps|3.21]], [[Linear Algebra 2C Dimension#^ladr-2-37|2.37]], [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-15|3.15]]

> [!remark]- Connections
> - Linear equations: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-26|Homogeneous system of linear equations]].

> [!example] 3.23 Linear map from F⁴ to F³ is not injective (p. 63)
> $T(z_1,z_2,z_3,z_4)=(\sqrt7z_1+\pi z_2+z_4,\ 97z_1+3z_2+2z_3,\ z_2+6z_3+7z_4)$ maps $\F^4\to\F^3$, so it is not injective by [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-22|3.22]], with no computation at all. This is the typical use of [[Fundamental theorem of linear maps|3.21]]: dimension counts decide injectivity and surjectivity before any calculation.

^ladr-3-23

> [!theorem] 3.24 Linear map to a higher-dimensional space is not surjective
> If $V,W$ are finite-dimensional and $\dim V<\dim W$, then no linear map $V\to W$ is surjective.

^ladr-3-24

> [!proof]+
> For $T\in\Lin(V,W)$, by [[Fundamental theorem of linear maps]],
> $$
> \dim\range T=\dim V-\dim\nullsp T\ \le\ \dim V\ <\ \dim W,
> $$
> so $\range T\neq W$.

*Uses:* [[Fundamental theorem of linear maps|3.21]]

> [!remark]- Connections
> - Linear equations: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-28|Inhomogeneous system of linear equations]].

> [!theorem] 3.26 Homogeneous system of linear equations
> A homogeneous system of linear equations with more variables than equations has nonzero solutions.

^ladr-3-26

> [!proof]+
> Write the system $\sum_{k=1}^n A_{j,k}x_k=0$ ($j=1,\dots,m$) as $T(x)=0$, where $T:\F^n\to\F^m$,
> $$
> T(x_1,\dots,x_n)=\Big(\sum_{k}A_{1,k}x_k,\ \dots,\ \sum_{k}A_{m,k}x_k\Big).
> $$
> $T$ is linear and nonzero solutions are nonzero elements of $\nullsp T$. If $n>m$, $T$ is not injective by [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-22|Linear map to a lower-dimensional space is not injective]], so $\nullsp T\neq\{0\}$ ([[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]]).

*Uses:* [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-22|3.22]], [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-15|3.15]]

> [!remark]- Connections
> - Also provable by Gaussian elimination; here it is pure dimension counting. Companion: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-28|Inhomogeneous system of linear equations]].

> [!theorem] 3.28 Inhomogeneous system of linear equations
> An inhomogeneous system of linear equations with more equations than variables has no solution for some choice of the constant terms.

^ladr-3-28

> [!proof]+
> With $T:\F^n\to\F^m$ as in [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-26|Homogeneous system of linear equations]], the system $\sum_kA_{j,k}x_k=c_j$ is solvable exactly when $(c_1,\dots,c_m)\in\range T$. If $n<m$, $T$ is not surjective by [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-24|Linear map to a higher-dimensional space is not surjective]], so some $(c_1,\dots,c_m)$ is not in the range.

*Uses:* [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-26|3.26]], [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-24|3.24]]

> [!remark]- Connections
> - Companion: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-26|Homogeneous system of linear equations]].
