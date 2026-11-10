---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 42.6", "Banach–Steinhaus", "Lax §15.2, Thm 6"]
tags: [functional-analysis, hub]
---
![[§42 Uniform Boundedness and Approximation#^thm-42-7]]

## Treated in
- [[§42 Uniform Boundedness and Approximation#^thm-42-7|Theorem §42.7: Banach–Steinhaus]], in [[§42 Uniform Boundedness and Approximation]]

## Its proof uses
- [[§42 Uniform Boundedness and Approximation#^thm-42-6|Theorem §42.6: Uniform Boundedness Principle]]

## Used in (Functional Analysis)
- [[§43 Weak and Weak-Star Convergence#^thm-43-3|Theorem §43.3: Criterion for Weak Convergence]]
- [[§43 Weak and Weak-Star Convergence#^thm-43-9|Theorem §43.9: Criterion for Weak-ast Convergence]]

## Connections
- **How.** ($\Rightarrow$) A convergent sequence $A_n x$ is bounded for each $x$, so the [[Uniform Boundedness Principle]] gives $\sup_n \|A_n\| < \infty$; this is where $X$ must be complete. ($\Leftarrow$) For $x$ near a point $y$ of the dense set, $\|A_n x - Ax\| \le \|A_n y - Ay\| + M\|x - y\|$: an $\varepsilon/2$ argument ([[Functional Analysis Problem-Solving Techniques#^rem-t19|Technique 19]]). Which hypotheses each direction uses: [[§42 Uniform Boundedness and Approximation#^rem-42-3|Remark: Which Hypotheses Each Direction Uses]].
- **Without a given limit.** If the target is complete, a uniform bound and convergence on a dense set already produce the limit map ([[§42 Uniform Boundedness and Approximation#^prop-42-8|§42.8]]).
- **Used for.** The criteria for weak and weak-$\ast$ convergence: view $x_n$ as maps on the Banach space $X'$ ([[Criterion for Weak Convergence]], [[Functional Analysis Problem-Solving Techniques#^rem-t29|Technique 29]]), or $\ell_n$ as maps on $X$ ([[§43 Weak and Weak-Star Convergence#^thm-43-9|§43.9]], which needs $X$ complete). With it, $\sin(mx) \rightharpoonup 0$ in $L^p$ follows from the case of continuous test functions ([[§43 Weak and Weak-Star Convergence#^ex-43-3|Ex. §43.3]]).
- **Same idea elsewhere.** In the QFT notes, a pointwise limit of tempered distributions is again a tempered distribution; the continuity of the limit is quoted from the uniform boundedness principle on the space of test functions ([[§CA.2 Generalized Functions#^thm-ca-2-5|QFT Theorem §CA.2.5]], part 1). That space is not normed, so the statement there is a relative of this theorem, not a case of it.
