---
subject: math
type: theorem
source: "[[Ordinary Differential Equations]]"
aliases: ["MATH 331 27.1"]
tags: [ordinary-differential-equations, hub]
---
![[§27 Solution of Initial Value Problems#^thm-27-1]]

## Treated in
- [[§27 Solution of Initial Value Problems#^thm-27-1|Theorem §27.1: Transform of a Derivative]], in [[§27 Solution of Initial Value Problems]]

## Its proof uses
- [[§26 Definition of the Laplace Transform#^thm-26-2|Theorem §26.2: Existence of the Laplace Transform]]
- [[§26 Definition of the Laplace Transform#^def-26-4|Definition §26.4: The Laplace Transform]]

## Used in (Ordinary Differential Equations)
- [[§27 Solution of Initial Value Problems#^cor-27-2|Corollary §27.2: Transform of the nth Derivative]]
- [[§27 Solution of Initial Value Problems#^thm-27-6|Theorem §27.6: Table of Elementary Laplace Transforms]]
- [[§41★ Nonhomogeneous Linear Systems#^prop-41-5|Proposition §41.5: Transform of the Derivative of a Vector Function]]

## Connections
- Integration by parts with $f$ only piecewise smooth: [[§34 Fundamental Theorem of Calculus#^thm-34-3|451 Thm. §34.3]] requires $u, v$ continuous on $[t_i, t_{i+1}]$, differentiable inside, with integrable derivatives, which is exactly the situation on each piece between consecutive discontinuities $t_i$ of $f'$ in the proof ([[§27 Solution of Initial Value Problems#^pf-27-1|§27]]).
- Continuity of $f$ is essential: if $f$ jumps at $t_i$, the boundary terms no longer cancel and each jump contributes $-e^{-st_i}\big(f(t_i^+) - f(t_i^-)\big)$; step functions are handled by the shift theorem [[§28 Step Functions#^thm-28-2|Theorem §28.2]] instead.
- **Also in [[Fourier Series and PDEs]]:** [[§64★ Definition and Elementary Properties#^thm-64-4|341 Thm. §64.4]] (the same rule), and its PDE version [[§66★ Partial Differential Equations#^thm-66-1|341 Thm. §66.1]] (transforms of partial derivatives, for heat and wave problems).
