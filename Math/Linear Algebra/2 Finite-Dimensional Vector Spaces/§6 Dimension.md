---
type: section
subject: "[[Linear Algebra]]"
chapter: 2
section: 6
aliases: ["LADR 2C", "2C Dimension"]
tags: [linear-algebra]
---
← [[§5 Bases]] · ↑ [[· 2 Finite-Dimensional Vector Spaces]] · [[§7 Vector Space of Linear Maps]] →

> [!theorem] Theorem 2.34: Basis length does not depend on basis
> Any two bases of a finite-dimensional vector space have the same length.

^ladr-2-34

> [!proof]+ Proof
> Let $B_1,B_2$ be bases. $B_1$ is linearly independent and $B_2$ spans, so $\operatorname{len}B_1\le\operatorname{len}B_2$ by [[Length of linearly independent list ≤ length of spanning list]]. Swap roles for the reverse inequality.

*Uses:* [[Length of linearly independent list ≤ length of spanning list|2.22]]

> [!remark]- Connections
> - Allows the definition [[§6 Dimension#^ladr-2-35|Dimension, dim V]].
> - Computational version: [[§27 The Dimension of a Vector Space#^thm-27-2|235 Thm. §27.2]] (all bases have the same size).

> [!definition] Definition 2.35: Dimension, dim V
> The *dimension* of a finite-dimensional vector space $V$, written $\dim V$, is the length of any basis of $V$.

^ladr-2-35

> [!remark] Remark: Examples
> $\dim\F^n=n$; $\dim\Poly_m(\F)=m+1$. The field matters: $\dim_\C\C=1$ but $\dim_\R\C=2$.

> [!remark]- Connections
> - Well defined by [[§6 Dimension#^ladr-2-34|Basis length does not depend on basis]]. Classifies spaces up to isomorphism: [[Dimension shows whether vector spaces are isomorphic]].
> - Computational version: [[§27 The Dimension of a Vector Space#^def-27-1|235 Def. §27.1]]; for subspaces of ℝⁿ, [[§19 Dimension and Rank#^def-19-2|235 Def. §19.2]].

> [!example] Example 2.36: Dimensions (p. 44)
> - $\dim\F^n=n$ (standard basis).
> - $\dim\Poly_m(\F)=m+1$ (basis $1,z,\dots,z^m$).
> - $\dim\{(x,x,y)\}=2$ and $\dim\{(x,y,z):x+y+z=0\}=2$, by (e) and (f) of [[§5 Bases#^ladr-2-27|2.27]].

^ladr-2-36

> [!remark]- Connections
> - Computational version: [[§27 The Dimension of a Vector Space#^ex-27-1|235 Ex. §27.1]] (dim ℝⁿ = n, dim ℙₙ = n + 1, a plane in ℝ³).

> [!theorem] Theorem 2.37: Dimension of a subspace
> If $V$ is finite-dimensional and $U$ is a subspace of $V$, then $\dim U\le\dim V$.

^ladr-2-37

> [!proof]+ Proof
> A basis of $U$ is a linearly independent list in $V$, and a basis of $V$ spans $V$; apply [[Length of linearly independent list ≤ length of spanning list]].

*Uses:* [[Length of linearly independent list ≤ length of spanning list|2.22]]

> [!remark]- Connections
> - Equality case: [[§6 Dimension#^ladr-2-39|Subspace of full dimension equals the whole space]]. Used in [[§8 Null Spaces and Ranges#^ladr-3-22|Linear map to a lower-dimensional space is not injective]] and throughout Chapter 3.
> - Computational version: [[§27 The Dimension of a Vector Space#^thm-27-3|235 Thm. §27.3]] (dim H ≤ dim V).

> [!theorem] Theorem 2.38: Linearly independent list of the right length is a basis
> If $V$ is finite-dimensional, every linearly independent list in $V$ of length $\dim V$ is a basis of $V$.

^ladr-2-38

> [!proof]+ Proof
> Extend the list to a basis by [[Every linearly independent list extends to a basis]]. Every basis has length $\dim V$ ([[§6 Dimension#^ladr-2-34|Basis length does not depend on basis]]), so nothing was added.

*Uses:* [[Every linearly independent list extends to a basis|2.32]], [[§6 Dimension#^ladr-2-34|2.34]]

> [!remark]- Connections
> - Companion: [[§6 Dimension#^ladr-2-42|Spanning list of the right length is a basis]]. Consequence: [[§6 Dimension#^ladr-2-39|Subspace of full dimension equals the whole space]]. Orthonormal version: [[§20 Orthonormal Bases#^ladr-6-28|Orthonormal lists of the right length are orthonormal bases]].
> - Computational version: [[§27 The Dimension of a Vector Space#^thm-27-5|235 Thm. §27.5]] (the Basis Theorem, first half).
> - ODE example: two linearly independent solutions of $y'' + py' + qy = 0$ form a fundamental set, [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^def-14-3|331 Def. §14.3]]; for $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$, $n$ independent solutions, [[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-3|331 Def. §30.3]].

> [!theorem] Theorem 2.39: Subspace of full dimension equals the whole space
> If $V$ is finite-dimensional and $U$ is a subspace with $\dim U=\dim V$, then $U=V$.

^ladr-2-39

> [!proof]+ Proof
> A basis $u_1,\dots,u_n$ of $U$ is linearly independent in $V$ and has length $n=\dim V$, so it is a basis of $V$ by [[§6 Dimension#^ladr-2-38|Linearly independent list of the right length is a basis]]. Thus every $v\in V$ is a combination of the $u_k$, i.e. $v\in U$.

*Uses:* [[§6 Dimension#^ladr-2-38|2.38]]

> [!remark]- Connections
> - Typical use: to prove $U=V$, show $U\subseteq V$ and compare dimensions.
> - Computational version: [[§27 The Dimension of a Vector Space#^cor-27-6|235 Cor. §27.6]] (in particular, the only n-dimensional subspace of ℝⁿ is ℝⁿ).

> [!example] Example 2.40: A basis of F² (p. 46)
> $(5,7),(4,3)$ is independent in $\F^2$ (neither is a multiple of the other), and $\dim\F^2=2$. By [[§6 Dimension#^ladr-2-38|2.38]] it is a basis; spanning comes for free.

^ladr-2-40

> [!example] Example 2.41: A basis of a subspace of P3(R) (p. 46)
> Find a basis of $U=\{p\in\Poly_3(\R):p'(5)=0\}$.
>
> $1$, $(x-5)^2$, $(x-5)^3$ lie in $U$. They are independent: in $a+b(x-5)^2+c(x-5)^3=0$, the $x^3$ coefficient gives $c=0$, then the $x^2$ coefficient gives $b=0$, then $a=0$. So $3\le\dim U\le\dim\Poly_3(\R)=4$ ([[§6 Dimension#^ladr-2-37|2.37]]).
>
> $x\notin U$ (its derivative is $1$), so $U\ne\Poly_3(\R)$ and $\dim U\ne4$ ([[§6 Dimension#^ladr-2-39|2.39]]). Hence $\dim U=3$, and the independent list $1,(x-5)^2,(x-5)^3$ of length $3$ is a basis ([[§6 Dimension#^ladr-2-38|2.38]]).
>
> The strategy (squeeze $\dim U$ between an independent list and the ambient space, then use the right-length results) is the standard way to find bases of subspaces cut out by conditions.

^ladr-2-41

> [!theorem] Theorem 2.42: Spanning list of the right length is a basis
> If $V$ is finite-dimensional, every spanning list in $V$ of length $\dim V$ is a basis of $V$.

^ladr-2-42

> [!proof]+ Proof
> Reduce the list to a basis by [[Every spanning list contains a basis]]. Every basis has length $\dim V$ ([[§6 Dimension#^ladr-2-34|Basis length does not depend on basis]]), so nothing was removed.

*Uses:* [[Every spanning list contains a basis|2.30]], [[§6 Dimension#^ladr-2-34|2.34]]

> [!remark]- Connections
> - Companion: [[§6 Dimension#^ladr-2-38|Linearly independent list of the right length is a basis]]. Operator analogue: [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]] (injective $\iff$ surjective when $\dim V=\dim W$).
> - Computational version: [[§27 The Dimension of a Vector Space#^thm-27-5|235 Thm. §27.5]] (the Basis Theorem, second half).

> [!theorem] Theorem 2.43: Dimension of a sum
> If $V_1,V_2$ are subspaces of a finite-dimensional vector space, then
> $$
> \dim(V_1+V_2)=\dim V_1+\dim V_2-\dim(V_1\cap V_2).
> $$

^ladr-2-43

> [!remark] Remark: Analogy and its limit
> This mirrors $|A\cup B|=|A|+|B|-|A\cap B|$. The analogue of inclusion–exclusion fails for three subspaces (three distinct lines in $\R^2$ are a counterexample).

> [!proof]+ Proof
> Let $v_1,\dots,v_m$ be a basis of $V_1\cap V_2$. Extend it to a basis $v_1,\dots,v_m,u_1,\dots,u_j$ of $V_1$ and to a basis $v_1,\dots,v_m,w_1,\dots,w_k$ of $V_2$ ([[Every linearly independent list extends to a basis]]). We claim
> $$
> v_1,\dots,v_m,\;u_1,\dots,u_j,\;w_1,\dots,w_k \tag{$*$}
> $$
> is a basis of $V_1+V_2$; then $\dim(V_1+V_2)=m+j+k=(m+j)+(m+k)-m$.
>
> **Spans.** The span of $(*)$ lies in $V_1+V_2$ and contains both $V_1$ and $V_2$, hence equals $V_1+V_2$ ([[§3 Subspaces#^ladr-1-40|Sum of subspaces is the smallest containing subspace]]).
>
> **Independent.** Suppose $\sum a_iv_i+\sum b_iu_i+\sum c_iw_i=0$. Then $\sum c_iw_i=-\sum a_iv_i-\sum b_iu_i\in V_1$, and also $\in V_2$, so $\sum c_iw_i\in V_1\cap V_2$ and $\sum c_iw_i=\sum d_iv_i$ for some $d_i$. Since $v_1,\dots,v_m,w_1,\dots,w_k$ is independent, all $c_i=0$ (and $d_i=0$). Then $\sum a_iv_i+\sum b_iu_i=0$, and independence of the basis of $V_1$ gives all $a_i=b_i=0$.

*Uses:* [[Every linearly independent list extends to a basis|2.32]], [[§3 Subspaces#^ladr-1-40|1.40]]

> [!remark]- Connections
> - Direct-sum case: [[§11 Products and Quotients of Vector Spaces#^ladr-3-94|A sum is a direct sum if and only if dimensions add up]] ($\dim(V_1+V_2)=\dim V_1+\dim V_2 \iff V_1\cap V_2=\{0\}$).
> - Alternative proof via [[Fundamental theorem of linear maps]]: apply it to $T:V_1\times V_2\to V$, $T(x,y)=x+y$. Then $\range T=V_1+V_2$, $\nullsp T=\{(x,-x):x\in V_1\cap V_2\}\cong V_1\cap V_2$, and $\dim(V_1\times V_2)=\dim V_1+\dim V_2$ by [[§11 Products and Quotients of Vector Spaces#^ladr-3-92|Dimension of a product is the sum of dimensions]].
> - The counting version: inclusion–exclusion for two finite sets, [[§10 Counting#^prop-10-7|250 Prop. §10.7]].

%% ex:2.43-fig %%
> [!example] Example: Two planes in $\R^3$, pictured
> Two distinct planes $V_1$ (blue) and $V_2$ (red) through $0$ meet in a line. As in the proof: $v_1$ is a basis of $V_1\cap V_2$, extended by $u_1$ to a basis of $V_1$ and by $w_1$ to a basis of $V_2$. Then $v_1,u_1,w_1$ is a basis of $V_1+V_2=\R^3$, and $\dim(V_1+V_2)=2+2-1=3$.
>
> ![[ladr-2.43-dim-sum.svg|340]]
