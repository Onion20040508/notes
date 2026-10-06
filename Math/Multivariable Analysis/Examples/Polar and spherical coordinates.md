---
subject: math
type: example
source: "[[Multivariable Analysis]]"
tags: ["math452", "workhorse"]
---
The coordinate changes $x = r\cos\theta$, $y = r\sin\theta$ in the plane and $x = \rho\sin\phi\cos\theta$, $y = \rho\sin\phi\sin\theta$, $z = \rho\cos\phi$ in space (the angle names vary from section to section). They are the running example of a Jacobian ($r$ and $\rho^2\sin\phi$), of a pair of inverse maps with reciprocal Jacobians, and of a change of variables whose Jacobian vanishes at a point; they turn rotationally symmetric integrals and PDEs into one-variable problems. The angle $\theta$ has no continuous choice on all of $\mathbb{R}^2 \setminus \{0\}$: in MATH 590 this is the covering map $\mathbb{R} \to S^1$, $t \mapsto (\cos 2\pi t, \sin 2\pi t)$ ([[§24 Covering Spaces#^thm-24-2|Topology §24]]) and $\pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle]]), and in MATH 452 it is the [[Angle form on the punctured plane]]. Its uses in MATH 452:

- Cartesian to polar: the Jacobian is $1/r$ ([[§13 The Inverse Function Theorem#^ex-13-3|§13]])
- Polar to Cartesian: the Jacobian is $r$ ([[§13 The Inverse Function Theorem#^ex-13-4|§13]])
- The two Jacobians are reciprocal ([[§13 The Inverse Function Theorem#^rem-13-6|§13]])
- Area and volume elements in polar, cylindrical and spherical coordinates ([[§15a The Definition of the Integral#^rem-15-5|§15a]])
- Change of variables to polar coordinates ([[§15b Properties of the Integral#^thm-15-7|§15.7]])
- The factor $r$ is the Jacobian ([[§15b Properties of the Integral#^rem-15-9|§15b]])
- $dx\,dy = r\,dr\,d\theta$, although $J = 0$ at the origin ([[§15e Change of Variables on General Domains#^ex-15-4|§15.4]])
- Spherical coordinates: $dx\,dy\,dz = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$ ([[§15e Change of Variables on General Domains#^ex-15-6|§15.6]])
- The Gaussian integral $\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$ ([[§15e Change of Variables on General Domains#^ex-15-7|§15.7]])
- The Laplacian in spherical coordinates ([[§19 The Laplacian in Spherical Coordinates#^thm-19-1|§19]])
- The same formula in any orthogonal coordinates, via scale factors ([[§19 The Laplacian in Spherical Coordinates#^rem-19-3|§19]])
- Polar and spherical coordinates as parametrizations for the pullback ([[§22 The Algebra of Differential Forms#^rem-22-2|§22]])

## Cartesian to polar: the Jacobian is $1/r$
![[§13 The Inverse Function Theorem#^ex-13-3]]

## Polar to Cartesian: the Jacobian is $r$
![[§13 The Inverse Function Theorem#^ex-13-4]]

## The two Jacobians are reciprocal
![[§13 The Inverse Function Theorem#^rem-13-6]]

## Area and volume elements in polar, cylindrical and spherical coordinates
![[§15 Multivariable Integration#^rem-15-5]]

## Change of variables to polar coordinates
![[§15 Multivariable Integration#^thm-15-7]]

## The factor $r$ is the Jacobian
![[§15 Multivariable Integration#^rem-15-9]]

## $dx\,dy = r\,dr\,d\theta$, although $J = 0$ at the origin
![[§15 Multivariable Integration#^ex-15-4]]

## Spherical coordinates: $dx\,dy\,dz = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$
![[§15 Multivariable Integration#^ex-15-6]]

## The Gaussian integral $\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$
![[§15 Multivariable Integration#^ex-15-7]]

## The Laplacian in spherical coordinates
![[§19 The Laplacian in Spherical Coordinates#^thm-19-1]]

## The same formula in any orthogonal coordinates, via scale factors
![[§19 The Laplacian in Spherical Coordinates#^rem-19-3]]

## Polar and spherical coordinates as parametrizations for the pullback
![[§22 The Algebra of Differential Forms#^rem-22-2]]
