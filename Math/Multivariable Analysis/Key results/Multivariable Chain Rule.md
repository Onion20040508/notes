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
- [[§7 The Regular Value Theorem#^def-7-1|Definition §7.1: Jacobian and Rank]]
- [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3: Regular Value Theorem]]
- [[§11 The Classical Groups Are Topological Manifolds#^rem-11-1|Remark: The Method: Level Sets and the Implicit Function Theorem]]
- [[§11 The Classical Groups Are Topological Manifolds#^prop-11-1|Proposition §11.1: Derivative of the Determinant]]
- [[§11 The Classical Groups Are Topological Manifolds#^cor-11-5|Corollary §11.5: SL(n,ℝ) Is a Manifold of Dimension n² − 1]]
- [[§16 Differentiable Structures#^thm-16-1|Theorem §16.1: Compatibility Means the Two Notions Agree]]
- [[§16 Differentiable Structures#^thm-16-5|Theorem §16.5: Every Atlas Lies in a Unique Maximal Atlas]]
- [[§18 Smooth Functions and Smooth Maps#^ex-18-1|Example §18.1: Two Smooth Structures on the Real Line]]
- [[§18 Smooth Functions and Smooth Maps#^prop-18-1|Proposition §18.1: Some Chart Suffices — Every Chart Then Works]]
- [[§18 Smooth Functions and Smooth Maps#^prop-18-2|Proposition §18.2: Smoothness of a Map Does Not Depend on the Charts]]
- [[§18 Smooth Functions and Smooth Maps#^prop-18-3|Proposition §18.3: The Two Notions of Diffeomorphism Agree]]
- [[§18 Smooth Functions and Smooth Maps#^lem-18-4|Lemma §18.4: Composition of Smooth Maps]]
- [[§19 Manifolds in Euclidean Space#^thm-19-1|Theorem §19.1: The Two Descriptions Agree]]
- [[§19 Manifolds in Euclidean Space#^prop-19-2|Proposition §19.2: Regular Level Sets Are Smooth Manifolds]]
- [[§19 Manifolds in Euclidean Space#^lem-19-3|Lemma §19.3: Smooth Maps into and out of Regular Level Sets]]
- [[§19 Manifolds in Euclidean Space#^prop-19-4|Proposition §19.4: The Three Circle Atlases Define One Smooth Structure]]
- [[§21 The Differential of a Map Between Vector Spaces#^lem-21-1|Lemma §21.1: Independence of Coordinates]]
- [[§21 The Differential of a Map Between Vector Spaces#^thm-21-3|Theorem §21.3: Coordinate-Free Formula for the Differential]]
- [[§23 The Geometric Tangent Space#^lem-23-2|Lemma §23.2: The Geometric Tangent Space of a Graph]]
- [[§23 The Geometric Tangent Space#^thm-23-3|Theorem §23.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§23 The Geometric Tangent Space#^cor-23-4|Corollary §23.4: Three Descriptions of the Geometric Tangent Space]]
- [[§23 The Geometric Tangent Space#^def-23-4|Definition §23.4: The Directional Derivative Attached to a Tangent Vector]]
- [[§23 The Geometric Tangent Space#^prop-23-8|Proposition §23.8: Basic Properties of D_v]]
- [[§24 Transversality#^thm-24-1|Theorem §24.1: Preimages of Transverse Level Sets]]
- [[§27 Coordinate Derivations and the Basis Theorem#^lem-27-2|Lemma §27.2: Hadamard's Lemma]]
- [[§28 The Differential in Coordinates#^cor-28-3|Corollary §28.3: The Chain Rule in Coordinates]]
- [[§28 The Differential in Coordinates#^prop-28-5|Proposition §28.5: Agreement with the Vector-Space Differential]]
- [[§33 Submanifolds#^prop-33-8|Proposition §33.8: The Old and New Versions Agree]]
- [[§42 The Cotangent Bundle#^prop-42-2|Proposition §42.2: The Smooth Atlas of T^*M]]

## Connections
- **Proof idea.** Split the increment of g into single-variable increments and apply the one-variable [[Mean Value Theorem]]. Continuity of the partials controls the intermediate points. The 451 version is the [[§28 Basic Properties of the Derivative#^thm-28-3|Chain Rule]] (§28.3). Under differentiability alone, see [[§8 Algebra of Differentiable Functions#^thm-8-7|Theorem §8.7]].
- **Linear algebra.** In matrix form, Dg = Df · D(φ, ψ) ([[§12 Composition of Functions and the Chain Rule#^rem-12-2|Matrix Form]]): the derivative of a composition is the composition of the derivatives, and its matrix is the product of the matrices ([[§9 Matrices#^ladr-3-43|LADR 3.43]]). Since determinants are multiplicative ([[§37 Determinants#^ladr-9-49|LADR 9.49]]), a map and its inverse have [[§16 The Inverse Function Theorem#^rem-16-6|reciprocal Jacobians]].
- **Used for.** It is the engine of the [[Inverse Function Theorem (several variables)]] and the [[Method of Lagrange Multipliers]], and it appears in the [[§24 The Change of Variables Formula#^thm-24-2|rectangular change of variables]]. It also underlies [[§37 The Algebra of Differential Forms#^def-37-3|pullback]] and the reduction of [[Stokes' Theorem in ℝ³]] to the parameter domain.
- **On manifolds.** The coordinate-free statement (G ∘ F)_* = G_* ∘ F_* is [[Chain Rule for Differentials]] (591 Thm. §26.6); in coordinates it reduces to this theorem, [[§28 The Differential in Coordinates#^cor-28-3|591 Cor. §28.3]].
- **Also in [[Calculus]]:** [[§110 The Chain Rule#^thm-110-2|Calc Thm. §110.2]] and [[§110 The Chain Rule#^thm-110-3|Calc Thm. §110.3]] (computational treatment with worked examples).
