---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 2.1", "invariance of domain consequence", "Lee Theorem 1.2"]
tags: [differentiable-manifolds, hub]
---
![[§2 Topological Manifolds#^thm-2-1]]

## Treated in
- [[§2 Topological Manifolds#^thm-2-1|Theorem §2.1: Topological Invariance of Dimension]], in [[§2 Topological Manifolds]]

## Its proof uses
- (only definitions)

## Used in (Differentiable Manifolds)
- [[§2 Topological Manifolds#^cor-2-2|Corollary §2.2: Dimension is Locally Constant]]

## Connections
- **Used for.** The dimension of a nonempty manifold is well defined, and if it is allowed to vary with the point it is constant on components ([[§2 Topological Manifolds#^cor-2-2|§2.2]]). It shows that ℝ_disc × ℝ, which as a set is the plane, is not homeomorphic to ℝ² ([[§2 Topological Manifolds#^rem-2-7|A Warning]]). The related invariance of domain makes openness of chart images automatic ([[§13 Differentiable Structures#^rem-13-2|§13, Remark]]).
- **Why it is hard.** No differentiability is assumed, so the linear-algebra argument ([[Dimension shows whether vector spaces are isomorphic]], LADR 3.70) does not apply. In 590, ℝ ≇ ℝ² because removing a point disconnects ℝ, and ℝ² ≇ ℝ³ because the punctured spaces have different π₁ ([[§23 The Fundamental Group#^rem-23-2|590 §23, Remark]]).
- **The smooth version is easy.** A diffeomorphism induces linear isomorphisms of tangent spaces ([[Chain Rule for Differentials]], [[§23 Derivations and the Abstract Tangent Space#^cor-23-7|§23.7]]), and dim T_pM = n ([[Basis Theorem for Tangent Spaces]]), so diffeomorphic open subsets of ℝⁿ and ℝᵐ have n = m.
- **Coming later in the course.** de Rham cohomology is the tool Lee uses to prove the theorem (Theorem 17.26).
