---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 10.1"]
tags: [functional-analysis, hub]
---
![[§10 Normed Linear Spaces#^prop-10-1]]

## Treated in
- [[§10 Normed Linear Spaces#^prop-10-1|Proposition §10.1: Norms and Gauges]], in [[§10 Normed Linear Spaces]]

## Its proof uses
- [[§4 Statement and Motivation#^def-4-1|Definition §4.1: Positive Homogeneous; Subadditive]]
- [[§6 Convex Sets and the Gauge#^def-6-1|Definition §6.1: Interior Point]]
- [[§6 Convex Sets and the Gauge#^prop-6-1|Proposition §6.1: Positive Homogeneous Subadditive p Gives a Convex Set]]
- [[§6 Convex Sets and the Gauge#^def-6-2|Definition §6.2: Gauge]]
- [[§6 Convex Sets and the Gauge#^prop-6-5|Proposition §6.5: Values of the Gauge]]
- [[§6 Convex Sets and the Gauge#^prop-6-6|Proposition §6.6: The Gauge is Positive Homogeneous and Subadditive]]
- [[§10 Normed Linear Spaces#^def-10-1|Definition §10.1: Norm; Normed Linear Space]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** (a) is immediate. In (b), the unit ball is convex by [[§6 Convex Sets and the Gauge#^prop-6-1|§6.1]], 0 is interior with ε(y) = 1/(‖y‖ + 1), and the admissible scales are (‖x‖, ∞) or [‖x‖, ∞), so p_K = ‖·‖. In (c), positivity of p_K fails exactly when K contains a full ray ([[§6 Convex Sets and the Gauge#^prop-6-5|§6.5]](c)), and symmetry p_K(−x) = p_K(x), for instance from K = −K, upgrades positive homogeneity to homogeneity.
- **Fails without symmetry.** The converse of (a) is false. p(x) = max{x, 0} + 2 max{−x, 0} on ℝ is positive homogeneous, subadditive and vanishes only at 0, but p(1) ≠ p(−1) ([[§10 Normed Linear Spaces#^rem-10-2|Remark §10]]). The gauge of a half-plane, max{x₁, 0}, vanishes on a whole half-plane ([[§6 Convex Sets and the Gauge#^ex-6-1|Ex. §6.1]]).
- **Used for.** By (a), every [[Hahn–Banach Theorem]] statement applies with p = ‖·‖ or p = C‖·‖ ([[§10 Normed Linear Spaces#^rem-10-2|Remark §10]]). By (b) and (c), norms on a real space correspond to symmetric convex sets with 0 interior and no full ray, and the unit ball is the picture of the norm.
- **Same idea elsewhere.** The disk, square and diamond are the unit balls of ‖·‖₂, ‖·‖∞ and ‖·‖₁, and each norm is the gauge of its ball ([[§6 Convex Sets and the Gauge#^ex-6-2|Ex. §6.2]]). The same balls appear in 551 ([[§19 Normed Linear Spaces and Lᵖ Spaces#^ex-19-2|551 Ex. §19.2]]). Comparing norms is comparing balls: equivalent norms squeeze each ball between scaled copies of the other ([[§12 New Normed Spaces from Old#^def-12-1|Def. §12.1]]), and the ℓᵖ balls grow with p ([[§16 Minkowski's Inequality and the Spaces ℓᵖ#^prop-16-4|§16.4]]).
