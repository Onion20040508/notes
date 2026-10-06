---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 27.1", "Green"]
tags: [multivariable-analysis, hub]
---
![[§27 Line Integrals and Green's Theorem#^thm-27-1]]

## Treated in
- [[§27 Line Integrals and Green's Theorem#^thm-27-1|Theorem §27.1: Green's Theorem]], in [[§27 Line Integrals and Green's Theorem]]

## Its proof uses
- [[§22 Properties of the Integral#^thm-22-3|Theorem §22.3: Additivity over Domains]]
- [[§23 Fubini's Theorem#^thm-23-2|Theorem §23.2: Fubini for Type I Regions]]
- [[§23 Fubini's Theorem#^thm-23-3|Theorem §23.3: Fubini for Type II Regions]]
- [[§23 Fubini's Theorem#^def-23-1|Definition §23.1: Type I Region]]
- [[§23 Fubini's Theorem#^def-23-2|Definition §23.2: Type II Region]]

## Its proof uses (other subjects)
- [[Fundamental Theorem of Calculus]] (Single Variable Analysis)

## Used in (Multivariable Analysis)
- [[§27 Line Integrals and Green's Theorem#^thm-27-2|Theorem §27.2: Divergence Theorem in ℝ²]]
- [[§27 Line Integrals and Green's Theorem#^thm-27-3|Theorem §27.3: Green's Theorem as 2D Stokes' Theorem]]
- [[§34 Stokes' Theorem in ℝ³#^thm-34-1|Theorem §34.1: Stokes' Theorem]]

## Connections
- **Proof idea.** On a region of both [[§23 Fubini's Theorem#^def-23-1|Type I and Type II]], the [[Fundamental Theorem of Calculus]] in y gives ∮ f dx = −∬ f_y, and in x it gives ∮ g dy = ∬ g_x. Iterated integrals equal double integrals by Fubini ([[§23 Fubini's Theorem#^thm-23-2|§23.2]], [[§23 Fubini's Theorem#^thm-23-3|§23.3]]). General regions are subdivided, and the internal edges cancel.
- **Two faces.** In circulation form it is [[§27 Line Integrals and Green's Theorem#^thm-27-3|2D Stokes]], and in flux form it is the [[§27 Line Integrals and Green's Theorem#^thm-27-2|Divergence Theorem in ℝ²]] ([[§27 Line Integrals and Green's Theorem#^rem-27-4|Two Faces of Green's Theorem]]).
- **Chain.** Pulled back to a parameter domain it proves [[Stokes' Theorem in ℝ³]]. The flux form grows into the [[Divergence Theorem in ℝⁿ]]. In forms language it is the [[Generalized Stokes' Theorem]] for the 1-form f dx + g dy, with d(f dx + g dy) = (g_x − f_y) dx∧dy.
- **Topology.** “Curl-free ⇒ conservative” needs a region without holes. The [[Angle form on the punctured plane]] is closed but not exact ([[§39 Closed and Exact Forms#^prop-39-6|§39.6]]). The relevant notion is [[§29 The Fundamental Group#^def-29-3|simply connected]] (590 §29.3), and the hole is seen by π₁(S¹) ≅ ℤ ([[Fundamental Group of the Circle]]).
- **Also in [[Calculus]]:** [[§130 Green's Theorem#^thm-130-1|Calc Thm. §130.1]] (computational treatment with worked examples).
- **Also in [[Complex Variables]]:** [[§50 Cauchy–Goursat Theorem#^thm-50-2|342 Thm. §50.2]] (Cauchy's theorem for f′ continuous, by Green's theorem and the Cauchy–Riemann equations) and [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|342 Thm. §51.3]] (the Cauchy–Goursat theorem without that hypothesis); complex-variables version with worked examples.
