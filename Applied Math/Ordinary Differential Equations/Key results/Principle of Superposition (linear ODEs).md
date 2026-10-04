---
subject: math
type: theorem
source: "[[Ordinary Differential Equations]]"
aliases: ["MATH 331 14.2", "superposition"]
tags: [ordinary-differential-equations, hub]
---
![[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-2]]

## Treated in
- [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-2|Theorem §14.2: Principle of Superposition]], in [[§14 Solutions of Linear Homogeneous Equations; the Wronskian]]

## Its proof uses
- [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^def-14-1|Definition §14.1: The Differential Operator L]]

## Used in (Ordinary Differential Equations)
- [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-3|Theorem §14.3: Solvability of the Initial Conditions]]
- [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^cor-14-7|Corollary §14.7: The Conjugate of a Solution]]
- [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-1|Theorem §17.1: Difference of Two Solutions]]
- [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-2|Theorem §17.2: General Solution of the Nonhomogeneous Equation]]

## Connections
- The computation says that $L$ is a linear map, $L[c_1y_1 + c_2y_2] = c_1L[y_1] + c_2L[y_2]$, so the solution set of $L[y] = 0$ is its null space and hence a subspace: [[§8 Null Spaces and Ranges#^ladr-3-13|LADR 3.13]], [[§24 Null Spaces, Column Spaces, and Linear Transformations#^thm-24-5|235 Thm. §24.5]]. Lay's instance is $y'' + \omega^2y = 0$, [[§24 Null Spaces, Column Spaces, and Linear Transformations#^ex-24-5|235 Ex. §24.5]].
- The same principle for systems $\mathbf{x}' = A\mathbf{x}$: [[§38 Applications to Differential Equations#^prop-38-1|235 Prop. §38.1]].
- **Also in [[Fourier Series and PDEs]]:** [[§1★ Homogeneous Linear Equations#^thm-1-2|341 Thm. §1.2]] (the same principle in Powers' review of ODEs), and its PDE version [[§19 Example꞉ Fixed End Temperatures#^thm-19-4|341 Thm. §19.4]] (superposition of product solutions of the heat equation).
