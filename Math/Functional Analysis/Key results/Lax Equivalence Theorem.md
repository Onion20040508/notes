---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 42.8", "consistency plus stability equals convergence", "Lax §34.3, Thm 8"]
tags: [functional-analysis, hub]
---
![[§42 Uniform Boundedness and Approximation#^thm-42-9]]

## Treated in
- [[§42 Uniform Boundedness and Approximation#^thm-42-9|Theorem §42.9: Lax Equivalence Theorem]], in [[§42 Uniform Boundedness and Approximation]]

## Its proof uses
- [[§39 Solving Mx = y#^thm-39-2|Theorem §39.2: Banach's Inverse Mapping Theorem]]
- [[§42 Uniform Boundedness and Approximation#^thm-42-6|Theorem §42.6: Uniform Boundedness Principle]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **What it says.** To solve $Tx = y$ approximately, solve $T_n x_n = y$. Consistency ($T_n x \to Tx$ for each $x$) plus stability ($\sup_n \|T_n^{-1} y\| < \infty$ for each $y$) is equivalent to convergence ($T_n^{-1} y \to T^{-1} y$) ([[§42 Uniform Boundedness and Approximation#^rem-42-4|Remark: Consistency + Stability = Convergence]]).
- **How.** ($\Rightarrow$) A convergent sequence is bounded. ($\Leftarrow$) [[Banach's Inverse Mapping Theorem]] makes each $T_n^{-1}$ bounded, the [[Uniform Boundedness Principle]] turns pointwise stability into $\sup_n \|T_n^{-1}\| < \infty$, and the identity $T_n^{-1} - T^{-1} = T_n^{-1}(T - T_n)T^{-1}$ transfers consistency at the single point $T^{-1}y$ to convergence at $y$ ([[Functional Analysis Problem-Solving Techniques#^rem-t28|Technique 28]]).
- **In Lax.** Lax's theorem (§34.3) is for difference approximations of a semigroup; the lecture's version is the same argument for equations $T_n x = y$.
