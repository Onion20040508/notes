---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 12.11", "chain rule on manifolds", "pushforward functoriality", "Lee Proposition 3.6"]
tags: [differentiable-manifolds, hub]
---
![[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-11]]

## Treated in
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-11|Theorem §12.11: The Chain Rule]], in [[§12 Tangent Spaces II꞉ The Abstract Tangent Space]]

## Its proof uses
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-9|Definition §12.9: Pullback of Germs]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-10|Definition §12.10: Pushforward — the Differential]]

## Used in (Differentiable Manifolds)
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-12|Corollary §12.12: Diffeomorphisms Induce Isomorphisms]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-23|Corollary §12.23: The Chain Rule in Coordinates]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-24|Corollary §12.24: Change of Coordinates]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-31|Corollary §12.31: Velocity of a Composite — Computing Differentials by Curves]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-32|Theorem §12.32: The Tangent Space of a Product]]
- [[§14 Local Diffeomorphisms and Submersions#^thm-14-2|Theorem §14.2: Local Diffeomorphisms Are Detected by the Differential]]
- [[§15 Submanifolds#^thm-15-6|Theorem §15.6: The Regular Value Theorem for Manifolds]]
- [[§16 Fibrations#^prop-16-1|Proposition §16.1: Fibres and Fibrations]]

## Connections
- **Used for.** Diffeomorphisms induce isomorphisms of tangent spaces ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-12|§12.12]]), so a chart identifies T_pM with a tangent space of an open subset of ℝⁿ ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-14|§12.14]]); this is how the [[Basis Theorem for Tangent Spaces]] is proved. It also gives the chain rule and the change of coordinates in matrices ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-23|§12.23]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-24|§12.24]]), differentials computed by curves ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-31|§12.31]]) and the [[Local Diffeomorphism Criterion]].
- **Why the proof is one line.** Pulling back germs reverses the order, (G ∘ F)* = F* ∘ G*. The differential is the dual of pullback, so it composes in the same order as the maps, as dual maps do in linear algebra, (ST)′ = T′S′ ([[§12 Duality#^ladr-3-120|LADR 3.120]]).
- **Same idea elsewhere.** In coordinates it is the [[Multivariable Chain Rule]] of 452: the Jacobian of a composite is the product of the Jacobians ([[§9 Matrices#^ladr-3-43|LADR 3.43]]). In 590, induced homomorphisms on π₁ compose the same way ([[Functoriality of π₁]]). Together with the basis theorem it shows that diffeomorphic manifolds have the same dimension, the easy smooth counterpart of [[Topological Invariance of Dimension]].
- **Coming later in the course.** Differential forms pull back along smooth maps with the same reversal of order, (G ∘ F)* = F* ∘ G*.
