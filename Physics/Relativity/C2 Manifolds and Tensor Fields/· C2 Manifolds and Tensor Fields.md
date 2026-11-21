---
type: chapter
subject: "[[Relativity]]"
level: C
chapter: C2
tags: [chapter, relativity]
---
# C2 Manifolds and Tensor Fields
← [[· C1 From Special Relativity to Gravity]] · ↑ [[Relativity]] · [[· C3 Metric, Connection and Curvature]] →

**Builds on:** [[· B1 Minkowski Spacetime and the Lorentz Group|B1 Minkowski Spacetime and the Lorentz Group]] (9), [[· B2 Four-Vectors and Tensors|B2 Four-Vectors and Tensors]] (12), [[· C1 From Special Relativity to Gravity|C1 From Special Relativity to Gravity]] (2), [[· C3 Metric, Connection and Curvature|C3 Metric, Connection and Curvature]] (7)
**Used by:** [[· B1 Minkowski Spacetime and the Lorentz Group|B1 Minkowski Spacetime and the Lorentz Group]] (2), [[· B2 Four-Vectors and Tensors|B2 Four-Vectors and Tensors]] (6), [[· B3 Relativistic Dynamics from an Action|B3 Relativistic Dynamics from an Action]] (1), [[· B4 Fields in Special Relativity|B4 Fields in Special Relativity]] (1), [[· C3 Metric, Connection and Curvature|C3 Metric, Connection and Curvature]] (176)

★ *Self-study: general relativity beyond any course taken (spine: Couzens' Oxford GR notes; textbooks d'Inverno & Vickers, Hartle, Schutz).*

**The question.** C1 described a weak static field in one coordinate system; general relativity must work in any coordinates and on spacetimes that no single chart covers. How is calculus done when coordinates are only labels? The chapter builds it in the order the failures demand: charts and atlases (§C2.1), tangent vectors as derivations and one-forms as their duals (§C2.2), tensors and their transformation law — and the discovery that partial derivatives of a tensor are not a tensor (§C2.3), maps that carry tensors between manifolds (§C2.4), the Lie derivative, which differentiates along a vector field (§C2.5), the exterior derivative, which needs only antisymmetry (§C2.6), and integration of forms with Stokes' theorem (§C2.7). There is no metric yet: lengths, angles, a volume and a derivative along a single direction come in C3. The mathematical homes of manifolds, tangent spaces, flows and forms are the MATH 591 notes ([[Differentiable Manifolds]]), linked box by box; what 591 does not cover (general tensor fields, Lie derivatives of tensors, Cartan's formula, integration on manifolds, Stokes' theorem) has its home here.

## Sections
- [[§C2.1 Spacetime as a Manifold]] — GR1 §3.1–3.2.1; 591 §2, §17, §19
- [[§C2.2 Tangent Vectors and One-Forms]] — GR1 §3.2.2–3.2.4; Schutz 5.2–5.5; 591 §28–§33
- [[§C2.3 Tensor Fields]] — GR1 §3.2.5; d'Inverno 5, 7.1; REL B2.2
- [[§C2.4 Push-Forward, Pull-Back and Diffeomorphisms]] — GR1 §3.2.6; 591 §28, §30, §79
- [[§C2.5 Flows and the Lie Derivative of Tensors]] — GR1 §3.3; d'Inverno 6.2; 591 §67–§72
- [[§C2.6 Differential Forms]] — GR1 §3.4.1–3.4.3; 591 §75–§84
- [[§C2.7 Integration on Manifolds and Stokes' Theorem]] — GR1 §3.4.4; d'Inverno 7.3–7.4

## Principles
- [[§C2.1 Spacetime as a Manifold#^pr-c2-1-1|§C2.1.1]] Spacetime Is a Four-Dimensional Manifold

## Theorems
- [[§C2.1 Spacetime as a Manifold#^thm-c2-1-2|§C2.1.2]] The Sphere Is Not One Chart
- [[§C2.1 Spacetime as a Manifold#^thm-c2-1-3|§C2.1.3]] The Stereographic Atlas of S²
- [[§C2.1 Spacetime as a Manifold#^thm-c2-1-4|§C2.1.4]] The Boundary Is Well Defined and Is a Manifold
- [[§C2.2 Tangent Vectors and One-Forms#^thm-c2-2-1|§C2.2.1]] Coordinate Basis
- [[§C2.2 Tangent Vectors and One-Forms#^thm-c2-2-2|§C2.2.2]] Transformation Law of Vector Components
- [[§C2.2 Tangent Vectors and One-Forms#^thm-c2-2-3|§C2.2.3]] Dual Basis and Covariant Transformation Law
- [[§C2.2 Tangent Vectors and One-Forms#^thm-c2-2-4|§C2.2.4]] The Pairing Is Chart-Independent
- [[§C2.3 Tensor Fields#^thm-c2-3-1|§C2.3.1]] Components and the General Transformation Law
- [[§C2.3 Tensor Fields#^thm-c2-3-2|§C2.3.2]] Contraction Is Chart-Independent
- [[§C2.3 Tensor Fields#^thm-c2-3-3|§C2.3.3]] Quotient Rule
- [[§C2.3 Tensor Fields#^thm-c2-3-4|§C2.3.4]] Partial Derivatives of a Vector Field Are Not a Tensor
- [[§C2.3 Tensor Fields#^thm-c2-3-5|§C2.3.5]] What Partial Derivatives Can Do Tensorially
- [[§C2.3 Tensor Fields#^thm-c2-3-6|§C2.3.6]] The Levi-Civita Symbol and the Determinant Are Densities
- [[§C2.4 Push-Forward, Pull-Back and Diffeomorphisms#^thm-c2-4-1|§C2.4.1]] Push-Forward in Components
- [[§C2.4 Push-Forward, Pull-Back and Diffeomorphisms#^thm-c2-4-2|§C2.4.2]] Pull-Back in Components
- [[§C2.4 Push-Forward, Pull-Back and Diffeomorphisms#^thm-c2-4-3|§C2.4.3]] Push-Forward and Pull-Back Respect the Pairing
- [[§C2.4 Push-Forward, Pull-Back and Diffeomorphisms#^thm-c2-4-4|§C2.4.4]] A Diffeomorphism Transports Tensors of Every Type
- [[§C2.4 Push-Forward, Pull-Back and Diffeomorphisms#^thm-c2-4-5|§C2.4.5]] What Survives along Maps That Are Not Diffeomorphisms
- [[§C2.5 Flows and the Lie Derivative of Tensors#^thm-c2-5-1|§C2.5.1]] Flow Properties
- [[§C2.5 Flows and the Lie Derivative of Tensors#^thm-c2-5-2|§C2.5.2]] Lie Derivative of Functions and Vector Fields
- [[§C2.5 Flows and the Lie Derivative of Tensors#^thm-c2-5-3|§C2.5.3]] Lie Derivative of a One-Form, in Components
- [[§C2.5 Flows and the Lie Derivative of Tensors#^thm-c2-5-4|§C2.5.4]] Lie Derivative of an (r, s) Tensor, in Components
- [[§C2.5 Flows and the Lie Derivative of Tensors#^thm-c2-5-5|§C2.5.5]] Leibniz Rule; the Lie Derivative Commutes with Contraction
- [[§C2.5 Flows and the Lie Derivative of Tensors#^thm-c2-5-6|§C2.5.6]] The Commutator of Two Lie Derivatives
- [[§C2.5 Flows and the Lie Derivative of Tensors#^thm-c2-5-7|§C2.5.7]] The Bracket Measures the Failure of Flows to Commute
- [[§C2.5 Flows and the Lie Derivative of Tensors#^thm-c2-5-8|§C2.5.8]] The Lie Derivative Depends on X near p, Not Only on Its Value at p
- [[§C2.6 Differential Forms#^thm-c2-6-1|§C2.6.1]] Components of dω; d² = 0, Graded Leibniz, d Commutes with Pull-Back
- [[§C2.6 Differential Forms#^thm-c2-6-2|§C2.6.2]] Poincaré Lemma
- [[§C2.6 Differential Forms#^thm-c2-6-3|§C2.6.3]] Cartan's Formula
- [[§C2.7 Integration on Manifolds and Stokes' Theorem#^thm-c2-7-1|§C2.7.1]] Top Forms Transform with the Jacobian Determinant
- [[§C2.7 Integration on Manifolds and Stokes' Theorem#^thm-c2-7-2|§C2.7.2]] The Integral Does Not Depend on the Oriented Atlas or the Partition
- [[§C2.7 Integration on Manifolds and Stokes' Theorem#^thm-c2-7-3|§C2.7.3]] Stokes' Theorem
- [[§C2.7 Integration on Manifolds and Stokes' Theorem#^thm-c2-7-4|§C2.7.4]] Gauss's Theorem for Vector Densities; Total Divergences Integrate to Zero
