---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 27.5", "coordinate derivations form a basis", "Lee Proposition 3.15", "Lee Corollary 3.3"]
tags: [differentiable-manifolds, hub]
---
![[§27 Coordinate Derivations and the Basis Theorem#^thm-27-5]]

## Treated in
- [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-5|Theorem §27.5: Basis Theorem]], in [[§27 Coordinate Derivations and the Basis Theorem]]

## Its proof uses
- [[§26 Derivations and the Abstract Tangent Space#^def-26-5|Definition §26.5: Pushforward — the Differential]]
- [[§26 Derivations and the Abstract Tangent Space#^prop-26-9|Proposition §26.9: Charts Are Diffeomorphisms]]
- [[§27 Coordinate Derivations and the Basis Theorem#^def-27-1|Definition §27.1: Coordinate Functions of a Chart]]
- [[§27 Coordinate Derivations and the Basis Theorem#^prop-27-1|Proposition §27.1: Coordinate Derivations Are Derivations]]
- [[§27 Coordinate Derivations and the Basis Theorem#^def-27-2|Definition §27.2: Coordinate Derivations]]
- [[§27 Coordinate Derivations and the Basis Theorem#^cor-27-4|Corollary §27.4: Derivations on ℝⁿ]]

## Used in (Differentiable Manifolds)
- [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-6|Theorem §27.6: Ambient and Abstract Agree]]
- [[§27 Coordinate Derivations and the Basis Theorem#^cor-27-7|Corollary §27.7: Consequences]]
- [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-8|Theorem §27.8: Dimension of the Tangent Space]]
- [[§28 The Differential in Coordinates#^thm-28-2|Theorem §28.2: The Matrix of the Differential]]
- [[§29 Tangent Vectors as Velocities of Curves#^prop-29-1|Proposition §29.1: Velocity in Coordinates]]
- [[§29 Tangent Vectors as Velocities of Curves#^thm-29-2|Theorem §29.2: Every Tangent Vector Is a Velocity]]
- [[§29 Tangent Vectors as Velocities of Curves#^thm-29-4|Theorem §29.4: The Tangent Space of a Product]]
- [[§30 Tangent Spaces III꞉ The Cotangent Space#^prop-30-1|Proposition §30.1: The Differential Evaluates Derivations]]
- [[§30 Tangent Spaces III꞉ The Cotangent Space#^thm-30-7|Theorem §30.7: The Cotangent Space from Germs]]
- [[§35 The Tangent Bundle#^prop-35-2|Proposition §35.2: The Smooth Atlas of TM]]

## Connections
- **Used for.** dim T_pM = n, which finishes [[Ambient and Abstract Tangent Spaces Agree]] ([[§27 Coordinate Derivations and the Basis Theorem#^cor-27-7|§27.7]]). The coordinate bases give the [[Matrix of the Differential]], the dual bases dxⁱ|_p of T*_pM ([[§30 Tangent Spaces III꞉ The Cotangent Space#^lem-30-2|§30.2]]), the charts of TM ([[Tangent Bundle Is a Smooth Manifold]]) and the straight-line curves of [[Every Tangent Vector Is a Velocity]].
- **Why only first derivatives survive.** The chart turns D into a derivation at a point of ℝⁿ ([[§26 Derivations and the Abstract Tangent Space#^prop-26-9|§26.9]]). There [[Hadamard's Lemma]], applied twice, writes a germ as a constant plus a linear term plus an element of I_p². D kills constants and I_p² by the Leibniz rule ([[§26 Derivations and the Abstract Tangent Space#^lem-26-2|§26.2]]), so only the linear term is left ([[§27 Coordinate Derivations and the Basis Theorem#^rem-27-3|A Derivation Sees Only the First Derivatives]]).
- **Same idea elsewhere.** The universal formula D = Σ D[xⁱ] ∂/∂xⁱ|_p is the expansion of a vector in a basis, with coefficients read off by the dual basis ([[§12 Duality#^ladr-3-114|LADR 3.114]]): D[xⁱ] = dxⁱ|_p(D). Changing the chart changes the basis by the Jacobian of the transition map ([[§28 The Differential in Coordinates#^cor-28-4|§28.4]]), an instance of the change-of-basis formula ([[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]]).
- **Coming later in the course.** Vector fields will be written in a chart as X = Σ Xⁱ ∂/∂xⁱ, with smooth coefficient functions Xⁱ.
