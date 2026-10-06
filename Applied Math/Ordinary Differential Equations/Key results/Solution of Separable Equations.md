---
subject: math
type: theorem
source: "[[Ordinary Differential Equations]]"
aliases: ["MATH 331 6.1", "separation of variables"]
tags: [ordinary-differential-equations, hub]
---
![[§6 Separable Differential Equations#^thm-6-1]]

## Treated in
- [[§6 Separable Differential Equations#^thm-6-1|Theorem §6.1: Solution of a Separable Equation]], in [[§6 Separable Differential Equations]]

## Its proof uses
- [[§6 Separable Differential Equations#^def-6-1|Definition §6.1: Separable Equation]]

## Used in (Ordinary Differential Equations)
- [[§7 Modeling with First-Order Differential Equations#^prop-7-3|Proposition §7.3: Velocity, Maximum Altitude and Escape Velocity]]
- [[§9 Autonomous Differential Equations and Population Dynamics#^prop-9-3|Proposition §9.3: Solution of the Logistic Equation]]

## Connections
- See also: [[§68 Separable Equations#^def-68-1|Calc Def. §68.1]] and [[§68 Separable Equations#^thm-68-1|Calc Thm. §68.1]] (Stewart's treatment, in the form $h(y)\,dy/dx = g(x)$) and its [[§68 Separable Equations#^rem-68-1|Calc Remark: Method — Solving a Separable Equation]].
- When does (16) actually define $y$ as a differentiable function of $x$? Put $F(x, y) = \int_{x_0}^{x} M + \int_{y_0}^{y} N$. Then $F_y = N(y)$, and if $N(y_0) \ne 0$ the [[§15 The Implicit Function Theorem#^thm-15-1|452 Thm. §15.1]] (Implicit Function Theorem) gives a unique differentiable $\phi$ near $x_0$ with $F(x, \phi(x)) = 0$ and $\phi' = -F_x/F_y = -M/N$, which is the equation $M(x) + N(y)\,dy/dx = 0$. Where $N(y) = 0$ the integral curve can have a vertical tangent, and the solution ends there ([[§6 Separable Differential Equations#^ex-6-1|Examples §6.1]] and [[§6 Separable Differential Equations#^ex-6-2|§6.2]]). The generalization to $M(x, y)\,dx + N(x, y)\,dy = 0$ is the exact equations of [[§11 Exact Differential Equations and Integrating Factors#^def-11-1|Definition §11.1]].
