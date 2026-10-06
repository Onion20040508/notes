---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 32.1", "Gauss divergence theorem"]
tags: [multivariable-analysis, hub]
---
![[§32 Flux Integrals and the Divergence Theorem in ℝ³#^thm-32-1]]

## Treated in
- [[§32 Flux Integrals and the Divergence Theorem in ℝ³#^thm-32-1|Theorem §32.1: Divergence Theorem in ℝ³]], in [[§32 Flux Integrals and the Divergence Theorem in ℝ³]]

## Its proof uses
- [[§22 Properties of the Integral#^thm-22-2|Theorem §22.2: Additivity in the Integrand]]
- [[§23 Fubini's Theorem#^thm-23-2|Theorem §23.2: Fubini for Type I Regions]]
- [[§31 Surface Integrals#^def-31-2|Definition §31.2: Tangent Vectors]]
- [[§32 Flux Integrals and the Divergence Theorem in ℝ³#^def-32-1|Definition §32.1: Vector Surface Integral / Flux Integral]]

## Its proof uses (other subjects)
- [[Fundamental Theorem of Calculus]] (Single Variable Analysis)

## Used in (Multivariable Analysis)
- [[§33 The Laplacian in Spherical Coordinates#^thm-33-1|Theorem §33.1: Laplacian in Spherical Coordinates]]
- [[§38 The Exterior Derivative#^ex-38-1|Example §38.1: Flux Through the Unit Sphere via Pullback]]

## Connections
- **Proof idea.** Treat one component at a time on a simple solid region. [[§23 Fubini's Theorem#^thm-23-2|Fubini]] makes the volume integral iterated, and the [[Fundamental Theorem of Calculus]] in z reduces it to top minus bottom: the flux through the two graph surfaces, where the [[§32 Flux Integrals and the Divergence Theorem in ℝ³#^rem-32-7|bottom normal is reversed]]. General regions are cut into simple pieces, and the fluxes through internal cuts cancel ([[§32 Flux Integrals and the Divergence Theorem in ℝ³#^rem-32-8|Simple Solid Regions]]).
- **Chain.** The 2D version is [[§27 Line Integrals and Green's Theorem#^thm-27-2|Divergence Theorem in ℝ²]], the flux form of [[Green's Theorem]]. The same proof works in any dimension ([[Divergence Theorem in ℝⁿ]]). In forms language it is the case of the [[Generalized Stokes' Theorem]] for a 2-form on a solid, since d on 2-forms gives the divergence ([[§38 The Exterior Derivative#^prop-38-3|Prop. §38.3]]).
- **Used for.** Green's identities in ℝ³, by applying it to the field u∇v ([[§32 Flux Integrals and the Divergence Theorem in ℝ³#^rem-32-9|Green's Identities Revisited]]), and the [[§33 The Laplacian in Spherical Coordinates#^thm-33-1|Laplacian in spherical coordinates]] (§33.1), which applies it to ∇u on an infinitesimal spherical brick.
- **Also in [[Calculus]]:** [[§137 The Divergence Theorem#^thm-137-1|Calc Thm. §137.1]] (computational treatment with worked examples).
