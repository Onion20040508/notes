---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 12.1", "IFT"]
tags: [multivariable-analysis, hub]
---
![[§12 The Implicit Function Theorem#^thm-12-1]]

## Treated in
- [[§12 The Implicit Function Theorem#^thm-12-1|Theorem §12.1: Implicit Function Theorem]], in [[§12 The Implicit Function Theorem]]

## Its proof uses
- [[§6 Differentiability#^thm-6-2|Theorem §6.2: Continuous Partials Imply Differentiability]]

## Its proof uses (other subjects)
- [[Intermediate Value Theorem]] (Single Variable Analysis)
- [[Mean Value Theorem]] (Single Variable Analysis)
- [[§29 The Mean Value Theorem#^cor-29-7|451 §29.7: Sign of the Derivative and Monotonicity]]
- [[§29 The Mean Value Theorem#^prop-29-8|451 §29.8: Mean Value Inequality (HW)]]

## Used in (Multivariable Analysis)
- [[§12 The Implicit Function Theorem#^ex-12-1|Example §12.1: Circle]]
- [[§12 The Implicit Function Theorem#^ex-12-2|Example §12.2: Where IFT Fails]]
- [[§14 Optimization and Lagrange Multipliers#^thm-14-2|Theorem §14.2: Method of Lagrange Multipliers]]

## Connections
- **Proof idea.** F_y > 0 near the point makes F strictly increasing in y ([[§29 The Mean Value Theorem#^cor-29-7|451 §29.7]]). A sign change plus the [[Intermediate Value Theorem]] on each vertical slice gives a root, monotonicity makes it unique, and the [[Mean Value Theorem]] gives f′ = −F_x/F_y.
- **One-variable relative.** This parallels the 451 [[§29 The Mean Value Theorem#^thm-29-10|Inverse Function Theorem]] (§29.10), where f′ ≠ 0 gives a local inverse. The derivative formula is what implicit differentiation with the [[Multivariable Chain Rule]] predicts ([[§12 The Implicit Function Theorem#^rem-12-2|The Derivative Formula]]).
- **Where hypotheses matter.** At (1, 0) on the unit circle F_y = 0, and y is not a function of x there ([[§12 The Implicit Function Theorem#^ex-12-2|Where IFT Fails]]). Where F_x = F_y = 0 the curve may be singular ([[§12 The Implicit Function Theorem#^rem-12-1|Why F_y ≠ 0]]). For systems, F_y ≠ 0 is replaced by a nonzero Jacobian determinant ([[Invertible ⟺ nonzero determinant]], LADR 9.50).
- **Used for.** The [[§12 The Implicit Function Theorem#^thm-12-2|general case]] (§12.2) is applied twice to prove the [[Inverse Function Theorem (several variables)]]. It also derives the [[Method of Lagrange Multipliers]] and gives the [[§15 Multivariable Integration#^pf-15-14-2|second proof]] of the change of variables formula.
