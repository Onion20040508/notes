---
type: section
subject: "[[Linear Algebra]]"
chapter: 9
section: 33
aliases: ["LADR 9B", "9B Alternating Multilinear Forms"]
tags: [linear-algebra]
---
← [[§32 Bilinear Forms and Quadratic Forms]] · ↑ [[· 9 Multilinear Algebra and Determinants]] · [[§34 Determinants]] →

> [!definition] Definition 9.24: Vᵐ
> $V^m=V\times\dots\times V$ ($m$ copies).

^ladr-9-24

> [!definition] Definition 9.25: M-linear form, V
> An *$m$-linear form* on $V$ is a function $\beta:V^m\to\F$ that is linear in each slot when the others are fixed. $V^{(m)}$ is the vector space of $m$-linear forms; a *multilinear form* is an $m$-linear form for some $m$.

^ladr-9-25

> [!remark] Remark: Special cases
> $1$-linear forms are functionals ($V^{(1)}=V'$), $2$-linear forms are bilinear forms.

> [!remark]- Connections
> - In the language of [[Differentiable Manifolds]]: covariant $m$-tensors on $V$.

> [!example] Example 9.26: M-linear forms (p. 346)
> - For $\alpha,\rho\in V^{(2)}$: $\beta(v_1,v_2,v_3,v_4)=\alpha(v_1,v_2)\rho(v_3,v_4)$ is $4$-linear (a tensor product of forms).
> - $\beta(T_1,\dots,T_m)=\operatorname{tr}(T_1\cdots T_m)$ is $m$-linear on $\Lin(V)$.

^ladr-9-26

> [!definition] Definition 9.27: Alternating forms, V⁽ᵐ⁾ alt
> An $m$-linear form $\alpha$ is *alternating* if $\alpha(v_1,\dots,v_m)=0$ whenever $v_j=v_k$ for some $j\ne k$. $V^{(m)}_{\mathrm{alt}}$ is the subspace of alternating $m$-linear forms.

^ladr-9-27

> [!remark]- Connections
> - These are exactly the $m$-covectors / values of differential $m$-forms at a point (Lee, Ch. 14).

> [!theorem] Theorem 9.28: Alternating multilinear forms and linear dependence
> If $\alpha$ is alternating $m$-linear and $v_1,\dots,v_m$ is linearly dependent, then $\alpha(v_1,\dots,v_m)=0$.

^ladr-9-28

> [!proof]+ Proof
> By [[Linear dependence lemma|2.19]] some $v_k=\sum_{j<k}b_jv_j$. Expanding in slot $k$, $\alpha(v_1,\dots,v_m)=\sum_{j<k}b_j\alpha(v_1,\dots,v_{k-1},v_j,v_{k+1},\dots,v_m)$, and each term has a repeated vector.

*Uses:* [[Linear dependence lemma|2.19]]

> [!theorem] Theorem 9.29: No nonzero alternating m-linear forms for m > dim V
> If $m>\dim V$, the only alternating $m$-linear form on $V$ is $0$.

^ladr-9-29

> [!proof]+ Proof
> Every list of length $m>\dim V$ is dependent ([[Length of linearly independent list ≤ length of spanning list|2.22]]); apply [[§33 Alternating Multilinear Forms#^ladr-9-28|9.28]].

*Uses:* [[Length of linearly independent list ≤ length of spanning list|2.22]], [[§33 Alternating Multilinear Forms#^ladr-9-28|9.28]]

> [!theorem] Theorem 9.30: Swapping input vectors in an alternating multilinear form
> Swapping the vectors in two slots of an alternating form multiplies its value by $-1$.

^ladr-9-30

> [!proof]+ Proof
> For the first two slots: $0=\alpha(v_1+v_2,v_1+v_2,v_3,\dots)=\alpha(v_1,v_2,\dots)+\alpha(v_2,v_1,\dots)$, since the terms with a repeated vector vanish. Any other pair of slots works the same way.

> [!definition] Definition 9.31: Permutation, perm m
> A *permutation* of $(1,\dots,m)$ is a list $(j_1,\dots,j_m)$ containing each of $1,\dots,m$ exactly once. $\operatorname{perm}m$ is the set of them ($m!$ elements).

^ladr-9-31

> [!remark]- Connections
> - As a group under composition this is the symmetric group, [[§3 Basic Examples of Groups#^def-3-5|493 Def. §3.5]], with two-line and cycle notation in [[§10 Cycle Notation and the Group S₃#^def-10-1|493 Def. §10.1]].

> [!definition] Definition 9.32: Sign of a permutation
> $\operatorname{sign}(j_1,\dots,j_m)=(-1)^N$, where $N$ is the number of pairs $k<l$ such that $k$ appears after $l$ in the list (the number of *inversions*).

^ladr-9-32

> [!remark]- Connections
> - Developed in 493: the sign via inversions, [[§20 The Sign Homomorphism and the Alternating Group#^def-20-2|493 Def. §20.2]], and its multiplicativity, [[The Sign Homomorphism]] (493 Thm. §20.3).
> - Same definition, by inversions, in 591: [[§10 Topological Groups and Classical Matrix Groups#^def-10-3|591 Def. §10.3]], with its properties in [[§10 Topological Groups and Classical Matrix Groups#^prop-10-2|591 Prop. §10.2]].

> [!example] Example 9.33: Signs (p. 349)
> - $\operatorname{sign}(1,\dots,m)=1$.
> - $\operatorname{sign}(2,1,3,4)=-1$ (one inversion).
> - $\operatorname{sign}(2,3,\dots,m,1)=(-1)^{m-1}$ (the inversions are the $m-1$ pairs involving $1$): a cyclic shift is even iff $m$ is odd.

^ladr-9-33

> [!theorem] Theorem 9.34: Swapping two entries in a permutation
> Swapping two entries of a permutation multiplies its sign by $-1$.

^ladr-9-34

> [!proof]+ Proof
> Swap entries $a$ and $b$. The pair $\{a,b\}$ itself changes status (inverted/not): a change of $\pm1$. For each entry $c$ strictly between them in position, the pairs $\{a,c\}$ and $\{b,c\}$ either both change status or neither does: a change of $-2$, $0$ or $2$. Pairs involving entries outside that stretch, or not involving $a$ or $b$, are unaffected. So $N$ changes by an odd number.

> [!remark]- Connections
> - Group form: a transposition has sign −1 and the sign is a homomorphism, [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-3|493 Thm. §20.3]], so parity is well defined, [[§20 The Sign Homomorphism and the Alternating Group#^cor-20-4|493 Cor. §20.4]].

> [!theorem] Theorem 9.35: Permutations and alternating multilinear forms
> If $\alpha\in V^{(m)}_{\mathrm{alt}}$, then $\alpha(v_{j_1},\dots,v_{j_m})=\operatorname{sign}(j_1,\dots,j_m)\,\alpha(v_1,\dots,v_m)$ for all $(j_1,\dots,j_m)\in\operatorname{perm}m$.

^ladr-9-35

> [!proof]+ Proof
> Reach $(1,\dots,m)$ from $(j_1,\dots,j_m)$ by swaps. Each swap flips the value of $\alpha$ ([[§33 Alternating Multilinear Forms#^ladr-9-30|9.30]]) and the sign of the permutation ([[§33 Alternating Multilinear Forms#^ladr-9-34|9.34]]); the identity has sign $1$.

*Uses:* [[§33 Alternating Multilinear Forms#^ladr-9-30|9.30]], [[§33 Alternating Multilinear Forms#^ladr-9-34|9.34]]

> [!theorem] Theorem 9.36: Formula for (dim V)-linear alternating forms on V
> Let $n=\dim V$, $e_1,\dots,e_n$ a basis, and $v_k=\sum_jb_{j,k}e_j$. For every alternating $n$-linear form $\alpha$,
> $$
> \alpha(v_1,\dots,v_n)=\alpha(e_1,\dots,e_n)\sum_{(j_1,\dots,j_n)\in\operatorname{perm}n}\operatorname{sign}(j_1,\dots,j_n)\,b_{j_1,1}\cdots b_{j_n,n}.
> $$

^ladr-9-36

> [!remark] Remark: Leibniz formula
> The sum is the determinant of the matrix $(b_{j,k})$ ([[§34 Determinants#^ladr-9-46|Formula for determinant of a matrix]]).

> [!proof]+ Proof
> Expand multilinearly: $\alpha(v_1,\dots,v_n)=\sum_{j_1,\dots,j_n}b_{j_1,1}\cdots b_{j_n,n}\,\alpha(e_{j_1},\dots,e_{j_n})$. Terms with a repeated index vanish, leaving permutations, and $\alpha(e_{j_1},\dots,e_{j_n})=\operatorname{sign}(j_1,\dots,j_n)\alpha(e_1,\dots,e_n)$ ([[§33 Alternating Multilinear Forms#^ladr-9-35|9.35]]).

*Uses:* [[§33 Alternating Multilinear Forms#^ladr-9-35|9.35]]

> [!theorem] Theorem 9.37: Dim V^(dim V) alt = 1
> $\dim V^{(\dim V)}_{\mathrm{alt}}=1$.

^ladr-9-37

> [!proof]+ Proof
> **At most one.** Let $\alpha\ne0$ and $\alpha'$ be alternating $n$-linear, with $\alpha(e_1,\dots,e_n)\ne0$; then $e_1,\dots,e_n$ is independent ([[§33 Alternating Multilinear Forms#^ladr-9-28|9.28]]), a basis. With $c$ such that $\alpha'(e)=c\,\alpha(e)$, [[§33 Alternating Multilinear Forms#^ladr-9-36|9.36]] gives $\alpha'(v_1,\dots,v_n)=c\,\alpha(v_1,\dots,v_n)$ for all $v$'s.
>
> **At least one.** With a basis $e$ and its dual basis $\varphi_1,\dots,\varphi_n$ ([[§12 Duality#^ladr-3-114|3.114]]), define
> $$
> \alpha(v_1,\dots,v_n)=\sum_{(j_1,\dots,j_n)\in\operatorname{perm}n}\operatorname{sign}(j_1,\dots,j_n)\,\varphi_{j_1}(v_1)\cdots\varphi_{j_n}(v_n).
> $$
> It is $n$-linear (each term is). Alternating: if $v_a=v_b$ ($a<b$), pair each permutation with the one obtained by swapping its entries in positions $a$ and $b$; the products agree and the signs are opposite ([[§33 Alternating Multilinear Forms#^ladr-9-34|9.34]]), so everything cancels. Nonzero: $\alpha(e_1,\dots,e_n)=1$ (only the identity permutation contributes).

*Uses:* [[§33 Alternating Multilinear Forms#^ladr-9-28|9.28]], [[§33 Alternating Multilinear Forms#^ladr-9-36|9.36]], [[§12 Duality#^ladr-3-114|3.114]], [[§33 Alternating Multilinear Forms#^ladr-9-34|9.34]]

> [!remark]- Connections
> - This one-dimensionality is what makes the determinant well defined ([[§34 Determinants#^ladr-9-41|Determinant of an operator, det T]]).

> [!theorem] Theorem 9.39: Alternating (dim V)-linear forms and linear independence
> Let $n=\dim V$ and $\alpha\ne0$ alternating $n$-linear. Then $\alpha(e_1,\dots,e_n)\ne0$ iff $e_1,\dots,e_n$ is linearly independent.

^ladr-9-39

> [!remark] Remark: Meaning
> A nonzero top-degree alternating form is a 'volume form': it detects whether $n$ vectors span a nondegenerate parallelepiped.

> [!proof]+ Proof
> ($\Rightarrow$) [[§33 Alternating Multilinear Forms#^ladr-9-28|9.28]]. ($\Leftarrow$) an independent list of length $n$ is a basis ([[§6 Dimension#^ladr-2-38|2.38]]); if $\alpha(e)=0$, [[§33 Alternating Multilinear Forms#^ladr-9-36|9.36]] would make $\alpha=0$.

*Uses:* [[§33 Alternating Multilinear Forms#^ladr-9-28|9.28]], [[§6 Dimension#^ladr-2-38|2.38]], [[§33 Alternating Multilinear Forms#^ladr-9-36|9.36]]

%% ex:9.39-fig %%
> [!example] Example: Independent versus dependent, pictured
> Think of a nonzero $\alpha\in V^{(3)}_{\mathrm{alt}}$ on $\R^3$ as a signed volume of the parallelepiped with edges $v_1,v_2,v_3$. Left: an independent list spans a solid parallelepiped and $\alpha\ne0$. Right: $v_3\in\Span(v_1,v_2)$, the parallelepiped is flattened into a plane, and $\alpha=0$ ([[§33 Alternating Multilinear Forms#^ladr-9-28|9.28]]).
>
> ![[ladr-9.39-volume-form.svg|440]]
