---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 6.7", "Lax §3.1, Thm 3"]
tags: [functional-analysis, hub]
---
![[§6 Convex Sets and the Gauge#^prop-6-7]]

## Treated in
- [[§6 Convex Sets and the Gauge#^prop-6-7|Proposition §6.7: Interior Points of K are Exactly p_K < 1]], in [[§6 Convex Sets and the Gauge]]

## Its proof uses
- [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Definition §2.3: Convex Set]]
- [[§6 Convex Sets and the Gauge#^def-6-1|Definition §6.1: Interior Point]]
- [[§6 Convex Sets and the Gauge#^def-6-2|Definition §6.2: Gauge]]

## Used in (Functional Analysis)
- [[§6 Convex Sets and the Gauge#^cor-6-8|Corollary §6.8: Convex Sets of Interior Points are Sublevel Sets]]

## Connections
- **How.** (⇒) Push x outward along its own ray. Since (1 + b)x ∈ K for small b > 0, p_K(x) ≤ 1/(1 + b) < 1. (⇐) If x/a ∈ K with a < 1, the triangle with apex x/a and base the segment {ty : |t| < δ(y)} through 0 lies in K by convexity. Its cross-section through x gives room (1 − a)δ(y) in the direction y. Both hypotheses on K are used: convexity, and 0 interior for the base segment.
- **Used for.** By [[§6 Convex Sets and the Gauge#^cor-6-8|§6.8]], the convex sets all of whose points are interior are exactly the sublevel sets {p < 1}, and each is recovered from its own gauge; the other direction is [[§6 Convex Sets and the Gauge#^prop-6-2|§6.2]]. This is the form the [[Hyperplane Separation Theorem]] uses: y₀ ∉ K forces p_K(y₀) ≥ 1. With [[The Gauge Is Positive Homogeneous and Subadditive]] and [[§6 Convex Sets and the Gauge#^prop-6-1|§6.1]], it completes the correspondence between convex sets and positive homogeneous subadditive functions.
- **Same idea elsewhere.** The interior point here is algebraic: it can move a little along each line. The topological interior asks for an open set instead ([[§7 Interior and Closure#^def-7-1|590 Def. §7.1]]). In a normed space a metric interior point is interior in this sense ([[§10 Normed Linear Spaces#^prop-10-7|§10.7]]). The converse fails for ℝ² minus the points (s, s²), s ≠ 0, which is not convex ([[§10 Normed Linear Spaces#^ex-10-2|Ex. §10.2]]): the parabola approaches 0 along no single line.
