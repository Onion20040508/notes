---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 14.2", "Lagrange multipliers"]
tags: [multivariable-analysis, hub]
---
![[§14 Optimization and Lagrange Multipliers#^thm-14-2]]

## Treated in
- [[§14 Optimization and Lagrange Multipliers#^thm-14-2|Theorem §14.2: Method of Lagrange Multipliers]], in [[§14 Optimization and Lagrange Multipliers]]

## Its proof uses
- [[§10 Composition of Functions and the Chain Rule#^thm-10-2|Theorem §10.2: Multivariable Chain Rule]]
- [[§12 The Implicit Function Theorem#^thm-12-1|Theorem §12.1: Implicit Function Theorem]]

## Its proof uses (other subjects)
- [[§29 The Mean Value Theorem#^thm-29-1|451 §29.1: Interior Extremum Theorem]]

## Used in (Multivariable Analysis)
- (not cited later in the course)

## Connections
- **Proof idea.** Since g_y ≠ 0, the [[Implicit Function Theorem]] writes the constraint as y = α(x). Then F(x) = f(x, α(x)) has an extremum at x₀, so F′(x₀) = 0 by the 451 [[§29 The Mean Value Theorem#^thm-29-1|Interior Extremum Theorem]]. The [[Multivariable Chain Rule]] turns this into f_x g_y = f_y g_x.
- **Where hypotheses matter.** The constraint qualification ∇g ≠ 0 is exactly the IFT hypothesis ([[§14 Optimization and Lagrange Multipliers#^rem-14-2|The Constraint Qualification]]). Without a constraint, the method reduces to [[§14 Optimization and Lagrange Multipliers#^thm-14-1|Fermat's theorem in ℝⁿ]].
- **Linear algebra.** With k constraints ([[§14 Optimization and Lagrange Multipliers#^thm-14-3|Theorem §14.3]]), ∇f lies in the orthogonal complement of the constraint set's tangent space ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-46|LADR 6.46]]). That complement has dimension k ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-51|LADR 6.51]]), so it is spanned by the independent ∇gᵢ.
- **Existence.** The method only finds candidates. If the constraint set is compact, a continuous f attains its max and min there ([[Heine–Borel Theorem]], [[Continuous Image of a Compact Space is Compact]]), so comparing values at the candidates finds them ([[§14 Optimization and Lagrange Multipliers#^rem-14-10|The Logical Flow]]).
- **Also in [[Calculus]]:** [[§97 Lagrange Multipliers#^thm-97-1|Calc Thm. §97.1]] (computational treatment with worked examples).
- **Also in [[Applied Linear Algebra]]:** [[§50★ Constrained Optimization#^thm-50-1|235 Thm. §50.1]] (the case of xᵀAx on the unit sphere, where the Lagrange condition is Ax = λx and the extremes are the extreme eigenvalues, with worked examples).
