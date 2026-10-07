---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 29.5", "coordinate derivations form a basis", "Lee Proposition 3.15", "Lee Corollary 3.3"]
tags: [differentiable-manifolds, hub]
---
![[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5]]

## Treated in
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|Theorem §29.5: Basis Theorem]], in [[§29 Coordinate Derivations and the Basis Theorem]]

## Its proof uses
- [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Definition §28.6: Pushforward — the Differential]]
- [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|Proposition §28.9: Charts Are Diffeomorphisms]]
- [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Definition §29.1: Coordinate Functions of a Chart]]
- [[§29 Coordinate Derivations and the Basis Theorem#^prop-29-1|Proposition §29.1: Coordinate Derivations Are Derivations]]
- [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Definition §29.2: Coordinate Derivations]]
- [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-4|Corollary §29.4: Derivations on ℝⁿ]]

## Used in (Differentiable Manifolds)
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|Theorem §29.6: Ambient and Abstract Agree]]
- [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-7|Corollary §29.7: Consequences]]
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|Theorem §29.8: Dimension of the Tangent Space]]
- [[§30 The Differential in Coordinates#^thm-30-2|Theorem §30.2: The Matrix of the Differential]]
- [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|Proposition §31.1: Velocity in Coordinates]]
- [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|Theorem §31.2: Every Tangent Vector Is a Velocity]]
- [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|Theorem §31.4: The Tangent Space of a Product]]
- [[§32 The Cotangent Space#^prop-32-1|Proposition §32.1: The Differential Evaluates Derivations]]
- [[§32 The Cotangent Space#^thm-32-8|Theorem §32.8: The Cotangent Space from Germs]]
- [[§42 Recap꞉ Germs, Derivations and Tangent Vectors#^ex-42-1|Example §42.1: Vectors in the Plane in Three Ways]]
- [[§44 The Tangent Bundle#^prop-44-2|Proposition §44.2: The Smooth Atlas of TM]]
- [[§47 Vector Fields#^prop-47-1|Proposition §47.1: Vector Fields in Coordinates]]
- [[§47 Vector Fields#^prop-47-7|Proposition §47.7: Derivations Are Vector Fields]]

## Connections
- **Used for.** dim T_pM = n, which finishes [[Ambient and Abstract Tangent Spaces Agree]] ([[§29 Coordinate Derivations and the Basis Theorem#^cor-29-7|§29.7]]). The coordinate bases give the [[Matrix of the Differential]], the dual bases dxⁱ|_p of T*_pM ([[§32 The Cotangent Space#^lem-32-2|§32.2]]), the charts of TM ([[Tangent Bundle Is a Smooth Manifold]]) and the straight-line curves of [[Every Tangent Vector Is a Velocity]].
- **Why only first derivatives survive.** The chart turns D into a derivation at a point of ℝⁿ ([[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]). There [[Hadamard's Lemma]], applied twice, writes a germ as a constant plus a linear term plus an element of I_p². D kills constants and I_p² by the Leibniz rule ([[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]]), so only the linear term is left ([[§29 Coordinate Derivations and the Basis Theorem#^rem-29-3|A Derivation Sees Only the First Derivatives]]).
- **Same idea elsewhere.** The universal formula D = Σ D[xⁱ] ∂/∂xⁱ|_p is the expansion of a vector in a basis, with coefficients read off by the dual basis ([[§12 Duality#^ladr-3-114|LADR 3.114]]): D[xⁱ] = dxⁱ|_p(D). Changing the chart changes the basis by the Jacobian of the transition map ([[§30 The Differential in Coordinates#^cor-30-4|§30.4]]), an instance of the change-of-basis formula ([[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]]).
- **Vector fields.** In a chart a vector field is X = Σ Xʲ ∂/∂xʲ, with coefficients Xʲ(p) = X_p[xʲ] given by the universal formula at each point, and it is smooth exactly when the Xʲ are ([[§47 Vector Fields#^prop-47-1|§47.1]]).
