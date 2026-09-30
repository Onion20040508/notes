---
type: section
subject: "[[Linear Algebra]]"
chapter: 1
section: "1C"
tags: [linear-algebra]
---
← [[Linear Algebra 1B Definition of Vector Space]] · ↑ [[Linear Algebra — 1 Vector Spaces]] · [[Linear Algebra 2A Span and Linear Independence]] →

> [!definition] 1.33 Subspace
> A subset $U\subseteq V$ is a *subspace* of $V$ if $U$ is itself a vector space with the same additive identity, addition and scalar multiplication as $V$.

^ladr-1-33

> [!remark]- Connections
> - The practical test: [[Linear Algebra 1C Subspaces#^ladr-1-34|Conditions for a subspace]]. Standard subspaces later: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-11|Null space, null T]], [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-16|Range]], eigenspaces, orthogonal complements [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-46|Orthogonal complement, U⟂]].

> [!theorem] 1.34 Conditions for a subspace
> A subset $U\subseteq V$ is a subspace of $V$ if and only if
> - **additive identity** $0\in U$;
> - **closed under addition** $u,w\in U \implies u+w\in U$;
> - **closed under scalar multiplication** $a\in\F,\ u\in U \implies au\in U$.

^ladr-1-34

> [!remark] Variant
> "$0\in U$" can be replaced by "$U\neq\varnothing$": take $u\in U$, then $0=0u\in U$ by [[Linear Algebra 1B Definition of Vector Space#^ladr-1-30|The number 0 times a vector]].

> [!proof]+
> If $U$ is a subspace, the three conditions hold by the definition of vector space.
>
> Conversely, assume the three conditions. The first puts the identity of $V$ in $U$; the second and third make addition and scalar multiplication operations on $U$. For $u\in U$, $-u=(-1)u\in U$ by [[Linear Algebra 1B Definition of Vector Space#^ladr-1-32|The number −1 times a vector]] and closure, so inverses exist in $U$. *(Filled in.)* The remaining axioms (commutativity, associativity, multiplicative identity, distributivity) are identities that hold for all vectors of $V$, hence in particular for those of $U$.

*Uses:* [[Linear Algebra 1B Definition of Vector Space#^ladr-1-32|1.32]]

> [!remark]- Connections
> - The workhorse for every 'is a subspace' claim: [[Linear Algebra 1C Subspaces#^ladr-1-40|Sum of subspaces is the smallest containing subspace]], [[Linear Algebra 2A Span and Linear Independence#^ladr-2-6|Span is the smallest containing subspace]], [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-11|Null space, null T]], [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-16|Range]].

> [!example] 1.35 Subspaces (p. 19)

^ladr-1-35

> [!definition] 1.36 Sum of subspaces
> For subspaces $V_1,\dots,V_m$ of $V$,
> $$
> V_1+\dots+V_m=\{v_1+\dots+v_m : v_k\in V_k\}.
> $$

^ladr-1-36

> [!remark]- Connections
> - It is the smallest subspace containing all $V_k$: [[Linear Algebra 1C Subspaces#^ladr-1-40|Sum of subspaces is the smallest containing subspace]]. When representations are unique: [[Linear Algebra 1C Subspaces#^ladr-1-41|Direct sum, ⊕]].

> [!example] 1.37 A sum of subspaces of F³ (p. 20)

^ladr-1-37

> [!example] 1.38 A sum of subspaces of F⁴ (p. 20)

^ladr-1-38

> [!theorem] 1.40 Sum of subspaces is the smallest containing subspace
> If $V_1,\dots,V_m$ are subspaces of $V$, then $V_1+\dots+V_m$ is the smallest subspace of $V$ containing $V_1,\dots,V_m$.

^ladr-1-40

> [!remark] Analogy
> Sums of subspaces play the role of unions of sets: the union of two subspaces is usually not a subspace, and the sum is the smallest subspace containing both.

> [!proof]+
> *(Filled in.)* $0=0+\dots+0$ lies in the sum;
> $(v_1+\dots+v_m)+(w_1+\dots+w_m)=(v_1+w_1)+\dots+(v_m+w_m)$ and $\lambda(v_1+\dots+v_m)=\lambda v_1+\dots+\lambda v_m$ stay in the sum because each $V_k$ is a subspace. So the sum is a subspace by [[Linear Algebra 1C Subspaces#^ladr-1-34|Conditions for a subspace]].
>
> It contains each $V_k$ (take all other summands $0$). Any subspace containing every $V_k$ is closed under finite sums, so it contains $V_1+\dots+V_m$.

*Uses:* [[Linear Algebra 1C Subspaces#^ladr-1-34|1.34]]

> [!remark]- Connections
> - Same shape of result: [[Linear Algebra 2A Span and Linear Independence#^ladr-2-6|Span is the smallest containing subspace]] for spans.

> [!definition] 1.41 Direct sum, ⊕
> Let $V_1,\dots,V_m$ be subspaces of $V$. The sum $V_1+\dots+V_m$ is a *direct sum* if every element of it can be written in only one way as $v_1+\dots+v_m$ with $v_k\in V_k$. In that case we write $V_1\oplus\dots\oplus V_m$.

^ladr-1-41

> [!remark]- Connections
> - Test with one vector: [[Condition for a direct sum]]. Two subspaces: [[Linear Algebra 1C Subspaces#^ladr-1-46|Direct sum of two subspaces]].
> - Direct sums organize the rest of the book: [[Linear Algebra 5D Diagonalizable Operators#^ladr-5-54|Sum of eigenspaces is a direct sum]], [[Linear Algebra 6C Orthogonal Complements and Minimization Problems#^ladr-6-49|Direct sum of a subspace and its orthogonal complement]], [[Generalized eigenspace decomposition]].
> - Physics: decomposing a state space into sectors (eigenspaces of a conserved quantity) is a direct-sum decomposition.

> [!example] 1.42 A direct sum of two subspaces (p. 21)

^ladr-1-42

> [!example] 1.43 A direct sum of multiple subspaces (p. 21)

^ladr-1-43

> [!example] 1.44 A sum that is not a direct sum (p. 21)

^ladr-1-44

> [!theorem] 1.45 Condition for a direct sum
> Let $V_1,\dots,V_m$ be subspaces of $V$. Then $V_1+\dots+V_m$ is a direct sum if and only if the only way to write $0=v_1+\dots+v_m$ with $v_k\in V_k$ is $v_1=\dots=v_m=0$.

^ladr-1-45

> [!proof]+
> ($\Rightarrow$) Uniqueness of representation applied to $0=0+\dots+0$.
>
> ($\Leftarrow$) Suppose $v=v_1+\dots+v_m=u_1+\dots+u_m$ with $v_k,u_k\in V_k$. Subtracting,
> $$
> 0=(v_1-u_1)+\dots+(v_m-u_m),\qquad v_k-u_k\in V_k,
> $$
> so every $v_k-u_k=0$ by hypothesis, i.e. the representation is unique.

> [!theorem] 1.46 Direct sum of two subspaces
> If $U,W$ are subspaces of $V$, then $U+W$ is a direct sum $\iff U\cap W=\{0\}$.

^ladr-1-46

> [!remark] Only for two subspaces
> Pairwise trivial intersections do not make a sum of three subspaces direct. In $\R^2$ take the lines spanned by $(1,0)$, $(0,1)$, $(1,1)$: all pairwise intersections are $\{0\}$, yet $(1,0)+(0,1)+(-1,-1)=0$.

> [!proof]+
> ($\Rightarrow$) If $v\in U\cap W$, then $0=v+(-v)$ with $v\in U$, $-v\in W$. Uniqueness of the representation of $0$ gives $v=0$.
>
> ($\Leftarrow$) By [[Condition for a direct sum]] it suffices to show: $0=u+w$ with $u\in U$, $w\in W$ forces $u=w=0$. From $u=-w\in W$ we get $u\in U\cap W=\{0\}$, so $u=0$ and then $w=0$.

*Uses:* [[Condition for a direct sum|1.45]]

> [!remark]- Connections
> - Used to build complements in [[Linear Algebra 2B Bases#^ladr-2-33|Every subspace of V is part of a direct sum equal to V]]. Dimension version: [[Linear Algebra 3E Products and Quotients of Vector Spaces#^ladr-3-94|A sum is a direct sum if and only if dimensions add up]].
