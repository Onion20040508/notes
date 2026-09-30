---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 16.1", "Green"]
tags: [multivariable-analysis, hub]
---
![[§16 Line Integrals and Green's Theorem#^thm-16-1]]

## Treated in
- [[§16 Line Integrals and Green's Theorem#^thm-16-1|Theorem §16.1: Green's Theorem]], in [[§16 Line Integrals and Green's Theorem]]

## Its proof uses
- [[§15 Multivariable Integration#^thm-15-4|Theorem §15.4: Additivity over Domains]]
- [[§15 Multivariable Integration#^thm-15-9|Theorem §15.9: Fubini for Type I Regions]]
- [[§15 Multivariable Integration#^thm-15-10|Theorem §15.10: Fubini for Type II Regions]]
- [[§15 Multivariable Integration#^def-15-12|Definition §15.12: Type I and Type II Regions]]

## Its proof uses (other subjects)
- [[Fundamental Theorem of Calculus]] (Single Variable Analysis)

## Used in (Multivariable Analysis)
- [[§16 Line Integrals and Green's Theorem#^thm-16-2|Theorem §16.2: Divergence Theorem in ℝ²]]
- [[§16 Line Integrals and Green's Theorem#^thm-16-3|Theorem §16.3: Green's Theorem as 2D Stokes' Theorem]]
- [[§20 Stokes' Theorem in ℝ³#^thm-20-1|Theorem §20.1: Stokes' Theorem]]

## Connections
- **Proof idea.** On a region of both [[§15 Multivariable Integration#^def-15-12|Type I and Type II]], the [[Fundamental Theorem of Calculus]] in y gives ∮ f dx = −∬ f_y, and in x it gives ∮ g dy = ∬ g_x. Iterated integrals equal double integrals by Fubini ([[§15 Multivariable Integration#^thm-15-9|§15.9]], [[§15 Multivariable Integration#^thm-15-10|§15.10]]). General regions are subdivided, and the internal edges cancel.
- **Two faces.** In circulation form it is [[§16 Line Integrals and Green's Theorem#^thm-16-3|2D Stokes]], and in flux form it is the [[§16 Line Integrals and Green's Theorem#^thm-16-2|Divergence Theorem in ℝ²]] ([[§16 Line Integrals and Green's Theorem#^rem-16-4|Two Faces of Green's Theorem]]).
- **Chain.** Pulled back to a parameter domain it proves [[Stokes' Theorem in ℝ³]]. The flux form grows into the [[Divergence Theorem in ℝⁿ]]. In forms language it is the [[Generalized Stokes' Theorem]] for the 1-form f dx + g dy, with d(f dx + g dy) = (g_x − f_y) dx∧dy.
- **Topology.** “Curl-free ⇒ conservative” needs a region without holes. The [[Angle form on the punctured plane]] is closed but not exact ([[§22 The Algebra of Differential Forms#^prop-22-11|§22.11]]). The relevant notion is [[§23 The Fundamental Group#^def-23-3|simply connected]] (590 §23.3), and the hole is seen by π₁(S¹) ≅ ℤ ([[Fundamental Group of the Circle]]).
