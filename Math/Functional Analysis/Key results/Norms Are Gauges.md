---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 8.1"]
tags: [functional-analysis, hub]
---
![[§8 Normed Linear Spaces#^prop-8-1]]

## Treated in
- [[§8 Normed Linear Spaces#^prop-8-1|Proposition §8.1: Norms and Gauges]], in [[§8 Normed Linear Spaces]]

## Its proof uses
- [[§3 Statement and Motivation#^def-3-1|Definition §3.1: Positive Homogeneous; Subadditive]]
- [[§5 Convex Sets and the Gauge#^def-5-1|Definition §5.1: Interior Point]]
- [[§5 Convex Sets and the Gauge#^prop-5-1|Proposition §5.1: Positive Homogeneous Subadditive p Gives a Convex Set]]
- [[§5 Convex Sets and the Gauge#^def-5-2|Definition §5.2: Gauge]]
- [[§5 Convex Sets and the Gauge#^prop-5-5|Proposition §5.5: Values of the Gauge]]
- [[§5 Convex Sets and the Gauge#^prop-5-6|Proposition §5.6: The Gauge is Positive Homogeneous and Subadditive]]
- [[§8 Normed Linear Spaces#^def-8-1|Definition §8.1: Norm; Normed Linear Space]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** (a) is immediate. In (b), the unit ball is convex by [[§5 Convex Sets and the Gauge#^prop-5-1|§5.1]], 0 is interior with ε(y) = 1/(‖y‖ + 1), and the admissible scales are (‖x‖, ∞) or [‖x‖, ∞), so p_K = ‖·‖. In (c), positivity of p_K fails exactly when K contains a full ray ([[§5 Convex Sets and the Gauge#^prop-5-5|§5.5]](c)), and symmetry p_K(−x) = p_K(x), for instance from K = −K, upgrades positive homogeneity to homogeneity.
- **Fails without symmetry.** The converse of (a) is false. p(x) = max{x, 0} + 2 max{−x, 0} on ℝ is positive homogeneous, subadditive and vanishes only at 0, but p(1) ≠ p(−1) ([[§8 Normed Linear Spaces#^rem-8-2|Remark §8]]). The gauge of a half-plane, max{x₁, 0}, vanishes on a whole half-plane ([[§5 Convex Sets and the Gauge#^ex-5-1|Ex. §5.1]]).
- **Used for.** By (a), every [[Hahn–Banach Theorem]] statement applies with p = ‖·‖ or p = C‖·‖ ([[§8 Normed Linear Spaces#^rem-8-2|Remark §8]]). By (b) and (c), norms on a real space correspond to symmetric convex sets with 0 interior and no full ray, and the unit ball is the picture of the norm.
- **Same idea elsewhere.** The disk, square and diamond are the unit balls of ‖·‖₂, ‖·‖∞ and ‖·‖₁, and each norm is the gauge of its ball ([[§5 Convex Sets and the Gauge#^ex-5-2|Ex. §5.2]]). The same balls appear in 551 ([[§19 Normed Linear Spaces and Lᵖ Spaces#^ex-19-2|551 Ex. §19.2]]). Comparing norms is comparing balls: equivalent norms squeeze each ball between scaled copies of the other ([[§10 New Normed Spaces from Old#^def-10-1|Def. §10.1]]), and the ℓᵖ balls grow with p ([[§13 Minkowski's Inequality and the Spaces ℓᵖ#^prop-13-4|§13.4]]).
