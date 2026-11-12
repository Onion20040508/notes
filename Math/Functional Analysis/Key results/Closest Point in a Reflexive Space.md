---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 44.10", "Lax §10.2, Thm 10"]
tags: [functional-analysis, hub]
---
![[§44 Weak Sequential Compactness#^thm-44-10]]

## Treated in
- [[§44 Weak Sequential Compactness#^thm-44-10|Theorem §44.10: Closest Point in a Closed Convex Subset of a Reflexive Space]], in [[§44 Weak Sequential Compactness]]

## Its proof uses
- [[§43 Weak and Weak-Star Convergence#^thm-43-4|Theorem §43.4: The Norm of a Weak Limit]]
- [[§43 Weak and Weak-Star Convergence#^thm-43-7|Theorem §43.7: Mazur's Theorem]]
- [[§44 Weak Sequential Compactness#^thm-44-4|Theorem §44.4: Eberlein's Theorem]]
- [[§44 Weak Sequential Compactness#^cor-44-7|Corollary §44.7: Bounded Closed Convex Sets in a Reflexive Space]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **What it says.** In a reflexive Banach space every nonempty closed convex set contains a point closest to any given point. Existence only: the point need not be unique ([[§44 Weak Sequential Compactness#^ex-44-3|Ex. §44.3]]).
- **How.** A minimizing sequence is bounded; [[Eberlein's Theorem]] gives a weakly convergent subsequence; [[Mazur's Theorem]] keeps the limit in the closed convex set; the norm of a weak limit is at most the $\liminf$ of the norms ([[§43 Weak and Weak-Star Convergence#^thm-43-4|§43.4]]). This is technique [[Functional Analysis Problem-Solving Techniques#^rem-t32|T32]].
- **Why the hypotheses.** Without reflexivity the distance need not be attained: in $C[0,1]$ a closed hyperplane has no point closest to $0$ ([[§44 Weak Sequential Compactness#^ex-44-4|Ex. §44.4]]).
- **In Hilbert space.** [[Closest Point in a Closed Convex Set]]: there the parallelogram law makes the minimizing sequence Cauchy, and the closest point is unique.
- **In Lax.** §10.2, Thm 10; Lax also proves existence and uniqueness in uniformly convex spaces (§5.2, Thm 8), not covered.
