---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 12.16", "coordinate derivations form a basis", "Lee Proposition 3.15", "Lee Corollary 3.3"]
tags: [differentiable-manifolds, hub]
---
![[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16]]

## Treated in
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|Theorem §12.16: Basis Theorem]], in [[§12 Tangent Spaces II꞉ The Abstract Tangent Space]]

## Its proof uses
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-10|Definition §12.10: Pushforward — the Differential]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-11|Definition §12.11: Coordinate Functions of a Chart]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-12|Definition §12.12: Coordinate Derivations]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-14|Proposition §12.14: Charts Are Diffeomorphisms]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-15|Proposition §12.15: Coordinate Derivations Are Derivations]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-19|Corollary §12.19: Derivations on ℝⁿ]]

## Used in (Differentiable Manifolds)
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-20|Corollary §12.20: Consequences]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|Theorem §12.22: The Matrix of the Differential]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-29|Proposition §12.29: Velocity in Coordinates]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-30|Theorem §12.30: Every Tangent Vector Is a Velocity]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-32|Theorem §12.32: The Tangent Space of a Product]]
- [[§13 Tangent Spaces III꞉ The Cotangent Space#^prop-13-1|Proposition §13.1: The Differential Evaluates Derivations]]
- [[§13 Tangent Spaces III꞉ The Cotangent Space#^thm-13-7|Theorem §13.7: The Cotangent Space from Germs]]
- [[§17 The Tangent Bundle#^prop-17-3|Proposition §17.3: The Smooth Atlas of TM]]

## Connections
- **Used for.** dim T_pM = n, which finishes [[Ambient and Abstract Tangent Spaces Agree]] ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-20|§12.20]]). The coordinate bases give the [[Matrix of the Differential]], the dual bases dxⁱ|_p of T*_pM ([[§13 Tangent Spaces III꞉ The Cotangent Space#^lem-13-2|§13.2]]), the charts of TM ([[Tangent Bundle Is a Smooth Manifold]]) and the straight-line curves of [[Every Tangent Vector Is a Velocity]].
- **Why only first derivatives survive.** The chart turns D into a derivation at a point of ℝⁿ ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-14|§12.14]]). There [[Hadamard's Lemma]], applied twice, writes a germ as a constant plus a linear term plus an element of I_p². D kills constants and I_p² by the Leibniz rule ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-6|§12.6]]), so only the linear term is left ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^rem-12-10|A Derivation Sees Only the First Derivatives]]).
- **Same idea elsewhere.** The universal formula D = Σ D[xⁱ] ∂/∂xⁱ|_p is the expansion of a vector in a basis, with coefficients read off by the dual basis ([[3F Duality#^ladr-3-114|LADR 3.114]]): D[xⁱ] = dxⁱ|_p(D). Changing the chart changes the basis by the Jacobian of the transition map ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-24|§12.24]]), an instance of the change-of-basis formula ([[3D Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]]).
- **Coming later in the course.** Vector fields will be written in a chart as X = Σ Xⁱ ∂/∂xⁱ, with smooth coefficient functions Xⁱ.
