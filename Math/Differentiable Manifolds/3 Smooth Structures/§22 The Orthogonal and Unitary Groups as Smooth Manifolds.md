---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 3
section: 22
tags: [differentiable-manifolds, math591]
---
← [[§21 The Differential of a Map Between Vector Spaces]] · ↑ [[· 3 Smooth Structures]] · [[§23 Tangent Spaces I꞉ The Geometric Picture]] →

*Stage: linear — The matrix groups become smooth level sets: $\mathrm{O}(n)$ and $\mathrm{U}(n)$ by the regular value theorem, with the differential computed along straight lines.*

The classical groups through the course: defined in [[§10 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§15 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§11 The Classical Groups Are Topological Manifolds#^thm-11-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§12 Group Actions and Orbit Spaces#^ex-12-4|the rotations of the plane]] and [[§12 Group Actions and Orbit Spaces#^ex-12-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§13 Homogeneous Spaces#^ex-13-2|the isotropy of the north pole]] and [[§13 Homogeneous Spaces#^ex-13-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-1|the orthogonal group]] and [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-2|the unitary group]]; their tangent spaces at the identity in [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5|The Classical Groups]], with [[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-4|the infinitesimal rotations]]; and the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§39 SU(2) → SO(3)꞉ The Double Cover#^thm-39-10|The Double Cover]].

The promise of [[§11 The Classical Groups Are Topological Manifolds|§11, The Classical Groups Are Topological Manifolds]] can now be kept, with [[§21 The Differential of a Map Between Vector Spaces|The Differential of a Map Between Vector Spaces]] supplying the meaning of every step.

> [!definition] Definition §22.1: Symmetric Matrices as a Euclidean Space
> Let $\operatorname{Sym}(n,\mathbb{R}) = \{\, S \in \operatorname{Mat}(n,\mathbb{R}) \mid S^{\mathsf T} = S \,\}$. It is a linear subspace of $\operatorname{Mat}(n,\mathbb{R})$, and the entries on and above the diagonal are free while those below are determined, so
>
> $$
> \dim \operatorname{Sym}(n,\mathbb{R}) = n + (n-1) + \cdots + 1 = \frac{n(n+1)}{2}.
> $$
>
> Reading off those entries in a fixed order gives a linear isomorphism $\operatorname{Sym}(n,\mathbb{R}) \cong \mathbb{R}^{n(n+1)/2}$, which we use to regard maps into $\operatorname{Sym}(n,\mathbb{R})$ as maps into a Euclidean space. Being linear, it changes neither smoothness nor rank.

^def-22-1

> [!remark]- Connections
> - Symmetric matrices in LADR: [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-11|LADR 9.11]], the matrices of symmetric bilinear forms ([[§32 Bilinear Forms and Quadratic Forms#^ladr-9-9|LADR 9.9]]).

> [!example] Example §22.1: $\mathrm{O}(n)$ Is a Smooth Manifold of Dimension $\tfrac{n(n-1)}{2}$
> Define
>
> $$
> F : \operatorname{Mat}(n,\mathbb{R}) \longrightarrow \operatorname{Sym}(n,\mathbb{R}), \qquad F(g) = g\, g^{\mathsf T}.
> $$
>
> Then $\mathrm{O}(n) = F^{-1}(I)$, the identity $I$ is a regular value of $F$, and consequently $\mathrm{O}(n)$ is a smooth manifold of dimension $n^2 - \tfrac{n(n+1)}{2} = \tfrac{n(n-1)}{2}$.
>
> *Lee: Example 7.27*

^ex-22-1

> [!proof]+ Proof
> *$F$ is well defined and smooth.* $(gg^{\mathsf T})^{\mathsf T} = g^{\mathsf T\mathsf T} g^{\mathsf T} = g g^{\mathsf T}$, so $F$ does land in $\operatorname{Sym}(n,\mathbb{R})$. Each entry $(gg^{\mathsf T})_{ij} = \sum_m g_{im}g_{jm}$ is a quadratic polynomial in the coordinates of [[§10 Topological Groups and Classical Matrix Groups#^def-10-2|Def. §10.2]], so $F$ is smooth.
>
> *$\mathrm{O}(n) = F^{-1}(I)$.* By Proposition [[§10 Topological Groups and Classical Matrix Groups#^prop-10-5|§10.5]], $g \in \mathrm{O}(n) \iff g^{-1} = g^{\mathsf T} \iff gg^{\mathsf T} = I$.
>
> *The differential as a linear map.* *(Lecture 6: “We're not going to compute [the] Jacobian of this thing… You use curves” — a technique he could “not emphasize enough”.)* $\operatorname{Mat}(n,\mathbb{R})$ and $\operatorname{Sym}(n,\mathbb{R})$ are finite-dimensional vector spaces and $F$ is smooth between them, so by Theorem [[§21 The Differential of a Map Between Vector Spaces#^thm-21-3|§21.3]] the differential is computed along lines: for $g \in F^{-1}(I)$ and any $A \in \operatorname{Mat}(n,\mathbb{R})$, $dF_g(A) = \frac{d}{dt}\big|_{t=0} F(g+tA)$. Expanding,
>
> $$
> F(g+tA) = (g+tA)(g^{\mathsf T} + tA^{\mathsf T}) = g g^{\mathsf T} + t\big(A g^{\mathsf T} + g A^{\mathsf T}\big) + t^2 A A^{\mathsf T},
> $$
>
> so
>
> $$
> dF_g(A) = A g^{\mathsf T} + g A^{\mathsf T}.
> $$
>
> This is visibly symmetric, as it must be: $(Ag^{\mathsf T} + gA^{\mathsf T})^{\mathsf T} = gA^{\mathsf T} + Ag^{\mathsf T}$.
>
> *$dF_g$ is surjective.* *(Lecture 6 observed that the left side is twice the symmetric part of a matrix, which is the substitution below; Lecture 7 finished with the explicit choice $A = \tfrac12 Sg$ — the equation “looks like a hard equation to solve until you realize that you have to use the fact that $S$ is symmetric and that $g$ is orthogonal.”)* Put $X = Ag^{\mathsf T}$, so that $dF_g(A) = X + X^{\mathsf T}$. Since $g$ is invertible, $A \mapsto Ag^{\mathsf T}$ is a linear *bijection* of $\operatorname{Mat}(n,\mathbb{R})$, and therefore
>
> $$
> \operatorname{im} F'(g) = \{\, X + X^{\mathsf T} \mid X \in \operatorname{Mat}(n,\mathbb{R}) \,\} = \operatorname{Sym}(n,\mathbb{R}),
> $$
>
> the last equality because $X + X^{\mathsf T}$ is always symmetric, and conversely any symmetric $S$ arises from $X = \tfrac12 S$. Unwinding the substitution gives the matrix explicitly: $A = X (g^{\mathsf T})^{-1} = \tfrac12 S g$, using $(g^{\mathsf T})^{-1} = g$ for orthogonal $g$. Directly, with $A = \tfrac12 Sg$:
>
> $$
> A g^{\mathsf T} = \tfrac12 S g g^{\mathsf T} = \tfrac12 S, \qquad
> g A^{\mathsf T} = g \big(\tfrac12 S g\big)^{\mathsf T} = \tfrac12 g\, g^{\mathsf T} S^{\mathsf T} = \tfrac12 S,
> $$
>
> using $gg^{\mathsf T} = I$ and $S^{\mathsf T} = S$; adding gives $dF_g(A) = S$.
>
> ![[m591-10-5.svg]]
>
> The same argument as a diagram: a bijection followed by symmetrization, which is onto. The unitary case in [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#The Unitary Group as a Smooth Manifold|The Unitary Group as a Smooth Manifold]] has exactly this shape, with ${}^{\mathsf T}$ replaced by ${}^*$.
>
> *Conclusion.* $dF_g$ is surjective onto $\operatorname{Sym}(n,\mathbb{R})$ for every $g \in F^{-1}(I)$. By Corollary [[§21 The Differential of a Map Between Vector Spaces#^cor-21-4|§21.4]] (here $\dim \operatorname{Mat} = n^2 \ge \tfrac{n(n+1)}{2} = \dim \operatorname{Sym}$), this says that in any linear coordinates the Jacobian has maximal rank $k = \tfrac{n(n+1)}{2}$ at every point of $F^{-1}(I)$, i.e. $I$ is a regular value ([[§7 The Regular Value Theorem#^def-7-2|Def. §7.2]]). Proposition [[§19 Manifolds in Euclidean Space#^prop-19-2|§19.2]] applies with $n + k = n^2$: $\mathrm{O}(n)$ is a smooth manifold of dimension $n^2 - \tfrac{n(n+1)}{2} = \tfrac{n(n-1)}{2}$.

^pf-ex-22-1

*Uses:* [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^def-22-1|Def. §22.1]], [[§10 Topological Groups and Classical Matrix Groups#^def-10-2|Def. §10.2]], [[§10 Topological Groups and Classical Matrix Groups#^def-10-6|Def. §10.6]], [[§10 Topological Groups and Classical Matrix Groups#^prop-10-5|§10.5]], [[§21 The Differential of a Map Between Vector Spaces#^def-21-3|Def. §21.3]], [[§21 The Differential of a Map Between Vector Spaces#^thm-21-3|§21.3]], [[§21 The Differential of a Map Between Vector Spaces#^cor-21-4|§21.4]], [[§7 The Regular Value Theorem#^def-7-2|Def. §7.2]], [[§19 Manifolds in Euclidean Space#^prop-19-2|§19.2]]

> [!remark]- Connections
> - $\mathrm{O}(n)$ as a group in 493: [[Matrix groups GLₙ, SLₙ and O(n)]]; the analogous level-set argument for $\mathrm{SL}(n,\mathbb{R})$: [[§11 The Classical Groups Are Topological Manifolds#^cor-11-5|§11.5]].
> - Its tangent spaces: [[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-2|Ex. §23.2]]; all classical groups: [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5|§23.5]].
> - Used in Relativity: $\dim SO(3) = 3$ counts the rotation parameters when a proper orthochronous Lorentz transformation is written as a boost times a rotation — [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-6|REL Theorem §B1.2.6]].

> [!remark] Remark
> **The codomain is not a cosmetic choice.** It is essential that $F$ be regarded as a map into $\operatorname{Sym}(n,\mathbb{R})$ and not into $\operatorname{Mat}(n,\mathbb{R})$. Since $F(g)$ is always symmetric, $\operatorname{im} F \subseteq \operatorname{Sym}(n,\mathbb{R}) \subsetneq \operatorname{Mat}(n,\mathbb{R})$, so $F'(g)$ could never be surjective onto $\operatorname{Mat}(n,\mathbb{R})$; with that codomain $I$ would fail to be a regular value at every point and the theorem would yield nothing. Choosing the codomain to be exactly the space the map lands in is what makes the rank condition attainable — and it is also what produces the right dimension count, since $\dim \mathrm{O}(n) = n^2 - \dim(\text{codomain})$.

^rem-22-1

> [!remark] Remark
> The smooth structure obtained is independent of the linear coordinates used to identify $\operatorname{Mat}(n,\mathbb{R})$ with $\mathbb{R}^{n^2}$ and $\operatorname{Sym}(n,\mathbb{R})$ with $\mathbb{R}^{n(n+1)/2}$: two such identifications differ by linear isomorphisms, which are diffeomorphisms, so the level set $F^{-1}(I)$ and its graph charts transport across them without change (Proposition [[§21 The Differential of a Map Between Vector Spaces#^prop-21-2|§21.2]]). “There's no ambiguity.”

^rem-22-2

> [!theorem] Proposition §22.1: The Kernel of the Differential
> With $F(g) = gg^{\mathsf T}$ as above, for every $g \in \mathrm{O}(n)$,
>
> $$
> \ker dF_g = \{\, A \in \operatorname{Mat}(n,\mathbb{R}) \mid gA^{\mathsf T} + Ag^{\mathsf T} = 0 \,\} = g \cdot \operatorname{Skew}(n,\mathbb{R}),
> $$
>
> where $\operatorname{Skew}(n,\mathbb{R}) = \{B \mid B^{\mathsf T} = -B\}$. In particular $\ker dF_I = \operatorname{Skew}(n,\mathbb{R})$, and $\dim \ker dF_g = \tfrac{n(n-1)}{2}$ for every $g$.

^prop-22-1

> [!proof]+ Proof
> The first equality is the definition of the kernel. For the second, since $g$ is invertible every $A$ can be written uniquely as $A = gB$ with $B = g^{-1}A$. Substituting, and using $A^{\mathsf T} = B^{\mathsf T} g^{\mathsf T}$,
>
> $$
> gA^{\mathsf T} + Ag^{\mathsf T} = g B^{\mathsf T} g^{\mathsf T} + g B g^{\mathsf T} = g\,(B^{\mathsf T} + B)\,g^{\mathsf T}.
> $$
>
> As $g$ and $g^{\mathsf T}$ are invertible, this vanishes iff $B + B^{\mathsf T} = 0$, i.e. iff $B$ is skew-symmetric. Hence $\ker dF_g = \{gB \mid B \in \operatorname{Skew}(n,\mathbb{R})\}$. At $g = I$ the description reads $\ker dF_I = \operatorname{Skew}(n,\mathbb{R})$ directly: $dF_I(A) = A^{\mathsf T} + A$. Left multiplication by $g$ is a linear isomorphism of $\operatorname{Mat}(n,\mathbb{R})$, so $\dim \ker dF_g = \dim \operatorname{Skew}(n,\mathbb{R})$ for every $g$.
>
> *Counting.* A skew-symmetric matrix has zero diagonal ($B_{ii} = -B_{ii}$) and its entries below the diagonal are the negatives of those above, so it is determined by the $\tfrac{n(n-1)}{2}$ entries strictly above the diagonal, which may be chosen freely:
>
> $$
> B = \begin{pmatrix} 0 & \ast \\ -(\ast)^{\mathsf T} & \ddots \end{pmatrix}, \qquad \dim \operatorname{Skew}(n,\mathbb{R}) = \binom{n}{2} = \frac{n(n-1)}{2}.
> $$

^pf-22-1

*Uses:* [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-1|Ex. §22.1]], [[§21 The Differential of a Map Between Vector Spaces#^def-21-4|Def. §21.4]]

> [!remark]- Connections
> - This kernel is the geometric tangent space $T^{\mathrm{geo}}_g\mathrm{O}(n)$: [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-3|§23.3]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-2|Ex. §23.2]].

> [!remark] Remark: Two Readings of the Dimension
> A student asked for a combinatorial reason that $\dim \mathrm{O}(n) = \tfrac{n(n-1)}{2}$, “like choosing two out of $n$.” There are now two: the level-set count $n^2 - \tfrac{n(n+1)}{2}$ from the regular value theorem, and the kernel count $\binom{n}{2}$ from Proposition [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-22-1|§22.1]]. They agree by [[§20 Linear Algebra Toolkit#^prop-20-1|rank–nullity]]: $dF_g$ is surjective onto a space of dimension $\tfrac{n(n+1)}{2}$, so its kernel has dimension $n^2 - \tfrac{n(n+1)}{2}$. The kernel is not yet officially anything, but Uribe named it ahead of time: it is the *geometric tangent space* $T^{\mathrm{geo}}_g\mathrm{O}(n)$ to $\mathrm{O}(n)$ at $g$ (see [[§23 Tangent Spaces I꞉ The Geometric Picture|§23]]), and at $g = I$ the skew-symmetric matrices will be the *Lie algebra* $\mathfrak{so}(n)$, “in some number of weeks.” The same move produced $\nabla\det$ in Proposition [[§11 The Classical Groups Are Topological Manifolds#^prop-11-1|§11.1]], and it will recur whenever a classical group is presented as a level set.

^rem-22-3

> [!theorem] Corollary §22.2: Consequences
> $\mathrm{SO}(n)$ is a smooth manifold of dimension $\tfrac{n(n-1)}{2}$, and $\mathrm{O}(n)$ is compact.
>
> *Lee: Example 7.27*

^cor-22-2

> [!proof]+ Proof
> $\mathrm{SO}(n) = \mathrm{O}(n) \cap \det^{-1}(0,\infty)$ is an open subset of $\mathrm{O}(n)$ ($\det$ is continuous and takes only the values $\pm1$ on $\mathrm{O}(n)$, so $\mathrm{SO}(n)$ is also closed), and an open subset of a smooth $m$-manifold is a smooth $m$-manifold, its charts being restrictions of the given ones. Compactness of $\mathrm{O}(n)$ was shown in Corollary [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-8|§14.8]]: it is closed as $F^{-1}(I)$ with $F$ continuous, and bounded because every column of an orthogonal matrix is a unit vector.

^pf-22-2

*Uses:* [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-1|Ex. §22.1]], [[§10 Topological Groups and Classical Matrix Groups#^def-10-7|Def. §10.7]], [[§10 Topological Groups and Classical Matrix Groups#^prop-10-3|§10.3]], [[§3 Subspaces and Products#^prop-3-6|§3.6]], [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-8|§14.8]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Heine–Borel Theorem|590 §15.12]]

> [!remark]- Connections
> - Compactness is [[Heine–Borel Theorem|590 §15.12 (Heine–Borel)]].

**Transcription note.** Page 20 of the handwritten notes writes “$\ker dF_g(A) = \{A \mid gA^{\mathsf T} + Ag^{\mathsf T} = 0\}$”; the kernel is of the linear map $dF_g$, and the “$(A)$” does not belong. The transposes sit to the right of $g$ throughout because that is how $F$ was written ($gg^{\mathsf T}$, not $g^{\mathsf T}g$); either convention defines $\mathrm{O}(n)$.

The unitary group $\mathrm{U}(n)$ is treated the same way, with $F(g) = gg^*$ mapping into the Hermitian matrices, in [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#The Unitary Group as a Smooth Manifold|The Unitary Group as a Smooth Manifold]]. The analogue for $\mathrm{SL}(n,\mathbb{R})$ was Corollary [[§11 The Classical Groups Are Topological Manifolds#^cor-11-5|§11.5]], which Proposition [[§19 Manifolds in Euclidean Space#^prop-19-2|§19.2]] now upgrades from a topological to a smooth manifold.

> [!remark] Remark: Where This Leaves Us
> Every level set met so far is now a smooth manifold: $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$, the spheres, and any surface cut out by a regular value. What remains owed is the global half of the internal picture: a manifold defined abstractly, not sitting inside any $\mathbb{R}^N$, has no external description until one knows it can be embedded in a Euclidean space at all. That is Whitney's embedding theorem, later in the course.

^rem-22-4

## The Unitary Group as a Smooth Manifold

*Assignment 2, Problem 4. The argument is that of [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds|The Orthogonal Group as a Smooth Manifold]] with one change that is easy to get wrong: the spaces involved are complex, but the map is not complex-linear, so everything must be done over $\mathbb{R}$.*

Write $A^{\ast} = \bar A^{\mathsf T}$ for the conjugate transpose, so that $\mathrm{U}(n) = \{g \in \operatorname{Mat}(n,\mathbb{C}) \mid g^{\ast} g = I\}$. Throughout, $\operatorname{Mat}(n,\mathbb{C})$ is regarded as a *real* vector space of dimension $2n^2$ ([[§10 Topological Groups and Classical Matrix Groups#^def-10-8|Def. §10.8]]).

> [!definition] Definition §22.2: Hermitian Matrices as a Real Vector Space
> Let $\operatorname{Herm}(n) = \{A \in \operatorname{Mat}(n,\mathbb{C}) \mid A^{\ast} = A\}$. It is closed under addition and under multiplication by *real* scalars, so it is a real vector space; it is *not* a complex subspace, since $(iA)^{\ast} = -iA$. A Hermitian matrix has real diagonal entries ($a_{jj} = \overline{a_{jj}}$), arbitrary complex entries above the diagonal, and entries below the diagonal determined by $a_{kj} = \overline{a_{jk}}$. Hence
>
> $$
> \dim_{\mathbb{R}} \operatorname{Herm}(n) = n + 2\binom{n}{2} = n^2 ,
> $$
>
> and reading off the real diagonal entries and the real and imaginary parts of the entries above the diagonal gives a linear isomorphism $\operatorname{Herm}(n) \cong \mathbb{R}^{n^2}$.

^def-22-2

> [!remark]- Connections
> - Hermitian matrices are the matrices of self-adjoint operators: [[§22 Self-Adjoint and Normal Operators#^ladr-7-10|LADR 7.10]], with the conjugate transpose of [[§22 Self-Adjoint and Normal Operators#^ladr-7-7|LADR 7.7]].

> [!theorem] Lemma §22.3: A One-Sided Inverse Suffices
> If $g \in \operatorname{Mat}(n,\mathbb{C})$ satisfies $gg^* = I$, then also $g^*g = I$. Consequently $\mathrm{U}(n) = \{g \mid gg^* = I\}$.

^lem-22-3

> [!proof]+ Proof
> Taking determinants, $\det(g)\det(g^*) = 1$, so $\det g \neq 0$ and $g$ is invertible. Multiplying $gg^* = I$ on the left by $g^{-1}$ gives $g^* = g^{-1}$, hence $g^*g = I$.

^pf-22-3

*Uses:* [[§34 Determinants#^ladr-9-49|LADR 9.49]], [[Invertible ⟺ nonzero determinant|LADR 9.50]]

> [!remark]- Connections
> - The general linear-algebra fact: [[§10 Invertibility and Isomorphisms#^ladr-3-68|LADR 3.68 (ST = I ⟺ TS = I)]]; unitary matrices in LADR: [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR 7.57]].

> [!example] Example §22.2: $\mathrm{U}(n)$ Is a Smooth Manifold of Dimension $n^2$
> Define
>
> $$
> F : \operatorname{Mat}(n,\mathbb{C}) \longrightarrow \operatorname{Herm}(n), \qquad F(g) = g g^*,
> $$
>
> both regarded as real vector spaces. Then $\mathrm{U}(n) = F^{-1}(I)$, the identity is a regular value, and $\mathrm{U}(n)$ is a smooth manifold of dimension $2n^2 - n^2 = n^2$.
>
> *Lee: Example 7.29*

^ex-22-2

![[m591-10-6.svg]]
*The map $F(g) = gg^{\ast}$ and its coordinate representation $\widehat F$ under the real-linear identifications $\operatorname{Mat}(n,\mathbb{C}) \cong \mathbb{R}^{2n^2}$ and $\operatorname{Herm}(n) \cong \mathbb{R}^{n^2}$.*

The vertical arrows are the real-linear identifications of [[§10 Topological Groups and Classical Matrix Groups#^def-10-8|Def. §10.8]] and [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^def-22-2|Def. §22.2]]. This is the square of [[§21 The Differential of a Map Between Vector Spaces|The Differential of a Map Between Vector Spaces]] with $X = \operatorname{Mat}(n,\mathbb{C})$ and $Y = \operatorname{Herm}(n)$ regarded as real vector spaces: $F$ is smooth, and $I$ is a regular value, exactly when the same holds for $\widehat F$ (Lemma [[§21 The Differential of a Map Between Vector Spaces#^lem-21-1|§21.1]], Corollary [[§21 The Differential of a Map Between Vector Spaces#^cor-21-4|§21.4]]). Nothing is computed in the bottom row; it only certifies that the top row may be used.

> [!proof]+ Proof
> *$F$ is well defined and smooth.* $(gg^{\ast})^{\ast} = g^{\ast \ast}g^{\ast} = gg^{\ast}$, so $F$ lands in $\operatorname{Herm}(n)$. Each entry $(gg^{\ast})_{jk} = \sum_m g_{jm}\overline{g_{km}}$ has real and imaginary parts that are quadratic polynomials in the real coordinates of $g$, so $F$ is smooth ([[§21 The Differential of a Map Between Vector Spaces#^def-21-2|Def. §21.2]]).
>
> *$\mathrm{U}(n) = F^{-1}(I)$.* Lemma [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^lem-22-3|§22.3]].
>
> *The differential.* By Theorem [[§21 The Differential of a Map Between Vector Spaces#^thm-21-3|§21.3]], for $g \in F^{-1}(I)$ and $h \in \operatorname{Mat}(n,\mathbb{C})$, $dF_g(h) = \frac{d}{dt}\big|_{t=0} F(g+th)$ with $t$ *real*. Since $(th)^{\ast} = t h^{\ast}$ for real $t$,
>
> $$
> F(g+th) = (g+th)(g^* + th^*) = gg^* + t\big(hg^* + gh^*\big) + t^2\, hh^*,
> \qquad\text{so}\qquad
> dF_g(h) = hg^* + gh^* ,
> $$
>
> which is Hermitian, as it must be.
>
> *$dF_g$ is surjective.* Put $X = hg^{\ast}$; then $gh^{\ast} = (hg^{\ast})^{\ast} = X^{\ast}$, so $dF_g(h) = X + X^{\ast}$. As $g$ is invertible, $h \mapsto hg^{\ast}$ is a real-linear bijection of $\operatorname{Mat}(n,\mathbb{C})$, with inverse $X \mapsto Xg$. Hence $\operatorname{im} dF_g = \{X + X^{\ast} \mid X \in \operatorname{Mat}(n,\mathbb{C})\} = \operatorname{Herm}(n)$, since any Hermitian $A$ arises from $X = \tfrac12 A$. Explicitly $h = \tfrac12 Ag$:
>
> $$
> hg^* = \tfrac12 A gg^* = \tfrac12 A, \qquad gh^* = \tfrac12\, g g^* A^* = \tfrac12 A .
> $$
>
> ![[m591-10-7.svg]]
>
> The surjectivity argument as a diagram: $dF_g$ factors as a bijection followed by $X \mapsto X + X^*$, and the second map is onto $\operatorname{Herm}(n)$, hitting $A$ at $X = \tfrac12 A$. Hence $dF_g$ is onto.
>
> *Conclusion.* $\dim_{\mathbb{R}}\operatorname{Mat}(n,\mathbb{C}) = 2n^2 \ge n^2 = \dim_{\mathbb{R}}\operatorname{Herm}(n)$, so by Corollary [[§21 The Differential of a Map Between Vector Spaces#^cor-21-4|§21.4]] surjectivity of $dF_g$ at every $g \in F^{-1}(I)$ is exactly the statement that $I$ is a regular value. Proposition [[§19 Manifolds in Euclidean Space#^prop-19-2|§19.2]] makes $\mathrm{U}(n)$ a smooth manifold of dimension $2n^2 - n^2 = n^2$.

^pf-ex-22-2

*Uses:* [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^def-22-2|Def. §22.2]], [[§10 Topological Groups and Classical Matrix Groups#^def-10-8|Def. §10.8]], [[§21 The Differential of a Map Between Vector Spaces#^def-21-2|Def. §21.2]], [[§21 The Differential of a Map Between Vector Spaces#^lem-21-1|§21.1]], [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^lem-22-3|§22.3]], [[§21 The Differential of a Map Between Vector Spaces#^thm-21-3|§21.3]], [[§21 The Differential of a Map Between Vector Spaces#^cor-21-4|§21.4]], [[§19 Manifolds in Euclidean Space#^prop-19-2|§19.2]]

> [!remark]- Connections
> - Unitary matrices in LADR: [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-56|LADR 7.56]]; $\mathrm{U}(1)$ is the circle, [[§10 Topological Groups and Classical Matrix Groups#^ex-10-3|Ex. §10.3]].
> - Its tangent spaces: [[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-3|Ex. §23.3]].

> [!remark] Remark
> **Why over $\mathbb{R}$.** The derivative $h \mapsto hg^{\ast} + gh^{\ast}$ is real-linear but not complex-linear: $dF_g(ih) = i\,hg^{\ast} - i\,gh^{\ast}$, which differs from $i\,dF_g(h)$ unless $gh^{\ast} = 0$. This is the conjugation in $g^{\ast}$ at work, and it is why Problem 4 insists that both spaces be regarded as real vector spaces. It is also why the holomorphic regular value theorem of [[§7 The Regular Value Theorem#Holomorphic Level Sets|§7, Holomorphic Level Sets]] does not apply, and why $\dim \mathrm{U}(n) = n^2$ can be odd, which no holomorphic level set can.

^rem-22-5

> [!theorem] Proposition §22.4: The Kernel of the Differential
> For $g \in \mathrm{U}(n)$,
>
> $$
> \ker dF_g = \mathfrak{u}(n)\cdot g = g \cdot \mathfrak{u}(n), \qquad \mathfrak{u}(n) = \{X \in \operatorname{Mat}(n,\mathbb{C}) \mid X^* = -X\},
> $$
>
> the skew-Hermitian matrices, and $\dim_{\mathbb{R}} \mathfrak{u}(n) = n^2$.

^prop-22-4

> [!proof]+ Proof
> Every $h$ can be written uniquely as $h = Xg$ with $X = hg^*$, and then $dF_g(Xg) = Xgg^* + gg^*X^* = X + X^*$, which vanishes iff $X \in \mathfrak{u}(n)$. So $\ker dF_g = \mathfrak{u}(n)\cdot g$. For the second description, conjugation by $g$ preserves $\mathfrak{u}(n)$: if $X^* = -X$ then $(gXg^*)^* = gX^*g^* = -gXg^*$; so $g \cdot \mathfrak{u}(n) = (g\,\mathfrak{u}(n)\,g^{-1})\cdot g = \mathfrak{u}(n)\cdot g$. A skew-Hermitian matrix has purely imaginary diagonal ($n$ real parameters) and arbitrary complex entries above the diagonal ($2\binom n2$ real parameters), so $\dim_{\mathbb{R}}\mathfrak{u}(n) = n^2$ — agreeing with $\dim \mathrm{U}(n)$ by [[§20 Linear Algebra Toolkit#^prop-20-1|rank–nullity]], $2n^2 - n^2$.

^pf-22-4

*Uses:* [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-2|Ex. §22.2]], [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^lem-22-3|§22.3]], [[§20 Linear Algebra Toolkit#^prop-20-1|§20.1]]

> [!remark]- Connections
> - The geometric tangent space of $\mathrm{U}(n)$: [[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-3|Ex. §23.3]]; the orthogonal analogue: [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-22-1|§22.1]].

> [!theorem] Corollary §22.5: $\mathrm{U}(n)$ Is Compact
> $\mathrm{U}(n)$ is a compact smooth manifold of dimension $n^2$.
>
> *Lee: Example 7.29*

^cor-22-5

> [!proof]+ Proof
> It is closed in $\operatorname{Mat}(n,\mathbb{C}) \cong \mathbb{R}^{2n^2}$ as $F^{-1}(I)$ with $F$ continuous, and bounded because the columns of a unitary matrix are unit vectors of $\mathbb{C}^n$, so every entry has modulus at most $1$. Apply Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](1).

^pf-22-5

*Uses:* [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-2|Ex. §22.2]], [[§10 Topological Groups and Classical Matrix Groups#^def-10-8|Def. §10.8]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Heine–Borel Theorem|590 §15.12]]

> [!remark]- Connections
> - Proposition §1.8(1) is [[Heine–Borel Theorem|590 §15.12 (Heine–Borel)]]; columns of unitary matrices are orthonormal by [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR 7.57]].
