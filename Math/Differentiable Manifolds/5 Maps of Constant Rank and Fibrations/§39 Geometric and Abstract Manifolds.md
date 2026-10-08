---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 39
tags: [differentiable-manifolds, math591]
---
← [[§38 Embeddings]] · ↑ [[· 5 Maps of Constant Rank and Fibrations]] · [[§40 Projective Spaces and the Hopf Fibration]] →

*Stage: recap — The two pictures of a manifold — a subset of Euclidean space, and a space with an atlas — set side by side, aspect by aspect, with the theorem that bridges each pair.*

*Not from lecture: a comparison written for these notes at the end of Chapter 5, when every bridge between the two pictures is in place. Nothing here is new; every object is defined, and every fact proved, where the cross-reference points.*

The course has built manifolds in two ways. The *geometric* picture is the equations thread of the roadmap: a manifold is a subset of some $\mathbb{R}^N$, cut out by equations or swept out by a parametrization, and everything — smoothness, tangent vectors, differentials — is inherited from the ambient space. The *abstract* picture needs no ambient space: a manifold is a topological space with a maximal smooth atlas, and every notion is defined through charts. The geometric picture is concrete and computable; the abstract one is intrinsic and covers the quotients. For each aspect, the table names the two versions and the result that shows they agree wherever both make sense.

| Aspect | Geometric (inside $\mathbb{R}^N$) | Abstract (charts only) | Bridge |
|---|---|---|---|
| the object | external, internal or graph description ([[§20 Manifolds in Euclidean Space\|§20]]) | maximal atlas (Definition [[§17 Differentiable Structures#^def-17-9\|§17.9]]) | Proposition [[§35 Submanifolds#^prop-35-6\|§35.6]] |
| examples | level sets: spheres, $\mathrm{SL}$, $\mathrm{O}(n)$, $\mathrm{U}(n)$ | also quotients: $\mathbb{CP}^n$, $G/H$, Grassmannians | — |
| smooth structure | graph charts (Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2\|§20.2]]) | chosen atlas; induced on submanifolds (Proposition [[§35 Submanifolds#^prop-35-2\|§35.2]]) | Proposition [[§35 Submanifolds#^prop-35-9\|§35.9]](1) |
| smooth maps | restrictions of ambient maps (Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3\|§20.3]]) | smooth in charts (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3\|§19.3]]) | Lemma [[§35 Submanifolds#^lem-35-3\|§35.3]] |
| tangent space | velocities, $\ker F'(p)$ (Theorem [[§25 The Geometric Tangent Space#^thm-25-3\|§25.3]]) | derivations of germs (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2\|§28.2]]) | Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6\|§29.6]], Proposition [[§35 Submanifolds#^prop-35-9\|§35.9]](2) |
| differential | the derivative $F'(p)$ (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5\|§22.5]]) | pushforward $F_{*p}$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6\|§28.6]]) | Theorem [[§30 The Differential in Coordinates#^thm-30-2\|§30.2]], Proposition [[§30 The Differential in Coordinates#^prop-30-5\|§30.5]] |
| normal directions | normal vectors, via the dot product | conormal covectors (Definition [[§35 Submanifolds#^def-35-3\|§35.3]]) | a metric ([[§35 Submanifolds#^rem-35-1\|No Normal Vectors Without a Metric]]) |
| regular values | Theorem [[§7 The Regular Value Theorem#^thm-7-3\|§7.3]], Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2\|§20.2]] | Theorem [[§35 Submanifolds#^thm-35-7\|§35.7]] | [[§35 Submanifolds#^rem-35-3\|Regular Value Theorems — Old and New]] |
| submanifolds | level sets in $\mathbb{R}^N$ | adapted charts (Definition [[§35 Submanifolds#^def-35-1\|§35.1]]) | Proposition [[§35 Submanifolds#^prop-35-6\|§35.6]] |
| global picture | inside $\mathbb{R}^N$ by construction | no ambient space | embeddings (Theorem [[§38 Embeddings#^thm-38-1\|§38.1]]) |

## The Object

Geometrically, a manifold is a subset of a Euclidean space that is, near each of its points, one of three equivalent things (Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]]):

![[§20 Manifolds in Euclidean Space#^def-20-1]]

![[§20 Manifolds in Euclidean Space#^def-20-2]]

— or a graph over $n$ of the coordinates. Abstractly, a manifold is a topological manifold together with a choice of charts:

![[§17 Differentiable Structures#^def-17-9]]

The bridge is the slice description. A subset of $\mathbb{R}^{n+k}$ has the three Euclidean descriptions near each point exactly when it is a submanifold of $\mathbb{R}^{n+k}$ in the abstract sense, the coordinate plane of an adapted chart (Proposition [[§35 Submanifolds#^prop-35-6|§35.6]]), and then it is a smooth manifold in its own right (Proposition [[§35 Submanifolds#^prop-35-2|§35.2]]). The circle shows all of this at once: its external, graph and internal descriptions (Example [[§24 The Circle#^ex-24-1|§24.1]]), and three atlases — four charts, stereographic and angle — that define one smooth structure ([[§24 The Circle|§24]]).

## Where the Examples Come From

The geometric examples are level sets: the spheres ([[§8 Spheres|§8]]), and the classical groups $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$, $\mathrm{U}(n)$ as level sets in spaces of matrices (Theorem [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|§12.6]], smooth by [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds|§23]]). The abstract picture adds the spaces built by gluing: $\mathbb{CP}^n$ ([[§9 Complex Projective Space|§9]], with its standard charts in [[§18 Projective Spaces as Smooth Manifolds|§18]]), coset spaces $G/H$ ([[§14 Homogeneous Spaces|§14]]) and the Grassmannians (Corollary [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|§15.8]]). These arrive with no ambient space: a point of $\mathbb{CP}^n$ is a line, not a point of some $\mathbb{R}^N$. Some of them can be placed in a Euclidean space afterwards — that is what an embedding does (below) — but not as constructed.

## Smooth Structures and Smooth Maps

A level set inherits its smooth structure from the ambient space: the graph charts project it onto coordinate planes, and their transition maps are smooth because they factor through $\mathbb{R}^{n+k}$ (Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]). An abstract manifold has the structure it is given; the same topological space can carry incompatible atlases — the two structures on $\mathbb{R}$ — which are nevertheless diffeomorphic ([[§17 Differentiable Structures|§17]], [[§19 Smooth Functions and Smooth Maps|§19]]). For a submanifold the two agree: the graph-chart structure is the induced one (Proposition [[§35 Submanifolds#^prop-35-9|§35.9]](1)).

Maps follow the same pattern. Geometrically, a map into or out of a level set is smooth when it is a restriction of, or lands in, a smooth map between Euclidean spaces (Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]]). Abstractly, a map is smooth when its coordinate representations are (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]). Lemma [[§35 Submanifolds#^lem-35-3|§35.3]] says the same as Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]] for submanifolds of any manifold.

## Tangent Vectors and Differentials

This is where the two pictures look most different.

![[§25 The Geometric Tangent Space#^def-25-1]]

![[§28 Derivations and the Abstract Tangent Space#^def-28-2]]

A geometric tangent vector is an arrow in the ambient space; an abstract one is a derivation, a machine that differentiates germs. Geometrically the tangent space is computed as a kernel, $T^{\mathrm{geo}}_pM = \ker F'(p)$ (Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]); abstractly it has the coordinate basis $\partial/\partial x^i|_p$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]). Three bridges connect them: an arrow $v$ gives the directional derivative $D_v$, and for a level set $v \mapsto D_v$ is an isomorphism $T^{\mathrm{geo}}_pM \to T_pM$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]); every abstract tangent vector is the velocity of a curve, which restores the arrow picture without an ambient space (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]]); and for a submanifold of $\mathbb{R}^{n+k}$, the inclusion carries $T_pS$ onto $T^{\mathrm{geo}}_pS$ (Proposition [[§35 Submanifolds#^prop-35-9|§35.9]](2) and the remark [[§35 Submanifolds#^rem-35-2|The Tangent Spaces Match]]).

The differential follows: geometrically it is the ordinary derivative, a linear map between the ambient spaces restricted to tangent spaces (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|§22.5]]); abstractly it is the pushforward $F_{*p}D = D \circ F_p^*$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]). In coordinates the pushforward has the Jacobian of the coordinate representation as its matrix (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]), and on open subsets of vector spaces it is the ordinary derivative (Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]); either can be computed by curves (Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]]).

## Normal Vectors and Conormal Covectors

In $\mathbb{R}^{n+k}$ a level set $F^{-1}(c)$ has normal vectors: the orthogonal complement of $T^{\mathrm{geo}}_pM = \ker F'(p)$ is the row space of $F'(p)$, spanned by the gradients $\nabla F^1(p), \ldots, \nabla F^k(p)$. Orthogonality needs the dot product, which an abstract manifold does not have. Its substitute is the conormal space, the covectors that vanish on the tangent space (Definition [[§35 Submanifolds#^def-35-3|§35.3]]), with the basis $dF^1|_p, \ldots, dF^k|_p$ for a level set (Proposition [[§35 Submanifolds#^prop-35-5|§35.5]]). A metric — an inner product on each tangent space — identifies covectors with vectors and turns conormal covectors back into normal vectors (the remark [[§35 Submanifolds#^rem-35-1|No Normal Vectors Without a Metric]]); in $\mathbb{R}^{n+k}$ the dot product does this, and $dF^i|_p$ becomes $\nabla F^i(p)$.

## Regular Values and Submanifolds

The regular value theorem exists in five forms, from level sets in $\mathbb{R}^{n+k}$ (Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]) to level sets in any manifold (Theorem [[§35 Submanifolds#^thm-35-7|§35.7]]); the remark [[§35 Submanifolds#^rem-35-3|The Regular Value Theorems — Old and New]] lists them with their roles. What they produce is, geometrically, a level set and, abstractly, a submanifold:

![[§35 Submanifolds#^def-35-1]]

In $\mathbb{R}^{n+k}$ the two coincide (Proposition [[§35 Submanifolds#^prop-35-6|§35.6]]): straightening a graph gives an adapted chart, and the last coordinates of an adapted chart are defining equations.

## The Global Picture: Embeddings

A geometric manifold sits in $\mathbb{R}^N$ by construction; an abstract one need not sit anywhere. The bridge is an embedding:

![[§38 Embeddings#^def-38-1]]

The image of an embedding is a submanifold (Theorem [[§38 Embeddings#^thm-38-1|§38.1]]), so an abstract manifold with an embedding into $\mathbb{R}^N$ is diffeomorphic to a geometric one, and all the comparisons above apply to it. Injective immersions are not enough: the figure-eight and the irrational line on the torus are injective immersions whose images are not submanifolds ([[§37 Immersions|§37]], [[§38 Embeddings|§38]]).

> [!remark] Remark: Whitney's Embedding Theorem
> *(Not from lecture; stated, not proved, in these notes.)* Every smooth $m$-manifold — Hausdorff and second countable, as in Definition [[§17 Differentiable Structures#^def-17-9|§17.9]] — admits a smooth embedding into $\mathbb{R}^{2m+1}$ (Lee, Theorem 6.15), and Whitney improved the dimension to $2m$. So no manifold is out of reach of the geometric picture: every abstract manifold is diffeomorphic to a submanifold of some Euclidean space. The abstract definition is still the right one, because the embedding is not part of the manifold: the same manifold has many embeddings, none of them preferred, and quotients such as $\mathbb{CP}^n$ come with none.

^rem-39-1

## What Each Picture Gives

The geometric picture gives computations: a tangent space is a kernel, a differential is a Jacobian, a normal vector is a gradient, and all of it can be drawn. The abstract picture gives intrinsic definitions: the tangent space of $\mathbb{CP}^n$ or of $G/H$ makes sense without choosing where to put them, and every notion is independent of an embedding — which is why the bundles, fields and forms of the next chapters are built on the abstract side. The bridges in the table are what let the course compute in the geometric picture and conclude in the abstract one.
