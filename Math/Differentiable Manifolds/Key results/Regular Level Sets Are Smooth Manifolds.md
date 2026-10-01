---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 9.2", "Lee Example 1.32", "Lee Corollary 5.14"]
tags: [differentiable-manifolds, hub]
---
![[§9 Manifolds in Euclidean Space#^prop-9-2]]

## Treated in
- [[§9 Manifolds in Euclidean Space#^prop-9-2|Proposition §9.2: Regular Level Sets Are Smooth Manifolds]], in [[§9 Manifolds in Euclidean Space]]

## Its proof uses
- [[§4 The Regular Value Theorem#^thm-4-1|Theorem §4.1: Implicit Function Theorem — Lee Theorem C.40]]
- [[§4 The Regular Value Theorem#^thm-4-3|Theorem §4.3: Regular Value Theorem]]
- [[§8 Differentiable Structures#^def-8-4|Definition §8.4: Smoothly Compatible Charts]]
- [[§8 Differentiable Structures#^thm-8-5|Theorem §8.5: Every Atlas Lies in a Unique Maximal Atlas]]
- [[§9 Manifolds in Euclidean Space#^ex-9-2|Example §9.2: A Surface in ℝ³]]
- [[§9 Manifolds in Euclidean Space#^def-9-2|Definition §9.2: Parametrization]]

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§9 Manifolds in Euclidean Space#^ex-9-2|Example §9.2: A Surface in ℝ³]]
- [[§9 Manifolds in Euclidean Space#^lem-9-3|Lemma §9.3: Smooth Maps into and out of Regular Level Sets]]
- [[§9 Manifolds in Euclidean Space#^prop-9-4|Proposition §9.4: The Three Circle Atlases Define One Smooth Structure]]
- [[§10 Vector Spaces and Matrix Groups#^ex-10-1|Example §10.1: O(n) Is a Smooth Manifold of Dimension n(n-1)/2]]
- [[§10 Vector Spaces and Matrix Groups#^ex-10-2|Example §10.2: U(n) Is a Smooth Manifold of Dimension n²]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5|Theorem §11.5: The Classical Groups]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-7|Theorem §11.7: Preimages of Transverse Level Sets]]
- [[§15 Submanifolds#^prop-15-8|Proposition §15.8: The Old and New Versions Agree]]

## Connections
- **Used for.** Smooth structures on O(n) and U(n) ([[§10 Vector Spaces and Matrix Groups#^ex-10-1|Ex. §10.1]], [[§10 Vector Spaces and Matrix Groups#^ex-10-2|Ex. §10.2]]), on SL(n,ℝ) and on the spheres, hence the smooth half of [[Classical Groups Are Manifolds]] ([[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5|§11.5]]). Maps into and out of a level set are smooth when the ambient formulas are ([[§9 Manifolds in Euclidean Space#^lem-9-3|§9.3]]), which shows that the three circle atlases define one structure ([[§9 Manifolds in Euclidean Space#^prop-9-4|§9.4]]).
- **Why it works.** A transition map between two graph charts factors through the ambient space, a parametrization up and a linear projection down ([[§9 Manifolds in Euclidean Space#^ex-9-2|Ex. §9.2]]). This needs the implicit functions to be smooth; the topological [[Regular Value Theorem (Euclidean)]] only needed them continuous ([[§9 Manifolds in Euclidean Space#^rem-9-3|§9, Remark]]).
- **Same idea elsewhere.** 452 solves the circle for y near (0, 1) ([[§12 The Implicit Function Theorem#^ex-12-1|452 Ex. §12.1]]) and for x near (1, 0) ([[§12 The Implicit Function Theorem#^ex-12-2|452 Ex. §12.2]]); the proposition says that such graph charts over different variables are smoothly compatible. At a critical value the conclusion fails: x² + y² = 0 is a single point, not a curve ([[§4 The Regular Value Theorem#^ex-4-1|Ex. §4.1]]).
- **Looking ahead (not yet announced in the course).** Whitney's embedding theorem puts every abstract manifold in some ℝᴺ, which is what an external description of it needs.
