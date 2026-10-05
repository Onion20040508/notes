---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 2
section: 15
tags: [differentiable-manifolds, math591]
---
← [[§14 The Topology of G∕H and Real Grassmannians]] · ↑ [[· 2 Topological Groups and Homogeneous Spaces]] · [[§16 Differentiable Structures]] →

*Thread: equations — The classical matrix groups of [[§10 Topological Groups and Classical Matrix Groups|§10]] as examples: the determinant disconnects $\mathrm{GL}(n,\mathbb{R})$ and $\mathrm{O}(n)$, $\mathrm{SO}(n)$ is a proper subgroup of $\mathrm{O}(n)$, and $\mathrm{U}(1)$ is the circle.*

The classical groups through the course: defined in [[§10 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of *this section*; topological manifolds as level sets in [[§11 The Classical Groups Are Topological Manifolds#^thm-11-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§12 Group Actions and Orbit Spaces#^ex-12-4|the rotations of the plane]] and [[§12 Group Actions and Orbit Spaces#^ex-12-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§13 Homogeneous Spaces#^ex-13-2|the isotropy of the north pole]] and [[§13 Homogeneous Spaces#^ex-13-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-1|the orthogonal group]] and [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-2|the unitary group]]; their tangent spaces at the identity in [[§23 The Geometric Tangent Space#^thm-23-5|The Classical Groups]], with [[§23 The Geometric Tangent Space#^ex-23-4|the infinitesimal rotations]]; and the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§38 SU(2) → SO(3)꞉ The Double Cover#^thm-38-10|The Double Cover]].

> [!theorem] Proposition §15.1: $\mathrm{GL}(n,\mathbb{R})$ Is Disconnected
> $\mathrm{GL}(n,\mathbb{R}) = \det^{-1}(0,\infty) \sqcup \det^{-1}(-\infty,0)$ is a disjoint union of two nonempty open sets, hence disconnected.
>
> *Lee: Proposition 21.35*

^prop-15-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Both sets are open as preimages of open sets under the continuous $\det$ ([[§10 Topological Groups and Classical Matrix Groups#^prop-10-3|Proposition §10.3]]), they are disjoint, their union is $\mathrm{GL}(n,\mathbb{R})$ since $\det \neq 0$ there, and both are nonempty ($I$ and $\mathrm{diag}(1,\ldots,1,-1)$).

^pf-15-1

*Uses:* [[§10 Topological Groups and Classical Matrix Groups#^prop-10-3|§10.3]], [[§10 Topological Groups and Classical Matrix Groups#^def-10-4|Def. §10.4]], [[§13 Connected Spaces#^def-13-1|590 Def. §13.1]], [[§9 Continuous Functions#^def-9-1|590 Def. §9.1]]

> [!remark]- Connections
> - The general principle: a continuous map onto a disconnected space forces disconnectedness, contrapositive of [[Continuous Image of a Connected Space is Connected|590 §13.3]].
> - Used in Relativity: the determinant splits the Lorentz group as it splits $O(n)$, and the sign of $\Lambda^0{}_0$ splits it once more, into four components — [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-4|REL Theorem §B1.2.4]].

> [!theorem] Theorem §15.2: Exactly Two Components
> Each of $\det^{-1}(0,\infty)$ and $\det^{-1}(-\infty,0)$ is connected, so $\mathrm{GL}(n,\mathbb{R})$ has exactly two connected components.
>
> *Lee: Proposition 21.35, via Proposition 21.34*

^thm-15-2

> [!proof]+ Proof (to be filled)
> Not proved here (stated in lecture; Lee, Proposition 21.35). To be filled.

^pf-15-2

**Not proved here.** Stated in lecture with “we'll say more about that.” The usual argument reduces a matrix of positive determinant to the identity by a path, using Gaussian elimination or the polar decomposition together with connectedness of $\mathrm{SO}(n)$. Only [[§15 The Classical Groups#^prop-15-1|Proposition §15.1]] is needed below.

![[m591-5-1.svg]]
*$\mathrm{O}(2)$ as two circles: the rotations $\mathrm{SO}(2)$ over $\det = +1$ and the reflections $R_\theta S$ over $\det = -1$.*

$\mathrm{O}(2)$ drawn as two circles. The rotations $R_\theta$ form $\mathrm{SO}(2)$, the matrices of determinant $1$, a circle through $I$. The matrices of determinant $-1$ are the reflections $R_\theta S$ with $S = \mathrm{diag}(1, -1)$ — if $\det A = -1$ then $AS \in \mathrm{SO}(2)$ — a second circle. The determinant is continuous with only the values $\pm 1$ on $\mathrm{O}(n)$, so it splits $\mathrm{O}(n)$ into two disjoint open and closed pieces, by the argument that disconnects $\mathrm{GL}(n,\mathbb{R})$ ([[§15 The Classical Groups#^prop-15-1|Proposition §15.1]]). That each piece is connected, so that $\mathrm{O}(n)$ has exactly two components, is Lee's Proposition 21.34.

> [!example] Example §15.1: Why $\mathrm{SO}(n)$ Is a Proper Subgroup of $\mathrm{O}(n)$
> A student asked why one bothers to intersect with $\mathrm{SL}$: does $\mathrm{O}(n)$ not already sit inside $\mathrm{SL}(n)$? No: $\det = \pm 1$, and both signs occur. The reflection
>
> $$
> g = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
> $$
>
> across the $x$-axis is orthogonal ($g^T g = I$) with $\det g = -1$, so $g \in \mathrm{O}(2,\mathbb{R}) \setminus \mathrm{SO}(2,\mathbb{R})$. The same works in every dimension with $\mathrm{diag}(1, \ldots, 1, -1)$.

^ex-15-1