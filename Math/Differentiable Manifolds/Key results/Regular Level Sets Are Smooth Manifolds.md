---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 20.2", "Lee Example 1.32", "Lee Corollary 5.14"]
tags: [differentiable-manifolds, hub]
---
![[§20 Manifolds in Euclidean Space#^prop-20-2]]

## Treated in
- [[§20 Manifolds in Euclidean Space#^prop-20-2|Proposition §20.2: Regular Level Sets Are Smooth Manifolds]], in [[§20 Manifolds in Euclidean Space]]

## Its proof uses
- [[§2 Topological Manifolds#^def-2-3|Definition §2.3: Chart]]
- [[§7 The Regular Value Theorem#^thm-7-1|Theorem §7.1: Implicit Function Theorem — Lee Theorem C.40]]
- [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3: Regular Value Theorem]]
- [[§7 The Regular Value Theorem#^cor-7-4|Corollary §7.4: Open Domains and Arbitrary Values]]
- [[§17 Differentiable Structures#^def-17-3|Definition §17.3: Diffeomorphism of Open Subsets of Euclidean Space]]
- [[§17 Differentiable Structures#^def-17-4|Definition §17.4: Smoothly Compatible Charts]]
- [[§17 Differentiable Structures#^thm-17-5|Theorem §17.5: Every Atlas Lies in a Unique Maximal Atlas]]
- [[§17 Differentiable Structures#^def-17-6|Definition §17.6: Atlas]]
- [[§17 Differentiable Structures#^def-17-9|Definition §17.9: Smooth Manifold Structure]]
- [[§20 Manifolds in Euclidean Space#^ex-20-1|Example §20.1: A Surface in ℝ³]]
- [[§20 Manifolds in Euclidean Space#^def-20-3|Definition §20.3: Parametrization]]

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§20 Manifolds in Euclidean Space#^lem-20-3|Lemma §20.3: Smooth Maps into and out of Regular Level Sets]]
- [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|Example §23.1: O(n) Is a Smooth Manifold of Dimension n(n-1)/2]]
- [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|Example §23.2: U(n) Is a Smooth Manifold of Dimension n²]]
- [[§24 The Circle#^prop-24-1|Proposition §24.1: The Three Circle Atlases Define One Smooth Structure]]
- [[§25 The Geometric Tangent Space#^thm-25-5|Theorem §25.5: The Classical Groups]]
- [[§26 Transversality#^thm-26-1|Theorem §26.1: Preimages of Transverse Level Sets]]
- [[§26 Transversality#^prop-26-4|Proposition §26.4: Transverse Intersections]]
- [[§35 Local Diffeomorphisms#^ex-35-1|Example §35.1: The Circle Covered by a Line]]
- [[§37 Regular Submanifolds#^prop-37-11|Proposition §37.11: The Old and New Versions Agree]]
- [[§43 Projective Spaces and the Hopf Fibration#^ex-43-1|Example §43.1: Spheres Cover Projective Spaces]]
- [[§43 Projective Spaces and the Hopf Fibration#^ex-43-3|Example §43.3: The Hopf Fibration S²ⁿ⁺¹ → ℂPⁿ]]

## Connections
- **Used for.** Smooth structures on O(n) and U(n) ([[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|Ex. §23.1]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|Ex. §23.2]]), on SL(n,ℝ) and on the spheres, hence the smooth half of [[Classical Groups Are Manifolds]] ([[§25 The Geometric Tangent Space#^thm-25-5|§25.5]]). Maps into and out of a level set are smooth when the ambient formulas are ([[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]]), which shows that the three circle atlases define one structure ([[§24 The Circle#^prop-24-1|§24.1]]).
- **Why it works.** A transition map between two graph charts factors through the ambient space, a parametrization up and a linear projection down ([[§20 Manifolds in Euclidean Space#^ex-20-1|Ex. §20.1]]). This needs the implicit functions to be smooth; the topological [[Regular Value Theorem (Euclidean)]] only needed them continuous ([[§20 Manifolds in Euclidean Space#^rem-20-3|§20, Remark]]).
- **Same idea elsewhere.** 452 solves the circle for y near (0, 1) ([[§15 The Implicit Function Theorem#^ex-15-1|452 Ex. §15.1]]) and for x near (1, 0) ([[§15 The Implicit Function Theorem#^ex-15-2|452 Ex. §15.2]]); the proposition says that such graph charts over different variables are smoothly compatible. At a critical value the conclusion fails: x² + y² = 0 is a single point, not a curve ([[§7 The Regular Value Theorem#^ex-7-1|Ex. §7.1]]).
- **Looking ahead (not yet announced in the course).** Whitney's embedding theorem puts every abstract manifold in some ℝᴺ, which is what an external description of it needs.
