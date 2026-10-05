---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 19.2", "Lee Example 1.32", "Lee Corollary 5.14"]
tags: [differentiable-manifolds, hub]
---
![[§19 Manifolds in Euclidean Space#^prop-19-2]]

## Treated in
- [[§19 Manifolds in Euclidean Space#^prop-19-2|Proposition §19.2: Regular Level Sets Are Smooth Manifolds]], in [[§19 Manifolds in Euclidean Space]]

## Its proof uses
- [[§7 The Regular Value Theorem#^thm-7-1|Theorem §7.1: Implicit Function Theorem — Lee Theorem C.40]]
- [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3: Regular Value Theorem]]
- [[§16 Differentiable Structures#^def-16-4|Definition §16.4: Smoothly Compatible Charts]]
- [[§16 Differentiable Structures#^thm-16-5|Theorem §16.5: Every Atlas Lies in a Unique Maximal Atlas]]
- [[§19 Manifolds in Euclidean Space#^ex-19-2|Example §19.2: A Surface in ℝ³]]
- [[§19 Manifolds in Euclidean Space#^def-19-2|Definition §19.2: Parametrization]]

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§19 Manifolds in Euclidean Space#^ex-19-2|Example §19.2: A Surface in ℝ³]]
- [[§19 Manifolds in Euclidean Space#^lem-19-3|Lemma §19.3: Smooth Maps into and out of Regular Level Sets]]
- [[§19 Manifolds in Euclidean Space#^prop-19-4|Proposition §19.4: The Three Circle Atlases Define One Smooth Structure]]
- [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-1|Example §22.1: O(n) Is a Smooth Manifold of Dimension n(n-1)/2]]
- [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-2|Example §22.2: U(n) Is a Smooth Manifold of Dimension n²]]
- [[§23 The Geometric Tangent Space#^thm-23-5|Theorem §23.5: The Classical Groups]]
- [[§24 Transversality#^thm-24-1|Theorem §24.1: Preimages of Transverse Level Sets]]
- [[§33 Submanifolds#^prop-33-8|Proposition §33.8: The Old and New Versions Agree]]

## Connections
- **Used for.** Smooth structures on O(n) and U(n) ([[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-1|Ex. §22.1]], [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-2|Ex. §22.2]]), on SL(n,ℝ) and on the spheres, hence the smooth half of [[Classical Groups Are Manifolds]] ([[§23 The Geometric Tangent Space#^thm-23-5|§23.5]]). Maps into and out of a level set are smooth when the ambient formulas are ([[§19 Manifolds in Euclidean Space#^lem-19-3|§19.3]]), which shows that the three circle atlases define one structure ([[§19 Manifolds in Euclidean Space#^prop-19-4|§19.4]]).
- **Why it works.** A transition map between two graph charts factors through the ambient space, a parametrization up and a linear projection down ([[§19 Manifolds in Euclidean Space#^ex-19-2|Ex. §19.2]]). This needs the implicit functions to be smooth; the topological [[Regular Value Theorem (Euclidean)]] only needed them continuous ([[§19 Manifolds in Euclidean Space#^rem-19-3|§19, Remark]]).
- **Same idea elsewhere.** 452 solves the circle for y near (0, 1) ([[§12 The Implicit Function Theorem#^ex-12-1|452 Ex. §12.1]]) and for x near (1, 0) ([[§12 The Implicit Function Theorem#^ex-12-2|452 Ex. §12.2]]); the proposition says that such graph charts over different variables are smoothly compatible. At a critical value the conclusion fails: x² + y² = 0 is a single point, not a curve ([[§7 The Regular Value Theorem#^ex-7-1|Ex. §7.1]]).
- **Looking ahead (not yet announced in the course).** Whitney's embedding theorem puts every abstract manifold in some ℝᴺ, which is what an external description of it needs.
