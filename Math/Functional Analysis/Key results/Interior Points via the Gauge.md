---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 5.7", "Lax §3.1, Thm 3"]
tags: [functional-analysis, hub]
---
![[§5 Convex Sets and the Gauge#^prop-5-7]]

## Treated in
- [[§5 Convex Sets and the Gauge#^prop-5-7|Proposition §5.7: Interior Points of K are Exactly p_K < 1]], in [[§5 Convex Sets and the Gauge]]

## Its proof uses
- [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Definition §2.3: Convex Set]]
- [[§5 Convex Sets and the Gauge#^def-5-1|Definition §5.1: Interior Point]]
- [[§5 Convex Sets and the Gauge#^def-5-2|Definition §5.2: Gauge]]

## Used in (Functional Analysis)
- [[§5 Convex Sets and the Gauge#^cor-5-8|Corollary §5.8: Convex Sets of Interior Points are Sublevel Sets]]

## Connections
- **How.** (⇒) Push x outward along its own ray. Since (1 + b)x ∈ K for small b > 0, p_K(x) ≤ 1/(1 + b) < 1. (⇐) If x/a ∈ K with a < 1, the triangle with apex x/a and base the segment {ty : |t| < δ(y)} through 0 lies in K by convexity. Its cross-section through x gives room (1 − a)δ(y) in the direction y. Both hypotheses on K are used: convexity, and 0 interior for the base segment.
- **Used for.** By [[§5 Convex Sets and the Gauge#^cor-5-8|§5.8]], the convex sets all of whose points are interior are exactly the sublevel sets {p < 1}, and each is recovered from its own gauge; the other direction is [[§5 Convex Sets and the Gauge#^prop-5-2|§5.2]]. This is the form the [[Hyperplane Separation Theorem]] uses: y₀ ∉ K forces p_K(y₀) ≥ 1. With [[The Gauge Is Positive Homogeneous and Subadditive]] and [[§5 Convex Sets and the Gauge#^prop-5-1|§5.1]], it completes the correspondence between convex sets and positive homogeneous subadditive functions.
- **Same idea elsewhere.** The interior point here is algebraic: it can move a little along each line. The topological interior asks for an open set instead ([[§7 Interior and Closure#^def-7-1|590 Def. §7.1]]). In a normed space a metric interior point is interior in this sense ([[§8 Normed Linear Spaces#^prop-8-7|§8.7]]). The converse fails for ℝ² minus the points (s, s²), s ≠ 0, which is not convex ([[§8 Normed Linear Spaces#^ex-8-2|Ex. §8.2]]): the parabola approaches 0 along no single line.
