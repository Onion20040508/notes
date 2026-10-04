---
subject: math
type: theorem
source: "[[Complex Variables]]"
aliases: ["MAT 342 23.1"]
tags: [complex-variables, hub]
---
![[§23 Sufficient Conditions for Differentiability#^thm-23-1]]

## Treated in
- [[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1: Sufficient Conditions for Differentiability]], in [[§23 Sufficient Conditions for Differentiability]]

## Its proof uses
- [[§4 Vectors and Moduli#^prop-4-1|Proposition §4.1: Modulus and the Real and Imaginary Parts]]
- [[§19 Derivatives#^def-19-1|Definition §19.1: Derivative]]

## Its proof uses (other subjects)
- [[§29 The Mean Value Theorem#^thm-29-3|451 §29.3: Mean Value Theorem]]

## Used in (Complex Variables)
- [[§23 Sufficient Conditions for Differentiability#^cor-23-2|Corollary §23.2: Real Differentiability Plus Cauchy–Riemann]]
- [[§24★ Polar Coordinates#^prop-24-1|Proposition §24.1: Polar Form of the Cauchy–Riemann Equations]]
- [[§24★ Polar Coordinates#^thm-24-3|Theorem §24.3: Sufficient Conditions in Polar Coordinates]]
- [[§25 Analytic Functions#^ex-25-3|Example §25.3: Differentiable on a Line, Analytic Nowhere]]
- [[§26 Further Examples (Analytic Functions)#^ex-26-2|Example §26.2: sin x cosh y + i cos x sinh y]]
- [[§27★ Harmonic Functions#^ex-27-3|Example §27.3: An Entire Function with Given Real Part]]
- [[§29★ Reflection Principle#^thm-29-1|Theorem §29.1: Reflection Principle]]
- [[§30 The Exponential Function#^thm-30-3|Theorem §30.3: e^z Is Entire]]
- [[§30 The Exponential Function#^ex-30-4|Example §30.4: exp z̄ Is Nowhere Analytic, exp(z²) Is Entire]]
- [[§114★ Local Inverses#^thm-114-1|Theorem §114.1: Conformal Maps Have Local Inverses]]
- [[§115★ Harmonic Conjugates#^thm-115-1|Theorem §115.1: Analytic Functions and Harmonic Conjugates]]
- [[§115★ Harmonic Conjugates#^thm-115-4|Theorem §115.4: Existence of Harmonic Conjugates]]

## Connections
- Step 1 of the [[§23 Sufficient Conditions for Differentiability#^pf-23-1|proof of Theorem §23.1]] is the theorem that continuous partials imply differentiability, [[§6 Differentiability#^thm-6-2|452 Thm. §6.2]] (stated there for partials continuous on an open set; that proof needs continuity only at the point). Its equations (2)–(3) say that $u$ and $v$ are differentiable at $(x_0, y_0)$ in the sense of [[§6 Differentiability#^def-6-1|452 Def. §6.1]].
- With $f'(z_0) = a + ib$, the Cauchy–Riemann equations say that the Jacobian matrix of $(u, v)$ at $(x_0, y_0)$ is $\begin{bmatrix} u_x & u_y \\ v_x & v_y \end{bmatrix} = \begin{bmatrix} a & -b \\ b & a \end{bmatrix}$, a rotation–scaling matrix, [[§36 Complex Eigenvalues#^prop-36-3|235 Prop. §36.3]]: the linear part of $\Delta w$ is multiplication by $f'(z_0)$, a rotation through $\arg f'(z_0)$ followed by a stretch by $|f'(z_0)|$. This is the geometric content of complex differentiability, and the source of conformality in Ch. 9.
