---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 24.5", "coordinate derivations form a basis", "Lee Proposition 3.15", "Lee Corollary 3.3"]
tags: [differentiable-manifolds, hub]
---
![[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5]]

## Treated in
- [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|Theorem §24.5: Basis Theorem]], in [[§24 Coordinate Derivations and the Basis Theorem]]

## Its proof uses
- [[§23 Derivations and the Abstract Tangent Space#^def-23-5|Definition §23.5: Pushforward — the Differential]]
- [[§23 Derivations and the Abstract Tangent Space#^prop-23-9|Proposition §23.9: Charts Are Diffeomorphisms]]
- [[§24 Coordinate Derivations and the Basis Theorem#^prop-24-1|Proposition §24.1: Coordinate Derivations Are Derivations]]
- [[§24 Coordinate Derivations and the Basis Theorem#^def-24-1|Definition §24.1: Coordinate Functions of a Chart]]
- [[§24 Coordinate Derivations and the Basis Theorem#^def-24-2|Definition §24.2: Coordinate Derivations]]
- [[§24 Coordinate Derivations and the Basis Theorem#^cor-24-4|Corollary §24.4: Derivations on ℝⁿ]]

## Used in (Differentiable Manifolds)
- [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-6|Theorem §24.6: Ambient and Abstract Agree]]
- [[§24 Coordinate Derivations and the Basis Theorem#^cor-24-7|Corollary §24.7: Consequences]]
- [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-8|Theorem §24.8: Dimension of the Tangent Space]]
- [[§25 The Differential in Coordinates#^thm-25-2|Theorem §25.2: The Matrix of the Differential]]
- [[§26 Tangent Vectors as Velocities of Curves#^prop-26-1|Proposition §26.1: Velocity in Coordinates]]
- [[§26 Tangent Vectors as Velocities of Curves#^thm-26-2|Theorem §26.2: Every Tangent Vector Is a Velocity]]
- [[§26 Tangent Vectors as Velocities of Curves#^thm-26-4|Theorem §26.4: The Tangent Space of a Product]]
- [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|Proposition §27.1: The Differential Evaluates Derivations]]
- [[§27 Tangent Spaces III꞉ The Cotangent Space#^thm-27-7|Theorem §27.7: The Cotangent Space from Germs]]
- [[§32 The Tangent Bundle#^prop-32-2|Proposition §32.2: The Smooth Atlas of TM]]

## Connections
- **Used for.** dim T_pM = n, which finishes [[Ambient and Abstract Tangent Spaces Agree]] ([[§24 Coordinate Derivations and the Basis Theorem#^cor-24-7|§24.7]]). The coordinate bases give the [[Matrix of the Differential]], the dual bases dxⁱ|_p of T*_pM ([[§27 Tangent Spaces III꞉ The Cotangent Space#^lem-27-2|§27.2]]), the charts of TM ([[Tangent Bundle Is a Smooth Manifold]]) and the straight-line curves of [[Every Tangent Vector Is a Velocity]].
- **Why only first derivatives survive.** The chart turns D into a derivation at a point of ℝⁿ ([[§23 Derivations and the Abstract Tangent Space#^prop-23-9|§23.9]]). There [[Hadamard's Lemma]], applied twice, writes a germ as a constant plus a linear term plus an element of I_p². D kills constants and I_p² by the Leibniz rule ([[§23 Derivations and the Abstract Tangent Space#^lem-23-2|§23.2]]), so only the linear term is left ([[§24 Coordinate Derivations and the Basis Theorem#^rem-24-3|A Derivation Sees Only the First Derivatives]]).
- **Same idea elsewhere.** The universal formula D = Σ D[xⁱ] ∂/∂xⁱ|_p is the expansion of a vector in a basis, with coefficients read off by the dual basis ([[§12 Duality#^ladr-3-114|LADR 3.114]]): D[xⁱ] = dxⁱ|_p(D). Changing the chart changes the basis by the Jacobian of the transition map ([[§25 The Differential in Coordinates#^cor-25-4|§25.4]]), an instance of the change-of-basis formula ([[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]]).
- **Coming later in the course.** Vector fields will be written in a chart as X = Σ Xⁱ ∂/∂xⁱ, with smooth coefficient functions Xⁱ.
