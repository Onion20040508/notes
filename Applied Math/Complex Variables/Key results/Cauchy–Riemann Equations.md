---
subject: math
type: theorem
source: "[[Complex Variables]]"
aliases: ["MAT 342 21.1", "Cauchy–Riemann"]
tags: [complex-variables, hub]
---
![[§21 Cauchy–Riemann Equations#^thm-21-1]]

## Treated in
- [[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1: Cauchy–Riemann Equations Are Necessary]], in [[§21 Cauchy–Riemann Equations]]

## Its proof uses
- [[§15 Limits#^thm-15-1|Theorem §15.1: Uniqueness of Limits]]
- [[§15 Limits#^cor-15-2|Corollary §15.2: Two-Path Test]]
- [[§16 Theorems on Limits#^thm-16-1|Theorem §16.1: Limits of the Real and Imaginary Parts]]
- [[§19 Derivatives#^def-19-1|Definition §19.1: Derivative]]

## Used in (Complex Variables)
- [[§24★ Polar Coordinates#^prop-24-2|Proposition §24.2: The Derivative in Polar Form]]
- [[§25 Analytic Functions#^thm-25-3|Theorem §25.3: Zero Derivative on a Domain]]
- [[§26 Further Examples (Analytic Functions)#^ex-26-3|Example §26.3: f and Its Conjugate Both Analytic]]
- [[§26 Further Examples (Analytic Functions)#^ex-26-5|Example §26.5: Real-Valued Analytic Functions Are Constant]]
- [[§27★ Harmonic Functions#^thm-27-1|Theorem §27.1: Real and Imaginary Parts Are Harmonic]]
- [[§29★ Reflection Principle#^thm-29-1|Theorem §29.1: Reflection Principle]]
- [[§30 The Exponential Function#^ex-30-4|Example §30.4: exp z̄ Is Nowhere Analytic, exp(z²) Is Entire]]
- [[§37 The Trigonometric Functions sin z and cos z#^prop-37-5|Proposition §37.5: Components of sin z and cos z]]
- [[§43 Contours#^prop-43-5|Proposition §43.5: Chain Rule Along an Arc]]
- [[§50 Cauchy–Goursat Theorem#^thm-50-2|Theorem §50.2: Cauchy's Theorem (f′ Continuous)]]
- [[§57 Some Consequences of the Extension#^cor-57-2|Corollary §57.2: Partial Derivatives of All Orders]]
- [[§114★ Local Inverses#^thm-114-1|Theorem §114.1: Conformal Maps Have Local Inverses]]
- [[§115★ Harmonic Conjugates#^thm-115-1|Theorem §115.1: Analytic Functions and Harmonic Conjugates]]
- [[§115★ Harmonic Conjugates#^prop-115-2|Proposition §115.2: Harmonic Conjugates Differ by a Constant]]
- [[§116★ Transformations of Harmonic Functions#^prop-116-2|Proposition §116.2: The Laplacian Under an Analytic Change of Variables]]
- [[§117★ Transformations of Boundary Conditions#^lem-117-1|Lemma §117.1: Gradients and Directional Derivatives Are Scaled by ∣f′(z)∣]]
- [[§118★ Steady Temperatures#^prop-118-2|Proposition §118.2: Heat Flows Along the Lines of Flow]]
- [[§122★ Electrostatic Potential#^prop-122-2|Proposition §122.2: Conductors Are Equipotentials; Flux Lines Follow the Field]]
- [[§125★ The Stream Function#^prop-125-1|Proposition §125.1: Velocity from the Complex Potential]]

## Connections
- In the language of multivariable calculus: if $f'(z_0) = a + ib$ exists, then $f(z_0 + \Delta z) - f(z_0) = (a + ib)\Delta z + o(|\Delta z|)$, so the map $(x, y) \mapsto (u, v)$ is differentiable at $(x_0, y_0)$ in the sense of [[§6 Differentiability#^def-6-1|452 Def. §6.1]], with Jacobian matrix ([[§13 The Inverse Function Theorem#^def-13-1|452 Def. §13.1]])

  $$
  \begin{pmatrix} u_x & u_y \\ v_x & v_y \end{pmatrix} = \begin{pmatrix} a & -b \\ b & a \end{pmatrix} .
  $$

  The Cauchy–Riemann equations say exactly that the Jacobian is a rotation–scaling matrix, [[§36 Complex Eigenvalues#^prop-36-3|235 Prop. §36.3]]: the derivative acts on small displacements as multiplication by the complex number $f'(z_0)$. The converse (real differentiability plus the Cauchy–Riemann equations imply complex differentiability) is the content of §23 ([[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]], hub: [[Sufficient Conditions for Complex Differentiability]]), where continuity of the partials supplies real differentiability through [[§6 Differentiability#^thm-6-2|452 Thm. §6.2]].
