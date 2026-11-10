---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 43.5", "separation of a closed convex set", "Lax §8.4, in the proof of Thm 17"]
tags: [functional-analysis, hub]
---
![[§43 Weak and Weak-Star Convergence#^thm-43-5]]

## Treated in
- [[§43 Weak and Weak-Star Convergence#^thm-43-5|Theorem §43.5: Hyperplane Separation in a Normed Space]], in [[§43 Weak and Weak-Star Convergence]]

## Its proof uses
- [[§8 The Hyperplane Separation Theorem#^thm-8-1|Theorem §8.1: Hyperplane Separation; Geometric Hahn–Banach]]
- [[§11 Normed Linear Spaces#^prop-11-9|Proposition §11.9: Metric Interior Points are Interior Points]]

## Used in (Functional Analysis)
- [[§43 Weak and Weak-Star Convergence#^cor-43-6|Corollary §43.6: Hyperplane Separation over ℂ]]
- [[§43 Weak and Weak-Star Convergence#^thm-43-7|Theorem §43.7: Mazur's Theorem]]

## Connections
- **How.** Since $K$ is closed, $x_0$ is at positive distance $d$ from it. Fatten $K$ to $K_\varepsilon = \{x : \operatorname{dist}(x, K) < \varepsilon\}$ with $\varepsilon < d$: it is convex, all its points are interior, and it still misses $x_0$ ([[Functional Analysis Problem-Solving Techniques#^rem-t30|Technique 30]]). The algebraic [[Hyperplane Separation Theorem]] separates $x_0$ from $K_\varepsilon$; a metric interior point is an interior point in the algebraic sense ([[§11 Normed Linear Spaces#^prop-11-9|§11.9]]). The room $\varepsilon$ makes the functional bounded and the separation strict. The proof was left to the class in Lecture 18.
- **What is new.** The functional is in $X'$ and the inequalities are strict. The earlier theorem needed no topology and gave only $\ell(y_0) = 1$, $\ell < 1$ on $K$.
- **Over $\mathbb{C}$.** The same with real parts ([[§43 Weak and Weak-Star Convergence#^cor-43-6|§43.6]]).
- **Used for.** [[Mazur's Theorem]]. The case of a closed subspace is [[§36 Duality in Normed Spaces#^cor-36-11|§36.11]], obtained there from the distance formula.
- **With an inner product.** In a Hilbert space the functional can be written down: with $y_0$ the point of $K$ closest to $x_0$ ([[Closest Point in a Closed Convex Set]]), $\ell = \operatorname{Re}(\cdot, x_0 - y_0)$ separates (not proved in these notes). In a normed space there is no closest point to use, and Hahn–Banach replaces it.
