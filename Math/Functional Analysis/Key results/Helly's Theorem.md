---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 44.1", "weak-star sequential compactness", "Lax §10.3, Thm 12"]
tags: [functional-analysis, hub]
---
![[§44 Weak Sequential Compactness#^thm-44-1]]

## Treated in
- [[§44 Weak Sequential Compactness#^thm-44-1|Theorem §44.1: Helly's Theorem]], in [[§44 Weak Sequential Compactness]]

## Its proof uses
- [[§30 Boundedness and Continuity#^prop-30-1|Proposition §30.1: The Operator Norm]]
- [[§42 Uniform Boundedness and Approximation#^prop-42-8|Proposition §42.8: Banach–Steinhaus Without a Given Limit]]
- [[§43 Weak and Weak-Star Convergence#^def-43-2|Definition §43.2: Weak-ast Convergence]]

## Its proof uses (other subjects)
- [[Bolzano–Weierstrass Theorem]] (Single Variable Analysis)

## Used in (Functional Analysis)
- [[§44 Weak Sequential Compactness#^cor-44-2|Corollary §44.2: Closed Balls in the Dual of a Separable Space]]
- [[§44 Weak Sequential Compactness#^thm-44-4|Theorem §44.4: Eberlein's Theorem]]

## Connections
- **What it says.** If $X$ is separable, a bounded sequence in $X'$ has a subsequence that converges in the weak-$\ast$ sense, and the limit is no larger in norm than the bound. So closed balls of $X'$ are weak-$\ast$ sequentially compact ([[§44 Weak Sequential Compactness#^cor-44-2|Cor. §44.2]]).
- **How.** A diagonal process ([[Functional Analysis Problem-Solving Techniques#^rem-t31|T31]]) makes a subsequence converge at every point of a countable dense set, one [[Bolzano–Weierstrass Theorem]] extraction per point. The uniform bound carries the convergence to all of $X$, and the pointwise limit is linear and bounded.
- **Why the hypotheses.** Separability supplies the countable dense set; for $X = \ell^\infty$ the coordinate functionals have no weak-$\ast$ convergent subsequence ([[§44 Weak Sequential Compactness#^ex-44-2|Ex. §44.2]]). Completeness of $X$ is not used. The limit need not stay in a set that is only norm-closed and convex ([[§44 Weak Sequential Compactness#^ex-44-1|Ex. §44.1]]).
- **Used for.** [[Eberlein's Theorem]], by applying it to $X'$ when $X$ is reflexive.
- **Without separability.** [[Alaoglu's Theorem]]: compactness of the ball in the weak-$\ast$ topology, with no statement about subsequences.
- **In Lax.** §10.3, Thm 12, for a separable Banach space; the name of Helly is Lax's.
