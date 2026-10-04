---
subject: math
type: example
source: "[[Functional Analysis]]"
tags: ["math556", "workhorse"]
---
The spaces $L^2(\Omega)$ with $(f, g) = \int_\Omega f\,\overline{g}\,dx$, the direct continuum analogue of the $\mathbb{C}^n$ dot product; on an interval, $L^2[a,b]$ is the completion of the [[Continuous functions on a closed interval]] in the $L^2$ norm. They are the Hilbert spaces of functions that the course keeps returning to: $L^2[-1,1]$ splits orthogonally into even and odd functions, $L^2[0,2\pi]$ has the Fourier basis $e^{inx}/\sqrt{2\pi}$, and $L^2(\mathbb{R}^n)$ is the state space of the quantum-mechanics companion, separable but without position eigenvectors. As Wu stressed, measure theory supplies the examples of functional analysis: the Lebesgue theory of $L^p$ is in [[§19 Normed Linear Spaces and Lᵖ Spaces|551 §19]], and the sequence analogue $\ell^2$ is in [[Sequence spaces ℓᵖ]]. Its uses in MATH 556:

*Revisit sections:* [[§19 ℝⁿ, C［a,b］, ℓᵖ and Lᵖ|Chapter 4]] · [[§25 Sequence and Function Spaces|Chapter 5]] · [[§29 ℝⁿ, Cᵐ and Lᵖ|Chapter 6]]

- The $L^2$ inner product, convergent by Hölder's inequality ([[§20 Definition and Examples#^ex-20-3|§20]])
- $L^2(\Omega)$ is a Hilbert space ([[§21 Cauchy–Schwarz and the Induced Norm#^ex-21-1|§21]])
- $C_c(\mathbb{R}^n)$ with the $L^2$ inner product is not complete; its completion is $L^2(\mathbb{R}^n)$ ([[§21 Cauchy–Schwarz and the Induced Norm#^ex-21-2|§21]])
- Among the $L^p(\Omega)$, only $L^2$ has a norm coming from an inner product ([[§21 Cauchy–Schwarz and the Induced Norm#^cor-21-5|§21]])
- Sobolev spaces: completing $C_c^\infty(\Omega)$ in $L^2$ norms of derivatives ([[§21 Cauchy–Schwarz and the Induced Norm#^ex-21-3|§21]])
- Even and odd functions: $L^2[-1,1] = E \oplus O$ ([[§22 Projection and Orthogonal Decomposition#^prop-22-7|§22]])
- On $L^2$ every bounded linear functional is $f \mapsto \int f\,\bar{g}$ ([[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^rem-23-2|§23]])
- The Fourier basis of $L^2[0,2\pi]$ ([[§24 Orthonormal Sets and Bases#^thm-24-11|§24]])
- Fourier series converge in $L^2$, with Parseval's equality ([[§24 Orthonormal Sets and Bases#^rem-24-9|§24]])
- $L^p(E)$, in particular $L^2(E)$, is separable ([[§25 Sequence and Function Spaces#^prop-25-4|§25]])
- $(L^2)' = L^2$ by the Riesz representation theorem ([[§27 Dual Spaces#^ex-27-1|§27]])
- Parity on $L^2[-1,1]$: the simplest resolution of the identity ([[§31 The Completeness Relation#^ex-31-1|§31]])
- A particle on a ring: the Fourier basis as momentum eigenstates ([[§31 The Completeness Relation#^ex-31-2|§31]])
- $L^2(\mathbb{R}^n)$ is separable, and every orthonormal basis of it is countably infinite ([[§32 Position Eigenstates and Continuous Resolutions#^thm-32-2|§32]])
- Position has no eigenvectors in $L^2(\mathbb{R})$ ([[§32 Position Eigenstates and Continuous Resolutions#^prop-32-3|§32]])
- Point evaluation is not bounded in the $L^2$ norm ([[§32 Position Eigenstates and Continuous Resolutions#^prop-32-4|§32]])
- The spectral projections of position on $L^2(\mathbb{R}^n)$ ([[§32 Position Eigenstates and Continuous Resolutions#^prop-32-5|§32]])
- The bound states of hydrogen are not complete in $L^2(\mathbb{R}^3)$ ([[§33 Bound States Need Not Be Complete꞉ Hydrogen#^cor-33-2|§33]])

## The $L^2$ inner product, convergent by Hölder's inequality
![[§20 Definition and Examples#^ex-20-3]]

## $L^2(\Omega)$ is a Hilbert space
![[§21 Cauchy–Schwarz and the Induced Norm#^ex-21-1]]

## $C_c(\mathbb{R}^n)$ with the $L^2$ inner product is not complete; its completion is $L^2(\mathbb{R}^n)$
![[§21 Cauchy–Schwarz and the Induced Norm#^ex-21-2]]

## Among the $L^p(\Omega)$, only $L^2$ has a norm coming from an inner product
![[§21 Cauchy–Schwarz and the Induced Norm#^cor-21-5]]

## Sobolev spaces: completing $C_c^\infty(\Omega)$ in $L^2$ norms of derivatives
![[§21 Cauchy–Schwarz and the Induced Norm#^ex-21-3]]

## Even and odd functions: $L^2[-1,1] = E \oplus O$
![[§22 Projection and Orthogonal Decomposition#^prop-22-7]]

## On $L^2$ every bounded linear functional is $f \mapsto \int f\,\bar{g}$
![[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^rem-23-2]]

## The Fourier basis of $L^2[0,2\pi]$
![[§24 Orthonormal Sets and Bases#^thm-24-11]]

## Fourier series converge in $L^2$, with Parseval's equality
![[§24 Orthonormal Sets and Bases#^rem-24-9]]

## $L^p(E)$, in particular $L^2(E)$, is separable
![[§25 Sequence and Function Spaces#^prop-25-4]]

## $(L^2)' = L^2$ by the Riesz representation theorem
![[§27 Dual Spaces#^ex-27-1]]

## Parity on $L^2[-1,1]$: the simplest resolution of the identity
![[§31 The Completeness Relation#^ex-31-1]]

## A particle on a ring: the Fourier basis as momentum eigenstates
![[§31 The Completeness Relation#^ex-31-2]]

## $L^2(\mathbb{R}^n)$ is separable, and every orthonormal basis of it is countably infinite
![[§32 Position Eigenstates and Continuous Resolutions#^thm-32-2]]

## Position has no eigenvectors in $L^2(\mathbb{R})$
![[§32 Position Eigenstates and Continuous Resolutions#^prop-32-3]]

## Point evaluation is not bounded in the $L^2$ norm
![[§32 Position Eigenstates and Continuous Resolutions#^prop-32-4]]

## The spectral projections of position on $L^2(\mathbb{R}^n)$
![[§32 Position Eigenstates and Continuous Resolutions#^prop-32-5]]

## The bound states of hydrogen are not complete in $L^2(\mathbb{R}^3)$
![[§33 Bound States Need Not Be Complete꞉ Hydrogen#^cor-33-2]]
