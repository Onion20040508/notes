---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 18.2", "Gauss divergence theorem"]
tags: [multivariable-analysis, hub]
---
![[Multivariable Analysis §18 Surface Integrals#^thm-18-2]]

## Treated in
- [[Multivariable Analysis §18 Surface Integrals#^thm-18-2|Theorem §18.2: Divergence Theorem in ℝ³]], in [[Multivariable Analysis §18 Surface Integrals]]

## Its proof uses
- [[Multivariable Analysis §15 Multivariable Integration#^thm-15-3|Theorem §15.3: Additivity in the Integrand]]
- [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|Theorem §15.9: Fubini for Type I Regions]]
- [[Multivariable Analysis §18 Surface Integrals#^def-18-2|Definition §18.2: Tangent Vectors]]
- [[Multivariable Analysis §18 Surface Integrals#^def-18-6|Definition §18.6: Vector Surface Integral / Flux Integral]]

## Its proof uses (other subjects)
- [[Fundamental Theorem of Calculus]] (Single Variable Analysis)

## Used in (Multivariable Analysis)
- [[Multivariable Analysis §19 The Laplacian in Spherical Coordinates#^thm-19-1|Theorem §19.1: Laplacian in Spherical Coordinates]]
- [[Multivariable Analysis §22 The Algebra of Differential Forms#^ex-22-5|Example §22.5: Flux Through the Unit Sphere via Pullback]]

## Connections
- **Proof idea.** Treat one component at a time on a simple solid region. [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|Fubini]] makes the volume integral iterated, and the [[Fundamental Theorem of Calculus]] in z reduces it to top minus bottom: the flux through the two graph surfaces, where the [[Multivariable Analysis §18 Surface Integrals#^rem-18-7|bottom normal is reversed]]. General regions are cut into simple pieces, and the fluxes through internal cuts cancel ([[Multivariable Analysis §18 Surface Integrals#^rem-18-8|Simple Solid Regions]]).
- **Chain.** The 2D version is [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-2|Divergence Theorem in ℝ²]], the flux form of [[Green's Theorem]]. The same proof works in any dimension ([[Divergence Theorem in ℝⁿ]]). In forms language it is the case of the [[Generalized Stokes' Theorem]] for a 2-form on a solid, since d on 2-forms gives the divergence ([[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-4|Prop. §22.4]]).
- **Used for.** Green's identities in ℝ³, by applying it to the field u∇v ([[Multivariable Analysis §18 Surface Integrals#^rem-18-9|Green's Identities Revisited]]), and the [[Multivariable Analysis §19 The Laplacian in Spherical Coordinates#^thm-19-1|Laplacian in spherical coordinates]] (§19.1), which applies it to ∇u on an infinitesimal spherical brick.
