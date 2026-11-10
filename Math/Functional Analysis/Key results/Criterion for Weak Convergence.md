---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 43.3", "weak convergence criterion", "Lax §10.1, Thm 1"]
tags: [functional-analysis, hub]
---
![[§43 Weak and Weak-Star Convergence#^thm-43-3]]

## Treated in
- [[§43 Weak and Weak-Star Convergence#^thm-43-3|Theorem §43.3: Criterion for Weak Convergence]], in [[§43 Weak and Weak-Star Convergence]]

## Its proof uses
- [[§31 Dual Spaces#^cor-31-1|Corollary §31.1: The Dual is Always a Banach Space]]
- [[§37 Separable Duals and Reflexive Spaces#^prop-37-5|Proposition §37.5: The Canonical Embedding X → X'']]
- [[§42 Uniform Boundedness and Approximation#^thm-42-7|Theorem §42.7: Banach–Steinhaus]]

## Used in (Functional Analysis)
- [[§43 Weak and Weak-Star Convergence#^thm-43-4|Theorem §43.4: The Norm of a Weak Limit]]

## Connections
- **How.** Regard each $x_n$ as a bounded linear functional on $X'$, with the same norm ([[§37 Separable Duals and Reflexive Spaces#^prop-37-5|§37.5]]). $X'$ is always a Banach space ([[§31 Dual Spaces#^cor-31-1|§31.1]]), so the [[Banach–Steinhaus Theorem]] applies there even when $X$ is not complete: pointwise convergence on $X'$ is the same as a uniform bound plus convergence on a dense set of functionals ([[Functional Analysis Problem-Solving Techniques#^rem-t29|Technique 29]]).
- **Used for.** Weakly convergent sequences are bounded, and $\|x_0\| \le \liminf \|x_n\|$ ([[§43 Weak and Weak-Star Convergence#^thm-43-4|§43.4]]). To prove weak convergence it is enough to test on a convenient dense set: continuous functions in $L^{p'}$ give $\sin(mx) \rightharpoonup 0$ in $L^p$, $1 < p < \infty$ ([[§43 Weak and Weak-Star Convergence#^ex-43-3|Ex. §43.3]]).
- **Weak-$\ast$ version.** The same statement for functionals $\ell_n$ tested on a dense subset of $X$ ([[§43 Weak and Weak-Star Convergence#^thm-43-9|§43.9]]) needs $X$ complete, because now Banach–Steinhaus is applied on $X$ itself ([[§43 Weak and Weak-Star Convergence#^rem-43-1|Remark: The Weak-∗ Criteria Need X Complete]], [[§43 Weak and Weak-Star Convergence#^ex-43-7|Ex. §43.7]]).
- **Same idea elsewhere.** For $\sin(ny)$ and $\cos(ny)$ on $[-\pi, \pi]$ the convergence on the test functions is the simplest case of the Riemann–Lebesgue lemma ([[§16★ Proof of Convergence#^lem-16-3|341 Lemma §16.3]]); in $L^2$ it is Bessel's inequality for an orthonormal sequence ([[§43 Weak and Weak-Star Convergence#^prop-43-2|§43.2]], [[Bessel's Inequality]]).
- **Finite dimensions.** Weak and strong convergence agree there, since the coordinates are bounded functionals; the notion is new only in infinite dimensions, where it replaces the lost compactness of the unit ball ([[The Unit Ball of an Infinite-Dimensional Space Is Not Compact]]).
