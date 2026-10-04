---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 18.1", "surface area formula"]
tags: [multivariable-analysis, hub]
---
![[§18 Surface Integrals#^thm-18-1]]

## Treated in
- [[§18 Surface Integrals#^thm-18-1|Theorem §18.1: Surface Area via the Gram Matrix]], in [[§18 Surface Integrals]]

## Its proof uses
- [[§18 Surface Integrals#^def-18-2|Definition §18.2: Tangent Vectors]]
- [[§18 Surface Integrals#^def-18-4|Definition §18.4: Gram Matrix]]

## Its proof uses (other subjects)
- [[§19 Inner Products and Norms#^ladr-6-1|LADR 6.1 Dot product]]

## Used in (Multivariable Analysis)
- (not cited later in the course)

## Connections
- **Proof.** In ℝ³, det G = |X_u × X_v|² by direct expansion (Lagrange's identity). The entries of G are [[§19 Inner Products and Norms#^ladr-6-1|dot products]] (LADR 6.1) of the tangent vectors.
- **Linear algebra.** G = (DX)ᵀDX is T*T for T = DX. So rank G = rank DX ([[§26 Singular Value Decomposition#^ladr-7-64|LADR 7.64]]), and det G > 0 exactly at [[§18 Surface Integrals#^def-18-3|regular points]]. When DX is square, √det(T*T) = |det T| ([[§34 Determinants#^ladr-9-60|LADR 9.60]], [[§34 Determinants#^ladr-9-61|LADR 9.61]]), which is the |J| of the [[Change of Variables Formula (multiple integrals)]].
- **Why the Gram matrix.** Unlike the cross product, it works in any ambient dimension, and it is the metric tensor (first fundamental form) of the surface ([[§18 Surface Integrals#^rem-18-4|Why the Gram Matrix?]]). For the sphere of radius R it gives area 4πR² ([[§18 Surface Integrals#^ex-18-2|Example §18.2]]).
- **In forms language.** The same area element appears when a 2-form is pulled back to the parameter domain ([[§22 The Algebra of Differential Forms#^ex-22-3|Pullback Along a Surface]]).
