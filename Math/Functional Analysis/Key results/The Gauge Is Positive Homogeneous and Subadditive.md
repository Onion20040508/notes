---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 5.6", "Minkowski functional", "Lax §3.1, Thm 2"]
tags: [functional-analysis, hub]
---
![[§5 Convex Sets and the Gauge#^prop-5-6]]

## Treated in
- [[§5 Convex Sets and the Gauge#^prop-5-6|Proposition §5.6: The Gauge is Positive Homogeneous and Subadditive]], in [[§5 Convex Sets and the Gauge]]

## Its proof uses
- [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Definition §2.3: Convex Set]]
- [[§3 Statement and Motivation#^def-3-1|Definition §3.1: Positive Homogeneous; Subadditive]]
- [[§5 Convex Sets and the Gauge#^def-5-2|Definition §5.2: Gauge]]
- [[§5 Convex Sets and the Gauge#^prop-5-3|Proposition §5.3: The Gauge is Finite]]
- [[§5 Convex Sets and the Gauge#^prop-5-5|Proposition §5.5: Values of the Gauge]]

## Used in (Functional Analysis)
- [[§5 Convex Sets and the Gauge#^cor-5-8|Corollary §5.8: Convex Sets of Interior Points are Sublevel Sets]]
- [[§6 The Hyperplane Separation Theorem#^thm-6-1|Theorem §6.1: Hyperplane Separation; Geometric Hahn–Banach]]
- [[§8 Normed Linear Spaces#^prop-8-1|Proposition §8.1: Norms and Gauges]]

## Connections
- **How.** Homogeneity is bookkeeping: the admissible scales for bx are b times those for x. Subadditivity is convexity, used exactly once. If x/a and y/b lie in K, then (x + y)/(a + b) is their convex combination with weights a/(a + b) and b/(a + b), so a + b is admissible for x + y; then take infima. Finiteness of p_K ([[§5 Convex Sets and the Gauge#^prop-5-3|§5.3]], from 0 being interior) must come first. Even p(0) = 0 needs p to be finite ([[§3 Statement and Motivation#^lem-3-1|§3.1]]).
- **Used for.** It makes the gauge a legitimate p for the [[Hahn–Banach Theorem]], which is how the [[Hyperplane Separation Theorem]] is proved. With [[Interior Points via the Gauge]] it gives K = {p_K < 1} ([[§5 Convex Sets and the Gauge#^cor-5-8|§5.8]]). A norm is the gauge of its own unit ball ([[Norms Are Gauges]]).
- **Not more.** p_K ≥ 0, but it can vanish away from 0: the gauge of a half-plane is max{x₁, 0} ([[§5 Convex Sets and the Gauge#^ex-5-1|Ex. §5.1]]). It need not be symmetric either. It is a norm exactly when K contains no full ray and p_K(−x) = p_K(x) ([[Norms Are Gauges]]).
- **Same idea elsewhere.** The converse construction, a convex set {p < 1} from p, is [[§5 Convex Sets and the Gauge#^prop-5-1|§5.1]], so convex sets and these functions are two descriptions of one object. The gauge of the unit disk is the Euclidean norm ([[§5 Convex Sets and the Gauge#^ex-5-2|Ex. §5.2]]). A square of side 4 gives half the max norm ([[§5 Convex Sets and the Gauge#^ex-5-3|Ex. §5.3]]).
