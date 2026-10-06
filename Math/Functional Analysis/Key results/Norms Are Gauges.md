---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 11.1"]
tags: [functional-analysis, hub]
---
![[§11 Normed Linear Spaces#^prop-11-1]]

## Treated in
- [[§11 Normed Linear Spaces#^prop-11-1|Proposition §11.1: Norms and Gauges]], in [[§11 Normed Linear Spaces]]

## Its proof uses
- [[§5 Statement and Motivation#^def-5-1|Definition §5.1: Positive Homogeneous]]
- [[§5 Statement and Motivation#^def-5-2|Definition §5.2: Subadditive]]
- [[§7 Convex Sets and the Gauge#^def-7-1|Definition §7.1: Interior Point]]
- [[§7 Convex Sets and the Gauge#^prop-7-1|Proposition §7.1: Positive Homogeneous Subadditive p Gives a Convex Set]]
- [[§7 Convex Sets and the Gauge#^def-7-2|Definition §7.2: Gauge]]
- [[§7 Convex Sets and the Gauge#^prop-7-5|Proposition §7.5: Values of the Gauge]]
- [[§7 Convex Sets and the Gauge#^prop-7-6|Proposition §7.6: The Gauge is Positive Homogeneous and Subadditive]]
- [[§11 Normed Linear Spaces#^def-11-1|Definition §11.1: Norm; Normed Linear Space]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** (a) is immediate. In (b), the unit ball is convex by [[§7 Convex Sets and the Gauge#^prop-7-1|§7.1]], 0 is interior with ε(y) = 1/(‖y‖ + 1), and the admissible scales are (‖x‖, ∞) or [‖x‖, ∞), so p_K = ‖·‖. In (c), positivity of p_K fails exactly when K contains a full ray ([[§7 Convex Sets and the Gauge#^prop-7-5|§7.5]](c)), and symmetry p_K(−x) = p_K(x), for instance from K = −K, upgrades positive homogeneity to homogeneity.
- **Fails without symmetry.** The converse of (a) is false. p(x) = max{x, 0} + 2 max{−x, 0} on ℝ is positive homogeneous, subadditive and vanishes only at 0, but p(1) ≠ p(−1) ([[§11 Normed Linear Spaces#^rem-11-2|Remark §11]]). The gauge of a half-plane, max{x₁, 0}, vanishes on a whole half-plane ([[§7 Convex Sets and the Gauge#^ex-7-1|Ex. §7.1]]).
- **Used for.** By (a), every [[Hahn–Banach Theorem]] statement applies with p = ‖·‖ or p = C‖·‖ ([[§11 Normed Linear Spaces#^rem-11-2|Remark §11]]). By (b) and (c), norms on a real space correspond to symmetric convex sets with 0 interior and no full ray, and the unit ball is the picture of the norm.
- **Same idea elsewhere.** The disk, square and diamond are the unit balls of ‖·‖₂, ‖·‖∞ and ‖·‖₁, and each norm is the gauge of its ball ([[§7 Convex Sets and the Gauge#^ex-7-2|Ex. §7.2]]). The same balls appear in 551 ([[§34 Normed Linear Spaces and Lᵖ Spaces#^ex-34-2|551 Ex. §34.2]]). Comparing norms is comparing balls: equivalent norms squeeze each ball between scaled copies of the other ([[§14 New Normed Spaces from Old#^def-14-1|Def. §14.1]]), and the ℓᵖ balls grow with p ([[§18 Minkowski's Inequality and the Spaces ℓᵖ#^prop-18-4|§18.4]]).
