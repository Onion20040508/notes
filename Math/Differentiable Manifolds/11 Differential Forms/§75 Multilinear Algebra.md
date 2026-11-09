---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 75
tags: [differentiable-manifolds, math591]
---
← · ↑ · →

*Stage: forms — Alternating multilinear forms on a vector space: the pointwise objects that differential forms are made of.*

*(Lecture 28.)* Forms are needed in every degree, not just two: this takes some multilinear algebra. Uribe thinks of these objects as minors of large determinants.

> [!definition] Definition §75.1: Linear $k$-Form
> Let $V$ be an $m$-dimensional real vector space and $k \in \{0, 1, 2, \ldots\}$. A **linear $k$-form** on $V$ is a multilinear map
>
> $$
> \alpha : \underbrace{V \times \cdots \times V}_{k} \longrightarrow \mathbb{R}
> $$
>
> (linear in each entry with the others fixed) that is **alternating**: exchanging two entries changes the sign,
>
> $$
> \alpha(v^1, \ldots, v^i, \ldots, v^j, \ldots, v^k) = -\alpha(v^1, \ldots, v^j, \ldots, v^i, \ldots, v^k) \qquad (i \neq j) .
> $$
>
> *Lee: Ch. 12, Symmetric and Alternating Tensors; Ch. 14, The Algebra of Alternating Tensors*

^def-75-1

The definition copies the determinant, which changes sign when two columns are exchanged. For $k = 1$ the alternating condition is empty and the linear $1$-forms are the covectors, $V^{\ast}$ (Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]]); for $k = 0$ the linear $0$-forms are, by convention, the scalars. On a manifold there will be one of these at each point, with $V$ the tangent space.

> [!example] Example §75.1: Linear $k$-Forms
> 1. On $\mathbb{R}^3$, each $dx^i \wedge dx^j$ (Definition [[§74 The Integrand Is a Two-Form#^def-74-1|§74.1]]) is a linear $2$-form, by Lemma [[§74 The Integrand Is a Two-Form#^lem-74-1|§74.1]](1).
> 2. On $\mathbb{R}^m$, the determinant $\alpha(v^1, \ldots, v^m) = \det(v^1 \cdots v^m)$ of the matrix with columns $v^1, \ldots, v^m$ is a linear $m$-form: it is linear in each column, and exchanging two columns changes its sign. For $m = 2$, $\det(v, w)$ is the signed area of the parallelogram spanned by $v$ and $w$ (figure below).
> 3. On $\mathbb{R}^m$, fix rows $1 \le i_1, \ldots, i_k \le m$. Let $\alpha(v^1, \ldots, v^k)$ be the $k \times k$ minor in the rows $i_1, \ldots, i_k$ of the $m \times k$ matrix with columns $v^1, \ldots, v^k$. Then $\alpha$ is a linear $k$-form, by the same two properties of the $k \times k$ determinant. This generalizes item 1, where $m = 3$, $k = 2$ and the rows are $i, j$.

^ex-75-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* (2) Multilinearity: expanding along the $j$-th column, $\det$ is a linear function of $v^j$ with the other columns fixed. Exchanging two columns changes the sign of a determinant. (3) The minor is the determinant of the $k \times k$ matrix whose $a$-th column is $(v^a_{i_1}, \ldots, v^a_{i_k})$; this column depends linearly on $v^a$, and exchanging $v^a$ and $v^{a'}$ exchanges two columns. So (2) applies. (1) is (3) with $m = 3$, $k = 2$, $(i_1, i_2) = (i, j)$, written with rows and columns exchanged, which does not change a determinant.

^pf-ex-75-1

> [!theorem] Lemma §75.1: Alternating Forms Vanish on Dependent Vectors
> Let $\alpha$ be a linear $k$-form on $V$ (Definition [[§75 Multilinear Algebra#^def-75-1|§75.1]]).
>
> 1. If two of the entries are equal, $v^i = v^j$ for some $i \neq j$, then $\alpha(v^1, \ldots, v^k) = 0$.
> 2. If $v^1, \ldots, v^k$ are linearly dependent, then $\alpha(v^1, \ldots, v^k) = 0$.

^lem-75-1

> [!proof]+ Proof
> *(Not from lecture; filled in, as in LADR, 9.28.)* (1) Exchanging the two equal entries does not change the list, but changes the sign of $\alpha$: $\alpha(v^1, \ldots, v^k) = -\alpha(v^1, \ldots, v^k)$, so the value is $0$.
>
> (2) Some $v^j$ is a linear combination of the others, $v^j = \sum_{i \neq j} c_i v^i$. By linearity of $\alpha$ in the $j$-th entry,
>
> $$
> \alpha(v^1, \ldots, v^j, \ldots, v^k) = \sum_{i \neq j} c_i\, \alpha(v^1, \ldots, \underbrace{v^i}_{j\text{-th entry}}, \ldots, v^k) ,
> $$
>
> and in the $i$-th term the vector $v^i$ appears twice, in the entries $i$ and $j$; by (1) every term is $0$.

^pf-75-1

> [!theorem] Corollary §75.2: No Nonzero $k$-Forms of Degree above the Dimension
> If $k > m = \dim V$, the only linear $k$-form on $V$ is $0$.

^cor-75-2

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Any $k > m$ vectors in the $m$-dimensional space $V$ are linearly dependent, so every value of a linear $k$-form is $0$ by Lemma [[§75 Multilinear Algebra#^lem-75-1|§75.1]](2).

^pf-75-2

*Uses:* [[§75 Multilinear Algebra#^lem-75-1|§75.1]]

![[m591-75-1.svg]]

*(Not from lecture; figure added.)* The $2$-form $\alpha = \det$ on $\mathbb{R}^2$ (Example [[§75 Multilinear Algebra#^ex-75-1|§75.1]](2)) as signed area. Left: $\alpha(v, w)$ is the area of the parallelogram spanned by $v$ and $w$, positive because $v$ turns to $w$ counterclockwise. Middle: exchanging the entries reverses the direction of turning and the sign, $\alpha(w, v) = -\alpha(v, w)$, the alternating condition of Definition [[§75 Multilinear Algebra#^def-75-1|§75.1]]. Right: for dependent vectors, here $w = 0.55\, v$, the parallelogram is flat and $\alpha(v, w) = 0$ (Lemma [[§75 Multilinear Algebra#^lem-75-1|§75.1]]).

> [!theorem] Proposition §75.3: The Space of $k$-Forms
> The set $\Lambda^k V$ of all linear $k$-forms on the $m$-dimensional space $V$ is a vector space, of dimension $\binom{m}{k}$.
>
> *Lee: Proposition 14.8*

^prop-75-3

> [!proof]+ Proof (to be filled)
> That linear combinations of alternating multilinear maps are again alternating and multilinear is immediate, so $\Lambda^k V$ is a subspace of the space of all functions $V^k \to \mathbb{R}$. The dimension, by writing down a basis, is for Lecture 29.

^pf-75-3

In particular $\Lambda^k V = 0$ for $k > m$ (this is Corollary [[§75 Multilinear Algebra#^cor-75-2|§75.2]], proved directly), and $\Lambda^m V$ is one-dimensional, spanned by the determinant in any basis. Lee writes $\Lambda^k(V^{\ast})$ for this space.

\appendix
