---
subject: math
type: theorem
source: "[[Ordinary Differential Equations]]"
aliases: ["MATH 331 5.1", "separation of variables"]
tags: [ordinary-differential-equations, hub]
---
![[§5 Separable Differential Equations#^thm-5-1]]

## Treated in
- [[§5 Separable Differential Equations#^thm-5-1|Theorem §5.1: Solution of a Separable Equation]], in [[§5 Separable Differential Equations]]

## Its proof uses
- [[§5 Separable Differential Equations#^def-5-1|Definition §5.1: Separable Equation]]

## Used in (Ordinary Differential Equations)
- [[§6 Modeling with First-Order Differential Equations#^prop-6-3|Proposition §6.3: Velocity, Maximum Altitude and Escape Velocity]]
- [[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-3|Proposition §8.3: Solution of the Logistic Equation]]
- [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-8|Theorem §14.8: Abel's Theorem]]

## Connections
- See also: [[§59 Separable Equations#^def-59-1|Calc Def. §59.1]] and [[§59 Separable Equations#^thm-59-1|Calc Thm. §59.1]] (Stewart's treatment, in the form $h(y)\,dy/dx = g(x)$) and its [[§59 Separable Equations#^rem-59-1|Remark: Method]].
- When does (16) actually define $y$ as a differentiable function of $x$? Put $F(x, y) = \int_{x_0}^{x} M + \int_{y_0}^{y} N$. Then $F_y = N(y)$, and if $N(y_0) \ne 0$ the [[§12 The Implicit Function Theorem#^thm-12-1|452 Thm. §12.1]] (Implicit Function Theorem) gives a unique differentiable $\phi$ near $x_0$ with $F(x, \phi(x)) = 0$ and $\phi' = -F_x/F_y = -M/N$, which is (4). Where $N(y) = 0$ the integral curve can have a vertical tangent, and the solution ends there (Examples §5.1 and §5.2). The generalization to $M(x, y)\,dx + N(x, y)\,dy = 0$ is the exact equations of [[§9 Exact Differential Equations and Integrating Factors#^def-9-1|Definition §9.1]].
