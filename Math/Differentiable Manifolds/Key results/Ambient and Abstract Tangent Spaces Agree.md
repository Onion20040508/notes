---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 12.8", "v ↦ D_v"]
tags: [differentiable-manifolds, hub]
---
![[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8]]

## Treated in
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8|Theorem §12.8: Ambient and Abstract Agree]], in [[§12 Tangent Spaces II꞉ The Abstract Tangent Space]]

## Its proof uses
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1|Definition §11.1: Geometric Tangent Space]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|Theorem §11.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-1|Proposition §12.1: Basic Properties of D_v]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-1|Definition §12.1: The Directional Derivative Attached to a Tangent Vector]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-2|Proposition §12.2: D_v Determines v]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|Theorem §12.16: Basis Theorem]]

## Used in (Differentiable Manifolds)
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-20|Corollary §12.20: Consequences]]
- [[§15 Submanifolds#^prop-15-8|Proposition §15.8: The Old and New Versions Agree]]

## Connections
- **Used for.** It lets the geometric tangent spaces computed in §11 serve as abstract ones, e.g. T_I O(n) = Skew(n) ([[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-2|Ex. §11.2]]) and the table of [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5|§11.5]]. It gives part (2) of [[§15 Submanifolds#^prop-15-8|§15.8]]: for a regular level set S, the submanifold tangent space ι_*(T_pS) is ker F′(p). Read through curves, it says the geometric and the abstract velocity of a curve agree ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^rem-12-16|The Two Faces Reconciled]]).
- **How it is proved.** v ↦ D_v is injective because D_v determines v ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-2|§12.2]]). Surjectivity is never constructed: both sides have dimension n, by [[Geometric Tangent Space Is the Kernel of the Jacobian]] and the [[Basis Theorem for Tangent Spaces]], so the injective linear map is onto ([[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]). The proof of [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|§11.3]] also gets one inclusion from a dimension count.
- **Same idea elsewhere.** In ℝⁿ the trade v ↔ D_v is the directional derivative of calculus, D_v g = Σ vⁱ ∂g/∂rⁱ ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-25|§12.25]]; the two-variable [[Directional Derivative Formula]] of 452).
- **Coming later in the course.** Whitney's embedding theorem puts every manifold inside some ℝᴺ, so every abstract tangent space can be realized as a subspace of ℝᴺ in this way.
