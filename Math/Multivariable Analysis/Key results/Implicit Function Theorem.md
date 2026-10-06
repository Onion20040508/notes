---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 15.1", "IFT"]
tags: [multivariable-analysis, hub]
---
![[§15 The Implicit Function Theorem#^thm-15-1]]

## Treated in
- [[§15 The Implicit Function Theorem#^thm-15-1|Theorem §15.1: Implicit Function Theorem]], in [[§15 The Implicit Function Theorem]]

## Its proof uses
- [[§7 Differentiability#^thm-7-2|Theorem §7.2: Continuous Partials Imply Differentiability]]

## Its proof uses (other subjects)
- [[Intermediate Value Theorem]] (Single Variable Analysis)
- [[Mean Value Theorem]] (Single Variable Analysis)
- [[§29 The Mean Value Theorem#^cor-29-7|451 §29.7: Sign of the Derivative and Monotonicity]]
- [[§29 The Mean Value Theorem#^prop-29-8|451 §29.8: Mean Value Inequality (HW)]]

## Used in (Multivariable Analysis)
- [[§15 The Implicit Function Theorem#^ex-15-1|Example §15.1: Circle]]
- [[§15 The Implicit Function Theorem#^ex-15-2|Example §15.2: Where IFT Fails]]
- [[§17 Optimization and Lagrange Multipliers#^thm-17-2|Theorem §17.2: Method of Lagrange Multipliers]]

## Used in (Differentiable Manifolds)
- [[§7 The Regular Value Theorem#^thm-7-1|Theorem §7.1: Implicit Function Theorem — Lee Theorem C.40]]

## Connections
- **Proof idea.** F_y > 0 near the point makes F strictly increasing in y ([[§29 The Mean Value Theorem#^cor-29-7|451 §29.7]]). A sign change plus the [[Intermediate Value Theorem]] on each vertical slice gives a root, monotonicity makes it unique, and the [[Mean Value Theorem]] gives f′ = −F_x/F_y.
- **One-variable relative.** This parallels the 451 [[§29 The Mean Value Theorem#^thm-29-10|Inverse Function Theorem]] (§29.10), where f′ ≠ 0 gives a local inverse. The derivative formula is what implicit differentiation with the [[Multivariable Chain Rule]] predicts ([[§15 The Implicit Function Theorem#^rem-15-2|The Derivative Formula]]).
- **Where hypotheses matter.** At (1, 0) on the unit circle F_y = 0, and y is not a function of x there ([[§15 The Implicit Function Theorem#^ex-15-2|Where IFT Fails]]). Where F_x = F_y = 0 the curve may be singular ([[§15 The Implicit Function Theorem#^rem-15-1|Why F_y ≠ 0]]). For systems, F_y ≠ 0 is replaced by a nonzero Jacobian determinant ([[Invertible ⟺ nonzero determinant]], LADR 9.50).
- **Used for.** The [[§15 The Implicit Function Theorem#^thm-15-2|general case]] (§12.2) is applied twice to prove the [[Inverse Function Theorem (several variables)]]. It also derives the [[Method of Lagrange Multipliers]] and gives the [[§24 The Change of Variables Formula#^pf-24-2-2|second proof]] of the change of variables formula.
- **Several equations.** The vector-valued version, which 591 deduces from the inverse function theorem, is [[Implicit Function Theorem (vector-valued)]] (591 Thm. §7.1). It is what makes regular level sets manifolds, [[Regular Value Theorem (Euclidean)]] (591 Thm. §7.3).
- **Also in [[Calculus]]:** [[§110 The Chain Rule#^thm-110-6|Calc Thm. §110.6]] (computational treatment with worked examples).
