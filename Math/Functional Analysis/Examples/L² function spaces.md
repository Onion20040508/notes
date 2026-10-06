---
subject: math
type: example
source: "[[Functional Analysis]]"
tags: ["math556", "workhorse"]
---
The spaces $L^2(\Omega)$ with $(f, g) = \int_\Omega f\,\overline{g}\,dx$, the direct continuum analogue of the $\mathbb{C}^n$ dot product; on an interval, $L^2[a,b]$ is the completion of the [[Continuous functions on a closed interval]] in the $L^2$ norm. They are the Hilbert spaces of functions that the course keeps returning to: $L^2[-1,1]$ splits orthogonally into even and odd functions, $L^2[0,2\pi]$ has the Fourier basis $e^{inx}/\sqrt{2\pi}$, and $L^2(\mathbb{R}^n)$ is the state space of the quantum-mechanics companion, separable but without position eigenvectors. As Wu stressed, measure theory supplies the examples of functional analysis: the Lebesgue theory of $L^p$ is in [[§34 Normed Linear Spaces and Lᵖ Spaces|551 §34]], and the sequence analogue $\ell^2$ is in [[Sequence spaces ℓᵖ]]. Its uses in MATH 556:

*Revisit sections:* [[§21 ℝⁿ, C［a,b］, ℓᵖ and Lᵖ|Chapter 4]] · [[§29 Sequence and Function Spaces|Chapter 5]] · [[§34 ℝⁿ, Cᵐ and Lᵖ|Chapter 6]]

- The $L^2$ inner product, convergent by Hölder's inequality ([[§22 Definition and Examples#^ex-22-3|§22]])
- $L^2(\Omega)$ is a Hilbert space ([[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-1|§23]])
- $C_c(\mathbb{R}^n)$ with the $L^2$ inner product is not complete; its completion is $L^2(\mathbb{R}^n)$ ([[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-2|§23]])
- Among the $L^p(\Omega)$, only $L^2$ has a norm coming from an inner product ([[§24 The Parallelogram Law and Jordan–von Neumann#^cor-24-3|§24]])
- Sobolev spaces: completing $C_c^\infty(\Omega)$ in $L^2$ norms of derivatives ([[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-3|§23]])
- Even and odd functions: $L^2[-1,1] = E \oplus O$ ([[§25 Projection and Orthogonal Decomposition#^prop-25-7|§25]])
- On $L^2$ every bounded linear functional is $f \mapsto \int f\,\bar{g}$ ([[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^rem-26-3|§26]])
- The Fourier basis of $L^2[0,2\pi]$ ([[§27 Orthonormal Sets and Bases#^thm-27-11|§27]])
- Fourier series converge in $L^2$, with Parseval's equality ([[§27 Orthonormal Sets and Bases#^rem-27-9|§27]])
- $L^p(E)$, in particular $L^2(E)$, is separable ([[§29 Sequence and Function Spaces#^prop-29-4|§29]])
- $(L^2)' = L^2$ by the Riesz representation theorem ([[§31 Dual Spaces#^ex-31-1|§31]])
- Parity on $L^2[-1,1]$: the simplest resolution of the identity ([[§36 The Completeness Relation#^ex-36-1|§36]])
- A particle on a ring: the Fourier basis as momentum eigenstates ([[§36 The Completeness Relation#^ex-36-2|§36]])
- $L^2(\mathbb{R}^n)$ is separable, and every orthonormal basis of it is countably infinite ([[§37 Position Eigenstates and Continuous Resolutions#^thm-37-2|§37]])
- Position has no eigenvectors in $L^2(\mathbb{R})$ ([[§37 Position Eigenstates and Continuous Resolutions#^prop-37-3|§37]])
- Point evaluation is not bounded in the $L^2$ norm ([[§37 Position Eigenstates and Continuous Resolutions#^prop-37-4|§37]])
- The spectral projections of position on $L^2(\mathbb{R}^n)$ ([[§37 Position Eigenstates and Continuous Resolutions#^prop-37-5|§37]])
- The bound states of hydrogen are not complete in $L^2(\mathbb{R}^3)$ ([[§38 Bound States Need Not Be Complete꞉ Hydrogen#^cor-38-2|§38]])

## The $L^2$ inner product, convergent by Hölder's inequality
![[§22 Definition and Examples#^ex-22-3]]

## $L^2(\Omega)$ is a Hilbert space
![[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-1]]

## $C_c(\mathbb{R}^n)$ with the $L^2$ inner product is not complete; its completion is $L^2(\mathbb{R}^n)$
![[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-2]]

## Among the $L^p(\Omega)$, only $L^2$ has a norm coming from an inner product
![[§24 The Parallelogram Law and Jordan–von Neumann#^cor-24-3]]

## Sobolev spaces: completing $C_c^\infty(\Omega)$ in $L^2$ norms of derivatives
![[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-3]]

## Even and odd functions: $L^2[-1,1] = E \oplus O$
![[§25 Projection and Orthogonal Decomposition#^prop-25-7]]

## On $L^2$ every bounded linear functional is $f \mapsto \int f\,\bar{g}$
![[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^rem-26-3]]

## The Fourier basis of $L^2[0,2\pi]$
![[§27 Orthonormal Sets and Bases#^thm-27-11]]

## Fourier series converge in $L^2$, with Parseval's equality
![[§27 Orthonormal Sets and Bases#^rem-27-9]]

## $L^p(E)$, in particular $L^2(E)$, is separable
![[§29 Sequence and Function Spaces#^prop-29-4]]

## $(L^2)' = L^2$ by the Riesz representation theorem
![[§31 Dual Spaces#^ex-31-1]]

## Parity on $L^2[-1,1]$: the simplest resolution of the identity
![[§36 The Completeness Relation#^ex-36-1]]

## A particle on a ring: the Fourier basis as momentum eigenstates
![[§36 The Completeness Relation#^ex-36-2]]

## $L^2(\mathbb{R}^n)$ is separable, and every orthonormal basis of it is countably infinite
![[§37 Position Eigenstates and Continuous Resolutions#^thm-37-2]]

## Position has no eigenvectors in $L^2(\mathbb{R})$
![[§37 Position Eigenstates and Continuous Resolutions#^prop-37-3]]

## Point evaluation is not bounded in the $L^2$ norm
![[§37 Position Eigenstates and Continuous Resolutions#^prop-37-4]]

## The spectral projections of position on $L^2(\mathbb{R}^n)$
![[§37 Position Eigenstates and Continuous Resolutions#^prop-37-5]]

## The bound states of hydrogen are not complete in $L^2(\mathbb{R}^3)$
![[§38 Bound States Need Not Be Complete꞉ Hydrogen#^cor-38-2]]
