---
type: section
subject: "[[Functional Analysis]]"
chapter: 6
section: 36
tags: [functional-analysis, math556]
---
← [[§35 Measures and the Radon–Nikodym Theorem]] · ↑ [[· 6 Bounded Linear Maps]] · [[§37 Bras, Kets, and the Riesz Map]] →

*Stage: maps — Examples revisited. Which maps between the course's spaces are bounded, and the duals of $L^p$ and $\ell^2$.*

## ℝⁿ

Every linear map out of a finite-dimensional space is bounded, so on $\mathbb{R}^n$ boundedness is automatic; a bilinear form on $\mathbb{R}^n$ is a matrix, $B(x, y) = (x, Ay)$, the finite-dimensional model of [[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-32-1|bounded forms as operators]].

![[§30 Boundedness and Continuity#^prop-30-4]]

![[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^ex-32-1]]

*Chain:* ← [[§29 Sequence and Function Spaces|Chapter 5]]

## Cᵐ and C∞

Differentiation is the test case for boundedness. With the $C^m$ norm on the domain and the $C^{m-1}$ norm on the target it is bounded, with norm at most $1$; [[§30 Boundedness and Continuity#^rem-30-2|the remark after it]] relates the completeness of $C^1$ to [[§13 The Completion of a Normed Space#^prop-13-4|Chapter 3]]. The proposition below states the case of $C^\infty(\overline{\Omega})$ with the maximum norm on both sides (homework; proof to be added after submission).

![[§30 Boundedness and Continuity#^ex-30-1]]

![[§30 Boundedness and Continuity#^prop-30-3]]

*Chain:* ← [[§29 Sequence and Function Spaces|Chapter 5]]

## Lᵖ, L² and ℓ²

The Fourier transform is a bounded map $L^1(\mathbb{R}^n) \to L^\infty(\mathbb{R}^n)$ with norm at most $1$. By the Riesz representation theorem, $(L^2)' = L^2$ and $(\ell^2)' = \ell^2$; this is a Hilbert-space phenomenon ([[§31 Dual Spaces#^rem-31-3|remark]]), and for $1 \le p < \infty$ the dual of $L^p$ is $L^{p'}$.

![[§30 Boundedness and Continuity#^ex-30-2]]

![[§31 Dual Spaces#^ex-31-1]]

![[§31 Dual Spaces#^thm-31-4]]

Lecture 12 used $L^2$ twice more. The [[§34 Weak Solutions of the Dirichlet Problem#^def-34-1|Dirichlet problem]] is solved in $H^1_0(\Omega)$, a [[§33 Sobolev Spaces and Weak Derivatives#^def-33-9|completion]] inside $L^2$, where the source term $f \in L^2(\Omega)$ gives the [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-1|bounded functional]] $v \mapsto \int_\Omega f v$ (Theorem [[§34 Weak Solutions of the Dirichlet Problem#^thm-34-2|§34.2]]); and the [[§35 Measures and the Radon–Nikodym Theorem#^thm-35-1|Radon–Nikodym theorem]] applies the [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-4|Riesz representation theorem]] in $L^2(\mu + \nu)$ for an abstract [[§35 Measures and the Radon–Nikodym Theorem#^def-35-3|measure]] (Theorem [[§35 Measures and the Radon–Nikodym Theorem#^thm-35-1|§35.1]]).

*Chain:* ← [[§29 Sequence and Function Spaces|Chapter 5]] · [[§39 Position Eigenstates and Continuous Resolutions#^thm-39-2|Chapter 7 (L² as a state space)]] →
