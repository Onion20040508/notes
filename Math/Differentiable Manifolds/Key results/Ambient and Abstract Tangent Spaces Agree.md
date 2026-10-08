---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 29.6", "v ↦ D_v", "Lee Proposition 3.2", "Lee Proposition 5.37", "Lee Proposition 5.38"]
tags: [differentiable-manifolds, hub]
---
![[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6]]

## Treated in
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|Theorem §29.6: Ambient and Abstract Agree]], in [[§29 Coordinate Derivations and the Basis Theorem]]

## Its proof uses
- [[§25 The Geometric Tangent Space#^def-25-1|Definition §25.1: Geometric Tangent Space]]
- [[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§25 The Geometric Tangent Space#^def-25-4|Definition §25.4: The Directional Derivative Attached to a Tangent Vector]]
- [[§25 The Geometric Tangent Space#^prop-25-8|Proposition §25.8: Basic Properties of D_v]]
- [[§25 The Geometric Tangent Space#^prop-25-9|Proposition §25.9: D_v Determines v]]
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|Theorem §29.5: Basis Theorem]]

## Used in (Differentiable Manifolds)
- [[§35 Submanifolds#^prop-35-9|Proposition §35.9: The Old and New Versions Agree]]

## Connections
- **Used for.** It lets the geometric tangent spaces computed in [[§25 The Geometric Tangent Space|§25]] serve as abstract ones, e.g. T_I O(n) = Skew(n) ([[§25 The Geometric Tangent Space#^ex-25-2|Ex. §25.2]]) and the table of [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]]. It gives part (2) of [[§35 Submanifolds#^prop-35-9|§35.9]]: for a regular level set S, the submanifold tangent space ι_*(T_pS) is ker F′(p). Read through curves, it says the geometric and the abstract velocity of a curve agree ([[§31 Tangent Vectors as Velocities of Curves#^rem-31-1|The Two Faces Reconciled]]).
- **How it is proved.** v ↦ D_v is injective because D_v determines v ([[§25 The Geometric Tangent Space#^prop-25-9|§25.9]]). Surjectivity is never constructed: both sides have dimension n, by [[Geometric Tangent Space Is the Kernel of the Jacobian]] and the [[Basis Theorem for Tangent Spaces]], so the injective linear map is onto ([[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]). The proof of [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]] also gets one inclusion from a dimension count.
- **Same idea elsewhere.** In ℝⁿ the trade v ↔ D_v is the directional derivative of calculus, D_v g = Σ vⁱ ∂g/∂rⁱ ([[§30 The Differential in Coordinates#^prop-30-5|§30.5]]; the two-variable [[Directional Derivative Formula]] of 452).
- **Looking ahead (not yet announced in the course).** Whitney's embedding theorem puts every manifold inside some ℝᴺ, so every abstract tangent space can be realized as a subspace of ℝᴺ in this way.
