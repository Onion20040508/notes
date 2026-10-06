---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 39.7"]
tags: [multivariable-analysis, hub]
---
![[§39 Closed and Exact Forms#^prop-39-7]]

## Treated in
- [[§39 Closed and Exact Forms#^prop-39-7|Proposition §39.7: Poincaré Lemma]], in [[§39 Closed and Exact Forms]]

## Its proof uses
- (no proof in the notes)

## Used in (Multivariable Analysis)
- (not cited later in the course)

## Connections
- **Converse of d² = 0.** [[§39 Closed and Exact Forms#^prop-39-5|Exact ⇒ Closed]] follows from [[Exterior Derivative Squares to Zero]]; the Poincaré Lemma gives the converse on star-shaped domains. The course does not prove it. The standard proof builds the primitive with a homotopy operator that integrates along the segments to p₀; it is in Lee, *Introduction to Smooth Manifolds*, Ch. 17, the textbook of [[Differentiable Manifolds]], and is not yet in the vault.
- **Topology.** A star-shaped domain contracts to p₀ by a [[§28 Homotopy of Paths#^thm-28-1|straight-line homotopy]] (590 §22.1), so it is [[§29 The Fundamental Group#^def-29-3|simply connected]]. With a hole the lemma fails: the [[Angle form on the punctured plane]] is closed but not exact ([[§39 Closed and Exact Forms#^prop-39-6|§39.6]]), matching π₁(ℝ² ∖ {0}) ≅ ℤ ([[Fundamental Group of the Circle]]).
- **Classical form.** On a star-shaped domain in ℝ³, an irrotational field is a gradient (1-forms), and a divergence-free field is a curl (2-forms). In the terms of [[§13 The Three Differential Operators꞉ Gradient, Curl, Divergence#^def-13-1|Def. §13.1]], [[§13 The Three Differential Operators꞉ Gradient, Curl, Divergence#^def-13-2|irrotational]] implies conservative there, which is the converse of curl(∇f) = 0.
- **On manifolds.** 591 states the 1-form case, that a covector field satisfying the necessary condition of [[§46 One-Forms#^prop-46-3|591 Prop. §46.3]] is a differential on star-shaped domains, and shows with the angle form that the condition alone is not enough ([[§46 One-Forms#^rem-46-1|591 Remark: The Condition Is Not Sufficient]]).
- **Cohomology.** The quotient of closed by exact k-forms is the de Rham group Hᵏ, which measures the k-dimensional holes of the domain. The lemma says that Hᵏ = 0 for k ≥ 1 on star-shaped domains.
- **Used in Electromagnetism.** The classical form gives the scalar and vector potentials of electrostatics and magnetostatics: [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-3|EM Theorem §B1.2.3]]. The hole case is the field of a line current, curl-free off the wire but with nonzero circulation around it: [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^cau-b1-2-1|EM Caution: Curl-free is not enough on a region with a hole]], [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^ex-b1-2-2|EM Example §B1.2.2]].
- **Also in [[Calculus]]:** [[§136 Stokes' Theorem#^thm-136-4|Calc Thm. §136.4]] and [[§131 Extended Versions of Green's Theorem#^thm-131-3|Calc Thm. §131.3]] (computational treatment with worked examples).
- **Also in [[Ordinary Differential Equations]]:** [[§11 Exact Differential Equations and Integrating Factors#^thm-11-2|331 Thm. §11.2]] (the test for exact equations: the case of 1-forms on a rectangle in ℝ², proved by building the potential, with worked examples).
- **Also in [[Complex Variables]]:** [[§115★ Harmonic Conjugates#^thm-115-4|342 Thm. §115.4]] (on a simply connected plane domain a harmonic u has a harmonic conjugate, by exactness of a closed 1-form; complex-variables version with worked examples).
