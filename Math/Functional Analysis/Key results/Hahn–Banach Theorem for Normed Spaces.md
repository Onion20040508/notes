---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 36.1", "norm-preserving extension", "normed Hahn-Banach"]
tags: [functional-analysis, hub]
---
![[§36 Duality in Normed Spaces#^thm-36-1]]

## Treated in
- [[§36 Duality in Normed Spaces#^thm-36-1|Theorem §36.1: Hahn–Banach for Normed Spaces]], in [[§36 Duality in Normed Spaces]]

## Its proof uses
- [[§5 Statement and Motivation#^thm-5-3|Theorem §5.3: Hahn–Banach]]
- [[§9 The Complex Hahn–Banach Theorem#^thm-9-2|Theorem §9.2: Complex Hahn–Banach]]

## Used in (Functional Analysis)
- [[§36 Duality in Normed Spaces#^ex-36-2|Example §36.2: (ℓ^∞)' is Larger than ell¹]]
- [[§36 Duality in Normed Spaces#^thm-36-2|Theorem §36.2: The Norm as a Maximum over the Dual]]
- [[§36 Duality in Normed Spaces#^thm-36-10|Theorem §36.10: Distance to a Subspace]]
- [[§37 Separable Duals and Reflexive Spaces#^thm-37-8|Theorem §37.8: Closed Subspaces of Reflexive Spaces are Reflexive]]
- [[§37 Separable Duals and Reflexive Spaces#^prop-37-10|Proposition §37.10: Distance from a Functional to Y^perp]]
- [[§37 Separable Duals and Reflexive Spaces#^cor-37-11|Corollary §37.11: The Dual of a Subspace: Y' ≅ X'/Y^perp]]

## Connections
- **How.** Apply the [[Hahn–Banach Theorem]] with $p(x) = \|\ell\|_Y \|x\|$, which is positive homogeneous and subadditive ([[Norms Are Gauges]]) and dominates $\ell$ on $Y$. The extension satisfies $L \le p$, and applying this to $-x$ gives $|L(x)| \le \|\ell\|_Y\|x\|$. Over $\mathbb{C}$ use the [[Complex Hahn–Banach Theorem]], whose hypothesis $p(ax) = |a|p(x)$ a norm satisfies.
- **What is new.** The extension keeps the norm. It is usually not unique.
- **Used for.** It is the source of every bounded functional the course constructs on a general normed space, always by the same recipe: define the functional on a small subspace, check its norm there, extend ([[Functional Analysis Problem-Solving Techniques#^rem-t22|Technique 22]]). This gives [[The Norm as a Maximum over the Dual]], [[Distance to a Subspace via Functionals]], a functional on $\ell^\infty$ that no $a \in \ell^1$ represents ([[§36 Duality in Normed Spaces#^ex-36-2|Ex. §36.2]]), the onto-ness of restriction $X' \to Y'$ in [[Closed Subspaces of Reflexive Spaces are Reflexive]] and in $Y' \cong X'/Y^\perp$ ([[§37 Separable Duals and Reflexive Spaces#^cor-37-11|§37.11]]).
- **Not needed.** The dual of a quotient, $(X/Y)' \cong Y^\perp$, is proved without it ([[§36 Duality in Normed Spaces#^rem-36-8|Remark: No Hahn–Banach Needed Here]]). On a Hilbert space a bounded functional on a closed subspace is $(\cdot, a)$ with $a$ in the subspace ([[Riesz Representation Theorem (Hilbert spaces)]]), and the same formula extends it to the whole space with the same norm, with no appeal to Zorn.
- **Finite dimensions.** In LADR's duality, functionals on a subspace extend by extending a basis, and the annihilator has dimension $\dim V - \dim U$ ([[§12 Duality#^ladr-3-121|LADR 3.121]], [[§12 Duality#^ladr-3-125|LADR 3.125]]). No norm is involved there; the control of the norm is the content here.
