---
subject: math
type: theorem
source: "[[Ordinary Differential Equations]]"
aliases: ["MATH 331 22.1"]
tags: [ordinary-differential-equations, hub]
---
![[§22 Solution of Initial Value Problems#^thm-22-1]]

## Treated in
- [[§22 Solution of Initial Value Problems#^thm-22-1|Theorem §22.1: Transform of a Derivative]], in [[§22 Solution of Initial Value Problems]]

## Its proof uses
- [[§21 Definition of the Laplace Transform#^thm-21-2|Theorem §21.2: Existence of the Laplace Transform]]
- [[§21 Definition of the Laplace Transform#^def-21-4|Definition §21.4: The Laplace Transform]]

## Its proof uses (other subjects)
- [[§44 Integration by Parts#^thm-44-1|Theorem §44.1: Integration by Parts]] (Calculus)

## Used in (Ordinary Differential Equations)
- [[§22 Solution of Initial Value Problems#^cor-22-2|Corollary §22.2: Transform of the nth Derivative]]
- [[§22 Solution of Initial Value Problems#^thm-22-6|Theorem §22.6: Table of Elementary Laplace Transforms]]
- [[§35★ Nonhomogeneous Linear Systems#^prop-35-5|Proposition §35.5: Transform of the Derivative of a Vector Function]]

## Connections
- Integration by parts with $f$ only piecewise smooth: [[§34 Fundamental Theorem of Calculus#^thm-34-3|451 Thm. §34.3]] requires $u, v$ continuous on $[t_i, t_{i+1}]$, differentiable inside, with integrable derivatives, which is exactly the situation on each piece.
- Continuity of $f$ is essential: if $f$ jumps at $t_i$, the boundary terms no longer cancel and each jump contributes $-e^{-st_i}\big(f(t_i^+) - f(t_i^-)\big)$; step functions are handled by the shift theorem [[§23 Step Functions#^thm-23-2|Theorem §23.2]] instead.
- **Also in [[Fourier Series and PDEs]]:** [[§51★ Definition and Elementary Properties#^thm-51-4|341 Thm. §51.4]] (the same rule), and its PDE version [[§53★ Partial Differential Equations#^thm-53-1|341 Thm. §53.1]] (transforms of partial derivatives, for heat and wave problems).
