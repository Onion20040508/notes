---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 16.2", "Lee Example 1.32", "Lee Corollary 5.14"]
tags: [differentiable-manifolds, hub]
---
![[§16 Manifolds in Euclidean Space#^prop-16-2]]

## Treated in
- [[§16 Manifolds in Euclidean Space#^prop-16-2|Proposition §16.2: Regular Level Sets Are Smooth Manifolds]], in [[§16 Manifolds in Euclidean Space]]

## Its proof uses
- [[§7 The Regular Value Theorem#^thm-7-1|Theorem §7.1: Implicit Function Theorem — Lee Theorem C.40]]
- [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3: Regular Value Theorem]]
- [[§13 Differentiable Structures#^def-13-4|Definition §13.4: Smoothly Compatible Charts]]
- [[§13 Differentiable Structures#^thm-13-5|Theorem §13.5: Every Atlas Lies in a Unique Maximal Atlas]]
- [[§16 Manifolds in Euclidean Space#^ex-16-2|Example §16.2: A Surface in ℝ³]]
- [[§16 Manifolds in Euclidean Space#^def-16-2|Definition §16.2: Parametrization]]

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§16 Manifolds in Euclidean Space#^ex-16-2|Example §16.2: A Surface in ℝ³]]
- [[§16 Manifolds in Euclidean Space#^lem-16-3|Lemma §16.3: Smooth Maps into and out of Regular Level Sets]]
- [[§16 Manifolds in Euclidean Space#^prop-16-4|Proposition §16.4: The Three Circle Atlases Define One Smooth Structure]]
- [[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-19-1|Example §19.1: O(n) Is a Smooth Manifold of Dimension n(n-1)/2]]
- [[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-19-2|Example §19.2: U(n) Is a Smooth Manifold of Dimension n²]]
- [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5|Theorem §20.5: The Classical Groups]]
- [[§21 Transversality#^thm-21-1|Theorem §21.1: Preimages of Transverse Level Sets]]
- [[§29 Submanifolds#^prop-29-8|Proposition §29.8: The Old and New Versions Agree]]

## Connections
- **Used for.** Smooth structures on O(n) and U(n) ([[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-19-1|Ex. §19.1]], [[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-19-2|Ex. §19.2]]), on SL(n,ℝ) and on the spheres, hence the smooth half of [[Classical Groups Are Manifolds]] ([[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5|§20.5]]). Maps into and out of a level set are smooth when the ambient formulas are ([[§16 Manifolds in Euclidean Space#^lem-16-3|§16.3]]), which shows that the three circle atlases define one structure ([[§16 Manifolds in Euclidean Space#^prop-16-4|§16.4]]).
- **Why it works.** A transition map between two graph charts factors through the ambient space, a parametrization up and a linear projection down ([[§16 Manifolds in Euclidean Space#^ex-16-2|Ex. §16.2]]). This needs the implicit functions to be smooth; the topological [[Regular Value Theorem (Euclidean)]] only needed them continuous ([[§16 Manifolds in Euclidean Space#^rem-16-3|§16, Remark]]).
- **Same idea elsewhere.** 452 solves the circle for y near (0, 1) ([[§12 The Implicit Function Theorem#^ex-12-1|452 Ex. §12.1]]) and for x near (1, 0) ([[§12 The Implicit Function Theorem#^ex-12-2|452 Ex. §12.2]]); the proposition says that such graph charts over different variables are smoothly compatible. At a critical value the conclusion fails: x² + y² = 0 is a single point, not a curve ([[§7 The Regular Value Theorem#^ex-7-1|Ex. §7.1]]).
- **Looking ahead (not yet announced in the course).** Whitney's embedding theorem puts every abstract manifold in some ℝᴺ, which is what an external description of it needs.
