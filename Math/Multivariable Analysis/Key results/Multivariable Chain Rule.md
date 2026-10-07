---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 12.2", "chain rule in several variables"]
tags: [multivariable-analysis, hub]
---
![[§12 Composition of Functions and the Chain Rule#^thm-12-2]]

## Treated in
- [[§12 Composition of Functions and the Chain Rule#^thm-12-2|Theorem §12.2: Multivariable Chain Rule]], in [[§12 Composition of Functions and the Chain Rule]]

## Its proof uses
- [[§3 Continuity and Limits of Functions#^def-3-1|Definition §3.1: Continuity]]
- [[§3 Continuity and Limits of Functions#^thm-3-1|Theorem §3.1: Sum and Difference of Continuous Functions]]
- [[§3 Continuity and Limits of Functions#^thm-3-2|Theorem §3.2: Product of Continuous Functions]]
- [[§5 Partial Derivatives#^def-5-1|Definition §5.1: Partial Derivatives]]
- [[§7 Differentiability#^thm-7-2|Theorem §7.2: Continuous Partials Imply Differentiability]]
- [[§12 Composition of Functions and the Chain Rule#^thm-12-1|Theorem §12.1: Continuity of Composition]]

## Its proof uses (other subjects)
- [[Mean Value Theorem]] (Single Variable Analysis)

## Used in (Multivariable Analysis)
- [[§16 The Inverse Function Theorem#^thm-16-2|Theorem §16.2: Inverse Function Theorem]]
- [[§17 Optimization and Lagrange Multipliers#^thm-17-2|Theorem §17.2: Method of Lagrange Multipliers]]
- [[§17 Optimization and Lagrange Multipliers#^thm-17-3|Theorem §17.3: Lagrange Multipliers with Multiple Constraints]]
- [[§24 The Change of Variables Formula#^thm-24-2|Theorem §24.2: Change of Variables Formula — Rectangular Case]]
- [[§29 Conservation of Mass and Laplace's Equation#^thm-29-2|Theorem §29.2: Fundamental Solution of the 2D Laplacian]]
- [[§34 Stokes' Theorem in ℝ³#^thm-34-1|Theorem §34.1: Stokes' Theorem]]
- [[§39 Closed and Exact Forms#^prop-39-6|Proposition §39.6: A Closed Form That Is Not Exact]]

## Used in (Differentiable Manifolds)
- [[§7 The Regular Value Theorem#^def-7-1|Definition §7.1: Jacobian Matrix]]
- [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3: Regular Value Theorem]]
- [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|Proposition §12.1: Derivative of the Determinant]]
- [[§12 The Classical Groups Are Topological Manifolds#^rem-12-1|Remark: The Method: Level Sets and the Implicit Function Theorem]]
- [[§12 The Classical Groups Are Topological Manifolds#^cor-12-5|Corollary §12.5: SL(n,ℝ) Is a Manifold of Dimension n² − 1]]
- [[§17 Differentiable Structures#^thm-17-1|Theorem §17.1: Compatibility Means the Two Notions Agree]]
- [[§17 Differentiable Structures#^thm-17-5|Theorem §17.5: Every Atlas Lies in a Unique Maximal Atlas]]
- [[§19 Smooth Functions and Smooth Maps#^ex-19-1|Example §19.1: Two Smooth Structures on the Real Line]]
- [[§19 Smooth Functions and Smooth Maps#^prop-19-1|Proposition §19.1: Some Chart Suffices — Every Chart Then Works]]
- [[§19 Smooth Functions and Smooth Maps#^prop-19-2|Proposition §19.2: Smoothness of a Map Does Not Depend on the Charts]]
- [[§19 Smooth Functions and Smooth Maps#^prop-19-3|Proposition §19.3: The Two Notions of Diffeomorphism Agree]]
- [[§19 Smooth Functions and Smooth Maps#^lem-19-4|Lemma §19.4: Composition of Smooth Maps]]
- [[§20 Manifolds in Euclidean Space#^thm-20-1|Theorem §20.1: The Two Descriptions Agree]]
- [[§20 Manifolds in Euclidean Space#^prop-20-2|Proposition §20.2: Regular Level Sets Are Smooth Manifolds]]
- [[§20 Manifolds in Euclidean Space#^lem-20-3|Lemma §20.3: Smooth Maps into and out of Regular Level Sets]]
- [[§22 The Differential of a Map Between Vector Spaces#^lem-22-1|Lemma §22.1: Independence of Coordinates]]
- [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|Theorem §22.3: Coordinate-Free Formula for the Differential]]
- [[§24 The Circle#^prop-24-1|Proposition §24.1: The Three Circle Atlases Define One Smooth Structure]]
- [[§25 The Geometric Tangent Space#^lem-25-2|Lemma §25.2: The Geometric Tangent Space of a Graph]]
- [[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§25 The Geometric Tangent Space#^def-25-4|Definition §25.4: The Directional Derivative Attached to a Tangent Vector]]
- [[§25 The Geometric Tangent Space#^cor-25-4|Corollary §25.4: Three Descriptions of the Geometric Tangent Space]]
- [[§25 The Geometric Tangent Space#^prop-25-8|Proposition §25.8: Basic Properties of D_v]]
- [[§26 Transversality#^thm-26-1|Theorem §26.1: Preimages of Transverse Level Sets]]
- [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-2|Lemma §29.2: Hadamard's Lemma]]
- [[§30 The Differential in Coordinates#^cor-30-3|Corollary §30.3: The Chain Rule in Coordinates]]
- [[§30 The Differential in Coordinates#^prop-30-5|Proposition §30.5: Agreement with the Vector-Space Differential]]
- [[§35 Submanifolds#^prop-35-8|Proposition §35.8: The Old and New Versions Agree]]
- [[§45 The Cotangent Bundle#^prop-45-2|Proposition §45.2: The Smooth Atlas of T^*M]]

## Connections
- **Proof idea.** Split the increment of g into single-variable increments and apply the one-variable [[Mean Value Theorem]]. Continuity of the partials controls the intermediate points. The 451 version is the [[§28 Basic Properties of the Derivative#^thm-28-3|Chain Rule]] (§28.3). Under differentiability alone, see [[§8 Algebra of Differentiable Functions#^thm-8-7|Theorem §8.7]].
- **Linear algebra.** In matrix form, Dg = Df · D(φ, ψ) ([[§12 Composition of Functions and the Chain Rule#^rem-12-2|Matrix Form]]): the derivative of a composition is the composition of the derivatives, and its matrix is the product of the matrices ([[§9 Matrices#^ladr-3-43|LADR 3.43]]). Since determinants are multiplicative ([[§37 Determinants#^ladr-9-49|LADR 9.49]]), a map and its inverse have [[§16 The Inverse Function Theorem#^rem-16-6|reciprocal Jacobians]].
- **Used for.** It is the engine of the [[Inverse Function Theorem (several variables)]] and the [[Method of Lagrange Multipliers]], and it appears in the [[§24 The Change of Variables Formula#^thm-24-2|rectangular change of variables]]. It also underlies [[§37 The Algebra of Differential Forms#^def-37-3|pullback]] and the reduction of [[Stokes' Theorem in ℝ³]] to the parameter domain.
- **On manifolds.** The coordinate-free statement (G ∘ F)_* = G_* ∘ F_* is [[Chain Rule for Differentials]] (591 Thm. §26.6); in coordinates it reduces to this theorem, [[§30 The Differential in Coordinates#^cor-30-3|591 Cor. §30.3]].
- **Also in [[Calculus]]:** [[§110 The Chain Rule#^thm-110-2|Calc Thm. §110.2]] and [[§110 The Chain Rule#^thm-110-3|Calc Thm. §110.3]] (computational treatment with worked examples).
