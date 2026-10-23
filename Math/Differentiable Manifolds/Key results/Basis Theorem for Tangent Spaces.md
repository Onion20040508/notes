---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 29.6", "coordinate derivations form a basis", "Lee Proposition 3.15", "Lee Corollary 3.3"]
tags: [differentiable-manifolds, hub]
---
![[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6]]

## Treated in
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|Theorem §29.6: Basis Theorem]], in [[§29 Coordinate Derivations and the Basis Theorem]]

## Its proof uses
- [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Definition §28.2: The Abstract Tangent Space]]
- [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Definition §28.6: Pushforward — the Differential]]
- [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|Lemma §28.8: Open Subsets Have the Same Abstract Tangent Spaces]]
- [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|Proposition §28.9: Charts Are Diffeomorphisms]]
- [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Definition §29.1: Coordinate Functions of a Chart]]
- [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Definition §29.2: Coordinate Derivations]]
- [[§29 Coordinate Derivations and the Basis Theorem#^prop-29-2|Proposition §29.2: Coordinate Derivations Are Derivations]]
- [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-5|Corollary §29.5: Derivations on ℝⁿ]]

## Used in (Differentiable Manifolds)
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|Theorem §29.7: Ambient and Abstract Agree]]
- [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-8|Corollary §29.8: Consequences]]
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|Theorem §29.9: Dimension of the Tangent Space]]
- [[§30 The Differential in Coordinates#^thm-30-2|Theorem §30.2: The Matrix of the Differential]]
- [[§30 The Differential in Coordinates#^cor-30-4|Corollary §30.4: Change of Coordinates]]
- [[§30 The Differential in Coordinates#^cor-30-6|Corollary §30.6: The Tangent Space to a Vector Space]]
- [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|Proposition §31.1: Velocity in Coordinates]]
- [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|Theorem §31.2: Every Tangent Vector Is a Velocity]]
- [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|Theorem §31.4: The Tangent Space of a Product]]
- [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|Corollary §31.5: Product Coordinates]]
- [[§32 The Cotangent Space#^prop-32-1|Proposition §32.1: The Tangent Spaces of ℝ]]
- [[§33 Covectors in Coordinates#^lem-33-1|Lemma §33.1: The Differential in Coordinates]]
- [[§33 Covectors in Coordinates#^cor-33-2|Corollary §33.2: Covectors in the Dual Basis]]
- [[§34 The Cotangent Space from Germs#^prop-34-2|Proposition §34.2: A Basis of I_p/I_p²]]
- [[§34 The Cotangent Space from Germs#^thm-34-4|Theorem §34.4: The Cotangent Space from Germs]]
- [[§36 Submersions#^prop-36-4|Proposition §36.4: Submersions to ℝᵏ and Independent Differentials]]
- [[§37 Regular Submanifolds#^prop-37-6|Proposition §37.6: Tangent Spaces of a Regular Submanifold]]
- [[§37 Regular Submanifolds#^prop-37-7|Proposition §37.7: Adapted Charts Give Local Defining Maps]]
- [[§37 Regular Submanifolds#^cor-37-17|Corollary §37.17: Special Cases of Transversality]]
- [[§41 Immersions#^ex-41-1|Example §41.1: An Immersion That Crosses Itself]]
- [[§47 Recap꞉ Germs, Derivations and Tangent Vectors#^ex-47-1|Example §47.1: Vectors in the Plane in Three Ways]]
- [[§49 The Tangent Bundle#^prop-49-2|Proposition §49.2: The Transition Maps of TM]]
- [[§49 The Tangent Bundle#^prop-49-3|Proposition §49.3: The Topology and Smooth Structure of TM]]
- [[§49 The Tangent Bundle#^cor-49-4|Corollary §49.4: The Tangent Bundle Is a Fibration]]
- [[§52 Critical Points and the Hessian#^prop-52-4|Proposition §52.4: The Hessian as a Map T_pM → T_p^(ast)M]]
- [[§52 Critical Points and the Hessian#^prop-52-5|Proposition §52.5: The Zero Section Is a Regular Submanifold]]
- [[§52 Critical Points and the Hessian#^prop-52-9|Proposition §52.9: The Vertical Space of T^*M Along the Zero Section]]
- [[§52 Critical Points and the Hessian#^prop-52-10|Proposition §52.10: The Differential of df at a Critical Point]]
- [[§52 Critical Points and the Hessian#^thm-52-11|Theorem §52.11: Transversality to the Zero Section]]
- [[§53 Vector Fields#^prop-53-1|Proposition §53.1: Vector Fields in Coordinates]]
- [[§53 Vector Fields#^prop-53-7|Proposition §53.7: Derivations Are Vector Fields]]
- [[§55 Lie Bracket and Lie Algebra#^prop-55-2|Proposition §55.2: The Bracket in Coordinates]]
- [[§55 Lie Bracket and Lie Algebra#^prop-55-3|Proposition §55.3: The Hessian at a Critical Point via Vector Fields]]
- [[§56 Related Vector Fields#^ex-56-1|Example §56.1: Fields Related by a Projection]]

## Connections
- **Used for.** dim T_pM = n, which finishes [[Ambient and Abstract Tangent Spaces Agree]] ([[§29 Coordinate Derivations and the Basis Theorem#^cor-29-8|§29.8]]). The coordinate bases give the [[Matrix of the Differential]], the dual bases dxⁱ|_p of T*_pM ([[§33 Covectors in Coordinates#^lem-33-1|§33.1]]), the charts of TM ([[Tangent Bundle Is a Smooth Manifold]]) and the straight-line curves of [[Every Tangent Vector Is a Velocity]].
- **Why only first derivatives survive.** The chart turns D into a derivation at a point of ℝⁿ ([[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]). There [[Hadamard's Lemma]], applied twice, writes a germ as a constant plus a linear term plus an element of I_p². D kills constants and I_p² by the Leibniz rule ([[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]]), so only the linear term is left ([[§29 Coordinate Derivations and the Basis Theorem#^rem-29-3|A Derivation Sees Only the First Derivatives]]).
- **Same idea elsewhere.** The universal formula D = Σ D[xⁱ] ∂/∂xⁱ|_p is the expansion of a vector in a basis, with coefficients read off by the dual basis ([[§12 Duality#^ladr-3-114|LADR 3.114]]): D[xⁱ] = dxⁱ|_p(D). Changing the chart changes the basis by the Jacobian of the transition map ([[§30 The Differential in Coordinates#^cor-30-4|§30.4]]), an instance of the change-of-basis formula ([[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]]).
- **Vector fields.** In a chart a vector field is X = Σ Xʲ ∂/∂xʲ, with coefficients Xʲ(p) = X_p[xʲ] given by the universal formula at each point, and it is smooth exactly when the Xʲ are ([[§53 Vector Fields#^prop-53-1|§53.1]]).
