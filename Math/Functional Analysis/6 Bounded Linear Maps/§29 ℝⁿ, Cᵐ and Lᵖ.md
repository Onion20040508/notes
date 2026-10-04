---
type: section
subject: "[[Functional Analysis]]"
chapter: 6
section: 29
tags: [functional-analysis, math556]
---
← [[§28 Sesquilinear Forms and the Lax–Milgram Theorem]] · ↑ [[· 6 Bounded Linear Maps]] · [[§30 Bras, Kets, and the Riesz Map]] →

*Stage: maps — Examples revisited. Which maps between the course's spaces are bounded, and the duals of $L^p$ and $\ell^2$.*

## ℝⁿ

Every linear map out of a finite-dimensional space is bounded, so on $\mathbb{R}^n$ boundedness is automatic; a bilinear form on $\mathbb{R}^n$ is a matrix, $B(x, y) = (x, Ay)$, the finite-dimensional model of [[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-28-1|bounded forms as operators]].

![[§26 Boundedness and Continuity#^prop-26-4]]

![[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^ex-28-1]]

*Chain:* ← [[§25 Sequence and Function Spaces|Chapter 5]]

## Cᵐ and C∞

Differentiation is the test case for boundedness. With the $C^m$ norm on the domain and the $C^{m-1}$ norm on the target it is bounded, with norm at most $1$; [[§26 Boundedness and Continuity#^rem-26-2|the remark after it]] relates the completeness of $C^1$ to [[§11 Completeness#^prop-11-7|Chapter 3]]. The proposition below states the case of $C^\infty(\overline{\Omega})$ with the maximum norm on both sides (homework; proof to be added after submission).

![[§26 Boundedness and Continuity#^ex-26-1]]

![[§26 Boundedness and Continuity#^prop-26-3]]

*Chain:* ← [[§25 Sequence and Function Spaces|Chapter 5]]

## Lᵖ, L² and ℓ²

The Fourier transform is a bounded map $L^1(\mathbb{R}^n) \to L^\infty(\mathbb{R}^n)$ with norm at most $1$. By the Riesz representation theorem, $(L^2)' = L^2$ and $(\ell^2)' = \ell^2$; this is a Hilbert-space phenomenon ([[§27 Dual Spaces#^rem-27-3|remark]]), and for $1 \le p < \infty$ the dual of $L^p$ is $L^{p'}$.

![[§26 Boundedness and Continuity#^ex-26-2]]

![[§27 Dual Spaces#^ex-27-1]]

![[§27 Dual Spaces#^thm-27-4]]

*Chain:* ← [[§25 Sequence and Function Spaces|Chapter 5]] · [[§32 Position Eigenstates and Continuous Resolutions#^thm-32-2|Chapter 7 (L² as a state space)]] →
