---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 39
tags: [differentiable-manifolds, math591]
---
← [[§38 Embeddings]] · ↑ [[· 5 Maps of Constant Rank and Fibrations]] · [[§40 Projective Spaces and the Hopf Fibration]] →

*Stage: recap — The two pictures of a manifold — a subset of Euclidean space, and a space with an atlas — set side by side, definition by definition and theorem by theorem, with the result that bridges each pair.*

*Not from lecture: a comparison written for these notes at the end of Chapter 5, when every bridge between the two pictures is in place. Nothing here is new; every object is defined, and every fact proved, where the cross-reference points.*

The course has built manifolds in two ways. The *geometric* picture is the equations thread of the roadmap: a manifold is a subset of some $\mathbb{R}^N$, cut out by equations or swept out by a parametrization, and everything — smoothness, tangent vectors, differentials, regular values — is inherited from the ambient space. The *abstract* picture needs no ambient space: a manifold is a topological space with a maximal smooth atlas, and every notion is defined through charts. Almost every definition and theorem of the geometric picture has a counterpart in the abstract one, usually proved by reducing to the geometric version in charts. Each part below lists the pairs one to one, recalls the central ones verbatim, and names the result that shows the two agree wherever both make sense.

| Aspect | Geometric (inside $\mathbb{R}^N$) | Abstract (charts only) | Bridge |
|---|---|---|---|
| the object | external, internal or graph description | maximal atlas; submanifold | Proposition [[§35 Regular Submanifolds#^prop-35-6\|§35.6]] |
| smooth structure | graph charts | chosen or induced atlas | Proposition [[§35 Regular Submanifolds#^prop-35-9\|§35.9]](1) |
| smooth maps | smooth between vector spaces | smooth in charts | Lemma [[§35 Regular Submanifolds#^lem-35-3\|§35.3]] |
| tangent space | velocities, $\ker F'(p)$ | derivations of germs | Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6\|§29.6]] |
| differential | Jacobian $F'(p)$ | pushforward $F_{\ast p}$ | Theorem [[§30 The Differential in Coordinates#^thm-30-2\|§30.2]] |
| covectors | gradient $\nabla f$, transpose $J^{\mathsf T}$ | $df_p$, pullback $F_p^{\ast}$ | the remark [[§32 The Cotangent Space#^rem-32-6\|The Two Differentials Meet]] |
| regular points | $F'(p)$ surjective | $F_{\ast p}$ surjective | Proposition [[§30 The Differential in Coordinates#^prop-30-7\|§30.7]] |
| key theorems | implicit and inverse function theorems | normal form; local diffeomorphism criterion | proved through charts |
| regular values | level sets are manifolds | level sets are submanifolds | Proposition [[§35 Regular Submanifolds#^prop-35-9\|§35.9]] |
| global picture | inside $\mathbb{R}^N$ by construction | no ambient space | Theorem [[§38 Embeddings#^thm-38-1\|§38.1]] |

## The Object and Its Smooth Structure

| Geometric | Abstract | How they correspond |
|---|---|---|
| Definition [[§20 Manifolds in Euclidean Space#^def-20-1\|§20.1]] (external: a regular level set) | Definition [[§35 Regular Submanifolds#^def-35-1\|§35.1]] (a coordinate slice of an adapted chart, Definition [[§35 Regular Submanifolds#^def-35-2\|§35.2]]) | Proposition [[§35 Regular Submanifolds#^prop-35-6\|§35.6]]: the slice is a fourth equivalent description |
| Definition [[§20 Manifolds in Euclidean Space#^def-20-2\|§20.2]], Definition [[§20 Manifolds in Euclidean Space#^def-20-3\|§20.3]] (a parametrization) | the inverse of a chart (the remark [[§20 Manifolds in Euclidean Space#^rem-20-2\|A Parametrization Is an Inverse Chart]]); Definition [[§37 Immersions#^def-37-1\|§37.1]] | rank $n$ Jacobian = immersion; homeomorphism onto the image = embedding (Definition [[§38 Embeddings#^def-38-1\|§38.1]]) |
| Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1\|§20.1]] (the descriptions agree) | Proposition [[§35 Regular Submanifolds#^prop-35-6\|§35.6]], Theorem [[§38 Embeddings#^thm-38-1\|§38.1]] | straightening a graph gives an adapted chart |
| Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2\|§20.2]] (graph charts) | Definition [[§17 Differentiable Structures#^def-17-9\|§17.9]]; Proposition [[§35 Regular Submanifolds#^prop-35-2\|§35.2]] (induced structure) | Proposition [[§35 Regular Submanifolds#^prop-35-9\|§35.9]](1): the same structure |
| Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-4\|§22.4]] (a vector space) | Proposition [[§22 The Differential of a Map Between Vector Spaces#^prop-22-2\|§22.2]] | a vector space is a manifold with one global chart |

Geometrically, a manifold is a subset of a Euclidean space with one of three equivalent local descriptions (Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]]):

![[§20 Manifolds in Euclidean Space#^def-20-1]]

![[§20 Manifolds in Euclidean Space#^def-20-2]]

— or a graph over $n$ of the coordinates. Abstractly, a manifold is a topological manifold with a choice of charts, and the subsets that look like the geometric ones are the submanifolds:

![[§17 Differentiable Structures#^def-17-9]]

![[§35 Regular Submanifolds#^def-35-1]]

A subset of $\mathbb{R}^{n+k}$ has the three Euclidean descriptions near each point exactly when it is a submanifold of $\mathbb{R}^{n+k}$ (Proposition [[§35 Regular Submanifolds#^prop-35-6|§35.6]]), and the graph-chart structure of Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]] is then the induced one (Proposition [[§35 Regular Submanifolds#^prop-35-9|§35.9]](1)). The circle shows all of this at once: its external, graph and internal descriptions (Example [[§24 The Circle#^ex-24-1|§24.1]]), and three atlases — four charts, stereographic and angle — that define one smooth structure ([[§24 The Circle|§24]]).

## Where the Examples Come From

The geometric examples are level sets: the spheres ([[§8 Spheres|§8]]), and the classical groups $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$, $\mathrm{U}(n)$ as level sets in spaces of matrices (Theorem [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|§12.6]], smooth by [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds|§23]]). The abstract picture adds the spaces built by gluing: $\mathbb{CP}^n$ ([[§9 Complex Projective Space|§9]], with its standard charts in [[§18 Projective Spaces as Smooth Manifolds|§18]]), coset spaces $G/H$ ([[§14 Homogeneous Spaces|§14]]) and the Grassmannians (Corollary [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|§15.8]]). These arrive with no ambient space: a point of $\mathbb{CP}^n$ is a line, not a point of some $\mathbb{R}^N$. Some of them can be placed in a Euclidean space afterwards — that is what an embedding does (below) — but not as constructed.

## Smooth Maps

| Geometric | Abstract | How they correspond |
|---|---|---|
| Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-3\|§22.3]] (smooth between vector spaces) | Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3\|§19.3]] (smooth in charts) | Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-3\|§19.3]]: the two notions of diffeomorphism agree |
| Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3\|§20.3]] (maps into and out of level sets) | Lemma [[§35 Regular Submanifolds#^lem-35-3\|§35.3]] (maps into and out of submanifolds) | the same statement, for submanifolds of any manifold |
| Theorem [[§33 Local Diffeomorphisms#^thm-33-1\|§33.1]] (inverse function theorem) | Theorem [[§33 Local Diffeomorphisms#^thm-33-2\|§33.2]] (local diffeomorphism criterion) | the criterion is the inverse function theorem in charts |

![[§33 Local Diffeomorphisms#^thm-33-1]]

![[§33 Local Diffeomorphisms#^thm-33-2]]

A map into or out of a level set is smooth when it is a restriction of, or lands in, a smooth map between Euclidean spaces; abstractly, when its coordinate representations are. Every abstract statement about smoothness is proved by reading it in charts, where it becomes the Euclidean one: the local diffeomorphism criterion is the inverse function theorem applied to a coordinate representation.

## Tangent Vectors

| Geometric | Abstract | How they correspond |
|---|---|---|
| Definition [[§25 The Geometric Tangent Space#^def-25-1\|§25.1]] (velocities $\gamma'(0)$ in $\mathbb{R}^{n+k}$) | Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2\|§28.2]] (derivations of germs, Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1\|§28.1]]) | Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6\|§29.6]]: $v \mapsto D_v$ is an isomorphism |
| Definition [[§25 The Geometric Tangent Space#^def-25-4\|§25.4]] (the directional derivative $D_v$) | Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1\|§28.1]] (a derivation at $p$) | Proposition [[§25 The Geometric Tangent Space#^prop-25-8\|§25.8]], Proposition [[§25 The Geometric Tangent Space#^prop-25-9\|§25.9]]: $D_v$ is a derivation and determines $v$ |
| $\gamma'(0)$, the velocity in the ambient space | Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2\|§31.2]]; Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2\|§31.2]] | every abstract tangent vector is a velocity |
| Lemma [[§25 The Geometric Tangent Space#^lem-25-1\|§25.1]] (locality) | Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8\|§28.8]] (open subsets have the same tangent spaces) | both depend only on a neighbourhood of $p$ |
| Lemma [[§25 The Geometric Tangent Space#^lem-25-2\|§25.2]] (tangent space of a graph) | Proposition [[§35 Regular Submanifolds#^prop-35-4\|§35.4]] (tangent space of a submanifold) | the span of the first coordinate directions of a slice |
| Theorem [[§25 The Geometric Tangent Space#^thm-25-3\|§25.3]] ($T^{\mathrm{geo}}_pM = \ker F'(p)$) | Theorem [[§35 Regular Submanifolds#^thm-35-7\|§35.7]] ($\iota_{\ast p}(T_pS) = \ker F_{\ast p}$) | Proposition [[§35 Regular Submanifolds#^prop-35-9\|§35.9]](2) |
| Theorem [[§25 The Geometric Tangent Space#^thm-25-7\|§25.7]] (dimension) | Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5\|§29.5]] (basis theorem) | both give dimension $n$ |

![[§25 The Geometric Tangent Space#^def-25-1]]

![[§28 Derivations and the Abstract Tangent Space#^def-28-2]]

![[§25 The Geometric Tangent Space#^thm-25-3]]

A geometric tangent vector is an arrow in the ambient space; an abstract one is a machine that differentiates germs. The arrow $v$ becomes the machine $D_v$, and for a level set $v \mapsto D_v$ is an isomorphism $T^{\mathrm{geo}}_pM \to T_pM$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]); conversely every abstract tangent vector is the velocity of a curve (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]]), which restores the arrow picture without an ambient space. For a submanifold of $\mathbb{R}^{n+k}$ the inclusion carries $T_pS$ onto $T^{\mathrm{geo}}_pS$ (Proposition [[§35 Regular Submanifolds#^prop-35-9|§35.9]](2) and the remark [[§35 Regular Submanifolds#^rem-35-2|The Tangent Spaces Match]]).

## Differentials: the Jacobian and the Pushforward

| Geometric | Abstract | How they correspond |
|---|---|---|
| Definition [[§7 The Regular Value Theorem#^def-7-1\|§7.1]] (Jacobian matrix $DF_p$); Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5\|§22.5]] ($dF_p$ between vector spaces) | Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6\|§28.6]] (pushforward $F_{\ast p}$) | Theorem [[§30 The Differential in Coordinates#^thm-30-2\|§30.2]]: the matrix of $F_{\ast p}$ is the Jacobian of the coordinate representation |
| composition $g \circ F$ inside the chain rule | Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-5\|§28.5]] (pullback of germs $F_p^{\ast}$) | $F_{\ast p}D = D \circ F_p^{\ast}$: the pushforward is defined through the pullback |
| Theorem [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3\|§22.3]] ($dF_p(v) = \tfrac{d}{dt}F(p + tv)$) | Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3\|§31.3]] (differentials by curves) | both compute the differential along curves |
| Definition [[§7 The Regular Value Theorem#^def-7-2\|§7.2]] (rank of a matrix) | Definition [[§30 The Differential in Coordinates#^def-30-1\|§30.1]] (rank of $F_{\ast p}$) | the rank of the Jacobian of any coordinate representation |
| the chain rule for Jacobians | Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6\|§28.6]]; Corollary [[§30 The Differential in Coordinates#^cor-30-3\|§30.3]] | $(G \circ F)_{\ast p} = G_{*F(p)} \circ F_{\ast p}$ is matrix multiplication in coordinates |
| $\mathbb{R}^n$ is its own tangent space | Corollary [[§30 The Differential in Coordinates#^cor-30-6\|§30.6]]; Proposition [[§30 The Differential in Coordinates#^prop-30-5\|§30.5]] | on open subsets of vector spaces $F_{\ast p}$ is the ordinary derivative |

![[§7 The Regular Value Theorem#^def-7-1]]

![[§28 Derivations and the Abstract Tangent Space#^def-28-5]]

![[§28 Derivations and the Abstract Tangent Space#^def-28-6]]

![[§30 The Differential in Coordinates#^thm-30-2]]

The two differentials are built in opposite directions. The Jacobian is computed from $F$ directly: differentiate the components. The pushforward is defined by duality: to see how $F_{\ast p}D$ differentiates a function $g$ near $F(p)$, pull $g$ back to $g \circ F$ and let $D$ differentiate that. In coordinates the result is the same matrix (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]), and on open subsets of Euclidean space the pushforward is the ordinary derivative (Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]).

## Covectors: Gradients, Transposes and Pullbacks

| Geometric | Abstract | How they correspond |
|---|---|---|
| the gradient $\nabla f(p)$, a row of the Jacobian | Definition [[§32 The Cotangent Space#^def-32-2\|§32.2]] ($df_p \in T_p^*M$); Lemma [[§32 The Cotangent Space#^lem-32-2\|§32.2]] | the remark [[§32 The Cotangent Space#^rem-32-2\|Differential — Not Gradient]]: a gradient needs an inner product |
| the transpose $J_F^{\mathsf T}$ of the Jacobian | Definition [[§32 The Cotangent Space#^def-32-5\|§32.5]] (pullback of covectors, the dual map of $F_{\ast p}$) | in dual bases the matrix of $F_p^{\ast}$ is the transpose of the matrix of $F_{\ast p}$ |
| $\nabla(f \circ F) = J_F^{\mathsf T} \nabla f$ (chain rule) | Proposition [[§32 The Cotangent Space#^prop-32-10\|§32.10]] ($F_p^{\ast}\, df = d(f \circ F)$) | the remark [[§32 The Cotangent Space#^rem-32-6\|The Two Differentials Meet]] |
| normal vectors, spanned by $\nabla F^1, \ldots, \nabla F^k$ | Definition [[§35 Regular Submanifolds#^def-35-3\|§35.3]] (conormal space); Proposition [[§35 Regular Submanifolds#^prop-35-5\|§35.5]] (basis $dF^i|_p$) | the remark [[§35 Regular Submanifolds#^rem-35-1\|No Normal Vectors Without a Metric]] |

![[§32 The Cotangent Space#^def-32-2]]

![[§32 The Cotangent Space#^def-32-5]]

![[§32 The Cotangent Space#^prop-32-10]]

![[§32 The Cotangent Space#^rem-32-6]]

![[§35 Regular Submanifolds#^def-35-3]]

In $\mathbb{R}^n$ the dot product identifies covectors with vectors, so the differential $df_p$ appears as the gradient, a pulled-back covector as the transpose of the Jacobian applied to a gradient, and a conormal covector $dF^i|_p$ as the normal vector $\nabla F^i(p)$. An abstract manifold has no dot product, so the covector versions are the intrinsic ones; an inner product on each tangent space — a metric — would turn them back into vectors.

## Regular Points, Regular Values and the Theorems Behind Them

| Geometric | Abstract | How they correspond |
|---|---|---|
| Definition [[§7 The Regular Value Theorem#^def-7-3\|§7.3]] ($DF_p$ surjective) | Definition [[§30 The Differential in Coordinates#^def-30-2\|§30.2]], Definition [[§34 Submersions#^def-34-3\|§34.3]] ($F_{\ast p}$ surjective) | Proposition [[§30 The Differential in Coordinates#^prop-30-7\|§30.7]]: regular for $F$ iff for its coordinate representation |
| Definition [[§7 The Regular Value Theorem#^def-7-4\|§7.4]] (every point of $F^{-1}(c)$ regular) | Definition [[§30 The Differential in Coordinates#^def-30-3\|§30.3]], Definition [[§34 Submersions#^def-34-4\|§34.4]] | the same condition, read through charts; Corollary [[§22 The Differential of a Map Between Vector Spaces#^cor-22-4\|§22.4]] without coordinates |
| Theorem [[§7 The Regular Value Theorem#^thm-7-1\|§7.1]] (implicit function theorem) | Theorem [[§34 Submersions#^thm-34-4\|§34.4]] (local normal form for submersions) | the normal form is the implicit function theorem in charts |
| Theorem [[§7 The Regular Value Theorem#^thm-7-3\|§7.3]] (a regular level set is a topological manifold) | Corollary [[§30 The Differential in Coordinates#^cor-30-8\|§30.8]] (the same for $F : M \to N$) | proved through Proposition [[§30 The Differential in Coordinates#^prop-30-7\|§30.7]] |
| Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2\|§20.2]] (a regular level set is a smooth manifold) | Theorem [[§35 Regular Submanifolds#^thm-35-7\|§35.7]] (a regular level set is a submanifold) | Proposition [[§35 Regular Submanifolds#^prop-35-9\|§35.9]]: the same structure and tangent spaces |
| Corollary [[§7 The Regular Value Theorem#^cor-7-4\|§7.4]] (open domains, arbitrary values) | Corollary [[§35 Regular Submanifolds#^cor-35-8\|§35.8]] (fibres of submersions) | every value of a submersion is regular |
| Theorem [[§26 Transversality#^thm-26-1\|§26.1]], Corollary [[§26 Transversality#^cor-26-3\|§26.3]] (transversality) | (no manifold version yet) | the regular value theorem is the case of a point |

![[§7 The Regular Value Theorem#^def-7-3]]

![[§30 The Differential in Coordinates#^def-30-2]]

![[§7 The Regular Value Theorem#^def-7-4]]

![[§30 The Differential in Coordinates#^def-30-3]]

![[§7 The Regular Value Theorem#^thm-7-1]]

![[§34 Submersions#^thm-34-4]]

![[§7 The Regular Value Theorem#^thm-7-3]]

![[§35 Regular Submanifolds#^thm-35-7]]

The pattern is the one of the whole course: a definition is transplanted by replacing the Jacobian $DF_p$ with the pushforward $F_{\ast p}$, and a theorem is proved by reading it in charts, where it becomes the Euclidean one. Proposition [[§30 The Differential in Coordinates#^prop-30-7|§30.7]] is the bridge for regular points — a point is regular for $F$ exactly when it is regular for the coordinate representation, because the matrix of $F_{\ast p}$ is that Jacobian. The local normal form for submersions plays the role of the implicit function theorem, and it upgrades the conclusion from “topological manifold” to “submanifold” with its tangent space. The remark *The Regular Value Theorems — Old and New* ([[§35 Regular Submanifolds|§35]]) lists all five versions with their roles.

## The Global Picture: Embeddings

A geometric manifold sits in $\mathbb{R}^N$ by construction; an abstract one need not sit anywhere. The bridge is an embedding:

![[§38 Embeddings#^def-38-1]]

The image of an embedding is a submanifold (Theorem [[§38 Embeddings#^thm-38-1|§38.1]]), so an abstract manifold with an embedding into $\mathbb{R}^N$ is diffeomorphic to a geometric one, and all the comparisons above apply to it. The internal description of Definition [[§20 Manifolds in Euclidean Space#^def-20-2|§20.2]] is exactly a local embedding: an injective immersion that is a homeomorphism onto its image. Injective immersions alone are not enough: their images are immersed submanifolds (Definition [[§38 Embeddings#^def-38-4|§38.4]], Proposition [[§38 Embeddings#^prop-38-12|§38.12]]), regular exactly when the immersion is an embedding (Proposition [[§38 Embeddings#^prop-38-14|§38.14]]); the figure-eight and the irrational line on the torus are immersed but not regular (Example [[§38 Embeddings#^ex-38-1|§38.1]]).

> [!remark] Remark: Whitney's Embedding Theorem
> *(Not from lecture; stated, not proved, in these notes.)* Every smooth $m$-manifold — Hausdorff and second countable, as in Definition [[§17 Differentiable Structures#^def-17-9|§17.9]] — admits a smooth embedding into $\mathbb{R}^{2m+1}$ (Lee, Theorem 6.15), and Whitney improved the dimension to $2m$. So no manifold is out of reach of the geometric picture: every abstract manifold is diffeomorphic to a submanifold of some Euclidean space. The abstract definition is still the right one, because the embedding is not part of the manifold: the same manifold has many embeddings, none of them preferred, and quotients such as $\mathbb{CP}^n$ come with none.

^rem-39-1

## What Each Picture Gives

The geometric picture gives computations: a tangent space is a kernel, a differential is a Jacobian, a normal vector is a gradient, and all of it can be drawn. The abstract picture gives intrinsic definitions: the tangent space of $\mathbb{CP}^n$ or of $G/H$ makes sense without choosing where to put them, and every notion is independent of an embedding — which is why the bundles, fields and forms of the next chapters are built on the abstract side. The bridges in the table are what let the course compute in the geometric picture and conclude in the abstract one.
