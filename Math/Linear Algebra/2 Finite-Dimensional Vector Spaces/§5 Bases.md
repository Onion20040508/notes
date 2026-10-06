---
type: section
subject: "[[Linear Algebra]]"
chapter: 2
section: 5
aliases: ["LADR 2B", "2B Bases"]
tags: [linear-algebra]
---
← [[§4 Span and Linear Independence]] · ↑ [[· 2 Finite-Dimensional Vector Spaces]] · [[§6 Dimension]] →

> [!definition] Definition 2.26: Basis
> A *basis* of $V$ is a list of vectors in $V$ that is linearly independent and spans $V$.

^ladr-2-26

> [!remark]- Connections
> - Characterization by unique coordinates: [[§5 Bases#^ladr-2-28|Criterion for basis]]. Existence: [[§5 Bases#^ladr-2-31|Basis of finite-dimensional vector space]]. All bases have the same length: [[§6 Dimension#^ladr-2-34|Basis length does not depend on basis]].
> - Computational version: [[§25 Linearly Independent Sets; Bases#^def-25-2|235 Def. §25.2]]; for subspaces of ℝⁿ, [[§18 Subspaces of ℝⁿ#^def-18-4|235 Def. §18.4]].

> [!example] Example 2.27: Bases (p. 39)
> - (a) $e_1,\dots,e_n$ is a basis of $\F^n$: the **standard basis**.
> - (b) $(1,2),(3,5)$ is a basis of $\F^2$ (independent since neither is a multiple of the other; see [[§6 Dimension#^ladr-2-38|2.38]]).
> - (c) $(1,2,-4),(7,-5,6)$ is independent in $\F^3$ but not a basis: two vectors cannot span $\F^3$ ([[Length of linearly independent list ≤ length of spanning list|2.22]]).
> - (d) $(1,2),(3,5),(4,13)$ spans $\F^2$ but is not a basis: three vectors in $\F^2$ are dependent.
> - (e) $(1,1,0),(0,0,1)$ is a basis of $\{(x,x,y)\}$.
> - (f) $(1,-1,0),(1,0,-1)$ is a basis of $\{(x,y,z):x+y+z=0\}$: indeed $(x,y,-x-y)=-y(1,-1,0)+(x+y)(1,0,-1)$, and the two vectors are independent.
> - (g) $1,z,\dots,z^m$ is a basis of $\Poly_m(\F)$: the **standard basis**.
>
> Bases are far from unique: $(7,5),(-4,9)$ is another basis of $\F^2$.

^ladr-2-27

> [!remark]- Connections
> - Computational version: [[§25 Linearly Independent Sets; Bases#^ex-25-2|235 Ex. §25.2]] (columns of an invertible matrix, and the standard bases of ℝⁿ, ℙₙ and the 2 × 2 matrices).

> [!theorem] Theorem 2.28: Criterion for basis
> A list $v_1,\dots,v_n$ in $V$ is a basis of $V$ iff every $v\in V$ can be written uniquely as
> $$
> v=a_1v_1+\dots+a_nv_n,\qquad a_1,\dots,a_n\in\F .
> $$

^ladr-2-28

> [!proof]+ Proof
> ($\Rightarrow$) Spanning gives existence. If also $v=c_1v_1+\dots+c_nv_n$, subtracting gives $0=\sum(a_k-c_k)v_k$, so all $a_k=c_k$ by independence.
>
> ($\Leftarrow$) Existence of representations means the list spans. Taking $v=0$, uniqueness says $0=\sum a_kv_k$ forces all $a_k=0$ (since $0=\sum 0\,v_k$ is one representation), i.e. independence.

> [!remark]- Connections
> - The unique $a_k$ are coordinates: [[§10 Invertibility and Isomorphisms#^ladr-3-73|Matrix of a vector, M(v)]]. Uniqueness is also what makes [[Linear map lemma]] work.
> - Computational version (the ⇒ direction): [[§26 Coordinate Systems#^thm-26-1|235 Thm. §26.1]] (the Unique Representation Theorem); for subspaces of ℝⁿ, [[§19 Dimension and Rank#^prop-19-1|235 Prop. §19.1]].

> [!theorem] Theorem 2.30: Every spanning list contains a basis
> Every spanning list in a vector space can be reduced to a basis of the vector space.

^ladr-2-30

> [!proof]+ Proof
> Let $v_1,\dots,v_n$ span $V$ and start with $B=v_1,\dots,v_n$. For $k=1,\dots,n$: if $v_k\in\Span(v_1,\dots,v_{k-1})$, delete $v_k$ from $B$; otherwise keep it (for $k=1$ this means: delete $v_1$ iff $v_1=0$).
>
> Only vectors already in the span of earlier ones are discarded, so $B$ still spans $V$. No vector of $B$ lies in the span of the earlier ones in $B$, so $B$ is linearly independent by [[Linear dependence lemma]]. Hence $B$ is a basis.

*Uses:* [[Linear dependence lemma|2.19]]

> [!remark]- Connections
> - Computational version: [[§25 Linearly Independent Sets; Bases#^thm-25-2|235 Thm. §25.2]] (the Spanning Set Theorem); for the columns of a matrix, the pivot columns are the basis kept, [[§25 Linearly Independent Sets; Bases#^thm-25-3|235 Thm. §25.3]].

> [!theorem] Theorem 2.31: Basis of finite-dimensional vector space
> Every finite-dimensional vector space has a basis.

^ladr-2-31

> [!proof]+ Proof
> By definition ([[§4 Span and Linear Independence#^ladr-2-9|Finite-dimensional vector space]]) it has a spanning list, which can be reduced to a basis by [[Every spanning list contains a basis]].

*Uses:* [[§4 Span and Linear Independence#^ladr-2-9|2.9]], [[Every spanning list contains a basis|2.30]]

> [!remark]- Connections
> - Makes [[§6 Dimension#^ladr-2-35|Dimension, dim V]] meaningful. Orthonormal refinement: [[§20 Orthonormal Bases#^ladr-6-35|Existence of orthonormal basis]].

> [!theorem] Theorem 2.32: Every linearly independent list extends to a basis
> Every linearly independent list in a finite-dimensional vector space can be extended to a basis.

^ladr-2-32

> [!proof]+ Proof
> Let $u_1,\dots,u_m$ be linearly independent in $V$ and let $w_1,\dots,w_n$ span $V$. Then $u_1,\dots,u_m,w_1,\dots,w_n$ spans $V$. Run the reduction procedure of [[Every spanning list contains a basis]] on this list. No $u_k$ is deleted, because $u_k\notin\Span(u_1,\dots,u_{k-1})$ by independence. The result is a basis consisting of $u_1,\dots,u_m$ and some $w$'s.

*Uses:* [[Every spanning list contains a basis|2.30]]

> [!remark]- Connections
> - Computational version: [[§27 The Dimension of a Vector Space#^thm-27-3|235 Thm. §27.3]] (a linearly independent set in H can be expanded to a basis of H); worked case in [[§25 Linearly Independent Sets; Bases#^ex-25-5|235 Ex. §25.5]](a).

> [!theorem] Theorem 2.33: Every subspace of V is part of a direct sum equal to V
> Suppose $V$ is finite-dimensional and $U$ is a subspace of $V$. Then there is a subspace $W$ of $V$ with $V=U\oplus W$.

^ladr-2-33

> [!proof]+ Proof
> $U$ is finite-dimensional ([[§4 Span and Linear Independence#^ladr-2-25|Finite-dimensional subspaces]]), so it has a basis $u_1,\dots,u_m$ ([[§5 Bases#^ladr-2-31|Basis of finite-dimensional vector space]]). As a linearly independent list in $V$ it extends to a basis $u_1,\dots,u_m,w_1,\dots,w_n$ of $V$ ([[Every linearly independent list extends to a basis]]). Let $W=\Span(w_1,\dots,w_n)$. By [[§3 Subspaces#^ladr-1-46|Direct sum of two subspaces]] it suffices to show $V=U+W$ and $U\cap W=\{0\}$.
>
> - Any $v\in V$ is $\underbrace{a_1u_1+\dots+a_mu_m}_{\in U}+\underbrace{b_1w_1+\dots+b_nw_n}_{\in W}$.
> - If $v\in U\cap W$, then $v=\sum a_ku_k=\sum b_jw_j$, so $\sum a_ku_k-\sum b_jw_j=0$ and all coefficients vanish by independence; hence $v=0$.

*Uses:* [[§4 Span and Linear Independence#^ladr-2-25|2.25]], [[§5 Bases#^ladr-2-31|2.31]], [[Every linearly independent list extends to a basis|2.32]], [[§3 Subspaces#^ladr-1-46|1.46]]

> [!remark] Remark: Not unique
> $W$ depends on the choice of extension: in $\R^2$ with $U$ the $x$-axis, every other line through $0$ is a complement. An inner product picks a canonical one, $U^\perp$ ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-49|Direct sum of a subspace and its orthogonal complement]]).

> [!remark]- Connections
> - Dimension count: $\dim W=\dim V-\dim U$, cf. [[§11 Products and Quotients of Vector Spaces#^ladr-3-105|Dimension of quotient space]] for $V/U$.
> - Infinite-dimensional version: [[§1 Linear Spaces#^prop-1-8|556 Prop. §1.8]] (every subspace has a complement), with Zorn's lemma ([[Zorn's Lemma|556 Thm. §5.2]]) in place of extending a basis.

%% ex:2.33-fig %%
> [!example] Example: Many complements, pictured
> In $\R^2$ with $U$ the $x$-axis (blue), both $W$ (red) and $W'$ (green) are complements: $\R^2=U\oplus W=U\oplus W'$. The same $v$ splits as $u+w$ with $w\in W$ and as $u'+w'$ with $w'\in W'$; the $U$-component depends on which complement was chosen.
>
> ![[ladr-2.33-complements.svg|400]]
