---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 22.12"]
tags: [multivariable-analysis, hub]
---
![[§22 The Algebra of Differential Forms#^prop-22-12]]

## Treated in
- [[§22 The Algebra of Differential Forms#^prop-22-12|Proposition §22.12: Poincaré Lemma]], in [[§22 The Algebra of Differential Forms]]

## Its proof uses
- (no proof in the notes)

## Used in (Multivariable Analysis)
- (not cited later in the course)

## Connections
- **Converse of d² = 0.** [[§22 The Algebra of Differential Forms#^prop-22-10|Exact ⇒ Closed]] follows from [[Exterior Derivative Squares to Zero]]; the Poincaré Lemma gives the converse on star-shaped domains. The course does not prove it. The standard proof builds the primitive with a homotopy operator that integrates along the segments to p₀.
- **Topology.** A star-shaped domain contracts to p₀ by a [[§22 Homotopy of Paths#^thm-22-1|straight-line homotopy]] (590 §22.1), so it is [[§23 The Fundamental Group#^def-23-3|simply connected]]. With a hole the lemma fails: the [[Angle form on the punctured plane]] is closed but not exact ([[§22 The Algebra of Differential Forms#^prop-22-11|§22.11]]), matching π₁(ℝ² ∖ {0}) ≅ ℤ ([[Fundamental Group of the Circle]]).
- **Classical form.** On a star-shaped domain in ℝ³, an irrotational field is a gradient (1-forms), and a divergence-free field is a curl (2-forms). In the terms of [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence#^def-11-1|Def. §11.1]], irrotational implies conservative there, which is the converse of curl(∇f) = 0.
- **Cohomology.** The quotient of closed by exact k-forms is the de Rham group Hᵏ, which measures the k-dimensional holes of the domain. The lemma says that Hᵏ = 0 for k ≥ 1 on star-shaped domains.
- **Used in Electromagnetism.** The classical form gives the scalar and vector potentials of electrostatics and magnetostatics: [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-3|EM Theorem §B1.2.3]]. The hole case is the field of a line current, curl-free off the wire but with nonzero circulation around it: [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^cau-b1-2-1|EM Caution: Curl-free is not enough on a region with a hole]], [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^ex-b1-2-2|EM Example §B1.2.2]].
