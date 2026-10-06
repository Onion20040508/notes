---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 31.1", "surface area formula"]
tags: [multivariable-analysis, hub]
---
![[§31 Surface Integrals#^thm-31-1]]

## Treated in
- [[§31 Surface Integrals#^thm-31-1|Theorem §31.1: Surface Area via the Gram Matrix]], in [[§31 Surface Integrals]]

## Its proof uses
- [[§31 Surface Integrals#^def-31-2|Definition §31.2: Tangent Vectors]]
- [[§31 Surface Integrals#^def-31-4|Definition §31.4: Gram Matrix]]

## Its proof uses (other subjects)
- [[§20 Inner Products and Norms#^ladr-6-1|LADR 6.1 Dot product]]

## Used in (Multivariable Analysis)
- (not cited later in the course)

## Connections
- **Proof.** In ℝ³, det G = |X_u × X_v|² by direct expansion (Lagrange's identity). The entries of G are [[§20 Inner Products and Norms#^ladr-6-1|dot products]] (LADR 6.1) of the tangent vectors.
- **Linear algebra.** G = (DX)ᵀDX is T*T for T = DX. So rank G = rank DX ([[§27 Singular Value Decomposition#^ladr-7-64|LADR 7.64]]), and det G > 0 exactly at [[§31 Surface Integrals#^def-31-3|regular points]]. When DX is square, √det(T*T) = |det T| ([[§37 Determinants#^ladr-9-60|LADR 9.60]], [[§37 Determinants#^ladr-9-61|LADR 9.61]]), which is the |J| of the [[Change of Variables Formula (multiple integrals)]].
- **Why the Gram matrix.** Unlike the cross product, it works in any ambient dimension, and it is the metric tensor (first fundamental form) of the surface ([[§31 Surface Integrals#^rem-31-4|Why the Gram Matrix?]]). For the sphere of radius R it gives area 4πR² ([[§31 Surface Integrals#^ex-31-2|Example §31.2]]).
- **Used ahead of §18.** The proof of the [[Divergence Theorem in ℝⁿ]] (§17.1) takes from it, on credit, the area element of a graph x_n = β(x′): dS = √(1 + |∇′β|²) dx′ ([[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^pf-28-1|proof of Theorem §17.1]], Step 3).
- **In forms language.** The same area element appears when a 2-form is pulled back to the parameter domain ([[§37 The Algebra of Differential Forms#^ex-37-3|Pullback Along a Surface]]).
