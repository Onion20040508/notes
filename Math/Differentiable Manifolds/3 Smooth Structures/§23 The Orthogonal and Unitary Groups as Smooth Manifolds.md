---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 3
section: 23
tags: [differentiable-manifolds, math591]
---
← [[§22 The Differential of a Map Between Vector Spaces]] · ↑ [[· 3 Smooth Structures]] · [[§24 The Circle]] →

*Stage: linear — The matrix groups become smooth level sets: $\mathrm{O}(n)$ and $\mathrm{U}(n)$ by the regular value theorem, with the differential computed along straight lines.*

The classical groups through the course: defined in [[§11 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§16 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§13 Group Actions and Orbit Spaces#^ex-13-4|the rotations of the plane]] and [[§13 Group Actions and Orbit Spaces#^ex-13-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§14 Homogeneous Spaces#^ex-14-2|the isotropy of the north pole]] and [[§14 Homogeneous Spaces#^ex-14-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|the orthogonal group]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|the unitary group]]; their tangent spaces at the identity in [[§25 The Geometric Tangent Space#^thm-25-5|The Classical Groups]], with [[§25 The Geometric Tangent Space#^ex-25-4|the infinitesimal rotations]]; the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|The Double Cover]]; the Lie algebra $\mathfrak{so}(3)$ and the cross product in [[§50 Lie Bracket and Lie Algebra#^ex-50-3|Ex. §50.3]]; and Lie groups in [[§52 Lie Groups and Left-Invariant Vector Fields#^prop-52-1|§52.1]].

The promise of [[§12 The Classical Groups Are Topological Manifolds|§12, The Classical Groups Are Topological Manifolds]] can now be kept, with [[§22 The Differential of a Map Between Vector Spaces|The Differential of a Map Between Vector Spaces]] supplying the meaning of every step.

> [!definition] Definition §23.1: Symmetric Matrices as a Euclidean Space
> Let $\operatorname{Sym}(n,\mathbb{R}) = \{\, S \in \operatorname{Mat}(n,\mathbb{R}) \mid S^{\mathsf T} = S \,\}$. It is a linear subspace of $\operatorname{Mat}(n,\mathbb{R})$, and the entries on and above the diagonal are free while those below are determined, so
>
> $$
> \dim \operatorname{Sym}(n,\mathbb{R}) = n + (n-1) + \cdots + 1 = \frac{n(n+1)}{2}.
> $$
>
> Reading off those entries in a fixed order gives a linear isomorphism $\operatorname{Sym}(n,\mathbb{R}) \cong \mathbb{R}^{n(n+1)/2}$, which we use to regard maps into $\operatorname{Sym}(n,\mathbb{R})$ as maps into a Euclidean space. Being linear, it changes neither smoothness nor rank.

^def-23-1

> [!remark]- Connections
> - Symmetric matrices in LADR: [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-11|LADR 9.11]], the matrices of symmetric bilinear forms ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-9|LADR 9.9]]).

> [!example] Example §23.1: $\mathrm{O}(n)$ Is a Smooth Manifold of Dimension $\tfrac{n(n-1)}{2}$
> Define
>
> $$
> F : \operatorname{Mat}(n,\mathbb{R}) \longrightarrow \operatorname{Sym}(n,\mathbb{R}), \qquad F(g) = g\, g^{\mathsf T}.
> $$
>
> Then $\mathrm{O}(n) = F^{-1}(I)$, the identity $I$ is a regular value of $F$, and consequently $\mathrm{O}(n)$ is a smooth manifold of dimension $n^2 - \tfrac{n(n+1)}{2} = \tfrac{n(n-1)}{2}$.
>
> *Lee: Example 7.27*

^ex-23-1

> [!proof]+ Proof
> Four things have to be shown: $F$ is a smooth map into $\operatorname{Sym}(n,\mathbb{R})$; its level set $F^{-1}(I)$ is $\mathrm{O}(n)$; $dF_g$ is surjective at every $g \in F^{-1}(I)$; and this makes $\mathrm{O}(n)$ a smooth manifold of the stated dimension.
>
> *$F$ is well defined and smooth.* For $F$ to land in $\operatorname{Sym}(n,\mathbb{R})$ we need $F(g)^{\mathsf T} = F(g)$. Using $(PQ)^{\mathsf T} = Q^{\mathsf T} P^{\mathsf T}$ and $g^{\mathsf T\mathsf T} = (g^{\mathsf T})^{\mathsf T} = g$,
>
> $$
> (gg^{\mathsf T})^{\mathsf T} = g^{\mathsf T\mathsf T} g^{\mathsf T} = g g^{\mathsf T},
> $$
>
> so $F$ does land in $\operatorname{Sym}(n,\mathbb{R})$. For smoothness, take the linear coordinates $L$ on $\operatorname{Mat}(n,\mathbb{R})$ of Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-2|§11.2]] and $K$ on $\operatorname{Sym}(n,\mathbb{R})$ of Definition [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^def-23-1|§23.1]]. The components of the coordinate representation $K \circ F \circ L^{-1}$ (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-2|§22.2]]) are the entries $(gg^{\mathsf T})_{ij}$ with $i \le j$, and by the definition of the matrix product each of them is
>
> $$
> (gg^{\mathsf T})_{ij} = \sum_{m=1}^n g_{im}\,(g^{\mathsf T})_{mj} = \sum_{m=1}^n g_{im}\,g_{jm},
> $$
>
> a quadratic polynomial in the coordinates $g_{11}, \ldots, g_{nn}$ of Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-2|§11.2]]. Polynomials are smooth, so $K \circ F \circ L^{-1}$ is smooth, and $F$ is smooth by Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-3|§22.3]].
>
> *$\mathrm{O}(n) = F^{-1}(I)$.* By Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-5|§11.5]], $g \in \mathrm{O}(n) \iff g^{-1} = g^{\mathsf T} \iff gg^{\mathsf T} = I$. In detail, both inclusions: if $g \in \mathrm{O}(n)$, then $g^{-1} = g^{\mathsf T}$ by (i)$\Rightarrow$(iii) of Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-5|§11.5]], so $F(g) = gg^{\mathsf T} = gg^{-1} = I$. Conversely, let $F(g) = gg^{\mathsf T} = I$. Taking determinants, $\det(g)\det(g^{\mathsf T}) = \det I = 1$, so $\det g \neq 0$ and $g \in \mathrm{GL}(n,\mathbb{R})$; multiplying $gg^{\mathsf T} = I$ on the left by $g^{-1}$ gives $g^{\mathsf T} = g^{-1}$, which is (iii) of Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-5|§11.5]], so $g \in \mathrm{O}(n)$ by (iii)$\Rightarrow$(i).
>
> *The differential as a linear map.* *(Lecture 6: “We're not going to compute [the] Jacobian of this thing\ldots You use curves” — a technique he could “not emphasize enough”.)* $\operatorname{Mat}(n,\mathbb{R})$ and $\operatorname{Sym}(n,\mathbb{R})$ are finite-dimensional vector spaces and $F$ is smooth between them (first step), so by Theorem [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]], with $X = \operatorname{Mat}(n,\mathbb{R})$, $Y = \operatorname{Sym}(n,\mathbb{R})$, $p = g$ and $v = A$, the differential is computed along lines: for $g \in F^{-1}(I)$ and any $A \in \operatorname{Mat}(n,\mathbb{R})$,
>
> $$
> dF_g(A) = \frac{d}{dt}\Big|_{t=0} F(g+tA).
> $$
>
> Expanding, with $(g + tA)^{\mathsf T} = g^{\mathsf T} + tA^{\mathsf T}$ because transposition is linear, and multiplying out by distributivity,
>
> $$
> F(g+tA) = (g+tA)(g^{\mathsf T} + tA^{\mathsf T}) = g g^{\mathsf T} + t\big(A g^{\mathsf T} + g A^{\mathsf T}\big) + t^2 A A^{\mathsf T}.
> $$
>
> This is a polynomial in $t$ with matrix coefficients. Its derivative at $t = 0$ is the coefficient of $t$: the constant term $gg^{\mathsf T}$ contributes $0$, and the term $t^2 AA^{\mathsf T}$ has derivative $2t\,AA^{\mathsf T}$, which is $0$ at $t = 0$. So
>
> $$
> dF_g(A) = A g^{\mathsf T} + g A^{\mathsf T}.
> $$
>
> This is visibly symmetric, as it must be, $dF_g$ taking values in $\operatorname{Sym}(n,\mathbb{R})$: the transpose of a sum is the sum of the transposes, and $(Ag^{\mathsf T})^{\mathsf T} = gA^{\mathsf T}$, $(gA^{\mathsf T})^{\mathsf T} = Ag^{\mathsf T}$, so $(Ag^{\mathsf T} + gA^{\mathsf T})^{\mathsf T} = gA^{\mathsf T} + Ag^{\mathsf T}$.
>
> *$dF_g$ is surjective.* *(Lecture 6 observed that the left side is twice the symmetric part of a matrix, which is the substitution below; Lecture 7 finished with the explicit choice $A = \tfrac12 Sg$ — the equation “looks like a hard equation to solve until you realize that you have to use the fact that $S$ is symmetric and that $g$ is orthogonal.”)* Fix $g \in F^{-1}(I) = \mathrm{O}(n)$. We must show that every $S \in \operatorname{Sym}(n,\mathbb{R})$ is $dF_g(A)$ for some $A$. Put $X = Ag^{\mathsf T}$. Then $gA^{\mathsf T} = (g^{\mathsf T})^{\mathsf T} A^{\mathsf T} = (Ag^{\mathsf T})^{\mathsf T} = X^{\mathsf T}$, so that
>
> $$
> dF_g(A) = Ag^{\mathsf T} + gA^{\mathsf T} = X + X^{\mathsf T}.
> $$
>
> The map $A \mapsto Ag^{\mathsf T}$ is linear, and since $g$ is invertible so is $g^{\mathsf T}$; hence $A \mapsto Ag^{\mathsf T}$ is a linear *bijection* of $\operatorname{Mat}(n,\mathbb{R})$, with inverse $X \mapsto X (g^{\mathsf T})^{-1}$. So as $A$ runs over $\operatorname{Mat}(n,\mathbb{R})$, $X$ runs over all of $\operatorname{Mat}(n,\mathbb{R})$, and therefore
>
> $$
> \operatorname{im} dF_g = \{\, X + X^{\mathsf T} \mid X \in \operatorname{Mat}(n,\mathbb{R}) \,\} = \operatorname{Sym}(n,\mathbb{R}),
> $$
>
> the last equality because $X + X^{\mathsf T}$ is always symmetric ($(X + X^{\mathsf T})^{\mathsf T} = X^{\mathsf T} + X$), and conversely any symmetric $S$ arises from $X = \tfrac12 S$: $\tfrac12 S + (\tfrac12 S)^{\mathsf T} = \tfrac12 S + \tfrac12 S^{\mathsf T} = \tfrac12 S + \tfrac12 S = S$. Unwinding the substitution gives the matrix explicitly: $A = X (g^{\mathsf T})^{-1} = \tfrac12 S g$, using $(g^{\mathsf T})^{-1} = g$ for orthogonal $g$ (from $g^{\mathsf T} = g^{-1}$, the previous step). Directly, with $A = \tfrac12 Sg$:
>
> $$
> A g^{\mathsf T} = \tfrac12 S g g^{\mathsf T} = \tfrac12 S, \qquad
> g A^{\mathsf T} = g \big(\tfrac12 S g\big)^{\mathsf T} = \tfrac12 g\, g^{\mathsf T} S^{\mathsf T} = \tfrac12 S,
> $$
>
> using $(Sg)^{\mathsf T} = g^{\mathsf T} S^{\mathsf T}$, $gg^{\mathsf T} = I$ and $S^{\mathsf T} = S$; adding gives $dF_g(A) = S$.
>
> ![[m591-10-5.svg]]
>
> The same argument as a diagram: a bijection followed by symmetrization, which is onto. The unitary case in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds|§23]] has exactly this shape, with $^{\mathsf T}$ replaced by $^{\ast}$.
>
> *Conclusion.* $dF_g$ is surjective onto $\operatorname{Sym}(n,\mathbb{R})$ for every $g \in F^{-1}(I)$. By Corollary [[§22 The Differential of a Map Between Vector Spaces#^cor-22-4|§22.4]] (here $\dim \operatorname{Mat} = n^2 \ge \tfrac{n(n+1)}{2} = \dim \operatorname{Sym}$, since the difference is $\tfrac{n(n-1)}{2} \ge 0$), this says that in any linear coordinates the Jacobian has maximal rank $k = \tfrac{n(n+1)}{2}$ at every point of $F^{-1}(I)$, i.e. $I$ is a regular value (Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]]). Concretely, with the linear coordinates $L$ and $K$ of the first step, the coordinate representation $\widetilde F = K \circ F \circ L^{-1} : \mathbb{R}^{n^2} \to \mathbb{R}^{n(n+1)/2}$ is smooth, its Jacobian $\widetilde F'(L(g))$ has rank $k$ for every $g \in F^{-1}(I)$, and since $K$ is injective,
>
> $$
> \widetilde F(L(g)) = K(F(g)) = K(I) \iff F(g) = I, \qquad\text{so}\qquad \widetilde F^{-1}(K(I)) = L\big(F^{-1}(I)\big) = L(\mathrm{O}(n)).
> $$
>
> So $K(I)$ is a regular value of $\widetilde F$. Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]] applies with $W = \mathbb{R}^{n^2}$, $n + k = n^2$ and $k = \tfrac{n(n+1)}{2}$: $L(\mathrm{O}(n))$ is a smooth manifold of dimension $n^2 - \tfrac{n(n+1)}{2}$. The topology of $\mathrm{O}(n)$ is the subspace topology of $\operatorname{Mat}(n,\mathbb{R})$, defined by declaring $L$ a homeomorphism (Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-2|§11.2]]), so $L$ restricts to a homeomorphism $\mathrm{O}(n) \to L(\mathrm{O}(n))$; transporting the smooth structure along it (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]]) makes $\mathrm{O}(n)$ a smooth manifold of the same dimension, its charts being the graph charts composed with $L$. Finally
>
> $$
> n^2 - \frac{n(n+1)}{2} = \frac{2n^2 - n^2 - n}{2} = \frac{n(n-1)}{2}.
> $$

^pf-ex-23-1

*Uses:* [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^def-23-1|Def. §23.1]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-2|Def. §11.2]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-7|Def. §11.7]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-5|§11.5]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|Def. §22.4]], [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]], [[§22 The Differential of a Map Between Vector Spaces#^cor-22-4|§22.4]], [[§7 The Regular Value Theorem#^def-7-3|Def. §7.3]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-2|Def. §22.2]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-3|Def. §22.3]], [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]]

> [!remark]- Connections
> - $\mathrm{O}(n)$ as a group in 493: [[Matrix groups GLₙ, SLₙ and O(n)]]; the analogous level-set argument for $\mathrm{SL}(n,\mathbb{R})$: [[§12 The Classical Groups Are Topological Manifolds#^cor-12-5|§12.5]].
> - Its tangent spaces: [[§25 The Geometric Tangent Space#^ex-25-2|Ex. §25.2]]; all classical groups: [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]].
> - Used in Relativity: $\dim SO(3) = 3$ counts the rotation parameters when a proper orthochronous Lorentz transformation is written as a boost times a rotation — [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-6|REL Theorem §B1.2.6]].
> - Its dimension $\frac{n(n-1)}2$ plus $n$ eigenvalues gives $\frac{n(n+1)}2$, the dimension of the symmetric matrices of Definition §23.1: the parameter count of the spectral decomposition $M=O^{\mathsf T}\Lambda O$ of a symmetric matrix ([[§R2.6 Haar Measure and the Jacobian of the Spectral Decomposition#^thm-r2-6-3|Thesis Thm. §R2.6.3]]).

> [!remark] Remark
> **The codomain is not a cosmetic choice.** It is essential that $F$ be regarded as a map into $\operatorname{Sym}(n,\mathbb{R})$ and not into $\operatorname{Mat}(n,\mathbb{R})$. Since $F(g)$ is always symmetric, $\operatorname{im} F \subseteq \operatorname{Sym}(n,\mathbb{R}) \subsetneq \operatorname{Mat}(n,\mathbb{R})$, so $F'(g)$ could never be surjective onto $\operatorname{Mat}(n,\mathbb{R})$; with that codomain $I$ would fail to be a regular value at every point and the theorem would yield nothing. Choosing the codomain to be exactly the space the map lands in is what makes the rank condition attainable — and it is also what produces the right dimension count, since $\dim \mathrm{O}(n) = n^2 - \dim(\text{codomain})$.

^rem-23-1

> [!remark] Remark
> The smooth structure obtained is independent of the linear coordinates used to identify $\operatorname{Mat}(n,\mathbb{R})$ with $\mathbb{R}^{n^2}$ and $\operatorname{Sym}(n,\mathbb{R})$ with $\mathbb{R}^{n(n+1)/2}$: two such identifications differ by linear isomorphisms, which are diffeomorphisms, so the level set $F^{-1}(I)$ and its graph charts transport across them without change (Proposition [[§22 The Differential of a Map Between Vector Spaces#^prop-22-2|§22.2]]). “There's no ambiguity.”

^rem-23-2

> [!theorem] Proposition §23.1: The Kernel of the Differential
> With $F(g) = gg^{\mathsf T}$ as above, for every $g \in \mathrm{O}(n)$,
>
> $$
> \ker dF_g = \{\, A \in \operatorname{Mat}(n,\mathbb{R}) \mid gA^{\mathsf T} + Ag^{\mathsf T} = 0 \,\} = g \cdot \operatorname{Skew}(n,\mathbb{R}),
> $$
>
> where $\operatorname{Skew}(n,\mathbb{R}) = \{B \mid B^{\mathsf T} = -B\}$. In particular $\ker dF_I = \operatorname{Skew}(n,\mathbb{R})$, and $\dim \ker dF_g = \tfrac{n(n-1)}{2}$ for every $g$.

^prop-23-1

> [!proof]+ Proof
> *First equality.* By definition $\ker dF_g = \{A \in \operatorname{Mat}(n,\mathbb{R}) \mid dF_g(A) = 0\}$, and $dF_g(A) = Ag^{\mathsf T} + gA^{\mathsf T}$ was computed in the proof of Example [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|§23.1]]; matrix addition is commutative, so the condition reads $gA^{\mathsf T} + Ag^{\mathsf T} = 0$.
>
> *Second equality.* Since $g$ is invertible, every $A$ can be written uniquely as $A = gB$ with $B = g^{-1}A$ (the map $B \mapsto gB$ is a bijection of $\operatorname{Mat}(n,\mathbb{R})$ with inverse $A \mapsto g^{-1}A$). Substituting, and using $A^{\mathsf T} = (gB)^{\mathsf T} = B^{\mathsf T} g^{\mathsf T}$, then distributivity,
>
> $$
> gA^{\mathsf T} + Ag^{\mathsf T} = g B^{\mathsf T} g^{\mathsf T} + g B g^{\mathsf T} = g\,(B^{\mathsf T} + B)\,g^{\mathsf T}.
> $$
>
> As $g$ and $g^{\mathsf T}$ are invertible, this vanishes iff $B + B^{\mathsf T} = 0$: if $g(B^{\mathsf T} + B)g^{\mathsf T} = 0$, multiplying on the left by $g^{-1}$ and on the right by $(g^{\mathsf T})^{-1}$ gives $B^{\mathsf T} + B = 0$, and conversely $B^{\mathsf T} + B = 0$ makes the product $0$. And $B + B^{\mathsf T} = 0$ says $B^{\mathsf T} = -B$, i.e. $B$ is skew-symmetric. Hence $\ker dF_g = \{gB \mid B \in \operatorname{Skew}(n,\mathbb{R})\}$. At $g = I$ the description reads $\ker dF_I = \operatorname{Skew}(n,\mathbb{R})$ directly: $dF_I(A) = A^{\mathsf T} + A$.
>
> *Dimension.* Left multiplication by $g$, $B \mapsto gB$, is a linear isomorphism of $\operatorname{Mat}(n,\mathbb{R})$: it is linear since $g(B + B') = gB + gB'$ and $g(cB) = c\,gB$, and bijective with inverse $A \mapsto g^{-1}A$. By the second equality it maps the subspace $\operatorname{Skew}(n,\mathbb{R})$ onto $\ker dF_g$, and it is injective, so it restricts to a linear isomorphism $\operatorname{Skew}(n,\mathbb{R}) \to \ker dF_g$. So $\dim \ker dF_g = \dim \operatorname{Skew}(n,\mathbb{R})$ for every $g$.
>
> *Counting.* The condition $B^{\mathsf T} = -B$ says $B_{ji} = -B_{ij}$ for all $i, j$. For $i = j$ it gives $B_{ii} = -B_{ii}$, so a skew-symmetric matrix has zero diagonal; for $i < j$ it says that the entry $B_{ji}$ below the diagonal is the negative of the entry $B_{ij}$ above. Conversely, any choice of the entries $B_{ij}$ with $i < j$, completed by $B_{ii} = 0$ and $B_{ji} = -B_{ij}$, is skew-symmetric. So $B$ is determined by the $\tfrac{n(n-1)}{2}$ entries strictly above the diagonal, which may be chosen freely — reading them off is a linear isomorphism $\operatorname{Skew}(n,\mathbb{R}) \cong \mathbb{R}^{n(n-1)/2}$, the number of positions $(i,j)$ with $i < j$ being $(n-1) + (n-2) + \cdots + 1 + 0 = \binom{n}{2}$:
>
> $$
> B = \begin{pmatrix} 0 & \ast \\ -(\ast)^{\mathsf T} & \ddots \end{pmatrix}, \qquad \dim \operatorname{Skew}(n,\mathbb{R}) = \binom{n}{2} = \frac{n(n-1)}{2}.
> $$

^pf-23-1

*Uses:* [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|Ex. §23.1]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|Def. §22.5]]

> [!remark]- Connections
> - This kernel is the geometric tangent space $T^{\mathrm{geo}}_g\mathrm{O}(n)$: [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], [[§25 The Geometric Tangent Space#^ex-25-2|Ex. §25.2]].
> - Varying $O$ in $M=O^{\mathsf T}\Lambda O$ moves it along this tangent space, $\delta O=\delta\Omega\,O$ with $\delta\Omega$ antisymmetric, and that is where the Vandermonde volume factor of the spectral decomposition comes from ([[§R2.6 Haar Measure and the Jacobian of the Spectral Decomposition#^thm-r2-6-4|Thesis Thm. §R2.6.4]]).

> [!remark] Remark: Two Readings of the Dimension
> A student asked for a combinatorial reason that $\dim \mathrm{O}(n) = \tfrac{n(n-1)}{2}$, “like choosing two out of $n$.” There are now two: the level-set count $n^2 - \tfrac{n(n+1)}{2}$ from the regular value theorem, and the kernel count $\binom{n}{2}$ from Proposition [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-1|§23.1]]. They agree by [[§21 Linear Algebra Toolkit#^prop-21-1|rank–nullity]]: $dF_g$ is surjective onto a space of dimension $\tfrac{n(n+1)}{2}$, so its kernel has dimension $n^2 - \tfrac{n(n+1)}{2}$. The kernel is not yet officially anything, but Uribe named it ahead of time: it is the *geometric tangent space* $T^{\mathrm{geo}}_g\mathrm{O}(n)$ to $\mathrm{O}(n)$ at $g$ (see [[§25 The Geometric Tangent Space|§25]]), and at $g = I$ the skew-symmetric matrices will be the *Lie algebra* $\mathfrak{so}(n)$, “in some number of weeks.” The same move produced $\nabla\det$ in Proposition [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|§12.1]], and it will recur whenever a classical group is presented as a level set.

^rem-23-3

> [!theorem] Corollary §23.2: Consequences
> $\mathrm{SO}(n)$ is a smooth manifold of dimension $\tfrac{n(n-1)}{2}$, and $\mathrm{O}(n)$ is compact.
>
> *Lee: Example 7.27*

^cor-23-2

> [!proof]+ Proof
> *$\mathrm{SO}(n)$ is open (and closed) in $\mathrm{O}(n)$.* By Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-8|§11.8]], $\mathrm{SO}(n) = \{g \in \mathrm{O}(n) \mid \det g = 1\}$. By Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-5|§11.5]], $\det g = \pm 1$ for every $g \in \mathrm{O}(n)$, so for $g \in \mathrm{O}(n)$ the conditions $\det g = 1$ and $\det g > 0$ are the same, and $\mathrm{SO}(n) = \mathrm{O}(n) \cap \det^{-1}(0,\infty)$ is an open subset of $\mathrm{O}(n)$: $\det$ is a polynomial in the entries, hence continuous on $\operatorname{Mat}(n,\mathbb{R})$, so $\det^{-1}(0,\infty)$ is open in $\operatorname{Mat}(n,\mathbb{R})$, and its intersection with $\mathrm{O}(n)$ is open in the subspace topology. ($\det$ is continuous and takes only the values $\pm1$ on $\mathrm{O}(n)$, so $\mathrm{SO}(n)$ is also closed: its complement in $\mathrm{O}(n)$ is $\mathrm{O}(n) \cap \det^{-1}(-\infty, 0)$, open by the same argument.)
>
> *$\mathrm{SO}(n)$ is a smooth manifold of dimension $\tfrac{n(n-1)}{2}$.* An open subset of a smooth $m$-manifold is a smooth $m$-manifold, its charts being restrictions of the given ones. In detail, with $M = \mathrm{O}(n)$, $m = \tfrac{n(n-1)}{2}$ (Example [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|§23.1]]) and $S = \mathrm{SO}(n)$: $S$ is a topological $m$-manifold by Proposition [[§3 Subspaces and Products#^prop-3-6|§3.6]]. For each smooth chart $(U, \varphi)$ of $M$, the set $U \cap S$ is open in $M$, so $(U \cap S, \varphi|_{U \cap S})$ is a chart by Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]](1), and these domains cover $S$ because the $U$ cover $M$. For two such restricted charts the transition function is
>
> $$
> \varphi'|_{U' \cap S} \circ \big(\varphi|_{U \cap S}\big)^{-1} = \big(\varphi' \circ \varphi^{-1}\big)\big|_{\varphi(U \cap U' \cap S)} ,
> $$
>
> the restriction of the transition function $\varphi' \circ \varphi^{-1}$ of the original charts to the open subset $\varphi(U \cap U' \cap S)$ of $\varphi(U \cap U')$ (open because $\varphi$ is a homeomorphism onto an open subset of $\mathbb{R}^m$). The restriction of a smooth map to an open subset is smooth, and the same applies to the inverse $\varphi \circ \varphi'^{-1}$; so the restricted charts are pairwise $C^\infty$-compatible (Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]), form an atlas on $S$ (Definition [[§17 Differentiable Structures#^def-17-6|§17.6]]), and determine a smooth structure (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]). Its charts take values in $\mathbb{R}^m$, so $\dim \mathrm{SO}(n) = m = \tfrac{n(n-1)}{2}$.
>
> *$\mathrm{O}(n)$ is compact.* Compactness of $\mathrm{O}(n)$ was shown in Corollary [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|§15.8]]: it is closed as $F^{-1}(I)$ with $F$ continuous, and bounded because every column of an orthogonal matrix is a unit vector. In detail: $F$ is smooth (Example [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|§23.1]]), hence continuous, and the point $\{I\}$ is closed in $\operatorname{Sym}(n,\mathbb{R})$, so $\mathrm{O}(n) = F^{-1}(I)$ is closed in $\operatorname{Mat}(n,\mathbb{R}) \cong \mathbb{R}^{n^2}$. By Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-5|§11.5]](ii), $g^{\mathsf T} g = I$; its $(j,j)$ entry is
>
> $$
> 1 = (g^{\mathsf T} g)_{jj} = \sum_{i=1}^n (g^{\mathsf T})_{ji}\, g_{ij} = \sum_{i=1}^n g_{ij}^2 ,
> $$
>
> which says that the $j$-th column is a unit vector. Hence $|g_{ij}| \le 1$ for all $i, j$, and $\|g\|^2 = \sum_{i,j} g_{ij}^2 = n$ in the norm of Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-2|§11.2]], so $\mathrm{O}(n)$ lies in the closed ball of radius $\sqrt n$. Closed and bounded in $\mathbb{R}^{n^2}$, it is compact by Heine–Borel (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](1)).

^pf-23-2

*Uses:* [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|Ex. §23.1]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-8|Def. §11.8]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-3|§11.3]], [[§3 Subspaces and Products#^prop-3-6|§3.6]], [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|§15.8]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Heine–Borel Theorem|590 §18.12]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-5|§11.5]], [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^def-17-6|Def. §17.6]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-2|Def. §11.2]]

> [!remark]- Connections
> - Compactness is [[Heine–Borel Theorem|590 §18.12 (Heine–Borel)]].
> - Compactness lets finitely many parametrizations cover $\mathrm{O}(n)$, so their local volume elements patch into a finite measure invariant under left and right multiplication, a multiple of the Haar probability measure ([[§R2.6 Haar Measure and the Jacobian of the Spectral Decomposition#^thm-r2-6-9|Thesis Thm. §R2.6.9]]).

**Transcription note.** Page 20 of the handwritten notes writes “$\ker dF_g(A) = \{A \mid gA^{\mathsf T} + Ag^{\mathsf T} = 0\}$”; the kernel is of the linear map $dF_g$, and the “$(A)$” does not belong. The transposes sit to the right of $g$ throughout because that is how $F$ was written ($gg^{\mathsf T}$, not $g^{\mathsf T}g$); either convention defines $\mathrm{O}(n)$.

The unitary group $\mathrm{U}(n)$ is treated the same way, with $F(g) = gg^*$ mapping into the Hermitian matrices, in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#The Unitary Group as a Smooth Manifold|The Unitary Group as a Smooth Manifold]]. The analogue for $\mathrm{SL}(n,\mathbb{R})$ was Corollary [[§12 The Classical Groups Are Topological Manifolds#^cor-12-5|§12.5]], which Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]] now upgrades from a topological to a smooth manifold.

> [!remark] Remark: Where This Leaves Us
> Every level set met so far is now a smooth manifold: $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$, the spheres, and any surface cut out by a regular value. What remains owed is the global half of the internal picture: a manifold defined abstractly, not sitting inside any $\mathbb{R}^N$, has no external description until one knows it can be embedded in a Euclidean space at all. That is Whitney's embedding theorem, later in the course.

^rem-23-4

## The Unitary Group as a Smooth Manifold

*Assignment 2, Problem 4. The argument is that of [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds|The Orthogonal Group as a Smooth Manifold]] with one change that is easy to get wrong: the spaces involved are complex, but the map is not complex-linear, so everything must be done over $\mathbb{R}$.*

Write $A^{\ast} = \bar A^{\mathsf T}$ for the conjugate transpose, so that $\mathrm{U}(n) = \{g \in \operatorname{Mat}(n,\mathbb{C}) \mid g^{\ast} g = I\}$. Throughout, $\operatorname{Mat}(n,\mathbb{C})$ is regarded as a *real* vector space of dimension $2n^2$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-9|Def. §11.9]]).

> [!definition] Definition §23.2: Hermitian Matrices as a Real Vector Space
> Let $\operatorname{Herm}(n) = \{A \in \operatorname{Mat}(n,\mathbb{C}) \mid A^{\ast} = A\}$. It is closed under addition and under multiplication by *real* scalars, so it is a real vector space; it is *not* a complex subspace, since $(iA)^{\ast} = -iA$. A Hermitian matrix has real diagonal entries ($a_{jj} = \overline{a_{jj}}$), arbitrary complex entries above the diagonal, and entries below the diagonal determined by $a_{kj} = \overline{a_{jk}}$. Hence
>
> $$
> \dim_{\mathbb{R}} \operatorname{Herm}(n) = n + 2\binom{n}{2} = n^2 ,
> $$
>
> and reading off the real diagonal entries and the real and imaginary parts of the entries above the diagonal gives a linear isomorphism $\operatorname{Herm}(n) \cong \mathbb{R}^{n^2}$.

^def-23-2

> [!remark]- Connections
> - Hermitian matrices are the matrices of self-adjoint operators: [[§23 Self-Adjoint and Normal Operators#^ladr-7-10|LADR 7.10]], with the conjugate transpose of [[§23 Self-Adjoint and Normal Operators#^ladr-7-7|LADR 7.7]].

> [!theorem] Lemma §23.3: A One-Sided Inverse Suffices
> If $g \in \operatorname{Mat}(n,\mathbb{C})$ satisfies $gg^* = I$, then also $g^*g = I$. Consequently $\mathrm{U}(n) = \{g \mid gg^* = I\}$.

^lem-23-3

> [!proof]+ Proof
> Let $gg^{\ast} = I$.
>
> *$g$ is invertible.* Taking determinants and using that $\det$ is multiplicative, $\det(g)\det(g^{\ast}) = \det(gg^{\ast}) = \det(I) = 1$, so $\det g \neq 0$ and $g$ is invertible.
>
> *$g^{\ast}g = I$.* Multiplying $gg^{\ast} = I$ on the left by $g^{-1}$ gives $g^{\ast} = g^{-1}$:
>
> $$
> g^{\ast} = g^{-1}(gg^{\ast}) = g^{-1} I = g^{-1}, \qquad\text{hence}\qquad g^{\ast}g = g^{-1}g = I .
> $$
>
> *The description of $\mathrm{U}(n)$.* By Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-10|§11.10]], $\mathrm{U}(n) = \{g \in \mathrm{GL}(n,\mathbb{C}) \mid g^{-1} = g^{\ast}\}$. If $g \in \mathrm{U}(n)$, then $gg^{\ast} = gg^{-1} = I$. Conversely, if $gg^{\ast} = I$, the two steps above show that $g$ is invertible with $g^{-1} = g^{\ast}$, so $g \in \mathrm{U}(n)$. Hence $\mathrm{U}(n) = \{g \mid gg^{\ast} = I\}$.

^pf-23-3

*Uses:* [[§37 Determinants#^ladr-9-49|LADR 9.49]], [[Invertible ⟺ nonzero determinant|LADR 9.50]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-10|Def. §11.10]]

> [!remark]- Connections
> - The general linear-algebra fact: [[§10 Invertibility and Isomorphisms#^ladr-3-68|LADR 3.68 (ST = I ⟺ TS = I)]]; unitary matrices in LADR: [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR 7.57]].

> [!example] Example §23.2: $\mathrm{U}(n)$ Is a Smooth Manifold of Dimension $n^2$
> Define
>
> $$
> F : \operatorname{Mat}(n,\mathbb{C}) \longrightarrow \operatorname{Herm}(n), \qquad F(g) = g g^*,
> $$
>
> both regarded as real vector spaces. Then $\mathrm{U}(n) = F^{-1}(I)$, the identity is a regular value, and $\mathrm{U}(n)$ is a smooth manifold of dimension $2n^2 - n^2 = n^2$.
>
> *Lee: Example 7.29*

^ex-23-2

![[m591-10-6.svg]]
*The map $F(g) = gg^{\ast}$ and its coordinate representation $\widehat F$ under the real-linear identifications $\operatorname{Mat}(n,\mathbb{C}) \cong \mathbb{R}^{2n^2}$ and $\operatorname{Herm}(n) \cong \mathbb{R}^{n^2}$.*

The vertical arrows are the real-linear identifications of [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|Def. §11.9]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^def-23-2|Def. §23.2]]. This is the square of [[§22 The Differential of a Map Between Vector Spaces|The Differential of a Map Between Vector Spaces]] with $X = \operatorname{Mat}(n,\mathbb{C})$ and $Y = \operatorname{Herm}(n)$ regarded as real vector spaces: $F$ is smooth, and $I$ is a regular value, exactly when the same holds for $\widehat F$ (Lemma [[§22 The Differential of a Map Between Vector Spaces#^lem-22-1|§22.1]], Corollary [[§22 The Differential of a Map Between Vector Spaces#^cor-22-4|§22.4]]). Nothing is computed in the bottom row; it only certifies that the top row may be used.

> [!proof]+ Proof
> As for $\mathrm{O}(n)$ in Example [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|§23.1]], four things have to be shown: $F$ is a smooth map into $\operatorname{Herm}(n)$; $F^{-1}(I) = \mathrm{U}(n)$; $dF_g$ is surjective at every $g \in F^{-1}(I)$; and this makes $\mathrm{U}(n)$ a smooth manifold of dimension $n^2$. All vector spaces are real, and “linear” means real-linear.
>
> *$F$ is well defined and smooth.* Using $(PQ)^{\ast} = Q^{\ast}P^{\ast}$ (conjugation is multiplicative and transposition reverses products) and $g^{\ast \ast } = g$ (conjugating and transposing twice),
>
> $$
> (gg^{\ast})^{\ast} = g^{\ast \ast }g^{\ast} = gg^{\ast},
> $$
>
> so $F$ lands in $\operatorname{Herm}(n)$. For smoothness, take the linear coordinates $L$ on $\operatorname{Mat}(n,\mathbb{C})$ of Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|§11.9]] and $K$ on $\operatorname{Herm}(n)$ of Definition [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^def-23-2|§23.2]]. The components of $K \circ F \circ L^{-1}$ are real and imaginary parts of entries of $gg^{\ast}$, and each entry is
>
> $$
> (gg^{\ast})_{jk} = \sum_{m=1}^n g_{jm}\,(g^{\ast})_{mk} = \sum_{m=1}^n g_{jm}\overline{g_{km}} .
> $$
>
> Writing $g_{jm} = a_{jm} + i\,b_{jm}$ with $a_{jm}, b_{jm}$ the real coordinates of $g$, each summand is $g_{jm}\overline{g_{km}} = (a_{jm}a_{km} + b_{jm}b_{km}) + i\,(b_{jm}a_{km} - a_{jm}b_{km})$. So each entry $(gg^{\ast})_{jk} = \sum_m g_{jm}\overline{g_{km}}$ has real and imaginary parts that are quadratic polynomials in the real coordinates of $g$, so $F$ is smooth (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-3|§22.3]]).
>
> *$\mathrm{U}(n) = F^{-1}(I)$.* Lemma [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^lem-23-3|§23.3]]: $g \in \mathrm{U}(n) \iff gg^{\ast} = I \iff F(g) = I$.
>
> *The differential.* By Theorem [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]], applied with $X = \operatorname{Mat}(n,\mathbb{C})$ and $Y = \operatorname{Herm}(n)$ as real vector spaces, for $g \in F^{-1}(I)$ and $h \in \operatorname{Mat}(n,\mathbb{C})$, $dF_g(h) = \frac{d}{dt}\big|_{t=0} F(g+th)$ with $t$ *real* — the line $g + th$ is formed with the real scalars of $X$. Since $(th)^{\ast} = \bar t\, h^{\ast} = t h^{\ast}$ for real $t$, and $^{\ast}$ is additive, $(g + th)^{\ast} = g^{\ast} + th^{\ast}$. Multiplying out,
>
> $$
> F(g+th) = (g+th)(g^{\ast} + th^{\ast}) = gg^{\ast} + t\big(hg^{\ast} + gh^{\ast}\big) + t^2\, hh^{\ast},
> \qquad\text{so}\qquad
> dF_g(h) = hg^{\ast} + gh^{\ast} ,
> $$
>
> the derivative at $t = 0$ of this polynomial in $t$ being its coefficient of $t$ (the constant term contributes $0$, and $\frac{d}{dt}(t^2 hh^{\ast}) = 2t\,hh^{\ast}$ vanishes at $t = 0$). It is Hermitian, as it must be: $(hg^{\ast} + gh^{\ast})^{\ast} = g^{\ast \ast }h^{\ast} + h^{\ast \ast }g^{\ast} = gh^{\ast} + hg^{\ast}$.
>
> *$dF_g$ is surjective.* Fix $g \in F^{-1}(I) = \mathrm{U}(n)$; we must show every $A \in \operatorname{Herm}(n)$ is $dF_g(h)$ for some $h$. Put $X = hg^{\ast}$; then $gh^{\ast} = (hg^{\ast})^{\ast} = X^{\ast}$, since $(hg^{\ast})^{\ast} = g^{\ast \ast }h^{\ast} = gh^{\ast}$, so $dF_g(h) = X + X^{\ast}$. As $g$ is invertible, $h \mapsto hg^{\ast}$ is a real-linear bijection of $\operatorname{Mat}(n,\mathbb{C})$, with inverse $X \mapsto Xg$: indeed $(hg^{\ast})g = h(g^{\ast}g) = h$ and $(Xg)g^{\ast} = X(gg^{\ast}) = X$, using $g^{\ast}g = gg^{\ast} = I$ (Lemma [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^lem-23-3|§23.3]]). So as $h$ runs over $\operatorname{Mat}(n,\mathbb{C})$, $X$ runs over all of $\operatorname{Mat}(n,\mathbb{C})$. Hence $\operatorname{im} dF_g = \{X + X^{\ast} \mid X \in \operatorname{Mat}(n,\mathbb{C})\} = \operatorname{Herm}(n)$: the inclusion $\subseteq$ because $(X + X^{\ast})^{\ast} = X^{\ast} + X$, and $\supseteq$ since any Hermitian $A$ arises from $X = \tfrac12 A$, as $\tfrac12 A + (\tfrac12 A)^{\ast} = \tfrac12 A + \tfrac12 A^{\ast} = \tfrac12 A + \tfrac12 A = A$ (the scalar $\tfrac12$ is real, so it passes through $^{\ast}$ unchanged). Explicitly $h = \tfrac12 Ag$, by $X \mapsto Xg$:
>
> $$
> hg^{\ast} = \tfrac12 A gg^{\ast} = \tfrac12 A, \qquad gh^{\ast} = g\big(\tfrac12 Ag\big)^{\ast} = \tfrac12\, g g^{\ast} A^{\ast} = \tfrac12 A ,
> $$
>
> using $(Ag)^{\ast} = g^{\ast}A^{\ast}$, $gg^{\ast} = I$ and $A^{\ast} = A$; adding gives $dF_g(h) = A$.
>
> ![[m591-10-7.svg]]
>
> The surjectivity argument as a diagram: $dF_g$ factors as a bijection followed by $X \mapsto X + X^{\ast}$, and the second map is onto $\operatorname{Herm}(n)$, hitting $A$ at $X = \tfrac12 A$. Hence $dF_g$ is onto.
>
> *Conclusion.* $\dim_{\mathbb{R}}\operatorname{Mat}(n,\mathbb{C}) = 2n^2 \ge n^2 = \dim_{\mathbb{R}}\operatorname{Herm}(n)$ (Definitions [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|§11.9]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^def-23-2|§23.2]]), so by Corollary [[§22 The Differential of a Map Between Vector Spaces#^cor-22-4|§22.4]] surjectivity of $dF_g$ at every $g \in F^{-1}(I)$ is exactly the statement that $I$ is a regular value. In the coordinates of the square above, this says: $\widehat F = K \circ F \circ L^{-1} : \mathbb{R}^{2n^2} \to \mathbb{R}^{n^2}$ is smooth, its Jacobian at $L(g)$ has maximal rank $n^2$ for every $g \in F^{-1}(I)$, and, $K$ being injective, $\widehat F(L(g)) = K(F(g)) = K(I) \iff F(g) = I$, so $\widehat F^{-1}(K(I)) = L(\mathrm{U}(n))$; thus $K(I)$ is a regular value of $\widehat F$ (Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]]). Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], with $W = \mathbb{R}^{2n^2}$, $n + k = 2n^2$ and $k = n^2$, makes $L(\mathrm{U}(n))$ a smooth manifold of dimension $2n^2 - n^2 = n^2$. The topology of $\mathrm{U}(n)$ is the subspace topology of $\operatorname{Mat}(n,\mathbb{C})$, defined by $L$ (Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|§11.9]]), so $L$ restricts to a homeomorphism $\mathrm{U}(n) \to L(\mathrm{U}(n))$, and transporting along it (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]]) makes $\mathrm{U}(n)$ a smooth manifold of dimension $2n^2 - n^2 = n^2$.

^pf-ex-23-2

*Uses:* [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^def-23-2|Def. §23.2]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|Def. §11.9]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-10|Def. §11.10]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-3|Def. §22.3]], [[§22 The Differential of a Map Between Vector Spaces#^lem-22-1|§22.1]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^lem-23-3|§23.3]], [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]], [[§22 The Differential of a Map Between Vector Spaces#^cor-22-4|§22.4]], [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|Ex. §23.1]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]]

> [!remark]- Connections
> - Unitary matrices in LADR: [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-56|LADR 7.56]]; $\mathrm{U}(1)$ is the circle, [[§11 Topological Groups and Classical Matrix Groups#^ex-11-3|Ex. §11.3]].
> - Its tangent spaces: [[§25 The Geometric Tangent Space#^ex-25-3|Ex. §25.3]].

> [!remark] Remark
> **Why over $\mathbb{R}$.** The derivative $h \mapsto hg^{\ast} + gh^{\ast}$ is real-linear but not complex-linear: $dF_g(ih) = i\,hg^{\ast} - i\,gh^{\ast}$, which differs from $i\,dF_g(h)$ unless $gh^{\ast} = 0$. This is the conjugation in $g^{\ast}$ at work, and it is why Problem 4 insists that both spaces be regarded as real vector spaces. It is also why the holomorphic regular value theorem of [[§7 The Regular Value Theorem#Holomorphic Level Sets|§7, Holomorphic Level Sets]] does not apply, and why $\dim \mathrm{U}(n) = n^2$ can be odd, which no holomorphic level set can.

^rem-23-5

> [!theorem] Proposition §23.4: The Kernel of the Differential
> For $g \in \mathrm{U}(n)$,
>
> $$
> \ker dF_g = \mathfrak{u}(n)\cdot g = g \cdot \mathfrak{u}(n), \qquad \mathfrak{u}(n) = \{X \in \operatorname{Mat}(n,\mathbb{C}) \mid X^* = -X\},
> $$
>
> the skew-Hermitian matrices, and $\dim_{\mathbb{R}} \mathfrak{u}(n) = n^2$.

^prop-23-4

> [!proof]+ Proof
> *$\ker dF_g = \mathfrak{u}(n)\cdot g$.* By the proof of Example [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|§23.2]], $dF_g(h) = hg^{\ast} + gh^{\ast}$, and $h \mapsto hg^{\ast}$ is a bijection of $\operatorname{Mat}(n,\mathbb{C})$ with inverse $X \mapsto Xg$. So every $h$ can be written uniquely as $h = Xg$ with $X = hg^{\ast}$ (uniquely, because $Xg = h$ forces $X = hg^{-1} = hg^{\ast}$). Then, using $(Xg)^{\ast} = g^{\ast}X^{\ast}$ and $gg^{\ast} = I$,
>
> $$
> dF_g(Xg) = (Xg)g^{\ast} + g(Xg)^{\ast} = X\,gg^{\ast} + gg^{\ast}\,X^{\ast} = X + X^{\ast},
> $$
>
> which vanishes iff $X^{\ast} = -X$, i.e. iff $X \in \mathfrak{u}(n)$. So $\ker dF_g = \{Xg \mid X \in \mathfrak{u}(n)\} = \mathfrak{u}(n)\cdot g$.
>
> *$g\cdot\mathfrak{u}(n) = \mathfrak{u}(n)\cdot g$.* Conjugation by $g$ preserves $\mathfrak{u}(n)$: if $X^{\ast} = -X$ then $(gXg^{\ast})^{\ast} = g^{\ast \ast }X^{\ast}g^{\ast} = gX^{\ast}g^{\ast} = -gXg^{\ast}$; so $g \cdot \mathfrak{u}(n) = (g\,\mathfrak{u}(n)\,g^{-1})\cdot g = \mathfrak{u}(n)\cdot g$. In detail, both inclusions, using $g^{-1} = g^{\ast}$ and $g^{\ast}g = gg^{\ast} = I$ (Lemma [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^lem-23-3|§23.3]]): for $Y \in \mathfrak{u}(n)$,
>
> $$
> gY = (gYg^{\ast})\,g, \qquad gYg^{\ast} \in \mathfrak{u}(n),
> $$
>
> so $g\cdot\mathfrak{u}(n) \subseteq \mathfrak{u}(n)\cdot g$; and for $X \in \mathfrak{u}(n)$, $Xg = g\,(g^{\ast}Xg)$, where $g^{\ast}Xg \in \mathfrak{u}(n)$ by the same computation with $g^{\ast}$ in place of $g$: $(g^{\ast}Xg)^{\ast} = g^{\ast}X^{\ast}g^{\ast \ast } = g^{\ast}X^{\ast}g = -g^{\ast}Xg$. So $\mathfrak{u}(n)\cdot g \subseteq g\cdot\mathfrak{u}(n)$.
>
> *Dimension.* A skew-Hermitian matrix has purely imaginary diagonal ($n$ real parameters) and arbitrary complex entries above the diagonal ($2\binom n2$ real parameters), so $\dim_{\mathbb{R}}\mathfrak{u}(n) = n^2$ — agreeing with $\dim \mathrm{U}(n)$ by rank–nullity, $2n^2 - n^2$. In detail: $X^{\ast} = -X$ says $\overline{x_{kj}} = -x_{jk}$ for all $j, k$. For $j = k$ this is $\overline{x_{jj}} = -x_{jj}$, i.e. $\operatorname{Re} x_{jj} = 0$, so each diagonal entry is $i$ times a free real number; for $j < k$ the entry $x_{jk}$ is an arbitrary complex number (two real parameters), and the entry below the diagonal is then determined, $x_{kj} = -\overline{x_{jk}}$. Hence
>
> $$
> \dim_{\mathbb{R}}\mathfrak{u}(n) = n + 2\binom n2 = n + n(n-1) = n^2 .
> $$
>
> The real-linear isomorphism $X \mapsto Xg$ maps $\mathfrak{u}(n)$ onto $\ker dF_g$, so $\dim_{\mathbb{R}} \ker dF_g = n^2$ as well. Rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)) gives the same number from the other side: $dF_g$ is surjective onto $\operatorname{Herm}(n)$, of real dimension $n^2$, so $\dim_{\mathbb{R}} \ker dF_g = 2n^2 - n^2 = n^2$.

^pf-23-4

*Uses:* [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|Ex. §23.2]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^lem-23-3|§23.3]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]]

> [!remark]- Connections
> - The geometric tangent space of $\mathrm{U}(n)$: [[§25 The Geometric Tangent Space#^ex-25-3|Ex. §25.3]]; the orthogonal analogue: [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-1|§23.1]].

> [!theorem] Corollary §23.5: $\mathrm{U}(n)$ Is Compact
> $\mathrm{U}(n)$ is a compact smooth manifold of dimension $n^2$.
>
> *Lee: Example 7.29*

^cor-23-5

> [!proof]+ Proof
> By Example [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|§23.2]], $\mathrm{U}(n)$ is a smooth manifold of dimension $n^2$; it remains to show it is compact. By Heine–Borel (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](1)) it suffices that $\mathrm{U}(n)$ be closed and bounded in $\operatorname{Mat}(n,\mathbb{C}) \cong \mathbb{R}^{2n^2}$ (Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|§11.9]]).
>
> *Closed.* It is closed in $\operatorname{Mat}(n,\mathbb{C}) \cong \mathbb{R}^{2n^2}$ as $F^{-1}(I)$ with $F$ continuous: $F$ is smooth (Example [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|§23.2]]), hence continuous, and the point $\{I\}$ is closed in $\operatorname{Herm}(n)$.
>
> *Bounded.* It is bounded because the columns of a unitary matrix are unit vectors of $\mathbb{C}^n$, so every entry has modulus at most $1$. Indeed, $g^{\ast}g = I$ (Lemma [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^lem-23-3|§23.3]]), and its $(j,j)$ entry is
>
> $$
> 1 = (g^{\ast}g)_{jj} = \sum_{i=1}^n \overline{g_{ij}}\, g_{ij} = \sum_{i=1}^n |g_{ij}|^2 ,
> $$
>
> so the $j$-th column is a unit vector and $|g_{ij}| \le 1$ for all $i, j$. In the real coordinates of Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|§11.9]] the squared Euclidean norm of $g$ is $\sum_{i,j}\big((\operatorname{Re} g_{ij})^2 + (\operatorname{Im} g_{ij})^2\big) = \sum_{i,j} |g_{ij}|^2 = n$, so $\mathrm{U}(n)$ lies in the closed ball of radius $\sqrt n$ in $\mathbb{R}^{2n^2}$.
>
> Apply Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](1).

^pf-23-5

*Uses:* [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|Ex. §23.2]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|Def. §11.9]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-10|Def. §11.10]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Heine–Borel Theorem|590 §18.12]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^lem-23-3|§23.3]]

> [!remark]- Connections
> - [[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8]](1) is [[Heine–Borel Theorem|590 §18.12 (Heine–Borel)]]; columns of unitary matrices are orthonormal by [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR 7.57]].
