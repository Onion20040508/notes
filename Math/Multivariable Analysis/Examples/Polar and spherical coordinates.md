---
subject: math
type: example
source: "[[Multivariable Analysis]]"
tags: ["math452", "workhorse"]
---
The coordinate changes $x = r\cos\theta$, $y = r\sin\theta$ in the plane and $x = \rho\sin\phi\cos\theta$, $y = \rho\sin\phi\sin\theta$, $z = \rho\cos\phi$ in space (the angle names vary from section to section). They are the running example of a Jacobian ($r$ and $\rho^2\sin\phi$), of a pair of inverse maps with reciprocal Jacobians, and of a change of variables whose Jacobian vanishes at a point; they turn rotationally symmetric integrals and PDEs into one-variable problems. The angle $\theta$ has no continuous choice on all of $\mathbb{R}^2 \setminus \{0\}$: in MATH 590 this is the covering map $\mathbb{R} \to S^1$, $t \mapsto (\cos 2\pi t, \sin 2\pi t)$ ([[§31 Covering Spaces#^thm-31-2|Topology §31]]) and $\pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle]]), and in MATH 452 it is the [[Angle form on the punctured plane]]. Its uses in MATH 452:

- Cartesian to polar: the Jacobian is $1/r$ ([[§16 The Inverse Function Theorem#^ex-16-3|§16]])
- Polar to Cartesian: the Jacobian is $r$ ([[§16 The Inverse Function Theorem#^ex-16-4|§16]])
- The two Jacobians are reciprocal ([[§16 The Inverse Function Theorem#^rem-16-6|§16]])
- Area and volume elements in polar, cylindrical and spherical coordinates ([[§21 The Definition of the Integral#^rem-21-5|§21]])
- Change of variables to polar coordinates ([[§22 Properties of the Integral#^thm-22-6|§22.6]])
- The factor $r$ is the Jacobian ([[§22 Properties of the Integral#^rem-22-9|§22]])
- $dx\,dy = r\,dr\,d\theta$, although $J = 0$ at the origin ([[§25 Change of Variables on General Domains#^ex-25-1|§25.1]])
- Spherical coordinates: $dx\,dy\,dz = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$ ([[§25 Change of Variables on General Domains#^ex-25-3|§25.3]])
- The Gaussian integral $\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$ ([[§25 Change of Variables on General Domains#^ex-25-4|§25.4]])
- The Laplacian in spherical coordinates ([[§33 The Laplacian in Spherical Coordinates#^thm-33-1|§33]])
- The same formula in any orthogonal coordinates, via scale factors ([[§33 The Laplacian in Spherical Coordinates#^rem-33-3|§33]])
- Polar and spherical coordinates as parametrizations for the pullback ([[§37 The Algebra of Differential Forms#^rem-37-2|§37]])

## Cartesian to polar: the Jacobian is $1/r$
![[§16 The Inverse Function Theorem#^ex-16-3]]

## Polar to Cartesian: the Jacobian is $r$
![[§16 The Inverse Function Theorem#^ex-16-4]]

## The two Jacobians are reciprocal
![[§16 The Inverse Function Theorem#^rem-16-6]]

## Area and volume elements in polar, cylindrical and spherical coordinates
![[§21 The Definition of the Integral#^rem-21-5]]

## Change of variables to polar coordinates
![[§22 Properties of the Integral#^thm-22-6]]

## The factor $r$ is the Jacobian
![[§22 Properties of the Integral#^rem-22-9]]

## $dx\,dy = r\,dr\,d\theta$, although $J = 0$ at the origin
![[§25 Change of Variables on General Domains#^ex-25-1]]

## Spherical coordinates: $dx\,dy\,dz = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$
![[§25 Change of Variables on General Domains#^ex-25-3]]

## The Gaussian integral $\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$
![[§25 Change of Variables on General Domains#^ex-25-4]]

## The Laplacian in spherical coordinates
![[§33 The Laplacian in Spherical Coordinates#^thm-33-1]]

## The same formula in any orthogonal coordinates, via scale factors
![[§33 The Laplacian in Spherical Coordinates#^rem-33-3]]

## Polar and spherical coordinates as parametrizations for the pullback
![[§37 The Algebra of Differential Forms#^rem-37-2]]
