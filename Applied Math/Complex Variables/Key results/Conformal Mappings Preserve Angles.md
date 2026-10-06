---
subject: math
type: theorem
source: "[[Complex Variables]]"
aliases: ["MAT 342 112.1", "conformal map"]
tags: [complex-variables, hub]
---
![[§112★ Preservation of Angles and Scale Factors#^thm-112-1]]

## Treated in
- [[§112★ Preservation of Angles and Scale Factors#^thm-112-1|Theorem §112.1: Directions Are Rotated by arg f′(z₀); Angles Are Preserved]], in [[§112★ Preservation of Angles and Scale Factors]]

## Its proof uses
- [[§9 Arguments of Products and Quotients#^thm-9-1|Theorem §9.1: The Argument of a Product]]
- [[§43 Contours#^def-43-4|Definition §43.4: Smooth Arc; Unit Tangent]]
- [[§43 Contours#^prop-43-5|Proposition §43.5: Chain Rule Along an Arc]]
- [[§112★ Preservation of Angles and Scale Factors#^def-112-1|Definition §112.1: Angle of Rotation]]

## Used in (Complex Variables)
- [[§117★ Transformations of Boundary Conditions#^lem-117-1|Lemma §117.1: Gradients and Directional Derivatives Are Scaled by ∣f′(z)∣]]
- [[§117★ Transformations of Boundary Conditions#^thm-117-2|Theorem §117.2: Constant Values and Zero Normal Derivatives Are Preserved]]
- [[§127★ Mapping the Real Axis onto a Polygon#^prop-127-1|Proposition §127.1: Constant Argument Gives a Straight Image]]

## Connections
- Why it works, in matrix form: by the Cauchy–Riemann equations the Jacobian matrix of $(x, y) \mapsto (u, v)$ at $z_0$ is $\begin{bmatrix} u_x & -v_x \\ v_x & u_x \end{bmatrix}$ with $u_x + iv_x = f'(z_0)$, a rotation–scaling matrix: rotation through $\arg f'(z_0)$ followed by scaling by $|f'(z_0)|$, [[§36 Complex Eigenvalues#^prop-36-3|235 Prop. §36.3]]. A linear map of that form preserves angles; the tangent vector $z'(t_0)$ is carried to $w'(t_0)$ by this matrix ([[§13 The Inverse Function Theorem#^def-13-1|452 Def. §13.1]], the Jacobian).
