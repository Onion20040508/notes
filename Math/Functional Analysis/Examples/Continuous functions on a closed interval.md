---
subject: math
type: example
source: "[[Functional Analysis]]"
tags: ["math556", "workhorse"]
---
The space $C[a,b]$ of continuous functions $f : [a,b] \to \mathbb{F}$, the first function space of the course. With the supremum norm $\|f\|_\infty = \max_{[a,b]} |f|$ it is a Banach space; with the $L^p$ norm $\|f\|_p = \bigl(\int_a^b |f|^p\bigr)^{1/p}$, $1 \le p < \infty$, it is a normed space that is not complete, and its completion is $L^p[a,b]$. The two norms are not equivalent, so the one set gives two different normed spaces: the norm decides, not the set. It is the example to keep in mind for what the abstract construction of the completion does in practice, and $C^2[a,b]$ with a $C^1$ norm is a second instance of the same phenomenon. The completion for $p = 2$ is in [[L² function spaces]]. Its uses in MATH 556:

*Revisit sections:* [[§13 ℝⁿ, C［a,b］ and ℓᵖ|Chapter 3]] · [[§19 ℝⁿ, C［a,b］, ℓᵖ and Lᵖ|Chapter 4]] · [[§25 Sequence and Function Spaces|Chapter 5]] · [[§29 ℝⁿ, Cᵐ and Lᵖ|Chapter 6]]

- $C[a,b]$ with the supremum norm is a Banach space ([[§11 Completeness#^thm-11-1|§11]])
- Unlike for $\ell^p$, the candidate limit must be shown to lie in the space ([[§11 Completeness#^rem-11-1|§11]])
- $C[a,b]$ sits inside $L^p[a,b]$ via $f \mapsto [f]$ ([[§11 Completeness#^rem-11-7|§11]])
- The norm decides, not the set: $L^1[a,b]$ is not the completion of $(C[a,b], \|\cdot\|_\infty)$ ([[§11 Completeness#^rem-11-9|§11]])
- $C^2[a,b]$ with a $C^1$ norm ([[§11 Completeness#^ex-11-2|§11]])
- $(C^2[a,b], \|\cdot\|_X)$ is not complete, and its completion is $C^1[a,b]$ ([[§11 Completeness#^prop-11-7|§11]])
- $\|\cdot\|_\infty$ and $\|\cdot\|_{L^1}$ on $C[a,b]$ are not equivalent ([[§12 New Normed Spaces from Old#^rem-12-1|§12]])
- Continuous functions are not dense in $L^\infty$ ([[§17 The Function Spaces Lᵖ(Ω)#^prop-17-5|§17]])
- A continuous $h \ge 0$ with vanishing integral is identically $0$ ([[§17 The Function Spaces Lᵖ(Ω)#^lem-17-6|§17]])
- Hölder's inequality for continuous functions ([[§17 The Function Spaces Lᵖ(Ω)#^lem-17-7|§17]])
- $L^p[a,b]$ as the completion of $(C[a,b], \|\cdot\|_p)$ ([[§17 The Function Spaces Lᵖ(Ω)#^prop-17-8|§17]])
- Ramps converging to a step function: the completion is forced to contain discontinuous functions ([[§17 The Function Spaces Lᵖ(Ω)#^rem-17-4|§17]])
- In $\{f \in C[0,1] : f(0) = 0\}$ the constant $\theta = 1$ in Riesz's lemma cannot be attained ([[§18 Compactness and the Unit Ball#^prop-18-4|§18]])
- A sharp integral inequality on $C^2[a,b]$, from the $L^2$ inner product on $C[a,b]$ ([[§22 Projection and Orthogonal Decomposition#^prop-22-8|§22]])
- Differentiation is bounded from $C^m$ to $C^{m-1}$ ([[§26 Boundedness and Continuity#^ex-26-1|§26]])

## $C[a,b]$ with the supremum norm is a Banach space
![[§11 Completeness#^thm-11-1]]

## Unlike for $\ell^p$, the candidate limit must be shown to lie in the space
![[§11 Completeness#^rem-11-1]]

## $C[a,b]$ sits inside $L^p[a,b]$ via $f \mapsto [f]$
![[§11 Completeness#^rem-11-7]]

## The norm decides, not the set: $L^1[a,b]$ is not the completion of $(C[a,b], \|\cdot\|_\infty)$
![[§11 Completeness#^rem-11-9]]

## $C^2[a,b]$ with a $C^1$ norm
![[§11 Completeness#^ex-11-2]]

## $(C^2[a,b], \|\cdot\|_X)$ is not complete, and its completion is $C^1[a,b]$
![[§11 Completeness#^prop-11-7]]

## $\|\cdot\|_\infty$ and $\|\cdot\|_{L^1}$ on $C[a,b]$ are not equivalent
![[§12 New Normed Spaces from Old#^rem-12-1]]

## Continuous functions are not dense in $L^\infty$
![[§17 The Function Spaces Lᵖ(Ω)#^prop-17-5]]

## A continuous $h \ge 0$ with vanishing integral is identically $0$
![[§17 The Function Spaces Lᵖ(Ω)#^lem-17-6]]

## Hölder's inequality for continuous functions
![[§17 The Function Spaces Lᵖ(Ω)#^lem-17-7]]

## $L^p[a,b]$ as the completion of $(C[a,b], \|\cdot\|_p)$
![[§17 The Function Spaces Lᵖ(Ω)#^prop-17-8]]

## Ramps converging to a step function: the completion is forced to contain discontinuous functions
![[§17 The Function Spaces Lᵖ(Ω)#^rem-17-4]]

## In $\{f \in C[0,1] : f(0) = 0\}$ the constant $\theta = 1$ in Riesz's lemma cannot be attained
![[§18 Compactness and the Unit Ball#^prop-18-4]]

## A sharp integral inequality on $C^2[a,b]$, from the $L^2$ inner product on $C[a,b]$
![[§22 Projection and Orthogonal Decomposition#^prop-22-8]]

## Differentiation is bounded from $C^m$ to $C^{m-1}$
![[§26 Boundedness and Continuity#^ex-26-1]]
