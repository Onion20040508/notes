---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 27.6", "v ↦ D_v", "Lee Proposition 3.2", "Lee Proposition 5.37", "Lee Proposition 5.38"]
tags: [differentiable-manifolds, hub]
---
![[§27 Coordinate Derivations and the Basis Theorem#^thm-27-6]]

## Treated in
- [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-6|Theorem §27.6: Ambient and Abstract Agree]], in [[§27 Coordinate Derivations and the Basis Theorem]]

## Its proof uses
- [[§23 The Geometric Tangent Space#^def-23-1|Definition §23.1: Geometric Tangent Space]]
- [[§23 The Geometric Tangent Space#^thm-23-3|Theorem §23.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§23 The Geometric Tangent Space#^def-23-4|Definition §23.4: The Directional Derivative Attached to a Tangent Vector]]
- [[§23 The Geometric Tangent Space#^prop-23-8|Proposition §23.8: Basic Properties of D_v]]
- [[§23 The Geometric Tangent Space#^prop-23-9|Proposition §23.9: D_v Determines v]]
- [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-5|Theorem §27.5: Basis Theorem]]

## Used in (Differentiable Manifolds)
- [[§27 Coordinate Derivations and the Basis Theorem#^cor-27-7|Corollary §27.7: Consequences]]
- [[§33 Submanifolds#^prop-33-8|Proposition §33.8: The Old and New Versions Agree]]

## Connections
- **Used for.** It lets the geometric tangent spaces computed in §23 serve as abstract ones, e.g. T_I O(n) = Skew(n) ([[§23 The Geometric Tangent Space#^ex-23-2|Ex. §23.2]]) and the table of [[§23 The Geometric Tangent Space#^thm-23-5|§23.5]]. It gives part (2) of [[§33 Submanifolds#^prop-33-8|§33.8]]: for a regular level set S, the submanifold tangent space ι_*(T_pS) is ker F′(p). Read through curves, it says the geometric and the abstract velocity of a curve agree ([[§29 Tangent Vectors as Velocities of Curves#^rem-29-1|The Two Faces Reconciled]]).
- **How it is proved.** v ↦ D_v is injective because D_v determines v ([[§23 The Geometric Tangent Space#^prop-23-9|§23.9]]). Surjectivity is never constructed: both sides have dimension n, by [[Geometric Tangent Space Is the Kernel of the Jacobian]] and the [[Basis Theorem for Tangent Spaces]], so the injective linear map is onto ([[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]). The proof of [[§23 The Geometric Tangent Space#^thm-23-3|§23.3]] also gets one inclusion from a dimension count.
- **Same idea elsewhere.** In ℝⁿ the trade v ↔ D_v is the directional derivative of calculus, D_v g = Σ vⁱ ∂g/∂rⁱ ([[§28 The Differential in Coordinates#^prop-28-5|§28.5]]; the two-variable [[Directional Derivative Formula]] of 452).
- **Looking ahead (not yet announced in the course).** Whitney's embedding theorem puts every manifold inside some ℝᴺ, so every abstract tangent space can be realized as a subspace of ℝᴺ in this way.
