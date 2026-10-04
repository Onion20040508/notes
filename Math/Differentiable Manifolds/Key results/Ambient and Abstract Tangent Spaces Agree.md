---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 24.6", "v ↦ D_v", "Lee Proposition 3.2", "Lee Proposition 5.37", "Lee Proposition 5.38"]
tags: [differentiable-manifolds, hub]
---
![[§24 Coordinate Derivations and the Basis Theorem#^thm-24-6]]

## Treated in
- [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-6|Theorem §24.6: Ambient and Abstract Agree]], in [[§24 Coordinate Derivations and the Basis Theorem]]

## Its proof uses
- [[§20 Tangent Spaces I꞉ The Geometric Picture#^def-20-1|Definition §20.1: Geometric Tangent Space]]
- [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-3|Theorem §20.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§22 Tangent Spaces II꞉ Germs#^def-22-1|Definition §22.1: The Directional Derivative Attached to a Tangent Vector]]
- [[§22 Tangent Spaces II꞉ Germs#^prop-22-1|Proposition §22.1: Basic Properties of D_v]]
- [[§22 Tangent Spaces II꞉ Germs#^prop-22-2|Proposition §22.2: D_v Determines v]]
- [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|Theorem §24.5: Basis Theorem]]

## Used in (Differentiable Manifolds)
- [[§24 Coordinate Derivations and the Basis Theorem#^cor-24-7|Corollary §24.7: Consequences]]
- [[§30 Submanifolds#^prop-30-8|Proposition §30.8: The Old and New Versions Agree]]

## Connections
- **Used for.** It lets the geometric tangent spaces computed in §20 serve as abstract ones, e.g. T_I O(n) = Skew(n) ([[§20 Tangent Spaces I꞉ The Geometric Picture#^ex-20-2|Ex. §20.2]]) and the table of [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5|§20.5]]. It gives part (2) of [[§30 Submanifolds#^prop-30-8|§30.8]]: for a regular level set S, the submanifold tangent space ι_*(T_pS) is ker F′(p). Read through curves, it says the geometric and the abstract velocity of a curve agree ([[§26 Tangent Vectors as Velocities of Curves#^rem-26-1|The Two Faces Reconciled]]).
- **How it is proved.** v ↦ D_v is injective because D_v determines v ([[§22 Tangent Spaces II꞉ Germs#^prop-22-2|§22.2]]). Surjectivity is never constructed: both sides have dimension n, by [[Geometric Tangent Space Is the Kernel of the Jacobian]] and the [[Basis Theorem for Tangent Spaces]], so the injective linear map is onto ([[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]). The proof of [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-3|§20.3]] also gets one inclusion from a dimension count.
- **Same idea elsewhere.** In ℝⁿ the trade v ↔ D_v is the directional derivative of calculus, D_v g = Σ vⁱ ∂g/∂rⁱ ([[§25 The Differential in Coordinates#^prop-25-5|§25.5]]; the two-variable [[Directional Derivative Formula]] of 452).
- **Looking ahead (not yet announced in the course).** Whitney's embedding theorem puts every manifold inside some ℝᴺ, so every abstract tangent space can be realized as a subspace of ℝᴺ in this way.
