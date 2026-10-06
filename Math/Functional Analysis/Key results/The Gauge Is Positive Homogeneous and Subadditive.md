---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 7.6", "Minkowski functional", "Lax §3.1, Thm 2"]
tags: [functional-analysis, hub]
---
![[§7 Convex Sets and the Gauge#^prop-7-6]]

## Treated in
- [[§7 Convex Sets and the Gauge#^prop-7-6|Proposition §7.6: The Gauge is Positive Homogeneous and Subadditive]], in [[§7 Convex Sets and the Gauge]]

## Its proof uses
- [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-3|Definition §3.3: Convex Set]]
- [[§5 Statement and Motivation#^def-5-1|Definition §5.1: Positive Homogeneous]]
- [[§5 Statement and Motivation#^def-5-2|Definition §5.2: Subadditive]]
- [[§7 Convex Sets and the Gauge#^def-7-2|Definition §7.2: Gauge]]
- [[§7 Convex Sets and the Gauge#^prop-7-3|Proposition §7.3: The Gauge is Finite]]
- [[§7 Convex Sets and the Gauge#^prop-7-5|Proposition §7.5: Values of the Gauge]]

## Used in (Functional Analysis)
- [[§7 Convex Sets and the Gauge#^cor-7-8|Corollary §7.8: Convex Sets of Interior Points are Sublevel Sets]]
- [[§8 The Hyperplane Separation Theorem#^thm-8-1|Theorem §8.1: Hyperplane Separation; Geometric Hahn–Banach]]
- [[§11 Normed Linear Spaces#^prop-11-1|Proposition §11.1: Norms and Gauges]]

## Connections
- **How.** Homogeneity is bookkeeping: the admissible scales for bx are b times those for x. Subadditivity is convexity, used exactly once. If x/a and y/b lie in K, then (x + y)/(a + b) is their convex combination with weights a/(a + b) and b/(a + b), so a + b is admissible for x + y; then take infima. Finiteness of p_K ([[§7 Convex Sets and the Gauge#^prop-7-3|§7.3]], from 0 being interior) must come first. Even p(0) = 0 needs p to be finite ([[§5 Statement and Motivation#^lem-5-1|§5.1]]).
- **Used for.** It makes the gauge a legitimate p for the [[Hahn–Banach Theorem]], which is how the [[Hyperplane Separation Theorem]] is proved. With [[Interior Points via the Gauge]] it gives K = {p_K < 1} ([[§7 Convex Sets and the Gauge#^cor-7-8|§7.8]]). A norm is the gauge of its own unit ball ([[Norms Are Gauges]]).
- **Not more.** p_K ≥ 0, but it can vanish away from 0: the gauge of a half-plane is max{x₁, 0} ([[§7 Convex Sets and the Gauge#^ex-7-1|Ex. §7.1]]). It need not be symmetric either. It is a norm exactly when K contains no full ray and p_K(−x) = p_K(x) ([[Norms Are Gauges]]).
- **Same idea elsewhere.** The converse construction, a convex set {p < 1} from p, is [[§7 Convex Sets and the Gauge#^prop-7-1|§7.1]], so convex sets and these functions are two descriptions of one object. The gauge of the unit disk is the Euclidean norm ([[§7 Convex Sets and the Gauge#^ex-7-2|Ex. §7.2]]). A square of side 4 gives half the max norm ([[§7 Convex Sets and the Gauge#^ex-7-3|Ex. §7.3]]).
